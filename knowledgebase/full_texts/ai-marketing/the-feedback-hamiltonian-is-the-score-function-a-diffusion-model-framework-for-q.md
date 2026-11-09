---
title: 'The Feedback Hamiltonian is the Score Function: A Diffusion-Model Framework for Quantum Trajectory
  Reversal'
url: https://arxiv.org/abs/2604.21210
category: ai-marketing
subcategory: measurement
date: 2026-04
venue: ''
authors:
- Sagar Dubey
- Alan John
source: arxiv
pdf_url: https://arxiv.org/pdf/2604.21210
pages: 14
chars: 37674
fetched_at: '2026-11-08T13:29:08+00:00'
kb_version: 1
---

# The Feedback Hamiltonian is the Score Function: A Diffusion-Model Framework for Quantum Trajectory Reversal

The Feedback Hamiltonian is the Score Function: A
Diffusion-Model Framework for Quantum Trajectory
Reversal
Sagar Dubey
Stony Brook University
Stony Brook, NY 11794, USA
sagar.dubey@stonybrook.edu
Alan John
Stony Brook University
Stony Brook, NY 11794, USA
alan.john@stonybrook.edu
Abstract
In continuously monitored quantum systems, the feedback protocol of García-Pintos, Liu, and
Gorshkov reshapes the arrow of time: a HamiltonianHmeas =rA/τ applied with gainX tilts
the distribution of measurement trajectories, withX <−2producing statistically time-reversed
outcomes. Why this specific Hamiltonian achieves reversal, and how the mechanism relates to
score-based diffusion models in machine learning, has remained unexplained.
We compute the functional derivative of the log path probability of the quantum trajectory
distribution directly in density-matrix space. Combining Girsanov’s theorem applied to the
measurement record, Fréchet differentiation on the Banach space of trace-class operators, and
Kähler geometry on the pure-state projective manifold, we prove thatδlogP F/δρ =rA/τ =
Hmeas. The García-Pintos feedback Hamiltonian is the score function of the quantum trajectory
distribution—exactly the object Anderson’s reverse-time diffusion theorem requires for trajectory
reversal. The identification extends to multi-qubit systems with independent measurement
channels, where the score is a sum of local operators.
Two consequences follow. First, the feedback gainX generates a continuous one-parameter
family of path measures (for feedback-active Hamiltonians with[H,A ]̸= 0), with X =−2
recovering the backward process in leading-order linearization—a structure absent from classical
diffusion, where reversal is binary. Second, the score identification enables machine learning
(ML) score estimation methods—denoising score matching, sliced score matching—to replace the
analytic formula when its idealizations (unit efficiency, zero delay, Gaussian noise) fail in real
experiments.
1 Introduction
The arrow of time—the observed asymmetry between forward and backward processes—has distinct
origins in classical and quantum physics. In thermodynamics it arises from entropy increase. In
quantum mechanics it has a more fundamental source: the act of measurement. Each measurement
outcome is correlated with the quantum state just before it, and this correlation is the statistical
signature of temporal direction. Observing an anticorrelation—outcomes systematically pointing
the wrong way relative to the state—is the signature of a time-reversed trajectory.
García-Pintos, Liu, and Gorshkov [1] showed that this quantum arrow can be engineered. By
constructing a feedback HamiltonianHmeas = rA/τ —a sequence of pulses proportional to the
measurement outcomer, the measured observableA, and the inverse measurement strength1/τ—
and applying it with a tunable gain parameterX, they demonstrated that the statistical signature of
a quantum trajectory can be continuously reshaped: the arrow can be reduced, canceled, or reversed.
1
arXiv:2604.21210v1  [quant-ph]  23 Apr 2026

