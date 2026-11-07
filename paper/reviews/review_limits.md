# Review of Limitations and Threats to Validity (CAM-Sim v1.6)

**Paper:** CAM-Sim: A Reproducible Benchmark for Situational-Awareness Ablations in Marketing Agents  
**Version:** v1.6 (snapshot 2026-11-03)  
**Reviewer:** Limitations and Threats-to-Validity Review  
**Date:** 2026-11-03

---

## Summary

This review evaluates the 25 limitations listed in §9.2 (Discussion) of the CAM-Sim paper, the \resolved{} annotation mechanism, and identifies additional threats to validity that should be addressed. The paper demonstrates strong transparency in acknowledging limitations and provides substantive resolutions for most through empirical ablations. However, several important threats to validity are either under-discussed or missing entirely.

**Overall Assessment:** The limitations section is comprehensive and well-structured. Most \resolved{} annotations point to genuine empirical work rather than hand-waving. However, 6 of the 10 candidate missing threats identified in this review warrant explicit acknowledgment.

---

## Issues Found

### Critical Severity

#### 1. Missing Threat: Synthetic Benchmark Generalization (§9.2 incomplete)
**Issue:** While §9.2 #12 notes that "profit is a scaled-reward proxy" and §9.2 #7 acknowledges "author-selected" environments, the paper does not explicitly state that the **entire synthetic benchmark may not generalize to real marketing platforms**. The reward function, situation taxonomy, and action space are all author-designed constructs.

**Location:** §9.2 #7, #12; §10.3 #1 (field validation deferred)

**Recommendation:** Add explicit limitation stating that CAM-Sim's synthetic environment, while internally consistent, has not been validated against real marketing platform data. The field-validation design (§10.3 #1) is pre-specified but not yet executed.

---

#### 2. Missing Threat: LLM Temperature-0 Non-Determinism (§8.21 incomplete)
**Issue:** §8.21 states LLMs run at "temperature 0" but does not acknowledge that **API responses at temperature 0 are still not guaranteed to be bitwise deterministic** across calls. The paper notes "providers do not guarantee bitwise determinism at temperature 0" (§8.21 scope) but this should be elevated to a formal limitation.

**Location:** §8.21 (scope paragraph)

**Recommendation:** Add as §9.2 limitation: "LLM zero-shot baseline uses temperature 0, but API providers do not guarantee determinism; reproducibility requires response caching."

---

