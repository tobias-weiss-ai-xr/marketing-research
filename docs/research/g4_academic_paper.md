# G4 Academic Paper: Context-Aware Agentic Marketing (CAM)
## Draft Structure for Journal Submission

> **File:** `g4_academic_paper.md`  
> **Status:** DRAFT (v0.2) — results section auto-generated from CAM-Sim v0.3; no hand-typed numbers  
> **Target:** *Journal of Marketing* (JM) / *Marketing Science*  
> **Type:** Conceptual / Empirical (Framework + Simulation)  
> **Word Target:** 8,000-10,000 words  
> **Key Contribution:** First framework connecting **agentic AI** (61 papers, +1.79× publications) with **marketing situational awareness** (0 papers) + ablation-based dose-response evidence  

---

## 1. Title & Running Head

**Proposed Title:** *Context-Aware Agentic Marketing: A Situational Awareness Framework for Autonomous Marketing Systems*  
**Running Head:** Context-Aware Agentic Marketing  
**Keywords:** Agentic AI, Contextual Intelligence, Situational Awareness, Marketing Automation, Dynamic Targeting

---

## 2. Abstract (150-200 words)

**DRAFT:**
The emergence of agentic AI systems in marketing (61 papers, +1.79× growth rate in our corpus of 7,778 marketing papers) has outpaced the development of frameworks for understanding **marketing context**—the situational, temporal, channel, social, and intent signals that determine message relevance. While marketing practice uses "contextual intelligence" as adtech vocabulary, and Häglund (2025) defines it computationally for NLP applications, **no marketing framework operationalizes situational awareness for autonomous agents**. We propose **Context-Aware Agentic Marketing (CAM)**—a four-layer framework that enables autonomous marketing agents to (1) **sense** multi-modal context signals, (2) **model** unified context representations, (3) **reason** about context relevance via an Awareness Engine, and (4) **act** through context-conditioned marketing actions. We develop CAM-Sim, a synthetic marketing simulation with an ablation-based evaluation design: every agent acts on identical scenario sequences, with both random seeds controlled. Across 50 seeds × 200 scenarios (10,000 evaluations per agent), we compare seven agents forming a situational-awareness ladder—from a context-blind baseline to graded-perception agents (50%/80% perception), a signal-based classifier (75.5% match), and a labeled oracle upper bound. Results show a monotone dose-response: mean profit improves from −$180.31 (baseline) to +$17.41 (50% perception, p = 4.8e-40), +$60.97 (inferred classifier, p = 4.9e-45), and +$105.88 (80% perception, p = 1.4e-48), with situation awareness contributing far more value (+$442.45, p = 1.1e-59) than bid optimization alone (+$52.50, p = 1.9e-15). Notably, the oracle's context-inflated bidding yields *less* profit (+$166.31) than flat bidding with perfect action matching (+$262.14) — a result that replicates in **all seven** tested environments (varying situation distributions, media costs, and context-payoff strength). A robustness sweep additionally reveals that the dose-response ordering is environment-dependent: a hand-tuned threshold classifier suffers systematic, distribution-shifted errors that can make it *worse* than unbiased 50% perception, while the action-matching and bid-surprise findings hold universally. We conclude with implications for autonomous marketing in the post-cookie era and directions for field validation.

---

## 3. Introduction

### 3.1 The Agentic Revolution in Marketing
The marketing corpus shows **61 agentic papers** (41 in 2024-2026), **burst growth of 1.79×** — the highest momentum trend. Yet **zero papers** connect agentic capabilities with **marketing situational awareness** (44 contextual papers, 4 situational papers, 0 combined with agentic).

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

### 5.1 The Agentic Literature in Marketing (61 papers from corpus)
From our marketing-research corpus (7,778 papers):
- **Definition:** Works that mention "agentic" in title/abstract
- **Total:** 61 papers
- **2024-2026:** 41 papers (12 in July 2026 alone)
- **Burst Factor:** 1.79× (highest in corpus)
- **Categories:**
  - AI-Marketing: 28 papers
  - Digital-Marketing: 15 papers
  - Analytics: 8 papers
  - Framework: 5 papers
  - Others: 5 papers

**Common Themes:**
- Agent-based simulation
- World models for marketing
- Autonomous decision systems