The parameterX <− 2produces trajectories statistically indistinguishable from time-reversed
ones. García-Pintos et al. deriveHmeas from the stochastic master equation, and demonstrate its
effect numerically, but do not connect it to the score-based diffusion literature or explain why this
particular construction achieves reversal from an information-geometric perspective.
The machine learning community has spent the last decade developing score-based diffusion
models for generative AI. The key insight of this field, due to Anderson [2] and made computationally
practical by Song et al. [3], is that any forward stochastic process can be exactly reversed if one
knows its score function—the gradient of the log-probability of the current state,∇logp t(x). A
neural network trained to estimate this score function can run the process backwards, generating
new data by denoising from pure noise.
Prior work on quantum diffusion.The connection between quantum stochastic processes and
score-based diffusion has recently attracted attention from multiple groups. Liu et al. [4] introduced
measurement-based quantum diffusion models usingrandomizedobservable measurements, and
showed that a score matchingtraining objectivein the space of Pauli expectation valuesz∈R 4n
is equivalent to learning a unitary generator for trajectory reversal. Crucially, their score is
∇z logpt(z)—a gradient in the classical Pauli expectation value space—and their result concerns
the existence of a learning objective for an unknown score function. They do not measure a fixed
observable continuously, they do not work in density matrix space, and they do not analytically
identify what the score function is in closed form. Nasu, Tanaka, and Tsuchiya [5] demonstrated,
via semiclassical approximation of the Lindblad equation, a correspondence between the Petz map
and classical reverse diffusion at the ensemble level. Zhang et al. [6] showed that complete positivity
constrains score reversal in Gaussian bosonic dynamics. None of these works address the specific
García-Pintos et al. feedback protocol, and none analytically identify the score function in density
matrix space.
This paper.We address a question left open by all prior work:what is the score function of the
quantum trajectory path probability in density matrix space, and does it equal the García-Pintos
feedback Hamiltonian?We answer this affirmatively and analytically.
First, we prove—via Girsanov’s theorem applied to the measurement path probability, a Fréchet
derivative on the Banach space of trace-class operators, and a trajectory-level quantum analogue of
Anderson’s [2] reverse diffusion theorem—that the functional derivative oflogPF with respect to
the density matrixρ is exactlyrA/τ =Hmeas. This is an analytic identification in density matrix
space, not a learning objective in Pauli expectation value space. It answerswhyHmeas achieves
reversal: it is precisely the object that Anderson’s theorem requires to reverse the stochastic process,
namely the score function of the trajectory distribution. This provides an information-geometric
explanation not given in García-Pintos et al.
Second, we identify a continuous one-parameter family of path measures parametrized by the
feedback gainX (for feedback-active Hamiltonians with[H,A ]̸= 0). Classical diffusion models offer
only binary reversal: you run either the forward SDE or the reverse SDE. The quantum feedback
parameter X provides a real-valued continuum, from forward (X = 0) through time-symmetric
(X =−2) to more-backward-than-backward (X≪− 2). The parameter provides an experimentally
tunable continuum not present in classical diffusion models.
The identification extends to multi-qubit systems with independent measurement channels
(Theorem 4.1): the score function is a sum of local operators acting on each measured subsystem,
and the optimal feedback Hamiltonian is correspondingly local.
2

The practical implication.The analytic identification has a practical consequence.Hmeas =
rA/τ is the optimal feedback policy only under ideal conditions—perfect measurement efficiency
η = 1, zero feedback delay, exactly Gaussian noise. In any real experiment these conditions fail
and the policy degrades. Because we have provedHmeas is the score function, ML score estimation
methods—denoising score matching, sliced score matching, noise-conditional score networks—can
now be applied directly to the experimental measurement record as a replacement for the analytic
formula, without requiring quantum state tomography or knowledge of the underlying state. The
X-interpolation result additionally provides a new control parameter for quantum state preparation
with a tunable degree of arrow reversal.
The paper is structured as follows. Section 2 reviews both backgrounds. Section 3 states
and proves the main theorem. Section 4 extends to the multi-qubit case. Section 5 develops the
experimental implications. Section 6 discusses open problems and the precise relationship to prior
work.
2 Background
2.1 Continuously Monitored Quantum Systems and the Arrow of Time
We consider a quantum system described by a density matrixρ on a Hilbert spaceH, undergoing
continuous Gaussian measurement of an observableA satisfying A2 = 1 (e.g., Pauli matrices for
qubit systems). This assumption onA is not merely a mathematical convenience—it is precisely
what guarantees the backward process corresponds to a physically realizable measurement, as shown
in García-Pintos et al. [1].
At each infinitesimal timestepdt, a measurement outcomeris drawn from:
P(r|ρ) =
√
dt
2πτ exp
(
−(r−⟨A⟩) 2dt 2τ ) ,(1)
where⟨A⟩ = Tr(Aρ)is the expectation value of the observable andτ is the characteristic measurement
time governing measurement strength. The outcomer tracks the system:rdt =⟨A⟩dt +√τdW ,
wheredWis a Wiener increment.
Following the standard quantum trajectory formalism [7], the stochastic master equation (SME)
forρin Itô form is:
dρ=−i[H,ρ]dt+ 1 τ (AρA−ρ)dt
+ 1√τ (Aρ+ρA−2⟨A⟩ρ)dW.(2)
Three terms: deterministic Hamiltonian evolution, a Lindblad dissipator from measurement back-
action, and a stochastic term proportional to the measurement innovation.
The quantum arrow of time is quantified by the log-ratio of forward to backward process
probabilities over a trajectory of durationT:
lnR= ln PF ({r}) PB({r}) = 2 τ ∫ T 0 rt⟨A⟩tdt.(3)
When lnR> 0, the forward trajectory is more likely—the arrow points forward. WhenlnR< 0, the
backward trajectory is more likely—the arrow has reversed. The feedback protocol of García-Pintos
et al. [1] applies a total HamiltonianH +XH meas whereHmeas =rtA/τ, and shows that forX <−2
the average oflnRbecomes negative, reversing the arrow.
3

