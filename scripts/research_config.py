#!/usr/bin/env python3
"""Shared config loader for the *-research skeleton.

Reads config/taxonomy.yaml and exposes:
  - topic metadata (name, short, description)
  - categories / subcategories with display names
  - arxiv_queries, other_sources_queries, openalex_queries
  - trend_keywords (for burst/trend analysis)
  - subcategory_keywords (for auto-classification)
  - openalex_mailto (for polite-pool API access)

All scripts use this module, so the taxonomy lives in ONE place.
"""

import os
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent

# Fallback keyword lists used when taxonomy.yaml does not define them.
# These are intentionally generic; each repo should override via config.
_DEFAULT_TREND_KEYWORDS = [
    "survey", "benchmark", "dataset", "evaluation", "method", "framework",
    "learning", "model", "system", "application", "tool", "real-world",
    "scalable", "novel", "analysis", "review", "human", "autonomous",
]


def load_config(path=None):
    path = path or (REPO / "config" / "taxonomy.yaml")
    if not path.exists():
        # Fallback: minimal default taxonomy (keeps scripts runnable out-of-the-box)
        return {
            "topic": {"name": "Research Corpus", "short": "research"},
            "taxonomy": {
                "categories": [{"id": "method", "display": "Methods"}],
                "subcategories": [{"id": "core", "display": "Core"}],
            },
            "arxiv_queries": [],
            "other_sources_queries": [],
            "openalex_queries": [],
            "trend_keywords": list(_DEFAULT_TREND_KEYWORDS),
            "subcategory_keywords": [],
        }
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def get_topic(cfg):
    return cfg.get("topic", {})


def get_categories(cfg):
    """Return ordered list of category dicts {id, display}."""
    return cfg.get("taxonomy", {}).get("categories", [])


def get_subcategories(cfg):
    return cfg.get("taxonomy", {}).get("subcategories", [])


def category_display(cfg, cat_id):
    for c in get_categories(cfg):
        if c.get("id") == cat_id:
            return c.get("display", cat_id)
    return cat_id


def subcategory_display(cfg, sub_id):
    for s in get_subcategories(cfg):
        if s.get("id") == sub_id:
            return s.get("display", sub_id)
    return sub_id


def get_trend_keywords(cfg):
    """Return trend/burst keywords from config, falling back to defaults.

    Used by standard_stats.py, trend_scanner.py, and landscape_analyzer.py
    for keyword-burst analysis.  Each repo should define topic-specific
    keywords in taxonomy.yaml under ``trend_keywords``.
    """
    kw = cfg.get("trend_keywords", [])
    if kw:
        return kw
    return list(_DEFAULT_TREND_KEYWORDS)


def get_subcategory_keywords(cfg):
    """Return a list of (subcategory_id, [keywords]) for auto-classification.

    Reads ``subcategory_keywords`` from taxonomy.yaml.  Each entry is a
    mapping with ``id`` (matching a subcategory id) and ``keywords`` (list).
    Falls back to an empty list (callers then use heuristic rules).
    """
    out = []
    for item in cfg.get("subcategory_keywords", []):
        sid = item.get("id", "")
        kws = item.get("keywords", [])
        if sid and kws:
            out.append((sid, kws))
    return out


def get_openalex_mailto(cfg):
    """Return the OpenAlex polite-pool email from config or env."""
    cfg_mailto = cfg.get("topic", {}).get("openalex_mailto", "")
    return os.environ.get("OPENALEX_MAILTO", cfg_mailto or "research@tobias-weiss-ai-xr.de")


def load_papers(path=None):
    path = path or (REPO / "papers.yaml")
    if not path.exists():
        return []
    with open(path, encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    return data.get("papers", [])


if __name__ == "__main__":
    cfg = load_config()
    print("Topic:", get_topic(cfg).get("name"))
    print("Categories:", [c["id"] for c in get_categories(cfg)])
    print("Subcategories:", [s["id"] for s in get_subcategories(cfg)])
    print("arXiv queries:", len(cfg.get("arxiv_queries", [])))
    print("Trend keywords:", len(get_trend_keywords(cfg)))
    print("Subcategory keywords:", len(get_subcategory_keywords(cfg)))
    print("OpenAlex mailto:", get_openalex_mailto(cfg))
