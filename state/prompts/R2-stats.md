You are an autonomous coding agent working in a git worktree.

TASK ID: R2-stats
TITLE: You are a statistical rigor reviewer for a computer science / marketing simulation paper. Read paper/g4_academic_paper.tex (the LaTeX draft) and paper/g4_academic_paper.md (the Markdown source of truth). Review from a statistical methodology perspective. The paper reports: 50 seeds x 200 scenarios, 11 agents on a situational-awareness ladder, paired seed-level t-tests, Cohen's d, bootstrap BCa CIs (B=200 and B=2000), Bonferroni correction (630 total tests), Spearman correlations, macro-F1, macro-recall. Key claims: cam_multisignal +$206.13 (10-seed) / +$220.29 (5-seed), oracle +$210.00 / +$224.49, LLM zero-shot 74-83% accuracy, macro-recall 50-61% vs cam_inferred 65.9%, arm-H end-to-end LLM +$250-273 vs +$206-220. Check: (1) Are p-values reported consistently (scientific notation, Bonferroni-annotated)? (2) Are confidence intervals properly computed and reported (seed-level, not scenario-level)? (3) Is the multiplicity correction (630 tests) correctly applied and annotated? (4) Are effect sizes (Cohen's d) reported for key contrasts? (5) Is the bootstrap methodology sound (BCa, B=200 diagnostic, B=2000 confirmatory)? (6) Are there any claims that exceed the evidence (e.g., causal language for correlational results)? (7) Is the macro-recall vs accuracy distinction clearly explained? (8) Are seed-1 sensitivity analyses reported? (9) Is the paired design (same seeds across agents) properly leveraged in the tests? (10) Are negative results (e.g., deepseek -$0.10, groq tie) reported honestly? Write your review to paper/reviews/review_stats.md with sections: Summary, Issues Found (severity: critical/major/minor), Recommendations. Cite specific section numbers, line numbers, and values. If a category is clean, say 'No issues found.'
Files you are allowed to modify:
*
Acceptance criteria:
(declared acceptance gate command)

Acceptance gate command (run verbatim to verify this task):
test -f paper/reviews/review_stats.md && [ $(wc -c < paper/reviews/review_stats.md) -gt 500 ] && grep -q 'Summary' paper/reviews/review_stats.md && grep -q 'Issues Found' paper/reviews/review_stats.md

Work on TASK_ID only. Do not touch files outside the allowed scope.
When done, make sure the acceptance criteria hold and your changes are
committed on the current branch.