2.2 Score-Based Diffusion Models
A diffusion model operates on a probability distribution over data (e.g., natural images) by defining
a forward process that gradually corrupts data with noise. The canonical formulation uses the Itô
stochastic differential equation (SDE):
dx=f(x,t)dt+g(t)dW,(4)
where for simple variance-exploding diffusion,f = 0and g(t) =σ(t), so data is progressively noised
toward a standard Gaussian. The reverse-time SDE, due to Anderson [2] and developed in modern
score-based form by Song et al. [3], is:
dx=
[
f(x,t)−g 2(t)∇x logpt(x) ] dt+g(t)d ¯W,(5)
whered ¯Wis a reverse-time Wiener process and the critical new term is thescore function:
s(x,t) =∇ x logpt(x).(6)
The score function points from low-probability toward high-probability regions of state space.
Following it backwards transforms noise into structured data. The neural network in a diffusion
model (a score network) learns to estimates(x,t)from data via denoising score matching [8]:
θ∗ = arg min
θ
Et,x0,xt
[
∥sθ(xt,t)−∇ xt logp(xt|x0)∥2] .(7)
Once trained, the reverse SDE can be simulated to generate new samples. The entire machinery of
generation is the score function.
3 Main Result:H meas is the Score Function
Theorem 3.1(Quantum Score Function).Under continuous Gaussian measurement of an observ-
able A with A2 = 1 on a pure quantum state, the Fréchet derivative of the log-path-probability of the
quantum trajectory distribution with respect to the density matrixρis:
δlogP F
δρt
= rtA τ =H meas.(8)
Therefore,Hmeas is the score function of the quantum trajectory distribution. More precisely, it is
the path-measure score: the functional derivative oflog(dPF/dPW )with respect toρ. This differs
from the marginal-state score∇ρ logpt(ρ)appearing in Anderson’s classical theorem, though the two
coincide in the relevant gradient-flow sense established in Lemma 3.4.
The proof proceeds in four lemmas.
Lemma 3.2(RigorousPathProbabilityviaGirsanov’sTheorem).The log-path-probability logPF ({r})
can be derived via Girsanov’s theorem, and the stochastic component of the functional derivative
with respect to⟨A⟩t isr t/τ.
Proof.The measurement output processrt satisfies the Itô SDE:
drt =⟨A⟩ tdt+√τdW t.(9)
4

By the Girsanov theorem, the Radon–Nikodym derivative of the path measurePF with respect to
the reference Wiener measurePW is:
log dPF
dPW
= 1√τ ∫ T 0 ⟨A⟩tdWt− 1 2τ ∫ T 0 ⟨A⟩2 tdt,(10)
where the stochastic integral is in the Itô sense. The Novikov conditionE
[
exp
( 1
2τ
∫T
0⟨A⟩2 tdt )] <∞
is satisfied since⟨A⟩t∈ [−1, 1]for all t (as A is a Pauli-type operator with eigenvalues±1) andT is
finite.
Under the reference measurePW the measurement record is pure noise,drt =√τdB t with B a
PW-Wiener process, sodBt =rtdt/√τ. Identifying the Girsanov driftθt =⟨A⟩t/√τ, the stochastic
integral in (10) evaluates as
∫T
0 θtdBt = (1/τ)
∫T
0⟨A⟩trtdt. Therefore:
log dPF
dPW
= 1 τ ∫ T 0 rt⟨A⟩tdt− 1 2τ ∫ T 0 ⟨A⟩2 tdt.(11)
The expression is now a pathwise Riemann integral overdt with no stochastic integral remaining. The
term− 1 2τ ∫ ⟨A⟩2 tdt is deterministic given the state trajectory and contributes only to normalization.
Taking the functional derivative with respect to⟨A⟩t:
δlogP F
δ⟨A⟩t
= rt
τ −⟨A⟩t τ .(12)
The second term is the predictable (drift) component—it modifies the drift in the reverse SDE but
does not affect the stochastic reversal operator. The stochastic component, which generates the
feedback Hamiltonian, is:
δlogP F
δ⟨A⟩t
⏐⏐⏐⏐
stochastic
= rt
τ .(13)
Lemma 3.3(Fréchet Derivative on Trace-Class Operators).The functional derivativeδlogP F/δρt
is well-defined as a Fréchet derivative on the Banach space of trace-class operatorsT1(H), and equals
the operatorrtA/τ.
Proof. LetT1(H)denote the Banach space of trace-class operators with norm∥B∥1 = Tr(
√
B†B).
The set of density matricesD(H) ={ρ∈T 1(H) : ρ≥ 0,Tr (ρ) = 1} is a convex subset ofT1(H),
and its tangent space atρis:
TρD(H) ={δρ∈T 1(H) :δρ† =δρ,Tr(δρ) = 0}.(14)
Consider the functionalF:D (H)→R defined byF (ρ) = (rt/τ) Tr(Aρ)at a single timet. For any
δρ∈T ρD(H):
|F(ρ+δρ)−F(ρ)|= |rt| τ |Tr(A·δρ)|≤ |rt| τ ∥A∥∞∥δρ∥1,(15)
by the Hölder inequality for trace-class operators|Tr(AB)|≤∥A∥ ∞∥B∥1. SinceA2 = 1, we have
∥A∥∞ = 1. ThereforeFis bounded and linear inδρ, and the Fréchet derivative exists:
DF(ρ)[δρ] = rt
τ Tr(A·δρ) = Tr
(rtA
τ ·δρ
)
.(16)
By the Riesz representation theorem onT1(H), any bounded linear functional onT1(H)is represented
asTr(B·δρ)for a unique bounded operatorB. HereB=r tA/τ.
5

