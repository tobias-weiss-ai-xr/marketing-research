---
title: 'Splitting the Difference: Interpretable Causal Forests for Treatment Effect Heterogeneity and
  Bias'
url: https://arxiv.org/abs/2609.16971
category: ai-marketing
subcategory: measurement
date: 2026-09
venue: ''
authors:
- Nicolas Alexander Ihlo
- Merle Behr
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.16971
pages: 43
chars: 95193
fetched_at: '2026-11-08T13:25:01+00:00'
kb_version: 1
---

# Splitting the Difference: Interpretable Causal Forests for Treatment Effect Heterogeneity and Bias

Splitting the Difference: Interpretable
Causal Forests for Treatment Effect
Heterogeneity and Bias
Nicolas Alexander Ihlo∗, Merle Behr†
Faculty of Informatics and Data Science
University of Regensburg, Germany
September 15, 2026
In various fields, such as medicine and marketing, accurately predicting
individual treatment effects holds significant promise. However, achieving
reliable predictions alone is often insufficient for making informed decisions; it
is equally important to understand why the treatment effect is higher for some
individuals than for others. To address this two-fold challenge of prediction
and interpretation, we introduce an algorithm based on decision trees and
random forests for estimating individual treatment effects. Our algorithm
is simple: it operates exactly like a standard random forest, but with a
different splitting criterion, and requires no additional workarounds such as
double machine learning or orthogonalization as used in Generalized random
forests. It handles observational studies with varying treatment propensities
without requiring separate estimation of the full propensity function. This
is achieved by combining two splitting criteria—one targeting heterogeneity
in the treatment effect, the other targeting bias correction for the average
treatment effect—which together improve split point selection and automati-
cally distinguish confounders from features responsible for heterogeneity. As
a result, interpretation follows directly from the fitted tree structure itself,
that is, from which features the trees split on and with which split statistics,
without requiring separate post-hoc analysis. For the theoretical analysis
of this algorithm, we consider a change point model with step functions for
potential outcomes and treatment propensity and provide insights into the
theoretical underpinnings of our approach. Simulation studies show that our
∗nicolas.ihlo@ur.de
†merle.behr@ur.de
1
arXiv:2609.16971v1  [stat.ML]  15 Sep 2026

simple algorithm achieves comparable, and often better, prediction accuracy
than existing methods, while substantially improving interpretability.
Keywords:causal inference, statistical machine learning, interpretable machine learning,
heterogeneous treatment effect estimation
1. Introduction
Estimating treatment effects, i.e., changes in an outcome due to some intervention, is of
interest across many fields [Manski, 1993, Imbens and Rubin, 2015, Angrist and Pischke,
2015], including medicine, marketing, public policy, and economics. Beyond average
effects, many applications benefit from individual-level estimates: for example, estimating
the effectiveness of a drug for a specific patient enables individualized medicine. For such
estimates to be useful in practice, however, accurate predictions are often not enough
by themselves; understanding why the treatment effect differs across individuals, i.e.,
interpreting the estimation method, is equally important. In this paper, we focus on the
estimation of individual treatment effects with a particular emphasis on interpretability.
In many settings, treatment effects cannot be estimated from randomized experiments
and one has to rely on observational data instead. This introduces the problem of
confounding: features that influence both the outcome and the treatment propensity, and
which can bias treatment effect estimates even when they do not affect the treatment
effect itself [Hernan and Robins, 2020]. Crucially, this means a feature can appear relevant
to treatment effect estimation for two entirely different reasons: either because it is a
confounder that must be corrected for, or because it genuinely drives treatment effect
heterogeneity. Distinguishing between these two cases is precisely the interpretation we
are interested in. Throughout this paper, we assume that all confounders are observed,
i.e., we rule out hidden confounding, and focus on the estimation of individual treatment
effects under observed confounding.
Machine learning (ML) methods are well suited to this task, as they can learn flexible
structures directly from data with little manual adjustment. General supervised learning
methods, originally developed for classification or regression, can be adapted for treatment
effect estimation, for example via metalearners [K¨ unzel et al., 2019] and double/debiased
machine learning (DML) [Chernozhukov et al., 2018]; other methods are purpose-built
for causal inference, building on neural networks, for example TarNet [Shalit et al., 2017],
DragonNet [Shi et al., 2019], and RA-Net [Curth and van der Schaar, 2021]. However,
many of the most powerful ML methods act as black boxes and offer little insight into
their prediction mechanism, even though such insight is often required for interpretation
and downstream decision-making.
Random forest (RF) [Breiman, 2001], originally developed for supervised learning but
since extended to causal inference as well, offers a compromise between these two goals: it
achieves state-of-the-art prediction accuracy, particularly on tabular data [Shmuel et al.,
2025], while remaining, to a certain extent, interpretable through its underlying tree
structure. This structure has, for instance, been used to gain insight into the mechanism
of the fitted forest, e.g., by feature importance statistics such as mean decrease in impurity
2

(MDI) [Breiman, 2001], as well as several extensions and other approaches, e.g., MDI+
[Agarwal et al., 2025], iRF [Basu et al., 2018], LSSFind [Behr et al., 2022], and TreeSHAP
[Lundberg et al., 2020].
Several RF-type algorithms have been proposed for estimating treatment effects, and it
is this line of work that we build on and extend in this paper; we review these approaches
in the following subsection. Our main motivation for building on RF, rather than a
black-box method such as a neural network, is its interpretability, and accordingly, our
goal is to preserve as much of this interpretability as possible in the RF-type algorithm
we propose.
1.1. Previous Tree-based Methods for Causal Inference
A popular adaptation of RF is causal forest [Wager and Athey, 2018], which itself uses
a simplified version of the causal-inference-specific adaptation of decision trees, causal
tree, introduced by Athey and Imbens [2016]. While causal forest proposes two possible
procedures, we focus here on procedure 1 (double sample trees), as only it incorporates
outcomes in the construction of the trees and is therefore able to model treatment effect
heterogeneity via the tree structure. Both causal tree and causal forest build trees by
selecting splits that maximize the variance of treatment effect predictions, a criterion
derived from an analogy to mean squared error (MSE) minimization in regression (see
Section 3.1 for details); however, this analogy relies on properties of the regression
setting that do not hold in general for causal inference, and the resulting susceptibility
to confounding has been noted previously, e.g., by Athey et al. [2019]. Notably, among
the tree-based methods discussed below, causal forest is the only one that preserves the
simple structure of the original RF: the individual treatment effect is estimated directly
as the average prediction of a single ensemble of decision trees, each of which remains
interpretable on its own.
Other adaptations of tree-based methods for causal inference typically sacrifice this
simplicity. Metalearners [K¨ unzel et al., 2019], for instance, do not estimate the treatment
effect directly with a single forest, but instead combine separate forests fit to the outcomes
under treatment and under control, so that the treatment effect estimate is no longer the
direct output of one interpretable ensemble. Generalized random forest (GRF) [Athey
et al., 2019], used as an alternative implementation of causal forest, instead modifies
the splitting criterion via gradient-based approximations to an estimating equation and
a correspondingly changed prediction mechanism, while additionally incorporating an
orthogonalization step to reduce the influence of confounders. This orthogonalization
step is similar in spirit to DML, reflected in the name “CausalForestDML” used for its
implementation in the popular package EconML [Battocchi et al., 2019]. While effective
at reducing confounding bias, this two-step procedure again departs from the direct,
single-ensemble structure that makes RF interpretable in the first place. A method
to improve feature importance for treatment effect heterogeneity in GRF was recently
developed by B´ enard and Josse [2025], but requires additional post-hoc steps which are
computationally costly, and, more importantly, does not address our goal of interpreting
the fitted tree structure itself. Further adaptations include orthogonal random forest
3

Sample 1 2 3 4 5 6
TreatmentT 0 1 0 1 0 1
Treated outcomeY T=1 0.50.50.51.51.51.5
Control outcomeY T=0 0.50.50.51.51.51.5
FeatureX 1 0 0 0 1 1 1
FeatureX 2 0 0 0 0 1 1
Table 1: Example for data in a potential outcomes model, with binary treatment T ,
potential outcomes Y T=1 and Y T=0 , and two binary features X1, X2. Note that
for each sample only the outcomes corresponding to the treatment assignment
can be observed (shown in bold). The outcomes in italics are unobserved and
cannot be used for estimating the treatment effect.
[Oprescu et al., 2019]; see Jiang et al. [2021] for an overview and comparison of these
methods.
Causal forest is therefore the only method that retains the interpretable, single-ensemble
structure of RF for individual treatment effect estimation. However, as noted above, it
does not explicitly account for confounders during split selection, so splits driven purely
by confounding cannot be distinguished from splits that reflect genuine treatment effect
heterogeneity, undermining the very interpretability its tree structure would otherwise
offer. In this paper, we propose a modification of RF for causal inference, denoted as
IntCF (interpretable causal forest), that follows the general idea of causal forest but
uses a different splitting criterion, one that explicitly accounts for confounders at the
split selection step. This direct inclusion of both heterogeneity and confounder detection
in the tree structure opens the possibility for improved interpretation, especially for
distinguishing features based on how they affect the treatment effect prediction, while
preserving the simple, single-ensemble structure that makes RF interpretable.
1.2. Confounding versus Heterogeneity: an Illustrative Example
In the following, we provide an illustrative example, which demonstrates why the original
splitting criterion of causal forest [Wager and Athey, 2018] fails to result in interpretable
tree structures under confounding, and how our new splitting criterion in IntCF improves
on this. Consider the data in Table 1, with binary treatment T , potential outcomes
Y T=1 and Y T=0 , and two binary features X1, X2. For each sample, only the upright,
bold outcome can be observed; the outcome in italics is unobservable. The treatment
effect Y T=1 −Y T=0 is zero for every sample. However, directly estimating the average
treatment effect from the observed outcomes gives a biased estimate: the difference
between the mean observed treated outcome 0.5+1.5+1.5 3 = 7 6 and the mean observed
control outcome 0.5+0.5+1.5 3 = 5 6 is 1 3 ̸= 0, because of the higher prevalence of treatment
among samples with higher potential outcomes.
Splitting the data into two subsets based on feature X1 would eliminate this bias,
leading to conditional average treatment effect estimates of 0 in both subsets. However,
4

X1 ≤ 0.5
Split criterion: max(dHet, dBias)
Heterogeneity criterion: dHet = 0
Bias criterion1: dBias = 1 9
samples: 1, 2, 3, 4, 5, 6
estimate ˆτ = 1 3
samples: 1, 2, 3
estimate ˆτ= 0
samples: 4, 5, 6
estimate ˆτ= 0
IntCF
X2 ≤ 0.5
Split criterion: dHet = 1 18
no separate criteria
for heterogeneity
and bias
samples: 1, 2, 3, 4, 5, 6
estimate ˆτ = 1 3
samples: 1, 2, 3, 4
estimate ˆτ= 1 2
samples: 5, 6
estimate ˆτ= 0
Causal forest
Figure 1: Decision stumps after the first split for the data in Table 1, using the combined
splitting criterion of our proposed method, IntCF (left), and the criterion of the
original causal forest algorithm [Wager and Athey, 2018] (right). ˆτdenotes the
estimated treatment effect in each node, computed as the difference between the
mean observed outcome under treatment and under control. IntCF selects the
split on X1, correctly identifying it as bias correction rather than heterogeneity,
and yields unbiased estimates in both child nodes; causal forest instead selects
the split on X2, which appears to indicate heterogeneity but remains biased
due to the unaddressed confounding fromX 1.
the splitting criterion used in causal forest [Wager and Athey, 2018], which is based on
heterogeneity in outcomes, will not select this split, as the estimated outcome is the same
on both sides. Even worse, the split on feature X2, which results in an estimate of 1 2
for the treatment effect of samples 1–4, an apparent effect that is itself an artifact of
confounding rather than true heterogeneity, would seem preferable.
This is in contrast to the modification we propose in IntCF below. There, we explicitly
combine two different splitting criteria, one for heterogeneity in the treatment effect and
one for bias correction. With this approach, the change in predicted average treatment
effect from splitting on X1 is recognized as bias correction rather than heterogeneity, so
the split is still used when building the tree. Interpretability is preserved, since the split
is explicitly labeled as reducing bias rather than as improving the estimated treatment
effect heterogeneity.
Applying IntCF to this example yields the decision stump shown in Figure 1 (left) after
the first split. While IntCF estimates the correct treatment effect in this example, causal
forest produces a biased estimate, as the confounding introduced by feature X1 is not
removed (Figure 1, right). Our combined splitting criterion in IntCF correctly indicates
that the selected split corrects bias rather than reflecting treatment effect heterogeneity.
1Note that our bias criterion is an estimate for the squared bias.
5

