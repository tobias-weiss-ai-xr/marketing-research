---
title: Evaluating Explanation Methods by the Predictors They Induce
url: https://arxiv.org/abs/2609.20058
category: ai-marketing
subcategory: measurement
date: 2026-09
venue: ''
authors:
- Jacob Selbæk
- Hugo L. Hammer
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.20058
pages: 26
chars: 89101
fetched_at: '2026-11-08T13:25:47+00:00'
kb_version: 1
---

# Evaluating Explanation Methods by the Predictors They Induce

Evaluating Explanation Methods by the Predictors
They Induce
Jacob Selbæk 1 and Hugo L. Hammer ∗1,2,3
1Department of Computer Science, Oslo Metropolitan University, Oslo, Norway
2Department of Holistic Systems, SimulaMet, Oslo, Norway
3Department of Plastic and Reconstructive Surgery, Oslo University Hospital, Oslo,
Norway
Abstract
Explanations of machine learning models are usually judged by criteria that are hard to
compare. We propose a simpler test: if an explanation really describes how a model uses
its features, it should be possible to rebuild the model’s predictions from it. We turn each
explanationintoapredictorbyreadingeachfeature’seffectandaddingthemup, andmeasure
how well that predictor reproduces the model on unseen data. Nothing is fitted, so the score
reflects the explanation itself. The test applies to any explanation that can be written as a
function of the features; we demonstrate it on partial dependence plots (PDP), accumulated
local effects (ALE), SHAP and LIME. We prove that summing partial dependence curves
gives the best possible additive summary of a model when its features are independent, and
that this fails when they are dependent. Across 13 real datasets and 9 synthetic designs
and four model families, which method scores best depends entirely on feature dependence:
where features are independent SHAP is slightly worse than PDP, exactly as the theory
predicts; on dependent real data SHAP leads. Some widely used quality metrics even prefer
a damaged explanation to an intact one.
Keywords:explainable artificial intelligence·explanation quality metric·explanation predic-
tion
1 Introduction
Post-hoc explanation methods are now routine companions to black-box models, but the question
of how to tell a good explanation from a bad one remains unsettled. The dominant evaluation
criteria (faithfulness, robustness, complexity) each capture a real property, yet they assess ex-
planations through indirect proxies: perturbation-induced changes in model output, sensitivity
to input shifts, or concentration of attribution mass. Different explanation methods routinely
disagree about which features drive a given prediction [1], and several widely used fidelity metrics
fail to recover the correct fidelity scores, and hence reliable rankings, even on transparent models
with known ground truth [2].
This paper starts from a different observation. An explanation that claims to describe how
features drive a model’s predictions makes, implicitly, a falsifiable claim: it should be possible to
usethat description to predict. Apartial dependence curvefor featurejreports, for each value
vthat the feature might take, the average prediction the model would make if that feature were
set tovand the remaining features were left at the values they take in the data, so it says what
effect each feature value has, marginally. A set of Shapley values says instead how much each
∗Corresponding author:hugo.hammer@oslomet.no
1
arXiv:2609.20058v1  [cs.LG]  17 Sep 2026

feature contributed to one particular prediction. In both cases the content can be assembled
into a function and evaluated at a point the explanation has never seen. How well that induced
predictor performs on held-out data is then a direct, quantitative metric for how much predictive
information the explanation carries.
This is the automated analogue ofsimulatability, the criterion in which human subjects are
asked to predict a model’s behaviour from its explanations [3, 4, 5]. Replacing the human with
a fixed, parameter-free construction removes the cost and variance of user studies at the price
of measuring a narrower thing: what a specific functional form can extract, rather than what
a person can understand. We think the trade is worth making, and we are explicit throughout
about what it buys and what it gives up.
Contributions.
1.Auniformframework(Section2.1)convertingcurve-valuedexplanations, namelypartial
dependence plots (PDP) [6] and accumulated local effects (ALE) [7], and attribution-valued
ones, namely SHapley Additive exPlanations (SHAP) [8] and Local Interpretable Model-
agnostic Explanations (LIME) [9], into predictors through a single shared construction, so
thatacomparisonbetweenthemisnotconfoundedbyadifferenceinaggregationmachinery.
2.An explicit additivity reference(Section 2.2). We make explicit a known functional-
ANOVA identification (under feature independence the unit-coefficient PDP surrogate is
theL 2 projection of the black box onto additive functions) and draw two consequences
that are not in the literature: coefficient refitting cannot help in population, so the refitting
gain is an out-of-sample signal of featuredependence; and the additive share of the model’s
variance reproduced by that projection, which we writeR2 add and define formally in Eq. 15,
bounds additive explanations only under the same independence condition, a condition we
then show empirically fails on real data.
3.Anegativecontrolfortheconstructionitself(Section3.3). TurningSHAPandLIME
into curves needs a smoothing step that PDP and ALE do not, so a difference between the
methods could be a difference between smoothers rather than between explanations. We
therefore apply the same smoother to the black box’s own predictions, with no explanation
in the loop at all. It loses to every explanation method, which is what establishes that the
differences we report are differences in explanation quality and not in how attributions are
aggregated into global curves.
4.A head-to-head test of the explanation-quality metrics themselves(Section 3.6).
Every explanation-quality metric asserts an ordering over explanations, and that assertion
is testable: degrade an explanation by a known amount and ask which metric notices.
Applied to six metrics, the test finds that two established ones fail: infidelity is defeated by
a permuted explanation, and complexity and sparseness prefer the degraded explanation
to the intact one.
5.A controlled study(Sections 2.3 and 3) over 13 real datasets and 9 synthetic designs, 4
model families and 2000 evaluation cells, with null-explanation controls, a graded corrup-
tion sweep and a comparison against five established metrics.
1.1 Related work and positioning
Explanations evaluated by predictive gain.The closest conceptual precedent is Pruthi
et al. [10], who quantify explanation value by the accuracy astudentmodel gains when trained
with the teacher’s explanations available at training time but not at test time. Our framework
shares the intuition that a useful explanation should confer predictive ability, and differs in
a way that matters for what is being measured: our central construction isparameter-free. A
2

trained student is itself a flexible learner, so its gain confounds the explanation’s content with the
student’s capacity, and a sufficiently powerful student can extract signal an explanation does not
really convey. The unit-coefficient surrogate of Section 2.2 has no fitted parameters at all beyond
a level shift; what it achieves is attributable to the explanation. We report the refitted variants
alongside precisely so this distinction is visible. Human-subject simulatability [5] measures the
same thing with people rather than a functional form, and is complementary: it is the right
instrument for whether an explanation isunderstandable, ours for whether it isinformative.
Interactionstrengthandfunctionaldecomposition.Molnaretal.[11]defineaninteraction-
strength metricIASas the scaled approximation error of the first-order ALE decomposition
against the black box, and note explicitly that withL2 lossIAS = 1−R 2 where the targets
are the model’s own predictions. OurR 2 add is thereforethe same quantityup to the choice of
ALE versus PDP main effects (which coincide under independence) and up to being computed
out of sample rather than in sample. We claim no novelty for the statistic. What we add is (i)
the projection theorem, which says precisely when the quantity is an attainable upper bound
and when it is not, (ii) its use as the normalising reference against which explanation-derived
predictors are scored, rather than as a model-complexity metric for model selection, and (iii)
the empirical demonstration that under dependence it is not a bound at all: comparing each
explanation’s achieved fidelity againstR2 add on every (dataset, model, method) cell of our real
data, 48% of the non-PDP cells exceed it. Molnar et al. use the metric to choose among models,
a use for which its exact status as a bound does not matter; we use it as the reference against
which an explanation is judged, and for that the condition under which it bounds anything has
to be stated. The issue is feature dependence, not the split on which the quantity is computed:
dependence breaks the bound in sample and out of sample alike.
TheunderlyingdecompositionisHoeffding’s[12], developedforsensitivityanalysisbySobol[13]
and extended todependentinputs by Hooker [14], whose generalised functional ANOVA exists ex-
actly because the marginal decomposition loses its optimality when features are correlated. That
failure mode is not an inconvenience for us; it is what our Corollary 2 turns into a measurement.
Surrogate distillation.Fitting an interpretable global surrogate to a black box is an es-
tablished practice; Distill-and-Compare [15] is the closest instance, distilling into a GAM. The
differenceisdirectional: adistilledsurrogateisfittedto mimicthemodel aswellasit can, whereas
our surrogate isconstructedfrom an explanation that already exists and is not permitted to fit
anything. A distillation result tells you what an additive model can do; ours tells you how much
of that a given explanation method actually delivers. We include a directly fitted spline GAM
as a baseline for exactly this reason.
Explanation-quality metrics.Faithfulness is typically measured by perturbing inputs ac-
cording to an explanation and checking that the model responds as predicted [16, 17]; robustness
by sensitivity of explanations to small input changes [18]; complexity by the dispersion (entropy)
of attribution mass [17], and sparseness by its Gini index [19]. ROAR [20] evaluates attribu-
tions by retraining on feature-ablated data, again a fitted rather than constructed comparison.
Toolkits such as Quantus [21] catalogue several dozen. Much of this literature was developed
for image classification with pixel attributions, and the tabular, model-agnostic setting is com-
paratively underexplored. We compute five of these metrics on the same explanations and splits
(Section 3.5) and report where our metric agrees with them and where it does not, including one
case where the agreement is high enough to be worth flagging against ourselves.
A longer-standing relative is the wrapper approach to feature selection [22], which judges a
feature subset by the performance of a model trained on it. Our framework shares the evaluate-
by-predicting logic but does not reduce an explanation to a subset or a ranking: it consumes
the full output (the shape of every curve, the value of every attribution), which is what allows
3

