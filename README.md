<h1 align="center">
  <strong>Marketing Research Corpus</strong>
</h1>
<h3 align="center">Latest marketing trends: AI & generative marketing, digital/performance, social & creator, privacy-first data, analytics/MMM, B2B/ABM</h3>

<div align="center">
  [![GitHub](https://img.shields.io/badge/GitHub-tobias-weiss-ai-xr/marketing--research-181717.svg?logo=github)](https://github.com/tobias-weiss-ai-xr/marketing-research)
  [![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
  [![CI](https://img.shields.io/github/actions/workflow/status/tobias-weiss-ai-xr/marketing--research/validate.yml?label=CI&logo=github)](https://github.com/tobias-weiss-ai-xr/marketing-research/actions/workflows/validate.yml)
  [![Business Dev](https://img.shields.io/badge/Business Dev-business--development--research-blue.svg?logo=github)](https://github.com/tobias-weiss-ai-xr/business-development-research) [![AI Literacy](https://img.shields.io/badge/AI Literacy-ai--literacy--research-blue.svg?logo=github)](https://github.com/tobias-weiss-ai-xr/ai-literacy-research)
</div>

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
Sources: **arXiv** 46 (0%) · **DOI** 7,017 (95%) · **Other** 315 (4%).  
Full paper list: [GitHub Pages site](https://tobias-weiss-ai-xr.github.io/marketing-research).

### Top categories

| Category | Papers | Recent | |
|----------|--------|--------|-|
| ai-marketing | **886** | 0 | ████████████ |
| consumer-behavior | **871** | 0 | ███████████░ |
| brand | **857** | 0 | ███████████░ |
| social-media | **839** | 0 | ███████████░ |
| survey | **808** | 0 | ██████████░░ |
| cx-retail | **799** | 0 | ██████████░░ |
| digital-marketing | **647** | 0 | ████████░░░░ |
| analytics | **508** | 0 | ██████░░░░░░ |
| content-marketing | **437** | 0 | █████░░░░░░░ |
| privacy-data | **396** | 0 | █████░░░░░░░ |
| *other* | **330** | | |


### By year

| Year | Papers | |
|------|--------|-|
| 2025 | 2,087 | ███████░░░░░ |
| 2026 | 3,185 | ████████████ |
| 2027 | 1 | ░░░░░░░░░░░░ |


### Momentum (hottest categories)

| Category | Total | Rate | Recent | Score |
|----------|-------|------|--------|-------|
| Analytics | 508 | 25.3/mo | 60% | 162 |
| Consumer Behavior | 871 | 38.6/mo | 53% | 132 |
| Social Media | 839 | 36.1/mo | 52% | 130 |
| B2B | 330 | 14.2/mo | 52% | 127 |
| Cx Retail | 799 | 36.1/mo | 54% | 115 |


### Trending keywords

| Keyword | Papers | Burst |
|---------|--------|-------|
| agentic | 20 | 1.83 |
| diffusion | 19 | 1.72 |
| dataset | 44 | 1.71 |
| hierarchical | 9 | 1.71 |
| benchmark | 7 | 1.65 |
| explainab | 21 | 1.47 |
| uncertainty | 24 | 1.45 |
| scalable | 12 | 1.45 |


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



*Generated 2027-01 by `scripts/standard_stats.py`.*

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
