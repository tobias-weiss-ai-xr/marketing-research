---
title: Productive State-Space Exploration for Multi-turn RL in LLM Agents
url: https://arxiv.org/abs/2610.25957
category: ai-marketing
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Mohammed Haroon Dupty
- Yong Liang Goh
- Song Guo
- Wee Sun Lee
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.25957
pages: 20
chars: 70278
fetched_at: '2026-11-08T13:34:27+00:00'
kb_version: 1
---

# Productive State-Space Exploration for Multi-turn RL in LLM Agents

Productive State-Space Exploration for Multi-turn RL in LLM Agents
Mohammed Haroon Dupty †
Institute of Advanced Computing
and Intelligence, A*STAR
haroon@u.nus.edu
Y ong Liang Goh
Grabtaxi Holdings Pte Ltd
gyl@u.nus.edu
Song Guo
The Hong Kong University of
Science and Technology
songguo@cse.ust.hk
Wee Sun Lee
School of Computing,
National University of Singapore
leews@comp.nus.edu.sg
Abstract
Reinforcement Learning (RL) for Large Lan-
guage Model (LLM) agents in multi-turn, long-
horizon environments remains challenging due
to inefficient action selection and repetitive be-
havioral patterns. In particular, agents often
become trapped in high-confidence yet unpro-
ductive behaviors, repeatedly executing invalid
actions or entering action loops that hinder task
completion. We observe that these frequently
violate environment preconditions, revealing a
mismatch between the agent’s representation
of the internal state and the dynamics of the
underlying environment. In addition, repetitive
high-confidence actions lead to cyclical behav-
iors that provide little to no progress towards
the goal. We argue that addressing these chal-
lenges requires moreproductive task-aligned
explorationto improve the agent’s understand-
ing of environment dynamics. Motivated by in-
trinsic curiosity-driven exploration, we propose
aconditional state-space explorationframe-
work that balances task completion with in-
trinsic information-seeking behavior. Specif-
ically, we introduce an intrinsic reward that
penalizes actions whose observation duplicates
prior state memory. This provides the benefit
of reducing redundant behaviors and encourag-
ing state-space coverage without relying on a
general information-theoretic measure. Strong
experimental results demonstrate that our ap-
proach substantially improves policy learning
in multi-turn environments, mitigating invalid
actions and repetitive loops.
1 Introduction
Reinforcement learning (RL) has become an im-
portant training paradigm for large language model
(LLM) agents that must operate over multiple
turns in partially observable, long-horizon environ-
ments (Carta et al., 2023; Shani et al., 2024; Guan
et al., 2026). In contrast to single-step prediction
†Major part of this work was done while at the National
University of Singapore.
tasks, these agents must select actions sequentially,
update internal memory, and adapt to changing
states while receiving sparse and delayed feedback.
Recent work has shown that RL is increasingly rel-
evant for improving reasoning, agentic control, and
long-horizon decision making in LLMs, but it has
also revealed a persistent difficulty: agents often
become stuck in repetitive, high-confidence behav-
iors that are locally plausible yet unproductive for
the task (Liu et al., 2025; Zhang et al., 2025; Xi
et al., 2025).
In such settings, effective learning depends not
only on exploiting promising actions but also on
exploring the environment in a way that improves
the agent’s understanding of its dynamics. In prac-
tice, agents often overcommit to high-confidence
actions that are locally plausible but globally un-
helpful, leading to invalid interactions or repetitive
loops that consume budget without advancing the
task. Such failures, as shown in Figure 1, typically
reflect a mismatch between the agent’s internal
state representation and the true environment dy-
namics, especially when the agent lacks sufficient
feedback about which actions are feasible or in-
formative. This motivates the need for a form of
productive state-space explorationthat helps the
agent learn environment dynamics while remaining
aligned with task completion.
A natural way to improve exploration is to en-
courage the agent to visit a broader range of states.
In principle, increasing the entropy of the explored
state space can improve coverage, reduce mode
collapse, and expose the agent to more informa-
tive trajectories. However, directly maximizing
exploration entropy can also be problematic. If en-
couraged too strongly, the agent may drift toward
diverse but task-irrelevant behavior, thereby sac-
rificing progress on the underlying objective. In
long-horizon environments, this tension between
exploration and exploitation is especially important:
exploration should broaden the agent’s experience,
1
arXiv:2610.25957v1  [cs.AI]  19 Oct 2026

Figure 1: Failure modes of an RL-trained LLM agent in ALFWorld. (a)Repetitive action loop.The agent repeats an
invalid action and receives the same failure feedback until the step budget runs out. (b)Repetitive reasoning loop.
The agent’s reasoning ignores the current observation, and the agent cycles between the fridge and the microwave
without completing the task. In both cases the agent’s internal state diverges from the environment dynamics, and
the looping steps consume interaction budget while revealing no new observation. These are the steps our intrinsic
reward penalizes.
but it should not pull the policy away from useful
action sequences that lead to task completion.
This paper pursues productive exploration
throughintrinsic curiosity-driven rewards, with a
conservative formulation that preserves task align-
ment. Rather than positively rewarding state-space
entropy increase, we penalize any step whose ob-
servation has already appeared in the episode. The
intuition is that unhelpful actions, such as invalid
steps or redundant repetitions, consume interaction
budget and policy probability without revealing
anything new about the environment. They can be
detected simply by checking whether each new ob-
servation adds any new information to the agent’s
memory.
Our formulation reframes entropy increase as
a consequence of avoiding unproductive actions
rather than as an objective to be optimized di-
rectly. The penalty improves within-episode state-
space coverage, while the task reward keeps explo-
ration tied to task completion. We further formal-
ize this argument by showing that the cumulative
penalty measures how many distinct observations
an episode visits, and that it bounds the episode’s
visitation entropy (Section 3). A single-step anal-
ysis further shows that novel observations always
increase entropy, while revisits of frequent obser-
vations decrease it.
Our approach is consistent with the broader lit-
erature on intrinsic motivation in reinforcement
learning, where curiosity, novelty seeking, and
uncertainty reduction have been used to improve
learning under sparse rewards (Chentanez et al.,
2004; Aubret et al., 2019; Gao et al., 2025). It
also aligns with recent efforts to train long-horizon
LLM agents, where robustness depends not only on
reasoning ability but also on the capacity to avoid
repetitive or uninformative interactions with the
environment (Kalyan and Andrews, 2025). Within
this setting, penalizing unhelpful actions provides
a simple compromise between unrestricted entropy
maximization and overly conservative exploitation.
The resulting behavior promotes broader state cov-
erage without losing contact with the task.
In summary, we propose aconditional intrinsic
rewardframework that supportsproductive explo-
rationby penalizing actions that yield no new in-
formative observation. Our key argument is that
entropy expansion is useful, but only when it is
induced indirectly through the suppression of re-
dundant or uninformative behavior. This allows the
agent to explore more broadly while maintaining a
strong coupling to task progress. We evaluate our
proposed exploration strategy on two prominent
multi-turn benchmark environments: ALFWorld
and WebShop. Empirical results show that our ap-
2

