---
title: 'Null importance: Disentangling relevance for interpretable machine learning'
url: https://arxiv.org/abs/2609.19511
category: ai-marketing
subcategory: measurement
date: 2026-09
venue: ''
authors:
- Garvesh Raskutti
- Kris Sankaran
- Jiaxin Ye
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.19511
pages: 29
chars: 120018
fetched_at: '2026-11-08T13:25:34+00:00'
kb_version: 1
---

# Null importance: Disentangling relevance for interpretable machine learning

Submitted to Statistical Science
Null importance: Disentangling relevance for
interpretable machine learning
Garvesh Raskutti, Kris Sankaran and Jiaxin Ye
Abstract.Feature importance is at the heart of many interpretable machine
learning methods and frameworks, but the term “importance” encompasses
several fundamentally different notions of relevance. We develop a unified
perspective based onnull importance: a population-level characterization of
when a feature is irrelevant under a specified notion of relevance. We consider
standard notions of null importance arising from marginal and conditional
statistical relevance, predictive risk, functional invariance, and causal effects,
and show how these notions answer different scientific questions. We illustrate
the framework through two applications in which the distinction is partic-
ularly consequential: algorithmic fairness, where common fairness criteria
correspond to different notions of null importance, and genomic perturbation
modeling, where different standard choices of relevance lead to different con-
clusions about what a prediction model has learned. The framework connects
three aspects of feature analysis: the scientific question defining relevance,
the data and model assumptions that shape how the different null notions
relate, and the methods used to assess importance. We establish sufficient
conditions under which standard notions of null importance coincide and give
counterexamples showing how they diverge when those conditions fail. We
then ask which notions of null different families of methods actually target
and analyze the conditions under which their zero-importance statistics can
identify their targets. Finally, simulations encompassing feature dependence,
redundancy, nonlinearity, hidden features and other standard phenomena as
well as real-data case studies on attribution in images and multiomics data
provide empirical evidence for these theoretical distinctions and their practical
consequences for interpreting feature importance methods. Taken together,
these results provide a common statistical language for relating scientific
questions, data-generating assumptions, and algorithms. This language makes
precise the conclusions about feature relevance that a given feature analysis
method can legitimately support.
Key words and phrases:feature importance, interpretable machine learning,
null hypothesis.
1. INTRODUCTION
Modern statistical and machine learning methods pro-
vide increasingly powerful tools primarily engineered for
predictive accuracy. However, applying these models to
solve real-world problems successfully demands an un-
derstanding of the underlying system. As emphasized by
Breiman’s distinction between the “two cultures” of sta-
tistical modeling [ 12], one culture prioritizes predictive
Department of Statistics, University of Wisconsin–Madison
(e-mail:
raskutti@stat.wisc.edu; ksankaran@wisc.edu; jye73@wisc.edu).
accuracy, while another seeks to understand the structure
underlying prediction. Truly interpretable machine learn-
ing unifies these two cultures: it acknowledges the predic-
tive design of modern models but insists that for real-world
deployment, we must go beyond askingcan we predict Y
from X?to rigorously examinewhich features matter, and
in what sense?
This question has no single answer. A feature may be rel-
evant because it is statistically associated with an outcome,
provides information beyond other variables, improves pre-
dictive performance, changes a fitted prediction function,
or has a causal effect. These notions can coincide in simple
settings, but they differ systematically in the presence of
1
arXiv:2609.19511v1  [stat.ML]  16 Sep 2026

2
dependence, redundancy, interactions, confounding, medi-
ation, and model misspecification.
We organize these distinctions around a simple idea:
null importance. Classical statistics uses a null hypothesis
to specify what it means for an effect or relationship to be
absent—for example, a zero regression coefficient, inde-
pendence, or no causal treatment effect [16, 29]. We use
the same logic for feature importance: anull importance
is a population-level statement specifying what it means
for a feature to be irrelevant under a particular notion of
relevance.
Null importance provides a common language for con-
necting three parts of interpretable feature analysis that are
often considered separately. First, at the level of thescien-
tific question, it specifies what kind of relevance or irrele-
vance is of interest in a particular application. Second, at
the level of thedata and data-generating process, it allows
us to state assumptions under which different notions of
relevance coincide, or to understand when they necessarily
differ. Third, at the level of themethod, it provides a way to
identify which notion of null importance a feature analysis
method targets and to determine whether the assumptions
required for that interpretation are satisfied. Our goal is
therefore not to identify a universally correct definition
of feature importance. Instead, we provide a framework
for connectingscientific questions,assumptions about the
data and model, andfeature analysis methods.
The framework applies across statistics, machine learn-
ing, and scientific applications. Classical feature selection
and conditional independence testing formalize statisti-
cal notions of irrelevance [38, 46, 79, 15, 69]. Predictive
importance methods define relevance through changes in
predictive risk [28, 48]. Explainable artificial intelligence
uses attribution and sensitivity measures to characterize
properties of learned prediction functions [53, 76, 57, 58].
Causal inference defines relevance through interventions
and counterfactual outcomes [ 62, 64]. These literatures
developed around different objectives, and the differences
among their definitions of relevance are often more conse-
quential than the differences among the algorithms used to
estimate them.
The same perspective also clarifies questions outside
conventional feature selection. Algorithmic fairness, for
example, can be viewed as asking under which notion
of relevance a protected attribute should be irrelevant.
Demographic parity, equalized odds, individual fairness,
proxy fairness, and counterfactual fairness impose differ-
ent forms of statistical, conditional, functional, or causal
nullity [25, 39, 22, 47]. Similarly, in scientific applica-
tions such as genomic perturbation modeling, one may
ask whether a perturbation is associated with a response,
improves prediction, or has a direct causal effect. These
represent distinct null questions even when concerning
the same variables, a divergence carrying critical conse-
quences for both scientific applications and methods de-
velopment. Consequently, different methods should nei-
ther be swapped interchangeably within an analysis nor
benchmarked against one another in methodological stud-
ies unless they are explicitly known to target the same
underlying notion of null importance.
The remainder of the paper develops this perspective
in three stages. Section 2 focuses on null importances at
the scientific question level. We define several population-
level notions of null importance corresponding to statisti-
cal, predictive, functional, and causal relevance. Section 3
askswhat assumptions can we make about the data and
data-generating process?We characterize conditions un-
der which these notions coincide and give counterexam-
ples showing how they separate under dependence, redun-
dancy, interactions, confounding, and model misspecifica-
tion. Section 4 then askswhich methods should we use?
We organize representative feature selection, attribution,
sensitivity, predictive, and causal methods according to the
notions of null importance they target and the conditions
under which their outputs identify those notions. Section 5
provides a number of synthetic and real data case studies
including local image attribution and multiomics that are
consistent with the messages in Sections 2-4.
The resulting message is simple: interpretable feature
importance is a family of questions whose answers depend
on what we mean by relevance, what assumptions we are
willing to make about the data, and what method we use
to assess it. Null importance provides a common language
for making these choices explicit and for connecting a
scientific claim to the assumptions and methods needed to
support it.
1.1 Related work and positioning
Interpretability has been studied from several com-
plementary perspectives. One emphasizesintrinsic inter-
pretability: models whose structure is sufficiently trans-
parent that no post-hoc explanation is required [49, 67]. A
second focuses onpost-hoc explanationof complex mod-
els, including feature attribution, surrogate models, exam-
ples, concepts, and counterfactuals. A third emphasizes
thescientific or practical purposeof an interpretation, ask-
ing whether an explanation is relevant to the question and
audience of interest. These perspectives have motivated
numerous taxonomies of interpretable machine learning
and explainable AI [24, 37, 58, 5].
Our work complements these taxonomies by organizing
interpretability methods according to a different dimen-
sion: thepopulation-level null notion of relevancerepre-
sented by zero importance. This distinction is important
because methods that appear similar computationally may
answer different questions, while methods from very dif-
ferent methodological families may target the same notion

NULL IMPORTANCE3
of irrelevance. In particular, the predictive, descriptive, and
relevance (PDR) framework of [58] emphasizes that rel-
evance depends on the purpose of an interpretation. We
make this relevance notion explicit statistically by defin-
ing the corresponding population null and studying the
assumptions under which it can be identified.
A related literature asks how explanations should be
evaluated. Doshi-Velez and Kim [24] called for a rigor-
ous science of interpretability, while subsequent work has
proposed criteria including faithfulness, sensitivity, robust-
ness, consistency, and human usefulness. For example,
Adebayo et al. [ 1] showed that some saliency methods
can be insensitive to the model or labels they purport to
explain, motivating systematic “sanity checks.” Axiomatic
approaches to attribution similarly specify desirable prop-
erties that explanation methods should satisfy [ 76, 53].
These perspectives are complementary to ours. Rather than
asking only whether an explanation satisfies a generic eval-
uation criterion, we ask what population-level claim is
represented by null importance and whether the proposed
statistic actually identifies that claim.
This distinction relates closely to work onstability,
reproducibility, and veridical data science. [ 83] empha-
sizes stability under appropriate perturbations as a fun-
damental requirement for reliable statistical conclusions,
while [84] place stability within the broader Predictability
Computability Stability (PCS) framework for trustworthy
data science. Stability and null identification address differ-
ent aspects of reliability: a feature-importance conclusion
may be stable but consistently target the wrong notion of
relevance, or it may target the appropriate null but be un-
stable in finite samples. Thus, null importance provides a
complementary component of a broader trust standard for
feature analysis.
Human-centered perspectives further emphasize that
explanations are shaped by the purpose for which they
are provided and the needs of their audience [ 56]. This
reinforces our view that there is no single notion of feature
relevance. A practitioner concerned with prediction may
regard a feature as irrelevant if removing it does not change
predictive risk, a scientist may instead require invariance of
a response function, and a causal investigator may require
that an intervention have no effect. These are different
scientific questions rather than competing estimates of a
single underlying quantity.
Our perspective is therefore broader than a taxonomy of
explainable AI methods and narrower than a general the-
ory of interpretability. We focus on a common statistical
question that arises across feature selection, feature attribu-
tion, sensitivity analysis, predictive modeling, and causal
analysis:what does it mean for a feature to be irrelevant?
Once a null notion is specified, three questions follow nat-
urally: what assumptions make that null identifiable; when
is it equivalent to other notions of irrelevance; and which
methods target and identify it? This leads to the central dis-
tinction in our paper between a method’stargeted nulland
the null that its zero-importance statistic actuallyidentifies.
The subsequent sections develop these connections for-
mally and examine their consequences through theoretical
results, counterexamples, simulations, and applications.
2. NULL IMPORTANCE: DEFINITIONS AND
EXAMPLES
The notion of feature importance depends fundamentally
on the underlying notion of scientific relevance. To make
these notions precise, let X= (X 1, . . . , Xp)∈ Xdenote
a vector of features, where X=X 1 × · · · × Xp, and let
Y∈ Ydenote a response variable.
DEFINITION2.1 (Null Importance). Feature Xj satis-
fies the null importance property, denoted byN j, ifX j is
deemed uninformative for Y under a chosen criterion of
relevance.
In many settings, relevance is quantified via a non-
negative function Rj ≥0 defined on the space of feature-
response relationships, where larger values correspond to
greater relevance. In this case, the null importance property
is characterized by:
Nj ⇐ ⇒Rj = 0.
The remainder of this section introduces several com-
monly used notions of null importance arising from differ-
ent criteria of scientific relevance.
2.1 Functional Null Importance
Functional relevance is determined entirely by a pre-
diction function f:X → Yand does not depend on a
data distribution. This notion underlies gradient-based
attribution methods such as saliency maps [ 72], Inte-
grated Gradients [ 76], and related interpretability ap-
proaches [6, 65, 68, 71, 73].
Let X=X 1 × · · · × Xp, and let X−j = Q k̸=j Xk denote
the subspace excluding the j-th feature, where x−j ∈ X−j
represents a vector x∈ X omitting its j-th coordinate
xj. For simplicity of notation we restrict to the setting of
prediction and binary classification. Natural extensions
to multi-class classification, generation and other settings
exist.
DEFINITION2.2 (Global Functional Null). A feature
Xj satisfies theglobal functional null property, denoted by
N func-global j , if the prediction function f does not depend
on xj anywhere on X . That is, there exists a function
g:X −j → Ysuch that
f(x) =g(x −j)for allx∈ X.

4
In terms of our general framework, this corresponds to
Rglobal j (f) = 0, where
Rglobal j (f)≡sup x,x′∈X
x−j=x′ −j
|f(x)−f(x ′)|.
DEFINITION2.3 (Local Functional Null). Let x∈ X.
A feature Xj satisfies thelocal functional null property at
x, denoted by N func-local j (x), if there exists an open neigh-
borhood U(x)⊆ Xand a function g:X −j → Ysuch that
f(z) =g(z −j)for allz∈U(x).
Equivalently, the prediction function is locally invariant to
perturbations of xj near x, corresponding to Rlocal j (f;x) =
0overU(x).
DEFINITION2.4 (Pointwise Functional Null). Sup-
pose X ⊆Rp and f is differentiable at x∈ X. A feature
Xj satisfies thepointwise functional null property at x,
denoted byN func-pointwise j (x), if
∂f(x)
∂xj
= 0.
Here, the local relevance measure reduces to
Rpointwise j (f;x) =

 ∂f(x) ∂xj

 = 0.
