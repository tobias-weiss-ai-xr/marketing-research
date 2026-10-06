# Desk-Review, Round 4: Computational-Venue Editor Assessment

**Paper:** *Context-Aware Agentic Marketing: A Situational Awareness Framework for Autonomous Marketing Systems* (`paper/g4_academic_paper.md`, v0.9)
**Reviewer persona:** Same senior editor as rounds 1–3 (`reviews/journal-editor.md` – `journal-editor-v3.md`), now wearing the *NeurIPS Datasets & Benchmarks* / *KDD* desk hat per my own round-3 redirect
**Decision window:** 10 minutes, desk review only
**Editorial question this round:** My round-3 verdict was DESK-REJECT at JM/MS with an explicit redirect to computational venues and a list of five cheap deferred experiments. v0.9 claims to act on both. Did the pivot land, does §8.6 change the venue verdict, and does this manuscript now clear a computational-venue desk?

## Summary

v0.9 is the redirect executed, mostly. The header block now targets NeurIPS D&B / KDD / *Journal of Interactive Marketing* / *Journal of Marketing Analytics* and declares the type "Empirical (Reproducible Benchmark + Ablation Study)"; the key-contribution line leads with the paired-seed benchmark; the abstract closes on exactly the right sentence ("We contribute a reproducible benchmark, environment-consistency evidence, and a pre-specified field-validation design"). §8.6 adds the three promised ablations and §10.3 items #11, #14, #19 are checked off — I verified each against the text. The statistical apparatus that survived rounds 2–3 is intact, and every §8.6 number I spot-checked propagates consistently into the abstract, §9.2 #13/#15, §10.1, and §10.2 #6 (one sign-convention slip aside, below). What did *not* change: the title, the research questions, and the front half of the paper. The pivot is real in the apparatus; it is incomplete in the packaging.

## Pivot-Assessment

Internally consistent? **Partially — the benchmark framing and the framework framing now coexist rather than one replacing the other.**

What converted: target venue, type line, key-contribution line, abstract's evaluation sentences and closing contribution sentence, §8.6, §10.2 items 3–6 (benchmark-shaped, honest, correctly caveated), and the limitations section, which now reads as the de facto results-at-a-glance for a referee.

Residual JM/MS framework claims, in order of visibility:

1. **The title still says "A Situational Awareness Framework."** This is the most-read line of the paper and it directly contradicts the type line fifteen lines below it. Round 3 asked for "CAM-Sim: a reproducible benchmark for situational-awareness ablations in marketing agents" or equivalent; v0.9 ships the benchmark under the old masthead.
2. **The abstract's first substantive sentence is "We propose … a four-layer framework."** A D&B/KDD abstract should open with the resource: the benchmark, the task, the agent ladder. The framework sentence is the JM-shaped move.
3. **RQ1 ("Conceptual") and RQ2 ("Framework") are framework-paper research questions.** A benchmark paper's questions are task-design questions: what does the environment vary, what agents does it discriminate, what claims about them does it license.
4. **§10.2 still leads its contributions list with "Theoretical" and "Conceptual" (items 1–2) before the benchmark items (3–6).** At a computational venue the order should invert.
5. **§4–§6 (~40% of the body) build the framework**, including the Endsley tables, the six-signal sensing taxonomy, and the action matrix — with limitations #23/#24 still on record conceding the crisis mapping may be backwards and the sensing layer emits a decoy signal. §9.4 still draws "theoretical implications" from Endsley. None of this is dishonest — every claim is caveated — but the manuscript is a hybrid: benchmark evidence in framework packaging. The keywords don't even contain "benchmark."

Two copy-edit residuals: (a) the matched-family gap is **−$103.85 in the abstract and in the §8.6 table row (labeled `cam_multisignal − ncc_intent_only`) but +$103.85 in the §8.6 prose, §9.2 #13, §10.1, §10.2 #6, and §10.3 #11** — pick a sign convention; (b) the abstract says "eleven agents" while F7 computes its per-seed Spearman over a "13-agent ranking" (11 default-table agents vs 13 including the recalibration variants). Both are ten-minute fixes; both will be noticed.

## Benchmark-Contribution

Does §8.6 move the needle? **Yes — materially, and in the right direction for a benchmark paper.**