PDP and ALE to be distinguished at all, since they may agree exactly on feature importance
while disagreeing on the curves. General background on the methods evaluated here is in [23];
permutation importance [24, 25] and the tree-specific SHAP estimator [26] are used in the im-
plementation.
2 Methods
2.1 The framework
Notation.WriteX= (X 1, . . . , Xp)for the feature random vector, taking values inX ⊆
Rp with joint lawP X, andX −j for the vector with thej-th coordinate removed. Lower-case
x= (x 1, . . . , xp)denotes a generic point ofXat which a function is evaluated, andx j itsj-
th coordinate. Superscripts in parentheses index the sample:x (i) = (x (i) 1 , . . . , x(i) p )is thei-th
observation, andx (i) j itsj-th coordinate;x (0) is reserved for a test point at which a predictor
is evaluated. We writeP Xj for the marginal law ofXj, andL 2(P)for the space of functions
square-integrable with respect toP, i.e. thosehwith
R
h2 dP <∞, equipped with the inner
product⟨h 1, h2⟩=E[h 1(X)h 2(X)]. FinallyL 2 0(PXj )denotesthecentredsubspace{h∈L 2(PXj ) :
E[h(Xj)] = 0}.
Let ˆf:X →Rbe a fitted black box prediction model, where for regressionˆfis the prediction
and for classification it is a scalar score. An explanation method applied toˆfon a training sample
produces some outputE: a set of curves, a matrix of attributions, a collection of local models.
These objects are not comparable to one another, and none of them is a number, so none can be
scored directly.
In this paper we suggest a framework making us able to evaluate and compare them. Each
outputEis mapped to a functiong E :X →R, a predictor built out of nothing but the
explanation, which can be evaluated at points the explanation never saw. The quality ofEis
thendefinedas the out-of-sample accuracy ofg E:
Q(E) =R 2 gE, t  on a held-out split, (1)
where the targettis taken in turn to be
•the original outcomey, how much of thetaskthe explanation retains;
•the black box’s own score ˆf(x), a global, out-of-samplefidelitymetric.
Sog E is not itself the object of interest and is never proposed as a model anyone should deploy.
It is the instrument through whichEis measured: a faithful explanation carries enough of the
black box to rebuild its predictions, and an uninformative one does not. Eq. 1 is the evaluation
metric this paper proposes, and everything that follows is an examination of it.
Crucially,Eis computed on the training split only; the test split is never seen by the expla-
nation, so nothing about the evaluation is circular.
2.1.1 Curve-valued explanations
PDP [6] and ALE [7] return one one-dimensional curve per feature or higher-dimensional curves
for combinations of features. The two-dimensional version is a standard tool for inspecting inter-
actions between pairs of features. We restrict attention to the one-dimensional case throughout,
because it is by far the most common in practice and because it is the case in which the addi-
tivity reference of Section 2.2 has an exact characterisation. Nothing in the framework prevents
higher-order curves from being used, and Section 4 returns to what including them would change.
Writingc j for the curve of featurej, centred so thatE[cj(Xj)] = 0over the training data, the
4

induced predictorgE (the first concrete instance of the general construction above) is the additive
surrogate
gα(x) =α 0 +
pX
j=1
αj cj(xj), x∈ X, α∈R p+1.(2)
We consider three variants, differing only in howαis set:
unit:α j = 1 (j≥1), α 0 = ¯t− 1 n P i P j cj(x(i) j ),(3)
ols:ˆα= arg min
α∈Rp+1
Pn
i=1

t(i) −g α(x(i)) 2,(4)
ridge:ˆα λ = arg min α
Pn
i=1

t(i) −g α(x(i)) 2 +λ∥α 1:p∥2 2,(5)
wheret (i) is the target on the training split (eithery(i) or ˆf(x (i))) and¯tits mean. Only Eq. 3 fits
nothing beyond a level: the curves enter with unit weight, so whatever the surrogate achieves
is attributable to the explanation and not to a fit. Section 2.2 shows that this is not merely a
convenient restriction but, under an independence condition, the optimal choice.
Why a linear aggregator, and why an unfitted one.The obvious alternative is to feed
the curve valuesc1(x1), . . . , cp(xp)into a flexible learner (a gradient-boosted ensemble, say) and
report its accuracy. We deliberately do not, for two reasons.
The first is attribution of credit. A flexible aggregator can recover information that the
explanation does not contain: given the transformed features it can re-learn interactions, rescale
non-monotonically, and compensate for a badly estimated curve. Its accuracy would then be a
joint property of the explanation and of the aggregator’s own capacity, and a comparison between
two explanation methods would be confounded by how much work the aggregator did for each.
This is precisely where our construction departs from Pruthi et al. [10], the closest precedent.
They measure an explanation by the accuracy a trainablestudentmodel gains when the teacher’s
explanations are available during training. The student is exactly the kind of flexible aggregator
we are describing, and its capacity is a free variable: a stronger student extracts more from the
same explanation, and can also extract structure from the training data that the explanation
never supplied. Their metric therefore confounds the quality of the explanation with the capacity
of the student, and two explanations can swap places under a change of student architecture.
Fixing every coefficient at unity removes that degree of freedom entirely: there is no student to
tune, and no capacity for a comparison to be sensitive to. Eq. 3 has no free parameters at all
beyond a single intercept: the curves are added up exactly as an analyst reading the plots would
add them up. WhateverR2 it attains is therefore a statement about the explanation.
The second is interpretabilityof thenumber. BecauseEq. 3 isparameter-free, its deficit1−R2
has a meaning we can characterise exactly: Section 2.2 identifies it, under feature independence,
with the share of the model’s variance that no additive description could capture. No such
characterisation is available for the output of an arbitrary learner.
The fitted variants Eqs. 4 and 5 are included not as competitors but as a diagnostic: they
are the smallest possible relaxation of the unit constraint, and Section 2.2 shows that what they
gain over it is itself an interpretable quantity.
2.1.2 Attribution-valued explanations
SHAP [8] and LIME [9] do not return functions. They return, for each explained observation, a
vector ofpnumbers describing that observation only, so there is nothing to evaluate at a point
the explanation has not seen. Converting them into a predictor therefore requires one additional
modelling step, and since that step is not part of either method we apply exactly the same one
to both.
5

From attributions to curves.Letϕ j(x(i))denote the attribution that the explanation
method assigns to featurejat observationx (i), and suppose attributions have been computed
onmtraining observations. For each featurejwe treat thempairs
Sj =

x(i) j , ϕj(x(i))  	m i=1 (6)
as a scatter of attribution against feature value, and estimate from it a univariate function
ˆcj :R→R. The estimator is a quantile-binned average. Writingq j(u)for the empirical
u-quantile of featurejon the training split, we partition its range intoBbins with edges
qj(0) =e j,0 < ej,1 <· · ·< ej,B =q j(1),e j,b =q j(b/B), so that each bin holds approximately
m/Bobservations. LetI j,b ={i:e j,b−1 < x(i) j ≤e j,b}be the index set of binb. The curve is
then defined at the within-bin mean feature value by the within-bin mean attribution,
˜xj,b = 1 |Ij,b| X i∈Ij,b x(i) j ,ˆc j(˜xj,b) = 1 |Ij,b| X i∈Ij,b ϕj(x(i)),(7)
and extended to all ofRby linear interpolation between consecutive knots(˜xj,b,ˆcj(˜xj,b)), held
constant beyond the outermost knots. Bins containing fewer than a minimum count are merged
with their neighbour, and a feature taking only two values is given one knot per value. Finally
ˆcj is centred so that 1 m P i ˆcj(x(i) j ) = 0, matching the convention for PDP and ALE curves, and
the resultingˆcj are substituted into Equation (2).
Two remarks on what Equation (7) is. First, it is a conditional-mean estimator: asBgrows
withm,ˆc j(v)approachesE[ϕ j(X)|X j =v]. This matters for interpretation (a conditional
average can track structure that the marginal partial dependence curve cannot when features
are dependent), and it is why Section 3.3 reports a control in which the same estimator is applied
to the model’s own output rather than to attributions. Second, it introduces the only tuning
parameter in the attribution arm, the bin countB; we useB= 20with a minimum of ten
observations per bin throughout and note the absence of a sensitivity sweep as a limitation.
SHAP.The attribution is the Shapley value itself,ϕ j(x(i)), andS j is precisely the SHAP
dependence plot of Lundberg et al. [26]. Summing per-feature Shapley curves into an additive
model is not new (Bordt and von Luxburg [27] establish a correspondence between Shapley values
and generalized additive models), though our use is narrower, since we need only a function that
can be evaluated out of sample.
LIME.LIMEreturnsnotattributionsbutalocalsurrogate: aroundeachexplainedobservation
x(i) it fits an interpretable modelLi to perturbations of that observation, weighted by proximity.
With the usual linear choice,Li(x) =β i,0 + Pp j=1 βi,jxj, the coefficientβ i,j is a slope and not
a contribution, so it is not yet on the scale that Equation (6) expects. We convert it in the
standard way, by evaluating the contribution of featurejatx(i) relative to a reference point (we
use the training mean¯xj), giving
ϕj(x(i)) =β i,j  x(i) j −¯xj  .(8)
This is the amount by which the local model atx(i) says featurejmoves the prediction away from
its value at the reference, and it is directly comparable to a Shapley value, which is likewise a
deviationfromabaseline. SubstitutingEquation(8)intoEquation(6)andthenintoEquation(7)
yieldsˆcj exactly as for SHAP; nothing else in the pipeline differs between the two methods.
Because LIME’s local models are themselves functions, LIME also admits a construction that
does not pass through Equation (7) at all: predict at a new point by an inverse-distance weighted
average of the local models evaluated there,
ˆy(x(0)) =
Pm
i=1 δ(x(i), x(0))−1Li(x(0))Pm
i=1 δ(x(i), x(0))−1 , δ(x (i), x(0)) =∥x (i) −x (0)∥2 2.(9)
6