REMARK1. The three notions above capture func-
tional relevance across different spatial scales. Under ap-
propriate smoothness conditions on X and f, these prop-
erties exhibit a natural hierarchy for allx∈ X:
N func-global j =⇒ Nfunc-local j (x) =⇒ Nfunc-pointwise j (x).
2.2 Statistical Null Importance
In probabilistic settings where (X, Y)is governed by a
joint distribution P(X, Y), statistical null importance for-
malizes feature relevance using probability theory and in-
formation theory. We focus on two primary model-agnostic
notions:marginalandconditionalstatistical null impor-
tance.
DEFINITION2.5 (Statistical Marginal Null Importance).
Feature Xj satisfies themarginal statistical null property,
denoted by N stat−marg j , if its marginal mutual information
with the response vanishes:
Rmarg j ≡I(X j;Y) = 0.
Equivalently, Xj is statistically independent of Y , denoted
byY⊥X j.
Conversely,Xj is marginally relevant whenever we have
Rmarg j >0 . Methods such as correlation screening [ 26,
27], mutual information screening [63], and nonparametric
independence measures [35, 36, 77] directly evaluate or
estimate this marginal quantity.
DEFINITION2.6 (Statistical Conditional Null Impor-
tance). Feature Xj satisfies theconditional statistical
null property, denoted by N stat−cond j , if its conditional
mutual information with the response given all other fea-
tures vanishes:
Rcond j ≡I(X j;Y|X −j) = 0.
Equivalently,X j is conditionally independent ofYgiven
X−j, denoted byY⊥X j |X −j.
Thus, Xj is conditionally null if it carries no incremental
information aboutYbeyond what is already contained in
X−j. Conversely, Xj is conditionally relevant whenever
Rcond j >0.
Conditional statistical relevance is among the most
widely adopted notions of feature importance in statis-
tical learning [2, 79, 46, 38]. It serves as the foundational
property behind conditional independence testing [69, 11]
and distribution-free feature selection frameworks such as
Model-X Knockoffs [7, 15].
2.3 Risk-Based Null Importance
Risk-based relevance quantifies the intrinsic predictive
value of a feature with respect to a designated hypoth-
esis class and loss function. This perspective is closely
related to predictive feature importance measures such as
LOCO [48], permutation importance [13, 28], and predic-
tive model reliance [28].
Let L:Y × Y →R≥0 denote a non-negative loss func-
tion, and let
R(f)≡E (X,Y)∼P [L(Y, f(X))]
denote the population risk of a prediction functionf:X →
Y.
Let F ⊆ {f:X → Y}denote a class of prediction func-
tions over the full feature space X , and let F−j ⊆ {g:
X−j → Y}denote the restricted class operating on X−j.
We define the optimal achievable risks as
R∗ ≡inf
f∈F
R(f)andR ∗ −j ≡inf g∈F−j E[L(Y, g(X−j))].
Assuming F−j is embedded in F via the inclusion f(x) =
g(x−j), it holds thatR ∗ −j ≥R ∗.
DEFINITION2.7 (Risk-Based Relevance Measure).
The risk-based relevance of feature Xj relative to the
tuple(P,F, L)is defined as
Rrisk j (F, L)≡R∗ −j −R ∗.

NULL IMPORTANCE5
DEFINITION2.8 (Risk-Based Null Importance). Fea-
ture Xj satisfies therisk-based null property, denoted by
N risk j , if its risk-based relevance vanishes:
N risk j ⇐ ⇒Rrisk j (F, L) = 0⇐ ⇒R∗ −j =R ∗.
Conversely, Xj is risk-relevant whenever Rrisk j (F, L)>
0, meaning that excluding Xj strictly deteriorates the pop-
ulation risk achievable by the model familyF.
This notion forms the basis of many predictive feature
importance and feature selection procedures, including
LOCO and related predictive relevance methods.
2.4 Causal Null Importance
Causal relevance evaluates whether an interventional
perturbation of Xj alters the distribution of Y . This notion
is rooted in the causal inference literature and intervention-
based reasoning [62, 64, 41, 42, 45].
Let P(Y|do(X j =x j)) denote the interventional re-
sponse distribution under Pearl’s do-calculus, and let
PY denote the space of probability measures on Y. Let
D:P Y × PY →R ≥0 be a statistical distance or divergence
on probability measures (e.g., Total Variation distance,
Kullback-Leibler divergence, or Wasserstein distance) sat-
isfyingD(P 1, P2) = 0⇐ ⇒P1 =P 2.
DEFINITION2.9 (Causal Relevance Measure). Causal
relevance of feature Xj may be defined as the supremum
interventional divergence over all pairs of feature values
xj, x′ j ∈ Xj,
Rcausal j ≡sup
xj,x′ j∈Xj
D

P(Y|do(X j =x j)),
P(Y|do(X j =x ′ j))  .
DEFINITION2.10 (Causal Null Importance). Feature
Xj satisfies thecausal null property, denoted by N causal j ,
if its causal relevance vanishes:
N causal j ⇐ ⇒Rcausal j = 0.
Equivalently, P(Y|do(X j =x j)) =P(Y|do(X j =
x′ j)) for all xj, x′ j ∈ Xj, rendering the interventional re-
sponse distribution strictly invariant to xj. Conversely, Xj
is causally relevant wheneverR causal j >0.
This notion captures scientific questions concerning
causal influence and intervention effects rather than statis-
tical association or predictive utility.
2.5 Example: Algorithmic Fairness as Null Importance
The null importance framework provides a unifying
mathematical language for algorithmic fairness. Rather
than viewing different fairness criteria as fundamentally
different mathematical objects, we interpret each crite-
rion as specifying a notion of relevance under which the
protected attribute should be irrelevant. This perspective
complements existing taxonomies of algorithmic fairness
[17, 25, 81] by emphasizing the underlying notion of null
importance.
Let A denote a protected attribute, letX= (X 1, . . . , Xp)
denote the remaining observed features, let Y denote the
true outcome, and let ˆY=f(X, A) denote the prediction
of a learned model. In this setting, the relevance of the
attribute A is characterized by a non-negative relevance
functional
RA ≥0,
with the corresponding null importance propertyN A.
Algorithmic fairness is therefore naturally formulated as
requiring that the protected attribute satisfy an appropriate
null importance property. Different fairness definitions
correspond to different choices of relevance functional.
2.5.0.1 Marginal Statistical Null Importance.Demo-
graphic parity [25, 8] requires that the prediction be sta-
tistically independent of the protected attribute over the
population.
Define the marginal statistical relevance
Rmarg A ( ˆY) =I(A; ˆY).
The corresponding fairness criterion Rmarg A ( ˆY) = 0 is
therefore exactly A⊥ ˆY . Thus demographic parity is pre-
cisely the marginal statistical null importance property
applied to the protected attribute.
2.5.0.2 Conditional Statistical Null Importance.Equal-
ized odds [ 39] requires predictions to be conditionally
independent of the protected attribute given the true out-
come.
Define
Rcond A ( ˆY|Y) =I(A; ˆY|Y).
The corresponding fairness criterion Rcond A ( ˆY|Y) = 0
is A⊥ ˆY|Y . Similarly, equality of opportunity [39] corre-
sponds to Rcond A ( ˆY|Y= 1) = 0 and hence only requires
conditional independence among positively labeled exam-
ples.
2.5.0.3 Proxy Fairness.Rather than asking whether pre-
dictions depend on the protected attribute, proxy fairness
asks whether an observed feature uniquely encodes pro-
tected information [22, 43, 80].
For featureX j, define
Rcond j (A) =I(X j;A|X −j).
The corresponding null importance property isRcond j (A)
= 0. Thus proxy detection is itself a conditional statisti-
cal null importance problem, with the protected attribute
serving as the response variable.

6
2.5.0.4 Local Functional Null Importance.Individual
fairness [25] is a local property of the prediction function
rather than a population-level property. Informally, similar
individuals should receive similar predictions.
Suppose f is differentiable. A natural local functional
relevance measure is
Rlocal A (x) =

 ∂f(x) ∂A

 .
The corresponding null importance property is Rlocal A (x)
= 0. More generally, local functional relevance may be
characterized through local invariance of the prediction
function, as given in Definition 2.3. Consequently, individ-
ual fairness is naturally interpreted as a local functional
null importance criterion.
2.5.0.5 Global Causal Null Importance.Counterfactual
fairness [47] is defined through interventions on the pro-
tected attribute.
Define
Rcausal A = sup a,a′ D  P( ˆY|do(A=a)),
P( ˆY|do(A=a ′))  ,
where D(·,·) is any divergence satisfying D(P, Q) = 0
if and only ifP=Q.
The corresponding null importance property isRcausal A =
0, or equivalently,
P( ˆY|do(A=a)) =P( ˆY|do(A=a ′))∀a, a ′.
Thus counterfactual fairness is precisely a global causal
null importance criterion.
The preceding examples illustrate that many widely-
used notions of algorithmic fairness differ primarily in the
notion of relevance they seek to eliminate rather than in
their mathematical structure [54, 17, 81]. Within the null
importance framework,
Fairness notion Null importance interpretation
Demographic parity Marginal statistical
Equalized odds Conditional statistical
Equality of opportunity Conditional statistical (re-
stricted outcome)
Proxy fairness Conditional statistical (target =
protected attribute)
Individual fairness Local functional
Counterfactual fairness Causal
From this perspective, algorithmic fairness is fundamen-
tally the problem of determining under which notion of
relevance the protected attribute should become irrelevant.
This is consistent with prior impossibility results [ 18, 44]
asserting that fairness measures can not simultaneously
satisfy multiple fairness criteria. The choice of statistical,
functional, predictive, or causal relevance and whether
relevance is assessed globally or locally determines the
appropriate mathematical formulation and corresponding
fairness methodology.
2.6 Example: Clarifying Perturbation Modeling via Null
Importance
Fairness is an unusually clean case. In most scientific
problems, the right null is harder to find, and finding it is
the scientific work itself. We illustrate this with genomic
perturbation modeling, where recent debates about how to
evaluate the models are, in large part, disagreements about
which null to target [82, 59, 50]. These models are trained
from perturbation sequencing data, where individual genes
are knocked down and profiles of the transcriptome are
recorded in response. When coupled with sufficiently pow-
erful prediction models, such experiments can uncover the
regulatory architecture of the genome. In this context, null
importance clarifies the object that is being declared rel-
evant, like the influence of a perturbation target G on the
entire response Y or an individual perturbation-response
edge g→j , suggesting relevance objects RG and Rg→j.
Further, by distinguishing between null notions, the frame-
work resolves disagreements around metric choice, like
whether an evaluation should be restricted to differentially
expressed genes.
Let G represent the collection of perturbation targets, ∅
the unperturbed control, and G+ =G ∪ {∅}. Let G∼Q
be a random perturbation from G+ and A=1{G̸=∅}
indicate that a cell has been perturbed. Suppose the
transcriptome-wide response across d genes is drawn ac-
cording to Y∼P(· |do (G)) . Let f denote a perturbation
prediction model, whose goal is to predict the response
Y given an observed perturbation G. First we consider
notions of relevance useful in characterizing good metrics.
Metric Confounding. The mere act of perturbing cells
can affect the transcriptome, regardless of the choice of per-
turbed gene. This creates an artificial signal that can make
a model appear effective even though it hasn’t learned
any perturbation-specific response; i.e., it learns a pattern
shared across all perturbations that differentiates them
from the unperturbed controls, but not the response to any
particular perturbation. A model confounded in this way
exhibits,
I(A;f(G))>0,whileI(G;f(G)|A= 1) = 0
where I(., .)refers to mutual information meaning the
model has learned a perturbation effect but a gene-specific
signal. From the null importance perspective, the critique
is that existing models are evaluating the relevance of
the existence of a perturbation A rather than the specific
perturbed geneG.
Metric Baselines. It is possible to set a baseline repre-
senting signal that can be captured by f that is unrelated
to the perturbation. Define the risk,
R(f) =E G∼Q EY∼P(·|do(G)) [L(Y, f(G))]
for loss function L(., .). Then, letting F0 represent all
constant functions, the “strong baseline” recommendation

NULL IMPORTANCE7
of [82] can be written as computing
Rrisk G = inf f ′∈F0 R(f ′)− R(f),
and using Rrisk G to indicate that the model has no per-
turbation-specific performance improvements. These rec-
ommendations can be read as a model-level notion of
relevance used to evaluate overall prediction perfor-
mance, which is distinct from the relevance of specific
perturbation-to-target edges g→j . Next we consider how
null importance can highlight these biological relation-
ships.
Marginal Importance and DE filtering. Methods like
SCEPTRE [9] identify marginal associations between re-
sponse genejand the fixed knockdown targetg,
Rmarg g→j =D(P(Y j |do(g)), P(Yj |∅))
where D(., .)refers to KL-divergence. Typically the pertur-
bation interventions are assumed to satisfy the conditions
of Lemma 3 below, allowing for this causal quantity to be
evaluated from marginal statistics.
Some authors have advocated for restricting evaluation
to a subset of genes that pass a differentially expression
(DE) filter [55]. This corresponds to ignoring edges in a
null set defined as edges where the relevance is too low or
the target gene is not sufficiently differentially expressed,
N ε g→j ⇐ ⇒Rmarg g→j < ε,
where ε is a threshold associated with the power of the un-
derlying differential test. As the sample size grows, power
increases, allowing us to reduce the DE thresholdε↓0 and
returning us to the definition of null importance in the un-
filtered case. DE filtering changes not only the set of genes
under consideration but also the implicit null notion. It
requires evaluation of edges that have already been judged
nonnull under a marginal perturbation-response notion.
Causal Importance and Drug Targeting. Let M de-
note the response of genes other than j, i.e., M=Y −j and
define,
Rcausal g→j = sup m D  P(Y j |do(g), M=m),
P(Y j |∅, M=m)

,
as the direct effect of perturbing gene g on gene j and
ignoring effects mediated through all other genes. In this
case an edge is null if and only if
P(Y j |do(g), M=m) =P(Y j |∅, M=m)for allm
where conditioning on all mediator genes removes the
possibility of backdoor confounding [62]. This perspective
distinguishes core vs. peripheral genes in the omnigenic
model [61] and is arguably more scientifically aligned with
the goal of drug targeting. Indeed a downstream gene j
may be correlated with g, and this relationship may be
learned by the black box f without g being an effective
target for modifying j’s activity. A perturbation g may be
nonnull under Rmarg g→j if changes the responsej downstream,
but it still may fail to be an effective intervention target
in the sense Rcausal g→j = 0 if it doesn’t impact the response j
directly.
These examples highlight that both metrics and meth-
ods in perturbation modeling can disagree because they
consider different objects to call relevant (e.g., A vs. G)
or because they target different notions of null importance
(Rmarginal g→j vs. Rcausal g→j ). The language of null importance of-
fers a simple way of organizing discussion around these
subtle scientific issues.
3. EQUIVALENCES AND COUNTER-EXAMPLES FOR
NULL IMPORTANCE
Once a scientific notion of relevance has been specified,
the next question is what can be inferred from the available
data. Different notions of null importance are generally
distinct, but they can coincide under particular assump-
tions about the data-generating process, the dependence
structure among features, the predictive function class, or
the relationship between observational and interventional
distributions.
This section therefore asks a different question from the
previous one. Section 2 specifiedwhat we mean by rele-
vance; here we askwhen different meanings of relevance
lead to the same conclusion. These equivalences are useful
because they explain when a method developed for one no-
tion of relevance can legitimately be interpreted in terms
of another. The counterexamples are equally important:
they identify common settings in which such interpreta-
tions fail. Furthermore, practitioners may be able to deter-
mine whether the assumptions imposed for equivalence
are likely to be satisfied or whether scenarios proposed by
the counter-examples are likely to arise in their data. We
emphasize that the assumptions below are sufficient condi-
tions for equivalence rather than universal requirements.
3.1 Equivalences and key sufficient assumptions
3.1.1 Global functional and statistical conditional null
equivalence.There is one idealized setting in which func-
tional and conditional statistical notions of importance
coincide. This result illustrates that, under a deterministic
and sufficiently regular data-generating mechanism with a
non-redundant feature representation, the two perspectives
identify the same null features. In practice, departures from
these assumptions can cause the two notions to diverge.
LEMMA1 (Functional–conditional statistical null equiv-
alence).LetX= (X j, X−j)∼P X and suppose that
Y=f(X)
almost surely. Assume that:

