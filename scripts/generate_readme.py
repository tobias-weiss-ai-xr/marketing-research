#!/usr/bin/env python3
"""Generate README.md and docs/papers.json from papers.yaml.

Generic for any *-research corpus: categories/subcategories and their display
names come from config/taxonomy.yaml (via research_config).

Usage:
    python3 scripts/generate_readme.py
    python3 scripts/generate_readme.py --check   # CI: fail if out of date
"""

STATS_ONLY = False  # Set True to skip full paper list generation
import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

import yaml

import research_config


def render_paper_list(papers, cfg):
    lines = ["## 📚 Paper list", ""]

    cats = research_config.get_categories(cfg)
    subs = research_config.get_subcategories(cfg)

    # Emoji TOC
    for cat in cats:
        cat_display = cat.get("display", cat["id"])
        cat_anchor = cat_display.lower().replace(" ", "-")
        lines.append(f"- [📚 {cat_display}](#{cat_anchor})")
        for sub in subs:
            group = [p for p in papers if p["category"] == cat["id"] and p["subcategory"] == sub["id"]]
            if not group:
                continue
            sub_display = sub.get("display", sub["id"])
            sub_anchor = sub_display.lower().replace(" ", "-")
            lines.append(f"  - [{sub_display}](#{sub_anchor})")
    lines.append("")

    for cat in cats:
        cat_display = cat.get("display", cat["id"])
        lines.append(f"### {cat_display}")
        lines.append("")

        for sub in subs:
            group = [p for p in papers if p["category"] == cat["id"] and p["subcategory"] == sub["id"]]
            if not group:
                continue

            sub_display = sub.get("display", sub["id"])
            lines.append(f"#### {sub_display}")
            lines.append("")

            # Group by year
            year_groups = defaultdict(list)
            for p in group:
                year = p["date"][:4]
                year_groups[year].append(p)

            for year in sorted(year_groups.keys(), reverse=True):
                lines.append(f"##### {year}")
                lines.append("")

                sorted_papers = sorted(year_groups[year], key=lambda p: p["date"], reverse=True)
                for p in sorted_papers:
                    y = p["date"][:4]
                    title = p["title"]
                    url = p["url"]
                    venue = p.get("venue", "")
                    code_url = p.get("code_url", "")
                    project_url = p.get("project_url", "")

                    entry = f"- [{y}] **{title}**"
                    if venue:
                        entry += f" *{venue}*"
                    entry += f" [[paper]({url})]"
                    if code_url:
                        entry += f" [[code]({code_url})]"
                    if project_url:
                        entry += f" [[project]({project_url})]"
                    lines.append(entry)

                lines.append("")

            lines.append("[⬆ Back to top](#paper-list)")
            lines.append("")

    return "\n".join(lines)


def generate_readme(papers, readme_path, cfg, check_mode=False):
    readme_text = readme_path.read_text(encoding="utf-8")

    start_marker = "## 📚 Paper list"  # (paper list replaced with stats)
    end_marker = "## 📖 Citation"  # (paper list replaced with stats)

    start_idx = readme_text.find(start_marker)
    end_idx = readme_text.find(end_marker)

    if start_idx == -1 or end_idx == -1:
        print(
            "Error: Could not find paper list or citation section in README.md",
            file=sys.stderr,
        )
        sys.exit(1)

    before = readme_text[:start_idx]
    after = readme_text[end_idx:]

    generated_list = render_paper_list(papers, cfg)
    new_readme = before + generated_list + "\n" + after

    if check_mode:
        if new_readme == readme_text:
            print("README.md is up-to-date.")
            sys.exit(0)
        else:
            print(
                "README.md is out-of-date. Run generate_readme.py without --check to update.",
                file=sys.stderr,
            )
            sys.exit(1)

    readme_path.write_text(new_readme, encoding="utf-8")
    print(f"Generated {readme_path}")


def generate_json(papers, json_path):
    json_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(
        json.dumps({"papers": papers}, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"Generated {json_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Generate README.md and papers.json from papers.yaml"
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Check if README is up-to-date (exit 1 if not)",
    )
    parser.add_argument(
        "--skip-json", action="store_true", help="Skip generating papers.json"
    )
    args = parser.parse_args()

    base = Path(__file__).parent.parent
    papers_yaml = base / "papers.yaml"
    readme_path = base / "README.md"
    json_path = base / "docs" / "papers.json"

    papers = research_config.load_papers(papers_yaml)
    cfg = research_config.load_config()

    generate_readme(papers, readme_path, cfg, check_mode=args.check)

    if not args.check and not args.skip_json:
        generate_json(papers, json_path)


if __name__ == "__main__":
    main()
