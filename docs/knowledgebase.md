# Marketing Knowledgebase — full texts from the corpus

A **local, searchable full-text library** built from the research corpus
(`papers.yaml`). The corpus stores metadata + abstracts; this knowledgebase
adds the **full texts** for every paper whose full text is openly
accessible.

Everything under `knowledgebase/` is **gitignored** ("local-only research
artifacts"): the fetched texts live on disk only. What IS committed and
reproducible:

- `scripts/build_knowledgebase.py` — the build pipeline
- `tools/kb_search.py` — the search tool
- this doc

## Coverage model (two tiers)

| Tier | Source | Papers | Yield |
|---|---|---|---|
| 1 `--scope arxiv` | arXiv PDFs (direct, free) | ~1,272 | ~100% |
| 2 `--scope oa` | DOI papers resolved via OpenAlex `best_oa_location` | ~13,083 eligible | partial (publisher-dependent; many OA links are HTML landing pages or bot-blocked) |

Corpus snapshot 2026-11-08: 15,779 papers → 1,272 arXiv (free full text) +
13,083 DOI + 2 PMC + others. `--scope all` runs both tiers.

## Build

```bash
python3.12 scripts/build_knowledgebase.py --scope arxiv            # tier 1 (~20 min, 6 workers)
python3.12 scripts/build_knowledgebase.py --scope oa --limit 300   # bounded best-effort tier 2
python3.12 scripts/build_knowledgebase.py --scope oa               # ALL remaining DOI papers (~90 min)
python3.12 scripts/build_knowledgebase.py --scope all              # everything (slow)
python3.12 scripts/build_knowledgebase.py --category ai-marketing  # one category only
python3.12 scripts/build_knowledgebase.py --dry-run                # plan only
python3.12 scripts/build_knowledgebase.py --stats                  # manifest summary
python3.12 scripts/build_knowledgebase.py --scan-existing          # absorb pre-existing manual full texts
python3.12 scripts/build_knowledgebase.py --write-index            # regenerate knowledgebase/INDEX.md
```

- **Resume-safe**: papers already recorded `ok` in the manifest are skipped;
  progress checkpoints every 25 completions. Re-run freely after
  interruptions or new ingestion rounds.
- Requires `pypdf` (`pip install pypdf --user --break-system-packages`) and
  `requests`/`pyyaml` (already in `requirements.txt`).
- Politeness: arXiv downloads are throttled (0.25 s each), OpenAlex uses the
  polite-pool mailto from `config/taxonomy.yaml`.

## Output layout

```
knowledgebase/
├── index.json                     # manifest: per-paper status, path, pages, chars
├── INDEX.md                       # auto-generated browsable listing (grouped by category)
└── full_texts/
    ├── ai-marketing/<slug>.md     # one file per paper
    ├── b2b/<slug>.md
    └── ...
```

Each file: YAML front matter (title, url, category/subcategory, date, venue,
authors, source, pages, chars, fetched_at) followed by the extracted full
text.

Manifest statuses: `ok` · `no_text` (scanned/image PDF) · `extract_failed` ·
`download_failed` · `not_pdf` · `landing_page` (OA tier: all candidates were
HTML) · `no_oa` (OA tier: no open-access location).

## Search

```bash
python3.12 tools/kb_search.py "customer churn retention" --limit 10
python3.12 tools/kb_search.py "agentic negotiation" --category ai-marketing
python3.12 tools/kb_search.py --stats
python3.12 tools/kb_search.py "loyalty program" --json     # machine-readable
```

Ranking: exact-phrase hits get a large bonus, title matches are boosted 5×,
body hits counted once each. Snippets skip the front matter.

## Reading a paper

```bash
ls knowledgebase/full_texts/analytics/
less knowledgebase/full_texts/analytics/improving-the-capabilities-of-*.md
```

## Caveats

- Extracted text comes from publisher PDFs; math/tables/figures may be
  garbled — cite the canonical `url` from the front matter, not the extract.
- `no_text` papers are image-only scans; OCR is out of scope.
- Copyright: files stay local (gitignored); the pipeline only fetches
  openly accessible copies.
- Pre-existing manually-collected files in `full_texts/` are absorbed into
  the manifest by `--scan-existing` (linked to papers.yaml metadata by
  title match when possible, `source: manual` otherwise). Unindexed PDFs
  in manual folders are not searchable.
