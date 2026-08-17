#!/usr/bin/env python3
"""Validate papers.yaml for schema, duplicates, URL normalization, and LaTeX artifacts.

Generic for any *-research corpus: the taxonomy (categories/subcategories) is read
from config/taxonomy.yaml, so no hardcoded topic values are needed.

Usage:
    python3 scripts/validate_papers.py
    python3 scripts/validate_papers.py --fix
"""

import argparse
import re
import sys
from datetime import datetime
from pathlib import Path

TODAY = datetime.now()

import yaml

import research_config

ARXIV_ID_PATTERN = re.compile(r"(\d{4}\.\d{4,5})(v\d+)?")
ARXIV_URL_PATTERN = re.compile(r"^https://arxiv\.org/abs/\d{4}\.\d{4,5}$")
ARXIV_DOI_PATTERN = re.compile(r"doi\.org/10\.48550/arXiv\.", re.IGNORECASE)
DATE_PATTERN = re.compile(r"^\d{4}-(0[1-9]|1[0-2])$")
URL_PATTERN = re.compile(r"^https://")
LATEX_PATTERNS = [
    re.compile(r"\$\{.*?\}"),
    re.compile(r"\\\("),
    re.compile(r"\\\)"),
    re.compile(r"\^\d"),
]
VANITY_DOMAINS = re.compile(
    r"(researchsquare\.com|techrxiv\.org|preprints\.org|hal\.science|"
    r"zenodo\.org/doi|rgdoi\.net)",
    re.IGNORECASE,
)


def normalize_arxiv_url(url):
    match = ARXIV_ID_PATTERN.search(url)
    if match:
        return f"https://arxiv.org/abs/{match.group(1)}"
    return url


def is_arxiv_url(url):
    return "arxiv.org" in url or bool(ARXIV_DOI_PATTERN.search(url))


def validate_papers(data, cfg, fix=False):
    errors = []
    warnings = []
    fixed = 0
    seen = {}
    papers = data.get("papers", [])

    valid_categories = {c["id"] for c in research_config.get_categories(cfg)}
    valid_subcategories = {s["id"] for s in research_config.get_subcategories(cfg)}

    if not papers:
        errors.append("papers.yaml contains no papers under the 'papers' key")
        return errors, warnings, fixed

    for i, paper in enumerate(papers):
        title = paper.get("title", "")
        prefix = f"[#{i + 1}] '{title}': " if title else f"[#{i + 1}] "

        for field in ("title", "date", "url", "category", "subcategory"):
            if not paper.get(field):
                errors.append(f"{prefix}missing required field '{field}'")

        cat = paper.get("category", "")
        if cat and cat not in valid_categories:
            errors.append(
                f"{prefix}invalid category '{cat}' — must be one of {sorted(valid_categories)}"
            )

        sub = paper.get("subcategory", "")
        if sub and sub not in valid_subcategories:
            errors.append(
                f"{prefix}invalid subcategory '{sub}' — must be one of {sorted(valid_subcategories)}"
            )

        date = paper.get("date", "")
        if date and not DATE_PATTERN.match(date):
            errors.append(
                f"{prefix}invalid date '{date}' — must be YYYY-MM format with month 01-12"
            )
        elif date:
            # QUALITY GATE: papers must not be dated in the future
            _y, _m = int(date[:4]), int(date[5:7])
            if (_y, _m) > (TODAY.year, TODAY.month):
                errors.append(
                    f"{prefix}future date '{date}' — papers cannot be dated after today ({TODAY:%Y-%m})"
                )

        url = paper.get("url", "")
        if url:
            if not URL_PATTERN.match(url):
                errors.append(f"{prefix}URL must start with https:// — got '{url}'")
            if is_arxiv_url(url) and not ARXIV_URL_PATTERN.match(url):
                if fix:
                    paper["url"] = normalize_arxiv_url(url)
                    fixed += 1
                else:
                    errors.append(
                        f"{prefix}arXiv URL not normalized — use https://arxiv.org/abs/XXXX format, got '{url}'"
                    )

        key = (title.strip().lower(), cat, sub)
        if key in seen:
            errors.append(
                f"{prefix}duplicate entry (same title/category/subcategory as #{seen[key] + 1})"
            )
        else:
            seen[key] = i

        if title:
            for pattern in LATEX_PATTERNS:
                if pattern.search(title):
                    warnings.append(
                        f"{prefix}title contains possible LaTeX artifact: '{pattern.search(title).group()}'"
                    )

        url = paper.get("url", "")
        if url and VANITY_DOMAINS.search(url):
            warnings.append(
                f"{prefix}URL points to non-peer-reviewed platform — verify venue quality"
            )

    return errors, warnings, fixed


def main():
    parser = argparse.ArgumentParser(description="Validate papers.yaml")
    parser.add_argument(
        "--fix", action="store_true", help="Auto-fix URL normalization issues"
    )
    args = parser.parse_args()

    yaml_path = Path(__file__).resolve().parent.parent / "papers.yaml"
    if not yaml_path.exists():
        print(f"ERROR: {yaml_path} not found", flush=True)
        sys.exit(1)

    cfg = research_config.load_config()

    with open(yaml_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}

    errors, warnings, fixed = validate_papers(data, cfg, fix=args.fix)

    if errors:
        print("ERRORS:", flush=True)
        for e in errors:
            print(f"  - {e}", flush=True)

    if warnings:
        print("WARNINGS:", flush=True)
        for w in warnings:
            print(f"  - {w}", flush=True)

    if fixed > 0:
        with open(yaml_path, "w", encoding="utf-8") as f:
            yaml.dump(
                data, f, default_flow_style=False, allow_unicode=True, sort_keys=False
            )
        print(f"FIXED: {fixed} URL(s) normalized", flush=True)

    if not errors and not warnings:
        print(
            f"OK: All {len(data.get('papers', []))} papers passed validation",
            flush=True,
        )
    elif not errors:
        print(
            f"OK: All {len(data.get('papers', []))} papers passed validation (with warnings)",
            flush=True,
        )

    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
