---
title: Backward-Consistent Diffusion Sampling for Sparsely Observed PDE Inverse Problems
url: https://arxiv.org/abs/2610.04624
category: ai-marketing
subcategory: measurement
date: 2026-10
venue: ''
authors:
- Yida Pan
- Muhammad H. Ashiq
- Chanyong Jung
- Yixuan Jia
- Jonah M. Miller
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.04624
pages: 58
chars: 134234
fetched_at: '2026-11-08T13:25:51+00:00'
kb_version: 1
---

# Backward-Consistent Diffusion Sampling for Sparsely Observed PDE Inverse Problems

Backward-Consistent Diffusion Sampling for
Sparsely Observed PDE Inverse Problems
Yida Pan1,†,Muhammad H. Ashiq 1,†,Chanyong Jung 1,Yixuan Jia 1,Jonah M. Miller 2,1,Qing Qu 1,‡,
Ismail R. Alkhouri2,1,‡
1University of Michigan· 2Los Alamos National Laboratory
† Joint first author ‡ Joint last author
Abstract
Recovering Partial Differential Equation (PDE) coefficient fields from extremely sparse observations is
a severely ill-posed inverse problem for which generative machine learning methods (e.g., diffusion
models) have become a leading way to encode the prior. Recent state-of-the-art diffusion solvers
lift these priors to function spaces, finding a physics-consistent reconstruction in the output space
of the diffusion denoiser. We prove that, in a discontinuous PDE setting, output space methods can
result in failure to appropriately minimize the unobserved error with the correct coefficient field.
Consequently, we proposeFunction SpaceBackward-ConsistentSampling (FunBCS), aninput space
optimization approach for solving PDE problems which aims to find the best input such that the
denoiser reconstruction is physics-consistent. We then prove that FunBCS appropriately minimizes
the unobserved error, unlike output space optimization methods. Per our theoretical analysis, we also
provide insights on how to dynamically allocate the number of input space optimization steps used
throughout the sampling process. Our evaluations, across four PDE inverse problems (including the
discontinuous Darcy flow), demonstrate that FunBCS reduces the reconstruction error by27–64%
while running1.4–2.1×faster when compared to the current state-of-the-art.
Keywords:Inverse Problems, Partial Differential Equations, Diffusion Models, Neural Operators, Function
Space, AI for Science
Date:November 5, 2026
Correspondence:ismailal@umich.edu
Resources:Project page·Code
 https://deepthink-umich.github.io
Solution u
500 pts (3%)
Observations of u
 Coeﬃcient a
Ground truth
 DDIS
 FunBCS (ours)
error rate 18.84%
DDIS error
error rate 2.78%
FunBCS error
correct
wrong
rel. ℓ2 4.65%
 rel. ℓ2 0.62%
 0.0000
0.0005
0.0010
0.0015
Figure 1:Darcy reconstruction from3%sparse solution observations (first column). The last two columns
showthereconstructionerror. DDIS,aSOTAoutputspaceoptimizationmethod,misplacesthediscontinuities,
mostly by assigning low permeability to regions where the true field is highly permeable, whereas FunBCS
recovers the discontinuity structure significantly more faithfully.
1
arXiv:2610.04624v2  [cs.LG]  4 Nov 2026

Contents
1 Introduction 3
2 Background 5
3 Analysis of Output Space Optimization Sampling 6
4 Input Space Optimization Sampling in Function Space 8
4.1 Analysis of Input Space Optimization . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
4.2 Allocating Input Space Optimization Steps Across Noise Levels . . . . . . . . . . . . 10
5 Experiments 11
6 Conclusion 12
A Notation 19
B Function Space Diffusion Setup 19
C Extended Related Work 20
C.1 Classical Inverse Solvers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
C.2 Physics-Informed Learning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
C.2.1 Forward Solvers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
C.2.2 Priors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
C.2.3 Inverse Solvers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
C.3 Theoretical Guarantees . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
D Limitations & Future Directions 23
E Overview of Recent Diffusion PDE Inverse Solvers 24
F Experimental Details 25
G The Proposed Scheduling Function 27
G.1 Scheduler Ablations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
G.2 Tuning the Selection Window . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
G.3 Generalizing Scheduling Function to DDIS . . . . . . . . . . . . . . . . . . . . . . . . 31
H Navier–Stokes Spectral Analysis 32
I Additional Experiments 33
I.1 Visualizing Reconstructed Fields & Solutions . . . . . . . . . . . . . . . . . . . . . . . 34
I.2 Box Plots of Main Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
I.3 Study of Discontinuous Poisson’s Equation . . . . . . . . . . . . . . . . . . . . . . . . 34
J Connection with Preconditioned Output Space Optimization 35
2

K Proofs 38
K.1 Helpful Lemmas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
K.2 Proof of Proposition 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
K.3 Proof of Proposition 2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
K.4 Proof of Corollary 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
K.5 Proof of Proposition 3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
K.6 Proof of Theorem 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50
K.7 Proof of Proposition 4 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50
K.8 Proof of Proposition 5 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52
K.9 Proof of Proposition 6 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54
K.10 Proof of Proposition 7 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
K.11 Statement and Proof of Proposition 8 . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
1 Introduction
Inverse problems governed by partial differential equations (PDEs) seek to estimate an unknown
physical coefficient fielda from sparse and sometimes noisy observationsuobs. These problems
are ubiquitous in observational science, where an incomplete observation must be described by a
physical model, and arise in many applications including geophysics [VO09; Bui+13], astrophysics
[Pen+24; CM22], biomedical imaging [Arr99; PLA19], and materials science [BC05; Avr+08].
Recovering the physical coefficient fielda isill-posed, since the observationsuobs often correspond
to several possible coefficient fieldsa. Thus, one aims to sample from the posterior𝜋(a|uobs)
[Stu10], e.g., classical methods use Markov Chain Monte Carlo (MCMC), which can exhibit slow
convergence for multimodal posteriors [GK07] or in high dimensions [RGG97]. Additionally,
practical use of classical methods often requires a fast surrogate for the forward model; these
surrogates are frequently highly application-specific, limiting their generalizability [TV22].
Recently, generative diffusion models [HJA20] have emerged as a powerful framework for
representing expressive, multimodal priors and enabling posterior sampling in high-dimensional
inverseproblems[Chu+23;Li+26;Zha+25]. Since aand uobsarediscretizedfunctions,arecentline
of work lifts diffusion inverse solvers to infinite-dimensional function spaces [Lim+25]. Existing
diffusion PDE inverse solvers, including the current state-of-the-art Decoupled Diffusion Inverse
Solver(DDIS)[Lin+26],firstdenoiseadiffusionstate a𝑡 toobtainanestimateofthecleancoefficient
fieldˆa0andthenseparatelymodifythisestimatetoenforcemeasurementconsistencysothat a0≈ˆa0
and uobs≈𝒜(a 0), where𝒜 is the forward operator. We refer to this class of methods asoutput
space optimizationmethods, since this amounts to optimizing in the denoiser’s output space while
holding the denoiser input fixed (Figure 2a).
However, output space optimization can be ineffective for sparsely observed PDE inverse prob-
lems. Measurementconsistencyupdatesmayleavetheunobservedcomponentofthereconstruction
a0 unchanged from the denoiser prediction, allowing errors in directions invisible to the forward
operator to persist. This limitation is particularly pronounced for discontinuousa, whose prior can
exhibit distinct modes corresponding to different discontinuity locations. When these modes differ
substantially in unobserved directions, measurement-consistency updates alone may fail to correct
an erroneous mode selected by the denoiser. This motivates the following research question:
Can we obtain a diffusion-based PDE inverse solver that modifies both the observed and unobserved
components of the denoiser prediction?
3

(a) Output Space Optimization Methods (e.g., DDIS)
×100 sampling steps (noise levels)
at Dθ a0 ≈ ˆa0
/upnablaa0 The output of Dθ is used only for initialization
Optimization
for Measurement
Consistency (20 steps)
uobs
DDIS Output 18.6% error
(b) The Proposed FunBCS: Input Space Optimization
×10 sampling steps (noise levels)
at v Dθ
/upnablav via Dθ a0 = Dθ (v∗)
Optimization
for Measurement
Consistency by F(t)
uobs
FunBCS Output 8.5% error
Figure 2: Overview of the differences between output space optimization methods (e.g., DDIS)
(a) and our input space optimization method (b). DDIS enforces measurement consistency on a
reconstruction near the denoiser’s (𝐷𝜃) output, requiring20optimization steps at each of its100
noiselevels. Incontrast,ourinputspaceoptimizationjointlyincorporatesmeasurementconsistency
and denoising by iteratively computing the denoiser output, requiring10noise levels for which
the number of input-space optimization steps,𝐹(𝑡), is dynamically allocated using the scheduler
presented in Sec. 4.2.
Contributions. We address the question affirmatively, showing thatinput space optimization, or
selecting theinputto the denoiser such that measurement consistency is satisfied (Fig. 2b), can
effectively update unobserved components. For finite-dimensional diffusion, input-space optimiza-
tion isbackward-consistentsampling [Alk+25], where the reconstruction is constrained to be in the
denoiser’s range. Our contributions can be summarized as follows:
• Theoretical analysis of output space optimization. We prove that, on a discontinuous Poisson
PDE inverse problem, output space optimization methods, such as DDIS, can fail to change the
unobserved components of the denoiser prediction and hence fail to recover the correct prior
mode.
• Input space optimization analysis, scheduling function, and algorithm. We theoretically
demonstratethatinputspaceoptimizationcanchangetheunobservedcomponent,thusobtaining
lessunobservederrorthanDDISandrecoveringthecorrectpriormode. Furthermore,weanalyze
where to allocate most of the input optimization steps across the sampling process, and use this
todesigna schedulingfunctionforvarious noiselevels. Combiningthese, we introduceFunction
SpaceBackward-ConsistentSampling(FunBCS),ourdiffusioninputspaceoptimizationmethod.
• Comprehensive evaluation. We extensively evaluate our method across four smooth and discon-
tinuous PDE inverse problems. Compared to the current state-of-the-art, our method reduces the
reconstruction error by27–64%(Fig. 1) while running1.4–2.1×faster. For example, on the same
hardware, FunBCS at8seconds per sample achieves11.8%relative ℓ2 error on Poisson, whereas
DDIS, at best, obtains13.7%error while running for72seconds (Fig. 3).
4

