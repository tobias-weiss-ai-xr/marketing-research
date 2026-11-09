---
title: Competence-Gated Pooling of Language Models and Priors for Event Forecasting
url: https://arxiv.org/abs/2609.12101
category: ai-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Aditi Tiwari
- Aashrith Bandaru
- Heng Ji
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.12101
pages: 18
chars: 74221
fetched_at: '2026-11-08T13:20:55+00:00'
kb_version: 1
---

# Competence-Gated Pooling of Language Models and Priors for Event Forecasting

When Do Language Models Add Value? Relative Competence in Hybrid
Event Forecasting
Aditi Tiwari and Aashrith Bandaru and Heng Ji
University of Illinois Urbana-Champaign
Urbana, Illinois, USA
aditit5@illinois.edu, hengji@illinois.edu
Abstract
When a forecasting system already has a predic-
tion from a market, crowd, or statistical model,
when should it use a language model? Stan-
dalone accuracy cannot answer this question
because a less accurate model may still improve
the existing forecast. We study this distinc-
tion through relative competence, separating a
model’s replacement advantage from its com-
plementary value. Under Brier loss (squared er-
ror between predicted probabilities and binary
outcomes), we characterize when model dis-
agreement can correct external forecast errors
and derive the population gain from regime-
specific affine pooling. We introduce a compe-
tence gate that estimates source weights from
resolved outcomes, shrinks regime-specific esti-
mates toward a global solution, and chronolog-
ically recalibrates the pooled forecast. Across
4,974 resolved binary questions and four lan-
guage models, the best standalone model has
24.94% higher Brier loss than the calibrated ex-
ternal forecast, yet the gate improves that refer-
ence by 3.35% (95% CI, 1.80–4.90%). Model
contributions vary across forecasting regimes,
with larger corrections in thinner markets and
forecasting crowds and smaller corrections in
higher-participation settings. The gate also
shows no statistically detectable performance
difference from more flexible contextual ag-
gregators. These results demonstrate that stan-
dalone superiority is not necessary for com-
plementary predictive value and that language
models should be evaluated relative to the fore-
casts already available.
1 Introduction
Consider forecasting whether the Federal Reserve
will cut interest rates at its next meeting. Suppose a
prediction market assigns a 70% probability, while
a language model (LM) predicts 55%. Should a
forecasting system use the LM’s prediction? The
answer depends not only on which source is more
accurate, but also on whether their errors differ in
useful ways. A less accurate LM may still iden-
tify information missing from the market forecast.
This question matters because forecasting systems
often already have predictions from markets, hu-
man crowds, or statistical models (Wolfers and
Zitzewitz, 2004; Mellers et al., 2014; Satopää et al.,
2014b; Halawi et al., 2024). The deployment prob-
lem is therefore not simply whether an LM fore-
casts well, but whether it improves the prediction
already available.
Forecast combination has long studied how
differently informed predictions can reduce er-
ror (Bates and Granger, 1969; Granger and Ra-
manathan, 1984; DeGroot and Fienberg, 1983;
Strähl and Ziegel, 2017). Learned aggregation
methods, including stacking, extend this frame-
work by optimizing how predictive distributions
are combined (Yao et al., 2018). Recent hybrid sys-
tems also combine model-generated forecasts with
human or market predictions and report improve-
ments over individual sources (Benjamin et al.,
2023; Alur et al., 2025; Kim et al., 2026). However,
aggregate improvements do not establish when an
LM should influence an existing forecast or when
that forecast should be largely preserved. The
distinction matters because a market, forecasting
crowd, and statistical model may already capture
different amounts of the information available to
an LM. We therefore study how the incremental
value of LM predictions varies across forecasting
regimes and whether that variation can be estimated
from resolved outcomes.
We formalize this question throughrelative com-
petence, the predictive value of an LM conditional
on an available external forecast. We distinguish
replacement advantage, which measures whether
the LM is more accurate than the external source,
fromcombination value, which measures whether
their forecasts can be combined to reduce error.
Under Brier loss (squared error between predicted
probabilities and binary outcomes), we show that
1
arXiv:2609.12101v2  [cs.AI]  13 Oct 2026

Will the Fed cut
rates at its next
meeting?
External0.70
LM 0.55
LM does not see
the external forecast.
(a) New question
.4
 0 .4
Disagreement d = f g
.15
0
.15
Ext. error e = g y
(b) Resolved history by source (schematic)
Polymarket: slope = 0.09
.4
 0 .4
Disagreement d = f g
INFER: slope = 0.32
.50 .55 .60 .65 .70
Predicted probability
0.69
Polymarket
0.65
INFER
(c) Same forecasts, by source
(d) History resolved questions Fit weights global + per source Shrink sparse sources  global
 Pool and clip
keep in [0, 1]
Calibrate
chronological isotonic
Figure 1: Overview. (a) A question receives an external forecast and an independently elicited LM forecast. (b)
Schematic resolved histories illustrate how the relationship between external error and model disagreement can differ
across source-defined regimes. (c) The same hypothetical forecasts illustrate different source-specific corrections
before calibration. (d) The gate fits global and source-specific weights from resolved outcomes, shrinks sparse
estimates toward the global solution, then pools, clips, and chronologically calibrates forecasts.
complementary value depends on whether LM dis-
agreement systematically corrects external forecast
errors (Brier, 1950; Gneiting and Raftery, 2007).
We also derive the population gain from regime-
specific rather than global affine pooling. This
characterization explains why standalone superior-
ity is not necessary for complementary value and
why different external sources can favor different
model contributions.
We introduce acompetence-gated forecast pool
that estimates source coefficients from previously
resolved questions. The method fits global and
regime-specific affine combinations, shrinks esti-
mates from sparse regimes toward the global so-
lution, and recalibrates the pooled forecast using
chronological out-of-sample predictions (Zadrozny
and Elkan, 2002). The LMs forecast independently
of the external probability, allowing their additional
information to be evaluated without first exposing
them to that source. Figure 1 illustrates the method.
Unlike self-reported confidence, the fitted coeffi-
cients reflect historical forecasting errors and pro-
vide an inspectable account of how each source
contributes to the combination.
We evaluate four LMs from the gpt-oss (OpenAI,
2025) and Llama (Grattafiori et al., 2024) fami-
lies on 4,974 resolved binary questions spanning
markets, forecasting crowds, and structured fore-
casting tasks. The best standalone LM has 24.94%
higher Brier loss than the calibrated external fore-
cast, yet the competence gate achieves a 3.35%
improvement over the external reference. Matched
regime-specific pooling also improves on global
affine pooling, although this smaller routing gain
is secondary. More flexible contextual aggrega-
tors achieve similar predictive accuracy. Impor-
tantly, model-side corrections decrease as market
participation or crowd size increases. One possi-
ble explanation is that broader external aggrega-
tion leaves less complementary information for the
LM, although participation does not directly mea-
sure forecast accuracy. Independent elicitation also
preserves complementary information: revealing
the external forecast reduces measured combina-
tion value from 0.00153 to 0.00072. Historical
comparative competence also improves on verbal
confidence in a separate diagnostic (Xiong et al.,
2024). Together, these findings show that useful
model influence depends on the competing infor-
mation source, rather than standalone accuracy or
confidence alone.
Our contributions are threefold.
1. We provide controlled evidence that individ-
ually weaker LMs improve stronger external
forecasts, and that this complementary value
varies across sources and participation levels
and roughly halves when the LM sees the ex-
ternal forecast.
2. We formalize relative competence, separat-
ing replacement advantage from combination
value, and characterize when disagreement
corrects external forecast errors under Brier
2

