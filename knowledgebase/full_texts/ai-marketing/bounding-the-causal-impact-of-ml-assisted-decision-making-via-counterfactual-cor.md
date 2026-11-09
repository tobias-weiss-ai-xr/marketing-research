---
title: Bounding the Causal Impact of ML-assisted Decision-Making via Counterfactual Correctness
url: https://arxiv.org/abs/2607.21806
category: ai-marketing
subcategory: measurement
date: 2026-07
venue: ''
authors:
- Jonathan Zhang
- Erik Skalnes
- Jacob Chen
- Michael Oberst
source: arxiv
pdf_url: https://arxiv.org/pdf/2607.21806
pages: 45
chars: 121830
fetched_at: '2026-11-08T13:29:40+00:00'
kb_version: 1
---

# Bounding the Causal Impact of ML-assisted Decision-Making via Counterfactual Correctness

Bounding the Causal Impact of ML-assisted Decision-Making
via Counterfactual Correctness
Jonathan Zhang1 Erik Skalnes1 Jacob M. Chen1 Michael Oberst1
1Computer Science Dept., Johns Hopkins University, Baltimore, Maryland, USA
Abstract
Predictive machine learning (ML) models are in-
creasingly used to aid human decision-makers
across various high-risk domains such as health-
care and criminal justice. There is a growing recog-
nition of the need to evaluate the causal impact
of deploying these systems on downstream out-
comes, such as patient survival or crime recidi-
vism. Randomized control trials (RCTs) can pro-
vide high-quality evidence on the impact of a de-
ployed model, but they run into a challenge: it is
often infeasible to run repeated trials when mod-
els are updated or retrained to improve predictive
performance. In this work, we present a partial-
identification approach to using prior RCT data
to construct bounds on the causal effect of a new
model. The core innovation in our approach is to
leverage assumptions relating fine-grained predic-
tive accuracy to downstream outcomes. We do
so via two monotonicity assumptions: first, on
individual-level ‘counterfactual correctness’ (all
else being equal, a correct prediction leads to non-
inferior outcomes); and second, on the relation
between subgroup predictive performance and out-
comes, interpretable as an assumption regarding
trust in model outputs. We demonstrate our method
with a simulation study, illustrating how incorporat-
ing this information can lead to more informative
bounds compared to prior work.
1 INTRODUCTION
Predictive machine learning (ML) models are being de-
ployed more and more into high-risk decision-making do-
mains, such as recidivism prediction for criminal justice or
diagnostic aids for physicians [Travaini et al., 2022, Esteva
et al., 2017]. In these domains, there is a growing recogni-
tion of the need to treat artificial intelligence (AI) systems
as interventions, going beyond predictive accuracy to rea-
son about their impact on decision-makers and downstream
outcomes [Ben-Michael et al., 2025, Liu et al., 2025, Joshi
et al., 2025, van Amsterdam et al., 2026].
In some settings, it is feasible to evaluate the impact of pre-
dictive systems via randomized control trials (RCTs), which
are increasingly being used to assess ML/AI interventions in
medicine [Shaukat et al., 2022, Yao et al., 2021, Upton et al.,
2024, Gohil et al., 2024, Chen et al., 2025, Shaban et al.,
2025] and criminal justice [Imai et al., 2023]. Such trials
are often designed to evaluate the impact of deploying an
ML/AI system as a discrete intervention, including impact
on decision-makers and downstream outcomes, keeping in
mind that the impact of predictive models is mediated by
human behavior [Raji and Liu, 2025].
However, there are limits to the approach of viewing dis-
tinct ML models as distinct interventions. For example, it
is typically infeasible to run a new RCT for every proposed
update to a model. This infeasibility creates a challenge: If
a randomized trial has been conducted for one model, and a
new model (with higher predictive accuracy) is developed
afterwards, what can we say about the expected impact of
the latter model?
Prior work has made some steps towards addressing this gap.
For instance, Nercessian et al. [2025] propose an adaptive
trial design under the assumption that downstream outcomes
do not differ between models whose predictions agree. Chen
and Oberst [2025] propose a causal framework for partial
identification that weakens this assumption, by allowing
for differences in outcomes at the individual level, even
if predictions are identical. They motivate this possibility
from the perspective of user trust: For instance, a model that
flags every patient as high-risk is likely to influence clinical
actions less than a model with higher precision, even on the
cases where they agree. To model this aspect of performance,
they assume that residual variation in outcomes is driven
by an observable per-model measure of global predictive
arXiv:2607.21806v1  [cs.LG]  23 Jul 2026

performance (e.g., precision).
However, both of these frameworks fail to incorporate the
accuracy of individual-level model predictions—in many
scenarios, we might expect that correct predictions are no
worse than suboptimal predictions. We refer to this notion
ascounterfactual correctness: Whether or not the predic-
tions of a new model would have been correct on individual
subjects in the original RCT. With that notion in mind, we
make the following contributions in this work: (i) We extend
the causal framework of Chen and Oberst [2025] to incor-
porate known ‘correct’ prediction labels: if a new model
produces the correct prediction, we assume that outcomes
are no worse than those of models that made incorrect pre-
dictions. (ii) We further extend this framework to consider
conditional subgroup predictive performance as influenc-
ing outcomes, rather than a global measure of performance,
reflecting the idea that users are likely to develop mental
heuristics of where models perform well or poorly. (iii) We
provide population-level upper and lower bounds under
these assumptions, and further provide a consistent and
asymptotically normal estimator of those bounds. Crucially,
unlike Chen and Oberst [2025], we do so without assuming
that model performance measures are known a priori, and
allow for the fact that e.g., sub-group performance needs to
be estimated from data. (iv) In a semi-synthetic simulation
study, we illustrate that incorporating this information can
lead to more informative bounds compared to prior work.
Our framework is most useful in settings where the “correct”
predictions (which we often refer to as the “true labels”)
are observed for all individuals in the RCT, and explicitly
assumes that predictions themselves do not influence the
true label. These conditions may co-occur when the predic-
tion task is fundamentally diagnostic, with the possibility
of retrospective (even if expensive) assessment of the cor-
rect prediction for each individual. Our framework can be
extended to settings where the true label is not always ob-
served, under specific mechanisms of missingness. We dis-
cuss one of these examples in greater detail in Appendix G.
We also discuss distinctions between our work and other
related areas in Appendix F.
2 SETUP & CAUSAL MODEL
Notation:We use upper case letters X to denote random
variables, lower case x to denote realizations, and calli-
graphic font X to denote the set of possible values. 1{E} is
the indicator function of an event E, equal to 1 if the event
occurs and 0 otherwise. Unless otherwise noted, ∥ · ∥refers
to theL 2(P)norm and| · |refers to the absolute value.
Problem Setup: We model the data-generating process as
the directed acyclic graph (DAG) in Fig. 1a. A directed edge
A→B means that A may cause B. No edge means A
does not cause B. Each node is a random variable. D∈
{1, . . . , d}are the arms of the RCT (e.g. with and without
ML assistance). T is the set of models being trialed, with
each model corresponding to a specific arm. The model we
would like to evaluate (denoted πe) is untrialed, so πe /∈ T.
X∈ Xare features used by the prediction model, Z∈ Z
is the “true label”, and ˆZ∈ Z is the predicted label. The
performance of the model Π for individuals with covariates
X is a real number M∈ M ⊆R, where M denotes the
range of achievable metric values.A∈ Ais the action taken
by the decision-maker, which we do not model explicitly
and generally allow to be unobserved. Finally, Y∈R is the
downstream outcome, influenced by A and X. We employ
potential outcomes notation [Richardson and Robins, 2013]
where Y(Π =π) represents the counterfactual value of Y
that would be observed had we setΠ =π.
Example2.1 (Diagnosis Recommendation System).To
build intuition for our notation in the context of a con-
crete example, consider a machine learning model (π)
designed to help radiologists make diagnoses. An RCT
to determine whether model deployment improves pa-
tient outcomes might randomly assign physicians to
either the control arm (no model, D= 1 ) or the treat-
ment arm (model assistance, D= 2 ). The model takes
in a chest x-ray, as well as other general patient infor-
mation (X) as input, and returns a predicted diagnosis
( ˆZ), such as pneumonia, pneumothorax, or healthy. This
prediction may or may not agree with the true diagno-
sis (Z), which may be recorded later in time (e.g., at
discharge). Over time, physicians will learn about the
performance of the deployed models (M) on different
types of patients. This learning can be captured quanti-
tatively by calculating a per-subgroup metric on each of
the models such as the sensitivity/specificity. Together,
the knowledge of these variables will affect the physi-
cian’s actions (A), in turn affecting some outcome of
interest such as survival rate (Y ). These actions are left
unmodeled, and in general could represent a complex
set of actions (e.g., specific language used in a radiol-
ogy report). Our goal is to evaluate expected patient
outcomes Y under the deployment of a new model πe
not included in the trial.
We now formally introduce our causal framework, shown
graphically in Fig. 1.
Assumption 2.1(Data Generating Process).We assume that
(D,Π, X, Z,ˆZ, M, Y)are generated according to the fol-
lowing structural causal model (SCM) Pearl [2009], where
all noise variablesϵare mutually independent:
D=f D(ϵD) Π =f Π(D)
X, Z=f XZ (ϵXZ ) ˆZ= Π(X)
Y=f Y (X, Z, M,ˆZ, ϵY )M=f M (X,Π)
Note that our SCM allows for the possibility of various
causal relationships between X and Z (e.g., where X causes

Π
D
ˆZ Y M
X Z A
(a)
Π
D
ˆZ Y M
X Z
(b)
Figure 1: Fig. 1a is the causal DAG representing the structure of an RCT, whereX denotes features, and D the arm of the
RCT, which determines the model Π used for prediction. The model Π outputs predictions ˆZ as a deterministic function
of X, where Z is the true label. The dotted bi-directed edge between X, Zrepresents the possibility that X and Z share
an unobserved common cause. M is a subgroup performance metric of Π, A is the decision-maker’s actions, and Y is the
downstream outcome. A solid square indicates the node is deterministic given its parents, and a dotted circle indicates
the node is hidden. In Fig. 1b, we show the same graph after applying the latent projection operator on A, which only
considers the observed variables in the RCT. Edges also present in prior work by Chen and Oberst [2025] are shown in blue
(re-interpreting Chen and Oberst [2025] as having an implicit actionA), while edges novel to our work are shown in red.
Z, vice versa, or where both are related by a common cause).
We make a few additional observations: First, our causal
model (reflected in Fig. 1b) does not include A, but can be
seen as a projection of the directed acyclic graph (DAG)
shown in Fig. 1a, where A mediates the effect of ˆZ on Y .
This mediation reflects our natural intuition that the decision-
maker, not the model, is the final conduit of change, and
serves as conceptual motivation for several of our assump-
tions. Second, we allow for X, Zto be arbitrarily related
(e.g., by a common cause), but we assume that ˆZ does not
have any causal effect on Z. Finally, several elements are
deterministicgiven their parents, ˆZandMin particular.
Our Goal:Consider a model πe ̸∈ T. Our goal is to esti-
mate the expectation ofYforπ e had it been in the RCT.
E[Y(π e)] =E[Y( ˆZ=π e(X), M=f M (X, πe))].(1)
This notation is used in conjunction with our SCM
notation defined in Assump. 2.1. In particular,
the right-hand side of Eq. (1) can be written as
E[f Y (X, Z, fM (X, πe), πe(X), ϵY )],1 where we set ˆZ=π e(X), M=f M (X, πe) and evaluate the expectation.
We further illustrate this estimand with an example.
Example2.1 (continuing from p. 2).Suppose we have
data from a previous RCT on radiology models. The
data records the values of Z and ˆZ for all models on all
patients. For each patient, we observe the value of Y
under the deployment of a single model. In this context,
given a new model, our goal would be to estimate its
effect on patient survival ( Y ) without running a new
RCT, leveraging only knowledge of the new model’s
predictions ( ˆZ) on the data from that previous RCT.
1Throughout, we write fY with its arguments in the order
given in Assump. 2.1, namely(X, Z, M,ˆZ, ϵY ).
3 STRUCTURAL ASSUMPTIONS AND
FALSIFICATION TESTS
To draw conclusions about the downstream outcomes of
an untrialed model, we need to make additionalstructural
assumptions on the data generating process, beyond those
implied by the causal graph. First, we formalize our notion
of counterfactual correctness.
Assumption 3.1(Counterfactual Correctness).We assume
that correct predictions cause no harm. That is, for all
m, m′ ∈ Mandz, z′ ∈ Zwithz′ ̸=z,
Y( ˆZ=z, M=m, Z=z)≥Y( ˆZ=z ′, M=m ′, Z=z)
This assumption states that, when predictions are correct, we
don’t expect them to harm outcomes.2 While intuitive, this
assumption may fail if e.g., physicians act contrary to predic-
tions. That said, this assumption has testable implications,
which can be assessed using RCT data.
Proposition 3.1(Falsification of Assump. 3.1).Let
πc, πw ∈ Tbe two trialed models (one of which will be
“correct” and the other “wrong”), and let Xc̸=w :={x∈
X |πc(x)̸=π w(x)} be the set of covariates on which their
predictions disagree. Consider the subpopulation where
X∈ Xc̸=w and Z=π c(X) (i.e., where πc is correct and
πw incorrect). Then, the observation that outcomes are bet-
ter underπ w,3
E[Y|X∈ X c̸=w,Π =π c, Z=π c(X)]
2This inequality can be written equivalently under Assump. 2.1
as requiring that for all values of z, x, m, ϵY and z′ ̸=z ,
fY (x, z, m, z, ϵY )≥f Y (x, z, m′, z′, ϵY ), where potential out-
comes are taken to be pointwise functions of the noise variables.
3All falsification tests require that the relevant conditioning
sets have non-zero probability of occurring. For this case, if D
is uniformly distributed and independent of X, Z, it suffices that
P

X∈ Xc̸=w, Z=π c(X)

>0.

<E[Y|X∈ X c̸=w,Π =π w, Z=π c(X)]
falsifies Assump. 3.1.
This falsification test allows practitioners to use a simple hy-
pothesis test (comparing two means) to assess if Assump. 3.1
is contradicted by RCT data. This falsification test, and oth-
ers we propose, cannot conclusively demonstrate that an
assumption is true, only that it is false, and passing the
falsification tests does not validate the assumptions: The
assumption may hold on RCT data but not more broadly
across all future, untrialed models, and our assumptions are
defined pointwise on potential outcomes, while these fal-
sifications test for inequalities in expectation. Nonetheless,
these tests have the appeal of being simple to implement.
Proofs for all results, including the proof for the falsification
tests, are provided in the Appendix.
Next, we introduce three additional assumptions adapted
from Chen and Oberst [2025], but modified to better align
with real-world conditions and our new data generating pro-
cess. While the previous assumption dealt with outcomes
under different predictions, the next assumptions focus on
outcomes under the same prediction. We first introduce a no-
tion of performance monotonicity, which was also explored
in Chen and Oberst [2025].
Assumption 3.2(Conditional Performance monotonicity).
Potential outcomes are monotonic in model performance
relative to correctness: If mi < mj for mi, mj ∈ M, then
for allz∈ Zand allˆz∈ Zwithˆz̸=z,
Y( ˆZ=z, M=m i, Z=z)≤Y( ˆZ=z, M=m j, Z=z)
Y( ˆZ= ˆz, M=m i, Z=z)≥Y( ˆZ= ˆz, M=m j, Z=z)
This assumption states that, conditioned on correctness, po-
tential outcomes are monotonic with respect to model per-
formance. When the prediction is correct (ˆz=z), potential
outcomes are monotonically increasing with respect to per-
formance, and vice versa when the prediction is incorrect
(ˆz̸=z ). Conceptually, this assumption reflects the idea
that decision-makers are more likely to trust higher per-
forming models, and follow through on their predictions.
When the prediction is correct, this increased trust leads
to better outcomes, but when predictions are incorrect, this
reliance leads to worse outcomes. Chen and Oberst [2025]
considered a simplified form of this assumption, where im-
proved performance always leads to better outcomes, which
is likely invalid outside a narrow range of settings. They
motivated the assumption in a binary alerting setting, where
false alerts are assumed to not be harmful at the individual
level, and ˆz= 0 does nothing to affect decision-making.
We similarly present a falsification test for Assump. 3.2.
This falsification test only covers the case when ˆZ=z ; we
provide an analogous test for the case when ˆZ̸=z in the
Appendix.
Proposition 3.2(Falsification of Assump. 3.2).Let
π+, π− ∈ T be two trialed models. Consider a sub-
population with Xbetter ⊆ Xsuch that for all x∈ Xbetter,
fM (x, π+)> fM (x, π−), and a subpopulation with covari-
ates Xagree ⊆ Xsuch that for all x∈ Xagree, π+(x) =
π−(x). Then, for anyX s =X better ∩ Xagree
E[Y|X∈ Xs,Π =π +, Z=π +(X)]
<E[Y|X∈ X s,Π =π −, Z=π +(X)]
falsifies Assump. 3.2.
Furthermore, we introduce the concept of a “neutral predic-
tion”, and assume that performance of the model does not
affect the outcome in this case.
Assumption 3.3(Neutral prediction).There exists ˆz0 ∈ Z
such that for allm i, mj ∈ Mandz∈ Z
Y( ˆZ= ˆz0, M=m i, Z=z) =Y( ˆZ= ˆz0, M=m j, Z=z)
We note that this assumption is “optional”, in the sense that
the method still produces bounds without it, at the cost of
those bounds being potentially looser. This assumption is
largely the same as Assumption 3.2 of Chen and Oberst
[2025], and plays the role of linking the “control arm” of
a trial to evaluation of a newer model, and can be seen as
a special case of Assump. 3.2 in which the nonstrict in-
equality becomes an equality. In our running example, such
a “prediction” could be choosing to defer to a radiologist,
and the control arm could be viewed as an “always defer”
policy. The intuition for this assumption is that when the
model takes the neutral prediction, the physician behaves as
if there were no model at all, and hence model performance
does not impact actions. We also provide a falsification test
for this assumption.
Proposition 3.3(Falsification of Assump. 3.3).Let
π1, π2 ∈ Tbe two trialed models. Letting Xˆz0 :={x∈
X |π1(x) =π 2(x) = ˆz0}, the observation that for some
z∈ Z:
E[Y|X∈ X ˆz0 ,Π =π 1, Z=z]
̸=E[Y|X∈ X ˆz0 ,Π =π 2, Z=z]
falsifies Assump. 3.3.
Finally, similar to Chen and Oberst [2025], we require that
Y itself be bounded by known maximum and minimum
values, which can be trivially falsified by observing values
ofYoutside of those bounds.
Assumption 3.4(Bounded outcomes).There exist
Ymin, Ymax ∈Rsuch thatY min ≤Y≤Y max

