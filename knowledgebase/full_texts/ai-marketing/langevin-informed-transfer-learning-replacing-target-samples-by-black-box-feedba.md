---
title: 'Langevin-Informed Transfer Learning: Replacing Target Samples by Black-Box Feedback'
url: https://arxiv.org/abs/2610.01522
category: ai-marketing
subcategory: measurement
date: 2026-10
venue: ''
authors:
- Vladimir R. Kostic
- Karim Lounici
- Hélène Halconruy
- Timothée Devergne
- Michele Parrinello
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.01522
pages: 43
chars: 124343
fetched_at: '2026-11-08T13:25:11+00:00'
kb_version: 1
---

# Langevin-Informed Transfer Learning: Replacing Target Samples by Black-Box Feedback

Langevin-Informed Transfer Learning:
Replacing Target Samples by Black-Box Feedback
Vladimir R. Kostic
CSML, Istituto Italiano di Tecnologia
University of Novi Sad
vladimir.kostic@iit.it
Karim Lounici
CMAP-Ecole Polytechnique
karim.lounici@polytechnique.edu
Hélène Halconruy
SAMOV AR, Télécom Sud-Paris
MODAL’X, Université Paris Nanterre
helene.halconruy@telecom-sudparis.eu
Timothée Devergne
CSML & ATSIM, Istituto Italiano di Tecnologia
timothee.devergne@iit.it
Michele Parrinello
ATSIM, Istituto Italiano di Tecnologia
michele.parrinello@iit.it
Massimiliano Pontil
CSML, Istituto Italiano di Tecnologia
AI Centre, University College London
massimiliano.pontil@iit.it
Abstract
Many scientific and machine learning systems, from molecular dynamics to
diffusion models and beyond, are governed by stochastic dynamics with low-
dimensional structure, evolving on slow timescales. However, target trajectories,
used to identify and interpret such dynamics, are often inaccessible: only biased or
static samples that explore the underlying manifold are available. We introduce
Langevin-Informed Transfer Learning (LITL), a framework for recovering target
Langevin dynamics from biased source samples using only black-box feedback.
LITL learns the leading spectral structure of the target infinitesimal generator and
the projected drift through Dirichlet representation learning, enabling kinetic recon-
struction in spectral form and slow-manifold gradient field estimation. We further
introduce a spherical variant well suited to steering normalized latent representa-
tions commonly used in learning systems toward desired objectives. We establish
finite-sample guarantees for eigenvalue, eigenfunction, and projected drift estima-
tion in Sobolev norms, thereby ensuring generalization of these quantities and their
first-order derivatives. Empirically, LITL recovers physical transition timescales
from biased molecular simulations, builds kinetic structure from static samples of
generative models, reconstructs spherical symmetries of physical systems, and en-
ables post-hoc latent steering of trained neural networks under black-box feedback.
Together, these results position spectral operator learning as a practical framework
for recovering stochastic dynamics under distribution shift and unlock applications
across machine learning and the physical sciences.
1 Introduction
Many systems across science and modern machine learning evolve through stochastic dynamics
shaped by a small number of slow collective modes. In molecular dynamics, these modes govern
metastable states and transition pathways [51, 5]; in modern machine learning, they relate to semantic
structures in generative [ 63] and transformer models [ 23, 30]. In both contexts, Langevin-type
Preprint.
arXiv:2610.01522v1  [cs.LG]  1 Oct 2026

dynamics underlie these stochastic gradient flows, further being backbone of Bayesian sampling,
diffusion models, and latent generative processes [10, 40, 53, 54, 58]. Across these domains, the key
object controlling long-timescale behavior is theinfinitesimal generator, whose dominant spectral
structure encodes geometry, kinetics, and transition pathways between metastable configurations of
the underlying dynamics. Understanding such systems requires recovering this spectral structure, a
task intractable with classical methods due to the curse of dimensionality that calls for data-driven
approaches. In practice, however, the target dynamics are often inaccessible: one may only observe
static or biased samples together with black-box evaluative feedback, while target trajectories,
gradients, or direct dynamical observations remain unavailable. So, a fundamental challenge persists:
How can one recover a target system’s dynamics without access to its trajectories?
This setting arises naturally in biased molecular simulations [ 36], generative models producing
equilibrium samples without kinetics [37], physical systems where potentials are reconstructed from
measurements [28], and post-hoc latent steering problems with purely evaluative black-box feedback.
Existing transfer-learning and adaptation methods predominantly rely on retraining, fine-tuning, or
direct optimization of parametric objectives [44, 39, 20]. In contrast, recent spectral approaches in
dynamical systems focus on learning transfer operators or infinitesimal generators from trajectory
data [24, 31, 13, 7, 34], but do not address transfer under distribution shift or recovery of target
dynamics from static biased samples. Moreover, existing generator-learning methods at best provide
guarantees only in L2-type geometries and all fail to recover projected drift fields [32, 8, 62, 16, 33],
limiting controlled reconstruction of target dynamics and kinetic transfer.
We introduceLangevin-Informed Transfer Learning (LITL), a framework for recovering and trans-
ferring target Langevin dynamics from biased source samples using only black-box feedback. Rather
than addressing transfer learning in full generality, LITL focuses specifically on transferring stochas-
tic dynamics by recovering the target generator’s slow spectral structure together with a projected
drift on a learned slow manifold. The method combines importance weighting, Sobolev/Dirichlet
representation learning, and generalized eigendecomposition to reconstruct physically meaningful
dynamics from static or biased data without requiring target trajectories, differentiable objectives,
or retraining. In this sense, LITL reframes transfer learning as transfer of stochastic dynamics: by
learning the generator geometry rather than task-specific parameters, it enables post-hoc steering
through geometry-aware Langevin flows in latent spaces. This perspective is particularly compelling
for modern machine learning systems operating on normalized embeddings and diffusion-like latent
dynamics, where semantic organization is intrinsically geometric and metastable. In this setting,
we further introduce a streamlined spherical formulation enabling efficient gradient-free transfer on
normalized latent manifolds. To relate LITL to existing transfer learning methods, see App. A.
On the theoretical side, we establish finite-sample guarantees for eigenvalue, eigenfunction, and
projected-drift estimation in Sobolev norms. Empirically, LITL recovers physical transition timescales
from biased molecular simulations, extracts kinetic structure from static GenAI samples, reconstructs
spherical dynamics of cobalt nanoparticles from black-box potential evaluations, and enables post-hoc
fairness-aware latent steering without retraining. Together, these results position spectral operator
learning as a practical framework for recovering and transferring stochastic dynamics under dis-
tribution shift, while highlighting broader implications for machine learning systems governed by
Langevin-type dynamics.
Contributions.This paper makes three main contributions.(i) Methodology:We introduce LITL, a
framework for recovering and transferring stochastic dynamics from biased samples using black-box
feedback.(ii) Theory:To our knowledge, we provide the first finite-sample guarantees for eigenvalue,
eigenfunction, and projected-drift estimation in Sobolev norms.(iii) Applications:We demonstrate
effectiveness across molecular modeling, physical systems, and post-hoc alignment tasks.
Paper organization.Sec. 2 provides background on Langevin dynamics and generator learning.
Sec. 3 presents our method. Sec. 4 establishes finite-sample bounds, and Sec. 5 reports experiments.
The appendix covers related work, additional background, and proofs of the main results.
2 Background and problem setup
Langevin dynamics and spectral learning.Many systems exhibit multiple timescales, with long-
term behavior governed by a few slow modes encoded in the generator’s spectrum. We recover this
2

structure from samples via the generator and its resolvent. A canonical model for such dynamics is
the overdamped Langevin equation describes a system evolving in a state space X ⊆Rd under a
potentialU:R d →Rat inverse temperatureβ >0:
dXt =−∇U(X t), dt+
p
2β−1 dWt, X 0 =x,(1)
where (Wt)t is a standard d-dimensional Brownian motion. It admits a unique strong solution defining
a Markov process X= (X t)t≥0 with transfer operators (Tt)t≥0 given by Ttf(x) =E[f(X t)|X0 =
x]. The law of Xt converges to the Boltzmann measureπ(dx) =e −βU(x) dx/( R e−βU(x) dx), and the
evolution is governed by theinfinitesimal generator L:= lim t→0+ (Tt −I)/t , which acts on smooth
functions as Lf=−⟨∇U,∇f⟩+β −1∆f, is linked to the transfer operators through Tt =e tL,
and is self-adjoint on L2 π by integration by parts. If the spectrum is discrete, the generator has the
decomposition
L= P i∈N0 λi ψi ⊗ψ i,(2)
where the eigenvalues (λi)i∈N0 determine the characteristic timescales of the system. In particular,
eigenvalues close to 0 correspond to slow, metastable dynamics, while large negative eigenvalues
describe rapidly decaying modes, making the spectral decomposition a natural tool for identifying
coherent structures and long-time behavior in the dynamics. While learning L directly is challenging
due to its unbounded nature, its resolvent Rµ = (I−µ −1L)−1, µ >0, is compact for confining
potentials and shares the same eigenfunctions, making it more amenable for spectral learning, see
App. B.
Transfer learning via biased dynamics.Sampling from complex distributions is typically impacted
by slow mixing due to metastability. To accelerate exploration, we can simulate dynamics under a
biased potential U ′ =U+V , where V:R d →R flattens energy barriers. Let L′ and π′ denote
the generator and invariant measure of the biased (source) dynamics. Our objective is to recover the
spectral decomposition of the (unbiased)targetgenerator L from trajectories generated under L′. At
the generator level, the bias enters as a linear additive perturbation, L′ =L− ⟨∇V,∇(·)⟩, which is
in principle straightforward to debias. This linear structure is lost at the level of transfer operators,
since the associated semigroups do not factorize (eL′ ̸=e Le−⟨∇V,∇(·)⟩), limiting the applicability of
transfer-operator-based methods. A widely used debiasing strategy is importance weighting, which
relies on the Radon–Nikodym derivative dπ dπ′ (x) = eβV(x) R eβV(x) dπ′(x), see App. C, and corrects for the
distribution shift induced by the bias.
Sobolev spaces and energy norms.To learn the generator or its resolvent from data, we need
a function space where they arewell-behavedandestimable from samples. Since the generator
acts through gradients, this leads to Sobolev (energy) norms combining values and derivatives,
which both regularize the problem and admit gradient-based empirical estimation under importance
weighting. Our approach relies on energy (equivalently graph) norms induced by the generator:
∥f∥ 2 W µ π =⟨(I−µ −1L)f, f⟩L2π =∥f∥ 2 L2π +∥∇f∥ 2 L2π /(µβ), which defines the Sobolev space
W µ π =  f∈ L2 π(X)

 ∥f∥ 2 W µ π =∥f∥ 2 L2π +∥∇f∥ 2 L2π /(µβ)<∞ 	 .(3)
More generally, for p >0, we define the fractional Sobolev norm ∥f∥ 2 W µ,p π :=⟨(I−µ −1L) p f, f⟩L2π
and space W µ,p π ={f∈ L 2 π(X)| ∥f∥ W µ,p π <∞} . These norms form a Sobolev scale: they
interpolate between the L2 π(X) norm (at p= 0 ) and the energy norm (at p= 1 ). Crucially, these
norms can be expressed as expectations involving function gradients, enabling empirical estimation
from biased trajectory data through importance weighting.
3 LITL methodology
We now turn the operator perspective into a practical procedure for learning spectral structure of the
target dynamics from biased data.
LITL in a nutshell.Given samples from the biased distribution π′, LITL proceeds in two stages.
(1)Representation learning.We learn neural features zθ = (z θ i )m i=0 to approximate the leading
invariant subspace of the resolvent Rµ = (I−µ −1L)−1 with their span Hθ by minimizing the loss
(7). (2)Projected spectral estimation and dynamics recovery.We project the operator Rµ onto Hθ
and compute its empirical spectral decomposition via (12). Finally, using ∇U=Lf for f(x) =x ,
we recover the projected dynamics by regressing coordinate functions in the learned spectral basis.
3

Step 1. Representation learning.We first construct a low-dimensional representation that captures
the slow modes of the target dynamics. To this end, we consider the resolvent Rµ, whose leading
eigenfunctions define the invariant subspace of interest, and correct for the distribution shift between
the source π′ and target π using importance weights v=e βV with mean v=E x′∼π′v(x′). We
introduce neural networks zθ i :X →R , 0≤i≤m , defining the representation space Hθ =
span(zθ i )m i=0 ⊆ Wµ π , and aim to approximate a spectral decomposition ofR µ in this space,
Rµ ≈Z θDθZ ∗ θ ,with the orthonormality constraintZ ∗ θ Zθ ≈I,
whereZ θ :R m+1 → Wµ π is the injection operator mappingv∈R m+1 to functionv Tzθ(·),
Dθ = diag

e−(dθ 0)2 , . . . , e−(dθ m)2  ,andZ ∗ θ f=  ⟨R−1 µ f, zθ j ⟩L2π(X)  0≤j≤m .
SinceR µ is a compact self-adjoint operator, this leads to the population loss
Lα(θ) = v

∥Rµ−ZθDθZ ∗ θ ∥2 HS(W µ π ) − ∥Rµ∥2 HS(W µ π )

+α v∥Z ∗ θ Zθ −I∥ 2 F ,(4)
where v accounts for the importance weighting induced by the bias potential. All operator terms in
this loss can be expressed as expectations underπ ′. Indeed, for1≤i, j≤m,
⟨zθ i ,(−L)z θ j ⟩L2π =E x′∼π′[v(x′)∇z θ i (x′)T∇zθ j (x′)],
implying thatZ ∗ θ Zθ corresponds to the covariance matrix inW µ π space
Wθ = vZ ∗ θ Zθ =E x′∼π′[wθ(x′)wθ(x′)T],withw θ(x′) = hp v(x′)zθ(x′)

 q v(x′) µ βJθ(x′) i ,(5)
and Jθ(x′)=  ∂1zθ(x′)

 · · ·

 ∂dzθ(x′)  ∈R (m+1)×d is the Jacobian of the neural network embedding.
On the other hand, the embedding of the operator Rµ in the W µ π reduces to the L2 π-covariance matrix
Cθ = v Z∗ θ RµZθ =E x′∼π′[v(x′)zθ(x′)zθ(x′)T].(6)
This yields the equivalent form of the loss
Lα(θ) = tr

(DθWθ)2 −2 vD θ Cθ+α(Wθ−vI) 2 .(7)
To estimate (7) from data, we construct an unbiased empirical loss using source samples. The easiest
way is to take two independent samples to estimate the products of random variables (DθWθ)2,
v(D θCθ), W2 θ and vW θ. This amounts to splitting each batch in two and estimating the loss as
bLα(θ) =tr
h
1
2 ( bW 1 θDθ bW 2 θDθ+ bW 2 θDθ bW 1 θDθ)−bv1 bC 2 θDθ−bv2 bC 1 θDθ+α( bW 1 θ −bv1I)( bW 2 θ−bv2I) i ,(8)
where bC k θ and bW k θ are the empirical covariances in (5) and (6), respectively, for empirical dis-
tributions bπ′ 1 =⌈b/2⌉ −1 P⌈b/2⌉ i=1 δx′ i and bπ′ 2 =⌊b/2⌋ −1 Pb ⌈b/2⌉+1 δx′ b+1 , respectively, while
bvk =E x′∼bπ′ k v(x′), k∈[2]. Notably, the computational complexity of the loss (8) is of the or-
der O(b m2d), where d is the state dimension and b the sample batch size. Alternatively to (8), the
products of expectations in the population loss (7) can be estimated from iid samples (x′ i)i∈[b] via
U-statistics yielding computational complexityO(b 2md), see App. D.4 for details.
The following result provides theoretical guarantees for our approach. The proof is provided in D.5.
Theorem 3.1.Given a compact operatorR µ,µ >0, if for allθ∈Θ,(z θ i )m i=0 ⊆ W1 π′(X), then
E
 bLα(θ)  = v2 Lα(θ)≥ −Pm i=0 µ2v2 (µ−λi)2 ,(9)
where, if λm+1<λm equality holds iff span(ψi)m i=0 = span(z θ i )m i=0, or equivalently Pm =P θ,
with Pm and Pθ being the orthogonal projectors onto span(ψi)m i=0 and span(zθ i )m i=0, respectively.
Additionally, if α >0 at optimum Pm =P θ =Z θZ ∗ θ and λθ i =d θ i , 0≤i≤m , up to the ordering
of indices.
4

This theorem provides a justification for minimizing the loss in (7) with stochastic optimization
algorithms to obtain an approximation of the leading invariant subspace of the resolvent Rµ, with a
natural metric to quantify the distance to the optimum being
Em(θ) =∥P m −P θ∥W µ π →W µ π +∥Z ∗ θ Zθ −I∥.(10)
The main advantage of this representation learning method is that it exploits knowledge of the
underlying process. Knowing that the dynamics are Langevin, and given only the change between
the source and target potentials (bias) V and the diffusion coefficient β, we can learn representations
that approximate the slow manifold of the target process from source samples.
We next show how, once the slow manifold is learned, to compute estimators of the generator’s
spectral decomposition and the target potential’s gradient.
Step 2. Projected spectral estimation and dynamics recovery.Once the representation Hθ approx-
imates the leading invariant subspace, we estimate the spectral structure of the target dynamics within
this space. Using the fact that the generator and resolvent share eigenfunctions, with eigenvalues
related byλ i =µ(1−1/ν i), we consider the decomposition
Rµ = P j∈N0 νj ψj ⊗ψ j.(11)
Since after learning θ the bias of representation space Em(θ) becomes sufficiently small, we have
that PmRµ =P mRµPm≈PθRµPθ, the task is to empirically estimate the operator PθRµPθ from
some samples (x′ j)n j=1. We can either use the same samples for training representations, or a set of
new independent samples, in which case the statistical analysis simplifies.
Recalling that the orthogonal projector in W µ π onto Hθ is given by Pθ =Z θ(Z ∗ θ Zθ)†Z ∗ θ , we have
that PθRµPθ = v ZθW† θCθW† θZ ∗ θ . But then, since due to the ortho-normality regularization of the loss (α >0) we can assume that Wθ are invertible, using the property of low-rank eigenvalue
problems, see [26],we have that the non-zero eigenvalues νθ i and their eigenfunctions ψθ i , 0≤i≤m ,
of PθRµPθ are characterized by Cθui =ν θ i Wθui, where ψθ i =z θ(·)Tui, 0≤i≤m . Therefore, the
slow eigenpairs of the target generatorLare estimated by solving generalized eigenvalue problem
bCθ bui =bνi bWθ bui,s.t.bu T i bWθ bui =bv,0≤i≤m,(12)
wherebv= Pn i=1 v(x′ i)and defining bλi =µ(1−1/bν i)and bψi =z θ(·)T bui for0≤i≤m.
As a result, we obtain the empirical operators that approximateP mRµ andP mL, respectively, as
bRµ = Pm i=0bνi bψi ⊗ bψi,and bL= Pm i=0 bλi bψi ⊗ bψi.(13)
Finally, to recover the projected dynamics, we empirically estimate the gradient using that∂kU=
−Lfk holds for k-th coordinate projection of the statefk :x7→x k, 1≤k≤d . Namely, by definition
of theW µ π -norm, we have that
∂kU=− P∞ i=0 λiψiEx∼π[ψi(x)xk + 1 µβ ∂kψi(x)],1≤k≤d,
which, by replacing L by bL and empirically estimating the expectation, after some algebra, yields that
the weight matrix bGof the target gradient’s projection onto the slow manifold can be computed as
bG=− Pn j=1 v(x′ j ) bv  xjzθ(x′ j)T + 1 µβ Jθ(x′ j)T  bΩbΛbΩT,(14)
where, bΩ = [bu0 | · · · |bum], bΛ = diag