For the composite functionalG(ρ) = logPF (⟨A⟩(ρ))with ⟨A⟩(ρ) = Tr(Aρ), both the outer
function (∂logP F/∂⟨A⟩ =rt/τ from Lemma 3.2) and inner function (D⟨A⟩(ρ)[δρ] = Tr(A·δρ )) are
Fréchet differentiable. By the Fréchet chain rule [9]:
DG(ρ)[δρ] = rt
τ ·Tr(A·δρ) = Tr
(rtA
τ ·δρ
)
.(17)
The Fréchet derivative oflogPF with respect toρis the operatorr tA/τ=H meas.
Lemma 3.4(Kähler Structure—Symplectic Feedback, Riemannian Measurement).Letρ =|ψ⟩⟨ψ|
be a pure state on a Hilbert spaceH of dimensiond, identified with a point of the projective manifold
CPd−1 (for a single qubit,CP 1∼=S2, the Bloch sphere). EquipCPd−1 with its canonical Kähler
structure(g,ω,J ), whereg is the Fubini–Study metric andω the Fubini–Study Kähler form, with the
Ashtekar–Schilling normalization defined as follows. For parameter-space indicesµ,ν, the horizontal
tangent vectors are|φµ⟩ = (1−|ψ⟩⟨ψ| )∂µ|ψ⟩. On such vectors,g(|φµ⟩,|φν⟩) = 2 Re⟨φµ|φν⟩ and
ω(|φµ⟩,|φν⟩) = 2 Im⟨φµ|φν⟩. LetAbe Hermitian withA 2 =1, and letH meas =r tA/τ.
The score functionrtA/τ generates two complementary flows via the two halves of the Kähler
structure:
(a)Symplectic flow=feedback dynamics.Viewing F (ψ) :=⟨ψ|Hmeas|ψ⟩ as a Hamiltonian
function onCP d−1, the Hamiltonian vector fieldXF defined byω(XF,·) =dFgenerates:
d|ψ⟩
dt =−iH meas|ψ⟩, dρ dt =−i[H meas,ρ].(18)
(b)Riemannian gradient flow=measurement back-action.The Fubini–Study gradient
of the same functionFgenerates:
dρ
dt = rt τ (Aρ+ρA−2⟨A⟩ρ),(19)
which matches the stochastic back-action term of the SME(2)in the innovation form.
The two flows are respectively the symplectic (imaginary) and Riemannian (real) parts of the
quantum geometric tensorQµν = 1 2gQF µν +iFµν acting on the score function. Measurement is the
Riemannian gradient oflogPF; feedback is the symplectic gradient of the samelogPF.
Proof. Part A: Kähler structure onCPd−1.At the point[ ψ], the horizontal tangent space
is TψCPd−1 ={|φ⟩ ∈Cd :⟨ψ|φ⟩ = 0}. The complex structure acts as J|φ⟩ = i|φ⟩. Kähler
compatibility follows directly: for horizontal|φ1⟩,|φ 2⟩:
ω(|φ1⟩,J|φ 2⟩) = 2 Im⟨φ1|iφ2⟩
= 2 Im(i⟨φ1|φ2⟩)
= 2 Re⟨φ1|φ2⟩
=g(|φ 1⟩,|φ 2⟩),
confirming the Kähler identityω(X,JY ) =g(X,Y ). The quantum geometric tensor in standard
form is
Qµν =⟨∂ µψ|∂νψ⟩−⟨∂ µψ|ψ⟩⟨ψ|∂νψ⟩,
which is Hermitian. Its real part is (proportional to) the quantum Fisher information metric
(QFIM) gQF µν [10], i.e. the Riemannian pullback ofg; its imaginary part is (proportional to) the
Berry curvatureFµν, the pullback ofω. For a single observableA, Fµν = 0on the one-dimensional
6

parameter manifold by antisymmetry—this records the absence of geometric phase along the
parameter direction but does not implyω vanishes on CPd−1, which remains non-degenerate and
continues to drive Hamiltonian flows.
Part B: Symplectic flow reproduces the feedback dynamics.For horizontal|φ⟩, the
differential ofFis:
dF(|φ⟩) = 2 Re⟨φ|Hmeas|ψ⟩.
We seek horizontal|XF⟩ satisfying ω(XF,|φ⟩ ) = dF (|φ⟩)for all horizontal |φ⟩. The ansatz
|XF⟩ =−i(Hmeas−⟨H meas⟩)|ψ⟩ is horizontal since⟨ψ|XF⟩ = 0. Verification usingIm(iz) = Re(z)
and noting that⟨ψ|φ⟩= 0withH meas Hermitian:
2 Im⟨XF|φ⟩= 2 Im
(
i⟨(Hmeas−⟨H meas⟩)ψ|φ⟩
)
= 2 Re⟨(Hmeas−⟨H meas⟩)ψ|φ⟩
= 2 Re⟨ψ|Hmeas|φ⟩
= 2 Re⟨φ|Hmeas|ψ⟩=dF(|φ⟩).
Uniqueness follows from non-degeneracy of ω. The flow on |ψ⟩ is d|ψ⟩/dt = −i(Hmeas−
⟨Hmeas⟩)|ψ⟩; the scalar⟨Hmeas⟩ contributes only a global phase on the Hilbert sphere, killed by the
quotient toCP d−1, givingd|ψ⟩/dt=−iH meas|ψ⟩. Computingdρ/dt= (d|ψ⟩/dt)⟨ψ|+|ψ⟩(d⟨ψ|/dt)
and cancelling the scalar terms gives:
dρ
dt =−i[H meas, ρ].
Part C: Riemannian gradient flow reproduces the measurement back-action.The
Fubini–Study gradient ofF at|ψ⟩ is the horizontal projection of 1 2 times the gradient in the
ambient Hilbert space: gradgF = (Hmeas−⟨H meas⟩)|ψ⟩ (the horizontal component ofHmeas|ψ⟩).
The resulting flow onρis:
dρ
dt = (Hmeas−⟨H meas⟩)|ψ⟩⟨ψ|
+|ψ⟩⟨ψ|(H meas−⟨H meas⟩)
=H measρ+ρH meas−2⟨H meas⟩ρ.
SubstitutingH meas =r tA/τ:
dρ
dt
⏐⏐⏐⏐
Riem
= rt
τ (Aρ+ρA−2⟨A⟩ρ).(20)
The stochastic back-action term of the SME (2) is:
1√τ (Aρ+ρA−2⟨A⟩ρ)dW t.
Using the innovation formdWt = (rt−⟨A⟩t)dt/√τ, this becomes:
rt−⟨A⟩t
τ (Aρ+ρA−2⟨A⟩ρ)dt.
The⟨A⟩t/τ difference is a drift term absorbed into the Girsanov drift treated in Lemma 3.2; the
direction in density-matrix space is exactly the Fubini–Study gradient direction.
Part D: Complementary geometric picture.The two flows are summarized in Table 1.
7