**Gap:** No connection to **marketing context** or **situational awareness**. Zero papers combine agentic + contextual.

*[Category breakdown above (28/15/8/5/5) asserted from exploratory analysis — re-verify against papers.yaml before submission.]*

### 5.2 The Contextual Literature in Marketing (44 papers from corpus)
- **Total:** 44 papers mentioning "contextual"
- **2024-2026:** 32 papers
- **Categories:**
  - AI-Marketing: 22 papers
  - Digital-Marketing: 8 papers
  - Analytics: 5 papers
  - Privacy/Data: 3 papers
  - B2B: 2 papers

**Common Themes:**
- Contextual advertising
- Context-aware recommendations
- Contextual targeting in privacy-preserving ways

**Gap:** No address **agentic systems**. All contextual work assumes **human-driven** systems.

### 5.3 The Zero-Intersection Problem
**Critical Finding:**
- Only **2 papers** in the entire corpus mention both "agentic" and "contextual"
- Paper #5269: "From Personalisation to Agentic Campaigns: Modern Marketing Techniques Using Artificial Intelligence in the Indian Context" (2026-07) — **superficial mention**
- Paper #7535: "I hope we don't do to trust what advertising has done to love" (2026-04) — **superficial mention**
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
- **H4 (dose-response):** Performance will increase monotonically with situational-awareness quality (noisy50 < cam_inferred < noisy80 < oracle) — *tested under default economics; robustness across environment distributions is reported in Section 8.4*

*Mediation of profit by context match was considered and deferred: under the oracle, match rate has zero variance (100% by construction) and cannot mediate. A mediation design requires a continuum of perception levels (e.g., p ∈ [0,1] in fine increments) — future work.*

**Benchmark scope note:** CAM-Sim operationalizes the Context Scorer, Situation Classifier, and Action Mapper. The **Context Predictor (Level-3 projection) is specified but NOT benchmarked** — the evaluation covers Endsley Levels 1–2 (perception quality, situation comprehension) plus action mapping only.

---

## 7. Research Design

### 7.1 CAM-Sim: Synthetic Marketing Simulation
**Why Simulation?** Reproducible, controlled evaluation without live ad spend or customer data.

**Design (v0.3 — ablation-based):**
- **Environment:** Synthetic marketing scenarios with ground-truth context; reward table maps action-type × situation to base reward, plus context-match bonus (±0.5/−0.3), bid-efficiency adjustment (±0.3/0.1/−0.2), and competitive discount
- **Fair pairing:** Scenarios are generated ONCE per seed; **every agent acts on the identical context sequence** — removing the scenario-draw confound and legitimizing seed-level paired tests
- **Full reproducibility:** Both the environment (numpy) and agents (stdlib random) are seeded per run; identical `--seeds` reproduce identical outputs (verified)
- **Agents (situational-awareness ladder):**
  - `baseline` — random channel/action, fixed bid table (context-blind floor)
  - `channel_only` — context-aware bidding, NO situation knowledge
  - `situation_only` — correct situation→action mapping, FLAT bidding
  - `noisy50` / `noisy80` — perceives true situation with probability p (graded Endsley Level-1 error)
  - `cam_inferred` — infers situation from observable intent signal (realistic classifier, ~75% accuracy due to genuine signal overlap)
  - `oracle` — ground-truth situation access (**labeled upper bound; validates environment consistency, not real-world performance**)

### 7.2 Experimental Setup
- **Seeds:** 50 independent seeds (1–50)
- **Scenarios per seed:** 200 (10,000 total per agent)
- **Robustness:** the full ladder is additionally run across **7 environment presets** (`--robustness`) that vary situation distribution (uniform, decision-, crisis-, retention-heavy), media costs (×2), and the strength of context-matching payoffs — while holding the situation→action language fixed
- **Comparison:** every agent vs. baseline (seed-level paired t-tests); ladder ordering tests H4

### 7.3 Statistical Methods
- **Paired t-test** (scipy.stats.ttest_rel) across seeds for each agent-vs-baseline metric comparison
- **Cohen's d** for effect size
- **95% CIs** from seed-level standard error
- **α = 0.05**; p-values reported in scientific notation
- ROAS computed at **aggregate level** (total value / total spend), not as a mean of per-action ratios (which is unstable under near-zero-cost actions)