4 PARTIAL IDENTIFICATION BOUNDS
In this section, we introduce our main result, which provides
upper and lower bounds on the expected outcome under de-
ployment of a new model (Eq. (1)). Before we can introduce
this result, we first introduce some notation for partitions of
the model and covariate space in our RCT. These partitions
will be used in the derivation of our bounds.
Definition 4.1(Partitions).We use πi as a model in the
model space and πe as the untrialed model. For each value
of x, we define the set of trialed models that make the same
prediction as our untrialed model,π e(x)4.
S(x) :={π i ∈ T |πi(x) =π e(x)}
We further partition S(x) into models whose predictive
performances imply outcomes that are no better / no worse
than those ofπ e
S↓(x, z):={π i ∈ S |fM (x, πi)≤f M (x, πe), πe(x) =z}
∪ {πi ∈ S |fM (x, πi)≥f M (x, πe), πe(x)̸=z}
S↑(x, z):={π i ∈ S |fM (x, πi)≥f M (x, πe), πe(x) =z}
∪ {πi ∈ S |fM (x, πi)≤f M (x, πe), πe(x)̸=z}
We further define subsets of S↓,S ↑ containing only the
models whose performance is closest to that ofπ e.
S⇓(x, z):= arg min
πi∈S↓(x,z)
|fM (x, πi)−f M (x, πe)|
S⇑(x, z):= arg min
πi∈S↑(x,z)
|fM (x, πi)−f M (x, πe)|
Finally, for some value of x and an optimal prediction z,
we define the set of all trialed models that give the correct
prediction and its complement:
C(x, z):={π i ∈ T |πi(x) =z}
C(x, z):={π i ∈ T |πi(x)̸=z}
We note that any of the defined sets can possibly be empty.
Example2.1 (continuing from p. 3).Suppose in our ra-
diology RCT, we have three models:π1, π2, π3. The pre-
cision of these models are 0.1, 0.8, and 0.9, respectively,
at a specific covariate valuex. For a specific patient with
covariates x, whose true diagnosis, z, is pneumonia, we
want to evaluate an untrialed model, πe, with precision
0.7. Suppose π2, π3 and πe all suggest the diagnosis of
pneumonia, while π1 suggests bronchitis for this par-
ticular patient. Under this scenario, S(x) ={π 2, π3},
and πe was optimal, and thus since both π2 and π3
4As in Chen and Oberst [2025], these sets should be written
with πe as an argument, but we omit this for brevity. Note thatS
stands for “same” andCstands for “correct”.
have greater performance than πe, S↑(x, z) ={π2, π3}
and S↓(x, z) =∅ . If πe were not optimal the sets
would be reversed. Further, S⇑(x, z) ={π 2}, since
its performance metric is closest to that of πe. Finally,
C(x, z) ={π2, π3}, C(x, z) ={π1}.
Next, under the notation established in Def. 4.1, we intro-
duce abranch selectorthat assigns each (x, z)to the single
assumption used to bound the outcome.
Definition 4.2(Branch selector).For each (x, z)we define
lower- and upper-bound branch selectorsbL, bU :X × Z →
{neu,mon,cor,def} (neutral, monotonic, correct, default),
evaluated by first match:
bL(x, z) =



neuπ e(x) = ˆz0,S(x)̸=∅
monπ e(x)̸= ˆz0,S ↓(x, z)̸=∅
corπ e(x) =z,S ↓(x, z) =∅, C(x, z)̸=∅
defotherwise,
bU (x, z) =



neuπ e(x) = ˆz0,S(x)̸=∅
monπ e(x)̸= ˆz0,S ↑(x, z)̸=∅
corπ e(x)̸=z,S ↑(x, z) =∅,C(x, z)̸=∅
defotherwise.
Because each selector is a function evaluated by first match,
it returns exactly one value, so the induced indicators
1{bL =k},1{b U =k}partition the space ofX × Z.
With this selector, we can now produce our main theorem,
which provides bounds on the expected outcome of deploy-
ing an untrialed model in our novel RCT setting.
Theorem 4.1(Bounds).Under Assumptions 2.1 and 3.1
to 3.4, we have the following bounds on the impact of our
untrialed modelπ e:
L(πe)≤E[Y( ˆZ=π e(X), M=f M (X, πe))]≤U(π e)
Where:
L(πe) =E[1{b L =neu}E[Y|X,Π∈ S(X), Z](2)
+1{b L =mon}E[Y|X,Π∈ S ⇓(X, Z), Z]
+1{b L =cor}max
i∈C(X,Z)
E[Y|X,Π =i, Z]
+1{b L =def}Y min].(3)
U(π e) =E[1{b U =neu}E[Y|X,Π∈ S(X), Z]
+1{b U =mon}E[Y|X,Π∈ S ⇑(X, Z), Z]
+1{b U =cor}min i∈C(X,Z) E[Y|X,Π =i, Z]
+1{b U =def}Y max].(4)
Note that each value of X, Zis covered by exactly one
“branch”, and the bound is constructed via pointwise upper

and lower bounds on the resulting outcome under πe. We
illustrate the intuition for the lower bound here, with sym-
metric logic for the upper bound: (i) When bL =neu , our
untrialed model takes the neutral prediction, and there are
models in the RCT that agree. By Assump. 3.3, the down-
stream outcome will be equal regardless of performance
across these neutral-prediction-taking models. (ii) When
bL =mon , our untrialed model does not take the neutral
prediction, and there are models in the RCT that agree with
it and have worse or equal performance. By Assump. 3.2,
the downstream outcome of our untrialed model will be no
worse than the best performing model in this set. (iii) When
bL =cor , our untrialed model takes the optimal predic-
tion, and there are no models in the RCT that agree with it
and have worse or equal performance. We also know that
bL ̸=neu and C(x, z), or the set of incorrect models, is
non-empty. By Assump. 3.1, the downstream outcome of
our untrialed model will be no worse than any of these in-
correct models, since they must have taken a suboptimal
prediction. (iv) Finally, when bL =def , none of the prior
cases apply, leaving us with the maximally conservative
choice of Ymin. We provide a flowchart for the lower bound
in Fig. A.8, and note that the logic is similar (with slightly
different relevant sets) for the upper bound.
Tightness of BoundsChen and Oberst [2025] construct
similar bounds under a different set of assumptions, and
show that they are tight, in the sense that there exists a pair
of SCMs that are allowable under their assumptions, and
for which the upper and lower bounds match the causal
effect. We do not claim that our bounds are tight, and pro-
vide intuition here as to why constructing tight bounds is
not feasible under our counterfactual correctness assump-
tion. Focusing on L(πe), Assump. 3.1 is stated pointwise
on potential outcomes, while our bounds instead maximize
over the conditional expectations. To illustrate, consider
an RCT in which the untrialed model takes the optimal
prediction. The data contains π1(x), π2(x) that take incor-
rect predictions, while πe(x) takes the optimal prediction.
Both trialed models have the same conditional expectation
E[Y|X,Π, Z] = 0.75, so our lower-bound for πe(x) would
be 0.75. A (likely tighter) lower bound would instead be
E[maxi=1,2 Y(π i)|X, Z] , but implementing such a bound
is not feasible given that we only observe outcomes for a
single trialed model for any individual.
5 ESTIMATION
The bounds in Theorem 4.1 have several values that must
be estimated. For example, Eq. (2) requires E[Y|X,Π∈
S(X), Z]for all x such that 1{bL =neu}= 1 . If S(X)
contains more than one model, it is impossible to have
data on Y under both. We address this with consistent and
asymptotically normal estimators, and asymptotically valid
confidence intervals for the lower and upper bounds. Con-
structing these estimators requires addressing three chal-
lenges that do not arise in Chen and Oberst [2025]: (i) es-
timating E[Y|X, Z, π] via nuisance models, (ii) handling
non-smooth max/min operators, and (iii) estimating model
performance from finite data rather than assuming oracle
knowledge. We address these challenges with an augmented
inverse propensity weighted estimator for the bounds, and
we prove its consistency and asymptotic normality.
Definition 5.1(Nuisance Functions).We define the follow-
ing nuisance functions and estimators:
µj(x, z) :=E[Y|x,Π =π j, z](5)
ˆdL(x, z) := arg max
j∈C(x,z)
bµj(x, z)
ˆdU (x, z) := arg min j∈C(x,z) bµj(x, z)(6)
bλj(Y,Π, x, z) := 1{Π =j} P(Π =j|X=x)  Y−bµ j(x, z) 
(7)
cS⇓(x, z):= arg min
π∈ bS↓(x,z)
| ˆfM (x, π)− ˆfM (x, πe)|
bS⇑(x, z):= arg min
π∈ bS↑(x,z)
| ˆfM (x, π)− ˆfM (x, πe)|(8)
φL

x, z;ˆdL  :=bµ ˆdL(x,z)(x, z) +bλ ˆdL(x,z)(Y,Π, x, z)
φU

x, z;ˆdU  :=bµ ˆdU (x,z)(x, z) +bλ ˆdU (x,z)(Y,Π, x, z),
(9)
Where bS↓(x, z),bS↑(x, z)are defined as in Def. 4.1, with ˆf
in place off, andbµ(x, z)is the plug-in estimator ofµ.
For our estimators to be consistent and asymptotically nor-
mal, we require the following assumptions:
Assumption 5.1(Known Propensities).The value of
P(Π∈S|X) is known for all S⊆ T , and is strictly
positive for allS, X.
Given our RCT setting, this assumption will be satisfied by
design. A similar assumption is implicit in Chen and Oberst
[2025], but we make it explicit here. We require additional
conditions to handle non-smooth max/min operators, which
we describe next.
Assumption 5.2(Margin Conditions).Under Def. 5.1, there
existsα >0such that for anyt≥0, we have
P

min
j̸=d(X,Z)

µd(X,Z) (X, Z)−µj(X, Z)

 ≤t  ≤t α
for both dL(x, z), dU (x, z), as defined in Eq. (6), and µ
defined in Eq. (5). Furthermore, there exists β >0 such that
for anyt≥0, we have
P

min
i̸=j
|fM (X, πj)−f M (X, πi)| ≤t

≤t β
where fM is defined in Assump. 2.1, and πi, πj ∈ T ∪ {πe}.

These assumptions state that there is sufficient separation
between the downstream outcomes of the best two models,
the worst two models, and between the performance of any
two models, untrialed or trialed.
Assumption 5.3(Convergence of Nuisance Functions).The
nuisance functions bµj(X, Z),bfM (x;π i), defined in Def. 5.1
converge at rates op(n− 1 2(1+α) ) and op(n− 1 2β ), respectively,
for all πi ∈ T, x∈ X, where α and β are the same constants
as in the Margin Conditions (Assump. 5.2). That is:
∥bµj(X, Z)−µj(X, Z)∥=o p(n− 1 2(1+α) )
∥ bfM (x;π i)−f M (x, πi)∥=o p(n− 1 2β )
whereπ i ∈ T ∪ {πe}
We note thatop(n−1/4) convergence rates have been demon-
strated for a variety of modern machine learning methods
under e.g., sparsity constraints [Chernozhukov et al., 2018],
making Assump. 5.3 plausible for moderate values of α, β
(e.g., α= 1, β= 2 ). Finally, we can define our estima-
tor of the upper and lower bounds as the average of the
pseudo-outcomes defined below.
Definition 5.2(Pseudo-Outcomes).We first define
ˆh(X, Y, Z, S) :=
bµS(X, Z) + 1{Π∈S} P(Π∈S|X)  Y−bµ S(X, Z) 
where S⊆ Tis an arbitrary set of models. Then, we define
pseudo-outcomes for the lower and upper bounds as
bψL(Y, X,Π, Z;bfM ) =
1{ˆbL =neu} ˆh(X, Y, Z,S) +1{ˆbL =mon} ˆh(X, Y, Z,bS⇓)
+1{ ˆbL =cor}φ L(X, Z;ˆdL) +1{ ˆbL =def}Y min
bψU (Y, X,Π, Z;bfM ) =
1{ˆbU =neu} ˆh(X, Y, Z,S) +1{ˆbU =mon} ˆh(X, Y, Z,bS⇑)
+1{ ˆbU =cor}φ U (X, Z;ˆdU ) +1{ ˆbU =def}Y max
where the argument after the semicolon denotes the perfor-
mance function used to construct the partitions and branch
selectors: ˆbL, ˆbU and the estimated sets are computed from
the estimated performance ˆfM in place off M .
Theorem 5.1(Consistency and asymptotic normality of
bL(πe), bU(π e)).If Assumptions 5.1 to 5.3 hold for some
α, β >0, then
bL(πe) =n −1
nX
i=1
bψL(Yi, Xi,Π i, Zi; bfM ) P − →L(πe)
bU(π e) =n −1
nX
i=1
bψU (Yi, Xi,Π i, Zi; bfM ) P − →U(πe)
Where
P
− →denotes convergence in probability. Furthermore,
√n(bL(πe)−L(π e)) d − →N(0, σ2 L)
√n( bU(π e)−U(π e)) d − →N(0, σ2 U )
Where
d
− →denotes convergence in distribution, and σ2 L =
Var(ψL), σ2 U =Var(ψ U ), with ψL, ψU denoting the pseudo-
outcomes of Def. 5.2 evaluated with the true nuisance func-
tionsµ j, fM in place of their estimates.
Since our estimator is asymptotically normal, this provides
us the following corollary:
Corollary 5.1(Confidence Intervals for L(πe), U(πe)).Un-
der the conditions of Theorem 5.1, we can construct the
following confidence intervals forL(π e), U(πe):
bL(πe)±z 1−γ/2
q
dV ar(bψL)/n
bU(π e)±z 1−γ/2
q
dV ar(bψU )/n
Where z1−γ/2 is the 1−γ/2 quantile of the standard nor-
mal distribution, and dV ar(bψL), dV ar(bψU ) are the empirical
variance of bψL, bψU , respectively.
We note that our results require Assump. 5.2 to hold for
some value of α, β. The first (α) condition controls the bias
from selecting the wrong argmax/argmin in the 1{bL =
cor},1{b U =cor} branches; the second (β) condition con-
trols a separate source of error specific to our setting, namely
that ˆψL, ˆψU are evaluated at the estimated partitions bS⇓, bS⇑
rather than at the population partitions in Theorem 4.1, and
ˆfM ’s error can permute the relevant ordering. The probabil-
ity of a permutation is bounded polynomially by the margin
condition, contributingo p(n−1/2)to the overall error.
6 EXPERIMENTS
We now shift discussion to a semi-synthetic simulation
study to demonstrate the efficiency of our proposed bounds.
All experiment code is available on Github at oberst-
lab/counterfactual-correctness-experiments.
We will use data from Imai et al. [2023], an experiment eval-
uating the impact of showing judges algorithmically gener-
ated risk scores (1-6) prior to bail sentencing. This data also
records the action taken by judges, which includes assigning
high bail, low bail, or release without bail to suspects (note
that “imprisonment without bail” does not appear as an op-
tion in the data). Downstream outcomes were recorded for
each suspect, such as failure to appear (FTA) at a trial hear-
ing. The full data includes suspect covariates, judge group,
judge decision, risk score, and FTA for every individual.
FTA distributions in the data are shown in Table A.6.

