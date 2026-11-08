#!/usr/bin/env python3
"""Search the local full-text marketing knowledgebase.

Ranks knowledgebase/full_texts documents by query-term hits: title matches
are boosted, body matches counted, exact-phrase hits get a large bonus.
The manifest (knowledgebase/index.json) supplies title/category metadata.

Usage:
  python3.12 tools/kb_search.py "customer churn retention" --limit 10
  python3.12 tools/kb_search.py "agentic negotiation" --category ai-marketing
  python3.12 tools/kb_search.py --stats
  python3.12 tools/kb_search.py "loyalty program" --json
"""

import argparse
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
KB_DIR = REPO / "knowledgebase"
INDEX_PATH = KB_DIR / "index.json"

TOKEN_RE = re.compile(r"[a-z0-9]{2,}")


def tokenize(text):
    return TOKEN_RE.findall((text or "").lower())


def load_docs(category=None, subcategory=None, status="ok"):
    """Return list of (record, path, text) for matching manifest records."""
    if not INDEX_PATH.exists():
        sys.exit(f"No manifest at {INDEX_PATH} — run scripts/build_knowledgebase.py first")
    with open(INDEX_PATH, encoding="utf-8") as f:
        manifest = json.load(f)
    docs = []
    for rec in manifest.get("papers", {}).values():
        if status and rec.get("status") != status:
            continue
        if category and rec.get("category") != category:
            continue
        if subcategory and rec.get("subcategory") != subcategory:
            continue
        path = KB_DIR / rec.get("path", "")
        if not path.exists():
            continue
        docs.append((rec, path))
    return docs


def score_doc(rec, text, q_tokens, q_phrase):
    """Score one document against a query. Higher = better."""
    title = (rec.get("title") or "").lower()
    t_tokens = set(tokenize(title))
    hits_body = sum(text.count(t) for t in q_tokens)
    hits_title = sum(1 for t in q_tokens if t in t_tokens)
    score = hits_body + 5 * hits_title
    body_low = text.lower()
    if q_phrase:
        if q_phrase in body_low:
            score += 10
        if q_phrase in title:
            score += 15
    # slight preference for longer documents (more context depth), scaled small
    score += min(len(text) / 200_000, 1.0)
    return score, hits_body, hits_title


FRONT_MATTER_RE = re.compile(r"\A---\n.*?\n---\n", re.DOTALL)


def strip_front_matter(text):
    return FRONT_MATTER_RE.sub("", text, count=1)


def snippet(text, q_tokens, width=110):
    text = strip_front_matter(text)
    low = text.lower()
    for t in q_tokens:
        i = low.find(t)
        if i >= 0:
            start = max(0, i - width // 2)
            frag = text[start:start + width].replace("\n", " ")
            return ("…" if start else "") + re.sub(r"\s+", " ", frag).strip() + "…"
    return ""


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("query", nargs="*", help="search terms")
    ap.add_argument("--category", help="filter by taxonomy category id")
    ap.add_argument("--subcategory", help="filter by subcategory id")
    ap.add_argument("--limit", type=int, default=10)
    ap.add_argument("--json", action="store_true", help="JSON output")
    ap.add_argument("--stats", action="store_true", help="KB summary and exit")
    args = ap.parse_args(argv)

    docs = load_docs(args.category, args.subcategory)

    if args.stats:
        from collections import Counter
        cats = Counter(r.get("category") for r, _ in docs)
        pages = sum(r.get("pages", 0) for r, _ in docs)
        chars = sum(r.get("chars", 0) for r, _ in docs)
        print(f"knowledgebase: {len(docs)} full texts, {pages:,} PDF pages, "
              f"{chars/1e6:.1f} MB extracted text")
        for c, n in cats.most_common():
            print(f"  {c}: {n}")
        return 0

    query = " ".join(args.query).strip()
    if not query:
        ap.error("provide search terms (or --stats)")
    q_low = query.lower()
    q_tokens = tokenize(q_low)
    if not q_tokens:
        ap.error("query has no searchable terms (min 2 chars)")
    q_phrase = q_low if len(q_tokens) > 1 else ""

    results = []
    for rec, path in docs:
        text = path.read_text(encoding="utf-8", errors="replace")
        score, hb, ht = score_doc(rec, text, q_tokens, q_phrase)
        if score > 1:
            results.append((score, rec, path, hb, ht))
    results.sort(key=lambda x: -x[0])

    if args.json:
        out = []
        for score, rec, path, hb, ht in results[: args.limit]:
            out.append({
                "score": round(score, 2),
                "title": rec.get("title"),
                "url": rec.get("url"),
                "category": rec.get("category"),
                "subcategory": rec.get("subcategory"),
                "date": rec.get("date"),
                "pages": rec.get("pages"),
                "path": str(path.relative_to(KB_DIR)),
            })
        print(json.dumps(out, ensure_ascii=False, indent=1))
        return 0

    if not results:
        print("no matches")
        return 1
    print(f"{len(results)} matches (top {min(args.limit, len(results))})\n")
    for i, (score, rec, path, hb, ht) in enumerate(results[: args.limit], 1):
        text = path.read_text(encoding="utf-8", errors="replace")
        sn = snippet(text, q_tokens)
        print(f"{i:>2}. [{score:.1f}] {rec.get('title', '')[:88]}")
        print(f"    {rec.get('category')}/{rec.get('subcategory')} · {rec.get('date')} · "
              f"{rec.get('pages')}p · {path.relative_to(KB_DIR)}")
        if sn:
            print(f"    {sn[:150]}")
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