The two flow directions are related by the complex structureJ—they are perpendicular in
the Kähler sense, and the Kähler identityω(·,J· ) = g(·,· )says that multiplication byi converts
one into the other. Reversing the arrow of time requires undoing both the unitary part of the
dynamics (symplectic) and the state-disturbance part (Riemannian). The feedback Hamiltonian
Hmeas =rtA/τ serves both roles simultaneously because both flows descend from the same score
function. This is the geometric content of the García-Pintos et al. protocol: a single object generates
both the unitary and the back-action components of the stochastic trajectory.
Table 1: Decomposition of the feedback Hamiltonian’s action on the pure-state manifoldCPd−1
into symplectic (feedback) and Riemannian (measurement) flows, corresponding to the imaginary
and real parts of the quantum geometric tensor.
Component Geometric structure Flow onρ
Feedback Symplecticω−i[H meas,ρ]
Measurement Riemanniang(r t/τ)(Aρ+ρA−2⟨A⟩ρ)
Caveats.The proof applies to pure states only—the pure state manifoldCPd−1 is Kähler, but the
mixed-state manifoldD(H)does not carry a globally compatible symplectic structure. Extension to
mixed states requires either purification on an enlarged Hilbert space or the KMS inner-product
framework discussed in Sec. 6(iv). For the multi-observable case (Theorem 4.1),Fµν need not vanish
and genuine geometric-phase contributions may arise—a direction not developed here.
Lemma 3.5(Quantum Anderson Theorem).Given the forward quantum trajectory measurePF,
the backward measurePB is defined by negating measurement outcomes, and the ratioln(PF/PB) =
(2/τ)
∫
rt⟨A⟩tdt. Under the leading-order linearization developed in the proof, setting the feedback
gain X =−2recovers PB. For feedback-active Hamiltonians with[H,A ]̸= 0, generalX generates a
one-parameter family of path measures with no classical analogue.
Proof. Existing literature.Belavkin’s quantum filtering theory [ 11] establishes the forward
quantum filter as the quantum Kushner–Stratonovich equation but does not derive a reverse filter.
Fagnola and Umanità [12] establish time-reversal for quantum Markov semigroups at the ensemble
level, not the trajectory level. We derive the trajectory-level result below.
The backward path measure.Define the backward process by negating the measurement
outcomes: rt→−r t. (This is equivalent to full time-reversalrt→−r T−t for the Girsanov density,
since the change of variables = T−t leaves
∫
⟨A⟩2dt invariant and negates ∫ r⟨A⟩dt, matching
plain negation.) Under this transformation, the measurement outputs of the backward process are
anticorrelated with the state (as the Kraus operator analysis in García-Pintos et al. [1] confirms for
A2 = 1). The Radon–Nikodym derivative ofPB with respect to Wiener measure is obtained by
substitutingr t→−r t in (10):
log dPB
dPW
=− 1 τ ∫ T 0 rt⟨A⟩tdt− 1 2τ ∫ T 0 ⟨A⟩2 tdt.(21)
The log-ratio is:
logdPF
dPB
= 2 τ ∫ T 0 rt⟨A⟩tdt= lnR,(22)
recovering the arrow quantifier exactly.
8

