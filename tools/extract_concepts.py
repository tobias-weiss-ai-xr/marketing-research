#!/usr/bin/env python3
"""extract_concepts.py — extract candidate concepts/ideas from a research corpus.

Minimal, portable, deterministic. Reads papers.yaml (+ optional
config/taxonomy.yaml and config/concepts.yaml) and emits a ranked concept
list as JSON. Composes with relate_concepts.py:

    python3 tools/extract_concepts.py --papers papers.yaml > concepts.json
    python3 tools/relate_concepts.py --papers papers.yaml \
        --concepts concepts.json --write-doc

Concept sources:
  1. taxonomy categories — from config/taxonomy.yaml, associated
     STRUCTURALLY (every paper in the category counts); these are the
     high-level backbone concepts.
  2. curated terms      — optional config/concepts.yaml (repo-specific
     important concepts/ideas), associated by text.
  3. emergent bigrams  — frequent noun bigrams mined from title+abstract,
     associated by text.

Each concept carries a `match` descriptor so relate_concepts.py knows how to
find its papers. Only stdlib + PyYAML. Works on ANY repo with papers.yaml;
taxonomy is optional.
"""
import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
TOKEN = re.compile(r"[a-z][a-z\-]+")

STOP = set("""
a an the and or but if then else for to of in on at by with from as is are was were be been being
this that these those it its their our your his her they we you i he she them us
we have has had do does did not no nor so than too very can will just should now
also more most other some such only into out up down over under again further
new using use used based approach method model study paper results show shows
proposed present presents presented paper research work works framework system
systems data analysis using via towards toward between within across among
which what when where who whom how why all any each both few many much
one two three first second third last next previous current recent
ai artificial intelligence machine learning deep neural network llms llm genai
development application method theory survey experiment review mechanism analysis
""".split())


def load_papers(path):
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f).get("papers", [])


def load_taxonomy_categories():
    """Return [(label, id)] for taxonomy categories."""
    p = REPO / "config" / "taxonomy.yaml"
    out = []
    if not p.exists():
        return out
    try:
        with open(p, encoding="utf-8") as f:
            cfg = yaml.safe_load(f) or {}
    except yaml.YAMLError:
        return out
    for c in cfg.get("taxonomy", {}).get("categories", []):
        disp = c.get("display", "")
        cid = c.get("id", "")
        if not disp and not cid:
            continue
        out.append((disp or cid, cid))
    return out


def load_curated():
    """Return [term] from optional config/concepts.yaml."""
    p = REPO / "config" / "concepts.yaml"
    if not p.exists():
        return []
    try:
        with open(p, encoding="utf-8") as f:
            cfg = yaml.safe_load(f) or {}
    except yaml.YAMLError:
        return []
    terms = []
    for t in cfg.get("concepts", []) or []:
        if isinstance(t, str):
            terms.append(t)
    terms += list((cfg.get("concepts_map") or {}).keys())
    return terms


def load_extraction_config():
    """Optional config/extraction.yaml: {"mode": "broad"|"selective"}.

    'selective' extracts only the structural (taxonomy) + curated seed
    concepts and skips the noisy emergent bigrams, yielding a clean,
    high-signal concept graph. Missing file or unknown mode => 'broad'.
    """
    p = REPO / "config" / "extraction.yaml"
    if not p.exists():
        return {}
    try:
        with open(p, encoding="utf-8") as f:
            cfg = yaml.safe_load(f) or {}
    except yaml.YAMLError:
        return {}
    return cfg


def mine_bigrams(papers, min_df):
    bi = Counter()
    for e in papers:
        toks = [t for t in TOKEN.findall(f"{e.get('title','')} {e.get('abstract','')}".lower())
                if t not in STOP and len(t) > 2]
        seen = set()
        for a, b in zip(toks, toks[1:]):
            if a not in STOP and b not in STOP:
                seen.add(f"{a} {b}")
        bi.update(seen)
    return {t: c for t, c in bi.items() if c >= min_df}


def main():
    ap = argparse.ArgumentParser(description="Extract concepts from a research corpus.")
    ap.add_argument("--papers", default="papers.yaml")
    ap.add_argument("--min-df", type=int, default=8)
    ap.add_argument("--max", type=int, default=120)
    ap.add_argument("--mode", choices=["broad", "selective"],
                    help="broad = taxonomy+curated+emergent (default); "
                         "selective = taxonomy+curated only (no emergent bigrams)")
    ap.add_argument("--out", help="write concepts JSON here (default: stdout)")
    args = ap.parse_args()
    cfg_mode = (load_extraction_config() or {}).get("mode")
    mode = args.mode or cfg_mode or "broad"
    if mode not in ("broad", "selective"):
        mode = "broad"

    papers = load_papers(args.papers)
    concepts = {}

    # 1) taxonomy categories — structural
    for label, cid in load_taxonomy_categories():
        df = sum(1 for e in papers if e.get("category") == cid)
        cells = Counter(f"{e.get('category','')}/{e.get('subcategory','')}"
                        for e in papers if e.get("category") == cid)
        concepts[label] = {"term": label, "kind": "taxonomy", "seed": True,
                           "df": df, "match": {"type": "field", "field": "category",
                                              "value": cid},
                           "top_cells": [k for k, _ in cells.most_common(4)]}

    # 2) curated — text
    for term in load_curated():
        concepts[term] = {"term": term, "kind": "curated", "seed": True,
                          "df": 0, "match": {"type": "text", "forms": [term.lower()]}}

    # 3) emergent bigrams — text (broad mode only)
    if mode == "broad":
        for term, df in sorted(mine_bigrams(papers, args.min_df).items(),
                               key=lambda x: -x[1])[:args.max]:
            if term not in concepts:
                concepts[term] = {"term": term, "kind": "emergent", "seed": False,
                                  "df": 0, "match": {"type": "text", "forms": [term]}}

    # text-match pass for curated + emergent
    text_cs = [c for c in concepts.values() if c["match"]["type"] == "text"]
    for c in text_cs:
        c["_toks"] = set()
        c["_pats"] = []
        for frm in c["match"]["forms"]:
            c["_toks"].update(frm.split())
            c["_pats"].append(re.compile(rf"\b{re.escape(frm)}\b"))
        c["cells"] = Counter()
    for e in papers:
        text = f" {e.get('title','')} {e.get('abstract','')} ".lower()
        toks = set(TOKEN.findall(text))
        cell = f"{e.get('category','')}/{e.get('subcategory','')}"
        for c in text_cs:
            if c["_toks"] <= toks and any(p.search(text) for p in c["_pats"]):
                c["df"] += 1
                c["cells"][cell] += 1

    out = []
    for c in concepts.values():
        cells = c.pop("cells", Counter())
        c.pop("_toks", None)
        c.pop("_pats", None)
        c["papers"] = c["df"]
        if not c.get("top_cells"):
            c["top_cells"] = [k for k, _ in cells.most_common(4)]
        if not c["seed"] and c["df"] == 0:
            continue
        out.append(c)

    out.sort(key=lambda x: (-x["df"], 0 if x["seed"] else 1))
    result = {"count": len(out), "concepts": out}
    text = json.dumps(result, indent=2, ensure_ascii=False)
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
        print(f"Wrote {len(out)} concepts to {args.out}", file=sys.stderr)
    else:
        print(text)


if __name__ == "__main__":
    main()