Simulation SetupWe use this data to construct a semi-
synthetic simulation study, re-using the covariates of indi-
viduals in the dataset, as well as the original risk scores. We
introduce simulation in order to reason about the ‘ground
truth’ counterfactual outcomes under different forms of AI
assistance. We focus primarily on hypothetical alerting mod-
els that notify the judge of high-risk individuals: This fram-
ing allows us to consider the “control arm” of the trial as
providing information on judge behavior in the absence of
an alert. We make the additional simplification, for conve-
nience, of considering “requires bail” (A= 1) and “does
not require bail” as the only actions, collapsing the “high”
and “low” bail options. Using the original data, we learn
ˆfa(X) := ˆP(A= 1|X,Arm=control)
ˆfy(X, A) :=ˆP(FTA= 1|X, A,Arm=control)
where both ˆfa and ˆfy represent our estimates of the condi-
tional probability of (a) the judge requiring some form of
bail in the absence of ML assistance, and (b) the defendant
failing to appear, conditioned on the type of bail required.
We also retain the risk score (from 1-6) that is provided in
the original dataset, which we denote R, and which is used
to inform some of the models that we evaluate later on.
We then simulate judge and defendant behavior as follows:
If no alert is raised ( ˆZ= 0 ), then judges make decisions
according to ˆfa(X), and if an alert is raised ( ˆZ= 1 ), then
their probability increases proportionally to the performance
(in this case, the precision) of the model as follows
P(A= 1|X,Π, ˆZ)
=σ(logit( ˆfa(X)) +1{ ˆZ= 1} ·fM (X,Π))
where σ is the sigmoid function, and fM (X,Π) is the per-
formance of the model Π at X. We then simulate failure-
to-appear using P(FTA= 1|X, A) = ˆfy(X, A), and
construct our outcome Y as a net utility that rewards court
appearance while imposing a penalty for requiring bail
Yraw = 1−c FTA ·FTA−c det ·A, Y= Yraw +c det 1 +c det ,
with cFTA = 1 and cdet = 0.1 . The affine rescaling is for
interpretability, as Yraw is already bounded by [−0.1,1] . The
bail penalty cdet reflects our intuition that over-detention is
harmful and allows incorrect predictions, particularly false
positives, to cause harm.
Finally, we take Z (the ‘ground truth’ label) to be whether
or not the defendant would fail to appear if released with-
out bail. While in reality, Z would only be observed for
individuals released without bail, for the purpose of the il-
lustrative simulation here, we take it to be observed for all
individuals.5 More broadly, while we use real data to inform
5In Appendix G we discuss assumptions under which our
method can handle missingness, and in Exp. 5 we consider a
misspecified experiment with missing values ofZ.
Exp # Width (Ours) Width (Chen) Lower Bd. (Ours) Upper Bd. (Ours) True value
1 0.331 0.704 0.430 0.761 0.726
2 0.121 0.362 0.616 0.737 0.728
3 0.140 0.281 0.624 0.764 0.696
4 0.454 0.802 0.349 0.803 0.695
5 0.204 0.281 0.586 0.790 0.697
Table 1: Semi-synthetic experiment results (see Section 6)
showing the mean width of our bounds ˆU(π e)− ˆL(πe) com-
pared to those derived via the method of Chen and Oberst
[2025], alongside the average upper and lower bound values
and the true value. We see that our bounds are consistently
tighter and always contain the true value ofY.
our simulation of judge and defendant behavior, we do not
claim that our simulation is a realistic surrogate for real-
world behavior: Rather, we design our simulation primarily
for ease of exposition, and to illustrate the application of
our method. We now briefly describe the experiments run,
with additional details and figures in Appendix E.
Evaluation of changing alert thresholds and re-training
of a pre-existing model (Exp 1, 2)
To start, we consider a simulated setting of an RCT that
has two arms: a control arm in which no alerts are raised,
and a trial arm in which alerts are raised when the risk
score R present in the Imai et al. [2023] dataset is greater
than 3. Judge decisions and outcomes are then simulated
as described above. In Experiment 1, we evaluate a new
alerting system that uses the same risk scores R, but raises
an alert at a lower (less conservative) threshold. In particular,
alerts are raised for every individual with a risk score R
greater than 1. In Experiment 2, we create a new risk score
algorithm and evaluate an untrialed model that raises an alert
when this new risk score is greater than 3. This algorithm
is discussed in greater detail in Appendix E.1. This setting
represents the motivating scenario where a freshly trained
model needs to be evaluated.
Overall results are shown in Table 1, where we observe
that the bounds produced by Chen and Oberst [2025] are
extremely wide (0.70 and 0.36 for Exp. 1 and 2, respectively)
given that the outcome (and hence the target to estimate) is
bounded between zero and one. This gap reflects the fact
that in both cases, the untrialed model tends to produce
alerts in cases where no alerts occurred in the original trial
(trialed model raises alerts on 28.1% of individuals, whereas
the untrialed model raises an alert on 80.2% and 45.6%
of individuals in Exp. 1 and 2, respectively). Our method
produces bounds that are consistently narrower than those
of prior work (0.33 and 0.12, respectively), because we are
able to produce tighter lower bounds in settings where these
previously unobserved alerts are correct, and tighter upper
bounds when they are incorrect.

In the Appendix, we conduct a further ablation study, using
data from Experiment 1, finding that the primary driver of
improvement over Chen and Oberst [2025] is the use of the
counterfactual correctness bounds, rather than e.g., stratifi-
cation of M on X. In Table A.4, we also show the results
of 100 Monte Carlo trials of Exp. 1, demonstrating that all
methods consistently capture the true expected outcome, but
our method produces a smaller bound interval and narrower
confidence intervals.
Evaluation in the absence of an RCT (Exp 3, 4)
When no RCT has been conducted, but data exists from
prior to the deployment of any AI system, such data is
effectively a “single-arm” RCT that only contains a control
arm that always takes the “neutral” action. We illustrate the
application of our method in this setting. Here, the prediction
of “no alert” is taken to be a neutral action (leading to similar
outcomes as those in prior data), while the prediction of
“alert”, when correct/incorrect, implies that outcomes will
be no worse/no better than those observed in prior data. In
Experiment 3, we evaluate an untrialed model that raises an
alert for individuals with a risk score greater than 3, and in
Experiment 4, we evaluate an untrialed model that does the
same for those with a risk score greater than 1.
Overall results are similarly shown in Table 1, where we
again find our bounds are consistently tighter than Chen
and Oberst [2025]. We also notice that bound width grows
with the alert rate of the untrialed model. Experiment 3’s
conservative threshold (R>3 ) raises few alerts and leads to
a narrow bound (0.140), while Exp. 4’s aggressive threshold
(R>1 ) raises many more alerts and leads to a much wider
bound ( 0.454). Additionally, in Fig. 2, we illustrate our
bounds across different age groups, compared to the method
from Chen and Oberst [2025], after modifying the latter
method to use per-age group performances. We see that
across all groups, our bounds capture the true value and are
tighter, agreeing with Table 1. This result suggests that our
notion of counterfactual correctness is the primary driver of
empirical improvement, rather than stratifyingMbyX.
Misspecified example with missing data (Exp 5)
As a sanity check, we consider the setting of Experiment
3, but where we hide the counterfactual failure-to-appear
values for offenders that were not released without bail. This
modification violates our assumptions, and this experiment
is designed to illustrate the impact of missing values of Z,
as discussed further in Appendix G.
In Table 1, we observe that our bounds are wider (0.2 in
Exp. 5 vs 0.14 in Exp. 3), but still contain the true value. We
show further details in Table A.2 in the Appendix, where we
demonstrate that the bounds still capture the true values, and
the confidence intervals for the lower and upper bounds still
capture the ground truth values. This result suggests that
the bias introduced by the misspecification in this particular
Figure 2: (Experiment 3) Comparison of bounds on down-
stream outcomes for an untrialed model with a single trialed
model in the RCT. The figure displays the lower bound
and upper bound computed using our proposed method and
a modified version of the method from Chen and Oberst
[2025], also plotted in Fig. A.1b with performance as func-
tions of individual age.
simulation is not significant enough to yield invalid results
from applying our method.
7 CONCLUSION AND LIMITATIONS
When a newly trained model has better predictive perfor-
mance than models previously evaluated in an RCT, there
will naturally be limited data on how its predictions impact
outcomes, insofar as it makes correct predictions where
prior models failed. Our work improves over prior work in
partial identification of the causal impact of AI systems, by
recognizing that, when ground truth labels exist in a prior
RCT, the model’s predictions can be evaluated against that
ground truth, and correctness used as a directional indicator
of relative impact at the individual level.
Several limitations and areas for future investigation merit
discussion. Since our falsification tests are in-expectation,
individual-level assumption violations may go undetected.
Handling cases where an identical prediction from a better
model has a worse outcome, or where neutral action de-
pends on performance, is an important direction for future
work. Many deployed models also do not provide discrete
decision recommendations. Instead, many may output con-
tinuous predictions. Our method can still be applied by
imposing discrete buckets, or using 1{bL =cor},1{b U =
cor},1{b L =def},1{b U =def} branches only, but more
efficient methods of evaluation may be of interest. As dis-
cussed, our method has limitations when values of Z are
missing, which presents avenues for future research. Finally,
investigating an approach that incorporates observational
data, which is often significantly more available than RCT
data, would be valuable.

References
Alexander Balke and Judea Pearl. Probabilistic evaluation
of counterfactual queries. InProceedings of the Twelfth
National Conference on Artificial Intelligence, volume 1,
pages 230–237. AAAI Press/MIT Press, 1994.
Alexander Balke and Judea Pearl. Bounds on treatment
effects from studies with imperfect compliance.Journal
of the American Statistical Association, 92(439):1171–
1176, 1997.
Elias Bareinboim and Judea Pearl. Causal inference by sur-
rogate experiments: z-identifiability. InProceedings of
the 28th Conference on Uncertainty in Artificial Intelli-
gence (UAI), pages 113–120, Catalina Island, CA, 2012.
AUAI Press.
Alexis Bellot. Towards bounding causal effects un-
der Markov equivalence. In Negar Kiyavash and
Joris M. Mooij, editors,Proceedings of the Forti-
eth Conference on Uncertainty in Artificial Intelli-
gence, volume 244 ofProceedings of Machine Learn-
ing Research, pages 308–332. PMLR, 15–19 Jul 2024.
URL https://proceedings.mlr.press/v244/
bellot24a.html.
Alexis Bellot and Silvia Chiappa. Towards estimating
bounds on the effect of policies under unobserved
confounding. In A. Globerson, L. Mackey, D. Belgrave,
A. Fan, U. Paquet, J. Tomczak, and C. Zhang, editors,
Advances in Neural Information Processing Systems, vol-
ume 37, pages 104556–104594. Curran Associates, Inc.,
2024. URL https://proceedings.neurips.cc/
paper_files / paper / 2024 / file /
bd0194a23b3b0787e54a0173d65b0b37 -
Paper-Conference.pdf.
Eli Ben-Michael, D James Greiner, Melody Huang, Kosuke
Imai, Zhichao Jiang, and Sooahn Shin. Does AI help
humans make better decisions? a statistical evaluation
framework for experimental and observational studies.
Proceedings of the National Academy of Sciences, 122
(38):e2505106122, 2025.
Yewon Byun, Dylan Sam, Michael Oberst, Zachary Lip-
ton, and Bryan Wilder. Auditing fairness under un-
observed confounding. In Sanjoy Dasgupta, Stephan
Mandt, and Yingzhen Li, editors,Proceedings of The
27th International Conference on Artificial Intelligence
and Statistics, volume 238 ofProceedings of Machine
Learning Research, pages 4339–4347. PMLR, 5 2024.
URL https://proceedings.mlr.press/v238/
byun24a.html.
Jacob M. Chen and Michael Oberst. Just trial once:
Ongoing causal validation of machine learning mod-
els. InProceedings of the Forty-first Conference
on Uncertainty in Artificial Intelligence, 2 2025.
URL https://proceedings.mlr.press/v286/
chen25b.html.
Yao Chen, D. Ohlssen, A. Readie, G. Ligozio, Ru-
vie Martin, and T. Coroller. The framework
that survives bad models: Human-AI collaboration
for clinical trials.ArXiv, abs/2510.06567, 2025.
URL https : / / api.semanticscholar.org /
CorpusId:281891637.
Victor Chernozhukov, Denis Chetverikov, Mert Demirer,
Esther Duflo, Christian Hansen, Whitney Newey, and
James Robins. Double/debiased machine learning for
treatment and structural parameters.The Economet-
rics Journal, 21(1):C1–C68, 02 2018. ISSN 1368-4221.
doi: 10.1111/ectj.12097. URL https://doi.org/
10.1111/ectj.12097.
David Maxwell Chickering and Judea Pearl. A clinician’s
tool for analyzing non-compliance. InProceedings of
the National Conference on Artificial Intelligence, pages
1269–1276. AAAI, 1996.
Juan Correa and Elias Bareinboim. General transportability
of soft interventions: Completeness results.Advances
in Neural Information Processing Systems, 33:10902–
10912, 2020a.
Juan D. Correa and Elias Bareinboim. A calculus for
stochastic interventions: Causal effect identification and
surrogate experiments. InProceedings of the 34th AAAI
Conference on Artificial Intelligence, pages 10093–10100.
AAAI Press, 2020b.
Guilherme Duarte, Noam Finkelstein, Dean Knox, Jonathan
Mummolo, and Ilya Shpitser. An automated approach
to causal inference in discrete settings.Journal of the
American Statistical Association, 119(547):1778–1793,
2024.
Andre Esteva, Brett Kuprel, Roberto A Novoa, Justin Ko,
Susan M Swetter, Helen M Blau, and Sebastian Thrun.
Dermatologist-level classification of skin cancer with
deep neural networks.nature, 542(7639):115–118, 2017.
Shruti K. Gohil, Edward Septimus, Ken Kleinman, Neha
Varma, Taliser R. Avery, Lauren Heim, Risa Rahm,
William S. Cooper, Mandelin Cooper, Laura E. McLean,
Naoise G. Nickolay, Robert A. Weinstein, L. Hayley
Burgess, Micaela H. Coady, Edward Rosen, Selsebil
Sljivo, Kenneth E. Sands, Julia Moody, Justin Vigeant,
Syma Rashid, Rebecca F. Gilbert, Kim N. Smith, Brandon
Carver, Russell E. Poland, Jason Hickok, S. G. Sturdevant,
Michael S. Calderwood, Anastasiia Weiland, David W.
Kubiak, Sujan Reddy, Melinda M. Neuhauser, Arjun
Srinivasan, John A. Jernigan, Mary K. Hayden, Abinav
Gowda, Katyuska Eibensteiner, Robert Wolf, Jonathan B.

Perlin, Richard Platt, and Susan S. Huang. Steward-
ship prompts to improve antibiotic selection for urinary
tract infection.JAMA, 331(23):2018, 6 2024. doi:
10.1001/jama.2024.6259. URL http://dx.doi.org/
10.1001/jama.2024.6259.
Dan Hendrycks, Steven Basart, Norman Mu, Saurav Ka-
davath, Frank Wang, Evan Dorundo, Rahul Desai, Tyler
Zhu, Samyak Parajuli, Mike Guo, et al. The many faces
of robustness: A critical analysis of out-of-distribution
generalization. InProceedings of the IEEE/CVF interna-
tional conference on computer vision, pages 8340–8349.
IEEE, 2021.
Kosuke Imai, Zhichao Jiang, D James Greiner, Ryan Halen,
and Sooahn Shin. Experimental evaluation of algorithm-
assisted human decision-making: Application to pretrial
public safety assessment.Journal of the Royal Statistical
Society Series A: Statistics in Society, 186(2):167–189,
2023.
Shalmali Joshi, Iñigo Urteaga, Wouter A C van Amster-
dam, George Hripcsak, Pierre Elias, Benjamin Recht,
Noémie Elhadad, James Fackler, Mark P Sendak, Jenna
Wiens, Kaivalya Deshpande, Yoav Wald, Madalina Fit-
erau, Zachary Lipton, Daniel Malinsky, Madhur Nayan,
Hongseok Namkoong, Soojin Park, Julia E V ogt, and
Rajesh Ranganath. AI as an intervention: improving
clinical outcomes relies on a causal approach to AI
development and validation.Journal of the Ameri-
can Medical Informatics Association, 1 2025. doi:
10.1093/jamia/ocae301. URL https://doi.org/
10.1093/jamia/ocae301.
Pang Wei Koh, Shiori Sagawa, Henrik Marklund,
Sang Michael Xie, Marvin Zhang, Akshay Balsubramani,
Weihua Hu, Michihiro Yasunaga, Richard Lanas Phillips,
Irena Gao, Tony Lee, Etienne David, Ian Stavness, Wei
Guo, Berton Earnshaw, Imran Haque, Sara M Beery,
Jure Leskovec, Anshul Kundaje, Emma Pierson, Sergey
Levine, Chelsea Finn, and Percy Liang. WILDS: A bench-
mark of in-the-wild distribution shifts. In Marina Meila
and Tong Zhang, editors,Proceedings of the 38th Inter-
national Conference on Machine Learning, volume 139
ofProceedings of Machine Learning Research, pages
5637–5664. PMLR, 18–24 Jul 2021. URL https://
proceedings.mlr.press/v139/koh21a.html.
Apoorva Lal, Wenjing Zheng, and Simon Ejdemyr. A
framework for generalization and transportation of
causal estimates under covariate shift.arXiv preprint
arXiv:2301.04776, 2023.
Sanghack Lee, Juan D. Correa, and Elias Bareinboim. Gen-
eral identifiability with arbitrary surrogate experiments.
InProceedings of the 35th Conference on Uncertainty in
Artificial Intelligence (UAI), volume 115 ofProceedings
of Machine Learning Research, pages 389–398. PMLR,
2019.
Lydia T. Liu, Inioluwa Deborah Raji, Angela Zhou, Luke
Guerdan, Jessica Hullman, Daniel Malinsky, Bryan
Wilder, Simone Zhang, Hammaad Adam, Amanda Cos-
ton, Ben Laufer, Ezinne Nwankwo, Michael Zanger-
Tishler, Eli Ben-Michael, Solon Barocas, Avi Feller,
Marissa Gerchick, Talia Gillis, Shion Guha, Daniel Ho,
Lily Hu, Kosuke Imai, Sayash Kapoor, Joshua Loftus,
Razieh Nabi, Arvind Narayanan, Ben Recht, Juan Carlos
Perdomo, Matthew Salganik, Mark Sendak, Alexander
Tolbert, Berk Ustun, Suresh Venkatasubramanian, An-
gelina Wang, and Ashia Wilson. Bridging prediction and
intervention problems in social systems.arXiv preprint
(2507.05216v3), 7 2025. URL http://arxiv.org/
abs/2507.05216v3.
Charles F. Manski. Nonparametric bounds on treatment ef-
fects.American Economic Review, 80(2):319–323, 1990.
Papers and Proceedings.
Chengzhi Mao, Kevin Xia, James Wang, Hao Wang, Jun-
feng Yang, Elias Bareinboim, and Carl V ondrick. Causal
transportability for visual recognition. InProceedings
of the IEEE/CVF Conference on Computer Vision and
Pattern Recognition, pages 7521–7531. IEEE, 2022.
John P Miller, Rohan Taori, Aditi Raghunathan, Shiori
Sagawa, Pang Wei Koh, Vaishaal Shankar, Percy Liang,
Yair Carmon, and Ludwig Schmidt. Accuracy on the line:
on the strong correlation between out-of-distribution and
in-distribution generalization. InInternational Confer-
ence on Machine Learning, pages 7721–7735. PMLR,
2021.
Hussein Mozannar, Hunter Lang, Dennis Wei, Prasanna
Sattigeri, Subhro Das, and David Sontag. Who should
predict? exact algorithms for learning to defer to humans.
InInternational conference on artificial intelligence and
statistics, pages 10520–10545. PMLR, 2023.
Hongseok Namkoong, Ramtin Keramati, Steve Yadlowsky,
and Emma Brunskill. Off-policy policy evaluation for
sequential decisions under unobserved confounding.Ad-
vances in Neural Information Processing Systems, 33:
18819–18831, 2020.
Michael Nercessian, Wenxin Zhang, Alexander Schubert,
Daphne Yang, Maggie Chung, Ahmed Alaa, and Adam
Yala. Data reuse enables cost-efficient randomized trials
of medical AI models.arXiv preprint arXiv:2511.08986,
2025.
Judea Pearl.Causality. Cambridge university press, 2009.
Judea Pearl. Generalizing experimental findings.Journal of
causal inference, 3(2):259–266, 2015.