Recovery of PB at X = −2.Under feedback with parameter X, the measurement SDE
drt =⟨A⟩(X) t dt +√τdW t retains its form but⟨A⟩(X) t is evaluated on the feedback-modified state
trajectory. In the regime where the feedback-modified expectation may be linearized as⟨A⟩(X) t ≈
(1 +X)⟨A⟩(0) t —which we justify below and discuss in Sec. 6—the Girsanov calculation of Lemma 3.2
yields (to leading order in this linearization):
log dPX
dPW
= 1 +X τ ∫ T 0 rt⟨A⟩tdt− 1 2τ ∫ T 0 ⟨A⟩2 tdt.(23)
Regime of validity.The linearization ⟨A⟩(X) t ≈ (1 +X)⟨A⟩(0) t requires that the Hamiltonian
dynamics couple the feedback into⟨A⟩ approximately linearly over the trajectory durationT. For
A2 = 1, the commutator Tr(A[A,ρ ]) = 0implies that the feedback affects ⟨A⟩t only indirectly,
through[ H,A ]-mediated transverse dynamics. The linearization therefore holds (i) whenωT≪ 1
(short trajectories on the Rabi scale) and (ii) for moderate|X|, with corrections of order(ωT )2
and higher powers ofX. When[ H,A ] = 0, the feedback has no effect on⟨A⟩t and PX =PF for
allX—the one-parameter family is degenerate in this case and the present Lemma is vacuous.
AtX= 0:
log dP0
dPW
= log dPF
dPW
.
AtX=−2:
logdP−2
dPW
=− 1 τ ∫ rt⟨A⟩tdt− 1 2τ ∫ ⟨A⟩2 tdt
= log dPB
dPW
.
ThusP−2 =PB in the leading-order expansion of(23). Higher-order corrections inωT and in|X|,
arising from the nonlinear dependence of⟨A⟩(X) t on feedback-modified transverse dynamics, shift
the exact time-reversal point away fromX =−2for generic H. We discuss this explicitly in Sec. 6
and below.
Comparison with numerics.García-Pintos et al. [1] plot⟨lnRX⟩ versusX in their Fig. 2 for
ωτ = 8π, T =τ, A =σz, H∝σ x, and observe the zero crossing atX≈− 3rather than X =−2.
This is consistent with the regime-of-validity caveat above: atωτ = 8π the Hamiltonian completes
eight Rabi periods within one measurement time, placing the system far outside theωT≪ 1window
in which the(1 +X)linearization is accurate. Finding a closed-form expression for the reversal
pointX∗(H,A,τ,T)at finiteωτis an open problem we leave to future work.
Continuous interpolation.For generalX:
logdPX
dPB
= (X+ 2)· 1 τ ∫ T 0 rt⟨A⟩tdt.(24)
ForX∈ (−2, 0): PX interpolates betweenPB and PF. The process is partially forward, partially
backward.
ForX <−2: PX is more extreme thanPB—the trajectory is more anticorrelated than a pure
backward process.
In classical Anderson reversal, the only options are the forward SDE (score weight= 0) and
the reverse SDE (score weight= 1). There is no parameter that interpolates or extrapolates. The
9

quantum parameterX provides a continuous, experimentally tunable family of path measures
parametrized by a real number.
The reverse SME (leading order).Substituting the reverse Wiener processd ¯Wt =dWt−
2√τ⟨A⟩tdtinto the forward SME (2):
dρ=−i[H,ρ]dt+ 1 τ (AρA−ρ)dt
+ 1√τ (Aρ+ρA−2⟨A⟩ρ)◦d ¯W
+ 2 τ⟨A⟩(Aρ+ρA−2⟨A⟩ρ)dt.
The additional drift term(2/τ)⟨A⟩t(Aρ +ρA− 2⟨A⟩ρ)is not a Hamiltonian commutator: in the
A-eigenbasis it has nonzero diagonal entries with real coefficients, whereas any commutator−i[B,ρ ]
has vanishing diagonal and purely imaginary off-diagonal entries. The reverse SME at the state level
therefore acquires a non-Hamiltonian drift, paralleling the classical Anderson reverse SDE, whose
score-induced drift likewise modifies the SDE without being reducible to a Hamiltonian generator.
The identification ofHmeas as the generator of reversal established in this paper operates at the
path-measure level (Lemma 3.2 and Lemma 3.3 via the Girsanov density), not as a literal generator
of the reverse drift on the density-matrix manifold. A complete characterization of the reverse SME
at the state level is left to future work and noted in Sec. 6(ii).
Proof of Theorem 3.1.Combining Lemmas 3.2–3.5:
Lemma 3.2 establishes that the path probability has the correct form under Girsanov’s theorem,
with Stratonovich corrections affecting only the deterministic drift component. Lemma 3.3 establishes
that the Fréchet derivative oflogPF with respect toρ is the operatorHmeas =rtA/τ. Lemma 3.4
establishes that the natural gradient flow on the density matrix manifold generated by this score
function is−i[Hmeas,ρ ]—the feedback dynamics. Lemma 3.5 establishes that this score function,
when used in the quantum analogue of Anderson’s reverse SDE, recovers the backward processPB
at X =−2in the leading-order linearization of Eq.(23) and generates a continuous family of path
measures for generalX(for feedback-active Hamiltonians with[H,A]̸= 0).
Together, these lemmas establish thatHmeas = rtA/τ is the score function of the quantum
trajectory distribution in each of the three senses relevant for trajectory reversal: as a Fréchet
derivative, as a Riemannian gradient, and as the generator of path measure reversal.
4 Multi-Qubit Generalization
We now extend Theorem 3.1 tonqubits withksimultaneously measured observables.
Setup.Let {Aj}k j=1 be Hermitian observables on ann-qubit Hilbert space, each satisfyingA2 j = 1,
measured independently with characteristic times{τj}. The measurement outputs satisfy:
rjdt=⟨A j⟩dt+ √τjdWj,(25)
with{dW j}independent Wiener increments. The multi-qubit SME is:
dρ=−i[H,ρ]dt+
∑
j
1
τj
(AjρAj−ρ)dt
+
∑
j
1√τj (Ajρ+ρA j−2⟨Aj⟩ρ)dWj.(26)
10

