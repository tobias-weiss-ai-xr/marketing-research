---
title: Asynchronous Cooperative Online Learning for Multi-Robot Control under Computational Delays
url: https://arxiv.org/abs/2608.29562
category: ai-marketing
subcategory: measurement
date: 2026-08
venue: ''
authors:
- Xiaobing Dai
- Zewen Yang
- Wei Ren
- Sandra Hirche
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.29562
pages: 10
chars: 55505
fetched_at: '2026-11-08T13:28:50+00:00'
kb_version: 1
---

# Asynchronous Cooperative Online Learning for Multi-Robot Control under Computational Delays

1
Asynchronous Cooperative Online Learning for
Multi-Robot Control under Computational Delays
Xiaobing Dai, Zewen YangMember, IEEE, Wei Ren,Fellow, IEEE, Sandra Hirche,Fellow, IEEE
Abstract—Ensuring the safe operation of multi-agent systems
(MASs) under uncertain environments is crucial for cooperative
robotic, where external disturbances and inaccurate dynamic
models can significantly compromise performance and reliability.
To address this challenge, calibrated machine learning models,
particularly Gaussian process (GP) regression, are extensively
employed due to their interpretable performance quantification.
As the interconnected communication of MASs facilitates cooper-
ative learning, agents are able to enhance learning performance
by exchanging local GP inferences with their neighbors and ag-
gregating the received information via distributed GP strategies.
However, variations in computational power and prediction tasks
among agents inevitably lead to heterogeneous computational
delays and differences in query points, which are often overlooked
in existing aggregation methods. To overcome these limitations,
this work proposes an asynchronous cooperative learning strategy
that explicitly accounts for prediction accuracy, query point
variations and delay effects. Additionally, a distributed control
law based on an adjoint MAS is developed to ensure the
desired control performance. Simulations on unmanned surface
vehicles validate the effectiveness of the proposed approach,
demonstrating substantial improvements in both learning and
control performance compared to the state-of-the-art approaches.
Index Terms—Cooperative learning, heterogeneous computa-
tional delay, Gaussian process regression, online learning
I. INTRODUCTION
A. Background
Safety-critical multi-agent system (MAS) control has drawn
large attention in robotics including applications in unmanned
vehicles [1] and manipulators [2], where individual robots
cooperate with each other to accomplish tasks such as con-
sensus [3], formation [4], coverage [5], [6] and optimization
[7]. However, the exact agent dynamics is often hard to
obtain because of high model complexity and environmental
uncertainties, imposing challenges for designing model-based
controllers [8]. To this end, machine learning (ML) techniques
are employed on each agent to predict unknown components
in its dynamics based on collected data.
This work was supported by the Federal Ministry of Education and
Research of Germany in the programme of “Souver ¨an. Digital. Vernetzt.”
under joint project 6G-life with project identification number: 16KISK002.
(Corresponding author: Zewen Yang.)
Xiaobing Dai and Sandra Hirche are with the Chair of Information-oriented
Control, Technical University of Munich, 80333 Munich, Germany (email:
xiaobing.dai, hirche@tum.de).
Zewen Yang is with the Chair of Robotics and Systems Intelli-
gence, Technical University of Munich, 80992 Munich, Germany (email:
zewen.yang@tum.de).
Wei Ren is with the Department of Electrical and Computer Engineering,
University of California at Riverside, Riverside, CA 92521 USA (e-mail:
ren@ece.ucr.edu).
B. Related Works
Notably, the dependency of high prediction accuracy and
better control performance for MASs is demonstrated in many
existing studies [9]. Consequently, cooperative learning is a
promising methodology that leverages inter-agent collabora-
tion to improve learning quality [10]. Specifically, cooperative
neural network (NN)-based MAS control is extensively studied
[11], assuming that the unknown system is approximated as a
linear combination of predefined nonlinear features. However,
the accuracy of NN relies on the choice of nonlinear features
[11]. Practical quantification of prediction error remains an
open challenge, where only overly conservative results exist
[12], limiting its applications in safety-critical scenarios.
Gaussian process (GP) regression-based cooperative learn-
ing is another popular approach due to its modeling flexibility
for arbitrary continuous functions [13] and interpretable er-
ror quantification [14], [15]. Cooperative GPs require agents
sharing their predictions with neighbors and aggregating re-
ceived neighbor predictions [10]. However, these aggrega-
tion techniques demand that agents compute predictions for
the neighboring agents, leading to significant local computa-
tional burden. Moreover, some resource-efficient distributed
GPs are investigated recently for multi-agent systems [16]–
[18]. Similarly, decentralized GP frameworks such as nested
GPs [19] enable cooperative learning across multiple agents
with limited communication. While these approaches focus
on computational efficiency, scalability and communication
constraints, they typically assume that predictions are syn-
chronously available or do not explicitly account for the
impact of computational delays. Notably, when computational
delays are considered in existing cooperative GP approaches,
the predictions received from neighbors, which are derived
from their local data, arrive in a delayed manner. However,
only few works take the limitation on local computational
power into account. Although cooperative learning enhances
predictive performance through information sharing, its ac-
curacy depends on the quality of each agent’s individual
GP model. To ensure desired learning performance during
operation, the effectiveness of online cooperative learning is
shown in the previous works [20], allowing individual GP
models to be updated with newly collected data. However,
the high computational intensity of online learning induces
non-negligible computational delays.
The learning-based MAS control with delays has drawn
huge attention, but existing research focuses only on the
communication delays [21]. Unlike well-understood hetero-
geneous communication delays, which allow continuous data
arXiv:2608.29562v1  [cs.LG]  30 Aug 2026