1.3. Outline of Paper
The remainder of this paper is organized as follows. In Section 2, we introduce the
considered setting, notation, and data model. In Section 3, we introduce the IntCF
algorithm, with a particular focus on our new splitting criteria, as well as an additional
step for honest predictions and validation of splits. In Section 4, we derive theoretical
properties of our new splitting criteria under a change point model. In Section 5,
an extensive simulation study, including a semi-synthetic benchmark as well as a real
data example, demonstrates that IntCF achieves competitive prediction accuracy while
substantially improving interpretability. Finally, in Section 6, we discuss our results and
outline open questions.
2. Preliminaries
2.1. Data and Potential Outcomes Model
We consider a potential outcomes framework [Rubin, 1974], in which the data generating
process is described by the joint distribution of
(T, X, YT=0 , YT=1 ),
with binary treatment T∈ {0, 1}, a feature vector X∈R d, and potential outcomes
Y T=0 and Y T=1 . For each unit, only the potential outcome corresponding to the realized
treatment is observed, i.e., we observe Y∼Y T , while the other potential outcome
remains unobserved. We aim to predict theconditional average treatment effect (CATE)
τ(x) :=E

Y T=1 −Y T=0 |X=x  ,(1)
for a given feature vectorx ∈R d; throughout this paper, we refer to τ (x) as the individual
treatment effect, since it is the treatment effect estimate available given the observed
covariatesx. Beyond predicting τ (x), we are interested in interpreting treatment effect
heterogeneity, i.e., in identifying which of the d features actually influence τ (x). We
observeNindependent and identically distributed copies of (T,X, Y),
(ti,x i = (xi,j)d j=1, yi), i= 1, . . . , N.
The main difficulty in estimating τ (x) is that, for each observation i, only one of yT=1 i
andy T=0 i is observed; the individual treatment effect
τi :=y T=1 i −y T=0 i
can therefore never be observed, so standard machine learning methods for regression,
which require direct observations of the target variable, cannot be applied to estimate τ
directly.
We further define
p(x) :=P(T= 1|X=x) (2)
6

for thetreatment propensity, and
µ(x) := 1 2 E  Y T=0 +Y T=1 |X=x  (3)
for themain outcome.
2.2. Decision Trees and RFs
Decision trees for classification and regression tasks were proposed by Breiman et al.
[1984] and later extended to RFs [Breiman, 2001]. RFs use a collection of decision trees,
whose predictions are combined (for regression, usually by taking the average) to obtain
an ensemble prediction. Each tree divides the feature space into subsets by performing
binary splits based on a threshold applied to one of the features at each inner node. For
deciding which split to use, a splitting criterion is applied, most commonly the impurity
decrease according to an impurity measure, for example mean squared error (MSE) for
regression.
Specifically, when selecting a split for a node eparent, which contains samples with
indices in Jparent, a collection of potential splits is considered; this might be all possible
splits or a subset of these. Each potential split creates two child nodes, eL and eR,
containing samples with indices JL and JR, respectively, such that Jparent = JL ⊔J R
is a disjoint union. We denote the number of samples in the left and right child nodes
by nL = |JL| and nR = |JR|, respectively. In a regression setting, each training sample
has an attached response value yi. For each of these three nodes, a prediction and an
impurity value are computed; comparing these then yields the impurity decrease for the
candidate split. Finally, the potential split with the highest impurity decrease is selected
as the actual split, and the procedure is repeated recursively at the two child nodes until
a stopping criterion is reached.
3. Interpretable Causal Tree and Forest Algorithm
3.1. Correcting Heterogeneity Splitting Rule for Confounding
As outlined in Section 2.2, a central element for the construction of decision trees from
training data is the splitting rule. In this section, we will derive a new splitting rule,
which can be applied to data from a potential outcomes model in a causal inference
setting. Recall that the main difficulty compared to a regression setting is that for each
observation i, only one of yT=1 i and yT=0 i is observed; the individual treatment effect
τi = yT=1 i −y T=0 i can never be observed directly, hence, standard splitting rules as used
for decision trees in regression, cannot be applied directly. Previous work has therefore
considered different splitting criteria which overcome this problem [see, e.g., Athey and
Imbens, 2016, Wager and Athey, 2018, Athey et al., 2019].
To motivate our new splitting criteria, as well as previously considered splitting criteria
for causal forest [Wager and Athey, 2018], we start with a recap of the impurity decrease via
MSE in the regression setting, the standard split statistic of RF implementations. There,
7

the splitting criterion is obtained by maximizing among possible splits Jparent = JL ⊔J R
the decrease in MSE, that is,
∆RF(L, R) := 1 N X i∈Jparent (ˆyparent −y i)2 − 1 N

 X
i∈JL
(ˆyL −y i)2 + X
i∈JR
(ˆyR −y i)2

 (4)
with node predictions obtained as averages, that is, ˆyparent := 1 nL+nR P i∈Jparent yi and similar
ˆyL := 1 nL X i∈JL yi and ˆy R := 1 nR X i∈JR yi.(5)
Note that for such averages we have
ˆyparent = nL ·ˆyL +n R ·ˆyR nL +n R .(6)
Using (5), it is easy to see that (4) is equal to
1
N

nL(ˆyparent −ˆyL)2 +n R(ˆyparent −ˆyR)2 .(7)
Moreover, using (6), it is easy to see that (7) is equal to
nL ·n R
N(n L +n R) (ˆyL −ˆyR)2 .(8)
Note that (8) equals, up to a factor of nL+nR N (which is constant within each node), the
variance among the predictions at the two child nodes.
For the causal inference setting with outcome of interest being the (unobserved)
treatment effectτ i, the direct analog to the splitting criterion from (4) is to consider
1
N
X
i∈Jparent
(ˆτparent −τ i)2 − 1 N

 X
i∈JL
(ˆτL −τ i)2 + X
i∈JR
(ˆτR −τ i)2

 .(9)
For the node predictions ˆτparent,ˆτL and ˆτR one can obtain natural estimates with the
difference-in-means estimatorat a specific nodee, that is,
ˆτe := 1 |{i∈J e :t i = 1}| X i∈Je
ti=1
yi − 1 |{i∈J e :t i = 0}| X i∈Je
ti=0
yi,(10)
e.g., for the parent node e = parent, for the left child node e = L, or for right child node
e=R.
The problem with the decrease in MSE as in (9) is, however, that the individual
treatment effects τi are not observed and hence, one cannot use (9) for a splitting criterion.
Therefore, the proposal of Wager and Athey [2018] for causal forest was to consider the
analog of (8) instead. That means, they propose to select splits Jparent = JL ⊔J R such
8

that the variance among the predicted treatment effects at the child nodes is maximized,
i.e., they maximize at each node
∆CF(L, R) :=dHet := nL ·n R
N(n L +n R) (ˆτL −ˆτR)2.(11)
We will call this theheterogeneity criterion. The major problem with using the het-
erogeneity criterion (11) as a replacement for the decrease in MSE in (9), is that the
corresponding analog equations to (5) and (6), which were needed to derive the equiva-
lence between (4) and (8) in the regression setting, do not hold in the causal inference
setting. More precisely, the analog to (5) is given by the condition
ˆτL = 1 nL X i∈JL τi and ˆτ R = 1 nR X i∈JR τi (12)
and the analog to (6) is given by the condition
ˆτparent = nLˆτL +n R ˆτR nL +n R .(13)
In contrast to the regression setting, (12) and (13) are not guaranteed to hold in the
causal inference setting. However, if these conditions do hold, one can derive equivalence
between (11) and (9), as the following two lemmas show.
Lemma 1.If (12) holds, then thedecrease in MSE (9) equals themean squared change
in prediction
1
N

nL(ˆτparent −ˆτL)2 +n R(ˆτparent −ˆτR)2 .(14)
The proof is given in the appendix. Note that (14) is the analog to (7) from the
regression setting.
Lemma 2.If (13) holds, then the mean squared change in prediction (14) equals the
heterogeneity criterion dHetin(11).
The proof is given in the appendix.
Both (12) and (13) may fail to hold under confounding, and either violation breaks
the equivalence between the heterogeneity criterion dHet in (11) and the decrease in MSE
in (9). However, the two assumptions differ fundamentally in nature. A violation of (13)
is a property of the candidate split itself: for any given split, ˆτparent, ˆτL, and ˆτR can
be computed directly from the observed data, and one can check whether the parent
estimate coincides with the sample-size-weighted average of the child estimates. Note
that even in a randomized controlled trial, i.e., in the absence of any confounding, (12)
and (13) will typically not hold exactly, simply due to finite-sample noise. However,
without confounding both conditions hold in expectation. Under confounding, in contrast,
they need not hold even in expectation. A strong violation of (13), beyond what would
be expected from sampling noise alone, therefore indicates a systematic effect rather
than a chance fluctuation and, as illustrated in our example above, arises precisely when
9

treatment propensity differs between the two child nodes, i.e., it is a direct symptom of
confounding along the considered split. This makes it possible to explicitly measure and
correct for such violations as part of the splitting criterion.
In contrast, (12) is not a property of any particular split, but a standing identification
assumption: it requires that, conditional on already being in a given node, the difference-
in-means estimator (10) is unbiased for the true average treatment effect within that
node, i.e., that no unobserved confounding remains once conditioned on the node. This
within-node unconfoundedness assumption underlies the use of the difference-in-means
estimator at any node regardless of the tree structure, and is required by essentially
every tree-based method for treatment effect estimation, including our own leaf-level
estimates. Since it is not tied to any single candidate split, it cannot be assessed or
corrected by comparing ˆτparent, ˆτL, and ˆτR at a given step, but only by conditioning on
the relevant confounders while growing the tree as a whole. We therefore focus our new
splitting criterion on correcting for violations of (13), while retaining (12) as a standing
assumption, consistent with its role throughout the tree-based causal inference literature.
As Lemma 2 shows, whenever the mean squared change in prediction (14) and the
heterogeneity criterion dHet in (11) are not equal, this can be directly attributed to
a violation of (13) and hence, a bias correction. We therefore treat the difference
between (14) and (11) as one component of our splitting criterion, quantifying the extent
to which a split corrects for confounding, as opposed to detecting heterogeneity in the
treatment effect. The following Lemma gives an explicit expression how this difference
corresponds to the violation of (13).
Lemma 3.The difference of(14)and(11)is given by
dBias := nL +n R
N

ˆτparent − nLˆτL +n R ˆτR nL +n R
2
.(15)
We call (15) thebias criterion. The proof is given in the appendix.
In total, we have shown the following decomposition
MSE decrease≈ 1 N  nL(ˆτparent −ˆτL)2 +n R(ˆτparent −ˆτR)2 = dHet + dBias.(16)
Note that the decomposition in (16) is analog to a classical bias-variance decomposition.
The two criteria, dHet and dBias, capture different reasons for improved predictions:
identified heterogeneity (which we measure by the variance of predictions) and bias
correction (which we estimate by the square of change of average prediction).
To improve interpretability of the final trees, we want to separate these two reasons.
Therefore, at each node, we select the split that has the strongest effect from either of
these two sources. As both the heterogeneity criterion dHet in (11) and the bias criterion
dBias in (15) are directly derived from the mean squared change (14), their values are
comparable. Hence, with IntCF we propose touse the maximum of both criteria to select
the split. That is, our splitting criterion for IntCF is obtained by maximizing among
possible splits Jparent = JL ⊔J R the maximum of heterogeneity and bias improvement,
10

that is,
∆IntCF(L, R) := max  dHet, dBias  .(17)
For our theoretical analysis, we also consider signed versions of these criteria, which
we refer to as signed splitting criteria, defined by
dHet ± := √nL ·n R
nL +n R
(ˆτL −ˆτR),(18)
thesigned heterogeneity, and
dBias ± := ˆτparent − nLˆτL +n R ˆτR nL +n R ,(19)
thesigned bias. By squaring and then multiplying by nL+nR N (a constant factor at each
node), one recovers the heterogeneity criterion dHet from the signed heterogeneity dHet ± ,
and the bias criterion dBias from the signed bias dBias ± .
3.2. Honest Validation of Splits
In this section, we introduce a second modification to standard RF that we propose
for IntCF, complementing the new splitting criterion (17) introduced in Section 3.1.
Importantly, this modification does not affect how the trees themselves are grown: trees
are constructed exactly as before, simply using the combined splitting criterion (17) in
place of the standard impurity decrease. Instead, this modification concerns how we later
summarize, at each node, the heterogeneity and bias contribution identified during tree
construction, for example when computing a mean-decrease-in-impurity-type measure of
feature importance.
While building the tree, especially for nodes close to the root, the criteria used to
select splits might not yet be informative: as discussed in Section 3.1, the within-node
unconfoundedness assumption (12) need not hold until the tree has conditioned on the
relevant confounders, so for nodes near the root the estimates entering the heterogeneity
criterion dHet (11) and the bias criterion dBias (15) may still be affected by confounding
that is only corrected at later splits.
To address this problem, we use out-of-bag (or hold-out) samples to summarize the
heterogeneity and bias contribution of each split. This overall idea is not new and has been
used in various forms before, both for prediction, where it is known ashonest prediction,
and for feature importance, e.g., in debiased or out-of-bag variants of MDI [Li et al., 2019,
Zhou and Hooker, 2021]. We build on both of these ideas. First, we also use out-of-bag or
hold-out samples for our final predictions; this is simply the standard honest-prediction
procedure of double-sample trees, as used in causal forest [Wager and Athey, 2018], and
not itself a new contribution. Second, and in addition, we use these samples as validation
set to re-evaluate the split statistics at every node, similar to out-of-bag MDI approaches
for RF. However, simply recomputing the heterogeneity criterion dHet (11) and the bias
criterion dBias (15) on out-of-bag samples, using the same difference-in-means estimator
11

