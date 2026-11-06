# Statistical Methodology Review: CAM-Sim Benchmark Paper

**Reviewer:** Statistical Rigor Reviewer  
**Date:** 2026-11-07  
**Target Document:** `paper/g4_academic_paper.tex` (LaTeX draft) and `paper/g4_academic_paper.md` (Markdown source)

---

## Summary

This paper presents CAM-Sim, a paired-seed benchmark (50 seeds × 200 scenarios) for evaluating situational-awareness ablations in marketing agents. The statistical methodology is generally sound and well-documented, with appropriate use of paired t-tests, bootstrap confidence intervals, and multiplicity corrections. The authors have addressed many methodological concerns through iterative revisions (5 review rounds including stats-audit and ml-methodology reviews). Key strengths include the paired design leveraging common random numbers, explicit reporting of both p-values and effect sizes, and transparent acknowledgment of limitations (e.g., B=200 bootstrap being underpowered, later addressed with B=2000 paired-difference bootstrap).

The paper reports extensive statistical results: 630 total tests with Bonferroni correction, Cohen's d effect sizes, bootstrap BCa CIs, Spearman correlations for environment consistency, and macro-F1 for per-class evaluation. Most claims are appropriately qualified, and negative results (e.g., DeepSeek -$0.10, Groq tie) are reported honestly.

However, several issues require attention, ranging from minor inconsistencies in p-value annotation to potential over-interpretation of some effect sizes. The review below details findings by severity.

---

## Issues Found

### Critical Severity

**No critical issues found.** The core statistical methodology is sound, and the authors have appropriately addressed major concerns through revisions (e.g., paired-difference bootstrap B=2000 in §8.6, explicit caveats about simulation vs. sampling inference).

---

### Major Severity

#### 1. Inconsistent Bonferroni Annotation for LLM Results (§8.21, §8.22; MD lines 587-595; TEX lines 679-700)

**Issue:** The paper reports 630 total tests but uses "610-way Bonferroni correction" for the LLM baseline contrasts. The threshold is stated as p < 8.2e-05 (0.05/610), but the total family is now 630 tests (0.05/630 = 7.9e-05). This is a minor numerical inconsistency but creates confusion about which correction applies.

**Location:** 
- MD line 587: "does not survive 610-way Bonferroni correction"
- MD line 595: "survives the 610-way Bonferroni correction (threshold p < 8.2e-05)"
- TEX line 700: "surviving 610-way Bonferroni (threshold $p < 8.2\times10^{-5}$)"
- TEX line 792: "All p-values survive Bonferroni (630 total family; §7.3); §8.21 rows keep the historical 610-way annotation"

**Recommendation:** Update all LLM contrast annotations to reference the correct 630-test family (threshold p < 7.9e-05) or explicitly state that the 610-way threshold is conservative. The TEX line 792 acknowledgment helps but should be more prominent in the results section.

#### 2. Cohen's d Interpretation Ambiguity (§7.3; MD lines 289, 332; TEX lines 320-322)

**Issue:** The paper reports both d_pooled (between-group) and d_z (paired within-subject), noting d_z is "1.4-1.5× smaller." However, the interpretation of d_z as "simulation reproducibility, not generalization" (MD line 436, TEX line 521) is not consistently applied. Some findings present d_z values without this caveat, potentially misleading readers about effect size generalizability.

**Location:**
- MD line 289: "Cohen's d (between-group pooled, d_pooled) for effect size; paired within-subject d_z = |t|/√n is 1.4–1.5× smaller"
- MD line 332: "Cohen's d is between-group pooled (d_pooled). Paired within-subject d_z values are 1.4–1.5× smaller."
- MD line 436: "d_z is t/√50 from a deterministic paired comparison, so it measures simulation reproducibility, not generalization"
- TEX line 320: "Cohen's d (between-group pooled, d$_{pooled}$) for effect size; paired within-subject d$_z$ = $\vert t\vert / \sqrt{n}$ is 1.41--1.5x smaller"

**Specific examples without consistent caveat:**
- cam_multisignal vs cam_inferred: d_z = 7.88 (MD line 332, TEX line 398) — caveat present
- LR-3 vs LR-1: d_z = 6.03 (MD line 494) — no caveat
- RF-3 vs RF-1: d_z = 5.17 (MD line 494) — no caveat
- RF vs NCC: d_z = 1.35 (MD line 496) — no caveat