2
transmission with different time shifts, computational delay di-
rectly blocks additional operations during execution [22]. This
difference prevents the straightforward extension of existing
results to the setting with computational delays from machine
learning. Consequently, the problem of computational delays
in cooperative online learning-based MAS control remains
unexplored, and only few preliminary works [23] explored
the effect of delayed learning in a single-agent system. Specifi-
cally, the computational delay induced by GP regression is first
analyzed in [22], revealing the coupled effect of prediction
accuracy and computational delay on control performance.
However, the extension to MAS with distributed cooperative
GP is nontrivial due to different computational power and pre-
diction tasks across agents. Therefore, it is urgent to investigate
a cooperative online learning-based distributed control strategy
for MAS under heterogeneous computational delays.
C. Contributions
In this paper, the main contributions are the answers to
the following three questions, which are induced by hetero-
geneous computational delay in cooperative online learning-
based multi-agent system control.
Q1Can the delayed prediction from neighboring agents
improve individual learning performance?
Q2How to properly utilize the asynchronous predictions from
neighbors with different query points?
Q3How to design a distributed controller leveraging asyn-
chronous cooperative online learning?
Q4Does the proposed controller have a formal guarantee on
control performance in MASs?
Here, we focus on a MAS modeled in the Euler-Lagrange form
with unknown disturbances motivated by robotics and mecha-
tronic systems, whose control objective is to achieve a second-
order consensus. GP regression is deployed on each agent to
predict unknown components using a data set, which is online
updated with newly collected measurements. Moreover, each
GP model only computes and shares the predictions of its
own state with neighbors, avoiding the inference of unknown
dynamics based on neighbors’ states as in [10]. To aggregate
received predictions, an asynchronous distributed cooperative
learning strategy is proposed for MASs, which accounts for
prediction accuracy, query point difference, and delay effects.
Furthermore, a distributed control law is devised based on an
introduced adjoint MAS and the proposed cooperative online
learning strategy, guaranteeing the achievement of practical
second-order consensus. The effectiveness of the coopera-
tive learning and distributed control strategy is demonstrated
through simulations on unmanned surface vehicles, highlight-
ing improvements in both learning and control performance.
D. Graph Theory
The communication network amongN∈N + agents is
modeled as an undirected graphG={V,E}, with the vertex
setV={1,· · ·, N}and the edge setE ⊂ V × V. Specifically,
(i, j)∈ Eindicates the existence of a communication channel
between agentiandjfor anyi, j∈ V. The communication
graph is characterized by adjacent matrixA∈R N×N ,
whose entriesa i,j at thei-th row andj-th column are set
asa i,j =a j,i = 1if(i, j)∈ E, anda i,j =a j,i = 0otherwise.
The neighbor set of agentiis defined asN i ={j∈ V|ai,j ̸=
0} ⊂ V. Moreover, the input degree matrix is defined as
D= diag(d 1,· · ·, dN )withd i = PN j=1 ai,j for anyi∈ V, so
that the Laplacian matrix is written asL=D−A∈R N×N .
II. PROBLEMSETTING
A. Problem Formulation
In this paper, a homogeneous MAS withN∈N + agents is
considered, where the dynamics of each agenti= 1,· · ·, N
in Euler-Lagrange form is written as
M(q i(t)) ¨qi(t) +C([q T i (t), ˙qT i (t)]T ) ˙qi(t) +g(q i(t))(1)
=τ i(t) +d([q T i (t), ˙qT i (t)]T ),
whereq i ∈X q,0 ⊂R n and ˙qi ∈X q,1 ⊂R n denote the
generalized coordinate and velocity of robotiforming the
agent statex i = [q T i , ˙qT i ]T ∈X⊂R 2n with dimensionn∈
N+. The known mass matrixM(·) :X q,0 →R n×n, Coriolis
force matrixC(·) :X→R n×n and gravity force vectorg(·) :
Xq,0 →R n are obtained from nominal robot dynamics. The
control input of the agent dynamics (1) denotesτ i ∈R n. The
unknown continuousd(·) :X→R n encodes all uncertainties,
which is assumed identical to all agents. Moreover, the system
(1) satisfies the following assumption.
Assumption 1:There exists strictly positive constantM ∈
R+ such thatσ (M(q))≥1/M for anyq∈X q.
Assumption 1 only requires the positive definite of the mass
matrixM(q)for anyq∈X q, which is satisfied in most
engineering applications including underwater vehicles [1] and
manipulators [2]. Assumption 1 guarantees that the inertia
matrixM(q i)remains uniformly positive definite for all
admissible configurations, which ensures the uniform nonsin-
gularity and well-posedness of (1). Therefore, this assumption
imposes no practical restriction.
The agents communicate through a network modeled as an
undirected graphG, which satisfies the following assumption.
Assumption 2:The undirected graphGis connected.
Assumption 2 is common in many MAS control literature,
e.g., [9], which allows the information of each agent to be
transmitted to other agents within finite steps.
The control task is to achieve second-order approximate
consensus, which is mathematically formulated as follows.
Definition 1:A second-order multi-agent system with (1)
achieves approximate consensus, if there exit well-defined
positive constantsϵ 0, ϵ1 ∈R 0,+ such that
limt→∞ ∥qi(t)−q j(t)∥ ≤ϵ0,lim t→∞ ∥ ˙qi(t)∥ ≤ϵ1 (2)
hold for anyi, j∈ Vandi̸=j.
Classical second-order consensus formulations typically re-
quire asymptotic agreement of both positions and velocities,
allowing the common velocity to be nonzero [24]. In contrast,
Definition 1 additionally enforces convergence of all agent ve-
locities ˙qi to zero. This formulation avoids persistent collective
drift in robotic coordination tasks [25] and achieves stationary
consensus behavior for the considered system (1). Moreover,

3
the approximate consensus in Definition 1 is widely studied in
MAS [26], [27], where agents are required to reach agreement
within a bounded tolerance. In this work, the approximate
consensus is considered due to the uncertain dynamics (1) and
practically non-vanishing estimation error for unknownd(·).
Remark 1:The generalized coordinatesq i in (1) are
not restricted to physical Cartesian positions and may also
represent abstract coordination variables, such as manipulator
joint configurations or task-space synchronization states. Even
whenq i are the Cartesian positions, collision-free coordination
can be interpreted through offset consensus, where consensus
ofq i yields constant relative distances between agents. Con-
sequently, physical collisions are avoided while preserving the
same stability analysis framework.
B. Data-driven Distributed Control
To achieve the second-order approximate consensus in Def-
inition 1, a distributed control law is designed as
τi(t) =τ s,i(∪j∈{i,Ni}xj) +τ m,i(xi) +τ c,i(t)− ˆdi(t)(3)
for∀i∈ V, where the consensus lawτ s,i(·)and the model
related feedforward termτ m,i(·)are written as
τs,i(∪j∈{i,Ni}xj) =−M(q i)(c0eq,i +c 1 ˙eq,i),(4)
τm,i(xi) =−M(q i)(c3 ˙qi +c 2qi) +C(x i) ˙qi +g(q i)(5)
with the consensus errore q,i = P j∈Ni (qi −q j). The correc- tion termτ c,i(·)from the proposed adjoint MAS is designed
later in Section IV-A, and the functions ˆdi(·) :R 0,+ →R n
serve as compensation terms ford(x i(·)),∀i∈ V. The control
gainsc i ∈Rwithi= 0,· · ·,3are designed to satisfy the
conditions derived later in Lemma 4.
Remark 2:The proposed control framework (3) consists of
4components. The consensus termτ s,i is inspired by second-
order consensus protocols [24], [25], and is based on position
and velocity consensus errors. The model-based termτ m,i
follows the classical computed-torque control [28], which is
widely employed to compensate for known system dynamics.
The disturbance compensation ˆdi(t)is obtained via machine
learning as shown in [20]. Notably, the proposed approach
differs from these methods by explicitly accounting for asyn-
chronous online learning with heterogeneous computational
delays. Finally, the correction termτ c,i is newly introduced in
this work. It is constructed based on an adjoint multi-agent sys-
tem that serves as a reference, together with an additional com-
ponent designed to mitigate the query mismatch from asyn-
chronous learning. Further details are provided in Section III.
Specifically, ˆdi(t)is estimated by agenti∈ Vusing an
online ML with time-varying data setsD i(t), which denotes
Di(t) ={x i(ti,k),y i(ti,k)}k=ki(t),···, ¯ki(t),(6)
leading to|D i(t)| ≤ ¯N∈N +,∀t∈R 0,+ with ¯N∈N +.
The discrete time sequence{t i,k}k∈N comprises the time
instances at which the ML model on agentibecomes avail-
able for next computation, which is defined ast i,0 = 0,
ti,k+1 =t i,k + ∆ i(ti,k),∀k∈N, where∆ i(ti,k)is the
computation time for ML initiated att i,k on agenti. The index
function ¯ki(·) :R 0,+ →Nin (6) returns the closest index of
Figure 1: Block diagram of the proposed distributed control
framework with asynchronous cooperative online learning,
where the blue lines indicate the signal to be transmitted to
neighbors and the red lines shows the information received
from neighbors. The dashed dot line infers the initialization
step implemented only once at timet= 0.
the time instances for new learning process on agenti, i.e.,
¯ki(t) = arg max k∈N{ti,k|ti,k + ∆i(ti,k)≤t,∀k∈N}with
ki(t) = max{0, ¯ki(t)− ¯N+ 1}. The vectory i ∈R n in (6)
is the noisy observation of unknownd(x i)evaluated atx i,
which satisfies the following assumption.
Assumption 3:The data pair{x i(ti,k),y i(ti,k)}is only
available on agenti∈ Vat time instancet i,k withk∈N,
wherey i(ti,k) =d(x i(ti,k))+wi(ti,k)with i.i.d measurement
noisew i(·) = [w i,1(·),· · ·, wi,n(·)]T . Moreover, it holds
|wi,p(ti,k)| ≤¯wp,∀p= 1,· · ·, nwith known¯wp ∈R +.
Assumption 3 ensures the local availability of data without
data sharing between agents. Moreover, Assumption 3 permits
noisy measurementsy i(·), which can be practically obtained
through numerical methods.
Motivated byQ1–Q4, the control objective of this paper is
formally stated as follows.
Problem:Consider the uncertain multi-agent system (1)
interconnected via an undirected communication graphG
satisfying Assumptions 1 and 2. The goal is to design an
asynchronous cooperative online learning strategy with hetero-
geneous computational delays∆ i(·)and to devise a distributed
learning-based control law, such that practical second-order
consensus in Definition 1 is achieved.
To address this problem, a distributed control framework is
proposed with asynchronous cooperative learning as in Fig. 1.
III. ASYNCHRONOUSCOOPERATIVEONLINELEARNING
In this section, a cooperative online learning strategy is
proposed to answerQ1andQ2, which concern the feasibility
and methodology of utilizing delayed neighboring predictions.
A. Gaussian Process Regression
To infer the unknown functiond(·) = [d 1(·),· · ·, dn(·)]T
in (1), GP regression is employed, which assumesd p(·)with
p= 1,· · ·, nbelongs to the reproduced kernel Hilbert space
(RKHS) corresponding to kernel functionsκ p(·,·) :X×X→
R0,+. Moreover, each unknown functiond p(·)and kernel
κp(·,·)withp= 1,· · ·, nsatisfy the following assumption.

