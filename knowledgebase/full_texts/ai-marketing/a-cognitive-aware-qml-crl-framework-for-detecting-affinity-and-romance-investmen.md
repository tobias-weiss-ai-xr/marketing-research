---
title: A Cognitive-Aware QML-CRL Framework for Detecting Affinity and Romance-Investment Fraud
url: https://arxiv.org/abs/2610.09141
category: ai-marketing
subcategory: framework
date: 2026-10
venue: arXiv (Cornell University)
authors:
- Bibhas Adhikari
- Ramya Srinivasan
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.09141
pages: 23
chars: 55408
fetched_at: '2026-11-08T13:35:34+00:00'
kb_version: 1
---

# A Cognitive-Aware QML-CRL Framework for Detecting Affinity and Romance-Investment Fraud

A Cognitive-Aware QML-CRL Framework for
Detecting Affinity and Romance-Investment Fraud
Bibhas Adhikari* and Ramya Srinivasan †
Abstract
We present a hybrid quantum-classical framework that detects affinity and
romance-investment fraud by modelling the cognitive biases in a manipulative
conversation. In our proposed framework, cognitive biases central to this fraud
class are carried by dedicated qubits in a structured parameterized quantum circuit,
together with a frame qubit makes the encoding sensitive to the temporal order of
manipulative reframing, and a narrative qubit that aggregates co-occurrence through
a trainable entanglement layer. The circuit parameters are trained jointly with a
classical reinforcement-learning agent that decides, turn by turn, whether to flag the
conversation, modeled as an optimal stopping problem. We evaluate the model’s
performance on synthetic conversations that include hard negatives, legitimate but
urgent, and legitimate but pushy sales conversations.
Keywords:Parameterized Quantum Circuits, Quantum Machine Learning, Reinforce-
ment Learning, Quantum Cognition, Fraud Detection, Order Effects, Conjunction
Fallacy
1 Introduction
Affinity and romance-investment fraud exploit trust built through shared identity or
emotional intimacy to bypass the scrutiny that a person would normally apply to a
financial decision. In affinity fraud, perpetrators target members of an identifiable group
such as a religious congregation, ethnic community, or professional network. This helps
the perpetrators to build in-group trust and the social vouching reduce due diligence.
The U.S.A. Securities and Exchange Commission has long flagged this as a recurring
driver of large-scale Ponzi schemes [26]. On the other hand, romance-investment fraud
follows a closely related but distinct mechanism, documented in detail by Whitty and
Buchanan [33]. This fraud is based on the scam’s staged structure: relationship-building,
a small demonstration of “legitimacy”, and then escalating financial requests. It is
also investigated in the literature why victims continue sending money even after clear
*Corresponding author, Fujitsu Research of America, Inc., Santa Clara, CA, USA, Email: bad-
hikari@fujitsu.com
†Security Science Lab, Fujitsu Research of America, Santa Clara, CA 95054 Inc. Email:
ramya@fujitsu.com
1
arXiv:2610.09141v1  [cs.LG]  6 Oct 2026

warning signs appear, attributing it to the relationship narrative overriding financial
judgment rather than any deficit in the victim’s general reasoning ability [ 2]. In the
UK Office of Fair Trading report, this pattern appears across fraud types, showing that
authority, urgency, and social-proof cues systematically override rational risk assessment
once a persuasive relationship or narrative has been established [19]. Thus, affinity and
romance-investment fraud succeed by exploiting cognitive biases in a specific, staged
sequence rather than by any single deceptive claim [23, 33, 2, 19, 10, 12].
In their proposal of classical Behavioral Reinforcement Learning (BRL) in [3], the
authors show how to embed biases such as Loss Aversion through an asymmetric utility
function into a reinforcement learning framework. Indeed, the utility function in their
paper represents a pointwise transform of a scalar reward which is not designed to
reproduce two well established human judgment phenomena:order effects[ 29, 4] and
theconjunction fallacy[ 30, 5]. These two notions play a key role into the development
of quantum cognition model [6, 34], and both are central to how affinity and romance-
investment fraud actually work [23]. The role of cognitive biases in financial decision
making is explored in the literature in different contexts, for instance, see [25, 11, 24, 15,
27, 14]. There are also studies to employ cognitive biases into define feature vectors for
learning tasks [7, 17]. Quantum-cognitive models of decision-making [4, 18] address
both by representing beliefs as vectors in a Hilbert space and questions as (generally
non-commuting) projective measurements.
In this paper, we consider the question:given a conversation, can a system watching
it learn to detect that this kind of manipulation is under way, and if so, when?We
investigate it with the use of a structured parameterized quantum circuit (PQC), of-
ten refereed to as Quantum Neural Network or ansatz [ 1] in the context of Quantum
Machine Learning (QML), acting as a trainable cognitive encoder followed by a Classi-
cal Reinforcement Learning (CRL) stopping agent. In our framework, we consider a
quantum register of n qubits to encode n cognitive biases driven by cue-conditioned
rotation modeled by rotation parametrized gates and two additional qubits: aframe
qubit that carries the temporal order of manipulative reframing through non-commuting
rotations, and anarrativequbit that aggregates co-occurrence. Indeed, the parametrized
rotation operators encode the cognitive bias cues, whose values are trained and learned
with the aid of the RL agent. The proposed scam detector therefore does not merely
use a quantum representation of cognitive bias, it learns one, under an objective that
is the deployment objective (flag early enough, but do not cry wolf) rather than a sur-
rogate classification loss. Thus, our framework introduces a quantum-classical hybrid
QML-CRL model for scam detection, which combines a cognitive-aware quantum
feature encoder with a classical reinforcement learning agent, providing a realization of
Quantum Reinforcement Learning (QRL) [20, 8] model for sequential scam detection.
The structure of the ansatz that we consider in this paper is motivated by the
following observation in the context of the scam. First, manipulative reframing is
order-dependent: presenting a loss frame before a recovery frame is not equivalent to the
reverse, and a same-axis rotation cannot distinguish the two, since RY (θ1)RY (θ2) =
RY (θ1 +θ 2) regardless of application order. We address this with a frame qubit
that receives RZ for loss-framing cues and RY for recovery-framing cues; because
[RY (θ), RZ(ϕ)] =−2isin(θ/2) sin(ϕ/2)X̸= 0 (Proposition 1), the resulting state
depends on the temporal order in which the two framings occur. We show, however,
2

