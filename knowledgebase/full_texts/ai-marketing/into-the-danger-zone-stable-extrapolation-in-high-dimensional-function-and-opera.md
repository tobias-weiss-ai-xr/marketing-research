---
title: 'Into the danger zone: stable extrapolation in high-dimensional function and operator learning'
url: https://arxiv.org/abs/2609.36709
category: ai-marketing
subcategory: measurement
date: 2026-09
venue: ''
authors:
- Ben Adcock
- Simone Brugiapaglia
- Xuemeng Wang
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.36709
pages: 58
chars: 155858
fetched_at: '2026-11-08T13:25:50+00:00'
kb_version: 1
---

# Into the danger zone: stable extrapolation in high-dimensional function and operator learning

INTO THE DANGER ZONE: ST ABLE EXTRAPOLA TION IN
HIGH-DIMENSIONAL FUNCTION AND OPERA TOR LEARNING∗
BEN ADCOCK † , SIMONE BRUGIAPAGLIA ‡ ,ANDXUEMENG W ANG †
Abstract.Out-of-distribution (OOD) generalization is a central challenge in scientific machine
learning. We study regression problems in which the test distribution differs from the training distri-
bution and ask: under what assumptions on the target function or operator is stable extrapolation
possible, and how far beyond the training domain can one extrapolate? Existing theory controls the
test error through additive penalties measuring the discrepancy between the training and test dis-
tributions. Such guarantees show robustness to small distribution shifts, but can be very pessimistic
in comparison to OOD performance observed empirically. We identify classes of holomorphic func-
tions and operators for which the OOD generalization error converges at algebraic rates even in
the presence of large distribution shifts. This phenomenon stems from the increasing smoothness of
higher-index coordinates, leading to what we term a ‘blessing of high dimensionality’. For learning
with either polynomials, deep neural networks or deep neural operators, we derive explicit rates
for arbitrary test measures supported on suitable domains and quantify how the admissible domain
depends on the underlying regularity of the function or operator. Our extrapolation guarantees are
independent of the test distribution, depending only on its support. We also present a series of
numerical experiments across a range of functions and operators that support the main theoretical
findings.
Key words.out-of-distribution generalization, stable extrapolation, high-dimensional approxi-
mation, operator learning, holomorphic functions and operators
MSC codes.41A63, 41A10, 46E50, 68Q32, 68T07
1. Introduction.The ability of models to extrapolate beyond their training
domain is a central challenge in modern Machine Learning (ML) and, in particular,
Scientific ML (SciML). Understanding and enhancing theout-of-distribution (OOD)
performance of ML models – namely, how well a model generalizes to examples drawn
from a test distribution that differs from the training distribution – is a substantial
area of research. Yet, as we discuss in§1.1, existing theory of OOD generalization
in ML largely addresses the case of smalldistributional shifts, where the training and
test distributions are close in some metric. Such guarantees are very general, placing
minimal assumptions on the model or target object, but say little about larger shifts.
However, a growing body of work in the SciML literature (described further in§1.4)
has shown that trained Deep Neural Network (DNN) and Deep Neural Operator
(DNO) models can oftenextrapolate: they generalize well much further from their
training distribution than such pessimistic guarantees imply.
This raises a key question:under what assumptions on the target function or oper-
ator is stable extrapolation possible and how far can one extrapolate?We address this
question for classes of holomorphic functions and operators using polynomials, DNNs
and DNOs. Our results establish explicit algebraic convergence rates for the OOD
generalization error in theL ∞-norm and quantify how the admissible extrapolation
domain depends on the underlying regularity Our results aredistribution-agnostic, as
they depend on the support of the test distribution only. They also reveal a certain
∗Submitted to the editors on September 30, 2026.
F unding:BA acknowledges support from the Natural Sciences and Engineering Research Coun-
cil of Canada (NSERC) through grants RGPIN-2026-04531 and DGDND-2026-04531. SB acknowl-
edges support from NSERC through grant RGPIN-2020-06766. BA, SB & XW acknowledge the
support of FRQ (Fonds de recherche du Qu´ ebec) – Nature et Technologies through grant 359708.
†Simon Fraser University (ben adcock@sfu.ca,xuemeng wang 2@sfu.ca).
‡Concordia University (simone.brugiapaglia@concordia.ca).
1
arXiv:2609.36709v2  [math.NA]  3 Oct 2026

2B. ADCOCK, S. BRUGIAPAGLIA AND X. W ANG
blessing of high dimensionality: increasing smoothness in higher-index coordinates
permits extrapolation in increasingly large domains and, in appropriate regimes, pre-
serves the underlying algebraic convergence order. Our results are complemented
with numerical experiments illustrating extrapolation in both function and operator
learning and supporting our main conclusions.
This work combines classical numerical analysis of polynomial extrapolation,
modern approximation theory in high and infinite dimensions and the recent advances
in DNN/DNO approximation and generalization theory. We provide a coherent and
comprehensive answer to this question of OOD generalization in the setting holomor-
phic regularity – a common assumption in practice, especially in SciML – thereby
bridging a key gap between existing distributional shift theory in ML and practical
performance of SciML models.
1.1. OOD generalization in ML.Consider a standard regression problem in
ML where a model ˆfis trained to approximate an unknownf:R d →R. Letϱ
andµbe two probability measures onR d, thein-distributionandout-of-distribution
measures, respectively. Then typical OOD guarantees in ML (see§1.4 for references)
take the form
(1.1)∥f− ˆf∥ p Lp µ(Rd) ≲∥f− ˆf∥ p Lp ϱ(Rd) +D(µ, ϱ),
assuming some mild regularity off, ˆf, such as Lipschitz continuity. Here and else-
where, we writeA≲Bto mean there exists a numerical constantc >0 such that
A≤cB, and likewise forA≳B. Such an estimate bounds the OOD error in terms of
the in-distribution error plus a termD(µ, ϱ) measuring the distance between the two
measures. Often,D=W p is the Wassersteinp-distance. For instance, whenp= 2, a
typical bound is
(1.2)∥f− ˆf∥ 2 L2µ(Rd) ≤ ∥f−ˆf∥ 2 L2ϱ(Rd) +C(f, ˆf , ϱ, µ)W2(µ, ϱ).
HereC(f, ˆf , ϱ, µ) = (Lf +L ˆf )
q
4(Lf +L ˆf )2(m2(µ) +m 2(ϱ)) + 16(|f(0)|2 +| ˆf(0)| 2),
L· denotes the Lipschitz constant andm 2(·) denotes the second moment. Unfor-
tunately, these error bounds are only meaningful for small distribution shifts. For
example, ifϱ=U([0,1] d) andµ=U([0,1 +δ] d), thenW p(ϱ, µ)≍δ √ d. Hence these
bounds become meaningless unlessδis small. More generally, convergence of the in-
distribution error to zero does not imply the same for the OOD error in the presence
of a fixed discrepancyD(µ, ϱ).
However, in practice, ML models often generalize much better than such bounds
suggest. To illustrate, in Fig. 1 we show in-distribution and OOD generalization errors
for function approximation and operator learning tasks. In the both cases, the terms
W2(ϱ, µ) are large. Yet, the OOD error decays asm→ ∞, albeit at a slower rate
than the in-distribution error (yet still algebraic). Our aim in this paper is to explain
this phenomenon.
1.2. Main results.Our results identify classes of functions and operators for
which the OOD error converges algebraically forarbitrarymeasures supported in
certain explicitly quantified domains. We now describe our setup for functions, before
considering operators later.
In- and out-of-distribution measures.For reasons we discuss in§2, we
consider functionsf:R N →Rof infinitely-many variables. However, our results
apply seamlessly to functions ofd <∞variables (Remark 2.3). For the training

STABLE EXTRAPOLATION IN LEARNING3
θ 0.1 0.2 0.3 0.4
W2(ϱ, µ) 0.91 1.82 2.73 3.64
θ 0.5 0.75 1.25 1.499
W2(ϱ, µ) 0.10 0.19 0.52 0.89
Fig. 1: For both function (left) and operator (right) learning tasks, the OOD generalization
error decays algebraically even thoughW 2(ϱ, µ) is large. Top row: the squared relativeL 2 µ-
norm error versus number of training samplesmfor various test distributionsµ=µ θ. Here
θis a parameter that controls how far the test distribution is from the training distribution,
which corresponds to the caseθ= 0. Bottom row: the distanceW 2(ϱ, µ) between the training
and distributionsϱandµ. This experiment considers thewing weightfunction (left), learned
with a fully-connected DNN, and the solution operator of the Navier–Stokes PDE (right),
learned with a so-called Fourier neural operator. See§6.2 and§6.3, respectively, for further
details and discussion on these experiments.
distribution, we consider the uniform probability measureϱ=U([−1,1] N). Now let
ω= (ω i)i∈N ≥1(understood componentwise). For the test distribution, we consider
any probability measureµwith supp(µ)⊆D w, where
(1.3)D ω = [−ω1, ω1]×[−ω 2, ω2]× · · ·.
T raining data and learning problem.We consider the standard regres-
sion setting in ML, wherex 1, . . . ,xm ∼i.i.d. ϱand we are given noisy training data
(xi, yi :=f(x i) +e i),i= 1, . . . , m. Our results consider a bounded noise model,
which may be adversarial, whose contribution is controlled by∥e∥ 2. Now consider a
model classM– i.e., a set of functionsR N →R, taken in this work to be family of
polynomials or DNNs – and the estimator
(1.4) ˆf∈argmin
g∈M
1
m
mX
i=1
|g(xi)−y i|2.
Class of functions.Givenε >0 andb∈ℓ 1(N) withb≥0, we consider
the classH(b, ε) of (b, ε)-holomorphic functions (with norm at most one). As we
discuss further in§1.3-1.4, this is an important class in high-dimensional function and
operator learning.
Extrapolation condition.As noted, our results employ a multiplicative OOD
error bound which allows for large distribution shifts, with size determined by reg-
ularity of the functions being learned. To state this condition, we require several
further concepts. First, we define themonotoneℓ p-space, 0< p≤ ∞, denoted
ℓp M(N), as the space of all sequencesz= (z i)i∈N whose minimal monotone majorant
˜z= (˜zi)i∈N ∈ℓ p(N), where ˜zi := supj≥i |zj|. Second, we defineζ: [1,∞)→[1,∞) as

4B. ADCOCK, S. BRUGIAPAGLIA AND X. W ANG
ζ(ω) =ω+
√
ω2 −1. We now introduce the following condition relatingb,ωand a
further scalarp∈(0,1):
(1.5)b⊙r p ∈ℓ p M(N),∥b⊙(r p −1)∥ 1 < ε,wherer p = (ζ(ω i)2/p−1)i∈N.
Here⊙is the Hadamard product. The first condition is a decay requirement on the
sequenceb. The second limits the enlargement of the domain using the holomorphy
budgetε. As we see below, smaller values ofpgive faster convergence rates, but
increaser p and therefore strengthen both requirements. We discuss concrete examples
of this condition in§4.3.
Theorem1.1 (Theorem 4.1, informal version).Letω≥1andD ω be as in(1.3).
Then there exists a polynomial model classM=Pwith the following property. Let
f∈ H(b, ε), wherebis such that(1.5)holds for some0< p <1. Then any minimizer
ˆfof(1.4)satisfies
∥f− ˆf∥ L∞µ (RN) ≲C(b, ε,ω, p)(m/log4(m))1−1/p +∥e∥ 2/log 2(m)
with high probability, for any measureµsupported inD ω. Moreover, all elements of
Pare polynomials with at mostm/log 4(m)terms in the Legendre basis.
Theorem1.2 (Theorem 4.4, informal version).Consider the setup of the pre-
vious theorem, whereω min = min{ω i}>1. Then there exists a family of feedfor-
ward tanh DNNsM=Nachieving the same bound, up to an additional additive
term proportional to2 −m. Moreoverwidth(N)≲m/log(ω min)anddepth(N)≲
log(log(m)/log(ω min)).
Finally, we also consideroperator learning[16, 18, 44, 74], where the target is an
operatorF:X → Ybetween two separable Hilbert spaces. We consider an in-
distribution probability measureνonX, an OOD measureµonX, training data
(Xi, Yi :=F(X i) +E i),i= 1, . . . , m, whereXi ∼i.i.d. ν, a class of holomorphic
operatorsH(b, ε;X,Y) (see Definition 5.4), a familyNofneural operatorsX → Y
and an estimator ˆF∈argmin
G∈N
1
m
Pm
i=1 ∥G(X)−Y i∥2.
Theorem1.3 (Theorem 5.6; informal version).Letω>1, whereω min =
min{ωi}>1, and suppose that Assumptions 5.1-5.3 hold. Then there is a class
of DNOsNsuch that, for anyF∈ H(b, ε;X,Y)andbsatisfying(1.5), the estimator
ˆFachieves a similar bound with high probability. Moreover,width(N)≲m/log(ω min)
anddepth(N)≲log(log(m)/log(ω min)).
See§5 for full details on this case. This theorem asserts a similar OOD bound
for holomorphic operators to that given in Theorem 1.2 for holomorphic functions.
1.3. Contributions.We now discuss several key features of this work.
(i) Practical relevance, unknown anisotropy .Holomorphic functions and
operators arise in many parametric PDE and operator learning problems. See§1.4
for further discussion. Their anisotropic regularity permits algebraic approximation
rates even in infinite dimensions. A notable feature of our results is that the training
problem (i.e., the model classMand loss function) are independent ofb. They
are consequently applicable to theunknown anisotropysetting, where the estimator
has noa prioriknowledge of the smoothness of the target function or operator. As
discussed in [2,§3.3], this is particularly relevant in applications, where the target
may be a black-box.

STABLE EXTRAPOLATION IN LEARNING5
(ii) Distribution-agnostic bounds.OurL ∞-bounds hold uniformly over test
distributionsµsupported in a prescribed extrapolation domainD ω. The model class
may depend onω, but it requires no further knowledge ofµ. Notably, our bounds
require neither a bounded density dµ/dϱnor proximity ofµtoϱin some metric.
In particular,µmay be singular with respect toϱand place all its mass outside the
training support. This is a major conceptual departure of our work from standard
theory (recall§1.1).
(iii) Quantifiable extrapolation.(1.5) quantifies how far one can extrapolate
while retaining algebraic convergence. For example, suppose thatω i =ω,∀i∈N.
Then (1.5) holds wheneverb∈ℓ p M(N) and (ζ(ω) 2/p−1 −1)∥b∥ 1 < εand yields the
noise-free convergence rate (m/log 4(m))1−1/p. Thus, one can extrapolate to arbitrary
accuracy asm→ ∞to hypercubes whose side lengths are a constant size larger than
the in-distribution domain [−1,1] N. This is very different to bounds of§1.1, where
the discrepancyD(µ, ϱ) limits the accuracy. But (1.5) also allows for more. Assuming
sufficient decay of theb i, it permits domains whereω i → ∞asi→ ∞. For example,
suppose thatb i =ci −a andω i = 1 +i b fora, b, c >0 satisfying (1.5). Forc >0
sufficiently small, our results give rates arbitrarily close to (m/log4(m))1−(a+b)/(1+2b).
This example illustrates that one can extrapolate arbitrarily far in theith variable as
i→ ∞. Such a conclusion is, on the face of it, quite remarkable, and very unintuitive
from the perspective of distribution shift theory. See§4.3 for further discussion.
(iv) Stability and a blessing of high dimensionality .In low dimensions,
polynomial approximations to holomorphic functions achieve in-distribution errors
that decay exponentially. Exponential rates can be retained for extrapolation, but
at the cost of exponential instability. Such instability can be avoided, but with a
dramatic reduction in convergence order from exponential to algebraic. By contrast,
natural in-distribution rates in infinite dimensions are algebraic. Our results in (iii)
reveal ablessing of high dimensionality. Stable extrapolation to admissible hypercubes
preserves the same algebraic convergence order as the in-distribution rates. Moreover,
algebraic rates, albeit slower, persist for certain hyperrectangles with unbounded side
lengths. See Remark 3.3 for further details.
(v) Sample efficiency and optimal rates.Problems in SciML are often
data-starved, making it critical to establish results on the sample complexity of learn-
ing tasks. We consider standard i.i.d. samples from the underlying measureϱ. In
particular, the samples, beingindependentofω, do not need to be adapted to the
extrapolation domain. Our results show that holomorphic functions and operators
can be learned in a sample-efficient manner with algebraic rates in terms ofm, which
are also optimal in various settings (see Remark 4.7).
(vi) Generalization to rougher inputs.A crucial consideration in operator
learning is generalization torougherinputs (i.e., functions of lower regularity) than
those seen in training [27,43,51,74,85]. Fig. 1 already shows an example of this effect,
as the eigenvalues of covariance operator of the test distributions decay more slowly
than those of the training distribution (see§6.3 for further examples). Theorem 1.3
shows this is possible: the learned model can generalize to test distributionsµthat
arearbitrarily rough, and do so in a quantifiable manner, given sufficient smoothness
of the target operator. See§5.3 for further discussion.
1.4. Related work.We now discuss various related areas of work.
The challenge of OOD generalization.Practical demands mean that SciML
models are often applied to inputs drawn from distributions differing significantly from
their training distribution. Many recent works have discussed the importance and

6B. ADCOCK, S. BRUGIAPAGLIA AND X. W ANG
challenges of OOD generalization [14, 17, 19, 23, 43, 56, 62, 63, 70, 71, 77]. More broadly,
OOD generalization is a critical issue in AI for Science [84], and a key component of
therobustnessof AI models.
Understanding and enhancing the OOD performance is also a large topic in ML
in general, with well-established concepts and techniques such as domain adaptation
and generalization, distributionally robust optimization, invariant risk minimization,
risk extrapolation and others. See, e.g., [7, 11, 46, 58, 63, 80, 83]. Much of the literature
focuses on classification, as opposed to regression problems, making it not directly
applicable to SciML [83]. Further, distribution shifts in SciML are typically highly
structured [71], which renders concepts and approaches, including the distribution
shift bounds discussed in§1.1, potentially less relevant.
Existing OOD works.Distributional shift bounds of the form (1.1) can be
found in many places in the ML literature (see [10, 37, 42, 51] and references therein).
Use of theW p-distance is standard [12, 37, 42, 47, 51–53, 72] and the specific estimate
(1.2) is from [37, Prop. 3.1], which is based on [42, 51]. See [10] for similar bounds
using the TV distance and so-calledH-divergences. Our results contrast with these
general-purposeadditivebounds, as they rely on a multiplicative bound (Lemma 3.1).
They are also distribution-free, as they depend only on the support. A distribution-
free bound was also developed in [41, Cor. 5.2] using the modulus of continuity. But
it is also additive in nature, thus only relevant to small shifts.
OOD generalization in SciML has been investigated, primarily empirically, in
many works [13, 17, 23, 33, 51, 54, 62, 70, 71, 71, 83, 85]. Several of these demonstrate
successful generalization under substantial shifts [17, 27, 63, 71, 85], a phenomenon our
work strives to explain. Among theoretical contributions, [51] derives OOD bounds
for neural operators applied to high-frequency PDE problems. Yet these employ the
bounds of§1.1, and are therefore valid only for small shifts. More closely related to
our work, [27] establishes algebraic convergence rates for Bayesian learning of linear
operators. Our work can be viewed a generalization from linear operators to holo-
morphic operators, albeit in a non-Bayesian context. The work [80] also shares some
similarity with ours, since it considers genuine extrapolation versus small shifts. But
it does not provide generalization error bounds for concrete function classes.
Assumptions and technical ingredients.Infinite-dimensional homolorphy
was developed extensively in the study of parametric DEs. It is now known that
many families of parametric DEs have solution maps that are (b, ε)-holomorphic
functions. The list includes parametric diffusion equations, parametric heat equa-
tions, PDEs over parametrized domains and various parametric initial value problems.
See [3, 4, 21, 24, 64, 65, 68] and references therein. Holomorphic operators have also re-
ceived substantial attention in recent years. See [5,40,44,67,79] and references therein.
Besides their relevance to applications, holomorphic operators represent one of the few
known classes of operators that are not subject to thecurse of parametric complexity
orcurse of sample complexity, in contrast to finite-regularity operators [6, 50]. How-
ever, virtually all theory on learning holomorphic functions or operators considers
in-distribution performance. Our work extends this to the OOD regime.
Besides holomorphy, our work has two further technical ingredients. First, mod-
ern polynomial approximation theory of infinite-dimensional functions. See, e.g.,
[2, 3, 21, 24, 25] and references therein. Second, the powerful technique ofemulation
of polynomials via DNNs/DNOs [38, 59, 66, 68, 82] (see [2,§7.1] for a review). Note
that emulation techniques have been at the core of the modern approximation theory
of DNNs/DNOs which has developed in the last decade [29, 32]. While emulation
techniques are normally employed to show the DNNs/DNOs with certain approxima-

STABLE EXTRAPOLATION IN LEARNING7
tion guarantees, in this work we follow ideas first developed in [1] to employ them to
establish full generalization bounds.
Relation to classical analytic continuation.Extrapolation of holomorphic
functions is synonymous with analytic continuation, which is a classical topic in nu-
merical analysis (see [76] and references therein). The work [28] considered analytic
continuation of univariate functions via polynomials and linear least squares. Our
results can be seen as a generalization of [28] to multivariate functions. In [76] it is
shown that univariate analytic continuation is ill-posed without further constraints,
such as boundedness. The classH(b, ε) consists of unit norm, and therefore bounded,
functions and hence avoids this problem. But [76] shows that analytic continuation is
always ill-conditioned with respect toℓ ∞-norm perturbations of the data, with infinite
condition number. Our results do not contradict this statement, as they only show
ℓ2-norm stability via the term∥e∥ 2. See Remark 4.8 for further discussion.
1.5. Limitations.Holomorphy is a strong assumption. Although relevant to
many SciML problems, other problems lack this regularity. Indeed, there is a growing
discussion in operator learning as to what are the right structures beyond regularity
that may govern learnability [16, 18, 44, 74]. Our work does not strive to address this
question, which is largely open even in the in-distribution context (see also§7). On a
related note, the fact that our DNN/DNO results use emulation means that the re-
sulting estimators perform no better than corresponding polynomial estimators. Our
results also employ handcrafted DNN/DNO model classes, which are some ways away
from those typically used in practice (see also§7). Nonetheless, our work aligns with a
recent trend in operator learning, in which more classical approaches such as polyno-
mials [79] and kernel methods [9] have been revisited and generalized to the operator
setting, and shown to be competitive with DNOs in terms of in-distribution perfor-
mance. Our theoretical results provide similar conclusions for OOD performance.
There are also many different types of OOD generalization in SciML. In operator
learning, for instance, there is much interest in multi-operator learning and foundation
models, i.e., DNOs that can simultaneously solve multiple PDEs [19, 22, 39, 43, 71, 81,
83]. This is a type of OOD generalization where one wants to generalize to PDEs not
seen in training. While not unrelated, it differs from our setting, as we consider learn-
ing a single operator only. Our setting is also different from extrapolation-in-time, as
is common in neural PDE solvers [33, 43, 78]. Another distinct type of extrapolation
is superresolution, where one trains a DNO on a coarse grid, then uses finer grids at
test time [55] (see also [73] and references therein).
Finally, we stress that the objective of this work is to understand the OOD gen-
eralization of estimators, rather than methods of enhancing it. We discuss this im-
portant topic further in§7.
1.6. Outline.In§2 we introduce the class of functions considered and discuss
their approximation via polynomials. In§3 we begin our focus on OOD errors, by
deriving a key multiplicative bound which underpins all our main results. Our main
results are presented in§4 (for functions) and§5 (for operators). In§6 we present
numerical experiments and in§7 we conclude and discuss open problems. Proofs of
all results in this paper can be found in§SM1, while§SM2 contains additional details
on the numerical experiments.
2. Holomorphic functions and polynomial approximation.As mentioned
in§1.2, we consider functionsf:R N →Rand thein-distributionmeasureϱ=
U([−1,1] N). However, our theory applies seamlessly to functions of finitely-many

