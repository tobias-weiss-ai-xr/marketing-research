"""Offline tests for scripts/verify_sources.py (paper-link verifier).

Self-contained: adds the repo's ``scripts/`` dir to sys.path so it works
regardless of each corpus repo's existing ``tests/conftest.py``. Mirrors
grant-intelligence/mcp/test_verify_sources.py — same tool, corpus config style
(papers.yaml: list_key=papers, id_field=title, url_fields=[url, code_url,
project_url]). Network is mocked.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scripts"))

from unittest import mock

import pytest
import requests

import verify_sources as vs


def test_iter_entries_yaml_list_multi_field(tmp_path):
    txt = ("papers:\n"
           "- title: P1\n  url: https://p.example/1\n"
           "- title: P2\n  url: ''\n  code_url: https://c.example/2\n"
           "- title: P3\n  url: https://ok.example/3\n  code_url: ''\n  project_url: ''\n")
    (tmp_path / "papers.yaml").write_text(txt)
    cfg = {"file": "papers.yaml", "format": "yaml", "list_key": "papers",
           "id_field": "title", "url_fields": ["url", "code_url", "project_url"]}
    items = list(vs.iter_entries(cfg, str(tmp_path)))
    assert {i[0] for i in items} == {"P1", "P2", "P3"}
    assert len(items) == 3  # only non-empty url fields counted


def test_iter_entries_json_object_map(tmp_path):
    src = {"ev": {"name": "EV", "url": "https://ev.example"},
           "kas": {"name": "KAS", "url": ""}}
    (tmp_path / "sources.json").write_text(__import__("json").dumps(src))
    cfg = {"file": "sources.json", "object_map": True, "id_field": "key",
           "url_fields": ["url"]}
    items = list(vs.iter_entries(cfg, str(tmp_path)))
    assert {i[0] for i in items} == {"ev"}


class _FakeResp:
    def __init__(self, status):
        self.status_code = status


def _fake_get(url, **kw):
    if "dead.example" in url:
        return _FakeResp(404)
    if "block.example" in url:
        return _FakeResp(403)
    if "down.example" in url:
        raise requests.exceptions.ConnectionError("x")
    if "slow.example" in url:
        raise requests.exceptions.Timeout("x")
    return _FakeResp(200)


def test_http_check_classification():
    with mock.patch("requests.get", side_effect=_fake_get):
        assert vs.http_check("https://ok.example", 5, vs.DEFAULT_UA)["kind"] == "ok"
        assert vs.http_check("https://dead.example", 5, vs.DEFAULT_UA)["kind"] == "broken"
        assert vs.http_check("https://block.example", 5, vs.DEFAULT_UA)["kind"] == "uncertain"
        assert vs.http_check("https://down.example", 5, vs.DEFAULT_UA)["kind"] == "broken"


def test_resolve_verdict():
    assert vs.resolve_verdict("ok", None) == "ok"
    assert vs.resolve_verdict("broken", None) == "broken"
    assert vs.resolve_verdict("uncertain", None) == "botblock"
    assert vs.resolve_verdict("uncertain", "ok") == "ok"
    assert vs.resolve_verdict("uncertain", "broken") == "broken"


def _write_cfg(tmp_path, papers):
    (tmp_path / "papers.yaml").write_text(__import__("json").dumps({"papers": papers}))
    return {
        "inputs": [{"file": "papers.yaml", "format": "yaml", "list_key": "papers",
                    "id_field": "title", "url_fields": ["url", "code_url"]}],
        "settings": {"browser": False, "fail_on_broken": True,
                     "report": str(tmp_path / "r.json")},
    }


def test_run_counts_ok_broken_botblock(tmp_path):
    papers = [
        {"title": "A", "url": "https://ok.example/a"},
        {"title": "B", "url": "https://dead.example/b"},
        {"title": "C", "url": "https://block.example/c"},
    ]
    cfg = _write_cfg(tmp_path, papers)
    with mock.patch("requests.get", side_effect=_fake_get):
        totals, results, status = vs.run(cfg, str(tmp_path / "x.json"))
    assert totals["ok"] == 1 and totals["broken"] == 1 and totals["botblock"] == 1
    assert status == 1  # broken -> fail


def test_run_botblock_does_not_fail(tmp_path):
    papers = [{"title": "C", "url": "https://block.example/c"}]
    cfg = _write_cfg(tmp_path, papers)
    with mock.patch("requests.get", side_effect=_fake_get):
        totals, results, status = vs.run(cfg, str(tmp_path / "x.json"))
    assert totals["broken"] == 0 and status == 0


def test_main_no_fail_override(tmp_path, capsys):
    papers = [{"title": "B", "url": "https://dead.example/b"}]
    (tmp_path / "papers.yaml").write_text(__import__("json").dumps({"papers": papers}))
    cfgf = tmp_path / "cfg.json"
    cfgf.write_text(__import__("json").dumps({
        "inputs": [{"file": "papers.yaml", "format": "yaml", "list_key": "papers",
                    "id_field": "title", "url_fields": ["url"]}],
        "settings": {"report": str(tmp_path / "r.json")},
    }))
    with mock.patch("requests.get", side_effect=_fake_get):
        rc = vs.main([str(cfgf), "--no-fail"])
    assert rc == 0
