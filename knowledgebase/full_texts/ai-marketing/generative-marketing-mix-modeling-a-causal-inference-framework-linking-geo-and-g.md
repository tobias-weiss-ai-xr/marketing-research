---
title: 'Generative Marketing Mix Modeling: A Causal Inference Framework Linking GEO and GEM to Business
  Impact'
url: https://arxiv.org/abs/2609.11915
category: ai-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Masahiro Kato
- Daiki Honma
- Taka Kato
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.11915
pages: 54
chars: 140412
fetched_at: '2026-11-08T13:19:45+00:00'
kb_version: 1
---

# Generative Marketing Mix Modeling: A Causal Inference Framework Linking GEO and GEM to Business Impact

Generative Marketing Mix Modeling: A Causal Inference
Framework Linking GEO and GEM to Business Impact
Masahiro Kato∗1 , Daiki Honma 2, and Taka Kato2
1The University of Tokyo and Mizuho-DL Financial Technology Co., Ltd.
2NP-hard
September 11, 2026
Abstract
Generative artificial intelligence changes how firms reach customers, but standard
marketing data do not record how often users see and notice a firm’s name in gener-
ated answers. We develop Generative Marketing Mix Modeling (GMMM) to estimate
the causal effects of Generative Engine Optimization (GEO) and Generative Engine
Marketing (GEM). For GEO, GMMM combines repeated generated answers with
question counts, shares of use across generative systems, and notice probabilities. For
GEM, it combines records of sponsored placements with notice probabilities. GMMM
compares expected business responses under alternative treatment sequences and es-
tablishes sufficient conditions for identifying the resulting effects. We investigate the
empirical performance of the proposed method using simulated answers to product
recommendation in English and Japanese.
Keywords:marketing mix modeling; generative engine optimization; generative engine
marketing; causal inference; measurement error; channel attribution; Bayesian inference
1 Introduction
Marketing mix modeling (MMM) relates an aggregate response, such as sales or conversions,
to media inputs observed across markets and periods. Two features of advertising motivate
the transformations used in MMM. An advertisement can affect the response after the period
in which it is shown, so a carryover function combines current and past inputs. The marginal
change in response can also become smaller when the accumulated input is already high, so a
saturation function maps the carried-over input into a bounded or slowly increasing regressor.
MMM applies these transformations before estimating the coefficients of the media channels
(Nerlove & Arrow, 1962; Clarke, 1976; Hanssens et al., 2001).
∗Email:mkato-csecon@g.ecc.u-tokyo.ac.jp
1
arXiv:2609.11915v1  [stat.ML]  10 Sep 2026

Generative artificial intelligence (AI) changes what must be measured before this model
can be used. Through Generative Engine Optimization (GEO), a firm modifies source material
that may alter answers about the firm, for example by adding a frequently asked questions
section or revising product documentation. Through Generative Engine Marketing (GEM), a
firm pays for sponsored placements in generated answers (Aggarwal et al., 2024; Feizi et al.,
2026; Hu et al., 2026). Conventional impression logs do not record nonsponsored occurrences
of a firm’s name in generated answers, and a platform record of sponsored placements does
not show whether users noticed them.
The frequency with which collected answers contain a firm’s name is not yet a media
input for a market and period. To obtain an expected count for a market and period, that
frequency must be combined with the number of relevant questions, the share handled by
each generative system, and the probability that a user notices the name. Referral sessions
measure a different event because users may read an answer without following a link. For
sponsored placements, spending must likewise be related to the number of placements shown
and the probability of notice. GEO and GEM require this additional measurement step before
they can be analyzed alongside media channels whose impressions are recorded directly.
Estimating a treatment effect adds a second requirement. Carryover makes the response in
period t depend on inputs from earlier periods, so disabling GEO or GEM changes the entire
sequence of media inputs over the affected periods. The relevant comparison must replace
the full sequence under one treatment with the full sequence under another treatment before
the response is evaluated. A regression coefficient by itself does not perform this comparison.
Throughout this study, GEO denotes the specified source modification, and its treatment
effect is the total effect of applying that modification. The response may change through
the generated answers represented by the GEO input and through other consequences of the
modification, such as conventional search traffic or conversion on a landing page.
1.1 Contributions
We develop GMMM to connect measurements of generated answers and sponsored placements
to MMM. For GEO, GMMM models the probability that an answer contains a specified
feature and combines that probability with market query counts and notice probabilities to
obtain the expected number of noticed occurrences under each source state. This count can
be positive without the source modification because GEO changes the occurrence probability
rather than creating the entire input from zero. For GEM, GMMM relates spending to
the number of sponsored placements and then accounts for notice. The resulting inputs
receive the same carryover and Hill transformations as established media before they enter
the response model.
Estimation need not be Bayesian. A likelihood or a penalized criterion can support
plug-in, joint, and other regularized procedures. We use a Bayesian formulation to average
over uncertainty in the occurrence and notice probabilities. The cut posterior leaves the
distribution of the measurement parameters determined by the measurement data, whereas
the joint posterior also allows the response data to update it. Comparing the two procedures
shows how estimation of the media transformations and uncertainty about the constructed
inputs affect the treatment effect of GEO.
The identification analysis gives conditions under which the treatment effect remains
2

identifiable even when the coefficients on the GEO source state and the GEO input cannot
be determined separately after the media transformations are fixed. It also characterizes
when replacing the expected market count by a sequence of occurrence probabilities changes
only the scale and when changes in market composition prevent that reduction.
The empirical collection contains 2,240 complete answers from GPT-5.6 Luna and GPT-4o.
Each model answers the same set of 56 questions, comprising 28 English questions and 28
Japanese questions. Every call uses the same system instruction and requires web search.
The target name is not included in the system instruction or in the questions. Glasp occurs in
33.8% of the GPT-5.6 Luna answers and 27 .8% of the GPT-4o answers, although GPT-4o has
the higher rate for the English questions. These observations estimate occurrence probabilities
under the source state present during collection. One simulation design uses those estimates
for the baseline occurrence probabilities, while the simulation itself generates the treatment
effect. Across the controlled comparisons, estimating carryover and saturation explains most
of the improvement in coefficient recovery over a plug-in method that fixes them, while
updating the measurement parameters with response data has no uniform advantage for
estimating the treatment effect.
1.2 Related Work
Classical MMM combines distributed lags with nonlinear response functions, and recent
methods use regularization or Bayesian pooling across markets (Jin et al., 2017; Ng et al., 2024;
Runge et al., 2025; Gong et al., 2024; Sun et al., 2017). These methods estimate a response
model once its media inputs have been defined. Causal interpretation requires further evidence
because predictive fit alone does not identify an advertising effect. Work on incrementality
and geographic experiments studies the assignment mechanisms and randomized comparisons
that can support such an interpretation (Chan & Perry, 2017; Lewis & Rao, 2015; Gordon
et al., 2019; Vaver & Koehler, 2011; Chen & Au, 2022).
Research on GEO studies how changes in source material affect generated answers and
their ranking, while work on GEM considers sponsored retrieval and placement (Bagga et al.,
2026; Kim et al., 2026; Martinez, 2026; Hajiaghayi et al., 2024; Dubey et al., 2024; D¨ utting
et al., 2024; Xu et al., 2026). Studies of GEO treat citation of a source and use of its content
in an answer as different outcomes (Zhang et al., 2026). Neither quantity alone gives the
number of users who notice the target feature. GMMM addresses the next step by placing
the occurrence probability on a market and time scale suitable for MMM.
The use of records on reach and frequency in MMM provides a precedent for replacing
spending with quantities closer to exposure (Zhang et al., 2023). Randomized estimates
have likewise been incorporated through informative priors or likelihood terms (Zhang et al.,
2024). Meridian and PyMC-Marketing are Bayesian implementations of MMM, and Meridian
supports inputs based on reach and frequency. 1 Our contribution concerns the measurements
required when the media input itself must be inferred from generated answers or sponsored
placements.
Cut and joint posteriors arise in modular Bayesian inference (Plummer, 2015; Jacob et al.,
2017; Carmona & Nicholls, 2020). A cut posterior passes uncertainty from one module to
1Seehttps://developers.google.com/meridianandhttps://www.pymc-marketing.io/.
3

another without allowing the later module to revise the first distribution. Its interpretation
in GMMM depends on the assignment of parameters to modules: fixing the prior for the
media transformations also prevents their estimation from response data, whereas cutting the
update of the measurement parameters still permits those transformations to be estimated.
2 Setup
We useresponsefor the business variable analyzed by MMM andanswerfor text returned
by a generative system. Atreatmentis a specified setting of GEO or GEM. When several
periods are involved, a treatment sequence lists those settings from period 1 through period
Tand includes any earlier values needed to initialize carryover.
2.1 Response and Media Inputs in MMM
For every observational unit i∈ {1, . . . , n}and period t∈ {1, . . . , T}, let Yit denote the
response and let Wit contain baseline variables and controls observed before the period- t
treatment. The unit may be a geographic market or another aggregation used consistently in
the measurement and response models. Let M0 be the set of established media channels.
For every m∈ M0, let Emit ≥ 0 denote the media input in period t and define its sequence
through periodtbyE mi,1:t = (Emi1, . . . , Emit).
A standard MMM transforms each sequence of media inputs before including it in the
response model. We write
Hmit =h m (Am(Emi,1:t;α m);θ m),(1)
where Am combines current and earlier inputs according to carryover parameters αm, and
hm represents saturation with parameters θm. Let b(W ; γ) be the baseline response with
coefficient vector γ. If I0 is a specified set of distinct pairs of media channels, the conditional
mean satisfies
gY

µMMM it  =b(W it;γ) + X
m∈M0
βmHmit +
X
(m,m′)∈I0
βmm′HmitHm′it,(2)
where µMMM it = E[Yit | Hit]. The information set Hit contains the controls and the sequences
of media inputs used to model Yit. We specify Yit | Hit ∼ F(µMMM it , ψ), where ψ contains the
remaining parameters of the response distribution. The identity link gives the usual model
for a continuous response with additive noise of mean zero, while other links accommodate
counts or rates.
2.2 Channels Through Generative AI
GMMM enlarges the media set to M = M0 ∪ {G, P}, where G indexes the input constructed
from generated answers and P indexes the input constructed from sponsored placements.
For each period, the first input is the expected number of generated answers in which the
specified property occurs and is noticed under the current source state. The second is the
4

expected number of sponsored placements that users notice. The first count need not be
zero when the source modification is absent; GEO changes its value by changing generated
answers. Inputs for established media are observed directly, while the two additional inputs
are constructed from generated answers, platform records, market counts, and observations
of user attention.
Let Zit ∈ {0, 1} denote the GEO source state, where Zit = 1 means that the specified
source modification is present and Zit = 0 means that it is absent. The response specification
studied here is
gY (µit) =b(W it;γ) +
X
m∈M0
βmHmit +β DZit +β GH G it +β P H P it +β GP H G it H P it .(3)
The term βDZit permits the source modification to affect the response through variables
that are not represented by the constructed GEO input, such as conventional search traffic
or conversion on a landing page. The coefficient βGP permits the effect associated with
one generative channel to depend on the other. Either term may be omitted when the
corresponding mechanism is excluded from the model.
2.3 Data Sources
Let DM contain the observations used to construct the GEO and GEM inputs. For GEO, these
observations include repeated generated answers, counts of relevant questions, shares of use
across generative systems, and observed notice indicators. For GEM, they include spending,
the number of sponsored placements shown, predictors of that number, and observed notice
indicators. Let DY contain Yit together with the controls and media inputs in the response
model. When a randomized experiment estimates the same treatment effect for a comparable
population and evaluation period, its estimate and standard error formD E.
The collection described in Section 5.1 contains 20 answers from each of two GPT models
for each of 56 questions, comprising 28 English questions and 28 Japanese questions. The
public referral series analyzed in Appendix F comes from an earlier period and lacks the
corresponding question counts, generated answers, and notice observations. These missing
observations prevent the two sources from being combined in one GMMM analysis.
The simulations use units of the form i = (g, j), where g∈ {1, . . . ,5} indexes geographic
markets and j∈ {1, . . . ,6} indexes product clusters. Each cluster contains pages and
questions that respond to the same GEO treatment. A substantive application must use
an observational unit that is common to the construction of the media inputs, the response
model, and the treatment effect.
2.4 Treatment Effect
Because carryover links the period- t response to media inputs observed before t, we define
the treatment effect from complete treatment sequences over a specified evaluation window.
Let aG ∈ {0, 1} select one of two GEO sequences: aG = 1 selects the specified sequence
with GEO, and aG = 0 selects the sequence with the source modification removed. Let
aP ∈ {0, 1} similarly select the specified GEM spending sequence or the sequence with GEM
removed. The pair ( aG, aP ) selects one complete GEO sequence and one complete GEM
5

sequence across all periods. The comparison uses the same history before period 1 unless
an intervention begins earlier; in that case, the treatment and input values before period 1
follow the selected sequence. The simulations set all media inputs before period 1 to zero.
For an evaluation setT E ⊆ {1, . . . , T}, define
V(a G, aP ) =
nX
i=1
X
t∈TE
E[Y it(aG, aP )],(4)
where Yit(aG, aP ) is the potential response under the selected treatment sequences and the
specified evolution of all other variables. The primary estimand is
∆G =V(1,1)−V(0,1).(5)
We refer to ∆ G as the treatment effect of GEO. It is the total effect of the specified source
modification, including the change transmitted through H G and any additional change
represented by βDZit. The contrast retains the specified GEM sequence. The evaluation
window may extend beyond the periods in which GEO is active so that the effect includes
responses associated with carried-over inputs. The analogous treatment effect of GEM is
∆P = V (1, 1) −V (1, 0), which compares the specified GEM sequence with the sequence in
which GEM is disabled while retaining the GEO sequence.
3 Generative Marketing Mix Modeling
The data record the source state, spending, and established media inputs, but they omit the
expected counts associated with GEO and GEM. GMMM constructs these two counts before
applying the standard media transformations and estimating the response model.
3.1 The GEO Input
Let q∈ {1, . . . , Q}index clusters of questions and let p∈ P index generative systems. A
system is defined by the model version and the settings used to obtain an answer. The set
Q(i) contains the question clusters associated with unit i. For every i, q, and t, let Niqt ≥ 0
be the number of times that a question in cluster q is submitted in unit i during period t.
For every i, p, and t, let ωipt ∈ [0, 1] be the share of those questions handled by system p,
with P p∈P ωipt = 1.
Before collecting answers, the analyst specifies the property to be recorded. For repetition
r∈ {1, . . . , Rqpt} and source state z∈ {0, 1}, let Xqptr(z) = 1 when the stored answer has
that property and let it equal zero otherwise. In the empirical collection, the property is the
occurrence of a spelling of the target name in a fixed dictionary. Let πqpt(z) = P[(]X qptr(z) =
1) be its occurrence probability. Conditional on Xqptr(z) = 1, let λqpt ∈ [0, 1] be the probability
that the user notices the recorded property. The input associated with GEO is
EG it (z) = X
q∈Q(i)
Niqt
X
p∈P
ωiptπqpt(z)λqpt.(6)
6

