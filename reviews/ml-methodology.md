# ML Methodology Review — CAM-Sim Classifier Comparison and Statistical Inference

**Reviewer persona:** ML researcher, NeurIPS/ICML reproducibility-track reviewer.
**Artifacts reviewed:** `paper/cam_sim.py` (v0.4, 1,878 lines) and the reporting in
`paper/g4_academic_paper.md` (§6.4, §7.1, §7.3, §8.5.2, §9.2.2, Appendix A).
**Constraint honored:** the paper and code were read but **not modified** (`git diff --quiet paper/g4_academic_paper.md` passes).

---

## Summary

CAM-Sim is a synthetic ablation benchmark that compares a ladder of marketing
agents differing in *what* context information they perceive (random, channel-only,
graded perception, intent-only, three-signal) and *how* they are implemented
(hand-set thresholds, hand-set true centroids, learned centroids, oracle). The
headline machine-learning claim (F9) is that multi-signal **nearest-centroid**
situation classification beats single-signal intent inference
(+$104.26 → +$206.13, +$101.87, p = 5.4e-46), and that a *learned* multi-signal
classifier recovers the structure from data (+$205.39).

The code is small, deterministic, and internally consistent: every number I
re-derived reproduces. The core methodological mechanics are implemented
correctly. My concerns are not about bugs but about **what the comparison
isolates, how strong the statistical machinery is at the sample sizes used, and
how faithfully the stress tests model the deployment risks the paper claims to
address.** Three of five dimensions are CONCERN; none is FLAWED at the level of
the central directional result.

---

## Classifier-Fairness — **CONCERN**

**What is correct.** I verified the learned multi-signal fit
(`fit_multisignal_classifier`, `cam_sim.py:571`): it computes, per class, the
arithmetic mean of each of the three features — i.e. genuine class-conditional
sample means. Nothing is wrong here. I re-drew the 2,000-sample calibration set
(seed 999999, default distribution) and confirmed the learned centroids sit
within L2 ≤ 0.012 of the true generative means, including the rarest classes.
Per-class counts are exploration 689, consideration 641, decision 294, crisis 87,
opportunity 93, retention 196; the Monte-Carlo standard deviation of each learned
centroid coordinate across re-draws is < 0.009 — one to two orders of magnitude
below the ~0.3 inter-class separations. **2,000 samples for 6 classes × 3
features is comfortably sufficient.** Sample size is not the issue.

**Issue 1 — the headline single-signal comparator is handicapped, and the paper's
own matched comparator changes the magnitude by ~2×.** The reported multi-signal
advantage is measured against `cam_inferred` (75.7%), a hand-tuned threshold rule
that (as §9.2 limitation 5 admits) can emit only 4 of 6 classes. The matched
complexity-class comparison is learned-vs-learned: `cam_learned` (87.5%,
intent-only interval classifier) vs `cam_multisignal_learned` (98.7%). That
contrast is **+$50.01** — half the headline +$101.87. The abstract and conclusion
("raises match from 75.7% to 98.9% … +$104 to +$206") quote the handicapped
comparator while the limitations section calls `cam_learned` "the fairer
intent-only comparator." The paper should lead with the matched learned-vs-learned
effect (+$50) and present +$101.87 only as the "naive hand-tuned baseline" effect.

**Issue 2 — "the generator's Bayes rate" is a mislabel.** §9.1 states the 98.9%
hand-set match "is the generator's Bayes rate." It is not. The hand-set rule is
equal-prior Euclidean **nearest-centroid** applied to features that the generator
draws with *unequal* variance (intent ±0.1, competition/quality ±0.15) under a
*skewed* class prior (exploration 35%, crisis 5%). The MAP classifier
(prior-weighted, variance-normalized) achieves ≈99.2% on 20,000 in-distribution
contexts; the true Bayes rate is therefore ≥ 99.2%, and 98.9% is a lower bound
produced by a misspecified discriminant. The distinction matters because the
paper uses "Bayes rate" to imply the classifier cannot be improved.

**Issue 3 — hand-set vs learned is a consistency check, not evidence.** Because
the hand-set centroids are exactly the true generative means and calibration and
deployment draw from the *identical, clean* generator, the learned variant can
only confirm that the estimator is unbiased. It does not demonstrate that
three-signal structure is recoverable under any realistic conditions (shifted,
noisy, or partly missing signals). §9.1 over-reads this as "the evidence that the
structure is recoverable from data alone."

**What is fair.** All classifier agents share the same oracle bid engine
(`_bid`), so the F9 contrast holds the bid policy fixed and isolates the
classifier. That is the right design.