Judea Pearl and Elias Bareinboim. Transportability of causal
and statistical relations: A formal approach. InProceed-
ings of the AAAI Conference on Artificial Intelligence,
volume 25, pages 247–254, 2011.
Inioluwa Deborah Raji and Lydia T. Liu. Evaluating
prediction-based interventions with human decision mak-
ers in mind. In Yingzhen Li, Stephan Mandt, Shipra
Agrawal, and Emtiyaz Khan, editors,Proceedings of The
28th International Conference on Artificial Intelligence
and Statistics, volume 258 ofProceedings of Machine
Learning Research, pages 1180–1188. PMLR, 5 2025.
URL https://proceedings.mlr.press/v258/
raji25a.html.
Amy Richardson, Michael G. Hudgens, Peter B. Gilbert,
and Jason P. Fine. Nonparametric bounds and sensitivity
analysis of treatment effects.Statistical Science, 29(4),
11 2014. ISSN 0883-4237. doi: 10 .1214/14-sts499. URL
http://dx.doi.org/10.1214/14-STS499.
Thomas S Richardson and James M Robins. Single world
intervention graphs (SWIGs): A unification of the coun-
terfactual and graphical approaches to causality.Center
for the Statistics and the Social Sciences, University of
Washington Series. Working Paper, 128(30):2013, 2013.
James M. Robins. The analysis of randomized and non-
randomized AIDS treatment trials using a new approach
to causal inference in longitudinal studies. In L. Sechrest,
H. Freeman, and A. Mulley, editors,Health Service Re-
search Methodology: A Focus on AIDS, pages 113–159.
U.S. Public Health Service, National Center for Health
Services Research, Washington, DC, 1989.
Jonas Rothfuss, Bhavya Sukhija, Tobias Birchler, Par-
nian Kassraie, and Andreas Krause. Halluci-
nated adversarial control for conservative offline pol-
icy evaluation. In Robin J. Evans and Ilya Sh-
pitser, editors,Proceedings of the Thirty-Ninth Con-
ference on Uncertainty in Artificial Intelligence, vol-
ume 216 ofProceedings of Machine Learning Re-
search, pages 1774–1784. PMLR, 31 Jul–04 Aug 2023.
URL https://proceedings.mlr.press/v216/
rothfuss23a.html.
Mostafa Shaban, Yasmine M Osman, Nermen Abdelfatah
Mohamed, and Marwa Mamdouh Shaban. Empowering
breast cancer clients through AI chatbots: transforming
knowledge and attitudes for enhanced nursing care.BMC
nursing, 24(1):994, 2025.
Aasma Shaukat, David R. Lichtenstein, Samuel C. Somers,
Daniel C. Chung, David G. Perdue, Murali Gopal,
Daniel R. Colucci, Sloane A. Phillips, Nicholas A.
Marka, Timothy R. Church, William R. Brugge, Robert
Thompson, Robert Chehade, Burr Loew, Jackie Downing,
James Vermillion, Lawrence Borges, Ruma Rajbhandari,
Theodore Schafer, Sahin Coban, James Richter, Peter
Carolan, Francis Colizzo, Tiffany Jeong, Marisa DelSig-
nore, Shreya Asher, Robert McCabe, Daniel Van Han-
del, Birtukan Cinnor, Benjamin Mitlyng, Cynthia Sher-
man, S. David Feldshon, Amy Lounsbury, Ana Thomp-
son, Anusha Duggirala, Irena Davies, Christopher Huang,
Charles Bliss, Arpan Mohanty, Oltion Sina, Jean Mendez,
Allison Iwan, Jennifer Stromberg, Jonathan Ng, Lavi Eris-
son, Polina Golland, Daniel Wang, Evan Wlodkowski,
Joseph Carlin, Perikumar Javia, Neelima Chavali, Austin
Wang, Janine Little, and Cara Hunsberger. Computer-
aided detection improves adenomas per colonoscopy
for screening and surveillance colonoscopy: A random-
ized trial.Gastroenterology, 163(3):732–741, 9 2022.
doi: 10 .1053/j .gastro.2022.05.028. URL http://
dx.doi.org/10.1053/j.gastro.2022.05.028.
Xu Shi, Ziyang Pan, and Wang Miao. Data integration in
causal inference.Wiley Interdisciplinary Reviews: Com-
putational Statistics, 15(1):e1581, 2023.
Elizabeth A Stuart, Stephen R Cole, Catherine P Bradshaw,
and Philip J Leaf. The use of propensity scores to as-
sess the generalizability of results from randomized trials.
Journal of the Royal Statistical Society Series A: Statistics
in Society, 174(2):369–386, 2011.
Yi Su, Pavithra Srinath, and Akshay Krishnamurthy. Adap-
tive estimator selection for off-policy evaluation. In
Hal Daumé III and Aarti Singh, editors,Proceedings
of the 37th International Conference on Machine Learn-
ing, volume 119 ofProceedings of Machine Learning
Research, pages 9196–9205. PMLR, 13–18 Jul 2020.
URL https://proceedings.mlr.press/v119/
su20d.html.
Rohan Taori, Achal Dave, Vaishaal Shankar, Nicholas Car-
lini, Benjamin Recht, and Ludwig Schmidt. Measuring
robustness to natural distribution shifts in image clas-
sification.Advances in Neural Information Processing
Systems, 33:18583–18599, 2020.
Guido Vittorio Travaini, Federico Pacchioni, Silvia Bellu-
more, Marta Bosia, and Francesco De Micco. Machine
learning and criminal justice: A systematic review of
advanced methodology for recidivism risk prediction.In-
ternational journal of environmental research and public
health, 19(17):10594, 2022.
Ross Upton, Ashley P. Akerman, Thomas H. Marwick,
Casey L. Johnson, Hania Piotrowska, Mamta Bajre,
Maria Breen, Helen Dawes, Hakim-Moulay Dehbi, Tine
Descamps, Victoria Harris, Will Hawkes, Samuel Kras-
ner, Emily Sanderson, Natalie Savage, Ben Thompson,
Victoria Williamson, William Woodward, Rizwan Sar-
war, Jamie O’Driscoll, Rajan Sharma, Virginia Chiocchia,
Steffen E. Petersen, Elena Frangou, Ged Ridgway, San-
jeev Bhattacharyya, David P. Ripley, Gary Woodward,

and Paul Leeson. PROTEUS: A prospective RCT eval-
uating use of AI in stress echocardiography.NEJM
AI, 1(11), 10 2024. doi: 10 .1056/aioa2400865. URL
http://dx.doi.org/10.1056/aioa2400865.
Wouter A. C. van Amsterdam, Michael Oberst, Jean Feng,
Jenna Wiens, Shengpu Tang, Shalmali Joshi, Rajesh
Ranganath, Mark Sendak, Uri Shalit, Julia E. V ogt,
Brett Beaulieu-Jones, Muhammad Mamdani, David Kent,
Patrick J. Heagerty, Thomas R. Fleming, and Anna Gold-
enberg. Clinical trials for continuously monitored and up-
dated AI systems.Nature Medicine, 32(6):1972–1974, 6
2026. doi: 10 .1038/s41591-026-04368-9. URL https:
//doi.org/10.1038/s41591-026-04368-9.
Wouter AC Van Amsterdam, Nan Van Geloven, Jesse H
Krijthe, Rajesh Ranganath, and Giovanni Ciná. When
accurate prediction models yield harmful self-fulfilling
prophecies.Patterns, 6(4):101229, 2025.
Rajeev Verma and Eric Nalisnick. Calibrated learning to
defer with one-vs-all classifiers. InInternational Confer-
ence on Machine Learning, pages 22184–22202. PMLR,
2022.
Olivia Wiles, Sven Gowal, Florian Stimberg, Sylvestre-
Alvise Rebuffi, Ira Ktena, Krishnamurthy Dj Dvijotham,
and Ali Taylan Cemgil. A fine-grained analysis on
distribution shift. InInternational Conference on
Learning Representations, 2022. URL https:/ /
openreview.net/forum?id=Dl4LetuLdyK.
Runzhe Wu, Masatoshi Uehara, and Wen Sun. Distribu-
tional offline policy evaluation with predictive error guar-
antees. In Andreas Krause, Emma Brunskill, Kyunghyun
Cho, Barbara Engelhardt, Sivan Sabato, and Jonathan
Scarlett, editors,Proceedings of the 40th International
Conference on Machine Learning, volume 202 ofPro-
ceedings of Machine Learning Research, pages 37685–
37712. PMLR, 23–29 Jul 2023. URL https://
proceedings.mlr.press/v202/wu23s.html.
Xiaoxi Yao, David R. Rushlow, Jonathan W. Inselman, Roza-
lina G. McCoy, Thomas D. Thacher, Emma M. Behnken,
Matthew E. Bernard, Steven L. Rosas, Abdulla Akfaly,
Artika Misra, Paul E. Molling, Joseph S. Krien, Randy M.
Foss, Barbara A. Barry, Konstantinos C. Siontis, Suraj
Kapa, Patricia A. Pellikka, Francisco Lopez-Jimenez,
Zachi I. Attia, Nilay D. Shah, Paul A. Friedman, and
Peter A. Noseworthy. Artificial intelligence–enabled
electrocardiograms for identification of patients with
low ejection fraction: a pragmatic, randomized clini-
cal trial.Nature Medicine, 27(5):815–819, 5 2021.
doi: 10 .1038/s41591-021-01335-4. URL http://
dx.doi.org/10.1038/s41591-021-01335-4.
Junzhe Zhang and Elias Bareinboim. Bounding causal ef-
fects on continuous outcome. InProceedings of the AAAI
Conference on Artificial Intelligence, volume 35, pages
12207–12215, 2021a.
Junzhe Zhang and Elias Bareinboim. Non-parametric meth-
ods for partial identification of causal effects.Columbia
CausalAI Laboratory Technical Report, 2021b.

Bounding the Causal Impact of ML-assisted Decision-Making
via Counterfactual Correctness (Supplementary Material)
Jonathan Zhang1 Erik Skalnes1 Jacob M. Chen1 Michael Oberst1
1Computer Science Dept., Johns Hopkins University, Baltimore, Maryland, USA
A APPENDIX OVERVIEW
The appendix contains the following sections:
• Appendix B: Proofs and Additional Materials.
This section provides proofs for falsification tests for the core assumptions introduced in the main text. If these tests
fail, then the assumptions do not hold in the data, and any results may not be valid.
• Appendix C: Proof of Theorem 4.1.
This section provides a formal proof of the core theorem of the paper. To prove the validity of the bounds, we write the
analytical form of the bounds and demonstrate the expected value of the untrialed model falls within the bounds.
• Appendix D: Proof of Theorem 5.1.
This section provides a formal proof that the empirical estimator for our bounds is consistent and asymptotically
normal, enabling us to construct confidence intervals for our bounds. Since some of the branches of the bounds contain
discontinuous “max/min” operators, the techniques of Chen and Oberst [2025] cannot be directly applied to the entire
estimator. We instead formulate an AIPW estimator for our bounds. By Theorem 2 of Byun et al. [2024], we can
demonstrate that such an estimator is consistent and asymptotically normal if seven conditions are met. For each
assumption, we verify the conditions are met and directly apply the theorem.
• Appendix E: Further Simulation Details.
This section provides some brief additional information about the simulation study.
• Appendix F: Additional Related Work. This section provides an overview of works in related areas that are relevant to
our work, but were not discussed in the main text.
• Appendix G: Missing Data.
This section discusses the handling of cases in whichZis missing from our data.
• Appendix H: Flowchart.
This section provides a flowchart visualizing the branch-selection logic (bL) used to construct the bounds.

B PROOFS AND ADDITIONAL MATERIALS
The following assumptions are used in the proofs of the propositions and theorems in this paper.
Corollary B.1(Consistency).Under Assump. 2.1, if ˆZ= ˆz, M=m, Z=zthen
Y=Y( ˆZ= ˆz, M=m, Z=z).
Corollary B.2(Conditional Ignorability).Under Assump. 2.1, sinceY(ˆz, m)⊥ ⊥(ˆZ, M)|(X, Z), we have
P(Y(ˆz, m)|X, Z) =P

Y| ˆZ= ˆz, M=m, X, Z

.(10)
B.1 FALSIFICATION OF ASSUMPTION 3.1
Assumption 3.1(Counterfactual Correctness).We assume that correct predictions cause no harm. That is, for all m, m′ ∈ M
andz, z′ ∈ Zwithz′ ̸=z,
Y( ˆZ=z, M=m, Z=z)≥Y( ˆZ=z ′, M=m ′, Z=z)
Proposition 3.1(Falsification of Assump. 3.1).Let πc, πw ∈ Tbe two trialed models (one of which will be “correct”
and the other “wrong”), and let Xc̸=w :={x∈ X |πc(x)̸=π w(x)} be the set of covariates on which their predictions
disagree. Consider the subpopulation where X∈ Xc̸=w and Z=π c(X) (i.e., where πc is correct and πw incorrect). Then,
the observation that outcomes are better underπ w,1
E[Y|X∈ X c̸=w,Π =π c, Z=π c(X)]
<E[Y|X∈ X c̸=w,Π =π w, Z=π c(X)]
falsifies Assump. 3.1.
Proof.Suppose Assump. 2.1 holds. Choosex∈ X c̸=w. Then we have the following:
E[Y|X=x,Π =π c, Z=π c(x)]−E[Y|X=x,Π =π w, Z=π c(x)]
=E
h
Y|X=x, ˆZ=π c(x), M=f M (x, πc), Z=π c(x)
i
−E
h
Y|X=x, ˆZ=π w(x), M=f M (x, πw), Z=π c(x)
i
(11)
=E
h
Y( ˆZ=π c(x), M=f M (x, πc), Z=π c(x))−Y( ˆZ=π w(x), M=f M (x, πw), Z=π c(x))|X=x
i
(12)
≥0 (13)
Where Eq. (11) follows from Assump. 2.1, Eq. (12) follows from Corollary B.1, and Eq. (13) follows from Assump. 3.1. We
now aggregate.
E[Y|X∈ X c̸=w,Π =π c, Z=π c(X)]−E[Y|X∈ X c̸=w,Π =π w, Z=π c(X)]
=
Z
x
E[Y|X=x,Π =π c, Z=π c(x)]dP(x|X∈ X c̸=w,Π =π c, Z=π c(X))
−
Z
x
E[Y|X=x,Π =π w, Z=π c(x)]dP(x|X∈ X c̸=w,Π =π w, Z=π c(X))(14)
=
Z
x

E[Y|X=x,Π =π c, Z=π c(x)]−E[Y|X=x,Π =π w, Z=π c(x)]

dP(x|X∈ X c̸=w, Z=π c(X))
(15)
≥0 (16)
Where Eq. (14) follows by the tower property, Eq. (15) by Π⊥ ⊥(X, Z)(dropping Π from both measures and combining),
and Eq. (16) by Eq. (13).
1All falsification tests require that the relevant conditioning sets have non-zero probability of occurring. For this case, ifD is uniformly
distributed and independent ofX, Z, it suffices thatP

X∈ Xc̸=w, Z=π c(X)

>0.

