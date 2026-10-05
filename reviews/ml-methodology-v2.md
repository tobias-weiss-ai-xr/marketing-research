# ML Methodology Review (Round 2) — CAM-Sim v0.4 and the v0.6 Statistical Disclosures

**Reviewer persona:** ML researcher, NeurIPS/ICML reproducibility-track reviewer (second round).
**Artifacts reviewed:** `paper/g4_academic_paper.md` (v0.6, read in full, 625 lines) and,
to audit the disclosures, `paper/cam_sim.py` (v0.4, 1,878 lines): `_fit_learner_for_config`
(504–530), `fit_multisignal_classifier` (571–587), `run_env` (1253–1300), `bca_ci` (1132),
`run_convergence` (1410–1452), and the `main` bootstrap call sites (1740–1760).
**Constraint honored:** the paper and code were read but **not modified**
(`git diff --quiet paper/g4_academic_paper.md` passes). Reproduction runs were executed
out-of-tree; `results/` is gitignored and untouched.

---

## Summary

Round 1 raised five substantive concerns: a handicapped headline comparator, a "Bayes rate"
mislabel, missing ML comparators, a B = 200 bootstrap that is underpowered and bootstraps the
wrong quantity, and two stress tests (uniform label noise, vacuous N = 10 convergence) that
answered narrower questions than the text claimed. v0.6 **discloses all of them**, and I
verified the disclosures against the code: every one is factually accurate. The candor is
genuine and unusual for a benchmark paper, and the core multi-signal direction remains
information-theoretically robust. Disclosure, however, is not correction: roughly eight
round-1 items are now restated as limitations with the fix *deferred*, not performed.

More seriously, I found a **reproducible reporting error** in the one block of numbers the
revision was specifically supposed to fix. The headline *fair* learned-vs-learned effect
(`cam_multisignal_learned − cam_learned`, +$50.01) is attributed the statistical signature of a
different, economically trivial contrast (`cam_multisignal − cam_multisignal_learned`, +$0.74):
the true effect is **d_z ≈ 3.96, p ≈ 8.5e-32**, not the reported **d_z = 0.56, p = 2.5e-04**.
The error appears in the abstract, §8.3 F9, §9.1, §9.3, and §10.1. Separately, the "learned"
comparison still quotes the *hand-set* classifier's 98.9% match instead of the learned 98.7%.
The dual reporting is therefore structurally improved but numerically still conflated. Because
these are fixable without new experiments, the verdict is MINOR-REVISION.

---

## Round-1 Concerns Addressed

I audited each item against the source, not just the prose.

| Round-1 concern | Status | Evidence |
|---|---|---|
| Handicapped single-signal comparator | **Addressed structurally, numbers wrong** | Abstract now leads with the learned-vs-learned +$51 and frames +$102 as the "hand-tuned threshold" effect; §9.1 names `cam_learned` "the fair single-signal comparator." But the +$51 block carries the wrong d_z/p (Issue A). |
| "Bayes rate" mislabel for 98.9% | **Addressed** | §7.1, §9.1, lim. 14: "nearest-centroid lower bound, not the Bayes rate; MAP ≈99.2%." One residual imprecision (Issue C). |
| Missing logistic/GBM/bandit comparators | **Disclosed, not done** | lim. 13–14; §10.3 #11–12. |
| B = 200 bootstrap underpowered / wrong quantity | **Disclosed, not done** | lim. 15; §9.2.2 caveat. Code confirms `bca_ci(per_seed_values['total_profit'][name], …)` resamples *marginal* means (1745) with B = 200. |
| Uniform, not class-conditional, label noise | **Disclosed, not done** | lim. 16. Code confirms flips go to a uniformly random *other* class (508, 515–521, 596–607). |
| N = 10 convergence vacuously stable | **Disclosed, not done** | lim. 17; §9.2.2 caveat. Code confirms `vals[-10:]` is the whole sample at N = 10 (1410–1452). |
| Seed pairing buys no power | **Newly disclosed, honest** | lim. 10. Code confirms one global `random.seed(seed)` consumed sequentially across agents (1269–1300). |