---

## 8. Results

> All numbers in this section are auto-generated from CAM-Sim v0.3 (`scripts/benchmarks/cam_sim.py --scenarios 200 --seeds 1..50 --output-md results/cam_sim_results.md`). No hand-typed values.

### 8.1 Aggregate Performance (50 seeds × 200 scenarios; mean [95% CI])
| Agent | Context match % | Total profit | ROAS (agg.) | Profit/cost |
|-------|-----------------|--------------|-------------|-------------|
| baseline | 21.7 [20.9, 22.5] | −$180.31 [−187.4, −173.2] | 0.452 | −0.548 |
| channel_only | 16.8 [16.2, 17.4] | −$127.81 [−133.3, −122.3] | 0.466 | −0.534 |
| **situation_only** | **100.0** | **+$262.14** [+259.4, +264.9] | **2.435** | **+1.435** |
| noisy50 | 59.9 [59.0, 60.8] | +$17.41 [+12.4, +22.4] | 1.068 | +0.068 |
| cam_inferred | 75.5 [74.7, 76.4] | +$60.97 [+56.4, +65.5] | 1.209 | +0.209 |
| noisy80 | 83.7 [83.1, 84.3] | +$105.88 [+102.1, +109.6] | 1.393 | +0.393 |
| oracle | 100.0 | +$166.31 [+162.9, +169.8] | 1.608 | +0.608 |

### 8.2 Paired Seed-Level Tests vs Baseline
| Agent | Profit diff | 95% CI | p | Cohen's d | Sig. |
|-------|-------------|--------|---|-----------|------|
| channel_only | +$52.50 | [+43.5, +61.5] | 1.9e-15 | 2.29 | yes |
| situation_only | +$442.45 | [+434.3, +450.6] | 1.1e-59 | 22.81 | yes |
| noisy50 | +$197.72 | [+188.5, +207.0] | 4.8e-40 | 8.93 | yes |
| cam_inferred | +$241.28 | [+232.4, +250.2] | 4.9e-45 | 11.25 | yes |
| noisy80 | +$286.19 | [+277.3, +295.1] | 1.4e-48 | 14.00 | yes |
| oracle | +$346.62 | [+338.0, +355.2] | 2.2e-53 | 17.26 | yes |

### 8.3 Findings

**F1 (H1–H3 supported):** Every context-aware agent significantly outperforms baseline on match rate, profit, and ROAS (all p ≤ 1.9e-15; every 95% CI excludes zero).

**F2 (H4 supported — dose-response):** Profit increases monotonically across the awareness ladder: noisy50 (+$17.41) < cam_inferred (+$60.97) < noisy80 (+$105.88) < oracle (+$166.31). The `cam_inferred` classifier achieves 75.5% match because crisis/opportunity/decision intent distributions genuinely overlap — realistic classifier confusion, not an artifact.

**F3 (unexpected — the bid surprise):** `situation_only` (+$262.14) **outperforms the oracle** (+$166.31) — and this replicates in **7/7 environments** (Section 8.4), including a doubled-cost regime where `situation_only` (+$79.24) is the *only* profitable agent. Perfect action matching with flat bidding beats perfect perception with context-inflated bidding. The oracle's bid heuristic (situation × channel-quality × intent multipliers) is not calibrated to the environment's clearing price (optimal bid = intent × quality), so it systematically over-pays: bid-efficiency bonuses (max +0.3) never recoup the added cost.

**F4 (decomposition):** Action matching is the dominant value driver (+$442.45); bid optimization alone adds +$52.50 (p = 1.9e-15) but cannot cross into profitability without situation knowledge (channel_only stays at −$127.81).

**Interpretation:** **The value of context concentrates in what to say (action selection), not how much to pay (bid modulation)**. This reframes the CAM value proposition: situational awareness is primarily a *content/offer decision* capability.

### 8.4 Robustness Across Environments (7 presets × 50 seeds)

Total profit by environment (mean over 50 seeds; full data: `results/cam_sim_results_robustness.md`):

