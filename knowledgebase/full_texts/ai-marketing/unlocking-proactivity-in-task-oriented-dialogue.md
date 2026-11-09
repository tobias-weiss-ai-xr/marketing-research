---
title: Unlocking Proactivity in Task-Oriented Dialogue
url: https://arxiv.org/abs/2605.22240
category: ai-marketing
subcategory: empirical
date: 2026-05
venue: ''
authors:
- Azure Zhang
- Ning Gao
- Yuqin Dai
- Ruiyuan Wu
- Jinpeng Wang
source: arxiv
pdf_url: https://arxiv.org/pdf/2605.22240
pages: 12
chars: 44714
fetched_at: '2026-11-08T13:36:21+00:00'
kb_version: 1
---

# Unlocking Proactivity in Task-Oriented Dialogue

Unlocking Proactivity in Task-Oriented Dialogue
Azure Zhang1, Ning Gao1, Yuqin Dai1, Ruiyuan Wu1, Jinpeng Wang1, Rena Wei Gao1
Bingdong Tan2, Shuzheng Gao3, Zongjie Li4, Chaozheng WangB1
1Keeta AI, Meituan 2Independent Researcher
3CUHK, 4HKUST
BCorresponding Author
Abstract
Proactive task-oriented dialogue (TOD), such as outbound sales, demands a per-
suasive agent that actively probes the user’s concerns and steers the conversation
toward acceptance within a bounded number of turns. Yet post-trained LLMs are
inherently conservative, and reward-shaping RL (e.g., GRPO) struggles since it
only re-weights what an already passive policy samples. We show that condition-
ing on the user’s latent concerns unlocks proactive capability that no amount of
sampling can undermine, establishing these concerns as a pivotal training-time
signal. To operationalize this finding, we build theCognitive User Simulator,
which models each user as a stratified persona comprising observable external
traits and hidden internal concerns. The simulator produces faithful and diverse
interactions, while emitting per-turn state dynamics that track persuasion progress.
We then introduceSimulator-Induced Asymmetric-View Policy Optimization,
which converts the modeled concerns and the simulation state transition into com-
plementary training objectives: (1)Asymmetric On-Policy Self-Distillationthat
transfers concern-aware behavior from a privileged view of the same policy into
its deployable, conversation-only view; and (2)State-Transition Policy Refinement
where the final decision provides trajectory-level advantage while synchronous
state transitions refine turn-level credit direction. Across two real-world food-
delivery benchmarks (merchantandcourieroutbound recruitment), our method
matches or surpasses leading proprietary LLMs, outperforms strong RL baselines,
and generalizes across various LLM-based user simulators.
1 Introduction
Large Language Models (LLMs) have demonstrated strong conversational capabilities, leading
interests in applying them to task-oriented dialogue (TOD) [1–4]. Among TOD scenarios,proactive
settings such as outbound sales are especially challenging compared with conventional reactive ones,
where agents respond to users’ explicit and direct requests [1]: the agent must initiate or sustain the
interaction, push the dialogue toward a predefined goal, and persuade users to take a target action
[5]. These requirements impose two core demands beyond fluent response generation: agents must
identify users’ inherent concerns and implicit needsandproactively steer the conversation
toward acceptance.
However, these demands expose two structural gaps that existing approaches cannot bridge.Gap1:
Current user simulators lack modeling of the implicit concerns.Existing simulators typically
model only surface traits (e.g., tone, politeness) [5–7], which makes simulated users differ mainly in
style, causing dialogues to collapse into homogeneous trajectories with limited behavioral diversity.
Crucially, such surface traits do not capture thelatent concernsthat actually drive user decisions,
making simulator decisions weakly grounded and noisy.Gap2: LLMs are inherently reactive.
Standard alignment optimizes models torespondhelpfully rather than todrivethe conversation,
Preprint.
arXiv:2605.22240v2  [cs.AI]  3 Jun 2026

1.8 2.2 2.6 3.0 3.4
Proactivity score (LLM judge, 1--5)
20
30
40
50
60Acceptance rate (%)
REACTIVE  PLATEAU LATENT-CONCERN  REGIME
+32.2 pp
+30.3 pp
Vanilla
Pass@16
GRPO
+int
sampling / RL: small shift
+int: large unlock
Figure 1:Pilot study.Latent concerns move agents from the reactive plateau to the high-
proactivity/high-acceptance regime, whereas sampling and GRPO provide only small shifts.
leaving them ill-suited for the initiative-taking required by proactive TOD. Mitigating this gap with
current post-training formats proves equally difficult: SFT [ 8–10] lacks high-quality data, merely
mimicking surface utterances; RL methods [5, 7, 11, 12] struggle to credit the specific turns where
persuasion occurs, whether relying on sparse outcome rewards or LLM judges that score generic
dialogue quality rather than actual progress toward acceptance. These two gaps meet at the same
training intersection for LLMs: the user’s latent decision process. Without modeling the concerns
that guide user decisions, simulators cannot provide grounded decisions, and training methods cannot
identify which proactive turns actually resolve user resistance.
To further examine whether this missing variable limits current LLM policies, we conduct a pilot
study to evaluate the capability and proactivity of LLMs in proactive TOD. Figure 1 summarizes the
results in the (Proactivity, Acceptance Rate) plane. Vanilla models (e.g., Qwen3-4B/8B) anchor at
low operating points, and test-time scaling with Pass@16 leaves them clustered nearby, suggesting
that more sampling alone cannot elicit the required persuasive behaviors. Reward-shaping RL (e.g.,
GRPO) consequently exhibits a similar ceiling, as it can only re-weight behaviors already sampled
by the policy. By contrast, conditioning the same agents on users’ latent concerns yields substantial
gains in both proactivity and acceptance (dashed arrows). This confirms that the user’s latent concerns
are the critical missing variable: once provided, they unlock proactive capability that no amount of
sampling or reward shaping can recover, establishing latent concerns not merely as a simulator detail
but as a pivotal training-time signal for learning proactive policies.
Guided by this finding, we propose a co-designed framework that models latent concerns to build
a faithful training environment and then converts the resulting information into complementary
learning objectives. TheCognitive User Simulator (CUS)models each user as a stratified persona
comprising observable external traits, hidden internal concerns P int, and synchronous state dynamics.
By explicitly modeling the latent concerns that anchor user decisions, CUS produces behaviorally
diverse and faithful interactions, providing a high-fidelity training environment that surface-trait-only
simulators cannot offer. It further emits simulation feedback—the final accept/reject outcome and
per-turn internal state transitions—that records how user receptiveness changes in each turn. We
then introduceSimulator-Induced Asymmetric-View Policy Optimizationto convert the modeled
concerns and the simulation state into complementary training objectives. (1)Asymmetric On-Policy
Self-Distillation (AOPD)evaluates asinglepolicy under two asymmetric information views: a
privileged view that additionally conditions on P int, and a deployable view that observes only the
dialogue history. The privileged view’s concern-aware behavior is progressively distilled into the
deployable one, requiring no separate teacher model and enabling the agent to implicitly infer and
address latent concerns at inference time. (2)State-Transition Policy Refinement (STPR)complements
this with evaluative policy-gradient signals: the final decision establishes trajectory-level advantage
while per-turn state transitions refine step-level credit direction—all derived from CUS without
external reward models or judges.
2

