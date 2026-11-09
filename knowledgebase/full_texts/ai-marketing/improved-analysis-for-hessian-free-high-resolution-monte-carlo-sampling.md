---
title: Improved Analysis for Hessian-free High-resolution Monte Carlo Sampling
url: https://arxiv.org/abs/2608.25052
category: ai-marketing
subcategory: measurement
date: 2026-08
venue: ''
authors:
- Wujun Lv
- Xiaoyu Wang
- Yingli Wang
- Lingjiong Zhu
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.25052
pages: 49
chars: 119064
fetched_at: '2026-11-08T13:30:40+00:00'
kb_version: 1
---

# Improved Analysis for Hessian-free High-resolution Monte Carlo Sampling

Improved Analysis for Hessian-free High-resolution Monte Carlo
Sampling
Wujun Lv∗ Xiaoyu Wang† Yingli Wang‡ Lingjiong Zhu§
August 27, 2026
Abstract
Hessian-free high-resolution (HFHR) dynamics augments underdamped Langevin dy-
namics (ULD) with reversible position diffusion for sampling problems that arise in machine
learning. We establish an explicit quantitative contraction rate for HFHR dynamics under
a position Poincar´ e inequality, weighted Hessian and Laplacian bounds, and a compact
Sobolev embedding, where the potential function is not necessarily convex. An adapted
time-augmented Poincar´ e inequality yields an explicit rate that improves upon the contrac-
tion rate of the underdamped Langevin dynamics. We also give a weak-solution construction
and a self-contained spectral proof of the divergence lemma underlying the argument. For
HFHR Monte Carlo (HFHRMC) algorithm, which is based on a discretization scheme of
HFHR dynamics, we use a path-space Girsanov argument to obtain a non-asymptotic con-
vergence bound and an explicit iteration complexity in total variation distance. The bounds
hold for everyα≥0 andγ >0 and remain regular at the ULD endpoint. Optimizing
the iteration complexity bound yields a positive, accuracy-dependent position-diffusion pa-
rameter at finite accuracy, while its leading high-accuracy order coincides with that of the
optimized ULD endpoint. Our iteration complexity bound improves upon the existing work
on HFHR algorithms. Numerical experiments including Bayesian learning problems on real
data are provided to illustrate the effect of positiveαand its benefit.
Keywords.Hessian-free high-resolution; Monte Carlo sampling; Fokker–Planck equation;
Poincar´ e inequality; nonconvex potential; explicit convergence rate.
1 Introduction
Consider a given probability measure on the Euclidean spaceR d:
µ(dq) :=Z −1 U e−U(q) dq,(1)
whereU:R d →Ris a potential function andZ U >0 is a normalizing constant. The problems
of sampling a given target distribution in (1) arise routinely in Bayesian statistics, inverse
problems and modern-day large-scale machine learning problems [GCSR95, Stu10, ADFDJ03,
TTV16, GGHZ21, GIWZ24, BGK +25].
∗School of Mathematics and Statistics, Donghua University, Shanghai, People’s Republic of China;
lvwujun@dhu.edu.cn
†Hong Kong University of Science and Technology (Guangzhou), Guangzhou, Guangdong Province, People’s
Republic of China;xiaoyuwang@hkust-gz.edu.cn
‡School of Mathematical Sciences, Fudan University, Shanghai, People’s Republic of China;
yingliwang@fudan.edu.cn
§Department of Mathematics, Florida State University, Tallahassee, Florida, United States of America;
zhu@math.fsu.edu
1
arXiv:2608.25052v1  [stat.ML]  25 Aug 2026