4
Assumption 4:The kernel functionκ p(·,·)is stationary
and Lipschitz continuous, which indicates the existence of a
well-defined constantL κ,p ∈R 0,+ such that|κ p(x1,x)−
κp(x2,x)| ≤Lκ,p∥x1 −x 2∥for anyx 1,x 2,x∈X. More-
over, the unknown functiond p(·)has the bounded RKHS
norm with well-defined positive constant ¯dp ∈R 0,+, i.e.,
∥dp∥κp =⟨d p(·), dp(·)⟩1/2 κp ≤ ¯dp for anyp= 1,· · ·, n.
Assumption 4 is commonly found in most universal kernels
such as squared exponential kernel and Mat´ ern kernels.
Remark 3:The bounded RKHS norm in Assumption 4 is a
standard modeling assumption in GP when deriving prediction
error bounds [14], [15], which imposes the smoothness on the
unknownd p(·). In practice, the exact RKHS norm bound ¯dp is
typically unknown, but it can be conservatively approximated
using data-driven methods [15], [29], [30]. While a tighter
estimate of ¯dp leads to less conservative prediction error
bounds, the theoretical analysis in this paper remains valid
with any conservative upper bound. Investigating a tighter
bound ¯dp is an interesting direction for future work.
UtilizingD i(t)in (6) withy i(·) = [y i,1(·),· · ·, yi,n(·)]T
and measurement noise bound¯w p for each dimensionp, the
posterior meanµ p(x,D i(t))and varianceσ 2 p(x,D i(t))for
dp(·)withp= 1,· · ·, nat anyx∈Xdenote
µp(x,Di(t)) =κT p (x,Di(t)) ¯K−1 p (Di(t))ζp(Di(t)),(7)
σ2 p(x,Di(t)) =σ2 s,p −κT p (x,Di(t)) ¯K−1 p (Di(t))κp(x,Di(t)),
whereσ 2 s,p =κ p(x,x)is constant for anyx∈Xdue to
the stationary kernel. The kernel vector isκ T p (x,D i(t)) =
[κp(x,x i(ti,ki(t))),· · ·, κp(x,x i(ti,¯ki(t)))]T and the kernel
gram matrix is ¯Kp(Di(t)) =K p(Di(t)) + ¯w2 pI|Di(t)| with
Kp(Di(t)) = [κ p(xi(ti,k1 ),x i(ti,k2 ))]k1,k2=ki(t),···, ¯ki(t). The concatenated outputζ p(Di(t)),∀p= 1,· · ·, nis defined
asζ p(Di(t)) = [y i,p(ti,ki(t)),· · ·, yi,p(ti,¯ki(t))]T . As a cali- brated learning-based model, GP provides the posterior mean
µp(·,D i(t))as the estimation ofd p(·)on agenti∈ Vat time
t∈R 0,+, and the posterior varianceσ 2 p(·,D i(t))for prediction
performance quantification as follows.
Lemma 1:Apply GP regression on agenti∈ Vto
estimated(·)satisfying Assumptions 3 and 4 with|D i(t)| ≤ ¯N. Then, the prediction error of concatenatedµ(x,D) =
[µ1(x,D),· · ·, µn(x,D)] T is bounded by
∥d(xi(t))−µ(x i(t),D i(t))∥ ≤βσ(xi(t),D i(t))(8)
withx i(t)∈Xfor anyt∈R 0,+, whereβ= ( Pn p=1( ¯d2 p + ¯N)) 1/2 andσ(x,D) =∥[σ 1(x,D),· · ·, σn(x,D)] T ∥.
Proof:See appendix.
Remark 4:The prediction error bound in Lemma 1 is
deterministic and derived from RKHS properties under As-
sumption 3, rather than a probabilistic upper confidence bound
[14]. Instead of a confidence level, the coefficientβrepresents
a worst-case upper bound depending on the maximal size ¯N
ofD. Althoughβincreases with the data set size due to the
use of a distribution-independent bound, the varianceσ(·,·)
decreases as more informative samples are collected via online
learning [13]. Consequently, the overall prediction error bound
remains meaningful and captures the improvement in learning
accuracy through the reduction of uncertainty.
Moreover, we consider that the computational time of GP
is bounded and satisfies the following assumption.
Assumption 5:There exist well-defined constants∆ i ∈
R0,+ for alli∈ V, such that∆ i(ti,k)≤∆ i for anyk∈N.
The bounded∆ i(·)in Assumption 5 is resulted from the
bounded size ofD i(·)in (6), i.e.,|D i(ti,k)| ≤¯N,∀i∈ Vand
k∈N. In particular, using incremental Cholesky rank-one up-
dates allows a computational complexity∆ i(·)∼ O(|Di(·)|2)
for online GP [13]. Consequently, the computation time
remains uniformly bounded as in Assumption 5. While online
learning continuously collects new data samples, the data set
construction in (6) incorporates data deletion to maintain the
bounded|D i(·)|. Specifically, if|D i(t− i,k)|= ¯N, wheret − i,k
denotes the time instant immediately before the model update
att i,k, the oldest data pair is removed before adding the
newly collected sample. In practice, computational efficiency
can be improved using e.g., LoG-GP [31] and Sky-GP [32].
Remark 5:The proposed framework explicitly models
computational delays induced by online GP inference and
model updates with complexityO( ¯N 2). Communication
delays (∼1ms, [2]) between agents are assumed negligible
relative to the computation delay (>50ms, [32]). Extending the
framework to simultaneously account for both computational
and communication delays is considered as future work.
For notational simplicity, defineµ i(k)=µ(xi(ti,k),Di(ti,k)),
becausex i andD i always have the same time stamp.
B. Cooperative Learning with Delayed Predictions
Before presenting the proposed asynchronous cooperative
learning strategy, we first analyze the inference accuracy of
predictions to answerQ1. Specifically, we examine how well
the predictionµ j(kj(t))of agentj∈i∪ N i approximates the
true value of the unknown functiond(x i(t))at timet.
Lemma 2:Assume that GP models on all agentsi∈ V
satisfy Assumptions 3 and 4. Then, the prediction error
∥d(xi(t))−µ j(kj(t))∥,∀t∈R 0,+ is bounded by
∥d(xi(t))−µj(kj(t))∥≤ηi,j(t)=βσj(kj(t)) +Ld∥˜xi,j(t)∥
1
2,(9)
whereL d = (2 Pn p=1 ¯d2 pLκ,p) 1 2 , ˜xi,j(t) =x i(t)−x j(tj,kj (t))
andσ j(kj(t)) =σ(x j(tj,kj (t)),D j(tj,kj (t))).
Proof:See appendix.
The boundη i,j(t)in Lemma 2 extends the standard GP pre-
diction error bound in Lemma 1 by incorporating an additional
term which accounts for misalignment between agents.
Remark 6:The square-root dependence on the state mis-
match ˜xi,j in Lemma 2 originates from the RKHS norm
bound in Assumption 4, and differs from linear Lipschitz
bounds. In contrast to classical Lipschitz conditions, Lemma 2
implies H ¨older continuity of order1/2ford(·). This relaxes
the requirement of bounded derivatives, which is practically
difficult to obtain. Moreover,this square-root form leads to
sublinear growth for large mismatches, since∥ ˜xi, j∥1/2 <
∥ ˜xi, j∥when∥ ˜xi, j∥>1. However, it also implies a slower
decay rate near equilibrium, as∥ ˜xi, j∥1/2 >∥ ˜xi, j∥when
∥ ˜xi, j∥<1. Consequently, the convergence rate of the error
bound becomes locally slower.

