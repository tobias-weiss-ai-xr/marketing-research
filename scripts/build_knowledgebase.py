#!/usr/bin/env python3
"""Build the local full-text marketing knowledgebase from the corpus.

Reads papers.yaml, downloads open-access full texts (arXiv PDFs directly;
DOI papers resolved via OpenAlex best_oa_location), extracts text with
pypdf, and writes:

  knowledgebase/full_texts/<category>/<slug>.md   (one file per paper,
                                                   metadata front matter +
                                                   extracted full text)
  knowledgebase/index.json                        (manifest: per-paper
                                                   status, paths, stats)

``knowledgebase/`` is gitignored ("local-only research artifacts"): the
SCRIPT, this pipeline, is committed and reproducible; the fetched texts
stay on disk.

Statuses in the manifest:
  ok              full text extracted and written
  no_text         PDF downloaded but extraction yielded too little text
                  (scanned/image PDFs)
  extract_failed  PDF parsed with errors only
  download_failed network error / non-200 after retries
  not_pdf         response was not a PDF (HTML landing page etc.)
  landing_page    OA tier: every candidate OA url was a landing page
  no_oa           OA tier: OpenAlex has no open-access location
  queued          in index but not yet attempted (crash resume marker)

Usage:
  python3.12 scripts/build_knowledgebase.py --scope arxiv              # tier 1 (~1,272 papers, fast)
  python3.12 scripts/build_knowledgebase.py --scope oa --limit 300     # tier 2 (bounded, best effort)
  python3.12 scripts/build_knowledgebase.py --scope all                # everything (slow)
  python3.12 scripts/build_knowledgebase.py --category ai-marketing    # filter to one category
  python3.12 scripts/build_knowledgebase.py --dry-run                  # plan only, no fetching
  python3.12 scripts/build_knowledgebase.py --stats                    # manifest summary only

Resume-safe: papers already recorded with status "ok" are skipped unless
--force. Progress is checkpointed to the manifest every N completions.
"""

import argparse
import concurrent.futures as cf
import hashlib
import io
import json
import re
import sys
import threading
import time
import unicodedata
from datetime import datetime, timezone
from pathlib import Path

import requests
import yaml

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
import research_config  # noqa: E402  (repo convention: single config loader)

KB_DIR = REPO / "knowledgebase"
TEXTS_DIR = KB_DIR / "full_texts"
INDEX_PATH = KB_DIR / "index.json"
KB_VERSION = 1

USER_AGENT = "Research-Corpus-KB/1.0 (mailto:research@tobias-weiss-ai-xr.de)"
DOWNLOAD_TIMEOUT = 90
OPENALEX_TIMEOUT = 30
RETRIES = 2
CHECKPOINT_EVERY = 25

_t0 = None
_print_lock = threading.Lock()


def log(msg):
    with _print_lock:
        dt = time.strftime("%H:%M:%S")
        print(f"[{dt}] {msg}", flush=True)


# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------

def slugify(title, url=""):
    """Filename-safe slug from a paper title (<= 80 chars, kebab-case)."""
    s = unicodedata.normalize("NFKD", title or "")
    s = s.encode("ascii", "ignore").decode("ascii").lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    s = re.sub(r"-{2,}", "-", s)[:80].strip("-")
    if not s:
        s = "paper-" + hashlib.sha1(url.encode()).hexdigest()[:8]
    return s


def arxiv_id_from_url(url):
    """Extract the arXiv id (e.g. 2401.12345) from a normalized abs URL."""
    m = re.search(r"arxiv\.org/abs/([0-9]{4}\.[0-9]{4,5})(v[0-9]+)?$", url)
    if not m:
        m = re.search(r"arxiv\.org/abs/([^/]+?)(v[0-9]+)?$", url)
    return m.group(1) if m else None


def doi_from_url(url):
    m = re.search(r"doi\.org/(.+)$", url)
    return m.group(1) if m else None


def load_index():
    if INDEX_PATH.exists():
        with open(INDEX_PATH, encoding="utf-8") as f:
            data = json.load(f)
        return data.setdefault("papers", {})
    return {}


