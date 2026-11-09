---
title: Transition Path Sampling Using Koopman Operators and Exit-Time Optimal Control
url: https://arxiv.org/abs/2610.10054
category: ai-marketing
subcategory: measurement
date: 2026-10
venue: ''
authors:
- Boya Hou
- Shane Wang
- Siddharth Ambekar
- Maxim Raginsky
- Olgica Milenkovic
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.10054
pages: 30
chars: 75471
fetched_at: '2026-11-08T13:26:01+00:00'
kb_version: 1
---

# Transition Path Sampling Using Koopman Operators and Exit-Time Optimal Control

Transition Path Sampling Using Koopman Operators and
Exit-Time Optimal Control
Boya Hou ∗ Shane Wang∗ Siddharth Ambekar Maxim Raginsky
Olgica Milenkovic
University of Illinois Urbana-Champaign
October 8, 2026
Abstract
Sampling transitions between metastable states is a central problem in dynamical systems
theory and molecular dynamics in particular. A key challenge is the existence of high free-energy
barriers that separate the states, making transitions extremely rare. Recent machine learning-
based methods cast transition path sampling (TPS) as an optimal stochastic control (OSC)
problem over a fixed time horizon, and parameterize the drift bias via a neural network trained
by simulation-in-the-loop, requiring repeated biased rollouts. To address computational and
performance guarantee issues of these models, we propose a new approach for the problem based
on Koopman operators. Because Koopman operators are linear, their leading eigenfunctions
reveal the metastable sets and provide an estimate of the committor function with no transition
path information required. Furthermore, we formulate TPS as an OSC problem up to an
exit time. Our time horizon is the first hitting time of the target set, and our running cost
penalizes time spent in nonreactive regions by encoding the estimated committor function. We
derive the optimal controller in closed form and approximate it in a reproducing kernel Hilbert
space (RKHS). This reduces the problem of constructing the optimal controller to solving a
single equality-constrained quadratic program, whose solution can be characterized by a linear
Karush-Kuhn-Tucker (KKT) system. On the two-channel double well and alanine dipeptide,
our controller increases the fraction of trajectories reaching the target from0%to99.8%within
1,000steps, and from0%to93%within1ps, respectively.
1 Introduction
Sampling transitions between metastable sets is a fundamental problem in dynamical systems theory
and molecular dynamics, underlying the study of conformational changes of proteins, folding, and
drug discovery (Grubmüller, 1995; Voter, 1997). A typical challenge is that the states of interest are
separated by high free-energy barriers: the overwhelming majority of simulated trajectories remain
within a single metastable set, while trajectories that cross from one metastable set to another
without returning (reactive paths) are rare under native dynamics (Vanden-Eijnden et al., 2006).
Classical transition path sampling (TPS) performs Markov chain Monte Carlo in the path space,
generating new trajectories from existing ones (Dellago et al., 1998; Bolhuis et al., 2002; Bolhuis
and Swenson, 2021). However, they require an initial reactive path connecting the two metastable
∗Co-first authors.
1
arXiv:2610.10054v1  [eess.SY]  7 Oct 2026

sets, which can be difficult to generate. In physical chemistry and molecular dynamics, rare event
sampling is typically accelerated by adding bias potentials to the energy landscape (Voter, 1997;
Grubmüller, 1995; Laio and Parrinello, 2002). These are usually defined over a small number of
hand-crafted collective variables. Modern machine learning-based samplers such as PIPS (Holdijk
et al., 2023) and TPS-DPS (Seong et al., 2025) cast transition path sampling as optimal stochastic
control or path-measure matching problems over a fixed time horizon, and parameterize the drift
biaswithaneuralnetworktrainedbysimulation-in-the-loop, whichcallsforrepeatedbiasedrollouts.
Learning a bias force through simulation, however, can be challenging. For example, early in the
training, few rollouts reach the target, and hence the training signal is highly sparse. Furthermore,
a fixed-horizon formulation requires a properly chosen horizon, and the transition time is a random
variable dependent on the path itself. Partial mitigation of these drawbacks is possible using replay
buffers and annealing, and truncating the paths at a time that maximizes specific kernel values.
To resolve the above issues, we propose anoperator-basedframework for efficient TPS that uses
Koopman spectral analysisand optimal stochastic control (OSC) up to anexit time, in which the
stopping rule is the first hitting time of the target set. Specifically, we cast TPS as sampling from a
Gibbs measure on the path space problem, following the information-theoretic frameworks of Mitter
and Newton (2003) and Raginsky (2026). By the Gibbs variational principle, the Gibbs measure
associated with a reference path measure and an energy on a path is, under certain conditions, the
unique minimizer of the free energy. Mitter and Newton (2003) used this insight to pose nonlinear
filtering as an optimal control problem. To adapt the described sampling method to TPS, we take
the reference to be the unbiased path measure of the original dynamics, and the energy to penalize
the time spent in nonreactive regions via the committor function. Since we assume the time horizon
to be the first time a path reaches the target set, we operate with exit rather than fixed times. We
prove that the resulting Gibbs measure is the law of a controlled diffusion process and prove that
the optimal controller minimizes the free energy overallpath measures on the stoppedσ-algebra
rather than only those generated by admissible controls. Furthermore, the optimal controller admits
a closed-form solution and can be computed without simulations in the loop.
It is worth pointing out that the proposed approach differs from the recent work of Du et al.
(2026), which investigates a related hitting-time problem for committor estimation, treating the
committor as a value function and training it with neural networks that require repeated simulation
of controlled dynamics during training. As previously emphasized, we instead follow anoperator-
theoreticapproach in which the spectrum of the Koopman generator of the model reveals the
metastable sets, and where the committor function is constructed from Koopman eigenfunctions.
These can be estimated from a fixed dataset without requiring any trajectory to transition between
the metastable sets. The Koopman generator plays a central role within this framework: its leading
eigenfunctions reveal the metastable sets and are incorporated into the committor function, which
in turn defines the running cost of the OSC. The optimal controller of the OSC can be solved via a
boundary value problem wrt the operator. This pipeline comes with several practical advantages.
First, it requires no transition paths, as Koopman eigenfunctions can be computed without crossings
between metastable sets via a generalized eigenproblem. Second, the controller admits a closed-form
solution, and thus is obtained without network training but through solutions of convex quadratic
programs. The approach is also interpretable, as the controller is built from physically meaningful
quantities that characterize the mechanism of the transition, namely the metastable sets and the
committor function. Furthermore, the sampled paths can be reweighted to recover the statistics of
the original dynamics.
Our contributions are multifold: (1) We formulate TPS as an OSC up to an exit time. We show
in Theorem 1 that the optimal controller admits a closed-form solution,u∗ =∇logρ, and that
its path measure minimizes the free energy overallpath measures, not only those generated by
2

admissible controls; (2) We construct this controller by approximatingρin a Reproducing Kernel
Hilbert Space (RKHS). The problem then reduces to solving a convex quadratic program with linear
equality constraints, whose solution can be characterized by a single linear Karush–Kuhn–Tucker
(KKT) system rather than repeated rollouts; (3) In TPS, the source and target metastable sets are
often predefined through collective variables. Following Koopman-based approaches that identify
metastable sets (Mardt et al., 2018; Pérez-Hernández et al., 2013), we construct these sets without
collective variables by using the leading eigenfunctions of the Koopman generator, which capture the
slow inter-basin modes. From the same eigenfunctions, we construct a committor function, which
defines the running cost of the OSC; (4) We generate transition paths by simulating the controlled
diffusion process until it first enters the target sets, and show the resulting paths can be reweighted
via Lemma 4 to recover the statistics of the original dynamics up to the transition; (5) We evaluate
our method on both synthetic and real-world datasets.
The paper is organized as follows. In Section 2, we introduce the diffusion process of interest
and the corresponding Koopman generator. In Section 3, we develop the OSC up to an exit time in
generalform. There, wealsoderiveaclosedformoftheoptimalcontroller. Theresultsofthissection
can be specialized for efficient TPS. Section 4 constructs metastable sets and the committor function
from Koopman eigenfunctions, and approximates the optimal controller in an RKHS. We generate
transition paths by simulating the optimally controlled SDE, and report numerical experiments in
Section 5. Due to space limitations, proofs and extra experiments are deferred to the Appendix G.4.
2 Preliminaries: Itô Diffusion and the Koopman Generator
LetX⊆R n denote the state space and consider the Itô diffusion process
dXt =b(X t)dt+σ(X t)dW t, X 0 =x,(1)
whereW t is anm-dimensional Brownian motion process, andb:X→R n andσ:X→R n×m are the
drift and diffusion functions, respectively Karatzas and Shreve (2014); Oksendal (2000). A model
of the form (1) used in MD simulations is theLangevin dynamics,wherebandσare specified by a
potential energyU, frictionγ, and bath temperatureTemp. In the overdamped case, the state is the
atomic configuration, and the drift and diffusion coefficients are specialized asb(x) =−1 γm ∇U(x),
σ(x) =σ 0I, withσ 0 =
q
2kBTemp
γm . In the underdamped case, the state additionally carries the
momenta, and friction and noise act only on the momentum component. In either case, the process
is metastable wheneverUhas multiple deep minima (wells) separated by barriers large relative to
kBTemp, and a trajectory spends most of its time in a single well.
Next, letT:= [0,∞)and fix the spaceΩ =C(T;X)of continuous paths mappingTtoX. Also,
letX t(ω) =ω(t)denote the evaluation of a pathω∈Ωat timet∈T. LetF=σ(X t :t∈T)be
the canonicalσ-algebra, and let(F t)t∈T withF t =σ(X s :s≤t)be the filtration, both generated
by the process(X t)t∈T. Forx∈X, letP x be the law on(Ω,F)of the solution of (1) started at
x, provided it is well posed, for example, under Assumptions 1 and 2 in Section 3. UnderPx, the
canonical processX t(ω) =ω(t)solves (1). Define the family of Koopman operators{Kt}t∈T as
Ktφ(x) =E[φ(X t)|X0 =x],(2)
per (Koopman and von Neumann, 1932; Lasota and Mackey, 2013). Although (1) is nonlinear,Kt
fort∈Tarelinearoperators and{K t}t∈T defines a semigroupK t+s =K t ◦ Ks. The associated
3

infinitesimal Koopman generatorLis alinearsecond-order differential operator given by
Lφ(x) =b(x)· ∇φ(x) +1 2 nX i=1 nX j=1 aij(x)∂ ijφ(x),(3)
forφ∈C 2(X), where the indicesi, j= 1,· · ·, nrange over the coordinates ofx= (x1, . . . , xn)∈X,
∂ij denotes the second partial derivative with respect toxi andx j,a ij is the(i, j)entry of the
diffusion matrixa(x) :=σ(x)σ(x) ⊤, andbis the drift term in (1). The spectrum ofLcan be utilized
to characterize the global structure of the dynamics (Mezić, 2005; Mardt et al., 2018; Kostic et al.,
2022). Let(λ, ψ)be an eigenpair ofL, i.e.,Lψ=λψ. ThenK tψ=e λtψ, i.e.,E x[ψ(Xt)] =e λtψ(x).
The constant functionψ0 ≡1is always an eigenfunction withλ 0 = 0.
The Koopman operator and its spectrum can be approximately computed from data via numer-
ical methods such as dynamic mode decomposition (DMD) (Schmid, 2010; Rowley et al., 2009) and
extended dynamic mode decomposition (EDMD) (Williams et al., 2015), as well as nonparametric
variants based on RKHS known as kernel EDMD (Williams et al., 2014; Kostic et al., 2022; Klus
et al., 2020; Hou et al., 2023). We provide a brief introduction to RKHS in Appendix A. Following
Kostic et al. (2022); Hou et al. (2023), we approximate the leading eigenpairs(λk, ψk)ofLfrom
samples{x i}N i=1 ⊂X. Sincebandaare known,Lcan be applied directly to the kernel via (3). This
yields a generalized eigenproblem in terms of Gram matrices; see, e.g., (Hou et al., 2023, Appendix
M) for details.
A trajectory of (1) that crosses from one metastable set to another without returning to its
origin is a (reactive) transition path (Vanden-Eijnden et al., 2006). For two disjoint setsAi andA j,
letτ Ak be the first time the system entersAk fork=i, j. The committor functionq (i,j)(x)for the
transition fromx∈A i toA j is defined asq(x) =P

