# Statistical Audit — `paper/g4_academic_paper.md`

**Scope:** statistical claims in the G4 CAM paper; internal consistency, statistical
validity, and methodology-code match against `paper/cam_sim.py` (v0.4).
**Method:** read the paper in full; ran the self-check; re-ran the default and
robustness/stress-test pipelines from the paper's own command; re-derived every
reported CI, p-value and effect size from the emitted data. **The paper and the
code were not modified.**

## Summary

The paper's quantitative core is **faithful to the code and reproducible**. Every
headline number I checked re-runs byte-for-byte from the documented command:

| Claim | Paper | Reproduced |
|---|---|---|
| baseline profit | −$170.03 | −170.03 |
| `cam_multisignal` | +$206.13 @ 98.9% | +206.13 @ 98.9% |
| oracle | +$210.00 | +210.00 |
| `bid_calibrated` | +$530.45, ROAS 26.4 | +530.45, ROAS 26.367 |
| §8.2 profit diffs / CIs / p / d (all 10 agents) | — | exact match |
| §8.4 nine-environment table, ρ CIs, F3 p-values | — | exact match |
| §8.5.1 α-sweep, §8.5.2 label-noise, §8.5.3 pacing | — | exact match |

`python paper/cam_sim.py --self-check` prints `[OK]`; `--seeds 1,2,3 --scenarios 20
--quiet` exits 0. The statistics code does what §7.3 says: paired
`scipy.stats.ttest_rel` across seeds, 95% CIs as mean ± 1.96·SE, aggregate ROAS.

However, there are real **internal inconsistencies** (abstract vs body, prose vs
tables) and **statistical-presentation concerns** (the reported "Cohen's d" is not
the paired effect size; the pairing does not behave as advertised). None of these
invalidate the qualitative conclusions. Verdict: **CONCERNS**.

## Internal Consistency

- **Abstract vs body paper count.** §2 says "70 papers, +1.8×"; §3.1, §5.1, the
  §5 heading and the title standfirst all say **61 papers / 1.79×**. The generated
  pipeline output `docs/research/trends.md` currently reports `agentic | 64 | 70 |
  1.8×`, so the abstract is current and the body is **stale** — but as printed the
  paper contradicts itself. The §5.1 category breakdown (28/15/8/5/5 = 61) is stale
  for the same reason.
- **§5.2 category counts do not sum.** AI-Marketing 22 + Digital 8 + Analytics 5 +
  Privacy 3 + B2B 2 = **40**, while the section and §3.1 state **44** contextual
  papers. No caveat (unlike §5.1) flags the breakdown as unverified.
- **§9.1 H2 contradicts §8.1/F4.** H2 claims "all context-aware agents profitable",
  but `channel_only` is context-aware bidding and loses **−$110.16**; §8.3 F4 says
  exactly that. H1 is correctly scoped ("situation-aware"); H2 is not.
- **§8.3 F1 is directionally wrong for `channel_only`.** F1: "Every context-aware
  agent significantly outperforms baseline on match rate …". Reproduced,
  `channel_only`'s match rate is **−6.2 pp below baseline** (15.4 vs 21.6,
  p = 8.3e-15) — significant, but in the *opposite* direction. F1's conjunction is
  false for the bid-only ablation.
- **§8.4 F6 "within $0.4" is false.** The gap between `cam_multisignal` and
  `cam_multisignal_recalibrated` is 0.14–0.75 in 8 presets and **1.79** under
  `concave_returns`; 5 of 9 exceed $0.4. The correct claim is "within ~$1.8".
- **Abstract scope slip.** §2 attributes "returns-to-bid curvatures α ∈ [0, 1.5]" to
  the nine-environment sweep. The 9 presets contain only `concave_returns` (α = 0.5);
  the α ∈ {0, .25, .5, .75, 1, 1.5} sweep is a separate stress test (§8.5.1).
- **§5.1 "Zero papers combine agentic + contextual"** vs §5.3 "Only 2 papers …
  mention both". The paper explains the two as "superficial", but the literal
  statements conflict.

Everything else is consistent: abstract ↔ §8.1 ↔ §8.3 ↔ §8.4 ↔ §9 ↔ §10 all agree
on the ladder, the F3/F5/F6/F9 numbers, the 8/9 orderings, the $3.87 oracle gap,
and the density/pacing/α results.

## Statistical Validity