8B. ADCOCK, S. BRUGIAPAGLIA AND X. W ANG
variables (Remark 2.3). Working in infinite dimensions is convenient theoretically
and practically relevant, even for finite-dimensional functions, as finite-dimensional
functions behave like infinite-dimensional functions in terms of their approximation
theory as soon as the dimension is moderately large (Remark 2.5).
2.1. Polynomial expansions ands-term approximation.We first recap
some standard notions from polynomial approximation. See, e.g., [3, 24]. LetP n,
n∈N 0, denote the Legendre polynomials on [−1,1], with normalizationP n(1) = 1.
We define the normalized polynomials
(2.1)ψ n(x) =
√
2n+ 1P n(x),∀n∈N 0
and note that these form an orthonormal basis with respect to the uniform prob-
ability measure on [−1,1]. To extend toR N, we proceed by tensorization. Let
n= (n 1, n2, . . .)∈NN 0 and write supp(n) ={i:n i ̸= 0} ⊆Nfor its support.
We defineF={n∈N ∞ 0 :|supp(n)|<∞}and consider the multivariate polynomials
Ψn(x) = Q i∈N ψni (xi). The set{Ψ n}n∈F forms an orthonormal basis ofL 2 ϱ(RN) and
therefore anyf∈L 2 ϱ(RN) has the convergent expansion
(2.2)f=
X
n∈F
cnΨn,wherec n =⟨f,Ψ n⟩L2ϱ(RN) =
Z
RN
f(x) Ψn(x) dϱ(x).
We are interested inn-term approximations to such functions. Ann-term approxi-
mationtofbased on an multi-index setS⊂ F,|S|=n, has the form
(2.3)f S =
X
n∈S
cnΨn ∈ PS,whereP S = span{Ψn :n∈S}.
2.2. Infinite-dimensional holomorphic functions.We now introduce the
class of holomorphic functions considered. In the univariate setting, it is well known
that the expansion of a functionfusing the firstnLegendre polynomials converges
with rateρ −n, whereρ≥1 is the parameter of the largestBernstein ellipseE ρ within
whichfis holomorphic. Here
E1 = [−1,1],E ρ ={(z+z −1)/2 :z∈C,1≤ |z| ≤ρ} ⊂C, ρ >1.
Generalizing via tensor products, we define theBernstein polyellipseof parameter
ρ= (ρ 1, ρ2, . . .)∈[1,∞)N asE ρ =E ρ1 × Eρ2 × · · · ⊂CN.
Definition2.1 ((b, ε)-holomorphy).Letb∈[0,∞) N andε >0. A function
f:R N →Cis(b, ε)-holomorphic if it is holomorphic in every Bernstein polyellipse
Eρ with parameterρ= (ρ i)∞ i=1 ∈[1,∞) N satisfying
(2.4)
∞X
i=1

(ρi +ρ −1 i )/2−1  bi ≤ε.
See§1.4 for relevant literature on this class. For convenience we write
Rb,ε =
[
{Eρ :ρ∈[1,∞) N,ρsatisfies (2.4)} ⊆C N
for the region andH(b, ε) ={f:D→C(b, ε)-holomorphic,∥f∥ L∞(Rb,ϵ) ≤1}for the set of functions that are holomorphic inR b,ε with uniform norm at most one.

STABLE EXTRAPOLATION IN LEARNING9
Note that the sequencebdetermines the type of anisotropic behaviour of functions
inH(b, ε). Indeed, ifb j is large for somej∈N, then (2.4) holds only for small values
ofρ j, meaning thatfis less smooth with respect to the variablex j. Conversely, ifb j
is small (or evenb j = 0), thenfis more smooth (entire) in the variablex j.
Remark2.2 (Unknown anisotropy). In some cases, suitable parameters (b, ε)
may be known, e.g., viaa priorianalysis of a given problem. However, in practical
cases, values for these parameters are typically unknown. We refer to this as theun-
known anisotropysetting. Our main focus is on this more practical case, with our goal
being to design estimators with guaranteed convergence rates that are independent
of (b, ε). See [2,§3.3] for more discussion on known versus unknown anisotropy.
Remark2.3 (Finite-dimensional functions). Definition 2.1 is somewhat compli-
cated, in that it requires the function to have a holomorphic extension to a union
of Bernstein polyellipses. This is used in infinite dimensions to obtain algebraic
rates of convergence of the bestn-term approximation. In finite dimensions, it is
enough for the function to be holomorphic in a single Bernstein polyellipse. Con-
cretely, letf:R d →Rbe holomorphic in the finite-dimensional Bernstein polyellipse
E ¯ρ1 × · · · × E¯ρd ⊂C d. Now let
bi =ε

(¯ρi + ¯ρ−1 i )/2−1 −1 , i∈[d], b i = 0, i∈N\[d].
Then the natural extension ˜foffto a function of infinitely-many variables, defined
by ˜f(x) =f(x 1, . . . , xd) for allx= (x i)i∈N ∈R N, is (b, ε)-holomorphic. Hence, all
results that follow also apply seamlessly to finite-dimensional holomorphic functions.
2.3. Bestn-term approximation of holomorphic functions.Bestn-term
approximation is a type of nonlinear approximation [31] in which one chooses the
subsetS⊂ F,|S|=n, that minimizes the errorf−f S in a certain norm, wheref S
is the corresponding approximation (2.3). We shall consider this with respect to the
L2 ϱ-norm (although otherL p ϱ-norms,p̸= 2, could equally be considered). We define
anL 2 ϱ-norm bestn-term approximation as
fn =f S∗ ,whereS ∗ ∈argmin{∥f−f S∥L2ϱ(RN) :S⊂ F,|S|=n}.
Due to Parseval’s identity,S ∗ has an explicit characterization as the index set corre-
sponding tonlargest coefficients offin absolute value (note thatS ∗, and therefore
fn, need not be unique, due to ties, but this makes no difference in what follows).
The following result is well known (see, e.g., [3, Thm. 3.28] or [24,§3.2]). It demon-
strates that the bestn-term approximation of any function inH(b, ε) converges with
algebraic rate wheneverbisℓ p-summable.
Theorem2.4 (Algebraic convergence of the bests-term approximation).Let
ε >0andb∈[0,∞) N be such thatb∈ℓ p(N)for some0< p <1. Then, for any
2≤q≤ ∞,
(2.5)∥f−f n∥Lq ϱ(RN) ≤C(b, ε, p)·n1− 1 q − 1 p ,∀f∈ H(b, ε), n∈N.
This remarkable result states that there are classes of functions whose approxi-
mation by polynomials is free from thecurse of dimensionality, despite depending on
infinitely-many variables. Recall thatbcontrols the anisotropy of functions inH(b, ε).
The fasterbdecays (i.e., the smallerp), the more anisotropic the functions and the
faster the rate in (2.5).

10B. ADCOCK, S. BRUGIAPAGLIA AND X. W ANG
Remark2.5 (Finite-dimensional functions and exponential rates). Standard
polynomial approximation theory asserts that then-term approximation of a func-
tion ofd <∞variables that is holomorphic inE ρ1 × · · · × Eρd converges exponentially
fast inn 1/d. While exponential, this rate exhibits the curse of dimensionality, and
raises the question: what happens for larged? The bound (2.5) provides an answer.
By assuming holomorphyandanisotropy, one achievesd-independent algebraic rates
(here we recall that (2.5) also holds for any holomorphic function ofdvariables, due
to Remark 2.3). Typically, the error follows the algebraic rate for smalln, before
transitioning to the exponential rate asngrows larger. However, whend≈10 or
larger, this transition point typically occurs at a large value ofn, meaning that the
exponential rates are often not witnessed in practical computations [2]. Thus, alge-
braic rates are the relevant even in finite dimensions, except whendis small. See§6.1
for several examples of this phenomenon.
3. F rom in-distribution to out-of-distribution.The bound (2.5) considers
only the in-distribution error in theL q ϱ-norm. Further, it only asserts the existence of
a polynomial achieving the specified algebraic rate, but no insight into how to compute
from data. In this section, we focus on the OOD error, for an arbitrary measureµ.
We introduce an OOD generalization guarantee which, in contrast to those discussed
in§1.1, is multiplicative rather than additive. We then apply this to the polynomial
setting in Theorem 3.2, demonstrating that it guarantees good OOD generalization
up to the size of the in-distribution error.
3.1. A multiplicative OOD generalization guarantee.LetMbe an arbi-
trarymodel classorhypothesis setfor the regression problem, i.e., a set of functions
RN →Rfrom which we aim to compute an estimator ˆf∈ Mto an unknown function
f. Given two measuresϱ, µonR N, we define thedistribution shiftconstant ofMas
(3.1) ∆(M;ϱ, µ) = sup
( ∥g1 −g 2∥L∞µ (RN)
∥g1 −g 2∥L2ϱ(RN)
:g 1, g2 ∈ M, g1 ̸=g 2
)
.
This constant measures the worst-case OOD behaviour of the difference of two ele-
ments ofMrelative to their in-distribution behaviour. Note that it is possible to
formulate ∆(M;ϱ, µ) in terms of other norms. We use theL 2 ϱ-norm as we generally
consider estimators that are defined through empirical least-squares fits. We use the
L∞ µ -norm in order to have error bounds that depend on the support of the measure
µonly (since, in our work, all functions are continuous).
Lemma3.1 (Multiplicative OOD generalization bound).LetMand∆(M;ϱ, µ)
be as above andf∈L ∞ µ (RN). Then, for any ˆf∈ M,
∥f− ˆf∥ L∞µ (RN) ≤inf g∈M
n
∆(M;ϱ, µ)∥f−g∥ L2ϱ(RN) +∥f−g∥ L∞µ (RN)
o
+ ∆(M;ϱ, µ)∥f− ˆf∥ L2ϱ(RN).
(3.2)
Proof.By the triangle inequality and the definition of ∆(M;ϱ, µ), we have
∥f− ˆf∥ L∞µ (RN) ≤ ∥f−g∥L∞µ (RN) +∥g− ˆf∥ L∞µ (RN)
≤ ∥f−g∥L∞µ (RN) + ∆(M;ϱ, µ)∥g− ˆf∥ L2ϱ(RN)
for anyg∈ M. We now use the triangle inequality once more to get the result.

STABLE EXTRAPOLATION IN LEARNING11
This result implies that accurate OOD generalization is possible provided (i) the
constant ∆(M;ϱ, µ) is not too large, (ii) the model classMcontains an element
gthat provides simultaneously good approximations tofin both theL 2 ϱ- andL ∞ µ -
norms and (iii) the in-distribution generalization error is small. Further, (3.2) also
implies stability: the OOD generalization behaviour of ˆfwill be robust to errors
in the training data, as long as ∆(M;ϱ, µ) is not too large and the in-distribution
generalization performance of ˆfis robust to such errors.
3.2. Application to polynomial model classes.This begs the question: for
holomorphic functions, when is it possible to achieve (i)–(iii)? Our next result focuses
on (i)-(ii), and shows the existence of a polynomial model class that achieves these
objectives. The third objective, (iii), i.e., the construction of a suitable estimator, is
the focus of the next section.
Theorem3.2.Letω≥1,ϱ=U([−1,1] ∞),ω≥1andD ω be as in(1.3).
Suppose thatf∈ H(b, ε), whereb≥0andε >0satisfy
(3.3)b⊙r p ∈ℓ p(N),∥b⊙(r p −1)∥ 1 < ε,wherer p =ζ(ω) 2/p−1
for some0< p <1. Then, for everyk >0, there exists a setS⊂ Fdepending onb,
ε,ωandkwith|S| ≤ksuch that
(3.4) ∆(P S;ϱ, µ)≤
√
k,
whereP S is as in(2.3), and ag∈ P S such that
(3.5) ∆(P S;ϱ, µ)∥f−g∥ L2ϱ(RN) +∥f−g∥ L∞µ (RN) ≤C(b, ε,ω, p)k1−1/p
for any probability measureµsupported inD ω.
This is a key result of the paper. It provides a precise criterion (3.3) under which
one achieves the algebraic rate (3.5) with a distribution shift constant (3.4) growing
mildly ink. Notice that the model class depends on the anisotropy parametersband
ε, which makes it unsuitable for the unknown anisotropy setting (recall (i) in§1.3).
In the next section, we shall remove this requirement through a mild strengthening
of (3.3), which is equivalent to (1.5).
Remark3.3 (The blessing of high dimensionality). Letf:R→Rbe holomor-
phic inE ρ,n∈N,M=P n be the space of polynomials of degree at mostnand
suppose that supp(µ)⊆[−ω, ω]. This case was considered in depth in [28]. As shown
therein, the constant ∆(P S;ϱ, µ)≲nζ(ω) n and there exists ag∈ Msuch that
∆(PS;ϱ, µ)∥f−g∥ L2ϱ(R) +∥f−g∥ L∞µ ≲ρ,ω n(ζ(ω)/ρ) n.
Thus extrapolation is possible for anyωsatisfyingζ(ω)< ρ, with an exponential rate
of convergence inn. But this comes at the expense of a potentially exponentially-large
stability constant ∆(P S;ϱ, µ)≲nζ(ω) n. To compare with Theorem 3.2, letk >0
be arbitrary and setn=⌊ log(k) 2 logζ(ω) ⌋so that ∆(P S;ϱ, µ) =O( √ k). Here, the symbol
O(·) suppresses a log factor inkandω-dependent constant (which are irrelevant to
the present discussion). With this choice ofn, one ensures a similar stability level.
However, this reduces the convergence rate
∆(PS;ϱ, µ)∥f−g∥ L2ϱ(R) +∥f−g∥ L∞µ =O(k
1
2 (1−log(ρ)/log(ζ(ω))) )

12B. ADCOCK, S. BRUGIAPAGLIA AND X. W ANG
to algebraic ink. See [28] for a similar derivation, as well as lower bounds show-
ing that such convergence is optimal. Here lies the blessing of high dimensionality.
In low (in particular, one) dimension, the in-distribution error decays exponentially
fast. However, stable extrapolation can only be achieved by reducing the rate from
exponential to algebraic. Conversely, in infinite dimensions, the in-distribution error
decays algebraically, and stable extrapolation can be achieved with algebraic rates,
albeit with a potentially smaller order.
4. Sample-efficient OOD learning of high-dimensional functions.The
previous results show that there are (polynomial) model classes that control the OOD
error of an estimator ˆfup to its in-distribution error. However, they do not describe
how to compute such an estimator from data and, critically, how much data is required
to do so. This is the focus of the present section, which contains the main results
in this paper on function approximation. In§5, we establish analogous results for
operator learning. We now drawx 1, . . . ,xm ∼i.i.d. ϱand consider the training data
(4.1) (x i, yi), i= 1, . . . , m,wherey i =f(x i) +e i,
ande i ∈R. We then consider theℓ 2-loss over some model classM, yielding the esti-
mator ˆfin (1.4). We first consider polynomial model classes. Next, we use emulation
techniques to establish similar results for DNN model classes.
4.1. Polynomial model classes.It is possible to obtain an estimator by di-
rectly combining Theorem 3.2, which identifies a suitable polynomial spaceP S, with
rather standard tools from the analysis of linear least-squares fitting with i.i.d. random
samples. However, such a result is unrealistic, since the model class (and consequently
the estimator) requires knowledge of the anisotropy parameters (b, ε). Our main result
establishes the existence of an estimator that is independent of (b, ε), and therefore
suitable for the unknown anisotropy setting described in Remark 2.2. For this, we
need the following assumption, which slightly strengthens (3.3):
(4.2)b⊙r p ∈ℓ p M(N),∥b⊙(r p −1)∥ 1 < ε,wherer p =ζ(ω) 2/p−1.
Recall from§1.2 thatℓ p M(N) is the monotoneℓ p-space.
Theorem4.1.Let0< ϵ <1,m≥¯m, where¯m= ¯m(ϵ)∈Ndepends onϵonly,
ϱ=U([−1,1] N),ω≥1andD ω be as in(1.3). Then there exists a polynomial model
classPdepending onm,ωandϵonly with the following property. Letf∈ H(b, ε),
whereb≥0andε >0satisfy(4.2)for some0< p <1, drawx 1, . . . ,xm ∼i.i.d ϱand
consider(1.4)with noisy training data(4.1). Then, with probability at least1−ϵ,
any minimizer ˆfsatisfies
∥f− ˆf∥ L∞µ (RN) ≲ C(b, ε,ω, p)√ϵ  m L 1−1/p + ∥e∥2√ L
for any probability measureµsupported inD ω, whereL=L(m, ϵ) := log 4(m) +
log(1/ϵ)ande= (e i)m i=1. Moreover, ˆf∈ PS for someSsatisfying|S| ≤m/L.
Here and elsewhere, apolynomial model classPis a subset of all algebraic poly-
nomials, i.e.,P ⊆span{x7→x n :n∈ F }, wherexn = Q i∈N xni i forx= (x i)i∈N
andn= (n i)i∈N. This result shows that the algebraic OOD error rate suggested by
Theorem 3.2 can be obtained frommsamples via a least-squares estimator, at the
loss of the log termL(m, ϵ). Further, the OOD error of the estimator is robust to
ℓ2-bounded noise, due to the term∥e∥ 2/ √ L.

STABLE EXTRAPOLATION IN LEARNING13
Remark4.2 (Condition (3.3) versus (4.2)). These conditions are identical when-
ever the sequenceb⊙r p is monotonically nonincreasing. Observe that in the in-
distribution setting (i.e.,ω=1), they reduce tob∈ℓ p(N) andb∈ℓ p M(N), respec-
tively. It has been shown [4] that it is impossible to construct estimators that converge
asm→ ∞for allb∈ℓ p(N). However, it is possible to construct an estimator for
allbsatisfyingb∈ℓ p M(N). Theorem 4.1 shows that it is also possible to construct
an estimator in the OOD setting that converges for allbsatisfying (4.2). It is cur-
rently unknown whether (4.2) can be weakened. However, as we discuss in Remark
4.7 later, under this condition the estimator developed in Theorem 4.1 yields rates
that are optimal up to the log termLfor specific choices ofω.
Remark4.3 (Practicality of the estimator). Theorem 4.1 is based on a sparse
polynomial approximation procedure, whereP=∪ S∈S PS is a union of subspaces of
dimension at mostm/L(m, ϵ). Roughly speaking, the collectionSis constructed by
selecting all possible index setsSasserted by Theorem 3.2 for any (b,ε) satisfying
(4.2). Being a union of polynomial subspaces, it shares some similarities with the
estimator of [26], although the choice of setsSis different. The strengthened condition
(4.2) is required over (3.3) to ensure that|S|<∞. This is a necessary component
of our analysis which, in general, uses compressed sensing techniques. Unfortunately,
the estimator in Theorem 4.1 is generally impractical to compute, since, in principle,
it would involve solving|S|linear least-squares problems and then choosing the one
with the smallest value of the loss function. This is, in some senses, analogous to
the classical problem of a sparse approximate solution to a linear systemAz=b
by minimizing∥Az−b∥ 2 2 over the set ofs-sparse vectors (since this set is a union
ofs-dimensional subspaces). In standard compressed sensing, one obtains practical
algorithms by via convexification – for instance, by minimizing the LASSO penalty
λ∥z∥1 +∥Az−b∥ 2 2. A similar approach could be considered here, by using a weighted
ℓ1-norm and following ideas from [3]. However, this is not the main focus of this work.
4.2. Deep learning and DNN model classes.We now focus on DNN model
classes. Letσ:R→Rbe an activation function. In this work, we consider feedfor-
ward DNNs of the form
(4.3)N:R n0 →R nM+1 ,z7→N(z) =A M (σ(AM−1 (σ(· · ·σ(A0(z))· · ·)))),
whereA l :R nl →R nl+1 are affine maps,n 1, . . . , nM are the widths of the hidden
layers, andn 0 andn M+1 are the input and output dimensions, respectively. We
define width(N) = max{n 1, . . . , nM }and depth(N) =M. We denote a DNN model
class of the form (4.3) with a fixed architecture (i.e., fixed activation function, depth
and widths) asN, and write width(N) = max{n 1, . . . , nM }and depth(N) =M.
LetNbe a DNN model class as above, with input dimensionn 0 =n∈Nand
output dimensionn M+1 = 1. Given training data (4.1) of an unknown functionf,
we consider estimator (1.4) withM=N. Notice that the variablex∈R N while
the input dimension of anyN∈ Nisn 0 <∞. We assume thatNacts on the first
n0 entries ofxonly, but to avoid unnecessary notation, we will simply writeN(x)
instead ofN(x [n0]).
Theorem4.4.Let0< ϵ <1,m≥¯m, where¯m= ¯m(ϵ)∈Ndepends onϵonly,
ϱ=U([−1,1] N),ω≥1satisfyω min := min{ω i}>1andD ω be as in(1.3). Then
there exists a DNN model classNwith tanh activation functions depending onm,ω
andϵonly with the following property. Letf∈ H(b, ε), whereb≥0andε >0satisfy
(4.2)for some0< p <1, drawx 1, . . . ,xm ∼i.i.d ϱand consider the problem(1.4)

14B. ADCOCK, S. BRUGIAPAGLIA AND X. W ANG
with noisy training data(4.1). Then, with probability at least1−ϵ, any minimizer ˆf
satisfies
∥f− ˆf∥ L∞µ (RN) ≲ C(b, ε,ω, p)√ϵ  m L 1−1/p + ∥e∥2√ L + 2−m,
for anyµprobability measure supported onD ω, whereL=L(m, ϵ) := log 4(m) +
log(1/ϵ)ande= (e i)m i=1. Further, the classNsatisfies
n0 ≲ m L ,width(N)≲ m log(ωmin) ,depth(N)≲log  log(m) log(ωmin)  .
This result shows one can achieve the same error bounds as in Theorem 4.1, up
to an extraO(2 −m) term, via deep learning with DNNs that are not excessively
wide or deep. This class uses tanh activations, yet other activations could readily be
considered (such as ReLU or general activations that are definable in ano-minimal
sense [45], for which the emulation results employed in the proof of Theorem 4.4 hold).
It also assumes thatω min >1, although we believe this could be removed by using
somewhat deeper DNNs.
Theorem 4.4 employs a specific ‘handcrafted’ family of DNNs. In the final layer,
the weights can take arbitrary real values, but in the hidden layers, only a certain
discrete set of values is allowed for the weights and biases (see the proof for the full
construction). This is because its proof is based on combining Theorem 4.1 with
tools from DNN emulation. Specifically, we approximately emulate the elements of
the polynomial model classPas tanh DNNs, then show that minimizers of the DNN
training problem yield approximate minimizers of the polynomial training problem.
Finally, the result follows through a careful perturbation analysis to show the overall
effect of the approximate emulation is at mostO(2 −m).
4.3. Examples and further discussion.We now discuss the condition (4.2)
and the various rates described by the above theorems. We do this by considering the
following two examples.
Example4.5 (Constant side lengths).Suppose first thatω 1 =ω 2 =· · ·=ω >1,
so thatD ω is a hypercube with side lengths2ω. Then(4.2)holds if and only if
(4.4)b∈ℓ p M(N)andω < ω ∗(b, ε, p) :=ζ−1

(1 +ε/∥b∥ 1)
p
2−p

.
Note here thatζ −1 : [1,∞)→[1,∞)is the Joukowsky mapζ −1(r) = 1 2  r+r −1 . Ob-
serve that the first conditionb∈ℓ p M(N)implies that the in-distribution error satisfies
∥f− ˆf∥ L∞µ (RN) ≲ C(b, ε, p)√ϵ  m L 1−1/p + ∥e∥2√ L
(this follows from Theorem 4.1 withω= 1). Hence, Theorems 4.1 and 4.4 show
that one can achieve precisely the same rate for the OOD error, for any measure
µsupported in[−ω, ω] N. Notice that this goes significantly beyond the realm of the
usual distribution shift theory described in§1.1, since such aµneed not be a small
perturbation ofϱ.
Example4.6 (Unbounded side lengths).Now suppose thatb i =ci −a andω i =
ib fora, b, c >0. Then(4.2)holds forp∈(0,1)if and only ifa,bandεsatisfy
(4.5) 1 p < a+b 1 + 2b andc
∞X
i=1
i−a

ζ(i b)2/p−1 −1  < ε.

STABLE EXTRAPOLATION IN LEARNING15
If this holds, the OOD error rate isO((m/L) 1− a+b 1+2b +δ)for anyδ >0. Conversely,
the in-distribution rate isO((m/L) 1−a+δ). Hence we achieve algebraic rates of decay
of the OOD error forany measure supported in a hypercube whose side lengths can
become arbitrarily large, albeit at a slower algebraic rate than the in-distribution error.
This setting is a stark contrast to theory of small distribution shifts discussed in§1.1.
Remark4.7 (Optimality of the rates). It is known that the in-distribution error
cannot decay any faster thanm1−1/p/log(m) in the worst case forb∈ℓ p M(N),∥b∥ p,M =
1, [5, Thm. 4.2]. This is a type of minimax lower bound, which considers the worst-case
error overH(b, ε) given arbitrary i.i.d. random samples and an arbitrary (nonlinear)
estimator. As a result of Example 4.5, the estimators of Theorems 4.1 and 4.4 yield
optimal OOD error rates (up to the log termL) over measuresµsupported in a
domain with constant side lengths. Currently, it is unknown whether the algebraic
rates in the setting of Example 4.6 are also optimal.
Remark4.8 (Ill-conditioning and best guaranteed accuracy). Our results show
that the estimator is robust to perturbations, yet, as noted in§1.4, analytic contin-
uation in one dimension is ill-conditioned with infinite condition number. We now
explain this seeming contradiction. The key point is that the former statements per-
tain toℓ ∞-norm perturbations in the data. Suppose now that the errorse i in the
data satisfy a uniform bound∥e∥ ∞ ≤χ, implying that∥e∥ 2 ≤ √mχ. Then, applying
Theorem 4.1 with an optimal choice ofmto balance the two error terms, we deduce
that one can compute an ˆfthat satisfies (for a possibly different constant)
(4.6)∥f− ˆf∥ L∞µ (RN) ≲C(b, ε,ω, p)χ
1/p−1
1/p−1/2 .
For this argument to imply that analytic continuation had a finite condition number,
this bound would have had to scale likeχ. But the power in (4.6) is less than one, as
indeed it must be so as not to contradict the one-dimensional result.
Viewingχ=ϵ mach as machine epsilon, the bound (4.6) can also be interpreted
as the best guaranteed accuracy in finite-precision computations. It is interesting
to note that this is some fractional power of machine epsilon that depends on the
smoothness, and settingω=1, this is even the case for the in-distribution error.
We believe this is an artefact of the estimator, which is based on theℓ 2-loss, or its
analysis. Determining whether (4.6) represents the best achievable accuracy forany
estimator is an interesting topic for future work.
5. Operator learning.Operator learning is an extension of the classical func-
tion approximation problem, where the target object is an operator between two, typ-
ically infinite-dimensional, spaces. As is customary, we consider operatorsF:X → Y
mapping between two separable Hilbert spacesX,Y. We endowXwith a probability
measureνand, givenX 1, . . . , Xm ∼i.i.d. ν, consider training data
(5.1) (X i, Yi), i= 1, . . . , m,whereYi =F(X i) +E i ∈ Y
andE i ∈ Yrepresents noise. The task is to approximateFfrom the data (5.1).
Operator learning is often carried out using DNOs. These are extensions of DNNs
that are designed to handle the infinite-dimensional nature of the inputs and outputs.
There are many different operator learning strategies, such as DeepONets [60], Fourier
Neural Operators (FNOs) [55], PCA-Net [48] and many others. We refer to [16, 18,
44, 74] for reviews.

16B. ADCOCK, S. BRUGIAPAGLIA AND X. W ANG
A standard operator learning paradigm, termedencoder-decoder nets, involves
approximatingFwith a DNO of the form
(5.2)F≈ ˆF:= ˆDY ◦ ˆN◦ ˆEX ,
where ˆEX :X →R dX in anencoderforX, ˆDY :R dY → Yis adecoderforYand ˆN:R dX →R dY is a neural network. The encoder and decoder are either specified by
the problem, learned spearately from data or learned concurrently with ˆN. Note that
DeepONets and PCA-Net both fall into this category, as do various other approaches.
Our main theoretical results consider certain types of encoder-decoder DNOs.
5.1. Assumptions and definitions.We now introduce the key assumptions
needed for our theoretical results.
Assumption5.1.The probability measureνhas mean zero and finite second mo-
ments, i.e.,
R
X ∥X∥ 2 X dµ(X)<∞. Further, letλ 1 ≥λ 2 ≥ · · · ≥0and{ϕi}i∈N ⊂ Xbe
the eigenvalues and orthonormal basis of eigenvectors of the covariance operator ofν.
Then the real-valued random variablesξ i =⟨X, ϕi⟩X /√3λi satisfyξ i ∼i.i.d. U([−1,1]).
Here
√
3 is a normalization factor, asEξ 2 i = 1/3. Assumption 5.1 means that
νis the law of theX-valued random variableX= P∞ i=1 √3λiξiϕi, whereξ i ∼i.i.d.
U([−1,1]). Such an assumption is quite common in practice. Indeed, it is standard in
operator learning literature to generate training data by simulating inputsXvia such
an expansion [16, 44, 74]. We slightly deviate from standard practice by assuming the
ξi are uniformly-distributed random variables, rather than standard normal random
variable. In the latter case,νis a Gaussian process onX. Dealing with normal
random variables presents some technical challenges, which are beyond the scope of
this paper. See§7 for further discussion.
Assumption5.2.Let theϕ i andλ i be as in Assumption 5.1. The encoder ˆEX is
given by ˆEX :X7→(⟨X, ϕ i⟩X /√3λi)dX i=1 and the decoder ˆDY is linear.
This assumption means that our DNO architecture is a type of PCA-Net [48], at
least in terms of its encoder, since ˆEX involves analyzingX∈ Xusing the firstd X
PCA basis functions. In PCA-Net, one normally first learns the PCA basis empirically
from data before learning the DNN ˆN. To avoid complications, we assume the exact
PCA basis is known. However, we believe it is possible to extend our analysis to
the case where an empirical PCA basis is employed by tracking the influence of this
error on the overall error bound. This is a topic for future work. In PCA-Net, the
decoder ˆDY is also constructed using the empirical PCA basis onYspecified by the
pushforward measureF ♯ν. However, we do not require this, since we just assume
linearity of the map.
Assumption5.3.The probability measureµonXsatisfies the following. Letυ
denote the law of the random variableξonR N, defined asξ=  ⟨X, ϕi⟩X /√3λi  i∈N,
whereX∼µ. Thensupp(υ)⊆D ω for someω≥1, whereD ω is as in(1.3).
This states that the projection of samplesX∼µvia the PCA basis{ϕ i}i∈N,
scaled by the PCA eigenvalues{λ i}i∈N, are bounded, and theith such projection
⟨X, ϕi⟩X /√3λi belongs to [−ω i, ωi] almost surely. Note that we do not require the
random variables⟨X, ϕi⟩X /√3λi to be uncorrelated, hence this assumption is quite
general. We discuss several examples that satisfy it in§5.3 below. In particular, we
show that this assumption allows for functions sampled from the test distribution
µto be less smooth than functions sampled from the training distributionν– an
important practical scenario.

STABLE EXTRAPOLATION IN LEARNING17
Finally, we now define the class of holomorphic operators we consider in this work.
Definition5.4.Suppose that Assumption 5.1 holds. We say thatF:X → Y
is a(b, ε)-holomorphic operator ifF(X) =f(⟨X, ϕ i⟩X )∞ i=1/√3λi),∀X∈ X, and
f:R N → Yis a(b, ε)-holomorphicY-valued function. We writeH(b, ε;Y)for the
class ofY-valued(b, ε)-holomorphic functions andH(b, ε;X,Y)for the class of(b, ε)-
holomorphic operators.
Remark5.5 (Infinite encoders and decoders). It is convenient at this point to
define the ‘infinite’ encoder and decoder
EX :X7→(⟨X, ϕ i⟩X /
p
3λi)i∈N,D X :x7→
X
i∈N
p
3λixiϕi.
Since{ϕ i}i∈N is an orthonormal basis, we have thatD X ◦ EX =I X . Notice that
Assumption 5.1 is equivalent toE X ♯ν=ϱ, where we recall thatϱ=U([−1,1]) N,
and Assumption 5.3 can be written equivalently as supp(E X ♯µ)⊆D ω. Further, the
operatorFand functionfin Definition 5.4 satisfyF=f◦ E X andf=F◦ D X .
5.2. Main result.Our main results consider operator learning using encoder-
decoder nets of the form (5.2). Given an encoder ˆEX and decoder ˆDY we letNbe a
family of DNNsN:R dX →R dY and consider the estimator
(5.3) ˆF= ˆDY ◦ ˆN◦ ˆEX ,where ˆN∈argmin
N∈N
1
m
mX
i=1
∥Yi − ˆDY ◦N◦ ˆEX (Xi)∥ 2 Y .
Before stating our result we need one further piece of notation. Recall from Assump-
tion 5.2 that ˆDY :R dY → Yis linear, therefore its range ˆY:= ˆDY (RdY ) denotes an
at mostd Y -dimensional subspace. We now write ˆBY :Y → ˆYfor the orthogonal
projection onto ˆY.
Theorem5.6.Let0< ϵ <1andm≥¯m, where¯m= ¯m(ϵ)depends onϵonly.
Suppose that Assumptions 5.1-5.3 hold withω>1satisfyingω min := min{ω i}>1.
Then there exists a DNN model classNwithn 0 =d X andn M+1 =d Y and depending
onm,ωandϵonly with the following property. LetF∈ H(b, ε;X,Y), whereb≥0
andε >0satisfy(4.2)for some0< p <1, drawX 1, . . . , Xm ∼i.i.d. νand let ˆFbe
as in(5.3)with noisy training data(5.1). Then, with probability at least1−ϵ, ˆF
satisfies
∥F− ˆF∥ L∞µ (X;Y) ≲ C(b, ε,ω, p)√ϵ  m L 1−1/p + r m ϵL ∥F− ˆBY ◦F∥ L2ν (X;Y)
+
∥E∥2;Y√
L
+ 2−m,
providedd X ≥cm/Lfor some universal constantc, whereL=L(m, ϵ) := log 4(m) +
log(1/ϵ)andE= (E i)m i=1. Further, the classNsatisfies
width(N)≲ m log(ωmin) ,depth(N)≲log  log(m) log(ωmin)  .
Here and elsewhere∥ · ∥Lp µ(X;Y) denotes theL p-Bochner norm (see§SM1.1). This
result provides an OOD generalization guarantee for operator learning. It shows that
the generalization error for learning holomorphic operator decays with algebraic rates