τAj < τAi |x 0 =x

(Vanden-Eijnden et al.,
2006; Metzner et al., 2009; Hoffmann et al., 2021). Along a transient path,q(i,j)(xt)is close to0
nearA i and close to1nearA j, whereas a path that lingers inAi hasq (i,j)(xt)≈0most of the
time. When the metastable sets are clear from context, we writeqas a shorthand forq(i,j). Next,
letD q :=X\(A i ∪A j). The committor functionqsatisfies the boundary value problem
Lq= 0inD q, q| ∂Ai = 0, q| ∂Aj = 1,(4)
whereLis the Koopman generator, and we extendedqbyq≡0onA i andq≡1onA j. We defer
the proof of this identity to the Appendix C.
The above concepts lead to our pipeline for TPS: the leading eigenfunctions of the Koopman
generatorLidentify the metastable sets and provide the spectral term of the committor function;
the committor function then defines the running cost of the OSC presented in the next section,
whose optimal controller can be approximated via a boundary value problem inL.
3 Transition Path Sampling via OSC up to an Exit Time
3.1 The Sampling Problem
Consider the diffusion process governed by the Itô SDE (1). To facilitate our analysis of the outlined
sampling approach, we make the assumption:
Assumption 1.b(x)andσ(x)are bounded and Lipschitz onX.
Under Assumption 1, the SDE (1) has a unique strong solution. LetPx be the path measure
started atx. LetD⊂Xbe open, andτ D := inf{t≥0 :X t /∈D}be the exit time. SinceDis
4

open,τ D is the hitting time of the closed setX\Dand is therefore an(F t)-stopping time. We
observe paths until they reach the target set (equivalently, exit the setD), and we work on the
stoppedσ-algebraF τD defined byF τD :=

A∈ F:A∩ {τD ≤t} ∈ Ft for allt≥0

. ThenX τD is
FτD-measurable.
Forx∈ ¯Dand each pathχunderP x, define the Hamiltonian as
H(χ) =
Z τD
0
f(X t)dt+ Φ(X τD ),(5)
wheref: ¯D→[0,∞)andΦ :∂D→[0,∞)are measurable, andH(χ) := +∞on{τ D =∞}. Here,
f≥0is the running cost andΦis the terminal cost. Since paths are continuous andDis open,
XτD ∈∂Don{τ D <∞}. Hence,His a well-definedF τD-measurable function.
For the purpose of efficient sampling, among all path measures on(Ω,FτD ), we seek the one
that minimizes the free energy
F( ˜P) := ˜E  H(χ)  +D KL  ˜P∥P x , ˜P∈ P(Ω,FτD ),(6)
where ˜Edenotes the expectation w.r.t. ˜P, andP(Ω,F τD )denotes the set of all probability measures
on(Ω,F τD ). Here, the first term favors paths with low energy, while the second keeps˜Pclose to the
original dynamics. We next make use of the Gibbs variational principle onFτD, which is adapted
from (Mitter and Newton, 2003, Proposition 2.1).
Proposition 1.LetHbe anF τD-measurable function, and supposeZ:=E x

e−H  >0. Then the
probability measureP ∗,x on(Ω,F τD )defined by
dP ∗,x
dP x

FτD
= e−H(χ)
Z (7)
is the unique minimizer of the free energy(6)over the set of all probability measures on(Ω,FτD ),
andmin ˜P F( ˜P) =F(P ∗,x) =−logZ.
It will be useful to keep in mind the following motivating example.
Example 1(TPS).LetA i, Aj ⊂Xbe disjoint closed source and target sets, and letD:=X\A j.
ThenA i ⊂D, and thus a trajectory initialized within the source set starts in the interior ofD. For
such a trajectory, the exit time ofDis the first hitting time ofAj, soτ D is the transition time of
interest. Letq(x) :=P x(τAj < τAi)be the committor function. Define the running and terminal
cost
fβ(x) :=β

1−q (i,j)(x)  ,Φ≡0on∂A j,(8)
withβ >0. Then,H=βH 0, whereH 0 =
R τD
0 (1−q (i,j)(Xt))dtis the time spent in nonreactive
regions before reaching the target. Here, the parameterβcontrols the trade-off between speed and
fidelity. Asβincreases, we increasingly prefer faster paths at the cost of deviating more from the
original dynamics. In Appendix F we show how to undo this dynamics distortion via reweighting.
The sampling problem of interest is to generate paths fromP∗,x. Proposition 1 identifies the
target measureP ∗,x but does not provide a way to sample from it. We therefore phrase the sampling
problem as a control problem where we add a control drift to the reference process (1) so that the
law of the controlled diffusion equalsP∗,x onF τD. We call a controlu: ¯D→R n admissibleifuis
5

Lipschitz continuous on ¯Dand useUto denote the set of all admissible controls. Au∈ Uenters
the drift througha(x)u(x), resulting in the controlled process
d ˜Xt =  b( ˜Xt) +a( ˜Xt)u( ˜Xt)  dt+σ( ˜Xt)d ˜Wt,(9)
where˜τD := inf{t≥0 : ˜Xt /∈D}. As we show in Theorem 1 (ii), restricting the focus to a Lipschitz
continuous controller does not weaken the result, since we can show that the path measure of the
optimal admissible controller is optimal overallprobability measures on(Ω,FτD ).
As the time-horizon is the first time the process exitsD, the exit timeτD is itself a random
variable. We first establish that it has a finite mean. We make the following Assumptions
Assumption 2.There existsc >0such thatz ⊤a(x)z≥c|z| 2 for allx∈X, z∈R n.
Assumption 3.D⊂Xis open and bounded withC 2,α boundary∂Dfor someα∈(0,1).
These assumptions are standard for exit-time problems for controlled diffusions (Fleming, 1977).
They ensure a unique solution of the associated elliptic boundary value problem inL. They hold, for
example, for overdamped Langevin dynamics with a smooth potential, including the double-well,
four-well, and Müller–Brown systems studied in Section 5 and Appendix G.4. The proof of the
following lemma is presented in Appendix B.1:
Lemma 1.Let Assumptions 1–3 hold. Then, the SDE(1)starting fromx∈Dhas a pathwise
unique strong solution, and its exit timeτD satisfiesE x[τD]<∞. Consequently,τ D <∞a.s.
3.2 A Candidate Optimal Controller
We now seek a controlled diffusion of the form (9) whose path measure equalsP∗,x. For this purpose,
we also require a regularity condition,
Assumption 4.The running costf∈C 0,α( ¯D)withf≥0, andΦ :∂D→[0,∞)such that
g:=e −Φ ∈C 2,α(∂D).
Define
ρ(x) :=E x

exp

−
Z τD
0
f(X t)dt−Φ(X τD )

.(10)
Here, we integrate time from0to an exit timeτD. Under Assumption 3,fis bounded on ¯D, andΦ
is bounded on∂Dsincegis continuous and positive on the compact set∂D. By Lemma 1,τD <∞
a.s. underP x, hence (10) is well-defined, andρ(x)∈(0,1].
We next show thatρsolves a boundary value problem via elliptic existence theory (Ladyzhen-
skaya and Uraltseva, 1968, Ch. III). We consider the following elliptic boundary value problem,
whereLis the (Koopman) generator:
Lw−f w= 0inD, w| ∂D =e −Φ.(11)
Since∂D∈C 2,α by Assumption 2 andg=e −Φ ∈C 2,α(∂D)by Assumption 3, applying (Ladyzhen-
skaya and Uraltseva, 1968, Ch. III, Theorem 1.1, 1.2) gives a unique solutionw∈C2,α( ¯D)to the
problem (11). The proof of the following lemma is included in the Appendix B.3.
Lemma 2.Let Assumptions 1–4 hold and letw∈C 2,α( ¯D)be the unique solution of the prob-
lem(11). Then,wcoincides on ¯Dwithρdefined in(10). Moreover,ρ >0on ¯D.
6

Our sampling/free energy minimization problem can now be cast as an optimal control problem.
In the fixed-horizon setting, the relative entropy of the controlled law with respect to the reference
law equals the expected control effort by Girsanov’s theorem, so the free energy (6) of the controlled
law is an optimal control cost (Raginsky, 2026, eq. (4.5)). By contrast, here we have to consider
the optimal stochastic control problem up to an exit time,
min
u∈U
J(u, x) :=˜Ex
Z ˜τD
0

f( ˜Xt) + 1 2 u( ˜Xt)⊤a( ˜Xt)u( ˜Xt)  dt+ Φ( ˜X˜τD )  ,
subject to (9), ˜X0 =x∈D.
(12)
We denote its value function asv(x) := inf u∈U J(u, x), forx∈ ¯D, withv| ∂D = Φ, since˜τD = 0
when ˜X0 ∈∂D. Consider the candidate value functionv:=−logρ(this is the logarithmic, or
Cole–Hopf, transform ofρ, (Fleming, 1977)). Since ¯Dis compact by Assumption 2 andρ∈C( ¯D)
withρ >0on ¯Das established in Lemma 2, the extreme value theorem givesm:= min ¯D ρ >0
andM:= max ¯D ρ <∞, soρ( ¯D)⊆[m, M]⊂(0,∞). Sinceρ∈C 2,α( ¯D), and−logis smooth on
[m, M], the chain rule givesv=−log◦ρ∈C 2,α( ¯D), and hence∇vis bounded on ¯D. Additionally,
sinceρ

∂D =g=e −Φ, the boundary condition ofvisv

 ∂D = Φ. We have the following lemma
whose proof is presented in Appendix B.4.
Lemma 3.The functionvsatisfies the Hamilton-Jacobi-Bellman (HJB) equation of the OSC prob-
lem(12)up to an exit time, i.e.,
Lv(x) +f(x) = 1 2 ∇v(x)⊤a(x)∇v(x)inD, v

 ∂D = Φ.(13)
We hence have a candidate for the optimal controller of (12) given by
u∗(x) =−∇v(x) =∇logρ(x) =∇ρ(x)/ρ(x).(14)
Theorem 1 below establishes that its minimal value equalsminF=−logZand that its optimally
controlled law isP ∗,x.
3.3 Verification Theorem of OSC up to an Exit Time
Let ˜P ∗,x be the law of the controlled process (9) underu ∗, starting atx. In the remainder of
the section, we establish thatu∗ in (14) is the optimal controller. Moreover, using a variational
characterization of the optimally controlled path measure, we show that˜P ∗,x minimizes the free
energy (6) over all path measures on(Ω,FτD ). We begin by presenting an explicit formula for the
Radon-Nikodym density of ˜P ∗,x relative toP x on(Ω,F τD ). To that end, we invoke Girsanov’s
formula. In the classic fixed time-horizon case, one needs a suitable regularity condition, such as
Novikov’s condition (Oksendal, 2000, Theorem 8.6.3). By contrast, in the exit time setting, such
a condition might not hold as it requires an exponential moment bound, which is hard to verify for
metastable systems. To address this challenge, the proof presented in Appendix B.6 only requires
τD <∞a.s. guaranteed by Lemma 1.
Lemma 4.Letu ∗ =−∇vbe as in(14), and let ˜Xt be a solution to the controlled SDE(9)with
u=u ∗, initiated at ˜X0 =x, and under a probability measure˜P ∗,x on(Ω,F τD ). Then, we have
d ˜P ∗,x
dP x

FτD
= e−H(χ)
ρ(x) ,E x
"
e−H(χ)
ρ(x)
#
= 1.(15)
7

