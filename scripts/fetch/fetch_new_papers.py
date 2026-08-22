#!/usr/bin/env python3
"""Discover new papers from arXiv API (topic configurable via config/taxonomy.yaml)."""
import argparse
import re
import subprocess
import sys
import time
from datetime import datetime, timezone, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import requests
import yaml

import research_config

ARXIV_ID_PATTERN = re.compile(r"(\d{4}\.\d{4,5})")
ARXIV_SEARCH_API = (
    "https://export.arxiv.org/api/query?search_query={}&start={}&max_results={}"
)


def get_queries(cfg):
    """Return arXiv queries, supporting both string and dict formats.

    Each entry can be:
      - a plain string (legacy): 'cat:cs.RO AND abs:"manipulation"'
      - a dict with query + optional category/subcategory_hint:
        query: 'cat:cs.RO AND abs:"manipulation"'
        category: manipulation        # optional
        subcategory_hint: method      # optional
    """
    out = []
    for q in cfg.get("arxiv_queries", []):
        if isinstance(q, dict):
            out.append({
                "query": q.get("query", ""),
                "category": q.get("category", ""),
                "subcategory_hint": q.get("subcategory_hint", ""),
            })
        else:
            out.append({"query": q, "category": "", "subcategory_hint": ""})
    return out


def classify_subcategory(title, abstract="", cfg=None):
    """Assign a subcategory using config keyword rules, then heuristics.

    Reads ``subcategory_keywords`` from taxonomy.yaml (via research_config).
    Falls back to a generic heuristic ordering when no config rules match.
    """
    if cfg is None:
        cfg = research_config.load_config()
    text = f"{title} {abstract}".lower()
    title_lower = title.lower()
    # 1. Config-driven rules (first match wins)
    for sid, keywords in research_config.get_subcategory_keywords(cfg):
        for kw in keywords:
            if kw.lower() in text:
                return sid
    # 2. Generic heuristic fallback (same ordering as fetch_other_sources)
    heuristic = [
        ("theory", ["theory", "theoretical", "formal", "proof", "convergence", "bound"]),
        ("mechanism", ["mechanism", "explainab", "interpretab", "attention", "saliency"]),
        ("method", ["method", "algorithm", "approach", "technique", "framework", "novel method"]),
        ("application", ["application", "applied", "deploy", "real-world", "case study"]),
        ("development", ["implementation", "system", "platform", "toolkit", "library", "open-source"]),
        ("systems", ["simulator", "simulation", "engine", "benchmark", "testbed", "environment"]),
        ("evaluation", ["benchmark", "evaluation", "comparison", "baseline", "leaderboard"]),
        ("review", ["survey", "review", "literature", "meta-analysis", "overview", "taxonomy"]),
    ]
    for sid, keywords in heuristic:
        for kw in keywords:
            if kw in text:
                return sid
    # 3. First configured subcategory as last resort
    subs = research_config.get_subcategories(cfg)
    return subs[0]["id"] if subs else ""


def load_existing_papers(yaml_path):
    if not yaml_path.exists():
        return {}, []
    with open(yaml_path, "r") as f:
        data = yaml.safe_load(f) or {}
    papers = data.get("papers", [])
    by_id = {}
    titles_lower = []
    for p in papers:
        url = p.get("url", "")
        match = ARXIV_ID_PATTERN.search(url)
        if match:
            by_id[match.group(1)] = p
        titles_lower.append(p.get("title", "").lower().strip())
    return by_id, titles_lower