The quantity EG it (z) is the expected number of generated answers in unit i and period t for
which the specified property occurs and is noticed under source state z. It may be positive
when z = 0; the change in this input caused by the source modification is EG it (1) −E G it (0). A
user who encounters the property more than once contributes more than once to this count.
The comparison between z = 1 and z = 0 holds Niqt and ωipt fixed. We assume that the
source modification does not change notice conditional on occurrence, which is why λqpt has
no argumentz.
Equation (6) pools occurrence and notice probabilities across markets after conditioning
on the question cluster, generative system, period, and source state. It also uses a system
share that is common across question clusters within a market and period. When the data
distinguish these cells, the same construction can use πiqpt(z), λiqpt, and ωiqpt without changing
the media transformations or the treatment contrasts.
We estimate the occurrence probabilities with the hierarchical model
Xqptr |π qpt ∼Bernoulli(π qpt),(7)
logit(πqpt) =A T qptα+u q,u=B Qσu eu, eu∼ N(0, IQ−1).(8)
The columns of BQ ∈R Q×(Q−1) form an orthonormal basis for vectors whose coordinates sum
to zero, so PQ q=1 uq = 0. The predictor vector Aqpt may contain indicators for the generative
system, the source state, and other observed determinants of occurrence. Its coefficient vector
is α. The effect for question cluster q is represented in noncentered form by standard normal
coordinates eu and scale σu > 0. Replacing the observed sequence of source states by another
treatment sequence yields probabilities under that sequence only when the data contain the
required variation in source state. Answers collected under one source state identify only the
occurrence probabilities for that state; the change caused by the source modification requires
observations under both states.
Suppose that a user study presents generated answers and records Cqpt cases in which
participants notice the property amongn qpt answers in which it occurs. We use
Cqpt |λ qpt ∼Binomial(n qpt, λqpt),(9)
logit(λqpt) = (Dλ qpt)Tξ+v q,v=B Qσv ev, ev∼ N(0, IQ−1).(10)
Here, Dλ qpt is a vector of observed predictors with coefficient vector ξ. The effect for question
cluster q, denoted by vq, uses the same zero-sum basis and its own scale σv > 0. Together,
the two models estimate the probabilities needed in (6).
3.2 The GEM Input
A sponsored placement contributes to the GEM input only if the platform shows it and the
user notices it. Let SP it ≥ 0 denote the spending level selected by the firm for the GEM
intervention in unit i and period t, before the platform determines delivery. Let LP it denote
the number of sponsored placements shown. Conditional on a placement being shown, let
ρP it ∈ [0, 1] be the probability that the user notices it. For positive spending, we model the
number shown by
LP it |S P it >0∼Poisson(µ P it),(11)
7

logµ P it =ϕ 0 +ϕ S logS P it +ϕ DDit +ϕ RRit, ϕ S >0,(12)
where Dit is a demand predictor observed before the period-t treatment and Rit is a promotion
indicator. We setµ P it = 0 whenS P it = 0. The input associated with GEM is
EP it =µ P itρP it.(13)
The restriction ϕS > 0 makes the expected number of sponsored placements increase with
positive spending. A user study in which participants report whether they noticed each
sponsored placement can estimate ρP it with a binomial model. The analysis below uses one
notice probability for all sponsored placements, while (13) permits variation across units
and periods when the data support it. When LP it is observed and the analysis conditions
on realized delivery, LP itρP it can be used directly. The Poisson model is needed for missing
delivery counts and for spending sequences that were not observed.
3.3 Carryover and Saturation
The two expected counts are transformed in the same way as inputs for established media.
We use normalized geometric carryover,
Amit =
PLm
ℓ=0 αℓ mEmi,t−ℓ/sm PLm
ℓ=0 αℓ m
,0≤α m <1,(14)
where Lm ∈ {0, 1, . . .}is the maximum lag and sm > 0 is a fixed scale used in the analysis.
Values before period 1 come from the earlier history assigned to the treatment sequence; the
simulations set these values to zero. The transformed input is
Hmit = Aκm mit
Aκm mit +θ κm m , θ m >0, κ m >0.(15)
The Hill function equals 1/2 when Amit = θm, and κm determines how sharply it changes near
that point. Carryover is applied before the Hill transformation (Jin et al., 2017). Substituting
H G it andH P it into (3) completes the response specification.
3.4 Estimation from Measurement and Response Data
Let ηM collect the parameters used in (6) and (13), let ηT collect the carryover and Hill
parameters, and let ϑ collect the response parameters. We write JM (ηM ; DM ) for a loss
based on the data used to construct the two inputs and JY (ϑ, ηM , ηT ; DY ) for a loss based
on the response data. If DE contains a randomized estimate of the same treatment effect, its
contribution is JE(ϑ, ηM , ηT ; DE); otherwise, we set JE = 0. A general estimator minimizes
J(η M , ηT , ϑ) =JM +J Y +J E +P M (ηM ) +P T (ηT ) +P Y (ϑ),(16)
where the penalty terms may be zero. With negative log likelihoods and no penalties, this
criterion gives maximum likelihood estimation. Nonzero penalties permit regularization.
The criterion covers several ways of using the data. A plug-in method estimates ηM from
DM , substitutes that estimate into the response model, and either fixes ηT or estimates it
from DY . A joint likelihood estimates ηM , ηT , and ϑ together. Resampling can be used with
either procedure to assess uncertainty. A Bayesian version makes both the treatment of
uncertainty and the direction of updating explicit.
8

3.5 Bayesian Computation
Minimizing the criterion with negative log likelihoods gives point estimates. In the Bayesian
analysis, the cut posterior leaves the distribution of the measurement parameters determined
by DM , whereas the joint posterior allows DY to update it. Both procedures average over
uncertainty in the constructed inputs. The hierarchical occurrence and notice models are
fitted in noncentered coordinates. Their posterior modes and analytic Hessians define a
Laplace approximation qL(ηM | DM ) to the posterior based only on DM . Sampling the
transformation parameters from their prior gives
q(η| DM ) =q L(ηM | DM )p(ηT ), η= (η M , ηT ).(17)
Let β = ( βD, βG, βP , βGP )T. After replacing the exact posterior for ηM by the Laplace
approximation, the joint posterior is
ep(η, β, σ2 Y | DM ,D Y )∝p(D Y |η, β, σ2 Y )p(β, σ2 Y )q(η| DM ).(18)
For each k∈ {1, . . . , K}, we sample ηk ∼q (η| DM ) and construct the corresponding
sequences of media inputs. Conditional on ηk, the response parameters are integrated under
the normal inverse-gamma model with the sign restrictions in Appendix G.2. Let mk be
the numerical approximation to p(DY |η k) obtained with a Gaussian approximation to the
posterior probability of the sign restrictions. The joint calculation assigns weight
wk = mk PK
h=1 mh
.(19)
After selecting ηk according to these weights, we sample the response parameters from their
conditional posterior and evaluate ∆ G.
The two-stage procedure uses equal weights for the samples from (17), leaving both the
Laplace approximation for ηM and the prior for ηT unchanged by DY . A cut posterior keeps
only the first of these distributions fixed:
pcut(ηM , ηT , β, σ2 Y | DM ,D Y ) =q L(ηM | DM )p(ηT , β, σ2 Y | DY , ηM ).(20)
Because the conditional posterior on the right is normalized separately for every ηM , in-
tegrating over ( ηT , β, σ2 Y ) leaves qL(ηM | DM ) unchanged (Plummer, 2015; Jacob et al.,
2017).
For computation, we use M samples of the measurement parameters and a common set
of J samples from the transformation prior. Let mmj approximate p(DY |η M,m, ηT,j ). On
this common set, the cut and joint weights are
wcut mj = 1 M mmj PJ h=1 mmh , w joint mj = mmj PM r=1 PJ h=1 mrh .(21)
The plug-in method that estimates the transformations uses the same J samples at the point
estimate of ηM , while the two-stage procedure assigns weight 1 /(M J) to every pair. For the
independent samples in (19), we report
ESS =
 KX
k=1
w2 k
!−1
(22)
9

as a numerical diagnostic. A small effective sample size means that a few samples carry most
of the weight. For the common set of samples, Appendix C.3 reports the effective sample
size within each measurement sample and the effective sample size of the joint weights across
measurement samples.
Figure 1 summarizes the order of the calculations.
Actions and
Measurement Data
GEO and GEM
Exposure Histories
Carryover and
Saturation
Outcome
Response
Effect Relative to
Disabling a Channel
GMMM constructs generative exposure before applying the response and attribution stages of MMM.
Figure 1: GMMM constructs the expected counts associated with GEO and GEM before
applying carryover, the Hill transformation, and the response model. The plug-in, cut,
and joint procedures differ in whether they average over uncertainty in the measurement
parameters and whether the response data update those parameters.
3.6 Randomized Estimate of the GEO Treatment Effect
A randomized experiment can inform GMMM when it estimates the same treatment effect for
a population, response definition, and evaluation window that can be related to the GMMM
target. Suppose that the experiment reports bτE with standard error sE, and let τE(ϑ, η) be
the corresponding effect implied by the GMMM parameters. We use
bτE |ϑ, η∼ N

τE(ϑ, η), s2 E +σ 2 tr  ,(23)
where σtr ≥ 0 is fixed before estimation and represents residual differences between the
experimental population and the target population after the measured design variables have
been aligned. This likelihood contributes JE to (16). In the Bayesian analysis, it changes the
weights and the conditional posterior for the response coefficients. For every parameter sample,
the experimental effect is computed from the complete treatment and control sequences
before the media transformations are applied.
The aligned simulation uses the average treatment effect of GEO, including the term
associated with the source state. A second simulation adds a nonzero difference between the
experimental and target populations to the same effect and thereby examines misspecification
of the transport model. If an additive attribution across interacting channels is also required,
Appendix D gives a Shapley allocation as an additional summary.
10

4 Identification of the Treatment Effect of GEO
Recovering the treatment effect of GEO requires both statistical variation in the response
model and observations that support the expected response under each treatment sequence.
Statistical variation determines whether the response coefficients or the linear combination
that defines the effect can be identified, while the observed market inputs and treatment
assignments determine whether the comparison can be evaluated.
4.1 Identification Within the Response Model
If the two constructed inputs were observed directly, GMMM would differ from a standard
MMM only through the additional term for the GEO source state. The following reduction
states this relation before the rank condition for the response coefficients.
Proposition 4.1(Reduction to standard MMM).Suppose that EG i,1:T and EP i,1:T are observed
for every i∈ {1, . . . , n}. If βD = 0, then (3) is an instance of (2) with channel set
M0 ∪ {G, P}and interaction set {(G, P)}. If βGP = 0also holds, the response is additive on
this enlarged channel set. Setting all four coefficients associated with GEO and GEM to zero
gives the additive model for established media withI 0 =∅.
Proof. The observed sequences determine H G and H P through (1). Substitution into (3),
together with the stated restrictions on the coefficients, gives the corresponding cases of
(2).
GMMM adds the construction of EG and EP and the definition of their values under each
treatment sequence. Once these quantities are fixed, identification of the response coefficients
is a rank problem.
Proposition 4.2(Identification of response coefficients and linear effects).Fix the sequences
of media inputs and all parameters of the media transformations. Suppose that the response
model has an identity link and b(W ; γ) = W γ. Let H0 be the matrix whose columns are
the transformed inputs for established media and let W∗ = ( W, H0). Let Xη contain the
variable for source state, H G, H P , and H GH P . If MW∗ is the orthogonal projection onto the
complement of the column space ofW ∗, define
Dη =M W∗Xη, G η =X T η MW∗Xη.(24)
Conditional on the fixed sequences and transformations, the four response coefficients are
identified from the conditional mean if and only if Gη is nonsingular. Under a Gaussian con-
ditional response with nonsingular variance, the same condition is equivalent to identification
by the likelihood. For a fixed vector d∈R 4, the linear effect dTβ is identified if and only if
dTv= 0for everyv∈R 4 such thatD ηv= 0.
Proof. Two coefficient vectors β and β′ give the same conditional mean after the nuisance
coefficients are adjusted if and only if Xη(β−β ′) belongs to the column space of W∗.
Equivalently, Dη(β−β ′) = 0. The four coefficients are identified exactly when Dη has full
column rank, which is equivalent to nonsingularity of Gη. The linear effect is constant over
11

observationally equivalent coefficient vectors exactly when it vanishes on the null space of
Dη. The necessity statement remains valid under the sign restrictions used in the simulations
because their parameter space has nonempty interior.
The simulations omit established media, so H0 has no columns and residualization with
respect to W is sufficient. In the general model, H0 must be included. For example, if a
transformed input for an established channel equalsH G, its coefficient cannot be separated
from βG even when the four columns of Xη are linearly independent after removing W alone.
A linear effect may remain identified when its component coefficients are not. This
distinction is especially relevant when the variable for source state and H G are nearly
proportional after the other regressors have been removed. Proposition 4.2 states the exact
null-space condition; finite-sample stability still depends on the degree of collinearity.
The proposition treats the transformations as fixed. Joint identification of ( βG, αG, θG, κG)
additionally requires the observed input sequences to provide independent information about
response amplitude, carryover, and the Hill curve. With all other parameters fixed, full
column rank of the Jacobian of the residualized mean with respect to these four parameters is
sufficient for local identification at an interior point of a continuously differentiable model. If
other parameters are unknown, full column rank of the Jacobian with respect to the complete
free parameter vector after removal of the fixed linear controls is sufficient. A step treatment
whose untransformed GEO input has one level before treatment and another after treatment
cannot separate response amplitude from the Hill parameters using steady-state observations
alone. Identification then depends on transition dynamics and on variation within source
states, including variation in question counts, system shares, or occurrence probabilities.
A prior can stabilize estimation without identifying a likelihood that lacks this variation.
Related ambiguities arise when nonlinear response and coefficients that change over time
produce similar observed sequences but different allocation decisions (Dew et al., 2024).
4.2 Occurrence Probabilities and Market Counts
The market input in (6) weights an occurrence probability by the number and composition
of questions, the shares of use across systems, and the probability of notice. In a special case,
this difference amounts only to a change of scale. Let A(π) denote linear carryover applied to
a sequence of exact occurrence probabilities, with the same initialization as (14).
Proposition 4.3(Constant rescaling of the GEO input).Suppose that EG it (z) = c0πit(z)for
the same constant c0 > 0in every market, period, and evaluated source state, including values
used to initialize carryover. For the Hill functionh(a;θ, κ) =a κ/(aκ +θ κ), it holds that
h(A(EG);θ, κ) =h(c0A(π);θ, κ) =h(A(π);θ/c 0, κ).(25)
Rescaling θ preserves the transformed sequence and the treatment effect computed from it. A
single common value of θ does not generally absorb scale factors that vary across markets or
periods.
Proof. Linearity gives A(c0π) = c0A(π). Dividing the numerator and denominator of
h(c0a; θ, κ) by cκ 0 proves (25). For the final statement, consider two markets with the same
12

positive occurrence-probability sequence and different constants c1 and c2. The transformed
market counts differ because h is strictly increasing, whereas a common transformation of
the identical probability sequences is the same. One common value of θ cannot represent
both.
The same equivalence holds within each market if its scale factor ci is constant over
time and the model permits a market-specific parameter θi, rescaled to θi/ci. A Bayesian
analysis must transform the prior and its support consistently. Under the common-scale
condition in Proposition 4.3, a common multiplicative level in question volume or notice
probability is absorbed by the Hill midpoint. Question volume, system shares, and notice
probabilities affect the treatment effect when their relative values vary across markets, periods,
systems, question clusters, or source states. When that variation changes the proportionality
between occurrence probabilities and expected counts, one occurrence-probability sequence
cannot represent every market input. A finite collection of answers adds a separate source
of uncertainty about the probabilities. Appendix C examines both issues in a static linear
model and under a nonlinear transformation.
4.3 Identification across Treatment Sequences
The rank condition concerns the response model after the inputs have been fixed. Identification
of ∆G also requires the observed data to determine the expected response under each complete
treatment sequence. For every i∈ {1, . . . , n}and t∈ {1, . . . , T}, let H− it contain the variables
observed immediately before the period- t GEO and GEM treatments. It includes earlier
responses, prior media inputs, earlier treatments, and any aggregate variables used to represent
interference. Let Hit add the period- t treatments and the values of EG it and EP it implied by
them. For a pair ( aG, aP ) of complete treatment sequences, let F aG,aP it be the distribution of
Hit obtained by recursively replacing the observed treatment assignment with those sequences.
Finally, define mit(h) = E[Yit | Hit = h]. The following assumptions place the standard
longitudinal g-formula on these GMMM treatment sequences.
Assumption 4.1(Consistency).If the observed GEO and GEM treatments through period t
equal the values specified by( aG, aP ), then the observed variables through period t equal their
potential values under those treatment sequences.
Assumption 4.2(Sequential exchangeability).Conditional on H− it , the period-t GEO and
GEM treatments are independent of future potential information sets and potential responses
under the treatment sequences evaluated in(4).
Assumption 4.3(Positivity).For every value of H− it in the target support, each discrete
treatment specified by the evaluated sequences has positive conditional probability. A positive
continuous GEM spending level lies in the interior of its conditional support and has positive
density in a neighborhood of that level. A sequence that sets spending to zero requires positive
conditional mass at zero when the absence of a campaign is represented by a separate point
mass.
Assumption 4.4(Observed-data laws in the target population).The measurement and
response data identify mit and the conditional laws used to construct F aG,aP it on the support
13