loss.
3. We develop a chronological competence-gated
pool that estimates interpretable, shrinkage-
stabilized source corrections from resolved
outcomes.
2 Related Work
LLM forecasting and hybrid systems.Retrieval,
aggregation, and post-cutoff evaluation have im-
proved LLM forecasting (Halawi et al., 2024;
Schoenegger et al., 2024; Turtel et al., 2025;
Karger et al., 2025; Cheng et al., 2026). Hybrid
systems combine LM forecasts with markets or
crowds (Alur et al., 2025; Kim et al., 2026; Barot
and Borkhatariya, 2026). Alur et al. (2024) study
complementary human expertise in algorithmic pre-
diction. We instead ask when an LM adds infor-
mation beyond an existing external forecast. Our
question-only, retrieval-free forecasts isolate this
contribution from search quality.
Forecast combination and conditional pool-
ing.Classical work studies forecast combina-
tion and encompassing (Bates and Granger, 1969;
Clemen, 1989; Ranjan and Gneiting, 2010; Chong
and Hendry, 1986; Harvey et al., 1998). Con-
ditional predictive ability examines performance
given an information set (Giacomini and White,
2006). Weak standalone models can also contribute
through aggregation (Peng et al., 2026). Contextual
and hierarchical pooling allow weights to vary (Yao
et al., 2022; Oelrich et al., 2024; Johnson and West,
2025; McAlinn et al., 2020). Our contribution is
not a new pooling algorithm. We characterize com-
plementary value under Brier loss and quantify the
gain from regime-specific rather than global affine
pooling.
Confidence, selective prediction, and defer-
ral.Confidence methods assess model uncer-
tainty (Xiong et al., 2024). Selective prediction
and deferral study withholding or handing off pre-
dictions (Mozannar and Sontag, 2020; Geifman
and El-Yaniv, 2017; Cortes et al., 2016). Forecast
evaluation also requires leakage control (Paleka
et al., 2025). We instead evaluate comparative com-
petence: whether historical signals identify when
model information improves an external forecast,
both in combination and selective ranking.
3 Problem Setup
Forecasting Setting.We study binary event fore-
casting when a system already has a probabil-
ity estimate from an external source. Question
i has text xi, forecast time ti, resolved outcome
yi ∈ {0,1}, and outcome-availability time si. The
system has an external forecast gi ∈[0,1] and
forecasts fim ∈[0,1] from M language models.
External forecasts may come from prediction mar-
kets, forecasting crowds, or statistical models. In
the primary protocol, a language model sees the
question, forecast date, and resolution criteria but
notg i.
Each question has an observed regime ki ∈ K.
We use external-source identity as the primary
regime because it is known when the forecast is
made. Define the S=M+ 1 source probabilities
as pi = [gi, fi1, . . . , fiM ]⊤.(1)
We evaluate probabilities using Brier loss (Brier,
1950; Gneiting and Raftery, 2007), with population
and regime-specific risks
B(h) =E[(h−y) 2],
Bk(h) =E[(h−y) 2 |k]. (2)
Lower risk is better. The calibrated external com-
parator is denoted gcal i . We use raw gi to analyze
disagreement and replacement advantage, but com-
pare the deployed gate against chronological gcal i
so improvements due only to external calibration
are not attributed to LMs.
Relative Competence.We userelative compe-
tenceto describe the predictive value of a language
model given an external forecast. Two targets an-
swer different questions.
Replacement advantagemeasures whether a
model should be used instead of the external prob-
ability: ∆rep k =B k(g)− Bk(f).(3)
A positive value indicates lower standalone
model risk. Replacement advantage does not mea-
sure whether the model can improve a combination.
Combination valuemeasures the best popula-
tion improvement from an affine adjustment ofg us-
ing disagreement with f. Following linear forecast
combination (Bates and Granger, 1969; Granger
and Ramanathan, 1984), define
hλ =g+λ(f−g), λ∈R.(4)
Its regime-specific combination value is
∆comb k =B k(g)−inf λ∈R Bk(hλ).(5)
The unconstrained affine score is an analytic
device and need not lie in [0,1] . The deployed
3

estimator clips before returning a probability. Com-
bination value can be positive even when replace-
ment advantage is negative. Thus, the deployment
question is not simply which forecaster has lower
standalone error, but whether model disagreement
helps correct errors in the available forecast.
With multiple models, an affine pool has score
p⊤ i w subject to 1⊤w= 1 . Individual coefficients
may be signed. The theory first studies one model
to make the source-relative gain explicit, then the
method fits allSsources.
4 Relative Competence Under Brier Loss
When Disagreement Adds Value.Let d=f−g
denote disagreement and e=g−y denote external
error. In regime k, write Ak =E k[d2] and Mk =
Ek[de]. Expanding the affine Brier risk gives
Rk(λ) =E k[(e+λd) 2] =B k(g) + 2λMk +λ 2Ak.(6)
For Ak >0 , the optimal coefficient and improve-
ment are
λ⋆ k =− Mk Ak ,∆ comb k = M 2 k Ak .(7)
When Ak = 0 , the two forecasts agree almost
surely in regime k. We set λ⋆ k = 0 by convention,
and the regime contributes no combination value
or routing gain.
When Mk <0 , a positive model coefficient
moves the pool in the direction of the model fore-
cast. When Mk >0 , a negative coefficient moves
it in the opposite direction. If Mk = 0, the optimal
affine adjustment is zero. Disagreement magnitude
alone therefore does not establish complementary
value. The relevant quantity is its signed relation-
ship with external forecast errors.
Gain from Regime-Specific Pooling.Let πk =
Pr(k) and suppose P k πkAk >0 . The optimal
single global coefficient is
λ⋆ G =
P
k πkAkλ⋆ kP
k πkAk
.(8)
Proposition 1 (Affine routing identity).The
reduction in population risk obtained by using
regime-specific optimal coefficients instead of the
optimal global coefficient is
X
k
πkRk(λ⋆ G)− X
k
πkRk(λ⋆ k) = X
k
πkAk(λ⋆ k −λ ⋆ G)2.
(9)
The identity follows by completing the square
around each regime optimum. It shows that regime-
specific pooling can outperform one global coef-
ficient when the regimes prefer different correc-
tions. It does not guarantee that estimated regime
weights improve out-of-sample forecasts. Proposi-
tion 1 concerns the unregularized population affine
score before clipping and recalibration. We give the
proof and multi-source extension in Appendix H.
5 Competence-Gated Forecast Pool
We learn a global source combination and regime-
specific corrections from resolved outcomes, then
shrink each regime estimate toward the global esti-
mate. This keeps the estimator interpretable while
limiting variance in small regimes. Figure 1 illus-
trates the architecture.
Chronological Weight Estimation.At forecast
time ti, only earlier questions with available out-
comes and admissible source forecasts can be used:
Hi ={j:s j < ti,p j admissible}.(10)
Admissibility requires the historical external prob-
ability and model input to contain no information
recorded after the respective forecast time. The
primary model probabilities are cutoff-controlled
question-only hindcasts rather than live historical
model submissions. Their provenance and this lim-
itation are described in Section 6.
Given a nonempty historical set, the global affine
weights solve a zero-target ridge problem:
ˆwG,i = arg min
1⊤w=1
n 1
|Hi|
X
j∈Hi
(p⊤ j w−y j)2 +ρG,i∥w∥2 2
o
.
(11)
For either historical set T , we use ρT =
10−3 tr( ˆΣT )/S, where ˆΣT =|T |−1 P j∈T pjp⊤ j .
The penalty is centered at zero, and source proba-
bilities are not standardized. The coefficients may
be negative and represent signed error corrections,
not source-reliability probabilities.
For regime k, set Hi,k ={j∈ H i :k j =k}
and nk,i =|H i,k|. When nk,i >0 , fit ˆwk,i by
replacing Hi with Hi,k in Eq. 11 and calculating
its own penalty ρk,i from that historical set. Both
estimators use mean squared loss and the same
coefficient constraint.
Regime Shrinkage.The gate interpolates between
the estimates using the number of resolved exam-
ples in the current regime:
αk,i = nk,i
nk,i +τ , ˜wk,i = (1−α k,i) ˆwG,i +α k,i ˆwk,i.
(12)
We fix τ= 50 in the primary evaluation. At 50
resolved regime questions, the estimates receive
equal interpolation weight. The factor αk,i mea-
sures the amount of regime-specific history used
for shrinkage, not a model’s probability of being
4

correct. The forecast contributions follow from the
fitted ˜wk,i.
Prediction, Calibration, and Fallback.For ques-
tion i, the raw affine score and probability projec-
tion are
qi = ˜w⊤ ki,ipi,¯q i = clip[0,1](qi).(13)
The returned probability is hi =C i(¯qi), where
Ci is a chronological isotonic calibrator (Zadrozny
and Elkan, 2002).
The calibrator Ci is fitted on historical out-of-
sample predictions. For each earlier question j, we
generate its prediction using only Hj and the same
weight-fitting and fallback rules as the deployed
gate. At time ti, isotonic calibration uses only
the resulting clipped predictions and outcomes for
which sj < ti. Historical predictions are never
recomputed using weights fitted after their forecast
times. This prevents leakage through calibration.
When fewer than Nhist = 150 globally resolved
examples are available, the system returns hi =g i.
When global history is sufficient but the current
regime has no history, it uses the global affine pool.
The calibrator is the identity until Ncal = 150 eli-
gible historical out-of-sample scores are available.
These are fixed deployment rules, not selected us-
ing current outcomes. Clipping to [10−6,1−10 −6]
is used separately for logit transforms and log loss,
not for the affine Brier score.
6 Experimental Setup
Questions, Sources, and Forecast Provenance.
The primary development population contains
4,974 complete binary questions from nine source-
defined regimes, representing 4,119 event or se-
ries clusters. The separate locked population con-
tains 1,173 questions from 947 clusters. Markets
contribute 2,941 questions from Polymarket and
Manifold (Polymarket, 2024; Manifold Markets,
2024). Crowds contribute 1,513 questions from
INFER and ForecastBench-derived crowd ques-
tions (INFER Platform, 2024; Karger et al., 2025).
Structured sources contribute 520 questions from
FRED, ACLED, Wikipedia, DBnomics weather,
and Yahoo Finance (Federal Reserve Bank of St.
Louis, 2024; Armed Conflict Location & Event
Data Project (ACLED), 2024; Wikimedia Foun-
dation, 2024; DBnomics, 2024; Yahoo Finance,
2024). These groups allow us to evaluate the same
deployment decision against collective forecasts
and quantitative time-series priors. Source counts
and the inclusion audit appear in Appendix B.
For market and crowd questions, gi is the latest
recorded probability at or beforeti, or the explicitly
supplied point-in-time probability. We never inter-
polate from a later snapshot. Participation measure-
ments are likewise taken at or before ti. Structured
priors use historical observations available at ti.
For FRED, these are the latest ALFRED vintages
available by that date, not subsequently revised
values.
The primary language-model probabilities are
generated retrospectively ascutoff-controlled
question-only hindcasts. They are not contempo-
raneously recorded live submissions. We require
the assigned model knowledge cutoff to precede
the question’s forecast date by at least 31 days and
exclude post-ti evidence from its input. This re-
duces known forms of leakage but cannot prove
that model pretraining lacked all relevant outcome
information. The registry comprises 6,269 records:
4,974 development questions, 1,173 locked ques-
tions, 120 gap questions, and two invalid primary-
panel parses. The row-level provenance manifest
and filtering rules appear in Appendix B.
Model Panel and Elicitation.The primary panel
contains gpt-oss-20b, gpt-oss-120b, Llama-3.1-8B-
Instruct, and Llama-3.3-70B-Instruct. These mod-
els allow us to examine relative competence across
two families and multiple model sizes. Each re-
ceives the question, forecast date, and resolution
criteria without the external probability or retrieval.
Primary predictions use temperature zero and are
parsed into one probability. Complete elicitation
settings appear in Appendix C.
External Forecasts and Calibration.For struc-
tured sources, gTS i is the equal-weight mean of
valid event probabilities from persistence, ETS,
ARIMA, and a local-level state-space model.
ACLED adds a Poisson or overdispersed negative-
binomial count component. At least two compo-
nents must be valid. Otherwise, the prior is the
same-horizon empirical event probability with Jef-
freys smoothing. This fallback is used on 20 of 520
structured questions. The conversion of predictive
distributions into binary event probabilities is given
in Appendix D.
We compare against a chronological external-
only Platt reference learned from the same eligible
resolved history without LM inputs. The gate re-
ceives the raw external probability, while the cali-
brated reference controls for improvements achiev-
able without combining sources. An external-only
isotonic comparator, evaluated on the same 4,974
5