B.2 FALSIFICATION OF ASSUMPTION 3.2
Assumption 3.2(Conditional Performance monotonicity).Potential outcomes are monotonic in model performance relative
to correctness: Ifm i < mj form i, mj ∈ M, then for allz∈ Zand allˆz∈ Zwithˆz̸=z,
Y( ˆZ=z, M=m i, Z=z)≤Y( ˆZ=z, M=m j, Z=z)
Y( ˆZ= ˆz, M=m i, Z=z)≥Y( ˆZ= ˆz, M=m j, Z=z)
Proposition 3.2(Falsification of Assump. 3.2).Let π+, π− ∈ Tbe two trialed models. Consider a sub-population with
Xbetter ⊆ Xsuch that for all x∈ Xbetter, fM (x, π+)> fM (x, π−), and a subpopulation with covariates Xagree ⊆ X
such that for allx∈ Xagree,π +(x) =π −(x). Then, for anyX s =X better ∩ Xagree
E[Y|X∈ Xs,Π =π +, Z=π +(X)]
<E[Y|X∈ X s,Π =π −, Z=π +(X)]
falsifies Assump. 3.2.
We will use the following lemma:
Lemma B.1(Observational Equivalence).For any πi ∈ Tand any x∈ X, z∈ Zsuch that P(X=x, Z=z,Π =π i)>
0:
E[Y|X=x,Π =π i, Z=z] =E
h
Y( ˆZ=π i(x), M=f M (x, πi), Z=z)|X=x, Z=z
i
(17)
Proof.
E[Y|X=x,Π =π i, Z=z] =E
h
Y|X=x, ˆZ=π i(x), M=f M (x, πi), Z=z
i
(18)
=E[Y( ˆZ=π i(x), M=f M (x, πi), Z=z)|X=x, ˆZ=π i(x),
M=f M (x, πi), Z=z](19)
=E
h
Y( ˆZ=π i(x), M=f M (x, πi), Z=z)|X=x, Z=z
i
(20)
Where Eq. (18) follows because ˆZ= Π(X) and M=f M (X,Π) are deterministic given (X,Π) , and Y⊥ ⊥Π|X, ˆZ, M, Z
under Assump. 2.1, since Π affects Y only through ( ˆZ, M). Eq. (19) follows from Consistency (Corollary B.1), noting
that given Z=z , we have Y(ˆz, m, z) =Y(ˆz, m)under Assump. 2.1. Eq. (20) follows from Conditional Ignorability
(Corollary B.2), i.e.,Y(ˆz, m)⊥ ⊥(ˆZ, M)|X, Z.
This lemma enables us to prove Proposition 3.2 and 3.3.
Proof.Choosingx∈ X s and settingz=π +(x), we have that:
E[Y|X=x,Π =π +, Z=π +(x)]−E[Y|X=x,Π =π −, Z=π +(x)]
=E[Y( ˆZ=π +(x), M=f M (x, π+), Z=π +(x))−(21)
Y( ˆZ=π +(x), M=f M (x, π−), Z=π +(x))|X=x, Z=π +(x)](22)
≥0(23)
Where Eq. (22) follows from Lemma B.1 with z=π +(x), noting that since x∈ Xs ⊆ Xagree we have π−(x) =π +(x), so
both potential outcomes share the prediction ˆZ=π +(x) and differ only in M. Eq. (23) then follows from Assump. 3.2,
which compares same-prediction outcomes that differ only in performance M. For this to hold over the entire Xs, we have:
E[Y|X∈ X s,Π =π +, Z=π +(X)]−E[Y|X∈ X s,Π =π −, Z=π +(X)]
=
Z
x
E[Y|X=x,Π =π +, Z=π +(x)]dP(x|X∈ X s,Π =π +, Z=π +(X))

−
Z
x
E[Y|X=x,Π =π −, Z=π +(x)]dP(x|X∈ X s,Π =π −, Z=π +(X))(24)
=
Z
x

E[Y|X=x,Π =π +, Z=π +(x)]−E[Y|X=x,Π =π −, Z=π +(x)]

dP(x|X∈ X s, Z=π +(X))
(25)
≥0 (26)
Where Eq. (24) follows from the tower property, Eq. (25) follows from Π⊥ ⊥(X, Z)(dropping Π from both measures,
which makes them identical and lets the integrals combine), and Eq. (26) follows from Eq. (23), thus contradicting our
observation.
This falsification test only tests for violations of Assump. 3.2 when the models give the correct prediction. The following
falsification test also exists for the case when the models give the incorrect prediction.
Proposition B.1(Falsification of Assump. 3.2).Let π+, π− ∈ Tbe two trialed models. Consider a sub-population with
Xbetter ⊆ Xsuch that for all x∈ Xbetter, fM (x, π+)> fM (x, π−), and a subpopulation with covariates Xagree ⊆ X
such that for allx∈ Xagree,π +(x) =π −(x). Then, for anyX s =X better ∩ Xagree
E[Y|X∈ Xs,Π =π +, Z̸=π +(X)]
>E[Y|X∈ X s,Π =π −, Z̸=π +(X)]
falsifies Assump. 3.2.
The proof is identical to the above, save for changes in the inequality direction and the value ofZin the expectation.
B.3 FALSIFICATION OF ASSUMPTION 3.3
Assumption 3.3(Neutral prediction).There existsˆz 0 ∈ Zsuch that for allmi, mj ∈ Mandz∈ Z
Y( ˆZ= ˆz0, M=m i, Z=z) =Y( ˆZ= ˆz0, M=m j, Z=z)
Proposition 3.3(Falsification of Assump. 3.3).Let π1, π2 ∈ Tbe two trialed models. Letting Xˆz0 :={x∈ X |π1(x) =
π2(x) = ˆz0}, the observation that for somez∈ Z:
E[Y|X∈ X ˆz0 ,Π =π 1, Z=z]
̸=E[Y|X∈ X ˆz0 ,Π =π 2, Z=z]
falsifies Assump. 3.3.
Proof.Suppose Assump. 3.3 holds. Choosex∈ X ˆz0 andz∈ Z, then we have the following:
E[Y|X=x,Π =π 2, Z=z]−E[Y|X=x,Π =π 1, Z=z]
=E[Y( ˆZ=π 2(x), M=f M (x, π2), Z=z)−
Y( ˆZ=π 1(x), M=f M (x, π1), Z=z)|X=x, Z=z](27)
=E[Y( ˆZ= ˆz0, M=f M (x, π2), Z=z)−Y( ˆZ= ˆz0, M=f M (x, π1), Z=z)|X=x, Z=z](28)
= 0 (29)
Where Eq. (27) follows from Lemma B.1. Eq. (28) follows from the definitions of π1 and π2. Eq. (29) follows from
Assump. 3.3. We then aggregate:
E[Y|X∈ Xˆz0 ,Π =π 2, Z=z]−E[Y|X∈ X ˆz0 ,Π =π 1, Z=z](30)
=
Z
x
E[Y|X=x,Π =π 2, Z=z]dP(x|Π =π 2, X∈ Xˆz0 , Z=z)−
Z
x
E[Y|X=x,Π =π 1, Z=z]dP(x|Π =π 1, X∈ Xˆz0 , Z=z)(31)

=
Z
x
E[Y|X=x,Π =π 2, Z=z]dP(x|X∈ Xˆz0 , Z=z)−
Z
x
E[Y|X=x,Π =π 1, Z=z]dP(x|X∈ Xˆz0 , Z=z)(32)
=
Z
x
E[Y|X=x,Π =π 2, Z=z]−E[Y|X=x,Π =π 1, Z=z]dP(x|X∈ Xˆz0 , Z=z)(33)
= 0 (34)
Where the logic is the same as before, contradicting our observation.

C PROOF OF THEOREM 4.1
Definition 4.2(Branch selector).For each (x, z)we define lower- and upper-bound branch selectors bL, bU :X × Z →
{neu,mon,cor,def}(neutral, monotonic, correct, default), evaluated by first match:
bL(x, z) =



neuπ e(x) = ˆz0,S(x)̸=∅
monπ e(x)̸= ˆz0,S ↓(x, z)̸=∅
corπ e(x) =z,S ↓(x, z) =∅, C(x, z)̸=∅
defotherwise,
bU (x, z) =



neuπ e(x) = ˆz0,S(x)̸=∅
monπ e(x)̸= ˆz0,S ↑(x, z)̸=∅
corπ e(x)̸=z,S ↑(x, z) =∅,C(x, z)̸=∅
defotherwise.
Because each selector is a function evaluated by first match, it returns exactly one value, so the induced indicators
1{bL =k},1{b U =k}partition the space ofX × Z.
Theorem 4.1(Bounds).Under Assumptions 2.1 and 3.1 to 3.4, we have the following bounds on the impact of our untrialed
modelπ e:
L(πe)≤E[Y( ˆZ=π e(X), M=f M (X, πe))]≤U(π e)
Where:
L(πe) =E[1{b L =neu}E[Y|X,Π∈ S(X), Z](2)
+1{b L =mon}E[Y|X,Π∈ S ⇓(X, Z), Z]
+1{b L =cor}max
i∈C(X,Z)
E[Y|X,Π =i, Z]
+1{b L =def}Y min].(3)
U(π e) =E[1{b U =neu}E[Y|X,Π∈ S(X), Z]
+1{b U =mon}E[Y|X,Π∈ S ⇑(X, Z), Z]
+1{b U =cor}min i∈C(X,Z) E[Y|X,Π =i, Z]
+1{b U =def}Y max].(4)
C.1 PROOF OF THEOREM 4.1 (LOWER BOUND)
Since bL is a function defined by first-match cases (Def. 4.2), exactly one of the indicators 1{bL =k} ,
k∈ {neu,mon,cor,def} , equals 1, so they are mutually exclusive and exhaustive. We will sometimes omit the
arguments for brevity.
Thus the equality follows:
1 =1{b L =neu}+1{b L =mon}+1{b L =cor}+1{b L =def}(35)
We have the following:
E[Y( ˆZ=π e(X), M=f M (X, πe), Z=z)]
=E[E[Y( ˆZ=π e(X), M=f M (X, πe), Z=z)|X]](36)
=E[E[Y|X, ˆZ=π e(X), M=f M (X, πe), Z=z]](37)
=E[E[Y|X, ˆZ=π e(X), M=f M (X, πe), Z=z](1{b L =neu}+
1{bL =mon}+

1{bL =cor}+
1{bL =def})](38)
=E[1{b L =neu}E[Y|X, ˆZ=π e(X), M=f M (X, πe), Z=z]+(39)
1{bL =mon}E[Y|X, ˆZ=π e(X), M=f M (X, πe), Z=z]+(40)
1{bL =cor}E[Y|X, ˆZ=π e(X), M=f M (X, πe), Z=z]+(41)
1{bL =def}E[Y|X, ˆZ=π e(X), M=f M (X, πe), Z=z]](42)
Where Eq. (36) follows from the law of iterated expectations. Eq. (37) follows from conditional ignorability (Corollary B.2)
and the fact that under Assump. 2.1, Y(ˆz, m, z) =Y(ˆz, m)under the conditioning. Eq. (38) follows from Eq. (35).
Eq. (42)-Eq. (40) follow from distributing the expectation over the sum.
We will now demonstrate that each line is greater than or equal to the corresponding line in the lower bound.
Eq. (39) We use the analogous proof from Chen and Oberst [2025].
We first must demonstrateY⊥ ⊥M|X, ˆZ= ˆz0:
P(Y|X, ˆZ= ˆz0, M=m, Z=z) =P(Y( ˆZ= ˆz0, M=m, Z=z)|X=x, M=m, ˆZ= ˆz0, Z=z)(43)
=P(Y( ˆZ= ˆz0, M=m ′, Z=z)|X=x, M=m, ˆZ= ˆz0, Z=z)(44)
=P(Y( ˆZ= ˆz0, M=m ′, Z=z)|X=x, M=m ′, ˆZ= ˆz0, Z=z)(45)
=P(Y|X=x, ˆZ= ˆz0, M=m ′, Z=z)(46)
Where Eq. (43) follows from Corollary B.1. Eq. (44) follows from Assump. 3.3. Eq. (45) follows from the structure
of Assump. 2.1 implying Y(ˆz, m)⊥ ⊥M,ˆZ|X . Eq. (46) follows from Corollary B.1. Thus we have demonstrated
Y⊥ ⊥M|X, ˆZ= ˆz0.
Next, we recall that the lower selector takes the valueneuexactly when
bL =neu:π e(x) = ˆz0,S(x)̸=∅.
Thus we have:
1{bL =neu}E[Y|X, ˆZ=π e(X), M=f M (X, πe), Z=z]
=1{b L =neu}E[Y|X, ˆZ= ˆz0, M=f M (X, πe), Z=z](47)
=1{b L =neu}E[Y|X, ˆZ= ˆz0, Z=z](48)
=1{b L =neu}E[E[Y|X=x, ˆZ= ˆz0, Z=z]|X=x, ˆZ=π e(x),Π∈ S(x)](49)
=1{b L =neu}E[E[Y|X=x, ˆZ= ˆz0, M, Z=z]|X=x, ˆZ=π e(x),Π∈ S(x)](50)
=1{b L =neu}E[E[Y|X=x, ˆZ=π e(x), M, Z=z]|X=x, ˆZ=π e(x),Π∈ S(x)](51)
=1{b L =neu}E[E[Y|X=x, ˆZ=π e(x), M,Π∈ S(x), Z=z]|X=x, ˆZ=π e(x),Π∈ S(x)](52)
=1{b L =neu}E[Y|X=x, ˆZ=π e(x),Π∈ S(x), Z=z](53)
=1{b L =neu}E[Y|X=x,Π∈ S(x), Z=z](54)
Where Eq. (47) follows from implication of the indicators. Eq. (48) follows from Y⊥ ⊥M|X, ˆZ= ˆz0 demonstrated above.
Eq. (49) follows from the law of total expectation. Eq. (50) follows from Assump. 3.3. Eq. (51) follows from implication of
the indicators. Eq. (52) follows from Y⊥ ⊥Π|X, ˆZ, Mimplied by the structure of Assump. 2.1. Eq. (53) follows from the
law of total expectation. Eq. (54) follows from implication of the indicators.
Eq. (40) We have the following: First we recall that the lower selector takes the valuemonexactly when
bL =mon:π e(x)̸= ˆz0,S ↓(x, z)̸=∅.
Thus we have:
1{bL =mon}E[Y|X, ˆZ=π e(X), M=f M (X, πe), Z=z]

≥1{b L =mon}E[Y|X,Π∈ S ⇓(X, Z), Z=z](55)
Where Eq. (55) follows from Assump. 3.2 and the definition of S⇓(x) and the fact that it takes only the next-worst policies
and not all worse policies. Thus, we have that the expected value of the outcome under the untrialed model is greater than or
equal to the lower bound.
Eq. (41) We have the following:
We recall that the lower selector takes the valuecorexactly when
bL =cor:π e(x) =z,S ↓(x, z) =∅, C(x, z)̸=∅.
For alli∈ T, we have the following:
1{bL =cor}E[Y|X, ˆZ=π e(X), M=f M (X, πe), Z=z] =1{b L =cor}E[Y|X, ˆZ=z, M=f M (X, πe), Z=z]
(56)
≥1{b L =cor}max
i∈C(X,Z)
E[Y|X,Π =i, Z=z](57)
Eq. (56) holds by implication of the indicators. Eq. (57) follows by Assump. 3.1, sinceπe(x) =z , while every πi ∈ C(X, Z)
hasπ i(x)̸=zby definition, so each such model takes an incorrect prediction.
Eq. (42) We have the following:
1{bL =def}E[Y|X, ˆZ=π e(X), M=f M (X, πe), Z=z]≥Y min (58)
Which holds by Assump. 3.4.
C.2 PROOF OF THEOREM 4.1 (UPPER BOUND)
Analogous to the lower bound, bU is a function defined by first-match cases (Def. 4.2), so exactly one of the indicators
1{bU =k},k∈ {neu,mon,cor,def}, equals1, and they are mutually exclusive and exhaustive.
1 =1{b U =neu}+1{b U =mon}+1{b U =cor}+1{b U =def}(59)
From the previous computation, we have the following:
E[Y( ˆZ=π e(X), M=f M (X, πe), Z=z)] =E[1{b U =neu}E[Y|X, ˆZ=π e(X), M=f M (X, πe), Z=z]+(60)
1{bU =mon}E[Y|X, ˆZ=π e(X), M=f M (X, πe), Z=z]+(61)
1{bU =cor}E[Y|X, ˆZ=π e(X), M=f M (X, πe), Z=z]+(62)
1{bU =def}E[Y|X, ˆZ=π e(X), M=f M (X, πe), Z=z]](63)
Using the equivalent indicator statements established in Eq. (59), we have that each line is less than or equal to the
corresponding line in the upper bound.
Eq. (60) Identical to the proof in the lower bound.
Eq. (61) We recall that the upper selector takes the valuemonexactly when
bU =mon:π e(x)̸= ˆz0,S ↑(x, z)̸=∅.
Thus we have:
1{bU =mon}E[Y|X, ˆZ=π e(X), M=f M (X, πe), Z=z]

≤1{b U =mon}E[Y|X,Π∈ S ⇑(X, Z), Z=z](64)
Eq. (64) holds by Assump. 3.2 and the definition ofS ⇑(x, z)and conditional independence.
Eq. (62) We recall that the upper selector takes the valuecorexactly when
bU =cor:π e(x)̸=z,S ↑(x, z) =∅,C(x, z)̸=∅.
Thus, for alli∈ T, we have the following:
1{bU =cor}E[Y|X, ˆZ=π e(X), M=f M (X, πe), Z=z] =1{b U =cor}E[Y|X, ˆZ̸=z, M=f M (X, πe), Z=z]
(65)
≤1{b U =cor}min i∈C(X,Z) E[Y|X,Π =i, Z=z](66)
Eq. (65) holds by implication of the indicators. Eq. (66) follows from Assump. 3.1, since πe(x)̸=z while every
πi ∈ C(X, Z), we haveπi(x) =z.
Eq. (63) Holds by the definition ofY max.
Thus, we have that the expected value of the outcome under the untrialed model is less than or equal to the upper bound.