of the evaluated treatment sequences. When the response model uses the expected counts in
(6) and (13), the measurement parameters and market inputs identify those counts for the
target population. Identification of mit on the same support must also be established. If Hit
instead contains unobserved realized impressions, their joint law with the observed variables
andY it must also be identified; a marginal distribution of impressions is insufficient.
Assumption 4.5(Interference through specified aggregates).Spillovers within an observa-
tional unit are included in that unit’s treatments and response. Treatments assigned to other
units may affect its potential response or generative inputs only through aggregate variables
included in H− it . The distribution F aG,aP it specifies how those aggregates evolve under the
evaluated treatment sequences.
Under these conditions, the longitudinal g-formula applies to the complete GEO and
GEM treatment sequences.
Theorem 4.4(Longitudinal g-formula for GMMM).Under the preceding assumptions, the
expected response in(4)is identified by
V(a G, aP ) =
nX
i=1
X
t∈TE
Z
mit(h)dF aG,aP it (h).(26)
The difference between this expression for( aG, aP ) = (1, 1)and( aG, aP ) = (0, 1)identifies
∆G.
Proof. Consistency links observed variables to their potential values under the realized
treatments. Sequential exchangeability permits the observed assignment mechanism to be
replaced, conditional on H− it , by the evaluated treatment sequences. Positivity ensures that
the required conditional laws are defined on their support. The measurement assumption
identifies the conditional laws and mit, including their dependence on the two constructed
inputs. The interference assumption makes the potential response for each unit well defined
at the chosen aggregation. Iterated expectation yields the longitudinal g-formula in (26)
(Robins, 1987).
Assumption 4.4 states the general observed-data requirement. The next corollary gives
concrete sufficient conditions for the parametric GMMM used in the simulations.
Corollary 4.5(Parametric identification with fixed market inputs).Consider (4) conditional
on measured market inputs, with every response input other than GEO fixed across the two
GEO treatment sequences. Suppose that consistency, sequential exchangeability, positivity,
and the interference assumption hold. Assume that ηM is identified on the required support
and that the occurrence probabilities apply to the target population. Suppose that the media
transformations are fixed or identified and that the response model with an identity link is
correctly specified. If W∗ has full column rank and Dη in Proposition 4.2 has rank four, then
∆G is identified. More generally, for a known vector dη, the condition dT η v = 0whenever
Dηv = 0is sufficient to identify dT η β even when the four coefficients are not separately
identified.
14

Proof. The identified measurement parameters and fixed market inputs determine EG and
EP under the two treatment sequences. Fixed or identified transformations then determine
the corresponding regressors and their differences. Proposition 4.2 identifies either the four
coefficients or the specified linear effect. The causal assumptions permit these identified
quantities to be evaluated under both treatment sequences. Because the response model
is written in terms of expected counts, these identified quantities suffice without modeling
unobserved realized impressions.
The corollary relies on occurrence probabilities that apply to the target population and
on a correctly specified conditional response mean. Under a nonlinear transformation, a
model for an expected count differs from a model for an unobserved realized count: for a
random input M , E[h(M ) | DM ] generally differs from h(E[M| DM ]). Either specification
also requires control of confounding between the media input and the response.
The general formula permits treatments to change variables observed later. The simulations
condition on generated question counts, shares of system use, notice probabilities, and all
response inputs other than GEO. For every parameter sample, the calculation replaces the
complete GEO sequence before evaluating the response. The rollout dates are fixed by
design, so the simulation obtains counterfactual values by evaluating the specified parametric
response model under both sequences rather than by using nonparametric overlap for every
cluster history.
A randomized rollout can supply treatment variation by design. An observational rollout
instead requires pre-treatment controls and support for both treatment sequences. A variable
such as referral traffic or brand search may transmit part of the effect of a current treatment
to revenue or conversion. Fixing that variable does not recover the total effect and is not
sufficient by itself to identify a controlled direct effect (Acharya et al., 2016). If the variable
is affected by an earlier treatment and also influences a later treatment, it may belong to H− it ;
the longitudinal g-formula then averages over its distribution under the treatment sequence
(Robins, 1987).
4.4 Decomposition under the Linear Response Model
Under the linear response used in the simulations, ∆ G can be written as a component
associated with the source state and a component due to the change in the transformed GEO
input.
Proposition 4.6(Decomposition under the linear response model).Suppose that gY is the
identity link and that every input to the response model other than the GEO source state and
the GEO input is the same under the two treatment sequences. Assume that the terms below
are integrable. Let Z denote the sequence of GEO source states selected by aG = 1, and let0
denote the sequence selected bya G = 0. Under(3), it holds that
∆G =β D
nX
i=1
X
t∈TE
E[Zit] +β G
nX
i=1
X
t∈TE
E

H G it (Z)−H G it (0) 
+β GP
nX
i=1
X
t∈TE
E

H P it  H G it (Z)−H G it (0)  .(27)
15

Proof. Subtract the two conditional means. Every term that contains neither the GEO source
state nor the GEO input cancels. The remaining terms are the term associated with the
source state, the change in H G, and the interaction between that change and H P . Taking
expectations and summing overT E gives (27).
The component due to the GEO input contains ( βG + βGP H P it )(H G it (Z) −H G it (0)), so the
interaction makes this component depend on the GEM input. Any other regressor changed
by the GEO treatment would add another term.
Equation (27) is an algebraic decomposition of the total GEO effect under the specified
response model. We use it to study estimation error in the term for the source state and in
the terms that contain the constructed GEO input. A causal mediation interpretation would
require interventions that can vary the source state and the generated exposure separately,
together with exchangeability and support for both interventions (Imai et al., 2010; Pearl,
1995). Our estimand remains the causal effect of the complete source modification.
5 Answer Collection and Simulation Evidence
The answer collection and the simulations serve different roles. The collection estimates
occurrence probabilities under one observed source state. The simulations introduce changes
in source state and generate the corresponding market responses, which permits evaluation of
estimators of ∆G. Appendices A and B give the collection procedure and additional numerical
results.
5.1 Target Name in Generated Answers
We submit a fixed list of 56 questions that ask for product recommendations in seven use
cases to GPT-5.6 Luna and GPT-4o. The list contains 28 English questions and 28 Japanese
questions. Each API call uses the same system instruction and requires web search. Its user
message contains only the requested language and question, and Glasp appears in neither
message. After storing the complete answer, we record one if it contains a spelling of Glasp in
a fixed dictionary and zero otherwise; the indicator records occurrence regardless of sentiment.
Each model answers every question 20 times, giving 2,240 answers. The requests are
randomized within four blocks collected during one window, and Table 1 summarizes the
resulting occurrence rates. Because the source state is unchanged throughout collection,
these observations estimate probabilities for that state. Identification of the GEO treatment
effect also uses variation in source state, market counts of the questions, shares of use across
systems, notice probabilities, and contemporaneous response data.
Glasp occurs in 33 .8% of the GPT-5.6 Luna answers and 27 .8% of the GPT-4o answers.
Averaging the posterior distributions for the individual questions gives a difference of 5 .70
percentage points with a 95% interval of [3 .12, 8.27]. The ordering reverses for English
questions, where GPT-4o has the higher rate. Conditional on occurrence, GPT-4o also names
Glasp first among the candidate brands more often. These results show why the recorded
property and the weights assigned to the questions must match the business application.
Appendix A reports results by language and use case.
16

Table 1: Occurrence of Glasp in the Collected Answers
Model English Japanese Panel Rate Posterior Mean (95% Interval) Mean Rank Rank 1 (%)
GPT-4o 35.4 20.2 27.8 28.8 [27.0,30.7] 1.62 60.5
GPT-5.6 Luna 28.6 38.9 33.8 34.5 [32.8,36.3] 1.94 39.4
English, Japanese, and Panel Rate are percentages of answers that contain Glasp. Panel Rate averages
the 56 observed rates with equal weights. Posterior means and intervals average the distributions for
the 56 questions in (32). Mean Rank is the rank at the first occurrence of Glasp among 11 candidate
brands, conditional on its occurrence.
5.2 Simulation Design
The simulations compare estimators on the same panels and with the same construction of
EG and EP . Five geographic markets each contain six product clusters and are observed for
36 periods. Two clusters begin the GEO treatment in period 19 and two begin in period 23,
while two never receive it. Every product cluster contains two question clusters observed
on two generative systems. The resulting data contain 1,080 observations across units and
periods but only six units of treatment assignment within each market. The response follows
(3) with
(βD, βG, βP , βGP ) = (0.55,4.00,2.20,0.50).(28)
In the controlled design, baseline occurrence probabilities follow the hierarchical logit model.
A second design uses probabilities estimated from the collected answers and preserves the
pairing of the two models for each question, as specified in (33). The treatment effect of
GEO is generated in both designs, and the evaluation window is TE = {1, . . . ,36}. The
simulations isolate uncertainty in the occurrence and notice models together with estimation
of the media transformations: question counts and system shares are known, the demand
variable is included among the controls, and every cell has 50 notice observations. A cell
consists of one question cluster, one generative system, and one period. Established media
channels are omitted. Appendix H gives the complete data-generating process.
The principal comparisons use 120 paired replications in every condition. We evaluate
the four response coefficients and ∆ G using root mean squared error (RMSE) and coverage
of 95% intervals. Appendix B.1 defines the metrics and numerical settings. Paired intervals
for differences between methods resample the 120 common replication indices 5,000 times.
Differences between relative RMSE values are reported in percentage points. Appendix B
gives additional results for one, five, and 20 answers per cell and for randomized estimates
included in estimation.
5.3 Estimation of Carryover and Saturation
Before comparing how uncertainty passes between the two models, we examine whether
carryover and saturation are estimated or fixed. On the same 120 controlled panels with five
answers per cell, one plug-in method fixes the carryover and Hill parameters at their prior
means, while a second estimates them from the response data using the same candidates as
17

Table 2: Effect of Estimating the Transformation Parameters With Five Answers per Cell
Estimator Transformations Effect RMSE (%) Vector RMSE Coverage
Plug-in Prior mean 17.642 1.207 0.975
Plug-in Estimated from response data 17.525 0.945 0.975
Two-stage Prior distribution 17.705 1.032 0.958
Joint Estimated from response data 17.541 0.950 0.975
Plug-in Known 17.135 0.882 0.950
Two-stage Known 17.066 0.876 0.950
Joint Known 17.191 0.884 0.958
the joint posterior. Three diagnostic benchmarks use the true transformation parameters.
Table 2 reports the results.
Estimating the transformation parameters reduces the RMSE of the coefficient vector
from 1.207 to 0.945 for the plug-in method. The corresponding value for the joint posterior is
0.950. The 95% paired interval for the joint value minus the plug-in value is [ −0.006, 0.016],
and the interval for the difference in effect RMSE also contains zero. Estimation of carryover
and saturation explains the principal improvement in coefficient recovery over the plug-in
method with fixed transformations. The designs based on the collected answers and the
designs with misspecification give the same qualitative result (Appendix B.4).
5.4 Use of Response Data in the Measurement Model
The cut posterior in (20) estimates the transformation parameters from the response data
while keeping the distribution of ηM fixed by DM . Comparing it with the joint posterior
isolates the effect of allowing DY to revise ηM . We use M = 128 samples of the measurement
parameters, a common set of J = 700 samples from the transformation prior, and 1,000
conditional samples of the response coefficients for each method. Appendix C.3 describes the
computation.
Let JA be the number of generated answers per cell. The controlled design combines
JA ∈ {1, 5} with standard deviations σY ∈ {0.4, 1.2} for the response errors. A fifth condition
uses occurrence probabilities estimated from the collected answers, with JA = 5 and σY = 1.2.
The 120 replications in each condition give 600 panels. Methods use the same observations
within a condition, and the controlled conditions use the same market inputs and standardized
response innovations. Each row uses 120 paired replications. Effect RMSE is the relative
RMSE of ∆ G. Coverage refers to its 95% interval. The parenthetical labels indicate whether
the transformation parameters are estimated from the response data or retained at their
prior distribution. With 120 independent replications, coverage near 95% has a binomial
Monte Carlo standard error of about 2 percentage points.
A smaller standard deviation for the response errors substantially reduces effect RMSE,
but the joint posterior has no uniform advantage over the cut posterior or the plug-in method
that estimates the transformations. WhenJ A = 1 andσ Y = 0.4, the joint posterior reduces
coefficient RMSE relative to the cut posterior by 0 .0300; the 95% paired interval for this
reduction is [0 .0221, 0.0383]. The corresponding interval for the difference in effect RMSE
18

Table 3: Comparison on a Common Set of Transformation Draws
Method Vector RMSE Effect RMSE (%) Coverage
Controlled:J A = 1,σ Y = 0.4
Plug-in (estimated) 0.667 6.000 0.958
Cut (estimated) 0.687 6.010 0.950
Joint 0.657 6.046 0.950
Two-stage (prior) 0.918 7.075 0.975
Oracle 0.493 5.723 0.950
Controlled:J A = 1,σ Y = 1.2
Plug-in (estimated) 0.975 17.450 0.967
Cut (estimated) 0.943 17.519 0.975
Joint 0.974 17.545 0.975
Two-stage (prior) 1.020 17.882 0.967
Oracle 0.886 17.236 0.950
Controlled:J A = 5,σ Y = 0.4
Plug-in (estimated) 0.639 5.912 0.967
Cut (estimated) 0.642 5.930 0.967
Joint 0.636 5.923 0.975
Two-stage (prior) 0.897 7.070 0.958
Oracle 0.493 5.723 0.950
Controlled:J A = 5,σ Y = 1.2
Plug-in (estimated) 0.956 17.513 0.975
Cut (estimated) 0.953 17.442 0.975
Joint 0.963 17.479 0.975
Two-stage (prior) 1.027 17.858 0.975
Oracle 0.886 17.236 0.950
Estimated occurrence probabilities:J A = 5,σ Y = 1.2
Plug-in (estimated) 0.931 17.359 0.942
Cut (estimated) 0.912 17.326 0.942
Joint 0.939 17.480 0.950
Two-stage (prior) 0.974 18.099 0.950
Oracle 0.821 16.984 0.958
19

