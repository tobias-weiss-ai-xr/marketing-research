<h1 align="center">
  <strong>Marketing Research Corpus</strong>
</h1>
<h3 align="center">Latest marketing trends: AI & generative marketing, digital/performance, social & creator, privacy-first data, analytics/MMM, B2B/ABM</h3>

### 🔗 Links

- **GitHub**: https://github.com/tobias-weiss-ai-xr/marketing-research
- **License**: https://github.com/tobias-weiss-ai-xr/marketing-research/blob/main/LICENSE
- **CI**: https://github.com/tobias-weiss-ai-xr/marketing-research/actions/workflows/validate.yml
- **Business Dev**: https://github.com/tobias-weiss-ai-xr/business-development-research
- **AI Literacy**: https://github.com/tobias-weiss-ai-xr/ai-literacy-research


> 📢 **Marketing research corpus:** AI & generative marketing, digital & performance,
> social media & creator economy, content marketing, consumer behavior, brand,
> analytics, privacy-first data, CX & retail, B2B/ABM — analyzed with the same
> pipeline as the other `*-research` corpus repos.

<p align="center">
  <img src="https://raw.githubusercontent.com/tobias-weiss-ai-xr/marketing-research/main/assets/visualizations/category_distribution.png" alt="Teaser" width="600" />
</p>

---

## What you get

| Capability | How |
|------------|-----|
| 📄 **Curated corpus** | `papers.yaml` is the source of truth — one structured entry per paper |
| ✅ **Auto-validation** | `scripts/validate_papers.py` checks schema, duplicates, URL normalization, LaTeX artifacts |
| 🧾 **Auto-generated README** | `scripts/generate_readme.py` renders the paper list grouped by your taxonomy |
| 📊 **Statistics & trends** | `scripts/standard_stats.py` → `statistics.json` (momentum, gaps, bursts, venues, authors) |
| 🔍 **Literature review report** | `scripts/analysis/generate_reports.py` → `docs/research/literature_review.md` + `trends.md` |
| 🧭 **Topic planning** | `tools/topic_planner.py`, `tools/trend_scanner.py`, `tools/landscape_analyzer.py`, `tools/brief_generator.py` |
| 🔎 **New paper discovery** | `scripts/fetch/fetch_new_papers.py` (arXiv), `fetch_other_sources.py` (dblp/crossref/europepmc), `fetch_openalex_bulk.py` |
| 🐙 **GitHub repos discovery** | `scripts/fetch/fetch_github_repos.py` (optional, config-driven via `github_queries` in taxonomy.yaml) |
| 🦊 **GitLab projects discovery** | `scripts/fetch/fetch_gitlab_repos.py` (optional, config-driven via `gitlab_queries` in taxonomy.yaml) |
| 🏠 **Codeberg repos discovery** | `scripts/fetch/fetch_codeberg_repos.py` (optional, config-driven via `codeberg_queries` in taxonomy.yaml) |
| 🖥️ **GitHub Pages site** | `docs/index.html` — searchable, filterable paper browser |
| 🤖 **Agentic workflow** | `AGENTS.md` + `config/taxonomy.yaml` make this repo agent-friendly by design |

## 🚀 Quick Start

```bash
# 1. Clone
git clone https://github.com/tobias-weiss-ai-xr/marketing-research.git
cd marketing-research

# 2. Install dependencies
pip install -r requirements.txt

# 3. Validate + generate
python3 scripts/validate_papers.py
python3 scripts/generate_readme.py
python3 scripts/standard_stats.py
python3 scripts/analysis/generate_reports.py
```

## 📖 How it works

```
config/taxonomy.yaml ──► papers.yaml ──► validate_papers.py
                          │   ▲              │
                          ▼   └── fetch_* ───┘
                   generate_readme.py ──► README.md (auto)
                          │
                          ▼
                  standard_stats.py ──► statistics.json, docs/papers.json
                          │
                          ▼
              analysis/generate_reports.py ──► docs/research/*.md
```

- **Never edit README.md directly** — it is generated from `papers.yaml`.
- The **taxonomy lives in one place** (`config/taxonomy.yaml`); every script reads it via `scripts/research_config.py`.
- **CI (validate.yml)** runs on every push/PR and weekly to discover new papers.

## 🧪 Local pipeline (all in one)

```bash
# Full pipeline (validate → README → stats → reports)
python3 scripts/validate_papers.py && \
python3 scripts/generate_readme.py && \
python3 scripts/standard_stats.py && \
python3 scripts/analysis/generate_reports.py
```

## 🤖 Agentic workflow (AGENTS.md)

This repo is designed to be driven by coding agents (OpenCode, Claude Code, …):

