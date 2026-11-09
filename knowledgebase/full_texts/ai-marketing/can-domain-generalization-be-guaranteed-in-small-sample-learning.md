---
title: Can Domain Generalization be Guaranteed in Small-Sample Learning?
url: https://arxiv.org/abs/2609.39512
category: ai-marketing
subcategory: measurement
date: 2026-09
venue: ''
authors:
- Hong Zheng
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.39512
pages: 17
chars: 37632
fetched_at: '2026-11-08T13:25:09+00:00'
kb_version: 1
---

# Can Domain Generalization be Guaranteed in Small-Sample Learning?

Can Domain Generalization be Guaranteed in Small-Sample
Learning?
Hong Zheng ∗ zhinhom@icloud.com
Abstract
The small-sample learning problem remains a fundamental challenge in machine learning
because limited training data lead to unstable model estimation and generalization. Struc-
tural Risk Minimization (SRM) has long been regarded as a principled solution under the
classical i.i.d. assumption. However, domain generalization (DG) violates this assumption,
leaving the theoretical role of SRM in DG largely unexplored. To bridge this gap, we
establish the first theoretical guarantees for SRM in DG under mild assumptions. Specif-
ically, based on the concept of stability, we derive learning consistency and generalization
error bounds and prove that these bounds become tight when the hypotheses satisfy the
stability condition. Building upon this, under a specific hypothesis space assumption, we
establish stability, learning, and generalization bounds for SRM. We further discuss the ap-
plicability of these bounds to deep learning. This work establishes theoretical foundations
for SRM under distribution shifts and sheds light on the design of robust DG algorithms
in small-sample scenarios.
Keywords:Stability, Domain Generalization, Generalization Bound, Regularization
1 Introduction
Domain generalization (DG) aims to train machine learning (ML) models using several
available data domains, ensuring that they perform well on related but inaccessible (unseen)
domains (Muandet et al., 2013). This is meaningful because it uses finite sets to develop
methods applicable to infinite sets, which can be regarded as a foundation for developing
artificial general intelligence. Recently, several studies have explored invariance (Arjovsky
et al., 2019; Ahuja et al., 2020) and causality (Christiansen et al., 2021; Wang et al., 2023)
from input data pairs, assuming they are essential for generalization, while developing learn-
ing approaches based on empirical risk minimization (ERM). By (Vapnik, 2013), the success
of ERM and its variants relies on the assumption of sufficient data, i.e., large-sample learn-
ing. However, in real-world applications, such an assumption may not always be satisfied,
particularly in scenarios where data collection is expensive. In other words, we have to face
the small-sample learning problem (a term introduced by Vapnik) in many learning sce-
narios. Under such scenarios, model estimation and generalization become unstable (Wang
et al., 2024).
How can this challenge be addressed? Is it through data augmentation, data gener-
ation using large models, or Structural Risk Minimization (SRM)? Data augmentation,
whether applied online or offline, violates data independence assumptions and cannot in-
crease the amount of independent samples. Although it may improve empirical perfor-
mance, model estimation remains theoretically unstable. Moreover, its effectiveness relies
∗. This work was completed during my Ph.D. period and was the result of a flash of inspiration. I decided
to submit it to arXiv and leave its value to the readers.
1
arXiv:2609.39512v2  [cs.LG]  5 Oct 2026

heavily on practitioners’ experience rather than a principled learning paradigm (Pereira
et al., 2022). Recent work (Shumailov et al., 2024) proves that using generated data can
lead to model collapse. Specifically, learning from AI-derived texts causes models to for-
get rare information as outputs become increasingly homogeneous. Moreover, AI-generated
images reproduce training-data semantics and appearances, indicating compromised data
independence. Then, SRM becomes an applicable method, as it at least preserves the data
independence assumption. However, in DG, data are not identically distributed, leaving
the theoretical role of SRM unclear.
In this work, we establish theoretical guarantees (Theorem 7) for SRM under DG sce-
narios with mild assumptions, thereby bridging this gap. First, based on the concept of
hypothesis stability, we derive learning consistency and generalization error bounds and
prove that the tightness of these bounds is determined by the stability of the hypothe-
sis. By assuming a reproducing kernel Hilbert space, we then establish stability, learning,
and generalization bounds for SRM. Furthermore, we extend our theoretical results to deep
learning by introducing corresponding regularizations for SRM and analyzing their stability,
learning consistency, and generalization error. In conclusion, we contribute by theoretically
proving that DG can be guaranteed in small-sample learning. Through this, we reveal that,
when data samples are limited, a sufficiently large SRM regularization parameter is re-
quired to obtain tighter stability bounds for hypotheses, thereby achieving tighter learning
and generalization bounds.
2 Theoretical Results
2.1 Preliminaries
We here introduce some notation and related concepts that will be used to derive our
methods. ConsideringX ⊂RandY ⊂Rbeing respectively an input and output space, we
have a training set
D={Z 1 = (X, Y)1, . . . , ZE = (X, Y)E}
of sizeEinZ=X × Ydrawn from unknown distributions inP. Assume that eachZ∈D
containsNdata pairs (x j, yj), i.e., (X, Y) :={(x j, yj)}N j=1. Under domain generalization
(DG), (X, Y)i∼i.i.d.Pi for alli∈[E], andP i ̸=P i′ for alli̸=i ′ ∈[E]. Thus, the overall
samples follow an independent non-identically distributed (i.n.d.) assumption. The training
setDis typically regarded as the source set, while the testing setD t is regarded as the
target set. Similarly,P i ̸=P t for alli∈[E] and allt∈[E t], whereE t denotes the number
of target domains inD t. Furthermore, no information fromD t is available during training.
Given a source setDof domain sizeE, for eachi= 1, . . . , E, we construct a modified
dataset by replacing thev-th domain ofDas follows:
Dv ={Z 1, . . . , Zv−1, Z′ v, Zv+1 . . . , ZE},
where the replacementZ ′ v is assumed to be drawn fromPand to satisfy the above distri-
bution assumption. Here,Z ′ v also denotes a group ofNsample pairs, rather than a single
sample pair, which differs from the setting in (Bousquet and Elisseeff, 2002). OnlyDpar-
ticipates in the learning process, whereasD v is excluded from learning and is used solely
for stability validation.
2