def save_index(papers_index, corpus_count):
    KB_DIR.mkdir(parents=True, exist_ok=True)
    counts = {}
    for rec in papers_index.values():
        counts[rec.get("status", "?")] = counts.get(rec.get("status", "?"), 0) + 1
    payload = {
        "version": KB_VERSION,
        "built_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "corpus_papers": corpus_count,
        "counts": dict(sorted(counts.items())),
        "papers": papers_index,
    }
    tmp = INDEX_PATH.with_suffix(".tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=1)
    tmp.replace(INDEX_PATH)


def make_session():
    s = requests.Session()
    s.headers.update({"User-Agent": USER_AGENT, "Accept": "*/*"})
    return s


def download_pdf(session, url, delay=0.0):
    """Download a URL, return (bytes|None, status). status in
    {ok, not_pdf, download_failed}. Checks the %PDF magic."""
    last = None
    for attempt in range(RETRIES + 1):
        try:
            if delay:
                time.sleep(delay)
            r = session.get(url, timeout=DOWNLOAD_TIMEOUT, stream=False)
            if r.status_code != 200:
                last = f"http {r.status_code}"
                continue
            data = r.content
            if not data.startswith(b"%PDF"):
                return None, "not_pdf"
            return data, "ok"
        except Exception as e:  # noqa: BLE001 (network: many failure modes)
            last = type(e).__name__
            time.sleep(1.5 * (attempt + 1))
    return None, f"download_failed ({last})"


def extract_pdf_text(data, min_chars=200):
    """Extract text from PDF bytes -> (text, pages, error).

    error is None on success, "no_text" if too little text (scanned PDFs),
    or a short description on parse failure.
    """
    try:
        from pypdf import PdfReader
    except ImportError:
        return "", 0, "pypdf not installed (pip install pypdf)"
    try:
        reader = PdfReader(io.BytesIO(data))
        pages = []
        for page in reader.pages:
            try:
                pages.append(page.extract_text() or "")
            except Exception:  # noqa: BLE001 (per-page errors tolerated)
                pages.append("")
        text = "\n\n".join(pages)
        text = text.replace("\x00", "").replace("\x0c", "\n\n")
        # drop lone surrogates (PDF math glyphs) that break UTF-8 writes
        text = re.sub(r"[\ud800-\udfff]", "", text)
        text = re.sub(r"[ \t]+\n", "\n", text)
        text = re.sub(r"\n{3,}", "\n\n", text).strip()
        n = len(reader.pages)
        if len(text) < min_chars:
            return text, n, "no_text"
        return text, n, None
    except Exception as e:  # noqa: BLE001 (corrupt/encrypted PDFs)
        msg = str(e)[:120] or type(e).__name__
        return "", 0, f"extract_failed ({msg})"


def write_doc(paper, text, meta):
    """Write one knowledgebase markdown file; return its relative path."""
    cat = (paper.get("category") or "uncategorized").strip()
    slug = slugify(paper.get("title"), paper.get("url", ""))
    folder = TEXTS_DIR / cat
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / f"{slug}.md"
    # URL-collision guard: same slug in one category -> disambiguate
    if path.exists() and meta.get("status") == "ok":
        digest = hashlib.sha1(paper.get("url", "").encode()).hexdigest()[:8]
        path = folder / f"{slug}-{digest}.md"
    fm = {
        "title": paper.get("title", ""),
        "url": paper.get("url", ""),
        "category": cat,
        "subcategory": paper.get("subcategory", ""),
        "date": paper.get("date", ""),
        "venue": paper.get("venue", ""),
        "authors": paper.get("authors", [])[:25],
        "source": meta.get("source", ""),
        "pdf_url": meta.get("pdf_url", ""),
        "pages": meta.get("pages", 0),
        "chars": meta.get("chars", 0),
        "fetched_at": meta.get("fetched_at", ""),
        "kb_version": KB_VERSION,
    }
    body = (
        "---\n"
        + yaml.safe_dump(fm, allow_unicode=True, sort_keys=False, width=100)
        + "---\n\n"
        + f"# {paper.get('title', '')}\n\n"
        + text
        + "\n"
    )
    tmp = path.with_suffix(".tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(body)
    tmp.replace(path)
    return str(path.relative_to(KB_DIR))


# --------------------------------------------------------------------------
# target collection
# --------------------------------------------------------------------------

def collect_targets(papers, scope, category=None):
    """Deduplicate by URL and filter by scope/category. Returns ordered list.

    Round-robins across categories so a --limit covers all categories.
    """
    by_cat = {}
    seen = set()
    for p in papers:
        url = p.get("url", "")
        if not url or url in seen:
            continue
        seen.add(url)
        if scope == "arxiv" and not arxiv_id_from_url(url):
            continue
        if scope == "oa" and not doi_from_url(url):
            continue
        cat = (p.get("category") or "uncategorized").strip()
        if category and cat != category:
            continue
        by_cat.setdefault(cat, []).append(p)
    # round-robin interleave for category diversity under --limit
    out, cats = [], sorted(by_cat)
    idx = 0
    while any(by_cat[c] for c in cats):
        for c in cats:
            if idx < len(by_cat[c]):
                out.append(by_cat[c][idx])
        idx += 1
        if idx > max(len(by_cat[c]) for c in cats):
            break
    return out


# --------------------------------------------------------------------------
# arXiv tier
# --------------------------------------------------------------------------

def process_arxiv(session, paper, force=False):
    url = paper.get("url", "")
    aid = arxiv_id_from_url(url)
    pdf_url = f"https://arxiv.org/pdf/{aid}"
    meta = {"source": "arxiv", "pdf_url": pdf_url,
            "fetched_at": datetime.now(timezone.utc).isoformat(timespec="seconds")}
    data, status = download_pdf(session, pdf_url, delay=0.25)
    if status != "ok":
        meta["status"] = status if status.startswith(("download_failed", "not_pdf")) else "download_failed"
        if "download_failed" in status:
            meta["error"] = status
        return meta
    text, pages, err = extract_pdf_text(data)
    meta["pages"] = pages
    if err:
        meta["status"] = err.split(" ")[0] if err.startswith("no_text") else err
        meta["error"] = err
        return meta
    meta.update(status="ok", pages=pages, chars=len(text))
    meta["path"] = write_doc(paper, text, meta)
    return meta


# --------------------------------------------------------------------------
# OA tier (DOI via OpenAlex)
# --------------------------------------------------------------------------

def oa_candidates(work):
    """Ordered candidate PDF urls from an OpenAlex work record."""
    urls = []
    locs = [work.get("best_oa_location") or {}] + (work.get("locations") or [])
    if work.get("primary_location"):
        locs.append(work["primary_location"])
    for loc in locs:
        u = loc.get("pdf_url") or ""
        if u and u not in urls:
            urls.append(u)
    return urls[:3]


def resolve_openalex(session, doi, mailto):
    """Return (work_record|None, status)."""
    try:
        time.sleep(0.12)
        r = session.get(
            f"https://api.openalex.org/works/doi:{doi}",
            params={"mailto": mailto}, timeout=OPENALEX_TIMEOUT)
        if r.status_code == 404:
            return None, "no_oa (not in OpenAlex)"
        if r.status_code != 200:
            return None, f"openalex_http_{r.status_code}"
        return r.json(), None
    except Exception as e:  # noqa: BLE001
        return None, f"openalex_error ({type(e).__name__})"


def process_oa(session, paper, mailto):
    url = paper.get("url", "")
    doi = doi_from_url(url)
    meta = {"source": "openalex-oa",
            "fetched_at": datetime.now(timezone.utc).isoformat(timespec="seconds")}
    work, err = resolve_openalex(session, doi, mailto)
    if err:
        meta["status"], meta["error"] = err, err
        return meta
    oa = work.get("open_access") or {}
    meta["oa_status"] = oa.get("oa_status", "")
    candidates = oa_candidates(work)
    if not candidates:
        meta["status"], meta["error"] = "no_oa", "no pdf_url in any OA location"
        return meta
    html_notes = []
    for cand in candidates:
        data, status = download_pdf(session, cand)
        if status == "ok":
            text, pages, xerr = extract_pdf_text(data)
            meta["pages"] = pages
            if xerr:
                meta["status"] = xerr if xerr.startswith("no_text") else xerr
                meta["error"] = xerr
                meta["pdf_url"] = cand
                return meta
            meta.update(status="ok", pages=pages, chars=len(text), pdf_url=cand)
            meta["path"] = write_doc(paper, text, meta)
            return meta
        html_notes.append(f"{cand[:80]} -> {status}")
    meta["status"] = "landing_page"
    meta["error"] = "; ".join(html_notes)
    return meta


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------

def main(argv=None):
    global _t0
    _t0 = time.time()
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--scope", choices=["arxiv", "oa", "all"], default="arxiv",
                    help="arxiv = free-PDF tier; oa = DOI/OpenAlex tier; all = both")
    ap.add_argument("--category", help="limit to one taxonomy category id")
    ap.add_argument("--limit", type=int, default=0,
                    help="process at most N not-yet-ok papers (0 = no limit)")
    ap.add_argument("--workers", type=int, default=4, help="parallel downloaders")
    ap.add_argument("--force", action="store_true",
                    help="re-fetch even papers already recorded as ok")
    ap.add_argument("--dry-run", action="store_true", help="plan only, no fetching")
    ap.add_argument("--stats", action="store_true", help="show manifest summary and exit")
    args = ap.parse_args(argv)

    cfg = research_config.load_config()
    mailto = research_config.get_openalex_mailto(cfg)
    papers = research_config.load_papers()
    index = load_index()

    if args.stats:
        counts = {}
        ok = 0
        for rec in index.values():
            counts[rec.get("status", "?")] = counts.get(rec.get("status", "?"), 0) + 1
            if rec.get("status") == "ok":
                ok += 1
        print(f"knowledgebase manifest: {INDEX_PATH}")
        print(f"records: {len(index)}  ok: {ok}")
        for k, v in sorted(counts.items()):
            print(f"  {k}: {v}")
        return 0

    scopes = ["arxiv", "oa"] if args.scope == "all" else [args.scope]
    todo_total = 0
    for scope in scopes:
        targets = collect_targets(papers, scope, args.category)
        queue = []
        for p in targets:
            rec = index.get(p["url"])
            if rec and rec.get("status") == "ok" and not args.force:
                continue
            queue.append(p)
        if args.limit:
            queue = queue[: args.limit]
        log(f"[{scope}] corpus candidates: {len(targets)}, to fetch: {len(queue)}")
        if args.dry_run:
            todo_total += len(queue)
            continue
        if not queue:
            continue

        session = make_session()
        done = 0
        fn = (lambda p: process_arxiv(session, p)) if scope == "arxiv" \
            else (lambda p: process_oa(session, p, mailto))
        with cf.ThreadPoolExecutor(max_workers=args.workers) as ex:
            futures = {ex.submit(fn, p): p for p in queue}
            for fut in cf.as_completed(futures):
                p = futures[fut]
                try:
                    meta = fut.result()
                except Exception as e:  # noqa: BLE001 (never let one paper kill the run)
                    meta = {"status": f"crashed ({type(e).__name__}: {e})"[:120]}
                index[p["url"]] = {
                    "title": p.get("title", ""),
                    "category": p.get("category", ""),
                    "subcategory": p.get("subcategory", ""),
                    "date": p.get("date", ""),
                    **meta,
                }
                done += 1
                if done % 10 == 0 or done == len(queue):
                    el = time.time() - _t0
                    log(f"[{scope}] {done}/{len(queue)} done ({el:.0f}s)")
                if done % CHECKPOINT_EVERY == 0:
                    save_index(index, len(papers))

    if not args.dry_run:
        save_index(index, len(papers))
        ok = sum(1 for r in index.values() if r.get("status") == "ok")
        chars = sum(r.get("chars", 0) for r in index.values() if r.get("status") == "ok")
        log(f"manifest saved: {len(index)} records, {ok} full texts, "
            f"{chars/1e6:.1f} MB text total -> {TEXTS_DIR}")
    elif todo_total:
        log(f"dry-run: {todo_total} papers would be fetched")
    return 0


if __name__ == "__main__":
    sys.exit(main())