questions, obtains 0.07556 Brier versus 0.07573 for
Platt calibration. Appendix F gives both calibration
procedures and the fallback rules.
Baselines and Matched Controls.We evalu-
ate individual models, an LLM-only pool, global
combinations, and regime-specific combinations.
Matched simplex and signed affine comparisons
hold source inputs and calibration fixed while vary-
ing the coefficient constraint and whether weights
depend on regime. The calibrated global affine
pool isolates the contribution of routing, while the
calibrated external-only baseline tests incremental
hybrid value.
We also evaluate Local Prediction Pools, regime-
aware logistic stacking, hierarchical logistic stack-
ing, and an XGBoost router. These alternatives use
the same forecast-time information and provide
more flexible aggregation rules. Their features, reg-
ularization, and chronological fitting procedures
are specified in Appendix F. They serve as accu-
racy controls rather than methods the simpler gate
is assumed to outperform.
Chronological Protocol, Hyperparameters, and
Tests.We replay predictions in forecast-time or-
der. An outcome becomes eligible for fitting only
after its recorded resolution-availability time. The
primary gate uses the fixed shrinkage and ridge
settings defined in Section 5. We vary τ and the
ridge multiplier only in sensitivity analyses, begin-
ning after at least 300 resolved historical examples.
The sensitivity grid and numerical safeguards are
reported in Appendix G.
The primary endpoint is the mean paired Brier
improvement over calibrated external forecasts:
∆1 = bB(gcal)− bB(hgate),(14)
where bB denotes the empirical mean Brier loss on
the evaluation population. We also report Brier
skill, 1− bB(hgate)/ bB(gcal). The secondary routing
endpoint is
∆2 = bB(hG)− bB(hgate),(15)
where hG uses global affine weights with matched
isotonic calibration. The separate raw routing diag-
nostic compares unprojected, uncalibrated global
and regime affine scores.
We report paired event-clustered uncertainty
with Wald intervals. Full inference procedures and
power checks appear in Appendix L. Routing is
a secondary endpoint, and its confidence interval
Method Brier↓ BSS (%)↑
External and LM-only
Calibrated external (reference) 0.07573 0.00
Best standalone LM 0.09461−24.94
Optimized LM-only pool 0.08731−15.30
Matched hybrid pools
Global affine + isotonic 0.07428 1.91
Regime simplex + isotonic 0.07386 2.47
Competence gate (ours) 0.07319 3.35
Flexible aggregators
Local Prediction Pools 0.07316 3.40
Hierarchical stacker 0.07308 3.49
Regime-aware logistic stacker 0.07306 3.52
Contextual XGBoost 0.07302 3.57
Table 1: Brier score and Brier skill score (BSS) on the
common 4,974-question population. BSS is measured
relative to the chronologically calibrated external fore-
cast.Bold: ours; underlined: lowest Brier. The gate
improves the reference by 3.35% (95% CI 1.80–4.90%);
differences from flexible aggregators are not statistically
significant.
includes gains smaller than the prespecified 0.001
Brier threshold of practical interest.
Development ends December 31, 2025. We ex-
clude January 1 through February 25, 2026 to sep-
arate development from locked evaluation, while
event-disjoint splits prevent overlap in underlying
targets. Locked evaluation begins February 26,
2026 and is used as a consistency check, not for
method selection.
7 Results
Weaker Standalone Models Improve the Exter-
nal Forecast.On the 4,974-question development
population, the best standalone LM obtains 0.09461
Brier, 24.94% higher loss than the calibrated exter-
nal forecast at 0.07573. The optimized LM-only
pool also performs worse than the external refer-
ence. Standalone superiority is therefore not neces-
sary for complementary value.
The competence gate reduces Brier to 0.07319,
a gain of 0.00254 or 3.35% Brier skill (95% CI
for the gain [0.00136, 0.00371]; p= 2.24×
10−5). The external-only isotonic comparator ob-
tains 0.07556 Brier, so the gain does not vanish
under matched calibration families. Table 1 reports
the matched comparisons.
Flexible contextual aggregators achieve slightly
lower Brier point estimates, but the reported paired
comparisons do not establish a significant differ-
ence from the gate. The gate therefore offers an
interpretable source-level combination rather than
a demonstrated accuracy advantage over flexible
stacking. Its fitted coefficients make the historical
corrections attributed to each source explicit.
6

Pool Global Regime Gain↑
Affine, raw 0.07510 0.07406 0.00104
Simplex, isotonic 0.07475 0.07386 0.00089
Affine, isotonic0.074280.07319 0.00109
Table 2: Matched global and regime-specific pooling
comparisons (Brier). Gain is global minus regime-
specific Brier; positive values favor regime-specific
pooling. The raw affine row uses scores before clipping
and recalibration.Bold: the deployed gate configura-
tion.
Regime Conditioning Contributes Beyond
Global Pooling.We isolate regime conditioning by
comparing global and regime-specific pools with
identical inputs, coefficient constraints, and cali-
bration. Table 2 shows positive regime-specific
gains under all three matched configurations. The
raw affine improvement is 0.00104 Brier before
clipping and recalibration. With matched isotonic
calibration, the routing gain is 0.00109 Brier, with
a 95% confidence interval of [0.00033, 0.00186]
and pairedp= 0.00504.
Routing explains only part of the full hybrid
improvement. The calibrated regime simplex ob-
tains 0.07386 Brier, compared with 0.07319 for the
signed affine gate, indicating an additional contribu-
tion from the coefficient constraint. Recalibration
also improves the final pool. The routing result is
secondary because its confidence interval includes
gains below the prespecified 0.001 Brier threshold
of practical interest.
Complementary Value Depends on the Exter-
nal Source.Complementary value varies across
the nine forecasting regimes. The gate improves
Manifold by approximately 0.00371 Brier, the
ForecastBench-derived crowd subset by 0.00305,
and INFER by 0.00477. In contrast, the Polymarket
gain is approximately 0.00038, with a confidence
interval spanning zero. The smaller correction is
consistent with limited additional model informa-
tion in this market setting, although it does not
establish that every Polymarket forecast is stronger.
Structured questions provide a separate test
against quantitative time-series priors. Across 520
questions, the calibrated classical ensemble ob-
tains 0.17374 Brier, compared with 0.16909 for
the hybrid, a gain of 0.00465. FRED has a posi-
tive source-level improvement, while the smaller
structured groups have less precise estimates. DB-
nomics weather and Yahoo Finance show near-zero
gains with intervals spanning zero. These results
indicate that the gate’s value depends on the com-
Source n External Gate
Polymarket 1,904 0.06008 0.05971
Manifold 1,037 0.073100.06939
ForecastBench crowd 912 0.058200.05515
INFER 601 0.071600.06683
FRED 214 0.167840.15995
ACLED 72 0.15493 0.14907
Wikipedia 61 0.14087 0.13651
DBnomics weather 78 0.15008 0.14996
Yahoo Finance 95 0.24181 0.24149
Table 3: Brier scores by external-source regime.Bold:
gate improvement whose event-clustered 95% confi-
dence interval excludes zero. The ForecastBench crowd
row identifies the dataset distribution source while re-
taining the underlying crowd regime. Counts sum to
4,974. Confidence intervals appear in Appendix I.
peting source and is not uniformly positive across
forecasting tasks.
Model Contribution Falls with Market and
Crowd Participation.We examine whether partic-
ipation is associated with the correction assigned to
LM forecasts. Market volume and trader count, or
the number of crowd forecasters, provide forecast-
time participation proxies. After ranking these mea-
surements within each source, we form four equal-
count bins from 4,454 market and crowd questions.
Because the affine source weights sum to one,
the net model-side coefficient for questioniis
λeff i =
MX
m=1
˜wki,i,m = 1−˜wki,i,g.(16)
Here ˜wki,i,g denotes the external-source coefficient,
and ˜wki,i,m denotes the coefficient of model m.
Mean net model-side affine correction coefficients
decrease from 0.20179 in the lowest-participation
quartile to 0.02860 in the highest, a difference of
0.17319 (95% CI, [0.09820, 0.24819]). A sep-
arate scalar later-held-out participation diagnos-
tic shows declining Brier gains from 0.00199 to
0.00015 across these bins. Its weighted mean gain
is 0.00104, distinct from the 0.00229 gain of the
full multi-model gate on the market and crowd pop-
ulation. Figure 2 shows both trends.
The negative association also appears in a regres-
sion controlling for source identity, forecast hori-
zon, and external probability extremity. Higher-
participation markets and larger crowds thus re-
ceive smaller model-side corrections in the evalu-
ated sources. This is consistent with broader exter-
nal aggregation leaving less complementary infor-
mation, but participation is not a direct measure of
accuracy and the relationship is observational.
7