contains zero. In the condition based on estimated occurrence probabilities, effect RMSE is
17.326% for the cut posterior and 17 .480% for the joint posterior. Their difference is 0 .154
percentage points with an interval of [0 .046, 0.259]. The interval comparing the cut posterior
with the plug-in method contains zero. Table 13 reports all 15 paired comparisons.
To assess numerical sensitivity, we doubled both numbers of candidates for eight replica-
tions in each condition. The cut and joint estimates of ∆ G changed by at most 1 .602% of the
true effect, although the effective sample size for the transformation candidates can approach
one when the standard deviation of the response errors is small. Appendix C.3 reports the
full diagnostics and states which approximation errors remain when the candidate counts
increase.
5.5 Accuracy of the Components of the Treatment Effect
The main simulation sets βD = 0.55 because a source modification can affect the response
outside generated answers. The total effect therefore combines the term for the source state,
the change in the transformed GEO input, and its interaction with GEM. Errors in the two
components can partially cancel when the sum is estimated. Let nZ = Pn i=1 P t∈TE Zit be the
number of treated observations across units and periods. Define the component for the source
state by CD = nZβD and the component that contains the GEO input by CE = ∆G −C D.
Every method estimates them as bCD = nZ bβD and bCE = b∆G − bCD, using its own estimate of
βD. The second component includes the interaction in Proposition 4.6 and is used here as a
decomposition of the specified response model.
The treatment sequences give nZ = 320 and CD = 176 in every replication. With five
answers per cell and σY = 1.2, the mean total effect is 266 .944 in the controlled design and
234.755 in the design based on estimated occurrence probabilities. The corresponding mean
values of CD/∆G are 66.34% and 75.38%. The term associated with the source state accounts
for most of the simulated total effect even though its coefficient is unknown to the estimators.
The first three numerical columns report relative RMSE for each component. For a component
Table 4: Accuracy of the Treatment Effect and Its Model Components
Method Total (%) Source State (%) GEO Input (%) Error Correlation
Controlled:J A = 5,σ Y = 1.2
Plug-in (estimated) 17.513 32.638 48.351 -0.627
Cut (estimated) 17.442 32.526 47.756 -0.626
Joint 17.479 32.646 48.366 -0.631
Two-stage (prior) 17.858 36.426 47.860 -0.677
Oracle 17.236 29.351 34.825 -0.523
Estimated occurrence probabilities:J A = 5,σ Y = 1.2
Plug-in (estimated) 17.359 27.551 47.129 -0.555
Cut (estimated) 17.326 27.483 45.929 -0.556
Joint 17.480 27.872 47.295 -0.561
Two-stage (prior) 18.099 29.810 48.439 -0.614
Oracle 16.984 24.470 31.468 -0.409
20

C and R = 120 replications, the reported value is 100( R−1 PR r=1(( bCr −C r)/Cr)2)1/2. The
columns have different denominators. The final column is the correlation between estimation
errors in the component associated with the source state and the component from the GEO
input. Section 5.4 reports all five conditions.
In the condition based on estimated occurrence probabilities, the plug-in method has
relative RMSE 17.359% for the total effect and 47 .129% for the component from the GEO
input. The latter value is 45 .929% for the cut posterior, 47 .295% for the joint posterior, and
31.468% for the oracle. The negative correlations in Table 4 explain why the total can be
more accurate than either component. If eD and eE denote their errors, the squared error
of the total contains 2 eDeE in addition to the two squared component errors. Errors with
opposite signs can cancel through this term. We retain ∆ G as the primary estimand and
report the decomposition alongside the total effect.
6 Discussion
GMMM separates construction of the two media inputs from the causal comparison. Generated
answers determine occurrence probabilities; question counts, system shares, and notice
probabilities put those probabilities on the scale of an MMM; complete treatment sequences
then define the effects of GEO and GEM. Plug-in, cut, and joint procedures differ only in
how they estimate the transformations and use uncertainty in the constructed inputs.
6.1 Interpretation of the Results
The GEO input describes expected noticed occurrence under a source state, and it may be
positive both with and without the source modification. GEO changes this input through
the occurrence probabilities. The estimand ∆ G compares the complete source-modification
sequences, so it includes the path through the constructed input and the additional path
represented by βDZit. For GEM, the corresponding comparison changes the spending sequence
that determines sponsored placements.
The collected answers also show that one overall occurrence rate is inadequate. The
ordering of GPT-5.6 Luna and GPT-4o changes with language, and rates vary substantially
across use cases. A feature used in an application should be chosen for the business question,
and the probabilities for individual questions should receive the weights of the target popula-
tion. Equal weights estimate the rate for the fixed panel used here. They also estimate a
population rate when that population has the same distribution of questions.
Identification of βD and βG requires variation in the transformed GEO input beyond
a proportional change in the variable for source state after the other regressors have been
removed. When the two regressors move together, the condition on the null space in
Proposition 4.2 determines whether ∆ G remains identified. The component results show why
this distinction matters in finite samples: errors in the component associated with the source
state and the component from the GEO input often have opposite signs and partially cancel
in the total effect.
The design that assigns the treatment supplies its causal interpretation. A randomized
rollout provides treatment variation by design. An observational rollout requires pre-treatment
21

controls, support for both treatment sequences, and a contemporaneous comparison group
when treated and untreated units experience common changes in the generative systems.
Variables affected by an earlier treatment may also influence later assignment, in which case
the g-formula in (26) averages over their distribution under each treatment sequence.
For estimation, the plug-in method that estimates carryover and saturation is a useful
reference when the measurement distribution is concentrated. The cut posterior averages
over measurement uncertainty while keeping the distribution of the measurement parameters
fixed by the data used to construct the inputs. The joint posterior also uses the response
likelihood to revise those parameters. We find no universal ranking: the joint posterior
improves coefficient RMSE in one condition with a small standard deviation for the response
errors, but it does not improve effect RMSE there and performs worse than the cut posterior
in the condition based on estimated occurrence probabilities.
Numerical approximation raises a different question. Concentrated importance weights
require checks of the number and placement of candidates, while a Markov chain would
require checks of mixing and convergence. Increasing the number of candidates leaves the
errors from the Laplace approximation for the measurement parameters and the Gaussian
approximation to the posterior probability of the sign restrictions unchanged.
The simulations hold the GEO and GEM inputs fixed across estimators and omit estab-
lished media channels, which isolates estimation of a common GMMM response model. A
separate comparison of input construction would keep the response model and transformation
estimation fixed while comparing a source indicator, occurrence probabilities, and expected
counts under changes in question volume, system shares, and attention. A randomized
estimate included in the likelihood informs the same treatment effect; an independently
evaluated treatment would address predictive transfer to a different intervention.
6.2 Alternative Response Models
The construction of EG and EP precedes the choice of response distribution, which allows
an application to use a link and distribution suited to sales, conversions, counts, or rates.
Hierarchical coefficients can share information across related units, and coefficients that vary
over time can represent changes in the relation between a media input and the response.
Other carryover or saturation functions can replace (14) and (15) without changing the
definitions of the two expected counts or ∆ G.
6.3 Alternative Estimation Procedures
The distinction between measurement and response parameters also applies outside the
Bayesian formulation. A procedure based on likelihood can estimate all parameters together
and use resampling for uncertainty, while a regularized procedure can penalize selected terms
in (16). In the Bayesian analysis used here, the cut and joint posteriors differ in whether DY
updatesη M .
22

6.4 Uncertainty in Market Inputs
The simulations treat the question counts Niqt and shares ωipt as known. In an application,
the counts may be estimated from a sample and the shares may change during the evaluation
window. A probability model for either quantity can be added to ηM , after which its
uncertainty passes through (6), the media transformations, and the calculation of ∆ G. This
extension changes the construction of the input but not the response model or the definition
of the treatment effect.
7 Conclusion
GMMM extends MMM to settings in which the media inputs associated with generative AI
are not recorded directly. Under each source state, the GEO input is the expected number of
generated answers in which a specified property occurs and is noticed; GEO changes this
count but need not create it from zero. The GEM input is the expected number of sponsored
placements that users notice. Both inputs are defined for each market and period before
carryover and the Hill transformation are applied. The treatment effect of GEO is the total
effect of the specified source modification under two complete treatment sequences.
The identification results allow the treatment effect to be determined in some designs
even when its component coefficients cannot be recovered separately. They also identify the
conditions under which a sequence of occurrence probabilities differs from a market count
only by scale. In the simulations, estimating carryover and saturation explains most of the
improvement in coefficient recovery over a plug-in method that fixes them. Allowing response
data to revise the measurement parameters has no consistent benefit for estimating ∆ G, and
the total effect can conceal larger errors in its two model components.
The collected answers identify occurrence probabilities under the source state present
during collection. Identification of the change caused by GEO uses observations under both
source states together with contemporaneous market counts, notice observations, and business
responses. GMMM combines these measurements and evaluates the causal effect from the
complete sequence of media inputs.
References
Adivit Acharya, Matthew Blackwell, and Maya Sen. Explaining causal findings without bias:
Detecting and assessing direct effects.American Political Science Review, 110(3):512–529,
2016. 15
Pranjal Aggarwal, Vishvak Murahari, Tanmay Rajpurohit, Ashwin Kalyan, Karthik
Narasimhan, and Ameet Deshpande. Geo: Generative engine optimization. InACM
SIGKDD Conference on Knowledge Discovery and Data Mining (KDD), 2024. 2
Puneet S. Bagga, Vivek F. Farias, Tamar Korkotashvili, Tianyi Peng, and Yuhang Wu. E-geo:
A testbed for generative engine optimization in e-commerce, 2026. arXiv: 2511.20867. 3
23

Christian Carmona and Geoff Nicholls. Semi-modular inference: enhanced learning in multi-
modular models by tempering the influence of components. InInternational Conference
on Artificial Intelligence and Statistics (AISTATS), 2020. 3
David Chan and Mike Perry. Challenges and opportunities in media mix modeling. Technical
report, Google Research, 2017. 3
Aiyou Chen and Timothy C. Au. Robust causal inference for incremental return on ad spend
with randomized paired geo experiments.The Annals of Applied Statistics, 16(1):1 – 20,
2022. 3
Darral G. Clarke. Econometric measurement of the duration of advertising effect on sales.
Journal of Marketing Research, 13(4):345–357, 1976. 1
Ryan Dew, Nicolas Padilla, and Anya Shchetkina. Your mmm is broken: Identification of
nonlinear and time-varying effects in marketing mix models, 2024. arXiv: 2408.07678. 12
Avinava Dubey, Zhe Feng, Rahul Kidambi, Aranyak Mehta, and Di Wang. Auctions with
llm summaries. InACM SIGKDD Conference on Knowledge Discovery and Data Mining
(KDD), pp. 713–722. Association for Computing Machinery, 2024. 3
Paul D¨ utting, Vahab Mirrokni, Renato Paes Leme, Haifeng Xu, and Song Zuo. Mechanism
design for large language models. InWeb Conference, 2024. 3
Soheil Feizi, Mohammadtaghi Hajiaghayi, Keivan Rezaei, and Suho Shin. Online adver-
tisements with llms: Opportunities and challenges.SIGecom Exchange, 22(2), 2026.
2
Chang Gong, Di Yao, Lei Zhang, Sheng Chen, Wenbin Li, Yueyang Su, and Jingping Bi.
Causalmmm: Learning causal structure for marketing mix modeling. InInternational
Conference on Web Search and Data Mining (WSDM), 2024. 3
Brett R. Gordon, Florian Zettelmeyer, Neha Bhargava, and Dan Chapsky. A comparison of
approaches to advertising measurement: Evidence from big field experiments at facebook.
Marketing Science, 38(2):193–225, 2019. 3
Mohammad Taghi Hajiaghayi, S´ ebastien Lahaie, Keivan Rezaei, and Suho Shin. Ad auctions
for llms via retrieval augmented generation. InInternational Conference on Neural
Information Processing Systems (NeurIPS), 2024. 3
D.M. Hanssens, L.J. Parsons, and R.L. Schultz.Market Response Models: Econometric and
Time Series Analysis. International Series in Quantitative Marketing. Springer US, 2001. 1
Silan Hu, Shiqi Zhang, Yimin Shi, and Xiaokui Xiao. Gem-bench: A benchmark for ad-injected
response generation within generative engine marketing. InConference on Knowledge
Discovery and Data Mining (KDD). Association for Computing Machinery, 2026. 2
Kosuke Imai, Luke Keele, and Dustin Tingley. A general approach to causal mediation
analysis.Psychological Methods, 15(4):309–334, Dec 2010. 16
24

Pierre E. Jacob, Lawrence M. Murray, Chris C. Holmes, and Christian P. Robert. Better
together? statistical learning in models made of modules, 2017. arXiv: 1708.08719. 3, 9
Yuxue Jin, Yueqing Wang, Yunting Sun, David Chan, and Jim Koehler. Bayesian methods
for media mix modeling with carryover and shape effects. Technical report, Google Inc.,
2017. 3, 8
Sunghwan Kim, Wooseok Jeong, Serin Kim, Sangam Lee, and Dongha Lee. Sageo arena: A
realistic environment for evaluating search-augmented generative engine optimization. In
Conference on Knowledge Discovery and Data Mining (KDD), 2026. 3
Randall A. Lewis and Justin M. Rao. The unfavorable economics of measuring the returns
to advertising.The Quarterly Journal of Economics, 130(4):1941–1973, 2015. 3
Olivier Martinez. Optimizing visibility in generative engines: A critical survey of generative
engine optimization (2023-2026), 2026. arXiv: 2607.14035. 3
Marc Nerlove and Kenneth J. Arrow. Optimal advertising policy under dynamic conditions.
Economica, 29(114):129–142, 1962. 1
Edwin Ng, Zhishi Wang, and Athena Dai. Bayesian time varying coefficient model with
applications to marketing mix modeling, 2024. arXiv: 2106.03322. 3
Judea Pearl. Causal diagrams for empirical research.Biometrika, 82(4):669–688, 1995. 16
Martyn Plummer. Cuts in bayesian graphical models.Statistics and Computing, 25(1):37–43,
2015. 3, 9
James Robins. A graphical approach to the identification and estimation of causal parameters
in mortality studies with sustained exposure periods.Journal of Chronic Diseases, 40:
139S–161S, 1987. 14, 15
Julian Runge, Igor Skokan, Gufeng Zhou, and Koen Pauwels. Packaging up media mix
modeling: An introduction to robyn’s open-source approach, 2025. arXiv: 2403.14674. 3
Lloyd S. Shapley.A value for n-person games, pp. 31–40. Cambridge University Press, 1988.
43
Yunting Sun, Yueqing Wang, Yuxue Jin, David Chan, and Jim Koehler. Geo-level bayesian
hierarchical media mix modeling. Technical report, Google Research, 2017. 3
Jon Vaver and Jim Koehler. Measuring ad effectiveness using geo experiments. Technical
report, Google Research, 2011. 3
Keisuke Watanabe and Kazuki Nakayashiki. Disentangling answer engine optimization from
platform growth: A log-based natural experiment on chatgpt referral traffic, 2026. arXiv:
2606.04362. 45, 46
Shengwei Xu, Zhaohua Chen, Xiaotie Deng, Zhiyi Huang, and Grant Schoenebeck. Ad
insertion in llm-generated responses, 2026. arXiv: 2601.19435. 3
25

Kai Zhang, Xinyue He, and Jingang Yao. From citation selection to citation absorption:
A measurement framework for generative engine optimization across ai search platforms,
2026. arXiv: 2604.25707. 3
Yingxiang Zhang, Mike Wurm, Alexander Wakim, Eddie Li, and Ying Liu. Bayesian
hierarchical media mix model incorporating reach and frequency data. Technical report,
Google Research, 2023. 3
Yingxiang Zhang, Mike Wurm, Eddie Li, Alexander Wakim, Joseph Kelly, Brenda Price, and
Ying Liu. Media mix model calibration with bayesian priors. Technical report, Google
Research, 2024. 3
26