that non-commutativity of the gates is not by itself sufficient and the measurement
basis must also avoid a degenerate choice at which the order dependence is invisible
(Proposition 3), and we therefore make that basis a trained parameter. Second, the
biases do not operate independently i.e. a target’s judgement that a person is trustworthy
and that an opportunity is legitimate are assessed as one mutually reinforcing narrative.
Since no joint measurement can exceed the Fréchet bound (Proposition 2), we use the
narrative qubit not to violate that bound but as an order-insensitive coherence aggregate,
implemented by controlled rotations whose angles are trained rather than fixed. The
parameters of the rotation gates are functions of cues (which are directly obtained from
the conversation using an Natural Language Processing (NLP) tool for the conversation
in each turn) and the cue thresholds. Besides, there are entangler parameters which are
incorporated to learn the narrative coherence in the conversation.
We emphasize that order effects and the conjunction fallacy are well documented
violations of Kolmogorov probability applied to a single fixed sample space [32, 28, 13].
This constrains probabilistic models of the judgement itself but not the classical learning
machinery in general. In fact, any recurrent or attention-based sequence model is order-
sensitive simply because its state updates do not commute, and indeed our encoder is
efficiently classically simulatable. Our claim is therefore one of inductive bias rather
than expressive necessity i.e. the quantum formalism supplies a compact, interpretable
encoding in which order sensitivity, bounded monotone readouts, and Fréchet-respecting
aggregation follow from the structure of the representation rather than having to be
learned from data or imposed by regularization.
In our numerical demonstration, we consider four cognitive biases as described
below, whose existence in these frauds can be clearly justified.
• Loss aversion[ 16] - the engine of the funnel’s “recovery pressure” stage: once
money is sunk, framing continuation as avoiding a certain loss (rather than risking
more) triggers risk-seeking behavior in the loss domain.
• Commitment (and consistency)[ 9] - having made a small commitment, a target
feels pressure to act consistently with it rather than admit it was a mistake; this
compounds with loss aversion rather than acting as an independent factor.
• Reciprocity[ 9] - a real small payout (or, in affinity fraud, a community member’s
personal vouching) creates a felt obligation to reciprocate trust, directly enabling
the next, larger ask.
• Authority[ 9] - borrowed authority (a trusted community figure in affinity fraud;
fabricated credentials in romance-investment fraud) is a primary trust-conferral
mechanism [22].
The CRL framework is then designed to convert the quantum encoder’s continuous,
per-turn risk signal into a single actionable decision: when, if ever, to flag a conversation.
The RL agent learns from labeled outcomes to trade off the cost of a false alarm
against the cost of intervening too late, rather than simply classifying the conversation
after the fact. Thus, we frame the detection as anoptimal stopping problem. The
RL layer receives no information about the conversation except the quantum register’s
readout. We perform numerical test on synthetic, labelled conversation data: order-effect
3

magnitude at both the feature level and the detection-timing level, and an ablation study
isolating each encoder channel’s contribution to detection quality.
The remainder of this paper is organized as follows. Section 2 introduces the
proposed cognitive-aware PQC for modeling manipulative conversations. Section 3
presents the joint QML-CRL framework for scam detection. Section 4 reports numerical
results on synthetic data. Finally, the paper concludes with a discussion on limitations
and future work in Section 5, followed by supplementary material after the references.
Raw conversation
turnst= 1,2, . . .
NLP cue extraction
ct ∈[0,1] n ×[−1,1] PQC encoderU(Θ) n+2qubits Risk features st(Θ), Eq. (1) Linear Q head Q(st, a) =wa ·st(Θ)
FLAG: high-risk
(episode ends)
FLAG
WAIT: advance to turnt+1
backward pass:δ t ∇Θ Q=δ t w⊤ a ∂st /∂Θ(parameter shift); the sameδ t updatesw a
(a) End-to-end pipeline. Solid: inference. Dashed: the temporal-difference error, which trains the
Q head and flows back into the circuit parametersΘ.
q0 lossR Y (∆t 0)
q1 commitmentR Y (∆t 1)
q2 reciprocityR Y (∆t 2)
q3 authorityR Y (∆t 3)
∆t i =  π−θ t−1 i  σ  wi ct,i +b i  — trainable gain and threshold,
enforcing θt i < π without a clip
q4 frame, prepared in|+⟩
RY

ζy[−ct,f ]+

RZ

ζz[ct,f ]+

non-commuting (Prop. 1)
q5 narrative qubit
CR
qj →q5
Y (φj )
trainable;φ j =π⇒CNOT
closed form, Eq. (15):
⟨Z5⟩= Re Q j  1 +p j (eiφj −1) 
readout basisR Y (µ)
trainable
order-blind at µ=±π/2
(Prop. 3)
(b) Parameterized encoder detail; bold symbols are trained.
Figure 1: Complete architecture. (a) The end-to-end pipeline from raw conversation
text to a flag/wait decision. (b) Detail of the parameterized quantum-cognitive encoder.
4

2 Quantum-Cognitive PQC Encoder
In this section, we propose a PQC on an (n+ 2) -qubit quantum register that acts
as a quantum-cognitive encoder. The first n-qubits, called the bias qubits encode
n cognitive biases, whereas the frame and narrative qubits are used to monitor the
ordering and coherence of the conversation, respectively. The Figure 1 describes the
end-to-end architecture of our proposal incorporating the four biases, as described in
the introduction. The Algorithm 1 describes the working of the PQC for the general
context.
2.1 Quantum Register
The bias qubits are labelled q0, . . . , qn−1, the frame qubit is qn (also denoted as qf to be
explicit), and the narrative qubit is qn+1 (also denoted as qn to be explicit), and we write
pullt f and pullt nar for their readouts, so that pullt f =−⟨Z n⟩t and pullt nar =−⟨Z n+1⟩t.
Bias and narrative qubits are prepared in |0⟩ and the frame qubit in |+⟩=H|0⟩ , for the
reason given in the supplementary notes, so that |ψ(0)⟩=|0⟩ ⊗n ⊗ |+⟩ ⊗ |0⟩, which is
the initial state of the quantum register. At every turn t, we determine the risk feature
vector
st =

pullt 0, . . . ,pullt n−1,pull t f ,pull t nar,1−e −t/τ0 ,1  ∈[−1,1] n+2×[0,1)×{1} ⊂R n+4,
(1)
where pull(t) i ∈[−1,1] are defined below, τ0 is a fixed time constant, 1−e −t/τ0
represents the saturating time feature, the trailing constant supplies the intercept of the
linear head and together with the saturating time feature it is independent of Θ. The
proposed structured PQC consists of two sub-circuits. In the first sub-circuit, for each
turnt,the output quantum state is given by
|ψ(t)⟩=U r(t)· · ·Ur(1)|ψ(0)⟩
with per-turn block Ur and the initial state |ψ(0)⟩. The readout block is applied to a
copy of this state,
|χ(t)⟩=U e(φ)

RY (µ)onq n

|ψ(t)⟩,(2)
and the risk features are read from |χ(t)⟩ rather than |ψ(t)⟩. The sub-circuits are
depicted in Figure 2.
An NLP front end (specified, not built here) produces a per-turn cue vector ct =
(ct,0, . . . , ct,n−1, ct,f )∈[0,1] n ×[−1,1]. The trainable parameter vector is
Θ =

w0, . . . , wn−1| {z }
cue gains
, b0, . . . , bn−1| {z }
cue thresholds
, ρz, ρy, φ0, . . . , φn| {z }
entangler
, µ

∈R 3n+4.(3)
For instance, forn= 4biases, there are16circuit parameters i.e.|Θ|= 16.
At each turnt,for each bias qubit, we apply a rotation gateR Y (∆t i)toq i with
∆t i =  π−θ t−1 i  gt i , g t i =σ(w i ct,i +b i), θ t i =θ t−1 i + ∆t i,(4)
where σ(x) = 1/(1 +e −x) is the logistic function and θ0 i = 0 . Note that, since
gt i ∈(0,1) , the cumulative angle satisfies θt i < πfor every t by construction, and hence
5

the monotonicity of pullt i =−⟨Z i⟩t =−cosθ t i on [0, π]is enforced. Unrolling (4)
gives a closed form that makes the semantics explicit,
θt i =π  1− Y
s≤t

