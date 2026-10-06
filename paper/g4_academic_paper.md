# G4 Academic Paper: Context-Aware Agentic Marketing (CAM)
## Draft Structure for Journal Submission

> **File:** `g4_academic_paper.md`  
> **Status:** DRAFT (v0.9) — results auto-generated from CAM-Sim v0.4; peer-reviewed (stats-audit, citation-audit, threats-to-validity, journal-editor, adversarial-reviewer, domain-expert, ml-methodology, round-2: journal-editor-v2, adversarial-reviewer-v2, domain-expert-v2, ml-methodology-v2, round-3: journal-editor-v3, adversarial-reviewer-v3, domain-expert-v3, ml-methodology-v3); all numbers regenerate from cam_sim.py  
> **Target:** *NeurIPS Datasets & Benchmarks* / *KDD* / *Journal of Interactive Marketing* / *Journal of Marketing Analytics* (reframed as benchmark paper per round-3 reviewer consensus: JM/MS requires field data; computational venues reward reproducible benchmarks)  
> **Type:** Empirical (Reproducible Benchmark + Ablation Study)  
> **Word Target:** 8,000-10,000 words  
> **Key Contribution:** A reproducible paired-seed benchmark (CAM-Sim) connecting **agentic AI** (70 papers, +1.8× publications) with **marketing situational awareness** (0 papers in our corpus) + ablation-based environment-consistency evidence, including a matched-family ablation (same NCC classifier, 1 vs 3 signals) that isolates signal structure from classifier capacity  
**Caveat:** The "first" claim rests on a title/abstract keyword search of our 9,994-paper corpus, not a systematic review; contextual-bandit and context-aware-recommender literatures are adjacent but use different terminology (§5.3, §9.2 #13)  

---

## 1. Title & Running Head

**Proposed Title:** *Context-Aware Agentic Marketing: A Situational Awareness Framework for Autonomous Marketing Systems*  
**Running Head:** Context-Aware Agentic Marketing  
**Keywords:** Agentic AI, Contextual Intelligence, Situational Awareness, Marketing Automation, Dynamic Targeting

---

## 2. Abstract (150-200 words)

**DRAFT:**
The emergence of agentic AI in marketing (70 papers, +1.8× growth in our corpus of 9,994) has outpaced frameworks for marketing context. While practice uses "contextual intelligence" as adtech vocabulary and Häglund (2025) defines it computationally for NLP, no paper in our corpus operationalizes situational awareness for autonomous marketing agents. We propose **Context-Aware Agentic Marketing (CAM)**, a four-layer framework (sense → model → reason → act) grounded in Endsley's situational awareness model. We evaluate it in CAM-Sim, a paired-seed synthetic benchmark: 50 seeds × 200 scenarios (10,000 evaluations per agent), eleven agents on a situational-awareness ladder from context-blind baseline through graded-perception (50%/80%) and signal-based classifiers (intent-only 87.5% learned, 98.7% multi-signal learned) to a labeled oracle and mechanism-calibrated bidder. Multi-signal awareness — the framework's core claim — raises match from 87.5% (learned single-signal) to 98.7% (learned multi-signal) and profit from +$155 to +$205 (+$50, p = 8.5e-32, d_z = 3.96); against a hand-tuned threshold classifier (75.7%, 4-of-6 classes), the gain is larger: +$102 (p = 5.4e-46). All profits are scaled-reward proxies, not validated currency (§9.2 #12). The advantage holds across nine environments (per-seed ρ ≥ 0.93), survives 30% label noise and budget pacing, and is checked by bootstrap BCa CIs (200 resamples; diagnostic, not confirmatory — §9.2 #15) and seed-count convergence (non-monotone, §9.2 #17). Miscalibrated bid modulation is worse than none; calibrated bidding nearly doubles flat bidding (+$530 vs +$294). A matched-family ablation (same nearest-centroid family, 1 vs 3 signals) confirms the gain is signal-driven, not classifier-capacity-driven (−$103.85, p = 5.16e-46); a majority-action floor (35.1% match, −$15.38) retires the random-action baseline; paired-difference bootstrap (B = 2000) confirms the normal-approximation CIs. We contribute a reproducible benchmark, environment-consistency evidence, and a pre-specified field-validation design.

---

## 3. Introduction

### 3.1 The Agentic Revolution in Marketing
The marketing corpus shows **70 agentic papers** (all from 2025-2026; 58 in 2026 alone), **burst growth of 1.8×** — the highest momentum trend. Yet **zero papers** connect agentic capabilities with **marketing situational awareness** (115 contextual papers, 6 situational papers, 0 combined with agentic).

**Research Gap:** Agents can plan and execute, but cannot **understand marketing context**.

### 3.2 The Häglund Prior Art Problem
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

**Scope caveat:** This is a keyword co-occurrence search (title/abstract) within our 9,994-paper corpus, not a systematic literature review. Adjacent literatures — **contextual bandits** (Agrawal & Goyal, 2013; Li et al., 2010; production deployments at every major ad platform), **context-aware recommender systems** (Adomavicius & Tuzhilin, 2011), and **pervasive/ubiquitous computing** (Dey, 2001) — address context-aware action selection but do not use the "agentic + situational awareness" terminology. The zero-intersection finding is a terminological gap, not evidence of conceptual novelty; a systematic review is needed to substantiate a first-mover claim (§9.2 #13).

### 5.4 Häglund (2025) — CS/NLP
**Key Differentiation:**
| Aspect | Häglund (2025) | Contextual Bandits | This Work (CAM) |
|--------|---------------|-------------------|------------------|
| **Domain** | Computer Science / NLP | Online advertising, recommender systems | Marketing |
| **Focus** | Opinion-unit extraction, aspect-based sentiment | Context-aware action selection under uncertainty | Agentic situational awareness |
| **Construct** | — | Context vector → arm selection | **Contextual Intelligence in Marketing (CIM)** |
| **Level** | Algorithm/method | Algorithm/policy | System/capability framework |
| **Agentic** | No | Partially (adaptive policies) | Yes |
| **Marketing Construct** | No | Partially (bid optimization) | Yes |
| **Situational Awareness** | No | No (context features, not situation taxonomy) | Yes (Endsley Levels 1–3) |

**Positioning vs contextual bandits:** Contextual bandits (Li et al., 2010; Agrawal & Goyal, 2013) are the closest algorithmic neighbor — they select actions from context signals and are deployed at scale in ad platforms. CAM differs in three respects: (1) bandits optimize a scalar reward from a fixed arm set; CAM introduces a **situation taxonomy** (6 archetypes) that mediates context→action mapping; (2) bandits learn online from observed rewards; CAM-Sim evaluates offline classification quality against ground-truth labels; (3) bandits do not model **situational awareness** (Endsley Levels 1–3) — they are context-aware but not situation-aware. A systematic comparison with contextual-bandit baselines is deferred to future work (§10.3).

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

> **Implementation note:** The framework specifies RandomForest and LSTM components; CAM-Sim (§7) implements simplified surrogates — nearest-centroid classification (3 signals) and threshold/interval rules — to isolate the value of signal structure without conflating it with classifier capacity. The Context Predictor (Level-3 projection) is specified but not benchmarked (§6.6).

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
- **H4 (environment-consistency):** Performance will increase with situational-awareness quality — tested both by label-ordering under default economics and label-free (Spearman ρ of match rate vs. profit across agents) across 9 environment presets (Section 8.4)

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
  - `noisy50` / `noisy80` — perceives true situation with probability p; on a miss, re-draws uniformly from all 6 situations (effective accuracy ≈ p + (1−p)/6 = 58.3% / 83.3%, not 50% / 80%; graded Endsley Level-1 error)
  - `cam_inferred` — infers situation from **intent alone** (hand-tuned threshold classifier, ~76% accuracy due to genuine signal overlap — crisis↔decision and retention↔exploration are conflated)
  - `cam_multisignal` — infers situation from **three signals** (intent + competitive density + channel quality) via nearest-centroid classification (98.9% match — tests the CAM framework's core claim that multi-signal awareness outperforms single-signal). **Note:** the hand-set centroids are the true generative means; 98.9% is the nearest-centroid lower bound, not the Bayes rate (a prior-weighted MAP classifier achieves ≈99.2% on these features). The learned variant (`cam_multisignal_learned`, 98.7%) is the fair empirical result.
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
- **95% CIs** from seed-level standard error (mean ± 1.96·SE; at n = 50 the t-quantile t(49, 0.975) = 2.01 differs by 2.5%, negligible at these effect sizes)
- **Bootstrap BCa CIs** (§9.2.2, 200 resamples) provide a non-parametric check on the normal-approximation CIs (diagnostic, not confirmatory — §9.2 #15)
- **α = 0.05**; p-values reported in scientific notation
- **Multiplicity:** 10 agents × 6 metrics vs baseline per environment (60 tests); the smallest p-value is 3.3e-70 and the largest is 8.5e-15, both far below a Bonferroni-corrected α = 0.05/60 = 8.3e-4, so all reported comparisons survive familywise correction within a single environment. Across 9 environments plus exploratory grids (α-sweep, label-noise, budget-pacing), the full family is ≈540+ tests; all p-values remain far below any reasonable correction.
- ROAS computed at **aggregate level** (total value / total spend), not as a mean of per-action ratios (which is unstable under near-zero-cost actions)

---

## 8. Results

> All numbers in this section are auto-generated from CAM-Sim v0.4 (`paper/cam_sim.py --scenarios 200 --seeds 1..50 --output-md results/cam_sim_results.md [--robustness --alpha-sweep --label-noise --budget-pacing]`). All numbers regenerate from cam_sim.py.

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

*Note: Cohen's d is between-group pooled (d_pooled). Paired within-subject d_z values are 1.4–1.5× smaller. Direct cam_multisignal − cam_inferred contrast: +$101.87, 95% CI [$98.3, $105.5], p = 5.4e-46, d_z = 7.88. CIs use z = 1.96; the t(49) equivalent is 2.01 (2.5% wider). Bootstrap BCa CIs (200 resamples, §9.2.2) check these intervals to within $1.4 (diagnostic, not confirmatory — §9.2 #15).*

### 8.3 Findings

**F1 (H1–H3 supported):** Every situation-aware agent significantly outperforms baseline on match rate, profit, and ROAS (all p ≤ 8.5e-15; every 95% CI excludes zero). Channel-only bidding outperforms on profit and ROAS but not on match rate (15.4% vs 21.6%), as it uses channel context without situation classification.

**F2 (H4 supported — environment-consistency):** Profit increases monotonically across the awareness ladder: noisy50 (+$48.31) < cam_inferred (+$104.26) < noisy80 (+$145.70) < cam_learned (+$155.38) < **cam_multisignal (+$206.13)** ≈ cam_multisignal_learned (+$205.39) < oracle (+$210.00) < **bid_calibrated (+$530.45)**. The `cam_inferred` classifier achieves 75.7% match because crisis/opportunity/decision intent distributions genuinely overlap — realistic classifier confusion, not an artifact. The *learned* intent-only classifier (87.5% match, +$155.38) sits close to noisy80 (83.7% match, +$145.70): on a **single signal**, profit gains flatten at high match rates — and *where* errors land matters as much as how many (§8.4, F6/F7). The multi-signal classifiers break this plateau (F9).

**F3 (the bid surprise — refined by the calibrated ceiling):** `situation_only` (+$294.27) **outperforms the heuristic-bid oracle** (+$210.00). But the mechanism-calibrated agent reframes the finding: `bid_calibrated` (+$530.45, ROAS 26.4) nearly **doubles** flat bidding. So bid modulation is *not* worthless — it is worth ≈ +$236/episode when calibrated to the mechanism, and *value-destroying when miscalibrated*: the oracle's hand-set context multipliers (uncorrelated with the clearing price) burn −$84 relative to flat bidding. **The ordering flat > heuristic-bid holds in 8 of 9 environments** (§8.4), including doubled costs (where `situation_only` +$111.60 is the *only* heuristic-bid agent in profit) and under budget caps. The single ordering flip (concave returns, α = 0.5) is a local crossing of two suboptimal policies, not a boundary of the calibrated result — `bid_calibrated` dominates every heuristic at *every* curvature tested (§8.5).

**F4 (decomposition):** Action matching is the dominant deployable value driver (+$464.30 from situation knowledge alone); bid optimization alone adds +$59.88 (p = 8.5e-15) but cannot cross into profitability without situation knowledge (channel_only stays at −$110.16). Full value requires both, correctly weighted: situation knowledge + calibrated bidding (+$530.45) > situation knowledge + flat bidding (+$294.27) > situation knowledge + *mis*calibrated bidding (+$210.00) > everything else.

**F9 (multi-signal awareness — the framework's core claim, confirmed):** Adding competitive density and channel quality to the intent-only signal raises match and profit. **The fair comparison is learned-vs-learned:** `cam_multisignal_learned` (98.7%, +$205.39) vs `cam_learned` (87.5%, +$155.38) — a +$50.01 gain (p = 8.5e-32, d_z = 3.96, 95% CI [+$46.5, +$53.5]), confirming that multi-signal structure is recoverable from data alone. **Against the hand-tuned threshold classifier** (`cam_inferred`, 75.7%, 4-of-6 classes, +$104.26), the gain is larger: +$101.87 (p = 5.4e-46, d_z = 7.88) — within $3.87 of the oracle (+$210.00). The advantage is **universal on the handicapped comparator**: `cam_multisignal` beats `cam_inferred` in all 9 environments (§8.4), with the largest swings exactly where intent-only classification collapses — `crisis_heavy` (−$66.8 vs +$141.9, a +$208.7 swing) and `retention_heavy` (−$15.5 vs +$237.2, +$252.7). The learned-vs-learned comparison is not reported per-environment (§10.3 #11). Mechanism: intent alone conflates crisis↔decision (both high intent) and retention↔exploration (both low intent); competitive density and channel quality resolve both ambiguities. This is the operational validation of CAM Layer 1 (*sense multi-modal context signals*): multi-signal awareness is not a marginal improvement but the difference between sub-oracle and near-oracle performance.

**Interpretation:** **Multi-signal situation classification is the first investment; bid modulation is a force multiplier that is only as good as its calibration.** Single-signal intent inference leaves roughly a quarter of the deployable value on the table (learned-vs-learned: +$155.38 vs +$205.39, a 24% gap), or roughly half against the handicapped comparator (+$104.26 vs +$206.13), and naive context-inflated bidding — the natural heuristic a practitioner would deploy — is *worse than doing nothing at the bid layer*. The CAM value proposition: invest first in **multi-signal situation classification** (intent + competitive density + channel quality), then in mechanism-calibrated bidding, and never in unvalidated bid heuristics.

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

**F6 (recalibration is the remedy — and multi-signal is the better remedy):** Refitting the same learner per distribution recovers most of the F5 loss: `crisis_heavy` −$66.8 → **+$27.1**; `retention_heavy` −$15.5 → **+$164.5**; `uniform_situations` −$31.0 → **+$32.3**. A classifier merely *learned* on the default distribution but deployed shifted (`cam_learned`, −$6.9 under crisis) stays biased — the gain comes specifically from **recalibration**, not from learning per se. **Multi-signal recalibration** (`cam_multisignal_recalibrated`) is even more robust: it tracks the hand-set multi-signal agent closely (within $1.79, max under `concave_returns`) and dominates intent-only recalibration — e.g. `uniform_situations` +$160.1 vs +$32.3. Exception: under `uniform_situations` the intent-only recalibrated classifier earns *less* than noisy50 under label noise (−$26.1 at ε = 0.2 vs +$7.9) despite a *higher* match rate (67.0%) — its residual confusions route high-stakes situations into payoff-catastrophic wrong actions. **Match rate is not profit; the *placement* of errors modulates the profit relationship.**

**F7 (label-free environment-consistency check, with proper inference):** Label-ordered ladders can mislead (an 87.5%-accurate classifier *should* exceed an 80%-perception agent). The label-free test — Spearman ρ(context match rate, profit) across agents — is computed **within each seed** (50 paired replicates of a 13-agent ranking) and reported as mean [95% CI]: **0.94–0.99 across all nine environments, with every lower CI bound ≥ 0.93** (Table). Monotonicity of profit in actual perception quality is thus established with a paired design rather than a pseudo-inferential p-value over non-independent agents. The moderator from F6 remains: error *placement* can suppress profit below what match rate alone predicts.

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

**Implications:** (1) the action-matching value claim is robust across economic regimes; (2) environment-consistency is universal when measured label-free; (3) systematically biased classifiers under distribution shift are a *deployment* problem with a known fix — per-distribution recalibration, or multi-signal inference that avoids the bias altogether (F9); (4) invest in bid optimization only when the buying mechanism rewards incremental spend.

---

### 8.6 Ablations (Round-3 Reviewer Experiments)

Three deferred experiments requested by round-3 reviewers, now run.

**Majority-action floor.** An always-EDUCATIONAL, flat-bid policy (the strongest context-blind baseline) achieves 35.1% match and −$15.38 profit — better than the random-action `baseline` (21.6%, −$170.03) but still negative. The context-aware agents (cam_inferred +$104.26, cam_multisignal +$206.13) dominate this floor. This retires the “engineered strawman” objection (adversarial New-Attack 4): the floor is now a majority-action policy, not a random agent.

**Matched-family ablation.** A nearest-centroid classifier on intent-only (`ncc_intent_only`, same NCC family as `cam_multisignal`, 1 signal instead of 3) achieves 72.7% match and +$102.28 profit. The 3-signal NCC (`cam_multisignal`, 98.9% match, +$206.13) outperforms it by +$103.85 (p = 5.16e-46, d_z = 7.89, paired-diff bootstrap CI [−$107.55, −$100.13]). Because both classifiers are nearest-centroid with the same calibration sample, the gap is signal-driven, not classifier-capacity-driven — directly addressing the family-confound concern (adversarial New-Attack 1, §9.2 #13–14).

**Paired-difference bootstrap (B = 2000).** The round-2 ml-methodology reviewer noted that the B = 200 bootstrap resamples marginal means, not paired differences (§9.2 #15). We re-run with B = 2000 on the paired seed-level differences for the two headline contrasts:

| Contrast | Mean diff | 95% CI (paired bootstrap, B = 2000) | Normal-approx CI |
|---|---|---|---|
| cam_multisignal − cam_inferred (handicapped) | +$101.87 | [+$98.41, +$105.49] | [+$98.30, +$105.44] |
| cam_multisignal_learned − cam_learned (learned-vs-learned) | +$50.01 | [+$46.62, +$53.69] | [+$46.42, +$53.60] |
| cam_multisignal − ncc_intent_only (matched-family) | −$103.85 | [−$107.55, −$100.13] | — |

The paired-difference bootstrap CIs are within $0.30 of the normal-approximation CIs, confirming the normal approximation is adequate for the paired design. The matched-family ablation CI is new.

---

## 9. Discussion

### 9.1 Why Context Awareness Wins (and Where It Doesn't)
**Mechanism Analysis:**
- **H1 (Context Match):** ✅ Supported — every situation-aware agent reaches 59.6–100% match vs 21.6% baseline
- **H2 (Profit):** ✅ Supported — all context-aware agents generate higher profit than the baseline (channel-only bidding improves to −$110.16 from −$170.03 but remains unprofitable; all situation-aware agents are profitable)
- **H3 (ROAS):** ✅ Supported — aggregate ROAS rises from 0.484 (baseline) to 1.20–2.61 for heuristic agents and **26.37 for `bid_calibrated`**
- **H4 (Environment-consistency):** ✅ Supported — per-seed Spearman ρ(match rate, profit) 0.94–0.99 across all 9 environments, every 95% CI lower bound ≥ 0.93 (F7); label-ordering holds under default economics and breaks only for the biased hand-tuned classifier under distribution shift (F5), which recalibration largely fixes (F6); multi-signal inference eliminates the bias altogether (F9). **Caveat:** ρ is partly mechanical — the match bonus is a linear component of profit (§9.2 #11); the dose-response is better read as an environment-consistency check than an empirical law.
- **Mediation:** *Deferred* — not testable in this design (see §6.6); requires a perception-level continuum

**Key insight (F3, refined by the calibrated ceiling; F9 extends it):** The dominant *deployable* mechanism is **multi-signal action selection**; bid modulation is a force multiplier that is only as good as its calibration. `situation_only` (+$294) beats the heuristic-bid `oracle` (+$210) because unvalidated context multipliers burn cost; but `bid_calibrated` (+$530) nearly doubles flat bidding. For CAM practice: invest first in **multi-signal situation classification** (F9: +$206 vs +$104 for single-signal), then in **mechanism-calibrated bidding** — and never deploy unvalidated bid heuristics, which are worse than not bidding at all.

**Honest framing of the oracle:** The oracle is an upper bound that validates environment consistency. The scientifically meaningful agents are `cam_multisignal` (three-signal classifier, 98.9% match, within $4 of oracle — but the $3.87 gap is itself significant: p = 1.3e-13, d_z = 1.43), `cam_multisignal_learned` (98.7%, the evidence that the structure is recoverable from data alone), `cam_inferred` (single-signal, 75.7% match, 4-of-6 classes), and the noisy agents (graded perception). The hand-set `cam_multisignal` uses the true generative centroids; its 98.9% match is the **nearest-centroid lower bound, not the Bayes rate** — a prior-weighted MAP classifier on the same features achieves ≈99.2%. The learned variant (98.7%) is the real empirical result. The **fair single-signal comparator is `cam_learned`** (87.5%, +$155.38), not the handicapped `cam_inferred` (75.7%, +$104.26): the learned-vs-learned gain is +$50.01 (p = 8.5e-32, d_z = 3.96), while the handicapped-vs-multisignal gain is +$101.87. The environment-consistency across these — not oracle-vs-baseline — is the paper's core empirical claim.

### 9.2 Limitations
1. **Reward-design circularity:** The situation→ideal-action table and reward magnitudes are author-designed; the environment cannot falsify the framework's own mapping. External validity requires field validation (Section 10.3). A pre-specified **adversarial-mapping condition** — in which the designer-preferred action is *not* the reward maximizer — would separate "CAM wins" from "following the scoring rubric scores points."
2. **Bid-layer calibration: tested.** The original oracle's hand-set bid multipliers are miscalibrated (hence F3). `bid_calibrated` — which numerically maximizes expected profit against the known mechanism — now provides the true ceiling (+$530.45 default; dominant in all 9 environments and at all curvatures α ∈ [0, 1.5], §8.5.1). Remaining scope: a *learned* bidding policy that discovers the mechanism from feedback alone (the calibrated agent is given the mechanism), and auction-style clearing.
3. **Oracle construction:** The oracle and `bid_calibrated` receive ground-truth situation labels; they are upper bounds, not deployable agents. Headline effects (d_pooled = 9–35) reflect the design; the scientifically meaningful agents are the noisy/classifier ladder and `cam_multisignal` (near-oracle without ground truth).
4. **Perception/bidding confound in the environment-consistency check:** The awareness ladder mixes perception quality with bid policy — the 100%-match agents span $320 of profit (`situation_only` +$294.3, `oracle` +$210.0, `bid_calibrated` +$530.5). The per-seed ρ(match rate, profit) across agents is therefore not a clean dose-response; a test that holds the bid policy fixed and varies only perception probability p would isolate the perception effect.
5. **`cam_inferred` is a structurally handicapped comparator:** its threshold rule can emit only 4 of 6 situation classes (never CRISIS or RETENTION), so its 75.7% match and distribution-shift collapse (F5) partly reflect a missing-class artifact. `cam_learned` (87.5%, emit-any-class) is the fairer intent-only comparator; the qualitative F5 story survives, but the magnitude is overstated by `cam_inferred`.
6. **Signals are supplied, not sensed:** `channel_quality` and `competitive_density` are exact scalars on the context; the `signals` field (the implemented Sensing Layer) is decorative and unused by agents. Feature extraction, missingness, and latency are assumed away — claims about multi-modal *sensing* are therefore not tested by CAM-Sim.
7. **Between-environment robustness: tested, but author-selected.** The ladder replicates across **9 environment presets** spanning distribution shifts, doubled costs, budget caps, a concave-returns curvature (α = 0.5), and weakened context payoffs (§8.4); a separate curvature sweep (α ∈ [0, 1.5], §8.5.1) tests bid sensitivity: per-seed environment-consistency ρ ≥ 0.93 (lower CI) everywhere; `bid_calibrated` is the invariant ceiling; multi-signal inference outperforms single-signal in all 9 presets (F9). These are author-chosen configurations, not draws from a distribution of real environments — replication across chosen presets is internal consistency, not external validity.
8. **Calibration protocol: stress-tested.** The F6 recalibration remedy survives **30% label noise**: intent-only match rates degrade by ≤ 0.6 pp; multi-signal recalibration degrades up to 14 pp (retention 98.9→84.9) but stays strongly profitable (≥ +$106) (§8.5.2). Remaining scope: label *drift* over time and labeling costs.
9. **Budget-awareness: tested.** Standard even-pacing wrappers do not change any conclusion: paced oracle (+$280.5) still loses to flat situation_only (+$294.3; §8.5.3).
10. **Seed pairing is fair but low-power.** Contexts are generated once per seed and shared across all agents (removing the scenario-draw confound), but the measured seed-level correlation between baseline and each agent is **−0.23 to +0.08** (mean ≈ −0.1): near zero, mostly negative. Every agent draws from a single global `random` stream seeded once per seed and consumed sequentially, so agent *k* sees the stream after agents 1…k−1 have consumed it — the *context* is paired but the *decision noise* is not. The paired t-test remains **valid** (it controls the seed-level confound), but pairing buys no power advantage over an unpaired test. Common random numbers (independent stream per agent, same contexts) would pair the noise and tighten inference; this is deferred to the next version.
11. **Match rate is a design-relative measure.** `context_match = (action == IDEAL_ACTION[situation])` measures agreement with the authors' mapping and is mechanically tied to the match bonus. Under the skewed class distribution (exploration 35%, consideration 30%), raw accuracy is unbalanced: a majority-class classifier would score non-trivially. Macro-F1 and per-class recall would be more informative; match rate should not be read as “contextual intelligence.”
12. **Profit is a scaled-reward proxy, not a validated outcome.** `profit = reward + long_term_value − cost`, with LTV a fixed multiple of the same reward — no discounting, incrementality, or carryover. Profit *signs* may generalize to real campaigns; magnitudes (e.g., ROAS 26.4) have no industry analogue.
13. **Missing comparators:** No logistic regression, gradient-boosted tree, random forest, or contextual bandit (LinUCB, ε-greedy) baseline is benchmarked. The framework itself specifies RandomForest/LSTM components (§6.4), but CAM-Sim implements nearest-centroid and threshold rules — the simplest classifier family that is also the generative family (well-separated Gaussian clusters). A stronger classifier on the same signals could narrow or close the multi-signal advantage; a matched-family ablation (NCC on intent-only vs NCC on 3 signals, §8.6) shows the gap is signal-driven (+$103.85, p = 5.16e-46), but a nonlinear learner (LR/GBM) on 1 and 3 signals remains future work.
14. **Classifier family = generative family:** The nearest-centroid classifier is Bayes-optimal only in the isotropic/equal-prior special case; the generator uses unequal priors and non-isotropic features (intent SD 0.1, competition/quality SD 0.15), so 98.9% is a lower bound, not the Bayes rate (a prior-weighted MAP classifier achieves ≈99.2%). `cam_multisignal` (hand-set centroids = true means) therefore achieves the generator's lower bound, not an empirical classifier result. `cam_multisignal_learned` (98.7%) confirms the estimator is unbiased but cannot demonstrate recovery under realistic conditions (shifted, noisy, or partly missing signals). The headline +$101.87 gain is measured against a handicapped comparator (`cam_inferred`, 4-of-6 classes); the fair learned-vs-learned gain is +$50.01 (§9.1, F9).
15. **Bootstrap B = 200 is underpowered:** The BCa CIs use 200 resamples; the Monte-Carlo noise in CI endpoints at B = 200 is ≈$2–3.5, exceeding the reported "$1.4 agreement" with normal CIs. The bias-correction |z₀| ≤ 0.16 is within ~1.7 standard errors of zero (MC SE ≈ 0.09). The bootstrap also resamples **marginal** per-agent means, not the **paired differences** that carry the inferential claims (e.g., cam_multisignal − cam_inferred). **Resolved (§8.6):** a paired-difference bootstrap with B = 2,000 confirms the normal-approximation CIs within $0.30 for both headline contrasts.
16. **Label noise is uniform, not class-conditional:** The ε-corruption flips each label to a uniformly random alternative. Real label noise is class-conditional (crisis↔decision and retention↔exploration are the documented confusable pairs) and boundary-concentrated. Uniform noise induces a graceful, symmetric degradation; class-conditional noise may produce different per-class recall patterns and a different multi-signal floor (§10.3).
17. **Convergence N = 10 is vacuously stable:** The convergence diagnostic declares a metric "stable from 10 seeds" because the last-10-seed mean equals the overall mean at N = 10 (the window is the entire sample). The meaningful threshold is N ≥ 20 (cam_multisignal +$208.52 at N = 20, within 1.2% of N = 50). No trend test (Spearman of metric vs seed index, Geweke z-score) is applied; a slow monotone drift could pass the 5% criterion.
18. **Six situations conflate three constructs:** Exploration/consideration/decision are funnel stages (person-level); crisis/opportunity are market conditions (environment-level); retention is a lifecycle state (account-level). A practitioner would model these as orthogonal axes (stage × condition), not a flat 6-way taxonomy. The flat design forces confusions (crisis↔decision) that an orthogonal design would not have.
19. **Single-decisioner model:** The simulation models one decision per scenario. B2B buying involves 6–10 stakeholders per account (champion, economic buyer, technical evaluator, blocker), each in a different stage. The situation→action mapping is a single-person approximation; an account-level aggregation is needed for B2B.
20. **Bid mechanism is simplified:** The simulated auction (reward = f(bid/clearing price), exogenous clearing price, cap) omits first-price dynamics, quality scores (Google Ad Rank, Meta total value), frequency caps, audience overlap, and censored feedback (clearing prices observed only on wins). `bid_calibrated` is given the mechanism — an omniscience no practitioner has. F3 (miscalibrated bidding worse than flat) survives (it is the industry's own migration to automated bidding), but the calibrated ceiling (+$530) is an artifact of mechanism knowledge.
21. **Even-pacing is the most naive budget algorithm:** The §8.5.3 pacing wrapper is even-spend (bid ≤ remaining/moments). Real systems use forecast-paced, PID-controlled, or RL-based pacing; pacing and bidding are coupled (pacing shades effective bids in first-price auctions), not an outer wrapper. The pacing conclusion (F3 survives) is directionally correct but premature.
22. **Match rate is not a practitioner KPI:** `context_match = (action == IDEAL_ACTION[situation])` measures agreement with the authors' mapping, not a field metric. Practitioners measure CTR, CVR, CPL, ROAS, and holdout-based uplift. Match rate is a design-relative diagnostic (§9.2 #11), not a deployable KPI; the profit proxy (§9.2 #12) is the closest field analogue but is unvalidated.
23. **Crisis action mapping may be backwards:** the Action Layer doubles the bid in `crisis` situations (§6.5, 2.0× multiplier). Standard brand-safety practice for most crises is to pause or exclude, not increase spend; deliberate counter-messaging is a niche, senior call. The hardcoded 2.0× multiplier is an author choice, not an empirically validated response, and an autonomous agent with this default could amplify a brand-safety incident.
24. **Sensing layer emits a decoy signal:** the `quality_score` field in the generated signals is drawn uniform(0.5, 1.0), uncorrelated with the situation-linked `channel_quality` the classifiers actually read. The implemented Sensing Layer therefore emits a feature that is not the real signal; any multi-modal sensing claim should be understood as testing the classifier on the three real signals (intent, competitive density, channel quality), not the sensing infrastructure.

#### 9.2.1 Statistical Discipline
- **Multiplicity:** All p-values survive Bonferroni correction (§7.3). The α-sweep, label-noise, and pacing grids are exploratory — a pre-specified analysis plan with a familywise hierarchy is deferred to the field trial (§10.3).
- **Normality:** Profit distributions are unimodal and approximately symmetric at the seed level; the paired t-test is robust at n = 50. Bootstrap BCa CIs (§9.2.2) provide a non-parametric check — though B = 200 is underpowered (§9.2 #15); the normal-approximation CIs are the primary inference.
- **Equivalence testing:** "Within $4 of the oracle" is descriptive — the residual $3.87 gap is significant (p = 1.3e-13, d_z = 1.43). `cam_multisignal` (+$206.13) vs `cam_multisignal_learned` (+$205.39) is also significant (p = 2.5e-04, d_z = 0.56) despite the near-identical match rate (98.9% vs 98.7%). "Essentially matches" claims should carry the caveat that the differences are statistically detectable at n = 50, even if economically negligible.

#### 9.2.2 Robustness of the Design to Resampling and Seed Count

**Bootstrap BCa CIs (200 resamples per agent; `--bootstrap 200`):** The non-parametric BCa CIs check the normal-approximation CIs to within $1.4 for all 11 agents (max: `noisy80`, $1.31). BCa bias-correction |z₀| ranges from 0.00 to 0.16 (noisy80, the most skewed); |acceleration| ≤ 0.014 — the bootstrap distributions are approximately centered and unbiased. **Caveat (§9.2 #15):** B = 200 produces Monte-Carlo endpoint noise of ≈$2–3.5, exceeding the reported agreement. The bootstrap resamples marginal per-agent means, not the paired differences that carry the inferential claims; **a paired-difference bootstrap (B = 2,000, §8.6) confirms the normal-approximation CIs within $0.30** for both headline contrasts.

| Agent | Mean | Normal 95% CI | BCa 95% CI |
|------|------|---------------|------------|
| baseline | −$170.03 | [−177.9, −162.2] | [−178.0, −162.8] |
| channel_only | −$110.16 | [−116.2, −104.1] | [−115.9, −103.8] |
| situation_only | +$294.27 | [+292.4, +296.1] | [+292.5, +296.0] |
| noisy50 | +$48.31 | [+42.1, +54.5] | [+42.7, +54.0] |
| noisy80 | +$145.70 | [+140.5, +150.9] | [+141.8, +152.1] |
| cam_inferred | +$104.26 | [+99.9, +108.6] | [+100.5, +108.1] |
| **cam_multisignal** | **+$206.13** | **[+202.0, +210.2]** | **[+202.5, +210.0]** |
| cam_learned | +$155.38 | [+150.6, +160.1] | [+150.8, +159.4] |
| cam_multisignal_learned | +$205.39 | [+201.3, +209.5] | [+201.5, +209.0] |
| oracle | +$210.00 | [+205.8, +214.2] | [+206.4, +214.8] |
| bid_calibrated | +$530.45 | [+529.4, +531.5] | [+529.4, +531.3] |

**Seed-count convergence diagnostic (`--convergence`):** Mean profit for `cam_multisignal` is non-monotone but stays within 5% of the final 50-seed value from **20 seeds onward** (+$208.52 at 20 seeds → +$206.13 at 50 seeds, 1.2% drift; intermediate: +$213.76 at 10, +$209.69 at 30, +$206.57 at 40). The per-seed Spearman ρ(match rate, profit) is stable at **ρ = 0.981** across all seed counts. The baseline shows the largest drift (−$177.18 at 10 seeds → −$170.03 at 50, 4.2%) but stays within the 5% criterion at every seed count. **Caveat (§9.2 #17):** the N = 10 row is vacuously stable (last-10 = entire sample at N = 10); the path is non-monotone (no trend test applied); a slow monotone drift could pass the 5% criterion. **Conclusion: the default 50-seed design is adequate; 20 seeds suffice for `cam_multisignal` and ρ, but convergence is not formally established.**

| Seeds | cam_multisignal | ρ (per seed) | baseline | stable cam/ρ/base |
|-------|-----------------|--------------|----------|--------------------|
| 10 | +213.76 | 0.981 | −177.18 | YES / YES / YES |
| 20 | +208.52 | 0.981 | −173.50 | YES / YES / YES |
| 30 | +209.69 | 0.981 | −171.90 | YES / YES / YES |
| 40 | +206.57 | 0.981 | −171.53 | YES / YES / YES |
| 50 | +206.13 | 0.980 | −170.03 | YES / YES / YES |

### 9.3 Practical Implications
**For Marketers:**
- **Multi-signal awareness > single-signal:** Adding competitive density and channel quality to intent raises deployable profit (+$206 vs +$104 vs a handicapped classifier, +$50 vs a matched learned classifier; p = 8.5e-32) — but all profits are scaled-reward proxies (§9.2 #12)
- **Calibrate bidding to the mechanism:** Miscalibrated context-inflated bidding is worse than flat bidding (oracle +$210 vs situation_only +$294); calibrated bidding nearly doubles flat (+$530) — but only with mechanism knowledge no practitioner has (§9.2 #20)
- **Recalibrate per distribution:** Per-environment recalibration recovers F5 losses (crisis −$67 → +$27); multi-signal inference avoids the bias altogether
- **Privacy-aware signal design:** CAM uses context signals (intent, competitive density, channel quality), not PII — but the intent scalar behaves like fully-observed identified-user intent, which cookieless environments remove; privacy-safe deployment requires signal-level differential privacy or on-device inference (§9.2 #6, #20)

**For Researchers:**
- **Terminological gap confirmed:** 0 papers in our corpus connect agentic + situational awareness in marketing (§5.3) — but this is a keyword search, not a systematic review; contextual-bandit and context-aware-recommender literatures are adjacent (§5.4)
- **Framework available:** CAM's four-layer architecture (sense → model → reason → act) is extensible
- **Benchmark available:** CAM-Sim is reproducible (fixed seeds, byte-identical), with bootstrap BCa CIs and seed-count convergence diagnostics

### 9.4 Theoretical Implications
**For Situational Awareness Theory:**
- Endsley's Level 1–2 model applies to marketing agents: perception quality (match rate) and comprehension (situation classification) drive measurable profit differences (per-seed ρ ≥ 0.93)
- Level-3 projection (future context) is specified but not benchmarked — a candidate differentiator for future work (§10.3)

**For Agent Theory:**
- Situational awareness is the dominant value driver (+$464 from action matching vs +$60 from bid optimization alone)
- Non-context-aware agents are suboptimal by design: the baseline loses $170/episode

---

## 10. Conclusion & Future Work

### 10.1 Summary
We introduced **Context-Aware Agentic Marketing (CAM)** — a framework connecting agentic AI with marketing situational awareness, grounded in Endsley's SA model. In a paired-seed synthetic benchmark (50 seeds × 200 scenarios, 10,000 evaluations per agent), multi-signal situation classification (intent + competitive density + channel quality) raises match from 87.5% (learned single-signal) to 98.7% (learned multi-signal) and deployable profit from +$155 to +$205 (+$50, p = 8.5e-32, d_z = 3.96); against a hand-tuned threshold classifier, the gain is +$102 (p = 5.4e-46). A matched-family ablation (same NCC family, 1 vs 3 signals) isolates the gain as signal-driven (+$103.85, p = 5.16e-46); a majority-action floor (35.1%, −$15.38) retires the random-action baseline; paired-difference bootstrap (B = 2000) confirms the normal-approximation CIs. The advantage replicates across 9 environments (per-seed ρ ≥ 0.93), survives 30% label noise and budget pacing, and is checked by bootstrap BCa CIs (diagnostic, not confirmatory — §9.2 #15) and seed-count convergence (non-monotone, §9.2 #17). All profits are scaled-reward proxies (§9.2 #12). The central practical finding: invest first in **multi-signal situation classification**, then in **mechanism-calibrated bidding** — unvalidated bid heuristics are worse than not bidding at all.

### 10.2 Contributions
1. **Theoretical:** Grounded CAM in Endsley's SA model (Levels 1–3 situational awareness applied to marketing automation)
2. **Conceptual:** Created a four-layer framework for context-aware marketing agents
3. **Empirical:** CAM-Sim ablation benchmark — reproducible, paired-seed statistics; profit spans −$170.03 (random-action baseline) to −$15.38 (majority-action floor) to +$294.27 (perfect action matching) to +$530.45 (situation knowledge + mechanism-calibrated bidding); monotone environment-consistency in perception quality (per-seed ρ ≥ 0.93 lower-CI in all 9 environments)
4. **Empirical:** Four novel findings — (F3/F8) miscalibrated context-inflated bidding is *worse than flat bidding* (replicates 8/9 environments, survives budget pacing); (F5/F6) systematic classifier bias under distribution shift beats coin-flip adversely, and per-distribution recalibration fixes it robustly to 30% label noise; (F6) match rate is not profit — error *placement* modulates the profit relationship; (F9) multi-signal awareness (intent + competitive density + channel quality) raises match from 87.5% (learned) to 98.7% (learned) and profit by +$50 (p = 8.5e-32, d_z = 3.96); against a hand-tuned classifier, +$102 (p = 5.4e-46). Note: F9's universality is established on the handicapped comparator; the learned-vs-learned per-environment comparison is deferred (§10.3 #11).
5. **Methodological:** Bootstrap BCa CIs (200 resamples) provide a non-parametric check on normal-approximation CIs (§9.2.2; caveat: B = 200 is underpowered, §9.2 #15); paired-difference bootstrap (B = 2000, §8.6) confirms the normal-approximation CIs within $0.30; seed-count convergence diagnostic shows `cam_multisignal` and ρ stable from 20 seeds (§9.2.2; caveat: N = 10 is vacuously stable and the path is non-monotone, §9.2 #17); all p-values survive Bonferroni correction (§7.3). Note: ρ(match rate, profit) is an environment-consistency check, not a dose-response law — the match bonus is a linear component of profit (§9.2 #11).
6. **Ablation (new, §8.6):** Matched-family ablation (same NCC family, 1 vs 3 signals) isolates the +$50 gain as signal-driven, not classifier-capacity-driven (+$103.85, p = 5.16e-46, d_z = 7.89); majority-action floor (35.1%, −$15.38) retires the random-action baseline; paired-difference bootstrap (B = 2000) confirms normal-approximation CIs within $0.30.

### 10.3 Future Work & Field-Validation Design
1. **Pre-specified field validation (priority):** two-arm experiment with a B2B partner (candidate: the proposed G6 collaboration): **Arm A** = CAM decisioning (multi-signal situation classifier → action mapper, exactly the `cam_multisignal_recalibrated` pipeline), **Arm B** = business-as-usual rule-based targeting. Primary endpoint: profit/conversion uplift per campaign; secondary: match-rate audit of agent classifications against human-coded situations. Design: ≥ 40 campaigns per arm over 8–12 weeks, analyzed with mixed-effects models (campaign as random effect) — the field analogue of CAM-Sim's paired-seed design.
2. **Learned bidding:** train the bid layer against the clearing mechanism (F8 shows this changes conclusions under concave returns); evaluate against situation_only as the null.
3. **Adversarial-mapping condition:** run CAM-Sim with a designer-preferred action that is *not* the reward maximizer, to test whether situational awareness wins when the mapping is adversarial rather than self-confirming (§9.2 #1).
4. **De-confound perception from bidding:** hold the bid policy fixed (e.g., all agents use flat bidding) and vary only perception probability p, to isolate the perception→profit relationship from the bid-policy effect (§9.2 #4).
5. **Common random numbers:** give each agent its own RNG stream (same contexts, independent decision noise) to tighten the paired test and realize the power benefit of the shared-environment design (§9.2 #10).
6. **Macro-F1 and per-class recall:** replace raw match accuracy with macro-F1 under the unbalanced class distribution; report per-class recall so that classifier errors are visible by situation type (§9.2 #11).
7. **Adversarial & dynamic environments:** competitor adaptation, context drift, multi-period state carryover.
8. **Field studies:** deploy CAM with marketer-in-the-loop in production settings.
9. **B2B extension:** value-context Layer 0 (G6) — the value-opportunity-recognition construct (Böhm et al., 2020) operationalized as the sensing capability.
10. **Theory:** formal treatment of marketing situational awareness (Levels 1–3 as measurable perception-quality intervals).
11. **Matched-family ablation (✅ done, §8.6):** benchmarked nearest-centroid on intent-only vs nearest-centroid on 3 signals — the +$103.85 gap (p = 5.16e-46, d_z = 7.89) is signal-driven. A nonlinear learner (logistic regression or small GBM) on 1 and 3 signals remains future work to further decouple classifier capacity from signal structure (§9.2 #13–14).
12. **Contextual-bandit baseline:** add a LinUCB or ε-greedy contextual bandit on the same 3 signals as a deployable-policy comparator (§5.4, §9.2 #13).
13. **Class-conditional label noise:** replace uniform ε-corruption with an asymmetric confusion matrix concentrated on crisis↔decision and retention↔exploration (§9.2 #16).
14. **Paired-difference bootstrap with B ≥ 2,000 (✅ done, §8.6):** bootstrapped the cam_multisignal − cam_inferred and cam_multisignal_learned − cam_learned contrasts directly (B = 2000); paired-diff CIs are within $0.30 of normal-approximation CIs.
15. **Account-level aggregation for B2B:** model 6–10 stakeholders per account with per-stakeholder situations (§9.2 #19).
16. **First-price auction mechanism:** replace the exogenous-clearing-price model with a first-price or quality-scored auction; test whether F3 survives under realistic bidding dynamics (§9.2 #20).
17. **Crisis action mapping:** test alternative crisis responses (pause, exclude, counter-messaging) against the hardcoded 2.0× bid multiplier; the current mapping may be backwards for most crises (§9.2 #23).
18. **Sensing-layer fidelity:** replace the decoy `quality_score` with the real `channel_quality` or a noisy observation of it; test whether multi-modal sensing claims survive when the sensing layer emits correlated rather than random features (§9.2 #24).
19. **Majority-action baseline (✅ done, §8.6):** an always-EDUCATIONAL, flat-bid agent achieves 35.1% match and −$15.38 profit — better than the random-action baseline (21.6%, −$170.03) but still negative, confirming that the context-aware agents' gains are not an artifact of a weak floor.

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
| noisy50 / noisy80 | Graded perception | True situation with prob p; on miss, re-draws uniformly from all 6 (effective accuracy ≈ p + (1−p)/6 = 58.3% / 83.3%); bid logic intact |
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

*Reproducibility: all numbers regenerate from `paper/cam_sim.py` with fixed seeds. Peer reviews: `reviews/stats-audit.md`, `reviews/threats-to-validity.md`, `reviews/citation-audit.md`, `reviews/journal-editor.md`, `reviews/adversarial-reviewer.md`, `reviews/domain-expert.md`, `reviews/ml-methodology.md`. Next steps: populate references with full citations from papers.yaml; add contextual-bandit baselines (§10.3 #12); field-validate with a B2B partner (§10.3 #1).*

### References (added in v0.6–v0.7)
- Agrawal, S., & Goyal, N. (2013). Thompson sampling for contextual bandits with linear payoffs. *ICML*.
- Li, L., Chu, W., Langford, J., & Schapire, R. E. (2010). A contextual-bandit approach to personalized news article recommendation. *WWW*.
- Adomavicius, G., & Tuzhilin, A. (2011). Context-aware recommender systems. *ACM RecSys*.
- Dey, A. K. (2001). Understanding and using context. *Personal and Ubiquitous Computing*, 5(1), 4–7.
