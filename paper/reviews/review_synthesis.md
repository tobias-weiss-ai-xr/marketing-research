# Review Synthesis — CAM-Sim Academic Paper (v1.6)

**Paper:** `paper/g4_academic_paper.tex` (LaTeX) / `paper/g4_academic_paper.md` (Markdown source)
**Version Reviewed:** DRAFT v1.6, snapshot 2026-11-03
**Reviews:** 6 (R1-latex, R2-stats, R3-content, R4-repro, R5-priorart, R6-limits)
**Date of synthesis:** 2026-11-07
**Git commits:** `618d3e5` → `09f5cff` → `141f712` → `06fba26`

---

## Executive Summary

Six independent reviews were commissioned (via `af` agentflow with a 3-worker pool) covering LaTeX typography, statistical methodology, content/narrative structure, reproducibility, prior-art positioning, and threats to validity. **All critical-severity findings across all six reviews have been resolved.** All major findings have been resolved or explicitly warranted as not-applicable. A small number of minor/presentational items remain and are catalogued at the end of this document.

The paper compiles cleanly: **17 pages, 0 errors, 0 undefined references**, PDF ≈ 210 KiB.

---

## Review-by-Review Status

### R1-latex (typography & LaTeX structure) — Manual review (worker exceeded context window)

| # | Finding | Severity | Status |
|---|---------|----------|--------|
| 1 | `\Ag{}` macro corruption (69 occurrences) — underscore-fixer script ate first char of every argument | CRITICAL | ✅ RESOLVED (`618d3e5`) |
| 2 | Hardcoded `\S8.x`/`\S9.x`/`\S10.x` references (32) pointed to wrong sections | CRITICAL | ✅ RESOLVED (`618d3e5`) — replaced with `\S\ref{sec:...}` |
| 3 | Corrupted `\label{}` tags (4): Russell/Kotler/Peppers/Godin lost first letter | CRITICAL | ✅ RESOLVED (`618d3e5`) |
| 4 | Abstract numeric error: "+$103.10 learned-vs-learned" → "+$103.10 fitted-3-signal-vs-fitted-1-signal" | MAJOR | ✅ RESOLVED (`618d3e5`) |
| 5 | "7 environments" → "7 of 9 environments" (abstract) | MAJOR | ✅ RESOLVED (`618d3e5`) |
| 6 | "Round-3 Reviewer"/"Round-4 Adversarial" review-process artifacts in subsection titles | MAJOR | ✅ RESOLVED (`618d3e5`) |
| 7 | Overfull hboxes (174) — cosmetic, worst 203pt (12-col robustness table) | COSMETIC | ⏸ Deferred (camera-ready) |
| 8 | Underfull hboxes (293) — cosmetic | COSMETIC | ⏸ Deferred |
| 9-12 | `\Ag{cam_multisignal*}` asterisk, table widths, unused `\Fx` macro, unreferenced labels | MINOR | ⏸ No action / defer |

**R1 verdict:** Paper ready for submission; only cosmetic box warnings remain.

---

### R2-stats (statistical methodology) — No critical issues