We consider a hypothesish∈ H:X → Yas a deterministic mapping for prediction.
Then, we assume that all mappings are measurable and all sets are countable, which does
not restrict the generality of the results presented hereafter. To measure the accuracy of
predictions fromh, we consider the cost functionc:Y × Y →R, and the loss ofhwith
respect to data pairsZ= (X, Y) is then defined as
ℓ(h, Z) =ℓ(h,(X, Y)) =c(h(X), Y).
Correspondingly, given any setD, the expected risk ofhis defined by
R(h, D) =1 E EX i=1 EZ∼Pi[ℓ(h, Z)] = 1 E EX i=1 EZi[ℓ(h, Zi)],
and the empirical risk ofhis defined by
ˆR(h, D) = 1 EN EX i=1 NX j=1 ℓ(h,(x j, yj)i).
Given the setD v, we consider only the empirical risk ˆR(h, Dv). In the following, we will
also use the simplified notations ˆR(h)≡ ˆR(h, D),R(h)≡R(h, D), and ˆR′(h)≡ ˆR(h, Dv)
when the dataset is clear from the context.
Note thatR(h) is typically defined asR(h) =E P∈P E EZ∈P [ℓ(h, Z)], wherePE denotes
the set of source distributions. SinceP E containsEobserved domains in DG, the outer
expectation reduces to the empirical average over domains, i.e.,E P∈P E [·] =E −1 PE i=1[·].
2.2 Stability and Bounds
We begin by establishing the basic definition of hypothesis stability under DG scenarios.
This is important for achieving our goal: we aim to obtain bounds on the learning consis-
tency and generalization error of hypotheses learned by SRM, and we want these bounds
to be tight when the hypotheses satisfy the stability condition.
Definition 1 (Error Stability)Any hypothesish∈ Hhas error stabilityβwith respect
to the loss functionℓif the following holds,∀D∈ Z E,∀v∈[E],
1
EN

 X Z∈D ℓ(h, Z)− X Z′∈Dv ℓ(h, Z′)

 ≤β,
which can also be written

 ˆR(h)− ˆR′(h)

 ≤β.(1)
Remarks. (a) Strictly, we should writeZ E×N instead ofZ E. For simplicity, we useZ E
hereafter. (b) The above stability measures the absolute difference between the empirical
risks of the same hypothesishon two datasets,DandD v. This notion differs from the
stability definitions in (Bousquet and Elisseeff, 2002), where stability is typically defined in
terms of the expected risks of different hypotheses.
Clearly, a smallβindicates that the hypothesis exhibits good stability. Based on this
definition, we establish the following exponential decay bound, which is derived from a
classical concentration inequality.
3

Theorem 2For any measurable functionR:H × Z E →R, any hypothesish∈ Hthat
satisfies the stability in Definition 1, i.e.,hhasβ-stability, and anyε >0, the following
inequality holds,∀D∈ Z E,
PD
h
ˆR(h)−R(h)≥ε
i
≤exp
 −2EN ε2
β2

.(2)
ProofConsider ˆR(h, D) with respect to any hypothesish. Sincehhasβerror stability,
the following holds,∀D∈ Z E,∀v∈[E],

 ˆR(h, D)− ˆR(h, Dv)

 ≤β.
This satisfies the condition of Lemma 8, i.e.,
sup
D∈Z E ,Z′v∈Z

 ˆR(h, D)− ˆR(h, Dv)

 ≤β,∀v∈[E].
This implies thatc v =β,∀v∈[E], i.e.,
X
v
X
i
c2 v =EN β2,
andε:=EN ε, completing the proof.
Remarks. (a) With probability at least 1−δ, it holds thatϵ S(h)≤β
p
ln(1/δ)/2EN,
whereϵ S(h) :=R(h)− ˆR(h). (b) As expected, a more restrictive stability criterion yields
a correspondingly tighter bound. This bound is a McDiarmid-type bound, which is more
flexible and capable of estimating nonlinear statistics (Li and Liu, 2024). When no further
information is available, the convergence rate of this bound cannot be improved. There-
fore, there is no need to derive a lower bound to establish its optimality. (c) This bound
establishes the learning consistency between the expected risk and the empirical risk.
Based on the above learning consistency bound, we observe that stability plays a critical
role in learning performance, as the tightness of the bound is closely related to the stability
of hypotheses. Namely, a smallerβleads to a tighter bound onϵ S(h). We see that
√
Eis
scaled byβ, which implies that for a fixedE, the magnitude ofβdominates the tightness,
highlighting the necessity of achieving a smallβ.
We then turn our attention to generalization and introduce the following expected risk
ofhon the target domains,
RT (h)≡R(h, D t) = 1 Et EtX t=1 EZ∼Pt[ℓ(h, Z)].
This target riskR T (h) is also defined as average expected loss of hypothesishoverE t target
domains. Accordingly, we establish the following generalization bound.
Theorem 3 (Generalization Bound)LetR T (h)denote the above definition of the ex-
pected risk of anyh∈ Hon the target domains, wherehhasβ-stability. Assume that
0≤ℓ≤M. Then, the following inequality holds with probability at least1−δ,
ϵT (h)≤β
r
ln(1/δ)
2EN +Cρ,(3)
4

