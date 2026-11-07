# Content & Narrative Review — CAM-Sim Academic Paper (R3-content)

**Files reviewed:** `paper/g4_academic_paper.tex` (L = line numbers below) and `paper/g4_academic_paper.md` (M = line numbers below, the declared "source of truth").
**Paper structure (per .md):** Abstract (§2), Introduction (§3), Theoretical Foundation (§4), Related Work (§5), CAM Framework (§6, Sensing Layer = §6.2), Research Design (§7), Results (§8.1–§8.22, 22 subsections), Discussion (§9; limitations 1–25 in §9.2 plus 9.2.1/9.2.2), Conclusion (§10), Appendix A (implementation), Appendix B (raw data).

---

## Summary

CAM-Sim is substantively strong and a genuine contribution: a reproducible paired-seed benchmark for situational-awareness ablations in marketing agents, with a clean ladder of eleven agents, nine environments, an honest discussion of reward-design circularity, and an unusually complete set of reviewer-motivated extensions (matched-family ablation, standard classifier baselines, adversarial mapping, bandit baselines, LLM zero-shot baseline, and end-to-end LLM agency). The **narrative arc is clear** (problem → theory → framework → method → results → discussion → conclusion), the **discussion is well balanced** (25-item limitations list that is largely self-resolved, plus practical and theoretical implications), and the **conclusion contains a concrete, pre-specified field-validation design**. The Results-to-Discussion `F1–F11` finding labels are an effective scaffolding, and the honest framing of the oracle / `bid_calibrated` ceilings is a model of scholarly restraint.

The review, however, found **one critical structural defect** that affects the entire document — the `.tex` and `.md` use two different section-numbering schemes, and the `.tex`'s hardcoded cross-references (which match the `.md` numbering) point to the wrong sections in the compiled PDF — plus **one critical/major abstract-vs-body numeric contradiction** and several major/minor content issues (abstract length and file divergence, review-history artifacts embedded in the body, redundancy in the Findings subsection and the Future Work ledger, and minor RQ-answer and result-ordering gaps). None of the issues undermine the underlying science or its main claims; they are presentation, consistency, and structure problems that should be fixed before submission.

---

## Issues Found

### Critical

