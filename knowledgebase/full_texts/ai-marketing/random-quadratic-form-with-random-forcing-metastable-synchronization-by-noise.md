---
title: 'Random Quadratic Form with random forcing: Metastable synchronization by noise'
url: https://arxiv.org/abs/2608.16664
category: ai-marketing
subcategory: measurement
date: 2026-08
venue: ''
authors:
- Anna Shalova
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.16664
pages: 27
chars: 59561
fetched_at: '2026-11-08T13:29:34+00:00'
kb_version: 1
---

# Random Quadratic Form with random forcing: Metastable synchronization by noise

Random Quadratic Form with random forcing:
Metastable synchronization by noise
Anna Shalova
Korteweg-de Vries Institute for Mathematics, University of Amsterdam,
a.shalova@uva.nl
August 18, 2026
Abstract
We study the Random Quadratic Form (RQF) on a sphere in the presence of
random Brownian forcing. We show that the forcing does not effectively change the
law of the process but affects the synchronization properties of the system. While the
RQF without forcing exhibits partial synchronization due to the intrinsic symmetries,
the introduction of an arbitrarily small forcing results in long-term symmetry breaking
and leads to full synchronization.
In this work we focus on the small forcing regime and recover the multiscale
behavior of the two-point process. We show that in the first stage the model converges
to an anti-polar configuration due to the symmetries of the RQF and in the second
stage the two clusters meet due to the symmetry breaking phenomenon.
The model is motivated by continuous-time machine learning models such as
Neural ODEs and continuous-time formulations of transformers. In particular, the
results of this work explain the role of the bias and the scale of its initialization.
Contents
1 Introduction 2
1.1 Neural ODEs and Transformers . . . . . . . . . . . . . . . . . . . . . . . . 3
1.2 Literature overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
1.3 Main Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
2 Notation and Preliminaries 7
2.1 Preliminaries on SDEs. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
2.2 Random Dynamical Systems . . . . . . . . . . . . . . . . . . . . . . . . . . 9
2.3 Random Attractors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
3 Main results 11
3.1 Random attractor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
3.2 Metastable synchronization . . . . . . . . . . . . . . . . . . . . . . . . . . 15
3.3 Auxiliary lemmas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
1
arXiv:2608.16664v1  [math.PR]  17 Aug 2026

4 Multi-cluster and multiscale dynamics 21
4.1 Multiple clusters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
4.2 Multiple time-scales . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
1 Introduction
In this work we study the Random Quadratic Form (RQF) on a sphereSn−1 with Brownian
forcing given by the following stochastic differential equation:
dXt =P Xt∂QtXt +γP Xt∂Wt,(1)
whereP X denotes the projection onto the tangent space ofSn−1 atX
PX :=P TX Sn−1 =I−XX T ,
the noisy processQt : (0,∞)×Ω→Sym n is given by
Qt = 1√ 2 (Bt +B T t ),
where {Bij t : i, j∈ 1 . . . n}are independent Brownian motions andWt : (0,∞ ) × Ω →R n
is an n-dimensional Brownian motion independent ofQt. We use the notation∂Qt, ∂Wt
to specify that the equation is understood in the Stratonovich sense.
The RQF model was introduced in [ES26] as a stochastic counterpart of a gradient
flow of a quadratic functional and only included the multiplicative noise, namely the case
γ = 0was considered. Analogously to the deterministic setting, the system was shown
to exhibit clustering behaviour in the sense that any two solutions of Eq.(1) with γ = 0
driven by the same noisy process in the long-time limit become either aligned or anti-polar.
At the same time, the one point motion of the system is a Brownian motion and has no
preferred direction, so the nontrivial behavior only appears on the level of the two-point
motion. Such a phenomenon is known assynchronization by noiseand we provide a
rigorous formulation of synchronization by noise result for the RQF in Section 1.3.
The anti-polar limiting configuration can be explained by the intrinsic symmetry of
the RQF without forcing, which is violated in the presence of an arbitrarily small forcing
γ. As a result of that, the system with any non-zeroγ in the long-time limit synchronizes
to a single point, namely the anti-polar state is no longer stable.
At the same time, in the small forcing regimeγ↓ 0, the strong attraction to the
symmetric configuration dominates on the time scalet∼logγ −1 and before converging to
the random attractor consisting of a single point, the system approaches the anti-polar
configuration defined by the dynamics of the non-forced RQF. We call this phenomenon
metastable synchronizationbecause both of the limiting configurations, namely stable and
metastable ones, are synchronizing. In this work we characterize both of the attractive
configurations and the corresponding rates of convergence.
Despite changing the symmetry properties of the system, the given forcing preserves
the qualitative behaviour of the single-point process: for an arbitraryγ, the RQF is a
(rescaled) spherical Brownian motion. This, in particular, implies that the effect of the
forcing is also only noticeable at the level of the two-point process.
The rest of the paper is structured as follows. In the rest of the introduction we
discuss the main driving application from machine learning, give a literature overview
2

Figure 1: Ensemble of solutions of eq.(1) with different initial conditions driven by the
same realization of the noisy processesQt and Wt with the forcing parameterγ = 0.1. In
the first stage (the first row), the particles cluster into an anti-polar configuration and
follow the dynamics of the ’meta’-attractorAQ(ω). In the second stage (the second row),
the particles converge to the global random attractorA(ω)and continue moving as a
single cluster.
and conclude the section with a schematic statement of the main results. In Section 2
we give the necessary theoretical background on random dynamical systems and random
attractors. We introduce and prove the main results in Section 3. Finally, in Section 4 we
discuss how the results of this work can be extended to recover the metastable behaviour
with multiple (>2) scales.
1.1 Neural ODEs and Transformers
Neural ODEs, introduced in [CRBD18], are a class of neural networks in which the features
x(t)evolve continuously in time according to an ordinary differential equation
˙x(t) =f(θ(t), x(t), t), x0 ∈X in,
where x0 is the input data defined on the input spaceXin and θ are the parameters of the
neural network. This is in contrast to the classical feed-forward networks, in which the
features evolution is defined by a discrete-time dynamical system
xk+1 =f(θ k, xk), x 0 ∈X in.
3

Considering a specific parametrization of a Neural ODE, consisting of a single feed-forward
layer with a normalization step, the corresponding dynamics of features takes the form
˙x=P xs

M(t)x+B(t)

, x(0) =x 0 ∈S n−1,(2)
where s is an activation function and the time-dependent parametersM (t)and B(t)are
the weights and the biases of the linear layer.
Define the cumulative weight and biases processes as
Qt =
Z t
0
M(s)dsandW t =
Z t
0
B(s)ds.
Then, considering the linear activation functions(x) = x, we note that features in(2)
follow the RQF dynamics as in Eq.(1) and therefore the RQF can be understood as
a simplified model of a Neural ODE model. To justify the white-noise structure of the
driving processes we remark that in discrete-time neural networks, the parametersθk
of every layerk are usually initialized randomly and independently from layer to layer.
Hence, we argue that the RQF driven by the diffusion processesQt and Wt as defined in
(1) is a natural continuous-time proxy for a neural ODE at initialization. The relative
scale of the weight and the bias initialization is then encoded in the single parameterγ,
and, as we show below, this scale determines the long-time behaviour of the system.
Moreover, recently introduced continuous-time models of transformers [SABP22,
GLPR25] can be understood as an extension of the Neural ODE framework and are
specifically concerned with the joint dynamics of features corresponding to multiple in-
puts. In particular, the input of a continuous time transformer is a sequence of vectors
(xi(0) ∈X in)i=1...N, which in language modeling problems correspond to different words
in a text. In contrast to Neural ODEs, the dynamics of every feature vectorxi(t)in
transformers is additionally coupled to the states of all the other vectorsxj(t)through the
so-called Self-Attention mechanism and takes the form
˙xi =P xi (FF(xi) +Attn(x i;x 1, x2 . . . xN )),
FF(xi) =s(M xi +B),
Attn(xi;x 1, x2 . . . xN ) = 1P
j exiQT Kxj
X
j
exiQT Kxj V xj,
see [VSP+17, GLPR25] for an extensive description of the architecture. Such a structure
can be interpreted as an interacting particle system, where the Feed-Forward layers act as
an effective potential and Self-Attention layers describe the interaction between vectors.
In the absence of the interaction force, the tokens(xi)1≤i≤d are driven by the common
noise coming from the shared parametersM and B and thus follow the multipoint motion
of the RQF with forcing. Recently, clustering and metastability of tokens in transformers
have been extensively studied for the self-attention driven dynamics [GLPR24, GLPR25],
see Section 1.2 for details. In this work we follow the approach of [ES26] and provide a
counterpart of these results for the dynamics defined purely by the feed-forward layers.
In particular, our results imply the existence of metastable clustering of the multi-point
motion in Neural ODEs when the variance of the bias initialization is smaller than the
variance of the weights initialization.
4