bλ0,· · ·,bλm

, and, as above,J θ denotes the Jacobian ofz θ.
This provides an estimate of the gradient of the target potential on the slow manifoldspan(ψ i)m i=0.
Inference.Before presenting high-probability error bounds for the resulting spectral decomposition
and gradinet estimation in Sec. 4, we note that the target Langevin dynamics can be estimated by
exponentiating bLto forecast the evolution of conditional probabilities
P[Xt∈B|X0 =x] = Pm i=0 ebλit buT i zθ(x) P x′ j ∈B v(x′ j ) bv buT i zθ(x′ j)
for any t≥0 and measurable set B⊆ X, under the same temperature β as the source data. This
approximation of the transfer operator semi-group etbL is detailed in App. B. Moreover, once the
5

target gradient is estimated as ∇U≈ d∇U= bGzθ(·) with bG∈R d×(m+1), it enables the simulation
of new Langevin dynamicsd bXt =− bGzθ( bXt)dt+ p 2β−1dWt.
Spherical LITL.Unlike classical Langevin dynamics in Euclidean space, which requires a confining
potential to admit an invariant distribution, Langevin dynamics on a sphere admits a well-defined
invariant measure even in the absence of a potential. This provides a principled, geometry-respecting
way to steer the system while avoiding the instability and mode collapse that can arise in unconstrained
Euclidean settings. In particular, if the source dynamics is pure diffusion on the sphere ( U ′ = 0 )
the uniform measure is its invariant distribution. This is crucial in our setting sincestatic samples
from the reference distribution are readily available by direct normalization of isotropic random
vectors, avoiding long trajectories simulation or stochastic integrators tuning. In this context, transfer
learning from the black-box potential is performed by short-horizon gradient updates on the sphere,
∇Sd−1 U(x) = (I−xx T)∇U(x), thereby driving the system toward the wells of potential energy.
This approach is motivated by the prevalence of normalized embeddings and cosine-based geometry in
modern AI systems, models latent dynamics as spherical diffusion with a locally constructed, human-
induced potential, enabling targeted, on-the-fly modulation of the invariant distribution without
retraining the base model. This geometric formulation aligns naturally with contrastive representation
learning, angular-margin classifiers, and embedding-based retrieval, where semantic information
is encoded directionally rather than in magnitude. Thus, Spherical LITL provides a principled and
sample-efficient mechanism for human control of learned representations, enhancing adaptability and
robustness, while preserving the global structure of pretrained representations.
4 Statistical bounds
We recall that spectral estimation enables analysis and understanding of the dynamics, while gradient
estimation enables efficient simulation of the learned dynamics. We establish statistical guarantees
for both spectral estimation and gradient estimation of target dynamics based on biased samples. To
this end, we make the following assumptions:
(BE) Bounded embeddings.There exist τ≥1 such that ess supx′∼π′ |∂kzθ j (x′)| ≤τ <∞ ,
∀k= 0, . . . , dandj= 0, . . . m, with the convention∂0zθ =z θ;
(CP) Confining potential.The potential U satisfies U(x)≥2α∥x∥ 21{∥x∥≥R} −c , ∀x, for some
α >0,R >0,c∈R, and the bias obeys∥V∥ ∞ <∞;
(RA) Gradient regularity. ∃p≥1 such that ∀k∈[d] , ∥∂kU∥ W µ,p π <∞ , that is ∥∇U∥ W µ,p π <∞ .
While these typical assumptions are discussed in detail in App. E.2, here we briefly note that they are
all satisfied in the prototypical example of spherical Langevin dynamics.
Let εn(δ)=τ e2β∥V∥ ∞
q
m d
µ β nln( m δ ), σ2 π=Ex∼π∥x∥2 and gapi= minℓ̸=i|νℓ−νi|= µ (µ−λi) min ℓ̸=i |λi−λℓ| |µ−λℓ|
be the resolvent’s spectral gap. The following key statistical result is proved in App. E.6.
Theorem 4.1.Let Assumptions(BE)and(CP)be satisfied. Assume that β(µ−λ m)≥1 and
n≳d∨e 3β∥V∥ ∞/2τ 2md/(µβ). Then w.p.a.l.1−δ, for any1≤i≤m:
|λi−bλi|
|λi| ≲
q
µ
|λi| +
q
|λi|
µ
2
Em(θ)+εn(δ)

and∥ bψi−ψi∥W µ π ≲ Em(θ) gapi + εn(δ) [gapi−3Em(θ)]+
Moreover, if(RA)holds, then∀s∈[0,1]w.p.a.l.1−δ:
∥∇U− d∇U∥ W µ,s π ≲ν
p−s
2
m+1∥∇U∥ W µ,p π +µ σπ ν − 3+s 2 m  Em(θ) +ε n(δ)  .
The above eigenvalue bound demonstrates that the shift parameter µ acts as aspectral focusing
mechanism. By tuning µ close to a target eigenvalue |λi|, the relative error is minimized since
the factor (
p
µ/|λi|+
p
|λi|/µ)2 achieves its minimum value of 4 when µ≈ |λi|. This allows
targeted estimation of specific spectral components by appropriately selecting µ. Furthermore, the
eigenfunction bound depend on whether the representation learning error is dominated by thespectral
gap, an expected necessary condition. The gradient bound reveals two competing sources of error:
the bias term ν(p−s)/2 m ∥∇U∥ W µ,p π from spectral truncation, and the statistical term σπεn(δ) from finite-sample estimation. Our approach hinges on accurately learning the dominant eigenspace of
6

the generator through representation learning: when the data exhibits low-dimensional structure,
reflected in a spectral gap νm≫νm+1, the leading m eigenfunctions capture the essential dynamics.
This spectral truncation to the dominant m-dimensional eigenspace is mathematicallyanalogous to
coarse-grainingprocedures in statistical mechanics [ 45], where high-frequency modes are integrated
out to yield effective dynamics on slow collective coordinates. In this context, the only error to
the approximated projected gradient is the second term. However, even if the task is to reconstruct
the complete gradient, whenever ν2 m+1 ≪σ πεn(δ), the bias becomes negligible so that the rate is
dominated by εn(δ), which is essentially parametric. Finally, we also note that if the true gradient
belongs to W µ,p π , then it can be accurately estimated in the Sobolev norm W µ,s π for any s < p, which
is a stronger result than a guarantee solely in theL 2 π(X)norm.
5 Experiments
In this section, we present four experiments, for classical and spherical Langevin dynamics, each
highlighting the diverse capabilities of the LITL framework.
Double well potential:In this first experiment, we test our method on a 1D-toy system for which
ground truth references can be numerically computed.The aim is to compare our method to the
baselines on spectral information recovery, and demonstrate performance on recovery of distribution
flow for which no baseline exists.We work with a double well potential U(x) to which we add a
perturbation potential V(x) which will induce more barrier crossing events from one minimum to the
other, see Figure 4 in App. F.1. We simulate the dynamics under U ′(x) = (U+V)(x) and keep the
values of the position and of V(x) with time. We compare the results obtained with LITL and with,
Method λ1=0.22 λ2=15.37 λ3=16.06 λ4=47.31
[16] 0.621±0.01 46.6±0.3 49.1±0.5 146±2
[62] 1±2 2±2 2±2 8±7
LITL 0.23±0.02 15.315±0.01 16.09±0.04 46.9±0.1
Table 1: Eigenvalue estimation in the double well experiment.
up to our knowledge, the only two existing methods for the same task [16] and [62]. While Table
1 shows that LITL is the only method that accurately estimated higher eigenvalues, in Figure 4 of
App. F.1 we show that the same holds for eigenfunction estimation. We note that results of [62] suffer
from uncontrolled collapse of learned subspace to slower modes, likely caused by larger number of
sensitive hyper-parameters.
Finally, we can also learn the forces acting on the system using d∇U= bGzθ(·) with bG given in (14)
and perform simulations of the true potential U for a lower cost, which is shown in Figures 5 and 6
of App. F, however LITL remains a unique method that solves this task.
Alanine-Dipeptide molecule:The second experiment is a controlled molecular transfer benchmark,
demonstrating how LITL transfers data samples from biased (non-physical) simulations of Alanine-
Dipeptide to recover physical transition rates.The system has 21 dimensional state made of dihedral
angles, and due to the curse of dimensionality spectral decompositions cannot be numerically
computed. The key message is that this simple molecule displays two main slow modes, of which
the slower one is identified by the dihedral angle ϕ and cannot be observed without the addition
of a bias potential during a simulation, which then requires the transfer learning method. Hence,
we trained the LITL model with and without reweighting and observed that for the slowest mode,
the eigenvalue changes from -0.56 in the non-reweighted model (learning without transfer yields
the physically impossible timescale ≈2) to -0.029 in the reweighted model (giving the physically
meaningful timescale≈350).
Chignolin miniprotein:In this experiment we demonstrate how LITL can equip generative molecular
models with kinetic capaabilities. Modern GenAI, such as BioEmu [37], can now produce equilibrium
protein conformations at unprecedented scale, but evaluating whether these samples reproduce the
correct kineticsremains a major challenge. Standard spectral methods such as TICA [ 49] require
trajectory data and therefore cannot be applied to static samples generated by foundation models. In
contrast, LITL learns slow dynamical modes directly from equilibrium samples, providing spectral
collective variables that identify metastable states and transition pathways without costly simulations.
7