5
With the saved predictionsµ j(kj(t))from agentsj∈ N i,
the compensation ˆdi(t)in (3) is designed as the aggregation
of all stored predictions to addressQ2, which is written as
ˆdi(t) = X j∈{i,Ni} ωi,j(t)µj(kj(t)),(10)
whereω i,j(·) :R 0,+ →[0,1]⊂Rare the time-varying
aggregation weights for the prediction from agentjused on
agenti. In this paper, the construction ofω i,j(·)is inspired
by the generalized Product-of-Experts (gPoE, [33]), where
predictions associated with smaller GP uncertainty and smaller
query-point mismatch receive larger aggregation weights.
Specifically, the aggregation weightω i,j(·)is designed as
ωi,j(t) =
ω∗ i,jρi,j(t)η−2 i,j (t) P
s∈{i,Ni} ω∗ i,sρi,s(t)η−2 i,s (t) ,(11)
whereω ∗ i,j ∈R 0,+ are pre-defined constants to show the prior
confidence of GP modelsjon agenti. The termρ i,j(t) =
γ(ηi,j(t)−βσ s),∀i, j∈ Vwithσ s = (Pn p=1 σ2 p) 1 2 and¯η∈
R+ reflects the informativeness [33], whereγ(·) :R→ {0,1}
is the Heaviside step function.
Remark 7:The weightsη i,j(t)are directly computable
online for allt∈R 0,+, since it depends only on the locally
available statex i(t)and the delayed neighboring information
xj(tj,kj (t)), σj(kj(t))transmitted by agentj∈ N i.
To quantify the accuracy of the aggregated prediction, we
present the following theorem.
Theorem 1:Let all Gaussian process models in all agents
satisfy Assumptions 3 and 4, and apply the aggregation
strategy as in (10) and (11). Then, the prediction error of each
agenti∈ Vis bounded for anyt∈R 0,+ by
∥d(xi(t) )−ˆdi(t)∥≤˜ηi(t)=ω∗ i X j∈ {i,Ni} ω∗ i,jρi, j(t)η−2 i, j(t) −1 2 ,(12)
whereω ∗ i = (P j∈{i,Ni} ω∗ i,j)1/2.
Proof:See appendix.
Theorem 1 shows a time-varying estimation error bound
˜ηi(·)for the aggregated prediction, whose value is related
toη i,j(·)from agentiand its neighborsj∈ N i for all
i∈ V. It is important to note that Theorem 1 does not aim
to establish posterior contraction or asymptotic convergence
of GP models. Such results typically rely on aggregation at
identical query points or synchronous prediction, which are
not applicable under the heterogeneous asynchronous compu-
tational delays considered in this work. Instead, Theorem 1
provides a control-oriented guarantee that directly enables the
stability and performance analysis in Section IV.
IV. DISTRIBUTEDSECOND-ORDERCONSENSUSCONTROL
This section answers the questionQ3about the control law
design. Specifically, the correction termτ c,i(·),∀i∈ Vin (3)
is devised in Section IV-A. Then, the performance of MAS is
analyzed in Section IV-B to answerQ4.
A. Adjoint Multi-agent System and Correction Input
In this subsection, the control law (3) is completed by
specifying the correction termτ c,i(·)for all agentsi∈ V. We
design the control correction input termτ c,i(·)by constructing
an adjoint MAS composed ofNagents as
¨¯qi =−¯c0 ¯eq,i −¯c1 ˙¯eq,i −¯c3 ˙¯qi (13)
with joint agent coordinate ¯qi ∈X q ⊂R n, adjoint consensus
error defined by ¯eq,i = P j∈Ni ( ¯qi − ¯qj), and the initial state
values are ¯qi(0) =q i(0), ˙¯qi(0) = ˙qi(0). The choice of
gains¯c0,¯c1,¯c3 ∈Rdetermines the performance of the adjoint
system (13) as shown below.
Lemma 3:Consider an adjoint MAS (13) withNagents
and any topology. Choose¯c 0,¯c1,¯c3 ∈R + satisfying¯c1¯c3 ≥
¯c0, then the adjoint MAS (13) achieves second-order consen-
sus defined in Definition 1 withϵ 0 =ϵ 1 = 0.
Proof:See appendix.
Due to the absence ofd(·)in (13), the adjoint MAS
achieves second-order consensus asymptotically as shown in
Lemma 3. Considering the introduced adjoint MAS, we design
the correction termτ c,i(·)in (3) for each agentias follows
τc,i(t) =M(q i(t))
¨¯qi(t) +c 0 ¯eq,i(t) +c 1 ˙¯eq,i(t)(14)
+c 2 ¯qi(t) +c 3 ˙¯qi(t)  −τ ε,i(t)
with positive constantc 2 ∈R + and
τε,i(t) =Ldω∗ i sign(M −T(qi) ˙εq,i)(15)
×
X
j∈{i,Ni}
(∥xi(t)−x j(t)∥/ω∗ i,j) 1 2 ,(16)
whereε q,i =q i − ¯qi and ¯xi(t) = [ ¯qT i (t), ˙¯qT i (t)]T .
B. Analysis of Learning-based Control Performance
The control performance is investigated for the proposed
controller (3) to answerQ4in Section I. The introduced
adjoint MAS serves as an ideal reference dynamics, assuming
the unknownd(·)is exactly canceled. The proposed learning-
based controller (3) then seeks to drive the actual system
toward this ideal reference behavior despite delayed GP pre-
dictions. This construction is conceptually related to certainty-
equivalence control [34] and backstepping [35], where stability
analysis is performed through the tracking error between the
actual and adjoint systems. Specifically, considering the MAS
(1) with the proposed control law (3), (4), (5) and (14), the
controlled agent dynamics of the agenti∈ Vis written as
¨qi = ¨¯qi −c 0 ˜eq,i −c 2εq,i −c 1 ˙˜eq,i −c 3 ˙εq,i +M −1(qi)(d(xi)−
ˆdi(t)−τ ε,i(t)), for alli∈ V, whereε q,i =q i − ¯qi and
˜eq,i =e q,i − ¯eq,i = P j∈Ni (εq,i −ε q,j ). Moreover, denote
the concatenation ofε q,i,∀i∈ Vbyε q = [εT q,1,· · ·,εT q,N ]T ∈
RnN , whose dynamics is ¨εq =−((c 0L+c 2IN )⊗I n)εq −
((c1L+c 3IN )⊗I n) ˙εq +M −1 G (q)(dG(x)− ˆdG(t)−τ ε,G(t))
withM G(q) = blkdiag(M(q 1),· · ·,M(qN ))∈R nN×nN ,
dG(x)=[dT (x1),· · ·,dT (xN )]T ∈R nN , ˆdG = [ ˆdT 1 ,· · ·,ˆdT N ]T ∈
RnN andτ ε,G = [τT ε,1,· · ·,τT ε,N ]T ∈R nN . Considering thatε i
in (15) is also written asε i = [ε T q,i, ˙εT q,i]T , the dynamics of
the concatenation forε i, i.e.,ε= [ε T 1 ,· · ·,εT N ]T ∈R 2nN , is
˙ε(t) =Φε(t)+B(q(t))(d G(x(t))− ˆdG(t)−τ ε,G(t)),(17)

