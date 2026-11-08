"""Tests for scripts/build_knowledgebase.py + tools/kb_search.py helpers.

Self-contained: adds the repo root, scripts/ and tools/ to sys.path.
No network access in tests.
"""
import os
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.insert(0, os.path.join(ROOT, "scripts"))
sys.path.insert(0, os.path.join(ROOT, "tools"))

import build_knowledgebase as bk  # noqa: E402
import kb_search as ks  # noqa: E402


# ---------------- slugify ----------------

def test_slugify_basic():
    assert bk.slugify("The Power  of  Generative Marketing!") == "the-power-of-generative-marketing"


def test_slugify_unicode_and_length():
    s = bk.slugify("Café Pricing — Über-Analysis of consumer behaviour " * 3)
    assert s.startswith("cafe-pricing-uber-analysis")
    assert len(s) <= 80
    assert s == s.strip("-")


def test_slugify_empty_falls_back_to_hash():
    s = bk.slugify("", "https://arxiv.org/abs/2401.12345")
    assert s.startswith("paper-")
    assert len(s) == len("paper-") + 8


# ---------------- url extraction ----------------

def test_arxiv_id_extraction():
    assert bk.arxiv_id_from_url("https://arxiv.org/abs/2401.12345") == "2401.12345"
    assert bk.arxiv_id_from_url("https://arxiv.org/abs/2506.02088v2") == "2506.02088"
    assert bk.arxiv_id_from_url("https://doi.org/10.1108/jcm-04-2024-6806") is None


def test_doi_extraction():
    assert bk.doi_from_url("https://doi.org/10.3390/asi7020029") == "10.3390/asi7020029"
    assert bk.doi_from_url("https://arxiv.org/abs/2401.12345") is None


# ---------------- collect_targets ----------------

def _papers():
    return [
        {"title": "A", "url": "https://arxiv.org/abs/2401.00001", "category": "ai-marketing"},
        {"title": "B", "url": "https://arxiv.org/abs/2401.00002", "category": "ai-marketing"},
        {"title": "C", "url": "https://doi.org/10.1/abc", "category": "b2b"},
        {"title": "D", "url": "https://doi.org/10.1/def", "category": "brand"},
        {"title": "E", "url": "", "category": "b2b"},  # no url -> skipped
        {"title": "A", "url": "https://arxiv.org/abs/2401.00001", "category": "ai-marketing"},  # dup
    ]


def test_collect_targets_scope_arxiv():
    out = bk.collect_targets(_papers(), "arxiv")
    urls = [p["url"] for p in out]
    assert urls == ["https://arxiv.org/abs/2401.00001", "https://arxiv.org/abs/2401.00002"]


def test_collect_targets_scope_oa_round_robin():
    out = bk.collect_targets(_papers(), "oa")
    cats = [p["category"] for p in out]
    # round-robin: b2b and brand alternate, not blocked
    assert cats == ["b2b", "brand"]
    out2 = bk.collect_targets(_papers(), "oa", category="b2b")
    assert [p["title"] for p in out2] == ["C"]


# ---------------- index roundtrip ----------------

def test_index_save_load_roundtrip(tmp_path, monkeypatch):
    monkeypatch.setattr(bk, "INDEX_PATH", tmp_path / "index.json")
    idx = {"https://arxiv.org/abs/2401.00001": {"status": "ok", "chars": 100}}
    bk.save_index(idx, 5)
    loaded = bk.load_index()
    assert loaded["https://arxiv.org/abs/2401.00001"]["status"] == "ok"
    data = (tmp_path / "index.json").read_text()
    assert '"counts"' in data and '"corpus_papers": 5' in data


# ---------------- kb_search scoring ----------------

def test_tokenize():
    assert ks.tokenize("Agentic AI: lead-gen!") == ["agentic", "ai", "lead", "gen"]
    assert ks.tokenize("a x") == []  # 1-char tokens dropped