A Collection of Generated Answers and Simulation
Inputs
Section 5.1 reports whether Glasp occurs in a fixed collection of generated answers. We
specified the questions, model identifiers, language instructions, and search settings before
collecting those answers.
Recorded indicator.An answer receives value one when it contains a spelling of Glasp in
the target dictionary and zero otherwise. The dictionary is applied after the complete API
record has been stored, so the target name is absent from the question and the instructions
sent to the model. The indicator records occurrence regardless of whether the surrounding
text endorses Glasp. The source state was constant during collection, so the answers identify
occurrence probabilities only for that state.
Connection to the GEO input.The collected answers estimate occurrence probabilities
under the information environment present during collection. Equation (6) combines these
probabilities with the number of relevant questions, the share handled by each generative
system, and the probability of notice. Repeated calls characterize variation for each question
and model, whereas the choice of questions determines the population described by their
weighted average. Applying the estimated probabilities to a market requires weights for that
market and generation settings that correspond to those used in the collection.
A.1 Collection Design and Target Quantities
The 56 questions ask for product recommendations in seven use cases, including web high-
lighting and summarization with AI. Each use case contains four questions in English and
four in Japanese. The questions exclude the target name and its listed aliases. Each model
receives the product question, the requested language, and a common system instruction
that requires an independent recommendation and a web search before answering. The API
call supplies a tool for web search and selects it through tool choice. Appendix J gives the
complete instruction and API settings.
For each question, we obtained 20 answers from GPT-5.6 Luna and 20 from GPT-4o. Four
randomized blocks contained five repetitions for each combination of question and model,
giving
56×2×4×5 = 2,240 (29)
API records. Collection ran from 05:58 UTC on September 3, 2026, to 04:40 UTC on
September 4, 2026. The four blocks randomize request order within this single collection
interval and do not represent distinct observation dates.
Let Rtext qpbr denote the complete answer for question q∈ {1, . . . ,56}, model p∈ {1, 2}, block
b∈ {1, . . . ,4}, and repetitionr∈ {1, . . . ,5}. We define
Iqpbr =1

a listed spelling of Glasp occurs inR text qpbr  .(30)
27

For the observed collection period and source state, Iqpbr realizes the Bernoulli variable in
(7). The complete answer and the position of the first occurrence among the 11 candidate
brands remain available for analyses of placement.
Let t∗ denote the collection period and z∗ the prevailing source state. The occurrence
probability for question q and model p is pqp = πqpt∗(z∗). Conditional on pqp, the 20 calls are
modeled as Bernoulli variables with a common probability during the collection interval. Let
J = 20 and Sqp = P4 b=1 P5 r=1 Iqpbr. The estimator for one question and model is bpqp = Sqp/J.
Given weightsω q ≥0 such that P56 q=1 ωq = 1, define the index for modelpby
Pp =
56X
q=1
ωqpqp.(31)
The primary analysis sets ωq = 1 /56. The resulting index describes the fixed panel of
questions; it equals a market occurrence rate only when the weights reproduce the market
distribution of questions.
For each question and model, uncertainty from 20 answers is represented by
pqp |S qp ∼Beta

Sqp + 1 2 , J−S qp + 1 2  .(32)
Independent samples from these distributions are averaged with the weights ωq to obtain
intervals for Pp and differences between models. These intervals condition on the Bernoulli
model and the fixed question weights. They exclude uncertainty from replacing the panel by
a different population of questions.
All 2,240 requests returned complete answers, and no request or response identifier was
duplicated. Each answer contains at least one completed call to the web search tool, giving
3,140 calls in total. GPT-5.6 Luna returned the requested model identifier, whereas GPT-4o
returned the dated identifiergpt-4o-2024-08-06.
A.2 Occurrence Results
Table 1 reports the occurrence rates. Glasp occurs in 378 of 1,120 GPT-5.6 Luna answers and
311 of 1,120 GPT-4o answers, which gives raw panel rates of 33 .8% and 27.8%. Averaging
the beta distributions for the 56 questions gives posterior means of 34 .5% and 28 .8%. The
posterior mean of the difference between the models is 5 .70 percentage points, with a 95%
posterior interval of [3 .12, 8.27] percentage points and posterior probability above 0 .999 of
being positive.
The aggregate rates conceal a reversal by language. GPT-4o exceeds GPT-5.6 Luna by
6.79 percentage points for the English questions, whereas GPT-5.6 Luna exceeds GPT-4o
by 18.75 percentage points for the Japanese questions. The corresponding 95% posterior
intervals are [2.90, 10.02] and [14 .11, 21.57] percentage points. Conditional on occurrence,
Glasp is the first brand from the candidate list in 60 .5% of the GPT-4o answers and 39 .4% of
the GPT-5.6 Luna answers. GPT-5.6 Luna has the higher overall rate but the lower frequency
of first placement.
Figure 2 shows variation across use cases. Both models have their highest occurrence rates
for questions about web highlighting and their lowest rates for questions about knowledge
28

management. The reversal by language is especially pronounced for summarization with AI
and YouTube learning. A model with system-specific effects for the questions can represent
this variation, whereas a model with one common occurrence probability cannot. The ordering
Web
highlighting
Research
capture
YouTube
learning
Knowledge
management
Social
annotation
Read-it-
later
AI
summarization
0.0
0.2
0.4
0.6
0.8
1.0T arget-Name Inclusion Rate
GPT-4o, English
GPT-4o, Japanese
GPT-5.6 Luna, English
GPT-5.6 Luna, Japanese
Figure 2: Occurrence rates by use case and answer language. Bars show posterior means, and
error bars show 95% intervals obtained by averaging the distributions for the four questions
in each cell.
of the two models is the same in every collection block. GPT-4o rates range from 24 .3%
to 30.0%, and GPT-5.6 Luna rates range from 31 .4% to 36 .8%. Because the blocks cover
different parts of one collection interval, comparisons across them assess stability during
collection and do not estimate a time trend.
A.3 Occurrence Probabilities Used in the Simulations
The variation across questions supplies baseline probabilities for a second simulation design.
Within each language, queries are sampled with replacement, and the same sampled query is
used for both models. The treatment effect of GEO is generated by the simulation and does
not equal the observed difference between the models.
Let Cjp be the occurrence count for question j and model p among J = 20 answers. In
each replication, six English and six Japanese question indices are sampled with replacement
within language. The selected index s(q) is common to the two models. Conditional on that
selection, the baseline probabilities are sampled independently across models from
π0 qp |s(q),D M ∼Beta  Cs(q),p + 1 2 , J−C s(q),p + 1 2  .(33)
The common question selection retains the observed pairing and language composition.
Variation within each beta distribution represents uncertainty from the finite number of
answers. The sampled probabilities determine the baseline log odds, after which the simulation
29

adds the same time component and treatment shift in log odds as the controlled design.
The simulation specifies the response coefficients and treatment shift independently of the
collected answers.
The fitted occurrence model includes a system-specific centered question effect, permitting
the difference in log odds between systems to vary across questions. The remaining models
used to construct the inputs and the equation for the business response are unchanged.
B Additional Simulation Results
The simulations keep the panel structure fixed while varying the number of generated answers,
the treatment of the transformation parameters, and the relation between the constructed
inputs and the business response. Because the treatment assignments are common across
methods, the comparisons can isolate the source of each difference before examining numerical
accuracy and alternative data-generating processes.
B.1 Panel Design and Evaluation Criteria
The controlled simulation observes five geographic markets for 36 periods, with TE =
{1, . . . ,36}. Each market contains six product clusters, every product cluster is linked to two
question clusters, and every question cluster is observed on two generative systems. Two
product clusters begin the GEO treatment in period 19 and two begin it in period 23; the
remaining two never receive GEO. Occurrence of the target name follows the hierarchical
logit model. The number of relevant questions varies with latent demand and seasonality,
while system shares vary across markets. GEM spending depends on demand observed before
treatment and on promotion, and a model for sponsored placements determines the number
shown.
The design using estimated occurrence probabilities retains the same panel and treatment
structure. Its baseline probabilities follow (33), and the fitted measurement model includes
interactions between question and system. The demand variable that affects the response is
included among the controls in both simulations. The panel has 1,080 observations, while
treatment is assigned at the level of six product clusters and shared across markets.
The response coefficients are given in (28).
For each collection size of one, five, or 20 answers per cell, we run 120 paired replications.
The market panel and the simulated randomized estimate are held fixed across collection
sizes. Each fit uses 700 candidates from the proposal distribution and 1,000 samples from the
conditional posterior for the response parameters defined in Section 3. The plug-in benchmark
fixes the sequences of media inputs. The two-stage procedure gives equal weight to samples
of the measurement parameters, whereas Joint GMMM reweights the same samples with the
response data. The randomized estimate from the target population is the average treatment
effect of GEO under the specified rollout relative to the complete sequence with GEO disabled.
A second version adds 0 .75 to represent a difference between the experimental and target
populations. The oracle observes the true sequences of media inputs and transformations.
We assess the response coefficients and ∆ G by root mean squared error (RMSE) and
coverage of 95% intervals. ForR replications, the RMSE of the coefficient vector is (PR r=1 ∥ bβr−
30

β0∥2 2/(4R))1/2. Relative effect RMSE is ( R−1 PR r=1(( b∆G,r − ∆G,r)/∆G,r)2)1/2, reported as a
percentage. Paired bootstrap intervals use 5,000 resamples of the common replication indices
and recompute both RMSEs. Differences between relative effect RMSEs are measured in
percentage points. Effective sample size (ESS) describes concentration of the importance
weights. Results with five answers per cell represent the central collection size, while the
comparison that adds a randomized estimate uses 20 answers per cell to reduce uncertainty
from the answer collection.
B.2 Simulation Based on the Collected Answers
Using the paired question probabilities in (33), this design assigns GPT-5.6 Luna to the first
system and GPT-4o to the second. Both models share the six selected query indices per
language in each replication, while the fitted model with interactions between question and
system allows their baseline log-odds differences to vary across queries.
With five simulated answers per cell, the RMSE of the coefficient vector is 0 .942 for Joint
GMMM, 1.120 for Plug-in GMMM, and 0 .981 for Two-stage GMMM (Table 5). The paired
difference for Joint minus Plug-in is −0.178, with a 95% bootstrap interval of [−0.261,− 0.096].
For Joint minus Two-stage, the difference is −0.038 and the interval is [ −0.096, 0.021]. The
comparison with Plug-in GMMM supports lower coefficient error when the transformation
parameters are estimated. For ∆ G, the RMSEs are 17.576%, 18.316%, and 18.258%, and both
paired intervals for Joint GMMM include zero. Section 5.3 separates the role of estimating
the transformation parameters from the role of averaging over measurement uncertainty.
Table 5: Simulation Based on Occurrence Probabilities Estimated From Collected Answers
Method Vector RMSE Effect Bias (%) Effect RMSE (%) Coverage Median ESS
Plug-in GMMM 1.120 -0.966 18.316 0.950 –
Two-stage GMMM 0.981 -0.246 18.258 0.950 –
Joint GMMM 0.942 0.380 17.576 0.958 91.2
Joint + aligned estimate 0.938 0.458 17.057 0.967 91.3
Joint + shifted estimate 0.942 3.813 17.804 0.950 91.4
Oracle 0.823 0.369 17.049 0.958 –
Effect Bias and Effect RMSE report the relative bias and relative RMSE of the treatment effect of
GEO as percentages. Coverage is the empirical coverage of its 95% interval. ESS is the effective sample
size of the importance weights for the joint computations. “Aligned estimate” uses the randomized
estimate from the target population, and “shifted estimate” adds 0 .75 to that estimate. Dashes mark
methods whose weights are fixed by construction. Each row is based on 120 paired replications. A cell
is defined by a question, a generative system, and a period.
Adding the randomized estimate from the target population lowers the RMSE of ∆ G from
17.576% to 17.057%. The paired difference is −0.519 percentage points with a 95% bootstrap
interval of [−0.862,− 0.182]. The RMSE of the coefficient vector changes only from 0 .942
to 0.938, and the paired interval for that change includes zero. When 0 .75 is added to the
randomized estimate, signed bias in ∆ G rises from 0 .380% to 3 .813%. Its RMSE is 17 .804%,
and the interval for its paired difference from Joint GMMM is [ −0.387, 0.826] percentage
points.
31

Figure 3 traces coefficient error as the number of answers increases. More answers reduce
uncertainty in the occurrence probabilities, while variation in the response and uncertainty in
the transformation parameters remain. The fitted model allows the difference between systems
to vary across questions. The controlled comparison below holds the baseline probability
model fixed and isolates the effect of averaging over measurement uncertainty.
1 5 20
Responses per Query, System, and Period
0.8
0.9
1.0
1.1
1.2RMSE Across the Four Response Coefficients
Plug-in GMMM
T wo-stage GMMM
Joint GMMM
Joint with aligned experiment
Oracle exposure
Figure 3: Root mean squared error of the coefficient vector in the simulation using estimated
occurrence probabilities. The baseline distributions of occurrence indicators are estimated
from the collected generated answers. Lines connect ordered numbers of answers, and error
bars are 95% bootstrap intervals over replications.
B.3 Controlled Simulation Results
With five answers per cell, the RMSE of the coefficient vector is 0 .950 for Joint GMMM,
1.207 for Plug-in GMMM, and 1 .032 for Two-stage GMMM (Table 6). Joint GMMM also
reduces the RMSE for the coefficient on the GEO input from 2 .068 to 1 .558 and for the
coefficient on the GEM input from 0 .754 to 0 .618 relative to Plug-in GMMM. The oracle has
vector RMSE 0.880, so variation in the response remains important even when the sequences
of media inputs and transformations are known.
Because every method uses the same simulated panel, the paired comparisons attribute
differences to the estimators. Joint GMMM reduces the RMSE of the coefficient vector by
0.256 relative to Plug-in GMMM and by 0 .082 relative to Two-stage GMMM. Both 95%
bootstrap intervals exclude zero. The relative RMSE of the treatment effect of GEO is similar
across the three methods because errors in the individual coefficients can offset in the scalar
estimand.
Figures 4 and 5 show the same pattern across numbers of answers: joint estimation has
lower coefficient error than the plug-in estimator with fixed transformations, while their errors
in the treatment effect of GEO remain close. This comparison changes both the treatment
32

Table 6: Root Mean Squared Error With Five Answers per Cell
Method Source State GEO Sponsored Interaction Vector Effect RMSE (%)
Plug-in GMMM 0.216 2.068 0.754 0.965 1.207 17.642
Two-stage GMMM 0.201 1.704 0.722 0.893 1.032 17.705
Joint GMMM 0.183 1.558 0.618 0.876 0.950 17.541
Joint + aligned estimate 0.182 1.549 0.614 0.869 0.944 17.441
Joint + shifted estimate 0.186 1.559 0.622 0.884 0.953 17.932
Oracle 0.161 1.429 0.494 0.885 0.880 17.158
“Aligned estimate” uses the randomized estimate from the target population, and “shifted estimate”
adds 0.75 to that estimate.
Table 7: Paired Root Mean Squared Error Differences With Five Answers per Cell
Comparison Metric Difference Lower Upper
Joint minus Plug-in GMMM Vector RMSE -0.2564 -0.3322 -0.1745
Joint minus Plug-in GMMM Effect RMSE (pp) -0.1010 -0.7087 0.4884
Joint minus Two-stage GMMM Vector RMSE -0.0821 -0.1403 -0.0215
Joint minus Two-stage GMMM Effect RMSE (pp) -0.1645 -0.7435 0.3804
of measurement uncertainty and the estimation of the transformation parameters. For that
reason, the comparison in Section 5.3 varies these features one at a time.
1 5 20
Responses per Query, System, and Period
0.8
0.9
1.0
1.1
1.2
1.3RMSE Across the Four Response Coefficients
Plug-in GMMM
T wo-stage GMMM
Joint GMMM
Oracle exposure
Figure 4: Root mean squared error of the coefficient vector by answers per cell. Error bars
are 95% bootstrap intervals over replications.
33