where,ϵ T (h) :=R T (h)− ˆR(h),C= (2 √ 2M)/EE t, andρ= P t P i dJS (Pt, Pi). Here,
dJS (P, Q) =
p
J S(P||Q), whereJ S(·||·)denotes the Jensen-Shannon (JS) divergence.
ProofAccording to Lemma 9, for anyP i andQ j, we have

EPi[ℓ]−E Qj [ℓ]

 ≤2 √ 2M dJS (Pi, Qj).
Then, extending this inequality to all source and target domains, we obtain

 1 Et EtX t EPt[ℓ]− 1 E EX i EPi[ℓ]

 ≤C EtX t EX i dJS (Pt, Pi),
whereC= (2
√
2M)/EE t. Letρ= P t P i dJS (Pt, Pi). By the inequality|a| − |b| ≤ |a−b|,
we have
RT (h)−R(h)≤Cρ.
Then, the proof is completed by applying Theorem 2.
Remarks. (a) The tightness of this generalization bound is still linked to the stability of
h. Specifically, givenρ, a smallβlead to a tighter generalization bound. (b) This term
ρcaptures a central challenge in DG, namely that the generalization bound is affected
by the distribution discrepancy between the source and target domains. Unfortunately,
there is nothing we can do about this term, as access toD t is unavailable during learning.
(c)d JS (·,·) is a metric that satisfies symmetry and the triangle inequality. When the JS
divergence is defined using the natural logarithm, 0≤d JS (·,·)≤
√
ln 2.
Similarly, the above generalization bound demonstrates the critical role ofβin gener-
alization. This is IMPORTANT because the stability ofhdetermines both learning and
generalization. Onceβis obtained, we derive the corresponding learning and generalization
bounds. Moreover, sincehis arbitrary, the hypothesis obtained by SRM also satisfies the
above bounds onϵ S(h) andϵ T (h). We then conduct further investigations.
The following two definitions are introduced as useful tools for our derivation: one is
theσ-admissibility ofℓ, and the other is optimal stability (β ∗).
Definition 4A loss functionℓdefined onH × Yisσ-admissible with respect toHis
the associated cost functioncis convex and the following condition holds,∀h, h ′ ∈ H,
∀(X, Y)∈ Z,

ℓ(h,(X, Y))−ℓ(h ′,(X, Y))

 ≤σ

h(X)−h ′(X)

 .
Remarks. Theσ-admissibility essentially implies thatℓisσ-Lipschitz continuous. This
establishes a relationship between the loss difference of two hypotheses and the distance
between the corresponding hypotheses.
Definition 5 (β ∗-stability)Considering the functionalf(h) =| ˆR(h)− ˆR′(h)|, leth ∗ ∈
arg minh∈H f(h)andh ∗ is non-zero. We say thath ∗ achieves the minimum error stability
β∗, i.e.,

 ˆR(h∗)− ˆR′(h∗)

 ≤β ∗.
5

Remarks. (a) Note thath ∗ is the minimizer of the functionalf(h), rather than of ˆR(h) or
ˆR′(h), and thath ∗ is not necessarily unique. (b) This non-uniqueness implies the existence
of multiple hypotheses that satisfy this stability condition.
We define ∆h=|h(X)−h ∗(X)|,∀h∈ H,∀X∈ X. Then, we have

 ˆR(h)− ˆR′(h)

 ≤σ(∆h D + ∆hDv ) +β ∗.(4)
Here, ∆hD and ∆hDv are defined respectively as|h(X)−h ∗(X)| D and|h(X)−h ∗(X)| Dv ,
where the subscriptsDandD v denote the sets over which the values ofXare taken.
ProofWe omit the hat notation in ˆRfor convenience, i.e.,Rdenotes ˆR. Since, we have
h∗ ∈arg min h∈H |R(h)−R ′(h)|. Then, for anyh∈ H, we have

R(h)−R ′(h)

 =

R(h) +R(h ∗)−R(h ∗) +R ′(h∗)−R ′(h∗) +R ′(h)

≤ |R(h)−R(h∗)|+

R′(h)−R ′(h∗)

 +

R(h∗)−R ′(h∗)

≤ |R(h)−R(h∗)|+

R′(h)−R ′(h∗)

 +β ∗
