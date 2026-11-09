---
title: Do Synthetic Personas Predict Real Audience Response? A Sim-to-Real Study Where a No-Persona Baseline
  Beats Persona-Based Copy Simulation
url: https://arxiv.org/abs/2609.25010
category: digital-marketing
subcategory: empirical
date: 2026-07
venue: ''
authors:
- Alexandre Cristovão Maiorano
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.25010
pages: 14
chars: 56180
fetched_at: '2026-11-08T13:21:48+00:00'
kb_version: 1
---

# Do Synthetic Personas Predict Real Audience Response? A Sim-to-Real Study Where a No-Persona Baseline Beats Persona-Based Copy Simulation

Do Synthetic Personas Predict Real Audience Response?
A Headline-Ranking Study with a Generic-Reader Baseline
Alexandre Cristov˜ ao Maiorano
alexandre@lumytics.com
Abstract
Do demographic personas improve an LLM’s prediction of audience engagement? We compare a fixed
ten-persona panel with a generic-reader baseline on Upworthy headlines, with supplementary news and
Reddit comparisons. The primary experiment collects Gemini 3.1 Flash-Lite and GPT-4.1 observations on
the same 190-package exploratory cohort, selected with simultaneous winner screening. It allocates thirty
scores per arm and variant within model, retains exact raw responses, and reports metric-specific valid and
paired counts. Complete-package coverage is 188 for Gemini and 188 for GPT-4.1. The baseline-minus-panel
Kendall τb gap is +0.222 (CI [+0.061, +0.385]) for Gemini and +0.257 (CI [+0.119, +0.391]) for GPT-4.1,
on respectively 136 and 188 valid rank pairs. Expected top-1 is 39.1% versus 54.8% for Gemini and 42.0%
versus 61.7% for GPT-4.1 (panel versus baseline). These intervals condition on the selected cohort and
recorded generations and do not adjust for dependence between related experiments. The Upworthy archive
documents a randomization-risk period. Excluding that period in a post-hoc sensitivity retains positive
expected top-1 and lift gaps in both configurations, while Gemini tau-b and Spearman intervals include zero.
Supplementary Reddit top-1 and captured lift favor the panel; these aggregate comparisons use unreconciled
collection protocols and do not isolate dataset effects. A raw-replay artifact supports offline reproduction
of the primary experiment. The results concern this panel, cohort, and protocol; they are not a held-out
evaluation or evidence of universal persona harm. Provider request protocols differ across models, and no
causal mechanism is isolated.
1 Introduction
LLM-based audience simulation offers a way to com-
pare messages before live testing. Demographic condi-
tioning can approximate aspects of survey samples [ 1],
but a copy-ranking system must predict measured
engagement. We study this narrower question with
Upworthy headline experiments [16].
We compare a fixed ten-persona panel with a
generic-reader baseline using a matched-budget exper-
iment on a simultaneously screened Upworthy cohort.
Both model configurations allocate the same num-
ber of scores to each arm and variant, preserve raw
responses, and report distinct rank and decision met-
rics with explicit denominators. The primary analysis
uses uniform expected credit for tied decisions and per-
metric paired contrasts; a post-hoc period-exclusion
sensitivity examines the archive’s documented ran-
domization risk. The cohort contains previously ex-
amined outcomes, so this is an exploratory evaluation
rather than a held-out test.
Supplementary evidence includes aggregate-report
comparisons and a GPT-4.1 scalar-checkpoint analysis.
These use different collection budgets, winner screens,
and tie rules and are reported separately from the pri-
mary comparison. Their evidential scope also differs:
reexporting an aggregate does not reconstruct its raw
observations, and replaying stored scalars cannot vali-
date absent response texts. Raw-backed reproduction
is available for the primary comparison; it does not
validate the supplementary generations or the other
datasets.
We ask (RQ1) how this panel and generic baseline
compare within tested packages, (RQ2) how agree-
ment varies with the observed outcome signal, and
(RQ3) what the dataset, aggregation, seed, and model
comparisons establish. This evaluates a specified har-
ness rather than all persona methods or audience
representativeness.
2 Related Work
Profile-conditioned models can approximate some ag-
gregate survey distributions [ 1]; broader computa-
tional social science applications raise validity ques-
tions [25]. Interview-grounded agents reproduce Gen-
eral Social Survey responses at approximately 85% of
participants’ own test–retest consistency in the origi-
nal version of Park et al. [19]. That result uses rich
1
arXiv:2609.25010v2  [cs.AI]  3 Nov 2026

individual grounding and a different outcome from
clicks.
Other work documents option-order sensitivity [ 5],
limited effects of persona attributes on subjective an-
notation, alongside modest significant gains in some
settings [10], persona-related degradation on objective
tasks [24], caricature [ 2], and biased outcomes from
generated personas [ 15]. Reasoning biases in persona-
assigned models are also documented [ 8]. These moti-
vate a baseline, but do not explain this study’s gap.
Upworthy [16] supports engagement analyses includ-
ing negativity effects [ 20]. LOLA [ 23] studies LLM-
assisted content experiments; differences in selection,
models, and evaluation prevent a direct numerical
comparison here. MIND [ 22] and Reddit reposts [ 14]
are additional observational settings, not interchange-
able headline experiments. Construct validity [ 4] dis-
tinguishes intent from behavior. Gamma [ 7] must
also be distinguished from Kendall correlation and its
treatment of ties [11, 12].
3 Sim-to-Real Validity Frame-
work
A package contains variants with observed outcome
rates and predicted scores (Figure 1). Upworthy was
designed for randomized traffic, but the archive au-
thors document randomization problems during part
of 2013–2014 [ 17]. We report observed rate rankings;
they are not automatically causal headline effects.
Grouping distinct headlines can also combine image
variants. MIND ranks different articles within a sub-
category by clicks divided by logged article appear-
ances, pooling user-level recommendation logs. Reddit
groups reposts by image and subreddit, pools votes
for identical titles, and uses upvotes divided by total
upvotes plus downvotes. This is a vote-approval ratio,
not CTR; vote totals are not exposure counts. Timing,
recommendation, and exposure remain uncontrolled
in these observational comparisons. Within-package
ranking does not establish absolute CTR calibration
or a causal copy effect in observational data.
Metric identity.For concordant and discordant
pair countsC, D, Goodman–Kruskal gamma is
γ= (C−D)/(C+D),
discarding pairs tied in either variable [ 7]. It is un-
defined when C + D = 0 and differs from Kendall τb,
which accounts for ties:
τb = C−Dp (C+D+T x)(C+D+T y) ,
where Tx, Ty count pairs tied only in the respective
variable [12]. Spearman uses average ranks [ 21]. Con-
stant rank inputs yield undefined values.
The primary experiment uses uniform expected top-
1 and bottom-1 credit: |Spred ∩S real|/|Spred| for the
corresponding extreme sets. Captured lift averages ob-
served rates across tied predicted maxima, then scales
distance from the observed minimum by the observed
range. Constant outcomes make lift undefined. Sup-
plementary aggregate-report top-1 results use the first
maximum and therefore depend on variant order.
4 Method Under Test
The study harness scores each headline with either a
demographic persona or a generic reader. It operates
independently of any commercial product. The fixed
ten-persona JSON takes inspiration from Upworthy-
era U.S. social-media demographics [9]. These descrip-
tors do not specify a deterministic behavioral-profile
generator or establish representativeness.
Elicitation and aggregation.The prompt re-
quests JSON with a click intent number in [0 , 1]
(Appendix A). Scores are averaged across recorded
observations:
bs(v) = 1 |Ov| X (i,d)∈Ov yi,d(v).
With complete draws this equals the mean over per-
sonas and draws. With missing draws it can dif-
fer from the supplementary aggregation mean, which
weights draw-collapsed personas equally. The sup-
plementary aggregation comparison evaluates these
alternative rules.
Sampling and parsing.The primary experiment
uses temperature 0 .8, three draws per persona and
thirty generic-reader draws per variant, with request
seeds recorded for both providers. The supplemen-
tary Gemini comparison uses the same nominal draw
allocation. The GPT-4.1 scalar-checkpoint analysis
instead uses three draws per persona versus ten base-
line draws; its requests sent no generation seed. Seeds
alone do not guarantee identical provider responses
over time.
Supplementary scalars were produced by a permis-
sive parser that could extract a first number, clamp
values, and accept booleans; event frequencies are un-
known. The matched-budget collector accepts only a
finite, non-boolean JSON number in range under the
exact requested key. Invalid parses are recorded as ter-
minal missing observations. Configuration hashes and
2