Figure 1: Free-energy landscapes learned from MD and BioEmu samples using LITL. State occupa-
tion probabilities computed from the recovered generators reveal kinetic mismatch between BioEmu
and physical MD dynamics.
We train LITL using graph neural networks [ 48] on (i) long MD trajectories of the Chignolin
miniprotein [38] and (ii) static samples generated by BioEmu [37]. Projecting onto the two slowest
learned eigenfunctions reveals the underlying free-energy landscape and metastable organization
(Fig. 1).
Qualitatively, both models recover the same dominant folding mechanisms: the first mode corre-
sponds to folding, while the second captures transitions between unfolded and intermediate hairpin
states. Quantitatively, however, the recovered kinetics differ substantially. In particular, BioEmu
underestimates the free-energy barrier between unfolded and folded states, leading to significantly
different metastable occupancies (folded/intermediate/unfolded: 60/24/16% for BioEmu versus
77/8/15%for MD).
These results show that LITL not only extracts physically meaningful slow modes from static
generative samples, but also enables direct kinetic comparison between generative and physical
molecular dynamics models.
Cobalt nanoparticle dynamics.Here we demonstrate how spherical LITL can recover structured
physics of magnetization using only measurements.We learn the spectral properties of the Langevin
generator on a sphere S2, modeling the magnetization dynamics of a cobalt nanoparticle under the
potential U(m) =−K u(m·n u)2 +K c(m2 xm2 y +m 2 ym2 z +m 2 zm2 x), nu being easy axis of uniaxal
anisotropy. [21, 22]. For uniaxal and cubic anisotropy constants Ku=1.0 and Kc=0.3, respectively,
four metastable states are separated by energy barriers. Understanding the thermodynamics and
kinetics of cobalt nanoparticles, in particular the metastable states and transition rates revealed by the
Langevin generator, helps set switching fields for memory devices, control blocking temperatures
and data retention times, and optimize heat dissipation in hyperthermia applications. LITL’s ability to
infer these crucial objects using only potential evaluations is critical to experimental scenarios where
anisotropy landscapes are reconstructed from measurements such as micro-SQUID experiments [28].
Figure 2 shows results from the LITL estimator that achieves ≈5·10 −3 errors w.r.t. numerically
computed ground truth for both time-scales and their eigenfunctions (in L2 norm) using n= 10 4
uniform samples. Remarkably, our method was able to recover over ten eigenfunctions with the
correct symmetry groups of the model, see App. F.3, purely from black-box potential evaluations and
without prior knowledge of the functional form, directly impacting applications from data storage
(bit stability) to hyperthermia (heat dissipation pathways).
Fairness-aware transfer via latent diffusion.Finally, we present a proof-of-concept ex-
periment in which we assess the LITL’s performance in the challenging setting of transfer
learning related to algorithmic fairness.To this end, we chose the Adult Income dataset
(https://archive.ics.uci.edu/dataset/2/adult), a standard benchmark for fairness in binary classifi-
cation, and consider the difficult unawareness case [11, 18, 61]. The task is to predict whether an
8

Figure 2:Leading eigenfunctions of the Langevin generator for a cobalt nanoparticle potentialin
polar coordinate representation ψ(θ, φ)associated to eigenvalues |bλ1|≈1.36 and |bλ2|≈|bλ3|≈2.5. The
first non-trivial eigenfunction ψ1 reveals the slowest transition pathway between metastable states,
while couple(ψ 2, ψ3)captures faster symmetric modes orthogonal to the first one.
individual’s annual income exceeds $50K, using demographic and employment-related features.
Following common practice, we considergenderas the sensitive attribute and measure fairness by
Equal Opportunity (EO) given by theTrue Positive Rate (TPR) differencebetween males and females.
The dataset is split into thetraining(60%),audit(25%) andtest(15%), with the sensitive variable
removed from the training set. The audit data is used to return black-box feedback on model’s
compliance with desired fairness criterion, typically at most5%TPR disparity between the groups.
The classifier fω(x) = softmax(aT ωeω(x)) learned via empirical risk minimization on the training
set, typically achieves strong predictive performance but does not pass the audit check. Here, ω
denotes the classifier’s parameters, associated with the latent (inner) representation eω(x)∈S d−1,
normalized to lie on the sphere, and the last layer weights aω ∈R d. To remedy this, we consider
Spherical LITL method and transfer n= 5k random representations uniformly sampled on a sphere
S31 to the representations that tend to minimize the TPR gap. That is, while U ′(e) = 0, the feedback
from the audit set V(e)=−U(e) is computed for each e as local TPR gap on the representation
manifold of the audit set, see App. F.4 for details.
While the source generator L′ of pure diffusion, the Laplace-Beltrami operator, captures the intrinsic
geometry and dominant modes of variation of the learned representation subject to pure randomness,
the target Langevin generator L’s eigenfunctions define a hierarchy of fairness related slow and fast
directions on the latent manifold. In particular, the leading nontrivial eigenfunctions correspond to
large-scale, semantically meaningful variations in the representation, while higher modes capture
localized or noisy fluctuations. This multiscale spectral structure provides a natural coordinate
system for analyzing and adjusting the model’s fairness behavior in a controlled and interpretable
way. In particular, we use learned gradient field b∇Sd−1 U(e)=(I−ee T) bGzθ(e) to perform short-
horizon, geometry-respecting updates on the latent sphere with a small γ >0 steps, steering the
pretrained model fω toward configurations with reduced TPR disparity while preserving the dominant
representational structure learned during initial training.
Figure 3 reports the resulting Pareto curves for different step sizesγ, illustrating the trade-off between
accuracy and fairness induced by the LITL intervention. Each point on the curve corresponds to
a different number of LITL steps. As the intervention increases, the TPR difference significantly
decreases to acceptable 1%, while accuracy degrades gracefully.
Moreover, as shown in App. F.4, LITL analysis reveals that around 50% of the TPR gap is due to
the model, which can be eliminated practically without the loss of accuracy by using 16 slowest
eigenfunctions of L. On the other hand, the intrinsic bias in the data can be corrected with additional
16 eigenfucntions which efficiently balance competing objectives TPR gap and accuracy.
To further support above conclusions, we perform ablation study by changing key components of
LITL, and compare to adequate ML baselines. As one can observe in Table 2, (i) replacing the
generator-based update collapses performance ( ≤10% ), showing that gains are not due to latent
post-processing (here via local finite differences); (ii) removing audit signal degrades performance,
yet still yields ≈50˘60% improvement, significantly outperforming zero-order baselines; (iii)
incorrect truncation degrades performance, confirming the importance of recovering the correct slow
9

Figure 3: Accuracy–fairness Pareto curve for the Adult Income experiment. Each point corresponds
to a different number of LITL steps. LITL hyperparameters are calibrated on audit set, and then used
to achieve substantial reduction in TPR disparity with a limited decrease in accuracy on a test set.
Method Rel. Acc. [%]↑ Rel. TPR gap [%]↑
LITL (full) 97.11±1.00 94.16±4.04
LITL (local proxy) 99.91±0.09 8.02±2.41
LITL (no feedback) 99.27±0.37 59.88±5.08
LITL (bad truncation) 95.68±0.89 70.68±5.72
Retraining baseline 101.32±0.21 94.60±4.30
Fine-tuning baseline 100.25±0.17 90.11±5.78
Latent correction baseline 98.34±0.61 32.33±2.51
Table 2: Ablation study and baseline comparisons in the fairness experiment over 10 trials with
recorded relative accuracy and TPR gap change w.r.t. the original classifier.
eigenspace. Together, these results show thatimportance weighting, spectral structure, and generator-
based updatesare all necessary for the observed ≈94% fairness improvement. Concerning baselines,
since no standard fairness methods operate under identical constraints, we follow [18] and include
retraining and fine-tuning in an unawareness setting (model excludes sensitive features but uses them
in loss regularization). We also include a zero-order latent correction (nearest-neighbor weighted
ridge regression of spherical gradients) under the same constraints. All methods use matched tuning
budgets. As we can observe, LITL achieves performance comparable to retraining/fine-tuning but
without access to sensitive features, gradients, or retraining, and clearly outperforms black-box latent
correction.
6 Conclusions
We introduced Langevin-Informed Transfer Learning (LITL), a framework for recovering and trans-
ferring target stochastic dynamics from biased samples using only black-box feedback. By learning
the target generator’s slow spectral structure and projected drift with finite-sample guarantees, LITL
enables principled coarse-graining, kinetic reconstruction without target trajectories, and post-hoc
steering of ML models without retraining. Conceptually, LITL reframes transfer learning as the
recovery and manipulation of stochastic dynamics rather than parameter adaptation. In other words:
Instead of transferring weights or features, LITL transfers generator structure,
enabling geometry-aware steering through learned slow manifolds.
Our results suggest broader relevance beyond molecular systems. Since Langevin-type dynamics also
underlie stochastic gradient flows and diffusion-based generative models, spectral operator learning
may provide a new route for analyzing and steering latent stochastic dynamics in modern AI systems
through gradient-free feedback.
Limitations.LITL currently focuses on reversible Langevin dynamics and assumes informative
black-box evaluations together with identifiable low-dimensional slow structure. Extending the
framework to non-reversible or time-dependent stochastic dynamics remains an important direction
for future work.
10

References
[1] Dominique Bakry, Ivan Gentil, and Michel Ledoux.Analysis and Geometry of Markov Diffusion
Operators. Springer, 2014.
[2] Jonathan Baxter. A model of inductive bias learning.Journal of Artificial Intelligence Research,
12:149–198, 2000.
[3] Shai Ben-David, John Blitzer, Koby Crammer, and Fernando Pereira. A theory of learning from
different domains.Machine Learning, 79(1):151–175, 2010.
[4] Petar Bevanda, Max Beier, Sebastian Kerz, Armin Lederer, Stefan Sosnowski, and Sandra
Hirche.arXiv preprint arXiv.2112.04085, 2021.
[5] Luigi Bonati, GiovanniMaria Piccini, and Michele Parrinello. Deep learning the slow modes
for rare events sampling.Proceedings of the National Academy of Sciences, 118(44), 2021.
[6] Luigi Bonati, Enrico Trizio, Andrea Rizzi, and Michele Parrinello. A unified framework for
machine learning collective variables for enhanced sampling simulations: mlcolvar.The Journal
of Chemical Physics, 159(1):014801, 2023.
[7] Daniel Bruder, Xun Fu, R. Brent Gillespie, C. David Remy, and Ram Vasudevan. Data-Driven
Control of Soft Robots Using Koopman Operator Theory.IEEE Transactions on Robotics,
37(3):948–961, 2021.
[8] Vivien Cabannes and Francis Bach. The Galerkin method beats graph-based approaches
for spectral algorithms. InProceedings of The 27th International Conference on Artificial
Intelligence and Statistics, volume 238, pages 451–459. PMLR, 2024.
[9] Andrea Caponnetto and Ernesto De Vito. Optimal rates for the regularized least-squares
algorithm.Foundations of Computational Mathematics, 7(3):331–368, 2007.
[10] Pratik Chaudhari and Stefano Soatto. Stochastic gradient descent performs variational inference,
converges to limit cycles for deep networks.Information and Inference: A Journal of the IMA,
7(4):605–636, 2018.
[11] Jiahao Chen, Nathan Kallus, Xiaojie Mao, Geoffry Svacha, and Madeleine Udell. Fairness
under unawareness: Assessing disparity when protected class is unobserved. InProceedings of
the Conference on Fairness, Accountability, and Transparency, pages 339–348, 2019.
[12] Wei Chen, Hythem Sidky, and Andrew L. Ferguson. Nonlinear discovery of slow molecular
modes using state-free reversible vampnets.The Journal of Chemical Physics, 150(21):214114,
2019.
[13] Matthew J Colbrook and Alex Townsend. Rigorous data-driven computation of spectral
properties of koopman operators for dynamical systems.Communications on Pure and Applied
Mathematics, 77(1):221–283, 2024.
[14] Jeffrey Comer, James C. Gumbart, Jérôme Hénin, Tony Lelièvre, Andrew Pohorille, and
Christophe Chipot. The adaptive biasing force method: Everything you always wanted to know
but were afraid to ask.The Journal of Physical Chemistry B, 119(3):1129–1151, 2015.
[15] E. Brian Davies.Spectral Theory and Differential Operators. Cambridge University Press,
1995.
[16] Timothée Devergne, Vladimir R. Kostic, Michele Parrinello, and Massimiliano Pontil. From
biased to unbiased dynamics: An infinitesimal generator approach. InAdvances in Neural
Information Processing Systems, volume 37, pages 1–27, 2024.
[17] Timothée Devergne, Vladimir Kostic, Massimiliano Pontil, and Michele Parrinello. Slow
dynamical modes from static averages.The Journal of Chemical Physics, 162(12):124108,
2025.
11

[18] Michele Donini, Luca Oneto, Shai Ben-David, John S Shawe-Taylor, and Massimiliano Pontil.
Empirical risk minimization under fairness constraints.Advances in Neural Information
Processing Systems, 31, 2018.
[19] Chelsea Finn, Pieter Abbeel, and Sergey Levine. Model-agnostic meta-learning for fast adapta-
tion of deep networks.International Conference on Machine Learning, 2017.
[20] Yaroslav Ganin, Evgeniya Ustinova, Hana Ajakan, Pascal Germain, Hugo Larochelle, François
Laviolette, Mario March, and Victor Lempitsky. Domain-adversarial training of neural networks.
Journal of Machine Learning Research, 17(59):1–35, 2016.
[21] Dmitry A Garanin. Fokker-planck and landau-lifshitz-bloch equations for classical ferromagnets.
Physical Review B, 55(5):3050, 1997.
[22] José Luis García-Palacios and Francisco J Lázaro. Langevin-dynamics study of the dynamical
properties of small magnetic particles.Physical Review B, 58(22):14937, 1998.
[23] Borjan Geshkovski, Cyril Letrouit, Yury Polyanskiy, and Philippe Rigollet. A mathematical
perspective on transformers.Bulletin of the American Mathematical Society, 62(3):427–479,
2025.
[24] Steffen Grünewälder, Guy Lever, Arthur Gretton, Luca Baldassarre, Sam Patterson, and Massi-
miliano Pontil. Conditional mean embeddings as regressors. InICML, 2012.
[25] Jonathan Ho, Ajay Jain, and Pieter Abbeel. Denoising diffusion probabilistic models.Advances
in Neural Information Processing Systems (NeurIPS), 33:6840–6851, 2020.
[26] Roger A Horn and Charles R Johnson.Matrix analysis. Cambridge university press, 2012.
[27] Michele Invernizzi and Michele Parrinello. Rethinking metadynamics: From bias potentials to
probability distributions.The Journal of Physical Chemistry Letters, 11(7):2731–2736, 2020.
[28] M. Jamet, W. Wernsdorfer, C. Thirion, D. Mailly, V . Dupuis, P. Mélinon, and A. Pérez. Magnetic
anisotropy of a single cobalt nanocluster.Physical Review Letters, 86(20):4676, 2001.
[29] Longlong Jing and Yingli Tian. Self-supervised visual feature learning with deep neural
networks: A survey.IEEE Transactions on Pattern Analysis and Machine Intelligence, 2020.
[30] Juno Kim, Denny Wu, Jason Lee, and Taiji Suzuki. Metastable dynamics of chain-of-thought
reasoning: Provable benefits of search, rl and distillation.arXiv preprint arXiv:2502.01694,
2025.
[31] Stefan Klus, Feliks Nüske, Sebastian Peitz, Jan-Hendrik Niemann, Cecilia Clementi, and
Christof Schütte. Data-driven approximation of the koopman generator: Model reduction,
system identification, and control.Physica D: Nonlinear Phenomena, 406:132416, 2020.
[32] Stefan Klus, Feliks Nüske, Sebastian Peitz, Jan-Hendrik Niemann, Cecilia Clementi, and
Christof Schütte. Data-driven approximation of the Koopman generator: model reduction,
system identification, and control.Physica D, 406:132416, 2020.
[33] Vladimir Kostic, Hélène Halconruy, Timothée Devergne, Karim Lounici, and Massimiliano
Pontil. Learning the infinitesimal generator of stochastic diffusion processes.Advances in
Neural Information Processing Systems, 37:137806–137846, 2024.
[34] Vladimir Kostic, Karim Lounici, Hélène Halconruy, Timothée Devergne, Pietro Novelli, and
Massimiliano Pontil. Laplace transform based low-complexity learning of continuous Markov
semigroups. InAdvances in Neural Information Processing Systems, volume 37, 2024.
[35] Vladimir R. Kostic, Karim Lounici, Grégoire Pacreau, Giacomo Turri, Pietro Novelli, and
Massimiliano Pontil. Neural conditional probability for uncertainty quantification. InAdvances
in Neural Information Processing Systems, volume 37, pages 60999–61039, 2024.
[36] Alessandro Laio and Michele Parrinello. Escaping free-energy minima.Proceedings of the
National Academy of Sciences, 99(20):12562–12566, 2002.
12

[37] Sarah Lewis, Tim Hempel, José Jiménez-Luna, Michael Gastegger, Yu Xie, Andrew Y . K.
Foong, Victor García Satorras, Osama Abdin, Bastiaan S. Veeling, Iryna Zaporozhets, Yaoyi
Chen, Soojung Yang, Adam E. Foster, Arne Schneuing, Jigyasa Nigam, Federico Barbero,
Vincent Stimper, Andrew Campbell, Jason Yim, Marten Lienen, Yu Shi, Shuxin Zheng, Hannes
Schulz, Usman Munir, Roberto Sordillo, Ryota Tomioka, Cecilia Clementi, and Frank Noé.
Scalable emulation of protein equilibrium ensembles with generative deep learning.Science,
389(6761):eadv9817, 2025.
[38] Kresten Lindorff-Larsen, Stefano Piana, Ron O. Dror, and David E. Shaw. How fast-folding
proteins fold.Science, 334(6055):517–520, 2011.
[39] Mingsheng Long, Yue Cao, Jianmin Wang, and Michael Jordan. Learning transferable features
with deep adaptation networks. InProceedings of the 32nd International Conference on
Machine Learning, volume 37 ofProceedings of Machine Learning Research, pages 97–105,
Lille, France, 2015.
[40] Yi-An Ma, Tianqi Chen, and Emily Fox. A complete recipe for stochastic gradient mcmc.
Advances in Neural Information Processing Systems, 2015.
[41] Andreas Mardt, Luca Pasquali, Hao Wu, and Frank Noé. V AMPnets for deep learning of
molecular kinetics.Nature Communications, 9(1), 2018.
[42] Andreas Maurer, Massimiliano Pontil, and Bernardino Romera-Paredes. The benefit of multitask
representation learning.Journal of Machine Learning Research, 17(81):1–32, 2016.
[43] Bernt Oksendal.Stochastic Differential Equations: an Introduction with Applications. Springer
Science & Business Media, 2013.
[44] Sinno Jialin Pan and Qiang Yang. A survey on transfer learning.IEEE Transactions on
Knowledge and Data Engineering, 22(10):1345–1359, 2010.
[45] Christine Peter and Kurt Kremer. Multiscale simulation of soft matter systems–from the
atomistic to the coarse-grained level and back.Soft Matter, 5(22):4357–4366, 2009.
[46] Robin Rombach, Andreas Blattmann, Dominik Lorenz, Patrick Esser, and Björn Ommer.
High-resolution image synthesis with latent diffusion models.Proceedings of the IEEE/CVF
Conference on Computer Vision and Pattern Recognition (CVPR), pages 10684–10695, 2022.
[47] Hadi Salman, Andrew Ilyas, Logan Engstrom, Ashish Kapoor, and Aleksander Madry. Do
adversarially robust imagenet models transfer better? InProceedings of the 34th International
Conference on Neural Information Processing Systems, NIPS ’20, Red Hook, NY , USA, 2020.
Curran Associates Inc.
[48] Kristof T. Schütt, Huziel E. Sauceda, Pieter-Jan Kindermans, Alexandre Tkatchenko, and
Klaus-Robert Müller. Schnet – a deep learning architecture for molecules and materials.The
Journal of Chemical Physics, 148(24):241722, 2018.
[49] Christoph Schütte, W. Huisinga, and P. Deuflhard. Transfer operator approach to conformational
dynamics in biomolecular systems. In Bernold Fiedler, editor,Ergodic Theory, Analysis, and
Efficient Simulation of Dynamical Systems, pages 191–223. Springer Berlin Heidelberg, 2001.
[50] Christian R. Schwantes and Vijay S. Pande. Modeling molecular kinetics with tica and the
kernel trick.Journal of Chemical Theory and Computation, 11(2):600–608, 2015.
[51] Christof Schütte, Stefan Klus, and Carsten Hartmann. Overcoming the timescale barrier in
molecular dynamics: Transfer operators, variational principles and machine learning.Acta
Numerica, 32:517–673, 2023.
[52] Hidetoshi Shimodaira. Improving predictive inference under covariate shift by weighting the
log-likelihood function.Journal of Statistical Planning and Inference, 90(2):227–244, 2000.
[53] Jascha Sohl-Dickstein, Eric Weiss, Niru Maheswaranathan, and Surya Ganguli. Deep unsuper-
vised learning using nonequilibrium thermodynamics.Proceedings of the 32nd International
Conference on Machine Learning (ICML), pages 2256–2265, 2015.
13

[54] Yang Song, Jascha Sohl-Dickstein, Diederik P. Kingma, et al. Score-based generative modeling
through stochastic differential equations. InInternational Conference on Learning Representa-
tions, 2021.
[55] G. W. Stewart and J.-G. Sun.Matrix Perturbation Theory. Computer Science and Scientific
Computing. Academic Press, 1990.
[56] Glenn M. Torrie and John P. Valleau. Nonphysical sampling distributions in monte carlo
free-energy estimation: Umbrella sampling.Journal of Computational Physics, 23(2):187–199,
1977.
[57] Joel A. Tropp. An introduction to matrix concentration inequalities.Foundations and Trends®
in Machine Learning, 8(1–2):1–230, 2015.
[58] Max Welling and Yee Whye Teh. Bayesian learning via stochastic gradient langevin dynamics.
InProceedings of the 28th International Conference on Machine Learning, pages 681–688,
2011.
[59] Hao Wu and Frank Noé. Variational approach for learning markov processes from time series
data.Journal of Nonlinear Science, 30, 2020.
[60] Jason Yosinski, Jeff Clune, Yoshua Bengio, and Hod Lipson. How transferable are features in
deep neural networks?Advances in Neural Information Processing Systems, 27, 2014.
[61] Rich Zemel, Yu Wu, Kevin Swersky, Toni Pitassi, and Cynthia Dwork. Learning fair representa-
tions. InInternational Conference on Machine Learning, pages 325–333. PMLR, 2013.
[62] Wei Zhang, Tiejun Li, and Christof Schütte. Solving eigenvalue pdes of metastable diffusion
processes using artificial neural networks.J. Comput. Phys., 465:111377, 2022.
[63] Ye Zhu, Yu Wu, Zhiwei Deng, Olga Russakovsky, and Yan Yan. Boundary guided learning-free
semantic control with diffusion models.Advances in Neural Information Processing Systems,
36:78319–78346, 2023.
Appendix
The appendix is organized as follows.
• Sec. A provides a detailed discussion of related work and its comparison to LITL.
• Sec. B presents additional details on the framework, with particular emphasis on Langevin
dynamics and the definition of Dirichlet forms and energy-based norms.
• Sec. C details the transfer learning setup and the importance weighting mechanism for
debiasing.
• Sec. D presents details on the derivation of our training loss and spectral learning.
• Sec. E establishes concentration bounds and proves our main statistical guarantees for
eigenvalue, eigenfunction, and gradient estimation.
• Sec. F presents additional numerical experiments, expanding on those in the main body of
the paper.
A Related work and positioning
Overview.Table 3 summarizes the relationship betweenLangevin Informed Transfer Learning
(LITL)and major paradigms in transfer learning, robustness, Bayesian sampling, and generative
modeling. Existing approaches predominantly transferparameters, representations, losses, or
optimization heuristicsand almost universally require access to target gradients, labels, or explicit
retraining. In contrast, LITL transfersspectral structure of the Langevin generator, enabling post-
training adaptation without target gradients, labels, or retraining.
14

Learning Transfer Needs Target Needs Representative
Method Mechanism Samples or Retraining References
Gradients
Fine-tuning / Parameters / Yes Yes/No [60]
Feature Transfer Features [44]
Domain Adaptation / Reweighted Loss Yes/No Yes [3]
Covariate Shift [52]
Self-supervised / Representations / Yes Yes [29]
Meta-learning Updates [19]
Adversarial Training Robust Parameters Yes Yes [47]
SGLD / Posterior Yes Yes [58]
Bayesian Sampling Samples [40]
Latent Learned Yes No [53]
Diffusion Latent [25]
Models Dynamics [46]
LITL (Ours) Generator Eigenspace No No–
Table 3: Comparison of LITL with related transfer learning, robustness, sampling, and diffusion-
based approaches. Latent diffusion models transfer learned generative dynamics through retraining in
latent spaces, whereas LITL transfers spectral structure of the underlying Langevin generator without
requiring target gradients, retraining, or access to target labels.
Transfer learning, domain adaptation, and meta-learning.Classical transfer learning focuses
on reusing parameters or representations learned on a source task to accelerate optimization or
improve generalization on a target task, typically through fine-tuning or feature reuse [see 44, 60, and
references therein]. Domain adaptation and covariate shift methods reweight losses or samples to
correct distribution mismatch, assuming access to target data and gradients [52, 3]. Meta-learning
provides a different setting in which shared representations are learned from multiple related tasks [2,
19, 29, 42]. While effective, these methods fundamentally rely on retraining and explicit optimization
against a target objective. LITL departs from this paradigm by transferringdynamical structure
rather than parameters or losses, enabling adaptation to unseen objectives without optimization in
the target domain.
Bayesian sampling and Langevin dynamics.Stochastic Gradient Langevin Dynamics (SGLD)
and related MCMC methods provide approximate Bayesian inference by injecting noise into gradient-
based optimization [ 58, 40]. These approaches assume direct access to the target energy or its
stochastic gradients and are not designed for controlled transfer across objectives. LITL is intrinsically
linked to these methods, but addresses a distinct inverse problem: learning and transferring the
generator itself, rather than sampling from a known energy. This enables principled post-hoc
adaptation without modifying step sizes, noise schedules, or loss functions.
Diffusion and score-based generative models.Score-based diffusion models and denoising
diffusion probabilistic models learn gradients of log-densities (the potential) in order to generate
samples by reversing a predefined noising process [ 25]. Latent diffusion models further improve
scalability by learning generative dynamics in compressed latent spaces [ 46]. LITL is related to
score-based diffusion models in that learn gradients of log-densities which can be used to generate
samples. However, the similarity is superficial. Diffusion models learn pointwise, time-dependent
score fields using samples from the target distribution or its noisy marginals [53]. In contrast, LITL
never observes samples from the target Gibbs/Boltzman distribution and does not learn a score field
directly. Instead, it learns spectral representations of the Langevin generator from biased trajectories
and forward-only side information, and reconstructs the target drift only after projection onto the
dominant slow eigenspaces. This yields aspectrally filtered scorethat governs long-time dynamics
rather than pointwise density matching. As a result, LITL enables the creation of unseen kinetic
models with finite-sample guarantees, capabilities that are fundamentally outside the scope of existing
diffusion and score-based approaches. We summarize this comparison in Table 4.
Spectral methods, Koopman operators, and generator learning.A large body of work studies
data-driven approximation of Koopman operators and infinitesimal generators using kernel methods
and deep learning [ 24, 31, 7, 4, 41, 13]. These methods successfully identify slow modes and
metastable states but typically assume access to trajectories generated by the dynamics of interest,
which is typical bottleneck of these approaches. So, to accelerate rare event sampling, practitioners use
15

Aspect Diffusion / Score-Based Models LITL (Ours)
Task Generate samples from a given data
distribution
Create dynamics from log density dis-
crepancies
Observed data Target samples or noisy marginals Samples from a source Gibbs distribu-
tion
Learned object Score field∇logp t(x) Generator eigenspaces & projected
score field
Score estimation Full, pointwise Spectrally projected (slow manifold)
Time dependence Time-dependent Time-homogeneous
Underlying dynamics Artificial noising process Physical / optimization-induced
Langevin dynamics
Target gradients Required Not required
Target samples Required Not required
Transfer across objectives Not supported Supported via transfer of the potential
U ′ →U
Theoretical guarantees Limited Finite-sample spectral and gradient
bounds
Table 4: Compact comparison between diffusion/score-based generative models and Langevin-
Informed Transfer Learning (LITL). Diffusion models learn scores to reproduce observed data
distributions, whereas LITL transfers kinetic structure to construct unseen dynamics without access
to target samples or gradients.
biased simulations with methods such as metadynamics and its variants[36, 27], umbrella sampling
[56], and adaptive biasing force [14]. Furthermore, machine learning has been employed to learn
collective variables from data [50, 5, 12]. While effective for sampling, these methods do not provide
a principled framework or statistical guarantees for transferring learned spectral information from
biased to unbiased dynamics. Crucially, transfer operator methods are fundamentally incompatible
with biased sampling: while the infinitesimal generator depends linearly on the bias potential,
the transfer operator does not, making principled debiasing impossible. Importance reweighting
techniques that correct distribution shift at the generator level fail to properly debias transfer operator
estimates. Recent work therefore focuses on learning the generator directly, often via its resolvent,
which is compact and shares eigenfunctions with the generator [ 33, 34, 62]. While [ 33] provide
statistical guarantees in RKHS settings without transfer, and [16] address biased data using neural
features but lacks strong finite sample guarantees. Notably, none of these works explore transfer
learning across objectives without retraining. LITL extends this line of work by improving the
performance and theoretical analysis, as well as providing a principled mechanism for transferring
spectral structure across biased and unbiased Langevin systems, with explicit control of representation
and optimization error.
Summary perspective.LITL operates at the level of distributional geometry and kinetic structure.
By learning dominant eigenspaces of the Langevin generator from source samples or models and
forward-only side information, it enables principled post-training adaptation to unseen objectives.
This places LITL orthogonally to existing transfer learning, robustness, Bayesian sampling, and
diffusion-based approaches, motivating one to further explore it in combination with those.
B Background: Langevin dynamics and Dirichlet forms
Langevin dynamics (LD) and evolution operatorsAs a reminder, we consider the Langevin
equation
dXt =−∇U(X t)dt+
p
2β−1dWt andX 0 =x,(15)
which describes the dynamics of the random vector Xt in the state space X ⊆Rd, governed by
a potential U:R d →R , where (Wt)t≥0 is a Rp-dimensional standard Brownian motion. Under
the usual conditions [see e.g. 43] that a and b are globally Lipschitz and sub-linear, the SDE (15)
admits a unique strong solution X= (X t)t≥0 that is a Markov process to which we can associate the
semi-group of Markovtransfer operators(T t)t≥0 defined, for everyt≥0, as
[Ttf](x) :=E[f(X t)|X0 =x], x∈ X, f:X →R.(16)
16

For stable processes, the distribution of Xt converges to aninvariant measure π on X , such that
X0 ∼π implies that Xt ∼π for all t≥0 . In such cases, one can define the semi-group on L2 π(X) ,
and characterize the process by theinfinitesimal generatorof the semi-group(T t)t≥0,
Lf:= lim
t→0+
Ttf−f
t (17)
defined on the Sobolev space W 1,2 π of functions in L2 π(X) whose gradients are in L2 π(X) , too, i.e.
L:L 2 π(X)→ L2 π(X) and dom(L) =W µ π . The transfer operator and the generator are linked to each
other by the formulaT t = exp(tL).
After defining the infinitesimal generator for Markov processes by (17), we provide its explicit form
for solution processes of (15). Given a smooth function f∈ C2(X,R) , Itô’s formula [see for instance
1, p. 495] provides fort∈R +,
f(X t)−f(X 0) =
Z t
0
dX
i=1
∂if(X s)dX i s + 1 2
Z t
0
dX
i,j=1
∂2 ijf(X s)d⟨X i, Xj⟩s
=
Z t
0
∇f(X s)TdXs + 1 2
Z t
0
Tr

XT s (∇2f)(X s)Xs  ds,
where∇ 2fis the Hessian matrix off. Recalling (15), we get
f(X t) =f(X 0) +
Z t
0

− ∇U(Xs)T∇f(X s) +β −1Tr  (∇2f(X s))  ds+ p 2β−1 Z t
0
divf(X s)dWs.
Providedfis smooth enough, the expectation of the last stochastic integral vanishes so that we get
E[f(X t)|X0 =x] =f(x) +
Z t
0
E

− ∇U(Xs)T∇f(X s) + ∆f(Xs)

X0 =x  ds
Recalling thatLf= lim
t→0+
(Ttf−f)/t, we get for everyx∈ X,
Lf(x) = lim
t→0+
E[f(X t)|X 0 =x]−f(x)
t
= lim
t→0+
1
t
Z t
0
E
h
− ∇U(Xs)T∇f(X s) +β −1∆f(X s)

 X0 =x i ds
=−∇U(x) T∇f(x) +β −1∆f(x).(18)
which provides the closed formula for the IG associated with the solution process of (15). The
operator L is closed on its domain dom(L) which is equal to the Sobolev space defined for µ >0 by
W µ π = n f∈ L2 π(X)| ∥f∥2 W µ π =⟨(I−µ −1L)f, f⟩L2π =∥f∥ 2 L2π + 1 µβ ∥∇f∥ 2 L2π <∞ o .(19)
An integration by parts argument yieldsZ
(Lf)g dπ=−β −1
Z
⟨∇f,∇g⟩dπ=
Z
f(Lg)dπ,
showing thatLis self-adjoint onL 2 π.
Spectral decomposition and resolvent.When the spectrum of L is discrete, the generator admits
the spectral decomposition
L=
X
i∈N0
λi ψi ⊗ψ i,(20)
which yields, for anyf:X →R,
Ttf=E[f(X t)|X 0 =x] = P∞ i=0etλi ψi(x)⟨ψi, f⟩.(21)
The characteristic timescales of the system are determined by the inverse generator eigenvalues
1/|λi|.
The resolvent operator (I−µ −1L)−1 for µ >0 is a crucial object in our analysis. For confining
potentials, the resolvent is a compact operator on L2 π(X) , unlike the unbounded generator L. This
compactness property makes the resolvent more tractable for statistical learning while preserving the
spectral information of the generator. Indeed, the resolvent shares the same eigenfunctions as L with
transformed eigenvalues: if (λi, ψi) are eigenpairs of L, then ((1−λ i/µ)−1, ψi) are eigenpairs of
the resolvent.
17

Empirical approximation of the transfer operator.If bL= Pm i=0 bλi bψi ⊗ bψi is available, we can
define estimators bTt =e tbL and for any observablef∈ L2 π(X):
bTtf= P i∈N0 etbλi bψi(x)⟨ bψi, f⟩.(22)
In particular, for the indicator function f=1 B of a measurable set B⊆ X , the conditional
probability under the target dynamics is
P[Xt ∈B|X 0 =x] =T t1B(x) =
mX
i=0
eλit ψi(x)
Z
B
ψi(y)dπ(y).(23)
Since the target invariant measure π is unknown, we cannot compute this integral directly. Instead,
using biased samples{x ′ j}n j=1 ∼π ′ and importance weightsv(x ′ j), we approximate:
Z
B
bψi(y)dπ(y) =
Z
B
bψi(y) dπ dπ′ (y)dπ ′(y)≈
Pn
j=1 v(x′ j)1B(x′ j) bψi(x′ j)Pn
j=1 v(x′ j) =
P
x′ j ∈B v(x′ j)buT i zθ(x′ j) Pn
j=1 v(x′ j) .
(24)
This yields the empirical conditional probability
bP[Xt ∈B|X 0 =x] =
mX
i=0
e
bλit buT i zθ(x)
P
x′ j ∈B v(x′ j)buT i zθ(x′ j) Pn
j=1 v(x′ j) .(25)
Dirichlet forms and (fractional) Sobolev spaces.Our approach relies on an energy-based for-
mulation of the IG learning problem, grounded in the theory of Dirichlet forms. This framework
provides a natural variational structure and allows us to exploit the functional-analytic properties of
the underlying generator. We introduce the (shifted) energy functional defined forf∈ L2 π(X)by
Eµ π(f) := lim t→0
Z
X
µ−1 f(f−T tf)  dπ t ,(26)
whenever the limit exists. The collection of such functions defines the domaindom(Eµ) of the energy.
The associatedDirichlet formis the bilinear form obtained by polarization: for any f, g∈dom(E µ),
Eµ(f, g) =−
Z
X
f(µ −1Lg)dπ=
Z
X
(−µ−1Lf)g dπ.(27)
In particular, for everyf∈dom(E µ), the energy satisfiesE µ(f) =E µ(f, f).
We define theenergy normby
∥f∥ 2 W µ π :=⟨(I−µ −1L)f, f⟩L2π =∥f∥ 2 L2π + 1 µβ ∥∇f∥ 2 L2π ,(28)
where (I−µ −1L) −1 denotes the resolvent associated with the generator L. This norm coincides with
the standard Sobolev norm and characterizes both the natural energy space and the domain of the
infinitesimal generator through its associated Dirichlet form.
This definition extends naturally to (possibly higher) fractional orders. For anyp >0, we introduce
thep-thenergy normby
∥f∥ 2 W µ,p π :=⟨(I−µ −1L) p f, f⟩L2π .(29)
The resulting scale of norms interpolates between L2 π regularity and higher-order smoothness induced
by the generator. This construction leads to the definition of thefractional Sobolev spaces: for any
p >0,
W µ,p π :=  f∈ L2 π | ∥f∥W µ,p π <∞ 	 .(30)
These spaces form the natural functional framework for our analysis, capturing the fractional regularity
encoded by the generator and its associated energy structure.
18

C Transfer learning from biased dynamics
Biased Langevin dynamics.To accelerate exploration in the presence of metastability or rare
events, practitioners introduce a bias potential V:R d →R and simulate the modified dynamics
under the perturbed potential
U ′(x) :=U(x) +V(x), x∈ X.(31)
The resulting biased Langevin equation is
dX ′ t =−∇U ′(X ′ t)dt+ p 2β−1dW ′ t , X ′ 0 =x,(32)
where (W ′ t )t≥0 is a standard d-dimensional Brownian motion. This biased process converges to the
biased Boltzmann distribution
π′(dx) = e−βU ′(x) R
X e−βU ′(x)dx dx= e−β(U(x)+V(x)) R X e−β(U(x)+V(x)) dx dx.(33)
Let L′ denote the infinitesimal generator of the biased dynamics, with associated transfer operators
(T ′ t )t≥0.
Generator perturbation.The effect of the bias on the generator is explicit and additive. From the
general form (18), the biased generator acts as
L′f=−⟨∇U ′,∇f⟩+β −1∆f=−⟨∇U+∇V,∇f⟩+β −1∆f.(34)
Therefore, the perturbation decomposes as
L′ =L− ⟨∇V,∇(·)⟩.(35)
This linear dependence on the bias is a key structural property that enables principled debiasing at the
generator level.
Transfer operator perturbation does not factorize.By contrast, the transfer operator perturbation
is highly nonlinear. Recall that the transfer operators are related to the generators via Tt =e tL and
T ′ t =e tL′ . One might hope that
T ′ t =e tL′ =e t(L−⟨∇V,∇(·)⟩) ? =e tL ·e −t⟨∇V,∇(·)⟩ =T t ·e −t⟨∇V,∇(·)⟩.
However, since L and ⟨∇V,∇(·)⟩ do not commute in general (they do not share the same eigen-
structure), the exponential does not factorize, so the above equality does not hold. This fundamental
asymmetry between generator-level and transfer-operator-level perturbations explains why stan-
dard transfer operator learning methods–which rely on estimating covariance matrices of the form
E[z(X0)z(Xt)T]–cannot be straightforwardly debiased through importance weighting. The temporal
propagation encoded in the transfer operator obscures the simple additive structure available at the
generator level.
Radon-Nikodym derivative and importance weighting.Comparing the unbiased invariant mea-
sureπwith the biased measureπ ′, we obtain
dπ
dπ′ (x) = e−βU(x) /Z e−βU ′(x)/Z′ = e−βU(x) e−β(U(x)+V(x)) · Z ′ Z
=e βV(x) ·
R
X e−β(U(x)+V(x)) dxR
X e−βU(x) dx = eβV(x) R X eβV(x) dπ′(x) ,
where Z=
R
X e−βU(x) dx and Z ′ = R X e−βU ′(x)dx are normalization constants. This Radon- Nikodym derivative makes the distribution shift explicit.
For any function f∈L 1 π(X) , we can reweight expectations under π′ to recover expectations under π:
Ex∼π[f(x)] =E x′∼π′
 dπ
dπ′ (x′)f(x ′)

=E x′∼π′
"
eβV(x ′)
R
X eβV(x) dπ′(x) f(x ′)
#
.(36)
Defining the importance weightv(x) :=e βV(x) , this becomes
Ex∼π[f(x)] = 1 v Ex′∼π′[v(x′)f(x ′)],where v:=E x′∼π′[v(x′)].(37)
This importance weighting principle forms the foundation of our debiasing approach: quantities
involving the unbiased generator L and measure π can be estimated from biased trajectory data by
appropriately reweighting withv(x ′).
19

D Loss function derivation and spectral learning
In this section we discuss in detail the proposedrepresentation learningmethod to directly learn
the dominant eigenspace (slow modes) of the generator through a spectral objective based on its
resolvent.
Spectral theory of the resolvent.We begin by establishing the spectral-theoretic foundation for
our approach. Under standard confinement assumptions on the potential U, namely that U(x)≥
2α|x|21|x|≥R −c for some α >0 , R >0 , and c∈R (see Assumption(CP)), the generator L
admits a compact resolvent and a discrete spectrum. This follows from the compact embedding of the
Dirichlet form domain into L2 π(X) [15]. Consequently, L is self-adjoint on L2 π(X) with eigenvalue
decomposition
L=
X
i∈N0
λi ψi ⊗ψ i,
where 0 =λ 0 > λ1 ≥λ 2 ≥ · · · → −∞are the eigenvalues and (ψi)i∈N0 form an orthonormal basis
ofL 2 π(X). The resolvent operator
Rµ := (I−µ −1L)−1, µ >0,
is compact and self-adjoint, sharing the same eigenfunctions asLwith eigenvalues
νi := µ µ−λ i = 1 1−λ i/µ .(38)
Since λi ∈(−∞,0] for all i, we have νi ≥1 , with ν0 =µ (corresponding to the trivial constant
eigenfunction) andν i →0asi→ ∞. The spectral decomposition of the resolvent is thus
Rµ =
X
i∈N0
νi ψi ⊗ψ i.
Crucially, the largest eigenvalues ν0, ν1, . . . , νm of Rµ correspond to the smallest (in magnitude)
eigenvalues λ0, λ1, . . . , λm of L. These are precisely theslow modesthat dominate the long-time
dynamics and metastable structure of the system - the primary objects of interest in our learning
framework.
Best rank-(m+ 1)approximation.We seek a rank-(m+ 1)approximation ofR µ of the form
Rµ ≈Z θDθZ ∗ θ .(39)
Here, Zθ = (z θ 0, . . . , zθ m) :R m+1 → Wµ π denotes the injection operator defined by Zθu=Pm
j=0 ujzθ j , where (zθ j )m j=0 are neural network features parameterized by θ. The operator
Z ∗ θ :W µ π →R m+1 is the adjoint, given by (Z ∗ θ f) j =⟨(I−µ −1L)f, zθ j ⟩L2π(X) . Finally, Dθ =
diag(e−(dθ 0)2 , . . . , e−(dθ m)2 )collects the trainable eigenvalue parameters.
By the Eckart-Young-Mirsky theorem, for a compact self-adjoint operator A:W µ π → Wµ π with
eigenvalues(σ i)i∈N0 and eigenvectors(u i)i∈N0, the best rank-(m+ 1)approximation is:
min
rank(B)≤m+1
∥A−B∥ W µ π →W µ π =
A− mX i=0 σiui ⊗u i  W µ π →W µ π =σ m+1.(40)
This holds for any unitarily invariant norm. For the Hilbert-Schmidt norm ∥A∥2 HS(W µ π ) := P i σ2 i ,
the error is P i>m σ2 i . While compactness and (40) suffice theoretically, we use the Hilbert–Schmidt formulation because it admits a tractable reformulation via covariance matrices estimable from data.
Application to the resolvent.Since the resolvent Rµ is compact and self-adjoint in W µ π under our
confinement assumptions, the Eckart–Young–Mirsky theorem implies that its optimal rank-(m+ 1)
approximation in operator norm is
Rm µ =
mX
i=0
νiψi ⊗ψ i,(41)
with approximation error ∥Rµ −R m µ ∥W µ π →W µ π =ν m+1. This same truncation is also optimal for the Hilbert-Schmidt norm when Rµ has finite Hilbert-Schmidt norm in W µ π . Our neural network
parameterizationZ θDθZ ∗ θ is designed to recover this leading spectral subspace.
20

D.1 Population loss derivation
Hilbert-Schmidt formulation.Following [ 35], for compact operator Rµ we formulate the popula-
tion loss as:
Lα(θ) =vlim k→∞

∥PkRµ−ZθDθZ ∗ θ ∥2 HS(W µ π ) − ∥PkRµ∥2 HS(W µ π )

+α v∥Z ∗ θ Zθ −I∥ 2 F ,(42)
where v=E x′∼π′[eβV(x ′)] accounts for importance weighting. The first term measures the ap-
proximation error; subtracting the constant ∥Rµ∥2 HS(W µ π ) ensures the loss depends only on θ and
is minimized when ZθDθZ ∗ θ optimally approximates Rµ. The regularization term α∥Z ∗ θ Zθ −I∥ 2 F
enforces orthonormality in theW µ π metric.
Key challenge.The loss (42) cannot be directly computed because the resolvent is unknown and
computing the Hilbert-Schmidt norm would require all eigenfunctions {ψi}i∈N. The key insight is to
reformulate using covariance matrices estimable from trajectory data.
D.2 Reformulation via theW µ π inner product
TheW µ π inner product structure.Recall from Sec. 2 that theW µ π inner product is defined by:
⟨f, g⟩W µ π =⟨(I−µ −1L)f, g⟩L2π(X) =⟨f, g⟩L2π(X) − 1 µ ⟨f, Lg⟩L2π(X) .
For Langevin dynamics with generatorLf=−⟨∇U,∇f⟩+β −1∆f, integration by parts gives:
⟨f, g⟩W µ π =⟨f, g⟩L2 π(X) + 1 µβ ⟨∇f,∇g⟩ L2π(X) =E x∼π

f(x)g(x) + 1 µβ ∇f(x) T∇g(x)  .(43)
Computing Z ∗ θ Zθ via the weighted feature matrix.The operator Z ∗ θ Zθ :R m+1 →R m+1 has
matrix elements:
(Z ∗ θ Zθ)ij =⟨(I−µ −1L)zθ i , zθ j ⟩L2π(X) =⟨z θ i , zθ j ⟩W µ π .
Using (43):
(Z ∗ θ Zθ)ij =E x∼π

zθ i (x)zθ j (x) + 1 µβ ∇zθ i (x)T∇zθ j (x)  .(44)
Importance reweighting.Since we only have samples from π′, not π, we use the Radon-Nikodym
derivative dπ dπ′ (x) =e βV(x) /vwhere v= R eβV(x) dπ′(x). Definev(x) =e βV(x) . Then:
v(Z ∗ θ Zθ)ij =E x′∼π′

v(x′)

zθ i (x′)zθ j (x′) + 1 µβ ∇zθ i (x′)T∇zθ j (x′)  .(45)
Matrix formulation.Define the Jacobian matrix:
Jθ(x′) = [∂1zθ(x′)| · · · |∂dzθ(x′)]∈R (m+1)×d,
and the weighted feature matrix:
wθ(x′) = hp v(x′)zθ(x′) q v(x′) µβ Jθ(x′) i ∈R (m+1)×(d+1).
Then:
wθ(x′)wθ(x′)T = hp v(x′)zθ(x′) q v(x′) µβ Jθ(x′) i "p v(x′)zθ(x′)T q v(x′)
µβ Jθ(x′)T
#
=v(x ′)zθ(x′)zθ(x′)T + v(x′) µβ Jθ(x′)Jθ(x′)T.
The(i, j)-th element is:
[wθ(x′)wθ(x′)T]ij =v(x ′)zθ i (x′)zθ j (x′) + v(x′) µβ dX k=1 ∂kzθ i (x′)∂kzθ j (x′)
=v(x ′)

zθ i (x′)zθ j (x′) + 1 µβ ∇zθ i (x′)T∇zθ j (x′)  .
21

Comparing with (45) (noting the factorµ):
Wθ := vZ ∗ θ Zθ =E x′∼π′[wθ(x′)wθ(x′)T].(46)
ComputingZ ∗ θ RµZθ.The operatorZ ∗ θ RµZθ :R m+1 →R m+1 has matrix elements:
(Z ∗ θ RµZθ)ij =⟨(I−µ −1L)zθ i , Rµzθ j ⟩L2π(X) .
For anyf∈ Wµ π , the action ofZ ∗ θ Rµ is, for anyj∈ {0, . . . , m}:
(Z ∗ θ Rµf) j =⟨(I−µ −1L)zθ j , Rµf⟩ L2 π(X) =⟨z θ j , f⟩L2 π(X) =E x∼π[zθ j (x)f(x)].(47)
Therefore:
(Z ∗ θ RµZθ)ij =E x∼π[zθ i (x)zθ j (x)].
With importance reweighting (45):
Cθ := v Z∗ θ RµZθ =E x′∼π′[v(x′)zθ(x′)zθ(x′)T].(48)
D.3 Hilbert-Schmidt norm decomposition
We derive the reformulation of the Hilbert-Schmidt norm in terms of Wθ and Cθ. Expanding the
squared norm:
∥Rµ −Z θDθZ ∗ θ ∥2 HS(W µ π ) =∥R µ∥2 HS(W µ π ) +∥Z θDθZ ∗ θ ∥2 HS(W µ π ) −2⟨R µ, ZθDθZ ∗ θ ⟩HS(W µ π ).(49)
For the finite-rank operator A=Z θDθZ ∗ θ mapping to the (m+ 1) -dimensional subspace
span(zθ 0, . . . , zθ m):
∥ZθDθZ ∗ θ ∥2 HS(W µ π ) =
mX
j=0
∥ZθDθZ ∗ θ zθ j ∥2 W µ π =
mX
j=0
⟨DθZ ∗ θ zθ j , Z∗ θ ZθDθZ ∗ θ zθ j ⟩Rm+1
= tr[(DθZ ∗ θ Zθ)2] = v−2tr[(DθWθ)2],(50)
where we used the cyclic property of trace and Wθ = vZ ∗ θ Zθ.
Similarly, for the cross term:
⟨Rµ, ZθDθZ ∗ θ ⟩HS(W µ π ) = X
i∈N
⟨Rµψi, ZθDθZ ∗ θ ψi⟩W µ π = X
i∈N
⟨ψi, ZθDθZ ∗ θ ψi⟩L2π(X)
= tr[Z ∗ θ RµZθDθ] = v−1tr[CθDθ].(51)
Substituting into (49), multiplying by v, and adding the orthonormality regularization α∥Z ∗ θ Zθ −
I∥2 F =α v−2tr[(Wθ − vI) 2]yields:
Lα(θ) = tr

(DθWθ)2 −2 vD θ Cθ+α(Wθ−vI) 2 ,(52)
which is the loss presented in equation (7) of the main text.
D.4 Empirical loss estimation
Challenge of unbiased estimation.The population loss (52) involves products of expectations:
(DθWθ)2, vC θ, and (Wθ − vI) 2. Naively replacing expectations with sample means yields biased
estimators.
Solution 1: Sample splitting.Split the batch into two independent subsets bπ′ 1,bπ′ 2 of size
⌈b/2⌉ and ⌊b/2⌋. Define empirical covariances bW k θ =E x′∼bπ′ k [wθ(x′)wθ(x′)T], bC k θ =
Ex′∼bπ′ k [v(x′)zθ(x′)zθ(x′)T], and means bvk =E x′∼bπ′ k [v(x′)] for k∈ {1,2} . For independent
22

samples, E[(Dθ bW 1 θ)(Dθ bW 2 θ)] = (DθWθ)2, and similarly for other terms. Averaging cross-terms for
symmetry yields:
bLα(θ) = tr
h ( bW 1 θDθ bW 2 θDθ+ bW 2 θDθ bW 1 θDθ)
2 −bv1 bC 2 θDθ−bv2 bC 1 θDθ+α( bW 1 θ −bv1I)( bW 2 θ−bv2I) i .
(53)
This simplicity allows one to exclude the trivial eigenpair λ0=0 and ψ0=1 by centering the features
zθ(x′)on each batch, as proposed in transfer operator setting in [35].
Computational complexity:Computing bW k θ requires O((b/2)(m+ 1) 2d) operations for Jacobians
and outer products. Computing bC k θ requires O((b/2)(m+ 1) 2) operations. Matrix multiplications
require O((m+ 1)3) operations. Overall, the total computational cost is O  b(m+ 1)2d+ (m+ 1) 3 .
Solution 2: U-statistics (when centering features).Alternatively, constant features might be
hard-coded with fixed weights, or when needed, c.f. [ 17], learned from data. In these cases the
products of expectations in the loss (7) can be estimated from iid samples (x′ i)i∈[b] from π′ via
U-statistics estimator:
bLα(θ) = 1 b(b−1) X
i̸=j∈[b]

⟨Dθwθ(x′ i), wθ(x′ j)⟩2 F +αv(x′ i)v(x′ j)−2v(x′ i)v(x′ j)∥Dθzθ(x′ j)∥2
+α⟨wθ(x′ i), wθ(x′ j)⟩2 F −2α v(x′ i)∥wθ(x′ j)∥2 F  .(54)
Computational complexity:The double sum over i̸=j requires O(b2) evaluations. Each evaluation
computes inner products ⟨wθ(x′ i), wθ(x′ j)⟩F and norms at cost O((m+ 1)d). Total: O(b2(m+ 1)d).
Sample splitting is preferred for large batches (b≫m ), while U-statistics are better when the latent
dimension is large (m≫b).
Property Sample Splitting U-Statistics
Computational complexityO(bm 2d)O(b 2md)
Handles trivial eigenpair Yes Requires centering
Batch efficiency Better for largebBetter for largem
Table 5: Comparison of empirical loss estimation strategies.
D.5 Proof of Theorem D.1
Theorem D.1.Given a compact operatorR µ,µ >0, if for allθ∈Θ,(z θ i )m i=0 ⊆ W1 π′(X), then
E
 bLα(θ)  = v2 Lα(θ)≥ −Pm i=0 µ2v2 (µ−λi)2 ,(55)
where, if λm+1<λm equality holds iff span(ψi)m i=0 = span(z θ i )m i=0, or equivalently Pm =P θ,
with Pm and Pθ being the orthogonal projectors onto span(ψi)m i=0 and span(zθ i )m i=0, respectively.
Additionally, if α >0 at optimum Pm =P θ =Z θZ ∗ θ and λθ i =d θ i , 0≤i≤m , up to the ordering
of indices.
Proof. We prove the theorem in four steps: (1-2) establish the lower bound using Eckart-Young-
Mirsky and taking the limit k→ ∞, (3) characterize when equality holds, and (4) verify unbiasedness
of the empirical estimator.
Step 1: Lower bound via Eckart-Young-Mirsky.Let Pk :W µ π → Wµ π be the orthogonal projector
onto the span of the firstkeigenfunctions{ψ 0, . . . , ψk−1}ofR µ. Consider the truncated loss:
Lk(θ)=v  ∥PkRµ−ZθDθZ ∗ θ ∥2 HS(W µ π )−∥PkRµ∥2 HS(W µ π )  .(56)
23

By the Eckart-Young-Mirsky theorem, for anyk > m, the best approximation to PkRµ in Hilbert–
Schmidt norm is obtained by retaining its largest m+ 1 eigenvalues, namely Pm+1Rµ whose spectral
decomposition isP m+1Rµ = Pm i=0 νiψi ⊗ψ i, whereν i =µ/(µ−λ i). Therefore:
Lk(θ)≥ v  ∥Pm+1Rµ −P kRµ∥2 HS(W µ π ) − ∥PkRµ∥2 HS(W µ π ) 
= v
 k−1X
i=m+1
ν2 i −
k−1X
i=0
ν2 i
!
=− v
mX
i=0
ν2 i =−
mX
i=0
µ2v
(µ−λ i)2 .(57)
Step 2: Taking the limitk→ ∞.Expanding the Hilbert-Schmidt norm inL k via the trace:
Lk(θ) = v  ∥ZθDθZ ∗ θ ∥2 HS(W µ π ) −2⟨Z θDθZ ∗ θ , PkRµ⟩HS(W µ π ) 
= v

∥ZθDθZ ∗ θ ∥2 HS(W µ π ) −2⟨Z θDθZ ∗ θ , Rµ⟩HS(W µ π )

+ 2v⟨ZθDθZ ∗ θ ,(I−P k)Rµ⟩HS(W µ π )
=L(θ) + 2 v⟨ZθDθZ ∗ θ ,(I−P k)Rµ⟩HS(W µ π ),(58)
whereL(θ)is the loss without the subtracted constant term (i.e., the first two terms in (4)).
By the Hölder inequality for the Hilbert-Schmidt inner product:
|L(θ)− Lk(θ)| ≤2vtr(Z θDθZ ∗ θ )∥(I−P k)Rµ∥
= 2tr(W θDθ)νk+1.(59)
Since zθ i ∈ Wµ π for all i∈ {0, . . . , m}by assumption, we have tr(WθDθ)<∞ . Moreover,
λk → −∞ask→ ∞, and, hence
lim
k→∞
Lk(θ) =L(θ).
Taking the limit in (57) and noting that Lα(θ)≥ L(θ) (since the orthonormality penalty is non-
negative), we obtain:
Lα(θ)≥ −
mX
i=0
µ2v
(µ−λ i)2 .(60)
Step 3: Characterizing equality.Equality in (55) requires:
1.L α(θ) =L(θ) , which implies the orthonormality penalty vanishes: ∥Z ∗ θ Zθ −I∥ 2 F = 0, so
Z ∗ θ Zθ =I.
2.L(θ) =− Pm i=0 µ2v (µ−λi)2 .
By the Eckart-Young-Mirsky theorem, condition (2) holds if and only if ZθDθZ ∗ θ equals the optimal
rank-(m+ 1) approximation Pm+1Rµ = Pm i=0 νiψi ⊗ψ i. Combined with condition (1), this means:
span(zθ 0, . . . , zθ m) = span(ψ0, . . . , ψm),
or equivalentlyP θ =P m+1.
If additionally α >0 and νm+1 < νm (i.e., λm+1 < λm, ensuring a spectral gap), then the optimal
rank-(m+ 1) approximation is unique. In this case, the orthonormality constraint Z ∗ θ Zθ =I
implies that {zθ i }m i=0 form an orthonormal basis of span(ψ0, . . . , ψm), and the eigenvalues satisfy
e−(dθ i )2 =ν i, i.e.,d θ i = √−logν i, up to reordering.
Step 4: Unbiasedness of empirical estimator.We now show that E[ bLα(θ)] = v2Lα(θ). Recall the
empirical loss (8):
bLα(θ) = tr
h
( bW 1 θDθ bW 2 θDθ+ bW 2 θDθ bW 1 θDθ)/2−bv1 bC 2 θDθ−bv2 bC 1 θDθ+α( bW 1 θ −bv1I)( bW 2 θ−bv2I) i .
24

Sincebπ′ 1 andbπ′ 2 are independent samples fromπ ′, we have:
E[ bW 1 θDθ bW 2 θDθ] =E[ bW 1 θ]DθE[ bW 2 θ]Dθ = (DθWθ)2,
E[bv1 bC 2 θ] =E[bv1]E[bC 2 θ] = vC θ
E[bv2 bC 1 θ] =E[bv2]E[bC 1 θ] = vC θ,
E

( bW 1 θ −bv1I)( bW 2 θ −bv2I)  = (E[ bW 1 θ]− vI)(E[ bW 2 θ]− vI) = (W θ − vI) 2,
Therefore:
E[ bLα(θ)] = tr  (DθWθ)2 −2 vD θCθ +α(W θ − vI) 2 = v2Lα(θ).
D.6 Extension to general compact operators
The formulation (42) requires Rµ to be Hilbert–Schmidt in W µ π for the norm ∥Rµ∥2 HS(W µ π ) to be finite.
However, the equivalent form (52) expressed via covariance matrices Wθ and Cθ is well-defined
whenever Rµ is compact (guaranteed by confinement) and the neural network features (zθ j )m j=0 and
their gradients are in W µ π (guaranteed by Assumption(BE)). This broader applicability is crucial since
compactness(rather than Hilbert–Schmidt) is the natural condition ensured by standard confinement
assumptions on the potential (Assumption(CP)). Indeed the covariance matrices Wθ and Cθ involve
only W µ π -inner products between finitely many neural network features (always finite if features are
in W µ π ) and expectations under π′ of bounded functions (bounded by Assumption(BE)). Crucially,
no infinite sums or traces over the full spectrum of Rµ appear in (52), unlike in (42). Therefore, the
covariance formulation extends naturally to all compact operators.
D.7 Resolvent estimation in a given representation.
Finally, we remark that our approach, defined by equations (12) and (13), differs fundamentally from
regression-based methods that minimize the Hilbert-Schmidt approximation error of the resolvent
(see in particular equation (16) in [16]). In spirit our approach is closer to CCA approaches [? 35, 59]
based on L2 π geometry. However, a key novelty is that here we work in the Dirichlet energy spaceW µ π .
This change of norm is instrumental in controlling gradient errors of the observables, and providing
sharp finite sample guarantees for the estimation of the drift.
E Statistical bounds
E.1 Preliminaries: some concentration bounds
Useful concentration inequalities.All the statistical bounds we present will relay on two versions
of Bernstein inequality. The first one is Pinelis and Sakhanenko inequality for random variables in a
separable Hilbert space, see [see e.g. 9, Proposition 2].
Proposition E.1.Let Ai, 1≤i≤n be i.i.d copies of a random variable A in a separable Hilbert
space with norm ∥·∥. If there exist constants Λ>0 and σ >0 such that for every m≥2 ,
E∥A∥m ≤ 1 2 m!Λm−2σ2, then with probability at least1−δ,  1 n nX i=1 Ai −EA  ≤ 4 √ 2√n log 2 δ r σ2 + Λ2 n .(61)
We also recall that a version of the non-commutative Bernstein inequality for bounded matrices. See
for instance [57].
Proposition E.2(Matrix Bernstein).Let Zi, 1≤i≤n be independent random matrices with
common dimensiond 1 ×d 2. Assume thatEZ i = 0and∥Z i∥ ≤cfor each indexi. Define the sum
¯Z= 1 n
nX
i=1
Zi.
25

Letσ 2 Z be the matrix variance statistic:
σ2 Z = max
( 1 n nX i=1 E[ZiZ ∗ i ]  ,  1 n nX i=1 E[Z ∗ i Zi]  ) .
Then with probability at least1−δ:
∥ ¯Z∥ ≤
r
2σ2 Z L(δ) n + c 3 L(δ) n ,
whereL(δ) = log d1+d2 δ .
Furthermore, the expectation satisfies:
E∥ ¯Z∥ ≤
r
2σ2 Z log(d1 +d 2) n + c 3 log(d1 +d 2) n .
Key concentration results.Our proofs of the statistical guarantees rely on the following concentra-
tion results.
Proposition E.3.Let ess supx′∼π′ |∂kzθ j (x′)| ≤τ <∞, for all k= 0, . . . , dand 0≤j≤m , with
the convention ∂0zθ =z θ, let ∥V∥ ∞ <∞ , and denote cθ := 2(m+ 1)τ 2(1 +d/(µβ))e β∥V∥ ∞.
Givenδ >0, with probability in the i.i.d. draw of(x ′ i)n i=1 fromπ ′, it holds that
P
n
∥W−1/2 θ ( bWθ −W θ)W−1/2 θ ∥ ∨ ∥W−1/2 θ (bCθ −C θ)W−1/2 θ ∥ ≤ Em,n(δ) o ≥1−δ,(62)
where
Em,n(δ) = 2(cθ+1) 3n ln 2m+ 2 δ +
r
2(cθ−1)
n ln 2m+ 2 δ .(63)
Moreover,
P

∥W1/2 θ bW −1 θ W1/2 θ ∥ ≤ 1 1− Em,n(δ)  ≥1−δ.(64)
Proof. The idea is to apply Proposition E.2 for operator A(x′) = [W−1/2 θ wθ(x′)]⊗[W −1/2 θ wθ(x′)], where
wθ(x′) = h zθ(x′)

 1√µβ ∂1zθ(x′)

 . . .

 1√µβ ∂dzθ(x′) i eβV(x ′)/2 ∈R (m+1)×(d+1) (65)
First, note that we have Ex′∼π′[A(x′)] =I and that under the assumptions on boundedness we
have that ∥A∥∞ :=ess sup x′∼π′∥A(x′)∥ ≤2(m+ 1)τ 2(1 +d/(µβ))e β∥V∥ ∞ =c θ, whenever
∥Wθ −I∥ 2 <1/2 . Next, since A(x′) is symmetric positive semidefinite, we have A(x′)2 ⪯
∥A∥∞ A(x′). Consequently,
(A(x′)−I) 2 =A(x ′)2 −2A(x ′) +I⪯(∥A∥ ∞ −2)A(x ′) +I.
Then, usingE[A(x ′)] =Iyields
E

(A(x′)−I) 2 ⪯(∥A∥ ∞ −1)I.
Hence, the matrix variance statistic satisfies
σ2 Z =∥E[Z 2 i ]∥ ≤ ∥A∥∞ −1.
Applying then the Proposition E.2 with d1 =d 2 =m+ 1 , we obtain that, with probability at least
1−δ,
 1 n nX i=1 A(x′ i)−I  ≤ r 2(cθ −1) n log  2(m+ 1) δ  + cθ + 1 3n log  2(m+ 1) δ  .
To obtain the same for bCθ −C θ, it suffices to observe that zθ(·)⊗z θ(·)⪯w θ(·)⊗w θ(·), and, hence
(62) follows from union bound.
26

To complete the proof, observe that
∥I−W −1/2 θ bWθW−1/2 θ ∥=∥W −1/2 θ (Wθ − bWθ)W−1/2 θ ∥ ≤ Em,n(δ),
and, hence forE m,n(δ)smaller than one we obtain
∥W1/2 θ bW −1 θ W1/2 θ ∥=∥(W −1/2 θ bWθW−1/2 θ )−1∥ ≤ 1 1− ∥I−W−1/2 θ bWθW−1/2 θ ∥ .
Proposition E.4.Given x′ ∈R d, let ξ(x′) =  zθ(x′)(x′)T + 1 µβ Jθ(x′)  eβV(x ′) ∈R (m+1)×d,
where the Jacobian of features is denoted by Jθ(x′) = [∂ 1zθ(x′)|. . .|∂dzθ(x′)]. Let
ess supx′∼π′ |∂kzθ j (x′)| ≤τ <∞ , for all k∈ {0, . . . , d}and j∈ {0, . . . , m}, with the con-
vention ∂0zθ =z θ, let ∥V∥ ∞ <∞ and ∥Wθ/v−I∥<1/2 . Assume that the potential U ′ is
sufficiently confining such that x′ ∼π ′ is K-sub-Gaussian with K∈(0,∞) . Given δ >0, with
probability in the i.i.d. draw of(x ′ i)n i=1 fromπ ′, it holds that
P
(
∥W−1/2 θ
h
1
n
nX
i=1
ξ(x′ i)−E x′∼π′ξ(x′) i ∥Rm+1→Rd ≤ E ′ m,n(δ)/ √ v ) ≥1−δ,(66)
where
E
′
m,n(δ)=Cτ eβ∥V∥ ∞ max ns min(m+ 1, d) µ2β2 r log((m+d+ 1)/δ) n + log((m+d+ 1)/δ) n  ,
r
m+ 1
n
r
E[∥x′∥2 2] + Kd n log 2 δ o ,
(67)
for a large enough absolute constantC >0.
Proof. Recalling ξ(x′) =  zθ(x′)(x′)T + 1 µβ Jθ(x′)  eβV(x ′) ∈R (m+1)×d, where the Jacobian of
features is denoted by Jθ(x′) = [∂ 1zθ(x′)|. . .|∂dzθ(x′)]. For brevity we set ∥·∥=∥·∥ Rm+1→Rd
and∥·∥ 2 =∥·∥ l2(Rm+1). We have
W−1/2 θ ξ(x′) =e βV(x ′)W−1/2 θ zθ(x′)(x′)T | {z }
=: ¯A
+e βV(x ′) 1 µβ W−1/2 θ Jθ(x′) | {z }
=: ˜A
.
We note that for anyt 1, t2 >0witht=t 1 +t 2, we have
P

∥
X
i
Ai∥> t
!
≤P

∥
X
i
¯Ai∥> t1
!
+P

∥
X
i
˜Ai∥> t2
!
.
We will control∥ P i ¯Ai∥and∥ P i ˜Ai∥separately.
Uniform bound on ∥P i ˜Ai∥.Note that under the boundedness assumption on the entries of zθ(x′)
and its partial derivatives we have ess supx′∼π′∥Jθ(x′)∥ ≤τ p min(m+ 1, d). Hence we get the
followingπ ′-almost surely upper bound on the Frobenius norm of ˜A:
∥ ˜A∥= eβV(x ′ ) µβ ∥W−1/2 θ Jθ(x′)∥ ≤eβV(x ′ ) µβ ∥W−1/2 θ ∥∥Jθ(x′)∥ ≤τ r 2 min(m+ 1, d) v eβ∥V∥ ∞ ,
(68)
where we have used that ∥Wθ/v−I∥<1/2 , implying that ∥W−1/2 θ ∥ ≤ √ 2/ √ v. Indeed, using that
∥A−1/2∥= 1/ p λmin(A)≤1/ p 1− ∥I−A∥withA=W θ/v, we get
∥W−1/2 θ ∥ ≤ 1p v(1− ∥Wθ/v−I∥) ≤ 1p v(1−1/2) = √ 2/ √ v.
27

We define the random matrix
Zi := eβV(x ′ i ) µβ W−1/2 θ Jθ(x′ i)−E h eβV(x ′) µβ W−1/2 θ Jθ(x′) i ∈R (m+1)×d.
Then E[Zi] = 0 and in view of (68), we have ∥Zi∥ ≤2
√
2τ
p
min(m+ 1, d)/v eβ∥V∥ ∞ µβ =:c , π′-a.s.
Since Zi is not square, we need to use the non-commutative Bernstein matrix concentration inequality
for rectangular matrices.
Left covariance operator.We haveZ i ∈R (m+1)×d, soZ iZ ∗ i ∈R (m+1)×(m+1). Also
E[ZiZ ∗ i ] =E h e2βV(x ′ i ) µ2β2 W−1/2 θ Jθ(x′ i)Jθ(x′ i)∗W−1/2 θ i
−E
h
eβV(x ′ i )
µβ W−1/2 θ Jθ(x′ i) i E h eβV(x ′ i ) µβ Jθ(x′ i)∗W−1/2 θ i .
Hence
E[ZiZ ∗ i ]⪯E
"
e2βV(x ′)
µ2β2 W−1/2 θ Jθ(x′)Jθ(x′)∗(W−1/2 θ )∗
#
= e2β∥V∥ ∞
µ2β2 W−1/2 θ E[Jθ(x′)Jθ(x′)∗]W−1/2 θ ⪯ e2β∥V∥ ∞ µβ Im+1 =:V L,
where we used 1 µβ Ex′∈π′[Jθ(x′)Jθ(x′)∗] =W θ −C θ ⪯W θ .
Right covariance operator.Similarly,Z ∗ i Zi ∈R d×d and:
E[Z ∗ i Zi]⪯E
"
Jθ(x′)∗(W−1/2 θ )∗ e2βV(x ′) µ2β2 W−1/2 θ Jθ(x′) # (69)
= e2β∥V∥ ∞
µ2β2 E[Jθ(x′)∗W−1 θ Jθ(x′)] :=V R.(70)
Note that
∥VL∥= e2β∥V∥ ∞
µ2β2 ,∥V R∥ ≤2e2β∥V∥ ∞ µ2β2v τ 2 min(m+ 1, d).
Defineσ 2 Z := max(∥VL∥,∥V R∥). Sinceτ≥1, we have∥V L∥ ≤ ∥VR∥, and consequently:
σ2 Z = 2 e2β∥V∥ ∞
µ2β2v τ 2 min(m+ 1, d).(71)
Final concentration bound.With probability at least1−δ:
 1 n nX i=1 Zi  ≤ r 2σ2 Z L(δ) n + c 3 L(δ) n
≤2
√
2τ
p
min(m+ 1, d)eβ∥V∥ ∞
vµβ
r log((m+d+ 1)δ −1)
n + log((m+d+ 1)δ −1) 3n  (72)
Uniform bound on∥ P i ¯Ai∥.Since ¯Ais of rank one, we have∥ ¯A∥F =∥ ¯A∥and consequently:
∥ ¯A∥F =∥ ¯A∥=∥W −1/2 θ zθ(x′)(x′)TeβV(x ′)∥
≤ ∥W−1/2 θ zθ(x′)(x′)T∥eβV(x ′)
≤e βV(x ′)∥W−1/2 θ zθ(x′)∥2∥x′∥2
≤
√
2
v eβV(x ′)∥zθ(x′)∥2∥x′∥2,
28

where we have used that ∥W−1/2 θ zθ(x′)∥2 ≤ ∥W−1/2 θ ∥∥zθ(x′)∥2 and ∥W−1/2 θ ∥ ≤ √ 2/v. Note that under the boundedness assumption on the entries of zθ(x′), we have ess supx′∼π′∥zθ(x′)∥2 ≤
τ √m+ 1. Hence we get the followingπ ′-almost surely bound:
∥ ¯A∥F ≤τ
r
2(m+ 1)
v eβ∥V∥ ∞ ∥x′∥2.(73)
Moment condition on ∥ ¯A∥.We need to verify that there exist constants Λ>0 and σ2 >0 such
that for everyp≥2:
E[∥ ¯A∥p F ]≤ 1 2 p!Λp−2σ2.(74)
From (73), we have
E[∥ ¯A∥p F ]≤E h τ √ m+ 1e β∥V∥ ∞ ∥x′∥2 pi = (τ √ m+ 1e β∥V∥ ∞ )pE[∥x′∥p 2].(75)
Since x′ ∼π ′ is K-sub-Gaussian, we have for any unit vector u∈R d, E[et⟨u,x′⟩]≤e K2t2/2, for all
t∈R. This implies that∥x ′∥2 isK √ d-sub-Gaussian.
Consequently, for the moments of∥x ′∥2, we use Cauchy-Schwarz forp≥2:
E[∥x′∥p 2] =E[∥x ′∥2 2 · ∥x′∥p−2 2 ]≤(E[∥x ′∥4 2])1/2(E[∥x′∥2(p−2) 2 ])1/2.(76)
Since ∥x′∥2 is K √ d-sub-Gaussian, by equivalence of moments for sub-Gaussian random variables,
we have: (E[∥x′∥4 2])1/2 ≲E[∥x ′∥2 2], where the implicit constant is absolute. For higher-order
moments with p≥2 , the standard sub-Gaussian moment bound gives for some absolute constant
C >0:
E[∥x′∥p 2]≤C(K √ d)pp p!.(77)
Combining these, there exists an absolute constantC ′ >0such that forp≥2:
E[∥x′∥p 2]≤C ′E[∥x′∥2 2]·(K √ d)p−2p (p−2)!.(78)
For the moment condition (74), we substitute:
E[∥ ¯A∥p F ]≤C  τ r m+ 1 v eβ∥V∥ ∞ p E[∥x′∥2 2]·(K √ d)p−2p (p−2)!.(79)
Hence we observe that the moment condition is satisfied with
Λ =C ′τ eβ∥V∥ ∞
r
K(m+ 1)d
v , σ 2 =C ′τ 2e2β∥V∥ ∞ (m+ 1) v E[∥x′∥2 2],(80)
for an appropriate absolute constantC ′ >0.
Step 3: Application of concentration inequality.Applying Proposition E.1 with the verified
moment condition, we obtain with probability at least1−δ:
 1 n nX i=1 ¯Ai −E[ ¯A]  F ≤ 4 √ 2√n log 2 δ r σ2 + Λ2 n .(81)
Therefore, there exists an absolute constantC >0, such that w.p.a.l.1−δ,
 1 n X i ¯Ai −E[ ¯A]  F ≤ E ′ m,n(δ)/ √ v:=C τ eβ∥V∥ ∞ r m+ 1 vn r E[∥x′∥2 2] + Kd n log 2 δ .(82)
29

Estimation of v.We derive an elementary concentration inequality for the estimation of the
renormalizing constant v.
Lemma E.5(Relative error bound).Let v(x) =e β·V(x) where ∥V∥ ∞ <∞ . Let x1, . . . , xn be i.i.d.
samples from distributionµonX, and define:
v=E x∼µ[v(x)],bv= 1 n
nX
i=1
v(xi).
Letσ 2 =Var(v(x)). Then with probability at least1−δ:

 bv−v v

 ≤ σ v r 2 log(2/δ) n + eβ∥V∥ ∞ log(2/δ) 3nv =:E ′′ n (δ).
Proof. Let vi =v(x i)− v. Then E[vi] = 0, |Wi| ≤eβ∥V∥ ∞ a.s., and Var(Wi) =σ 2. By Bernstein’s
inequality:
P
(

 nX i=1 vi

 ≥t ) ≤2 exp  − t2/2 σ2n+e β∥V∥ ∞ t/3  .
Setting the right side equal toδand solving fortyields
t=σ
p
2nlog(2/δ) + eβ∥V∥ ∞ log(2/δ) 3 .
Dividing byn vgives the result.
E.2 Assumptions (BE), (CP) and (RA): discussion
Before presenting the proofs for resolvent (App. E.3), generator (App. E.4), and gradient estimation
(App. E.5), we briefly discuss the assumptions used throughout the analysis, namely(BE),(CP)and
(RA).
Bounded embeddings: (BE)There exist τ≥1 such that ess supx′∼π′ |∂kzθ j (x′)| ≤τ <∞ ,
∀k= 0, . . . , dand∀j= 0, . . . , m, with the convention∂0zθ =z θ.
Assumption(BE)requires then uniform boundedness of the embedding functions (zθ j )m j=0 and their
first-order derivatives under the biased sampling distributionπ′. This condition ensures finite variance
of empirical spectral and gradient estimators and allows uniform concentration over basis indices and
coordinates. It is satisfied by many standard choices of embeddings, including truncated trigonometric
bases, bounded neural feature maps, or other smooth finite-dimensional representations.
When the dynamics evolve on acompact manifold, such as the sphere Sd−1, this assumption can be
substantially relaxed. Indeed, compactness implies that any continuous embedding is automatically
bounded, and any C 1 embedding has bounded (intrinsic) first derivatives. Consequently, for spherical
Langevin dynamics, a(BE)-type condition holds automatically for any fixed truncation level m,
provided the embeddings areC 1 on the manifold.
Confining potential: (CP)The potential U satisfies U(x)≥2α∥x∥ 21{∥x∥≥R} −c , ∀x, for some
α >0,R >0,c∈R, and the bias obeys∥V∥ ∞ <∞.
Assumption(CP)ensures stability and the existence of an invariant distribution for Langevin dynamics
in Euclidean space. The quadratic lower bound on U outside a compact set guarantees exponential
tail decay of the invariant measure, implying finite moments of all orders. This integrability is
essential when working withbiased samples, as it ensures that reweighting by a bounded bias does
not lead to ill-conditioned estimators. Together with boundedness of the bias V , this assumption
yields equivalence between the biased and unbiased measures, ergodicity of the dynamics, and
consistency of empirical averages. Furthermore, crucially,(CP)implies that x∼π and x′ ∼π ′ are
K-sub-Gaussian with K 2 ≲(βα) −1, allowing one to derive concentration bounds for the gradient
estimation.
In contrast, spherical Langevin dynamics evolve on a compact state space. Compactness prevents
escape to infinity and ensures the existence of an invariant distribution under much weaker conditions.
In this setting, no confining growth of U is required; it suffices that the target density is well-defined
with respect to the surface measure and that the drift is sufficiently regular.
Gradient regularity: (RA) ∃p≥1 such that ∀k∈[d] , ∥∂kU∥ W µ,p π <∞ , that is ∥∇U∥ W µ,p π <∞ .
30

Assumption(RA)requires the gradient of the potential to belong to a Sobolev space W µ,p π for some
p≥1 . This ensures that ∇U is well-defined in a weak sense and has finite p-th moments under
the invariant distribution. The condition is used to control the bias–variance trade-off in gradient
estimation and to establish stability and convergence of the resulting gradient-based dynamics.
Importantly, it does not require global Lipschitz continuity or pointwise smoothness, and is therefore
compatible with nonconvex or moderately rough potentials.
E.3 Resolvent estimation
As a reminder, bCθ and bWθ are the empirical counterparts of the covariance matrices associated to
the parametrized features Cθ = vZ ∗ θ RµZθ and Wθ = vZ ∗ θ Zθ, where Zθ :R m+1 → Wµ π (X) is the
(parametrized) injection operators. Further we note that for Em(θ)<1 , Wθ is invertible implying
that
√
vZθW−1/2 θ is a partial unitary operator, that is [ √ vZθW−1/2 θ ]∗√ vZθW−1/2 θ =I , and, hence, partial isometry.
Let Nθ =W −1 θ CθW−1 θ and Qθ =W −1/2 θ CθW1/2 θ , and further denote cMθ =W 1/2 θ bW −1 θ W1/2 θ and
bNθ = bW −1 θ bCθ bW −1 θ . Recall that Pθ = vZθW−1 θ Z ∗ θ is the orthogonal projector on Hθ :=H Zθ and
HZθ is the space spanned by the set of basis functions zθ j :X →R, j∈ {0, . . . , m}. Let Pm be the
spectral projector associated with the set{0, . . . , m}. Using that
∥P ⊥ θ PmRµ∥W µ π →W µ π ∨ ∥PθP ⊥ m Rµ∥W µ π →W µ π ≤(1∨ν m+1)∥Pθ −P m∥W µ π →W µ π ≤ Em(θ),
sinceν j ∈(0,1)for anyj≥0, we get
∥Rm µ − vZθNθZ ∗ θ ∥W µ π →W µ π =∥(P θ +P ⊥ θ )(Rm µ − vZθNθZ ∗ θ )(Pθ +P ⊥ θ )∥W µ π →W µ π
≤3∥P ⊥ θ Rm µ ∥W µ π →W µ π +∥P θRm µ Pθ − vZθNθZ ∗ θ ∥W µ π →W µ π
≤3∥P ⊥ θ Rm µ ∥W µ π →W µ π +∥P θP ⊥ m Rµ∥W µ π →W µ π
+∥P θRµPθ − vZθNθZ ∗ θ ∥W µ π →W µ π (83)
≤(3 +ν m+1)Em(θ)+∥PθRµPθ − vZθNθZ ∗ θ ∥W µ π →W µ π (84)
≤4E m(θ),(85)
where we have used in the last line thatP θRµPθ = vZθNθZ ∗ θ and thatν m+1 ≤1.
Next, recalling Wθ = vZ ∗ θ Zθ and using the partial isometry property we have
∥vZθNθZ ∗ θ − vZθ bNθZ ∗ θ ∥W µ π →W µ π =∥W 1/2 θ [Nθ − bNθ]W1/2 θ ∥(86)
=∥W −1/2 θ CθW−1/2 θ − cMθ[W−1/2 θ bCθW−1/2 θ ] cMθ∥
≤ ∥I−cMθ∥(1 +∥ cMθ∥) +∥ cMθ∥2∥W−1/2 θ [bCθ −C θ]W−1/2 θ ∥, (87)
where we obtain the second line by adding and subtracting terms Qθ cMθ and cMθQθ cMθ, and using
that∥Q θ∥ ≤1. But since,
∥I− cMθ∥=∥I−W 1/2 θ bW −1 θ W1/2 θ ∥
=∥W 1/2 θ W−1 θ W1/2 θ −W 1/2 θ bW −1 θ W1/2 θ ∥
=∥W 1/2 θ W−1 θ ( bWθ −W θ) bW −1 θ W1/2 θ ∥=∥W −1/2 θ ( bWθ −W θ)W−1/2 θ W1/2 θ bW −1 θ W1/2 θ ∥
≤ ∥W−1/2 θ ( bWθ −W θ)W−1/2 θ ∥∥ cMθ∥,
we conclude
∥vZθNθZ ∗ θ − vZθ bNθZ ∗ θ ∥W µ π →W µ π ≤ ∥cMθ∥ h ∥ cMθ∥∥W−1/2 θ (bCθ−Cθ)W−1/2 θ ∥
+ (1+∥cMθ∥)∥W−1/2 θ ( bWθ−Wθ)W−1/2 θ ∥ i .
Finally, we observe that∥ vZθNθZ ∗ θ ∥W µ π →W µ π ≤1implies
∥vZθ bNθZ ∗ θ −bvZθ bNθZ ∗ θ ∥W µ π →W µ π ≤ |bv−v| v  1 +∥ vZθNθZ ∗ θ − vZθ bNθZ ∗ θ ∥W µ π →W µ π  .
31

By Lemma E.5, we have |bv−v|/v≤ E
′′
n (δ). Combining this with the above bounds and Proposition
E.3, we conclude that, forE m,n(δ)≤1/3, the following holds with probability at least1−2δ:
∥Rm µ −bvZθ bNθZ ∗ θ ∥W µ π →W µ π ≤4E m(θ) + 6E m,n(δ) + 3E ′′ n (δ).(88)
We can think of the empirical estimation of the spectral decomposition ofRµ as a two step perturbation
scheme, where each steps originates from the corresponding learning scheme of LITL.
In the first phase we learn representations, yielding that the spectral decomposition of Rµ is approxi-
mated by the one of PθRµPθ, which, using the properties of low rank eigenvalue problems [55], is
characterized by the definite generalized eigenvalue problem Cθuθ i =ν θ i Wθuθ i and [uθ i ]T Wθuθ i = v,
0≤i≤m, where normalized eigenfunctions of PθRµPθ are given by ψθ i =Zθuθ i . On the other hand,
in the second phase perturbations are induced by replacing Wθ and Cθ by their empirical counter-
parts. So, to control these errors and obtain the final spectral bounds, we use the following standard
perturbation result on definite matrix pencils.
Theorem E.6([ 55]).Let A and B be compact self-adjoint operators on a Hilbert space, with B pos-
itive definite. Consider the generalized eigenvalue problem Ax=λBx with eigenvalues λ1≤λ2≤ · · ·
and corresponding B-orthonormal eigenvectors x1, x2, . . .satisfying xT i Bxj=δij. Let bA and bB be
self-adjoint perturbations, and denote ∆A= bA−A and ∆B= bB−B. If ∥∆B∥<|B −1∥−1, then for
eigenvalues bλi and bB-orthonormal eigenvectors bxi of the generalized eigenvalue problem bAbx=bλ bBbx
the following bounds hold.
1.Eigenvalue perturbation:For everyi∈N 0,
|λi − bλi| ≤∥∆A∥+λ i∥∆B∥ ∥B−1∥−1 − ∥∆B∥.
2. Eigenvector perturbation:Let X and bX be invariant subspaces corresponding to eigenval-
ues λi1 , . . . , λik and bλi1 , . . . ,bλik, respectively. Define the gap gap{i1,...,ik} = min  |µ−
λij |:µ∈Sp(B −1A)\ {λi1 , . . . λik }j∈[k] 	 , and assume gap{i1,...,ik} >0 . Let ΘB be
theB-based angles betweenXand bXand∥∆A∥ ∧ ∥∆B∥ ≤ε. Then
∥sin ΘB∥≤ ∥∆A∥+ (max j |λij |)∥∆B∥ gap{i1,...,ik}  ∥B−1∥−1−∥∆B∥  ,
and, consequently,
∥x−bx∥B≤
√
2(1 +|λ|)ε
gap{i1,...,ik}

∥B−1∥−1−ε  +O(ε2).
First, recalling (83), we apply the above result in the spaceW µ π when∆B= 0and obtain
|νθ i −ν i| ≤3Em(θ)and∥ψ θ i −ψ i∥W µ π →W µ π ≤ 3E m(θ) gapi ,(89)
where gapi = minν∈Sp(Rµ)\{i} |ν−ν i|
Next, relying on the Proposition E.3 and, as before assuming Em(θ)≤1/2 and Em,n(δ)≤ v/3, we
have that∥W −1 θ ∥−1 ≥ v/2and w.p.a.l.1−δ
|νθ i −bνi|
1 +ν θ i ≤ 6E m,n(δ) v and∥u θ i / √ v−bui/ √ bv∥Wθ ≤ 6 √ 2E m,n(δ) v(gapi −3E m(θ)) (1 +ν θ i ).(90)
Recalling that
√
vZθW−1/2 θ is partial isometry, we have
∥uθ i / √ v−bui/ √ bv∥Wθ = √ v∥Zθ[uθ i / √ v−bui/ √ bv]∥W µ π →W µ π =∥ψ θ i − bψi √ v/ √ bv∥W µ π →W µ π
32

and, hence
∥ψθ i − bψi∥W µ π →W µ π ≤ 6
√
2E m,n(δ)
v(gapi −3E m(θ)) (1 +ν θ i ) + (1 +∥ψ θ i − bψi∥W µ π →W µ π )

1− q v bv

.
Now, assuming thatE
′′
n (δ)≤1/2, we have that|1−
√
v/
√
bv| ≤ E
′′
n (δ), and we conclude
∥ψθ i − bψi∥W µ π →W µ π ≤ 12
√
2 (1 +ν θ i )
v(gapi −3E m(θ)) Em,n(δ) + 2E
′′
n (δ).(91)
Finally, collecting (89), (90) and (91) we have shown that
|bνi −ν i|≤3(Em(θ)+2E m,n(δ)/v)(92)
and
∥ bψi−ψi∥W µ π →W µ π ≤ 3E m(θ) gapi + 12
√
2 (2+3Em(θ))
v(gapi−3E m(θ)) Em,n(δ)+2E
′′
n (δ).(93)
E.4 Generator estimation
Start by observing that
bQθ = bW −1/2 θ bCθ bW −1/2 θ = 1 bv mX i=0 bνi bW 1/2 θ buibuT i bW 1/2 θ ,
which, if allbνi >0, implies that
bL=
mX
i=0
bλi bψi ⊗W µ π bψi =µ
mX
i=0
(1−1/bνi)Zθ buibuT i Z ∗ θ
=µbvZθ bW −1/2 θ  1 bv mX i=0 bW 1/2 θ buibuT i bW 1/2 θ − bQ−1 θ  bW −1/2 θ Z ∗ θ .
But, then, since
 1√
bv
bW 1/2 θ bui m i=0 forms orthonormal basis, we obtain bL=bvµZθ[ bW −1 θ − bC −1 θ ]Z ∗ θ .
To proceed, we in the following lemma we guarantee that indeed bνi’s are positive and bQθ is invertible
matrix with high probability.
Lemma E.7.Under the assumptions of Proposition E.3 and Lemma E.5, if E
′′
n (δ)≤1/2 and
12E m,n(δ)/v+ 6E m(θ)< νm, then with probability in the i.i.d. draw of (x′ i)n i=1 from π′, it holds
that, bQθ is invertible and ∥ bQ−1 θ ∥ ≤2ν−1 m . Consequently, bv∥Zθ bC −1 θ Z ∗ θ ∥W µ π →W µ π ≤4/ν m and
∥bL∥W µ π →W µ π ≤6µ/ν m.
Proof. First, observe that due to (92) and (93), 3Em(θ) + 6E m,n(δ)/v < νm/2 implies that
λmin( bQθ) =bνm > νm/2>0. To conclude, observe that
bv∥Zθ bC −1 θ Z ∗ θ ∥W µ π →W µ π =bv∥Zθ bW −1/2 θ bQ−1 θ bW −1/2 θ Z ∗ θ ∥W µ π →W µ π
≤ bv v ∥ cMθ∥∥ bQ−1 θ ∥ ≤2 1 +E
′′
n (δ)
1− Em,n(δ) ν−1 m .
and∥ bL∥W µ π →W µ π ≤µ bv v ∥ cMθ∥(1 +∥ bQ−1 θ ∥).
Next, we obtain the bound on ∥Lm − bL∥W µ π →W µ,s π , for s∈[0,1] . To that end, we split the analysis as
∥Lm − bL∥W µ π →W µ,s π ≤ ∥P⊥ m R
1−s
2
µ [Lm − bL]∥W µ π →W µ π +∥P mR
1−s
2
µ [Lm − bL]∥W µ π →W µ π .(94)
33

For the first term, observe that
∥P ⊥ m R
1−s
2
µ [Lm − bL]∥W µ π →W µ π =∥P ⊥ m R
1−s
2
µ Pθ bL∥W µ π →W µ π ≤ν
1−s
2
m+1∥P ⊥ m bL∥W µ π →W µ π
≤ν
1−s
2
m+1∥[P ⊥ m −P ⊥ θ ]bL∥W µ π →W µ π ≤ν
1−s
2
m+1Em(θ)∥ bL∥W µ π →W µ π
≤ν
1−s
2
m+1
6µE m(θ)
νm
.
For the second term, sinceL m =µ(P m −[R m µ ]†), start by bounding
∥PmR
1−s
2
µ [Pm−bvZθ bW −1 θ Z ∗ θ ]∥W µ π →W µ π
≤ ∥PmR
1−s
2
µ ∥W µ π →W µ π

∥Pm−Pθ∥W µ π →W µ π +bv∥Zθ[W−1 θ − bW −1 θ ]Z ∗ θ ∥W µ π →W µ π 
≤ Em(θ) + bv v ∥I− cMθ∥ ≤ Em(θ) +E m,n(δ) 1+E ′′ n (δ) 1−Em,n(δ) ≤ Em(θ) +E m,n(δ),
and, then,
∥[Rm µ ] 1−s 2 [[Rm µ ]†−bvZθ bC −1 θ Z ∗ θ ]∥W µ π →W µ π
=∥[R m µ ] 1−s 2 [[Rm µ ]†−PmbvZθ bC −1 θ Z ∗ θ ]∥W µ π →W µ π
≤∥[Rm µ ] 1−s 2 [[Rm µ ]†Pθ −bvPmZθ bC −1 θ Z ∗ θ ]∥W µ π →W µ π +∥[Rm µ ] −1−s 2 P ⊥ θ ∥W µ π →W µ π
≤ ∥[Rm µ ] 1−s 2 [[Rm µ ]†Pθ −bvPmZθ bC −1 θ Z ∗ θ ]∥W µ π →W µ π + ∥PmP ⊥ θ ∥W µ π →W µ π
ν
1+s
2
m
.
But then, usingA †(B−A)B † =A †PIm(B) −P Im(A)B† withA=R m µ and
B=(bvZθ bC −1 θ Z ∗ θ )−1=  bv v √ vZθW−1/2 θ [W1/2 θ bC −1 θ W1/2 θ ]W−1/2 θ Z ∗ θ √ v −1
= v2 bvZθW−1/2 θ [W1/2 θ bC −1 θ W1/2 θ ]−1W−1/2 θ Z ∗ θ = v2 bvZθW−1 θ bCθW−1 θ Zθ,
with Lemma E.7, we have
∥[Rm µ ] 1−s 2 [[Rm µ ]†−bvZθ bC −1 θ Z ∗ θ ]∥W µ π →W µ π
≤ ∥Rm µ − v2 bvZθW−1 θ bCθW−1 θ Z ∗ θ ∥W µ π →W µ π ∥bvZθ bC −1 θ Z ∗ θ ∥W µ π →W µ π +Em(θ)
ν
1+s
2
m
≤4 ∥Rm µ − v2 bvZθW−1 θ bCθW−1 θ Z ∗ θ ∥W µ π →W µ π
ν
3+s
2
m
+ Em(θ)
ν
1+s
2
m
Now, by splitting the norm in the first term as
∥Rm µ − v2 bvZθW−1 θ bCθW−1 θ Z ∗ θ ∥W µ π →W µ π ≤∥Rm µ −vZθNθZ ∗ θ ∥W µ π →W µ π
+∥W−1/2 θ [bCθ−Cθ]W−1/2 θ ∥+∥W−1/2 θ bCθW−1/2 θ ∥

1− v bv

,
we conclude
∥[Rm µ ] 1−s 2 [[Rm µ ]†−bvZθ bC −1 θ Z ∗ θ ]∥W µ π →W µ π ≤4 4Em(θ) +E m,n(δ) +E
′′
n (δ) 1+Em,n(δ) 1−E ′′ n (δ)
ν
3+s
2
m
+ Em(θ)
ν
1+s
2
m
≤4 4Em(θ) +E m,n(δ) + 3E
′′
n (δ)
ν
3+s
2
m
+ Em(θ)
ν
1+s
2
m
.
Therefore, collecting the above, for alls∈[0,1]we obtain
µ−1∥Lm − bL∥W µ π →W µ,s π ≤ 6ν
1−s
2
m+1 Em(θ)
νm
+Em(θ)+Em,n(δ)
+4 4Em(θ) +E m,n(δ) + 3E
′′
n (δ)
ν
3+s
2
m
+ Em(θ)
ν
1+s
2
m
,
34

and, hence,
∥Lm − bL∥W µ π →W µ,s π ≤µ
"
(7νm + 16)E m(θ) + 4E m,n(δ) + 12E
′′
n (δ)
ν
3+s
2
m
+E m(θ) +E m,n(δ)
#
.
(95)
E.5 Gradient estimation
To estimate the gradient, recall that d∇U= bGzθ, where, using the notation of Proposition E.4,
bG T =−
mX
i=0
bλi buibuT i
h
1
nbv
nX
j=1
ξ(x′ j) i =−µ[ bW −1 θ − bC −1 θ ]bξ,
where bξ= 1 n Pn i=1 ξ(x′ i) = [bξ1 | · · · |bξd]∈R (m+1)×d.
We recall also that for anyp≥1
∥∇U− d∇U∥ W µ,p π =
s X
k∈[d]
∥∂kU− d∂kU∥ 2 W µ,p π .
In the following we consider the regularity assumption(RA): There exists p≥1 such that for every
k∈[d] , ∥∂kU∥ W µ,p π <∞ , that is ∥∇U∥ W µ,p π <∞ . Under this assumption, for every s≤p and everyk∈[d], we have that:
∥P ⊥ m ∂kU∥ W µ,s π =∥R (p−s)/2 µ P ⊥ m ∂kU∥ W µ,p π ≤ν (p−s)/2 m+1 ∥∂kU∥ W µ,p π (96)
Next, recalling bξ= [ bξ1 | · · · |bξd]∈R (m+1)×d and denoting ξ=E x′∼π′ξ(x′) = [ξ1 | · · · |ξd(x′)]∈
R(m+1)×d, we have
−bLfk=−µ bv v Zθ[ bW −1 θ −bC −1 θ ]Ex′∈π′[ξk(x′)]and d∂kU=µ Zθ[ bW −1 θ −bC −1 θ ]bξk,
which than implies
s X
k∈[d]
∥Pm∂kU− d∂kU∥ 2 W µ,s π ≤
s
2
X
k∈[d]
∥(Lm − bL)fk∥2 W µ,s π +
s
2
X
k∈[d]
∥bLfk − d∂kU∥ 2 W µ,s π
≤ ∥Lm − bL∥W µ π →W µ,s π
s
2
X
k∈[d]
∥fk∥2 W µ π +
s
2
X
k∈[d]
∥bLfk − d∂kU∥ 2 W µ π
=
p
2Ex∼π∥x∥2∥Lm − bL∥W µ π →W µ,s π
+
√
2µ∥Zθ[ bW −1 θ −bC −1 θ ](bξ− bv v ξ)∥
=
p
2Ex∼π∥x∥2∥Lm − bL∥W µ π →W µ,s π
+
√
2µ∥Zθ[ bW −1 θ −bC −1 θ ]W1/2 θ W−1/2 θ (bξ− bv v ξ)∥
≤
p
2Ex∼π∥x∥2∥Lm − bL∥W µ π →W µ,s π
+
√
2∥bL∥W µ π →W µ π
√
v
bv∥W−1/2 θ [bξ− bv v ξ]∥
≤
p
2Ex∼π∥x∥2∥Lm − bL∥W µ π →W µ,s π
+
√
2∥bL∥W µ π →W µ π
√
v∥W −1/2 θ [ 1 bv bξ− 1 v ξ]∥.(97)
Using that E
′′
n (δ)<1/2 from Lemma E.5 we have that |1/bv−1/v| ≤2E
′′
n (δ)/v and 1/bv≤2/ v.
Moreover, from the proof of Proposition E.4 we have
v∥W −1/2 θ ξ∥2 ≤ vEx′∼π′∥W−1/2 θ ξ(x′)∥2
≤ v(Ex′∼π′∥x′∥2 ∨1)ess sup
x′∼π′
∥W−1/2 θ wθ(x′)⊗w θ(x′)W−1/2 θ ∥ ≤cθ (σ2 π′ ∨1) v,
35

whereσ 2 π′ =E x′∼π′∥x′∥2.
Therefore, bounding the last term in (97) as
√
v∥W −1/2 θ [ 1 bv bξ− 1 v ξ]∥ ≤1 bv √ v∥W −1/2 θ [bξ−ξ]∥+ √ v∥W −1/2 θ ξ∥| 1 bv− 1 v | ≤2E
′
m,n(δ)
v + 2E
′′
n (δ)σπ′
√cθ√
v
and collecting all bounds we conclude that
∥∇U− bGzθ∥W µ,s π ≤ν(p−s)/2 m+1 ∥∇U∥ W µ,p π +µ σπ′ √ 2 h 24E m(θ)+5Em,n(δ)+12E ′′ n (δ) ν 3+s 2 m
+ 12E
′
m,n(δ)/σπ′+E
′′
n (δ)√cθ v
v νm
i
.(98)
E.6 Proof of Theorem 4.1
Proof of Theorem 4.1. First, observe that, since λi =µ(1−1/ν i), we have νi =µ/(µ−λ i), and,
hence:
gapi = min ℓ̸=i |νℓ −ν i|= min ℓ̸=i

 µ µ−λ ℓ − µ µ−λ i

 =µmin ℓ̸=i

 λi −λ ℓ (µ−λ ℓ)(µ−λ i)

= µ |µ−λ i| min ℓ̸=i |λi −λ ℓ| |µ−λ ℓ| ∈(0,1).
Next, to prove spectral bounds we use (92), (93) and substitute definitions of Em(θ), Em,n(δ) and
E
′′
n (δ)as follows
Em,n(δ)/v≲ε n(δ) :=τ e2β∥V∥ ∞
s
m d
µ β nlog m δ ,and
E
′′
n (δ)≲ σv v
r
2 log(2/δ)
n ≤e β∥V∥ ∞
r
2 log(2/δ)
n ≲ε n(δ),
where we used that σ2 π′ =E x′∼π′∥x′∥2 ≤σ 2 πeβ∥V∥ ∞, σ2 v =E x′∼π′v(x′)2 ≤ veβ∥V∥ ∞ and
v≥e −β∥V∥ ∞.
Therefore,
|bνi −ν i|≲E m(θ) +ε n(δ)and∥ bψi−ψi∥W µ π →W µ π ≲ Em(θ) gapi + εn(δ) [gapi−3E m(θ)]+ ,(99)
and the bound follows, after some algebra, by expressing gap in generator eigenvlues w.r.t. gap in the
resolvent ones.
To conclude the proof, observe that
E
′
m,n(δ)ν
1+s
2
m /v≲τ e2β∥V∥ ∞
r µ m
(µ−λ m)n max
(
1
µβ
r
log m+d δ , σπeβ∥V∥ ∞/2 log 1 δ
)
≲σ πεn(δ),
wheneverβ(µ−λ m)≥1, while
σπ′E
′′
n (δ)
p
cθ/v≤σ π′τ eβ∥V∥ ∞
s
m d
µ βE
′′
n (δ)≲σ π′e2β∥V∥ ∞
s
m d
µ β nlog 2 δ ≲ε n(δ).
So, substituting this in (98) we obtain
∥∇U− bGzθ∥W µ,s π ≤ν(p−s)/2 m+1 ∥∇U∥ W µ,p π +µν − 3+s 2 m σπ  εn(δ) +E m(θ)  .
36

Figure 4: Top left panel: the different potentials involved in this experiment in units of 1/β. Other
panels: comparison of the eigenfunctions obtained with LITL and with the methods presented in
[16] and [62]. Error bars have been computed using 4 different models with different random initial
parameters
F Experiments
In this section we expand on the experimental validation of LITL and its applications in physics and
ML. While details for each experiment are provided, the code for reproducing them is available upon
request and will be included in the camera ready version of the paper.
F.1 1D double-well potential
The goal of this experiment is to recover the spectral decomposition of the generator corresponding
to the 1D double-well potential. We compared LILT to prior methods [16] and [62] for the estimation
of the four eigenpairs (λj, ψj)4 j=1. We note that for the method of [62], even in the best-performing
trial, we were able to identify only two distinct eigenfunctions, with eigenvalues 0.6 and 8, which are
close to the reference values.
For our method LILT in this experiment, we used standard feed forward neural networks, with tanh
activation function. We used µ= 100 , α= 5 and trained 20 features. One of the strengths of LITL
is the estimation of the drift. In this section, we compare our estimation with respect to the ground
truth. In Figure 5, left panel we show how the drift can be projected on the basis of the eigenfunctions
of L obtained by numerically solving the eigenvalue problem. We note, that already even with the
ground-truth eigenfunctions, one needs a sufficiently high number of basis functions to express the
drift. On the right panel, we show our estimation of the drift using LITL: it matches very well the
ground truth on the training set. Finally, we compare the dynamics produced from the estimation of
the drift from LITL with the true one in Figure 6. We started 500 simulations in the left well and
looked at the time evolution of the probability distribution, both with the target potential and with
LITL. LITL reproduces very well the time evolution of the probability distribution, without having to
be trained with data coming from the target potential.
In Figure 4 we show the accuracy of the estimated eigenfunctions by computing uncertainties over 4
different trials with different random initialization. The results of [62] are omitted due to frequent
uncontrolled collapse of learned subspace to slower modes, likely caused by larger number of
sensitive hyper-parameters. The other two methods perform very well on the first eigenfunction,
which characterizes the transition between the two wells, the only slow mode of the system. But then,
as we increase the eigenfunction index, the variance between trials for the second method increases,
while LITL’s one remains.
F.2 Chignolin
For this experiment, we used the schnet architecture [48] as implemented in the mlcolvar library [6].
Only the positions of the alpha carbons were taken into account, and for more expressibility, the one
hot encoding of the atomic number node feature information was replaced with the residue type. We
used with 3 interaction blocks, 14 RBF functions and an hidden dimension of 64. The value ofµ used
was 5000 with α= 1.0 . To optimize the weights, we used the AdamW optimizer. The variational
37

Figure 5:1D double-well Langevin dynamics.Gradient of the target potential projected on the leading
eigenspaces (left), and its estimation from data (right). Uncertainty is computed over 4 different
models
Figure 6:1D double-well Langevin dynamics.Target flow from an initial distribution and its
estimation from data.
ansatz for the features was of the form: Zθ(x) =G θsoftmax(hθ). Where Gθ is a linear layer and hθ
is the output of the graph neural network.
F.3 Cobalt nanoparticle
Cobalt nanoparticle magnetization dynamics.We learn the spectral properties of the Langevin
generator on a sphere S2, modeling the magnetization dynamics of a cobalt nanoparticle under the
potential U(m) =−K u(m·n u)2 +K c(m2 xm2 y +m 2 ym2 z +m 2 zm2 x), nu being easy axis of uniaxal
anisotropy. [21, 22]. For uniaxal and cubic anisotropy constants Ku = 1.0and Kc = 0.3, respectively,
four metastable states are separated by energy barriers. Understanding the thermodynamics and
kinetics of cobalt nanoparticles, in particular the metastable states and transition rates revealed by the
Langevin generator, helps set switching fields for memory devices, control blocking temperatures and
data retention times, and optimize heat dissipation in hyperthermia applications. Our method infers
the generator’s eigenvalues and eigenfunctions using only potential evaluations - without accessing
its gradient - simulating experimental scenarios where analytic form of the potential is unknown, but
instead anisotropy landscapes are empirically reconstructed via techniques like torque magnetometry
or micro-SQUID measurements [28] which probe switching field distributions without direct gradient
information. Furthermore, learning the generator directly from sampled trajectories enables prediction
of long-time magnetization relaxation, identification of dominant transition pathways, and extraction
38

Figure 7:First triplet of leading eigenfunctions of the Langevin generator for a cobalt nanoparticle
potential.First row show 3D visualization on the unit sphere S2, colored by eigenfunction value,
while the second one shows polar coordinate representation ψ(θ, φ). Third row shows reult obtained
by LITL. Multiplicity of learned eigenvalues (i.e. time-scales) and spatial symmetry of eigenfunction
are consistent with symmetries of the potential energy, and eigenvalue and eignfunction errors are
reported in the header.
of effective energy barriers, all critical aspect for designing nanoparticle-based hyperthermia agents,
where heating efficiency depends on the slowest dynamical modes and only equilibrium data may be
available.
In magnetic nanoparticle systems, knowledge of metastable states directly governs key technological
metrics. The number, depth, and connectivity of these states determine the switching field in magnetic
memory devices—each metastable orientation can encode a distinct bit. The energy barriers between
states set the blocking temperature and data retention time in storage applications, with β∆U >60
enabling non-volatile memory stable for years. For magnetic hyperthermia cancer treatment, the
transition rates between states control the heat dissipation rate under alternating fields; optimizing the
anisotropy landscape maximizes tumor heating while minimizing nanoparticle dosage. In magnetic
sensors, engineered metastable states enhance sensitivity by creating steep magnetization transitions
at specific field thresholds. Furthermore, the multi-state dynamics produce multi-exponential relax-
ation in AC susceptibility measurements, allowing experimentalists to fingerprint nanoparticle size
distributions and anisotropy disorders.
Remarkably, our method was able to recover over ten eigenfunctions with the correct symmetry groups
of the model, see Figures 7-9, purely from black-box potential evaluations, without prior knowledge
of the functional form. The learned eigenfunctions exhibit degeneracy patterns characteristic of the
underlying D2h point group symmetry including a singlet stationary distribution and doublets of
symmetry-related eigenfunctions linked by rotations of π/2 in azimuthal angle ϕ, and reflections
through the equatorial plane. Identifying these symmetries is fundamental because they dictate the
multiplicity of relaxation timescales.
39

Figure 8:Second triplet of leading eigenfunctions of the Langevin generator for a cobalt nanoparticle
potential.First row show 3D visualization on the unit sphere S2, colored by eigenfunction value,
while the second one shows polar coordinate representation ψ(θ, φ). Third row shows reult obtained
by LITL. Multiplicity of learned eigenvalues (i.e. time-scales) and spatial symmetry of eigenfunction
are consistent with symmetries of the potential energy, and eigenvalue and eignfunction errors are
reported in the header.
In magnetic nanoparticles, such symmetry dictates the multiplicity of relaxation timescales, and
knowing it reveals whether the anisotropy is purely uniaxial or includes cubic contributions, directly
impacting applications from data storage (bit stability) to hyperthermia (heat dissipation pathways).
The ability of our method to extract this symmetry structure from potential-only queries demonstrates
that the method can infer not just dynamical rates but also the underlying geometric constraints of
experimentally measured systems. To summarize, LITL’s capacity to map the metastable landscape
isn’t merely academic, it enables rational design of nanoparticles for targeted applications by linking
atomic-scale anisotropy to macroscopic magnetic performance unlocking exciting new avenues of
research.
F.4 Fairness-aware transfer via latent diffusion.
We evaluate the proposed method on the Adult Income dataset
(https://archive.ics.uci.edu/dataset/2/adult), a standard benchmark for fairness in binary classification,
in the challenging unawareness case [ 11, 18, 61]. The task is to predict whether an individual’s
annual income exceeds $50K, using demographic and employment-related features. Following
common practice, we considergenderas the sensitive attribute and measure fairness by Equal
Opportunity (EO) given by theTrue Positive Rate (TPR) differencebetween males and females. The
dataset is split intotraining(60%),audit(25%) andtest(15%) datasets, with the sensitive variable
removed from the training set. The audit data is used to returns black-box feedback indicating
whether a model satisfies the desired fairness criterion.
We first learn a classifier fω(x) = softmax(aT ωeω(x)) via empirical risk minimization on the training
set, where ω denote the classifier’s parameters. In particular, eω(x)∈S d−1 denotes the network
40

Figure 9:Third triplet of leading eigenfunctions of the Langevin generator for a cobalt nanoparticle
potential.First row show 3D visualization on the unit sphere S2, colored by eigenfunction value,
while the second one shows polar coordinate representation ψ(θ, φ). Third row shows reult obtained
by LITL. Multiplicity of learned eigenvalues (i.e. time-scales) and spatial symmetry of eigenfunction
are consistent with symmetries of the potential energy, and eigenvalue and eignfunction errors are
reported in the header.
latent (inner) representation, normalized to lie on the sphere, and aω ∈R d. This base classifier
achieves strong predictive performance but exhibits a non-negligible TPR disparity between groups,
both on the held-out audit set and on the test set.
We adopt a geometric viewpoint in which the latent representations produced by the trained encoder
induces a compact state space on Sd−1, allowing us to model their variability using intrinsic diffusion
processes. As asourcereference dynamics, we consider apure diffusion(i.e., U ′ = 0) on the latent
sphere, whose generator is the Laplace-Beltrami operator. This source diffusion does not encode any
task-specific objective; rather, it captures the intrinsic geometry and dominant modes of variation of
the learned representation subject to pure randomness.
Figure 10: Accuracy–fairness Pareto curve for the Adult Income experiment. Each point corresponds
to a different number of LITL steps. LITL hyperparameters are calibrated on audit set, and then used
to achieve substantial reduction in TPR disparity with a limited decrease in accuracy on a test set.
The EO score objective induces an unknown target potential U on the latent space Sd−1, whose
values can be evaluated locally by probing the model on the audit data, but whose gradient is not
41

directly accessible. To be precise, we define U(e)=|TPR male(Ne)−TPR female(Ne)|, where Ne
denotes the 100 nearest neighbors ofe∈S d−1.
Unlike the source Laplace-Beltrami operator with potential U ′= 0, now the target Langevin gen-
erator’s eigenfunctions define a hierarchy of fairness related slow and fast directions on the latent
manifold. In particular, the leading nontrivial eigenfunctions correspond to large-scale, semantically
meaningful variations in the representation, while higher modes capture localized or noisy fluctu-
ations. This multiscale spectral structure provides a natural coordinate system for analyzing and
adjusting the model’s fairness behavior in a controlled and interpretable way. So, LITL leverages
samples from the source diffusion and scalar evaluations of the bias functionalV=−U obtained from
the audit set to estimate the gradient of the induced potentialprojected onto the slow eigenspaces of
the source generator. Importantly, this estimation does not rely on differentiating the bias measure
with respect to model parameters. Instead, LITL withing its two phases learns a vector field that
approximates the intrinsic spherical gradient of the bias-induced potential in directions that are stable
under latent diffusion.
Figure 11: Training dynamics of the LITL encoder. Physics-informed contrastive loss measurign the
discrepancy of
In this experiment we sampled n= 5000 samples from d= 32 dimensional latent sphere,
parametrized zθ as a multilayer perceptron [32,66,33,66,33] with Tanh activations up to penulti-
mate layer. In Figure 11 we show the training and validation losses (on 200 samples) across the
epochs. Main SVD loss is shown on the left, while the orthonormal penalty is shown on the right.
Once LITL encoder zθ is trained, we proceed with the estimation of the spectrum and gradient field
using all training samples.
The learned gradient field b∇Sd−1 U(e)=(I−ee T) bGzθ(e) is used to perform short-horizon, geometry-
respecting updates on the latent sphere
e(k+1) ω = (1+γe(k) ω T bGzθ(e(k) ω )e(k) ω −γ bGzθ(e(k) ω ) ∥(1+γe(k) ω T bGzθ(e(k) ω )e(k) ω −γ bGzθ(e(k) ω )∥ , k≥0,
where each update corresponds to a small γ >0 step along the estimated spherical gradient,
followed by projection to the sphere. Repeating this procedure steers the pretrained model fω toward
configurations with reduced TPR disparity while preserving the dominant representational structure
learned during initial training. Since the intervention acts only along slow diffusion modes and is
applied over short time scales, it avoids the instability and performance collapse typically associated
with direct re-optimization using fairness regularizers.
We apply the LITL update iteratively and monitor both predictive accuracy and TPR difference on
the audit set. Once we have calibrated hyperparameters step size and number of gradient steps, we
perform the evaluation of the validated model on a test set.
In Figure 10 we report the resulting Pareto curves on audit and test set, illustrating the trade-off
between accuracy and fairness induced by the LITL intervention. Each point on the curve corresponds
to a different number of LITL steps. As the intervention increases, the TPR difference significantly
decreases to acceptable 1%, while accuracy degrades gracefully.
Furthermore, since by inspecting the estimated spectrum of the generator, c.f. Figure 12 (middle),
one observes a clear separation of the slow and faster manifold, we examine how much improvement
one obtains by using only first 16 nontrivial eigenfunctions in projecting the gradient of U Figure 12
(left) compared to using all 32 learned ones, Figure 12 (right). Shown results are obtained via 100
42

Figure 12: Accuracy deterioration and TPR disparity improvement across LITL gradient steps on
100 random test datasets. On the left the LITL model uses 16 slowest directions, while on the right
the flow is across additional 16 faster ones. While slowest manifold corrects the TPR gap while
minimally changing the accuracy it reaches the metastable state at around 50% gap reduction. On
the other hand, including faster dynamics allows further reduction, but the transformations of the
latent space geometry induce accuracy deterioration. The gap in the spectrum shown in the middle
plot shows how the two manifolds are separated. This demonstrates how spectral structure of the
generator related to the feedback potential allows one to introduce alignment of the model in a control
manner.
randomly chosen test sets, where the mean improvement is shown with a line, while the shaded are
represents 5th and 95th percentile.
43