8
1.Deterministic outcome:Y=f(X)almost surely.
2. Functional regularity:For PX−j -almost every x−j,
the function
xj 7→f(x j, x−j)
is absolutely continuous on the support of Xj |
X−j =x −j.
3. Rich conditional support:For PX−j -almost every
x−j, the conditional distribution ofXj given X−j =
x−j has a density that is positive almost everywhere
on its support.
4. Non-redundancy:The conditional distribution of
Xj givenX −j is non-degenerate almost surely.
Then
N func−global j PX-almost everywhere⇐ ⇒ Nstat−cond j .
PROOF. First suppose that
∂f(x)
∂xj
= 0P X-almost everywhere.
By the rich conditional support assumption, this implies
that
∂f(x j, x−j)
∂xj
= 0
for Lebesgue-almost every xj and PX−j -almost every x−j.
By absolute continuity, it follows that, for PX−j -almost
everyx −j,
f(x j, x−j) =g(x −j)
for almost every xj, for some measurable function g.
Hence
Y=g(X −j)
almost surely. Therefore,
Y⊥X j |X −j.
Conversely, suppose that
Y⊥X j |X −j.
Since Y=f(X) deterministically, for PX−j -almost every
x−j,
f(X j, x−j)
is almost surely constant under the conditional distribution
of Xj given X−j =x −j. By the rich conditional support
assumption, this implies that
f(x j, x−j) =g(x −j)
for Lebesgue-almost every xj and PX−j -almost every x−j.
Absolute continuity then implies
∂f(x j, x−j)
∂xj
= 0
for Lebesgue-almost every(x j, x−j), and hence
∂f(x)
∂xj
= 0P X-almost everywhere.
The two key assumptions aredeterminismandnon-
redundancy. The deterministic assumption rules out out-
come noise. Non-redundancy prevents conditional inde-
pendence from arising simply because Xj is already deter-
mined by X−j. Conditional independence provides the
standard statistical formalization of irrelevance of Xj
given X−j; see, for example [ 23]. Under the additional
deterministic and functional regularity assumptions stated,
this statistical notion can be equated with a functional
notion based on the partial derivative.
Based on thedeterminismandnon-redundancyas-
sumptions, the key question a practitioner must ask is
whether the response exactly satisfies the functional re-
lationship across samples (determinism) and whether the
feature set can be compressed (non-redundancy) due to
dependence.
3.1.2 Risk-based and conditional statistical null equiv-
alence.Risk-based null importance is closely related to
conditional statistical null importance, but the equivalence
depends critically on the richness of the predictive function
class and on the loss function. In particular, squared loss
identifies the conditional mean, whereas a strictly proper
scoring rule for the full conditional distribution identifies
the entire conditional distribution.
LEMMA2 (Risk–conditional statistical null equiva-
lence).Let (Xj, X−j, Y)∼P . Let F be a class of pre-
dictive distributions for Y given X, and let ℓ be a strictly
proper scoring rule. Define
R(f) =E[ℓ(Y, f(X))].
Let F−j ⊆ Fdenote the subclass of predictors that depend
only onX −j. Assume:
1. Bayes completeness:The true conditional distribu-
tionP Y|X belongs toF.
2. Strict properness:The population risk is uniquely
minimized, up to PX-almost sure equality, by the
true conditional distributionP Y|X .
3.Restriction completeness:If
inf
f∈F
R(f) = inf
f∈F −j
R(f),
then the Bayes-optimal conditional distribution ad-
mits a representation inF −j.
Then
Y⊥X j |X −j ⇐ ⇒inf f∈F R(f) = inf f∈F −j R(f).

NULL IMPORTANCE9
PROOF. Suppose first that
Y⊥X j |X −j.
Then
PY|X =P Y|X −j
almost surely. Thus the Bayes-optimal conditional distribu-
tion depends only on X−j and belongs to F−j. Therefore,
inf
f∈F
R(f) = inf
f∈F −j
R(f).
Conversely, suppose that
inf
f∈F
R(f) = inf
f∈F −j
R(f).
By restriction completeness, the Bayes-optimal condi-
tional distribution can be represented as
PY|X =g(X −j)
for some measurable functiong. Hence
PY|X =P Y|X −j
almost surely, which is equivalent to
Y⊥X j |X −j.
The key assumption isfunction-class richness, ex-
pressed here through Bayes completeness and restriction
completeness. If F is too restrictive, a feature may be
conditionally relevant while its contribution cannot be rep-
resented by the chosen model class.
For example, under squared loss,
R(f) =E

(Y−f(X)) 2 ,
the Bayes predictor is
f ∗(X) =E[Y|X].
Thus equality of the optimal risks with and without Xj
identifies only the conditional-mean null
E[Y|X] =E[Y|X −j],
which is weaker than conditional independence. Therefore,
the equivalence in Lemma 2 requires a loss and function
class capable of identifying the full conditional distribu-
tion.
The connection between predictive risk and conditional
statistical relevance follows from the theory of proper
scoring rules. In particular, strictly proper scoring rules
uniquely identify the true conditional distribution as the
Bayes-optimal predictive distribution [32]. Consequently,
when the predictive function class is sufficiently rich to
contain the true conditional distribution, equality of the op-
timal risks with and withoutXj is equivalent to conditional
independence. Thus the key question a practitioner must
ask is whether for the data being used, does the response
satisfies a functional relationship that belongs within the
function class induced by the predictive risk.
3.1.3 Marginal statistical and causal null equivalence
under randomization.The connection between statistical
and causal null importance requires an assumption that
relates the observational and interventional distributions.
Randomization provides a particularly transparent setting
because it is a property of the feature assignment mecha-
nism rather than an assumption about the null itself. Let
Y xj denote the potential outcome under the intervention
do(Xj =x j).
LEMMA3 (Marginal Statistical and Causal Null Equiva-
lence under Randomization).Let Y xj denote the poten-
tial outcome under the intervention do(Xj =x j). Suppose
the following assumptions hold:
1. Randomization (exchangeability):For every inter-
vention valuex j under consideration,
Y xj ⊥X j.
2.Consistency:IfX j =x j, then
Y=Y xj almost surely.
3. Positivity:Every intervention value xj under con-
sideration lies in the support of the randomization
distribution ofX j.
Then
N stat−marg j ⇐ ⇒ Ncausal j .
Equivalently,
Rmarg j = 0⇐ ⇒R causal j = 0.
PROOF. Under randomization and consistency, for ev-
ery intervention valuex j under consideration,
P(Y∈A|X j =x j) =P(Y xj ∈A|X j =x j)
=P(Y xj ∈A)
for every measurable set A. The first equality follows from
consistency, while the second follows from randomization.
Therefore,
P(Y|X j =x j) =P(Y xj ) =P(Y|do(X j =x j)).
Thus, under randomization,
P(Y|X j =x j) =P(Y|do(X j =x j))
for every intervention valuex j under consideration.
Suppose first that
N stat−marg j
holds. Then
P(Y|X j =x j) =P(Y|X j =x ′ j)
for allx j, x′ j. By the identification equality above,
P(Y|do(X j =x j)) =P(Y|do(X j =x ′ j))

10
for allx j, x′ j. Hence
N causal j
holds.
Conversely, suppose that
N causal j
holds. Then
P(Y|do(X j =x j)) =P(Y|do(X j =x ′ j))
for allx j, x′ j. Again using the identification equality,
P(Y|X j =x j) =P(Y|X j =x ′ j)
for allx j, x′ j. Hence
N stat−marg j
holds.
Therefore,
N stat−marg j ⇐ ⇒ Ncausal j ,
or equivalently,
Rmarg j = 0⇐ ⇒R causal j = 0.
The key assumption israndomization. Randomization
makes the distribution of potential outcomes independent
of the assigned value of Xj, thereby allowing the observa-
tional conditional distribution to identify the corresponding
interventional distribution. Consistency connects the ob-
served outcome to the relevant potential outcome, while
positivity ensures that the interventions of interest are iden-
tifiable.
The equivalence between the statistical and causal nulls
under randomization follows from the standard potential-
outcomes framework. Randomization implies exchange-
ability of the potential outcomes and treatment assignment,
while consistency links the observed outcome to the corre-
sponding potential outcome; see [66, 40].
3.1.4 Marginal and conditional statistical nulls.A natu-
ral question is whether marginal and conditional statistical
null importance coincide when the features are indepen-
dent. Feature independence is sufficient for one direction,
but not for the reverse direction in general.
LEMMA4 (Feature independence and marginal–condi-
tional nulls).Suppose that
Xj ⊥X −j.
Then
Y⊥X j |X −j =⇒Y⊥X j.
The converse does not hold in general.
PROOF. Suppose that
Y⊥X j |X −j.
Then
P(Y∈A|X j =x j, X−j =x −j)
=P(Y∈A|X −j =x −j)
for every measurable setA. Therefore,
P(Y∈A|X j =x j)
=
Z
P(Y∈A|X j =x j, X−j =x −j)dPX−j|Xj=xj (x−j)
=
Z
P(Y∈A|X −j =x −j)dP X−j (x−j),
where the second equality follows from
Xj ⊥X −j.
The final expression does not depend onx j. Hence
Y⊥X j.
The converse does not hold even when the features are
independent. For example, let
Xj, Xk ind∼Bernoulli(1/2)
and define
Y=X j ⊕X k,
where⊕denotes the XOR operation. Then
Y⊥X j,
but
Y̸⊥X j |X k.
Thusfeature independencealone is not sufficient for
equivalence of marginal and conditional statistical nulls.
An additionalno-interactionorstructural homogeneity
assumption is required for the reverse implication.
3.2 Counterexamples: Separation of Null Importance
Notions
The previous section established conditions under which
specific notions of null importance coincide. In this section,
we construct several counterexamples illustrating strict
separations between functional, statistical, risk-based, and
causal notions of null importance.

NULL IMPORTANCE11
3.2.0.1 Marginal vs Conditional Statistical Null.Per-
haps one of the most widely known difference in the statis-
tics literature is the distinction between marginal and con-
ditional null (see e.g. [23]).
EXAMPLE3.1 (Marginal null does not imply conditional
null). LetX 1 ∼Bernoulli(1/2)and define
X2 =X 1 ⊕ϵ, ϵ∼Bernoulli(1/2),
independent ofX 1. LetY=X 1.
Then:
•I(X 2;Y) = 0 , so X2 is marginally statistically null.
• However, I(X 2;Y|X 1)>0 , so X2 is not condi-
tionally statistically null.
Thus, marginal and conditional null importance do not
coincide in general.
3.2.0.2 Functional Null vs Conditional Statistical Null.
We provided an equivalence result in Lemma 1 and also
discussed conditions under which this equivalence breaks
down. To flesh this out further, we provide two more ex-
amples where the Lemma’s assumptions fail to hold.
EXAMPLE3.2 (Redundant representation). Let
X1 ∼ N(0,1), X 2 =X 1,
and define
Y=X 2.
The prediction function can be written as
f(x 1, x2) =x 2,
which does not depend on x1. Therefore there exists a
function
g(x2) =x 2
such that
f(x 1, x2) =g(x 2),
and henceX 1 satisfies the functional null property.
Moreover,
Y=X 2,
implies
P(Y|X 1, X2) =P(Y|X 2),
and therefore
Y⊥X 1 |X 2.
Thus X1 is both functionally null and conditionally sta-
tistically null. This example illustrates how redundancy
can create multiple equivalent representations of the predic-
tion mechanism. Although the two notions of null impor-
tance coincide in this setting, the relevance of individual
features becomes non-identifiable because the same pre-
dictive information is duplicated across multiple variables.
EXAMPLE3.3 (Conditional statistical null without func-
tional null). Let
X1 ∼ N(0,1), X 2 =X 1,
and define
Y= 1 2 X1 + 1 2 X2.
SinceX 1 =X 2, we have
Y=X 2 =X 1.
Consequently,
P(Y|X 1, X2) =P(Y|X 2),
so that
Y⊥X 1 |X 2.
Similarly,
Y⊥X 2 |X 1.
Thus each variable satisfies the conditional statistical null
property.
Now consider the prediction function
f(x 1, x2) = 1 2 x1 + 1 2 x2.
There does not exist a functiongsuch that
f(x 1, x2) =g(x 2)for all(x 1, x2)∈R 2,
since, for example,
f(0,0) = 0, f(2,0) = 1,
while both inputs have the same value of x2. Therefore
X1 is not functionally null. By symmetry, X2 is also not
functionally null.
This example illustrates that the conditional statisti-
cal null and functional null need not coincide due to re-
dundancy in the feature set which is assumed away in
Lemma 1. The discrepancy arises because perfect redun-
dancy makes the prediction mechanism statistically non-
identifiable: either feature alone determines the response
under the observational distribution, even though the cho-
sen functional representation explicitly depends on both
variables.
3.2.0.3 Risk-Based Null vs Conditional Statistical Null.
EXAMPLE3.4 (Failure of Bayes-completeness). Let
X1 ∼Unif(−1,1), X 2 =X 2 1 ,
and define
Y=X 2 =X 2 1 .
SinceX 2 is a deterministic function ofX 1,
P(Y|X 1, X2) =P(Y|X 1),