Observed variants
and outcomes
Winner
screening
Persona panel
mean score
Generic reader
mean score
Within-package
ranking metrics
and bootstrap CIs
Figure 1: Comparison protocol. Outcomes determine selection; the two scoring arms are compared within
selected packages. Supplementary aggregates use gamma and the top-versus-runner-up screen. The primary
experiment and GPT checkpoint analysis additionally report tau-b and simultaneous selection. Selection
does not establish that excluded packages are unpredictable.
separate protocol namespaces prevent mixing primary
checkpoints with supplementary scores.
5 Experimental Setup
Corpus.Upworthy rows are grouped by experiment
and distinct headline, aggregating identical text. Pack-
ages require at least two headlines and 3 ,000 impres-
sions per headline; sampling uncertainty matters in
online experiments [ 13]. The locked exploratory cor-
pus has 6978 variants in 1695 packages. In these
locked inputs, headline linebreaks were removed be-
fore grouping. One retained variant has such a line-
break in the source CSV; its package is outside both
selected cohorts. Exact locked strings define the saved
experiments, and the original manifests remain un-
changed.
Archive allocation risk and sensitivity.
The archive authors’ 2024 report identifies a
randomization-risk window from 25 June 2013
through 10 January 2014 inclusive [ 17]. The pre-
served CSV contains creation dates but neither
the documented problem flag nor a risk indicator.
Calendar-date overlap identifies 318 corpus packages,
83 supplementary-screen packages and 42 packages
in the primary selected cohort. These counts mark
window membership, not individually proven de-
fects. Bonferroni screening cannot repair allocation
problems.
A post-hoc offline sensitivity, specified after the
primary collection, excludes an entire experiment if
any row for that experiment in the preserved CSV
has a creation date that falls in that inclusive win-
dow, using the original date string without inventing a
timezone. Each model otherwise retains its complete
primary-package policy and the same recorded gen-
erations, metrics and bootstrap procedure. Primary
reports are preserved unchanged. Dates outside the
window are not a certification of valid randomization;
this sensitivity is not confirmatory or an independent
replication.
Simultaneous winner screen.The primary exper-
iment requires a unique observed maximum and com-
pares it with every opponent using two-sided pooled z
tests. For k variants the comparison family contains
m = k(k− 1)/2 unordered pairs. All winner–opponent
comparisons must pass α/m, with α = 0 .05. The
screening statistic is min(1, mmaxj̸=w pwj ). Bonfer-
roni’s inequality motivates the adjustment [ 18]. The
nominal bound is approximate and per package, con-
ditional on independent binomial observations, fixed
sampling horizons, and adequate normal approxima-
tion. It is not an across-package false-discovery guar-
antee or proof of a population winner. Repeated
exposures and Reddit voting further limit these as-
sumptions. In the locked corpus 190 packages pass,
all within the supplementary selected set described
below. A stricter screen does not demonstrate that
removed packages had false winners. The archive
documents editorial stopping based on accumulating
results [16]. Fixed-horizon p-values need not remain
calibrated under that stopping policy; Bonferroni does
not repair invalid input p-values. The screen defines
a reproducible cohort, without a verified five-percent
winner-error guarantee for these archived tests.
Supplementary winner screen.The supplemen-
tary aggregate comparisons use the observed best vari-
ant and runner-up, comparing them using a one-sided
pooled two-proportion z test at p < 0.05, selecting
399 packages. The direction was chosen from the data:
even a two-arm null comparison can pass in either
direction, so the nominal one-sided threshold does not
3

