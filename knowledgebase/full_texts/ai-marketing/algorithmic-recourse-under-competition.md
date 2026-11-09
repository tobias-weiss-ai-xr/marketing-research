---
title: Algorithmic Recourse Under Competition
url: https://arxiv.org/abs/2609.39877
category: ai-marketing
subcategory: measurement
date: 2026-09
venue: ''
authors:
- Shahin Jabbari
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.39877
pages: 21
chars: 60825
fetched_at: '2026-11-08T13:25:28+00:00'
kb_version: 1
---

# Algorithmic Recourse Under Competition

Algorithmic Recourse Under Competition
Shahin Jabbari ∗
Abstract
Algorithmic recourse provides individuals who have received undesirable outcomes from machine
learning models with suggestions for minimum-cost improvements to achieve the desired outcome. A
central assumption when computing recourse is that the decision rule remains fixed throughout the
recourse implementation phase. We challenge this assumption in settings where individuals compete
for limited resources. In such settings, widespread recourse implementation can change the acceptance
threshold even when the scoring model that is used to evaluate individuals remains the same. This change
in acceptance threshold can, in turn, invalidate the original recourse recommendations (i.e., following the
recourse may not lead to the desired outcome). To address this problem, we introduce a framework called
recourse under competitionthat jointly optimizes for recommendation recipients and the recommended
score target they need to satisfy to balance the recourse cost and post-shift validity among initially
rejected individuals. We develop an algorithm based on the Implicit Function Theorem and empirically
analyze its performance. Experiments on synthetic and real datasets show that personalized score targets
can achieve higher validity, albeit at a higher cost. In contrast, common score targets generally offer
favorable cost-validity trade-offs for lower to medium validity values.
1 Introduction
With the rapid deployment of machine learning models in critical domains and the major impact of their
decisions on people’s livelihoods, a surge of recent work in responsible machine learning aims to make these
models fair [3, 5, 23, 64], transparent [38, 52], and explainable [42, 51, 55]. A recent line of work within
the explainability literature, termedalgorithmic recourse[ 59, 62], involves the decision-maker providing
individuals who received an undesirable label (e.g., one whose loan request was denied) with minimum-cost
improvement suggestions to achieve the desired label.
A central assumption when computing recourse is that the decision rule remains fixed during the time
needed for individuals to implement their modifications. However, this assumption can fail in settings where
individuals compete for limited resources, and only a limited number or fraction of individuals can be accepted
(e.g., a fixed number of approved loans or university admissions). As individuals implement recourse, they
alter the population’s distribution. To maintain the acceptance rate dictated by limited resources, the
decision-maker recomputes the acceptance threshold for the updated population, even when its scoring model
remains unchanged. The updated threshold can invalidate the initially prescribed recourse, i.e., following the
suggestions may no longer lead to the desired outcome. Prior work has shown reaching the original acceptance
threshold is insufficient to ensure acceptance under competition [16]. This motivates designing recourse
recommendation strategies that explicitly anticipate the competition induced by their implementation.
In this work, we proposerecourse under competition, a framework that explicitly anticipates future updates
in acceptance threshold in competitive environments. In this formulation, the individuals are restricted by a
budget for their feature modification, and the decision-maker simultaneously should decide which individuals
should be instructed to implement recourse and what score target each such individual should aim for. Our
main goal is to understand the trade-off between the expected recourse cost across the population of rejected
individuals against the validity of recourse, after accounting for distribution changes and acceptance threshold
updates caused by recourse implementation.
∗Drexel University, shahin@drexel.edu
1
arXiv:2609.39877v1  [cs.LG]  30 Sep 2026

Our Results and Contributions.We formalizerecourse under competition, a framework for balancing
recourse cost and post-shift validity through population-level recommendation policies. We develop an
optimization algorithm based on the Implicit Function Theorem that anticipates future updates in the
selection threshold when recommending recourse.
We evaluate our algorithm on four real datasets and two synthetic datasets to study the trade-off between
the cost of recourse implementation and its validity after competitive threshold updates. We observe empirical
convergence of the smooth training objective across different datasets and model classes. Our main findings
indicate that anticipating recourse-induced threshold changes can significantly improve the validity of recourse
compared to the original-threshold baseline that do not consider competition when providing recourse. We
also find that personalized score targets can achieve higher validity at greater cost, while common score
targets often offer better tradeoffs at lower to medium validity values. Sensitivity experiments show that larger
budgets and admission rates generally increase validity. We also study the effect of these selected policies on
the distribution of recourse cost and targets across populations and their disparities across subpopulations.
2 Related Work
Algorithmic Recourse.Recourse is a post-hoc counterfactual explanation that aims to provide the
lowest-cost modification that changes the prediction for a given input with an undesirable predicted label
under the current model [59, 62]. Since its introduction, different formulations have been used to model the
optimization problem in recourse [6, 10, 18, 28, 29, 30, 41, 46, 50, 54, 61] or study additional aspects such
as fairness [7, 17, 19, 21, 24, 49], repeated dynamics [4, 14, 16], improvement [2, 35, 36], effects of temporal
data [8] and potential harms [15]. See [31, 60] for surveys.
Wachteretal. [62]and Pawelczyketal. [46]focusonscore-basedclassifiers, generatingfeaturemodifications
that help individuals attain a target score. In contrast, Ustun et al.[59] addresses binary classifiers and
requires that recourse actions lead to a change in the predicted label. Conceptually, the score-based formulation
can be viewed as a relaxation of the label-based setting. We also adopt a score-based formulation in our work
subject to a recourse budget. Our main point of departure from all these works is that we optimize recourse
at the population level by simultaneously considering the effect of recourse on all individuals.
Robust Recourse.Although most prior work assumes a static setting, several recent works have focused
on robustness under uncertainty about the data or the classifier. Upadhyay et al.[58] and Nguyen et al.[45]
propose recourse mechanisms that remain effective under model shift induced by distributional shift. Guo
et al.[20] introduces a robust training procedure that jointly trains the classifier and a recourse model under
data shifts. Similar to algorithmic recourse, many different variations and formulations of robust recourse
have also been proposed (see, e.g., [11, 13, 32, 37, 39, 44, 57, 63] and [27] for a survey). Our setting considers
a different source of recourse invalidation: recommendations change the applicant population and thereby the
capacity-constrained acceptance threshold, even though the scoring function remainsfixed.
Recourse Over Time with Limited Resources.Several works studied the temporal dynamics of recourse
by analyzing how recourse recommendations change over time in settings where individuals repeatedly interact
with a decision-making system under resource constraints [1, 16, 40, 56]. Segal et al.[53] modeled limited
resources using a 0/1 knapsack formulation. Ceccon et al.[9] formulated the long-term effects of recourse and
resource limitations as a partially observable MDP. Conceptually, the closest related work models collective
recourse through penalties for population congestion [14] or through capacitated matching between applicants
and providers [33]. Direct comparison to these works is difficult due to different modeling choices.
Performative Prediction.Perdomo et al. [47] introduced performative prediction, where predictions
affect behavior; the data distribution can shift in response, making it hard to train a model that performs
well after a distribution shift. They show that standard empirical risk minimization may fail when the model
deployment changes the data generation process. They distinguish between two key notions: performative
2