**Recommendation:** Add the "simulation reproducibility" caveat to all d_z interpretations in §8.8 (standard classifier baselines) and §8.10-§8.17 (v1.3 extensions), not just the headline contrasts.

#### 3. Bootstrap BCa CI Reporting Inconsistency (§9.2.2; MD lines 665, 428; TEX lines 326, 506, 795-796)

**Issue:** The paper states B=200 bootstrap is "diagnostic, not confirmatory" due to Monte-Carlo noise of ≈$2-3.5, yet reports BCa CIs alongside normal-approximation CIs in Table 2 (TEX line 398) without clearly distinguishing which is which. The paired-difference bootstrap (B=2000) in §8.6 is confirmatory but only covers three headline contrasts, not all 11 agents.

**Location:**
- MD line 665: "Bootstrap BCa CIs (200 resamples per agent; `--bootstrap 200`)... Caveat (§9.2 #15): B = 200 produces Monte-Carlo endpoint noise of ≈$2–3.5"
- MD line 428: "Paired-difference bootstrap (B = 2000)... confirmatory check"
- TEX line 326: "Bootstrap BCa CIs (B = 200 resamples; Section~\ref{sec:bootstrap}) as non-parametric check on normal approximation (diagnostic, not confirmatory)"
- TEX line 795-796: "Bootstrap BCa CIs (200 resamples): check normal-approx CIs within \$1.4... Caveat: B = 200 has Monte-Carlo endpoint noise of $\approx$\$2--3.5"

**Recommendation:** 
1. Clearly label Table 2 CIs as "normal-approximation" with a footnote referencing the paired-difference bootstrap confirmation in §8.6.
2. Consider extending the B=2000 paired-difference bootstrap to all key contrasts (not just the three headline ones) for full confirmatory coverage.

---

### Minor Severity

#### 4. P-Value Scientific Notation Format Inconsistency (§7.3; MD lines 286-287; TEX lines 319-332)

**Issue:** P-values are reported in multiple formats:
- Scientific notation with LaTeX macro: `\pv{8.5\!\times\!10^{-32}}` (TEX line 64)
- Inline scientific notation: `p = 8.5e-32` (MD line 46)
- Threshold notation: `p < 1e-04` (MD line 595)
- Plain notation: `p = 0.034` (MD line 516)

While all are valid, the paper should standardize on one format for consistency. The TEX file uses `\pv{}` and `\pvl{}` macros (e.g., `\pv{5.4\!\times\!10^{-46}}`), but the MD file mixes formats.

**Location:**
- MD line 46: "p = 8.5e-32"
- MD line 286: "p-values reported in scientific notation"
- MD line 516: "rho = -0.301 (p = 0.034, marginally significant)"
- TEX line 64: "\pv{8.5\!\times\!10^{-32}}"
- TEX line 319-332: Table with `\pv{}` macro

**Recommendation:** Standardize on scientific notation for all p < 0.001 (e.g., p = 8.5×10⁻³² or p = 8.5e-32 consistently) and plain decimal for p ≥ 0.001. Ensure MD and TEX files match.

#### 5. Confidence Interval Width Justification (§7.3; MD line 332; TEX line 383)

**Issue:** The paper notes "CIs use z = 1.96; the t(49) equivalent is 2.01 (2.5% wider)" but uses z-based CIs throughout. With n=50 seeds, the t-distribution is more appropriate, though the difference is small (2.5%). This is acknowledged but the choice is not justified beyond brevity.

**Location:**
- MD line 332: "CIs use z = 1.96; the t(49) equivalent is 2.01 (2.5% wider)"
- TEX line 383: "\tnote{95\% CIs use z = 1.96; t(49) = 2.01 gives marginally wider intervals.}"

**Recommendation:** Either switch to t-based CIs (more conservative, standard for n=50) or add a brief justification for z-based CIs (e.g., "z-based CIs reported for consistency with bootstrap BCa intervals; t-based CIs are 2.5% wider and do not affect conclusions").

#### 6. Spearman Correlation CI Reporting (§8.4; MD lines 370, 624; TEX lines 456-458)