Q1
Lowest
Q2 Q3 Q4
Highest
Within-source participation quartile
0.00
0.05
0.10
0.15
0.20Mean net LM coefficient
0.202
0.149
0.083
0.029
(a)  Model-side coefficient
Q1
Lowest
Q2 Q3 Q4
Highest
Within-source participation quartile
0.000
0.001
0.002
0.003Brier gain over raw external
0.00199
0.00133
0.00070
0.00015
(b)  Held-out hybrid gain
Figure 2: Participation and LM correction across 4,454
market and crowd questions. (a) Mean net signed LM
coefficient by within-source participation quartile. (b)
Brier gains over the raw external forecast from a sep-
arate scalar diagnostic, evaluated on the later 20% of
questions within each source-quartile. Error bars show
95% confidence intervals, and the horizontal line marks
zero gain. Participation is not a direct measure of accu-
racy, and the association is observational.
Historical Confidence as a Secondary Diagnos-
tic.Historical comparative competence predicts
individual-model wins over the raw external fore-
cast with model–question-pair AUC 0.681, com-
pared with raw verbal-confidence AUCs of 0.463–
0.501. It also improves question-level selection
of hybrid benefit, with relative AURC −0.00502
versus −0.00295 for history-oriented verbal con-
fidence. This diagnostic does not feed the gate;
definitions and comparisons appear in Appendix K.
Temporal and Mechanism Checks.The sep-
arate locked evaluation shows a positive but
inconclusive gain of 0.00227 Brier (95% CI,
[−0.00040,0.00494] ) across 1,173 questions. Its
interval includes zero. Raw routing and sensitivity
checks are reported in Appendices H, G, and L.
8 Discussion and Conclusion
Our findings show that forecasting competence de-
pends on the information already available. Under
Brier loss, a weaker standalone LM can improve an
external forecast when its disagreement systemati-
cally corrects external errors. The competence gate
learns inspectable source-specific corrections from
resolved outcomes and improves a calibrated exter-
nal forecast while achieving accuracy comparable
to more flexible aggregators. Model-side correc-
tions decrease with market and crowd participation,
although this relationship is observational. These
findings support evaluating LMs by their comple-
mentary value rather than standalone accuracy or
self-reported confidence. Hybrid systems should
preserve strong external forecasts when historical
evidence does not support additional corrections.
Further discussion appears in Appendix A.
Our results shift the deployment question from
whether an LM is a better forecaster to whether it
contributes information beyond an existing predic-
tion. Relative competence provides a way to char-
acterize this value, while historical source-specific
corrections offer a practical way to estimate it. The
broader implication is that hybrid forecasting sys-
tems should adapt model influence to the compet-
ing information source rather than assign uniform
trust to LMs.
9 Limitations
Our evaluation covers resolved binary questions
from nine forecasting sources. Generalization to
continuous outcomes, other information sources,
and different event distributions remains untested.
Smaller source populations limit estimation preci-
sion, and shrinkage cannot guarantee adaptation to
changing source quality or capture finer question-
level relationships. The primary LM forecasts
are cutoff-controlled retrospective hindcasts rather
than live predictions. Historical eligibility restric-
tions reduce identifiable leakage but cannot rule
out training-data contamination or errors in infor-
mation availability. The routing gain remains sec-
ondary, and the locked evaluation is insufficiently
powered for independent confirmation. Participa-
tion associations are observational, and the theo-
retical routing identity does not guarantee finite-
sample improvement. Finally, Brier-score gains
do not establish better downstream decisions or ac-
count for inference costs, latency, or consequences
of errors. Prospective evaluation is needed.
8

References
Rohan Alur, Manish Raghavan, and Devavrat Shah.
2024. Human expertise in algorithmic prediction.
InAdvances in Neural Information Processing Sys-
tems, volume 37.
Rohan Alur, Bradly C. Stadie, Daniel Kang, Ryan
Chen, Matt McManus, Michaela Rickert, Tyler Lee,
Michael P. Federici, Richard Zhu, Dennis Fogerty,
H.R. Williamson, Nina Lozinski, Aaron Linsky, and
Jasjeet S. Sekhon. 2025. Aia forecaster: Technical
report.ArXiv, abs/2511.07678.
Armed Conflict Location & Event Data Project
(ACLED). 2024. Armed conflict location & event
data. https://acleddata.com/. Accessed: 2026-
10-12.
Rajat M. Barot and Arjun S. Borkhatariya. 2026.
Polyswarm: A multi-agent large language model
framework for prediction market trading and latency
arbitrage.arXiv preprint arXiv:2604.03888.
J. M. Bates and C. W. J. Granger. 1969. The com-
bination of forecasts.Journal of the Operational
Research Society, 20:451–468.
Daniel M. Benjamin, Fred Morstatter, Ali E. Abbas,
Andres Abeliuk, Pavel Atanasov, Stephen Bennett,
Andreas Beger, Saurabh Birari, David V . Bude-
scu, Michele Catasta, Emilio Ferrara, Lucas Har-
avitch, Mark Himmelstein, KSM Tozammel Hossain,
Yuzhong Huang, Woojeong Jin, Regina Joseph, Jure
Leskovec, Akira Matsui, and 10 others. 2023. Hy-
brid forecasting of geopolitical events.AI Magazine,
44(1):112–128.
Glenn W. Brier. 1950. Verification of forecasts ex-
pressed in terms of probability.Monthly Weather
Review, 78(1):1–3.
Pu Cheng, Juncheng Liu, and Yunshen Long. 2026.
Polybench: Benchmarking llm forecasting and trad-
ing capabilities on live prediction market data.arXiv
preprint arXiv:2604.14199.
Yock Y . Chong and David F. Hendry. 1986. Economet-
ric evaluation of linear macro-economic models.The
Review of Economic Studies, 53(4):671–690.
Robert T. Clemen. 1989. Combining forecasts: A re-
view and annotated bibliography.International Jour-
nal of F orecasting, 5(4):559–583.
Corinna Cortes, Giulia DeSalvo, and Mehryar Mohri.
2016. Learning with rejection. InAlgorithmic Learn-
ing Theory.
DBnomics. 2024. Dbnomics: The world’s economic
database and api. https://db.nomics.world/.
Accessed: 2026-10-12.
Morris H. DeGroot and Stephen E. Fienberg. 1983. The
comparison and evaluation of forecasters.Journal of
the Royal Statistical Society: Series D (The Statisti-
cian), 32(1–2):12–22.
Federal Reserve Bank of St. Louis. 2024. Fed-
eral reserve economic data (fred) and vintage data
(alfred). https://fred.stlouisfed.org/. Ac-
cessed: 2026-10-12.
Yonatan Geifman and Ran El-Yaniv. 2017. Selective
classification for deep neural networks. InAdvances
in Neural Information Processing Systems (NeurIPS).
Raffaella Giacomini and Halbert White. 2006. Tests
of conditional predictive ability.Econometrica,
74(6):1545–1578.
Tilmann Gneiting and Adrian E. Raftery. 2007. Strictly
proper scoring rules, prediction, and estimation.
Journal of the American Statistical Association,
102(477):359–378.
C. W. J. Granger and Ramu Ramanathan. 1984. Im-
proved methods of combining forecasts.Journal of
F orecasting, 3(2):197–204.
Aaron Grattafiori et al. 2024. The llama 3 herd of mod-
els.arXiv preprint arXiv:2407.21783.
Danny Halawi, Fred Zhang, Yueh-Han Chen, and Jacob
Steinhardt. 2024. Approaching human-level forecast-
ing with language models. InAdvances in Neural
Information Processing Systems, volume 37.
David I. Harvey, Stephen J. Leybourne, and Paul New-
bold. 1998. Tests for forecast encompassing.Journal
of Business & Economic Statistics, 16(2):254–259.
INFER Platform. 2024. Infer crowd forecasting dataset
and platform. https://www.inferpub.com/. Ac-
cessed: 2026-10-12.
Matthew C. Johnson and Mike West. 2025. Bayesian
predictive synthesis with outcome-dependent pools.
Statistical Science, 40(1):109–127. Originally circu-
lated as arXiv:1803.01984 (2018).
Ezra Karger, Houtan Bastani, Yueh-Han Chen, Zachary
Jacobs, Danny Halawi, Fred Zhang, and Philip E.
Tetlock. 2025. ForecastBench: A dynamic bench-
mark of AI forecasting capabilities. InInternational
Conference on Learning Representations.
Sumin Kim, Jihoon Kwon, Yoon Kim, Nicole Ka-
gan, Raffi Khatchadourian, Wonbin Ahn, Alejan-
dro Lopez-Lira, Jaewon Lee, Yoontae Hwang, Oscar
Levy, Yongjae Lee, and Chanyeol Choi. 2026. Fore-
casting future language: Context design for mention
markets.Preprint, arXiv:2602.21229.
Manifold Markets. 2024. Manifold markets api
and dataset documentation. https://manifold.
markets/. Accessed: 2026-10-12.
Kenichiro McAlinn, Knut Are Aastveit, Jouchi Naka-
jima, and Mike West. 2020. Multivariate Bayesian
predictive synthesis in macroeconomic forecasting.
Journal of the American Statistical Association,
115(531):1092–1110.
9