We report this as local-IDW alongside the additive construction. It is legitimate here precisely
becauseL i is a function; the superficially similar construction on SHAP values is not, for the
reason given in Section 2.1.3.
Equation (8) is specific to a linear local model, and it is worth being explicit about what
happens otherwise. The local-IDW construction Eq. 9 needs only thatL i be a function of
x, so it applies unchanged if the local surrogate is a shallow decision tree, a rule list, or any
other evaluable model. The additive construction is more demanding: it needs a per-feature
contributionϕ j(x(i)), which a linear model supplies through its coefficients but a tree does not,
since a tree’s output is not separable across features. For a non-additive local surrogate one would
have to extract per-feature contributions by a further decomposition (for instance the Shapley
values ofL i itself, which is cheap becauseL i is small), and the choice of that decomposition
would then become part of the construction being evaluated. We therefore restrict attention to
the linear local model, which is both the LIME default and the case in which the conversion is
unambiguous.
2.1.3 A construction to avoid
It is tempting to apply inverse-distance weighting to SHAP values in the same way we applied
it to LIME’s local models in Eq. 9. The motivation is identical: a SHAP explanation, like a
LIME explanation, is attached to particular training points, so to predict at a new point one
interpolates between the nearby ones. Concretely, one takes an inverse-distance weighted average
of the training attribution sumsSi = P j ϕj(x(i))and adds back the baseline,
ˆy(x(0)) =E[ ˆf] + X
i
wiSi, P i wi = 1.(10)
The two constructions are not, however, on the same footing, and this one is degenerate. SHAP
satisfies local accuracy exactly,Si = ˆf(x (i))−E[ ˆf], so Equation (10) collapses to
ˆy(x(0)) = X
i
wi ˆf(x (i)),(11)
which is inverse-distancekNN regression on the black box’s own predictions. The individual
attributions cancel: the predictor is invariant to how the attribution mass is distributed across
features, and would return identical values for a completely fabricated attribution matrix with
the same row sums. Worse, it fits its anchor points by tautology (at zero distance the weight
diverges), so it exhibits a large train–test gap that is an artefact of the construction and says
nothing about SHAP.
The contrast with LIME is what makes the point sharp. Eq. 9 interpolates between local
models, each of which is a function ofxcarrying per-feature slopes, so the interpolation preserves
the content of the explanation. Eq. 10 interpolates between attributionsums, and local accuracy
has already fixed every one of those sums to a number that does not depend on the attributions
at all. The construction therefore cannot see the explanation it is supposedly evaluating. We
flag this because it is the natural first thing to reach for, and because a reader encountering a
large SHAP train–test gap in the literature should ask which construction produced it.
2.2 Theory: the additive projection
Recall from Section 2.1 thatL2(PX )is the space of functions square-integrable against the joint
law of the features, thatPXj is the marginal law ofXj, and thatL2 0(PXj )is the centred subspace
ofL 2(PXj ). Define the space of square-integrableadditivefunctions
A=
n
a0 +
pX
j=1
aj(Xj) :a 0 ∈R, a j ∈L 2 0(PXj ) o ⊆L 2(PX ),(12)
7

that is, all functions expressible as a constant plus a sum of one-dimensional functions of the
individual features, each with mean zero.Acontains every surrogateg α of Equation (2), for
anyαand any centred curves, and is far larger than that finite-dimensional family: it places no
restriction on the shape of eachaj beyond square-integrability.
Let
PDj(xj) =E
 ˆf(x j, X−j)  = Z ˆf(x j, x−j) dPX−j (x−j)(13)
denote the partial dependence function of featurej(the average prediction when featurejis
held atx j and the others are drawn from theirmarginaljoint distribution), with centred version
cj(xj) = PDj(xj)−E[ ˆf(X)].
Proposition 1(Additive projection).SupposeX 1, . . . , Xp are mutually independent and ˆf∈
L2(PX ). Then the orthogonal projection ofˆfontoA, i.e. the minimiser ofE[( ˆf(X)−a(X)) 2]
overa∈ A, is
ˆfadd(x) =E[ ˆf(X)] +
pX
j=1
cj(xj),(14)
which is exactly the unit-coefficient surrogateg1 of Equation(3). Consequently
R2 add := 1− E

( ˆf(X)− ˆfadd(X)) 2
Var( ˆf(X)) (15)
is the fraction of the model’s variance that is additive. It depends only onˆfandP X, not on any
explanation method.
Proof.Under independence, marginalising overX −j coincides with conditioning:PD j(xj) =
E[ ˆf(x j, X−j)] =E[ ˆf(X)|X j =x j], sinceX −j has the same law conditionally onXj =x j as
unconditionally. Under a product measureˆfadmits the Hoeffding decomposition [12]
ˆf(X) = X
S⊆{1,...,p}
ˆfS(XS),E  ˆfS(XS)|X T  = 0wheneverS̸⊆T,(16)
whose components are mutually orthogonal inL2(PX )and whose first-order terms areˆf{j}(xj) =
E[ ˆf|X j =x j]−E[ ˆf] =c j(xj). The space defined in Eq. 12 is the direct sum of the order-≤1
components,
A=R⊕L 2 0(PX1)⊕ · · · ⊕L2 0(PXp) =R⊕
pM
j=1
L2 0(PXj ),(17)
where⊕denotes a direct sum of mutually orthogonal subspaces: everya∈ Adecomposes
uniquely into a constant plus one centred function of each feature, and functions drawn from
different summands are orthogonal inL2(PX ). The space is closed as a finite direct sum of closed
subspaces, so the projection exists and is unique. Every higher-order component is orthogonal
to it: for|S| ≥2and anyjwe haveE[ ˆfS |X j] = 0, hence⟨ ˆfS, aj⟩=E[a j(Xj)E[ ˆfS |X j]] = 0
for alla j ∈L 2 0(PXj ), and⟨ ˆfS,1⟩= 0. The projection therefore retains exactly the constant and
first-order terms,Π A ˆf=E[ ˆf] + P j cj =g 1.
WhatR 2 add means.It is worth drawing out the interpretation, because it is what makes the
quantity useful rather than merely definable. Proposition 1 says that the unit-coefficient partial-
dependence surrogate (the object one obtains by reading each PDP curve at the observed feature
value and adding the readings up) is not an approximation to the best additive summary of the
model. Itisthe best additive summary, in the mean-square sense, under independence. The
variance it fails to explain,1−R 2 add, is therefore not a deficiency of partial dependence as an
8

explanation device: it is the variance that no additive description of ˆfcould have captured,
because it lives entirely in the interaction termsˆfS,|S| ≥2.
This gives a concrete reading of what is lost when a model is explained through marginal
curves. Presenting a practitioner withpone-dimensional plots rather than the model itself costs
exactly1−R 2 add of the model’s variance, the same loss that would have been incurred by fitting
an additive model to the data in the first place and dispensing with the black box. In that
sense the choice between "explain a complex model additively” and "fit an additive model” is,
on this criterion, not a choice at all: they forgo the same information. What differs is that the
black box retains the interaction structure internally and can still use it to predict, while the
additive model cannot.R2 add is the price of the summary, and it is a property of the model being
summarised.
Corollary 1(Refitting cannot help).Under the conditions of Proposition 1, for everyα∈Rp+1,
E

( ˆf−g 1)2 ≤E  ( ˆf−g α)2 .(18)
The population-optimal coefficients areαj ≡1, uniquely so when thecj are linearly independent
and non-degenerate; a feature with no main effect (cj ≡0) leaves itsα j unidentified.
Proof.Eachg α of Equation (2) is a constant plus a sum of univariate centred functions, hence
gα ∈ A. By Proposition 1,g1 = ΠA ˆf, and the claim is the defining minimality of an orthogonal
projection over its subspace.
Corollary 1 is worth pausing on. It says that fitting coefficients to the curves (theolsvariant
of Eq. 4) cannot improve on leaving them at unity, provided features are independent. Any
improvement that ordinary least squares does deliver must therefore come from one of two
places: it is exploiting sample noise, or it is compensating for a violation of the independence
assumption. The second is the useful one, and it can be measured.
Corollary 2(Refitting gain as a dependence diagnostic).Letˆαbe the ordinary-least-squares
coefficients of Eq. 4 fitted on the training split against the targetˆf, and define the out-of-sample
refitting gain on a held-out split as
∆OLS =R 2 g ˆα  −R 2 g1  ,∆ rel OLS = R2 g ˆα  −R 2 g1  R2 g1  ,(19)
the second being the same quantity expressed as a proportion of what the parameter-free surrogate
already achieves, which is the form we report because it is comparable across settings whose overall
fidelity differs. Under the conditions of Proposition 1,∆OLS →0as the training and evaluation
samples grow. Under dependencePDj ̸=E[ ˆf|X j]in general, sog 1 need not be the projection,
the population-optimalαwithinspan{1, c 1, . . . , cp}need not be1, and∆ OLS ≥0in population
with strict inequality whenever it differs.
What makes Corollary 2 useful in practice is what it doesnotrequire. Feature dependence is
a property of the joint lawPX, and establishing it directly means estimating that law, or at least
testing for dependence amongpvariables, a problem that is hard in more than a few dimensions,
that pairwise correlations answer only partially since they miss non-linear dependence, and that
a practitioner working with a fitted model and a data sample is rarely in a position to solve.
∆OLS sidesteps it. Both terms in Eq. 19 are out-of-sampleR2 values of predictors the analyst has
already built, so the diagnostic costs one extra least-squares fit on curves that were computed
anyway, and it never touchesPX. In other words, the very condition under which the parameter-
free construction is licensed can be checked with the construction itself: fit the coefficients, see
whether the gain is bigger than the model family’s calibrated null, and if it is, treatR2 add as a
reconstruction rather than a bound.
9

