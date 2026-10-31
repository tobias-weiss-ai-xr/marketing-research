#!/usr/bin/env python3
"""Standard brief generator for a *-research corpus.

Search the corpus by topic keywords and print (or write) a ready-to-write
article brief. Self-contained taxonomy discovery.

Standard pipeline mimic shared across all research repos.

Usage:
    python3 tools/brief_generator.py "topic words" --papers 5
    python3 tools/brief_generator.py "topic words" --as-doc
"""

import argparse
import re
from datetime import datetime
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent

STOP = {"for", "in", "the", "and", "with", "of", "on", "to", "a", "an"}

# Strong journals (peer-review quality boost for the brief's ranking).
STRONG_VENUES = [
    "Journal of Marketing", "Journal of Marketing Research",
    "Journal of the Academy of Marketing Science", "Marketing Science",
    "Journal of Consumer Research", "Journal of Consumer Psychology",
    "Industrial Marketing Management", "Journal of Business Research",
    "International Journal of Research in Marketing", "Journal of Interactive Marketing",
    "Journal of Advertising", "Journal of Advertising Research", "Marketing Letters",
    "Journal of Retailing", "Journal of Service Research", "European Journal of Marketing",
    "Psychology & Marketing", "Journal of Personal Selling & Sales Management",
    "Journal of Marketing Analytics", "Journal of Marketing Management",
]


def _venue_boost(venue):
    v = (venue or "").lower()
    return 2 if any(s.lower() in v for s in STRONG_VENUES) else 0


def _recency_boost(date, now_year):
    try:
        y = int(str(date)[:4])
    except (ValueError, TypeError):
        return 0
    if y >= now_year - 1:
        return 2
    if y >= now_year - 3:
        return 1
    return 0


def _norm_title(t):
    return re.sub(r"[^a-z0-9]+", " ", (t or "").lower()).strip()


def find_papers(papers, topic, now_year=None):
    now_year = now_year or datetime.now().year
    terms = [t for t in topic.lower().split() if t not in STOP]
    scored = []
    seen_titles = set()
    for p in papers:
        hay = " ".join([p.get("title", ""), p.get("category", ""),
                        p.get("subcategory", ""), p.get("abstract", "")]).lower()
        m = sum(1 for t in terms if t in hay)
        if not m:
            continue
        # near-duplicate guard: keep the strongest-ranked copy of similar titles
        key = _norm_title(p.get("title", ""))
        if key and key in seen_titles:
            continue
        score = m * 3 + _venue_boost(p.get("venue")) + _recency_boost(p.get("date"), now_year)
        scored.append((score, p.get("date", ""), p))
        if key:
            seen_titles.add(key)
    scored.sort(key=lambda x: x[1], reverse=True)   # date desc (newest first)
    scored.sort(key=lambda x: -x[0])                # score desc, stable tie-break
    return [p for _, _, p in scored]


def _display(kebab):
    return kebab.replace("-", " ").replace("_", " ").title()


def slugify(topic):
    return re.sub(r"[^a-z0-9]+", "_", topic.lower()).strip("_") or "brief"


def load_papers():
    with open(REPO / "papers.yaml", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data.get("papers", [])


def main():
    ap = argparse.ArgumentParser(description="Standard brief generator")
    ap.add_argument("topic")
    ap.add_argument("--papers", type=int, default=5)
    ap.add_argument("--as-doc", action="store_true")
    a = ap.parse_args()

    papers = load_papers()
    hits = find_papers(papers, a.topic)[: a.papers]

    lines = [f"# Article Brief: {a.topic}\n"]
    if not hits:
        lines.append("No corpus papers matched. Consider expanding the corpus.")
    for p in hits:
        cat = f"{_display(p.get('category',''))} / {_display(p.get('subcategory',''))}"
        lines.append(f"- **{p.get('title','')}** ({cat}) — {p.get('date','')} — {p.get('url','')}")
        if p.get("abstract"):
            lines.append(f"  {p['abstract'][:400].rsplit(' ', 1)[0]}…\n")

    print("\n".join(lines))

    if a.as_doc:
        out = REPO / "docs" / "topics" / f"brief_{slugify(a.topic)}.md"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text("\n".join(lines), encoding="utf-8")
        print(f"\nWrote {out}")


if __name__ == "__main__":
    main()