Barbara A. Mellers, Lyle Ungar, Jonathan Baron, Jaime
Ramos, Burcu Gurcay, Katrina Fincher, Sydney E.
Scott, Don Moore, Pavel Atanasov, Scott A. Swift,
Terry Murray, Eric Stone, and Philip E. Tetlock.
2014. Psychological strategies for winning a geopo-
litical forecasting tournament.Psychological Sci-
ence, 25(5):1106–1115.
Hussein Mozannar and David Sontag. 2020. Consistent
estimators for learning to defer to an expert. InInter-
national Conference on Machine Learning (ICML).
Oscar Oelrich, Mattias Villani, and Sebastian Ankargren.
2024. Local prediction pools.Journal of F orecasting,
43(1):103–117.
OpenAI. 2025. Gpt-oss. https://openai.com/
index/introducing-gpt-oss/. Accessed: 2026-
10-12.
Daniel Paleka, Shashwat Goel, Jonas Geiping, and Flo-
rian Tramèr. 2025. Pitfalls in evaluating language
model forecasters.arXiv preprint arXiv:2506.00723.
Cheng Peng, Ruixi Luo, Zhi Chen, and Wei Tang.
2026. Two heads are better than one: Aggregating
weaker LLMs for better forecasts.arXiv preprint
arXiv:2609.33257.
Polymarket. 2024. Polymarket prediction market data
and api. https://polymarket.com/. Accessed:
2026-10-12.
Roopesh Ranjan and Tilmann Gneiting. 2010. Com-
bining probability forecasts.Journal of the Royal
Statistical Society: Series B.
Ville A. Satopää, Shane T. Jensen, Barbara A. Mellers,
Philip E. Tetlock, and Lyle H. Ungar. 2014b. Proba-
bility aggregation in time-series: Dynamic hierarchi-
cal modeling of sparse expert beliefs.The Annals of
Applied Statistics, 8(2).
Philipp Schoenegger, Indre Tuminauskaite, Peter S.
Park, Rafael Valdece Sousa Bastos, and Philip E.
Tetlock. 2024. Wisdom of the silicon crowd: LLM
ensemble prediction capabilities rival human crowd
accuracy.Science Advances, 10(45):eadp1528.
Christof Strähl and Johanna F. Ziegel. 2017. Cross-
calibration of probabilistic forecasts.Electronic Jour-
nal of Statistics, 11(1):608–639.
Benjamin Turtel, Danny Franklin, and Philipp
Schoenegger. 2025. LLMs can teach themselves
to better predict the future.arXiv preprint
arXiv:2502.05253.
Wikimedia Foundation. 2024. Wikipedia pageviews
and dump data. https://dumps.wikimedia.org/.
Accessed: 2026-10-12.
Justin Wolfers and Eric Zitzewitz. 2004. Prediction mar-
kets.Journal of Economic Perspectives, 18(2):107–
126.
Miao Xiong, Zhiyuan Hu, Xinyang Lu, Yifei Li, Jie
Fu, Junxian He, and Bryan Hooi. 2024. Can
llms express their uncertainty? an empirical eval-
uation of confidence elicitation in llms.Preprint,
arXiv:2306.13063.
Yahoo Finance. 2024. Yahoo finance market histori-
cal data api. https://finance.yahoo.com/. Ac-
cessed: 2026-10-12.
Yuling Yao, Gregor Pirš, Aki Vehtari, and Andrew Gel-
man. 2022. Bayesian hierarchical stacking: Some
models are (somewhere) useful.Bayesian Analysis,
17(4):1043–1071.
Yuling Yao, Aki Vehtari, Daniel Simpson, and Andrew
Gelman. 2018. Using stacking to average bayesian
predictive distributions (with discussion).Bayesian
Analysis, 13(3).
Bianca Zadrozny and Charles Elkan. 2002. Transform-
ing classifier scores into accurate multiclass proba-
bility estimates. InProceedings of the Eighth ACM
SIGKDD International Conference on Knowledge
Discovery and Data Mining, pages 694–699.
Impact Statement
Probabilistic forecasts support decisions in ar-
eas such as public policy, resource planning, fi-
nance, and disaster response. This work stud-
ies how language-model predictions can be com-
bined with forecasts that are already available from
other sources. Estimating complementary predic-
tive value may improve forecast aggregation and
help practitioners identify settings where additional
model predictions contribute limited information.
The proposed method also provides inspectable
source coefficients that can support analysis of his-
torical forecasting behavior.
Forecasting errors can have consequential ef-
fects, and historical competence does not guaran-
tee future reliability. Source quality may change,
model predictions may reflect incomplete or con-
taminated information, and evaluation datasets may
not represent the conditions of a particular deploy-
ment. The reported improvements concern proba-
bilistic forecasting accuracy, not downstream deci-
sion quality. Applications involving consequential
decisions require independent validation, ongoing
monitoring, and appropriate human oversight.
A Additional Discussion and Implications
Forecasting value is relative to the available in-
formation.Standalone accuracy is not sufficient
to determine whether a language model should be
used in a hybrid forecasting system. A model can
10

be less accurate than an external source yet provide
information that improves the combined forecast.
Our results demonstrate this distinction across mar-
kets, forecasting crowds, and structured prediction
tasks. The Brier-loss analysis identifies the underly-
ing condition: model disagreement is useful when
it systematically corrects errors in the external fore-
cast. This shifts the deployment question from
whether a model is the better forecaster to whether
it contributes information beyond what is already
available. The distinction also applies to forecast
combinations involving statistical models and hu-
man judgments, where the value of an additional
source depends on the information represented by
the existing ones.
Interpretable combination is useful even without
superior accuracy.The competence gate pro-
vides a simple way to estimate how source contri-
butions differ across forecasting regimes. Its coef-
ficients are learned from resolved outcomes, with
shrinkage limiting the influence of sparse regime
histories. The matched experiments show an addi-
tional benefit from regime conditioning, although
this contribution is smaller and less firmly estab-
lished than the overall hybrid gain. More flexi-
ble contextual aggregators achieve similar predic-
tive accuracy. The gate’s contribution is therefore
not a claim of universal superiority over stacking
methods. Beyond conventional pooling, we study
source-relative predictive value, characterize it un-
der Brier loss, and test source-conditioned correc-
tions using matched controls. The fitted coeffi-
cients make those corrections inspectable. This
makes the relationship between observed forecast-
ing errors and the resulting source weights easier
to examine.
Complementary value changes with the compet-
ing forecast.The measured benefit of language-
model forecasts varies across external sources. Im-
provements are small in the evaluated Polymarket
and near-zero-gain structured regimes. Within mar-
ket and crowd sources, higher participation is asso-
ciated with smaller model-side corrections, consis-
tent with less complementary information remain-
ing after external aggregation. This is an observa-
tional relationship, not evidence that participation
causes greater forecast accuracy. The confidence
results reinforce the same distinction between stan-
dalone performance and complementary value. His-
torical comparative signals are more informative
than raw verbal confidence, but predicting when an
individual model wins does not necessarily identify
when the hybrid improves. Together, these find-
ings support estimating model contributions from
resolved outcomes and the external forecasting con-
text rather than treating language-model confidence
or standalone rankings as sufficient deployment cri-
teria.
B Population Construction and
Point-in-Time Provenance
The registry contains 6,269 records: 4,974 devel-
opment complete cases, 1,173 questions in the sep-
arate locked population, 120 questions in the eight-
week gap, and two invalid primary-panel parses.
The development rows belong to 4,119 event or
series clusters. The locked population contains 947
event-disjoint clusters. Source counts are 1,904
Polymarket, 1,037 Manifold, 912 ForecastBench-
derived crowd, 601 INFER, 214 FRED, 72 ACLED,
61 Wikipedia, 78 DBnomics weather, and 95 Ya-
hoo Finance. A given event or series contributes
one resampling cluster even when it has several
forecast snapshots.
The canonical row-level manifest records
question_id, event_id, forecast_time,
resolution_available_time, regime, snapshot
timestamps and identifiers, ALFRED vintage
dates, model-cutoff eligibility, raw probabilities,
parsing-validity flags, split, forecast artifact hashes,
and event-cluster membership. The model record
additionally preserves model_id, question-text
hash, prompt hash, and generation commit. Source
values and participation proxies must be from at or
before ti. These fields determine every analysis
population and support an audit of information
available at the question timestamp. Because the
LLM predictions are retrospectively generated
hindcasts, cutoff eligibility is a contamination
control rather than evidence that the forecasts were
recorded live.
ForecastBench provenance.The 912-question
crowd subset was obtained from the publicly re-
leased ForecastBench dataset (Karger et al., 2025),
rather than collected through the original forecast-
ing platform’s API. We retain the underlying source
identity for regime construction and historical ag-
gregation. The ForecastBench dataset repository
distributes its data under CC BY-SA 4.0. Dataset
attribution and the frozen release identifier are re-
tained in the provenance manifest.
11