1.2 Literature overview
Diffusions on a sphere.Diffusion processes on Sn−1 naturally arise in the context of
stability analysis of stochastic differential equations by means of the multiplicative ergodic
theorem. In particular, the Furstenberg–Khasminskii formula reduces the calculation of
the leading Lyapunov exponent to the ergodic averaging of a specific functional over the
ergodic measure of the projective process [Fur63, Kha11], see also [Arn98, Chapter 6] and
[IL01]. Therefore, synchronizing behaviour of diffusions on the sphere is closely related
to the Lyapunov stability of SDEs in Euclidean spaces and has been studied in various
formulations. Specifically, synchronization of diffusions on Sn−1 has been established:
for the canonical Brownian motion in [Bax86], for general isotropic Brownian flows in
[Rai99, CGS16] and for the RQF formulation in [ES26]. We remark that for each of these
models the one-point motion is a spherical Brownian motion and therefore carries no
distinctive information about the flow, which motivates the study of the two-point process.
We remark that the Euclidean counterpart of this picture is classical: the full Lyapunov
spectrum for isotropic Brownian flows onRd is computed in [LJ85], see also [BH86]. And
the random attractor in the stable regime is shown to be a singleton [LJ85, DLJ88].
Synchronization by noise.Synchronization of diffusion processes is an example of
a more general phenomenon which is known as synchronization by noise. For a general
class of random dynamical systems it has been formalized in [FGS17a], and we refer
the reader to this work for an extensive literature review on the topic. The approaches
allowing to establish synchronization by noise include multiplicative ergodic theorem
[ACW83, Bax91, CR04] and the Feller explosion test [Sch02, CGS16] which was also used
for the RQF without forcing in [ES26]. Alternatively, synchronization can be deduced from
the order-preserving properties of the dynamics [CF98, FGS17b]. Local synchronization
can also be established using large-deviations theory, see e.g. [MHM96, Tea08].
Metastability in particle systems.Classically, metastability of a stochastic system
refers to the phenomena observed in gradient-type systems when the system spends a large
time near the local minima of the corresponding energy. In such a setting the metastability
can be studied using a large deviations-based approach and, in particular, Eyring-Kramers
asymptotics [FW12, BG06, BdH15]. This work is concerned with a different setting,
namely small perturbation of astochasticprocess but not of a deterministic flow. At
the same time, our result can be understood as an analog of the classical metastability
phenomenon but on the level of thetwo-point motion.
Since we characterize the relative convergence of multi-point motion, another related
phenomenon is the transient clustering in interacting particle systems where the fast
scale corresponds to the clusters formation. In particular, on a finite-particle level, the
metastable clustering of interacting diffusions and the corresponding Lyapunov exponents
are studied in [AEG26]. In a mean-field setting, the cluster formation and merging
dynamics is discussed in [GGH+26, WSHW26]. We also remark that the mean-field
formulation is a special case of the dynamic metastability framework [OR07]. However,
the clustering mechanism studied in these works is of a different nature and is caused by
the pairwise interactions. Note that interactions are not present in our setting.
5

Clustering and metastability in transformers.The continuous-time models of trans-
formers can be interpreted as interacting particle systems [SABP22, GLPR24, GLPR25]
and have been shown to exhibit (metastable) clustering dynamics. In particular, the long-
time clustering of tokens has been established in various settings, see [Rig26] for an overview
of the results and recent works [BKK+25, ABRR26, LMP+26]. In particular, the rate of
convergence to a single cluster in this context is established in [CLPR25]. The transient
clustering dynamics in the context of transformers is studied in [GKPR24, BPA25, BPA26].
Closest to the present work are the stochastic formulations of Neural ODEs and
transformers, in which the randomness appears due to the random initialization of the
parameters. In particular, the pathwise synchronization of the flow of randomly initialized
NeuralODEsischaracterizedin[ ES26,ABG+26]. Similarly, clusteringinrandomattention-
based models is established in [FSE+26, KGR26]. We also remark that the pathwise
synchronization is conceptually different from the clustering in noisy transformer models
[SS26, BBR25], which correspond to interacting particle systems with independent noises.
1.3 Main Results
In this work we study the effect of additive noise on the two-point process of the RQF
and the metastable behaviour arising in the small-forcing regimeγ→ 0. We characterize
both the global attractor and the transient clustering dynamics appearing on the faster
time-scale. We complement the analysis by studying the one-point motion and showing
that no metastability arises on the level of one-point dynamics.
To introduce the results, we will require some preliminary facts. Recall that the
processes Qt and Wt are independent and therefore the probability space generated by
(Qt, Wt)is in fact a product spaceΩ = ΩQ × ΩW, where Qt = Qt(ωQ)and Wt = Wt(ωW ).
In case γ = 0, the spaceΩW is redundant and easily factors out. In addition, the SDE
(1) has smooth coefficients and thus admits a path-wise solution, see Proposition 2.6. We
denote the corresponding solution map byX ω t (x0), where x0 ∈S n−1 denotes the initial
conditionX 0 =x 0.
With this notation we are ready to present the main results. In particular, recall the
characterization of the two-point process without forcing from [ES26].
Theorem 1.1( γ = 0, [ES26, Theorem 4.8]).There exists a random setAQ(ω) = AQ(ωQ)
consisting of two anti-polar points
AQ(ω) ={a Q(ω),−a Q(ω)},
where aQ(ω)is measurable with respect to the past, and for allx0 ∈S n−1 the pathwise
solutionX ω t (x0)in the long-time limit converges toAQ(θtω):
dist(X ω t (x0), AQ(θtω))→0 Ω−a.s.,
whereθ t is the time-shift defined in Eq.(3).
The random set AQ is in fact the forward attractor of the corresponding random
dynamical system as defined in Section 2.3. In case of the non-zero forcing,AQ(ω)no
longer attracts all the trajectories in the long-time limit due to the effect of the additive
noise. Instead, all the trajectories synchronize to a single-valued attractorA(ω). However,
on a time-scalet∼log|γ| −1, the setAQ(ω)is still attractive, and thus in the forced regime
we call AQ(ω)the ’meta’-attractor after the ’meta’-stable behaviour it describes. We,
therefore, obtain the following characterization of the dynamics forγ̸= 0.
6

Theorem 1.2( γ̸ = 0).There exists a random set AQ(ωQ)as in Theorem 1.1 and a
random singletonA(ω) ={a(ω)}such that the dynamics consists of the two stages:
•(convergence to the ’meta’-attractorA Q):
Edist(X ω t (x0), AQ(θtω))≲e − 1 2 t +|γ|C(n, t),
•(convergence to the global attractorA):
Edist(X ω t (x0), A(θtω))≲e −λ(n,γ)t, λ(n, γ)∼ 1 2 γ2(n−1),
where θt is the time-shift as in Eq.(3) and C(n, t) ≲ √ne2t for larget. The characterization
holds for an arbitrary choice ofx0.
In particular we obtain explicit convergence rates in expectation to the random attractor
in both forced and non-forced regimes, which allows us to study the intermediate regime of
convergence to the anti-polar configuration. We highlight that the two attractorsAQ and
A are structurally different and therefore the long-term behaviour of the two-point motion
of the system with forcing differs from the non-forced case and exhibits a multi-scale
behavior, see Figure 1. At the same time, this difference cannot be detected on the level
of one point motion as follows from the following result, see also Theorem 3.1.
Theorem 1.3(RQF is a Brownian motion).For anyγ∈R the processXt/(1+γ2) is an
Sn−1-valued Brownian motion.
Acknowledgments and use of AI.I am grateful to Maximilian Engel and Enrique
Carro Garrido for many insightful discussions on random attractors. The work was
supported by the Dutch Research Council (NWO), in the framework of the program
VI.Vidi.233.133 ‘A Rigorous Framework for Transient Random Dynamics’.
I used AI at different stages of the manuscript preparation. In particular, the use of
a regularized function in Lemma 3.2 and Proposition 3.8 was suggested by an AI and
the code used to produce illustrations was generated by an LLM. The paper was written
entirely by me and all mistakes are mine.
2 Notation and Preliminaries
In this section we introduce the notation and give the necessary theoretical background
on SDEs and random dynamical systems. We refer the reader to [Arn98] for a detailed
introduction to RDS.
For a separable metric spaceX we denote the Borelσ-algebra on X by B(X ). Let
ΩQ = C0(R,R n×n)andΩ W = C0(R,R n)be the spaces of continuous functions satisfying
ω(0) = 0equipped with the metricd:
d(ω,bω) :=
∞X
N=1
1
2N
∥ω−bω∥N
1 +∥ω−bω∥ N
,∥ω−bω∥ N := sup
|t|≤N
∥ω(t)−bω(t)∥,
7

