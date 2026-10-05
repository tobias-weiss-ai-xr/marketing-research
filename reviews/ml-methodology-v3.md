# ML Methodology Review (Round 3) — CAM-Sim v0.4 and the v0.7 Statistical Corrections

**Reviewer persona:** ML researcher, NeurIPS/ICML reproducibility-track reviewer (third round).
**Artifacts reviewed:** `paper/g4_academic_paper.md` (v0.7, read in full, 631 lines); `paper/cam_sim.py`
(v0.4) re-executed out-of-tree to re-derive every headline contrast.
**Constraint honored:** the paper and code were **not modified** (`git diff --quiet paper/g4_academic_paper.md`
passes); reproduction ran in `/tmp`, `results/` untouched.

---

## Summary

Round 2 (v0.6) reported that the round-2 disclosure work was structurally correct but numerically
contaminated: the *fair* learned-vs-learned headline (+$50.01) carried the effect-size signature of
the economically trivial `cam_multisignal − cam_multisignal_learned` contrast (+$0.74), the
"learned" endpoints still quoted the hand-set 98.9% / +$206.13, "NCC is Bayes-optimal" was imprecise,
ρ(match, profit) was presented as dose-response evidence, the non-monotone convergence path was
described as "stable from 20 seeds," and the admittedly underpowered B = 200 bootstrap was still
listed as confirmatory. v0.7 addresses the pieces it set out to address, and I verified the fixes
against the code rather than the prose.

I re-ran `run_env(None, seeds=1..50, scenarios=200, DEFAULT_AGENTS)` and recomputed the paired
contrasts. **The three rewritten statistics now reproduce exactly**: learned-vs-learned = +$50.01,
p = 8.5e-32, d_z = 3.96; the equivalence contrast = +$0.74, p = 2.5e-04, d_z = 0.56 (and it appears
**only** in §9.2.1); the handicapped contrast = +$101.87, p = 5.4e-46, d_z = 7.88. The marginal
table reproduces to the cent. The round-2 major finding — a reproducible reporting error on the
headline claim — is fixed and verified.

Issues A, B, C, and F are resolved. Issue D is substantially resolved. Issue H is only *partially*
resolved: the bootstrap is demoted in the contribution list but the abstract, §7.3, the §9.2.2
opening, and §10.1 still assert that BCa and convergence *confirm* the result — the exact claim the
body now retracts. Issues E (per-class recall) and G (multiplicity family) remain open, as expected.
The verdict improves from round-2's MINOR-REVISION to a workshop-acceptable MINOR-REVISION, gated on
aligning the summary layer with the body.

---

## Issues A–H Status

| # | Round-2 concern | v0.7 status | Verification |
|---|---|---|---|
| **A** | Learned-vs-learned carried the +$0.74 contrast's d_z/p | **RESOLVED** | Re-derived: `cam_ms_learned − cam_learned` = +$50.0096, p = 8.45e-32, d_z = 3.959. Paper's +$50.01 / 8.5e-32 / 3.96 (abstract, F9, §9.1, §10.1) is correct. `2.5e-04` and `d_z = 0.56` now appear **only** at §9.2.1 (line 456), attached to the +$0.74 equivalence contrast, which also re-derives exactly. |
| **B** | Abstract/§10.1 used hand-set 98.9% / +$206.13 | **RESOLVED** | Abstract (l.25) and §10.1 (l.512) now say "87.5% (learned single-signal) to 98.7% (learned multi-signal) and profit from +$155 to +$205." Hand-set 98.9 / +$206.13 now appears only where the hand-set agent is explicitly the subject (§7.1, §8.1, F9, §9.1). |
| **C** | "NCC is Bayes-optimal" | **RESOLVED** | §7.1, §9.1, lim. 14: "Bayes-optimal only in the isotropic/equal-prior special case; the generator uses unequal priors and non-isotropic features … 98.9% is a lower bound, not the Bayes rate (MAP ≈99.2%)." |
| **D** | ρ(match, profit) sold as dose-response | **SUBSTANTIALLY RESOLVED** | Caveat added in §9.1 ("better read as an environment-consistency check than an empirical law") and §10.2 #5. But the label "dose-response" persists verbatim in F7's heading, §8.5 implications, §10.2 #3–4, and the title's "dose-response evidence." Partially purged, not fully. |
| **E** | Label-noise robustness aggregate-only | **REMAINS** | §8.5.2 still reports only match-rate/profit aggregates; no per-class recall table. lim. 11 & 16 and §10.3 #6 still *defer* it. |
| **F** | "Stable from 20 seeds" overclaims | **RESOLVED** | §9.2.2 now states the path is "non-monotone," the N = 10 row is "vacuously stable," and "convergence is not formally established." lim. 17 identical. |
| **G** | Multiplicity family under-scoped | **REMAINS** | §7.3 still corrects within **0.05/60** (one environment) and claims "all reported comparisons survive familywise correction," while claims span 9 presets plus exploratory grids (≈540+ tests). §9.2.1 still defers a familywise hierarchy. Numerically moot, statement under-scoped. |
| **H** | B = 200 bootstrap listed as contribution | **PARTIALLY RESOLVED** | §10.2 #5 now reads "demoted from confirmatory to diagnostic"; §9.2.1 says "the normal-approximation CIs are the primary inference." **But** §7.3 (l.285), the abstract (l.25), the §9.2.2 opening (l.460), and §10.1 (l.512) still say BCa "confirm[s]" the result. |

---

## Remaining Concerns

