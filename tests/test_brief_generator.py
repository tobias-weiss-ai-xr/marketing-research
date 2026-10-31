"""Tests for tools/brief_generator.py ranking (venue + recency boosts, dedup).

Self-contained: adds the repo root and tools/ to sys.path.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))

import brief_generator as bg


def test_venue_boost():
    assert bg._venue_boost("Journal of Business Research") == 2
    assert bg._venue_boost("Journal of the Academy of Marketing Science") == 2
    assert bg._venue_boost("Zenodo (CERN European Organization for Nuclear Research)") == 0
    assert bg._venue_boost("") == 0
    assert bg._venue_boost(None) == 0


def test_recency_boost():
    assert bg._recency_boost("2026-01", 2026) == 2
    assert bg._recency_boost("2025-12", 2026) == 2
    assert bg._recency_boost("2024-05", 2026) == 1
    assert bg._recency_boost("2023-01", 2026) == 1
    assert bg._recency_boost("2019-05", 2026) == 0
    assert bg._recency_boost("", 2026) == 0
    assert bg._recency_boost(None, 2026) == 0


def test_norm_title():
    assert bg._norm_title("The Power  of  Generative-Marketing!") == "the power of generative marketing"
    assert bg._norm_title(None) == ""
    assert bg._norm_title("") == ""


def test_find_papers_ranks_quality_first():
    papers = [
        {"title": "Weak venue old", "category": "ai-marketing", "subcategory": "empirical",
         "abstract": "generative ai marketing", "venue": "Some Unknown Journal", "date": "2019-01",
         "url": "https://a.example/1"},
        {"title": "Strong venue recent", "category": "ai-marketing", "subcategory": "empirical",
         "abstract": "generative ai marketing", "venue": "Journal of Business Research", "date": "2026-01",
         "url": "https://a.example/2"},
        {"title": "Strong venue mid", "category": "ai-marketing", "subcategory": "empirical",
         "abstract": "generative ai marketing", "venue": "Marketing Science", "date": "2024-06",
         "url": "https://a.example/3"},
    ]
    ranked = bg.find_papers(papers, "generative ai marketing", now_year=2026)
    assert [p["title"] for p in ranked] == ["Strong venue recent", "Strong venue mid", "Weak venue old"]


def test_find_papers_dedupes_near_identical_titles():
    papers = [
        {"title": "Agentic Marketing", "category": "ai-marketing", "subcategory": "empirical",
         "abstract": "agentic marketing", "venue": "Journal of Business Research", "date": "2026-01",
         "url": "https://a.example/1"},
        {"title": "Agentic   Marketing!!", "category": "ai-marketing", "subcategory": "empirical",
         "abstract": "agentic marketing", "venue": "Zenodo", "date": "2026-02",
         "url": "https://a.example/2"},
    ]
    ranked = bg.find_papers(papers, "agentic marketing", now_year=2026)
    assert len(ranked) == 1
    assert ranked[0]["title"] == "Agentic Marketing"  # the strong-venue copy wins


def test_find_papers_no_match():
    assert bg.find_papers([{"title": "Unrelated", "abstract": "nothing here",
                            "category": "brand", "subcategory": "empirical",
                            "venue": "", "date": "2026-01", "url": ""}],
                          "quantum teleportation", now_year=2026) == []
