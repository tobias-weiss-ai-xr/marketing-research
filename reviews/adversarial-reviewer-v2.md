# Second-Round Adversarial Review — Reviewer 2

**Manuscript:** *Context-Aware Agentic Marketing: A Situational Awareness Framework for Autonomous Marketing Systems* (g4_academic_paper.md, DRAFT v0.6)
**Reviewer stance:** Default REJECT, as in Round 1. I came to this round asking one question: did v0.6 *fix* the circularity, or did it *describe* the circularity more beautifully? I also re-ran the benchmark (`paper/cam_sim.py --scenarios 200 --seeds 1..50`) and ran the baseline the authors declined to run. All numbers below are my own computations from their code, unmodified.
**Venue claim:** *Journal of Marketing* / *Marketing Science*.

---

## Summary

v0.6 is a substantially more honest document than v0.5. It now dual-reports the headline (learned-vs-learned +$50.01 alongside the inflated +$101.87), concedes the 98.9% agent is the generator's decoder, cites and differentiates contextual bandits, replaces "pre-registered" with "pre-specified," and has grown a 22-item limitations section of unusual candor. The statistical machinery remains excellent and — I verified — the aggregate profits reproduce to the cent.

None of this changes the verdict, for three reasons I establish below with computation rather than rhetoric. First, the circularity is not merely acknowledged but *quantifiable*: I zeroed out the match bonus and found that **42.6–53.4% of every classifier agent's profit is a direct author payment for agreeing with the authors' own situation→action table**, with the residual advantage governed by a second copy of the same answer key hidden in `BASE_REWARDS`. Second, the manuscript's new flagship statistic — the one number repositioned to answer my Round-1 attack on the headline — **is assembled from three different contrasts and carries the wrong p-value and wrong effect size**, which I verified by regeneration. Third, the 22-limitations section, while honest, functions structurally as a shield: four open problems are relabeled "tested" because more author-designed environments were run, and the paper's own Contributions section still sells the numbers the Limitations section retracts.

The core empirical claim remains true by construction: in an environment whose reward surface the authors wrote, features the authors made separable classify better than features the authors made confusable, and the environment pays agents for agreeing. Dual reporting changed which of these numbers is quoted first. It did not change what any of them mean.

---

## Round-1-Attacks-Resolved

**Attack 1 (circularity / author-designed reward table) — ACKNOWLEDGED, NOT RESOLVED. FATAL, unchanged.**
§9.2 #1 admits it verbatim; §10.3 #3 defers the adversarial-mapping condition to future work; the nine robustness presets "hold the situation→action language fixed" (§8.4), i.e., they re-test the answer key under different fonts, exactly as I charged. My decomposition makes the charge precise: setting `match_bonus = match_penalty = 0` and re-scoring identical decisions, cam_multisignal falls +$206.13 → +$118.25 (bonus share 42.6%), cam_learned +$155.38 → +$82.69 (46.8%), cam_inferred +$104.26 → +$48.55 (53.4%). Worse, the surviving gap is still authored: `BASE_REWARDS` pays the ideal action the maximum in *every* situation (diagonal 2.0–3.0 vs. off-diagonal 0.1–1.8), so the answer key is encoded twice. H1–H4 remain unfalsifiable in this environment, as the paper itself now states.

**Attack 2 (headline = decoder reading back hand-set centroids) — PARTIALLY RESOLVED, then fumbled. MAJOR (downgraded from FATAL), with a new FATAL-adjacent defect introduced (see New-Attack 1).**
Dual reporting is real: §9.1 names cam_multisignal_learned as "the real empirical result," the abstract leads with 87.5%→98.9% learned-vs-learned, and the MAP-classifier caveat (98.9 is a lower bound, not Bayes) is a welcome correction. But the abstract still attaches the *hand-set* agent's numbers (98.9%, +$206) to the word "learned" (the learned agent is 98.7%, +$205.39), still quotes the +$102 handicapped-comparator gain one clause later, and §8.3/§9.3 still say single-signal "leaves roughly half the deployable value on the table" — the honest learned pair is +$155 vs. +$205, i.e., a quarter, not half. The inflated comparison still carries the rhetoric; the honest one rides in parentheses.

**Attack 3 (missing baselines) — CATALOGUED, NOT RESOLVED. MAJOR.**
§9.2 #13 now admits the entire gap (no logistic regression, no GBM, no RF — which the framework itself specifies — no contextual bandit, no majority floor); §10.3 #11–12 defer all of it. I ran the majority-action floor myself (always emit EDUCATIONAL, flat bid, one line of code): 35.1% match, −$15.38 profit. Honest reporting: this does *not* overturn the ladder — the constant policy is unprofitable, so the ideal-action table pays above the trivial floor. But it confirms Attack 8 quantitatively: a one-line constant policy beats the manuscript's random floor by +$155/episode, which is the artificial headroom beneath every "vs. baseline" headline delta and every d_pooled = 9–35.

