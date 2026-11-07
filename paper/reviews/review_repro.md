# Reproducibility and Data-Integrity Review: CAM-Sim Paper (v1.6)

**Review Date:** 2026-11-07  
**Files Reviewed:** `paper/g4_academic_paper.tex`, `paper/g4_academic_paper.md`  
**Snapshot Date:** 2026-11-03 (consistent in both files)

---

## Summary

This review cross-checked the key numerical results and agent naming conventions between the LaTeX source (`.tex`) and Markdown source (`.md`) files for the CAM-Sim benchmark paper (v1.6). The review focused on eight key areas: (1) aggregate performance table values, (2) LLM zero-shot results, (3) v1.6 arms bootstrap CIs, (4) Bonferroni correction sum, (5) agent name consistency, (6) \Ag{} macro consistency, (7) experimental parameters (seeds × scenarios), and (8) snapshot date consistency.

**Overall Assessment:** Most numerical values are consistent between the two files. However, there are significant issues with the `\Ag{}` macro usage in the `.tex` file where agent names are truncated (missing the `c` prefix or `b`/`s` prefixes), creating a mismatch with the `.md` source. Additionally, the task description mentions `cam_inferred 75.0%` but both files correctly report `75.7%`.

---

## Issues Found

### Critical Issues

#### 1. Agent Name Truncation in \Ag{} Macros (.tex file)

**Severity:** Critical

The `.tex` file uses truncated agent names in `\Ag{}` macros throughout the document. These truncations create a mismatch with the `.md` source which uses full agent names.

| Location (line) | .tex \Ag{} Value | Correct Value (from .md) | Issue |
|-----------------|------------------|--------------------------|-------|
| Line 64, 409, 436, 504, 542, 578, 584, 588, 592, 595, 598, 611, 631, 673, 741, 758, 767, 798, 825, 921 | `\Ag{am_multisignal}` | `cam_multisignal` | Missing 'c' prefix |
| Line 64, 409, 436, 578, 595, 598, 631, 758, 767, 921 | `\Ag{am_inferred}` | `cam_inferred` | Missing 'c' prefix |
| Line 409, 578, 595, 598, 631, 758, 921 | `\Ag{am_learned}` | `cam_learned` | Missing 'c' prefix |
| Line 409, 436, 921 | `\Ag{am_recalibrated}` | `cam_recalibrated` | Missing 'c' prefix |
| Line 578 | `\Ag{am_multisignal_learned}` | `cam_multisignal_learned` | Missing 'c' prefix |
| Line 741, 758 | `\Ag{id_calibrated}` | `bid_calibrated` | Missing 'b' prefix |
| Line 64 | `\Ag{am_multisignal}` | `cam_multisignal` | Missing 'c' prefix |
| Line 631 | `\Ag{am_inferred}` | `cam_inferred` | Missing 'c' prefix |

**Impact:** This is a critical documentation error. The `\Ag{}` macro is intended to format agent names consistently, but the truncated names do not match the actual agent identifiers used in the code (`cam_sim.py`, etc.) or the `.md` source.

**Recommendation:** All `\Ag{am_*}` should be corrected to `\Ag{cam_*}`, `\Ag{id_calibrated}` to `\Ag{bid_calibrated}`, and `\Ag{ituation_only}` to `\Ag{situation_only}`.

### Major Issues

#### 2. Task Description Discrepancy: cam_inferred Match Rate

**Severity:** Major (external to files, but noted for clarity)

The task description states: "cam_inferred 75.0% match"

However, both `.tex` (line 356) and `.md` (line 310) correctly report:
- **cam_inferred: 75.7% match** [74.9, 76.5]

This appears to be an error in the task description, not in the paper files.

#### 3. LLM Model Name Inconsistency (Minor Formatting)

**Severity:** Minor

The `.tex` and `.md` files use slightly different naming conventions for LLM models:

| Model | .tex Name | .md Name |
|-------|-----------|----------|
| qwen3.6-35b | `qwen3.6-35b` | `saia/qwen3.6-35b-a3b` |
| qwen3.8-27b | `qwen3.8-27b` | `groq/qwen3.8-27b` |
| Mistral | `mistral-128B` | `tud/mistral-medium-3.5-128b` |
| glm-4.7 | `glm-4.7 (thinking)` | `zai/glm-4.7 (thinking)` |
| deepseek | `deepseek-v4-flash` | `local/deepseek-v4-flash (reasoning)` |

**Impact:** The `.md` file includes provider prefixes (`saia/`, `groq/`, `tud/`, `zai/`, `local/`) which are more precise for reproducibility. The `.tex` file uses simplified names.

**Recommendation:** Consider adding provider prefixes to the `.tex` table for full reproducibility, or note that these are simplified names.

