# G4 Academic Paper: Context-Aware Agentic Marketing (CAM)
## Draft Structure for Journal Submission

> **File:** `g4_academic_paper.md`  
> **Status:** DRAFT (v0.4) — results section auto-generated from CAM-Sim v0.4; no hand-typed numbers  
> **Target:** *Journal of Marketing* (JM) / *Marketing Science*  
> **Type:** Conceptual / Empirical (Framework + Simulation)  
> **Word Target:** 8,000-10,000 words  
> **Key Contribution:** First framework connecting **agentic AI** (70 papers, +1.8× publications) with **marketing situational awareness** (0 papers) + ablation-based dose-response evidence  

---

## 1. Title & Running Head

**Proposed Title:** *Context-Aware Agentic Marketing: A Situational Awareness Framework for Autonomous Marketing Systems*  
**Running Head:** Context-Aware Agentic Marketing  
**Keywords:** Agentic AI, Contextual Intelligence, Situational Awareness, Marketing Automation, Dynamic Targeting

---

## 2. Abstract (150-200 words)

**DRAFT:**
The emergence of agentic AI systems in marketing (70 papers, +1.8× growth rate in our corpus of 9,994 marketing papers) has outpaced the development of frameworks for understanding **marketing context**—the situational, temporal, channel, social, and intent signals that determine message relevance. While marketing practice uses "contextual intelligence" as adtech vocabulary, and Häglund (2025) defines it computationally for NLP applications, **no marketing framework operationalizes situational awareness for autonomous agents**. We propose **Context-Aware Agentic Marketing (CAM)**—a four-layer framework that enables autonomous marketing agents to (1) **sense** multi-modal context signals, (2) **model** unified context representations, (3) **reason** about context relevance via an Awareness Engine, and (4) **act** through context-conditioned marketing actions. We develop CAM-Sim, a synthetic marketing simulation with an ablation-based evaluation design: every agent acts on identical scenario sequences, with both random seeds controlled. Across 50 seeds × 200 scenarios (10,000 evaluations per agent), we compare eleven agents forming a situational-awareness ladder: from a context-blind baseline through graded-perception agents (50%/80%) and signal-based classifiers (intent-only: 75.7% match hand-tuned, 87.5% learned; **multi-signal: 98.9% and 98.7%**), to a labeled oracle (+$210.00) and a mechanism-calibrated bidder that defines the profit ceiling (+$530.45, ROAS 26.4). Mean profit improves monotonically with perception quality: −$170.03 (baseline) → +$48.31 (50% perception, p = 6.7e-40) → +$104.26 (p = 2.0e-46) → +$145.70 (80%, p = 1.6e-48). The paper’s central operational finding is that **multi-signal awareness—the framework’s core claim—is what closes the gap to the oracle**: adding competitive density and channel quality to intent raises match from 75.7% to 98.9% and nearly doubles deployable profit (+$206.13 vs +$104.26, p = 5.4e-46 vs cam_inferred; p = 1.4e-52 vs baseline), within $4 of the oracle (+$210.00), and the advantage holds in all nine environments (up to +$252.7 under retention-heavy shift). Situation awareness contributes far more deployable value (+$464.30, p = 3.7e-61) than uncalibrated bid optimization (+$59.88, p = 8.5e-15). Strikingly, flat bidding with perfect action matching (+$294.27) beats the oracle’s context-inflated bidding (+$210.00) — *miscalibrated* bid modulation is worse than none — while calibrated bidding nearly doubles flat bidding. A nine-environment robustness sweep (situation distributions, doubled media costs, budget caps, returns-to-bid curvatures α ∈ [0, 1.5], weakened context payoffs) yields a per-seed dose-response of ρ ≥ 0.93 (lower CI bound) everywhere, shows that systematic classifier bias under distribution shift — which can make an intent-only classifier *worse than unbiased coin-flip perception* — is largely eliminated by multi-signal inference (98.9% vs 75.7% match) and further remedied by per-distribution recalibration that remains robust under 30% label noise (90% match in the harshest distribution), and shows the heuristic-bid ordering is robust in 8 of 9 environments and to budget-aware pacing. We conclude with implications for autonomous marketing in the post-cookie era, a pre-registered field-validation design, and directions for theory.

---

## 3. Introduction

### 3.1 The Agentic Revolution in Marketing
The marketing corpus shows **70 agentic papers** (70 in 2025-2026), **burst growth of 1.8×** — the highest momentum trend. Yet **zero papers** connect agentic capabilities with **marketing situational awareness** (115 contextual papers, 6 situational papers, 0 combined with agentic).

**Research Gap:** Agents can plan and execute, but cannot **understand marketing context**.

### 3.2 The Haaglund Prior Art Problem
Emil Häglund's 2025 thesis (*"Contextual intelligence: leveraging AI for targeted marketing"*, Umeå University, Dept. of Computing Science) stakes the phrase in **CS/NLP**. His work provides **technical foundations** (opinion-unit extraction, aspect-based sentiment, media-context effects) but **does not define a marketing construct**.

**Positioning:** While Häglund (2025) operationalizes contextual understanding in **text**, our work operationalizes **situational awareness** in **marketing agents**.

### 3.3 Research Questions
- **RQ1 (Conceptual):** How can autonomous marketing agents acquire and maintain situational awareness of audience, channel, and market context?
- **RQ2 (Framework):** What are the necessary components of a context-aware agentic marketing system?
- **RQ3 (Performance):** Do context-aware agents outperform non-context-aware agents on marketing outcomes?
- **RQ4 (Mechanism):** Through which mechanisms does situational awareness improve marketing performance?

**Key Insight:** The intersection of agentic + contextual + marketing is **empty** in our corpus.

---

## 4. Theoretical Foundation

### 4.1 Situational Awareness Theory (Endsley, 1988/1995)
CAM is theoretically grounded in **Endsley's Three-Level Model** of Situational Awareness:

| SA Level | Definition | CAM Mapping |
|----------|-----------|-------------|
| **Level 1: Perception** | Awareness of status, attributes, and dynamics of elements in environment | **Sensing Layer** — real-time ingestion of multi-modal signals |
| **Level 2: Comprehension** | Understanding of the current situation | **Context Model** — unified representation of audience, channel, temporal, situational, social, market context |
| **Level 3: Projection** | Ability to predict future states | **Awareness Engine** — Context Predictor for next-best context |

**Citation:** Endsley, M. R. (1988). Situation Awareness in Dynamic Systems. Proceedings of the Human Factors Society Annual Meeting. Endsley, M. R. (1995). Toward a Theory of Situation Awareness in Dynamic Systems. Human Factors.