imply a five-percent false-positive rate. Comparing
only the runner-up need not separate a winner from
every opponent. Outcome selection changes the eval-
uation population. Packages failing a screen are not
thereby unpredictable.
Matched-budget collection.We froze the pro-
tocol and its source before collection. Both Gemini
3.1 Flash-Lite and Azure GPT-4.1 score every vari-
ant of the same 190-package simultaneously screened
exploratory cohort. This cohort was selected from
previously examined outcomes and is not a held-out
population. The matched-budget protocol is evalu-
ated on this Upworthy cohort only; MIND, Reddit,
other Upworthy splits, model tiers, seeds and aggrega-
tion rules are covered by the supplementary analyses,
which do not establish prompt robustness.
Each variant is allocated three observations for each
of ten fixed personas and thirty generic-reader obser-
vations. Package and variant order is shuffled with
a recorded seed; baseline/persona requests are inter-
leaved with randomized order within pairs. Tempera-
ture is 0 .8, JSON output is requested, and output is
limited to 64 tokens per choice. Gemini uses single-
choice requests with MINIMAL thinking. Azure uses
three indexed choices per request in both arms: ten
requests per arm and variant. We match the number
of retained scores within each model, not an identical
transport or inference protocol across providers. To-
ken use and monetary cost are not equalized. Choices
in one request are not assumed independent. Request
seeds, exact prompts, responses, returned model iden-
tities, usage, and failures are preserved. Provider
aliases and best-effort seeds do not establish future
replay of generations.
The primary analysis retains a package only
when every planned observation is valid in both
arms for all its variants. This also makes equal-
persona and observation-weighted panel means iden-
tical. Failures are never replaced with addi-
tional semantic draws; bounded retries address tran-
sient transport failures only. Available-observation
arm summaries are reported separately as sen-
sitivity analyses, with their own coverage, in
the available observation sensitivity field of
the committed Gemini and Azure reports in
recollection/2026-10-31/. The primary policy is
stricter than the scalar-checkpoint analysis require-
ment of at least one valid score per variant. Oper-
ational compatibility probes are retained separately
and excluded. An Azure prompt refusal initially trig-
gered a global HTTP400 stop. Before comparative
analysis, a documented technical amendment classi-
fied only the confirmed content-filter refusal type as
terminal missing while allowing unrelated planned re-
quests to continue. The blocked request is not retried
or rewritten; filtering remains active. Original journal
bytes, the pause, source versions and the amendment
marker are preserved. Other permanent failures and
budget stops remain blocking. This is a response to
an observed technical incident, not a preregistered
amendment. The fixed cohort closes before inspect-
ing comparative performance; there is no outcome-
dependent stopping or choice of model after observing
results.
Estimation and denominators.Primary pack-
age metrics are averaged without size weighting.
The displayed means describe the recorded pack-
ages. Bootstrap intervals summarize between-package
resampling variability conditional on the selection
rule and recorded scores; interpreting them for a
population of similarly selected experiments addi-
tionally assumes that these packages are exchange-
able independent units. Raw-backed reports in-
clude ntotal, nvalid, nundefined and metric-specific pack-
age IDs. Each paired gap uses packages valid in both
arms for that metric. Empty estimates are undefined,
not zero. Primary and period-exclusion percentile
bootstrap CIs use 10 ,000 package resamples, seed
42 [ 6]. They condition on selection and recorded
scores and omit generation, selection, and outcome-
measurement uncertainty. These are pointwise esti-
mation intervals, not simultaneous guarantees across
metrics or models. Resampling treats experiment IDs
as independent units. The archive also records follow-
up tests with shared content [ 16]; related IDs may
therefore be dependent. The intervals do not adjust
for such dependence, and their coverage as population
confidence intervals is not established. Supplementary
aggregate coefficient-specific valid counts are not fully
recorded; coverage totals are not those denominators.
Planning and robustness scope.We report coef-
ficient estimates and intervals without assigning stan-
dardized effect-size categories [ 3]. The analysis does
not establish prospective power for averages of within-
package coefficients or equivalence. Time-stamped
preregistration of all thresholds is not established.
Supplementary reports cover three Upworthy splits,
MIND [22], Reddit [ 14], three Gemini models, seed
runs, and aggregation. Prompt robustness is not eval-
uated by these artifacts. Reddit’s manifest records
many more selected packages than the evaluated sub-
set; its subset-selection procedure is undocumented.
4

Table 1: Primary Gemini 3.1 Flash-Lite comparison on 188 complete packages from the 190-package selected
cohort. Every retained variant has all planned observations in both arms. Counts are metric-specific valid
panel/baseline/paired packages. Gap is baseline minus panel; decision gaps use percentage points. Percentile
bootstrap CIs condition on this cohort and these recorded generations. Undefined coefficients are omitted
with their denominators disclosed.
Metric Panel [95% CI] Baseline [95% CI] Paired gap [95% CI]n valid p/b/pair
Goodman–Kruskalγ0.082 [-0.031, 0.192] 0.381 [0.253, 0.501] 0.268 [0.101, 0.434] 185/137/136
Kendallτ b 0.082 [-0.030, 0.191] 0.336 [0.214, 0.450] 0.222 [0.061, 0.385] 185/137/136
Spearmanρ0.100 [-0.016, 0.214] 0.371 [0.248, 0.488] 0.236 [0.069, 0.405] 185/137/136
Expected top-1 39.1% [32.2, 46.3] 54.8% [49.4, 60.2] 15.7 pp [7.1, 24.0] 188/188/188
Expected bottom-1 43.4% [36.4, 50.3] 47.5% [41.4, 53.6] 4.2 pp [-4.1, 12.3] 188/188/188
Captured lift 0.458 [0.394, 0.522] 0.591 [0.541, 0.641] 0.133 [0.054, 0.210] 188/188/188
6 Results
Primary matched-budget comparison (RQ1).
Tables 1 and 2 give the primary matched-budget ex-
periment. Supplementary comparisons below retain
their own protocols and evidence boundaries. The
complete-package policy retains 188 Gemini packages
and 188 GPT-4.1 packages; exclusions are respectively
2 and 2. Reports retain every planned observation
and failure, with metric-specific valid and paired IDs.
For Gemini, panel and baseline Kendall τb are 0.082
and 0.336; the paired baseline-minus-panel gap is
+0.222 (CI [+0.061, +0.385]) on 136 valid pairs. Ex-
pected top-1 is 39.1% versus 54.8%, with paired gap
+15.7 percentage points (CI [+7.1, +24.0]).
For GPT-4.1, panel and baseline Kendall τb are
0.088 and 0.345; the paired gap is +0.257 (CI [+0.119,
+0.391]) on 188 valid pairs. Expected top-1 is 42.0%
versus 61.7%, with paired gap +19.7 percentage points
(CI [+10.6, +28.7]). In Gemini, τb is undefined on
51 baseline packages and 3 panel packages. Marginal
means therefore use different valid sets; their difference
is not the paired gap. The paired rank comparison
uses their valid intersection, while top-1 includes ev-
ery complete package with expected credit for ties.
Baseline-minus-panel CIs exclude zero for the rank
metrics, top-1 and captured lift in both configurations;
bottom-1 CIs include zero. These are pointwise con-
ditional estimates. Gamma and τb have distinct rows
and denominators; neither is substituted for the other.
These conditional package-bootstrap intervals omit
repeated-generation uncertainty and do not compare
model families causally. The GPT scalar-checkpoint
analysis uses a separate collection protocol.
Post-hoc randomization-window sensitivity.
Table 3 excludes 40 Gemini and 41 GPT-4.1 com-
plete primary packages in the documented risk win-
dow, leaving respectively 148 and 147 packages. Ex-
pected top-1 gaps remain +11.4 percentage points (CI
[+1.7, +21.0]) and +22.4 points (CI [+12.2, +32.7]).
Captured-lift gaps also remain positive with pointwise
CIs excluding zero.
Gemini’s Kendall τb gap becomes +0.157 (CI [-0.030,
+0.346]) on 109 valid pairs; its tau-b and Spearman
intervals include zero. GPT-4.1’s tau-b gap is +0.272
(CI [+0.118, +0.425]) on 147 pairs. Thus the primary
Gemini rank contrast is not robust across this cohort
restriction and all rank estimators. Gamma remains a
distinct conditional measure; it is not substituted for
the uncertain tau-b result. Bottom-1 intervals include
zero for both models. These are post-hoc, pointwise
intervals, not an equivalence test.
Supplementary Upworthy comparison (RQ1).
Table 4 and Figure 2 give supplementary aggregate
estimates. The generic baseline has higher gamma
(0.361 versus 0.084) and top-1 (49.2% versus 34.6%).
These are conditional descriptions under the top-
versus-runner-up screen and tie rule. Marginal CIs
are not a paired test, and gamma is not assigned a
calibrated medium-effect interpretation.
Figure 3 shows the supplementary screening statis-
tic, not calibrated winner probabilities. The supple-
mentary all-package panel gamma is 0.054 (CI [0.025,
0.083]), with the aggregate-report metric and parsing
semantics.
Signal strength (RQ2).The pinned supplemen-
tary producer defines its separation index as 1 −p ,
where p is the one-sided observed-best-versus-runner-
up value, and correlates it with the panel’s first-index
top-1 hit. The stored Spearman association is 0.059
(CI [0.011, 0.107]) over 1678 packages, using 5 ,000
bootstrap resamples. Its code requires every variant
to have a score and within-package Spearman to be
defined, even for this top-1 analysis. The report alone
5