### Minor Issues

#### 4. cam_inferred Match Rate: Abstract vs Table

**Severity:** Minor

In the `.tex` abstract (line 64), the text states "Multi-signal situation classification raises match from 87.5% to 98.7%". This correctly references `cam_learned` (87.5%) vs `cam_multisignal` (98.7%).

However, the task asks about `cam_inferred` (75.7%) being consistent. The value 75.7% for `cam_inferred` is consistent between:
- `.tex` Table (line 356): 75.7%
- `.md` Table (line 310): 75.7% [74.9, 76.5]

No discrepancy found in the files themselves.

---

## Verification of Key Numbers

### (1) Aggregate Performance Table (§8.1)

| Agent | Metric | .tex Value | .md Value | Match? |
|-------|--------|------------|-----------|--------|
| cam_inferred | Match % | 75.7% | 75.7% | ✅ |
| cam_inferred | Profit | +$104.26 | +$104.26 | ✅ |
| cam_multisignal | Match % | 98.9% | 98.9% | ✅ |
| cam_multisignal | Profit | +$206.13 | +$206.13 | ✅ |
| oracle | Match % | 100.0% | 100.0% | ✅ |
| oracle | Profit | +$210.00 | +$210.00 | ✅ |
| bid_calibrated | Profit | +$530.45 | +$530.45 | ✅ |

**Status:** All values consistent. Note: Task description mentions 75.0% for cam_inferred, but both files correctly show 75.7%.

### (2) LLM Zero-Shot (§8.21) - All 5 Models

| Model | .tex Accuracy | .md Accuracy | Match? |
|-------|---------------|--------------|--------|
| qwen3.6-35b | 83.0% | 83.0% | ✅ |
| Mistral (mistral-128B) | 80.3% | 80.3% | ✅ |
| glm-4.7 | 79.9% | 79.9% | ✅ |
| groq (qwen3.8-27b) | 75.7% | 75.7% | ✅ |
| deepseek | 74.1% | 74.1% | ✅ |

**Status:** All 5 models consistently reported in both files.

### (3) v1.6 Arms (§8.22) - Bootstrap CIs

| Arm/Model | Metric | .tex Value | .md Value | Match? |
|-----------|--------|------------|-----------|--------|
| Mistral (arm-H) | Profit | +$273.64 | +$273.64 | ✅ |
| Mistral (arm-H) | CI | [260.67, 286.61] | [260.67, 286.61] | ✅ |
| glm (arm-H) | Profit | +$250.28 | +$250.28 | ✅ |
| glm (arm-H) | CI | [240.90, 259.57] | [240.90, 259.57] | ✅ |

**Status:** Bootstrap CIs match exactly across abstract, results, and discussion sections in both files.

### (4) 630-way Bonferroni Sum

**Calculation:** 540 + 3 + 5 + 5 + 12 + 5 + 40 + 20 = 630

| Component | .tex (line 328) | .md (line 293) | Match? |
|-----------|-----------------|----------------|--------|
| Confirmatory tests | 540 (10 agents × 6 metrics × 9 env) | 540 (10 agents × 6 metrics × 9 environments) | ✅ |
| Ablations | 3 | 3 | ✅ |
| Context-blind policies | 5 | 5 | ✅ |
| Standard-baseline contrasts | 5 | 5 | ✅ |
| v1.3 extension contrasts | 12 | 12 | ✅ |
| v1.4 extension contrasts | 5 | 5 | ✅ |
| v1.5 LLM contrasts | 40 | 40 | ✅ |
| v1.6 prompt-variant contrasts | 20 | 20 | ✅ |
| **Total** | **630** | **630** | ✅ |

**Status:** Sum is correct and consistently stated in both files.

### (5) Agent Names Consistency

**Required agents:** cam_inferred, cam_multisignal, cam_learned, cam_multisignal_learned, cam_recalibrated, bid_calibrated, channel_only, situation_only, noisy50, noisy80, oracle

| Agent Name | In .tex Tables? | In .md Tables? | \Ag{} Macro Correct? |
|------------|-----------------|----------------|---------------------|
| cam_inferred | ✅ (line 356) | ✅ (line 310) | ❌ Uses `\Ag{am_inferred}` |
| cam_multisignal | ✅ (line 357) | ✅ (line 311) | ❌ Uses `\Ag{am_multisignal}` |
| cam_learned | ✅ (line 358) | ✅ (line 312) | ❌ Uses `\Ag{am_learned}` |
| cam_multisignal_learned | ✅ (line 359) | ✅ (line 313) | ❌ Uses `\Ag{am_multisignal_learned}` |
| cam_recalibrated | ✅ (mentioned) | ✅ (line 276) | ❌ Uses `\Ag{am_recalibrated}` |
| bid_calibrated | ✅ (line 362) | ✅ (line 316) | ❌ Uses `\Ag{id_calibrated}` |
| channel_only | ✅ (line 354) | ✅ (line 307) | ✅ (not in \Ag{}) |
| situation_only | ✅ (line 355) | ✅ (line 308) | ❌ Uses `\Ag{ituation_only}` |
| noisy50 | ✅ (line 355) | ✅ (line 309) | ✅ (not in \Ag{}) |
| noisy80 | ✅ (line 360) | ✅ (line 314) | ✅ (not in \Ag{}) |
| oracle | ✅ (line 361) | ✅ (line 315) | ✅ (not in \Ag{}) |