12
and therefore
Y⊥X 2 |X 1.
ThusX 2 satisfies the conditional statistical null property.
Now consider the hypothesis class of linear predictors
F={f(x 1, x2) =β 0 +β 1x1 +β 2x2 :β 0, β1, β2 ∈R}.
When both variables are available, the predictor
f(x 1, x2) =x 2
belongs toF, so the optimal risk equals the Bayes risk,
R∗ = 0.
If X2 is removed, however, the restricted hypothesis
class becomes
F−2 ={f(x 1) =β 0 +β 1x1 :β 0, β1 ∈R},
which cannot represent the quadratic function
Y=X 2 1 .
Consequently,
R∗ −2 > R∗,
soX 2 is not risk-null.
This example demonstrates that conditional statistical
null and risk null need not coincide when the hypothe-
sis class is not Bayes-complete. Although X2 contains
no information beyond X1, its explicit inclusion enables
the restricted hypothesis class to represent the regression
function exactly. In contrast, a Bayes-complete hypothesis
class would allow the same predictor to be represented
using X1 alone, making X2 risk-null as well. This nonlin-
ear example is recurring scenario where methods suited to
linear and nonlinear relationships differ.
3.2.0.4 Causal null vs Conditional Statistical Null.
EXAMPLE3.5 (Causal importance without conditional
statistical importance). Let
X∼ N(0,1),
and define the structural equations
M=X, Y=M.
The causal graph is
X− →M− →Y.
Since intervening on X changes M, which in turn
changesY, the variableXis not causally null.
On the other hand,
P(Y|X, M) =P(Y|M),
becauseYdepends only on the mediatorM. Hence
Y⊥X|M,
soXis conditionally statistically null.
This example illustrates that conditional statistical null
does not imply causal null. Conditioning on a mediator
blocks the indirect causal pathway, rendering the treat-
ment statistically redundant for prediction even though it
remains causally relevant.
4. CHARACTERIZING FEATURE ANALYSIS METHODS
BY NULL IMPORTANCE
The notions of null importance given in Section 2 al-
low us to frame precise scientific questions about the role
of a variable in a dataset, and Section 3 gave conditions
under which they coincide. We now turn to methods for
establishing whether features are null. For each feature-
analysis method, we ask two questions: (i) which notion
of null importance does the method directly target, and (ii)
does the population importance statistic produced by the
method identify that null? This distinction is important. A
method may be motivated by a particular notion of rele-
vance without its zero importance statistic identifying that
notion. Further, a method may identify a null only under
assumptions that connect its statistical target to its scien-
tific context. We therefore distinguish betweentargetinga
null notion andidentifyingthat null.
The resulting taxonomy is summarized in Table 1. The
table should be read as a guide to methodological align-
ment rather than as a ranking of methods. The appropriate
choice depends on the scientific question, the available
data, and the assumptions that are credible in the appli-
cation. Since there are so many feature analysis methods,
we focus on specific examples of feature attribution, fea-
ture selection and functional sensitivity methods. Methods
not included may also be put through this taxonomy or
framework. This illustrates another key motivation of null
importance which is to evaluate feature analysis methods.
A method should be evaluated against the null notion it is
intended to answer, not merely by the numerical behavior
of its importance scores.
4.1 Feature attribution methods
We begin with feature attribution methods, which assign
to each feature an importance scoreϕj intended to quantify
its contribution to a specified value functional V: 2 p →R .
Shapley values provide a general axiomatic framework
for such attribution (see e.g. [70, 53, 51, 41, 31, 20, 19]).
Given a value functional V , the Shapley value for feature
jis defined as
ϕj =
X
S⊆{1,...,p}\{j}
1
p
p−1
|S|
 [V(S∪ {j})−V(S)].
The Shapley values are uniquely characterized by the
following axioms:
•Efficiency: Pp j=1 ϕj =V({1, . . . , p})−V(∅).

NULL IMPORTANCE13
• Symmetry:if two features contribute identically to
V, then they receive equal attribution.
• Null player:if V(S∪ {j}) =V(S) for all S, then
ϕj = 0.
•Linearity:Shapley values are linear inV.
The null player axiom suggests a connection to null im-
portance; however, it is a uni-directional statement. A zero
value for φj does not imply zero contribution toV . Further,
a key feature of Shapley values is that the interpretation
of null importance depends entirely on the choice of value
functionalV.
•V(S) =E[f(X)|do(X S =x S)] corresponds to
causal Shapley values.
•V(S) =E[f(X)|X S =x S] corresponds to obser-
vational/statistical Shapley values.
•V(S) =R(f S) corresponds to risk-based Shapley
values.
•V(S) =f(x S, x′ S) corresponds to functional/baseline
attribution (e.g., Integrated Gradients-type construc-
tions).
Each of these choices induces a different notion of rele-
vance and therefore a different notion of null importance.
We now analyze whether Shapley values satisfy strong or
weak null properties under these different choices.
4.1.0.1 Risk-based Shapley.For function f we define
the difference of risk:
R(f(X))− R(f−j(X−j)).
The corresponding Shapley value [20, 31] is
ϕrisk j = X
S⊆[p]\{j}
1
p
p−1
|S|

h
R(fS(XS))− R(fS∪j (XS∪j ))
i
.
Thetargeted nullis a risk-based null importance (not iden-
tical to the original definition sincefis pre-defined):
R−j =R.
However, in general Shapley valuesdo notidentify the
risk-based null. Indeed, the risk null concerns the marginal
contribution of Xj when all other features are available,
whereas the Shapley value averages marginal contributions
over all subsets. A feature can therefore be risk-null in the
full model while making nonzero contributions to smaller
coalitions.
For example, consider a chain
X1 − →X2 − →X3 − →Y,
with
X2 =X 1 +γ, X 3 =X 2 +δ, Y=X 3 +ϵ,
where the noise variables are mutually independent. Once
X3 is available, X1 provides no additional predictive infor-
mation. Thus X1 is risk-null relative to X3. Nevertheless,
X1 contributes predictive information to coalitions that
do not contain X3, and therefore receives a nonzero Shap-
ley attribution. The example illustrates the fundamental
distinction betweenfull-model leave-one-feature-out im-
portanceandaverage coalition contribution.
Consequently, risk-based Shapley should not be inter-
preted as a general test for risk-based null importance.
4.1.0.2 Causal Shapley.Causal Shapley values [ 41, 42]
replace the observational distribution in the Shapley value
function by an interventional distribution. In the do-based
formulation, the value of a coalitionSis
V(S;x S) =E[f(X)|do(X S =x S)].
Thus, the corresponding Shapley value is
ϕcausal j (x) = X
S⊆−j
1
p
p−1
|S|

h
V(S∪ {j};xS∪{j} )
−V(S;x S)
i
.
This construction targets aninterventional functional
notion of relevance: feature Xj is causally null for the
prediction function if intervening on Xj does not change
the corresponding interventional expectation. In particular,
define a variant of the causal null defined through expecta-
tion:
E[f(X)|do(X j =x j)] =E

f(X)|do(X j =x ′ j) 
for all intervention values xj, x′ j in the relevant support.
The null-player property of the Shapley value gives the
following one-way guarantee.
LEMMA5 (Causal null implies zero causal Shapley).
Suppose that Xj is causally null in the sense that its inter-
vention does not change the interventional value function
for any coalition of the remaining features. Then
E[f(X)|do(X j =x j)] =E

f(X)|do(X j =x ′ j) 
=⇒ϕ causal j = 0.
PROOF. If Xj is causally null, then for every S⊆
{1, . . . , p} −j,
V(S∪ {j};xS∪{j} ) =V(S;x S).
Hence every marginal contribution of Xj is zero. Since
the Shapley value is a weighted average of these marginal
contributions,
ϕcausal j = 0.
The converse does not hold in general. Unlike a value
function based on optimal predictive risk, the interven-
tional expectation V(S;x S) is not monotone in the set of

14
intervened variables. Consequently, the marginal contribu-
tions
∆j(S) =V(S∪ {j};xS∪{j} )−V(S;x S)
may be positive for some coalitions and negative for
others. The Shapley value averages these contributions, so
they can cancel:
X
S⊆−j
wS∆j(S) = 0
even though∆ j(S)̸= 0for someS. Thus
ϕcausal j = 0̸=⇒
E[f(X)|do(X j =x j)] =E

f(X)|do(X j =x ′ j) 
without an additional assumption preventing such cancel-
lation.
Importantly, this is anidentificationissue rather than
a claim that cancellation is common in applications. The
causal Shapley literature of [41] and [42] establishes the
interventional construction and its causal interpretation,
but does not, to our knowledge, provide a general no-
cancellation condition or establish that cancellation is em-
pirically frequent.
4.1.0.3 Integrated Gradients.Integrated Gradients (IG)
[76] is a path-based attribution method that measures the
sensitivity of a prediction function relative to a baseline x′.
For the straight-line path from x′ to x, the attribution to
featureX j is
IGj(x;x ′) = (xj −x ′ j)
Z 1
0
∂f(x ′ +α(x−x ′))
∂xj
dα.(1)
The method therefore targetsfunctionalrelevance. Its
attribution is determined entirely by the prediction function
f, the input x, and the chosen baseline x′, rather than by
the distribution of(X, Y).
LEMMA6 (Functional null implies zero Integrated Gra-
dients).Suppose f is differentiable almost everywhere
and Xj is functionally null (along the path from x to x′).
Then, for every input x and baseline x′ for which the Inte-
grated Gradients path is defined,
IGj(x;x ′) = 0.
Consequently, any population-level aggregation of Inte-
grated Gradients that averages or otherwise aggregates
the absolute attributions also assigns zero importance to
Xj.
PROOF. Since f(x j, x−j) =g(x −j), the prediction
function is constant with respect tox j. Hence
∂f(x)
∂xj
= 0
almost everywhere. Therefore,
∂f(x ′ +α(x−x ′))
∂xj
= 0
for almost every α∈[0,1] . Substituting into the defini-
tion of Integrated Gradients gives
IGj(x;x ′) = (xj −x ′ j)
Z 1
0
0dα= 0.
This result is the functional-null property underlying the
Sensitivity(b)axiom of [ 76]: if the prediction function is
constant in a feature, that feature receives zero attribution.
Sundararajan et al. also establish that Integrated Gradients
satisfies Sensitivity (a), which requires a nonzero attribu-
tion when the input and baseline differ only in feature j
and the corresponding predictions differ. Thus IG is de-
signed to avoid the failure of ordinary local gradients to
detect changes that occur away from the endpoint of the
attribution path [76].
The result above is anull guaranteein the sense func-
tional nullity along a path implies zero Integrated Gradi-
ents. The converse, however, is not true. Indeed,
IGj(x;x ′) = 0
may occur even when f depends on xj, because the
signed derivatives along the path can cancel. Therefore,
N func−path j =⇒IG j(x;x ′) = 0,
but, in general,
IGj(x;x ′) = 0̸=⇒ N func−path j .
4.2 Feature selection methods
We now classify standard feature selection methods ac-
cording to which notion of null importance they satisfy.
4.2.0.1 Correlation and mutual information screening.
Correlation screening [26, 27] selects features based on
marginal association with the response. Thetargeted null
is marginal statistical association, with the precise null
depending on the association measure. It satisfies:
Corr(Xj, Y) = 0⇐X j ⊥Y,
However the converse does not hold, since correlation
captures linear dependence only. The simple univariate
example Y=X 2 where X∼Normal(0,1) shows that
Corr(X, Y) = 0butX̸⊥Y.
The weaknesses of correlation screening are addressed
by mutual information screening, where Corr(Xj, Y)is
replaced by mutual information I(X j;Y) . For mutual in-
formation screening [10, 63], the targeted null is marginal
statistical since
I(X j;Y) = 0⇐ ⇒X j ⊥Y
under the standard definition of mutual information. Thus
mutual information is an exact population measure for the
marginal statistical null.

NULL IMPORTANCE15
4.2.0.2 Lasso.Under a correctly specified linear model
with sparsity assumptions, Lasso [ 79] recovers features
satisfying:
Y⊥X j |X −j
in the population limit.
Thus, under standard assumptions (restricted eigenvalue,
irrepresentability), Lasso satisfies a form ofconditional
null consistency. However, this equivalence fails under
model misspecification or nonlinear dependence.
4.2.0.3 Knockoffs.Model-X knockoffs [ 7, 15] target the
conditional statistical null N stat−cond j (see Defn. 2.6). The
key theoretical result is that, under the Model-X assump-
tions that the knockoff variables eXsatisfy
(X, eX) swap(S) d= (X, eX)for allS, eX⊥Y|X,
the knockoff statistic for a conditionally null feature has
a symmetric distribution about zero. This sign symmetry
yields finite-sample false discovery rate control:
FDR≤q
for the knockoff selection procedure at target level q [15].
Thus, under valid knockoff construction, the method pro-
vides a finite-sample guarantee for identifying features that
are non-null with respect to the conditional statistical null.
Unlike methods based on a population importance score,
however, this is a selection and error-control guarantee
rather than a statement that a zero statistic identifies the
null.
4.2.0.4 Leave-One-Covariate-Out (LOCO).Leave-One-
Covariate-Out (LOCO) importance [ 48] targets N risk j
(Def 2.7). The corresponding population LOCO impor-
tance is
∆LOCO j =R ∗ −j −R ∗.
Then by definition,
∆LOCO j = 0⇐ ⇒ N risk j .
Thus LOCO directly identifies its targeted risk-based null
at the population level. The interpretation remains depen-
dent on the predictive function class F: risk nullity means
that Xj can be removed without increasing the optimal
achievable risk within that class, and does not in general
imply marginal or conditional statistical nullity. Lei et
al. [48] develop distribution-free inference for LOCO im-
portance, providing statistical guarantees for estimating
this population quantity.
4.2.0.5 Generalized Covariance Measure (GCM).The
generalized covariance measure (GCM) [ 69] targets the
conditional statistical null
N cond j :Y⊥X j |X −j.
For scalar Xj and Y , define the conditional-mean resid-
uals
εj =X j −E[X j |X −j], ε Y =Y−E[Y|X −j],
and the population generalized covariance measure
GCMj =E[ε jεY ].
If
Y⊥X j |X −j,
then
GCMj = 0,
provided the relevant second moments exist. Indeed,
conditional independence implies
E[εY |X j, X−j] =E[Y|X j, X−j]−E[Y|X −j] = 0,
and hence
E[εjεY ] =E[ε jE[εY |X j, X−j]] = 0.
Thus GCM provides a validnull guarantee: conditional
statistical nullity implies zero population GCM. The con-
verse does not hold in general. A zero covariance of the
residuals only rules out conditional linear association be-
tween the residualized variables (see the example for cor-
relation screening); conditional dependence can remain
through nonlinear or higher-order relationships. Shah and
Peters [ 69] therefore formulate GCM as a conditional-
independence test whose validity relies on consistently
estimating the conditional means.
4.2.0.6 MinShap.A recent method MinShap [ 85] tar-
gets thestatistical conditional and risk-based null: feature
Xj is null if its contribution remains zero after condition-
ing on all other features. Let
V IS j =V(S∪ {j})−V(S)
denote the marginal value of Xj given XS. The Min-
Shap population importance is defined by
MinShapj = min S⊆[p]\{j} V IS j ,
which simply replaces the average operator by the mini-
mum operator for the statistics V IS j . The key theoretical
result is that, undernull monotonicity,
S⊆T, V I S j = 0 =⇒V I T j = 0,
we have
MinShapj = 0⇐ ⇒V I −j j = 0.
Thus, under null monotonicity, MinShap identifies the con-
ditional risk-based null [85]: zero MinShap importance is
equivalent to zero marginal contribution after conditioning
on all remaining features.
For the population predictive-risk value functional, null
monotonicity holds under suitable faithfulness and no-
reverse-causation conditions. In contrast to ordinary Shap-
ley values, which average marginal contributions over sub-
sets and can therefore obscure conditional nullity, MinShap
is constructed to preserve this null property.