| # | Finding | Severity | Status |
|---|---------|----------|--------|
| 1 | Bonferroni 610-way vs 630-way family inconsistency in LLM contrasts | MAJOR | ✅ RESOLVED — §8.21 keeps historical 610-way with explicit parenthetical (610-way threshold p<8.2e-05; full 630-way family p<7.9e-05); §7.3 notes "630 total family; §8.21 rows keep the historical 610-way annotation" (`09f5cff`/`618d3e5`) |
| 2 | d_z "simulation reproducibility" caveat not consistently applied | MAJOR | ✅ RESOLVED — caveat now at §7.3 ("d_z is a reproducibility index"), §8.1 table note (1.4–1.5× smaller), §8.5/§8.6 ("d_z = t/√50 ... measures simulation reproducibility"), §8.8 LR/RF ("reproducibility indices ... not generalizable") (`141f712` + `06fba26`) |
| 3 | Bootstrap BCa CI labeling (B=200 diagnostic vs B=2000 confirmatory) | MAJOR | ✅ ADDRESSED — text at §9.2.2 and §8.6 explicitly distinguishes; B=2000 paired-diff confirmed within $0.30 |
| 4 | p-value format inconsistency (MD vs TEX) | MINOR | ⏸ .md-only style; TEX uses `\pv{}`/`\pvl{}` consistently |
| 5 | z=1.96 vs t(49)=2.01 CIs | MINOR | ✅ ADDRESSED — §7.3 now justifies z=1.96 (consistency with BCa; t(49)=2.01 gives 2.5% wider intervals, no conclusion change) |
| 6 | Spearman ρ CI method unspecified | MINOR | ✅ ADDRESSED — §7.3 now specifies CI = 2.5–97.5 percentile of per-seed ρ distribution (matches code: `np.percentile(seed_rhos, [2.5,97.5])`) |
| 7 | Macro-recall definition not in methods | MINOR | ✅ ADDRESSED — §7.3 now defines macro-recall explicitly |
| 8 | Seed-1 sensitivity only for LLM results | MINOR | ✅ ADDRESSED — §8.21 justifies scope (LLM arms have 2–10 seeds; main ladder at 50 is insensitive) |
| 9 | Paired-design power discussion in limitations, not methods | MINOR | ✅ ADDRESSED — §7.3 now includes pairing rationale (fairness) + power note |
| 10 | "tie" informal language | MINOR | ✅ ADDRESSED — §8.21 to "statistically indistinguishable from cam_inferred (p = 0.70)"; qwen3.8 non-survival now explicit in .tex |

**R2 verdict:** Accept with minor revisions. Core methodology sound; Bonferroni, d_z, bootstrap CI labeling, and all 5 minor presentational items (z-vs-t, Spearman CI method, macro-recall, seed-1 scope, pairing power, "tie" language) now resolved in §7.3/§8.21.

---

### R3-content (content & narrative) 

| # | Finding | Severity | Status |
|---|---------|----------|--------|
| C1 | Hardcoded section numbering vs LaTeX numbering mismatch | CRITICAL | ✅ RESOLVED (`618d3e5`) — 32 `\S\ref{}` fixes |
| C2 | Abstract contradiction: "learned-vs-learned" vs actual +$103.10 (fitted-3 vs fitted-1) | CRITICAL | ✅ RESOLVED (`618d3e5`) |
| M1 | Abstract length (MD ~551 words labeled "150-200") | MAJOR | ✅ ADDRESSED — .tex abstract is 186 words (correct); .md header label corrected to ~550 words |
| M2 | "Round-3/Round-4" review-process artifacts | MAJOR | ✅ RESOLVED (`618d3e5`) |
| M3 | Redundant standalone "Findings" subsection | MAJOR | ✅ ADDRESSED — .tex integrates findings into results (only a bold "Findings." lead-in within §8.21); .md retains §8.3 Findings but this mirrors the .tex structure where F1-F9 appear in §8.1/§8.3 | 
| M4 | Future Work reads as completed-items changelog | MAJOR | ✅ RESOLVED (`141f712`) — restructured into "Planned work" (8 open items) vs "Completed extensions" (15 referenced items) |
| m1 | RQ answers not explicit | MINOR | ✅ RESOLVED (`141f712`) — added RQ1–RQ4 answer mapping in `§9.1` after H1–H4 |
| m4 | "7 environments" → "7 of 9 environments" | MINOR | ✅ RESOLVED (`618d3e5`) |
| m2/m3/m5/m6/m7 | Results subsection ordering, version roadmap, TL;DR vs abstract, gap repetition, RQ2 wording | MINOR | ⏸ Deferred / acceptable as-is |

**R3 verdict:** All critical + major narrative issues resolved. Paper now reads as a forward-looking contribution, not a review log.

---

### R4-repro (reproducibility) 

