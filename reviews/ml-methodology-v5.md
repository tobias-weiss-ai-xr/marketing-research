# ML Methodology Review (Round 5) — Paper v1.0 (§8.7 Policy Search + Round-4 Fixes)

**Reviewer persona:** ML researcher, NeurIPS/ICML reproducibility-track reviewer (fifth round).
**Artifacts reviewed:** `paper/g4_academic_paper.md` (v1.0, read in full, 668 lines); `paper/cam_sim.py`
and `paper/cam_sim_ablations.py` read and selectively re-executed. §8.7 was **independently reproduced
from scratch** (constant-policy agents implemented de novo against the committed environment; full
750-policy grid sweep; 9-preset comparison via `run_env`).
**Constraint honored:** the paper and code were **not modified** (`git diff --quiet
paper/g4_academic_paper.md` passes); all reproduction ran from temp-directory scripts.

---

## Summary

Round 4 returned ACCEPT (methods workshop / benchmark venue) with Issues E (per-class recall) and G
(multiplicity denominator) remaining and three recommendations: disclose the matched-family arm
asymmetry, state the multiplicity denominator explicitly, trim the abstract. v1.0 acts on all three:
§8.6 adds the arm disclosure plus the learned-arm contrast (+$103.10); §7.3 states the denominator
(540 + 3 + 5 = 548); the abstract is trimmed to 210 words (round 4: 281). The major new content is
§8.7 (context-blind policy search) and §9.2 #25, which honestly surface a channel-cost arbitrage
(EDUCATIONAL|EMAIL|bid 0.3 = +$252.41 beats every deployable context-aware agent) as a
benchmark-construction limitation rather than hiding it. I verified every §8.7 number by independent
reimplementation: **all four tabled policies reproduce to the cent, EDUCATIONAL|EMAIL|0.3 is the true
argmax over the full constant-policy grid, and the "7 of 9 environments" claim is exact** (losses:
`retention_heavy` +$177.3 vs +$237.3, `concave_returns` +$398.1 vs +$675.5). The arm disclosure is
accurate and the learned-arm contrast +$103.10 reproduces exactly (p = 1.60e-45, d_z = 7.71).

Two problems survive verification, one of them new and submission-blocking for a benchmark venue:
**(1) the §8.7 policy search is not in the committed code.** The footer states "context-blind policy
search regenerates from `paper/cam_sim_ablations.py`," but that file (last modified at v0.9) contains
no policy search, and `cam_sim.py` has none either — Appendix B's regeneration commands cannot
produce §8.7. The numbers are correct (I reproduced them), but the reproducibility contract is broken
for the paper's newest headline result. **(2) The abstract, §10.1, §9.2 #25, and the header
contribution line drop §8.7's own "in 7 of 9 environments" qualifier**, claiming the policy "beats
every context-aware agent" without qualification. Both are mechanical fixes, not methodological
errors. Issue G is substantively resolved with a one-sentence scoping caveat; Issue E remains
deferred, properly disclosed.

**Reproduction record (all exact):** EDU|EMAIL|0.3 → 35.1% match, +$252.41; EDU|EMAIL|0.5 → +$236.46;
EDU|EMAIL|1.0 → +$214.62; EDU|SEARCH|1.0 (majority floor) → 35.1%, −$15.38. Grid sweep (5 actions × 5
channels × 30 bids): argmax = EDUCATIONAL|EMAIL|0.30. Learned-arm contrast (cam_multisignal_learned −
ncc_intent_only): +$103.10, p = 1.60e-45, d_z = 7.71. Policy-vs-deployables across 9 presets: wins 7,
loses retention_heavy and concave_returns. Abstract: 210 words.

---

## Issue-Resolution (round-4 ledger)