#### 3. Missing Threat: No Real-World Validation (§9.2 #1, #3 acknowledge but defer)
**Issue:** The paper explicitly defers field validation to future work (§10.3 #1), but this should be more prominently flagged as a **critical limitation** rather than buried in the "resolved" annotations. The claim that "external validity requires field validation" (§9.2 #1) is honest but the absence of any field data is a fundamental constraint on the paper's claims.

**Location:** §9.2 #1, §10.3 #1

**Recommendation:** Elevate this to a standalone limitation or strengthen the language in #1 to emphasize that ALL findings are simulation-only.

---

### Major Severity

#### 4. Missing Threat: 200-Scenario Design Diversity (§9.2 silent)
**Issue:** The paper does not discuss whether the **200 scenarios per seed provide sufficient diversity** to represent the marketing situation space. The scenarios are generated from a fixed parametric model (Gaussian clusters with specified means/SDs), which may not capture real-world complexity.

**Location:** Not discussed

**Recommendation:** Add limitation acknowledging that scenario diversity is constrained by the generative model's parametric assumptions.

---

#### 5. Missing Threat: 50 Seeds May Be Insufficient (§9.2 #10, #17 partial)
**Issue:** While §9.2 #10 notes "seed pairing is fair but low-power" and #17 addresses convergence, the paper does not explicitly state that **50 seeds may be insufficient for detecting small effects or for certain subgroups** (e.g., rare situations like crisis at ~5% prevalence).

**Location:** §9.2 #10, #17

**Recommendation:** Strengthen #17 to explicitly note that 50 seeds provides ~80% power only for large effects (d > 0.4); smaller effects or rare-situation analyses may be underpowered.

---

#### 6. Resolved Annotation Quality: Mixed
**Assessment of \resolved{} annotations:**

| Limitation | Resolution Location | Substantive? |
|------------|---------------------|--------------|
| #1 (circularity) | §8.11 adversarial mapping | ✅ Yes - empirical falsification test |
| #4 (perception/bid confound) | §8.15 flat-bid dose-response | ✅ Yes - clean ablation |
| #10 (seed pairing) | §8.9 CRN check | ✅ Yes - empirical check |
| #11 (match rate) | §8.9 macro-F1 | ✅ Yes - alternative metric |
| #13 (missing comparators) | §8.8 + §8.12 | ✅ Yes - LR/RF/bandit baselines |
| #15 (bootstrap B=200) | §8.6 B=2000 paired-diff | ✅ Yes - improved bootstrap |
| #16 (label noise) | §8.13 class-conditional | ✅ Yes - realistic noise model |
| #17 (convergence) | §8.14 Spearman/Geweke | ✅ Yes - trend diagnostics |
| #18 (flat taxonomy) | §8.20 confusion quantification | ✅ Yes - empirical quantification |
| #23 (crisis mapping) | §8.16 pause vs counter | ✅ Yes - policy comparison |
| #24 (decoy signal) | §8.17 sensing fidelity | ✅ Yes - ablation test |
| #25 (channel arbitrage) | §8.10 channel-dependent reward | ✅ Yes - sensitivity analysis |

**Assessment:** All 12 \resolved{} annotations point to **substantive empirical work**, not hand-waving. This is a strength of the paper.

---

### Minor Severity

#### 7. v1.6 Arm-H Results Caveating (§8.22 adequate but could be clearer)
**Issue:** The v1.6 arm-H results (LLM end-to-end +$250-273) are caveated as "no fitted component" but the caveat that **the LLM is still a pre-trained model with its own training data biases** could be more explicit.

**Location:** §8.22, Abstract

**Assessment:** The paper does note "pre-trained LLM" in Table A.2 and the abstract states "without any fitted component." This is **adequate but borderline**—a reader might conflate "no fitted component" with "no training whatsoever."

**Recommendation:** Add explicit note that "no fitted component" means no task-specific fine-tuning, but the LLM carries pre-training biases from its original training corpus.

---

#### 8. No-Skill Baseline Discussion (§8.21 adequate)
**Issue:** The "big-3 80.3% accuracy" no-skill baseline is discussed in §8.21: "a no-skill classifier sampling the funnel trio (exploration 36.5% + consideration 30.4% + decision 13.4% = 80.3% of contexts) by base rate scores 80.3%."

**Assessment:** This is **properly discussed** and used to contextualize LLM accuracy claims. No issue found.

---

#### 9. Bonferroni Failures Reported Honestly (§8.21, §9.2.1)
**Issue:** Check whether qwen3.6 p=8.1e-03 FAILS after correction is reported honestly.

**Assessment:** **Yes, reported honestly.** §8.21 states: "qwen3.6-35b's nominal +$0.10 vs cam_inferred (p = 8.1e-03; does not survive 610-way Bonferroni correction) is not a reliable win." §9.2.1 also notes the near-equivalence caveat "does not survive Bonferroni at α/565."

**No issue found** - the paper is transparent about which results survive correction.

---

#### 10. Nearest-Centroid Classifier Simplification (§9.2 #14 adequate)
**Issue:** Whether the nearest-centroid classifier being a simplification of real ML classifiers is adequately discussed.

**Assessment:** §9.2 #14 states: "Classifier family = generative family. 98.9% is a lower bound, not the Bayes rate." §8.8 benchmarks LR and RF, showing RF achieves 100% match and "slightly beats NCC (+$3.66)."

**Assessment:** **Adequately discussed.** The paper explicitly benchmarks alternative classifiers and acknowledges NCC's relationship to the generative model.

---

#### 11. Fixed Action-to-Situation Mapping (§9.2 #1, #23 adequate)
**Issue:** Whether the fixed action-to-situation mapping limitation is adequately discussed.

**Assessment:** §9.2 #1 addresses "reward-design circularity" and the situation→ideal-action table being author-designed. §9.2 #23 addresses the crisis action mapping specifically. §8.11 tests a "deranged mapping" to show the benchmark can falsify wrong mappings.

**Assessment:** **Adequately discussed** with empirical validation.

---

#### 12. Six Situations Coverage (§9.2 #18 adequate)
**Issue:** Whether the 6 situations covering the full marketing situation space is addressed.

**Assessment:** §9.2 #18 explicitly states: "Six situations conflate three constructs... A practitioner would model these as orthogonal axes (stage × condition), not a flat 6-way taxonomy." The limitation is acknowledged and quantified in §8.20.

**Assessment:** **Adequately discussed.**

---

#### 13. bid_calibrated Ceiling Artifact (§9.2 #2, #20 partial)
**Issue:** Whether the bid_calibrated ceiling (+$530.45) being an artifact of the synthetic reward function is adequately discussed.

**Assessment:** §9.2 #2 states bid_calibrated "provides the true ceiling" but notes "Remaining: a learned bidding policy and auction-style clearing." §9.2 #20 states "bid_calibrated is given the mechanism — an omniscience no practitioner has" and "the calibrated ceiling (+$530) is an artifact of mechanism knowledge."

**Assessment:** **Adequately discussed** — the paper is clear that bid_calibrated is an upper bound, not a deployable agent.

---

#### 14. Channel-Cost Arbitrage Reward-Design Sensitivity (§9.2 #25 adequate)
**Issue:** Whether channel-cost arbitrage revealing reward-design sensitivity is discussed.

**Assessment:** §9.2 #25 explicitly addresses this: "Channel-cost arbitrage... the environment's reward function does not penalize wrong-channel assignments, so the cheapest channel dominates." §8.10 tests a channel-dependent reward condition that eliminates the arbitrage.

**Assessment:** **Adequately discussed** with empirical sensitivity analysis.

---

## Recommendations

### Must Address (Critical)

1. **Add explicit limitation on synthetic benchmark generalization** (§9.2 new item or strengthen #7/#12): State clearly that CAM-Sim's findings are simulation-only and have not been validated against real marketing platform data.

2. **Add explicit limitation on LLM temperature-0 non-determinism** (§9.2 new item): Note that API providers do not guarantee determinism even at temperature 0, and reproducibility depends on response caching.

3. **Elevate "no field validation" to prominent limitation** (§9.2 #1 or new item): Make clearer that ALL empirical claims are from simulation, with field validation explicitly deferred.

### Should Address (Major)

4. **Add limitation on 200-scenario diversity** (§9.2 new item): Acknowledge that scenario diversity is constrained by the parametric generative model.

5. **Strengthen §9.2 #17 on seed count** to explicitly note power limitations for small effects and rare situations.

6. **Consider adding limitation on 50-seed statistical power** for subgroup analyses (e.g., per-situation performance).

### Nice to Address (Minor)

7. **Clarify v1.6 arm-H caveat** to explicitly note that "no fitted component" does not mean "no training" — the LLM carries pre-training biases.

8. **Consider adding a summary table** of all 25 limitations with resolution status (Resolved/Partial/Open) for reader convenience.

---

## Categories with No Issues Found

- **Limitation numbering and distinctness:** All 25 limitations are clearly numbered and distinct. ✓
- **\resolved{} annotation substantiveness:** All 12 resolved annotations point to genuine empirical work. ✓
- **No-skill baseline discussion:** Properly contextualized in §8.21. ✓
- **Bonferroni failure reporting:** Honestly reported (qwen3.6 p=8.1e-03 explicitly noted as failing correction). ✓
- **Nearest-centroid simplification:** Adequately discussed in §9.2 #14 with LR/RF benchmarks. ✓
- **Fixed action-to-situation mapping:** Adequately discussed in §9.2 #1, #23 with adversarial test. ✓
- **Six situations coverage:** Adequately discussed in §9.2 #18 with confusion quantification. ✓
- **bid_calibrated ceiling:** Adequately discussed in §9.2 #2, #20 as an upper bound. ✓
- **Channel-cost arbitrage sensitivity:** Adequately discussed in §9.2 #25 with §8.10 resolution. ✓

---

## Conclusion

The CAM-Sim paper demonstrates **strong transparency** in its limitations section. The 25 limitations are well-organized, and the \resolved{} mechanism is used appropriately to point to substantive empirical work. The primary gaps are **missing threats** rather than mischaracterized ones: synthetic benchmark generalization, LLM non-determinism, and scenario diversity should be explicitly acknowledged. The field-validation design (§10.3 #1) is concrete enough to be actionable (specifies ≥40 campaigns/arm, 8-12 weeks, mixed-effects analysis), but its absence remains a critical limitation until executed.

**Recommendation:** Address the 3 critical and 2-3 major issues above before publication. The paper's honest treatment of limitations is a strength that should be maintained and extended.