**Issue:** The paper reports Spearman ρ values with mean and range (e.g., "0.94–0.99 across all nine environments, with every lower CI bound ≥ 0.93") but does not specify the CI method (Fisher z-transformation? Bootstrap?). The per-seed ρ computation is clear, but the CI aggregation method is not.

**Location:**
- MD line 370: "reported as mean [95% CI]: 0.94–0.99 across all nine environments, with every lower CI bound ≥ 0.93"
- MD line 624: "per-seed Spearman ρ(match rate, profit) 0.94–0.99 across all 9 environments, every 95% CI lower bound ≥ 0.93"
- TEX line 456-458: Table with ρ column but no CI details

**Recommendation:** Specify the CI method for Spearman ρ (e.g., "95% CIs computed via Fisher z-transformation on per-seed ρ values") in §7.3 or §8.4.

#### 7. Macro-Recall vs Accuracy Distinction (§8.21; MD lines 595, 603; TEX lines 679-706)

**Issue:** The distinction is explained but could be clearer. The paper states "raw accuracy (74–83%) is inflated by class imbalance" and "macro-recall 50–61% vs 65.9%," but the mechanistic explanation (no-skill funnel-trio sampler scores 80.3%) appears only in findings, not in the methods section.

**Location:**
- MD line 595: "raw accuracy (74–83%) is inflated by class imbalance — a no-skill classifier sampling the funnel trio... scores 80.3%"
- MD line 603: "macro-recall 50–61% vs cam_inferred 65.9%"
- TEX line 700: "Raw accuracy (74--83\%) is inflated by class imbalance (a no-skill funnel-trio sampler scores 80.3\%)"

**Recommendation:** Move the class-imbalance inflation explanation to §7.4 (Metrics) or add a cross-reference from §8.21 to §7.4. Define macro-recall explicitly (mean of per-class recall) in the methods section.

#### 8. Seed-1 Sensitivity Analysis Scope (§8.21; MD line 595; TEX line 704)

**Issue:** Seed-1 sensitivity is reported only for LLM accuracy (dropping seed 1 shifts accuracy by -0.3 to -3.5pp), not for profit contrasts or other key metrics. The analysis is labeled "dev-on-test check" but is not applied to the main agent ladder.

**Location:**
- MD line 595: "seed-1 sensitivity (dev-on-test check, computed from the response cache): dropping seed 1 shifts accuracy only slightly..."
- TEX line 704: "seed-1 sensitivity (dev-on-test). Dropping seed 1: glm 79.9→79.6, Mistral 80.3→79.7..."

**Recommendation:** Either extend seed-1 sensitivity analysis to profit contrasts for the main agent ladder (cam_multisignal, cam_learned, etc.) or explicitly state why it's only reported for LLM results (e.g., "LLM results have smaller seed counts (2-10 seeds) and thus higher sensitivity to individual seeds").

#### 9. Paired Design Power Analysis (§7.3; MD line 285; TEX line 334)

**Issue:** The paper notes "seed-level correlation between baseline and agents is near zero (−0.23 to +0.08); pairing buys no power advantage" (MD line 794, TEX line 794) but this appears only in limitations, not in the methods section where the paired design is justified.

**Location:**
- TEX line 794 (limitations): "Seed pairing is fair but low-power. Seed-level correlation between baseline and agents is near zero ($-$0.23 to +0.08); pairing buys no power advantage."

**Recommendation:** Move this observation to §7.3 (Statistical Methods) with a note that pairing is retained for fairness (same scenarios) rather than power, and that the design is adequately powered despite low correlation (n=50 seeds provides >99% power for the observed effect sizes).

#### 10. Negative Results Reporting — Groq Tie (§8.21; MD line 595; TEX line 700)

**Issue:** The paper reports "qwen3.8-27b's −$0.01 (p = 0.70, tie)" but the term "tie" is informal. The result is correctly reported as non-significant, but the language could be more precise (e.g., "not significantly different from zero" or "statistically equivalent within CI bounds").

**Location:**
- MD line 595: "qwen3.8-27b's −$0.01 (p = 0.70, tie)"
- TEX line 700: Not explicitly mentioned (only in MD)

**Recommendation:** Replace "tie" with "not significantly different from cam_inferred (p = 0.70)" or report the 95% CI for the contrast to show it includes zero.