We now present the verification theorem the proof of which can be found in Appendix B.7.
Theorem 1.Let Assumptions 1–4 hold, and letu ∗ be the controller in(14). Then,
(i)[Optimality]v(x) =J(u ∗, x) = minu J(u, x)for allx∈D.
(ii)[Variational inequality] For every probability measure˜Pon(Ω,F τD ),
J(u ∗, x)≤D KL( ˜P∥P x) + ˜Ex[H(χ)],(16)
with equality if and only ifd˜P /dPx =e −H(χ) /ρ(x)onF τD; equivalently, if and only if˜P= ˜P ∗,x,corresponding to the law of the optimally-controlled process restricted toFτD.
Part (i) of the above theorem states that the minimal control cost isminu∈U J(u, x) =v(x) =
−logρ(x), and by Part (ii), that the free energy (6) satisfiesF( ˜P)≥v(x)foreveryprobability
measure on(Ω,F τD ), with equality precisely for ˜P= ˜P ∗,x. Hence, the two minimal values of (6)
and (12) coincide, and the optimal path measure that minimizes the free energy is exactly the
one generated by the optimal controller. In the proof of Part (i) of Theorem 1, we also show
that the minimizer is unique in the following sense:J(u, x) =v(x)for someu∈ Uif and only if
u( ˜Xt) =u ∗( ˜Xt)for Lebesgue-a.e.t∈[0,˜τ D], ˜P u,x-a.s.
By the definition in (10),ρ(x)is large where the trajectory of the original dynamics (1) tends
to exit quickly and small where it dwells in nonreactive regions. The optimal controller in (14)
therefore points toward states from which a trajectory is more likely to exit. The normalization by
ρ >0in (14) provides a stronger push towards whereρis small and the original dynamics is least
likely to escape; thus the controller acts more aggressively when deep inside the source basin.
Using Lemma 4, we can recover statistics of the original dynamics (1) from the accelerated path
alone. We present a reweighting mechanism via Girsanov’s change of measure in Appendix F.
4 Koopman-Based Construction of the Optimal Controller
Theorem 1 reduces the problem of sampling fromP∗,x to computing the optimal controlleru∗ =
∇logρ, whereρsolves the elliptic problem (11). For TPS in Example 1, applying this result
requires three ingredients: the source and target setsAi, Aj, the committor functionqwhich defines
the running costf β, andρitself. Each can be characterized through the Koopman generatorL.
Specifically, the metastable sets can be computed through the leading eigenfunctions ofL,qthrough
Lq= 0in (4), andρthroughLρ−f βρ= 0in (11).
4.1 Constructing Metastable Cores and Committor Functions
ThespectrumofthelinearoperatorLrevealsglobalgeometricstructuresoftheunderlyingdynamics
(Mezić, 2005; Mauroy and Mezić, 2016). In molecular dynamics, for example, the metastable sets
can be estimated using leading eigenfunctions whose eigenvalues are close to zero, followed by a
spectral gap (Mardt et al., 2018; Hou et al., 2023, 2026). Specifically, the leading eigenvalues
0 =λ 0 > λ1 ≥ · · · ≥λm−1 ≫λ m · · ·also capture the slow-mode, inter-basin dynamics. By
truncating atmmodes, fast modes are removed as they encode intra-basin dynamics. The leading
eigenfunctions{ψ k}m−1 k=1 are approximately constant within each metastable set but take different
values across them; we omitk= 0sinceψ 0 ≡1. LetΨ(x) = [ψ 1(x), . . . , ψm−1(x)]∈R m−1, where
{xn}N n=1 ⊂Xare data samples and the eigenpairs are estimated from them via kernel EDMD in
Section 2. We then applyk-means clustering to{Ψ(xn)}N n=1, which partitions the samples intom
8

clusters with index setsI1, . . . ,Im. For each clusterkand the set of leading eigenfunctionsψl, for
l= 1, . . . , m−1, we define the core level of thel-th eigenfunction as
θ(k) l := 1 |Ik| X n∈Ik ψl(xn), θ (k) :=  θ(k) 1 , . . . , θ(k) m−1 ⊤,(17)
so thatθ (k) is thek-means centroid of clusterk. Letε k >0be a radius. Since eachψ l is approxi-
mately constant on a metastable set with value approximatelyθ(k) l on thek-th one, we define the
core of thek-th metastable set fork= 1,· · ·, mas
Ak :={x∈X:∥Ψ(x)−θ (k)∥2 ≤ε 2 k}.(18)
Leveraging the global geometric structure carried by the leading eigenfunctions of the Koopman
generator, we next approximate the committor functionqvia an ansatzq= ˜ψ+h, where ˜ψis a
spectral term constructed from leading eigenfunctions andh∈ Hκ is a remainder withH κ is an
RKHS equipped with kernelκ, since in general, the solution of (4) may not lie in span{ψl}m−1 l=1 .
The spectral term ˜ψcontributes to the global shape of the transition, and also captures the slow
coordinate along which the transition occurs, without requiring a reaction coordinate to be specified
in advance. Due to space limitations, detailed construction of˜ψthat maps the core ofAi to0and the
core ofA j to1is presented in Appendix D. We computeh∈ Hκ viah(x) = P l∈Iq αl κ(x, xl)with
{xl}l∈Iq ⊂D q andI q ={1, . . . , Nq}. The coefficientsαare obtained from an equality-constrained
convex quadratic program that minimizes the residual of (4) inDq, which is also deferred to in
Appendix D. Putting together, we compute the committor function via
ˆq(x) :=˜ψ(x) + X
l∈Iq
αl κ(x, xl), (19)
4.2 Kernel-Based Approximation of the Optimal Controller
Unlike the fixed-horizon case studied in (Raginsky, 2026), whereu ∗ depends on time, the exit-
time optimal controlleru ∗ in (14) is stationary. To computeu ∗, we focus on approximatingρ
defined in (10) so that it solves the elliptic boundary value problem (11). By definition ofρ, and
fβ =β(1−q (i,j)),Φ≡0in Example 1, we have
ρ(x) =E x
h
e−βH0
i
, H 0 =
Z τD
0

1−q (i,j)(Xt)  dt,(20)
whereH 0 is the time spent in nonreactive regions before reaching the target. We need to handle
two regimes, capturing the transition region and regions within the basins. Directly approximating
ρin an RKHS can be challenging, as the behavior ofρin the two regimes may be quite different.
Near∂A j, the target is reached almost immediately andρ≈1. Within the source basin, however,
the transition is a rare event, andρis small as the trajectory lingers there. Sinceu∗ depends onρ
throughlogρ, we seek an ansatz of the formρ:=ρ 0(x)w(x)so thatlogρ= logρ 0 + logw. Here we
chooseρ 0 in closed form to capture howρvaries across the two regimes, and use a residualwto
solve forHκ. We defer additional details to Appendix E and only mention here that we approximate
ρvia a closed-form factorˆρas
ˆρ(x) :=ρ0(x)w(x), ρ 0(x) := ˆq(x) +

1−ˆq(x)

r, w∈ Hκ,(21)
whereH κ is an RKHS with kernelκ,ˆqas in (19) andr= 1 1+βT0 , withT 0 >0which encodes the
time-scale of the original dynamics; for example, we setT0 = 1 |λ1| ,whereλ 1 is the leading nontrivial
9

Koopman eigenvalue. Let{x i}N i=1 ={x i}i∈ID ∪ {xi}i∈I∂D, with interior points{xi}i∈ID ⊂Dand
boundary points{x i}i∈I∂D ⊂∂D. We approximatew∈ Hκ viaw= PN i=1 ci κ(x, xi)(Appendix E).
Applying the chain rule tolog ˆρ= logρ0 + logw, we have
ˆu(x) =∇log ˆρ(x) = (1−r)∇ˆq(x) ˆq(x) +  1−ˆq(x)  r + ∇w(x) w(x) .(22)
Thus, the problem of solving foru ∗ reduces to solving a convex quadratic program with linear
equalityconstraints, whosesolutionischaracterizedbyasinglelinearKKTsystemasinAppendixE.
The method is summarized in Algorithm 1.
Algorithm 1Summary of the Algorithm in Four Stages
Stage I.Construct leading eigenpairs(λ k, ψk)m−1 k=1 of the Koopman generatorLand identify
metastable cores.
Stage II.Compute the committor functionˆqvia (19) using the leading Koopman eigenfunctions.
Stage III.Construct the optimal controllerˆuvia (22).
Stage IV.SamplestartingpointsfromthesourcesetA i andintegratethecontrolleddynamics(9)
withˆufrom (22) until the paths hit the target set.
5 Numerical Experiments
We now present empirical evaluations of the proposed method on two synthetic systems, namely,
the two-channel double-well system (Figure 1) and the Müller-Brown system (Figure 2), and a
real-world alanine dipeptide (Figure 3). Due to space limitations, experimental details and one
additional example are deferred to Appendix G.4. In all these experiments, a path is a hit at its
first entrance to the target, and is truncated at the numerical censorTmax otherwise. We report
the target-hit percentage (THP), which is the fraction of paths that hit the target set beforeTmax.
We also remark that alanine dipeptide does not satisfy Assumption 2; nevertheless, our algorithm
can be applied beyond the confines of the theoretical analysis, and this experiment serves as a
demonstration that it performs well even in such cases.
References
Alain Berlinet and Christine Thomas-Agnan.Reproducing kernel Hilbert spaces in probability and
statistics. Springer Science & Business Media, 2011.
Peter G Bolhuis and David W H Swenson. Transition path sampling as markov chain monte carlo
of trajectories: Recent algorithms, software, applications, and future outlook.Advanced Theory
and Simulations, 4(4):2000237, 2021.
Peter G Bolhuis, David Chandler, Christoph Dellago, and Phillip L Geissler. Transition path
sampling: Throwing ropes over rough mountain passes, in the dark.Annual review of physical
chemistry, 53(1):291–318, 2002.
Christoph Dellago, Peter G Bolhuis, and David Chandler. Efficient transition path sampling: Ap-
plication to lennard-jones cluster rearrangements.The Journal of Chemical Physics, 108(22):
9236–9245, 1998.
10

Figure 1: Two-channel double well. The potential has two minima at(±
√
5/2,0)connected by
two channels around(0,±1). Following Algorithm 1, we compute the Koopman eigenfunctions and
extract the metastable coresAleft andA right as described in Section 4.1. Their minima are marked
by the green and red stars, and the dashed red curve marks∂Aright. We sample1000uncontrolled
and1000controlled paths, all started at the minimum ofAleft. (Left) Potential energy landscape.
(Middle) Uncontrolled paths: THP(Tmax) =0%. (Right) Proposed method: THP(Tmax) =99.8%.
(a) Uncontrolled
 (b) TPS-DPS
 (c) Proposed method
Figure 2: Müller-Brown potential, with a deep well at(−0.558,1.442)(green star), a medium well
at(0.623,0.028)(red circle), and a shallow well at(−0.050,0.467). We aim to sample transitions
from the deep well to the medium well withinTmax = 10ps. (a) Uncontrolled paths: THP(Tmax)
=1.8%. (b) TPS-DPS (Seong et al., 2025): THP(Tmax) =100%, but the paths run over the high
energy barrier. (c) Proposed method: THP(Tmax) =99.0%usingβ= 1, with paths following the
low-energy channel through the shallow well rather than crossing the barrier.
Yuanqi Du, Jiajun He, Dinghuai Zhang, Eric Vanden-Eijnden, and Carles Domingo-Enrich. Rare
event analysis via stochastic optimal control.arXiv preprint arXiv:2604.13213, 2026.
Wendell H Fleming. Exit probabilities and optimal stochastic control.Applied Mathematics and
Optimization, 4(1):329–346, 1977.
Helmut Grubmüller. Predicting slow structural transitions in macromolecular systems: Conforma-
tional flooding.Phys. Rev. E, 52:2893–2906, Sep 1995. doi: 10.1103/PhysRevE.52.2893. URL
https://link.aps.org/doi/10.1103/PhysRevE.52.2893.
Moritz Hoffmann, Martin Konrad Scherer, Tim Hempel, Andreas Mardt, Brian de Silva,
Brooke Elena Husic, Stefan Klus, Hao Wu, J Nathan Kutz, Steven Brunton, and Frank Noé.
Deeptime: a python library for machine learning dynamical models from time series data.Ma-
chine Learning: Science and Technology, 2021.
Lars Holdijk, Yuanqi Du, Ferry Hooft, Priyank Jaini, Berend Ensing, and Max Welling. Stochastic
11