Theorem 4.1(Multi-Qubit Score Function).Under independent Gaussian measurements of
observables{A j}, the multi-qubit score function is:
δlogP F
δρt
=
∑
j
rj(t)
τj
Aj =H multi meas.(27)
The multi-qubit feedback Hamiltonian is a sum of local terms.
Proof.Since measurement noises are independent, the joint path probability factorizes:
logPF ({r1,...,r k}) =
∑
j
1
τj
∫
rj(t)⟨Aj⟩tdt
+ (normalization).(28)
The Fréchet derivative with respect toρ onT1(C2n )follows by the same chain rule argument as
Lemma 3.3, applied to each term in the sum:
δlogP F
δρ =
∑
j
rj
τj
Aj.(29)
EachAj acts as a local operator on its respective qubit subsystem (tensored with identity on others).
The score function is therefore a sum of local operators, and the optimal feedback Hamiltonian
under independent local measurements is local.
5 Implications
The analytic solutionHmeas =rA/τ is optimal only under idealized conditions: pure states, perfect
measurement efficiencyη = 1, zero feedback delay, exactly Gaussian measurement noise. Real
experiments violate all of these. BecauseHmeas is the score function, ML score estimation provides
a replacement in all three regimes.
5.1 Capability 1: Imperfect Measurement Efficiency
In a real superconducting qubit lab, detectors do not catch every photon. At efficiencyη <1, only
a fractionη of the measurement information reaches the controller. The analyticHmeas =rA/τ
assumes η = 1; atη = 0.8the r you read is a corrupted signal, and the optimal corrective pulse
depends on the full conditional state given partial information—a quantity with no closed form in
general. The first-order correctionHη meas≈ηrA/τ is known but captures only the leading-order
degradation.
Because Hmeas is the score function, denoising score matching applies directly: collect measure-
ment records from the real imperfect detector, and train a networksθ(rt)to minimize:
θ∗ = arg min
θ
Er,ρ
[‖‖‖‖sθ(rt)− rt−⟨A⟩t τ ‖‖‖‖ 2] .(30)
The network learns the true score of the imperfect trajectory distribution from data, without
requiring knowledge ofη or the underlying quantum state. Sliced score matching [13] provides an
even more practical variant requiring no quantum state tomography:
θ∗ = arg min
θ
E
[
vT∇rsθ(rt)v+ 1 2∥sθ(rt)∥2
]
,(31)
for random projection directionsv, fully observable from the measurement record alone.
11

5.2 Capability 2: Feedback Delay
Real electronics introduce a gapδt between readingr and firing the corrective pulse. By the time
the pulse fires, the qubit has evolved further under both the HamiltonianH and the continued
measurement back-action. The analyticHmeas = rA/τ assumes zero delay; under delayδt the
optimal policy must predict the qubit’s current state from the history of past measurements
{rt−δt,rt−2δt,...}—a sequence prediction problem with no analytic solution.
Because the score function can be estimated from historical data, a recurrent score network
trained on measurement sequences handles delay naturally. The network learns to predict the
current optimal pulse from the measurement history, without any closed-form model of the delay
dynamics. This converts an analytically intractable optimal control problem into a sequence-learning
problem.
5.3 Capability 3: Non-Gaussian Measurement Noise
The entire derivation ofHmeas assumes exactly Gaussian measurement noise. Real superconducting
qubit detectors have amplifier noise, cross-talk, and non-linearities that make the actual measurement
distribution non-Gaussian. Without Gaussian noise the path probability does not have the clean
quadratic form of(11), and no closed-form score exists at all—the analytic approach breaks down
rather than degrading gracefully.
Score estimation from samples requires no knowledge of the analytic form of the distribution. A
score network trained on experimental data from the real non-Gaussian system learns whatever
the true score is. All existing convergence guarantees for score matching [8, 13] apply regardless of
whether the underlying distribution is Gaussian, since they are derived from the structure of the
loss function, not the distribution family.
6 Discussion and Open Problems
What is proved.Theorem 3.1 establishes the core claim—Hmeas is the score function—rigorously
within clearly stated assumptions: pure states, single measured observableA with A2 = 1, perfect
measurement efficiency, independent measurement channels. Theorem 4.1 extends this to the
multi-qubit independent measurement case.
What remains open.
(i) Full QFIM metric agreement.Lemma 3.4 establishes that the measurement-induced metric
(QFIM) governs the Riemannian gradient flow—the measurement back-action—while the symplectic
form governs the feedback dynamics. Full metric agreement on the entire density matrix manifold
is not needed for the main result: the Kähler geometry argument applies to pure states onCPd−1,
and the paper’s assumptions are restricted to pure states throughout.
(ii) Exact reverse generator beyond leading order.The reverse SME in Lemma 3.5 is
established to leading order in the weak-measurement limit. The next-order correction, arising from
the noise component ofrt, is expected to modify the reverse drift but not the identification ofHmeas
as the stochastic reversal operator. A complete proof would carry all Itô correction terms explicitly.
In particular, the(1 +X)linearization of ⟨A⟩(X) t underlying Eq.(23) becomes degenerate when
[H,A ] = 0(the feedback has no effect on⟨A⟩t, soPX =PF for allX); deriving the exact reversal
pointX∗(H,A,τ,T)at finiteωτremains open.
12

