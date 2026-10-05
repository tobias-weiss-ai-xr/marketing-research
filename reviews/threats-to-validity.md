# Threats to Validity Review

**Paper:** *Context-Aware Agentic Marketing: A Situational Awareness Framework for Autonomous Marketing Systems* (`paper/g4_academic_paper.md`, v0.4 draft, targeting *Journal of Marketing* / *Marketing Science*)
**Artifact under review:** the conceptual framework **CAM** and its synthetic benchmark **CAM-Sim** (`paper/cam_sim.py`)
**Framework applied:** Cook & Campbell four-category scheme — Internal, External, Construct, and Statistical Conclusion Validity
**Reviewer stance:** JM / Marketing Science causal-inference and measurement standards

---

## Summary

The paper proposes CAM, a four-layer framework mapping Endsley's (1995) three-level situational-awareness (SA) model onto autonomous marketing agents, and evaluates it in CAM-Sim, an ablation-based synthetic simulation. The headline evidence is a situational-awareness "ladder": in a 50-seed × 200-scenario design every agent acts on the same pre-generated context sequence, and profit rises from −$170.03 (context-blind baseline) to +$294.27 (perfect action matching with flat bidding) to +$530.45 (labeled oracle with mechanism-calibrated bidding). Four secondary claims are (F3/F8) uncalibrated context-inflated bidding is worse than flat bidding; (F5/F6) a systematically biased single-signal classifier can be worse than unbiased 50% perception under distribution shift, and per-distribution recalibration fixes it; (F6) match rate is not profit because error *placement* matters; and (F9) adding competitive density and channel quality to intent raises match rate from 75.7% to 98.9% and nearly closes the gap to the labeled oracle.

The paper is unusually candid and well-engineered for a simulation study: it uses paired seeds, pre-generated shared contexts, byte-reproducibility via `--self-check`, a label-free per-seed Spearman dose-response test, nine environment presets, an α-sweep, a label-noise study, and budget-pacing wrappers. Critically, it labels the oracle and `bid_calibrated` as upper bounds rather than deployable agents. Nevertheless, the study's central quantity — "situational awareness improves profit" — is partly **built into the data-generating process**, and several inferential claims are stated more strongly than the design licenses. Section 9.2 anticipates the most important threats (reward-design circularity, oracle construction, environment robustness) but frames them as "tested" rather than as residual limitations, and it omits several methodological threats that a JM/Marketing Science reviewer would raise immediately: engineered signal separability, a structurally crippled comparator, a perception/bidding confound in the dose-response, and the absence of any multiplicity or pre-registration discipline. Overall: strong as an internally coherent demonstration of a mechanism *conditional on the authors' mapping and reward table*; not yet evidence that CAM improves real marketing outcomes.

---

## Internal Validity