at each node, is not sufficient in the causal inference setting: while using held-out data
addresses the classical overfitting bias that motivates honest estimation and out-of-bag
MDI, it does not address confounding. In particular, the within-node unconfoundedness
assumption (12) need not hold until the tree has conditioned on the relevant confounders,
regardless of whether the underlying estimate is computed on training or on out-of-bag
data. We therefore develop a modified validation procedure in the remainder of this
section, which draws on the fully grown tree (or forest) to correct for this remaining
confounding.
To use the validation set to also validate split attribution at all nodes, we extend the
double-sample-trees procedure to compute predictions from this data set not only at
leaf nodes, but also at inner nodes. To obtain both an estimate of corrected bias and
of identified heterogeneity, we compute two separate estimates for each node, using the
following procedure.
For the first estimate, we feed the validation samples through the considered tree and,
at each node, compute an estimate as before using the difference-in-means estimator (10),
but now based on validation samples instead of training samples. Denote the indices of
validation samples in node e by Ie; throughout this section, ne, nL, nR, and N refer to
the corresponding counts of validation samples, analogous to their earlier use for training
samples in Section 3.1. At nodee, we call this estimate
ˆτf e = 1 |{i∈I e :t i = 1}| X i∈Ie
ti=1
yi − 1 |{i∈I e :t i = 0}| X i∈Ie
ti=0
yi (20)
theforward prediction. It might still be influenced by bias that is only corrected at later
splits. As with double-sample trees, at leaf nodes these estimates are used as predictions
for samples falling in the respective leaf.
For the second estimate, we use the final predictions ˆτval i for the validation samples
(these can be either the predictions from the single tree or from an entire RF). At each
node e, a new estimate ˆτb e for the CATE can then be computed by averaging the final
predictions of validation samples contained in this node, i.e.,
ˆτb e = 1 |Ie| X i∈Ie ˆτval i .(21)
For inner nodes, this estimate can also be computed as ˆτb parent = nL ˆτb L+nR ˆτb R nL+nR . Since these estimates can therefore be computed iteratively from the leaves up to the root, we call
thembackward predictions. If the final predictions are unbiased, so are the backward
predictions.
One task in validating split attribution is to estimate the heterogeneity between
treatment effects in the child nodes at each split. For this, we use a formula analogous to
the heterogeneity splitting criterion (11), but now using the backward predictions, i.e.,
dHet v := nL ·n R
N(n L +n R)

ˆτb L −ˆτb R
2
.(22)
12

We refer to (22) as theheterogeneity validation criterion.
For the bias, such a direct transfer is not possible: unlike the heterogeneity criterion,
the backward predictions already incorporate bias corrections made throughout the tree,
not only the correction attributable to the split under consideration. Instead, we can
estimate the squared bias corrected by the remainder of the tree by comparing forward
and backward estimates, using nL+nR N  ˆτf parent −ˆτb parent 2. But this also includes bias that
was only corrected in descendant nodes. For that reason, we instead use the decrease in
squared bias,
dBias v := nL +n R
N

ˆτf parent −ˆτb parent
2
− nL
N

ˆτf L −ˆτb L
2
− nR
N

ˆτf R −ˆτb R
2
,(23)
which we refer to as thebias validation criterion.
In each node, one can show that sum of the heterogeneity validation criterion and the
bias validation criterion equals the decrease in mean squared error obtained by replacing
the forward estimate of the average treatment effect with the final individual predictions,
as the following lemma shows.
Lemma 4.For the validation criteria(22)and(23)we have
dHet v + dBias v = 1 N

 X
i∈Iparent

ˆτf parent −ˆτval i
2
−
X
i∈IL

ˆτf L −ˆτval i
2
−
X
i∈IR

ˆτf R −ˆτval i
2

 .
The proof is given in the appendix. Again, note that the decomposition in Lemma 4 is
analog to a classical bias-variance decomposition, similar to (16) for the splitting criteria.
3.3. Summary of Algorithm
We now combine the two modifications introduced above—the amended splitting criterion
∆IntCF (17) from Section 3.1 and the honest validation procedure from Section 3.2—into
a complete algorithm for growing decision trees and RFs. Analogous to how a RF is
built from individual decision trees (Section 2.2), we first describe how to grow a single
tree, which we call theinterpretable causal tree (IntCT); the corresponding forest,IntCF,
is then obtained by combining many such trees, as described below.
3.3.1. Interpretable Causal Tree (IntCT)
1. Split the samples into a training setJand a validation setI.
2. Build the tree based on the training samplesJ:
a) At the current node, consider all possible splits, determine the resulting sample
sets for the two child nodes, and compute the treatment-effect estimates ˆτL,ˆτR
for these child nodes using the difference-in-means estimator (10).
b) For each possible split, compute the heterogeneity criterion dHet (11) and the
bias criterion dBias (15).
13

c) Select the split that maximizes ∆ IntCF = max  dHet, dBias  (17), i.e., the split
with the largest value of either criterion.
d) Create the new child nodes and assign them their respective training samples.
e) If no stopping criterion (e.g., maximum depth or minimum leaf size) has been
reached, repeat the above steps at each child node.
3. Validate the splits and compute predictions using the validation samples (see
Section 3.2); this step retraces the tree built in Step 2, but now operates on I
instead ofJ:
a) Compute the forward predictions ˆτf e (20) for all nodes of the tree.
b) At the leaves, use the forward prediction as the tree’s prediction for samples
that fall into the respective leaf; this is the standard “honest prediction”
procedure, as proposed, e.g., in [Wager and Athey, 2018].
c) Use the tree (or the forest) to compute estimated treatment effects ˆτval i for all
validation samples.
d) Use these estimated treatment effects to compute the backward predictions
ˆτb e according to (21) for all nodes of the tree.
e) Compute the heterogeneity validation criterion dHet v (22) and the bias vali-
dation criterion dBias v (23) from the forward and backward predictions, and
store their values at each node.
4. The final result is the tree together with its leaf-level predictions and the validation
criterion values dHet v , dBias v stored at each split.
3.3.2. Interpretable Causal Forest (IntCF)
In a forest, the same algorithm is used to grow each tree, with the training/validation
split of Step 1 performed independently for each tree, so that every sample is used, either
in the training or in the validation role, in every tree of the forest. This plays a role
analogous to the bootstrap sampling used in standard RFs, where the samples not drawn
in the bootstrap, the out-of-bag samples, serve as the validation set. As with standard
RFs, only a random subset of features is considered at each split when growing each tree.
3.3.3. Feature Importance
Following the original mean-decrease-in-impurity approach to feature importance [Breiman
et al., 1984], we sum, over all nodes that split on a given feature, a measure of that split’s
contribution to obtain the feature’s importance. Instead of the impurity decrease, we
use a validation criterion for this purpose: by default, only the heterogeneity validation
criterion dHet v (22) is used, but the bias validation criterion dBias v (23), or the sum of
both, can also be used if desired.
In many implementations, for example scikit-learn [Pedregosa et al., 2011], it is
customary to scale the importance measure so that it sums to 1. In contrast to this
14

standard MDI procedure, the bias validation criterion can take negative values, so feature
importance scores that include it may also be negative. We therefore scale our feature
importance scores so that the sum of the non-negative scores is 1.
4. Population-level Analysis of the Splitting Criteria under a
Change Point Model
In this section, we provide theoretical support for the central claim of this paper: that
the combined splitting criterion introduced in Section 3.1 correctly distinguishes splits
driven by confounding-induced bias from splits that reflect genuine heterogeneity in the
treatment effect. Rather than finite-sample guarantees, we study this question at the
population level, i.e., in the limit as the sample size N→ ∞, under a stylizedchange
point modelin which the treatment effect, the propensity, and the main outcome are step
functions of a single covariate.
The remainder of this section is organized as follows. Section 4.1 derives the population
limits of the signed heterogeneity criterion dHet ± and the signed bias criterion dBias ± .
Section 4.2 explains why, due to the marginalization inherent to decision-tree splits, it
suffices to study a univariate change point model, which we introduce formally. Section 4.3
then shows that any such change point model decomposes into a component with a
constant treatment effect and a component for which the difference-in-means estimator is
unbiased. Finally, Section 4.4 shows that our two splitting criteria correctly recover this
decomposition: the population bias criterion attains an extremum at the true change
point exactly when bias is present, and the population heterogeneity criterion attains
an extremum there exactly when the treatment effect is genuinely heterogeneous. This
provides theoretical justification for the algorithm’s ability to separate these two sources
of improvement, which underlies its interpretability.
4.1. Population-level Analysis
Rather than deriving finite-sample results, we focus on the corresponding population
analogs of (18) and (19) in order to elucidate general structural properties of these
splitting criteria. To this end, consider a decision tree with an inner node e and the
associated hyper-rectangle R(e). At node e, we examine a candidate split along a given
variable, say x1, at threshold k. Throughout the analysis, we impose the following
simplifying assumptions:
A1 The feature vector X is uniformly distributed on the unit hypercube, that is,
X∼U([0,1] d).
A2 The outcomesY T=1 , YT=0 are bounded.
A3 The positivity assumption holds, meaning that there exists some ϵ >0 such that,
for allx∈[0,1] d,
ϵ≤P(T= 1|X=x)≤1−ϵ.
15

A4 The hyper-rectangle R(e), with positive volume µ(R(e)) > 0, the choice of the split-
ting variable (without loss of generality assumed to be x1), as well as the considered
threshold k are independent of the training data D = {(y1, x1, t1), . . . ,(yN , xN , tN )}.
Note that, since decision trees are invariant under monotone transformations of the
covariates, the first assumption is essentially equivalent to assuming independence among
the different features. Assumptions A1 and A2 are standard in the analysis of decision-
tree-based methods [see, for example, Behr et al., 2022, Wager and Athey, 2018]. As-
sumption A3 is a requirement for causal inference in general [compare, for example,
Rosenbaum and Rubin, 1983]. The final assumption is clearly violated for our intCT
algorithm, since all split points in the tree are selected in a data-dependent manner,
implying that the resulting hyper-rectangle R(e) likewise depends on the training data
D. Nevertheless, extending the subsequent results to this setting appears to be relatively
straightforward and mainly of a technical nature; see Remark 1 for details.
Under Assumptions A1–A4, it follows directly from the law of large numbers and
the continuous mapping theorem that, when the training data D are generated i.i.d.
according to the data-generating process P (Y T=0 , YT=1 , X, T), for any fixed threshold k
dHet ± p →Het ±(k), dBias ± p →Bias ±(k),asN→ ∞.(24)
The corresponding population quantities are given by
Het±(k) := p k(1−k)·  ¯Y T=1 L − ¯Y T=0 L  −  ¯Y T=1 R − ¯Y T=0 R  ,(25)
and
Bias±(k) :=  ¯Y T=1 − ¯Y T=0  −k·  ¯Y T=1 L − ¯Y T=0 L  −(1−k)·  ¯Y T=1 R − ¯Y T=0 R  (26)
where, fora∈ {0,1},
¯Y T=a :=E  Y T=a |X∈R(e), T=a  ,
¯Y T=a L :=E  Y T=a |X 1 ≤k, X∈R(e), T=a  ,
¯Y T=a R :=E  Y T=a |X 1 > k, X∈R(e), T=a 
are expectations of observed outcomes in the whole node as well as to left and right of the
considered split, respectively. In the following, we study the properties of the population
counterparts Het±(k) and Bias ±(k) associated with our proposed splitting criteria.
Remark 1.To dispense with Assumption 4, it would suffice to establish the convergence
result in (24) uniformly over all hyper-rectangles R(e)with a fixed minimal volume. More
precisely, one would require a result of the form that, for anyϵ >0,
P
"
sup
R,k,j∈{1,...,d}, µ(R)>δ

dHet ± −Het ±(k)

 > ϵ
#
→0asN→ ∞,
and an analogous statement for the bias term. The assumption of a minimal volume can be
enforced in practice by imposing a maximal tree depth and by requiring splitting thresholds
16