1 5 20
Responses per Query, System, and Period
14
15
16
17
18
19
20
21Relative RMSE of the GEO Effect (percent)
Plug-in GMMM
T wo-stage GMMM
Joint GMMM
Oracle exposure
Figure 5: Relative root mean squared error for the treatment effect of GEO by answers per
cell. Error bars are 95% bootstrap intervals over replications.
B.4 Role of Estimating Carryover and Saturation
We use the same 120 controlled panels with five answers per cell to isolate the contribution
of estimating the transformations. In the first comparison, the plug-in estimator uses the
response data to estimate the parameters of the media transformations from the same
candidates as Joint GMMM while its measurement parameters remain fixed. The second
comparison supplies the true transformations to the plug-in, two-stage, and joint estimators,
leaving only their treatment of measurement uncertainty to differ. This second comparison
is diagnostic because the true transformations would be unavailable in an application. All
comparisons retain 700 importance candidates and 1,000 posterior samples.
Estimating the transformation parameters while fixing the measurement inputs lowers
vector RMSE from 1 .207 to 0 .945. The paired difference is −0.262 with a 95% interval
of [−0.339,− 0.182]. Joint GMMM has vector RMSE 0 .950, only 0 .005 above the plug-in
estimator with estimated transformations, and the interval for this difference is [−0.006, 0.016].
Their relative RMSEs for ∆ G are 17.541% and 17 .525%, with a paired interval that contains
zero. When the true transformation parameters are supplied, vector RMSE ranges from 0 .876
to 0.884 and relative effect RMSE ranges from 17 .066% to 17 .191%. The controlled design
attributes most of the improvement over fixed transformations to their estimation. Averaging
over measurement uncertainty provides no clear additional improvement in ∆ G in this design.
We also compare estimated transformations on 120 matched panels in each of three
designs: the design using estimated occurrence probabilities, shifted transformations, and
combined misspecification. Each panel uses five answers per cell, 700 importance candidates,
and 1,000 samples from the conditional posterior for the response parameters. Plug-in
and joint estimators receive the same transformation samples and panels generated with
common random numbers, but the plug-in estimator fixes the measurement parameters at
34

their fitted values. Table 8 reports the three methods needed to isolate the role of estimating
the transformation parameters.
Table 8: Comparison After Estimating the Transformation Parameters
Design Method Vector RMSE Effect RMSE (%) Coverage
estimated occurrence probabilities Plug-in (fixed) 1.120 18.316 0.950
Plug-in (estimated) 0.929 17.417 0.958
Joint (estimated) 0.942 17.576 0.958
Shifted transformations Plug-in (fixed) 1.815 23.131 0.808
Plug-in (estimated) 0.952 19.135 0.908
Joint (estimated) 0.961 19.133 0.900
Combined misspecification Plug-in (fixed) 2.014 22.738 0.783
Plug-in (estimated) 1.071 18.048 0.917
Joint (estimated) 1.080 18.059 0.917
Vector RMSE measures recovery of the four response coefficients. Effect RMSE is relative to
the true treatment effect of GEO, and coverage refers to its 95% interval. “Fixed” uses the
transformations fixed at their prior means, whereas “estimated” allows the response data to
change the weights assigned to transformation samples.
In the design using estimated occurrence probabilities, vector RMSE is 0 .929 for the
plug-in estimator with estimated transformations and 0 .942 for Joint GMMM. The paired
difference for Joint minus Plug-in is 0 .0133, with a 95% bootstrap interval of [0 .0008, 0.0262].
The corresponding relative RMSEs for ∆ G are 17 .417% and 17 .576%; their difference is
0.159 percentage points with an interval of [ −0.012, 0.330]. Estimating the transformations
also brings the plug-in and joint results close under shifted transformations and combined
misspecification. Table 21 shows that all three intervals for the difference in effect RMSE
contain zero. Across these designs, the improvement over the plug-in method with fixed
transformations comes chiefly from estimating the transformations.
B.5 Cut and Joint Posteriors With Common Candidates
Because the two-stage benchmark retains the transformation prior, it cannot isolate the effect
of allowing response data to revise the measurement parameters. We make that comparison by
evaluating the cut posterior in (20) and the joint posterior on the same M×J combinations
of measurement and transformation parameters. We also retain a plug-in estimator that
estimates the transformations, the two-stage benchmark, and an oracle that observes the true
sequences of media inputs and the true transformations. The computation crosses M = 128
samples of the measurement parameters with J = 700 common transformation samples and
then takes 1,000 conditional coefficient samples for each method. This candidate set differs
from the 700 independent pairs of measurement and transformation parameters used in the
preceding tables, so the numerical levels can differ even when the market panels are the same.
Let JA denote the number of answers per cell. The controlled design crosses JA ∈ {1, 5}
with standard deviations σY ∈ {0.4, 1.2} for the response errors. A fifth condition uses
35

estimated occurrence probabilities with JA = 5 and σY = 1 .2. With 120 replications
per condition, this gives 600 primary panels. Controlled conditions share market inputs
and standardized response innovations, and all methods within a condition use the same
observations. Query volumes and shares of system use remain known, with 50 notice
observations per cell. Holding those sources of information and the construction of EG and
EP fixed lets us compare the estimators as the occurrence probabilities become more precise
and the standard deviation of the response errors changes. Comparing alternative media
inputs would instead require changing howE G andE P are constructed.
Table 3 reports every condition. When σY falls from 1 .2 to 0 .4, the oracle’s relative effect
RMSE falls from 17 .236% to 5 .723%. Methods that estimate the transformation parameters
have RMSE near 6%, while the two-stage benchmark remains near 7%. The concentration
near 17% in the original design reflects the standard deviation of the response errors. Even
when that standard deviation is smaller, Joint GMMM does not uniformly improve estimation
of ∆G.
Each row uses 120 paired replications. Effect RMSE is the relative RMSE of ∆ G, expressed
as a percentage, and Coverage is the empirical coverage of its 95% interval. Cut and Joint
estimate the transformation parameters at each measurement sample, while Plug-in estimates
them at the measurement point estimate. Two-stage retains the transformation prior. With
120 independent replications, coverage near 95% has a binomial Monte Carlo standard error
of about 2 percentage points.
With one answer per cell and σY = 0 .4, Joint GMMM lowers vector RMSE relative
to the cut posterior by 0 .0300; the 95% paired bootstrap interval for this reduction is
[0.0221, 0.0383]. The difference in relative effect RMSE is 0 .035 percentage points with an
interval of [−0.053, 0.131]. When σY = 1.2, the cut posterior has lower vector RMSE at both
collection sizes. Allowing the response data to revise the measurement parameters can affect
coefficient recovery without improving estimation of ∆ G.
In the condition using estimated occurrence probabilities, effect RMSE is 17 .359% for
Plug-in, 17.326% for Cut, and 17 .480% for Joint. The difference for Joint minus Cut is 0 .154
percentage points, with an interval of [0 .046, 0.259], while the interval for Cut minus Plug-in
includes zero. Across the five conditions, none of the paired comparisons of effect RMSE
favors the joint posterior over the cut posterior or the plug-in estimator with estimated
transformations. Table 13 reports all 15 comparisons, including the cases in which the joint
posterior improves coefficient recovery.
These comparisons approximate the specified posterior distributions with a finite set of
candidates. Doubling both candidate counts on eight replications selected in advance per
condition changes estimates from the cut and joint posteriors by at most 1 .602% of the true
effect. The effective sample size within a measurement sample can approach one, especially
when the standard deviation of the response errors is small. Appendix C.3 reports the checks
in full. The paired intervals describe these computations; they do not determine the ranking
under exact posterior integration.
B.6 Numerical Accuracy
Increasing the number of importance candidates from 700 to 1,400 changes root mean squared
error of the coefficient vector from 0.950 to 0.947 and root mean squared error of the treatment
36

effect of GEO from 17 .541% to 17 .525%. Median effective sample size rises from 124 .3 to
251.0. Across replications, the absolute change in the coefficient on the GEO input has
median 0.087 and 90th percentile 0 .253, while the median absolute change in ∆ G is 0.386%
of its true value.
Table 9: Sensitivity to the Number of Importance Candidates
Importance Candidates GEO GEM Vector Effect RMSE (%) ESS ESSq 0.10
700 1.558 0.618 0.950 17.541 124.266 40.394
1400 1.556 0.613 0.947 17.525 250.993 84.884
The lower tail of ESS in Table 10 shows why we report weight concentration alongside
the estimates. In the correctly specified design, the tenth percentile rises from 40 .4 with 700
candidates to 84.9 with 1,400 candidates, whereas it is 8.6 under combined misspecification
with 700 candidates. Panels with low ESS remain in the reported distributions. Increasing
the candidate count assesses the stability of importance sampling, while the hierarchical
Laplace approximation and the numerical probabilities used for coefficient constraints must
be assessed by other calculations. We have not compared these computations with exact
posterior integration.
Table 10: Diagnostics for the Importance Weights
Design Medianq 0.10 q0.05 Minimum
Correctly specified, K=700 124.266 40.394 15.465 3.042
Correctly specified, K=1400 250.993 84.884 36.550 8.176
Combined misspecification, K=700 25.947 8.616 5.466 2.779
B.7 Alternative Data-Generating Processes
The remaining designs alter either the data used to construct the inputs or the response
equation. Two add overdispersion to the occurrence indicators or the counts of sponsored
placements; the others shift the transformation parameters, add a nonlinear term omitted
from the fitted response model, or combine these changes. Each design uses 120 replications
with five answers per cell, 700 importance candidates, and 1,000 samples from the conditional
posterior for the response parameters. Table 11 reports relative RMSE for ∆ G, vector RMSE,
interval coverage, and weight concentration.
Adding overdispersion to the occurrence indicators or the counts of sponsored placements
produces similar relative effect RMSE across the three estimators. Under shifted transfor-
mations, relative effect RMSE is 19 .133% for Joint GMMM, 23 .131% for Plug-in GMMM,
and 22.550% for Two-stage GMMM. When all departures are combined, the corresponding
value for Joint GMMM is 18 .059% with bias −4.683% and coverage 91 .7%. Plug-in GMMM
has RMSE 22 .738% and bias −14.835%, while Two-stage GMMM has RMSE 22 .110% and
bias −14.082%. The matched comparisons in Table 8 attribute most of these differences to
estimation of the transformation parameters. Appendix H.2 reports the oracle, which isolates
error from the response model after the media inputs are observed.
37

Table 11: Results Under Alternative Data-Generating Processes With Five Answers per Cell
Design Plug-in Two-stage Joint Joint Vector RMSE Coverage ESSq 0.10
Occurrence overdispersion 19.005 18.689 18.869 0.887 0.908 35.814
Overdispersion in sponsored placements 18.934 18.677 18.972 0.881 0.900 38.576
Shifted transformations 23.131 22.550 19.133 0.961 0.900 11.181
Omitted nonlinear response 18.145 17.912 17.959 0.951 0.917 30.843
Combined misspecification 22.738 22.110 18.059 1.080 0.917 8.616
The first three method columns report the relative RMSE of the treatment effect of GEO in percent.
Joint Vector RMSE, Coverage, and ESS q0.10 report the RMSE of the coefficient vector, interval
coverage, and the tenth percentile of the Joint GMMM effective sample size.
B.8 Randomized Estimate of the GEO Treatment Effect
With 20 answers per cell, adding the randomized estimate from the target population changes
relative effect RMSE from 17 .430% to 17 .424% and vector RMSE from 0 .950 to 0 .947. When
the randomized estimate is shifted, relative effect RMSE is 18 .013% and signed bias is
4.169%, compared with bias 1 .243% without that estimate. The randomized quantity is
the average treatment effect of GEO, including the component associated with the source
state. Appendix B.2 reports a larger reduction in RMSE in the design based on estimated
occurrence probabilities.
Table 12: Use of a Randomized Estimate With 20 Answers per Cell
Method Effect Bias (%) Effect RMSE (%) Coverage Vector RMSE
Joint GMMM 1.243 17.430 0.967 0.950
Joint + aligned estimate 1.259 17.424 0.967 0.947
Joint + shifted estimate 4.169 18.013 0.967 0.951
“Aligned estimate” uses the randomized estimate from the target population, and “shifted estimate”
adds 0.75 to that estimate.
C Measurement Uncertainty and Numerical Integra-
tion
Once the occurrence probabilities have been estimated, two different sources of error remain.
Replacing a market count by an estimated probability changes the regression input, whereas
averaging over uncertain inputs and transformation parameters requires numerical integration.
Finite collections of repeated answers in a static linear model.Suppose that
Y = βGEG + ε and EG = cπ, where c converts the occurrence probability π to an expected
noticed count by combining the relevant market opportunity and notice probability. Let
bπ= π + u be an estimate based on finitely many generated answers. Assume that all variables
38

have finite second moments, Var(bπ) > 0, E[u|π, c ] = 0, and Cov(bπ, ε) = 0. The population
least squares slope from regressingYonbπwith an intercept is
brate =β G
Cov(π, cπ)
Var(π) + Var(u).(34)
Ifc=c 0 is constant, then the slope becomes
brate =β Gc0
Var(π)
Var(π) + Var(u).(35)
Proof. The population slope is Cov(bπ, Y)/Var(bπ). The conditional mean restriction on u
implies that Cov(u, cπ) = 0 and Cov(u, π) = 0. Together with the assumption on ε, these
relations give Cov(bπ, Y) = βGCov(π, cπ) and Var(bπ) = Var(π) +Var(u), which establish (34).
Ifc=c 0 holds, then Cov(π, cπ) =c0Var(π), and (35) follows.
When u = 0 and c is constant, the change of scale can be absorbed by the response
coefficient. Variation in c across observations changes the covariance in (34), while estimating
π from a finite collection of repeated answers adds the attenuation term in the denominator.
These are distinct reasons why an occurrence probability can fail to represent the corresponding
market count.
C.1 Nonlinear Transformation of an Uncertain Input
Even after an input has been expressed as an expected market count, uncertainty about that
count can matter because the media transformation is nonlinear. Conditional on DM , let eA
denote an uncertain adstock value and define A = E[ eA| DM ]. A plug-in analysis uses h(A).
Averaging over the measurement distribution instead gives E[h( eA) | DM ] before the response
data alter any weights.
Proposition C.1(Transformation of an uncertain media input).Suppose that eA is supported
on an interval A ⊂(0,∞ )and that both eA and h( eA)are integrable conditional on DM . If h
is convex onA, then it holds that
E
h
h( eA)| DM
i
≥h

E[ eA| DM ]

.(36)
If h is concave on A, then the reverse inequality holds. Equality holds when eA is degenerate
conditional onD M or whenhis affine on the convex hull of its conditional support.
Proof. The convex case follows from Jensen’s inequality conditional on DM . Applying the
same argument to−hgives the concave case. The stated equality cases follow directly.
For the Hill function in (15), the second derivative ata >0 is
h′′(a) = κθκaκ−2 ((κ−1)θ κ −(κ+ 1)a κ)
(aκ +θ κ)3 .(37)
If 0 < κ≤ 1 holds, then the Hill function is concave on (0 ,∞ ). If κ >1 holds, its curvature
changes at a = θ((κ− 1)/(κ + 1))1/κ. The direction of the plug-in discrepancy depends on the
range of the input after carryover. Replacing an uncertain sequence by one fitted sequence
need not reproduce the estimate obtained by averaging over that uncertainty.
39

C.2 Joint Weights Under the Measurement Approximation
The joint calculation assigns weights based on the response likelihood to candidates sampled
from the measurement approximation. To interpret the calculation, one must specify the
distribution approached as the number of candidates increases while the measurement
approximation remains fixed.
Let DM denote the measurement data and DY the response data. The parameter vector
η determines the constructed media inputs and their transformations, and q(η| DM ) denotes
the proposal distribution in (17). Let ϑY contain the response coefficients and the remaining
parameters of the response distribution. For fixed η, define the response marginal likelihood
by
mY (DY |η) =
Z
p(DY |η, ϑY )p(ϑY |η)dϑ Y .(38)
The weighted calculation targets
ep(η| DM ,D Y ) = mY (DY |η)q(η| DM )R mY (DY |u)q(u| DM )du .(39)
Proposition C.2(Limit of the joint weights).Suppose that η1, . . . , ηK are independent
samples from q(η| DM )and that0 <
R
mY (DY |η )q(η| DM ) dη <∞. Let K→ ∞ while
DM ,D Y , andqremain fixed, and define
wk = mY (DY |η k)PK
j=1 mY (DY |η j)
.(40)
Let Eq denote expectation under q(η| DM ). For every function h satisfying Eq[|h(η)|mY (DY |
η)]<∞, it holds that
KX
k=1
wkh(ηk)− →
Z
h(η)ep(η| DM ,D Y )dηalmost surely.(41)
Let µh denote the integral on the right. If Eq[mY (DY |η )2(h(η) −µ h)2] <∞ holds, then we
also have
√
K
 KX
