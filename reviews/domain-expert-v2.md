# Domain-Expert Review, Round 2: CAM / CAM-Sim v0.6

**Reviewer profile:** Same reviewer as round 1 (`reviews/domain-expert.md`) — 15 years in programmatic buying and demand-side platforms (Google Ads, DV360, Meta, LinkedIn, The Trade Desk). This is a second-round review of v0.6 after the authors responded to the four-viewpoint peer review.

**Scope:** `paper/g4_academic_paper.md` (v0.6). I did not re-run the simulation; I assess whether the revised limitations and reframed claims change the practice mapping.

---

## Summary

v0.6 is a substantially more honest paper. Ten new limitations (§9.2 #13–22) concede, accurately and in the right vocabulary, nearly every structural objection from my first review: the six-situation taxonomy conflates three constructs (#18); B2B buying committees are absent (#19); the auction mechanism omits first-price dynamics, quality scores, and censored feedback, and the calibrated-bid ceiling rests on omniscience no practitioner has (#20); even-pacing is the most naive budget algorithm and the pacing conclusion is premature (#21); match rate is not a field KPI (#22). The paper also demoted its own headline: the fair single-signal comparator is now `cam_learned` (87.5%), making the honest multi-signal gain +$51 (d_z = 0.56), not the +$102 measured against the handicapped 4-of-6-class classifier (#13/#14).

The limitation text reads like it was written by someone who listened. But with one exception, the round-1 concerns were **conceded, not modeled** — no limitation changed the simulation, the taxonomy, or the results. That is legitimate scoping for a framework-plus-benchmark paper, and the concessions are precise enough to trust. What remains is a set of qualitative findings that survive their own caveats, one claim that got *less* defensible (privacy-safe by design), and one practitioner objection that was never adopted at all (crisis → 2.0× budget).

## New-Limitations-Assessment

**Adequate, and in the right words:**

- **#18 (three constructs conflated)** — mirrors my round-1 critique almost verbatim, including the stage × condition restructure I proposed. Adequate as scoping; note the entire results section still runs on the flat 6-way taxonomy, so every number remains conditional on the conflation.
- **#19 (single decision-maker)** — honest. B2B is my world; 6–10 stakeholders per account is correct, and the account-level aggregation needed (future work #15) is the real problem. A framework paper may defer this; a B2B field deployment (§10.3 #1) may not — the primary endpoint there is account-level, so the gap between sim unit and field unit will bite first in the trial design.
- **#20 (bid mechanism)** — the strongest revision. The paper now states plainly that `bid_calibrated` is "given the mechanism — an omniscience no practitioner has" and defends F3 on the industry's own migration to automated bidding rather than on simulation results. That is exactly the right evidentiary move: F3's field validation is external (tCPA/tROAS, Advantage+ displacing manual multipliers), not internal. This limitation does not weaken the paper; it relocates the claim to where the evidence actually is.
- **#21 (even-pacing naive)** — concedes "directionally correct but premature," which is what I wrote. The pacing-bidding coupling point (pacing shades effective bids) is now on the record. Fine.
- **#22 (match rate not a KPI)** — the concession is complete, including the observation that no operating review has ever asked for match rate. **But the demotion is rhetorical, not analytical.** The abstract still leads with "raises match from 87.5% … to 98.9%"; H4/F7 still operationalizes dose-response as Spearman ρ(match rate, profit). If match rate is a design-relative diagnostic, the central dose-response claim is still being carried by a diagnostic. F6's "error placement > error count" — the genuinely practitioner-true finding — should be promoted to the headline; it remains a sub-finding.
- **#13/#14 (missing comparators; classifier family = generative family)** — these mostly serve the methodology review, but they matter to practitioners too: nearest-centroid on well-separated Gaussian clusters is close to reading the answer key's structure. The transferable question is *signal separability in production*, not classifier choice, and the paper now effectively says so.

**One step backward:** §9.3 still claims "**Privacy-safe by design** … not PII — aligned with cookieless targeting," unchanged from v0.5. After #20 and #22, this claim is now inconsistent with the paper's own honesty. The intent signal behaves like fully-observed, identified-user intent — precisely the thing cookieless browsers and iOS ATT remove. A paper that concedes censored clearing prices and absent ground-truth labels cannot simultaneously claim its intent scalar survives privacy restriction untested. This should be deleted or rewritten as an open problem.

**Never adopted:** my round-1 objection that **crisis → 2.0× budget multiplier is backwards** for most crises is absent from #13–22. Standard brand-safety playbooks pause or exclude; deliberate counter-messaging is a niche, senior call. "Crisis = bid double" remains hardcoded in the Action Layer (§6.5) as default agent behavior. An autonomous agent with that default is an incident-report generator. This is the one round-1 critique that received neither concession nor fix.

## What-Still-Transfers

After all caveats, I stand by a shorter but real list:

1. **Multi-signal beats single-signal (F9) — survives at the honest comparison.** +$51 (p = 2.5e-04, d_z = 0.56) against the fair learned comparator is modest, not spectacular — and it still transfers, because the *mechanism* is what practitioners recognize: intent alone conflates crisis↔decision and retention↔exploration, and competitive density plus contextual quality resolve exactly those ambiguities. That is why the ABM stack (Bombora, 6sense, Demandbase) layers surge, technographic, and contextual signals on behavioral scoring. The paper's honest number matches the industry's honest experience: enrichment is worth real but bounded money.
2. **Miscalibrated bid modulation is worse than none (F3) — now better supported than in v0.5**, because the defense is the industry's own automated-bidding migration rather than the toy auction.
3. **Systematic bias under distribution shift beats random noise, adversely (F5/F6) — transfers.** Every static lead-scoring model I have watched decay proves it; per-distribution recalibration is standard MLOps hygiene.
4. **Error placement > error count (F6) — transfers and is under-modeled by vendors.** Serving an awareness ad to a decision-stage buyer is expensive; the reverse is cheap. The paper's `uniform_situations` result (higher match rate, negative profit vs noisy50) is a clean demonstration of a phenomenon we see in QA audits.
5. **Sequencing: invest in classification before bid modulation.** Defensible as strategy.

**No longer transferable (correctly conceded):** the +$102 headline (handicapped comparator), the calibrated +$530 ceiling (omniscience artifact), all magnitudes and ROAS values (scaled-reward proxy, #12), and multi-signal robustness *magnitudes* under label noise (uniform noise, #16 — real corruption is class-conditional, which the paper itself notes hits the confusable pairs hardest).

## What-Is-Still-Missing

Beyond the conceded items, these practitioner concerns remain unaddressed from round 1 or are newly visible:

- **Crisis action mapping** (see above) — the outstanding un-adopted objection.
- **Privacy/consent reality** (see above) — the claim got worse as the rest got more honest.
- **Cross-device and identity resolution** — same person mid-journey on two devices; the practical blocker for exactly the context-matching proposed. Still absent.
- **Dark funnel** — G2 reviews, peer communities, offline sales conversations: where B2B evaluation actually happens, invisible to the sensing layer.
- **Label provenance in production.** The learned classifiers are fit on 2,000 *labeled* samples. In production there is no ground-truth situation label (#22 says so) — so where do 2,000 calibration labels come from? The field design's "human-coded situations" audit implies manual coding; its cost, throughput, and inter-rater reliability at campaign scale are unaddressed. This is the circular dependency the limitations miss: the remedy for distribution shift (F6) presupposes the labeled data whose absence #22 concedes.
- **Delayed, censored, attributed feedback.** Profit in the sim is immediate and fully observed. Real conversion signals arrive days later through a noisy attribution window, on a fraction of impressions. Nothing in #13–22 covers feedback latency or attribution — the gap that makes offline-trained static classifiers fragile in live campaigns.
- **One-dimensional action space** — creative/offer only; no creative × audience × placement × bid joint decision, no frequency caps or audience overlap (mentioned only as auction omissions in #20).
- **Own-ad quality as a state variable** — quality scores gate whether you clear at all; channel quality is context, your creative's historical performance is you.

## Deployability

**What I would deploy from this paper into a real DSP:** the decision heuristics, not the artifact.

- *Deploy:* the sequencing rule (multi-signal classification before bid modulation) — it is already the direction of travel; this paper is a reasoned argument for the budget order.
- *Deploy:* "never ship unvalidated bid multipliers" — already enforced by the industry's migration to automated bidding; useful as an internal justification memo.
- *Deploy:* per-distribution drift monitoring and recalibration as a first-class MLOps requirement for any situation/lead-scoring classifier, with error-*placement* (per-class recall × payoff) as the alarm metric, not raw accuracy.
- *Not deploy:* the CAM framework's Layer 1 as specified (free, exact, real-time signals), the flat 6-class taxonomy, the action-situation matrix as hardcoded policy (crisis 2× above all), any static classifier trained once, and the bid layer in any form.

The field-validation design (§10.3 #1: two arms, ≥40 campaigns, 8–12 weeks, mixed-effects) is the first thing in this line of work I would actually sign off on running — with two amendments: an incrementality holdout inside Arm A (uplift vs observed conversions, since #12 concedes no incrementality in the reward), and an explicit labeling protocol (coder count, agreement threshold, cost per labeled context) before the trial starts, because it determines whether the remedy arm is feasible at all.

## VERDICT

**PARTIALLY.** v0.6's limitations adequately and honestly address the round-1 structural critiques — the concessions are accurate, well-placed, and in one case (F3's relocation to field evidence) genuinely strengthen the paper. The transferable core survives its own caveats: multi-signal enrichment over intent-only (worth real, bounded money), the harm of uncalibrated bid modulation, drift-plus-recalibration, and error placement over error count. But the round-1 concerns were conceded rather than modeled, so every quantitative result remains conditional on abstractions (flat taxonomy, single decision-maker, free exact signals, omniscient-free but still exogenous auction); the privacy-safe claim is now internally inconsistent; the crisis-multiplier default was never addressed; and production label provenance — the precondition for the paper's own remedy — is missing. Nothing in the artifact maps to a deployable DSP component; the paper maps to practice as validated heuristics plus a credible field-trial design, which is a real contribution, but a partial one.