16
4.2.0.7 Mean Decrease Impurity (MDI).Mean decrease
impurity (MDI) is a feature importance measure derived
from tree-based models [13]. For a fitted tree, the MDI im-
portance of feature Xj is the total decrease in the splitting
criterion attributable to splits on Xj, typically averaged
over the trees in an ensemble.
MDI does not target a single population notion of null
importance. In particular, because tree construction is
based on greedy impurity reduction, MDI can reflect
marginal association, conditional association, feature re-
dundancy, and algorithm-specific choices such as split
selection and randomization. Consequently, MDI does not
in general provide a null-importance guarantee for either
marginal or conditional statistical relevance.
EXAMPLE4.1 (MDI and conditional null importance).
Consider binary features
X1 ∼Bernoulli(1/2), X 2 =X 1,
and response
Y=X 1.
ThenX 2 is conditionally statistically null givenX 1:
Y⊥X 2 |X 1.
However,X 1 andX 2 are observationally indistinguish-
able predictors of Y . At a node where both variables are
available, they produce the same impurity reduction. A
tree-building algorithm must therefore resolve a tie through
its implementation-specific tie-breaking or randomization
mechanism.
In a randomized tree ensemble, different trees can select
X1 or X2 for the corresponding split. Consequently, both
variables can receive positive MDI importance,
MDI(X1)>0,MDI(X 2)>0,
even though
Y⊥X 2 |X 1.
Thus MDI does not satisfy conditional null importance.
The example also illustrates that MDI is sensitive to the
representation of redundant predictive information: the al-
location of importance between statistically indistinguish-
able features can depend on the tree-building procedure
rather than on an intrinsic population property.
This phenomenon is consistent with the theoretical anal-
ysis of tree-based variable importance, which shows that
impurity-based importance can be affected by feature dis-
tributions, selection mechanisms, and correlations among
predictors [74, 75]. In particular, Strobl et al. [74] demon-
strate that the variable-selection mechanism underlying
random forests can favor certain variables even when their
predictive relevance is comparable.
4.3 Functional sensitivity methods
These methods characterize how a fixed prediction func-
tion f depends on a feature rather than testing whether
the feature can be removed from a predictive model.
Their targeted nulls are therefore functional, but the sum-
maries they use differ in whether they capture local
sensitivity, marginal effects, or total functional depen-
dence [3, 4, 72, 73, 33, 71].
4.3.0.1 Saliency maps.Saliency maps target thelocal
functional null
N func−local j : ∂f(x) ∂xj = 0.
The classical saliency map [72] uses
Sj(x) =

 ∂f(x) ∂xj

 .
Thus,
N func−local j =⇒S j(x) = 0
at every point where the derivative exists. Under stan-
dard regularity and support conditions, if the derivative is
zero throughout the relevant support, then f is constant in
xj, so the feature is functionally null. The converse can
therefore be stated as a functional result rather than as a
statistical or predictive one.
Saliency maps are consequently sensitive to local be-
havior: a feature can have zero gradient at a particular
observation even though the prediction function depends
on that feature elsewhere. This is one motivation for path-
based methods such as Integrated Gradients [72].
4.3.0.2 Partial Dependence.Partial dependence (PD)
[30] targets amarginal functional effectrather than the full
functional null. Its population partial dependence function
is
P Dj(xj) =E X−j [f(x j, X−j)].
A natural null for PD is therefore
N PD j :P D j(xj) =cfor allx j,
for some constant c. Hence a flat population PD curve
implies zero PD effect. However, a flat PD curve doesnot
imply the global functional null N func−global j (see Defini-
tion 2.2). For example, let Xj and Xk be independent with
E[Xk] = 0, and let
f(x j, xk) =x jxk.
Then
P Dj(xj) =x jE[Xk] = 0
for every xj, even thoughf depends directly on xj. Thus
PD can fail to identify functional relevance because aver-
aging can cancel heterogeneous effects. This distinction
is inherent in the marginal averaging construction of PD
[30].

NULL IMPORTANCE17
4.3.0.3 Accumulated Local Effects.Accumulated Lo-
cal Effects (ALE) [4] also targets amarginal functional
effect, but averages local derivatives over the observed
conditional distribution rather than averaging predictions
over the marginal distribution of the other features. For a
continuous feature,
ALEj(xj) =
Z xj
z0
E
 ∂f(z, X−j)
∂z

 Xj =z  dz.
Consequently, ifN func−global j holds, then
∂f(x)
∂xj
= 0
and therefore
ALEj(xj) =constant.
Thus the global functional null implies a flat ALE curve.
The converse does not hold in general: the conditional
averaging of local derivatives can cancel across values of
X−j, so a flat ALE curve need not imply that f is globally
independent of xj. ALE was introduced in part to avoid
the extrapolation problems of PD when predictors are cor-
related; it does not turn a marginal functional summary
into a complete characterization of functional dependence
[4].
A recurring theme is that aggregation can obscure null
identification. Shapley values average marginal contribu-
tions across coalitions, Integrated Gradients integrates
signed derivatives along a path, and PD and ALE aver-
age predictions or local derivatives over a marginal or
conditional distribution; in each case, nonzero effects in
some coalitions, path segments, or conditioning sets can
offset one another in the aggregate. This is not inherently a
defect of these summaries, but it suggests that methods in-
tended to identify null importance should be evaluated for
whether their aggregation step can erase relevant signal.
5. CASE STUDIES IN NULL IMPORTANCE
5.1 Counterexamples and Equivalence on Synthetic
Data
We next use synthetic data to distinguish the notions
of null importance defined in Section 2. We consider ten
data-generating mechanisms, each with p= 18 features,
six deliberately structured features S, detailed in Table
2, and twelve independent N(0,1) variables. For each
mechanism, we generate seven replicates at each of three
sample sizes n∈ {50,500,5000}, and each mechanism
has an underlying response signal f. We generate both
continuous responses,
y∼N

f(x), σ2 y 
and binary responses,
y∼Bernoulli(logit −1 (f(x))).
Mechanism D1 is an additive linear model, D2 remains
additive but is quadratic. D3 and D4 introduce interactions.
D4 reduces to XOR when the group sizesGk are set to two.
D5 - D7 use simple structural causal models. In D5, each
nonnull variable is matched by a highly correlated proxy
which is irrelevant for prediction. D6 introduces an unob-
served confounder, and D7 uses two length-three chain
graphs with all mediators measured, so that condition-
ing on downstream mediators makes upstream variables
conditionally null. D8 - D10 distinguish between func-
tional, conditional, and risk-based null importance. In D8,
features appear in highly correlated pairs, both of which
appear inf. D9 and D10 also use paired variables. In D9,
the mean depends quadratically on one member of the pair.
The second member is a quadratically-transformed, but
corrupted version, of the relevant feature. For D10, one
member of the pair influences the mean and the other its
variance. For this dataset, we only consider the Gaussian
response case.
To ensure our measured importances reflect the data
generating mechanism rather than a model-based approxi-
mation to it, we formed predictions using the ground truth
function f. This allows us to compare null importance
notions induced by the mechanism itself, bypassing error
from estimating f. For D1 – D3, the structured features S
are nonnull under every notion of null importance. They
are useful for comparing methods but do not distinguish
notions of null importance. The remaining mechanisms
do. For example, D9 is based on Example 3.4 and dis-
tinguishes conditional from risk nulls. The true response
depends on a quadratic transformations of x1, x3, and x5,
but each of these true features is accompanied by an al-
ready transformed proxy. These proxies are conditionally
null because they contribute no new information over the
original features, but since F is chosen to be the set of lin-
ear functions, they are risk-nonnull. Similarly, D8, based
off Example 3.3, provides features that are functionally
and marginally nonnull, but conditionally and risk null.
Any one member of the redundant pair can be removed
without losing information.
For each dataset, we applied representative feature attri-
bution (Sage1, integrated gradients), selection (correlation,
lasso, knockoffs, LOCO, GCM, MDI), and functional sen-
sitivity methods (PDP variance, permutation importance).
For MDI alone, we did not use the ground truth f and
instead fit a CART model, since MDI is not well-defined
without a tree model. For the risk-based methods, we esti-
mate a risk R∗ = inff∈F R(f) for an appropriate R and
F. We use a 70/30 train-test split, with squared error loss
and cross-entropy on the test set for continuous and binary
y, respectively. All risk-based methods use the same split,
and Sage and MinSHAP share coalitions. For all datasets
1A risk-based Shapley method [20].

18
TABLE1
Targeted null importance and theoretical guarantees for representative feature analysis methods. Results refer to population quantities unless
otherwise indicated.
Method Targeted null Theoretical guarantee Key condition
Correlation screening Marginal statistical One-way null guarantee Linear relationship
Mutual information Marginal statistical Exact identificationX j ⊥Y⇐ ⇒I(X j;Y) = 0
MDI UnclearCounterexampleRedundant features
Knockoffs Conditional statistical FDR guarantee Valid knockoff construction
GCM Conditional statistical One-way null guarantee Consistent conditional-mean
LOCO Risk-based Exact identification Population risk
Lasso Linear-model relevance Support recovery Correct sparse linear model
Risk-based Shapley Risk-basedCounterexampleShapley averaging
Causal Shapley Causal One-way null guarantee Intervention consistency
MinShap Conditional risk-based Exact identification Null monotonicity
Integrated Gradients Path-based functional One-way null guarantee Differentiability and path
Saliency maps Local functional One-way null guarantee Differentiability
Partial Dependence Marginal functional Exact identification Population PD
ALE Marginal functional One-way null guarantee Regularity and support
except D9, we used gradient boosting ensembles to rep-
resent F. For D9 we deliberately restricted F to linear
predictors, illustration a violation of Bayes completeness.
Figure 1 summarizes the resulting scores for the re-
gression case when n= 500 . The analogous figures for
n= 5000 and classification re given in Supplementary
Figures 6 - 8. Color encodes
P
k∈N |φk|P
j |φj|
where N denotes the null set defining each panel. The
importance scores are held fixed across columns, only the
null notionNvaries (Table 3).
Correlation. Since correlation is sensitive to linear asso-
ciation, it fails to assign importance to nonnull features in
D2–D4, which are nonlinear. In D5, it places importance
on features that are marginally nonnull but null under every
other notion. In D7, it places high importance on mem-
bers of the mediated chain, which are nonnull only from
marginal and interventional causal perspectives.
Lasso. Like correlation, Lasso underperforms on non-
linear datasets. In D5, it does not assign importance to
features x2, x4, and x6, since it selects only one mem-
ber from correlated groups. Therefore it outperforms risk-
based methods across every notion on this dataset. A sim-
ilar pattern appears in D8, where the correlated proxies
are given coefficients equal to zero. On D9, the Lasso’s
failure to detect the nonlinear association leads it to assign
importance to the pretransformed features, which are null
according to conditional and risk notions.
Knockoffs. Knockoffs performs similarly to Lasso,
though it is more conservative, reflected in the smaller null
importance fractions in D2 - D4. On D8, it assigns impor-
tance to some correlated proxies, though to a lesser extent
than functionally-sensitive methods. A closer comparison
with correlation in D5 is given in Figure 2a. Knockoffs
send conditionally null variables to zero, despite their high
correlation with the response. The ability to distinguish
conditionally important variables improves with sample
size n because conditional null importance is harder to
evaluate than marginal null importance.
LOCO. Since LOCO measures the drop in risk after
fitting a flexible model, it detects the nonnull quadratic
features in D2. On D3 and D4, where the signal is based
entirely on interactions, LOCO can in principle detect the
risk drop. However, this depends on accurately estimat-
ing the interaction structure, which it fails to do here. On
the redundant pairs D8, it fails even under marginal and
functional null notions. It assigns little importance to any
feature in S, since dropping one feature doesn’t substan-
tially reduce performance. Estimation error means that
features S C have scores on a comparable scale, making
the signal invisible.
GCM. GCM performs similarly to LOCO except on
D2. Since the signal features there are independent,
E[X j |X −j] = 0. After residualization, GCM tests the
association between Xj and X 2 j −1 , but since it uses co-
variance, it cannot detect the quadratic dependence.
PDP variance, Integrated Gradients, and Permuta-
tion Importance. These methods flag the same variables
as nonnull across all datasets. Their sensitivity to nonlinear
features allows them to perform well on D2–D4 and D9. In
D8 they place high importance on the correlated proxies,
which are considered null under conditional, causal, and
risk null notions, but which are functionally related to the
response.
Sage. Sage performs worse than all other methods on
the mediated chains D7. There are coalitions where all
terms downstream of an internal node are absent. On these
coalitions performance improves when adding the internal

NULL IMPORTANCE19
TABLE2
Synthetic dataset construction used in Section 5.1. Latent variables and noise terms are independent standard Gaussian variables and the response
column gives the mean functionf(x)unless otherwise indicated. The structured features are denoted byS; in our instantiation this is simply
{1, . . . ,6}. In D4 the groupsGk are pairs of adjacent variables, and in D7,q c = 2is the number of chains andL k = 3denotes the terminal leaf
node. For all datasets, we useβ= 4andγ= 3. The assignment of each feature inSto the different notions of null importance is given in Table 3.
ID Mechanism Features Response signal
D1 Linearx j iid∼ N(0,1)β X
j∈S
xj
D2 Quadraticx j iid∼ N(0,1)γ X
j∈S
(x2 j −1)
D3 Pairwise productsx j iid∼ N(0,1)γ X
k
x2k−1x2k
D4 Grouped parityx j iid∼U[−1,1]−γ X
k
Y
j∈Gk
sign(xj )
D5 Dependent features
x2k−1 =z k,
x2k =z k +τ ϵk
γ
X
k
x2k−1
D6 Confounding
xj =z j +τ ϵj ,
zj unobserved
η(z) =γ
X
j∈S
zj ,
f(x) =γ
X
j∈S
xj
D7 Mediated chains
xk,1 ∼ N(0,1),
xk,ℓ =x k,ℓ−1 +τ ϵk,ℓ
γ√qc qcX k=1 xk,Lk
D8 Redundant pairs
x2k−1 =z k,
x2k =z k +δϵ k
γ
X
k
x2k−1 +x 2k
2
D9 Quadratic proxy
uk ∼U[−1,1],
x2k−1 =u k,
x2k =u 2 k +δϵ k
γ
X
k

x2 2k−1 − 1 3 
D10 Heteroscedastic
x2k−1 =m k,
x2k =v k
E[Y|x] =γ
X
k
mk,
sd(Y|x) =σ y exp