**Attack 4 (novelty claim is a keyword grep; contextual bandits unengaged) — PARTIALLY RESOLVED. MAJOR (downgraded from FATAL as an ignorance charge; the substantive problem stands).**
§5.3 now carries a scope caveat naming bandits, CARS, and Dey; Li et al. (2010) and Agrawal & Goyal (2013) are cited and differentiated; the abstract flags the claim as corpus-relative. This is the right direction. But the differentiation is hand-wavy: point (2) — "bandits learn online from observed rewards; CAM-Sim evaluates offline classification against ground-truth labels" — is a confession that the benchmark tests *less* than a bandit deployment faces (no exploration cost, no feedback loop, labels free at calibration), offered as a differentiator. Point (1), the 6-way taxonomy, is a context feature any bandit consumes. The empirical comparison remains deferred (§10.3 #12). "First framework" now means "first to use our keywords in our database" — which the paper concedes needs a systematic review (#13) it did not do.

**Attack 5 (profit/ROAS are author-scaled proxies) — PARTIALLY RESOLVED. MINOR residual.**
The caveat is now attached in the abstract itself ("All profits are scaled-reward proxies, not validated currency"). Adequate. Residual gripe: "nearly doubles flat bidding (+$530 vs +$294)" and ROAS 26.4 still headline, and $530 is earned by an agent *given the mechanism* (see Attack 9).

**Attack 6 (dose-response partially mechanical; perception/bid confound) — PARTIALLY RESOLVED. MAJOR.**
F7's per-seed ρ with CIs is a genuine methodological improvement over pseudo-inferential ladder claims, and #4 admits the ladder confound with a de-confound design deferred. But "label-free" is not "mechanism-free": 42–53% of profit *is* the match payment, so ρ(match rate, profit) remains substantially x correlated with x + x/2. The abstract's "The advantage holds across nine environments (per-seed ρ ≥ 0.93)" still presents a reward-table consequence as an empirical law.

**Attack 7 (Endsley metaphor, CIM ghost, sensing decorative) — NOT RESOLVED. MAJOR.**
Level 3 still unbenchmarked (§6.6). CIM still appears exactly once in the entire manuscript (§5.4 table cell) — I grepped. And the sensing claim got *worse* on inspection: `_generate_signals` puts a `quality_score` in the signals field drawn uniform(0.5, 1.0) — uncorrelated with the situation-linked `context.channel_quality` the classifiers actually read. The implemented "Sensing Layer" emits a decoy random quality score. #6 says "decorative and unused"; accurate, and beside the point: a framework layer that actively emits misleading data is not an untested layer, it is a wrong one.

**Attack 8 (baseline strawman) — NOT RESOLVED. MAJOR.** See Attack 3: my majority-floor run shows +$155/episode of artificial headroom under the d = 9–35 headline effects. #3 admits the effects "reflect the design" and revisits nothing.

**Attack 9 (F3 is the authors' own calibration error, autopsied) — PARTIALLY ABSORBED. MAJOR.**
Adding `bid_calibrated` as an honest ceiling and the α-sweep showing the F3 flip is local are both improvements; §8.5.1's "a property of two suboptimal policies" is correct. But the finding remains what it was: the discovery that hand-set multipliers were mis-chosen against the authors' own clearing-price formula, plus a ceiling agent granted omniscience of that formula (#20 admits the omniscience; #2 nevertheless labels this "tested"). Two findings (F3/F8) and a curvature sweep spent on one's own bug is still a revision note, not a results section.

**Attack 10 (presentation) — LARGELY RESOLVED. MINOR.** "Pre-specified" fixes the registry claim. Remaining: references are still placeholders ("All 70 agentic papers ... papers.yaml") — non-citable as written and load-bearing for every corpus count; agent counts are inconsistent (abstract "eleven agents," §8.1 eleven rows, F7 a "13-agent ranking," §8.4 thirteen columns).

**Net: of ten Round-1 attacks, zero FATAL ones are resolved. Two are downgraded on honesty grounds; the rest are acknowledged, catalogued, or improved at the margins.**

---

## New-Attacks

**New-Attack 1: The repositioned headline statistic is a misassembled pastiche — verified by regeneration. MAJOR (conservative in direction; FATAL for the "no hand-typed numbers" trust claim).**
The abstract, F9, §9.1, and §9.3 all attach **(p = 2.5e-04, d_z = 0.56)** to the +$50.01 learned-vs-learned gain (cam_multisignal_learned − cam_learned). I reran the exact benchmark and computed the contrast: **p = 8.5e-32, d_z = 3.96**. The (2.5e-04, 0.56) pair belongs to an entirely different contrast — cam_multisignal − cam_multisignal_learned, a +$0.75 difference — which §9.2.1 reports correctly. The abstract's parenthetical "(+$51, p = 2.5e-04, d_z = 0.56)" additionally takes "+$51" from a *third* contrast (206.13 − 155.38 = 50.75, hand-set vs. learned single-signal; the learned pair is 50.01) and mislabels the hand-set 98.9%/+$206 as "learned." Three contrasts, one sentence, zero correct bindings — in the flagship statistic added specifically to answer Round 1, in a manuscript whose status line claims "no hand-typed numbers." The error is *understating* significance (the true effect is stronger), so I do not allege intent; I allege that the paper's one defense against Round 1 — that its numbers are auto-generated and therefore trustworthy — is falsified by its own new headline. The pipeline computes vs-baseline contrasts; this contrast was evidently assembled by hand, and botched.

**New-Attack 2: The Contributions section sells what the Limitations section retracts. MAJOR.**
Contribution 4 still claims multi-signal "closes the gap to oracle within $4" — the hand-set-agent framing §9.1 explicitly demotes, and §9.2.1 shows the $3.87 gap is itself significant (p = 1.3e-13). Contribution 5 still markets "Bootstrap BCa CIs (200 resamples) confirm normal-approximation CIs within $1.4" — which #15 calls underpowered and mis-targeted (it resamples marginal means, not the paired contrasts that carry every inferential claim; the abstract nonetheless says results are "confirmed by bootstrap BCa CIs"). A paper cannot simultaneously cite §9.2 #n as its conscience and quote the unconscioned number in §10.2.

**New-Attack 3: The "tested" limitation labels reclassify open problems as closed. MAJOR (this answers the question: the 22 limitations are honest *and* a defense mechanism).**
#2 "Bid-layer calibration: **tested**" — by an agent *given* the mechanism, which #20 then calls "an omniscience no practitioner has." #7 "Between-environment robustness: **tested**, but author-selected" — running nine more configurations of one's own environment is internal consistency, as #7 itself concedes in its final clause; the label contradicts its own sentence. #8 and #9 follow the pattern. The confessional mode has a strategic function: every Round-2 attack can be pre-answered with "we disclosed this (§9.2 #n)" — disclosure substituting for remedy. Several disclosed-but-unfixed items are an afternoon of work: the majority floor was one line (I ran it); the matched-family ablation (NCC on intent-only) and macro-F1 reporting are a day. That they remain future work while 2,500 words were spent describing them is a choice, not a constraint.

**New-Attack 4: F5/F6 as "novel findings" — textbook drift management. MINOR.**
"Systematic bias under distribution shift is worse than unbiased noise, and per-distribution recalibration fixes it" is concept-drift 101 (known in ML under domain adaptation for two decades). Same for F6's "match rate is not profit." Presenting standard practice as empirical findings 2 and 3 of a four-finding contributions list inflates the contribution count.

**New-Attack 5: The implemented Sensing Layer emits a decoy signal. MAJOR (sharpens #6).** A uniform-random `quality_score` in the signals field, uncorrelated with the real `channel_quality`. Claims about multi-modal *sensing* are not merely untested; the implemented layer would mislead any agent that trusted it.

**New-Attack 6: Robustness results are asymmetrically narrative. MINOR.**
F9's "universal across 9 environments" claim is still argued from cam_multisignal vs. cam_inferred (the handicapped comparator) rather than the learned-vs-learned pair the paper declares fair. The fair per-environment comparison is computable from the paper's own Table (§8.4, cam_ms_recal vs. cam_recal: +$127.8 uniform, +$114.6 crisis, +$72.5 retention) and is large — so why is the abstract's universal claim not made on it? Because +$51 with d_z = 0.56 (as mis-reported) reads weaker than +$102. The honest comparison is available, stronger than the quoted default-environment effect, and unused.

---

## Severity-Table

| # | Issue | Round-1 status | Severity (v0.6) |
|---|-------|----------------|-----------------|
| 1 | Reward-surface circularity (match bonus 42–53% of profit; BASE_REWARDS diagonal = second answer key) | Acknowledged (#1), deferred (§10.3 #3) | **FATAL** |
| 2 | Designed feature-separability + classifier family = generative family; "multi-signal wins" is true by construction | Admitted (#13–14) | **FATAL** (as awareness claim) / MAJOR (as environment diagnostic) |
| 3 | Headline statistic misassembly: p/d_z from wrong contrast, "+$51" from a third, "learned" label on hand-set numbers | **NEW** | **MAJOR** |
| 4 | Contributions section contradicts Limitations (within-$4; B=200 bootstrap) | **NEW** | **MAJOR** |
| 5 | "Tested" labels relabel open problems as closed; limitations as shield | **NEW** | **MAJOR** |
| 6 | Missing baselines (bandit, logreg/GBM/RF, matched-family NCC); majority floor only now run (by me) | Admitted (#13), deferred | **MAJOR** |
| 7 | Novelty = keyword grep in own corpus; bandit differentiation is a confession | Caveated, not substantiated | **MAJOR** |
| 8 | ρ dose-response partially mechanical (bonus in profit); perception/bid confound | Improved (F7), confound deferred | **MAJOR** |
| 9 | Endsley metaphor; CIM single table cell; sensing layer emits decoy signal | Unchanged; decoy **NEW** | **MAJOR** |
| 10 | Baseline strawman (+$155/episode artificial headroom, measured) | Admitted (#3) | **MAJOR** |
| 11 | F3/F8 = autopsy of authors' own miscalibration; omniscient ceiling agent | Partially absorbed | **MAJOR** |
| 12 | Profit/ROAS unitless proxies still headline rhetoric ("roughly half") | Caveated | **MINOR** |
| 13 | References placeholders; agent-count inconsistencies | Unchanged | **MINOR** (collectively MAJOR) |
| 14 | F5/F6 presented as novel findings (textbook drift management) | **NEW** | **MINOR** |
| 15 | Bootstrap B = 200, marginal not paired | Admitted (#15) | **MINOR** |
| 16 | No field/experimental evidence at JM/Marketing Science bar | Design promised (§10.3 #1) | **FATAL** (for this venue) |

---

## What-Would-Change-My-Mind

1. **Break the answer key, not just disclose it.** Run the adversarial-mapping condition (§10.3 #3) with a reward table sourced independently of the authors (expert panel or revealed preference), and show multi-signal classification still pays. One week of compute answers the FATAL issue; nothing else in the paper does.
2. **Re-source the economics.** Even partially: calibrate the reward table and LTV multiple against published campaign benchmarks, or strip all dollar/ROAS figures from headline claims.
3. **Fix the headline statistic and the abstract binding.** Correct (p, d_z) on the learned-vs-learned contrast; make every quoted number in the abstract come from the agents the sentence names. Re-audit §10.2 against §9.2 so Contributions stop selling retracted numbers.
4. **Run the matched-family ablation and one bandit.** NCC-on-intent vs. NCC-on-3-signals, plus ε-greedy on the same signals, plus macro-F1. If multi-signal still wins against a learning policy that pays exploration costs, the claim finally has content. My majority-floor run shows the authors how cheap baselines are to add; it did not embarrass them, which is exactly why they should run it themselves.
5. **Deliver any field pilot** registered in an actual registry. For this venue tier, even a small pre-specified A/B with a match-rate audit against human-coded situations would move the paper from self-referential to falsifiable.
6. **Make the sensing layer honest:** either implement noisy/missing/decoy-free signals and test perception under them, or delete sensing claims from the framework.

---

## VERDICT

**REJECT** (closer than Round 1; a major-revision outcome would be defensible at a simulation/benchmark venue, not at the claimed one).

**Justification.** The manuscript answered Round 1 with candor rather than evidence. The single FATAL defect — an environment that pays agents for agreeing with its authors — is not only unresolved but, on my decomposition, worse than Round 1 alleged: the answer key is encoded twice (a direct match bonus worth 42–53% of classifier profit, and a base-reward diagonal that pays the ideal action in every situation), so even the honestly-reported learned-vs-learned contrast measures the authors' feature-design choices, not a property of marketing. The dual reporting that was supposed to fix the headline instead produced a flagship statistic stitched from three different contrasts with the wrong p-value and effect size attached — verified by my regeneration — which falsifies the manuscript's only remaining structural defense ("no hand-typed numbers"). The 22 limitations are honest, and that is the problem: honesty has been substituted for remedy, with open defects relabeled "tested" and the Contributions section still trading on numbers the Limitations section has retracted. What survives is a well-engineered, genuinely reproducible toy (my rerun matched every aggregate to the cent) demonstrating that more-informative features classify better on separable synthetic data — an information-theoretic banality wrapped in a framework whose novel layers are untested (Level 3), unmeasured (CIM), or misleading as implemented (the sensing decoy). At *Journal of Marketing* or *Marketing Science*, where field evidence or validated measurement is the entry price, this is not close. The adversarial-mapping condition, an independently-sourced reward table, matched-family and bandit baselines, and one registered field pilot would make this a publishable benchmark paper somewhere. I would read that paper with interest; this version of this paper, I cannot accept.