| # | Finding | Severity | Status |
|---|---------|----------|--------|
| 1 | `\Ag{}` truncation corrupts agent names / paths (reproducibility-critical identifiers) | CRITICAL | ✅ RESOLVED (`618d3e5`) |
| 2 | cam_inferred 75.0% vs 75.7% discrepancy | — | ✅ FALSE ALARM — task-description error; paper/code both 75.7% |
| 3 | LLM table missing provider prefixes (zai/, saia/, groq/, tud/, local/) | MAJOR | ✅ RESOLVED (`141f712`) — prefixes added to §8.21 LLM table; Model column widened 2.0→3.2cm |

**R4 verdict:** All reproducibility findings resolved. Paired-on-identical-sequences protocol documented; provider quotas disclosed per model.

---

### R5-priorart (prior art & positioning) 

| # | Finding | Severity | Status |
|---|---------|----------|--------|
| 1 | Situation types mismatch (LOYALTY/ONBOARDING vs CONSIDERATION/OPPORTUNITY) | CRITICAL | ✅ FALSE ALARM — paper/code both define EXPLORATION, CONSIDERATION, DECISION, CRISIS, OPPORTUNITY, RETENTION; LOYALTY is an ActionType, not a SituationType |
| 2 | "Zero papers" overstates evidence | CRITICAL | ✅ RESOLVED (`618d3e5`) — "no papers in our corpus" + terminological-gap caveat |
| 3 | Endsley Level 3 (projection) mapped but not benchmarked | MAJOR | ✅ ADDRESSED — already stated in 4 places (lines 107, 241, 279, 820); abstract makes no L3 claims |
| 4 | R&N agent function / agent-type taxonomy not addressed | MAJOR | ✅ RESOLVED (`3f2242e`+) — added §4.2 paragraph mapping CAM ladder to R&N agent types (simple-reflex, model-based, goal/utility-based, learning agents); explicit agent-function f: P* → A framing |
| 5 | Häglund positioning insufficient technical detail | MAJOR | ✅ RESOLVED (`141f712`) — expanded §3.4 with BERT-based aspect-sentiment classifiers, media-context effect estimation, context-aware content recommendation; explicit contrast with CAM's agentic decision layer |
| 6 | Situation types lack marketing-literature grounding | MAJOR | ✅ RESOLVED (`06fba26`) — added Lemon & Verhoef (2016) customer journey citation; framed taxonomy as contribution, not established theory; cross-ref to §8.20 confusion quantification |
| 7 | Differentiation from marketing automation systems (segmentation, journey orchestration, CDPs, RTB) | MAJOR | ✅ RESOLVED (`06fba26`) — added §5.3 paragraph positioning CAM as theoretical layer beneath commercial automation |
| 8-10 | Missing related works (Minsky, Maes, ReAct, etc.); thin theory foundation; external validity roadmap | MINOR | ⏸ Deferred / nice-to-have |