and let F Q = B(ΩQ),F W = B(ΩW ). Let PQ and PW be the Wiener probability measures
on F Q and F W, where the Wiener probability measure of anRm-valued Brownian motion
is given by
P({ω∈Ω :ω 1(t)≤x 1, . . . , ωm(t)≤x m}) = 1 (2π|t|)m/2
Z x1
−∞
· · ·
Z xm
−∞
e−∥y∥2/2|t|dy1 · · ·dym,
for all x∈R m. We denote the product probability space by(Ω,F,P ) = (ΩQ × ΩW ,F Q ×
F W ,P Q ×P W ).
Finally, we define the family of time shifts(θt)t∈R on the product space(Ω,F)by
θtω(·) :=ω(t+·)−ω(t),(3)
and remark that this family preserves the Wiener measure of a setA∈ F, namely
P(θ−1 t A) =P(A)for allt∈R, A∈ F.
2.1 Preliminaries on SDEs.
Let M be a smooth Riemannian manifold without boundary. Consider anM-valued Ito
SDE of the form
dXt =F 0 (Xt) dt+
mX
j=1
Fj (Xt) dWj t , X 0 =x∈ M, t∈R.(4)
Fixing a probability space of the Brownian motionWt we define the pathwise solution of
(4) as follows.
Definition 2.1(Pathwise solution).Given a probability space generated by an m-
dimensional two-sided Brownian motion(Ω,F,P ), an SDE(4) is said to admit a pathwise
solution on(Ω,F,P )with initial conditionx0 ∈ Mif there exists a mapX ω : Ω →C (R,M )
satisfyingω-a.s
X ω t =x 0 +
Z t
0
F0 (X ω s (x0)) ds+
mX
j=1
Z t
0
Fj (X ω s (x0)) dWω,j s , X ω 0 =x 0,
whereW ω,j t is thej-th component of the sample pathWω t .
Definition 2.2(Infinitesimal generator).Let the diffusion Xt be a weak solution of(4),
the operatorL:C ∞(M)→C ∞(M)
(Lf)(x) := lim
t↓0
1
t E

f(X t)−f(X 0)

X0 =x 
is called theinfinitesimal generatorofX t.
The infinitesimal generator describes the evolution of statistics of a diffusion process,
and thus can be used to track the expected distance between two solutions along the
dynamics. This is the key component of the proof of Theorems 3.4 and 3.9, where we will
require the following elementary version of Dynkin’s formula.
8

Proposition 2.3(Dynkin’s formula, [Øks03, Theorem 7.4.1]).Let L be the infinitesimal
generator of a diffusion processXt on R with X0 = x0, then for anyf∈C ∞ c and for all
t∈R +
Ef(X t) =f(x 0) +E
Z t
0
(Lf)(X s)ds

.
Finally, we remark that infinitesimal generatorL and its L2 adjoint L∗ define the
backward and forward Kolmogorov evolutions respectively. The latter,
∂tρt −L ∗ρt = 0,
describes the evolution ofρt = lawX t and is also known as the Fokker-Planck equation.
2.2 Random Dynamical Systems
Definition 2.4(Random dynamical system (RDS)).Let(Ω ,F,P )be an abstract proba-
bility space and(M,B (M))be a compact Riemannian manifold with the corresponding
Borelσ-algebra. An RDS consists of the two components:
1. model of the noise:a family ofF-measurable measure-preserving maps(θt : Ω →
Ω)t∈R, satisfying:
θ0ω=ω,∀ω∈Ω,
θt+sω=θ tθsω,∀t, s∈R, ω∈Ω,
2. model of the dynamics:a( B(R) ⊗ F ⊗ B(M))-measurable mapφ : R× Ω × M → M
which, for allω∈Ωandx∈ Msatisfies thecocycle property
φ(0, ω, x) =x,andφ(t+s, ω, x) =φ(t, θ sω, φ(s, ω, x)),∀s, t∈R.
Given an RDS(φ, θ), for anyu, v∈R with u < v, we denote byFu,v the sub-σ-algebra
generated by the random variablesφ(t, θsω, x)for x∈ Mand t, s∈R with u≤s≤v
and0 < t≤v−s . We say that the RDS satisfies the Markov property if its future is
independent of its past, namely:
Definition 2.5(Markov RDS).The RDS( θ, φ)is calledMarkovif F−∞,0 and F0,∞ are
independent.
Due to the following result, any SDE with sufficiently regular coefficients can be
uniquely reformulated in the form of a Markov RDS.
Proposition 2.6(SDE as an RDS, [Arn98, Theorem 2.3.42]).Consider an Ito SDE
(4) or the corresponding Stratonovich SDE and assume thatF0 ∈C 1,δ(M, TM)and
every Fj ∈C 2,δ(M, TM)for some δ∈ (0, 1]. Let(Ω ,F,P )be a (fixed) probability space
generated by a two-sidedm-dimensional Brownian motion. Then there exists a unique
(B(R)⊗ F ⊗ B(M))-measurable mapφ(t, ω, x)such that
•X ω t =φ(t, ω, x)is a pathwise solution of(4),
• (θ, φ)is a Markov RDS, where( θt)t∈R is the family of time shifts defined in Eq.(3).
9

Due to their equivalence, we switch to the RDS notationφ(t, ω, x)for the pathwise
solutions of Eq. (4).
Moreover, to use the probabilistic estimates of Dynkin’s type for Markov RDS with
random initial conditions we will need the following property of conditional expectation.
Lemma 2.7(Freezing lemma).Let( θ,ˆφ)be a Markov RDS on a manifoldM over the
probability space(Ω,F,P )and let β : Ω → Mbe an F−∞,0-measurable random point. Let
ψ:C(R +,M)→Rbe a Borel-measurable bounded map and define
Ψ(x) :=E[ψ( ˆφ(·, ω, x))],∀x∈ M.
ThenΨis Borel-measurable, bounded and
E[ψ( ˆφ(·, ω, β(ω)))

F−∞,0] = Ψ(β(ω)),Ω−a.s..
In particular,Ψ(β(ω))isF −∞,0-measurable and satisfies
inf
x
Ψ(x)≤E[Ψ(β(ω))]≤sup
x
Ψ(x).
Proof. Since ˆφisMarkov, themap( ω, x) 7→ˆφ(·, ω, x)is F0,∞×B(M)-measurable, implying
that the same is true for the composition functionψ( ˆφ(·, ω, x)). With this remark, the
result is a special case of the ’freezing’ lemma [Bal17, Lemma 4.1].
In particular, the freezing lemma decouples expectations with respect to the past and
future when the correspondingσ-algebras are independent.
2.3 Random Attractors
Given a state spaceM and a probability space(Ω,F,P ), we say that a set-valued map
A : Ω → B(M)is arandom compact setif it isΩ-a.s. compact and the function
dist(x0, A(ω))is F-measurable for all x0 ∈ M. With this, we define a random point
attractor of an RDS as the random set attracting all trajectories under the forward
dynamics, namely
Definition 2.8(Random Point Attractor).A random compact set(A(ω))ω∈Ω is called
theforward point attractor, if
•it isφ-invariant:
φ(t, ω, A(ω)) =A(θtω),∀t∈R,
•for everyx∈ M
dist

φ(t, ω, x), A(θtω)

→0,Ω−a.s.
A random attractorA(ω)is calledminimalif for any other random attractor ˜A(ω)
we haveA(ω) ⊆ ˜A(ω),Ω-a.s. Finally, replacing the a.s. convergence with convergence in
probability we obtain the definition of aweak random point attractor. We note that if a
strong point attractor exists, it is also a weak point attractor but the converse is not true.
Existence of a weak point attractor for ergodic Markov RDS on compact state spaces is
guaranteed by the correspondence theorem, see [KS12, Theorem 4.2.9]. In particular, the
following holds.
10

Proposition 2.9(Existence of a weak point attractor).Let(θ, φ)be a Markov RDS on a
compact Riemannian manifold which admits a unique ergodic measureρ, then the weak
limit
φ(t, θ−tω,·) ∗ρ w →µ ω,ast→ ∞,
exists almost surely and the random set
A(ω) := supp(µω)
is the minimal weak point attractor of the RDS(θ, φ).
As follows from the result by Le Jan [LJ87], the sample measures can either consist
entirely of atoms or be fully continuous with no atoms at all, namely the following
characterization holds.
Proposition 2.10(Discrete vs. continuous sample measures [LJ87]).The sample measures
µω are eitherΩ-a.s. continuous, namely for every x∈ Msatisfy µω({x}) = 0, or are
Ω-a.s. discrete measures supported onN∈Natoms and given by
µω = 1 N
NX
i=1
δai(ω),
where eacha i : Ω→ Mis anF −∞,0-measurable random point.
3 Main results
We begin by recovering the Fokker-Planck equation of the RQF SDE with forcing. We
establish that RQF is a rescaled spherical Brownian motion, which, in particular, implies
that it is ergodic and the unique invariant distribution is the uniform measure onSn−1.
Theorem 3.1(RQF is a Brownian motion).Let ρt = law(Xt)as in the eq. (1), then for
anyγ∈R,ρ t is the unique classical solution of the rescaled heat flow onSn−1:
∂tρt − 1 +γ 2
2 ∆ρt = 0, ρ t
w
→law(X 0)ast↓0,
where∆is the Laplace-Beltrami operator on Sn−1. In particular, the uniform measure
¯ρ= 1 volSn−1 (Sn−1) volSn−1 is the unique ergodic measure of the RQF, wherevolSn−1 is the volume measure of then−1-dimensional sphere.
Proof.Consider the following Stratonovich diffusions onSn−1:
dUt =P Ut∂QtUt,
dVt =P Vt∂Wt.
The process Vt is a natural definition of a Brownian motion onSn−1. Moreover, the
generator of the process Ut is LU = 1 2 ∆, see [ES26, Theorem 4.3]. Since the driving
processes Qt and Wt are independent, we conclude that the generator of the RQF with
forcing takes the form
Lf= (L U +γ 2LV )f= (1 +γ 2) 2 ∆f,∀f∈C ∞.
Finally, since the Laplace-Beltrami operator onSn−1 is essentially self-adjoint we conclude
thatlawX t solves the given Fokker-Planck equation and hence the result.
11