k=1
wkh(ηk)−µ h
!
d
− → N(0, σ2 h),(42)
where
σ2 h = Eq [mY (DY |η) 2(h(η)−µ h)2] Eq [mY (DY |η)] 2 .(43)
Ifq(η| DM ) =p(η| DM )holds, thenepequals the joint posterior under the stated model.
40

Proof. The numerator and denominator of the self-normalized estimator are sample averages
underq. The strong law of large numbers gives the almost-sure limits
1
K
KX
k=1
h(ηk)mY (DY |η k)− →
Z
h(η)mY (DY |η)q(η| DM )dη,(44)
1
K
KX
k=1
mY (DY |η k)− →
Z
mY (DY |η)q(η| DM )dη.(45)
Their ratio is the expectation under ep. The central limit theorem for self-normalized impor-
tance sampling gives the second result under the stated second-moment condition. When
q equals the measurement posterior, Bayes’ rule shows that multiplication by the response
marginal likelihood gives the joint posterior up to normalization.
Under the second-moment condition in Proposition C.2, the numerical integration error for
the specified marginal likelihood is of order K −1/2. Replacing the measurement posterior by
qL, or replacing the Student probability of the sign restrictions by a Gaussian approximation,
changes the target distribution. Increasing K leaves those approximation errors unchanged.
When a numerical marginal likelihood is substituted for mY , the same argument gives
convergence to the corresponding reweighted approximation. Effective sample size measures
concentration of the weights. Approximation error must be assessed numerically, and the
identification assumptions in Section 4 must be justified from the study design.
A second limit applies when the entire proposal distribution, including the transformation
parameters, concentrates at one value.
Proposition C.3(Agreement under concentration of the proposal distribution).Let qN (η)be
a sequence of proposal distributions indexed by increasingly informative measurement designs,
where N∈N and N→ ∞, and let bηN be the corresponding plug-in estimate. Suppose that
bηN
p
− →η0 and that qN converges weakly in probability to a point mass at η0. Conditional on
fixed response data DY , suppose that h(η)and mY (DY |η )are bounded and continuous at η0,
withm Y (DY |η 0)>0. Then, it holds that
h(bηN )
p
− →h(η0),(46)Z
h(η)qN (η)dη
p
− →h(η0),(47)
R
h(η)mY (DY |η)q N (η)dηR
mY (DY |η)q N (η)dη
p
− →h(η0).(48)
Proof. Equation (46) follows from the continuous mapping theorem, and weak convergence
of qN gives (47). Applying the same argument to the bounded functions h(η)mY (DY |η )
and mY (DY |η ) gives limits h(η0)mY (DY |η 0) and mY (DY |η 0) for the numerator and
denominator in (48). The denominator has a positive limit, so their ratio converges to
h(η0).
The proposition requires concentration of the entire proposal distribution. More generated
answers provide information about the occurrence probabilities, but uncertainty about market
41

opportunities, notice probabilities, sponsored placements, and media transformations must
also vanish for its conclusion to apply. The comparisons in Section 5.3 isolate the contribution
from estimating the transformation parameters.
Suppose that an external randomized experiment DE is conditionally independent of
DY given the common parameters. The integrated likelihood then factorizes as p(DY ,D E |
η) = mY (DY |η )p(DE | DY , η). Because the two data sources share response coefficients,
the second factor averages the experimental likelihood under the response posterior given
DY . Integrating the experimental likelihood separately would omit this conditioning. The
estimated effect must refer to the same treatment and population, except for any population
difference represented by (23).
C.3 Numerical Comparison on Common Samples
The paired differences in Table 13 use the same 120 replications per condition as the
comparison in which all methods estimate the transformations. Each entry gives the RMSE
of the first method minus that of the second, followed by its 95% interval from 5,000 paired
bootstrap resamples. Negative differences favor the first method, and differences in relative
effect RMSE are expressed in percentage points.
Table 13: Paired RMSE Differences When All Methods Estimate the Transformations
Comparison Vector Difference Effect Difference (pp)
Controlled:J A = 1,σ Y = 0.4
Cut minus Plug-in 0.0201 [0.0142,0.0259] 0.010 [−0.026,0.048]
Joint minus Cut−0.0300 [−0.0383,−0.0221] 0.035 [−0.053,0.131]
Joint minus Plug-in−0.0098 [−0.0165,−0.0038] 0.046 [−0.053,0.157]
Controlled:J A = 1,σ Y = 1.2
Cut minus Plug-in−0.0318 [−0.0447,−0.0192] 0.069 [−0.024,0.166]
Joint minus Cut 0.0304 [0.0140,0.0478] 0.025 [−0.081,0.124]
Joint minus Plug-in−0.0014 [−0.0131,0.0106] 0.094 [−0.022,0.217]
Controlled:J A = 5,σ Y = 0.4
Cut minus Plug-in 0.0034 [0.0014,0.0054] 0.017 [−0.007,0.046]
Joint minus Cut−0.0057 [−0.0081,−0.0033]−0.006 [−0.034,0.019]
Joint minus Plug-in−0.0024 [−0.0044,−0.0002] 0.011 [−0.022,0.050]
Controlled:J A = 5,σ Y = 1.2
Cut minus Plug-in−0.0028 [−0.0091,0.0031]−0.070 [−0.161,0.018]
Joint minus Cut 0.0101 [0.0025,0.0180] 0.036 [−0.057,0.125]
Joint minus Plug-in 0.0072 [0.0001,0.0147]−0.034 [−0.123,0.054]
Estimated occurrence probabilities:J A = 5,σ Y = 1.2
Cut minus Plug-in−0.0184 [−0.0283,−0.0092]−0.033 [−0.152,0.088]
Joint minus Cut 0.0265 [0.0136,0.0406] 0.154 [0.046,0.259]
Joint minus Plug-in 0.0081 [−0.0027,0.0204] 0.121 [−0.016,0.261]
Table 14 reports concentration of the measurement weights and, within each measurement
sample, the transformation weights. Measurement ESS is the median ESS of the joint
42

measurement marginal across 120 replications. The cut marginal is uniform by definition and
has no corresponding entry. Conditional ESS is the median across replications of the median
transformation ESS within a replication, while Minimum ESS is the smallest conditional
transformation ESS over all measurement samples and replications. The last two quantities
agree for Cut and Joint because their conditional transformation weights are the same.
For the numerical check, we increase M from 128 to 256 and J from 700 to 1,400 for the
first eight replications in every condition, leaving the 120-replication comparisons unchanged.
The last two columns report the median and maximum absolute changes in the posterior
mean of the treatment effect as percentages of the true effect. The largest change for Cut
or Joint is 1 .602%, and the largest change in an interval bound is 4 .357%. This calculation
examines sensitivity to the numbers of candidates and posterior samples. Assessing the
Laplace approximation and the Gaussian approximation to the sign probability requires
additional calculations.
Table 14: Integration Diagnostics With Twice as Many Candidates
Method Measurement ESS Conditional ESS Minimum ESS Median Change Maximum Change
Controlled:J A = 1,σY = 0.4
Cut – 10.9 1.0 0.356 0.876
Joint 45.2 10.9 1.0 0.454 0.901
Controlled:J A = 1,σY = 1.2
Cut – 136.6 2.2 0.220 1.038
Joint 111.7 136.6 2.2 0.348 1.548
Controlled:J A = 5,σY = 0.4
Cut – 10.4 1.1 0.440 1.098
Joint 87.7 10.4 1.1 0.365 1.002
Controlled:J A = 5,σY = 1.2
Cut – 138.3 2.2 0.240 0.566
Joint 121.9 138.3 2.2 0.293 1.190
Estimated occurrence probabilities:JA = 5,σY = 1.2
Cut – 105.9 4.3 0.697 1.602
Joint 108.9 105.9 4.3 0.597 1.147
D Attribution With Channel Interactions
The interaction term belongs jointly to GEO and GEM, so the two effects obtained by
disabling one channel at a time need not sum to the effect of disabling both. When an
application requires an additive allocation across the channels, the Shapley values are
ΦG = 1 2 (V(1,0)−V(0,0)) + 1 2 (V(1,1)−V(0,1)),(49)
ΦP = 1 2 (V(0,1)−V(0,0)) + 1 2 (V(1,1)−V(1,0)).(50)
This allocation assigns the interaction once and satisfies ΦG + ΦP = V (1, 1) −V (0, 0) (Shapley,
1988). The same definition extends to more channels, although each additional interacting
channel increases the number of treatment combinations that must be evaluated.
43

E Consequences of Treatment Design in Simulation
Two auxiliary simulations isolate consequences of treatment design that the response equation
alone cannot resolve: one introduces time variation shared by treated and untreated units,
and the other conditions on a variable affected by treatment.
In the first simulation, treated and untreated clusters share platform growth, while treated
clusters receive an additional GEO effect after treatment begins. Across 500 replications, the
comparison of treated units before and after treatment has bias 0 .081 and zero coverage for a
95% interval. Difference-in-differences removes the shared growth component, reducing bias
below 0.001 and RMSE to 0.008, with coverage of 0.954.
Treated pre-post Post-period difference Difference-in-differences
0.00
0.05
0.10
0.15
0.20Change in Response-Feature Probability
True GEO effect
Figure 6: Difference-in-differences removes platform growth shared by treated and untreated
clusters. Error bars equal 1.96 Monte Carlo standard errors.
Table 15: Simulation of Platform Growth
Method Bias RMSE Coverage
Change within treated units 0.081 0.082 0.000
Difference after treatment -0.000 0.032 0.952
Difference-in-differences -0.000 0.008 0.954
The second simulation assigns a direct GEO effect of 0 .70 and an effect through brand
search of 0.88. A response model that omits brand search estimates their sum, 1 .58, at 1 .579.
Because the disturbances for brand search and the response are independent in this additive
design, conditioning on brand search estimates the direct effect at 0 .700. This interpretation
relies on the stated absence of confounding between brand search and the response; it does
not justify conditioning on an arbitrary variable affected by treatment.
44

T otal-effect model
Model controlling for brand search
0.0
0.2
0.4
0.6
0.8
1.0
1.2
1.4
1.6Estimated Effect of GEO Exposure
True total effect
True direct effect
Figure 7: Estimates of the total and direct effects in the additive mediation design with
independent disturbances. Error bars equal 1.96 Monte Carlo standard errors.
Table 16: Simulation of Post-Treatment Adjustment
Method Estimate Standard Deviation Bias for Total Bias for Direct
Model for the total effect 1.579 0.028 -0.001 0.879
Model controlling for brand search 0.700 0.031 -0.880 0.000
F Public Referral Traffic Analysis
The repository accompanying Watanabe & Nakayashiki (2026) contains weekly treated
and control session indices from July 2025 through May 2026. 2 It does not contain the
contemporaneous question counts, generated answers, or notice observations needed to
construct the GEO input, and it has no information on sponsored placements. The analysis
uses the referral indices alone. The source material places the treatment transition around
December 2025 and January 2026. We use December 30, 2025 as the central first post-
treatment week and examine the neighboring weekly dates.
Let Rt denote the ratio of treated to control sessions and let rt = logR t. For a specified
first post-treatment weekt 0, we estimate
rt =δ 0 +δ 1t+δ 21(t≥t 0) +δ 3(t−t 0)1(t≥t 0) +e t.(51)
Using Newey–West covariance with four lags, we report an interval and a t test for the
immediate ratio exp(δ2). A platform shock cancels from Rt when it changes treated and
control traffic by the same proportion. The segmented terms describe how the groups diverge
from the trend estimated before treatment, including changes that affect them differently.
For December 30, the immediate ratio is 1 .842, with a 95% interval from 1 .306 to 2 .599.
The geometric mean ratio implied by the model over the final four weeks is 2 .301, compared
2https://github.com/glasp-co/aeo-natural-experiment
45

with an observed geometric mean of 2 .055 after adjustment for the pre-treatment trend. The
placebo rank is 0.150 among 19 admissible dates before treatment. Because the pre-treatment
period contains changes at least as large as the estimate at rollout, this diagnostic does not
by itself establish a treatment effect.
Table 17: Referral Traffic Analysis
Quantity Estimate Lower Upper P-value
Weekly trend factor before treatment 1.027 1.007 1.048 0.010
Immediate ratio: all referral sessions 1.842 1.306 2.599<0.001
Immediate ratio: engaged referral sessions 2.388 1.487 3.833<0.001
Final four weeks: fitted ratio 2.301 1.342 4.032 0.026
Final four weeks: adjusted observed ratio 2.055 – – –
Monthly ratio of growth factors 1.750 – – –
Placebo rank before treatment 0.150 – – –
2025-07 2025-08 2025-09 2025-10 2025-11 2025-12 2026-01 2026-022026-03 2026-04 2026-05 2026-06
Week
−0.5
0.0
0.5
1.0
1.5
2.0
Log Ratio of Treated to Control Sessions
Observed log ratio
Segmented regression
Extrapolated pre-intervention path
First post-intervention week
Figure 8: Observed and fitted log ratio of treated to control referrals. The vertical line marks
the first post-treatment week, and the dotted path extrapolates the relation estimated before
treatment.
The date assigned to the treatment transition materially changes the estimate. Moving the
first post-treatment week from December 16, 2025 to January 6, 2026 changes the immediate
ratio from 1 .183 to 2 .404. The intervals for December 16 and December 23 include one,
whereas those for December 30 and January 6 exclude it. We report this range because the
source material describes a transition window and does not identify one breakpoint.
The source study reports that bot filtering changed in mid-March and that the composition
of sessions subsequently changed, with a larger increase in engagement for the treated group
(Watanabe & Nakayashiki, 2026). A differential measurement change can remain in the ratio
of treated to control sessions. Because the exact date is unavailable, we use March 10, March
46

Table 18: Sensitivity to the First Post-Treatment Week
First Post-Treatment Week Ratio Lower Upper P-value
2025-12-16 1.183 0.665 2.103 0.560
2025-12-23 1.412 0.852 2.341 0.176
2025-12-30 1.842 1.306 2.599<0.001
2026-01-06 2.404 1.770 3.265<0.001
17, and March 24 as alternative weekly starts. For each date, we first add a change in level to
(51) and then allow both the level and slope to change. We also fit the original specification
to the 36 weeks ending before March 10, using the terms described in Appendix I. Each
Table 19: Sensitivity to the Referral Measurement Change
Measurement Specification Date All Sessions Engaged Sessions
No measurement change – 1.842 [1.306, 2.599] 2.388 [1.487, 3.833]
Level change 2026-03-10 1.782 [1.233, 2.575] 2.328 [1.385, 3.914]
Level and slope change 2026-03-10 1.337 [0.937, 1.907] 1.543 [0.981, 2.427]
Level change 2026-03-17 1.713 [1.191, 2.464] 2.219 [1.322, 3.725]
Level and slope change 2026-03-17 1.387 [0.977, 1.967] 1.617 [1.032, 2.534]
Level change 2026-03-24 1.685 [1.174, 2.419] 2.125 [1.287, 3.508]
Level and slope change 2026-03-24 1.455 [1.025, 2.067] 1.696 [1.083, 2.655]
Sample ending before date 2026-03-10 1.337 [0.937, 1.906] 1.543 [0.982, 2.426]
entry reports exp(δ2) and its 95% interval. All specifications use Newey–West covariance
with four lags, the finite-sample correction, and a t reference distribution. The final row uses
36 observations; all other rows use 47.
When a change in measurement level begins on March 17, the ratio for all sessions is
1.713, with an interval of [1 .191, 2.464]. Allowing the slope to change reduces the ratio to
1.387, with an interval of [0 .977, 1.967]. Across the three candidate dates, estimates from
specifications with changes in both level and slope range from 1 .337 to 1 .455. The sample
ending before March 10 gives 1 .337, with an interval of [0 .937, 1.906]. Later observations
help estimate the post-treatment intercept and trend even though filtering changed after
treatment began, so the two estimated changes are statistically dependent. The estimate at
rollout is correspondingly sensitive to the specification of the later measurement change.
The week beginning December 30 has the largest Cook’s distance, 0 .741, and the largest
absolute studentized residual, 3 .706. Leave-one-out estimates range from 1 .700 to 2 .272,
while changes in the response specification produce ratios from 1 .842 to 2 .647. Newey–West
lag choices from zero through 12 leave the baseline interval above one. The immediate ratio
exceeds one in every reported specification, but whether its interval excludes one depends on
the first post-treatment week and on the treatment of the measurement change.
47