---

## Missing-Comparators — **CONCERN**

There is no logistic regression, gradient boosting, or neural comparator; the
only learned models are a greedy interval rule and nearest-centroid. Two
analyses are needed to judge the risk:

1. **Capacity is not the binding constraint.** I measured the intent-only
   information ceiling: with the skewed prior and overlapping intent bands, the
   MAP/threshold rule on intent alone tops out at ≈87.4%, and `cam_learned`
   already achieves 87.5%. A logistic regression, GBM, or MLP on intent alone
   cannot exceed the single-feature Bayes rate, so **no stronger single-signal
   model would overturn the direction of F9.** The claim is information-limited,
   which is a genuine strength of the design.

2. **But family and information are confounded in the label.** The learned
   single-signal comparator is an axis-aligned interval classifier while the
   multi-signal comparator is nearest-centroid; the two differ in both estimator
   family and information set. The clean test is a *matched-family* ablation:
   nearest-centroid on intent only vs nearest-centroid on all three signals (and
   symmetrically, a nonlinear model like logistic regression / small GBM fit on
   1 and 3 signals). This would (a) show the NCC is near-optimal, removing the
   concern that a stronger learner changes conclusions, and (b) confirm F9 is
   driven by signal structure, not classifier family.

Verdict on missing comparators: completeness gap, not a threat to the headline.
Add two matched-family comparators; that closes it.

---

## Bootstrap-BCa — **CONCERN**

**The implementation is mathematically correct.** I verified `bca_ci`
(`cam_sim.py:1132`) line-by-line and by numerical replication:
- `z0 = Φ⁻¹(mean(boot < θ̂))` — the bias-correction term is the proportion of
  bootstrap means below the observed mean, correctly mapped through the normal
  quantile and correctly clamped to avoid ±∞.
- Acceleration is the jackknife (leave-one-out) skewness estimate
  `Σd³ / (6 (Σd²)^{3/2})` — correct.
- The adjusted percentiles
  `Φ(z0 + (z0+z)/(1 − a(z0+z)))` are the standard BCa formula, applied to
  `z_{α/2}` and `z_{1−α/2}` — correct.
- Resampling over the 50 seed-level total-profit values is the **right unit**:
  the estimand is the mean over independent seeds, and each seed value is
  itself a mean over 200 scenarios. This is an ordinary i.i.d. seed-level
  bootstrap, appropriately applied.

**Issue — B = 200 is too few, and the reported agreement is inside the
Monte-Carlo noise.** On an n = 50 skewed sample I measured the RNG-to-RNG
standard deviation of the CI endpoints at B = 200 to be ≈ $2.1 (lower) and
≈ $3.5 (upper), versus ≈ $0.6/$0.9 at B = 2000. The paper's headline robustness
claim is that BCa "confirms" the normal CIs "to within $1.4" — that is *smaller
than the B = 200 endpoint noise*, so the agreement is not evidence of anything.
Likewise the reported bias-correction magnitudes (|z0| ≤ 0.16) have a
Monte-Carlo standard deviation of ≈ 0.09 at B = 200: every reported z0 is within
~1.7 standard errors of zero and is not distinguishable from resampling noise.
This is benign here (the distributions are tight and the normal CI is already
adequate) but the paper should not cite it as confirmation.

**Issue — the wrong quantity is bootstrapped.** The paper's inferential claims
rest on *paired* contrasts (`cam_multisignal − cam_inferred`, p = 5.4e-46). Only
the *marginal* per-agent means are bootstrapped, so the BCa check never touches
the contrast that matters. Recommendation: bootstrap the paired differences (or
the contrast directly), use B ≥ 2,000 (10,000 for the reported tail/Bca
percentiles), and align §7.3's "Bootstrap BCa CIs confirm …" wording to what was
actually resampled.

---

## Label-Noise — **CONCERN**

**Implementation.** The corruption logic (`cam_sim.py:515-526`, `596-607`) flips
each label, with probability ε, to a **uniformly random other** of the five
remaining classes. This is symmetric, homoscedastic label noise.

**Why that is the benign case, and the finding is model-dependent.** Uniform
noise induces a predictable, graceful response: every class-conditional mean
shrinks toward the global mean by the same factor, class ordering is preserved,
and accuracy degrades smoothly. Real label noise is *class-conditional* and
boundary-concentrated — and the paper itself names the confusions that matter:
crisis↔decision and retention↔exploration. I ran the corrupted-label fit under
both models (ε ∈ {0, 0.1, 0.2, 0.3}, same calibration seed) and measured
resulting clean per-class recall:

| ε | uniform: crisis / retention recall | class-conditional: crisis / retention recall |
|---|-----------------------------------|-----------------------------------------------|
| 0.0 | 99.5 / 99.2 | 99.5 / 99.2 |
| 0.1 | 99.1 / 98.8 | 100.0 / 99.1 |
| 0.2 | 89.3 / 97.4 | 100.0 / 92.2 |
| 0.3 | **63.5** / 90.8 | 100.0 / **82.8** |

Neither noise model dominates: uniform noise devastates the *rare* classes
(crisis is 5% of samples, so contamination-in at ε = 0.3 exceeds the true
count), while confusable-pair noise specifically damages retention. Critically,
the *placement* of residual errors — which the paper correctly argues governs
profit (§8.3 F6) — changes with the noise model. A blanket "remarkably
label-robust up to ε = 0.3" is therefore not established for a realistic,
class-conditional corruption process; the reported multi-signal match floor of
84.9% could be materially different under boundary-concentrated noise. The study
also exercises only the *recalibrated* learners, not the default
`cam_multisignal_learned` fit. Fix: parameterize the corruption as an asymmetric
confusion matrix (e.g. flip mass concentrated on the documented confusable
pairs), and report per-class recall alongside match rate.

---

## Convergence — **CONCERN**

`run_convergence` (`cam_sim.py:1410`) declares a metric "stable" when the mean
over the **last 10 seeds** differs from the **overall mean** by < 5%. Three
failure modes:

1. **The first row is vacuous.** At N = 10, `vals[-10:]` is the entire sample, so
   the last-10 mean equals the overall mean identically — the diagnostic reports
   "stable from 10 seeds onward," but the N = 10 check is true by construction.
   The claim should start at N ≥ 20.
2. **The window is inside the reference.** The last 10 seeds are part of the
   overall mean, biasing the comparison toward agreement; the test is not
   independent.
3. **The criterion is scale-relative and ad hoc.** A fixed 5% of the mean is
   meaningless for a metric near zero (weakly guarded by the `abs(overall) <
   1e-9` branch) and indifferent to whether the series is drifting,
   oscillating, or stationary. It is not a convergence diagnostic in the
   MCMC/sampling sense (no R-hat, ESS, or stationarity test). A slow monotone
   drift can pass; the code never tests for trend.

The *conclusion* survives independently — at N = 20 the `cam_multisignal` mean is
already within ~1.2% of the N = 50 value, and the SE falls as σ/√N — but the
diagnostic as written overstates its own strength. Recommended: report the
standard error (or relative SE) as a function of N with a pre-registered
tolerance, and add a trend test (Spearman of the metric vs. seed index, or a
Geweke early-vs-late z-score). The 5% rule may remain as a secondary heuristic
once the first row is removed.

---

## Priority-Fixes

1. **Lead with the matched single-signal comparator** (`cam_learned`,
   +$50.01) instead of `cam_inferred` (+$101.87) in the abstract, §8.3 F9, §9.1,
   and §10; retain the larger number explicitly as the "naive hand-tuned
   baseline" effect.
2. **Correct the "Bayes rate" claim** in §9.1 — 98.9% is the equal-prior
   nearest-centroid accuracy (a lower bound); prior-weighted MAP is ≈99.2%.
3. **Add two matched-family comparators**: nearest-centroid on intent-only, and
   one nonlinear learner (logistic regression or small GBM) on 1 and 3 signals,
   to decouple estimator family from information set.
4. **Rebuild the BCa check**: B ≥ 2,000 (tail/Bca percentiles ≥ 10,000), applied
   to the **paired differences** that carry the claims, not only marginal means;
   drop or soften the "confirms within $1.4" claim at B = 200.
5. **Replace uniform label noise with a class-conditional confusion model**
   concentrated on crisis↔decision and retention↔exploration (the paper's own
   documented confusions), and report per-class recall.
6. **Fix the convergence diagnostic**: remove the trivially-stable N = 10 row,
   make the comparison window disjoint from the reference, and add an SE-vs-N
   curve plus a monotone-trend test.

---

## VERDICT

**CONCERNS** — the classifier, bootstrap, and noise implementations are
individually correct and the multi-signal direction is information-theoretically
robust, but the headline effect is roughly halved by the paper's own fairer
comparator, the B = 200 bootstrap is underpowered to the point of being
uninformative, and the label-noise and convergence stress tests answer narrower
questions than the text claims.