**C1. Cross-reference / numbering scheme is broken in the compiled `.tex`.**
The `.md` hand-numbers Title/Abstract as §§1–2, so its Results = §8, Discussion = §9, Conclusion = §10, with **22** Results subsections (§8.1–§8.22). The `.tex` is compiled by LaTeX, which numbers Introduction = §1 and **Results = §6, Discussion = §7, Conclusion = §8, Appendix A = §9, Appendix B = §10**, and it has only **20** Results subsections (the `.tex` merges the `.md`'s `8.3 Findings` into §8.1–8.3 and its `8.5 Stress Tests` into §8.3). The `.tex` nevertheless hard-codes the `.md`'s numbers in dozens of places, e.g. `\S8.5.3` (L771), `\S8.7`–`\S8.22` (L545, L758), `\S9.2` (L545, L771, L758), `\S10.3` (L853), `\S7.3` (L322). In the compiled PDF these all resolve to the wrong section (a §8.x pointer lands in *Conclusion*; §9.2 lands in *Appendix A*; §10.3 in *Appendix B*), and some point to subsections that do not exist in the `.tex` at all (e.g., `§8.5.3` budget pacing is in the `.tex`'s §8.3, not 8.5.3). The `.tex` even mixes styles — a few refs use proper `\ref{sec:...}` (L85, L241, L274, L326, L394) while most use hard-coded `\S` — so the compiled numbering will be internally contradictory. **Fix:** either restore the `.md`'s 22-subsection Results layout in the `.tex` (re-add a labeled `Findings` subsection and a `Stress Tests` subsection) and convert *every* cross-reference to `\label`/`\ref`, or renumber the `.md` to match the compiled `.tex`. This is the single most important structural fix before resubmission.
*(Sections: §8 (Results) and all of §9/§10; .tex L64, L322, L545, L758, L771, L799, L843–853; .md L348, L374, L601, L727.)*

**C2. Abstract contradicts the body on the headline "matched-family / learned-vs-learned" gain.**
The `.md` abstract (M46) and `.tex` abstract (L64) report the matched-family ablation as `+$103.85 (p=5.16e-46); +$103.10 learned-vs-learned (p=1.60e-45)`. The body reports the **same named comparison, "learned-vs-learned", as `+$50.01 (p=8.5e-32)`** — .tex matched-family ablation L504 and bootstrap table L517; .md §8.6 M426/M433, F9 M344, §8.7 M451, §8.8 M478, §9.1 M629, Limitation #14 M645, and the Conclusion Summary (.tex L827, .md M717, M722, M738). The two numbers are actually different comparisons (`+$103.10` ≈ `cam_multisignal_learned − ncc_intent_only`; `+$50.01` = `cam_multisignal_learned − cam_learned`, a *different* single-signal comparator), but the paper uses the same label for both, so a reader sees the abstract headline gain as twice the body's headline gain. Because the "fitted 3-signal vs fitted 1-signal" phrasing in the abstract is not the same comparator as §8.6's "learned-vs-learned", the abstract is factually misleading about which comparison $+103.10 refers to. At minimum, pick one canonical "learned-vs-learned" definition (the body's `+$50.01`, which is the conservative estimate) and state the `+$103.10` pairing explicitly and consistently everywhere.
*(Sections: Abstract §2, Results §8.6, Discussion §9.1/§9.2 #14, Conclusion §10.1–10.2; .tex L64, L504, L517, L827; .md M46, M344, M426, M433, M629, M645, M717, M722, M738.)*

### Major

**M1. Abstract exceeds its own length budget and the two files carry different abstracts.**
The `.md` labels §2 "Abstract (150–200 words)" (M43) but the abstract paragraph is ~380–390 words (~2× the budget). The `.tex` abstract is ~209 words (L63–67) and *omits* content present in the `.md` abstract: there is no "We contribute a reproducible benchmark, environment-consistency evidence, and a pre-specified field-validation design" sentence, and the "eight v1.3 extensions / three v1.4 extensions" enumeration is compressed. The two files therefore do not present the same abstract, and neither is at the stated 150–200-word target. Decide on one canonical abstract, trim to ≤250 words, and mirror it exactly in both files.
*(Sections: §2; .tex L63–67; .md M43–49.)*

**M2. Review/revision process artifacts are embedded in the manuscript body.**
Subsection titles and text still advertise the paper's own peer-review history: "Ablations (Round-3 Reviewer Experiments)" (.tex L499; .md M420), "Context-Blind Policy Search (Round-4 Adversarial Review)" (.tex L525; .md M438), and the `\resolved{...}` markers that print "Resolved (§X): …" inline throughout the Limitations list (e.g., .tex L762–768, L772, L781–789) and in Results (e.g., .tex L593, L599, L602, L605, L608). "Statistical Discipline" (.tex L790) and repeated "(§9.2 #15)"-style self-citations to the limitations list (e.g., .tex L517, L545) read as a reviewer-response memo rather than a submission. These meta-markers break the formal academic register (checklist item 9) and inflate length (checklist item 8). Fold the "resolved" verdicts into plain prose ("We test this in §X: …") and remove round-number references from section titles.
*(Sections: §8.6, §8.7, §9.2, §9.2.1; .tex L499, L525, L790; .md M420, M438, M691.)*

**M3. Redundant "Findings" subsection vs the inline finding blocks.**
The `.md`'s `8.3 Findings` (M334–346) duplicates F1–F4 and F9 plus the interpretation paragraph, which are then restated as inline `\finding{...}` blocks within §8.1–§8.4 and re-summarized again in Discussion §9.1 and Conclusion §10.2. The `.tex` already removed the standalone Findings subsection (its Results go straight from §8.2 to §8.3 Robustness), which is the better choice. Either delete or shrink `8.3 Findings` in the `.md` to a 3–4 sentence "headline results" digest, or keep the subsection but strip F1–F9 from the inline flow to avoid three-fold repetition. This also contributes to checklist item 8 (length).
*(Sections: §8.3; .md M334–346 vs .tex L369–405.)*

**M4. "Future Work" is mostly a completed-items ledger.**
§10.3 / §10 lists 24 items, of which ~21 are marked "done"/"partial" (e.g., adversarial mapping, CRN, matched-family ablation, LLM baseline are all flagged ✅done). The genuinely forward-looking work (field validation #1, learned bidding #2, adversarial/dynamic environments #7, field studies #8, B2B Layer-0 #9, theory #10, account aggregation #15, first-price auction #16, fine-tuned LLMs #24) is buried in a reviewer-response checklist. Restructure into "Planned work" (the open items) with the completed extensions referenced back to their Results sections (or moved to an appendix). The "done" repetitions make the Conclusion read as a changelog rather than a close (checklist items 7 and 8).
*(Sections: §10.3; .tex L836–863; .md M727–753.)*

### Minor

**m1. Research questions are stated but never explicitly answered by number.**
RQ1–RQ4 are cleanly stated in the Introduction (.tex L82–89; .md M62–71), and RQ2 gets an inline "Resolved (§8.8)" marker. But the Discussion answers hypotheses H1–H4, not RQ1–RQ4 by number, and neither the Discussion nor the Conclusion maps each RQ to its supporting section. Add one short "Answers to the research questions" paragraph (RQ1 → §8.3–8.4; RQ2 → §8.6/§8.8; RQ3 → §9.1; RQ4 → §9.1, F9/F10) so the stated questions are visibly closed (checklist item 3).
*(Sections: §3.3, §9.1; .tex L82–89, L750; .md M62–71, M619.)*

**m2. Results-subsection ordering has three small coherence gaps.**
(a) The eight v1.3 extensions (§8.10–8.17) are one-paragraph "dump" subsections that fragment the narrative; consider grouping them under a single "Threat-to-Validity and Sensitivity Analyses (v1.3)" heading with numbered sub-items — especially since §8.5 already exists as a "Stress Tests" cluster in the `.md`. (b) §8.9 Macro-F1/CRN are statistical-methodology checks and would read more naturally adjacent to §8.1–8.2 than after §8.8. (c) The online-learning section (§8.18) explicitly builds on the bandit baselines (§8.12 — "The §8.12 bandit baselines were offline-trained") but is separated from them by five unrelated subsections; moving the bandit/online pair together would tighten the causal narrative. The overall order is otherwise logical, and the v1.4→v1.5→v1.6 tail is coherent (§8.22 explicitly continues §8.21).
*(Sections: §8.9–§8.18; .tex L576–609; .md M480–530.)*

**m3. Version-history terminology is used without a roadmap.**
Results opens directly into §8.1 ("All numbers are auto-generated from CAM-Sim v0.4…") with no explanation of the v0.4 / v1.3 / v1.4 / v1.5 / v1.6 version arc that frames the whole Results tail. The transition between versions is internally coherent once a reader reaches §8.18, but a one-paragraph "extension roadmap" at the top of Results (what each version added and why) would make the arc legible on first read (checklist item 4).
*(Sections: §8 intro; .tex L336–339; .md M299–301.)*

**m4. Abstract phrase "in 7 environments" is imprecise.**
The `.tex` abstract (L64) says the context-blind EMAIL policy beats every deployable agent "in 7 environments"; everywhere else (body L545, .md abstract M46, .md §8.7 M451) it is "7 of 9 environments". The "of 9" is important (it interacts with the "replicates across 9 environments" claim in the same sentence) and should be restored (part of checklist item 1).
*(Sections: §2, §8.7; .tex L64 vs L545; .md M46.)*

**m5. TL;DR vs abstract: broadly consistent, two divergences.**
The TL;DR (M4–18) matches the abstract on the headline +$50, the +$103.85 matched-family gap, the channel-cost arbitrage, and the v1.4/v1.5/v1.6 storyline — good. Two divergences: (a) the TL;DR omits the +$103.10 "fitted vs fitted" number entirely (which is actually the safer choice given C2 — recommend the abstract follow the TL;DR, not vice versa); (b) the TL;DR asserts "four of five [LLM models] beat it on profit," a stronger claim than the abstract's "profit-competitive," and the body (§8.21) shows only two of five profit contrasts survive Bonferroni — the TL;DR should mirror the abstract's more careful framing. After C2/M1 are fixed, the TL;DR and abstract should be word-for-word aligned (checklist item 10).
*(Sections: front matter §TL;DR, §2, §8.21; .md M4–18, M46, M578–600.)*

**m6. Research-gap message repeated too often.**
The "zero papers connect agentic + situational awareness in marketing" gap is stated at least five times: §3.1 quote, §3.3 Key Insight, §5.3, §5.4, and §9.3 "For Researchers." Each statement adds the important scope caveat (keyword search, not systematic), which is good, but one consolidated statement plus a "see §5.3" pointer in §9.3 would trim length (checklist item 8).
*(Sections: §3.1, §3.3, §5.3, §5.4, §9.3; .tex L72–89, L139–176, L800–814; .md M52–71, M133–156, M691–702.)*

**m7. RQ2 answer wording differs between files.**
The `.md` says RQ2 is "Resolved (§8.8)" (M64) while the `.tex` says "Resolved (Section~\ref{sec:baselines})" (L85) — both are correct in their own numbering, which is exactly the C1 hazard made manifest in the front matter. Once C1 is fixed this disappears; flagging only to show the inconsistency is not limited to the Results section.

---

## Checklist Answers (the ten requested review questions)

1. **Abstract accuracy:** No — see **C2** (learned-vs-learned +$103.10 vs +$50.01), **M1** (over-budget, two different abstracts), **m4** ("7 environments" vs "7 of 9").
2. **Narrative arc:** Yes — clear problem → theory → framework → method → results → discussion → conclusion. Blocked at the reading level only by **C1** (broken numbering across the `.tex`).
3. **RQs explicitly stated/answered:** Stated clearly (RQ1–RQ4); answered, but never mapped back to RQ numbers — see **m1**.
4. **v1.4→v1.5→v1.6 transition:** Coherent (§8.22 explicitly localizes §8.21's blindness cause); only missing is a version-roadmap for readers — see **m3**.
5. **Result-subsection ordering:** Largely logical; three regroupings recommended (v1.3 extension cluster, Macro-F1/CRN placement, bandit/online adjacency) — see **m2**. The `.md`'s 22-subsection layout is the intended one; the `.tex`'s 20-subsection merge is the source of **C1**.
6. **Discussion balance:** Yes — 25-item limitations (self-resolved), practical implications, theoretical implications, and honest oracle framing all present; only the `\resolved` in-line artifacts detract — see **M2**.
7. **Conclusion contributions + future work:** Contributions well summarized and future work concrete (field-validation design, learned bidding) — but the future-work section is dominated by "done" markers — see **M4**.
8. **Redundancy / length cuts:** Yes to cuts — see **M3** (Findings duplication), **M4** (completed-items ledger), **m6** (gap repetition), and **M2** (review-history artifacts). The `.tex` already merged some of this; apply the same to the `.md`.
9. **Tone consistency:** Formal and appropriately cautious scientific prose ("simulation, not sampling", "must not be read as field-deployment evidence"); the colloquial "beats every deployable agent", "the bid surprise", and the reviewer-round artifacts break register in places — see **M2**.
10. **TL;DR vs abstract:** Mostly consistent, two discrepancies — see **m5**; resolution should favor the body/TL;DR numbers.

---

## Recommendations

1. **[Critical] Unify section numbering.** Compile the `.tex` with the `.md`'s six-part Results layout (or vice versa), label every Results subsection, and replace all hard-coded `\S8.x` / `\S9.2` / `\S10.3` / `\S7.3` references with `\ref`. Verify every cross-reference resolves to the intended section in the rendered PDF (the task's own description of the paper as having "22 subsections §8.1–§8.22" matches the `.md`, so the `.md` layout should be canonical).
2. **[Critical/major] Reconcile the headline ablation numbers.** Pick the body's `+$50.01` as the canonical "learned-vs-learned" gain; either drop `+$103.10` from the abstract or rename it precisely ("fitted-3-signal vs fitted-NCC-1-signal") so no reader conflates it with `+$50.01`. Propagate one consistent set of numbers through Abstract, §8.6, §9.1, §9.2 #14, §10.1, §10.2, §10.3, and the TL;DR.
3. **[Major] Set one canonical abstract.** Target ≤250 words, restore the "7 of 9 environments", add the contributions sentence if kept, and mirror it byte-for-byte in both files.
4. **[Major] Strip review-history meta-commentary.** Remove "(Round-3/Round-4 …)", `\resolved` markers, and "Statistical Discipline" reviewer-speak from the manuscript body; convert to plain prose and neutral section titles.
5. **[Major] Cut redundancy:** shrink/remove `.md` §8.3 Findings; split §10.3 into "Planned work" vs "Completed extensions (see §8)". Consolidate the research-gap statements to §3 and §5.3.
6. **[Minor] Add an RQ→answer mapping** paragraph in Discussion, a one-paragraph Results roadmap covering v0.4/v1.3/v1.4/v1.5/v1.6, and regroup the v1.3 extensions and the bandit/online pair as suggested in m2.
7. **[Minor] Align TL;DR with the corrected abstract**, especially the LLM profit claim ("two of five contrasts survive correction"), so front-matter claims never outrun the body.

**Clean categories:** (2) main narrative arc — No issues found beyond the numbering defect; (6) Discussion *balance* (breadth of limitations/implications) — No issues found beyond M2's presentation artifacts; (9) overall tone is consistently formal/cautious — minor exceptions only.