Two caveats belong with the corollary rather than in a later discussion. First,∆OLS is con-
founded with anything else that mis-scales a curve: finite-sample noise in the partial dependence
estimate, grid coarseness, and most conspicuously a regularised explanation method whose coef-
ficients are attenuated. It is a dependence signal only when the curve estimator is otherwise well
calibrated. Second, the finite-sample out-of-sample∆OLS carries a negative bias, so its null is not
exactly zero and is model-dependent; it requires per-family calibration rather than assumption.
Section 3.2 tests the corollary and reports both.
Remark1 (Relation toIAS).R 2 add = 1−IASin the sense of Molnar et al. [11], modulo ALE
versus PDP main effects and in-sample versus out-of-sample evaluation. Proposition 1 supplies
the condition (independence) under which the quantity is the optimal additive approximation
and hence a genuine ceiling. When that condition fails,R 2 add is neither an upper bound nor
bounded below by zero, and we observe negative values on dependent data. This is precisely the
regime Hooker [14] introduced the generalised functional ANOVA to handle, and it is a caveat
that the in-sample, model-selection use ofIASdoes not have to confront.
2.3 Experimental design
DataThe study uses 13 tabular benchmarks from OpenML [28], selected for a high share of
continuous features, and 9 synthetic designs whose structure is known by construction. Table 1
lists the real datasets; the synthetic designs are described below and named where they are used.
The synthetic suite is generated from a single family with two free knobs, so that feature
dependence and interaction strength can be varied independently. Features are drawn from a
mean-zero, unit-variance multivariate Gaussian distribution with equicorrelated components,
X∼ Np(0,Σ ρ),(Σ ρ)jk =ρ I(j̸=k) ,(20)
whereI(Boolean)is the indicator function returning 1 if Boolean is true and 0 else. Usingρ= 0
gives mutually independent features (the condition of Proposition 1) andρ >0violates it. The
signal is built from an additive part and a pure-interaction part,
A(x) = 1.2x 1 + 0.9 sin(1.5x2) + 0.8 (x2 3 −1) + tanh(2x 4) + X
j≥5
0.6√j xj,(21)
H(x) =x 1x2 +x 3x4 + 0.8x 5x6,(22)
each standardised to zero mean and unit variance over the sample.
The point of splitting the signal this way is that atρ= 0the two parts are orthogonal, so
the interaction weight below controls the additive share exactly rather than approximately. This
is worth spelling out. Take a single product termXkXl withk̸=l, and suppose the features are
independent with mean zero. Conditioning on any one featureXj leaves at least one of the two
factors free, and that free factor is independent of everything conditioned on, so
E

XkXl |X j

=



Xk E[Xl] = 0, j=k,
E[Xk]X l = 0, j=l,
E[Xk]E[X l] = 0, j /∈ {k, l},
(23)
and henceE[H(X)|X j] = 0for everyj, andE[H(X)] = 0. Two consequences follow. First,
His orthogonal to the additive spaceAof Eq. 12: for anya=a 0 + P j aj(Xj)inA, the tower
property gives
⟨H, a⟩=a 0 E[H(X)] +
pX
j=1
E

aj(Xj)E[H(X)|X j]

= 0.(24)
Second,Hcontributes nothing to any partial dependence function, since under independence
PDj is the conditional mean andE[H(X)|X j =x j] = 0. So the whole ofHlives in the part of
10

the model that no additive explanation can reach, which is precisely the property the interaction
sweep needs in order to be a controlled experiment. Note that Eq. 23 uses independence twice;
atρ >0neither conclusion survives, which is why only theρ= 0designs validate the estimator.
The two parts are combined with an interaction weightτ∈[0,1],
fτ,ρ(x) =κ
√
1−τ A(x) + √τ H(x)  ,(25)
withκfixed so thatsd(f τ,ρ) = 2.5. BecauseAandHare orthogonal atρ= 0, the additive share
of the signal variance is then1−τby construction. Targets arey|x∼Bernoulli

logit−1fτ,ρ(x) 
for classification andy=f τ,ρ(x) +εwithε∼ N(0,(0.3 sd(f)) 2)for regression.
The suite then consists of: aninteraction sweepτ∈ {0,0.10,0.25,0.50,0.75}atρ= 0, giving
designed additive shares from1.00down to0.255with independent features; acorrelation sweep
ρ∈ {0.30,0.60,0.85}at fixedτ= 0.20; and a regression variant. All usen= 2000andp= 8.
Feature encoding matters more than it appears. On a two-valued column a curve is anaffine
function of that column, so the explanation transform is a no-op and a linear model on the raw
dummy spans the same space. A design dominated by binary columns thereforecannotdiscrim-
inate between curve-based explanation methods, whatever their relative merits. We accordingly
exclude any dataset whose encoded design is more than 60% binary, which removescredit_g
from the real data and the binary-dominated synthetic design from the suite; including them
would have diluted every comparison with cells that are uninformative by construction. For the
datasets that remain we report the binary fraction, drop reference levels when one-hot encoding
so that the design matrix is full rank, and never discretise continuous features.
Table 1: The real datasets used in the study.nis the number of rows,p raw the number of
variables before encoding,pthe width of the one-hot encoded design matrix, andBin. frac.the
share of encoded columns taking at most two values.Taskis clf for classification and reg for
regression, andPos. ratethe marginal rate of the positive class, shown as a dash for regression.
Datasetn p raw pBin. frac. Task Pos. rate
abalone 4177 8 9 0.22 reg –
boston_housing 506 13 20 0.45 reg –
breast_cancer_wisc 699 9 9 0.00 clf 0.345
concrete 1030 8 8 0.00 reg –
cpu_activity 8192 21 21 0.00 reg –
diabetes_pima 768 8 8 0.00 clf 0.349
heart_statlog 270 13 13 0.23 clf 0.444
phoneme 5404 5 5 0.00 clf 0.293
qsar_biodeg 1055 41 41 0.07 clf 0.337
spambase 4601 57 57 0.00 clf 0.394
wind_speed 6574 14 14 0.00 reg –
wine_quality_red 1599 11 11 0.00 clf 0.136
wine_quality_white 4898 11 11 0.00 clf 0.216
Models and protocol.Four black-box families, namely Random Forest, Gradient Boosting,
Multilayer Perceptron (MLP), Radial Basis Function Support Vector Machine (SVM RBF), each
tuned by randomised search with 5-fold cross-validation within every repeat, and 20 repeated
stratified train/test splits (75%/25%). This gives25×4×20 = 2000evaluation cells and 6.31
million recorded metric values, with no failed fits. Classification is explained on the probability
scale, and motivation in Section 4.
Controls.A new metric must be shown to measure something. We include:null explanations,
a gradedcorruption sweep, andbaselines. Stated precisely, let a curvec j be represented by
11

its valuesv j,1, . . . , vj,Kj at knotsu j,1 <· · ·< uj,Kj, and writes j = sd(v j,1, . . . , vj,Kj )for its
amplitude. The three curve manipulations are
permuted:v perm j,k =v j,πj (k), π j a uniform random permutation of{1, . . . , Kj},(26)
randomised:v rand j,k =η j,k −¯ηj, η j,k ∼ N(0, s2 j ),(27)
corrupted atσ:v σ j,k =v j,k +ζ j,k, ζ j,k ∼ N(0, σ2s2 j ).(28)
Equation (26) is the sharp null: it leaves the multiset of effect magnitudes exactly unchanged
and destroys only the mapping from feature value to effect, so a metric that does not collapse
under it is not reading the curve’s shape. Equation (27) additionally discards the magnitudes.
Equation (28) interpolates between the intact curve and noise, withσ∈ {0,0.1,0.25,0.5,1,2,4}
in units of each curve’s own amplitude, so that features with large and small effects are corrupted
comparably. Baselines span an intercept-only floor (g≡ ¯t), ordinary least squares on the raw
encoded features, a spline additive model fitted directly to the target, and the black box itself.
Statistics.The unit of replication is thedataset. Repeats within a dataset share most of their
training rows and the four model families share the data entirely, so treating individual cells as
independent would be pseudoreplication; every reported test therefore averages to one value per
dataset and is paired over those. For a replicated synthetic design the unit is thedesign, its 10
independent draws being averaged into it first, so that one generative family does not cast 10
timesthevotesofarealdataset. Holmcorrection[29]isappliedoverthesixpairwisecomparisons,
which are the confirmatory family; everything else (the controls, the estimator comparison, the
correlations against established metrics) is exploratory and reported uncorrected. Intervals in
the pooled tables are 95%tintervals over repeats and describe split-to-split variation only; the
between-dataset variation that the paired tests use is substantially larger.
Smoothing parameters.PDP uses a 25-point quantile grid over a 300-row background; ALE
uses 20 quantile intervals; the SHAP and LIME dependence curves use 20 quantile bins with a
10-row minimum. LIME is run at library defaults withdiscretize_continuous=False, 1000
perturbations and 300 anchor points; TreeSHAP is runinterventional(see Section 3.3). We
have not swept these; a sensitivity analysis over the bin count is the most obvious omission.
3 Results
Six experiments follow, in an order that builds on itself, and they fall into three groups.
The first three ask whether the proposed metric can be trusted at all, and must come be-
fore any comparison rests on it. Section 3.1 checks that the metric responds to the content of
an explanation, since a metric that survives having its input destroyed cannot rank anything.
Section 3.2 checks the prediction the theory makes about refitting. Section 3.3 checks that a
difference between two explanation methods is a difference between the explanations themselves,
rather than between the machinery used to turn them into predictors.
Section 3.4 then uses the metric for the comparison the paper set out to make, between PDP,
ALE, SHAP and LIME.
The last two turn outward, to the other metrics in the literature. Section 3.5 asks how ours
relates to five established ones, and Section 3.6 asks whether it detects a degraded explanation
any better than they do.
Unless a subsection says otherwise, results are computed on the 13 real datasets only. The
one exception is Section 3.2, which needs a known feature correlation and therefore uses the
synthetic designs; it says so explicitly.
12

3.1 The metric responds to explanation content
It is important to establish, before any comparison between explanation methods, that the
metric is reading the explanation at all. A predictor built from an explanation could score well
for reasons that have nothing to do with the explanation’s content: the feature values alone carry
information, and a construction that leaked any of it would produce respectable numbers from
an explanation that had been reduced to noise. Any such leak would invalidate every comparison
that follows.
We therefore replace each explanation with a null version and rescore it. Two nulls are used,
defined in Section 2.3: the permuted null of Eq. 26 shuffles each curve’s values across its grid,
which leaves every effect magnitude intact and destroys only the mapping from feature value to
effect; the randomised null of Eq. 27 replaces each curve with amplitude-matched noise. We also
add noise to the intact curves in increasing amounts, in units of each curve’s own amplitude, so
that the degradation is graded rather than all-or-nothing. Every number in this subsection uses
the parameter-free surrogateg 1 of Eq. 3, scored byR2 on the held-out split against the black
box’s predictions; the fitted variants are excluded here because rescaling the curves could partly
repair a damaged explanation and blunt the collapse we are trying to expose.
Table 2: TestR 2 against the black box under the unit-coefficient constructiong 1 of Eq. 3,
averagedoverdatasetsandmodelfamilies.Intactistheunmodifiedexplanation,Values permuted
the null of Eq. 26, andRandomisedthe null of Eq. 27.Collapseis the difference between the
intact and permuted columns. Parenthesised ranges are 95% intervals.
Method Intact Values permuted Randomised Collapse
PDP 0.702 (0.695, 0.709) -0.654 (-0.678, -0.630) -0.617 (-0.636, -0.597) 1.357
ALE 0.713 (0.706, 0.720) -0.741 (-0.756, -0.726) -0.693 (-0.720, -0.667) 1.454
SHAP 0.798 (0.794, 0.802) -0.416 (-0.434, -0.399) -0.380 (-0.396, -0.365) 1.215
LIME 0.540 (0.535, 0.544) -0.218 (-0.232, -0.204) -0.196 (-0.207, -0.184) 0.758
0.0 0.5 1.0 1.5 2.0 2.5 3.0 3.5 4.0
noise added to explanation (multiples of curve amplitude)
−10
−8
−6
−4
−2
0
test R2 against the black box
PDP
ALE
SHAP
LIME
Figure 1: TestR 2 against the black box as Gaussian noise of increasing standard deviation is
added to each explanation’s curves, in units of that curve’s own amplitude. Bands are 95%
intervals over repeated splits.
Table 2 shows the intact and null scores for each method, and Figure 1 shows the graded
version. The collapse is complete: PDP falls from0.702to−0.654and SHAP from0.798
to−0.416. Negative values are worse than predicting the model’s average output, so a null
13

