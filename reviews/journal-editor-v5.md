# Desk-Review, Round 5: Computational-Venue Editor Assessment

**Paper:** *CAM-Sim: A Reproducible Benchmark for Situational-Awareness Ablations in Marketing Agents* (`paper/g4_academic_paper.md`, v1.0)
**Reviewer persona:** Same senior editor as rounds 1–4 (`reviews/journal-editor.md` – `reviews/journal-editor-v4.md`)
**Decision window:** 10 minutes, desk review only
**Editorial question this round:** My round-4 verdict was SEND OUT FOR REVIEW with five packaging gaps. v1.0 claims all five are fixed and adds §8.7 (a disclosed channel-cost arbitrage). Did the packaging pivot close, does the disclosure change the venue, and does v1.0 go out — and where?

## Summary

v1.0 is the packaging round executed, and I can confirm four of the five fixes from the text without re-running anything. **Title** (§1): now "CAM-Sim: A Reproducible Benchmark for Situational-Awareness Ablations in Marketing Agents" — the framework masthead is gone from the submission title. **Abstract**: opens with the resource ("We present CAM-Sim, a reproducible paired-seed benchmark…") and closes the first paragraph on the channel-cost arbitrage — benchmark-first, exactly as round 4 asked. **RQs** (§3.3): now Benchmark / Ablation / Performance / Mechanism, i.e. task-design questions, not framework questions. **§10.2 order**: contributions now run Benchmark (1) → Findings (2) → Ablation (3) → Methodological (4) → Theoretical (5) → Conceptual (6); the JM-shaped items are last. **F7**: now "an 11-agent ranking (plus 2 recalibration variants in the label-noise grid, for 13 total)" — the 11-vs-13 discrepancy is closed. The sign convention on the matched-family gap (+$103.85) is also consistent across §8.6, the bootstrap table, §10.1 and §10.2. The pivot is real and it is now in the packaging, not only the apparatus.

What is new this round is §8.7: the majority-action floor was mis-specified, and a context-blind policy on the cheapest channel (EDUCATIONAL|EMAIL|bid 0.3, +$252.41) beats every *deployable* context-aware agent in 7 of 9 environments. The authors disclose it in the body, in §9.2 #25, in the abstract, and defer the fix to §10.3 #20. That is the right instinct, and it changes my venue calculus more than any of the five packaging items.

## Packaging-Assessment

**Resolved, with three residuals that must be fixed before referees, not by them:**

1. **The document header still carries the old title.** The manuscript H1 reads "# G4 Academic Paper: Context-Aware Agentic Marketing (CAM)" and the type block still says "Draft Structure for Journal Submission." §1 is correct; the header is a file artifact. Cosmetic, but it is the first line of the PDF and it contradicts §1.
2. **The abstract still overclaims.** It says the context-blind EMAIL policy beats "every context-aware agent," while §8.7 and #25 correctly say "every *deployable* context-aware agent." `situation_only` (+$294.27) and `bid_calibrated` (+$530.45) are context-aware and beat it. The qualifier was dropped in the abstract, §10.1 and §10.2 #3. This is a factual, one-word fix in the most-read sentence of the paper.
3. **Abstract length.** 214 words against the stated 150–200 target. Improved from ~280 in round 4, still over. Trim, do not ship an out-of-spec abstract.

Two further copy-nits: §10.1 and §10.2 #3 call +$103.10 the gap "vs the learned 3-signal arm" — it is the *fitted 3-signal vs fitted 1-signal* contrast, so the label is backwards; and "fair learned-vs-learned" denotes +$50.01 in §8.6/§9.1 but +$103.10 in §10.3 #11. Pin one definition. None of this is desk-dispositive; all of it is the authors' to fix before the paper reaches a referee, not a referee's to adjudicate.

**Net:** the round-4 packaging condition is met. The title, abstract, RQs, contribution order and F7 count are as requested.

## Venue-Decision

Round 4 said: SEND OUT at KDD/JMA immediately, at NeurIPS D&B after the benchmark-first retitle. The retitle is done — but §8.7 changes the answer, because it is a statement about the *instrument*, not the prose.

- ***Journal of Marketing Analytics* — best fit in current form.** JMA publishes reproducible simulation methodology, statistical hygiene, and honest null/validity results. A benchmark whose dominant policy is context-free, disclosed and diagnosed rather than hidden, is squarely a JMA contribution: it is a *diagnostic* paper — "here is a harness and here is how it fails." Send it here now.
- ***KDD* (applied/data-science track) — sendable after the baselines, not before.** The ablation ladder, nine presets and reproducibility contract are KDD-shaped, and KDD tolerates a negative/validity finding when it is framed as a null-selection lesson. But KDD referees will require at least one deployable learned policy (GBM or bandit) beyond nearest-centroid. This is the gap most likely to sink an otherwise positive review.
- ***NeurIPS Datasets & Benchmarks* — hold.** D&B judges a benchmark by what it measures. §8.7 establishes that this one's reward function does not penalize wrong-channel assignments, so the cheapest channel dominates — the paper admits the artifact does not isolate the capability it names. A D&B referee would rightly treat "fix the reward" as a precondition of the resource, not a v2.0 wish. Additionally D&B requires a citable, versioned artifact (no DOI here) and a task that discriminates methods (98.7–98.9% on the default environment is near-saturated, so it *confirms* rather than *discriminates*). Do not route this to D&B until channel-dependent reward, standard baselines and a DOI'd release exist.
- ***Journal of Interactive Marketing* — not this version.** Framework-forward and practitioner-facing, which suits §4–§6, but JIM expects field or observational evidence; §10.3 #1 is a pre-specified *design*, not data. JMA is the better computational home.