Table 2: Primary GPT-4.1 comparison on 188 complete packages from the 190-package selected co-
hort. Every retained variant has all planned observations in both arms. Counts are metric-specific valid
panel/baseline/paired packages. Gap is baseline minus panel; decision gaps use percentage points. Percentile
bootstrap CIs condition on this cohort and these recorded generations. Undefined coefficients are omitted
with their denominators disclosed. Azure requested three indexed choices per call; choices are not assumed
independent.
Metric Panel [95% CI] Baseline [95% CI] Paired gap [95% CI]n valid p/b/pair
Goodman–Kruskalγ0.088 [-0.026, 0.200] 0.345 [0.242, 0.445] 0.257 [0.119, 0.391] 188/188/188
Kendallτ b 0.088 [-0.026, 0.200] 0.345 [0.242, 0.445] 0.257 [0.119, 0.391] 188/188/188
Spearmanρ0.107 [-0.010, 0.222] 0.373 [0.265, 0.475] 0.266 [0.124, 0.404] 188/188/188
Expected top-1 42.0% [35.1, 48.9] 61.7% [54.8, 68.6] 19.7 pp [10.6, 28.7] 188/188/188
Expected bottom-1 43.1% [36.2, 50.0] 52.1% [44.7, 59.0] 9.0 pp [0.0, 17.6] 188/188/188
Captured lift 0.467 [0.400, 0.534] 0.654 [0.590, 0.719] 0.187 [0.103, 0.271] 188/188/188
Table 3: Post-hoc sensitivity excluding the archive’s documented randomization-risk window (25 June 2013–10
January 2014 inclusive) from each model’s complete primary cohort. Primary reports and recorded generations
remain unchanged. All six metrics are shown; gaps are baseline minus panel, decision gaps are percentage
points, and counts are metric-specific valid pairs. Pointwise percentile bootstrap CIs condition on retained
packages and generations; remaining tests are not certified defect-free.
Model (complete packages) Metric Paired gap [95% CI]n paired
Gemini (148) Goodman–Kruskalγ0.201 [0.010, 0.396] 109
Gemini (148) Kendallτ b 0.157 [-0.030, 0.346] 109
Gemini (148) Spearmanρ0.170 [-0.022, 0.367] 109
Gemini (148) Expected top-1 11.4 pp [1.7, 21.0] 148
Gemini (148) Expected bottom-1 3.1 pp [-6.4, 12.6] 148
Gemini (148) Captured lift 0.091 [0.001, 0.181] 148
GPT-4.1 (147) Goodman–Kruskalγ0.272 [0.118, 0.425] 147
GPT-4.1 (147) Kendallτ b 0.272 [0.118, 0.425] 147
GPT-4.1 (147) Spearmanρ0.292 [0.133, 0.450] 147
GPT-4.1 (147) Expected top-1 22.4 pp [12.2, 32.7] 147
GPT-4.1 (147) Expected bottom-1 8.8 pp [-0.7, 18.4] 147
GPT-4.1 (147) Captured lift 0.213 [0.117, 0.307] 147
cannot identify which excluded packages lacked scores
or had undefined ranks. This index mixes outcome
separation with exposure, and top-1 difficulty also
varies with the number of variants; the association is
unadjusted for those factors. It is not evidence of an
intrinsic predictability effect. Missing supplementary
predictions prevent recomputing the analysis under
simultaneous screening and expected tie credit; the
primary selected-cohort experiment does not estimate
this all-package association.
Dataset comparisons (RQ3).Table 5 shows
higher baseline gamma on the three Upworthy splits
and a smaller difference on MIND, where packages
compare articles. On Reddit, the panel has higher top-
1 (40.3% versus 30.2%) and lift (0.452 versus 0.333).
The available summaries show different directions, but
unreconciled collection and subset differences prevent
attributing this variation to the dataset alone. Reddit
gamma CIs include zero; this establishes neither equiv-
alence nor absence of a title-related signal. Posting
time and visibility were not tested as explanations.
Subset-selection and coverage limitations further re-
strict interpretation. The aggregate summary does
not record draw counts or evaluated package IDs,
so cross-dataset protocol equivalence is not indepen-
dently verified by those aggregates.
Seed, model, ties, and aggregation.The sup-
plementary three-seed SDs (0.025 for gamma; 0.008
for top-1) use the population convention over those
seeds, not sample SDs or precise general-variability
estimates. The baseline has higher gamma on three
tested Gemini tiers (Table 9, Appendix A); evaluated
6

Table 4: Supplementary Upworthy exploratory estimates under the top-versus-runner-up screen. Panel
ntotal = 399; baseline ntotal = 398; correlation-specific valid counts are unavailable. The stored rank coefficient
is Goodman–Kruskal gamma, not Kendall tau. Top-1 uses first-index tie breaking. Random top-1 reference
30.4%. Marginal 95% bootstrap CIs; the reported screen and decision tie rule are retained.
Method Top-1 [95% CI] Goodman–Kruskalγ[95% CI] Spearmanρ[95% CI]
No-persona baseline 49.2% [44.2, 54.3] 0.361 [0.289, 0.430] 0.350 [0.281, 0.417]
Persona panel 34.6% [29.8, 39.1] 0.084 [0.020, 0.147] 0.104 [0.035, 0.172]
Table 5: Supplementary estimates under the top-versus-runner-up screen and first-index tie breaking. ntotal
is panel/baseline coverage, not the correlation-specific valid count (unavailable). Lift is the fraction of the
observed outcome-rate range captured by the selected variant (panel/baseline). The panel exceeds the
baseline on Reddit lift and top-1 (discussed in text); near-zero gamma does not establish equivalence or
unpredictability. Gap is the difference of reported marginal gamma means, not a paired contrast. The
summary does not retain draw counts or evaluated package IDs; the exploratory row differs from Table 4,
and protocol equivalence cannot be verified from the aggregates alone.
Datasetn total p/b PersonaγBaselineγGap Lift p/b
Upworthy exploratory (2013–15) 399/398 0.079 0.361 +0.282 0.45/0.58
Upworthy holdout (2013–15) 402/401 0.100 0.398 +0.298 0.48/0.56
Upworthy confirmatory (2013–15) 1866/1864 0.070 0.393 +0.323 0.44/0.55
MIND news (2019) 74/74 0.177 0.214 +0.038 0.47/0.51
Reddit titles (2008–12) 600/599 -0.009 -0.026−0.017 0.45/0.33
T op-1 Goodman--Kruskal
 Spearman