C Model Input and Reproducibility
The primary panel has two gpt-oss and two Llama
instruct models. The frozen cutoff assignment is
June 1, 2024 for gpt-oss. For the month-level De-
cember 2023 cutoff reported for Llama 3.1 and 3.3,
we conservatively use December 31, 2023 when
applying the 31-day eligibility buffer. Every el-
igible question satisfies the 31-day buffer. The
input contains only question text, resolution crite-
ria, and forecast date, with no external probability,
retrieval, or post-date evidence. The primary out-
put is one parsed probability at temperature zero.
The gpt-oss models use medium reasoning effort
and a 4,096-token output limit. The Llama models
use their native chat templates and a 1,024-token
output limit.
For reproducibility, the release includes check-
point identifiers, input templates, the probabil-
ity parser, inference software versions, generation
hashes, and model-specific hardware. The event-
level manifest links each parsed prediction to its
model, prompt, and forecast date. Because the pri-
mary panel uses question-only models without re-
trieval, these experiments do not establish whether
the same gains hold for retrieval-augmented or
more capable frontier models. The external-
conditioned elicitation control in Appendix E tests
access to the external probability, not retrieval aug-
mentation.
D Quantitative External Prior
For FRED, Wikipedia, DBnomics, and Yahoo Fi-
nance, eligible probabilities come from persistence,
ETS, ARIMA, and local-level state space. ACLED
additionally uses a Poisson or negative-binomial
count model, selecting negative binomial under
overdispersion. If Ji indexes the valid components
and|J i| ≥2, their equal-probability ensemble is
gTS i = 1 |Ji| X m∈Ji gTS im .(17)
When all components are valid, there are four equal
weights except for ACLED, which has five.
For a continuous forecast distribution with CDF
F , Pr(X > c) = 1−F(c) and Pr(X≤c) =
F(c) . For integer counts, Pr(X≥c) = 1−F(c−
1) and Pr(X > c) = 1−F(c) . The threshold
direction and forecast horizon follow the question.
We average event probabilities, not point estimates.
For FRED, the estimation sample is the latest AL-
Method Brier↓
Calibrated classical prior 0.173740
Chronos 0.175811
TimesFM 0.176504
Moirai 0.176123
Hybrid with classical prior 0.169090
Table 4: Structured-event forecasting on 520 questions.
Foundation-model predictions are separate reference
forecasts and are not components of the primary classi-
cal prior.
FRED vintage available at ti, rather than modern
revisions of earlier observations.
If fewer than two components are valid, the fall-
back uses the historical same-horizon frequency
with Jeffreys smoothing:
gTS i = x+ 1/2 n+ 1 ,(18)
where x is the number of event occurrences among
navailable past comparisons. This case occurs on
20 of 520 structured questions. Classical model fit-
ting and predictive-distribution construction must
obey the historical cutoff. Component weights
remain fixed and equal and are not selected us-
ing forecasting-question outcomes. Time-series
foundation-model robustness results appear in Ta-
ble 4 and are not inputs tog TS i .
E Additional Quantitative and
Information-Set Controls
E.1 Time-Series Foundation-Model
Comparisons
The classical structured reference is compared with
three time-series foundation models on the struc-
tured evaluation. These foundation models are ro-
bustness references rather than members of the pri-
mary equal-weight prior. The hybrid using the clas-
sical prior obtains 0.169090 Brier, versus 0.173740
for the calibrated classical prior. Table 4 reports
the additional comparisons.
E.2 Independent and External-Conditioned
Elicitation
We compare the primary question-only LLM fore-
casts with an elicitation variant that shows the
model the external probability. The measured
combination value decreases from 0.001532 to
0.000718, a 53.1% reduction. The standalone Brier
reported for this matched elicitation comparison im-
proves from 0.101694 to 0.097881; it is a separate
summary from the best-single-model result in the
12

Metric Independent Conditioned
Standalone Brier (elicitation comparison)↓0.101694 0.097881
Combination value↑0.001532 0.000718
Corr.(f, g)0.603814 0.841117
Mean|f−g|0.126441 0.071932
Model-side coefficient 0.132814 0.063184
Table 5: Independent question-only elicitation versus
forecasts generated after revealing the external proba-
bility. Both variants are evaluated on the same 4,974
development questions. The conditioned forecast is a
separate elicitation variant. The primary gate uses inde-
pendent question-only forecasts.
Control Brier↓
Raw global affine 0.075101842
Raw regime affine 0.074064247
Clipped regime affine 0.074028511
Shrinkage gate, before calibration 0.073842610
Final calibrated gate 0.073187332
Table 6: Matched ablation controls on the development
population. Each row reports its stated estimator. The
rows are not sequential deployment stages.
main results table. The correlation between model
and external probabilities rises from 0.603814 to
0.841117, while mean absolute disagreement de-
creases from 0.126441 to 0.071932. The net model-
side affine coefficient decreases from 0.132814 to
0.063184. The measurements are consistent with
increased imitation of the external signal after ex-
posure, but do not establish that imitation alone
caused the loss of complementary value.
E.3 Regime Conditioning, Clipping,
Shrinkage, and Calibration
Matched ablations isolate the effects of regime con-
ditioning, clipping, shrinkage, and calibration. Ta-
ble 6 reports distinct controlled comparisons, not
consecutive operations in one prediction pipeline.
The deployed method shrinks fitted weights before
pooling, clipping, and chronological isotonic cali-
bration.
Relative to raw global affine pooling, the
raw regime affine control improves Brier by
0.001037595. Clipping the regime affine score
changes Brier by 0.000035736. The pre-calibration
shrinkage-gate control differs from the clipped
regime affine control by 0.000185901, and chrono-
logical calibration changes the shrinkage-gate score
by 0.000655278. These are matched control con-
trasts, not consecutive deployment stages.
F Baseline Implementations and
Calibration
F.1 Matched Linear Pools
The global and regime-specific affine models use
the same historical forecasts, mean squared-error
objective, zero-centered ridge penalty, and sum-to-
one coefficient constraint. A simplex pool addition-
ally imposes wj ≥0 on every source. Matched
raw and calibrated comparisons use identical eval-
uation questions. Their calibration maps are fitted
chronologically, with each historical pooled predic-
tion generated using only the information available
at its own forecast date.
F.2 External-Only Platt Calibration
The external-only reference is learned without
LLM inputs. For each historical or test probability,
let
uj = logit

clip[10−6,1−10−6](gj)

.(19)
At time ti, global Platt parameters (aG,i, bG,i) min-
imize the mean binary logistic loss over Hi, with
an additional penalty 10−4(a2 +b 2). When regime
k has eligible outcomes, the corresponding param-
eters (ak,i, bk,i) are fitted using Hi,k and the same
objective. We shrink the parameter vectors, not
their output probabilities, using βk,i =n k,i/(nk,i +
50) and ˜θk,i = (1−βk,i)ˆθG,i+βk,i ˆθk,i, where θ=
(a, b)⊤. The final comparator is σ(˜ak,i + ˜bk,iui). A
regime with no eligible examples uses the global
fit. If fewer than 150 globally resolved outcomes
are available, the comparator returns gi. The global
and regime Platt fits use the same chronologically
eligible historical question sets Hi and Hi,k as the
primary analysis, but use only g and y. The Platt
penalty is independent of the gate’s ridge penalty.
External-only isotonic control.On the matched
4,974-question development population, chrono-
logical external-only isotonic calibration ob-
tains 0.075560 Brier, versus 0.075725674 for
the primary external-only Platt comparator and
0.073187332 for the gate. The paired uncertainty
reported for the Platt comparison does not apply to
this additional control.
F.3 Contextual Comparators
We construct contextual features from informa-
tion available at the forecast time. Let Ti be the
forecast horizon in days, ¯fi =M −1 P m fim,
and let sf (i) be the sample standard deviation
13

