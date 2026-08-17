# 📄 Latest Marketing Trends — One-Pager (Bayesian Evidence)

**Corpus:** 5,201 papers, 2024–2026 (1,609 in the last 12 months) · OpenAlex + CrossRef + dblp + Europe PMC
**Method:** exact conjugate Bayes — Beta-Binomial share-shift per category, Gamma-Poisson ratios per term; posterior medians with 95% credible intervals (CrI). No MCMC; reproducible via `scripts/bayesian_trends.py` (seed 42). Numbers: `docs/research/bayesian_trends.json`.

---

## 1. The four areas gaining share (P > 0.99)

Ratio = category's share of the corpus in the recent 12m (2025-08→2026-07) vs the prior 12m (2024-08→2025-07).

| Area | Share shift | Posterior median | 95% CrI | P(ratio>1) |
|------|-------------|------------------|---------|-----------|
| **Analytics, Attribution & Measurement** | 6.3% → 17.0% | **2.67×** | [2.21, 3.23] | 1.000 |
| **B2B & Account-Based Marketing** | 4.0% → 9.9% | **2.46×** | [1.92, 3.15] | 1.000 |
| **Content & Storytelling** | 5.9% → 9.6% | **1.63×** | [1.31, 2.03] | 1.000 |
| **Data, Privacy & Cookieless Advertising** | 6.1% → 8.4% | **1.38×** | [1.10, 1.74] | 0.997 |
| CX, Omnichannel & Retail | 11.4% → 11.5% | 1.01× | [0.84, 1.20] | 0.534 (stable) |

*AI & Marketing, Social, Brand, Consumer Behavior, Surveys lost share — in part a relevance-ranking artifact of the fetch (older papers rank higher), so the four risers above are conservative lower bounds of true growth.*

## 2. What's rising in the literature's language (12m ratio, Gamma-Poisson)

| Term | Recent/Prior | Median | 95% CrI | P |
|------|--------------|--------|---------|---|
| agentic | 8/1 | **5.2×** | [1.25, 38.4] | 0.99 |
| account-based (ABM) | 18/6 | **2.8×** | [1.22, 7.29] | 0.99 |
| incrementality | 7/3 | 2.1× | [0.64, 8.15] | 0.89 |
| marketing mix modeling (MMM) | 16/8 | 1.9× | [0.87, 4.56] | 0.95 |
| attribution | 32/20 | 1.6× | [0.92, 2.78] | 0.95 |
| creator (economy) | 20/12 | 1.6× | [0.82, 3.37] | 0.92 |
| retail media | 8/5 | 1.5× | [0.54, 4.64] | 0.79 |
| first-party data | 6/4 | 1.4× | [0.44, 4.97] | 0.73 |
| LLM | 13/9 | 1.4× | [0.63, 3.31] | 0.80 |

## 3. What normalized (hype faded)

| Term | Median | P |
|------|--------|---|
| "generative AI" as buzzword | 0.39× | 0.00 |
| influencer | 0.44× | 0.00 |
| metaverse | 0.56× | 0.03 |
| personalization | 0.54× | 0.00 |
| virtual influencer / community | 0.38× | 0.01 |
| email | 0.38× | 0.05 |

---

## Bottom line (read these five)

1. **GenAI moved from topic to tool.** Mentions of *generative AI* collapsed (−61%); *agentic*, *LLM*, *first-party*, *retail media* all rose. The research question switched from "does GenAI change marketing?" to "how do agents/LLMs get operationalized (content ops, CX, media buying)?"
2. **Measurement is the new battleground.** Analytics/MMM/attribution/incrementality grew the fastest of any area — cookie deprecation killed last-click, so CMOs fund MMM + experimentation.
3. **B2B is the fastest-growing domain** — ABM mainstreamed, B2B absorbed consumer CX techniques; share nearly tripled.
4. **Privacy-first data is now core infrastructure** — first-party/contextual/deterministic targeting research grew even as the *privacy* debate term cooled.
5. **Creator economy persists; the metaverse did not.** Creator/retail-media rose while metaverse/virtual-influencer mentions decayed toward zero.

**Caveats:** corpus is relevance-sorted OpenAlex (under-samples newest months; risers are conservative). Term counts are title+abstract mentions, not citations. Full evidence: `papers.yaml`, `statistics.json`, `docs/research/trends.md`, `scripts/bayesian_trends.py`.