(a) Uncontrolled
 (b) TPS-DPS
 (c) Proposed method
Figure 3: Alanine dipeptide in vacuum, shown on the free-energy surface over the backbone dihedral
angles(ϕ, ψ). We aim to sample the transition fromC5conformation (upper left) to theC7 ax
conformation (red star) withinTmax = 1ps. (a) Uncontrolled paths:(T max) = 0%(b) TPS-DPS:
THP(T max) = 100%, obtained by training a neural-network bias with simulation in the loop (1000
rollouts,∼10 6 gradient updates). (c) Proposed method: THP(T max) = 93%, with a controller
obtained in closed form. The setup and computational cost are reported in Appendix G.4.
optimal control for collective variable free sampling of molecular transition paths.Advances in
Neural Information Processing Systems, 36:79540–79556, 2023.
Boya Hou, Sina Sanjari, Nathan Dahlin, Subhonmesh Bose, and Umesh Vaidya. Sparse learning
of dynamical systems in rkhs: An operator-theoretic approach. InInternational Conference on
Machine Learning, pages 13325–13352. PMLR, 2023.
Boya Hou, Sina Sanjari, Alec Koppel, Nathan Dahlin, and Subhonmesh Bose. Nonparametric
sparse online learning of the koopman operator.To appear at SIAM Journal on Control and
Optimization, 2026.
Ioannis Karatzas and Steven Shreve.Brownian motion and stochastic calculus. springer, 2014.
Stefan Klus, Feliks Nüske, and Boumediene Hamzi. Kernel-based approximation of the koopman
generator and schrödinger operator.Entropy, 22(7):722, 2020.
Bernard O Koopman and J von Neumann. Dynamical systems of continuous spectra.Proceedings
of the National Academy of Sciences, 18(3):255–263, 1932.
Vladimir Kostic, Pietro Novelli, Andreas Maurer, Carlo Ciliberto, Lorenzo Rosasco, and Massimil-
iano Pontil. Learning dynamical systems via koopman operator regression in reproducing kernel
hilbert spaces.Advances in Neural Information Processing Systems, 35:4017–4031, 2022.
Olga A Ladyzhenskaya and Nina N Uraltseva.Linear and Quasilinear Elliptic Equations. Academic
Press, New York, 1968.
Alessandro Laio and Michele Parrinello. Escaping free-energy minima.Proceedings of the National
Academy of Sciences, 99(20):12562–12566, 2002. doi: 10.1073/pnas.202427399. URLhttps:
//www.pnas.org/doi/abs/10.1073/pnas.202427399.
Andrzej Lasota and Michael C Mackey.Chaos, fractals, and noise: stochastic aspects of dynamics,
volume 97. Springer Science & Business Media, 2013.
Andreas Mardt, Luca Pasquali, Hao Wu, and Frank Noé. Vampnets for deep learning of molecular
kinetics.Nature communications, 9(1):5, 2018.
12

Alexandre Mauroy and Igor Mezić. Global stability analysis using the eigenfunctions of the koopman
operator.IEEE Transactions on Automatic Control, 61(11):3356–3369, 2016.
Philipp Metzner, Christof Schütte, and Eric Vanden-Eijnden. Transition path theory for markov
jump processes.Multiscale Modeling & Simulation, 7(3):1192–1219, 2009.
Igor Mezić. Spectral properties of dynamical systems, model reduction and decompositions.Non-
linear Dynamics, 41(1):309–325, 2005.
Sanjoy K Mitter and Nigel J Newton. A variational approach to nonlinear estimation.SIAM journal
on control and optimization, 42(5):1813–1833, 2003.
Klaus Müller and Leo D. Brown. Location of saddle points and minimum energy paths by a
constrained simplex optimization procedure.Theoretica chimica acta, 53(1):75–93, Mar 1979.
ISSN 1432-2234. doi: 10.1007/BF00547608. URLhttps://doi.org/10.1007/BF00547608.
Bernt Oksendal.Stochastic differential equations: an introduction with applications (Fifth Edition).
Springer Science & Business Media, 2000.
Guillermo Pérez-Hernández, Fabian Paul, Toni Giorgino, Gianni De Fabritiis, and Frank Noé. Iden-
tification of slow molecular order parameters for markov model construction.The Journal of
chemical physics, 139(1), 2013.
Maxim Raginsky. A variational approach to sampling in diffusion processes.Communications in
Optimization Theory, 2026(30):1–20, 2026. URLhttps://cot.mathres.org/archives/2289.
ClarenceWRowley, IgorMezić, ShervinBagheri, PhilippSchlatter, andDanSHenningson. Spectral
analysis of nonlinear flows.Journal of fluid mechanics, 641:115–127, 2009.
Peter J Schmid. Dynamic mode decomposition of numerical and experimental data.Journal of
fluid mechanics, 656:5–28, 2010.
Kiyoung Seong, Seonghyun Park, Seonghwan Kim, Woo Youn Kim, and Sungsoo Ahn. Transition
path sampling with improved off-policy training of diffusion path samplers. InInternational
Conference on Learning Representations, volume 2025, pages 93040–93062, 2025.
Eric Vanden-Eijnden et al. Towards a theory of transition paths.Journal of statistical physics, 123
(3):503–523, 2006.
Arthur F. Voter. Hyperdynamics: Accelerated molecular dynamics of infrequent events.Phys. Rev.
Lett., 78:3908–3911, May 1997. doi: 10.1103/PhysRevLett.78.3908. URLhttps://link.aps.
org/doi/10.1103/PhysRevLett.78.3908.
Matthew O Williams, Clarence W Rowley, and Ioannis G Kevrekidis. A kernel-based approach to
data-driven koopman spectral analysis.Journal of Computational Dynamics, 2014.
Matthew O Williams, Ioannis G Kevrekidis, and Clarence W Rowley. A data–driven approximation
of the koopman operator: Extending dynamic mode decomposition.Journal of Nonlinear Science,
25(6):1307–1346, 2015.
13

Appendix
A The Reproducing Kernel Hilbert Space
We provide a brief introduction to the real-valued RKHS – for a more comprehensive treatment,
see (Berlinet and Thomas-Agnan, 2011). LetXbe a subset of a Euclidean space and letκ:X×X→
Rbe a continuous, symmetric, positive semi-definite kernel. Define the RKHS associated with the
kernelκ,H κ,as the completion of the span of{ϕ(x) :=κ(x,·) :x∈X}, equipped with the inner
product⟨·,·⟩, satisfying⟨ϕ(x), ϕ(y)⟩=κ(x, y). Here,ϕis called the feature map for the kernelκ.
The inner product satisfies thereproducing property, given by⟨ϕ(x), f⟩=f(x), for allx∈Xand
f∈ Hκ. Throughout the exposition, we make the standard assumption thatκis measurable.
A.1 Auxiliary Result: A Localized Dynkin Formula
Several proofs in this paper follow a similar outline: we start with a real-valued functionhthat
solves a partial differential equation onD, and we aim to evaluate the expectation ofhalong the
trajectory at the exit timeτD. However, Itô’s formula is stated for functions that areC2 onR n,
whereas the functions we work with areC2 only on the setD. Therefore, we need a mechanism to
integrate up toτ D at which time the trajectory reaches∂D. In addition, such aτ D is a random
variable itself. We address this by localizing, following the scheme in the proof of (Oksendal, 2000,
Theorem 9.1.1). Specifically, we first integrate toσk :=k∧τ Dk, whereD k is an increasing sequence
of open sets inD. Then on[0, σ k], the optional stopping theorem (Karatzas and Shreve, 2014,
Theorem 1.3.22) applies. Lettingk→ ∞then takes the result toτD, givenσ k →τ D. The following
lemma (localized Dynkin formula) makes this construction precise.
Lemma 5.Let Assumption 1–4 hold. LetYbe the pathwise unique strong solution of
dYt =b(Y t)dt+σ(Y t)dW t, Y 0 =x∈D,(23)
with generatorL Y h:=b ⊤∇h+ 1 2 P ij aij∂ijh, and letτD := inf{t >0 :Y t /∈D}. Define a sequence
of open sets as
Dk :={y∈D: dist(y, ∂D)>1/k}.(24)
Letσ k :=k∧τ Dk, whereτ Dk is the exit time ofYfromD k. Then, we have
(i)The sequence(σ k)k≥1 is nondecreasing, andσk →τ D ask→ ∞.
(ii)Leth∈C 2(D)∩C( ¯D),c∈C( ¯D)withc≥0, andZ t := exp  − R t 0 c(Ys)ds  . Then for every
k, we have
h(Yσk )Zσk −h(x) =
Z σk
0
Zt

LY h−ch

(Yt)dt+
Z σk
0
Zt ∇h(Yt)⊤σ(Yt)dW t,(25)
and
E

h(Yσk )Zσk

−h(x) =E
hZ σk
0
Zt

LY h−ch

(Yt)dt
i
.(26)
14

Proof.By construction ofD k in (24),D k ⊂D k+1, and S k Dk =D. Moreover, ¯Dk is a compact
subset ofD.
Part (i)For everyk≥1, sinceD k ⊂D k+1, we have{t >0 :Y t /∈Dk+1} ⊆ {t >0 :Yt /∈Dk}.
Hence,τ Dk ≤τ Dk+1. Sinceσ k =k∧τ Dk is the minimum of two nondecreasing sequences, it is itself
also nondecreasing.
We next show thatsupk σk =τ D pathwise. SinceD k ⊂D, we haveσ k ≤τ D for everyk, so
supk σk ≤τ D. For the reverse direction, fixωandt < τ D. Then{Y s : 0≤s≤t}is a compact
subset ofDand hence has strictly positive distance to∂D, so it is contained inDk0 for somek 0.
Fork >max(k 0, t)we haveDk0 ⊆D k, soτ Dk > tandσ k =k∧τ Dk > t. Ast < τD was arbitrary,
we havesup k σk ≥τ D.
Part (ii)Fixk≥1. We distinguish two cases, depending on whether the initial pointxis in¯Dk
or not. For the first case, considerx /∈¯Dk. SinceX\ ¯Dk is open and paths are continuous, there is
ϵ >0such thatY t /∈¯Dk, and in particularYt /∈Dk, for allt∈(0, ϵ). Henceτ Dk = 0andσ k = 0.
Thent∧σ k = 0for everyt≥0. We haveh(Y 0)Z0 −h(x) = 0asZ 0 = 1and all integrals from0to
σk = 0are zero. Hence, both sides of (25) and (26) vanish.
For the second case wherex∈ ¯Dk, we first show thatYt ∈ ¯Dk for allt∈[0, σ k]. Indeed,Y 0 =
x∈ ¯Dk, and fort∈(0, σk), we havet < τDk, henceY t ∈D k. Ifσ k >0, thenY σk = limt→σk Yt ∈ ¯Dk
by path continuity.
Since ¯Dk is a compact subset of the open setD, there exists someζk ∈C ∞ c (D)withζ k ≡1
on an open neighbourhoodU k of ¯Dk, so that in particular,Uk ⊆suppζ k ⊂D. Leth k equalζ kh
onDandh k := 0onR n \D. The open setsDandR n \suppζ k coverR n,h k isC 2 on the first
and identically zero on the second, and the two definitions agree on the overlap. Thushk ∈C 2(Rn)
with compact support. In addition, we havehk =h,∇h k =∇handL Y hk =L Y honU k.
SinceZ t = exp(−
R t
0 c(Ys)ds)is absolutely continuous intwithdZ t =−Z t c(Yt)dt, it has locally
bounded variation and hencedZ⊤ t dYt = 0. Applying Itô’s product rule toh k(Yt)Zt on[0, t∧σ k],
we have
hk(Yt∧σk )Zt∧σk −h k(x) =
Z t∧σk
0
Zs