6
whereΦ=Φ s⊗In∈R2nN×2nN ,B(q)=  0nN×nN,M −T G (q) T ∈
R2nN×nN andΦ s=
 0N×N IN
−c0L−c2IN −c1L−c3IN

. The gains
ci withi= 0,· · ·,3are chosen as follows.
Lemma 4:Choosec 0,c1,c2,c3 ∈R +, such thatc 2 3 ≥4c 2 and
2c0 ≤c 1(c3 +(c2 3 −4c2) 1 2 ), thenΦin (17) is negative definite.
Proof:See appendix.
With the property ofΦin Lemma 4, the convergence of the
dynamics (17) is shown in the following lemma.
Lemma 5:Consider a controlled MAS (1) satisfying
Assumptions 1 to 5, where the coefficientsc i withi= 0,· · ·,3
and¯ci withi= 0,1,3satisfy Lemmas 3 and 4, respectively.
Then, the value ofε i,∀i∈ Vis ultimately bounded by
limt→∞ ∥εi(t)∥ ≤¯ε= 2λ−1M ∥θ∥,(18)
whereθ= [θ 1,· · ·, θN ]T . The entriesθ i ∈Rfori∈ Vdenote
θi =ω ∗ i  X j∈{i,Ni} ω∗ i,j(β¯σj +L d(2F∆ j) 1 2 )−2− 1 2 ,(19)
whereλ ∈R + denote the minimal eigenvalue of−Φand¯σ j =
(Pn p=1 ¯w2 p) 1 2 is the upper bound of posterior variance. The
constantF∈R + is defined asF= (2ε max,0 +ε 2 max,1)∥Φs∥+
M (ˆω¯η+ ¯τε,G) + ¯qmax, whereε max,0 =υ s max{ˆωM(¯η+
2(n∥x(0)∥)1/2)/λ,∥ε(0)∥},ε max,1 = 2ˆωυsM n1/2/λ,ˆω=P
i∈V
P
j∈{i,Ni} ˆωi,j,¯τε,G = 2ˆωn1/2((2εmax,0 +ε 2 max,1)1/2 +
∥x(0)∥1/2)andυ s =∥Q s∥∥Q−1 s ∥. The matrixQ s ∈R 2N×2N
is the orthogonal eigenvector matrix ofΦ s.
Proof:See appendix.
Lemma 5 shows the ultimate bound of∥ε i(·)∥,∀i∈ V.
Considering ¯xi(0) =x i(0), it holds∥ε i(t)∥ ≤¯ε,∀t∈R0,+.
Remark 8:The Lyapunov function adopted in Lemma 5 is
chosen for analytical tractability and explicit characterization
of the effects of GP uncertainty, asynchronous delays and co-
operative learning. Less conservative estimates may potentially
be obtained using matrix-weighted quadratic Lyapunov func-
tions associated with the system dynamics (1). Investigating
such tighter bounds is an interesting direction for future work.
Remark 9:The discontinuous sign function inτ ε,i intro-
duces chattering effects. The amplitude of this term is related
to the state mismatch between agents, which satisfies
∥xi(t)−x j(t)∥ ≤∥εi(t)∥+∥ε j(t)∥+∥ ¯xi(t)− ¯xj(t)∥
≤2¯ε+∥¯xi(t)− ¯xj(t)∥,(20)
considering Lemma 5. This also leads tolim t→∞ ∥xi(t)−
xj(t)∥ ≤2¯εdue to the asymptotic consensus in Lemma 3.
Moreover, the value of¯εdepends on the prediction error bound
β¯σi and the computational delay∆ i, indicating that improved
learning accuracy and reduced delay lead to smoother control
inputs. To reduce chattering,sign(·)can be replaced by smooth
approximations, such as saturation [36] or hyperbolic tangent
functions [37]. These methods introduce a small residual
approximation error near zero, which slightly relax the ro-
bustness while improving control smoothness.
With Lemmas 3 and 5, we are ready to present the perfor-
mance analysis of the proposed distributed control law with
asynchronous cooperative online GP regression as follows.
Theorem 2:Consider a MAS with unknown dynamics
(1) satisfying Assumptions 1 and 2, where the unknown
nonlinearity is estimated using the proposed asynchronous
cooperative learning approach (10) with GP models satisfying
Assumptions 3 to 5. If the MAS is controlled by the proposed
control law (3) with (4), (5) and (14), which is calculated by
introducing a adjoint MAS (13) with coefficients satisfying
Lemmas 3 and 4, the second-order approximate consensus
defined in Definition 1 is achieved withϵ 0 = 2¯εandϵ 1 = ¯ε.
Proof:See appendix.
Theorem 2 shows the approximate consensus in Definition 1
by using the proposed online GP-based controller.
Remark 10:The derived ultimate error boundεis es-
tablished using a uniform upper bound of the online GP
posterior variance¯σi to obtain explicit worst-case robustness
guarantees under asynchronous delayed learning. In practice,
as additional data are collected and the sampling density
increases, the GP posterior varianceσ i(·)typically decreases,
leading to improved prediction accuracy and smaller consensus
boundε. Moreover, smaller computational delays∆ i increase
the effective learning update frequency and further improve
practical performance. Explicitly characterizing the coupled
relationship among posterior variance¯σ i and computation
delay remains an interesting direction for future investigation.
Remark 11:Note that the ultimate bound¯ϵin Lemma 5
and Theorem 2 depends on the number of agentsN, which
originates from the aggregation of individual prediction error
¯σi bounds and computational delays∆ i. For large-scale MAS,
the ultimate bound can be reduced by improving GP accuracy
with smaller¯σi and enhancing computational capabilities for
smaller∆ i. The dependence onNcan potentially be allevi-
ated by using local input-to-state stability [38] or normalized
consensus gains [39], whose analysis is beyond the scope
of this paper. The primary focus is to address asynchronous
cooperative learning with heterogeneous delays and query
point mismatch.
C. Comparison to Local Learning-based Control
1) Learning Performance:To compare with the local pre-
diction with ˆdloc,i(t)=P j∈{i,Ni} ωi,j(t)µloc,j(kj(t)), the ag-
gregated prediction is considered asµ loc,i(ki(t)) =µ i(ki(t))
and zero neighboring predictionsµ loc,j(kj(t)) =0n×1. Con-
sider the prior mean as the posterior mean with empty
data sets, it holdsµ loc,j(kj(t)) =µ(x j(tj,kj (t)),∅)with
σ(xj(tj,kj (t)),∅) =σ s, which results inω i,j(t) = 0. The
resulting prediction error bounds are denoted by∥d(x i(t))− ˆdloc,i(t)∥ ≤˜ηloc,i,j(t)=βσ s+Ld∥xi(t)−x j(tj,kj (t))∥ 1 2 , which
satisfyη i,j(t)< η loc,i,j(t)due to the strict reduction of
posterior varianceσ(·,·). Then, by monotonicity, it follows
that˜ηi(t)<˜ηloc,i(t),∀t∈R 0,+, which shows that cooperative
learning with ˆdi(t)does not deteriorate the theoretical error
bound compared to the local case with ˆdloc,i(t). Moreover, the
analysis indicates that cooperative learning improves perfor-
mance when neighboring predictions have smaller uncertainty
or query point mismatch.
2) Control Performance:According to the expression of
θi in (19), incorporating predictions from neighboring agents
can reduce the tracking error bound¯ε, especially when those
predictions have lower uncertainty (smaller¯σ i) or smaller