The disclosures are **truthful**, which matters: the round-1 reviewer could not have assumed the
authors would admit the bootstrap resamples the wrong quantity or that pairing buys no power.
That is a real gain in trust.

---

## Remaining Statistical Issues

**A. Duplicated effect-size statistics on the headline claim (major, reproducible).**
Running `paper/cam_sim.py` at 50 seeds × 200 scenarios (default economics), the paired seed-level
contrasts are:

- `cam_multisignal_learned − cam_learned` = **+$50.01**, SD_diff $12.63, **d_z = 3.96**,
  t = 27.99, **p = 8.5e-32**, 95% CI [+$46.5, +$53.5].
- `cam_multisignal − cam_multisignal_learned` = **+$0.74**, **d_z = 0.56**, t = 3.95,
  **p = 2.5e-04**.
- `cam_multisignal − cam_inferred` = +$101.87, p = 5.4e-46, d_z = 7.88 (**reproduces exactly**).

The paper attaches the *second* contrast's `d_z = 0.56, p = 2.5e-04` to the *first* contrast in
the abstract, §8.3 F9, §9.1, §9.3, and §10.1. The impossibility is visible even without running
the code: a +$50.01 paired difference with `d_z = 0.56` requires SD_diff ≈ $89, but the paper's
own §8.1 marginal CIs imply SD ≈ $15–17 per agent, and SD_diff can never exceed SD_a + SD_b ≈ $32.
The error is *conservative* (it understates significance), but it contradicts the paper's "no
hand-typed numbers" pledge and lands on precisely the contrast the revision was meant to repair.

**B. Hand-set/learned conflation persists.** The abstract and §10.1 state that multi-signal
awareness "raises match from 87.5% (learned single-signal) to 98.9% (learned multi-signal)." 98.9%
is `cam_multisignal` (hand-set true centroids); the *learned* multi-signal agent is 98.7%. The
abstract's profit endpoint uses the hand-set +$206.13 rather than the learned +$205.39. §8.3 F9
and §9.1 use the correct 98.7%; the abstract and summary do not. This is the same
hand-set-vs-learned confusion round 1 asked to remove.

**C. "NCC is Bayes-optimal" is imprecise.** Lim. 14 calls nearest-centroid "the Bayes-optimal
classifier for the generative model (equal-variance Gaussian clusters)." But the generator draws
intent with SD 0.1 and competition/quality with SD 0.15 and uses unequal priors; §9.1 itself
reports MAP ≈99.2% > 98.9%. NCC is Bayes-optimal only under isotropic equal-variance features and
equal priors. Correct wording: "Bayes-optimal only in the isotropic/equal-prior special case; here
it is a lower bound."

**D. The ρ "dose-response" is near-tautological.** `context_match` is defined against the authors'
`IDEAL_ACTION[situation]`, and the reward table pays a match bonus keyed to that same label
(lim. 11 concedes the mechanical tie). A near-unity ρ(match, profit) therefore validates the
simulator's own accounting rule, not an empirical law. The bid-policy confound (lim. 4) compounds
this, and heavy ties (three agents at 100% match) shrink the effective rank. The label-free ρ is a
useful environment-consistency check; it should not be presented as dose-response evidence for H4.

**E. Label-noise robustness is aggregate-only.** §8.5.2's "remarkably label-robust up to ε = 0.3"
concerns *match rate*. Uniform corruption concentrates contamination in the rare classes (crisis
prior ≈ 5%); without per-class recall (deferred, lim. 11/16), the rare-class collapse round 1
measured (crisis recall 63.5% at ε = 0.3) is invisible in the reported aggregate. The inline
§8.5.2 text does not carry the lim. 16 caveat, so a reader of the stress test alone gets the
strong claim.

**F. "Stable from 20 seeds" is not established.** The v0.6 convergence path is non-monotone
(N = 10→50: +213.76, +208.52, +209.69, +206.57, +206.13); N = 20 is closest to N = 50 by
coincidence, not convergence. With no trend test (lim. 17), "20 seeds suffice" is an assertion.
Remove the N = 10 row and report SE-vs-N.