def search_arxiv(query, months, start=0, max_results=100):
    now = datetime.now(timezone.utc).replace(tzinfo=None)
    cutoff = now - timedelta(days=months * 30)
    date_start = cutoff.strftime("%Y%m%d0000")
    date_end = now.strftime("%Y%m%d") + "2359"

    full_query = f"({query}) AND submittedDate:[{date_start} TO {date_end}]"
    try:
        resp = requests.get(
            ARXIV_SEARCH_API.format(
                requests.utils.quote(full_query), start, max_results
            ),
            timeout=30,
        )
        resp.raise_for_status()
        entries = []
        root = resp.text
        for match in re.finditer(r"<entry>(.*?)</entry>", root, re.DOTALL):
            entry_xml = match.group(1)
            entry = {}
            title_m = re.search(r"<title>(.*?)</title>", entry_xml, re.DOTALL)
            if title_m:
                entry["title"] = re.sub(r"\s+", " ", title_m.group(1).strip())
            id_m = re.search(r"<id>(.*?)</id>", entry_xml)
            if id_m:
                entry["url"] = id_m.group(1).strip().replace("http://", "https://")
            published_m = re.search(r"<published>(.*?)</published>", entry_xml)
            if published_m:
                entry["date"] = published_m.group(1).strip()[:7]
            summary_m = re.search(r"<summary>(.*?)</summary>", entry_xml, re.DOTALL)
            if summary_m:
                entry["abstract"] = re.sub(r"\s+", " ", summary_m.group(1).strip())
            # Extract authors from <author><name>...</name></author> tags
            authors = []
            for auth_m in re.finditer(r"<author>\s*<name>(.*?)</name>\s*</author>", entry_xml, re.DOTALL):
                name = auth_m.group(1).strip()
                if name:
                    authors.append(name)
            entry["authors"] = authors[:5]  # cap at 5 for readability
            # Extract venue hint from <arxiv:comment> if present
            venue = ""
            comment_m = re.search(r"<arxiv:comment[^>]*>(.*?)</arxiv:comment>", entry_xml, re.DOTALL)
            if comment_m:
                comment = re.sub(r"\s+", " ", comment_m.group(1).strip())
                venue_match = re.search(
                    r"(?:Accepted|Published|Appears in|in proceedings of|in|at)\s+"
                    r"((?:ACL|EMNLP|NAACL|NeurIPS|ICML|ICLR|CVPR|ICCV|ECCV|AAAI|"
                    r"IJCAI|COLM|COLING|KDD|WWW|SIGIR|WSDM|CIKM|TMLR|JMLR|ICRA|IROS|RA-L|"
                    r"CoRL|RSS|Humanoids|CASE|RAL)[\w\s\.\-]*"
                    r"(?:\d{4})?)",
                    comment, re.IGNORECASE
                )
                if venue_match:
                    venue = venue_match.group(1).strip()
            entry["venue"] = venue
            # Extract code/project URLs from abstract
            abstract_text = entry.get("abstract", "")
            code_url = ""
            project_url = ""
            github_match = re.search(r"https?://github\.com/[\w\-.]+/[\w\-.]+", abstract_text)
            if github_match:
                code_url = github_match.group(0).rstrip(".")
            proj_match = re.search(r"https?://(?:[\w\-.]+\.)?(?:github\.io|sites\.google\.com|huggingface\.co|zenodo\.org|projectpage\.[\w\-.]+)/[^\s\)]+", abstract_text)
            if proj_match:
                project_url = proj_match.group(0).rstrip(".")
            if not code_url and not project_url:
                gh_io_match = re.search(r"https?://[\w\-.]+\.github\.io/[^\s\)]+", abstract_text)
                if gh_io_match:
                    project_url = gh_io_match.group(0).rstrip(".")
            entry["code_url"] = code_url
            entry["project_url"] = project_url
            if entry.get("title") and entry.get("url"):
                entries.append(entry)
        return entries
    except Exception as e:
        print(f"  WARNING: arXiv search error: {e}", flush=True)
        return []