optimality, where a model minimizes empirical loss on the distribution it induces, and performative stability,
where the selected model matches the model induced by the deployment. They provided algorithms to
compute performatively stable points and sufficient conditions for their existence. They also show that
performatively optimal points are in a close neighborhood of performatively stable points. These algorithms
were later extended to compute performatively optimal solutions under specific assumptions on the input
distributions [25, 26]. Building on this, Mendler-Dünner et al.[43] propose methods to anticipate performative
shifts by learning to predict from predictions, offering stability-aware model selection strategies [34, 48].
Through a causality lens, König et al.[36] study sufficient conditions under which recourse remains valid after
performativity. See [22] for a survey. Our objective shares the performative perspective of evaluating a policy
under the distribution it induces, though our models do not satisfy the strong convexity and smoothness
assumptions that are commonly used in the performative prediction literature.
3 Problem Formulation
Let X ⊆Rd be the instance space representing individuals. LetD be anunknownpopulation distribution. An
unknown ground-truth functionf ∗ : X →[0, 1]determines the qualification of individuals. The decision-maker
can learn a proxy forf ∗ by performing empirical risk minimization using a parameterized hypothesis class
F={f w :X →[0,1]|w∈ W ⊆Rn}:
w0 ∈arg min
w∈W
Ex∼D

ℓerm

fw(x), f∗(x)  ,(1)
whereℓ erm is a convex loss function. Throughout, we refer tofw0 as thescoring function.
Individuals compete for a resource that can be allocated to anα∈ (0, 1)fraction of the population.
Assume the initial score distribution is continuous. The decision-maker determines the initial allocation by
selecting the highest-scoringαfraction, with threshold
t0 = inf{t∈[0,1] :P x∼D[fw0 (x)≥t]≤α}(2)
and the decision rule
ˆy0(x) =I[f w0 (x)≥t 0].(3)
Let X − = {x : ˆy0(x) = 0} and X + = {x : ˆy0(x) = 1} denote the initially rejected and accepted individuals,
respectively. Algorithmic recourse recommends feature modifications intended to improve an individual’s
outcome [59, 62]. Let c : X × X →R+ denote a cost function for feature modification that satisfyc(x, x) = 0,
and letB≥0be a common recourse budget. 1
Unlike most prior work that provides recourse at an individual level, we focus on recourse at the population
level. In apopulation-level recourse policy, the decision-maker not only provides a target score for each
individual to achieve but also recommends whether this recommendation should be implemented or not.
More formally, the population-level recourse policy consists of two measurable functions:
q:X →[t 0,1], ρ:X → {0,1}.(4)
The targetq(x)specifies which score an individual should attain;ρ(x) = 1means that recourse is recommended
(to be implemented), andρ(x) = 0means the recourse is not recommended.2
Forx∈X − whose target is feasible within budget, define thebest responseas
br(x;q)∈arg min
x′∈X
c(x, x′)
s.t.f w0 (x′)≥q(x), c(x, x′)≤B.(5)
1Individual-specific budgets can be accommodated in the same way.
2We assume every recommended response is implemented.
3