**Fit of §4–§6.** The framework half (~40% of the body) is tolerable as task motivation at JMA and KDD, and it is now correctly scoped: §6.4's implementation note and §6.6's scope note concede that Level-3 projection is specified but unbenchmarked and that CAM-Sim runs nearest-centroid/threshold surrogates. At D&B it is not tolerable as written — §§6.2–6.3 describe a six-signal, six-dimension sensing model, but limitations #6 and #24 concede the signals are supplied, not sensed, and the `quality_score` field is a decoy. The framework describes a capability the benchmark does not exercise. Trim §6.2–6.3 to an appendix for any computational submission; keep them in the JMA/JIM framing as motivation.

## Remaining-Gaps

These are referee-level for KDD/D&B and should be fixed in the revision cycle, not deferred to a v2.0 that will not exist:

1. **Standard baselines (highest priority).** No logistic regression, GBM, random forest or contextual bandit (LinUCB/ε-greedy) is benchmarked (§9.2 #13, §10.3 #11–12). Without a nonlinear learner on 1 vs 3 signals and at least one bandit, the multi-signal result is only "beats the authors' own NCC and threshold classifiers" — the exact family-confound round 3 raised. This is mandatory for KDD/D&B and arguably for JMA acceptance.
2. **Headroom.** 98.7–98.9% match on the default environment leaves no room to separate methods. The nine presets vary *economics* (costs, budget, curvature), not *difficulty*; none adds feature noise, missing signals, or class overlap. A benchmark that is saturated on its default task cannot discriminate state-of-the-art methods, which is the D&B bar.
3. **Common random numbers (CRN).** §9.2 #10 is candid: contexts are paired but decision noise is not (single global RNG consumed sequentially; seed-level baseline correlation −0.23 to +0.08), so pairing buys no power over an unpaired test. For a paper whose central design virtue is "paired-seed," this is a real methodological gap. It is a few lines of code (independent stream per agent, same contexts) and it is already pre-registered as §10.3 #5. Do it.
4. **DOI / artifact logistics.** No DOI, no versioning, no hosting statement; `results/` is gitignored. For D&B a citable, versioned artifact is mandatory. Worse, the §8.7 policy search is *not reproducible from any committed script*: the footer claims it "regenerates from `paper/cam_sim_ablations.py`," but that script contains only the majority action, the NCC contrasts and the bootstrap — I read it, and there is no EMAIL policy, no `(action, channel, bid)` grid, and no per-environment context-blind run. Real numbers, missing artifact. Commit the search before the paper's reproducibility contribution can be taken at face value.
5. **Copy/dispatch items** from Packaging-Assessment above (abstract "deployable," 214→≤200 words, the two "fair learned-vs-learned" labels, the document header).

One structural note for the authors: with §8.7 on the record, the "central practical finding" ("invest first in multi-signal situation classification") now sits under a sentence that says channel economics can dominate signal quality. At JMA that is publishable as a diagnostic; at D&B it reads as a benchmark that invalidates its own recommendation. Pick the framing deliberately.

## VERDICT

**SEND OUT FOR REVIEW — at *Journal of Marketing Analytics* now; at *KDD* (applied track) after the standard baselines; do not route to *NeurIPS Datasets & Benchmarks* in current form.**

The round-4 condition is met: the title, abstract, RQs, §10.2 order and F7 count are all fixed, and the sign convention is consistent. The desk-reject era ended in round 3; this round moves the manuscript from "hybrid benchmark in framework packaging" to "honest benchmark/diagnostic with a disclosed construction defect." That is enough for JMA, whose readers value exactly this kind of validity finding. It is not yet enough for D&B: the admitted channel-cost arbitrage means the artifact does not isolate the capability it names, and the missing standard baselines, absent headroom, unpaired decision noise and missing DOI are the referee-level work that separates a diagnostic artifact from a resource. I am willing to put v1.0 in front of a JMA referee pool today; I would not put it in front of a D&B pool until channel-dependent reward (§10.3 #20), a LR/GBM and a contextual-bandit baseline, a harder-regime preset, CRN, and a DOI'd release exist. Before any of that, fix the abstract's "every context-aware agent" and commit the §8.7 policy-search script — a benchmark paper cannot assert a result its own repository does not reproduce.