**R5 verdict:** All critical + major positioning issues resolved or refuted. Only R&N agent-function mapping (#4) remains as a candidate improvement.

---

### R6-limits (threats to validity) 

| # | Finding | Severity | Status |
|---|---------|----------|--------|
| 1 | Missing threat: synthetic benchmark generalization (no real-world validation) | CRITICAL | ✅ RESOLVED (`618d3e5`) — added limitation #26 |
| 2 | Missing threat: LLM temperature-0 non-determinism (API providers don't guarantee bitwise determinism) | CRITICAL | ✅ RESOLVED (`618d3e5`) — added limitation #27 |
| 3 | "No field validation" should be more prominent | CRITICAL | ✅ ADDRESSED — covered by #26 + field-validation design in §10.3 #1 |
| 4 | 200-scenario design diversity constrained by parametric generative model | MAJOR | ✅ RESOLVED (`618d3e5`) — added limitation #28 |
| 5 | 50 seeds may be underpowered for small/rare effects | MAJOR | ✅ RESOLVED (`06fba26`) — added power note (≥80% for d>0.4; underpowered for rare situations like crisis ~5% prevalence) |
| 6 | `\resolved{}` annotation quality | — | ✅ All 12 resolved annotations point to substantive empirical work |
| 7 | v1.6 arm-H "no fitted component" could conflate with "no training" | MINOR | ✅ RESOLVED (`06fba26`) — clarified: no task-specific fine-tuning; LLM carries pre-training biases |
| 8-14 | No-skill baseline, Bonferroni honesty, NCC simplification, fixed action mapping, 6-situation coverage, bid_calibrated ceiling, channel arbitrage | — | ✅ Adequately discussed (no action needed) |

**R6 verdict:** All critical + major threats addressed. Limitations section now has 28 items, each either resolved empirically or honestly open.

---

## Comprehensive Fix Log (commits)

### `618d3e5` — LaTeX review fixes
- 69 `\Ag{}` corruption fixes (root cause: `/tmp/fix_underscores3.py` missing `continue` after `break`)
- 4 corrupted `\label{}` tags restored (Russell, Kotler, Peppers, Godin)
- 32 hardcoded cross-references → `\S\ref{sec:...}` (added `sec:futurework` label)
- Abstract: "+$103.10 fitted-3-signal-vs-fitted-1-signal" (was "learned-vs-learned")
- Abstract: "7 of 9 environments" (was "7 environments")
- Removed "Round-3 Reviewer" / "Round-4 Adversarial" from subsection titles
- "Zero papers" → "no papers in our corpus" + terminological-gap caveat
- 3 threats to validity added (#26–28): synthetic generalization, LLM non-determinism, parametric scenario diversity
- `$\times$` math mode fix (was `\$\\times\$` text mode)

### `09f5cff` — R1-latex review + Bonferroni annotation
- Added `paper/reviews/review_latex.md` (manual review, worker context overflow)
- Clarified 610-way vs 630-way Bonferroni annotation in §8.21

### `141f712` — Content/narrative + reproducibility
- R3-M4: Future Work restructured → "Planned work" (8) + "Completed extensions" (15)
- R3-m1: RQ1–RQ4 answer mapping added to §9.1
- R3-M2: review-process references removed from acknowledgment/reproducibility notes
- R4-3: provider prefixes added to §8.21 LLM table; Model column widened
- R5-5: Häglund positioning expanded (§3.4)
- R2-2: d_z reproducibility caveat added to §8.8 LR/RF baselines
- Synced .md with .tex (zero-papers, Round-3/4, "7 of 9", threats #26–28)

### `06fba26` — Remaining major items
- R6-5: 50-seed power note (≥80% power for d>0.4; rare-situation caveat)
- R6-7: v1.6 arm-H "no fitted component" clarified (no task-specific fine-tuning; pre-training biases)
- R5-6: Lemon & Verhoef (2016) citation for situation taxonomy; framed as contribution
- R5-7: Marketing automation differentiation paragraph added to §5.3
- .md synced throughout; abstract header label corrected

---

## Remaining Open Items (all minor / deferred)

1. **R1-7/8 (overfull underfull hboxes)** — overfull reduced from 174 → 73 with worst from 203pt → 54pt by converting worst tables to `table*`/`\resizebox`; remaining warnings are all inside resized tables (absorbed in output). Underfull boxes remain (cosmetic).
2. **R5-8/9/10 (expansion of related work, theory synthesis, external-validity roadmap)** — nice-to-have for a longer-format venue.
3. **.md sync drift** — the .md still contains §8.3 standalone Findings (mirrors .tex F1–F9 which live inline) and the richer ~550-word abstract; both are intentional .md conveniences, not publication artifacts.

---

## Final Assessment

The paper is **ready for submission** (17 pages, 0 errors, 0 undefined references). **All 6 reviews' critical and major findings are resolved.** The remaining open items are presentational or candidate-v1.7 enhancements. The review cycle caught and fixed a systematic `\Ag{}` corruption (reproducibility-critical), 32 wrong cross-references, 2 factual abstract errors, review-process artifacts, overclaiming language, and 3 missing threats to validity.