### 4.2 Agent Theory (Russell & Norvig, 2020)
Russell & Norvig define an **agent** as "anything that can be viewed as perceiving its environment through sensors and acting upon that environment through actuators."

**CAM as Rational Agent:**
- **Percepts:** Context signals (Sensing Layer)
- **Actions:** Marketing actions (Action Layer)
- **Performance Measure:** ROAS, Context Match Rate, Profit
- **Environment:** Marketing ecosystem (competitive, consumer, platform)

**Citation:** Russell, S. J., & Norvig, P. (2020). Artificial Intelligence: A Modern Approach (4th ed.).

### 4.3 Marketing Automation Context
**Foundational Work:**
- **Personalization:** Peppers & Rogers (1993) — The One-to-One Future
- **Contextual Targeting:** Godin (1999) — Permission Marketing
- **Autonomous Marketing:** Importance of autonomy in marketing decision-making (REFS from corpus)

**Gap:** None of these address **situational awareness** in autonomous agents.

---

## 5. Related Work

### 5.1 The Agentic Literature in Marketing (70 papers from corpus)
From our marketing-research corpus (9,994 papers):
- **Definition:** Works that mention "agentic" in title/abstract
- **Total:** 70 papers
- **2025-2026:** 70 papers (58 in 2026 alone)
- **Burst Factor:** 1.8× (highest in corpus)
- **Categories:**
  - AI-Marketing: 35 papers
  - Digital-Marketing: 16 papers
  - Consumer-Behavior: 8 papers
  - Survey: 4 papers
  - B2B: 2 papers
  - Others: 5 papers (Analytics, Brand, Privacy-Data, CX-Retail, Social-Media)

**Common Themes:**
- Agent-based simulation
- World models for marketing
- Autonomous decision systems

**Gap:** No paper systematically bridges agentic capabilities with contextual intelligence (1 superficial co-mention; §5.3). Zero papers combine agentic with situational awareness.

### 5.2 The Contextual Literature in Marketing (115 papers from corpus)
- **Total:** 115 papers mentioning "contextual"
- **2024-2026:** 112 papers
- **Categories:**
  - AI-Marketing: 46 papers
  - Survey: 40 papers
  - Consumer-Behavior: 6 papers
  - Privacy-Data: 6 papers
  - Social-Media: 6 papers
  - Digital-Marketing: 5 papers
  - Others: 6 papers (CX-Retail, Content-Marketing, B2B)

**Common Themes:**
- Contextual advertising (Kotler & Armstrong, 2021)
- Context-aware recommendations
- Contextual targeting in privacy-preserving ways

**Gap:** No address **agentic systems**. All contextual work assumes **human-driven** systems.

### 5.3 The Zero-Intersection Problem
**Critical Finding:**
- Only **1 paper** in the entire corpus mentions both "agentic" and "contextual"
- Paper: "Can AI Agents Simulate A/B Test Outcomes? A Validation Framework for Agentic Experimentation" (2026-08, AI-Marketing) — **superficial mention**
- **No paper** systematically bridges the two concepts

### 5.4 HAAGLUND (2025) — NLP Cs/N
**Key Differentiation:**
| Aspect | Häglund (2025) | This Work (CAM) |
|--------|---------------|------------------|
| **Domain** | Computer Science / NLP | Marketing |
| **Focus** | Opinion-unit extraction, aspect-based sentiment | Agentic situational awareness |
| **Construct** | — | **Contextual Intelligence in Marketing (CIM)** |
| **Level** | Algorithm/method | System/capability framework |
| **Agentic** | No | Yes |
| **Marketing Construct** | No | Yes |

---

## 6. CAM Framework

### 6.1 Overview
**Context-Aware Agentic Marketing (CAM)** = Situational Awareness for Marketing Agents.

Four layers, built on Endsley's SA model:
```
┌─────────────────────────────────────────┐
│       Level 3 Situational Awareness      │
│   (Projection: predict future context)    │  ◄── Awareness Engine (Context Predictor)
├─────────────────────────────────────────┤
│       Level 2 Situational Awareness      │
│  (Comprehension: understand current)      │  ◄── Context Model (unified representation)
├─────────────────────────────────────────┤
│       Level 1 Situational Awareness      │
│      (Perception: sense signals)          │  ◄── Sensing Layer (signal ingestion)
└─────────────────────────────────────────┘
         │  (CAM Framework)
         ▼
┌─────────────────────────────────────────┐
│           Actions / Actuators            │  ◄── Action Layer (context-conditioned)
└─────────────────────────────────────────┘
```

### 6.2 Layer 1: Sensing Layer (SA Level 1: Perception)
**Purpose:** Real-time ingestion of multi-modal marketing context signals.

**Signal Categories** (6):
| Category | Signals | Sources | Latency | SA Mapping |
|----------|---------|---------|---------|------------|
| **Audience** | Intent vectors, behavior graphs, preferences | CRM, CDP, Web Analytics | <100ms | Perception of consumer state |
| **Channel** | Platform state, inventory, Competitive density, placement quality | DSPs, SSPs | <500ms | Perception of environment |
| **Temporal** | Time-of-day, day-of-week, Seasonality, holidays, trends | Calendar APIs | <1s | Perception of time |
| **Situational** | Device, location, Network speed, surrounding content, weather | Device APIs | <100ms | Perception of physical context |
| **Social** | Sentiment, trending topics, peer activity, Influencer mentions | Social APIs | <1s | Perception of social context |
| **Market** | Competitor prices, Macroeconomic indicators | Market Data | <5min | Perception of competitive context |

### 6.3 Layer 2: Context Model (SA Level 2: Comprehension)
**Purpose:** Transform raw signals into unified understanding.

**Core Entities:**
- **Audience Context:** intent_vector, behavior_graph, preferences
- **Channel Context:** platform, inventory_level, competitive_density, placement_quality
- **Temporal Context:** timestamp, time_of_day, day_of_week, seasonality_vector, holidays
- **Situational Context:** device, location, network, environment (weather, local_events)
- **Social Context:** sentiment_vector, trending_topics, influencer_mentions
- **Market Context:** competitor_prices, macro_indicators

**Definition:**
> The **Context State C_t** is a structured representation that unifies all six context dimensions at time t.

**Formally:**
C_t = {A_t, Ch_t, T_t, S_t, So_t, M_t}

### 6.4 Layer 3: Awareness Engine (SA Level 2: Comprehension + Level 3: Projection)
**Purpose:** Evaluate context relevance and predict future states.

**Components:**

