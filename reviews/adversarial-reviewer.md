# Adversarial Review — Reviewer 2

**Manuscript:** *Context-Aware Agentic Marketing: A Situational Awareness Framework for Autonomous Marketing Systems* (g4_academic_paper.md, DRAFT v0.5)
**Reviewer stance:** Default REJECT. Simulation-only papers can be valuable; self-confirming simulations are not. My working hypothesis, which the manuscript repeatedly fails to displace, is that this one rewards the authors' own design choices and reports the reward as a finding.
**Venue claim:** *Journal of Marketing* / *Marketing Science* — I evaluate against that bar.

---

## Summary

The authors propose CAM, a four-layer framework mapping Endsley's situational-awareness levels onto marketing agents, and evaluate eleven agents in a synthetic simulation (CAM-Sim) in which a hand-authored reward table pays agents for selecting the authors' "ideal" action per situation. The headline result is that a three-signal classifier (98.9% match, +$206) beats a single-signal classifier (75.7%, +$104) and nearly matches a ground-truth oracle. The statistical machinery (paired seeds, bootstrap BCa, seed convergence, multiplicity correction) is unusually careful, and the limitations section is disarmingly honest — the manuscript *knows* its headline number "is the generator's Bayes rate, not an empirical classifier result" (§9.1). Honest self-diagnosis, however, is not a substitute for a study that can falsify its central claim. What remains after removing the circular and tautological pieces is a modest, well-known point: classifiers with more informative features are more accurate on separable synthetic data. That is an information-theoretic banality, not a *Journal of Marketing* contribution.

---

## Attack-1: The hypothesis is circular — the simulation rewards exactly what the framework prescribes