k to be bounded away from zero and one; both restrictions are standard in the analysis
of RFs [see, e.g., Scornet and Hooker, 2026]. Establishing such uniform convergence
results should be feasible using standard tools from empirical process theory, including
uniform convergence arguments and concentration inequalities [see, e.g., Behr et al.,
2022]. Since this extension is largely technical and does not affect the qualitative insights
of our analysis, we do not pursue it further here and instead focus on the population
quantitiesHet ±(k)andBias ±(k)in(25)and(26)directly.
4.2. Marginalization Effects
By construction, when a decision tree considers a split along a given variable Xj, say X1,
the influence of the remaining variables X2, . . . , Xd is marginalized out through averaging,
as reflected in the conditional expectations in (25) and (26). Consequently, once a specific
variable X1 is selected, decision trees can capture only the marginal effect of this variable.
This is an intrinsic property of decision trees and gives rise to well-known limitations of
such methods.
This marginalization is visible directly in the population criteria themselves: Het±(k)
and Bias±(k) in (25) and (26) depend on the joint distribution of (X, T, YT=0 , YT=1 ) only
through X1 and the conditioning eventX ∈R (t), which is fixed across both candidate
children. It therefore suffices, for the purpose of studying the behavior of a single
candidate split, to consider a data-generating process in which only one covariate, say x1,
carries any signal. Here, we study a univariatechange point modelfor CATE, propensity,
and main outcome, in analogy to the general definitions ofτ, p, µin (1), (2) and (3):
τ(x 1) :=β 0 +β 11x1≤γ,
p(x1) :=q 0 +q 11x1≤γ,
µ(x1) :=α 0 +α 11x1≤γ.
(27)
Each coefficient governs a distinct aspect of the model. The slope β1 governs treatment
effect heterogeneity: β1 = 0 corresponds to a constant treatment effect τ (x1) = β0, i.e.,
a model without treatment effect heterogeneity. Analogously, q1 governs the degree of
confounding through x1: q1 = 0 corresponds to a constant propensity p(x1) = q0, i.e.,
a setting in which treatment assignment does not depend on x1, as in a randomized
trial. Finally, α1 governs whether x1 has a direct, prognostic effect on the main outcome:
α1 = 0 corresponds to a constant main outcome µ(x1) = α0. Intuitively, confounding bias
for the difference-in-means estimator arises when x1 affects both treatment assignment
(q1 ̸= 0) and the potential outcomes; Theorem 5 below makes this precise.
By construction, this model has a unique natural split point at γ: splitting exactly
there separates τ , p, and µ into constant pieces on either side, which is what allows the
resulting heterogeneity and bias to be exactly quantified.
With µ and τ specified by the change point model above—now understood as depending
onxonly through its first coordinatex 1—the potential outcomes are defined as
Y T=0 (x) =µ(x)− 1 2 τ(x) +ε 0 andY T=1 (x) =µ(x) + 1 2 τ(x) +ε 1 (28)
17

with mean-zero noise terms ε0, ε1 that are assumed to be independent of one another
and ofX.
4.3. Bias–Heterogeneity Decomposition of the Change Point Model
In the following, we provide theoretical insight into why the population splitting criteria
Het±(k) and Bias±(k) in (25) and (26) are able to distinguish between heterogeneity
in the treatment effect and bias induced by confounding. To this end, we first observe
that any change point model of the form (27) can be decomposed into the sum of
two components: one corresponding to a model with a constant treatment effect, and
another for which the difference-in-means estimator is unbiased. This decomposition is
formalized in the following lemma. More precisely, consider a potential outcome model
(Y T=0 , YT=1 , X, T) with treatment effect τ (x), main outcome µ(x), and propensity p(x)
as defined in Section 2.1. We say that thedifference-in-means estimator is unbiasedif
E[τ(X)] =E

Y T=1 |T= 1  −E  Y T=0 |T= 0  ,(29)
or, equivalently (recall Equation 28), if
E[τ(X)] =E

µ(X) + 1 2 τ(X)|T= 1  −E  µ(X)− 1 2 τ(X)|T= 0  .
Theorem 5.Consider a potential outcome model( Y T=0 , YT=1 , X, T)with a single
uniformly distributed covariate X∼U ([a, b]), a < b∈R, potential outcomes as in (28),
and main outcome, treatment effect, and propensity following a change point model as
in(27), i.e.,
µ(x) =α 0 +α 1 ·1 x≤γ, τ(x) =β 0 +β 1 ·1 x≤γ, p(x) =q 0 +q 1 ·1 x≤γ.
Assume that Assumption A3 holds. Thenµ(x)andτ(x)can be decomposed as
µ(x) =µ B(x) +µ H (x)andτ(x) =τ B(x) +τ H (x),
such that, for suitable constantsα ′ 0, α′ 1, α′′ 0, α′′ 1, β′ 0, β′′ 0 , β′′ 1 , the following holds:
1.(Change point model with constant treatment effect)
µB(x) =α ′ 0 +α ′ 1 ·1 x≤γ andτ B(x) =β ′ 0.
2.(Change point model with unbiased difference-in-means)
µH (x) =α ′′ 0 +α ′′ 1 ·1 x≤γ andτ H (x) =β ′′ 0 +β ′′ 1 ·1 x≤γ, where
E

τ H (X)  =E  µH (X) + 1 2 τ H (X)|T= 1  −E  µH (X)− 1 2 τ H (X)|T= 0  .(30)
The proof is given in the appendix.
Remark 2.Note that this decomposition is not unique. The condition (30) does not
restrict α′ 0 and α′′ 0 as well as β′ 0 and β′′ 0 , so that α0 and β0 can be freely distributed onto
the respective pair of parameters. If the treatment assignment is randomized, i.e., p(x)
constant in[0 , 1], any parameters will fulfill (30), so the same freedom of choice also
extends toα 1.
18

Figure 2: Illustration of the decomposition of a change point model into a component with
constant treatment effect and a component with unbiased difference-in-means,
as in Theorem 5. The original model was defined by µ(x) = 0 + 2·1x≤0.6, τ(x) =
1 + 3·1 x≤0.6 andp(x) = 0.25 + 0.5·1 x≤0.6.
Intuitively, this decomposition isolates exactly the two reasons a split can improve
the estimated treatment effect (cf. Section 4.2): the bias component ( µB, τB) has, by
construction, a constant treatment effect, so any change in the estimated treatment
effect attributable to this component must be due to bias correction rather than genuine
heterogeneity. Conversely, the heterogeneity component ( µH , τH ) satisfies the unbiased-
ness condition (30) by construction, so any change in its estimated treatment effect
must reflect genuine heterogeneity rather than bias correction. We make this precise in
Section 4.4 below. Figure 2 illustrates such a decomposition as described in Theorem 5.
4.4. Identifying Heterogeneity and Bias with Signed Splitting Criteria
By Theorem 5 and the linearity of expectation, it follows directly that the population
splitting criteria Het±(k) and Bias±(k) in (25) and (26) can be decomposed accordingly.
19

To make this explicit, we first rewrite Het±(k) and Bias±(k) in terms of the treatment
effect functionτ(x) and the main outcome functionµ(x) as follows:
Het±(k) = p k(1−k)· h E  µ(X) + 1 2 τ(X)|X 1 ≤k, X∈R(e), T= 1 
−E

µ(X)− 1 2 τ(X)|X 1 ≤k, X∈R(e), T= 0 
−

E

µ(X) + 1 2 τ(X)|X 1 > k, X∈R(e), T= 1 
−E

µ(X)− 1 2 τ(X)|X 1 > k, X∈R(e), T= 0 i .
(31)
and
Bias±(k) =E  µ(X) + 1 2 τ(X)|X∈R(e), T= 1 
−E

µ(X)− 1 2 τ(X)|X∈R(e), T= 0 
−k·
h
E

µ(X) + 1 2 τ(X)|X 1 ≤k, X∈R(e), T= 1 
−E

µ(X)− 1 2 τ(X)|X 1 ≤k, X∈R(e), T= 0 i
−(1−k)·
h
E

µ(X) + 1 2 τ(X)|X 1 > k, X∈R(e), T= 1 
−E

µ(X)− 1 2 τ(X)|X 1 > k, X∈R(e), T= 0 i .
(32)
Consequently, under the assumptions of Theorem 5, we obtain the decomposition
Het±(k) = Het± B(k) + Het± H (k) and Bias ±(k) = Bias± B(k) + Bias± H (k),(33)
where Het± B(k) is defined analogously to (31), with µ and τ replaced by µB and τ B
as in Theorem 5, and where Het± H (k), Bias± B(k), and Bias± H (k) are defined in complete
analogy. Note that, while there is some freedom in the choice of decomposition in
Theorem 5, any such decomposition results in the same values for Het± B(k), Het± H (k),
Bias± B(k), and Bias± H (k). An illustrative example of this decomposition for both the bias
and heterogeneity splitting criteria is shown in Figure 3.
Theorem 6.Consider a potential outcome model( Y T=0 , YT=1 , X, T)with a single
uniformly distributed covariate X∼U ([a, b]), a < b∈R, potential outcomes as in (28),
and main outcome, treatment effect, and propensity following a change point model as
in(27), i.e.,
µ(x) =α 0 +α 1 ·1 x≤γ, τ(x) =β 0 +β 1 ·1 x≤γ, p(x) =q 0 +q 1 ·1 x≤γ.
Fix a decomposition as in Theorem 5, and define Het± B(k), Het± H (k), Bias± B(k), and
Bias± H (k)as in(33). Then, under Assumption A3, the following statements hold:
1. If the difference-in-means estimate is biased as in(29), i.e.,
E[τ(X)]̸=E

Y T=1 |T= 1  −E  Y T=0 |T= 0  ,
thenBias ± B(k)attains a global extremum atk=γandHet ± B(γ) = 0.
20

Figure 3: The signed heterogeneity and bias criteria, Het±(k) and Bias±(k), together
with their decomposition into Het± B(k) + Het± H (k) and Bias± B(k) + Bias± H (k) as
in (33), for the model shown in Figure 2.
2. If the treatment effect τ (x)is non-constant, then Het± H (k)attains a local extremum
atk=γandBias ± H (γ) = 0.
The proof is given in the appendix.
Remark 3.By the relationship between signed and unsigned splitting criteria, as well as
the details of the proof of Theorem 6, the extrema in Theorem 6 of the signed splitting
criteria correspond to maxima of their unsigned counterparts while zeros are preserved.
As the splitting criteria are non-negative, the zeros correspond to minima of the splitting
criteria.
The interpretation of Theorem 6 is as follows. Theorem 5 shows that, locally at
any fixed node, the potential outcome model marginalized with respect to a given
splitting variable can be decomposed into two distinct components: one component that
captures all heterogeneity in the treatment effect, and another component that captures
21

all bias of the local difference-in-means estimator. This decomposition is intrinsic to
the marginalization mechanism of decision trees and holds at the population level for
each candidate split. As a consequence, a split at a given node may improve the local
estimation of heterogeneous treatment effects for two fundamentally different reasons:
either because it captures genuine heterogeneity in the treatment effect function, or
because it reduces bias in the local average treatment effect induced by confounding.
Standard decision tree–based approaches do not distinguish between these two sources of
improvement, as they rely only on the heterogeneity criterion when selecting splits.
Theorem 6 shows that this separation can be achieved at the population level by
the proposed splitting criteria. More precisely, the heterogeneity component of the
signed heterogeneity criterion, Het± H (k), attains an extremum at the true jump location
γ whenever the treatment effect is non-constant, while the bias component of the signed
bias criterion, Bias± B(k) is maximized at the same location whenever bias is present. The
behavior predicted by Theorem 6 can also be observed empirically in the illustrative
example shown in Figure 3. Thus, the population versions of our splitting criteria Het±(k)
and Bias±(k) in (25) and (26) recover the split positions associated with treatment effect
heterogeneity and bias, respectively, within the appropriate model components, with
the former guaranteed up to a local optimum. Overall, this result provides a theoretical
explanation for the empirical improvements observed for the proposed splitting criteria
in our simulation studies, presented in the next section.
5. Simulations and Application
In this section, we apply IntCF on semi-synthetic and synthetic data sets, which allow
for evaluation of prediction accuracy by having known ground-truth causal effects, as
well as on a real data example. For synthetic data sets we are further able to compare
importance measures to the relation of features to outcomes defined by the data model.
Throughout, we pay particular attention to the trade-off between prediction accuracy,
model simplicity, and interpretability, since this trade-off is the central motivation for
our approach.
5.1. Prediction Accuracy on Real-data Benchmarks
First, we compare prediction accuracy of our method with other established tree-based
treatment effect estimation methods on four established data sets using the framework of
Balazadeh et al. [2025]. As tree-based competitors we consider generalized random forests
(GRF) [Athey et al., 2019], CausalForestDML as implemented in the EconML package
[Battocchi et al., 2019], and causal forest [Wager and Athey, 2018]. These models were
employed to gain predictions for average treatment effect (ATE) and CATE on four data
sets with ground-truth causal effects: IHDP [Ramey et al., 1992, Hill, 2011], ACIC 2016
[Dorie et al., 2019], Lalonde CPS and PSID cohorts [LaLonde, 1986] with causal effects
from RealCause [Neal et al., 2021]. The predictions were evaluated against ground-truth
ATE and CATE using relative ATE error and precision in estimation of heterogeneous
treatment effects (PEHE) [see Balazadeh et al., 2025].
22