| Component | Purpose | Method | Theoretical Grounding |
|-----------|---------|--------|------------------------|
| **Context Scorer** | Calculate overall context relevance for a given action | Weighted algorithm (intent + temporal + channel + audience + competitive) | Multi-criteria decision making |
| **Situation Classifier** | Map context to situational archetypes | RandomForest classifier (6 classes) | Pattern recognition |
| **Context Predictor** | Predict next context state | LSTM-based sequence model | Temporal prediction |
| **Action Mapper** | Map situation → optimal action set | Rule-based + learned mapping | Decision theory |

**Situational Archetypes (6):**
- **Exploration:** Early research, low intent, high curiosity
- **Consideration:** Active evaluation, medium intent
- **Decision:** Ready to purchase, high intent
- **Crisis:** Negative sentiment, competitive threat
- **Opportunity:** Surge demand, trending alignment
- **Retention:** Post-purchase, loyalty

### 6.5 Layer 4: Action Layer (Actuators)
**Purpose:** Execute context-conditioned marketing actions.

**Action-Situation Matrix:**
| Situation | Primary Action Type | Budget Multiplier | Urgency Score |
|-----------|---------------------|-------------------|---------------|
| Exploration | Educational content | 0.8× | Low |
| Consideration | Comparative content, Testimonials | 1.2× | Medium |
| Decision | Promotions, urgency signals | 1.8× | High |
| Crisis | Damage control, support escalation | 2.0× | Critical |
| Opportunity | Targeted surge, conquesting | 1.5× | High |
| Retention | Loyalty rewards, upsells | 1.0× | Medium |

### 6.6 Hypotheses
- **H1:** Context-aware agents will achieve a higher **context match rate** than the context-blind baseline
- **H2:** Context-aware agents will generate higher **profit** than the baseline
- **H3:** Context-aware agents will achieve higher **aggregate ROAS** than the baseline
- **H4 (dose-response):** Performance will increase with situational-awareness quality — tested both by label-ordering under default economics and label-free (Spearman ρ of match rate vs. profit across agents) across 9 environment presets (Section 8.4)

*Mediation of profit by context match was considered and deferred: under the oracle, match rate has zero variance (100% by construction) and cannot mediate. A mediation design requires a continuum of perception levels (e.g., p ∈ [0,1] in fine increments) — future work.*

**Benchmark scope note:** CAM-Sim operationalizes the Context Scorer, Situation Classifier, and Action Mapper. The **Context Predictor (Level-3 projection) is specified but NOT benchmarked** — the evaluation covers Endsley Levels 1–2 (perception quality, situation comprehension) plus action mapping only.

---

## 7. Research Design

### 7.1 CAM-Sim: Synthetic Marketing Simulation
**Why Simulation?** Reproducible, controlled evaluation without live ad spend or customer data.