**Reward-design circularity (addressed, §9.2 #1 — but not resolved).** `IDEAL_ACTION` is defined as the base-reward maximizer for each situation, and `evaluate_action` then adds the `match_bonus` *only* for that same action. H1 (context-aware agents match more) and H2 (they profit more) are therefore near-tautological: the metric (`context_match`) and the payoff are both built from the author's mapping. The nine presets vary economics but hold `IDEAL_ACTION`/`SITUATION_CHANNEL` fixed, so they cannot falsify the mapping. The paper concedes this but does not run the one test that would: an **adversarial mapping** where the designer-preferred action is *not* the reward-maximizer. Until then, the causal claim "situational awareness causes profit" reduces to "following the scoring rubric scores points."

**Engineered separability of the core claim (not addressed).** `MULTISIGNAL_CENTROIDS` are set to the exact means used to generate the signals (`SITUATION_CHANNEL_QUALITY`, `SITUATION_COMPETITIVE_DENSITY`, and the intent means in `_get_intent_strength`). The hand-set `cam_multisignal` classifier is therefore given the true generative model, and its 98.9% match is the generator's Bayes rate, not an empirical result. `cam_multisignal_learned` recovers those centroids from data (98.7%), which is a genuine robustness demonstration — but from the *same* generator. Because the generator was deliberately constructed so that intent is non-diagnostic for crisis and retention while two added signals are near-perfectly diagnostic, F9 ("multi-signal awareness is the framework's core claim, confirmed") is close to a restatement of the simulation's design assumptions. A stronger test would add label noise, correlated/irrelevant signals, and signals that carry no payoff information.

**A structurally handicapped comparator inflates F5 and F9 (not addressed).** `infer_situation_from_intent` has four intent branches and can emit only EXPLORATION, CONSIDERATION, OPPORTUNITY, or DECISION — it **can never output CRISIS or RETENTION**. Its ~76% accuracy and its distribution-shift collapse are therefore partly an artifact of a classifier that is missing two of six classes, not of "intent-only inference" per se. The dramatic F5 result (intent-only *worse than coin flip* under `crisis_heavy`/`retention_heavy`) is guaranteed because the classifier systematically routes crisis→decision and retention→exploration. `cam_learned` is a fairer intent-only comparator (it can emit any class present in calibration), and it still degrades under shift (§9.2 #5), so the qualitative F5 story survives — but its magnitude and the F9 contrast are overstated by the non-emitting `cam_inferred`.

**Perception and bidding are confounded in the dose-response (partly addressed, §9.2 #2).** The "awareness ladder" mixes perception quality with bid policy: `situation_only` (100% match, flat bid) earns +$294.27, `oracle` (100% match, heuristic bid) earns +$210.00, and `bid_calibrated` (100% match, optimal bid) earns +$530.45 — the *same* perception level spans $320 of profit. The per-seed Spearman ρ(match, profit) across agents is thus not a clean dose-response; it ranks agents whose bid rules differ. A clean test would hold the action/bid policy fixed and vary only perception probability `p`.

**Paired-seed design (addressed, §7.1 — but incomplete pairing).** Contexts are generated once per seed and shared, which is genuinely strong. However, all stochastic agents draw from a single global stdlib `random` stream seeded once per seed (`random.seed(seed)`), consumed sequentially agent-by-agent. The *context* is paired, but the *decision noise* is not: each agent sees a different slice of the stream, and results depend on agent ordering. Common random numbers across agents would pair the noise as well, tightening the paired test. This is a modest but real internal-validity gap.

**Oracle and ceiling agents are not testable policies.** `bid_calibrated` is handed the reward table, cost table, competitive scale, and curvature, and grid-searches the objective the metric measures; its dominance and ROAS of 26.4 are definitional. The paper correctly flags both as upper bounds, so the *headline* causal comparison should be the noisy/classifier ladder, as §9.1 acknowledges. Good practice; the abstract should carry the same caveat rather than leading with +$530.45.

---

## External Validity

**Ecological validity of the environment (partly addressed, §9.2 #1, #4, #6).** CAM-Sim has six discrete archetypes, five channels, six actions, additive uniform signal noise, and a linear/quadratic reward table. Real marketing context is continuous, high-dimensional, non-stationary, partially observed, and often has *no ground-truth "situation" label at all*. The "oracle" concept only exists because the generator assigns a latent label; in the field, SA is inherently uncertain and the paper's own §10.3 proposes human-coded situations as a proxy. Generalization from this generator to real campaigns is asserted, not demonstrated.

**No competitive or dynamic market (acknowledged as remaining scope, §9.2 #4).** Agents act in isolation with no auctions, no clearing prices, no competitor response, no cross-episode budget reallocation, no consumer learning, and no state carryover. The `bid_calibrated` "clearing price" is a deterministic function of the context, not a market. Yet the practical implications (§9.3) speak to "the post-cookie era" and deployment — a large leap from a single-agent synthetic world.

**Hand-picked presets are not a sample (partly addressed, §9.2 #4).** Nine robustness presets give a reassuring replication but are *author-selected* configurations, not draws from a distribution of real environments. Robustness across chosen environments is not external validity; it is internal consistency across parameter settings.

**Signals are clean and the "sensing layer" is bypassed (not addressed).** In `generate_context`, `channel_quality` and `competitive_density` are supplied as exact scalars on `FullContext`, while `_generate_signals` emits a *different*, unrelated `quality_score` drawn uniformly from [0.5, 1.0] and omits competitive density entirely. The agents never use the `signals` list; they read the scalar fields directly. The hard part of the Sensing Layer — feature extraction, missingness, latency, calibration — is assumed away, and the implemented signal objects are cosmetic. Any claim about multi-modal sensing is therefore not tested.

**Outcome units are arbitrary.** Costs and rewards are uncalibrated toy units; an aggregate ROAS of 26.4 has no industry analogue. Profit *signs* may generalize, magnitudes cannot. §10.3's pre-registered field trial is the right remedy and should precede strong external claims.

---

## Construct Validity

**Situation awareness is under-represented by classification accuracy (partly acknowledged).** The benchmark measures a one-shot Level-1/Level-2 proxy (read three scalars, nearest-centroid). Endsley's Level 3 (projection) is explicitly not benchmarked (§6.6, §9.2), and the Context Predictor is specified but untested. The framework claims a three-level SA construct; the evidence covers perception and a simplified comprehension step only. A construct-validity review would demand per-level operationalizations and evidence that the classifier's errors are SA errors rather than geometry.

**Match rate is a design-relative measure, not a validated proxy (not addressed).** `context_match = (action == IDEAL_ACTION[situation])`. It measures agreement with the authors' mapping, is mechanically tied to `match_bonus` and therefore to reward, and under the skewed class distribution (exploration 35%, consideration 30%) raw accuracy is an unbalanced metric: a majority-class classifier scores non-trivially, and the 21.6% baseline floor reflects base rates. The paper should report macro-F1 and per-class recall, and should not interpret match rate as "contextual intelligence."

**Profit is the right *concept* but the operationalization is a toy (not addressed).** `profit = reward + long_term_value − cost`, with `long_term_value = reward × 0.2 × intent`. LTV is a fixed multiple of the same reward, so profit is essentially a rescaled reward minus cost — it double-counts value, has no discounting, no incrementality, no attribution, and no carryover. Profit is conceptually preferable to match rate (the paper is right to note "match rate is not profit"), but it is not a validated marketing outcome.

**The classifiers' signals are payoff inputs, not merely situation cues (not addressed).** `channel_quality` enters the bid-efficiency target (`optimal_bid = intent × quality`) and `competitive_density` enters the reward (`competitive_factor`). Multi-signal classification therefore benefits not only from *understanding the situation* but from directly exploiting variables that determine the payoff. Better "awareness" and better "reward-function knowledge" are conflated, which inflates the F9 construct claim.

**"Realistic classifier confusion" is asserted (not addressed).** The crisis↔decision and retention↔exploration conflations follow from deliberately overlapping uniform intent bands and from a threshold classifier that cannot emit those classes. Calling this "realistic" is plausible but unvalidated; no external classifier or human-coded data supports it.

---

## Statistical Conclusion Validity

**Unit of analysis and within-seed information loss (partly addressed).** Each seed collapses 200 scenarios into one mean, yielding n=50 independent observations. This is defensible, but it discards within-seed variance and provides no scenario-level mixed model (`scenario` nested in `seed`). With only 50 units and effect sizes of d≈9–35, power is not the issue — the issue is that those enormous d's are *design artifacts* of comparing an oracle to a strawman, and reporting them as substantive effect sizes is misleading. A mixed-effects or multilevel specification with scenario-level data would be more informative.

**Multiple comparisons are uncontrolled (not addressed).** The analysis runs ~13 agents × 6 metrics × 9 environments × 6 α values × 5 label-noise levels, all evaluated at α=0.05 with no familywise correction (Bonferroni, Holm, or FDR). Most comparisons are so extreme that multiplicity is not the binding constraint, but the borderline claims — the F8 reversal (p=1.8e-27), per-environment F3 tests, and the "within $3.87 of the oracle" equivalence claim — require correction or, better, a pre-specified hierarchy.

**Paired t-test assumptions are untested (not addressed).** `compute_statistics` uses `ttest_rel` on seed-level aggregates with a normal-approximation 1.96 CI and a pooled-SD Cohen's d. It reports no normality checks, no Wilcoxon signed-rank or bootstrap robustness, and uses pooled rather than difference-score d for paired data. At n=50 with skewed profit distributions, a non-parametric or bootstrap check should accompany every headline test. The 95% CIs also use 1.96 rather than the t-quantile (49 df).

**Dose-response inference conflates perception with policy (not addressed).** As noted under Internal Validity, ρ(match, profit) is computed across agents whose bid rules differ, so the rank association is not identified. The label-free improvement (per-seed ρ with a 50-replicate ranking) is a good reliability device, but ρ ∈ [0.94, 0.99] cannot separate "better perception → more profit" from "better bid calibration → more profit." A regression of profit on match rate with a bid-regime fixed effect, or a design that holds bidding fixed, is needed.

**No equivalence testing (not addressed).** "Within $4 of the oracle," "essentially matches," and "dominates every agent everywhere" are descriptive comparisons without a formal equivalence or superiority test at the specified margin. `cam_multisignal` (+$206.13) vs `cam_multisignal_learned` (+$205.39) is treated as equal without a test.

**Pre-registration and researcher degrees of freedom (partly addressed).** H1–H4 are stated as hypotheses, but F3–F9 (including the F5 distribution-shift failure, the F3 reversal, and the multi-signal finding) read as post-hoc discoveries; only the §10.3 field validation is described as pre-registered. The simulation analysis plan is not pre-registered, and the label-noise ceiling (ε≤0.3), the α grid, and the nine presets are author choices. Real-world reviewers will treat the simulation findings as exploratory until a pre-registered analysis exists.

---

## Priority Recommendations (top 5)

1. **Break the reward-design circularity.** Derive `IDEAL_ACTION`, the reward table, and the match bonus independently (theory, prior literature, or expert elicitation), and report a pre-registered **adversarial-mapping** condition in which the designer-preferred action is *not* the reward maximizer. If CAM still wins there, the causal claim is credible; if not, the current results are a consistency check, not evidence.

2. **De-confound perception from bidding in the dose-response.** Vary perception quality `p` while holding the action-*and-bid* policy fixed (e.g., all levels use flat bidding, and separately all use calibrated bidding), then estimate profit ~ match rate with a bid-regime control or a mixed model. The current ladder's 100%-match agents differ by $320, so the headline "monotone dose-response" is not identified.

3. **Repair the constructs and comparators.** Replace raw match accuracy with macro-F1 and per-class recall under the unbalanced distribution; fix `cam_inferred` so it *can* emit all six classes (or drop the claim that its failure is intrinsic to single-signal inference); wire the actual Sensing Layer (make `signals` the observable inputs, not decorative objects), add missingness/noise/latency, and benchmark the Level-3 Context Predictor if the framework is sold as a three-level SA model. Re-frame "profit" as a scaled-reward proxy, not a validated outcome.

4. **Establish external validity before making deployment claims.** Add multi-agent competition/auctions, consumer dynamics, budget reallocation, non-stationarity, and messy/unstructured signals, or at minimum soften §9.3–§10 language to "conditional on the synthetic mechanism." Treat the 9 presets as internal-consistency checks, not generalization, and make §10.3's pre-registered field trial the gate for any "deployable value" claim.

5. **Impose statistical discipline.** Pre-register the simulation analysis plan; control familywise error across the agent × environment × metric grid; use common random numbers so stochastic agents are genuinely paired; add Wilcoxon/bootstrap and t-based CIs alongside the paired t-tests; run formal equivalence tests for "within $X of the oracle"; and report a realistic range of effect sizes rather than d≈35, which will read to reviewers as a design artifact.

---

*Note: this review deliberately did not modify the paper or any code; it is confined to `reviews/threats-to-validity.md`.*