- **CIs are mean ± 1.96·SE — yes.** `aggregate_seeds` uses `mean ± 1.96·sd/√n`;
  `compute_statistics` uses `diff_mean ± 1.96·sd_diff/√n`. Reproduced CIs match to
  reported precision. Note the mixed convention: **CIs use the normal z = 1.96 while
  p-values use the t distribution (df = 49)**. At n = 50 the discrepancy is
  negligible, but it should be one or the other.
- **p-values are plausible — yes, exactly.** With n = 50 paired seeds,
  t = diff_mean / (CI-half-width/1.96); reconstructing p from the printed CIs
  reproduces every §8.2 p to within ~2% (rounding). E.g. `noisy50`:
  t = 41.75, reconstructed p = 5.8e-40 vs printed 6.7e-40. The effect sizes are
  large enough that the p-values are not surprising.
- **"Cohen's d" is the wrong standardized effect for this design.** The code computes
  `d = Δmean / sqrt((var_a + var_b)/2)` — a **between-group pooled d**, not the
  paired `d_z = Δmean / sd_diff`. Because the paired differences are only weakly
  correlated (see next point), the printed d is **1.3–1.5× larger than d_z**:

  | agent | printed d (pooled) | paired d_z | corr(baseline, agent) |
  |---|---|---|---|
  | channel_only | 2.37 | 1.55 | −0.17 |
  | situation_only | 22.57 | 16.17 | +0.06 |
  | noisy50 | 8.57 | 5.89 | −0.06 |
  | cam_inferred | 11.98 | 8.05 | −0.13 |
  | cam_multisignal | 16.65 | 10.78 | −0.23 |
  | cam_learned | 13.89 | 9.27 | −0.14 |
  | cam_multisignal_learned | 16.64 | 10.83 | −0.22 |
  | noisy80 | 13.16 | 8.90 | −0.10 |
  | oracle | 16.74 | 10.84 | −0.23 |
  | bid_calibrated | 34.66 | 24.77 | +0.08 |

  The printed d *is* self-consistent with the §8.1 group CIs (I recovered each d
  from them to ±0.01). The issue is labeling/presentation: the headline
  "d = 9–35" (§9.2) is a between-group d presented next to paired tests and paired
  CIs. d_z = 5.9–24.8 is the honest paired figure and is still enormous.
- **Fair pairing does not deliver its promised benefit.** §7.1 justifies pairing as
  "removing the scenario-draw confound and legitimizing seed-level paired tests".
  The confound is indeed removed (contexts are generated once per seed), but the
  measured seed-level correlation between baseline and each agent is **−0.23 to
  +0.08** — near zero, mostly negative. For a shared-environment paired design one
  expects *positive* correlation; here the paired test has essentially no power
  advantage over an unpaired test (and is marginally weaker where correlation is
  negative). Likely cause: every agent draws from a **single global stdlib `random`
  stream seeded once per seed**, so agent *k* sees the stream after agents 1…k−1 have
  consumed it, and the shared-context "difficulty" component is small relative to
  each agent's own action randomness. The paired t-test remains *valid*, but the
  stated rationale overstates what pairing buys.
- **The central F9 claim has no direct test.** §8.3/§9.1 report the multisignal
  gain with "p = 1.4e-52 vs baseline" — a baseline comparison, not
  `cam_multisignal − cam_inferred`. I computed the missing direct paired test:
  **+$101.87, 95% CI [+98.3, +105.5], p = 5.4e-46, d_z = 4.2** — so the claim holds
  strongly, but the printed p is the wrong contrast. Likewise "within $4 of the
  oracle" hides that the residual gap is statistically significant
  (+$3.87, p = 1.3e-13).
- **Multiplicity is unaddressed.** 10 agents × 6 metrics vs baseline, and 9
  environments × paired F3 tests, are reported without correction. At these p-values
  it does not change any conclusion, but the paper should say so.
- **`noisy50`/`noisy80` understate perception.** On a miss, `NoisyCAM` re-draws
  uniformly over all 6 situations — *including the true one* — so effective accuracy
  is `p + (1−p)/6` (≈58.3% / 83.3%), not 50% / 80%. The observed match rates
  (59.6% / 83.7%) confirm this. The labels are approximate.

## Methodology-Code Match