Extensive experiments validate both components. Human evaluation confirms that CUS produces
substantially more diverse and truthful dialogue topics and more grounded decisions than prior LLM
simulators. Built on CUS, our trained policy achieves higher task success on real-world outbound-call
benchmarks, and is remarkably more persuasive than RL baselines and current flagship LLMs,
evaluated by both powerful LLM-as-judge and human evaluators.
We make the following contributions:
• We propose Cognitive User Simulator (CUS), which models each user as a stratified persona with
hidden internal concerns P int and synchronous state dynamics, calibrated on 100K+ real-world
outbound-call logs, producing faithful and behaviorally diverse interactions.
• We introduce Simulator-Induced Asymmetric-View Policy Optimization, which converts the
modeled concerns and simulation state from CUS into complementary training objectives via
Asymmetric On-Policy Self-Distillation and State-Transition Policy Refinement, with no external
reward model, judge, or another teacher model.
• Extensive experiments on two real-world food-delivery proactive-TOD benchmarks (merchant
andcourieroutbound recruitment) demonstrate that our method matches or surpasses leading
flagship LLMs (e.g., Claude-Sonnet-4.5, GLM-5.1) and outperforms strong RL baselines, while
remaining robust across other LLM-based user simulators.
2 Related Work
Task-oriented dialogue (TOD) has evolved from sequence-to-sequence architectures [ 13, 14] to
LLM-driven paradigms that leverage in-context reasoning and instruction following [15, 16], with
reinforcement learning increasingly applied for policy optimization in multi-turn settings [7, 17, 18].
On the post-training side, alignment has progressed from RLHF/DPO [19, 20] through value-free
alternatives like GRPO [ 11, 12], multi-turn RL [ 21, 22], and distillation-based methods such as
OPD [23] and OPSD [24]. However, existing TOD methods lack proactive, multi-dimensional user
modeling, and current post-training recipes struggle to internalize latent user state for persuasive policy
learning. We address both gaps by coupling concern-grounded user simulation with asymmetric-view
policy optimization.
3 Methodology
Motivated by the finding that latent concerns are the critical missing variable for proactive TOD (§1),
we build a framework that models these concerns inside the simulator and converts them into training
signals as shown in Fig. 2: (1) TheCognitive User Simulator (CUS)(§3.2) represents each user
with observable external traits, hidden internal concerns, and concern-driven state dynamics, yielding
both a faithful training environment and two categories of natural byproduct: the privileged internal
persona P int and simulation feedback (final decision and per-turn state transitions). (2)Simulator-
Induced Asymmetric-View Policy Optimization (SI-A VPO)(§3.3) then converts these signals into
complementary training objectives:Asymmetric On-Policy Self-Distillation (AOPD)evaluates the
same policy under a privileged view that additionally conditions on P int and progressively distills
the resulting concern-aware behavior into the deployable, dialogue-only view;State-Transition
Policy Refinement (STPR)complements AOPD with policy-gradient credit, where the final decision
establishes trajectory-level advantage while per-turn state transitions refine step-level credit direction—
all derived from CUS without any external reward model or judge.
3.1 Problem Definition
We formalize proactive task-oriented dialogue as an episodic, undiscounted, turn-level Markov
Decision Process M={S,A, P, R}. Each episode samples a user profile P that parameterizes
the transition dynamics; the detailed design are described in §3.2. The profile governs all user-side
dialogue behavior and decisions but is never exposed to the agent.
States and actions.The state space S consists of variable-length dialogue histories. The initial
state s0 = [x 0] contains only the system instruction x0 (task description); the agent produces
the opening utterance y0 ∼π θ(· |s0) beforeany user response. At subsequent turns, the state
3

sk = [x0, y0, u1, y1, . . . , uk−1, yk−1, uk] concatenates the full history up to the user’s k-th utterance
uk, and the agent responds with yk ∼π θ(· |sk). The action space A=V ∗ comprises sequences
over the token vocabulary. Given sk and agent response yk, the user simulator generates uk+1
conditioned on P and the history, yielding sk+1 = [sk, yk, uk+1]; the resulting transition is denoted
PP (sk+1 |s k, yk).
Reward and objective.The episode runs for at most K turns and terminates with a binary user
decision d∈ {ACCEPT,REJECT} . A terminal reward r∈ {+1,−1}is assigned for acceptance and
rejection, respectively; the agent’s objective is to maximize the expected reward:
max
πθ
EP, πθ

r