def format_yaml_entry(entry, cfg):
    title = entry["title"].replace('"', '\\"')
    cats = " | ".join(c["id"] for c in research_config.get_categories(cfg)) or "?"
    subs = " | ".join(s["id"] for s in research_config.get_subcategories(cfg)) or "?"
    cat = entry.get("category", "")
    sub = entry.get("subcategory", "")
    cat_line = f'    category: "{cat}"' if cat else f'    category: ""  # TODO: {cats}'
    sub_line = f'    subcategory: "{sub}"' if sub else f'    subcategory: ""  # TODO: {subs}'
    lines = [
        f'  - title: "{title}"',
        f'    date: "{entry.get("date", "")}"',
        f'    url: "{entry.get("url", "")}"',
        cat_line,
        sub_line,
    ]
    authors = entry.get("authors", [])
    if authors:
        lines.append(f'    authors:')
        for a in authors:
            lines.append(f'      - "{a}"')
    if entry.get("venue"):
        venue = entry["venue"].replace('"', '\\"')
        lines.append(f'    venue: "{venue}"')
    if entry.get("code_url"):
        lines.append(f'    code_url: "{entry["code_url"]}"')
    if entry.get("project_url"):
        lines.append(f'    project_url: "{entry["project_url"]}"')
    if entry.get("abstract"):
        abstract = entry["abstract"][:200].replace('"', '\\"')
        lines.append(f'    abstract: "{abstract}..."')
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Discover new papers from arXiv (topic from config/taxonomy.yaml)"
    )
    parser.add_argument(
        "--months",
        type=int,
        default=3,
        help="Search papers from the last N months (default: 3)",
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="Preview without creating anything"
    )
    parser.add_argument(
        "--create-pr", action="store_true", help="Create a GitHub PR with new papers"
    )
    parser.add_argument(
        "--local", action="store_true", help="Append discovered papers locally (no GitHub)"
    )
    args = parser.parse_args()

    cfg = research_config.load_config()
    queries = get_queries(cfg)

    yaml_path = Path(__file__).resolve().parent.parent.parent / "papers.yaml"
    by_id, titles_lower = load_existing_papers(yaml_path)

    print(f"Loaded {len(by_id)} existing papers from papers.yaml", flush=True)
    print(f"Using {len(queries)} arXiv query(ies) from config/taxonomy.yaml", flush=True)
    print(
        f"Searching arXiv for papers from the last {args.months} month(s)...",
        flush=True,
    )

    if not queries:
        print("No arxiv_queries configured in config/taxonomy.yaml — nothing to do.", flush=True)
        return

    all_new = []
    for qi, qinfo in enumerate(queries):
        query = qinfo["query"]
        q_category = qinfo.get("category", "")
        q_hint = qinfo.get("subcategory_hint", "")
        print(f"\nQuery {qi + 1}/{len(queries)}...", flush=True)
        entries = search_arxiv(query, args.months)
        for entry in entries:
            arxiv_id_match = ARXIV_ID_PATTERN.search(entry.get("url", ""))
            arxiv_id = arxiv_id_match.group(1) if arxiv_id_match else None

            if arxiv_id and arxiv_id in by_id:
                continue

            title_lower = entry.get("title", "").lower().strip()
            if any(title_lower == t for t in titles_lower):
                continue

            if arxiv_id and any(e.get("url", "") == entry["url"] for e in all_new):
                continue

            # Auto-classify subcategory if no hint; always classify subcategory
            sub = q_hint or classify_subcategory(
                entry.get("title", ""), entry.get("abstract", ""), cfg)
            entry["category"] = q_category
            entry["subcategory"] = sub
            all_new.append(entry)

        time.sleep(3)

    print(
        f"\nFound {len(all_new)} new papers ({len(by_id)} already in list)", flush=True
    )

    if not all_new:
        print("No new papers to add.", flush=True)
        return

    print("\n--- New Papers ---", flush=True)
    for entry in all_new:
        print(format_yaml_entry(entry, cfg), flush=True)
        print(flush=True)

    if args.dry_run:
        print("\nDry run complete — no files modified", flush=True)
        return

    if args.local:
        print(f"\nAppending {len(all_new)} new papers to papers.yaml locally...", flush=True)
        try:
            with open(yaml_path, "r") as f:
                data = yaml.safe_load(f) or {}
            papers = data.get("papers", [])
            before = len(papers)
            for entry in all_new:
                papers.append(
                    {
                        "title": entry.get("title", ""),
                        "date": entry.get("date", ""),
                        "url": entry.get("url", ""),
                        "category": entry.get("category", ""),
                        "subcategory": entry.get("subcategory", ""),
                        "authors": entry.get("authors", []),
                        "venue": entry.get("venue", ""),
                        "code_url": entry.get("code_url", ""),
                        "project_url": entry.get("project_url", ""),
                        "abstract": entry.get("abstract", ""),
                    }
                )
            data["papers"] = papers
            with open(yaml_path, "w") as f:
                yaml.dump(
                    data,
                    f,
                    default_flow_style=False,
                    allow_unicode=True,
                    sort_keys=False,
                )
            print(f"Saved {len(papers) - before} new papers to papers.yaml", flush=True)
        except Exception as e:
            print(f"ERROR: local write failed: {e}", flush=True)
            sys.exit(1)
        return

    if args.create_pr:
        branch_name = f"add-new-papers-{datetime.now().strftime('%Y%m%d')}"
        yaml_entries = "\n".join(format_yaml_entry(e, cfg) for e in all_new)

        print(f"\nCreating branch '{branch_name}' and PR...", flush=True)

        try:
            subprocess.run(
                ["git", "checkout", "-b", branch_name], check=True, cwd=yaml_path.parent
            )
            with open(yaml_path, "r") as f:
                data = yaml.safe_load(f) or {}
            papers = data.get("papers", [])
            for entry in all_new:
                papers.append(
                    {
                        "title": entry.get("title", ""),
                        "date": entry.get("date", ""),
                        "url": entry.get("url", ""),
                        "category": entry.get("category", ""),
                        "subcategory": entry.get("subcategory", ""),
                        "authors": entry.get("authors", []),
                        "venue": entry.get("venue", ""),
                        "code_url": entry.get("code_url", ""),
                        "project_url": entry.get("project_url", ""),
                        "abstract": entry.get("abstract", ""),
                    }
                )
            data["papers"] = papers
            with open(yaml_path, "w") as f:
                yaml.dump(
                    data,
                    f,
                    default_flow_style=False,
                    allow_unicode=True,
                    sort_keys=False,
                )
            subprocess.run(
                ["git", "add", "papers.yaml"], check=True, cwd=yaml_path.parent
            )
            subprocess.run(
                [
                    "git",
                    "commit",
                    "-m",
                    f"Add {len(all_new)} new papers from arXiv discovery",
                ],
                check=True,
                cwd=yaml_path.parent,
            )
            subprocess.run(
                ["git", "push", "origin", branch_name], check=True, cwd=yaml_path.parent
            )
            subprocess.run(
                [
                    "gh",
                    "pr",
                    "create",
                    "--title",
                    f"Add {len(all_new)} new papers from arXiv discovery",
                    "--body",
                    f"Automatically discovered {len(all_new)} new papers.\n\n**Please review taxonomy assignments.**",
                ],
                check=True,
                cwd=yaml_path.parent,
            )
            print("PR created successfully!", flush=True)
        except subprocess.CalledProcessError as e:
            print(f"ERROR: Failed to create PR: {e}", flush=True)
            sys.exit(1)
    else:
        print(
            "\nTo add these papers, re-run with --create-pr or manually add to papers.yaml",
            flush=True,
        )


if __name__ == "__main__":
    main()