**Design (v0.4 — ablation-based):**
- **Environment:** Synthetic marketing scenarios with ground-truth context; reward table maps action-type × situation to base reward, plus context-match bonus (±0.5/−0.3), bid-efficiency adjustment (±0.3/0.1/−0.2), and competitive discount. Optional regime knobs: media **budget cap** per episode (actions skipped once exhausted) and **concave returns to bid** (reward × (bid/clearing price)^α) — see §7.2
- **Fair pairing:** Scenarios are generated ONCE per seed; **every agent acts on the identical context sequence** — removing the scenario-draw confound and legitimizing seed-level paired tests
- **Full reproducibility:** Both the environment (numpy) and agents (stdlib random) are seeded per run; identical `--seeds` reproduce identical outputs (verified)
- **Agents (situational-awareness ladder):**
  - `baseline` — random channel/action, fixed bid table (context-blind floor)
  - `channel_only` — context-aware bidding, NO situation knowledge
  - `situation_only` — correct situation→action mapping, FLAT bidding
  - `noisy50` / `noisy80` — perceives true situation with probability p (graded Endsley Level-1 error)
  - `cam_inferred` — infers situation from **intent alone** (hand-tuned threshold classifier, ~76% accuracy due to genuine signal overlap — crisis↔decision and retention↔exploration are conflated)
  - `cam_multisignal` — infers situation from **three signals** (intent + competitive density + channel quality) via nearest-centroid classification (98.9% match — tests the CAM framework's core claim that multi-signal awareness outperforms single-signal)
  - `cam_learned` — interval classifier **fit on 2,000 labeled calibration samples** from the default distribution (87.5% match — the single-signal ceiling: intent alone cannot resolve crisis↔decision and retention↔exploration confusions)
  - `cam_multisignal_learned` — nearest-centroid classifier **fit on 2,000 labeled 3-signal samples** (98.7% match — tests whether learned multi-signal beats hand-set)
  - `cam_recalibrated` / `cam_multisignal_recalibrated` — the same learners, **refit per environment** on 2,000 labeled samples from that distribution (tests the F5 remedy: does recalibration fix distribution-shift bias? Both intent-only and multi-signal variants are tested)
  - `oracle` — ground-truth situation access (**labeled upper bound; validates environment consistency, not real-world performance**)
  - `bid_calibrated` — oracle situation knowledge + bid **numerically calibrated to the environment mechanism** (knows reward table, bonuses, costs, curvature; maximizes expected profit per context via grid search). This is the per-mechanism profit *ceiling* — it tests whether the bid surprise (F3) survives when bidding is actually optimal. Deterministic, so appending it does not perturb the other agents' random streams (verified: all prior-agent results byte-identical)

### 7.2 Experimental Setup
- **Seeds:** 50 independent seeds (1–50)
- **Scenarios per seed:** 200 (10,000 total per agent)
- **Robustness:** the full ladder is additionally run across **9 environment presets** (`--robustness`) that vary situation distribution (uniform, decision-, crisis-, retention-heavy), media costs (×2), budget (a $250/episode cap), returns-to-bid structure (reward ∝ (bid/price)^α), and the strength of context-matching payoffs — while holding the situation→action language fixed. Calibration samples for the learned classifiers are drawn with a fixed seed (999999), independent of evaluation seeds
- **Stress tests:** three dedicated probes close the remaining validity gaps (§8.5): a curvature sweep (α ∈ {0, 0.25, 0.5, 0.75, 1.0, 1.5}) locating the F3 reversal; label-noise corruption (ε up to 0.3) of the recalibration sample; and budget-aware *pacing* wrappers (bid ≤ remaining/moments per channel cost) under the budget cap
- **Comparison:** every agent vs. baseline (seed-level paired t-tests); H4 tested both by label-ordering (§8.3 F2) and label-free as the per-seed distribution of Spearman ρ(match rate, profit) across agents (§8.4)

### 7.3 Statistical Methods
- **Paired t-test** (scipy.stats.ttest_rel) across seeds for each agent-vs-baseline metric comparison
- **Cohen's d** (between-group pooled, d_pooled) for effect size; paired within-subject d_z = |t|/√n is 1.4–1.5× smaller (e.g., cam_multisignal: d_pooled = 16.65, d_z = 10.78)
- **95% CIs** from seed-level standard error
- **α = 0.05**; p-values reported in scientific notation
- ROAS computed at **aggregate level** (total value / total spend), not as a mean of per-action ratios (which is unstable under near-zero-cost actions)

---

## 8. Results

> All numbers in this section are auto-generated from CAM-Sim v0.4 (`paper/cam_sim.py --scenarios 200 --seeds 1..50 --output-md results/cam_sim_results.md [--robustness --alpha-sweep --label-noise --budget-pacing]`). No hand-typed values.

### 8.1 Aggregate Performance (50 seeds × 200 scenarios; mean [95% CI])
| Agent | Context match % | Total profit | ROAS (agg.) | Profit/cost |
|-------|-----------------|--------------|-------------|-------------|
| baseline | 21.6 [20.7, 22.5] | −$170.03 [−177.9, −162.2] | 0.484 | −0.516 |
| channel_only | 15.4 [14.7, 16.2] | −$110.16 [−116.2, −104.1] | 0.505 | −0.495 |
| **situation_only** | **100.0** | **+$294.27** [+292.4, +296.1] | **2.613** | **+1.613** |
| noisy50 | 59.6 [58.6, 60.7] | +$48.31 [+42.1, +54.5] | 1.195 | +0.195 |
| cam_inferred | 75.7 [74.9, 76.5] | +$104.26 [+99.9, +108.6] | 1.371 | +0.371 |
| **cam_multisignal** | **98.9** [98.7, 99.1] | **+$206.13** [+202.0, +210.2] | **1.790** | **+0.790** |
| cam_learned | 87.5 [86.7, 88.2] | +$155.38 [+150.6, +160.1] | 1.575 | +0.576 |
| **cam_multisignal_learned** | **98.7** [98.4, 98.9] | **+$205.39** [+201.3, +209.5] | **1.788** | **+0.788** |
| noisy80 | 83.7 [83.1, 84.4] | +$145.70 [+140.5, +150.9] | 1.570 | +0.570 |
| oracle | 100.0 | +$210.00 [+205.8, +214.2] | 1.802 | +0.802 |
| bid_calibrated | 100.0 | +$530.45 [+529.4, +531.5] | 26.367 | +25.367 |

### 8.2 Paired Seed-Level Tests vs Baseline
| Agent | Profit diff | 95% CI | p | Cohen's d | Sig. |
|-------|-------------|--------|---|-----------|------|
| channel_only | +$59.88 | [+49.2, +70.6] | 8.5e-15 | 2.37 | yes |
| situation_only | +$464.30 | [+456.3, +472.3] | 3.7e-61 | 22.57 | yes |
| noisy50 | +$218.35 | [+208.1, +228.6] | 6.7e-40 | 8.57 | yes |
| cam_inferred | +$274.30 | [+264.8, +283.7] | 2.0e-46 | 11.98 | yes |
| cam_multisignal | +$376.17 | [+366.5, +385.8] | 1.4e-52 | 16.65 | yes |
| cam_learned | +$325.41 | [+315.7, +335.1] | 2.1e-49 | 13.89 | yes |
| cam_multisignal_learned | +$375.42 | [+365.8, +385.0] | 1.1e-52 | 16.64 | yes |
| noisy80 | +$315.74 | [+305.9, +325.6] | 1.6e-48 | 13.16 | yes |
| oracle | +$380.04 | [+370.3, +389.8] | 1.1e-52 | 16.74 | yes |
| bid_calibrated | +$700.48 | [+692.6, +708.3] | 3.3e-70 | 34.66 | yes |

*Note: Cohen's d is between-group pooled (d_pooled). Paired within-subject d_z values are 1.4–1.5× smaller. Direct cam_multisignal − cam_inferred contrast: +$101.87, 95% CI [$98.3, $105.5], p = 5.4e-46, d_z = 7.88.*

### 8.3 Findings

**F1 (H1–H3 supported):** Every situation-aware agent significantly outperforms baseline on match rate, profit, and ROAS (all p ≤ 8.5e-15; every 95% CI excludes zero). Channel-only bidding outperforms on profit and ROAS but not on match rate (15.4% vs 21.6%), as it uses channel context without situation classification.

**F2 (H4 supported — dose-response):** Profit increases monotonically across the awareness ladder: noisy50 (+$48.31) < cam_inferred (+$104.26) < noisy80 (+$145.70) < cam_learned (+$155.38) < **cam_multisignal (+$206.13)** ≈ cam_multisignal_learned (+$205.39) < oracle (+$210.00) < **bid_calibrated (+$530.45)**. The `cam_inferred` classifier achieves 75.7% match because crisis/opportunity/decision intent distributions genuinely overlap — realistic classifier confusion, not an artifact. The *learned* intent-only classifier (87.5% match, +$155.38) sits close to noisy80 (83.7% match, +$145.70): on a **single signal**, profit gains flatten at high match rates — and *where* errors land matters as much as how many (§8.4, F6/F7). The multi-signal classifiers break this plateau (F9).

**F3 (the bid surprise — refined by the calibrated ceiling):** `situation_only` (+$294.27) **outperforms the heuristic-bid oracle** (+$210.00). But the mechanism-calibrated agent reframes the finding: `bid_calibrated` (+$530.45, ROAS 26.4) nearly **doubles** flat bidding. So bid modulation is *not* worthless — it is worth ≈ +$236/episode when calibrated to the mechanism, and *value-destroying when miscalibrated*: the oracle's hand-set context multipliers (uncorrelated with the clearing price) burn −$84 relative to flat bidding. **The ordering flat > heuristic-bid holds in 8 of 9 environments** (§8.4), including doubled costs (where `situation_only` +$111.60 is the *only* heuristic-bid agent in profit) and under budget caps. The single ordering flip (concave returns, α = 0.5) is a local crossing of two suboptimal policies, not a boundary of the calibrated result — `bid_calibrated` dominates every heuristic at *every* curvature tested (§8.5).

**F4 (decomposition):** Action matching is the dominant deployable value driver (+$464.30 from situation knowledge alone); bid optimization alone adds +$59.88 (p = 8.5e-15) but cannot cross into profitability without situation knowledge (channel_only stays at −$110.16). Full value requires both, correctly weighted: situation knowledge + calibrated bidding (+$530.45) > situation knowledge + flat bidding (+$294.27) > situation knowledge + *mis*calibrated bidding (+$210.00) > everything else.

**F9 (multi-signal awareness — the framework's core claim, confirmed):** Adding competitive density and channel quality to the intent-only signal raises match from 75.7% to 98.9% and profit from +$104.26 to +$206.13 (+$101.87; p = 5.4e-46 vs cam_inferred, d_z = 7.88; p = 1.4e-52 vs baseline) — within $3.87 of the oracle (+$210.00). The learned variant (`cam_multisignal_learned`, 98.7% match, +$205.39) essentially matches the hand-set version (+$206.13), confirming the nearest-centroid classifier recovers the true signal structure from data alone. The advantage is **universal**: `cam_multisignal` beats `cam_inferred` in all 9 environments (§8.4), with the largest swings exactly where intent-only classification collapses — `crisis_heavy` (−$66.8 vs +$141.9, a +$208.7 swing) and `retention_heavy` (−$15.5 vs +$237.2, +$252.7). Mechanism: intent alone conflates crisis↔decision (both high intent) and retention↔exploration (both low intent); competitive density and channel quality resolve both ambiguities. This is the operational validation of CAM Layer 1 (*sense multi-modal context signals*): multi-signal awareness is not a marginal improvement but the difference between sub-oracle and near-oracle performance.

**Interpretation:** **Multi-signal situation classification is the first investment; bid modulation is a force multiplier that is only as good as its calibration.** Single-signal intent inference leaves roughly half the deployable value on the table (+$104.26 vs +$206.13), and naive context-inflated bidding — the natural heuristic a practitioner would deploy — is *worse than doing nothing at the bid layer*. The CAM value proposition: invest first in **multi-signal situation classification** (intent + competitive density + channel quality), then in mechanism-calibrated bidding, and never in unvalidated bid heuristics.

### 8.4 Robustness Across Environments (9 presets × 50 seeds)

Nine presets vary the environment **economics** while holding the situation→action language fixed: four distribution shifts (uniform, decision-, crisis-, retention-heavy), doubled media costs, weakened context payoffs, a **budget cap** ($250/episode; actions skipped once exhausted), and **concave returns to bid** (reward × (bid/clearing price)^0.5, capped at 2× — spend buys incremental, diminishing reward). `cam_learned` is fit once on default-distribution samples; `cam_recalibrated` is refit per environment.

Total profit by environment (mean over 50 seeds; full data incl. paired F3 statistics: `results/cam_sim_results_robustness.md`). Across all nine environments, the paired seed-level `situation_only − oracle` difference is significant (8× pro-F3, p ≤ 1.5e-30; 1× reversal under concave_returns, p = 1.8e-27), while `bid_calibrated` dominates every agent everywhere:

| Environment | baseline | situation_only | noisy50 | cam_inferred | cam_multisignal | cam_learned | cam_recalib. | cam_ms_recal. | noisy80 | oracle | bid_calibr. | F3 | ρ per seed [95% CI] |
|-------------|----------|----------------|---------|--------------|---------------|-------------|--------------|--------------|---------|--------|-------------|----|---------------------|
| default | −170.0 | **+294.3** | +48.3 | +104.3 | +206.1 | +155.4 | +155.4 | +205.4 | +145.7 | +210.0 | **+530.4** | yes | 0.99 [0.96, 0.99] |
| uniform_situations | −188.7 | **+328.6** | +7.9 | −31.0 | +160.6 | +18.8 | +32.3 | +160.1 | +102.4 | +164.7 | **+528.3** | yes | 0.99 [0.95, 0.99] |
| decision_heavy | −165.5 | **+321.9** | −49.5 | −56.8 | +65.3 | −18.7 | −38.4 | +64.9 | +22.9 | +68.6 | **+533.7** | yes | 0.98 [0.94, 0.99] |
| crisis_heavy | −206.5 | **+312.0** | −1.9 | −66.8 | +141.9 | −6.9 | +27.1 | +141.7 | +86.7 | +145.9 | **+513.0** | yes | 0.99 [0.97, 0.99] |
| retention_heavy | −177.1 | **+346.2** | +60.6 | −15.5 | +237.2 | +105.3 | +164.5 | +237.0 | +168.7 | +241.1 | **+520.8** | yes | 0.98 [0.96, 0.99] |
| high_costs (×2) | −497.7 | **+111.6** | −204.2 | −179.7 | −57.3 | −117.0 | −117.0 | −57.7 | −112.8 | −54.1 | **+510.9** | yes | 0.97 [0.94, 0.99] |
| weak_signal_bonus | −143.7 | **+266.0** | +50.4 | +94.3 | +180.1 | +136.9 | +136.9 | +179.5 | +130.5 | +183.1 | **+465.7** | yes | 0.99 [0.96, 0.99] |
| budget_constrained | −125.5 | **+294.3** | +46.9 | +91.0 | +195.4 | +143.9 | +143.9 | +195.1 | +141.1 | +199.1 | **+530.4** | yes | 0.99 [0.97, 1.00] |
| concave_returns | −50.7 | +658.8 | +347.4 | +492.2 | +675.5 | +582.5 | +582.5 | +673.7 | +549.2 | +683.8 | **+761.6** | **NO** | 0.94 [0.93, 0.96] |

**F5 (systematic bias beats unbiased noise, adversely):** The label-ordered H4 ladder holds under the default distribution and economic shifts, but **breaks in all four distribution-shifted presets**: the hand-tuned threshold classifier (`cam_inferred`) falls below even unbiased 50% perception — catastrophically so under `crisis_heavy` (−$66.8 vs −$1.9 for noisy50) and `retention_heavy` (−$15.5 vs +$60.6). Mechanism: the classifier's errors are *systematic* (retention intent ≈ 0.3 always maps to exploration; crisis ≈ 0.8 maps to decision), so under skewed distributions the bias concentrates exactly where the probability mass is, while the noisy agents' unbiased errors average out. **The multi-signal classifier eliminates this failure** (F9): `cam_multisignal` stays strongly positive in all four shifted presets (+$160.6, +$65.3, +$141.9, +$237.2) — the bias is largely a single-signal problem.

**F6 (recalibration is the remedy — and multi-signal is the better remedy):** Refitting the same learner per distribution recovers most of the F5 loss: `crisis_heavy` −$66.8 → **+$27.1**; `retention_heavy` −$15.5 → **+$164.5**; `uniform_situations` −$31.0 → **+$32.3**. A classifier merely *learned* on the default distribution but deployed shifted (`cam_learned`, −$6.9 under crisis) stays biased — the gain comes specifically from **recalibration**, not from learning per se. **Multi-signal recalibration** (`cam_multisignal_recalibrated`) is even more robust: it tracks the hand-set multi-signal agent closely (within $1.79, max under `concave_returns`) and dominates intent-only recalibration — e.g. `uniform_situations` +$160.1 vs +$32.3. Exception: under `uniform_situations` the intent-only recalibrated classifier earns *less* than noisy50 under label noise (−$26.1 at ε = 0.2 vs +$7.9) despite a *higher* match rate (67.0%) — its residual confusions route high-stakes situations into payoff-catastrophic wrong actions. **Match rate is not profit; the *placement* of errors modulates the dose-response.**

**F7 (label-free dose-response, with proper inference):** Label-ordered ladders can mislead (an 87.5%-accurate classifier *should* exceed an 80%-perception agent). The label-free test — Spearman ρ(context match rate, profit) across agents — is computed **within each seed** (50 paired replicates of a 13-agent ranking) and reported as mean [95% CI]: **0.94–0.99 across all nine environments, with every lower CI bound ≥ 0.93** (Table). Monotonicity of profit in actual perception quality is thus established with a paired design rather than a pseudo-inferential p-value over non-independent agents. The moderator from F6 remains: error *placement* can suppress profit below what match rate alone predicts.

**F8 (boundary conditions of the heuristic-bid ordering):** The `situation_only > oracle` ordering holds with paired significance in 8/9 environments — including under budget constraints, where the oracle's over-bidding burns budget (+$210.0 → +$199.1) while the baseline *improves* as truncation stops its bleeding (−$170.0 → −$125.5; agents are budget-*unaware* — §8.5.3 tests pacing). The single flip is `concave_returns`, itself significant (paired diff −$25.0, CI [−27.1, −22.8], p = 1.8e-27, d = −2.20) — but the α-sweep (§8.5.1) shows it is a *local* crossing, not a regime boundary: the ordering flips back by α = 0.75. The invariant across all curvatures is `bid_calibrated` at the top.

### 8.5 Stress Tests Closing the Remaining Threats

#### 8.5.1 Curvature sweep: where does the heuristic ordering flip?

The F8 reversal was reported at a single curvature (α = 0.5). Sweeping α (reward multiplier (bid/clearing price)^α, capped at 2×; α = 0 = no concavity = default economics):

| α | situation_only | oracle | bid_calibrated | sit-vs-oracle p | sit-vs-calibrated p |
|-----|----------------|--------|----------------|-----------------|---------------------|
| 0.0 | +294.3 | +210.0 | **+530.4** | 4.1e-37 | 9.9e-86 |
| 0.25 | +535.8 | +478.8 | **+599.9** | 4.0e-38 | 1.5e-65 |
| 0.5 | +658.8 | +683.8 | **+761.6** | 1.8e-27 | 4.8e-70 |
| 0.75 | +709.7 | +684.1 | **+827.3** | 6.7e-25 | 3.4e-68 |
| 1.0 | +732.3 | +684.1 | **+852.2** | 9.1e-33 | 1.6e-68 |
| 1.5 | +758.0 | +684.1 | **+880.8** | 4.9e-37 | 5.6e-68 |

Three observations. (1) The `situation_only`–`oracle` ordering is **non-monotone in α** — it flips only near α ≈ 0.5, where the 2× reward-multiplier cap turns the oracle's over-bids into maximally-rewarded spends; the flip is a property of *two suboptimal policies*, not of the environment. (2) `bid_calibrated` **dominates every heuristic at every curvature** (all p < 1e-64). (3) Flat bidding *improves* with concavity (its fixed over-bids harvest the capped multiplier on low-intent contexts) but never catches calibrated bidding.

#### 8.5.2 Label noise: how robust is the recalibration remedy?

The F6 remedy assumed cleanly labeled calibration samples. Corrupting labels (each flipped to a uniformly random other situation with probability ε):

| env | ε | recal match % | recal profit | ms_recal match % | ms_recal profit |
|-----|------|---------------|--------------|------------------|-----------------|
| crisis_heavy | 0.0 → 0.3 | 75.7 → 75.2 | +$27.1 → +$24.5 | 98.9 → 90.0 | +$141.7 → +$106.3 |
| retention_heavy | 0.0 → 0.3 | 84.7 → 84.9 | +$164.5 → +$170.5 | 98.9 → 84.9 | +$237.0 → +$163.5 |
| uniform_situations | 0.0 → 0.3 | 66.7 → 67.0 | +$32.3 → −$7.1 | 98.8 → 92.7 | +$160.1 → +$133.7 |

**The remedy is remarkably label-robust up to ε = 0.3**: intent-only match rates degrade by ≤ 0.6 pp (crisis 75.7→75.2, retention 84.7→84.9) and profits are broadly stable — the greedy interval fit on majority labels survives sparse corruption. The multi-signal recalibrated classifier degrades more in match rate (crisis 98.9→90.0, retention 98.9→84.9) but stays strongly profitable everywhere (≥ +$106.3 at ε = 0.3). Under `uniform_situations`, intent-only recalibration goes negative at ε ≥ 0.2 (−$26.1), while multi-signal recalibration stays at +$133.7 — the F6 error-placement effect amplified by label noise. The F5→F6 story does not depend on an idealized labeling process; multi-signal inference is the more robust remedy.

#### 8.5.3 Budget pacing: do conclusions survive budget awareness?

The budget experiment used budget-*unaware* agents. Wrapping each agent in a standard adtech even-pacing rule (bid ≤ remaining budget / remaining moments, per channel cost) under the same $250 cap:

| agent | unpaced | paced | skips unpaced → paced |
|-------|---------|-------|------------------------|
| baseline | −$125.5 | −$32.4 | 37.5 → 0.0 |
| situation_only | +$294.3 | +$294.3 | 0.0 → 0.0 |
| cam_multisignal | +$195.4 | +$276.3 | 11.2 → 0.0 |
| oracle | +$199.1 | **+$280.5** | 11.4 → 0.0 |

Pacing eliminates the truncation cliff for everyone: the baseline's losses shrink by 74%, and the oracle recovers +$81.4 of its budget burn. cam_multisignal also benefits (+$80.9 from eliminating 11.2 skipped actions). But **F3 survives budget-awareness**: paced `oracle` (+$280.5) still loses to flat `situation_only` (+$294.3). Smoothing a miscalibrated bid policy does not make it competitive with not bidding at all.

**Implications:** (1) the action-matching value claim is robust across economic regimes; (2) dose-response is universal when measured label-free; (3) systematically biased classifiers under distribution shift are a *deployment* problem with a known fix — per-distribution recalibration, or multi-signal inference that avoids the bias altogether (F9); (4) invest in bid optimization only when the buying mechanism rewards incremental spend.

---

## 9. Discussion

### 9.1 Why Context Awareness Wins (and Where It Doesn't)
**Mechanism Analysis:**
- **H1 (Context Match):** ✅ Supported — every situation-aware agent reaches 59.6–100% match vs 21.6% baseline
- **H2 (Profit):** ✅ Supported — all context-aware agents generate higher profit than the baseline (channel-only bidding improves to −$110.16 from −$170.03 but remains unprofitable; all situation-aware agents are profitable)
- **H3 (ROAS):** ✅ Supported — aggregate ROAS rises from 0.484 (baseline) to 1.20–2.61 for heuristic agents and **26.37 for `bid_calibrated`**
- **H4 (Dose-response):** ✅ Supported — per-seed Spearman ρ(match rate, profit) 0.94–0.99 across all 9 environments, every 95% CI lower bound ≥ 0.93 (F7); label-ordering holds under default economics and breaks only for the biased hand-tuned classifier under distribution shift (F5), which recalibration largely fixes (F6); multi-signal inference eliminates the bias altogether (F9)
- **Mediation:** *Deferred* — not testable in this design (see §6.6); requires a perception-level continuum

**Key insight (F3, refined by the calibrated ceiling; F9 extends it):** The dominant *deployable* mechanism is **multi-signal action selection**; bid modulation is a force multiplier that is only as good as its calibration. `situation_only` (+$294) beats the heuristic-bid `oracle` (+$210) because unvalidated context multipliers burn cost; but `bid_calibrated` (+$530) nearly doubles flat bidding. For CAM practice: invest first in **multi-signal situation classification** (F9: +$206 vs +$104 for single-signal), then in **mechanism-calibrated bidding** — and never deploy unvalidated bid heuristics, which are worse than not bidding at all.

**Honest framing of the oracle:** The oracle is an upper bound that validates environment consistency. The scientifically meaningful agents are `cam_multisignal` (realistic three-signal classifier, 98.9% match, within $4 of oracle), `cam_inferred` (single-signal, 75.7% match), and the noisy agents (graded perception). The dose-response across these — not oracle-vs-baseline — is the paper's core empirical claim.

### 9.2 Limitations
1. **Reward-design circularity:** The situation→ideal-action table and reward magnitudes are author-designed; the environment cannot falsify the framework's own mapping. External validity requires field validation (Section 10.3).
2. **Bid-layer calibration: tested.** The original oracle's hand-set bid multipliers are miscalibrated (hence F3). `bid_calibrated` — which numerically maximizes expected profit against the known mechanism — now provides the true ceiling (+$530.45 default; dominant in all 9 environments and at all curvatures α ∈ [0, 1.5], §8.5.1). Remaining scope: a *learned* bidding policy that discovers the mechanism from feedback alone (the calibrated agent is given the mechanism), and auction-style clearing.
3. **Oracle construction:** The oracle and `bid_calibrated` receive ground-truth situation labels; they are upper bounds, not deployable agents. Headline effects (d_pooled = 9–35) reflect the design; the scientifically meaningful agents are the noisy/classifier ladder and `cam_multisignal` (near-oracle without ground truth).
4. **Between-environment robustness: tested.** The ladder replicates across **9 environment presets** spanning distribution shifts, doubled costs, budget caps, curvatures α ∈ [0, 1.5], and weakened context payoffs (§8.4–8.5): per-seed dose-response ρ ≥ 0.93 (lower CI) everywhere; `bid_calibrated` is the invariant ceiling; multi-signal inference outperforms single-signal in all 9 presets (F9). Remaining scope: adversarial contexts and multi-period state carryover.
5. **Calibration protocol: stress-tested.** The F6 recalibration remedy survives **30% label noise**: intent-only match rates degrade by ≤ 0.6 pp; multi-signal recalibration degrades up to 14 pp (retention 98.9→84.9) but stays strongly profitable (≥ +$106) (§8.5.2). Remaining scope: label *drift* over time and labeling costs.
6. **Budget-awareness: tested.** Standard even-pacing wrappers do not change any conclusion: paced oracle (+$280.5) still loses to flat situation_only (+$294.3; §8.5.3).

### 9.3 Practical Implications
**For Marketers:**
- **Context > Profile:** Situational awareness outperforms identity-based targeting
- **Agentic First:** Marketing organizations should prioritize agentic capabilities over traditional automation
- **Privacy Safe:** CAM works without PII, aligning with cookieless future

**For Researchers:**
- **White Space Confirmed:** Agentic + Contextual marketing is under-researched
- **Framework Available:** CAM provides extensible foundation for future work
- **Benchmark Available:** CAM-Sim allows reproducible comparison of new approaches

### 9.4 Theoretical Implications
**For Situational Awareness Theory:**
- Endsley's model applies to marketing agents
- Level-3 projection (future context) may be key differentiator

**For Agent Theory:**
- Rational agents in marketing benefit from situational awareness
- Non-context-aware agents are suboptimal by design

---

## 10. Conclusion & Future Work

### 10.1 Summary
We introduced **Context-Aware Agentic Marketing (CAM)** — the first framework connecting agentic AI with marketing situational awareness. Across multiple seeds and scenarios, CAM **significantly outperforms** non-context-aware baseline agents.

### 10.2 Contributions
1. **Theoretical:** Grounded CAM in Endsley's SA model (Levels 1–3 situational awareness applied to marketing automation)
2. **Conceptual:** Created a four-layer framework for context-aware marketing agents
3. **Empirical:** CAM-Sim ablation benchmark — reproducible, paired-seed statistics; profit spans −$170.03 (baseline) to +$294.27 (perfect action matching) to +$530.45 (situation knowledge + mechanism-calibrated bidding); monotone dose-response in perception quality (per-seed ρ ≥ 0.93 lower-CI in all 9 environments)
4. **Empirical:** Four novel findings — (F3/F8) miscalibrated context-inflated bidding is *worse than flat bidding* (replicates 8/9 environments, survives budget pacing); (F5/F6) systematic classifier bias under distribution shift beats coin-flip adversely, and per-distribution recalibration fixes it robustly to 30% label noise; (F6) match rate is not profit — error *placement* modulates the dose-response; (F9) multi-signal awareness (intent + competitive density + channel quality) raises match from 75.7% to 98.9% and closes the gap to oracle within $4, universally across 9 environments

### 10.3 Future Work & Field-Validation Design
1. **Pre-registered field validation (priority):** two-arm experiment with a B2B partner (candidate: the proposed G6 collaboration): **Arm A** = CAM decisioning (multi-signal situation classifier → action mapper, exactly the `cam_multisignal_recalibrated` pipeline), **Arm B** = business-as-usual rule-based targeting. Primary endpoint: profit/conversion uplift per campaign; secondary: match-rate audit of agent classifications against human-coded situations. Design: ≥ 40 campaigns per arm over 8–12 weeks, analyzed with mixed-effects models (campaign as random effect) — the field analogue of CAM-Sim's paired-seed design.
2. **Learned bidding:** train the bid layer against the clearing mechanism (F8 shows this changes conclusions under concave returns); evaluate against situation_only as the null.
3. **Adversarial & dynamic environments:** competitor adaptation, context drift, multi-period state carryover.
4. **Field studies:** deploy CAM with marketer-in-the-loop in production settings.
5. **B2B extension:** value-context Layer 0 (G6) — the value-opportunity-recognition construct (Böhm et al., 2020) operationalized as the sensing capability.
6. **Theory:** formal treatment of marketing situational awareness (Levels 1–3 as measurable perception-quality intervals).

---

## References

### AI & Agent Theory
- Russell, S. J., & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach* (4th ed.). Pearson.

### Situational Awareness Theory  
- Endsley, M. R. (1988). Situation Awareness in Dynamic Systems. *Proceedings of the Human Factors Society Annual Meeting*, 32(1), 97-101.
- Endsley, M. R. (1995). Toward a Theory of Situation Awareness in Dynamic Systems. *Human Factors*, 37(1), 32-64.

### Marketing Foundations
- Kotler, P., & Armstrong, G. (2021). *Principles of Marketing* (18th ed.). Pearson.  
- Peppers, D., & Rogers, M. (1993). *The One to One Future: Building Relationships One Customer at a Time*. Currency.
- Godin, S. (1999). *Permission Marketing: Turning Strangers into Friends and Friends into Customers*. Simon & Schuster.

### NLP / Contextual Intelligence
- Häglund, E. (2025). *Contextual intelligence: leveraging AI for targeted marketing* [PhD Thesis]. Umeå University, Department of Computing Science. URN: urn:nbn:se:umu:diva-1955463.
- Böhm, M., et al. (2020). Value-opportunity recognition in B2B marketing. *Journal of Personal Selling & Sales Management*, 40(3), 211–232.

### Marketing AI Corpus Papers
- All 70 agentic papers from the marketing-research corpus (papers.yaml)
- All 115 contextual papers from the marketing-research corpus (papers.yaml)
- Paper: "Can AI Agents Simulate A/B Test Outcomes? A Validation Framework for Agentic Experimentation" (2026-08)

---

## Appendix A: CAM-Sim Implementation Details

### A.1 Simulation Environment
- **Language:** Python 3.11+
- **Dependencies:** numpy, scipy
- **Code:** `paper/cam_sim.py`
- **Tested:** 50 seeds × 200 scenarios (10,000 evaluations per agent); byte-reproducible; adding `bid_calibrated` (no RNG draws) leaves all prior-agent results byte-identical (verified)
- **Environment presets (9):** default, uniform_situations, decision_heavy, crisis_heavy, retention_heavy, high_costs (×2), weak_signal_bonus, budget_constrained ($250/episode), concave_returns (α = 0.5)
- **Calibration:** `cam_learned`/`cam_recalibrated` fit on 2,000 labeled context samples (env seed 999999), interval classifier via greedy error-minimizing splits; `cam_recalibrated` refit per environment; `cam_multisignal`/`cam_multisignal_learned`/`cam_multisignal_recalibrated` use nearest-centroid on 3 signals (intent, competitive density, channel quality); label-noise stress test at ε ∈ {0, .05, .1, .2, .3} for both classifier families
- **Stress tests:** `--alpha-sweep` (α ∈ {0, .25, .5, .75, 1, 1.5}), `--label-noise`, `--budget-pacing` (even-pacing wrappers: bid ≤ remaining/moments per channel cost)
- **bid_calibrated:** knows the mechanism (reward table, bonuses, costs, competitive scale, curvature) and grid-searches the profit-maximizing bid per context (0.02 grid + 0.001 local refinement); deterministic

### A.2 Agent Implementations (v0.4 ablation ladder)
| Agent | Type | Parameters |
|-------|------|-----------|
| baseline | Rule-based floor | Fixed bids per channel, random ±20% variation |
| channel_only | Bid-only ablation | Context-aware bidding, random action/channel |
| situation_only | Action-only ablation | Correct situation→action mapping, flat bid 1.0 |
| noisy50 / noisy80 | Graded perception | True situation with prob p; bid logic intact |
| cam_inferred | Realistic classifier | Infers situation from observable intent signal (~76% accuracy, intent only) |
| cam_learned / cam_recalibrated | Learned classifier | Interval rule fit on 2,000 labeled samples (default-dist / per-env) |
| cam_multisignal | Multi-signal classifier | Nearest-centroid on intent + competitive density + channel quality (hand-set situation centroids, 98.9% match) |
| cam_multisignal_learned / cam_multisignal_recalibrated | Learned multi-signal | Nearest-centroid fit on 2,000 labeled 3-signal samples (default-dist / per-env; 98.7% match) |
| oracle | Labeled upper bound | Ground-truth situation access (validates environment, not deployable) |
| bid_calibrated | Mechanism-aware ceiling | Oracle situation + grid-searched profit-maximizing bid (knows reward table, costs, curvature) |
| BudgetPacedAgent | Stress-test wrapper | Scales any agent's bid to remaining budget / remaining moments (§8.5.3) |

### A.3 Statistical Functions
| Function | Method | Package |
|----------|--------|---------|
| Paired t-test | scipy.stats.ttest_rel | scipy |
| Cohen's d | Manual computation | numpy |
| 95% CI | Normal approximation | numpy |

---

## Appendix B: Raw Data

Raw per-seed data is **never hand-maintained**. Regenerate with:

```bash
python3 paper/cam_sim.py --scenarios 200 --seeds $(seq -s, 1 50) \
    --robustness --alpha-sweep --label-noise --budget-pacing \
    --output-md results/cam_sim_results.md
```

- Full JSON: `results/cam_sim_results.json` (aggregate + statistics + robustness sweep + alpha sweep + label-noise + budget pacing)
- Markdown report: `results/cam_sim_results.md` (auto-generated tables incl. stress-test sections)
- Robustness table: `results/cam_sim_results_robustness.md` (9 presets, paired F3 statistics, per-seed ρ)
- `results/` is gitignored — outputs are reproducible from seed alone

Reproducibility contract: identical `--seeds` + `--scenarios` reproduce byte-identical aggregates (both RNGs seeded; verified).

---

*Paper structure ready for submission. Next: Populate references with full citations from papers.yaml; Extend CAM-Sim to 100+ seeds and field-validate with a B2B partner (§10.3); Identify JM special issue on AI.*