D PROOF OF THEOREM 5.1
Theorem 5.1(Consistency and asymptotic normality of bL(πe), bU(π e)).If Assumptions 5.1 to 5.3 hold for some α, β >0,
then
bL(πe) =n −1
nX
i=1
bψL(Yi, Xi,Π i, Zi; bfM ) P − →L(πe)
bU(π e) =n −1
nX
i=1
bψU (Yi, Xi,Π i, Zi; bfM ) P − →U(πe)
Where
P
− →denotes convergence in probability. Furthermore,
√n(bL(πe)−L(π e)) d − →N(0, σ2 L)
√n( bU(π e)−U(π e)) d − →N(0, σ2 U )
Where
d
− →denotes convergence in distribution, and σ2 L =Var(ψ L), σ2 U =Var(ψ U ), with ψL, ψU denoting the pseudo-
outcomes of Def. 5.2 evaluated with the true nuisance functionsµ j, fM in place of their estimates.
Proof. We first investigate the lower bound. Recall the following lines (Eq. (6), Eq. (7), Eq. (8), Eq. (9)). We also define
ˆµS(X, Z)as the estimator for E[Y|X,Π∈S, Z] =µ S(X, Z), and C(x, z)is the set of policies, indexed by i, whose
outputs do not agree with the true label atx.
Recall that conceptually, dL(X, Z)is the index of the model with the highest expected outcome among those that do not
agree with πe at X. S⇓(x, z)is the best-performing set of agreeing models with performance less than or equal to the
untrialed model.φ L

X, Z;ˆdL  is the estimator for the outcome under the model with indexd L(X, Z).
First, we will demonstrate that ˆL(πe) is a consistent estimator of L(πe), as follows. Recall our definition of the estimator
from Def. 5.2, using the sets defined in Def. 4.1 and Theorem 4.1:
bL(πe) =E n
h
bψL(Yi, Xi,Π i, Zi; bfM )
i
=E n
h
1{ˆbL =neu} ˆh(X, Y,S)(67)
+1{ ˆbL =mon} ˆh(X, Y,bS⇓)(68)
+1{ ˆbL =cor}φ L(X, Z;ˆd)
+1{ ˆbL =def}Y min
i
.
Where we use the following substitution for brevity:
ˆh(X, Y, S) :=

bµS(X, Z) + 1{Π∈S} P(Π∈S|X)  Y−bµ S(X, Z) 
Where we use Π to denote the random variable and T as its support. S is used to denote a subset of T , and π to denote an
instance ofΠ. (See Def. 4.1 where we defined notation).
We first demonstrate the following Lemma, in which h, φL, and dL denote the functionals of Definitions 5.1 and 5.2
evaluated with the true nuisance functionsµ j and true performancef M in place of their estimates:
Lemma D.1(Unbiased Estimator).
L(πe) =E[ψ L(Yi, Xi,Π i, Zi;f M )] =E
h
1{bL =neu}h(X, Y,S)
+1{b L =mon}h(X, Y,S ⇓)
+1{b L =cor}φ L(X, Z;d)
+1{b L =def}Y min
i
.

By linearity of expectation, we have:
=E
h
1{bL =neu}h(X, Y,S)
i
(69)
+E
h
1{bL =mon}h(X, Y,S ⇓)
i
(70)
+E
h
1{bL =cor}φ L(X, Z;d)
i
(71)
+E
h
1{bL =def}Y min
i
.(72)
For Eq. (69)-Eq. (71), each term consists of a regression term and a correction term as follows:
E[1{·}(µ(X, Z) +λ(X, Z))](73)
µis defined as the corresponding conditional expectation term in Theorem 4.1. Forλ:
E[1{·}λ(X, Z)] =E[E[1{·}λ(X, Z)|X, Z]]
=E[1{·}E[λ(X, Z)|X, Z]]
=E[1{·}0]
= 0
Where the first line follows by the tower property and the fact that the branch selector 1{·} is measurable with respect to
(X, Z). The second line follows from condition 2 of Lemma D.2. Thus, we have:
L(πe) =E[ψ L(Yi, Xi,Π i, Zi;f M )] =E
h
1{bL =neu}µ S (X, Z)
+1{b L =mon}µ S⇓ (X, Z)
+1{b L =cor}µ dL(X,Z) (X, Z)
+1{b L =def}Y min
i
.
Which is preciselyL(π e). The proof for the upper bound is analogous.
We have (omitting the arguments (Yi, Xi,Π i, Zi) for brevity, retaining only the performance function after the semicolon;
the unhattedψ L(·;f M )denotes the pseudo-outcome computed with the true nuisance functions and true performance):
bL(πe)−L(π e) =E n
h
bψL(Yi, Xi,Π i, Zi; bfM )
i
−E[ψ L(Y, X,Π, Z;fM )](74)
=E n
h
bψL(·; bfM )
i
−E n
h
bψL(·;f M )
i
| {z }
R1
+E n
h
bψL(·;f M )
i
−E[ψ L(·;f M )]
| {z }
R2
Where Eq. (74) follows from Lemma D.1.
We will demonstrate
bL(πe)−L(π e) =R 1 +R 2
=O P (n−1/2)
We will focus onR 2 first.
R2 = (En[1{bL =neu} ˆh(X, Y,S)]−E[1{b L =neu}E[Y|X,Π∈ S, Z]])| {z }
R2,1
+ (En[1{bL =mon} ˆh(X, Y,S⇓)]−E[1{b L =mon}E[Y|X,Π∈ S ⇓, Z]])| {z }
R2,2

+ (En[1{bL =cor}φ L(X, Z;ˆd)]−E[1{b L =cor}max
i∈C(X,Z)
E[Y|X,Π =i, Z]])
| {z }
R2,3
+Y min(En[1{bL =def}]−E[1{b L =def}])| {z }
R2,4
=R 2,1 +R 2,2 +R 2,3 +R 2,4
We will leave R2,4 as is. We will consider R2,3 first. We note that the proofs for R2,1, R2,2 are identical except for the sets S
being considered, as they can be interpreted as being a maximum over a subset of T that contains one element. For example:
E[1{bL =neu}E[Y|X,Π∈ S, Z]] =E[1{b L =neu}max j∈{1} E[Y|X,Π∈ S, Z]](75)
The termR 2,3 corresponds to the following branch in the lower bound:
E[1{bL =cor}max
i∈C(X,Z)
E[Y|X,Π =i, Z]]
We note this term has an “expectation of max” form. This structure has non-smooth properties that prevent straightforward
estimation via plugins or other methods. As a result, we can utilize an augmented inverse probability-weighted estimator.
Previous literature exists on similar topics. For example, Byun et al. [2024] considers a problem of using AIPW to estimate
the expected maximum of a set of functions. We will adapt their results to our setting.
Definition D.1.Consider the following class of estimators. Let θj(W;P), λj(W;P) for all j∈ {1, . . . , J}represent some
arbitrary set of smooth functions and their associated influence functions, where W is the observed data and P is the true
data distribution. Use of bP indicates the parameter was taken with respect to an estimated distribution. We further define the
following functionals:
θj :=E[θ j(W;P)](76)
bθj :=E n[θj(W; bP)](77)
ψ:=E

max
j∈{1,...,J}
θj(W;P)

=E

θd(W) (W;P)

(78)
d(W) := arg max
j∈{1,...,J}
θj(W;P)(79)
bψj :=E n[θj(W; bP) +λ j(W; bP)](80)
bψ:=E n[φ(W; bP ,bd)](81)
φ(W; bP ,bd) :=θ bd(W) (W; bP) +λ bd(W) (W; bP)(82)
bd(W) := arg max
j∈{1,...,J}
θj(W; bP)(83)
We note that these definitions are copied verbatim from Byun et al. [2024]. We can now state their main lemma:
Lemma D.2(Lemma 10 and 11 of Byun et al. [2024]).For the class of estimators defined in Def. D.1, if the following
conditions hold:
1. For everyj∈ {1, . . . , J}, λj(W;P)andθ j(W;P)are both uniformly bounded by constants with respect ton.
2. For everyj∈ {1, . . . , J},E[λj(W;P)] = 0
3. For everyj∈ {1, . . . , J},∥bθj −θ j∥=o P (1)
4. There existsα >0such that:P

minj̸=d(W) |θd(W) (W)−θ j(W)| ≤t

≲t α
5. In Eq.(81), the expectation is taken with respect to bP1, while the estimator φ(W; bP2, bd) uses an independent sample
bP2.
Then the following is true:
bψ−ψ=E n[φ(W;P, d)]−E[φ(W;P, d)](84)

+O P

∥bθj −θ j∥1+α ∞ + max j∈{1,...,J} E h θj(W; bP) +λ j(W; bP)−θ j(W;P) i (85)
+o P (n−1/2)(86)
If two additional conditions hold:
6.∥ bθj −θ j∥1+α ∞ =o P (n−1/2)
7. For eachj∈ {1, . . . , J},E[θj(W; bP) +λ j(W; bP)−θ j(W;P)] =o P (n−1/2)
Then the following simplification holds:
bψ−ψ=E n[φ(W;P, d)]−E[φ(W;P, d)] +o P (n−1/2)(87)
And the error is asymptotically normal:
√n( bψ−ψ) d − →N(0, V ar(φ(W;P, d)))(88)
We recognize that our problem fits into this framework with the following identifications:
W↔(X, Z)
θj(W;P)↔µ j(X, Z)
bθj(W; bP)↔ˆµ j(X, Z)
θj ↔E[µ j(X, Z)]
bθj ↔E n[ˆµj(X, Z)]
λj(W;P)↔λ j(X, Z)
d(W)↔d L(X, Z)
bd(W)↔ ˆd(X, Z)
J↔ C(x, z)
Where any unspecified functionals are defined analogously to their counterparts in Eq. (76) - Eq. (83). Here the conditioning
argument W of Byun et al. [2024] is identified with the pair (X, Z), since each branch of Theorem 4.1 conditions on (X, Z).
Because model assignment is randomized, Π⊥ ⊥Z|Xand hence P(Π =j|X, Z) =P(Π =j|X) , so the propensity
nuisance is unchanged and only the outcome regression µj acquires the Z argument. Thus, we can apply Lemma D.2 to our
setting,
Lemma D.3.Suppose the following conditions hold:
1. For everyj∈ C(x, z),λj(X, Z)andˆµj(X, Z)are both uniformly bounded by constants.
2.E[λ j(X, Z)|X, Z] = 0for allj∈ C(x, z).
3. For everyj∈ C(x, z),
|En[ˆµj(X, Z)]−E[µj(X, Z)]|=o P (1)
4. There existsα >0such that:
P

min
j̸=dL(X,Z)

µdL(X,Z) (X, Z)−µj(X, Z)

 ≤t  ≤t α
5. Independent samples are used forE n
h
bψL(Yi, Xi,Π i, Zi; bfM )
i
andφ L(X, Z;ˆd).
Then the difference between the estimator and the true parameter can be expressed as:
bψl −ψ l =E n[φL(X, Z;d)]−E[φ L(X, Z;d)]
+O P

∥En [ˆµj(X, Z)]−E[µj(X, Z)]∥1+α ∞ + max
j∈C(x,z)
E
h
bµj(X, Z) +ˆλj(X, Z)−µj(X, Z)
i!
+o P (n−1/2)
We can further simplify this with the following 2 additional conditions:

6. The following holds:
∥En[ˆµj(X, Z)]−E[µj(X, Z)]∥1+α ∞ =o P (n−1/2)
whereαis the same as in Assump. 5.2.
7. For eachj∈ C(x, z),
E[ˆµj(X, Z) +ˆλj(X, Z)−µj(X, Z)] =oP (n−1/2).
Thus the following holds:
bψl −ψ l =E n[φL(X, Z;d)]−E[φ L(X, Z;d)] +oP (n−1/2)
We will demonstrate the conditions hold forR 2,3.
1. (Boundedness): For everyj∈ C(x, z),λj(X, Z)andˆµj(X, Z)are both uniformly bounded by constants.
This is true by Assump. 3.4 and can be enforced by clipping the value of the nuisance function.
2. (Zero-mean Correction Term):E[λ j(X, Z)|X, Z] = 0for allj∈ C(x, z).
E[λj(X, Z)|X, Z] =E
 1{Π =j}
P(Π =j|X) (Y−g j(X, Z))

X, Z  (89)
= E[1{Π =j}(Y−g j(X, Z))|X, Z] P(Π =j|X) (90)
= P(Π =j|X, Z) (E[Y|X,Π =j, Z]−g j(X, Z)) P(Π =j|X) (91)
= (E[Y|X,Π =j, Z]−g j(X, Z))(92)
= 0(93)
Eq. (89) follows by the definition of λj(X, Z). Eq. (90) follows because the propensity is constant under the
conditioning. Eq. (91) follows because the expectation of the indicator is the probability of the event, and gj(X, Z)
is a constant under the conditions. Eq. (92) follows because randomized model assignment gives Π⊥ ⊥Z|X, so
P(Π =j|X, Z) =P(Π =j|X) and the ratio of propensities is one. Eq. (93) follows by the definition of gj(X, Z)as
a plug-in estimator forE[Y|X,Π =j, Z].
3. (Consistent Plug-in Estimator): For everyj∈ C(x, z),
∥En [ˆµj(X, Z)]−E[µj(X, Z)]∥=o P (1)
This will be satisfied by the validation of Condition 7, so discussion is deferred to there.
4. (Margin Condition): There existsα >0such that:
P

min
j̸=dL(X,Z)

µdL(X,Z) (X, Z)−µj(X, Z)

 ≤t  ≤t α
This condition asserts that the probability of a small gap between the outcome regressions µj of the best two models is
bounded polynomially. This holds by the first margin condition of Assump. 5.2.
5. (Independent Samples):
This holds by construction. As described in Appendix E, data are split into K≥2 folds, with all nuisance functions
(bµj and bfM , etc.) fit on the first and the bounds estimated on the second.

6. (Convergence of plug-in estimators)
∥En [ˆµj(X, Z)]−E[µj(X, Z)]∥1+α ∞ =o P (n− 1 2 ),whereαis the same as in Assump. 5.2.
This is stating that the maximum difference between the empirical expectation of our machine learning-derived
estimate from the true expected outcome, across all j, converges at oP (n− 1 2 ) rate. We will prove this by demonstrating
that all plug-in estimators converge sufficiently fast.
We want to show:
∀j,∥E n [ˆµj(X, Z)]−E[µj(X, Z)]∥1+α =o P (n− 1 2 )
Consider the following:
For eachj∈ C(x, z), we have:
En [ˆµj(X, Z)]−E[µj(X, Z)] =En [ˆµj(X, Z)]−E[ˆµj(X, Z)] +E[ˆµj(X, Z)]−E[µj(X, Z)](94)
= (En [ˆµj(X, Z)]−E[ˆµj(X, Z)]) + (E[ˆµj(X, Z)]−E[µj(X, Z)])(95)
Looking solely at the first term, we have:
En [ˆµj(X, Z)]−E[ˆµj(X, Z)] =1 n
nX
i=1
(ˆgj(Xi, Zi)−E[ˆg j(Xi, Zi)])(96)
√n(E n [ˆµj(X, Z)]−E[ˆµj(X, Z)]) d − →N(0, σ2)(97)
=⇒E n [ˆµj(X, Z)]−E[ˆµj(X, Z)] =Op(n− 1 2 )(98)
Which follows from the CLT.
The second term is the bias of the machine learning estimator. In order for the whole norm to converge atoP (n− 1 2 ),
we require this term to converge at a rate of oP (n− 1 2(1+α) ). For a reasonable α, such as α= 1 , this is satisfied by a
convergence rate ofo P (n− 1 4 ). It is reasonable to assume our model converges at this rate.
We now have:
∥O(n− 1 2 ) +o P (n− 1 2(1+α) )∥1+α ≤  ∥O(n− 1 2 )∥+∥o P (n− 1 2(1+α) )∥ 1+α (99)
≤2 α ∥O(n− 1 2 )∥1+α +∥o P (n− 1 2(1+α) )∥1+α (100)
=O(n − 1+α 2 ) +o P (n− 1 2 )(101)
=o P (n− 1 2 )(102)
Where Eq. (99) follows from the triangle inequality. Eq. (100) follows from the Cr inequality with r= 1 +α and the
constant gets absorbed. Eq. (101) evaluates the rates. Eq. (102) since α >0. Since this holds for all j∈ C(x, z), we
have shown our result.
7. (Convergence of bias-corrected estimator) For each
j∈ C(x, z),E
h
bµj(X, Z) +ˆλj(X, Z)−µj(X, Z)
i
=o P (n− 1 2 ).
Where C(x, z)is the set of models in the branch.
For clarity, we rewrite the full bias-corrected estimator as:
φL(X, Z;ˆd) =bµˆd(X, Z) + 1
n
π= ˆd
o
P(Π = ˆd|X) (Y−bµ ˆd(X, Z))
Thus, we have the following nuisance functions:
µj(X, Z), P(Π =j|X)

We will assume thatµ j(X, Z)converges at a rate ofoP (n− 1 4 ). We also assume thatP(Π =j|X)is known.
We have, for arbitraryj∈ C(x, z):
E
h
bµj(X, Z) +ˆλj(X, Z)−µj(X, Z)
i
=E

bµj(X, Z)−µj(X, Z) + 1{Π =j} P(Π =j|X) (Y−bµ j(X, Z))  (103)
=E

E

bµj(X, Z)−µj(X, Z) + 1{Π =j} P(Π =j|X) (Y−bµ j(X, Z))|X, Z 
(104)
=E

bµj(X, Z)−µj(X, Z) + 1 P(Π =j|X) E[1{Π =j}(Y−bµ j(X, Z))|X, Z] 
(105)
=E

bµj(X, Z)−µj(X, Z) +P(Π =j|X, Z) P(Π =j|X) E[(Y−bµ j(X, Z))|X,Π =j, Z] 
(106)
=E