(iii) Correlated measurements.Theorem 4.1 assumes independent measurement channels.
For measurements sharing a probe (e.g., a single microwave cavity coupling to multiple qubits),
the noise processesdWj are correlated, the path probability does not factorize, and the score
function acquires off-diagonal terms coupling different observables. Whether the optimal feedback
Hamiltonian remains local in this regime is an open question.
(iv) Mixed states.The proofs assume pure state evolution throughout. For mixed states arising
from partial measurement efficiency or environmental decoherence, the symmetric logarithmic
derivative (SLD) in Lemma 3.4 is not unique (there is a family of SLDs related by the kernel of the
state), and the connection between the Fréchet derivative and the commutator dynamics requires
additional geometric machinery. The correct framework is likely the KMS (Kubo–Martin–Schwinger)
inner product on the space of observables, which generalizes the QFIM to mixed states.
Relationship to prior work in detail.Liu et al. [4] is related but structurally distinct. They
work withrandomizedobservables drawn from a distribution independent of the state, and their
score function is∇z logpt(z)—a gradient in the classical4n-dimensional Pauli expectation value
spacez∈R 4n . Their core result is that alearning objective—minimizing infidelity to train a unitary
generator—is equivalent to a score matching loss inz-space. They do not analytically identify what
the score is; they propose to learn it. By contrast, we work with continuous measurement of a
fixedobservableA, and prove analytically that the functional derivative of the logpath probability
with respect to the density matrixρ equals rA/τ —an explicit closed-form identification in density
matrix space. These are complementary results in different physical settings with genuinely different
mathematical objects called “score.”
Nasu et al. [5] work at the ensemble level via Wigner function semiclassical approximation
of the Lindblad equation, connecting the Petz map to Bayes’ rule reverse diffusion. Our work is
complementary: we work at the individual trajectory level, require no semiclassical approximation,
and apply to the discrete-variable qubit setting rather than the continuous-variable bosonic setting.
Zhang et al. [6] establish that complete positivity constrains score reversal in Gaussian bosonic
dynamics. This does not directly apply to the qubit trajectory setting, but raises the open question
of whether the commutator-based feedback dynamics derived here also faces complete positivity
constraints at higher order.
6.1 Outlook
Beyondtheimperfect-measurementapplicationsdiscussedinSection5, thecontinuous X-parametrized
family of path measures identified in Lemma 3.5 is not present in classical diffusion models, where
reversal is binary. Whether this structure translates into useful capabilities for generative modeling—
for example, annealed samplers or interpolation schedules for consistency models—is a natural
follow-up question we leave for future work.
Acknowledgments
The authors used AI tools for editorial feedback and to stress-test proof arguments. All mathematical
content and results are the authors’ own.
13

References
[1] L. P. García-Pintos, Y.-K. Liu, and A. V. Gorshkov, Reshaping the quantum arrow of time,
Phys. Rev. X16, 011028 (2026). doi:10.1103/l18s-9vmh.
[2] B. D. O. Anderson, Reverse-time diffusion equation models,Stoch. Process. Appl.12, 313
(1982). doi:10.1016/0304-4149(82)90051-5.
[3] Y. Song, J. Sohl-Dickstein, D. P. Kingma, A. Kumar, S. Ermon, and B. Poole, Score-based
generative modeling through stochastic differential equations, inInternational Conference on
Learning Representations(ICLR, 2021); arXiv:2011.13456.
[4] X. Liu, J. Zhuang, W. Hou, and Y.-Z. You, Measurement-based quantum diffusion models,
arXiv:2508.08799 [quant-ph] (2025).
[5] R. Nasu, G. Tanaka, and A. Tsuchiya, Quantum reversibility meets classical reverse diffusion,
arXiv:2510.18512 [quant-ph] (2025).
[6] B. Zhang, P. Xu, X. Chen, and Q. Zhuang, Quantum diffusion models: Score reversal is not
free in Gaussian dynamics, arXiv:2603.06488 [quant-ph] (2026).
[7] H. M. Wiseman and G. J. Milburn,Quantum Measurement and Control(Cambridge University
Press, 2009). doi:10.1017/CBO9780511813948.
[8] P. Vincent, A connection between score matching and denoising autoencoders,Neural Comput.
23, 1661 (2011). doi:10.1162/NECO_a_00142.
[9] H. Cartan,Differential Calculus(Houghton Mifflin, 1971).
[10] S. Amari and H. Nagaoka,Methods of Information Geometry(AMS/Oxford University Press,
2000). doi:10.1090/mmono/191.
[11] V. P. Belavkin, Quantum stochastic calculus and quantum nonlinear filtering,J. Multivar.
Anal.42, 171 (1992). doi:10.1016/0047-259X(92)90042-E.
[12] F. Fagnola and V. Umanità, Generators of detailed balance quantum Markov semigroups,Infin.
Dimens. Anal. Quantum Probab. Relat. Top.10, 335 (2010). doi:10.1142/S0219025710004152.
[13] Y. Song, A. Garg, J. Shi, and S. Ermon, Sliced score matching: A scalable approach to density
and score estimation, inUncertainty in Artificial Intelligence(UAI, 2020); arXiv:1905.07088.
14