7
x
y
0
 qi,1
qi,2
qi,3
(a)
12
3
4 5
6
(b)
Figure 2: Setting of the multi-USV system. (a) Generalized
coordinate. (b) Communication topologyG.
delay-induced mismatch (smaller∆ i). Specifically, following
the same procedure in Lemma 5 and [9], the ultimate tracking
error bound using local learning is written as
¯εloc = 2λ−1M ∥θloc∥, θ loc,i =β¯σi +L d(2F∆ i) 1 2 (21)
for alli= 1,· · ·, Nwithθ loc = [θ loc,1,· · ·, θloc,N ]T .
Similarly as in Theorem 2, the ultimate consensus error and
velocity error are expressed asϵ loc,0 = 2¯εloc andϵ loc,1 = ¯εloc.
The comparison between¯εand¯ε loc is shown below.
Proposition 1:Consider a MAS (1) satisfying Assump-
tions 1 and 2, whose dynamics is learned via (10) satisfying
Assumptions 3 to 5 andω ∗ i,j =ω ∗ j,i,∀(i, j)∈ E. The system is
controlled by the proposed control law (3) with (4), (5), (10)
and (14) satisfying Lemmas 3 and 4. Then, the cooperative
learning achieves improved control performance compared to
local learning, in the sense thatϵ 0 ≤ϵ loc,0 andϵ 1 ≤ϵ loc,1.
Proof:See appendix.
Proposition 1 shows that cooperative learning leads to
smaller error bounds than local learning. In summary, agents
improve their prediction accuracy and therefore enhance con-
trol performance by sharing learning information.
V. SIMULATION
To demonstrate the effectiveness of the proposed approach,
simulations are conducted with more details in appendix.
A. Simulation Setting
In this simulation, we investigate a second-order consensus
problem involvingN= 6unmanned surface vehicles (USVs),
as illustrated in Fig. 2. Each USV is governed by the Euler-
Lagrange dynamics specified in (1), characterized byn= 3
degrees of freedom (DoFs). The physical parameters of all
USVs are adopted from the same configuration in [1], and each
USV is subject to unknown state dependent wind effect and
current influence. The connection of the USVs are formulated
as a graphGshown in Fig. 2. The gains are set as¯c 1 = ¯c3 =
c2 = 2,c 1 = 1andc 3 = 2 √c2,c 0 = 0.5c 1c3,¯c0 = ¯c1¯c3,
such that Lemmas 3 and 4 hold. To estimate the unknown
disturbanced(·), GP model is deployed on each agenti∈ V
with empty initial data setD i(0) =∅and squared exponential
kernelκ p(x,x ′) =σ 2 f,p exp(−σ−2 l (x−x ′)T (x−x ′)/2)
for anyx,x ′ ∈X, whereσ f,p = 1for each dimension
p= 1,· · ·, nandσ l = 0.1. Each agenticollects the
received data pair att i,k and deletes the oldest data pair when
|Di(t)| ≥¯N= 100. The upper bound of measurement noise
Figure 3: Aggregated prediction error∥d(x(t))− ˆd(t)∥and
the prediction error bound∥ ˜η(t)∥in Theorem 1.
for the data pair is considered as¯w p = 0.01forp= 1,· · ·, n.
The compensation ˆdi(·)on each agenti∈ Vis calculated by
the proposed distributed GPs with (10), where the constant
coefficients in (11) are set asω ∗ i,j =a i,j/(1 +|N i|)for any
i, j∈ V. The computation time∆i(ti,k)is randomly uniformly
distributed in[0.01,0.1],∀k∈Nandi∈ V. The total
simulation time is set as30. To demonstrate the effectiveness
of the proposed approach, some existing learning methods are
compared, namely MoE, PoE, gPoE, BCM, rBCM and Local.
B. Control and Prediction Performances
To compare the control and prediction performances, the
same random initial valuesq(0) = [q T 1 (0),· · ·,qT 6 (0)]T are
set for all methods. The comparative analysis of prediction
accuracy across different strategies is presented in Fig. 3,
where the proposed aggregation method demonstrates supe-
rior performance by achieving significantly reduced aggre-
gated prediction errors∥d(x(t))− ˆd(t)∥, withd(x(t)) =
[dT (x1(t)),· · ·,dT (xN (t))]T and ˆd(t) = [ ˆdT 1 (t),· · ·,ˆdT N (t)]T
representing the true and estimated disturbances, respectively.
This performance advantage can be attributed to the fundamen-
tal limitation of alternative PoE and BCM-based approaches,
which neglect query point bias. Moreover, it is noteworthy that
the cooperative learning performs better than local approach,
only when the delay is explicitly considered in the aggregation
as our method. In addition to the actual aggregated prediction
error, the theoretical error bound ˜η(t) = [˜η1(t),· · ·,˜ηN (t)]T
derived in Theorem 1 is also evaluated in simulation. As
shown in Fig. 3, the actual prediction error∥d(x(t))− ˆd(t)∥
remains consistently below the derived bound∥ ˆη(t)∥for all
time, demonstrating the correctness of the theoretical analysis.
Given the strong interdependence between prediction ac-
curacy and consensus performance, a comparative evaluation
of control effectiveness across different cooperative learning-
based strategies is conducted, with results presented in Fig. 4.
The experimental results clearly demonstrate that the proposed
methodology achieves superior performance in maximal con-
sensus error and the maximal velocity compared to existing
methods, which demonstrates the effectiveness of the proposed
approach for addressing the second-order consensus problem.
C. Monte Carlo Test
To eliminate potential biases arising from specific initial
conditions, a Monte Carlo test is conducted with 100 inde-

8
Figure 4: Maximal consensus error∥q i(t)−qj(t)∥and velocity
error∥ ˙qi(t)∥for alli, j∈ Vwithi̸=j.
Figure 5: Aggregated prediction error∥d(x(t))− ˆd(t)∥w.r.t
timetfrom7cooperative learning-based control methods. The
solid line represents the mean value among100Monte Carlo
tests, and the shadowed area denotes the variances.
pendent trials for each comparative method. In each trial, the
initial position coordinatesq i(0)and velocities ˙qi(0)for each
agenti∈ Vare randomly sampled from a uniform distribution
over the domain[−1,1] 3, thereby providing a statistically
representative assessment of algorithm performance across
diverse initialization scenarios.
The aggregated prediction performance across all six coop-
erative learning-based control strategies is presented in Fig. 5,
where the proposed methodology consistently demonstrates
superior prediction accuracy as reflected by smaller prediction
error. Consequently, the enhanced disturbance estimation capa-
bility translates directly into improved second-order consensus
performance as shown in Fig. 6, where the maximal difference
betweenq i andq j and the maximal velocity ˙qi are smaller
compared to existing cooperative learning frameworks, thereby
demonstrating the statistical significance and robustness of the
proposed approach.
Furthermore, the evaluation of steady-state prediction and
control performance is essential for comprehensively demon-
strating the efficacy of the proposed methodology. To quantify
steady-state behavior, three key performance indicators are
employed: the maximal prediction errormax t∈T ∥d(x(t))−
Figure 6: Maximal consensus error∥q i(t)−q j(t)∥between
any two agentsi, j∈ Vwithi̸=jand maximal velocity
error∥ ˙qi(t)∥for any agenti∈ Vover timetusing different
cooperative learning-based control strategies. The solid line
represents the mean value among100Monte Carlo tests, and
the shadowed area denotes the variances.
Figure 7: Maximal aggregated prediction error∥d(x(t))−
ˆd(t)∥in time domaint∈[10,30]for different cooperative
learning-based control strategy, which is summarized from100
times Monte Carlo tests.
ˆd(t)∥, consensus errormax t∈T maxi,j∈V,i̸=j ∥qi(t)−q j(t)∥
and velocity errormax t∈T maxi∈V ∥ ˙qi(t)∥in the time domain
T= [10,30]. The results shown in Figs. 7 and 8 demonstrate
that the proposed approach achieves substantially reduced
errors in both disturbance prediction and consensus control
compared to other strategies. These findings provide empirical
evidence supporting the superior performance and practical ef-
fectiveness of the proposed cooperative learning-based control
framework for multi-agent consensus applications.
VI. CONCLUSION
This paper presents a novel cooperative online learning-
based control framework for multi-agent robotic systems with
unknown dynamics, addressing the challenge of achieving
second-order consensus under heterogeneous computational
delays. GP regression is employed at each individual agent,
and an asynchronous cooperative learning strategy is devel-
oped to aggregate predictions despite differing computational
delays and query point. Furthermore, a distributed control law

