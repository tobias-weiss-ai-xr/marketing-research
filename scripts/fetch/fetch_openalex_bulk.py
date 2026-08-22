#!/usr/bin/env python3
"""Bulk-fetch papers from OpenAlex, one request per category (config-driven).

Categories and search terms come from config/taxonomy.yaml (openalex_queries).
Uses OpenAlex cursor pagination with a precise `title_and_abstract.search`
filter (AND semantics) and relevance sorting.

Usage:
    python3 scripts/fetch/fetch_openalex_bulk.py --per-category 100 --months 36
"""

import argparse
import re
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
import sys

import requests
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import research_config

OPENALEX_API = "https://api.openalex.org/works"

ARXIV_ID_PATTERN = re.compile(r"(\d{4}\.\d{4,5})(v\d+)?")

def load_category_terms(cfg):
    """Load (category, search term) pairs from config/taxonomy.yaml."""
    terms = []
    for item in cfg.get("openalex_queries", []):
        terms.append((item.get("category", "method"), item.get("query", "")))
    if not terms:
        short = cfg.get("topic", {}).get("short", "research")
        terms = [("method", short)]
    return terms


def load_subcat_keywords(cfg):
    """Subcategory keyword rules from config (via research_config).

    Returns a list of (subcat_id, [keywords]).  Falls back to an empty
    list; the caller then uses the heuristic classify_subcategory.
    """
    return research_config.get_subcategory_keywords(cfg)


def load_existing_papers(yaml_path):
    """Load existing papers and build lookup structures."""
    if not yaml_path.exists():
        return {}, []
    with open(yaml_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    papers = data.get("papers", [])
    by_id = {}
    titles_lower = []
    for p in papers:
        url = p.get("url", "")
        match = ARXIV_ID_PATTERN.search(url)
        if match:
            by_id[match.group(1)] = p
        else:
            by_id.setdefault(url, p)
        titles_lower.append((p.get("title") or "").lower().strip())
    return by_id, titles_lower


def classify_subcategory(title, abstract, keywords_rules=None):
    """Assign a subcategory using config keyword rules against title + abstract.

    keywords_rules: list of (subcat_id, [keywords]) from config. If not
    provided, returns the first configured subcategory as a safe default.
    """
    if keywords_rules:
        text = f"{title} {abstract}".lower()
        for subcat, keywords in keywords_rules:
            if any(k.lower() in text for k in keywords):
                return subcat
        # Fall back to first configured subcategory
        return keywords_rules[0][0] if keywords_rules else ""
    return ""


def sanitize_date(date_str):
    """Normalize a date to YYYY-MM, clamping future dates to today."""
    if not date_str:
        return ""
    y = date_str[:4]
    m = date_str[5:7] if len(date_str) >= 7 else "01"
    if not y.isdigit() or not m.isdigit():
        return ""
    now = datetime.now(timezone.utc)
    if (int(y), int(m)) > (now.year, now.month):
        return now.strftime("%Y-%m")
    return f"{y}-{m}"


def date_filter(months):
    cutoff = datetime.now(timezone.utc) - timedelta(days=months * 30)
    return cutoff.strftime("%Y-%m-%d")


def reconstruct_abstract(inverted):
    if not inverted:
        return ""
    pos = {}
    for word, positions in inverted.items():
        for p in positions:
            pos[p] = word
    return " ".join(pos[i] for i in sorted(pos))


def fetch_category(terms, months, per_category, sleep, subcat_keywords=None, mailto=None):
    """Cursor-paginated, relevance-sorted fetch for one category."""
    import requests
    session = requests.Session()
    session.headers.update({"User-Agent": "research-runner/1.0"})
    entries = []
    cursor = "*"
    search_filter = f"title_and_abstract.search:{terms}"
    while len(entries) < per_category and cursor:
        params = {
            "filter": (
                f"from_publication_date:{date_filter(months)},"
                f"{search_filter}"
            ),
            "per-page": 200,
            "mailto": mailto or "research@tobias-weiss-ai-xr.de",
            "cursor": cursor,
        }
        data = None
        for attempt in range(4):
            try:
                resp = session.get(OPENALEX_API, params=params, timeout=30)
                if resp.status_code == 429:
                    wait = int(resp.headers.get('Retry-After', 5 * (attempt + 1)))
                    print(f"    rate-limited (429), waiting {wait}s...", flush=True)
                    time.sleep(wait)
                    continue
                resp.raise_for_status()
                data = resp.json()
                break
            except Exception as e:
                print(f"  WARNING: {e}", flush=True)
                break
        if not data:
            break
        results = data.get("results", [])
        cursor = data.get("meta", {}).get("next_cursor")
        if not results:
            break
        for work in results:
            title = work.get("title") or ""
            if not title:
                continue
            url = ""
            for loc in work.get("locations", []):
                src = (loc.get("source") or {}).get("id", "")
                lurl = loc.get("landing_page_url") or ""
                if "arxiv" in src or "arxiv" in lurl:
                    url = lurl.replace("http://", "https://").replace("https://arxiv.org/abs/", "https://arxiv.org/abs/")
                    url = re.sub(r"(arxiv\.org/abs/\d{4}\.\d{4,5})v\d+", r"\1", url)
                    break
            if not url:
                primary = work.get("primary_location") or {}
                url = (primary.get("landing_page_url") or "").replace("http://", "https://")
            if not url:
                url = work.get("doi") or ""
            if not url:
                continue
            mdoi = re.match(r"https?://doi\.org/10\.48550/arxiv\.(\d{4}\.\d{4,5})", url)
            if mdoi:
                url = "https://arxiv.org/abs/" + mdoi.group(1)
            date = sanitize_date(work.get("publication_date") or "")
            if not date:
                date = sanitize_date(str(work.get("publication_year") or ""))
            abstract = reconstruct_abstract(work.get("abstract_inverted_index"))
            entries.append(
                {
                    "title": title,
                    "date": date,
                    "url": url,
                    "category": None,
                    "subcategory": classify_subcategory(title, abstract, subcat_keywords),
                    "authors": [a.get("author", {}).get("display_name", "") for a in work.get("authorships", [])][:3],
                    "abstract": abstract,
                    "venue": ((work.get("primary_location") or {}).get("source") or {}).get("display_name") or "",
                }
            )
        print(f"    page: {len(results)} results ({len(entries)} total)", flush=True)
        time.sleep(sleep)
    return entries


def append_papers(yaml_path, new_papers):
    if yaml_path.exists():
        with open(yaml_path, "r") as f:
            data = yaml.safe_load(f) or {}
    else:
        data = {}
    papers = data.get("papers", [])
    for entry in new_papers:
        papers.append(entry)
    data["papers"] = papers
    with open(yaml_path, "w") as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)