- **Majority-action floor (35.1% match, −$15.38).** This retires the "engineered strawman" objection properly: the floor is no longer a random agent but the strongest context-blind policy, and it still loses money while every context-aware agent clears it. The floor also quietly sharpens the framing: the *ceiling* of context-blind behavior is negative profit. Good benchmark hygiene.
- **Matched-family ablation (NCC intent-only 72.7% / +$102.28 vs NCC 3-signal 98.9% / +$206.13; +$103.85, p = 5.16e-46, d_z = 7.89).** This is the strongest addition. Holding the classifier family and calibration protocol fixed and varying only signal count is precisely the control a D&B referee wants, and it addresses the round-3 adversarial attack (family confound) at the root. Note the corroborating detail: `ncc_intent_only` (72.7%, +$102.28) lands within ~3 points of the handicapped `cam_inferred` (75.7%, +$104.26), so the intent-only difficulty level is now triangulated by a non-handicapped comparator — the +$101.87 headline gain is no longer resting solely on a 4-of-6-classes strawman. The learned-vs-learned +$50.01 remains the conservative number and the paper keeps it primary. Correct.
- **Paired-difference bootstrap (B = 2000, CIs within $0.30 of normal approximation).** Closes §9.2 #15 exactly as the round-2 ml-methodology reviewer specified: resample the paired differences, not marginal means. Two of the five deferred experiments from my round-3 list are done and done correctly; still open are the adversarial-mapping condition (#3), the contextual-bandit baseline (#12), and common random numbers (#5) — all referee-level, none desk-level.

This is enough to change my venue verdict. In round 3 I said the benchmark "would be competitive" at a computational venue *after* the cheap experiments; with the floor, the matched-family control, and defensible CIs in hand, the core empirical claims (multi-signal beats single-signal; miscalibrated bidding is worse than flat; systematic bias under shift is worse than noise and recalibration fixes it) are now controlled results, not just large effects against weak baselines.

## Venue-Fit

- ***Journal of Marketing Analytics* / *Journal of Interactive Marketing* — best fit as-is.** Reproducible simulation methodology, statistical hygiene, and practitioner implications are squarely in scope; the framework sections read naturally as task motivation rather than as overclaim. I would send this out today at JMA.
- ***KDD* (applied/data-science track) — good fit.** The ablation ladder, environment presets, and reproducibility contract are KDD-shaped. Referees will still expect at least one deployable learned policy (bandit or GBM) beyond nearest-centroid before acceptance.
- ***NeurIPS D&B* — conditional fit, highest upside.** The resource is a synthetic simulator rather than a dataset; D&B accepts these when the task is well-motivated, discriminates methods, and the artifact is maintained. Reproducibility is exemplary (seeded, byte-identical, results regenerated from code). But three D&B-specific gaps: (1) no hosting/versioning/DOI statement for the artifact; (2) no standard-baseline suite — no LR/GBM/RF, no LinUCB, and the framework's own specified RandomForest/LSTM components remain unimplemented surrogates; (3) no headroom — at 98.7–98.9% on the default environment the task is nearly saturated, so the benchmark currently *confirms* rather than *discriminates*. I would not desk-reject at D&B; I would send it out only after the benchmark-first retitle, because a paper whose title claims a framework will attract the wrong referee comparisons and deserve them.

## Remaining-Gaps

For acceptance at a computational venue, in priority order:

1. **Retitle and reframe** (title, abstract's first sentence, RQ1/RQ2, reorder §10.2 benchmark-first). Zero compute; largest single improvement.
2. **Standard baselines:** logistic regression and a small GBM on 1 vs 3 signals, plus one contextual bandit (LinUCB or ε-greedy) as the deployable-policy comparator (§10.3 #12). This is the gap most likely to sink an otherwise positive D&B/KDD review.
3. **Headroom:** add harder regimes — feature noise, missing signals, increased class overlap — so the benchmark separates methods near the top; and fix or scope the decoy sensing signal (#24).
4. **Adversarial-mapping condition (#3):** the shared author-design of ideal-action table and reward is the benchmark's deepest validity threat; one condition where the mapping is not self-confirming would inoculate the headline claim.
5. **Common random numbers (#5)** and the per-environment learned-vs-learned comparison (#11, second half) — both cheap, both pre-registered in §10.3.
6. **Artifact logistics:** DOI'd release (e.g., Zenodo), versioning, and a benchmark documentation sheet / D&B checklist. `results/` being gitignored is fine *because* everything regenerates — but the artifact must then be citable.
7. **Copy-edits:** the ±$103.85 sign convention, the 11-vs-13 agent count, abstract length (~280 words against a stated 150–200 target).

## VERDICT

**SEND OUT FOR REVIEW — at KDD or JMA immediately; at NeurIPS D&B after the benchmark-first retitle and reframing (items 1, and ideally 2, above).** The desk-reject era is over: the round-3 redirect was executed in substance, §8.6 converts the two most damaging round-3 objections (strawman floor, classifier-family confound) into controlled experiments, and the statistical record — now including paired-difference bootstrap CIs — is submission-clean. What remains are referee-level gaps (baselines, headroom, artifact logistics) and one packaging decision (the title) that no referee should be asked to adjudicate for the authors. This is not a desk-accept: the missing standard baselines alone make acceptance premature. But it is a manuscript I am now willing to put in front of the right referee pool, which is what the authors asked of the pivot. My disposition for the authors' file: retitle before submission anywhere; add the bandit/GBM baselines in the revision cycle; archive a DOI'd artifact; and keep the limitations section exactly as honest as it currently is — at a computational venue, that section is now an asset, not a confession.