LY hk −c hk

(Ys)ds+
Z t∧σk
0
Zs∇hk(Ys)⊤σ(Ys)dWs.(27)
SinceY s ∈ ¯Dk ⊂U k fors≤t∧σ k, every term above may be written in terms ofh, yielding (25).
Finally,σ k ≤kis a bounded stopping time,∇h k is continuous with compact support, hence
bounded onR n. In addition,σis bounded by Assumption 2, andZs ∈(0,1]sincec≥0. Hence, we
haveE
R k
0 |Zs ∇hk(Ys)⊤σ(Ys)|2ds  <∞and the optional stopping theorem (Karatzas and Shreve,
2014, Theorem 1.3.22) applies. Takingt=kin (25), so thatt∧σ k =σ k, and taking expectations
proves Eq. (26).
B Proof of Results in Section 3
B.1 Proof of Lemma 1
Since ¯Dis bounded by Assumption 3, we haveb∈C 0,α( ¯D)forα∈(0,1). We show that the
SDE (1) withX 0 =x∈Dhas a pathwise unique strong solution, and its exit timeτ D satisfies
Ex[τD]≤φ(x)<∞, whereφ∈C 2,α( ¯D),φ≥0is the unique solution of the elliptic BVP
Lφ=−1inD, φ| ∂D = 0.(28)
Step 1:Consider the elliptic BVPLφ=−1inD,φ| ∂D = 0. Sinceb∈C 0,α( ¯D)anda=
σσ⊤ ∈C 0,α( ¯D)by Assumption 2,∂D∈C 2,α by Assumption 3, and the boundary data0∈
15

C2,α(∂D), elliptic regularity theory (Ladyzhenskaya and Uraltseva, 1968, Ch. III, Theorem 1.1 and
Theorem 1.2) guarantees existence and uniqueness of a solutionφ∈C2,α( ¯D).
Step 2:To establish thatφ≥0on ¯D, we will show that the minimum ofφover ¯Dis attained
at a boundary point and is therefore equal to0sinceφ|∂D ≡0. Suppose, for contradiction, thatφ
attains a local minimum at some interior pointx0 ∈D. Then∇φ(x 0) = 0andHess (φ(x 0))⪰0by
the second-order necessary condition for a local minimum. And we have
Lφ(x0) =b(x 0)⊤∇φ(x0)| {z }
=0
+ 1 2 tr  a(x0) Hess (φ(x0))  ≥0.(29)
Here, by uniform ellipticity in Assumption 2, we havea(x0)≻0, and sinceHess (φ(x 0))⪰0, the
inequality holds. This contradictsLφ≡ −1<0onD. Henceφhas no interior local minimum, so
min ¯D φ= min ∂D φ= 0, i.e.φ≥0on ¯D.
Step 3:Sinceb, σare bounded and Lipschitz by Assumption 1, the SDE (1) has a pathwise
unique strong solution for allt≥0(Oksendal, 2000, Thm. 5.2.1).
Step 4:We next showEx[τD]≤φ(x). By the previous step, Eq. (1) has a pathwise unique strong
solution, so Lemma 5 applies withh=φandc≡0. Let(σ k)k≥1 and(D k)k≥1 be the stopping
times and open sets defined in Lemma 5. SinceLφ=−1onD, Eq. (26) givesEx[φ(Xσk )]−φ(x) =
−Ex[σk]. By Step 2,φ≥0on ¯D. SinceD k ⊂D, we haveσ k ≤τ Dk ≤τ D. And, since the path
stays in ¯Dup to its exit timeτD, we haveXσk ∈ ¯D. Thus we haveEx[φ(Xσk )]≥0, and hence
Ex[σk]≤φ(x), k∈N.(30)
Since the sequence(σk)k≥1 is nondecreasing andσk →τ D from Lemma 5(i), monotone convergence
applied to (30) givesEx[τD] = limk Ex[σk]≤φ(x)<∞. Here, sinceφ∈C( ¯D)and ¯Dis compact,
max ¯D φ <∞, sosupx∈D Ex[τD]≤max ¯D φ <∞. Finally, a nonnegative random variable with finite
expectation is finite almost surely, henceτD <∞a.s.
B.2 Finite Mean Exit Time for Controlled Processes
By Assumption 1,bis bounded and Lipschitz onX. More generally, foru∈ U,b+auis bounded
and Lipschitz onX, asais bounded and Lipschitz by Assumption 2, anduis Lipschitz on¯D, which
is compact, hence bounded, and is extended toX. Hence, the following result on the finite mean
exit time for every admissible control is immediate by applying Lemma 1 to˜b=b+au.
Corollary 1.Consider the controlled SDE(9), and denote ˜Lg:= (b+au) ⊤∇g+ 1 2 P ij aij∂ijg.
Let Assumptions 1–3 hold and letu∈ U. Then, the controlled SDE(9)starting fromx∈Dhas a
pathwise unique strong solution ˜X, and its exit-time˜τD satisfies ˜Ex[˜τD]<∞. Thus we also have
˜τD <∞, ˜P u,x-a.s.
B.3 Proof of Lemma 2
To showw=ρonD, letY t :=w(X t)andZ t := exp(−
R t
0 f(X s)ds). Fixx∈Dand we apply
Lemma 5 withh=w, andc=fthat satisfies Assumption 4. SinceLw−f w= 0inD, the drift
term in (26) vanishes and we have
Ex

w(Xσk )Zσk

=w(x), k∈N.(31)
We now takek→ ∞. By Lemma 1,τ D <∞,P x-a.s. Sinceσ k →τ D andDis open,
Xσk →X τD ∈∂D. By continuity ofwon ¯Dand using the boundary condition (11), we haveYσk =
16

w(Xσk )→e −Φ(XτD ) a.s. By continuity oft7→ R t 0 f(X s)ds, we haveZσk →exp(− R τD 0 f(X s)ds)a.s.
Moreover, sincew∈C( ¯D)with ¯Dcompact andZ t ∈(0,1], we have|Y σk Zσk | ≤max¯D |w|<∞for
everyk. Hence,Y σk Zσk →e −Φ(XτD ) exp(− R τD 0 f ds)a.s., and this sequence is uniformly bounded
bymax ¯D |w|. Thus, the bounded convergence theorem gives
lim
k→∞
Ex

Yσk Zσk

=E x

e−Φ(XτD ) exp

−
Z τD
0
f(X s)ds

=ρ(x),(32)
where the last equality follows from the definitionρin (10). On the other hand,Ex[Yσk Zσk ] =w(x)
for everykby (31), so the limit on the left isw(x). Therefore, we concludew(x) =ρ(x)onD.
Forx∈∂D, we haveτ D = 0,P x a.s. hence (10) givesρ(x) =e −Φ(x) =w(x)via the boundary
condition (11). Hence,w(x) =ρ(x)on ¯D.
It remains to showρ >0on ¯D. On the boundary,ρ| ∂D =e −Φ =g >0by Assumption 4. In
the interior, fixx∈D: by Assumption 4,f≥0is bounded on ¯DandΦ =−loggis bounded on
∂D, whileτ D <∞a.s. by Lemma 1. Hence, we have
exp

−
Z τD
0
f(X t)dt−Φ(X τD )

>0, P x-a.s.,(33)
and taking expectations givesρ(x)>0. Combining these,ρ >0on ¯D. Sinceρ∈C( ¯D)and ¯Dis
compact, it follows thatmin¯D ρ >0.
B.4 Proof of Lemma 3
Recallx= (x 1, . . . , xn)∈X, and∂ ij denotes the second partial derivative with respect toxi and
xj. The gradient ofρis given by
∇ρ=e −v(−∇v) =−ρ∇v.(34)
For the second-order partP ij aij∂ijρ, we have
X
ij
aij∂ijρ=−
X
ij
aij∂jρ ∂iv−ρ
X
ij
aij∂ijv.(35)
Substituting∂ jρ=−ρ ∂ jv, we have
X
ij
aij∂ijρ=ρ
X
ij
aij∂iv ∂jv−ρ
X
ij
aij∂ijv=ρ

(∇v)⊤a∇v−∆ av  ,(36)
where∆ av:= P ij aij∂ijv. Hence,Lρcan be written as
Lρ=b ⊤(−ρ∇v) + 1 2 ρ  (∇v)⊤a∇v−∆ av 
=ρ
h
−b⊤∇v− 1 2 ∆av+ 1 2 (∇v)⊤a∇v i
=ρ
h
−Lv+ 1 2 (∇v)⊤a∇v i ,
(37)
where the last line follows fromb⊤∇v+ 1 2 ∆av=Lv. UsingLρ−f ρ= 0, and sinceρ >0, divide by
ρ, we have
−Lv+ 1 2 (∇v)⊤a∇v=f.(38)
17

Rearranging the above equation, we have
Lv(x) +f(x) = 1 2 (∇v(x))⊤a(x)∇v(x)inD, v

 ∂D = Φ.(39)
We next show that this coincides with the HJB equation for the OSC (12) up to an exit time.
Let ˜Xt solve the controlled SDE (9). Sincev∈C 2(D), Itô’s formula gives
dv( ˜Xt) =  Lv( ˜Xt) + (∇v( ˜Xt))⊤a( ˜Xt)u( ˜Xt)  | {z }
drift
dt+∇v( ˜Xt)⊤σ( ˜Xt)d ˜Wt.(40)
Foru∈ U, substituting (39) into the drift, and adding and subtracting1 2 u⊤a u, we have
drift=−

f+ 1 2 u⊤a u  + 1 2 (∇v+u) ⊤a(∇v+u),(41)
where the last term≥0sincea⪰0. Equation (41) also shows that, for eachx∈D, the mapping
u7→u ⊤a∇v+ 1 2 u⊤auis minimized uniquely atu∗ =−∇v, sincea≻0by Assumption 2. Therefore,
(13) is the HJB equation of the OSC (12) up to an exit time, with a candidate optimal controller
u∗ in (14).
B.5 Proof of Proposition 1
SinceH≥0, we haveHe −H ≥0and hence−E x[He −H ]<∞. Together withZ∈(0,∞),
hypotheses of Mitter and Newton (2003, Proposition 2.1) hold on(Ω,FτD )with reference measure
P x|FτD and energyH. Hence, the claim follows.
B.6 Proof of Lemma 4
Sinceρ∈C 2,α( ¯D)as established in Lemma 2, and−logis smooth on[m, M], the chain rule gives
v=−log◦ρ∈C 2,α( ¯D), thus we haveu ∗ =−∇v∈C 1,α( ¯D), henceu ∗ ∈ U. By the paragraph
preceding Corollary 1, ˜b:=b−a∇vis bounded and Lipschitz onR n. Thus, (9) has a pathwise
unique strong solution for allt≥0by the standard SDE existence-uniqueness theorem for bounded,
Lipschitz coefficients; see, e.g., (Oksendal, 2000, Thm. 5.2.1).
Define an exponential process as
Zt := exp
Z t
0

(σ⊤u∗)(Xs) ⊤ dWs − 1 2 Z t 0 |σ⊤u∗(Xs)|2 ds  , t < τ D.(42)
Sincev∈C 2,α( ¯D)and ¯Dis compact by Assumption 1,∇vis continuous and hence bounded on¯D.
Together withσbounded by Assumption 2, letC:=∥σ∥ ∞ ∥∇v∥∞ and we have

σ⊤u∗

 ≤Con ¯D.