18B. ADCOCK, S. BRUGIAPAGLIA AND X. W ANG
of convergence in terms ofmdepending on the support of the measureµ, as described
by Assumption 5.3. We discuss examples of this condition in the next subsection.
As with previous results, the DNNs are not excessively wide or deep. Similar to
Theorem 4.4, while this result considers tanh DNNs, other activations could readily
be considered. Distinct from Theorem 4.4, however, this result describes learning
classes of operators taking values in an arbitrary separable Hilbert spaceY. For this
reason, the error bound contains an additional term that acounts for the decoding
error onY: namely,
∥F− ˆBY ◦F∥ L2ν (X;Y) =
sZ
X
∥F(X)− ˆBY ◦F(X)∥ 2 Y dν(X)≡ ∥IY − ˆBY ∥L2 F ♯ν(Y;Y) .
HereI Y :Y → Yis the identity map. Such an expression is quite standard in the
operator learning literature. Overall, this term implies that the decoder error depends
on how well ˆBY approximates the identity map. Concrete estimates for this term have
been established in various settings, such as PCA-Nets and DeepONets [48, 49].
5.3. Examples and further discussion.We now discuss Assumption 5.3 in
more detail.
Example5.7 (Rougher test distributions).Suppose thatµhas the same PCA
eigenbasis asν, with PCA eigenvalues{λ ′ i}i∈N satisfyingλ ′ i ≥λ i,∀i∈N. In this case,
µis the law of the random variableX= P∞ i=1 ξi p 3λ′ iϕi, whereξ i ∼i.i.d. U([−1,1]).
Note that, if{ϕ i}i∈N is an orthonormal basis of smooth functions, such as the Fourier
basis, this means that functions sampled from the test distributionµcan be less smooth
than functions sampled from the training distributionν. In this case, Assumption 5.3
holds if and only if
λ′ i ≤ω 2 i λi,∀i∈N.
meaning that the eigenvaluesλ ′ i may decay asi→ ∞at a slower rate than the
λi, depending on the growth rate of theω i. Indeed, after choosingωminimally so
that the above inequality holds, we obtain the OOD rateO((m/L) 1−1/p)provided
F∈ H(b, ε;X,Y)forb,εsatisfying
(5.4)
b⊙r p ∈ℓ p M(N),∥b⊙(r p −1)∥ 1 < ε,wherer p =

ζ
q
λ′ i/λi
2/p−1!
i∈N
.
Concretely, letλ i =i −v andλ ′ i =i −u forv≥u >1and suppose, as in Example 4.6,
thatb i =ci −a for somec >0. Then, it is a short argument to show that algebraic
convergence occurs – i.e.,(5.4)holds for somep∈(0,1)– whenevera >1 + v−u 2 and
cis sufficiently small. Thus, the OOD error decays algebraically even whenµis much
rougher thanν(i.e.,u≪v), providedFhas sufficient regularity.
In the previous example, the entriesξ i of the random variableξdefined in As-
sumption 5.3 were uncorrelated, sinceνandµdiffered only in their PCA eigenvalues.
However, Assumption 5.3 allows for correlated distributions, thus allowingνandµ
to be very different in nature. We now explore several such examples
Example5.8 (Arbitrarily rough test distributions).Suppose that∥X∥ X ≤cfor
X∼µa.s.. Note that such a distribution can be arbitrarily rough. Assumption 5.3
holds, providedω i ≥c/ √3λi,∀i∈N. In this case, Theorem 5.6 shows that one can

STABLE EXTRAPOLATION IN LEARNING19
generalize to arbitrarily rough test distributions given sufficient smoothness: namely,
(b, ε)-holomorphy, wherebsatisfies(4.2)for someωwhose entriesω i grow propor-
tional to1/ √λi. Thus, and perhaps unsurprisingly, faster decay of the eigenvalues
λi (i.e., a smoother training distributionν) translates into higher smoothness of the
operator in order to ensure convergence for an arbitrarily rough test distributionµ.
For a concrete example, letX=L 2([0,1])andϕ i(x) = √ 2 sin(iπx),∀i∈N, be
the sine basis. Letνbe the law of the random variableX=
√
2 P∞ i=1 ξii−v/2 sin(iπ·),
whereξ i ∼i.i.d. U([−1,1]), for somev >1. Now letd >1andµbe the law of
the random variableX= Pd−1 i=0 (2 +ξ i)I[i/d,(i+1)/d)(·), whereξ i ∼i.i.d. U([−1,1]).
Functions drawn fromνbelong almost surely toH s([0,1])fors <(v−1)/2, while
functions drawn fromµare pieceiwse constant and only belong toH s([0,1])almost
surely fors <1/2. Since∥X∥ X ≤3forX∼µa.s. we may chooseω i = 3i v/2 in
order for Assumption 5.3 to hold. Such choice is independent ofd. However, a direct
calculation gives that|⟨X, ϕi⟩X | ≤6
√
2d/i,∀i∈N, almost surely forX∼µ, meaning
that one can also chooseω i = max{1,6
√
2div/2−1}. Therefore, ifdis not large, a more
slowly-growing choice ofω i – which equates to a less stringent smoothness requirement
onF– is also possible.
6. Numerical experiments.We now present a series of numerical experiments.
These experiments consider polynomial, DNN and DNO estimators, with full imple-
mentation details given in Appendix SM2. The intention of these experiments is to
illustrate the main messages of the paper: namely, OOD generalization errors decay
at algebraic rates depending on the support of the test distribution. But they also
elucidate a number of gaps between the theory developed in this work and practice.
This motivates future work, as we discuss further in§7.
Remark6.1 (Unknown supports). The estimators we consider in our experiments
are all independent ofω, the parameter defining the hyperrectangleD ω in which the
support of the test distributionµis contained. This is a key difference with our theory,
since the estimators of Theorems 4.1, 4.4 and 5.6 all depend onω. An important
takeaway from our experiments is that polynomial and DNN estimators possess even
stronger OOD performance than the theory suggests, as they achieve algebraic rates
of convergencewithout any knowledgeof the test distributionµ. As we discuss further
in§7, understanding why this is the case is an open problem.
6.1. Polynomial estimators for multivariate function approximation.
We first consider multivariate function approximation. Our aim is to conduct a precise
study of the effect of changing the support of the test distribution on the convergence
rate and to compare the empirically-observed rates to the theoretical rates. Therefore,
in order to avoid effects implicit to training DNNs – such as architecture design,
initializations and optimization solvers – in this subsection we consider polynomial
estimators. For the reasons discussed in Remark 6.2, we do not implement exact the
estimator of Theorem 4.1. Instead, we consider an efficient Adaptive Least Squares
(ALS) estimator based on [61]. This estimator is described in§SM2.1.
Remark6.2 (Differences between Theorem 4.1 and the experiments). There
are several reasons why we do not implement the estimator of Theorem 4.1. First,
as discussed in Remark 4.3 it is generally impracticable. While it is possible to
design an implementable estimator using weightedℓ 1-minimization, such estimators
can be memory-intensive and slow to compute [3], thus limiting ones ability to perform
convergence studies involving large sample sizes. In comparison, the ALS estimator is
relatively inexpensive to compute, yet it lacks theoretical guarantees, even in the in-

20B. ADCOCK, S. BRUGIAPAGLIA AND X. W ANG
distribution setting [61]. However, the experiments in this section suggest it possesses
excellent in-distribution and OOD generalization properties.
To conduct a precise study, we consider the family of functions
(6.1)f: [−1,1] d →R,x= (x i)d i=1 7→
dY
i=1
p
2δi +δ 2 i
xi + 1 +δ i
,
for positive parametersδ i >0 (the factor in the numerator ensures this function has
unit norm, and therefore avoids scale effects for largeddue to thed-fold product) [2].
These functions are holomorphic in [−1,1] d with singularities at anyxfor which
xi =−1−δ i for somei. Therefore they are holomorphic inE ρ1 × · · · × Eρd for any
ρi ≥1 satisfying
(6.2)ρ i < ζ(1 +δi)∀i∈[d],
where we recallζfrom§1.2. Because of Remark 2.3, the function (6.1) – or, more
precisely, its extension to [−1,1] N – is (b, ε)-holomorphic for anyb= (bi)∞ i=1 satisfying
(6.3)b i > ε/δi,∀i∈[d], b i = 0,∀i > d.
In our experiments, we considerδ i = 2i2. For training and and test distributions, we
considerϱ=U([−1,1] d) andµ=U  ⊗d i=1[−ωi, ωi]  , respectively.
Following Example 4.5, in Fig. 2 we first consider constant side lengthsω 1 =
· · ·=ωd =ω≥1. Since min i δi =δ 1 = 2, (6.2) implies thatfis holomorphic in any
hypercube [−ω, ω]d withω <3. Fig. 2 shows that the OOD error decays for all values
ofωconsidered. Recalling Remark 2.5, we notice that in lower dimensiond= 8, the
rate of convergence appears slightly faster than algebraic, while whendincreases to
d= 32 we witness algebraic convergence.
In Fig. 2, we also compare the empirically-obtained algebraic rate of convergence
qfit with the rate predicted by our theoryq thy. Recall that our theory predicts a rate
(m/L)1−1/p whenever (4.2) holds for some 0< p <1. For a given value ofω, recalling
(6.3) and the fact thatδ i = 2i2, we determine that
(6.4)q thy = 1 2
"
log

1 + 2
. dX
i=1
i−2
! .
log(ζ(ω))−1
#
,
meaning that our theory predicts a rate that ism −qthy+δ for anyδ >0.
As Fig. 2 shows, the estimator consistently outperforms the theoretical conver-
gence rate, except in the caseω= 1, which corresponds to the in-distribution error.
Further, after manipulating (6.4), we see thatq thy ≤0, meaning our theory predicts
no convergence, wheneverω≥1.343. Yet, the estimator still converges algebraically
forω= 1.6 andω= 1.8. This suggests the main condition (4.2) may not be sharp –
improving it is an open problem.
Next, we consider varying side lengths. Following Example 4.6, we setω i =i b
for several different values ofb. Similar to the previous example, we witness algebraic
convergence, or faster in thed= 8 case. We also compare the rate against our theory.
In this case, the theoretical rate is given by
(6.5)q thy = 1/pthy −1,wherep thy solves
dX
i=1

ζ(i b)2/p−1 −1  i−2 = 2.

STABLE EXTRAPOLATION IN LEARNING21
ω q fit qthy
1.0 1.004 1.000
1.1 0.960 0.409
1.2 0.912 0.148
1.3 0.854 0.033
1.6 0.689 —
1.8 0.564 —
Fig. 2: Error versus number of training samplesmfor function approximation using poly-
nomial estimators computed by the ALS algorithm. The function is given by (6.1) with
δi = 2i 2,∀i∈[d] andd= 8 (left) ord= 32 (middle). The training and test distributions
areϱ=U([−1,1] d) andµ=U(⊗ d i=1[−ωi, ωi]), whereω 1 =· · ·=ωd =ω. The valueq thy is
given by (6.4) in the cased= 32. A dashed line means thatq thy ≤0, i.e., no convergence.
The valuesq fit were computed by empirical fitting in the cased= 32.
b q fit qthy
0.0 1.026 1.000
0.1 0.951 0.855
0.2 0.864 0.430
0.3 0.782 0.237
0.4 0.707 0.120
0.5 0.660 0.039
0.6 0.581 —
0.8 0.488 —
Fig. 3: The same as Fig. 2, except with varying side lengthsω i =i b and the valueq thy given
by (6.5) in the cased= 32 once more.
Once more, the empirical convergence rate is better than our theory predicts. In
particular, the estimator converges forb= 0.6 andb= 0.8. This is outside the realm
of our theory, which only asserts convergence forb <0.562. Indeed, (6.5) implies
thatq thy ≤0 wheneverb≥0.562. This once again points towards a potential lack of
sharpness in the condition (4.2) and an open problem for future work.
6.2. DNN estimators for multivariate function recovery .We now con-
sider DNN estimators. Rather than examine precise algebraic rates, our goal is to
demonstrate the OOD performance for a series of different functions motivated by
applications, in scenarios where the support of the test distribution varies. As in
the previous section, we do not implement the estimator described in our theoretical
result (Theorem 4.4). Instead, we opt for a fully-connected, feedforward architecture
that is independent ofω(recall Remark 6.1). Details of the architecture and training
procedure are given in§SM2.2.
We consider several standard test functions from theVirtual Library of Simulation
Experiments[75], specifically, thePhysical Modelssection of theEmulation/Prediction
Test Problemstest set. This is a standard library for high-dimensional approximation
and integration tasks, where each function represents a model for a certain physical
process. See [75] for details. To align with the rest of the paper, we rescale the input
variables to [−1,1] d and considerϱ=U([−1,1] d) as the training distribution.
In Fig. 1, we consider thewing weightfunction. This is ad= 10 variate