≤σ|h(X)−h ∗(X)| D +σ|h(X)−h ∗(X)| Dv +β ∗
The first inequality holds by the triangle inequality, the second holds under the definition
that|R(h ∗)−R ′(h∗)| ≤β ∗, and the last holds due to theσ-admissibility of the loss
functions.
The Structural Risk Minimization (SRM) framework for DG is subsequently formulated
as ˆRr(h)≡ ˆRr(h, D, λ), where
ˆRr(h, D, λ) =ˆR(h, D) +λN(h) = 1 EN EX i=1 ℓ(h, Zi) +λN(h).
Here,λis a penalty factor, andN(h) represents any regularization forh. When using the
datasetD v, we obtain ˆR′ r(h)≡ ˆR′ r(h, Dv, λ).
Before presenting the main results, we establish the following result with respect to the
regularizerN(·).
Theorem 6Letℓbeσ-admissible with respect toH, letNbe a functional defined onH,
and leth ∗ hasβ ∗-stability. Assuming that∇ ˆR(h∗)≥0, for anyt∈[0,1], anyh∈ H,
ˆRr(h∗), and ˆR′ r(h∗), we have
N(h ∗)− N(h∗ +t∆h)≤ σt 2λEN (∆hD + ∆hDv ).(5)
ProofWe omit the hat notation in ˆRfor convenience, i.e.,Rdenotes ˆR. Sinceh ∗ ∈
arg minh∈H |R(h)−R ′(h)|, for anyh∈ H, we have

R(h∗)−R ′(h∗)

 ≤

R(h∗ +t∆h)−R ′(h∗ +t∆h)

 .
Here, (h∗ +t∆h)(X)̸=h ∗(X) for anyt >0. Then, we have
(R(h∗)−R ′(h∗))2 ≤(R(h ∗ +t∆h)−R ′(h∗ +t∆h)) 2.
6

Let Φ(h) =|R(h)−R ′(h)|, we have 0∈ ∇Φ(h∗), which implies that∃g∈ ∇R(h∗)∩∇R ′(h∗).
Note that here 0 andgbelong to the hypothesis class rather than being scalars.
Now, letϕ(t) =R(h ∗ +t∆h) andϕ ′(t) =R ′(h∗ +t∆h). Then, we have
∇tϕ(t) =∇R(h ∗ +t∆h)∆h,
∇tϕ′(t) =∇R ′(h∗ +t∆h)∆h.
Considerφ(t) =ϕ(t)ϕ ′(t), we have
∇tφ(t) =∇R(h ∗ +t∆h)∆hϕ ′(t) +∇R ′(h∗ +t∆h)∆hϕ(t),
∇tφ(0) =∇R(h ∗)∆hϕ′(0) +∇R ′(h∗)∆hϕ(0).
SinceRis convex (see Definition 4), its gradient is a monotone mapping, so we have∇R(h ∗+
t∆h)≥ ∇R(h∗) for anyt≥0. Moreover, we assume that∇R(h ∗)≥0. Then, we obtain
∇tφ(t)≥ ∇tφ(0). This implies that
R(h∗ +t∆h)R ′(h∗ +t∆h)≥R(h ∗)R′(h∗).
Then, we compute
(R(h∗ +t∆h) +R ′(h∗ +t∆h)) 2 −(R(h ∗) +R ′(h∗))2
=(R2 ∆ + 2R∆R′∆ + (R′∆)2)−(R 2 + 2RR′ + (R′)2)
=(R2 ∆ + 2R∆R′∆ + (R′∆)2 −2R ∆R′∆ + 2R∆R′∆)
−(R 2 + 2RR′ + (R′)2 −2RR ′ + 2RR′)
=((R∆ −R ′∆)2 + 4R∆R′∆)−((R−R ′)2 + 4RR′)
=((R∆ −R ′∆)2 −(R−R ′)2) + 4(R∆R′∆ −RR ′).
Based on the previous derivations, we obtain
(R(h∗) +R ′(h∗))2 ≤(R(h ∗ +t∆h) +R ′(h∗ +t∆h)) 2
R(h∗) +R ′(h∗)≤R(h ∗ +t∆h) +R ′(h∗ +t∆h).
Then, we replaceR(h ∗) andR ′(h∗) withR r(h∗) andR ′ r(h∗), respectively, and obtain
Rr(h∗) +R ′r(h∗)≤R r(h∗ +t∆h) +R ′r(h∗ +t∆h).
Consequently, we have
2λ(N(h ∗)− N(h∗ +t∆h))≤(R(h ∗ +t∆h)−R(h ∗)) + (R′(h∗ +t∆h)−R ′(h∗))
Finally, based on theσ-admissibility of the loss functions and the definition ofR, we obtain
N(h ∗)− N(h∗ +t∆h)≤ σt 2λEN (∆hD + ∆hDv ).
Remarks. (a) This result leads to the regularizations associated with theσ-admissibility
7

of loss functions. (b) Similarly,h ∗ is not the minimizer of either ˆRr(h) or ˆR′ r(h). (c) This
theorem considers only minimizersh ∗ satisfying∇ ˆR(h∗)≥0.
Next, we impose an assumption onHto ensure thatN(·) is well-defined. Specifically, we
consider regularization in a reproducing kernel Hilbert space (RKHS). An RKHS is chosen
to ensure efficient kernel computation and a complete, stable function space. Accordingly,
we define
N(h) =∥h∥ 2 k ,
wherekrefers to the kernel. Typically, we state thatH k denotes the norm in an RKHS,
but for simplicity, we usekhere. Based on the fundamental property (reproducing) of an
RKHSH, we have
∀h∈ H,∀X∈ X, h(X) =⟨h, k(X,·)⟩.
Then, according to Cauchy-Schwarz inequality, we have
∀h∈ H,∀X∈ X,|h(X)| ≤ ∥h∥k
p
k(X, X).(6)
With all the previous preparations, we finally present the following result for our main
goal.
Theorem 7Assume thatHis a reproducing kernel Hilbert space with kernelksuch that
∀X∈ X,
p
k(X, X)≤κ≤ ∞. Letℓbeσ-admissible with respect toH, and assume that
0≤ℓ≤M. Any hypothesishachieved by
min
h∈H
ˆR(h) +λ∥h∥ 2 k ,(7)
has error stabilityβrespect toℓwith
β≤ 2σ2κ2
λEN +β ∗.
Furthermore, with probability al least1−δ, the learning consistency bound holds:
ϵS(h)≤
 2σ2κ2