9
Figure 8: Maximal consensus error∥q i(t)−qj(t)∥and velocity
error∥ ˙qi(t)∥for alli, j∈ Vwithi̸=jin time domain
t∈[10,30]for different cooperative learning-based control
strategy, which is from100times Monte Carlo tests.
is designed based on an adjoint MAS, which provides the-
oretical approximate consensus guarantees. The effectiveness
and superiority of the proposed methodology are demonstrated
through numerical simulations on unmanned surface vehicles
compared to existing cooperative approaches.
REFERENCES
[1] Z. Yang, X. Dai, L. Fang, J. Zhou, and Z. Yan, “Safe Event-Triggered
Control of Unmanned Surface Vehicles with Gaussian Processes: Re-
silience in Denial of Service Attacks and Uncertain Dynamics,”Engi-
neering Applications of Artificial Intelligence, vol. 153, p. 110776, 2025.
[2] K. Zhang, M. Sharma, J. Liang, and O. Kroemer, “A Modular Robotic
Arm Control Stack for Research: Franka-Interface and FrankaPy,”arXiv
preprint arXiv:2011.02398, 2020.
[3] D. Panagou, D. M. Stipanovi ´c, and P. G. V oulgaris, “Distributed Coordi-
nation Control for Multi-Robot Networks Using Lyapunov-Like Barrier
Functions,”IEEE Transactions on Automatic Control, vol. 61, no. 3, pp.
617–632, 2015.
[4] Y . Wang, Y . Song, and W. Ren, “Distributed Adaptive Finite-Time
Approach for Formation–Containment Control of Networked Nonlin-
ear Systems under Directed Topology,”IEEE Transactions on Neural
Networks and Learning Systems, vol. 29, no. 7, pp. 3164–3175, 2017.
[5] J. Cort ´es, S. Mart ´ınez, T. Karatas ¸, and F. Bullo, “Coverage Control
for Mobile Sensing Networks,”IEEE Transactions on Robotics and
Automation, vol. 20, no. 2, pp. 243–255, 2004.
[6] M. Zhu and S. Mart ´ınez, “Distributed Coverage Games for Energy-
Aware Mobile Sensor Networks,”SIAM Journal on Control and Opti-
mization, vol. 51, no. 1, pp. 1–27, 2013.
[7] ——, “On Distributed Convex Optimization under Inequality and Equal-
ity Constraints,”IEEE Transactions on Automatic Control, vol. 57, no. 1,
pp. 151–164, 2011.
[8] A. Lederer, Z. Yang, J. Jiao, and S. Hirche, “Cooperative Control
of Uncertain Multiagent Systems via Distributed Gaussian Processes,”
IEEE Transactions on Automatic Control, vol. 68, no. 5, pp. 3091–3098,
2023.
[9] X. Dai, Z. Yang, M. Xu, S. Zhang, F. Liu, G. Hattab, and S. Hirche,
“Decentralized Event-Triggered Online Learning for Safe Consensus
Control of Multi-Agent Systems with Gaussian Process Regression,”
European Journal of Control, p. 101058, 2024.
[10] Z. Yang, S. Dong, A. Lederer, X. Dai, S. Chen, S. Sosnowski, G. Hattab,
and S. Hirche, “Cooperative Learning with Gaussian Processes for
Euler–Lagrange Systems Tracking Control under Switching Topologies,”
arXiv preprint arXiv:2402.03048, 2024.
[11] Y . Zhu, Z. Wang, H. Liang, and C. K. Ahn, “Neural-Network-Based
Predefined-Time Adaptive Consensus in Nonlinear Multi-Agent Systems
with Switching Topologies,”IEEE Transactions on Neural Networks and
Learning Systems, 2023.
[12] A. Lamperski and T. Lekang, “Approximation with Random Shallow
ReLU Networks with Applications to Model Reference Adaptive Con-
trol,”arXiv preprint arXiv:2403.17142, 2024.
[13] C. K. I. Williams and C. E. Rasmussen,Gaussian Processes for Machine
Learning. Cambridge, MA: MIT Press, 2006.
[14] N. Srinivas, A. Krause, S. M. Kakade, and M. W. Seeger, “Information-
Theoretic Regret Bounds for Gaussian Process Optimization in the
Bandit Setting,”IEEE Transactions on Information Theory, vol. 58,
no. 5, pp. 3250–3265, 2012.
[15] K. Hashimoto, A. Saoud, M. Kishida, T. Ushio, and D. V . Dimarog-
onas, “Learning-Based Symbolic Abstractions for Nonlinear Control
Systems,”Automatica, vol. 146, p. 110646, 2022.
[16] T. Ding, R. Zheng, S. Zhang, and M. Liu, “Resource-Efficient Coop-
erative Online Scalar Field Mapping via Distributed Sparse Gaussian
Process Regression,”IEEE Robotics and Automation Letters, vol. 9,
no. 3, pp. 2295–2302, 2024.
[17] Z. Yuan and M. Zhu, “Communication-Aware Distributed Gaussian
Process Regression Algorithms for Real-Time Machine Learning,” in
Proceedings of the American Control Conference (ACC), 2020, pp.
2197–2202.
[18] ——, “Lightweight Distributed Gaussian Process Regression for Online
Machine Learning,”IEEE Transactions on Automatic Control, vol. 69,
no. 6, pp. 3928–3943, 2024.
[19] G. P. Kontoudis and D. J. Stilwell, “Decentralized Nested Gaussian
Processes for Multi-Robot Systems,” inProceedings of the IEEE In-
ternational Conference on Robotics and Automation (ICRA), 2021, pp.
8881–8887.
[20] X. Dai, Z. Yang, S. Zhang, D.-H. Zhai, Y . Xia, and S. Hirche, “Coop-
erative Online Learning for Multiagent System Control via Gaussian
Processes With Event-Triggered Mechanism,”IEEE Transactions on
Neural Networks and Learning Systems, 2024.
[21] X. Zhang, S. Zheng, C. K. Ahn, and Y . Xie, “Adaptive Neural Consensus
for Fractional-Order Multi-Agent Systems with Faults and Delays,”
IEEE Transactions on Neural Networks and Learning Systems, vol. 34,
no. 10, pp. 7873–7886, 2022.
[22] X. Dai, A. Lederer, Z. Yang, and S. Hirche, “Can Learning Deteriorate
Control? Analyzing Computational Delays in Gaussian Process-Based
Event-Triggered Online Learning,” inProceedings of the 5th Annual
Learning for Dynamics and Control Conference (L4DC), 2023, pp. 445–
457.
[23] Z. Yang, X. Dai, and S. Hirche, “Asynchronous Distributed Gaussian
Process Regression,” inProceedings of the AAAI Conference on Artificial
Intelligence, vol. 39, no. 21, 2025, pp. 22 065–22 073.
[24] W. Hou, M. Fu, H. Zhang, and Z. Wu, “Consensus Conditions for Gen-
eral Second-Order Multi-Agent Systems with Communication Delay,”
Automatica, vol. 75, pp. 293–298, 2017.
[25] P. Lin and Y . Jia, “Consensus of a Class of Second-Order Multi-Agent
Systems with Time-Delay and Jointly-Connected Topologies,”IEEE
Transactions on Automatic Control, vol. 55, no. 3, pp. 778–784, 2010.
[26] N. Amelina, A. Fradkov, Y . Jiang, and D. J. Vergados, “Approximate
Consensus in Stochastic Networks with Application to Load Balancing,”
IEEE Transactions on Information Theory, vol. 61, no. 4, pp. 1739–
1752, 2015.
[27] X. Jiang, G. Xia, Z. Feng, W. X. Zheng, and R. Su, “Reachable
Set Estimation of Multiagent Systems: An Approximate Consensus
Perspective,”IEEE Transactions on Control of Network Systems, vol. 11,
no. 1, pp. 353–363, 2023.
[28] R. H. Middletone and G. C. Goodwin, “Adaptive Computed Torque
Control for Rigid-Link Manipulators,” inProceedings of the IEEE
Conference on Decision and Control, 1986, pp. 68–73.
[29] A. Tokmak, T. B. Sch ¨on, and D. Baumann, “PACSBO: Probably
Approximately Correct Safe Bayesian Optimization,” inProceedings of
the Symposium on Systems Theory in Data and Optimization, 2024, pp.
3–18.
[30] A. Tokmak, K. G. N. Krishnan, T. B. Sch ¨on, and D. Baumann, “Safe
Exploration in Reproducing Kernel Hilbert Spaces,”Proceedings of
Machine Learning Research, vol. 258, pp. 784–792, 2025.
[31] A. Lederer, A. J. O. Conejo, K. A. Maier, W. Xiao, J. Umlauft, and
S. Hirche, “Gaussian Process-Based Real-Time Learning for Safety-
Critical Applications,” inProceedings of the International Conference
on Machine Learning (ICML), 2021, pp. 6055–6064.
[32] Z. Yang, D. Zhang, X. Dai, F. Yu, C. Zhang, B. Huang, H. Sadeghian,
and S. Haddadin, “Streaming Generated Gaussian Process Experts for
Online Learning and Control,” inProceedings of the AAAI Conference
on Artificial Intelligence, vol. 40, no. 33, 2026, pp. 27 719–27 727.