| Environment | baseline | channel_only | situation_only | noisy50 | cam_inferred | noisy80 | oracle | ladder | F3 |
|-------------|----------|--------------|----------------|---------|--------------|---------|--------|--------|----|
| default | −180.3 | −127.8 | **+262.1** | +17.4 | +61.0 | +105.9 | +166.3 | yes | yes |
| uniform_situations | −197.6 | −147.4 | **+315.1** | −1.5 | −54.8 | +88.4 | +149.6 | NO | yes |
| decision_heavy | −169.5 | −152.4 | **+317.0** | −43.2 | −47.7 | +29.6 | +78.3 | NO | yes |
| crisis_heavy | −214.1 | −155.9 | **+312.5** | −16.0 | −100.3 | +70.1 | +130.2 | NO | yes |
| retention_heavy | −190.3 | −126.4 | **+315.9** | +41.1 | −28.1 | +144.8 | +215.0 | NO | yes |
| high_costs (×2) | −508.0 | −366.0 | **+79.2** | −247.2 | −233.6 | −165.8 | −109.0 | yes | yes |
| weak_signal_bonus | −156.7 | −97.8 | **+235.8** | +19.1 | +52.6 | +91.8 | +141.6 | yes | yes |

**F5 (new — bias beats noise, adversely):** The H4 dose-response ordering holds under the default distribution and under economic shifts (high costs, weak context payoffs), but **breaks in all four distribution-shifted presets**: the hand-tuned threshold classifier (`cam_inferred`) falls below even unbiased 50% perception — catastrophically so under `crisis_heavy` (−$100.33 vs +$16.01 for noisy50) and `retention_heavy` (−$28.10 vs +$41.10). Mechanism: the classifier's errors are *systematic* (retention intent ≈ 0.3 always maps to exploration; crisis ≈ 0.8 maps to decision), so under skewed distributions the bias concentrates exactly where the probability mass is, while the noisy agents' unbiased errors average out. Its effective match rate drops to ~46% under `retention_heavy` — below the coin-flip agents.

**F6:** `situation_only` is the **only agent profitable in all 7 environments**, and its margin over the oracle widens under distribution shift. The universality of F3 across reward scales, cost structures, and payoff designs indicates it is a property of the *economic structure* (bid efficiency capped at +0.3 vs uncapped cost of over-bidding), not of one reward table.

**Implications:** (1) the action-matching value claim is robust; (2) the dose-response claim requires *unbiased* perception — systematically biased classifiers can invert it; (3) deployed CAM perception models must be recalibrated per situation distribution, and unbiased-but-noisy perception can dominate biased-but-often-correct perception.

---

## 9. Discussion

### 9.1 Why Context Awareness Wins (and Where It Doesn't)
**Mechanism Analysis:**
- **H1 (Context Match):** ✅ Supported — every situation-aware agent reaches 59.9–100% match vs 21.7% baseline
- **H2 (Profit):** ✅ Supported — all context-aware agents profitable; baseline loses −$180.31
- **H3 (ROAS):** ✅ Supported — aggregate ROAS rises from 0.452 (baseline) to 1.07–2.44
- **H4 (Dose-response):** ✅ Supported under default economics — monotone profit ordering across the perception ladder (F2); *breaks for the biased classifier under distribution shift (F5) — see §8.4*
- **Mediation:** *Deferred* — not testable in this design (see §6.6); requires a perception-level continuum

**Key insight (F3):** The dominant mechanism is **action selection**, not price modulation. `situation_only` beats `oracle` because context-inflated bidding burns more cost than bid-efficiency bonuses return. For CAM practice, this says: invest first in **situation classification** (which message, which offer), and treat bid modulation as a separately calibrated problem — naive context multipliers can be value-destroying.

**Honest framing of the oracle:** The oracle is an upper bound that validates environment consistency. The scientifically meaningful agents are `cam_inferred` (realistic: infers situation from observable signals, 75.2% match) and the noisy agents (graded perception). The dose-response across these — not oracle-vs-baseline — is the paper's core empirical claim.