.(1)
3.2 Cognitive User Simulator
To provide a faithful environment that produces behaviorally diverse and grounded interactions,
we propose a stratified user simulator framework that models the latent concerns that anchor user
decisions and couples state dynamics to concern progress.
Three-Layer Persona Framework.We instantiate CUS for proactive TOD tasks in collaboration
with the operations team of a major food-delivery platform; the persona schema and the concern
bank described below are co-designed with domain specialists, while a corpus of 100K+ outbound
call records provides a stylistic and behavioral prior that calibrates the simulator’s language, pacing,
and reaction patterns. Each user is represented as a stratified profile P=

P bg,P ext,P int
whose three layers play distinct functional roles. The (1)background P bg specifies the situational
frame at call onset (e.g., demographic attributes) and is naturally exposed through the call. The (2)
external persona P ext governs surface behavior along five observable axes (time pressure, courtesy,
communication style, cooperation tendency, technical familiarity) and shapes the texture of every
user utterance the agent receives.
The (3)internal persona P int encodes the user’s latent concerns across financial, psychological,
and operational facets. Each P int dimension is grounded by a curatedconcern bank: every concern
contains a natural-language resistance point, unlock conditions that specify when it can be resolved,
and anti-patterns that penalize harmful or over-promising agent behavior. P int directly governs
both the per-turn state dynamics and the terminal decision: willingness can only rise meaningfully
through concern resolution, and acceptance is gated by sufficient concern coverage—ensuring that
the simulator’s decisions reflect genuine concern progress rather than free-form LLM judgments.
Simulation State Transitions.Beyond the static persona, CUS maintains a scalarwillingness
state that tracks how close the user is to acceptance and is updated turn by turn. At each agent
turn k, the simulator emits a textual user response uk, a discrete action ak ∈ {CHAT,HANGUP}, a
signed willingness shift ∆wk, and per-concern state transitions ∆Ck that track each concern through
monotone states (UNRESOLVED → PARTIALLY-ADDRESSED → RESOLVED). Importantly, ∆wk is
not a free-form LLM score: it is rule-bounded by concern progression, so positive shifts require
actual concern resolution and anti-pattern hits induce penalties. The episode terminates with a binary
decisiond∈ {ACCEPT,REJECT}, gated by willingness and concern coverage.
Summary.This design yields one privileged state signal and two natural state-transition signals,
which are all available without any external annotation:
P int |{z}
privileged internal state
, d,{∆w k}K k=1| {z }
simulation state-transitions

.(2)
The internal state, which specifies the latent concerns invisible to the deployed agent, supports
asymmetric self-distillation; the final decision and per-turn willingness shifts provide trajectory- and
turn-level credit assignment. The next section composes these signals into the training objective.
3.3 Simulator-Induced Asymmetric-View Policy Optimization
To utilize the user’s invisible latent decision process induced by CUS and derive training signals, we
proposeSimulator-Induced Asymmetric-View Policy Optimization (SI-A VPO).
Overall Objective.SI-A VPO has two complementary components that convert the aforementioned
signals into training objectives, respectively. First,Asymmetric On-Policy Self-Distillation (AOPD)
4

ℒ!"!#$=ℒ%&’(+𝜆)!ℒ*+,’
(d) Asymmetric-View Policy Optimization
Optimized Deployable Policy
(c) CUS-Induced Training Signals(b) Example Dialogue Rollout
Agent
Our onboarding
includes dedicated
support and training.
Integration time
worriesme.
That helps, but
what about
hidden fees?
No hidden fees.
Transparent pricing
and clear ROI.
Sounds good
let's proceed.
Higher task
completion
Better credit
assignment
Dialogue Trajectory 𝒙
User
Proactive
actions
Faithful user simulation inherentlyproduceshierarchical supervision!
External Persona 𝑷𝒆𝒙𝒕(Observable)
Decision State Transition
Willingness Dynamics
(a) Cognitive User Simulator (CUS)
Communication StyleCooperationPolitenessTone
Internal Persona 𝑷𝒊𝒏𝒕
(Privileged / Hidden)
Decision FactorsCore Concerns Latent NeedsWillingness
Policy-Gradient Loss
from trajectory advantage
andturn-level credit
assignment
ℒ!"#$
Distillation Loss
from token-level
progressive KL
distillation
ℒ%&$’
Refusal -> Hesitation -> Acceptance
𝚫w!=−1,0,+1
We can reduce
costs by 20% and
integrate in a week
𝜋"
𝚫𝒘!
𝚫𝒘"
Internal
Profile
𝑷𝒊𝒏𝒕
State-Transition
Policy Refinement
HighLow
Asymmetric
On-policy Self-Distillation
distillation
Turn KTurn 1
Privileged
Self-Teacher
1
2
Student
Policy
Outcome Reward
𝑟&∈{−1,+1}
I
𝐴&’() * =𝒏𝒐𝒓𝒎(𝑟*)
II
Trajectory-level Advantage
𝐴*,, -.∝𝐴&’() * ⋅𝑧*,,⋅𝑚*,,
Turn-level Credit Assignment
III
1 2
𝐷’((𝜋)⋅𝑥*+,𝑃&,+)||𝜋)(⋅|𝑥*+))
(a) Cognitive User Simulator (CUS)
Insight
Induced Training Signals
Decision𝒅 ∈{Accept,Reject}
Simulator State Transitions
Shifts 𝚫𝒘=−1,0,+1
Figure 2: Overview of our framework.
transfers concern-aware behavior from a privileged view of the same policy into its deployable
dialogue-only view. Second,State-Transition Policy Refinement (STPR)uses the simulator’s final
decision and synchronous state (i.e., willingness) transitions to refine on-policy credit assignment:
LSI-A VPO=L AOPD(P int) +λ st LSTPR(d,{∆w k}K k=1).(3)
Asymmetric On-Policy Self-Distillation.AOPD aims to turn the internal persona exposed by CUS
at training time into token-level supervision for a dialogue-only policy. We define two information
views of the same policy πθ: aprivileged teacherview whose context is augmented with the user’s
internal persona P int i , and adeployable studentview that observes only the task instruction and
dialogue history. For each student-generated token in an on-policy rollout, we compute the probability
distributions under both views and minimize their divergence, thereby distilling concern-aware
behavior from the teacher into the student:
LAOPD = 1 N X i,t ϕ(k(t), K)DKL  sg  πθ  · |xi,t,P int i   πθ(· |xi,t)  .(4)
Here, N is the number of assistant tokens, K is the maximum turns, k(t) maps token t to its dialogue
turn, and ϕ(k(t), K)is a nonnegative turn-dependent distillation weight. The stop-gradient operator
sg[·] freezes the teacher distribution as a fixed target, so gradients flow only through the student view.
Because both views share the same πθ, no separate teacher model is needed; at inference time the
policy operates under the student view alone, without any dependence onP int.
State-Transition Policy Refinement.While AOPD provides directive supervision that teaches the
studentwhata concern-aware agent would say, it leaves the question ofwhethera particular attempt
actually steers the user’s acceptance, e.g., a turn may probe the right concern at the wrong moment
that triggers user resistance. Furthermore, since P int is unavailable at inference, perfect imitation of
the privileged teacher is inherently unattainable; the student must explore and refine its own dialogue
strategies under the constrained information view, yet distillation alone offers no evaluative signal to
guide this exploration.
Therefore, we propose STPR to address both limitations by introducing evaluative credit grounded
in the simulator’s state dynamics. STPR uses CUS state transition dynamics to assign trajectory
credit. Formally, the final decision defines a normalized trajectory advantage A(i) traj = ri−µr σr+εnorm , setting the trajectory-level update direction and scale. Here, ri is the terminal reward for rollout i,
µr and σr are the mean and standard deviation of rewards within the rollout group, and εnorm is a
small positive constant for numerical stability. The per-turn willingness shift ∆wi,k then adjusts this
signal: a transition that directionally aligns with the final outcome reinforces the trajectory direction,
a contradictory transition flips it, and a zero transition leaves the trajectory credit unchanged. Let
∆wmax denote the maximum absolute willingness shift over all turns in the rollout group. For
turns with a nonzero willingness shift, let mi,k =|∆w i,k|/∆wmax denote the magnitude gate and
zi,k = sgn(A(i) traj∆wi,k)denote the alignment sign. The state-transition advantage is:
Ast i,k =A (i) trajzi,kmi,k exp(τ zi,k),∆w i,k ̸= 0.(5)
5