| Round-4 item | v1.0 status | Verification |
|---|---|---|
| **Arm disclosure (matched-family asymmetry)** | **RESOLVED, sound** | §8.6 now discloses: `cam_multisignal` uses hand-set generative centroids, `ncc_intent_only` is fitted (2,000 samples, seed 999999); the 3-signal arm is a lower bound. Verified against code (`MULTISIGNAL_CENTROIDS` vs `fit_ncc_intent_from_env`): the disclosure is factually exact and consistent with §7.1/§9.2 #14. The learned-arm number +$103.10 (abstract, §10.1, §10.2 #3, §10.3 #11) reproduces **exactly** (+$103.10, p = 1.60e-45, d_z = 7.71 — matching my round-4 independent measurement). |
| **G — multiplicity denominator** | **RESOLVED in substance, scoping caveat remains** | §7.3 now states: 540 confirmatory (10 agents × 6 metrics × 9 environments) + 3 ablation contrasts + 5 context-blind policies = 548. See assessment below. |
| **Abstract trim (281 words)** | **RESOLVED** | 210 words; five findings still packed in, but within shouting distance of the 150–200 target stated in §2. |
| **E — per-class recall** | **REMAINS, properly deferred** | §8.5.2 still reports aggregate match only; §9.2 #11 and §10.3 #6 still defer macro-F1/per-class recall. Bounded, disclosed, non-blocking at benchmark-venue level; still required for a journal. |
| **Cosmetic (a) missing normal-approx CI on matched-family row** | **RESOLVED** | §8.6 row now shows [+$100.20, +$107.50]. |
| **Cosmetic (b) sign orientation of matched-family row** | **RESOLVED** | Now +$103.85, same orientation as other rows. |
| **Cosmetic (c) CI digit drift §8.2 vs §8.6** | **REMAINS (trivial)** | §8.2 note: CI [$98.3, $105.5]; §8.6: [+$98.30, +$105.44]. $105.44 rounds to $105.4, not $105.5. |