Langevin algorithms are popular Markov chain Monte Carlo algorithms that are designed
to solve the sampling problem (1). The most classical Langevin algorithm is based on the
discretization of theoverdamped Langevin dynamics(OLD):
dqt =−∇U(q t) dt+
√
2 dWt,(2)
where (W t)t≥0 is a standardd-dimensional Brownian motion. The diffusion (2) has invariant
distribution (1) under mild conditions; see e.g. [CHS87, HKS89]. There have been extensive
studies on the non-asymptotic convergence theory for (2) and its various discretization schemes
[Dal17, DM17, DM19, DK19, RRT17, BCM +21, CMR+21, ZADS23, CB18, EHZ22].
To accelerate convergence, one can introduce a momentum variable and consider theunder-
damped Langevin dynamics(ULD) (also known as kinetic or second-order Langevin dynamics)
[MSH02, Vil09a, CCBJ18, CCA +18, CL W21, CL W23, DRD20, GGZ20, MCC+21, GGZ22]:
(
dpt =−γp t dt− ∇U(qt) dt+ √2γdW t,
dqt =p t dt, (3)
where (Wt)t≥0 is a standardd–dimensional Brownian motion andγ >0 is the friction parameter.
Under mild assumptions, (3) admits a unique invariant measure with density∝e −U(q)− 1 2 |p|2 ,
whoseq–marginal coincides withµas in (1). It is by now well–understood that underdamped
Langevin dynamics (3) and its various discretized schemes can converge faster than the over-
damped counterpart [EGZ19, CL W23, CCBJ18, GGZ22].
There is a close connection between the underdamped Langevin dynamics andNesterov’s
accelerated gradient(NAG) method in optimization literature [Nes83, Nes13, MCC+21, GGZ22].
Motivated by the high-resolution ordinary differential equation (ODE) viewpoint on NAG, in
a seminal paper, [LZT22] proposed theHessian-free high-resolution(HFHR) dynamics that
satisfies the following stochastic differential equation (SDE):
(
dqt = (pt −α∇U(q t)) dt+
√
2αdW q t ,
dpt = (−∇U(q t)−γp t) dt+ √2γdW p t , α≥0, γ >0,(4)
where (W q t )t≥0 and (W p t )t≥0 are independent standardd-dimensional Brownian motions. The
caseα= 0 is underdamped Langevin dynamics (ULD) (3). The invariant law of (4) is given
by [LZT22, Theorem 4.1]:
π(dqdp) :=µ(dq)κ(dp), κ(dp) := (2π) −d/2e−|p|2/2 dp.(5)
The drift in the SDE (4) only depends on∇Uand is thus “Hessian-free”, in contrast to other
high-resolution ODEs for NAG that contain∇ 2U; see e.g. [SDJS22]. The connection to NAG
method in optimization has been further studied to design gradient-adjusted underdamped
Langevin (GAUL) dynamics for accelerated sampling that includes HFHR dynamics as a special
case [ZOL25]. Recently, HFHR and GAUL dynamics have been shown to reduce the asymptotic
variance in Monte Carlo computations compared to the more classical OLD [NWWZ26].
Under them-strong convexity andL-smoothness assumptions:mI d ⪯ ∇2U⪯LI d, the
HFHR analysis in [LZT22, Theorem 5.1 and Lemma D.5] proves weighted synchronous-coupling
contraction and, in the parameter regimeγ 2 > L+mandα≤ γ2−L−m mγ obtains the position-
marginalW 2 contraction rate m γ +αm.
A complementary continuous-time result was recently obtained in [CDOP25, Theorem 4.2].
For an equivalent fully diffusive parametrization of HFHR, they prove exponential decay of
relative entropy under a logarithmic Sobolev inequality.
Coupling method is a popular approach to explicit contraction in transport metrics in the
literature. For overdamped Langevin dynamics with locally nonconvex potentials, [Ebe16] de-
velops reflection coupling with concave transport costs. Eberle–Guillin–Zimmer [EGZ19] com-
bine reflection and synchronous coupling with a Lyapunov weight for underdamped Langevin
2

dynamics; see also [DRD20] for underdamped Langevin sampling in the log-concave setting.
Building on this kinetic coupling framework, [WWZ26] studies the same HFHR dynamics un-
der global smoothness and dissipativity assumptions. It proves exponential contraction in a
Lyapunov-weighted Wasserstein distance for all sufficiently smallα >0. Under an additional
asymptotically linear-gradient condition, it further establishes a strict linear-in-αimprovement
over ULD and transfers the result toW 2. In this paper, we will adopt a position-Poincar´ e
framework, allows arbitraryα≥0, and improves upon the coupling results in [WWZ26].
Quantitative convergence for ULD is a central example of hypocoercivity [Vil09a]. InL 2,
one major approach modifies the Hilbert norm to couple the macroscopic and microscopic
modes [DMS15, RS18]. Other constructive approaches use Schur complements or Poincar´ e–
Lions inequalities and time averaging [BFLS22, BS25], while variational space–time Poincar´ e
inequalities provide the route closest to ours [AAMN24, CL W23].
The objective of the present paper is different. We seek an explicitL 2(π) rate as in [CL W23,
Theorem 1]. As in [CL W23, Theorems 1 and 2], our assumptions do not require strong convexity
or a uniform upper bound on∇ 2U, and the ULD proof there combines a time-augmented
Poincar´ e inequality with theL2 energy identity obtained by testing the kinetic equation with
its solution. Two recent complementary ULD results further situate this endpoint. A gap-
shifted modified-L2 approach [FLL26, Theorem 1 and Corollary 2] recovers a rate of order √m
for convex potentials, and more generally an explicit rate under a global Hessian lower bound.
In the convex and semiconvex regimes, the optimized estimate agrees up to universal constants
with the Cao–Lu–Wang rate, while requiring fewer technical regularity assumptions; it does
not, however, provide the full arbitrary-friction and general-potential estimate used here. In
relative entropy, a recent result [Lu26, Theorem 2.3] obtains a sharp rate of order √ρfor convex
potentials whose position marginal satisfies a logarithmic Sobolev inequality with constantρ,
using a nonlinear Wasserstein entropy-current corrector. Neither result addresses the HFHR
position diffusionα >0 considered here.
Closer to the present setting, [CDOP25, Theorem 4.2, Algorithm 2, and Corollary 4.4]
studies a more general parametrization of the same fully diffusive high-resolution Langevin
system, together with its discretization and an application to global optimization. Under a
logarithmic Sobolev inequality for the joint Gibbs law, they obtain relative-entropy decay at rate
2ρmin{α, γ}in our normalization. This direct elliptic estimate requiresα >0 and degenerates
asα→0. Our result instead works in a position-Poincar´ e framework, supplemented by weighted
derivative and compactness assumptions, retains the hypocoercive contribution, and covers the
ULD endpointα= 0.
Discrete-time ULD convergence bounds under a Poincar´ e inequality require additional care
because continuous-timeL 2 contraction does not by itself control the discretization error in
relative entropy. For ULD, [ZCL +23, Lemma 8 and Theorem 9] combines a R´ enyi Girsanov
estimate with continuous-timeχ 2-decay, while [Leh25, Theorem 1] obtains a total-variation
bound by controlling the kinetic moments through relative entropy and the exact diffusion. We
adapt the latter self-bounding mechanism to the two-noise HFHR interpolation. The resulting
entropy–moment closure is explicit, remains regular atα= 0, and avoids a separate time-
uniform moment-stability assumption.
In this paper, for the discretization scheme of HFHR dynamics (4), we consider theHessian-
free high-resolution Monte Carlo(HFHRMC) algorithm:
Pk+1 =aP k −b∇U(Q k) +η p k,
Qk+1 =Q k +bP k −(c+αh)∇U(Q k) +η q k, (6)
wherea, b, cwill be speicified in (73) and (η p k, ηq k) are i.i.d. centered Gaussian random vectors
with covariance structure given in (75), (76) and (77). This is exactly the discretization scheme
given in [CDOP25, Algorithm 2]. We obtain non-asymptotic convergence bounds and iteration-
complexity estimates for the HFHRMC algorithm (6) for everyα≥0 andγ >0. This full-range
3

guarantee allows parameter optimization without imposing a priori parameter restrictions.
To summarize, the pioneering HFHR analysis of [LZT22, Theorem 5.1 and Corollary 5.4]
concerns the strongly convex setting and imposesγ >
√
L+mtogether with an upper bound
onα. The analysis in [CDOP25, Theorem 4.2 and Corollary 4.4] extends to nonconvex targets
but requires strictly positive position diffusion, and its continuous- and discrete-time estimates
degenerate asα→0. The coupling result of [WWZ26] applies to sufficiently smallα >0
and requires an additional asymptotically linear-gradient condition for strict acceleration. Our
continuous-time result instead holds for the whole rangeα≥0,γ >0, including the ULD
endpoint. It does not require strong convexity or a uniform upper bound on the Hessian:
the position-Poincar´ e and weighted-derivative framework covers nonconvex and non-globally-
smooth potentials. The assumptions also include a compact-embedding condition, however,
and hence are not strictly nested with those used in the coupling literature.
Contributions.The contributions of the paper can be summarized as follows.
•Our main result for the continuous-time HFHR dynamics is an explicitL 2 decay rate
(Theorem 3.1):
να,γ ≥cmin

γ, αm+ mγ (√m+R+γ) 2

,
wheremis the position Poincar´ e constant andRmeasures the curvature contribution.
The estimate recovers the Cao–Lu–Wang rate atα= 0 [CL W23, Theorem 1] and has the
HFHR scalingαm+m/γin the convex high-friction regime [LZT22, Theorem 5.1].
•We develop the analytic framework needed to prove the rate. This includes conservative
Markov semigroup constructions for bothα >0 and the kinetic endpointα= 0, an HFHR-
adapted space–time Poincar´ e inequality, and a variational decay estimate (Proposition 3.10,
3.13, Proposition 3.16, and Proposition 3.19). The technical novelty is to incorporate the
position diffusion into the kinetic graph operator and to control the resulting term by
integration by parts against the position derivative of the Cao–Lu–Wang divergence test.
Combining this hypocoercive estimate with direct product coercivity yields the additive
αm-improvement without losing the ULD endpoint.
•For the HFHRMC algorithm, which is based on a discretization scheme of the continuous-
time HFHR dynamics, we prove a path-space Kullback-Leibler (KL) error bound whose
Girsanov factor isα+γ −1, and hence remains finite at the ULD endpoint (Theorem 4.4).
An entropy–moment argument leads to the state-dependent local error, without assum-
ing a time-uniform moment bound for the numerical chain. This yields an explicit non-
asymptotic convergence bound in TV distance (Corollary 4.6) and iteration complex-
ity (Corollary 4.7). We then optimize this iteration complexity overα, γand obtain
an accuracy- and dimension-dependentα ⋆ ε, as well as the high-accuracy friction choice
γ⋆ ε →2( √m+R) (Proposition 4.9). Unlike the fixed ( √ 3−1)/γchoice arising from the
strongly convex iteration complexity bound of [LZT22, Corollary 5.4 and Remark 5.5],
our optimizer tends to zero with the requested TV accuracy. Its leading high-accuracy
order agrees with that of the optimized ULD endpoint, while a comparison with [CDOP25,
Corollary 4.4] shows our iteration complexity improves upon that result.
•We complement the theory with four numerical experiments, consisting of a toy example
of exact Gaussian calculations for an anisotropic target and a real data Bayesian linear
regression posterior, followed by ensemble diagnostics relative to numerical posterior refer-
ences for real data Bayesian logistic regression and a Bayesian neural network with bounded
transformed weights and biases (Section 5). These experiments illustrate effect and benefit
of positiveαfor the HRHRMC algorithm.
4

Organization.The rest of the paper is organized as follows. In Section 2, we present the
preliminaries and assumptions for the model. Section 3 introduces the main results for the
continuous-time analysis, including an explicitL 2 decay rate for HFHR dynamics (Section 3.1)
and a functional framework and the space-time estimate (Section 3.2). The proofs of the
main results will be provided in Section 3.3. Section 4 develops the discrete-time HFHRMC
algorithm, its non-asymptotic convergence bounds, iteration complexity, and parameter tuning.
Finally, we conclude in Section 6. The additional technical results, such as weighted elliptic
estimates and spectral construction of the divergence test, and weighted kinetic density, traces
and Green’s formula will be provided in Appendix A, B and C respectively.
2 Preliminaries and Assumptions
Notation.The probability measuresµ,κ, andπ=µ⊗κare those introduced in (1) and (5).
For a probability measureνon the Euclidean spaceR n, we write
ν(f) :=
Z
Rn
fdν,(f) ν :=ν(f), L 2 0(ν) :={f∈L 2(ν) :ν(f) = 0}.
We set Varν(f) :=ν(|f−ν(f)| 2). For the intervalI= (0, T), the normalized time measure and
the Gaussian velocity projection are
λT (dt) :=T −11(0,T) (t) dt,Π pf(t, q) :=
Z
Rd
f(t, q, p) dκ(p).
The symbolH k(ν) denotes the usual weighted Sobolev space. We write
H 1 κ :={g∈L 2(κ) :∇ pg∈L 2(κ)}, H −1 κ := (H 1 κ)∗,
withL 2(κ) as pivot space. Bochner spaces in the (t, q)-variables are taken againstλ T ⊗µ, and
H 1 0 (λT ⊗µ) means zero traces only att= 0 andt=T. We also use
∇t,q = e∇:= (∂ t,∇ q), D 2 t,q :=D 2 (t,q).
Unlabelled norms and pairings are taken with respect to the measure specified by the variables
appearing in the corresponding formula. The relationsa≲banda≍bmean, respectively,
one-sided and two-sided bounds up to universal positive constants.
The adjoints of the gradients inL 2(π) are
∇∗ qF=−∇ q ·F+∇U·F,∇ ∗ pF=−∇ p ·F+p·F.
Define
Lα,γ :=L ham −α∇ ∗ q∇q −γ∇ ∗ p∇p,(7)
where
Lham :=∇ ∗ p∇q − ∇∗ q∇p =p· ∇q − ∇U· ∇p.(8)
The Hamiltonian operator is antisymmetric inL 2(π), while the last two operators are self-
adjoint and nonpositive. We writeA q =∇ ∗ q∇q for the nonnegative Friedrichs realization in
L2(µ), and
Kα :=∂ t − Lham +αA q,A:=−∂ tt +A q
for the kinetic graph operator and the time–position operator, respectively;Acarries Neumann
conditions in time.
Forα≥0 andγ >0, we denote by (S α,γ t )t≥0 theL 2(π) semigroup generated byL α,γ. Its
construction forα >0 andα= 0 is given in Propositions 3.10 and 3.13, respectively.
We impose the following assumptions, with the same normalization as [CL W23].
5

Assumption 2.1(Position Poincar´ e inequality).There ism >0such that
Varµ(g)≤ 1 m Z Rd |∇qg|2 dµfor everyg∈H 1(µ).(9)
Assumption 2.2(Weighted derivative bounds).The potentialU∈C 2(Rd), and there exist
M≥1andδ∈(0,1)such that, for everyq∈R d,

∇2U(q)

2 F ≤M 2  d+|∇U(q)| 2  ,(10)
∆U(q)≤M d+ δ 2 |∇U(q)| 2 .(11)
Assumption 2.3(Compact embedding).The embeddingH 1(µ),→L 2(µ)is compact.
Remark2.4 (Sufficient conditions for the position Poincar´ e inequality).If∇ 2U⪰m 0Id for some
m0 >0, the Bakry– ´Emery criterion gives Assumption 2.1 withm≥m 0 [MS14, Theorem 3.1].
More generally, every integrable log-concave measure onR d satisfies a Poincar´ e inequality,
although the constant need not be explicit [BBCG08, Corollary 1.9]. IfU=V+W, where
∇2V⪰m 0Id and osc(W)<∞, the bounded perturbation principle givesm≥m 0e−osc(W)
[MS14, Theorem 3.2]. More precisely, putL OLD = ∆ q − ∇U· ∇q. If there areθ >0,b≥0,
R >0, and aC 2 functionW ≥1 such that
LOLDW ≤ −θW+b1B(0,R),
then [BBCG08, Theorem 1.4] yields a Poincar´ e inequality, including for many nonconvex con-
fining potentials.
Remark2.5 (Comparison with global smoothness).If∇Uis globallyL-Lipschitz, then

∇2U

2 F ≤dL 2 and ∆U≤dL. Hence Assumption 2.2 holds withM= max{1, L}and any
fixedδ∈(0,1). The converse is false: Assumption 2.2 allows the Hessian to grow with|∇U|.
For example, quartic confining potentials satisfy bounds of the form (10)–(11), whereas their
gradients are not globally Lipschitz.
Remark2.6 (Role of compactness).The compact embedding in Assumption 2.3 is used only in
Appendix B, where it yields a discrete spectral resolution of∇ ∗ q∇q. It is a technical assumption
rather than a curvature condition. A sufficient condition recorded in [CL W23, Remark 1.1] is
that, for someβ >1,
lim
|q|→∞
U(q)
|q|β = +∞.
As in [CL W23], we introduce the following quantity that measures the curvature contribu-
tion:
R:=



0, Uis convex,
√
K,∇ 2U(q)⪰ −KId for everyq,
M+M 3/4d1/4,without an additional Hessian lower bound.
(12)
In the second lineK≥0. The first line is the caseK= 0. ForC 2 potentials, the condition
∇2U⪰ −KId is equivalent to convexity ofq7→U(q) +K|q| 2 /2. Such a function is commonly
calledK-weakly convex in optimization andK-semiconvex in analysis; conventions concerning
the factor 1/2 may vary [DD19].
3 Continuous-Time Analysis
3.1 ExplicitL 2 decay rate for HFHR dynamics
The main result of the paper is the following explicitL 2 decay for HFHR dynamics.
6

Theorem 3.1(ExplicitL 2 decay for HFHR).Suppose Assumptions 2.1–2.3 hold. Letα≥0
andγ >0. Recall that(S α,γ t )t≥0 is theL 2(π)semigroup generated byL α,γ, introduced in
Section 2 and constructed in Propositions 3.10 and 3.13. Forf 0 ∈L 2(π)withπ(f 0) = 0, set
ft =S α,γ t f0; equivalently,
∂tft =L α,γft, π(f 0) = 0.
There are universal constantsc, C >0, independent ofm, M, d, R, α, γ, such that
∥ft∥L2(π) ≤Ce −να,γ t ∥f0∥L2(π) ,(13)
where
να,γ ≥cmin

γ, αm+ mγ (√m+R+γ) 2

.(14)
Proof.The proof will be provided in Section 3.3.
Remark3.2 (Convex, weakly convex, and general potentials).Theorem 3.1 gives the following
three explicit forms:
να,γ ≥cmin

γ, αm+ mγ (√m+γ) 2

, Uconvex,(15)
να,γ ≥cmin

γ, αm+ mγ
(√m+ √ K+γ) 2

,∇ 2U⪰ −KI,(16)
να,γ ≥cmin

γ, αm+ mγ (√m+M+M 3/4d1/4 +γ) 2

,general case.(17)
Thus position diffusion contributes through the Poincar´ e constant even when the Hessian is not
pointwise positive.
Remark3.3 (Comparison with ULD).The additional position diffusion in HFHR (4) compared
to ULD (3) has two analytically distinct roles. It provides direct coercivity through the product
Poincar´ e inequality, and it appears as an extra weak term in the space-time argument of [CL W23,
Theorem 2 and Lemma 2.6]. Since the divergence construction already controls the derivative of
the required test function, the second role costs no new assumption on the potential. Combining
the two estimates prevents this perturbative cost from degrading the ULD rate and produces
the additive HFHR scaling up to universal constants. Atα= 0, (14) gives the explicit Cao–
Lu–Wang rate [CL W23]:
ν0,γ ≥c mγ (√m+R+γ) 2 .
Thus, our result extends the analysis for ULD in [CL W23]. In the convex case,R= 0. At the
ULD endpointα= 0, choosingγ= √mgivesν 0,γ ≥c √m/4≳ √m, which gives the square-root
improvement over the overdamped LangevinL 2 ratemdiscussed after [CL W23, Theorem 1].
Ifαremains of constant order asm→0, the additional contributionαmis lower order than√m. Thus positive position diffusion does not yield a further improvement in the asymptotic
dependence onmin this regime, although it may improve constants at finite parameter values.
Takingαlarge can improve the continuous-time rate, but it also might increase the discretization
error. This motivates the parameter optimization for the HFHRMC algorithm in Section 4.
Remark3.4 (Comparison with recent HFHR results).(i) Under them-strong convexity andL-
smoothness assumptions:mI d ⪯ ∇2U⪯LI d, the HFHR analysis in [LZT22, Theorem 5.1 and
Lemma D.5] proves weighted synchronous-coupling contraction and, in the parameter regime
γ2 > L+mandα≤ γ2−L−m mγ obtains the position-marginalW 2 contraction rate m γ +αm. Our
result givesL 2 andχ 2 convergence under the more general Assumptions 2.1–2.3. IfUis convex,
thenR= 0. If in additionγ≫ √m, then mγ (√m+γ)2 ≍ m γ , and hence,
να,γ ≳min

γ, αm+ m γ  .
7

Thus, in the overlapping strongly convex high-friction regime, two estimates have the same
m
γ +αmscaling up to universal constants. However, the restrictionγ 2 > L+min [LZT22] in
general leads to sub-optimal convergence rate, whereas our rateν α,γ can be optimized over the
entire parameter spaceα≥0,γ >0, which, for example, leads to a better rate whenmis small
andγ≍ √m.
(ii) In the normalization of the present paper, [CDOP25, Theorem 4.2] gives relative-entropy
decay at rate 2ρmin{α, γ}, assuming a logarithmic Sobolev inequality with constantρfor the
joint Gibbs measure. That estimate works directly in relative entropy but requiresα >0 and
degenerates asα→0. By contrast, ourL 2 rate retains the positive hypocoercive contribution
mγ/(√m+R+γ) 2 atα= 0.
(iii) The coupling results in [WWZ26, Corollary 3.9, Corollary 4.13, and Corollary 4.14]
apply under global smoothness and dissipativity assumptions and yields contraction between
arbitrary probability laws in a Lyapunov-weighted Wasserstein distance. Its strict acceleration
result holds for sufficiently smallαunder an additional asymptotically linear-gradient condition.
Our result is complementary: it gives a simpler explicit rate for everyα≥0 under functional-
inequality assumptions, but only for convergence to equilibrium fromL 2 densities.
Remark3.5 (Dimension dependence of the Poincar´ e constant).The dimension dependence of
the rate is partly encoded in the Poincar´ e constantm. It is dimension-free, for example, under
uniform strong convexity or for tensor products of one-dimensional measures with a uniform
spectral gap. For genuinely nonconvex multi-well targets, however,mmay be exponentially
small in the dimension or in the barrier height; see also [MS14, Corollary 2.15]. Under smooth-
ness and dissipativity assumptions, [RRT17, Proposition 13 and Appendix B] derives a conser-
vative spectral-gap bound whose reciprocal can grow exponentially ind. Thus (14) is explicit in
m, but it does not by itself guarantee polynomial dimension dependence in general nonconvex
settings.
Remark3.6 (Overdamped Langevin spectral gap).The optimal value ofmin Assumption 2.1
is the spectral gap of the overdamped Langevin generator ∆ q − ∇U· ∇q; any admissiblemis
a lower bound on this gap. Consequently, for every centeredg∈L 2(µ),
P OLD t g  L2(µ) ≤e −mt ∥g∥L2(µ) .
For forward densities this is equivalently aχ2-decay estimate with exponent 2m. This statement
is specific toL 2; it does not automatically identify the Wasserstein contraction rate.
The semigroup constructions in Propositions 3.10 and 3.13 also determine the forward equa-
tion, including at the kinetic endpoint, as presented in the following proposition.
Proposition 3.7(Adjoint semigroup and forward equation).Letα≥0andγ >0, and set
P α,γ t := (Sα,γ t )∗ onL 2(π).
Then(P α,γ t )t≥0 is a conservative Markov contraction semigroup. Ifh 0 ≥0,π(h 0) = 1, and
h0 ∈L 2(π), then
ht =P α,γ t h0, ρ t =h tπ,
defines a probability measure for everyt≥0. It is the weak forward solution in the sense that,
for everyφ∈C ∞ c (R2d), d
dt
Z
R2d
φht dπ=
Z
R2d
(Lα,γφ)ht dπ(18)
inD ′((0,∞)). Moreover,
∥P α,γ t g∥L2(π) ≤Ce −να,γ t ∥g∥L2(π) wheneverπ(g) = 0,(19)
with the constants and rate of Theorem 3.1.
8

Proof.Positivity ofS α,γ t implies positivity of its adjoint, because the positive cone ofL 2(π) is
self-dual. The two identities
Sα,γ t 1 = 1,⟨S α,γ t f,1⟩=⟨f,1⟩
imply, respectively, preservation of mass byPα,γ t andP α,γ t 1 = 1. Thus the adjoint is conservative
and Markovian. It is strongly continuous becauseL 2(π) is reflexive.
Forφ∈C ∞ c , Propositions 3.10 and 3.13 identify the backward infinitesimal withL α,γ onφ.
The generator identity
Sα,γ t φ−φ=
Z t
0
Sα,γ s Lα,γφds
therefore implies, after pairing withh 0,
⟨P α,γ t h0, φ⟩ − ⟨h0, φ⟩=
Z t
0
⟨P α,γ s h0,L α,γφ⟩ds.
This is (18) in distributions. Finally, bothS α,γ t andP α,γ t leaveL 2 0(π) invariant. Their restrictions
to this closed subspace are adjoints of one another, and hence have equal operator norms.
Theorem 3.1 now yields (19).
As an immediate corollary of Theorem 3.1, we obtain the following result for the finite-time
convergence bound.
Corollary 3.8(χ 2, KL and total-variation convergence).Under the assumptions of Theo-
rem 3.1, letρ 0 =h 0π, whereh 0 ≥0,π(h 0) = 1, andh 0 ∈L 2(π). Then
KL(ρt∥π)≤χ 2(ρt∥π)≤C 2e−2να,γ tχ2(ρ0∥π),(20)
and
∥ρt −π∥ TV ≤ C 2 e−να,γ tp χ2(ρ0∥π).
Proof.Sinceh t −1 =P α,γ t (h0 −1), (20) follows from (19). The total-variation estimate follows
from Cauchy-Schwarz inequality:
∥ρ−π∥ TV ≤ 1 2 ∥dρ/dπ−1∥ L2(π) .
Finally, the KL divergence is upper bounded by theχ 2 divergence, which concludes the proof.
Remark3.9.Ifπsatisfies a log-Sobolev inequality with constantρ >0, Talagrand’s inequality
[Vil09b, Theorem 22.15(i)] implies the following convergence in 2-Wasserstein distance:
W2(ρt, π)≤
r 2
ρ KL(ρt∥π)≤
r 2
ρ Ce−να,γ tp χ2(ρ0∥π).(21)
3.2 Functional framework and the space–time estimate
The additional diffusion inqchanges the natural energy space. This section constructs the
HFHR semigroup forα >0 and records the weak formulation used later. The endpointα= 0
is constructed below by vanishing position diffusion.
Let
V:=H 1(π) =  f∈L 2(π) :∇ qf,∇ pf∈L 2(π) 	 ,
that is equipped with its usual graph norm. Smooth compactly supported functions are dense
inV. Indeed, cutoff first reduces to a compact set becauseπis finite, and ordinary mollification
9

applies there because the density ofπis positive, continuous, and locally bounded from above
and below.
For smoothf, g, the weighted adjoint identities give
⟨Lhamf, g⟩L2(π) =⟨∇ qf,∇ pg⟩L2(π) − ⟨∇pf,∇ qg⟩L2(π) .(22)
The right-hand side extends continuously toV×V. Forα, γ >0, define
aα,γ(f, g) :=α⟨∇qf,∇ qg⟩+γ⟨∇ pf,∇ pg⟩ − ⟨∇qf,∇ pg⟩+⟨∇ pf,∇ qg⟩.(23)
All unlabelled inner products in this section are inL 2(π).
We first turn the formal generator into a well-posed Markov evolution. The coercive-form
construction below also supplies the exact energy identity needed in the decay argument.
Proposition 3.10(Weak HFHR semigroup).Letα, γ >0. For everyf 0 ∈L 2(π)andT >0,
there exists a unique
f∈L 2(0, T;V)∩C([0, T];L 2(π)), ∂ tf∈L 2(0, T;V∗),
such thatf(0) =f 0 and
⟨∂tf, g⟩V ∗,V +a α,γ(f, g) = 0for a.e.tand everyg∈V.(24)
The solutions define a strongly continuous contraction semigroupS α,γ t onL 2(π). This semigroup
is conservative and Markov:S α,γ t 1 = 1, and0≤S α,γ t f0 ≤1for any0≤f 0 ≤1.
IfG α,γ denotes its infinitesimal generator, thenC ∞ c (R2d)⊂D(G α,γ)andG α,γf=L α,γfon
this class. The solution preserves itsπ-mean and satisfies
1
2 ∥ft∥2 L2(π) +
Z t
0

α∥∇ qfs∥2 L2(π) +γ∥∇ pfs∥2 L2(π)

ds= 1 2 ∥f0∥2 L2(π) .(25)
Proof.The form is continuous onV×V. Its antisymmetric terms cancel on the diagonal, so
aα,γ(f, f) =α∥∇ qf∥ 2 +γ∥∇ pf∥ 2 .
Consequently,a α,γ +⟨·,·⟩is coercive onV, with a coercivity constant that may depend on
the fixed pair (α, γ). The representation and semigroup-generation theorems for continuous
coercive forms [Ouh05, Proposition 1.22 and Theorems 1.52 and 1.55] then give a unique
solution inL 2(0, T;V)∩C([0, T];L 2(π)), with time derivative inL 2(0, T;V∗), and an asso-
ciated strongly continuous contraction semigroup. Forf∈C ∞ c , integration by parts shows
aα,γ(f, g) =− ⟨Lα,γf, g⟩for everyg∈V. SinceL α,γf∈L 2(π), this proves the claimed in-
finitesimal inclusion and identity; no operator-core assertion is needed.
Takingg= 1 in (24) proves mean preservation, while the constant function is itself a solution,
soS α,γ t 1 = 1. To prove positivity, use the negative partf − t = max{−ft,0}as a time-dependent
test function. The Sobolev chain rule is valid inV, and the two antisymmetric terms cancel on
the set{f t <0}. Consequently,
1
2
d
dt
f − t 2 L2(π) +α ∇qf − t 2 L2(π) +γ ∇pf − t 2 L2(π) = 0.
Thus nonnegative initial data remain nonnegative. Applying the same argument to (f t −1) +
proves preservation of the interval [0,1]. This is the Markov property. Finally, the Hilbert-space
chain rule applied withg=f t yields (25).
10

Remark3.11 (Semigroup and diffusion interpretation).BecauseC ∞ c (R2d) is dense both inVand
inC 0(R2d), the form is regular. Its transpose has the same Markov contraction property. The
representation theorem for regular non-symmetric Dirichlet forms therefore gives a conservative
diffusion whose martingale infinitesimal onC ∞ c isL α,γ; see [MR92, Theorems IV.3.5 and V.1.5].
This identifies the form semigroup with the HFHR diffusion at the level needed here. We use
only the inclusionC ∞ c ⊂D(G α,γ), not the stronger claim thatC ∞ c is an operator core.
The weak space-time operator should include the position diffusion rather than place it in
the velocity negative Sobolev norm.
Definition 3.12(HFHR kinetic energy space).ForI= (0, T) andα≥0, letH α(I) be the
graph space of distributionsfsuch that
f∈L 2(λT ⊗µ;H 1 κ), √α∇ qf∈L 2(λT ⊗π),
and
Kαf∈L 2(λT ⊗µ;H −1 κ ).
Forα= 0, this is the time-dependent kinetic space used in [CL W23, AAMN24].
The preceding form construction degenerates whenα= 0. We therefore construct the
kinetic endpoint by vanishing position diffusion and retain the energy and Markov properties
in the limit.
Proposition 3.13(Kinetic endpoint).Letγ >0. For everyf 0 ∈L 2(π)andT >0, there is a
unique
f∈C([0, T];L 2(π))∩H 0((0, T))
with initial tracef(0) =f 0 such that
K0f=∂ tf− Lhamf=−γ∇ ∗ p∇pf(26)
in distributions. These solutions define a conservative Markov contraction semigroupS 0,γ t ,
preserve theπ-mean, and satisfy, for its infinitesimalG 0,γ,
C∞ c (R2d)⊂D(G 0,γ), G 0,γφ=L 0,γφ.
They also satisfy
1
2 ∥ft∥2 L2(π) +γ
Z t
0
∥∇pfs∥2 L2(π) ds= 1 2 ∥f0∥2 L2(π) .(27)
Proof.We give a vanishing-position-diffusion construction. Forε >0, letf ε =S ε,γ t f0 be the
solution from Proposition 3.10. These solutions are defined for all positive times. Their energy
identity gives, for every finiteT,
sup
0≤t≤T
∥f ε t ∥2 L2(π) + 2γ
Z T
0
∥∇pf ε s ∥2 L2(π) ds+ 2ε
Z T
0
∥∇qf ε s ∥2 L2(π) ds≤ ∥f0∥2 L2(π) .(28)
Weak compactness yields, along a sequenceε→0,
f ε ⇀∗ finL ∞(0, T;L2(π)),∇ pf ε ⇀∇ pfinL 2(0, T;L2(π)).
A diagonal extraction over integer values ofTgives a single limit on (0,∞). For every compactly
supported smooth test functionχ,

ε Z T 0 ⟨∇qf ε s ,∇ qχs⟩ds

 ≤ √ε √ε∥∇ qf ε∥L2  ∥∇qχ∥L2 − →0.
11

Passing to the limit in the weak equation therefore gives (26); in particularf∈H 0((0, T)).
The same weak equations give compactness in weak time continuity. More precisely, for
everyχ∈C ∞ c , the Hamiltonian term is uniformly integrable in time, the velocity-diffusion
term is uniformly one-half H¨ older in duality withχ, and the position-diffusion term isO( √ε)
by (28). A diagonal argument over a countable dense family of tests therefore gives, asε→0,
f ε − →finC([0, T];L 2(π)w).
Sincef ε 0 =f 0, the limit has weakL 2 initial tracef 0.
Proposition C.2 first givesf∈C((0,∞);L 2(π)). Weak lower semicontinuity in (28), using
the weak convergence at each fixed time supplied above, gives
1
2 ∥ft∥2 L2(π) +γ
Z t
0
∥∇pfs∥2 L2(π) ds≤ 1 2 ∥f0∥2 L2(π) (t >0).(29)
In particular, lim supt→0 ∥ft∥L2(π) ≤ ∥f0∥L2(π). The endpoint criterion in Proposition C.2 there-
fore upgrades the weak initial trace to a strong one. Corollary C.3, first on interior intervals
and then with the initial endpoint included, proves (27). Thusf∈C([0, T];L 2(π)) for every
finiteT.
Applying the same chain rule to the difference of two solutions proves uniqueness. Hence,
the whole familyf ε, not merely a subsequence, converges weakly tof; uniqueness also gives
the semigroup property. Contractivity follows from (27). Mean preservation passes through
the weak limit. Positivity and preservation of the interval [0,1] pass as well, because these are
weakly closed convex conditions inL 2(π) and hold for everyS ε,γ t . ThusS 0,γ t is conservative and
Markov.
It remains to record the infinitesimal identity used below. Fixφ∈C ∞ c and putg=L 0,γφ∈
L2(π). By linearity of the weak equation, the variation-of-constants function
vt =φ+
Z t
0
S0,γ s gds
belongs locally to the kinetic energy space. Sinceg=L 0,γφ, integration of the weak equation
forS 0,γ s ggives
K0v=K 0φ+g+
Z t
0
K0

S0,γ s g  ds=−γ∇ ∗ p∇pv.
Thus,vsolves the same weak Cauchy problem asS 0,γ t φ. Uniqueness givesv t =S 0,γ t φ. Dividing
bytand using strong continuity yields
lim
t→0
S0,γ t φ−φ
t =ginL 2(π),
which proves the asserted infinitesimal inclusion.
For the weak HFHR solution of Proposition 3.10, the equation gives, in distributions,
Kαf=−γ∇ ∗ p∇pf.(30)
In particular, the right-hand side belongs toL 2(λT ⊗µ;H −1 κ ), with
∥Kαf∥ L2(H −1 κ ) ≤γ∥∇ pf∥ L2(λT ⊗π) .(31)
Thus positive position diffusion supplies exactly theq-regularity needed below. No assertion
that∇ ∗ q∇qfseparately belongs to the velocity negative Sobolev space is required.
12

The modified time-augmented Poincar´ e inequality .The proof uses the divergence con-
struction of [CL W23, Lemma 2.6], itself motivated by the variational kinetic framework of
[AAMN24]. Define
B0(T) := 1√m(1−e −√mT ) +T,(32)
B1(T) := 1 +RT+ 1 (1−e −√mT )2 + R√m(1−e −√mT )2 .(33)
The macroscopic component offwill be estimated by duality against a time–position di-
vergence equation. The following lemma provides a test field with the first- and second-order
bounds required for that argument.
Lemma 3.14(Cao–Lu–Wang divergence test).For every centeredh∈L 2(λT ⊗µ), there are
ϕ0 ∈H 1 0 (λT ⊗µ)andψ∈H 2(λT ⊗µ), with∇ qψ∈H 1 0 (λT ⊗µ) d, such that
−∂tϕ0 +∇ ∗ q∇qψ=h.(34)
Moreover,
∥ϕ0∥L2 +∥∇ qψ∥L2 ≤CB 0(T)∥h∥ L2 ,(35)
∥∇qϕ0∥L2 +∥∇ t,q∇qψ∥L2 ≤CB 1(T)∥h∥ L2 .(36)
Proof.The construction is proved in Appendix B. We use the spectral argument of [CL W23,
Lemma 2.6], but give the details with spectral parameters denoted byωj so they are not confused
with the HFHR parameterα.
To use the divergence field with functions in the kinetic graph space, we need an integration-
by-parts identity that remains valid at the available weak regularity. It also isolates the addi-
tional term created by position diffusion.
Lemma 3.15(Graph-space integration by parts).Letf∈H α(I), letϕ 0 ∈H 1 0 (λT ⊗µ), and let
ζ∈H 1 0 (λT ⊗µ) d. Set
Φ(t, q, p) :=ϕ0(t, q)−p·ζ(t, q),
and
TΦ :=−∂ tϕ0 +p· ∇qϕ0 +p·∂ tζ−p ⊤∇qζ p+∇U·ζ.(37)
ThenΦ∈L 2(λT ⊗µ;H 1 κ),∇ qΦ∈L 2(λT ⊗π),TΦ∈L 2(λT ⊗π), and Z
I×R d
fTΦ dλ T dπ=⟨K αf,Φ⟩ H −1 κ ,H 1κ −α
Z
I×R d
∇qf· ∇qΦ dλT dπ.(38)
Proof.The only coefficient requiring attention is∇U·ζ. Lemma A.2, applied componentwise,
shows that it belongs toL 2; the remaining assertions follow from the Gaussian moments of
1, pi, pipj.
Forϕ 0, ζsmooth, compactly supported inq, and vanishing neart= 0, T, weighted integra-
tion by parts int, q, pgives
Z
I×R d
fTΦ dλ T dπ=⟨∂ tf− Lhamf,Φ⟩=⟨K αf,Φ⟩ −α⟨∇qf,∇ qΦ⟩.
To pass to the stated Sobolev class, approximateϕ 0 andζby trace-preserving smooth func-
tions inH 1 0 , and insert a Gaussian velocity cutoff in the corresponding Φ. The usual Sobolev
convergence handles all first-order terms, while Lemma A.2 gives
∥(ζn −ζ)∇U∥ L2 ≤C(M, d)∥ζ n −ζ∥ H 1 .
Thus Φ n →Φ inL 2(H 1 κ),∇ qΦn → ∇qΦ inL 2, andTΦ n →TΦ inL 2. Each term in the
identity therefore converges, proving (38).
13

We now combine the divergence construction with the graph-space identity. This yields the
HFHR analogue of the time-augmented Poincar´ e inequality used for ULD.
Proposition 3.16(HFHR space-time inequality).Under Assumptions 2.1–2.3, letf∈H α(I).
Whenα= 0, the last term below is understood to vanish. Then
∥f−(f) λT ⊗π∥L2(λT ⊗π) ≤C

B1(T)∥(I−Π p)f∥ L2(λT ⊗π)
+B 0(T)∥K αf∥ L2(λT ⊗µ;H −1 κ ) +αB 1(T)∥∇ qf∥ L2(λT ⊗π)

.(39)
Forα= 0, this is the time-augmented Poincar´ e inequality of [CL W23, Theorem 2].
Proof.It suffices to prove the estimate for functions with zero global mean. Set
h:= Π pf, g:= (I−Π p)f,
so thatf=h+g, Π pg= 0, and (h) λT ⊗µ = 0. Apply Lemma 3.14 toh, and define
Φ(t, q, p) :=ϕ0(t, q)−p· ∇qψ(t, q).(40)
Gaussian moment identities and (35)–(36) imply
∥Φ∥L2(λT ⊗µ;H 1κ) ≤CB 0(T)∥Π pf∥ L2 ,(41)
∥∇qΦ∥L2(λT ⊗π) ≤CB 1(T)∥Π pf∥ L2 .(42)
To present the complete macro–micro identity, introduce
AΦ :=−∂ tϕ0 +p· ∇qϕ0 +p·∂ t∇qψ−p ⊤∇2 qψ p+∇qψ· ∇U.(43)
The Gaussian identities
Z
Rd
pi dκ= 0,
Z
Rd
pipj dκ=δ ij,
Z
Rd
pipjpk dκ= 0,(44)
and (34) imply
Z
I×R d
hAΦ dλT dπ=
Z
I×R d
h(−∂tϕ0 −∆ qψ+∇U· ∇qψ) dλT dµ=∥h∥ 2 L2 .
Therefore,
∥h∥2 L2 =
Z
I×R d
fA Φ dλT dπ−
Z
I×R d
gAΦ dλT dπ.(45)
Becauseϕ 0 and∇ qψhave zero traces at both time endpoints, Lemma 3.15, withζ=∇ qψ,
gives Z
I×R d
fA Φ dλT dπ=⟨K αf,Φ⟩ −α⟨∇qf,∇ qΦ⟩.(46)
Consequently, duality and Cauchy–Schwarz inequality yield

 Z I×R d fA Φ dλT dπ

 ≤ ∥Kαf∥ L2(H −1 κ ) ∥Φ∥L2(H 1κ) +α∥∇ qf∥ L2 ∥∇qΦ∥L2
≤C
h
B0(T)∥K αf∥ L2(H −1 κ ) +αB 1(T)∥∇ qf∥ L2
i
∥h∥L2 .(47)
It remains to estimate the second term of (45). Expanding the square inp, using the
fourth-moment identity
Z
Rd
pipjpkpℓ dκ=δ ijδkℓ +δ ikδjℓ +δ iℓδjk ,
14

and then using (34), gives
∥AΦ∥2 L2(λT ⊗π) ≤C  ∥h∥2 L2 +∥∇ qϕ0∥2 L2 +∥∂ t∇qψ∥2 L2 + ∇2 qψ 2 L2  .(48)
Indeed, the velocity average ofA Φ ish; all terms odd inpvanish; and the centered quadratic
part has variance bounded by a universal multiple of
∇2 qψ 2. Lemma 3.14 now gives
∥AΦ∥L2(λT ⊗π) ≤CB 1(T)∥h∥ L2 .(49)
Consequently,

 Z I×R d gAΦ dλT dπ

 ≤CB 1(T)∥g∥ L2 ∥h∥L2 .
Ifh= 0, the desired estimate follows immediately fromf=gandB 1(T)≥1. Otherwise,
insert the last two bounds in (45) and divide by∥h∥ L2. This controls the macroscopic part.
Finally,
∥f∥ L2 ≤ ∥h∥L2 +∥g∥ L2 ,
and the microscopic term is absorbed becauseB 1(T)≥1.
3.3 Proofs of the main results
Forα >0, Proposition 3.10 gives the energy identity below directly for the weak solution. For
α= 0, it is provided by Proposition 3.13:
d
dt ∥ft∥2 L2(π) =−2α∥∇ qft∥2 L2(π) −2γ∥∇ pft∥2 L2(π) .(50)
Write
Dα,γ(f) :=α∥∇ qf∥ 2 L2(π) +γ∥∇ pf∥ 2 L2(π) .(51)
Direct coercivity .Position diffusion also gives a direct coercive mechanism that is indepen-
dent of hypocoercivity. Tensorization of the position and Gaussian Poincar´ e inequalities makes
this contribution explicit.
Lemma 3.17(Product Poincar´ e bound).For every centeredf∈H 1(π),
∥f∥ 2 L2(π) ≤ 1 m ∥∇qf∥ 2 L2(π) +∥∇ pf∥ 2 L2(π) .(52)
Consequently,
∥Sα,γ t f∥ L2(π) ≤e −νdirt ∥f∥ L2(π) , ν dir = min{αm, γ}.(53)
Proof.Tensorize Assumption 2.1 with the Gaussian Poincar´ e inequality. Then
Dα,γ(f)≥min{αm, γ} ∥f∥2 L2(π) .
Forα >0, the conclusion follows from the weak energy identity. Whenα= 0,ν dir = 0, and
the asserted estimate is simply theL 2-contractivity following from the kinetic energy identity;
noq-regularity is needed at that endpoint.
15

The time-averaged hypocoercive bound.Fix an intervalI= (s, s+T), translated to
(0, T), and use the normalized measureλ T . For the HFHR solution,
Kαf=−γ∇ ∗ p∇pf,(54)
and therefore
∥Kαf∥ L2(λT ⊗µ;H −1 κ ) ≤γ∥∇ pf∥ L2(λT ⊗π) .(55)
The Gaussian Poincar´ e inequality also gives
∥(I−Π p)f∥ L2(λT ⊗π) ≤ ∥∇pf∥ L2(λT ⊗π) .(56)
Combining Proposition 3.16 with (55)–(56), and then applying weighted Cauchy–Schwarz
inequality, yields
∥f∥ L2(λT ⊗π) ≤C
h
(B1 +γB 0)∥∇ pf∥ L2(λT ⊗π) +αB 1 ∥∇qf∥ L2(λT ⊗π)
i
,(57)
and hence
∥f∥ 2 L2(λT ⊗π) ≤CK α,γ(T)
Z
I
Dα,γ(ft) dλT (t),(58)
where
Kα,γ(T) := (B1(T) +γB 0(T)) 2 γ +αB 1(T) 2.(59)
The following elementary bookkeeping lemma records both sides of the estimate needed in
the iteration. Its lower bound is important: it makes the prefactor in the resulting exponential
estimate universal, rather than merely finite for each fixed set of parameters.
Lemma 3.18(Constants at the natural time scale).Let
T∗ :=m −1/2, A:= √m+R, Q α,γ := (A+γ) 2 mγ + αA2 m .(60)
Then, with a universal constantC >0,
B0(T∗)≤ C√m , B 1(T∗)≤C A√m ,4T ∗ ≤K α,γ(T∗)≤CQ α,γ.(61)
Proof.AtT=T ∗, one hasη ∗ := 1−e −√mT∗ = 1−e −1, and in fact
B0(T∗) = 1 +η −1 ∗√m , B 1(T∗) = (1 +η −2 ∗ ) A√m .
This proves the first two estimates and implies
B1(T∗) +γB 0(T∗)≤C A+γ√m ,
which gives the upper bound forK α,γ(T∗). For the lower bound, the arithmetic–geometric mean
inequality gives, for everyT >0,
(B1(T) +γB 0(T)) 2
γ ≥4B 1(T)B 0(T)≥4T,
becauseB 1(T)≥1 andB 0(T)≥T. This proves (61).
The interval coercivity estimate can now be combined with energy dissipation and iterated
over intervals of the natural lengthm −1/2. The resulting estimate records the purely variational
decay rate.
16

Proposition 3.19(Variational rate).There are universal constantsc, C >0such that, for
everyf∈L 2 0(π),
∥Sα,γ t f∥ L2(π) ≤Ce −νvart ∥f∥ L2(π) ,(62)
with
νvar ≥c
 (√m+R+γ) 2
mγ + α(√m+R) 2 m −1 .(63)
Proof.LetE(t) :=∥f t∥2 L2(π). Integrating (50) overI= (s, s+T) gives
E(s)−E(s+T) = 2T
Z
I
Dα,γ(ft) dλT (t).(64)
SinceEis nonincreasing,
E(s+T)≤ ∥f∥ 2 L2(λT ⊗π) .
Using (58) and (64),
E(s+T)≤ CstKα,γ(T) 2T (E(s)−E(s+T)).
HereC st denotes one fixed universal constant for which (58) holds. Set
xT := 2T CstKα,γ(T) .
After moving the last occurrence ofE(s+T) to the left, the previous inequality becomes the
exact one-step contraction
E(s+T)≤(1 +x T )−1E(s).(65)
Consequently, ifk=⌊t/T⌋, monotonicity ofEand iteration of (65) give
E(t)≤(1 +x T )−kE(0)≤(1 +x T ) exp

− t T log(1 +x T )  E(0).(66)
ChooseT=T ∗ =m −1/2. Lemma 3.18 implies 0< x T∗ ≤C 0 for a universalC 0. Hence both
the prefactor (1 +x T∗)1/2 in the norm estimate and the constant in
log(1 +x T∗)≥ xT∗
1 +C 0
are universal. Taking square roots in (66) therefore gives a decay exponent
νvar = 1 2T∗ log(1 +x T∗)≥ c Kα,γ(T∗) ≥ c Qα,γ .
Inserting (60) proves (63) and shows at the same time that the constantCin (62) is independent
of all parameters.
Combining the two mechanisms.The variational estimate retains the ULD contribution
but deteriorates whenαis large, whereas direct coercivity improves withα. The following
elementary lemma combines the two complementary bounds.
Lemma 3.20(Rate algebra).LetA≥ √m,α≥0, andγ >0. Set
ν0 := mγ (A+γ) 2 , ν 1 :=  ν−1 0 + αA2 m −1 , ν 2 := min{αm, γ}.
Then, for a universalc >0,
max{ν1, ν2} ≥cmin{γ, αm+ν0}.(67)
17

Proof.First,ν 0 ≤γ. IfαA 2/m≤ν −1 0 , thenν 1 ≥ν 0/2. Otherwise,
αm
ν0
> m2
A2ν2 0 = (A+γ) 4 A2γ2 ≥16.
The last inequality is simply (A+γ) 2 ≥4Aγ. Hence in the second caseαm≥16ν 0, and
thereforeν 2 = min{αm, γ} ≥ν0. In both cases it follows that
max{ν1, ν2} ≥1 2 max{ν0,min(αm, γ)}.
Finally, for anya≤gandb≥0,
max{a,min(b, g)} ≥1 2 min{g, a+b}.
Apply this elementary inequality witha=ν 0,b=αm, andg=γto obtain (67), for instance
withc= 1/4.
Finally, we are ready to prove Theorem 3.1.
Proof of Theorem 3.1.Set
A:= √m+R, ν 0 := mγ (A+γ) 2 ,
and define
ν1 :=

ν−1 0 + αA2 m −1 , ν 2 := min{αm, γ}.(68)
Suppose first thatα >0. Proposition 3.10 gives a mean-preserving weak solution in the
energy class, and (30) shows that its restriction to every finite time interval belongs toH α(I).
Thus Proposition 3.19 and Lemma 3.17 apply directly and give universal constantsc 1, C1 >0
such that
∥Sα,γ t f∥ L2(π) ≤C 1e−c1ν1t ∥f∥ L2(π) ,(69)
and
∥Sα,γ t f∥ L2(π) ≤e −ν2t ∥f∥ L2(π) .(70)
After decreasingc 1 so thatc 1 ≤1 and increasingC 1 so thatC 1 ≥1, selecting (69) whenν 1 ≥ν 2
and (70) otherwise yields
∥Sα,γ t f∥ L2(π) ≤C 1e−c1 max{ν1,ν2}t ∥f∥ L2(π) .(71)
Ifα= 0, Proposition 3.13 supplies the mean-preserving solution inH 0(I), together with
(26) and (27). Proposition 3.19 therefore again gives (69); meanwhileν 2 = 0, and Lemma 3.17
supplies the contractive version of (70). Hence (71) remains valid at the kinetic endpoint.
Finally, Lemma 3.20, applied withA= √m+R, gives
max{ν1, ν2} ≥c2 min

γ, αm+ mγ (√m+R+γ) 2

for a universalc 2 >0. Inserting this estimate into (71) proves (13)–(14). This completes the
proof.
18

4 Discrete-Time Analysis
To implement HFHR dynamics (4) in practice, one relies on a discrete-time algorithm that is
based on a discretization scheme of approximating the continuous-time dynamics (4).
Leth >0,t k =kh, and setg k :=∇U(¯qtk ). On [t k, tk+1), define the continuous interpolation
(
d¯qt = (¯pt −αg k) dt+
√
2αdW q t ,
d¯pt = (−gk −γ¯pt) dt+ √2γdW p t . (72)
Thus the momentum appearing in the position equation is not frozen. Writing
a:=e −γh, b:= 1−a γ , c:= h−b γ ,(73)
the grid-point chain generated by (72) is exactly the HFHRMC algorithm given in (6):
Pk+1 =aP k −b∇U(Q k) +η p k,
Qk+1 =Q k +bP k −(c+αh)∇U(Q k) +η q k, (74)
such that (¯pkh,¯qkh) = (Pk, Qk) in distribution for everyk, where (η q k, ηp k) are independent across
steps, centered joint Gaussian vectors with block covariances
E
h
ηp k  ηp k ⊤i = (1−a 2)Id,(75)
E
h
ηq k  ηp k ⊤i = (1−a) 2 γ Id,(76)
E
h
ηq k  ηq k ⊤i =  2αh+ 2 γ  h− 2(1−a) γ + 1−a 2 2γ  Id.(77)
Consequently, (74) is directly implementable with one new evaluation of∇Uper iteration. This
is the exact linear frozen-force step; the corresponding frozen-gradient HFHR scheme appears
as [CDOP25, Algorithm 2].
Throughout this section we impose the following additional regularity, which is separate
from the weighted derivative bounds used in the continuous-time analysis.
Assumption 4.1(Smoothness for discretization).The gradient∇Uis globallyL-Lipschitz,
and the initial lawρ 0 satisfies
Z
R2d

|q|2 +|p| 2

dρ0(q, p)<∞.
4.1 Path-space KL discretization error
The path-space argument below uses the SDE realization of the exact dynamics, whereas the
continuous-time decay theorem was formulated for the semigroups constructed in Section 3.2.
The next lemma records that these are the same objects, including at the degenerate endpoint
α= 0.
Lemma 4.2(Identification of the exact SDE semigroup).Under Assumption 4.1, let(T α,γ t )t≥0
be the backward transition semigroup of the strong solution of(4). Then
Tα,γ t =S α,γ t onL 2(π) (78)
for everyα≥0andγ >0. Consequently, ifρ 0 =h 0πwithh 0 ∈L 2(π), the exact SDE law at
timetis(P α,γ t h0)π.
19

Proof.Forα >0, the identification follows from Remark 3.11; global Lipschitz continuity of
the drift also gives uniqueness of the corresponding martingale problem.
It remains to identify the endpoint obtained by vanishing position diffusion. Fixx= (q, p),
and construct on the same probability space the solutionsX ε andX 0 of (4), starting fromx,
with parametersα=ε∈(0,1] andα= 0, and driven by the same Brownian motions. Global
Lipschitz continuity and linear growth first give
Ex sup
0≤s≤T
|X ε s |2 ≤C T,L,γ

d+|x| 2 +|∇U(0)| 2

.
Subtracting the equations in (4) forX ε andX 0, corresponding respectively toα=εandα= 0,
and then applying the Cauchy–Schwarz and Burkholder–Davis–Gundy inequalities, gives
Ex sup
0≤s≤t

X ε s −X 0 s

2 ≤C T,L,γ Z t
0
Ex sup
0≤r≤s

X ε r −X 0 r

2 ds+C T,L,γ ε  d+|x| 2 +|∇U(0)| 2  .
Gr¨ onwall’s inequality therefore gives, for every finiteT,
Ex sup
0≤s≤T

X ε s −X 0 s

2 ≤C T,L,γ ε  d+|x| 2 +|∇U(0)| 2  .(79)
It follows from (79) that, for every fixedt≥0,x∈R 2d, andφ∈C ∞ c (R2d), asε→0,
Tε,γ t φ(x)− →T0,γ t φ(x).
The functions are uniformly bounded by∥φ∥ ∞, so the convergence also holds strongly inL 2(π).
Forε >0, the first part of the proof givesT ε,γ t =S ε,γ t . The vanishing-diffusion construction
in Proposition 3.13 givesS ε,γ t φ ⇀ S0,γ t φinL 2(π). Comparing this weak limit with the strong
limit above yieldsT 0,γ t φ=S 0,γ t φ. SinceC ∞ c (R2d) is dense inL 2(π) and both semigroups are
contractions, the equality extends to all ofL 2(π). Taking adjoints proves the final assertion.
The following entropy estimate will replace a time-uniform moment assumption. It uses
only the Gaussian momentum law and global smoothness of the potential.
Lemma 4.3(Entropy control of the kinetic moments).Suppose∇Uis globallyL-Lipschitz.
There is a universal constantC 0 >0such that every probability measureν≪πsatisfies
Z
R2d

|p|2 +|∇U(q)| 2

dν≤C 0(1 +L) [d+ KL(ν∥π)].(80)
Proof.The Gaussian factorκsatisfies
log
Z
Rd
e|p|2/4 dκ(p) = d 2 log 2.
We next record the analogous estimate for the force. We may takeL >0, enlarging the Lipschitz
constant if necessary. Since∇UisL-Lipschitz, by the descent lemma [Nes13, Lemma 1.2.3],
for everyq, v∈R d andλ≥0,
U(q−λv)≤U(q)−λv· ∇U(q) + Lλ2
2 |v|2 .
After exponentiating, integrating, and making the translationq7→q−λv, we obtain
Z
Rd
eλv·∇U dµ≤e λ2L|v|2/2.
20

Gaussian randomization, with an independent vectorG∼ N(0,I d), now yields
Z
Rd
exp

|∇U(q)| 2
4L
!
dµ(q)≤Ee |G|2/4 = 2d/2.(81)
The variational formula for relative entropy [DE97, Proposition 1.4.2], applied toθFand ex-
tended to nonnegativeFby truncation, gives, for everyθ >0,
Z
R2d
Fdν≤ 1 θ  KL(ν∥π) + log Z R2d eθF dπ  .
Applying this inequality with
(F, θ) = (|p|2 ,1/4) and (F, θ) = (|∇U(q)| 2 ,1/(4L)),
respectively, and using the preceding exponential-moment bounds proves (80).
LetP T be the path law on [0, T] of the HFHR SDE (4) and let ¯PT,h be the path law of (72),
with the same initial law andT=N h. Denote their time-Tlaws byρ T and ¯ρN , respectively.
Theorem 4.4(Girsanov discretization bound).Suppose Assumption 4.1 holds andρ 0 =h 0π,
whereh 0 ∈L 2(π). Define
R0 := log

1 +χ 2(ρ0∥π)  , G 0 :=d+R 0,(82)
and set
Λα,γ :=α+ 1 γ ,Ξ α,L := (1 +α 2)(1 +L).
For everyα≥0,γ >0, andT=N h,
KL
¯PT,h ∥PT  ≤ 1 4 Λα,γE Z T 0

∇U(¯qt)− ∇U(¯q⌊t/h⌋h)

2 dt.(83)
Moreover, for a universal constantC 1 >0,
KL
¯PT,h ∥PT  ≤C 1L2Λα,γT  αdh+ Ξ α,LG0h2 ·exp  C1L2Λα,γΞα,LT h2	 .(84)
Proof.Let
∆t :=∇U(¯qt)− ∇U(¯q⌊t/h⌋h).
We carry out the entropy closure on a localized process so that no integrability assumption
is used before it has been proved. ForR >0, let ¯X R = (¯qR,¯pR) follow the frozen-force
interpolation until
τR := inf

t≥0 :

 ¯X R t

 ≥R 	 ,
and follow the exact HFHR drift afterτ R, with the same diffusion coefficients throughout. Thus,
withg R k =∇U(¯qR tk ), the force used in both drift coordinates is
F R t =1 {t<τR}gR k +1 {t≥τR}∇U(¯qR t ), t∈[t k, tk+1).
Write ¯PR t,h for its path law on [0, t],E R for expectation on the probability space carrying ¯X R
and its driving Brownian motions, ¯ρR t for its time-tlaw, and
DR(t) := KL
¯PR t,h∥Pt  .
Beforeτ R, the drift discrepancy is (α∆ R t ,∆ R t ), where
∆R t :=∇U  ¯qR t  − ∇U  ¯qR ⌊t/h⌋h  ,
21

and it is zero afterwards. This discrepancy is bounded on [0, T∧τ R], so the usual Novikov
condition holds. Forα >0, its squared norm in the inverse diffusion covariance is
α
2

∆R t

2 + 1 2γ

∆R t

2 .
The entropy identity in Girsanov’s theorem [ZCL +23, Theorem 15] therefore gives
DR(t) = 1 4 Λα,γER
Z t∧τR
0

∆R s

2 ds.(85)
Whenα= 0, the position drifts of the two processes are both the current momentum. The
discrepancy lies entirely in the noisy momentum coordinate, so the same identity holds with
Λ0,γ =γ −1. This also makes explicit why no inverse power ofαoccurs.
Restriction of paths shows thatD R(s)≤D R(t) whens≤t. Data processing inequality and
the entropy variational inequality imply
KL

¯ρR t ∥π  ≤2KL  ¯ρR t ∥ρt  + log  1 +χ 2(ρt∥π)  ≤2D R(t) +R 0.(86)
Indeed, withr t = dρt/dπ, the entropy variational inequality onR 2d gives
Z
R2d
logr t(q, p) ¯ρR t (dqdp)≤KL  ¯ρR t ∥ρt  + log Z
R2d
rt(q, p)ρt(dqdp),
and the last integral is
R
R2d r2 t dπ= 1 +χ 2(ρt∥π). The exact SDE law is the forward semigroup
law by Lemma 4.2. ItsL 2(π) contractivity therefore makes thisχ 2 divergence no larger than
its initial value.
Lemma 4.3 and (86) therefore give
ER
h

¯pR t

2 +

∇U(¯qR t )

2i ≤C 1(1 +L) [G0 +D R(t)].(87)
Fort∈[t k, tk+1], puts=t−t k. The integral form of the frozen-force equation on{t < τ R},
Cauchy–Schwarz inequality, the bound
ER
h
1{t<τR}

W q t −W q tk

2i ≤E R

W q t −W q tk

2 =d s,
and (87) imply
ER
h
1{t<τR}

¯qR t −¯qR tk

2i ≤C 1  αds+ Ξ α,L (G0 +D R(t))s 2 .(88)
Here moments at times beforetare controlled byD R(t) becauseD R is nondecreasing. Since
∇UisL-Lipschitz, integrate the stopped bound

∆R t

2 ≤L 2

¯qR t −¯qR tk

2 over theNtime steps
and use (85)–(88). For everyT=N h, this yields
DR(T)≤C 1L2Λα,γ

αdT h+ Ξα,LG0T h2 + Ξα,Lh2
Z T
0
DR(t) dt

.
Gr¨ onwall’s inequality gives the right-hand side of (84), uniformly inR.
It remains to remove the localization. Couple ¯X R with the original frozen-force interpolation
¯Xby using the same initial state and Brownian motions. Pathwise uniqueness makes them
identical up toτ R. Since the globally Lipschitz dynamics is nonexplosive,P(τ R ≤T)→0, and
hence ¯PR T,h converges to ¯PT,h on path space. Moreover, the expectation in (85) equals
E
Z T∧τ R
0
|∆t|2 dt,
22

because the two processes agree before the exit time. Lower semicontinuity of relative entropy
and monotone convergence therefore give
KL
¯PT,h ∥PT  ≤lim inf R→∞ DR(T)≤ 1 4 Λα,γE Z T 0 |∆t|2 dt,
which is (83). Passing to the limit in the uniform Gronwall bound proves (84). This self-
bounding step is analogous to the entropy closure used in the proof of [Leh25, Theorem 1]; the
higher-order R´ enyi Girsanov approach of [ZCL+23, Theorem 9 and Corollary 16] provides a
related route under a Poincar´ e inequality.
Remark4.5 (Scaling of the discretization error).IfC 1L2Λα,γΞα,LT h2 ≤1, the exponential
factor in (84) is bounded by a universal constant, and hence
KL
¯PT,h ∥PT  ≲L 2Λα,γ  αdT h+ Ξα,LG0T h2 .
Thus, forα >0, the leading path-space KL error has the usualT hscaling and gives a
√
T h
total-variation error. At the kinetic endpointα= 0, theT hterm vanishes and the bound
improves toT h2 in KL, or √ T hin total variation. The exponential factor therefore imposes
only the stability condition recorded in the first term of (92); it does not change the high-
accuracy iteration-complexity order.
4.2 Non-asymptotic convergence bound and iteration complexity
The next result combines the path-space estimate with the continuous mixing theorem. It
controls the joint law and therefore, by projection, also the position marginal sampled by the
algorithm.
Corollary 4.6(TV error bound of HFHRMC).Suppose Assumptions 2.1–2.3 and 4.1 hold,
and letρ 0 =h 0πwithh 0 ∈L 2(π). Then
∥¯ρN −π∥ TV ≤ C 2 e−να,γ T p χ2(ρ0∥π)
+C 1L
q
Λα,γT[αdh+ Ξ α,LG0h2] exp  C1L2Λα,γΞα,LT h2	 , T=N h, (89)
whereCis as in Theorem 3.1 andC 1 is universal.
Proof.By the triangle inequality,
∥¯ρN −π∥ TV ≤ ∥¯ρN −ρ T ∥TV +∥ρ T −π∥ TV .
Pinsker’s inequality [Tsy09, Lemma 2.5], together with Theorem 4.4 bound the first term. The
second term is controlled by Corollary 3.8.
Set
A:= √m+R, r 0(γ) := mγ (A+γ) 2 , r(α, γ) := min{γ, mα+r 0(γ)}.(90)
Theorem 3.1 supplies a universalc 0 >0 such thatν α,γ ≥c 0r(α, γ). Write
W0 :=
p
χ2(ρ0∥π),M χ := (1 +L)  d+ log(1 +W 2 0 )  ,
ℓε := log CW0 ε , T ε := ℓε c0r(α, γ).
The resulting iteration complexity is recorded as a corollary.
23

Corollary 4.7(Iteration complexity of HFHRMC).Suppose the assumptions of Corollary 4.6
hold and0< ε < CW 0. Seth=T ε/N. There is a universal constantC 2 >0such that
∥¯ρN −π∥ TV ≤ε, provided that
N≥C 2Nε(α, γ),(91)
where
Nε(α, γ) := max
(
L
p
Λα,γΞα,LT 3/2 ε , L2d α(α+γ−1)T 2 ε ε2 , L p Mχ(α+γ −1)(1 +α 2)T 3/2 ε ε ) .
(92)
Whenα= 0, the middle term vanishes. This reflects the fact that the position increment is
then of orderh, whereas forα >0its Brownian component is of order
√
αh.
Proof.Sinceν α,γ ≥c 0r(α, γ), the definition ofT ε makes the mixing term in (89) at mostε/2.
The first term in (92) ensures that
L2Λα,γΞα,LTεh2 ≲1,
so the exponential factor in (89) is bounded by a universal constant. The second and third
terms in (92) make, respectively, the contributions ofαdhand Ξ α,LG0h2 to the discretization
error at most fixed universal multiples ofε. IncreasingC 2, if necessary, proves (91).
Remark4.8 (2-Wasserstein error bound and iteration complexity of HFHRMC).Under the ad-
ditional assumption thatπsatisfies a log-Sobolev inequality with constantρ >0, Talagrand’s
inequality [Vil09b, Theorem 22.15(i)] (see Remark 3.9) can be combined with the same en-
tropy closure used in (86). Indeed, data processing, the entropy variational inequality, and
Corollary 3.8 give
KL(¯ρN ∥π)≤2KL(¯ρ N ∥ρT ) + log

1 +χ 2(ρT ∥π) 
≤2KL( ¯PT,h ∥PT ) +C 2e−2να,γ T χ2(ρ0∥π).(93)
Talagrand’s inequality, (93), and Theorem 4.4 therefore yield, after enlarging the universal
constants if necessary,
W2(¯ρN , π)≤
r 2
ρ Ce−να,γ T p χ2(ρ0∥π)
+
r 2
ρ C1L
q
Λα,γT[αdh+ Ξ α,LG0h2] exp  C1L2Λα,γΞα,LT h2	 , (94)
whereT=N h. To state the resulting iteration complexity, set
ερ :=
√ρ ε
2
√
2
and suppose 0< ε ρ < CW0. TakingT=T ερ andh=T ερ/NgivesW 2(¯ρN , π)≤ε, provided
thatN≥ eC2 eNε(α, γ), where eC2 is a universal constant and
eNε(α, γ) :=Nερ(α, γ)
= max
(
L
p
Λα,γΞα,LT 3/2 ερ , L2d α(α+γ−1)T 2 ερ ε2ρ , L p Mχ(α+γ −1)(1 +α 2)T 3/2 ερ ερ ) .
(95)
24

4.3 Optimal choices ofαandγ
We finally optimize the explicit proxyN ε in (92), rather than the continuous-time rate alone.
This distinction is important because increasingαaccelerates continuous mixing but also in-
creases the local discretization error. Define the saturation threshold
αsat(γ) := γ−r 0(γ) m >0.(96)
Forα≥α sat(γ), the rate proxy in (90) has already saturated atγ, while bothα(α+γ −1) and
(α+γ −1)(1 +α 2) increase. Hence no minimizer of the complexity proxy needs to lie above
αsat(γ).
Proposition 4.9(High-accuracy parameter tuning).For fixedγ, letα ⋆ ε(γ)minimizeN ε(α, γ)
overα≥0. With all problem parameters other thanεfixed, asε→0,
α⋆ ε(γ)≍ ε
p
Mχ γr0(γ)
Ld√ℓε , α ⋆ ε(γ)< αsat(γ).(97)
Ifγis optimized as well, let(α ⋆ ε, γ⋆ ε )denote a joint minimizer. Then
γ⋆ ε − →2A= 2(√m+R), α ⋆ ε ≍ 2ε p Mχm 3Ld√ℓε .(98)
Proof.Below saturation,r(α, γ) =r 0(γ) +mα. Denote the three terms in (92) byB st, B1, B2,
respectively. For fixedγ, the last two terms, after omitting fixed universal constants, are
B1(α) = L2d α(α+γ−1)ℓ2 ε ε2(r0 +mα) 2 , B 2(α) = L p Mχ(α+γ −1)(1 +α 2)ℓ3/2 ε ε(r0 +mα) 3/2 .
We first justify that it is enough to optimize these expressions near zero. Atα= 0, the full
proxy is of orderℓ 3/2 ε /ε. On the other hand, for every fixedδ∈(0, α sat), compactness of [δ, αsat]
gives
inf
δ≤α≤αsat
B1(α)≥c δ
ℓ2 ε
ε2 .
Together with the exclusion ofα > αsat preceding the proposition, this provesα ⋆ ε(γ)→0.
The logarithmic derivatives are
d
dα logB 1(α) = 1 α + 1 α+γ −1 − 2m r0 +mα ,
d
dα logB 2(α) = 1 2(α+γ −1) + α 1 +α 2 − 3m 2(r0 +mα) .
HenceB 1 is strictly increasing on a fixed neighborhood of zero, whereasB 2 is strictly decreasing
there because
d
dα logB 2(α)

α=0
= γ 2 − 3m 2r0(γ) <0.
In the same neighborhood,B st =O(ℓ 3/2 ε ), whileB 2 ≥cℓ 3/2 ε /ε; thus the stability term is
uniformly lower order. At zero one hasB 1 < B2, whereas at the fixed right endpoint of this
neighborhood one hasB 1 > B2 for all sufficiently smallε. There is therefore a unique crossover.
Before it the maximum equals the decreasing functionB 2, and after it the maximum equals the
increasing functionB 1. The crossover is consequently the global high-accuracy minimizer.
The crossover tends to zero, so replacingr 0 +mαbyr 0,α+γ −1 byγ −1, and 1 +α 2 by one
inB 1 =B 2 gives
α⋆ ε(γ)≍ ε
p
Mχ γr0(γ)
Ld√ℓε .
25

Since this quantity tends to zero, it is strictly belowα sat(γ) for all sufficiently smallε. This
proves (97). At this optimized scale, the leadingγ-dependent factor is
γ−1/2(r0(γ))−3/2 = (A+γ) 3 m3/2γ2 .
For completeness, joint minimizers cannot escape to zero or infinity. Indeed, the benchmark
(α, γ) = (0,2A) has complexity of orderℓ 3/2 ε /ε. Ifγ→0, thenr≤γand Λ α,γ ≥γ −1,
so the third term is at least a fixed multiple ofℓ 3/2 ε /(εγ2). Ifγ→ ∞, putx=α+γ −1.
Sincer 0(γ)≤m/γ, one hasr≤mx. The second and third terms are consequently bounded
below, up to fixed factors, by α x ℓ2 ε ε2 and 1 x ℓ3/2 ε ε , respectively. Matching the benchmark forces
α/x=O(ε/ √ℓε), hencex∼γ −1; the third lower bound then diverges relative to the benchmark.
Thusγ ⋆ ε remains in a compact subset of (0,∞).
On compactγ-sets the preceding small-αexpansion is uniform. The leading profile is
therefore (A+γ)3 m3/2γ2 , which tends to infinity at both endpoints, and its logarithmic derivative is
3/(A+γ)−2/γ, whose unique zero isγ= 2A. Henceγ ⋆ ε →2A, proving the first term in (98).
Finally,r 0(2A) = 2m/(9A); substituting this value in (97) proves the second term in (98).
Remark4.10 (Optimized iteration complexity).Recall thatA= √m+R. For fixedγ, substi-
tution of (97) into the complexity proxy gives
Nε(α⋆ ε(γ), γ) = (1 +o(1))Nε(0, γ) =eO

L
p
Mχ(A+γ) 3
εm3/2γ2
!
, ε→0.(99)
Here eOsuppresses powers ofℓ ε and other logarithmic factors. Forα= 0, one has Λ 0,γ =γ −1,
Ξ0,L = 1 +L, andr(0, γ) =r 0(γ). Therefore,
Nε(0, γ) =O

L(A+γ) 3ℓ3/2 ε
m3/2γ2 max
(
√
1 +L,
p
Mχ
ε
)!
.(100)
In the high-accuracy regimeε≤1, the definition ofM χ impliesM χ ≥1 +L, and hence
Nε(0, γ) =O

L
p
Mχ(A+γ) 3ℓ3/2 ε
εm3/2γ2
!
.(101)
Consequently, the optimized positive value ofαdoes not improve the leading high-accuracy
dependence onε,d, ormrelative to ULD; its benefit in the present certified bound is a lower-
order finite-accuracy improvement.
IfL≥1 and log(1 +W 2 0 ) = eO(d), thenM χ = eO(Ld) and it follows from (99) that
Nε(α⋆ ε(γ), γ) = eO

L3/2√ d(A+γ) 3
εm3/2γ2
!
, ε→0.(102)
The ULD contribution has the parameter regimes
r0(γ)≍



mγ/A2, γ≪A,
m/A, γ≍A,
m/γ, γ≫A.
After optimizing also overγ, Proposition 4.9 gives
Nε(α⋆ ε, γ⋆ ε ) = eO

L
p
Mχ A
εm3/2
!
= eO

L3/2√ d( √m+R)
εm3/2
!
.(103)
26

In particular, the convex caseR= 0 gives
Nε(α⋆ ε, γ⋆ ε ) = eO

L3/2√ d
εm
!
,
whereas in the general caseR=M+M 3/4d1/4 in (103).
Remark4.11 (Complexity comparison with ULD).For the ULD endpoint, the onlyγ-dependent
factor in (100) is (A+γ) 3/γ2. Its unique minimizer is
γ⋆ ULD = 2A= 2( √m+R).(104)
Consequently,
Nε(0, γ⋆ ULD) =O

LAℓ3/2 ε
m3/2 max
(
√
1 +L,
p
Mχ
ε
)!
= eO

L
p
MχA
εm3/2
!
(ε→0).(105)
Thus the jointly optimized HFHR proxy and the separately optimized ULD proxy have the same
leading high-accuracy order, although a positiveαcan improve the finite-accuracy certificate.
Remark4.12 (Comparison of ULD with [DRD20] in 2-Wasserstein distance).The bound of
[DRD20] is stated inW 2, and its friction restriction is already optimized at the boundary of its
admissible range, that isγ ∗ = √ m+Lsuch that they obtain the iteration complexity asε→0
[DRD20, Theorem 2 and the discussion following it]:
N DR ε (0, γ∗) = eO

L3/2√ d
εm2
!
.(106)
In our setting, whenUism-strongly convex, applying the Bakry– ´Emery criterion [MS14, The-
orem 3.1] to the joint potential givesπ=µ⊗κa log-Sobolev constantρ= min{m,1}. In the
regimem≤1, this isρ=m, and asε→0 ourW 2 iteration complexity satisfies:
eNε(0, γ⋆ ULD) = eO

L
p
MχA √ρεm3/2
!
= eO

L3/2√ d
εm3/2
!
.(107)
By comparing (106) with (107), we can see that our iteration complexity bound has a √m
improvement. Indeed, this further improves the iteration complexity in [CCBJ18, Theorem 1]
which is of order eO

L2√ d
εm5/2

.
Remark4.13 (Comparison of ULD with [Leh25] in TV distance).A closer ULD benchmark in
total variation is [Leh25, Theorem 1]. Writing its Poincar´ e constant asC P = 1/m, its warm-
start iteration complexity isO ∗

(L/m)3/2√ d
ε

under a Poincar´ e inequality. For our result at
α= 0, ifUisK-weakly convex whereKis of constant order, then, our iteration complexity
isN ε(0, γ⋆ ULD) = eO

L
√
Mχ A
εm3/2

= eO

L3/2√ d
εm3/2

which matches their iteration complexity. On
the other hand, in the log-concave case, the TV iteration complexity in [Leh25, Theorem 1]
improves toO ∗

(L/m)
√
d
ε

. Thus our convex ULD specialization eO(L3/2√ d/(εm)) does not
uniformly improve the best known dependence on all problem parameters.
Remark4.14 (Comparison of HFHRMC with [CDOP25] in the non-convex setting).We next
compare with the iteration complexity in [CDOP25, Algorithm 2 and Corollary 4.4], which is
based on the same HFHRMC algorithm. In their notation, our normalization corresponds to
a=b= 1,β CDOP =σ 2 x,CDOP =α,α CDOP =σ 2 y,CDOP =γ,γ CDOP = 1. IfUism-strongly
convex, applying the Bakry–´Emery criterion [MS14, Theorem 3.1] to the joint potential givesπa
27

log-Sobolev constantρ= min{m,1}. Since our iteration complexity is in TV distance whereas
that in [CDOP25, Corollary 4.4] is in KL, Pinsker’s inequality [Tsy09, Lemma 2.5] suggests
using KL accuracy of orderε 2 for a fair comparison. Substitution in the explicit constants of
[CDOP25, Appendix C.3] gives in the high-accuracy regime
N CDOP ε (α, γ) = eO
 L2(1 +α 2)BCDOP(α, γ)d
ρ2s3ε2

,(108)
where, using the notation of [CDOP25, Corollary 4.4],
s:= min{α, γ}, B CDOP(α, γ) := 12 + 4L+ 2α+ 4Lα2 + 3γ.
ForL≥1, minimizingN CDOP ε (α, γ) over bothαandγyields
inf
α,γ>0
N CDOP ε (α, γ) = eO
 L3d
ρ2ε2

.
By comparison, under the common strong-convexity and warm-start conditions, our iteration
complexity in (103) withR= 0 gives
Nε(α⋆ ε, γ⋆ ε ) = eO

L3/2√ d
mε
!
.
Thus the present analysis improves the certified dependence on accuracy and dimension, as well
as the dependence onmwhenm≤1, for this common discretization. This is a comparison of
proved upper bounds, not a claim of pointwise algorithmic dominance.
Remark4.15 (Comparison of HFHRMC with [LZT22] in the strongly-convex setting).In the
setting whereUism-strongly convex andL-smooth, [LZT22, Corollary 5.4] obtains the iteration
complexity
N LZT ε (α, γ) = eO

b′(α2 − α γ + 1 γ2 )
m( m γ +mα)
√
d
ε
!
,(109)
for some constantb ′ that may depend onγ(and henceLandmgiven the constraintγ 2 > L+m);
[LZT22, Remark 5.5] minimizes theW 2 iteration-complexity constant and under the contraint
γ2 > L+min [LZT22, Theorem 5.1] and obtainsα ∗ HFHR = min n √ 3−1 γ , γ2−L−m mγ o . Since the
dependence ofb ′ onγis unspecified in [LZT22], it is not clear how their iteration complexity
depends onLandm. However, since theirγhas the contraintγ 2 > L+mwhereas we know
the unconstrained optimalγaccording to our analysis should be of order √min the convex
setting (see (98)), we expect that their iteration complexity is worse than ours.
5 Numerical Experiments
This section illustrates our theory by studying a toy example of anisotropic Gaussian target
on synthetic data and three Bayesian learning problems on real data. All discrete-time experi-
ments use the HFHRMC algorithm in (74), with one full data gradient evaluation per iteration.
Throughout this section, HFHRMC refers toα >0 andα= 0 gives KLMC. The first experi-
ment computes the continuous-time Gaussian law, and the second computes a Gaussian upper
bound on the total variation error of the discrete chain. The last two experiments compare
HFHRMC and KLMC with numerical posterior references for a Bayesian logistic regression and
a Bayesian neural network. In the Bayesian learning experiments (Sections 5.2, 5.3, and 5.4),
Kis the number of completed iterations and also the number of full data gradient evaluations
along each particle trajectory. The initial state is indexed byK= 0. The number of particles
and independent ensembles is not included in this count.
28

5.1 Anisotropic Gaussian target
We first consider a toy example with the four-dimensional Gaussian position targetµ=
N(0, H−1) withH:= diag(0.25,1,4,9). Thus,m= 0.25,L= 9,R= 0, and we consider
γ= √m= 0.5 andγ= 2 √m= 1. The initial joint law is Gaussian with the invariant co-
variance diag(H −1,I 4) and a position mean shift 2e 1 in the slowest eigendirection. Its initial
divergence is thereforeχ 2(ρ0∥π) =e−1. Since the covariance remains invariant, the meanz t
is obtained from the exact matrix exponential of the linear HFHR dynamics and
χ2(ρt∥π) = exp  z⊤ t diag(H,I 4)zt  −1.
Consequently, this toy experiment contains no time discretization or Monte Carlo error.
Figure 1 comparesα∈ {0,0.1,0.3,0.7}at both friction values. Att= 18 andγ= 0.5,
the exactχ 2 divergences are 2.1391×10 −4, 1.1877×10 −4, 3.6623×10 −5, and 4.3128×10 −6,
respectively. Atγ= 1, they are 2.7566×10 −6, 2.8670×10 −7, 1.2550×10 −8, and 2.4157×10 −9.
Increasingαaccelerates convergence in this Gaussian slow mode for both choices ofγ, which is
consistent with the additionalαmcontribution in Theorem 3.1 and theχ 2-divergence estimate
in Corollary 3.8.
Exact Gaussian chi-square convergence, gamma=0.5
0 8 16 24 32 40
2.87e-13
1.51e-10
8e-08
4.22e-05
0.0223
11.8
physical time t
chi-square divergence
alpha=0
alpha=0.1
alpha=0.3
alpha=0.7
(a)γ= √m= 0.5
Exact Gaussian chi-square convergence, gamma=1
0 8 16 24 32 40
6.18e-22
2.29e-17
8.5e-13
3.16e-08
0.00117
43.5
physical time t
chi-square divergence
alpha=0
alpha=0.1
alpha=0.3
alpha=0.7 (b)γ= 2 √m= 1
Figure 1: Exact convergence for the anisotropic Gaussian target inχ 2-divergence. Every curve
is evaluated analytically from the continuous-time Gaussian law.
5.2 Bayesian linear regression on real data
We next conduct a Bayesian linear regresion experiment on real data. We use all 1599 records
and 11 features of the UCI Wine Quality red wine data set. 1 A fixed random split contains
1279 training records and 320 test records. Features and responses are centered and scaled
using training statistics only. For the standardized response, we use the conjugate model
y|β∼ N(Xβ,I 1279), β∼ N(0,4I 11).
The posterior isN( bβ, H−1), where
H:=X ⊤X+ 0.25I 11, bβ:=H −1X ⊤y.
The eigenvalues ofHdetermine the geometry of this Gaussian posterior. Their smallest and
largest values arem= 74.3373 andL= 3976.8834. Since the posterior potential is quadratic,
its Hessian is constant, soR= 0 andA= √m+R= 8.6219. These values determine the
friction scales used below. The response vectorydetermines the posterior center bβ, but it does
not change the precision matrixH. After transforming predictions back to the original quality
1The data set is available from the UCI Machine Learning Repository, DOI 10.24432/C56S3T.
29

scale, the posterior mean predictor has a test root mean square error (RMSE) of 0.6582 quality
units, compared with 0.8198 for the mean training response. The convergence calculation below
is instead based on the exact posterior law.
Since the posterior is Gaussian, its evolution can be calculated without simulating particles.
Write the eigendecomposition ofHas
H=Vdiag(λ 1, . . . , λ11)V ⊤, λ 1 =m,
and transform both the centered position and the momentum according to
eQ=V ⊤

Q− bβ

, eP=V ⊤P.
In these coordinates, the joint dynamics separates into 11 independent two-dimensional Gaus-
sian systems, one for each eigenvalue ofH. The continuous time mean and covariance are ob-
tained from the corresponding matrix exponentials, and the discrete mean and covariance are
propagated exactly under the linear Gaussian recurrence induced by the frozen force scheme.
Letv 1 be the unit eigenvector corresponding toλ 1 =m. We initialize the joint law by shifting
its mean in this direction while keeping the target covariance,
E

Q0 − bβ

= 1√m v1,EP 0 = 0,Cov ((Q 0, P0)) = diag(H −1,I 11).
The initial mean is therefore one posterior standard deviation away from the target mean in the
slowest direction, since

1√m v1
⊤
H

1√m v1

= 1,and henceχ 2(ρ0∥π) =e−1. All distributions
in this experiment are calculated exactly from their Gaussian means and covariance matrices.
We next specify how the iteration count is determined. For fixed (α, γ, ε), letρ α,γ t be the
exact law of the continuous-time dynamics. Since∥ρ α,γ t −π∥ TV ≤B cont(t) := 1 2 p χ2(ρα,γ t ∥π),
we chooseTas the earliest time for whichB cont(T)≤ε/2. Thus the total variation upper
bound for the continuous law is at most half of the target tolerance at timeT. For every integer
K≥1, we seth K =T /Kand let

Q(K) j , P(K) j K j=0 denote the discrete chain with step sizeh K.
The exact Gaussian recurrence gives its law at the end of the same interval [0, T]. Then,
Law  Q(K) K , P(K) K  −π  TV ≤B K := 1 2 r χ2  Law  Q(K) K , P(K) K  π  .
Moreover,B K also bounds the total variation error of the coefficient distributionQ (K) K . We
report the smallestKfor whichB K ≤ε. IncreasingKtherefore reduces the step size while
keeping the terminal timeTfixed. For every reported value, we repeat the calculation with
K−1 equal intervals and verifyB K ≤ε < BK−1,whereB K−1 is computed from a different
discretization with step sizeh K−1 =T /(K−1). It is not obtained by stopping theKiteration
chain one iteration earlier. Although the Gaussian laws are propagated directly,Kis the number
of updates and full data gradient evaluations that the corresponding sampler would use along
one trajectory. This procedure is repeated for every candidateα. At each accuracy, we choose
the value requiring the smallestKfrom the grid
{0.003,0.01,0.03,0.05,0.1,0.15,0.2,0.3,0.4,0.5,0.7,1,1.5,2}.
We report the results in Figure 2. The first panel compares HFHRMC and KLMC at the
common frictionγ= 2Aand also shows KLMC atγ= 2
√
L. The second panel compares
HFHRMC and KLMC at the common frictionγ=A. In the first panel, the minimizing grid
value isα= 0.03 for the displayed accuracies from 0.3 to 10 −3 andα= 0.01 for 3×10 −4 and
10−4. Atε= 10 −4, HFHRMC requires 548652 iterations, however, KLMC requires 1318015
iterations atγ= 2Aand 2000214 iterations atγ= 2
√
L. In the second panel, the grid selects
α= 0.03 at every displayed accuracy. Atε= 10 −4, HFHRMC requires 1034914 iterations,
compared with 4159467 for KLMC. The decrease in the selectedαin the first panel agrees
qualitatively with Proposition 4.9, which givesα ⋆ ε →0 asε→0.
30

Bayesian linear regression TV convergence
1e-4 1e-3 1e-2 1e-1
1e2
1e3
1e4
1e5
1e6
target TV upper bound epsilon
K iterates
HFHRMC (alpha>0, gamma=2A)
KLMC (alpha=0, gamma=2A)
KLMC (alpha=0, gamma=2sqrt(L))
(a) The friction choicesγ= 2Aandγ= 2
√
L
Bayesian linear regression convergence, gamma=A
1e-4 1e-3 1e-2 1e-1
1e2
1e3
1e4
1e5
1e6
target TV upper bound epsilon
K iterates
HFHRMC (alpha>0)
KLMC (alpha=0) (b) The common frictionγ=A
Figure 2: The numberKof iterations required to satisfyB K ≤εfor the Bayesian linear
regression posterior on wine quality real data. The quantityB K is the analytically computed
χ2-divergence upper bound on joint total variation. Positiveαis selected from the stated
grid separately at each accuracy. For the corresponding sampler,Kis also the number of full
data gradient evaluations along one trajectory. Both axes are logarithmic. We noteγ= 2
√
L
corresponds to [CCBJ18].
5.3 Bayesian logistic regression on real data
We next conduct a Bayesian logistic regression experiment using the UCI Breast Cancer Wis-
consin Diagnostic data set. 2 We use a fixed stratified subset with 96 training and 64 test
observations. The six features are radius, texture, smoothness, compactness, concavity, and
number of concave points, all measured from the original image. Standardization uses training
statistics only, after which the design is multiplied by 0.65. With a standard Gaussian prior,
the posterior potential is
U(β) = 1 2 |β|2 + 96X i=1 h log  1 +e x⊤ i β  −y ix⊤ i β i .
It satisfies
I6 ⪯ ∇2U(β)⪯

1 + 1 4 ∥X∥ 2 op

I6,
so that we use the lower boundm= 1 andR= 0, and the scaled design givesL≤39.7118.
We use a weighted importance sample with 60000 proposal draws as the numerical posterior
reference. Its effective sample size is 45100.5, or 75.17% of the proposal size.
Withm= 1, we haveA= 1 and chooseγ= 2A= 2. Sincer 0(2) = 2/9, we setα= 2/9,
which increasesr(α, γ) in (90) from 2/9 to 4/9, and useh= 0.30/
√
L= 0.047606. This
choice follows the continuous time rate proxy, whereasα ⋆ ε in Proposition 4.9 minimizes the
discrete complexity bound. The comparisons are KLMC with the sameγandh, and KLMC
withγ= 2
√
L= 12.6035 andh= 0.50/
√
L= 0.079343. For every ensemble,Q 0 andP 0
are independent standard Gaussian arrays, and all configurations share these arrays and the
random number streams. Each method performsK max = 500 iterations using 24 independent
ensembles of 384 particles. The curves report ensemble means and pointwise 95% Studentt
confidence intervals.
To define posterior convergence, consider one ensemble afterKiterations withM= 384
coefficient particles
n
β(j) K oM j=1 . Let n eβ(s), ωs oS s=1 denote the weighted numerical reference,
whereS= 60000,ω s ≥0, and PS s=1 ωs = 1. The two empirical posterior laws arebν K =
1
M
PM
j=1 δβ(j) K andbνref = PS s=1 ωsδ eβ(s). For each of the 96 fixed unit directionsv ℓ, let bF −1 K,ℓ
2The data set is available from the UCI Machine Learning Repository, DOI 10.24432/C5DW2B.
31

be the empirical quantile function of (v ⊤ ℓ ·)#bνK. For the weighted reference, let bF −1 ref,ℓ be the
interpolated projected quantile curve obtained from the cumulative weight midpoints used in
the computation. WithJ= 512 andu r = (r−1/2)/J, the plotted posterior convergence
diagnostic is
Dpost(K) =
"
1
96J
96X
ℓ=1
JX
r=1

 bF −1 K,ℓ(ur)− bF −1 ref,ℓ (ur)

 2 #1/2 .
ThusD post is the slicedW 2 approximation computed with 96 directions and 512 quantile levels.
It compares projected coefficient distributions rather than a single posterior moment.
To define posterior mean probability convergence, writep β(xi) =σ(x ⊤ i β), whereσ(z) =
(1 +e −z)−1, for the positive class probability at theith test input. The current and reference
posterior mean probabilities and their discrepancy are
pK(xi) = 1 M MX j=1 pβ(j) K (xi), pref (xi) = SX s=1 ωsp eβ(s)(xi),
Dmean(K) =
"
1
64
64X
i=1
|pK(xi)− pref (xi)|2
#1/2
.
Thus,D mean is the RMSE of the posterior expected class probabilities over the 64 test inputs.
It measures convergence of the posterior predictive mean, not convergence of the entire poste-
rior distribution or classification accuracy. Figure 3 reports both diagnostics. Over the fixed
transient window 0≤K≤240, the slicedW 2 areas under the curve are 28.4475, 46.3072, and
61.2117 for HFHRMC, KLMC atγ= 2, and KLMC atγ= 2
√
L, respectively. The correspond-
ing posterior mean probability RMSE areas are 2.9340, 5.3162, and 7.3604. For slicedW 2, the
first recorded values after which the upper confidence limit remains below 0.10 areK= 53, 77,
and 164, respectively. For probability RMSE, the corresponding values for the threshold 0.02
areK= 30, 53, and 93. Over the late window 280≤K≤500, the coefficients of variation
remain below 6.5% for both diagnostics and all configurations. Since each iteration uses one full
data gradient evaluation, HFHRMC reaches both thresholds with fewer gradient evaluations.
Logistic posterior convergence
0 100 200 300 400 500
1e-1
1e0
K iterates
sliced-W2 to reference posterior
HFHRMC (alpha=2/9, gamma=2)
KLMC (alpha=0, gamma=2)
KLMC (alpha=0, gamma=2sqrt(L))
(a) Posterior convergence
Logistic posterior mean probability convergence
0 100 200 300 400 500
1e-2
1e-1
K iterates
posterior-mean probability RMSE
HFHRMC (alpha=2/9, gamma=2)
KLMC (alpha=0, gamma=2)
KLMC (alpha=0, gamma=2sqrt(L)) (b) Posterior mean probability convergence
Figure 3: Convergence for the real data Bayesian logistic posterior. Solid curves are independent
ensemble means and shaded regions are pointwise 95% confidence intervals. The horizontal axis
reportsKiterates. The state shown atKhas used exactlyKfull data gradient evaluations
along each particle trajectory. We noteγ= 2
√
Lcorresponds to [CCBJ18].
5.4 Bayesian neural network with bounded weights and biases on real data
The final experiment is conducted for a Bayesian neural network with bounded weights and
biases on real data; it uses the same training and test split with the standardized radius and
32

texture features. Letθ∈R 13 be the latent parameter of a tanh network with two inputs, three
hidden units, and one output. Its 13 physical weights and biases are obtained coordinatewise
from
ϑj = 1.5 tanh(θj)∈(−1.5,1.5), j= 1, . . . ,13,
and the latent prior isθ∼ N(0,I 13). Thus boundedness refers to the transformed weights
and biases used by the network. The posterior of the latent variableθhas supportR 13, and its
pushforward under the coordinatewise tanh map is supported on (−1.5,1.5) 13. The transforma-
tion pushes the Gaussian latent prior forward to a nonuniform prior supported on (−1.5,1.5) 13.
Bounded parameter classes have also been used in Bayesian neural network theory. In par-
ticular, [PR18] uses a uniform slab on [−1,1] for active network parameters, [KK25] proves
posterior concentration using approximation by fully connected networks with bounded param-
eters. Unlike the slab construction in [PR18], the tanh map gives a smooth unconstrained
parametrization for the Langevin dynamics.
Since the output layer has three weights and one bias, the network logit satisfies|a θ(x)| ≤6.
Ifa θ(x) denotes this logit, the Gibbs posterior potential is
U(θ) = 1 2 |θ|2 + 6 96 96X i=1 h log  1 +e aθ(xi)  −y iaθ(xi) i .
Fory∈ {0,1}, the oscillation of log(1 +e a)−yaovera∈[−6,6] equals 6. Consequently, ifW
denotes the data term inU, then osc(W)≤36. The bounded perturbation principle [HS87],
applied to the Gaussian latent prior, it gives a Poincar´ e inequality for the posterior. The finite
data set and the smooth bounded derivatives of tanh also imply that∇Uis globally Lipschitz,
and the posterior can be nonconvex. This example therefore satisfies the structural assumptions
in a nonconvex setting, although we do not use the resulting conservative constants to tune the
sampler. A weighted prior importance sample with 50000 draws defines the numerical reference
and has effective sample size 14145.1, or 28.29%.
We compare HFHRMC with (α, γ, h) = (0.4,1,0.03) and KLMC with (α, γ, h) = (0,1,0.03).
These parameters compare the methods at commonγandhrather than optimize over sampler
parameters. We initializeQ 0 ∼ N(s,I13), where the entries ofsare equally spaced from−0.7
to 0.7, andP 0 ∼ N(0,I13). Both methods use the same initial arrays, random number streams,
friction, and step size. Each method performsK max = 260 iterations and produces states
indexed byK= 0, . . . ,260. The state atKhas therefore used exactlyKfull data gradient
evaluations along each particle trajectory. We run 12 independent ensembles of 384 particles.
For a latent parameterθ, define its vector of test probabilities by
fθ = (pθ(x1), . . . , pθ(x64)), p θ(xi) =σ(a θ(xi)).
To avoid hidden unit permutation ambiguity, we use the same finite direction formula and
projected quantile interpolation asD post for the empirical and weighted reference laws off θ in
[0,1] 64, again using 96 fixed directions and 512 quantile levels. The first Bayesian neural network
(BNN) panel compares the posterior laws of predictive probability vectors, which are invariant
under hidden unit permutations, rather than distances between latent parameter vectors. We
use the formula forD mean withp β replaced byp θ, so the second panel measures the RMSE of the
posterior mean probability vector relative to the numerical reference. It measures a posterior
mean rather than a second distributional distance.
Figure 4 reports both diagnostics. Over the recorded checkpoints spanningK= 0 to
K= 260, the areas under the slicedW 2 curve for the predictive probability distribution are
7.3413 for HFHRMC and 9.8377 for KLMC. The posterior mean probability RMSE areas are
6.1325 and 8.9156, respectively. Over the recorded checkpoints withK≥151, the slicedW 2
coefficients of variation are 1.69% and 3.51%, and the probability RMSE coefficients of variation
are 5.63% and 7.27%. Thus, HFHRMC has lower empirical areas under both reported error
curves over the 260 iteration budget and lower late window variability.
33

BNN predictive distribution convergence
0 52 104 156 208 260
0
0.05038
0.1008
0.1511
0.2015
0.2519
K iterates
predictive-function sliced-W2
HFHRMC (alpha=0.4, gamma=1)
KLMC (alpha=0, gamma=1)
(a) Predictive distribution convergence
BNN posterior mean probability convergence
0 52 104 156 208 260
0
0.05866
0.1173
0.176
0.2346
0.2933
K iterates
posterior-mean probability RMSE
HFHRMC (alpha=0.4, gamma=1)
KLMC (alpha=0, gamma=1) (b) Posterior mean probability convergence
Figure 4: Convergence for the Bayesian neural network with transformed physical weights and
biases in (−1.5,1.5). Solid curves are independent ensemble means and shaded regions are
pointwise 95% confidence intervals. The horizontal axis reportsKiterates. The state shown at
Khas used exactlyKfull data gradient evaluations along each particle trajectory.
6 Conclusion
We established an explicitL2(π) convergence rate for HFHR dynamics under a position Poincar´ e
inequality and weighted regularity assumptions, without requiring convexity of the potential.
The estimate combines the hypocoercive ULD contribution with the direct position-diffusion
contribution and is uniform at the ULD endpointα= 0. The main analytic ingredient is an
HFHR-adapted time–augmented Poincar´ e inequality, in which the position diffusion is handled
through the position regularity of the divergence test rather than through a velocity negative
Sobolev norm. As a by-product, we also obtained explicit convergence inχ 2 divergence and
total variation forL 2 initial densities. For the discrete-time HFHRMC algorithm, we obtained a
non-asymptotic convergence bound and iteration complexity by using a path-space KL estimate
without a separate time-uniform moment-stability assumption. Our results hold throughout the
parameter spaceα≥0,γ >0, remain regular at the ULD endpoint, and therefore allow un-
constrained parameter tuning. The optimized positive position diffusion gives a finite-accuracy
improvement, while the leading high-accuracy order agrees with that of the separately opti-
mized ULD endpoint. Our iteration complexity improves upon the existing works on HFHR
algorithms. The numerical experiments complemented these results including the Bayesian
learning problems on real data. They illustrated the effect and benefit of positiveαfor the
HFHRMC algorithm.
A Weighted Elliptic Estimates
This appendix supplies the analytic ingredients for the divergence construction. They are the
time-augmented versions of the estimates in [CL W23, Lemmas 2.4 and 2.6]. We use the notation
of Section 2 onI×R d, with measureλ T ⊗µ; no spatial boundary is present.
We begin by tensorizing the position Poincar´ e inequality with the Neumann Poincar´ e in-
equality in time. This provides coercivity for the mixed time–position operator.
Lemma A.1(Time–position Poincar´ e inequality).For everyu∈H 1(λT ⊗µ),
∥u−(u) λT ⊗µ∥2 L2 ≤ 1 m ∥∇qu∥2 L2 + T 2 π2 ∥∂tu∥2 L2 ≤max  1 m , T 2 π2   e∇u  2 L2 .(110)
Proof.Writeu t(q) =u(t, q) and ¯u(t) =
R
Rd ut dµ. Variance decomposition and Assumption 2.1
give Z
I
∥ut −¯u(t)∥2 L2(µ) dλT (t)≤ 1 m ∥∇qu∥2 L2 .
34

The Neumann Poincar´ e inequality on (0, T) gives
∥¯u−(¯u)λT ∥2 L2(λT ) ≤ T 2 π2 ∥∂t ¯u∥2 L2(λT ) ≤ T 2 π2 ∥∂tu∥2 L2 .
The two components are orthogonal, which proves (110).
The unbounded coefficient∇Uappears when the Hamiltonian operator acts on the diver-
gence test. Assumption 2.2 gives the following weighted multiplier estimate.
Lemma A.2(Control of multiplication by∇U).Under Assumption 2.2, everyφ∈H 1(λT ⊗µ)
satisfies
∥φ∇U∥ 2 L2 ≤16∥∇ qφ∥2 L2 + 4M d∥φ∥2 L2 .(111)
Proof.Weighted integration by parts gives
Z
I×R d
φ2 |∇U| 2 dλT dµ=
Z
I×R d
∇q ·(φ 2∇U) dλT dµ
= 2
Z
I×R d
φ∇qφ· ∇UdλT dµ+
Z
I×R d
φ2∆Udλ T dµ.
Young’s inequality and (11) bound the right-hand side by
 1
4 + δ 2  ∥φ∇U∥ 2 L2 + 4∥∇ qφ∥2 L2 +M d∥φ∥2 L2 .
Sinceδ <1, absorption proves the claim.
The divergence construction also requires second-order regularity. The next weighted
Bochner estimate controls it in terms of the curvature parameterR.
Lemma A.3(Time–positionH 2 estimate).Supposeu∈H 2(λT ⊗µ)and the boundary terms
in the time integration by parts vanish; in particular this holds when e∇u∈H 1 0 (λT ⊗µ) d+1.
Then, D2 t,qu 2 L2 ≤C  ∥Au∥ 2 L2 +R 2 ∥∇qu∥2 L2  .(112)
The spatial companion is
∇2 qu 2 L2 ≤C ∇∗ q∇qu 2 L2 +R 2 ∥∇qu∥2 L2  .(113)
Proof.The integrated weighted Bochner identity is
D2 t,qu 2 L2 =∥Au∥ 2 L2 − Z I×R d (∇qu)⊤∇2U(∇ qu) dλT dµ.(114)
For convexU, the last term is nonpositive and (112) holds withR= 0. If∇ 2U⪰ −KId, it is
bounded byK∥∇ qu∥2 L2, givingR= √ K.
In the general case, (10) and Cauchy–Schwarz inequality yield

 Z I×R d (∇qu)⊤∇2U(∇ qu) dλT dµ

 ≤M √ d∥∇ qu∥2 +M∥∇ qu∥ ∥|∇U| |∇qu|∥.
Apply Lemma A.2 to each component of∇ qu:
∥|∇U| |∇qu|∥2 ≤16 D2 t,qu 2 + 4M d∥∇qu∥2 .
35

Young’s inequality therefore gives

 Z I×R d (∇qu)⊤∇2U(∇ qu) dλT dµ

 ≤ 1 2 D2 t,qu 2 +C  M 2 +M 3/2d1/2  ∥∇qu∥2 .
Absorb
D2 t,qu 2 /2 into the left-hand side of (114) and note that
M 2 +M 3/2d1/2 ≤C  M+M 3/4d1/4 2 .
This proves (112). The proof of (113) is identical without the time coordinate.
Recall thatA q is the nonnegative self-adjoint operator associated with the closed form
z7− → ∥∇qz∥2 L2(µ) onH 1(µ).
ThusA q is the Friedrichs realization of∇ ∗ q∇q =−∆ q +∇U· ∇q. We first identify its operator
domain without using translations of the Gibbs weight.
Lemma A.4(Position operator core and domain regularity).The operator
Amin q z=−∆ qz+∇U· ∇qz, D(A min q ) =C ∞ c (Rd),
is essentially self-adjoint inL 2(µ). Consequently,C ∞ c (Rd)is an operator core forA q, and
D(Aq)⊂H 2(µ), ∇2 qz 2 L2(µ) ≤C  ∥Aqz∥2 L2(µ) +R 2 ∥∇qz∥2 L2(µ)  .(115)
Forz∈D(A q), the identity
Aqz=−∆ qz+∇U· ∇qz
holds inL 2(µ).
Proof.The minimal operator is symmetric and nonnegative by weighted integration by parts.
For a densely defined nonnegative symmetric operatorB, the condition ker(B ∗ + 1) ={0}is
equivalent to density of Ran(B+ 1). Let Bbe its closure. The estimate
(B+ 1)z  ≥ ∥z∥,
together with closedness of B, makes Ran( B+ 1) closed. It contains the dense range ofB+ 1,
so it equals the whole Hilbert space; a closed symmetric operator with−1 in its resolvent is
self-adjoint. We therefore verify
ker

(Amin q )∗ + 1  ={0}.
Letzbelong to this kernel. Since the density ofµis positive and locally bounded above and
below,z∈L 2 loc. The distributional equation
−∆qz+∇U· ∇qz+z= 0,
and local elliptic regularity givez∈H 2 loc. Chooseχ∈C ∞ c (Rd), with 0≤χ≤1, equal to one
on the unit ball, and putχ R(q) =χ(q/R). Testing the equation byχ 2 Rz, justified by compactly
supportedH 1 approximation, gives
∥χRz∥2 L2(µ) +
Z
Rd
χ2 R |∇qz|2 dµ=−2
Z
Rd
χRz∇ qχR · ∇qzdµ.
Young’s inequality therefore yields
∥χRz∥2 L2(µ) + 1 2 Z Rd χ2 R |∇qz|2 dµ≤ C R2 ∥z∥2 L2(µ) .
36

LettingR→ ∞provesz= 0. HenceA min q is essentially self-adjoint, and its closure is the
Friedrichs operatorA q.
Now letz∈D(A q). There arez n ∈C ∞ c (Rd) such thatz n →zandA qzn →A qzinL 2(µ).
Forw=z n −z k,
∥∇qw∥2 L2(µ) =⟨A qw, w⟩L2(µ) ≤ ∥Aqw∥L2(µ) ∥w∥L2(µ) .
Thusz n is Cauchy inH 1(µ). Applying the spatial Bochner estimate (113) toz n −z k shows that
its spatial Hessians are also Cauchy inL 2(µ). Local equivalence of weighted and unweighted
norms identifies the limits as the weak derivatives ofz, provingz∈H 2(µ); passage to the limit
also proves (115). Finally, Lemma A.2, applied to each component of∇ qz, gives
∥|∇U| |∇qz|∥2 L2(µ) ≤16 ∇2 qz 2 L2(µ) + 4M d∥∇qz∥2 L2(µ) .
The claimedL 2 realization ofA q follows by passing to the limit in the distributional identity
forz n.
We next apply the preceding coercivity and Bochner estimates to the mixed Neumann
problem. Its solution supplies the elliptic potentials used in the divergence construction.
Lemma A.5(Mixed elliptic regularity).Leth∈H −1(λT ⊗µ)have zero mean. There is a
unique mean-zero weak solutionu∈H 1(λT ⊗µ)of
Au=h, ∂ tu(0,·) =∂ tu(T,·) = 0.(116)
Ifh∈L 2, thenu∈H 2 and
 e∇u  2
L2
≤max
 1
m , T 2 π2  ∥h∥2 L2 .(117)
Moreover,
∥∂ttu∥2 L2 + 2∥∂ t∇qu∥2 L2 +∥A qu∥2 L2 =∥h∥ 2 L2 ,(118)
and D2 t,qu 2 L2 ≤C  1 +R 2 max  1 m , T 2 π2  ∥h∥2 L2 .(119)
Proof.On
V0 =

v∈H 1(λT ⊗µ) : (v) λT ⊗µ = 0 	 ,
consider
B(u, v) =⟨∂tu, ∂tv⟩+⟨∇ qu,∇ qv⟩.
Lemma A.1 makesBcoercive onV 0. The Lax–Milgram theorem [Ouh05, Lemma 1.3] gives a
unique weak solution. Testing byu, applying Cauchy–Schwarz inequality, and then using (110)
proves (117).
For theL 2 regularity, letB t be the nonnegative Neumann operator−∂ tt inL 2(λT ). We
writeH 1 b⊗H 2 for the Hilbert-space tensor product, namely the completion of the algebraic
tensor product in its canonical Hilbert norm. The mapf⊗g7→[(t, q)7→f(t)g(q)] extends to
a canonical unitary identification
L2(λT ⊗µ)≃L 2(λT ) b⊗L 2(µ);
see [Sch12, Definition 7.2 and Example 7.9]. Under this identification, the operatorsB t ⊗I and
I⊗A q are nonnegative self-adjoint operators, their algebraic sum is essentially self-adjoint, and
they strongly commute [Sch12, Theorem 7.23 and Lemma 7.24]. The operator associated with
37

the formBis the closure of that sum. Therefore the weak solution above is the joint-spectral
solution
u= (B t ⊗I + I⊗A q)−1h
on the orthogonal complement of the constants, by the joint functional calculus [Sch12, Propo-
sition 5.25]. This inverse is bounded there by Lemma A.1. In the formulas below, tensoring
with the identity operator on the complementary factor is left implicit.
Letσ u be the scalar joint spectral measure ofufor these two operators, with spectral
variables (b, a). Sinceh= (a+b)uin this representation,
∥h∥2 L2 =
Z
[0,∞)2
(a+b) 2 dσu(b, a) =∥Btu∥2 L2 +∥A qu∥2 L2 + 2   B1/2 t ⊗A 1/2 q  u  2 L2 .
The form domains ofB t andA q areH 1(0, T) andH 1(µ), respectively. Tensor-product approx-
imation consequently identifies
Btu=−∂ ttu,
  B1/2 t ⊗A 1/2 q  u  L2 =∥∂ t∇qu∥L2 .
This proves (118), including the Neumann time traces encoded inD(B t).
Finally,u∈D(I⊗A q). Lemma A.4, applied in the direct integral over time, and (117) give
∇2 qu 2 L2 ≤C  ∥Aqu∥2 L2 +R 2 max  1 m , T 2 π2  ∥h∥2 L2  .
Together with (118), this provesu∈H 2 and (119).
B Spectral Construction of the Divergence Test
We now prove Lemma 3.14. The proof is included to make clear both the role of compact
embedding and the origin of theT, m, Rdependence. It follows the construction of [CL W23,
Lemma 2.6].
Position spectrum and harmonic decomposition.The closed quadratic formv7− →
∥∇qv∥2 L2(µ) has associated operatorA q =∇ ∗ q∇q. Assumption 2.3 makes the resolvent ofA q, re-
stricted to mean-zero functions, compact. Hence [Sch12, Proposition 5.12] gives an orthonormal
basis{1} ∪ {wj :j≥1}ofL 2(µ) such that
Aqwj =ω 2 j wj, ω j ≥ √m.(120)
The eigenfunctions lie inH 2(µ) by Lemma A.4. Moreover,
⟨∇qwi,∇ qwj⟩L2(µ) =ω 2 j δij.(121)
Let
H:=

v∈L 2(λT ⊗µ) :Av= 0 in distributions 	 .
This is a closed subspace ofL 2. Decompose the centered datum as
h=h h +h ⊥, h h ∈ H, h⊥ ⊥ H.
38

The component orthogonal to harmonic functions.Letube the mean-zero solution of
Au=h ⊥, ∂ tu(0,·) =∂ tu(T,·) = 0,
given by Lemma A.5. For every smoothv∈ H, integration by parts gives
0 =⟨h ⊥, v⟩=⟨u,Av⟩+
Z
Rd
[u(T)∂ tv(T)−u(0)∂ tv(0)] dµ.
For thej-th nonconstant position mode, the functionse ωj twj ande −ωj twj make the pair
(∂tv(0), ∂tv(T)) arbitrary in the span ofw j. Thus all nonconstant components ofu(0,·) and
u(T,·) vanish. In the constant position mode, affine harmonic tests show that the two endpoint
constants agree. Subtracting this common constant fromu, which changes neither the equation
nor any estimate below, we may arrange
u(0,·) =u(T,·) = 0.
Thus both∂ tuand∇ quhave zero traces. Set
ϕ⊥ 0 =∂ tu, ψ ⊥ =u.(122)
Then
−∂tϕ⊥ 0 +A qψ⊥ =h ⊥.
Lemma A.5 gives ϕ⊥ 0  + ∇qψ⊥  ≤C  1√m +T  ∥h⊥∥.(123)
Because all first derivatives ofuvanish at the time endpoints, Lemma A.3 also gives
∇qϕ⊥ 0  + ∂t∇qψ⊥  + ∇2 qψ⊥  ≤C  1 + R√m +RT  ∥h⊥∥.(124)
The right-hand sides of (123) and (124) are bounded respectively byCB 0(T)∥h ⊥∥and
CB1(T)∥h ⊥∥.
Expansion of the harmonic component.Expandh h in the position eigenbasis. The
equationAh h = 0 implies
hh(t, q) =c0

t− T 2  + X j≥1  c+ j e−ωj t +c − j e−ωj (T−t)  wj(q).(125)
The additive constant in the zero position mode vanishes becauseh h is centered.
The two exponentials belonging to the samejare not orthogonal, but their Gram matrix
can be computed explicitly. Withx=ω jT, it is
 dx e−x
e−x dx

, d x = 1−e −2x 2x .
Its smaller eigenvalue is
dx −e −x =e −x
 sinhx
x −1

.
For 0< x≤1, the series of sinhxand 1−e −x ≤xgive
dx −e −x ≥cx 2 ≥c (1−e −x)3 x .
39

Forx≥2, the boundxe −x ≤2e −2 givesd x −e −x ≥c/x, while the same conclusion on [1,2]
follows by continuity and strict positivity. Thus, for allx >0,
dx −e −x ≥c (1−e −x)3 x .(126)
Applying (126) mode by mode gives
∥hh∥2 L2 ≥ c2 0T 2 12 +c X j≥1  (c+ j )2 + (c− j )2  (1−e −ωj T )3 ωjT .(127)
A scalar mode construction.Fixω >0, setϑ=e −ωT , and define
Gϑ(s) := 6s(s−ϑ)(1−s) (1−ϑ) 2 , ϑ≤s≤1.(128)
It satisfies
Gϑ(ϑ) =G ϑ(1) = 0,
Z 1
ϑ
Gϑ(s)
s ds= 1−ϑ.
Set
bω(t) := 1 ω2 Gϑ(e−ωt), a ω(t) := Z t 0  ω2bω(r)−e −ωr dr.(129)
The integral identity forG ϑ shows that
aω(0) =a ω(T) =b ω(0) =b ω(T) = 0,
and the defining equation is
−a′ ω(t) +ω 2bω(t) =e −ωt.(130)
For completeness, the estimates (131)–(135) are obtained by the change of variabless=e−ωt.
The elementary bounds
0≤G ϑ(s)≤ 3 2 s,

G′ ϑ(s)

 ≤ C 1−ϑ
and dt=−ds/(ωs) give
ω4 ∥bω∥2 L2(λT ) = 1 ωT Z 1 ϑ Gϑ(s)2 s ds≤C 1−ϑ 2 ωT ,(131)
ω2 b′ ω 2 L2(λT ) = 1 ωT Z 1 ϑ sG′ ϑ(s)2 ds≤ C ωT(1−ϑ) .(132)
Writing
aω(t) = 1 ω Rϑ(e−ωt), R ϑ(s) = Z 1 s  Gϑ(r) r −1  dr= (s−ϑ)(1−s)(1 +ϑ−2s) (1−ϑ) 2 ,
we obtain, after settings=ϑ+ (1−ϑ)y,
Z 1
ϑ
Rϑ(s)2
s ds≤C(1−ϑ) 3.
Consequently,
ω2 ∥aω∥2 L2(λT ) ≤C (1−ϑ) 3 ωT .(133)
Sincea ′ ω =G ϑ(s)−sand|G ϑ(s)−s| ≤s, the same change of variables gives
a′ ω 2 L2(λT ) ≤C 1−ϑ 2 ωT .(134)
40

Finally, direct differentiation gives
b′′ ω(t) =sG ′ ϑ(s) +s 2G′′ ϑ(s),

b′′ ω(t)

 ≤ Cs (1−ϑ) 2 ,
and therefore,
b′′ ω 2 L2(λT ) ≤C 1−ϑ 2 ωT(1−ϑ) 4 .(135)
The estimates (131), (132), and (133) will be used to prove (138)–(142). The estimates (134)
and (135) provide the additional time regularity in (143)–(144).
For the reversed exponential, define
eaω(t) =−a ω(T−t), ebω(t) =b ω(T−t).
Then,
−ea′ ω(t) +ω 2ebω(t) =e −ω(T−t) ,
and all endpoint traces still vanish.
Assembly and estimates.The zero position mode in (125) is handled by
ϕ(0) 0 (t) =− c0 2 (t2 −T t), ψ (0) = 0.
Define
ϕh 0 :=ϕ (0) 0 + X
j≥1
h
c+ j aωj (t)−c − j aωj (T−t) i wj,(136)
ψh := X
j≥1
h
c+ j bωj (t) +c − j bωj (T−t) i wj.(137)
Equations (130) and (120) imply that
−∂tϕh 0 +A qψh =h h.
Every term inϕ h 0 and∇ qψh has zero trace att= 0, T. We first work with finite spectral sums;
passage to the infinite sum is justified after deriving all required Sobolev estimates.
We next sum the estimates (131), (132), and (133) overjin the expansions (136)–(137).
Orthogonality and (133) give
ϕh 0  2 ≤C  T 2 + 1 m  ∥hh∥2 .
By (131), (120), and (127),
∇qψh  2 ≤ C m(1−e −√mT )2 ∥hh∥2 .
Together, these estimates imply
ϕh 0  + ∇qψh  ≤CB 0(T)∥h h∥.(138)
Similarly, (133) gives
∇qϕh 0  ≤C∥h h∥,(139)
41

while (132) gives
∂t∇qψh  ≤ C (1−e −√mT )2 ∥hh∥.(140)
Finally, apply the spatial Bochner estimate (113) at each time. Since
Aqψh = X
j≥1
ω2 j
h
c+ j bωj (t) +c − j bωj (T−t) i wj,
orthogonality, (131), andω j ≥ √myield
∇2 qψh  ≤C  1 1−e −√mT + R√m(1−e −√mT )  ∥hh∥.(141)
The right-hand sides of (139), (140) and (141) are bounded byCB 1(T)∥h h∥; hence,
∇qϕh 0  + ∂t∇qψh  + ∇2 qψh  ≤CB 1(T)∥h h∥.(142)
It remains to justify the full Sobolev regularity and the infinite spectral sums. Let
ηT := 1−e −√mT >0.
Comparing (134) with (127), and using 1−e −ωj T ≥η T , gives
∂tϕh 0  2 L2 ≤C  1 +η −2 T  ∥hh∥2 L2 .(143)
Similarly, (135) yields ∂ttψh  2 L2 ≤Cη −6 T ∥hh∥2 L2 .(144)
Indeed, for each nonconstant mode the ratio of the right-hand side in (135) to the spectral
weight in (127) is bounded by
C 1 +e −ωj T
(1−e −ωj T )6 ≤Cη −6 T .
Bothψ h and∂ tψh have zero position mean. The position Poincar´ e inequality, together with
(138) and (142), therefore controls theirL 2 norms by those of∇ qψh and∂ t∇qψh. Equations
(143)–(144) now show
ϕh 0 ∈H 1 0 (λT ⊗µ), ψ h ∈H 2(λT ⊗µ).
For completeness, leth >N h denote the part of (125) withj > N. Orthogonality of the
position modes gives
h>N h  L2 →0. Apply (138), (142), (143), and (144) to this tail. The
corresponding tails ofϕ h 0 andψ h converge to zero inH 1 andH 2, respectively. Thus the finite
spectral sums are Cauchy in the asserted spaces. Continuity of the trace maps preserves the
zero endpoint traces, and the divergence equation passes to the limit in distributions.
Set
ϕ0 :=ϕ ⊥ 0 +ϕ h 0, ψ:=ψ ⊥ +ψ h.
The two components solve the divergence equation, have the required time traces, and satisfy
the desired estimates by (123)–(124) and (138)–(142). This completes the proof of Lemma 3.14.
42

C Weighted Kinetic Density, Traces, and Green’s Formula
This appendix proves the weighted whole-space kinetic trace result used in Proposition 3.13.
It is the analogue, in the Gibbs space and without a spatial boundary, of the density and
trace arguments in [AAMN24, Proposition 2.2, Proposition 6.1, and Lemma 6.12]. The proof
is included because the force∇Uneed not be bounded.
In this appendix, we set
H:=L 2(π), V p :=L 2  µ;H 1 κ  , V ∗ p :=L 2  µ;H −1 κ  ,
so thatV p ⊂H⊂V ∗ p . We use ordinary Lebesgue measure in time; replacing it byλ T only
rescales the norms. Recall
K0 =∂ t − Lham,L ham =p· ∇q − ∇U(q)· ∇p.
The trace argument requires approximation by smooth functions in the kinetic graph norm.
The following lemma handles both the unbounded Gaussian velocity multiplier and the whole-
space cutoffs.
Lemma C.1(Gaussian multiplier and local graph density).For everyg∈L 2(κ)and1≤i≤d,
∥pig∥H −1 κ ≤C∥g∥ L2(κ) .(145)
LetI⊂Rbe an open interval and let
u∈L 2(I;V p), F:=K 0u∈L 2(I;V ∗ p ).
For everyJ⋐I, there areu n ∈C ∞ c (I×R 2d)such that, asn→ ∞,
un − →uinL 2(J;V p),K 0un − →FinL 2(J;V ∗ p ).(146)
Proof.Forφ∈H 1 κ, Gaussian integration by parts and Young’s inequality give
Z
Rd
p2 i φ2 dκ=
Z
Rd

φ2 + 2piφ ∂piφ  dκ≤ ∥φ∥2 L2(κ) + 1 2 ∥piφ∥2 L2(κ) + 2∥∂ piφ∥2 L2(κ) .
Thus multiplication byp i mapsH 1 κ continuously intoL 2(κ). Duality proves (145).
Chooseη∈C ∞ c (I) equal to one on a neighborhood ofJ. Replacingubyηuintroduces only
the graph termη ′u, since
K0(ηu) =ηF+η ′u.
It therefore suffices to approximate a function compactly supported in time.
Letχ∈C ∞ c (Rd), with 0≤χ≤1, equal one on the unit ball, and putχ R(q) =χ(q/R).
Then
K0(χRu) =χ RF−(p· ∇qχR)u.(147)
The first term converges toFinL 2(I;V ∗ p ), while (145) gives
∥(p· ∇qχR)u∥L2(I;V ∗p ) ≤ C R ∥u∥L2(I;H) − →0 asR→ ∞.
Alsoχ Ru→uinL 2(I;V p).
Next fixR, choose an analogous cutoffθ S(p) =χ(p/S), and setu R,S =θ SχRu. Multi-
plication byθ S is uniformly bounded onH 1 κ, hence also onH −1 κ , and converges strongly to
the identity on both spaces. For the negative space, the latter claim follows first on the dense
subspaceL 2(κ) and then on all ofH −1 κ by uniform boundedness. Moreover,
K0uR,S =θ SK0(χRu) + (∇U· ∇pθS)χRu.(148)
43

Becauseqis now restricted to a fixed compact set,∇Uis bounded there. The last term in
(148) is consequently bounded inL 2(I;H) byC RS−1 ∥u∥L2(I;H) and tends to zero. Taking
firstS→ ∞and then a diagonal sequenceR→ ∞produces compactly supported functions
converging touin the kinetic graph norm.
It remains to smooth such a compactly supported function. On a fixed compact set the
Gibbs density is bounded above and below by positive constants, so weighted and unweighted
local Sobolev norms are equivalent. Chooseρ∈C ∞ c (R1+2d) withρ≥0 and R ρ= 1, and set
ρε(z) :=ε −(1+2d)ρ(z/ε), z= (t, x), x= (q, p).
Writeb(q, p) = (p,−∇U(q)), so thatL ham =b· ∇q,p. On that compact set,bis Lipschitz and
divq,p b= 0. Hence
K0(ρε ∗u) =ρ ε ∗F+C εu,
Cεu(t, x) =
Z
R1+2d
(b(x−y x)−b(x))· ∇yxρε(τ, yx)u(t−τ, x−y x) dτdy x.
The Lipschitz bound gives∥C εu∥L2 ≤C∥u∥ L2, uniformly inε. For smoothu, direct differentia-
tion showsC εu→0 inL 2. Approximation of an arbitraryL 2 function by smooth ones and the
uniform bound give the same conclusion for the presentu. The approximate-identity property,
applied first inH 1 p and then by duality inH −1 p , gives on everyJ⋐I
ρε ∗u→uinL 2(J;V p), ρ ε ∗F→FinL 2(J;V ∗ p ).
Together withC εu→0, these convergences prove (146).
The graph-density result permits the classical smooth integration-by-parts identity to be
passed to weak kinetic solutions. This yields both strong interior time traces and Green’s
formula.
Proposition C.2(Kinetic traces and Green’s formula).Let
u, v∈L 2 loc(I;V p),K 0u,K 0v∈L 2 loc(I;V ∗ p ).
They admit representatives inC(I;L 2(π)), and, for everys, t∈Iwiths < t,
⟨ut, vt⟩L2(π) − ⟨us, vs⟩L2(π) =
Z t
s
h
⟨K0ur, vr⟩V ∗p ,Vp +⟨K 0vr, ur⟩V ∗p ,Vp
i
dr.(149)
If, in addition,u t ⇀ u0 weakly inL 2(π)ast→0and
lim sup
t→0
∥ut∥L2(π) ≤ ∥u0∥L2(π) ,(150)
thenu t →u 0 strongly ast→0. In that case Green ’s formula extends tos= 0. The analogous
statement holds at a finite right endpoint.
Proof.For compactly supported smooth functions, weighted integration by parts gives
⟨Lhamu, v⟩L2(π) +⟨u,L hamv⟩L2(π) = 0.
Indeed, the Hamiltonian vector field is divergence-free and annihilatesU(q) +|p| 2 /2. Conse-
quently,
d
dt ⟨ut, vt⟩L2(π) =⟨K 0ut, vt⟩V ∗p ,Vp +⟨K 0vt, ut⟩V ∗p ,Vp .(151)
44

We first obtain the time trace. Ifwis smooth on a compact intervalJ⋐I, choose a time
r∈Jat which∥w r∥2 H ≤ |J|−1 ∥w∥2 L2(J;H) , and integrate (151) withu=v=w. This yields
sup
t∈J
∥wt∥2 H ≤ 1 |J| ∥w∥2 L2(J;H) + 2∥K 0w∥L2(J;V ∗p ) ∥w∥L2(J;V p) .(152)
Apply Lemma C.1 on a slightly larger compact subinterval. Estimate (152), applied to the
difference of two approximants, shows that the approximants are Cauchy inC(J;H). Their
limit is the desired representative ofu. Representatives obtained on overlapping intervals agree,
givingu∈C(I;H), and similarly forv.
Integrating (151) and passing to the limit in the graph norm proves (149). Finally, (150),
weak lower semicontinuity, and the weak convergence imply convergence of the norms. Weak
convergence together with convergence of norms in a Hilbert space is strong convergence. The
endpoint form of (149) follows by lettings→0.
Taking the same function in both slots of Green’s formula gives the kinetic energy chain
rule used in the construction of the endpoint semigroup.
Corollary C.3(Kinetic chain rule).Supposeusatisfies the local graph conditions of Proposition
C.2 and
K0u=−γ∇ ∗ p∇pu.
Then, fors, t∈Iwiths < t,
1
2 ∥ut∥2 L2(π) +γ
Z t
s
∥∇pur∥2 L2(π) dr= 1 2 ∥us∥2 L2(π) .(153)
If the endpoint hypothesis of Proposition C.2 holds, the identity extends to that endpoint.
Proof.By takingv=uin (149) and using

−γ∇∗ p∇pu, u  V ∗p ,Vp =−γ∥∇ pu∥2 L2(π) ,
we get the desired result.
References
[AAMN24] Dallas Albritton, Scott Armstrong, Jean-Christophe Mourrat, and Matthew No-
vack. Variational methods for the kinetic Fokker–Planck equation.Analysis &
PDE, 17(6):1953–2010, 2024.
[ADFDJ03] Christophe Andrieu, Nando De Freitas, Arnaud Doucet, and Michael I Jordan. An
introduction to MCMC for machine learning.Machine Learning, 50(1):5–43, 2003.
[BBCG08] Dominique Bakry, Franck Barthe, Patrick Cattiaux, and Arnaud Guillin. A simple
proof of the Poincar´ e inequality for a large class of probability measures including
the log-concave case.Electronic Communications in Probability, 13:60–66, 2008.
[BCM+21] Mathias Barkhagen, Ngoc Huy Chau, ´Eric Moulines, Mikl´ os R´ asonyi, Sotirios Sa-
banis, and Ying Zhang. On stochastic gradient Langevin dynamics with dependent
data streams in the logconcave case.Bernoulli, 27(1):1–33, 2021.
[BFLS22] ´Etienne Bernard, Max Fathi, Antoine Levitt, and Gabriel Stoltz. Hypocoercivity
with Schur complements.Annales Henri Lebesgue, 5:523–557, 2022.
45

[BGK+25] Waheed U. Bajwa, Mert G¨ urb¨ uzbalaban, Mustafa Ali Kutbay, Lingjiong Zhu, and
Muhammad Zulqarnain. DIGing-SGLD: Decentralized and scalable Langevin sam-
pling over time-varying networks.arXiv:2511.12836, 2025.
[BS25] Giovanni Brigati and Gabriel Stoltz. How to construct explicit decay rates for
kinetic Fokker–Planck equations?SIAM Journal on Mathematical Analysis,
57(4):3587–3622, 2025.
[CB18] Xiang Cheng and Peter L. Bartlett. Convergence of Langevin MCMC in KL-
divergence. InProceedings of the 29th International Conference on Algorithmic
Learning Theory (ALT), volume 83, pages 186–211. PMLR, 2018.
[CCA+18] Xiang Cheng, Niladri S. Chatterji, Yasin Abbasi-Yadkori, Peter L. Bartlett, and
Michael I. Jordan. Sharp Convergence Rates for Langevin Dynamics in the Non-
convex Setting.arXiv:1805.01648, 2018.
[CCBJ18] Xiang Cheng, Niladri S Chatterji, Peter L Bartlett, and Michael I Jordan. Under-
damped Langevin MCMC: A non-asymptotic analysis. InConference on Learning
Theory, volume 75, pages 300–323. PMLR, 2018.
[CDOP25] Daniel Cortild, Claire Delplancke, Nadia Oudjane, and Juan Peypouquet. Global
optimization algorithm through high-resolution sampling.Transactions on Ma-
chine Learning Research, 2025. Published September 2025.
[CHS87] Tzuu-Shuh Chiang, Chii-Ruey Hwang, and Shuenn Jyi Sheu. Diffusion for global
optimization inR n.SIAM Journal on Control and Optimization, 25(3):737–753,
1987.
[CL W21] Yu Cao, Jianfeng Lu, and Lihan Wang. Complexity of randomized algorithms
for underdamped Langevin dynamics.Communications in Mathematical Sciences,
19(7):1827–1853, 2021.
[CL W23] Yu Cao, Jianfeng Lu, and Lihan Wang. On explicitL 2-convergence rate estimate for
underdamped Langevin dynamics.Archive for Rational Mechanics and Analysis,
247(5):90, 2023.
[CMR+21] Ngoc Huy Chau, ´Eric Moulines, Miklos R´ asonyi, Sotirios Sabanis, and Ying Zhang.
On stochastic gradient Langevin dynamics with dependent data streams: the fully
non-convex case.SIAM Journal of Mathematics of Data Science, 3(3):959–986,
2021.
[Dal17] Arnak S Dalalyan. Theoretical guarantees for approximate sampling from smooth
and log-concave densities.Journal of the Royal Statistical Society: Series B (Sta-
tistical Methodology), 79(3):651–676, 2017.
[DD19] Damek Davis and Dmitriy Drusvyatskiy. Stochastic model-based minimization of
weakly convex functions.SIAM Journal on Optimization, 29(1):207–239, 2019.
[DE97] Paul Dupuis and Richard S. Ellis.A Weak Convergence Approach to the Theory of
Large Deviations. Wiley Series in Probability and Statistics. John Wiley & Sons,
New York, 1997.
[DK19] Arnak S. Dalalyan and Avetik G. Karagulyan. User-friendly guarantees for the
Langevin Monte Carlo with inaccurate gradient.Stochastic Processes and their
Applications, 129(12):5278–5311, 2019.
46

[DM17] Alain Durmus and Eric Moulines. Non-asymptotic convergence analysis for the
Unadjusted Langevin Algorithm.Annals of Applied Probability, 27(3):1551–1587,
2017.
[DM19] Alain Durmus and Eric Moulines. High-dimensional Bayesian inference via the
Unadjusted Langevin Algorithm.Bernoulli, 25(4A):2854–2882, 2019.
[DMS15] Jean Dolbeault, Cl´ ement Mouhot, and Christian Schmeiser. Hypocoercivity for lin-
ear kinetic equations conserving mass.Transactions of the American Mathematical
Society, 367(6):3807–3828, 2015.
[DRD20] Arnak S. Dalalyan and Lionel Riou-Durand. On sampling from a log-concave
density using kinetic Langevin diffusions.Bernoulli, 26(3):1956–1988, 2020.
[Ebe16] Andreas Eberle. Reflection couplings and contraction rates for diffusions.Proba-
bility Theory and Related Fields, 166(3–4):851–886, 2016.
[EGZ19] Andreas Eberle, Arnaud Guillin, and Raphael Zimmer. Couplings and quantitative
contraction rates for Langevin dynamics.The Annals of Probability, 47(4):1982–
2010, 2019.
[EHZ22] Murat A Erdogdu, Rasa Hosseinzadeh, and Matthew S. Zhang. Convergence of
Langevin Monte Carlo in chi-squared and R´ enyi divergence. InProceedings of the
25th International Conference on Artificial Intelligence and Statistics, volume 151,
pages 8151–8175. PMLR, 2022.
[FLL26] Zexi Fan, Bowen Li, and Jianfeng Lu. Sharp hypocoercive convergence esti-
mates for underdamped Langevin dynamics via the modifiedL 2 method, 2026.
arXiv:2604.10068v1.
[GCSR95] Andrew Gelman, John B Carlin, Hal S Stern, and Donald B Rubin.Bayesian Data
Analysis. Chapman & Hall/CRC Press, 1995.
[GGHZ21] Mert G¨ urb¨ uzbalaban, Xuefeng Gao, Yunhan Hu, and Lingjiong Zhu. Decentralized
stochastic gradient Langevin dynamics and Hamiltonian Monte Carlo.Journal of
Machine Learning Research, 22(239):1–69, 2021.
[GGZ20] Xuefeng Gao, Mert G¨ urb¨ uzbalaban, and Lingjiong Zhu. Breaking reversibility
accelerates Langevin dynamics for global non-convex optimization. InAdvances in
Neural Information Processing Systems (NeurIPS), volume 33, pages 17850–17862.
Curran Associates, Inc., 2020.
[GGZ22] Xuefeng Gao, Mert G¨ urb¨ uzbalaban, and Lingjiong Zhu. Global convergence of
Stochastic Gradient Hamiltonian Monte Carlo for non-convex stochastic optimiza-
tion: Non-asymptotic performance bounds and momentum-based acceleration.Op-
erations Research, 70(5):2931–2947, 2022.
[GIWZ24] Mert G¨ urb¨ uzbalaban, Mohammad Rafiqul Islam, Xiaoyu Wang, and Lingjiong
Zhu. Generalized EXTRA stochastic gradient Langevin dynamics.arXiv preprint
arXiv:2412.01993, 2024.
[HKS89] Richard A Holley, Shigeo Kusuoka, and Daniel W Stroock. Asymptotics of the
spectral gap with applications to the theory of simulated annealing.Journal of
Functional Analysis, 83(2):333–347, 1989.
[HS87] Richard Holley and Daniel Stroock. Logarithmic Sobolev inequalities and stochastic
Ising models.Journal of Statistical Physics, 46(5–6):1159–1194, 1987.
47

[KK25] Insung Kong and Yongdai Kim. Posterior concentrations of fully-connected
Bayesian neural networks with general priors on the weights.Journal of Machine
Learning Research, 26(94):1–60, 2025.
[Leh25] Joseph Lehec. Convergence in total variation for the kinetic Langevin algorithm.
Mathematical Statistics and Learning, 8(1–2):71–104, 2025.
[Lu26] Jianfeng Lu. A sharp hypocoercive entropy decay estimate for underdamped
Langevin dynamics, 2026. arXiv:2605.01933v2.
[LZT22] Ruilin Li, Hongyuan Zha, and Molei Tao. Hessian-free high-resolution Nesterov
acceleration for sampling. InProceedings of the 39th International Conference on
Machine Learning, volume 162 ofProceedings of Machine Learning Research, pages
13125–13162. PMLR, 2022.
[MCC+21] Yi-An Ma, Niladri S. Chatterji, Xiang Cheng, Nicolas Flammarion, Peter L.
Bartlett, and Michael I. Jordan. Is there an analog of Nesterov acceleration for
gradient-based MCMC?Bernoulli, 27(3):1942–1992, 2021.
[MR92] Zhi-Ming Ma and Michael R¨ ockner.Introduction to the Theory of (Non-Symmetric)
Dirichlet Forms. Universitext. Springer-Verlag, Berlin, 1992.
[MS14] Georg Menz and Andr´ e Schlichting. Poincar´ e and logarithmic Sobolev inequalities
by decomposition of the energy landscape.The Annals of Probability, 42(5):1809–
1884, 2014.
[MSH02] Jonathan C Mattingly, Andrew M Stuart, and Desmond J Higham. Ergodicity
for SDEs and approximations: locally Lipschitz vector fields and degenerate noise.
Stochastic Processes and their Applications, 101(2):185–232, 2002.
[Nes83] Yurii Nesterov. A method for solving the convex programming problem with con-
vergence rateo(1/k 2).Dokl. Akad Nauk. SSSR, 269:543–547, 1983.
[Nes13] Yurii Nesterov.Introductory Lectures on Convex Optimization: A Basic Course,
volume 87. Springer Science & Business Media, 2013.
[NWWZ26] Bingye Ni, Xiaoyu Wang, Yingli Wang, and Lingjiong Zhu. Variance reduction for
stochastic gradient generalized non-reversible Langevin Monte Carlo algorithms.
arXiv:2606.28808, 2026.
[Ouh05] El Maati Ouhabaz.Analysis of Heat Equations on Domains, volume 31 ofLondon
Mathematical Society Monographs Series. Princeton University Press, Princeton,
NJ, 2005.
[PR18] Nicholas G. Polson and Veronika Roˇ ckov´ a. Posterior concentration for sparse deep
learning. InAdvances in Neural Information Processing Systems, volume 31. Cur-
ran Associates, Inc., 2018.
[RRT17] Maxim Raginsky, Alexander Rakhlin, and Matus Telgarsky. Non-convex learning
via stochastic gradient Langevin dynamics: a nonasymptotic analysis. InPro-
ceedings of the 2017 Conference on Learning Theory, volume 65, pages 1674–1703.
PMLR, 2017.
[RS18] Julien Roussel and Gabriel Stoltz. Spectral methods for Langevin dynamics and
associated error estimates.ESAIM: Mathematical Modelling and Numerical Anal-
ysis, 52(3):1051–1083, 2018.
48

[Sch12] Konrad Schm¨ udgen.Unbounded Self-Adjoint Operators on Hilbert Space, volume
265 ofGraduate Texts in Mathematics. Springer, Dordrecht, 2012.
[SDJS22] Bin Shi, Simon S. Du, Michael I. Jordan, and Weijie J. Su. Understanding the
acceleration phenomenon via high-resolution differential equations.Mathematical
Programming, 195:79–148, 2022.
[Stu10] Andrew M Stuart. Inverse problems: A Bayesian perspective.Acta Numerica,
19:451–559, 2010.
[Tsy09] Alexandre B. Tsybakov.Introduction to Nonparametric Estimation. Springer Series
in Statistics. Springer, New York, 2009.
[TTV16] Yee Whye Teh, Alexandre H Thiery, and Sebastian J Vollmer. Consistency and
fluctuations for stochastic gradient Langevin dynamics.Journal of Machine Learn-
ing Research, 17(1):193–225, 2016.
[Vil09a] C´ edric Villani. Hypocoercivity.Memoirs of the American Mathematical Society,
202(950):iv+141, 2009.
[Vil09b] C´ edric Villani.Optimal Transport: Old and New, volume 338 ofGrundlehren der
mathematischen Wissenschaften. Springer, Berlin, Heidelberg, 2009.
[WWZ26] Xiaoyu Wang, Yingli Wang, and Lingjiong Zhu. Sampling non-log-concave densities
via Hessian-free high-resolution dynamics.arXiv:2601.02725v1, 2026.
[ZADS23] Ying Zhang, ¨Omer Deniz Akyildiz, Theodoros Damoulas, and Sotirios Sabanis.
Nonasymptotic estimates for Stochastic Gradient Langevin Dynamics under local
conditions in nonconvex optimization.Applied Mathematics & Optimization, 87:25,
2023.
[ZCL+23] Matthew Shunshi Zhang, Sinho Chewi, Mufan Bill Li, Krishnakumar Balasubra-
manian, and Murat A. Erdogdu. Improved discretization analysis for underdamped
Langevin monte carlo. InProceedings of the 36th Conference on Learning Theory,
volume 195 ofProceedings of Machine Learning Research, pages 36–71. PMLR,
2023.
[ZOL25] Xinzhe Zuo, Stanley Osher, and Wuchen Li. Gradient-adjusted underdamped
Langevin dynamics for sampling.SIAM/ASA Journal on Uncertainty Quantifi-
cation, 13(4):1735–1765, 2025.
49