The magnitude gate mi,k measures how much the simulator state changes at turn k, and the tempera-
ture τ controls the strength of outcome–transition polarization: larger values amplify turns whose
willingness shift aligns with the final outcome and more strongly suppress contradictory turns. The
alignment sign zi,k determines the credit direction: it is positive when the local willingness shift
agrees with the terminal trajectory advantage and negative when it contradicts it. The exponential
factor then further amplifies aligned transitions and suppresses contradictory ones. If ∆wi,k = 0,
we directly set Ast i,k =A (i) traj, so turns without simulator state change keep the original trajectory
credit. STPR therefore anchors credit to the trajectory-level advantage while assigning aligned turns
same-signed credit and contradictory turns opposite-signed credit according to the simulator’s state
dynamics. BroadcastingA st i,k to all assistant tokens in turnkgives the clipped refinement loss
LSTPR =− 1 N X i,t min  ρi,t Ast i,k(t),clip(ρ i,t,1−ε clip,1+ε clip)A st i,k(t)  ,(6)
whereρ i,t =π θ(yi,t |x i,t)/πθold (yi,t |x i,t). Algorithm 1 summarizes the complete training loop.
4 Experimental Setup
Baselines.We compare SI-A VPO against two categories of baselines.(1) Large Models.We
select five state-of-the-art proprietary LLMs—GPT-4.1 [25], DeepSeek-V3.2 [26], GLM-5.1 [27],
Kimi-K2.5 [28], and Claude-Sonnet-4.5 [29]—with the same task instructions to establish upper-
bound references.(2) RL-based Methods.Starting from two foundation models, Qwen3-4B and
Qwen3-8B [30], we apply several representative reinforcement learning algorithms: GRPO [ 12],
PPO [31], DAPO [11], and SEAD [5]. All RL baselines are trained with the same user simulator and
environment configuration for a fair comparison.
Datasets.We instantiate SI-A VPO on two real-world proactive outbound-call tasks from our business:
Merchant Promotion(recruiting new merchants into a paid traffic campaign) andCourier Regional
Bonus(enrolling couriers into a region-specific rush-hour bonus program). For each task we sample
10,000 personas for training and a disjoint set of200 personas for evaluation, so test-time performance
reflects generalization to unseen profile combinations rather than memorization. During persona
construction, each user’s specific internal concerns are sampled uniformly at random from the task-
specific concern bank, with the number of concerns drawn from Uniform{3,6} , yielding diverse
difficulty levels across episodes. The shared external profile covers five observable dimensions, while
the task-specific internal profile contains 14 dimensions/42 values/89 curated concerns for merchants
and 12 dimensions/36 values/78 curated concerns for couriers; all concerns are audited to remain
within the agent’s authorized scope.
Evaluation Metrics.We measure two objective signals from the simulator’s internal state transitions:
theAcceptance Rate (AR), the percentage of dialogues ending in user acceptance, and theConcern
Solving Rate (CSR), the proportion of the user’s hidden concerns successfully addressed during the
interaction. To assess interaction quality beyond task completion, we employ three strong third-party
LLMs (Gemini-3.1-Pro [ 32], GPT-5.4 [ 33], and Claude-Opus-4.6 [ 34]) as judges to score each
dialogue on a 1–5 scale along three dimensions:Communication,Logic, andProactivity. We
average the independent judge scores for each dialogue and report means across repeated evaluation
runs.
Implementation Details.All experiments are implemented using veRL [ 35]. For RL training,
we use 8× NVIDIA A100 (80GB) GPUs with batch size 128, learning rate 1×10 −6, three inner
optimization epochs, eight rollouts per prompt, and a maximum dialogue length of 20 interaction
turns. The user simulator is served on 16× NVIDIA H20 GPUs to support high-throughput parallel
rollout generation with bfloat16 SGLang inference. We use Qwen3.5-115B [36] as the default user
simulator during training and Claude-Sonnet-4.5 for evaluation. For evaluation, each experiment
is repeatedthree times. For LLM-as-judge metrics, each dialogue is scored by the three judges
introduced above independently, and we report the average scores.
6