Method Mean PEHE±Standard Error(↓better) Mean ATE Relative Error±Standard Error(↓better)
IHDP ACIC 2016 LalondeCPSLalondePSID IHDP ACIC 2016 LalondeCPSLalondePSID
(×103) (×10 3)
IntCF 2.99±0.49 1.57±0.109.99±0.06 15.93±0.27 0.21±0.04 0.15±0.040.39±0.02 0.18±0.02
causal forest 3.72±0.61 2.19±0.129.58±0.03 16.02±0.17 0.22±0.04 0.28±0.060.24±0.01 0.09±0.01
GRF3.67±0.61 1.32±0.30 12.33±0.06 22.91±0.17 0.18±0.03 0.07±0.020.82±0.02 0.85±0.02
Forest DML 4.53±0.731.48±0.3112.95±0.04 22.99±0.15 0.08±0.01 0.05±0.01 1.03±0.01 1.05±0.01
Table 2: CATE & ATE results.Columns correspond to benchmark suites: IHDP,
ACIC 2016, LalondeCPS/PSID.(left half )mean PEHE,(right half )mean ATE
relative error. Lalonde PEHE is in thousands. The best andsecond best
entries in each column are highlighted. This table is modified from Balazadeh
et al. [2025], with results for IntCF in the first line, results for causal forest
[Wager and Athey, 2018] in the second line and the results for GRF and Forest
DML of Balazadeh et al. [2025] as comparison in the remaining two lines.
Results are shown in Table 2. Overall, IntCF is mostly comparable with causal forest,
with some improvement on data sets IHDP and ACIC 2016, while causal forest produces
better ATE estimates on the Lalonde data sets. The results for the other two methods
follow a different pattern: they perform better in estimating ATE for data sets IHDP
and ACIC 2016, but their results for PEHE and ATE on the Lalonde data sets are
significantly worse than those of IntCF. Overall, IntCF performs best in two settings, is
second best in three settings, and third out of four in the remaining three settings, so that
we conclude that IntCF is very competitive in terms of prediction accuracy compared to
other established tree-based competitors.
Beyond the tree-based competitors considered here, [Balazadeh et al., 2025] also
benchmark several additional, non-tree-based methods on the same four data sets, using
the identical evaluation setup we adopt here; we refer to Balazadeh et al. [2025] for the full
comparison. Some of these methods, most notably CausalPFN, achieve higher prediction
accuracy than any of the tree-based methods considered in Table 2, including IntCF,
in most settings. However, CausalPFN and related methods are complete black boxes:
unlike tree-based approaches, they offer no direct way to inspect which features drive a
given prediction, or to what extent, and hence cannot answer the type of interpretability
questions that motivate this paper. Tree-based methods therefore occupy a useful middle
ground between prediction accuracy and interpretability. Within this class of methods,
IntCF is particularly attractive: as shown above, it is competitive in prediction accuracy
with the best tree-based alternatives, while, as we show in the remainder of this section,
achieving substantially better interpretability than all of them.
5.2. Interpretation Accuracy on Synthetic Data
While the data sets in Section 5.1 allow for evaluation of prediction accuracy by providing
ground-truth causal effects, they do not lend themselves to evaluation of interpretability
of models, as the mechanisms behind these effects are not known. For this reason, we
generated synthetic data to compare importance measures to the structure of treatment
23

effects as defined by the data model.
Four data models were used to generate the synthetic data sets for this section, each
with a complexity parameter s. This parameter scaled the dimension of the data, so
that features for all models are generated uniformly from [0 , 1]d with d = 5s, and the
parameter also affected the functions µ, τ, pdefining the models. These models were
defined as follows:
1. Interaction model: An adaption of a, so-called, locally-spiky-sparse (LSS) model,
based on [Basu et al., 2018, Behr et al., 2022], with interactions for the treatment
effect, but constant baseline and randomized treatment assignment:
p(X) = 0.5,
µ(X) = 0,
τ(X) =
sX
i=1
1X2i−1≤γ ·1 X2i≤γ,
where γ = 0 .7. The features responsible for treatment effect heterogeneity are
therefore X1, . . . , X2s, appearing in interacting pairs ( X2i−1, X2i); since p and µ do
not depend on X at all, this model contains no confounders. Note that the marginal
effect (see Section 4.2) of any single feature in this LSS model again corresponds to
a change point model, directly connecting this simulation setting to our theoretical
analysis in Section 4.
2. Change point model: An additive change point model with both confounding
features and features responsible for treatment effect heterogeneity:
p(X) = 0.2 + 0.6 s 2sX i=s+1 1Xi≤γ,
µ(X) =
2sX
i=s+1
1Xi≤γ,
τ(X) =
sX
i=1
1Xi≤γ,
this time with γ = 0.5. The features responsible for treatment effect heterogeneity
are therefore X1, . . . , Xs, while Xs+1, . . . , X2s act as pure confounders, affecting
both the propensity and the main outcome but not the treatment effect itself.
3. Linear model: A model with linear functions for propensity, main effect and
24

treatment effect:
p(X) = 0.25 + 0.5 s 2sX i=s+1 Xi,
µ(X) =
2sX
i=s+1
Xi,
τ(X) =
sX
i=1
Xi.
As in the change point model, the features responsible for treatment effect hetero-
geneity areX 1, . . . , Xs, whileX s+1, . . . , X2s act as pure confounders.
4. Mixed model: Combination of linear and LSS model:
p(X) = 0.2 + 0.6 s 3sX i=2s+1 1Xi≤γ,
µ(X) =
3sX
i=2s+1
Xi,
τ(X) =
sX
i=1
1X2i−1≤γ ·1 X2i≤γ + 1 s 2sX i=s+1 Xi,
with γ = 0 .7. The features responsible for treatment effect heterogeneity are
therefore X1, . . . , X2s, with Xs+1, . . . , X2s entering both the interaction and the
linear part ofτ;X 2s+1, . . . , X3s act as pure confounders.
In all four models, any remaining features beyond those listed above, up to the total
dimension d = 5s, are pure noise, unrelated to p, µ, or τ . The ROC-AUC statistic which
we introduced below treats a feature as a positive only if it appears in the formula for
τ ; confounders and noise features are therefore both treated as negatives, even though
confounders do affect p and µ. Data was generated with normal distributed noise terms
where the variance was equal to the variance of treatment effects.
Again, we compare our method IntCF to the three other tree-based causal machine
learning methods, causal forest [Wager and Athey, 2018], GRF [Athey et al., 2019]
and CausalForestDML from EconML [Battocchi et al., 2019]. For the evaluation, both
predictions and feature importance generated by these models were considered. Both
GRF and CausalForestDML use a maximum depth and decay exponent for their feature
importance calculation. We set maximum depth to infinity (or a very high value if
not possible) and decay exponent to zero to ensure that the importance measures are
comparable with those of the other estimation methods. For predictions, the precision in
estimation of heterogeneous treatment effects (PEHE) was calculated and normalized
by dividing it by the PEHE of a dummy predictor, which predicts a constant treatment
effect by the difference-in-means from the training samples. For the feature importance,
25

Figure 4: Comparison of precision in estimation of heterogeneous effects (PEHE) of IntCF
(blue), Forest DML (yellow), causal forest (green) and GRF (red), normalized
to PEHE of a constant difference-in-means estimator. For each method, a band
of one standard error is around the respective mean. In this figure, lower values
are better. Top left shows interaction model, top right change point model,
bottom left linear model, and bottom right mixed model.
we considered a ROC-AUC statistic which measures how good the feature importance
can distinguish between features which actually appear in the respective formula for
treatment effectτand those which do not.
Each of the models with parameter s from 1 to 10 were used for simulations. For
each model and parameter, 500 ·s training samples and 100 000 separate evaluation
samples were generated. The training samples were then used to train the machine
learning models, which were subsequently evaluated on the evaluation samples. For each
combination of data model, parameter s, and machine learning method, these steps were
repeated 20 times.
The results of these simulations for precision in estimation are shown in Figure 4. In
most considered data models IntCF achieves the best prediction results, especially for
the Interaction and Mixed model. For the Change point model, Forest DML and GRF,
both of which include a double machine learning/orthogonalization step, are the best
performing methods. Between the two methods that do not use this additional step,
26

Figure 5: ROC-AUC for feature importance as signal feature classifier for IntCF (blue),
Forest DML (yellow), causal forest (green) and GRF (red). For each method,
a band of one standard error is around the respective mean. In this figure,
higher values are better. Top left shows interaction model, top right change
point model, bottom left linear model, and bottom right mixed model.
IntCF has a better precision than causal forest in all cases except one (Interaction model
withs= 1).
Simulation results regarding feature importance are shown in Figure 5. In all considered
combinations of data model and complexity parameter s, the feature importance of IntCF
results in a ROC-AUC of almost 1, while each other method achieves smaller values in
most situations. This reflects a substantial improvement in interpretability, as IntCF is
best at identifying the features actually relevant for treatment effect heterogeneity. This
improvement is particularly notable given the relative simplicity of IntCF. As discussed in
Section 3, IntCF retains the same structure as the original RF: predictions are obtained
directly as the average of individual decision trees, with no additional correction step
required, and feature importance can be read off directly from the tree structure. Causal
forest shares this simple structure, but does not distinguish heterogeneity from bias when
selecting splits, and consequently performs worse in our feature importance comparison.
GRF and CausalForestDML, in contrast, rely on a substantially more involved procedure:
both incorporate an additional orthogonalization (double machine learning) step, which
27

wt71
smokeyrs
age
smokeintensity
education
active
exercise
sex
race
Feature
0.0
0.1
0.2
0.3
0.4
0.5Importance score
type
Heterogeneity score
Bias score
Figure 6: Importance scores for heterogeneity (blue) and bias (orange) produced by IntCF
for NHEFS data set. Features are sorted by heterogeneity score. For the bias
scores, negative values where truncated at 0.
alters the prediction mechanism and means that predictions can no longer be read off
directly from the individual trees, unlike for IntCF and causal forest. Despite this added
complexity, GRF and CausalForestDML do not achieve better feature importance scores
than IntCF in our simulations. IntCF thus achieves the strongest interpretability results
of all four methods while remaining, by construction, the structurally simplest.
5.3. Application on NHEFS Data set
Finally, we demonstrate the application of our algorithm on a real-world data set: the
National Health and Nutrition Examination Survey I Epidemiologic Followup Study
(NHEFS)2 is a longitudinal study of a cohort first examined in 1971–75. This data set
was also used previously to exemplify the handling of confounders and treatment effect
heterogeneity [Hernan and Robins, 2020]. Like Hernan and Robins [2020], we consider
data from 1566 smokers to estimate the effect of quitting smoking on weight change up to
the follow-up examination in 1982–84, using the same 9 baseline covariates as Hernan and
Robins [2020], including, e.g., the weight at the initial examination ( wt71), the number of
years of smoking (smokeyrs), and age ( age). Notably, our method does not require these
covariates to be labeled a priori as confounders or effect modifiers; instead, it attributes
each split to bias correction or heterogeneity directly from the fitted tree.
For the average treatment effect, we obtain an estimated weight gain of 3 .2 kg due to
quitting smoking, slightly lower than the 3 .4 kg reported by Hernan and Robins [2020].
2More information about this study can be found athttps://wwwn.cdc.gov/nchs/nhanes/nhefs/.
28

Additionally, we evaluate feature importance scores for the contribution to heterogeneity
and bias of the predictions, shown in Figure 6. As can be seen in Figure 6, the feature
with the highest heterogeneity importance is wt71, the weight at the initial examination,
consistent with other methods that identify this feature as having the strongest influence
on heterogeneity [see, e.g., B´ enard and Josse, 2025]. In addition, our bias importance
score identifiesageas the most relevant confounder.
6. Discussion
6.1. Summary
In this paper, we introduced the interpretable causal forest (IntCF), a modification of RF
for estimating individual treatment effects. The only change relative to standard RF is
the splitting criterion: by combining a heterogeneity criterion with a novel bias criterion,
each split can be attributed to either genuine heterogeneity in the treatment effect or a
correction for confounding bias. Together with a validation step that honestly re-evaluates
these contributions at each node (Section 3.2), this enables direct interpretation of the
resulting tree structure, for example through standard feature importance measures. We
supported this splitting criterion theoretically by analyzing its population limit under a
change point model tailored to causal inference, showing that it correctly attributes a
split to bias correction precisely when the naive difference-in-means estimator is biased,
and to heterogeneity precisely when the treatment effect is genuinely non-constant.
In simulations, IntCF achieved prediction accuracy competitive with established tree-
based methods, while substantially outperforming all of them in recovering the features
responsible for treatment effect heterogeneity, especially in the presence of confounders.
6.2. Simplicity as a Feature, not a Limitation
A recurring theme of this paper is that IntCF requires no machinery beyond a modified
splitting criterion: predictions are still obtained directly as the average of individual
decision trees, exactly as in the original RF. This stands in contrast to generalized random
forest and CausalForestDML, both of which rely on an additional orthogonalization
(double machine learning) step that changes the prediction mechanism and severs the
direct correspondence between the fitted trees and the resulting predictions. Causal forest
shares IntCF’s simple structure, but does not distinguish heterogeneity from bias at the
split level, and correspondingly falls short of IntCF’s interpretability in our simulations.
That IntCF exceeds the interpretability of substantially more complex competitors, while
remaining competitive with them in prediction accuracy, is in our view the central
practical contribution of this paper: interpretability need not come at the cost of added
model complexity.
29