0.0
0.1
0.2
0.3
0.4
0.5validity (estimate, 95% CI)
Supplementary Upworthy comparison
No-persona baseline
Persona panel
Figure 2: Supplementary comparison under the top-
versus-runner-up screen. Coefficient-specific valid
counts are unavailable. The displayed rank coeffi-
cient is gamma.
IDs are not retained to verify a shared subset. This
cannot establish universal model or prompt robust-
ness.
The tie report rounds scores before counting con-
stant packages; the rank code uses exact equality.
That count cannot recover excluded gamma values.
Undefined coefficients cannot be silently assigned zero,
and the reports do not justify a conservative-lower-
bound claim for the gap.
Table 6 preserves six supplementary aggregation
rules, all with lower reported gamma than the base-
0.0 0.1 0.2 0.3 0.4 0.5
one-sided p-value of the top-vs-runner-up CTR difference
0
50
100
150
200
250
300number of A/B tests
T op-vs-runner-up screen: 399/1695 packages selected
p = 0.05 cutoff
Figure 3: Supplementary one-sided top-versus-runner-
up screen selecting 399 packages. Selection of direction
from observed rates invalidates a literal one-sided false-
positive-rate interpretation. Nonsignificant packages
need not be unpredictable.
line. Equal-persona and observation-weighted means
can differ with missing draws. The reports do not
establish why their top-1 results differ, or whether
bias, sampling noise, scale, or another factor explains
relative performance.
GPT-4.1 scalar-checkpoint analysis.The re-
covered checkpoint contains scalars, not original re-
sponses. Offline replay of the pinned producer repro-
duces all published cross-family report fields within
7

Table 6: Supplementary aggregation comparison
(ntotal = 399 for panel rules). The baseline has
398 covered packages; correlation-specific valid counts
are unavailable. The mean row weights draw-
collapsed personas equally, whereas the primary col-
lector weights recorded observations equally. These
estimands can differ when draws are missing; the
stored reports do not identify the cause of their top-1
discrepancy. No tested rule reaches the baseline’s re-
ported gamma. This descriptive comparison does not
identify a failure mechanism. Top-versus-runner-up
screen, first-index tie breaking, 95% marginal boot-
strap CIs.
Aggregation Goodman–Kruskalγ[95% CI] Top-1 [95% CI]
No-persona baseline 0.361 [0.289, 0.430] 49.2% [44.2, 54.3]
Equal-persona mean 0.084 [0.020, 0.147] 34.8% [30.1, 39.3]
Panel median 0.141 [0.076, 0.205] 39.3% [34.6, 44.1]
Trimmed mean (20%) 0.081 [0.017, 0.144] 34.3% [29.6, 38.8]
Per-personaz-mean 0.064 [0.001, 0.128] 33.6% [29.1, 38.3]
Borda (rank fusion) 0.081 [0.018, 0.146] 35.3% [30.8, 40.1]
Condorcet (pairwise) 0.079 [0.014, 0.146] 35.8% [31.3, 40.6]
numerical tolerance. Collection coverage is 399 panel
and 395 baseline/paired packages. Thirty panel obser-
vations versus ten baseline draws and no generation
seed make it an unequal-budget comparison.
Table 7 applies simultaneous screening and tie-
aware estimators to those scores. Coverage becomes
190 panel, 189 baseline, and 189 paired packages. Base-
line Kendall τb is 0.325 versus 0.049. Paired CIs for
the displayed gaps exclude zero, supporting a positive
baseline gap in this checkpoint analysis. It is not an
independent replication or a budget-matched estimate,
and does not validate raw parsing. Gamma and tau-b
remain separate. The supplementary Gemini obser-
vations are unavailable for applying these estimators;
the primary Gemini comparison uses its own retained
generations and configuration.
7 Discussion and Limitations
The comparisons make a generic-reader baseline neces-
sary for this task. A persona panel adds assumptions
about audience composition and behavior that require
predictive validation. The primary matched-score
comparisons favor the baseline in valid rank compar-
isons, expected top-1 and captured lift, but do not
establish a bottom-1 advantage. Gemini rank means
exclude constant outputs with explicit arm-specific
counts; top-1 retains those packages through expected
tie credit. Supplementary Upworthy reports and the
GPT checkpoint analysis also favor the baseline; sup-
plementary Reddit decision metrics favor the panel.
Excluding the documented randomization-risk period
preserves the primary top-1 and lift contrasts but
leaves Gemini tau-b and Spearman uncertain. The
ranking conclusion therefore depends on cohort and
estimator, not just model configuration.
Mechanism remains open.The baseline may use
general headline knowledge, while role-play may add
unhelpful conditioning. Neither explanation was iso-
lated experimentally. Similar score spreads, selected
ranking examples, and rank-only aggregation failures
cannot distinguish bias from noise or identify a mech-
anism. The balanced, interleaved primary collection
tests the panel/baseline comparison with retained raw
responses, but does not separately manipulate de-
mographic content, role-play, or response noise. It
therefore does not by itself identify those mechanisms.
The archive measures clicks on Upworthy’s website,
while the prompt frames a social-media reader in 2014
and omits the image. This platform/time framing
is not an exact reconstruction of the test audience.
Intent versus engagement remains a construct-validity
limitation [4].
Ground truth and generalization.The
Upworthy archive documents a period of poten-
tially invalid randomization [17]; our selected cohort
includes affected-window tests. Our predictions rank
recorded outcome rates, and neither an adjusted
screen nor model responses establishes causal headline
effects. The post-hoc exclusion sensitivity addresses
one known risk window, not every possible allocation
or image confound. Editorial stopping and shared
content across follow-up experiments [16] add distinct
risks: the screen does not correct sequential moni-
toring, and the package bootstrap does not cluster
related experiment IDs. The preserved aggregate
outcomes do not reconstruct the stopping trajectories,
and dependence has not been quantified by an
article-level cluster analysis. Nominal intervals may
understate uncertainty. Simultaneous screening does
not make outcome measurements certain. Exclusion
changes the target population and relative task
difficulty. Failure to reject equality does not imply
no predictor can recover an ordering. MIND and
Reddit are observational; correlated exposures, time,
image, audience mix, and topic may matter. Training
contamination and generalization to current audiences
or other formats are not excluded by the archive
corpus.
Reproduction limits.Aggregate reports allow re-
export, not complete verification of their generating
process. Supplementary Gemini observations and
some aggregate-report producers were not recovered.
8