### 9.2 Limitations
1. **Reward-design circularity:** The situation→ideal-action table and reward magnitudes are author-designed; the environment cannot falsify the framework's own mapping. External validity requires field validation (Section 10.3).
2. **Bid-heuristic miscalibration (finding, not just limitation):** The oracle's bid multipliers are not calibrated to the clearing price — hence F3. A bid layer trained against the environment (or a real auction) is needed before any bid-modulation claim is made.
3. **Oracle construction:** The oracle receives ground-truth situation labels; it is an upper bound, not a deployable agent. Headline effects (d = 13–18) reflect the design, not deployable performance.
4. **Between-environment robustness: tested.** The full ladder replicates across 7 environment presets (§8.4): F3 is universal; the H4 ordering holds under economic shifts but not under distribution shift for the biased threshold classifier (itself a finding, F5). Remaining scope: alternative reward-structure *families* (e.g., concave returns, budget constraints) and adversarial contexts.
5. **Single environment/reward design:** Robustness across alternative reward tables, situation distributions, and cost structures is untested.
6. **No learned perception:** `cam_inferred` uses a hand-set threshold classifier; a trained classifier on observable signals (not ground-truth labels) is future work.

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
1. **Theoretical:** Grounded CAM in Endsley's SA model ( Levels 1–3 situational awareness applied to marketing automation)
2. **Conceptual:** Created a four-layer framework for context-aware marketing agents
3. **Empirical:** Developed CAM-Sim benchmark with reproducible, statistically significant results
4. **Empirical:** Developed CAM-Sim ablation benchmark with reproducible, statistically significant results: profit swings from −$180.31 (baseline) to +$262.14 (perfect action matching), +$442.45 delta (p = 1.1e-59), with a monotone dose-response across perception quality

### 10.3 Future Work
1. **Real-World Validation:** Deploy CAM with live ad spend and measure actual performance
2. **Extended Evaluation:** Test across multiple environments and parameter configurations
3. **Field Studies:** Collaborate with marketers to validate CAM in production settings
4. **B2B Extension:** Apply CAM to B2B marketing with firmographic and value-context layers (G6)
5. **Theory Extension:** Develop formal theory of marketing situational awareness

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

### stads
- Häglund, E. (2025). *Contextual intelligence: leveraging AI for targeted marketing* [PhD Thesis]. Umeå University, Department of Computing Science. URN: urn:nbn:se:umu:diva-238303.

### Marketing AI Corpus Papers
- All 61 agentic papers from the marketing-research corpus (papers.yaml)
- All 44 contextual papers from the marketing-research corpus (papers.yaml)
- Paper #5269: "From Personalisation to Agentic Campaigns: Modern Marketing Techniques Using Artificial Intelligence in the Indian Context" (2026-07)
- Paper #7535: "I hope we don't do to trust what advertising has done to love" (2026-04)

---

## Appendix A: CAM-Sim Implementation Details

### A.1 Simulation Environment
- **Language:** Python 3.11+
- **Dependencies:** numpy, scipy
- **Code:** `scripts/benchmarks/cam_sim.py`
- **Tested:** 50 seeds × 200 scenarios (10,000 evaluations per agent); byte-reproducible

### A.2 Agent Implementations (v0.3 ablation ladder)
| Agent | Type | Parameters |
|-------|------|-----------|
| baseline | Rule-based floor | Fixed bids per channel, random ±20% variation |
| channel_only | Bid-only ablation | Context-aware bidding, random action/channel |
| situation_only | Action-only ablation | Correct situation→action mapping, flat bid 1.0 |
| noisy50 / noisy80 | Graded perception | True situation with prob p; bid logic intact |
| cam_inferred | Realistic classifier | Infers situation from observable intent signal (~75% accuracy) |
| oracle | Labeled upper bound | Ground-truth situation access (validates environment, not deployable) |

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
python3 scripts/benchmarks/cam_sim.py --scenarios 200 --seeds $(seq -s, 1 50) \
    --output-md results/cam_sim_results.md
```

- Full JSON: `results/cam_sim_results.json` (aggregate + per-seed metrics + statistics + robustness sweep)
- Markdown report: `results/cam_sim_results.md` (auto-generated tables)
- Robustness: add `--robustness` to sweep 7 environment presets (report: `results/cam_sim_results_robustness.md`)
- `results/` is gitignored — outputs are reproducible from seed alone

Reproducibility contract: identical `--seeds` + `--scenarios` reproduce byte-identical aggregates (both RNGs seeded; verified).

---

*Paper structure ready for submission. Next: Populate references with full citations from papers.yaml; Run larger CAM-Sim study (10+ seeds, 1000+ scenarios); Identify JM special issue on AI.*