Algorithm 1: Simulator-Induced Asymmetric-View Policy Optimization(SI-AVPO).
Input :policyπ θ; CUS persona samplerP; group sizeG; max turnsK; inner epochsE
Hyper :ε clip, εnorm, ϕ(k, K), τ, λst
Output :deployable policyπ θ
1 foreach training iterationdo
2θ old ←θ
// Phase 1: collect CUS rollouts under the deployable view
3SampleP i ∼ P
4 fori= 1toGdo
5Run aK-turn dialogue withπ θold (· |x)
6Record{(x i,t, yi,t, k(t))}, hidden profilePint i , shifts{∆w i,k}K k=1, and rewardr i
7 end
// Phase 2: compute simulator-grounded STPR credit
8A (i) traj ←(r i −µ r)/(σr +ε norm)∀i,∆w max ←max j∈[G], ℓ∈[K]|∆wj,ℓ|
9 foreachturn(i, k)do
10z i,k ←sgn(A (i) traj ∆wi,k),m i,k ← |∆wi,k|/∆wmax
11A st i,k ←
(
A(i) traj ,∆w i,k = 0,
A(i) traj zi,kmi,k exp(τ zi,k),∆w i,k ̸= 0;
12BroadcastA st i,k to all assistant tokens in turnk
13 end
// Phases 3–4: privileged AOPD loss and joint update
14 fore= 1toEand each minibatchBdo
15 foreach(i, t)∈ Bdo
16q priv i,t ←sg  πθ(· |xi,t,P int i )  ,p i,t ←π θ(· |xi,t),ρ i,t ← πθ(yi,t |x i,t) πθold (yi,t |x i,t)
17 end
18L B AOPD ← 1 |B| X (i,t)∈B ϕ(k(t), K)DKL  qpriv i,t pi,t 
19L B STPR ← −1 |B| X (i,t)∈B min  ρi,tAst i,k(t),clip(ρ i,t,1−ε clip,1 +ε clip)Ast i,k(t) 
20θ←θ− ∇ θ

LB AOPD +λ stLB STPR

21 end
22 end
23 returnπ θ
5 Experiment Results
5.1 Main Results
We first evaluate SI-A VPO against two groups of baselines: representative RL algorithms built on
the same Qwen backbones and flagship proprietary LLMs prompted with the same task instructions.
Table 1 summarizes both task success and dialogue-quality metrics on the merchant and courier
outbound-call scenes.
Among the RL baselines, general-purpose algorithms (GRPO, DAPO, PPO) yield modest improve-
ments over the base model in task scores and dialogue quality, yet their gains on the proactivity
remain limited. For example, on Qwen3-8B, DAPO raises Proact. from 2.18 to only 2.41 on the
merchant scene. This pattern suggests that outcome-driven RL can refine surface-level communica-
tion skills and help the agent better address user concerns once they are raised, but it struggles to
induce genuinely proactive behaviors such as anticipating latent objections or steering the conversa-
tion toward unspoken needs. SEAD advances further through its curriculum-based self-evolution,
achieving stronger performance. Nevertheless, SI-A VPO consistently and substantially outperforms
all RL baselines across both scenes and both backbone sizes. On Qwen3-8B, SI-A VPO significantly
surpasses the best RL baseline (SEAD) by +12.2% CSR, +12.2% Acc, and +0.55 Proact. on the
merchant scene, and by +8.9% CSR, +10.8% Acc, and +0.49 Proact. on the courier scene (with
p-value less than 10−5). The improvement in proactivity indicates that our SI-A VPO provides direct
supervision for initiative-taking behaviors that conventional RL rarely discovers on its own: actively
probing hidden concerns, adapting to user hesitation, and steering conversations toward decisions
rather than passively responding.
7

Table 1: Model performance onFoodDeliverService. CSR and Acc are percentages; Comm., Logic,
and Proact. are 1–5 judge scores.Bold: best overall; underline : second best overall.
Method
Merchant Promotion Courier Regional Bonus
Task Dialogue Task Dialogue
CSR↑Acc↑Comm.↑Logic↑Proact.↑CSR↑Acc↑Comm.↑Logic↑Proact.↑
Large Models
GPT-4.1 36.1 34.7 2.93 3.02 2.12 30.7 22.8 2.66 2.91 1.79
DeepSeek-v3.2 45.7 39.5 3.04 3.13 2.45 32.6 28.0 2.54 3.27 1.96
GLM-5.1 46.2 42.3 3.32 3.44 2.78 38.7 38.7 2.86 3.56 2.12
Kimi-K2.5 49.0 39.8 3.26 3.51 2.67 39.0 38.8 2.79 3.45 2.21
Claude-Sonnet-4.5 51.150.83.56 3.763.09 45.0 43.2 3.03 3.752.67
Qwen-3-4B
Base 22.5 20.2 2.23 2.15 1.90 20.8 18.5 1.96 2.34 1.76
+GRPO 28.4 28.0 2.47 2.61 2.17 24.3 22.3 2.13 2.55 1.86
+PPO 26.5 22.3 2.36 2.59 2.22 22.7 19.8 2.06 2.44 1.75
+DAPO 29.7 29.5 2.60 2.74 2.33 23.8 26.3 2.25 2.81 2.10
+SEAD 33.7 32.7 2.95 3.22 2.58 30.2 32.5 2.52 3.21 2.26
+SI-A VPO 51.9 46.3 3.25 3.56 3.11 44.6 42.0 2.87 3.52 2.63
Qwen-3-8B
Base 30.6 26.2 2.66 2.48 2.18 23.5 22.2 2.35 2.51 2.00
+GRPO 33.2 30.5 2.69 2.88 2.51 29.6 24.7 2.41 3.03 2.11
+PPO 31.8 26.8 2.60 2.81 2.26 25.2 24.8 2.40 2.87 2.13
+DAPO 36.3 34.3 2.81 3.37 2.41 30.7 28.7 2.59 3.19 2.28
+SEAD 40.4 36.3 3.23 3.56 2.63 36.7 33.5 2.75 3.51 2.45
+SI-A VPO 52.6 48.5 3.61 3.71 3.18 45.6 44.3 3.06 3.66 2.94
Notably, SI-A VPO outperforms four of the five flagship LLMs, including GPT-4.1, DeepSeek-v3.2,
GLM-5.1, and Kimi-K2.5, on most metrics across both scenes, even with the smaller Qwen3-4B
backbone. With Qwen3-8B, SI-A VPO further rivals the strongest flagship and proprietary model,
Claude-Sonnet-4.5, surpassing it on CSR (52.6% vs. 51.1%), Proact. (3.18 vs. 3.09) on the merchant
scene, and on both CSR and Acc on the courier scene, while trailing only marginally on Acc and
Logic for merchants. Since flagship models of this scale are impractical for real-time outbound calling
due to latency, cost, and data-governance constraints, the key takeaway is that a deployable-size
policy trained with SI-A VPO can match or exceed much larger general-purpose models in proactive
task-oriented dialogue.
5.2 Ablation Study
Table 2 presents the ablation results, from which we draw the following observations.
AOPD is essential for effective exploration.Removing AOPD while retaining STPR (“w/o
AOPD”) causes CSR to drop by 16.5% and Acc by 11.8%. Crucially, the steepest single-metric
decline is on Proact. ( −0.76). This decrease confirms that AOPD provides adirectionaltraining
signal: by distilling the privileged teacher’s targeted strategies into the student, it specifically guides
the policy toward initiative-taking behaviors rather than merely improving surface fluency. Further
Table 2: Ablation onMerchant(Qwen3-4B).
Variant CSR(%)Acc(%)Comm. Logic Proact.
SI-A VPO (Full) 51.9 46.3 3.25 3.56 3.11
Removing AOPD components
w/o AOPD (→STPR) 35.4↓16.534.5↓11.82.81 3.01 2.35
w/o AOPD + Turn (→GRPO) 28.4↓23.528.0↓18.32.47 2.61 2.17
Removing STPR components
w/o Turn-Level Reward 46.7↓5.242.2↓4.13.01 3.21 3.14
w/o STPR (→AOPD) 44.6↓7.338.7↓7.62.85 2.983.23
w/o STPR + Asym (→OPD) 37.6↓14.332.8↓13.52.66 3.01 2.39
8

stripping the turn-level reward (“w/o AOPD + Turn-Level”, equivalent to vanilla GRPO) yields
an additional 7.0% CSR and 6.5% Acc decline, indicating that sparse outcome rewards alone are
insufficient to discover effective proactive strategies.
STPR grounds AOPD’s proactive drive in context.Removing the turn-level reward (“w/o Turn-
Level Reward”) lowers CSR by 5.2% and Acc by 4.1%, with noticeable drops in Comm. (−0.24)
and Logic (−0.35). Further removing the entire STPR component (“w/o STPR”, i.e. AOPD only)
widens the gap to −7.3% CSR and −7.6% Acc, while Comm. and Logic continue to deteriorate
(−0.40 and −0.58, respectively). Interestingly, the Proact. scoreincreasesin both variants ( 3.14
and 3.23 vs. 3.11 in the full model), revealing that AOPD alone drives the policy toward anoverly
aggressivepersuasion style: it eagerly pushes proposals and steers toward acceptance, but neglects the
user’s intermediate reactions and conversational context. STPR corrects this tendency by supplying
fine-grained, per-turn evaluative feedback that grounds each proactive move in the dialogue state,
encouraging the agent to balance initiative with attentive, context-aware responses.
The role of information asymmetry.To isolate whether the gain of AOPD stems fromprivileged
informationor merely from the distillation mechanism itself, we replace AOPD with a vanilla OPD
variant (“OPD only”): the teacher is upgraded to a stronger Qwen3-32B model but observes only the
same dialogue history as the student, without access to the hidden internal persona P int. Despite its
substantially larger capacity, OPD yields 7.0% lower CSR and 5.9% lower Acc than AOPD, with
Proact. dropping sharply from 3.23 to 2.39 (−0.84). This confirms that the critical ingredient is not
teacher capacity butinformation asymmetry—access to the user’s latent concerns enables the teacher
to demonstrate targeted, concern-aware strategies that a stronger but equally uninformed teacher
cannot discover from dialogue alone.
5.3 Generalization on Different User Simulator
Figure 3 evaluates the transferability of the learned dialogue policy to user simulators unseen during
training. An important observation is that different LLMs, even when instantiated with identical
persona profiles and instructions, exhibit markedly different levels of strictness in role-playing the
user. For instance, DeepSeek-V3.2 proves to be an exceptionally strict simulator—both Qwen3-4B
and Qwen3-8B achieve near-zero Acceptance Rate against it in the base setting. This variance reflects
genuine differences in how each LLM interprets and enacts the user persona rather than differences
in task difficulty, as all simulators share the same scenario configuration. To contextualize these
behavioral differences, we also assess simulator fidelity in Section 5.4, combining topic-diversity
analysis with human rationality judgments to measure whether simulator decisions remain grounded
in the prescribed persona and dialogue history.
Despite this substantial variation in simulator strictness, SI-A VPO yields consistent improvements
acrosseverytested simulator. On average, SI-A VPO improves CSR by 14.8% and Acc by 15.5% on
Qwen3-4B, and by 13.2% and 13.8% on Qwen3-8B, with gains observed on all six simulators without
exception. This uniformity across diverse model families, parameter scales, and conversational styles
confirms that SI-A VPO acquires generalizable proactive dialogue competencies rather than overfitting
to the idiosyncrasies of a single training-time simulator.
5.4 User Simulator Fidelity
To verify that CUS provides a more faithful training environment than prior external-persona-only
simulators [5], we sample 500 dialogues per simulator and evaluate two aspects: behavioral diversity
(# Unique Topics, Top-3 Topic Share) and Decision Rationality—whether annotators can articulate a
Claude
Sonnet-4.5
DeepSeek
V3.2
Claude
Haiku-4.5
GPT-4.1 GPT-5.4
Mini
GPT-4o
0
20
40
60Concern Solving Rate (CSR, %)
+29 +22
+8
+11
+13 +10
+10
+10
+18 +13
+9
+13
Claude
Sonnet-4.5
DeepSeek
V3.2
Claude
Haiku-4.5
GPT-4.1 GPT-5.4
Mini
GPT-4o
0
20
40Acceptance Rate (Acc, %)
+26 +22
+8 +10
+20 +14
+6
+6
+22
+17
+10
+12
Qwen3-4B Qwen3-4B + SI-A VPO Qwen3-8B Qwen3-8B + SI-A VPO
Figure 3: Generalization across different user simulators onMerchantscene.
9

grounded reason for the terminal acceptance/rejection decision from the dialogue context. As Table 3
shows, CUS expands topic coverage from 8 to 72, reduces Top-3 topic concentration from 56.2% to
14.4%, and raises Decision Rationality from 71.4% to 94.8% (κ= 0.76 ). The external-only baseline
frequently terminates after content-empty turns (e.g., “I clicked / I received it”) with unmotivated
decisions, whereas CUS exposes concrete concerns and willingness shifts that make each decision
traceable. These results confirm that the performance gains of SI-A VPO are grounded in optimization
against a substantially more faithful user model.
Table 3: User simulator fidelity on 500Merchantdialogues per simulator. Topic clusters use Qwen3-
embedding with annotator verification; Decision Rationality is the majority vote of three blind
domain-expert annotators.
Simulator # Unique Topics↑Top-3 Topic Share↓Decision Rationality↑
External-only [5] 8 56.2% 71.4%
CUS (Ours) 72 14.4% 94.8%
6 Conclusion
We identified the user’s latent concerns as the critical missing variable for proactive task-oriented
dialogue and built a framework that models and exploits them. The Cognitive User Simulator
represents each user with hidden internal concerns and synchronous state dynamics, yielding behav-
iorally diverse interactions whose decisions are grounded in concern progress. Simulator-Induced
Asymmetric-View Policy Optimization converts the resulting privileged state and per-turn transitions
into complementary training objectives: asymmetric self-distillation transfers concern-aware behavior
into the deployable policy, while state-transition refinement provides fine-grained credit assignment,
all without external reward models or judges. On two real-world food-delivery outbound-call bench-
marks, our method matches or surpasses flagship proprietary LLMs and consistently outperforms
strong RL baselines, with gains that generalize across diverse unseen user simulators.
References
[1] Shunyu Yao, Noah Shinn, Pedram Razavi, and Karthik Narasimhan. τ -bench: A benchmark for
tool-agent-user interaction in real-world domains.arXiv preprint arXiv:2406.12045, 2024.
[2] Victor Barres, Honghua Dong, Soham Ray, Xujie Si, and Karthik Narasimhan. Tau2-
bench: Evaluating conversational agents in a dual-control environment.arXiv preprint
arXiv:2506.07982, 2025.
[3] Paweł Budzianowski, Tsung-Hsien Wen, Bo-Hsiang Tseng, Iñigo Casanueva, Stefan Ultes,
Osman Ramadan, and Milica Gaši´c. Multiwoz–a large-scale multi-domain wizard-of-oz dataset
for task-oriented dialogue modelling.arXiv preprint arXiv:1810.00278, 2018.
[4] Tom Bocklisch, Thomas Werkmeister, Daksh Varshneya, and Alan Nichol. Task-oriented
dialogue with in-context learning.arXiv preprint arXiv:2402.12234, 2024.
[5] Yuqin Dai, Ning Gao, Wei Zhang, Jie Wang, Zichen Luo, Jinpeng Wang, Yujie Wang, Ruiyuan
Wu, and Chaozheng Wang. Sead: Self-evolving agent for multi-turn service dialogue.arXiv
preprint arXiv:2602.03548, 2026.
[6] Feng Zhang, Shijia Li, Chunmao Zhang, Zhanyu Ma, Jun Xu, Jiuchong Gao, Jinghua Hao,
Renqing He, Jingwen Xu, and Han Liu. Userlm-r1: Modeling human reasoning in user language
models with multi-reward reinforcement learning.arXiv preprint arXiv:2601.09215, 2026.
[7] Ning Gao, Wei Zhang, Yuqin Dai, Ling Shi, Ziyin Wang, Yujie Wang, Wei He, Jinpeng Wang,
and Chaozheng Wang. Reinforcing real-world service agents: Balancing utility and cost in
task-oriented dialogue.arXiv preprint arXiv:2602.22697, 2026.
[8] Chunting Zhou, Pengfei Liu, Puxin Xu, Srinivasan Iyer, Jiao Sun, Yuning Mao, Xuezhe Ma,
Avia Efrat, Ping Yu, Lili Yu, Susan Zhang, Gargi Ghosh, Mike Lewis, Luke Zettlemoyer, and
Omer Levy. LIMA: Less is more for alignment. InAdvances in Neural Information Processing
Systems 36 (NeurIPS), 2023.
10

[9] Arnav Gudibande, Eric Wallace, Charlie Snell, Xinyang Geng, Hao Liu, Pieter Abbeel, Sergey
Levine, and Dawn Song. The false promise of imitating proprietary language models. InThe
Twelfth International Conference on Learning Representations (ICLR), 2024.
[10] Tianzhe Chu, Yuexiang Zhai, Jihan Yang, Shengbang Tong, Saining Xie, Dale Schuurmans,
Quoc V . Le, Sergey Levine, and Yi Ma. SFT memorizes, RL generalizes: A comparative study
of foundation model post-training. InProceedings of the 42nd International Conference on
Machine Learning (ICML), volume 267 ofProceedings of Machine Learning Research, pages
10818–10838. PMLR, 2025.
[11] Qiying Yu, Zheng Zhang, Ruofei Zhu, Yufeng Yuan, Xiaochen Zuo, Yu Yue, Weinan Dai,
Tiantian Fan, Gaohong Liu, Lingjun Liu, et al. Dapo: An open-source llm reinforcement
learning system at scale.arXiv preprint arXiv:2503.14476, 2025.
[12] Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang,
Mingchuan Zhang, YK Li, Yang Wu, et al. Deepseekmath: Pushing the limits of mathematical
reasoning in open language models.arXiv preprint arXiv:2402.03300, 2024.
[13] Oriol Vinyals and Quoc Le. A neural conversational model.arXiv preprint arXiv:1506.05869,
2015.
[14] Tsung-Hsien Wen, Milica Gasic, Nikola Mrkši´c, Pei-Hao Su, David Vandyke, and Steve Young.
Semantically conditioned lstm-based natural language generation for spoken dialogue systems.
InProceedings of the 2015 conference on empirical methods in natural language processing,
pages 1711–1721, 2015.
[15] Lei Wang, Chen Ma, Xueyang Feng, Zeyu Zhang, Hao Yang, Jingsen Zhang, Zhiyuan Chen,
Jiakai Tang, Xu Chen, Yankai Lin, et al. A survey on large language model based autonomous
agents.Frontiers of Computer Science, 18(6):186345, 2024.
[16] Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and Yuan
Cao. React: Synergizing reasoning and acting in language models. InInternational Conference
on Learning Representations (ICLR), 2023.
[17] Xiao Yu, Qingyang Wu, Kun Qian, and Zhou Yu. Krls: Improving end-to-end response
generation in task oriented dialog with reinforced keywords learning. InProceedings of the
2023 Conference on Empirical Methods in Natural Language Processing, pages 12338–12358,
2023.
[18] Yanming Wan, Jiaxing Wu, Marwa Abdulhai, Lior Shani, and Natasha Jaques. Enhancing
personalized multi-turn dialogue with curiosity reward.arXiv preprint arXiv:2504.03206, 2025.
[19] Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll Wainwright, Pamela Mishkin,
Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, et al. Training language models to
follow instructions with human feedback.Advances in neural information processing systems,
35:27730–27744, 2022.
[20] Rafael Rafailov, Archit Sharma, Eric Mitchell, Christopher D Manning, Stefano Ermon, and
Chelsea Finn. Direct preference optimization: Your language model is secretly a reward model.
Advances in neural information processing systems, 36:53728–53741, 2023.
[21] Yifei Zhou, Andrea Zanette, Jiayi Pan, Sergey Levine, and Aviral Kumar. Archer: Training
language model agents via hierarchical multi-turn rl.arXiv preprint arXiv:2402.19446, 2024.
[22] Yifei Zhou, Song Jiang, Yuandong Tian, Jason Weston, Sergey Levine, Sainbayar Sukhbaatar,
and Xian Li. Sweet-rl: Training multi-turn llm agents on collaborative reasoning tasks.arXiv
preprint arXiv:2503.15478, 2025.
[23] Rishabh Agarwal, Nino Vieillard, Yongchao Zhou, Piotr Stanczyk, Sabela Ramos Garea,
Matthieu Geist, and Olivier Bachem. On-policy distillation of language models: Learning from
self-generated mistakes. InThe twelfth international conference on learning representations,
2024.
11

[24] Siyan Zhao, Zhihui Xie, Mengchen Liu, Jing Huang, Guan Pang, Feiyu Chen, and Aditya
Grover. Self-distilled reasoner: On-policy self-distillation for large language models.arXiv
preprint arXiv:2601.18734, 2026.
[25] OpenAI. Introducing GPT-4.1 in the API.https://openai.com/index/gpt-4-1/, 2025.
[26] Aixin Liu, Aoxue Mei, Bangcai Lin, Bing Xue, Bingxuan Wang, Bingzheng Xu, Bochao Wu,
Bowei Zhang, Chaofan Lin, Chen Dong, et al. Deepseek-v3. 2: Pushing the frontier of open
large language models.arXiv preprint arXiv:2512.02556, 2025.
[27] Z.AI. GLM-5.1.https://huggingface.co/zai-org/GLM-5.1, 2026.
[28] Kimi Team, Tongtong Bai, Yifan Bai, Yiping Bao, SH Cai, Yuan Cao, Y Charles, HS Che,
Cheng Chen, Guanduo Chen, et al. Kimi k2. 5: Visual agentic intelligence.arXiv preprint
arXiv:2602.02276, 2026.
[29] Anthropic. Introducing Claude Sonnet 4.5. https://www.anthropic.com/news/claud
e-sonnet-4-5, 2025.
[30] An Yang, Anfeng Li, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu,
Chang Gao, Chengen Huang, Chenxu Lv, et al. Qwen3 technical report.arXiv preprint
arXiv:2505.09388, 2025.
[31] John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal
policy optimization algorithms.arXiv preprint arXiv:1707.06347, 2017.
[32] DeepMind. Best for complex tasks and bringing creative concepts to life. https://deepmind
.google/models/gemini/pro/, 2025.
[33] OpenAI. Introducing GPT-5.4. https://openai.com/index/introducing-gpt-5-4/ ,
2026.
[34] Anthropic. Introducing Claude Opus 4.6. https://www.anthropic.com/news/claude-o
pus-4-6, 2026.
[35] Guangming Sheng, Chi Zhang, Zilingfeng Ye, Xibin Wu, Wang Zhang, Ru Zhang, Yanghua
Peng, Haibin Lin, and Chuan Wu. Hybridflow: A flexible and efficient rlhf framework.arXiv
preprint arXiv: 2409.19256, 2024.
[36] Qwen. Qwen3.5.https://qwen.ai/blog?id=qwen3.5, 2026.
12