bµj(X, Z)−µj(X, Z) +P(Π =j|X, Z) P(Π =j|X) (µj(X, Z)−bµj(X, Z)) 
(107)
=E

(bµj(X, Z)−µj(X, Z))

1− P(Π =j|X, Z) P(Π =j|X)  (108)
=E[(bµj(X, Z)−µj(X, Z)) (1−1)](109)
= 0(110)
=o P (n− 1 2 )(111)
Eq. (103) follows from Assump. 5.1. Eq. (104) follows from the law of iterated expectation. Eq. (105) follows because
the relevant expressions are constants under the conditioning. Eq. (106) follows from removing the indicator from
the definition of conditional expectation. Eq. (107) follows by the definition of µj(X, Z). Eq. (108) is an algebraic
rearrangement; Eq. (109) uses P(Π =j|X, Z) =P(Π =j|X) , which holds because randomized model assignment
givesΠ⊥ ⊥Z|X. Eq. (111) follows vacuously from the definition of convergence in probability.
Thus, we have verified Condition 7. This also verifies Condition 3. Since the bias corrected estimator converges at a
rate of oP (n− 1 2 ) to the true value, it follows that the uncorrected plug-in estimator is at least consistent, since the
correction term has mean 0.
We have thus verified all necessary conditions. As a result, the following equality holds:
R2,3 =E n[1{bL =cor}φ(X, Z; ˆd)]−E[1{b L =cor}φ(X, Z; ˆd)] +o P (n−1/2)
It follows that the same applies toR 2,1, R2,2, R2,4, since the ˆh(X, Y, S)functionals are identical in structure toφ(x, z;ˆd),
except for the subscript of ˆµ, which instead is a single nuisance function that converges to the true value at oP (n− 1 2 ) under
Assump. 5.3, allowing the whole function ˆh(X, Y, S)to converge atoP (n− 1 2 )rate under analogous logic.
Thus we have:
R2 =En[1{bL =neu}h(X, Y,S)]−E[1{b L =neu}h(X, Y,S)]+
En[1{bL =mon}h(X, Y,S⇓)]−E[1{b L =mon}h(X, Y,S⇓)]+
En[1{bL =cor}φ(X, Z;d)]−E[1{b L =cor}φ(X, Z;d)]+
En[1{bL =def}Y min]−E[1{b L =def}Y min] +o P (n−1/2)
We will now considerR 1 =E n
h
bψL(·; bfM )
i
−E n
h
bψL(·;f M )
i
:
The theoretical construction ofψ L involves the construction of the setS ↓(x, z), defined in Def. 4.1 as:
S↓(x, z) ={πi ∈ S(x)|fM (x, πi)≤f M (x, πe), πe(x) =z}

∪ {πi ∈ S(x)|fM (x, πi)≥f M (x, πe), πe(x)̸=z}
Where fM (x, πi) is the true performance of model πi at covariate x. If we instead use the estimated performance bfM to
construct the set, as in Def. 5.1, we have:
bS↓(x, z) ={πi ∈ S(x)| bfM (x, πi)≤ bfM (x, πe), πe(x) =z}
∪ {πi ∈ S(x)| bfM (x, πi)≥ bfM (x, πe), πe(x)̸=z}
However, we only concern ourselves with the model(s) whose performance is closest to that of the untrialed model, per
Definitions 4.1 and 5.1:
S⇓(x, z) = arg min
πi∈S↓(x,z)
|fM (x, πi)−f M (x, πe)|
bS⇓(x, z) = arg min
πi∈ bS↓(x,z)
| bfM (x, πi)− bfM (x, πe)|
However, error in our estimation may permute the ordering of the models relative to the untrialed model, in terms of their
estimated performance, resulting in:
bS⇓(x, z)̸=S ⇓(x, z)
This leads to two distinct cases:
1. Case 1: bS⇓(x, z) =S⇓(x, z)
2. Case 2: bS⇓(x, z)̸=S ⇓(x, z)
In case 1, we have that:
bψL(·; bfM ) = bψL(·;f M )
Since bψL depends on the performance function only through the set S⇓(x, z). If the estimates have no impact on the set, then
the estimates have no impact on the value of bψL. In case 2, we know that the error is bounded:

 bψL(·;f M )− bψL(·; bfM )

 ≤
|Ymax −Y min|=B, by Assump. 3.4. 2
To prove convergence, we utilize the second margin condition of Assump. 5.2: there existsβ >0 such that for any t≥0 ,
we have:
P

min
i̸=j
|fM (x;π j)−f M (x;π i)| ≤t

≤t β
For allx∈ Xandπ i, πj ∈ T ∪ {πe}.
This condition states that the probability that the minimum performance gap between any two models is less than t decays at
least polynomially in t. Under this assumption, we can show that the first term converges to 0 as n→ ∞by demonstrating
the indicator converges to 0:
We first define:
δn := 2 max i

fM (x;π i)− bfM (x;π i)

 ∞
g(X) := min
i,j
|fM (X;π i)−f M (X;π j)|
It follows that:
|R1| ≤En
h
| bψL(·; bfM )− bψL(·;f M )|
i
(112)
=E n
h
|1
n
bS⇓(X, Z)̸=S ⇓(X, Z)
o 
bψL(·; bfM )− bψL(·;f M )

|
i
(113)
≤E n
"
|1

min
i,j
|fM (X;π i)−f M (X;π j)| ≤2 max i

fM (x;π i)− bfM (x;π i)

 ∞ 
2This assumption is technically stronger than necessary, as only sufficient separation between the performance of the two closest
models withπ e on both sides is necessary.


bψL(·; bfM )− bψL(·;f M )

|
#
(114)
=E n
"
|1{g(X)≤δ n}

bψL(·; bfM )− bψL(·;f M )

|
#
(115)
≤E n
"
|1{g(X)≤δ n}B|
#
(116)
=E n
"
1{g(X)≤δ n}
#
B(117)
Where B is an arbitrary constant, πi, πj ∈ T ∪ {πe}. Eq. (112) is Jensen’s inequality. Eq. (113) follows because the
difference is only non-zero when the sets differ. Eq. (114) follows because the sets differ only when model error causes
permutations in the ordering of πe and the 2 closest performing models on either side. This occurs when the estimation error
is larger than half of the minimum distance between the untrialed model and any other model, as maximum error in both
values can “bridge the gap”. Eq. (115) is by the definitions of δn and g(X). Eq. (116) follows from the boundedness of the
difference from Assump. 3.4, where B=Y max −Y min. Eq. (117) follows because the indicator is non-negative. From here,
we cannot directly apply the margin condition of Assump. 5.2, because the expectation is empirical; instead, we have:
P
√n|R 1|> ϵ  ≤P  En  1{g(Xi)≤δ n}  ≥ ϵ B√n  (118)
≤E

En

1{g(Xi)≤δ n}
 B√n
ϵ (119)
=E

1
n
nX
i=1

1{g(Xi)≤δ n}

!
B√n
ϵ (120)
=P(g(X i)≤δ n) B√n ϵ (121)
≤δ β n B√n ϵ (122)
− →0.(123)
Eq. (118) uses |R1| ≤BEn[1{g(Xi)≤δ n}]. Eq. (119) follows from Markov’s inequality. Equation (120) is by definition.
Eq. (121) is by linearity of expectation. Eq. (122) follows from the margin condition (Assump. 5.2), and Eq. (123) follows
since δn =o P (n− 1 2β ) by Assump. 5.3, so δβ n √n→0 in probability. Because this holds for every ϵ >0, R1 =o P (n−1/2).
We note thatthis is differentthan the required convergence rate for the plug-in estimators for µj(X, Z), which was
oP (n− 1 2(1+α) ). This is because in Byun et al. [2024], or our 6th condition of Lemma D.3, at the step analogous to Eq. (114),
the term in the right hand side inside of the indicator is the same as the term outside of the indicator. After application
of the margin condition, this results in a squared convergence rate. In our case, the term outside of the indicator is B, a
constant, which does not converge. We are unable to improve this, since the convergence of bfM is not necessarily related to
the convergence of bψL, whose error is bounded byB. We have now shown:
bL(πe)−L(π e) =En[1{bL =neu}h(X, Y,S)]−E[1{b L =neu}h(X, Y,S)]+
En[1{bL =mon}h(X, Y,S⇓)]−E[1{b L =mon}h(X, Y,S⇓)]+
En[1{bL =cor}φ(X, Z;d)]−E[1{b L =cor}φ(X, Z;d)]+
En[1{bL =def}Y min]−E[1{b L =def}Y min]
+o P (n−1/2) +o P (n−1/2)| {z }
R1
(124)
=En[1{bL =neu}h(X, Y,S) +1{b L =mon}h(X, Y,S⇓)+(125)
1{bL =cor}φ(X, Z;d) +1{b L =def}Y min]−(126)
E[1{bL =neu}h(X, Y,S) +1{b L =mon}h(X, Y,S⇓)+(127)
1{bL =cor}φ(X, Z;d) +1{b L =def}Y min](128)
+o P (n−1/2)(129)

In Eq. (124), the term outside the underbrace corresponds to R2. In Eq. (129), we have the difference of an empirical mean
and the corresponding true mean. By the CLT, this is a random variable that converges to a normal distribution. By Slutsky’s,
theo P (n−1/2)terms vanish asymptotically.
It directly follows that since bL(πe)is an empirical function of i.i.d. random variables, we can apply the CLT to show that:
√n(bL(πe)−L(π e))∼N  0, σ2 L  (130)
By the CLT, whereσ 2 L =V ar(ψL). It follows:
Corollary 5.1(Confidence Intervals for L(πe), U(πe)).Under the conditions of Theorem 5.1, we can construct the following
confidence intervals forL(π e), U(πe):
bL(πe)±z 1−γ/2
q
dV ar(bψL)/n
bU(π e)±z 1−γ/2
q
dV ar(bψU )/n
Where z1−γ/2 is the 1−γ/2 quantile of the standard normal distribution, and dV ar(bψL), dV ar(bψU ) are the empirical
variance of bψL, bψU , respectively.
Proof. By Theorem 5.1,√n(bL(πe)−L(πe)) d − →N(0, σ2 L) with σ2 L =Var(ψ L). We must show cVar(bψL) P − →σ2 L. Decompose
cVar(bψL)−Var(ψ L) = cVar(bψL)−Var( bψL)| {z }
(A)
+Var( bψL)−Var(ψ L)| {z }
(B)
.
For term (A), bψL is uniformly bounded by a constant independent of n: Assump. 3.4 bounds Y∈[Y min, Ymax], and the
influence terms bλj are bounded by Condition 1 of Lemma D.3. Under cross-fitting, the evaluation-fold observations are
i.i.d. conditional on the training fold, on which bψL is a fixed bounded function; a law of large numbers for this bounded
conditionally-i.i.d. sample therefore gives cVar(bψL)−Var( bψL) =o P (1), so(A) =o P (1).
For term (B), the rate condition Assump. 5.3 and margin condition Assump. 5.2 give bψL P − →ψL (as established in the proof
of Theorem 5.1). Since bψL is uniformly bounded, the bounded convergence theorem upgrades convergence in probability to
moment convergence,E[ bψL]→E[ψ L]andE[ bψ2 L]→E[ψ 2 L], hence Var(bψL)→Var(ψ L)and(B) =o P (1).
Thus, cVar(bψL) P − →σ2 L, and by Slutsky’s theorem the interval attains asymptotic coverage1−γ.
We now consider the upper bound.
U(π e) =E[1{b U =neu}E[Y|X,Π∈ S(X), Z]
+1{b U =mon}E[Y|X,Π∈ S ⇑(X, Z), Z]
+1{b U =cor}min i∈C(X,Z) E[Y|X,Π =i, Z]
+1{b U =def}Y max].
Where the sets in the indicators are defined as they are in Theorem 4.1. We note that the structure of this expression is
identical to that of the lower bound, except for the use of minima instead of maxima, and the different definitions of the sets
in the indicators. Since the proof was agnostic to the specific definitions of the sets, and a minimum can be interpreted as a
maximum over negative values, the proof follows identically.

(a)
 (b)
 (c)
 (d)
Figure A.1: Ablation study of generated bounds on downstream outcomes. The figure displays the lower bound and upper
bound computed using our proposed method in Fig. A.1a, the existing method in Chen and Oberst [2025] using performance
stratified across age groups in Fig. A.1b, the existing method using AIPW estimation in Fig. A.1c, and the existing method
without any modifications in Fig. A.1d. 90% two-sided confidence intervals are shown.
Figure A.2: The figure displays the lower and upper bound computed with our method using the true theoretical values, as if
we had access to the counterfactual outcomes for all models.
E FURTHER SIMULATION DETAILS
Method Bound width Lower (mean) Lower 90% CI Upper (mean) Upper 90% CI True value
Our Method 0.331 0.430 [0.409, 0.451] 0.761 [0.742, 0.781] 0.726
True Bounds (oracle) 0.315 0.437 – 0.751 – 0.726
Chen et al., 2025 (fM (x, π)stratified) 0.704 0.153 [0.139, 0.166] 0.857 [0.837, 0.877] 0.726
Chen et al., 2025 (AIPW) 0.700 0.153 [0.139, 0.166] 0.852 [0.837, 0.867] 0.726
Chen et al., 2025 (unchanged) 0.704 0.153 [0.139, 0.166] 0.857 [0.837, 0.877] 0.726
Table A.1: (Experiment 1) Numerical summary of the ablation study results.
The experimental trial consisted of 1,891 defendants from the dataset whose various covariates, such as demographics,
charge history, and staff recommendations were recorded. The original dataset also contained an indicator of whether the
judge was shown the risk score predicted by the Public Safety Assessment (PSA) model, the judge’s detention decision, and
the outcome of whether the defendant failed to appear in court (FTA). We use these data to construct all the variables in our
RCT, as outlined in the experiments section of the main text.
In the original setting of Imai et al. [2023], judges were able to give high or low bail, and models provided integer risk scores
on a scale of 1-6 on not only FTA, but also new criminal activity and new violent criminal activity. The score is also always
shown to the judge. Our method is still applicable to these settings, however we choose to artificially binarize the model

Experiment Bounds Bound width Lower (mean) Lower 90% CI Upper (mean) Upper 90% CI True value
Experiment 3 Estimated 0.140 0.624 [0.607, 0.641] 0.764 [0.749, 0.779] 0.696
Experiment 3 Ground truth 0.144 0.615 – 0.760 – 0.696
Experiment 5 Estimated 0.204 0.586 [0.568, 0.604] 0.790 [0.776, 0.804] 0.697
Experiment 5 Ground truth 0.209 0.578 – 0.787 – 0.697
Table A.2: Semi-synthetic experiment results comparison between experiment 3 and experiment 5, which differ only in the
presence of missing data.
prediction and modify the setting to an alerting context so that a meaningful neutral action (ˆz0) exists. We chose to binarize
the judge’s decision and omit the other scores largely for simplicity.
Van Amsterdam et al. [2025] discusses a setting in which performance is dependent on the data distribution on which it is
measured. Thus, under a performance-dependent intervention, the dataset will shift, causing confounding that may lead to
orthogonal changes between potential outcomes and performance. We highlight this due to its similarity to our setting, but
emphasize that it does not apply. This is because performance is not measured relative to the potential outcomes, but instead
relative to counterfactual outcomes that do not change with any interventions.
The nuisance models used to learn the relationships in the data to simulate judge decisions and outcomes were simple
logistic regressions, without any feature engineering outside of the existing features in the dataset. The nuisance models
used in the AIPW estimation were lasso regularized linear regressions with cross-validatedL 1 penalty.
E.1 ADDITIONAL EXPERIMENT DETAILS
We now present additional details to some of the experiments discussed. We present some of the figures for each experiment,
but any graphs and tables presented have analogous versions for every experiment. They are available in the GitHub
repository. In no experiment do the falsification tests fail.
Experiment 1Suppose the alerting model discussed in Experiment 3 already exists and a two-arm RCT was conducted
comparing the FTA of the alerting model against a control arm (never alert). We are considering lowering the threshold of
the alerting model so that it alerts when the same risk score is >1 instead, without running an RCT. We use our method to
develop bounds on the downstream FTA from the data in the two-arm RCT.
We use the same experimental setup as in Experiment 3, except that we now have an additional trialed model. Thus, we
first randomly assign each defendant to either the control arm (never alert) or the trialed model (alert if risk score > 3). The
values ofA, Yare generated only for the appropriate model per the random assignment.
We show our results of this experiment in Fig. A.3. We see that our bounds remain tighter than the existing methods, though
both are significantly wider than in Experiment 4. The difference between the two methods is also less pronounced. This
is because the additional trialed model decreases the likelihood that the untrialed model disagrees with all trialed models,
which activates the 1{bL =cor},1{b U =cor} terms less often. This demonstrates that our method is more effective in
settings with more limited data, and has diminishing returns as the number of trialed models increases.
Experiment 2Suppose a model that alerts for offenders with a Imai et al. [2023] risk score greater than 3 already exists,
and a two-arm RCT was conducted comparing the FTA of the alerting model against a control arm (never alert). We develop
a new model that still alerts when the risk score is >3 ; however, it generates those risk scores in a fundamentally different
way. We want to evaluate the effectiveness of the new risk score algorithm without running an RCT. We use our method to
develop bounds on the downstream FTA from the data in the two-arm RCT.
We first randomly assign each defendant to either the control arm (never alert) or the trialed model (alert if risk score > 3).
The values of A, Yare generated only for the appropriate model per the random assignment. The untrialed model doesn’t
use the risk scores from the Imai et al. [2023] data. Instead, it finds the top 5 non-demographic features most correlated with
FTA in the data. It then does a simple tally of the number of those features that are present for a given defendant, and uses
that as the risk score, where 0 features present corresponds to a risk score of 1, and 5 features present corresponds to a risk
score of 6.
We show the results of this experiment in Fig. A.4. We see that our bounds are somewhat looser but still comparable to the