6.3. Limitations and Future Work
Several open questions remain. On the theoretical side, our analysis of the splitting
criteria is currently limited to the population level; extending these results to finite
samples, to more general data-generating processes beyond the change point model, and
to the validation step from Section 3.2 are natural next steps. Likewise, our analysis
of marginalization effects in Section 4.2 considered only a single confounder at a time;
understanding how these effects interact in the presence of multiple, simultaneously
confounding features warrants further investigation.
Another open question is the consistency of the resulting IntCF estimator, which
we did not establish in this paper. We expect that an adaptation of the consistency
proof for causal forest from Wager and Athey [2018] should be feasible. Such a proof
typically requires the conditional mean function E[Y|X=x] to be Lipschitz continuous,
an assumption violated by the discontinuous change point model used in our theoretical
analysis. However, as tree depth increases, the fraction of samples affected by any such
discontinuity should vanish, suggesting that this is a technical rather than a fundamental
obstacle.
Code Availability
An implementation of IntCF, together with code to reproduce all analyses and figures in
this paper, is publicly available athttps://github.com/behr-group/intcf.
Acknowledgments
The project was funded by the Deutsche Forschungsgemeinschaft (DFG, German Research
Foundation), project number 509149993, TRR 374.
References
Abhineet Agarwal, Ana M. Kenney, Yan Shuo Tan, Tiffany M. Tang, and Bin Yu.
Integrating random forests and generalized linear models for improved accuracy and
interpretability, 2025. URLhttps://arxiv.org/abs/2307.01932.
Joshua D. Angrist and J¨ orn-Steffen Pischke.Mastering ’metrics: the path from cause to
effect. Princeton University Press, 2015.
Susan Athey and Guido Imbens. Recursive partitioning for heterogeneous causal effects.
Proceedings of the National Academy of Sciences, 113(27):7353–7360, 2016. doi:
10.1073/pnas.1510489113.
Susan Athey, Julie Tibshirani, and Stefan Wager. Generalized random forests.The
Annals of Statistics, 47(2):1148–1178, 2019. doi: 10.1214/18-AOS1709.
30

Vahid Balazadeh, Hamidreza Kamkari, Valentin Thomas, Benson Li, Junwei Ma, Jesse C.
Cresswell, and Rahul G. Krishnan. CausalPFN: Amortized causal effect estimation via
in-context learning. InAdvances in Neural Information Processing Systems, volume 38,
2025.
Sumanta Basu, Karl Kumbier, James B. Brown, and Bin Yu. Iterative random forests
to discover predictive and stable high-order interactions.Proceedings of the National
Academy of Sciences, 115(8):1943–1948, 2018. doi: 10.1073/pnas.1711236115.
Keith Battocchi, Eleanor Dillon, Maggie Hei, Greg Lewis, Paul Oka, Miruna Oprescu, and
Vasilis Syrgkanis. EconML: A Python Package for ML-Based Heterogeneous Treatment
Effects Estimation. https://github.com/py-why/EconML, 2019. Version 0.x.
Merle Behr, Yu Wang, Xiao Li, and Bin Yu. Provable boolean interaction recovery from
tree ensemble obtained via random forests.Proceedings of the National Academy of
Sciences, 119(22):e2118636119, 2022. doi: 10.1073/pnas.2118636119.
Leo Breiman. Random forests.Machine Learning, 45(1):5–32, 2001. doi: 10.1023/A:
1010933404324.
Leo Breiman, Jerome H. Friedman, Richard A. Olshen, and Charles J. Stone.Classification
and Regression Trees. Chapman and Hall/CRC, 1984. doi: 10.1201/9781315139470.
Cl´ ement B´ enard and Julie Josse. Variable importance for causal forests: breaking down
the heterogeneity of treatment effects.Journal of Causal Inference, 13(1):20230062,
2025. doi: 10.1515/jci-2023-0062.
Victor Chernozhukov, Denis Chetverikov, Mert Demirer, Esther Duflo, Christian Hansen,
Whitney Newey, and James Robins. Double/debiased machine learning for treatment
and structural parameters.The Econometrics Journal, 21(1):C1–C68, 2018. doi:
10.1111/ectj.12097.
Alicia Curth and Mihaela van der Schaar. Nonparametric estimation of heterogeneous
treatment effects: From theory to learning algorithms. InProceedings of the 24th
International Conference on Artificial Intelligence and Statistics (AISTATS), volume
130, pages 1810–1818, 2021.
Vincent Dorie, Jennifer Hill, Uri Shalit, Marc Scott, and Dan Cervone. Automated
versus do-it-yourself methods for causal inference: Lessons learned from a data analysis
competition.Statistical Science, 34(1):43–68, 2019. doi: 10.1214/18-STS667.
Miguel A. Hernan and James M. Robins.Causal Inference: What If. Chapman &
Hall/CRC, 2020.
Jennifer L. Hill. Bayesian nonparametric modeling for causal inference.Journal of
Computational and Graphical Statistics, 20(1):217–240, 2011. doi: 10.1198/jcgs.2010.
08162.
31

Guido W. Imbens and Donald B. Rubin.Causal Inference for Statistics, Social, and
Biomedical Sciences: An Introduction. Cambridge University Press, 2015. doi: 10.
1017/CBO9781139025751.
Hao Jiang, Peng Qi, Jingying Zhou, Jack Zhou, and Sharath Rao. A short survey on
forest based heterogeneous treatment effect estimation methods: Meta-learners and
specific models. In2021 IEEE International Conference on Big Data (Big Data), pages
3006–3012, 2021. doi: 10.1109/BigData52589.2021.9671439.
S¨ oren R. K¨ unzel, Jasjeet S. Sekhon, Peter J. Bickel, and Bin Yu. Metalearners for
estimating heterogeneous treatment effects using machine learning.Proceedings of the
National Academy of Sciences, 116(10):4156–4165, 2019. doi: 10.1073/pnas.1804597116.
Robert J. LaLonde. Evaluating the econometric evaluations of training programs with
experimental data.The American Economic Review, 76(4):604–620, 1986.
Xiao Li, Yu Wang, Sumanta Basu, Karl Kumbier, and Bin Yu. A debiased MDI feature
importance measure for random forests. InAdvances in Neural Information Processing
Systems, volume 32. 2019.
Scott M. Lundberg, Gabriel Erion, Hugh Chen, Alex DeGrave, Jordan M. Prutkin, Bala
Nair, Ronit Katz, Jonathan Himmelfarb, Nisha Bansal, and Su-In Lee. From local
explanations to global understanding with explainable AI for trees.Nature Machine
Intelligence, 2(1):56–67, 2020. doi: 10.1038/s42256-019-0138-9.
Charles F. Manski. Identification problems in the social sciences.Sociological Methodology,
23:1–56, 1993. doi: 10.2307/271005.
Brady Neal, Chin-Wei Huang, and Sunand Raghupathi. RealCause: Realistic causal
inference benchmarking, 2021. URLhttps://arxiv.org/abs/2011.15007.
Miruna Oprescu, Vasilis Syrgkanis, and Zhiwei Steven Wu. Orthogonal random forest
for causal inference. InProceedings of the 36th International Conference on Machine
Learning, volume 97, pages 4932–4941, 2019.
Fabian Pedregosa, Ga¨ el Varoquaux, Alexandre Gramfort, Vincent Michel, Bertrand
Thirion, Olivier Grisel, Mathieu Blondel, Peter Prettenhofer, Ron Weiss, Vincent
Dubourg, Jake Vanderplas, Alexandre Passos, David Cournapeau, Matthieu Brucher,
Matthieu Perrot, and ´Edouard Duchesnay. Scikit-learn: Machine learning in Python.
Journal of Machine Learning Research, 12(85):2825–2830, 2011.
Craig T. Ramey, Donna M. Bryant, Barbara H. Wasik, Joseph J. Sparling, Kaye H. Fendt,
and Lisa M. La Vange. Infant health and development program for low birth weight,
premature infants: program elements, family participation, and child intelligence.
Pediatrics, 89(3):454–465, 1992. doi: 10.1542/peds.89.3.454.
Paul R. Rosenbaum and Donald B. Rubin. The central role of the propensity score in
observational studies for causal effects.Biometrika, 70(1):41–55, 1983. doi: 10.1093/
biomet/70.1.41.
32

Donald B. Rubin. Estimating causal effects of treatments in randomized and non-
randomized studies.Journal of Educational Psychology, 66(5):688–701, 1974. doi:
10.1037/h0037350.
Erwan Scornet and Giles Hooker. Theory of random forests.Annual Review of Statistics
and Its Application, 13:99–121, 2026. doi: 10.1146/annurev-statistics-112723-034707.
Uri Shalit, Fredrik D. Johansson, and David Sontag. Estimating individual treatment
effect: generalization bounds and algorithms. InProceedings of the 34th International
Conference on Machine Learning, volume 70, pages 3076–3085, 2017.
Claudia Shi, David Blei, and Victor Veitch. Adapting neural networks for the estimation
of treatment effects. InAdvances in Neural Information Processing Systems, volume 32.
2019.
Assaf Shmuel, Oren Glickman, and Teddy Lazebnik. A comprehensive benchmark of
machine and deep learning models on structured data for regression and classification.
Neurocomputing, 655:131337, 2025. doi: 10.1016/j.neucom.2025.131337.
Stefan Wager and Susan Athey. Estimation and inference of heterogeneous treatment
effects using random forests.Journal of the American Statistical Association, 113(523):
1228–1242, 2018. doi: 10.1080/01621459.2017.1319839.
Zhengze Zhou and Giles Hooker. Unbiased measurement of feature importance in tree-
based methods.ACM Transactions on Knowledge Discovery from Data (TKDD), 15
(2):26:1–26:21, 2021. doi: 10.1145/3429445.
33

A. Proofs
A.1. Proofs of Section 3
Proof of Lemma 1. In the following computation, the property Jparent = JL ⊔J R is used
in the second equation and Assumption (12) is used in the third equation:
1
N
X
i∈Jparent
(ˆτparent −τ i)2 − 1 N

 X
i∈JL
(ˆτL −τ i)2 + X
i∈JR
(ˆτR −τ i)2


= 1 N

 X
i∈Jparent
ˆτ2 parent − X
i∈Jparent
2ˆτparentτi +
X
i∈Jparent
τ 2 i


− 1 N



 X
i∈JL
ˆτ2 L − X
i∈JL
2ˆτLτi +
X
i∈JL
τ 2 i

 +

 X
i∈JR
ˆτ2 R − X
i∈JR
2ˆτRτi +
X
i∈JR
τ 2 i




= 1 N

(nL +n R)ˆτ2 parent −2ˆτparent

 X
i∈JL
τi +
X
i∈JR
τi

 + X
i∈Jparent
τ 2 i


− 1 N

nLˆτ2 L −2ˆτL X
i∈JL
τi +n R ˆτ2 R −2ˆτR X
i∈JR
τi +
X
i∈Jparent
τ 2 i


= 1 N

(nL +n R)ˆτ2 parent −2ˆτparent(nLτL +n RτR) + X
i∈Jparent
τ 2 i


− 1 N

nLˆτ2 L −2n Lˆτ2 L +n R ˆτ2 R −2n R ˆτ2 R + X
i∈Jparent
τ 2 i


= 1 N  (nL +n R)ˆτ2 parent −2ˆτparent(nLτL +n RτR) +n Lˆτ2 L +n R ˆτ2 R 
= 1 N (nL(ˆτparent −ˆτL)2 +n R(ˆτparent −ˆτR)2)
34

Proof of Lemma 2.By using assumption (13) direct computation yields:
1
N (nL(ˆτparent −ˆτL)2 +n R(ˆτparent −ˆτR)2)
= 1 N

nL
 nLˆτL +n R ˆτR
nL +n R
−ˆτL
2
+n R
 nLˆτL +n R ˆτR
nL +n R
−ˆτR
2!
= 1 N

nL
 −nR ˆτL +n R ˆτR
nL +n R
2
+n R
 nLˆτL −n LˆτR
nL +n R
2!
= 1 N  nL ·n 2 R (nL +n R)2 (−ˆτL + ˆτR)2 + n2 L ·n R (nL +n R)2 (ˆτL −ˆτR)2 
= nL ·n R
N(n L +n R)
 nR
nL +n R
(ˆτL −ˆτR)2 + nL nL +n R (ˆτL −ˆτR)2