**Stated attack.** H1–H4 are "supported" in an environment whose scoring function was written by the same authors who wrote the hypotheses, using the same situation→action mapping (`IDEAL_ACTION`) that CAM's Action Layer prescribes (paper §6.5 table = `IDEAL_ACTION` in cam_sim.py). An agent scores well by *reading the authors' answer key*: `context_match = (action == IDEAL_ACTION[situation])` and a ±0.5/−0.3 match bonus is added to reward by construction. Confirming "context-aware agents outperform" here is logically equivalent to confirming that students who copy the teacher's answer key score higher. The manuscript's own future-work list concedes the experiment that would break the circle has not been run: an "adversarial-mapping condition — in which the designer-preferred action is *not* the reward maximizer — would separate 'CAM wins' from 'following the scoring rubric scores points'" (§9.2 #1, deferred to §10.3.3).

**Evidence-From-Paper.** §9.2 #1 admits the circularity verbatim ("the environment cannot falsify the framework's own mapping"). cam_sim.py's environment-preset comment claims the 9 presets "address reward-design circularity" — but the same comment states the "situation→ideal-action LANGUAGE is held fixed across environments." Varying the economics *around* an unfalsified mapping does not test the mapping; it re-tests the same answer key under different fonts.

**Does-The-Paper-Defend-It?** No. It acknowledges and defers. Acknowledgment with deferral leaves the core empirical contribution unfalsifiable as published.

**Severity: FATAL.**

## Attack-2: The headline 98.9% is the answer handed back, not an answer discovered

**Stated attack.** `cam_multisignal`, the agent carrying the abstract's flagship number, classifies by nearest-centroid against `MULTISIGNAL_CENTROIDS` — which are, digit for digit, the true generative means (`SITUATION_*_QUALITY`/`DENSITY` values, cam_sim.py lines 177–203). This is not a classifier; it is the generator's decoder with noise on top. The paper admits it: "its 98.9% match is the generator's Bayes rate, not an empirical classifier result — the learned variant (98.7%) is the real evidence" (§9.1). Yet the abstract, F9, and the conclusion all lead with 98.9%/$206. Worse, the fallback "real evidence" is itself structurally privileged: the classes are generated as equal-width (±0.15) clusters around well-separated centroids in 3-D, and *nearest-centroid is the Bayes-optimal classifier for exactly that generative family*. `cam_multisignal_learned` recovers 98.7% because the classifier family is the generative family. Calling this "recovering the true signal structure from data alone" (F9) is celebrating a tautology. The signal separation (e.g., centroid spacing 0.2–0.4 with 0.3-wide noise support, comfortably disjoint) makes the task trivially separable; any competent classifier would do this.

**Evidence-From-Paper.** §9.1 (Bayes-rate admission); §7.1 agent list ("hand-set situation centroids, 98.9% match"); §9.2 #5 shows the authors already know how a handicapped comparator inflates a claim (they concede `cam_inferred`'s 75.7% is partly a missing-class artifact) — the same logic applies to a *favored* agent seeded with the truth.

**Does-The-Paper-Defend-It?** Partially and inconsistently: the admission exists (§9.1), but every headline deployment of the number (Abstract, F2, F9, §10.1) ignores it. The abstract's "raises match from 75.7% to 98.9%" is, on the paper's own account, a comparison of a genuinely handicapped classifier against a decoder.

**Severity: FATAL (for the headline claim as framed).**

## Attack-3: Missing baselines — no trained ML comparator, no majority-action floor, no contextual bandit

**Stated attack.** Where is logistic regression, a gradient-boosted tree, or a random forest on the same three signals? The framework itself *specifies* RandomForest and LSTM components (§6.4) — then the simulation benchmarks nearest-centroid and threshold rules (§6.4 implementation note). The paper tests a caricature of its own architecture. A nearest-centroid agent on trivially separable synthetic data tells us nothing about "multi-signal *awareness*"; it tells us that three features beat one feature on a task the authors made three-feature-solvable (crisis density 0.8 vs decision 0.6 is an author's keystroke, not a market fact — set them equal and F9 evaporates). Similarly absent: an always-majority-action baseline (exploration is 35% of the default distribution; always-EDUCATIONAL is free, trainable in one line, and profitable — I cannot verify it would beat baseline only because it was never run), and any exploration/exploitation agent (ε-greedy, LinUCB, Thompson sampling). Contextual bandits are the canonical "context-aware marketing agent" and are absent from both the agent ladder and the references.

**Evidence-From-Paper.** §6.4 (RF/LSTM specified, "simplified surrogates" substituted); §7.1 (full agent list — no statistical-learner or bandit agent); §9.2 #11 (admits a majority-class classifier "would score non-trivially" — noted, never measured).

**Does-The-Paper-Defend-It?** No. The implementation note defends the substitution as "isolating the value of signal structure without conflating it with classifier capacity" — but classifier capacity is precisely what practitioners must buy, and its omission is why the result reads as a toy.

**Severity: FATAL (as an empirical claim about awareness); MAJOR if reframed as environment diagnostics.**

## Attack-4: The "zero papers" novelty claim is a keyword artifact; entire adjacent literatures are unengaged

**Stated attack.** "First framework connecting agentic AI with marketing situational awareness" rests on counting title/abstract keyword co-occurrences ("agentic" AND "contextual"/"situational") inside the authors' own self-curated 9,994-paper corpus (§5.1–5.3). This is not a literature review; it is a grep. Terms absent from the query design — *context-aware*, *contextual AI*, *situation-aware*, *pervasive computing*, *contextual recommender* — name decades of directly relevant work: context-aware computing since Dey (2001), context-aware recommender systems (Adomavicius & Tuzhilin), and above all **contextual bandits**, which are literally autonomous agents selecting marketing actions from context signals, with a mature theory and production deployments at every major ad platform. Not one contextual-bandit citation appears in the references. Claiming first-mover status in a field that has shipped contextual bandits for a decade is, at a top journal, a desk-reject-grade error. The corpus counts (70 agentic, 1.8× burst) inherit the same fragility: they are functions of the authors' query strings in taxonomy.yaml, not of the field.

**Evidence-From-Paper.** §5.1 definition ("mention 'agentic' in title/abstract"); §5.3 (the single co-mention dismissed as "superficial"); References section (zero bandit/CARS/pervasive-computing entries; corpus papers cited as bulk placeholders "All 70 agentic papers ... papers.yaml").

**Does-The-Paper-Defend-It?** No. §5.4 differentiates only Häglund (2025), a thesis. The differentiation table does not mention the literatures that actually occupy the claimed white space.

**Severity: FATAL (for the "first framework" positioning); MAJOR if the claim is rewritten as "no papers use our exact keywords."**

## Attack-5: Profit and ROAS are author-scaled proxies with no external calibration

**Stated attack.** "Profit" = reward + LTV − cost, where LTV = reward × 0.2 × intent (cam_sim.py line 881) — the same reward variable, re-counted at a fixed multiple. The metric is reward wearing a dollar sign. ROAS 26.4 for `bid_calibrated` has no industry analogue (paid-media ROAS typically 2–10×), and the agent achieves it by *knowing the mechanism* — reward table, clearing-price formula, curvature — i.e., it is the environment's own optimizer reported as an agent. The paper concedes magnitudes "have no industry analogue" (§9.2 #12) while the abstract still headlines "+$206 vs +$104," "$530 vs $294," and "26.4." Every dollar figure in the paper is an author-chosen constant in disguise (base rewards, ±0.5/−0.3 bonuses, ×0.2 LTV multiple, competitive discount ×0.5).

**Evidence-From-Paper.** §9.2 #12 (full admission); §7.1 (`bid_calibrated` "knows reward table, bonuses, costs, curvature"); §8.1 (ROAS 26.367).

**Does-The-Paper-Defend-It?** Partially — the caveat exists, but the headline framing (abstract, practical implications §9.3: "nearly doubles deployable profit") trades on the uncaveated numbers.

**Severity: MAJOR.**

## Attack-6: The dose-response is partially mechanical, and the ladder confounds perception with bidding

**Stated attack.** H4's per-seed Spearman ρ(match rate, profit) ≥ 0.93 is presented as the crown-jewel robustness result. But profit *contains* the ±0.5/−0.3 match bonus, and match rate is defined by the same mapping that triggers the bonus. Agents that match more mechanically collect more bonus; correlating the two is close to correlating x with x + x/2. The residual signal (error *placement*, F6) is real but is a property of the authors' reward asymmetries, again. Separately, §9.2 #4 concedes the ladder mixes perception quality with bid policy (the three 100%-match agents span $320), so the headline ladder ordering (F2) is not a dose-response in perception at all — yet it anchors the abstract.

**Evidence-From-Paper.** §9.2 #4 (confound admitted); §6.6 ("A mediation design requires a continuum of perception levels — future work"); F7 itself ("Match rate is not profit" — correct, and equally an indictment of using ρ as the headline).

**Does-The-Paper-Defend-It?** Partially — F7's label-free framing and the deferral of a clean p-continuum design are honest, but the abstract still sells the confounded ladder ("from intent-only 75.7%... to a labeled oracle").

**Severity: MAJOR.**

## Attack-7: Construct validity — Endsley is a metaphor, CIM is a ghost, and the Sensing Layer is decorative

**Stated attack.** The "theoretical grounding" is a relabeling table: Endsley's Level 1/2/3 become Sensing/Model/Engine. Endsley's construct concerns human perception in dynamic systems, with a validated measurement tradition (SAGAT); nothing here is measured, predicted, or validated as SA — Level 3 (Projection) is "specified but NOT benchmarked" (§6.6), i.e., the most distinctive part of the theory is untested. The paper's own construct, "Contextual Intelligence in Marketing (CIM)," appears exactly once (§5.4 table) and is never defined, operationalized, or measured — a construct introduced solely to fill a differentiation-table cell. Meanwhile §9.2 #6 concedes the *sensing* claim is untested: `channel_quality` and `competitive_density` are handed to agents as exact scalars, and the signals field "is decorative and unused." A framework whose three novel layers are (a) metaphor, (b) unmeasured, (c) untested is a diagram, not a theory.

**Evidence-From-Paper.** §4.1 (the relabeling table); §5.4 (CIM's sole appearance); §9.2 #6 (signals supplied, not sensed); §6.6 (Level 3 not benchmarked).

**Does-The-Paper-Defend-It?** The scope note (§6.6) and limitation #6 are candid about what is not tested; candor does not convert untested layers into contributions.

**Severity: MAJOR.**

## Attack-8: The baseline is an engineered strawman

**Stated attack.** The floor agent picks channels uniformly at random and bids 0.1–2.5 against an optimal bid of intent×quality (typically ≪1), guaranteeing bid-efficiency penalties and negative profit. Its 21.6% match rate is exactly the combinatorial consequence of a fixed channel→action table (0.4×0.35 + 0.4×0.15 + 0.2×0.10). The paper then reports d_pooled = 9–35 against this floor — effect sizes that should have prompted the question "why is my comparator losing $170 by construction?" rather than "how significant is my win?" Every headline p-value (5.4e-46, 3.3e-70) measures distance from a doormat. A paper about the value of context needs the *strongest* realistic context-blind policy (e.g., a tuned flat-bid best-fixed-action agent), not the weakest.

**Evidence-From-Paper.** §8.1 (baseline row); §9.2 #3 ("Headline effects (d_pooled = 9–35) reflect the design"); A.2 (baseline "Rule-based floor").

**Does-The-Paper-Defend-It?** No — limitation #3 admits the effects "reflect the design" without revisiting whom the comparisons flatter.

**Severity: MAJOR.**

## Attack-9: F3, the "bid surprise," is a finding about the authors' own typo

**Stated attack.** The celebrated non-obvious result — situation_only (+$294) beats the oracle (+$210), "miscalibrated bidding is worse than none" — is the discovery that *the authors' own hand-set* `SITUATION_MULTIPLIERS` and interpolation tables were mis-chosen relative to *the authors' own* clearing-price formula. The paper then repairs it with `bid_calibrated` (+$530), an agent granted the mechanism. So the arc is: author writes a bad heuristic, calls it "oracle," finds flat bidding beats it, diagnoses the bug, writes the optimal policy by construction, and reports both the bug and its fix as two novel findings (F3/F8 and the calibrated ceiling). In any real review cycle, this is a revision note, not a results section. §8.5.1's α-sweep analyzing the "non-monotone ordering" of two suboptimal author-written policies is epicyclic: the finding under analysis is an artifact of the authors' constants.

**Evidence-From-Paper.** §7.1 (oracle's hand-set multipliers; `bid_calibrated` "knows reward table, bonuses, costs, curvature"); F3 (the "surprise"); §8.5.1 ("a property of two suboptimal policies" — the manuscript says it itself).

**Does-The-Paper-Defend-It?** The "two suboptimal policies" admission defuses the *interpretation* but not the decision to spend three findings and a curvature sweep on autopsying one's own calibration error.

**Severity: MAJOR.**

## Attack-10: Presentation and positioning failures

**Stated attack.** (a) The field-validation design is called "pre-registered" (Abstract, §10.3) with no registry, no registration number, and no date — it is a *plan*. (b) References are placeholders ("REFS from corpus"; "All 70 agentic papers ... papers.yaml") — non-citable as written. (c) §9.2.1's "equivalence" discussion correctly retreats from "within $4" language, yet the abstract retains it. (d) Bootstrap BCa with 200 resamples is thin; convention is ≥1,000–10,000 (minor, given the tiny BCa/normal discrepancies). (e) Venue fit: JM and Marketing Science expect field data or a theory contribution with measurement; a synthetic benchmark with unitless currency and a grep-based gap claim meets neither bar.

**Evidence-From-Paper.** Abstract ("pre-registered field-validation design"); §4.3 "(REFS from corpus)"; §9.2.1 vs Abstract; §9.2.2 (200 resamples).

**Does-The-Paper-Defend-It?** No; these are fixable presentation defects, but they signal a manuscript submitted before its evidence matured.

**Severity: MINOR individually; collectively MAJOR.**

---

## What-Would-Change-My-Mind

1. **Run the adversarial-mapping condition** (§10.3.3) and show CAM wins when the designer's preference is *not* the reward maximizer — with an independently sourced reward table (expert panels, revealed-preference field data), not author constants.
2. **Replace the headline number**: drop the hand-set-centroid agent entirely; lead with learned classifiers, and add logistic regression, gradient boosting, the framework's own RandomForest, an always-majority-action floor, and a contextual bandit (LinUCB or ε-greedy) on identical signals. If multi-signal structure still wins under bandit exploration costs, the claim gains content.
3. **Break the classifier-family = generative-family symmetry**: generate data from a process the model class does not mirror (heteroscedastic, dependent, mixed-type signals; realistic feature noise, missingness, latency — i.e., actually *sense* something, per §9.2 #6).
4. **Substantiate the gap claim** with a systematic review that queries the synonym space (context-aware, contextual bandits, CARS, pervasive marketing) and explicitly positions against contextual bandits; or narrow the claim to the keyword finding it actually is.
5. **Anchor the money**: map synthetic reward to a calibrated currency (real CPMs/conversion values) and report sensitivity to the LTV multiple, or strip dollar signs and ROAS from the abstract.
6. **Deliver the field trial** — even a pilot A/B with the pre-registered design actually registered — and reposition as a framework-plus-field-evidence paper for this venue tier.

None of these is satisfied by the current draft; several are the paper's own listed future work, which is the problem: the manuscript's strongest defenses are promises.

---

## VERDICT

**REJECT.** — The simulation rewards the authors' own answer key, the headline result is the answer key read back at 98.9%, and the "first framework" claim is unseated by an unengaged contextual-bandit literature, so what survives scrutiny is a triviality dressed in impeccable statistics.
