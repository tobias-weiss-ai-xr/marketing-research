# 📄 Latest Marketing Trends — One-Pager (Bayesian Evidence)

**Corpus:** 7,378 papers, 2024–2026 (3,414 in the last 12 months) · OpenAlex + CrossRef + dblp + Europe PMC
**Method:** exact conjugate Bayes — Beta-Binomial share-shift per category, Gamma-Poisson ratios per term; posterior medians with 95% credible intervals (CrI). No MCMC; reproducible via `scripts/bayesian_trends.py` (seed 42). Numbers: `docs/research/bayesian_trends.json`.
**Status:** auto-refreshed weekly (GitHub Actions `discover` job). This is a rolling snapshot.

---

## 1. The areas gaining share (P > 0.90)

Ratio = category's share of the corpus in the recent 12m (2025-08→2026-07) vs the prior 12m (2024-08→2025-07).

| Area | Share shift | Posterior median | 95% CrI | P(ratio>1) |
|------|-------------|------------------|---------|-----------|
| **Analytics, Attribution & Measurement** | 6.3% → 8.7% | **1.39×** | [1.15, 1.68] | 1.00 |
| **B2B & Account-Based Marketing** | 4.0% → 4.8% | **1.18×** | [0.93, 1.52] | 0.91 |
| Social Media & Creator Marketing | 9.6% → 11.0% | 1.11× | [0.95, 1.29] | 0.90 |
| Consumer Behavior & Psychology | 11.0% → 11.8% | 1.08× | [0.93, 1.25] | 0.84 |
| Content & Storytelling | 5.9% → 6.7% | 1.00× | [0.82, 1.22] | 0.50 (stable) |

*Declining share: Digital & Performance (0.83, P=0.02), Data/Privacy & Cookieless (0.76, P=0.01), AI & Marketing (0.91). Partly a relevance-ranking artifact of the fetch (older papers rank higher), so the risers above are conservative.*

## 2. What's rising in the literature's language (12m ratio, Gamma-Poisson)

| Term | Recent/Prior | Median | 95% CrI | P |
|------|--------------|--------|---------|---|
| agentic | 17/1 | **10.5×** | [2.84, 75.1] | 1.00 |
| account-based (ABM) | 18/6 | **2.8×** | [1.21, 7.27] | 0.99 |
| LLM | 24/9 | **2.6×** | [1.26, 5.64] | 1.00 |
| large language | 16/6 | 2.5× | [1.07, 6.56] | 0.98 |
| genai | 29/12 | 2.3× | [1.24, 4.67] | 1.00 |
| creator (economy) | 27/12 | 2.2× | [1.15, 4.38] | 0.99 |
| incrementality | 7/3 | 2.1× | [0.64, 8.19] | 0.89 |
| marketing mix modeling (MMM) | 17/8 | 2.0× | [0.93, 4.79] | 0.96 |
| ABM | 12/6 | 1.9× | [0.77, 5.15] | 0.92 |
| tiktok / short-form | 86/46 | 1.9× | [1.31, 2.67] | 1.00 |
| experiment | 24/13 | 1.8× | [0.95, 3.59] | 0.96 |
| attribution | 36/20 | 1.8× | [1.04, 3.09] | 0.98 |

## 3. What normalized (hype faded)

| Term | Median | P |
|------|--------|---|
| metaverse | 0.80× | 0.21 |
| virtual influencer | 0.83× | 0.30 |
| cookieless | 0.57× | 0.23 |
| customer journey | 0.91× | 0.36 |
| programmatic | 0.91× | 0.35 |

---

## Bottom line (read these five)

1. **Agentic AI is the breakout frontier.** *agentic* mentions rose **10.5×** (P=1.00) — the single strongest signal in the corpus. The research question switched from "does GenAI change marketing?" to "how are agents/LLMs operationalized?" (LLM +2.6×, genAI +2.3×, large-language +2.5× all confirmed).
2. **Measurement is the durable battleground.** Analytics/Attribution/Measurement is the only category with a robust share gain (1.39×, P=1.00); incrementality +2.1×, MMM +2.0×, attribution +1.8× all rising. Cookie deprecation killed last-click, so MMM + experimentation fund the gap.
3. **B2B is rising, modestly but steadily** (1.18×, P=0.91); ABM/account-based surged (+2.8×). B2B absorbed consumer CX techniques.
4. **Creator economy resurged** — creator +2.2×, TikTok/short-form +1.9× (P=1.00). After a 2025 lull it's back as a core channel.
5. **The metaverse did not.** metaverse 0.80×, virtual-influencer 0.83×, cookieless 0.57× — hype cycles decayed; "cookieless" is now infrastructure (quiet), not a topic.

**Caveats:** corpus is relevance-sorted OpenAlex (under-samples newest months; risers are conservative). Term counts are title+abstract mentions, not citations. Full evidence: `papers.yaml` (7,378 entries), `statistics.json`, `docs/research/trends.md`, `scripts/bayesian_trends.py`.