explanation is not merely uninformative but actively misleading about the model. Figure 1
shows the same thing without a cliff edge: fidelity falls monotonically with added noise for all
four methods, crossing zero between one and two curve amplitudes.
The metric therefore passes the test it had to pass. Nothing in the construction lets an
explanation score well without carrying information about how feature values map to model
output, which is the property every comparison in the rest of this section relies on.
Two further readings of Table 2 are worth taking while it is in front of us. TheIntact
column already orders the methods SHAP (best explanations)>ALE>PDP>LIME (poorest
explanations), which Section 3.4 confirms with paired tests. And thesizeof the collapse differs
sharply: LIME falls by0.758where ALE falls by1.454. That is a fact about scale rather than
about information. LIME’s local models are ridge-regularised, so its coefficients are attenuated
and its curves have small amplitude; the nulls preserve amplitude by construction, and summing
near-flat wrong curves approximates predicting the mean, which scores near zero rather than far
below it. The collapse is thus confounded with how boldly a method states its case, which is
why we report the intact value and the collapse separately rather than combining them.
3.2 Testing the refitting-gain prediction
Corollary 1 makes a prediction that can be checked: when features are independent, fitting
coefficients to the curves cannot improve on leaving them at unity, and Corollary 2 adds that
any gain which does appear is a signal of feature dependence. It is important to test this, for two
reasons. The prediction is what licenses the parameter-free construction used throughout the
paper, so if refitting turned out to help substantially under independence the construction would
be poorly chosen. And if the gain does track dependence, it delivers the practical diagnostic
argued for in Section 2.2: a check on the independence condition that costs one extra least-
squares fit and never requires estimating the feature distribution.
Testing it requires knowing the true feature correlation, which real data cannot supply. We
therefore use the synthetic suite, where interaction strengthτand feature correlationρare set
independently by construction. Each design is drawn 10 times from independent seeds and the
draws are averaged, so that a difference between designs reflects the design rather than the
particular sample each happened to receive. We report the relative gain∆rel OLS of Eq. 19, because
the designs differ in overall fidelity and the same absolute gap means different things on different
rows.
Table 3: Relative refitting gain for PDP,(R2(g ˆα)−R 2(g1))/R2(g1)of Eq. 19, in per cent. Rows
are the synthetic designs, those with independent features (ρ= 0) above the rule and those with
correlated features below;ρis the designed feature correlation of Eq. 20. Columns are the four
model families. Each entry averages the independent draws of that design.
DesignρGradient Boosting MLP Random Forest SVM RBF
syn_inter00 0.00 +0.1 +0.0 -1.9 -0.0
syn_inter10 0.00 +0.2 +0.1 -1.5 +0.1
syn_inter25 0.00 +0.3 +0.0 -2.0 +0.0
syn_inter50 0.00 +0.2 -0.3 -2.2 -0.4
syn_inter75 0.00 -0.1 +0.3 -4.1 -0.3
syn_corr30 0.30 +1.4 +2.4 +0.9 +2.0
syn_corr60 0.60 +4.8 +18.0 +4.1 +7.2
syn_corr85 0.85 +7.1 +59.0 +3.9 +38.0
syn_regress 0.20 +1.8 +1.4 +1.1 +1.2
Table 3 shows the relative gain for PDP on each design. In the independent block it is within
±0.4%of zero for Gradient Boosting, the MLP and the SVM RBF at every interaction strength.
14

In the correlated block it grows withρ: roughly1%–2%atρ= 0.30,4%–18%atρ= 0.60, and
4%–59%atρ= 0.85. Random Forest is offset downwards throughout the independent block,
sitting at−1.5%to−4.1%where the other three sit at zero.
Both halves of the prediction hold. Refitting buys nothing under independence, whatever
the interaction strength, which is what Corollary 1 requires and what justifies usingg1 as the
paper’s metric. And the gain rises with feature correlation, confirming Corollary 2’s claim that
it carries information about dependence.
Two limits on its use follow from the same table. The random forest’s negative offset under
independence means the null is model-dependent, so a value must be calibrated per model family
before it can be called positive, exactly the caveat attached to Corollary 2. And the spread across
families at high correlation is wide: atρ= 0.85the MLP gains59%and Random Forest3.9%
from the same data. The gain detects dependence; it does not measure it on a scale comparable
across models.
Why the tree ensembles gain so much less.The split atρ= 0.85is between the two tree
ensembles, which gain7.1%and3.9%, and the two smooth models, which gain59%and38%. It
is not an artefact of the relative scale: the absolute gains differ in the same direction and by a
similar factor,0.062and0.035for Gradient Boosting and Random Forest against0.272and0.175
for the MLP and the SVM RBF. What drives it is how much the parameter-free surrogate had
already achieved. Atρ= 0.85the unit surrogate reproduces the tree ensembles well (R2 = 0.885
and0.905) and the smooth models poorly (0.541and0.623), so there is far more for refitting to
recover in the smooth case, and refitting duly recovers it, bringing all four to between0.80and
0.95.
We offer the following explanation, and flag that we have not tested it directly. A partial
dependence function averages ˆfover themarginaldistribution of the remaining features, so at
ρ= 0.85it evaluates the model at feature combinations that the joint distribution almost never
produces. How badly the resulting curve is distorted therefore depends on how the model behaves
away from the data. A tree ensemble is piecewise constant on axis-aligned cells and its predictions
off the data manifold are bounded by the leaf values it learned on it, so its partial dependence
curves stay close to the right scale. An RBF support vector machine and a multilayer perceptron
are smooth global functions that extrapolate, and off-manifold they can return systematically
inflated or deflated values, which distorts the amplitude of their curves. A single coefficient per
feature is exactly the correction such a distortion needs, which is why refitting buys them so
much. Testing this would require comparing on-manifold and off-manifold partial dependence
estimates directly, which we did not do.
For the parameter-free surrogate the practical reading is favourable. At the correlations
typical of real tabular data the cost of fixing the coefficients at unity is1%–2%ofR 2, sog 1
remains a reliable instrument even though the independence condition that formally licenses it
does not hold. Only at extreme correlation does that change, and there it changes sharply for
the smoother models.
3.3 Is it the explanation or the aggregator?
Comparing SHAP and LIME against PDP and ALE through a shared construction is only fair if
the construction itself is not doing the work. There are two specific concerns. First, SHAP and
LIME receive an estimation step that PDP and ALE do not: their per-observation attributions
must be smoothed into curves by the binning of Eq. 7, and that step is a conditional average.
A conditional average can trackE[ˆf|X j]under feature dependence in a way a marginal partial
dependence curve provably cannot, so it could hand SHAP and LIME an advantage that has
nothing to do with their attributions. Second, SHAP’s tree estimator has a marginal and a
conditional variant, the choice between them is usually left at a library default, and the two
estimate different quantities, so a SHAP result could be an artefact of that default.
15

We address the first concern with a control that removes the explanation entirely: the black
box’s own predictions are passed through the identical binning, giving curvesˆcj(xj)≈ bE[ ˆf|
Xj =x j]with no attribution anywhere in the pipeline. If the aggregator were doing the work,
this control would match the explanation-derived predictors. For the second we compute both
TreeSHAP variants separately on the two tree families where both are defined. All results here
are on the real datasets and use the refitted constructiongˆαof Eq. 4; refitting is used because
the control sumspconditional means that each carry the whole marginal signal, and under unit
coefficients it would over-count by roughly a factor ofp, producing a scaling artefact rather than
an informative comparison.
Table 4: TestR2 against the black box under the refitted constructiongˆαof Eq. 4, averaged over
the real datasets. Rows are curve sources, columns model families.SHAP, conditional TreeSHAP
replaces the marginalinterventionalestimator withtree_path_dependentand is defined only
on the two tree families.E[f|x j], binnedapplies the binning of Eq. 7 to the black box’s own
predictions, with no explanation in the pipeline. Dashes mark undefined combinations.
Curve source Gradient Boosting MLP Random Forest SVM RBF
PDP 0.799 0.816 0.848 0.756
ALE 0.801 0.816 0.848 0.759
SHAP 0.814 0.837 0.857 0.784
SHAP, conditional TreeSHAP 0.813 – 0.859 –
E[f | x_j], binned (no explanation) 0.769 0.788 0.824 0.745
Table 4 shows every curve source against every model family. The control is the last row. It
is beaten by all three curve sources on all four model families, reaching0.781on average against
0.805for PDP,0.806for ALE and0.823for SHAP; each of the three beats it at the dataset
level (PDPp= 0.0113, ALEp= 0.0817, SHAPp= 0.0013). The two TreeSHAP variants sit
on top of each other: tested over the two tree families the difference is0.0004under the unit
construction (p= 0.92) and0.0003under refitting (p= 0.78).
Neither concern survives. The shared aggregator does not reproduce the explanations (ap-
plied on its own it loses to every one of them), so the comparison in the next subsection is
between explanations and not between smoothers. And the estimator choice does not account
for the SHAP result, since the marginal and conditional variants are indistinguishable on this
benchmark. The advantage lies in the attributions.
3.4 Comparing the reliability of the four explanation methods
With the construction validated and the aggregator ruled out, the comparisons in the rest of the
paper can be read directly. Two questions matter to a practitioner: which explanation method
carries most of the model, and how much of the model any of them carries relative to using no
explanation at all. The second matters because a ranking is only useful if the quantities being
ranked are worth having.
We score all four methods on the real datasets under the three constructions of Eqs. 3–5, test
the six pairwise differences with the dataset as the unit of replication and Holm correction over
the family, and place the results against four reference points scored on the original outcome: an
intercept-only floor, a linear model on the raw features, an additive spline model fitted directly
toy, and the average of the four black-box models (Gradient Boosting, MLP, Random Forest
and SVM RBF).
Table 5 shows the testR2 of each method and construction, and Table 6 shows the paired
differences. SHAP is first and LIME last: SHAP leads PDP by0.096and ALE by0.085, and
every method leads LIME. PDP and ALE are not separated, differing by only0.011.
Thatlastresultisworthstatingpositivelyratherthanasafailuretoreject. ALEwasdesigned
16

