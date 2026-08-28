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

# Ensure UTF-8 output on all platforms (Windows cp1252 would otherwise raise
# UnicodeEncodeError when printing arrows/dashes in diagnostics).
try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):  # pragma: no cover - non-TTY / older Python
    pass

ARXIV_ID_PATTERN = re.compile(r"((?:[a-z\-]+/)?\d{4}\.\d{4,5}|(?:[a-z\-]+/)?\d{7})(v\d+)?")
ARXIV_PATH_PREFIX = re.compile(
    r"^https?://(?:www\.)?arxiv\.org/(?:abs|pdf)/", re.IGNORECASE
)
ARXIV_DOI_PREFIX = re.compile(
    r"^https?://doi\.org/10\.48550/arXiv\.", re.IGNORECASE
)
ARXIV_URL_PATTERN = re.compile(
    r"^https://arxiv\.org/abs/(?:[a-z\-]+/)?(?:\d{4}\.\d{4,5}|\d{7})$"
)
ARXIV_DOI_PATTERN = re.compile(r"doi\.org/10\.48550/arXiv\.", re.IGNORECASE)
DATE_PATTERN = re.compile(r"^\d{4}-(0[1-9]|1[0-2])$")
URL_PATTERN = re.compile(r"^https://")
LATEX_PATTERNS = [
    re.compile(r"\$\{.*?\}"),
    re.compile(r"\\\("),
    re.compile(r"\\\)"),
    re.compile(r"\^\d"),
    re.compile(r"\\\["),
    re.compile(r"\\\]"),
    re.compile(r"\$[^$]+\$"),
    re.compile(r"\\[a-zA-Z]+\{"),
]
VANITY_DOMAINS = re.compile(
    r"(researchsquare\.com|techrxiv\.org|preprints\.org|hal\.science|"
    r"zenodo\.org/doi|rgdoi\.net)",
    re.IGNORECASE,
)


def clean_latex_artifacts(text):
    """Clean common LaTeX artifacts from a string."""
    if not text:
        return text
    # Remove $...$ inline math (replace with contents)
    text = re.sub(r"\$([^$]+)\$", r"\1", text)
    # Remove \(...\) inline math
    text = re.sub(r"\\\((.+?)\\\)", r"\1", text)
    # Remove \[...\] display math
    text = re.sub(r"\\\[(.+?)\\\]", r"\1", text)
    # Remove ${...}$ patterns
    text = re.sub(r"\$\{([^}]+)\}\$", r"\1", text)
    # Remove \textit{...}, \textbf{...}, \emph{...} etc.
    text = re.sub(r"\\(?:textit|textbf|emph|text|mathrm|mathbf)\{([^}]+)\}", r"\1", text)
    # Clean up double spaces
    text = re.sub(r"\s+", " ", text).strip()
    return text


def normalize_arxiv_url(url):
    # New-style: 1234.56789v2; Old-style: math/0311487v1 (category prefix).
    # Capture the arXiv ID portion (strip /abs/|/pdf/|10.48550/arXiv. prefixes
    # and any version suffix) so both URL styles normalize correctly.
    core = url
    core = ARXIV_PATH_PREFIX.sub("", core)
    core = ARXIV_DOI_PREFIX.sub("", core)
    # Strip a stray "arXiv:" prefix (e.g. arxiv.org/abs/arXiv:2412.13474)
    core = re.sub(r"(?i)arxiv:", "", core)
    m = ARXIV_ID_PATTERN.search(core)
    if m:
        return f"https://arxiv.org/abs/{m.group(1)}"
    return url


def is_arxiv_url(url):
    # Require arxiv.org as a real domain path (abs/ or pdf/), not a bare
    # substring — otherwise edarxiv.org etc. would wrongly match.
    return bool(re.search(r"arxiv\.org/(?:abs|pdf)/", url, re.IGNORECASE)) or bool(
        ARXIV_DOI_PATTERN.search(url)
    )


def validate_papers(data, cfg, fix=False, sort=False):
    errors = []
    warnings = []
    fixed = 0
    seen = {}
    papers = data.get("papers", [])

    valid_categories = {c["id"] for c in research_config.get_categories(cfg)}
    valid_subcategories = {s["id"] for s in research_config.get_subcategories(cfg)}

    # --fix: backfill any missing subcategory with a valid value so the
    # paper remains validation-compliant (fetch may leave it empty).
    if fix:
        for _p in papers:
            if not _p.get("subcategory"):
                _sub = sorted(valid_subcategories)[0] if valid_subcategories else _p.get("category", "")
                if _sub:
                    _p["subcategory"] = _sub
                    fixed += 1

    if not papers:
        errors.append("papers.yaml contains no papers under the 'papers' key")
        return errors, warnings, fixed, papers

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
                m = pattern.search(title)
                if m:
                    if fix:
                        new_title = clean_latex_artifacts(title)
                        if new_title != title:
                            paper["title"] = new_title
                            fixed += 1
                    else:
                        warnings.append(
                            f"{prefix}title contains possible LaTeX artifact: '{m.group()}'"
                        )
                        break

        # Check abstract for LaTeX artifacts
        abstract = paper.get("abstract", "")
        if abstract:
            for pattern in LATEX_PATTERNS:
                m = pattern.search(abstract)
                if m:
                    if fix:
                        new_abstract = clean_latex_artifacts(abstract)
                        if new_abstract != abstract:
                            paper["abstract"] = new_abstract
                            fixed += 1
                    else:
                        warnings.append(
                            f"{prefix}abstract contains possible LaTeX artifact: '{m.group()}'"
                        )
                        break

        url = paper.get("url", "")
        if url and VANITY_DOMAINS.search(url):
            warnings.append(
                f"{prefix}URL points to non-peer-reviewed platform — verify venue quality"
            )

    if sort:
        papers.sort(key=lambda p: (p.get("date", ""), p.get("title", "")), reverse=True)
        data["papers"] = papers

    return errors, warnings, fixed, papers


def main():
    parser = argparse.ArgumentParser(description="Validate papers.yaml")
    parser.add_argument(
        "--fix", action="store_true", help="Auto-fix URL normalization and LaTeX artifacts"
    )
    parser.add_argument(
        "--sort", action="store_true", help="Sort papers by date (desc) then title"
    )
    args = parser.parse_args()

    yaml_path = Path(__file__).resolve().parent.parent / "papers.yaml"
    if not yaml_path.exists():
        print(f"ERROR: {yaml_path} not found", flush=True)
        sys.exit(1)

    cfg = research_config.require_valid_config()

    with open(yaml_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}

    errors, warnings, fixed, papers = validate_papers(data, cfg, fix=args.fix, sort=args.sort)

    if errors:
        print("ERRORS:", flush=True)
        for e in errors:
            print(f"  - {e}", flush=True)

    if warnings:
        print("WARNINGS:", flush=True)
        for w in warnings:
            print(f"  - {w}", flush=True)

    if fixed > 0 or args.sort:
        with open(yaml_path, "w", encoding="utf-8") as f:
            yaml.dump(
                data, f, default_flow_style=False, allow_unicode=True, sort_keys=False
            )
        if fixed > 0:
            print(f"FIXED: {fixed} issue(s) fixed", flush=True)
        if args.sort:
            print(f"SORTED: {len(papers)} papers sorted by date (desc), title", flush=True)

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