λEN +β ∗
 r ln(1/δ)
2EN ,
and the generalization bound is given by
ϵT (h)≤
 2σ2κ2
λEN +β ∗
 r ln(1/δ)
2EN +Cρ.
ProofSinceN(h) =∥h∥ 2 k, based on Theorem 6, we have
t∥∆h∥ 2 k ≤ σt 2λEN (∆hD + ∆hDv ).
8

According to the assumption that∀X∈ X,
p
k(X, X)≤κ≤ ∞and Inequality (6), we
have
∆hD ≤ ∥∆h∥k
p
k(X, X)≤ ∥∆h∥kκ,
∆hDv ≤ ∥∆h∥kκ.
Consequently, we obtain
∥∆h∥2 k ≤ σ 2λEN 2∥∆h∥kκ= σ∥∆h∥kκ λEN ,
∥∆h∥k ≤ σκ λEN
Moreover, according to Inequality (4), and by takingβ≤σ(∆h D + ∆hDv ) +β ∗, we have
β≤2σ∥∆h∥ kκ+β ∗.
By Theorem 2 and Theorem 3, we complete the proof.
Remarks. (a) Up to an intercept,βis inversely proportional to the product of the penalty
factor and the total number of data samples. AsλEN→ ∞, the bound onβbecomes tight
whenβ ∗ approaches zero. (b) The tightness of the learning and generalization bounds is
now linked to the number of data samples within each domain. Namely, the main order of
the above bounds isO(1/
√
λE3N 3). (c) Assumingβ ∗ →0, the term involvingβ ∗ in the
above bounds can be regarded as a bias term that is typically negligible.
Now, we have established stability, learning, and generalization bounds for the hypoth-
esishlearned by SRM in DG. By the theorem, for fixedσandκ, the tightness of all the
above bounds is determined by the parametersλ,E, andN. Specifically, a sufficiently large
λENtheoretically leads to a smallerβ, which in turn yields better learning consistency and
generalization performance.
2.3 Application
Still, one step remains before applying our theoretical results to practical applications. In
most deep learning scenarios, the hypothesis space is assumed to be a Euclidean space. In
the previous subsection, we presented the stability, learning, and generalization bounds for
SRM under the assumption of an RKHS. For a kernel-induced RKHS, the function norm in
the RKHS can be transformed into the EuclideanL 2(µ) norm in the corresponding feature
space through finite-dimensional feature representations or kernel feature mappings. This
property provides a theoretical foundation for applying RKHS-based analysis to models
defined in Euclidean spaces. The detailed derivation is omitted for brevity. We then consider
the following SRM framework:
ˆRr(h) = ˆR(h) +λ∥h∥ 2 2,
where the hypothesishis parameterized byθ, i.e.,h=h θ. Correspondingly, the learning
objective is
min
h∈H
ˆR(h) +λ∥h∥ 2 2 .(8)
9

Note that, for simplicity, we directly use the above Lagrangian formulation as the learning
objective instead of the original constrained optimization problem.
We further assume that, for a finite-dimensional RKHS, the induced kernel is normalized,
i.e.,
k(X, X)≤1,∀X∈ X,
which yieldsκ= 1. This assumption is equivalent to bounding the norm of the induced
feature representation and naturally extends to Euclidean-space models, including deep
neural networks, through their learned feature embeddings.
Accordingly, under the above assumption and settings of Theorem 7, any hypothesish
achieved by learning objective (8) has error stabilityβrespect toℓwith
β≤ 2σ2
λEN +β ∗.
Furthermore, with probability al least 1−δ, the learning consistency bound holds:
ϵS(h)≤
 2σ2
λEN +β ∗
 r ln(1/δ)
2EN ,
and the generalization bound is given by
ϵT (h)≤
 2σ2
λEN +β ∗
 r ln(1/δ)
2EN +Cρ.
In the above, we only consider theL 2-norm. However, in SRM, theL 1(µ)-norm is also
commonly considered to promote sparsity. Since there is no direct correspondence between
∥h∥2 k and theL 1-norm, we instead consider the following learning objective to promote
sparsity,
min
h∈H
ˆR(h) + λ E EX i=1 ∥hi∥2 2 .(9)
The above implies thatN(h) = P ∥hi∥, and we still obtain the stability bound
β≤ 2σ2
λEN +β ∗,
which yields the same learning and generalization bounds as those for the learning objec-
tive (8). Here,h i denotes the parameters ofhassociated with domaini.
Although the parameters are identical across all domains during the learning process, the
summation over domains is introduced for the purpose of sparsity regularization. In essence,
∥h∥1 = P |θi|, i.e., the sum of the absolute values of all weights inh. Similarly, P ∥hi∥2 2
can also be viewed as a summation over the parameters ofh, except that each summand
is replaced by∥h i∥2 2, with the summation taken over theEdomains. This formulation
promotes domain-level sparsity, i.e., inter-domain sparsity, while encouraging smoothness
within each domain. Such a consideration is analogous to the ideas underlying LASSO
and Group LASSO; further details are omitted here. Additionally, learning objectives (8)
and (9) are strongly convex. Therefore, under gradient-based optimization methods, the
optimization converges Q-linearly.
10

