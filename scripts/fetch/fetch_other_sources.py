#!/usr/bin/env python3
"""Generic multi-source fetcher — discovers papers from DBLP, CrossRef, and
Europe PMC beyond arXiv.

Domain queries are loaded from a YAML config file
(`config/other_sources_queries.yaml`) that ships per-repo.  Each query
specifies source, search string, target category, and subcategory hint.

Usage:
    python3 scripts/fetch/fetch_other_sources.py
    python3 scripts/fetch/fetch_other_sources.py --dry-run
    python3 scripts/fetch/fetch_other_sources.py --sleep 3
"""

import argparse
import os
import re
import sys
import time
from datetime import datetime

def clamp_future_date(yyyymm):
    """QUALITY GATE: clamp a YYYY-MM date to today — no future dates allowed.
    Forthcoming articles (e.g. 2027 book chapters from Crossref) are pulled back
    to the current month instead of polluting the corpus with impossible dates."""
    if not yyyymm or not isinstance(yyyymm, str) or len(yyyymm) < 7:
        return yyyymm
    try:
        y, m = int(yyyymm[:4]), int(yyyymm[5:7])
    except (ValueError, IndexError):
        return yyyymm
    now = datetime.now()
    if (y, m) > (now.year, now.month):
        return now.strftime("%Y-%m")
    return yyyymm
from pathlib import Path

import requests
import yaml

BASE = Path(__file__).resolve().parent.parent.parent
ARXIV_ID_RE = re.compile(r"(\d{4}\.\d{4,5})")

DEFAULT_CONFIG = BASE / "config" / "other_sources_queries.yaml"
USER_AGENT = "Research-Corpus/1.0 (mailto:research@tobias-weiss-ai-xr.de)"

# ── Subcategory classification (portable fallback) ────────────────────

SUBCATEGORY_RULES = [
    ("theory",     ["theory", "theoretical", "formal", "proof", "convergence", "bound"],
     False),
    ("mechanism",  ["mechanism", "explainability", "interpretab", "attention",
                    "saliency", "feature importance", "why does"],
     False),
    ("method",     ["method", "algorithm", "approach", "technique", "framework",
                    "proposed method", "our method", "novel method"],
     False),
    ("application",["application", "applied", "deploy", "real-world", "case study",
                    "use case", "experiment", "evaluation on"],
     False),
    ("development",["implementation", "system", "platform", "toolkit", "library",
                    "open-source", "software", "pipeline", "infrastructure"],
     False),
    ("systems",    ["simulator", "simulation", "engine", "benchmark", "testbed",
                    "environment", "gym", "sandbox", "distributed system"],
     False),
    ("evaluation", ["benchmark", "evaluation", "comparison", "baseline",
                    "state-of-the-art", "sota", "leaderboard"],
     False),
    ("review",     ["survey", "review", "literature", "systematic review",
                    "meta-analysis", "overview", "taxonomy"],
     False),
]
SUBCATEGORY_FALLBACK = "application"


def classify_subcategory(title, abstract=""):
    """Assign a subcategory using keyword rules against title + abstract."""
    t_lower = title.lower()
    text = f"{title} {abstract}".lower()
    for subcat, keywords, title_only in SUBCATEGORY_RULES:
        haystack = t_lower if title_only else text
        for kw in keywords:
            if kw in haystack:
                return subcat
    return SUBCATEGORY_FALLBACK


# ── Dedup helpers ────────────────────────────────────────────────────────

