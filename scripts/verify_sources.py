#!/usr/bin/env python3
"""verify_sources.py — repo-agnostic link-liveness verifier.

Turns an ad-hoc "are my source links still alive?" check into a repeatable,
config-driven workflow. Works for any catalog that is "a list of entries, each
with one or more URL fields" — e.g. a funding catalogue (``catalog.json`` →
``quelle``) or a paper corpus (``papers.yaml`` → ``url``/``code_url``/``project_url``).

Two-stage check (the second stage only runs when needed):
  1) HTTP (requests):  classify each URL as OK / BROKEN / UNCERTAIN.
  2) Browser (Playwright, optional, --browser):  re-check UNCERTAIN URLs.
       2xx/3xx → OK       404/410 → BROKEN
       401/403  → BOTBLOCK (warn, never fails)   other → BROKEN

UNCERTAIN without a browser (e.g. in CI) is reported as BOTBLOCK (warn), so the
pipeline stays stable while still catching *definitively* dead links (404/410,
5xx, connection errors). This is deliberate: 403/Cloudflare blocks on official
portals (ec.europa.eu, DAAD, NIH, HFSP, …) are not broken links.

Config (JSON or YAML). Paths are resolved relative to the config file.

    inputs:
      - file: catalog.json
        format: json                 # json | yaml (inferred from extension)
        list_key: programme          # key holding the list (omit for object-map)
        id_field: id                # stable id (fallback: "<file>#<idx>")
        url_fields: [quelle]        # URL fields to check (empty strings skipped)
      - file: sources.json
        object_map: true            # iterate dict *values*; id from the key
        id_field: key
        url_fields: [url]
    settings:
      timeout: 20
      workers: 12
      user_agent: "Mozilla/5.0 (...) Chrome/126.0.0.0 Safari/537.36"
      browser: false                # enable Playwright recheck of UNCERTAIN
      fail_on_broken: true          # exit 1 if any BROKEN remains
      report: verify-sources-report.json

Usage:
    verify_sources.py CONFIG.yaml
    verify_sources.py CONFIG.json --browser --no-fail

Exit code: 0 if no BROKEN (after browser recheck), else 1 (when fail_on_broken).
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from typing import Any

import time

DEFAULT_UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
)


# --------------------------------------------------------------------------- IO
def load_config(path: str) -> dict:
    if path.endswith((".yaml", ".yml")):
        import yaml  # lazy: only needed for YAML configs

        return yaml.safe_load(open(path, encoding="utf-8"))
    return json.load(open(path, encoding="utf-8"))


def read_data(path: str, fmt: str | None) -> Any:
    fmt = fmt or ("yaml" if path.endswith((".yaml", ".yml")) else "json")
    if fmt == "yaml":
        import yaml

        return yaml.safe_load(open(path, encoding="utf-8"))
    return json.load(open(path, encoding="utf-8"))


def _resolve(base: str, path: str) -> str:
    return path if os.path.isabs(path) else os.path.join(base, path)


def iter_entries(inp: dict, base: str):
    """Yield (id, url, field, source_label) for every URL in an input spec."""
    fmt = inp.get("format")
    data = read_data(_resolve(base, inp["file"]), fmt)
    url_fields = inp.get("url_fields") or ["url"]
    id_field = inp.get("id_field", "id")
    label = inp["file"]
    if inp.get("object_map"):
        for k, it in data.items():
            if not isinstance(it, dict):
                continue
            for uf in url_fields:
                u = it.get(uf)
                if u:
                    yield (k, u, uf, label)
    else:
        items = data[inp["list_key"]] if inp.get("list_key") else data
        for idx, it in enumerate(items):
            if not isinstance(it, dict):
                continue
            eid = it.get(id_field) or f"{label}#{idx}"
            for uf in url_fields:
                u = it.get(uf)
                if u:
                    yield (eid, u, uf, label)


# --------------------------------------------------------------------- checking
@dataclass
class Result:
    source: str
    id: str
    field: str
    url: str
    http_status: int | None
    http_kind: str  # ok | broken | uncertain
    browser_kind: str | None = None  # ok | broken | botblock | None
    verdict: str = "botblock"
    note: str = ""

    def to_dict(self) -> dict:
        return {
            "source": self.source,
            "id": self.id,
            "field": self.field,
            "url": self.url,
            "http_status": self.http_status,
            "http_kind": self.http_kind,
            "browser_kind": self.browser_kind,
            "verdict": self.verdict,
            "note": self.note,
        }


def http_check(url: str, timeout: int, ua: str) -> dict:
    import requests  # lazy: only when actually checking

    last: dict | None = None
    for attempt in range(3):
        try:
            r = requests.get(
                url, headers={"User-Agent": ua}, timeout=timeout,
                allow_redirects=True, verify=True,
            )
            s = r.status_code
            if 200 <= s < 400:
                return {"status": s, "kind": "ok", "note": ""}
            if s in (401, 403):
                return {"status": s, "kind": "uncertain", "note": f"bot-block likely ({s})"}
            if s == 429:  # rate-limited by bulk CI scan: transient, NOT a dead link
                if attempt < 2:
                    time.sleep(1.5 * (attempt + 1)); continue
                return {"status": s, "kind": "uncertain", "note": "rate-limited (429)"}
            if s in (400, 404, 405, 406, 410):
                return {"status": s, "kind": "broken", "note": f"HTTP {s}"}
            if 500 <= s < 600:  # transient server error -> one retry
                if attempt < 2:
                    time.sleep(1.5 * (attempt + 1)); continue
                return {"status": s, "kind": "broken", "note": f"server error {s}"}
            return {"status": s, "kind": "broken", "note": f"HTTP {s}"}
        except requests.exceptions.SSLError:
            return {"status": None, "kind": "uncertain", "note": "SSL error"}
        except requests.exceptions.Timeout:
            return {"status": None, "kind": "uncertain", "note": "timeout"}
        except requests.exceptions.ConnectionError:
            return {"status": None, "kind": "broken", "note": "connection error"}
        except Exception as e:  # noqa: BLE001 - classify everything else as uncertain
            return {"status": None, "kind": "uncertain", "note": type(e).__name__}
    return last or {"status": None, "kind": "uncertain", "note": "unknown"}


def browser_check(url: str, ua: str) -> dict:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return {"kind": "uncertain", "note": "playwright not installed"}
    try:
        with sync_playwright() as p:
            b = p.chromium.launch(args=["--no-sandbox"])
            pg = b.new_page(user_agent=ua)
            r = pg.goto(url, wait_until="domcontentloaded", timeout=60000)
            pg.wait_for_timeout(2000)
            s = r.status if r else None
            b.close()
        if s and 200 <= s < 400:
            return {"kind": "ok", "note": f"browser {s}"}
        if s in (404, 410):
            return {"kind": "broken", "note": f"browser {s}"}
        if s in (401, 403):
            return {"kind": "botblock", "note": f"browser {s} (valid official URL)"}
        return {"kind": "broken", "note": f"browser {s}"}
    except Exception as e:  # noqa: BLE001
        return {"kind": "uncertain", "note": f"browser err: {type(e).__name__}"}


def resolve_verdict(http_kind: str, browser_kind: str | None) -> str:
    if http_kind == "ok":
        return "ok"
    if http_kind == "broken":
        return "broken"
    # http_kind == "uncertain"
    if browser_kind in ("ok", "broken", "botblock"):
        return browser_kind
    return "botblock"


# ------------------------------------------------------------------------- run
def run(config: dict, cfg_path: str = "") -> tuple[Counter, list[Result], int]:
    base = os.path.dirname(os.path.abspath(cfg_path)) if cfg_path else os.getcwd()
    settings = config.get("settings", {})
    timeout = int(settings.get("timeout", 20))
    workers = int(settings.get("workers", 12))
    ua = settings.get("user_agent", DEFAULT_UA)
    use_browser = bool(settings.get("browser", False))

    items = [i for inp in config.get("inputs", []) for i in iter_entries(inp, base)]

    def check_one(item):
        eid, url, field, label = item
        h = http_check(url, timeout, ua)
        b = None
        if h["kind"] == "uncertain":
            if use_browser:
                b = browser_check(url, ua)
            else:
                b = {"kind": "botblock",
                     "note": "no browser recheck; 401/403/timeout -> bot-block (warn)"}
        verdict = resolve_verdict(h["kind"], (b or {}).get("kind"))
        res = Result(
            source=label, id=eid, field=field, url=url,
            http_status=h["status"], http_kind=h["kind"],
            browser_kind=(b or {}).get("kind"),
            verdict=verdict,
            note=(b or {}).get("note") or h["note"],
        )
        return res

    results: list[Result] = []
    with ThreadPoolExecutor(max_workers=workers) as ex:
        for res in ex.map(check_one, items):
            results.append(res)

    totals = Counter(r.verdict for r in results)
    broken = totals.get("broken", 0)
    status = 0 if broken == 0 or not settings.get("fail_on_broken", True) else 1
    return totals, results, status


def render_summary(totals: Counter, results: list[Result]) -> str:
    lines = [
        "## verify-sources report",
        "",
        f"- OK: {totals.get('ok', 0)}  "
        f"bot-block (warn): {totals.get('botblock', 0)}  "
        f"**BROKEN: {totals.get('broken', 0)}**",
        "",
    ]
    broken = [r for r in results if r.verdict == "broken"]
    if broken:
        lines.append("### Broken links")
        for r in broken:
            lines.append(f"- [{r.source}] `{r.id}` ({r.field}): {r.url} — {r.note}")
        lines.append("")
    bot = [r for r in results if r.verdict == "botblock"]
    if bot:
        lines.append(f"### Bot-blocked / unverified ({len(bot)}) — valid URLs, script-blocked")
        for r in bot[:25]:
            lines.append(f"- [{r.source}] `{r.id}` ({r.field}): {r.url}")
        if len(bot) > 25:
            lines.append(f"- … and {len(bot) - 25} more")
        lines.append("")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Repo-agnostic link-liveness verifier.")
    ap.add_argument("config", help="verify-sources config (JSON or YAML)")
    ap.add_argument("--browser", dest="browser", action="store_true", default=None,
                    help="enable Playwright recheck of uncertain URLs")
    ap.add_argument("--no-browser", dest="browser", action="store_false")
    ap.add_argument("--fail", dest="fail", action="store_true", default=None)
    ap.add_argument("--no-fail", dest="fail", action="store_false")
    ap.add_argument("--report", default=None, help="override report output path")
    args = ap.parse_args(argv)

    config = load_config(args.config)
    # CLI overrides
    config.setdefault("settings", {})
    if args.browser is not None:
        config["settings"]["browser"] = args.browser
    if args.fail is not None:
        config["settings"]["fail_on_broken"] = args.fail
    if args.report:
        config["settings"]["report"] = args.report

    totals, results, status = run(config, args.config)

    summary = render_summary(totals, results)
    print(summary)

    report_path = config["settings"].get("report")
    if report_path:
        out = {
            "totals": dict(totals),
            "results": [r.to_dict() for r in results],
        }
        with open(report_path, "w", encoding="utf-8") as fh:
            json.dump(out, fh, indent=2, ensure_ascii=False)
            fh.write("\n")
        print(f"\nReport written to {report_path}")

    return status


if __name__ == "__main__":
    sys.exit(main())