**G. Multiplicity family is under-scoped.** §7.3 corrects within 60 comparisons in one
environment, but claims span 9 environments plus exploratory grids. This is mostly moot — the true
+$50 effect is p = 8.5e-32 and survives any correction — but the family should be stated explicitly.

**H. A known-inadequate check is still a listed contribution.** §10.2 includes the B = 200
bootstrap under "Methodological," with the caveat attached. A test the paper has itself shown to be
underpowered should be demoted to an appendix diagnostic, not counted as a contribution.

---

## Dual-Reporting-Assessment

**Honest in structure, not yet in numbers.** The abstract now opens with the matched
learned-vs-learned +$51 and presents +$102 only as the naive hand-tuned effect; §9.1 explicitly
identifies `cam_learned` as the fair comparator; lim. 5 and 14 flag `cam_inferred` as structurally
handicapped (4-of-6 classes). That is the requested fix, and it is the right one. But the content
still leaks: (i) the +$51 block carries the +$0.74 contrast's d_z/p (Issue A); (ii) the match
endpoints pair a learned 87.5% with a hand-set 98.9% (Issue B); (iii) the abstract's profit endpoint
is the hand-set +$206.13, not the learned +$205.39. The ordering is no longer misleading; the
numbers are. Replace 98.9 → 98.7, +$206 → +$205.39, and d_z = 0.56 / p = 2.5e-04 →
d_z = 3.96 / p = 8.5e-32 in the learned-vs-learned sentences, and the dual reporting becomes fully
honest.

---

## Limitations-Assessment

**Mostly rigor, with a genre risk.** Items 1–12 are substantive self-critiques. Items 13–22 are,
almost without exception, "not done, deferred to §10.3," and several duplicate one another
(11/22, 13/14, 13/16). A 22-item list in which a third is "we did not run the comparator or
analysis that would settle this" reads less as rigor than as an inventory of unaddressed problems;
the honesty is real, but the volume also reveals how far the claims outrun the evidence. Two
refinements would convert the list from a to-do roll into methodological discipline: (a) give every
item a disposition — *tested / bounded / known-safe / open* — and (b) state which specific claim
each open item would change if run. The "tested" items (2, 7, 8, 9) already do this well; the
untested items do not. As written, the four "tested" items do real defensive work, and the ten
untested ones mostly transfer risk to future work.

---

## VERDICT

**MINOR-REVISION.**

**Justification.** The round-1 disclosures are adequate and — verified against `cam_sim.py` — truthful;
the simulation is byte-reproducible and the central multi-signal direction is information-theoretically
robust (nearest-centroid on a single feature is capped near the learned 87.5%, so no stronger
single-signal learner can overturn the direction). No new experiment is needed to make the paper
honest. But the headline *fair* effect carries a duplicated statistic in four places (true
d_z ≈ 3.96, p ≈ 8.5e-32 versus reported 0.56, 2.5e-04), and the learned/hand-set match and profit
numbers remain conflated in the abstract and conclusion. These are reproducible correctness errors in
the paper's own claims and must be fixed before publication.

Required for acceptance at a methods workshop: (1) correct the +$50.01 block (Issue A) and the
98.9/98.7 and +$206/+$205.39 endpoints (Issue B); (2) reframe ρ(match, profit) as an
environment-consistency check rather than dose-response evidence (Issue D); (3) fix the NCC/Bayes
wording (Issue C); (4) demote the B = 200 bootstrap from a contribution (Issue H). Nothing here meets
REJECT — the disclosures are unusually candid and the core direction survives — but at
*Journal of Marketing* / *Marketing Science* rather than a methods workshop, the absent
matched-family comparator and per-class recall would leave me at CONCERNS.

---

### Reproduction note

Contrasts were re-derived by importing `paper/cam_sim.py` and calling
`run_env(None, seeds=1..50, scenarios=200, DEFAULT_AGENTS)`; `compute_statistics` was replicated with a
pure-Python Student-t tail to avoid a WSL scipy/numpy binary clash. The reproduction returns
`cam_multisignal − cam_inferred` = +$101.87, p = 5.4e-46, d_z = 7.88 — byte-matching the paper — which
validates the pipeline used to expose the +$50.01 discrepancy. The paper and code were not modified.