κ
2√q
X
k
vk



TABLE3
Notions of null associated with each feature from datasets D1–D10 in Table 2. In addition to these structured features, each dataset includes twelve
independent standard normal features that are null under every notion.
Feature subset Null under notion(s) Non-null under notion(s)
D1–D3 all — all notions
D4 all marginal conditional, risk, functional, causal
D5 proxiesx 2k conditional, risk, functional, causal marginal
D6 all causal marginal, conditional, risk, functional
D7 internal nodesx kl s.t.l < Lk conditional, risk, functional marginal, causal
D8 Copiesx 2k conditional, risk, causal marginal, functional
D9 Transformationsx 2k conditional, functional, causal marginal, risk
D10 Variance featuresx 2k risk, functional marginal, conditional, causal

20
node. Averaging over coalitions, the internal nodes are
flagged as important, reinforcing the discussion of Section
4.1. See also Figure 2b.
MinSHAP. Though it is formed with the same coali-
tions as Sage, MinSHAP does not place importance on any
intermediate nodes in D7. For D3 and D4, MinSHAP as-
signs zero importance to all features due to failures of the
null monotonicity condition. Features on their own have
no predictive value but when their interaction partners are
present they become important. MinSHAP assigns zero
importance to all features in D5 as well, but for a differ-
ent reason. For the features x2k−1, the population risk is
nonzero but small, due to the presence of the highly cor-
related proxy. On finite samples, the risk differences are
subject to Monte Carlo error, and taking the minimum over
coalitions biases the importance downwards to zero.
MDI. MDI performs similarly to LOCO except on D8,
where the functional method places high importance on the
correlated proxies. This faithfulness to the functional form
of the data-generating mechanism makes it incompatible
with conditional, causal, or risk-based null notions.
The purpose of this example is not to rank one method
over others, but rather to demonstrate the concrete differ-
ences in data characteristics to which these methods are
sensitive. Even with relatively simple generative mech-
anisms, differences in functional form and dependence
structure lead to substantive differences in which features
are considered important.
5.2 Local Attributions for functional local null on
MNIST
We can similarly evaluate local attribution methods
from a null importance perspective. In particular the tar-
geted null here is the local functional null N func−local j .
We apply representative local attribution methods to the
MNIST digit classification task. Our model is a pretrained
two-stage ResNet with hidden layer widths of 32 and 64
(fxmarty/resnet-tiny-mnist on HuggingFace).
We explain 10 examples of the digit “0.” The examples
were chosen as the five examples with the highest and
lowest predicted probability of the correct class, respec-
tively. For local attribution, we apply three gradient-based
methods (saliency maps, gradient × input, and integrated
gradients) and two Shapley values-based methods (SHAP
and MinSHAP). Gradient×Input is defined as
∂f(x)
∂xj
·(x j −x ′ j)
where x′ j is the same baseline used for integrated gradi-
ents. Saliency maps and Gradient × Input use the gradient
evaluated at the observed input, while integrated gradients
averages gradients along the path from the baseline to the
observed input (see Equation 1). For both gradient based
methods, we used a discretization size of 0.001, and for in-
tegrated gradients we considered ten steps. For SHAP and
Figure 1: Relative variable importance from null or signal
features when they are assigned to alternative notions of
null importance. Each row is a synthetic data set as de-
scribed in Table 2, averaging importances across all seeds
among datasets with n= 500 and the regression task. Each
column gives a variable importance method. Gray cells
indicate cases where the relative variable importance is un-
defined, either because all features are considered nonnull
(D4 marginal and D6 causal) or because a method did not
assign positive importance to any feature.
MinSHAP, we considered the formulation with value func-
tion derived from instance-level predictions f(x) rather
than the risk-based formulation, which only applies to
global attribution. For SHAP, we used a KernelSHAP
approximation with 100 background samples and 7300
coalitions. For MinSHAP, we used an IME approximation
with 40 coalition orderings. In both cases, we use the value
function V(S) =E[f(X)|do (X S =x S)], which is ap-
propriate to local attribution. The coalition budgets were
chosen to give SHAP and MinSHAP roughly compara-
ble runtimes (1 hour under current settings), allowing the
comparison to reflect differences between the attribution
methods rather than differences driven by unequal compu-
tational runtimes. For each panel, we centered and scaled
attributions to mean zero and variance one, ensuring that
the attributions are on a comparable scale across panels.
Attribution z-scores were clipped at ±4 to prevent outliers
from dominating the heatmap.
The resulting attributions are shown in Figure 3. For
correctly predicted samples, the saliency maps are close
to zero due to vanishing gradients. Since these examples
were those with the highest predicted probabilities of the
correct class, their final layer activations are saturated and
the gradients are nearly zero. When the saliency gradient

NULL IMPORTANCE21
Figure 2: a. A comparison between correlation and knock-
off importance scores across sample sizes on dataset D5.
Only Knockoffs distinguishes between conditionally rele-
vant and null features. b. The relative contributions of each
coalition on the mediated chains task, as used by Sage and
MinSHAP. In the left panel, each row along the y-axis cor-
responds to a coalition and shows features S in grey and
new addition j in red. The rows of this figure are aligned
with those in right panel, where each bar displayed Ij (S).
is nonzero, Gradient × Input gives clearer attribution pat-
terns by downweighting pixels that are close to the zero
baseline. However, because it still uses the gradient evalu-
ated at the observed input, it also becomes zero when the
saliency gradient vanishes. This difficulty is bypassed by
integrated gradients, which produces gradients with large
magnitudes at intermediate values along the path integral,
even for correctly classified examples. This comparison
suggests that multiplying by the input can remove much
of the background variation seen in saliency, while inte-
grating gradients along the path is what allows integrated
gradients to avoid the saturation problem. For the Shapley
value-based methods, SHAP remains relatively diffuse,
while MinSHAP produces a clearer attribution patterns
around the digit. The attribution patterns could become
clearer for both methods if more coalitions are included in
computation.
This case study suggests that although these local attri-
bution methods all returned images with pixel-level impor-
tances, they can differ because they target different nulls,
like the functional vs. causal nulls targeted by the gradi-
ent and SHAP-based methods, respectively. Further, even
when they target the same null, differences in estimation
strategy can highlight or suppress particular pixels, like in
the case of saliency vs. Gradient×Input explanations.
5.3 Variable Importance in TCGA Multiomics
The synthetic data analysis showed that alternative defi-
nitions of null importance strongly influence interpretation.
While synthetic data provide ground truth, the data gen-
erating mechanisms are necessarily simplified. Next we
evaluate the impact of alternative null importance notions
on a multiomics analysis problem. A common strategy
in modern genomics is to study disease mechanisms by
predicting phenotypes from high-dimensional sequencing
assays. To ensure accurate predictions, it is often neces-
sary to use black-box models to capture nonlinearities and
interactions, but the scientific goal is mechanistic under-
standing, not simply to classify new samples. A feature
importance analysis can flag molecular features to perturb
in a follow-up experiment, to see their impact on in-vitro
disease models. In practice many methods have been used.
How do their different sensitivities to null importance no-
tions affect the resulting scientific conclusions?
We analyzed 461 samples from The Cancer Genome At-
las (TCGA). Each sample includes features from mRNA,
miRNA, and RPPA (protein) molecular assays. The data
include 362 ductal and 99 lobular tumors. Before filter-
ing, the mRNA, miRNA, and RPPA assays contain 59427,
2238, and 131 features respectively. We preprocessed the
data following [60], which benchmarked multiomic predic-
tion models on this dataset. Because several explanation
methods scale poorly in the number of features, we ap-
plied more stringent filtering than [60]. We kept the 150
most variable mRNA features, 100 most variable miRNA
features, and 50 most variable RPPA features (a total of
300 features), while [60] retained the 1000 most variable
in total after combining assays. Otherwise, we followed
their preprocessing procedure, first imputing missing val-
ues with their mean and then residualizing each feature on
age, gender, and race. We trained random forest models to
predict cancer type. Each model included 50 trees. To eval-
uate out-of-sample performance, we used stratified five-
fold cross-validation. Within each training fold, we eval-
uate the hyperparameters min_samples_leaf∈
{1,3,6},max_features∈
n
log10 d,
√
d, d 5 , d 2
o
and selected the combination that maximized the out-
of-bag Matthews correlation coefficient (MCC). The

22
Figure 3: Local feature attributions for selected ten MNIST digit-0 examples. Each row corresponds to one input image,
with its prediction status shown on the left, and each column gives the attribution from a different explanation method.
Attribution scores are standardized within each panel and displayed as z-scores. Blank saliency and Gradient × input
panels reflect near-zero gradients.

NULL IMPORTANCE23
resulting model was evaluated using that fold’s held-
out samples, and pooling across folds yields an out-of-
samples MCC of 0.618 and area under the curve of
0.770. The classifier used for methods below was fit
separately on the full dataset with hyperparameters of
(min_samples_leaf,max_features) = (6,150)
again chosen using out-of-bag MCC.
We have applied twelve methods to interpret this final
model: MDI, TreeSHAP, permutation importance, PDP
variance, integrated gradients (discretized to 64 steps), cor-
relation, lasso coefficients on standardized inputs, Gaus-
sian model-X knockoff statistics, negative logp-value from
a GCM conditional independence test, LOCO, Sage, and
MinSHAP. For the risk-based methods, we used an XG-
Boost classifier fit with a 70/30 train/test split, estimating
risk using binary cross entropy,
ˆR(S) =− 1 Ntest X i∈Test
"
Yi log ˆgS(Xi,S)
+ (1−Y i) log (1−ˆgS(Xi,S))
#
where ˆgS(x) estimates P(Y= 1|X S =x) . Each
methodmprovidesJ= 300importance estimates,
φm = (φm 1 , . . . , φm J ).
To account for randomness in the methods, we recomputed
explanations using four seeds and averaged the resulting
estimates to obtain ¯φm j . To put importance measures on
the same scale, we normalize using,
πm j =

 ¯φm j

P300
k=1

 ¯φm k

 , j= 1, . . . , J.
We applied PCA to the matrix Π =

πm j

∈R M×J . The
first two principal components are displayed in Figure 4.
We excluded MinSHAP from the PCA because it assigned
zero importance to every feature. This is consistent with
the high feature-feature correlations present in these data
– across features, the maximum absolute correlation with
any other feature has a median of 0.72.
The first principal component (PC1) explains 80.1% of
the variation in normalized feature importance profiles.
This dimension contrasts methods with diffuse vs. concen-
trated feature profiles. Methods with larger PC1 scores,
including correlation and the risk-based methods, spread
their importances across many features (Supplementary
Figure 9). If the scientific question is whether a feature
contributes predictive information or is marginally related
to the response, the diffuse profiles for these methods
suggests that most are. In contrast, methods with smaller
PC1 scores concentrate their normalized importance on
fewer features. These features are also separated along
PC2 (13.8% of variance explained) and appears to con-
trast methods emphasizing conditional independence vs.
those sensitive to functional importance. Figure 5 exam-
ines this interpretation using the partial dependence pro-
files for the three features with largest absolute PC2 load-
ings. Integrated gradients assigns high importance to fea-
tures like Beta-catenin, where the predicted class probabil-
ities rapidly transition between zero and one, even though
Knockoffs did not detect conditional dependence between
the feature and the tumor type given the remaining fea-
tures. In contrast, MIMAT0000267, which has the largest
PC2 loading, has a relatively flat partial dependence pro-
file but receives high importance under both the Lasso and
Knockoffs, both of which account for the remaining fea-
tures. E-cadherin also has a large positive loading on PC2,
but provides an intermediate case, receiving modest im-
portance under both functional and conditional relevance
notions. Because correlation, GCM, and LOCO spread
importance across many features, their normalized impor-
tance is spread thin, leading to shorter feature-level bars.
The bar lengths should not be compared directly with more
concentrated methods, as they are not absolute importance
magnitudes.
Features identified under any of these null notions could
motivate experimental follow-up. We emphasize only that
if the method’s target does not match the scientific question
– for example, if we were searching for rapid changes in
probability (functional relevance) using Knockoffs (target-
ing conditional statistical relevance), or uniquely related
features (conditional statistical relevance) using integrated
gradients (targeting functional relevance) – then we may
miss a pattern relevant to the motivating question.
6. DISCUSSION
A central message of this paper is that whether a feature
is “important” depends on the question being asked, the
data-generating process that produced the observations,
and the algorithm or value function used to analyze them.
These three components are often considered separately:
domain scientists formulate questions about which vari-
ables matter, data analysts work with an observed joint
distribution, and learning algorithms quantify the contri-
bution of variables to a particular predictive or functional
objective. The notion ofnull importanceprovides a com-
mon language for connecting these perspectives.
The key advantage of this language is that it makes ex-
plicit what it means for a feature to be irrelevant. In the
framework developed in this paper, functional, statistical
(marginal and conditional), risk-based, and causal notions
of null importance correspond to different answers to the
question of what should remain invariant when a feature
is removed or changed. These notions are not generally
equivalent. Their relationships depend on properties of the
data-generating process, such as dependence, redundancy,

