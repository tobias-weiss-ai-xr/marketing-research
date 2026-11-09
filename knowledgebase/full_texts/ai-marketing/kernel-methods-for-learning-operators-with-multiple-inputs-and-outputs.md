---
title: Kernel Methods for Learning Operators with Multiple Inputs and Outputs
url: https://arxiv.org/abs/2608.11831
category: ai-marketing
subcategory: measurement
date: 2026-08
venue: ''
authors:
- Adrien Weihs
- Chunyang Liao
- Jingmin Sun
- Hayden Schaeffer
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.11831
pages: 56
chars: 161803
fetched_at: '2026-11-08T13:29:55+00:00'
kb_version: 1
---

# Kernel Methods for Learning Operators with Multiple Inputs and Outputs

Kernel Methods for Learning Operators with
Multiple Inputs and Outputs
Adrien Weihs*a, Chunyang Liao †b, Jingmin Sunc, and Hayden Schaeffera
aDepartment of Mathematics,
University of California Los Angeles,
Los Angeles, CA 90095, USA.
bDepartment of Mathematical Sciences,
University of Arkansas,
Fayetteville, AR, 72701, USA.
cDepartment of Applied Mathematics and Statistics,
Johns Hopkins University,
Baltimore, MD 21218 , USA.
Abstract
Learning mappings between infinite-dimensional objects is a central challenge in scientific machine learn-
ing. We introduce a general kernel-based encoder-decoder framework for operator learning that separates
observation, representation, learning, and reconstruction. We develop this framework for multi-input, multi-
output operator learning, where operators map between products of potentially distinct function spaces. Our
approximation theory shows that, although the number of inputs and outputs can increase, the convergence
rate is governed by the most challenging constituent approximation problem rather than the overall problem
dimension. The framework leads to practical kernel methods with closed-form training and inference, com-
bining mathematical tractability with computational efficiency. We further specialize the approach to multi-
ple operator learning by introducing KernelMO, a family of kernel methods with complementary operator-
valued and product-space formulations. Across five families of parametric partial differential equations,
the proposed methods achieve competitive or state-of-the-art predictive accuracy while reducing training
and inference costs relative to neural operator architectures and deep learning based models, offering an
efficient and lightweight alternative.1
Keywords and phrases.Multiple operator learning, operator learning, kernel methods, encoder–decoder
methods, operator-valued kernels, scientific machine learning, parametric partial differential equations.
Mathematics Subject Classification.46E22, 65D15, 41A05
1 Introduction
Learning families of related operators between function spaces is an increasingly important problem in sci-
entific machine learning, arising from parametric partial differential equations, inverse problems, and multi-
fidelity simulation [51]. This setting, commonly referred to asmultiple operator learningormulti-task operator
learning, seeks to learn a map
G:W− → {G[α] :U→V} α∈W ,
*Corresponding author. Email:weihs@math.ucla.edu.
†This work was initiated while the author was at the University of California Los Angeles.
1An implementation of KernelMO, together with the code used to reproduce all numerical experiments, is available athttps:
//github.com/liaochunyang/kernelMO.
1
arXiv:2608.11831v1  [cs.LG]  12 Aug 2026

Theory
Empirical performance Scalability
Foundation
models
MNO
Kernel
methods
Figure 1: Conceptual illustration of the trade-offs between theoretical guarantees, empirical performance, and scalability
in learning operators with multiple inputs and outputs. Foundation models prioritize scalability across large collections
of operators, dedicated neural architectures such as MNO seek a balance between scalability and predictive performance,
while the kernel-based methods proposed in this work target the moderate-data regime by emphasizing theoretical guar-
antees together with competitive predictive accuracy.
which assigns to each parameter (or task)α∈Wan operatorG[α] :U→V,whereW,U, andVare
typically function spaces. A variety of approaches have been proposed for multiple operator learning, see for
example [11, 21, 26, 33, 34, 37, 46, 50, 53, 58, 61]. As illustrated conceptually in Figure 1, existing methods
can be viewed as occupying different positions in the trade-off between scalability, empirical performance,
and theoretical guarantees. Large-scale foundation models leverage massive datasets to learn highly expressive
representations across diverse families of PDEs and scientific simulations. These models have demonstrated
remarkable empirical performance and excellent scalability, although their theoretical understanding remains
comparatively limited. Dedicated architectures, such as Multiple Neural Operators (MNO) [51–53], instead
exploit the structure of the learning problem to achieve strong empirical performance while benefiting from
increasing theoretical support.
Many scientific computing applications; however, are not constrained by scalability to large training datasets.
Instead, they prioritize predictive accuracy, mathematical guarantees, and computational efficiency in moderate-
data settings. This motivates the development of learning architectures tailored to this regime by utilizing the
general encoder-decoder formulation illustrated in Figure 2a: inputs and outputs are first encoded into latent
spaces, a surrogate is learned between these representations, and the prediction is subsequently decoded to the
original output space. A key feature of this framework is that the surrogate can be chosen independently of
the encoders and decoders: whereas existing approaches predominantly employ deep neural networks for this
purpose [25, 29, 35], we instead utilize kernel-based surrogate models.
Importantly, the proposed kernel-based encoder-decoder approach naturally extends beyond classical mul-
tiple operator learning to general multi-input, multi-output operator learning problems, i.e., learning maps of
the form
(1)G:X 1 × · · · ×Xm − →Y1 × · · · ×Yn,
where eachX i andY j may be a distinct function space. We show that our approach is mathematically tractable
in this generalized setting: it admits rigorous approximation guarantees, scales favorably with the numbers of
input and output tasks, and leads to highly efficient computational implementations.
1.1 Main Contributions
The main contributions of this work can be summarized as follows.
1.A general kernel framework for encoder–decoder learning.We develop a general kernel-based
framework for learning maps between Hilbert spaces within an encoder–decoder architecture. Specif-
ically, in Theorem 3.3, we show that every kernel defined on the latent surrogate space induces a cor-
responding kernel on the original input and output spaces. In addition, in Corollary 3.4, we establish
2

an equivalence between learning in the latent reproducing kernel Hilbert space and learning with the
induced kernel on the original spaces. Together, these results provide a rigorous theoretical foundation
for kernel-based encoder–decoder learning.
2.An encoder–decoder error decomposition.We derive an encoder–decoder error decomposition in
Theorem 3.7 of the form
Approximation error≲Representation error+Learning error+Data consistency error,
thereby separating the contributions of the encoder–decoder architecture, the learned surrogate, and the
measurement process.
3.Approximation theory for multi-input, multi-output operator learning.We specialize this frame-
work to generalized multi-input, multi-output operator learning on product Hilbert spaces of functions.
For a map as in (1), we establish rigorous approximation guarantees for the proposed kernel-based
encoder–decoder architecture in Theorem 3.15:
Approximation error≲max
1≤i≤m
{Input reconstruction errori}+ max 1≤j≤n {Output reconstruction errorj}
+Learning error+Data consistency error.
Importantly, these guarantees scale favorably with the numbers of input and output tasks: the approxi-
mation rate is governed by the most challenging individual task rather than deteriorating with the overall
problem dimension.
4.Kernel formulations for multiple operator learning.In Section 3.4, we instantiate the proposed frame-
work for multiple operator learning through the KernelMO family of methods. Depending on the rep-
resentation of the target map, this yields the operator-valued formulation KernelMO-OV, which directly
approximatesG:W→ {G[α] :U→V} α∈W ,or the product-space formulation KernelMO-PS, which
instead approximates the equivalent mapG:W×U→V.Both formulations inherit the approxi-
mation guarantees of the general framework while exhibiting different computational complexities and
scalability with respect to the number of training samples.
5.Comprehensive empirical evaluation.We validate the proposed methods on a diverse collection of
multiple operator learning benchmarks arising from parametric PDEs in Section 4. Our experiments
demonstrate competitive predictive accuracy, substantial reductions in training and inference time com-
pared with state-of-the-art neural operator architectures, and illustrate the practical advantages of kernel-
based encoder–decoder learning in moderate-data regimes.
1.2 Related Works
Multi-operator learningMultiple operator learning arises in a variety of settings where one seeks to approx-
imate not a single operator, but an entire collection of related input–output mappings. Such collections may
emerge naturally from parameterized models, changing geometries, varying boundary conditions, or different
governing equations. Alternatively, they may be constructed deliberately to enable information sharing across
related learning tasks, with the goal of improving sample efficiency, robustness, and generalization. These
viewpoints have motivated a rapidly expanding literature on multiple operator learning and related frame-
works; see, for example, [7, 11, 21, 26, 33, 34, 37, 46, 47, 50, 51, 53, 55, 56, 58, 60, 61, 63, 64, 66]. Recently, [57]
extended the analysis to the general multi-input, multi-output operator learning framework.
From a modeling perspective, existing approaches can largely be grouped into two categories. The first
treats each operator as an independent learning problem, training a separate surrogate for every member of
the collection. While simple, this approach cannot exploit relationships between operators and therefore offers
limited transfer to new tasks. The second instead represents the collection as a single parameterized operator
family, in which an auxiliary variable identifies the desired operator. This variable may encode, for example,
physical parameters, a task identifier, the governing equations, or even textual descriptions of the problem
[32,34,39,46,51–53,56]. By conditioning on such auxiliary information, a single model can share information
across related operators and often exhibits improved transfer, zero-shot capabilities, and out-of-distribution
generalization. This structure forms the basis of most recent work on PDE foundation models.
3

Kernel-based surrogate modelingKernel-based methods have long served as a fundamental framework
for surrogate modeling due to their strong approximation property and rigorous theoretical foundations. By
representing the target function in a reproducing kernel Hilbert space (RKHS), these methods provide flexible,
nonparametric approximations from scatter data while naturally supporting interpolation, regularization, and
uncertainty quantification. Classical kernel surrogates include kernel interpolation, kernel ridge regression,
and Gaussian process regression, all of which have found widespread use in scientific computing; see, for
example, [8, 13, 20, 22, 23, 45].
These ideas have been extended to operator learning, where the objective is to learn nonlinear mappings
between function spaces rather than finite-dimensional input-output pairs [7,9,24,28,38,62,65]. By extending
reproducing kernel Hilbert space (RKHS) techniques from finite-dimensional regression to mappings between
function spaces, it provides a principled framework for learning nonlinear operators while admitting rigorous
analyses of approximation accuracy, stability, and generalization. Numerical studies have demonstrated that
kernel-based operator learning models can achieve competitive performance compared with neural networks-
based operator learning methods. These advantages make kernel operator learning both a mathematically
principled framework for constructing surrogates of complex solution operators and an important benchmark
for evaluating the accuracy and generalization capability.
Although kernel operator learning has a theoretical foundation, simple implementation, and competitive
performance, existing methods rely on computationally expensive kernel representation. This motivates the
development of scalable kernel surrogate models that retain the theoretical advantages of kernel-based methods
while providing computational efficiency; see, for example, [31, 40, 59].
Organization of the paperThe remainder of the paper is organized as follows. In Section 2, we introduce
the assumptions and mathematical framework underlying our analysis. Section 3 presents the main theo-
retical results, including the general encoder–decoder framework, its approximation theory for multi-input,
multi-output operator learning, and its specialization to the KernelMO family of methods for multiple operator
learning. In Section 4, we numerically evaluate the proposed methods across a range of multiple operator
learning problems. Proofs of all theoretical results are collected in Appendix A.
2 Background
In this section, we review the mathematical background required throughout the paper. We begin by introducing
the framework of minimum-norm recovery from bounded linear measurements, which provides a canonical
reconstruction procedure and forms the basis for the encoder–decoder construction developed in subsequent
sections. We then briefly recall the theory of operator-valued reproducing kernel Hilbert spaces, which serves
as the learning space for the latent surrogate operators considered in this work.
2.1 General Notation
For a spaceX, the mapId X denotes the identity map onX. We writeL(X)for the set of bounded linear
operators mappingXtoX. For a mapL, we denote its domain byD(L), its adjoint byL ∗, its kernel by
ker(L), and its range byran(L). We say that a map is boundedly invertible if it is bijective and its inverse is
bounded. Forx∈R, we write(x) + := max{x,0}for its positive part. Forx∈Xandr >0, we denote by
BX (x, r) :={y∈X:∥x−y∥ X < r}the open ball of radiusrcentered atx, and writeB X (r) :=B X (0, r).
For an open setΩ⊂R d, we denote byW s,p(Ω)the Sobolev space of orders≥0and integrability exponent
1≤p≤ ∞. Its seminorm is denoted by| · | Ws,p(Ω),and its norm by∥ · ∥Ws,p(Ω).Whenp= 2, we write
Hs(Ω) := Ws,2(Ω).
2.2 Optimal Recovery from Linear Measurements
In this section, we introduce minimum-norm recovery from bounded linear measurements in a Hilbert-space
setting. This provides a canonical way of reconstructing functions from observations. We allow the observa-
tion space to be an arbitrary Hilbert space, thereby encompassing finite collections of measurements as well
as infinite-dimensional observation spaces. Typical examples include local averages [6], integral functionals,
4

and Fourier coefficients [36, 41]. In operator learning, the most common setting is a finite collection of point-
wise measurements of the input and output functions [9]. The following result gives explicit formulas for the
reconstructed function. For completeness, we provide a proof in Section A.1.
Theorem 2.1(Minimum-norm recovery).LetXandZbe Hilbert spaces and letL:X→Zbe a bounded
linear measurement operator. Given a measurement vectorS∈Zandγ >0, consider the minimum-norm
recovery problem
x(S) = argmin
x∈X
{∥x∥X |Lx=S}.
and the regularized recovery problem
xγ(S) = argmin
x∈X