2.4 Discussion
Stability. We provide a discussion of Definition 1 and the definitions in (Bousquet and
Elisseeff, 2002). The stability in (Bousquet and Elisseeff, 2002) measures the difference
between the expected losses of two modelsh 1 andh 2 trained onDandD v, respectively,
thereby evaluating the sensitivity of the learning algorithm to changes in training data.
In contrast, our stability measures the difference between the empirical risks of the same
hypothesishevaluated onDandD v. It assesses whether the hypothesis is sensitive to
source domain changes. A largerβindicates weaker stability. We consider empirical risk
instead of expected risk since it is directly computable in practice, making our measure
suitable for evaluating model stability in DG.
β∗-stability. We may avoid consideringβ ∗-stability, as well ash ∗. By Lemma 20 in (Bous-
quet and Elisseeff, 2002), some results regardingN(·) associated with the minimizer of SRM
can be established, thereby restricting all subsequent theorems to this minimizer. However,
by definingβ ∗-stability, our theory no longer unnecessarily depends on the restriction to
the SRM minimizer. Therefore, in essence,h ∗ relaxes the restriction that the learning and
generalization bounds must be based on the SRM minimizer, resulting in a milder condi-
tion for DG scenarios. This serves as a significant novelty and distinguishes our work from
theirs.
σandM. One may note that, throughout our main results, we use the notationσto
denote the Lipschitz constant andMto denote the uniform bound of the loss function.
This is because we do not specify the exact loss formulation or the specific task. Here, we
present the following examples for classification and regression tasks, whose derivations rely
on Lemma 3 provided in the supplemental material. IfY ∈ {−1,1}, and considering the
following loss function
ℓ(f,(x, y)) =
(
1−yf(x), if1−yf(x)≥0
0, otherwise ,
we haveσ= 1 andM= 1. IfY ∈ {0, B}and considering the following loss function
ℓ(f,(x, y)) = (f(x)−y) 2,
we haveσ= 2BandM=B. Other examples can be found in (Bousquet and Elisseeff,
2002).
Previous works. Recently, under the assumption of sufficient data samples, many studies
have developed theoretical analyses of learning under distribution shifts. To the best of our
knowledge, our work is the first to investigate small-sample learning in DG from a theoretical
perspective. Therefore, a direct comparison with these works is not meaningful, and we only
provide some related discussions. One well-known work is presented by Ben-David et al.
(2010), which has motivated many subsequent studies on representation learning. Their
work is elegant and introduces a challenge term in the upper bound that is similar to ourρ.
Tong et al. (2023) presented an upper bound for their learning method; however, the con-
nection between the hyperparameters of the learning algorithm and the derived bound was
not established. Zheng and Teng (2026) provides insights into how distribution shift itself
affects learning, but their upper bound relies on a strong assumption regarding distribution
11

divergence. Besides upper bounds, a lower bound for DG was presented by Wang et al.
(2024) to explain the phenomenon observed in (Gulrajani and Lopez-Paz, 2020); however,
it requires an infinite number of data samples in each domain.
Limitations. It should be emphasized that our theoretical bounds for SRM are established
within the RKHS framework. Consequently, the results naturally extend to learning prob-
lems whose hypothesis spaces admit an RKHS formulation, such as deep learning. However,
when the hypothesis space does not admit an RKHS formulation, our theoretical results
may no longer hold.
3 Related Works
We briefly introduce some empirical and theoretical methods in DG. For more details, see
the references.
Empirical Methods: Since IRM (Arjovsky et al., 2019), various extensions, including
IRM-Games (Ahuja et al., 2020), invariant information bottleneck (Li et al., 2022), and
P-IRM (Choraria et al., 2023), have been proposed, along with studies on invariant repre-
sentation learning in latent spaces (Muandet et al., 2013; Li et al., 2018). These methods
assume that invariant features from observed domains improve generalization to Out-of-
distribution domains. However, recent works have challenged this assumption by revealing
failure cases of invariance-based methods (Rosenfeld et al., 2020) and proposing low-risk
alternatives (Wang et al., 2022). Causality-based approaches (Christiansen et al., 2021;
Wang et al., 2023) have also been introduced to address domain shifts but generally require
stronger assumptions. In addition, the sparsity of ML models has also gained increasing
attention recently, such as in (Xu et al., 2024; Galanti et al., 2023; Levy and Abramovich,
2023).
Theoretical Methods: From the VC bounds (Vapnik and Chervonenkis, 2015; Vapnik,
2013) to the Massart-noisy bounds (Massart and N´ ed´ elec, 2006), the mystery of the learning
pattern in machine learning has been revealed gradually. These theories provide fundamen-
tal inequalities for analyzing learning problems and inspire subsequent studies. Ben-David
et al. (2010) provides an early theoretical study of learning under distribution shift, motivat-
ing further investigations in DG. Many efforts have since focused on developing guarantees
for well-generalized ML models, e.g., (Wang et al., 2024; Zheng and Teng, 2026). Our work
contributes to this line of research by addressing learning problems under limited data.
4 Conclusion
In this study, we present theoretical guarantees for SRM in DG scenarios and provide corre-
sponding applications. Our results imply that, even when data samples are limited, stable,
well-performing, and generalizable models can still be learned, i.e., DG can be theoretically
guaranteed in small-sample learning. This finding is important for practical applications of
ML and deep learning methods, as sufficient training samples cannot be collected in every
application field. Moreover, for fields where data collection is highly expensive, our theory
provides an alternative solution. However, we cannot theoretically characterize the selection
ofλ, which serves as a limitation of our work. We expect to address this issue in future
research.
12

Ackonwlegement
I would like to express my sincere gratitude to my supervisors, Prof. T & Prof. L, for
providing me with the time, freedom, and support to pursue my own research interests and
ideas throughout my studies.
Appendix A.
In this appendix, we only provide the lemmas, along with their porous, used to prove our
main theorems.
A.1 Lemmas
Lemma 8 (McDiarmid’s inequality (McDiarmid et al., 1989))LetS:={z 1, . . . , zn}
andS i :={z 1, . . . , zi−1, z′ i, z1+1, . . . , zn}, and letF:Z n →Rbe any measurable function
for which there exist constantsc i (i= 1, . . . , n)such that
sup
S∈Z n,z′ i∈Z

F(S)−F(S i)

 ≤c i
then, for anyε >0,
PS [F(S)−E S[F(S)]≥ε]≤exp
 −2ε2
Pn
i=1 c2 i

.
ProofThis is a classical concentration inequality, and the proof is omitted here. For more
details, please refer to (McDiarmid et al., 1989).
For clarity on how this lemma is applied in our case, we provide the following simple
example. Consider that ˆR(h, D) :H × ZE×N →Rand ˆR(h, Dv). Here,DandD v differ
fromSandS i, respectively. Then, if we have
sup
D∈Z E×N ,Z′v∈Z N

 ˆR(h, D)− ˆR(h, Dv)

 ≤c v,
it follows that
P
h
ˆR(h, D)−R(h, D)≥ε
i
≤exp
(
−2ε2
PE
v=1
PN
i=1 c2v
)
.
Note the difference in the sum ofc 2: in the original lemma,z ′ i represents a single data pair,
whereas in our case,Z ′ v containsNdata pairs. Therefore, we use a double summation
here.
Lemma 9 (Expectation Bound via JS divergence)LetPandQbe two probability
distributions. LetF:Z →Rbe a measurable function satisfying
∥F∥ ∞ := sup Z∈Z |F(Z)| ≤M≤ ∞.
13

Then,
|EP [F]−E Q[F]| ≤2M
p
2J S(P||Q),
or
|EP [F]−E Q[F]| ≤2
√
2M dJS (P, Q).
ProofThe result follows from standard inequalities in information theory. First, by a
standard total variation bound,
|EP [F]−E Q[F]| ≤2∥F∥∞ dT V(P, Q).
Applying the Pinsker’s inequality, we have
 1
2 dT V(P, Q)
2
≤ 1 2 KL(P||M)
 1
2 dT V(P, Q)
2
≤ 1 2 KL(Q||M).
Here,M= (P+Q)/2,d T V(P, M) = (1/2)dT V(P, Q), anddT V(Q, M) = (1/2)dT V(P, Q).
Then, by the definition of the JS divergence, i.e.,J S(P;Q) = 1/2KL(P;M) +
1/2KL(Q;M), we obtain
2
 1
2 dT V(P, Q)
2
≤ 1 2 J S(P||Q).
Here, we clarify how this lemma can be used to derive some results in our paper. Let
Z= (h(X), Y) and considerℓasF. Then, assuming∥ℓ∥ ∞ ≤M, we have
EZ∼P [|ℓ(Z)|]−E Z∼Q[|ℓ(Z)|]≤2M
q
2J S(P(h(X),Y) ||Q(h(X),Y) ),
≤2M
q
2J S(P(X,Y) ||Q(X,Y) ),
considering|a| − |b| ≤ |a−b|. The last inequality is a consequence of the Data Processing
Inequality from information theory. Note thathis the same for bothPandQ. If this
condition does not hold, the last inequality will not hold either.
Lemma 10Lethbe the hypothesis obtained by SRM whereℓis a loss function associated
with a convex cost functionc(·,·). We denote byB(·)a positive non-decreasing real-valued
function such that for ally∈ Y. Then, we have
∀y′ ∈ Y, c(y, y′)≤B(y).
Moreover,ℓisσ-admissible whereσcan be taken as
σ= sup
y′∈Y
sup
|y|≤B(y)

 ∂c ∂y (y, y′)

 .
14

ProofThe proof can be found in (Bousquet and Elisseeff, 2002), on page 515, referring to
the proof of Lemma 23. Note that this lemma differs slightly from the original one, but the
proof is identical.
In the original lemma, the authors derived the following bound for the loss function:
∀z∈ Z,0≤ℓ(A s, Z)≤B

κ
r
B(0)
λ
!
.
Here,A s denotes the optimal hypothesis returned by the SRM algorithm. Consequently,
the upper bound is established specifically.
In our work, the hypothesishlearned by SRM is not necessarily the minimizer, and
the assumption 0≤c(h(X), Y)≤Mis inherited from Theorem 3. Therefore, we do not
strictly follow the original lemmas; instead, we adopt only the parts that are relevant to
our analysis.
Specifically, the above result follows directly from the consideration ofσ-admissibility.
References
Kartik Ahuja, Karthikeyan Shanmugam, Kush Varshney, and Amit Dhurandhar. Invariant
risk minimization games. InInternational Conference on Machine Learning, pages 145–
155. PMLR, 2020.
Martin Arjovsky, L´ eon Bottou, Ishaan Gulrajani, and David Lopez-Paz. Invariant risk
minimization.arXiv preprint arXiv:1907.02893, 2019.
Shai Ben-David, John Blitzer, Koby Crammer, Alex Kulesza, Fernando Pereira, and Jen-
nifer Wortman Vaughan. A theory of learning from different domains.Machine learning,
79(1):151–175, 2010.
Olivier Bousquet and Andr´ e Elisseeff. Stability and generalization.Journal of machine
learning research, 2(Mar):499–526, 2002.
Moulik Choraria, Ibtihal Ferwana, Ankur Mani, and Lav R. Varshney. Learning optimal
features via partial invariance.Proceedings of the AAAI Conference on Artificial Intelli-
gence, 37(6):7175–7183, Jun. 2023.
Rune Christiansen, Niklas Pfister, Martin Emil Jakobsen, Nicola Gnecco, and Jonas Pe-
ters. A causal framework for distribution generalization.IEEE Transactions on Pattern
Analysis and Machine Intelligence, 44(10):6614–6630, 2021.
Tomer Galanti, Mengjia Xu, Liane Galanti, and Tomaso Poggio. Norm-based generalization
bounds for sparse neural networks.Advances in Neural Information Processing Systems,
36:42482–42501, 2023.
Ishaan Gulrajani and David Lopez-Paz. In search of lost domain generalization, 2020. URL
https://arxiv.org/abs/2007.01434.
15

Tomer Levy and Felix Abramovich. Generalization error bounds for multiclass sparse linear
classifiers.Journal of Machine Learning Research, 24(151):1–35, 2023.
Bo Li, Yifei Shen, Yezhen Wang, Wenzhen Zhu, Dongsheng Li, Kurt Keutzer, and Han
Zhao. Invariant information bottleneck for domain generalization. InProceedings of the
AAAI Conference on Artificial Intelligence, volume 36, pages 7399–7407, 2022.
Shaojie Li and Yong Liu. Concentration inequalities for general functions of heavy-tailed
random variables. InForty-first International Conference on Machine Learning, 2024.
Ya Li, Mingming Gong, Xinmei Tian, Tongliang Liu, and Dacheng Tao. Domain general-
ization via conditional invariant representations. InProceedings of the AAAI conference
on artificial intelligence, volume 32, 2018.
Pascal Massart and ´Elodie N´ ed´ elec. Risk bounds for statistical learning.The Annals of
Statistics, 34(5):2326–2366, 2006.
Colin McDiarmid et al. On the method of bounded differences.Surveys in combinatorics,
141(1):148–188, 1989.
Krikamol Muandet, David Balduzzi, and Bernhard Sch¨ olkopf. Domain generalization via
invariant feature representation. InInternational conference on machine learning, pages
10–18. PMLR, 2013.
Emeson Pereira, Gustavo Carneiro, and Filipe R Cordeiro. A study on the impact of data
augmentation for training convolutional neural networks in the presence of noisy labels.
In2022 35th SIBGRAPI Conference on Graphics, Patterns and Images (SIBGRAPI),
volume 1, pages 25–30. IEEE, 2022.
Elan Rosenfeld, Pradeep Kumar Ravikumar, and Andrej Risteski. The risks of invariant
risk minimization. InInternational Conference on Learning Representations, 2020.
Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Nicolas Papernot, Ross Anderson, and
Yarin Gal. Ai models collapse when trained on recursively generated data.Nature, 631
(8022):755–759, 2024.
Peifeng Tong, Wu Su, He Li, Jialin Ding, Zhan Haoxiang, and Song Xi Chen. Distribution
free domain generalization. In Andreas Krause, Emma Brunskill, Kyunghyun Cho, Bar-
bara Engelhardt, Sivan Sabato, and Jonathan Scarlett, editors,Proceedings of the 40th
International Conference on Machine Learning, volume 202 ofProceedings of Machine
Learning Research, pages 34369–34378. PMLR, 23–29 Jul 2023.
Vladimir Vapnik.The nature of statistical learning theory. Springer science & business
media, 2013.
Vladimir N Vapnik and A Ya Chervonenkis. On the uniform convergence of relative fre-
quencies of events to their probabilities. InMeasures of complexity: festschrift for alexey
chervonenkis, pages 11–30. Springer, 2015.
16

Haoxiang Wang, Haozhe Si, Bo Li, and Han Zhao. Provable domain generalization via
invariant-feature subspace recovery. InInternational Conference on Machine Learning,
pages 23018–23033. PMLR, 2022.
Xinyi Wang, Michael Saxon, Jiachen Li, Hongyang Zhang, Kun Zhang, and William Yang
Wang. Causal balancing for domain generalization. InThe Eleventh International Con-
ference on Learning Representations, 2023.
Yimu Wang, Yihan Wu, and Hongyang Zhang. Lost domain generalization is a natural
consequence of lack of training domains. InProceedings of the AAAI Conference on
Artificial Intelligence, volume 38, pages 15689–15697, 2024.
Danru Xu, Dingling Yao, Sebastien Lachapelle, Perouz Taslakian, Julius von K¨ ugelgen,
Francesco Locatello, and Sara Magliacane. A sparsity principle for partially observable
causal representation learning. InForty-first International Conference on Machine Learn-
ing. PMLR, 2024.
Hong Zheng and Fei Teng. Distribution shift is key to learning invariant prediction.Pro-
ceedings of the AAAI Conference on Artificial Intelligence, 40(34):28812–28820, Mar.
2026.
17