Sinceτ D <∞a.s. by Lemma 1, we have
R τD
0 |σ⊤u∗(Xs)|2 ds≤C 2τD <∞a.s. Thus the stochastic
integral in (42) is well defined att=τD, andt7→Z t is continuous on[0, τD].
Step 1:WecomputeZ t asfollows. Sincea=σσ ⊤ andu ∗ =−∇v, wehave(∇v) ⊤a∇v=|σ ⊤u∗|2,
so the HJB equation (39) isLv= 1 2 |σ⊤u∗|2 −finD. Applying Lemma 5 withh=vandc= 0,
and takingklarge enough thatσ k > t, which is possible sinceσk →τ D, fort < τD, we have,
dv(Xt) =Lv(X t)dt+∇v(X t)⊤σ(Xt)dW t =  1 2 |σ⊤u∗(Xt)|2 −f(X t)  dt−  (σ⊤u∗)(Xt) ⊤ dWt,
(43)
where we used∇v=−u ∗ and the HJB equation (13).
18

Rearranging and integrating from0tot < τD, we have
Z t
0

(σ⊤u∗)(Xs) ⊤ dWs − 1 2 Z t 0 |σ⊤u∗(Xs)|2 ds=v(x)−v(X t)− Z t 0 f(X s)ds.(44)
Taking exponential and usinge−v =ρ, we have
Zt = ρ(Xt) ρ(x) exp  − Z t 0 f(X s)ds  , t < τ D.(45)
Step 2:We now taket→τ D in (45). By Lemma 1, we haveτ D <∞,P x-a.s., thusX t →
XτD ∈∂Dby continuity of the path, andρ(X t)→ρ(X τD ) =e −Φ(XτD ) by continuity ofρon ¯D
together with the boundary conditionρ|∂D =e −Φ in (11). Moreover, R t 0 f(X s)ds→ R τD 0 f(X s)ds
by continuity oft7→
R t
0 f(X s)ds, the limit is finite sincefis bounded by Assumption 4 andτD <∞
a.s. Hence, we have
ZτD = e−Φ(XτD ) ρ(x) exp  − Z τD 0 f(X s)ds  = e−H(χ) ρ(x) , P x-a.s. (46)
Taking expectations, the Feynman–Kac identityρ(x) =Ex[e−H(χ) ]of (10) gives
Ex

ZτD

= ρ(x) ρ(x) = 1.(47)
Step 3:Since ¯Dis compact andρ∈C( ¯D), we have0< m≤ρ≤M <∞on ¯D; and
exp(−
R t
0 f ds)∈(0,1]sincef≥0. Hence (45) gives the uniform, deterministic bound
0< Zt∧τD ≤ M ρ(x) for everyt≥0and a.e.ω.(48)
The stopped processZ ·∧τD is a stochastic exponential, hence a local martingale; by (48) it is
bounded, and a bounded local martingale is a true martingale. ThereforeEx[Zt∧τD ] = 1for every
t≥0.
Step 4:Finally, defineQonF τD viadQ/dP x =Z τD, which is a probability measure by the
above. By Girsanov’s theorem, we haveWt −
R t
0 σ⊤u∗(Xs)dsis aQ-Brownian motion on[0, τ D].
Thus underQ, the process solves the controlled SDE (9) withu=u∗ up toτ D. By uniqueness in
law for said SDE, established above, we haveQ= ˜P ∗,x onF τD, which together with (46) proves
(15).
B.7 Proof of Theorem 1
Part (i).We first consideru∈ U, and consider the optimal controlu∗ at the end as the special case.
We proceed in four steps: (1) applying Itô’s formula forv(˜Xt)underu∈ U; (2) applying Lemma 5
to integratevon ¯D; (3) passingk→ ∞; and (4) rearranging and specializing tou=u∗.
Step 1:From Itô’s formula and (41), for the controlled process˜X,we have
dv( ˜Xt) =−

f( ˜Xt) + 1 2 u⊤a u(˜Xt)  dt+ 1 2  ∇v+u ⊤a  ∇v+u  ( ˜Xt)dt+∇v( ˜Xt)⊤σ( ˜Xt)d ˜Wt.
(49)
19

Step 2:The above equation is derived fromv∈C 2(D), so it may be integrated only while the
trajectory remains inD. We therefore apply Lemma 5 with driftb+au,h=vandc≡0along
the controlled diffusion process (9), where admissibility ofuand Assumption 2 make the drift term
bounded and Lipschitz. Substituting the drift decomposition in (41) into (26), we have
˜E  v( ˜Xσk )  | {z }
:=T1
−v(x) =− ˜E
Z σk
0

f+ 1 2 u⊤a u  dt 
| {z }
:=T2
+ ˜E
Z σk
0
1
2 (∇v+u) ⊤a(∇v+u)dt

| {z }
:=T3
.(50)
Step 3:We next study the three termsT1-T3 in (50) separately. For the boundary termT1, recall
by Corollary 1,˜τD <∞a.s., and we have shown before thatσ k →˜τD ask→ ∞in Lemma
5. Hence ˜Xσk → ˜X˜τD a.s. by continuity of the path. Since the controlled process exitsDat
time˜τD, we have ˜X˜τD ∈∂Da.s., so continuity ofvon ¯Dtogether with the boundary condition
v|∂D = Φgivesv( ˜Xσk )→v( ˜X˜τD ) = Φ( ˜X˜τD )a.s. Moreoverv∈C( ¯D)with ¯Dcompact gives
|v| ≤M:= max ¯D |v|<∞, so|v( ˜Xσk )| ≤Mfor everykand a.e.ω. By bounded convergence
theorem, we thus have
lim
k→∞
˜E  v( ˜Xσk )  = ˜E  Φ( ˜X˜τD )  .(51)
For the running costT2, sincef≥0by Assumption 4 anda≻0by Assumption 2, we have
thatf+ 1 2 u⊤a uis nonnegative. Asσk is nondecreasing withσk →˜τD from Lemma 5, the integralsR σk
0 (f+ 1 2 u⊤a u)dtare nondecreasing inkand converge pointwise a.s. to R ˜τD 0 (f+ 1 2 u⊤a u)dt. By
monotone convergence theorem, we have
lim
k→∞
˜E
Z σk
0

f+ 1 2 u⊤a u  dt  = ˜E Z ˜τD
0

f+ 1 2 u⊤a u  dt  .(52)
ForthelasttermT 3, proceedsimilarlyasabove, sincea≻0, 1 2 (∇v+u)⊤a(∇v+u)isnonnegative,
so monotone convergence theorem gives
lim
k→∞
˜E
Z σk
0
1
2 (∇v+u) ⊤a(∇v+u)dt

= ˜E
Z ˜τD
0
1
2 (∇v+u) ⊤a(∇v+u)dt

.(53)
We next show that all three limits are finite. Indeed, by Assumption 4,Φ =−loggis continuous
on the compact set∂D, hence bounded. LetC:= sup ¯D

f+ 1 2 u⊤a u  andC ′ := sup ¯D 1 2 (∇v+
u)⊤a(∇v+u). Both terms are finite becausefis bounded by Assumption 4,ais bounded by
Assumption 2,u∈ Uis bounded on the compact ¯Dby definition, and∇vis bounded on ¯Dsince
v∈C 2,α( ¯D). The two integrals in (52) and (53) are dominated byC˜τD andC ′˜τD, respectively,
whose expectations are finite since˜E  ˜τD  <∞by Corollary 1. Combining (51)–(53) into (50), we
have
˜E  Φ( ˜X˜τD )  −v(x) =− ˜E Z ˜τD
0

f+ 1 2 u⊤a u  dt  + ˜E Z ˜τD
0
1
2 (∇v+u) ⊤a(∇v+u)dt

,(54)
where every term is finite.
Step 4:Rearranging (54), and using∇v+u=u−u ∗ asu ∗ =−∇v, we obtain
J(u, x) =˜E  Φ( ˜X˜τD )  + ˜E Z ˜τD
0

f+ 1 2 u⊤au  dt 
=v(x) + ˜E
Z ˜τD
0
1
2 (u−u ∗)⊤a(u−u ∗)dt

≥v(x),
(55)
20

where the inequality follows froma≻0by Assumption 2. Sinceu∈ Uwas arbitrary,v(x)is a lower
bound. Here, equality holds if and only if˜E R ˜τD 0 1 2 (u−u ∗)⊤a(u−u ∗)dt  = 0. Since the integrand
is nonnegative, this holds if and only if
R ˜τD
0
1
2 (u−u ∗)⊤a(u−u ∗)( ˜Xt)dt= 0, ˜P u,x-a.s. Again, by
nonnegativity, it holds if and only if(u−u ∗)⊤a(u−u ∗)( ˜Xt) = 0for Lebesgue-almost everyt∈
[0,˜τD(ω)], ˜P u,x-a.s. By uniform ellipticity in Assumption 2, we have(u−u∗)⊤a(u−u ∗)≥c|u−u ∗|2
withc >0. So this is equivalent tou(˜Xt) =u ∗( ˜Xt)for Lebesgue-almost everyt∈[0,˜τ D], ˜P u,x-a.s.
It remains to check that this bound is attained. Sincev∈C 2,α( ¯D), we haveu ∗ =−∇v∈
C1,α( ¯D), henceu ∗ ∈ Uand (55) applies. The remainder term then vanishes identically, and we have
J(u ∗, x) =v(x). Hence, the infimum is attained, and for everyx∈D, we have
v(x) =J(u ∗, x) = min
u∈U
J(u, x).(56)
This completes the proof of Part (i).
Part (ii)Sinceτ D <∞,P x-a.s. as in Lemma 1,H(χ)is well-defined and finitePx-a.s., and by the
Feynman–Kac representation ofρ, we can define
Z:=E x

e−H(χ)  =ρ(x)∈(0,1],(57)
soZ∈(0,∞)as required by (Raginsky, 2026, Proposition 1). Moreoverf≥0by Assumption 4
andΦ =−logg≥0sinceg≤1by the same assumption, soH(χ)≥0P x-a.s. Hence the integrand
−H(χ)e −H(χ) is non-positive and−E x  H(χ)e −H(χ)  <∞. So both assumptions of Proposition 1
are satisfied, and applying it on(Ω,FτD )withP=P x andH=H(χ), for every admissible path
measure ˜P≪P x, we have
DKL( ˜P∥P x) +E[H(χ)]≥ −logρ(x) =v(x),(58)
with equality if and only ifd˜P /dPx =e −H(χ) /ρ(x). By Part (i), we havev(x) =J(u ∗, x), so (58)
is (16). By Lemma 4,˜P ∗,x of the optimally-controlled process satisfies
d ˜P ∗,x
dP x

FτD
= e−H(χ)
ρ(x) (59)
Hence equality in (58), and so in (16), holds if and only if˜P= ˜P ∗,x.
C Proof of Identity(4)in Section 4.1
LetAssumption2hold. ByconstructioninSection4.1,A i, Aj areclosed, and∂A i∩∂Aj =∅. Assume
thatD q =X\(A i ∪A j)satisfies Assumption 3, with∂D q =∂A i ∪∂A j. Denoteφ:∂D q → {0,1}
withφ= 0on∂A i andφ= 1on∂A j. Since∂A i and∂A j are disjoint compact sets,φis locally
constant, henceφ∈C 2,α(∂Dq). By (Ladyzhenskaya and Uraltseva, 1968, Ch. III, Theorem 1.1 and
Theorem 1.2), the boundary value problem
Lw= 0inD q, w| ∂Dq =φ,(60)
has a unique solutionw∈C 2,α( ¯Dq). In particular,wis continuous and bounded on the compact
set ¯Dq.
We next showq=w. Forx∈D q, letτ:= inf{t >0 :X t /∈Dq}be the first time the trajectory
leavesD q. SinceX\D q =A i ∪A j, we haveτ=τ Ai ∧τ Aj. LetD k,σ k be as in Lemma 5 with
21

D=D q. Apply Lemma 5(ii) withh=wandc= 0, we haveZ t = 1. SinceLw= 0inD q, from
(26), we have
Ex