---

## Recommendations

### High Priority

1. **Standardize Bonferroni annotation:** Update all LLM contrast references from "610-way" to "630-way" Bonferroni correction, or add a prominent note explaining the historical 610-way annotation is conservative.

2. **Add d_z caveats consistently:** Ensure all Cohen's d_z interpretations include the "simulation reproducibility, not generalization" caveat, not just the headline contrasts.

3. **Clarify bootstrap CI labeling:** Distinguish diagnostic (B=200) from confirmatory (B=2000) CIs in tables and text. Consider extending B=2000 to all key contrasts.

### Medium Priority

4. **Standardize p-value format:** Choose one scientific notation format (e.g., 8.5×10⁻³² or 8.5e-32) and apply consistently across MD and TEX files.

5. **Justify z-based CIs:** Either switch to t-based CIs (t(49) = 2.01) or add explicit justification for z-based CIs in §7.3.

6. **Specify Spearman CI method:** Add the CI computation method (Fisher z-transformation or bootstrap) for Spearman ρ in §7.3 or §8.4.

### Low Priority

7. **Clarify macro-recall vs accuracy:** Move the class-imbalance inflation explanation to the methods section (§7.4) and define macro-recall explicitly.

8. **Extend seed-1 sensitivity:** Apply seed-1 sensitivity analysis to profit contrasts for the main agent ladder, or explain why it's limited to LLM results.

9. **Relocate pairing power discussion:** Move the seed-pairing power observation from limitations to §7.3 with appropriate context.

10. **Formalize "tie" language:** Replace informal "tie" terminology with precise statistical language (e.g., "not significantly different").

---

## Categories with No Issues Found

- **Confidence interval computation level:** CIs are correctly computed at the seed level (n=50), not scenario level (n=10,000). The paper explicitly states "seed-level paired t-tests" (§7.3, MD line 285) and "per-seed differencing" (MD line 516).

- **Multiplicity correction application:** The 630-test family is correctly enumerated (§7.3, MD line 293; TEX line 328), and all confirmatory p-values are noted to survive Bonferroni correction. The annotation is consistent except for the 610 vs 630 discrepancy noted above.

- **Bootstrap methodology soundness:** The BCa bootstrap is correctly described with bias-correction (|z₀| ≤ 0.16) and acceleration (|acceleration| ≤ 0.014) diagnostics. The B=200 limitation is acknowledged and addressed with B=2000 paired-difference bootstrap.

- **Causal language:** The paper appropriately uses correlational language ("associated with," "predicts") and explicitly states "The environment and all agents are deterministic given the seed; the only randomness is the seed. Reported p-values... quantify simulation reproducibility across seeds, not sampling error from a population" (§7.3, TEX line 337-339).

- **Negative results honesty:** DeepSeek's -$0.10 (p = 4.9e-06) is reported as "significantly negative" (MD line 595), and the Groq/qwen3.8-27b tie is reported with p = 0.70. The channel-cost arbitrage finding (context-blind policy beats context-aware) is reported transparently as a "benchmark-construction limitation" (§8.7).

- **Paired design leverage:** The paired design is correctly leveraged with `scipy.stats.ttest_rel` (paired t-test) for all agent-vs-baseline comparisons (§7.3, MD line 285; TEX line 319). The paired-difference bootstrap (§8.6) correctly resamples seed-level differences, not marginal means.

---

## Overall Assessment

**Rating:** Accept with Minor Revisions

The paper demonstrates strong statistical rigor with appropriate methods for a simulation-based benchmark. The authors have proactively addressed methodological concerns through multiple review rounds, and the remaining issues are primarily presentational (standardization of notation, clarification of caveats) rather than substantive. The core findings are well-supported by the data, and the limitations are honestly acknowledged.

**Key strengths:**
- Paired design with common random numbers
- Explicit multiplicity correction (630 tests)
- Both p-values and effect sizes reported
- Bootstrap BCa CIs with diagnostics
- Negative results reported honestly
- Simulation vs. sampling inference clearly distinguished

**Key areas for improvement:**
- Standardize Bonferroni annotation (610 vs 630)
- Consistent d_z interpretation caveats
- Clearer bootstrap CI labeling (diagnostic vs confirmatory)