Table 7: GPT-4.1 scalar-checkpoint analysis on recorded post-parser values. Simultaneous winner screen and
uniform expected tie credit; marginal percentile bootstrap CIs. Gap is baseline minus panel on paired packages;
top-1 gap is in percentage points. Counts are per-metric valid panel/baseline/paired. Original responses are
unavailable, so this does not validate the collection parser. Sampling remains 30 panel observations versus 10
baseline draws per variant.
Metric Panel [95% CI] Baseline [95% CI] Paired gap [95% CI]n valid p/b/pair
Goodman–Kruskalγ0.049 [-0.061, 0.159] 0.325 [0.223, 0.429] 0.270 [0.132, 0.407] 190/189/189
Kendallτ b 0.049 [-0.061, 0.159] 0.325 [0.222, 0.429] 0.270 [0.132, 0.407] 190/189/189
Expected top-1 39.5% [32.6, 46.3] 60.6% [53.7, 67.7] 20.9 pp [11.1, 30.4] 190/189/189
The GPT checkpoint supports replay and partial re-
analysis, but range-checking stored scalars cannot
retroactively validate the permissive parser. The pri-
mary strict-parser observations have complete raw lin-
eage and matched within-model score budgets; they
are not mixed with supplementary scores. Azure
multi-choice and Gemini single-choice requests differ
operationally. Returned aliases are not immutable
model snapshots, and request seeds do not guarantee
determinism. A single collection session does not esti-
mate provider drift or generation variability. Content
filtering can cause exclusions associated with content
or arm; the Azure technical pause also divides its
collection in time. The outcome-selected cohort lim-
its generalization. Prompt robustness, deterministic
demographic-to-panel construction, full Reddit sub-
set lineage, and preregistration chronology remain
evidence gaps.
The artifact package distinguishes aggregate reex-
port, scalar-checkpoint analysis and raw-response re-
play, so each reported comparison can be assessed
within its available evidence.
8 Conclusion
This fixed demographic persona panel should be com-
pared with a generic-reader LLM baseline. The pri-
mary raw-retained comparison favors the baseline
on valid rank comparisons, expected top-1 and cap-
tured lift in both tested configurations. In the post-
hoc sensitivity excluding the archive’s documented
randomization-risk period, top-1 and lift gaps retain
positive pointwise intervals, but Gemini tau-b and
Spearman intervals include zero. The rank advan-
tage is therefore not uniformly supported across these
cohorts and estimators. In the primary comparison,
expected top-1 baseline-minus-panel gaps are +15.7
percentage points for Gemini and +19.7 for GPT-4.1.
Bottom-1 intervals include zero; a blanket advantage
across metrics is not established. Supplementary Red-
dit top-1 and lift favor the panel.
The comparison uses distinct rank metrics, expected
tie credit, and explicit valid and paired counts. We
provide a simultaneous winner screen and an offline
raw-replay artifact in the accompanying local replica-
tion bundle, prepared for deposition. Rank estimates
condition on valid coefficients, and all intervals con-
dition on selected packages and recorded generations.
Related-test dependence and editorial stopping re-
main unadjusted, limiting interval calibration and
winner-screen interpretation. Supplementary Gemini
observations remain unavailable. This study neither
establishes a general causal mechanism nor shows
universal persona harm.
Data and Code Availability
The package at https://github.com/alemaiorano
/sim-to-real-validity includes sources, exporters,
supplementary aggregate reports, the fixed panel, and
original corpus manifests. Reexporting these reports
reproduces their displayed numbers, not their gen-
eration from raw observations. Original reports are
hash-pinned and unchanged. GPT-4.1 checkpoint
analyses, input hashes, and offline replay verification
are in reanalysis/2026-10-31/. A separate replica-
tion bundle retains the GPT scalar checkpoint, exact
exploratory inputs, and the primary matched-budget
experiment: all raw response bytes, request and ob-
servation plans, immutable journal snapshots, cover-
age, package metrics, and source history. Committed
primary aggregate reports and hash provenance are
in recollection/2026-10-31/. Offline raw replay
needs no provider account. Supplementary Gemini ob-
servations remain missing; primary generations do not
restore them. REPLICATION.md distinguishes these ev-
idence tiers. The accompanying replication bundle is
prepared locally for deposition; it is not yet available
at the public repository URL.
9

Ethics and Conflict of Interest
The study uses public archive data and synthetic per-
sonas; no new human subjects were recruited. The
author has a commercial interest in copy-simulation
tools. This evaluates a study harness rather than a
specific product. Disclosure, adverse results, explicit
limitations, and available artifacts and the accompa-
nying local bundle support scrutiny; an unverified
preregistration chronology is not presented as a safe-
guard.
AI Tools Disclosure
This research used AI-assisted development tools for
manuscript preparation and code development under
human oversight and accountability.
• Language models:Claude (Anthropic, via Claude
Code) and GPT-family models (OpenAI, via Codex)
supported code implementation, analysis, literature
checks, and manuscript preparation and review. Au-
tomated manuscript feedback also supported the
review. The Google Gemini and Azure GPT-4.1
configurations evaluated in the study are experimen-
tal components, as described in the methods and
supplementary analyses; their outputs are study
observations.
• Web search:MCP Tavily and web search tools
supported literature review and fact-checking dur-
ing manuscript preparation.
The author retains full responsibility for the sci-
entific arguments, methodology, analysis, citations,
and conclusions. Numerical and literature claims are
checked against retained artifacts and primary sources;
AI-generated suggestions and automated reviews do
not constitute independent empirical validation.
References
[1] Lisa P. Argyle, Ethan C. Busby, Nancy Fulda,
Joshua R. Gubler, Christopher Rytting, and
David Wingate. Out of one, many: Using
language models to simulate human samples.
Political Analysis, 31(3):337–351, 2023. doi:
10.1017/pan.2023.2.
[2] Myra Cheng, Tiziano Piccardi, and Diyi Yang.
CoMPosT: Characterizing and evaluating car-
icature in LLM simulations. InProceedings
of the 2023 Conference on Empirical Methods
in Natural Language Processing, 2023. doi:
10.18653/v1/2023.emnlp-main.669.
[3] Jacob Cohen.Statistical Power Analysis for the
Behavioral Sciences. Routledge, 2nd edition, 1988.
doi: 10.4324/9780203771587.
[4] Lee J. Cronbach and Paul E. Meehl. Construct
validity in psychological tests.Psychological Bul-
letin, 52(4):281–302, 1955. doi: 10.1037/h00409
57.
[5] Ricardo Dominguez-Olmedo, Moritz Hardt, and
Celestine Mendler-D¨ unner. Questioning the sur-
vey responses of large language models. InAd-
vances in Neural Information Processing Systems,
pages 45850–45878, 2024. doi: 10.52202/07901
7-1458.
[6] B. Efron. Bootstrap methods: Another look at
the jackknife.The Annals of Statistics, 7(1):1–26,
1979. doi: 10.1214/aos/1176344552.
[7] Leo A. Goodman and William H. Kruskal. Mea-
sures of association for cross classifications.Jour-
nal of the American Statistical Association, 49
(268):732–764, 1954. doi: 10.1080/01621459.195
4.10501231.
[8] Shashank Gupta, Vaishnavi Shrivastava, Ameet
Deshpande, Ashwin Kalyan, Peter Clark, Ashish
Sabharwal, and Tushar Khot. Bias runs deep:
Implicit reasoning biases in persona-assigned
LLMs. InInternational Conference on Learn-
ing Representations (ICLR), 2024. URL https:
//arxiv.org/abs/2311.04892v2.
[9] Jesse Holcomb, Jeffrey Gottfried, and Amy
Mitchell. News use across social media platforms.
Technical report, Pew Research Center, 11 2013.
URL https://www.pewresearch.org/journa
lism/2013/11/14/news-use-across-socia
l-media-platforms/ . In collaboration with
the John S. and James L. Knight Foundation.
Accessed 2026-06-03.
[10] Tiancheng Hu and Nigel Collier. Quantifying the
persona effect in LLM simulations. InProceedings
of the 62nd Annual Meeting of the Association
for Computational Linguistics (Volume 1: Long
Papers), pages 10289–10307, 2024. doi: 10.18653
/v1/2024.acl-long.554.
[11] M. G. Kendall. A new measure of rank correlation.
Biometrika, 30(1/2):81–93, 1938. doi: 10.1093/
biomet/30.1-2.81.
[12] M. G. Kendall. The treatment of ties in ranking
problems.Biometrika, 33(3):239–251, 1945. doi:
10.1093/biomet/33.3.239.
10