Table 5: TestR2 of each explanation-derived predictor against the black box’s own predictions.
Rows are the constructions of Eqs. 3–5 —g 1,g ˆαandg ˆαλ — plus LIME’s native local-IDW
variant; columns are the explanation methods. Entries are testR2, averaged over datasets and
over the four model families, with the half-width of a 95%tinterval. A dash marks a construction
a method does not have.
Construction PDP ALE SHAP LIME
additive, unit 0.702±0.007 0.713±0.007 0.798±0.004 0.540±0.005
additive, ols 0.805±0.005 0.806±0.005 0.823±0.005 0.762±0.005
additive, ridge 0.806±0.005 0.806±0.005 0.824±0.005 0.762±0.005
local-IDW – – – 0.463±0.034
Table 6: Paired differences in testR2 against the black box between explanation methods, under
theunit-coefficientconstructiong 1 ofEq.3. Theentryinrowa, columnbis∆R 2 =R 2(a)−R2(b),
followed in parentheses by the Holm-correctedp-value of a pairedt-test over datasets. A positive
entry favours the row method. The unit of replication is the dataset (n= 13): differences are
averaged to one value per dataset before testing. Holm correction is over the 6 comparisons. The
lower triangle is left empty because it carries the same numbers with the sign reversed.
PDP ALE SHAP LIME
PDP – -0.011 (0.781) -0.096 (0.019) +0.163 (0.019)
ALE – – -0.085 (0.019) +0.173 (1e-05)
SHAP – – – +0.258 (4e-05)
LIME – – – –
to behave better than PDP under feature dependence, and these are dependent real datasets,
yet on this criterion and at this sample size the two cannot be told apart.
One explanation is that the two properties pull in opposite directions and roughly cancel.
ALE’s advantage over PDP is confined to dependence: it accumulates local effects computed
within narrow intervals of the feature, so it never evaluates the model at the off-manifold com-
binations that distort a partial dependence curve. But that same construction is awkward when
the model contains interactions, since the local effect ofxj then depends on where the other
features happen to sit within each interval, and accumulating those effects into a single curve
has no clean interpretation, a limitation Apley and Zhu [7] are explicit about. Real tabular data
supplies both dependence and interaction at once, so ALE gains on one axis and loses on the
other. That would produce exactly what we observe: a difference close to zero, rather than the
ALE advantage the dependence argument alone would predict. We put this forward as a reading
consistent with the data rather than as something these experiments isolate, since separating
the two effects would need designs that vary dependence and interaction independently and then
measure ALE against PDP on each; our synthetic suite varies them independently but was not
analysed for this contrast. Table 5 also shows why LIME’s position depends on which construc-
tion is read: its unit and refitted scores differ by more than0.2, where SHAP’s differ by0.025.
LIME’s information is present but mis-scaled, because its ridge-regularised local coefficients are
attenuated; reporting either construction alone would misrepresent it in one direction or the
other.
Table 7 places these numbers on the outcome axis, and three things follow from it. First, the
ordering of the explanation methods is the same one Section 3.1 found against the black box:
SHAP is best and LIME worst, with PDP and ALE between them. That the ranking survives a
change of target (from reproducing the model to recovering the outcome) is worth noting, since
the two are different questions and need not have agreed.
Second, the explanation-derived predictors come close to the black box itself. SHAP’s unit
17

Table 7: Predictors scored against the original targety(test ROC-AUC), averaged over datasets
and over the four model families, with a 95% interval. Rows are ordered best to worst. Expla-
nation rows use the unit-coefficient constructiong1 of Eq. 3;Additive spline modelandLinear
on raw featuresare fitted directly toywith no explanation involved.
Predictor Score
Black box 0.917 (0.913, 0.921)
Additive spline model (fitted toy) 0.900 (0.896, 0.904)
SHAP (additive, unit) 0.895 (0.890, 0.899)
PDP (additive, unit) 0.890 (0.885, 0.894)
Linear on raw features 0.883 (0.880, 0.887)
ALE (additive, unit) 0.870 (0.866, 0.875)
LIME (additive, unit) 0.845 (0.841, 0.849)
Intercept only 0.500 (0.500, 0.500)
surrogate reaches0.895against0.917for the average of the four black-box models, so a predictor
built from nothing but an explanation recovers most of what the model achieves. Note where
the linear baseline falls: at0.883it is not below all four explanations but among them, above
ALE and LIME and below SHAP and PDP. The floor against which the explanations should be
read is therefore the intercept-only row at0.500; the linear model is better understood as a fifth
competitor than as a baseline.
Third, and most informative, the explanations are essentially level with the additive spline
model at0.900, a model fitted directly toywith no explanation involved, and the best any
additive function of the features can do here. The explanation curves therefore capture very
nearly all of the marginal information available. This is what Proposition 1 leads one to expect:
the curves span the additive space, so a predictor built from them should reach the additive
optimum and stop there. The remaining gap to the black box is the interaction structure, which
no additive explanation can convey.
The practical conclusion is therefore narrower than the ranking alone suggests. The ordering
is real and reliably measured, but on the axis a practitioner cares about (recovering the outcome),
the four methods differ little, and none of them approaches the black box. The value of the metric
is in auditing how much of a model an explanation conveys, not in choosing an explanation
method to deploy as a predictor.
The ranking is a dependence phenomenon.The ordering above is not a general property
of the methods, and the synthetic suite shows why. Where features are independent by con-
struction, Proposition 1 says the partial dependence surrogate is already the optimal additive
approximation, so nothing should beat it. That is what happens: on the 5 independent-feature
designs SHAP isworsethan PDP (−0.005, winning on0/5designs,p= 0.005) and indistin-
guishable from ALE. An attribution-based estimate of an object PDP already computes exactly
can only add noise. On the 13 real datasets, where features are dependent and the projection
property lapses, SHAP leads PDP by0.096(12/13,p= 0.005). Both figures come from the same
per-cell results that Tables 5 and 6 summarise, split by whether the dataset’s features are inde-
pendent by construction rather than pooled; the real-data figure is the split that Table 6 reports,
and the independent-feature figure uses the synthetic designs that the rest of this section sets
aside. So the ranking is what happens once the condition that makes PDP optimal is violated,
which on real tabular data it almost always is.
3.5 Relation to established metrics
A new evaluation metric has to answer what it adds. If it merely reproduces the ranking of
an existing metric then it is a reformulation, however differently motivated, and a practitioner
18

already computing that metric gains nothing by adopting it.
We therefore compute five established explanation metrics (infidelity [16], faithfulness corre-
lation [17], max-sensitivity [16], complexity [17] and sparseness [19]) on the same explanations,
the same models and the same splits as our own, and correlate the rankings. Each has free pa-
rameters, and a rank correlation is only meaningful if they are stated: infidelity uses50Gaussian
perturbations at scale0.2standard deviations; faithfulness correlation uses50random subsets
covering30%of the features, replaced by the training mean; max-sensitivity uses20perturba-
tions at radius0.1standard deviations; complexity and sparseness have no parameters beyond
the attribution matrix. All five are evaluated on the same200held-out points. We took these
values from the defaults in the originating papers and did not tune them.
Table 8: Spearman rank correlations between the proposed metric (testR2 against the black box,
unit-coefficient construction) and five established metrics computed on the same explanations
and splits, one row per established metric.Pooledρranks over all (dataset, model, method,
split) cells at once, with itsp-value alongside.Within-cellρranks the four explanation methods
against each other inside a single (dataset, model, split) cell and averages over the 1040 such
cells, with a 95% interval.
Established metric Pooledρ pWithin-cellρ
infidelity 0.120 7.9e-15 0.433 (0.403, 0.463)
faithfulness corr 0.628 0.0e+00 0.452 (0.422, 0.481)
max sensitivity -0.237 2.5e-54 0.035 (-0.001, 0.071)
complexity -0.090 6.4e-09 0.003 (-0.033, 0.038)
sparseness 0.190 3.2e-35 0.012 (-0.024, 0.047)
Table 8 shows the correlations two ways. Pooled across cells, the metric is close to orthogonal
to infidelity (ρ= 0.120), complexity (−0.090) and sparseness (0.190), and correlated with faith-
fulness correlation (0.628) and weakly with max-sensitivity (−0.237). Within a (dataset, model,
split) cell, the comparison in which a choice between explanation methods is actually taken,
the picture changes: faithfulness correlation0.452, but also infidelity0.433. Sparseness remains
indistinguishable from zero, and so does complexity (0.003, with an interval of(−0.033,0.038)
that includes zero).
Thehonestsummaryisthatthemetricbelongstothefaithfulness familyratherthanrestating
any single member of it. It is best understood as a global, out-of-sample, construction-based
relative of faithfulness correlation, and its value does not rest on being orthogonal to it. What
it adds is the decomposition: a fidelity number paired withR2 add separates "this explanation is
poor” from "this model is not additive, so no additive explanation could have done better”, a
distinction no single faithfulness score makes.
Metric versus mechanism.A low correlation could arise from either of two sources and this
design does not separate them. One is thescoring function: ours is anR2 against the black box,
theirs are perturbation-based quantities on other scales. The other is theevaluation mechanism:
ours is the only one that builds a predictor from the explanation and tests it out of sample,
whereas the other five interrogate the attribution matrix in place. We hold the reference metrics
at the mechanism their authors specify and do not compute, say, an infidelity of our surrogate,
so the comparison is between the metrics as they are used rather than a factorial decomposition.
Our reading is that the mechanism is the larger part of the difference (an out-of-sample predictive
test can fail in ways an in-place perturbation test cannot see, which is what the next subsection
exploits), but the present experiment does not isolate it.
19