= nL ·n R
N(n L +n R) (ˆτL −ˆτR)2
Proof of Lemma 3.By direct computation:
1
N (nL(ˆτparent −ˆτL)2 +n R(ˆτparent −ˆτR)2)− nL ·n R N(n L +n R) (ˆτL −ˆτR)2
= 1 N  nL(ˆτparent −ˆτL)2 +n R(ˆτparent −ˆτR)2 − nL ·n R nL +n R (ˆτL −ˆτR)2 
= 1 N  nL(ˆτ2 parent −2ˆτparentˆτL + ˆτ2 L) +n R(ˆτ2 parent −2ˆτparentˆτR + ˆτ2 R)
− nL ·n R
nL +n R
(ˆτ2 L −2ˆτLˆτR + ˆτ2 R)

= 1 N  (nL +n R)ˆτ2 parent −2ˆτparent(nLˆτL +n R ˆτR)
+ n2 L
nL +n R
ˆτ2 L + 2 nL ·n R nL +n R ˆτLˆτR + n2 R nL +n R ˆτ2 R 
= nL +n R
N

ˆτ2 parent −2ˆτnLˆτL +n R ˆτR nL +n R +  nLˆτL +n R ˆτR nL +n R 2!
= nL +n R
N

ˆτparent − nLˆτL +n R ˆτR nL +n R
2
35

Proof of Lemma 4.At each nodeewe have ˆτ b e = 1 n P i∈Ie ˆτval i , so
X
i∈Ie

ˆτf e −ˆτval i
2
−
X
i∈Ie

ˆτb e −ˆτval i
2
=
X
i∈Ie

(ˆτf e)2 −2ˆτf e ˆτval i + (ˆτval i )2

−
X
i∈Ie

(ˆτb e )2 −2ˆτb e ˆτval i + (ˆτval i )2

=n

(ˆτf e)2 −(ˆτb e )2

+ 2

ˆτb e −ˆτf e
 X
i∈Ie
ˆτval i
=n

(ˆτf e)2 −(ˆτb e )2

+ 2

ˆτb e −ˆτf e

·n·ˆτ b e
=n

(ˆτf e)2 −(ˆτb e )2 + 2(ˆτb e )2 −2ˆτf e ˆτb e

=n

(ˆτf e)2 −2ˆτf e ˆτb e + (ˆτb e )2

=n

ˆτf e −ˆτb e
2
,
and, using ˆτb parent = nL ˆτb L+nR ˆτb R nL+nR , we get
X
i∈Iparent

ˆτb parent −ˆτval i
2
−
X
i∈IL

ˆτb L −ˆτval i
2
−
X
i∈IR

ˆτb R −ˆτval i
2
=
X
i∈IR

(ˆτb parent)2 −2ˆτb parentˆτval i + (ˆτval i )2

−
X
i∈IL

(ˆτb L)2 −2ˆτb L ˆτval i + (ˆτval i )2

−
X
i∈IR

(ˆτb R)2 −2ˆτb R ˆτval i + (ˆτval i )2

= (nL +n R)(ˆτb parent)2 −2(n L +n R)(ˆτb parent)2
−n L(ˆτb L)2 + 2nL(ˆτb L)2 −n R(ˆτb R)2 + 2nR(ˆτb R)2
=−(n L +n R)(ˆτb parent)2 +n L(ˆτb L)2 +n R(ˆτb R)2
=n L(ˆτb L)2 +n R(ˆτb R)2 −(n L +n R)
 nLˆτb L +n R ˆτb R
nL +n R
2
= (nL +n R)nL(ˆτb L)2 + (nL +n R)nR(ˆτb R)2 −n 2 L(ˆτb L)2 −2n LnR ˆτb L ˆτb R −n 2 R(ˆτb R)2
nL +n R
= nL ·n R
nL +n R

ˆτb L −ˆτb R
2
.
Combining these results, we have
X
i∈Iparent

ˆτf parent −ˆτval i
2
−
X
i∈IL

ˆτf L −ˆτval i
2
−
X
i∈IR

ˆτf R −ˆτval i
2
=
nL ·n R
nL +n R

ˆτb L −ˆτb R
2
+ nL +n R
N

ˆτf parent −ˆτb parent
2
− nL
N

ˆτf L −ˆτb L
2
− nR
N

ˆτf R −ˆτb R
2
.
36

A.2. Proof of Theorem 5
Remark 4.In the following statements and proofs, we will assume w.l.o.g. that the
covariate X is uniformly distributed on[0 , 1], also implying R(e) = [0, 1]. If its domain
would be a different interval[a, b], replacing it by X−a b−a —as well as performing the same
transformation for γ and k—would create an equivalent model with the same values for
treatment effect estimates and (signed) splitting criteria.
Lemma 7.For the univariate change-point model (27) with potential outcomes as in (28),
assuming Assumption A3 holds, the bias of the difference-in-means estimate as defined
in(29)is given by

E

Y T=1 |T= 1  −E  Y T=0 |T= 0  −E[τ(X)]
=γ(1−γ)q 1
α1 + (1/2−q 0 −γq 1)β1
(q0 +γq 1)(1−q 0 −γq 1) .(34)
Proof. Because of Assumption A3, the conditional expectations are well defined and we
have
E

Y T=0 |T= 0  =α 0 −β 0/2 + (α1 −β 1/2)γ(1−q 0 −q 1) 1−q 0 −γq 1 ,
E

Y T=1 |T= 1  =α 0 +β 0/2 + (α1 +β 1/2)γ(q0 +q 1) q0 +γq 1
and hence,
E

Y T=1 |T= 1  −E  Y T=0 |T= 0 
=β0 + (α1 +β 1/2)γ(q0 +q 1) q0 +γq 1 − (α1 −β 1/2)γ(1−q 0 −q 1) 1−q 0 −γq 1
=β0 +γ(α 1 −β 1/2) (1−γ)q 1 (q0 +γq 1)(1−q 0 −γq 1) +γβ 1

1 + (1−γ)q 1
q0 +γq 1

.
Moreover, we haveE[τ(X)] =β 0 +γβ 1 and hence,

E

Y T=1 |T= 1  −E  Y T=0 |T= 0  −E[τ(X)]
=(α1 −β 1/2) γ(1−γ)q 1 (q0 +γq 1)(1−q 0 −γq 1) +β 1 γ(1−γ)q 1 q0 +γq 1
=γ(1−γ)q 1
α1 + (1/2−q 0 −γq 1)β1
(q0 +γq 1)(1−q 0 −γq 1) .
Proof for Theorem 5.Define
α′ 0 :=α 0, α ′ 1 :=α 1 −α ′′ 1, β ′ 0 :=β 0,
α′′ 0 := 0, α ′′ 1 :=−(1/2−q 0 −γq 1)β1, β ′′ 0 := 0, β ′′ 1 :=β 1.
With these definitions, µ(x) = µB(x) + µH (x) and τ (x) = τ B(x) + τ H (x) follows directly.
37

For the second model, we consider the difference between the difference-in-means
prediction E

τ H (X)  = E  µH (X) + 1 2 τ H (X)|T= 1  −E  µH (X)− 1 2 τ H (X)|T= 0 
and the expectation of the treatment effectE