def test_score_doc_title_boost():
    rec = {"title": "Customer Churn in Retail"}
    text = "churn churn churn unrelated words " * 10
    s_body_only = ks.score_doc({"title": "Unrelated"}, text, ["churn"], "")[0]
    s_title = ks.score_doc(rec, text, ["churn"], "")[0]
    assert s_title > s_body_only  # title hit adds 5x


def test_score_doc_phrase_bonus():
    rec = {"title": "T"}
    text = "the phrase appears here exactly loyalty program once"
    with_phrase = ks.score_doc(rec, text, ["loyalty", "program"], "loyalty program")[0]
    without = ks.score_doc(rec, text, ["loyalty", "program"], "")[0]
    assert with_phrase == without + 10


def test_strip_front_matter():
    doc = "---\ntitle: X\n---\n\n# T\n\nbody text"
    assert ks.strip_front_matter(doc).startswith("\n# T")


def test_snippet_finds_body_not_front_matter():
    doc = "---\ntitle: 'A churn paper'\n---\n\n# A\n\nThis discusses churn deeply."
    sn = ks.snippet(doc, ["churn"])
    assert "title:" not in sn
    assert "discusses churn" in sn


# ---------------- scan-existing + browse index ----------------

def test_normalize_title():
    assert bk.normalize_title("The  Power of Gen-AI! (2026)") == "thepowerofgenai2026"
    assert bk.normalize_title(None) == ""


def test_title_from_file(tmp_path):
    fm = tmp_path / "a.md"
    fm.write_text("---\ntitle: 'Real Title'\n---\n\n# Heading\nbody")
    assert bk.title_from_file(fm, fm.read_text()) == "Real Title"
    hd = tmp_path / "b.md"
    hd.write_text("intro\n\n# First Heading\nmore")
    assert bk.title_from_file(hd, hd.read_text()) == "First Heading"
    pl = tmp_path / "Some_File_Name.md"
    pl.write_text("plain scraped text")
    assert bk.title_from_file(pl, pl.read_text()) == "Some File Name"


def test_scan_existing(tmp_path, monkeypatch):
    monkeypatch.setattr(bk, "KB_DIR", tmp_path)
    monkeypatch.setattr(bk, "TEXTS_DIR", tmp_path / "full_texts")
    papers = [{"title": "Known Marketing Paper", "url": "https://doi.org/10.1/x",
               "category": "b2b", "subcategory": "empirical", "date": "2025-01",
               "venue": "J"}]
    folder = tmp_path / "full_texts" / "ai-lead-marketing"
    folder.mkdir(parents=True)
    (folder / "Known_Marketing_Paper.md").write_text("full text here")
    (folder / "Unknown_Local_Doc.md").write_text("scraped stuff")
    index = {"https://arxiv.org/abs/1": {"status": "ok", "path": "full_texts/x/a.md"}}
    unlinked, linked, skipped = bk.scan_existing(index, papers)
    # neither scanned file matches the tracked arxiv path or a fetched paper
    assert (unlinked, linked, skipped) == (1, 1, 0)
    rec = index["file:full_texts/ai-lead-marketing/Known_Marketing_Paper.md"]
    assert rec["category"] == "b2b" and rec["source"] == "manual-linked"
    assert index["file:full_texts/ai-lead-marketing/Unknown_Local_Doc.md"]["url"] == ""
    # file whose paper was already fetched by pipeline -> skipped
    index2 = {"https://doi.org/10.1/x": {"status": "ok", "path": "full_texts/b2b/fetched.md"}}
    _, _, sk = bk.scan_existing(index2, papers)
    assert sk == 1


def test_write_browse_index(tmp_path, monkeypatch):
    monkeypatch.setattr(bk, "KB_DIR", tmp_path)
    index = {
        "a": {"status": "ok", "path": "full_texts/b2b/a.md", "category": "b2b",
              "title": "Alpha", "date": "2026-01", "pages": 10, "source": "arxiv"},
        "b": {"status": "no_oa", "path": None, "category": "b2b", "title": "Skip me"},
    }
    n = bk.write_browse_index(index)
    assert n == 1
    text = (tmp_path / "INDEX.md").read_text()
    assert "## b2b (1)" in text and "Alpha" in text and "Skip me" not in text