3.6 Is the proposed metric better?
The previous subsection established that the metric is not a restatement of an existing one.
That is a claim about difference, and it leaves the harder question open: is itbetter? This is
the question a practitioner choosing a metric actually faces, and it is rarely asked of explanation
metrics, which are usually justified by the reasonableness of their definition rather than tested
against a known answer.
It can be asked, because any evaluation metric asserts an ordering: given two explanations of
the same model, it says which is better. That assertion is testable whenever we can manufacture
pairs whose true ordering is known. We build such pairs by degrading an explanation by a
controlled amount, giving a ladder of progressively worse versions,
E≻E σ=0.5 ≻E σ=1 ≻E σ=2 ≻E perm,(29)
whereE σ adds Gaussian noise of standard deviationσtimes each curve’s own amplitude (Eq. 28)
andE perm is the permuted null of Eq. 26. The ordering is fixed by construction: each rung is the
previous explanation plus strictly more noise. For every (dataset, model, split, method) on the
real data we compute all six evaluation metrics at every rung and record whether each ranked the
intact explanation above the degraded one, reading each metric in the direction its own authors
specify. Aggregating with the dataset as the unit gives a probability of correct ranking, for which
0.5is chance.
Difficulty comes from degrading the explanation rather than from noising the data. Noising
the data would change what the true explanation is, so the ground-truth ordering the comparison
rests on would itself become an estimate, and a metric could be penalised for correctly tracking
an ordering we had mis-specified. Degrading the explanation leaves the ground truth exact, and
the intermediate rungs supply difficulty by sitting close to the intact explanation.
Table 9: One row per evaluation metric. Columns are the rungs of the degradation ladder of
Eq. 29:σis Gaussian noise added to the explanation’s curves in units of each curve’s own
amplitude, andpermutedis the null of Eq. 26. Each entry is the fraction of (model, split,
explanation method) cells in which the metric ranked the intact explanation above that rung,
averaged over the 13 datasets;Meanaverages across rungs. Each metric is read in the direction
its originating paper specifies, so that a larger entry always means better agreement with the
known ordering. Rows are ordered byMean, best first.
Evaluation metricσ= 0.5σ= 1σ= 2permuted Mean
Faithfulness correlation 0.940 0.987 0.994 0.998 0.980
Proposed (R2 vs. ˆf) 0.932 0.962 0.981 0.995 0.967
Max-sensitivity 0.957 0.959 0.961 0.956 0.958
Infidelity 0.757 0.887 0.962 0.347 0.738
Sparseness 0.368 0.361 0.364 0.291 0.346
Complexity 0.341 0.333 0.338 0.283 0.324
Table 9 shows the accuracy of each metric at each rung. Three patterns stand out, and they
are of different kinds. Faithfulness correlation ranks the ladder correctly 0.980 of the time against
0.967foroursand0.958formax-sensitivity. Takingthedatasetastheunit, thedifferencebetween
ours and faithfulness correlation is−0.012(p= 0.371, ours ahead on3/13of 13 datasets): the
two cannot be separated on this evidence.
Infidelity is defeated by the sharp null. It handles noise well, rising from0.757atσ= 0.5
to0.962atσ= 2, but against the permuted explanation it scores 0.347, far below chance: it
prefers the permuted version. Permutation preserves the multiset of curve values exactly and
only reassigns them to different feature values, so attribution magnitudes survive intact, and
infidelity’s local perturbation test is largely a test of magnitude.
20

Complexity and sparseness are inverted. Both score below chance at every rung, averaging
0.324 and 0.346, meaning they systematically prefer the degraded explanation. Neither is a
faithfulness metric: both quantify howconcentratedan attribution vector is, and concentration
is a property an explanation can have while being entirely wrong. Adding noise to a curve tends
to inflate whichever feature the noise happened to favour, which concentrates the attributions
and improves both scores.
Returning to the question the subsection opened with: our metric is not better than the best
established alternative, and we do not claim it is. What it is, is a member of the group that
works: it detects a degraded explanation as reliably as faithfulness correlation does, and the case
for the framework rests on the decomposition of Section 3.5 rather than on this comparison. The
more consequential finding concerns the others. Of the five established metrics tested, two track
the ordering reliably, one fails on the single most important case, and two point the wrong way.
Benchmark suites that report complexity and sparseness alongside faithfulness metrics invite the
reading that a better score means a better explanation, and on this evidence that reading is
reversed.
What this experiment can and cannot settle.The ladder degradescurves, and three of
the six metrics are computed from attributions derived from those curves, so there is a structural
affinity between the test and part of what is being tested; a ladder built by corrupting attri-
butions before they are smoothed might order the metrics differently. Where the experiment
is unambiguous is in the negative direction: a metric that ranks a permuted explanation above
an intact one is not measuring faithfulness, whatever else it may be measuring, and no affinity
argument rescues it.
4 Discussion
Whether the black box was warranted at all.Rudin [30] argues that for high-stakes
decisions one should use an inherently interpretable model rather than explain an opaque one.
Our results speak to that claim without settling it, and they lean the other way.
Two facts from Table 7 matter. The black box is the most accurate predictor in the study,
reaching AUC0.917against0.900for the spline GAM fitted directly toy, so the interpretable
model does carry a real accuracy cost here. And the explanation-derived predictors come within
a hair of the GAM (SHAP’s reaches0.895), so the explanations convey very nearly as much
of the task as the interpretable model does in total. On this evidence the combination of an
accurate black box with model-agnostic explanations performs well: one keeps the accuracy and
gives up little of what the interpretable model would have shown.
The obvious rejoinder is that an explanation is only worth what it faithfully reports, and a
predictor built from an unfaithful explanation could score well for the wrong reasons. This is
where the theory does some work. Proposition 1 establishes that under feature independence the
partial dependence surrogateisthe optimal additive summary of the model, so there is a regime
in which these explanations are provably as good as any additive description could be. Outside
it, Corollary 2 identifies the sole source of degradation as feature dependence, and Section 3.2
shows the resulting cost is1%–2%ofR 2 at the correlations typical of tabular data. So the
reliability of the explanations is not merely assumed: it is bounded by a stated condition and
the departure from it is measurable.
None of this settles the debate, which turns on considerations (auditability, recourse, con-
testability) that a fidelity number does not reach. What our framework contributes is a way
to make one side of it quantitative: the cost of using a black box plus explanations, rather
than an interpretable model, can now be read off as the gap between the black box and the
explanation-derived predictor, and on these datasets that gap is small.
21

What the metric does not capture.An explanation can be informative without being com-
prehensible, and our construction is blind to the difference. A method that scattered predictive
content across forty features would score well here and be useless to a practitioner. The metric
belongs alongside complexity and robustness criteria, not in place of them; its weak association
with the complexity family (Section 3.5) suggests it measures a largely different axis, not that
the other axis is unimportant.
The additive form is a choice, and so is the one-dimensional curve.Both curve-based
methods and our SHAP/LIME conversions produce additive surrogates, so the framework cannot
reward an explanation for conveying interaction structure. This is a deliberate restriction (a more
flexible surrogate would measure the surrogate’s capacity rather than the explanation’s content),
but it bounds what the comparison can say.
The restriction has two layers, and they are worth separating. The first is thesumma-
tion: we add the per-feature curves rather than combining them in some richer way. The
second is theinput: we take one-dimensional curves, although PDP and ALE are defined for
feature subsets of any size and two-dimensional versions are routinely used to inspect pair-
wise interactions. Admitting second-order curves would raise the ceiling, since a surrogate
a0 + P j aj(xj) + P j<k ajk (xj, xk)can reach the order-two Hoeffding components thatAof
Eq. 12 cannot, and Proposition 1 generalises to that space unchanged. What does not generalise
cheaply is the parameter-free property: the number of second-order terms grows asp2, most of
them are near zero, and estimating which to keep reintroduces exactly the fitting step whose
absence makes the present metric attributable. Extending the framework in this direction while
keeping it parameter-free is open, and is the most obvious next step.
Output scale.Classification is explained on the probability scale. Log-odds is arguably more
principled, since additivity is a property of the score, but it is not safe by default: a tree ensemble
grows pure leaves and emits probabilities of exactly0and1, so the required clip becomes the
dominant determinant of the score’s variance. With 60% of predictions saturated on one dataset
we measuredR 2 add =−2.11, an artefact entirely of the clip. Setting the clip from the ensemble’s
own resolution (1/2TforTtrees) removes most but not all of the damage. Practitioners running
this framework on log-odds should report the saturated fraction.
Library behaviour.Two implementation details silently invert results and are worth record-
ing. In regression mode the reference LIME implementation stores its fitted coefficients under
one label key and asign-negateddisplay copy under another. Reading the first key (the obvi-
ous choice) inverts every local model, which turns a positive fidelity into a negative one: the
surrogate then predicts the black box’s deviations backwards, so it scores worse than predicting
the mean. We caught this during development and it is now guarded by a unit test that fits
LIME to a black box known to be monotone increasing in one feature and asserts the recovered
coefficient is positive. Separately, TreeSHAP’srawoutput for a scikit-learn tree classifier is the
probability, not the log-odds, so on the log-odds scale its attributions violate local accuracy and
every construction built on that decomposition becomes invalid. Both are guarded by assertions
in our released code.
What excludingmagic_telescopecosts.We removed one real dataset from the study be-
cause a single (dataset, model) cell, the RBF support vector machine, produced a partial depen-
dence reconstruction far worse than predicting the model’s own mean, and that cell dominated
every pooled average it entered. The decision is defensible but it is not free, and it cuts against
the paper’s own argument in one respect: the regime in which partial dependence fails catas-
trophically is exactly the regime Proposition 1 says to watch for, so removing the clearest real
22