**Assessment of the arm disclosure (question 1): sound.** The disclosure sentence is accurate on every
checkable fact, and the framing ("+$103.85 is the family-matched maximum; +$50.01 learned-vs-learned
is the conservative estimate; +$103.10 is the learned-arm contrast") gives the reader all three
defensible numbers with the right epistemic labels. Two wording nits, neither affecting soundness:
(i) **"learned-vs-learned" now names two different contrasts** — §8.6/F9/abstract use it for
cam_multisignal_learned vs cam_learned (+$50.01), while §10.3 #11 says "The fair learned-vs-learned
gap is +$103.10 (cam_multisignal_learned vs ncc_intent_only, both fitted)." Both pairs are fitted, but
one contrast crosses classifier families (NCC vs interval). Suggest "matched-family learned arm" for
the +$103.10 contrast. (ii) The abstract and §10.1 attach "p = 5.16e-46" to both +$103.85 and +$103.10;
that p belongs to the +$103.85 contrast only (the +$103.10 contrast's own p is 1.60e-45, unreported in
the paper). Scope the p or report the second one.

**Assessment of 548 (question 2): arithmetically correct, materially sufficient, not exhaustive.**
The arithmetic checks (540 + 3 + 5 = 548), the 6-metric count matches `METRIC_KEYS` in the code, and
no conclusion is at risk: the largest claim-carrying p (8.5e-15) clears Bonferroni at 0.05/548 ≈ 9.1e-5
by ten orders of magnitude. But under a strict reading the family is miscounted in both directions:

1. **Undercount:** the robustness pipeline (`run_robustness_sweep` → `run_env` with
   `extra_agent_factories`) computes vs-baseline statistics for **12** comparators per environment —
   the two recalibrated variants are included in `stats_vs_baseline` — so the computed confirmatory
   family is 12 × 6 × 9 = **648**, not 540. Separately, the 9 per-environment situation_only−oracle
   F3 tests (§8.4) and the 2 §9.2.1 near-equivalence tests (p = 1.3e-13, p = 2.5e-04) are excluded.
   The α-sweep tests are excluded as exploratory — defensible, and §9.2.1 says so.
2. **Overcount:** the "+5 context-blind policies" contribute **zero p-values** — §8.7 reports
   descriptive profits only. Padding the denominator with untested policies is harmless
   (conservative), but the count "5" is itself unverifiable: the §8.7 table shows **4** constant
   policies plus the cam_multisignal reference row, the search grid is undocumented, and the code is
   not committed (see below). If "5" counts table rows, it is a miscount (the reference agent is not
   context-blind).
3. **One overbroad sentence:** "all p-values remain far below any reasonable correction" is falsified
   by the paper's own §9.2.1 caveat p = 2.5e-04 (cam_multisignal vs cam_multisignal_learned), which
   does not survive 0.05/548. The affected statement is a *caveat* (near-identical agents are still
   statistically distinguishable at n = 50) — failing the correction there would only *strengthen*
   the paper's "economically negligible" reading — but the sentence should be scoped to the family,
   or the exception noted.

**Bottom line on G:** resolved in substance — the denominator is explicit, conservative where padded,
and no finding depends on the residual count ambiguity. One sentence of scoping closes it fully
(e.g., "548 covers the vs-baseline family plus ablation contrasts; the recalibration variants (108
further tests), per-environment F3 contrasts, and near-equivalence checks all clear correction as
well, except the §9.2.1 caveat, whose failure to survive correction is itself the point").

---

## New-Content-Verification (§8.7 and §9.2 #25)

I re-implemented the policy search from scratch against the committed environment (constant
(action, channel, bid) agents; no RNG consumption, so pairing is unperturbed) and ran: (a) the four
tabled policies, default preset, 50 seeds × 200 scenarios; (b) a full grid sweep over all 5 action
types × 5 channels × 30 bids (0.05–1.5); (c) the best policy vs all deployable context-aware agents
across all 9 presets via `run_env`.

**Every number in §8.7 is internally consistent and correct.**
- All four tabled rows reproduce **to the cent**: 35.1% match for all (EXPLORATION mass 0.35 →
  EDUCATIONAL is its ideal action; match depends only on action type), profits +$252.41 / +$236.46 /
  +$214.62 / −$15.38. The monotone profit-in-bid ordering on EMAIL is mechanically correct (cost =
  0.05 × bid per moment; reward nearly bid-invariant at these levels).
- The arbitrage mechanism is verified in code: `BASE_REWARDS` is keyed by (action_type, situation)
  only — reward is channel-independent — while `ACTION_COSTS` gives EMAIL $0.05 (cheapest) vs SEARCH
  $1.20. §9.2 #25's description is exact.
- **"Best context-blind policy" is a true argmax**: over the full 750-policy grid, EDUCATIONAL|EMAIL|
  bid 0.30 is the winner (runner-up: same policy at bid 0.35, −$56 per 10,000 evaluations; best
  non-EDUCATIONAL: COMPARISON|EMAIL|0.3, lower by ~$294). The claim does not overstate the search.
- **"In 7 of 9 environments" is exact**: the policy beats every deployable context-aware agent
  (cam_inferred, cam_learned, cam_multisignal, cam_multisignal_learned — and noisy80, which is
  stronger than required) in 7 presets; it loses `retention_heavy` (+$177.3 vs cam_multisignal_learned
  +$237.3) and `concave_returns` (+$398.1 vs cam_multisignal +$675.5). My per-preset deployable-agent
  numbers also reproduce §8.4's table throughout, so §8.7 and §8.4 are mutually consistent.
- The "deployable" scoping is correct and necessary: `situation_only` (+$294.27) beats the arbitrage
  policy but requires ground-truth labels (§9.2 #3), so excluding it from "deployable" is right —
  though a one-clause footnote ("the label-requiring situation_only still dominates") would preempt
  the reader's discovery.

**Two defects, one of them blocking:**

1. **§8.7 is not regenerable from the committed code (blocking for a benchmark submission).** The
   footer (line 661) asserts "context-blind policy search regenerates from `paper/cam_sim_ablations.py`";
   that file contains only the three v0.9 experiments (majority floor, NCC intent-only, paired
   bootstrap) and was last modified at v0.9 — before §8.7 existed. `cam_sim.py` has no policy-search
   function, and Appendix B's regeneration command cannot produce the section. Every other section of
   this paper regenerates from committed code — the reproducibility contract is the paper's core
   selling point, and it is currently broken for exactly the newest headline result. Fix: commit the
   policy-search script (my 40-line reimplementation reproduces all rows, so the original cannot be
   large), or strike the footer claim. Until then, the "5 constant policies" count is also
   unverifiable (the table shows 4 constant policies + 1 reference agent).
2. **Unqualified "beats every context-aware agent" outside §8.7.** §8.7's body correctly says "in 7 of
   9 environments," but the abstract, §10.1, §9.2 #25, and the header contribution line drop the
   qualifier. In `retention_heavy` and `concave_returns` the claim is false as stated. Add the
   qualifier (or "in the default environment; 7 of 9 presets") in at least the abstract.

§9.2 #25 itself is a model limitation entry: accurate, cross-referenced (§10.3 #20, #19), and it
correctly demotes the paper's claim from "context-aware beats all context-free policies" to
"multi-signal beats single-signal within the context-aware ladder." This is the right scientific
move and I commend it.

---

## VERDICT

**ACCEPT — with two required pre-submission fixes (both mechanical).**

The round-4 recommendations are all implemented and verifiably correct: the arm disclosure is exact,
the learned-arm contrast (+$103.10, p = 1.60e-45) reproduces to the cent, the multiplicity
denominator is explicit and materially sufficient, and the abstract is trimmed (210 words). The new
§8.7 is methodologically sound and — verified by independent reimplementation — numerically perfect:
all four policies, the full-grid argmax, the reward/cost mechanics, and the 7-of-9 claim all
reproduce. Surfacing the channel-cost arbitrage as a benchmark-construction limitation (§9.2 #25,
§10.3 #20) rather than burying it is exactly the disclosure discipline this paper has maintained
across five rounds.

**Required before submission (no re-review needed):**
1. **Commit the §8.7 policy-search code** (or correct the footer and Appendix B). A Datasets &
   Benchmarks reviewer will run the regeneration commands; today §8.7 fails them.
2. **Restore the "in 7 of 9 environments" qualifier** in the abstract (and ideally §10.1, §9.2 #25,
   header).

**Recommended (non-blocking):** scope §7.3's "all p-values" sentence (the §9.2.1 caveat p = 2.5e-04
does not survive the 548-family correction — which supports, not undermines, the paper's reading);
reconcile "5 context-blind policies" with the 4 tabled policies; disambiguate the two
"learned-vs-learned" contrasts and scope the p = 5.16e-46 attribution in the abstract; fix the §8.2
vs §8.6 CI digit drift ($105.5 vs $105.44).

**Remaining blockers for journal-level (not benchmark-venue) submission:** Issue E (per-class
recall / macro-F1 under label noise, §10.3 #6) — unchanged since round 3, properly disclosed, and
still the largest open methodology gap; plus the channel-dependent reward rebuild (§10.3 #20), which
v1.0 itself now correctly identifies as v2.0 scope.

---

### Reproduction note

Independent reimplementation of §8.7 in temp-directory scripts (no repo files touched): constant-policy
agents evaluated through the committed `SimulationEnvironment.evaluate_action` (4 policies × 50 seeds ×
200 scenarios); vectorized 750-policy grid sweep on cached per-seed context features; 9-preset
comparison via `run_env` with the policy injected as an `extra_agent_factory`; learned-arm contrast via
`fit_ncc_intent_from_env` + `NCCIntentAgent`. All §8.7 and §8.6 numbers reproduce exactly; §8.4
deployable-agent profits reproduce throughout. The paper and code were not modified.