2 Background
PDE inverse problems. A partial differential equation (PDE) can be written as:
(
𝒥𝑎(·)𝑢(·)=𝑓(·)onΩ,
𝑢(·)=𝑔(·)on𝜕Ω, (1)
for functions𝑢(·)∈ℋ and𝑎(·)∈ℱ , whereℋ,ℱ are separable Hilbert spaces,Ω⊂R 𝑑 is a domain,
𝜕Ω is the domain boundary, and𝒥𝑎(·) is a (potentially nonlinear) differential operator that depends
on𝑎(·). ThegoalofaPDEinverseproblemistoreconstructphysicalcoefficientfield 𝑎(·) fromsparse
observations of PDE solution𝑢(·), assuming known𝑓(·)and𝑔(·). Specifically, we have:
𝑢obs(·)=𝒜(𝑎(·))+𝜂(·),(2)
where𝒜 is ameasurement operatorand 𝜂(·) is a noise term. Letting𝒢 :ℱ →ℋ be the solution
operator which maps coefficient fields to PDE solution fields, and𝒪 :ℋ→ℋ be an observation
operator (e.g., a mask), we can write𝒜=𝒪◦𝒢 . Critically,𝑢obs(·) often corresponds to several
possible 𝑎(·), and small variations in𝑢obs(·) result in drastically different𝑎(·); that is,𝒜 is not
injective and the inverse problem corresponding to Eq. (2) is severely ill-posed. To address this,
research on PDE inverse problems often takes the Bayesian perspective [Stu10], where one assumes
a prior𝜋(𝑎(·)) onℱ and aims to sample from the posterior𝜋(𝑎(·)|𝑢 obs(·)) via Bayes’ theorem, i.e.,
𝜋(𝑎(·)|𝑢 obs(·))∝𝜋(𝑢 obs(·)|𝑎(·))𝜋(𝑎(·)).
Throughout, weconsiderthediscretizedversionoftheprobleminEq.(2); inparticular, weselect
𝑛 collocation pointsx𝑖∈Ω for𝑖= 1,...,𝑛 , and evaluate only at those finitely many points1. For
example, we discretize𝑎(·) as a=(𝑎(x 1),...,𝑎(x 𝑛)); we respectively discretize𝑢(·),𝑢 obs(·),𝜂(·),𝒢,
and𝒪 as u∈R 𝑛, uobs,η∈R 𝑚,𝒢ℎ : R𝑛→R 𝑛, and𝒪ℎ : R𝑛→R 𝑚 where𝑚≪𝑛 . Importantly,
note that𝒢ℎ and𝒪ℎ can remain nonlinear in this setting, and thus do not necessarily admit matrix
representations. Wethuslet𝒜ℎ =𝒪 ℎ𝒢ℎ. AdetailedoverviewofournotationisprovidedinApp.A.
Functionspacediffusion. Oneimportantwayofobtainingaprior 𝜋(a)forthePDEinverseproblem
in Eq. (2) is to set𝜋(a0) :=𝜋(a) and samplea0∼𝜋(a 0) by running a learned reverse diffusion
process initialized with a sample from a simple distributiona𝑇∼𝜋(a 𝑇). Since𝑎(·) is a function,
this involves training diffusion on (discretized) functions [Lim+25]. After discretization, this
is equivalent to the standard diffusion process [HJA20] with two slight alterations, specifically
that the noise has kernel matrixK as its covariance instead ofI and thatK multiplies the score
in Tweedie’s formula. More specifically, we have the variance exploding (VE) diffusion forward
process [Son+21] at0<𝑡 0 <···<𝑡 𝑁 =𝑇, where𝑁is the number of sampling steps:
a𝑡𝑘+1 =a 𝑡𝑘+
q
𝜎2 𝑡𝑘+1 −𝜎 2 𝑡𝑘 ε𝑘, 𝑘=0,...,𝑁−1,(3)
where ε𝑘 ∼𝒩(0,K) are independent across𝑘. We perform reverse diffusion with respect to
Tweedie’s formula given by:
𝐷∗(a𝑡,𝑡):=E[a 0|a𝑡]=a 𝑡+𝜎 2 𝑡 K∇a𝑡 log𝑝 𝑡(a𝑡).(4)
For a learned scoresθ≈∇ a𝑡 log𝑝 𝑡(a𝑡) [Son+21], we denote the denoiser by𝐷θ≈E[a 0|a𝑡]. We
provide a more detailed formal characterization of function space diffusion in App. B.
1Without loss of generality, we note that not all traditional numerical methods use collocation points or pointwise
values. For example, finite volume and finite element methods may useaveragesand spectral methods may use Fourier
coefficients [Qua09].
5

Diffusion PDE inverse solvers. Diffusion models [Soh+15] are successful at modeling high-
dimensional priors [Rom+22], including in function spaces [Lim+25]. Thus, several diffusion
solvers have been developed for PDE inverse problems, with standard [Hua+24] or function space
[Yao+25; Lin+26] diffusion priors. At a sampling step𝑡𝑘, these solvers perform two key operations:
(D) using the diffusion denoiser to estimate the coefficient field and (M) enforcing measurement
consistency. We use the termoutput space optimizationto describe methods where (D) and (M)
aredisjoint, since this amounts to optimizing in the output space of the denoiser while leaving
the denoiser input fixed. From this perspective, DiffusionPDE [Hua+24], FunDPS [Yao+25], and
Decoupled Diffusion Inverse Solver (DDIS) [Lin+26] are all output space optimization procedures.
We discuss these solvers in further detail in App. E. We provide an extensive related work section
in App. C covering classical numerical solvers, diffusion inverse solvers and theory, approaches to
updating unobserved components, and guidance scheduling.
3 Analysis of Output Space Optimization Sampling
We instantiate DDIS as an example output space optimization method for which we provide a
discontinuous PDE inverse problem, demonstrating that unobserved differences in prior modes
arisenaturally. Consequently,DDISdoesnotalterthedenoiser’sunobservedcomponent,andhence
fails to recover the correct prior mode. All proofs are deferred to App. K.
To sample from𝜋(a|uobs), diffusion inverse solvers, as discussed earlier, do the following at
timestep𝑡 𝑘 with noisy instancea𝑡𝑘:
•(D) compute the estimated output sampleˆa(𝑡𝑘) 0 via, e.g., Eq. (4) froma𝑡𝑘 and
• (M) enforcemeasurement consistencyon the reconstructiona(𝑡𝑘) 0 ≈ˆa(𝑡𝑘) 0 , i.e., incorporate likelihood
information𝜋(u obs|a)so thatu obs≈𝒜 ℎ(a(𝑡𝑘) 0 ).
Thedefiningcharacteristicofoutputspaceinversesolversisthattheoperations(D)and(M)are
performedseparatelyat time 𝑡𝑘. Notably, output space inverse solvers may perform other operations
before, between, or after(D)and(M). Next, we formalize the DDIS sampler. Fix consecutive
diffusion times𝑡𝑘 >𝑡 𝑘−1. DDIS assumes Gaussian likelihood at timestep0, with𝛾 >0, yielding
𝑝(uobs|a 0)∝exp

−∥𝒜ℎa0−u obs∥2
2𝛾2

.
At time𝑡𝑘, DDIS approximates the denoising law𝜋(a0|a 𝑡𝑘) with𝜋𝐷(a0|a(𝐷) 𝑡𝑘 ) which has density
𝑞𝐷(a0|a(𝐷) 𝑡𝑘 )=𝒩(a 0;ˆa(𝑡𝑘) 0 ,𝑟 2 𝑡𝑘 I) withˆa(𝑡𝑘,𝐷) 0 :=𝐷 θ(a(𝐷) 𝑡𝑘 ,𝑡 𝑘), where superscript(𝐷) denotes DDIS. Setting𝑟 𝑡𝑘 =𝜎 𝑡𝑘 gives:
𝑞𝐷,𝑡𝑘(a0|a(𝐷) 𝑡𝑘 ,u obs)∝exp
(
−∥𝒜ℎa0−u obs∥2
2𝛾2 −
∥a0−ˆa(𝑡𝑘,𝐷) 0 ∥2
2𝜎2 𝑡𝑘
)
.(5)
The next iteration of DDIS is given by:
a(𝐷) 𝑡𝑘−1 =˜a(𝑡𝑘) 0 +𝜎 𝑡𝑘−1 ε(𝐷) 𝑘 ,˜a (𝑡𝑘) 0 ∼𝑞 𝐷,𝑡𝑘(·|a(𝐷) 𝑡𝑘 ,u obs),ε (𝐷) 𝑘 ∼𝒩(0,K),(6)
where 𝜀(𝐷) 𝑘 are drawn independently. In practice, DDIS uses Langevin dynamics [RT96] to sample
from Eq. (5) for use in Eq. (6) at every diffusion timestep𝑡𝑘. In particular, DDIS finds˜a(𝑡𝑘) 0 close to
6

ˆa(𝑡𝑘,𝐷) 0 , enforces measurement consistency ona0, and then renoises to𝑡𝑘−1. This is run until time𝑡0
to obtain a final reconstructed physical coefficient field.
Next, towards explaining why output space optimization can fail, we provide an example PDE
inverse problem on which we will show that DDIS fails:
𝑢′′(·)=𝑎(·),on(0,1), 𝑢(1)=𝑢(0)=0.(7)
We now assume that𝑎(·) has a single discontinuity at𝑧∈( 0, 1), so that admissible coefficient
fields are{𝑎(·)∈𝐿 2(0, 1) : 𝑎(𝑥)=𝑎 (1)1(0,𝑧)+𝑎(2)1[𝑧,1], 𝑧∈( 0, 1)}, where𝐿2 are square-integrable
functions. We assume that the coefficients𝑎(1),𝑎(2) are known beforehand so that the uncertainty is
only over the discontinuity location; upon reconstruction one can place𝑎(1),𝑎(2) on either side of
𝑧. Furthermore, we consider two physical coefficient fields𝑎−(·) and𝑎+(·) with respective distinct
discontinuity locations𝑧−≠𝑧+. With discretization at𝑛 collocation pointsx𝑖∈( 0, 1), consider a
prior which weights these two discontinuity locations equally, i.e.,
𝜋(a0)= 1 2𝛿a−+ 1 2𝛿a+.
In this setting, we consider a noiseless Bayesian inverse problem per Eq. (2) given byuobs =
OG(a+), where G is a linear solution operator andO is a selection matrix. Thus, givenuobs, a
successful diffusion inverse solver should recovera+ at the end of the sampling process. Note that
while the prior ona+ and a− is not exactly learnable by a diffusion model, it can be approximated
by a mixture of Gaussians with small variance. The noiseless setting ofη=0 matches both our
experiments in Sec. 5 and the DDIS experiments in Lin, Yao, et al. [Lin+26].
Note that this setting is a linear analogue of the nonlinear Darcy inverse problem in Fig. 1 where
weassumethat 𝑎(1) and𝑎(2) areknown,andfindthecorrectdiscontinuitylocationforlinearPoisson.
We simplify this setting by assuming only two possible discontinuity locations; we find that this is
sufficient to observe the limitations of output space optimization methods, and the benefits of input
space optimization (which we will discuss in the upcoming sections).
Remark 1.Let A :=OG be the forward operator andPkerA be the orthogonal projection matrix
onto its nullspace. We prove in Prop. 8, described in App. K.11, that the setting described above
yields that the measurements differ (Aa+ ≠Aa −) and that the nullspace components differ
(PkerAa+≠P kerAa−) with high probability. We thus take these as assumptions throughout.
In the setting above, we find that output space optimization can do no better than the denoiser
in unobserved error. This issue is critical if the denoiser chooses the incorrect prior mode. Formally:
Proposition 1(DDIS preserves denoiser nullspace component).Fix𝑡𝑘 >𝑡 𝑘−1. SupposeAa+≠Aa−
and PkerAa+ ≠P kerAa− and let¯a𝐷,𝑡𝑘−1 :=E[a (𝐷) 𝑡𝑘−1|a(𝐷) 𝑡𝑘 ,u obs], wherea(𝐷) 𝑡𝑘−1,a(𝐷) 𝑡𝑘 are given by Eq.(6)
under the exact denoiser𝐷∗(·,𝑡 𝑘)in Eq.(4). We then have that:
∥PkerA(¯a𝐷,𝑡𝑘−1−a+)∥2=∥P kerA(𝐷∗(a(𝐷) 𝑡𝑘 ,𝑡 𝑘)−a +)∥2 .(8)
Remark 2.Per Eq. (8), DDIS at step𝑡𝑘−1 does not grow any closer in nullspace toa+ than the
denoiser does at step𝑡𝑘. This is precisely because the measurement consistency error in Eq. (5)
does not update the unobserved components, while the second term aligns the reconstruction
with the denoiser. While the reconstruction˜a(𝑡𝑘) 0 influences the denoiser input at the next diffusion
timestep after renoising, this merely gives the denoiser another chance to correct itself, which is not
guaranteed. Consequently, if the denoiser remains mistaken at later timesteps, particularly near the
endofthereverseprocess, thecorrespondingnullspaceerrormaypersistinthefinalreconstruction.
We provide experimental validation for this on Darcy flow in Sec. 5.
7

WenotethatinpracticeDDISusestheprobabilityflowODEinsteadofthedenoiser;perLemma9
in App. K.1, the above Prop. 1 still holds in this case. Prop. 1 immediately yields that DDIS fails to
recovera+ more generally:
Corollary 1(DDIS does not recovera+).Fix 𝑡𝑘 >𝑡 𝑘−1. With the same assumptions as Prop. 1, let
𝑘𝑡𝑘(v)=P(a 0=a+|a𝑡𝑘 =v) be the regular conditional probability of recovering the correcta+. Then, this
probability is well-defined and we have that:
∥¯a𝐷,𝑡𝑘−1−a+∥2≥(1−𝑘 𝑡𝑘(a(𝐷) 𝑡𝑘 ))||PkerAd||2 >0.(9)
Remark 3.Note that Cor. 1 holds for𝑡𝑘 arbitrary, including at the end of the sampling process, and
that Eq. (9) continues to hold as𝜎𝑡0→ 0. Furthermore, as discussed in Remark 2, DDIS’ inability
to recover the truea+ is exacerbated when the wrong mode is preferred (i.e., when𝑘𝑡𝑘(a(𝐷) 𝑡𝑘 )< 1 2), particularly near the end of the reverse process; we confirm this empirically on Darcy flow in Sec. 5.
4 Input Space Optimization Sampling in Function Space
In this section, we propose merging steps (D) and (M) discussed above, iteratively denoising
and finding theinputto the denoiser such that measurement consistency holds. We demonstrate
theoretically that this scheme does not fail in the same Poisson setting of the previous section.
Subsequently, we provide insights and a procedure on how to select the number of optimization
steps for the input at each sampling iteration, and present the FunBCS algorithm. To motivate input
space optimization, we note the following fact about the denoiser in the setting of Sec. 3:
Proposition 2(Denoiser nullspace component).Suppose Aa+≠Aa− and PkerAa+≠P kerAa− hold.
Let d=a +−a− bethedifferencebetweenthetwopriormodes, and v beafixeddenoiserinput. Wethenhave:
𝐷∗(v,𝑡 𝑘)=a −+𝑘 𝑡𝑘(v)d,P kerA𝐷∗(v,𝑡 𝑘)=P kerAa−+𝑘 𝑡𝑘(v)PkerAd. (10)
Per Prop. 2, the unobserved component of𝐷∗(·,𝑡 𝑘)can be changed by updating𝑘𝑡(v); since𝑘𝑡(·)
is a function of the denoiser input, it suffices to optimize in the input space of the denoiser. Thus, to
enable input space optimization, at every𝑡𝑘, we propose solving:
arg min
v
∥𝒪ℎ◦𝒢 ℎ,ϕ◦𝐷 θ(v,𝑡 𝑘)−u obs∥2 2 ,𝒜 ℎ =𝒪 ℎ◦𝒢 ℎ,ϕ ,(11)
for a neural surrogate𝒢ℎ,ϕ, since𝒢ℎ may be difficult to differentiate. Using superscript (𝐵) for
FunBCS, consider the gradient flow onv with respect to the objective in Eq. (11) with𝛾 >0and
optimization time𝑠≥0:
𝑑v(𝑠)
𝑑𝑠 =− 1 2𝛾2∇v∥𝒪ℎ◦𝒢 ℎ,ϕ◦𝐷 θ(v,𝑡 𝑘)−u obs∥2

 v=v(𝑠) ,v(0)=𝑎 (𝐵) 𝑡𝑘 .(12)
Remark 4.After discretizing Eq. (12), this amounts to iteratively denoising and optimizing the
input, thus merging steps (D) and (M). Under the exact denoiser, the solution of Eq. (12) exists
and is unique per Lemma 6 in App. K.1, and the probability𝑘𝑡𝑘(v(𝑠)) is monotonically increasing in
𝑠 per Lemma 7 in App. K.1. Additionally, input space optimization is equivalent topreconditioned
output space optimization, with the preconditioner (which we further discuss in App. J)
∇v𝐷∗(v,𝑡 𝑘)∇v𝐷∗(v,𝑡 𝑘)𝑇|v=v(𝑠).
Solving Eq. (11) with Eq. (12) and renoising yields the update rule at a diffusion time𝑡𝑘 and
optimization time𝑠, forε(𝐵) 𝑘 drawn independently:
a(𝐵) 𝑡𝑘−1 =𝐷 θ(v(𝑠),𝑡 𝑘)+𝜎 𝑡𝑘−1 ε(𝐵) 𝑘 ,ε (𝐵) 𝑘 ∼𝒩(0,K).(13)
8

Algorithm 1Function Space Backward-Consistent Sampling (FunBCS)
Require: observations uobs; observation operator𝒪; denoiser𝐷θ; neural operator surrogate𝒢ℎ,𝜙;
diffusion schedule{𝜎𝑡𝑘}; optimization step function𝐹(𝑡𝑘); Adam step size𝛼.
1:a (𝐵) 𝑡𝑁 ←𝜎 𝑡𝑁 𝜀𝑁,𝜀 𝑁∼𝒩(0,K)⊲initial latent drawn from the training GRF
2:for𝑘=𝑁,...,1do
3:v 0←a(𝐵) 𝑡𝑘 ⊲warm start at the current noisy state
4:for𝑠=0,...,𝐹(𝑡 𝑘)−1do
5:𝒥 ← 1 2𝛾2∥𝒪ℎ◦𝒢 ℎ,𝜙(𝐷θ(v𝑠,𝜎𝑡𝑘))−u obs∥2 2 ⊲compute denoiser output (D)
6:v 𝑠+1←AdamStep 𝛼(v𝑠,∇ vs𝒥)⊲enforce measurement consistency (M)
7:end for
8:a (𝐵) 𝑡𝑘−1←𝐷 θ(v𝐹(𝑡𝑘),𝜎𝑡𝑘)+𝜎 𝑡𝑘−1 ε𝐾,ε 𝐾∼𝒩(0,K)⊲renoise
9:end for
10:returna (𝐵) 𝑡0
4.1 Analysis of Input Space Optimization
To analyze input space optimization, we revisit the setting of Sec. 3, where we assume access to
the exact operatorG. We begin by analyzing how the recurrence in Eq. (13) changes the nullspace
error:
Proposition 3(Inputspaceoptimizationreducesnullspaceerrorbetter).Underthesameassumptions
as Prop. 1, we have thatE[a(𝐵) 𝑡𝑘−1|a(𝐵) 𝑡𝑘 ,u obs]=𝐷 ∗(v(𝑠),𝑡 𝑘)and for any𝑠>0:
∥PkerA(𝐷∗(v(𝑠),𝑡 𝑘)−a +)∥2≤∥P kerA(𝐷∗(a(𝐵) 𝑡𝑘 ,𝑡 𝑘)−a +)∥2 .(14)
Additionally, there exists an𝑠∗ >0such that𝑠≥𝑠 ∗ yields:
∥PkerA(𝐷∗(v(𝑠),𝑡 𝑘)−a +)∥2≤∥P kerA(¯a𝐷,𝑡𝑘−1−a+)∥2 .(15)
Remark 5.As expected per our discussion in Prop. 2, the input space optimization recurrence in
Eq. (13) contracts nullspace error better than both the denoiser evaluated at the previous iterate
and DDIS, since it can update𝑘𝑡(v). We demonstrate Prop. 3 empirically in App. I.3.
Furthermore, input space optimizationcanrecover the correcta+ in this PDE inverse setting:
Theorem 1(Input space optimization can recovera+).Consider diffusion times𝑡𝑘 >𝑡 𝑘−1. Under the
same assumptions as Prop. 1, we have that:
𝜋𝑠(a(𝐵) 𝑡𝑘−1|a(𝐵) 𝑡𝑘 ,u obs)=𝒩(𝐷 ∗(v(𝑠),𝑡 𝑘),𝜎 2 𝑡𝑘−1K)⇒𝒩(a +,𝜎 2 𝑡𝑘−1 K),as𝑠→∞.(16)
At the final step𝑡𝑘−1 =𝑡 0 the limiting law converges in distribution to𝛿a+ as𝜎 𝑡0→0.
Thus, for a multimodal prior and with differences between prior modes partially lying in
measurement nullspace, which arises naturally in the discontinuous PDE inverse problem setting
perProp.8inApp.K.11,inputspaceoptimizationcansignificantlyoutperformoutputoptimization.
We note that this happens regardless of whether the denoiser begins by preferring the wrong mode;
we provide experimental validation for this on Darcy flow in Sec. 5. The resulting algorithm not
only provides a mechanism to change the unobserved components of the denoiser prediction (as
we theoretically support), but also reduces the need for a large number of sampling steps as we
show in our experimental results in Sec. 5.
9

4.2 Allocating Input Space Optimization Steps Across Noise Levels
In this subsection, we address the question of how many measurement consistency steps we should
take per one noise level (or sampling step). Let𝐹(𝑡𝑘) denote the number of gradient flow steps
taken at noise level𝑡𝑘, so that the sampler takes𝑀= ˝𝑁 𝑘=1𝐹(𝑡𝑘) steps in total. Every such step
differentiates through the denoiser, so this allocation sets the cost of the sampler.
To make our sampler more efficient, we ask how a fixed budget of steps should be distributed
across noise levels, and we answer in the setting of Sec. 3. We begin with the case in which the
sampler leans towards the wrong prior mode and a noise level receives no optimization steps at all.
In particular, for𝑡𝑘+1 >𝑡 𝑘, we let
𝑘𝑡𝑘+1(a(𝐵) 𝑡𝑘+1 )≤ 1 2−𝛿,for𝛿∈(0,1/2),anda (𝐵) 𝑡𝑘 =𝐷∗(a(𝐵) 𝑡𝑘+1 ,𝑡 𝑘+1)+𝜎 𝑡𝑘 ε(𝐵) 𝑘 .
We can then characterize the number of gradient flow steps necessary to escape to the correct mode
in the subsequent diffusion step𝑡𝑘 as follows:
Proposition 4(Time explosion with no optimization steps).Consider the setting of Sec. 4.2 with
Aa+ ≠Aa − and PkerAa+ ≠P kerAa−. Let v𝑡𝑘(𝑠) solve Eq.(12)and define the hitting time𝜏𝑡𝑘 :=
inf

𝑠≥0 :𝑘 𝑡𝑘(v𝑡𝑘(𝑠))≥ 1 2 	 . Then, for constants𝑄,𝐶>0, we have that:
P

𝜏𝑡𝑘≥
𝜎4 𝑡𝑘
𝐶
"
exp

𝑄𝛿
2𝜎2 𝑡𝑘
!
−1
#

 a(𝐵) 𝑡𝑘+1 ! ≥1−exp  −𝑄𝛿 2 8𝜎2 𝑡𝑘 ! .(17)
Remark 6.For fixed 𝛿 > 0, the lower bound on the hitting time tends to∞ exponentially, with
probability tending to 1 as𝜎𝑡𝑘→ 0. That is, a lean towards the wrong mode that is not corrected
withinputspaceoptimizationstepscanresultinanexponentiallylargercosttocorrectinlatersteps.
We conclude that we should retain a positive number of optimization steps to avoid this critical
scenario.
We next consider at which noise level(s) to allocate most of the gradient flow steps in our
method. To address this, we allow the noise standard deviation𝜎 > 0to vary continuously and
consequentlyuse 𝜎, inplaceof 𝑡𝑘, toindex. Wethenfixasingledenoiserinputleaningtothewrong
mode, and see where the minimal time to escape to the correct mode is. Formally, we fix an input
v∗∈R 𝑛 satisfying𝑘 𝜎(v∗)< 1 2, and compute the fastest hitting time across𝜎:
Proposition 5(Selection window).Under the assumptions of Prop. 4, let𝑤𝜎(𝑠) denote𝑘𝜎(v(𝑠)) for v(𝑠)
a solution to Eq.(12)at noise level𝜎 with initializationv∗, and define𝜏(𝜎) :=inf

𝑠≥0 :𝑤 𝜎(𝑠)≥ 1 2 	 .
Then, there exist𝜎low,𝜎 high∈(0,∞)and𝜎 ★∈[𝜎 low,𝜎 high]such that𝜏(𝜎 ★)=min 𝜎>0 𝜏(𝜎).
Remark 7.At very high noise levels, the denoiser is undecided between the two modes, but its
output responds only weakly to its input, so the gradient flow moves prohibitively slowly. At very
low noise levels, the denoiser responds strongly to input changes, but it has already committed to
the wrong mode. The correct prior mode is therefore selected most cheaply at intermediate noise
levels, inside an interval[𝜎low,𝜎 high] that we call theselection window. By our experiments in Sec. 5
with our scheduler described in App. G, we find this generalizes across PDEs.
Together, the two propositions constrain how a budget of optimization steps should be dis-
tributed. By Prop. 4, every noise level must retain a positive number of steps, so that a lean towards
the wrong mode is never carried uncorrected into the lower noise levels. By Prop. 5, the remaining
stepsarebestspentinsidetheselectionwindow. Wethereforetreatthetotalnumberofoptimization
10

Table1: Recoveryofphysicalcoefficientfields awithrelative ℓ2 errorandspectralenergyerror 𝐸𝑠 on
100sampledinstancesfrom3%observations. s/sampleissecondspersampleononeNVIDIAA100.
FunBCS-AC and FunBCS-EF denote FunBCS in accuracy mode and in efficiency mode, respectively
(App. G). FunBCS (uniform) is FunBCS without the scheduling function, which corresponds to the
case of assigning𝐹(𝑡𝑘)= 80at every noise level (𝑀= 800). Errors are mean± standard deviation
over these instances. Lower is better.
Poisson Helmholtz Navier–Stokes Darcy
Method rel.ℓ 2 𝐸𝑠 rel.ℓ 2 𝐸𝑠 rel.ℓ 2 𝐸𝑠 err. rate𝐸 𝑠 s/sample
DiffusionPDE 21.20±6.860.150±0.11918.93±5.040.133±0.0849.49±1.650.230 ±0.0257.49±4.600.311±0.169274.5
FunDPS 22.05±7.110.169±0.11616.25±4.090.156±0.0778.18±1.530.381±0.0325.04±2.710.152±0.06014.5
DDIS 15.76±5.080.071±0.05315.47±4.340.070±0.0518.36±1.550.158±0.0177.48±3.890.165±0.08918.0
FunBCS (uniform) 10.51±3.380.050 ±0.0389.90 ±2.710.056±0.0346.23±1.130.300±0.0692.82±1.560.113±0.05316.5
FunBCS-EF 10.22 ±3.330.056±0.04910.04±2.950.085±0.0536.14 ±1.110.280±0.0592.69 ±1.500.086 ±0.04110.4
FunBCS-AC9.60±3.080.047±0.0399.06±2.510.069 ±0.0375.89±1.040.288±0.0512.32±1.270.080±0.03316.5
steps𝑀 as a budget, which a scheduling function allocates across noise levels by choosing𝐹(𝑡𝑘),
whichkeepsafloorofstepsateverylevelandconcentratestherestinacomputedselectionwindow,
with further details in App. G. At a fixed budget, this moves steps to where they matter; at a smaller
budget, it removes the steps that matter least.
Algorithm. Our sampler is given in Algorithm 1. Equation (13) yields backward-consistent
sampling, but not in the finite-dimensional regime as in Alkhouri, Liang, et al. [Alk+25]. This
means that the reconstructiona(𝑡𝑘) 0 before renoising isexactlythe output of the denoiser, rather than
approximately.
5 Experiments
Setup.We evaluate on four PDE inverse problems, each at a resolution of1282 points:Poisson,
Helmholtz,Navier–Stokes(NS) andDarcy flow, each observed at500randomly placed points of the
solution field (3%of the grid) without noise following [Lin+26]. We report the relativeℓ2 error
of the recovered coefficient field in percent and the spectral energy error𝐸𝑠 averaged across 100
inferencesamples. FunBCSuses 𝑁= 10noiselevels(samplingsteps)withtwoschedulingschemes,
Accuracy mode (AC) and Efficiency mode (EF). See App. G for details. Other experimental details
are given in App. F.
Main reconstruction results.Per Table 1, our sampler attains the lowest reconstruction error
on every task when compared to baselines. Relative to DDIS, the error falls by39%on Poisson,
41%on Helmholtz,30%on Navier–Stokes, and69%on Darcy. Box plots of the Table 1 errors are
visualized in Fig. 15 in App. I.2. In line with our theory, the largest gain is on Darcy flow, whose
piecewise-constant coefficient makes the prior sharply multimodal: the error rate drops from7.48%
to2.32%, a3.2× reduction, and the visualization in Fig. 1 shows that DDIS misplaces interfaces
whereas our reconstructions recover the correct discontinuity locations and geometries. Qualitative
visualizations of the results on all four PDEs are in Figs. 16 and 17 in App. I.1. The spectral energy
error of our method is better on Poisson, Helmholtz and Darcy, whereas DDIS retains a lower𝐸𝑠 on
Navier–Stokes despite its higherℓ2 error. This is because𝐸𝑠 only checks whether a reconstruction
has the right amount of detail at each spatial scale, not whether that detail is in the right place. As
we show in App. H, DDIS produces more fine-scale detail than FunBCS, which brings this amount
closer to that of the ground truth, but neither method places the fine-scale detail where it appears
in the true field.
11

Impact of the proposed scheduling function.At a budget of𝑀= 800steps, concentrating them in
the selection window (i.e., FunBCS-AC) lowers the error when compared to the uniform allocation
(i.e., FunBCS without the scheduling function in Table 1). For example, on Poisson, the error is
reduced by9%. Trimming the steps outside the window, i.e., FunBCS-EF, removes24–49%of them,
yet FunBCS-EF still outperforms every baseline on every task, running1.4–2.1×faster than DDIS
with27–64%lower reconstruction error (App. G.1). We show in App. G.3 that our scheduling
function also improves DDIS on its efficiency, though not as much in magnitude as the gain we
observed for FunBCS.
Scalingwithcompute.Figure3presentshowthePoisson
errorofeverymethodscales(Fig.6inApp.Fpresentsthe
resultsontheotherPDEs). Ateverytimebudget,FunBCS
is more accurate than baselines. For example, FunBCS at
8seconds per sample achieves11.8%relative ℓ2 error on
Poisson, whereas DDIS, at best, obtains13.7%error while
running for72seconds.
FunBCS ability of escaping a wrong mode. In Sec. 3 and
Sec. 4, we highlighted that DDIS on a discontinuous Pois-
soninverseproblemcanfailwhenthedenoiserselectsthe
wrong mode, while FunBCS fixes this problem. We test
thismechanismonDarcyflow,whereseveralpossibledis-
continuity locations result in a learned multimodal prior
and, as discussed in Sec. 3 and Prop. 8 in App. K.11, a
component of the denoiser decision lies in measurement
nullspace with high probability. Results across50test
instances are given in Fig. 4 where we move every discon-
tinuity location of the true fielda+ by five pixels to obtain
a wrong fielda−, resulting in11%pixel error. We say an
instanceescapeswhenitsfinalreconstructionassignsmost
of the pixels wherea+ and a− differ to the true fielda+,
withalowererrorratethan a−. Wefindthatwhenstarted
at 𝜎= 0.5, FunBCS escapesa− on 94% of the instances,
whereasDDISescapesonnone;doublingtheinferencebud-
get of DDIS only increases this to 18%. We visualize this
acrossnoiselevels 𝜎inFig.4. Thisispreciselythebehavior
predictedbyCor.1forDDISandThm.1forFunBCS:ifthe
denoiser is wrong, DDIS can fail, and this is exacerbated
towardstheendofthesamplingprocess,whileincontrast
FunBCS can adjust the denoiser’s decision and solve this
problem.
5
 10
 20
 50
 100
 200
 500
time per sample (s)
8
12
16
20
24rel. ℓ2 error (%) DiﬀPDE
FunDPS
DDIS
FunBCS
Poisson
Figure 3: Poisson reconstruction error
with respect to the time per sample. All
methods are run using the same hard-
ware. FunBCS and DDIS use the same
diffusion prior.
1.94
 1.02
 0.50
 0.23
noise level at which sampling starts, σ
0
25
50
75
100instances that escape (%)
96
84
0 0
18
DDIS, 2× budget
100 100
94
88
FunBCS
DDIS
Figure 4: Share of the50Darcy test in-
stances on which each sampler escapes
thewrongfield a−,againstthenoiselevel
𝜎 at which sampling starts from renoised
a−. The hollow marker is DDIS with
twice its inference budget.
6 Conclusion
We introduce FunBCS, an input space optimization approach for solving sparse PDE inverse prob-
lems. We demonstrate that existing methods, such as the state-of-the-art DDIS, perform output
space optimization and consequently can fail to obtain the correct coefficient field, especially when
the prior is naturally multimodal (e.g., when discontinuities are present in the coefficient field).
12

We demonstrate that FunBCS does not suffer from this issue: across four PDE inverse problems, it
significantly reduces the reconstruction error of the state-of-the-art at significantly lower runtime.
We discuss limitations and future directions in App. D.
Acknowledgements
ThismaterialisbaseduponworksupportedbytheNationalScienceFoundationGraduateResearch
FellowshipProgramunderGrantNo. DGE2241144,whichsupportsM.H.A.Anyopinions,findings,
and conclusions or recommendations expressed in this material are those of the author(s) and do
notnecessarilyreflecttheviewsoftheNationalScienceFoundation. J.M.M.andI.A.weresupported
by the U.S. Department of Energy through the Laboratory Directed Research and Development at
LosAlamosNationalLaboratory(LANL)underprojects20260060DRand20250048DR,respectively.
LANLisoperatedbyTriadNationalSecurity,LLC,fortheNationalNuclearSecurityAdministration
ofU.S.DepartmentofEnergy(ContractNo. 89233218CNA000001). Q.Q.,C.J.,andY.J.acknowledge
support from NSF CAREER grant CCF-2143904; NSF grants CCF-2212066, CCF-2212326, and
IIS-2402950; ONR grant N000142512339; and Google TPU Research Awards.
References
[Alk+25] Ismail R. Alkhouri, Shijun Liang, Cheng-Han Huang, Jimmy Dai, Qing Qu, Saiprasad
Ravishankar, and Rongrong Wang. “SITCOM: Step-wise Triple-Consistent Diffusion
SamplingforInverseProblems”.In:InternationalConferenceonMachineLearning(ICML).
2025.
[And+26] Martin Andrae, Erik Wikingsson, So Takao, Tomas Landelius, and Fredrik Lindsten.
“DAISI: Data Assimilation with Inverse Sampling using Stochastic Interpolants”. In:
International Conference on Machine Learning (ICML). 2026.
[Arr99] Simon R Arridge. “Optical tomography in medical imaging”. In:Inverse Problems
(1999).
[AS21] GiovanniSAlbertiandMatteoSantacesaria.“Infinitedimensionalcompressedsensing
from anisotropic measurements and applications to inverse problems in PDE”. In:
Applied and Computational Harmonic Analysis(2021).
[Ash+26] MuhammadHAshiq,SamanyuArora,AbhinavNHarish,IshaanKharbanda,HungY
Tseng, and Grigorios G Chrysos. “Why DDIM Hallucinates More Than DDPM: A
Theoretical Analysis of Reverse Dynamics”. In:International Conference on Machine
Learning (ICML). 2026.
[Avr+08] Stéphane Avril, Marc Bonnet, Anne-Sophie Bretelle, Michel Grédiac, François Hild,
Patrick Ienny, Félix Latourte, Didier Lemosse, Stéphane Pagano, Emmanuel Pagnacco,
and Fabrice Pierron. “Overview of identification methods of mechanical parameters
based on full-field measurements”. In:Experimental Mechanics(2008).
[Ban+26] Junseo Bang, Dong Ju Mun, Hoigi Seo, Seongmin Hong, and Se Young Chun. “Triadic
Dynamics Aware Diffusion Posterior Sampling for Inverse Problems: Optimizing
Guidance and Stochasticity Schedules”. In:International Conference on Machine Learning
(ICML). 2026.
13

[Bar+14] Johnathan M Bardsley, Antti Solonen, Heikki Haario, and Marko Laine. “Randomize-
then-optimize:Amethodforsamplingfromposteriordistributionsinnonlinearinverse
problems”. In:SIAM Journal on Scientific Computing(2014).
[BC05] Marc Bonnet and Andrei Constantinescu. “Inverse problems in elasticity”. In:Inverse
Problems(2005).
[Bel12] Yurii Ya Belov.Inverse problems for partial differential equations. Walter de Gruyter, 2012.
[BF26] Benjamin A. Burns and Sara Fridovich-Keil. “When, why, and how do diffusion poste-
rior samplers fail? A finite-sample lens”. In:arXiv preprint arXiv:2605.30330(2026).
[Boy+24] Benjamin Boys, Mark Girolami, Jakiw Pidstrigach, Sebastian Reich, Alan Mosca, and
Omer Deniz Akyildiz. “Tweedie Moment Projected Diffusions for Inverse Problems”.
In:Transactions on Machine Learning Research (TMLR)(2024).
[BSK25] Jan-Hendrik Bastek, WaiChing Sun, and Dennis Kochmann. “Physics-Informed Diffu-
sion Models”. In:International Conference on Learning Representations (ICLR). 2025.
[Bui+13] Tan Bui-Thanh, Omar Ghattas, James Martin, and Georg Stadler. “A computational
framework for infinite-dimensional Bayesian inverse problems Part I: The linearized
case, with application to global seismic inversion”. In:SIAM Journal on Scientific Com-
puting(2013).
[Che+18] Ricky TQ Chen, Yulia Rubanova, Jesse Bettencourt, and David K Duvenaud. “Neural
ordinary differential equations”. In:Advances in neural information processing systems
(2018).
[Che+25] Siyi Chen, Yixuan Jia, Qing Qu, He Sun, and Jeffrey Fessler. “Flowdas: A stochastic
interpolant-based framework for data assimilation”. In:Advances in Neural Information
Processing Systems (NeurIPS)(2025).
[Chu+23] Hyungjin Chung, Jeongsol Kim, Michael T Mccann, Marc L Klasky, and Jong Chul Ye.
“Diffusion Posterior Sampling for General Noisy Inverse Problems”. In:International
Conference on Learning Representations (ICLR). 2023.
[Cit+24] Jonathan Citrin, Ian Goodfellow, Akhil Raju, Jeremy Chen, Jonas Degrave, Craig Don-
ner, Federico Felici, Philippe Hamel, Andrea Huber, Dmitry Nikulin, David Pfau,
Brendan Tracey, Martin Riedmiller, and Pushmeet Kohli. “TORAX: a fast and dif-
ferentiable tokamak transport simulator in JAX”. In:arXiv preprint arXiv:2406.06718
(2024).
[CM22] Nelson Christensen and Renate Meyer. “Parameter estimation with gravitational
waves”. In:Reviews of Modern Physics(2022).
[Cot+13] Simon L Cotter, Gareth O Roberts, Andrew M Stuart, and David White. “MCMC
methods for functions: modifying old algorithms to make them faster”. In:Statistical
Science(2013).
[CV25] Evan Scope Crafts and Umberto Villa. “Benchmarking diffusion annealing-based
Bayesian inverse problem solvers”. In:IEEE Open Journal of Signal Processing(2025).
[Del+26] MatiasGDelgadino,SebastienMotsch,AdvaitParulekar,WilliamPorteous,andSanjay
Shakkottai. “Diffusion-Based Posterior Sampling: A Feynman-Kac Analysis of Bias
and Stability”. In:arXiv preprint arXiv:2605.06538(2026).
[DHS12] Masoumeh Dashti, Stephen Harris, and Andrew Stuart. “Besov priors for Bayesian
inverse problems”. In:Inverse Problems and Imaging(2012).
14

[Efr11] Bradley Efron. “Tweedie’s formula and selection bias”. In:Journal of the American
Statistical Association(2011).
[EHN96] Heinz Werner Engl, Martin Hanke, and Andreas Neubauer.Regularization of inverse
problems. Springer Dordrecht, 1996.
[ESS15] Oliver G Ernst, Björn Sprungk, and Hans-Jörg Starkloff. “Analysis of the ensemble
and polynomial chaos Kalman filters in Bayesian inverse problems”. In:SIAM/ASA
Journal on Uncertainty Quantification(2015).
[GK07] Yongtao Guan and Stephen M Krone. “Small-world MCMC and convergence to multi-
modal distributions: From slow mixing to fast mixing”. In:The Annals of Applied
Probability(2007).
[GLR18] RongGe,HoldenLee,andAndrejRisteski.“Beyondlog-concavity:Provableguarantees
for sampling multi-modal distributions using simulated tempering langevin monte
carlo”. In:Advances in Neural Information Processing Systems (NeurIPS)(2018).
[Gor+20] AlexAGorodetsky,JohnDJakeman,GianlucaGeraci,andMichaelSEldred.“MFNets:
Multi-fidelity data-driven networks for Bayesian learning and prediction”. In:Interna-
tional Journal for Uncertainty Quantification(2020).
[Hen+26] Liav Hen, Tom Tirer, Raja Giryes, and Shady Abu-Hussein. “Jacobian-Aware Posterior
Sampling for Inverse Problems”. In:Transactions on Machine Learning Research (TMLR)
(2026).
[HJA20] Jonathan Ho, Ajay N Jain, and Pieter Abbeel. “Denoising Diffusion Probabilistic Mod-
els”. In:Advances in Neural Information Processing Systems (NeurIPS). 2020.
[HSV14] MartinHairer,AndrewMStuart,andSebastianJVollmer.“SpectralgapsforaMetropolis–
Hastings algorithm in infinite dimensions”. In:The Annals of Applied Probability(2014).
[Hua+24] Jiahe Huang, Guandao Yang, Zichen Wang, and Jeong Joon Park. “DiffusionPDE:
Generative PDE-Solving under Partial Observation”. In:Advances in Neural Information
Processing Systems (NeurIPS). 2024.
[ILS13] Marco A Iglesias, Kody JH Law, and Andrew M Stuart. “Ensemble Kalman methods
for inverse problems”. In:Inverse Problems(2013).
[ILS16] Marco A Iglesias, Yulong Lu, and Andrew M Stuart. “A Bayesian level set method for
geometric inverse problems”. In:Interfaces and free boundaries(2016).
[Jia+26a] Yixuan Jia, Siyi Chen, Yida Pan, Xiao Li, Lianghe Shi, Chanyong Jung, Haijie Yuan,
Ismail Alkhouri, Yue Cynthia Wu, Saiprasad Ravishankar, Jeffrey A Fessler, and Qing
Qu. “ForcingDAS: Unified and Robust Data Assimilation via Diffusion Forcing”. In:
arXiv preprint arXiv:2605.14285(2026).
[Jia+26b] Yuchen Jiao, Na Li, Changxiao Cai, Yuxin Chen, and Gen Li. “Provable diffusion-
based posterior sampling for linear inverse problems via DDIM”. In:arXiv preprint
arXiv:2607.19333(2026).
[Kar+21] George E Karniadakis, Ioannis G Kevrekidis, Lu Lu, Paris Perdikaris, Sifan Wang, and
Liu Yang. “Physics-informed machine learning”. In:Nature Reviews Physics(2021).
[Kas+21] KKashinath,MMustafa,AAlbert,J-LWu,CJiang,SEsmaeilzadeh,KAzizzadenesheli,
R Wang, A Chattopadhyay, A Singh, et al. “Physics-informed machine learning: case
studies for weather and climate modelling”. In:Philosophical Transactions of the Royal
Society A(2021).
15

[KLS23] Gavin Kerrigan, Justin Ley, and Padhraic Smyth. “Diffusion Generative Models in
Infinite Dimensions”. In:International Conference on Artificial Intelligence and Statistics.
2023.
[KP92] Peter E Kloeden and Eckhard Platen.Numerical solution of stochastic differential equations.
Springer Berlin, Heidelberg, 1992.
[Li+21] Zongyi Li, Nikola Kovachki, Kamyar Azizzadenesheli, Burigede Liu, Kaushik Bhat-
tacharya, Andrew Stuart, and Anima Anandkumar. “Fourier Neural Operator for
Parametric Partial Differential Equations”. In:International Conference on Learning Rep-
resentations (ICLR). 2021.
[Li+26] XiangLi,SooMinKwon,ShijunLiang,IsmailRAlkhouri,SaiprasadRavishankar,and
Qing Qu. “DCDP: Decoupled Data Consistency via Diffusion Purification for Inverse
Problems”. In:2026 IEEE International Conference on Computational Photography (ICCP).
2026.
[Lim+25] Jae Hyun Lim, Nikola B Kovachki, Ricardo Baptista, Christopher Beckham, Kamyar
Azizzadenesheli, Jean Kossaifi, Vikram Voleti, Jiaming Song, Karsten Kreis, Jan Kautz,
Christopher Pal, Arash Vahdat, and Anima Anandkumar. “Score-Based Diffusion
Models in Function Space”. In:Journal of Machine Learning Research (JMLR)(2025).
[Lin+26] Thomas YL Lin, Jiachen Yao, Lufang Chiang, Julius Berner, and Anima Anandku-
mar. “Decoupled Diffusion Sampling for Inverse Problems on Function Spaces”. In:
International Conference on Learning Representations Workshops(2026).
[LL26] Haibo Liu and Guang Lin. “DiLO: Decoupling Generative Priors and Neural Op-
erators via Diffusion Latent Optimization for Inverse Problems”. In:arXiv preprint
arXiv:2604.11375(2026).
[LT26] OscarLeongandYannTraonmilin.“ARecoveryTheoryforDiffusionPriors:Determin-
istic Analysis of the Implicit Prior Algorithm”. In:International Conference on Artificial
Intelligence and Statistics (AISTATS). 2026.
[Pap+26] Pinelopi Papalampidi, Olivia Wiles, Ira Ktena, Aleksandar Shtedritski, Emanuele
Bugliarello, Ivana Kajić, Isabela Albuquerque, and Aida Nematzadeh. “Dynamic
classifier-free diffusion guidance via online feedback”. In:International Conference on
Learning Representations (ICLR). 2026.
[Par+26] Sungwon Park, Anthony Zhou, Hongjoong Kim, and Amir Barati Farimani. “Genera-
tive Neural Operators through Diffusion Last Layer”. In:International Conference on
Machine Learning (ICML). 2026.
[Pen+24] YingleiPeng,MarkoRistić,AtulKedia,RichardO’Shaughnessy,ChristopherJ.Fontes,
Chris L. Fryer, Oleg Korobkin, Matthew R. Mumpower, V. Ashley Villar, and Ryan T.
Wollaeger. “Kilonova light-curve interpolation with neural networks”. In:Physical
Review Research(2024).
[Pid+24] JakiwPidstrigach,YoussefMarzouk,SebastianReich,andSvenWang.“Infinite-Dimensional
Diffusion Models”. In:Journal of Machine Learning Research(2024).
[PLA19] Joemini Poudel, Yang Lou, and Mark A Anastasio. “A survey of computational frame-
works for solving the acoustic inverse problem in three-dimensional photoacoustic
computed tomography”. In:Physics in Medicine & Biology(2019).
16

[Qin+23] Yilan Qin, Jiayu Ma, Mingle Jiang, Chuanfei Dong, Haiyang Fu, Liang Wang, Wenjie
Cheng,andYaqiuJin.“Data-drivenmodelingofLandaudampingbyphysics-informed
neural networks”. In:Physical Review Research(2023).
[Qua09] Alfio Quarteroni.Numerical models for differential problems. Springer, 2009.
[RGG97] Gareth O Roberts, Andrew Gelman, and Walter R Gilks. “Weak convergence and
optimal scaling of random walk Metropolis algorithms”. In:The Annals of Applied
Probability(1997).
[Rom+22] RobinRombach,AndreasBlattmann,DominikLorenz,PatrickEsser,andBjörnOmmer.
“High-resolution image synthesis with latent diffusion models”. In:Conference on
Computer Vision and Pattern Recognition (CVPR). 2022.
[Roz+24] François Rozet, Gérôme Andry, François Lanusse, and Gilles Louppe. “Learning
diffusion priors from observations by expectation maximization”. In:Advances in
Neural Information Processing Systems (NeurIPS)(2024).
[RPK19] Maziar Raissi, Paris Perdikaris, and George E Karniadakis. “Physics-informed neural
networks: A deep learning framework for solving forward and inverse problems
involving nonlinear partial differential equations”. In:Journal of Computational Physics
(2019).
[RT96] Gareth O Roberts and Richard L Tweedie. “Exponential convergence of Langevin
distributions and their discrete approximations”. In:Bernoulli(1996).
[Sap+24] Facundo Sapienza, Jordi Bolibar, Frank Schäfer, Brian Groenke, Avik Pal, Victor
Boussange, Patrick Heimbach, Giles Hooker, Fernando Pérez, Per-Olof Persson, et al.
“Differentiable programming for differential equations: A review”. In:arXiv preprint
arXiv:2406.09699(2024).
[Sha+26] SimingShan,MinZhu,YouzuoLin,andLuLu.“Regularizationbydenoisingdiffusion
modelsforsolvinginversePDEproblemswithapplicationtofullwaveforminversion”.
In:Communications Physics(2026).
[Shi+25] Yaozhong Shi, Zachary E Ross, Domniki Asimaki, and Kamyar Azizzadenesheli.
“Stochastic Process Learning via Operator Flow Matching”. In:Advances in Neural
Information Processing Systems (NeurIPS). 2025.
[Shi+26] Xiao Shi, Edward P. Chandler, Chicago Y. Park, Shirin Shoushtari, and Ulugbek S.
Kamilov.“NullFlow:One-StepGenerativeReconstruction”.In:arXivpreprintarXiv:2606.22696
(2026).
[Soh+15] Jascha Sohl-Dickstein, Eric Weiss, Niru Maheswaranathan, and Surya Ganguli. “Deep
unsupervised learning using nonequilibrium thermodynamics”. In:International Con-
ference on Machine Learning (ICML). 2015.
[Son+21] Yang Song, Jascha Sohl-Dickstein, Diederik P. Kingma, Abhishek Kumar, Stefano Er-
mon,andBenPoole.“Score-BasedGenerativeModelingthroughStochasticDifferential
Equations”. In:International Conference on Learning Representations (ICLR). 2021.
[SRL26] Thomas Savary, François Rozet, and Gilles Louppe. “Training-Free Bayesian Filtering
with Generative Emulators”. In:International Conference on Machine Learning (ICML).
2026.
[SRY26] Yaozhong Shi, Zachary E. Ross, and Yisong Yue. “Flow Annealing Posterior Sampling
forFunction-SpaceRegressionandInverseProblems”.In:arXivpreprintarXiv:2606.22346
(2026).
17

[Stu10] AndrewMStuart.“Inverseproblems:aBayesianperspective”.In:ActaNumerica(2010).
[Tho49] Llewellyn Hilleth Thomas. “Elliptic problems in linear difference equations over a
network”. In:Watson Sci. Comput. Lab. Rept., Columbia University, New York(1949).
[TV22] Manuel Tiglio and Aarón Villanueva. “Reduced order and surrogate models for gravi-
tational waves”. In:Living Reviews in Relativity(2022).
[Utk+25] Utkarsh Utkarsh, Pengfei Cai, Alan Edelman, Rafael Gomez-Bombarelli, and Christo-
pher Vincent Rackauckas. “Physics-Constrained Flow Matching: Sampling Generative
Models with Hard Constraints”. In:Advances in Neural Information Processing Systems
(NeurIPS). 2025.
[VO09] Jean Virieux and Stéphane Operto. “An overview of full-waveform inversion in explo-
ration geophysics”. In:Geophysics(2009).
[Wu+24a] Yuchen Wu, Minshuo Chen, Zihao Li, Mengdi Wang, and Yuting Wei. “Theoreti-
cal insights for diffusion guidance: A case study for Gaussian mixture models”. In:
International Conference on Machine Learning (ICML). 2024.
[Wu+24b] ZihuiWu,YuSun,YifanChen,BingliangZhang,YisongYue,andKatherineLBouman.
“Principled probabilistic imaging using diffusion models as plug-and-play priors”. In:
Advances in Neural Information Processing Systems (NeurIPS)(2024).
[WYZ23] Yinhuai Wang, Jiwen Yu, and Jian Zhang. “Zero-Shot Image Restoration Using Denois-
ingDiffusionNull-SpaceModel”.In:InternationalConferenceonLearningRepresentations
(ICLR). 2023.
[Xu+25] Tongda Xu, Xiyan Cai, Xinjie Zhang, Xingtong Ge, Dailan He, Ming Sun, Jingjing Liu,
Ya-QinZhang,JianLi,andYanWang.“RethinkingDiffusionPosteriorSampling:From
Conditional Score Estimator to Maximizing a Posterior”. In:International Conference on
Learning Representations (ICLR). 2025.
[Yan+26] Yiming Yang, Xiaoyuan Cheng, Yi He, Kaiyu Li, Wenxuan Yuan, and Zhuo Sun.
“Outlier-robust Diffusion Posterior Sampling for Bayesian Inverse Problems”. In:arXiv
preprint arXiv:2602.02045(2026).
[Yao+25] Jiachen Yao, Abbas Mammadov, Julius Berner, Gavin Kerrigan, Jong Chul Ye, Kamyar
Azizzadenesheli, and Anima Anandkumar. “Guided Diffusion Sampling on Function
SpaceswithApplicationstoPDEs”.In:AdvancesinNeuralInformationProcessingSystems
(NeurIPS). 2025.
[YKA25] Nebiyou Yismaw, Ulugbek S Kamilov, and M Salman Asif. “Gaussian is all you need:
A unified framework for solving inverse problems via diffusion posterior sampling”.
In:IEEE Transactions on Computational Imaging(2025).
[Zha+25] Bingliang Zhang, Wenda Chu, Julius Berner, Chenlin Meng, Anima Anandkumar,
and Yang Song. “Improving Diffusion Inverse Problem Solving with Decoupled Noise
Annealing”. In:Conference on Computer Vision and Pattern Recognition (CVPR). 2025.
18

A Notation
We use𝑎(·) to denote a function;a to denote a vector, which may be a discretization of function𝑎(·)
at collocation pointsx1,...,x 𝑛; and𝑎 to denote a scalar. We use𝒜 to denote an operator,𝒜ℎ to
denote a discretized operator at pointsx1,...,x 𝑛; andA to denote a linear operator (i.e., a matrix).
We use𝜋 to denote a probability distribution and𝑝 or𝑞 to denote its density, if it exists.∇x𝑓(x)
is taken to be either the gradient or Jacobian of𝑓, depending on the codomain dimension of𝑓.
We use1𝐴 to denote the indicator on event𝐴. We usea𝑡𝑘 to denote a sample drawn from the
VE diffusion reverse process at timestep𝑡𝑘, per Eq. (20), anda0 to denote a sample drawn from
the end of this process;ˆa(𝑡𝑘) 0 =𝐷 θ(a𝑡𝑘,𝑡 𝑘) to denote the denoiser output given samplea𝑡𝑘; a(𝑡𝑘) 0 to
denote the reconstruction of the signala obtained from a generic diffusion inverse solver at time𝑡𝑘;
and˜a(𝑡𝑘) 0 to denote the reconstruction of the signala obtained from DDIS specifically. We useuobs
systematically to denote the measurements.𝜋⇒𝜋 ′ represents convergence in distribution of𝜋 to
𝜋′. We denote by𝐿2(Ω)the space of square (Lebesgue) integrable functions on domainΩ.
B Function Space Diffusion Setup
Let K be a kernel matrix, with entriesK𝑖𝑗 =𝑘(x 𝑖,x𝑗), where𝑘 : R𝑑×R 𝑑→R is a trace-class,
positive definite kernel. For example,𝑘(·,·)can be the radial basis function (RBF) kernel
𝑘(x𝑖,x𝑗)=exp(−||x 𝑖−x 𝑗||2 2/ℓ)
for a fixed length scaleℓ> 0. We assume𝐾 is positive definite and write𝐾1/2 for its symmetric
positive definite square root. Let𝜎𝑡 > 𝜎0= 0for 𝑡> 0be a diffusion noise schedule, and assume
that𝑡↦→𝜎 2 𝑡 is continuously differentiable and nondecreasing. We write𝑝𝑡 for the density ofa𝑡 so
that a𝑡|a0∼𝒩(a 0,𝜎 2 𝑡 K) and consider the variance exploding (VE) diffusion forward process at
0<𝑡 0 <···<𝑡 𝑁 =𝑇:
a𝑡𝑘+1 =a 𝑡𝑘+
q
𝜎2 𝑡𝑘+1 −𝜎 2 𝑡𝑘 ε𝑘 , 𝑘=0,...,𝑁−1,(18)
where theε𝑘∼𝒩(0,𝐾)are independent across𝑘.
With𝑔(𝑡)=
q
𝑑
𝑑𝑡𝜎2 𝑡, the continuous-time forward process is given by the VE SDE:
𝑑a𝑡 =𝑔(𝑡)𝐾 1/2𝑑W𝑡 ,0≤𝑡≤𝑇 ,(19)
where𝑊𝑡 is an𝑛-dimensional Brownian motion. With𝑡 decreasing from𝑇 to0, the reverse VE SDE
is given by:
𝑑a𝑡 =−𝑔(𝑡) 2K∇a𝑡 log𝑝 𝑡(a𝑡)𝑑𝑡+𝑔(𝑡)K 1/2𝑑W𝑡 ,0≤𝑡≤𝑇 ,(20)
where W𝑡 is𝑛-dimensional Brownian motion in reverse time. To obtain the appropriate reverse
diffusion process, one learnssθ(a𝑡,𝑡)≈∇ a𝑡 log𝑝 𝑡(a𝑡) with score matching and then discretizes
Eq. (20) at times𝑡𝑘 via, e.g., Euler-Maruyama [KP92]. Additionally, by the function-space analogue
ofTweedie’sformula[Lim+25],whichafterdiscretizationyieldsthestandardmultivariateTweedie’s
formula [Efr11], we have:
𝐷∗(a𝑡,𝑡):=E[a 0|a𝑡]=a 𝑡+𝜎 2 𝑡 K∇a𝑡 log𝑝 𝑡(a𝑡).(21)
Wenotethatthisdoesnotrequire a0 tohaveadensity,makingitcompatiblewithourpriorinSec.3;
under this prior, a density is admitted for all numerical times𝑡0 <···<𝑡 𝑁, yielding that Eq. (21) is
well-defined. For a learned scoresθ, we denote the denoiser by𝐷θ.
19

C Extended Related Work
C.1 Classical Inverse Solvers
The partial differential equation (PDE) inverse problem in Sec. 2 is prevalent across many subfields
of science and engineering, including geophysics [VO09], astrophysics [Pen+24; CM22], fluid
dynamics [Bui+13], imaging [Arr99], and materials [Avr+08]. Thus, many methods have been
developed to solve PDE inverse problems [Bel12].
One key approach involves specifying different structured priors, such as Besov [DHS12]
or level set [ILS16] priors, and sampling from the posterior with an MCMC method such as
the preconditioned Crank-Nicolson method [Cot+13]. While these methods often come with
formal guarantees, they can take prohibitively long to sample from the posterior, especially under
multimodality or in high dimensions [GK07; GLR18].
Because of the expense of these methods, exact forward models are rarely used in the inner
loop, and rather domain-specific emulators are used instead. These forward models are often
highly tuned and problem-specific, limiting generalization. For example, the gravitational wave
communityreplacesitsexpensivenumericalrelativitysimulationswithhand-parametrizedeffective
models, and doing so has been a decades-long endeavor [TV22].
Recently, multi-fidelity techniques have been leveraged to build emulators in these data-sparse
environments [Gor+20]. Other methods include optimization-based samplers, such as randomize-
then-optimize methods [Bar+14], which repeatedly compute the maximum a posteriori estimate
underdifferentrandomperturbationsoftheobservationsandprior,aswellasensembleapproaches
based on the Kalman filter [ILS13]. These methods, however, fail to sample from the correct
posterior under nonlinear forward operators and complicated priors [ESS15].
Recently a concerted effort has been made in many communities, such as plasma physics
[Cit+24], to make differentiable forward models that may be placed into optimization loops
[Sap+24]. We note that many other methods have been developed for the inverse problem in
Sec. 2 without taking the Bayesian perspective, such as compressed sensing [AS21], but these only
produce point estimates, thus falling outside the scope of our work.
C.2 Physics-Informed Learning
Physics-informed learning has become a widely used approach for accelerating scientific com-
putation [Kar+21] across diverse fields such as climate modeling [Kas+21] and plasma physics
[Qin+23]. Below, we discuss key approaches towards solving forward and inverse problems.
C.2.1 Forward Solvers
Representative approaches to solving the forward problem include physics-informed neural net-
works (PINNs) [RPK19], which encode the governing PDE into the training objective, and neural
operators [Li+21], which learn mappings between function spaces and can amortize repeated PDE
solves. For modeling the forward operator, neural ODEs [Che+18] are often leveraged to replace a
component of a solver with a neural network. Deterministic formulations of these methods return
a single reconstruction rather than samples across the posterior. Probabilistic variants have been
developed [Par+26], but require problem-specific training and additional modeling assumptions.
We study methods which can be used across several measurement operators without retraining.
Thus, in our setting, we primarily use neural operators as differentiable surrogates for the forward
PDE operator and as the denoiser for function space diffusion in our experiments. Separately,
several approaches have been presented for physics-informed [BSK25] and physics-constrained
20

[Utk+25] generation; these approaches are complementary to, but distinct from, solving PDE
inverse problems with diffusion.
C.2.2 Priors
Diffusion models have seen enormous success in modeling complicated, high-dimensional priors
[Rom+22]. Thus, several recent works have constructed approaches to function space diffusion
priors. Kerrigan, Ley, et al. [KLS23] develop diffusion models on possibly infinite-dimensional
Hilbert spaces using Gaussian measures, and Pidstrigach, Marzouk, et al. [Pid+24] similarly
formulate diffusion models in infinite dimensions and study well-posedness and approximation
bounds. Lim, Kovachki, et al. [Lim+25] develop Denoising Diffusion Operators (DDO), where
neural operator architectures parameterize the learned score during score matching. These provide
a concrete mathematical and algorithmic basis for using diffusion models to model function space
priors for use in diffusion-based PDE inverse solvers.
C.2.3 Inverse Solvers
Duetotheirabilitytomodelcomplicatedpriors,diffusionmodelshavebeenadaptedtoPDEinverse
problems. In our work, we focus on developing diffusion solvers which are agnostic to the choice of
measurement operator; that is, one learned prior can be used with many different measurement
operators during inference. DiffusionPDE [Hua+24] replaces the diffusion likelihood𝜋(uobs|a𝑡)
withaGaussiancenteredatthedenoiserestimate ˆa(𝑡) 0 ,andsamplesfromthejointdistribution (a,u).
Notably, DiffusionPDE trains a standard diffusion prior at fixed discretization; instead, FunDPS
[Yao+25]trainsafunctionspaceprior. Morerecentwork,suchasthestate-of-the-artDDIS[Lin+26],
has decoupled the physical parameter and solution fields(a,u), specifically approximatingu with
a neural operator surrogate while performing prior learning and posterior sampling ona. In our
work,wealsodecouplethelearningof aand u. DDISalsorelaxestheassumptionsofDiffusionPDE
andFunDPS;insteadofapproximatingthediffusionlikelihoodwithaGaussian,DDISapproximates
𝜋(a0|a𝑡)withanisotropicGaussian,asdiscussedinSec.3. Anotherapproach,RED-DiffEq[Sha+26],
performs regularized optimization on the measurement consistency objective, but uses diffusion to
encode the regularization; however, this approach is not Bayesian and has not been compared with
the strong diffusion posterior samplers discussed above. The concurrent work DiLO [LL26] adopts
the same decoupling as DDIS, but instead discusses the issue of evaluating the neural operator
surrogate on noisy diffusion statesa𝑡 instead of clean reconstructions, which the operator was
originally trained on. We note that their solution for this issue can easily be incorporated into our
input optimization procedure introduced in Sec. 4, and the failure modes of the neural operator
surrogate are not the focus of our work. Additionally, the concurrent work FAPS [SRY26] is similar
to DDIS, instead using operator flow matching [Shi+25] to encode the prior and approximating the
denoising distribution with an anisotropic Gaussian.
To distinguish these diffusion PDE inverse solvers, consider two key operations that occur
within a reverse sampling step𝑡𝑘 with noisya𝑡𝑘: (D) computing an estimate of the signal𝑎(·) as
ˆa(𝑡𝑘) 0 =𝐷 θ(a𝑡𝑘,𝑡 𝑘), where𝐷θ is the diffusion denoiser and (M) enforcing measurement consistency
on a reconstructiona(𝑡𝑘) 0 ≈ˆa(𝑡𝑘) 0 , so that it is consistent with the observations (i.e.,𝒜(a(𝑡𝑘) 0 )≈u obs).
We use the termoutput space optimizationto describe methods where (D) and (M) aredisjoint, since
this amounts to optimizing in the output space of the denoiser, while leaving the denoiser input
fixed. Fromthisperspective,DiffusionPDE[Hua+24],FunDPS[Yao+25],andDecoupledDiffusion
Inverse Solver (DDIS) [Lin+26] are all output space optimization procedures. We discuss this
further in App. E.
21

In Sec. 3, we demonstrate that output space approaches can fail to update unobserved compo-
nentsofthedenoiserestimateappropriatelyforaPDEinverseproblem. Wethususethistomotivate
input space optimizationin Sec. 4, where steps (D) and (M) arecombined: we iteratively compute the
denoiseroutput(D)andoptimizetheinputsuchthatmeasurementconsistencyissatisfied(M).We
show that this updates the unobserved components as desired. This results inbackward-consistent
sampling [Alk+25], where the reconstruction is constrained to be in the denoiser’s range. We note
thatourapproachisdifferent,motivatedbythesettingofPDEinverseproblemswherepriorscanbe
sharply multimodal and with a new approach to allocate input optimization steps motivated by our
theory. Additionally, the concurrent work FAPS [SRY26] uses its anisotropic Gaussian covariance
to precondition the measurement gradient. We note that input space optimization can be viewed
aspreconditionedoutput space optimization, as discussed in App. J. Note that our preconditioner
differs from FAPS, and furthermore is grounded in the theory of PDE inverse problems and does
not require additional estimation from training data after the diffusion model has been trained.
The computer vision literature also contains several approaches to address the unobserved
componentofthereconstructionwhilesolvingtheinverseproblem. Mostnotably,DDNM[WYZ23]
assumesalinearforwardoperatoranddoesdiffusiononlyinnullspace; NullFlow[Shi+26]extends
thisapproachtoone-stepsamplingwithflowmatching. Notethattheseapproachesdonotsolvethe
issue that DDIS suffers from discussed in Prop. 1. In particular, the nullspace component of the re-
constructionisstillthesameasthatofthedenoiser. Separately, Posterior-DDIM[Jia+26b]performs
ODE-based diffusion sampling in each singular direction separately, incorporating measurement
consistencyinasingulardirectiononlywhenthediffusionsignal-to-noiseratioissmall. Importantly,
this approach assumes a linear forward operator so that the singular value decomposition is easily
computable. However, PDE inverse problems can have highly nonlinear forward operators, e.g.,
Darcy flow as considered in our experiments in Sec. 5. One can obtain a local approximation with
the Jacobian, but this still comes at a high computational expense and may not have the same
desirable properties.
Finally, note that there have been several recent approaches developed to use diffusion for data
assimilation [And+26; Jia+26a]. While data assimilation is closely related to Bayesian inverse
problems, it considers a sequential setting; rather than recovering a fixed coefficient fielda from
measurements uobs, data assimilation repeatedly propagates a statea(ℓ) 0 and assimilates new obser-
vationsu(ℓ) obs. Accordingly, recent generative data assimilation work focuses on combining learned
generative priors with state transition operators. These approaches are complementary to our work.
Furthermore, moment-matching posterior samplers like DPS [Chu+23] or MMPS [Roz+24] have
been adopted for use in data assimilation [Che+25; SRL26]; backward-consistent sampling can be
adopted as well, and we leave a comprehensive study of this to future work.
C.3 Theoretical Guarantees
Classical inverse solver theory provides guarantees for recovering an unknown signal from in-
complete observations. For deterministic inverse problems, where one recovers a point estimate,
regularization theory extensively studies the existence, stability, and convergence of solutions,
especially with linear forward operators [EHN96]. Bayesian inverse solver theory studies when the
posterior is well-defined and when the problem is well-posed and stable [Stu10]; theory for MCMC
methods is likewise used to study MCMC-based solvers for these problems [HSV14], including
using diffusion priors [Wu+24b]. Due to the prevalence of these diffusion priors in recent inverse
solvers, recent works likewise have developed theory for diffusion inverse solvers. For Gaussian
priors, approximating the denoising distribution exactly by first- and second-moment Tweedie’s
22

formulas can recover the posterior [Boy+24]. Other recent work obtains insights into the bias and
stability of diffusion posterior samplers [Del+26]; the robustness of these samplers to likelihood
misspecification and outliers [Yan+26]; connections to projected gradient descent and its conver-
gence theory [LT26]; convergence to the posterior [Jia+26b]; and how this relates to maximum
a posteriori estimation [Xu+25]. Notably, Burns and Fridovich-Keil [BF26] study multimodal
priors; however, they focus on a different failure mode of diffusion posterior samplers, specifically
issues with likelihood approximations such as those made by DPS. Additionally, several works
have used multimodal Gaussian mixture priors to empirically study the behaviors of diffusion
posterior samplers [CV25; YKA25]; however, these works do not study the PDE setting or the
unobserved components of the denoiser. Much of the literature studies the finite-dimensional
image inverse problem setting; for the function space setting present in our PDE inverse problems,
FunDPS [Yao+25] develops an analogue of Tweedie’s formula while DDIS [Lin+26] obtains theo-
retical results characterizing why learning the coupled prior(a,u) is problematic, motivating the
learning of the prior over onlya done in both their and our algorithms. More broadly, there has
been significant work on how diffusion models select modes under multimodal priors [Wu+24a;
Ash+26]. Our work adds to this literature in the PDE inverse problem setting; we study when and
whydiffusionsolversbasedonoutputspaceoptimizationfailinthePDEsetting,wheremultimodal
priors naturally arise, and instantiate a solution based on input space optimization, validating our
results empirically. We also study what unique conditions on the measurements and nullspace
components of different prior modes arise due to the PDE setting in Prop. 8 in App. K.11 and
connect our results to preconditioning in App. J.
The effectiveness of conditioning in diffusion models depends on when and how guidance is
applied throughout the reverse process; while classifier and classifier-free guidance are frequently
implemented using a constant guidance scale, several works show that this is suboptimal across
diffusionnoiselevels[Pap+26]. InthesettingofBayesianinversesolversbasedondiffusionmodels,
there has been work done on designing schedules for likelihood or measurement guidance across
the diffusion sampling process. For example, Jacobian-aware posterior sampling [Hen+26] adapts
the step size of the likelihood gradient based on the denoiser Jacobian, while the recent work
TriPS [Ban+26] adjusts this step size for conditional priors based on the classifier-free guidance
schedule and added stochasticity in the sampling process. Additionally, Delgadino, Motsch, et al.
[Del+26] show that DPS guidance can become numerically unstable towards the end of the reverse
process, providing a principled explanation for early stopping the DPS measurement-consistency
guidance in the sampling process. We add to this body of work, designing a principled approach
to scheduling input optimization steps across noise levels based on our theoretical analysis of an
inverse problem on Poisson’s equation. Notably, we control a different quantity than, e.g., gradient
stepsizeorguidanceweight;instead,wecontrolthecomputationaleffortusedtoenforcemeasurement
consistency at each diffusion noise level, done so by a function that automatically allocates more
steps on critical noise levels during inference.
D Limitations & Future Directions
Limitations include that FunBCS is reliant on the accuracy of the neural operator surrogate𝒢ℎ,ϕ
and the diffusion prior𝜋(a). Additionally, our current input optimization scheduler requires
task-specific calibration. Future directions include addressing these limitations, improving our
method further for discontinuous inverse problems by, e.g., using discontinuous bases [ILS16], and
extending input space optimization to PDE data assimilation [Che+25].
23

E Overview of Recent Diffusion PDE Inverse Solvers
We provide an overview of the recurrences of diffusion PDE inverse solvers, to make clear how
existing methods perform output space optimization (with separate (D) and (M) steps) while our
method performs input optimization (combined (D) and (M) steps). We present these all for fixed
diffusion times𝑡𝑘 >𝑡 𝑘−1.
DiffusionPDE/FunDPS recurrence. DiffusionPDE [Hua+24] applies diffusion posterior sam-
pling [Chu+23] with a standard diffusion prior at a fixed discretization, and FunDPS [Yao+25]
extends it to function space priors. Both use the following recurrence:
a(𝑃) 𝑡𝑘−1=˜a(𝑃) 𝑡𝑘−1−𝜁 𝑘∇a(𝑃) 𝑡𝑘 ∥𝒜ℎˆa(𝑃,𝑡𝑘) 0 −u obs∥2 2 ,(22)
where:
˜a(𝑃) 𝑡𝑘−1=a(𝑃) 𝑡𝑘 +Δ𝑡𝑘 sθ(a(𝑃) 𝑡𝑘 ,𝑡 𝑘)+ p Δ𝑡𝑘 ε(𝑃) 𝑘 ,(23)
andΔ𝑡𝑘 =𝑡 𝑘−𝑡 𝑘−1 withˆa(𝑃,𝑡𝑘) 0 :=𝐷 θ(a(𝑃) 𝑡𝑘 ,𝑡 𝑘), andε(𝑃) 𝑘 ∼𝒩(0,I) for DiffusionPDE and𝒩(0,K) for FunDPS, independent across𝑘.
Remark 8.At a timestep𝑡𝑘, one first computesˆa(𝑃,𝑡𝑘) 0 (i.e.,(D)); this can then be used in the
measurementconsistencyterminEq.(22)aswellastoestimate sθ byTweedie’sformulaperEq.(4),
used in Eq. (23). DPS then performs a renoising-type step in Eq. (23), and subsequently enforces
measurementconsistency(i.e.,performs(M)inEq.(22)). Wenotethatthesetwostepsareseparate
at diffusion timestep𝑡𝑘, so that measurement consistency is enforced by optimizing over the output
space of the denoiser. That is, methods such as DiffusionPDE and FunDPS perform output space
optimization.
DDIS recurrence. As presented in Eq. (6), the DDIS recurrence is given by:
a(𝐷) 𝑡𝑘−1 =˜a(𝑡𝑘) 0 +𝜎 𝑡𝑘−1 ε(𝐷) 𝑘 ,˜a (𝑡𝑘) 0 ∼𝑞 𝐷,𝑡𝑘(·|a(𝐷) 𝑡𝑘 ,u obs),ε (𝐷) 𝑘 ∼𝒩(0,K),(24)
with
𝑞D,𝑡𝑘(a0|a(𝐷) 𝑡𝑘 ,u obs)∝exp
(
−∥𝒜ℎa0−u obs∥2
2𝛾2 −
∥a0−ˆa(𝐷,𝑡𝑘) 0 ∥2
2𝜎2 𝑡𝑘
)
.(25)
whereˆa(𝐷,𝑡𝑘) 0 :=𝐷 θ(a(𝐷) 𝑡𝑘 ,𝑡 𝑘)and𝜀 (𝐷) 𝑘 are drawn independently.
Remark 9.At a timestep𝑡𝑘, one first computesˆa(𝐷,𝑡𝑘) 0 (i.e.,(D)). DDIS then incorporates this
into Eq. (25) to sample from𝑞𝐷,𝑡𝑘; from the perspective of Langevin dynamics, this is precisely
optimizing in the output space of the denoiser by enforcing measurement consistency (M) with
the first term and ensuring the reconstruction does not deviate too far from the denoiser estimate
per the second term. Subsequently, DDIS renoises up to timestep𝑡𝑘−1 per Eq. (24). Computing
the denoiser output and enforcing measurement consistency are clearly separated. Thus, DDIS
performs output space optimization.
FunBCS recurrence. As presented in Eq. (13), the FunBCS recurrence is given by:
a(𝐵) 𝑡𝑘−1 =𝐷 θ(v(𝑠),𝑡 𝑘)+𝜎 𝑡𝑘−1 ε(𝐵) 𝑘 ,ε (𝐵) 𝑘 ∼𝒩(0,K),(26)
24

wherev(𝑠)is a solution to the gradient flow:
𝑑v(𝑠)
𝑑𝑠 =−∇ v
∥𝒪ℎ◦𝒢 ℎ,𝜙◦𝐷 θ(v,𝑡 𝑘)−u obs∥2
2𝛾2

v=v(𝑠)
,v(0)=𝑎 (𝐵) 𝑡𝑘 ,(27)
andε(𝐵) 𝑘 are drawn independently.
Remark 10.At a fixed diffusion timestep𝑡𝑘, per Eq. (27), for an optimization step𝑠𝑖, we alternate
between computing the denoiser output𝐷θ(v(𝑠𝑖),𝑡 𝑘) and finding the inputv(𝑠𝑖+Δ 𝑠) so that
measurement consistency is satisfied. This thus optimizes in theinputspace of the denoiser and
couples steps (D) and (M). Hence, our method FunBCS is an input space optimization procedure.
F Experimental Details
Tasks.We use the four PDE inverse problems of DDIS [Lin+26], whose data were generated
by DiffusionPDE [Hua+24] with the solvers of FNO [Li+21]; we use the normalized version
provided with DDIS’s public codebase. Every problem is posed on the unit squareΩ =(0, 1)2,
discretizedona128 × 128grid. Ineachproblem,werecoverthecoefficientfield 𝑎 from500noiseless
observationsofthesolution 𝑢atrandomgridpoints,about3%ofthegrid. Theobservationlocations
are drawn anew for each test sample and are the same for FunBCS, DDIS and FunDPS, whereas
DiffusionPDE’s public code uses one fixed set of locations for every sample. Below,∇2 denotes
the Laplacian, and a Gaussian random field with parameters(𝛼,𝜏) has covariance proportional to
(−∇2+𝜏 2𝐼)−𝛼. The coefficient fields of Poisson, Helmholtz and Darcy flow are all built from such a
field with(𝛼,𝜏)=(2,3)and zero Neumann boundary conditions.
Poisson.The source term𝑎is the Gaussian random field above, and
∇2𝑢(x)=𝑎(x),x∈Ω, 𝑢(x)=0,x∈𝜕Ω.
Helmholtz.Thesourceterm 𝑎isdrawnasforPoissonandsettozeroon 𝜕Ω,andwithwavenumber
𝑘=1,
∇2𝑢(x)+𝑘 2𝑢(x)=𝑎(x),x∈Ω, 𝑢(x)=0,x∈𝜕Ω.
Navier–Stokes.The vorticity 𝑤=∇×v of an incompressible velocity fieldv on the periodic
domainΩevolves as
𝜕𝑡𝑤+v·∇𝑤=𝜈∇ 2𝑤+𝑓,∇·v=0,x∈Ω, 𝑡∈(0,𝑇],
with viscosity𝜈= 10−3 (Reynolds number1,000) and forcing𝑓(x)= 0.1  sin(2𝜋(𝑥1+𝑥 2))+
cos(2𝜋(𝑥1+𝑥 2))

. The coefficient field is the initial vorticity𝑎=𝑤(·, 0), a periodic Gaussian random
field with(𝛼,𝜏)=(2.5,7), and the solution is the vorticity𝑢=𝑤(·,𝑇)at𝑇=1.
Darcy flow.The permeability𝑎 equals12where a Gaussian random field drawn as for Poisson is
nonnegative and3elsewhere, so it is piecewise constant, and
−∇·

𝑎(x)∇𝑢(x)

=1,x∈Ω, 𝑢(x)=0,x∈𝜕Ω.
DDIS’s public codebase supports Darcy flow, but DDIS does not report it, so we include it
because its piecewise-constant coefficient makes the prior multimodal.
25

Evaluation.All methods are evaluated on the same100test samples. On Poisson, Helmholtz and
Navier–Stokes, we report the relativeℓ2 error∥ˆ𝑎−𝑎∥ 2/∥𝑎∥ 2 in percent. On Darcy flow, we threshold
the reconstruction at7.5, the midpoint of the two coefficient values, and report the percentage of
misclassified pixels [Hua+24]. The spectral energy error, from [Lin+26],𝐸𝑠 compares the radially
averaged power spectraˆ𝑃(𝑘) and𝑃(𝑘) of the reconstruction and of the ground truth. We take the
geometric mean of|ˆ𝑃(𝑘)−𝑃(𝑘)|/𝑃(𝑘) over wavenumbers𝑘, and then average over the test samples.
Modelsandsamplers.FunBCSusesthesamepretraineddiffusionprior,neuraloperatorsurrogate
and noise schedule as DDIS [Lin+26]. DDIS uses the settings of DDIS’s public codebase:100noise
levels,20Langevinstepsperlevel,andthelikelihoodweightsrecommendedinthepaper. ForDarcy
flow,whichDDISdoesnotreport,wetunedandchosetheweight30from {5, 10, 15, 20, 30}. FunBCS
uses𝑁= 10noise levels and optimizes the denoiser input with Adam at learning rate𝛾= 0.03.
Its scheduling function (App. G) uses the selection windows(𝜎low,𝜎 high)=( 0, 0.711) on Poisson,
(0, 0.335) on Helmholtz,(0, 0.144) on Navier–Stokes and(0.335, 2.6) on Darcy flow. FunBCS-AC
uses𝑀=𝑁𝐾= 800optimization steps per sample, and FunBCS-EF uses𝑀★= 607,506,406and
488steps on the four tasks, respectively. We note that these𝑀★ budgets are not hardcoded, but
instead dynamically determined by our method during inference.
Baselines.DiffusionPDE [Hua+24] trains a diffusion model on the joint distribution of the coeffi-
cient and solution fields at a fixed resolution, and guides its sampling with the observation misfit
and the PDE residual, evaluated on the denoiser estimate. FunDPS [Yao+25] follows the same
approach with a joint diffusion prior in function space built from neural operators. DDIS [Lin+26]
learns a diffusion prior on the coefficient field only, predicts the solution with a neural operator
surrogate, and enforces the observations with annealed Langevin sampling in the output space
of the denoiser. We run each baseline with its authors’ public code and default settings. For the
scaling curves of Figs. 3 and 6, we run every method at0.5×,1×,2×and4×its default budget and
change nothing else: FunBCS with400,800,1,600and3 ,200optimization steps, distributed over
its𝑁= 10noise levels by the scheduling function; DDIS with50,100,200and400noise levels of
20Langevin steps each, that is,1,000to8 ,000Langevin steps; and FunDPS with250,500,1,000
and2,000sampling steps. DiffusionPDE, which is much slower, is run with500,2,000and3 ,000
sampling steps, where2,000is its default.
Choosing𝑁 and𝐾.We fix the max budget of FunBCS at𝑁𝐾= 800optimization steps. In order
to determine the optimal𝑁, assuming a uniform allocation of𝐾 inner steps per outer level, we had
to choose how to split between the number of noise levels𝑁 and the number of steps𝐾 per level.
Figure 5 compares three splits on Poisson and Darcy flow. These runs place the same𝐾 steps on
every noise level and do not use the scheduling function at all, so that the choice of𝑁 and𝐾 is not
confounded with how the steps are allocated. The split𝑁= 10,𝐾= 80reaches the lowest error on
both tasks, and we use it for every task. The scheduling function then redistributes these800steps
across the𝑁=10noise levels (App. G).
Timing.WemeasuresecondspersampleonasingleNVIDIAA100GPUwithoneprocessperGPU,
atbatchsize25forFunBCS,DDISandFunDPSandatbatchsize1forDiffusionPDE.DiffusionPDE’s
public code reconstructs one test sample at a time, with a single ground truth, observation mask
and guidance loss per run, so we time it unmodified at batch size1. The time covers the whole
sampling process, including all denoiser and surrogate evaluations. Each optimization step of
FunBCSdifferentiatesthroughboththedenoiserandthesurrogate,soitcostsmorethanaLangevin
26

Figure5: ReconstructionerrorofFunBCSduringsamplingforthreesplits 𝑁×𝐾 of800optimization
steps, with the same𝐾 at every noise level and without the scheduling function, on50samples:
relativeℓ2 error on Poisson (left) and pixel error rate on Darcy flow (right). The error jumps up at
the end of each noise level, when the sample is renoised.
step of DDIS, which differentiates through the surrogate only. FunBCS, however, uses10noise
levels instead of100, which DDIS uses.
Scaling with compute.Figure 6 shows the error of every method against its time per sample on
Helmholtz, Navier–Stokes and Darcy, as Fig. 3 does for Poisson. As on Poisson, FunBCS is more
accurate than every baseline at every budget, and at about8seconds per sample it is more accurate
than every baseline at any of the budgets we tested.
G The Proposed Scheduling Function
A uniform schedule gives every noise level the same number of optimization steps, although the
analysis of Sec. 4.2 shows that steps matter unequally across noise levels: every level needs a few, so
that a lean towards the wrong mode is corrected before it is carried to lower noise levels (Prop. 4),
and the remaining steps are worth the most inside the selection window (Prop. 5). The scheduling
function therefore treats the optimization steps of algorithm 1 as a total budget𝑀 and allocates it
across noise levels, keeping a floor at every level and concentrating the remainder in the selection
window. Figure 7 shows the resulting allocations, and that withholding the steps of a single noise
levelhurtsmostwheretheschedulerconcentratesthem. Wedefinetheallocationbelow,thenablate
it (App. G.1), describe how the window is tuned (App. G.2), and apply it to DDIS (App. G.3).
Effort weights.The scheduling function assigns each noise level𝜎 an effort weight through a
smooth window whose only task-specific parameters are the two edges𝜎low≤𝜎 high of the selection
window:
𝜔(𝜎)=
h
1+(𝜎/𝜎 high)𝛽
i−1h
1+(𝜎 low/𝜎)𝛽
i−1
.(28)
The weight is close to one inside the window and decays polynomially outside it, at a rate set by
the exponent𝛽 >0. Setting𝜎low= 0removes the lower edge, setting𝜎high=∞ removes the upper
edge, and𝛽→∞ recovers a hard window. Because𝜔 depends on the noise level rather than on the
index𝑘, the same edges apply to any number and spacing of noise levels.
27

5
 10
 20
 50
 100
 200
 500
time per sample (s)
8
10
12
14
16
18rel. ℓ2 error (%)
DiﬀPDE
FunDPS
DDIS
FunBCS
Helmholtz
5
 10
 20
 50
 100
 200
 500
time per sample (s)
6
7
8
9
10rel. ℓ2 error (%)
DiﬀPDE
FunDPS
DDIS
FunBCS
Navier–Stokes
5
 10
 20
 50
 100
 200
 500
time per sample (s)
2
4
6
8error rate (%)
DiﬀPDE
FunDPS
DDIS
FunBCS
Darcy
Figure 6: Scaling behavior of all methods with increasing inference time per sample on Helmholtz,
Navier–Stokes and Darcy, as in Fig. 3 for Poisson. Darcy reports the pixel error rate. All methods
are run using the same hardware.
0
100
200
optimization steps F(tk)
M⋆ = 488 (61% of NK)
σhigh σlow
Darcy (discontinuous PDE)
2.82%
2.32%
2.69%
accuracy mode, M = NK
eﬃciency mode, M = M⋆
0
100
200
M⋆ = 607 (76% of NK)
σhigh
Poisson (smooth PDE)
10.51%
9.60%
10.22%
uniform, K = 80 per level
ﬂoor kmin = 10
10
 6
 3.5
 1.9
 1
 0.5
 0.23
 0.09
 0.03
 0.01
0.0
1.1
∆ error
10
 6
 3.5
 1.9
 1
 0.5
 0.23
 0.09
 0.03
 0.01
0.0
0.5
noise level σtk (sampling proceeds from left to right)
Figure 7:Top: Optimization steps per noise level under the scheduling function (App. G). The
accuracy mode (blue) reallocates the𝑁𝐾= 800steps of the uniform allocation (grey) towards
the selection window (shaded), and the efficiency mode (red) cuts the budget to𝑀★; every noise
level keeps at least𝑘min= 10steps (dotted). Numbers give the resulting error (Table 1).Bottom:
increase in error, in percentage points, when a single noise level receives no optimization steps,
which is largest where the scheduler places its steps.
Allocation.Given a total budget of𝑀 optimization steps, the scheduler reserves a floor of
𝑘min steps at every noise level and distributes the remainder in proportion to the effort weights
𝜔𝑘 :=𝜔(𝜎 𝑡𝑘):
𝐹(𝑡𝑘)=𝑘 min+

𝑀−𝑁𝑘 min
 𝜔𝑘
˝𝑁
𝑗=1 𝜔𝑗
, 𝑘=1,...,𝑁.(29)
We round each share down and give the remaining steps, one each, to the noise levels with the
largest remainders, so that˝ 𝑘𝐹(𝑡𝑘)=𝑀 exactly. A uniform allocation of𝐾 steps per noise level
corresponds to𝜔≡ 1, and at the same budget𝑀=𝑁𝐾 , Eq. (29) moves steps towards the selection
28

window without changing the cost of the sampler.
Accuracy and efficiency modes.Since the effort weights identify the noise levels on which
optimization steps matter, the scheduler also determines a natural budget below𝑁𝐾:
𝑀★=𝑁𝑘 min+(𝐾−𝑘 min)
˝
𝑗 𝜔𝑗
𝜏max𝑗 𝜔𝑗
,𝜏∈(0,1],(30)
capped at𝑁𝐾. At this budget, Eq. (29) assigns exactly𝐾 steps to a noise level whose weight is a
fraction𝜏 of the peak, so every noise level with at least this weight keeps at least as many steps as
under the uniform allocation, and the saving comes from the noise levels outside the window. We
call𝑀=𝑁𝐾 theaccuracy modeand 𝑀=𝑀 ★ theefficiency mode, and write FunBCS-AC and FunBCS-
EF for FunBCS in these two modes. For every run, FunBCS-AC seeks to non-uniformly disperse
the 𝑀 total optimization steps in order to reach higher accuracy without changing the budget,
while FunBCS-EF seeks to cut as much budget as possible while maintaining similar accuracy to
the uniform allocation. During inference, one can easily interpolate between the two modes with
no tuning as the two modes differ only in the budget.
Shared constants.All FunBCS experiments use𝛽= 2,𝑘min= 10and 𝜏= 0.7on every PDE and
in both modes, with𝑁= 10noise levels and𝐾= 80, so that the accuracy mode has a budget of800
steps. Only the window edges are chosen per PDE (App. G.2):(𝜎low,𝜎 high)=( 0, 0.711) on Poisson,
(0,0.335)on Helmholtz,(0,0.144)on Navier–Stokes and(0.335,2.6)on Darcy.
G.1 Scheduler Ablations
Table1comparesFunBCSwiththescheduler(FunBCS-ACandFunBCS-EF)againstFunBCSwithout
it, which places𝐾= 80optimization steps on each of its𝑁= 10noise levels. At the same budget of
800steps, the accuracy mode lowers the error by10%on average, and on every task, at unchanged
cost. The efficiency mode removes37%of the steps on average, which makes FunBCS1.6× faster,
with2%lower error on average. On Poisson, Helmholtz, Navier–Stokes and Darcy, it uses607,506,
406and488of the800steps, which take12 .6,10.5,8.4and10 .1seconds per sample; Table 1 reports
their mean. Even without the scheduler, FunBCS is more accurate than every baseline on every
task, and faster than DDIS.
Varying the shared constants.Figures 8 to 10 vary the three constants that are shared across
tasks, on50samples with everything else fixed. The slope𝛽 controls how sharply the effort weight
ofEq.(28)fallsoffattheedgesofthewindow. As 𝛽→ 0,theweightbecomesflatandtheallocation
approaches the uniform one; as𝛽→∞ , the window becomes a hard box, and every noise level
outside it keeps only the floor. We use𝛽= 2, which gives the lowest error averaged over the four
tasks. The constant𝜏 controls the budget of the efficiency mode through Eq. (30). At𝜏= 1, the
noise level with the largest weight keeps the𝐾 steps of the uniform allocation and all other levels
receive fewer; lowering𝜏scales the steps above the floor by1/𝜏, until𝑀★ reaches the budget𝑁𝐾 of
the accuracy mode. The floor𝑘min is the number of steps that every noise level keeps regardless of
its weight. Without a floor, the noise levels outside the window receive almost no steps, while a
large floor moves the allocation back towards the uniform one.
G.2 Tuning the Selection Window
Since𝛽,𝑘min and𝜏 are shared across tasks, only the two edges of the selection window are set for a
new PDE. We choose them with the grid search of algorithm 2, run with FunBCS in the accuracy
mode. The candidate edges are the geometric midpoints between consecutive noise levels, roughly
a factor of two apart; the upper edge is selected first, and a lower edge is kept only if it lowers the
29

0.5
 1
 2
 4
 6
 ∞
9.6
9.8
10.0
10.2
10.4error (%)
uniform, 800 steps
Poisson
0.5
 1
 2
 4
 6
 ∞
9.2
9.4
9.6
9.8
10.0
10.2
Helmholtz
0.5
 1
 2
 4
 6
 ∞
5.7
5.8
5.9
6.0
Navier–Stokes
0.5
 1
 2
 4
 6
 ∞
2.4
2.6
2.8
Darcy
slope β of the eﬀort weight
Figure 8: Error of FunBCS in the accuracy mode on50samples as the slope𝛽 of Eq. (28) varies, at
the selected window edges;∞ denotes a hard window, and the outlined marker is the value used,
𝛽= 2. The grey line is the uniform allocation of the same800steps. Darcy reports the pixel error
rate and the other tasks the relativeℓ2 error.
400
 600
 800
9.5
10.0
10.5
11.0error (%)
τ = 0.7
τ = 1
M = NK
Poisson
400
 600
 800
9.5
10.0
10.5
11.0
τ = 0.7
Helmholtz
400
 600
 800
5.7
5.8
5.9
6.0
6.1
τ = 0.7
uniform, 800 steps
Navier–Stokes
400
 600
 800
2.4
2.6
2.8
3.0
3.2
τ = 0.7
Darcy
optimization steps per sample, M⋆(τ)
Figure 9: Error of FunBCS on50samples against the budget𝑀★ resolved by Eq. (30) for𝜏=
1, 0.9, 0.8, 0.7, 0.65, 0.6and0 .5, from left to right. The outlined marker is the value used,𝜏= 0.7,
the square is the accuracy mode (𝑀=𝑁𝐾= 800), and the grey line is the uniform allocation at800
steps. On Poisson,𝜏=0.5reaches the cap and coincides with the accuracy mode.
error further. Each candidate window is evaluated on20samples, so the search, which needs at
most nine runs, takes about50minutes per PDE on a single A100 GPU.
Sensitivitytothewindowedges.Acoarsegridsufficesbecausetheerrordependsontheshape
of the window far more than on the exact position of its edges. Figure 11 shows this on Darcy,
the only task whose selected window has both edges. Moving one or both edges of the selected
window by one grid step, a factor of about two in𝜎, keeps the error rate between2.34and2 .60%,
against2.88%for the uniform allocation, and12of the13windows with both edges improve on the
uniformallocation. Awindowofthewrongshape, incontrast, doesnot: threeofthefourone-sided
low-noise windows that suit the smooth tasks are worse than uniform on Darcy, with error rates
up to4.67%. The selection window is therefore not a sensitive choice. Once its shape is right, each
edge only needs to be located to within a grid step, which the coarse search of algorithm 2 does in a
30

0
 5
 10
 20
 30
 40
ﬂoor kmin
9.2
9.4
9.6
9.8
10.0
10.2
10.4
10.6
10.8error (%)
uniform, 800 steps
800 steps
560 steps
Helmholtz
Figure 10: Error of FunBCS on Helmholtz
on50samples as the floor𝑘min varies, at800
and at560steps. Outlined markers are the
value used,𝑘min= 10, and the grey line is the
uniform allocation at800steps.
0.711 1.4 2.6 4.59 ∞
upper edge σhigh
0
0.144
0.335
0.711
1.4
lower edge σlow
4.67 3.37 2.92 2.78 2.88
uniform
3.22 2.60 2.50 2.49 2.58
2.76 2.46 2.38 2.42 2.54
2.37 2.34 2.41 2.64
2.42 2.56 2.96
2.4
2.88
3.5
4.5
Darcy error rate (%)
Figure 11: Darcy error rate (%) of FunBCS on50
samples for each window;𝜎low= 0and 𝜎high=∞
removeanedge, sothebottom-rightcellistheuni-
formallocation. Bluecellsbeatit,andtheoutlined
cell is the selected window.
Algorithm 2Finding the selection window for each PDE
Require: AfewsamplesofthePDE(outsidethetrainingandtestingsets);setofcandidatewindow
bounds𝒮, the midpoints√𝜎𝑡𝑘𝜎𝑡𝑘+1 between consecutive noise levels; a tolerance𝜖 for noise in
the measured error.
1: Run every configuration below with FunBCS (algorithm 1) in the accuracy mode, using the
shared𝛽and𝑘 min.
2:Measure the error𝑒 uni of the uniform allocation.
3:Upper bound.For each𝑠∈𝒮, measure the error𝑒(𝑠)of the window(0,𝑠).
4: Set𝜎high tothe 𝑠 withthelowesterror,orto ∞(noupperbound)ifnowindowbeatstheuniform
allocation. If𝜎high is the smallest or largest candidate, also try the next midpoint beyond it and
keep the better of the two.
5: Lower bound.For each𝑠∈𝒮 below𝜎high, measure the error𝑒′(𝑠) of the window(𝑠,𝜎 high), and
let𝑠 ★ be the𝑠with the lowest error.
6: Set 𝜎low =𝑠 ★ if 𝑒′(𝑠★) is lower than the error of the window(0,𝜎 high) by more than𝜖, and
𝜎low=0(no lower bound) otherwise.
7:return(𝜎 low,𝜎 high)
few short runs.
G.3 Generalizing Scheduling Function to DDIS
We evaluate whether the scheduling function generalizes to DDIS, an output space optimization
method. It significantly improves the speed and also the accuracy of DDIS after only a short tuning
of the window[𝜎low,𝜎 high]. DDIS spends its budget on the Langevin steps with which it samples
Eq. (5) at each of its𝑁= 100noise levels. We allocate these steps with Eq. (29), using𝐾= 20steps
per noise level for the uniform budget of2,000steps, a floor of𝑘min= 2, and the same𝛽 and𝜏 as for
FunBCS. The floor differs from that of FunBCS only because DDIS takes fewer steps per noise level:
we keep the same fraction, one eighth of the steps of each noise level (10of𝐾= 80for FunBCS),
which gives𝑘min= 2for 𝐾= 20after rounding down. The edges are chosen with the same search
31

(algorithm 2), which takes under an hour per PDE on a single A100 GPU. On Poisson, Helmholtz
and Navier–Stokes it returns a one-sided low-noise window,(0, 0.335) on Poisson and Helmholtz
and(0, 0.144)onNavier–Stokes,identicaltooronegridstepfromthewindowofFunBCS.OnDarcy
it returns the window(0.144,∞).
Table2reportstheresultsonthe100testsamplesofTable1. Intheaccuracymode,thescheduler
lowers the error of DDIS by8%on average at unchanged cost, and on all four tasks. In the efficiency
mode, it makes DDIS1.3×faster on average while lowering its error by1%on average. On Darcy,
the window covers most noise levels of DDIS, so𝑀★ reaches the full budget and the two modes
coincide. The time falls by less than the number of steps because the probability-flow solve that
DDIS runs at every noise level does not depend on the budget.
Table 2: DDIS with and without the scheduling function on the100test samples of Table 1. The
uniform allocation is DDIS as in Table 1, with𝐾= 20Langevin steps on each of its𝑁= 100noise
levels. The accuracy mode redistributes the same2,000steps, and the efficiency mode cuts steps
while maintaining baseline accuracy. On Darcy,𝑀★ reaches the full budget, so the two modes
coincide. Errors are mean±standard deviation over the test samples.
Poisson Helmholtz Navier–Stokes Darcy
DDIS rel.ℓ 2 s/sample rel.ℓ 2 s/sample rel.ℓ 2 s/sample err. rate s/sample
uniform allocation 15.76±5.0818.0 15.47±4.3418.0 8.36±1.5518.0 7.48±3.8918.0
accuracy mode14.68±4.7118.0 13.95±4.0818.0 8.08±1.4818.0 6.64±3.6218.0
efficiency mode 15.56 ±5.0013.116.66±6.1013.18.28 ±1.5611.3 6.64±3.6218.0
H Navier–Stokes Spectral Analysis
Navier–Stokes is the only task where our two metrics disagree: our method improves relativeℓ2
over DDIS but worsens the spectral energy error𝐸𝑠 (Table 1). This section examines what drives
that gap.
The two metrics can disagree because𝐸𝑠 compares radially averaged power spectra, and is
therefore phase-blind. It measures whether a reconstruction carries the right amount of energy at
each spatial frequency, but not whether that energy sits in the right places. A reconstruction whose
high-frequency content is entirely unrelated to the ground truth can still score well on𝐸𝑠, as long
as its spectrum has roughly the right shape.
To tell these two cases apart, we take the 2D Fourier transform of the reconstruction and of the
ground truth, group the modes into radial bins by wavenumber𝑘, and compute a normalized inner
product between the two sets of coefficients in each bin,
𝒦(𝑘)=

˝ k∈𝑆𝑘 ˆ𝐴(k)𝐴(k)

 q˝
k∈𝑆𝑘|ˆ𝐴(k)|2
q˝
k∈𝑆𝑘|𝐴(k)|2
,(31)
where ˆ𝐴 and𝐴 are the Fourier coefficients of the reconstruction and the ground truth,(·) denotes
complex conjugation, and𝑆𝑘 collects every mode falling in radial bin𝑘, across all test instances.
This is a correlation coefficient computed in the Fourier domain, and Cauchy–Schwarz places it
in[0, 1]. It equals1when the reconstructed modes match the true modes in both amplitude and
phase,andfallstoward0whenthetwoareunrelated,nomatterhowmuchenergythereconstruction
places at that frequency.
32

10 4
10 3
10 2
10 1
100101102
tk
100
101
102
mean 2 error with a+
 FunBCS
DDIS
(a) Nullspace error toa+. FunBCS (orange) per-
forms significantly better than DDIS (blue).
10 4
10 3
10 2
10 1
100101102
tk
100
101
102
mean 2 error with a+
 FunBCS
DDIS
(b) Cumulative mean error toa+. FunBCS (orange)
performs significantly better than DDIS (blue).
Figure12: Wefindthatinnullspace(a)andoverall(b),FunBCS(orange)hassignificantlylesserror
on our discontinuous Poisson problem discussed in Sec. 3, as compared to DDIS (blue) validating
our theoretical results.
101
Wavenumber k
101
102
103
104
105
106
Radially averaged PSD
Poisson
101
Wavenumber k
101
102
103
104
105
106
Helmholtz
101
Wavenumber k
10 1
101
103
105
Navier Stokes
101
Wavenumber k
104
105
106
107
108
Darcy
Ground truth DDIS Ours
Figure 13: Radially averaged power spectral density of the Navier–Stokes reconstructions against
the ground truth, alongside three other PDEs. Above𝑘≈ 8, DDIS retains substantially more power
than our method and exceeds the ground-truth spectrum over part of this range, which is what
drives its lower𝐸𝑠 in Table 1.
We observe that in Fig. 13, at the crossover at𝑘≈ 8, DDIS retains considerably more power than
we do, and this is what produces its lower𝐸𝑠. However, the coherence of both methods is near zero
over exactly this range, so the extra power DDIS retains is not aligned with the true modes.
Comparing both curves against the ground truth sharpens this. Our reconstructions fall below
the true spectrum in this range, whereas DDIS rises above it over part of it, so DDIS is adding
high-frequency detail that the true field does not contain and that does not match the true modes.
Because this content is uncorrelated with the ground truth, it adds to the squared error rather than
reducingit,whichisconsistentwithourlowerrelative ℓ2,asshrinkingunrecoverablemodestoward
zero is the better choice under anℓ2 objective, even though it costs spectral realism. We therefore
report𝐸𝑠 alongside coherence, since on this benchmark a lower𝐸𝑠 reflects plausible but spurious
high-frequency texture rather than recovered structure.
I Additional Experiments
33

0 10 20 30 40 50 60
Wavenumber k
0.0
0.2
0.4
0.6
0.8
1.0Coherence with ground truth
Poisson
0 10 20 30 40 50 60
Wavenumber k
Helmholtz
0 10 20 30 40 50 60
Wavenumber k
Navier Stokes
0 10 20 30 40 50 60
Wavenumber k
Darcy
DDIS Ours
Figure 14: Per-wavenumber coherence with the ground truth on four PDEs. Beyond the same
𝑘≈ 8crossover, coherence is near zero forbothmethods, indicating that neither recovers the true
high-wavenumber modes. Together with Fig. 13, this suggests the𝐸𝑠 gap reflects prior-consistent
texture in unidentified modes rather than recovered information.
I.1 Visualizing Reconstructed Fields & Solutions
In this section we provide additional visualizations of the reconstructed coefficient fields, together
with the solution fields estimated from the same sparse observations, on Poisson and Helmholtz
(Fig. 16) and on Navier–Stokes and Darcy (Fig. 17).
I.2 Box Plots of Main Results
Figure 15 shows the distribution of the errors in Table 1 over the100test samples.
DiﬀusionPDE
FunDPS
DDIS
FunBCS (uniform)
FunBCS-EFFunBCS-AC
0
20
40rel. ℓ2 error (%)
Poisson
DiﬀusionPDE
FunDPS
DDIS
FunBCS (uniform)
FunBCS-EFFunBCS-AC
0
10
20
30rel. ℓ2 error (%)
Helmholtz
DiﬀusionPDE
FunDPS
DDIS
FunBCS (uniform)
FunBCS-EFFunBCS-AC
0
5
10
15rel. ℓ2 error (%)
Navier–Stokes
DiﬀusionPDE
FunDPS
DDIS
FunBCS (uniform)
FunBCS-EFFunBCS-AC
0
10
20error rate (%)
Darcy
Figure 15: Per-sample errors of the recovered coefficient field on the100test samples of Table 1:
relativeℓ2 error on Poisson, Helmholtz and Navier–Stokes, and pixel error rate on Darcy. Each box
spans the interquartile range, with the median as a line and the mean reported in Table 1 as a white
dot. Whiskers extend to1.5times the interquartile range, and samples beyond them are drawn
individually.
I.3 Study of Discontinuous Poisson’s Equation
In order to validate Prop. 3, and the distinction between DDIS and FunBCS more broadly, we
perform an experiment on discontinuous Poisson following our setting in Sec. 3 except we use
a neural operator surrogate; learned prior; compute¯a𝐷,𝑡𝑘−1 by averaging 100 samplesa(𝐷) 𝑡𝑘−1 . We considerΩ=(− 32, 32), and𝑧−=− 2,𝑧+= 2. Note that we do not configure an input optimization
34

scheduler, instead using 10 reverse sampling steps each with 30 input optimization steps. We
compute PkerA with respect to the finite difference approximationG. As expected, per Fig. 12a,
FunBCS obtains significantly less error than DDIS in nullspace; per Fig. 12b, FunBCS thus obtains
significantly less error overall.
J Connection with Preconditioned Output Space Optimization
As discussed in App. C, input optimization is equivalent to preconditioned output space opti-
mization. We discuss this further below. We consider the setting of Sec. 3. Firstly, we note that
outputspaceoptimizationfailsbecausetheunobservedcomponentofthemeasurementconsistency
gradient is 0:
Proposition 6.Letℒ(a):=
∥Aa−uobs∥2 2
2𝛾2 for a𝛾 >0. Then,
∇aℒ(a)= 1 𝛾2 A𝑇(Aa−u obs)(32)
and thus
PkerA∇aℒ(a)=0.(33)
Proof: See App. K.9.
Consequently, an output space optimization procedure which leverages the measurement con-
sistency gradient, unchanged, will not update the nullspace component. In particular, output space
optimization can be viewed in continuous time as computing∝⌈≀⊔⊣⌋⌋a=−∇ aℒ(a), and consequently
PkerA∝⌈≀⊔⊣⌋⌋a= 0. However, one can leverage apreconditionerto couple the observed and unobserved
components. Then, changing the observed component in output space by minimizing the measure-
ment consistency loss will also change the unobserved component. In particular, our approach as
outlined in Sec. 4 is equivalent to performing preconditioned output space optimization:
Proposition 7.Assume Ad≠ 0and PkerAd≠ 0. Fix diffusion time𝑡𝑘 and consider the exact denoiser
𝐷θ(·,𝑡 𝑘)=𝐷 ∗(·,𝑡 𝑘). Letv(𝑠) be defined per the gradient flow in Eq.(12). Leta(𝑠) :=𝐷∗(v(𝑠),𝑡 𝑘). Then,
we have that:
𝑑
𝑑𝑠 a(𝑠)=−𝑃(𝑣(𝑠),𝑡 𝑘)∇aℒ(a)|a=a(𝑠),(34)
where
P(v,𝑡 𝑘):=∇ v𝐷∗(v,𝑡 𝑘)∇v𝐷∗(v,𝑡 𝑘)⊤.(35)
Consequently,
PkerA
𝑑
𝑑𝑠 a(𝑠)≠0.(36)
Proof: See App. K.10.
Thus, optimizing over the input is equivalent to preconditioned output space optimization,
which can update the unobserved components. We note that the recent approach of [SRY26] also
incorporates a preconditioner, but does not motivate it rigorously and requires extra computation;
our approach is instead motivated from the perspective of PDE inverse problems and leverages the
diffusion denoiser.
35

0
 0.1
 0.2
0
 6
 12
0
 0.1
 0.2
0
 6
 12
Sparse Observation Ground Truth FunBCS (Ours) DDIS FunDPS DiﬀusionPDE
500 Points (3%)
Poisson
Coeﬃcient Field
Absolute Error
Error: 8.7% Error: 16.7% Error: 23.3% Error: 18.2%
Solution Field
Absolute Error (×10−5)
Error: 0.4% Error: 0.7% Error: 1.2% Error: 0.4%
500 Points (3%)
Helmholtz
Coeﬃcient Field
Absolute Error
Error: 8.5% Error: 18.6% Error: 15.9% Error: 17.9%
Solution Field
Absolute Error (×10−5)
Error: 0.6% Error: 0.8% Error: 0.6% Error: 0.7%
Figure 16: Reconstructions on one test sample of Poisson and of Helmholtz. For each PDE, the
upper block shows the coefficient field and the lower block the solution field estimated from the
same sparse observations, each with its absolute error to the ground truth underneath and its error
on that sample. Every method here was run with their published default test-time compute budget,
and FunBCS was run in efficiency mode, which is1.7×,1.4×, and26.4×faster than DDIS, FunDPS,
and DiffusionPDE, respectively. FunBCS and DDIS obtain the solution field by applying the neural
operator to their recovered coefficient field, whereas FunDPS and DiffusionPDE sample both fields
jointly. 36

0
 0.04
 0.08
0
 4
 8
0
 5
 10
0
 7.5
 15
Sparse Observation Ground Truth FunBCS (Ours) DDIS FunDPS DiﬀusionPDE
500 Points (3%)
Navier–Stokes
Coeﬃcient Field
Absolute Error
Error: 8.2% Error: 12.0% Error: 11.9% Error: 12.9%
Solution Field
Absolute Error (×10−3)
Error: 0.6% Error: 0.7% Error: 0.8% Error: 0.7%
500 Points (3%)
Darcy
Coeﬃcient Field
Absolute Error
Error: 2.6% Error: 17.4% Error: 7.1% Error: 17.1%
Solution Field
Absolute Error (×10−4)
Error: 0.5% Error: 4.0% Error: 1.2% Error: 6.4%
Figure 17: Reconstructions on one test sample of Navier–Stokes and of Darcy, arranged as in Fig. 16.
On Darcy, the error of the coefficient field is the pixel error rate.
37

K Proofs
Consider the setting of App. B. Fix diffusion times𝑡𝑘 >𝑡 𝑘−1 with 𝜎𝑡𝑘≥𝜎 𝑡0 > 0. Throughout, we
consider the setting of Sec. 3. In proofs,𝑘𝑡𝑘(·)denotes the function defined by𝑘𝑡𝑘(v) :=P(a 0=a+|
a𝑡𝑘 =v) , and𝑤(𝑠) :=𝑘 𝑡𝑘(v(𝑠)). Here,𝑘𝑡𝑘(a𝑡𝑘) means evaluation at the forward random vectora𝑡𝑘,
while𝑘𝑡𝑘(a(𝐷) 𝑡𝑘 ) and𝑘𝑡𝑘(a(𝐵) 𝑡𝑘 ) mean evaluation of this same function at the algorithmic states. We show this regular conditional probability is well-defined in Lemma 4.
K.1 Helpful Lemmas
Lemma 1(Conditional laws after renoising).The update in Eq.(6)satisfies
a(𝐷) 𝑡𝑘−1 |a(𝐷) 𝑡𝑘 ,u obs∼𝒩 '›
«
¯aD,𝑡𝑘−1,

A⊤A
𝛾2 + I 𝜎2 𝑡𝑘
!−1
+𝜎 2 𝑡𝑘−1 K“ﬁ
‹
,(37)
where¯aD,𝑡𝑘−1 is given by Lemma 2, and under the exact denoiser𝐷∗(·,𝑡 𝑘), the update in Eq.(13)satisfies:
a(𝐵) 𝑡𝑘−1 |a(𝐵) 𝑡𝑘 ,u obs∼𝒩(𝐷 ∗(v(𝑠),𝑡 𝑘),𝜎 2 𝑡𝑘−1 K).(38)
Proof.Conditional ona (𝐷) 𝑡𝑘 ,u obs, Lemma 2 gives
˜a0∼𝒩(¯a D,𝑡𝑘−1,𝚺 D,𝑡𝑘),ε (𝐷) 𝑘 ∼𝒩(0,K),˜a 0⊥⊥ε(𝐷) 𝑘 .(39)
Therefore
𝜎𝑡𝑘−1 ε(𝐷) 𝑘 ∼𝒩(0,𝜎 2 𝑡𝑘−1 K),˜a 0+𝜎 𝑡𝑘−1 ε(𝐷) 𝑘 ∼𝒩(¯a D,𝑡𝑘−1,𝚺 D,𝑡𝑘+𝜎 2 𝑡𝑘−1 K),(40)
proving Eq. (37).
For Eq. (38), Lemma 6 determinesv(𝑠) uniquely for fixeda(𝐵) 𝑡𝑘 ,u obs. Thus𝐷∗(v(𝑠),𝑡 𝑘)∈R 𝑛 is fixed under this conditioning, and
ε(𝐵) 𝑘 ∼𝒩(0,K)=⇒𝐷 ∗(v(𝑠),𝑡 𝑘)+𝜎 𝑡𝑘−1 ε(𝐵) 𝑘 ∼𝒩(𝐷 ∗(v(𝑠),𝑡 𝑘),𝜎 2 𝑡𝑘−1 K).(41)
This proves Lemma 1.□
Lemma2(DDISmeanandcovariance).ThedensityinEq.(5),given 𝒜ℎ =A ,isthatof 𝒩(¯aD,𝑡𝑘−1,𝚺 D,𝑡𝑘),
where
¯aD,𝑡𝑘−1 =

A⊤A
𝛾2 + I 𝜎2 𝑡𝑘
!−1
'›
«
A⊤uobs
𝛾2 +
𝐷θ(a(𝐷) 𝑡𝑘 ,𝑡 𝑘)
𝜎2 𝑡𝑘
“ﬁ
‹
(42)
and
𝚺D,𝑡𝑘 :=

A⊤A
𝛾2 + I 𝜎2 𝑡𝑘
!−1
.(43)
Proof. Fix𝑡𝑘 > 0, a(𝐷) 𝑡𝑘 ∈R 𝑛, anduobs∈R 𝑚. Throughout the proof,a0∈R 𝑛 is the variable in the density. DDIS approximates the denoising conditional density by
𝑞𝐷(a0|a(𝐷) 𝑡𝑘 )= 1 (2𝜋𝜎2 𝑡𝑘 )𝑛/2 exp
 
 −
∥a0−𝐷 θ(a(𝐷) 𝑡𝑘 ,𝑡 𝑘)∥2
2𝜎2 𝑡𝑘
 
 .(44)
38

The observation likelihood is
𝑝(uobs|a 0)= 1 (2𝜋𝛾2)𝑚/2 exp

−∥Aa0−u obs∥2
2𝛾2

.(45)
DDIS defines the following density
𝑞𝐷,𝑡𝑘(a0|a(𝐷) 𝑡𝑘 ,u obs):= 𝑝(uobs|a 0)𝑞 𝐷(a0|a(𝐷) 𝑡𝑘 ) ∫
R𝑛
𝑝(uobs|x)𝑞 𝐷(x|a (𝐷) 𝑡𝑘 )𝑑x
.(46)
The denominator is strictly positive because its integrand is everywhere positive. It is finite because
𝑝(uobs|x)≤(2𝜋𝛾 2)−𝑚/2 and𝑞 𝐷(·|a (𝐷) 𝑡𝑘 )integrates to one. Thus Eq. (46) is well-defined. Substituting Eqs. (44) and (45) into Eq. (46) gives
𝑞𝐷,𝑡𝑘(a0|a(𝐷) 𝑡𝑘 ,u obs)=
exp

−∥Aa0−uobs∥2 2𝛾2 − ∥a0−𝐷θ(a(𝐷) 𝑡𝑘 ,𝑡𝑘)∥2 2𝜎2 𝑡𝑘 
(2𝜋𝛾2)𝑚/2(2𝜋𝜎2 𝑡𝑘 )𝑛/2
∫
R𝑛 exp

−∥Ax−uobs∥2 2𝛾2 − ∥x−𝐷θ(a(𝐷) 𝑡𝑘 ,𝑡𝑘)∥2 2𝜎2 𝑡𝑘  𝑑x
(2𝜋𝛾2)𝑚/2(2𝜋𝜎2 𝑡𝑘 )𝑛/2
.(47)
We next complete the square in the exponent. The matrixA⊤A/𝛾2+I/𝜎 2 𝑡𝑘 is symmetric, and for every nonzerox∈R 𝑛,
x⊤

A⊤A
𝛾2 + I 𝜎2 𝑡𝑘
!
x= ∥Ax∥2
𝛾2 +∥x∥2 𝜎2 𝑡𝑘 >0.(48)
Hence it is positive definite and invertible, so𝚺D,𝑡𝑘 in Lemma 2 is well-defined and positive definite.
By definition, we have
𝚺−1 D,𝑡𝑘 ¯aD,𝑡𝑘−1 = A⊤uobs 𝛾2 + 𝐷θ(a(𝐷) 𝑡𝑘 ,𝑡 𝑘) 𝜎2 𝑡𝑘 .(49)
39

Expanding the two squared norms and using Eq. (49) yields
∥Aa0−u obs∥2
2𝛾2 +
∥a0−𝐷 θ(a(𝐷) 𝑡𝑘 ,𝑡 𝑘)∥2
2𝜎2 𝑡𝑘
= 1 2𝛾2(Aa0−u obs)⊤(Aa0−u obs)
+ 1
2𝜎2 𝑡𝑘
(a0−𝐷 θ(a(𝐷) 𝑡𝑘 ,𝑡 𝑘))⊤(a0−𝐷 θ(a(𝐷) 𝑡𝑘 ,𝑡 𝑘))
= 1 2𝛾2  a⊤ 0 A⊤Aa0−2a⊤ 0 A⊤uobs+∥u obs∥2
+ 1
2𝜎2 𝑡𝑘

a⊤ 0 a0−2a⊤ 0𝐷θ(a(𝐷) 𝑡𝑘 ,𝑡 𝑘)+∥𝐷 θ(a(𝐷) 𝑡𝑘 ,𝑡 𝑘)∥2

= 1 2 a⊤ 0

A⊤A
𝛾2 + I 𝜎2 𝑡𝑘
!
a0
−a⊤ 0 '›
«
A⊤uobs
𝛾2 +
𝐷θ(a(𝐷) 𝑡𝑘 ,𝑡 𝑘)
𝜎2 𝑡𝑘
“ﬁ
‹
+∥uobs∥2
2𝛾2 +
∥𝐷θ(a(𝐷) 𝑡𝑘 ,𝑡 𝑘)∥2
2𝜎2 𝑡𝑘
= 1 2 a⊤ 0 𝚺−1 D,𝑡𝑘 a0−a⊤ 0 '›
«
A⊤uobs
𝛾2 +
𝐷θ(a(𝐷) 𝑡𝑘 ,𝑡 𝑘)
𝜎2 𝑡𝑘
“ﬁ
‹
+∥uobs∥2
2𝛾2 +
∥𝐷θ(a(𝐷) 𝑡𝑘 ,𝑡 𝑘)∥2
2𝜎2 𝑡𝑘
= 1 2 a⊤ 0 𝚺−1 D,𝑡𝑘 a0−a⊤ 0 𝚺−1 D,𝑡𝑘 ¯aD,𝑡𝑘−1+∥uobs∥2 2𝛾2 + ∥𝐷θ(a(𝐷) 𝑡𝑘 ,𝑡 𝑘)∥2 2𝜎2 𝑡𝑘 .
(50)
Symmetry of𝚺−1 D,𝑡𝑘 gives
1
2(a0−¯aD,𝑡𝑘−1)⊤𝚺−1 D,𝑡𝑘 (a0−¯aD,𝑡𝑘−1)
= 1 2(a⊤ 0−¯a⊤ D,𝑡𝑘−1 )𝚺−1 D,𝑡𝑘 (a0−¯aD,𝑡𝑘−1)
= 1 2  a⊤ 0 𝚺−1 D,𝑡𝑘 a0−a⊤ 0 𝚺−1 D,𝑡𝑘 ¯aD,𝑡𝑘−1−¯a⊤ D,𝑡𝑘−1 𝚺−1 D,𝑡𝑘 a0+¯a⊤ D,𝑡𝑘−1 𝚺−1 D,𝑡𝑘 ¯aD,𝑡𝑘−1 
= 1 2  a⊤ 0 𝚺−1 D,𝑡𝑘 a0−2a⊤ 0 𝚺−1 D,𝑡𝑘 ¯aD,𝑡𝑘−1+¯a⊤ D,𝑡𝑘−1 𝚺−1 D,𝑡𝑘 ¯aD,𝑡𝑘−1 
= 1 2 a⊤ 0 𝚺−1 D,𝑡𝑘 a0−a⊤ 0 𝚺−1 D,𝑡𝑘 ¯aD,𝑡𝑘−1+ 1 2¯a⊤ D,𝑡𝑘−1 𝚺−1 D,𝑡𝑘 ¯aD,𝑡𝑘−1.
(51)
Define
𝑐D,𝑡𝑘 :=∥uobs∥2 2𝛾2 + ∥𝐷θ(a(𝐷) 𝑡𝑘 ,𝑡 𝑘)∥2 2𝜎2 𝑡𝑘 − 1 2¯a⊤ D,𝑡𝑘−1 𝚺−1 D,𝑡𝑘 ¯aD,𝑡𝑘−1.(52)
Incorporating Eq. (51) into Eq. (50) yields
∥Aa0−u obs∥2
2𝛾2 +
∥a0−𝐷 θ(a(𝐷) 𝑡𝑘 ,𝑡 𝑘)∥2
2𝜎2 𝑡𝑘
= 1 2(a0−¯aD,𝑡𝑘−1)⊤𝚺−1 D,𝑡𝑘 (a0−¯aD,𝑡𝑘−1)+𝑐 D,𝑡𝑘.(53)
40

The scalar𝑐D,𝑡𝑘 is independent ofa0. Since Eq. (53) holds for everya0∈R 𝑛, it also holds with the
integration variablexin place ofa0, with the same scalar𝑐D,𝑡𝑘. Consequently, Eq. (47) becomes
𝑞𝐷,𝑡𝑘(a0|a(𝐷) 𝑡𝑘 ,u obs)= 𝑒−𝑐D,𝑡𝑘 exp n − 1 2(a0−¯aD,𝑡𝑘−1)⊤𝚺−1 D,𝑡𝑘 (a0−¯aD,𝑡𝑘−1) o
𝑒−𝑐D,𝑡𝑘
∫
R𝑛
exp

− 1 2(x−¯a D,𝑡𝑘−1)⊤𝚺−1 D,𝑡𝑘 (x−¯a D,𝑡𝑘−1)

𝑑x
=
exp
n
− 1 2(a0−¯aD,𝑡𝑘−1)⊤𝚺−1 D,𝑡𝑘 (a0−¯aD,𝑡𝑘−1) o ∫
R𝑛
exp

− 1 2(x−¯a D,𝑡𝑘−1)⊤𝚺−1 D,𝑡𝑘 (x−¯a D,𝑡𝑘−1)

𝑑x
.
(54)
Toevaluatetheremainingintegral,thespectraltheoremprovidesthesymmetricpositivedefinite
square root𝚺1/2 D,𝑡𝑘 . Definez=𝚺 − 1 2(x−¯a𝐷,𝑡𝑘−1), i.e.,x=¯a𝐷,𝑡𝑘−1+𝚺 1 2 z. The mapz↦→¯a D,𝑡𝑘−1+𝚺 1/2 D,𝑡𝑘 z isacontinuouslydifferentiablebijectionof R𝑛 withcontinuouslydifferentiableinverseandJacobian
determinant(det𝚺 D,𝑡𝑘)1/2 >0. The change of variables theorem therefore gives
∫
R𝑛
exp

− 1 2(x−¯a D,𝑡𝑘−1)⊤𝚺−1 D,𝑡𝑘 (x−¯a D,𝑡𝑘−1)

𝑑x
=(det𝚺 D,𝑡𝑘)1/2
∫
R𝑛
𝑒−∥z∥2/2𝑑z
=(det𝚺 D,𝑡𝑘)1/2(2𝜋)𝑛/2,
(55)
byTonelli’stheoremandtheGaussianintegral
∫
R𝑒−𝑟 2/2𝑑𝑟= √ 2𝜋. SubstitutingEq.(55)intoEq.(54)
yields
𝑞𝐷,𝑡𝑘(a0|a(𝐷) 𝑡𝑘 ,u obs)= exp
n
− 1 2(a0−¯aD,𝑡𝑘−1)⊤𝚺−1 D,𝑡𝑘 (a0−¯aD,𝑡𝑘−1) o
(2𝜋)𝑛/2(det𝚺 D,𝑡𝑘)1/2 .(56)
This is exactly the density of𝒩(¯aD,𝑡𝑘−1,𝚺 D,𝑡𝑘), as desired.
□
Lemma 3(Orthogonal projection ontokerA).For everyu∈R 𝑚 anda∈R 𝑛,
PkerA(A⊤u)=0,∥P kerA a∥2≤∥a∥ 2.(57)
Proof.For everyu∈R 𝑚 andz∈kerA,
⟨A⊤u,z⟩=⟨u,Az⟩=0.(58)
ThusA⊤u∈(kerA) ⊥, soPkerA(A⊤u)=0.
For everya∈R 𝑛, the vectorsPkerA a and a−P kerA a are orthogonal witha=P kerA a+(I−
PkerA)a. Hence
∥a∥2 2=∥P kerA a∥2 2+∥a−P kerA a∥2 2≥∥P kerA a∥2 2,(59)
which gives∥PkerA a∥2≤∥a∥ 2 as desired.□
Lemma 4(Exact denoiser under𝜋0).For everyv∈R 𝑛,
𝐷∗(v,𝑡 𝑘)=a −+P(a 0=a+|a 𝑡𝑘 =v)(a+−a−),(60)
41

where
P(a0=a+|a 𝑡𝑘 =v)=

1+exp
(
−(a+−a−)⊤K−1(v−(a −+a+)/2)
𝜎2 𝑡𝑘
)!−1
(61)
is well-defined.
Proof.Forv∈R 𝑛, by definition of the diffusion forward process, we have that
𝑝(a𝑡𝑘 =v|a 0=a±)=
exp{−(v−a ±)⊤K−1(v−a ±)/(2𝜎2 𝑡𝑘 )}
(2𝜋)𝑛/2𝜎𝑛 𝑡𝑘 (detK) 1/2 >0.(62)
By the law of total probability,
𝑝(a𝑡𝑘 =v)= 1 2𝑝(a𝑡𝑘 =v|a 0=a−)+ 1 2𝑝(a𝑡𝑘 =v|a 0=a+)>0.(63)
Define
𝑘𝑡𝑘(v):=
1
2𝑝(a𝑡𝑘 =v|a 0=a+)
𝑝(a𝑡𝑘 =v) .(64)
This function is Borel measurable and takes values in(0, 1). Thus𝑘𝑡𝑘(a𝑡𝑘) is integrable and𝜎(a𝑡𝑘)-
measurable. For every Borel set𝐵⊆R𝑛,
E[𝑘𝑡𝑘(a𝑡𝑘)1{a𝑡𝑘∈𝐵}]=
∫
𝐵
𝑘𝑡𝑘(v)𝑝(a𝑡𝑘 =v)𝑑v
= 1 2 ∫ 𝐵 𝑝(a𝑡𝑘 =v|a 0=a+)𝑑v
=P(a 0=a+)P(a𝑡𝑘∈𝐵|a 0=a+)
=P(a 0=a+,a𝑡𝑘∈𝐵)
=E[1{a0=a+}1{a𝑡𝑘∈𝐵}].
(65)
Since the events{a𝑡𝑘∈𝐵} form 𝜎(a𝑡𝑘), by the definition of conditional expectation this verifies
𝑘𝑡𝑘(a𝑡𝑘)=E[ 1{a0=a+}|𝜎(a 𝑡𝑘)]=P(a 0 =a +|𝜎(a 𝑡𝑘)) almost surely. Define𝑄(·,·) by𝑄(v,𝐶)=
𝑘𝑡𝑘(v)1{a+∈𝐶}+( 1−𝑘 𝑡𝑘(v))1{a−∈𝐶} for v∈R 𝑛 and Borel set𝐶⊂R 𝑛. For every fixedv, the map
𝐶↦→𝑄(v,𝐶) is a probability measure onR𝑛, and for every Borel set𝐶⊂R 𝑛, the mapv↦→𝑄(v,𝐶)
is Borel measurable. Moreover, sincea0 takes values only in{a+,a−},
E[1{a0∈𝐶}|𝜎(a 𝑡𝑘)]=1 {a+∈𝐶}E[1{a0=a+}|𝜎(a 𝑡𝑘)]
+1{a−∈𝐶}E[1{a0=a−}|𝜎(a 𝑡𝑘)]
=1{a+∈𝐶}𝑘𝑡𝑘(a𝑡𝑘)+1 {a−∈𝐶}(1−𝑘 𝑡𝑘(a𝑡𝑘))
=𝑄(a 𝑡𝑘,𝐶)
almostsurely,since 1{a0=a−}= 1−1{a0=a+}. Hence𝑄 isaregularconditionaldistributionof a0 given
a𝑡𝑘. In particular,P(a0=a+|a 𝑡𝑘 =v):=𝑄(v,{a +})=𝑘 𝑡𝑘(v)is well-defined for everyv∈R 𝑛.
Incorporating Eqs. (62) and (63) into Eq. (64) yields
𝑘𝑡𝑘(v)=

1+ 𝑝(a𝑡𝑘 =v|a 0=a−) 𝑝(a𝑡𝑘 =v|a 0=a+) −1
=

1+exp
(
(v−a +)⊤K−1(v−a +)−(v−a −)⊤K−1(v−a −)
2𝜎2 𝑡𝑘
)!−1
.
(66)
42

By symmetry ofK−1,
(v−a +)⊤K−1(v−a +)−(v−a −)⊤K−1(v−a −)
=

v⊤K−1v−v ⊤K−1a+−a⊤ + K−1v+a ⊤ + K−1a+ 
−

v⊤K−1v−v ⊤K−1a−−a⊤ − K−1v+a ⊤ − K−1a− 
=−2v⊤K−1a++2v⊤K−1a−+a⊤ + K−1a+−a⊤ − K−1a−
=−2v⊤K−1(a+−a−)+a ⊤ + K−1a+−a⊤ − K−1a−
=−2v⊤K−1(a+−a−)+(a +−a−)⊤K−1(a++a−)
=−2(a+−a−)⊤K−1v+(a +−a−)⊤K−1(a++a−)
=−2(a+−a−)⊤K−1

v− a−+a+
2

,
(67)
proving Eq. (61).
Finally, sincea0 takes only the valuesa−,a+,
𝐷∗(v,𝑡 𝑘)=E[a 0|a 𝑡𝑘 =v]
=(1−𝑘 𝑡𝑘(v))a−+𝑘 𝑡𝑘(v)a+
=a−+𝑘 𝑡𝑘(v)(a+−a−).
(68)
Substitute𝑘 𝑡𝑘(v)=P(a 0=a+|a 𝑡𝑘 =v)to obtain Lemma 4 as desired.□
Lemma 5(Strict positivity of the conditional weights).For everyv∈R𝑛,
0<P(a 0=a+|a 𝑡𝑘 =v)<1,0<P(a 0=a−|a 𝑡𝑘 =v)<1.(69)
Proof. By Eq. (62), both conditional densities𝑝(a𝑡𝑘 =v|a 0 =a+) and𝑝(a𝑡𝑘 =v|a 0 =a−) are
strictly positive. Thus
0< 𝑝(a𝑡𝑘 =v|a 0=a±) 𝑝(a𝑡𝑘 =v|a 0=a+)+𝑝(a 𝑡𝑘 =v|a 0=a−) <1.(70)
By Eqs. (63) and (64), these ratios are the two conditional probabilities, yielding Eq. (69) as
desired. □
Lemma 6(Global existence and uniqueness of the gradient flow).For any current statea(𝐵) 𝑡𝑘 ∈R 𝑛,
with the exact denoiser𝐷θ(·,·)=𝐷 ∗(·,·), the gradient flow in Eq.(12), initialized byv(0)=a (𝐵) 𝑡𝑘 , has a solutionv(𝑠)that exists and is unique for all𝑠≥0.
Proof.Throughout, set
b:= K−1(a+−a−)
𝜎2 𝑡𝑘
, 𝑐:=
∥A(a+−a−)∥2 2
𝛾2 , ℓ 𝑡𝑘(v):=b ⊤

v− a−+a+
2

.(71)
By Lemma 4,
𝑘𝑡𝑘(v)=

1+𝑒 −ℓ𝑡𝑘(v)
−1
.(72)
43

Since∇ vℓ𝑡𝑘(v)=b, differentiation gives
∇v𝑘𝑡𝑘(v)=−

1+𝑒 −ℓ𝑡𝑘(v)
−2 
−𝑒−ℓ𝑡𝑘(v)b 
= 𝑒−ℓ𝑡𝑘(v) 
1+𝑒 −ℓ𝑡𝑘(v)
 2 b.
Moreover,
𝑘𝑡𝑘(v)= 1 1+𝑒 −ℓ𝑡𝑘(v),1−𝑘 𝑡𝑘(v)= 𝑒−ℓ𝑡𝑘(v) 1+𝑒 −ℓ𝑡𝑘(v).(73)
Therefore,
∇v𝑘𝑡𝑘(v)=𝑘 𝑡𝑘(v)

1−𝑘 𝑡𝑘(v)

b.(74)
Usingu obs=Aa+ and Lemma 4,
A𝐷∗(v,𝑡 𝑘)−u obs=Aa−+𝑘 𝑡𝑘(v)A(a+−a−)−Aa +
=−(1−𝑘 𝑡𝑘(v))A(a+−a−). (75)
Hence the measurement objective is
𝐽𝑡𝑘(v):=
∥A𝐷∗(v,𝑡 𝑘)−u obs∥2 2
2𝛾2 = 𝑐 2  1−𝑘 𝑡𝑘(v)  2.(76)
The chain rule and Eq. (74) yield
∇v𝐽𝑡𝑘(v)= 𝑐 2 2  1−𝑘 𝑡𝑘(v)  −∇v𝑘𝑡𝑘(v) 
=−𝑐𝑘 𝑡𝑘(v)

1−𝑘 𝑡𝑘(v)
 2b.(77)
Substituting the definitions ofband𝑐intov ′(𝑠)=−∇𝐽 𝑡𝑘(v(𝑠))gives
v′(𝑠)= ∥A(a+−a−)∥2 2
𝛾2𝜎2 𝑡𝑘
P a0=a+|a 𝑡𝑘 =v(𝑠) 
×P  a0=a−|a 𝑡𝑘 =v(𝑠)  2K−1(a+−a−),
v(0)=a (𝐵) 𝑡𝑘 .
(78)
It remains to show that the vector field−∇𝐽𝑡𝑘 is globally Lipschitz. To compute the Hessian, fix
𝑖,𝑗∈{1,...,𝑛}. By Eq. (77),
𝜕𝐽𝑡𝑘
𝜕𝑣𝑖
(v)=−𝑐𝑏 𝑖𝑘𝑡𝑘(v)

1−𝑘 𝑡𝑘(v)
 2.(79)
Since𝑏 𝑖 and𝑐are constant with respect tov, the product rule gives
𝜕
𝜕𝑣𝑗
𝜕𝐽𝑡𝑘
𝜕𝑣𝑖
(v)=−𝑐𝑏 𝑖
𝜕
𝜕𝑣𝑗
h
𝑘𝑡𝑘(v)

1−𝑘 𝑡𝑘(v)
 2i
=−𝑐𝑏 𝑖
𝜕𝑘𝑡𝑘
𝜕𝑣𝑗
(v)

1−𝑘 𝑡𝑘(v)
 2+𝑘 𝑡𝑘(v) 𝜕 𝜕𝑣𝑗  1−𝑘 𝑡𝑘(v)  2

.
44

By the chain rule,
𝜕
𝜕𝑣𝑗

1−𝑘 𝑡𝑘(v)
 2=−2  1−𝑘 𝑡𝑘(v) 𝜕𝑘𝑡𝑘 𝜕𝑣𝑗 (v).(80)
Substituting this identity gives
𝜕
𝜕𝑣𝑗
𝜕𝐽𝑡𝑘
𝜕𝑣𝑖
(v)=−𝑐𝑏 𝑖
h
1−𝑘 𝑡𝑘(v)
 2−2𝑘 𝑡𝑘(v)  1−𝑘 𝑡𝑘(v) i 𝜕𝑘𝑡𝑘 𝜕𝑣𝑗 (v)
=−𝑐𝑏 𝑖

1−𝑘 𝑡𝑘(v)

1−3𝑘 𝑡𝑘(v)
𝜕𝑘𝑡𝑘
𝜕𝑣𝑗
(v).
By Eq. (74),
𝜕𝑘𝑡𝑘
𝜕𝑣𝑗
(v)=𝑘 𝑡𝑘(v)

1−𝑘 𝑡𝑘(v)

𝑏𝑗.(81)
Therefore,
𝜕
𝜕𝑣𝑗
𝜕𝐽𝑡𝑘
𝜕𝑣𝑖
(v)=−𝑐𝑏 𝑖

1−𝑘 𝑡𝑘(v)

1−3𝑘 𝑡𝑘(v)

𝑘𝑡𝑘(v)

1−𝑘 𝑡𝑘(v)

𝑏𝑗
=−𝑐𝑘 𝑡𝑘(v)

1−𝑘 𝑡𝑘(v)
 2 1−3𝑘 𝑡𝑘(v)  𝑏𝑖𝑏𝑗.
Since(bb⊤)𝑖𝑗 =𝑏 𝑖𝑏𝑗, we obtain
∇2 v𝐽𝑡𝑘(v)=−𝑐𝑘 𝑡𝑘(v)  1−𝑘 𝑡𝑘(v)  2 1−3𝑘 𝑡𝑘(v)  bb⊤.(82)
By Lemma 5,0<𝑘 𝑡𝑘(v)<1. Hence
𝑘𝑡𝑘(v)≤1,

1−𝑘 𝑡𝑘(v)
 2≤1,

1−3𝑘 𝑡𝑘(v)

≤2.(83)
We also have
∥bb⊤∥op≤∥b∥ 2 2,(84)
since for everyx∈R 𝑛 with∥x∥ 2=1, Cauchy–Schwarz gives
∥bb⊤x∥2=∥b∥ 2|b⊤x|
≤∥b∥ 2 2∥x∥2=∥b∥ 2 2.
Thus, using Eq. (82),
∥∇2 v𝐽𝑡𝑘(v)∥op≤2𝑐∥b∥ 2 2
=
2∥A(a+−a−)∥2 2∥K−1(a+−a−)∥2 2
𝛾2𝜎4 𝑡𝑘
=:𝐿 𝑡𝑘 <∞(85)
for everyv∈R 𝑛.
Now letx,y∈R 𝑛 and define
g(𝑟):=∇𝐽 𝑡𝑘

y+𝑟(x−y)

, 𝑟∈[0,1].(86)
Since𝐽 𝑡𝑘 is twice continuously differentiable, the chain rule gives
g′(𝑟)=∇ 2𝐽𝑡𝑘  y+𝑟(x−y)  (x−y).(87)
45

The fundamental theorem of calculus therefore gives
∇𝐽𝑡𝑘(x)−∇𝐽 𝑡𝑘(y)=g(1)−g(0)
=
∫ 1
0
∇2𝐽𝑡𝑘  y+𝑟(x−y)  (x−y)𝑑𝑟.
Taking norms and applying Eq. (85),
∥∇𝐽𝑡𝑘(x)−∇𝐽 𝑡𝑘(y)∥2≤
∫ 1
0
∇2𝐽𝑡𝑘  y+𝑟(x−y)  op∥x−y∥ 2𝑑𝑟
≤
∫ 1
0
𝐿𝑡𝑘∥x−y∥ 2𝑑𝑟
=𝐿 𝑡𝑘∥x−y∥ 2.(88)
Thus−∇𝐽𝑡𝑘 is globally Lipschitz onR𝑛. Consequently, the global Picard–Lindelöf theorem gives a
unique solution to Eq. (12), as desired.
□
Lemma7(Evolutionoftheconditionalprobabilityunderthegradientflow).Suppose A(a+−a−)≠ 0.
For the solution of the gradient flow in Eq.(12)initialized byv(0)=a (𝐵) 𝑡𝑘 , v(𝑠), let𝑤(𝑠) :=𝑘 𝑡𝑘(v(𝑠)). Then,
𝑑
𝑑𝑠𝑤(𝑠)= ∥A(a+−a−)∥2∥K−1(a+−a−)∥2 𝛾2𝜎4 𝑡𝑘 𝑤(𝑠) 2(1−𝑤(𝑠)) 3.(89)
Proof. The solutionv(𝑠) exists and is unique by Lemma 6. Withb,𝑐 as in Eq. (71), Eq. (77) and the
definition of gradient flow give
v′(𝑠)=−∇𝐽 𝑡𝑘(v(𝑠))=𝑐𝑤(𝑠)(1−𝑤(𝑠)) 2b.(90)
Since𝑘 𝑡𝑘(·)andv(·)are continuously differentiable, the chain rule and Eq. (74) give
𝑤′(𝑠)=∇ v𝑘𝑡𝑘(v(𝑠))⊤v′(𝑠)
=[𝑤(𝑠)(1−𝑤(𝑠))b] ⊤[𝑐𝑤(𝑠)(1−𝑤(𝑠)) 2b]
=𝑐∥b∥ 2𝑤(𝑠) 2(1−𝑤(𝑠)) 3.
(91)
Substituting the definitions ofb,𝑐gives
𝑤′(𝑠)=𝐶𝑤(𝑠) 2(1−𝑤(𝑠)) 3, 𝐶:= ∥A(a+−a−)∥2∥K−1(a+−a−)∥2
𝛾2𝜎4 𝑡𝑘
.(92)
The constant is positive becauseA(a+−a−)≠0 , K is invertible, and𝛾,𝜎 𝑡𝑘 > 0; this yields Eq. (89)
as desired. □
Lemma 8(Convergence of the conditional probability and denoiser).SupposeA(a+−a−)≠ 0.
Along the gradient flow in Eq.(12), initialized byv(0)=a(𝐵) 𝑡𝑘 , as𝑠→∞,
P(a0=a+|a 𝑡𝑘 =v(𝑠))−→1,P(a 0=a−|a 𝑡𝑘 =v(𝑠))−→0,(93)
and
𝐷∗(v(𝑠),𝑡 𝑘)−→a +.(94)
46

Proof. Set𝑤(𝑠) :=𝑘 𝑡𝑘(v(𝑠)) andtake 𝐶 fromEq.(92). Notethat v(𝑠) existsandisuniquebyLemma6.
By Lemmas 5 and 7,0<𝑤(𝑠)< 1and 𝑤′(𝑠)> 0for every finite𝑠. Thus𝑤(·) is increasing and
bounded above, so its limit𝐿 exists and satisfies0<𝑤( 0)≤𝐿≤ 1. Suppose𝐿< 1. By continuity of
the polynomial in Eq. (92),
𝑤′(𝑠)−→𝐶𝐿 2(1−𝐿) 3=:𝑐 0 >0.(95)
Hence there is𝑆≥ 0such that𝑤′(𝑠)≥𝑐 0/2for all𝑠≥𝑆 . The fundamental theorem of calculus then
gives
𝑤(𝑠)−𝑤(𝑆)=
∫ 𝑠
𝑆
𝑤′(𝑟)𝑑𝑟≥ 𝑐0
2(𝑠−𝑆), 𝑠≥𝑆.(96)
The right-hand side grows without bound as𝑠→∞ , contradicting𝐿< 1. Therefore𝐿= 1, which
also gives1−𝑤(𝑠)→0.
Finally, by Lemma 4,
𝐷∗(v(𝑠),𝑡 𝑘)−a +=a−+𝑤(𝑠)(a+−a−)−a +
=−(1−𝑤(𝑠))(a +−a−),
∥𝐷∗(v(𝑠),𝑡 𝑘)−a +∥=(1−𝑤(𝑠))∥a +−a−∥−→0,
(97)
because1−𝑤(𝑠)→0, as desired.□
Lemma 9(DDIS preserves the denoiser’s kernel component in expectation).Fix𝑡𝑘 >𝑡 𝑘−1 and any
current statea(𝐷) 𝑡𝑘 ∈R 𝑛. The DDIS conditional mean¯aD,𝑡𝑘−1 :=E[a(𝐷) 𝑡𝑘−1 |a(𝐷) 𝑡𝑘 ,u obs]from Lemma 1 satisfies
PkerA¯aD,𝑡𝑘−1 =P kerA𝐷θ(a(𝐷) 𝑡𝑘 ,𝑡 𝑘).(98)
Proof.By Lemma 2,
¯aD,𝑡𝑘−1 =

A⊤A
𝛾2 + I 𝜎2 𝑡𝑘
!−1
'›
«
A⊤uobs
𝛾2 +
𝐷θ(a(𝐷) 𝑡𝑘 ,𝑡 𝑘)
𝜎2 𝑡𝑘
“ﬁ
‹
.(99)
Multiplying by the invertible matrixA⊤A/𝛾2+I/𝜎 2 𝑡𝑘 gives
A⊤A¯aD,𝑡𝑘−1
𝛾2 +¯aD,𝑡𝑘−1 𝜎2 𝑡𝑘 = A⊤uobs 𝛾2 + 𝐷θ(a(𝐷) 𝑡𝑘 ,𝑡 𝑘) 𝜎2 𝑡𝑘 .(100)
Move both terms on the right to the left and factor:
0= A⊤A¯aD,𝑡𝑘−1−A⊤uobs
𝛾2 +
¯aD,𝑡𝑘−1−𝐷 θ(a(𝐷) 𝑡𝑘 ,𝑡 𝑘)
𝜎2 𝑡𝑘
= A⊤(A¯aD,𝑡𝑘−1−u obs) 𝛾2 + ¯aD,𝑡𝑘−1−𝐷 θ(a(𝐷) 𝑡𝑘 ,𝑡 𝑘) 𝜎2 𝑡𝑘 . (101)
Apply the linear mapPkerA. By Lemma 3,PkerA A⊤u=0 for everyu∈R 𝑚, in particular for
u=A¯a D,𝑡𝑘−1−u obs. Consequently,
0= PkerA A⊤(A¯aD,𝑡𝑘−1−u obs) 𝛾2 + PkerA¯aD,𝑡𝑘−1−P kerA𝐷θ(a(𝐷) 𝑡𝑘 ,𝑡 𝑘) 𝜎2 𝑡𝑘
=
PkerA¯aD,𝑡𝑘−1−P kerA𝐷θ(a(𝐷) 𝑡𝑘 ,𝑡 𝑘)
𝜎2 𝑡𝑘
.
(102)
47

Since𝜎 2 𝑡𝑘 >0, we have thatPkerA¯aD,𝑡𝑘−1 =P kerA𝐷θ(a(𝐷) 𝑡𝑘 ,𝑡 𝑘)as desired.□
K.2 Proof of Proposition 1
Proof.By Lemma 9, with𝐷θ(·,𝑡 𝑘)=𝐷 ∗(·,𝑡 𝑘), and linearity ofPkerA,
PkerA(¯aD,𝑡𝑘−1−a+)=P kerA¯aD,𝑡𝑘−1−P kerA a+ (103)
=P kerA𝐷∗(a(𝐷) 𝑡𝑘 ,𝑡 𝑘)−P kerA a+ (104)
=P kerA

𝐷∗(a(𝐷) 𝑡𝑘 ,𝑡 𝑘)−a +

.(105)
Taking norms on both sides proves the claim. The same argument also applies when𝑡𝑘−1 =𝑡 0. □
K.3 Proof of Proposition 2
Proof.Let
d:=a +−a−.(106)
By Lemma 4,𝑘𝑡𝑘(·) is a regular conditional probabilityP(a0=a+|a 𝑡𝑘 =·) and is well-defined, and
𝐷∗(v,𝑡 𝑘)=a −+𝑘 𝑡𝑘(v)d.(107)
The orthogonal decomposition ofdwith respect tokerAis
d=P (kerA)⊥d+P kerA d.(108)
Substituting this identity into Eq. (107) gives
𝐷∗(v,𝑡 𝑘)=a −+𝑘 𝑡𝑘(v)P(kerA)⊥d+𝑘 𝑡𝑘(v)PkerA d.(109)
Finally, applyingPkerA and usingPkerA P(kerA)⊥ =0andP 2 kerA =P kerA yields
PkerA𝐷∗(v,𝑡 𝑘)=P kerA a−+𝑘 𝑡𝑘(v)PkerA d,(110)
as desired. □
K.4 Proof of Corollary 1
Proof.Note that the probability is well-defined by Lemma 4. Let
d:=a +−a−, 𝑤 𝐷 :=𝑘 𝑡𝑘(a(𝐷) 𝑡𝑘 ).(111)
By Lemma 4,
𝐷∗(a(𝐷) 𝑡𝑘 ,𝑡 𝑘)−a +=−(1−𝑤 𝐷)d.(112)
Incorporating this into Prop. 1, we have that:
PkerA(¯aD,𝑡𝑘−1−a+)  2= PkerA  𝐷∗(a(𝐷) 𝑡𝑘 ,𝑡 𝑘)−a +  2
=(1−𝑤 𝐷)∥PkerA d∥2.
(113)
By Lemma 3, we then have
∥¯aD,𝑡𝑘−1−a+∥2≥
PkerA(¯aD,𝑡𝑘−1−a+)  2.(114)
48

Hence
∥¯aD,𝑡𝑘−1−a+∥2≥(1−𝑤 𝐷)∥PkerA d∥2.(115)
Finally, by Lemma 5,1−𝑤𝐷 >0, and by assumptionPkerA d≠0. Therefore,
∥¯aD,𝑡𝑘−1−a+∥2≥(1−𝑤 𝐷)∥PkerA d∥2 >0,(116)
which proves Cor. 1, as desired.□
K.5 Proof of Proposition 3
Proof.Under the exact denoiser𝐷θ(·,𝑡 𝑘)=𝐷 ∗(·,𝑡 𝑘), Lemma 1 gives, for every finite𝑠≥0,
E
h
a(𝐵) 𝑡𝑘−1

 a(𝐵) 𝑡𝑘 ,u obs i =𝐷∗(v(𝑠),𝑡 𝑘).(117)
Let
𝑤𝑆(𝑠):=𝑘 𝑡𝑘(v(𝑠)), 𝑤 𝐷 :=𝑘 𝑡𝑘(a(𝐷) 𝑡𝑘 ),d:=a +−a−.(118)
By Lemma 4,
𝐷∗(v(𝑠),𝑡 𝑘)−a +=a−+𝑤 𝑆(𝑠)d−a +
=−(1−𝑤 𝑆(𝑠))d. (119)
Therefore
∥PkerA(𝐷∗(v(𝑠),𝑡 𝑘)−a +)∥2=(1−𝑤 𝑆(𝑠))∥P kerA d∥2.(120)
By Lemmas 5 and 7,𝑤′ 𝑆(𝑠)> 0for every finite𝑠≥ 0. Sincev(0)=a (𝐵) 𝑡𝑘 , we have𝑤𝑆(𝑠)>𝑤 𝑆(0)=
𝑘𝑡𝑘(a(𝐵) 𝑡𝑘 )for every𝑠>0. Applying Eq. (120) at𝑠and at0therefore gives
∥PkerA(𝐷∗(v(𝑠),𝑡 𝑘)−a +)∥2≤∥P kerA(𝐷∗(a(𝐵) 𝑡𝑘 ,𝑡 𝑘)−a +)∥2, 𝑠>0.(121)
On the other hand, by Lemma 9,
PkerA¯aD,𝑡𝑘−1 =P kerA𝐷∗(a(𝐷) 𝑡𝑘 ,𝑡 𝑘).(122)
Applying Lemma 4 ata(𝐷) 𝑡𝑘 yields
PkerA(¯aD,𝑡𝑘−1−a+)=P kerA

𝐷∗(a(𝐷) 𝑡𝑘 ,𝑡 𝑘)−a + 
=−(1−𝑤 𝐷)PkerA d.
(123)
Hence
∥PkerA(¯aD,𝑡𝑘−1−a+)∥2=(1−𝑤 𝐷)∥PkerA d∥2.(124)
By Lemma 5,0<𝑤 𝐷 <1, so1−𝑤 𝐷 >0. By Lemma 8,
𝑤𝑆(𝑠)−→1as𝑠→∞.(125)
Therefore there exists𝑠∗ >0such that, for every𝑠≥𝑠 ∗,
1−𝑤 𝑆(𝑠)≤1−𝑤 𝐷.(126)
Multiplying by∥PkerA d∥2 and using Eqs. (120) and (124) gives
∥PkerA(𝐷∗(v(𝑠),𝑡 𝑘)−a +)∥2≤∥P kerA(¯aD,𝑡𝑘−1−a+)∥2,(127)
as desired. □
49

K.6 Proof of Theorem 1
Proof.By Lemma 1, for every finite𝑠,
𝜋(𝐵) 𝑠 =𝒩  𝐷∗(v(𝑠),𝑡 𝑘),𝜎 2 𝑡𝑘−1 K  .(128)
By Lemma 8,𝐷∗(v(𝑠),𝑡 𝑘)→a + as𝑠→∞ . Hence, for everyξ∈R 𝑛, the characteristic function of
𝜋(𝐵) 𝑠 satisfies
b𝜋(𝐵) 𝑠 (ξ)=exp

𝑖ξ⊤𝐷∗(v(𝑠),𝑡 𝑘)− 1 2𝜎2 𝑡𝑘−1 ξ⊤Kξ

−→exp

𝑖ξ⊤a+− 1 2𝜎2 𝑡𝑘−1 ξ⊤Kξ

.
(129)
The limit is the characteristic function of𝒩(a+,𝜎 2 𝑡𝑘−1 K) and is continuous atξ=0 . Therefore, Lévy’s continuity theorem gives
𝜋(𝐵) 𝑠 ⇒𝒩(a +,𝜎 2 𝑡𝑘−1 K)as𝑠→∞.(130)
Finally, when𝑡𝑘−1 =𝑡 0, for everyξ∈R 𝑛,
exp

𝑖ξ⊤a+− 1 2𝜎2 𝑡0ξ⊤Kξ

−→exp(𝑖ξ⊤a+)as𝜎 𝑡0→0.(131)
The limit is the characteristic function of𝛿a+, so another application of Lévy’s continuity theorem
yields
𝒩(a+,𝜎 2 𝑡0K)⇒𝛿 a+.(132)
This proves Thm. 1, as desired.□
K.7 Proof of Proposition 4
Proof.Letd:=a +−a−,m:=(a −+a+)/2,𝑄:=d ⊤K−1d, and
𝐶:=
∥Ad∥2 2∥K−1d∥2 2
𝛾2 .
SinceAd≠0andKis positive definite, we have𝑄,𝐶>0.
Fix a realization ofa(𝐵) 𝑡𝑘+1 satisfying𝑘 𝑡𝑘+1(a(𝐵) 𝑡𝑘+1 )≤1/2−𝛿, and set𝑝:=𝑘 𝑡𝑘+1(a(𝐵) 𝑡𝑘+1 ). By Lemma 4,
𝐷∗(a(𝐵) 𝑡𝑘+1 ,𝑡 𝑘+1)=a −+𝑝d(133)
=m−

1
2−𝑝

d.(134)
Therefore, since no optimization is performed at𝑡𝑘+1,
a(𝐵) 𝑡𝑘 =m−

1
2−𝑝

d+𝜎 𝑡𝑘 ε(𝐵) 𝑘 ,ε (𝐵) 𝑘 ∼𝒩(0,K).
Conditionally ona(𝐵) 𝑡𝑘+1 ,d⊤K−1ε(𝐵) 𝑘 ∼𝒩(0,𝑄), since
V ar

d⊤K−1ε(𝐵) 𝑘

=d⊤K−1KK−1d=𝑄.
50

Thus, with𝑍:=d ⊤K−1ε(𝐵) 𝑘 /√𝑄, we have𝑍∼𝒩(0,1)and
d⊤K−1(a(𝐵) 𝑡𝑘 −m)=−𝑄

1
2−𝑝

+𝜎 𝑡𝑘
p
𝑄𝑍.(135)
Define𝐸:={𝑍≤𝛿 √𝑄/(2𝜎𝑡𝑘)}. Since1/2−𝑝≥𝛿, on𝐸,
d⊤K−1(a(𝐵) 𝑡𝑘 −m)≤−𝑄𝛿+𝜎 𝑡𝑘 p 𝑄𝛿√𝑄 2𝜎𝑡𝑘 (136)
=− 𝑄𝛿 2 .(137)
For𝑥>0, the standard Gaussian Chernoff bound gives
Pr(𝑍>𝑥)=Pr(𝑒 𝑥𝑍 >𝑒 𝑥2 )≤𝑒 −𝑥 2 E[𝑒𝑥𝑍]=𝑒 −𝑥 2/2.
Taking𝑥=𝛿 √𝑄/(2𝜎𝑡𝑘)therefore yields
Pr

𝐸

 a(𝐵) 𝑡𝑘+1  ≥1−exp  −𝑄𝛿 2 8𝜎2 𝑡𝑘 ! .(138)
Now set𝑤(𝑠):=𝑘 𝑡𝑘(v𝑡𝑘(𝑠)). Sincev𝑡𝑘(0)=a (𝐵) 𝑡𝑘 , Lemma 4 and Eq. (137) give, on𝐸,
𝑤(0)= '›
«
1+exp
 
 −
d⊤K−1(a(𝐵) 𝑡𝑘 −m)
𝜎2 𝑡𝑘
 

“ﬁ
‹
−1
(139)
≤

1+exp
(
𝑄𝛿
2𝜎2 𝑡𝑘
)!−1
< 1 2.(140)
By Lemma 7,
𝑤′(𝑠)= 𝐶
𝜎4 𝑡𝑘
𝑤(𝑠) 2(1−𝑤(𝑠)) 3.(141)
By Lemma 5,0<𝑤(𝑠)< 1for every finite𝑠, so𝑤′(𝑠)> 0. By Lemma 8,𝑤(𝑠)→ 1as 𝑠→∞ . Hence,
on𝐸,𝜏 𝑡𝑘 <∞and, by continuity,𝑤(𝜏𝑡𝑘)=1/2.
Integrating Eq. (141) from0to𝜏𝑡𝑘 and using𝑢=𝑤(𝑠)gives
𝜏𝑡𝑘 =
𝜎4 𝑡𝑘
𝐶
∫ 1/2
𝑤(0)
𝑑𝑢
𝑢2(1−𝑢) 3 (142)
≥
𝜎4 𝑡𝑘
𝐶
∫ 1/2
𝑤(0)
𝑑𝑢
𝑢2 (143)
=
𝜎4 𝑡𝑘
𝐶

1
𝑤(0)−2

,(144)
where the inequality follows from(1−𝑢)−3≥1for𝑢∈(0,1/2]. By Eq. (140),
1
𝑤(0)≥1+exp

𝑄𝛿
2𝜎2 𝑡𝑘
!
,
51

so, on𝐸,
𝜏𝑡𝑘≥
𝜎4 𝑡𝑘
𝐶
"
exp

𝑄𝛿
2𝜎2 𝑡𝑘
!
−1
#
.
Consequently, by Eq. (138),
Pr

𝜏𝑡𝑘≥
𝜎4 𝑡𝑘
𝐶
"
exp

𝑄𝛿
2𝜎2 𝑡𝑘
!
−1
#

 a(𝐵) 𝑡𝑘+1 ! (145)
≥1−exp

−𝑄𝛿 2
8𝜎2 𝑡𝑘
!
,(146)
as desired. □
K.8 Proof of Proposition 5
Proof. Let d :=a+−a−, m :=(a−+a+)/2, and𝐶 :=∥Ad∥ 2 2∥K−1d∥2 2/𝛾2. SinceAd≠ 0, K ispositive
definite, and𝛾 >0, we have𝐶>0.
By Lemma 4, for every𝜎 >0,
𝑘𝜎(v)=

1+exp

− d⊤K−1(v−m) 𝜎2 −1 .(147)
Setℎ:=d ⊤K−1(v★−m). By assumption,𝑘𝜎(v★)<1/2for every𝜎 >0. Using Eq. (147),
𝑘𝜎(v★)< 1 2 ⇐⇒exp

− ℎ 𝜎2

>1⇐⇒ℎ<0.
Hence, setting𝑏:=−ℎ>0,
𝑤𝜎(0)=𝑘 𝜎(v★)= 1 1+exp(𝑏/𝜎 2)∈

0, 1 2

.(148)
Fix𝜎 >0, and writev𝜎(𝑠) for the solution of Eq. (12) at noise level𝜎, initialized byv𝜎(0)=v ★.
By Lemma 6, this solution exists uniquely for all𝑠≥0. Let𝑤𝜎(𝑠):=𝑘 𝜎(v𝜎(𝑠)).
By Lemma 7, with𝜎in place of𝜎𝑡𝑘,
𝑤′ 𝜎(𝑠)= 𝐶 𝜎4𝑤𝜎(𝑠) 2(1−𝑤 𝜎(𝑠)) 3.(149)
ByLemma5,0 <𝑤 𝜎(𝑠)< 1foreveryfinite 𝑠. Since𝐶> 0,Eq.(149)gives 𝑤′ 𝜎(𝑠)> 0,so 𝑤𝜎 isstrictly
increasing. Moreover, by Lemma 8,𝑤𝜎(𝑠)→ 1as 𝑠→∞ . Together with Eq. (148) and continuity of
𝑤𝜎, this implies0< 𝜏(𝜎)<∞and
𝑤𝜎(𝜏(𝜎))= 1 2.(150)
Rearranging Eq. (149), integrating from0to𝜏(𝜎), and using the change of variables𝑢=𝑤 𝜎(𝑠)
gives
𝜏(𝜎)= 𝜎4
𝐶
∫ 𝜏(𝜎)
0
𝑤′ 𝜎(𝑠)
𝑤𝜎(𝑠) 2(1−𝑤 𝜎(𝑠)) 3 𝑑𝑠(151)
= 𝜎4
𝐶
∫ 1/2
𝑤𝜎(0)
𝑑𝑢
𝑢2(1−𝑢) 3.(152)
52

The change of variables is valid because𝑤𝜎 is continuously differentiable and strictly increasing.
We first consider𝜎↓0. For𝑢∈(0,1/2],(1−𝑢) −3≥1, so
𝜏(𝜎)≥ 𝜎4
𝐶
∫ 1/2
𝑤𝜎(0)
𝑑𝑢
𝑢2 (153)
= 𝜎4
𝐶

1
𝑤𝜎(0)−2

(154)
= 𝜎4
𝐶

exp

𝑏
𝜎2

−1

,(155)
where the last equality follows from Eq. (148). For every𝑥> 0, the power series for𝑒𝑥 gives
𝑒𝑥−1≥𝑥 3/6. Taking𝑥=𝑏/𝜎 2 in Eq. (155),
𝜏(𝜎)≥ 𝜎4
𝐶
1
6

𝑏
𝜎2
 3
= 𝑏3
6𝐶𝜎 2−→∞as𝜎↓0.(156)
Wenextconsider 𝜎→∞ . For𝑢∈( 0, 1/2],𝑢2(1−𝑢) 3≤𝑢 2≤ 1/4,so[𝑢2(1−𝑢) 3]−1≥ 4. Therefore
𝜏(𝜎)≥ 4𝜎4
𝐶

1
2−𝑤 𝜎(0)

.(157)
Set𝑥:=𝑏/𝜎 2. By Eq. (148),
1
2−𝑤 𝜎(0)= 𝑒𝑥−1 2(1+𝑒 𝑥).(158)
For all sufficiently large𝜎,0<𝑥≤1. Then𝑒 𝑥−1≥𝑥and𝑒 𝑥≤𝑒, so
1
2−𝑤 𝜎(0)≥ 𝑥 2(1+𝑒) = 𝑏 2(1+𝑒)𝜎 2.
Combining this with Eq. (157),
𝜏(𝜎)≥ 2𝑏 𝐶(1+𝑒) 𝜎2−→∞as𝜎→∞.(159)
Itremainstoshowthat 𝜏attainsitsminimum. Define 𝐻(𝑞) :=
∫ 1/2
𝑞 𝑢−2(1−𝑢)−3𝑑𝑢 for𝑞∈( 0, 1/2).
The fundamental theorem of calculus gives𝐻′(𝑞)=−𝑞 −2(1−𝑞)−3, so𝐻 is continuous. By Eq. (148),
𝜎↦→𝑤 𝜎(0)is continuous, and therefore Eq. (152) gives
𝜏(𝜎)= 𝜎4
𝐶𝐻(𝑤𝜎(0)),
so𝜏is continuous on(0,∞).
Fixany¯𝜎 >0andset 𝑀 :=𝜏(¯𝜎)+ 1. ByEqs.(156)and(159),thereexist0 < 𝜎low <¯𝜎 < 𝜎high <∞
such that
𝜏(𝜎)>𝑀whenever0< 𝜎≤𝜎 low or𝜎≥𝜎 high.(160)
Since𝜏 is continuous on the compact interval[𝜎low,𝜎 high], the extreme value theorem gives some
𝜎★∈[𝜎 low,𝜎 high]such that
𝜏(𝜎★)=min
𝜎∈[𝜎low,𝜎high]
𝜏(𝜎).(161)
53

Since¯𝜎∈[𝜎 low,𝜎 high], we have𝜏(𝜎★)≤𝜏( ¯𝜎)<𝑀 . Thus, Eq. (160) gives𝜏(𝜎)> 𝜏(𝜎★) for every𝜎∉
[𝜎low,𝜎 high], while minimality on the compact interval gives𝜏(𝜎)≥𝜏(𝜎 ★)for every𝜎∈[𝜎 low,𝜎 high].
Therefore,
𝜏(𝜎★)=min
𝜎>0
𝜏(𝜎),𝜎 ★∈[𝜎 low,𝜎 high],(162)
as desired. □
K.9 Proof of Proposition 6
Proof.Fixa∈R 𝑛. For anyh∈R 𝑛, define𝜙(𝜀):=ℒ(a+𝜀h). Then
𝜙(𝜀)= 1 2𝛾2∥Aa−u obs+𝜀Ah∥2 2 (163)
= 1 2𝛾2  ∥Aa−u obs∥2 2+2𝜀(Ah)⊤(Aa−u obs)+𝜀 2∥Ah∥2 2  .(164)
Therefore,
𝜙′(0)= 1 𝛾2(Ah)⊤(Aa−u obs)(165)
=h⊤

1
𝛾2 A⊤(Aa−u obs)

.(166)
Since
𝜙′(0)=𝐷 hℒ(a)= ⟨∇aℒ(a),h⟩=h⊤∇aℒ(a),(167)
for everyh∈R 𝑛, comparison with the expression above gives
∇aℒ(a)= 1 𝛾2 A⊤(Aa−u obs),(168)
which proves the first claim.
We now show that this gradient has no component inkerA. Set
y:=Aa−u obs∈R 𝑚.(169)
For everyz∈kerA,
A⊤y,z  =⟨y,Az⟩=0,(170)
becauseAz=0. Hence
A⊤y∈(kerA) ⊥.(171)
The orthogonal projection of a vector in(kerA)⊥ ontokerAis zero. Consequently,
PkerA∇aℒ(a)= 1 𝛾2 PkerA A⊤(Aa−u obs)(172)
=0,(173)
as desired. □
54

K.10 Proof of Proposition 7
Proof. Let d :=a +−a−, 𝑤(𝑠) :=𝑘 𝑡𝑘(v(𝑠)). Define the Jacobian of the exact denoiser by
J𝐷∗(v,𝑡 𝑘):=∇ v𝐷∗(v,𝑡 𝑘)∈R 𝑛×𝑛, and define
P(v,𝑡 𝑘):=J 𝐷∗(v,𝑡 𝑘)J𝐷∗(v,𝑡 𝑘)⊤.(174)
Define𝒥𝑡𝑘(v) :=ℒ(𝐷∗(v,𝑡 𝑘)). ThegradientflowinEq.(12)istherefore v′(𝑠)=−∇ v𝒥𝑡𝑘(v)

 v=v(𝑠).
By the multivariate chain rule,
∇v𝒥𝑡𝑘(v)=J 𝐷∗(v,𝑡 𝑘)⊤∇aℒ(a)

 a=𝐷∗(v,𝑡𝑘).(175)
Consequently,
v′(𝑠)=−J 𝐷∗(v(𝑠),𝑡 𝑘)⊤∇aℒ(a)

 a=a(𝑠),(176)
wherea(𝑠):=𝐷 ∗(v(𝑠),𝑡 𝑘). Differentiatinga(𝑠)and applying the chain rule once more gives
a′(𝑠)=J 𝐷∗(v(𝑠),𝑡 𝑘)v′(𝑠)(177)
=−J 𝐷∗(v(𝑠),𝑡 𝑘)J𝐷∗(v(𝑠),𝑡 𝑘)⊤∇aℒ(a)

 a=a(𝑠) (178)
=−P(v(𝑠),𝑡 𝑘)∇aℒ(a)

a=a(𝑠),(179)
as desired.
We next show explicitly that the preconditioner in Eq. (174) can introduce a nonzero measure-
ment nullspace component. By Lemma 4, we have that
𝐷∗(v,𝑡 𝑘)=a −+𝑘 𝑡𝑘(v)d.(180)
Moreover, by Lemma 4, we have that
𝑘𝑡𝑘(v)=

1+exp
(
−
d⊤K−1  v− a−+a+ 2 
𝜎2 𝑡𝑘
)!−1
.(181)
Thus,
∇v𝑘𝑡𝑘(v)= 𝑘𝑡𝑘(v)(1−𝑘 𝑡𝑘(v)) 𝜎2 𝑡𝑘 K−1d.(182)
Differentiating Eq. (180) with respect tovtherefore gives
J𝐷∗(v,𝑡 𝑘)=d  ∇v𝑘𝑡𝑘(v) ⊤.(183)
Substituting Eq. (182) into Eq. (183) and then into Eq. (174) yields
P(v,𝑡 𝑘)=d

∇v𝑘𝑡𝑘(v)
⊤∇v𝑘𝑡𝑘(v)d⊤ (184)
=
∇v𝑘𝑡𝑘(v) 2 2 dd⊤ (185)
= 𝑘𝑡𝑘(v)2(1−𝑘 𝑡𝑘(v))2
𝜎4 𝑡𝑘
∥K−1d∥2 2dd⊤.(186)
We now evaluate the output space optimization alongv(𝑠). By Eq. (180),a(𝑠)=a −+𝑤(𝑠)d.
Sinceu obs=Aa+ anda+=a−+d,
Aa(𝑠)−u obs=Aa−+𝑤(𝑠)Ad−Aa + (187)
=−(1−𝑤(𝑠))Ad.(188)
55

By Prop. 6,
∇aℒ(a)

a=a(𝑠) = 1 𝛾2 A⊤(Aa(𝑠)−u obs) (189)
=− 1−𝑤(𝑠) 𝛾2 A⊤Ad.(190)
Using Eq. (186) and Eq. (190) in Eq. (179) gives
a′(𝑠)= 𝑤(𝑠) 2(1−𝑤(𝑠)) 3
𝛾2𝜎4 𝑡𝑘
∥K−1d∥2 2dd⊤A⊤Ad(191)
=
∥Ad∥2 2∥K−1d∥2 2
𝛾2𝜎4 𝑡𝑘
𝑤(𝑠) 2(1−𝑤(𝑠)) 3d,(192)
sinced⊤A⊤Ad=∥Ad∥ 2 2. ApplyingPkerA to Eq. (192) yields
PkerA a′(𝑠)= ∥Ad∥2 2∥K−1d∥2 2
𝛾2𝜎4 𝑡𝑘
𝑤(𝑠) 2(1−𝑤(𝑠)) 3PkerA d.(193)
For every finite𝑠≥ 0, we have that𝑤(𝑠)∈( 0, 1) by Lemma 5, and furthermoreAd≠ 0and
PkerA d≠ 0byassumption. Since K ispositivedefinite,itisinvertible,and d≠ 0implies∥K−1d∥2 2 >
0. Together with𝛾 >0and 𝜎𝑡𝑘 > 0, every scalar factor multiplyingPkerA d in Eq. (193) is strictly
positive. Therefore,PkerA 𝑑 𝑑𝑠 a(𝑠)=P kerA a′(𝑠)≠0for every finite𝑠≥0, as desired.□
K.11 Statement and Proof of Proposition 8
We first state the proposition:
Proposition 8.Assume0 <𝑧 − <𝑧 + < 1without loss of generality, and1≤𝑚≤𝑛 . Let A=OG
and PkerA be the orthogonal projection matrix of a vector ontokerA. Under a centered finite difference
discretizationof𝒢 as Gwith𝑛>max{ 1 𝑧− , 1 1−𝑧+ , 2 𝑧+−𝑧− },if Osamples𝑚pointsuniformlyatrandom,without
replacement, fromu, thenAa+≠Aa− and with probability at least1−(𝑚/𝑛)4,P kerA a+≠P kerA a−.
Discussion: The condition on𝑛 ensures that the resolution is fine enough that there are some
grid points between the locations of𝑧− and𝑧+. Additionally, we ensure that𝑧− and𝑧+ are not at
the end of the grid.
We then provide the proof, which leverages the classic result by Thomas [Tho49]:
Proof.Let
ℎ:= 1 𝑛+1 , 𝑥 𝑖 :=𝑖ℎ, 𝑖=0,...,𝑛+1,(194)
so that𝑥0 = 0and 𝑥𝑛+1 = 1. Under the centered finite difference discretization of𝑢′′(·)=𝑎(·) on
(0,1)with homogeneous Dirichlet boundary conditions, defineL∈R𝑛×𝑛 by
(Lu)𝑖 := 𝑢𝑖−1−2𝑢 𝑖+𝑢 𝑖+1
ℎ2 , 𝑖=1,...,𝑛,(195)
where𝑢 0=𝑢 𝑛+1 =0. The corresponding discrete solution operator isG=L−1.
56

We first identify the indices on whichd:=a+−a− is nonzero. Define
𝑝:=min{𝑖∈{1,...,𝑛}:𝑥 𝑖≥𝑧−}, 𝑞:=max{𝑖∈{1,...,𝑛}:𝑥 𝑖 <𝑧+}.(196)
The assumption𝑛>max
n
1
𝑧− , 1 1−𝑧+ , 2 𝑧+−𝑧−
o
impliesℎ= 1 𝑛+1 < 1 𝑛 <𝑧 −, and hence𝑥1 =ℎ<𝑧 −, so
𝑝≥ 2. Similarly,ℎ< 1 𝑛 < 1−𝑧+,sothat 𝑥𝑛 = 1−ℎ>𝑧 + andtherefore 𝑞≤𝑛− 1. Finally,wehavethat
2ℎ< 2 𝑛 <𝑧+−𝑧−. By the definition of𝑝,𝑥𝑝−1 <𝑧−≤𝑥 𝑝, so that𝑥𝑝+1 =𝑥 𝑝−1+ 2ℎ<𝑧 −+ 2ℎ<𝑧 +,
and thus
2≤𝑝<𝑞≤𝑛−1.(197)
Since𝑧− <𝑧+,thetwodiscretizedcoefficientfieldsdifferpreciselyatthegridpoints 𝑥𝑖∈[𝑧−,𝑧+).
Hence, setting𝑐:=𝑎 (1)−𝑎(2)≠0, we have
d=𝑐
𝑞Õ
𝑗=𝑝
e𝑗,(198)
wheree 𝑗 is the𝑗th standard basis vector ofR𝑛.
We first show thatAd≠0. For𝑖,𝑗∈{1,...,𝑛}, define
𝑔𝑖𝑗 :=−ℎmin(𝑥 𝑖,𝑥 𝑗)

1−max(𝑥 𝑖,𝑥 𝑗)

,(199)
and letg𝑗 :=(𝑔 1𝑗,...,𝑔 𝑛𝑗)⊤. We verify thatLg𝑗 =e 𝑗. Firstly, extend the definition of𝑔𝑖𝑗 so that
𝑔0𝑗 =𝑔 𝑛+1,𝑗 = 0. If𝑖<𝑗 , then𝑔𝑖𝑗 =−ℎ𝑥 𝑖(1−𝑥 𝑗), which yields
𝑔𝑖−1,𝑗−2𝑔𝑖𝑗+𝑔𝑖+1,𝑗
ℎ2 = 0. Similarly, if𝑖>𝑗 ,
then𝑔𝑖𝑗 =−ℎ𝑥 𝑗(1−𝑥 𝑖), which then yields that
𝑔𝑖−1,𝑗−2𝑔𝑖𝑗+𝑔𝑖+1,𝑗
ℎ2 = 0. When𝑖=𝑗 , using𝑥𝑗−1 =𝑥 𝑗−ℎ
and𝑥 𝑗+1 =𝑥 𝑗+ℎ,
𝑔𝑗−1,𝑗−2𝑔 𝑗𝑗+𝑔 𝑗+1,𝑗 =−ℎ
h
(𝑥𝑗−ℎ)(1−𝑥 𝑗)−2𝑥 𝑗(1−𝑥 𝑗)+𝑥 𝑗(1−𝑥 𝑗−ℎ)
i
(200)
=ℎ 2.(201)
Consequently,
𝑔𝑗−1,𝑗−2𝑔𝑗𝑗+𝑔𝑗+1,𝑗
ℎ2 = 1. Thus Lg𝑗 =e 𝑗 for every𝑗, so G=L −1 =[g 1,...,g 𝑛]. In
particular, G is symmetric, since𝑔𝑖𝑗 =𝑔 𝑗𝑖, and for every𝑖,𝑗∈{ 1,...,𝑛} ,𝑔𝑖𝑗 < 0, becauseℎ> 0and
𝑥𝑖,𝑥 𝑗∈(0,1).
It follows that, for every𝑖= 1,...,𝑛 ,(Gd)𝑖 =𝑐 ˝𝑞 𝑗=𝑝 𝑔𝑖𝑗, and since𝑔𝑖𝑗 < 0,𝑐≠ 0,(Gd)𝑖 ≠ 0for
every𝑖=1,...,𝑛, and thusAd=OGd≠0as desired.
It remains to characterizePkerA d. We have that
PkerA d=0⇐⇒d∈range(A 𝑇)(202)
⇐⇒d∈range(GO ⊤)(203)
⇐⇒Ld∈range(O ⊤),(204)
where the last equivalence follows fromL=G−1.
We now computeLd. Since
𝑑𝑖 =
(
𝑐, 𝑝≤𝑖≤𝑞,
0,otherwise, (205)
57

and2≤𝑝<𝑞≤𝑛−1, the centered difference gives
(Ld)𝑖 =
 

𝑐
ℎ2, 𝑖=𝑝−1,
− 𝑐 ℎ2, 𝑖=𝑝,
− 𝑐 ℎ2, 𝑖=𝑞, 𝑐
ℎ2, 𝑖=𝑞+1,
0,otherwise.
(206)
Equivalently,Ld= 𝑐 ℎ2  e𝑝−1−e 𝑝−e 𝑞+e 𝑞+1  . Since𝑐≠ 0and 𝑝<𝑞 , its support is therefore exactly
𝐵:=supp(Ld)={𝑝−1,𝑝,𝑞,𝑞+1},|𝐵|=4.(207)
Let𝑆⊂{ 1,...,𝑛},|𝑆|=𝑚> 0be the set of indices sampled byO. Since O is a selection
matrix, range(O⊤)=span{e 𝑖 :𝑖∈𝑆} . ThusLd∈range(O ⊤) ⇐⇒𝐵⊂𝑆 , so thatPkerA d= 0 ⇐⇒
𝐵⊂𝑆.
If𝑚< 4, thenP(𝐵⊂𝑆)= 0. If𝑚≥ 4, since𝑆 is chosen uniformly from the𝑚-element subsets of
{1,...,𝑛},
P(𝐵⊂𝑆)=
𝑛−4
𝑚−4

𝑛
𝑚
 (208)
= 𝑚(𝑚−1)(𝑚−2)(𝑚−3) 𝑛(𝑛−1)(𝑛−2)(𝑛−3) (209)
=
3Ö
𝑟=0
𝑚−𝑟
𝑛−𝑟 .(210)
For𝑟= 0, 1, 2, 3and 𝑚≤𝑛 , 𝑚−𝑟 𝑛−𝑟 ≤ 𝑚 𝑛, since𝑛(𝑚−𝑟)≤𝑚(𝑛−𝑟) ⇐⇒𝑚𝑟≤𝑛𝑟 . Therefore, in either
case𝑚<4or𝑚≥4,
P(PkerA d=0 )=P(𝐵⊂𝑆)≤
𝑚
𝑛
 4
.(211)
Taking complements yields
P(PkerA d≠0 )≥1−
𝑚
𝑛
 4
.(212)
Together withAd≠0, this proves the proposition as desired.□
58
