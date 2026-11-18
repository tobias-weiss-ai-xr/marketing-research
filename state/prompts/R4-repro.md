You are an autonomous coding agent working in a git worktree.

TASK ID: R4-repro
TITLE: You are a reproducibility and data-integrity reviewer. Read paper/g4_academic_paper.tex and paper/g4_academic_paper.md. The paper cites results from CAM-Sim (paper/cam_sim.py v0.4 + extensions: paper/cam_sim_extensions.py, paper/cam_sim_v14.py, paper/cam_sim_v15_llm.py, paper/cam_sim_v16_arms.py). Key numbers to cross-check: (1) Aggregate performance table (§8.1): cam_inferred 75.0% match +$104.26, cam_multisignal 98.9% +$206.13, oracle 100% +$210.00, bid_calibrated +$530.45 — do these appear consistently in abstract, TL;DR, and results? (2) LLM zero-shot (§8.21): 5 models (qwen3.6-35b 83.0%, Mistral 80.3%, glm-4.7 79.9%, groq 75.7%, deepseek 74.1%) — are all 5 consistently reported? (3) v1.6 arms (§8.22): arm-H mistral +$273.64 [260.67, 286.61], glm +$250.28 [240.90, 259.57] — do the bootstrap CIs match across abstract, results, and discussion? (4) The 630-way Bonferroni: 540+3+5+5+12+5+40+20=630 — is this sum correct and consistently stated? (5) Agent names: cam_inferred, cam_multisignal, cam_learned, cam_multisignal_learned, cam_recalibrated, bid_calibrated, channel_only, situation_only, noisy50, noisy80, oracle — are these consistent between .tex and .md? (6) Are all \Ag{} agent names in the .tex matching the .md source? (7) Are the 50 seeds x 200 scenarios parameters stated consistently? (8) Is the snapshot date (2026-11-03) consistent? Write your review to paper/reviews/review_repro.md with sections: Summary, Issues Found (severity: critical/major/minor), Recommendations. List every discrepancy you find with exact values from .tex vs .md. If everything matches, say 'No discrepancies found.'
Files you are allowed to modify:
*
Acceptance criteria:
(declared acceptance gate command)

Acceptance gate command (run verbatim to verify this task):
test -f paper/reviews/review_repro.md && [ $(wc -c < paper/reviews/review_repro.md) -gt 500 ] && grep -q 'Summary' paper/reviews/review_repro.md && grep -q 'Issues Found' paper/reviews/review_repro.md

Work on TASK_ID only. Do not touch files outside the allowed scope.
When done, make sure the acceptance criteria hold and your changes are
committed on the current branch.