# Domain-Expert Review, Round 3: CAM / CAM-Sim v0.7

**Reviewer profile:** Same reviewer as rounds 1–2 (`reviews/domain-expert.md`, `reviews/domain-expert-v2.md`) — 15 years in programmatic buying and demand-side platforms (Google Ads, DV360, Meta, LinkedIn, The Trade Desk). Third-round review of v0.7, written after the authors responded to the round-2 four-viewpoint review.

**Scope:** `paper/g4_academic_paper.md` (v0.7). I did not re-run the simulation; I assess whether the round-2 practitioner concerns are addressed, whether the transferable core is now isolated, and whether I would put my name on the field trial.

---

## Summary

v0.7 is the first revision that **closes the loop with this reviewer rather than merely conceding**. Every item the task lists as addressed is genuinely addressed, and two of them — the privacy claim and the F9 framing — are fixed in exactly the form round 2 requested.

The privacy-safe claim is deleted. In its place §9.3 now says the intent scalar "behaves like fully-observed identified-user intent, which cookieless environments remove," and that privacy-safe deployment requires signal-level differential privacy or on-device inference (§9.2 #6, #20). That is the right correction: it removes the one internally inconsistent claim in v0.6 and replaces it with the open problem a practitioner actually faces. The crisis→2.0× objection — raised in round 1, ignored in v0.6 — is now limitation #23 plus future work #17. The decoy `quality_score` signal is now #24 plus #18. F9's universality is explicitly relabeled "on the handicapped comparator" in F9, in contribution 4, and in §9.1's oracle framing. H4's dose-response is caveated as "partly mechanical … an environment-consistency check," and the bootstrap is demoted from confirmatory to diagnostic.

One correction deserves credit: the learned-vs-learned effect size. v0.6 reported the fair +$51 comparison as p = 2.5e-04, d_z = 0.56; v0.7 reports +$50.01, p = 8.5e-32, d_z = 3.96, 95% CI [+$46.4, +$53.6]. The corrected value is internally consistent with the direct cam_multisignal − cam_inferred contrast (+$101.87, d_z = 7.88): the d_z ratio 3.96/7.88 = 0.50 matches the effect ratio 50.01/101.87 = 0.49. The fair comparison is therefore statistically robust, not marginal. As a practitioner I note the *dollar* magnitude is unchanged (~+32% relative to `cam_learned`'s +$155), so this corrects the confidence, not the business case.

## Round-2-Concerns-Addressed

1. **Privacy-safe claim (round 2: "one step backward") — ADDRESSED, fully.** Deleted as a claim; rewritten as a caveat and an open requirement. No residual.
2. **Crisis 2.0× multiplier backwards (un-adopted in rounds 1–2) — ADDRESSED as documentation (#23, #17), NOT as behavior.** This is my main remaining objection to the artifact. The Action Layer still hardcodes 2.0× for `crisis` (§6.5), and §10.3 #1 proposes to deploy "exactly the `cam_multisignal_recalibrated` pipeline" as Arm A. An honest limitation does not make an incident-generating default safe to ship into a live arm. It must be replaced with pause/exclude before launch, not deferred.
3. **Sensing-layer decoy signal — ADDRESSED as documentation (#24, #18).** Correct and specific. The paper now says the multi-modal claim is about the classifier on the three real signals, not the sensing infrastructure. Good; still a sim-only statement.
4. **F9 universality on a handicapped comparator — ADDRESSED.** The language is now consistent across abstract, F9, §9.1, §9.3, and contribution 4. The learned-vs-learned per-environment gap is explicitly deferred (§10.3 #11).
5. **Transferable findings preserved with honest caveats — ADDRESSED.** H4 mechanical-ρ caveat, bootstrap demotion, corrected #14 (NCC is Bayes-optimal only in the isotropic/equal-prior case), and the new #19 majority-action floor all improve the honest core.

**What did not change:** the round-2 "What-Is-Still-Missing" list is almost entirely still missing. The limitation list grew by exactly the two items named in the task (#23, #24). Label provenance in production, delayed/censored/attributed feedback, cross-device identity resolution, and the B2B dark funnel are still absent from #1–24. These are pre-existing structural gaps a framework paper may legitimately defer — but they are the same gaps that govern whether Arm A is runnable, so they return below.

## What-Still-Transfers

After the corrections, my round-2 transfer list stands, with the F9 entry upgraded on confidence:

1. **Multi-signal beats single-signal (F9) — transfers, now on a statistically strong foot.** The mechanism is what practitioners recognize: intent alone conflates crisis↔decision and retention↔exploration; competitive density and channel quality resolve exactly those. That is why the ABM stack (Bombora, 6sense, Demandbase) layers surge, technographic, and contextual signals on behavioral scoring. The honest magnitude remains bounded (~+$50/proxy-episode), which matches industry experience — enrichment is worth real but not transformative money.
2. **Miscalibrated bid modulation is worse than none (F3) — transfers**, defended on the industry's own automated-bidding migration rather than the toy auction.
3. **Systematic bias under distribution shift beats random noise, adversely (F5/F6) — transfers.** Every decaying static lead-scoring model proves it; per-distribution recalibration is standard MLOps hygiene.
4. **Error placement > error count (F6) — transfers and is under-modeled by vendors.** The `uniform_situations` result (higher match, negative profit vs noisy50) is the clean demonstration.
5. **Sequencing: classification before bid modulation — defensible as strategy.**

Correctly non-transferable: the +$102 handicapped headline as a business number, the +$530 calibrated ceiling (omniscience artifact), all magnitudes/ROAS, and multi-signal magnitudes under uniform label noise.

## Practitioner-Verdict

**Is the transferable core now clearly identified? Yes — this is the round's biggest improvement.** §9.1's oracle framing, the learned-vs-learned comparator, and the consistent "handicapped comparator" label make it unambiguous which findings a practitioner is allowed to carry. The abstract still leads with match-rate percentages and still presents +$102 as the larger gain, but it presents the fair +$50 first and §9.3 labels the +$104 comparator as handicapped, so a careful reader cannot be misled. I would no longer call the match-rate demotion "rhetorical only": the H4 caveat and the environment-consistency reframe are analytic changes.

**What practitioner issues remain:**
- **Sim unit ≠ field unit.** CAM-Sim models one decision per scenario; the §10.3 #1 endpoint is per-campaign account-level uplift. B2B outcomes are decided by 6–10 stakeholders per account (#19), and account-level aggregation is deferred (#15). The trial would measure a quantity the simulation does not model.
- **Label provenance.** The recalibration remedy (`cam_multisignal_recalibrated`) needs 2,000 labeled samples per distribution *before* deployment, yet #22 concedes there is no ground-truth situation label in production. The trial's secondary endpoint is "human-coded situations," with no coder count, agreement threshold, throughput, or cost. This is the precondition for Arm A feasibility and it is unaddressed.
- **Incrementality.** #12 concedes no incrementality in the reward; the trial's primary endpoint is between-arm uplift, with no within-Arm-A holdout. Observed conversions are not incremental conversions, and I asked for this in round 2.
- **Field signal acquisition.** The three real signals are exact real-time scalars in the sim and delayed, censored, or buyer-side-invisible in practice (competitive density via Auction Insights is aggregated and delayed; open-exchange RTB shows no participants; intent is the privacy-limited scalar). The design does not say how Arm A obtains them, at what latency, cost, or coverage, nor what happens on a miss.
- **Crisis default shipping into Arm A** (above).
- **Arm A's bid policy is unspecified.** "The `cam_multisignal_recalibrated` pipeline" implies a bid layer; whether it is flat (F3-safe) or context-multiplied (F3-harmful) is not stated. It must be flat, or the trial conflates classification with a known-bad bid policy.

## Trial-Feasibility

Section 10.3 item 1 is **credible in shape and not yet executable.** The two-arm, campaign-random-effect, ≥40-campaigns-per-arm, 8–12-week, pre-specified design is the field analogue of the paired-seed sim and is the correct skeleton. It is also unchanged from v0.6 and still lacks the two amendments I requested in round 2 — an incrementality holdout inside Arm A and an explicit labeling protocol — plus two that round 3 makes unavoidable: a crisis-default guardrail and a signal-acquisition specification (including a missing-intent fallback).

Two design risks are worth stating plainly. First, 8–12 weeks may be shorter than a B2B sales cycle, so campaign-level conversions observed in-window are immature and the feedback-latency gap becomes a bias, not a noise term. Second, 40 campaigns per arm with campaign as random effect gives limited power in a high-variance, low-frequency B2B outcome space; the sim's power comes from 10,000 paired decision-level observations, which the trial cannot replicate at campaign level.

**Would I sign off on running it? Conditional yes.** I would fund and run the trial conditional on five changes before launch: (a) a written labeling protocol (coders, agreement threshold, per-label cost) and pre-launch recalibration labels; (b) a within-Arm-A incrementality holdout; (c) replacing crisis-2.0× with pause/exclude in the Arm A action mapper; (d) a signal-acquisition spec with availability/latency/cost and a missing-intent fallback; (e) specifying Arm A's bid policy as flat and fixing the measurement window against the actual sales cycle. None of these is a research risk; all are protocol hygiene. That is a materially stronger position than my round-2 "would actually sign off on running it," which was itself qualified.

## VERDICT

**PARTIALLY — with a conditional sign-off on the field trial, and a clear upgrade from round 2.** v0.7 addresses all five round-2 practitioner concerns in the terms requested: the privacy-safe claim is gone, the crisis and sensing-layer objections are now on the record as #23/#24 and #17/#18, F9 is honestly scoped to the handicapped comparator, and the transferable core is cleanly isolated and correctly caveated. The corrected learned-vs-learned effect size legitimately strengthens F9's fair comparison. The paper still maps to practice as validated heuristics plus a credible trial design, not as a deployable DSP artifact, and the residual gaps (label provenance, incrementality, field signal acquisition, the still-hardcoded crisis multiplier, the unchanged trial protocol) are real. But the direction and the honesty are now right, and the field trial at §10.3 #1 is the first concrete experiment in this line of work I would put my operational weight behind — conditional on the five protocol changes above.