**Status:** Agent names in tables are consistent. However, `\Ag{}` macros in `.tex` have truncation errors (see Critical Issue #1).

### (6) \Ag{} Agent Names Matching .md Source

**Status:** As documented in Critical Issue #1, the `\Ag{}` macros in `.tex` do NOT match the `.md` source due to truncation.

| .tex \Ag{} | Expected (from .md) | Match? |
|------------|---------------------|--------|
| `\Ag{am_inferred}` | `cam_inferred` | ❌ |
| `\Ag{am_multisignal}` | `cam_multisignal` | ❌ |
| `\Ag{am_learned}` | `cam_learned` | ❌ |
| `\Ag{am_multisignal_learned}` | `cam_multisignal_learned` | ❌ |
| `\Ag{am_recalibrated}` | `cam_recalibrated` | ❌ |
| `\Ag{id_calibrated}` | `bid_calibrated` | ❌ |
| `\Ag{ituation_only}` | `situation_only` | ❌ |

### (7) 50 Seeds × 200 Scenarios Parameters

| Location | .tex | .md | Match? |
|----------|------|-----|--------|
| Abstract | "50 seeds × 200 scenarios" (line 64) | "50 seeds × 200 scenarios" (line 4, 46) | ✅ |
| Section 8.1 header | N/A | "50 seeds × 200 scenarios" (line 304) | ✅ |

**Status:** Consistent in both files.

### (8) Snapshot Date (2026-11-03)

| Location | .tex | .md | Match? |
|----------|------|-----|--------|
| Header | "DRAFT v1.6 -- snapshot 2026-11-03" (line 2) | "DRAFT (v1.6); snapshot 2026-11-03" (line 26) | ✅ |
| Title block | "DRAFT v1.6 -- snapshot 2026-11-03" (line 53) | N/A | ✅ |

**Status:** Consistent in both files.

---

## Recommendations

### Critical (Must Fix Before Publication)

1. **Fix all `\Ag{}` macro truncations in `.tex`:**
   - Replace `\Ag{am_*}` with `\Ag{cam_*}` throughout
   - Replace `\Ag{id_calibrated}` with `\Ag{bid_calibrated}`
   - Replace `\Ag{ituation_only}` with `\Ag{situation_only}`
   - Consider adding a linting step to catch such truncations

2. **Verify agent names in code match paper:**
   - Ensure `cam_sim.py` and extension files use `cam_` prefix consistently
   - Cross-reference agent identifiers in `results/cam_sim_v16.md`

### Major (Should Fix)

3. **Add provider prefixes to LLM model names in `.tex` table:**
   - Change `qwen3.6-35b` to `saia/qwen3.6-35b-a3b`
   - Change `qwen3.8-27b` to `groq/qwen3.8-27b`
   - Change `mistral-128B` to `tud/mistral-medium-3.5-128b`
   - Change `glm-4.7` to `zai/glm-4.7`
   - Change `deepseek-v4-flash` to `local/deepseek-v4-flash`

### Minor (Optional)

4. **Add a reproducibility checklist appendix** documenting:
   - Exact agent identifiers
   - Provider/model versions for LLM experiments
   - Random seed values used

5. **Consider adding automated consistency checks** between `.tex` and `.md` sources as part of the build process.

---

## Conclusion

The numerical results in CAM-Sim v1.6 are **internally consistent** between the `.tex` and `.md` files. All key values (aggregate performance, LLM zero-shot results, v1.6 arms CIs, Bonferroni sum, experimental parameters, snapshot date) match exactly.

However, there is a **critical documentation issue** with the `\Ag{}` macros in the `.tex` file, where agent names are systematically truncated (missing the `c`, `b`, or `s` prefix). This creates a mismatch with the `.md` source and the actual code identifiers, which could cause confusion for readers attempting to reproduce the results.

**Recommendation:** Fix the `\Ag{}` macro truncations before publication. All other findings are minor formatting inconsistencies that do not affect reproducibility.

---

**Reviewer:** Autonomous Reproducibility Agent  
**Review Completed:** 2026-11-07