proach surpasses recent baselines in performance
metrics of success rates and significantly mitigates
both invalid and repetitive action rates.
2 Related Work
2.1 Prompting-Based LLM Agents
Early LLM agent frameworks rely on prompting for
multi-step reasoning and action selection without
updating model weights. ReAct (Yao et al., 2023)
interleaves reasoning (Thought) and actions (Act),
outperforming pure reasoning or action prompting
on tasks such as ALFWorld and WebShop. Reflex-
ion (Shinn et al., 2023) extends this with verbal
reinforcement, storing self-reflections from failed
episodes in episodic memory to guide future deci-
sions. Although ReAct and Reflexion improve per-
formance on multi-turn tasks, both methods depend
heavily on self-evaluation quality, which degrades
for smaller LLMs, and cannot structurally suppress
invalid actions since prompting alone cannot alter
action priors.
2.2 Reinforcement Learning for LLM Agents
Recently, reinforcement learning (RL) has emerged
as a principled approach for post-training LLMs,
with growing focus on agent-based LLMs in multi-
turn environments. PPO (Schulman et al., 2017)
and its critic-free variant GRPO (Shao et al.,
2024), which estimates baselines from group roll-
out scores, are widely adopted for RL-based LLM
training. RLOO (Kool et al., 2019; Ahmadian et al.,
2024) further reduces variance without a learned
critic, and AGILE (Feng et al., 2024) applies PPO
to LLM agents using a four-module architecture
with proactive expert consultation, significantly out-
performing prompting on long-horizon QA tasks.
Retrospex (Xiang et al., 2024) combines an offline
RL critic with LLM action likelihood through dy-
namic rescoring, improving performance on ALF-
World and WebShop over prompting baselines.
GiGPO (Feng et al., 2025) captures global trajec-
tory quality and group-level effectiveness without
additional rollouts, providing rich signals for LLM
agent learning. Recently, ProxMO (Fang et al.,
2026) presents a framework to address GRPO’s
context-agnostic normalization and GiGPO’s dis-
crete state-grouping limitation. They explore the
provision of gradient intensities based on task diffi-
culty, and replace hard boundary partitioning with
continuous semantic similarity weighting, so as
to provide richer reward signals that are less task-
agnostic. In totality, these works establish multi-
ple avenues to improve vanilla RL for multi-turn
LLM agents, such as stable baselines and sup-
porting tools to provide more information about
the world. However, they do not directly address
the exploration failure modes we identify in this
work. Specifically, we explore the notion of invalid
actions that arise from environment precondition
mismatches, resulting in action loops driven by
high-confidence but unproductive behaviors. Our
approach adds a conditional intrinsic reward that
explicitly penalizes such behaviors during RL train-
ing.
Recent RL methods for multi-turn LLM agents
focus on improving credit assignment, exploration,
and training stability. ArCHer (Zhou and Zanette,
2024) introduces a hierarchical RL framework com-
bining off-policy temporal difference learning at
the utterance level with on-policy policy gradi-
ents at the token level, substantially improving
sample efficiency over PPO while emphasizing
information-seeking behavior in multi-turn settings.
Tree-GRPO (Ji et al., 2026) improves training ef-
ficiency by replacing chain-based rollouts with
tree-structured sampling, enabling step-level su-
pervision from outcome rewards alone. Address-
ing exploration instability, EPO (Xu et al., 2025)
identifiesexploration-exploitation cascade failure
in shared multi-turn policies and mitigates it via
trajectory-level entropy regularization and entropy
smoothing, yielding gains on ScienceWorld and
ALFWorld. Similarly, RAGEN (Wang et al., 2025)
studies multi-turn RL failure modes, identifying
an “Echo Trap” caused by reward variance cliffs
and gradient spikes, and proposes trajectory fil-
tering with a critic for stabilization. While these
works improvehowagents learn—through efficient
credit propagation, entropy stabilization, or robust
optimization—our approach is complementary, fo-
cusing onwhatto explore by penalizing invalid
or repetitive actions that fail to expand state-space
knowledge, without itself performing credit assign-
ment across turns.
2.3 Intrinsic Motivation and Exploration in
RL
Intrinsic motivation has long been used to im-
prove exploration under sparse rewards by encour-
aging state diversity and novelty. Curiosity-based
methods like Pathak et al. (2017); Burda et al.
(2019) reward novel states or high prediction er-
rors, while count-based exploration formalizes re-
3

visitation penalties through information gain via
KL-divergence between prior and posterior state
beliefs (Bellemare et al., 2016). Extending state-
entropy exploration to task-reward settings, Kim
et al. (2023) propose value-conditional state en-
tropy (VCSE), addressing the tendency of naive
entropy maximization to overexplore low-value
regions by maximizing entropy within value par-
titions. Mutti et al. (2021); Ashlag et al. (2025)
further provide a theoretical foundation for state
entropy regularization, showing that it improves
robustness and promotes broader coverage across
multiple viable trajectories, unlike policy entropy
which mainly injects noise along a dominant path.
These works motivate our approach – by target-
ing state-space entropy, our conditional intrinsic
penalty discourages revisiting already-observed
states. Additionally, by tying the penalty to in-
formation gain rather than raw visitation counts,
we ensure that only transitions that fail to expand
the agent’s knowledge are penalized, preserving
the pull of the task reward toward goal-relevant
states.
In LLM-based RL, intrinsic signals have recently
been explored to complement sparse task rewards.
MIRA (Nourzad and Joe-Wong, 2026) improves
exploration by using memory graphs from agent
trajectories and semantic reasoning to shape PPO
advantages, mitigating poor early critic calibration.
Similarly, our approach leverages accumulated ex-
perience for exploration, but instead defines an
information-gain-based intrinsic signal that penal-
izes observations failing to expand state knowl-
edge. This is simpler to compute, and is moti-
vated by Shannon entropy (Proposition 2), while
being aligned with repetitive and invalid behaviors
in text-based environments. Further recent work
on moral intrinsic rewards (Tennant et al., 2025)
has shown that intrinsic signals can shape agent be-
havior toward desired norms without task-specific
reward engineering, reinforcing the broader appli-
cability of intrinsic motivation for LLM alignment.
Our contribution fits within this emerging direc-
tion: intrinsic rewards as a practical mechanism for
shaping LLM agent behavior in ways that extrinsic
rewards alone cannot achieve.
3 Methodology
3.1 Problem Setup
We consider reinforcement learning for LLM
agents operating in partially observable, long-
horizon interactive environments. At each timestep
t, the agent is in state st, takes an action at ∈ A,
and receives an observation ot from the environ-
ment. We define the agent’s state st as the set
of all observations received so far along the trajec-
tory, i.e., the information the agent has accumulated
about the environment up to time t. The objective
is to learn a policy π(at |s t) that maximizes ex-
pected cumulative reward while completing the
task within a finite horizonT.
Unlike standard short-horizon decision prob-
lems, this setting introduces two recurring failure
modes. First, the agent may produceinvalid ac-
tionswhose preconditions are not satisfied, caus-
ing the transition to fail or yielding no meaningful
progress. Second, the agent may enteraction loops,
repeatedly selecting a small set of actions that do
not improve task state or move the agent closer to
completion. Both issues reduce learning efficiency
and often reflect an imperfect internal model of the
environment dynamics. In practice, these failures
are especially harmful in LLM agents because they
waste interaction budget and reinforce unproduc-
tive behavior patterns.
3.2 State Representation
To support long-horizon decision making, we de-
fine the agent’s state as the accumulated observa-
tion history:
st ={o 1, o2, . . . , ot}.
This representation captures the information avail-
able to the agent at time t. Instead of relying only
on the most recent observation, the agent maintains
a memory of the full trajectory ofunique observa-
tions, enabling it to reason about what has already
been explored and what remains uncertain. This
accumulated state serves as the basis for evaluat-
ing whether a new observation provides additional
information about the environment.
At each step, the agent observes the current state
st, selects an action at, and receives the next obser-
vation ot+1. The state is then updated by appending
the new observation:
st+1 =s t ∪ {ot+1}.
The intrinsic reward is computed from the change
in information content between st and ot+1. If
the new observation does not improve the agent’s
knowledge of the environment, a negative intrinsic
reward is assigned. This signal is combined with
the task reward and used to update the policy.
4