**Excellent.** Every §7.1 / Appendix A agent maps to a class in `cam_sim.py`:
`baseline`→`BaselineAgent`, `channel_only`→`ChannelOnly`, `situation_only`→
`SituationOnly`, `noisy50/80`→`NoisyCAM(p)`, `cam_inferred`→`CAMInferred`, `oracle`→
`CAMOracle`, `cam_learned`→`CAMLearned`, `cam_multisignal`→`CAMMultisignal`,
`cam_multisignal_learned`→`CAMMultisignalLearned`, `bid_calibrated`→
`BidCalibratedAgent` (env-aware branch in `run_env`), `BudgetPacedAgent`→
`BudgetPacedAgent` (used by `run_budget_pacing_study`). `cam_recalibrated` /
`cam_multisignal_recalibrated` are correctly described as per-environment refits
(extra factories), not registry agents. Appendix A.1 details (9 presets, calib seed
999999, 2,000 samples, greedy interval splits, ε grid, α grid, 0.02/0.001 bid grid,
determinism) all match the source. The self-check confirms byte-reproducibility, as
claimed.

One framing gap: `MULTISIGNAL_CENTROIDS` are **exactly the true generative means**
(`SITUATION_CHANNEL_QUALITY`, `SITUATION_COMPETITIVE_DENSITY`, and the intent
strengths), so the hand-set `cam_multisignal` is configured with the ground-truth
centroids. The code comment acknowledges this; the paper calls it a "realistic
three-signal classifier" (§7.1, §9.1). The *learned* variant
(`cam_multisignal_learned`, 98.7%) is the legitimate evidence that the structure is
recoverable from data, and it matches — but the hand-set 98.9% should not be
presented as an independent classifier result. Also, `cam_learned` is described as
"Bayes-optimal given intent"; a greedy top-down classifier capped at 5 splits is an
approximation, not a proven optimum.

## Findings

1. **(Moderate) Abstract/body paper count mismatch:** abstract "70 papers" vs body
   "61 papers"; `docs/research/trends.md` says 70, so the body is stale. Also
   infects the §5.1 category breakdown.
2. **(Moderate) §5.2 contextual category counts sum to 40, not the stated 44.**
3. **(Moderate) §9.1 H2 ("all context-aware agents profitable") contradicts the
   §8.1 `channel_only` = −$110.16 result.**
4. **(Moderate) §8.3 F1 is false for `channel_only`:** its match rate is significantly
   *below* baseline (−6.2 pp), not above.
5. **(Moderate) §8.4 F6 "within $0.4" is false:** actual `cam_multisignal` ↔
   `cam_multisignal_recalibrated` gaps reach $1.79 (5/9 presets exceed $0.4).
6. **(Minor) Abstract attributes α ∈ [0, 1.5] curvature variation to the 9-preset
   sweep**, which only contains α = 0.5.
7. **(Moderate) Reported "Cohen's d" is a between-group pooled d, not the paired
   d_z**, inflation 1.3–1.5×; headline "d = 9–35" should be d_z 5.9–24.8 or reframed.
8. **(Moderate) Seed pairing yields near-zero/negative correlations (−0.23…+0.08)**,
   so the "fair pairing legitimizes paired tests" justification overstates the
   design's power; shared global RNG is the likely cause.
9. **(Minor/presentation) F9 is tested only against baseline (p = 1.4e-52); the
   direct `cam_multisignal − cam_inferred` test is +$101.87, p = 5.4e-46**, and the
   $3.87 oracle gap is itself significant (p = 1.3e-13).
10. **(Moderate, framing) `cam_multisignal` hand-set centroids equal the true
    generative means**; its "realistic classifier" framing is too strong. The learned
    variant carries the real evidence.
11. **(Minor) "Bayes-optimal" claim for `cam_learned`** is not established for a
    greedy ≤5-split interval rule.
12. **(Minor) `noisy50/80` effective perception is p + (1−p)/6 (≈58%/83%)**, so the
    graded-perception labels understate reality.
13. **(Minor) CI uses z = 1.96, p-values use t(df = 49);** and no multiplicity
    correction is reported across agents/metrics/environments.

**Strengths:** all headline numbers, all table values, all p-values, all CI widths
and all robustness/stress-test results reproduce exactly from the documented
command; the pipeline is deterministic and self-checking; the code implements the
described statistical methods correctly. The concerns above are about labeling,
stale prose, and the paired-design framing — not about fabricated or wrong numbers.

## VERDICT

**CONCERNS** — every simulated statistic reproduces exactly and the methodology
matches the code, but the paper carries several stale/incorrect internal claims
(70-vs-61 papers, 40-vs-44 categories, F1/H2 direction, F6 "within $0.4") and
presents a between-group Cohen's d alongside a paired design whose seed
correlations are near zero/negative.