of the M model probabilities. Define Di =
M −1 P m |fim −g i|, Ei =|g i −0.5| , and ℓ(p) =
logit(clip[10−6,1−10−6](p)). These transformations
provide source probabilities, cross-model disper-
sion, external extremity, and disagreement without
using outcomes or later information.
Regime-aware logistic stacking.We use the 14
continuous features
vi = [ℓ(gi), ℓ(fi1), . . . , ℓ(fi4),
fi1 −g i, . . . , fi4 −g i,
¯fi, sf (i), Di, Ei,log(1 +T i)]⊤.
(20)
The predictor is σ(β0 +β ⊤vi +γ ki,0), with global
feature coefficients and regime-specific intercept
indicators. We standardize the continuous features
using the eligible historical mean and standard de-
viation and leave regime indicators unscaled. We fit
L2 logistic regression using lbfgs, an intercept, no
class weighting, max_iter=5000, and tol=1e-8.
We choose C∈ {0.01,0.1,1,10} on the most re-
cent 20% of chronologically eligible history and
refit on all eligible history with the selected value.
The ordinary logistic stack has no regime-specific
feature slopes, leaving that flexibility to the hierar-
chical comparator.
Hierarchical logistic stacking.We use the same
14 continuous features but allow regime-dependent
intercepts and slopes:
ηi =β 0 +β ⊤vi +γ ki,0 +γ ⊤ kivi.(21)
The global L2 penalty is fixed at 1, while the
regime-deviation penalty is selected chronologi-
cally from {1,10,100} . This is a partial-pooling
comparator that can represent within-regime rela-
tionships absent from the proposed source-level
affine gate.
Contextual gradient boosting.The XGBoost
comparator uses the same forecast-time contextual
features and regime information as logistic stack-
ing. It uses objective=binary:logistic, learn-
ing rate 0.03, maximum depth 3, minimum child
weight 20, row and column subsampling of 0.8,
L2 regularization 1, and at most 500 trees. The
most recent 20% of eligible historical examples
are reserved for chronological early stopping with
patience 30. We then refit on all eligible history
using the selected number of trees.
Local Prediction Pools.We implement the
caliper Local Prediction Pool of Oelrich et al.
(2024), using six forecast-time pooling variables:
zi = [ℓ(gi), Ei,log(1 +T i),
¯fi, sf (i), Di]⊤. (22)
We standardize each pooling coordinate using eli-
gible historical means and standard deviations only.
Neighbors come from the current regime’s his-
torical set Hi,ki, with Euclidean distance dij =
∥˜zi − ˜zj∥2. For caliper width ϱ, the local set is
Ni(ϱ) ={j∈ H i,ki :d ij ≤ϱ} . We choose ϱ∈
{0.50,0.75,1.00,1.50,2.00,3.00} on the most re-
cent 20% of available historical observations, re-
specting chronology, and recompute local weights
using all earlier resolved history at the selected
width.
For source s∈ {0, . . . , M}with probability pjs,
its local mean Bernoulli log score is
ˆais = 1 |Ni| X j∈Ni  yj logp ϵ js + (1−y j) log(1−p ϵ js)  ,
(23)
where pϵ js = clip [10−6,1−10−6](pjs) and the for-
mula applies when |Ni|>0 . Following the
natural-scaling version of the published caliper
pool, weights depend on the localsumof log scores,
rather than an unscaled mean:
ωis = exp(|Ni|ˆais)PM
r=0 exp(|Ni|ˆair)
, h LPP i =
MX
s=0
ωispis.
(24)
If the caliper contains no observations, we set all
source weights to 1/S. The predicted probability is
a convex pool in [0,1] . The 10−6 clip is used only
in the log-score calculation. Local pooling uses
the same historical eligibility and observed regime
partition as the gate, but learns question-dependent
rather than regime-constant source weights.
F.4 Forecast-Information Parity
All contextual methods are trained on chronologi-
cal, resolved history and receive only forecast-time
features. They do not receive future market activity,
future crowd sizes, later time-series observations,
resolved outcomes for current questions, or realized
gate errors. The contextual alternatives achieve
Brier scores of 0.073061 (logistic), 0.073082 (hi-
erarchical logistic), 0.073155 (Local Prediction
Pools), and 0.073021 (XGBoost), compared with
0.073187 for the gate. None has a statistically es-
tablished advantage over the gate in the reported
14

paired comparisons. These results indicate com-
parable predictive accuracy, not superiority of the
gate.
G Sensitivity and Numerical Stability
The primary ridge multiplier is fixed at 10−3
and τ at 50. Sensitivity analyses evaluate τ∈
{10,25,50,100,200}and
cρ ∈ {2.5×10−4,5×10−4,10 −3,2×10−3,4×10−3}.
(25)
The sensitivity analysis is evaluated once at least
300 historical cases are available and does not re-
tune primary predictions. The second moment is
uncentered and calculated separately for each eli-
gible global or regime fit. Mean squared error is
used throughout. A summed-loss ridge solver must
use nρ. The condition-number audit threshold is
105 with family-mean stabilization when required.
The audit records activation of the 105 condition-
number guard separately from the ordinary fitted-
weight distribution.
In the fitted-weight audit, 21.47% of affine coeffi-
cients are negative, and 1.99% of raw affine outputs
fall outside [0,1] . The latter are clipped for proba-
bility evaluation but not in the raw theory diagnos-
tic. The best evaluated shrinkage–ridge grid setting
obtains 0.073083 Brier, compared with 0.073187
for the frozen primary configuration, a difference
of 0.000104. The regime-aware logistic stacker
obtains 0.073061 Brier and is not part of this sen-
sitivity grid. A separate uncertainty-aware variant
reduces the negative-transfer rate from 0.155227 to
0.143884, a 7.31% relative reduction, with nearly
unchanged Brier loss. This variant is not the pri-
mary estimator.
H Population Routing Proof and
Mechanism Controls
For any regime withAk >0 , completing the square
in Eq. 6 gives
Rk(λ) =R k(λ⋆ k) +A k(λ−λ ⋆ k)2.(26)
Minimizing the weighted sum over a shared λ
yields Eq. 8. Substituting the global optimum into
Eq. 26 and subtracting the regime-specific minima
proves Eq. 9.
For S sources with weights on the affine hyper-
plane, choose any matrix U∈R S×(S−1) whose
columns span the zero-sum subspace and any feasi-
ble wref with 1⊤wref = 1. Write w=w ref +Uθ .
Regime Gain 95% low 95% high
Polymarket 0.00038 -0.00010 0.00086
Manifold 0.00371 0.00236 0.00506
ForecastBench crowd 0.00305 0.00175 0.00435
INFER 0.00477 0.00282 0.00672
FRED 0.00790 0.00309 0.01269
ACLED 0.00586 -0.00064 0.01236
Wikipedia 0.00436 -0.00114 0.00986
DBnomics 0.00013 -0.00052 0.00078
Yahoo Finance 0.00032 -0.00023 0.00087
Table 7: Absolute paired Brier gains against the cali-
brated external reference, with reported event-clustered
95% confidence intervals. Several small-source inter-
vals contain zero.
Define the projected source feature a=U ⊤p,
residual eref =p ⊤wref −y , and Hk =E k[aa⊤].
Assuming Hk is positive definite on this subspace,
the regime optimizer isθ⋆ k =−H −1 k Ek[aeref ]. The
multi-source population routing gain is
X
k
πkRk(θ⋆ G)− X
k
πkRk(θ⋆ k)
=
X
k
πk(θ⋆ G −θ ⋆ k)⊤Hk(θ⋆ G −θ ⋆ k). (27)
This statement concerns a population least-squares
problem on the feasible affine subspace. Singular
cases can be treated by restricting to identifiable
directions or using pseudoinverses. The empiri-
cal gate adds ridge, shrinkage, clipping, and cal-
ibration. For the unconstrained affine population
problem, the stated identity is not an out-of-sample
performance guarantee for those additions.
Raw ridge-fitted Brier scores are 0.075101842
for global and 0.074064247 for regime affine pool-
ing, a difference of 0.001037595. The reported
nine-regime raw-routing diagnostic has correla-
tion 0.960596, slope 0.992201, and mean abso-
lute error 0.000294. These statistics describe
theory-aligned pattern agreement and are not an
independent proof of the population identity. A
forecast-round-blocked event-level regime permu-
tation test uses 1,000 permutations. Six null val-
ues equal or exceed the observed statistic, giving
(1 + 6)/1001 = 0.006993.
I Regime-Level Confidence Intervals
Figure 3 and Table 7 report source-level gains with
event-clustered 95% confidence intervals. Inter-
vals exclude zero for Manifold, the ForecastBench-
derived crowd subset, INFER, and FRED. Several
smaller-source intervals include zero.
15