22B. ADCOCK, S. BRUGIAPAGLIA AND X. W ANG
ω 1.1 1.2 1.3
W2(ϱ, µ) 0.141 0.283 0.424
ω 1.1 1.2 1.4
W2(ϱ, µ) 0.153 0.306 0.811
Fig. 4: Error versus number of training samplesmfor approximating the circuit (left) and
piston (right) functions via tanh DNNs withL= 15 layers and widthW= 150.
function, which, after rescaling to [−1,1] 10 is holomorphic inside the hyperrectan-
gleD ω =⊗ 10 i=1[−ωi, ωi] for anyω= (ω i)10 i=1 satisfyingω<ω max, whereω max =
(7,6.5,4,9,2.10,3,2.6,2.43,5.25,+∞).In Fig. 1 we considerµ=U(D ω), whereω i =
1 +θ(ω i,max −1),∀i∈[10], with the valueω max,10 = 10. In other words, we study
extrapolation to a domain whose side lengths are a constant fraction of the maximum
possible extrapolation domain. As expected, in all cases we see algebraic convergence
with the rate depending on the size ofθ. Note that we plot the squaredL 2-error in
this experiment, in order to make a comparison with the distributional shift bound
(1.2). As we see from the table, the Wasserstein distanceW 2(ϱ, µ) is significantly
larger than this error, thus demonstrating the pessimistic nature of such bounds.
In Fig. 4 we consider two other functions from the same library, thecircuitandpis-
tonfunctions. These ared= 6 andd= 7 variate functions, respectively, that are holo-
morphic inside the hyperrectangleD ω =⊗ 6 i=1[−ωi, ωi] for anyω= (ω i)6 i=1 satisfying
ω= (ω 1, . . . , ω6)<ω max := (2,2.11,1.40,2.85,20.427,1.40) andω= (ω 1, . . . , ω7)<
ωmax := (3,1.67,1.5,1.5,10.97,67,35), respectively. We considerϱ=U([−1,1] d) and
µ=U([−ω, ω] d), whereω≥1 is a parameter we vary. For both functions, we witness
algebraic convergence for all values ofω. It is noticeable that the algebraic rate de-
creases slightly asωincreases. For the circuit function, the algebraic power decreases
from 0.4 in theω= 1 (i.e., in distribution) case to 0.19 in theω= 1.3 case. Similarly,
for the piston function it decreases from 0.44 whenω= 1 to 0.21 whenω= 1.4.
Remark6.3 (Differences between Theorem 4.4 and numerical experiments). The
primary difference is the choice of DNN familyN. As discussed in 4.2, Theorem 4.4
uses a specific handcrafted family of DNNs, where only certain values for the internal
weights and biases are allowed. Conversely, in our numerical experiments, we consider
fully-connected, feedforward DNNs where all weights and biases are trained and can
take arbitrary real values. In particular, the resulting estimator is independent of
ω, whereas the DNN family, and consequently the DNN estimator, of Theorem 4.4
depends onω(recall Remark 6.1).
6.3. DNO estimators for PDE operators.Finally, we consider operator
learning. As in the previous subsections, we do not strive to implement the DNO
estimators described in Theorem 5.6. Instead, due to their wide popularity and robust
performance, we consider FNOs. Details of the architecture and training procedure

STABLE EXTRAPOLATION IN LEARNING23
Fig. 5: Error versus number of training samplesmfor the Darcy flow problem withν=µ LN 3,2
andµ=µ LN 3,α (left),µ=µ PC 3,α (middle);ν=µ LN 3,1 andµ=µ cookies (right).
are given in§SM2.3.
In our first example, we consider the Darcy flow PDE
−∇ ·(a(x)∇u(x)) =f(x), x∈D, u(x) = 0, x∈∂D.(6.6)
HereD= (0,1) 2,u(x) is the pressure field,f(x) is the forcing function anda(x) is
the input permeability field. We takef(x) = 1 and consider the operatorFmapping
from the diffusion coefficienta(x) to the solutionu(x), i.e.,F:a7→u.
In Fig. 5, we follow standard practice and consider log-normal random fields, with
corresponding probability measures
(6.7)µ LN τ,α =ψ#N  0,(−∆ +τ 2I) −α ,whereψ(x) = exp(x).
Here ∆ is the Laplacian, which we equip with homogeneous Neumann boundary
conditions. In Fig. 5 (left) we considerν=µ LN 3,2 for training and for testing we
considerµ=µ LN 3,α for variousα <2. This corresponds to the setting of Example 5.7,
since the eigenvalues of the covariance operator ofN

0,(−∆ +τ 2I) −α are (π2(k2 1 +
k2 2) +τ 2)−α fork 1, k2 ∈N 0, which means that the test functions are rougher for
smallerα. Fig. 5 illustrates the same qualitative behaviour predicted by our theory:
the OOD generalization error decays at an algebraically inm, at a rate that decreases
asα→1 +. Next we test the conclusions of Example 5.8. We once more consider
ν=µ LN τ,α, while for testing we use distributions of piecewise constant functions. We
consider two examples. The first is a standard distribution in operator learning [55],
denotedµ PC τ,α, which takes the same form as (6.7), except withψ(x) replaced by a
piecewise constant functionϕtaking valueϕ(x) = 2 whenx >0 andϕ(x) = 0.5
otherwise. The second is the ‘cookies’ distribution, denotedµ=µ cookies, which
is common in parametric PDEs [8, 20]. See (SM2.2). In both cases, we see the
behaviour expected: namely, algebraic convergence (albeit at a slow rate) even though
realizations from the test distribution are very different from those seen in training.
In our second example, we consider the incompressible Navier–Stokes equations
in vorticity form on the torusT 2:
(6.8)
∂tw(x, t) +u(x, t)· ∇w(x, t) =ν∆w(x, t) +f(x), x∈T2, t∈(0, T],
∇ ·u(x, t) = 0, x∈T 2, t∈[0, T],
w(x,0) =w 0(x), x∈T 2.
Here,uis the velocity field,w=∇ ×uis the vorticity,w 0 is the initial vorticity,
ν >0 is the viscosity andfis a forcing function. We learn the solution operator

