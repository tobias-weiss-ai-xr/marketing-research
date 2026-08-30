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
import sys
from pathlib import Path

import yaml

# Many scripts/tools print emoji and unicode dashes; on Windows the default
# cp1252 stdout encoding cannot represent them and raises UnicodeEncodeError.
# Force UTF-8 output once here so every consumer (which imports this module)
# is covered. CI (Linux) is unaffected.
try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):  # pragma: no cover - non-TTY / old Python
    pass

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


def display_name(cfg, kebab):
    """Return the display name for a category OR subcategory id.

    Prefers the configured ``display`` value; falls back to a title-cased
    version of the kebab id (e.g. ``"method"`` -> ``"Method"``, ``"real-world"``
    -> ``"Real World"``).  Shared by report/tool generators so display logic
    lives in one place.
    """
    disp = category_display(cfg, kebab)
    if disp != kebab:
        return disp
    disp = subcategory_display(cfg, kebab)
    if disp != kebab:
        return disp
    return kebab.replace("-", " ").replace("_", " ").title()


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
    raw = cfg.get("subcategory_keywords", [])
    out = []
    if isinstance(raw, dict):
        # Schema: {subcat_id: [keywords]} (dict map)
        items = [{"id": k, "keywords": v if isinstance(v, list) else [v]} for k, v in raw.items()]
    elif isinstance(raw, list):
        # Schema: [{id, keywords}] or [id, ...] (bare ids)
        items = [i if isinstance(i, dict) else {"id": i, "keywords": []} for i in raw]
    else:
        items = []
    for item in items:
        sid = item.get("id", "")
        kws = item.get("keywords", [])
        if not isinstance(kws, list):
            kws = [kws]
        if sid and kws:
            out.append((sid, kws))
    return out


def get_openalex_mailto(cfg):
    """Return the OpenAlex polite-pool email from config or env."""
    cfg_mailto = cfg.get("topic", {}).get("openalex_mailto", "")
    return os.environ.get("OPENALEX_MAILTO", cfg_mailto or "research@tobias-weiss-ai-xr.de")


def load_papers(path=None):
    """Return the list of paper dicts from papers.yaml (empty if absent)."""
    path = path or (REPO / "papers.yaml")
    if not path.exists():
        return []
    with open(path, encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    return data.get("papers", [])


def validate_config(cfg, path=None):
    """Validate the structure of a taxonomy config and return a list of errors.

    Catches common user mistakes early (missing/invalid categories,
    subcategories, or a malformed taxonomy) so downstream scripts fail fast
    with a clear message instead of misbehaving silently.

    Returns a ``list[str]`` of human-readable problems (empty when valid).
    """
    import re as _re

    errors = []

    if not isinstance(cfg, dict):
        return [f"Config must be a mapping, got {type(cfg).__name__}: {path or 'N/A'}"]

    topics = cfg.get("topic")
    if not isinstance(topics, dict) or not topics.get("name"):
        errors.append("config missing 'topic.name' (used for README header + discovery)")

    taxonomy = cfg.get("taxonomy")
    if not isinstance(taxonomy, dict):
        errors.append("config missing or invalid 'taxonomy' section")
        return errors

    cats = taxonomy.get("categories", [])
    if not isinstance(cats, list) or not cats:
        errors.append("taxonomy.categories must be a non-empty list")
    else:
        ids = []
        for i, c in enumerate(cats):
            if not isinstance(c, dict) or not c.get("id"):
                errors.append(f"taxonomy.categories[{i}] missing an 'id'")
            elif c["id"] in ids:
                errors.append(f"taxonomy.categories has duplicate id '{c['id']}'")
            else:
                ids.append(c["id"])
            if not _re.fullmatch(r"[a-z0-9-]+", str(c.get("id", ""))):
                errors.append(f"taxonomy.categories id '{c.get('id')}' must be lowercase kebab-case")

    subs = taxonomy.get("subcategories", [])
    if not isinstance(subs, list) or not subs:
        errors.append("taxonomy.subcategories must be a non-empty list")
    else:
        ids = []
        for i, s in enumerate(subs):
            if not isinstance(s, dict) or not s.get("id"):
                errors.append(f"taxonomy.subcategories[{i}] missing an 'id'")
            elif s["id"] in ids:
                errors.append(f"taxonomy.subcategories has duplicate id '{s['id']}'")
            else:
                ids.append(s["id"])
            if not _re.fullmatch(r"[a-z0-9-]+", str(s.get("id", ""))):
                errors.append(f"taxonomy.subcategories id '{s.get('id')}' must be lowercase kebab-case")

    # Validate subcategory_keywords reference real subcategories
    for item in cfg.get("subcategory_keywords", []) or []:
        sid = item.get("id", "") if isinstance(item, dict) else ""
        if sid and subs and sid not in {s.get("id") for s in subs}:
            errors.append(f"subcategory_keywords id '{sid}' does not match any subcategory")

    return errors


def require_valid_config(path=None):
    """Load and validate the config, raising SystemExit(1) on problems.

    Pipeline scripts call this at startup so that a malformed
    ``config/taxonomy.yaml`` fails fast with a clear message instead of
    misbehaving silently.
    """
    import sys as _sys

    cfg = load_config(path)
    errs = validate_config(cfg, path)
    if errs:
        print(f"ERROR: invalid config ({path or REPO / 'config' / 'taxonomy.yaml'}):",
              file=_sys.stderr)
        for e in errs:
            print(f"  - {e}", file=_sys.stderr)
        _sys.exit(1)
    return cfg


def main(_argv=None):
    import sys as _sys

    cfg = load_config()
    errs = validate_config(cfg)
    if errs:
        print("CONFIG ERRORS:", file=_sys.stderr)
        for e in errs:
            print(f"  - {e}", file=_sys.stderr)
        _sys.exit(1)
    print("Topic:", get_topic(cfg).get("name"))
    print("Categories:", [c["id"] for c in get_categories(cfg)])
    print("Subcategories:", [s["id"] for s in get_subcategories(cfg)])
    print("arXiv queries:", len(cfg.get("arxiv_queries", [])))
    print("Trend keywords:", len(get_trend_keywords(cfg)))
    print("Subcategory keywords:", len(get_subcategory_keywords(cfg)))
    print("OpenAlex mailto:", get_openalex_mailto(cfg))


if __name__ == "__main__":
    main()