instance of it removes evidence for our own thesis as well as noise. What remains is the con-
trolled correlation sweep, where the same failure is produced deliberately and can be read against
a knownρ. A study aimed specifically at characterising catastrophic PDP failure should keep
such datasets and report them per model rather than pooled; ours is aimed at comparing expla-
nation methods on average, and for that purpose one dominating cell is a liability. We flag the
exclusion here so that it is not mistaken for a data-cleaning step.
Reproducibility.All code, dataset specifications, and the full result table are released. Every
table and figure is generated from the recorded results and read at compile time. So is every
number quoted in the prose: each is emitted by the same pipeline as a macro and referenced
by name, so the text cannot disagree with the tables beside it. We adopted this after finding
that it had already happened: when one run superseded another, several sentences kept the
earlier run’s values while the adjacent tables were regenerated. Hand-checking is what failed, so
hand-checking is not the remedy.
Explanations that claim to describe how a model works can be asked to predict. Turning
that observation into a metric requires care: the construction must be shared across explanation
families to be fair, parameter-free to be attributable, and interpreted against a reference that
says how much additive structure was available to recover in the first place. We have made
explicit the identification of that reference with theL2 additive projection under independence,
and shown that the condition is not a technicality: it is what decides the empirical ranking.
Across 13 real datasets and 9 synthetic designs, SHAP-derived curves carry the most recover-
able predictive content and LIME the least, with ALE and PDP not reliably separated. But the
ordering is entirely a dependence phenomenon. Where features are independent by construction,
PDP is provably optimal and is measurably not beaten; where they are dependent (which on
real tabular data they invariably are), SHAP gains, and two controls establish that the gain is
in the attributions rather than in the aggregation used to read them. The useful statement for
a practitioner is therefore conditional: how much of a model an explanation can convey depends
less on which explanation method is chosen than on how far the model’s inputs depart from
independence.
Applying the same logic to the evaluation metrics themselves turns out to be the more
uncomfortable exercise. A metric that claims to say which of two explanations is better can
be handed two explanations whose ordering is known by construction, and asked. Of the five
established metrics we tested this way, two track the ordering reliably, one is defeated by the
simplest possible worthless explanation (a permuted curve, which it prefers to the intact one)
and two are reversed, systematically scoring degraded explanations above faithful ones. Our own
metric lands in the first group, not statistically separable from the best performer (p= 0.371).
That is a modest claim for the metric and a considerably less modest one about the state of
explanation evaluation: face validity is not evidence that a metric orders explanations correctly,
and the ordering can be tested directly by anyone willing to build a ladder of known quality and
climb it.
Acknowledgements
This work began as the first author’s bachelor thesis at Oslo Metropolitan University.
Author contributions
H.L.H. conceived the original idea, carried out the experiments, supervised the project, and
wrote and reviewed the manuscript. J.S. carried out the experiments and wrote and reviewed
the manuscript. Both authors read and approved the final manuscript.
23

Competing interests
The authors declare no competing interests.
Funding
The authors received no specific funding for this work.
Data availability
The real datasets analysed in this study are publicly available from OpenML [28]; the dataset
identifiers are listed in Table 1. The synthetic designs are generated by the released code from
the specifications in Section 2.3.
Code availability
All code needed to reproduce the experiments, tables and figures is publicly available athttps:
//github.com/hugohammer/xaieval.
References
[1] Satyapriya Krishna, Tessa Han, Alex Gu, Javin Pombra, Shahin Jabbari, Steven Wu, and
Himabindu Lakkaraju. The disagreement problem in explainable machine learning: A
practitioner’s perspective.Transactions on Machine Learning Research, 2024. Preprint
arXiv:2202.01602.
[2] Miquel Miró-Nicolau, Antoni Jaume-i Capó, and Gabriel Moyà-Alcover. A comprehensive
study on fidelity metrics for XAI.Information Processing & Management, 62(1):103900,
2025.
[3] Zachary C. Lipton. The mythos of model interpretability.ACM Queue, 16(3):31–57, 2018.
[4] Finale Doshi-Velez and Been Kim. Towards a rigorous science of interpretable machine
learning.arXiv preprint arXiv:1702.08608, 2017.
[5] Peter Hase and Mohit Bansal. Evaluating explainable AI: Which algorithmic explanations
help users predict model behavior? InProceedings of the 58th Annual Meeting of the
Association for Computational Linguistics, pages 5540–5552, 2020.
[6] Jerome H. Friedman. Greedy function approximation: A gradient boosting machine.The
Annals of Statistics, 29(5):1189–1232, 2001.
[7] Daniel W. Apley and Jingyu Zhu. Visualizing the effects of predictor variables in black box
supervised learning models.Journal of the Royal Statistical Society Series B, 82(4):1059–
1086, 2020.
[8] Scott M. Lundberg and Su-In Lee. A unified approach to interpreting model predictions. In
Advances in Neural Information Processing Systems 30, pages 4765–4774, 2017.
[9] Marco Tulio Ribeiro, Sameer Singh, and Carlos Guestrin. “why should I trust you?”: Ex-
plaining the predictions of any classifier. InProceedings of the 22nd ACM SIGKDD Inter-
national Conference on Knowledge Discovery and Data Mining, pages 1135–1144, 2016.
24

[10] Danish Pruthi, Rachit Bansal, Bhuwan Dhingra, Livio Baldini Soares, Michael Collins,
Zachary C. Lipton, Graham Neubig, and William W. Cohen. Evaluating explanations: How
much do explanations from the teacher aid students?Transactions of the Association for
Computational Linguistics, 10:359–375, 2022.
[11] Christoph Molnar, Giuseppe Casalicchio, and Bernd Bischl. Quantifying model complex-
ity via functional decomposition for better post-hoc interpretability. InMachine Learning
and Knowledge Discovery in Databases (ECML PKDD 2019 Workshops), volume 1167 of
Communications in Computer and Information Science, pages 193–204. Springer, 2020.
[12] Wassily Hoeffding. A class of statistics with asymptotically normal distribution.The Annals
of Mathematical Statistics, 19(3):293–325, 1948.
[13] Ilya M. Sobol. Global sensitivity indices for nonlinear mathematical models and their Monte
Carlo estimates.Mathematics and Computers in Simulation, 55(1–3):271–280, 2001.
[14] Giles Hooker. Generalized functional ANOVA diagnostics for high-dimensional functions
of dependent variables.Journal of Computational and Graphical Statistics, 16(3):709–732,
2007.
[15] Sarah Tan, Rich Caruana, Giles Hooker, and Yin Lou. Distill-and-compare: Auditing black-
box models using transparent model distillation. InProceedings of the 2018 AAAI/ACM
Conference on AI, Ethics, and Society, pages 303–310, 2018.
[16] Chih-Kuan Yeh, Cheng-Yu Hsieh, Arun Suggala, David I. Inouye, and Pradeep Ravikumar.
On the (in)fidelity and sensitivity of explanations. InAdvances in Neural Information
Processing Systems 32, pages 10967–10978, 2019.
[17] Umang Bhatt, Adrian Weller, and José M. F. Moura. Evaluating and aggregating feature-
based model explanations.Proceedings of the 29th International Joint Conference on Arti-
ficial Intelligence (IJCAI), pages 3016–3022, 2020.
[18] David Alvarez-Melis and Tommi S. Jaakkola. On the robustness of interpretability methods.
arXiv preprint arXiv:1806.08049, 2018.
[19] Prasad Chalasani, Jiefeng Chen, Amrita Roy Chowdhury, Xi Wu, and Somesh Jha. Con-
cise explanations of neural networks using adversarial training. InProceedings of the 37th
International Conference on Machine Learning, pages 1383–1391, 2020.
[20] Sara Hooker, Dumitru Erhan, Pieter-Jan Kindermans, and Been Kim. A benchmark for
interpretability methods in deep neural networks. InAdvances in Neural Information Pro-
cessing Systems 32, pages 9734–9745, 2019.
[21] Anna Hedström, Leander Weber, Daniel Krakowczyk, Dilyara Bareeva, Franz Motzkus,
Wojciech Samek, Sebastian Lapuschkin, and Marina M.-C. Höhne. Quantus: An explainable
AI toolkit for responsible evaluation of neural network explanations and beyond.Journal
of Machine Learning Research, 24(34):1–11, 2023.
[22] Isabelle Guyon and André Elisseeff. An introduction to variable and feature selection.
Journal of Machine Learning Research, 3:1157–1182, 2003.
[23] Christoph Molnar.Interpretable Machine Learning: A Guide for Making Black Box Models
Explainable. Independently published, 3rd edition, 2025.
[24] Leo Breiman. Random forests.Machine Learning, 45(1):5–32, 2001.
25

[25] Aaron Fisher, Cynthia Rudin, and Francesca Dominici. All models are wrong, but many are
useful: Learning a variable’s importance by studying an entire class of prediction models
simultaneously.Journal of Machine Learning Research, 20(177):1–81, 2019.
[26] Scott M. Lundberg, Gabriel Erion, Hugh Chen, Alex DeGrave, Jordan M. Prutkin, Bala
Nair, Ronit Katz, Jonathan Himmelfarb, Nisha Bansal, and Su-In Lee. From local expla-
nations to global understanding with explainable AI for trees.Nature Machine Intelligence,
2(1):56–67, 2020.
[27] Sebastian Bordt and Ulrike von Luxburg. From Shapley values to generalized additive mod-
els and back. InProceedings of the 26th International Conference on Artificial Intelligence
and Statistics (AISTATS), volume 206 ofProceedings of Machine Learning Research, pages
709–745, 2023.
[28] Joaquin Vanschoren, Jan N. van Rijn, Bernd Bischl, and Luis Torgo. OpenML: Networked
science in machine learning.ACM SIGKDD Explorations Newsletter, 15(2):49–60, 2014.
[29] Sture Holm. A simple sequentially rejective multiple test procedure.Scandinavian Journal
of Statistics, 6(2):65–70, 1979.
[30] Cynthia Rudin. Stop explaining black box machine learning models for high stakes decisions
and use interpretable models instead.Nature Machine Intelligence, 1(5):206–215, 2019.
26