∥x∥2 X +γ −1∥Lx−S∥ 2 Z 	 .
1. IfLis surjective, the unique minimizer x(S)is given by
(2) x(S) =L ∗(LL∗)−1S.
2. The unique minimizer xγ(S)is given by
(3) xγ(S) =L ∗(LL∗ +γI Z)−1S.
In the encoder–decoder framework developed in Section 3.2, the measurement operatorLof Theorem 2.1
will play the role of an encoder, while the corresponding minimum-norm or regularized recovery map will
provide a natural choice of decoder.
2.3 Reproducing Kernel Hilbert Spaces
In this section, we review the necessary background on kernels and RKHSs. In particular, RKHSs are of
interest because their structure equips the general encoder–decoder framework with mathematical structure
and leads to well-posed learning problems (see Theorem 3.3 and Corollary 3.4). Moreover, RKHSs that embed
continuously into Sobolev spaces (see Remark 3.1), provide a setting in which quantitative reconstruction error
estimates can be derived, as developed in Section 3.3.
We first define an operator-valued kernel and then the corresponding function-valued RKHS, which were
introduced in [27]. LetXandYbe separable Hilbert spaces endowed with the inner products⟨·,·⟩ X and⟨·,·⟩ Y.
Definition 2.2(Operator-valued Kernel).We callK:X × X → L(Y)an operator-valued kernel if
1.Kis Hermitian, i.e.K(x, x ′) =K(x ′, x)⊤ for allx, x′ ∈ X, writingA⊤ for the adjoint of the operator
Awith respect to⟨·,·⟩ Y.
2.Kis non-negative, i.e. for allm∈Nand any set of points{(x (i), y(i)}m i=1 ⊂ X × Yit holds thatPm
i,j=1⟨y(i), K(x(i), x(j))y(j)⟩Y ≥0
We callKnon-degenerate if Pm i,j=1⟨y(i), K(x(i), x(j))y(j)⟩Y = 0impliesy (i) = 0for alliwhenever
x(i) ̸=x (j) for alli̸=j.
Definition 2.3(Function-valued Reproducing Kernel Hilbert Space).A Hilbert spaceHof functions fromX
toYis called a function-valued reproducing kernel Hilbert space if there is a nonnegativeL(Y)-valued kernel
KonX × Xsuch that:
1. the functionz7→K(w, z)gbelongs toH, for everyz, w∈ Xandg∈ Y,
2. for everyH∈ H,w∈ X, andg∈ Y,⟨H, K(w,·)⟩ H =⟨H(w), g⟩Y.
There exists a bijection between non-negative kernel and RKHS, which is summarized in the following
theorem [27, Theorem 2].
5

Theorem 2.4(Bijection between function-valued RKHS and operator-valued kernel).AL(Y)-valued kernel
KonX × Xis the reproducing kernel of some Hilbert spaceH, if and only if it is non-negative.
The above theorem is parallel to the theorem of bijection between scalar-valued kernels and RKHS, which
was first established by Aronszajn in [5].
We note that the classical scalar- and vector-valued RKHS can be viewed as special cases of the function-
valued RKHS. In particular, when we take the output spaceY=R, the kernel functionK:X × X → L(Y)
reduces to a scalar-valued functionK:X × X →R, which is exactly the classical scalar-valued kernel
function [18]. When the output space isY=R d, then bounded linear operators mappingR d toR d are simply
alld×dmatrices, i.e.L(Y) =R d×d. Therefore, we obtain a matrix-valued kernel functionK:X ×X →Rd×d
corresponding to the classical vector-valued RKHS setting [2]. Scalar- and matrix-valued kernels are widely
used in scalar- and vector-valued function approximation problems [2, 54]. In practice, a simple choice of a
matrix-valued kernel is the block-diagonal kernel
K(x, x′) =S(x, x′)Idd×d,
whereS(x, x′) :X × X →Ris a scalar-valued kernel. The block-diagonal matrix-valued kernel also implies
that we can separately approximate each component of a vector-valued function.
Remark2.5 (RKHS interpolation as minimum-norm recovery).Minimum-norm recovery from Theorem 2.1
encompasses classical interpolation in reproducing kernel Hilbert spaces. When the ambient Hilbert space is
an operator-valued RKHS and the observations consist of pointwise evaluations, the minimum-norm recovery
problem is precisely the standard RKHS interpolation problem and the minimum-norm interpolant is therefore
given by the classical vector-valued kernel interpolant (see the proof of Corollary 3.4).
3 Main Results
In this section, we develop the main theoretical framework of the paper. We first establish an abstract encoder–
decoder formulation together with a decomposition of the prediction error into representation, learning, and
data consistency terms. We then derive approximation guarantees for the multi-input, multi-output operator
learning problem and characterize its approximation complexity in terms of the approximation complexities of
the individual input-output operator learning tasks. Finally, we specialize the general framework to multiple
operator learning, yielding practical learning algorithms.
3.1 Assumptions
We review the assumptions used throughout our results.
Assumptions1.We make the following assumption on our spaces.
S.1The spacesH

J,(Ω j)J j=1,(n j)J j=1,(s j)J j=1,(p j)J j=1,(t j)J j=1,(q j)J j=1,(A j)J j=1  andX  J,(Ω j)J j=1,(t j)J j=1,
(qj)J j=1  are function sets such that
(a)Ω j ⊂R nj is a bounded domain with Lipschitz boundary;
(b) the spaceH= QJ j=1 Hj is the Hilbert product of spacesH j of real-valued functions onΩ j,
each satisfying the continuous embeddingH j ,→W sj ,pj (Ωj),and is equipped with the canonical
product norm∥u∥ 2 H = PJ j=1 ∥uj∥2 Hj .
(c) the space X is given byX= QJ j=1 Wtj ,qj (Ωj)and is equipped with the the product norm∥u∥ 2 X =PJ
j=1 ∥uj∥2 Wtj ,qj (Ωj ).
(d) for eachj= 1, . . . , J,pj, qj ∈[1,∞]and
sj ≥n j ifp j = 1, s j > nj pj if1< p j <∞, s j ∈N ∗ ifp j =∞;
6

(e) for eachj= 1, . . . , J, definingℓ0,j :=s j −n j

1
pj − 1 qj

+
,we have
tj ∈N 0,0≤t j < ℓ0,j;
(f) for eachj= 1, . . . , J, letAj ={x 1 j , . . . , xmj j } ⊂Ωj be a finite sampling set with fill distance
hj := sup
x∈Ωj
min
a∈Aj
∥x−a∥ 2;
Sinces j −t j > nj

1
pj − 1 qj

+
,the Sobolev embedding theorem [1], together with the finite-measure
embedding whenq j < pj, yieldsW sj ,pj (Ωj),→W tj ,qj (Ωj)continuously. Consequently,H j ,→W tj ,qj (Ωj)
continuously for everyj, and henceH,→Xcontinuously. Moreover, the Sobolev embedding theorem also
yields the continuous embeddingH j ,→W sj ,pj (Ωj),→C 0(Ωj).
The spacesHandXplay distinct roles throughout the paper. The spaceXis the domain of the operator
G, and all approximation errors are measured in the weaker norm ofX. In contrast,Hserves as a regularity
space: its stronger norm quantifies the additional smoothness required to obtain interpolation and reconstruc-
tion estimates from finitely many observations. This separation mirrors classical approximation theory, where
errors are typically measured in a weak norm while convergence rates depend on higher-order regularity. For
example, finite element estimates take the form
∥u−I hu∥L2(Ω) ≤Ch k∥u∥Hk(Ω),
where the error is measured in the weakerL 2-norm, whereas the rate is governed by the strongerH k-norm.
Remark3.1 (Hilbert spaces embedded in Sobolev spaces).An important class of examples forHis provided
by reproducing kernel Hilbert spaces. Indeed, for several kernels used in approximation theory, such as Matérn
and Wendland kernels, the associated RKHS is continuously embedded in, or is norm-equivalent to, a Sobolev
space of finite smoothness (see [54, Chapter 10]).
Assumptions2.We make the following assumptions on our encoding and decoding maps.
M.1ForR >0, we haveD X EX BR(X)⊂B R(X).
M.2The encoding/decoding maps and measurement space(E H, DH, ZH)associated with a space
H

J,(Ω j)J j=1,(n j)J j=1,(s j)J j=1,(p j)J j=1,(t j)J j=1,(q j)J j=1,(A j)J j=1 
satisfying AssumptionS.1are defined as follows:
(a) we define the point-evaluation mapE j :H j →R mj byE juj :=  uj(x1 j ), . . . , uj(xmj j )  and let
Zj := Ran(Ej);
(b) letD j :Z j → Hj denote the minimum-norm interpolant from Theorem 2.1;
(c) we define the measurement spaceZ H := QJ j=1 Zj,together with the componentwise encoding and
decoding maps
EH :H →ZH, E Hu:= (E juj)J j=1,
and
DH :Z H → H, D HU:= (D jUj)J j=1.
As shown in the proof of Theorem 2.1, ifD X is the minimum-norm interpolant, then AssumptionM.1
holds automatically.
Assumptions3.We make the following regularity assumptions on the mapG:X→Y.
O.1There existR >0and a nondecreasing functionω: [0,∞)→[0,∞)withω(0) = 0such that,
BR(X)⊂ D(G)and, for everyx, x′ ∈B R(X),
∥G(x)−G(x ′)∥Y ≤ω  ∥x−x ′∥X  .
7

O.2LetH X =H

JX ,(Ω X,j )JX j=1,(n X,j )JX j=1,(s X,j )JX j=1,(p X,j )JX j=1,(t X,j )JX j=1,(q X,j )JX j=1,(A X,j )JX j=1  andX=
X

JX ,(Ω X,j )JX j=1,(t X,j )JX j=1,(q X,j )JX j=1  satisfy AssumptionS.1. Likewise, letH Y =H  JY ,(Ω Y,k )JY k=1,
(nY,k )JY k=1,(s Y,k )JY k=1,(p Y,k )JY k=1,(t Y,k )JY k=1,(q Y,k )JY k=1,(A Y,k )JY k=1  andY=X  JY ,(Ω Y,k )JY k=1,(t Y,k )JY k=1,
(qY,k )JY k=1  satisfy AssumptionS.1.
• There existR >0and a nondecreasing functionω: [0,∞)→[0,∞)withω(0) = 0such that
BR(HX )⊂ D(G)and, for everyx, x′ ∈B R(HX ),
∥G(x)−G(x ′)∥Y ≤ω  ∥x−x ′∥X  .
• The operatorGmapsB R(HX )intoH Y , and there exists a constantM R >0such that
sup
x∈BR(HX )
∥G(x)∥HY ≤M R.
AssumptionO.1is an abstract continuity assumption on the operatorG:X→Y, expressed solely in
terms of the natural spacesXandY. It is sufficient to control the error introduced by reconstructing the input.
AssumptionO.2specializes to the Sobolev setting. Besides continuity in the weakerY-norm, it requires that
Gmaps sufficiently regular inputs into the stronger spaceH Y with uniformly boundedH Y -norm on bounded
subsets ofH X. This additional regularity is needed to derive quantitative Sobolev reconstruction rates.
Assumptions4 (Kernel learning in the encoder-decoder framework).We make the following assumptions on
our learning setup.
L.1LetΓ :Z X ×Z X → L(ZY )be an operator-valued kernel with reproducing kernel Hilbert spaceH Γ.
Letx 1, . . . , xN ∈Xbe training inputs and define measurementsU i :=E X xi ∈Z X .LetS i ∈Z Y ,for
i= 1, . . . , Nbe prescribed measured output data. Define the observation operator
LΓ,A :H Γ →Z N Y , L Γ,Af:= (Af(U 1), . . . , Af(UN )),
whereA:=E Y DY :Z Y →Z Y .WriteU= (U 1, . . . , UN ),S= (S 1, . . . , SN ),and define the block
operatorΓ A(U,U) :Z N Y →Z N Y by

ΓA(U,U)c

i :=
NX
j=1
AΓ(Ui, Uj)A∗cj, c= (c 1, . . . , cN )∈Z N Y .
ForU∈Z X, defineΓ A(U,U) :Z N Y →Z Y by
ΓA(U,U)c:=
NX
j=1
Γ(U, Uj)A∗cj.
WheneverA= Id ZY , we simply writeΓ(U,U)andΓ(U,U).
L.2Assume AssumptionL.1. In addition, letS i =E Y G(xi)and defineG enc(Ui) :=E Y G(DX Ui)∈Z Y
fori= 1, . . . , N. Letλ≥0. Ifλ= 0, assume thatΓ(U,U) :Z N Y →Z N Y is boundedly invertible.
Denote by bGλ(z)and bGenc,λ(z)the kernel interpolant (forλ= 0) or kernel ridge-regression estimator
of the measured dataS i and ideal encoded dataG enc(Ui), respectively. Let bG= bGλ and define G:=
DY ◦ bGλ ◦E X :X→Y.Define the residual smoother
RU,λη:Z X →Z Y ,(R U,λη)(U) := Γ(U,U)

Γ(U,U) +λId ZN Y
−1η, U∈Z X
whereη= (η 1, . . . , ηN )∈Z N Y withη i :=S i −G enc(Ui).
8

L.3LetH X =H

JX ,(Ω X,j )JX j=1,(n X,j )JX j=1,(s X,j )JX j=1,(p X,j )JX j=1,(t X,j )JX j=1,(q X,j )JX j=1,(A X,j )JX j=1  andX=
X

JX ,(Ω X,j )JX j=1,(t X,j )JX j=1,(q X,j )JX j=1  satisfy AssumptionS.1. Likewise, letH Y =H  JY ,(Ω Y,k )JY k=1,
(nY,k )JY k=1,(s Y,k )JY k=1,(p Y,k )JY k=1,(t Y,k )JY k=1,(q Y,k )JY k=1,(A Y,k )JY k=1  andY=X  JY ,(Ω Y,k )JY k=1,(t Y,k )JY k=1,
(qY,k )JY k=1  satisfy AssumptionS.1. LetGsatisfy AssumptionO.2. Assume AssumptionL.2. In addi-
tion, suppose thatZ HX ⊆R dX andZ HY ⊂R dY .LetΥ⊂Z HX be a bounded domain with Lipschitz
boundary such thatE HX

BR(HX )

⊂Υ.Define the encoded operator byG enc :=E HY ◦G◦D HX :
Υ→Z HY .Assume that the operator-valued kernel is defined onΓ : Υ×Υ→ L(R dY ),and that its
associated RKHS satisfies, for someτ > d X /2,we haveH Γ ,→H τ (Υ;R dY )continuously. Assume
furthermore thatG enc ∈ HΓ.
Let the training inputs satisfyx 1, . . . , xN ∈B R(HX ),so that
Ui =E HX xi ∈Υ, S i =E HY G(xi), i= 1, . . . , N.
Define the fill distance of the encoded training inputs inΥbyh tr := supU∈Υ min1≤i≤N ∥U−U i∥2.
AssumptionsL.1-L.3introduce increasingly specialized learning settings. AssumptionL.1specifies the
abstract kernel learning framework on the encoded spaces, including the training data and kernel notation,
without making any assumptions on the origin of the measurements. AssumptionL.2specializes this frame-
work to the encoder–decoder setting by assuming that the measurements arise from an underlying operator G,
thereby introducing the encoded operator, its kernel approximation, and the associated reconstruction operator.
Finally, AssumptionL.3specializes further to the Sobolev setting, where the encoder and decoder are con-
structed from product Sobolev spaces, the encoded domain is a bounded Lipschitz subset of a Euclidean space,
and additional Sobolev regularity assumptions are imposed on both the kernel RKHS and the encoded operator.
These assumptions enable the quantitative approximation estimates derived in the subsequent sections.
Remark3.2 (Regularity of the encoded operator).The assumption that the encoded operatorG enc belongs
to the RKHSH Γ in AssumptionS.1can be verified from regularity assumptions on the original operatorG.
Indeed, if the encoders and decoders are bounded linear operators (for example, the decoders are the minimum-
norm interpolants from Theorem 2.1), Fréchet differentiability is preserved under composition. More precisely,
ifG∈C k(X, Y),thenG enc =E Y ◦G◦D X also belongs toC k(ZX , ZY ), with
∥DkGenc(U)∥ ≤ ∥EY ∥ ∥DX ∥k∥DkG(DX U)∥
by [9, Lemma 3.3]. If the chosen RKHSH Γ contains sufficiently smooth functions (for example, through a
continuous embedding of an appropriate Sobolev space intoH Γ), then the assumptionG enc ∈ HΓ follows
directly from corresponding regularity assumptions onG.
3.2 General Learning Framework
The diagrams in Figure 2 summarize the abstract encoder–decoder formulation used throughout this section.
The proofs of the results in this section can be found in Appendix A.2.1.
9

X Y
ZX ZY
G
EX EY
bG
DYDX
(a) Encoder-decoder framework.
X Y
ZX ZY
G=D Y ◦ bG◦E X
EX EY
Genc =E Y ◦G◦D X
DYDX
(b) Approximation and ideal encoded map.
xi G(xi)
Ui Si andG enc(Ui)
G
EX EY
bGλ
DYDX
(c) Training data.
Figure 2: Schematic description of the proposed learning framework. (a) Encoder–decoder formulation for learning a map
G:X→Y. The mapsE X :X→Z X andE Y :Y→Z Y encode inputs and outputs into measurement spaces, while
DX :Z X →XandD Y :Z Y →Yreconstruct representatives in the original spaces. The surrogate bG:Z X →Z Y is
learned between the measurement spaces. (b) The learned surrogate induces the approximation G=D Y ◦ bG◦E X on
the original spaces, while the target map induces the encoded-space mapG enc :=E Y ◦G◦D X. Theorem 3.7 bounds
the error between GandG. (c) Location of the training data in the encoder–decoder framework. The training inputs
xi ∈Xare observed through the measurementsU i =E X xi ∈Z X, while the measured outputs areS i ∈Z Y . Learning
is performed entirely on the measurement spacesZ X andZ Y through a kernel learner bGλ (see Corollary 3.4). The
diagram also highlights the encoded target valuesG enc(Ui) =E Y G(DX Ui). When the training outputs are chosen as
Si =E Y G(xi), one error term in Theorem 3.7 depends on the discrepancyη i :=S i −G enc(Ui), which measures the
mismatch between the measured data and the ideal encoded target.
Our goal is to approximate a target mapG:X→Ybetween Hilbert spaces from measured data. In many
settings, however, the data do not provide direct access to elements ofXandY. Instead, inputs and outputs are
observed only through bounded linear measurement, or encoding, mapsE X :X→Z X andE Y :Y→Z Y ,
whereZ X andZ Y are Hilbert measurement spaces. We therefore pose the learning problem on the latter
spaces: given measured input–output pairs(E X (xi), EY (G(xi)))∈Z X ×Z Y ,one first constructs a surrogate
bG:Z X →Z Y .
To obtain an approximation of the original mapG:X→Y, we then decode the predicted output measurement
and define
(4) G:=D Y ◦ bG◦E X :X→Y,
whereD Y :Z Y →Yis an output reconstruction map. Thus, the method learns where the data are observed
and then lifts the learned prediction back to the original output space. This formulation is particularly useful
whenXandYare infinite-dimensional function spaces, whileZ X andZ Y are finite-dimensional, lower-
dimensional, or otherwise computationally tractable representations.
If the target mapGwere known, the natural map to use between the measurement spaces would be
Genc :=E Y ◦G◦D X :Z X →Z Y ,
whereD X :Z X →Xis a chosen input reconstruction map. Indeed, if the decoding maps are chosen so that
DX ◦E X ≈Id X andD Y ◦E Y ≈Id Y ,then usingG enc in place of bGin (4) gives
DY ◦G enc ◦E X =D Y ◦E Y ◦G◦D X ◦E X ≈G.
This observation separates the encoder–decoder construction in Figure 2a into two coupled tasks:
• Reconstruction: choose decoding mapsD X andD Y that lift measurements back to meaningful repre-
sentatives in the original spaces;
• Learning: approximate the unknown measurement-space mapG enc :Z X →Z Y from measured training
pairs by constructing a surrogate bG:Z X →Z Y .
We first address the reconstruction task. The given mapsE X andE Y typically aim to produce simpler or
more tractable representations of objects inXandY, and are therefore not expected to be injective. A single
measurement may consequently correspond to many elements of the original space, so the decoding mapsD X
andD Y cannot be obtained by ordinary inversion. To resolve this ambiguity, we choose a canonical decoder
by minimum-norm recovery:
DX (U) := argmin
x∈X
{∥x∥X :E X x=U}, D Y (S) := argmin
y∈Y
{∥y∥Y :E Y y=S}.
10

This selects, among all elements compatible with the measurements, the one of smallest Hilbert norm, where
the norm encodes the chosen notion of complexity on the underlying space.
In some situations however, exact consistency with the measurements may be undesirable or ill-conditioned,
for instance when the measurements are noisy or when the operatorsE X ◦E ∗ X and/orE Y ◦E ∗ Y are poorly
conditioned. One may then replace the hard constraints by a regularized recovery problem. Forγ >0, this
gives
DX,γ (U) := argmin
x∈X

∥x∥2 X +γ −1∥EX x−U∥ 2 ZX 	 ,
and
DY,γ (S) := argmin
y∈Y

∥y∥2 Y +γ −1∥EY y−S∥ 2 ZY 	 .
A major advantage of both the constrained and regularized formulations is that they lead to explicit reconstruc-
tion formulas given in Theorem 2.1.
We now turn to the learning task. The choice of learning method depends on the structure of the measure-
ment spacesZ X andZ Y , and involves a trade-off between expressivity, numerical complexity, and theoretical
tractability. In this way, richer model classes may capture more complex maps between measurements, while
more structured methods often lead to explicit formulas and sharper analysis. We focus on kernel methods
for the learning step. This choice is motivated by the analytical and computational structure they provide:
minimum-norm interpolation, regularized regression, deterministic error bounds, and kernel-based uncertainty
quantification can all be written in closed form. In addition, kernel methods interact naturally with the encoder–
decoder construction. As our first result shows, a kernel on the measurement spaces induces a corresponding
kernel on the original spaces. Specifically, any operator-valued kernel
Γ :Z X ×Z X → L(ZY )
induces an operator-valued kernel
K:X×X→ L(Y).
Theorem 3.3(Encoder–decoder induced operator-valued kernel).Assume thatD Y :Z Y →Yis a bounded
linear output decoder. LetΓ :Z X ×Z X → L(ZY )be an operator-valued kernel with associated RKHSH Γ of
mapsZ X →Z Y . DefineK:X×X→ L(Y)by
K(x, x′) :=D Y Γ(EX x, EX x′)D ∗ Y .
ThenKis an operator-valued kernel onXwith values inL(Y). Moreover, the associated RKHS is
HK ={D Y ◦f◦E X :f∈ HΓ},
equipped with the minimal-representative norm
∥F∥ HK = inf{∥f∥ HΓ :F=D Y ◦f◦E X }.
Suppose, in addition, thatE X andE Y are surjective and that the decodersD X :Z X →XandD Y :
ZY →Yare given by the exact minimum-norm recovery maps from Theorem 2.1. Then, the representation
F=D Y ◦f◦E X
is unique and the minimal-representative norm reduces to the identity
∥DY ◦f◦E X ∥HK =∥f∥ HΓ.
As a consequence of Theorem 3.3, when the surrogatebGis constructed by kernel interpolation or regression
on the measurement spaces, the full approximation
G=D Y ◦ bG◦E X :X→Y
can itself be interpreted as a kernel method acting directly fromXtoY. In other words, although the learning
problem is posed on the measurement spacesZ X andZ Y , the resulting reconstructed operator belongs to an
operator-valued RKHS of maps fromXtoY.
We now detail the equivalence of learning frameworks.
11

Corollary 3.4(Equivalence of induced and measurement-space learning problems).Assume the setting of
Theorem 3.3 and that AssumptionL.1is satisfied. Forλ≥0, consider the induced RKHS problem
min
F∈H K
(
λ−1
NX
i=1
∥EY F(x i)−S i∥2 ZY +∥F∥ 2 HK
)
.
Forλ= 0, this is understood as the minimum-norm interpolation problem
min
F∈H K
∥F∥ 2 HK subject toE Y F(x i) =S i, i= 1, . . . , N.
This problem is equivalent to the encoded measurement-space problem
min
f∈H Γ
(
λ−1
NX
i=1
∥Af(U i)−S i∥2 ZY +∥f∥ 2 HΓ
)
.
Again, forλ= 0, this is understood as the minimum-norm interpolation problem
min
f∈H Γ
∥f∥ 2 HΓ subject toAf(U i) =S i, i= 1, . . . , N.
Ifλ= 0, further assume thatL Γ,A is surjective, equivalently thatΓ A(U,U) =L Γ,AL∗ Γ,A is boundedly in-
vertible onZ N Y . Then, the encoded measurement-space solution and the corresponding induced RKHS solution
are
f λ(U) = Γ A(U,U)

ΓA(U,U) +λId ZN Y
−1Sand F λ(x) =D Y ΓA(EX x,U)  ΓA(U,U) +λId ZN Y −1S.
Suppose now, in addition, thatE X,E Y are surjective and thatD X,D Y are the exact minimum-norm
recovery maps from Theorem 2.1. Then, the encoded measurement-space problems reduce to the standard
measurement-space problems
min
f∈H Γ
∥f∥ 2 HΓ subject tof(U i) =S i, i= 1, . . . , N,
and
min
f∈H Γ
(
λ−1
NX
i=1
∥f(U i)−S i∥2 ZY +∥f∥ 2 HΓ
)
.
Ifλ= 0, further assume thatΓ(U,U)is boundedly invertible. Then, the encoded measurement-space solution
and the corresponding induced RKHS solution are
f λ(U) = Γ(U,U)

Γ(U,U) +λId ZN Y
−1S, F λ(x) =E ∗ Y (EY E∗ Y )−1Γ(EX x,U)  Γ(U,U) +λId ZN Y −1S.
Remark3.5 (Pointwise learning in the encoded space).While the encodersE X andE Y may be constructed
from arbitrary bounded linear measurements, the induced learning problem is simply a pointwise regression
problem on the encoded spacesZ X andZ Y , where the training data consist of the encoded pairs(Ui, Si).Con-
sequently, the kernel learning theory depends only on the geometry of the encoded spaces and is independent
of the particular measurement modality used to constructE X andE Y .
Remark3.6 (Measurement transferability).The encoder–decoder construction in Figure 2a naturally induces
a notion of measurement transferability, as illustrated in Figure 3 and similarly discussed in [9, Section 2.4].
Consider an alternative pair of measurement spaceseZX and eZY , together with measurement and reconstruction
maps
eEX :X→ eZX , eDX : eZX →X,
and
eEY :Y→ eZY , eDY : eZY →Y.
The previously learned surrogate bGthen induces an alternative measurement-space surrogate
eG:= eEY ◦D Y ◦ bG◦E X ◦ eDX : eZX → eZY .
12

Thus, data represented in eZX can first be reconstructed inX, encoded into the original learning spaceZ X,
propagated through bG, reconstructed inY, and finally remeasured in eZY . The corresponding approximation
of the original map is
eDY ◦ eG◦ eEX :X→Y.
In this sense, the learned surrogate is transferable across different choices of input and output measurements:
it can be transported to alternative measurement systems through the associated reconstruction and remeasure-
ment maps, without retraining bG.
A particularly important case arises whenXandYare spaces of continuous functions and
EX :X→R cW , E Y :Y→R cY
are point-evaluation maps on prescribed input and output grids. Alternative maps eEX and eEY then correspond
to different sets of evaluation points. In this setting, measurement transferability becomes mesh transferability:
a surrogate trained using one pair of grids can be transferred to another pair of grids through reconstruction and
resampling. This mesh transferability is a defining feature of (multiple) operator learning. Indeed, methods
such as DeepONet [35], FNO [30], MNO [51–53] and related architectures are designed to learn mappings
between function spaces rather than between fixed finite-dimensional vectors, allowing predictions on dis-
cretizations different from those used during training. Remark 3.19 discusses an alternative approach in which
the learned representation is directly evaluable independently of a prescribed output mesh.
The next result separates the total error into an encoder–decoder error and a learning error. The first term
measures how well the measurement and reconstruction maps preserve the action of the continuum mapG.
The second term measures how well the surrogate bGapproximates the encoded-space targetG enc.When bG
is chosen by kernel interpolation on the measurement space, the learning error can be further bounded by a
kernel residual term, together with a data-consistency term accounting for the possible mismatch between the
measured training outputsE Y G(xi)and the encoded target valuesG enc(EX xi)(see Figure 2c).
Theorem 3.7(Encoder–decoder and learning error decomposition).We have the following error decomposi-
tions.
1. Let bG:Z X →Z Y be any surrogate, and define G:=D Y ◦ bG◦E X :X→Y.Then, for everyx∈X,
∥G(x)− G(x)∥Y ≤ ∥G(x)−DY EY G(DX EX x)∥Y
+∥D Y (Genc − bG)(EX x)∥Y .
2. Assume that AssumptionL.2is satisfied.
(a) For everyx∈X,
∥G(x)− G(x)∥Y ≤ ∥G(x)−DY EY G(DX EX x)∥Y +∥D Y ∥op ∥(Genc − bGenc,λ)(EX x)∥ZY
+∥D Y ∥op ∥RU,λη(EX x)∥ZY .
X Y
ZX ZY
eZX eZY
G
EX
eEX
EY
eEY
bG
DX DY
eDX
eG
eDY
Figure 3: Measurement transferability of the encoder-decoder learning framework. The mapsE X :X→Z X and
EY :Y→Z Y encode inputs and outputs into measurement spaces, whileD X :Z X →XandD Y :Z Y →Y
reconstruct representatives in the original spaces. The surrogate bG:Z X →Z Y is learned between the measurement
spaces. The additional measurement and reconstruction maps induce an alternative surrogate eG:= eEY ◦D Y ◦ bG◦E X ◦ eDX : eZX → eZY and approximation eDY ◦ eG◦ eEX ofG.
13

(b) Define the regularized residual kernel
Γ⊥ λ (U, U′) := Γ(U, U′)−Γ(U,U)  Γ(U,U) +λId ZN Y −1Γ(U, U′), U, U ′ ∈Z X
and furthermore assume that, for everyU∈Z X,Tr

Γ⊥ λ (U, U)  <∞.With
QN,λ(U) :=

Tr

Γ⊥ λ (U, U)  +λTr(Id ZY ) 1/2 ,
for everyx∈X,
∥G(x)− G(x)∥Y ≤ ∥G(x)−DY EY G(DX EX x)∥Y +∥D Y ∥op QN,λ(EX x)∥G enc∥HΓ,λ
+∥D Y ∥op ∥RU,λη(EX x)∥ZY
whereH Γ,λ is the RKHS with kernelΓ(U, U′) +λId ZY δU,U ′.
The goal of Section 3.3 is to progressively sharpen the error decomposition of Theorem 3.7 by imposing
additional assumptions on the operatorG, the spacesXandY, the encoder–decoder pairs(E X , DX )and
(EY , DY ), and the available data.
3.3 Kernel Learning for Multi-Input, Multi-Output Operators
In this section, we focus on the setting of multi-input, multi-output operator learning, where the underlying
function spaces are Sobolev spaces, the encoders are given by pointwise sampling operators, and the decoders
reconstruct functions from these pointwise observations. This setting encompasses many problems arising
from partial differential equations and allows us to derive explicit error bounds. The proofs of the results in
this section can be found in Appendix A.2.2.
We begin by examining the data-consistency term in Theorem 3.7.
Remark3.8 (Consistent measured training data).If the measured training outputs are consistent with the
encoded-space target, namely
EY G(xi) =G enc(EX xi) =E Y G(DX EX xi), i= 1, . . . , N,
thenη i =S i −G enc(Ui) = 0.Consequently,R U,λη= 0and the data-consistency term in Theorem 3.7
vanishes: for everyx∈X,
∥G(x)− G(x)∥Y ≤ ∥G(x)−DY EY G(DX EX x)∥Y +∥D Y ∥op ∥(Genc − bGenc,λ)(EX x)∥ZY .
A sufficient condition for this consistency is exact input reconstruction on the training data, that is
DX EX xi =x i, i= 1, . . . , N.
Next, we analyze the reconstruction error of the mapG.
Proposition 3.9(Encoder–decoder reconstruction error).Suppose that there exist functionsδ X :X→[0,∞)
andδ Y :Y→[0,∞),such that
(5)
(
∥x−D X EX x∥X ≤δ X (x), x∈X,
∥y−D Y EY y∥Y ≤δ Y (y), y∈Y.
Assume thatGsatisfies AssumptionO.1and that AssumptionM.1is satisfied.
Then, for everyx∈B R(X),
∥G(x)−D Y EY G(DX EX x)∥Y ≤ω(δ X (x)) +δ Y (G(DX EX x)).
If, in addition,X= QJX j=1 Xj,andY= QJY j=1 Yj,with product norms∥x∥ 2 X = PJX j=1 ∥xj∥2 Xj ,and∥y∥ 2 Y = PJY
j=1 ∥yj∥2 Yj ,and there exist componentwise reconstruction bounds
(
∥xj −(D X EX x)j∥Xj ≤δ X,j (x), x∈X, j= 1, . . . , JX ,
∥yj −(D Y EY y)j∥Yj ≤δ Y,j (y), y∈Y, j= 1, . . . , JY ,
14

then
∥G(x)−D Y EY G(DX EX x)∥Y ≤ω




JXX
j=1
δX,j (x)2


1/2
 +


JYX
j=1
δY,j (G(DX EX x))2


1/2
.
Remark3.10 (Componentwise and coupled measurements).Proposition 3.9 does not require the encoder or
decoder to act componentwise. While independent measurements of each component are the most common
situation in operator learning, more general measurement procedures naturally arise in several applications
[44, 49].
When one considers products of Sobolev space, we can explicitly bound the reconstruction errors in terms
of the fill distance as the next result shows.
Lemma 3.11(Recovery estimate for products of Sobolev-embedded Hilbert spaces).LetH=H

J,(Ω j)J j=1,
(nj)J j=1,(s j)J j=1,(p j)J j=1,(t j)J j=1,(q j)J j=1,(A j)J j=1  andX=X  J,(Ω j)J j=1,(t j)J j=1,(q j)J j=1  satisfy As-
sumptionS.1, and let(E H, DH, ZH)be the associated encoding/decoding maps and measurement space from
AssumptionM.2.
Then, there exist constantsh 0 j >0andC j >0, independent ofh j andu j, such that, wheneverh j ≤h 0 j ,
one has
∥uj −D jEjuj∥Wtj ,qj (Ωj ) ≤C jh
sj −tj −nj

1
pj − 1 qj

+
j ∥uj∥Hj
for everyu j ∈ Hj. Consequently, for everyu∈ H,
∥u−D HEHu∥X ≤


JX
j=1
C2 j h
2

sj −tj −nj

1
pj − 1 qj

+
!
j ∥uj∥2 Hj


1/2
.
Remark3.12 (Fractional Sobolev orders).For simplicity, Lemma 3.11 is stated for integer Sobolev orderst j ∈
N0. This is because its proof relies on [3, Theorem 4.1], which establishes the required sampling inequalities
for integer target orders. By instead appealing to [4, Theorem 3.1], the same argument extends to fractional
Sobolev orders, yielding an analogous result for arbitraryt j ≥0within the admissible range.
We continue by considering the learning-error term. The latter can be estimated in several ways. In this
work, we adopt an approach based on Sobolev embeddings and sampling inequalities, which yields explicit
convergence rates under suitable regularity assumptions on the reproducing kernel Hilbert space. This frame-
work naturally accommodates vector-valued kernels and is particularly well suited to the encoder–decoder
setting considered here.
Lemma 3.13(Learning error in a finite-dimensional RKHS).LetΥ⊂R dX be a bounded domain with Lips-
chitz boundary, and letU={U 1, . . . , UN } ⊂Υbe a finite sampling set with fill distance
htr := sup
U∈Υ
min
1≤i≤N
∥U−U i∥2.
LetΓ : Υ×Υ→ L(R dY )be an operator-valued kernel with associated RKHSH Γ. Assume that, for some
τ > dX 2 ,there is a continuous embeddingH Γ ,→H τ (Υ;R dY )≃H τ (Υ)dY .
Letf∈ HΓ, and denote by bfλ the kernel interpolant, whenλ= 0, or the kernel ridge-regression estimator,
whenλ >0, associated with the exact data

(Ui, f(Ui))
	N
i=1.Ifλ= 0, assume thatΓ(U,U) : (R dY )N →
(RdY )N is boundedly invertible. Definee λ :=f− bfλ.
Letq∈[1,∞], setγ:= max{2, q},and let0≤s≤ℓ(τ, q, d X ),where
ℓ(τ, q, d) =



ℓ0(τ, q, d),ifτ∈Nand eitherq= 2orq >2withℓ 0(τ, q, d)∈N,
⌈ℓ0(τ, q, d)⌉ −1,otherwise,
15

with
ℓ0(τ, q, d) :=τ−d
 1
2 − 1 q  + .
Whenq=∞, assume additionally thats∈N 0.
Then, there exist constantsh 0 >0andC >0, independent ofh tr,λ, andf, such that, wheneverh tr ≤h 0,
one has
|eλ|Ws,q(Υ;RdY ) ≤C

h
τ−s−d X

1
2 − 1 q

+
tr +h dX /γ−s tr √ λ
!
∥f∥ HΓ.
Consequently, for everyU∈Υ,
∥eλ(U)∥ 2 ≤C

hτ−d X /2 tr + √ λ  ∥f∥ HΓ.
Remark3.14 (Alternative estimates via the power function).The Sobolev-based approach of Lemma 3.13 is
not the only way to estimate the learning error. An alternative is to bound the interpolation error directly
in terms of the associated power function (see Theorem 3.7). For example, in the scalar-valued kernel case,
the decay of the power function can be estimated from the smoothness of the reproducing kernel, leading to
convergence rates in terms of the fill distance; see, for example, [54].
Theorem 3.15(Reconstruction guarantees for kernel multi-input, multi-output learning).LetH X =H

JX ,
(ΩX,j )JX j=1,(n X,j )JX j=1,(s X,j )JX j=1,(p X,j )JX j=1,(t X,j )JX j=1,(q X,j )JX j=1,(A X,j )JX j=1  andX=X  JX ,(Ω X,j )JX j=1,
(tX,j )JX j=1,(q X,j )JX j=1  satisfy AssumptionS.1. Likewise, letH Y =H  JY ,(Ω Y,k )JY k=1,(n Y,k )JY k=1,(s Y,k )JY k=1,
(pY,k )JY k=1,(t Y,k )JY k=1,(q Y,k )JY k=1,(A Y,k )JY k=1  andY=X  JY ,(Ω Y,k )JY k=1,(t Y,k )JY k=1,(q Y,k )JY k=1  satisfy Assump-
tionS.1. Let(E HX , DHX , ZHX )and(E HY , DHY , ZHY )be the associated encoding maps, decoding maps,
and measurement spaces from AssumptionM.2. Assume thatGsatisfies AssumptionO.2. Letd X := PJX j=1 mX,j
andd Y := PJY k=1 mY,k ,so thatZ HX ⊆R dX andZ HY ⊆R dY .Assume that AssumptionL.3is satisfied.
Then, there exist constantsC >0,h 0 tr >0,h 0 X,j >0,h 0 Y,k >0independent of the fill distances,λ, and the
functions being reconstructed, such that, wheneverh tr ≤h 0 tr, hX,j ≤h 0 X,j forj= 1, . . . , JX andh Y,k ≤h 0 Y,k
fork= 1, . . . , JY , one has, for everyx= (x 1, . . . , xJX )∈B R(HX ),the estimate
∥G(x)− G(x)∥Y ≤ω

CRmax
1≤j≤JX
h
sX,j −tX,j −nX,j

1
pX,j − 1 qX,j

+
X,j


+CM R max 1≤k≤JY h
sY,k −tY,k −nY,k

1
pY,k − 1 qY,k

+
Y,k
+∥D Y ∥op C

hτ−d X /2 tr + √ λ  ∥Genc∥HΓ +∥D Y ∥op ∥RU,λη(EX x)∥2
Remark3.16 (Sample-sensor complexity trade-off).One important results would be to derive a joint complex-
ity bound that balances the number of sensors against the number of sampled training operators. Such a result
is difficult because the statistical learning error depends on the fill distance of the encoded training samples
inZ X, which is generally not directly tractable. The encoded training points are obtained by applying the
encoder to the original training inputs, and there is no reason for them to form a quasi-uniform or otherwise
space-filling design in the encoded space. Existing convergence results in kernel-based operator learning typ-
ically circumvent this difficulty by assuming that the encoded training points become dense in the encoded
domain (see [9, Theorem 3.4]), without explicitly quantifying the decay of the corresponding fill distance as
a function of the number of training samples. A possible approach towards such quantitative estimates would
be to study optimal experimental design inZ X, selecting training inputs whose encoded representations min-
imize the fill distance. Under suitable geometric assumptions on the encoded manifold, or by constructing
quasi-uniform designs directly in the encoded space and mapping them back to admissible inputs via suit-
able preimages or the decoder, one may then obtain explicit trade-offs between the number of sensors and the
number of required training operators.
16

Remark3.17 (Scaling with the number of tasks).The reconstruction terms in Theorem 3.15 exhibit the same
qualitative scaling behaviour as the approximation results obtained for multiple operator learning with neural
operators. As shown in [52], passing from a single operator to multiple related operators, either through
concatenation [52, Theorem 3.29] or through dedicated architectures [52, Theorem 3.19], need not alter the
approximation exponent, i.e., the approximation rates are governed by the least regular (or most difficult)
task, rather than suffering from a compounding deterioration of the approximation exponent with the number
of tasks. An analogous phenomenon appears in the reconstruction part of the present kernel-based estimate.
The input and output reconstruction errors are controlled by the largest componentwise discretization errors.
Consequently, the associated convergence exponents are determined by the least favorable Sobolev regularity
among the component spaces, rather than by the number of components itself.
The kernel-learning term requires a separate discussion. Its convergence rate is governed byh τ−d X /2 tr ,and
therefore depends on the dimensiond X of the encoded measurement space and the regularity of the encoded
operatorG enc. Since adding tasks typically increases the total number of measurements, and hence the di-
mension of the encoded measurement space, the learning rate may deteriorate accordingly. This dependence
is inherited from the underlying single-operator kernel approximation theory rather than from the multi-task
formulation itself.
Remark3.18 (Extension to other measurement operators).The Sobolev reconstruction results presented in
Theorem 3.15 are derived for pointwise measurements. However, as noted in Remark 3.5, the subsequent
learning analysis is independent of the particular choice of measurements and only requires the encoded train-
ing dataE X (xi)∈Z X andE Y (yi)∈Z Y . Consequently, as noted in [9], the present framework extends
immediately to other bounded linear measurement operators, provided that suitable reconstruction estimates
are available (i.e. analogues of Lemma 3.11).
More precisely, suppose that the encodersE X andE Y are constructed from a family of bounded linear
measurements (e.g., local averages as in [43, Lemma 14.34], moments, Fourier coefficients, or other sensor
functionals), and that the corresponding decoders satisfy approximation estimates analogous to those estab-
lished here for point evaluations. Then the encoder–decoder error decomposition, the RKHS construction,
and all subsequent kernel learning results remain unchanged. Only the reconstruction estimates need to be
replaced by the corresponding sampling inequalities for the chosen measurements. This separation highlights
the modular structure of the framework: the measurement modality enters exclusively through the approxima-
tion properties of the encoder-decoder pair, whereas the kernel learning theory depends only on the resulting
finite-dimensional encoded spaces.
Extending the framework to genuinely infinite-dimensional measurement spacesZ X andZ Y would re-
quire two additional ingredients. First, one would need sampling inequalities for bounded linear measurement
operators taking values in infinite-dimensional Hilbert spaces, such as trace operators, distributed observation
operators, or other function-valued measurements. Second, the Sobolev reconstruction theory developed in
this section would need to be extended to encoder–decoder pairs with infinite-dimensional encoded spaces,
yielding approximation estimates analogous to Lemma 3.13. Once such reconstruction results are available,
the abstract encoder–decoder framework and the subsequent kernel learning analysis apply without essential
modification.
3.4 Kernel Methods for Multi-Task Operator Learning
Theorem 3.15 provides a general error estimate for kernel-based encoder–decoder learning of maps between
product spaces of functions,
G:X 1 × · · · ×XJX − →Y1 × · · · ×YJY ,
where each component may represent a different modality, parameter, or function space. As a special case, it
naturally recovers the kernel operator learning framework of [9], depicted in figure 4a and corresponding to
the choiceJ X =J Y = 1. As a further important example and application, we now specialize this framework
to multi-task/multiple operator learning, where the objective is to learn
G:W− → {G[α] :U→V} α∈W ,
assigning to each task parameterα∈Wan operatorG[α] :U→V. While we focus on this representative
application, the insights developed below, including the different formulations, their statistical and compu-
17

tational properties, and the settings in which each formulation is most appropriate, apply equally to general
product-space learning problems.
We begin by introducing two equivalent viewpoints of the multiple operator learning problem. These
are illustrated in figures 4b and 4c. The first learns the operator-valued map assigning an operator to each
parameter, while the second casts the same problem as learning the product-space map
G′ :W×U→V, G ′(α, u) =G[α](u).
U V
ZU ZV
G
EU EV
bG
DVDU
(a) Operator learning.
W {G[α] :U→V}
ZW ZO
G
EW EO
bG
DODW
(b) Operator-valued learning.
W×U V
ZW×U ZV
G′
EW×U EV
cG′
DVDW×U
(c) Product-space learning.
Figure 4: Encoder–decoder formulations for classical operator learning and multiple operator learning. (a) Classical
operator learning, where a single operatorG:U→Vis learned from measurements in the Hilbert spacesZ U andZ V [9].
(b) Operator-valued multiple operator learning, where the objective is to learn the mapG:W→ {G[α] :U→V} α∈W
that assigns an operator to each parameter, using measurement spacesZ W andZ O. (c) Product-space multiple operator
learning, where the same problem is represented by the mapG ′ :W×U→V, defined byG ′(α, u) =G[α](u), with
measurement spacesZ W×U andZ V . In each formulation, the encoder mapsEmap the original inputs and outputs into
abstract Hilbert measurement spaces, the decoder mapsDreconstruct representatives in the original spaces, and bG(or
bG′ in figure (c)) denotes the learned surrogate.
Although both formulations solve the same learning problem, they represent different prediction tasks.
The operator-valued formulation learns an entire solution operatorG[α] :U→Vfor each parameterα,
so that a prediction consists of reconstructing the complete operator: this is therefore particularly attractive
when one wishes to repeatedly query the same operator for many different input functions. In contrast, the
product-space formulation learns individual operator evaluations through the mapG ′ :W×U→V. Thus, it
directly predicts the solution corresponding to a single parameter–input pair(α, u), making it a natural choice
when only isolated evaluations are required or when different parameters are associated with different input
functions.
These differing representations lead to distinct statistical and computational properties. The operator-
valued formulation generalizes only across the parameter spaceW, while the product-space formulation si-
multaneously generalizes across both the parameter spaceWand the input spaceU. On the other hand, the
operator-valued formulation requires one training sample per operator, whereas the product-space formulation
requires one sample for every parameter–input pair. As a result, the size of the kernel matrix in the operator-
valued approach scales with the number of operators, while the product-space formulation scales with the
total number of parameter–input pairs. The operator-valued formulation is therefore expected to be consider-
ably more computationally efficient whenever each operator is observed on many input functions, whereas the
product-space formulation offers greater flexibility by learning directly over the joint parameter–input domain.
Table 1 summarizes the principal differences between the two formulations. In Section 4, we compare both
approaches empirically in terms of predictive performance and computational efficiency.
W×U×Ω V R
ZW×U×Ω V
G′′
E cG′′D
Figure 5: Complete product-space formulation of multiple operator learning. Instead of learning the operator-valued map
G:W→ {U→V}or the product-space mapG ′ :W×U→V, this formulation learns the pointwise evaluation map
G′′ :W×U×Ω V →R, defined byG ′′(α, u, x) =G[α](u)(x). The encoderEmaps parameter–input–location triples
into a measurement space, while the decoderDreconstructs representatives in the original product space. The learned
surrogate cG′′ predicts the solution value at individual spatial locations.
18

Operator-valued learning Product-space learning
Learned mapG:W→ {U→V}G ′ :W×U→V
PredictionEntire operatorG[α]Single operator evaluationG[α](u)
GeneralizationParameter spaceWParameter spaceWand input spaceU
Typical settingMultiple tasks sharing common input func-
tions
Multiple tasks with varying input functions
Training samplesn α operatorsn αnu parameter–input pairs
Size of kernel matrixn α ×n α (nαnu)×(n αnu)
Theoretical guaran-
tees
Theorem 3.15 withJ X =J Y = 1(for
integral operators)
Theorem 3.15 withJ X = 2, JY = 1
Table 1: Comparison of the two multiple operator learning formulations. The operator-valued formulation predicts entire
operators and generalizes across the parameter space, whereas the product-space formulation predicts individual operator
evaluations and simultaneously generalizes across both the parameter and input spaces. Here,n α denotes the number of
operators (or parameter instances) in the training set, andn u denotes the number of input functions associated with each
operator.
Remark3.19 (Alternative mesh-transferability).An alternative formulation to those depicted in Figure 4 is
obtained by learning the pointwise evaluation map
G′′ :W×U×Ω V →R,(α, u, x)7→G[α](u)(x),
rather than the operator-valued mapG:W→ {U→V}or the product-space mapG ′ :W×U→
V; see Figure 5. In this setting, the spatial coordinate is treated as an additional input variable, so that the
learned surrogate directly predicts the solution value at any query location. Consequently, the resulting model
is naturally mesh-independent and can be evaluated on arbitrary output discretizations directly.
The increased flexibility comes at a significant computational cost. Each training sample now corresponds
to a parameter–input–location triple(α, u, x), so that the number of training examples grows proportionally
to the product of the number of parameters, input functions, and output locations. Accordingly, kernel meth-
ods require solving linear systems whose size scales with the total number of such triples, leading to sub-
stantially higher memory and computational complexity than either the operator-valued or product-space for-
mulations. For this reason, we focus on the two formulations in Figures 4b and 4c, which already provide
mesh-transferability through the encoder–decoder framework while remaining computationally tractable.
Among the two formulations introduced above, the product-space formulation in Figure 4c fits directly
within the setting of Theorem 3.15 by choosingJ X = 2andJ Y = 1, with input spaceW×Uand output
spaceV. As a consequence, all approximation, reconstruction, and learning guarantees developed in Section
3.2 apply immediately.
The operator-valued formulation of Figure 4b is more subtle. Although the encoder-decoder framework
itself is formulated abstractly, the quantitative reconstruction theory developed in this work specializes to prod-
ucts of Hilbert spaces of functions admitting Sobolev embedding so that Sobolev sampling inequalities provide
reconstruction error estimates as in Lemma 3.11. Consequently, applying the present theory to operator-valued
learning requires the operator space to admit an appropriate realization as a function space. This is naturally
the case for many important classes of operators, including integral operators [10, 14]
(T f)(x) =
Z
Ω
k(x, y)f(y) dy,
which are canonically identified with their kernelsk. Such operators arise throughout scientific computing, for
example as Green’s operators for boundary value problems, kernel integral transforms such as the Fourier and
19

Laplace transforms, and many classes of nonlocal operators [15–17]. Under this identification, the operator-
valued learning problem becomes a classical operator learning problem in which the outputs are the kernel
functionsk. In other words, the operator-valued mapG:W→ {U→V}is identified with a function-
valued mapG:W→K,so that the general encoder-decoder theory of Theorem 3.15 applies directly with
JX =J Y = 1. The resulting learning guarantees are therefore those of kernel operator learning. From the
perspective of the encoder–decoder framework, the principal difference is that the outputs now belong to a
Sobolev space over the product domainΩ×Ω, rather thanΩ. Thus, the reconstruction rates inherited from
the Sobolev sampling inequalities depend on the dimension of the product domain, typically leading to more
stringent sampling requirements than in the standard setting.
We leave the extension of the reconstruction theory developed here directly to general spaces of operators,
without relying on an underlying functional representation, as a future work. Such a theory would substantially
broaden the applicability of kernel-based encoder-decoder learning and could enable analogous approximation,
reconstruction, and learning guarantees for genuinely operator-valued prediction problems.
Remark3.20 (Learning maps between measures).As with the integral operators discussed above, the encoder–
decoder framework can also accommodate learning problems involving measures that are absolutely contin-
uous with respect to a fixed reference measure and whose densities belong to the function spaces considered
in Section 3.3. Identifying each measure with its density reduces the measure-valued learning problem to a
function-valued one, allowing the approximation theory developed above to be applied directly.
4 Numerical Experiments
In this section, we evaluate the performance and efficiency of our proposed kernel-based multiple operator
learning methods for both operator-valued learning and product-space learning, depicted in Figures 4b and
4c, respectively. The code implementing both methods and reproducing all numerical experiments is publicly
available athttps://github.com/liaochunyang/kernelMO.
Learning task.We consider five representative parametric PDEs which were also studied in [53]. In all
experiments, we learn the solution operator(α, u0)7→u,mapping a parametric function/parametersαand an
initial conditionu 0 to the complete solution trajectoryu: (0,2]×[0,2]→R,(t, x spatial)7→u(t, x spatial).
Thus, our models predict the full spatio-temporal evolution of the PDE solution, whereas the experiments in [9]
predict the solution only at a fixed timet=t 0.
Sampling of initial conditions and parameter functions.We generate the initial conditions using the sinu-
soidal construction proposed in [48]:
(6)u 0(x) =
2X
i=1
Ai sin(πnix+ϕ i),
where the amplitudesA i are sampled uniformly from[0,1], the frequenciesn i are sampled uniformly from
the integers{1, . . . ,4}, and the phasesϕi are sampled uniformly from(0,2π). As in [48], each sampled
initial condition is post-processed by flipping its sign with probability0.5. The construction of the parameter
functionsαis PDE-specific and is described below.
Training datasetsFor each learning formulation, we train all models on the same underlying collection
of parametric functions and initial conditions. The two learning formulations differ only in how this data is
organized. For the operator-valued formulation, each training sample consists of an entire operator represented
through its evaluations on a common set of probe functions. The training dataset is therefore
Dop =
n
αi,

G[αi](uj)
	20
j=1
o320
i=1
,
where the initial conditionsu 1, . . . , u20 are fixed across all parameter instances. In contrast, the product-space
formulation treats each parameter–input pair as an individual training sample. The corresponding dataset is
Dprod ={(α i, uj, G[αi](uj)) :i= 1, . . . ,200, j= 1, . . . ,50}.
20

Test set Setting#parametric functions#initial conditionsN test
In-distribution Operator-valued 80 2080×20 Product-space 80 5080×50
Out-of-distribution Operator-valued 40 2040×20 Product-space 80 5080×50
Table 2: Number of parametric functions, number of initial conditions, and number of test samples for in-distribution
and out-of-distribution sets under both settings. In the operator-valued setting, the initial conditions are fixed across all
settings. In the product-space setting, the initial conditions are distinct.
Remark4.1 (Fixed initial conditions in the operator-valued formulation).In the operator-valued learning for-
mulation in figure 4b, the initial conditions are kept fixed across all parameter instances. This reflects the
fact that each training sample corresponds to an entire operator rather than a single operator evaluation. More
precisely,E O is the common encoder, mapping each operator to its evaluations on a fixed collection of input
functions together with a fixed discretization of the output domain. This ensures that all operators are repre-
sented in the same measurement spaceZ O. Varying the initial conditions would represent different encoding
maps and thus alter the operator-valued learning problem. In contrast, the product-space formulation naturally
permits different initial conditions for each parameter instance, since each training sample corresponds to a
single parameter–input pair rather than an entire operator.
We additionally evaluate the generalization capabilities of each framework using several out-of-distribution
(OOD) datasets. In the operator-valued formulation, the initial conditions are fixed and shared across all
parameter instances, so we only consider OOD parameter functions. In the product-space formulation, where
both the parameter functions and initial conditions are sampled, we consider OOD parameter functions, OOD
initial conditions, and the joint OOD setting in which both are sampled from distributions not encountered
during training. Details of the construction of all OOD datasets are provided in Appendix B.1. In Table 2, we
report the numbers of parametric functions, initial conditions, and test samples in in-distribution and out-of-
distribution test sets under both settings.
Methods and benchmarks.We evaluate the proposed kernel-based multiple operator learning framework
against both classical operator learning methods and existing multiple operator learning architectures.
•Proposed methods.We consider the proposed kernel-based multiple operator learning framework, de-
noted by KernelMO, with operator-valued and product-space variants KernelMO-OV and KernelMO-PS,
respectively.
•Classical Operator Learning benchmarks.These methods do not explicitly account for multiple opera-
tors. We consider:
–KernelO [9], the single operator learning kernel method corresponding to the formulation in fig-
ure 4a;
–DeepONet [35], the standard neural operator architecture corresponding to the same formulation.
Both methods treat the initial condition as the sole input and the PDE solution as the output, without
incorporating the parameter function.
•Multiple Operator Learning benchmarks.We compare against several architectures specifically designed
or adapted for multiple operator learning:
–DeepONet-C [52,53], a variant of DeepONet in which the parameter function and initial condition
are concatenated into a single input function;
–MIONet [25], which employs separate branch networks for each input function and combines their
latent representations through a tensor-product operation;
–MNO [53], which uses separate neural networks for the parametric function, input function, and
spatial coordinates before combining their latent representations.
21

All kernel-based models are trained by solving a minimum-norm interpolation optimization problem. All
neural-network-based method are trained with mean squared loss.
Remark4.2 (Well-posedness of the operator-valued learning problem).The classical operator learning base-
lines (KernelO and DeepONet) cannot be accurately trained in the operator-valued setting because they ignore
the parameter functionα. Their induced training set would be
{(uj, G[αi](uj))}j=1,...,m i=1,...,N ,
where the probe functionsu 1, . . . , um are fixed across all parameter instances (see Remark 4.1). Since there
generally existα 1 ̸=α 2 such thatG[α 1](uj)̸=G[α 2](uj),the same inputu j is paired with multiple outputs.
Thus, the induced training set does not define a functionU→V, and classical operator learning methods
are not applicable. In contrast, the product-space formulation is trained on individual triples(α, u, G[α](u)),
rather than collections of outputs evaluated on a fixed set of probe functions. Thus, every input is associated
with a unique output, and the resulting supervised learning problem is well defined.
For the proposed KernelMO methods, the theoretical framework employs matrix-valued kernels. In prac-
tice, we use separable kernels of the form
K(x, x′) =k(x, x′) Id,
wherekis a scalar-valued kernel andIddenotes the identity matrix of appropriate dimension. For KernelMO-
OV, the inputs consist solely of the parametric functions, and we therefore choose
k:W×W→R.
For KernelMO-PS, the inputs are pairs(α, u)∈W×Uand we use the product kernel
k

(α1, u1),(α 2, u2)

=k W (α1, α2)kU (u1, u2)
for kernelsk W :W×W→Randk U :U×U→R. The hyperparameters fork,k W , andk U are selected
independently. For completeness, we also train KernelMO-PS on the Cartesian set of(α, u)pairs underlying
the operator-valued dataset. This allows the two kernel formulations to be compared using exactly the same
PDE evaluations.
We also consider two representations of the sampled data for the proposed kernel methods. In the first,
each function is represented directly by its pointwise values at the observation locations, and kernel regression
is performed on these high-dimensional observations. Since numerical simulations only provide sampled func-
tion values, this corresponds to the standard discrete kernel learning setting. Although this does not employ the
encoder–decoder framework, it still constitutes a novel kernel-based multiple operator learning method under
the proposed operator-valued and product-space formulations. We therefore include it as a high-dimensional
baseline to isolate the effect of the encoder–decoder approach. In the second, we employ principal component
analysis (PCA) to obtain a low-dimensional latent representation of the sampled observations. Kernel regres-
sion is then performed in this latent space, and the learned representation is mapped back to the observation
space through the inverse PCA transform. This corresponds to the full encoder–decoder framework analyzed
in Section 3.2. Throughout the experiments, we refer to the corresponding operator-valued and product-space
variants as KernelMO-OV (PCA) and KernelMO-PS (PCA), respectively.
Remark4.3 (Construction of the PCA representation).The PCA bases are computed from the training data.
In the product-space formulation, we construct a single PCA basis for the parametric functions, a single PCA
basis for the initial conditions, and a single PCA basis for the solution functions. These bases are shared
across all training samples. In the operator-valued formulation, a single PCA basis is likewise constructed for
the parametric functions. The probe functionsu 1, . . . , um are fixed and are therefore not encoded. Instead,
for each probe functionu j, we compute a separate PCA basis from the collection of corresponding solution
functions
{G[αi](uj)}N i=1.
Thus, the outputs associated with each fixed probe function are encoded in their own latent space, which is
shared across all parameter instances.
22

Evaluation metric.We evaluate all models on withheld test datasets consisting of in-distribution samples
and out-of-distribution samples (see Table 2). For each test case, the predicted and reference solution functions
are evaluated on a128×64spacetime grid over[0,2]×[0,2]. For each test sample, we compute the relative
L2 error
ei =
∥u(i) pred −u (i) target∥2
∥u(i) target∥2
where(u (i) pred, u(i) target)corresponds to thei-th pair of predicted and reference solution functions, each evaluated
at all points of discretized spacetime grid. We report the mean relativeL 2 error
1
Ntest
NtestX
i=1
ei,
together with the corresponding standard deviation computed over the test samples.
Hyperparameter optimization.For the kernel-based methods, we consider both radial basis function (RBF,
denoted by R) and Matérn (denoted by M) kernels and perform a simple hyperparameter search. We denote the
corresponding methods by appending the latent representation and kernel choice. For example, KernelMO-OV
(PCA) / R and KernelMO-OV (PCA) / M denote the operator-valued method with a PCA representation and
an RBF or Matérn kernel, respectively. For the product-space formulation, we specify the kernel family used
on each input component separately. Thus, KernelMO-PS (PCA) / M×M denotes Matérn kernels on both
the parameter and initial-condition spaces, while KernelMO-PS (PCA) / R×R denotes an RBF kernel on the
parameter space and a RBF kernel on the initial-condition space. The same notation applies to the KernelO
method as well.
For the RBF kernel, we search over the length-scale parameterγ={0.01,0.1,1,10,100}. For the Matérn
kernel, we search over the length-scale parameterγ={0.01,0.1,1,10,100}and the smoothness parameter
ν={1/2,3/2,5/2,7/2}. Exact hyperparameter choices are detailed in Appendix B.2. For neural-networks-
based methods, we consider three different network sizes, referred to as small, medium, and large. In Table 3,
we summarize the architectures and the corresponding numbers of trainable parameters.
small medium large
DeepONet 0.29M 2.15M 9.48M
DeepONet-C 0.31M 2.17M 9.53M
MIONet 0.32M 2.22M 9.73M
MNO 0.60M 1.22M 16.70M
Table 3: Summary of number of trainable parameters for each architecture and network size. "M" denotes million.
4.1 Performance
We begin this section with a summary of the main experimental findings. Figures 6 and 7 provide an overview
of the relative performance of all methods across the five PDE benchmarks for the operator-valued and product-
space formulations, respectively. In addition, Figures 8 and 9 show representative sample trajectories from
the test datasets for both formulations on all PDE benchmarks. Detailed quantitative results for each PDE
benchmark are presented in the subsequent subsections, while representative results on some of the out-of-
distribution datasets are shown in Figures 10-19.
Across the five PDE benchmarks, the proposed kernel-based methods are consistently competitive with,
and in most cases substantially outperform, the neural operator baselines, as illustrated by the predominance of
light-colored cells for the proposed methods in Figures 6 and 7. Their largest gains are generally observed on
the in-distribution test sets, where the prediction error is often reduced by one or two orders of magnitude. For
example, in operator-valued learning, on the conservation law the best kernel methods reduce the error from
1.23%for MIONet to0.01%, while on the nonlinear Klein–Gordon equation the error decreases from4.63%
23

Conservation LawDiffusion-Reaction-AdvectionNonlinear Klein–GordonParametric Diffusion-ReactionParametric Wave
KernelMO-OV / M 1.00 1.52 1.32 1.00 1.71
KernelMO-OV / R 4.55 1.03 2.24 10.3 5.18
KernelMO-OV (PCA) / M 90.0 1.89 1.98 19.8 1.31
KernelMO-OV (PCA) / R 90.3 1.47 2.88 20.5 1.02
KernelMO-PS / M×M 1.00 1.79 1.32 2.17 1.71
KernelMO-PS / R×R 76.0 5.25 27.7 16.7 1.72
KernelMO-PS (PCA) / M×M 90.0 2.11 1.98 19.8 1.29
KernelMO-PS (PCA) / R×R 120 5.33 27.7 23.3 1.01
DeepONet-C 202 4.74 31.7 14.7 6.66
MIONet 65.3 9.27 23.5 12.7 7.49
MNO 94.6 2.52 13.3 9.19 7.27
Figure 6: Summary of normalized performance in the operator-valued-learning experiments. For each methodm, PDEp,
and associated test datasetd, we compute the normalized errorErrorm,p,d/min m′ Errorm′,p,d,whereError m,p,d denotes
the mean relative error. Consequently, the best-performing method on each test dataset attains the value1. For each PDE,
the displayed value is obtained by averaging the normalized errors over all associated test datasets (one in-distribution
and all out-of-distribution datasets). Lighter colors indicate better performance.
24

Conservation LawDiffusion-Reaction-AdvectionNonlinear Klein–GordonParametric Diffusion-ReactionParametric Wave
KernelO / M 3.97 5.89 28.0 4.90 15.3
KernelO / R 2.25 139 141 3.96 125
KernelO (PCA) / M 2.20 4.39 27.8 4.91 15.7
KernelO (PCA) / R 1.88 26.7 56.5 3.81 22.6
KernelMO-PS / M×M 1.23 1.04 1.10 1.45 1.67
KernelMO-PS / R×R 1.94 1.27 3.04 14.4 1.79
KernelMO-PS (PCA) / M×M 1.32 1.03 1.20 14.8 1.13
KernelMO-PS (PCA) / R×R 1.82 1.26 2.02 21.8 1.00
DeepONet 2.10 3.61 20.6 4.25 10.7
DeepONet-C 1.36 1.24 8.13 1.83 4.08
MIONet 2.30 3.34 10.4 3.11 5.27
MNO 1.23 1.14 3.35 1.46 5.11
Figure 7: Summary of normalized performance in the product-space-learning experiments. For each methodm, PDE
p, and associated test datasetd, we compute the normalized errorError m,p,d/min m′ Errorm′,p,d,whereError m,p,d
denotes the mean relative error. Consequently, the best-performing method on each test dataset attains the value1. For
each PDE, the displayed value is obtained by averaging the normalized errors over all six associated test datasets (one
in-distribution and five out-of-distribution datasets). Lighter colors indicate better performance.
Figure 8: Qualitative summary across PDEs for operator-valued learning. Columns correspond to conservation law,
diffusion-reaction-advection, nonlinear Klein-Gordon, parametric diffusion-reaction, parametric wave. The top row
shows the reference solution for one selected trajectory from the test split; the bottom row shows the signed predic-
tion error for the kernel method with the smallest mean relative error.
25

Figure 9: Qualitative summary across PDEs for product-space learning. Columns correspond to conservation law,
diffusion-reaction-advection, nonlinear Klein-Gordon, parametric diffusion-reaction, parametric wave. The top row
shows the reference solution for one selected trajectory from the test split; the bottom row shows the signed predic-
tion error for the kernel method with the smallest mean relative error.
for MNO to0.21%. The proposed methods also frequently attain the lowest out-of-distribution errors, although
the relative improvement depends more strongly on the governing PDE and the type of distribution shift.
The operator-valued and product-space formulations exhibit complementary strengths. The KernelMO-OV
methods are particularly well-suited to operator-valued learning, generally outperforming the KernelMO-PS
variants and obtaining the lowest in-distribution errors on the conservation law (0.01%), diffusion–reaction–
advection equation (0.38%), nonlinear Klein–Gordon equation (0.21%), and parametric diffusion–reaction
equation (0.06%). Its PCA-based variants also frequently provide the best out-of-distribution performance.
For product-space learning, KernelMO-PS consistently outperforms the corresponding single-kernel baseline
KernelO (e.g.2.13%versus59.28%for the parametric wave equation) and remains competitive with, or
superior to, the neural operator baselines across most benchmarks.
The comparison between the full and PCA-based variants reveals no universal ordering. PCA substantially
reduces the dimensionality of the encoded inputs and outputs while often preserving most of the predictive ac-
curacy and, in several experiments, improving out-of-distribution generalization. For example, on the nonlinear
Klein–Gordon equation in operator-valued learning, the OOD error decreases from6.72%for KernelMO-OV /
M to4.11%for KernelMO-OV (PCA) / M. Likewise, for the parametric wave equation in product-space learn-
ing, KernelMO-PS (PCA) / R×R substantially improves the most challenging distribution shifts compared
with its non-PCA counterpart (46.20%versus99.55%). On the other hand, PCA introduces a moderate loss
of in-distribution accuracy on some benchmarks; for instance, in operator-valued learning, on the conservation
law, the error increases from0.01%to1.77%, while on the parametric diffusion–reaction equation it increases
from0.06%to3.04%. Thus, PCA should primarily be viewed as a computationally efficient representation that
can additionally provide a regularization effect, rather than as a uniformly accuracy-improving transformation.
The choice of kernel is similarly problem dependent. Matérn kernels generally provide the strongest and
most stable performance, particularly for the conservation law, nonlinear Klein–Gordon equation, and paramet-
ric diffusion–reaction equation. For example, in operator-valued learning, on the conservation law, KernelMO-
OV / M achieves an OOD error of0.77%, compared with5.47%for the RBF kernel. Likewise, on the para-
metric diffusion–reaction equation, KernelMO-OV / M attains OOD errors of3.53%,4.05%, and0.12%on the
three distribution shifts, whereas KernelMO-OV / R reaches56.22%,83.90%, and0.33%. RBF kernels can
nevertheless attain extremely small in-distribution errors. The clearest example is the product-space parametric
diffusion–reaction experiment, where KernelMO-PS / R×R achieves the lowest in-distribution error (0.75%).
Finally, the experiments reveal no universal out-of-distribution trend across all PDEs. Generalization de-
pends strongly on both the governing equation and the nature of the distribution shift. Overall, OOD prediction
is consistently more challenging than in-distribution prediction for all methods, highlighting the intrinsic diffi-
culty of extrapolating beyond the training distribution. Changes in initial-condition amplitude are, for example,
particularly challenging for the nonlinear Klein–Gordon equation in product-space learning, where all meth-
ods incur large OOD errors, although KernelMO-PS still achieves the lowest overall error. Across operator-
26

valued and product-space learning, in the parametric wave equation, changing the Gaussian-process kernel
(OOD_matern) or its length scale (OOD_scale) is also challenging. Across several benchmarks, we further
note that PCA-based variants exhibit improved robustness under distribution shift, suggesting that the reduced
latent representation can provide a useful regularization effect (e.g. from 3.37% to 2.47% for KernelMO-PS/
M×M in product-space learning for the nonlinear Klein Gordon equation).
4.1.1 Conservation Laws
We consider the following one-dimensional conservation law with periodic boundary conditions:
ut + (α1u+α 2u2 +α 3u3)x =α 4uxx,(t, x)∈[0,2]×[0,2]
u(0, x) =u0(x),
u(t,0) =u(t,2),
where the components of parameter vectorα= [α 1, α2, α3, α4]⊤ are sampled from the rangesα i ∈[0.9α c i ,
1.1αc i ], with the reference values given byα c = [1,1,1,0.1] ⊤.
Operator-Valued Learning.The mean relative errors and standard deviations are summarized in Table 4,
while the implementation details and hyperparameter choices are summarized in Table 17. Overall, the
proposed kernel-based methods achieve the lowest prediction errors on both the in-distribution and out-of-
distribution datasets and the best performance is obtained with the Matérn kernel. Compared with the best-
performing neural operator baselines, the proposed methods can improve the prediction accuracy by ap-
proximately two orders of magnitude on the in-distribution test set (from1.23%for MIONet to0.01%for
KernelMO-OV/ M and KernelMO-PS/ M×M) and by a factor of approximately five on the out-of-distribution
dataset (from3.97%for MNO to0.77%for KernelMO-OV/ M and KernelMO-PS/ M×M). Applying PCA
substantially reduces the dimensionality of the learning problem while incurring a loss of accuracy, however,
the PCA-based variants remain highly competitive. For example, KernelMO-OV (PCA) / M and KernelMO-PS
(PCA) / M×M achieve prediction errors of1.77%on the in-distribution test set and2.32%on the out-of-
distribution dataset, compared with1.23%for MIONet and3.97%for MNO, respectively.
Method / kernel Test OOD
KernelMO-OV/ M 0.01% (0.02%) 0.77% (1.54%)
KernelMO-OV/ R0.02% (0.02%) 5.47% (6.40%)
KernelMO-OV (PCA)/ M 1.77% (0.43%) 2.32% (1.21%)
KernelMO-OV (PCA)/ R 1.77% (0.43%) 2.82% (1.65%)
KernelMO-PS/ M x M 0.01% (0.02%) 0.77% (1.54%)
KernelMO-PS/ R x R1.46% (1.09%) 4.63% (5.02%)
KernelMO-PS (PCA) / M x M1.77% (0.43%) 2.32% (1.21%)
KernelMO-PS (PCA) / R x R2.34% (0.90%) 5.15% (4.74%)
DeepONet-C 3.96% (0.74%) 5.56% (2.75%)
MIONet 1.23% (0.28%) 5.86% (7.64%)
MNO 1.84% (0.34%) 3.97% (4.09%)
Table 4: Operator-valued learning: performance comparison on the conservation laws. We report mean relative errors
with standard deviations in parentheses on in-distribution and out-of-distribution datasets.
27

Figure 10: Operator-valued learning: qualitative prediction and uncertainty comparison for the conservation law on the
OOD dataset. The first row shows a reference solution and signed prediction errors for four kernel variants; the relative
error for the displayed trajectory is reported in each error-figure title. The second row shows the final-time solution,
predictive mean, and an uncertainty band of±2predictive standard deviations.
Product-Space Learning.The mean relative errors and standard deviations are summarized in Table 5, while
the implementation details and hyperparameter choices are summarized in Table 18. Overall, the proposed
kernel-based methods achieve the lowest prediction errors on the in-distribution test set, with the best per-
formance obtained by KernelMO-PS / M×M using the Matérn kernel. Compared with the best-performing
neural operator baseline, the proposed method improves the prediction accuracy by approximately a factor
of two on the in-distribution test set (from3.29%for MNO to1.76%for KernelMO-PS / M×M). Across
the out-of-distribution datasets, different methods achieve the best performance under different distribution
shifts. Nevertheless, the proposed product-kernel methods consistently rank among the top-performing ap-
proaches, demonstrating strong robustness and improved generalization ability. Applying PCA substantially
reduces the dimensionality of the learning problem while incurring only a moderate loss of accuracy. For ex-
ample, KernelMO-PS (PCA) / M×M achieves a prediction error of2.96%on the in-distribution test set while
maintaining competitive performance across all out-of-distribution datasets.
Method / kernel Test OOD_par OOD_init_GP OOD_init_amp OOD_par_init_GP OOD_par_init_amp
KernelO / M 6.67% (5.45%)3.98% (3.28%)14.18% (8.47%) 46.93% (20.19%) 17.41% (9.52%) 47.18% (19.88%)
KernelO / R 4.76% (3.21%) 7.50% (5.17%) 10.29% (3.50%) 16.32% (6.36%) 14.65% (6.48%) 16.93% (6.20%)
KernelO (PCA) / M 6.97% (5.11%) 4.82% (2.84%) 13.28% (7.60%) 10.31% (4.10%) 16.63% (9.21%) 11.21% (4.70%)
KernelO (PCA) / R 5.34% (2.88%) 7.87% (4.92%) 10.30% (3.53%) 7.20% (1.86%) 14.63% (6.49%) 8.15% (2.63%)
KernelMO-PS / M x M 1.76% (1.52%)6.24% (4.24%) 5.57% (3.69%)6.18% (1.99%)10.80% (7.57%) 9.05% (3.49%)
KernelMO-PS / R x R2.97% (2.15%) 9.36% (6.46%) 8.59% (3.65%) 10.38% (3.61%) 16.25% (9.51%) 14.84% (7.75%)
KernelMO-PS (PCA) / M x M2.96% (1.13%) 6.10% (3.60%) 5.81% (3.38%) 6.35% (1.90%) 10.04% (7.17%) 8.63% (3.11%)
KernelMO-PS (PCA) / R x R3.79% (1.73%) 9.21% (5.84%) 8.56% (3.65%) 6.68% (1.82%) 15.65% (9.19%) 11.61% (7.45%)
DeepONet 6.77% (2.80%) 8.49% (4.16%) 10.55% (3.62%) 8.36% (2.29%) 14.70% (6.46%) 9.23% (3.03%)
DeepONet-C 4.42% (0.92%) 4.88% (1.22%) 6.22% (1.68%) 7.66% (2.11%)6.92% (2.61%)7.83% (2.10%)
MIONet 4.32% (1.31%) 8.90% (9.79%) 6.37% (2.83%) 21.98% (11.22%) 10.74% (11.55%) 21.09% (10.83%)
MNO 3.29% (1.05%) 4.79% (2.88%)5.46% (1.71%)7.04% (2.11%) 8.25% (4.96%)7.49% (2.30%)
Table 5: Product-space learning: performance comparison on the conservation law. We report mean relative errors with
standard deviations in parentheses on in-distribution and out-of-distribution datasets.
28

Figure 11: Product-space learning: qualitative prediction and uncertainty comparison for the conservation law on the
OOD_par dataset. The first row shows a reference solution and signed prediction errors for four kernel variants; the
relative error for the displayed trajectory is reported in each error-figure title. The second row shows the final-time
solution, predictive mean, and an uncertainty band of±2predictive standard deviations.
4.1.2 Diffusion-Reaction-Advection
We consider the following one-dimensional diffusion-reaction-advection equation:
ut =α 1uxx +α 2ux +α 3uα4(1−u α5),(t, x)∈[0,2]×[0,2]
u(0, x) =u0(x),
u(t,0) =u(t,2),
where the first three components of parameter vectorα= [α 1, α2, α3, α4, α5]⊤ are sampled from the ranges
αi ∈[0.9α c i ,1.1α c i ], with the reference values given byα c = [0.01,1,1] ⊤, whileα 4 andα 5 are drawn uni-
formly from[1,3].
Operator-Valued Learning.The mean relative errors and standard deviations are summarized in Table 6,
while the implementation details and hyperparameter choices are summarized in Table 19. Overall, the
proposed kernel-based methods achieve the lowest prediction errors on both the in-distribution and out-of-
distribution datasets. The best in-distribution performance is obtained by KernelMO-OV / R, while the lowest
out-of-distribution error is achieved by KernelMO-OV (PCA) / R. Compared with the best-performing neural
operator baseline, the proposed methods improve the prediction accuracy by more than a factor of three on the
in-distribution test set (from1.21%for MNO to0.38%for KernelMO-OV / R) and by nearly a factor of two
on the out-of-distribution dataset (from6.58%for MNO to3.53%for KernelMO-OV (PCA) / R). Applying
PCA substantially reduces the dimensionality of the learning problem while preserving the strong predictive
performance of the proposed methods, and even slightly improves the out-of-distribution accuracy for the RBF
kernel.
29

Method / kernel Test OOD
KernelMO-OV / M0.60% (0.51%) 5.18% (4.80%)
KernelMO-OV / R 0.38% (0.38%)3.72% (3.94%)
KernelMO-OV (PCA) / M0.88% (0.46%) 5.17% (4.63%)
KernelMO-OV (PCA) / R0.74% (0.34%)3.53% (3.50%)
KernelMO-PS / M x M0.79% (0.66%) 5.33% (4.59%)
KernelMO-PS / R x R2.87% (1.41%) 10.42% (6.48%)
KernelMO-PS (PCA) / M x M1.03% (0.60%) 5.30% (4.44%)
KernelMO-PS (PCA) / R x R2.93% (1.38%) 10.43% (6.46%)
DeepONet-C 2.89% (0.63%) 6.61% (3.59%)
MIONet 5.56% (1.43%) 13.80% (7.08%)
MNO 1.21% (0.34%) 6.58% (5.85%)
Table 6: Operator-valued learning: performance comparison on the diffusion-reaction-advection equation. We report
mean relative errors with standard deviations in parentheses on in-distribution and out-of-distribution datasets.
Figure 12: Operator-valued learning: qualitative prediction and uncertainty comparison for the diffusion-reaction-
advection equation on the OOD dataset. The first row shows a reference solution and signed prediction errors for four
kernel variants; the relative error for the displayed trajectory is reported in each error-figure title. The second row shows
the final-time solution, predictive mean, and an uncertainty band of±2predictive standard deviations.
Product-Space Learning.The mean relative errors and standard deviations are summarized in Table 7, while
the implementation details and hyperparameter choices are summarized in Table 20. On the in-distribution test
set, the proposed product-kernel methods achieve prediction errors comparable to the best-performing neu-
ral operator baseline, with KernelMO-PS / M×M attaining a mean relative error of2.55%, compared with
2.25%for MNO. On the out-of-distribution datasets, however, the proposed methods consistently outperform
the neural operator baselines. In particular, KernelMO-PS (PCA) / M×M achieves the lowest prediction
errors on four of the five out-of-distribution datasets, while KernelMO-PS / M×M achieves the best perfor-
mance on the remaining one. Applying PCA substantially reduces the dimensionality of the learning problem
while preserving the strong predictive performance of the proposed methods. Moreover, the proposed product-
kernel methods consistently outperform the corresponding vanilla kernel methods, highlighting the advantage
of explicitly modeling the product-space structure inherent in multiple operator learning problems.
30

Method / kernel Test OOD_par OOD_init_GP OOD_init_amp OOD_par_init_GP OOD_par_init_amp
KernelO / M 18.81% (10.19%) 8.27% (4.83%) 23.00% (14.71%) 48.20% (19.41%) 28.09% (16.11%) 48.77% (18.81%)
KernelO / R 12.63% (5.46%) 15.83% (7.18%) 233.85% (153.11%) 2589.43% (1249.39%) 233.85% (155.23%) 2590.93% (1250.92%)
KernelO (PCA) / M 18.80% (10.23%) 8.30% (4.80%) 22.46% (15.23%) 15.59% (6.05%) 27.65% (16.62%) 17.48% (6.71%)
KernelO (PCA) / R 12.64% (5.45%) 15.84% (7.17%) 115.56% (122.83%) 347.07% (255.06%) 116.17% (113.67%) 347.40% (255.15%)
KernelMO-PS / M x M2.55% (1.54%)4.57% (3.74%)3.16% (1.50%) 7.29% (2.74%) 6.16% (3.76%) 8.16% (2.84%)
KernelMO-PS / R x R2.77% (2.54%) 5.92% (5.13%) 3.88% (2.07%) 7.28% (2.69%) 9.37% (6.11%) 9.92% (5.75%)
KernelMO-PS (PCA) / M x M2.61% (1.50%) 4.61% (3.67%)3.15% (1.50%) 6.86% (2.44%) 6.15% (3.76%) 7.77% (2.70%)
KernelMO-PS (PCA) / R x R2.83% (2.44%) 5.88% (5.02%) 3.85% (2.05%) 7.15% (2.64%) 9.25% (6.03%) 9.74% (5.67%)
DeepONet 13.14% (5.11%) 15.98% (6.83%) 15.33% (6.18%) 13.76% (4.52%) 21.37% (9.38%) 15.40% (5.30%)
DeepONet-C 3.46% (0.73%) 5.91% (3.32%) 3.65% (0.96%) 8.37% (2.85%) 6.34% (3.97%) 9.10% (2.90%)
MIONet 5.71% (1.35%) 16.22% (13.97%) 9.66% (3.88%) 30.24% (14.11%) 17.47% (13.65%) 28.18% (13.38%)
MNO2.25% (0.74%)5.62% (4.48%) 3.33% (1.32%) 8.16% (2.90%) 7.15% (5.14%) 9.27% (3.23%)
Table 7: Product-space learning: performance comparison on the diffusion-reaction-advection equation. We report mean
relative errors with standard deviations in parentheses on in-distribution and out-of-distribution datasets.
Figure 13: Product-space learning: qualitative prediction and uncertainty comparison for the diffusion-reaction-advection
equation on the OOD_init_GP dataset. The first row shows a reference solution and signed prediction errors for four
kernel variants; the relative error for the displayed trajectory is reported in each error-figure title. The second row shows
the final-time solution, predictive mean, and an uncertainty band of±2predictive standard deviations.
4.1.3 Nonlinear Klein-Gordon
We consider the following nonlinear Klein–Gordon equation:
utt =α 2 1uxx −α 2 2α4 1u−α 3u3,(t, x)∈[0,2]×[0,2]
u(0, x) =u0(x),
ut(0, x) = 0,
u(t,0) =u(t,2).
The components of the parameter vectorα= [α 1, α2, α3]⊤ are sampled from the rangesα i ∈[0.9α c i ,1.1α c i ]
with reference valuesα c = [1,1,1] ⊤.
Operator-Valued Learning.The mean relative errors and standard deviations are summarized in Table 8,
while the implementation details and hyperparameter choices are summarized in Table 21. Overall, the
proposed kernel-based methods achieve the lowest prediction errors on both the in-distribution and out-of-
distribution datasets. The best in-distribution performance is obtained by KernelMO-OV / M and KernelMO-
PS / M×M, while the lowest out-of-distribution error is achieved by their PCA-based variants. Compared with
the best-performing neural operator baseline, the proposed methods improve the prediction accuracy by more
than one order of magnitude on the in-distribution test set (from4.63%for MNO to0.21%for KernelMO-OV
/ M and KernelMO-PS / M×M) and by more than a factor of four on the out-of-distribution dataset (from
18.50%for MNO to4.11%for KernelMO-OV (PCA) / M and KernelMO-PS (PCA) / M×M). Applying PCA
substantially reduces the dimensionality of the learning problem while further improving the out-of-distribution
performance.
31

Method / kernel Test OOD
KernelMO-OV / M 0.21% (0.19%)6.72% (9.13%)
KernelMO-OV / R0.37% (0.24%) 11.17% (24.33%)
KernelMO-OV (PCA) / M0.62% (0.28%)4.11% (6.96%)
KernelMO-OV (PCA) / R0.68% (0.33%) 10.39% (23.80%)
KernelMO-PS / M x M 0.21% (0.19%)6.72% (9.13%)
KernelMO-PS / R x R10.22% (6.85%) 27.57% (27.58%)
KernelMO-PS (PCA) / M x M0.62% (0.28%)4.11% (6.96%)
KernelMO-PS (PCA) / R x R10.23% (6.84%) 27.57% (27.58%)
DeepONet-C 12.17% (3.64%) 22.06% (14.84%)
MIONet 8.41% (2.83%) 28.46% (31.09%)
MNO 4.63% (1.46%) 18.50% (19.36%)
Table 8: Operator-valued learning: performance comparison on the nonlinear Klein-Gordon equation. We report mean
relative errors with standard deviations in parentheses on in-distribution and out-of-distribution datasets.
Figure 14: Operator-valued learning: qualitative prediction and uncertainty comparison for the Nonlinear Klein-Gordon
equation on the OOD dataset. The first row shows a reference solution and signed prediction errors for four kernel
variants; the relative error for the displayed trajectory is reported in each error-figure title. The second row shows the
final-time solution, predictive mean, and an uncertainty band of±2predictive standard deviations.
Product-Space Learning.The mean relative errors and standard deviations are summarized in Table 9, while
the implementation details and hyperparameter choices are summarized in Table 22. Overall, the proposed
product-kernel methods achieve the lowest prediction errors on the in-distribution test set and consistently out-
perform the neural operator baselines across the out-of-distribution datasets. In particular, KernelMO-PS / M
×M attains the lowest in-distribution test error of0.31%, compared with2.84%for the best-performing neural
operator baseline MNO, corresponding to an improvement of approximately one order of magnitude. Across
the out-of-distribution datasets, KernelMO-PS (PCA) / M×M achieves the best performance on four of the
five datasets, while KernelMO-PS / M×M performs best on the remaining one. Applying PCA substan-
tially reduces the dimensionality of the learning problem while preserving the strong predictive performance
of the proposed methods. Finally, we observe that the datasets involving out-of-distribution initial-condition
amplitudes (OOD_init_amp and OOD_par_init_amp) are substantially more challenging for all methods, as
the unseen initial conditions contain higher-frequency modes that are absent from the training data, leading to
more oscillatory solution dynamics and larger prediction errors.
32

Method / kernel Test OOD_par OOD_init_GP OOD_init_amp OOD_par_init_GP OOD_par_init_amp
KernelO / M 41.28% (27.25%) 28.12% (15.75%) 24.95% (14.78%) 59.59% (16.29%) 35.95% (20.22%) 65.80% (14.20%)
KernelO / R 28.94% (14.46%) 42.95% (19.50%) 434.20% (297.77%) 5811.74% (2849.27%) 431.33% (289.06%) 5672.18% (2787.12%)
KernelO (PCA) / M 41.25% (27.26%) 28.12% (15.74%) 24.64% (14.83%) 46.81% (12.42%) 35.78% (20.42%) 57.36% (14.91%)
KernelO (PCA) / R 28.94% (14.46%) 42.95% (19.50%) 214.07% (218.27%) 766.86% (609.60%) 213.33% (202.18%) 750.18% (594.53%)
KernelMO-PS / M x M 0.31% (0.24%)8.36% (12.27%) 2.10% (1.33%)31.79% (12.65%)3.37% (2.18%) 32.90% (11.56%)
KernelMO-PS / R x R0.90% (0.66%) 15.81% (25.30%) 7.79% (5.67%) 90.45% (40.93%) 9.13% (5.77%) 90.30% (38.01%)
KernelMO-PS (PCA) / M x M0.68% (0.35%)7.18% (11.64%) 2.02% (1.27%)31.94% (12.74%)2.47% (1.68%) 32.75% (11.78%)
KernelMO-PS (PCA) / R x R1.01% (0.66%) 14.86% (24.83%) 4.22% (4.19%) 36.08% (14.83%) 5.86% (4.84%) 40.08% (16.84%)
DeepONet 28.58% (12.44%) 45.35% (19.29%) 18.55% (8.38%) 42.43% (9.25%) 31.65% (16.22%) 53.09% (12.07%)
DeepONet-C 10.25% (3.58%) 23.42% (17.12%) 8.23% (2.08%) 36.52% (12.09%) 14.55% (10.46%) 43.00% (12.97%)
MIONet 11.19% (2.60%) 35.97% (35.71%) 13.26% (9.19%) 72.59% (32.71%) 26.00% (26.60%) 66.93% (29.43%)
MNO 2.84% (0.70%) 18.94% (20.61%) 3.98% (1.69%) 32.50% (12.60%) 10.29% (9.00%) 37.93% (12.55%)
Table 9: Product-space learning: performance comparison on the nonlinear Klein-Gordon equation. We report mean
relative errors with standard deviations in parentheses on in-distribution and out-of-distribution datasets.
Figure 15: Product-space learning: qualitative prediction and uncertainty comparison for the nonlinear Klein-Gordon
equation on the OOD_par_init_amp dataset. The first row shows a reference solution and signed prediction errors for
four kernel variants; the relative error for the displayed trajectory is reported in each error-figure title. The second row
shows the final-time solution, predictive mean, and an uncertainty band of±2predictive standard deviations.
4.1.4 Parametric Diffusion-Reaction Equation
We consider the following parametric diffusion-reaction equation:
ut = (α(x)ux)x +u(1−u),(t, x)∈[0,2]×[0,2]
u(0, x) =u0(x),
u(t,0) =u(t,2),
where the spatially varying diffusivityα(x)is sampled from a Gaussian random process with RBF kernel
(length scale=1) and with variance0.01 2. The parametric functionα(x)is evaluated at 129 sensor points
corresponding to the boundaries of uniformly spaced cells,{xb i }129 i=1, and the resulting valuesα(xb i )are encoded
within the operator-valued learning and product-space learning methods.
Operator-Valued Learning.The mean relative errors and standard deviations are summarized in Table 10,
while the implementation details and hyperparameter choices are summarized in Table 23. Overall, the
proposed kernel-based methods achieve the lowest prediction errors on both the in-distribution and out-of-
distribution datasets. The best in-distribution performance is jointly attained by KernelMO-OV / M and
KernelMO-PS / M×M, while KernelMO-OV / M achieves the lowest prediction errors on the OOD_matern
and OOD_var datasets and KernelMO-OV (PCA) / M achieves the best performance on OOD_scale. Com-
pared with the best-performing neural operator baseline, the proposed methods improve the prediction accu-
racy by more than one order of magnitude on the in-distribution test set (from1.34%for MNO to0.06%for
KernelMO-OV / M and KernelMO-OV / M×M). Applying PCA substantially reduces the dimensionality of
the learning problem while preserving competitive predictive performance, particularly under distribution shifts
33

in the coefficient functions. Overall, the operator-valued formulation demonstrates stronger out-of-distribution
generalization than the product-space formulation on this benchmark.
Method / kernel Test OOD_matern OOD_scale OOD_var
KernelMO-OV / M 0.06% (0.15%) 3.53% (1.56%)4.13% (1.67%)0.12% (0.37%)
KernelMO-OV / R0.12% (0.34%) 56.22% (48.91%) 83.90% (72.76%) 0.33% (1.08%)
KernelMO-OV (PCA) / M3.04% (1.90%) 3.77% (1.67%)4.05% (1.59%)3.19% (1.92%)
KernelMO-OV (PCA) / R3.04% (1.90%) 7.25% (6.29%) 10.34% (10.19%) 3.19% (1.92%)
KernelMO-PS / M x M 0.06% (0.15%)10.12% (8.30%) 14.80% (11.56%) 0.14% (0.42%)
KernelMO-PS / R x R2.48% (1.07%) 6.48% (3.22%) 8.19% (3.63%) 2.60% (1.12%)
KernelMO-PS (PCA) / M x M3.04% (1.90%) 3.81% (1.69%) 4.12% (1.62%) 3.19% (1.92%)
KernelMO-PS (PCA) / R x R3.58% (1.82%) 4.44% (1.60%) 4.91% (1.52%) 3.73% (1.86%)
DeepONet-C 2.22% (0.88%) 4.19% (1.41%) 4.68% (1.44%) 2.34% (0.99%)
MIONet 1.88% (0.78%) 4.98% (1.69%) 5.42% (1.63%) 2.02% (0.89%)
MNO 1.34% (0.50%) 4.18% (1.62%) 4.68% (1.52%) 1.45% (0.62%)
Table 10: Operator-valued learning: performance comparison on the parametric diffusion-reaction equation. We report
mean relative errors with standard deviations in parentheses on in-distribution and out-of-distribution datasets.
Figure 16: Operator-valued learning: qualitative prediction and uncertainty comparison for the parametric diffusion-
reaction equation on the OOD_var dataset. The first row shows a reference solution and signed prediction errors for four
kernel variants; the relative error for the displayed trajectory is reported in each error-figure title. The second row shows
the final-time solution, predictive mean, and an uncertainty band of±2predictive standard deviations.
Product-Space Learning.The mean relative errors and standard deviations are summarized in Table 11,
while the implementation details and hyperparameter choices are summarized in Table 24. Overall, the pro-
posed product-kernel methods achieve prediction errors comparable to those of the best-performing neural
operator baseline across both the in-distribution and out-of-distribution datasets. In particular, KernelMO-PS /
R×R attains the lowest in-distribution test error of0.75%, compared with1.77%for MNO. However, this vari-
ant exhibits poor generalization under most distribution shifts, with substantially larger errors on the OOD_init,
OOD_par_init, OOD_par_kernel, and OOD_par_scale datasets. By contrast, KernelMO-PS / M×M achieves
consistently strong performance across all evaluation settings, obtaining prediction errors comparable to MNO
on every out-of-distribution dataset and outperforming it on the OOD_par_var dataset (1.30%versus1.73%).
These results highlight the superior robustness of the Matérn product-kernel method under distribution shifts,
even though the RBF variant achieves the lowest in-distribution error.
34

Method / kernel Test OOD_init OOD_par_init OOD_par_kernel OOD_par_scale OOD_par_var
KernelO / M 9.21% (5.27%) 12.48% (3.52%) 12.51% (3.47%) 8.20% (3.50%) 8.01% (3.47%) 8.64% (5.11%)
KernelO / R 6.76% (2.54%) 18.96% (7.00%) 19.02% (6.95%) 4.98% (1.78%) 5.18% (1.67%) 6.87% (2.64%)
KernelO (PCA) / M 8.96% (4.72%) 15.70% (5.20%) 15.74% (5.14%) 7.77% (3.12%) 7.62% (3.08%) 8.62% (4.53%)
KernelO (PCA) / R 6.97% (2.74%)10.76% (3.62%) 10.78% (3.57%) 5.11% (1.91%) 5.30% (1.83%)7.09% (2.84%)
KernelMO-PS / M x M1.50% (0.75%) 11.88% (3.53%) 12.73% (3.43%) 5.40% (1.98%) 7.35% (2.57%) 1.30% (0.70%)
KernelMO-PS / R x R 0.75% (0.44%)127.42% (47.76%) 188.16% (88.56%) 105.53% (50.74%) 157.30% (77.91%)0.76% (0.45%)
KernelMO-PS (PCA) / M x M3.94% (2.01%) 104.63% (68.48%) 150.65% (81.94%) 104.76% (68.56%) 154.17% (91.24%) 4.04% (2.04%)
KernelMO-PS (PCA) / R x R4.27% (1.96%) 156.18% (102.47%) 243.60% (144.65%) 155.33% (109.85%) 235.54% (162.35%) 4.39% (1.96%)
DeepONet 7.75% (2.76%) 11.56% (3.38%) 11.56% (3.36%) 6.27% (1.95%) 6.37% (1.85%) 7.86% (2.91%)
DeepONet-C 2.48% (0.78%) 11.03% (3.73%) 11.66% (3.67%) 5.02% (1.51%) 5.52% (1.58%) 2.52% (0.76%)
MIONet 3.49% (1.00%) 36.36% (16.85%) 37.00% (16.77%) 5.43% (1.74%) 6.60% (2.50%) 3.51% (0.95%)
MNO 1.77% (0.66%) 11.26% (3.77%) 11.43% (3.66%)4.42% (1.82%) 5.00% (1.82%)1.73% (0.61%)
Table 11: Product-space learning: performance comparison on parametric diffusion-reaction equation. We report mean
relative errors with standard deviations in parentheses on in-distribution and out-of-distribution datasets.
Figure 17: Product-space learning: qualitative prediction and uncertainty comparison for the parametric diffusion-
reaction equation on the OOD_par_var dataset. The first row shows a reference solution and signed prediction errors
for four kernel variants; the relative error for the displayed trajectory is reported in each error-figure title. The second row
shows the final-time solution, predictive mean, and an uncertainty band of±2predictive standard deviations.
Remark4.4 (Hyperparameter selection and out-of-distribution performance).The out-of-distribution perfor-
mance of the proposed kernel methods can be sensitive to the choice of kernel hyperparameters. In all ex-
periments, we select these hyperparameters using only in-distribution validation data and do not tune them
separately for the OOD test cases. Consequently, a hyperparameter choice that yields strong in-distribution
performance need not be optimal under distribution shift. Table 12 illustrates this effect for KernelMO-PS with
an RBF kernel on the parametric diffusion–reaction problem. In particular, the length scale selected based on
in-distribution performance can lead to substantially larger errors for some OOD shifts, whereas other length
scales yield considerably better OOD performance despite being less accurate in distribution.
Length-scale Test OOD_init OOD_par_init OOD_par_kernel OOD_par_scale OOD_par_var
1 5.43% (3.40%) 78.10% (23.07%) 78.11% (23.05%) 4.44% (1.88%) 4.84% (1.87%) 3.81% (2.21%)
10 0.75% (0.44%) 127.42% (47.76%) 188.16% (88.56%) 105.53% (50.74%) 157.30% (77.91%) 0.76% (0.45%)
100 1.51% (0.68%) 251.19% (158.00%) 458.95% (284.88%) 276.53% (146.44%) 408.37% (227.92%) 1.56% (0.70%)
1000 3.16% (1.21%) 516.14% (344.66%) 937.77% (641.70%) 575.36% (332.08%) 811.18% (501.40%) 3.29% (1.23%)
Table 12: Product-space learning: performance of KernelMO-PS with an RBF kernel on the parametric diffusion–reaction
equation for different length scales. The first column reports the length scale of the kernelk U acting on the initial
conditions, while the remaining columns report the corresponding in-distribution and OOD prediction errors.
35

4.1.5 Parametric Wave Equation
We consider the following parametric wave equation:
utt =α 2(t)uxx,(t, x)∈[0,2]×[0,2]
u(0, x) =u0(x),
ut(0, x) = 0,
u(t,0) =u(t,2),
where the time-dependent parametric functionα(t)is drawn from a Gaussian random process with RBF kernel
(length scale = 1) and with variance 1. The parametric functionα(t)is evaluated at 64 sensor points cor-
responding to the boundaries of spaced cells,{t b i }64 i=1, and the resulting valuesα(t b i )are encoded within the
operator-valued learning and product-space learning methods.
Operator-Valued Learning.The mean relative errors and standard deviations are summarized in Table 13,
while the implementation details and hyperparameter choices are summarized in Table 25. Overall, the pro-
posed kernel-based methods achieve the lowest prediction errors on the in-distribution test set, with the best
performance obtained by KernelMO-OV (PCA) / R. Compared with the best-performing neural operator base-
line, the proposed method improves the prediction accuracy by more than one order of magnitude on the in-
distribution test set (from17.83%for DeepONet-C to1.59%for KernelMO-OV (PCA) / R). On the OOD_var
dataset, the proposed methods also substantially outperform all neural operator baselines, achieving the low-
est prediction error of1.29%compared with17.11%for DeepONet-C. By contrast, all methods experience
a significant degradation in performance on the OOD_matern and OOD_scale datasets, indicating that these
distribution shifts are particularly challenging for this PDE. This behavior differs from that observed for the
parametric diffusion–reaction equation (Table 10), demonstrating that out-of-distribution generalization de-
pends strongly on the underlying PDE. Applying PCA substantially reduces the dimensionality of the learning
problem while consistently improving the out-of-distribution performance of the proposed kernel-based meth-
ods.
Method / kernel Test OOD_matern OOD_scale OOD_var
KernelMO-OV / M2.63% (5.86%) 56.69% (17.61%) 71.93% (13.38%) 2.05% (3.22%)
KernelMO-OV / R9.37% (25.42%) 209.27% (247.77%) 117.14% (69.91%) 6.65% (10.34%)
KernelMO-OV (PCA) / M2.50% (4.42%) 32.90% (16.17%) 43.27% (20.56%) 1.98% (2.33%)
KernelMO-OV (PCA) / R 1.59% (2.34%)31.57% (15.71%) 43.60% (20.86%)1.29% (1.04%)
KernelMO-PS / M x M2.63% (5.86%) 56.69% (17.61%) 71.93% (13.38%) 2.05% (3.22%)
KernelMO-PS / R x R2.37% (5.13%) 66.05% (17.44%) 79.51% (13.45%) 1.68% (2.29%)
KernelMO-PS (PCA) / M x M2.50% (4.42%) 32.27% (16.31%) 42.40% (21.19%) 1.98% (2.33%)
KernelMO-PS (PCA) / R x R1.64% (2.46%)30.42% (15.96%)42.36% (21.68%) 1.31% (1.05%)
DeepONet-C 17.83% (7.29%) 35.91% (17.51%)41.90% (23.91%)17.11% (5.98%)
MIONet 19.08% (8.44%) 67.88% (20.60%) 70.41% (20.11%) 18.13% (6.75%)
MNO 19.46% (8.38%) 40.09% (19.75%) 46.28% (24.27%) 18.60% (7.19%)
Table 13: Operator-valued learning: performance comparison on the parametric wave equation. We report mean relative
errors with standard deviations in parentheses on in-distribution and out-of-distribution datasets.
36

Figure 18: Operator-valued learning: qualitative prediction and uncertainty comparison for the parametric wave equation
on the OOD_var dataset. The first row shows a reference solution and signed prediction errors for four kernel variants;
the relative error for the displayed trajectory is reported in each error-figure title. The second row shows the final-time
solution, predictive mean, and an uncertainty band of±2predictive standard deviations.
Product-Space Learning.The mean relative errors and standard deviations are summarized in Table 14,
while the implementation details and hyperparameter choices are summarized in Table 26. Overall, the pro-
posed PCA-based product-kernel methods achieve the lowest prediction errors across both the in-distribution
and out-of-distribution datasets. In particular, KernelMO-PS (PCA) / R×R attains the lowest in-distribution
test error of2.13%, compared with18.20%for the best-performing neural operator baseline DeepONet-C,
corresponding to an improvement of nearly one order of magnitude. Moreover, KernelMO-PS (PCA) / R×R
achieves the best performance on four of the five out-of-distribution datasets, while KernelMO-PS (PCA) / M
×M performs best on the remaining one. By contrast, although the original product-kernel methods achieve
competitive in-distribution prediction errors, their performance deteriorates substantially under several distri-
bution shifts, particularly on the OOD_par_init, OOD_par_kernel, and OOD_par_scale datasets. These results
demonstrate that combining the product-kernel formulation with PCA substantially improves the robustness
and out-of-distribution generalization of the proposed approach.
Method / kernel Test OOD_init OOD_par_init OOD_par_kernel OOD_par_scale OOD_par_var
KernelO / M 83.16% (40.26%) 80.02% (26.03%) 84.30% (28.92%) 74.34% (38.37%) 72.95% (37.89%) 75.26% (39.70%)
KernelO / R 59.29% (21.32%) 13473.96% (6245.11%) 15134.50% (6361.41%) 50.63% (19.00%) 52.13% (20.95%) 55.35% (20.30%)
KernelO (PCA) / M 83.14% (40.25%) 124.30% (39.58%) 135.55% (41.91%) 74.32% (38.36%) 72.93% (37.89%) 75.24% (39.69%)
KernelO (PCA) / R 59.28% (21.32%) 1415.03% (1126.69%) 1585.64% (1200.96%) 50.62% (19.00%) 52.13% (20.95%) 55.35% (20.30%)
KernelMO-PS / M x M3.33% (6.75%) 38.15% (22.19%) 97.65% (0.34%) 60.48% (17.09%) 76.32% (11.83%) 2.67% (4.98%)
KernelMO-PS / R x R3.52% (6.25%) 37.89% (22.21%) 99.55% (0.21%) 68.31% (19.36%) 83.82% (12.27%) 2.88% (5.35%)
KernelMO-PS (PCA) / M x M2.84% (4.51%) 37.72% (22.24%) 46.29% (5.58%) 32.06% (17.45%)41.43% (19.02%)2.37% (3.53%)
KernelMO-PS (PCA) / R x R 2.13% (3.38%) 37.47% (22.24%) 46.20% (5.55%) 31.46% (17.10%)41.73% (18.62%)1.69% (2.00%)
DeepONet 56.93% (21.72%) 54.88% (19.86%) 55.52% (14.22%) 48.72% (19.18%) 50.37% (20.99%) 53.70% (21.09%)
DeepONet-C 18.20% (7.00%) 42.10% (20.72%) 108.17% (14.57%) 35.87% (17.08%) 42.41% (19.92%) 17.43% (6.70%)
MIONet 20.54% (10.85%) 45.40% (20.06%) 170.46% (16.33%) 97.25% (28.43%) 110.74% (28.18%) 19.07% (10.51%)
MNO 25.04% (11.75%) 43.36% (20.27%) 73.84% (19.56%) 46.96% (27.01%) 53.72% (28.81%) 22.58% (10.79%)
Table 14: Product-space learning: performance comparison on the parametric wave equation. We report mean relative
errors with standard deviations in parentheses on in-distribution and out-of-distribution datasets.
37

Figure 19: Product-space learning: qualitative prediction and uncertainty comparison for the parametric wave equation on
the OOD_par_var dataset. The first row shows a reference solution and signed prediction errors for four kernel variants;
the relative error for the displayed trajectory is reported in each error-figure title. The second row shows the final-time
solution, predictive mean, and an uncertainty band of±2predictive standard deviations.
4.2 Efficiency
In this section, we compare the computational efficiency of the proposed kernel-based methods with the neural
network-based baselines in terms of training time and prediction time. For brevity, we report the results for the
conservation law problem only, as similar trends are observed across the other PDE models.
Table 15 summarizes the computational cost of the operator-valued learning problem shown in Fig. 4b.
Although both KernelMO-OV and KernelMO-PS rely on kernel regression, KernelMO-OV is substantially
more efficient during training. As explained in Section 3.4 (see also Table 1), the reason is that its kernel
matrix has dimensionsn α ×n α and therefore contains320 2 = 102400entries, whereas the kernel matrix of
KernelMO-PS has dimensions(n αnu)×(n αnu)and contains320 2202 = 40960000entries. Thus, without
PCA, KernelMO-OV trains approximately13–14×faster than KernelMO-PS. For the PCA-based variants, the
corresponding speedup is approximately48–55×.
Compared with the neural operator baselines, the kernel methods are also considerably more efficient. The
fastest KernelMO-OV variants require less than0.5seconds for training, compared with158–250seconds for
the neural operators, corresponding to speedups of more than two orders of magnitude. At inference time,
KernelMO-OV also provides the fastest predictions, requiring approximately0.04ms per sample. This corre-
sponds to prediction times that are approximately4–9×faster than the neural operator baselines. With PCA,
the prediction time is further reduced to approximately0.004ms per sample, yielding speedups of roughly
40–80×over the neural operators. Although KernelMO-PS is slower due to its larger kernel matrix, it remains
competitive with the neural operator baselines while providing comparable or better predictive accuracy.
Applying PCA yields an additional reduction in computational cost. For KernelMO-OV, PCA decreases
the training time from approximately0.47s to0.036s and reduces the prediction time by almost an order
of magnitude. Similar improvements are observed for KernelMO-PS. These computational savings are ob-
tained with only a modest reduction in predictive accuracy, indicating that PCA provides an attractive trade-off
between computational efficiency and accuracy.
38

Method / kernel Train time (s) Test pred. (ms/sample)
KernelMO-OV / M 0.472 0.0375
KernelMO-OV / R 0.464 0.0377
KernelMO-OV(PCA) / M 0.0357 0.00407
KernelMO-OV (PCA) / R 0.0361 0.00412
KernelMO-PS / M x M 6.56 0.538
KernelMO-PS / R x R 6.24 0.497
KernelMO-PS (PCA) / M x M 1.96 0.24
KernelMO-PS (PCA) / R x R 1.72 0.19
DeepONet-C 250.44 0.334
MIONet 157.95 0.17
MNO 180.54 0.16
Table 15: Operator-valued learning: Training time and prediction time per evaluated sample.
These observations are also illustrated in Fig. 20, which jointly displays predictive accuracy and computa-
tional cost. The figure highlights that KernelMO-OV consistently combines the lowest prediction errors with
the shortest training and inference times among all methods considered. While the PCA variants incur a modest
increase in prediction error, they achieve substantial additional reductions in computational cost. In contrast,
the neural operator baselines require significantly longer training times while providing lower predictive accu-
racy, whereas KernelMO-PS offers a competitive compromise between computational efficiency and predictive
performance despite its larger kernel matrix.
10−1 100 101 1020
2
4
MR
M
R
M×M
R×R
M×M
R×R
Training time (s)
Mean relative error (%)
(a) Training time.
10−2 10−1 1000
2
4
MR
M
R
M×M
R×R
M×M
R×R
Inference time (ms/sample)
Mean relative error (%)
(b) Inference time.
KernelMO-OV KernelMO-OV (PCA) KernelMO-PS KernelMO-PS (PCA)
DeepONet-C MIONet MNO
Figure 20: Operator-valued learning: trade-off between predictive accuracy and computational cost on the conservation-
law benchmark. Labels beside kernel points indicate the kernel choice: M denotes Matérn and R denotes RBF.
Table 16 summarizes the computational cost of the product-space learning formulation shown in Fig. 4c.
As in the operator-valued setting, the proposed kernel-based methods are substantially more computationally
efficient than the neural operator baselines. The full-dimensional kernel methods require only15–16seconds
for training, compared with227–397seconds for the neural operators, corresponding to speedups of approx-
imately15–25×. Applying PCA further reduces the training time to approximately4–5seconds, yielding an
additional factor of about three. At inference time, the prediction cost of the kernel methods is comparable to
that of the neural operator baselines. The full-dimensional methods require approximately0.8ms per sample,
while the PCA variants reduce this to approximately0.35–0.42ms per sample, which is comparable to MIONet
and MNO and substantially faster than DeepONet-C. The proposed kernel methods are particularly attractive
in applications where both training and inference efficiency are important, such as settings requiring frequent
retraining or repeated deployment on new operator families.
One observation is that KernelMO-PS and the corresponding single-operator baseline KernelO exhibit
nearly identical training and prediction times, both with and without PCA. This is expected, since both meth-
ods solve kernel regression problems of the same size and therefore have essentially identical computational
complexity. However, as demonstrated throughout the experimental Section 4.1, KernelMO-PS consistently
39

achieves substantially higher predictive accuracy than KernelO across all benchmarks. These results demon-
strate that the proposed product-kernel framework provides a favorable trade-off between computational effi-
ciency and predictive performance, improving accuracy in multiple operator learning without increasing com-
putational cost.
Method / kernel Train time (s) Test pred. (ms/sample)
KernelMO-PS (PCA) / M x M 5.19 0.415
KernelMO-PS (PCA) / R x R 4.7 0.365
KernelMO-PS / M x M 15.5 0.874
KernelMO-PS / R x R 14.8 0.829
KernelO (PCA) / M 4.06 0.339
KernelO (PCA) / R 3.9 0.323
KernelO / M 14 0.815
KernelO / R 14 0.778
DeepONet 226.79 0.23
DeepONet-C 397.46 0.83
MIONet 245.41 0.41
MNO 277.59 0.38
Table 16: Product-space learning: Training time and prediction time per evaluated sample.
These observations are further illustrated in Fig. 21, which jointly displays predictive accuracy and com-
putational cost. The figure shows that the proposed product-kernel methods consistently achieve a favorable
balance between accuracy and efficiency. In particular, KernelMO-PS occupies a similar computational regime
to the corresponding single-operator baseline KernelO while consistently attaining substantially lower predic-
tion errors. The PCA variants further reduce both training and inference times while maintaining competitive
predictive performance. Overall, the figure highlights that the proposed multiple-operator kernel construc-
tion improves predictive accuracy without increasing computational cost, while remaining significantly more
efficient to train than the neural operator baselines.
101 1020
2
4
6
8
M×M
R×RM×M
R×R
M
R
M
R
Training time (s)
Mean relative error (%)
(a) Training time.
10−0.6 10−0.4 10−0.2 1000
2
4
6
8
M×M
R×RM×M
R×R
M
R
M
R
Inference time (ms/sample)
Mean relative error (%)
(b) Inference time.
KernelMO-PS KernelMO-PS (PCA) KernelO KernelO (PCA)
DeepONet DeepONet-C MIONet MNO
Figure 21: Product-space learning: trade-off between predictive accuracy and computational cost on the conservation-law
benchmark. Labels beside kernel points indicate the kernel choice: M denotes Matérn and R denotes RBF.
5 Conclusion
We have introduced a general kernel-based framework for learning maps between Hilbert spaces within an
encoder–decoder architecture. By showing that kernels defined on the latent surrogate space induce corre-
sponding kernels on the original input and output spaces, we established a rigorous theoretical connection
between latent-space learning and learning in the original function spaces. This perspective leads to an en-
coder–decoder error decomposition and a general approximation theory for learning maps between products
40

of function spaces, yielding approximation guarantees that scale favorably with the numbers of input and out-
put tasks. As an application of the proposed framework, we developed two kernel formulations for multiple
operator learning. The resulting methods inherit the theoretical guarantees of the general framework while
exhibiting complementary computational characteristics. Our numerical experiments demonstrate that these
approaches achieve competitive predictive performance while substantially reducing training and inference
times compared with state-of-the-art neural operator architectures.
More broadly, this work suggests that kernel methods constitute a viable alternative to deep neural surro-
gates for scientific machine learning. Importantly, the kernel learning approaches presented in this work have
mathematical guarantees, are computational efficiency, and leverage limited data sampling. At the same time,
the proposed encoder-decoder framework is not restricted to multiple operator learning and provides a unified
perspective for kernel-based learning of general maps between function spaces.
Several directions for future work naturally arise. From a theoretical perspective, it would be of consider-
able interest to develop an approximation theory for learning maps whose inputs and outputs are themselves
spaces of operators, rather than function spaces, and to establish corresponding guarantees when the encoders
and decoders are learned from data. Another important direction is to extend the framework to settings in
which the observation spaces are themselves infinite-dimensional, requiring both new theoretical foundations
and practical learning algorithms. From a practical perspective, replacing the prescribed encoders and de-
coders by adaptive learned representations is a natural extension of the present framework. Another promising
direction is to investigate the transferability of learned surrogates across different observation operators and
to leverage the close connection between kernel methods and Gaussian processes for principled uncertainty
quantification.
Acknowledgments
This work was supported by NSF 2514157. The authors would like to thank Bamdad Hosseini for helpful
discussions.
References
[1] R.A. Adams and J.J.F. Fournier.Sobolev Spaces. Pure and Applied Mathematics. Academic Press, 2003.
[2] Mauricio A. Álvarez, Lorenzo Rosasco, and Neil D. Lawrence. Kernels for vector-valued functions: A
review.Foundations and Trends in Machine Learning, 4(3):195–266, March 2012.
[3] Rémi Arcangéli, María Cruz López de Silanes, and Juan José Torrens. An extension of a bound for
functions in sobolev spaces, with applications to (m, s)-spline interpolation and smoothing.Numerische
Mathematik, 107(2):181–211, 2007.
[4] Rémi Arcangéli, María Cruz López de Silanes, and Juan José Torrens. Extension of sampling inequalities
to sobolev semi-norms of fractional order and derivative data.Numerische Mathematik, 121(3):587–608,
2012.
[5] Nachman Aronszajn. Theory of reproducing kernels.Transactions of the American Mathematical Society,
68:337–404, 1950.
[6] Vladyslav Babenko, Vira Babenko, and Oleg Kovalenko. Korneichuk-stechkin lemma, ostrowski and
landau inequalities, and optimal recovery problems for l-space valued functions.Numerical Functional
Analysis and Optimization, 44(12):1309–1341, 2023.
[7] Aras Bacho, Aleksei G. Sorokin, Xianjin Yang, Théo Bourdais, Edoardo Calvello, Matthieu Darcy,
Alexander Hsu, Bamdad Hosseini, and Houman Owhadi. Operator learning at machine precision, 2025.
[8] Pau Batlle, Yifan Chen, Bamdad Hosseini, Houman Owhadi, and Andrew M. Stuart. Error analysis of
kernel/GP methods for nonlinear and parametric pdes.Journal of Computational Physics, 520:113488,
2025.
41

[9] Pau Batlle, Matthieu Darcy, Bamdad Hosseini, and Houman Owhadi. Kernel methods are competitive
for operator learning.Journal of Computational Physics, 496:112549, 2024.
[10] H. Brezis.Functional Analysis, Sobolev Spaces and Partial Differential Equations. Universitext. Springer
New York, 2010.
[11] Yadi Cao, Yuxuan Liu, Liu Yang, Rose Yu, Hayden Schaeffer, and Stanley Osher. Vicon: Vision in-
context operator networks for multi-physics fluid dynamics prediction.arXiv preprint arXiv:2411.16063,
2024.
[12] C. Carmeli, E. De Vito, A. Toido, and V . Umanità. Vector valued reproducing kernel hilbert spaces and
universality.Analysis and Applications, 08(01):19–61, 2010.
[13] Yifan Chen, Bamdad Hosseini, Houman Owhadi, and Andrew M. Stuart. Solving and learning nonlinear
pdes with gaussian processes.Journal of Computational Physics, 447:110668, 2021.
[14] John B. Conway.A Course in Functional Analysis, volume 96 ofGraduate Texts in Mathematics.
Springer, New York, NY , 2 edition, 2007.
[15] Brian Davies.Integral Transforms and Their Applications. Springer, New York, 3 edition, 2002.
[16] Dean G. Duffy.Green’s Functions with Applications. CRC Press, Boca Raton, FL, 2 edition, 2015.
[17] Lawrence C. Evans.Partial Differential Equations, volume 19 ofGraduate Studies in Mathematics.
American Mathematical Society, Providence, RI, 2 edition, 2010.
[18] Simon Foucart.Mathematical Pictures at a Data Science Exhibition. Cambridge University Press, 2022.
[19] Quoc Thong Le Gia, Ian Hugh Sloan, and Holger Wendland. Vector-valued gaussian processes for ap-
proximating divergence- or rotation-free vector fields.Journal of Machine Learning Research, 27(74):1–
36, 2026.
[20] John Harlim, Daniel Sanz-Alonso, and Ruiyi Yang. Kernel methods for bayesian elliptic inverse problems
on manifolds.SIAM/ASA Journal on Uncertainty Quantification, 8(4):1414–1445, 2020.
[21] Maximilian Herde, Bogdan Raonic, Tobias Rohner, Roger Käppeli, Roberto Molinaro, Emmanuel
de Bezenac, and Siddhartha Mishra. Poseidon: Efficient foundation models for PDEs. InThe Thirty-
eighth Annual Conference on Neural Information Processing Systems, 2024.
[22] Boya Hou, Sina Sanjari, Nathan Dahlin, Subhonmesh Bose, and Umesh Vaidya. Sparse learning of
dynamical systems in RKHS: An operator-theoretic approach. InProceedings of the 40th International
Conference on Machine Learning, volume 202 ofProceedings of Machine Learning Research, pages
13325–13352. PMLR, 23–29 Jul 2023.
[23] Yasamin Jalalian, Juan Felipe Osorio Ramirez, Alexander Hsu, Bamdad Hosseini, and Houman Owhadi.
Data-efficient kernel methods for learning differential equations and their solution operators: Algorithms
and error analysis, 2025.
[24] Jikai Jin, Yiping Lu, Jose Blanchet, and Lexing Ying. Minimax optimal kernel operator learning via
multilevel training. InThe Eleventh International Conference on Learning Representations, 2023.
[25] Pengzhan Jin, Shuai Meng, and Lu Lu. Mionet: Learning multiple-input operators via tensor product.
SIAM Journal on Scientific Computing, 44(6):A3490–A3514, 2022.
[26] Derek Jollie, Jingmin Sun, Zecheng Zhang, and Hayden Schaeffer. Time-series forecasting and refine-
ment within a multimodal pde foundation model.Journal of Machine Learning for Modeling and Com-
puting, 6(2):77–89, 2025.
[27] Hachem Kadri, Emmanuel Duflos, Philippe Preux, Stéphane Canu, Alain Rakotomamonjy, and Julien
Audiffren. Operator-valued kernels for learning from functional response data.Journal of Machine
Learning Research, 17(20):1–54, 2016.
42

[28] Rüdiger Kempf. Kernel-based operator learning: Error analysis, budget allocation, and a physics-
informed extension, 2026.
[29] Samuel Lanthaler. Operator learning with pca-net: upper and lower complexity bounds.J. Mach. Learn.
Res., 24(1), January 2023.
[30] Zongyi Li, Nikola Kovachki, Kamyar Azizzadenesheli, Burigede Liu, Kaushik Bhattacharya, Andrew
Stuart, and Anima Anandkumar. Fourier neural operator for parametric partial differential equations. In
International Conference on Learning Representations (ICLR), 2021. preprint arXiv:2010.08895.
[31] Chunyang Liao, Deanna Needell, and Hayden Schaeffer. Cauchy random features for operator learning
in sobolev space.arXiv: 2503.00300, 2025.
[32] Yuxuan Liu, Jingmin Sun, Xinjie He, Griffin Pinney, Zecheng Zhang, and Hayden Schaeffer. Prose-fd: A
multimodal pde foundation model for learning multiple operators for forecasting fluid dynamics.arXiv
preprint arXiv:2409.09811, 2024.
[33] Yuxuan Liu, Jingmin Sun, and Hayden Schaeffer. Bcat: A block causal transformer for pde foundation
models for fluid dynamics.arXiv preprint arXiv:2501.18972, 2025.
[34] Yuxuan Liu, Zecheng Zhang, and Hayden Schaeffer. Prose: Predicting multiple operators and symbolic
expressions using multimodal transformers.Neural Networks, 180:106707, 2024.
[35] Lu Lu, Pengzhan Jin, Guofei Pang, Zhongqiang Zhang, and George Em Karniadakis. Learning nonlinear
operators via deeponet based on the universal approximation theorem of operators.Nature Machine
Intelligence, 3(3):218–229, 2021.
[36] G G Magaril-Il’yaev and K Yu Osipenko. Optimal recovery of functions and their derivatives from Fourier
coefficients prescribed with an error.Sbornik. Mathematics, 193(3), January 2025.
[37] Michael McCabe, Bruno Régaldo-Saint Blancard, Liam Holden Parker, Ruben Ohana, Miles Cranmer,
Alberto Bietti, Michael Eickenberg, Siavash Golkar, Géraud Krawezik, Francois Lanusse, et al. Multiple
physics pretraining for physical surrogate models.arXiv preprint arXiv:2310.02994, 2023.
[38] Carlos Mora, Amin Yousefpour, Shirin Hosseinmardi, Houman Owhadi, and Ramin Bostanabad. Op-
erator learning with gaussian processes.Computer Methods in Applied Mechanics and Engineering,
434:117581, 2025.
[39] Elisa Negrini, Yuxuan Liu, Liu Yang, Stanley J Osher, and Hayden Schaeffer. A multimodal pde founda-
tion model for prediction and scientific text descriptions.arXiv preprint arXiv:2502.06026, 2025.
[40] Nicholas H. Nelsen and Andrew M. Stuart. Operator learning using random features: A tool for scientific
computing.SIAM Review, 66(3):535–571, 2024.
[41] K Yu Osipenko. On optimal recovery methods in hardy-sobolev spaces.Sbornik: Mathematics,
192(2):225, feb 2001.
[42] Houman Owhadi. Do ideas have shape? idea registration as the continuous limit of artificial neural
networks.Physica D: Nonlinear Phenomena, 444:133592, 2023.
[43] Houman Owhadi and Clint Scovel.Operator-Adapted Wavelets, Fast Solvers, and Numerical Homoge-
nization: From a Game Theoretic Approach to Numerical Approximation and Algorithm Design. Cam-
bridge Monographs on Applied and Computational Mathematics. Cambridge University Press, 2019.
[44] R. Robey and J. K. Lundquist. Behavior and mechanisms of doppler wind lidar error in varying stability
regimes.Atmospheric Measurement Techniques, 15(15):4585–4622, 2022.
[45] Andrew M. Stuart. Inverse problems: A bayesian perspective.Acta Numerica, 19:451–559, 2010.
43

[46] Jingmin Sun, Yuxuan Liu, Zecheng Zhang, and Hayden Schaeffer. Towards a foundation model for partial
differential equations: Multioperator learning and extrapolation.Physical Review E, 111(3):035304,
2025.
[47] Jingmin Sun, Zecheng Zhang, and Hayden Schaeffer. Lemon: Learning to learn multi-operator networks.
arXiv preprint arXiv:2408.16168, 2024.
[48] Makoto Takamoto, Timothy Praditia, Raphael Leiteritz, Dan MacKinlay, Francesco Alesiani, Dirk
Pflüger, and Mathias Niepert. Pdebench: an extensive benchmark for scientific machine learning. In
Proceedings of the 36th International Conference on Neural Information Processing Systems, NIPS ’22,
Red Hook, NY , USA, 2022. Curran Associates Inc. doi: 10.5555/3600270.3600387.
[49] Peter Jan van Leeuwen. Non-local observations and information transfer in data assimilation.Frontiers
in Applied Mathematics and Statistics, V olume 5 - 2019, 2019.
[50] Zhuoyuan Wang, Hanjiang Hu, Xiyu Deng, Saviz Mowlavi, and Yorie Nakahira. Opinf-llm: Parametric
pde solving with llms via operator inference, 2026.
[51] Adrien Weihs and Hayden Schaeffer. Generalization bounds and statistical guarantees for multi-task and
multiple operator learning with mno networks, 2026.
[52] Adrien Weihs and Hayden Schaeffer. Multiple neural operators achieve near-optimal rates for multi-task
learning, 2026.
[53] Adrien Weihs, Jingmin Sun, Zecheng Zhang, and Hayden Schaeffer. A deep learning framework for
multi-operator learning: Architectures and approximation theory, 2025. arXiv:2510.25379.
[54] Holger Wendland.Scattered Data Approximation. Cambridge Monographs on Applied and Computa-
tional Mathematics. Cambridge University Press, 2004.
[55] Liu Yang, Siting Liu, Tingwei Meng, and Stanley J Osher. In-context operator learning with
data prompts for differential equation problems.Proceedings of the National Academy of Sciences,
120(39):e2310142120, 2023.
[56] Liu Yang, Tingwei Meng, Siting Liu, and Stanley J Osher. Prompting in-context operator learning with
sensor data, equations, and natural language.arXiv preprint arXiv:2308.05061, 2023.
[57] Yahong Yang, Zecheng Zhang, Wei Zhu, Wenjing Liao, and Hao Liu. Generalization guarantees for
multi-input neural operator learning in sobolev spaces, 2026.
[58] Zhanhong Ye, Zining Liu, Bingyang Wu, Hongjie Jiang, Leheng Chen, Minyan Zhang, Xiang Huang,
Qinghe Meng Zou, Hongsheng Liu, and Bin Dong. Pdeformer-2: A versatile foundation model for two-
dimensional partial differential equations.arXiv preprint arXiv:2507.15409, 2025.
[59] Xinyue Yu and Hayden Schaeffer. Regularized random fourier features and finite element reconstruction
for operator learning in sobolev space.Journal of Machine Learning for Modeling and Computing,
7(3):1–47, 2026.
[60] Benjamin J Zhang, Siting Liu, Stanley J Osher, and Markos A Katsoulakis. Probabilistic operator learn-
ing: generative modeling and uncertainty quantification for foundation models of differential equations.
arXiv preprint arXiv:2509.05186, 2025.
[61] Zecheng Zhang. Modno: Multi-operator learning with distributed neural operators.Computer Methods
in Applied Mechanics and Engineering, 431:117229, 2024.
[62] Zecheng Zhang, Wing Tat Leung, and Hayden Schaeffer. A discretization-invariant extension and analysis
of some deep operator networks.Journal of Computational and Applied Mathematics, 456:116226, 2025.
44

[63] Zecheng Zhang, Christian Moya, Lu Lu, Guang Lin, and Hayden Schaeffer. D2no: Efficient handling
of heterogeneous input function spaces with distributed deep neural operators.Computer Methods in
Applied Mechanics and Engineering, 428:117084, 2024.
[64] Zecheng Zhang, Christian Moya, Lu Lu, Guang Lin, and Hayden Schaeffer. Deeponet as a multi-operator
extrapolation model: Distributed pretraining with physics-informed fine-tuning.Journal of Computa-
tional Physics, page 114537, 2025.
[65] Zecheng Zhang, Leung Wing Tat, and Hayden Schaeffer. Belnet: basis enhanced learning, a mesh-free
neural operator.Proceedings of the Royal Society A: Mathematical, Physical and Engineering Sciences,
479(2276):20230043, 2023.
[66] Min Zhu, Jingmin Sun, Zecheng Zhang, Hayden Schaeffer, and Lu Lu. Pi-mfm: Physics-informed mul-
timodal foundation model for solving partial differential equations.arXiv preprint arXiv:2512.23056,
2025.
45

A Proofs
A.1 Proofs of the Background Section
Proof of Theorem 2.1.We first note thatL ∗ exists becauseL:X→Zis a bounded linear operator between
Hilbert spaces [14, Theorem 2.2].
1. SinceLis surjective, the affine constraint setA S :={x∈X:Lx=S}is nonempty. Ifx 0 ∈ AS, then
(7)A S =x 0 + kerL.
Ifh∈kerL, thenL(x 0 +h) =S, and conversely, ifx∈ A S, thenL(x−x 0) = 0, sox−x 0 ∈kerL.
Letx∈ AS and decompose it as
x=x ⊥ +x ker, x ⊥ ∈(kerL) ⊥, x ker ∈kerL.
Then,Lx ⊥ =Lx=S, sox ⊥ ∈ AS, and, by (7), every other feasible point has the formx ⊥ +hwith
h∈kerL. Sincex ⊥ ⊥h,∥x ⊥ +h∥ 2 X =∥x ⊥∥2 X +∥h∥ 2 X .Thus, the minimum-norm element ofA S, is
uniquely defined by havingh= 0i.e. x(S)is orthogonal tokerL.
SinceLis surjective, the restricted operator
eL: (kerL) ⊥ →Z, eLx:=Lx,
is a bounded linear bijection. It is injective because ifx∈(kerL) ⊥ and eLx= 0, thenx∈kerL∩
(kerL) ⊥ ={0}. It is surjective because, for anyz∈Z, surjectivity ofLgives somex∈Xwith
Lx=z. If
x=x ⊥ +x ker, x ⊥ ∈(kerL) ⊥, x ker ∈kerL,
thenLx ⊥ =Lx=z.Thus eLis bijective.
By the bounded inverse theorem [10, Corollary 2.7], we deduce that eL−1 :Z→(kerL) ⊥ is bounded.
Hence there exists a constantC >0such that, for everyz∈Z, there existsx z ∈(kerL) ⊥ satisfying
Lxz =z,∥x z∥X ≤C∥z∥ Z.
Using thisx z, we obtain
∥z∥2 Z =⟨z, Lxz⟩Z =⟨L ∗z, xz⟩X ≤ ∥L∗z∥X ∥xz∥X ≤C∥L ∗z∥X ∥z∥Z.
Therefore, forz∈Z,∥L ∗z∥X ≥C −1∥z∥Z,and it follows that
⟨LL∗z, z⟩Z =⟨L ∗z, L∗z⟩X =∥L ∗z∥2 X ≥C −2∥z∥2 Z.
Thus, the bilinear form
a:Z×Z7→Rgiven bya(z, w) :=⟨LL ∗z, w⟩Z
is coercive and bounded, since|a(z, w)|=|⟨L ∗z, L∗w⟩X | ≤ ∥L∗∥2 op∥z∥Z∥w∥Z =∥L∥ 2 op∥z∥Z∥w∥Z.
We apply the Lax–Milgram theorem [10, Corollary 5.8] and obtain that for anyF∈Z ∗, there exists a
unique elementz∈Zsuch thata(z, w) =F(w)for allw∈Z. By pickingF z(w) =⟨ z, w⟩Z, this
implies that
a(z, w) =⟨LL∗z, w⟩Z =⟨ z, w⟩Z
for allw∈Z, or equivalentlyLL ∗z= z. This shows thatLL ∗ :Z→Zis a linear bijection and,
by [10, Corollary 2.7], therefore boundedly invertible.
Finally, we set x(S) =L ∗(LL∗)−1S.Then,L x(S) =LL ∗(LL∗)−1S=S,so x(S)∈ AS. Moreover,
x(S)∈ran(L ∗), andran(L ∗)⊆(kerL) ⊥, because forh∈kerLandz∈Z,
⟨L∗z, h⟩X =⟨z, Lh⟩Z = 0.
This implies that x(S)is feasible and orthogonal tokerL, and therefore it is the unique minimum-norm
solution.
46

2. We start by proving
(8) xγ(S) = (L∗L+γI X )−1L∗S.
Define the functional
Jγ :X→R, J γ(x) :=∥x∥ 2 X +γ −1∥Lx−S∥ 2 Z.
The functionalJ γ is strictly convex, sincex7→ ∥x∥ 2 X is strictly convex. HenceJ γ has at most one
minimizer.
We compute the first-order optimality condition. Leth∈X. Forε∈R,
Jγ(x+εh) =∥x+εh∥ 2 X +γ −1∥Lx+εLh−S∥ 2 Z.
Differentiating atε= 0gives
d
dε Jγ(x+εh)

ε=0
= 2⟨x, h⟩X + 2γ−1⟨Lx−S, Lh⟩Z.
Using the definition of the adjoint,⟨Lx−S, Lh⟩ Z =⟨L ∗(Lx−S), h⟩X and therefore the first variation
is2

x+γ −1L∗(Lx−S), h  X .The minimizer hence satisfiesx+γ −1L∗(Lx−S) = 0or equivalently,
(L∗L+γI X )x=L ∗S.
We now show thatL ∗L+γI X is boundedly invertible. Forx∈X, we have
⟨(L∗L+γI X )x, x⟩X =⟨Lx, Lx⟩Z +γ∥x∥ 2 X =∥Lx∥ 2 Z +γ∥x∥ 2 X ≥γ∥x∥ 2 X ,
and hence the bilinear form
a:X×X7→Rgiven bya X (x, h) :=⟨(L∗L+γI X )x, h⟩X
is coercive. It is also bounded, since|aX (x, h)| ≤(∥L∥2 op+γ)∥x∥ X ∥h∥X .By the Lax-Milgram theorem
[10, Corollary 5.8] and the same argument as part 1 of the proof,L ∗L+γI X :X→Xis boundedly
invertible and (8) therefore has the unique solution
xγ(S) = (L∗L+γI X )−1L∗S.
It remains to show the equivalent measurement-space formula (3). First observe thatLL∗+γI Z :Z→Z
is also boundedly invertible. Forz∈Z,
⟨(LL∗ +γI Z)z, z⟩Z =⟨L ∗z, L∗z⟩X +γ∥z∥ 2 Z =∥L ∗z∥2 X +γ∥z∥ 2 Z ≥γ∥z∥ 2 Z.
ThusLL ∗ +γI Z is coercive and bounded, and hence boundedly invertible. Next, setx S :=L ∗(LL∗ +
γIZ)−1S.andc:= (LL ∗ +γI Z)−1S.Then,(LL ∗ +γI Z)c=Sand therefore,L ∗LL∗c+γL ∗c=L ∗S.
Sincex S =L ∗c, this becomes(L ∗L+γI X )xS =L ∗Sand thusx S solves the normal equation (8). By
uniqueness of the solution, we conclude that
xγ(S) =x S =L ∗(LL∗ +γI Z)−1S.
47

A.2 Proofs of the Main Results
A.2.1 Proofs for the General Learning Framework
Proof of Theorem 3.3.We prove the result by applying two standard operations for operator-valued reproduc-
ing kernels: first a pullback in the input variable, and then a pushforward in the output variable.
We start with the pullback construction. The pullback theorem [12, Proposition 7] withΨ =E X :X7→
ZX gives the kernel
ΓEX :X×X→ L(Z Y ),Γ EX (x, x′) := Γ(EX x, EX x′)
with associated RKHS
(9)H ΓEX ={f◦E X :f∈ HΓ}
and minimal-representative norm
(10)∥F 0∥HΓEX = inf{∥f∥ HΓ :F 0 =f◦E X }.
We note that we only use the Hilbert-space part of the pullback theorem. The locally compact, second countable
assumptions appearing in some formulations of this result are needed for additional topological conclusions
[12, Page 4].
We next apply the output transformation. SinceD Y :Z Y →Yis bounded and linear, the output pushfor-
ward theorem [12, Proposition 7] applied toΓ EX withw=D Y implies that
K:X×X→ L(Y), K(x, x ′) :=D Y ΓEX (x, x′)D∗ Y =D Y Γ(EX x, EX x′)D∗ Y .
is aY-valued reproducing kernel onX. The output pushforward theorem also identifies the associated RKHS
as
HK ={D Y ◦F 0 :F 0 ∈ HΓEX },
with norm
(11)∥F∥ HK = inf
n
∥F0∥HΓEX :F=D Y ◦F 0
o
.
Using (9), everyF 0 ∈ HΓEX has the formF 0 =f◦E X for somef∈ HΓ. Therefore
HK ={D Y ◦f◦E X :f∈ HΓ}
and, inserting (10) into (11), we obtain
(12)∥F∥ HK = inf{∥f∥ HΓ :F=D Y ◦f◦E X }.
It remains to prove the simplified statement under exact minimum-norm recovery. By Theorem 2.1, we
have
DX =E ∗ X (EX E∗ X )−1, D Y =E ∗ Y (EY E∗ Y )−1.
Next, we assume that
DY ◦f 1 ◦E X =D Y ◦f 2 ◦E X .
Then, applyingE Y on the left andD X on the right givesf 1 =f 2.Hence the infimum in the minimal-
representative norm in (12) is attained by the unique representativef, and therefore
∥DY ◦f◦E X ∥HK =∥f∥ HΓ.
48

Proof of Corollary 3.4.By Theorem 3.3, everyF∈ H K can be represented asF=D Y ◦f◦E X for somef∈
HΓ. For any such representative,E Y F(x i) =E Y DY f(E X xi) =Af(U i).Hence the constraintsE Y F(x i) =
Si andAf(U i) =S i are equivalent, under the representationF=D Y ◦f◦E X. Since the norm inH K, i.e.
∥F∥ HK = inf{∥f∥ HΓ :F=D Y ◦f◦E X },
is the minimalH Γ-norm over all representatives inducing the sameF, minimizing overF∈ H K is equivalent
to minimizing over representativesf∈ HΓ. This proves the equivalence of the interpolation problems.
We now compute the interpolation formula. The observation map is
LΓ,A :H Γ →Z N Y , L Γ,Af= (Af(U 1), . . . , Af(UN )).
This map is bounded and linear because point evaluation is bounded in the RKHSH Γ andA=E Y DY is
bounded and linear by assumption onD Y . Forc= (c 1, . . . , cN )∈Z N Y , using the product inner product on
ZN Y , we compute as follows:
⟨LΓ,Af, c⟩ZN Y =
NX
j=1
⟨Af(U j), cj⟩ZY
=
NX
j=1
⟨f(U j), A∗cj⟩ZY
=
NX
j=1
⟨f,Γ(·, Uj)A∗cj⟩HΓ (13)
=
*
f,
NX
j=1
Γ(·, Uj)A∗cj
+
HΓ
where (13) follows from the reproducing property onH Γ.
Therefore
L∗ Γ,Ac=
NX
j=1
Γ(·, Uj)A∗cj
and
LΓ,AL∗ Γ,A = ΓA(U,U).
IfL Γ,A is surjective, equivalently ifΓ A(U,U)is boundedly invertible, the minimum-norm formula from
Theorem 2.1 gives
f=L ∗ Γ,A(LΓ,AL∗ Γ,A)−1S.
Evaluating atU∈Z X yields
f(U) = Γ A(U,U)Γ A(U,U) −1S.
For ridge regression, Theorem 2.1 yields
f λ(U) = Γ A(U,U)

ΓA(U,U) +λId ZN Y
−1S.
We note that these formulas correspond to standard kernel interpolation/ridge regression with kernelAΓ(·,·)A∗.
The formulas for F λ follow by composing withD Y andE X.
Finally, assume thatD X andD Y are the exact minimum-norm recovery maps. Then, Theorem 2.1 gives
A=E Y DY =I ZY and the encoded residuals reduce toAf(U i) =f(U i).The simplified interpolation and
ridge-regression formulas follow by settingA=I ZY in the general formulas.
Proof of Theorem 3.7.For the first statement, observe that
G(x)− G(x) =G(x)−D Y bG(EX x)
=

G(x)−D Y Genc(EX x)

+D Y

Genc − bG  (EX x).
49

Taking norms and applying the triangle inequality gives
∥G(x)− G(x)∥Y ≤ ∥G(x)−DY Genc(EX x)∥Y +∥D Y (Genc − bG)(EX x)∥Y .
Using the definition ofG enc gives the first estimate.
For the second statement, writingG enc :=

Genc(U1), . . . , Genc(UN )

∈Z N Y ,we have (analogously to
the derivation in the proof of Corollary 3.4)
bGenc,λ(z) = Γ(z,U)

Γ(U,U) +λId ZN Y
−1
Genc
and
bGλ(z) = Γ(z,U)

Γ(U,U) +λId ZN Y
−1
S,
whereS= (S 1, . . . , SN )∈Z N Y .By definition of the data-consistency residuals, we have
S=G enc +η, η= (η 1, . . . , ηN )∈Z N Y .
Therefore, forz∈Z X,
bGλ(z)− bGenc(z) = Γ(z,U)

Γ(U,U) +λId ZN Y
−1
S−G enc

= Γ(z,U)

Γ(U,U) +λId ZN Y
−1
η
= (RU,λη)(z).
Therefore,G enc − bGλ =  Genc − bGenc,λ  − RU,ληand
∥(Genc − bGλ)(EX x)∥ZY ≤ ∥(Genc − bGenc,λ)(EX x)∥ZY +∥R U,λη(EX x)∥ZY .
Plugging this into the first statement proves (a).
Finally, applying [42, Theorem 5.4] yields∥(G enc − bGenc,λ)(z)∥ZY ≤Q N,λ(z)∥Genc∥HΓ,λ.Inserting this
withz=E X (x)into (a) yields (b).
A.2.2 Proofs for Kernel Learning for Multi-Input, Multi-Output Operators
Proof of Proposition 3.9.Letx∈B R(X). We estimate as follows:
∥G(x)−D Y EY G(DX EX x)∥Y ≤ ∥G(x)−G(DX EX x)∥Y +∥G(D X EX x)−D Y EY G(DX EX x)∥Y
≤ω(∥x−D X EX x∥X ) +δ Y (G(DX EX x))(14)
≤ω(δ X (x)) +δ Y (G(DX EX x))(15)
where we used AssumptionO.1for (14) and (5) for (14) and (15). The proof of the second identity is analogous.
Proof of Lemma 3.11.Throughout the proof,C >0denotes a generic constant independent of the sampling
fill distances and of the functions being reconstructed. Its value may change from line to line.
We first establish the reconstruction estimate for a fixedj-th component. Foru j ∈ Hj, definee:=
uj −D j(Ejuj).By Theorem 2.1 and definition ofD j, we haveE j(Dj(Ejuj)) =E juj and thereforeE je= 0,
or equivalently,
(16)e| Aj = 0.
Using (16) in [3, Theorem 4.1] withr=s j and each integer derivative orderℓ= 0, . . . , tj,yields
(17)|e| Wℓ,qj (Ωj ) ≤Ch
sj −ℓ−nj

1
pj − 1 qj

+
j |e|Wsj ,pj (Ωj )
50

as soon ash j ≤h 0 j. Defineα j :=s j −t j −n j

1
pj − 1 qj

+
so that, for everyℓ= 0, . . . , tj,s j −ℓ−
nj

1
pj − 1 qj

+
=α j +t j −ℓand
h
sj −ℓ−nj

1
pj − 1 qj

+
j =h αj j htj −ℓ j ≤h αj j max{1, h0 j }tj −ℓ ≤h αj j max{1, h0 j }l0,j ≤Ch αj j
where we used the fact thath j ≤h 0 j for the first inequality. By definition of the Sobolev norms (with the usual
modification whenq j =∞) and inserting the latter in (17), we conclude that
∥e∥Wtj ,qj (Ωj ) ≤Ch αj j ∥e∥Wsj ,pj (Ωj ) ≤Ch αj j ∥e∥Hj
where we used the fact thatH j ,→W sj ,pj (Ωj)for the last inequality. Moreover,e=u j −D j(Ejuj)∈
ker(Ej),whileD j(Ejuj)∈ker(E j)⊥,as was shown in the proof of Theorem 2.1. Therefore,uj =D j(Ejuj)+
eis an orthogonal decomposition inH j, and
∥uj∥2 Hj =∥D j(Ejuj)∥2 Hj +∥e∥ 2 Hj ≥ ∥e∥2 Hj
and, combining the preceding estimates, we conclude that
∥uj −D j(Ejuj)∥Wtj ,qj (Ωj ) ≤C jhαj j ∥uj∥Hj .
Since the above argument holds for everyj= 1, . . . , J, the definition of the product norm yields
∥u−DEu∥ 2 X =
JX
j=1
∥uj −D j(Ejuj)∥2 Wtj ,qj (Ωj ) ≤
JX
j=1
C2 j h2αj j ∥uj∥2 Hj .
Proof of Lemma 3.13.Throughout the proof,C >0denotes a generic constant independent of the sampling
fill distances and of the functions being reconstructed. Its value may change from line to line.
Sincef∈ HΓ, it is an admissible competitor in the minimization problem defining bfλ. Therefore,
(18)
NX
i=1
∥ bfλ(Ui)−f(U i)∥2 2 +λ∥ bfλ∥2 HΓ ≤λ∥f∥ 2 HΓ.
Sincee λ(Ui) =f(U i)− bfλ(Ui),it follows that PN i=1 ∥eλ(Ui)∥2 2 ≤λ∥f∥ 2 HΓ,or, equivalently,
(19)∥e λ∥ℓ2(UN ;RdY ) ≤
√
λ∥f∥ HΓ.
Similarly, (18) also gives∥ bfλ∥HΓ ≤ ∥f∥HΓ and therefore,
(20)∥e λ∥HΓ =∥f− bfλ∥HΓ ≤ ∥f∥HΓ +∥ bfλ∥HΓ ≤2∥f∥ HΓ.
We now apply the vector-valued sampling inequality of [19, Theorem 17] toeλ ∈ HΓ with input dimension
dX, output dimensiond Y , and discrete exponentp= 2. Sinceγ= max{2,2, q}= max{2, q},we obtain:
|eλ|Ws,q(Υ;RdY ) ≤C

h
τ−s−d X

1
2 − 1 q

+
tr |eλ|Hτ (Υ;RdY ) +h dX /γ−s tr ∥eλ∥ℓ2(UN ;RdY )
!
≤C

h
τ−s−d X

1
2 − 1 q

+
tr ∥eλ∥HΓ +h dX /γ−s tr ∥eλ∥ℓ2(UN ;RdY )
!
(21)
≤C

h
τ−s−d X

1
2 − 1 q

+
tr ∥f∥ HΓ +h dX /γ−s tr √ λ∥f∥ HΓ
!
(22)
51

where we used the continuous embeddingH Γ ,→H τ (Υ;R dY )for (21) and (20) as well as (19) for (22).
Takingq=∞ands= 0,we have
 1
2 − 1 q  + = 1 2 , γ=∞, dX γ = 0
which implies
∥eλ∥L∞(Υ;RdY ) ≤C

hτ−d X /2 tr + √ λ  ∥f∥ HΓ.
Using the latter, we conclude that, for everyx∈Xsuch thatE X x∈Υ,
∥eλ(EX x)∥2 ≤ ∥eλ∥L∞(Υ;RdY ) ≤C

hτ−d X /2 tr + √ λ  ∥f∥ HΓ.
Proof of Theorem 3.15.Forj= 1, . . . , JX andk= 1, . . . , JY , define
αX,j :=s X,j −t X,j −n X,j
 1
pX,j
− 1 qX,j

+
and
αY,k :=s Y,k −t Y,k −n Y,k
 1
pY,k
− 1 qY,k

+
.
Fixx∈B R(HX )and for brevity, writeE X :=E HX , DX :=D HX , EY :=E HY , DY :=D HY .By Theorem
3.7, we have:
∥G(x)− G(x)∥Y
≤ ∥G(x)−DY EY G(DX EX x)∥Y +∥D Y ∥op ∥(Genc − bfλ)(EX x)∥2 +∥D Y ∥op ∥RU,λη(EX x)∥2
≤ω(δ X (x)) +δ Y (G(DX EX x)) +∥D Y ∥op ∥(Genc − bGenc,λ)(EX x)∥2 +∥D Y ∥op ∥RU,λη(EX x)∥2
(23)
≤ω




JXX
j=1
C2 X,j h2αX,j X,j ∥xj∥2 HX,j


1/2
 +
" JYX
k=1
C2 Y,k h2αY,k Y,k ∥(G(DX EX x))k∥2 HY,k
#1/2
+∥D Y ∥op ∥(Genc − bGenc,λ)(EX x)∥2 +∥D Y ∥op ∥RU,λη(EX x)∥2
(24)
≤ω



max
1≤j≤JX
CX,j hαX,j X,j
 

JXX
j=1
∥xj∥2 HX,j


1/2
 +

max
1≤k≤JY
CY,k hαY,k Y,k
 " JYX
k=1
∥(G(DX EX x))k∥2 HY,k
#1/2
+∥D Y ∥op C

hτ−d X /2 tr + √ λ  ∥Genc∥HΓ +∥D Y ∥op ∥RU,λη(EX x)∥2 (25)
=ω

max
1≤j≤JX
CX,j hαX,j X,j

∥x∥HX

+

max
1≤k≤JY
CY,k hαY,k Y,k

∥G(DX EX x)∥HY
+∥D Y ∥op C

hτ−d X /2 tr + √ λ  ∥Genc∥HΓ +∥D Y ∥op ∥RU,λη(EX x)∥2
≤ω

Rmax
1≤j≤JX
CX,j hαX,j X,j

+M R max 1≤k≤JY CY,k hαY,k Y,k +∥D Y ∥op C  hτ−d X /2 tr + √ λ  ∥Genc∥HΓ
(26)
+∥D Y ∥op ∥RU,λη(EX x)∥2
(27)
where we used Proposition 3.9 for (23), Lemma 3.11 for (24), Lemma 3.13 for (25) and AssumptionO.2for
(27).
52

B Experiment Setup
B.1 Out-of-distribution datasets
In this section, we summarize the details of out-of-distribution datasets for five PDE benchmarks for both
operator-valued and product-space learning frameworks.
We first consider the operator-valued learning framework. For PDE examples (conservation law, diffusion-
reaction-advection equation, and nonlinear Klein Gordon equation) where we only have finite-dimensional
parameter vectors, we take the following out-of-distribution parameter vectors:
•Conservation law:The components of parameter vectorα= [α 1, α2, α3, α4]⊤ are sampled from the
rangesα i ∈[0.8α c i ,1.2α c i ]with reference values given byα c = [1,1,1,0.1] ⊤ fori= 1,2,3,4.
•Diffusion-reaction-advection:The first three components of parameter vectorα= [α 1, α2, α3, α4, α5]⊤
are sampled from the rangesα i ∈[0.8α c i ,1.2α c i ]with reference values given byα c = [0.01,1,1] ⊤ for
i= 1,2,3.
•Nonlinear Klein Gordon:The components of parameter vectorα= [α 1, α2, α3]⊤ are sampled from
the rangesα i ∈[0.8α c i ,1.2α c i ]with reference values given byα c = [1,1,1] ⊤ fori= 1,2,3.
For the parametric diffusion–reaction equation and the parametric wave equation, we generate out-of-distribution
test samples by randomly drawing the parametric function from Gaussian processes whose distributions differ
from the one used for training. In particular, we consider the following three out-of-distribution datasets:
•OOD_matern: Gaussian process with a Matérn kernel (length scale parameterγ= 1and smoothness
parameterν= 0.5) and variance1.
•OOD_scale: Gaussian process with an RBF kernel (length scale parameterγ= 0.1) and variance1.
•OOD_var: Gaussian process with an RBF kernel (length scale parameterγ= 1) and variance0.1 2.
Next, we consider the product-space learning framework. For the conservation law, diffusion–reaction–
advection equation, and nonlinear Klein–Gordon equation, we consider the following out-of-distribution datasets:
•OOD_par: the same out-of-distribution of parameter vectors as above.
•OOD_init_GP: the initial conditions are randomly drawn from a Gaussian process with an RBF kernel
(length scale parameterγ= 1) and variance1.
•OOD_init_amp: the initial conditions follow the sinusoidal formulation with four sine functions,n i
uniformly sampled integers in[1,8], and amplitudesA i sampled uniformly from[−2,2].
•OOD_par_init_GP: the combination ofOOD_parandOOD_init_GP.
•OOD_par_init_amp: the combination ofOOD_parandOOD_init_amp.
For the parametric diffusion–reaction equation and the parametric wave equation, we consider the following
out-of-distribution datasets:
•OOD_par_kernel: the same asOOD_maternin the operator-valued learning framework.
•OOD_par_scale: the same asOOD_scalein the operator-valued learning framework.
•OOD_par_var: the same asOOD_varin the operator-valued learning framework.
•OOD_init: the same asOOD_init_ampabove.
•OOD_par_init: the combination ofOOD_par_scaleandOOD_init.
53

B.2 Hyperparameter choices
Methodk k W kU PCA Configuration
KernelMO-OV R (γ= 0.1) M (γ= 1, ν= 5/2) – –v(10 PCs) –
KernelMO-PS – R (γ= 100) M (γ= 1, ν= 5/2) R (γ= 100) M (γ= 1, ν= 5/2) u, v(10 PCs) –
DeepONet-C – – – – Small
MIONet – – – – Medium
MNO – – – – Large
Table 17: Hyperparameter choices and implementation details for the operator-valued learning experiments on the para-
metric conservation law.
Methodk k W kU PCA Configuration
KernelO R (γ= 100) M (γ= 1, ν= 5/2) – –u, v(10 PCs) –
KernelMO-PS – R (γ= 1) M (γ= 1, ν= 5/2) R (γ= 100) M (γ= 100, ν= 3/2) u, v(10 PCs) –
DeepONet – – – – Small
DeepONet-C – – – – Small
MIONet – – – – Medium
MNO – – – – Large
Table 18: Hyperparameter choices and implementation details for the product-space learning experiments on the para-
metric conservation law.
Methodk k W kU PCA Configuration
KernelMO-OV R (γ= 1) M (γ= 10, ν= 7/2) – –v(10 PCs) –
KernelMO-PS – R (γ= 100) M (γ= 10, ν= 5/2) R (γ= 100) M (γ= 10, ν= 5/2) u, v(10 PCs) –
DeepONet-C – – – – Small
MIONet – – – – Small
MNO – – – – Large
Table 19: Hyperparameter choices and implementation details for the operator-valued learning experiments on the para-
metric diffusion–reaction–advection PDE.
Methodk k W kU PCA Configuration
KernelO R (γ= 10) M (γ= 1, ν= 5/2) – –u, v(10 PCs) –
KernelMO-PS – R (γ= 1) M (γ= 1, ν= 5/2) R (γ= 100) M (γ= 100, ν= 3/2) u, v(10 PCs) –
DeepONet – – – – Small
DeepONet-C – – – – Small
MIONet – – – – Small
MNO – – – – Large
Table 20: Hyperparameter choices and implementation details for the product-space learning experiments on the
diffusion–reaction–advection equation.
54

Methodk k W kU PCA Configuration
KernelMO-OV R (γ= 1) M (γ= 1, ν= 5/2) – –v(10 PCs) –
KernelMO-PS – R (γ= 100) M (γ= 1, ν= 5/2) R (γ= 100) M (γ= 1, ν= 7/2) u, v(10 PCs) –
DeepONet-C – – – – Small
MIONet – – – – Medium
MNO – – – – Medium
Table 21: Hyperparameter choices and implementation details for the operator-valued learning experiments on the non-
linear Klein–Gordon equation.
Methodk k W kU PCA Configuration
KernelO R (γ= 10) M (γ= 1, ν= 5/2) – –u, v(10 PCs) –
KernelMO-PS – R (γ= 1) M (γ= 1, ν= 5/2) R (γ= 10) M (γ= 100, ν= 5/2) u, v(10 PCs) –
DeepONet – – – – Large
DeepONet-C – – – – Medium
MIONet – – – – Medium
MNO – – – – Large
Table 22: Hyperparameter choices and implementation details for the product-space learning experiments on the nonlin-
ear Klein–Gordon equation.
Methodk k W kU PCA Configuration
KernelMO-OV R (γ= 0.1) M (γ= 0.1, ν= 5/2) – –α, v(10 PCs) –
KernelMO-PS – R (γ= 100) M (γ= 1, ν= 5/2) R (γ= 100) M (γ= 0.1, ν= 5/2) α, u, v(10 PCs) –
DeepONet-C – – – – Medium
MIONet – – – – Medium
MNO – – – – Large
Table 23: Hyperparameter choices and implementation details for the operator-valued learning experiments on the para-
metric diffusion–reaction equation.
Methodk k W kU PCA Configuration
KernelO R (γ= 100) M (γ= 100, ν= 3/2) – –u, v(10 PCs) –
KernelMO-PS – R (γ= 1) M (γ= 1, ν= 5/2) R (γ= 1000) M (γ= 1000, ν= 5/2) α, u, v(10 PCs) –
DeepONet – – – – Small
DeepONet-C – – – – Small
MIONet – – – – Medium
MNO – – – – Large
Table 24: Hyperparameter choices and implementation details for the product-space learning experiments on the para-
metric diffusion–reaction equation.
55

Methodk k W kU PCA Configuration
KernelMO-OV R (γ= 1) M (γ= 1, ν= 5/2) – –α, v(10 PCs) –
KernelMO-PS – R (γ= 1) M (γ= 1, ν= 5/2) R (γ= 1000) M (γ= 1, ν= 5/2) α, u, v(10 PCs) –
DeepONet-C – – – – Medium
MIONet – – – – Small
MNO – – – – Large
Table 25: Hyperparameter choices and implementation details for the operator-valued learning experiments on the para-
metric wave equation.
Methodk k W kU PCA Configuration
KernelO R (γ= 10) M (γ= 100, ν= 3/2) – –u, v(10 PCs) –
KernelMO-PS – R (γ= 1) M (γ= 1, ν= 5/2) R (γ= 1000) M (γ= 1000, ν= 5/2) α, u, v(10 PCs) –
DeepONet – – – – Large
DeepONet-C – – – – Medium
MIONet – – – – Small
MNO – – – – Large
Table 26: Hyperparameter choices and implementation details for the product-space learning experiments on the para-
metric wave equation.
56