1−g s i  ,(5)
i.e. the bias qubit’s angle is a soft OR, a differentiable relaxation of the Boolean OR
over turns, saturating as the learned probability that at least one turn so far carried cue i.
Both the gain wi and the threshold bi are trainable parameters. The parameter bi plays
the role of the hand-set cue threshold of a fixed encoder and wi that of its gain, but one
per channel and fitted to data rather than shared and guessed. The monotonic pulli is
given by pulli =−⟨Z i⟩=−cos(θ i)∈[−1,1]fori= 0, . . . , n−1(see Eqn. 12).
Let us denote [x]+ = max(x,0) , ζz = softplus(ρ z), and ζy = softplus(ρ y) for
some trainable parametersρ z andρ y. For the frame qubit, at each turntapply
RY (vt)R Z(ut), u t =ζ z [c t,f ]+, v t =ζ y [−ct,f ]+,(6)
where softplus(x) = log(1 +e x) with d dx softplus(x) =σ(x). Thus a loss-framing
term ct,f >0 drives the Z-axis, whereas a recovery framing turn ct,f <0 the Y -axis
with trainable gains. Further, note that the application of RY (µ) on qf in the Read-out
block realizes the observable
M(µ) =R † Y (µ)Z RY (µ) = cosµ Z−sinµ X,pull t f =−⟨M(µ)⟩ t.(7)
Finally, observe from Proposition 3 that at µ=±π/2 the frame channel is provably
order-blind.
Now we introduce trainable entangler gates that interact with the narrative qubit qn.
After the per-turn block, each of q0, . . . , qn−1, qf acts as the control of a controlled-RY
intoq n, defined by
Ue(φ) =
nY
j=0
CR qj →qn+1 Y (φj),pull t nar =−⟨Z n+1⟩t,(8)
where j= 0, . . . , n−1indexes the bias qubits and j=n the frame qubit, so there
are n+ 1 controls in all. At φj =π each gate is CNOT. This entangler facilitates the
strength of each bias’s contribution to narrative coherence, which is a learned quantity.
The qubit and gate complexities scale linearly with the number of cognitive biases.
For n biases the register holds n+ 2 qubits, the per-turn block Ur(t) contributes n+ 2
single-qubit rotations and no entangling gates, and the readout block contributes one
further rotation together with n+ 1 two-qubit controlled rotations. The circuit producing
st therefore comprisest(n+ 2) + 1rotations andn+ 1controlled rotations.
3 Joint Quantum-Classical Learning
We next describe a procedure for jointly learning the PQC parameters through the
RL agent. This coupling yields a hybrid quantum-classical learning framework that
6