24B. ADCOCK, S. BRUGIAPAGLIA AND X. W ANG
F:w 0 7− →w|T2×(0,T] .Our setup is a standard one in the operator learning literature
[55]. For training and test distributions, we useµ τ,α =N(0, σ(−∆ +τ 2I) −α), where
∆ is equipped with periodic boundary conditions. Throughout, we use parameters
σ= 7 3/2,τ= 7.5,ν= 10 −3 (equivalently Re = 10 3),T= 50 and the forcing
f(x) = 0.1(sin(2π(x 1 +x 2)) + cos(2π(x1 +x 2))). For training, we useα= 2.5 while
in testing we use various valuesα <2.5, thus producing rougher test distributions.
Fig. 1 gives our results for the parameterθ:= 2.5−α. Once more, we see
algebraic convergence for all values ofα, with the rate decreasing asα→1 +. In this
figure, we plot the squaredL 2-error, to make a direct comparison with the bounds
(1.2). Notably, the errors are significantly smaller than the corresponding Wasserstein
distancesW 2(ν, µ), thus demonstrating the inadequacy of distributional shift theory
in explaining the OOD generalization performance of operator learning models, which
is the main thesis of this work.
Remark6.4 (Differences between Theorem 5.6 and the experiments). As in
Remark 6.3, the architectures used in our experiments (i.e., FNOs) differ from those
used in Theorem 5.6, which are handcrafted PCA-Net-type architectures. Also, we use
Gaussian or lognormal random fields for training in our numerical experiments, while
Assumption 5.1 means that in our theory the training distribution has a Karhunen–
Lo` eve expansion defined by i.i.d.U([−1,1]) random variables, rather thanN(0,1)
random variables. As we discuss below, extending our theory to deal with the latter
– and consequently Gaussian random fields – is an open problem.
7. Conclusion and future work.OOD generalization is one of the biggest
challenges in SciML. While standard theory shows robustness of estimators to small
distributional shifts, it has often been observed that estimators generalize much fur-
ther beyond their training distribution. This paper provides a theoretical analysis of
this phenomenon. Working with classes of holomorphic functions and operators, we
derived convergence rates for OOD generalization that depend on the specific regular-
ity and the support of the test distribution. These show successful generalization well
beyond small distributional shifts and genuine extrapolation behaviour. Our results
are quantifiable, distribution agnostic (i.e., depending only on the support) and, in
certain cases, the rates are optimal. We also show that stable extrapolation is possible
while retaining algebraic rates, which we refer to as a blessing of high dimensionality.
Finally, in the context of operator learning, our results show it is possible to generalize
from smooth training distributions to arbitrarily rough test distributions. Numerical
results on function and operator learning tasks support our main conclusions. There
are various avenues for future work, several of which we now describe.
F rom adaptation to generalization.As noted in Remark 6.1, our theoretical
estimators require knowledge ofω, i.e., a support estimate for the test distribution
µ. Thus, our results are ofdomain adaptationform. In domain adaptation [10,
11] one uses information aboutµto construct ML models that generalize beyond
their training set. Interestingly, our results require only very weak knowledge ofµ:
namely, a support estimate. However, the estimators used in our numerical results are
independent ofω(see Remark 6.1), thus they pertain to thedomain generalization
setting. An important question is whether one can construct estimators independent
ofωthat yield the same generalization bounds.. This would provide a theoretical
explanation for the domain generalization behaviour observed in practice.
W eaker conditions and sharper rates.Our theoretical results provide a suffi-
cient condition, (4.2), linking holomorphic regularity to the admissible extrapolation
domain and the convergence rate. The experiments in§6.1 motivate investigating

STABLE EXTRAPOLATION IN LEARNING25
whether this condition can be weakened. They show convergence for domains larger
than those ensured by (4.2), as well as faster rates. Note, however, that these ob-
servations concern particular functions, and do not determine worst-case convergence
rates of the specific holomorphic function classes. As discussed in Remark 4.7, the
theoretical rates are optimal up to logarithmic factors for certain domains with con-
stant side lengths. Establishing sharp rates for growing side lengths, as in Example
4.6, remains open. Resolving these questions requires lower bounds that account for
both the extrapolation domain and the required stability to perturbations.
Gaussian distributions.Our function approximation results consider the train-
ing distributionϱ=U([−1,1] N) and arbitrary test distributions supported in the
hyperrectanglesD ω. A natural extension is to tensor-product Jacobi distributions
on [−1,1] N, using orthonormal Jacobi polynomials in place of Legendre polynomials.
However, distributions with unbounded support present significantly more difficul-
ties. This impacts the operator learning case as well, as in Assumption 5.1 we impose
that the random variablesξ i ∼ U([−1,1]). In particular, our analysis does not apply
to the case whereνis a Gaussian measure onX, as in that case one would have
ξi ∼ N(0,1). Gaussian measures are ubiquitous in operator learning and, for these
reasons, we also used them in our numerical experiments. An important topic for
future work is to generalize our analysis to this case. We note, however, that this lim-
itation is not unique to our work – existing statistical learning theory guarantees for
operators typically assume boundedness of the training and test distributions [57, 67].
Practical architectures and statistical learning theory .As mentioned in
Remarks 6.3 and 6.4, our DNN/DNO architectures differ from those typically em-
ployed in practice. A challenge of future work is to extend our analysis to practical
architectures. In particular, for operator learning, we consider a type of PCA-Net,
while FNOs and DeepONets are substantially more popular. The typical machinery
to analyze generalization error with standard (as opposed to carefully handcrafted)
architectures is statistical learning theory, which has been employed in [57, 67] and
elsewhere to derive in-distribution generalization bounds for operator learning. Sta-
tistical learning theory considers the case of statistical noise whose variance may not
be small, i.e.,e i ∼ N(0, σ2) in (4.1), and can be used to construct DNN/DNO estima-
tors that achieveminimax optimal ratesfor nonparametric regression. Minimax rates
concern the best achievable accuracy formmnoisy samples uniformly over given class
of functions or operators. Our work focuses on the more typical setting in scientific
computing, of bounded, potentially adversarial noise that is small in norm. Thus, our
results are more closely associated withoptimal recovery rates, i.e., the best achiev-
able accuracy over a given class frommnoiseless samples. See [30] for discussion on
minimax versus optimal recovery rates. A major distinction is that minimax rates
typically decay no faster than the Monte Carlo rate, i.e.,O(m −1/2), while optimal re-
covery rates can be arbitrarily fast depending on the function or operator class. This
is also reflected in our results, where the algebraic order can be arbitrarily large with
sufficient smoothness. Nonetheless, it is an interesting problem for future work to use
statistical learning theory to derive OOD generalization guarantees for holomorphic
functions and operators in the presence of statistical noise.
Structure beyond regularity .As mentioned in§1.5, holomorphy is a strong
assumption which may not hold in practice. This has resulted in increasing discussion
about what underlying structure may allow high-dimensional functions and operators
to be efficiently learned [16,18,44,74]. Related to this is the question of how to enforce
such structure into SciML models. For instance, regularization functionals have been
used to encode PDE priors such as boundary conditions [56] and variational formula-

26B. ADCOCK, S. BRUGIAPAGLIA AND X. W ANG
tions [35]. Other approaches include PDE-informed architectures [15,34]. See also [69]
and references therein. Much of this discussion centres on in-distribution generaliza-
tion, but the same considerations apply OOD as well. Understanding what types of
structures aid OOD generalization and, critically, how to enforce such structure in
SciML models is a significant open problem.
Enhancing OOD performance.Similarly, there are many methods, largely
empirical, that strive to improve OOD generalization in SciML. These include: [85],
which studies incorporating physics, fine-tuning with new observations and multi-
fidelity data; [19], which considers in-context learning; [36], which considers transfer
learning; and [17, 70], which consider domain adaptation. See also [69] and references
therein. It would be interesting to understand if any of these approaches conveyed a
theoretical advantage over the generalization guarantees derived in this work.
F urther types of OOD generalization.Finally, as mentioned in§1.5, there
are different types of OOD generalization in SciML, especially in the realm of multi-
operator learning and foundation models. Our work considers OOD generalization
in the sense of differing training and test distributions. Extending our work to other
types of OOD generalization is an interesting topic for future research.
Acknowledgments.The authors would like to thank Chris Budd, Stefania
Fresca, Anastasis Kratsios and Jakob Zech for helpful discussions.
REFERENCES
[1]B. Adcock, S. Brugiapaglia, N. Dexter, and S. Moraga,Deep neural networks are effec-
tive at learning high-dimensional Hilbert-valued functions from limited data, in Proceed-
ings of The Second Annual Conference on Mathematical and Scientific Machine Learning,
J. Bruna, J. S. Hesthaven, and L. Zdeborov´ a, eds., vol. 145 of Proc. Mach. Learn. Res.
(PMLR), PMLR, 2021, pp. 1–36.
[2]B. Adcock, S. Brugiapaglia, N. Dexter, and S. Moraga,Learning smooth functions in high
dimensions: from sparse polynomials to deep neural networks, in Numerical Analysis Meets
Machine Learning, S. Mishra and A. Townsend, eds., vol. 25 of Handbook of Numerical
Analysis, Elsevier, 2024, pp. 1–52.
[3]B. Adcock, S. Brugiapaglia, and C. G. Webster,Sparse Polynomial Approximation of
High-Dimensional Functions, Comput. Sci. Eng., Society for Industrial and Applied Math-
ematics, Philadelphia, PA, 2022.
[4]B. Adcock, N. Dexter, and S. Moraga,Optimal approximation of infinite-dimensional
holomorphic functions, Calcolo, 61 (2024), p. 12.
[5]B. Adcock, N. Dexter, and S. Moraga,Optimal deep learning of holomorphic operators
between Banach spaces, in Advances in Neural Information Processing Systems, A. Glober-
son, L. Mackey, D. Belgrave, A. Fan, U. Paquet, J. Tomczak, and C. Zhang, eds., vol. 37,
Curran Associates, Inc., 2024, pp. 27725–27789.
[6]B. Adcock, M. Griebel, and G. Maier,The sample complexity of learning Lipschitz operators
with respect to Gaussian measures, arXiv:2410.23440, (2025).
[7]M. Arjovsky,Out of distribution generalization in machine learning, arXiv:2103.02667,
(2021).
[8]J. B ¨ack, F. Nobile, L. Tamellini, and R. Tempone,Stochastic spectral Galerkin and collo-
cation methods for PDEs with random coefficients: a numerical comparison, in Spectral
and High Order Methods for Partial Differential Equations, J. S. Hesthaven and E. M.
Rønquist, eds., vol. 76 of Lect. Notes Comput. Sci. Eng., Berlin, Heidelberg, Germany,
2011, Springer, pp. 43–62.
[9]P. Batlle, M. Darcy, B. Hosseini, and H. Owhadi,Kernel methods are competitive for
operator learning, J. Comput. Phys., 496 (2024), p. 112549.
[10]S. Ben-David, J. Blitzer, K. Crammer, A. Kulesza, F. Pereira, and J. W. V aughan,A
theory of learning from different domains, BIT, 79 (2010), pp. 151–175.
[11]S. Ben-David, J. Blitzer, K. Crammer, and F. Pereira,Analysis of representations for
domain adaptation, in Advances in Neural Information Processing Systems, vol. 19, 2006,
pp. 137–144.

STABLE EXTRAPOLATION IN LEARNING27
[12]J. Blanchet and K. Murthy,Quantifying distributional model risk via optimal transport,
Math. Oper. Res., 44 (2019), pp. 565–600.
[13]A. Bonfanti, R. Santana, M. Ellero, and B. Gholami,On the generalization of PINNs
outside the training domain and the hyperparameters influencing it, Neural Comput. Appl.,
36 (2024), pp. 22677–22696.
[14]F. Bonnet, J. Mazari, P. Cinnella, and P. Gallinari,AirfRANS: High fidelity compu-
tational fluid dynamics dataset for approximating Reynolds-averaged Navier–Stokes solu-
tions, in Advances in Neural Information Processing Systems, vol. 35, 2022, pp. 23463–
23478.
[15]N. Boull ´e, C. J. Earls, and A. Townsend,Data-driven discovery of green ’s functions with
human-understandable deep learning, Scientific reports, 12 (2022), p. 4824.
[16]N. Boull ´e and A. Townsend,A mathematical guide to operator learning, in Handbook of
Numerical Analysis, vol. 25, Elsevier, 2024, pp. 83–125.
[17]S. Brivio, S. Fresca, and A. Manzoni,PTPI-DL-ROMs: Pre-trained physics-informed deep
learning-based reduced order models for nonlinear parametrized PDEs, Comput. Methods
Appl. Mech. Engrg., 432 (2024), p. 117404.
[18]S. Brugiapaglia, N. R. Franco, and N. H. Nelsen,A short tour of operator learning theory:
convergence rates, statistical limits, and open questions, arXiv:2603.00819, (2026).
[19]W. Chen, J. Song, P. Ren, S. Subramanian, D. Morozov, and M. W. Mahoney,Data-
efficient operator learning via unsupervised pretraining and in-context learning, in Pro-
ceedings of the 38th International Conference on Neural Information Processing Systems,
Curran Associates Inc., 2024.
[20]A. Chkifa, A. Cohen, G. Migliorati, F. Nobile, and R. Tempone,Discrete least squares
polynomial approximation with random evaluations - application to parametric and sto-
chastic elliptic PDEs., ESAIM Math. Model. Numer. Anal., 49 (2015), pp. 815–837.
[21]A. Chkifa, A. Cohen, and C. Schwab,Breaking the curse of dimensionality in sparse polyno-
mial approximation of parametric PDEs, J. Math. Pures Appl., 103 (2015), pp. 400–428.
[22]Y. Choi, S. W. Cheung, Y. Kim, P.-H. Tsai, A. N. Diaz, I. Zanardi, S. W. Chung,
D. M. Copeland, C. Kendrick, W. Anderson, T. Iliescu, and M. Heinkenschloss,
Defining Foundation Models for Computational Science: A Call for Clarity and Rigor,
arXiv:2505.22904, (2025).
[23]M. Chu, Y. Liu, A. Biswas, and H.-W. Shen,Do physics foundation models learn gener-
alizable physics? a bias-aware benchmark across physical regimes and distribution shifts,
arXiv:2605.29283, (2026).
[24]A. Cohen and R. A. DeVore,Approximation of high-dimensional parametric PDEs, Acta
Numer., 24 (2015), pp. 1–159.
[25]A. Cohen, R. A. DeVore, and C. Schwab,Analytic regularity and polynomial approximation
of parametric and stochastic elliptic PDE’s, Anal. Appl. (Singap.), 9 (2011), pp. 11–47.
[26]A. Cohen, G. Migliorati, and F. Nobile,Discrete least-squares approximations over op-
timized downward closed polynomial spaces in arbitrary dimension, Constr. Approx., 45
(2017), pp. 497–519.
[27]M. V. de Hoop, N. B. Kovachki, N. H. Nelsen, and A. M. Stuart,Convergence Rates
for Learning Linear Operators from Noisy Data, SIAM/ASA J. Uncertain. Quantif., 11
(2023), pp. 480–513.
[28]L. Demanet and A. Townsend,Stable extrapolation of analytic functions, Found. Comput.
Math., 19 (2019), pp. 297–331.
[29]R. DeVore, B. Hanin, and G. Petrova,Neural network approximation, Acta Numer., 30
(2021), pp. 327–444.
[30]R. DeVore, R. D. Nowak, R. Parhi, G. Petrova, and J. W. Siegel,Optimal recovery meets
minimax estimation, arXiv:2502.17671, (2025).
[31]R. A. DeVore,Nonlinear approximation, Acta Numer., 7 (1998), pp. 51–150.
[32]D. Elbr ¨achter, D. Perekrestenko, P. Grohs, and H. B ¨olcskei,Deep neural network
approximation theory, IEEE Trans. Inform. Theory, 67 (2021), pp. 2581–2623.
[33]L. Fesser, L. D’Amico-Wong, and R. Qiu,Understanding and Mitigating Extrapolation
Failures in Physics-Informed Neural Networks, arXiv:2306.09478, (2023).
[34]C. R. Gin, D. E. Shea, S. L. Brunton, and J. N. Kutz,Deepgreen: deep learning of green ’s
functions for nonlinear boundary value problems, Scientific reports, 11 (2021), p. 21614.
[35]S. Goswami, A. Bora, Y. Yu, and G. E. Karniadakis,Physics-informed deep neural operator
networks, in Machine learning in modeling and simulation: methods and applications,
Springer, 2023, pp. 219–254.
[36]S. Goswami, K. Kontolati, M. D. Shields, and G. E. Karniadakis,Deep transfer operator
learning for partial differential equations under conditional shift, Nat. Mach. Intell., 4

28B. ADCOCK, S. BRUGIAPAGLIA AND X. W ANG
(2022), pp. 1155–1164.
[37]N. Guerra, N. H. Nelsen, and Y. Yang,Learning where to learn: training data distribution
optimization for scientific machine learning, arXiv:2505.21626, (2025).
[38]I. G ¨uhring and M. Raslan,Approximation rates for neural networks with encodable weights
in smoothness spaces, Neural Networks, 134 (2021), pp. 107–130.
[39]M. Herde, B. Raoni ´c, T. Rohner, R. K ¨appeli, R. Molinaro, E. de B ´ezenac, and
S. Mishra,Poseidon: Efficient foundation models for PDEs, in Advances in Neural Infor-
mation Processing Systems, vol. 37, 2024, pp. 72525–72624.
[40]L. Herrmann, C. Schwab, and J. Zech,Neural and spectral operator surrogates: Unified
construction and expression rate bounds, Adv. Comput. Math., 50 (2024).
[41]R. Hong and A. Kratsios,Bridging the gap between approximation and learning via optimal
approximation by ReLU MLPs of maximal regularity, arXiv:2409.12335, (2024).
[42]S. Hou, P. Kassraie, A. Kratsios, A. Krause, and J. Rothfuss,Instance-dependent gen-
eralization bounds via optimal transport, J. Mach. Learn. Res., 24 (2023), pp. 1–51.
[43]S. Jiang and A. F. Queiruga,What should physics foundation model benchmarks measure?,
Comput. Sci. Eng., (2026), pp. 1–7.
[44]N. B. Kovachki, S. Lanthaler, and A. M. Stuart,Operator learning: algorithms and
analysis, in Numerical Analysis Meets Machine Learning, S. Mishra and A. Townsend,
eds., vol. 25 of Handbook of Numerical Analysis, Elsevier, 2024, pp. 419–467.
[45]A. Kratsios, S. Brugiapaglia, B. J. Kim, G. Cousins, and H. S. d. O. Borde,Algorith-
mic foundations of deep learning: Complexity-theoretic rates and a characterization of
universal approximation, arXiv preprint arXiv:2606.26705, (2026).
[46]D. Krueger, E. Caballero, J.-H. Jacobsen, A. Zhang, J. Binas, D. Zhang, R. Le Priol,
and A. Courville,Out-of-distribution generalization via risk extrapolation (REx), in Pro-
ceedings of the 38th International Conference on Machine Learning, M. Meila and T. Zhang,
eds., vol. 139 of Proceedings of Machine Learning Research, PMLR, 2021, pp. 5815–5826.
[47]D. Kuhn, S. Shafiee, and W. Wiesemann,Distributionally robust optimization, Acta Numer.,
34 (2025), pp. 579–804.
[48]S. Lanthaler,Operator learning with PCA-Net: upper and lower complexity bounds, J. Mach.
Learn. Res., 24 (2023), pp. 318:15014–318:15080.
[49]S. Lanthaler, S. Mishra, and G. E. Karniadakis,Error estimates for DeepOnets: A deep
learning framework in infinite dimensions, arXiv:2102.09618, (2022).
[50]S. Lanthaler and A. M. Stuart,The parametric complexity of operator learning,
arXiv:2306.15924, (2024).
[51]J. A. Lara Benitez, T. Furuya, F. F aucher, A. Kratsios, X. Tricoche, and M. V.
De Hoop,Out-of-distributional risk bounds for neural operators with applications to the
Helmholtz equation, J. Comput. Phys., 513 (2024), p. 113168.
[52]J. Lee and M. Raginsky,Minimax statistical learning with Wasserstein distances, in Advances
in Neural Information Processing Systems, vol. 31, 2018.
[53]A. Levine and S. Feizi,Wasserstein smoothing: Certified robustness against Wasserstein
adversarial attacks, in Proceedings of the Twenty Third International Conference on Arti-
ficial Intelligence and Statistics, S. Chiappa and R. Calandra, eds., vol. 108 of Proceedings
of Machine Learning Research, PMLR, 2020, pp. 3938–3947.
[54]K. Li, A. N. Rubungo, X. Lei, D. Persaud, K. Choudhary, B. DeCost, A. B. Dieng, and
J. Hattrick-Simpers,Probing out-of-distribution generalization in machine learning for
materials, Communications Materials, 6 (2025), p. 9.
[55]Z. Li, N. Kovachki, K. Azizzadenesheli, B. Liu, K. Bhattacharya, A. Stuart, and
A. Anandkumar,Fourier neural operator for parametric partial differential equations,
in ICLR, 2021.
[56]Z. Li, H. Zheng, N. B. Kovachki, D. Jin, H. Chen, B. Liu, K. Azizzadenesheli, and
A. Anandkumar,Physics-informed neural operator for learning partial differential equa-
tions, ACM/IMS J. Data Sci., 1 (2024), pp. 1–27.
[57]H. Liu, H. Yang, M. Chen, T. Zhao, and W. Liao,Deep nonparametric estimation of
operators between infinite dimensional spaces, J. Mach. Learn. Res., 25 (2024), pp. 1–67.
[58]J. Liu, Z. Shen, Y. He, X. Zhang, R. Xu, H. Yu, and P. Cui,Towards out-of-distribution
generalization: A survey, arXiv:2108.13624, (2023).
[59]J. Lu, Z. Shen, H. Yang, and S. Zhang,Deep network approximation for smooth functions,
SIAM J. Math. Anal., 53 (2021), pp. 5465–5506.
[60]L. Lu, P. Jin, Z. Pang, G. Zhang, and G. E. Karniadakis,Learning nonlinear operators via
DeepONet based on the universal approximation theorem of operators, Nat. Mach. Intell.,
3 (2021), pp. 218–229.
[61]G. Migliorati,Adaptive approximation by optimal weighted least squares methods, SIAM J.

STABLE EXTRAPOLATION IN LEARNING29
Numer. Anal, 57 (2019), pp. 2217–2245.
[62]E. S. Muckley, J. E. Saal, B. Meredig, C. S. Roper, and J. H. Martin,Interpretable
models for extrapolation in scientific machine learning, Digit. Discov., 2 (2023), pp. 1425–
1435.
[63]B. D. Nguyen and S. Sandfeld,Out-of-distribution generalization of deep-learning surrogates
for 2D PDE-generated dynamics in the small-data regime, arXiv:2601.08404, (2026).
[64]F. Nobile, R. Tempone, and C. G. Webster,An anisotropic sparse grid stochastic collocation
method for partial differential equations with random input data, SIAM J. Numer. Anal.,
46 (2008), pp. 2411–2442.
[65]F. Nobile, R. Tempone, and C. G. Webster,A sparse grid stochastic collocation method for
partial differential equations with random input data, SIAM J. Numer. Anal., 46 (2008),
pp. 2309–2345.
[66]J. A. A. Opschoor, C. Schwab, and J. Zech,Exponential ReLU DNN expression of holo-
morphic maps in high dimension, Constr. Approx., 55 (2022), pp. 537–582.
[67]N. Reinhardt, S. W ang, and J. Zech,Statistical learning theory for neural operators,
arXiv:2412.17582, (2024).
[68]C. Schwab and J. Zech,Deep learning in high dimension: neural network expression rates for
generalized polynomial chaos expansions in UQ, Anal. Appl. (Singap.), 17 (2019), pp. 19–
55.
[69]L. Serrano, J. Han, E. Oyallon, S. Ho, and R. Morel,Test-time Generalization for Physics
through Neural Operator Splitting, arXiv:2602.00884, (2026).
[70]P. Setinek, G. Galletti, T. Gross, D. Schn ¨urer, J. Brandstetter, and W. Zellinger,
SIMSHIFT: A benchmark for adapting neural surrogates to distribution shifts,
arXiv:2506.12007, (2025).
[71]L. Shikhman,Diagnosing failure modes of neural operators across diverse PDE families,
arXiv:2601.11428, (2026).
[72]A. Sinha, H. Namkoong, and J. C. Duchi,Certifying some distributional robustness with
principled adversarial training, in International Conference on Learning Representations,
2018.
[73]U. Subedi and A. Tewari,Is Zero-Shot Super-Resolution Possible in Operator Learning?,
arXiv:2606.00296, (2026).
[74]U. Subedi and A. Tewari,Operator learning: a statistical perspective, Annu. Rev. Stat. Appl.,
13 (2026), pp. 123–148.
[75]S. Surjanovic and D. Bingham,Virtual library of simulation experiments: test functions and
datasets. http://www.sfu.ca/ ∼ssurjano.
[76]L. N. Trefethen,Quantifying the ill-conditioning of analytic continuation, BIT, 60 (2020),
pp. 901–915.
[77]H. W ang et al.,Scientific discovery in the age of artificial intelligence, Nature, 620 (2023),
pp. 47–60.
[78]S. W ang and P. Perdikaris,Long-time integration of parametric evolution equations with
physics-informed DeepONets, J. Comput. Phys., 475 (2023), p. 111855.
[79]J. Westermann, B. Huber, T. O’Leary-Roseberry, and J. Zech,Performance of neural
and polynomial operator surrogates, arXiv:2604.00689, (2026).
[80]K. Xu, M. Zhang, J. Li, S. S. Du, K.-I. Kawarabayashi, and S. Jegelka,How neural net-
works extrapolate: From feedforward to graph neural networks, in International Conference
on Learning Representations, 2021.
[81]Y. Yang, Z. Zhang, W. Zhu, W. Liao, and H. Liu,Generalization guarantees for multi-input
neural operator learning in Sobolev spaces, arXiv:2606.17419, (2026).
[82]D. Yarotsky,Error bounds for approximations with deep ReLU networks, Neural Networks,
94 (2017), pp. 103–114.
[83]L. Yuan, H. S. Park, and E. Lejeune,Towards out of distribution generalization for problems
in mechanics, Comput. Methods Appl. Mech. Engrg., 400 (2022), p. 115569.
[84]X. Zhang et al,Artificial intelligence for science in quantum, atomistic, and continuum
systems, Foundations and Trends in Machine Learning, 18 (2025), pp. 385–849.
[85]M. Zhu, H. Zhang, A. Jiao, G. E. Karniadakis, and L. Lu,Reliable extrapolation of deep
neural operators informed by physics or sparse observations, Comput. Methods Appl.
Mech. Engrg., 412 (2023), p. 116064.

SUPPLEMENT AR Y MA TERIALS: INTO THE DANGER ZONE:
ST ABLE EXTRAPOLA TION IN HIGH-DIMENSIONAL FUNCTION
AND OPERA TOR LEARNING∗
BEN ADCOCK † , SIMONE BRUGIAPAGLIA ‡ ,ANDXUEMENG W ANG †
SM1. Proofs of the main results.In this appendix, we present the proofs of
the main results from the paper.
Overall, these proofs use, adapt and extend tools from the approximation the-
ory of infinite-dimensional holomorphic functions [SM16, SM17, SM13, SM6, SM15], in
combination with emulation techniques [SM5, SM18, SM20, SM21, SM24, SM33, SM31,
SM25, SM28, SM32] to establish results for learning DNNs and DNOs. We commence
in§SM1.1 with some additional notation and concepts.§SM1.2 presents what is ar-
guably the key technical innovation in this work, namely, new weighted summability
bounds (Lemma SM1.4 and SM1.5) and weightedk-term approximation error bounds
(Theorems SM1.2 and SM1.3) for holomorphic functions forexponentially growing
weights. As we explain, summability with respect to exponentially growing weights
is directly related to extrapolation with polynomials.
In§SM1.3 we use these results to prove our main result on the existence of good
polynomial estimators for extrapolation, Theorem 3.2. Next, in§SM1.4 we prove the
main result on sample-efficient out-of-distribution learning via polynomials, Theorem
4.1. Finally, in§SM1.5 we establish the main results for DNNs and DNNOs, Theorems
4.4 and 5.6, respectively.
SM1.1. Additional notation and concepts.While the results in the main
paper consider real-valued functionsf:D→R, in our proofs we will establish results
for Hilbert-valued functionsf:D→ Y, where (Y,⟨·,·⟩ Y ) is a Hilbert space. This not
only generalizes the results in the main paper, but is also needed in order to establish
the results on operator learning considered in§5.
This necessitates some additional concepts (see, e.g., [SM6, SM8] and references
therein). First, given a setDwith a measureϱand 1≤p≤ ∞, we define the
Lebesgue–Bochner spaceL p ϱ(D;Y) as the space consisting of (equivalence classes of)
stronglyϱ-measurable functionsf:D→ Yfor which∥f∥ Lp ϱ(D;Y) <∞, where
∥f∥ Lp ϱ(D;Y) :=
(R
D ∥f(y)∥ p Y dϱ(y) 1/p 1≤p <∞,
ess supy∈D ∥f(y)∥ Y p=∞.
For simplicity we writeL p ϱ(D) whenY=R.
Second, we require various notions relating to sequences whose entries take values
inY. Letd∈N∪ {∞}, Λ⊆ Fbe a multi-index set andc= (c n)n∈Λ be a sequence
withY-valued entries. For 0< p≤ ∞, we writeℓ p(Λ;Y) for the space ofY-valued
∗Submitted to the editors on September 30, 2026.
F unding:BA acknowledges support from the Natural Sciences and Engineering Research Coun-
cil of Canada (NSERC) through grants RGPIN-2026-04531 and DGDND-2026-04531. SB acknowl-
edges support from NSERC through grant RGPIN-2020-06766. BA, SB & XW acknowledge the
support of FRQ (Fonds de recherche du Qu´ ebec) – Nature et Technologies through grant 359708.
†Simon Fraser University (ben adcock@sfu.ca,xuemeng wang 2@sfu.ca).
‡Concordia University (simone.brugiapaglia@concordia.ca).
SM1

SM2B. ADCOCK, S. BRUGIAPAGLIA AND X. W ANG
sequencesc= (c n)n∈Λ for which∥c∥ p;Y <∞, where
∥c∥p;Y =
(P
n∈Λ ∥cn∥p Y  1 p 0< p <∞,
supn∈Λ ∥cn∥Y p=∞.
WhenY=R, we just writeℓ p(Λ) and∥ · ∥p. Note that∥·∥ p;Y defines a norm when
1≤p≤ ∞and quasi-norm when 0< p <1. Now letc∈ℓ p(Λ;Y) ands∈Nwith
1≤s≤ |Λ|. We define theℓ p-normbests-term approximation errorofcas
(SM1.1)σ s(c)p;Y = inf
n
∥c−z∥ p;Y :z∈ℓ p(Λ;Y),|supp(z)| ≤s o .
Here,
supp(z) ={n∈Λ :z n ̸= 0}
is thesupportofz. Given aY-valued sequencecandS⊆Λ, we writec S for the
Y-valued vector withnth entry equal toc n ifn∈Sand zero otherwise. Observe
that
σs(c)p;Y = inf
n
∥c−c S∥p;Y :S⊆Λ,|S| ≤s
o
.
Now letw= (w n)n∈Λ >0be a vector of positive weights. For 1≤p≤2, we define
the weightedℓ p w(Λ;Y) space as the space ofY-valued sequencesc= (c n)n∈Λ for which
∥c∥p,w;Y <∞, where
∥c∥p,w;Y =
 X
n∈Λ
w2−p n ∥cn∥p Y
! 1
p
,1≤p≤2.
Notice that∥·∥ p,w;Y coincides with the unweighted norm∥·∥ p;Y for anywwhenp= 2,
or for anypwhenw=1. Next, we define the weighted cardinality of an index set
S⊆Λ as|S| w = P n∈S w2 n and, for 0< k≤ |Λ|w, we define theℓ p w-normweighted
best(k,w)-term approximation errorof aY-valued vector or sequencec∈ℓ p w(Λ;Y)
as
(SM1.2)σ k(c)p,w;Y = inf
n
∥c−z∥ p,w;Y :z∈ℓ p w(Λ;Y),|supp(z)| w ≤k o .
For later use, we also require the following result, which is a weighted version of
Stechkin’s inequality. See [SM6, Lem. 3.12] (note the result therein is only stated for
Y=R, but it readily extends to Hilbert-valued sequences).
LemmaSM1.1 (Weighted Stechkin’s inequality).Letd∈N∪ {∞},0< p≤2≤
2,k >0,c∈ℓ p w(Λ;Y)for someΛ⊆N d 0 andw= (w n)n∈Λ >0. Then
σk(c)q,w;Y ≤ ∥c∥p,w;Y k
1
q − 1 p .
Finally, we also need several concepts involving lower and anchored sets. Fori∈[d],
lete i be the multi-index withith entry equal to 1 and all other entries equal to zero. A
set Λ⊆N d 0, whered∈N∪ {∞}, islowerif, whenevern∈Λ andn ′ ≤n, it also holds
thatn ′ ∈Λ. Moreover, Λ isanchoredif it is lower and if, whenevere j ∈Λ for some
j∈[d], it also holds that{e 1,e 2, . . . ,ej} ⊆Λ. A scalar-valued sequenced= (d n)n∈Λ

SUPPLEMENTARY MATERIALS: STABLE EXTRAPOLATION IN LEARNINGSM3
ismonotonically nonincreasingifd n ≥d n′ whenevern≤n ′. It isanchoredif it is
monotonically nonincreasing andd ej ≤d ei wheneveri, j∈[d] withi≤j. Now let
c∈ℓ ∞(Λ;Y). Ananchored majorantofcis any scalar-valued sequenced= (d n)n∈Λ
that is anchored and satisfiesd n ≥ ∥cn∥Y ,∀n∈Λ. Theminimal anchored majorant
ofcis the (unique) scalar-valued sequence ˜cthat is an anchored majorant and for
which ˜c≤dfor any other anchored majorantd. It has the explicit expression
(SM1.3) ˜c n =
(
sup{∥cµ∥Y :µ≥n}ifn̸=e j for anyj∈[d],
sup{∥cµ∥Y :µ≥e i for somei≥j}ifn=e j for somej∈[d].
Given 0< p≤ ∞, we define theanchoredℓ p spaceℓ p A(Λ;Y) as the space of sequences
c∈ℓ ∞(Λ;Y) for which ˜c∈ℓ p(Λ), and define the (quasi-)norm∥c∥ p,A;Y =∥ ˜c∥p.
Finally, for 1≤s≤ |Λ|we also define theℓ p-normbests-term approximation error
in anchored setsby
(SM1.4)
σs,A(c)p;Y = inf
n
∥c−z∥ p;Y :z∈ℓ p(Λ;Y),|supp(z)| ≤s,supp(z) anchored o .
SM1.2. Summability and weightedk-term approximation of polyno-
mial coefficients.In this section, we provide several results on weighted summability
and weightedk-term approximation of polynomial coefficients of (b, ε;Y)-holomorphic
functions. They are crucial steps towards establishing our main results, as they can
be used to estimate both the in-distribution and out-of-distribution polynomial ap-
proximation errors.
Unweighted summability of polynomial coefficients of (b, ε;Y)-holomorphic func-
tions is a topic at the core of infinite-dimensional polynomial approximation the-
ory [SM6, SM15] since, in view of Stechkin’s inequality, it implies algebraic conver-
gence of the bests-term approximation. The extension from unweighted to weighted
summability and weightedk-term approximation was a crucial advance, since sets
with low weighted cardinality are critical to both guaranteeing convergence in the
L∞-norm and to ensuring that sample-efficient estimators can be constructed via
least-squares or compressed sensing techniques. See [SM30, SM14, SM29], as well
as [SM6, SM4, SM8]. However, these works consider only the in-distribution error and
weights that grow algebraically fast. As we explain next, to address out-of-distribution
errors, we require summability of polynomial coefficients with respect to exponentially
growing weights.
Recall thatϱis the uniform probability measure on [−1,1] N. To commence,
observe first that
(SM1.5)∥Ψ n∥L∞ϱ (RN) =
Y
j∈supp(n)
p
2nj + 1 =:u n,∀n∈ F,
which follows directly from the definition of the Ψ n. Next, we consider the behaviour
of the Legendre polynomials onD ω, whereD ω is as in (1.3). For this, we use the
integral representation
Pn(x) = 1 π Z π 0 (x+ p x2 −1 cos(θ)) n dθ,∀|x|>1, n∈N 0.
which follows from the contour integral representation ofP n [SM1, Tab. 18.10.1].
Hence
|Pn(x)| ≤ζ(ω)n,∀|x| ≤ω, ω >1, n∈N 0.

SM4B. ADCOCK, S. BRUGIAPAGLIA AND X. W ANG
We deduce that, for any probability measureµsupported inD ω,
(SM1.6)∥Ψ n∥L∞µ (RN) ≤
Y
j∈supp(n)
p
2nj + 1ζ(ωj)nj =:w n,∀n∈ F.
The key consequence of these observations is the following. Letf:D→ Ywith
Y-valued coefficientsc= (c n)n∈F ,S⊂ Fandf S = P n∈S cnΨn. Then observe that
the in-distributionL ∞-norm error can be bounded by
∥f−f S∥L∞ϱ (D;Y) ≤ ∥c−cS∥1,u;Y
whereu= (u n)n∈F , and the out-of-distributionL ∞-norm error can be bounded by
∥f−f S∥L∞µ (RN;Y) ≤ ∥c−cS∥1,w;Y ,
wherew= (w n)n∈F . Hence, the weighted Stechkin inequality (Lemma SM1.1) im-
plies algebraic decay of these errors, wheneverc∈ℓ p u(F;Y) orc∈ℓ p w(F;Y), re-
spectively. We now establish conditions under which these properties hold (note that
the former is just a special case of the latter corresponding toω=1). The key
innovation here is we show weighted summability of the polynomial coefficients of a
(b, ε;Y)-holomorphic function with respect to the exponentially-growing weightsw.
Our first main result in this section is the following.
TheoremSM1.2 (Weighted summability and weightedk-term approximation
with exponentially growing weights).Letω≥1and suppose thatf∈ H(b, ε;Y),
whereb∈ℓ 1(N)satisfies
(SM1.7)b⊙r p ∈ℓ p(N),∥b⊙(r p −1)∥ 1 < ε,wherer p =ζ(ω) 2/p−1
for some0< p <1. Then its coefficientsc∈ℓ p w(F;Y), wherewis given by(SM1.6).
Moreover, for anyk >0, there exists a setS⊂ Fdepending onk,b,εandωonly
with|S| w ≤ksuch that
∥c−c S∥q,w;Y ≤C(b, ε,ω, p)k1/q−1/p,
for anyq∈(p,2].
Secondly, we also establish a result on approximation of such anfvia anchored
sets, which will be needed in order to establish the results in§4 and§5 of the paper.
Here, we recall the definition of monotoneℓ p-space,ℓ p M(N) (see§1.2).
TheoremSM1.3 (Weighted summability and anchoreds-term approximation
with exponentially growing weights).Letω≥1and suppose thatf∈ H(b, ε;Y),
whereb∈ℓ 1(N)satisfies
(SM1.8)b⊙r p ∈ℓ p M(N),∥b⊙(r p −1)∥ 1 < ε,wherer p =ζ(ω) 2/p−1
for some0< p <1. Then its coefficientsc∈ℓ p w(F;Y), wherewis given by(SM1.6).
Moreover, for anys∈N, there exists an anchored setS⊂ Fdepending ons,b,ε
andωonly with|S| ≤ssuch that
∥c−c S∥q,w;Y ≤C(b, ε,ω, p)s1/q−1/p,
for anyq∈(p,2].

SUPPLEMENTARY MATERIALS: STABLE EXTRAPOLATION IN LEARNINGSM5
To prove these results, we require the following two abstract summability lem-
mas. Results of this type have a long history in the literature, first appearing
in [SM13, SM15, SM16] in the context of Chebyshev and Legendre polynomial co-
efficients of, firstly, parameter-to-solution maps of parametric PDEs and, latterly,
(b, ε;Y)-holomorphic functions [SM6, Thms. 3.28 & 3.33]. These two lemmas are
based directly on [SM8, Lem. 5.5], which considered abstract sequences of coefficients,
but only algebraically growing weights.
LemmaSM1.4 (Abstract summability).Let0< p <1,ε >0,ξ: (1,∞)→
[0,∞)be continuous withξ(t)bounded ast→ ∞,r≥1andb∈ℓ 1(N)be such that
(SM1.9)b⊙r∈ℓ p(N),∥b⊙(r−1)∥ 1 < ε.
Letc, γ >0be constant andd= (d n)n∈F be such that|d 0| ≤cand, for every
n∈ F \{0},
|dn| ≤
Y
k∈supp(n)
ξ(ρk)ρ−nk k rnk k (cnk + 1)γ
for allρ= (ρ j)j∈N ≥1satisfiying{k:ρ k >1} ⊇supp(n)and
(SM1.10)
∞X
j=1

ρj +ρ −1 j
2 −1
!
bj ≤ε.
Thend∈ℓ p(F)and∥d∥ p ≤C(b, ε,r, p, c, γ, ξ).
Proof.We follow the setup of [SM8, Lem. 5.5]. We splitN=E∪F, whereE= [d]
andF=N\[d], whered∈Nwill be chosen later. By assumption, there exists an
0< s <1 such that∥b⊙(r−1)∥ 1 ≤s 2ε. Now leta= (a j)j∈N >1be a sequence
that will be specified later that satisfies
(SM1.11)
∞X
j=1
(aj −1)b j ≤sε
Givenn∈ F, let ˜ρ= ˜ρ(b, ε,n)≥1be defined by
˜ρj + ˜ρ−1 j
2 =



aj j∈supp(n E)
aj + (1−s)εnj bj ∥nF ∥1 j∈supp(n F )
1j /∈supp(n)
Observe that{k:ρ k >1}= supp(n) and ˜ρsatisfies (SM1.10). Now suppose that
(SM1.12)a min = inf j {aj}>1.
and notice that
ξ(˜ρj)≤C(a min, ξ),∀j∈supp(n),
where the constantC(a min, ξ) is increasing asa min decreases. This follows from the
assumptions onξ, which imply that it is uniformly bounded on the interval [a min,∞),
combined with the fact that ˜ρj ≥a j > amin forj∈supp(n). This implies that
ξ(˜ρj)≤C(a min, ξ)nj + 1,∀j∈supp(n),

SM6B. ADCOCK, S. BRUGIAPAGLIA AND X. W ANG
and therefore
(SM1.13)|d n| ≤B(n) :=
Y
j∈supp(n)
˜ρ−nj j rnj j (˜cnj + 1)˜γ,
where ˜c= ˜c(amin, ξ, c) = max{C(amin), ξ), c}is likewise increasing asamin decreases
and ˜γ=γ+ 1. We now split the product and writeB(n) =B E(n)BF (n) and then
get
∥d∥p p ≤ X
n∈FE
BE(n)p · X
n∈FF
BF (n)p =: ΣE ·Σ F ,
whereF S ={n∈ F: supp(n)⊆S}forS=E, F. To complete the proof, it suffices
to show that Σ E,Σ F <∞.
Consider ΣE. We have
ΣE ≤
dY
j=1


∞X
nj =1
(rj/aj)pnj (˜cnj + 1)p˜γ

 .
This is finite, providedasatisfies
(SM1.14)a j > rj,∀j∈N.
Now consider Σ F . Using the definition of ˜ρj, we have
BF (n)≤
Y
j∈supp(nF )
 bj∥nF ∥1rj
(1−s)εn j
nj
(˜cnj + 1)˜γ
≤ ∥nF ∥1! nF !  e(b⊙r) F (1−s)ε nF Y j∈supp(nF )  ((˜c+ 1)nj)˜γ+ 1 
(heren F ! = Q j∈supp(nF ) nj! is the multi-index factorial). The argument is now
identical to the corresponding part of the proof of [SM8, Lem. 5.5], except withb
replaced byb⊙r. In particular, we see that Σ F <∞after takingdsufficiently large,
providedb⊙r∈ℓ p(N).
To summarize, we have shownd∈ℓ p(N), provided there exists a sequencea>1
that satisfies (SM1.11), (SM1.12) and (SM1.14). Set
(SM1.15)a j = 1 + max
 1 +s
2s (rj −1), (1−s)sε 2∥b∥1

.
Since 0< s <1, we see that (SM1.12) and (SM1.14) hold. Also, lettingJ={j∈N:
aj = 1 + 1+s 2s (rj −1)}, we see that
∞X
j=1
(aj −1)b j = 1 +s 2s X j∈J (rj −1)b j + X j /∈J (1−s)sε 2∥b∥1 bj
≤ 1 +s 2s s2ε+ (1−s)s 2 εε
=sε,
where in the second step we used the fact that∥b⊙(r−1)∥ 1 ≤s 2ε. Therefore
(SM1.14) holds as well. This completes the proof.

SUPPLEMENTARY MATERIALS: STABLE EXTRAPOLATION IN LEARNINGSM7
LemmaSM1.5 (Abstract anchored summability).Consider the setup of the pre-
vious lemma, except where(SM1.9)is replaced by
b⊙r∈ℓ p M(N),∥b⊙(r−1)∥ 1 < ε.
Thend∈ℓ p A(F)and∥d∥ p,A ≤C(b, ε,r, p, c, γ, ξ).
Proof.We proceed in a similar manner, but with some key differences. Lets∈
(0,1) be such that∥b⊙(r−1)∥ 1 ≤s 2ε. Now definea j as in (SM1.15) once more
and notice thata min = min{aj}>1. We also have
∞X
j=1
(aj −1)b j ≤sε,
as before. We now writeN=E∪F, whereE= [d] andF=N\[d] once more and
assume thatd∈Nis now sufficiently large so that
X
j>d
(rj −1)b j ≤ (1−s)ε 2β
for someβ >0 that will be chosen later. Givenb∈ F, we now let ˜ρ= ˜ρ(b, β, ε,n)≥1
be defined by
˜ρj + ˜ρ−1 j
2 =



aj j∈supp(n E)
aj +βr j + (1−s)εnj 2bj ∥nF ∥1 j∈supp(n F )
1j /∈supp(n)
Observe that{k:ρ k >1}= supp(n) and ˜ρsatisfies (SM1.10). Note that (SM1.13)
also holds for this choice of ˜ρ. The rest of the proof involves constructing an upper
bound ˜B(n)≥B(n) for which ( ˜B(n))n∈F is monotonically nonincreasing, anchored
andℓ p-summable. This will immediately imply the result.
WriteB(n) =B E(n)BF (n) as before, and considerB E(n). Let
κ= 1 + (1−s)sε 2∥b∥1 >1
and observe that there is a constantD=D(˜c,˜γ, κ)≥1 such that
(˜cn+ 1)˜γ≤D
 1 +κ
2
n
,∀n∈N 0.
Notice from (SM1.15) that
˜ρj ≥a j ≥1 + (1−s)sε 2∥b∥1 =κ,∀j∈supp(n E).
Hence
(SM1.16)B E(n)≤D d Y
j∈supp(nE )
 1 +κ
2κ
nj
=: ˜BE(n).

SM8B. ADCOCK, S. BRUGIAPAGLIA AND X. W ANG
Now considerB F (n). Lett= ]b⊙rbe a minimal monotone majorant ofb⊙r. Then
BF (n)≤
Y
j∈supp(nF )
(˜cnj + 1)˜γrnj j

βrj + (1−s)εn j 2bj∥nF ∥1
−nj
≤
Y
j∈supp(nF )
(˜cnj + 1)˜γ

β+ (1−s)εn j
2tj∥nF ∥1
−nj
=: ˜BF (n)
Hence, we define ˜B(n) = ˜BE(n) ˜BF (n).
We now show that ˜B(n) is monotonically nonincreasing. We do this by showing
it separately for ˜BE(n) and ˜BF (n). For the former, we see this readily holds since
κ >1 and therefore 1+κ 2κ <1. Now consider ˜BF (n). To show monotonicity, we show
that for everyn∈ Fand everyi > d, we have ˜BF (n+e i)≤ ˜BF (n). Assume first
thatn i ̸= 0. Then, arguing as in the proof of [SM8, Lem. 5.2], we have
˜BF (n+e i)
˜BF (n) ≤ 2˜γe β .
Now suppose thatn i = 0. Then
˜BF (n+e i)
˜BF (n) ≤ (˜c+ 1)˜γe β .
Therefore, it suffices to chooseβsatisfying
(SM1.17)β≥max

2˜γe,(˜c+ 1)˜γe 	 .
For any suchβ, we deduce that ˜BF (n), and therefore ˜B(n), is monotonically nonin-
creasing.
We now show that ˜B(n) is anchored, i.e., ˜B(ej)≤ ˜B(ei) wheneveri≤j. Observe
that
˜B(ej) =



Dd  1+κ 2κ  j∈E
(˜c+ 1)˜γ

β+ (1−s)ε 2tj
−1
j∈F
Suppose first thati, j∈E. Then ˜B(ej) = ˜B(ei), as required. Now suppose that
i, j∈F. Then we require

β+ (1−s)ε 2tj
−1
≤

β+ (1−s)ε 2ti
−1
.
This holds, sincetis a monotonically nonincreasing by assumption. Finally, ifi∈E,
j∈Fthen we require
(˜c+ 1)˜γ

β+ (1−s)ε 2tj
−1
≤D d
 1 +κ
2κ

.
We see that this holds, provided
β≥ (˜c+ 1)˜γ
Dd  1+κ 2κ  .

SUPPLEMENTARY MATERIALS: STABLE EXTRAPOLATION IN LEARNINGSM9
Recall thatD≥1 by assumption. Hence this condition is implied by
β≥(˜c+ 1) ˜γ
 2κ
1 +κ

.
Combining this with (SM1.17), we now pick
β= max

2˜γe,(˜c+ 1)˜γe,(˜c+ 1)˜γ
 2κ
1 +κ

This concludes the third case, and therefore we have shown that ˜B(n) is anchored.
It remains to show thatd∈ℓ p A(F). By construction, we have
∥d∥p p,A ≤ X
n∈F
˜B(n)p = X
n∈FE
˜BE(n)p · X
n∈FF
˜BF (n)p =: ˜ΣE · ˜ΣF .
Using (SM1.16), we see that
˜ΣE =D dp
 ∞X
n=0
 κ+ 1
2κ
n!p
<∞,
sinceκ >1. Now consider ˜ΣF . As in the previous proof, we have
˜BF (n)≤ Y
j∈supp(nF )
 2tj∥nF ∥1
(1−s)εn j
nj
(˜cnj + 1)˜γ.
We now argue in the same way as before, except withb⊙rreplaced by the sequence
2t, using the assumption thatt∈ℓ p(N).
We are now ready to establish Theorems SM1.2 and SM1.3.
Proof of Theorem SM1.2.We use Lemma SM1.4. Letn∈ F. Using [SM8, Lem.
5.4], we have
(SM1.18)∥c n∥Y ≤
Y
k∈supp(n)
ρ−nk+1 k
(ρk −1) 2 (nk + 1),
for anyρsatisfying (SM1.10) and{k:ρ k >1} ⊇supp(n), sincef∈ H(b, ε;Y) by
assumption. Now write
∥c∥p,w;Y =∥ ˜c∥p;Y ,
where ˜c= (˜cn)n∈F is given by ˜cn =c nw2/p−1 n . Using (SM1.18) and (SM1.6), we have
∥˜cn∥Y ≤ ∥f∥L∞(Eρ)
Y
k∈supp(n)
ρ−nk+1 k
(ρk −1) 2 (nk+1)
Y
k∈supp(n)
(2nk+1)1/p−1/2ζ(ω k)(2/p−1)nk
Therefore
∥˜cn∥Y ≤ ∥f∥L∞(Eρ)dn,

SM10B. ADCOCK, S. BRUGIAPAGLIA AND X. W ANG
where
dn =
Y
k∈supp(n)
ξ(ρk)ρ−nk k rnk p,k(cnk + 1)γ
and
ξ(ρ) = ρ (ρ−1) 2 , r p,k =ζ(ω k)2/p−1, c= 2, γ= 1/p+ 1/2.
We now apply Lemma SM1.4 withrreplaced byr p = (rp,k)k∈N to see thatd∈ℓ p(F)
with
∥d∥p ≤C(b, ε,rp, p, c, γ, ξ) =C(b, ε,ω, p),
sinceb⊙r p ∈ℓ p(N) and∥b⊙(r p −1)∥ 1 < εby assumption. This gives the first
result.
For the second result, we use Lemma SM1.1. This implies thatσ k(c)q,w ≤
∥c∥p,w;Y k1/q−1/p for anyq∈(p,2]. Moreover, inspecting its proof, we see that the
upper bound is achieved by∥c−c S∥q,w;Y , where the setSsatisfies|S| w ≤kand is
chosen independently ofq(andp), and depending only oncandw.
Proof of Theorem SM1.3.Letdbe the sequence defined in the previous proof.
We now appeal to Lemma SM1.5 withrreplaced byr p to see thatd∈ℓ p A(F), since
b⊙r p ∈ℓ p M(N) and∥b⊙(r p −1)∥ 1 < εby assumption. The result now follows.
SM1.3. Proof of Theorem 3.2.We shall prove the following generalization of
Theorem 3.2, which allows for Hilbert-valued functions. For this theorem, we define
the Hilbert-valued version of the distribution shift constant (3.1) for model classes
ofY-valued functionsP:D→ Ysimply by replacing the Lebesgue norms in (3.1)
by Lebesgue-Bochner norms. Given a setS⊂ F, we also define the corresponding
subspace ofY-valued polynomials by
PS;Y =
( X
n∈S
cnΨn :c n ∈ Y, S∈ S
)
.
TheoremSM1.6.Letϱbe the uniform probability measure on[−1,1] N,ω≥1
andD ω be as in(1.3). Suppose thatf∈ H(b, ε;Y), wherebsatisfies(3.3)for some
0< p <1. Then, for everyk >0, there exists a setSdepending onb,ε,ωandk
with|S| ≤ksuch that
(SM1.19) ∆(P S;Y ;ϱ, µ)≤
√
k
and ag∈ PS;Y such that
∆(PS;Y ;ϱ, µ)∥f−g∥ L2ϱ(RN;Y) +∥f−g∥ L∞µ (RN;Y) ≤C(b, ε,ω, p)k1−1/p
for any probability measureµsupported inD ω.
Proof of Theorem SM1.6.Define the weightsu= (u n)n∈F andw= (w n)n∈F ,
whereu n andw n are as in (SM1.5) and (SM1.6), respectively. LetS⊂ F,|S| ≤s, be
an index set (we will chooseSlater) and consider first the constant ∆(P S;Y ;ϱ, µ). For

SUPPLEMENTARY MATERIALS: STABLE EXTRAPOLATION IN LEARNINGSM11
anyP= P n∈S cnΨn ∈ PS;Y , the triangle inequality, (SM1.6), the Cauchy–Schwarz
inequality and Parseval’s identity give that
∥P∥ L∞µ (RN) ≤
X
n∈S
|cn|wn ≤
p
|S|w∥P∥ L2ϱ(RN).
SinceP S;Y is a linear space andP∈ P S;Y was arbitrary, it follows that
∆(PS;Y ;ϱ, µ)≤
p
|S|w.
Now letP=f S be as in (2.3). Then, by Parseval’s identity and the definition of the
ℓ2 w-norm,
∥f−P∥ L2ϱ(RN;Y) =∥c−c S∥2;Y =∥c−c S∥2,w;Y ,
and by the triangle inequality and (SM1.6),
∥f−P∥ L∞ϱ (RN;Y) ≤
X
n/∈S
wn∥cn∥Y =∥c−c S∥1,w;Y .
Combining with (SM1.19), we deduce that
∆(PS;Y ;ϱ, µ)∥f−P∥ L2ϱ(RN;Y) +∥f−P∥ L∞µ (RN;Y) ≤
p
|S|w∥c−c S∥2,w;Y +∥c−c S∥1,w;Y .
Now, the assumption (3.3) and Theorem SM1.2 imply that there is a setSwith
|S|w ≤ksuch that∥c−c∥ q,w;Y ≤C(b, ε,ω, p)k1/q−1/p for anyq∈(p,2]. We now
substitute this into the previous expression usingq= 1,2 to get
(SM1.20)
∆(PS;Y ;ϱ, µ)∥f−P∥ L2ϱ(RN;Y) +∥f−P∥ L∞µ (RN;Y) ≤ ∥c∥p,w;Y k1−1/p,whereP=f S.
The weightsw≥1and therefore|S| ≤ |S| w ≤k. The result now follows.
SM1.4. Proof of Theorem 4.1.We now prove a generalization of Theorem
4.1. The arguments for this proof are inspired by existing compressed sensing ap-
proaches to polynomial approximation of high-dimensional functions [SM30, SM29,
SM6, SM4, SM8], although with substantial differences in order to derive out-of-
distribution generalization bounds. Furthermore, we also extend the setting of The-
orem 4.1 to consider the approximation of Hilbert-valued functions, as opposed to
scalar-valued functions. This will be of use later when we consider operator learning.
Givenk >0 (its precise value will be chosen in the proof), let
(SM1.21) Λ =


n= (n j)∞ j=1 ∈ F:
∞Y
j=1
(nj + 1)≤ ⌈k⌉, nj = 0,∀j >⌈k⌉


 .
and define the set
(SM1.22)S={S⊆Λ :|S| w ≤k}.
Another aspect we deal with in this section is the case whereYis discretized to
some subspace ˆY, which we consider a Hilbert space with the same norm. This is
relevant for computations – as in practice, one can never work overYwhen it is

SM12B. ADCOCK, S. BRUGIAPAGLIA AND X. W ANG
infinite dimensional – and relevant later in the context of operator learning. To this
end, we now define LetP S; ˆY = S S∈S PS; ˆY . Now consider a Hilbert-valued function
f:D→ Ywith training data
(SM1.23) (x i, yi), i= 1, . . . , m,whereyi =f(x i) +e i ∈ Y
ande i ∈ Yrepresents measurement noise. We now consider the Hilbert-valued non-
linear least-squares fit
(SM1.24) min
P∈P S; ˆY
1
m
mX
i=1
∥yi −P(x i)∥2 Y .
The main objective of this section is to establish the following extension of Theorem
4.1 (the latter corresponds to the caseY= ˆY=R). For this and subsequent results,
we require several additional concepts. First, we let ˆBY :Y → ˆYbe the orthogonal
projection onto ˆY. Second, given an optimization problem min t g(t) and scalarsσ≥1
andτ≥0, we say that ˆtis a (σ, τ)-minimizerifg( ˆt)≤σ 2 mint g(t) +τ 2.
TheoremSM1.7.Letk≥1,τ >0,σ≥1,0< ϵ <1,ω≥1andD ω be
as in(1.3). Letf∈ H(b, ε;Y), wherebsatisfies(4.2)for some0< p <1, draw
x1, . . . ,xm ∼i.i.d ϱ, wheremsatisfies
m≥c·k·

log4(2k) + log(1/ϵ) 
for some universal constantc >0. Then, with probability at least1−ϵ, any(σ, τ)-
minimizer ˆfof(SM1.24)satisfies
∥f− ˆf∥ L∞µ (RN;Y) ≲ σC(b, ε,ω, p)√ϵ k1−1/p + σ
√
k√ϵ ∥f− ˆBY ◦f∥ L2ϱ(RN;Y) + σ
√
k∥e∥2;Y√m + √ kτ,
wheree= (e i)m i=1 ∈ Ym, for any probability measureµsupported inD ω.
To prove this result, we require several lemmas.
LemmaSM1.8.Letω≥1,D ω be as in(1.3),f∈C(D ω;Y),x 1, . . . ,xm ∈D
and define
(SM1.25)α= inf



q
1
m
Pm
i=1 ∥P1(xi)−P 2(xi)∥2 Y
∥P1 −P 2∥L2ϱ(RN;Y)
:P 1, P2 ∈ PS; ˆY , P1 ̸=P 2


 .
Suppose thatα >0and let ˆfbe a(σ, τ)-minimizer of(SM1.24). Then
∥f− ˆf∥ L∞µ (RN;Y) ≤ √ 2k
"
∥f− ˆBY ◦f∥ L2ϱ(RN;Y) +α −1(σ+ 1)
vuut 1
m
mX
i=1
∥f(x i)− ˆBY ◦f(x i)∥ 2 Y
+ 2∥f−P∥ L2ϱ(RN;Y) +α −1(σ+ 1)
vuut 1
m
mX
i=1
∥f(x i)−P(x i)∥2 Y
+α −1(σ+ 1) ∥e∥2;Y√m +α −1τ
#
+∥f−P∥ L∞µ (RN;Y) .
for allP∈ P S;Y and any probability measureµsupported inD ω.

SUPPLEMENTARY MATERIALS: STABLE EXTRAPOLATION IN LEARNINGSM13
Notice that this error bound is with respect to polynomialsP∈ P S;Y , and not
P∈ P S; ˆY , which is the space over which the minimization problem (SM1.24) is
formulated. This is critical in establishing Theorem SM1.7.
Proof.LetP∈ P S;Y be arbitrary and observe that ˆBY ◦P∈ PS; ˆY . Then
∥f− ˆf∥ L2ϱ(RN;Y) ≤ ∥f−ˆBY ◦f∥ L2ϱ(RN;Y) +∥ ˆBY ◦f− ˆBY ◦P∥ L2ϱ(RN;Y) +∥ ˆBY ◦P− ˆf∥ L2ϱ(RN;Y)
For the middle term, we use the fact that ˆBY is an orthogonal projection, and for the
third term, we use the fact that ˆBY ◦P, ˆf∈ PS;Y to get
∥f− ˆf∥ L2ϱ(RN;Y) ≤ ∥f− ˆBY ◦f∥ L2ϱ(RN;Y) +∥f−P∥ L2ϱ(RN;Y)
+α −1
vuut 1
m
mX
i=1
∥ ˆBY ◦P(x i)− ˆf(x i)∥ 2 Y . (SM1.26)
Now write the training labelsy i in (SM1.23) as
yi = ˆBY ◦f(x i) +e ′ i,wheree ′ i =f(x i)− ˆBY ◦f(x i) +e i.
Then for the third term above, the triangle inequality and the fact that ˆfis an
approximate minimizer give
vuut 1
m
mX
i=1
∥ ˆBY ◦P(x i)− ˆf(x i)∥ 2 Y
≤
vuut 1
m
mX
i=1
∥yi − ˆf(x i)∥ 2 Y +
vuut 1
m
mX
i=1
∥ ˆBY ◦P(x i)− ˆBY ◦f(x i)∥ 2 Y + 1√m ∥e′∥2;Y
≤σ
vuut 1
m
mX
i=1
∥yi − ˆBY ◦P(x i)∥ 2 Y +
vuut 1
m
mX
i=1
∥ ˆBY ◦P(x i)− ˆBY ◦f(x i)∥ 2 Y + 1√m ∥e′∥2;Y +τ
≤(σ+ 1)
vuut 1
m
mX
i=1
∥P(x i)−f(x i)∥2 Y + σ+ 1√m ∥e′∥2;Y +τ
≤(σ+ 1)
vuut 1
m
mX
i=1
∥P(x i)−f(x i)∥2 Y + (σ+ 1)
vuut 1
m
mX
i=1
∥f(x i)− ˆBY ◦f(x i)∥ 2 Y
+ σ+ 1√m ∥e∥2;Y +τ.
Here, in the penultimate step we used the fact that ˆBY is an orthogonal projection,
and in the final step we used the definition ofe ′. Substituting this into (SM1.26) now

SM14B. ADCOCK, S. BRUGIAPAGLIA AND X. W ANG
gives that
∥f− ˆf∥ L2ϱ(RN;Y) ≤ ∥f− ˆBY ◦f∥ L2ϱ(RN;Y) +∥f−P∥ L2ϱ(RN;Y)
+α −1(σ+ 1)
vuut 1
m
mX
i=1
∥P(x i)−f(x i)∥2 Y
+α −1(σ+ 1)
vuut 1
m
mX
i=1
∥f(x i)− ˆBY ◦f(x i)∥ 2 Y +α −1(σ+ 1) ∥e∥2;Y√m +α −1τ.
Now observe that ˆf−P∈ P S′;Y for some setS ′ with|S ′|w ≤2k. Using (SM1.19)
withS ′ we get ∆(P S′;Y ;ϱ, µ)≤ √ 2k. We now apply (3.2) (or, more precisely, the
Hilbert-valued extension of this bound, which is proved in exactly the same way) to
deduce that
∥f− ˆf∥ L∞µ (RN;Y) ≤ √ 2k  ∥f−P∥ L2ϱ(RN;Y) +∥f− ˆf∥ L2ϱ(RN;Y)  +∥f−P∥ L∞µ (RN;Y) .
Combining this with the previous estimate now gives the result.
LemmaSM1.9.Let0< ϵ <1,x 1, . . . ,xm ∼i.i.d. ϱand consider the constantα
defined in(SM1.25). Suppose thatk≥1. ThenP(α <1/2)≤ϵ, provided
(SM1.27)m≥c·k·

log4(2k) + log(1/ϵ)  ,
wherec >0is a universal constant.
Proof.LetP 1, P2 ∈ PS;Y be arbitrary and observe thatP 1 −P 2 can be expressed
asP 1 −P 2 = P n∈S′ cnΨn whereS ′ ⊆Λ,|S ′|w ≤2k. Definec n = 0∈ Yforn/∈S ′.
Now{ψ j}j be an orthonormal basis ofYand writec n = P j dn,jψj ford n,j ∈R. Let
dj = (dn,j)n∈Λ. Then, by Parseval’s identity,
∥P1 −P 2∥2 L2(RN;Y) = X
n∈Λ
∥cn∥2 Y = X
n∈Λ
X
j
|dn,j|2 = X
j
∥dj∥2 2,
and
1
m
mX
i=1
∥P1(xi)−P 2(xi)∥2 Y = X
j
∥Adj∥2 2,
whereA∈R m×N is the matrixA= 1√m (Ψn(xi))i∈[m],n∈Λ. We deduce that
α≥inf
z∈T
∥Az∥2,whereT=

z= (z n)n∈Λ ∈R N ,∥z∥ 2 = 1,|supp(z)| w ≤2k 	 .
Notice thatT⊆ {z:∥z∥ 1,w ≤
√
2k}by the Cauchy–Schwarz inequality. Now define
the random vectorX∈R N byX= (Ψ n(x))n∈Λ forx∼ϱand observe that
(SM1.28)E|⟨X,z⟩| 2 =∥z∥ 2 2
by Parseval’s identity, and also that
|⟨X,e n⟩| ≤ ∥Ψn∥L∞ϱ (RN) =u n ≤w n,∀n∈Λ,

SUPPLEMENTARY MATERIALS: STABLE EXTRAPOLATION IN LEARNINGSM15
almost surely, due to (SM1.5) and (SM1.6). We now apply [SM11, Thm. 2.13]. This
gives that there are univeral constantsκ, c0, c1 >0 such that, if
(SM1.29)m≥c 0 ·δ −2 ·k·log(e|Λ|)·log 2(k/δ) log2(1/δ)
for someδ∈(0, κ), then
sup
z∈T

 1 m mX i=1 |⟨Xi,z⟩| 2 −E|⟨X,z⟩| 2

 ≤c 1δ  1 + sup z∈T E|⟨X,z⟩| 2 
with probability at least 1−2 exp(−c 2δ2m/k), whereX 1, . . . ,Xm are independent
copies ofX. Notice that 1 m Pm i=1 |⟨Xi,z⟩| 2 =∥Az∥ 2 2. Using this, (SM1.28) and
rearranging, we see that
α2 ≥inf
z∈T
∥Az∥2 2 ≥1−2c 1δ,
with the same probability. Setδ= min{κ/2,3/(8c 1)}. Then we see that
P(α <1/2)≤2 exp(−c 2δ2m/k),
provided (SM1.29) holds with this value ofδ. ThereforeP(α <1/2)< ϵ, provided
(SM1.29) holds, along with
m≥c −1 2 ·δ −2 ·k·log(2/ϵ)
for the given value ofδ. In particular, it suffices for
(SM1.30)m≥c 3 ·k·

log(e|Λ|)·log 2(2k) + log(1/ϵ)  ,
providedk≥1. A standard bound (see, e.g., the proof of [SM5, Lem. 6.4]) gives that
log(E|Λ|)≤4 log 2(e⌈k⌉)≤4 log 2(2ek). Hence (SM1.30) is implied by
(SM1.31)m≥c 4 ·k·

log4(2k) + log(1/ϵ)  .
This complete the proof.
We are now ready to establish Theorem SM1.7.
Proof of Theorem SM1.7.For a suitable choice of the universal constantcwe
see that (SM1.27) holds withϵreplaced byϵ/3. Hence Lemma SM1.9 gives that
P(α <1/2)≤ϵ/3. We now apply Lemma SM1.8 to deduce that
∥f− ˆf∥ L∞µ (RN;Y) ≲ √ k
"
∥f− ˆBY ◦f∥ L2ϱ(RN;Y) +σ
vuut 1
m
mX
i=1
∥f(x i)− ˆBY ◦f(x i)∥ 2 Y
+∥f−P∥ L2ϱ(RN;Y) +σ
vuut 1
m
mX
i=1
∥f(x i)−P(x i)∥2 Y +σ ∥e∥2;Y√m +τ
#
+∥f−P∥ L∞µ (RN;Y)
(SM1.32)
for allP∈ P S , with probability at least 1−ϵ/3.

SM16B. ADCOCK, S. BRUGIAPAGLIA AND X. W ANG
We next fix a suitableP. LetS⊂ F,|S| w ≤k, be the set specified in Theorem
SM1.2 (notice that (SM1.7) holds by assumption). Now writeS=S 1 ∪S 2, where
S1 =S∩Λ andS 2 =S∩Λ c. Notice that|S i|w ≤k,i= 1,2, and thereforeS 1 ∈ S.
Finally, letP=f S1 . Now consider the middle term of (SM1.32). LetXbe the
random variable 1 m Pm i=1 ∥P(x i)−f(x i)∥2 Y and notice thatE(X) =∥f−P∥ 2 L2ϱ(RN;Y) .
Hence Markov’s inequality gives that
P


vuut 1
m
mX
i=1
∥P(x i)−f(x i)∥2 Y ≥ ∥f−P∥ L2ϱ(RN;Y) p ϵ/3

 ≤ϵ/3.
Similarly, Markov’s inequality also gives that
P


vuut 1
m
mX
i=1
∥f(x i)− ˆBY ◦f(x i)∥ 2 Y ≥ ∥f− ˆBY ◦f∥ L2ϱ(RN;Y) p ϵ/3   ≤ϵ/3.
Using these two estimates, (SM1.32) and the union bound, we deduce that
∥f− ˆf∥ L∞µ (RN;Y) ≲ √ k  σ√ϵ ∥f− ˆBY ◦f∥ L2ϱ(RN;Y) + σ√ϵ ∥f−f S1 ∥L2ϱ(RN;Y) +σ ∥e∥2;Y√m +τ 
+∥f−f S1 ∥Lµ ϱ (RN;Y)
(SM1.33)
with probability at least 1−ϵ.
Finally, we bound the two terms involvingf−f S1 in (SM1.33). Letc= (c n)n∈F
be the coefficients off. SinceS 1 =S∩Λ, we have
∥f−f S1 ∥L2ϱ(RN;Y) =∥c−c S1 ∥2;Y
≤ ∥c−cS∥2;Y +∥c−c Λ∥2;Y
=∥c−c S∥2,w;Y +∥c−c Λ∥2,w;Y ,
wherew= (w n)n∈F is as in (SM1.6) and
∥f−f S1 ∥L∞µ (RN;Y) =∥c−c S1 ∥1,w ≤ ∥c−cS∥1,w;Y +∥c−c Λ∥1,w;Y .
By definition ofS, Theorem SM1.2 gives that
∥c−c S∥q,w;Y ≤C(b, ε,ω, p)k1/q−1/p
for allq∈(p,2]. Theorem SM1.3 (notice that (SM1.8) holds by assumption) implies
that there exists an anchored setTwith|T| ≤ ⌈k⌉such that
∥c−c T ∥q,w;Y ≤C(b, ε,ω, p)⌈k⌉1/q−1/p
for allq∈(p,2]. Moreover, Λ contains all anchored sets of size at mostn[SM6, Prop.
2.18]. HenceT⊆Λ and we deduce that
∥c−c Λ∥q,w;Y ≤C(b, ε,ω, p)⌈k⌉1/q−1/p

SUPPLEMENTARY MATERIALS: STABLE EXTRAPOLATION IN LEARNINGSM17
for allq∈(p,2]. Combining the various estimates, we conclude that
∥f−f S1 ∥L2ϱ(RN;Y) ≤C(b, ε,ω, p)k1/2−1/p,∥f−f S1 ∥L∞µ (RN;Y) ≤C(b, ε,ω, p)k1−1/p.
Substituting this into (SM1.33) we get
(SM1.34)
∥f− ˆf∥ L∞µ (RN;Y) ≤ σ√ϵ C(b, ε,ω, p)k1−1/p+ σ
√
k√ϵ ∥f− ˆBY ◦f∥ L2ϱ(RN;Y) + σ
√
k∥e∥2√m + √ kτ.
with probability at least 1−ϵ, as required.
Proof of Theorem 4.1.Letcbe the constant from Lemma SM1.9 and assume,
without loss of generality, thatc≥1/log 4(2). Set
(SM1.35)k= m c  log4(m) + log(1/ϵ)  .
Notice thatk≤m/(clog 4(2)) wheneverm≥2 and thereforek≤m. Now let
¯m= ¯m(ϵ)∈Nbe the smallestm∈N,m≥2, such thatk≥1. LetY= ˆY=Rwith
the Euclidean inner product, so that, in particular, ˆBY =I Y is the identity. We now
apply Theorem SM1.7 with this value ofk,σ= 1 andτ= 0. This yields the result.
SM1.5. Proofs of Theorems 4.4 and 5.6.We now prove Theorems 4.4 and
5.6. Our main focus in the proof of Theorem 5.6, since Theorem 4.4 will then follow
as a special case.
Our broad approach is based on well-established technique of emulation of poly-
nomials via DNNs, or in this case, DNOs, [SM5, SM18, SM20, SM21, SM24, SM33,
SM31, SM25, SM28, SM32] (see [SM3,§7.1] for a review). As noted earlier, emulation
techniques are normally used to assert the existence of DNNs/DNOs with certain
approximation guarantees. Conversely, we follow ideas developed in [SM2, SM5, SM7]
that emulate a whole polynomial training problem as a DNO training problem, thus
showing the existence of DL strategies with guaranteed error bounds.
Our proof proceeds in three steps. These steps are broadly similar to those used
in [SM7], which develops generalization bounds learning holomorphic operators, but
considers only the in-distribution setting. Our results generalize these by considering
arbitrary test distributions. First, we introduce the polynomial training problem
(SM1.36) min
P∈P S; ˆY
1
m
mX
i=1
∥Yi −P◦ ˆEX (Xi)∥ 2 Y ,
whereSis as defined in (SM1.22) with Λ as in (SM1.21). The second step is to then
emulate the relevant polynomials in the hypothesis class a DNOsN(§SM1.5.1). Next,
we show that the weights corresponding to an approximate minimizer of the associated
DNO training problem yield coefficients of a polynomial that is an approximate min-
imizer of (SM1.36) (§SM1.5.2). Using this, we establish a general out-of-distribution
error bound for the DNO training problem, based on the analogous bound for the
polynomial training problem. Finally, we specialize this to the settings of Theorems
4.4 and 5.6 to conclude the proof (§SM1.5.3).
SM1.5.1. Construction ofN.Let 0< k≤d X be a number whose value will
be chosen later. We first require the following lemma.

SM18B. ADCOCK, S. BRUGIAPAGLIA AND X. W ANG
LemmaSM1.10.LetΓ⊆Λandm(Γ) = max n∈Γ ∥n∥1 <∞. Then there exists a
fully-connected familyN o of tanh DNNsR ⌈k⌉ →Rwith
width(No)≲m(Γ),depth(N o)≲log(m(Γ)),
such that, for any0< δ <1,ω≥1andn∈Γ, there is aN n ∈ No satisfying
sup
x∈Dω
|Nn(x)−Ψ n(x)| ≤δ.
Moreover, the zero network0 :x7→0also belongs toN o (trivially, sincetanh(0) = 0).
Note here we slightly abuse notation and consider the DNNsN n both as maps
with domainR ⌈k⌉ and maps with domainR N that depend only on the first⌈k⌉entries
of the given input. This is permissible, since the Legendre polynomials Ψ n,n∈Λ,
depend on the first⌈k⌉variables only. This lemma is based on [SM7, Lem. D.9],
which is itself based on [SM18, SM28]. Notice that [SM7, Lem. D.9] considers only
the domainD=D 1. However, the proof extends toω≥1. In particular, the width
and depth bounds do not depend onω(although the weights and biases ofN n do).
This is a particular feature of tanh DNNs, which makes them particularly desirable
over, for instance, ReLU DNNs for out-of-distribution generalization.
Now fixδ >0 (its value will be chosen later in the proof), let Γ =∪ S∈S SandN o
andN n,n∈Γ, be as in the above lemma. We now estimatem(Γ). Letn∈Γ. Since
n∈Sfor someS∈ Sand, by construction,|S| w ≤k, we have
∞Y
j=1
(2nj + 1)ζ(ωj)2nj =w 2 n ≤k.
Sinceζ(ω) =ω+
√
ω2 −1≥ω, it follows that
∥n∥1 exp(2∥n∥1 log(ωmin))≤k,
whereω min = min{ωj}>1 by assumption, and therefore
m(Γ)≲ log(k) log(ωmin) .
Notice that|S| ≤ |S|w ≤kfor anyS∈ S. We now define the familyNof DNNs
N:R dX →R dY as
N=


 N=C


Nn1
...
Nn|S|
0
...
0

 :S={n 1, . . . ,n|S|} ∈ S,C∈RdY ×⌈k⌉


 .
Here 0 denotes the zero network. As before, we slightly abuse notation by allowingN
to be a function whose domain is eitherR ⌈k⌉,R dX orR ∞ depending on the context.
Notice that this family satisfies
(SM1.37) width(N)≤width(N o) max S∈S |S|≲km(Γ)≲ klog(k) log(ωmin)

SUPPLEMENTARY MATERIALS: STABLE EXTRAPOLATION IN LEARNINGSM19
and
(SM1.38) depth(N)≤depth(N o)≲log(m(Γ))≲log
 log(k)
log(ωmin)

.
Finally, givenN∈ Nand its associated matrixC∈R dY ×⌈k⌉. Letc 1, . . . ,c⌈k⌉ denote
the columns ofC, so thatNcan be expressed as
N=
|S|X
i=1
ciNni .
Moreover, we have
ˆDY ◦N=
|S|X
i=1
ˆDY (ci)Nni =
|S|X
i=1
ciNni ,wherec i ∈ ˆY,
where ˆY= ˆDY (RdY )⊆ Y. Therefore, we can associateNwith the space of functions
QS; ˆY given by
QS; ˆY =
( X
n∈S
cnNn :c n ∈ ˆY, S∈ S
)
.
SM1.5.2. Polynomial training problem and approximate DNN mini-
mizers.We first require the following lemma.
LemmaSM1.11.LetS,{N n}n∈Γ be as defined above and(Z,∥ · ∥Z )be a Hilbert
space. LetS∈ Sand suppose that
p=
X
n∈S
cnΨn,˜p=
X
n∈S
cnNn,
wherec n ∈ Z. Then
sup
x∈Dω
∥p(x)−˜p(x)∥Z ≤δ
p
|S|∥p∥L2ϱ(RN;Z) .
Proof.We have
∥p(x)−˜p(x)∥Z ≤
X
n∈S
∥cn∥Z |Ψn(x)−N n(x)| ≤δ
X
n∈S
∥cn∥Z .
The result now follows from the Cauchy–Schwarz inequality and Parseval’s identity.
We now show that approximate minimizers of the DNO training problem yield
approximate minimizers of the polynomial training problem.
LemmaSM1.12.Suppose thatα >0, whereαis as in(SM1.25)withYreplaced
by ˆY, letNbe the DNN model class defined above and ˆNbe any(σ, τ)-approximate
minimizer of(5.3). Write
DY ◦ ˆN= X
n∈S
ˆcnNn ∈ QS; ˆY

SM20B. ADCOCK, S. BRUGIAPAGLIA AND X. W ANG
whereS∈ Sandˆc n ∈ ˆY, and define the polynomial
ˆP= X
n∈S
ˆcnΨn ∈ PS; ˆY .
Then ˆPis a(σ ′, τ′)-approximate minimizer of(SM1.36), where
σ′ ≤σ(1 +δ √ k/α)
τ ′ ≤τ+ σδ
√
k
α

∥F∥ L∞ν (X;Y) + 1√m ∥E∥2;Y

+δ
√
k∥ ˆP∥ L2ϱ(RN;Y) . (SM1.39)
Proof.LetP= P n∈S cnΨn ∈P S; ˆY be arbitrary andN∈ Nbe such that
ˆDY ◦N= P n∈S cnNn. Then
vuut 1
m
mX
i=1
∥Yi − ˆP◦ ˆEX (Xi)∥ 2 Y ≤
vuut 1
m
mX
i=1
∥Yi − ˆDY ◦ ˆN◦ ˆEX (Xi)∥ 2 Y
+
vuut 1
m
mX
i=1
∥ ˆP◦ ˆEX (Xi)− ˆDY ◦ ˆN◦ ˆEX (Xi)∥ 2 Y
≤σ
vuut 1
m
mX
i=1
∥Yi − ˆDY ◦N◦ ˆEX (Xi)∥ 2 Y +τ
+
vuut 1
m
mX
i=1
∥ ˆP◦ ˆEX (Xi)− ˆDY ◦ ˆN◦ ˆEX (Xi)∥ 2 Y
≤σ
vuut 1
m
mX
i=1
∥Yi −P◦ ˆEX (Xi)∥ 2 Y +τ
+
vuut 1
m
mX
i=1
∥ ˆP◦ ˆEX (Xi)− ˆDY ◦ ˆN◦ ˆEX (Xi)∥ 2 Y
+σ
vuut 1
m
mX
i=1
∥P◦ ˆEX (Xi)− ˆDY ◦N◦ ˆEX (Xi)∥ 2 Y
and therefore
vuut 1
m
mX
i=1
∥Yi − ˆP◦ ˆEX (Xi)∥ 2 Y ≤σ
vuut 1
m
mX
i=1
∥Yi −P◦ ˆEX (Xi)∥ 2 Y +τ
+∥ ˆP− ˆDY ◦ ˆN∥ L∞µ (RN;Y) +σ∥P− ˆDY ◦N∥ L∞µ (RN;Y) ,
where we recall that ˆEX (Xi)∈Dby Assumption 5.1(ii). We now apply Lemma

SUPPLEMENTARY MATERIALS: STABLE EXTRAPOLATION IN LEARNINGSM21
SM1.11 to the latter two terms to get, after recalling that|S| ≤ksinceS∈ S,
vuut 1
m
mX
i=1
∥Yi − ˆP◦ ˆEX (Xi)∥ 2 Y ≤σ
vuut 1
m
mX
i=1
∥Yi −P◦ ˆEX (Xi)∥ 2 Y +τ
+δ
√
k∥ ˆP∥ L2ϱ(RN;Y) +σδ √ k∥P∥ L2ϱ(RN;Y) .
It remains to estimate the final term. Applying (SM1.25) withP 1 =PandP 2 = 0,
we get
∥P∥ L2 ϱ(RN;Y) ≤α −1
vuut 1
m
mX
i=1
∥P◦ ˆEX (Xi)∥ 2 Y
≤α −1
vuut 1
m
mX
i=1
∥Yi −P◦ ˆEX (Xi)∥ 2 Y +α −1
vuut 1
m
mX
i=1
∥Yi∥2 Y
≤α −1
vuut 1
m
mX
i=1
∥Yi −P◦ ˆEX (Xi)∥ 2 Y +α −1∥F∥ L∞ν (X;Y) + α−1 √m ∥E∥2;Y .
Substituting this into the previous expression and recalling thatPwas arbitrary now
gives the result.
With this to hand, we now establish the following general out-of-distribution error
bound for the DNO training problem.
TheoremSM1.13 (Out-of-distribution generalization bound for the DNO train-
ing problem).Let1≤k≤d X ,τ >0,σ≥1,0< ϵ <1andNbe the DNN
model class defined above, whereδsatisfiesδ≤(4
√
k)−1. Suppose that Assump-
tion 5.1 holds and Assumption 5.3 holds withω≥1satisfyingω min = min{ω j}>
1. LetF∈ H(b, ε,X,Y), wherebsatisfies(4.2)for some0< p <1, and draw
X1, . . . , Xm ∼i.i.d. ν, wheremsatisfies
m≥c·k·

log4(2k) + log(1/ϵ) 
for some universal constantc >0. Then, with probability at least1−ϵ, any(σ, τ)-
approximate minimizer ˆNof(5.3)is such that the approximation ˆF= ˆDY ◦ ˆN◦ ˆEX
satisfies
∥F− ˆF∥ L∞µ (X;Y) ≲ σC(b, ε,ω, p)√ϵ k1−1/p + σ
√
k√ϵ ∥F− ˆBY ◦F∥ L2ν (X;Y) + σ
√
k∥E∥ 2;Y√m
+
√
kτ+σδk,
whereE= (E i)m i=1 ∈ Ym. Further, the classNsatisfies
width(N)≲ klog(k) log(ωmin) ,depth(N)≲log  log(k) log(ωmin)  .
Proof.The width and depth bounds forNfollow immediately from the construc-
tion and (SM1.37)-(SM1.38). We divide the remainder of the proof into a series of
steps.

SM22B. ADCOCK, S. BRUGIAPAGLIA AND X. W ANG
Step 1: Reduction to polynomials.Let ˆPbe as in Lemma SM1.12. Then
(SM1.40)
∥F− ˆF∥ L∞µ (X;Y) ≤ ∥F−ˆP◦ ˆEX ∥L∞µ (X;Y) +∥ ˆP◦ ˆEX − ˆDY ◦ ˆN◦ ˆEX ∥L∞µ (X;Y) .
For the second term, we recall first that ˆPand ˆNdepend on the first⌈k⌉ ≤d X
variables only. Therefore, we can write
∥ ˆP◦ ˆEX − ˆDY ◦ ˆN◦ ˆEX ∥L∞µ (X;Y) =∥ ˆP− ˆDY ◦ ˆN∥ L∞ EX ♯µ(RN;Y)
We now apply Lemma SM1.11 to get
(SM1.41)
∥ ˆP◦ ˆEX − ˆDY ◦ ˆN◦ ˆEX ∥L∞µ (X;Y) ≤δmax S∈S
p
|S|∥P∥ L2ϱ(RN;Y) ≤δ
√
k∥ ˆP∥ L2ϱ(RN;Y) .
For the first term of (SM1.40), we writef=F◦ D X :R ∞ → Yand recall that ˆP◦ ˆEX = ˆP◦ EX to get
∥F− ˆP◦ ˆEX ∥L∞µ (X;Y) =∥f− ˆP∥ L∞ EX ♯µ(RN;Y) .
Hence
∥F− ˆF∥ L∞µ (X;Y) ≤ ∥f−ˆP∥ L∞ EX ♯µ(RN;Y) +δ √ k∥ ˆP∥ L2ϱ(RN; ˆY) .
Step 2: ˆPis an approximate minimizer.Since ˆPcomes from Lemma SM1.12, it is a
(σ′, τ′)-minimizer of (SM1.36), where (σ ′, τ′) are given by (SM1.39). Recall that any
P∈ PS; ˆY depends on the first⌈k⌉entries of an inputx. Sincek≤d X , we see that
P◦ ˆEX (Xi) =P(x i), wherex i =E X (Xi) is a uniformly distributed random variable
onD= (−1,1) N. We also haveF(X i) =f(x i) and thereforeY i =F(X i) +Ei is equal
toy i =f(x i) +e i withE i =e i. Hence (SM1.36) is equivalent to (SM1.24).
The conditions of Theorem SM1.7 hold by assumption, hence we may apply it
withϵto deduce that
∥f− ˆP∥ L∞µ (RN;Y) ≲ σ′C(b, ε,ω, p)√ϵ k1−1/p + σ′√ k√ϵ ∥f− ˆBY ◦f∥ L2ϱ(RN;Y)
+
σ′√ k∥E∥ 2;Y√m + √ kτ ′,
whereE= (R N i )m i=1, with probability at least 1−ϵ/2. Plugging in the values (SM1.39)
forσ ′, τ′ combining with the previous bound, we deduce that
∥F− ˆF∥ L∞µ (X;Y) ≲ σ(1 +δ
√
k/α)C(b, ε,ω, p)√ϵ k1−1/p
+ σ(1 +δ
√
k/α)
√
k√ϵ ∥f− ˆBY ◦f∥ L2ϱ(RN;Y) + σ(1 +δ
√
k/α)
√
k∥E∥ 2;Y√m
+
√
kτ+ σδk α  ∥F∥ L∞ν (X;Y) + 1√m ∥E∥2;Y 
+δk∥ ˆP∥ L2ϱ(RN;Y) +δ √ k∥ ˆP∥ L2ϱ(RN;Y) ,

SUPPLEMENTARY MATERIALS: STABLE EXTRAPOLATION IN LEARNINGSM23
whereαis given by (SM1.25). Now recall from the proof of Theorem SM1.7α≥1/2 as
part of the probabilistic event that holds with probability at least 1−ϵthat guarantees
its main error bound. Sinceδ≤1/(4
√
k) by assumption, we obtain
∥F− ˆF∥ L∞µ (X;Y) ≲ σC(b, ε,ω, p)√ϵ k1−1/p + σ
√
k√ϵ ∥f− ˆBY ◦f∥ L2ϱ(RN;Y)
+
σ
√
k∥E∥ 2;Y√m + √ kτ+σδk  ∥F∥ L∞ν (X;Y) + 1√m ∥E∥2;Y 
+δk∥ ˆP∥ L2ϱ(RN;Y) .
(SM1.42)
Step 3: Estimating∥ ˆP∥ L2ϱ(RN;Y) The next step is to estimate the final term. Using
(SM1.25) and the fact that 0, ˆP∈ PS; ˆY , we get
∥ ˆP∥ L2ϱ(RN;Y) ≤α −1
vuut 1
m
mX
i=1
∥ ˆP(x i)∥ 2 Y
≤α −1
vuut 1
m
mX
i=1
∥ ˆDY ◦ ˆN(x i)∥ 2 Y +α −1∥ ˆDY ◦ ˆN− ˆP∥ L∞ϱ (RN;Y) .
We now use Lemma SM1.11 and the fact that ˆF= ˆDY ◦ ˆN◦ ˆEX to obtain
∥ ˆP∥ L2ϱ(RN;Y) ≤α −1
vuut 1
m
mX
i=1
∥ ˆF(x i)∥ 2 Y +α −1δ √ k∥ ˆP∥ L2ϱ(RN;Y) .
We now rearrange and use the facts that ˆFis as (σ, τ)-minimizer and the zero network
belongs toN, to get
∥ ˆP∥ L2ϱ(RN;Y) ≤ α−1 1−α −1δ √ k


vuut 1
m
mX
i=1
∥ ˆF(X i)−Y i∥ 2 Y + 1√m ∥Y∥ 2;Y


≤ α−1
(1−α −1δ √ k)
 1 +σ√m ∥Y∥ 2;Y +τ  .
We now recall thatα≥1/2,δ≤1/(4
√
k) andY i =F(X i) +E i. This gives
∥ ˆP∥ L2ϱ(RN;Y) ≲(1 +σ)∥F∥ L∞ν (X;Y) + 1 +σ√m ∥E∥2;Y +τ.
Substituting this into (SM1.42) and recalling thatδ≤1/(4
√
k) andσ≥1 we deduce
that
∥F− ˆF∥ L∞µ (X;Y) ≲ σC(b, ε,ω, p)√ϵ k1−1/p + σ
√
k√ϵ ∥f− ˆBY ◦f∥ L2ϱ(RN;Y) + σ
√
k∥E∥ 2;Y√m
+
√
kτ+σδk∥F∥ L∞ν (X;Y) .

SM24B. ADCOCK, S. BRUGIAPAGLIA AND X. W ANG
After rewriting
∥f− ˆBY ◦f∥ L2ϱ(RN;Y) =∥F− ˆBY ◦F∥ L2ν (X;Y)
and recalling that∥F∥ L∞ν (X;Y) ≤1 sinceF∈ H(b, ε;X,Y), we obtain the desired bound.
SM1.5.3. Final arguments.
Proof of Theorem 5.6.Letcbe the constant from Theorem SM1.13 and suppose,
without loss of generality, thatc≥1/log 4(2). We argue as in the proof of Theorem
4.1 and setkas in (SM1.35) and let ¯m= ¯m(ϵ) be the smallestm∈N,m≥2, such
thatk≥1. We now setδ= min{(4
√
k)−1,2 −m/k}and apply Theorem SM1.13 with
σ= 1 andτ= 0. This completes the proof.
Proof of Theorem 4.4.We will apply Theorem 5.6. LetY=Rwith the Euclidean
inner product andd Y = 1, so that ˆDY = ˆBY =I Y is the identity map. LetXbe any
separable, infinite-dimensional Hilbert space, (λ i)i∈N be any summable sequence with
λ1 ≥λ 2 ≥ · · ·>0 and{ϕi}i∈N ⊂ Xbe any orthonormal basis. Define the probability
measureνonXas the pushforwardν=D X ♯ϱ. Define the encoder ˆEX :X7→
(⟨X, ϕi⟩X /√λi)dX i=1. It is clear that Assumption 5.1 holds. Givenω>1withω min >1,
letNbe the DNN model class withn 0 =d X =⌈cm/L⌉andn M+1 =d Y = 1 whose
existence is established by Theorem 5.6. Now letf∈ H(b, ε) for somebsatisfying
(4.2) with 0< p <1 andx 1, . . . ,xm ∼i.i.d. ϱ, whereϱis the uniform probability
measure on (−1,1) N. LetX i =D X (xi) and notice thatX 1, . . . , Xm ∼i.i.d. ν. Further,
letF=f◦ E X and observe thatF∈ H(b, ε;X,Y). Then we can write
yi =f(x i) +e i =F(X i) +e i =:F(X i) +E i =:Y i
and observe that any minimizer ˆNof (4.1) is also a minimizer of (5.3). Now let
µbe an arbitrary probability measure onR N that is supported inD ω. Define the
measureυ=D X ♯µonXand notice thatυsatisfies Assumption 5.3. Observe that ˆF= ˆDY ◦ ˆN◦ ˆEX = ˆN◦ EX and therefore
∥f− ˆN∥ L∞µ (RN) =∥f◦ EX − ˆN◦ EX ∥L∞ DX ♯µ(X;R) =∥F− ˆF∥ L∞υ (X;R) ,
since ˆEX ◦ DX is the identity onR N. We now apply the error bound from Theorem
5.6 and notice that the second term vanishes since ˆBY =I Y .
SM2. F urther details on the numerical experiments.We now give full
details on the numerical experiments. First, we remark that all the experiments in
the paper compute a certain error versus number of training samplesm. We use
multiple trials and, following [SM6,§A.1.3], we display the geometric mean and one
geometric standard deviation. The number of trials is described below.
SM2.1. Polynomial estimators.For the experiments in§6.1, we compute the
relativeL ∞ µ (Rd)-norm error. Estimating this error accurately in high dimensions may
be challenging. We use a grid of size 10 4, drawn randomly and independently from
µ. However, since the functions in this section are sharply peaked near the bottom
left corner of any hyperrectangular region, we also augment this grid with the point
x= (−ω 1, . . . ,−ωd). We use a total of 30 trials in our experiments.
As mentioned, we employ an adaptive Least Squares (ALS) estimator. This
follows [SM26] (see also [SM27], which is based on techniques for the construct-
ing adaptive sparse grid quadratures [SM19]. ALS iteratively computes a sequence

SUPPLEMENTARY MATERIALS: STABLE EXTRAPOLATION IN LEARNINGSM25
of least-squares polynomial approximations ˆf (1), ˆf (2), . . .and corresponding (nested)
multi-index setsS (1) ⊆S (2) ⊆ · · · ⊂Nd 0, where ˆf (l) ∈ PS(l) ,∀l∈NandP S(l) is as in
(2.3).
We now describe how the one-step update in ALS is performed. This requires
several definitions. First, we define themarginof a multi-index setS⊆N d 0 as
M(S) =

n∈N d 0\S:∃j∈[d] :n−e j ∈S 	 ,
wheree j isjth canonical multi-index, and thereduced marginofSas the set
R(S) ={n= (ν j)d j=1 ∈ M(S) :∀j∈[d], νj ̸= 0⇒n−e j ∈S}.
Given a current multi-index setS⊂N d 0, ALS constructs a new set by selecting multi-
indicesR(S) using abulk chasing procedure, defined as follows. Lete:R(S)→R
and 0< β≤1 be a parameter. The functioneserves as an estimate for the true
polynomial coefficients of the function being approximated. We describe a precise
choice ofebelow. With this, the procedurebulk(R(S), e, β) computes a setT⊆ R(S)
of minimal positive cardinality such that
X
n∈T
e(n)≥β
X
n∈R(S)
e(n).
Now suppose at some iteration we have an multi-index setS⊂ Fand corresponding
least-squares approximation ˆf∈ PS based on sample pointsx 1, . . . ,xm. We define
e:R(S)→Ras the discrete residual
(SM2.1)e(n) =

 1 m mX i=1  f(x i)− ˆf(x i)  Ψn(xi)

 2 ,∀n∈ R(S).
We now computeT= bulk(R(S), e, β), construct the new index setS new =S∪T
and compute a new estimator ˆfnew as the least-squares polynomial approximation to
ffromP Snew .
The full ALS approximation is presented in Algorithm SM2.1. Note that, follow-
ing [SM27], we use the valueβ= 0.5 in our experiments. We also make the choice
m(l) =c d max{n(l) + 1,⌈n (l) ·log(n (l))⌉}, wherec d = 2 whend= 8 andc d = 1 other-
wise. The reason for the larger constant in lower dimensions is to avoid instability of
the least-squares system.
SM2.2. DNN estimators.For the experiments in§6.2, we compute the rela-
tiveL 2 µ(Rd)-norm error. We do this on a grid of size 10 4, drawn randomly and inde-
pendently fromµ. We use fully connected DNNs with the architecture and parameters
specified in Table SM1. For each training-set size, we perform 30 independent trials.
SM2.3. DNO estimators.We now describe the DNO setup for the experi-
ments in§6.3. As noted we use FNOs. Our setup and implementation is based
on [SM22, SM23].
Darcy flow.Details of the architecture and training parameters are given in Table
SM2. In our experiments, we show the discrete relativeL 2 µ-norm error, computed over
the computational grid. For a fixed input-output pair (a, u), this is defined as
erel =
P
p,q |eup,q −u p,q|2
1/2
P
p,q |up,q|2
1/2 ,

SM26B. ADCOCK, S. BRUGIAPAGLIA AND X. W ANG
Algorithm SM2.1Adaptive least-squares approximation
Require:Function to approximatef∈L 2 ϱ([−1,1] d), bulk chasing parameter 0<
β≤1
Ensure:Sequence of multi-index setsS (1) ⊆S (2) ⊆ · · · ⊂Nd 0 and approximations ˆf (1), ˆf (2), . . .
SetS (1) ={0}
forl= 1,2, . . .do
Setn (l) =|S (l)|
Determine a number of samplesm (l) ≥n (l)
Drawx 1, . . . ,xm(l) ∼i.i.d. ϱ
Compute ˆf (l) ∈argmin
p∈P (l)
1
m(l)
Pm(l)
i=1 |f(x i)−p(x i)|2
Compute the estimatore=e (l) via (SM2.1) withm=m (l),S=S (l) and ˆf= ˆf (l)
ComputeT (l) =bulk(R(S (l)), e(l), β)
SetS (l+1) =S (l) ∪T (l)
end for
Parameter V alue
Hidden layers 15
Hidden layer width 150
Activation tanh
Training samples{10,20,40,80,160,320,640,1280}
Test samples 10,000
Batch size Full batch (all training samples)
Epochs 2000
Optimizer Adam
Weight decay 0
Initial learning rate 10 −4
Learning-rate schedule Multiplied by 0.999 every epoch
Table SM1: DNN architecture and training parameters for benchmark functions from the
Virtual Library of Simulation Experiments.
whereeudenotes the FNO prediction, andu p,q andeup,q are the grid values ofuand
˜u, respectively.
The test distributionµ cookies is based on a benchmark commonly known as
thefixed-radius cookie problem[SM10, SM9, SM12]. LetD= [0,1] 2, and let Ω i,
i= 1, . . . ,8, be non-overlapping disks of radiusrcookie, with centres (0.5±0.3,0.5±
0.3),(0.5,0.5±0.3),(0.5±0.3,0.5). Thena∼µ cookies if
(SM2.2)a(x) = 1−
8X
i=1
1Ωi (x) (C1 +C 2yi),wherey 1, . . . , y8 ∼i.i.d. U([−1,1]).
In our experiments, we setr cookie = 0.14,C 1 = 0.625, C2 = 0.375.
Fig. SM1 illustrates selected input–output pairs drawn from the different training
and test distributions used in our experiments.

SUPPLEMENTARY MATERIALS: STABLE EXTRAPOLATION IN LEARNINGSM27
Parameter V alue
Training resolution 64×64
Testing resolution 64×64
Training samples{10,20,40,80,160,320,640,1280}
Test samples 200
Input channels 1
Output channels 1
Fourier layers 4
Fourier modes 12
Hidden channels 32
Projection channels 2
Activation GeLU
Batch size 32
Epochs 100
Optimizer AdamW
Weight decay 10 −4
Initial learning rate 10 −3
Learning-rate schedule Halved every 100 epochs
Table SM2: FNO architecture and training parameters for the Darcy Flow problem.
Fig. SM1: Representative input-output pairs from the Darcy flow training and test distri-
butions. The top row shows the diffusion coefficientsa, and the bottom row shows the
corresponding solutionsu. The distributions areµ LN 3,2,µ LN 3,1,µ cookies andµ PC 3,1 (left to right).
Incompressible Navier–Stokes.Details of the architecutre and training parameters
are given in Table SM3. In our experiments, we show the discrete relativeL 2 µ-norm
error, computed jointly spatio-temporal computational grid. For a fixed input-output
pair (w0, w), this is defined as
erel =
P
p,q,l |ewp,q,l −w p,q,l|2
1/2
P
p,q,l |wp,q,l|2
1/2 ,
whereewdenotes the FNO prediction, andw p,q,l andewp,q,l are the grid values ofw
andew, respectively.

SM28B. ADCOCK, S. BRUGIAPAGLIA AND X. W ANG
Parameter V alue
Training resolution 64×64×50
Testing resolution 64×64×50
Training samples [150,300,600,1200,2400,4800]
Test samples 200
Input channels 4
Output channels 1
Fourier layers 4
Fourier modes 12
Hidden channels 32
Projection channels 2
Activation GeLU
Batch size 32
Epochs 200
Optimizer Adam
Weight decay 0
Initial learning rate 10 −3
Learning-rate schedule Halved every 50 epochs
Table SM3: FNO architecture and training parameters for the Navier-Stokes problem.
REFERENCES
[SM1]M. Abramowitz and I. A. Stegun, eds.,Handbook of Mathematical Functions: With For-
mulas, Graphs, and Mathematical Tables, Dover Publications, Inc., New York, NY, 1964.
[SM2]B. Adcock, S. Brugiapaglia, N. Dexter, and S. Moraga,Deep neural networks are effec-
tive at learning high-dimensional Hilbert-valued functions from limited data, in Proceed-
ings of The Second Annual Conference on Mathematical and Scientific Machine Learning,
J. Bruna, J. S. Hesthaven, and L. Zdeborov´ a, eds., vol. 145 of Proc. Mach. Learn. Res.
(PMLR), PMLR, 2021, pp. 1–36.
[SM3]B. Adcock, S. Brugiapaglia, N. Dexter, and S. Moraga,Learning smooth functions in
high dimensions: from sparse polynomials to deep neural networks, in Numerical Analy-
sis Meets Machine Learning, S. Mishra and A. Townsend, eds., vol. 25 of Handbook of
Numerical Analysis, Elsevier, 2024, pp. 1–52.
[SM4]B. Adcock, S. Brugiapaglia, N. Dexter, and S. Moraga,On efficient algorithms for com-
puting near-best polynomial approximations to high-dimensional, Hilbert-valued functions
from limited samples, vol. 13 of Mem. Eur. Math. Soc., EMS Press, 2024.
[SM5]B. Adcock, S. Brugiapaglia, N. Dexter, and S. Moraga,Near-optimal learning of
Banach-valued, high-dimensional functions via deep neural networks, Neural Networks,
181 (2025), p. 106761.
[SM6]B. Adcock, S. Brugiapaglia, and C. G. Webster,Sparse Polynomial Approximation of
High-Dimensional Functions, Comput. Sci. Eng., Society for Industrial and Applied Math-
ematics, Philadelphia, PA, 2022.
[SM7]B. Adcock, N. Dexter, and S. Moraga,Optimal deep learning of holomorphic operators
between Banach spaces, in Advances in Neural Information Processing Systems, A. Glober-
son, L. Mackey, D. Belgrave, A. Fan, U. Paquet, J. Tomczak, and C. Zhang, eds., vol. 37,
Curran Associates, Inc., 2024, pp. 27725–27789.
[SM8]B. Adcock, N. Dexter, and S. Moraga,Optimal approximation of infinite-dimensional
holomorphic functions II: recovery from iid pointwise samples, J. Complexity, 89 (2025),
p. 101933.
[SM9]J. B ¨ack, F. Nobile, L. Tamellini, and R. Tempone,Stochastic spectral Galerkin and col-
location methods for PDEs with random coefficients: a numerical comparison, in Spectral
and High Order Methods for Partial Differential Equations, J. S. Hesthaven and E. M.
Rønquist, eds., vol. 76 of Lect. Notes Comput. Sci. Eng., Berlin, Heidelberg, Germany,
2011, Springer, pp. 43–62.

SUPPLEMENTARY MATERIALS: STABLE EXTRAPOLATION IN LEARNINGSM29
[SM10]J. Ballani and L. Grasedyck,Hierarchical tensor approximation of output quantities of
parameter-dependent pdes, SIAM/ASA Journal on Uncertainty Quantification, 3 (2015),
pp. 852–872, https://doi.org/10.1137/140960980.
[SM11]S. Brugiapaglia, S. Dirksen, H. C. Jung, and H. Rauhut,Sparse recovery in bounded
Riesz systems with applications to numerical methods for PDEs, Appl. Comput. Harmon.
Anal., 53 (2021), pp. 231–269.
[SM12]A. Chkifa, A. Cohen, G. Migliorati, F. Nobile, and R. Tempone,Discrete least squares
polynomial approximation with random evaluations - application to parametric and sto-
chastic elliptic PDEs., ESAIM Math. Model. Numer. Anal., 49 (2015), pp. 815–837.
[SM13]A. Chkifa, A. Cohen, and C. Schwab,Breaking the curse of dimensionality in sparse
polynomial approximation of parametric PDEs, J. Math. Pures Appl., 103 (2015), pp. 400–
428.
[SM14]A. Chkifa, N. Dexter, H. Tran, and C. G. Webster,Polynomial approximation via
compressed sensing of high-dimensional functions on lower sets, Math. Comp., 87 (2018),
pp. 1415–1450.
[SM15]A. Cohen and R. A. DeVore,Approximation of high-dimensional parametric PDEs, Acta
Numer., 24 (2015), pp. 1–159.
[SM16]A. Cohen, R. A. DeVore, and C. Schwab,Convergence rates of bestN-term Galerkin
approximations for a class of elliptic sPDEs, Found. Comput. Math., 10 (2010), pp. 615–
646.
[SM17]A. Cohen, R. A. DeVore, and C. Schwab,Analytic regularity and polynomial approxima-
tion of parametric and stochastic elliptic PDE’s, Anal. Appl. (Singap.), 9 (2011), pp. 11–47.
[SM18]T. De Ryck, S. Lanthaler, and S. Mishra,On the approximation of functions by tanh
neural networks, Neural Networks, 143 (2021), pp. 732–750.
[SM19]T. Gerstner and M. Griebel,Dimension-adaptive tensor-product quadrature, Computing,
71 (2003), pp. 65–87.
[SM20]I. G ¨uhring and M. Raslan,Approximation rates for neural networks with encodable weights
in smoothness spaces, Neural Networks, 134 (2021), pp. 107–130.
[SM21]B. Li, S. Tang, and H. Yu,Better approximations of high dimensional smooth functions
by deep neural networks with rectified power units, Commun. Comput. Phys., 27 (2020),
pp. 379–411.
[SM22]Z. Li, N. Kovachki, K. Azizzadenesheli, B. Liu, K. Bhattacharya, A. Stuart, and
A. Anandkumar,Fourier neural operator for parametric partial differential equations, in
ICLR, 2021.
[SM23]Z. Li, H. Zheng, N. B. Kovachki, D. Jin, H. Chen, B. Liu, K. Azizzadenesheli, and
A. Anandkumar,Physics-informed neural operator for learning partial differential equa-
tions, ACM/IMS J. Data Sci., 1 (2024), pp. 1–27.
[SM24]J. Lu, Z. Shen, H. Yang, and S. Zhang,Deep network approximation for smooth functions,
SIAM J. Math. Anal., 53 (2021), pp. 5465–5506.
[SM25]H. Mhaskar,Neural networks for optimal approximation of smooth and analytic functions.,
Neural Comput., 8 (1996), pp. 164–177.
[SM26]G. Migliorati,Adaptive polynomial approximation by means of random discrete least
squares, in Numerical Mathematics and Advanced Applications – ENUMATH 2013, A. Ab-
dulle, S. Deparis, D. Kressner, F. Nobile, and M. Picasso, eds., Cham, Switzerland, 2015,
Springer, pp. 547–554.
[SM27]G. Migliorati,Adaptive approximation by optimal weighted least squares methods, SIAM
J. Numer. Anal, 57 (2019), pp. 2217–2245.
[SM28]J. A. A. Opschoor, C. Schwab, and J. Zech,Exponential ReLU DNN expression of
holomorphic maps in high dimension, Constr. Approx., 55 (2022), pp. 537–582.
[SM29]H. Rauhut and C. Schwab,Compressive sensing Petrov-Galerkin approximation of high-
dimensional parametric operator equations, Math. Comp., 86 (2017), pp. 661–700.
[SM30]H. Rauhut and R. W ard,Interpolation via weightedℓ 1 minimization, Appl. Comput.
Harmon. Anal., 40 (2016), pp. 321–351.
[SM31]C. Schwab and J. Zech,Deep learning in high dimension: neural network expression rates
for generalized polynomial chaos expansions in UQ, Anal. Appl. (Singap.), 17 (2019),
pp. 19–55.
[SM32]C. Schwab and J. Zech,Deep learning in high dimension: neural network expression
rates for analytic functions inL 2(Rd, γd), SIAM/ASA J. Uncertain. Quantif., 11 (2023),
pp. 199–234.
[SM33]D. Yarotsky,Error bounds for approximations with deep ReLU networks, Neural Networks,
94 (2017), pp. 103–114.
