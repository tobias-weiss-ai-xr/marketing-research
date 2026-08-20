# Changelog

## [0.1.4] — 2026-08-20
- Stabilize CI: `discover` job gets its own concurrency group (was self-cancelling on its own push via shared group); now regenerates README stats + assets and commits papers.yaml + README.md + assets/graph_analysis.json so the corpus stays consistent after each refresh.
- Fix `standard_stats.py`: replaced skeleton's generic RL `BURST_KEYWORDS` with marketing terms; added README 'Corpus Statistics' section self-healing (regenerated between markers on every run).

## [0.1.3] — 2026-08-16
- Topped up 3 thin cells (b2b/measurement, content-marketing/framework, privacy-data/framework) via proxy host; corpus 5,068 → 5,201 papers, all 66 cells >=7.
- Living corpus: scheduled weekly OpenAlex incremental refresh (GitHub Actions `discover` job, replaces arXiv-only skeleton step); `workflow_dispatch` added for manual runs.

## [0.1.2] — 2026-08-16
- Gap-filling round via proxy hosts (contextual-intelligence.org, tobi-yoga, tobias-weiss.org): corpus 2,349 → 5,068 papers, saturation 31.8% → 100% (66/66 taxonomy cells).

## [0.1.1] — 2026-08-16
- Bootstrap marketing corpus: 2,349 papers (OpenAlex bulk + CrossRef/dblp/Europe PMC), marketing taxonomy (11 categories × 6 subcategories), subcategory keyword rules + subcategory_hint support in OpenAlex fetcher, fixed import bootstrap, trends brief (TRENDS.md).

## [0.1.0] — 2026-08-06
- Initial skeleton: config-driven taxonomy, validation, README generation, statistics, reports, discovery, GitHub Pages, CI, AGENTS.md.