0.000 0.003 0.006 0.009 0.012
Brier gain over calibrated external forecast
FRED
ACLED
INFER
Wikipedia
Manifold
ForecastBench crowd
Polymarket
Yahoo Finance
DBnomics weather
0.0079 [0.0031, 0.0127]
0.0059 [-0.0006, 0.0124]
0.0048 [0.0028, 0.0067]
0.0044 [-0.0011, 0.0099]
0.0037 [0.0024, 0.0051]
0.0031 [0.0018, 0.0043]
0.0004 [-0.0001, 0.0009]
0.0003 [-0.0002, 0.0009]
0.0001 [-0.0005, 0.0008]
Figure 3: Hybrid Brier gain over the calibrated exter-
nal forecast across nine source-defined regimes. Points
show paired mean improvements and horizontal bars
show reported 95% event-clustered confidence inter-
vals. The vertical dashed line indicates no improvement.
The ForecastBench crowd label identifies the dataset
distribution source while retaining its upstream crowd
regime.
J Participation and Model Contribution
For each question, λeff i = PM m=1 ˜wki,i,m = 1−
˜wki,i,g is thenet signedmodel-side coefficient.
It is not the sum of absolute weight magnitudes
and need not lie in [0,1] . The bin estimate is
the arithmetic mean of the chronological coeffi-
cients used for questions in that bin. The later-
held-out scalar diagnostic in Table 8 has weighted
mean gain 0.00104. For each participation quar-
tile b, we split questions chronologically within
each source, using the earliest 80% for fitting
and latest 20% for evaluation, then pool the fit
rows across sources in that quartile. With ¯fi =
1
4
P4
m=1 fim, di = ¯fi −g i, and ei =g i −y i, we
fit ˆλb =− P i∈fit,b diei/ P i∈fit,b d2 i . On the later-
held-out rows, we predict ˆhi =g i + ˆλbdi and report
Gainb = (N test b )−1 P i∈test,b[(gi −y i)2 −( ˆhi −
yi)2]. The scalar fit uses earlier forecast dates and
is separate from the deployed multi-model gate.
Its weighted mean gain of 0.00104 is not directly
comparable to the full gate gain of 0.00229 on mar-
ket and crowd questions. Market and crowd par-
ticipation proxies are converted to within-source
percentile ranks using only snapshot-time infor-
mation. The 4,454-question market and crowd
set yields four pooled equal-rank bins with counts
1,114, 1,114, 1,113, and 1,113.
The Q1 minus Q4 coefficient difference is
0.173193 with approximate 95% interval [0.09820,
0.24819]. Gain intervals from Q1 through Q4
are [0.001201, 0.002771], [0.000612, 0.002048],
[0.000081, 0.001319], and [-0.000294, 0.000586].
A source-fixed-effects regression additionally con-
Quartile n ˆλeff Gain
Q1, lowest 1,114 0.201794 0.001986
Q2 1,114 0.148566 0.001330
Q3 1,113 0.083382 0.000700
Q4, highest 1,113 0.028601 0.000146
Table 8: Mean chronological net model-side coefficients
and gains from a separate later-held-out scalar diagnos-
tic by market or crowd participation rank. Gains are
evaluated on the later 20% of each bin against the raw
external forecast. The n column reports full-bin counts.
These scalar gains are not the deployed multi-model
gate gains. Participation is not a direct measure of exter-
nal accuracy.
trols for horizon and probability extremity. Its
reported negative association has approximately
p= 0.001 . Since participants are not randomized
and accuracy does not define the bins, no causal
claim follows.
K Comparative Confidence and
Selectivity
Historical Comparative Signals Outperform
Raw Confidence.We evaluate whether confidence
and uncertainty signals identify when an individ-
ual LM outperforms the raw external forecast. For
modelm, define
zim =1{(f im −y i)2 <(g i −y i)2}.(28)
A ridge-logistic estimator with regime fixed effects
predicts comparative success from previously re-
solved examples. Its penalty is fixed at 0.01, and
signal orientation is learned from history rather
than manually reversing below-chance raw AUCs.
Raw verbal confidence produces AUCs be-
tween 0.463 and 0.501 across the primary mod-
els. Disagreement and explicit comparative self-
assessment obtain raw AUCs of 0.589 and 0.594.
Historical comparative competence, evaluated over
model–question pairs using the fitted probabilities
cPr(zim = 1|ϕ im, ki,H i), achieves an AUC of
0.681. For question-level selective ranking, we
average these model-specific probabilities:
ci = 1 M MX m=1 cPr(zim = 1|ϕ im, ki,H i),(29)
where ϕim contains the comparative signals avail-
able for model m at forecast time. The resulting
score measures historical comparative success, not
expected hybrid gain. Table 9 reports the model–
question-pair AUC comparisons.
16

Signal Raw AUC Historical AUC
20b verbal confidence 0.488 0.548
120b verbal confidence 0.463 0.572
Llama 8b verbal confidence 0.501 0.533
Llama 70b verbal confidence 0.474 0.560
Entropy or sharpness 0.552 0.562
Model disagreement 0.589 0.608
Comparative self-assessment 0.594 0.611
Historical competence (pairs) – 0.681
Table 9: Raw and past-only historically fitted AUC
for predicting standalone model wins over the raw ex-
ternal forecast, evaluated over model–question pairs.
The historical fit includes regime effects. The averaged
question-level score is used separately for selective rank-
ing.
We separately test whether historical compe-
tence identifies realized hybrid improvement. De-
fine
ri = (gcal i −y i)2 −(h i −y i)2.(30)
At each coverage level, we average the signed rel-
ative loss ℓrel i =−r i over retained questions and
integrate the resulting risk-coverage curve. Lower
relative AURC indicates greater hybrid improve-
ment.
The relative AURCs are −0.002538 (random),
−0.002946 (history-oriented verbal), −0.003718
(comparative self-assessment), −0.005024
(question-level competence), and −0.006358
(oracle). The competence ranking improves on
verbal ranking by 0.002078 AURC (95% CI,
[0.001381, 0.002775]).
Individual-model success against the raw exter-
nal forecast does not guarantee an optimal ranking
of hybrid gains over the calibrated external fore-
cast. In particular, ranking by Pr(zim = 1) is
not generally optimal for ranking E[ri |features] .
Comparative self-assessment is a separate diagnos-
tic and does not feed the gate. Unlike the primary
question-only forecasts, the diagnostic explicitly
provides the model with the external probability
gi. The prompt is “Your forecast is fim, while an
external source forecasts gi. Before the outcome is
known, estimate the probability that your forecast
will have lower squared error than the external fore-
cast.” We therefore do not interpret self-assessment
as independent of the external forecast.
L Statistical Inference and Locked
Holdout
Let di = (g cal i −y i)2 −(h i −y i)2. The pri-
mary mean paired gain is 0.002538342, with re-
ported event-cluster standard error 0.000598700,
z= 4.2398 , two-sided p= 2.24×10 −5, and
95% interval [0.001364890, 0.003711794]. The
fixed-comparator Brier skill is 3.3520%. We re-
sample event IDs 10,000 times with replacement
and carry all constituent question snapshots in each
draw. The bootstrap distribution supplies the event-
cluster standard error. The reported 95% interval is
the Wald interval ˆ∆1 ±1.96 cSEcluster, and the two-
sided p-value uses z= ˆ∆1/ cSEcluster under the
normal approximation. These are not percentile-
bootstrap intervals.
The calibrated routing difference is
0.074279618−0.073187332 = 0.001092286 ,
with reported standard error 0.000389500, 95%
interval [0.000328866, 0.001855706], and
p= 0.00504 . The routing result is secondary
because its 95% interval includes gains below
the prespecified 0.001 Brier smallest interesting
effect. The estimated minimum detectable effect is
0.0010906.
Development ends on December 31, 2025. The
protocol excludes the following eight weeks, and
locked testing begins on February 26, 2026. The
event-disjoint locked test has 1,173 questions in
947 clusters. Its gain is 0.002269 with 95% in-
terval [-0.000401, 0.004939]. Using development
dispersion σd ≈0.0384242 and the reported effect,
the approximate required size is (2.8σd/∆1)2 ≈
1,796.5 clusters. The available holdout has insuffi-
cient clusters for that target. The confidence inter-
val crosses zero, so this result is not independent
confirmation of improvement.
M Reproducibility and Artifacts
The execution environment uses Linux on x86-64,
Python 3.11, vLLM 0.25.1 for LLM inference, Py-
Torch 2.11.0, CUDA 12.9, and bfloat16 inference
on NVIDIA A100-SXM4 GPUs with 80 GB mem-
ory per GPU. The host uses an AMD EPYC 7763
CPU and 2 TB system RAM. Forecast aggregation
and evaluation use scikit-learn 1.7.2 and XGBoost
3.0.5. The stochastic baseline fitting and resam-
pling configuration uses seed 42 where applicable.
Primary LLM predictions use temperature zero.
Statistical uncertainty uses 10,000 event-cluster
bootstrap samples and the shuffled-regime analysis
uses 1,000 blocked event-level permutations.
The reproduction package records population
manifests, point-in-time source snapshots, AL-
FRED vintage metadata, question and prompt
hashes, model checkpoints, parsed probabilities,
17

historical out-of-sample calibration inputs, exact
baseline configurations, and clustered inference
scripts. The structured forecast records iden-
tify component probabilities, the number of avail-
able components, and use of the historical fall-
back. The contextual comparator settings, six-
dimensional local pooling variables, historical scal-
ing, caliper grid, local log-score weighting, and
logistic-stacking feature transformations are speci-
fied in Appendix F.
18