def load_existing_papers(yaml_path):
    """Load papers.yaml and return (by_id dict, titles_lower list)."""
    if not yaml_path.exists():
        return {}, []
    with open(yaml_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    papers = data.get("papers", [])
    by_id = {}
    titles_lower = []
    for p in papers:
        url = p.get("url", "")
        match = ARXIV_ID_RE.search(url)
        if match:
            by_id[match.group(1)] = p
        # Also index by DOI and full URL for cross-source dedup
        doi = p.get("doi", "")
        if doi:
            by_id[f"doi:{doi}"] = p
        if url:
            by_id[url] = p
        titles_lower.append(p.get("title", "").lower().strip())
    return by_id, titles_lower


# ── API fetchers ────────────────────────────────────────────────────────

session = requests.Session()
session.headers.update({"User-Agent": USER_AGENT})


def fetch_with_retry(fn, retries=3, base_wait=15):
    """Call fn() with exponential backoff on failure."""
    for attempt in range(retries):
        try:
            return fn()
        except (requests.ConnectionError, requests.Timeout):
            wait = base_wait * (attempt + 1)
            print(f"    connection error, retry in {wait}s...", flush=True)
            time.sleep(wait)
        except requests.HTTPError as e:
            if e.response is not None and e.response.status_code == 429:
                wait = base_wait * 2 * (attempt + 1)
                print(f"    rate limit (429), waiting {wait}s...", flush=True)
                time.sleep(wait)
            else:
                print(f"    error: {e}", flush=True)
                return []
        except Exception as e:
            print(f"    error: {e}", flush=True)
            return []
    print(f"    gave up after {retries} retries", flush=True)
    return []


def fetch_dblp(query, max_results=20):
    def _do():
        r = session.get(
            "https://dblp.org/search/publ/api",
            params={"q": query, "format": "json", "h": str(max_results)},
            timeout=30,
        )
        r.raise_for_status()
        hits = r.json().get("result", {}).get("hits", {}).get("hit", [])
        results = []
        for h in hits:
            info = h.get("info", {})
            title = info.get("title", "")
            if not title:
                continue
            year = info.get("year", "")
            venue = info.get("venue", "")
            key = info.get("key", "")
            doi = info.get("doi", "")
            url = f"https://dblp.org/rec/{key}" if key else ""
            authors_raw = info.get("authors", {}).get("author", [])
            if isinstance(authors_raw, dict):
                authors_raw = [authors_raw]
            authors = [a.get("@_text", "") for a in authors_raw[:3]
                       if isinstance(a, dict)]
            ee = info.get("ee", [])
            if isinstance(ee, str):
                ee = [ee]
            for e_url in ee:
                if "arxiv" in e_url:
                    url = e_url.replace("http://", "https://")
                    break
            results.append({
                "title": title,
                "date": clamp_future_date(f"{year}-01" if year and year.isdigit() else ""),
                "url": url, "authors": authors, "abstract": "",
                "venue": venue, "doi": doi,
            })
        return results
    return fetch_with_retry(_do)


def fetch_crossref(query, max_results=10):
    def _do():
        r = session.get(
            "https://api.crossref.org/works",
            params={
                "query": query, "rows": str(max_results),
                "select": ("DOI,title,abstract,author,published-print,"
                           "published-online,container-title,type,URL"),
            },
            timeout=30,
        )
        if r.status_code == 429:
            print("    CrossRef 429, waiting 20s...", flush=True)
            time.sleep(20)
            return fetch_crossref(query, max_results)
        r.raise_for_status()
        items = r.json().get("message", {}).get("items", [])
        results = []
        for item in items:
            title = (item.get("title") or [""])[0]
            doi = item.get("DOI", "")
            abstract = re.sub(r"<[^>]+>", "", item.get("abstract", "")).strip()
            authors = [
                f'{a.get("given", "")} {a.get("family", "")}'.strip()
                for a in item.get("author", [])[:3]
            ]
            venue = (item.get("container-title") or [""])[0]
            pp = (item.get("published-print")
                  or item.get("published-online") or {})
            dp = pp.get("date-parts", [[]])[0] if pp else []
            year = str(dp[0]) if dp else ""
            month = f"{dp[1]:02d}" if len(dp) > 1 else "01"
            url = (item.get("URL", "")
                   or f"https://doi.org/{doi}" if doi else "")
            if title:
                results.append({
                    "title": title,
                    "date": clamp_future_date(f"{year}-{month}" if year.isdigit() else ""),
                    "url": url, "authors": authors,
                    "abstract": abstract[:300], "venue": venue, "doi": doi,
                })
        return results
    return fetch_with_retry(_do)


def fetch_europe_pmc(query, max_results=10):
    def _do():
        r = session.get(
            "https://www.ebi.ac.uk/europepmc/webservices/rest/search",
            params={"query": query, "format": "json",
                     "pageSize": str(max_results), "resultType": "core"},
            timeout=30,
        )
        r.raise_for_status()
        results_list = r.json().get("resultList", {}).get("result", [])
        results = []
        for hit in results_list:
            title = hit.get("title", "")
            if not title:
                continue
            year = hit.get("pubYear", "")
            doi = hit.get("doi", "")
            pmcid = hit.get("pmcid", "")
            pmid = hit.get("pmid", "")
            abstract = hit.get("abstractText", "") or ""
            src = hit.get("source", "")
            authors_raw = hit.get("authorList", {}).get("author", [])
            if isinstance(authors_raw, dict):
                authors_raw = [authors_raw]
            authors = [a.get("fullName", a.get("authorName", ""))
                       for a in authors_raw[:3] if isinstance(a, dict)]
            if doi:
                url = f"https://doi.org/{doi}"
            elif pmcid:
                url = f"https://europepmc.org/article/pmc/{pmcid}"
            elif pmid:
                url = f"https://pubmed.ncbi.nlm.nih.gov/{pmid}"
            else:
                url = ""
            results.append({
                "title": title,
                "date": clamp_future_date(f"{year}-01" if year and year.isdigit() else ""),
                "url": url, "authors": authors,
                "abstract": abstract[:300], "venue": src, "doi": doi,
            })
        return results
    return fetch_with_retry(_do)


FETCHERS = {
    "dblp": fetch_dblp,
    "crossref": fetch_crossref,
    "europepmc": fetch_europe_pmc,
}


# ── Dedup check ──────────────────────────────────────────────────────────

def is_dup(entry, by_id, titles_lower):
    url = entry.get("url", "")
    doi = entry.get("doi", "")
    t = entry.get("title", "").lower().strip()
    if not t:
        return True
    m = ARXIV_ID_RE.search(url)
    if m and m.group(1) in by_id:
        return True
    if doi and f"doi:{doi}" in by_id:
        return True
    if url and url in by_id:
        return True
    return any(t == tl for tl in titles_lower)


# ── YAML append ─────────────────────────────────────────────────────────

def append_to_yaml(yaml_path, new_papers):
    with open(yaml_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    papers = data.get("papers", [])
    for e in new_papers:
        entry = {
            "title": e["title"],
            "date": clamp_future_date(e.get("date", "")),
            "url": e["url"],
            "category": e["category"],
            "subcategory": e["subcategory"],
            "authors": e.get("authors", []),
        }
        if e.get("abstract"):
            entry["abstract"] = e["abstract"]
        if e.get("doi"):
            entry["doi"] = e["doi"]
        if e.get("venue"):
            entry["venue"] = e["venue"]
        papers.append(entry)
    data["papers"] = papers
    with open(yaml_path, "w", encoding="utf-8") as f:
        yaml.dump(data, f, default_flow_style=False,
                  allow_unicode=True, sort_keys=False)


# ── Main ─────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Multi-source fetch from DBLP, CrossRef, Europe PMC")
    parser.add_argument("--dry-run", action="store_true",
                        help="Print results but don't write papers.yaml")
    parser.add_argument("--sleep", type=float, default=5.0,
                        help="Seconds to sleep between queries (default: 5)")
    parser.add_argument("--config", type=str, default=None,
                        help="Path to query config YAML (default: "
                             "config/other_sources_queries.yaml)")
    args = parser.parse_args()

    config_path = Path(args.config) if args.config else DEFAULT_CONFIG
    if not config_path.exists():
        print(f"Error: config not found at {config_path}", file=sys.stderr)
        print("Create config/other_sources_queries.yaml with your queries.",
              file=sys.stderr)
        sys.exit(1)

    with open(config_path) as f:
        queries = yaml.safe_load(f) or []

    # Try to import repo-specific classify_subcategory if available
    repo_fetch = BASE / "scripts" / "fetch" / "fetch_new_papers.py"
    try:
        sys.path.insert(0, str(repo_fetch.parent))
        from fetch_new_papers import classify_subcategory as _repo_cls  # noqa
        classify_subcategory = _repo_cls
        print("Using repo-specific classify_subcategory", flush=True)
    except ImportError:
        print("Using built-in classify_subcategory", flush=True)

    # Use local papers.yaml if --local flag is set
    if args.local:
        yaml_path = Path("papers.yaml")
    else:
        yaml_path = BASE / "papers.yaml"
    by_id, titles_lower = load_existing_papers(yaml_path)
    print(f"Loaded {len(titles_lower)} existing papers", flush=True)

    all_new = []
    for qi, q in enumerate(queries):
        source = q.get("source", "dblp")
        query = q.get("query", "")
        category = q.get("category", "")
        hint = q.get("subcategory_hint", "")

        fetcher = FETCHERS.get(source)
        if not fetcher:
            print(f"[{qi+1}/{len(queries)}] unknown source '{source}', skip",
                  flush=True)
            continue

        label = f"[{qi+1}/{len(queries)}] {source}/{category}: {query[:50]}"
        print(label, flush=True)
        entries = fetcher(query)
        new = 0
        for e in entries:
            if not e.get("title") or not e.get("url"):
                continue
            if is_dup(e, by_id, titles_lower):
                continue
            e["category"] = category
            e["subcategory"] = (hint or classify_subcategory(
                e["title"], e.get("abstract", "")))
            all_new.append(e)
            doi = e.get("doi", "")
            if doi:
                by_id[f"doi:{doi}"] = e
            by_id[e["url"]] = e
            titles_lower.append(e["title"].lower().strip())
            new += 1
        print(f"  → {new} new (from {len(entries)} results)", flush=True)
        time.sleep(args.sleep)

    print(f"\nTotal new papers: {len(all_new)}", flush=True)
    if args.dry_run:
        for e in all_new[:20]:
            print(f"  [{e['category']}] {e['title'][:80]}")
        if len(all_new) > 20:
            print(f"  ... and {len(all_new) - 20} more")
    else:
        if all_new:
            append_to_yaml(yaml_path, all_new)
            print(f"Appended {len(all_new)} to papers.yaml", flush=True)
        else:
            print("No new papers to add.", flush=True)

    from collections import Counter
    cats = Counter(e["category"] for e in all_new)
    for c, n in cats.most_common():
        print(f"  {c}: +{n}")


if __name__ == "__main__":
    main()