[13] Ron Kohavi, Roger Longbotham, Dan Sommer-
field, and Randal M. Henne. Controlled exper-
iments on the web: survey and practical guide.
Data Mining and Knowledge Discovery, 18(1):
140–181, 2009. doi: 10.1007/s10618-008-0114-1.
[14] Himabindu Lakkaraju, Julian McAuley, and Jure
Leskovec. What’s in a name? understanding
the interplay between titles, content, and com-
munities in social media. InProceedings of the
Seventh International AAAI Conference on We-
blogs and Social Media, pages 311–320, 2013. doi:
10.1609/icwsm.v7i1.14408. 2013 proceedings;
publisher portal migration date is 2021.
[15] Ang Li, Haozhe Chen, Hongseok Namkoong,
and Tianyi Peng. LLM Generated Persona is
a Promise with a Catch, 2025. URL https:
//arxiv.org/abs/2503.16527v1.
[16] J. Nathan Matias, Kevin Munger, Mari-
anne Aubin Le Quere, and Charles Ebersole. The
upworthy research archive, a time series of 32,487
experiments in U.S. media.Scientific Data, 8(1):
195, 2021. doi: 10.1038/s41597-021-00934-7.
[17] J. Nathan Matias, Kevin Munger, Mari-
anne Aubin Le Quere, and Charles Ebersole. Au-
thor correction: The upworthy research archive,
a time series of 32,487 experiments in U.S. media.
Scientific Data, 11:765, 2024. doi: 10.1038/s415
97-024-03600-w.
[18] NIST/SEMATECH. e-handbook of statistical
methods: Bonferroni’s method. https://www.
itl.nist.gov/div898/handbook/prc/secti
on4/prc473.htm . Accessed 2026-10-31; used
for the multiplicity principle, not the binomial
approximation.
[19] Joon Sung Park, Carolyn Q. Zou, Aaron Shaw,
Benjamin Mako Hill, Carrie Cai, Meredith Ringel
Morris, Robb Willer, Percy Liang, and Michael S.
Bernstein. Generative agent simulations of 1,000
people, 2024. URL https://arxiv.org/abs/24
11.10109v1.
[20] Claire E. Robertson, Nicolas Pr¨ ollochs, Kaoru
Schwarzenegger, Philip P¨ arnamets, Jay J.
Van Bavel, and Stefan Feuerriegel. Negativ-
ity drives online news consumption.Nature
Human Behaviour, 7(5):812–822, 2023. doi:
10.1038/s41562-023-01538-4.
[21] C. Spearman. The proof and measurement of
association between two things.The American
Journal of Psychology, 15(1):72–101, 1904. doi:
10.2307/1412159.
[22] Fangzhao Wu, Ying Qiao, Jiun-Hung Chen,
Chuhan Wu, Tao Qi, Jianxun Lian, Danyang
Liu, Xing Xie, Jianfeng Gao, Winnie Wu, and
Ming Zhou. MIND: A large-scale dataset for
news recommendation. InProceedings of the 58th
Annual Meeting of the Association for Compu-
tational Linguistics, pages 3597–3606, 2020. doi:
10.18653/v1/2020.acl-main.331.
[23] Zikun Ye, Hema Yoganarasimhan, and Yufeng
Zheng. LOLA: LLM-assisted online learning al-
gorithm for content experiments.arXiv preprint
arXiv:2406.02611, 2024. URL https://arxiv.
org/abs/2406.02611v3.
[24] Mingqian Zheng, Jiaxin Pei, Lajanugen Lo-
geswaran, Moontae Lee, and David Jurgens.
When “a helpful assistant” is not really helpful:
Personas in system prompts do not improve per-
formances of large language models. InFindings
of the Association for Computational Linguistics:
EMNLP 2024, pages 15126–15154, 2024. doi:
10.18653/v1/2024.findings-emnlp.888.
[25] Caleb Ziems, William Held, Omar Shaikh, Jiaao
Chen, Zhehao Zhang, and Diyi Yang. Can large
language models transform computational social
science?Computational Linguistics, 50(1):237–
291, 2024. doi: 10.1162/coli a 00502.
A Persona Panel, Prompt, and
Reproducibility Details
Fixed panel.The ten-persona JSON is the repro-
ducible input. Demographic inspiration [ 9] is not
a deterministic recipe for recreating behavioral de-
scriptions. The unweighted panel is not an estimated
population sample.
First-person template.
You are simulating a specific person reacting to
a news headline on social media in 2014.
Person: {description} (age {age_group},
{gender}, mainly on {platform}, news engage-
ment:{news_engagement}.)
Headline:"{headline}"
As this exact person, how likely are
you to click this headline? Respond
ONLY with JSON: {"click_intent":
<number between 0 and 1>}.
The primary panel condition uses this first-person
template; the generic-reader condition uses the base-
line template below. Each is sent as a single user
11

