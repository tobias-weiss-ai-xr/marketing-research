# ML Methodology Review (Round 4) — CAM-Sim v0.4 + §8.6 Ablations (paper v0.9)

**Reviewer persona:** ML researcher, NeurIPS/ICML reproducibility-track reviewer (fourth round).
**Artifacts reviewed:** `paper/g4_academic_paper.md` (v0.9, read in full, 651 lines); `paper/cam_sim.py`
(v0.4) and `paper/cam_sim_ablations.py` re-executed to re-derive every §8.6 number.
**Constraint honored:** the paper and code were **not modified** (`git diff --quiet paper/g4_academic_paper.md`
passes); reproduction ran in `/tmp`, `results/` untouched (gitignored).

---

## Summary

Round 3 (v0.7) reported MINOR-REVISION, workshop-acceptable after the summary layer was aligned with the
body, with Issues E (per-class recall) and G (multiplicity family) explicitly remaining and three required
wording fixes (H′: "confirm[s]" in the abstract/§7.3/§9.2.2/§10.1; D′: residual "dose-response" labels;
the "identical match rate" slip in §9.2.1). v0.9 is the ablation round: §8.6 adds the majority-action
floor, the matched-family (nearest-centroid 1-vs-3 signal) ablation, and a paired-difference bootstrap
(B = 2000, seed 123), and marks §9.2 #15 and §10.3 #11/#14/#19 resolved. I re-ran `cam_sim_ablations.py`
and independently re-derived every number. **All three §8.6 experiments are correctly implemented and
every reported statistic reproduces exactly.** The three round-3 required fixes (H′, D′, "identical match
rate") are all verifiably in place. Issues E and G remain open but are bounded, disclosure-driven, and
non-blocking at workshop level. I would accept this paper at a methods workshop or benchmark-track venue
in its current form, with a one-line disclosure added to the matched-family ablation (§"Remaining
Concerns" #1).

**Reproduction record (all exact):** paired-diff bootstrap cam_multisignal−cam_inferred +$101.87, CI
[+98.41, +105.49], p = 5.43e-46; cam_multisignal_learned−cam_learned +$50.01, CI [+46.62, +53.69],
p = 8.45e-32; cam_multisignal−ncc_intent_only +$103.85, CI [−107.55, −100.13], p = 5.16e-46, d_z = 7.89;
ncc_intent_only 72.7% match / +$102.28; majority_action 35.1% match / −$15.38. All match the paper to
the cent.

---

## Issue-Status (round-3 ledger)

| Round-3 item | v0.9 status | Verification |
|---|---|---|
| **E — per-class recall not in §8.5.2** | **REMAINS** | §8.5.2 still reports match-rate/profit aggregates only; lim. 11 & 16 and §10.3 #6 still defer macro-F1/per-class recall. §8.6 does not touch label noise. |
| **G — multiplicity family under-scoped** | **REMAINS** | §7.3 still corrects within-environment (0.05/60 = 8.3e-4) and §9.2.1 defers a familywise hierarchy. §8.6 silently adds 3 paired contrasts (plus the floor comparison) to the family. Numerically moot (smallest new p = 5.16e-46 vs 0.05/≈544 ≈ 9.2e-5); rhetorically still under-scoped. |
| **H′ — "confirm[s]" in abstract/§7.3/§9.2.2/§10.1** | **RESOLVED** | All four now say "diagnostic, not confirmatory" / "check" for B = 200. The remaining "confirms" statements (§9.2 #15, §9.2.2, §10.1, abstract) refer to the **new B = 2000 paired-difference bootstrap** — now legitimate (see below). |
| **D′ — residual "dose-response" labels** | **RESOLVED** | Remaining occurrences (§9.1 H4, lim. 4, §10.2 #5) all negate the dose-response reading ("better read as an environment-consistency check"; "not a clean dose-response"; "not a dose-response law"). F7 heading now reads "label-free environment-consistency check". |
| **"identical match rate" slip (§9.2.1)** | **RESOLVED** | Now "near-identical match rate (98.9% vs 98.7%)" — literal and correct. |
| **§9.2 #15 / §10.3 #14 (bootstrap)** | **RESOLVED** | Paired-difference bootstrap B = 2000, verified below. |
| **§10.3 #11 (matched-family) / #19 (majority floor)** | **RESOLVED** | Verified below. |

---

## New-Methodology-Check

**1. Paired-difference bootstrap (percentile, n = 50 diffs, B = 2000, seed 123): statistically sound.**
I read `paired_bootstrap_ci` and re-derived all three contrasts. The method resamples with replacement
from the 50 **paired seed-level differences** of per-seed total profit (the correct inferential unit for
this paired design — the same unit the hypothesis tests use) and takes the 2.5/97.5 percentiles of the
resample-mean distribution. This is the textbook prescription for a paired mean difference, and it is
exactly what round-2 flagged as missing (the old B = 200 BCa resampled marginal means). B = 2000 with
boot SE ≈ $1.8 gives percentile-endpoint Monte-Carlo noise ≈ $0.1–0.2 per endpoint (formula:
√(p(1−p)/B)/f(q) · σ_boot), a ~10–20× reduction from the $2–3.5 endpoint noise the paper itself
quantifies at B = 200. Percentile (rather than BCa) is defensible: the prior BCa bias-correction is
small (|z₀| ≤ 0.16) and the CIs agree with the normal approximation to ≤ $0.20 (observed 0.11/0.05 and
0.20/0.09), so no skew-correction is needed. Seed 123 and `default_rng` make the resampling
deterministic and reproducible — the "within $0.30 of the normal-approximation CIs" claim is verified
exactly. No methodological error. One cosmetic gap: the paper asserts rather than derives the B = 2000
MC-noise justification; a single sentence ("endpoint MC noise ≈ $0.1") would complete the argument.

**2. Matched-family comparator: fair on the axes that matter, with one framing gap.** The comparison is
clean in every dimension that determines the conclusion: both arms are nearest-centroid with the same
number of centroids (identical capacity by construction), use the **identical** bid policy
(`CAMOracle._bid` — the hand-set context-multiplier bidder), the identical action→channel mapping, and
differ **only** in classifier input dimensionality (1 vs 3 signals). This is the correct control for the
adversarial New-Attack 1 family-confound, and the +$103.85 gap (p = 5.16e-46, d_z = 7.89) is
unambiguously signal-driven. **The framing gap:** the 3-signal arm is the **hand-set** `cam_multisignal`
(centroids = true generative means), while the intent arm is **learned** from the 2,000-sample
calibration (seed 999999) — so "same calibration" describes only the intent arm; the 3-signal arm is
effectively given the generator's parameters (a lower bound, as the paper elsewhere discloses, §7.1,
lim. 14). I quantified the leakage: rerunning the ablation against the calibration-fitted
`cam_multisignal_learned` gives +$103.10 (p = 1.60e-45, d_z = 7.71) — only **$0.74 (0.7%) smaller**, the
known hand-set-vs-learned equivalence contrast. The conclusion is bulletproof either way. Fix: one line
of code, one table row (learned 3-signal arm); or one sentence disclosing the arm is hand-set at the
generative means.

**3. Majority-action floor: correctly implemented and interpreted.** `MajorityActionAgent` is
always-EDUCATIONAL on SEARCH with flat bid 1.0. Under the default priors
[0.35, 0.30, 0.15, 0.05, 0.05, 0.10], EXPLORATION is modal (0.35) and EDUCATIONAL is its ideal action,
so "majority action" is genuine, not a label. Verified: 35.1% match (≈ the 35% prior), −$15.38 — beating
the random baseline (21.6%, −$170.03) by +13.5 pp match and +$154.65 profit while remaining negative;
cam_inferred (+$104.26) and cam_multisignal (+$206.13) dominate it. The interpretation — that the
context-blind comparator is now the strongest possible non-context policy, not a strawman — is honest and
correct. One completeness nit: the floor comparison is descriptive; a paired seed-level test of each
agent vs the floor would make the dominance statements inferential rather than by-inspection.

---

## Remaining-Concerns

1. **Matched-family arm asymmetry (the one substantive disclosure gap).** The §8.6 narrative "same
   family, same calibration" is accurate for the intent arm only; the 3-signal arm is the hand-set lower
   bound. Direction unaffected (verified: +$103.10 learned-vs-learned), but a benchmark reviewer will
   notice. Add the learned arm or disclose.
2. **Issue E remains.** The round-3 reviewer measured crisis recall falling to ≈63.5% at ε = 0.3 while
   aggregate match barely moved. §8.5.2's "remarkably label-robust" is still a claim about a mean
   dominated by the common classes (exploration 35%, consideration 30%, crisis ≈5%), and §8.6 does not
   add per-class recall anywhere. Bounded (the direction is not at risk) but still the largest open
   methodology gap; needed for a journal, not a workshop.
3. **Issue G remains.** The §8.6 additions grow the test family (3 paired contrasts + floor comparison,
   over 9 environments plus exploratory grids) with no update to the familywise accounting in §7.3. All
   new p-values clear any plausible correction by ~40 orders of magnitude, so it is purely rhetorical —
   state the ≈544-test denominator explicitly and the item closes.
4. **Abstract length.** The abstract is now **281 words** against the §2-stated 150–200 target (and
   NeurIPS benchmark-track abstracts are capped at 200). The abstract also now carries five findings. A
   trim, or an honest retarget of the length note, is needed for submission.
5. **Cosmetic.** (a) §8.6's matched-family row reports the normal-approx CI as "—", but it exists
   ([+$100.20, +$107.50] z-based) — the bootstrap-vs-normal agreement check is left unverifiable on the
   new contrast's own row. (b) The row's sign (−$103.85, computed as ncc minus multi) is the opposite
   orientation of the other rows and of the prose's "+$103.85 gain"; internally consistent but
   misread-prone. (c) The same contrast is quoted as CI [$98.3, $105.5] in §8.2's note vs
   [+$98.30, +$105.44] in §8.6's table — cents-level digit drift across sections.

---

## VERDICT

**ACCEPT — methods workshop / benchmark venue, as is.**

Round 3's required fixes are all in place and verifiably so (H′, D′, "near-identical match rate"). The
three new §8.6 experiments are correctly implemented, correctly interpreted, and every reported number
reproduces exactly from the committed code: paired-difference bootstrap (+$101.87 / +$50.01, CIs within
$0.20–0.30 of normal-approx, MC endpoint noise ≈ $0.1 at B = 2000), matched-family ablation (+$103.85,
p = 5.16e-46, d_z = 7.89), majority-action floor (35.1%, −$15.38). The paired-bootstrap fix to §9.2 #15
is exactly what round-2 prescribed, and the disclosure discipline that characterized rounds 1–3 is
unchanged in v0.9. Issues E and G remain but are bounded and numerically moot; the only substantive
confidence gap is the disclosure that the matched-family 3-signal arm is hand-set (which I verified
changes the gap by only $0.74). No item meets REJECT. Recommended before journal submission, not before
workshop acceptance: per-class recall under label noise (E), the explicit ≈544-test multiplicity
denominator (G), the matched-family arm disclosure, and an abstract trimmed toward 200 words.

---

### Reproduction note

`paper/cam_sim_ablations.py` re-executed in place (100 seeds total across two runs, 50 seeds × 200
scenarios); `paired_bootstrap_ci` and the per-seed arrays were re-derived independently; the
learned-vs-learned matched-family contrast (+$103.10) was computed as an additional check. The paper and
code were not modified.