w(Xσk )

=w(x), k∈N.(61)
Herew(X σk )is well defined sinceX σk ∈ ¯Dq by the case split in the proof of Lemma 5.
We next takek→ ∞. From Lemma 5(i), we haveσ k →τ. Sinceτ <∞a.s.,D q is open,
and by path continuity, we haveXσk →X τ ∈∂D q a.s. Sincewis continuous on ¯Dq, we have
w(Xσk )→w(X τ ) =φ(X τ )a.s. Furthermore,|w(X σk )| ≤max ¯Dq |w|<∞fork∈N. By the
bounded convergence theorem, we then have
w(x) =E x

φ(Xτ )

=P x Xτ ∈∂A j  ,(62)
where the second equality follows sinceφ(Xτ ) =1 ∂Aj (Xτ ).
Finally, we showP x Xτ ∈∂A j  =q(x). SinceA i, Aj are closed by construction, and paths
are continuous, and by definition ofτ, we haveX τAk ∈A k wheneverτ Ak <∞fork∈ {i, j}. If Xτ ∈∂A j ⊂A j, thenτ̸=τ Ai, since otherwiseX τ ∈A i ∩A j =∅, and we haveτ=τ Aj < τAi.
Conversely, ifτ Aj < τAi, thenτ=τ Aj, and we haveXτ ∈∂A j. Thus{X τ ∈∂A j}={τ Aj < τAi},
and forx∈D q, we have
w(x) =P x τAj < τAi  =q(x).(63)
By definition ofq, forx∈∂A i (x∈∂A j), we haveq(x) = 0 =w(x)(q(x) = 1 =w(x)). Hence
q=won ¯Dq. Therefore,q∈C 2,α( ¯Dq), andqis the unique solution of (4).
D Detailed Computation of the Committor Function from Section
4.1
We first construct the spectral term˜ψthat separates the two cores using the leading eigenfunctions
ofL. ConsiderA k and the set of leading eigenfunctionsψl, forl= 1, . . . , m−1. With the core level
θ(k) l defined in (17), we defineˆψ(x) := Pm−1 l=1 cl ψl(x), wherec l :=θ (j) l −θ (i) l measures how much the
l-th mode varies betweenAi, Aj. Define the core level ofˆψas ¯θ(k) := 1 |Ik| P i∈Ik ˆψ(xi). Substituting
ˆψ, we have¯θ(k) = P l clθ(k) l . Letc= [c 1,· · ·, cm−1]. We recenter and rescaleˆψto get ˜ψas
˜ψ(x) := ˆψ(x)− ¯θ(i)
∥c∥2 , ¯θ(i) = X l clθ(i) l .(64)
With this choice ofc, we have ¯θ(j) − ¯θ(i) =∥c∥ 2, and ˜ψmaps the centroid ofA i to0and that of
Aj to1. Since eachψ l is an eigenfunction, we have∇ˆψ= Pm−1 l=1 cl ∇ψl, andL ˆψ= Pm−1 l=1 cl λl ψl.
ApplyingLto (64) and using that ¯θ(i) and∥c∥ 2 are constants, so thatL ¯θ(i) = 0, we haveL ˜ψ=
L ˆψ/∥c∥2 = 1 ∥c∥2 Pm−1 l=1 cl λl ψl. Using linearity ofL, we obtainLh=Lq−L ˜ψ=−L ˜ψinD q.
Together with the boundary conditionsq|∂Ai = 0andq| ∂Aj = 1, we have thathsolves
Lh=−L ˜ψinD q, h| ∂Ai =− ˜ψ|∂Ai, h| ∂Aj = 1− ˜ψ|∂Aj .(65)
We next approximate the remainderhin the ansatzq= ˜ψ+hinH κ. To solve (65) with˜ψin
(64), let{x l}l∈Iq ⊂D q withI q ={1, . . . , Nq}, and consider solving for ah∈ Hκ of the form
h(x) =
X
l∈Iq
αl κ(x, xl), α= (α l)l∈Iq .(66)
22