def main():
    parser = argparse.ArgumentParser(description="Bulk-fetch papers from OpenAlex per category (config-driven)")
    parser.add_argument("--months", type=int, default=1)
    parser.add_argument("--full-history", action="store_true", help="Use --months 6 for initial fetch")
    parser.add_argument("--per-category", type=int, default=500)
    parser.add_argument("--sleep", type=float, default=1.5)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--categories", default=None, help="Comma-separated subset of category keys")

    parser.add_argument("--local", action="store_true", help="Run locally without modifying remote repos")
    args = parser.parse_args()

    cfg = research_config.load_config()
    category_terms = load_category_terms(cfg)
    subcat_keywords = load_subcat_keywords(cfg)
    mailto = research_config.get_openalex_mailto(cfg)

    yaml_path = Path(__file__).resolve().parent.parent.parent / "papers.yaml"
    by_id, titles_lower = load_existing_papers(yaml_path)
    print(f"Loaded {len(by_id)} existing papers", flush=True)

    if args.categories:
        wanted = {c.strip() for c in args.categories.split(",") if c.strip()}
        terms_list = [(c, t) for c, t in category_terms if c in wanted]
    else:
        terms_list = category_terms

    # Use 6 months if --full-history, otherwise use args.months
    months = 6 if args.full_history else args.months
    for cat, terms in terms_list:
        print(f"\n=== [{cat}] {terms} ===", flush=True)
        entries = fetch_category(terms, months, args.per_category, args.sleep, subcat_keywords, mailto)
        new = []
        for e in entries:
            m = ARXIV_ID_PATTERN.search(e["url"])
            key = m.group(1) if m else e["url"]
            if key and key in by_id:
                continue
            if any(e["url"] == x["url"] for x in new):
                continue
            t_lower = e["title"].lower().strip()
            if any(t_lower == t for t in titles_lower):
                continue
            e["category"] = cat
            new.append(e)
            by_id[key] = e
            titles_lower.append(t_lower)

        print(f"  {len(new)} new for {cat}", flush=True)
        if args.dry_run:
            continue
        append_papers(yaml_path, new)
        print(f"  saved ({len(by_id)} total)", flush=True)
        time.sleep(args.sleep * 2)

    print("\nDone.", flush=True)


if __name__ == "__main__":
    main()