3.1 Random attractor
We now move to studying theω-pointwise properties of the solutions to(1). For this we
define an essential component of the proof, namely the auxiliary processZt = ⟨Xt, Yt⟩,
where the couple(Xt, Yt)solving:
dXt =P Xt∂QtXt +γP Xt∂Wt, X 0 ∈S n−1,
dYt =P Yt∂QtYt +γP Yt∂Wt, Y 0 ∈S n−1 (5)
is the two-point motion of the RQF with forcing. Note that any two points on a sphere
x, y∈S n−1 coincide iff ⟨x, y⟩ = 1and are anti-aligned iff ⟨x, y⟩ = −1. Therefore,
convergence to either an anti-polar configuration or a singleton of a stochastic process can
be both characterized in terms of the dynamics of the corresponding processZt, namely
its boundary behaviour at ±1. In particular, for γ̸ = 0we will require the following
moment-bound on(1−Z t)to upper bound the distance to the attractor.
Lemma 3.2(Lyapunov function for γ̸ = 0).Let( Xt, Yt)be the two-point motion of the
RQF with forcingγ̸ = 0and let Zt = ⟨Xt, Yt⟩. Then for all p∈ (0, γ2(n−1)+4 2(γ2+4) )and every
z0 =⟨X 0, Y0⟩ ∈[−1,1]:
E(1−Z t)p ≤(1−z 0)pe−pαt,
where
α= min{γ 2(n−1), γ2(n−1) + 4−2p(γ 2 + 4))},
in particular,α >0.
The proof of the bound is largely technical and therefore is deferred to Section 3.3. In
addition, we will need the following pointwise bound.
Lemma 3.3.Forx, y∈S n−1 letz=⟨x, y⟩, then∀p∈(0, 1 2 ]:
dist(x, y)≤ π 2p (1−z) p.
Proof. First note that the geodesic distance on a sphere is upper bounded by the Euclidean
distance dist(x, y) ≤ π 2 ∥x−y∥ . At the same time, expanding the norm of the difference
we get
∥x−y∥ 2 =∥x∥ 2 +∥y∥ 2 −2⟨x, y⟩= 2(1−z),
and sincex, y∈S n−1 implies1−z∈[0,2]:
∥x−y∥=
√
2(1−z)
1
2 = √ 2(1−z) 1 2 −p(1−z) p ≤2 1−p(1−z) p.
Combining the inequalities we get the result.
We now proceed to characterizing attractors of the RQF with forcing.
Theorem 3.4(Random attractor with forcing).Let γ̸ = 0, then there exists anF−∞,0-
measurable map a : Ω →S n−1 such that A(ω) = {a(ω)} is the strong forward point
attractor of the RQF RDS. Moreover, for allx0 ∈S n−1:
E(dist(φ(t, ω, x0), A(θtω)))≤πe −λγ t,(6)
whereλ γ = 2γ2 γ2+4 (n−1).
12

Proof. The proof is structured as follows. First we prove almost sure collapsedist(Xt, Yt) →
0using the Lemma 3.2. Then we relate the two-point dynamics to the weak forward
random point attractor of the corresponding RDS. Finally, we apply the freezing Lemma
2.7 to establish almost sure convergence and the estimate (6).
Step 1: Lyapunov function.Applying Lemma 3.2 withp = 2 γ2+4, we obtainα(γ, n, p) =
γ2(n−1)and therefore:
E(1−Z t)p ≤(1−z 0)pe−λγ t,
where λγ = 2γ2 γ2+4 (n−1). Since the bound holds for an arbitrary choice of the initial condition
z0 ∈ [−1, 1], the stochastic process ξt = (1 −Z t)p is a non-negative supermartingale.
Moreover, it is uniformly bounded by construction, namelyξt ≤ 2p. Thus, by Doob’s
supermartingale convergence theorem, the convergenceξt → 0holdsΩ-almost surely.
Hence, using the pointwise comparison dist(x, y) ≤ π 2p (1 −z )p from Lemma 3.3, we
conclude thatdist(X t, Yt)→0almost surely for everyX 0, Y0 ∈S n−1.
Step 2: Random attractor.By Proposition 2.9, there exist the sample measuresµω
and a weak point attractorA(ω). Since the sphere is a compact manifold and the RQF is
ergodic, by [Bax91, Proposition 2.6]:
(Pt)∗(¯ρ×¯ρ)→E(µω(dx)×µ ω(dy))
where P ∗ t is the adjoint of the semigroup of the two-point process(5). At the same time,
for the test functionf(x, y) = dist(x, y)usingdist(Xt, Yt)→0we obtain
lim
t→∞
Z
Ptf(x, y)d(¯ρ×¯ρ) = 0 =
Z
dist(x, y)E(µω(dx)×µ ω(dy)).
and thus µω isΩ-a.s. supported on a single point, which we denote bya(ω). Applying
Proposition 2.10, we conclude that the setA(ω) := {a(ω)} is the minimal weak point
attractor of the RQF with forcing anda(ω)is measurable with respect to the past.
Step 3: Almost sure convergence.First note that by theφ-invariance of the random
attractor we necessarily haveA(θtω) = {a(θtω)} = {φ(t, ω, a(ω))}. Thus, to upgrade to an
almost sure convergence we argue as follows. Consider the Markov RDSˆφcorresponding
to the two-point process of the RQF:
ˆφ(t, ω,(x, y)) = (φ(t, ω, x), φ(t, ω, y)),
and the functionψ:C(R +,S n−1)×C(R +,S n−1)→ {0,1}defined as
ψ(u, v) := 1{dist(u(t), v(t))→0},
with the corresponding functionΨ :S n−1 ×S n−1 →[−1,1]:
Ψ(x, y) :=E(ψ(φ(·, ω, x), φ(·, ω, y))) =P
h
dist(Xt, Yt)→0