The problem then reduces to solving forα. To this end, we impose (65) it at interior points
{xn}n∈Jq ⊂D q where the residual is minimized, and boundary points{x n}n∈J∂ ⊂∂A i ∪∂A j
where the boundary condition is imposed. Specifically, define the matrixA∈R|Jq|×|Iq| and vector
g∈R |Jq| with entries
Anl := (Lκ)(xn, xl),[g] n := (L ˜ψ)(xn) = 1 ∥c∥2 m−1X l=1 clλlψl(xn),(67)
forn∈ Jq. Similarly, defineK∂ ∈R |J∂ |×|Iq| andb∈R |J∂ | as
(K∂)nl :=κ(x n, xl),(b) n :=
(
− ˜ψ(xn), x n ∈∂A i,
1− ˜ψ(xn), x n ∈∂A j, (68)
forn∈ J∂. Here,Lκcan be computed using the derivative of the kernel functionκ. Specifically,
for the Gaussian kernelκ(x, y) = exp

− ∥x−y∥2/2σ2 with bandwidthσ, writingz:=x−y, we
have
∇xκ(x, y) =− z σ2 κ(x, y), ∂ xixj κ(x, y) =  zizj σ4 − δij σ2  κ(x, y).(69)
Hence, we have
(Lκ)(x, y) =

− b(x)·z σ2 + z⊤a(x)z 2σ4 − tra(x) 2σ2  κ(x, y).(70)
We next solve forαin (66) by imposing the boundary condition at{xn}n∈J∂ and minimizing
the least-squares sense with Tikhonov regularization as
min
α
Aα+g 2 +λ q α⊤Kα,
s.t.K ∂ α=b,
(71)
forλ q ≥0andK ll′ =κ(x l, xl′ ). For such an equality-constrained quadratic program, define a
multiplierµ∈R |J∂ |. The Lagrangian is then∥Aα+g∥ 2 +λ qα⊤Kα+ 2µ ⊤(K∂α−b), and the KKT
conditions in(α, µ)are
"
A⊤A+λ qK K ⊤ ∂
K∂ 0
# "
α
µ
#
=
"
−A⊤g
b
#
.(72)
Solving forˆαvia the linear system (72) and plugging this intoq= ˜ψ+h, the committor function
can be approximated via (19).
E Details Behind the Computation ofρfrom Section 4.2
We start by constructingρ0. Considerx∈D, defineτ i := inf{t >0 :X t ∈A i}, andτj := inf{t >0 :
Xt ∈A j}=τ D. LetR:={τ j < τi}be the reactive event, i.e., the trajectory reaches the target set
before returning to the source set. By definition of the committor function in Section 4.1, we have
23

q(i,j)(x) =P x(R)whereP x denotes the probability of starting fromx. ConditioningEx  e−βH0  in
(20) onRandR c, and using the law of total expectation, we have
ρ(x) =Ex
h
e−βH0
i
=P x(R)E x
h
e−βH0

 R i
| {z }
:=ρR(x)
+P x(Rc)E x
h
e−βH0

 Rc i
| {z }
:=ρNR(x)
=q(i,j)(x)ρR(x) +  1−q (i,j)(x)  ρNR(x),
(73)
whereρ R, ρNR ∈(0,1]sinceH 0 ≥0, withtheconventionthatatermisomittedwhenitsconditioning
event has probability zero. Thusρ(x)is a convex combination ofρ R(x)andρ NR(x)with weight
beingq(x). In practice, we useˆqfrom (19) as an approximation ofq.
OnR c, the trajectory reachesA i at timeτ i < τj. We therefore splitH 0 =H i 0 +H ij 0 with
H i 0 := R τi 0 (1−q (i,j))dtandH ij 0 := R τj τi (1−q (i,j))dt. Conditioning on the path up to timeτi, by the
Markov property, we haveE

e−βH ij 0 | Fτi  =ρ(X τi)whereX τi ∈∂A i. Sincee −βH0 =e −βH i 0e−βH ij 0 ,
we have
ρNR(x) =E x
h
e−βH i 0 ρ(Xτi)

Rc i .(74)
Forρ(X τi), notice that the trajectory lingers insideAi, and henceρ(X τi)≈ρ| Ai. To compute the
latter, lety∈A i. Sinceq (i,j) ≡0onA i and the trajectory spends nearly all of time[0, τj]insideA i,
we haveH i 0 ≈τ j. Since the system is metastable, we assume the first hitting time is asymptotically
exponential with meanT 0 = 1/|λ1|, whereλ 1 is the leading nontrivial eigenvalue of the Koopman
generator. In other words„τj has densityT −1 0 e−t/T0 ont≥0, and we have
ρA ≈E
h
e−βτj
i
=
Z ∞
0
1
T0
e−t/T0 e−βt dt= 1 1 +βT 0 =:r.(75)
Hence, we have
ρ(x) =q(i,j)(x)ρR(x) + h 1−q (i,j)(x)  r i Ex h e−βH i 0

 Rc i .(76)
OnR, the trajectory goes fromxtoA j without visitingA i, henceρ R =E x

e−βH0

 R  lies in
(0,1]withH 0 the duration of reactive crossing. For termEx
h
e−βH i 0

Rc i , onR c,H i 0 is the time
of a non-reactive path falling back intoAi. Therefore, neither term encodes the metastability of
the system, and the metastability enters only throughq(i,j)(x)and  1−q (i,j)(x)  r. We therefore
consider the factorization ofρas
ρ=

q(i,j)(x) +  1−q (i,j)(x)  r  × ρ q(i,j)(x) +  1−q (i,j)(x)  r . (77)
Replacingq (i,j) by its approximationˆqfrom (19), we defineρ0(x) := ˆq(x) +  1−ˆq(x)  r, and the
remainder is theH0.
We next computewin the ansatzˆρ(x) :=ρ0(x)w(x). Sinceρ 0 is affine inˆq, we also have
∇ρ0 = (1−r)∇ˆq, Lρ 0 = (1−r)Lˆq,(78)
By the product rule, we have
L(ρ0w) =ρ 0Lw+wLρ 0 +∇ρ ⊤ 0 a∇w.(79)
24

ThusLρ−f βρ= 0in (11) can be written in terms ofwas
ρ0 Lw+w

Lρ0 −f β ρ0

+∇ρ ⊤ 0 a∇w= 0inD.(80)
To solve (80), define two matrices inR|ID|×N as
(KD)li =κ(x l, xi),(LK) li = (Lκ)(xl, xi),(81)
forx l ∈I D andi= 1, . . . , N. In addition, defineΓD ∈R |ID|×N, andP, Q∈R |ID|×|ID| as
(ΓD)li =∇ρ 0(xl)⊤a(xl)∇ xκ(xl, xi),
P:= diag

ρ0(xl)

, Q:= diag

Lρ0(xl)−f β(xl)ρ0(xl)

, (82)
where∇ xκis available in closed form as in (69), and∇ˆq=∇˜ψ+ P l αl∇xκ(·, xl)from (19). Using
the chain rule and (21), we also have
Lρ0 =ρ 0

η Lˆq+η2 2 ∇ˆq⊤a∇ˆq  .(83)
Hence (81) together with (82), the residual of (80) at the interior points can thus be written as

P LK+Q KD + ΓD

c=:S D c, S D ∈R |ID|×N .(84)
Likewise, withbl :=e −Φ(xl)/ρ0(xl)forx l ∈I ∂D and(K ∂D )li :=κ(x l, xi), the boundary condition
can be written asK∂D c=b. We then consider the following regularized optimization problem
min
c∈RN
∥SD c∥2 +λ c⊤Kc
s.t.K ∂D c=b,(85)
forλ≥0, andK∈R N×N is the Gram matrix,K ii′ =κ(x i, xi′ ), so thatc ⊤Kc=∥w∥ 2 Hk. Here,
the boundary condition is imposed exactly, while the interior residual is minimized in the least
squares sense with Tikhonov regularization. Here, (85) is again an equality-constrained convex
quadratic program. We define the Lagrangian∥SDc∥2 +λc ⊤Kc+ 2µ ⊤(K∂D c−b), and obtain the
KKT condition, which is a linear system incand the Lagrange multiplierµ

S⊤ DSD +λK K ⊤ ∂D
K∂D 0
!
c
µ
!
=

0
b
!
.(86)
Withcdetermined by (86), applying the chain rule tolog ˆρ= logρ 0 + logwwithρ 0 in (21), we
obtain (22).
F Reweighting the Generated Paths
The controlled dynamics (9) generate transition paths more efficiently than the reference dynamics,
but at the price of sampling from a tilted path measure rather than the reference one. To fix this,
first consider starting from some initial conditionx∈D. Recall thatPx is the path measure of (1)
started atx, and ˜P ∗,x is that of the optimally controlled process (9) started atx. By Girsanov’s
theorem,P x and ˜P ∗,x are equivalent masures on the common path spaceΩ. Letχ∈Ωbe a generic
element of the path space. By Lemma 4, we have
d ˜P ∗,x
dP x = e−H(χ) ρ(x) ,(87)
25

whereρ(x) =E x[e−H ], andH(χ) := R ˜τD 0 f(˜xt)dt+Φ(˜x˜τD ). Hence, thecorrectionfromthecontrolled
process (9) to the original process (1) at a fixed start is simplyρ(x)eH(χ).
When the initial conditions are drawn from a probability measureνon the source setAi, e.g.,
the Boltzmann measure restricted toAi, consider the mixture
M(·) =
Z
Ai
P x0(·)ν(dx 0), ˜M(·) =
Z
Ai
˜P ∗,x0(·)ν(dx 0).(88)
BothMand ˜Mshare the same initial distributionν. Since every path starts from its own initial
conditionx 0 =χ(0), we have
d ˜M
dM = d ˜P ∗,χ(0) dP χ(0) = e−H(χ) ρ  χ(0)  .(89)
Hence, to map ˜Mback toM, each path is weighted bydM/d ˜Mby Lemma 4. From (89) and
replacingρbyˆρin (21), we can approximate it as
weight(χ) = dM
d ˜M = ˆρ

˜x0

eH(χ) ,˜x 0 :=χ(0).(90)
Here,ˆρ(˜x0)is given by (21).
We further note that asβ→ ∞, the probability that a sampled path spends more than an
arbitrary fixed timeε >0in nonreactive regions tends to zero. To see this, recall from Example 1
thatH=βH 0. From (87), we have
˜P ∗,x(H0 > ε) =Ex

e−βH01{H0 > ε} 
Ex [e−βH0] ≤ e−βε Ex [e−βH0]
≤ e−βε
Ex [e−βH01{H0 ≤ε/2}]
≤ e−βε/2
P x(H0 ≤ε/2) ,
(91)
forε >0withP x(H0 ≤ε/2)>0. Here, the first inequality follows frome−βH0 ≤e −βε on{H 0 > ε}.
Takingβ→ ∞, we have˜P ∗,x(H0 > ε)→0.
G Experiment Details and Additional Examples
G.1 The Double-Well System
For the two-dimensional double-well system, the drift and diffusion coefficients in (1) are specialized
asb(x) =−∇U(x), with
U(x, y) =1 6

4(1−x 2 −y 2)2 + 2(x2 −2) 2 +  (x+y) 2 −1 2 +  (x−y) 2 −1 2 −2  ,(92)
andσ(x) =σ 0Iwithσ 0 =
p
2kBTemp ≈0.455atT emp = 1200 K. Its potential has two minima
at(±
√
5/2,0)and two channels around(0,±1). Following Algorithm 1, we compute the Koop-
man eigenfunctions and extract the metastable coresAleft andA right as described in Section 4.1.
Specifically,A left andA right are obtained by retaining those points whose spectral embedding lies
within radiusε= 0.5of its cluster centroid. We sample1000uncontrolled and1000controlled
26

paths, all initialized at the minimum ofAleft. A path is a hit at its first entrance toAright, and is
truncated at the numerical censorTmax otherwise. We use a step size of∆t= 0.01, andTmax = 10,
equivalently, a budget ofTmax/∆t= 1000integration steps, andβ= 1. We adopt two metrics to
evaluate performance: the target hit percentage (THP), which measures the proportion of trajec-
tories that successfully reach the target beforeTmax; and the energy of the transition state (ETS),
which measures the maximum potential energy along each transition path. As shown in Figure 1
and Table 1, the controller raises the THP from0%to99.8%, and the controlled ensemble retains
both channels rather than collapsing onto one.
Table 1: Target hit percentage (THP) and energy of the transition state (ETS) for the 2-channel
double well. Uncontrolled and controlled rows are measured in our setup; TPS-DPS values are as
reported by Seong et al. (2025).
Method THP (↑) ETS (↓)
% kJmol −1
Uncontrolled (1200K)0.0–
Uncontrolled (2400K)2.7 1.73±0.42
Uncontrolled (3600K)18.8 2.07±0.46
Uncontrolled (4800K)42.1 2.49±0.66
TPS-DPS (1200K)99.9 1.38±0.16
Proposed method (1200K)99.81.40±0.11
G.2 Muller-Brown Potential
The Müller-Brown potential (Müller and Brown, 1979) is described by
U(x, y) = 1 10 4X k=1 Ak exp  ak(x−x k)2 +b k(x−xk)(y−y k) +c k(y−y k)2 ,(93)
with parameters specified as


A1 a1 b1 c1 x1 y1
A2 a2 b2 c2 x2 y2
A3 a3 b3 c3 x3 y3
A4 a4 b4 c4 x4 y4

 =


−200−1 0−10 1 0
−100−1 0−10 0 0.5
−170−6.5 11−6.5−0.5 1.5
15 0.7 0.6 0.7−1−1

 (94)
We consider a particle withm= 12a.m.uandγ= 1ps −1. As shown in Figure 2, the dynamics
has one deep well at(−0.558,1.442), a medium-deep well at(0.623,0.028), and a shallow well sitting
between the two at(−0.050,0.467). The goal is to transition from the deep well to the medium well.
The source and target cores are defined with radiusε= 0.2. We choose a stepsize of∆t= 0.002ps
andT max = 10ps. We use a Gaussian kernel with bandwidth0.35. At temperatureTemp = 200K,
the controller raises the THP from1.8%for the uncontrolled process to99.0%.
G.3 Alanine Dipeptide
We simulate alanine dipeptide (ACE–ALA–NME) in vacuum with AMBER99SB-ILDN, hydrogen-
bond constraints, and the VVVR integrator at300 K, friction10 −3 fs−1, and timestep1 fs. Tra-
jectories start from the energy-minimizedC5structure. Following (Seong et al., 2025), the target
27

Table 2: Müller-Brown benchmark atT= 150 Kand200 K.
Method THP (↑) ETS (↓)
% kJmol −1
Uncontrolled (150K)0.1 12.4
Uncontrolled (200K)1.8 14.0±1.3
TPS-DPS (150K)100 15.9±3.5
TPS-DPS (200K)100 15.7±1.9
Proposed method (150K,β= 1)95.1 14.1±2.1
Proposed method (150K,β= 2)95.9 14.3±2.1
Proposed method (200K,β= 1)98.4 14.5±2.1
Proposed method (200K,β= 2)99.014.5±2.1
is defined asB={R| ||ξ(R)−ξ(R B)||<0.75}(in radians), whereξ= (ϕ, ψ)are the backbone
dihedral angles andRB is the energy-minimizedC7 ax structure. A trajectory stops when it enters
Bor reachesT max = 1ps.
The controllerˆu=∇log ˆρis evaluated on the Kabsch-aligned Cartesian configuration and
applied as an external forceFbias =sˆuin OpenMM, withs= 30 kJ mol −1nm−1 and∥ˆu∥capped
at75 kJ mol −1nm−1 per atom. We useβ= 1, Gaussian bandwidth1, andε= 0.01, with80kernel
centers and400interior and48boundary collocation points. OpenMM integrates the underdamped
Langevin dynamics
dxi = pi mi dt, dp i =F i(x)dt−γ ipidt+ p 2miγikBT dWi,
whereiindexes the atom. In this experiment, we solve the boundary value problem (11) with the
isotropic generatorL=F· ∇+ σ2 0 2 ∆whereFis the force andσ 0 = 1as an approximation of the
simulated dynamics that ignores the per-atom mobility1/(miγ).
The proposed pipeline as summarized in Algorithm 1 runs once: Koopman eigenfunctions are
constructed via a generalized eigenproblem in terms of Gram matrices (see, e.g., (Hou et al., 2023,
Appendix M) for details), followed by solving forˆqandˆu. In contrast, the baselines in (Seong et al.,
2025) repeatedly simulate controlled trajectories and update the neural network, so they pay the
sampling cost per rollout. Table 3 compares the cost of obtaining the bias in the drift term. All
timings are measured on a single NVIDIA A100 GPU.
G.4 Additional Experiment: The Four-Well Dynamics
Consider the two-dimensional four-well potential described by
U(x, y) = 5((x2 −1) 2 + (y2 −1) 2),(95)
which has four symmetric local minima at(±1,±1). The source core is centered at pair(−1,−1)
and the target core is centered at(1,1), with radiusε= 0.3. We use massm= 12a.m.u, friction
γ= 1ps −1, stepsize∆t= 0.002ps, andT max = 10ps. Results for various settings are reported in 4,
and the sampled paths at200 Kare shown in Figure 6.
28

Figure 4: Alanine dipeptide on the Ramachandran plain of backbone dihedral angles(ϕ, ψ). (Left)
The first nontrivial Koopman eigenfunctionψ 1 which separates theC5basin fromC7 ax basin.
(Right) The committorqfromC5toC7 ax.
(a) Uncontrolled
 (b) TPS-DPS
 (c) Proposed method
Figure 5: Sampled transition paths for alanine dipeptide in vacuum, same as Figure 3 in Section 5.
Paths start in theC5basin (upper left) and end in theC7 ax basin (red star). (a) Uncontrolled
paths. (b) TPS-DPS (Seong et al., 2025): THP= 100%, obtained by training a neural-network bias
with simulation in the loop (1000rollouts,∼10 6 gradient updates). (c) Proposed method: THP
= 93%, with a closed-form controller.
Table 3: Cost of obtaining the controller on alanine dipeptide on a single NVIDIA A100 GPU,
excluding the subsequent path generation, which is common to all methods.
Proposed method
Stage Time (s) Total (s)
Sampling Direct evaluation of (3)
180Koopman eigenpairs 73.8 Committorˆq56.2
Controllerˆu51.0
Training-based baselines
Method Rollouts×(Sampling (s)+Training (s))=Total (h)
TPS-DPS (F) 1000×(60.6+14)=20.7
PIPS (F) 15000×(60.6+5.4)=275
29

(a) Uncontrolled
 (b) TPS-DPS
 (c) Proposed method
Figure 6: Four-well dynamics atT= 200 K. We aim to sample transitions from the source core at
(−1,−1)(green star) to the target core at(1,1)(red star). (a) Uncontrolled paths: THP(Tmax) =
0.9%. (b) TPS-DPS (Seong et al., 2025): THP(Tmax) =81.6%. (c) Proposed method withβ= 2:
THP(Tmax) =94.7%.
Table 4: Four-well benchmark atT= 200 Kand300 K.
Method THP (↑) ETS (↓)
% kJmol −1
Uncontrolled (200K)0.9 10.6±3.2
Uncontrolled (300K)8.8 12.8±3.6
TPS-DPS (200K)81.6 8.6±.9
TPS-DPS (300K)87.1 10.2pm.6
Proposed method (200K,β= 1)73.2 9.5±1.8
Proposed method (200K,β= 2)94.7 9.0±1.8
Proposed method (300K,β= 1)91.8 11.2±3.1
Proposed method (300K,β= 2)100.010.4±2.5
30