G Bayesian Computation
The Bayesian computation in Section 3 combines Laplace approximations for the models
used to construct the inputs with conditional calculations for the response model. The priors,
importance weights, and update from a randomized estimate are specified below.
G.1 Noncentered Laplace Approximation for the Measurement
Models
The hierarchical measurement models are approximated in coordinates that keep the stan-
dardized random effects independent of their unknown scale. For a hierarchical logit model,
write u = BQσ eu, where eu∼ N(0, IQ−1), and assign a normal prior to logσ . We optimize
the posterior in ( α, eu,logσ ) coordinates. The analytic Hessian includes the cross derivatives
between the fixed effects and the scale of the random effects. After inversion, the delta
method maps the covariance to (α,u) coordinates.
The model for occurrence of the target name contains an intercept and a question
characteristic. Its other fixed effects represent differences between generative systems, calendar
variation, and the change associated with the GEO source state. Calendar variation consists
of a scaled trend and harmonic terms with period 18. The prior standard deviation is 3 .0
for the intercept, 1 .5 for the question characteristic and system effect, 1 .0 for the calendar
terms, and 1 .5 for the GEO coefficient. The log standard deviation of the question effects
has a normal prior with mean log(0.45) and standard deviation 0 .55. The notice model omits
the calendar and GEO terms, and its log standard deviation has prior mean log(0.35).
G.2 Posterior for the Response Model
We place a normal inverse-gamma prior on the response coefficients and variance, with
nonnegative main effects for GEO and GEM:
σ2 Y ∼InverseGamma(2.5,2.0),(52)
β|σ 2 Y ∼ N(0, σ2 Y V0) subject toβ G ≥0, β P ≥0,(53)
where
V0 = diag(2.52,5.0 2,4.0 2,1.5 2).(54)
The simulations contain no established media channels. We residualize the response and the
four regressors associated with GEO and GEM with respect to W , which is equivalent to
assigning a flat prior to the control coefficients. This residualization requires a finite control
matrix with full column rank and positive residual degrees of freedom.
For each channel m, the decay parameter is αm = 0.90Um with Um ∼Beta (2, 2). The
saturation midpoint is θm = 0.25 + 1.25Vm with Vm ∼Beta (2.5, 2.5), and the Hill exponent
isκ m = 0.25 + 0.75Rm withR m ∼Beta(3,2). The lag length isL m = 8.
For candidate k, let eY and fMk denote the response and the four target regressors after
residualization with respect to W . Before the sign restrictions are imposed, the prior in (53)
48

yields a normal inverse-gamma posterior whose marginal distribution for the coefficient vector
is multivariate Student t. We approximate the posterior probability that ( βG, βP ) lies in the
positive orthant with a Gaussian distribution matched to the posterior mean and covariance.
The constrained integrated likelihood equals the unconstrained marginal likelihood multiplied
by this posterior probability and divided by the prior probability 1/4.
For independent candidates, we first sample σ2 Y from its inverse-gamma posterior and
then sample the coefficient vector from the corresponding multivariate normal, retaining
vectors that satisfy βG ≥ 0 and βP ≥ 0. In the crossed comparison, the marginal Student
distribution is first conditioned on the less probable of the two positivity events. That
coefficient is sampled from its truncated univariate Student distribution, and the remaining
coefficients are sampled from their conditional Student distribution. Rejection based on the
other sign yields the same constrained marginal distribution. Both procedures continue until
they obtain the required number of posterior samples; neither uses a fixed proposal limit.
The Gaussian orthant approximation affects the candidate weights, whereas the conditional
coefficient samples follow the Student distribution. The two-stage benchmark retains the
prior for the transformations. The cut and joint procedures use the response data to estimate
the transformation parameters, and the plug-in comparisons state whether those parameters
are fixed or estimated.
G.3 Update With a Randomized Estimate
An estimate from a randomized experiment can update the Gaussian approximation to the
coefficient posterior when it refers to the same treatment and target population as the model
estimand.
For candidate k, let N (µk, Σk) approximate the unconstrained coefficient posterior given
the response data. Define the region satisfying the sign restrictions by C = {β : βG ≥ 0, βP ≥
0} and let Pk be its probability under this approximation. Let Mit,k(aG, aP ) denote the four
regressors, including the indicator for the source state, constructed under the treatment
sequences indexed by ( aG, aP ). With NE = n|TE|, the average difference between the design
vectors is
dk = 1 NE
nX
i=1
X
t∈TE
(Mit,k(1,1)−M it,k(0,1)),(55)
τE,k =d T k β.(56)
Each candidate supplies its own design vector, including the component associated with the
source state. Write vE = s2 E + σ2 tr and sk = vE + dT k Σkdk. The unconstrained Gaussian update
is
µ+ k =µ k + Σkdk sk  bτE −d T k µk  ,(57)
Σ+ k = Σk − ΣkdkdT k Σk sk .(58)
Let P + k be the probability of C under N (µ+ k , Σ+ k ). If φ(x; m, v) denotes the normal density
with mean m and variance v, the predictive factor under the sign restrictions and the updated
49

candidate weight are
ℓE,k =φ

bτE;d T k µk, sk  P + k Pk ,(59)
w+ k = wkℓE,kP
h whℓE,h
.(60)
The ratio P + k /Pk follows by integrating the product of the Gaussian likelihood and the
truncated Gaussian distribution over C. After a candidate is selected with probability w+ k ,
the coefficients are sampled from N (µ+ k , Σ+ k ) conditional on C. The weight calculation and the
conditional coefficient distribution use the same Gaussian approximation and sign restrictions.
G.4 Model for Sponsored Placements
The prior for the model of sponsored placements assigns standard deviation 3 .0 to the
intercept and 1 .5 to the elasticity with respect to spending. The demand and promotion
coefficients each have standard deviation 1 .0. Optimization imposes ϕS > 0, and Gaussian
proposal samples that violate this restriction are discarded. Sponsored notice has a Beta(1, 1)
prior, whose posterior mean supplies the plug-in value.
H Simulation Models
The simulation designs vary the source of measurement uncertainty, the response equation,
and the treatment sequence. The model and parameter values below define the principal
comparisons and the additional data-generating processes.
H.1 Main GMMM Simulation
In the controlled design, the true transformation parameters are sampled from the same
distributions used in estimation. The resulting comparison is favorable to that prior speci-
fication. Another design fixes the transformation parameters away from the prior centers
while keeping them within the prior support.
The panel contains five markets observed for 36 periods. Each market has six product
clusters linked to 12 question clusters on two generative systems. Two product clusters first
receive GEO in period 19, two first receive GEO in period 23, and two remain untreated.
Periods are indexed by t∈ {1, . . . ,36}. The log-odds coefficient of the GEO source state in
the occurrence model is 0 .72, and the standard deviation of the question effects is 0 .45. The
remaining variation reflects the generative system and calendar time: the coefficient for the
second system is 0 .24, and the calendar terms combine a linear trend with periodic variation.
Question counts follow a log-normal distribution driven by latent demand and seasonality,
while the shares of use across systems follow a symmetric Dirichlet distribution.
The design based on the collected answers uses (33). It samples one question index
for each pair of models and gives equal representation to English and Japanese. With P
generative systems, the fitted occurrence model contains P (Q− 1) centered question effects.
Each system has its own vector of effects, and the vectors share one scale parameter. This
50

likelihood reproduces the estimated baseline probabilities while retaining the same coefficient
for the GEO source state.
The probability of positive spending and the positive amount spent depend on promotion,
market and product-cluster effects, and demand measured before treatment. The coefficient
vector in the model for sponsored placements is (2 .10, 0.82, 0.20, 0.14), and the notice proba-
bility for those placements is 0.57. The two generated channels use transformation parameters
sampled from the distributions that generate the estimation candidates. The response errors
have standard deviation 1 .20. Controls consist of additive market and product-cluster effects,
a linear time trend, two seasonal terms, and the two predictors observed before treatment.
Each conditional response posterior contains 1,000 samples. The independent randomized
experiment has 400 equally allocated units and a response standard deviation of 3 .5. The
treated mean differs from the control mean by the true average treatment effect of GEO over
the panel, ∆G/1080. Inference constructs dk using (56). Its first coordinate is 320 /1080, while
the coordinate for the main GEM effect is zero because GEM spending is held fixed. A second
version adds 0.75 to the same true effect. Both analyses use the specified transport standard
deviation 0.20. The estimator continues to use the specified transport standard deviation
without an additional mean shift, so the added 0.75 becomes an unmodeled difference between
the experimental and target populations.
H.2 Alternative Data-Generating Processes
Five designs alter either the measurement model, the response equation, or both while retaining
the panel dimensions and treatment sequences. The numbers of importance candidates and
conditional posterior samples are also unchanged.
Two designs change the distribution of the measurement data. Occurrence overdispersion
first samples a cell probability from a Beta distribution with concentration 12 and then
generates repeated Bernoulli indicators. Overdispersion in sponsored placements uses a
gamma–Poisson mixture with dispersion 4. Two other designs change the response equation.
The first uses (α, L, θ, κ) = (0.84, 8, 1.42, 0.92) for GEO and (0 .78, 8, 1.32, 0.90) for GEM. The
second adds 0 .80(H G)2 to both the response and the true treatment effect of GEO. The fifth
design combines all four departures. Each difference is Joint GMMM minus the plug-in
Table 20: Combined Departure in the Measurement and Response Models
Method Effect Bias (%) Effect RMSE (%) Coverage Vector RMSE ESS ESSq 0.10
Plug-in GMMM -14.835 22.738 0.783 2.014 – –
Two-stage GMMM -14.082 22.110 0.850 1.501 – –
Joint GMMM -4.683 18.059 0.917 1.080 25.947 8.616
Oracle inputs -1.186 16.988 0.917 0.775 – –
estimator that also estimates the transformations. The bounds are 95% paired bootstrap
intervals from 5,000 resamples of the 120 common panels within each design. Differences in
effect RMSE are measured in percentage points. A positive value favors the plug-in estimator.
51

Table 21: Paired Differences When Both Methods Estimate the Transformations
Design Metric Difference Lower Upper
Estimated occurrence probabilities Vector RMSE 0.0133 0.0008 0.0262
Estimated occurrence probabilities Effect RMSE (pp) 0.159 -0.012 0.330
Shifted transformations Vector RMSE 0.0095 -0.0004 0.0194
Shifted transformations Effect RMSE (pp) -0.002 -0.165 0.150
Combined misspecification Vector RMSE 0.0096 -0.0006 0.0196
Combined misspecification Effect RMSE (pp) 0.012 -0.133 0.157
H.3 Simulation With Platform Growth
This simulation contains 80 clusters observed for 48 periods on three platforms. Half of the
clusters receive GEO beginning in period 24. Each platform has a common time path that
combines deterministic growth, seasonal variation, and a random walk, while the log-odds
coefficient of GEO is 0 .65. Across 500 replications, we compare difference-in-differences with
the change before and after treatment among treated units and with the difference between
treated and control units after treatment.
H.4 Simulation With a Post-Treatment Variable
A continuous randomized encouragement changes the constructed GEO input, which affects
the response directly and through brand search. The direct effect is 0 .70, and the effect
through brand search is 0.88, giving a total effect of 1.58. Across 800 replications, we compare
a response regression on the treatment with a regression that also conditions on brand search.
I Computation for the Referral Analysis
The referral analysis uses segmented regression and then varies the treatment date, trend
specification, lag length, and influential observations. The details below define those calcula-
tions.
The analysis uses 47 weekly observations and the regression with four parameters in (51).
Inference uses Newey–West covariance with four lags. The date analysis moves the first
post-treatment week from two weeks before the central date to one week after it, while the
lag analysis considers every integer from zero through 12. Other checks alter one part of
the response specification at a time. They remove the first post-treatment week, shorten
the period before treatment, change the baseline trend, or omit the common linear trend.
Influence is assessed through 47 leave-one-out regressions, together with studentized residuals
and Cook’s distance.
For a candidate week tc at which measurement changes, the level specification adds
ζ01(t≥t c) to (51). The specification allowing both level and slope changes also adds
ζ1(t−t c)1(t≥t c). These terms represent differential measurement changes that remain in the
log ratio of treated to control sessions. Holding the first post-treatment week at December 30,
we fit each candidate tc to all sessions and to engaged sessions. The truncated specification
52

retains the original four regressors and uses observations strictly before March 10. Every
reported ratio exponentiates the treatment coefficient δ2, while the later measurement terms
account for the subsequent change. With n observations and p regressors, the Newey–West
covariance uses the correctionn/(n−p), and the intervals usen−pdegrees of freedom.
The fitted ratio over the final four weeks is computed from the segmented regression.
Its interval uses 5,000 residual moving-block bootstrap replications. Residuals are centered
within the periods before and after treatment, sampled in circular blocks of four weeks within
each segment, and added to the fitted values before the regression is refitted. The reported
95% interval contains the 2.5th and 97.5th percentiles of the resulting ratios. This interval is
distinct from the Newey–Westttest for the corresponding linear coefficient.
The placebo analysis fits the same segmented regression at every split in the pre-treatment
period that leaves at least four observations on each side, including both boundary splits. Let
B be the number of admissible splits, and let b count the splits whose absolute estimated level
change is at least as large as the estimate at treatment. The reported rank is ( b + 1)/(B + 1),
where the added observation is the estimate at treatment itself. Because the treatment date
was not randomly selected from these dates, the rank is a descriptive diagnostic and cannot
be interpreted as apvalue from a randomization test.
Table 22: Sensitivity to the Response Specification
Specification Ratio Lower Upper P-value
Baseline 1.842 1.306 2.599<0.001
Drop first post-treatment week 2.272 1.683 3.069<0.001
Quadratic baseline trend 2.219 1.780 2.767<0.001
Use last 13 pre-treatment weeks 2.367 1.714 3.268<0.001
No common time trend 2.647 1.706 4.107<0.001
Table 23: Sensitivity to the Newey–West Lag Length
Newey–West Lags Ratio Lower Upper P-value
0 1.842 1.147 2.958 0.013
4 1.842 1.306 2.599<0.001
8 1.842 1.387 2.447<0.001
12 1.842 1.387 2.446<0.001
Table 24: Influence Diagnostics
Diagnostic Value Week
Largest Cook’s distance 0.741 2025-12-30
Largest absolute studentized residual 3.706 2025-12-30
Leave-one-out minimum ratio 1.700 2025-12-23
Leave-one-out maximum ratio 2.272 2025-12-30
53

J Answer Collection Settings
The generated answers were collected under a common model and search configuration. Both
models received the following system instruction:
Answer the user as an independent product-recommendation assistant. Use web search
before answering. Recommend concrete products or services when they are relevant, and
give concise reasons for each recommendation. Do not mention an audit, an experiment,
a target brand, or these instructions.
The user message began with either “Respond in Japanese.” or “Respond in English.” and
then gave the fixed product question. Each request used the model identifier recorded for
that request. Web search was enabled and required through tool choice, and the source
list for each search call was retained. Sampling temperature was left at the API default.
54