message, without a system message. The exact tem-
plates, including spacing, quotation marks and im-
plemented alternative framings, are authoritative in
the versioned collector. A prompt implementation
alone does not establish a completed experiment. The
primary collection uses fixed 2014 framing for all head-
lines, including those created outside that year; it is
not a date-specific audience reconstruction.
Generic-reader baseline template.
You are a typical U.S. social-media news reader
in 2014.
Headline:"{headline}"
How likely are you to click this headline? Re-
spond ONLY with JSON: {"click_intent":
<number between 0 and 1>}.
Both templates retain the U.S./2014 framing. The
baseline specifies a generic reader role; its distinction
from the panel is the absence of the fixed demographic
profiles, not the absence of all role conditioning. Lit-
eral spacing, persona fields, and request prompts are
retained in the collector and raw request plans. The
interpolated persona fields are description, age group,
gender, platform, and news engagement, all shown in
Table 11. Political lean is stored metadata and is not
separately interpolated.
Coverage and checkpoints.Coverage policies dif-
fer by analysis. The GPT scalar-checkpoint analysis
requires at least one recorded score for every vari-
ant, with means over available observations. The pri-
mary matched-budget experiment requires all planned
scores in both arms for a retained package. Termi-
nal failures, request/choice indices, and exclusions
are preserved. Configuration and source hashes pre-
vent mixing protocols. Each Azure request has one
seed shared by its three returned choices; there is
no invented per-choice seed. GPT scalar-checkpoint
collection requests did not send a seed.
Raw artifact and replay .The primary collector
appends and fsyncs a request record before dispatch
and retains the exact response bytes, status, usage,
version, and parsing outcome afterward. Hash-chained
journals are synchronously mirrored. Unknown out-
comes after interruption remain unknown and are not
silently regenerated. Offline analysis validates the
request plan, input hashes, response hashes, and jour-
nal chain, then reparses the same immutable snapshot
whose hash identifies the report. The replication bun-
dle contains that snapshot, all inputs, request plans,
aggregate reports, source history, and the retained
GPT scalar checkpoint. Replaying saved bytes re-
quires no provider account and does not assert that
future generations will match.
Supplementary outcome construction.MIND
aggregates the supplied news and behavior logs by
article ID, counting appearances in recommendation
lists and click labels across users. Articles need at
least 200 appearances; within each subcategory, at
most ten are retained by appearance count, with at
least two per package. Reddit aggregates identical
titles within image/subreddit pairs, requires at least
300 total votes per title, and retains at most ten titles
by vote count. Upvotes are the numerator and total
upvotes plus downvotes the denominator, regardless
of the schema’s clicks/impressions names. These
inputs cover the supplied logs, not a matched exposure
window or common audience. Original manifests and
the pinned corpus builders specify the transformations;
missing evaluated IDs prevent fully reconciling the
supplementary samples.
Supplementary pilot and model comparison.
Tables 8 and 9 retain the pilot and cross-tier gap;
shared package IDs are not retained in those sum-
maries. Overlap of pilot CIs does not establish equiv-
alence. The supplementary Upworthy comparison
uses Gemini 3.1 Flash-Lite. No cost comparison is
available from the pilot report.
Headline-ranking examples and panel.
Table 10 shows supplementary reported cases
where the baseline found the observed winner and
the panel did not; they are not representative causal
evidence. Table 11 presents the fixed panel descrip-
tions. Full fields and grounding notes remain in
data/persona panel.json.
12

Table 8: Supplementary pilot with reported coverage ntotal = 100 packages per model. Evaluated IDs and
coefficient-specific valid counts are unavailable; a shared subset cannot be verified. The intervals overlap;
this is not an equivalence test. The stored pilot contains no cost measurements and does not establish
cost-effectiveness. 95% bootstrap CIs.
Model Top-1 Goodman–KruskalγSpearmanρ
gemini-2.5-flash0.390 [0.29, 0.49] 0.116 [-0.01, 0.24] 0.133 [-0.01, 0.27]
gemini-3.1-flash-lite0.330 [0.24, 0.42] 0.035 [-0.10, 0.17] 0.051 [-0.09, 0.19]
gemini-3.5-flash0.390 [0.29, 0.49] 0.122 [-0.01, 0.25] 0.139 [-0.00, 0.28]
Table 9: Supplementary cross-model comparison with reported coverage ( ntotal = 100 per condition). The
baseline has higher reported gamma on these three tested Gemini models. This does not establish a model-
independent effect. Evaluated IDs and correlation-specific valid counts are unavailable; a common subset
cannot be verified from this summary. Gap is the difference of reported marginal gamma means, not a paired
contrast.
Model PersonaγBaselineγGap
gemini-3.1-flash-lite0.035 0.401 +0.367
gemini-2.5-flash0.116 0.219 +0.103
gemini-3.5-flash0.122 0.404 +0.282
Table 10: Supplementary reported examples of ob-
served winning headlines that the no-persona baseline
ranked first but the persona panel did not (of 126 such
cases). These are selected illustrations, not evidence
of a systematic causal mechanism.
Real winning headline CTR #var
Bookmark This For When You’re
Sad And Instantly Be 100 Times
Happier
1.38% 4
10 Amazing International Photos
That Will Give You Some Perspec-
tive
1.92% 4
If You Saw Someone Bullying A Kid
For Being Gay Would You Speak
Out...
1.11% 2
If You Watch Hilary Swank Annoy A
Whiny Senator,$1 Will Go To Pun...
1.67% 3
Seven Wonderful People Share Se-
crets That Are Killing Them. This
C...
1.99% 4
A 9-Year-Old Asks McDonald’s CEO
A Simple Question. She’s Not
Lovin...
3.23% 4
Did These Words Really Come Out
Of Conan’s Mouth?
4.45% 3
We Use This Word So Often We
Probably Don’t Realize We’re Say-
ing It...
1.68% 4
Did You Know You Can Go For A
Swim In Google Earth?
0.88% 3
Cookie Monster Is In Jail? I’m Actu-
ally Really Happy About The Reas...
2.30% 4
13

Table 11: Prompt fields of the fixed persona panel ( P= 10), inspired by Upworthy-era audience U.S. social-
media demographics [ 9], with the verbatim behavioural descriptions used in the prompt. F/M denotes
female/male. Political lean is retained as metadata in the replication package ( data/persona panel.json)
and is not separately interpolated.
ID Demographics News en-
gagement
Behavioural description (verbatim)
p01 18-29, F, Face-
book
incidental 29-year-old woman, scrolls Facebook on her phone during breaks;
clicks human-interest and feel-good stories shared by friends;
rarely seeks news directly.
p02 18-29, M, Twit-
ter
active 24-year-old man, heavy Twitter user, follows journalists and
culture accounts; clicks surprising or contrarian takes; low toler-
ance for clickbait he’s seen before.
p03 30-49, F, Face-
book
incidental 38-year-old working mother, checks Facebook in the evening;
drawn to headlines about family, health, and local impact; shares
uplifting or outrage-inducing stories.
p04 30-49, M, Reddit active 41-year-old man, browses Reddit and Facebook; skeptical of
sensational headlines, clicks when a headline promises concrete
information or a strong narrative payoff.
p05 50-64, F, Face-
book
incidental 57-year-old woman, mostly on Facebook; clicks emotionally
resonant stories and anything about social causes she follows;
less drawn to internet-slang headlines.
p06 50-64, M, Face-
book
moderate 60-year-old man, reads news on Facebook and cable; clicks
political and economic headlines, distrusts overtly hyped ’you
won’t believe’ framing.
p07 18-29, F,
YouTube
incidental 22-year-old college student, video-first, on YouTube and Insta-
gram; clicks visually evocative or identity-relevant headlines;
very sensitive to authenticity.
p08 30-49, M, Face-
book
incidental 45-year-old man, casual Facebook user; clicks curiosity-gap head-
lines that promise a quick interesting fact, especially maps, lists,
and ’what happened next’ stories.
p09 65+, F, Face-
book
moderate 68-year-old retiree, active on Facebook with family; clicks heart-
warming, nostalgic, or cause-driven stories; avoids headlines that
feel like tricks.
p10 30-49, F, Twit-
ter
active 34-year-old professional, follows news and advocacy on Twitter;
clicks data-driven or justice-oriented angles; fatigued by repeti-
tive viral formats.
14