X0 =x, Y0 =y i .
From step 1 we know thatΨ((x, y)) ≡ 1. Consider the randomF−∞,0-measurable point
β(ω) = (x 0, a(ω)), then applying freezing Lemma 2.7 to the RDSˆφ, we deduce
P[dist(φ(t, ω, x0), φ(t, ω, a(ω))→0] =E[Ψ(β(ω))]≥inf x,y Ψ(x, y) = 1.
Step 4: Convergence rate.Arguing analogously to step 4 we obtain the expected rate
of convergence to the random attractor. In particular, consider the sameˆφand β(ω)as
13

in the previous step and define a family of functionsκt : C(R+,S n−1) ×C (R+,S n−1)for
t∈R +:
κt(u, v) = dist(u(t), v(t)),
which is bounded by construction. The correspondning functionΨthen takes the form
Ψ(x, y) :=E[κt( ˆφ(·, ω,(x, y)))] =E[κt(φ(·, ω, x), φ(·, ω, y))]
=E
h
dist(Xt, Yt)

X0 =x, Y0 =y i .
Then, applying the freezing Lemma 2.7 and using the exponential convergence from Lemma
3.2 we obtain
E[dist(φ(t, ω, x0), φ(t, ω, a(ω))] =E[Ψ(β(ω))]≤sup
x,y
Ψ((x, y)) =πe−λγ t,
where the bound
sup
x,y
Ψ((x, y))≤sup
z∈[−1,1]
(1−z) p π 2p e−λγ t =πe −λγ t.
follows from Lemmas 3.2 and 3.3.
Remark 3.5(Contraction rate).We remark that the top Lyapunov exponent classically
provides local exponential convergence rate for points in theω-dependent neighborhood of
the attractor; namely bounds of the form
dist(φ(t, ω, x), A(θtω))≤C(ω, x)e Λmaxt dist(x, A(ω)),∀x: dist(x, A(ω))< r(ω, x),
which do not generally imply exponential convergence to the attractor in expectation.
Notably, for the classical Brownian flow onSn−1 given by
dXt =P Xt∂Wt,(7)
[Bax86, Theorem 5.3(ii)] establishes almost sure exponential convergence with the rate
e− 1 2 (n−1)t. We also remark that our rate−λγ/γ2 recovers the result of [Bax86]
− λγ
γ2 =− 2(n−1) 4 +γ 2 → −1 2 (n−1)
in the limitγ→0.◁
Remark 3.6(Rate for large γ).For large γ the second branch ofα(γ, n, p)becomes
optimal in Lemma 3.2, giving the optimal valueˆp= γ2(n−1)+4 4(γ2+4) . At the same time, forn≥ 4
and large enoughγ2 we have ˆp≥ 1 2. Thus we can takep = 1 2 directly estimating √1−z
to get the contraction rate
λγ =pα(p, γ, n) =1 2 (γ2(n−1) + 4−γ 2 −4) = (n−2) 2 γ2
forγ≫1. ◁
14

Remark 3.7(Generalizations).We expect similar estimates to hold for a larger class
of isotropic diffusions onSn−1. In particular, for the classical formulation of a spherical
Brownian motion (7) the proof applies in a simplified form since the γ-independent
components are not present. In particular, takingp↑ 1 2 and following the steps of the
proof above, yields the following estimate
Edist( ˜φ(t, ω, x0), A(θtω))≤C 0e− 1 2 (n−2)t,
which is consistent with the rate for the largeγ regime in Remark 3.6. We also note that
the rate in expectation is weaker than the almost sure ratee− 1 2 (n−1)t established in [Bax86,
Theorem 5.3(ii)].
To cover the casen = 2, it is also possible to choosep∈ (0, 1 2 )still giving exponential
contraction and therefore almost sure convergence. For example, takingp = 1 4 we get the
estimate
Edist( ˜φ(t, ω, x0), A(θtω))≤C 0e− 1 8 t.
◁
3.2 Metastable synchronization
Finally, we consider the small forcing regimeγ→ 0and establish the multi-scale behaviour
of the two-point process(5). In this Section we slightly change the notation and use the
upper index γ to denote the RQF process with the forcingγ, namely X γ t and, analogously,
φγ for the corresponding RDS. In particular,X 0 t denotes the RQF without forcing as
studied in [ES26]. Since the dynamics for smallt is dominated by quadratic component,
the proof relies on a coupling argument between the processesXγ t andX 0 t.
First, arguing analogously to the Theorem 3.4, we establish convergence rates for the
non-forced RQFφ 0.
Proposition 3.8(Exponential convergence for γ = 0).Let γ = 0, then there exists a
random setA Q(ω) =A Q(ωQ)consisting of two anti-polar points
AQ(ω) ={a Q(ω),−a Q(ω)},
wherea Q(ω)is anF Q −∞,0-measurable random point and the RQF RDS satisfies:
E(dist(φ0(t, ω, x0), AQ(θtω)))≤ π√ 2 e− 1 2 t,(8)
for allx 0 ∈S n−1
The proof of Proposition 3.8 is analogous to the proof of Theorem 3.4 and is postponed
to Section 3.3. We are now moving to the main result.
Theorem 3.9(Metastability of the two-point motion).For any γ∈R there exists a
random set
AQ(ωQ) ={a Q(ωQ),−a Q(ωQ)},
wherea Q(ωQ)is anF Q −∞,0-measurable function, and the RQF RDS(φγ, θ)satisfies
Edist(φ γ(t, ω, x0), AQ(θtω))≤ π√ 2 e− 1 2 t + π√n−1 4 |γ| √ e4t −1,(9)
for allx 0 ∈S n−1.
15

Remark 3.10(The time scale).The two terms of the upper bound(9) balance at t∈R +
solving
e− 1 2 t = √n−1 4 |γ| √ e4t −1,
which corresponds to
t= 2 5 log|γ| −1 − 1 5 logn+O(1)
as γ→ 0. This estimate supports the statement of the ’meta’-attractorAQ being attractive
on the time scale of orderlog|γ|−1.◁
Proof. We consider the coupling of the RQFs with and without forcing(φ0, φγ)and by
triangle inequality obtain
Edist(φ γ(t, ω, x0), AQ(θtω))≤Edist(φ 0(t, ω, x0), AQ(θtω))
+Edist(φ 0(t, ω, x0), φγ(t, ω, x0)) :=A(t) +B(t).
By Proposition 3.8, the first term decays exponentiallyA(t) ≤ π√ 2 e− 1 2 t, and thus we only
need to bound the distance betweenφ0 andφ γ.
LetV t :=X 0 t −X γ t , V0 = 0, thenV t solves the following SDE
dVt = n−1 2  γ2X γ t −V t  dt−γP X γ t dWt + (PX 0 t dQtX 0 t −P X γ t dQtX γ t ),(10)
and applying Ito formula tof (x) = ∥x∥2 we conclude that the evolution of∥Vt∥2 follows
the dynamics
d∥Vt∥2 = (γ2(n−1) +λ V ∥Vt∥2)dt+ dM t,(11)
where
λV = 2

X γ t , X0 t 2 + 2
X γ t , X0 t  − γ2(n−1) 2 ≤4,
and EMt = 0is a martingale, see Lemma 3.12 for details. Integrating Eq.(11) and taking
expectation on both sides then gives
E∥Vt∥2 ≤ ∥V0∥2 +
Z t
0
4E∥Vs∥2ds+γ 2(n−1)t.
Applying standard Gronwall argument we obtain the upper bound
E∥Vt∥2 ≤ γ2(n−1) 4 (e4t −1)≤ γ2(n−1) 4 (e4t −1).
Finally, note that by Cauchy-Schwartz inequalityB(t) ≤
p
E∥Vt∥2. Therefore, using
dist(x, y) ≤ π 2 ∥x−y∥ and combining the estimates forA(t)and B(t)we get the result.
3.3 Auxiliary lemmas
We begin with characterizing the dynamics of the processZt, which is used to establish
the moment bound in Lemma 3.2 and Proposition 3.8.
16

Lemma 3.11(Dynamics of Zt).Let( Xt, Yt)be the two-point motion of the RQF with
forcing and letZt =⟨X t, Yt⟩. ThenZ t solves the Ito stochastic differential equation
dZt =

γ2(1−Z t)(n−2−Z t)−2Z t(1−Z 2 t )  dt
−Z t(X T t dQtXt +Y T t dQtYt) + 2XT t dQtYt +γ(1−Z t)(Xt +Y t)T dWt.
In particular, the infinitesimal generator of the processZt, takes the form
(Lγf)(z) = (1−z)

γ2(n−2−z)−2z(1 +z)  ∂zf
+ (1−z) 2(1 +z)(2(1 +z) +γ 2)∂zzf,(12)
for anyf∈C ∞([−1,1]).
Proof.We start with reformulating the RQF (1) in the Ito form:
dXt =− (n−1)(1 +γ 2) 2 Xtdt+P XtdQtXt +γP XtdWt,
which follows from [ES26, Lemma 4.9] and the classical representation of a Brownian
motion onS n−1. Then, applying Ito’s lemma to the functionf(x, y) =⟨x, y⟩we obtain
dZt = df(X t, Yt) =X T t dYt +Y T t dXt + d[Xt, Yt]
=−(n−1)(1 +γ 2)Ztdt+ d[X t, Yt] + dMγ t ,(13)
where the martingaleM γ t is given by the following equation
dM γ t =−Z t(X T t dQtXt +Y T t dQtYt) + 2XtdQtYt +γ(1−Z t)(Xt +Y t)T dWt.
Calculating the quadratic covariation[Xt, Yt] =
R t
0 q(Zs)ds we obtain the following expres-
sion for the functionq:
q(z) =q γ=0(z) +γ 2
X
i,j
P i,j x P i,j y =q γ=0(z) +γ 2
X
i,j
(δi,j −x ixj)(δi,j −y iyj)
=nz−3z+ 2z 3 +γ 2(n+z 2 −2),
where
qγ=0(z) =nz−3z+ 2z 3
is the quadratic covariation of the quadratic noise component of the RQF as follows
from the proof of [ES26, Lemma 4.9]. Plugging the expression into(13) we obtain the
cumulative drift
−(n−1)(1 +γ 2)z+nz−3z+ 2z 3 +γ 2(n+z 2 −2) =γ 2(1−z)(n−2−z)−2z(1−z 2).
Finally, to obtain (12) we calculate the covariance of the processZt:
Σ(z) = Σγ=0(z) +γ 2
X
i
(1−z) 2(xi +y i)2 = 4(1−z 2)2 + 2γ2(1−z) 2(1 +z)
whereΣ γ=0(z) = 4(1 −z 2)2 is the covariance of the quadratic part derived in [ES26,
Theorem 4.8], and hence the result.
17

We are now ready to prove Lemma 3.2 and Proposition 3.8.
Proof of Lemma 3.2.By Lemma 3.11, the generator of the processZt takes the closed
form and is therefore decoupled from the dynamics of(Xt, Yt). We consider the test
functiong p,δ = (1−z+δ) p forδ, p∈(0,1). Note thatg p,δ is smooth on[−1,1]and since
the process is restricted to the interval[−1, 1]the discontinuity of g′ p,δ at z = 1 + δ does
not play any role. Forgp,δ we calculate
(Lγgp,δ)(z) =−p(1−z)

γ2(n−2−z)−2z(1 +z)  (1−z+δ) p−1
+p(p−1)(1−z) 2(1 +z)(2(1 +z) +γ 2)(1−z+δ) p−2
:=−pΛ p(n, γ, z)gp,δ +R p(δ, γ, z),
where
Λp(n, γ, z) =γ2(n−2−z)−2z(1 +z)−(p−1)(1 +z)(2(1 +z) +γ 2)
=γ 2(n−1) + (z+ 1)  2−p(γ 2 + 2(1 +z))  ,
Rp(n, δ, γ, z) =pδ(1−z+δ)p−1(γ2(n−2−z)−2z(1 +z))
−p(p−1)(1−z+δ) p−2(1 +z)(2(1 +z) +γ 2)δ(δ+ 2(1−z))
=:A+B
Lets= 1 +zand rewriteΛ p as
Λp(n, γ, z) =γ2(n−1) +s(2−p(γ 2 + 2s)).
Since it is a concave function ofs for any given interval it is minimized at one of the end
points. Sincez∈[−1,1], and therefores∈[0,2]we conclude that
min
z∈[−1,1]
Λp(n, γ, z) = min{γ2(n−1), γ2(n−1) + 4−2p(γ 2 + 4))}:=α(γ, n, p),
implying that for everyp∈ (0, p∗), where p∗ = γ2(n−1)+4 2(γ2+4) , α(·,·, p)is a strictly positive
function. At the same time, using z∈ [−1, 1], p∈ (0, p∗)and p∗ < 1we obtain the
following upper bounds:
|A| ≤δ(1−z+δ) p−1(γ2(n−1) + 4)≤δ p(γ2(n−1) + 4)
|B| ≤δ2(1−z+δ) p−22(4 +γ 2)≤2δ(1−z+δ) p−1(4 +γ 2)≤2δ p(4 +γ 2),
hence,
|Rp(n, δ, γ,·)| ≤δp(γ2n+ 12) :=δ pβ(γ, n)
on[−1,1]. Applying Dynkin’s formula (Proposition 2.3) togp,δ for allδ >0we obtain
Egp,δ(Zt)≤g p,δ(z0) +E
Z t
0
(−pα(γ, n, p)gp,δ(Zs) +δ pβ(γ, n))ds

.
Using a standard variation of constants estimate we therefore conclude that
Egp,δ(Zt)≤g p,δ(z0)e−pα(γ,n,p)t +δ p β(γ, n) pα(γ, n, p).
Since the inequalitygp,0(z) ≤g p,δ(z)holds for all δ >0pointwise on[ −1, 1], we can bound
thep-th moment of(1−Z t)by:
E(1−Z t)p ≤E(1−Z t +δ) p ≤g p,δ(z0)e−pα(γ,n,p)t +δ p β(γ, n) pα(γ, n, p)
Taking limitδ→0concludes the proof.
18

Proof of Proposition 3.8.First note that the existence of the strong forward point attractor
AQ(ω)follows directly from [ES26, Theorem 4.8]. The proof of the estimate(8) follows the
structure of the proof of Theorem 3.4 with the Lyapunov functionhp,δ(z) = (1 −z 2 + δ)p.
In particular the generator ofZ0 t takes the form
(L0f)(z) =−2z(1−z 2)∂zf(z) + 2(1−z 2)2∂zzf(z),
for allf∈C ∞([−1,1]). Plugging inh p,δ we obtain the expression
L0hp,δ = 4pz2(1−z 2)(1−z 2 +δ) p−1
+ 4p(1−z 2)2(1−z 2 +δ) p−2((p−1)2z 2 −(1−z 2 +δ))
= 4p(1−z 2 +δ) p(z2 + (p−1)2z 2 −(1−z 2))
+ 4pδ(1−z 2 +δ) p−2  (1−2z 2)(1−z 2 +δ) + 2(1−p)z 2[2(1−z 2) +δ] 
:=−4p ˆΛp(z)hp,δ + ˆRp(z, δ),
where
ˆΛp(z) = (1−2pz 2)
ˆRp(z, δ) = 4pδ(1−z 2 +δ) p−2  (1−z 2)(1 + 2(1−2p)z 2) +δ(1−2pz 2)  ,
and forp∈(0, 1 2 ]
| ˆRp| ≤4pδ(1−z 2 +δ) p−2(3(1−z 2) +δ)≤12pδ p.
Choosing p = 1 4 we get ˆΛ 1 4 (z) ≥ 1 2 and reproducing the variation of constants estimate
from Lemma 3.2 we bound the growth of the random variable(1−Z2 t ) 1 4 by
E(1−Z 2 t ) 1 4 ≤(1−z 2 0) 1 4 e− 1 2 t.
Since the points converge to either polar or anti-polar configuration, we define
ξt := min(∥Xt −Y t∥,∥X t +Y t∥),
and, using∥X t ±Y t∥=
p
2(1±z), obtain
ξt ≤
p
∥Xt +Y t∥∥Xt −Y t∥=
4
p
4(1−Z t)(1 +Z t) =
√
2(1−Z 2 t ) 1 4 ,
which immediately yields
Eξt ≤
√
2e− 1 2 t.
Similarly to the proof of Theorem 3.4, applying the freezing argument and usingdist(x, y) ≤
π
2 ∥x−y∥we conclude that
Edist(φ(t, ω, x0), AQ(θtω))≤ π 2 Eξt ≤ π√ 2 e− 1 2 t.
Where
AQ(θtω) ={φ 0(t, ω, aQ(ω)),−φ 0(t, ω, aQ(ω))}
by invariance of the random attractor.
19

Finally, we derive the dynamics of the process∥Vt∥2 used in the proof of Theorem 3.9.
Lemma 3.12(Dynamics of ∥Vt∥2).Consider X 0 t , Xγ t and Vt as in Eq. (10), and let
Ut =∥V t∥2, thenU t solves
dUt =b(X 0 t , Xγ t , Ut)dt+ dM t,
whereM t is a martingale withEMt = 0and
b(X 0 t , Xγ t , Ut) =γ 2(n−1) +U t

2

X γ t , X0 t 2 + 2
X γ t , X0 t  − γ2(n−1) 2  .
Proof.Applying Ito’s lemma tof(x) =∥x∥ 2 =⟨x, x⟩we obtain
df(V t) = 2⟨V t,dV t⟩+ d[V t, Vt]
The first term gives
2⟨V t,dV t⟩= (n−1)(γ 2 ⟨Vt, Xγ t ⟩ −Ut)dt+ dM t =−(n−1)U t

1 + 1 2 γ2

dt+ dM t,
where we used
⟨Vt, Xγ t ⟩=
X 0 t −X γ t , Xγ t  =
X 0 t , Xγ t  −1 =− 1 2
X 0 t −X γ t , X0 t −X γ t  =− 1 2 ∥Vt∥2.
Calculating the quadratic covariation[Vt, Vt] =
R t
0 q(s)dswe obtain
q(s) = 1 2 X i,j,k  P i,j X γ s (X γ s )k −P i,j X 0s (X 0 s )k +P i,k X γ s (X γ s )j −P i,k X 0s (X 0 s )j 2 +γ 2 X i,j (P i,j X γ s )2
:=I+II.
The second term is essentially the trace of the projection matrix and thereforeII =
γ2(n−1).
Letσ k i,j(x) := 1√ 2 (P i,j x xk +P i,k x xj), then, simplifying the first term, we obtain
I=
X
i,j,k
(σk i,j(X γ t ))2 + X
i,j,k
(σk i,j(X 0 t ))2 −2 X
i,j,k
σk i,j(X 0 t )σk i,j(X γ t ),(14)
where for alla, b∈S n−1
X
i,j,k
σk i,j(a)σk i,j(b) = (n−3)⟨a, b⟩+ 2⟨a, b⟩3 .
as follows from the proof of [ES26, Lemma 4.9]. In particular, fora=bwe obtain
X
i,j,k
(σk i,j(a))2 = (n−3) + 2 =n−1.
Plugging it into (14) and using∥Vt∥2 = 2−2⟨X 0 t , Xγ t ⟩we obtain
I= 2(n−1)−2(n−3)

X 0 t , Xγ t  −4
X 0 t , Xγ t 3
=∥V t∥2((n−1) + 2
X 0 t , Xγ t 2 + 2
X 0 t , Xγ t  ),
20

Figure 2: On the left: the ensemble of solutions of Eq.(17) driven by the same noise
from different initial conditions. The system gradually approaches each of the random
attractors for k = 7, 3and1. On the right: the dynamics of pairwise scalar products
between the particles showing the formation and dissolvement of the clusters.
and hence the total drift takes the form
b(X 0 t , Xγ t , Ut) =γ 2(n−1)−(n−1)U t

1 + 1 2 γ2

+U t((n−1) + 2

X 0 t , Xγ t 2 +
X 0 t , Xγ t  )
=γ 2(n−1) +U t

2

X γ t , X0 t 2 + 2
X γ t , X0 t  − γ2(n−1) 2  .
Finally note that the processMt satisfiesM 0 = 0and is given by
dMt =
X
i
hi tdW i t + X
i,j
gi,j t dBi,j t ,|h i t|,|g i,j t |< C,
where allh i t, gi,j t are adapted processes. ThusMt is a martingale andEMt = 0.
4 Multi-cluster and multiscale dynamics
In this section we discuss how the same approach can be extended to the cases of multi-
clustered attractors and multi-scale dynamics. From now on we only consider the dynamics
on the circle, namely the casen = 2. Formulating a Brownian motion on a sphere ofn >2
dimensions with a discrete random attractor consisting ofk >2points is generally an
open question.
4.1 Multiple clusters
To construct a system with a random attractor consisting ofk >1points we consider the
angular representation of the RQF on the circle as in [ES26, Section 5.1]. In particular,
consider the Stratonovich SDE withk-harmonic coefficients of the form
dϕt = cos(kϕt)∂B 1 t + sin(kϕt)∂B 2 t ,(15)
21

where B1,2 t are independent Brownian motions. Notice that for anyk∈N the variable
ψt =kϕ t satisfies the equation
dψt =kcosψ t∂B 1 t +ksinψ t∂B 2 t .(16)
The model(16) is the angular representation of the (rescaled) classical Brownian motion
as in Eq.(7) on S1, implying that so is(15). Moreover, the RDS corresponding to(16) is
fully synchronizing, namely its random point attractor is almost surely a singleton [Bax86,
Section 5]. Therefore, the random attractor of thek-harmonic model(15) consists of at
mostkpoints and the following extension of [ES26, Proposition 5.1] holds.
Proposition 4.1(Harmonic model on S1).Let k∈N and ϕt be the harmonic model on
R/2πZ ∼= S1 defined in Eq.(15), then
(i)ϕ t is a Brownian motion
(ii) the minimal weak random point attractorA(ω)of the corresponding RDS is supported
on exactlykequidistantF −∞,0-measurable random points:
A(ω) =

a(ω) + 2mπ k :m= 0. . . k−1  .
Proof. The infinitesimal generator of the process(16) is L = k2 2 ∂2 ψψ, changing the variables
back to ϕ gives(i). To show(ii)note that the proof of [ES26, Proposition 5.1] applies
with the reparametrizationψt =kϕ t.
At the same time, according to the Remark 3.7, we expect the model(16) to satisfy at
least
Edist(ψ(t, ω, x0), A(θtω))≤C 0e− k2 8 t.
The fact dist(ϕ1, ϕ2) = k−1 dist(ψ1, ψ2)therefore implies exponential convergence to the
random attractor in expectation for thek-harmonic model at the same ratee− k2 8 t.
4.2 Multiple time-scales
To construct a model with multiple time scales note that the RQF with forcing in angular
coordinates is written as
dϕt = (cos(2ϕt)∂B 1 t + sin(2ϕt)∂B 2 t ) +γ(cos(ϕ t)∂B 3 t + sin(ϕt)∂B 4 t ),
where the harmonic noise withk = 1is treated as perturbation of a harmonic model
with k = 2. We emphasize that the perturbation corresponds to the lower harmonic
and that the multiscale dynamics would not be present in the opposite case, as follows
from the estimates in Theorem 1.2 forγ≫ 1. Indeed, if a higher harmonic serves as a
small perturbation, then the unperturbed system synchronizes to a singleton on the fast
time-scale and the perturbation will not be able to split the mass into two points again.
Thus, to construct an model exhibiting a multiscale synchronization we consider a cascade
ofmharmonic noises of a decreasing order, namely the SDE of form:
dϕt =
m−1X
i=0
γi(cos(kiϕt)∂B i,1 t + sin(kiϕt)∂B i,2 t ), k i > ki+1,(17)
where Bi,1, Bi,2 are independent Brownian motions. We first note thatϕ is a rescaled
Brownian motion on the circle.
22

Proposition 4.2(Multiharmonic model is a Brownian motion).Let ϕt be the multi-
harmonic model as in Eq.(17), then ϕt/w(γ,m) is a Brownian motion, wherew(γ, m) =Pm−1
i=0 γ2i.
Proof. As follows from Proposition 4.1 and the independence of the driving processes
Bi,1, Bi,2, the generator of the multiharmonic processϕt is Lf = 1 2 Pm−1 i=0 γ2i∆and hence
the result.
We remark that the time scale appearing in the Fokker-Planck equation of the multihar-
monic model does not depend on the harmonicski but only on the number of components
m and the small parameterγ. At the same time, the parameterski define the structure
of the attractive configuration. In particular, the model withm harmonics admits m− 1
’meta’-attractors Ai(ω) : i = 0 . . . m−2and one global attractor Am−1(ω)where the
structure thej-th attractor depend on the harmonics(ki)i≤j.
To show the existence ofm different random attractors and the correspondingm-
scale behaviour we argue as follows. We define the first random attractorA0(ω)as the
attractor of k0-harmonic model(15). According to Proposition 4.1, it consists of exactly
k0 equidistant points and is exponentially attractive with a rate independent onγ as
discussed above. By a coupling argument analogous to the proof of Theorem 3.9, we also
conclude that the divergence fromA0(ω)is linear inγ.
To recover the second scale we defineA1(ω)as the random attractor of the truncated
system driven by the first two harmonic noises:
dϕ1 t =
1X
i=0
γi(cos(kiϕ1 t )∂B i,1 t + sin(kiϕ1 t )∂B i,2 t ).
By Proposition 2.9, there exists a weak point attractorA1(ω)of the truncated system
bi-harmonic model ϕ1 t and its structure only depends on the first two harmonic numbers
k0 andk 1. Iterating this construction and considering the next truncated model
dϕ2 t =
2X
i=0
γi(cos(kiϕ2 t )∂B i,1 t + sin(kiϕ2 t )∂B i,2 t ).
we obtain a cascade of random weak point attractors.
We also expect that the explicit exponential rates of convergence to the random point
attractors Ai(ω)are available when ki modk i+1 = 0for all i < m. In this case Ai(ω)
consists of exactlyki equidistant points and, by analogy with the RQF, the Lyapunov
function of the two-point process at thei-th time scale is the corresponding harmonic
function f (ξ1, ξ2) = (1 −cos (ki(ξ1 −ξ 2)))p. We conjecture that in this case an analog of
Theorem 1.2 could be formulated iteratively for each truncation.
At the same time, we expect the multiscale behavior to appear in a general multi-
harmonic setting and we illustrate it on Figure 2. We show the dynamics of the multi-point
motion of the system(17) with m = 3and k = 7, 3, 1. As expected, at three different
scales the model concentrates around different number of clusters. It is important to
note that the harmonics are not divisible and thus the random attractorA1(ω)is not an
equidistant triplet. In this work we do not specify the structure ’meta’-attractors of a
general multi-harmonic model. In addition, we remark that the transition between the
’meta’-attractors follows a non-trivial dynamics which is also outside of the scope of this
article.
23

References
[ABG+26] Andrea Agazzi, Giuseppe Bruno, Eloy Mosig García, Samuele Saviozzi, and
Marco Romito. Stochastic scaling limits and synchronization by noise in deep
transformer models.arXiv preprint arXiv:2604.26898, 2026.
[ABRR26] Albert Alcalde, Leon Bungert, Konstantin Riedl, and Tim Roith. Quantifying
concentration phenomena of mean-field transformers in the low-temperature
regime.arXiv preprint arXiv:2605.10931, 2026.
[ACW83] L. Arnold, H. Crauel, and V. Wihstutz. Stabilization of linear systems by
noise.SIAM J. Control Optim., 21(3):451–461, 1983.
[AEG26] Zachary P Adams, Maximilian Engel, and Rishabh S Gvalani. Separation of
time scales in weakly interacting diffusions.Archive for rational mechanics
and analysis, 250(3):33, 2026.
[Arn98] Ludwig Arnold.Random Dynamical Systems. Springer, Berlin, 1998.
[Bal17] Paolo Baldi. Stochastic calculus. InStochastic Calculus: An Introduction
Through Theory and Exercises, pages 215–254. Springer, 2017.
[Bax86] Peter H. Baxendale. Asymptotic behaviour of stochastic flows of diffeomor-
phisms: two case studies.Probab. Theory Related Fields, 73(1):51–85, 1986.
[Bax91] Peter H Baxendale. Statistical equilibrium and two-point motion for a stochas-
tic flow of diffeomorphisms. InSpatial Stochastic Processes: A Festschrift
in Honor of Ted Harris on his Seventieth Birthday, pages 189–218. Springer,
1991.
[BBR25] Krishnakumar Balasubramanian, Sayan Banerjee, and Philippe Rigollet. On
the structure of stationary solutions to McKean–Vlasov equations with appli-
cations to noisy transformers.arXiv preprint arXiv:2510.20094, 2025.
[BdH15] Anton Bovier and Frank den Hollander.Metastability: A Potential-Theoretic
Approach, volume 351 ofGrundlehren der mathematischen Wissenschaften.
Springer, 2015.
[BG06] Nils Berglund and Barbara Gentz.Noise-Induced Phenomena in Slow-Fast
Dynamical Systems: A Sample-Paths Approach. Springer, 2006.
[BH86] Peter H. Baxendale and Theodore E. Harris. Isotropic stochastic flows.Ann.
Probab., 14(2):1155–1179, 1986.
[BKK+25] Martin Burger, Samira Kabri, Yury Korolev, Tim Roith, and Lukas Weigand.
Analysis of mean-field models arising from self-attention dynamics in trans-
former architectures with layer normalization.Philosophical Transactions A,
383(2298), 2025.
[BPA25] Giuseppe Bruno, Federico Pasqualotto, and Andrea Agazzi. Emergence of
meta-stable clustering in mean-field transformer models. InThe Thirteenth
International Conference on Learning Representations, 2025.
24

[BPA26] Giuseppe Bruno, Federico Pasqualotto, and Andrea Agazzi. A multiscale anal-
ysis of mean-field transformers in the moderate interaction regime.Advances
in Neural Information Processing Systems, 38:133305–133341, 2026.
[CF98] Hans Crauel and Franco Flandoli. Additive noise destroys a pitchfork bifurca-
tion.J. Dynam. Differential Equations, 10(2):259–274, 1998.
[CGS16] Michael Cranston, Benjamin Gess, and Michael Scheutzow. Weak synchro-
nization for isotropic flows.Discrete and Continuous Dynamical Systems-B,
21(9):3003–3014, 2016.
[CLPR25] Shi Chen, Zhengjiang Lin, Yury Polyanskiy, and Philippe Rigollet. Quantita-
tive clustering in mean-field transformer models.arXiv:2504.14697, 2025.
[CR04] Tomás Caraballo and James C Robinson. Stabilisation of linear PDEs by
Stratonovich noise.Systems & control letters, 53(1):41–50, 2004.
[CRBD18] Ricky T. Q. Chen, Yulia Rubanova, Jesse Bettencourt, and David Duvenaud.
Neural ordinary differential equations. InAdvances in Neural Information
Processing Systems, volume 31, 2018.
[DLJ88] Richard W. R. Darling and Yves Le Jan. The statistical equilibrium of an
isotropic stochastic flow with negative Lyapunov exponents is trivial. In
Séminaire de Probabilités XXII, volume 1321 ofLecture Notes in Math., pages
175–185. Springer, 1988.
[ES26] Maximilian Engel and Anna Shalova. Random quadratic form on a sphere:
Synchronization by common noise.arXiv preprint arXiv:2603.06187, 2026.
[FGS17a] Franco Flandoli, Benjamin Gess, and Michael Scheutzow. Synchronization by
noise.Probability Theory and Related Fields, 168(3):511–556, 2017.
[FGS17b] Franco Flandoli, Benjamin Gess, and Michael Scheutzow. Synchronization
by noise for order-preserving random dynamical systems.Ann. Probab.,
45(2):1325–1350, 2017.
[FSE+26] Lev Fedorov, Michaël E Sander, Romuald Elie, Pierre Marion, and Math-
ieu Laurière. Clustering in deep stochastic transformers.arXiv preprint
arXiv:2601.21942, 2026.
[Fur63] Harry Furstenberg. Noncommuting random products.Transactions of the
American Mathematical Society, 108(3):377–428, 1963.
[FW12] Mark I. Freidlin and Alexander D. Wentzell.Random Perturbations of Dynam-
ical Systems, volume 260 ofGrundlehren der mathematischen Wissenschaften.
Springer, 3 edition, 2012.
[GGH+26] NJ Gerber, Rishabh S Gvalani, Martin Hairer, Grigorios A Pavliotis, and
André Schlichting. Formation of clusters and coarsening in weakly interacting
diffusions.Nonlinearity, 39(7):075023, 2026.
25

[GKPR24] Borjan Geshkovski, Hugo Koubbi, Yury Polyanskiy, and Philippe Rigollet.
Dynamic metastability in the self-attention model.arXiv:2410.06833, 2024.
[GLPR24] Borjan Geshkovski, Cyril Letrouit, Yury Polyanskiy, and Philippe Rigollet.
The emergence of clusters in self-attention dynamics.Advances in Neural
Information Processing Systems, 36, 2024.
[GLPR25] Borjan Geshkovski, Cyril Letrouit, Yury Polyanskiy, and Philippe Rigol-
let. A mathematical perspective on transformers.Bulletin of the American
Mathematical Society, 62(3):427–479, 2025.
[IL01] Peter Imkeller and Christian Lederer. Some formulas for lyapunov exponents
and rotation numbers in two dimensions and the stability of the harmonic
oscillator and the inverted pendulum.Dynamical Systems: An International
Journal, 16(1):29–61, 2001.
[KGR26] Hugo Koubbi, Borjan Geshkovski, and Philippe Rigollet. Homogenized trans-
formers.arXiv preprint arXiv:2604.01978, 2026.
[Kha11] Rafail Khasminskii.Stochastic stability of differential equations. Springer
Science & Business Media, 2011.
[KS12] Sergei Kuksin and Armen Shirikyan.Mathematics of two-dimensional turbu-
lence, volume 194 ofCambridge Tracts in Mathematics. Cambridge University
Press, Cambridge, 2012.
[LJ85] Yves Le Jan. On isotropic Brownian motions.Z. Wahrscheinlichkeitstheorie
verw. Gebiete, 70:609–620, 1985.
[LJ87] Y. Le Jan. Équilibre statistique pour les produits de difféomorphismes aléa-
toires indépendants.Ann. Inst. H. Poincaré Probab. Statist., 23(1):111–120,
1987.
[LMP+26] Sixu Li, Thomas Jacob Maranzatto, Jan Peszek, Trevor Teolis, Semih Akkoc,
Konstantin Riedl, Sennur Ulukus, and Nicolás García Trillos. On the diverse
dynamical behaviors arising in deep linear transformers.arXiv preprint
arXiv:2607.18584, 2026.
[MHM96] R.E. Mahony, U Helmke, and J.B. Moore. Gradient algorithms for principal
component analysis.The ANZIAM Journal, 37(4):430–450, 1996.
[Øks03] Bernt Øksendal. Stochastic differential equations. InStochastic differential
equations: an introduction with applications, pages 65–84. Springer, 2003.
[OR07] Felix Otto and Maria G Reznikoff. Slow motion of gradient flows.Journal of
Differential Equations, 237(2):372–420, 2007.
[Rai99] Olivier Raimond. Flots browniens isotropes sur la sphere. InAnnales de
l’Institut Henri Poincare (B) Probability and Statistics, volume 35, pages
313–354. Elsevier, 1999.
26

[Rig26] Philippe Rigollet. The mean-field dynamics of transformers. InInternational
Congress of Mathematicians 2026. SIAM, 2026.
[SABP22] Michael E Sander, Pierre Ablin, Mathieu Blondel, and Gabriel Peyré. Sink-
formers: Transformers with doubly stochastic attention. InInternational
Conference on Artificial Intelligence and Statistics, pages 3515–3530. PMLR,
2022.
[Sch02] Michael Scheutzow. Comparison of various concepts of a random attractor:
A case study.Archiv der Mathematik, 78(3):233–240, 2002.
[SS26] Anna Shalova and André Schlichting. Solutions of stationary McKean–Vlasov
equation on a high-dimensional sphere and other Riemannian manifolds.Adv.
Nonlinear Anal., 15(1):Paper No. 20250141, 2026.
[Tea08] Oliver M. Tearne. Collapse of attractors for ODEs under small random
perturbations.Probab. Theory Related Fields, 141(1-2):1–18, 2008.
[VSP+17] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones,
Aidan N Gomez, Łukasz Kaiser, and Illia Polosukhin. Attention is all you
need.Advances in neural information processing systems, 30, 2017.
[WSHW26] Nathalie Wehlitz, Richard Scherzer, Carsten Hartmann, and Stefanie Winkel-
mann. Energetic characterisation of transient clustering dynamics in
aggregation-diffusion systems.arXiv preprint arXiv:2605.30243, 2026.
27