24
correlationpermutation sage
knockoffs
pdp_variance
integrated_gradients
gcm
lasso
loco
mdi treeshap
−0.2
0.0
0.2
−0.6 −0.4 −0.2 0.0
PC1 (80.6%)
PC2 (14.2%)
(a) Method scores
PC2 (14.2%)
ecadherin
betacatenin
mimat0000267
mimat0002868
linc00993
mimat0004780
hmgcs2
ar
mimat0015085
fabp4
npy1r
igkv1−16
scgb1d2
cyp4z1
mimat0000262
collagenvi
mimat0000707
p70s6k
mimat0022696
eralphaps118
mimat0000688
cyp4x1
mimat0018101
mimat0000761
dscam−as1
eef1a2
serpina6
apod
mimat0019059
mimat0004784
claudin7
mimat0000253
mimat0001631
mimat0004929
mimat0004980
cyclinb1
areg
atm
casp14
scgb2a2
mimat0006790
ac044784.1
mimat0022472
mimat0000281
mimat0004946
mimat0026738
fibronectin
s6ps240s244
caveolin1
cyp2t1p
egfrpy1173
mimat0000102
tff1
al157387.1
syk
ugt2b11
mimat0001413
accps79
s100a8
egfrpy1068
eralpha
mimat0003283
cxcl14
iglv6−57
tcn1
hsp70
mimat0004499
mimat0004550
s6ps235s236
bak
maob
rbps807s811
mimat0000454
ighg3
mimat0015030
nkain1
mimat0004951
mimat0004584
mimat0000646
mimat0003393
bex1
ceacam6
crabp1
kcnj3
clic6
mimat0000462
mimat0004599
pvalb
inpp4b
mimat0004809
igkv3−11
wfdc2
mimat0017985
acc1
mimat0002869
ighv7−4−1
caspase7cleavedd198
mimat0004978
s100p
cmyc
PC1 (80.6%)
betacatenin
mimat0002868
ar
igkv1−16
mimat0015085
collagenvi
p70s6k
mimat0022696
eralphaps118
mimat0000688
mimat0000761
mimat0018101
dscam−as1
serpina6
eef1a2
apod
mimat0004784
mimat0019059
atm
ac044784.1
casp14
cyclinb1
mimat0022472
fibronectin
mimat0000253
mimat0006790
egfrpy1173
mimat0004980
mimat0001631
areg
mimat0004929
s6ps240s244
cyp4x1
iglv6−57
mimat0000102
mimat0004946
caveolin1
s6ps235s236
cyp2t1p
ugt2b11
mimat0000281
eralpha
bak
mimat0003283
syk
al157387.1
accps79
mimat0004499
mimat0001413
mimat0026738
mimat0003393
mimat0004550
mimat0004951
cxcl14
bex1
igkv3−11
ceacam6
clic6
hsp70
tcn1
kcnj3
nkain1
mimat0004978
mimat0002869
egfrpy1068
mimat0004599
wfdc2
mimat0017985
iglv3−25
mimat0000266
s100a9
mimat0000462
mimat0004584
bcl2
pvalb
caspase7cleavedd198
mimat0000089
dhrs2
maob
crabp1
iglc3
s100p
claudin7
fdcsp
rbps807s811
mimat0015030
mimat0000454
scgb2a2
tff1
mimat0000707
mimat0000262
scgb1d2
fabp4
cyp4z1
mimat0004780
npy1r
hmgcs2
linc00993
ecadherin
mimat0000267
mirna
mrna
protein
mirna
mrna
protein
Feature
Measurement Assay
(b) Feature loadings
Sign negative positive
|Loading| 0.2 0.4 0.6
Figure 4: PCA of πm j importances from the TCGA example. Panel (a) organizes the methods according to the top two
principal component scores. Panel (b) is a Hinton diagram that shows the 50 features that contribute the largest loadings to
either PC1 or PC2.
noise, confounding, and interactions, as well as on assump-
tions about the model class and the value function used by
the algorithm.
This separation is important because the scientific ques-
tion and the available data need not identify the same
notion of relevance. A domain scientist may ask whether
a variable is causally relevant to an outcome, while the
available data support only an observational or predictive
question. Similarly, an algorithm may assign a feature high
importance because it improves prediction, even when
the scientific question concerns functional necessity. Con-
versely, a feature may be scientifically relevant but receive
little importance under a particular predictive objective
because its information is redundant with other variables.
Null importance makes these distinctions explicit: rather
than asking whether a feature is important in the abstract,
one can ask under which notion of irrelevance the feature is
null, and under what assumptions that notion corresponds
to the scientific question of interest.
The equivalence results in this paper identify conditions
under which these different perspectives can be aligned.
For instance, Lemma 1 shows that functional and condi-
tional statistical nullity coincide only under deterministic,
non-redundant, and sufficient regimes and Lemma 2 es-
tablishes that risk-based and conditional statistical nullity
coincide only under well-specification and sufficiently rich
function classes. These results specify when an algorithmic
notion of null importance can be interpreted as evidence
for a particular scientific notion of irrelevance.
The counterexamples illustrate why such alignment can-
not be assumed in general. Redundancy can make a feature
statistically informative without making it functionally nec-
essary, interactions can make relevance inherently joint and
therefore invisible to certain local measures, and confound-
ing can produce observational relevance without causal

NULL IMPORTANCE25
0.0
0.5
1.0
−2 0 2
Feature value
Prediction probability
BETACATENIN
knockoffs
gcm
loco
correlation
sage
lasso
treeshap
permutation
mdi
integrated_gradients
pdp_variance
0.0% 10.0% 20.0% 30.0% 40.0%
Fraction of absolute importances
0.0
0.5
1.0
−7.5 −5.0 −2.5 0.0 2.5 5.0
Feature value
Prediction probability
MIMAT0000267
integrated_gradients
gcm
correlation
loco
sage
mdi
treeshap
permutation
pdp_variance
knockoffs
lasso
0.0% 10.0% 20.0%
Fraction of absolute importances
0.0
0.5
1.0
−4 −2 0 2
Feature value
Prediction probability
ECADHERIN
gcm
correlation
loco
sage
treeshap
mdi
permutation
integrated_gradients
lasso
pdp_variance
knockoffs
0.0% 20.0% 40.0%
Fraction of absolute importances
Actual class Infiltrating Ductal Carcinoma Infiltrating Lobular Carcinoma
Figure 5: Features with large-magnitude loadings on PC2
in the TCGA multiomics analysis. Left panels show partial
dependence profiles for each feature, with points colored
by observed cancer type. Right panels show the fraction of
absolute importance assigned to the corresponding feature
by each method.
relevance. These are not merely failure modes of partic-
ular feature importance methods. They are consequences
of a mismatch between the scientific question, the struc-
ture of the data-generating process, and the value function
encoded by the algorithm. In this sense, disagreement be-
tween feature importance methods can be scientifically
informative because it may reveal that the methods are an-
swering different questions rather than that one of them is
simply incorrect. These equivalences and counterexamples
were reflected in the synthetic and real data results across
different interpretable feature analysis methods.
This perspective also suggests a practical role for null
importance as acommunication and validation tool. In
applied work, interpretable feature analysis is often used
in collaboration with practitioners, domain scientists, or
other stakeholders who have a substantive notion of what
it means for a variable to matter. The term “important” can
conceal substantial ambiguity in such collaborations. A
practitioner may mean that changing the variable would
change the outcome, a scientist may mean that the variable
has a causal effect, and a machine-learning practitioner
may mean that removing the variable increases prediction
error. By explicitly stating the corresponding null impor-
tance, these interpretations can be distinguished and com-
pared. This provides a common vocabulary for discussing
what a feature importance analysis establishes, what as-
sumptions connect the analysis to the scientific question,
and what conclusions can legitimately be drawn from the
result.
Viewed this way, interpretable feature analysis is not
only a problem of constructing or estimating importance
scores. It is a problem of aligning ascientific question, a
data-generating process, and analgorithmic value func-
tion. Null importance provides a useful organizing prin-
ciple for this alignment because it forces the analyst to
specify what notion of irrelevance is being tested. The
framework developed here consequently provides a way to
make assumptions visible, identify when different notions
of relevance coincide, and diagnose when they necessarily
diverge.
6.0.0.1 Extensions to learned representations.Although
the paper focuses on raw input features (X1, . . . , Xp), the
same framework applies to learned or hidden representa-
tions. Let U= (u 1, . . . , um) denote a collection of explana-
tory units, where a unit may be a latent feature, learned
concept, attention head, or computational component. Null
importance can be defined for these units by replacing the
raw feature set with U and specifying the relevant value
function.
The distinction between the scientific question, the data-
generating process, and the algorithm is particularly im-
portant in this setting. Learned units are themselves con-
structed by an algorithm and may be redundant, distributed,
or non-identifiable. Consequently, a unit that is null under
one value function need not be null under another, and
algorithmic necessity need not correspond directly to a
scientifically meaningful notion of relevance. This issue
arises naturally in representation learning and mechanistic
interpretability, including work on sparse and monoseman-
tic representations [14, 21, 78]. Extending the taxonomy
of null importance to learned representations provides a
way to study how their components relate to the underlying
data-generating process and to the scientific questions that
the representation were built to answer.
6.0.0.2 Extensions from individual features to subsets.
A second extension concerns subsets of features. The anal-
ysis in this paper focuses on the null importance of an
individual feature Xj, but the same questions arise for
groups of variables. For a subset S⊆ {1, . . . , p}, one may
ask whether XS is null and, conversely, whether there
exists a smallest subsetSwhose complement is null.
These questions become particularly important when
the scientific question concerns a collection of variables,
or when the data-generating process contains redundancy

26
and interactions. A feature may be individually null be-
cause another feature carries the same information, while
a group of features may be jointly necessary. Conversely,
several different subsets may provide equivalent informa-
tion for the value function. Thus, individual feature im-
portance need not identify the smallest scientifically or
predictively relevant set of variables. Interaction measures
and cooperative-game formulations provide related per-
spectives on these issues [52, 34].
A subset-level extension of null importance would there-
fore need to specify not only which features are being
considered jointly, but also the relevant notion of joint
irrelevance and the value function against which it is as-
sessed. As with individual features, this would provide a
language for distinguishing scientific relevance from sta-
tistical, predictive, or functional necessity at the group
level.
REFERENCES
[1] ADEBAYO, J., GILMER, J., MUELLY, M., GOODFELLOW, I.,
HARDT, M. and KIM, B. (2018). Sanity Checks for Saliency
Maps. InAdvances in Neural Information Processing Systems31
9505–9515.
[2] AKAIKE, H. (1974). A new look at the statistical model identifi-
cation.IEEE Transactions on Automatic Control19716–723.
[3] APLEY, D. W. (2023). Conditional Feature Importance for Mixed
Data.AStA Advances in Statistical Analysis. Metadata to verify.
[4] APLEY, D. W. and ZHU, J. (2020). Visualizing the Effects of
Predictor Variables in Black Box Supervised Learning Models.
Journal of the Royal Statistical Society: Series B821059–1086.
[5] ARRIETA, A. B., DÍAZ-RODRÍGUEZ, N., DELSER, J., BEN-
NETOT, A., TABIK, S., BARBADO, A., GARCIA, S., GIL-
LÓPEZ, S., MOLINA, D., BENJAMINS, R., CHATILA, R. and
HERRERA, F. (2020). Explainable Artificial Intelligence (XAI):
Concepts, Taxonomies, Opportunities and Challenges toward Re-
sponsible AI.Information Fusion5882–115.
[6] BACH, S., BINDER, A., MONTAVON, G., KLAUSCHEN, F.,
MÜLLER, K.-R. and SAMEK, W. (2015). On Pixel-Wise Ex-
planations for Non-Linear Classifier Decisions by Layer-Wise
Relevance Propagation.PLoS ONE10e0130140.
[7] BARBER, R. F. and CANDÈS, E. (2015). Controlling the False
Discovery Rate via Knockoffs.Annals of Statistics432055–2085.
[8] BAROCAS, S. and SELBST, A. D. (2016). Big data’s disparate
impact.California Law Review104671–732.
[9] BARRY, T., WANG, X., MORRIS, J. A., ROEDER, K. and KATSE-
VICH, E. (2021). SCEPTRE improves calibration and sensitivity
in single-cell CRISPR screen analysis.Genome biology22344.
[10] BATTITI, R. (1994). Using Mutual Information for Selecting Fea-
tures in Supervised Neural Net Learning.IEEE Transactions on
Neural Networks5537–550. https://doi.org/10.1109/72.298224
[11] BERRETT, T. B., SAMWORTH, R. J. and YUAN, M. (2021).
Efficient Gradient-Based Testing of Conditional Independence.
Journal of the Royal Statistical Society: Series B.
[12] BREIMAN, L. (2001). Statistical modeling: The two cultures
(with comments and a rejoinder by the author).Statistical Science
16199–231. https://doi.org/10.1214/ss/1009213726
[13] BREIMAN, L. (2001). Random Forests.Machine Learning45
5–32. https://doi.org/10.1023/A:1010933404324
[14] BRICKEN, T., TEMPLETON, A., BATSON, J., CHEN, B. et al.
(2023). Towards Monosemanticity: Decomposing Language Mod-
els with Dictionary Learning.Transformer Circuits Thread.
[15] CANDÈS, E., FAN, Y., JANSON, L. and LV, J. (2018). Panning
for Gold: Model-X Knockoffs for High Dimensional Controlled
Variable Selection.Journal of the Royal Statistical Society: Series
B80551–577. https://doi.org/10.1111/rssb.12265
[16] CASELLA, G. and BERGER, R. L. (2002).Statistical Inference,
2 ed. Duxbury.
[17] CATON, S. and HAAS, C. (2024). Fairness in Machine Learning:
A Survey.ACM Computing Surveys561–38. https://doi.org/10.
1145/3616865
[18] CHOULDECHOVA, A. (2017). Fair prediction with disparate im-
pact: A study of bias in recidivism prediction instruments.Big
Data5153–163.
[19] COVERT, I. and LEE, S.-I. (2021). Improving KernelSHAP: Prac-
tical Shapley Value Estimation Using Linear Regression.Proceed-
ings of AISTATS130788–797.
[20] COVERT, I., LUNDBERG, S. M. and LEE, S.-I. (2020). Under-
standing Global Feature Contributions with Additive Importance
Measures.Advances in Neural Information Processing Systems.
[21] CUNNINGHAM, H., EWART, A., RIGGS, L., HUBEN, R.
and SHARKEY, L. (2023). Sparse Autoencoders Find Highly
Interpretable Features in Language Models.arXiv preprint
arXiv:2309.08600.
[22] DATTA, A., FREDRIKSON, M., KO, G., MARDZIEL, P. and
SEN, S. (2017). Proxy Non-Discrimination in Data-Driven Sys-
tems.arXiv preprint arXiv:1707.08120.
[23] DAWID, A. P. (1979). Conditional Independence in Statistical
Theory.Journal of the Royal Statistical Society: Series B (Method-
ological)411–15. https://doi.org/10.1111/j.2517-6161.1979.
tb01052.x
[24] DOSHI-VELEZ, F. and KIM, B. (2017). Towards a Rigor-
ous Science of Interpretable Machine Learning.arXiv preprint
arXiv:1702.08608.
[25] DWORK, C., HARDT, M., PITASSI, T., REINGOLD, O. and
ZEMEL, R. (2012). Fairness through awareness. InProceedings of
the 3rd Innovations in Theoretical Computer Science Conference
214–226. ACM.
[26] FAN, J. and LV, J. (2008). Sure Independence Screening for
Ultrahigh Dimensional Feature Space.Journal of the Royal Sta-
tistical Society: Series B70849–911. https://doi.org/10.1111/j.
1467-9868.2008.00674.x
[27] FAN, J. and SONG, R. (2010). Sure Independence Screening in
Generalized Linear Models with NP-Dimensionality.Annals of
Statistics383567–3604.
[28] FISHER, A., RUDIN, C. and DOMINICI, F. (2019). All Models are
Wrong, but Many are Useful: Learning a Variable’s Importance
by Studying an Entire Class of Prediction Models Simultaneously.
Journal of Machine Learning Research201–81.
[29] FISHER, R. A. (1925).Statistical Methods for Research Workers.
Oliver and Boyd.
[30] FRIEDMAN, J. H. (2001). Greedy Function Approximation: A
Gradient Boosting Machine.Annals of Statistics291189–1232.
[31] FRYE, C. and STRÜMKE, I. (2019). Modeling the Predictive
Value of Features with Shapley Values.arXiv.
[32] GNEITING, T. and RAFTERY, A. E. (2007). Strictly Proper Scor-
ing Rules, Prediction, and Estimation.Journal of the American
Statistical Association102359–378. https://doi.org/10.1198/
016214506000001437
[33] GOLDSTEIN, A., KAPELNER, A., BLEICH, J. and PITKIN, E.
(2015). Peeking Inside the Black Box: Visualizing Statistical
Learning with Plots of Individual Conditional Expectation.Jour-
nal of Computational and Graphical Statistics2444–65.
[34] GRABISCH, M. and ROUBENS, M. (1999). An Axiomatization
of the Shapley Interaction Index.Proceedings of the International
Conference on Artificial Intelligence and Statistics.