- **Spec-style guardrails** in `AGENTS.md` — agents know the pipeline, never edit README, always re-validate.
- **One config file** to change → one re-run to verify (low context cost for agents).
- **Auto-validation** gives agents an objective pass/fail signal.
- **Weekly discovery** keeps the corpus fresh without human babysitting.

## 📊 Corpus Statistics

**7,378 papers** across **11 categories**.
Sources: **arXiv** 46 (1%) · **DOI** 7017 (95%) · **Other** 315 (4%).
Full paper list: [GitHub Pages site](https://tobias-weiss-ai-xr.github.io/marketing-research).

### Top categories

| Category | Papers | Recent | |
|----------|--------|--------|-
| ai-marketing | **886** | 461 | ████████████ |
| consumer-behavior | **871** | 463 | ████████████ |
| brand | **857** | 441 | ████████████ |
| social-media | **839** | 433 | ███████████░ |
| survey | **808** | 402 | ███████████░ |
| cx-retail | **799** | 433 | ███████████░ |
| digital-marketing | **647** | 307 | █████████░░░ |
| analytics | **508** | 304 | ███████░░░░░ |
| content-marketing | **437** | 234 | ██████░░░░░░ |
| privacy-data | **396** | 180 | █████░░░░░░░ |
| b2b | **330** | 170 | ████░░░░░░░░ |

### By year

| Year | Papers | |
|------|--------|-
| 1987 | 1 | ░░░░░░░░░░░░ |
| 1988 | 1 | ░░░░░░░░░░░░ |
| 1992 | 1 | ░░░░░░░░░░░░ |
| 2004 | 1 | ░░░░░░░░░░░░ |
| 2005 | 1 | ░░░░░░░░░░░░ |
| 2011 | 1 | ░░░░░░░░░░░░ |
| 2012 | 1 | ░░░░░░░░░░░░ |
| 2013 | 2 | ░░░░░░░░░░░░ |
| 2014 | 2 | ░░░░░░░░░░░░ |
| 2015 | 3 | ░░░░░░░░░░░░ |
| 2016 | 3 | ░░░░░░░░░░░░ |
| 2017 | 3 | ░░░░░░░░░░░░ |
| 2018 | 2 | ░░░░░░░░░░░░ |
| 2019 | 5 | ░░░░░░░░░░░░ |
| 2020 | 3 | ░░░░░░░░░░░░ |
| 2021 | 6 | ░░░░░░░░░░░░ |
| 2022 | 2 | ░░░░░░░░░░░░ |
| 2023 | 32 | ░░░░░░░░░░░░ |
| 2024 | 2035 | ████████░░░░ |
| 2025 | 2087 | ████████░░░░ |
| 2026 | 3186 | ████████████ |

### Momentum (hottest categories)

| Category | Total | Rate | Recent | Score |
|----------|-------|------|--------|-------|
| analytics | 508 | 25.3/mo | 59% | 162.5 |
| consumer-behavior | 871 | 38.6/mo | 53% | 132.0 |
| social-media | 839 | 36.1/mo | 51% | 130.5 |
| b2b | 330 | 14.2/mo | 51% | 126.8 |
| cx-retail | 799 | 36.1/mo | 54% | 114.6 |

### Trending keywords

| Keyword | Papers | Burst |
|---------|--------|-------|
| agentic | 20 | 1.83 |
| incrementality | 10 | 1.35 |
| genai | 46 | 1.3 |
| creator | 45 | 1.28 |
| cx | 49 | 1.26 |
| account-based | 28 | 1.24 |
| llm | 41 | 1.22 |
| tiktok | 153 | 1.18 |

### Top venues

| Venue | Papers |
|-------|--------|
| Zenodo (CERN European Organization for Nuclear Research) | 425 |
| SSRN Electronic Journal | 113 |
| Sustainability | 80 |
| Journal of theoretical and applied electronic commerce research | 58 |
| International Journal For Multidisciplinary Research | 49 |
| Journal of Marketing Analytics | 49 |
| Journal of Business Research | 49 |
| Journal of Retailing and Consumer Services | 48 |

### Research gaps (thinnest cells)

| Cell | Papers |
|------|--------|
| `b2b/measurement` | 7 |
| `content-marketing/empirical` | 32 |
| `analytics/theory` | 35 |
| `b2b/review` | 41 |
| `content-marketing/measurement` | 42 |
| `b2b/theory` | 42 |
| `brand/theory` | 46 |
| `analytics/framework` | 47 |

*Generated by `scripts/standard_stats.py`.*

## 📖 Citation

If you use this corpus in your work, please cite:

```bibtex
@software{marketing_research,
  author = {Tobias Weiss},
  title = {Marketing Research Corpus},
  year = {2026},
  url = {https://github.com/tobias-weiss-ai-xr/marketing-research},
}
```

## 📄 License

MIT — see [LICENSE](LICENSE).
