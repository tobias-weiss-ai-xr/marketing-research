You are an autonomous coding agent working in a git worktree.

TASK ID: R1-latex
TITLE: You are a LaTeX typography and compilation reviewer. Read paper/g4_academic_paper.tex (981 lines, compiles with tectonic 0.17.0/XeTeX to 16 pages, 0 errors). Also read paper/g4_academic_paper.md (the Markdown source of truth, 864 lines). Review from a LaTeX/typography perspective. Check: (1) Table formatting — do all tables use booktabs correctly (toprule/midrule/bottomrule), are column specs valid, do multicolumn spans match cmidrule ranges, are tablenotes properly formatted? (2) Cross-references — do all \ref targets have matching \label definitions, are there undefined references or multiply-defined labels? (3) Math notation — are all math commands inside $...$ or equation environments, are there any bare \alpha/\beta/\rho/\times/\le/\in outside math mode? (4) Macros — are \finding, \pv, \pvl, \ci, \Ag, \srho, \tnote, \resolved, \Fx used correctly and consistently? (5) Spacing — are there overfull/underfull hboxes/vboxes that affect readability (check the .log if available)? (6) Consistency — are agent names (cam_inferred, cam_multisignal, etc.) consistently formatted (\Ag{} in text, plain in math)? (7) Abstract/TL;DR — does the abstract fit the two-column layout properly? (8) Appendix — are appendices properly structured with \appendix? (9) Any remaining encoding issues (stray tabs, control chars, non-UTF8)? (10) Are the 20 tables (table*/table environments) all referenced in text? Write your review to paper/reviews/review_latex.md with sections: Summary, Issues Found (severity: critical/major/minor/cosmetic), Recommendations. Be specific — cite line numbers and exact LaTeX commands. If you find no issues in a category, say 'No issues found.'
Files you are allowed to modify:
*
Acceptance criteria:
(declared acceptance gate command)

Acceptance gate command (run verbatim to verify this task):
test -f paper/reviews/review_latex.md && [ $(wc -c < paper/reviews/review_latex.md) -gt 500 ] && grep -q 'Summary' paper/reviews/review_latex.md && grep -q 'Issues Found' paper/reviews/review_latex.md

Work on TASK_ID only. Do not touch files outside the allowed scope.
When done, make sure the acceptance criteria hold and your changes are
committed on the current branch.