NULL IMPORTANCE27
[35] GRETTON, A., BOUSQUET, O., SMOLA, A. and SCHÖLKOPF, B.
(2005). Measuring Statistical Dependence with Hilbert-Schmidt
Norms.Proceedings of ALT63–77.
[36] GRETTON, A., FUKUMIZU, K., HARCHAOUI, Z., SRIPERUM-
BUDUR, B. K. et al. (2008). A Kernel Statistical Test of Indepen-
dence.Advances in Neural Information Processing Systems.
[37] GUIDOTTI, R., MONREALE, A., RUGGIERI, S., TURINI, F., GI-
ANNOTTI, F. and PEDRESCHI, D. (2018). A Survey of Methods
for Explaining Black Box Models.ACM Computing Surveys51
93.
[38] GUYON, I. and ELISSEEFF, A. (2003). An Introduction to Vari-
able and Feature Selection.Journal of Machine Learning Re-
search31157–1182.
[39] HARDT, M., PRICE, E. and SREBRO, N. (2016). Equality of
Opportunity in Supervised Learning. InAdvances in Neural Infor-
mation Processing Systems 29 (NIPS 2016)3315–3323. Curran
Associates, Inc.
[40] HERNÁN, M. A. and ROBINS, J. M. (2023).Causal Inference:
What If. Chapman & Hall/CRC, Boca Raton.
[41] HESKES, T., SIJBEN, E., BUCUR, I. G. and CLAASSEN, T.
(2020). Causal Shapley Values: Exploiting Causal Knowledge to
Explain Individual Predictions of Complex Models. InAdvances
in Neural Information Processing Systems33.
[42] JANZING, D., MINORICS, L. and BLÖBAUM, P. (2020). Feature
Relevance Quantification in Explainable AI: A Causal Problem.
Proceedings of the 23rd International Conference on Artificial
Intelligence and Statistics1082907–2916.
[43] KILBERTUS, N., ROJAS-CARULLA, M., PARASCANDOLO, G.,
HARDT, M., JANZING, D. and SCHÖLKOPF, B. (2017). Avoiding
discrimination through causal reasoning. InAdvances in Neural
Information Processing Systems30656–666.
[44] KLEINBERG, J., MULLAINATHAN, S. and RAGHAVAN, M.
(2016). Inherent trade-offs in the fair determination of risk scores.
arXiv preprint arXiv:1609.05807.
[45] KOCAOGLU, M., SNYDER, E., HAIR, A. and DIMAKIS, A. G.
(2018). CausalGAN: Learning Causal Implicit Generative Models
with Adversarial Training.arXiv preprint arXiv:1709.02023.
[46] KOHAVI, R. and JOHN, G. H. (1997). Wrappers for Feature
Subset Selection.Artificial Intelligence97273–324.
[47] KUSNER, M. J., LOFTUS, J., RUSSELL, C. and SILVA, R. (2017).
Counterfactual Fairness. InAdvances in Neural Information Pro-
cessing Systems 30 (NIPS 2017)4066–4076. Curran Associates,
Inc.
[48] LEI, J., G’SELL, M., RINALDO, A., TIBSHIRANI, R. J. and
WASSERMAN, L. (2018). Distribution-Free Predictive Inference
for Regression.Journal of the American Statistical Association
1131094–1111.
[49] LIPTON, Z. C. (2018). The Mythos of Model Interpretability: A
Diagnostic Taxonomy.Communications of the ACM6136–43.
[50] LIU, Q., ZHANG, Q., DU, J., ZHAO, S. and WANG, J. (2025).
Effects of Distance Metrics and Scaling on the Perturbation Dis-
crimination Score. https://doi.org/10.48550/ARXIV .2511.16954
[51] LUNDBERG, S. M., ERION, G., CHEN, H., DEGRAVE, A.,
PRUTKIN, J. M., NAIR, B., KATZ, R., HIMMELFARB, J. and
BANSAL, S.-I. L. (2020). Explainable AI for Trees: From Local
Explanations to Global Understanding.Nature Machine Intelli-
gence256–67.
[52] LUNDBERG, S. M., ERION, G. and LEE, S.-I. (2018). Consistent
Individualized Feature Attribution for Tree Ensembles.arXiv
preprint arXiv:1802.03888.
[53] LUNDBERG, S. M. and LEE, S.-I. (2017). A Unified Approach
to Interpreting Model Predictions. InAdvances in Neural Infor-
mation Processing Systems30.
[54] MEHRABI, N., MORSTATTER, F., SAXENA, N., LERMAN, K.
and GALSTYAN, A. (2021). A Survey on Bias and Fairness in
Machine Learning.ACM Computing Surveys541–35. https:
//doi.org/10.1145/3457607
[55] MEJIA, G. M., MILLER, H. E., LEBLANC, F. J. A., WANG, B.,
SWAIN, B. and CAMILLO, L. P.D. L. (2025). Diversity by De-
sign: Addressing Mode Collapse Improves scRNA-seq Pertur-
bation Modeling on Well-Calibrated Metrics. https://doi.org/10.
48550/ARXIV .2506.22641
[56] MILLER, T. (2019). Explanation in Artificial Intelligence: In-
sights from the Social Sciences.Artificial Intelligence2671–38.
[57] MOLNAR, C. (2022). Interpretable Machine Learning. Book, 2nd
edition.
[58] MURDOCH, W. J., SINGH, C., KUMBIER, K., ABBASI-ASL, R.
and YU, B. (2019). Definitions, methods, and applications in
interpretable machine learning.Proceedings of the National
Academy of Sciences11622071–22080. https://doi.org/10.1073/
pnas.1900654116
[59] NICOL, P. (2026). Spurious correlation inflates performance in
single-cell perturbation prediction.bioRxiv2026–05. https://doi.
org/10.64898/2026.05.07.723486
[60] NOVOLOACA, A., BROC, C., BELOEIL, L., YU, W.-H. and
BECKER, J. (2024). Comparative analysis of integrative classifi-
cation methods for multi-omics data.Briefings in Bioinformatics
25. https://doi.org/10.1093/bib/bbae331
[61] OTA, M., SPENCE, J. P., ZENG, T., DANN, E., MILIND, N.,
MARSON, A. and PRITCHARD, J. K. (2025). Causal modelling
of gene effects from regulators to programs to traits.Nature650
399–408. https://doi.org/10.1038/s41586-025-09866-3
[62] PEARL, J. (2009).Causality: Models, Reasoning, and Inference,
2 ed. Cambridge University Press.
[63] PENG, H., LONG, F. and DING, C. (2005). Feature Selection
Based on Mutual Information Criteria of Max-Dependency, Max-
Relevance, and Min-Redundancy.IEEE Transactions on Pattern
Analysis and Machine Intelligence271226–1238.
[64] PETERS, J., JANZING, D. and SCHÖLKOPF, B. (2017).Elements
of Causal Inference: Foundations and Learning Algorithms.Adap-
tive Computation and Machine Learning Series. The MIT Press,
Cambridge, MA.
[65] RIBEIRO, M. T., SINGH, S. and GUESTRIN, C. (2016). Why
Should I Trust You? Explaining the Predictions of Any Classifier.
InProceedings of the 22nd ACM SIGKDD International Confer-
ence on Knowledge Discovery and Data Mining1135–1144.
[66] RUBIN, D. B. (1974). Estimating causal effects of treatments in
randomized and nonrandomized studies.Journal of Educational
Psychology66688–701. https://doi.org/10.1037/h0037350
[67] RUDIN, C. (2019). Stop Explaining Black Box Machine Learning
Models for High Stakes Decisions and Use Interpretable Models
Instead.Nature Machine Intelligence1206–215.
[68] SELVARAJU, R. R., COGSWELL, A., DAS, A., VEDANTAM, R.,
PARIKH, D. and BATRA, D. (2017). Grad-CAM: Visual Explana-
tions from Deep Networks via Gradient-Based Localization. In
Proceedings of the IEEE International Conference on Computer
Vision618–626.
[69] SHAH, R. D. and PETERS, J. (2020). The Hardness of Con-
ditional Independence Testing and the Generalised Covariance
Measure.Annals of Statistics481514–1538.
[70] SHAPLEY, L. S. (1953). A Value for n-Person Games.Contribu-
tions to the Theory of Games2307–317.
[71] SHRIKUMAR, A., GREENSIDE, P. and KUNDAJE, A. (2017).
Learning Important Features Through Propagating Activation
Differences. InProceedings of the 34th International Conference
on Machine Learning703145–3153.

28
[72] SIMONYAN, K., VEDALDI, A. and ZISSERMAN, A. (2014). Deep
Inside Convolutional Networks: Visualising Image Classification
Models and Saliency Maps. InInternational Conference on Learn-
ing Representations.
[73] SMILKOV, D., THORAT, N., KIM, B., VIÉGAS, F. and WAT-
TENBERG, M. (2017). SmoothGrad: Removing Noise by Adding
Noise.arXiv preprint arXiv:1706.03825.
[74] STROBL, C., BOULESTEIX, A.-L., KNEIB, T., AUGUSTIN, T.
and ZEILEIS, A. (2008). Conditional Variable Importance for
Random Forests.BMC Bioinformatics9307.
[75] STROBL, C., BOULESTEIX, A.-L., ZEILEIS, A. and
HOTHORN, T. (2007). Bias in Random Forest Variable
Importance Measures: Illustrations, Sources and a Solution.BMC
Bioinformatics825.
[76] SUNDARARAJAN, M., TALY, A. and YAN, Q. (2017). Axiomatic
Attribution for Deep Networks. InProceedings of the 34th Inter-
national Conference on Machine Learning703319–3328.
[77] SZÉKELY, G. J., RIZZO, M. L. and BAKIROV, N. K. (2007).
Measuring and Testing Dependence by Correlation of Distances.
Annals of Statistics352769–2794.
[78] TEMPLETON, A., CONERLY, T., MARCUS, J., LINDSEY, J.,
BRICKEN, T. et al. (2024). Scaling Monosemanticity: Extract-
ing Interpretable Features from Claude 3 Sonnet.Transformer
Circuits Thread.
[79] TIBSHIRANI, R. (1996). Regression Shrinkage and Selection via
the Lasso.Journal of the Royal Statistical Society: Series B58
267–288.
[80] VEALE, M., VANKLEEK, M. and BINNS, R. (2018). Fairness
and accountability design needs for algorithmic support in high-
stakes public sector decision-making. InProceedings of the 2018
CHI Conference on Human Factors in Computing Systems1–14.
[81] VERMA, S. and RUBIN, J. (2018). Fairness Definitions Ex-
plained.
[82] VOLLENWEIDER, M. and BÜHLMANN, P. (2026). Signal,
Bounds, and Baselines: Principles for Evaluating Virtual Cell
Perturbation Models.bioRxiv2026–04. https://doi.org/10.64898/
2026.04.20.719650
[83] YU, B. (2013). Stability.Bernoulli191484–1500.
[84] YU, B. and KUMBIER, K. (2020). Veridical Data Science.Pro-
ceedings of the National Academy of Sciences1173920–3929.
[85] ZHENG, C. and RASKUTTI, G. (2026). MinShap: A Shapley-
Based Framework for Feature Redundancy.arXiv.
APPENDIX A: SUPPLEMENTARY FIGURES
Figure 6: The analog of Figure 1 when n= 5000 . The
same trends appear.
Figure 7: The analog of Figure 1 for classification.

NULL IMPORTANCE29
Figure 8: The analog of Figure 1 for classification and
whenn= 5000.
correlationpermutation
sage
knockoffs
pdp_variance
pdp_variance integrated_gradients
gcm
gcm
lasso
lasso
lasso
loco
loco
mdi
treeshap
correlation
permutation
sage
knockoffs
pdp_variance
pdp_variance
integrated_gradients
gcm
gcm
lasso
lasso
lasso
loco
loco
mdi
treeshap
PC2
−0.6 −0.4 −0.2 0.0
PC1
−0.2 0.0 0.2
conditional
functional
marginal
risk
conditional
functional
marginal
risk
Score
Category
Method score by null−importance category
−0.8
−0.6
−0.4
−0.2
0.0
0.1 0.2
Mean |correlation| with other features
PC1 loading
Omic mirna mrna protein
Spearman rho = 0.28
PC1 loading vs. feature's correlation with the rest of the data
−0.75
−0.50
−0.25
0.00
0.25
0.50
0.4 0.6 0.8
PDP curve Gini (sharp local jump vs. gradual change)
PC2 loading
Omic mirna mrna protein
Spearman rho = −0.27
PC2 loading vs. concentration of the feature's PDP curve
correlation
permutation
sage
knockoffs
pdp_variance
integrated_gradients
gcm
lasso
loco
mdi
treeshap
rho = −0.92
correlation
permutation
sage
knockoffs
pdp_variance
integrated_gradients
gcm
lasso
loco
mdi
treeshap
rho = −0.94
gini top_k_frac
0.4 0.6 0.8 1.0 0.25 0.50 0.75 1.00
−0.6
−0.4
−0.2
0.0
Concentration metric
PC1 score
Method PC1 score vs. importance−mass concentration
0.00
0.25
0.50
0.75
1.00
0 100 200 300
Feature rank
Cumulative importance
Method
pdp_variance
knockoffs
lasso
integrated_gradients
mdi
permutation
treeshap
sage
loco
correlation
gcm
PC1/PC2 diagnostics
Figure 9: Cumulative variable importances on the TCGA
case study. The color gradient has been organized by the
PC1 score shown in Figure 4.
B. CASE STUDY MATERIALS
Data to replicate the case studies have been deposited on
Figshare (https://doi.org/10.6084/m9.figshare.33857824).
A code repository is available on GitHub (https://github.
com/krisrs1128/null_importance).