We assume a minimizer exists whenever the constraints are feasible. For infeasible targets and initially
accepted applicants, we setbr(x; q) = x and require ρ(x) = 0. In particular, initially rejected applicants who
cannot reach the initial target oft0 within budget always receive no recommendation. Among the remaining
rejected applicants, the decision-maker choosesρ(x), subject to recommending only feasible targets.
The pair(q, ρ)induces therecourse mapr
r(x) =
(
br(x;q),ifρ(x) = 1,
x,ifρ(x) = 0. (6)
Thus br(x; q)is the candidate response to the target, whereasr(x)is the individual’s resulting feature vector
post-recourse.
The recourse policy can impose the following situations:
1. A common target: q(x) = qc for all x∈X −, with ρ(x) = 1exactly for rejected applicants who can
reach the targetqc. Only the scalarqc ∈[t 0,1]is optimized.
2. Personalized targets without selection:q is optimized andρ(x) = 1for any rejected applicant who can
reach their corresponding targetq(x).
3.Personalized targets with selection:bothqandρare optimized as functions of applicant features.
In particular, setting q(x) = t0 and recommending recourse to every feasible rejected applicant recovers
minimum-cost recourse to the original threshold as studied in prior work [16].
Implementing recourse will change the distribution of individuals. LetDr denote the distribution of
r(x)for x∼D . We assume the (post-recourse) qualification can still be assessed through the ground truth
functionf ∗ as formally stated below.
Assumption 1 The qualification functionf ∗ is invariant to population composition. Recourse may change
f ∗(x)tof ∗(r(x)), but does not change the relationship between resulting features and qualification.
Given that the distribution of individuals can change after recourse, the decision-maker should update its
threshold to satisfy the capacity constraint:
t1(r) = inf{t∈[0,1] :P x′∼Dr [fw0 (x′)≤t]≥1−α}.(7)
Note that since we assumedf ∗ is unchanged, the decision-maker still utilizesfw0 to set the acceptance
threshold.
Recourse can create positive probability mass at a target score. When the cutoff thresholdt1(r)has
positive mass, define
βr = α−P x′∼Dr [fw0 (x′)> t1(r)] Px′∼Dr [fw0 (x′) =t 1(r)] ,(8)
as the fraction of individuals with scoret1(r)that can be selected without violating the capacity constraint.
Otherwise set βr = 0. For a uniform random variableU∼Unif [0, 1], independent of the applicant and drawn
after recourse, the future allocation rule is
ˆyr 1(x′;U) =I[f w0 (x′)> t1(r)] +I[f w0 (x′) =t 1(r)]I[U≤β r].(9)
This rule gives the population acceptance probabilityα, after randomization at the thresholdt1(r).
For the recourse mapr induced by( q, ρ), define post-shift validityV and expected costC over all initially
rejected individuals as
V(q, ρ) =Px∼D, U

ˆyr 1(r(x);U) = 1

 x∈X − ,(10)
C(q, ρ) =Ex∼D

c(x, r(x))

 x∈X − .(11)
4

These definitions include individuals receiving no recommendation and costs incurred by those whose recourse
does not lead to acceptance. LetP be the chosen family of measurable pairs(q, ρ). For a fixedλ >0, the
decision-maker aims to optimize the following objective:
(q∗, ρ∗)∈arg min
(q,ρ)∈P
{C(q, ρ)−λV(q, ρ)}.(12)
The parameter λ weights validity relative to cost; it does not impose a prescribed minimum validity. We
can study the trade-off between validity and cost by varyingλ and solving the optimization problem in
Equation (12) for eachλ.
4 Our Algorithm
Optimizing Equation(12) is difficult because recommendations change the competitive threshold, and both
acceptance and the binary recommendation decisionρ are discontinuous. Our main algorithmic idea is to use
smooth surrogates forqandρ, smooth the acceptance threshold, and apply the Implicit Function Theorem
(IFT) to differentiate through the resulting competitive threshold.
As is common, we assume a sampleS = {x1, . . . , xN } of size N drawn independently fromD and optimize
empirical averages instead of expectations. Throughout this section, we assume the scoring modelfw0 is
learned beforehand using the empirical counterpart of Equation(1) on a labeled sample. That supervised
formulation assumes qualification labelsf ∗(x)are available for score training. We discuss how we learn this
function from data in more detail in Section 5. The recourse sampleS requires only features. The modelfw0
and initial thresholdt0 remain fixed during recourse optimization.
Let k = ⌊αN⌋ and use this threshold to select the acceptance threshold offw0 such that onlyk individuals
are selected byfw0. Let S− denote the rejected individuals. We assume|S−|> 0and1 ≤k < N. For each
rejected applicant, we precompute
¯q(x) = max
x′∈X:c(x,x ′)≤B fw0 (x′),(13)
assuming the maximum is attained. In words,¯q(x)is the highest score achievable by individualx under fw0
within budget B. We refer to an individualx as eligible ifx∈X − and ¯q(x) ≥t 0, i.e., a rejected individual
who can at least reach the initial threshold.
Let σ(z) = (1 + e−z)−1 denote the sigmoid function. We estimateq and ρ using smooth surrogates of the
form
bqθ1 (x) =t 0 + (¯q(x)−t0)σ

gθ1 (x)

,(14)
and
bρθ2 (x) =σ

hθ2 (x)

(15)
for eligible applicants. The functionsgθ1 and hθ2 are twice continuously differentiable in their respective
parameters on neighborhoods ofΘ1 ⊆R m1 andΘ 2 ⊆R m2. We assume each parameter set is nonempty,
compact, and convex.
The estimate bqθ1 is feasible by construction and can be used to compute the best responsebr(x; bqθ1 )using
Equation (5). For ineligible applicants, including initially accepted individuals, we setbqθ1 (x) = t0, bρθ2 (x) = 0,
andbr(x;bqθ1 ) =x.
We use bρto form a differentiable relaxation of recommendation decisions. Letτ >0be a temperature
parameter. During training, we mix the smoothed acceptance outcomes of no action and the complete best
response, with respective weights1−bρθ2 (x)andbρ θ2 (x), defined formally as:
a(t, θ1, θ2) = (1−bρθ2 (x))σ
 fw0 (x)−t
τ

+bρθ2 (x)σ
 fw0 (br(x;bqθ1 ))−t
τ

.(17)
Thus, a averages outcomes rather than feature changes. It should be treated as an approximation that our
algorithm uses in training, not the acceptance probability of the final binary policy we are aiming to compute.
5

ALGORITHM 1:Recourse under Competition
Input: Sample S of individuals; fixed modelfw0; budget B; selection rateα; initial thresholdt0; parametric
functionsgandh; weightλ >0; temperatureτ >0; learning rateη >0; iterationsT.
Output: Selected target functionqand binary recommendation functionρ.
1:Randomly initializeθ (1) ℓ ∈Θ ℓ forℓ∈ {1,2}.
2:Letk=⌊αN⌋and computeS −.
3:Precompute¯qusing Equation (13) and determine eligibility.
4:forj= 1, . . . , Tdo
5:For each eligiblex i ∈S, evaluatebqθ(j) 1 (xi)andbρ θ(j) 2 (xi)using Equations (14) and (15).
6:For each eligiblex i ∈S, compute the best response using Equation (5).
7:Forma i(t, θ(j) 1 , θ(j) 2 )for alli= 1, . . . , Nusing Equation (17).
8:Solve Equation (18) by bisection to obtain ˆt.
9:Compute the full gradients of Equation (19) at the current iterate, differentiating through the best responses
and using the IFT-based threshold derivative in Equation (20).
10:Update both parameter vectors by a gradient step with learning rateλ:
θ(j+1) ℓ = ΠΘℓ

θ(j) ℓ −η∇ θℓ bJ(θ (j) 1 , θ(j) 2 )  , ℓ∈ {1,2},(16)
whereΠ Θℓ denotes Euclidean projection.
11:end for
12:Setq(x) =bq θ(T) 1 (x)andρ(x) =I[bρ θ(T) 2 (x)≥1/2],
13:returnqandρ.
The temperature parameterτ controls how sharply training approximates the acceptance threshold. For small
τ, acceptance changes sharply near the thresholdt. This resembles the actual decision rule, but gradients
become concentrated around the threshold. For largeτ, acceptance changes gradually over a wider score
range. This provides broader gradient signals but is a less accurate approximation of hard acceptance.
Define ˆt= ˆt(θ1, θ2)as the unique real solution of
NX
i=1
ai(ˆt, θ1, θ2) =k.(18)
Note that the sum includes all applicants because initially accepted individuals continue to compete for the
resource.
Using the quantities we defined so far, we obtain the following smooth empirical approximation of
Equation (12):
bJ(θ 1, θ2) = 1 |S−| X
i∈S−
h
bρθ2 (xi)c

xi,br(x i;bqθ1 )

−λa i(ˆt, θ1, θ2)
i
,(19)
whereλ >0is fixed as in the formulation.
Before stating our algorithm, we make the following response regularity assumption.
Assumption 2 For every xi ∈S , the maps θ1 7→f w0 (br(xi; bqθ1 ))and θ1 7→c (xi,br (xi; bqθ1 ))are twice
continuously differentiable on a neighborhood ofΘ1.
Algorithm 1 alternates between computing targets and best responses, recalibrating the competitive
threshold, and updating both parameter vectors. Updatingθ1 changes targets and best responses; updatingθ2
changes recommendation weights through Equations(14) and (15). Neither output is updated independently
for each applicant. Under Assumption 2, the left-hand side of Equation(18) is continuously differentiable
and has a strictly negative derivative with respect tot. Therefore, the IFT ensures thatˆt is differentiable in
6

the policy parameters and gives
∇θℓ ˆt=−
PN
i=1 ∂θℓ ai(ˆt, θ1, θ2) PN
i=1 ∂tai(ˆt, θ1, θ2) , ℓ∈ {1,2}.(20)
Here ∂θℓ holds the threshold fixed. The denominator is strictly negative. Full gradients of Equation(19)
include differentiation through the best responses and this threshold dependence. After T rounds, the
algorithm uses the learned weightsθ(T) 1 to form the estimate forbq. The learned weightθ(T) 2 form estimates
forbρwhich will get converted to binary decisions by thresholding.
5 Experiments
In this section, we empirically evaluate our algorithm on synthetic and real datasets. We describe our datasets
in Section 5.1, our implementation details in Section 5.2, and our findings in Section 5.3. Our code is available
here.
5.1 Datasets
The experiments use four real datasets (Adult, German Credit, ACSIncome, and Give Me Some Credit) and
two synthetic populations. All real datasets are publicly available, and our code provides details on where
the dataset is downloaded from. Adult and ACSIncome predict whether income exceeds $50,000; ACSIncome
uses the 2018 California sample [12]. German Credit classifies credit risk, and Give Me Some Credit predicts
serious delinquency within two years. Favorable labels correspond to high income, good credit, and no serious
delinquency, respectively. We generate two synthetic populations. Each synthetic population contains6,000
three-dimensional Gaussian observations with pairwise correlation0.5and a known nonlinear qualification
function. Synthetic Nonlinear uses a sinusoidal interaction in the logit, while Synthetic Curved uses a concave
quadratic logit.
Preprocessing replaces missing numerical values with the corresponding feature median and missing
categorical values with their most frequent category. Numerical features are standardized to zero mean
and unit variance, and categorical features are one-hot encoded. Synthetic features retain their generated
scale. For each dataset, we divide the features into two sets: mutable features and immutable features.
Immutable features remain inputs to the scoring function and recourse policy, but their encoded coordinates
cannot change during recourse generation. For the synthetic dataset, we designated the first coordinate to be
immutable in both populations. Table 1 provides a summary of datasets and the number of features before
and after preprocessing.
Dataset Size Raw features Processed features
Adult 48,842 14 104
German Credit 1,000 20 61
Give Me Some Credit 150,000 10 10
ACSIncome 195,665 10 666
Synthetic Nonlinear 6,000 3 3
Synthetic Curved 6,000 3 3
Table 1: Summary of dataset statistics.
5.2 Implementation Details
The data is split into30%for model fitting,30%for policy training,20%for validation, and20%for testing.
Model fitting learnsfw0, policy training runs Algorithm 1, validation selects policy checkpoints and baseline
7

candidates (as we will describe shortly), and testing evaluates the generalizability of selected policies on
unseen samples. These are held-out splits, not cross-validation; the experimental parameter grids are specified
separately below. We repeat this process 5 times using seeds{42, 43, 44, 45, 46} with matched data and policy
We report average values and error bars (when applicable) in all experiments.
For the synthetic datasets, the ground-truth qualification scores are generated by our simulator and hence
are known. For real datasets, we learn the qualification scores from the binary-labeled dataset and treat these
learned scores as ground-truth. The learned proxy is trained on the observed binary outcomes using binary
cross-entropy: a tanh network with two hidden layers (of size(32, 16)) and a sigmoid activation function for
the output. We train the proxy using the Adam optimizer, early stopping on an internal10%holdout of the
model-fitting partition, and at most1,500epochs.
We learn two scoring rulesfw0 from the generated ground-truth labels: one is an affine logit and the
other one is a quadratic logit. Both scoring functions use soft-label binary cross-entropy andℓ2 regularization
with a regularizerλ = 10−2, excluding the intercept. They are fitted by L-BFGS-B. Affine coefficients and
intercept are restricted to be in[−5, 5]and quadratic coefficients (for the quadratic logic) are restricted to
be in[10 −4, 3]. For real datasets, the mean AUC is approximately0.87for ACSIncome,0 .91-0.92for Adult,
0.69-0.70for Give Me Some Credit, and0.60for German Credit, with modest differences between scoring
families.
We use Euclidean distance (L2-norm) as the cost functionc when computing recourse. Immutable features
cannot change during recourse generation. The policy uses separate affine sigmoid surrogatesθ1 and θ2
for targets qθ1 and recommendations ρθ2, where θ1, θ2 ∈R d+1 and include an intercept. The non-intercept
parameters are initialized independently fromN (0, 0.022). The target and recommendation intercepts are
initialized to−1and0, respectively. Both parameter vectors are projected onto Euclidean balls of radius3.
Under the implementation’s continuous relaxation of mutable coordinates, computing the highest achievable
score ¯qin Equation(13) and the minimum-cost responsebr in Equation(5) is equivalent to a convex program
when written using the score function’s logit. We use closed-form solutions for the affine logit and scalar
multiplier bisection for the quadratic logit. Derivatives of these responses with respect to the target are
obtained analytically or by implicit differentiation of the KKT equations, allowing policy gradients to pass
through the best response.
When running Algorithm 1, we set the number projected full-gradient updates toT = 500. The competitive
threshold ¯t in Equation(18) is recomputed using80bisection steps at every update, and its implicit derivative
is included. The smooth recommendation weight mixes the outcomes of no action and the complete response,
rather than interpolating features. A singleτ smooths acceptance in both the objective and capacity equation.
Unless varied in an experiment, the default parameter settings are as follows:
Parameter Default Range of values tested
λ30 14values in[0.3,30]
B0.75{0.25,0.75,1.5}
α0.4{0.2,0.4,0.6}
τ0.01{0.005,0.01,0.02,0.05}
η0.2{0.05,0.2}
T500—
Table 2: Default parameter setting.
In addition to Algorithm 1, we use the following baselines:
1.No recourse:where no individual changes features.
2. Original threshold:where every eligible individual is provided with recourse to achieve the initial
target of t0. This tests the reliability of initial-target recommendations under renewed competition, as
motivated by prior recourse-over-time studies [16].
8

3. Common target:where we perform a grid search to find a common target in[t0, 1], for all individuals
that achieves the lowest validation objective. The recourse would be recommended to every rejected
individual who can attain that common target within the feasible budget ofB.
4. Personalized targets without selection:where we run Algorithm 1 to learnθ1, while fixingρ = 1for
every eligible rejected individual.
Cost and validity are averaged over allN− initially rejected individuals in S−, as in Equations(11)
and (10). Validity is their mean acceptance probability, using expected acceptance under uniform cutoff
tie-breaking. Therefore, the upper bound on validity ismin{1, k/N−}. However, this bound need not be
attainable under the recourse budget and policy restrictions. At the population level, when the initially
rejected fraction is1−α, the corresponding bound becomesmin{1, α/(1−α)}.
(a) ASCIncome dataset, affine model,λ= 3.
(b) ASCIncome dataset, affine model,λ= 30.
Figure 1: Convergence results for the ASCIncome dataset with an affine scoring model. Each subfigure
corresponds to a differentλ value as stated in the caption. Each curve corresponds to a different learning
rate as indicated in the legend.
5.3 Findings
Convergence.Inourfirstexperiment, westudytheconvergenceofAlgorithm1. Usingthedefaultparameter
settings, two valuesλ∈ {3, 30}, and two step sizesη∈ {0.05, 0.2}, we run the algorithm forT = 500iterations.
9

We track the smooth empirical training objective and the best-so-far squared projected-gradient mapping,
averaged across five seeds.
The results are presented in Figure 1 for the ACSIncome dataset with an affine scoring model asfw0. Each
subfigure corresponds to a differentλ value. The left panel shows the training objective, evaluated on the
policy-training cohort, and the right panel shows the best-so-far squared projected-gradient mapping, both as
functions of the number of iterations for both of the learning rates. Both quantities decrease substantially,
with η = 0.2producing faster progress thanη = 0.05in these plots. The objective stabilizes earlier forλ = 30,
although the stationarity measure continues to improve. Because changingλ changes the objective itself, this
observation does not establish a general improvement in convergence rate. Moreover, the best-so-far measure
is non-increasing by construction, but its reduction indicates that training finds iterates closer to stationarity.
The speed of improvement varies across datasets and scoring functions. Additional results for other dataset
and model pairs are provided in Appendix A.1.
(a) German Credit dataset, quadratic model.
 (b) Synthetic Non-linear dataset, quadratic model.
Figure 2: The trade-off between recourse cost and post-shift validity. Each subfigure corresponds to a different
dataset and scoring model as indicated by the caption. In each subfigure, each curve corresponds to the
Pareto frontier of the trade-off between cost and validity for Algorithm 1 and the baselines. Dominated points
remain visible as faint markers.
The Trade-Off Between Cost and Validity.We next study the trade-off between recourse cost and
post-shift validity for our algorithm and baselines. Across all datasets, we varyλ over 14 values between0.3
and30, while keeping the other parameters at their default values.
The results are summarized in Figure 2. Each subfigure corresponds to a dataset and scoring model. Cost
and validity are computed over all initially rejected applicants in each test cohort and then averaged across
five seeds. For each method, the connected points show the nondominated cost-validity combinations for each
of the evaluated policies.
We observe that no action incurs zero cost but can have nonzero measured validity. This is because the
initial threshold t0 is estimated from a reference population, whereas allocation is recomputed for each test
cohort. But as expected, the validity achieved by no action is close to 0. Providing recourse with the original
threshold incurs positive cost without significantly improving aggregate validity over the no-action baseline.
This illustrates the limitation of recommending recourse to the original threshold in competitive settings, an
observation that has also been pointed out by prior work [16].
Commontargetsofferfavorabletrade-offsatlowtomoderatevaliditylevels, andsomeobservedpersonalized-
policy points are dominated by common-target points. Personalized targets, with or without selection,
nevertheless achieve the highest observed validity, albeit at higher cost. This is despite the observation that
personalized targets achieve the lowest objective values in training (and often in testing), indicating greater
validity does not necessarily imply a lower objective value, perhaps due to overfitting.
10

Follow-up target diagnostics help explain these differences. Atλ = 3, personalized policies with selection
assign higher targets than the common-target policy to approximately80%-100%of applicants receiving
recommendations under both methods, depending on the dataset and scoring function. Their mean recourse
cost ranges from0.695to0 .745, close to the budgetB = 0.75, compared with0.507-0.576for common targets.
Selection reduces expenditure on unsuccessful actions relative to implementing the same learned targets for
every eligible applicant, indicating that the learned target levels and recipient selection both contribute to
the observed trade-offs.
Analogous to the results in the robust recourse literature [37, 45, 46, 58], our results show that achieving
high validity under competition also imposes a significant increase in the cost of implementing the recourse.
Additional results for other dataset and model pairs are provided in Appendix A.2, where many of our
observations continue to hold.
Effect of Parameters.To better understand the effect of each of the parameters in our setting, we
conducted sensitivity analysis on the choice of parameters through three different experiments: (1) In budget
sensitivity experiments, we varied budget from 0.25 to 1.75 for 3 choices ofλ∈ {3, 10, 30} while keeping the
other parameters at their default values. (2) In admission rate sensitivity experiments, we variedα from 0.2
to 0.6 for the same three values ofλ and other default parameters. (3) In temperature sensitivity experiments,
we selected τ values ranging from 0.005 to 0.005 for the same three values ofλ and other default parameters.
Figure 3: The effect of budgetB on cost and validity of recourse in the ACSIncome dataset for quadratic
cost atλ= 10. Curves correspond to different approaches.
Increasing the budget generally improves post-shift validity, but also increases the cost. For example, on
ACSIncome with a quadratic scoring function andλ = 10, as depicted in Figure 3, increasing the budgetB
from0 .25to1 .5raises Algorithm 1’s mean validity from9.6%to51 .4%and its mean cost from0.05to1 .11.
However, additional expenditure does not necessarily provide much advantage: at the budgetB = 1.5, the
common-target baseline achieves approximately the same validity at a mean cost of0.61. Larger budgets,
therefore, expand the opportunities for successful recourse, but, by themselves, do not ensure efficient use of
those opportunities.
Increasing the admission rate consistently raises Algorithm 1’s mean validity across all tested datasets,
models, and λ combinations. For Synthetic Curved with a quadratic scoring function andλ = 30, as depicted
in Figure 4, increasingα from0 .2to0 .6raises validity from7 .1%to26 .3%, while increasing the mean cost
11

Figure 4: The effect of admission rateα on cost and validity of recourse in the Synthetic Curved dataset for
quadratic cost atλ= 30. Curves correspond to different approaches.
Figure 5: The effect of temperatureτ on the recourse objective in the Synthetic Curved dataset for quadratic
cost atλ= 30. Curves correspond to different approaches.
from0 .10to0 .32. In general, greater capacity increases the average recourse expenditure as the eligible
population, and selected recommendations will also change with the budget increase.
Performance is relatively stable across the tested temperatures for many dataset and model pairs, but
excessive smoothing sometimes can substantially worsen the achieved recourse objective in Equation(12). On
Give Me Some Credit with a quadratic scoring function, as depicted in Figure 5, increasing the temperatureτ
from0 .01to0 .05worsens Algorithm 1’s objective value from−8.62to −6.28by reducing both mean validity
and cost. However, the results are nearly identical for smallerτ values. These findings support our approach
of selecting the temperature through validation, as the effect depends on the dataset and scoring function.
12

Target Distributions.We next examine how common and personalized targets affect the score improve-
ments and costs required of recourse recipients. We useλ∈ {1, 3, 10} and default values for all the other
parameters.
Figure 6 shows results for the ACSIncome dataset with an affine scoring model andλ = 3. The left panel
shows recommended scores q(x), the middle panel shows required score increasesq(x) −f w0 (x), and the
right panel shows the minimum cost of attaining the recommended target. The curves give the cumulative
fraction of recipient observations whose value is at most the horizontal-axis value. The middle and right
panels distinguish improvement in score from effort measured by the recourse cost to achieve the improved
score.
Figure 6: Target distributions for the ACSIncome dataset with an affine scoring model andλ = 3. The panels
show the cumulative density function of the recommended targets (left), required score increases (middle),
and recourse costs (right) among recipients for seed42. Vertical dashed lines in the left panel indicate the
original threshold and common target.
The left panel of Figure 6 shows that both personalized policies assign very similar targets, and the
fraction of individuals receiving each target score is almost uniform. The middle panel shows that even a
common target requires different score increases because recipients have different initial scores. Furthermore,
personalized policies generally require larger score increases than the common targets. The right panel
shows that personalization does not necessarily reduce effort. The median recipient cost is approximately
0.589for the common target,0 .747for personalized targets without selection, and0.731for personalized
targets with selection. Thus, many personalized recommendations require expenditure close to the maximum
allowable budget ofB = 0.75. Further analysis, comparing the personalized policy with common-target policy,
indicates that the personalized policy with selection assigns higher targets than the common-target policy to
approximately94%of their shared recipient, with a mean additional cost of0.147.
The Role of Selection.To isolate the effect of recipient selection, we take a learned personalized policy,
retain its target functionq, and replace its recommendation rule withρ(x) = 1for every eligible rejected
applicant. Previously selected applicants retain their recommended actions, while previously unselected
eligible applicants now implement their minimum-cost responses to the learned targets. We recompute
the competitive threshold and measure cost, validity, and the objective value. In this experiment, we use
λ∈ {1,3,10}and default values for all the other parameters.
Figure 7 illustrates this comparison for the Synthetic Curved dataset with a quadratic scoring function.
The three panels plot outcomes againstλ. The left panel reports mean recourse cost (including expenditure
on unsuccessful recourse). The middle panel reports post-shift validity. The right panel reports the objective
value as in Equation(12). At λ = 3, disabling selection increases mean cost from approximately0.148to0 .223
(left panel), while validity increases only from0.139to0 .144(middle panel). Consequently, the objective
worsens from approximately−0.268to −0.210(right panel). Further analysis shows that expenditure on
unsuccessful recourse increases from0.050to0 .121per initially rejected applicant. Thus, selection can avoid
substantial expenditure for a small reduction in aggregate validity.
13

Figure 7: Effect of modifying the recipient selection for the Synthetic Curved dataset with a quadratic scoring
model. The panels report mean cost (left), post-shift validity (middle), and recourse objective (right) for
λ∈ {1,3,10}.
Figure 8: Group outcomes partitioned by gender for the Adult dataset with an affine scoring model and
λ = 3. The panels report recommendation rates among eligible rejected applicants (left), post-shift validity
gains relative to no action (middle), and mean cost per initially rejected applicant (right). Points show means
across the seeds with95%confidence intervals.
Group Outcomes.We also examine how recourse benefits and costs are distributed across subpopulations.
In this experiment, we use λ∈ {1, 3, 10} and default values for all the other parameters. To form the
subpopulations, we used gender or race for real datasets. For synthetic datasets, we use diagnostic groups
defined by the sign of the immutable first coordinate.
Figure 8 shows outcomes by gender for the Adult dataset with an affine scoring model andλ = 3. The
left panel reports recommendation rates among eligible rejected applicants. The middle panel reports validity
gains relative to no action. The right panel reports mean cost over initially rejected members of each group.
For personalized targets with selection, the mean recommendation rate is approximately83.9%among eligible
male applicants and66.7%among eligible female applicants. Validity gains are approximately23.1%and
11.4%, respectively, while mean costs are0.276and0.161.
These results reveal differences in both access to recommendations and realized benefits. The lower mean
cost for female applicants does not imply that their recommended actions are individually cheaper: cost per
initially rejected applicant also reflects how many applicants receive recommendations. The comparisons show
that optimizing aggregate cost and validity does not ensure equal group outcomes. This is not surprising as
equity is not included in the optimization objective [59].
14

Figure 9: Partial adoption for the German Credit dataset with an affine scoring model andλ = 30. The
policy selected under full adoption is held fixed while the adoption probability varies, and the competitive
allocation is recomputed after each realization.
Partial Adoption.We examine how incomplete adoption affects policies designed under the assumption
that every recommendation is implemented. We keep the policy selected under full adoption fixed and let
each recommended applicant independently implement their response with probabilityp where p belongs to
the set {0, 0.25, 0.5, 0.75, 1}. Non-adopters retain their original features, and we recompute the competitive
allocation after each realization. We measure cost and validity over all initially rejected applicants.
Figure 9 presents results for the German Credit dataset with an affine scoring model,λ = 30, and the
remaining parameters at their default values. At50%adoption, mean cost is approximately0.246and validity
is20 .9%, compared with0.493and31 .2%under full adoption. Thus, half adoption retains approximately
two-thirds of full-adoption validity at half the cost. Although expected expenditure scales proportionally
with adoption when recommendations remain fixed, validity need not. This is because fewer implemented
actions also change the competition faced by adopters.
Further analysis across all12datasets and scoring function combinations shows that, atλ = 30, average
validity increases as more applicants implement their recommendations. Full adoption achieves the lowest
average objective value: although more applicants incur recourse costs, the increase in validity outweighs this
additional expenditure at the chosen value ofλ. Therefore, partial adoption can preserve some of the benefits
of recourse, while reducing both expenditure and overall validity.
6 Discussion and Limitations
In this work, we introduced a framework for algorithmic recourse under competition that explicitly anticipates
the effects of population-wide feature modifications. We studied population-wide recourse computation
policies and how these policies can affect the validity and cost of recourse.
We discuss some of the limitations of our setting and flesh out new directions for future work. First, our
analysis assumes that achieved scores and recourse costs depend smoothly on the policy parameters. Even in
such settings, our approach does not guarantee optimality. Understanding under what conditions optimal
strategies can be designed for the smooth setting is a natural next step. Handling nonsmooth response
changes and analyzing the performance in such settings likely requires different optimization techniques and
analysis. Second, our formulation models a single round of recourse in which (in almost all our experiments)
individuals fully implement the recourse. Extending the framework to a repeated setting where individuals
repeatedly go through the decision-making process, adoption of recourse is selective and asynchronous remains
15

an important direction. Finally, improvements in aggregate cost and validity do not mean these benefits are
distributed equitably across all individuals and subpopulations. Understanding what it means for a recourse
policy to be equitable in a competitive setting and providing equitable recourse policies for such settings is
left for future work (see the Ethical Consideration section).
Ethical Consideration.Our framework assumes that the decision-maker’s goal is to help initially re-
jected individuals by balancing their aggregate recourse cost and post-shift validity. Although we model
individual costs and competitive outcomes, we do not assess the broader consequences of these decisions
for individuals and subpopulations. Selecting recipients may distribute acceptance opportunities unequally
across subpopulations, unsuccessful recourse may impose unrewarded effort, and initially accepted individuals
may lose access to the resource due to future competition. Since our objective does not incorporate equity
into considerations, improvements in aggregate cost and validity should not be interpreted as guarantees of
individual/subpopulation benefit or societal welfare. Future work should carefully analyze these aspects.
Acknowledgments.We thank Kshitij Kayastha for discussions during the early stages of this work.
Usage of LLMs.Gemini 3.1 Pro was used to write the initial version of the experiments from the problem
formulation and algorithm. GPT-6 Astra was used to verify the correctness of implementation. We then
checked the edited code by Astra. GPT-6 Astra was used to proofread the paper and provide edits, especially
in the implementation details of the experiments. LLMs were not used for problem formulation, formation of
research questions, algorithmic solutions, and the description of related work.
References
[1] Patrick Altmeyer, Giovan Angela, Aleksander Buszydlik, Karol Dobiczek, Arie van Deursen, and Cynthia
Liem. Endogenous macrodynamics in algorithmic recourse. In1st Conference on Secure and Trustworthy
Machine Learning, pages 418–431, 2023.
[2] Srikanth Avasarala, Varun Gupta, Shahin Jabbari, Saber Salehkaleybar, and Juba Ziani. The role of
causality in algorithmic recourse.CoRR, abs/2607.28497, 2026.
[3] Solon Barocas, Moritz Hardt, and Arvind Narayanan.Fairness and Machine Learning: Limitations and
Opportunities. fairmlbook.org, 2019.
[4] Andrew Bell, João Fonseca, Carlo Abrate, Francesco Bonchi, and Julia Stoyanovich. Fairness in
algorithmic recourse through the lens of substantive equality of opportunity.CoRR, abs/2401.16088,
2024.
[5] Richard Berk, Hoda Heidari, Shahin Jabbari, Michael Kearns, and Aaron Roth. Fairness in criminal
justice risk assessments: The state of the art.Sociological Methods & Research, 50(1):3–44, 2021.
[6] Tom Bewley, Salim Amoukou, Saumitra Mishra, Daniele Magazzeni, and Manuela Veloso. Counterfactual
metarules for local and global recourse. In41st International Conference on Machine Learning, 2024.
[7] Kate Boxer and Daniel Neill. Realizing the promises of algorithmic recourse through reliability, accessi-
bility, and fairness principles. In5th ACM Conference on Equity and Access in Algorithms, Mechanisms,
and Optimization, pages 218–240, 2025.
[8] Andrei Buliga, Chiara Di Francescomarino, Chiara Ghidini, Marco Montali, and Massimiliano Ronzani.
Generating counterfactual explanations under temporal constraints. In39th Annual AAAI Conference
on Artificial Intelligence, pages 15622–15631, 2025.
[9] Marina Ceccon, Alessandro Fabris, Goran Radanovic, Asia J. Biega, and Gian Antonio Susto. Reinforce-
ment learning for durable algorithmic recourse.CoRR, abs/2509.22102, 2025.
16

[10] Yatong Chen, Andrew Estornell, Yevgeniy Vorobeychik, and Yang Liu. To give or not to give? the
impacts of strategically withheld recourse. In28th International Conference on Artificial Intelligence
and Statistics, volume 258, pages 739–747, 2025.
[11] Seung Hyun Cheon, Anneke Wernerfelt, Sorelle Friedler, and Berk Ustun. Feature responsiveness scores:
Model-agnostic explanations for recourse. In13th International Conference on Learning Representations,
2025.
[12] Frances Ding, Moritz Hardt, John Miller, and Ludwig Schmidt. Retiring adult: New datasets for fair
machine learning. InAdvances in Neural Information Processing Systems 34, pages 6478–6490, 2021.
[13] Sanghamitra Dutta, Jason Long, Saumitra Mishra, Cecilia Tilli, and Daniele Magazzeni. Robust
counterfactual explanations for tree-based ensembles. In39th International Conference on Machine
Learning, volume 162, pages 5742–5756, 2022.
[14] Ahmad-Reza Ehyaei, Ali Shirali, and Samira Samadi. Collective counterfactual explanations: Balancing
individual goals and collective dynamics. InAdvances in Neural Information Processing Systems 38,
2025.
[15] Hidde Fokkema, Damien Garreau, and Tim van Erven. The risks of recourse in binary classification. In
27th International Conference on Artificial Intelligence and Statistics, pages 550–558, 2024.
[16] João Fonseca, Andrew Bell, Carlo Abrate, Francesco Bonchi, and Julia Stoyanovich. Setting the
right expectations: Algorithmic recourse over time. In3rd ACM Conference on Equity and Access in
Algorithms, Mechanisms, and Optimization, pages 29:1–29:11, 2023.
[17] Ruijiang Gao and Himabindu Lakkaraju. On the impact of algorithmic recourse on social segregation.
In40th International Conference on Machine Learning, pages 10727–10743, 2023.
[18] Prateek Garg, Lokesh Nagalapatti, and Sunita Sarawagi. From search to sampling: Generative models
for robust algorithmic recourse. In13th International Conference on Learning Representations, 2025.
[19] OzgurGuldogan, YuchenZeng, Jy-yongSohn, RamtinPedarsani, andKangwookLee. Equalimprovability:
A new fairness notion considering the long-term impact. In11th International Conference on Learning
Representations, 2023.
[20] Hangzhi Guo, Feiran Jia, Jinghui Chen, Anna Squicciarini, and Amulya Yadav. RoCourseNet: Robust
training of a prediction aware recourse model. In32nd ACM International Conference on Information
and Knowledge Management, pages 619–628, 2023.
[21] Vivek Gupta, Pegah Nokhiz, Chitradeep Roy, and Suresh Venkatasubramanian. Equalizing recourse
across groups.CoRR, abs/1909.03166, 2019.
[22] Moritz Hardt and Celestine Mendler-Dünner. Performative prediction: Past and future.CoRR,
abs/2310.16608, 2023.
[23] Moritz Hardt, Eric Price, and Nathan Srebro. Equality of opportunity in supervised learning. In30th
Annual Conference on Neural Information Processing Systems, pages 3315–3323, 2016.
[24] Hoda Heidari, Vedant Nanda, and Krishna Gummadi. On the long-term impact of algorithmic decision
policies: Effort unfairness and feature segregation through social learning. In36th International
Conference on Machine Learning, pages 2692–2701, 2019.
[25] Zachary Izzo, Lexing Ying, and James Zou. How to learn when data reacts to your model: Performative
gradient descent. In38th International Conference on Machine Learning, pages 4641–4650, 2021.
[26] Zachary Izzo, James Zou, and Lexing Ying. How to learn when data gradually reacts to your model. In
25th International Conference on Artificial Intelligence and Statistics, pages 3998–4035, 2022.
17

[27] Junqi Jiang, Francesco Leofante, Antonio Rago, and Francesca Toni. Robust counterfactual explanations
in machine learning: A survey. In33rd International Joint Conference on Artificial Intelligence, pages
8086–8094, 2024.
[28] Kentaro Kanamori, Takuya Takagi, Ken Kobayashi, and Yuichi Ike. Learning decision trees and forests
with algorithmic recourse. In41st International Conference on Machine Learning, 2024.
[29] Amir-Hossein Karimi, Gilles Barthe, Borja Balle, and Isabel Valera. Model-agnostic counterfactual
explanations for consequential decisions. In23rd International Conference on Artificial Intelligence and
Statistics, pages 895–905, 2020.
[30] Amir-Hossein Karimi, Bodo Julius von Kügelgen, Bernhard Schölkopf, and Isabel Valera. Algorithmic
recourse under imperfect causal knowledge: a probabilistic approach. InAdvances in Neural Information
Processing Systems 33, 2020.
[31] Amir-Hossein Karimi, Gilles Barthe, Bernhard Schölkopf, and Isabel Valera. A survey of algorithmic
recourse: Contrastive explanations and consequential recommendations.ACM Comput. Surv., 55(5):
95:1–95:29, 2023.
[32] Kshitij Kayastha, Vasilis Gkatzelis, and Shahin Jabbari. Learning-augmented robust algorithmic recourse.
Transactions on Machine Learning Research, 2026.
[33] Zahra Khotanlou, Kate Larson, and Amir-Hossein Karimi. Your recourse, my loss? algorithmic recourse
under shared constraints. In9th ACM Conference on Fairness, Accountability, and Transparency, pages
3717–3737, 2026.
[34] Michael Kim and Juan Perdomo. Making decisions under outcome performativity. In14th Innovations
in Theoretical Computer Science Conference, pages 79:1–79:15, 2023.
[35] Gunnar König, Timo Freiesleben, and Moritz Grosse-Wentrup. Improvement-focused causal recourse
(ICR). In37th AAAI Conference on Artificial Intelligence, pages 11847–11855, 2023.
[36] Gunnar König, Hidde Fokkema, Timo Freiesleben, Celestine Mendler-Dünner, and Ulrike von Luxburg.
Performative validity of recourse explanations.CoRR, abs/2506.15366, 2025.
[37] Phone Kyaw, Kshitij Kayastha, and Shahin Jabbari. Optimal robust recourse with lp-bounded model
change. In4th IEEE Conference on Secure and Trustworthy Machine Learning, pages 303–325, 2026.
[38] Himabindu Lakkaraju, Stephen Bach, and Jure Leskovec. Interpretable decision sets: A joint framework
for description and prediction. In22nd ACM SIGKDD International Conference on Knowledge Discovery
and Data Mining, pages 1675–1684, 2016.
[39] Francesco Leofante and Nico Potyka. Promoting counterfactual robustness through diversity. In38th
AAAI Conference on Artificial Intelligence, pages 21322–21330, 2024.
[40] Bo-Yi Liu, Zhi-Xuan Liu, Kuan Lun Chen, Shih-Yu Tsai, Jie Gao, and Hao-Tsung Yang. Understanding
endogenous data drift in adaptive models with recourse-seeking users. In8th AAAI/ACM Conference
on AI, Ethics, and Society, 2025.
[41] Arnaud Van Looveren and Janis Klaise. Interpretable counterfactual explanations guided by prototypes.
InMachine Learning and Knowledge Discovery in Databases, pages 650–665, 2021.
[42] Scott Lundberg and Su-In Lee. A unified approach to interpreting model predictions. InAdvances in
Neural Information Processing Systems 30, pages 4765–4774, 2017.
[43] Celestine Mendler-Dünner, Frances Ding, and Yixin Wang. Anticipating performativity by predicting
from predictions. InAdvances in Neural Information Processing Systems 35, 2022.
18

[44] Duy Nguyen, Ngoc Bui, and Viet Anh Nguyen. Distributionally robust recourse action. In11th
International Conference on Learning Representations, 2023.
[45] Tuan-Duy Nguyen, Ngoc Bui, Duy Nguyen, Man-Chung Sue, and Viet Anh Nguyen. Robust bayesian
recourse. In38th Conference on Uncertainty in Artificial Intelligence, pages 1498–1508, 2022.
[46] Martin Pawelczyk, Teresa Datta, Johannes van den Heuvel, Gjergji Kasneci, and Himabindu Lakkaraju.
Probabilistically robust recourse: Navigating the trade-offs between costs and robustness in algorithmic
recourse. In11th International Conference on Learning Representations, 2023.
[47] Juan Perdomo, Tijana Zrnic, Celestine Mendler-Dünner, and Moritz Hardt. Performative prediction. In
37th International Conference on Machine Learning, pages 7599–7609, 2020.
[48] Juan Perdomo, Tolani Britton, Moritz Hardt, and Rediet Abebe. Difficult lessons on social prediction
from wisconsin public schools. In8th ACM Conference on Fairness, Accountability, and Transparency,
2025.
[49] Nicholas Perello, Cyrus Cousins, Yair Zick, and Przemyslaw A. Grabowicz. Discrimination induced by
algorithmic recourse objectives. In8th ACM Conference on Fairness, Accountability, and Transparency,
pages 1653–1663, 2025.
[50] Kaivalya Rawal and Himabindu Lakkaraju. Beyond individualized recourse: Interpretable and interactive
summaries of actionable recourses. InAdvances in Neural Information Processing Systems 33, 2020.
[51] Marco Túlio Ribeiro, Sameer Singh, and Carlos Guestrin. “Why should I trust you?": Explaining the
predictions of any classifier. In22nd ACM SIGKDD International Conference on Knowledge Discovery
and Data Mining, pages 1135–1144, 2016.
[52] Cynthia Rudin. Stop explaining black box machine learning models for high stakes decisions and use
interpretable models instead.Nat. Mach. Intell., 1(5):206–215, 2019.
[53] Meirav Segal, Anne-Marie George, Ingrid Chieh Yu, and Christos Dimitrakakis. Better luck next time:
About robust recourse in binary allocation problems. In2nd World Conference on Explainable Artificial
Intelligence, pages 374–394, 2024.
[54] Dylan Slack, Anna Hilgard, Himabindu Lakkaraju, and Sameer Singh. Counterfactual explanations can
be manipulated. InAdvances in Neural Information Processing Systems 34, pages 62–75, 2021.
[55] Daniel Smilkov, Nikhil Thorat, Been Kim, Fernanda Viégas, and Martin Wattenberg. Smoothgrad:
removing noise by adding noise.CoRR, abs/1706.03825, 2017.
[56] Giovanni De Toni, Stefano Teso, Bruno Lepri, and Andrea Passerini. Time can invalidate algorithmic
recourse.CoRR, abs/2410.08007, 2024.
[57] Bohdan Turbal, Iryna Voitsitska, and Lesia Semenova. ElliCE: Efficient and provably robust algorithmic
recourse via the Rashomon sets. InAdvances in Neural Information Processing Systems 38, 2025.
[58] Sohini Upadhyay, Shalmali Joshi, and Himabindu Lakkaraju. Towards robust and reliable algorithmic
recourse. InAdvances in Neural Information Processing Systems 34, pages 16926–16937, 2021.
[59] Berk Ustun, Alexander Spangher, and Yang Liu. Actionable recourse in linear classification. In3rd
AMC Conference on Fairness, Accountability, and Transparency, pages 10–19, 2019.
[60] Sahil Verma, John Dickerson, and Keegan Hines. Counterfactual explanations for machine learning: A
review.CoRR, abs/2010.10596, 2020.
[61] Sahil Verma, Keegan Hines, and John Dickerson. Amortized generation of sequential algorithmic recourses
for black-box models. In36th AAAI Conference on Artificial Intelligence, pages 8512–8519, 2022.
19

[62] Sandra Wachter, Brent Mittelstadt, and Chris Russell. Counterfactual explanations without opening the
black box: automated decisions and the GDPR.Harvard Journal of Law and Technology, 31(2):841–887,
2018.
[63] Jayanth Yetukuri, Ian Hardy, Yevgeniy Vorobeychik, Berk Ustun, and Yang Liu. Providing fair recourse
over plausible groups. In38th AAAI Conference on Artificial Intelligence, pages 21753–21760, 2024.
[64] Muhammad Zafar, Isabel Valera, Manuel Gomez-Rodriguez, and Krishna P. Gummadi. Fairness
constraints: Mechanisms for fair classification. In20th International Conference on Artificial Intelligence
and Statistics, pages 962–970, 2017.
A Additional Experimental Results
A.1 Convergence
(a) ASCIncome dataset, quadratic model,λ= 3.
 (b) ASCIncome dataset, quadratic model,λ= 30.
Figure 10: Convergence results for the ASCIncome dataset with a quadratic scoring model. Each subfigure
corresponds to a differentλ value as stated in the caption. Each curve corresponds to a different learning
rate as indicated in the legend.
(a) ASCIncome dataset, quadratic model,λ= 3.
 (b) ASCIncome dataset, quadratic model,λ= 30.
Figure 11: Convergence results for the Adult dataset with a quadratic scoring model. Each subfigure
corresponds to a differentλ value as stated in the caption. Each curve corresponds to a different learning
rate as indicated in the legend.
A.2 The Trade-Off Between Cost and Validity
20

(a) Adult dataset, affine model.
 (b) Adult dataset, quadratic model.
(c) German Credit dataset, affine model.
 (d) Synthetic non-linear dataset, affine model.
Figure 12: The trade-off between validity of recourse and its cost. Each subfigure corresponds to a different
dataset and scoring model as indicated by the caption. In each subfigure, each curve corresponds to the
Pareto frontier of the trade-off between cost and validity for Algorithm 1 and the baselines.
21
