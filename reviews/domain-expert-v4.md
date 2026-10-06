# Domain-Expert Review, Round 4: CAM / CAM-Sim v0.9

**Reviewer profile:** Same reviewer as rounds 1–3 (`reviews/domain-expert.md`, `reviews/domain-expert-v2.md`, `reviews/domain-expert-v3.md`) — 15 years in programmatic buying and demand-side platforms (Google Ads, DV360, Meta, LinkedIn, The Trade Desk). Fourth-round review of v0.9, the benchmark-pivot revision.

**Scope:** `paper/g4_academic_paper.md` (v0.9). I did not re-run the simulation. I assess the retargeting from JM/MS to computational venues, the three new §8.6 ablations, the status of my five round-3 field-trial conditions, and whether the central practical finding survives.

---

## Summary

v0.9 does two things: it retargets the paper (*NeurIPS Datasets & Benchmarks / KDD / Journal of Interactive Marketing / Journal of Marketing Analytics*, "Reproducible Benchmark + Ablation Study") and it adds §8.6 — a majority-action floor, a matched-family ablation, and a paired-difference bootstrap. Neither touches the evidence base: the agent ladder, the nine environments, and findings F1–F9 are unchanged, and the central practical finding (invest first in multi-signal situation classification, then in mechanism-calibrated bidding) is restated essentially verbatim in §8.3, §9.1, §9.3, and §10.1.

My assessment in brief: the pivot is correct and changes less than it first appears; the ablations are genuinely decision-relevant — two of the three directly so — and they strengthen rather than stress the practical finding, at the cost of an honest downward correction of headline magnitudes; and my five round-3 field-trial conditions are untouched, unmet, and still binding on any field launch. My verdict improves from round 3's PARTIALLY.

## Pivot-Practitioner-Impact

Does the venue reframe change what transfers to practice? Mostly no — and where it does, the change is positive.

**What is unchanged.** Every item on my round-3 transfer list transfers on exactly the same footing: multi-signal beats single-signal (F9), miscalibrated bid modulation is worse than none (F3), systematic bias under distribution shift beats random noise adversely (F5/F6), error placement dominates error count (F6), classification before bidding as sequencing. Same caveats, too: proxy dollars, sim unit ≠ field unit, supplied-not-sensed signals, single-decisioner accounts. The pivot is a relabeling of venue claims, not of evidence.

**Why the pivot is right.** The round-3 consensus was that JM/MS requires field data, and this line of work has none. The paper now concedes that rather than papering over it. For a practitioner this is the honest move: no venue claim of field validation remains, while §9.3's practical implications still stand clearly labeled as simulation-derived.

**What is newly transferable.** A benchmark framing promotes the one artifact the JM/MS framing never foregrounded: the evaluation protocol itself. Paired seeds, an awareness ladder, a majority-action floor, and a matched-family ablation constitute a procurement-grade test template. Any ABM vendor claiming "context-aware" (6sense, Demandbase, Bombora-adjacent stacks) can be run through a ladder with the buyer's own reward table — and the two §8.6 design ablations are precisely the tests that catch vendor slop: *beating random* is not *beating the incumbent static playbook*, and *a feature gain* is not *a better model*. I would put this harness pattern into my next vendor-evaluation RFP unchanged. That is a real, new practical output of the pivot.

**Residual concern.** JIM/JMA remain on the target list, and JMA readers are practitioners who will act on §9.3. For that half of the list the field-side gaps (label provenance, incrementality, signal acquisition) are editorially live rather than deferrable. And the pivot changes nothing about §10.3 #1, which stays in the paper as the priority experiment and as the abstract's closing contribution ("a pre-specified field-validation design").

## Ablation-Relevance

Are the §8.6 results decision-relevant to a practitioner deciding whether to invest in multi-signal classification? Yes — with one bookkeeping fix.

1. **Majority-action floor (35.1% match, −$15.38) — the most decision-relevant of the three, because it installs the right null.** No B2B program randomizes actions; the incumbent default is a fixed playbook, which is exactly what an always-EDUCATIONAL, flat-bid policy models. Against this realistic null, the value of context is real but materially smaller than the random-baseline comparison suggests: `cam_multisignal` beats the floor by ≈ +$221.51, not by +$376.17. The floor also enables the cleanest classification-only decomposition: under identical flat bidding, perfect classification (`situation_only`, +$294.27) beats the majority playbook by +$309.65/episode — a number uncontaminated by bid-policy effects, since the `cam_*` agents carry the heuristic bid multipliers per the action mapper (which F3 shows are value-burning, so the multi-signal headline if anything *understates* flat-bid value). The floor retires the "engineered strawman" reading of the baseline — a real concern whenever a vendor demos against random. The 35.1% ≈ exploration base rate (35%) consistency check also holds.