10
[33] Y . Cao and D. J. Fleet, “Generalized Product of Experts for Automatic
and Principled Fusion of Gaussian Process Predictions,”arXiv preprint
arXiv:1410.7827, 2014.
[34] I. Karafyllis and M. Krstic, “Adaptive Certainty-Equivalence Control
with Regulation-Triggered Finite-Time Least-Squares Identification,”
IEEE Transactions on Automatic Control, vol. 63, no. 10, pp. 3261–
3275, 2018.
[35] J. A. Farrell, M. Polycarpou, M. Sharma, and W. Dong, “Command Fil-
tered Backstepping,”IEEE Transactions on Automatic Control, vol. 54,
no. 6, pp. 1391–1395, 2009.
[36] V . I. Utkin,Sliding Modes in Control and Optimization. Springer
Science & Business Media, 2013.
[37] X. Wang and X. Mao, “Non-Overshooting Sliding Mode for UA V
Control,”The Aeronautical Journal, vol. 128, no. 1329, pp. 2483–2529,
2024.
[38] Z. Zeng, X. Wang, and Z. Zheng, “Convergence analysis using the
edge laplacian: Robust consensus of nonlinear multi-agent systems via
iss method,”International Journal of Robust and Nonlinear Control,
vol. 26, no. 5, pp. 1051–1072, 2016.
[39] F. M. Atay, “Consensus in Networks under Transmission Delays and the
Normalized Laplacian,”IFAC Proceedings Volumes, vol. 43, no. 2, pp.
277–282, 2010.
Xiaobing Daireceived the B.Sc. mechanical engi-
neering from the Tongji University, Shanghai, China,
in 2018 with direction in mechatronics, building en-
vironment and civil engineering. He received double
M.Sc degrees in Mechanical Engineering, Mecha-
tronics and Robotics from the Technical Univer-
sity of Munich, Munich, Germany, in 2021. Since
February 2022, he is a PhD student at the Chair
of Information-oriented Control, TUM School of
Computation, Information and Technology at the
Technical University of Munich, Munich, Germany.
His current research interests include efficient online machine learning,
networked control systems, safe learning-based control.
Zewen Yang(Member, IEEE) received the M.S.
degree in control engineering from Northeast For-
est University, in 2017. He pursued a Ph.D. in
control science and engineering at the College of
Intelligent Systems Science and Engineering, Harbin
Engineering University, Harbin, China, from 2017 to
2019 and joined the Chair of Information-oriented
Control, School of Computation, Information and
Technology, the Technical University of Munich
(TUM), Munich, Germany, in machine learning and
data-driven control until 2023. From 2023 to 2024,
he was a postdoctoral researcher at the Robert Koch Institute, Berlin, Germany.
Since 2025, he has been with the Chair of Robotics and Systems Intelligence
at the Munich Institute of Robotics and Machine Intelligence, TUM. His
current research interests include multi-agent systems, cooperative learning,
generative models, control theory, and general robotics.
Wei Ren(Fellow, IEEE) received the Ph.D. degree
in electrical engineering from Brigham Young Uni-
versity, Provo, UT, USA, in 2004.
He is currently a Professor with the Department
of Electrical and Computer Engineering, University
of California at Riverside, Riverside, CA, USA. His
research focuses on distributed control of multiagent
systems.
Dr. Ren was the recipient of the IEEE Control
Systems Society Antonio Ruberti Young Researcher
Prize in 2017 and the National Science Foundation
CAREER Award in 2008. He was an IEEE Control Systems Society Distin-
guished Lecturer from 2020 to 2024.
Sandra Hirche(Fellow, IEEE) received the Dipl.-
Ing degree in aeronautical engineering from the
Technical University of Berlin, Berlin, Germany, in
2002, and the Dr. Ing. degree in electrical engi-
neering from the Technical University of Munich,
Munich, Germany, in 2005. From 2005 to 2007, she
was awarded a Post-doctoral scholarship from the
Japanese Society for the Promotion of Science at
the Fujita Laboratory, Tokyo Institute of Technology,
Tokyo, Japan. From 2008 to 2012, she was an
Associate Professor with the Technical University
of Munich. Since 2013, she has served as Technical University of Munich
Liesel Beckmann Distinguished Professor and has been with the Chair of
Information-Oriented Control, Department of Electrical and Computer Engi-
neering, Technical University of Munich. She has authored or coauthored more
than 150 papers in international journals, books, and refereed conferences.
Her main research interests include cooperative, distributed, and networked
control with applications in human–machine interaction, multirobot systems,
and general robotics.
Dr. Hirche has served on the editorial boards of the IEEE Transactions
on Control of Network Systems, the IEEE Transactions on Control Systems
Technology, and the IEEE Transactions on Haptics. She has received multiple
awards such as the Rohde & Schwarz Award for her Ph.D. thesis, the IFAC
World Congress Best Poster Award in 2005, and – together with students – the
2018 Outstanding Student Paper Award of the IEEE Conference on Decision
and Control as well as Best Paper Awards from IEEE Worldhaptics and the
IFAC Conference of Manoeuvring and Control of Marine Craft in 2009.