bounds in Fig. A.3. This demonstrates that our method still remains more effective than existing methods even when the
trialed model is fundamentally different from the untrialed model.
Experiment 5This experiment is identical to Experiment 3, but with missing values of Z. Z is defined as the counterfactual
outcome under no bail from the judge. Thus, it is only observed for individuals where A= 0 , but never observed for
individuals where A= 1 . In this experiment, we set all values of Z for such individuals to Z=−1 , which prevents the
logic in 1{bL =cor},1{b U =cor},1{b L =mon},1{b U =mon} from activating. As discussed in Appendix G.1, this is a
possibly misspecified experiment.
We see that our bounds are somewhat looser but still comparable to the bounds in Fig. 2. They remain tighter than the
existing methods, which are not affected by the missingness of Z. We see that in this case, the violation of MAR does
not significantly affect the bounds. This is because the fallback to 1{bL =def},1{b U =def} branches remain valid, the
1{bL =neu},1{b U =neu} branches for missing Z values are only impacted through the estimation of µ(X, Z), and the
1{bL =cor},1{b U =cor},1{b L =mon},1{b U =mon} branches do not get activated sufficiently to significantly affect
the bounds.

Figure A.3: (Experiment 1) Bounds on downstream outcomes for an untrialed model with two trialed models in the RCT,
plotted as functions of individual age.

Figure A.4: (Experiment 2) Bounds on downstream outcomes for an untrialed model under a covariate tally alerting rule,
plotted as functions of age.

Figure A.5: (Experiment 4) Bounds on downstream outcomes for an untrialed model with a single trialed model in the RCT,
plotted as functions of age.

Figure A.6: (Experiment 5) Bounds on downstream outcomes for an untrialed model with a single trialed model in the RCT,
plotted as functions of age, with missing data.

Patient_ID age_group UPPER LOWER UPPER (ground-truth) LOWER (ground-truth) TRUE_EXPECTED
0 4 1.000 1.000 0.681 0.681 0.681
1 4 0.909 0.000 0.651 0.000 0.652
2 3 1.000 1.000 0.818 0.818 0.818
3 2 1.000 0.909 1.000 0.472 0.476
4 2 1.000 1.000 0.777 0.777 0.777
5 4 1.000 1.000 0.715 0.715 0.715
6 3 1.000 0.000 0.612 0.000 0.613
7 2 0.091 0.000 0.672 0.000 0.672
8 3 1.000 1.000 0.687 0.687 0.687
9 4 1.000 0.000 0.676 0.000 0.677
10 2 0.091 0.000 0.665 0.000 0.666
11 4 1.000 0.000 1.000 0.570 0.572
12 2 1.000 1.000 1.000 0.647 0.649
Table A.3: The bound values generated for the first 13 individuals in the dataset (Experiment 3). The UPPER and LOWER
columns refer to the values of the upper and lower bounds generated using this paper’s method. These sometimes fall outside
[0,1] or fail to capture the true value due to estimation error. The ground truth columns are the bounds generated using
the true theoretical values. The TRUE_EXPECTED column is the true expected outcome for the individual, which was
unknown to the methods.
Method Outcome cov. Interval width Lower CI cov. Lower CI width Upper CI cov. Upper CI width
Our Method 1.00 0.313 0.97 0.042 0.91 0.039
True Bounds (oracle) 1.00 0.315 – – – –
Chen et al. (fM (x, π)) 1.00 0.692 0.00 0.027 0.00 0.039
Chen et al. (unchanged) 1.00 0.692 0.00 0.027 0.00 0.039
Chen et al. (AIPW) 1.00 0.693 0.00 0.027 0.00 0.031
Table A.4: Monte Carlo coverage and width across 100 seeds (Experiment 1). The Outcome cov. column is how often the
final bound interval [lower, upper] covers the true outcome. The Lower/Upper CI cov.: how often the two-sided 90% CI
around the lower (resp. upper) bound covers the true lower (resp. upper) bound. Widths are means.

Policy Precision Alert fraction
Control – 0.000
R>10.349 0.802
R>30.456 0.281
CustomRiskScore 0.413 0.456
Table A.5: Overall precision and alert frequency of each alerting policy used across the experiments, evaluated on the full
dataset (n= 1891 ). The alert fraction is the proportion of defendants for whom the policy raises an alert. Precision is the
fraction of raised alerts for which the defendant would fail to appear if released. The Control policy never alerts, so its
precision is undefined (-). “R>1 ” and “R>3 ” are the models that threshold the Imai et al. [2023] PSA failure-to-appear
risk score, and CustomRiskScore is the custom alerting system introduced in Experiment 2.
FTAScore Count Proportion
1 375 0.198
2 531 0.281
3 454 0.240
4 286 0.151
5 189 0.100
6 56 0.030
Table A.6: Baseline distribution of the Imai et al. [2023] PSA failure-to-appear risk score (integer values 1–6) across all
defendants in the dataset (n= 1891). This is the score thresholded by theR>1andR>3policies in Table A.5.
F RELATED WORK
Offline Policy EvaluationOur work is related to offline policy evaluation [Su et al., 2020, Wu et al., 2023, Rothfuss et al.,
2023, Namkoong et al., 2020]. If we interpret a model as a deterministic policy that dictates treatments, we are seeking to
evaluate the effectiveness of a new decision-making policy, using recorded outcomes under different policies. However, our
work differs due to the presence of a human decision-maker, whose compliance with the policy is dependent on many factors
such as their perception of the policy’s effectiveness. Furthermore, in offline policy evaluation, if the unknown policy makes
a prediction not present in data, we cannot estimate its effect due to a positivity violation. However, our setting specifically
focuses on using counterfactual correctness to resolve this situation.
Transportability and Z-IdentificationTransportability studies compute the causal effect of an intervention in a “target”
environment from data on the same intervention in a “source” environment. The two environments differ structurally, often
due to a selection node [Pearl, 2015, Mao et al., 2022, Shi et al., 2023, Lal et al., 2023, Stuart et al., 2011, Pearl and
Bareinboim, 2011]. Conversely, Z-identification studies compute the causal effect of an intervention based on data of a
different intervention in the same environment [Correa and Bareinboim, 2020b, Bareinboim and Pearl, 2012, Lee et al.,
2019, Correa and Bareinboim, 2020a]. We are related to both fields, but more closely to z-identification, as we are estimating
the causal effect of an untrialed model (different intervention) deployed in the existing environment of the RCT. We differ
from both approaches in that we make parametric assumptions, like monotonicity, and our goal is not to give conditions for
unbiased point estimation from infinite data. Instead, we give an interval containing the effect from finite data when the
above algorithms preclude unbiased point estimation.
Partial IdentificationPartial identification is concerned with bounding causal effects when point estimation is impossible.
It begins with Manski’s assumption-free natural bounds and progresses to sharper bounds under graphical assumptions via
linear and polynomial programming [Manski, 1990, Robins, 1989, Chickering and Pearl, 1996, Balke and Pearl, 1994, 1997,
Richardson et al., 2014, Zhang and Bareinboim, 2021a,b, Bellot, 2024, Bellot and Chiappa, 2024, Duarte et al., 2024]. We
differ from these approaches because our bounds use non-graphical assumptions pertinent to the application (as well as
graphical assumptions), and we use experimental (interventional) data instead of observational data. Furthermore, the causal
effect we bound occurs in a structurally different environment.
Evaluation of Machine Learning Models under Distribution ShiftDistribution shift occurs when the environment
in which a model is deployed differs structurally (not randomly) from the environment in which it is trained, violating
the assumption that train and test sets are identically distributed [Taori et al., 2020, Hendrycks et al., 2021, Wiles et al.,
2022, Koh et al., 2021, Miller et al., 2021]. In our setting, the presence of a human decision-maker causes the deployment

Bound Branch Experiment 1 Experiment 2 Experiment 3 Experiment 4 Experiment 5
Lower def 698 (36.91%) 238 (12.59%) 289 (15.28%) 987 (52.19%) 406 (21.47%)
Lower cor 529 (27.97%) 356 (18.83%) 242 (12.80%) 529 (27.97%) 125 (6.61%)
Lower neu 375 (19.83%) 1028 (54.36%) 1360 (71.92%) 375 (19.83%) 1360 (71.92%)
Lower mon 289 (15.28%) 269 (14.23%) 0 (0.00%) 0 (0.00%) 0 (0.00%)
Upper def 287 (15.18%) 124 (6.56%) 242 (12.80%) 529 (27.97%) 372 (19.67%)
Upper cor 987 (52.19%) 507 (26.81%) 289 (15.28%) 987 (52.19%) 159 (8.41%)
Upper neu 375 (19.83%) 1028 (54.36%) 1360 (71.92%) 375 (19.83%) 1360 (71.92%)
Upper mon 242 (12.80%) 232 (12.27%) 0 (0.00%) 0 (0.00%) 0 (0.00%)
Table A.7: Frequency of each bound branch across all individuals (n= 1891 ) for Experiments 1–4 (fully observed Z) and
Experiment 5 (Experiment 3 with missing Z). Each cell reports the count of individuals and, in parentheses, the percentage;
each individual activates exactly one lower and one upper branch.
environment to be differently distributed than the training environment, because the human can choose to implement a
different action from the machine’s suggestion. We overcome this challenge by making assumptions about how the human
will act, and the RCT data that we learn from is unconfounded.
Learning to DeferIn our work, we mention deferral as a possible example of a neutral outcome. Our setting is closely
related to learning to defer, in which an AI classifier may abstain on a given input and pass the decision to a human
expert, with the goal of training the classifier to complement rather than duplicate the human [Verma and Nalisnick, 2022,
Mozannar et al., 2023]. Like our work, L2D recognizes that the human decision-maker, not the model, is the final arbiter
of the outcome, and that the two should be modeled jointly. However, L2D differs from our setting in several respects.
First, L2D is concerned more with specifically how to train models, while our work focuses on the evaluation of already
trained models. Second, L2D models an explicit, learnable rejector that routes each input to either the model or the human,
while in our setting the human’s response to a model prediction is unobserved and mediated by their trust in the model’s
perceived performance. Finally, L2D typically assumes the human prediction is available on deferred examples, whereas our
framework must reason about counterfactual outcomes that are never directly observed.
G MISSING DATA
In the main text, we assume that Z is observed for all subjects, and derive our results in that context. In many practical
settings, however, Z may be missing for some subjects, due to limitations of data collection and/or due to being defined in
counterfactual terms (e.g., in our motivating example for the semi-synthetic experiments,Z is a counterfactual FTA indicator
that is unobserved when bail is granted).
In this section, we discuss an example missingness structure under which our method remains valid. We limit our discussion
to a simple missingness mechanism, to demonstrate how our method can hold under missingness. There may exist more
interesting and unique structures in which our method remains valid. However, we leave the exploration of these structures
to future work.
Let R∈ {0,1}be an observation indicator with R= 1 when Z is observed and R= 0 otherwise, so the analyst observes
(X,Π, ˆZ, M, Y, R, Z)rather than fully observingZ.
Suppose we have the augmented DAG in Fig. A.7, which is a simple extension of the DAG in Fig. 1a to include the
missingness indicatorR, where:
R=f R(X, ϵR), ϵ R ⊥(ϵ XZ , ϵY , . . .).
The analyst observes(X,Π, ˆZ, M, Y, R)and observesZonly whenR= 1.
We define augmented versions of our bounds, L′(πe) and U ′(πe), where L′(πe)≤L(π e) and U ′(πe)≥U(π e). In
these augmented versions, we modify the definitions of 1{bL =cor},1{b U =cor},1{b L =mon},1{b U =mon} to
additionally require R= 1 , so that these branches are only activated when Z is observed. Thus, for individuals with
R= 0 , the only branches that can activate are 1{bL =def},1{b U =def},1{b L =neu},1{b U =neu} . The branches
1{bL =def},1{b U =def} take the constant values Ymin, Ymax; under Assump. 3.4 they are always valid, and can only
loosen the inequality, never violate it, regardless of the missingness mechanism. The branches 1{bL =neu},1{b U =neu} ,

Π
D
ˆZ Y M
X Z A
R
Figure A.7: Augmented version of Fig. 1a including missingness. Node styles and edge colors follow Fig. 1a.
however, require estimation of a nuisance function:
ˆh(X, Y, Z,S) =bµS (X, Z) + 1{Π∈ S} P(Π∈ S |X)  Y−bµ S (X, Z)  ,
which references the individual’sZthroughbµ S (X, Z)and is therefore not directly computable whenZis missing.
To resolve this, we consider the neutral contribution to the population bound, noting that the neutral selector is a function of
Xonly. Let
•b(X) :=1{b L =neu}(X)— a function ofXonly,
•g(X, Z) :=E[Y|X,Π∈ S, Z]— a function of(X, Z).
Thus, the neutral contribution to the lower bound is E

b(X)g(X, Z)

, where the expectation is taken over the joint
distribution of (X, Z). We consider only the lower bound, but the upper bound is identical. Becauseb(X) depends on X
alone, the law of iterated expectations gives
E

b(X)g(X, Z)

=E

E[b(X)g(X, Z)|X]

=E

b(X)E[g(X, Z)|X]

.
From the randomization we haveΠ⊥Z|X, so the inner term satisfies
E[g(X, Z)|X] =E

E[Y|X,Π∈ S, Z]|X

=E

E[Y|X,Π∈ S, Z]|X,Π∈ S

=E[Y|X,Π∈ S].
We then define ν(X) :=E[Y|X,Π∈ S] . Since ν(X) depends only on X, it can be estimated regardless of whether Z is
observed, and we estimatebν(X)in place ofbµS (X, Z). Thus the neutral term of our estimator becomes
ˆhmarg(X, Y,S) =bν(X) + 1{Π∈ S} P(Π∈ S |X)  Y−bν(X)  .
We use that estimator for all individuals. For the other branches on the individuals with R= 1 , we must show that the
nuisance functions in Theorem 5.1 do not become inconsistent under missingness. To estimate our bounds, we require
nuisance functions of the form E[Y|X,Π =π j, Z]. This cannot be estimated directly, since Z is missing for R= 0
subjects; instead, we can only estimate
E[Y|X,Π =π j, Z, R= 1].
Because in Fig. A.7 we haveR=f R(X, ϵR)withϵ R independent of the rest, it follows that
R⊥(Z, Y)|X⇒R⊥Y|X,Π, Z,
and therefore
E[Y|X,Π =π j, Z, R= 1] =E[Y|X,Π =π j, Z] =µ j(X, Z).
For the fitted bµj to be consistent, and for the margin and rate conditions of Theorem 5.1 to carry over, the observed- Z
subsample must be representative of the populationX-support. This requires the following assumption:

Assumption G.1(Missingness Positivity).There exists η >0 such that πR(x) :=P(R= 1|X=x)≥η for all x∈ X.
This prevents missingness structures in which Z is never observed for some values of X. For example, in a diagnostic
context, if Z were never observed for patients above age 80, the assumption would be violated. Under these conditions, the
nuisance functions estimated on the R= 1 subset converge to the original nuisance functions, and our estimator remains
consistent. The model-assignment propensity P(Π|X) is fixed by RCT design and does not involve R, so Assump. 5.1 is
unaffected; under Assump. G.1 the observed-Z subsample shares the population X-support, so the margin conditions and
nuisance rates transfer, with the observed fraction affecting only the constant in the rate. Therefore, under this missingness
structure and Assump. G.1, bL′(πe) and bU ′(πe) are consistent and asymptotically normal (Theorem 5.1) for the valid bounds
L′(πe)≤E[Y(π e)]≤U ′(πe).
G.1 RELATION TO EXPERIMENT 5
In Experiment 5, these conditions are clearly not satisfied. The missingness of Z depends directly on the value of A. In this
experiment, Z is defined as the counterfactual outcome under no judge intervention, when it is available. When A= 1 , the
judge gives bail to the defendant, and Z is never observed. Conversely, when A= 0 , the judge does not give bail to the
defendant, andZis always observed.
This clearly does not match the missingness structure described in Fig. A.7 and violates Assump. G.1. Regardless, as
mentioned, we run it for demonstration purposes.
G.2 SPECIFIC VIOLATED ASSUMPTIONS
We also discuss how our method can handle violations of specific assumptions posited in our method. Since each branch
corresponds to a specific assumption, if any of the assumptions is violated, the corresponding indicator and its branch can be
removed from the bounds. This would cause any values ofxthat would have activated the branch to activateb L/bU =def
instead, resulting in a valid albeit looser bound. For example, if we are in a diagnostic setting, and there is no adequate
neutral action (model cannot defer to physician), then we have violated Assump. 3.3, but we can run the method as is, since
the neutral branches (bU =neu , bL =neu ) will never activate regardless, and the bounds will be constructed using the other
assumptions. Under violations of Assump. 3.1 or Assump. 3.2, the corresponding branches (1 or 2, respectively) can instead
default toY min, Ymax bounds, maintaining validity, which trivially follows from Assump. 3.4.

H FLOWCHART
X
Agreers
exist?
Neutral
prediction? bL =neu
Worse agreeing
models exist? bL =mon
Optimal
prediction? bL =def
Disagreers
exist?
Optimal
prediction?bL =def
bL =cor
Yes
No
Yes
No
Yes
No
No
Yes
No
Yes
Yes
No
Figure A.8: Flowchart with logic equivalent to that ofL(π e)