q0: loss RY (∆t 0)
q1: commit RY (∆t 1)
q2: recip. RY (∆t 2)
q3: auth. RY (∆t 3)
q4: frame RZ(ut) RY (vt)
q5: narrative
(a) Per-turn block Ur(t), applied once
for each turn with that turn’s cue-
derived, trainable angles (4)–(6).
q0
q1
q2
q3
q4 RY (µ)
q5 RY (φ0) RY (φ1) RY (φ2) RY (φ3) RY (φ4)
(b) Readout block, applied to a copy of the state at
every turn: trainable basis rotation on q4, then the
trainable controlled-RY aggregation into q5. At
φj =πthese are CNOTs.
Figure 2: Gate-level structure of the parameterized quantum-cognitive encoder. All
angles shown are functions of the trainable parameters Θ and of the current turn’s cues.
falls within the broader paradigm of quantum reinforcement learning. At every turn
t, the agent observes the learned risk feature vector st (Eqn. (1)) which form the
Markov Decision Process (MDP) space for the RL framework. We define the action
space as A={WAIT,FLAG} , where FLAGterminates the episode, WAITadvances
deterministically, so Pr(st+1 |s t,WAIT) = 1 and the only stochasticity is in which
conversation is drawn. Rewards are defined asr(s t,WAIT) = 0and
r(st,FLAG) =
(
−Pfa label= 0,
B βmax(0, t−t∗) label= 1,
with a terminal penalty Pmiss for reaching the end of a fraud conversation without
flagging. Here t∗ is the labelled critical loss turn, β <1 discounts late-but-correct
detections, Pfa is the false-alarm penalty and B the detection bonus, and labels 0 and
1 denote benign and fraud conversations respectively. We use Pfa = 20, Pmiss = 10,
B= 10 , β= 0.8 and γ= 0.98 , with a 20/80 fraud/benign base rate. We note that
the base rate is not incidental to this choice: at a 50/50 rate with Pfa = 5 the expected
reward of blind flagging is 0.5(+10) + 0.5(−5) = +2.5>0 , so “always flag at t= 0 ”
is the genuine optimum of the reward function, and Q-learning correctly finds it.
In our proposal, the RL agent approximates the action-value function linearly instead
of a neural network based action-value function. Thus, the action-value function is
defined as QΘ,W (st, a) =wa ·s t(Θ) which stays linear in the encoder’s output. Thus
our model can be interpreted as a PQC feature map composed with a two-row linear
head, and all nonlinearity and all representational capacity beyond that head live in the
7

Algorithm 1PQC encoding of a conversation (nbiases,n+ 2qubits)
1:procedureENCODE({c t}T t=1,Θ)
2:|ψ⟩ ← |0⟩ ⊗n ⊗ |+⟩ ⊗ |0⟩;θi ←0fori= 0, . . . , n−1;Φ←[ ]
3:fort= 1toTdo
4:fori= 0ton−1do▷bias qubits
5:g←σ(w ict,i +b i);∆←(π−θ i)g;θ i ←θ i + ∆
6:|ψ⟩ ←

RY (∆)onq i

|ψ⟩
7:end for
8:u←softplus(ρ z) [ct,f ]+;v←softplus(ρ y) [−ct,f ]+
9:|ψ⟩ ←

RY (v)RZ(u)onq n

|ψ⟩▷frame qubit, non-commuting
10:|χ⟩ ←

RY (µ)onq n

|ψ⟩▷readout copy: separate execution
11:forj= 0tondo
12:|χ⟩ ←CR qj →qn+1 Y (φj)|χ⟩
13:end for
14:s t ←

−⟨χ|Z0|χ⟩, . . . ,−⟨χ|Zn+1|χ⟩,1−e −t/τ0 ,1  ; appends t toΦ
15:end for
16:returnΦ
17:end procedure
circuit. Given the semi-gradient temporal-difference (TD) error
δt =r t +γmax a′ Q(st+1, a′)−Q(s t, at),(9)
with the bootstrap target treated as constant, the classical head follows the usual update
wat ←w at +α w δt st, and the same error drives the circuit parameters,
Θ←Θ +α Θ δt ∇ΘQ(st, at),∇ ΘQ(st, at) =
n+2X
k=1
[wat ]k
∂[s t]k
∂Θ .(10)
The details of the learning through gradients mechanism is described in the Supplemen-
tary Section 7.2. Algorithms 1 and 2 give the full procedure.
4 Numerical Simulations with Synthetic Data
Since we do not have access to real affinity/romance-fraud conversation transcripts, as
it is not reported in the literature to the best of our knowledge, we generate synthetic,
explicitly labelled conversations, described precisely below so the process is fully
reproducible. In our generative process, each conversation has T turns (T= 14 for the
base classes). We divide T into 6 equal-length stages using boundaries stage_bounds=
⌊linspace(0, T,7)⌋(so, e.g., T= 14 gives stage boundaries at turns 0,2,4,7,9,11,14 ),
mirroring the six-stage structure documented for recovery/romance-investment scams in
the fraud related cognitive psychology literature [33, 23]: contact, rapport, reciprocity
hook, authority-backed big ask, loss event, recovery pressure. Each stages∈ {0, . . . ,5}
8

Algorithm 2Joint training of the PQC encoder and the RL detector
Require: labelled conversations ({ct}, y, t∗); rates αw, αΘ; discount γ; schedule ϵ;
constantsP fa, Pmiss, B, β; anchorλ; warm-upE0
Ensure:trainedΘandW= (w WAIT, wFLAG )
1:W∼ N(0,0.01 2);Θ←Θ 0;ν←0
2:forepoche= 1, . . . , Edo
3:foreach conversation, shuffleddo
4:Φ← ENCODE( {ct},Θ ); J←∂Φ/∂Θ by (16) if e > E0; G←0 ,
m←0
5:fort= 1toTdo
6:a t ←ϵ-greedy w.r.t.Q(s t, a) =wa ·s t
7:computer t and the target;δ t ←TD error
8:¯w←w at ▷retain the pre-update head weights
9:w at ←w at +α w δt st
10:ife > E 0 then
11:G←G+δ t ¯w⊤ 1:n+2Jt;m←m+ 1
12:end if
13:ifa t =FLAGthen break
14:end for
15:ife > E 0 andm >0then
16:G←G/m−λ(Θ−Θ 0);G←G/max(1,∥G∥)
17:ν←0.9ν+ 0.1G ⊙2;Θ←Θ +α Θ G⊘( √ν+ 10 −6)
18:end if
19:end for
20:end for
21:returnΘ, W
has a fixed base cue profile b(s) = (b(s) loss, b(s) commit, b(s) recip, b(s) auth, b(s) frame), given in Table 1 for
the FRAUDclass.
For every turntfalling in stagesthe cue values are drawn as
ct,i = clip

b(s) i +ε, ℓi, ui  , ε∼ N(0, σ 2),(11)
independently for each of the five channels, with (ℓi, ui) = (0,1) for the bias channels
and (−1,1) for the frame channel. The generator produces five classes, two positive and
three negative. FRAUDfollows Table 1 over T= 14 turns with σ= 0.10 on all channels.
SUBTLEFRAUDuses the same staged schedule over T= 18 turns with the bias profile
scaled by 0.4 and the frame profile by 0.5, giving a slower, lower-intensity escalation.
Among the negatives, BENIGNuses a single flat profile (0.08,0.10,0.08,0.15,0.0) with
σ= 0.05 ; LEGITURGENTuses a flat profile (0.35,0.12,0.05,0.20,0.0) with σ= 0.08 ,
representing a bona fide financial conversation with genuinely elevated loss and ur-
gency discussion but no reciprocity hook, no authority escalation and no reframing; and
PUSHYSALESis a staged hard negative that mimics the funnel’s escalation of reciprocity
(0.60 at the hook stage), authority (0.55) and commitment (0.60) but contains neither
a loss event nor any reframing ( ct,f ≡0 ), with σ= 0.10 on the bias channels and
9

Table 1: FRAUDclass base cue profileb (s) by stage (Eq. 11).
Stage loss commit recip. auth. frame
Contact 0.05 0.05 0.05 0.10 0.0
Rapport 0.10 0.25 0.10 0.20 0.0
Reciprocity hook 0.10 0.30 0.65 0.30 0.0
Authority + big ask 0.20 0.45 0.30 0.60 0.0
Loss event 0.70 0.55 0.15 0.40−0.8
Recovery pressure 0.65 0.75 0.20 0.55+0.8
0.08 on the frame channel. Positives are drawn evenly from FRAUDand SUBTLE-
FRAUD; negatives are 35% BENIGN, 30% LEGITURGENTand 35% PUSHYSALES.
Consequently PUSHYSALESoverlaps substantially with fraud when only the four bias
channels are considered, while retaining a benign label. We use 300 training and 300
test conversations at a20% fraud base rate and report results averaged over three random
seeds.
The initial values for ρz =ρ y are considered as 0.5413 =softplus −1(1), so
ζz =ζ y = 1, unit gain i.e. a maximal framing cue |ct,f |= 1 produces a one-rotation
on that turn. The equal values encode no prior that one framing direction matters more
than the other.
4.1 Simulation results
First, we introduce te following standard notations used in the sequel. Denoting TP,
FN, FP and TN as true positive (label=1, flagged at some run), false negative (label=1,
never flagged), false positive (label=0, flagged at some run), true negative (label=0,
never flagged), respectively, the False Positive Rule (FPR) is defined as FP/(FP+TN),
F1 (score) is defined as F1=(2 · Precision · Recall)/ (Precision + Recall), where Preci-
sion=TP/(TP+FP), Recall=TP/(TP+FN).
In Table 2 we report that joint training provides only a marginal benefit when the
encoder is already well calibrated. From the cognitive initialization the trained and
frozen encoders achieve comparable performance (F1 = 0.934±0.019 and 0.919±
0.051respectively), a difference of roughly one standard deviation that we do not read
as decisive. The difference is substantial under the mis-specified initialization, which
represents transfer to a domain with poorly calibrated parameters and rotation angles.
There the frozen encoder, i.e. RL-only learning, fails completely (F1 = 0.000), missing
all 62 fraud conversations, whereas end-to-end training from the same initialization
achieves the best performance in the table, F1 = 0.971±0.041 with no false positives.
Figure 3a shows that the two runs diverge only after the circuit is unfrozen. The same
reversal produces no change at all in a frame channel that is prepared in|0⟩ and measured
in theZbasis, consistent with Proposition 3.
Further, we note from Table 2 that removing the frame qubit causes detection
to collapse ( F1 = 0.000 ). With only the bias channels, and against PUSHYSALES
negatives that mimic the funnel’s bias escalation, the optimal policy under Pfa = 20
at a 20% base rate is to flag nothing. Whereas, removing only the narrative qubit is
comparatively benign. Figure 4 shows the reason after training, the frame channel is
10

Table 2: Detection quality on the hard synthetic benchmark (300 test conversations, 20%
fraud base rate, mean ± s.d. over three seeds). Lateness is the mean flag turn minus
the labelled critical loss turn, over true positives; it is undefined for configurations that
never flag.
ConfigurationF 1 FPR Lateness FN
PQC, joint, cognitive init0.934±0.019 0.000 +2.19 7.7
PQC, frozen, cognitive init0.919±0.051 0.000 +1.68 9.0
Classical cue baseline0.899±0.020 0.000 +0.99 11.3
PQC, frozen, mis-specified init0.000±0.000 0.000—62.0
PQC, joint, mis-specified init0.971±0.0410.000 +1.37 3.3
PQC, joint, no frame qubit0.000±0.000 0.000—62.0
PQC, joint, no narrative qubit0.937±0.015 0.000 +2.19 7.3
PQC, joint, bias qubits only0.000±0.000 0.000—62.0
the one that separates fraud from pushy sales, rising from −1 to −0.08 after the loss
event while remaining pinned at −1 for both negative classes, whereas the loss and
authority channels saturate on all three. Detection timing is also sequence-dependent at
the decision level (Fig. 3b).
(a) Joint versus frozen training
 (b) Effect of turn-order shuffling on detection
timing
Figure 3: Training and order-sensitivity results. (a) Joint training enables the mis-
specified encoder to adapt after warm-up, whereas the frozen encoder fails to flag. (b)
Detection timing under turn-order shuffling with cue content held fixed.
5 Limitations and Future Work
Several limitations of the present framework motivate future work. First, a quantum
hardware implementation introduces additional cost and noise. Estimating ⟨Zi⟩ requires
finite-shot measurements, and measurement at turnt destroys the quantum state; hence, a
T -turn trajectory requires T independent circuit executions, with total costO(T×shots)
per conversation. Training further multiplies this cost by the 2|G| shifted evaluations
11

Figure 4: Risk-feature trajectories at the cognitive initialization (top) and after joint
training (bottom), for a fraud conversation, a pushy-sales hard negative, and a benign
conversation. Training sharpens the frame channel into the discriminator that separates
fraud from pushy sales, while the loss and authority channels saturate on all three
classes.
required by (16), while shot noise in the TD error δt compounds the intrinsic variance
of TD learning. A systematic shot-noise analysis is therefore left for future work.
Next, joint optimization remains fragile because the semi-gradient TD update operates
on a moving feature map. Warm-up, anchoring, and adaptive gradient scaling are
required for stability, with the anchor strength introducing a tradeoff between stability
and adaptability, policy-gradient methods or fitted-Q learning with a target network
may provide more robust alternatives. Finally, the present evaluation relies entirely on
synthetic conversations constructed around the funnel structure encoded by the model.
In addition, the NLP front end that maps raw text to per-turn cue vectors is currently
specified but not independently implemented or validated, and errors in cue extraction
would propagate directly to the circuit through the angle map in (4).
6 Conclusion
We proposed a hybrid quantum-classical pipeline in which a structured parameterized
quantum circuit encodes manipulation-relevant cognitive biases such as loss aversion,
commitment, reciprocity, authority together with an order-sensitive frame qubit and a
narrative-coherence aggregator, and is trained jointly with a classical reinforcement-
learning agent that learns when to flag a conversation. On synthetic conversations
with hard negatives, an encoder that is useless when frozen and at a mis-specified
initialization becomes the best-performing configuration when trained end-to-end, and
the frame qubit proves necessary for detection.
12

References
[1] Amira Abbas, David Sutter, Christa Zoufal, Aurélien Lucchi, Alessio Figalli, and
Stefan Woerner. The power of quantum neural networks.Nature computational
science, 1(6):403–409, 2021.
[2] Tom Buchanan and Monica T Whitty. The online dating romance scam: causes
and consequences of victimhood.Psychology, Crime & Law, 20(3):261–283,
2014.
[3] Francois Buet-Golfouse, Osian Shelley, and George-Octavian Barbulescu. Be-
havioural reinforcement learning (beyond rationality: Rl under investor bias). In
Proceedings of the 6th ACM International Conference on AI in Finance, pages
344–351, 2025.
[4] Jerome R Busemeyer and Peter D Bruza.Quantum models of cognition and
decision. Cambridge University Press, 2012.
[5] Jerome R Busemeyer, Emmanuel M Pothos, Riccardo Franco, and Jennifer S
Trueblood. A quantum theoretical explanation for probability judgment errors.
Psychological review, 118(2):193, 2011.
[6] Jerome R Busemeyer and Zheng Wang. What is quantum cognition, and how is it
applied to psychology?Current Directions in Psychological Science, 24(3):163–
169, 2015.
[7] Claire Cardie. A cognitive bias approach to feature selection and weighting for
case-based learners.Machine Learning, 41(1):85–116, 2000.
[8] Samuel Yen-Chi Chen. Quantum reinforcement learning: Concepts and applica-
tions.Quantum Computational AI, pages 3–23, 2026.
[9] Robert Cialdini and Robert B Cialdini.Influence: Science and practice. Allyn &
Bacon, Boston, MA., 2013.
[10] Anna Coluccia, Andrea Pozza, Fabio Ferretti, Fulvio Carabellese, Alessandra
Masti, and Giacomo Gualtieri. Online romance scams: Relational dynamics
and psychological characteristics of the victims and scammers. a scoping review.
Clinical practice and epidemiology in mental health: CP & EMH, 16:24, 2020.
[11] Filipa de Almeida, Ian J Scott, Jerônimo C Soro, Daniel Fernandes, André R Ama-
ral, Mafalda L Catarino, André Arêde, and Mário B Ferreira. Financial scarcity
and cognitive performance: A meta-analysis.Journal of Economic Psychology,
101:102702, 2024.
[12] Thomas Dearden, Jill O Jasperson, and Ronald Mellado Miller. Mechanisms of
affinity fraud victimization.Journal of Financial Crime, 32(1):64–76, 2025.
[13] Riccardo Franco. The conjunction fallacy and interference effects.Journal of
Mathematical Psychology, 53(5):415–422, 2009.
13

[14] Dinesh Gabhane, A Sharma, and Rupam Mukherjee. Behavioral finance: exploring
the influence of cognitive biases on investment decisions.Boletin de Literatura
Oral-The Literary Journal, 10(1):3133–3141, 2023.
[15] VP Syed Abdullahil Hammad and M Marimuthu. Cognitive biases and port-
folio decisions: A neurofinance perspective on investor irrationality.Scriptora
International Journal of Research and Innovation (SIJRI), pages 14–23, 2026.
[16] Daniel Kahneman and Amos Tversky. Prospect theory: An analysis of decision
under risk. InHandbook of the fundamentals of financial decision making: Part I,
pages 99–127. World Scientific, 2013.
[17] Danish Kaleem and Ken Ferens. A cognitive approach for attribute selection
in internet dataset. In2017 IEEE 16th International Conference on Cognitive
Informatics & Cognitive Computing (ICCI* CC), pages 319–328. IEEE, 2017.
[18] Polina Khrennikova. Order effect in a study on us voters’ preferences: quantum
framework representation of the observables.Physica Scripta, 163(1):014010,
2014.
[19] Stephen EG Lea, Peter Fischer, and Kath M Evans. The psychology of scams:
Provoking and committing errors of judgement. 2009.
[20] Nico Meyer, Christian Ufrecht, Maniraman Periyasamy, Daniel D Scherer, Axel
Plinge, and Christopher Mutschler. A survey on quantum reinforcement learning.
arXiv preprint arXiv:2211.03464, 2022.
[21] Michael A Nielsen and Isaac L Chuang.Quantum computation and quantum
information, volume 2. Cambridge university press Cambridge, 2001.
[22] Frank S Perri and Richard G Brody. Birds of the same feather: the dangers of
affinity fraud.Journal of Forensic Studies in Accounting and Business, 3(1):33–46,
2011.
[23] Anthony Pratkanis and Doug Shadel. Weapons of fraud: A source book for fraud
fighters. 2005.
[24] Kai Ruggeri, Giampaolo Abate Romero Landini, Katharina Busch, Valentina
Cafarelli, Barbora Doubravová, Deniz Gurol, Melika Miralem, Fredrik Nilsson,
Sarah Ashcroft-Jones, and Friederike Stock. Financial decision-making, income,
cognitive biases: The impact of economic systems and environments on behavior
in six countries. 2024.
[25] Kai Ruggeri, Sarah Ashcroft-Jones, Giampaolo Abate Romero Landini, Narjes Al-
Zahli, Natalia Alexander, Mathias Houe Andersen, Katherine Bibilouri, Katharina
Busch, Valentina Cafarelli, Jennifer Chen, et al. The persistence of cognitive biases
in financial decisions across economic groups.Scientific Reports, 13(1):10329,
2023.
14

[26] US Securities, Exchange Commission, et al. Affinity fraud: how to avoid invest-
ment scams that target groups, 2013.
[27] Maciej Tkacz, Celina Olszak, Jozef Zurada, and Paweł Weichbroth. Exploration
of behavioral patterns and cognitive biases among stock market investors. 2025.
[28] Jennifer S Trueblood and Jerome R Busemeyer. A quantum probability account of
order effects in inference.Cognitive science, 35(8):1518–1552, 2011.
[29] Amos Tversky and Daniel Kahneman.Judgment under uncertainty: Heuristics
and biases, volume 185. American Association for the Advancement of Scienc.
[30] Amos Tversky and Daniel Kahneman. Extensional versus intuitive reasoning:
The conjunction fallacy in probability judgment.Psychological review, 90(4):293,
1983.
[31] Hado Van Hasselt, Yotam Doron, Florian Strub, Matteo Hessel, Nicolas Sonnerat,
and Joseph Modayil. Deep reinforcement learning and the deadly triad.arXiv
preprint arXiv:1812.02648, 2018.
[32] Hongbin Wang, Todd R Johnson, and Jiajie Zhang. The order effect in human ab-
ductive reasoning: An empirical and computational study.Journal of Experimental
& Theoretical Artificial Intelligence, 18(2):215–247, 2006.
[33] Monica T Whitty and Tom Buchanan. The online romance scam: A serious
cybercrime.CyberPsychology, Behavior, and Social Networking, 15(3):181–183,
2012.
[34] Dominic Widdows, Jyoti Rani, and Emmanuel Pothos. Quantum circuit compo-
nents for cognitive decision-making.arXiv preprint arXiv:2302.03012, 2023.
15

7 Supplementary
7.1 Mathematical Foundations
Recall that ann-qubit state is|ψ⟩ ∈C 2n . The Pauli matrices of order2are
X=
0 1
1 0

, Y=
0−i
i0

, Z=
1 0
0−1

,
along with the identity I2 =
1 0
0 1

. Then the single-qubit rotations that we consider
in this paper are: RY (θ) =e −iθY /2= cos(θ/2)I−isin(θ/2)Y , and similarly for RZ.
The observables we consider as the Pauli Z matrix and ⟨Z⟩=⟨ψ|Z|ψ⟩ ∈R denotes
the expected value of the measurement outcomes, see [ 21] for basics of quantum
computation.
Now we have the following propositions, whose proofs are computational and easy
to verify. The Lie bracket for two operators A, Bis defined as [A, B] =AB−BA,
which is the zero matrix only when they commute. Proposition 1 describes the frame-
order dependence, whereas Proposition 2 shows that no joint measurement can produce
the conjunction fallacy.
Proposition 1. [RY (θ), RZ(ϕ)] =−2isin(θ/2) sin(ϕ/2)X , which vanishes only for
trivial rotation angles; for any otherθ, ϕ,RY (θ)RZ(ϕ)̸=R Z(ϕ)RY (θ).
Proposition 2.For any two qubits qA, qB in any joint state,P(A∧B)≤min(P(A), P(B)) ,
since Born-rule outcome probabilities p00, p01, p10, p11 ≥0 summing to 1 give P(A∧
B) =p 11 ≤p 10 +p 11 =P(A), and symmetrically forB, regardless of entanglement.
Proposition 2 shows that the conjunction fallacy cannot be reproduced by asingle
joint measurementof two qubits, however they are entangled. Indeed, the Fréchet
bound follows from non-negativity of the Born-rule outcome probabilities alone. This
does not contradict the quantum-cognitive account of the fallacy, which obtains it from
sequential incompatiblemeasurements rather than a joint one [ 5]. It does, however,
determine our design: the narrative qubit is used not to violate the bound but as an
order-insensitive coherence aggregate, while order sensitivity is carried entirely by the
frame qubit through Proposition 1.
Next, we show that the expected value ⟨Zi⟩ for any bias qubit i after applying a rota-
tion gate RY (θ) is given by cosθ for the initial state |0⟩. Note that |ψ⟩=R Y (θ)|0⟩=
cos θ 2 |0⟩+ sin θ 2 |1⟩.Then
⟨Z⟩=⟨ψ|Z|ψ⟩= cos 2 θ 2 −sin 2 θ 2 = cosθ.(12)
Then applying a sequence of RY gates, only amplify the rotation angle, and hence it
remains cosine of the total rotation angle. Then note that −⟨Zi⟩=−cosθ i is a strictly
monotonic function on[0, π].
Next we have the following Proposition, which establishes the order-blind of the
measurement bases.
16

Proposition 3.Let the frame qubit be prepared in |+⟩ and let one loss-framing event
RZ(u) and one recovery-framing event RY (v) occur, in either order. Write⟨·⟩ZY for
the stateR Y (v)RZ(u)|+⟩and⟨·⟩ Y ZforR Z(u)RY (v)|+⟩. Then
⟨X⟩ ZY =⟨X⟩ Y Z= cosucosv,⟨Z⟩ ZY − ⟨Z⟩Y Z= sinv(1−cosu),(13)
and consequently, for the observableM(µ)of(7),

⟨M(µ)⟩ ZY − ⟨M(µ)⟩Y Z

 =

cosµ

 sinv(1−cosu).(14)
The order effect is therefore zero atµ=±π/2 and maximal at µ∈ {0, π}. Moreover,
for a frame qubit prepared in |0⟩ and measured in the Z basis, any prefix consisting
solely of RZ rotations leaves ⟨Z⟩ unchanged, so such a frame channel cannot register
loss-framing that is not followed by recovery-framing.
Proof. On the Bloch sphere |+⟩ is (1,0,0) . RZ(u) rotates by u about z, RY (v) by
v about y. Applying RZ then RY gives (cosucosv,sinu,−cosusinv) ; applying
RY then RZ gives (cosvcosu,cosvsinu,−sinv) . The x components agree and the
z components differ by sinv−cosusinv . Substituting into ⟨M(µ)⟩= cosµ⟨Z⟩ −
sinµ⟨X⟩gives (14). The final claim is immediate fromR Z(u)|0⟩=e −iu/2 |0⟩.
Proposition 3 is the reason the readout angleµ is a trained parameter and is initialized
at −π/4 rather than at the natural-looking −π/2 (which measures X exactly, and is
precisely the blind point).
The following Proposition provides a closed form expression of the narrative qubit’s
readout.
Proposition 4.Every gate of the per-turn block acts on a single qubit, so |ϕ(t)⟩ is a
product state N j |ϕj(t)⟩. Let pj =|⟨1|ϕ j(t)⟩|2 for j= 0, . . . , n(for j=n , after the
readout rotation RY (µ)). Then the gates of Ue(φ) in (8) pairwise commute, each leaves
its own control’s⟨Z j⟩invariant, and
⟨Zn+1⟩= Re
nY
j=0

1 +p j

eiφj −1  .(15)
Proof. All the gates of Ue share the target qn+1 and rotate it about the same axis, and
their controls are diagonal, so they commute pairwise; a controlled gate is diagonal
on its control, hence leaves ⟨Zj⟩ unchanged. Conditioned on the control bitstring z∈
{0,1} n+1, which occurs with probabilityQ j pzj j (1−p j)1−zj because the controls are in
a product state, the target evolves as RY
P
j zjφj

|0⟩ and contributes cos
P
j zjφj

to ⟨Zn+1⟩. Averaging and writing cosx= Ree ix factorises the sum over z into the
product (15).
Remark 1.By Proposition 4, the full feature trajectory {st}T t=1 can be evaluated in
O(nT) classical arithmetic operations, without forming the 2n+2-dimensional stat-
evector. The role of the quantum formalism here is representational. It supplies a
non-commutative, interference-based inductive bias matched to documented judgement
phenomena not computational. Quantum hardware implementation of the proposal
would invite additional challenges, which is left as future work.
17

Next we have the following propositions, which shows that the entangler defined by
CNOT gates is stationary.
Proposition 5.With⟨Z n+1⟩as in(15)andf l = 1 +p l(eiφl −1),
∂⟨Zn+1⟩
∂φj
= Re
h
i pjeiφj
Y
l̸=j
fl
i
.
At φ=π1 every fl = 1−2p l is real, so the bracket is purely imaginary and the
derivative vanishes for every j, every t, and every input. The point φ=π1 is thus
a critical point of the narrative readout and the second derivative is strictly negative.
Consequently, it is a local maximum of the narrative contrast.
Observe that the Proposition 5 explains why the CNOT aggregation of a fixed
encoder could be a sensible design choice for the encoder. Besides, it also establishes our
observation in numerical simulations that the entangler angles do not move when training
starts from Θ0, in fact the the first-order signal is identically zero there. Accordingly,
the evidence that training φ helps comes only from the mis-specified runs, which start
away from the stationary point. Initializing φj such as π−0.2 removes the degeneracy
at negligible cost to interpretability.
7.2 Gradients through the circuit and the joint training
Note that Eqn. (10) is the entire quantum-classical interface. The RL agent’s surprise
at turn t is projected through its own weights onto the Jacobian of the Born-rule
expectations with respect to the gate parameters. Besides, nothing about the conversation
reaches the agent except the register’s readout, and nothing about the labels reaches the
circuit exceptδ t.
The Jacobian is obtained on hardware by the parameter-shift rule composed with
the chain rule through the classical angle map. Writing G for the set of parameterised
gate occurrences in the circuit that producess t, andη g for the angle of occurrenceg,
∂⟨O⟩
∂Θ =
X
g∈G
1
2
h
⟨O⟩ηg+π/2 − ⟨O⟩ηg−π/2
i
| {z }
parameter shift
· ∂ηg
∂Θ ,(16)
which costs 2|G|= 2

t(n+2) + (n+ 2)

circuit evaluations per turn, for any observable
O. Note that the second factor is not a plain derivative because the angle map (4) is
recurrent since ∆t i depends on θt−1 i , and hence on all earlier cues but the recursion
admits a closed form representation. The following lemma provides gradients of the
saturating accumulation.
Lemma 1.With gs i =σ(w ics,i +b i) and θt i as in (5), and writing P t i = Q s≤t(1−g s i ),
∂θ t i
∂wi
=π Pt i X
s≤t
gs i cs,i, ∂θ t i ∂bi =π Pt i X s≤t gs i .(17)
18

Table 3: Notation used in Algorithm 2.
Symbol Meaning
Episode (one labelled conversation)
Tnumber of turns
ct ∈[0,1] n ×[−1,1]cue vector at turntfrom the NLP front end
y∈ {0,1}conversation label;1= fraud
t∗ labelled critical loss turn (first turn of the loss stage)
Quantum encoder
Θ∈R 3n+4 circuit parameters, Eq. (3)
Θ0 cognitive initialisation (φj =π,µ=−π/4)
Φ = (s1, . . . , sT )encoded feature trajectory for the episode
st ∈R n+4 state at turnt, Eq. (1)
Jt =∂(s t)1:n+2/∂ΘJacobian of the Born-rule features,(n+2)×(3n+4)
Reinforcement learner
A={WAIT,FLAG}action set; FLAGis terminal
W= (w WAIT, wFLAG )linear head,w a ∈R n+4
Q(st, a) =wa ·st action-value function
at,r t action taken and reward received at turnt
δt temporal-difference error, Eq. (19)
γ= 0.98discount factor
ϵexploration probability, annealed1→0.05
Pfa, Pmiss, B, βfalse-alarm penalty, miss penalty, detection bonus, lateness discount
Optimization
E,E 0 total epochs (30) and warm-up epochs (⌊0.34E⌋= 10)
αw = 0.02,α Θ = 0.003learning rates for head and circuit
G∈R 3n+4,maccumulated circuit gradient and its step count
λ= 0.02anchor strength towardΘ 0
νRMSProp running second moment
⊙,⊘elementwise square, elementwise division
Proof.∂log(1−g s i )/∂wi =−g s i (1−g s i )cs,i/(1−g s i ) =−g s i cs,i, so ∂P t i /∂wi =
−P t i P s≤t gs i cs,i; substitute into θt i =π(1−P t i ). The bi case is identical with cs,i
replaced by1.
If both running sums are accumulated online, the classical factor in (16) costs O(n)
per turn. In the simulations of Section 4 we evaluate the same derivative exactly and
analytically from Proposition 4 and Lemma 1; we verified this implementation against
central finite differences over all 16 parameters and all 6 observables at every turn, with
maximum absolute discrepancy1.0×10 −9.
7.3 Algorithm 2
In this section we explain the execution of the Algorithm 2. First, we include all the
notations in Table 3.
19

The head W is initialized near zero and the circuit at the cognitive point Θ0, so
the very first policy is uninformed but the very first feature map is a hand-designed
encoder. Note that τ0 >0 is a fixed time constant, in units of turns, that sets the
scale over which the saturating time feature 1−e −t/τ0 distinguishes early from late
turns. We use τ0 = 5, so the feature reads 0.63 at t=τ 0 and 0.93 at the final turn
of a T= 14 conversation. Each epoch sweeps the labelled conversations in a fresh
random order. For one conversation the encoder is invoked once (per visit), before the
agent acts, and it returns the entire trajectory Φ = (s1, . . . , sT ) together with (when the
circuit is unfrozen) the stack of per-turn Jacobians J1, . . . , JT , Jt =∂(s t)1:n+2/∂Θ∈
R(n+2)×(3n+4), the Jacobian of the Born-rule features at turn t with respect to the
circuit parameters; row k is ∂

−⟨Zk⟩t

/∂Θ and the time and constant components of
st are omitted as they do not depend on Θ (see Eq. (16)). The agent then replays that
pre-computed trajectory turn by turn, choosinga t at each row.
Note that, during theE0 warm-up epochs, the Jacobians are not formed at all. Indeed,
Φ costs one forward sweep, whereas each Jt costs 2|G| shifted circuit evaluations. Thus,
where the saturating recursion θt i =θ t−1 i + ∆t i passes through every prefix on its
way to t=T and so yields all T states in a single pass. On hardware, measurement
collapses the state, so the trajectory genuinely requires T separate circuit executions;
what encoding once per episode avoids there is a further factor of T from re-encoding
inside the agent loop.
At turn t the agent evaluates Q(st, a) =w a ·s t for both actions and selects at
ϵ-greedily, meaning that with probability 1−ϵ it takes the currently best-estimated
action arg maxa Q(st, a)and with probability ϵ it ignores its own estimate and samples
uniformly fromA={WAIT,FLAG}.Thus,
at =
(
arg maxa∈A Q(st, a)with probability1−ϵ,
Uniform(A)with probabilityϵ.
(18)
At evaluation we set ϵ= 0 , so the reported detector is the deterministic greedy policy
a∗ t = arg maxa Q(st, a).
The reward and bootstrap target follow the three cases of the stopping problem:
if at =FLAG the episode terminates and rt is −Pfa on a benign conversation or
Bβ max(0,t−t∗) on a fraudulent one, with no bootstrap term; if the agent reaches the
last turn still waiting, it receives −Pmiss when y= 1 and 0 otherwise, again with no
bootstrap; otherwise rt = 0 and the target is γmax a′ Q(st+1, a′). Thus the temporal-
difference error is given by
δt =

target

−Q(s t, at)(19)
which measures how wrong the current estimate was, and it drives both halves of the
model. The classical head takes its usual semi-gradient step wat ←w at +α wδtst
immediately. The circuit’s contribution for this turn, δt (wat )⊤ 1:n+2Jt, is not applied
immediately but accumulated into G: this is the chain rule of Eq. (10), which captures
“how much would each gate angle have had to change to move Q(st, at) toward its
target". Only the first n+ 2 components of ¯wappear because the time feature and the
constant do not depend onΘ. Choosing FLAGbreaks the turn loop.
20

Note that both updates are gradients of the same objective 1 2  target−Q(s t, at) 2
under the semi-gradient convention, so both must be evaluated at the same parameters.
Substituting the already-updated head weights instead perturbs the circuit gradient by
δt

wnew at −¯w ⊤ 1:n+2Jt =α w δ2 t (st)⊤ 1:n+2Jt,(20)
which, being proportional to δ2 t ≥0 , is a sign-definite drift along s⊤ t Jt rather than
zero-mean noise. Thus it systematically inflates whichever channels are currently large,
and does so most strongly on exactly the episodes the agent finds most surprising.
After the episode, G is divided by the number m of turns that contributed, so a
conversation flagged at turn 2 does not receive a smaller circuit update than one that
ran to turn 14. The anchor term −λ(Θ−Θ 0) is then subtracted, a quadratic pull back
toward the cognitive initialization, G is clipped to unit norm, and the step is scaled
per coordinate by an RMSProp second moment ν, so that parameters of very different
sensitivity, a cue gain wi and an entangler angle φj move the features by quite different
amounts, take comparable steps. Two guards make this stable. The circuit is frozen
for the first E0 epochs, so the feature map does not move while the Q-values are
still random, and the anchor bounds how far the learned encoder can drift from the
documented baseline, which is a governance property as much as an optimization one.
Finally, note that nothing about the conversation reaches the agent except the
register’s readout st(Θ), and nothing about the labels reaches the circuit except the
scalar δt. The encoder is therefore not trained to classify turns. In fact, it is trained to
make the stopping decision easier, under the same cost asymmetry the deployed detector
faces. This distinguishes Algorithm 2 from fitting a quantum feature map to labels and
then bolting an agent onto it.
It is worth stating explicitly that neither Θ nor W is trained by minimizing a loss.
Indeed, the per-turn squared error
Lt(Θ, W) =1 2  yt−QΘ,W (st, at) 2 , y t =
(
rt terminal step,
rt +γmax a′ Q(st+1, a′)otherwise,
(21)
is a surrogate whose target yt is held fixed during differentiation even though it depends
on Θ and W through Q(st+1,·) . Thus, the update direction δt∇Θ,W Q(st, at) omits
the term −γ∇max a′ Q(st+1, a′) (it is not ∇Lt) and hence it is not the gradient of
any fixed scalar function, so semi-gradient temporal-difference learning is a stochastic
approximation to a fixed point of the projected Bellman optimality operator rather
than a descent method. The objective that is genuinely being optimized here is the
reinforcement-learning one, and because rt = 0 at every non-terminal step an episode’s
return collapses to a single discounted terminal reward, making the problem exactly one
of optimal stopping,
J(Θ, W) =E(c1:T , y, t∗)∼D

γ τ−1 Rτ  , R τ =



−Pfa y= 0, τ≤T,
B βmax(0,τ−t ∗) y= 1, τ≤T,
−Pmiss y= 1,never flagged,
0y= 0,never flagged,
(22)
21

where τ is the stopping time induced by the greedy policy. The one component of the
circuit update that is an exact gradient is the anchor, λ(Θ−Θ 0) =∇ Θ λ 2 ∥Θ−Θ 0∥2 2.
We therefore report mean episode return rather than a training loss throughout. Here D
denotes the distribution over labelled conversations, each draw being a triple(c1:T , y, t∗)
comprising a cue trajectory, its label, and its critical turn, with the horizonT itself part of
the draw; in our experiments D is the generative process of Section 4, and in deployment
it would be the population of monitored conversations.
7.3.1 Stability of the joint update mechanism
It is well-known that training a feature map with a semi-gradient TD error is the deadly
triad in miniature [ 31]. In particular, the TD targets are obtained by bootstrapping
from a function approximator whose underlying feature representation is itself being
updated during training. Consequently, both the value estimates and their feature
representation evolve simultaneously, which can lead to unstable learning dynamics. In
our experiments, such instability was not only associated with slower convergence, in
fact without appropriate stabilization, the joint update learning occasionally collapsed
to degenerate policies that either never issued a flag or flagged every conversation in
the early runs. To mitigate this behavior, we employ the following three stabilization
mechanisms.
• Warm-up.The parameters of the quantum circuit are kept fixed during the first
third of the training epochs. This allows the Q-function to acquire a meaningful
initial estimate before the feature representation itself is allowed to adapt.
• Anchoring.We regularize the circuit parameters toward their cognitively moti-
vated initial values by adding
−λ(Θ−Θ 0)
to the circuit gradient, with λ= 0.02 . This regularization constrains the learned
encoder to remain interpretable while still allowing it to adapt to the learning
objective. The parameter λ therefore controls a trade-off between interpretability
and adaptability. For example, with λ= 0.06 , the model is unable to recover
from the deliberately mis-specified initialization considered in Table 2.
• Per-episode, RMSProp-scaled steps.The circuit gradients are accumulated
and averaged over each episode, followed by norm clipping and scaling using
a running estimate of their second moment. The circuit learning rate is set
to αΘ = 0.003 . This procedure limits abrupt changes in the learned feature
representation caused by individual TD updates.
7.4 Synthetic data generation
In Figure 5, we describe our synthetic data generation process.
22

0 1 2 3 4 5 6 7 8 9 10 11 12 13
turn t
Contact Rapport Recip. hook Auth. + ask Loss event Recovery pressure
t * = 9
(a)
loss commit recip auth
Contact
Rapport
Reciprocity hook
Authority + big ask
Loss event
Recovery pressure
0.05 0.05 0.05 0.10
0.10 0.25 0.10 0.20
0.10 0.30 0.65 0.30
0.20 0.45 0.30 0.60
0.70 0.55 0.15 0.40
0.65 0.75 0.20 0.55
(b)
frame
+0.0
+0.0
+0.0
+0.0
-0.8
+0.8
(c)
0 5 10
turn
1.0
0.5
0.0
0.5
1.0
cue value
(d) Fraud
0 5 10
turn
(e) PushySales
loss commit recip auth frame
Figure 5:The synthetic conversation generator. (a)Each fraudulent conversation is
divided into six stages by the boundaries ⌊linspace(0, T,7)⌋, shown here for T= 14 ;
the labelled critical turn t∗ is the first turn of the loss-event stage (turn 9), and detection
lateness is measured relative to it.(b)Each stage s carries a fixed base level b(s) i ∈[0,1]
for the four bias channels.(c)The frame channel b(s) f ∈[−1,1] is zero for the first
four stages and non-zero only in the last two, with opposite signs, so every fraudulent
conversation contains exactly one RZ ↔R Y transition. By the sign convention of
Eq. (6), ct,f >0 is loss framing and drives RZ while ct,f <0 is recovery framing
and drives RY . (d,e)Sampled realizations, drawn as c(t,i) = clip(b(s) i +ε, ℓi, ui) with
ε∼ N(0, σ2), σ= 0.10 , independently per turn and per channel, so there is within-
stage variation but no autoregressive structure. Shading marks the stage, the dashed red
line markst ∗.
23