τ H (X)  . By Lemma 7 this is given by
γ(1−γ)q 1
α′′ 1 + (1/2−q 0 −γq 1)β′′ 1
(q0 +γq 1)(1−q 0 −γq 1) = 0,
where for the evaluation we used α′′ 1 = −(1/2 −q 0 −γq 1)β1 and β′′ 1 = β1. So the
difference-in-means estimator is in expectation equal to the treatment effect, i.e., is
unbiased.
A.3. Proof of Theorem 6
Remark 5.We will continue assumingX∼U([0,1]), see Remark 4.
Further we will assume that γ∈ (0, 1)in (27). For values outside(0 , 1), there is a
model with β1 = q1 = α1 = 0and γ∈ (0, 1)which has almost surely the same propensities
and expected outcomes, which therefore also result in the same expected predictions and
(signed) splitting criteria.
Lemma 8.For the univariate change-point model (27), assuming Assumption A3 holds,
with potential outcomes as in(28)and a split pointk∈(0,1)define
ˆτ∞ L :=E  Y T=1 |X≤k, T= 1  −E  Y T=0 |X≤k, T= 0  ,
ˆτ∞ R :=E  Y T=1 |X > k, T= 1  −E  Y T=0 |X > k, T= 0  (35)
Then we have
ˆτ∞ L =
(
β0 +β 1 k≤γ,
β0 + (α1 −β 1/2) γ(k−γ)q 1 (kq0+γq1)(k−kq0−γq1) +β 1

1− (k−γ)q 0 kq0+γq1

k > γ
and
ˆτ∞ R =



β0 + (α1 −β 1/2) (γ−k)(1−γ)q 1 ((1−k)q 0 + (γ−k)q 1)((1−k)(1−q 0)−(γ−k)q 1)
+β 1

1− (1−γ)q 0
(1−k)q 0 + (γ−k)q 1
 k≤γ,
β0 k > γ.
Proof.For a splitting pointk, we have
E

Y T=0 |X≤k, T= 0  =
(
α0 −β 0/2 +α 1 −β 1/2k≤γ,
α0 −β 0/2 + (α1−β1/2)γ(1−q0−q1) k−kq0−γq1 k > γ,
E

Y T=1 |X≤k, T= 1  =
(
α0 +β 0/2 +α 1 +β 1/2k≤γ,
α0 +β 0/2 + (α1+β1/2)γ(q0+q1) kq0+γq1 k > γ,
38

and hence,
ˆτ∞ L =
(
β0 +β 1 k≤γ,
β0 + (α1 −β 1/2) γ(k−γ)q 1 (kq0+γq1)(k−kq0−γq1) +β 1

1− (k−γ)q 0 kq0+γq1

k > γ.
Moreover, we have
E

Y T=0 |X > k, T= 0  =
(
α0 −β 0/2 + (α1−β1/2)(γ−k)(1−q 0−q1) (1−k)(1−q0)−(γ−k)q 1 k≤γ,
α0 −β 0/2k > γ,
E

Y T=1 |X > k, T= 1  =
(
α0 +β 0/2 + (α1+β1/2)(γ−k)(q 0+q1) (1−k)q0+(γ−k)q 1 k≤γ,
α0 +β 0/2k > γ,
and hence,
ˆτ∞ R =



β0 + (α1 −β 1/2) (γ−k)(1−γ)q 1 ((1−k)q 0 + (γ−k)q 1)((1−k)(1−q 0)−(γ−k)q 1)
+β 1

1− (1−γ)q 0
(1−k)q 0 + (γ−k)q 1
 k≤γ,
β0 k > γ.
Note that all terms in the denominators are either treatment propensities for some subset
of samples, scaled versions of these, or a product of multiple such propensities. By
Assumption A3, these are positive, so all terms are defined.
Proof of Theorem 6.Use the notation from (35) and
ˆτ∞ parent :=E  Y T=1 |T= 1  −E  Y T=0 |T= 0 
=β 0 +γ(α 1 −β 1/2) (1−γ)q 1 (q0 +γq 1)(1−q 0 −γq 1) +γβ 1

1 + (1−γ)q 1
q0 +γq 1

,
as calculated in Lemma 8. Note that we can write
Het±(k) = p k(1−k)·(ˆτ ∞ L −ˆτ∞ R ),
Bias±(k) = ˆτ∞ parent −kˆτ∞ L −(1−k)ˆτ ∞ R .
Further note, that α0 does not appear in any of ˆτ∞ parent,ˆτ∞ L ,ˆτ∞ R , so it does not have
any effect on Het±(k) or Bias±(k). Additionally, β0 appears in all three treatment effect
estimates, but always as simple summand. So changing it does not have any effect
on the differences ˆτ∞ L −ˆτ∞ R and ˆτ∞ parent −kˆτ∞ L − (1 −k )ˆτ∞ R , which define Het±(k) and
Bias±(k). To simplify notation, we will therefore, without loss of generality, set all of
α0, α′ 0, α′′ 0, β0, β′ 0, β′′ 0 zero for the following analysis of the signed splitting criteria.
We proof the two statements (for bias and for heterogeneity) of the theorem separately.
39

BiasAfter settingα ′ 0 =β ′ 0 = 0, as explained above, the bias model is given by
µB(x) =α ′ 1 ·1 x≤γ,
τ B(x) = 0,
p(x) =q 0 +q 1 ·1 x≤γ.
In this model, the estimated treatment effect tends to
ˆτ∞ parent =γα ′ 1 (1−γ)q 1 (q0 +γq 1)(1−q 0 −γq 1) ,
while the true treatment effect is constant zero:τ B = 0.
In the child nodes for a split atk, the estimates are
ˆτ∞ L =
(
0k≤γ,
α′ 1 γ(k−γ)q 1 (kq0+γq1)(k−kq0−γq1) k > γ,
ˆτ∞ R =
(
α′ 1 (γ−k)(1−γ)q 1 ((1−k)q0+(γ−k)q 1)((1−k)(1−q0)−(γ−k)q 1) k≤γ,
0k > γ.
Therefore, the population signed splitting criteria are given by
Het± B(k) = p k(1−k)(ˆτ ∞ L −ˆτ∞ R ),
=



p
k(1−k)

0−α ′ 1 (γ−k)(1−γ)q 1 ((1−k)q0+(γ−k)q 1)((1−k)(1−q0)−(γ−k)q 1)

k≤γ,
p
k(1−k)

α′ 1 γ(k−γ)q 1 (kq0+γq1)(k−kq0−γq1) −0  k > γ,
=
(
−
p
k(1−k)α ′ 1 (γ−k)(1−γ)q 1 ((1−k)q0+(γ−k)q 1)((1−k)(1−q0)−(γ−k)q 1) k≤γ,p
k(1−k)α ′ 1 (k−γ)γq 1 (kq0+γq1)(k−kq0−γq1) k > γ,
Bias± B(k) = ˆτ∞ parent −kˆτ∞ L −(1−k)ˆτ ∞ R
=
(
γα′ 1 (1−γ)q1 (q0+γq1)(1−q0−γq1) −k·0−(1−k)α′ 1 (γ−k)(1−γ)q 1 ((1−k)q0+(γ−k)q1)((1−k)(1−q0)−(γ−k)q1) k≤γ,
γα′ 1 (1−γ)q1 (q0+γq1)(1−q0−γq1) −kα ′ 1 γ(k−γ)q 1 (kq0+γq1)(k−kq0−γq1) −(1−k)·0k > γ,
=
(
α′ 1
 γ(1−γ)q 1
(q0+γq1)(1−q0−γq1) −(1−k) (γ−k)(1−γ)q 1 ((1−k)q0+(γ−k)q1)((1−k)(1−q0)−(γ−k)q1)  k≤γ,
α′ 1

γ(1−γ)q 1
(q0+γq1)(1−q0−γq1) −k γ(k−γ)q 1 (kq0+γq1)(k−kq0−γq1)

k > γ,
Note that Het ± B(k) and Bias ± B(k) are both continuous and atk=γwe have
Het± B(γ) = 0
Bias± B(γ) =α ′ 1 γ(1−γ)q 1 (q0 +γq 1)(1−q 0 −γq 1) .
40

Recall from Theorem 5 that µ(x) = µB(x) + µH (x) and τ (x) = τ B(x) + τ H (x) and
hence,
E[τ(X)] =E

τ B(X)  +E  τ H (X)  ,
E

µ(X)+ 1 2 τ(X)|T= 1  =E  µB(X)+ 1 2 τ B(X)|T= 1  +E  µH (X)+ 1 2 τ H (X)|T= 1  ,
E

µ(X)− 1 2 τ(X)|T= 0  =E  µB(X)− 1 2 τ B(X)|T= 0  +E  µH (X)− 1 2 τ H (X)|T= 0  .
From (30) it follows that
E

µ(X) + 1 2 τ(X)|T= 1  −E  µ(X)− 1 2 τ(X)|T= 0  −E[τ(X)]
=E

µB(X) + 1 2 τ B(X)|T= 1  −E  µB(X)− 1 2 τ B(X)|T= 0  −E  τ B(X)  .
By Lemma 7 the right-hand side of this equation is equal to Bias± B(γ). Because we
assume that the difference-in-means estimator of the original model is biased, i.e.,
E

µ(X) + 1 2 τ(X)|T= 1  −E  µ(X)− 1 2 τ(X)|T= 0  −E[τ(X)]̸ = 0, it follows that
Bias± B(γ) ̸= 0 along with α′ 1 ̸= 0 and q1 ̸= 0. Moreover, as Bias± B(0) = Bias± B(1) = 0, it
follows that Bias± B is non-constant and we will show that it has a global extremum at
k=γ.
Considering the derivative of Bias ± B fork > γyields
d
dk α′ 1
 γ(1−γ)q 1
(q0 +γq 1)(1−q 0 −γq 1) −k γ(k−γ)q 1 (kq0 +γq 1)(k−kq 0 −γq 1) 
=−α ′ 1
 (γ(k−γ)q 1 +kγq 1)(kq0 +γq 1)(k−kq 0 −γq 1)
(kq0 +γq 1)2(k−kq 0 −γq 1)2
− kγ(k−γ)q 1(q0(k−kq 0 −γq 1) + (kq0 +γq 1)(1−q 0)) (kq0 +γq 1)2(k−kq 0 −γq 1)2

=−α ′ 1γ2q1 (q2 0 + 2q0q1 −q 0 −q 1)k2 + 2γq2 1k−γ 2q2 1 (kq0 +γq 1)2(k−kq 0 −γq 1)2 .
Note that Bias± B is contentiously differentiable in (γ, 1). Hence, for a potential extremum
kof Bias ± B in (γ,1), we would need
0 =−α ′ 1γ2q1 (q2 0 + 2q0q1 −q 0 −q 1)k2 + 2γq2 1k−γ 2q2 1 (kq0 +γq 1)2(k−kq 0 −γq 1)2
⇐ ⇒0 = (q2 0 + 2q0q1 −q 0 −q 1)k2 + 2γq2 1k−γ 2q2 1
⇐ ⇒k=−2γq 2 1 ± p (2γq 2 1)2 −4(q 2 0 + 2q0q1 −q 0 −q 1)(−γ2q2 1) 2(q2 0 + 2q0q1 −q 0 −q 1) ,
but the discriminant is
(2γq 2 1)2 −4(q 2 0 + 2q0q1 −q 0 −q 1)(−γ2q2 1)
= 4γ2q4 1 + 4γ2q2 0q2 1 + 8γ2q0q3 1 −4γ 2q0q2 1 −4γ 2q3 1
=−4γ 2q2 1(q0 +q 1)(1−q 0 −q 1)<0.
41

Therefore, there are no local extrema for k∈ (γ, 1). Similarly, there are also no local
extrema within (0 , γ). As Bias± B is continuous and non-constant with Bias± B(k) = 0 at
k= 0 andk= 1, Bias ± B(γ) must be a global extremum.
HeterogeneityAfter setting α′′ 0 = β′′ 0 = 0, as explained above, the heterogeneity model
is given by
µH (x) =α ′′ 1 ·1 x≤γ,
τ H (x) =β ′′ 1 ·1 x≤γ,
p(x) =q 0 +q 1 ·1 x≤γ,
withα ′′ 1 =−(1/2−q 0 −γq 1)β′′ 1 , such that the bias calculated in Lemma 7 is 0.
For this model, the treatment effect obtained from the difference-in-means estimator
tends to the correct average treatment effect, i.e., ˆτ∞ parent = E[τ(X)] = γβ ′′ 1 and the
estimates in the child nodes converge to
ˆτ∞ L =
(
β′′ 1 k≤γ,
β′′ 1

1−(k−γ) (kq0+γq1)(1−q0)−(q0+γq1)γq1 (kq0+γq1)(k−kq0−γq1)

k > γ,
ˆτ∞ R =
(
β′′ 1 (γ−k) (q0+γq1)(1−q0−γq1)−k(q0+q1)(1−q0−q1) ((1−k)q0+(γ−k)q 1)((1−k)(1−q0)−(γ−k)q 1) k≤γ,
0k > γ,
which can be calculated by using α′′ 1 = −(1/2 −q 0 −γq 1)β′′ 1 in the formulas given by
Lemma 8. The population signed splitting criteria evaluate to
Het± H (k) = p k(1−k)(ˆτ ∞ L −ˆτ∞ R ),
=



p
k(1−k)

β′′ 1 −β ′′ 1 (γ−k) (q0+γq1)(1−q0−γq1)−k(q0+q1)(1−q0−q1) ((1−k)q0+(γ−k)q 1)((1−k)(1−q0)−(γ−k)q 1)

k≤γ,
p
k(1−k)

β′′ 1

1−(k−γ) (kq0+γq1)(1−q0)−(q0+γq1)γq1 (kq0+γq1)(k−kq0−γq1)

−0

k > γ,
=



β′′ 1 p k(1−k)  1−(γ−k) (q0+γq1)(1−q0−γq1)−k(q0+q1)(1−q0−q1) ((1−k)q0+(γ−k)q 1)((1−k)(1−q0)−(γ−k)q 1)  k≤γ,
β′′ 1 p k(1−k)  1−(k−γ) (kq0+γq1)(1−q0)−(q0+γq1)γq1 (kq0+γq1)(k−kq0−γq1)  k > γ,
Bias± H (k) = ˆτ∞ parent −kˆτ∞ L −(1−k)ˆτ ∞ R
=



γβ ′′ 1 −kβ ′′ 1 −(1−k)β ′′ 1 (γ−k) (q0+γq1)(1−q0−γq1)−k(q0+q1)(1−q0−q1) ((1−k)q0+(γ−k)q 1)((1−k)(1−q0)−(γ−k)q 1) k≤γ,
γβ ′′ 1 −kβ ′′ 1

1−(k−γ) (kq0+γq1)(1−q0)−(q0+γq1)γq1 (kq0+γq1)(k−kq0−γq1)

−(1−k)·0k > γ,
=



−β′′ 1 (γ−k) k(1−γ) 2q2 1 ((1−k)q0+(γ−k)q 1)((1−k)(1−q0)−(γ−k)q 1) k≤γ,
β′′ 1 (k−γ) (1−k)γ 2q2 1 (kq0+γq1)(k−kq0−γq1) k > γ
Note that Het ± H (k) and Bias ± H (k) are both continuous and atk=γwe have
Het± H (γ) =β ′′ 1 p γ(1−γ),
Bias± H (γ) = 0.
42

If the treatment effect of the original model τ (x) is non-constant, it follows that 0 < γ <1,
β1 ̸= 0, and β′′ 1 ̸= 0. This implies Het± H (γ) ̸= 0 and, as Het± H (0) = Het± H (1) = 0, that
Het± H non-constant. We will now show that Het ± H (γ) is a local extremum.
Considering the derivative of Het ± H fork < γyields
d
dk Het± H (k) =β ′′ 1 p k(1−k)
·
 1−2k
2k(1−k) + (q0 +γq 1)(1−q 0 −γq 1)−k(q 0 +q 1)(1−q 0 −q 1) ((1−k)q 0 + (γ−k)q 1)((1−k)(1−q 0)−(γ−k)q 1) 
−β ′′ 1 p k(1−k)(γ−k)
·

− (q0 +q 1)(1−q 0 −q 1) ((1−k)q 0 + (γ−k)q 1)((1−k)(1−q 0)−(γ−k)q 1)
+ (q0 +q 1) (q0 +γq 1)(1−q 0 −γq 1)−k(q 0 +q 1)(1−q 0 −q 1) ((1−k)q 0 + (γ−k)q 1)2((1−k)(1−q 0)−(γ−k)q 1)
+ (1−q 0 −q 1) (q0 +γq 1)(1−q 0 −γq 1)−k(q 0 +q 1)(1−q 0 −q 1) ((1−k)q 0 + (γ−k)q 1)((1−k)(1−q 0)−(γ−k)q 1)2
+ 1−2k 2k(1−k) (q0 +γq 1)(1−q 0 −γq 1)−k(q 0 +q 1)(1−q 0 −q 1) ((1−k)q 0 + (γ−k)q 1)((1−k)(1−q 0)−(γ−k)q 1) 
and fork > γ
d
dk Het± H (k) =β ′′ 1 p k(1−k)  1−2k 2k(1−k) − (kq0 +γq 1)(1−q 0)−(q 0 +γq 1)γq1 (kq0 +γq 1)(k−kq 0 −γq 1) 
+β ′′ 1 p k(1−k)(k−γ)  − q0(1−q 0) (kq0 +γq 1)(k−kq 0 −γq 1)
+q 0
(kq0 +γq 1)(1−q 0)−(q 0 +γq 1)γq1
(kq0 +γq 1)2(k−kq 0 −γq 1)
+ (1−q 0) (kq0 +γq 1)(1−q 0)−(q 0 +γq 1)γq1 (kq0 +γq 1)(k−kq 0 −γq 1)2
− 1−2k 2k(1−k) (kq0 +γq 1)(1−q 0)−(q 0 +γq 1)γq1 (kq0 +γq 1)(k−kq 0 −γq 1)  .
Note that Het± H (k) is continuously differentiable in (0 , γ) and in ( γ, 1). The limits of
these derivatives atγare
lim
k→γ −
d
dk Het± H (k) =β ′′ 1 p γ(1−γ) q0(1−q 0) + 2γ2q2 1 2γ(1−γ)q 0(1−q 0)
lim
k→γ +
d
dk Het± H (k) =−β ′′ 1 p γ(1−γ) (1−q 0 −q 1)(q0 +q 1) + 2(1−γ) 2q2 1 2γ(1−γ)(q 0 +q 1)(1−q 0 −q 1)
All of γ, (1 −γ ), q0, (1 −q 0), (q0 + q1) and (1 −q 0 −q 1) are assumed to be posi-
tive by Assumptions A3 and γ∈ (0, 1), as well as q2 1 ≥ 0. Therefore, we have
sgn(limk→γ − d dk Het± H (k)) = sgn(β′′ 1 ) and sgn(limk→γ + d dk Het± H (k)) = −sgn (β′′ 1 ). Also
note that sgn(Het± H (γ)) = sgn(β′′ 1 ). Together, it follows that Het± H (γ) has a local ex-
tremum atk=γ.
43