**H′ — the demotion did not propagate to the summary layer (the one substantive integrity issue left).**
The paper's body now correctly says the B = 200 bootstrap is underpowered, resamples the wrong
(marginal, not paired) quantity, and is *not* confirmatory. Yet four locations still assert the
opposite: the abstract ("is confirmed by bootstrap BCa CIs (200 resamples) and seed-count
convergence"), §7.3 ("Bootstrap BCa CIs … confirm the normal-approximation CIs"), the §9.2.2
opening ("The non-parametric BCa CIs confirm … to within $1.4"), and §10.1 ("confirmed by bootstrap
BCa CIs and seed-count convergence"). A reader who reads only the abstract or conclusion receives the
retracted claim. This is verbatim self-contradiction inside one document, and it lands on the
paper's robustness story. It is a wording fix, not a new experiment — but it must be made.

**D′ — "dose-response" survives in the results framing.** §9.1 and §10.2 #5 carry the correct
"environment-consistency check" reframe; F7's heading, §8.5's implications, §10.2 #3–4, and the top
banner still call it "dose-response evidence." Since the paper itself concedes the match bonus is a
linear component of profit, keeping the dose-response label in the results sections re-introduces the
near-tautology the caveat was meant to neutralize. Purge it consistently or define what, beyond the
accounting identity, the ρ test establishes.

**E′ — per-class recall is still invisible where it matters.** The round-2 reviewer measured crisis
recall falling to 63.5% at ε = 0.3 while aggregate match barely moved. §8.5.2's "remarkably
label-robust" is a statement about a mean that is dominated by the common classes (exploration 35%,
consideration 30%, crisis ≈5%). The stress-test paragraph carries no pointer to lim. 16, so a reader
who reads only §8.5.2 gets the strong claim without the rare-class caveat. This is the largest
remaining methodological gap; it is bounded (the direction is not at risk) but not closed.

**Minor — "despite the identical match rate" (§9.2.1, l.456).** The relocated equivalence sentence
says `cam_multisignal` (+$206.13) vs `cam_multisignal_learned` (+$205.39) is significant "despite
the identical match rate." The match rates are 98.9% and 98.7% — near-identical, not identical. A
small but literal inaccuracy in the one sentence v0.7 moved specifically to fix Issue A.

**G′ — the multiplicity family is numerically safe but rhetorically loose.** Every reported p-value
(≤ 8.5e-15 for the headline, ≤ 1.5e-30 for the robustness contrasts) survives 0.05/540 and the
α-sweep grids by many orders of magnitude, so no conclusion changes. The correction denominator
merely understates the search space; state it explicitly (9 environments × 60 = 540, plus exploratory
grids) and the point is closed.

---

## Statistical-Integrity-Verdict

**Honest in the body, inconsistent at the summary.** The substantive pattern from round 2 has
flipped: where v0.6 had correct structure with wrong numbers, v0.7 has correct numbers with residual
overstatement at the edges. The disclosure discipline is genuine and verified — the convergence
caveat, the seed-pairing admission (lim. 10), the decoy-signal admission (#24), and the
perception/bidding confound (lim. 4) are the kind of self-critique that survives audit. The central
claim is information-theoretically robust independent of all this: a single noisy scalar cannot
identify six overlapping classes, so no stronger single-signal learner overturns the direction, and
the learned-vs-learned +$50 gap (d_z = 3.96) is not a classifier-family artifact. Nothing here is
fabrication; the failures are places where a fixed claim was not propagated to every location.

What keeps this from a clean pass is that the remaining overstatements (H′ especially) sit precisely
on the paper's robustness claims, and the abstract is the most-read artifact. That is a revise-and-
resubmit at journal level, but at a **methods workshop** — which rewards a reproducible benchmark and
candid stress testing over polished overclaiming — I would accept after the summary layer is aligned.

**Direct answers to the four assessment questions.** (1) Issues A–C and F are resolved; D is
substantially resolved; H is partially resolved (demeaned in the body, still confirmatory in the
summary). (2) Issues E and G remain open. (3) The paper is statistically honest *in the body*; the
abstract, §7.3, and §10.1 remain inconsistent with it. (4) Yes — I would accept this at a methods
workshop once the abstract/conclusion stop claiming confirmation the body retracts; the core
contribution does not depend on the disputed diagnostics.

---

## VERDICT

**MINOR-REVISION — workshop-acceptable after the abstract is aligned with the body.**

The round-2 major error (Issue A) is fixed and I verified it by re-running the simulation: +$50.01,
p = 8.5e-32, d_z = 3.96 for learned-vs-learned, and the +$0.74 / 2.5e-04 / 0.56 equivalence signature
now appears only in §9.2.1. Issues B, C, and F are cleanly resolved; D is substantially resolved.
Required before I would sign off: (1) delete "confirmed by bootstrap BCa CIs … and seed-count
convergence" from the abstract and §10.1, and remove "confirm" from §7.3 and the §9.2.2 opening, so
the summary matches the §9.2 #15 / §10.2 #5 demotion; (2) purge the residual "dose-response" labels
(§8.3 F7, §8.5, §10.2 #3–4); (3) fix the "identical match rate" slip in §9.2.1. Not required for
workshop acceptance, but needed for a journal: per-class recall in the label-noise stress test (Issue
E) and an explicit 9-environment multiplicity denominator (Issue G). No item meets REJECT — the core
multi-signal direction survives every disclosure, and the replication is byte-reproducible.

---

### Reproduction note

`run_env(None, seeds=1..50, scenarios=200, DEFAULT_AGENTS)` was imported from `paper/cam_sim.py` and
executed in `/tmp`; `compute_statistics` was used directly. All three headline contrasts and all
eleven marginal means reproduced the paper to rounding. The paper and code were not modified.