2. **Matched-family ablation (NCC intent-only 72.7% / +$102.28 vs NCC 3-signal 98.9% / +$206.13; gap +$103.85, p = 5.16e-46, d_z = 7.89) — decision-relevant in the direction practitioners need.** It answers the exact question asked when buying features: holding the model fixed, what are competitive density and channel quality worth? That is the feature-procurement question (add Bombora-style surge + Auction-Insights-style density to the same model: what do I get?), and the answer is decisive. Two caveats for decision use. First, `ncc_intent_only` (72.7%) is a weaker single-signal base than `cam_learned` (87.5%) — classifier-family choice alone is worth ≈ +$53 on one signal — so the fair value band for the two added signals is +$50.01 (vs the best single-signal learner) to +$103.85 (family-matched), and the business case should quote +$50; §9.3 correctly does. Second, the sign convention in §8.6 and the abstract is inverted ("cam_multisignal − ncc_intent_only … −$103.85" — the gap runs in the claimed positive direction), and contribution 6 then folds the +$50 and +$103.85 numbers into one sentence. Fix the sign; keep both numbers, labeled.

3. **Paired-difference bootstrap (B = 2000; CIs within $0.30 of normal approximation) — necessary hygiene, not decision input.** At d_z = 3.96–7.89 with n = 50, no investment decision ever hinged on CI precision; the binding uncertainty is external (label provenance, signal availability, proxy dollars). But it fully retires the round-2 statistics objection. With this, the sim-side internal-validity story is complete; everything that remains is field-side.

## Trial-Conditions-Status

All five round-3 conditions stand, verbatim, and none is met — v0.9 did not attempt them:

- **(a) Labeling protocol** — §10.3 #1 still specifies "human-coded situations" with no coder count, agreement threshold, throughput, or per-label cost, and pre-launch recalibration labels (2,000 per distribution) remain unsourced. #22 still concedes there is no ground-truth situation label in production.
- **(b) Incrementality** — §9.2 #12 still concedes no incrementality in the reward; the trial's primary endpoint remains between-arm uplift with no within-Arm-A holdout.
- **(c) Crisis guardrail** — §6.5 still hardcodes the 2.0× crisis multiplier; #23/#17 still defer it; Arm A still deploys "exactly the `cam_multisignal_recalibrated` pipeline." An incident-generating default documented in the limitations is still not launch-safe.
- **(d) Signal acquisition** — no availability/latency/cost specification for the three signals, and no missing-intent fallback, anywhere in v0.9.
- **(e) Arm A bid policy / window** — still unspecified whether Arm A bids flat or context-multiplied (F3 makes this a known-bad confound), and the 8–12-week window is still fixed against an unmodeled B2B sales cycle.

The pivot does not dissolve these. As long as §10.3 #1 remains the paper's priority experiment and the abstract promises a pre-specified field-validation design, the conditions attach to it — and the JIM/JMA half of the venue list raises their weight, because those readers will operationalize §9.3. To be precise about scope: none of the five blocks the benchmark submission; all five block the field launch.

## VERDICT

**ACCEPT as the reframed benchmark paper — upgraded from round-3 PARTIALLY** — with the five field-trial conditions reaffirmed as standing pre-conditions on §10.3 #1 (unchanged, unmet, required before any field launch), and two minor text fixes before submission: (i) the inverted sign convention on the matched-family gap in §8.6 and the abstract; (ii) a one-line majority-floor-based value decomposition in §9.3, so practitioners read the honest magnitudes — ≈ +$221 over the static-playbook null (not +$376 over random) and +$50 (not +$104) as the fair two-signal premium.

The pivot matches the evidence to the venue without weakening the transferable core, and usefully repositions the harness itself as the practitioner artifact. The ablations strengthen the practical finding rather than stress it: the strongest context-blind policy is still negative (−$15.38), the multi-signal gain survives family matching at p = 5.16e-46, and the fair premium is now honestly bounded at +$50–$104 proxy per episode. **Invest first in multi-signal situation classification, then in mechanism-calibrated bidding — that recommendation survives round 4 intact, now with a stronger floor under it.** The remaining gaps are all field-side: label provenance, incrementality, signal acquisition, the crisis default, and Arm A's bid policy — the same five items as round 3, and they now constitute the entire distance between this paper and a deployable, field-validated result.