3.3 Conditional State-Space Exploration
We propose a conditional state-space exploration
mechanism that penalizes unhelpful transitions. Af-
ter taking action at, the agent receives a new obser-
vation ot+1, and the information gain is computed
by comparing this new observation with the previ-
ous state st. Let I(·) denote a measure of informa-
tion content or entropy associated with the agent’s
accumulated state representation. We define the
change in information as
∆I(s t, ot+1) =I(s t ∪ {ot+1})−I(s t).
This quantity measures whether the new observa-
tion expands the agent’s knowledge of the environ-
ment.
The intrinsic reward is then defined as:
rintrinsic t =
(
−γif∆I(s t, ot+1)≤0,
0otherwise, (1)
where γ >0 controls the penalty magnitude.
This formulation penalizes actions that do not lead
to a meaningful increase in the agent’s informa-
tion about the environment, thereby discouraging
redundant or cyclic behavior.
The formulation is general, and I(·) can be any
measure of the information in the agent’s mem-
ory. In practice, we use a simple instantiation,
I(s) = log|s| , with new observations compared
by string matching. Then ∆I(s t, ot+1)≤0 iff
ot+1 ∈s t, and Equation 1 reduces to a duplicate-
observation penalty (Algorithm 1). Exact match-
ing suffices in many settings, includingALFWorld,
where environment feedback is drawn from a fixed
set of templated observations, so identical states
produce identical text. It errs only toward under-
penalization, since it may miss near-duplicates but
never penalizes a genuinely new observation. Un-
like similarity-based measures, it also requires no
threshold and adds no hyperparameters beyond γ.
Moreover, since the agent controls actions rather
than observation text, it can avoid the penalty only
by reaching a different state. More sophisticated
measures, such as embedding similarity, are needed
only in environments with free-form or noisy ob-
servations, where the same state can be described
in different ways.
How Does the Penalty Teach Preconditions?
Let F(s) be the set of actions whose precondi-
tions fail in state s. We assume that (A1) every
Algorithm 1Computation of the intrinsic reward
Require: state memory st ={o 1, . . . , ot}, new
observationo t+1, penalty weightγ
1:ifo t+1 ∈s t then
2:r intrinsic t ← −γ
3:s t+1 ←s t
4:else
5:r intrinsic t ←0
6:s t+1 ←s t ∪ {ot+1}
7:end if
8:returnr intrinsic t ,s t+1
a∈ F(s) returns the same observation o⊥, inde-
pendent of a and s, and (A2) a failed action leaves
the state unchanged. Under A1, every precondi-
tion violation after the first in an episode yields
ot+1 =o ⊥ ∈s t and is penalized, whichever ac-
tion failed. The policy is thus pushed away from
all precondition-violating actions, not only from
repeating one. Under A2, avoiding them loses no
information, so the penalty does not conflict with
information gathering.
3.4 Final Reward
The final reward used for policy optimization com-
bines the task reward and the intrinsic reward:
rt =r task t +λr intrinsic t ,
where λ≥0 balances task performance and explo-
ration pressure. The resulting objective is
J(π) =E π
"T−1X
t=0
ρtrt
#
,
where ρ∈[0,1] is the discount factor. This objec-
tive encourages the agent to maximize task reward
while avoiding actions that fail to improve state-
space coverage.
3.5 Entropy-Oriented Exploration Objective
The motivation for this design is that directly maxi-
mizing state-space entropy can sometimes distract
the agent from the task objective. An overly strong
incentive for novelty may lead the policy to ex-
plore diverse but irrelevant trajectories. By con-
trast, penalizing non-informative actions creates
a task-constrained pressure toward visiting more
distinct observations within an episode. The pol-
icy is discouraged from remaining in low-diversity
5

action cycles, but it is still constrained by the ex-
ternal task reward, which ensures that exploration
remains useful for task completion.
This conditional structure is especially impor-
tant in long-horizon environments, where the agent
must balance exploration and exploitation over
many sequential decisions. Actions that expand
state coverage or contribute to task progress re-
ceivenointermediate positive incentive. However,
actions that actively fail to improve the agent’s state
knowledge arepenalized. As a result, the learned
policy is pushed toward trajectories that are both
diverse and productive.
This penalization mechanism encourages pro-
ductive exploration by discouraging repeated ob-
servations and promoting broader coverage of the
agent’s experience. It is related to information-
theoretic exploration, which uses visitation entropy
to characterize exploration diversity. Below, we for-
malize this connection through single-step changes
in visitation entropy and episode-level coverage.
Let Pt denote the empirical observation-
visitation distribution over o1, . . . , ot, with p(t) i =
c(t) i /N, where c(t) i counts occurrences of the i-
th distinct observation, n=|s t|, and N=Pn
i=1 c(t) i =t≥1 . Its Shannon entropy
is H(P t) =− Pn i=1 p(t) i logp (t) i . Unlike the
memory-based measure I(s t) = log|s t|, H(P t)
accounts for observation frequencies.
Proposition 1.For the distribution Pt defined
above, let n=n t be the number of distinct states
observed by time t. States are identified with obser-
vations in the memorys t. Then,
1. If the new observation introduces a previously
unseen state, thenH(P t+1)> H(Pt).
2. If the new observation repeats an already-
visited state k satisfying p(t) k ≥e −H(P t), then
H(P t+1)≤H(P t).
Proof. Let α= 1/(N+ 1) , where N=t is the
total count of observations. The update induced by
a new observation can be written as
Pt+1 = (1−α)P t +αe,
whereeis a point mass on the observed state.
Case 1: Introduction of a new state.
Suppose the observation corresponds to a previ-
ously unseen state. Then the support expands by
one dimension and
Pt+1 =

(1−α)P t, α

.
The entropy of the updated distribution decom-
poses as
H(P t+1) = (1−α)H(P t) +h(α),
where h(α) =−(1−α) log(1−α)−αlogα is
the binary entropy term arising from introducing
the new state. Therefore,
H(P t+1)−H(P t) =h(α)−αH(P t).
Since the support size before the update is at most
N,
H(P t)≤logN.
Substitutingα= 1/(N+ 1)gives
h(α)−αH(P t)≥h(α)−αlogN
=αlog N+ 1 N −(1−α) log(1−α)
>0
HenceH(P t+1)> H(Pt).
Case 2: Repetition of an existing state.
Suppose the observation revisits an already-seen
statek∈ {1, . . . , n}. Then
Pt+1 = (1−α)P t +αe k,
where ek is the point mass on statek. For λ∈[0,1] ,
define
f(λ) =H((1−λ)P t +λe k).
If Pt =e k, then f(λ) = 0 for all λ∈[0,1] . Other-
wise, since Shannon entropy is strictly concave on
the simplex and Pt ̸=e k, f is strictly concave in λ.
Its right derivative atλ= 0is
f ′(0) =−H(P t)−logp (t) k .
Thus,
f ′(0)≤0⇐ ⇒p (t) k ≥e −H(P t).
By concavity, a non-positive initial slope implies
f(λ)≤f(0)
for all λ∈(0,1] . If Pt ̸=e k, strict concavity gives
f(λ)< f(0)for allλ∈(0,1].
Takingλ=αgives
H(P t+1)≤H(P t),
with strict inequality unlessP t =e k.
6

Remark 1.Proposition 1 formalizes the intuition
underlying our intrinsic penalty at the level of a
single visitation update. Introducing novel states
strictly increases visitation entropy, whereas re-
peatedly revisiting sufficiently frequent states re-
duces entropy and concentrates probability mass.
Penalizing repeated observations therefore discour-
ages unproductive revisitation and is directionally
aligned with broader intrinsic exploration.
Proposition 2(Whole-episode coverage and en-
tropy).Consider an episode with observations
o1, . . . , oL and D=|{1≤t < L:o t+1 ∈s t}| du-
plicate steps. Then |sL|=L−D , and the undis-
counted cumulative intrinsic reward is
Rint =
L−1X
t=1
rintrinsic t =−γD=−γ(L− |s L|).
Thus, at fixed episode length L, maximizing Rint
maximizes within-episode coverage |sL|. More-
over,
H(P L)≤log(L−D),
H(P L)≥logL− D+ 1 L log(D+ 1).
The lower bound is attained, both bounds are de-
creasing in D, and both equal logL if and only if
D= 0, equivalentlyR int = 0.
Proof. Coverage. o1 is always novel, and each
subsequent observation either adds one element to
the memory or is a duplicate. Therefore,
|sL|= 1 + (L−1−D) =L−D.
By the definition of the intrinsic reward,
Rint =−γD=−γ(L− |s L|).
Upper bound.Entropy is at most the logarithm
of the support size:
H(P L)≤log|s L|= log(L−D).
Lower bound.For positive integer counts
c1, . . . , cL−D summing toL,
H(P L) = logL− 1 L L−DX i=1 ci logc i.
The sum P i ci logc i is maximized when the counts
are (D+1,1, . . . ,1). Indeed, whenever two counts
satisfy a≥b >1 , moving one unit from b to a
does not decrease the sum, since xlogx is convex.
Repeating this operation leaves all but one count
equal to1. Therefore,
H(P L)≥H
 D+ 1
L , 1 L , . . . ,1 L 
= logL− D+ 1 L log(D+ 1),
with equality when the count vector is (D+
1,1, . . . ,1), up to permutation.
Monotonicity.The upper bound log(L−D) is
strictly decreasing in D. The lower bound is also
strictly decreasing, since (D+ 1) log(D+ 1) is
strictly increasing for D≥0 . Both bounds equal
logL when D= 0 and are strictly below logL
when D≥1 . Since γ >0, D= 0 if and only if
Rint = 0.
Remark 2.Proposition 2 establishes that, for a
fixed episode length, maximizing the cumulative
intrinsic reward is equivalent to maximizing within-
episode coverage. It also bounds the visitation
entropy in terms of the number of duplicate steps,
showing that fewer duplicates permit higher en-
tropy. However, we do note that maximizing cover-
age does not necessarily maximize entropy across
trajectories, since entropy also depends on the fre-
quency distribution of visited observations.
4 Experiments
In this section, we report the experimental results
of our proposed approach of productive state-space
exploration. We evaluate our method against sev-
eral recent baselines across two interactive agent
benchmarks: ALFWorld (Shridhar et al., 2020) and
WebShop (Yao et al., 2022). With this, we aim to
demonstrate two main benefits of our proposed ap-
proach. First, the performance improvements due
to the intrinsic reward signals. Second, the explo-
ration behavior and its usefulness in overcoming
the repeated actions and looping behavior of RL
trained LLM agents.
4.1 Baselines
For the performance comparison, we benchmark
against several state-of-the-art recent baseline
models. These include prompting frameworks
and those trained with RL. The prompting base-
lines are Gemini-2.5 (Team et al., 2023), GPT-
4o (Achiam et al., 2023), Qwen-2.5 (Qwen et al.,
2025), ReAct (Yao et al., 2023) and Reflex-
ion (Shinn et al., 2023) frameworks. The RL
trained baselines include PPO (Schulman et al.,
7

Table 1: Performance on ALFWorld and WebShop. Following GiGPO, for ALFWorld environment we report the
average success rate (%) for each subtask along with the overall result. For WebShop environment, we report the
average score and the average success rate (%). Prompting/PPO/RLOO/GRPO/GiGPO rows are quoted from Feng
et al. (2025); ProxMO from Fang et al. (2026).
Type Method ALFWorld WebShop Pick Look Clean Heat Cool Pick2 All Score Succ.
Closed-Source Model
Prompting GPT-4o 75.3 60.8 31.2 56.7 21.6 49.8 48.0 31.8 23.7
Prompting Gemini-2.5-Pro 92.8 63.3 62.1 69.0 26.6 58.7 60.3 42.5 35.9
Qwen2.5-1.5B-Instruct
Prompting Qwen2.5 5.9 5.5 3.3 9.7 4.2 0.0 4.1 23.1 5.2
Prompting ReAct 17.4 20.5 15.7 6.2 7.7 2.0 12.8 40.1 11.3
Prompting Reflexion 35.3 22.2 21.7 13.6 19.4 3.7 21.8 55.8 21.9
RL Training PPO (with critic) 64.8 (3.5) 40.5(6.9) 57.1(4.9) 60.6(6.6) 46.4(4.0) 47.4(1.9) 54.4(3.1) 73.8(3.0) 51.5(2.9)
RL Training RLOO 88.3 (3.0) 52.8(8.6) 71.0(5.9) 62.8(8.7) 66.4(5.5) 56.9(4.7) 69.7(2.5) 73.9(5.6) 52.1(6.7)
RL Training GRPO 85.3 (1.5) 53.7(8.0) 84.5(6.8) 78.2(7.9) 59.7(5.0) 53.5(5.6) 72.8(3.6) 75.8(3.5) 56.8(3.8)
RL Training GiGPO 94.4 (5.9) 67.5(4.6) 94.8(3.8) 94.4(7.8) 79.8(4.7) 76.4(5.4) 86.7(1.7) 83.1(1.6) 65.0(3.2)
RL Training ProxMO 94.3 (–) 92.9(–) 89.3(–) 92.2(–) 89.5(–) 87.0(–) 90.6(–) 85.3(–) 67.1(–)
RL Training OURS (PPO) 99.5(0.7) 95.5(6.4) 99.7(0.4) 97.1(2.9) 87.4(1.6) 83.9(3.7) 94.0(1.2) 89.2(1.1) 78.3(1.2)
Table 2: Exploration efficiency on ALFWorld and WebShop. We compare our method with GiGPO using three
metrics: mean episode length, invalid action rate, and repetitive action rate. Both GiGPO and our method are run by
us under the same setup. Lower values indicate more productive exploration.
Method ALFWorld WebShop Mean Episode Length Invalid Action Rate Repetitive Action Rate Mean Episode Length Invalid Action Rate Repetitive Action Rate
GiGPO 32.27 4.08 45.31 5.53 0.14 43.25
Ours22.02 2.79 11.53 5.18 0.09 40.83
2017), RLOO (Kool et al., 2019; Ahmadian et al.,
2024), GRPO (Shao et al., 2024), GiGPO (Feng
et al., 2025), ProxMO (Fang et al., 2026). The
most recent and relevant baselines for our approach
are GiGPO and ProxMO, since we aim to address
challenges in multi-turn LLM agent training with
RL. We do not re-run these baselines, all Table 1
numbers except our method are quoted from their
original publications. For the additional analyses
(Table 3, Sections 4.4–4.5 and Appendix A.2), we
re-train GiGPO with the latest officialverl-agent
implementation, without the intrinsic penalty, and
evaluate it under exactly the same protocol as our
agent.
4.2 Training Details:
We train Qwen-2.5-1.5B-Instruct model with the
proposed state-space exploration rewards along
with Proximal Policy Optimization (PPO) based
RL training. We run all our experiments on top of
verl-agentframework released by GiGPO (Feng
et al., 2025). We train for 300 steps with all other
hyperparameters kept same as in the framework.
We set the maximum steps at 50 for ALFWorld and
15 for WebShop as with GiGPO. The strength of
state-space exploration penalty, γ, as defined in
Equation 1, is set 1 40 of the final success reward.
Full reproducibility details (γ selection, reward nor-
malization, splits) are in Appendix A.3.
4.3 Results
Table 1 compares our proposed method (labelled
OURS) against existing prompting-based and re-
inforcement learning (RL) training approaches on
the ALFWorld and WebShop benchmarks. Follow-
ing prior work, we report the average success rate
for each ALFWorld subtask together with the over-
all success rate. For WebShop, we report both the
average task score and the average success rate.
We primarily compare our approach against
recent RL optimization methods, namely GiGPO
(Group-in-Group Policy Optimization) and
ProxMO (Fang et al., 2026), which represent
strong baselines for LLM agent training. Com-
pared to GiGPO, our method achieves consistent
gains across all ALFWorld subtasks, improving
the overall success rate from 86.7% to 94.0%.
The improvements are particularly pronounced
on challenging long-horizon tasks such asCool
(+7.6%) andPick2( +7.5%), indicating stronger
sequential reasoning and more effective action
planning. On WebShop, our intrinsic-rewards
8

Figure 2: A successful ALFWorld episode of the agent trained with our intrinsic reward, shown in two halves. The
agent searches eight locations, revisiting only two, then takes, cleans and places the butterknife in 18 steps without a
single invalid action.
approach improves the average task score from
83.1 to 89.2 and substantially increases the success
rate from 65.0% to 78.3%, demonstrating superior
capability in complex web-based interaction tasks.
Compared to ProxMO, a recent proximity-based
multi-turn optimization framework designed for
practical credit assignment in LLM agent training,
our approach still achieves better overall perfor-
mance across both benchmarks. Specifically, it
improves the overall ALFWorld success rate from
90.6% to 94.0%, while increasing theWebShop suc-
cess rate from 67.1% to 78.3%. The improvements
on ALFWorld are especially significant, suggesting
that our method generalizes more effectively in
environments requiring long-horizon exploration,
recovery from intermediate mistakes, and consis-
tent multi-turn decision making.
Generalization to unseen scenes.To test
whether these gains carry over to environments
not seen during training, we evaluate our agent and
the re-trained GiGPO agent (Section 4.1) on the
ALFWorld out-of-distribution split, which contains
unseen scenes, and on the in-distribution split under
the same protocol (128 episodes each, same games
for both agents; Appendix A.2). Since these are
Table 3: Success rate (%) on seen and unseenALFWorld
scenes for our agent and the re-trained GiGPO.
Split Method Pick Look Clean Heat Cool Pick2 All
Seen GiGPO 92.3 84.6 92.0100.0 81.283.3 89.1 Ours100.0 100.0 100.090.981.2 91.7 95.3
Unseen GiGPO 82.6 91.3 79.2 73.7 87.0 81.2 82.8 Ours95.7 100.0 91.7 89.5 100.0 87.5 94.5
single evaluations of one checkpoint per method,
the seen-scene numbers differ slightly from Ta-
ble 1, where the GiGPO result is quoted from its
original paper. Table 3 shows that our agent gen-
eralizes markedly better. Its success rate is nearly
unchanged on unseen scenes, whereas GiGPO’s
drops noticeably, so the gap between the two agents
roughly doubles, and our agent leads on every task
type.
4.4 Intrinsic Productive Exploration
To look beyond overall success rates, we evaluate
the behavioral dynamics of our agent against the
competitive baseline GiGPO (Feng et al., 2025).
This analysis focuses onintrinsic productive explo-
ration- the agent’s capacity to autonomously dis-
cover optimal state-action trajectories through tar-
9

geted, purposeful environment interactions, rather
than wasting computational steps on redundant or
unproductive behaviors. We define three behav-
ioral diagnostics across theALFWorld and WebShop
benchmarks to quantify the efficiency and produc-
tivity of the agent’s intrinsic exploration strategy:
• Mean Episode Length:The average number of
sequential steps to complete a task instance.
• Invalid Action Rate:The frequency of actions
that fail (violate action preconditions). It is de-
tected as described in Appendix A.3.
• Repetitive Action Rate:The frequency of steps
spent executing identical actions. We consider
an action repetitive when either the action or the
resulting observation is repeated in the trajectory.
The empirical results detailing these behavioral
metrics are shown in Table 2. In ALFWorld, our
method compresses the Mean Episode Length from
≈32 steps down to ≈22 relative to GiGPO. Simi-
lar trend persists in the WebShop, where the gains
are not as profound as in ALFWorld, however help
in score improvement compared to GiGPO. More
broadly, the results suggest:
• Learning of Environment Dynamics:The im-
provement in Mean Episode Length and Invalid
Action Rate shows that the agent better under-
stands the environment dynamics and, in particu-
lar, rarely repeats actions that have already failed.
• Loop Resolution and Novelty Seeking:The
most supporting evidence of productive explo-
ration is revealed by theRepetitive Action Rate
in ALFWorld. While GiGPO spends 45.31% of
its execution trajectory repeating identical com-
mands, our approach drops this rate dramatically
to 11.53%. This absolute reduction of 33.78%
demonstrates that our intrinsic penalty inherently
disincentivizes stale, repeated states. Instead, it
forces the agent to continuously break out of
loops and seek novel, progressive environmental
interactions.
Both the above inferences can also be seen in
qualitative action trajectories as shown in Figure 2.
The contrast in the decrease in the number of in-
valid actions relative to Figure 1 suggests our ap-
proach of penalizing actions which repeat states is
indeed helpful in reducing the redundancy of the
agent’s trajectory.
To examine information gathering more closely,
we record every step of our agent and of the re-
trained GiGPO agent (Section 4.1). Our agent
searches the partially observable environment more
widely while wasting fewer steps: it visits more
distinct locations, revisits fewer of them, ob-
tains new information from a larger share of its
information-gathering actions, and finds the target
object more often. The two agents also fail differ-
ently. GiGPO’s failed episodes are dominated by
repeated observations, whereas ours keep exploring
new states until the step budget runs out. These ad-
vantages hold on both seen and unseen scenes. Per
action, both agents satisfy preconditions for nearly
all of their actions; our agent’s advantage lies in
avoiding repeated failures rather than in avoiding a
first one (Appendix A.2).
4.5 Effect of the Intrinsic Penalty on
Exploration
To isolate the effect of the penalty, we train two
PPO agents from the same base model with iden-
tical settings, differing only in the penalty weight
(γ= 0 vs. γ= 1 40 of the success reward), and
evaluate them after 100 training steps (details in
Appendix A.2). We measure exploration by the
duplicate-observation rate (steps whose observa-
tion repeats an earlier one), the location revisit
rate (go to actions to an already visited location),
the new-information rate (information-gathering
actions go to , open and examine that reveal a new
observation), and whether the target object is ever
observed. A precondition violation is an executed
action outside the environment’s admissible set; we
report violations after the first one in an episode
and the recovery rate, i.e. how often the action fol-
lowing a violation is admissible.
The penalty broadens exploration during train-
ing.Starting from identical behavior, the penalized
agent reduces repeated observations much faster
and covers a substantially larger part of the state
space (Figure 3). This broader exploration precedes
its gain in success, which emerges after the first 50
steps.
The learned policy explores productively at test
time.It repeats observations and revisits locations
far less often, gains new information from more of
its actions, and finds the target object more often,
equally on seen and unseen scenes (Table 4).
Better exploration leads to better use of feed-
back and higher success.Since repeated failures
reveal nothing new, the penalized agent makes far
10

0 50 100
20
30
40
50
Validation success (%)
0 50 100
40
50
60
70
Duplicate-observation rate (%)
0 50 100
Training step
12.5
15.0
17.5
20.0
22.5
Distinct observations / episode
0 50 100
Training step
0
50
100 penalty
no penalty
Cumulative distinct states (k)
no penalty ( = 0)
 penalty ( = 1/40)
Figure 3: Controlled comparison of our model with
and without the intrinsic penalty during the first 100
training steps (identical settings). Top: validation suc-
cess and duplicate-observation rate in the training roll-
outs. Bottom: distinct observations per episode in the
training rollouts and the cumulative number of distinct
(game, observation) states visited during training. Roll-
out curves are 10-step moving averages.
Table 4: Effect of the intrinsic penalty: PPO with γ= 0
vs. ours (identical settings, 100 training steps), same
128 episodes per split.
Seen scenes Unseen scenes
Metricγ= 0Oursγ= 0Ours
Exploration
Duplicate-observation rate 59.3%37.0%61.8%36.6%
Location revisit rate 68.6%41.3%68.7%42.3%
New-information rate of info. actions 43.5%67.4%40.4%67.1%
Distinct locations visited 4.686.174.876.88
Target object found 76.6%87.5%64.8%85.9%
Preconditions
Precondition satisfied 68.0%82.4%67.8%81.9%
Violations after the first, per episode 9.874.6510.125.09
Recovery after a violation 47.2%59.9%50.8%64.2%
fewer repeated precondition violations, recovers
more often, satisfies preconditions more often, and
succeeds considerably more often on both splits.
Absolute success is lower than in Table 1 because
of the shorter training.
5 Conclusion
In this paper, we addressed the tendency of RL-
trained LLM agent policies to repeat invalid ac-
tions and fall into action loops in multi-turn, long-
horizon environments. We introduced a condi-
tional state-space exploration framework driven
by an information-aware intrinsic reward. Instead
of directly maximizing unconstrained state entropy,
which risks driving the agent toward task-irrelevant
trajectories, our approach reframes exploration by
penalizing actions that produce redundant state in-
formation. Our experimental evaluation demon-
strates that this framework achieves substantial per-
formance gains and significantly mitigates action
repetition and circular reasoning patterns.
Limitations
Our experiments are conducted primarily on
smaller reasoning models. Because exploration
strategies are inherently influenced by a model’s
overall capacity and pre-trained priors, larger
instruction-tuned models may exhibit fewer fail-
ures than those documented in this study. Growth
in model scale often mitigates baseline reasoning
bottlenecks; nevertheless, optimizing smaller mod-
els remains highly valuable. Enhancing the ca-
pabilities of these smaller architectures enables
more practical, targeted applications, particularly
in hardware-constrained environments where de-
ployment efficiency is critical.
Additionally, this work focuses specifically on
text-based environments within ALFWorld and
WebShop, which feature relatively small, well-
defined action spaces that lend themselves well
to set representations. Environments with larger,
continuous, or stochastic action spaces may exhibit
vastly different dynamics under this set-based state
representation, potentially limiting direct general-
izability.
Regardless of these limitations, our approach
provides a structurally sound framework for agent
reasoning and state representation in multi-turn
settings. Ultimately, the insights gained from our
set-based representation and reward design estab-
lish a foundation for future scaling and adaptation
across more complex, open-ended environments.
Acknowledgments
This research was supported by fundings
from the Hong Kong RGC General Research
Fund (152228/23E, 162161/24E, 162116/25E,
162180/25E), National Natural Science Foundation
of China (NSFC) Key Program (No.62532005),
Collaborative Research Fund (No. C1042-23GF,
No. 5097-25G), NSFC/RGC Collaborative
Research Scheme (Grant No. 62461160332 &
CRS_HKUST602/24), Research Impact Fund
(No. R5011-23), and Areas of Excellence Scheme
(AoE/E-601/22-R).
11

References
Josh Achiam, Steven Adler, Sandhini Agarwal, Lama
Ahmad, Ilge Akkaya, Florencia Leoni Aleman,
Diogo Almeida, Janko Altenschmidt, Sam Altman,
Shyamal Anadkat, and 1 others. 2023. Gpt-4 techni-
cal report.arXiv preprint arXiv:2303.08774.
Arash Ahmadian, Chris Cremer, Matthias Gallé,
Marzieh Fadaee, Julia Kreutzer, Olivier Pietquin, Ah-
met Üstün, and Sara Hooker. 2024. Back to basics:
Revisiting reinforce-style optimization for learning
from human feedback in llms. InProceedings of the
62nd Annual Meeting of the Association for Compu-
tational Linguistics (Volume 1: Long Papers), pages
12248–12267.
Yonatan Ashlag, Uri Koren, Mirco Mutti, Esther Der-
man, Pierre-Luc Bacon, and Shie Mannor. 2025.
State entropy regularization for robust reinforcement
learning. InAdvances in Neural Information Pro-
cessing Systems.
Arthur Aubret, Laetitia Matignon, and Salima Hassas.
2019. A survey on intrinsic motivation in reinforce-
ment learning.arXiv preprint arXiv:1908.06976.
Marc G. Bellemare, Sriram Srinivasan, Georg Ostro-
vski, Tom Schaul, David Saxton, and Rémi Munos.
2016. Unifying count-based exploration and intrinsic
motivation. InProceedings of the 30th International
Conference on Neural Information Processing Sys-
tems, NIPS’16, page 1479–1487, Red Hook, NY ,
USA. Curran Associates Inc.
Yuri Burda, Harri Edwards, Deepak Pathak, Amos
Storkey, Trevor Darrell, and Alexei A. Efros. 2019.
Large-scale study of curiosity-driven learning. In
ICLR.
Thomas Carta, Clément Romac, Thomas Wolf, Sylvain
Lamprier, Olivier Sigaud, and Pierre-Yves Oudeyer.
2023. Grounding large language models in interac-
tive environments with online reinforcement learn-
ing. InInternational conference on machine learning,
pages 3676–3713. PMLR.
Nuttapong Chentanez, Andrew Barto, and Satinder
Singh. 2004. Intrinsically motivated reinforcement
learning.Advances in neural information processing
systems, 17.
Yangyi Fang, Jiaye Lin, Xiaoliang Fu, Cong Qin, Haolin
Shi, Chang Liu, and Peilin Zhao. 2026. Proximity-
based multi-turn optimization: Practical credit as-
signment for llm agent training.arXiv preprint
arXiv:2602.19225.
Lang Feng, Zhenghai Xue, Tingcong Liu, and Bo An.
2025. Group-in-group policy optimization for LLM
agent training. InAdvances in Neural Information
Processing Systems.
Peiyuan Feng, Yichen He, Guanhua Huang, Yuan Lin,
Hanchong Zhang, Yuchen Zhang, and Hang Li. 2024.
Agile: A novel reinforcement learning framework of
llm agents.Advances in Neural Information Process-
ing Systems, 37:5244–5284.
Jingtong Gao, Ling Pan, Yejing Wang, Rui Zhong, Chi
Lu, Maolin Wang, Qingpeng Cai, Peng Jiang, and Xi-
angyu Zhao. 2025. Navigate the unknown: Enhanc-
ing llm reasoning with intrinsic motivation guided
exploration.arXiv preprint arXiv:2505.17621.
Shengyue Guan, Jindong Wang, Jiang Bian, Bin Zhu,
Jian-Guang Lou, and Haoyi Xiong. 2026. Evaluating
llm-based agents for multi-turn conversations: A sur-
vey.ACM Transactions on Intelligent Systems and
Technology, 17(4):1–40.
Yuxiang Ji, Ziyu Ma, Yong Wang, Guanhua Chen, Xi-
angxiang Chu, and Liaoni Wu. 2026. Tree search for
LLM agent reinforcement learning. InInternational
Conference on Learning Representations.
Vivek Kalyan and Martin Andrews. 2025. Reinforce-
ment learning for long-horizon multi-turn search
agents.arXiv preprint arXiv:2510.24126.
Dongyoung Kim, Jinwoo Shin, Pieter Abbeel, and
Younggyo Seo. 2023. Accelerating reinforcement
learning with value-conditional state entropy explo-
ration.Advances in Neural Information Processing
Systems, 36:31811–31830.
Wouter Kool, Herke van Hoof, and Max Welling. 2019.
Buy 4 reinforce samples, get a baseline for free!
Keliang Liu, Dingkang Yang, Ziyun Qian, Weijie Yin,
Yuchi Wang, Hongsheng Li, Jun Liu, Peng Zhai,
Yang Liu, and Lihua Zhang. 2025. Reinforcement
learning meets large language models: A survey of
advancements and applications across the llm lifecy-
cle.arXiv preprint arXiv:2509.16679.
Mirco Mutti, Lorenzo Pratissoli, and Marcello Restelli.
2021. Task-agnostic exploration via policy gradi-
ent of a non-parametric state entropy estimate. In
Proceedings of the AAAI conference on artificial in-
telligence, volume 35, pages 9028–9036.
Narjes Nourzad and Carlee Joe-Wong. 2026. MIRA:
Memory-integrated reinforcement learning agent
with limited LLM guidance. InThe Fourteenth Inter-
national Conference on Learning Representations.
Deepak Pathak, Pulkit Agrawal, Alexei A Efros, and
Trevor Darrell. 2017. Curiosity-driven exploration by
self-supervised prediction. InInternational confer-
ence on machine learning, pages 2778–2787. PMLR.
Qwen, :, An Yang, Baosong Yang, Beichen Zhang,
Binyuan Hui, Bo Zheng, Bowen Yu, Chengyuan
Li, Dayiheng Liu, Fei Huang, Haoran Wei, Huan
Lin, Jian Yang, Jianhong Tu, Jianwei Zhang, Jianxin
Yang, Jiaxi Yang, Jingren Zhou, and 25 oth-
ers. 2025. Qwen2.5 technical report.Preprint,
arXiv:2412.15115.
12

John Schulman, Filip Wolski, Prafulla Dhariwal,
Alec Radford, and Oleg Klimov. 2017. Proxi-
mal policy optimization algorithms.arXiv preprint
arXiv:1707.06347.
Lior Shani, Aviv Rosenberg, Asaf Cassel, Oran Lang,
Daniele Calandriello, Avital Zipori, Hila Noga, Or-
gad Keller, Bilal Piot, Idan Szpektor, and 1 others.
2024. Multi-turn reinforcement learning with prefer-
ence human feedback.Advances in Neural Informa-
tion Processing Systems, 37:118953–118993.
Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu,
Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan
Zhang, YK Li, Yang Wu, and 1 others. 2024.
Deepseekmath: Pushing the limits of mathematical
reasoning in open language models.arXiv preprint
arXiv:2402.03300.
Noah Shinn, Federico Cassano, Ashwin Gopinath,
Karthik Narasimhan, and Shunyu Yao. 2023. Re-
flexion: Language agents with verbal reinforcement
learning.Advances in neural information processing
systems, 36:8634–8652.
Mohit Shridhar, Xingdi Yuan, Marc-Alexandre Côté,
Yonatan Bisk, Adam Trischler, and Matthew
Hausknecht. 2020. Alfworld: Aligning text and em-
bodied environments for interactive learning.arXiv
preprint arXiv:2010.03768.
Gemini Team, Rohan Anil, Sebastian Borgeaud, Jean-
Baptiste Alayrac, Jiahui Yu, Radu Soricut, Johan
Schalkwyk, Andrew M Dai, Anja Hauth, Katie Mil-
lican, and 1 others. 2023. Gemini: a family of
highly capable multimodal models.arXiv preprint
arXiv:2312.11805.
Elizaveta Tennant, Stephen Hailes, and Mirco Musolesi.
2025. Moral alignment for LLM agents. InInterna-
tional Conference on Learning Representations.
Zihan Wang, Kangrui Wang, Qineng Wang, Pingyue
Zhang, Linjie Li, Zhengyuan Yang, Xing Jin, Kefan
Yu, Minh Nhat Nguyen, Licheng Liu, and 1 others.
2025. Ragen: Understanding self-evolution in llm
agents via multi-turn reinforcement learning.arXiv
preprint arXiv:2504.20073.
Zhiheng Xi, Jixuan Huang, Chenyang Liao, Baodai
Huang, Honglin Guo, Jiaqi Liu, Rui Zheng, Junjie Ye,
Jiazheng Zhang, Wenxiang Chen, and 1 others. 2025.
Agentgym-rl: Training llm agents for long-horizon
decision making through multi-turn reinforcement
learning.arXiv preprint arXiv:2509.08755.
Yufei Xiang, Yiqun Shen, Yeqin Zhang, and Nguyen
Cam-Tu. 2024. Retrospex: Language agent meets
offline reinforcement learning critic. InProceedings
of the 2024 Conference on Empirical Methods in
Natural Language Processing, pages 4650–4666.
Wujiang Xu, Wentian Zhao, Zhenting Wang, Yu-Jhe Li,
Can Jin, Mingyu Jin, Kai Mei, Kun Wan, and Dim-
itris N Metaxas. 2025. Epo: Entropy-regularized pol-
icy optimization for llm agents reinforcement learn-
ing.arXiv preprint arXiv:2509.22576.
Shunyu Yao, Howard Chen, John Yang, and Karthik
Narasimhan. 2022. Webshop: Towards scalable real-
world web interaction with grounded language agents.
Advances in Neural Information Processing Systems,
35:20744–20757.
Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak
Shafran, Karthik Narasimhan, and Yuan Cao. 2023.
ReAct: Synergizing reasoning and acting in language
models. InInternational Conference on Learning
Representations.
Kaiyan Zhang, Yuxin Zuo, Bingxiang He, Youbang Sun,
Runze Liu, Che Jiang, Yuchen Fan, Kai Tian, Guoli
Jia, Pengfei Li, and 1 others. 2025. A survey of
reinforcement learning for large reasoning models.
arXiv preprint arXiv:2509.08827.
Yifei Zhou and Andrea Zanette. 2024. Archer: training
language model agents via hierarchical multi-turn rl.
InProceedings of the 41st International Conference
on Machine Learning, ICML’24. JMLR.org.
13

A Appendix
A.1 Datasets:
ALFWorld. ALFWorld (Shridhar et al., 2020)
is a text-based interactive environment designed
for studying embodied decision making and long-
horizon reasoning in language agents. Derived
from the ALFRED benchmark, it converts house-
hold manipulation tasks into a partially observable
textual setting where agents interact through natu-
ral language actions and observations. Tasks typi-
cally involve navigation, object manipulation, and
sequential planning over multiple turns, making
the environment particularly suitable for evaluating
reinforcement learning methods for LLM agents
under sparse rewards and delayed feedback. Con-
cretely, ALFWorld contains 6 task types of various
difficulty. The tasks are:
• Pick & Place: agent must find an object of
a specified type, pick it up, find the correct
location to place it, and place it down there.
• Examine in Light: agent must find an object
of a specified type, locate and turn on a light
source with the object still in hand.
• Clean & Place: agent must find an object of a
specified type, pick it up, move to a sink or a
basin, turn on the faucet and wash the object,
find the correct location to place it, and place
it down there.
• Heat & Place: agent must find an object of
a specified type, pick it up, move to the mi-
crowave, heat the object by turning on the
microwave, find the correct location to place
it, and place it down there.
• Cool & Place: agent must find an object of a
specified type, pick it up, move to the fridge,
place the object in the fridge to cool it, find
the correct location to place it, and place it
down there.
• Pick Two & Place: agent must find an object
of a specified type, find the correct location to
place it, place it down there, look for another
object of a specified type, pick up the object,
return to the previous location, place it down
there together with the first object.
WebShop. WebShop (Yao et al., 2022) is an e-
commerce interaction benchmark that evaluates
language agents on realistic online shopping tasks.
In this environment, agents must search through
large collections of products, inspect item descrip-
tions and reviews, and iteratively refine decisions to
satisfy user instructions. Unlike embodied environ-
ments, WebShop emphasizes retrieval, preference
understanding, and multi-step reasoning in semi-
structured web settings. The benchmark is widely
used for evaluating the effectiveness of sequential
decision-making and reinforcement learning ap-
proaches for interactive LLM agents. Concretely,
the WebShop dataset contains 1,000,000 products,
670 unique attributes, 842,849 unique options, ex-
tracted publicly from Amazon. It presents over
12,000 annotated trajectories and an action space
of 8 valid actions.
A.2 Additional Experiments
This subsection reports additional ALFWorld exper-
iments that analyze (i) whether the trained agent
gathers information more effectively at test time,
and (ii) whether more of its actions satisfy their
preconditions. Sections 4.4 and 4.5 summarize the
main findings; here we give the full results.
A.2.1 Test-Time Exploration and
Preconditions
Setup.We compare our agent with a GiGPO
agent that we trained ourselves using the released
verl-agentcode. Both agents play the same 128
evaluation episodes (91 distinct games) from the
ALFWorldin-distribution split, with sampling tem-
perature 0.4 and at most 50 steps. We record every
step (observation, admissible actions, chosen ac-
tion and next observation) and compute all metrics
below per episode, then average over episodes.
Test-time exploration and information gather-
ing. ALFWorld is partially observable: the con-
tents of a receptacle are revealed only when the
agent goes to it or opens it. Table 5 measures how
the agents gather information. Our agent covers
more of the environment with less effort: it vis-
its more distinct locations per episode while tak-
ing fewer steps, revisits locations less often, and a
larger share of its information-gathering actions (go
to, open, examine) reveals a previously unseen ob-
servation. As a result, it finds the target object more
often. When both agents find the target, our agent
gets there in fewer steps despite searching more
locations, i.e. it searches more widely and wastes
fewer steps on revisits. The failure modes also dif-
fer. Failed episodes of both agents exhaust the step
14

budget, but GiGPO’s failures are dominated by rep-
etition, whereas our failed episodes keep exploring
new states.
Table 5: Test-time information gathering (per-episode
means). †Episodes in which both agents find the target.
Metric GiGPO Ours
Success rate 89.1%95.3%
Episode length (steps) 14.712.5
Distinct locations visited 3.665.16
Location revisit rate 31.5%18.9%
New-information rate of info. actions 81.2%89.2%
Duplicate-observation rate 16.7%8.7%
Target object found 91.4%96.9%
Steps until target found† 4.464.19
Locations searched before target† 2.27 3.19
Duplicate-obs. rate in failed episodes 72%27%
Precondition satisfaction at test time.
ALFWorld provides the set of admissible ac-
tions in each state, which are exactly the actions
whose preconditions are satisfied. We therefore
measure, for each action type, how many actions
each agent executes and the fraction of them that
are admissible (Table 6). On the same episodes,
our agent completes the tasks with about 16%
fewer actions. The saving comes almost entirely
from navigation, as it needs far fewer go to
actions, while it uses information-gathering actions
such as open and examine more often. Both
agents satisfy preconditions for nearly all of
their actions, with a small difference in GiGPO’s
favor overall. The per-action picture is mixed:
our agent is more reliable on take and examine,
while GiGPO is more reliable on put. Against
this baseline, our agent therefore does not show
a higher precondition-satisfaction rate per action
at test time. Its advantage lies in reaching the
goal with fewer actions and in avoidingrepeated
uninformative actions (Table 5), which is the
behavior the penalty directly targets.
Table 6: Actions per episode and precondition satisfac-
tion by action type. ‡Includescloseandlook.
GiGPO Ours
Action Per ep.nSatisfied Per ep.nSatisfied
go to10.24 1311 98.6%7.26929 98.3%
take1.58 202 93.6% 1.43 183 100.0%
put1.38 176 99.4% 1.40 179 92.2%
open0.74 95 98.9% 1.34 171 99.4%
examine0.07 9 66.7% 0.37 47 80.9%
clean0.22 28 100.0% 0.24 31 96.8%
cool0.13 17 100.0% 0.13 17 100.0%
heat0.09 12 100.0% 0.09 11 100.0%
use0.23 30 100.0% 0.11 14 100.0%
All actions‡ 14.71 1883 98.0%12.381584 97.4%
Repeated precondition violations.In
ALFWorld, every action whose preconditions
are not satisfied returns the same fixed observation,
"Nothing happens." (Appendix A.3). The
first violation in an episode therefore adds a
new observation to the state memory and is not
penalized, while every later violation in the same
episode repeats this observation and is penalized.
The penalty is thus not expected to prevent a first,
exploratory violation, but to discourage the agent
from violating preconditionsagainafter it has
already received this feedback. Table 7 measures
this behavior on the same 128 episodes, using the
following definitions:
• Violation:an executed action that is not in the
admissible set of the state in which it is taken, i.e.
an action whose preconditions are not satisfied.
we report violations after the first, which are the
violations which receive the intrinsic penalty.Per
episodedivides their number by the 128 episodes.
• Exact repeat of a failed action:a violation in
which the agent executes the very same action
string that has already failed earlier in the same
episode.
• Share of all violations:the percentage of an
agent’s violations that fall into the given category.
• Back-to-back violations:violations that imme-
diately follow another violation.
• Recovery after a violation:the percentage of
violations whose next action is admissible.
Our agent is less likely to violate preconditions
again once it has received the failure feedback: it
has fewer violations after the first in an episode.
The clearest difference is in exact repeats. About
half of GiGPO’s violations re-execute an action
that has already failed in the same episode, com-
pared with about a quarter of ours. Our agent also
recovers more often, with the action following a vi-
olation more frequently being admissible. This pat-
tern matches the mechanism of the penalty, which
leaves the first violation unpenalized but penalizes
repeating it.
A.2.2 Generalization to Unseen Scenes
We repeat all of the above analyses on the
ALFWorld out-of-distribution split, which contains
scenes not seen during training. Both agents use
the same checkpoints and evaluation settings as
before, and both play the same 128 episodes (74
distinct games). Table 8 summarizes the results,
15

Table 7: Repeated precondition violations (shares of
each agent’s violations).
Metric GiGPO Ours
Violations after the first (total) 2623
per episode 0.200.18
share of all violations 70.3%56.1%
Exact repeats of a failed action (total) 1910
share of all violations 51.4%24.4%
Back-to-back violations 43
Recovery after a violation 88.9%92.5%
Maximum violations in one episode 87
and all metrics follow the definitions given above.
The advantage of our agent grows on unseen
scenes. Its success rate barely changes, while
GiGPO’s drops noticeably, so the gap roughly dou-
bles to about 12 points, and our agent is ahead
on every task type. All information-gathering dif-
ferences persist, mostly with larger margins. Its
failed episodes keep exploring rather than looping,
and it again completes the tasks with fewer actions.
On unseen scenes, it also satisfies preconditions
slightly more often than GiGPO and makes fewer
violations in total.
Table 8: Results on unseen scenes (out-of-distribution
split). †Episodes in which both agents find the target.
Metric GiGPO Ours
Information gathering
Episode length (steps) 17.414.7
Distinct locations visited 4.225.80
Location revisit rate 35.4%22.1%
New-information rate of info. actions 76.7%88.7%
Duplicate-observation rate 20.8%9.4%
Target object found 88.3%97.7%
Steps until target found† 4.964.44
Duplicate-obs. rate in failed episodes 67%25%
Actions and preconditions
Actions per episode 17.414.6
Precondition satisfied (all actions) 96.7%97.3%
take/put/examine94.0 /99.4/ 40.0%98.7/ 94.1 /93.0%
Repeated violations
Violations after the first, per episode 0.380.23
share of all violations 65.8%58.0%
Exact repeats of a failed action (total) 3119
share of all violations 42.5%38.0%
Back-to-back violations1617
Recovery after a violation78.1%64.6%
Maximum violations in one episode 127
A.2.3 Controlled Comparison with the
Penalty Disabled
Here we detail the controlled comparison of
Section 4.5. Both PPO agents start from
Qwen2.5-1.5B-Instruct and share all hyperparam-
eters, prompts and the random seed, so they en-
counter exactly the same training games at every
step. We record all training rollouts (100 episodes
per step) and evaluate both policies on the same
validation episodes every 25 steps, using a single
run per setting.
Exploration during training.Table 9 comple-
ments Figure 3 with further training-rollout metrics
at selected steps. Besides repeating fewer observa-
tions, the penalized agent revisits fewer locations,
obtains new information from a larger share of its
information-gathering actions, and runs into fewer
precondition failures throughout training. The num-
ber of distinct observations per episode eventually
decreases for the penalized agent because it suc-
ceeds more often and its episodes become shorter.
Table 9: Training rollouts with γ= 0 vs. ours, averaged
over the 10 steps ending at each step.
Step 25 Step 50 Step 100
Metricγ= 0Oursγ= 0Oursγ= 0Ours
Duplicate-observation rate 69.6%63.2%66.1%51.5%56.9%40.7%
Distinct observations / episode 14.517.614.721.615.118.8
Location revisit rate 67.4%64.5%65.6%58.9%68.9%49.8%
New-information rate of info. actions 33.0%38.2%37.8%48.8%42.0%59.7%
"Nothing happens."rate 45.7%40.2%44.4%31.1%31.3%20.2%
Cumulative distinct states (k) 28.330.450.465.784.9116.0
Training success 11.4% 11.4%21.3%20.7% 41.9%49.3%
Episode length (steps) 47.1 47.3 44.8 44.8 38.535.2
Validation success 15%19%28%32%45%57%
Test-time behavior of the controlled agents.Ta-
ble 10 extends Table 4 with further metrics, using
the same 128 episodes per split as Tables 5–8. In
addition to the effects discussed in Section 4.5, the
penalized agent completes episodes with fewer ac-
tions, wins far more of the games that only one of
the two agents solves, satisfies preconditions more
often for almost every action type, and its failed
episodes contain less repetition. At this stage of
training, both agents still violate preconditions of-
ten, so absolute rates are lower than for the fully
trained agent in Tables 5–8.
Table 10: Test-time behavior of the controlled agents
after 100 training steps.
Seen scenes Unseen scenes
Metricγ= 0Oursγ= 0Ours
Success rate 39.1%57.8%34.4%52.3%
Episode length (steps) 37.931.040.532.7
Actions per episode 33.830.334.432.1
Distinct locations visited 4.686.174.876.88
Location revisit rate 68.6%41.3%68.7%42.3%
New-information rate of info. actions 43.5%67.4%40.4%67.1%
Duplicate-observation rate 59.3%37.0%61.8%36.6%
Target object found 76.6%87.5%64.8%85.9%
Duplicate-obs. rate in failed episodes 72%56%72%57%
Precondition satisfied (all actions) 68.0%82.4%67.8%81.9%
Violations after the first, per episode 9.874.6510.125.09
Exact repeats, share of all violations 62.5%55.4%61.7%54.1%
Recovery after a violation 47.2%59.9%50.8%64.2%
A.2.4 Relation to Theory and Qualitative
Example
Relation to Proposition 2.Proposition 2 bounds
the visitation entropy H(P L) of an episode by its
number of duplicate observations D. Figure 4 plots
16

both quantities for all full-length episodes of the
controlled agents. Every episode of both agents lies
between the two bounds, and across all episodes,
entropy decreases almost monotonically with the
number of duplicates (rank correlation close to−1).
The penalized agent produces episodes with clearly
fewer duplicates and correspondingly higher visita-
tion entropy, both in failed full-length episodes and
on average over all episodes, where the paired con-
fidence interval of the entropy difference excludes
zero on both splits. This confirms empirically that
minimizing the cumulative penalty, i.e. the num-
ber of duplicate observations, translates into higher
visitation entropy in practice.
0 10 20 30 40 50
Duplicate observations D (episodes with L = 51 observations)
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
4.0
Visitation entropy H(PL)
upper bound log(L D)
lower bound
no penalty ( = 0)
penalty ( = 1/40)
Figure 4: Visitation entropy H(P L) against the number
of duplicate observations D for all full-length episodes
(L= 51 observations) of the controlled agents after
100 training steps, seen and unseen splits combined.
The dotted and dashed curves are the upper and lower
bounds of Proposition 2.
Qualitative example.Figure 5 shows the two
controlled agents on the same game from the un-
seen split, taken directly from the evaluation logs.
Both agents start identically and pick up the mug.
The agent trained without the penalty then repeat-
edly issues a command for the location it is already
at, receives "Nothing happens." over and over,
and never cools the mug before the step budget
runs out. The penalized agent instead proceeds to
the fridge, cools the mug and completes the task
in eight steps. This is the looping failure mode of
Figure 1, which the penalty removes.
Task: cool some mug and put it in coffeemachine (unseen scene).
Penalty(γ= 1 40 ): success in 8 steps 1go to sinkbasin 1arrive; sinkbasin empty
2go to countertop 1arrive; see mug 1
3take mug 1 from countertop 1pick up mug 1
4go to fridge 1arrive; fridge closed
5–6cool mug 1 with fridge 1cool mug 1
7go to coffeemachine 1arrive
8move mug 1 to coffeemachine 1task completed
No penalty(γ= 0): failure after 50 steps
1–3 same as above (mug 1 picked up)
4go to sinkbasin 1arrive
5–7go to sinkbasin 1(×3)"Nothing happens."
8–9go to fridge 1,open fridge 1fridge open
10go to sinkbasin 1arrive
11–21go to sinkbasin 1(×11)"Nothing happens."
22–50 moves the mug around; 17 more"Nothing happens.";
the mug is never cooled; step budget exhausted
Figure 5: The two controlled agents after 100 training
steps on the same unseen game (actions and observa-
tions from the evaluation logs, abridged). In total, 31
of the 50 steps of the agent without the penalty return
"Nothing happens.".
A.2.5 Additional Qualitative Results
In Figure 6, we further show some of the example
outputs of the LLM agent trained with intrinsic
productive exploration rewards framework.
A.3 Reproducibility Details
Penalty weight γ and reward weight λ. γ=
1/10 destabilized training; γ= 1/100 matched the
baseline; γ= 1/40 (used throughout) gave a clear,
consistent improvement.
Prompts.Shown in Figure 7.
Invalid actions:The two environments signal in-
valid actions differently. In ALFWorld, every action
whose preconditions are not satisfied returns the
fixed observation "Nothing happens." , and we
count a step as invalid when its observation matches
this string or when the agent’s output contains no
well-formed action. WebShop provides no failure
message: an action that is not available on the cur-
rent page, such as clicking an element that is not
displayed, is ignored, and the environment returns
the unchanged page. For WebShop, we therefore
count a step as invalid when the agent’s output con-
tains no well-formed action. Because an ignored
action returns the same page, it always produces
a duplicate observation and is penalized by our
intrinsic reward.
Rollout and optimization settings.Batch size,
rollouts/step, PPO epochs, clip range, and learn-
ing rate are unmodifiedverl-agent/GiGPO de-
faults (Feng et al., 2025). Details are mentioned in
17

Table 11.
Table 11: Training hyperparameters.
Hyperparameter Value
Batch size 256
Rollouts per step 128
PPO clip range 0.2
Learning rate 1e-6
Training steps 300
Max steps (ALFWorld) 50
Max steps (WebShop) 15
γ(intrinsic penalty)1/40×success reward
Train/test splits.We use the standard ALFWorld
seen/unseen split released by Shridhar et al. (2020)
and the standard WebShop train/eval split released
by Yao et al. (2022).
A.4 Declaration
We have cited the models and code used in Sec-
tion 4. We have used ChatGPT, Gemini, and
Claude to assist with polishing writing.
18

Figure 6: Additional example outputs of the multi-turn interaction of the LLM agent on the ALFWorld dataset after
training with conditional state-space exploration with intrinsic rewards.
19

Figure 7: Prompts used for bothALFWorldandWebShopenvironments.
20
