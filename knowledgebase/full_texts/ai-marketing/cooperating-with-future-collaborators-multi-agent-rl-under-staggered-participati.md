---
title: 'Cooperating with Future Collaborators: Multi-Agent RL under Staggered Participation'
url: https://arxiv.org/abs/2610.07578
category: ai-marketing
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Jianglin Qiao
- Siyi Hu
- Thien Hoang Nguyen
- Zehong Cao
- Salah Sukkarieh
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.07578
pages: 43
chars: 122855
fetched_at: '2026-11-08T13:31:50+00:00'
kb_version: 1
---

# Cooperating with Future Collaborators: Multi-Agent RL under Staggered Participation

Preprint
Cooperating with Future Collaborators:
Multi-Agent RL under Staggered Participation
Jianglin Qiao1 Siyi Hu2 Thien Hoang Nguyen1 Zehong Cao3 Salah Sukkarieh1
1ACFR, The University of Sydney, Sydney, Australia
2School of EECMS, Curtin University, Bentley, Australia
3School of CSIT, Adelaide University, Adelaide, Australia
{jianglin.qiao,thienhoang.nguyen,salah.sukkarieh}@sydney.edu.au
siyi.hu@curtin.edu.au jimmy.cao@adelaide.edu.au
In cooperative Multi-Agent Reinforcement Learning (MARL), agents are often trained under concurrent
participation, while in many tasks some agents act earlier and leave task-relevant information that
becomes useful to agents participating later. We study this setting asstaggered participation(SP), which
introduces a cross-time, cross-agent learning dependency because an early action may affect the return
through the information it provides and the later policy that uses it. Learning under SP therefore requires
both identifying what information is useful for future decisions and learning how later agents should
use it. We proposeStaggered Participation Learning(SPL), a training-time augmentation that addresses
these two parts withprospective acquisition supervisionfor earlier agents andoutcome-supervised receiver
learningfor later agents. We evaluate SPL across multiple policy-based MARL backbones, environments,
and staggered-participation patterns. Across 60 MPE/RWARE backbone setting comparisons, SPL
achieves higher observed mean task completion in every case, with an average difference of 14.1%.
The gains also extend to eight-agent teams and a physics-based UAV–UGV environment in Isaac Lab,
providing evidence across algorithmic, temporal, and embodied settings.
Keywords: Multi-Agent RL, Staggered Participation, Cooperative Tasks
1. Introduction
Cooperative agents do not always participate over the same time interval. For instance, in multi-robot
systems, one agent may begin sensing or exploration earlier, while another becomes active later for
navigation or task execution [1–3]. Their participation windows may partially overlap, allowing direct
interaction for some time steps, or they may be fully separated. In these cases, earlier agents can
acquire or leave task-relevant information that remains useful to agents participating later. We study
this temporal structure asstaggered participation(SP), where agents contribute to the same cooperative
objective over temporally offset participation windows. As illustrated in Fig. 1, these windows may
partially overlap or be fully separated, while earlier participants can leave task-relevant information
that supports later decisions.
Learning under SP is challenging in cooperative MARL because the effect of an early action may only
become visible through the behavior of an agent acting later. An earlier agent may take an action that
acquires or reveals information for downstream decisions, but the usefulness of that action depends on
how the resulting information affects later behavior. The return therefore links decisions across both
time and participants. When participation windows overlap, this dependency can coexist with direct
interaction; when they are disjoint, it is carried through information and other consequences of earlier
actions. This gives rise to two interdependent learning requirements:(i) Information Acquisition, where
earlier agents learn which actions provide useful information for later decisions, and(ii) Downstream
1
arXiv:2610.07578v1  [cs.AI]  6 Oct 2026

Cooperating with Future Collaborators: Multi-Agent RL under Staggered Participation
Figure1: Simultaneous and staggered participation. In simultaneous participation, agents contribute within
the same participation period. Under staggered participation, earlier participants acquire or leave information
that remains available to future collaborators and supports later decisions. Participation windows may partially
overlap or be fully separated.
Utilization, where later agents learn how that information should influence action selection. Although
a shared team return couples the two roles through a common objective, it does not provide separate
supervision for acquiring useful evidence and using it effectively downstream.
SP is closely related to three existing directions in cooperative MARL. First, asynchronous MARL studies
agents that act or communicate at different times [4–6]. Second, dynamic and open-team MARL
considers agents that join, leave, or interact with changing teammates [7–9]. Third, communication
MARL learns what information is useful for decision-making. Our focus is the learning dependency
that appears when information acquisition and downstream utilization are distributed across different
participation windows and potentially different agents. SP therefore places these two components
within the same cooperative learning problem.
We introduce Staggered Participation Learning (SPL), a training-time augmentation that provides com-
plementary supervision for the two learning requirements under SP.Prospective acquisition supervision
guides earlier agents toward actions that provide useful information for future collaborators, while
outcome-supervised receiver learningtrains later agents to use inherited evidence based on downstream
outcomes. SPL augments actor training without modifying environment rewards and introduces
no additional communication or auxiliary inference at execution. We evaluate SPL across multiple
policy-based MARL backbones, participation patterns, larger teams, and a physics-based UAV–UGV
setting. Across the 60 primary Vanilla–SPL comparisons, SPL achieves higher observed mean task
completion in every configuration, with an average gain of 14.1%. Our contributions are: (i)Staggered
participation.We formulate cooperative MARL with temporally offset participation and identify the
dependency between evidence acquisition and downstream utilization; (ii)Staggered Participation
Learning.We introduce complementary supervision for prospective acquisition and outcome-informed
evidence use while preserving the underlying reward and decentralized execution; and (iii)Empirical
evaluation.We evaluate SPL across policy-based MARL backbones, temporal participation patterns,
larger teams, and physics-based UAV–UGV simulation.
2. Related Work
Simultaneous vs. Staggered Participation in Cooperative MARL.In simultaneous participation,
agents contribute within the same interaction period. Cooperative MARL also studies temporal vari-
ation through asynchronous interaction, dynamic team composition, and staged decision making.
Asynchronous methods consider agents that execute actions, communicate, or assign credit across
2

Cooperating with Future Collaborators: Multi-Agent RL under Staggered Participation
asynchronous interactions [4–6, 10, 11], while dynamic and open-team approaches address agents that
join, leave, or interact with changing teammates [7–9, 12]. Cooperative Consecutive Policies studies
cooperation across consecutive decision stages [13]. These directions examine different aspects of
when agents act and participate in a cooperative task. SP concerns temporally offset participation win-
dows, which may partially overlap or be fully separated. In the tasks studied here, earlier participants
can acquire task-relevant evidence before future collaborators begin participating, and this evidence
remains available to support downstream decisions.
Direct vs. Indirect Communication Protocols in Cooperative MARL.Communication methods
support direct information exchange and learn what to send and with whom to communicate, including
under intermittent connectivity [14–19]. Cooperation can also occur indirectly through persistent
environmental traces or another agent’s subsequent actions. Stigmergic methods support coordination
through such environmental traces [20], while MAE-MAPPO addresses indirect cooperation with
invisible collaborators through marginal advantage estimation [21]. Related methods provide com-
plementary mechanisms for retaining and interpreting information: sequence-based methods retain
long-horizon context [22], while SMPE2 and MA2E model or reconstruct information unavailable
from local observations [23, 24]. Policy distillation transfers training-time coordination knowledge
into decentralized policies [25, 26]. Informative sensing and Dec-POMDP approaches further guide
information acquisition according to its expected decision value [27–29]. The form of SP studied here
combines temporally offset participation with indirect cooperation through persistent task-relevant
evidence. Within this setting, SPL focuses on evidence acquisition and downstream utilization, while
related credit-assignment methods study how cooperative outcomes are attributed across agents or
coalitions [21, 30]. SPL builds on value-aware information acquisition and policy distillation to su-
pervise earlier participants and learn receiver preferences from attributable downstream outcomes.
Persistent evidence connects the two roles without requiring additional execution-time communication.
3. Methodology
3.1. Staggered Participation (SP)
Cooperative decision process.We model the cooperative task as a decentralized partially observable
Markov decision process (Dec-POMDP) [31], defined by M=⟨N,S,{O i}i∈N ,{U i}i∈N ,P,R,γ⟩ ,
where N={1, . . . ,N} is the set of agents andS is the global state space. At timet, the environment
is in statest ∈ Sand agent i receives a local observationoi t ∈ Oi. Each agent maintains an action–
observation historyτi t and selects an actionui t ∈ Ui according toπθi (ui t |τ i t ,M i t), where Mi t denotes the
legal-action mask. The joint actionut = (u1 t , . . . ,u N t ) produces the shared rewardrt =R(s t,u t) and
the next state is sampled according tost+1 ∼P(· |st,u t). All agents optimize the common discounted
team returnG= ∑︀T−1 t=0 γtrt.
Staggered participation.Agents may participate over different temporal intervals, so teammates
need not be active throughout the same period. LetN part t ⊆ Ndenote the set of agents participating
at time t; agents outside this set take a null action and make no policy decision. For each agenti, let
[tstart i ,t end i ) denote its participation interval, wheretstart i is the first participating time andtend i is the
exclusive end time. We call agentj afuture collaboratorof agent i if tstart i <t start j and both contribute to
the same cooperative objective. Their participation intervals may be disjoint, withtend i ≤t start j , or may
partially overlap, withtstart j <t end i . In both cases, agentican act before agentjbegins participating.
3

Cooperating with Future Collaborators: Multi-Agent RL under Staggered Participation
Figure2: Overview of SP and SPL. Earlier participants receive prospective acquisition supervision, while future
collaborators learn evidence-conditioned preferences from downstream outcomes. SPL is used only during
training.
Learning problem under SPEarlier information-gathering actions can change the evidence available
to future collaborators and thereby influence downstream decisions and the shared return. This creates
two interdependent learning requirements: what evidence earlier participants should acquire and how
future collaborators should use it. Because the effect of an earlier action is realized through persistent
evidence and subsequent decisions by another policy, its learning signal is delayed and indirect. We
therefore focus on improving both evidence preparation and downstream evidence use. The next
subsection introduces SPL to support these two requirements.
3.2. Staggered Participation Learning (SPL)
Under SP, earlier participants and future collaborators are coupled through persistent task-relevant
evidence. SPL augments the native cooperative MARL objective with two complementary actor-side
trainingsignals.Prospectiveacquisitionsupervisionguidesearlierparticipantstowardevidence-gathering
actions expected to support future decisions, whileoutcome-supervised receiver learningteaches future
collaborators how inherited evidence should influence downstream action selection. Both augment
native actor training while leaving the environment reward and backbone critic objective unchanged,
as illustrated inFig. 2.
Structured training supervision.SPL uses structured task knowledge available during training to
construct its auxiliary targets. Prospective acquisition supervision uses task-family validity priors, the
fixed valid-task constraint, and the probe observation model to estimate the downstream value of
candidate evidence-gathering actions. Receiver supervision uses fixed task-level utilities for successful
and unsuccessful execution, while candidate-specific success probabilities are learned from attributable
outcomes observed during training. These quantities describe task-generation, sensing, and outcome
semantics; they do not reveal realized task validity, future outcomes, or a predefined correct action. In
particular, the fixed acquisition model does not provide receiver success probabilities. The acquisition
and receiver objectives are complementary but separately constructed: the acquisition target is fixed
by the structured task model and is not updated from the learned receiver policy or outcome model.
SPL therefore assumes that such task structure is available from the training environment or task
4

Cooperating with Future Collaborators: Multi-Agent RL under Staggered Participation
specification. All SPL-specific models and targets remain training-only and are unavailable during
execution. Implementation details are provided inAppendix B.4.
3.2.1. Prospective Acquisition Supervision
Prospective evidence value.Consider an eligible evidence-acquisition decision of an earlier partici-
pant i. Let ci t denote its actor-visible acquisition context andMi t the corresponding legal-action mask.
For each legal task-directed actionu, SPL uses a fixed training-time task model to estimate∆i t(u), the
expected increase in downstream decision value associated with the evidence produced by that action.
SPL combines this prospective value with the corresponding travel or acquisition distancedi t(u):
si t(u) =log (︁ max{∆i t(u),ϵ acq} )︁ − di t(u) τd ,(1)
where τd isafixeddistancetemperatureand ϵacq >0 isanumericalstabilizer. Adeterministictransform
Tacq masks illegal actions, normalizes the scores of positive-gain task actions, and reserves a small
fixed probability mass for the scan action, which gathers local evidence without targeting a specific
candidate. If no positive-gain task action is available, the scan action receives all target mass. The
resulting prospective acquisition target isqi acq =T acq(si t,M i t).
Acquisition policy supervision.For eligible earlier-participant decisionsDacq, SPL distils the prospec-
tive acquisition target into the decentralized policy:
Lacq SPL =E (i,t)∼D acq
[︁
CE
(︁
qi acq,π θi (· |τi t ,M i t) )︁]︁ .(2)
This auxiliary loss updates only the earlier-participant actor.
3.2.2. Outcome-Supervised Receiver Learning
Outcome-labeled decisions.Consider a future collaborator j making a downstream decision at time
t≥t start j . Let xj t denote the actor-visible information available before the decision, including retained
task-relevant evidence and the collaborator’s current local context. The collaborator selectsuj t using its
decentralized policy, and the selected task subsequently produces an attributable outcomeyj t ∈ {0, 1},
where yj t =1 denotes successful completion andyj t =0 an attributable unsuccessful attempt. Each
eligibledecisioncontributesatuple (x j t,u j t,j,y j t)totheoutcomereplayset Dout. Subsequentobservations
are used only to determine the outcome label; we exclude interrupted, expired, or unresolved attempts
when their outcomes cannot be reliably attributed.
Candidate outcome model.SPL learns how the evidence and local context available to a future
collaborator relate to the outcome of each candidate action. Letgj(x,u) collect the actor-visible decision
context, candidate-action features, and collaborator-role identity. A candidate-shared scorerfψ predicts
p j ψ(u|x) =sigmoid (︀ fψ (︀ gj(x,u) )︀)︀ ,(3)
wherep j ψ(u|x)estimates the probability that candidateusucceeds under informationx. The model
is trained from attributable outcomes using binary cross-entropy,
Lout(ψ) =E(x,u,j,y)∼D out
[︁
ℓBCE
(︁
y,p j ψ(u|x) )︁]︁ .(4)
The outcome model is therefore learned from the observed consequences of the future collaborator’s
own selected actions. It receives no labels identifying which candidate action should have been selected.
5

Cooperating with Future Collaborators: Multi-Agent RL under Staggered Participation
Evidence-conditioned action utility.Outcome probability alone does not determine the desirability
of a candidate when successful and unsuccessful executions have different task-level consequences.
Let c+ j (u) and c− j (u) denote fixed task-level utilities associated with successful and unsuccessful
execution of candidateu, respectively. SPL combines these utilities with the evidence-conditioned
success probability predicted by a slowly updated target outcome model with parameters¯ψ:
U j ¯ψ(u|x) =p j ¯ψ(u|x)c + j (u) + [︁ 1−p j ¯ψ(u|x) ]︁ c− j (u).(5)
Because p j ¯ψ(u|x) is conditioned on decision-time information, the same candidate can receive different
utility estimates under different evidence prepared by earlier participants.
Receiver target and policy supervision.Let Aj t ={u∈ Uj :M j t(u) =1} denote the legal actions
available to collaboratorj. SPL standardizes the predicted utilities over this set and constructs a soft
preference target:
zj t(u) = U j ¯ψ(u|x j t)−µ j t √︁
(σ j t )2 +ϵ z
,q j SPL(u) = exp(βz j t(u)) ∑︀
v∈A j t exp(βz j t(v)) ,(6)
where µj t and (σ j t )2 are the mean and variance of the legal-action utilities,ϵz >0 is a variance stabilizer,
and β>0 controls the strength of the induced preference. Illegal actions receive zero probability. Since
the target is constructed from learned evidence-conditioned outcome predictions, it expresses relative
preferences among the currently legal actions and does not require predefined correct-action labels.
For eligible future-collaborator decision pointsDrec, SPL distills this soft target into the decentralized
policy:
Lrec SPL =E (j,t)∼D rec
[︁
CE
(︁
qj SPL,π θj (· |τj t ,M j t) )︁]︁ .(7)
Thetargetistreatedasfixedduringthisupdate. Gradientsthereforemodifyonlythefuture-collaborator
actor and do not propagate through the outcome model, recorded outcomes, or environment dynamics.
TrainingandExecution.SPLcombines Lacq SPL forearlierparticipantswith Lrec SPL forfuturecollaborators,
while the MARL backbone continues to optimize its native objective from the shared team return.
After each rollout, attributable outcomes are added toDout and used to update the outcome model
once replay-readiness conditions are met; the target parameters are updated by¯ψ←(1−ρ) ¯ψ+ρψ .
SPL actor updates are interleaved with native actor optimization, while critic optimization follows
the original backbone procedure. During execution, agents act solely throughui t ∼π θi (· |τi t ,M i t); no
acquisition model, auxiliary target, outcome replay, outcome model, or utility estimate is required.
We provide detailed readiness conditions, update ordering, gradient boundaries, and the complete
training algorithm inAppendices B.6 and B.7.
3.3. Theoretical Analysis
We provide a local analysis of the auxiliary objectives introduced by SPL. The results characterize the
prospective acquisition target, calibration of the outcome-based receiver model, and local decision
quality induced by the receiver target under the structured task assumptions of Sec. 3.2. The acquisition
result instantiates a standard value-of-information argument for the top-k surrogate used by SPL, while
the receiver results characterize calibration and distillation errors. Together, these results support
6

Cooperating with Future Collaborators: Multi-Agent RL under Staggered Participation
the construction of the SPL training signals but do not form an end-to-end guarantee or establish
global convergence of the cooperative return. Full proofs, assumptions, and guarantee boundaries are
provided inAppendix A.
Prospective acquisition.Consider task families represented by the fixed binary-validity model used
to construct acquisition supervision. Letb= (b1, . . . ,b n) denote posterior validity marginals under this
model, wherebr =Pr(W r =1|c i t). If a future collaborator can execute at mostk tasks, define the top-k
posterior completion value asVk(b) =maxS:|S|≤k
∑︀
r∈S br. For a purely informational acquisition action
u, let Zu denote the resulting observation andbZu the updated posterior. Its model-relative prospective
gain is ∆i t(u) =E[Vk(bZu )|c i t,u]−V k(b). Let P i t ={u:M i t(u) =1,uis task-directed,∆ i t(u)>0}
denote the legal task-directed actions with positive prospective gain.
Proposition 1(Prospective acquisition target).Assume that acquisition actions change only the available
information and that posterior updating and predictive expectation are Bayesian-consistent under the
acquisition model. Then∆i t(u)≥0 for every legal acquisition action. Moreover, before adding the scan
mass, if Tacq applies Gibbs normalization overP i t, the acquisition target satisfiesqi acq(u)∝exp(s i t(u))
and uniquely maximizes the corresponding entropy-regularized score objective.
Proof sketch.The top- k value Vk is the maximum of linear functions of the posterior marginals
and is therefore convex. Bayesian consistency givesE[bZu |c i t,u] =b, so Jensen’s inequality implies
E[Vk(bZu )|c i t,u]≥V k(b). TheGibbsformfollowsfromthestandardentropy-regularizedmaximization
problem. The full proof is provided inAppendix A.2.
Outcome prediction and local utility.For an attributable future-collaborator decision, letY∈ {0, 1}
denote its downstream outcome and letC∈ {0, 1} indicate whether that outcome is retained in
Dout. We define p j ∗(u|x) =Pr(Y=1|X=x,U=u,J=j,C=1) , with corresponding local
utility U j ∗(u|x) =p j ∗(u|x)c + j (u) + [1−pj ∗(u|x)]c − j (u). For any predictorp, letLout(p) denote its
population binary-cross-entropy risk over retained outcomes andUj p the induced local utility.
Proposition 2(Retained-outcome calibration).On the covered retained-outcome support,Lout(p) is
uniquely minimized pointwise bypj ∗. IfC ∆ =sup u,j |c+ j (u)−c − j (u)|<∞, then
E
[︂(︁
U J p(U|X)−U J ∗(U|X) )︁2 |C=1 ]︂ ≤ C2 ∆ 2 [Lout(p)− Lout(p ∗)] .(8)
Proof sketch.Excess binary-cross-entropy risk equals the Bernoulli KL divergence on the retained-
outcome distribution. Since U j p −U j ∗ = (pj −p j ∗)(c+ j −c − j ), Pinsker’s inequality gives Eq. 8. The
result applies to retained, selected receiver actions and is conditional onC=1 ; an unconditional
interpretation additionally requiresY⊥C|X,U,J. The full proof is provided inAppendix A.3.
Receiver decision quality.Fix an eligible future-collaborator decision with legal action setA and
K=|A| . Let z∗ denote the reference standardized score andz ¯ψ the score produced by the target
outcome model. Defineδ=∥z ¯ψ −z ∗∥∞,R z =max u∈A z∗(u)−min u∈A z∗(u), and
η=KL(q j SPL∥π j t) =CE(qj SPL,π j t)−H(q j SPL),
7

Cooperating with Future Collaborators: Multi-Agent RL under Staggered Participation
Figure3: Evaluation environments and temporal participation patterns. (a) MPE, (b) RWARE, (c) the physics-
based UAV–UGV environment in Isaac Lab, and (d) the five participation patterns used in MPE and RWARE.
where qj SPL(u)∝exp(βz ¯ψ(u)). Thus, η is directly measurable from the receiver target and actor
distributions. The score errorδ additionally depends on generalization across the full legal action
set and score standardization; controlling it from outcome-model error requires stronger coverage
conditions.
Theorem 1(Local receiver score regret).For any legal receiver policyπj t satisfyingKL(q j SPL∥π j t)<∞,
Regj z,t(π j t)≤ logK β +2δ+R z
√︂
η
2 ,(9)
whereReg j z,t(π j t) =maxu∈A z∗(u)−E u∼π j t [z∗(u)].
Proof sketch.The Boltzmann target contributes a softness gap of at mostlogK/β . Replacing z ¯ψ with
z∗ contributes at most2δ, and Pinsker’s inequality bounds the remaining distillation error byRz
√︀
η/2.
The three terms therefore capture finite-temperature softness, score approximation, and incomplete
receiver distillation. The full proof is provided inAppendix A.5.
Scope.The results characterize local components of SPL under the structured training assumptions
ofSec. 3.2.Proposition 1gives a model-relative information-value guarantee: internally consistent
Bayesian updating preserves non-negative prospective gain, but misspecified priors can change how
this gain relates to performance under the true environment distribution; this sensitivity is evaluated
inAppendix D.6.Proposition 2controls expected local-utility error on the retained selected-action
distribution.Theorem 1separates the measurable distillation errorη from the score-approximation
term δ and bounds standardized local-score regret, not raw utility or full team return. Relatingδ
directly to outcome-model training requires stronger coverage and generalization assumptions across
legal actions.
4. Experimental Setup
Environments.We evaluate SPL in MPE, RWARE, and a physics-based UAV–UGV environment, where
earlier participants gather task-relevant evidence before future collaborators perform downstream
tasks. MPE-Base builds on the Multi-Agent Particle Environment [32], while MPE-Advanced further
randomizes task assignments, spawn positions, and future-collaborator identities. RWARE-Base trans-
fers the same evidence-mediated cooperation problem to the Multi-Robot Warehouse domain [33],
and RWARE-Advanced additionally introduces task permutation, a shared candidate pool, and dy-
namic task claims. Isaac Lab [34] provides an embodied UAV–UGV setting with physical motion and
8

Cooperating with Future Collaborators: Multi-Agent RL under Staggered Participation
25
50
75
90
100 Non-overlap
MPE-Base
Overlap-25 Overlap-50 Dynamic Cascaded
25
50
75
90
100
MPE-Advanced
25
50
75
90
100
RWARE-Base
0 1 2
15
25
50
75
90
100
RWARE-Advanced
0 1 2 0 1 2 0 1 2 0 1 2
Environment Steps (×106)
Task Completion (%)
IPPO SPL-IPPO MAPPO SPL-MAPPO HAPPO SPL-HAPPO MAE-MAPPO Sable SMPE²
Figure4: Training TC (%) for all methods across 4 environments and 5 participation patterns averaged over 5
training seeds.
obstacle constraints. Full environment specifications are given inAppendices B.1–B.3. For MPE and
RWARE, we evaluate five patterns:Non-overlap, with a strict handoff between roles;Overlap-25and
Overlap-50, with fixed temporal overlap;Dynamic, with stochastic pair-specific handoff times; and
Cascaded, with successive participation intervals. Isaac Lab uses corresponding UAV–UGV schedules.
Exact participation windows are provided inAppendices B.2–B.3.
ImplementationWe augment three PPO-based MARL backbones—IPPO, MAPPO, and HAPPO—to ob-
tain SPL-IPPO, SPL-MAPPO, and SPL-HAPPO. MAPPO [35] is the primary backbone, while HAPPO [36]
and IPPO [37] test compatibility with heterogeneous and independent learning, respectively. We
additionally compare with MAE-MAPPO [21], Sable [22], and SMPE2 [23] as complementary cross-
method references. The primary controlled comparisons remain between each Vanilla backbone and
its SPL-augmented counterpart. Baseline adaptations and implementation details are provided in
Appendix B.5. Our implementation builds on HARL [38]. SPL preserves the native actor–critic archi-
tecture and training objective of each backbone and adds only role-specific auxiliary actor updates
during training; SPL-specific models are not required during execution. Optimization details, training
procedures, and observed training costs are reported inAppendices B–C.
Evaluation.Task completion (TC) is the primary metric. The four-agent MPE/RWARE experiments
use five independent training seeds per method and configuration, while the eight-agent and Isaac Lab
evaluations use three; all final evaluations contain 200 episodes per seed. Results are reported as mean
± standard error across training seeds. Throughout the results, reported TC gains denote absolute
differences between percentage-valued TC scores and are written using %. The primary Vanilla–SPL
comparisons are additionally examined using paired seed-level analyses where same-seed pairing
is available; complete confidence intervals, Holm-adjusted tests, and pairing details are reported in
Appendix D.7. Additional metrics, including full success, return, failed execution, and exploration
diagnostics, are reported inAppendix D. All configurations are trained and evaluated independently,
9

Cooperating with Future Collaborators: Multi-Agent RL under Staggered Participation
Table 1: Final task completion (TC, %) after 2M environment steps. Values are mean± standard error over five
training seeds. SPL columns are shaded; bold indicates the highest observed mean in each setting and does not
denote statistical significance.
Environment Participation IPPO MAPPO HAPPO Other baselines
Van. SPL Van. SPL Van. SPL MAE-MAPPO Sable SMPE 2
MPE-Base
Non-overlap70.50±0.00 78.38±0.38 70.50±0.00 78.73±0.43 67.45±3.05 79.18±0.2370.50±0.00 62.70±0.25 42.73±9.29
Overlap-2568.25±2.75 79.35±0.57 70.78±0.14 80.25±0.21 70.70±0.18 80.35±0.2967.93±2.95 63.50±2.24 53.85±5.43
Overlap-5067.85±3.15 78.90±0.3169.53±1.27 78.90±0.2469.80±0.92 78.50±0.47 70.63±0.23 64.43±1.85 63.95±3.34
Dynamic66.20±3.01 79.65±0.1870.23±0.59 78.88±0.18 69.53±0.99 79.63±0.39 64.85±3.06 58.30±1.11 49.70±1.04
Cascaded66.83±3.68 78.90±0.70 70.63±0.10 78.93±0.4870.68±0.19 78.78±0.22 70.45±0.05 38.03±0.93 27.93±5.74
MPE-Advanced
Non-overlap70.38±0.00 77.95±0.19 64.08±3.86 78.23±0.1667.28±3.10 78.03±0.16 63.28±3.47 64.90±1.36 49.78±3.25
Overlap-2565.65±3.53 79.95±0.5268.28±1.50 79.38±0.27 70.93±0.56 79.55±0.40 71.40±0.23 64.30±1.63 47.83±9.02
Overlap-5071.30±0.22 78.63±0.23 68.58±3.05 78.33±0.40 71.40±0.14 78.68±0.2562.63±5.92 61.88±1.48 52.08±8.25
Dynamic66.63±3.66 78.23±0.29 67.05±3.20 79.08±0.5461.73±5.55 78.80±0.18 67.68±1.76 57.60±1.30 43.10±6.61
Cascaded67.68±2.58 76.80±0.13 67.28±3.10 77.00±0.33 69.28±1.10 77.23±0.1866.83±3.02 62.73±0.98 56.70±5.50
RWARE-Base
Non-overlap66.45±5.86 86.83±0.40 71.38±2.27 86.70±0.49 73.18±1.50 86.93±0.2673.48±1.69 71.80±0.98 66.05±3.29
Overlap-2581.10±3.41 89.15±0.1674.25±3.41 89.08±0.35 70.15±2.93 88.35±0.50 72.50±2.86 76.70±1.18 67.28±2.87
Overlap-5082.00±1.12 89.00±0.1974.73±3.35 88.58±0.28 70.28±2.41 88.80±0.23 77.53±0.72 77.23±1.97 61.95±4.09
Dynamic72.88±1.19 88.88±0.2765.35±5.46 88.70±0.30 68.80±4.06 88.40±0.42 72.28±1.51 74.63±1.22 62.03±4.29
Cascaded66.80±1.98 86.25±0.38 67.53±2.05 86.75±0.5066.58±2.24 85.95±0.79 71.63±0.73 76.83±0.93 64.18±2.94
RWARE-Advanced
Non-overlap52.08±1.37 79.93±0.59 58.63±2.31 80.03±0.2357.58±3.44 79.55±0.79 58.50±2.20 50.70±0.32 45.70±0.25
Overlap-2564.18±1.62 83.23±0.47 68.83±1.40 83.65±0.32 63.28±1.98 83.73±0.4864.70±1.81 54.75±0.44 47.68±0.66
Overlap-5070.35±1.28 84.55±0.6968.05±4.14 84.45±0.33 67.50±2.12 84.43±0.56 72.88±1.05 58.88±0.77 47.05±0.38
Dynamic66.60±1.95 81.30±0.34 62.55±2.83 82.50±0.4363.23±0.83 82.20±0.16 65.90±2.33 56.30±0.49 47.55±0.40
Cascaded58.95±1.70 85.40±0.42 65.55±1.76 85.98±0.4466.03±2.06 84.90±0.51 64.18±3.98 54.90±1.08 47.03±0.55
so the reported results characterize within-configuration performance rather than transfer across
participation patterns or task structures.
5. Results
5.1. Main Results
Fig. 4shows the training task-completion trajectories across the four environments and five partici-
pation patterns. In most settings, the SPL variants reach a higher task-completion regime than their
corresponding Vanilla backbones and maintain this difference through 2M environment steps. Al-
though the Vanilla IPPO, MAPPO, and HAPPO trajectories differ, their SPL counterparts often converge
to similar final performance, suggesting that the observed improvement is not specific to a single
PPO-based actor–critic backbone.Table 1reports the final results for the 60 primary Vanilla–SPL
comparisons. SPL achieves higher observed mean TC in every configuration, with an equal-weight
descriptive mean difference of 14.09%. The corresponding mean differences are 13.93%, 14.02%, and
14.33% for IPPO, MAPPO, and HAPPO, respectively. Among the 57 configurations with paired inference,
56 pointwise 95% confidence intervals have positive lower bounds, and 29 remain significant after
Holm correction over the declared family of 60 comparisons at a familywise level of 0.05. Complete
statistical results are reported inAppendix D.7, while full TC, FS, return, and FE results are provided
inAppendices D.1–D.4.
Participation structure affects the magnitude of the observed improvement. Averaged across envi-
ronments and backbones, SPL improves task completion by 15.1% under Non-overlap, 13.3% under
Overlap-25, 11.7% under Overlap-50, 15.5% under Dynamic, and 14.9% under Cascaded participation.
Across the fixed Non-overlap, Overlap-25, and Overlap-50 schedules, the average gain decreases as
cross-role concurrency increases. Since the exact temporal constructions differ between MPE and
RWARE, we treat this pattern as descriptive and do not interpret it as a controlled effect of overlap.
The positive gains under both overlap settings nevertheless show that SPL does not require a strictly
10

Cooperating with Future Collaborators: Multi-Agent RL under Staggered Participation
Table 2: Task completion (%) for eight-agent scaling and physics-based UAV–UGV evaluations using MAPPO.
MPE-Advanced (8) RWARE-Advanced (8)
Participation Vanilla SPL Vanilla SPL
Non-overlap64.21±0.61 77.77±0.3041.10±2.66 74.38±1.24
Dynamic68.60±2.64 77.75±0.2044.81±1.57 76.15±0.88
Cascaded71.79±0.27 75.13±0.1419.73±0.70 31.75±1.06
1 UAV + 1 UGV 2 UAVs + 2 UGVs
Participation Vanilla SPL Vanilla SPL
Non-overlap31.50±5.97 61.58±0.6755.79±3.23 76.38±1.52
Dynamic36.67±0.71 59.58±1.7958.46±3.40 79.25±1.30
sequential handoff. Improvements under Dynamic and Cascaded participation further show that the
observed benefit extends to stochastic and successively staged participation schedules. We additionally
evaluate SPL-MAPPO in eight-agent MPE-Advanced and RWARE-Advanced settings. As shown inTa-
ble 2, SPL-MAPPO achieves higher mean task completion than MAPPO in all six matched comparisons,
with an average observed gain of 17.1%. The gains range from 3.3% in MPE-Advanced Cascaded to
more than 30% in the Non-overlap and Dynamic RWARE-Advanced settings. Non-overlap and Dynamic
use 2M environment steps, whereas Cascaded uses 4M to accommodate its longer participation horizon;
differences across participation patterns should therefore not be interpreted as controlled compar-
isons of training budget. SPL introduces no additional models during execution. Its training-time
computational cost, however, varies across environments and team sizes: the overhead is small in
several four-agent settings but becomes more pronounced in some larger-scale configurations. Detailed
wall-clock measurements are reported inAppendix C.
5.2. Physics-Based UAV–UGV Evaluation
We further evaluate SPL in a physics-based UAV–UGV setting in Isaac Lab, where earlier UAVs navigate
to sensing locations, and later UGVs navigate to and execute downstream tasks. This introduces
embodied motion and obstacle constraints on both evidence acquisition and downstream execution. As
shown inTable 2, SPL-MAPPO achieves higher mean task completion than MAPPO in all four team-size–
participation settings. The gains range from 20.6% to 30.1% across both team sizes and occur under
both Non-overlap and Dynamic participation. Attempt-level diagnostics show more resolved executions
and successful completions with SPL-MAPPO, together with a lower observed failure rate per resolved
attempt, while map and published evidence coverage vary with team size. These results provide
complementary evidence that the observed SPL improvement persists when evidence acquisition
and downstream task execution are coupled to embodied motion. Execution, coverage, and safety
diagnostics are reported inAppendix D.5.
Qualitative case study.Figure 5 compares MAPPO and SPL-MAPPO on the same deterministic
fixed-handoff rollout in the one-UAV–one-UGV Isaac setting. The hidden ground truth, shown only for
interpretation, contains two decoy tasks (Tasks 1 and 3) and two serviceable tasks (Tasks 2 and 4). All
candidate locations are visible to the agents, while task serviceability must be inferred from acquired
evidence. The UAV acts during the first 200 steps of the 600-step episode, after which the UGV acts
using the persistent shared board. In the trajectory panels, triangles and squares mark UAV and
UGV starting positions, circles mark trajectory endpoints, plus/minus symbols denote published task
cues, and check/cross symbols denote UGV service outcomes; trajectory color darkens with time. At
11

Cooperating with Future Collaborators: Multi-Agent RL under Staggered Participation
Figure5: Isaac Lab case study comparing Vanilla and SPL based on MAPPO.
handoff, both methods have mapped 48 of 144 occupancy cells, but their task-specific evidence differs
substantially. MAPPO publishes no task-quality cues, after which its UGV attempts decoy Task 3 at
step 453 and completes serviceable Task 2 at step 577, leaving Task 4 unserved. SPL-MAPPO instead
acquires cues for Tasks 2, 3, and 4, which are published to the shared board after the five-step delay:
positive for Tasks 2 and 4 and negative for Task 3. Its UGV then completes Task 4 at step 438 and Task 2
at step 484 without attempting a decoy. This example makes the cross-stage information pathway
explicit: similar spatial coverage can coexist with different task-specific evidence and, consequently,
different downstream decisions.
5.3. Ablation Study
Weevaluate SPL-MAPPO underNon-overlapparticipation toexaminethecontributionof itstwotraining
components, the role of inherited evidence in receiver learning, and the dependence on structured
training information.Acquisition-onlyandReceiver-onlyretain only the corresponding SPL component.
Evidence-redactedremoves inherited task evidence consistently from both outcome-model inputs and
receiver-target construction, whereasSKD-MAPPOretains full evidence during outcome-model training
but masks predecessor-generated evidence when constructing receiver targets.Outcome-agnosticfixes
candidate success probabilities to0.5, whilePermutedassigns predicted utilities to incorrect legal actions
while preserving the receiver-update budget.Table 3shows that full SPL achieves the highest observed
mean task completion in all four environments. Relative to full SPL, Acquisition-only and Receiver-only
12

Cooperating with Future Collaborators: Multi-Agent RL under Staggered Participation
Table 3: SPL ablations under Non-overlap.
Variant MPE-Base MPE-Adv. RWARE-Base RWARE-Adv.
Full SPL78.73±0.43 78.23±0.16 86.70±0.49 80.03±0.23
SKD-MAPPO70.50±0.00 70.38±0.00 70.75±0.00 67.63±0.23
Acquisition-only70.50±0.00 69.88±0.50 77.80±2.37 62.83±1.98
Receiver-only73.45±1.29 72.28±0.94 74.40±1.94 72.90±1.03
Evidence-redacted70.50±0.00 70.38±0.00 70.75±0.00 69.13±0.21
Outcome-agnostic70.50±0.00 70.38±0.00 62.33±2.27 48.48±0.80
Permuted37.13±0.37 37.05±0.87 26.80±2.76 28.95±0.84
reduce mean task completion by 10.7% and 7.7% on average, respectively. Neither component alone
reproduces the complete method, supporting the complementary roles of evidence preparation and
downstream evidence use.
SKD-MAPPO also remains below full SPL in every environment, with an average gap of 11.1%.
Thus, matching SPL’s training-side structured information and auxiliary machinery without evidence-
conditionedreceiversupervisiondoesnotreproducethefullSPLperformance. Wefurthertestsensitivity
to misspecified validity priors while keeping the true environment distribution unchanged. Even with
fully reversed priors (λ=1 ), SPL-MAPPO retains 76.73% and 77.45% TC in MPE-Advanced and
RWARE-Advanced, compared with nominal values of78.23% and 80.03%, respectively. Full success
is more sensitive, particularly in RWARE-Advanced; complete results are reported inAppendix D.6.
These results show that SPL retains substantial task-completion performance under validity-prior
misspecification in the tested settings. Other forms of structured-model error remain outside the scope
of this experiment. Receiver-target ablations further show that the information used to construct the
target matters. Evidence-redacted, Outcome-agnostic, and Permuted reduce mean task completion by
10.7%, 18.0%, and 48.4% on average, respectively. The strong degradation under Permuted, despite
preserving the receiver-update budget, shows that the correspondence between candidate actions and
their predicted utilities is important. Preserving the auxiliary update budget alone is insufficient to
recover the full SPL performance.
6. Conclusion
We studied cooperative MARL under staggered participation and introduced SPL, which combines
prospective evidence acquisition with downstream evidence use. SPL achieves higher observed mean
task completion across multiple policy-based backbones, participation patterns, larger teams, and
physics-based UAV–UGV simulation. These results support explicitly addressing both information
acquisition and downstream utilization when agents contribute over staggered participation windows.
13

Cooperating with Future Collaborators: Multi-Agent RL under Staggered Participation
References
[1] Friedrich M Rockenbauer, Jaeyoung Lim, Marcus G Müller, Roland Siegwart, and Lukas Schmid. Traversing
mars: Cooperative informative path planning to efficiently navigate unknown scenes.IEEE Robotics and
Automation Letters, 2024.
[2] Takahiro Sasaki, Kyohei Otsu, Rohan Thakker, Sofie Haesaert, and Ali-akbar Agha-mohammadi. Where
to map? iterative rover-copter path planning for mars exploration.IEEE Robotics and Automation Letters,
2020.
[3] Shiyong Zhang, Xuebo Zhang, Tianyi Li, Jing Yuan, and Yongchun Fang. Fast active aerial exploration for
traversable path finding of ground robots in unknown environments.IEEE Transactions on Instrumentation
and Measurement, 2022.
[4] Chao Yu, Xinyi Yang, Jiaxuan Gao, Jiayu Chen, Yunfei Li, Jijia Liu, Yunfei Xiang, Ruixin Huang, Huazhong
Yang, Yi Wu, and Yu Wang. Asynchronous multi-agent reinforcement learning for efficient real-time
multi-robot cooperative exploration. InProceedings of the 2023 International Conference on Autonomous
Agents and Multiagent Systems, 2023.
[5] Yifei Min, Jiafan He, Tianhao Wang, and Quanquan Gu. Cooperative multi-agent reinforcement learning:
Asynchronous communication and linear function approximation. InInternational Conference on Machine
Learning. PMLR, 2023.
[6] Sydney Dolan, Siddharth Nayak, Jasmine Jerry Aloor, and Hamsa Balakrishnan. Asynchronous cooperative
multi-agent reinforcement learning with limited communication. InProceedings of the 24th International
Conference on Autonomous Agents and Multiagent Systems, 2025.
[7] Bo Liu, Qiang Liu, Peter Stone, Animesh Garg, Yuke Zhu, and Anima Anandkumar. Coach-player multi-
agent reinforcement learning for dynamic team composition. InInternational Conference on Machine
Learning. PMLR, 2021.
[8] Arrasy Rahman, Ignacio Carlucho, Niklas Höpner, and Stefano V Albrecht. A general learning framework
for open ad hoc teamwork using graph-based policy learning.Journal of Machine Learning Research, 2023.
[9] Caroline Wang. N-agent ad hoc teamwork. InProceedings of the Thirty-Third International Joint Conference
on Artificial Intelligence, 2024.
[10] Yongheng Liang, Hejun Wu, Haitao Wang, and Hao Cai. Asynchronous credit assignment for multi-agent
reinforcement learning. InProceedings of the Thirty-Fourth International Joint Conference on Artificial
Intelligence, IJCAI ’25, 2025.
[11] Milad Farjadnasab and Shahin Sirouspour. Cooperative and asynchronous transformer-based mission
planning for heterogeneous teams of mobile robots.Robotics and Autonomous Systems, page 105131, 2025.
[12] Siyi Hu, Mohamad A Hady, Jianglin Qiao, Jimmy Cao, Mahardhika Pratama, and Ryszard Kowalczyk.
Adaptability in multi-agent reinforcement learning: A framework and unified review.arXiv preprint
arXiv:2507.10142, 2025.
[13] Jordan Erskine and Christopher Lehnert. Developing cooperative policies for multi-stage reinforcement
learning tasks.IEEE Robotics and Automation Letters, 2022.
[14] Changxi Zhu, Mehdi Dastani, and Shihan Wang. A survey of multi-agent deep reinforcement learning with
communication.Autonomous Agents and Multi-Agent Systems, 38(1):4, 2024.
[15] Shengchao Hu, Li Shen, Ya Zhang, and Dacheng Tao. Learning multi-agent communication from graph
modeling perspective. InInternational Conference on Learning Representations, 2024.
[16] XinranLiandJunZhang. Context-awarecommunicationformulti-agentreinforcementlearning.Proceedings
of the 2024 International Conference on Autonomous Agents and Multiagent Systems, 2024.
[17] Ming Yang, Kaiyan Zhao, Yiming Wang, Renzhi Dong, Yali Du, Furui Liu, Mingliang Zhou, and Leong Hou
U. Team-wise effective communication in multi-agent reinforcement learning.Autonomous Agents and
Multi-Agent Systems, 2024.
14

Cooperating with Future Collaborators: Multi-Agent RL under Staggered Participation
[18] Yi-Yu Lin, Jiahao Zhang, and Xiao-Jun Zeng. Why and whom to communicate? a dual-objective, cost-benefit
framework for multi-agent communication. InProc. of the 25th International Conference on Autonomous
Agents and Multiagent Systems, 2026.
[19] Enguang Yao, Qidong Liu, Jialu Sun, Kaibo Huang, and Mingliang Xu. Direct: Decentralized intention and
latent rule emergence for multi-agent cooperation under intermittent communication. InProceedings of the
Thirty-Fifth International Joint Conference on Artificial Intelligence, IJCAI-26, pages 437–445. International
Joint Conferences on Artificial Intelligence Organization, 2026.
[20] XingXu, RongpengLi, ZhifengZhao, andHonggangZhang. Stigmergicindependentreinforcementlearning
for multiagent collaboration.IEEE transactions on neural networks and learning systems, 2021.
[21] Jianglin Qiao, Zehong Cao, Siyi Hu, Mingjun Fan, Mahardhika Pratama, and Ryszard Kowalczyk. Multi-
agentRLwithinvisiblecollaborators: Marginaladvantageestimationforindirectcooperation. InProceedings
of the 42nd Conference on Uncertainty in Artificial Intelligence. PMLR, 2026.
[22] Omayma Mahjoub, Sasha Abramowitz, Ruan John de Kock, Wiem Khlifi, Simon Verster Du Toit, Jemma
Daniel, Louay Ben Nessir, Louise Beyers, Juan Claude Formanek, Liam Clark, and Arnu Pretorius. Sable: a
performant, efficient and scalable sequence model for MARL. InForty-second International Conference on
Machine Learning, 2025.
[23] Andreas Kontogiannis, Konstantinos Papathanasiou, Yi Shen, Giorgos Stamou, Michael M. Zavlanos, and
George Vouros. Enhancing cooperative multi-agent reinforcement learning with state modelling and
adversarial exploration. InForty-second International Conference on Machine Learning, 2025.
[24] Sehyeok Kang, Yongsik Lee, Gahee Kim, Song Chong, and Se-Young Yun. MA2E: Addressing partial observ-
ability in multi-agent reinforcement learning with masked auto-encoder. InThe Thirteenth International
Conference on Learning Representations, 2025.
[25] Yuhang Pei, Tao Ren, Yuxiang Zhang, Zhipeng Sun, and Matys Champeyrol. Policy distillation for efficient
decentralized execution in multi-agent reinforcement learning.Neurocomputing, 626:129617, 2025.
[26] ZimoZhai, ManjieXu, andWeiLiang. Distillingtask-levelcoordinationpoliciesforgeneralizablemulti-agent
cooperation. InForty-third International Conference on Machine Learning, 2026.
[27] Nannan Cao, Kian Hsiang Low, and John M. Dolan. Multi-robot informative path planning for active
sensing of environmental phenomena: a tale of two algorithms. InProceedings of the 2013 International
Conference on Autonomous Agents and Multi-Agent Systems, 2013.
[28] Mikko Lauri, Joni Pajarinen, and Jan Peters. Information gathering in decentralized pomdps by policy graph
improvement. InProceedings of the 18th International Conference on Autonomous Agents and MultiAgent
Systems, 2019.
[29] Wei-Chen Liao, Ti-Rong Wu, and I-Chen Wu. Dynamic sight range selection in multi-agent reinforcement
learning. InProceedings of the 24th International Conference on Autonomous Agents and Multiagent Systems,
2025.
[30] Yugu Li, Zehong Cao, Jianglin Qiao, and Siyi Hu. Nucleolus credit assignment for effective coalitions in
multi-agent reinforcement learning. InProceedings of the 24th International Conference on Autonomous
Agents and Multiagent Systems, AAMAS ’25, page 1318–1326. International Foundation for Autonomous
Agents and Multiagent Systems, 2025.
[31] Frans A Oliehoek and Christopher Amato.A concise introduction to decentralized POMDPs. Springer, 2016.
[32] Ryan Lowe, Yi Wu, Aviv Tamar, Jean Harb, Pieter Abbeel, and Igor Mordatch. Multi-agent actor-critic for
mixed cooperative-competitive environments.Advances in neural information processing systems, 2017.
[33] Georgios Papoudakis, Filippos Christianos, Lukas Schäfer, and Stefano V. Albrecht. Benchmarking multi-
agent deep reinforcement learning algorithms in cooperative tasks. InProceedings of the Neural Information
Processing Systems Track on Datasets and Benchmarks (NeurIPS), 2021.
[34] Mayank Mittal, Pascal Roth, James Tigue, Antoine Richard, Octi Zhang, Peter Du, Antonio Serrano-Munoz,
15

Cooperating with Future Collaborators: Multi-Agent RL under Staggered Participation
Xinjie Yao, René Zurbrügg, Nikita Rudin, et al. Isaac lab: A gpu-accelerated simulation framework for
multi-modal robot learning.arXiv preprint arXiv:2511.04831, 2025.
[35] Chao Yu, Akash Velu, Eugene Vinitsky, Jiaxuan Gao, Yu Wang, Alexandre Bayen, and Yi Wu. The surprising
effectiveness of ppo in cooperative multi-agent games.Advances in neural information processing systems,
2022.
[36] Jakub Grudzien Kuba, Ruiqing Chen, Muning Wen, Ying Wen, Fanglei Sun, Jun Wang, and Yaodong Yang.
Trust region policy optimisation in multi-agent reinforcement learning. InInternational Conference on
Learning Representations, 2022.
[37] Christian Schroeder De Witt, Tarun Gupta, Denys Makoviichuk, Viktor Makoviychuk, Philip HS Torr, Mingfei
Sun, and Shimon Whiteson. Is independent learning all you need in the starcraft multi-agent challenge?
arXiv preprint arXiv:2011.09533, 2020.
[38] Yifan Zhong, Jakub Grudzien Kuba, Xidong Feng, Siyi Hu, Jiaming Ji, and Yaodong Yang. Heterogeneous-
agent reinforcement learning.Journal of Machine Learning Research, 2024.
16

Cooperating with Future Collaborators: Multi-Agent RL under Staggered Participation
A. Proofs and Additional Analysis for SPL
This section provides full proofs for Proposition 1, Proposition 2, and Theorem 1 in the main paper,
together with supporting lemmas and additional analysis of the SPL auxiliary objectives. The acquisition
result applies a standard value-of-information argument to the top-k completion surrogate used by
SPL. For the receiver analysis, we additionally relate the distillation term directly to the training
objective and give a conditional connection between outcome-model error and standardized-score
error. Section A.6 summarizes the scope of the analysis.
A.1. Notation and Assumptions
Agent i denotes an earlier participant and agentj a future collaborator. The actor-visible acquisition
context ofi is denoted byci t, while xj t denotes the actor-visible receiver context ofj. The legal receiver
action set is
Aj t ={u∈ Uj :M j t(u) =1}.
For an attributable receiver decision, letY∈ {0, 1}denote its downstream outcome and letC∈ {0, 1}
indicate whether that outcome is retained inDout. The retained-outcome probability is
p j ∗(u|x) =Pr(Y=1|X=x,U=u,J=j,C=1).(A.1)
The corresponding local utility is
U j ∗(u|x) =p j ∗(u|x)c + j (u) + [︁ 1−p j ∗(u|x) ]︁ c− j (u),(A.2)
where c+ j (u) and c− j (u) are the task-level utilities associated with successful and unsuccessful execution,
respectively. Illegal actions are excluded from the distributions below.
Assumption 1(Attribution and censoring).Whenever C=1 , the recorded outcome is correctly
attributed to the selected receiver action. Receiver-side probability and utility results are conditional
onC=1. They admit an unconditional interpretation only when
Y⊥C|X,U,J.
Assumption 2(Coverage).Every legal context–candidate pair on which a receiver guarantee is invoked
is selected with positive probability under the retained rollout distribution.
A.2. Proof of Proposition 1: Prospective Acquisition Target
Let Macq denote the fixed acquisition model used to construct SPL supervision. Probabilities and
expectations in this subsection are taken with respect to this model. Consider binary task-validity
variablesW 1, . . . ,Wn. Given acquisition contextci t, let
br =Pr Macq (Wr =1|c i t),b= (b 1, . . . ,b n).
If a future collaborator can execute at mostktasks, define
Vk(b) =max S⊆{1,...,n}:|S|≤k
∑︁
r∈S
br.(A.3)
17

Cooperating with Future Collaborators: Multi-Agent RL under Staggered Participation
For a legal acquisition actionu, let Zu denote its observation andbZu the posterior marginals produced
byM acq. Its model-relative prospective gain is
∆i t(u) =EMacq
[︁
Vk(bZu )|c i t,u ]︁ −V k(b).(A.4)
SPL combines this gain with acquisition distance through
si t(u) =log (︁ max{∆i t(u),ϵ acq} )︁ − di t(u) τd .(A.5)
Let
P i t = {︁ u:M i t(u) =1,uis task-directed,∆ i t(u)>0 }︁
denote the legal positive-gain task-directed actions.
For completeness, the task-directed component of the SPL acquisition target is
̃︀qi acq(u) = exp(si t(u))∑︀
v∈P i t exp(si t(v)) .(A.6)
Equivalently,
̃︀qi acq =arg max q∈∆(P i t )
⎧
⎨
⎩
∑︁
u∈P i t
q(u)s i t(u) +H(q)
⎫
⎬
⎭ ,(A.7)
whereH(q) =− ∑︀ u q(u)logq(u).
Proof.For every feasible setSwith|S| ≤k, let
LS(b) =
∑︁
r∈S
br.
Since
Vk(b) =max S:|S|≤k LS(b),
Vk is convex. Bayesian consistency underMacq gives
EMacq
[︁
bZu |c i t,u ]︁ =b.
Jensen’s inequality therefore gives
EMacq
[︁
Vk(bZu )|c i t,u ]︁ ≥V k (︁ EMacq[bZu |c i t,u] )︁ =V k(b),
which proves
∆i t(u)≥0.
This is the standard nonnegative value-of-information argument applied to the top-k completion
surrogate.
For the Gibbs characterization, consider
F(q) =
∑︁
u∈P i t
q(u)s i t(u) +H(q)
18

Cooperating with Future Collaborators: Multi-Agent RL under Staggered Participation
over the probability simplex. Introducing a Lagrange multiplier for∑︀ u q(u) =1 gives the stationary
condition
si t(u)−logq(u)−1+λ=0,
hence
q(u)∝exp(s i t(u)).
Normalization yields Eq.(A.6). Since entropy is strictly concave and the score term is linear, this
solution is the unique maximizer of Eq. (A.7).
The complete acquisition target assigns the prescribed fixed mass to the scan action and distributes
the remaining mass according tõ︀qi acq. If P i t is empty, the scan action receives unit target mass. The
implementation uses the small positive-gain threshold and numerical constants reported in Sec. B.4.
The nonnegativity result is model-relative. Bayesian consistency withinMacq does not require its
assumed priors to equal the true environment priors. Prior misspecification can therefore preserve
nonnegative model-relative gains while changing how those gains relate to performance in the true
environment; this sensitivity is evaluated in Sec. D.6.
A.3. Proof of Proposition 2: Retained-Outcome Calibration
For any measurable predictorpj(u|x)∈[0, 1] , define its population binary-cross-entropy risk over
retained outcomes as
Lout(p) =E
[︁
ℓBCE
(︁
Y,p J(U|X) )︁ |C=1 ]︁ .(A.8)
The excess population risk satisfies
Lout(p)− Lout(p ∗) =E
[︁
KL
(︁
Ber(p J ∗(U|X))∥Ber(p J(U|X)) )︁ |C=1 ]︁ .(A.9)
Let
C∆ =sup
u,j
|c+ j (u)−c − j (u)|<∞.
The induced local utility then satisfies
E
[︂(︁
U J p(U|X)−U J ∗(U|X) )︁2 |C=1 ]︂ ≤ C2 ∆ 2 [Lout(p)− Lout(p ∗)] .(A.10)
Proof.Fix a covered triple(x,u,j)and abbreviate
p∗ =p j ∗(u|x),p=p j(u|x).
The conditional binary-cross-entropy risk is
r(p;p ∗) =−p ∗ logp−(1−p ∗)log(1−p).
Its excess risk is
r(p;p ∗)−r(p ∗;p ∗) =KL (Ber(p ∗)∥Ber(p) ) ,
which is non-negative and vanishes only whenp=p ∗. Taking expectations over(X,U,J)|C=1 gives
Eq. (A.9).
19

Cooperating with Future Collaborators: Multi-Agent RL under Staggered Participation
From Eq. (A.2),
U j p(u|x)−U j ∗(u|x) = [︁ pj(u|x)−p j ∗(u|x) ]︁ [︁ c+ j (u)−c − j (u) ]︁ .
Hence ⃒⃒⃒U j p −U j ∗ ⃒⃒⃒ 2 ≤C 2 ∆|p−p ∗|2.
Pinsker’s inequality gives
|p−p ∗|2 ≤ 1 2 KL (Ber(p ∗)∥Ber(p) ) .
Combining the two inequalities and taking expectations proves Eq. (A.10).
The result is conditional on retained attributable outcomes. Under the additional condition
Y⊥C|X,U,J,
the retained-outcome probability also equals the corresponding unconditional success probability.
A.4. Receiver Target and Supporting Analysis
Fix an eligible receiver decision(j,t)with legal action set
A=A j t,K=|A|.
For any local utility vectorU over A, letµU and σ2 U denote its mean and variance over legal actions,
and define the standardized score
zU(u) = U(u)−µ U√︁
σ2 U +ϵ z
,ϵ z >0.(A.11)
For a score vectorz, the SPL receiver target is
qj SPL(u) = exp(βz(u))∑︀
v∈A exp(βz(v)) ,u∈ A.(A.12)
Lemma 1(Soft receiver target).Forβ>0, the distribution in Eq.(A.12)uniquely maximizes
∑︁
u∈A
q(u)z(u) + 1 β H(q)(A.13)
overq∈∆(A), and satisfies
max
u∈A
z(u)−E u∼q j SPL [z(u)]≤ logK β .(A.14)
Proof.Introducing a Lagrange multiplier for the simplex constraint gives the stationary condition
z(u)− 1 β [logq(u) +1] +λ=0,
hence
q(u)∝exp(βz(u)).
20

Cooperating with Future Collaborators: Multi-Agent RL under Staggered Participation
Since the entropy term is strictly concave, this solution is unique and equals Eq. (A.12).
Let
u∗ ∈arg max
u∈A
z(u).
Optimality ofq j SPL relative to the point mass onu∗ gives
Eqj SPL [z] +1 β H(q j SPL)≥z(u ∗).
Using
H(q j SPL)≤logK
yields Eq. (A.14).
Receiver distillation.For a fixed SPL targetq j SPL and receiver policyπj t,
CE(q j SPL,π j t) =H(q j SPL) +KL(qj SPL∥π j t).(A.15)
Thus,
η=KL(q j SPL∥π j t) =CE(qj SPL,π j t)−H(q j SPL),(A.16)
so the local distillation term is directly computable from the receiver target and actor distributions.
Averaging Eq. (A.16) over receiver decisions gives an empirical diagnostic of target distillation.
Connection between outcome error and score error.The calibration result in Eq.(A.10) controls
utility error on selected actions, whereas receiver regret depends on scores over the full legal action
set. A quantitative connection follows under stronger coverage. Let
ρj(u|x) =Pr(U=u|X=x,J=j,C=1).
Suppose that, on the retained context distribution considered below, there existsα>0such that
ρj(u|x)≥α
for every legal candidate whose utility is supplied by the outcome model. Any remaining legal actions
with fixed utilities are assumed identical in the predicted and reference utility vectors.
Lemma 2(Mean score-error control).Letp ¯ψ denote the target outcome predictor and let
δ(X,J) =∥z ¯ψ −z ∗∥∞.
Under the uniform coverage condition above,
E
[︀
δ(X,J) 2 |C=1 ]︀ ≤ C2 ∆
2αϵz
[︁
Lout(p ¯ψ)− Lout(p ∗)
]︁
≤ C2 ∆
2αϵz
Lout(p ¯ψ).(A.17)
Proof. For a fixed legal action set, the stabilized standardization map in Eq.(A.11) is 1/√ϵz-Lipschitz
from the utility-vectorℓ2 norm to the score-vectorℓ∞ norm. Hence
δ(X,J) 2 ≤ ∥U ¯ψ −U ∗∥2 2
ϵz
.
21

Cooperating with Future Collaborators: Multi-Agent RL under Staggered Participation
The uniform coverage condition gives
∑︁
u∈A
(︁
U j ¯ψ(u|x)−U j ∗(u|x) )︁2 ≤ 1 α E [︂(︁ U J ¯ψ(U|X)−U J ∗(U|X) )︁2 |X=x,J=j,C=1 ]︂ .
Taking expectations over retained contexts and applying Eq.(A.10) proves the first inequality in
Eq. (A.17). The second follows from
Lout(p ∗)≥0.
Equation (A.17) controls mean squared score error under the retained context distribution; it is not
a uniform per-context bound. For fixedα and ϵz, vanishing population excess outcome risk implies
vanishing mean squared score error. Held-out binary-cross-entropy provides an empirical estimate of
population outcome risk, while finite-sample generalization remains separate from this population
statement.
A.5. Proof of Theorem 1: Local Receiver Score Regret
Let z∗ denote the standardized score induced by the retained-outcome local utilityU j ∗, and letz ¯ψ
denote the score induced by the target outcome model. Define
δ=∥z ¯ψ −z ∗∥∞,η=KL
(︁
qj SPL∥π j t )︁ ,
where
qj SPL(u)∝exp(βz ¯ψ(u)),
and let
Rz =max u∈A z∗(u)−min u∈A z∗(u).
Theorem 1 in the main paper states that
Regj z,t(π j t)≤ logK β +2δ+R z
√︂
η
2 ,(A.18)
where
Regj z,t(π j t) =max u∈A z∗(u)−E u∼π j t [z∗(u)].(A.19)
Proof.Add and subtract the expected reference score underqj SPL:
Regj z,t(π j t) = [︁ max u z∗(u)−E qj SPL [z∗] ]︁ + [︁ Eqj SPL [z∗]−E πj t [z∗] ]︁ .
Since
∥z ¯ψ −z ∗∥∞ ≤δ,
we have
max
u
z∗(u)−E qj SPL [z∗]≤max u z ¯ψ(u)−E qj SPL [z ¯ψ] +2δ.
22

Cooperating with Future Collaborators: Multi-Agent RL under Staggered Participation
Applying Eq. (A.14) gives
max
u
z∗(u)−E qj SPL [z∗]≤ logK β +2δ.
For the second term,
Eqj SPL [z∗]−E πj t [z∗]≤R z TV
(︁
qj SPL,π j t )︁ .
Pinsker’s inequality gives
TV
(︁
qj SPL,π j t )︁ ≤
√︃
KL(q j SPL∥π j t)
2 =
√︂
η
2 .
Combining the two bounds proves Eq. (A.18).
The bound separates three local sources of receiver error: finite-temperature softness, error in the
evidence-conditioned score estimate, and incomplete distillation of the SPL target into the decentralized
policy. Equation(A.16) makes the distillation term directly observable during training, while Lemma 2
gives a population-level connection between score approximation and outcome-model error under
uniform coverage.
A.6. Scope of the Local Analysis
The results above characterize the local auxiliary objectives used by SPL. They support the construc-
tion and interpretation of the training signals but do not establish global convergence or monotonic
improvement of the cooperative return.
Acquisition model and prior misspecification.Proposition 1 in the main paper is a model-relative
value-of-information result. Bayesian consistency within the acquisition model guarantees non-negative
prospective gain for the top-k surrogate, including when the model uses internally consistent but
misspecified priors. Such misspecification can change the relation between the acquisition score and
performance under the true environment distribution. Section D.6 evaluates this sensitivity while
keeping the remaining structured model components fixed.
Receiver approximation scope.Proposition 2 in the main paper controls expected local-utility error
on the retained selected-action distribution. The receiver distillation quantityη is directly computable
from the target and actor distributions through Eq.(A.16). Lemma 2 further connects mean squared
standardized-score error to population outcome-model risk under a uniform retained-action coverage
condition. It does not provide a uniform per-context bound, and empirical validation loss introduces
the usual finite-sample generalization error. Theorem 1 in the main paper therefore remains a local
standardized-score guarantee, not a bound on raw utility or full team return.
Local utility and retained outcomes.The retained-outcome utility in Eq. (A.2) describes the task-
level consequence of an attributable receiver action and need not equal the full Dec-POMDP action
value. Receiver-side results are conditional on attributable outcomes retained inDout and admit an
unconditional interpretation only under Assumption 1. Under partially overlapping participation, the
receiver context may combine evidence acquired before and after participation begins; the analysis
conditions on the complete actor-visible context and does not isolate the causal contribution of pre-
participation evidence.
23

Cooperating with Future Collaborators: Multi-Agent RL under Staggered Participation
Backbone optimization.SPL auxiliary actor updates are applied in addition to the native MAPPO,
IPPO, or HAPPO optimization. The analysis does not provide a convergence guarantee for the resulting
joint optimization; the reported task-completion and return results are empirical.
B. Implementation and Reproducibility Details
This section provides the environment configurations, participation schedules, SPL target construction,
optimization settings, and training procedure used in the reported experiments. All methods are
implemented within the HARL framework. We denote the SPL extensions of MAPPO, IPPO, and
HAPPO as SPL-MAPPO, SPL-IPPO, and SPL-HAPPO, respectively. Within each matched comparison, the
corresponding unmodified backbone is referred to as MAPPO, IPPO, or HAPPO.
B.1. Environment Configuration
The primary four-agent MPE and RWARE evaluations contain two earlier participants, two future
collaborators, and eight candidate tasks. Each domain includes Base and Advanced variants. We
additionally evaluate SPL in physics-based UAV–UGV tasks in Isaac Lab with either one UAV and one
UGV or two UAVs and two UGVs. Persistent task-relevant evidence produced by earlier participants
remains available to future collaborators.
The Base variants use fixed task assignments and earlier-participant–future-collaborator correspon-
dences. MPE-Advanced randomizes balanced task shards, spawn assignments, and future-collaborator
identities, while RWARE-Advanced permutes task identifiers and uses a shared candidate pool with
dynamic task claims. The Isaac Lab settings introduce physical motion, obstacles, and planner-mediated
downstream task execution. The eight-agent scaling configurations are described separately below.
Table B.1: Four-agent MPE/RWARE and Isaac Lab configurations.
Environment Earlier Future Tasks Horizon
MPE-Base 2 2 8 125 (250)
MPE-Advanced 2 2 8 125 (250)
RWARE-Base 2 2 8 500 (1000)
RWARE-Advanced 2 2 8 500 (1000)
Isaac Lab (2-agent) 1 UAV 1 UGV 4 600
Isaac Lab (4-agent) 2 UAVs 2 UGVs 6 840
For the primary four-agent MPE and RWARE settings, the environments use the same eight task-validity
priors and a fixed-valid-task sampling rule. Probe outcomes are noisy but persistent, and each future
collaborator can execute at most two candidate tasks. Table B.2 summarizes the main task and evidence
parameters.
B.2. Temporal Participation Patterns
Participation intervals follow the half-open convention[tstart,t end). Inactive agents take a null envi-
ronment action and make no effective policy decision. The Base and Advanced variants within each
domain use the same participation schedules.
We evaluate five participation patterns.Non-overlapuses a strict team-wide handoff from earlier
participants to future collaborators.Overlap-25andOverlap-50introduce fixed levels of cross-role
overlap.Dynamicsamples pair-specific handoff times each episode while preserving aggregate role
24

Cooperating with Future Collaborators: Multi-Agent RL under Staggered Participation
Table B.2: Task and evidence settings for MPE and RWARE.
Setting MPE RWARE
Candidate tasks 8 8
Validity priors(0.80, 0.80, 0.65, 0.65, 0.35, 0.35, 0.20, 0.20)
Probe budget / earlier participant 5 6
Probe limit / task 2 2
Probe accuracy 0.85 0.85
Publication delay 5 5
Execution budget / future collaborator 2 2
Valid-task value{12, 12, 10, 10, 8, 8, 6, 6}1
Probe cost 0.2 0.01
Invalid-execution cost 8.0 0.25
exposure.Cascadeddistributes the two earlier-participant–future-collaborator pairs across successive
participation intervals, with an extended horizon to preserve total role exposure.
Table B.3: Four-agent participation schedules.
Domain Participation HorizonP 0 P1 R0 R1
MPE Non-overlap 125[0, 45) [0, 45) [45, 125) [45, 125)
MPE Overlap-25 125[0, 45) [0, 45) [34, 125) [34, 125)
MPE Overlap-50 125[0, 45) [0, 45) [22, 125) [22, 125)
MPE Dynamic 125[0,h 0) [0,h 1) [h 0, 125) [h 1, 125)
MPE Cascaded 250[0, 45) [125, 170) [45, 125) [170, 250)
RWARE Non-overlap 500[0, 200) [0, 200) [200, 500) [200, 500)
RWARE Overlap-25 500[0, 175) [0, 225) [175, 500) [225, 500)
RWARE Overlap-50 500[0, 150) [0, 250) [150, 500) [250, 500)
RWARE Dynamic 500[0,h 0) [0,h 1) [h 0, 500) [h 1, 500)
RWARE Cascaded 1000[0, 200) [500, 700) [200, 500) [700, 1000)
Here, P0,P 1 denote earlier participants andR0,R 1 denote future collaborators. In MPE, Overlap-25
and Overlap-50 provide 11 and 23 steps of cross-role overlap, respectively; the corresponding RWARE
overlaps are 50 and 100 steps. For Dynamic participation,h0 = ¯h+δ and h1 = ¯h−δ , where δ
is sampled once per episode from a symmetric discrete uniform distribution. MPE uses¯h=45 and
δ∈ {−11, . . . , 11}, whileRWAREuses ¯h=200 and δ∈ {−50, . . . , 50}. Consequently, Dynamicchanges
the pair-specific handoff times while preserving aggregate earlier-participant and future-collaborator
exposure. Cascaded preserves the same role exposure while changing its temporal ordering.
B.3. Isaac Lab Configuration
The two-agent Isaac Lab task contains four candidate sites, of which two are serviceable in each episode,
on a12×12 occupancy grid with five barriers. The four-agent setting contains six candidate sites, of
which four are serviceable. Candidate positions are public from reset, while serviceability remains
hidden. UAV sensing has accuracy0.85 and a five-step publication delay. UGV motion is planned from
the published occupancy map, and selecting a task commits the UGV to its physical execution. Neither
the actor nor the critic receives hidden serviceability.
Dynamic handoff times are sampled per episode. The two-agent setting exposes the normalized handoff
25

Cooperating with Future Collaborators: Multi-Agent RL under Staggered Participation
Table B.4: Isaac Lab participation and training configurations.
Agents Participation Training steps Participation windows
1 UAV + 1 UGV Non-overlap 1,996,800 UAV[0, 200); UGV
[200, 600)
1 UAV + 1 UGV Dynamic 1,996,800 UAV[0,h); UGV[h, 600),
h∼Unif{150, . . . , 250}
2 UAVs + 2 UGVs Non-overlap 3,010,560 UAVs[0, 300); UGVs
[300, 840)
2 UAVs + 2 UGVs Dynamic 3,010,560 UAVs[0, 300); UGVs
[h,h+540),
h∈ {150, 180, . . . , 300}
step to the actors, while the four-agent setting uses a shared UGV participation window with a sampled
start time. MAPPO and SPL-MAPPO use matched participation schedules and evaluation instances.
Each setting uses three independent training seeds and 200 final evaluation episodes per seed. Final
policies are evaluated deterministically, and checkpoints are not selected by performance.
B.4. SPL Target Construction
Prospective acquisition target.The frozen acquisition model constructs the task-validity posterior
from the configured validity priors, the fixed number of valid tasks, and public probe outcomes available
in the actor-visible context. Repeated probe observations are aggregated through their positive and
negative counts using the configured probe accuracy. Hidden task validity and future outcomes are
never provided to either the actor or the target-construction procedure.
Posterior marginalsbr =Pr(W r =1|c i t) are used to compute the prospective gain∆i t(u) defined in
Eq. (A.4). In the implementation, task-directed actions with∆i t(u)≤10 −8 receive no acquisition-target
mass. For the remaining legal task-directed actions,
wi t(u) =max{∆ i t(u),ϵ acq}exp
(︂
− di t(u) τd )︂ ,ϵ acq =10 −12,τ d =0.50.(B.1)
The weights are normalized over eligible task-directed actions. The target assigns0.95 total probability
mass to this distribution and0.05 to the scan action. If no positive-gain task-directed action is legal, the
scan action receives unit target mass. The acquisition model and target-construction rule remain fixed
throughout training.
Outcome-supervised receiver target.For each future collaborator j, SPL uses a candidate-shared
outcome model
p j ψ(u|x) =sigmoid (︀ fψ(g j(x,u)) )︀ ,(B.2)
where gj(x,u) contains the actor-visible pre-decision context, candidate-action features, and
collaborator-role identity. The same scorerfψ is applied across candidate actions. Training labels
are available only for selected actions whose outcomes can be reliably attributed; unselected actions
receive no counterfactual labels.
A slowly updated target modelp ¯ψ is used to construct the receiver target. For legal candidate actionu,
U j ¯ψ(u|x) =p j ¯ψ(u|x)c + j (u) + [︁ 1−p j ¯ψ(u|x) ]︁ c− j (u).(B.3)
26

Cooperating with Future Collaborators: Multi-Agent RL under Staggered Participation
The task-level utilities are fixed during training. In MPE,c+ j (u) =v(u)/12 with v(u)∈ {12, 10, 8, 6}
and c− j (u) =−8/12 . In RWARE, c+ j (u) =1 and c− j (u) =−0.25 . In Isaac Lab, c+ j (u) =1 and
c− j (u) =0. The no-op utility is zero. These quantities define the local utilities used for SPL supervision
and are not interpreted as the complete environment return.
Utilities are standardized over the current legal action set usingϵz =10 −6 as the variance stabilizer,
following Eq.(A.11). The receiver target is then the Boltzmann distribution in Eq.(A.12). All reported
experiments use β=1 . Receiver supervision uses this soft utility target directly, without mixing it with
the current actor policy or converting it to a one-hot target.
Table B.5: Training hyperparameters for the PPO backbones and SPL.
PPO backbone SPL-specific
Parameter Value Parameter Value
Actor hidden layers[128, 128]Outcome hidden width 128
Activation ReLU Outcome learning rate3×10 −4
Actor learning rate1×10 −4 Replay capacity 20,000
Critic learning rate5×10 −4 Outcome minibatch size 128
PPO epochs 3 Outcome gradient steps 4
Critic epochs 3 Target EMA rateρ0.05
PPO clip 0.2 Outcome-model gate 128
Entropy coefficient 0.002 Per-class model gate 16
Discountγ0.99 Receiver-policy gate 1,024
GAEλ0.95 Per-class receiver gate 128
Value normalization enabled Acquisition epochs 1
Recurrent policy disabled Receiver epochs 20
Parameter sharing disabled Acquisition task mass 0.95
Gradient norm cap 10 Distance temperatureτ d 0.50
Receiver target strengthβ1.0
B.5. Optimization and Training Settings
MAPPO, IPPO, and HAPPO use the same feed-forward actor architecture and PPO hyperparameters
listed in Table B.5. Policies are not parameter-shared within a team. MAPPO and HAPPO retain
centralized critics, whereas IPPO uses independent critics based on local observations. SPL does not use
centralized critic state and does not modify the native reward, return estimator, critic objective, or critic
target. The corresponding augmented methods are denoted SPL-MAPPO, SPL-IPPO, and SPL-HAPPO.
Vanilla–SPL comparisons use the same backbone configuration, environment, participation schedule,
training budget, and evaluation protocol.
All primary four-agent MPE and RWARE method–environment–participation combinations are trained
for two million environment steps without early stopping. Reported results use five independent
training seeds per method and configuration, with 200 final evaluation episodes per seed. Training
seeds are the independent replication units. Final policies are evaluated deterministically using a fixed
200-episode reset-seed schedule reused across training seeds within each environment protocol. The
scaling and Isaac Lab settings use the training procedures described in their respective configuration
sections.
27

Cooperating with Future Collaborators: Multi-Agent RL under Staggered Participation
Training-seed pairing.A retrospective audit recovered all 600 expected method–training-seed
records for the 60 primary Vanilla–SPL comparisons. Same-training-seed pairing was verified for 285
pairs across 57 configurations, providing five paired training seeds in each of those configurations.
The Non-overlap MAPPO comparisons in MPE-Advanced, RWARE-Base, and RWARE-Advanced use
different Vanilla and SPL training-seed sets. Their observed method means remain included in the
descriptive results, but paired confidence intervals and pairedp-values are reported as unavailable.
Consequently, paired inference covers 57 of the 60 primary configurations. Full statistical details are
provided in Appendix D.7.
Baseline implementation and adaptation.MAE-MAPPO uses the same per-agent observations, legal
task-option masks, team rewards, participation schedules, and evaluation protocol as MAPPO. For Sable
and SMPE2, we retain the original learning architectures and optimization objectives and adapt only
the environment interface to the SP tasks. Both methods receive the same environment-specific local
observations, legal task-option masks, shared rewards, participation schedules, and episode boundaries
as the PPO-based methods. A common task-option controller maps each legal high-level choice to
the corresponding native environment action, while inactive agents receive only the environment-
defined no-op action. Where global or state-level inputs are required, they are constructed solely
from non-privileged observable information and do not expose hidden task validity. Sable retains
its sequence-model rollout procedure, while SMPE2 retains its recurrent policy, critic, state-VAE, and
state-filtering components. All primary four-agent baseline comparisons use the same two-million-step
training budget, five independent training seeds per method and configuration, and 200 final evaluation
episodes per seed.
Knowledge-matched control.SKD-MAPPO uses the same structured task information, prospective
acquisition supervision, task utilities, outcome-model training procedure, target-model update, readi-
ness conditions, and auxiliary update budget as SPL-MAPPO. Its online outcome model is trained from
the same complete actor-visible pre-decision context and attributable outcome labels as in SPL. When
the learned target outcome model is subsequently used to construct receiver supervision, however,
predecessor-generated task evidence is masked from its input. The decentralized actor observation
remains unchanged. SKD-MAPPO therefore retains evidence during outcome-model learning but
withholds that evidence when constructing the receiver target. This control tests the effect of removing
inherited evidence specifically from the target-construction pathway while leaving the remaining SPL
training machinery unchanged.
Evidence-redacted control.Evidence-redacted uses the same MAPPO backbone, acquisition super-
vision, task utilities, attributable outcome labels, readiness conditions, receiver utility construction,
and auxiliary update budget as SPL-MAPPO. Unlike SKD-MAPPO, inherited predecessor-generated
task evidence is removed consistently from the feature vectors supplied to both the online outcome
model during outcome-model training and the target outcome model during receiver-target construc-
tion. The replay buffer retains the original actor-visible pre-decision context, and redaction is applied
when outcome-model features are constructed. The decentralized actor observation is not modified.
Evidence-redacted therefore evaluates receiver learning when inherited task evidence is unavailable to
both outcome prediction and receiver-target construction, while preserving the remaining training and
execution pipeline.
The distinction between the two controls is thus the stage at which inherited evidence is removed. SKD-
MAPPO allows the outcome model to learn from the complete evidence-conditioned context but removes
28

Cooperating with Future Collaborators: Multi-Agent RL under Staggered Participation
predecessor evidence when that model is queried to construct receiver supervision. Evidence-redacted
removes the same class of inherited evidence from both outcome-model learning and receiver-target
construction. Neither control removes the evidence from the decentralized actor observation, and
neither exposes hidden task validity or future outcomes to the actor or critic.
B.6. Training Procedure and Decentralized Execution
Outcome replay and readiness.When a future collaborator selects a task-directed action, SPL
stores its actor-visible pre-decision context, selected action, collaborator-role identity, and subsequently
attributable outcome. Successful completion is labeled1, while an attributable unsuccessful attempt is
labeled 0. Interrupted, expired, unresolved, or otherwise ambiguous attempts are excluded and receive
no synthetic labels. Information observed after the decision is used only to determine the outcome
label and is not included in the stored pre-decision context.
Outcome-model optimization begins onceDout contains at least 128 retained decisions, including at
least 16 examples from each outcome class. Each eligible training iteration then applies four outcome-
model gradient steps with minibatches of at most 128 replay samples. Receiver-policy supervision
begins once the replay contains at least 1,024 retained decisions with at least 128 examples from each
class. Before this condition is met, future collaborators receive only their native MARL actor update.
Prospective acquisition supervision does not depend on the receiver-side readiness conditions.
Update order and gradient boundaries.After each rollout, attributable receiver outcomes are
appended toDout. Once the outcome-model readiness condition is satisfied, the online outcome model
is updated by binary cross-entropy, followed by the exponential-moving-average update
¯ψ←(1−ρ) ¯ψ+ρψ.
When receiver supervision is ready, receiver targets are constructed from the updated target outcome
model before backbone optimization.
SPL actor updates are interleaved with the native actor updates. For each eligible actor, the native
backbone actor update is performed first, followed by the corresponding SPL update. MAPPO processes
actors in fixed agent order and updates the centralized critic after all actor updates. IPPO applies the
native actor update, SPL update, and independent critic update for each agent before proceeding to
the next agent.
HAPPO retains its sequential heterogeneous actor-update order. For each actor, the current cumulative
factor is stored before the native actor update, followed by the applicable SPL update. Action probabili-
ties are then re-evaluated to update the cumulative factor used by subsequent actors. Thus, later actors
can receive factors reflecting the post-SPL policies of earlier actors. We do not claim that SPL-HAPPO
preserves HAPPO’s original monotonic-improvement guarantee.
The outcome loss updates only the online outcome modelψ, the acquisition loss updates only the
eligible earlier-participant actor, and the receiver loss updates only the eligible future-collaborator
actor. Gradients do not propagate through the frozen acquisition model, target outcome model, utility
construction, replayed outcomes, future trajectories, or environment dynamics. SPL does not modify
the environment reward, transition function, observation space, action space, native return estimator,
or critic objective.
29

Cooperating with Future Collaborators: Multi-Agent RL under Staggered Participation
Decentralized execution.At execution time, each active agent acts solely through its decentralized
policy,
ui t ∼π θi
(︁
· |τi t ,M i t
)︁
.(B.4)
The acquisition model, outcome replay, online and target outcome models, utility calculations, and
SPL target distributions are used only during training. SPL-MAPPO, SPL-IPPO, and SPL-HAPPO use
the original decentralized policy architecture at execution time, without privileged state, auxiliary
inference, or additional communication.
B.7. Training Algorithm
Algorithm 1 summarizes one SPL training iteration. SPL preserves the native optimization procedure of
each MARL backbone and adds the role-appropriate auxiliary actor update. Earlier participants receive
prospective acquisition supervision, while future collaborators receive receiver supervision once the
corresponding replay-readiness condition is satisfied.
30

Cooperating with Future Collaborators: Multi-Agent RL under Staggered Participation
Algorithm 1One training iteration with Staggered Participation Learning
Require: Backbone B; policies{πθi }i∈N; frozen acquisition model; online outcome modelpψ; target outcome modelp ¯ψ;
outcome replayD out
1: Collect one cooperative rollout
2: Compute native return and advantage inputs
3: Extract attributable future-collaborator outcomes
4: Add retained samples(xj t,u j t,j,y j t)toD out
5:ifoutcome-model readiness condition is satisfiedthen
6: UpdateψusingL out
7: ¯ψ←(1−ρ) ¯ψ+ρψ
8:end if
9: Construct acquisition targets for eligible earlier participants
10:ifreceiver-supervision readiness condition is satisfiedthen
11: Construct receiver targets usingp ¯ψ
12:end if
13:ifBis MAPPOthen
14:foreach actorido
15: Apply the native MAPPO actor update toi
16: Apply the eligible SPL actor update toi
17:end for
18: Update the centralized critic
19:else ifBis IPPOthen
20:foreach actorido
21: Apply the native IPPO actor update toi
22: Apply the eligible SPL actor update toi
23: Update the local critic ofi
24:end for
25:else ifBis HAPPOthen
26: Initialize cumulative factorF←1
27: Select the HAPPO actor-update order
28:foreach actoriin the selected orderdo
29: Store the current factorFfor actori
30: Evaluate the pre-update action probabilities
31: Apply the native HAPPO actor update toi
32: Apply the eligible SPL actor update toi
33: Evaluate the post-update action probabilities
34: Update the cumulative factorF
35:end for
36: Update the centralized critic
37:end if
38:returnupdated policies, critics, outcome models, and replay
B.8. Eight-Agent Scaling Protocol
Experimental scope.The eight-agent scaling study evaluates MPE-Advanced and RWARE-Advanced
withfourearlierparticipants P0, . . . ,P3,fourfuturecollaborators R0, . . . ,R 3,andsixteencandidatetasks.
We evaluate Non-overlap, Dynamic, and Cascaded participation using MAPPO and SPL-MAPPO. Non-
overlap and Dynamic are trained for two million environment steps, while Cascaded uses four million
steps to accommodate its extended participation horizon; all configurations use three independent
training runs.
Environment configuration.The sixteen candidate tasks form four groups of four, with two valid
tasks sampled in each group. In MPE-Advanced, balanced task shards are randomly assigned at reset
and the earlier-participant–future-collaborator correspondence is randomly assigned at handoff. This
31

Cooperating with Future Collaborators: Multi-Agent RL under Staggered Participation
Table B.6: Task and evidence configuration for the eight-agent scaling experiments. The notationx×4 denotes
four repetitions of valuex.
Setting MPE-Advanced RWARE-Advanced
Earlier participants 4 4
Future collaborators 4 4
Candidate tasks 16 16
Fixed valid tasks 8 8
Valid tasks / four-task group 2 2
Validity priors(0.80 ×4, 0.65×4, 0.35×4, 0.20×4)
Probe budget / earlier participant 5 6
Probe limit / task 2 2
Probe accuracy 0.85 0.85
Publication delay 5 5
Execution budget / future collaborator 2 2
Valid-task value(12 ×4, 10×4, 8×4, 6×4)1
Probe cost 0.20 0.01
Invalid-execution cost 8.00 0.25
correspondence is not available to earlier participants beforehand. Earlier participants and future
collaborators spawn on opposite sides of the environment atx=−1.82 and x=1.82 , respectively,
with
y∈ {0.76, 0.2533,−0.2533,−0.76}.
The agent speed, view radius, interaction radius, and placement jitter are1.0, 4.0, 0.18, and 0.02.
Each actor observation has dimension 339, and the MAPPO critic input concatenates the eight actor
observations, giving dimension 2712. Hidden task validity is unavailable to both representations.
RWARE-Advanced uses one shelf row, three shelf columns of height eight, and sensor range one.
Candidate task identifiers are permuted each episode, future collaborators select from a shared
candidate pool, and competing claims are resolved by first arrival. Hidden task validity is excluded
from both actor observations and the MAPPO critic input.
Temporal participation schedules.All participation intervals follow the half-open convention
[tstart,t end). Let H denote the ordinary episode horizon,a the nominal handoff time,d the maxi-
mum Dynamic deviation, andHcas the Cascaded horizon. Table B.7 summarizes the corresponding
values.
Table B.7: Temporal parameters and aggregate role exposure for the eight-agent experiments. Exposure is
measured in agent-steps per episode.
DomainH a d H cas Earlier Future
MPE-Advanced 125 45 11 500 180 320
RWARE-Advanced 500 200 50 2000 800 1200
For Non-overlap,
I Pi non = [0,a),I Ri non = [a,H),i∈ {0, 1, 2, 3}.(B.5)
32

Cooperating with Future Collaborators: Multi-Agent RL under Staggered Participation
For Dynamic participation, two independent deviations are sampled per episode,
δk ∼Unif{−d, . . . ,d},k∈ {0, 1},(B.6)
with paired handoffs
h2k =a+δ k,h 2k+1 =a−δ k.(B.7)
The corresponding intervals are
I Pi dyn = [0,hi),I Ri dyn = [hi,H).(B.8)
The handoff vector is sampled each episode and included in the actor-visible schedule information.
Since ∑︀3 i=0 hi =4a, Dynamic preserves the same aggregate role exposure as Non-overlap.
For Cascaded participation,
I Pi cas = [iH,iH+a),I Ri cas = [iH+a,(i+1)H),i∈ {0, 1, 2, 3}.(B.9)
The resulting horizon isHcas =4H , preserving aggregate role exposure while distributing the four
earlier-participant–future-collaborator pairs across successive intervals.
Training and evaluation.The eight-agent MAPPO and SPL-MAPPO runs use the feed-forward
architecture, PPO settings, and SPL-specific hyperparameters reported in Table B.5. Policies are not
parameter-shared and recurrent policies are disabled. Non-overlap and Dynamic are trained for two
million environment steps, whereas Cascaded is trained for four million steps; each configuration uses
three independent runs and is evaluated over 200 final episodes per run. MPE-Advanced uses eight
parallel rollout environments, whereas RWARE-Advanced uses one. Reported task-completion results
use the final checkpoint at the corresponding training budget, without performance-based checkpoint
selection.
C. Observed Training Cost
We report observed wall-clock training time as a practical indication of computational cost. Measure-
ments correspond to completed full-budget runs; short qualification and smoke-scale runs are excluded.
Because experiments ran under varying system load and host hardware was not recorded consistently,
these values are descriptive runtime measurements. They are not controlled hardware-throughput
benchmarks or estimates of algorithmic complexity.
Table C.1 summarizes the observed training time. In the primary four-agent experiments, all methods
use two million environment steps, and Table C.1(a) reports mean minutes per completed run averaged
over the ten settings formed by two environment variants and five participation patterns. Table C.1(b)
reports the eight-agent scaling and Isaac Lab experiments. The eight-agent Non-overlap and Dynamic
settings use 2M environment steps, whereas Cascaded uses 4M. The two- and four-agent Isaac Lab
settings use approximately 2.0M and 3.0M steps, respectively.
Observation.The practical training-time effect of SPL varies across environments and team configu-
rations. In the primary four-agent experiments, SPL incurs moderate additional wall-clock cost for most
PPO backbones, while MAPPO and SPL-MAPPO are nearly identical in RWARE. In the eight-agent exper-
iments, the relative increase is modest in MPE and larger in RWARE; absolute times across participation
patterns should be interpreted together with their different training budgets, particularly the 4M-step
33

Cooperating with Future Collaborators: Multi-Agent RL under Staggered Participation
Table C.1: Observed wall-clock training time in minutes. Primary four-agent values are averages across the ten
environment–participation settings in each domain; scaling and Isaac Lab values are mean± standard error
over three independent runs. Light blue shading identifies SPL results.
(a) Primary four-agent experiments.
Method MPE RWARE
IPPO 154.1 166.4
SPL-IPPO 175.3 177.9
MAPPO 114.0 128.3
SPL-MAPPO 131.1 129.6
HAPPO 134.6 128.5
SPL-HAPPO 152.4 145.2
MAE-MAPPO 157.2 128.6
Sable 205.1 210.8
SMPE2 119.2 218.0
(b) Scaling and Isaac Lab experiments.
Setting Participation Steps MAPPO SPL-MAPPO
MPE-Adv. (8) Non-overlap 2.00M76.0±0.2 87.0±0.1
Dynamic 2.00M89.5±0.6 103.0±0.5
Cascaded 4.00M175.5±0.2 185.5±2.7
RWARE-Adv. (8) Non-overlap 2.00M242.9±6.1 396.9±15.3
Dynamic 2.00M216.6±3.6 377.5±11.0
Cascaded 4.00M453.6±16.6 538.3±15.4
Isaac Lab (2) Non-overlap 2.00M548.8±17.5 562.9±18.8
Dynamic 2.00M438.1±9.9 450.0±7.0
Isaac Lab (4) Non-overlap 3.01M1090.2±17.8 1244.7±43.2
Dynamic 3.01M1120.1±15.1 1295.0±7.3
Cascaded settings. The two-agent Isaac Lab runs show only a small difference, whereas the four-agent
settings require approximately 14–16% more observed training time with SPL-MAPPO. Overall, SPL
introduces additional training-time computation whose magnitude depends on the environment and
configuration, while decentralized execution remains unchanged.
D. Detailed Experiment Results
The following tables provide the complete evaluation metrics underlying the main-paper results.
Task completion (TC) measures the percentage of required downstream task objectives successfully
completed within an evaluation episode, while full success (FS) is the percentage of episodes in which
all required downstream tasks are completed. We also report episode return and failed execution (FE).
Higher values are better for TC, FS, and return, whereas lower FE is better. MPE and RWARE values
are reported as mean± standard error over five independent training seeds and 200 final evaluation
episodes per seed. A reported standard error of0.00 indicates that the five seed-level evaluation means
are exactly identical at full precision; further discussion is provided in Appendix D.7.
D.1. MPE-Base
Table D.1 reports the complete MPE-Base results across the five participation patterns, including task
completion, full success, return, and failed execution.
34

Cooperating with Future Collaborators: Multi-Agent RL under Staggered Participation
Table D.1: Complete MPE-Base four-agent results at 2M environment steps. Values are mean± standard error
over five independent training seeds and 200 final evaluation episodes per seed. Bold marks the best reported
mean in each participation–metric row. For legacy MPE-Base Non-overlap HARL runs, FS is recovered from the
retained per-episode completed-task counts using the same all-four-tasks definition.
Participation Metric IPPO MAPPO HAPPO Other baselines
Vanilla SPL Vanilla SPL Vanilla SPL MAE-MAPPO Sable SMPE 2
Non-overlap
TC (%)↑70.50±0.00 78.38±0.38 70.50±0.00 78.73±0.43 67.45±3.05 79.18±0.2370.50±0.00 62.70±0.25 42.73±9.29
FS (%)↑17.50±0.00 31.80±0.87 17.50±0.00 32.80±1.06 14.00±3.50 34.20±0.4917.50±0.00 9.00±0.71 4.20±2.57
Return↑21.569±0.029 27.337±0.083 21.644±0.036 27.231±0.091 21.010±0.675 27.409±0.04821.747±0.076 15.100±0.199 11.016±2.409
FE↓1.125±0.000 0.582±0.0081.127±0.002 0.610±0.012 1.056±0.069 0.608±0.004 1.125±0.000 1.450±0.011 0.873±0.232
Overlap-25
TC (%)↑68.25±2.75 79.35±0.57 70.78±0.14 80.25±0.21 70.70±0.18 80.35±0.2967.93±2.95 63.50±2.24 53.85±5.43
FS (%)↑14.90±2.60 34.10±1.45 17.50±0.00 36.80±0.4617.50±0.16 36.40±0.81 14.00±3.38 9.30±2.22 4.30±2.53
Return↑20.308±1.009 27.068±0.212 21.521±0.082 27.232±0.139 21.439±0.174 27.358±0.12220.950±0.554 15.295±1.868 12.778±2.124
FE↓1.124±0.036 0.654±0.0091.161±0.007 0.670±0.014 1.159±0.010 0.658±0.017 1.079±0.079 1.460±0.090 1.246±0.236
Overlap-50
TC (%)↑67.85±3.15 78.90±0.3169.53±1.27 78.90±0.2469.80±0.92 78.50±0.47 70.63±0.23 64.43±1.85 63.95±3.34
FS (%)↑14.00±3.50 32.20±0.6015.70±1.36 31.90±0.71 16.20±0.97 30.70±1.11 17.50±0.16 10.30±2.12 10.60±3.20
Return↑20.744±0.680 26.429±0.112 21.213±0.287 26.569±0.09821.228±0.340 26.125±0.134 21.353±0.166 15.888±1.503 15.529±2.966
FE↓1.086±0.074 0.731±0.003 1.136±0.033 0.715±0.0081.148±0.009 0.748±0.003 1.161±0.010 1.422±0.074 1.442±0.133
Dynamic
TC (%)↑66.20±3.01 79.65±0.1870.23±0.59 78.88±0.18 69.53±0.99 79.63±0.39 64.85±3.06 58.30±1.11 49.70±1.04
FS (%)↑12.60±3.43 35.30±0.51 16.70±0.80 33.60±0.43 16.30±1.20 35.60±1.1411.20±3.39 5.30±0.58 0.60±0.60
Return↑20.694±0.600 27.643±0.09021.364±0.232 27.306±0.124 21.153±0.367 27.499±0.146 20.613±0.613 13.970±0.839 12.579±1.591
FE↓1.003±0.079 0.599±0.0091.125±0.010 0.610±0.012 1.119±0.015 0.610±0.014 0.963±0.077 1.318±0.038 1.022±0.139
Cascaded
TC (%)↑66.83±3.68 78.90±0.70 70.63±0.10 78.93±0.4870.68±0.19 78.78±0.22 70.45±0.05 38.03±0.93 27.93±5.74
FS (%)↑14.00±3.50 33.70±1.7917.50±0.00 33.50±0.85 17.40±0.10 33.00±0.57 17.50±0.00 0.50±0.32 0.20±0.20
Return↑20.872±0.753 27.563±0.259 21.529±0.060 27.447±0.207 21.502±0.048 27.581±0.05921.642±0.047 9.745±0.861 6.875±2.668
FE↓1.040±0.085 0.577±0.0151.138±0.004 0.590±0.018 1.144±0.008 0.578±0.014 1.127±0.002 0.850±0.058 0.650±0.059
Observation.Across all five participation patterns, SPL improves TC, FS, and return while reducing
FE relative to the matched Vanilla backbone. The improvement is consistent across IPPO, MAPPO, and
HAPPO, indicating that the additional gains are not specific to a single PPO-based backbone.
D.2. MPE-Advanced
Table D.2 reports the corresponding results in MPE-Advanced, where task assignments, spawn configu-
rations, and future-collaborator identities vary across episodes.
35

Cooperating with Future Collaborators: Multi-Agent RL under Staggered Participation
Table D.2: Complete MPE-Advanced four-agent results at 2M environment steps. Values are mean± standard
error over five independent training seeds and 200 final evaluation episodes per seed. Bold marks the best
reported mean in each participation–metric row.
Participation Metric IPPO MAPPO HAPPO Other baselines
Vanilla SPL Vanilla SPL Vanilla SPL MAE-MAPPO Sable SMPE 2
Non-overlap
TC (%)↑70.38±0.00 77.95±0.19 64.08±3.86 78.23±0.1667.28±3.10 78.03±0.16 63.28±3.47 64.90±1.36 49.78±3.25
FS (%)↑19.00±0.00 30.50±0.65 11.40±4.65 31.90±0.6215.20±3.80 31.10±0.53 10.60±4.35 10.80±1.41 1.60±1.09
Return↑21.485±0.135 27.229±0.092 19.986±0.847 27.390±0.10620.754±0.645 27.328±0.076 19.939±0.798 16.683±1.085 10.730±2.269
FE↓1.125±0.000 0.589±0.008 0.989±0.083 0.579±0.0071.056±0.069 0.580±0.006 0.971±0.078 1.369±0.057 1.238±0.256
Overlap-25
TC (%)↑65.65±3.53 79.95±0.5268.28±1.50 79.38±0.27 70.93±0.56 79.55±0.40 71.40±0.23 64.30±1.63 47.83±9.02
FS (%)↑12.60±4.28 35.50±0.5716.60±1.27 33.80±0.73 18.70±0.80 34.50±1.21 19.30±0.20 10.50±2.20 5.20±4.17
Return↑20.343±0.734 27.536±0.23520.611±0.494 27.244±0.139 21.634±0.205 27.502±0.185 21.967±0.120 15.589±1.238 13.152±2.718
FE↓1.011±0.077 0.622±0.012 1.101±0.027 0.641±0.007 1.126±0.016 0.611±0.0121.131±0.004 1.427±0.066 0.901±0.255
Overlap-50
TC (%)↑71.30±0.22 78.63±0.23 68.58±3.05 78.33±0.40 71.40±0.14 78.68±0.2562.63±5.92 61.88±1.48 52.08±8.25
FS (%)↑19.20±0.30 31.90±0.60 15.80±3.70 31.10±1.11 19.40±0.10 32.10±0.7612.00±4.60 9.10±1.20 6.10±4.23
Return↑21.669±0.083 26.481±0.08421.005±0.701 26.358±0.171 21.567±0.090 26.446±0.097 19.743±1.443 13.716±1.266 13.018±3.412
FE↓1.124±0.007 0.713±0.0071.069±0.066 0.715±0.010 1.143±0.006 0.721±0.005 0.958±0.115 1.525±0.059 1.139±0.067
Dynamic
TC (%)↑66.63±3.66 78.23±0.29 67.05±3.20 79.08±0.5461.73±5.55 78.80±0.18 67.68±1.76 57.60±1.30 43.10±6.61
FS (%)↑14.70±3.68 32.30±0.64 14.70±3.68 34.10±1.38 11.10±4.53 34.20±0.6415.60±2.42 6.50±1.10 0.00±0.00
Return↑20.509±0.893 27.006±0.131 20.770±0.681 27.312±0.258 19.867±1.215 27.330±0.08120.936±0.420 14.027±1.018 13.678±2.577
FE↓1.037±0.072 0.608±0.005 1.047±0.064 0.608±0.013 0.915±0.123 0.596±0.0121.047±0.038 1.272±0.052 0.608±0.083
Cascaded
TC (%)↑67.68±2.58 76.80±0.13 67.28±3.10 77.00±0.33 69.28±1.10 77.23±0.1866.83±3.02 62.73±0.98 56.70±5.50
FS (%)↑15.90±3.10 29.00±0.45 15.20±3.80 29.20±0.68 17.80±1.20 30.70±0.7214.80±3.72 8.30±1.66 7.10±3.72
Return↑20.895±0.638 25.976±0.072 20.623±0.661 25.988±0.143 21.038±0.238 26.033±0.10020.707±0.662 14.706±0.811 18.650±1.423
FE↓1.065±0.055 0.734±0.0061.056±0.069 0.742±0.007 1.101±0.024 0.741±0.007 1.043±0.067 1.457±0.035 0.795±0.108
Observation.The same pattern persists under the additional structural variation of MPE-Advanced.
SPL improves all four reported metrics for every matched backbone–participation comparison, while
the three SPL backbones remain close in final performance.
D.3. RWARE-Base
Table D.3 reports the complete RWARE-Base results across the five participation patterns.
Table D.3: Complete RWARE-Base four-agent results at 2M environment steps. Values are mean± standard error
over five independent training seeds and 200 final evaluation episodes per seed. Bold marks the best reported
mean in each participation–metric row.
Participation Metric IPPO MAPPO HAPPO Other baselines
Vanilla SPL Vanilla SPL Vanilla SPL MAE-MAPPO Sable SMPE 2
Non-overlap
TC (%)↑66.45±5.86 86.83±0.40 71.38±2.27 86.70±0.49 73.18±1.50 86.93±0.2673.48±1.69 71.80±0.98 66.05±3.29
FS (%)↑14.50±6.27 53.80±1.68 19.50±4.14 53.70±1.46 19.20±3.09 54.00±0.5721.30±2.28 20.00±1.30 14.10±3.61
Return↑2.342±0.226 3.292±0.018 2.548±0.101 3.286±0.023 2.618±0.070 3.297±0.0102.641±0.072 2.471±0.049 2.301±0.164
FE↓0.848±0.088 0.494±0.013 1.075±0.110 0.503±0.019 1.064±0.057 0.483±0.0111.003±0.068 1.128±0.039 1.358±0.131
Overlap-25
TC (%)↑81.10±3.41 89.15±0.1674.25±3.41 89.08±0.35 70.15±2.93 88.35±0.50 72.50±2.86 76.70±1.18 67.28±2.87
FS (%)↑38.60±7.30 61.00±0.3225.90±7.18 60.60±0.94 16.60±4.20 58.80±1.95 19.20±5.35 28.10±3.03 16.00±2.83
Return↑2.960±0.157 3.404±0.0082.667±0.157 3.401±0.018 2.500±0.131 3.369±0.023 2.633±0.105 2.720±0.056 2.358±0.145
FE↓0.728±0.142 0.411±0.011 0.935±0.165 0.410±0.0181.075±0.092 0.424±0.014 0.877±0.114 0.932±0.047 1.309±0.115
Overlap-50
TC (%)↑82.00±1.12 89.00±0.1974.73±3.35 88.58±0.28 70.28±2.41 88.80±0.23 77.53±0.72 77.23±1.97 61.95±4.09
FS (%)↑41.80±1.74 59.40±0.68 24.60±6.55 59.30±0.94 15.20±3.03 59.70±0.8030.20±1.32 31.20±4.47 10.10±4.15
Return↑3.008±0.052 3.397±0.0102.706±0.153 3.375±0.013 2.487±0.112 3.388±0.011 2.834±0.033 2.741±0.099 2.143±0.175
FE↓0.686±0.037 0.414±0.0100.979±0.144 0.432±0.009 1.184±0.099 0.415±0.009 0.858±0.039 0.911±0.079 1.322±0.150
Dynamic
TC (%)↑72.88±1.19 88.88±0.2765.35±5.46 88.70±0.30 68.80±4.06 88.40±0.42 72.28±1.51 74.63±1.22 62.03±4.29
FS (%)↑19.30±1.56 60.10±0.8114.50±5.14 58.70±1.20 16.30±4.89 58.40±1.37 18.90±2.62 24.70±2.72 10.20±4.07
Return↑2.579±0.041 3.389±0.0132.304±0.211 3.385±0.014 2.425±0.199 3.368±0.020 2.572±0.072 2.616±0.058 2.095±0.215
FE↓0.910±0.118 0.423±0.007 1.119±0.129 0.415±0.0061.166±0.203 0.438±0.014 1.106±0.061 1.015±0.049 1.519±0.172
Cascaded
TC (%)↑66.80±1.98 86.25±0.38 67.53±2.05 86.75±0.5066.58±2.24 85.95±0.79 71.63±0.73 76.83±0.93 64.18±2.94
FS (%)↑13.20±2.83 52.40±1.07 11.80±3.64 53.60±1.0211.90±2.64 51.50±1.67 18.70±0.97 28.80±1.97 11.00±3.67
Return↑2.346±0.097 3.281±0.014 2.417±0.074 3.299±0.0232.322±0.110 3.269±0.032 2.573±0.031 2.721±0.047 2.207±0.146
FE↓1.298±0.079 0.456±0.012 1.095±0.141 0.466±0.011 1.333±0.088 0.448±0.0081.135±0.029 0.927±0.037 1.433±0.118
36

Cooperating with Future Collaborators: Multi-Agent RL under Staggered Participation
Observation.SPL produces larger gains in RWARE than in MPE, particularly in FS and FE. The
increase in full success indicates that higher task completion is accompanied by more episodes in which
the cooperative objective is completed in full.
D.4. RWARE-Advanced
Table D.4 reports the results in RWARE-Advanced, which additionally includes task permutation, a
shared candidate pool, and dynamic task claims.
Table D.4: Complete RWARE-Advanced four-agent results at 2M environment steps. Values are mean± standard
error over five independent training seeds and 200 final evaluation episodes per seed. Bold marks the best
reported mean in each participation–metric row.
Participation Metric IPPO MAPPO HAPPO Other baselines
Vanilla SPL Vanilla SPL Vanilla SPL MAE-MAPPO Sable SMPE 2
Non-overlap
TC (%)↑52.08±1.37 79.93±0.59 58.63±2.31 80.03±0.2357.58±3.44 79.55±0.79 58.50±2.20 50.70±0.32 45.70±0.25
FS (%)↑2.60±0.58 40.60±0.87 4.70±0.93 42.20±1.445.70±1.79 38.70±1.71 4.30±1.19 1.60±0.19 1.20±0.62
Return↑1.654±0.059 2.950±0.026 1.972±0.096 2.951±0.0101.891±0.144 2.928±0.030 1.951±0.099 1.510±0.017 1.346±0.022
FE↓1.573±0.043 0.577±0.0131.174±0.098 0.583±0.011 1.386±0.115 0.599±0.020 1.330±0.119 1.660±0.019 1.882±0.025
Overlap-25
TC (%)↑64.18±1.62 83.23±0.47 68.83±1.40 83.65±0.32 63.28±1.98 83.73±0.4864.70±1.81 54.75±0.44 47.68±0.66
FS (%)↑7.00±0.84 42.30±0.94 11.60±1.27 44.50±1.017.60±1.64 43.50±2.11 8.40±1.71 1.80±0.34 1.00±0.42
Return↑2.175±0.062 3.069±0.023 2.360±0.066 3.092±0.016 2.122±0.086 3.095±0.0202.193±0.087 1.636±0.021 1.331±0.045
FE↓1.316±0.054 0.590±0.017 1.159±0.061 0.567±0.018 1.368±0.073 0.566±0.0111.256±0.100 1.770±0.013 2.007±0.039
Overlap-50
TC (%)↑70.35±1.28 84.55±0.6968.05±4.14 84.45±0.33 67.50±2.12 84.43±0.56 72.88±1.05 58.88±0.77 47.05±0.38
FS (%)↑13.40±1.51 45.90±1.9212.40±3.67 45.20±0.77 11.70±3.14 45.10±1.78 17.50±1.31 4.90±0.33 0.80±0.49
Return↑2.437±0.056 3.124±0.0342.344±0.184 3.122±0.017 2.327±0.104 3.120±0.024 2.566±0.051 1.836±0.039 1.340±0.015
FE↓1.118±0.056 0.587±0.026 1.209±0.156 0.574±0.0151.141±0.124 0.574±0.0111.002±0.037 1.629±0.035 2.054±0.020
Dynamic
TC (%)↑66.60±1.95 81.30±0.34 62.55±2.83 82.50±0.4363.23±0.83 82.20±0.16 65.90±2.33 56.30±0.49 47.55±0.40
FS (%)↑11.60±2.43 39.30±0.64 8.50±2.32 42.80±0.727.90±0.93 41.20±0.78 11.10±1.87 3.80±0.64 0.60±0.40
Return↑2.282±0.084 2.995±0.014 2.090±0.124 3.048±0.0182.162±0.041 3.031±0.006 2.269±0.098 1.713±0.024 1.353±0.035
FE↓1.122±0.077 0.590±0.004 1.351±0.114 0.564±0.0141.207±0.046 0.586±0.015 1.147±0.086 1.705±0.025 2.054±0.031
Cascaded
TC (%)↑58.95±1.70 85.40±0.42 65.55±1.76 85.98±0.4466.03±2.06 84.90±0.51 64.18±3.98 54.90±1.08 47.03±0.55
FS (%)↑4.10±0.87 46.00±1.17 8.60±1.76 48.30±1.549.50±2.13 44.80±1.85 9.40±2.50 2.70±0.37 0.60±0.19
Return↑1.936±0.076 3.153±0.021 2.194±0.078 3.182±0.0212.226±0.093 3.126±0.026 2.150±0.167 1.625±0.054 1.339±0.035
FE↓1.539±0.115 0.573±0.017 1.368±0.070 0.547±0.0141.317±0.077 0.599±0.021 1.331±0.130 1.804±0.043 2.119±0.022
Observation.The greatest improvements appear in RWARE-Advanced, where downstream decisions
depend more strongly on the available task-relevant evidence. SPL increases TC, FS, and return and
reduces FE across every matched backbone and participation pattern.
D.5. Additional Isaac Lab Metrics
Table D.5 reports the complete Isaac Lab evaluation, including task completion (TC), full success (FS),
episode return, failed execution (FE), map coverage, task discovery, and wall-penetration steps. These
additional diagnostics complement the TC results reported in the main paper and provide a broader
view of the behaviors induced by SPL-MAPPO under embodied UAV–UGV execution.
Task performance.SPL-MAPPO achieves higher TC, FS, and return in all four team-size–participation
settings. For the two-agent system, TC increases from31.50% to 61.58% under Non-overlap and from
36.67% to 59.58% under Dynamic participation. The corresponding FS gains are also substantial,
increasing from 5.17% to 35.17% and from 9.00% to 34.50%. The same pattern persists with four
agents: TC increases from55.79% to 76.38% under Non-overlap and from58.46% to 79.25% under
Dynamic participation, while FS increases from11.83% to 39.83% and from12.17% to 44.83%. Episode
return follows the same direction in all four settings.
37

Cooperating with Future Collaborators: Multi-Agent RL under Staggered Participation
Table D.5: Isaac Lab evaluation metrics. Values are mean± standard error over three independent training seeds
and 200 final evaluation episodes per seed.
Agents Metric Non-overlap Dynamic
MAPPO SPL-MAPPO MAPPO SPL-MAPPO
2
TC (%)↑31.50±5.97 61.58±0.6736.67±0.71 59.58±1.79
FS (%)↑5.17±3.03 35.17±0.739.00±0.76 34.50±2.29
Return↑0.648±0.147 1.540±0.0160.785±0.022 1.494±0.059
FE↓0.632±0.057 0.822±0.009 0.798±0.003 0.760±0.038
Map coverage (%)↑36.21±1.69 44.03±0.1733.21±1.60 44.03±1.07
Tasks discovered↑0.238±0.009 0.287±0.0030.150±0.020 0.261±0.016
Wall-penetration steps↓0.000±0.000 0.000±0.000 0.000±0.000 0.000±0.000
4
TC (%)↑55.79±3.23 76.38±1.5258.46±3.40 79.25±1.30
FS (%)↑11.83±4.69 39.83±3.2212.17±4.21 44.83±1.17
Return↑2.235±0.172 3.330±0.0922.343±0.174 3.499±0.064
FE↓1.100±0.016 1.167±0.0271.160±0.023 1.193±0.020
Map coverage (%)↑67.96±1.45 54.90±0.3669.25±1.59 53.84±0.76
Tasks discovered↑0.470±0.022 0.200±0.0070.512±0.041 0.190±0.009
Wall-penetration steps↓0.000±0.000 0.000±0.000 0.000±0.000 0.000±0.000
Execution and exploration diagnostics.FE does not change uniformly with SPL. In the two-agent
setting it is higher under Non-overlap and slightly lower under Dynamic participation, while in the
four-agent setting it is slightly higher under both schedules. These absolute FE values occur under
substantially different exploration and task-discovery behavior and should therefore be interpreted
together with those diagnostics.
The exploration pattern also differs with team size. With two agents, SPL-MAPPO attains greater map
coverage and discovers more tasks under both participation schedules. For example, under Dynamic
participation, map coverage increases from33.21% to 44.03%, while task discovery increases from0.150
to 0.261. This pattern is consistent with broader evidence acquisition. With four agents, SPL-MAPPO
exhibits the opposite exploration pattern: map coverage decreases from67.96% to 54.90% under Non-
overlap and from69.25% to 53.84% under Dynamic participation, while task discovery also decreases.
Despite this reduced exploration, SPL-MAPPO achieves higher TC, FS, and return in both four-agent
settings. This is consistent with more selective acquisition and/or more effective use of the available
task-relevant evidence, although the reported diagnostics do not separate these effects causally.
No wall-penetration steps are observed for either method in any of the four settings, indicating that
the performance differences reported above are not accompanied by violations of this physical-safety
diagnostic.
D.6. Prior-Misspecification Robustness
SPLusestask-familyvaliditypriorsaspartofthestructuredmodelforprospectiveacquisitionsupervision.
We therefore evaluate how sensitive SPL is to misspecification of these priors. The true environment
distribution is kept unchanged, and only the validity priors assumed by the acquisition model are
perturbed. Let
p= (0.80, 0.80, 0.65, 0.65, 0.35, 0.35, 0.20, 0.20)
38

Cooperating with Future Collaborators: Multi-Agent RL under Staggered Participation
denote the nominal prior vector. For misspecification levelλ∈[0, 1] , the acquisition model instead uses
̂︀pλ = (1−λ)p+λ(1−p).(D.1)
Thus, λ=0 recovers the nominal priors,λ=0.5 produces an uninformative prior of0.5 for every task,
and λ=1 fully reverses the nominal prior ordering. All other structured information, including the
fixed-valid-task constraint, probe observation model, task utilities, environment dynamics, and receiver
learning procedure, remains unchanged.
We evaluate SPL-MAPPO under Non-overlap participation in MPE-Advanced and RWARE-Advanced.
Each misspecified condition uses five independent training seeds, two million environment steps, and
200 final evaluation episodes per seed, matching the primary four-agent protocol. Theλ=0 values cor-
respond to the nominal SPL-MAPPO results reported in the main experiments; theλ∈ {0.25, 0.50, 1.00}
conditions comprise 30 additional training runs. In all misspecified runs, the environment continues to
sample tasks from the nominal prior distribution inp.
Table D.6: Sensitivity of SPL-MAPPO to misspecified validity priors under Non-overlap participation. Values are
mean ± standard error over five training seeds and 200 final evaluation episodes per seed. The environment
always uses the nominal prior distribution; only the acquisition model useŝ︀pλ.
Environmentλ TC (%)↑ FS (%)↑ Return↑ FE↓
MPE-Advanced
0.00 78.23±0.16 31.90±0.62 27.390±0.106 0.579±0.007
0.25 77.70±0.39 30.70±0.80 27.02±0.15 0.560±0.006
0.50 76.43±0.11 29.90±0.33 26.70±0.10 0.557±0.009
1.00 76.73±0.21 29.80±0.72 26.59±0.05 0.612±0.007
RWARE-Advanced
0.00 80.03±0.23 42.20±1.44 2.951±0.010 0.583±0.011
0.25 79.93±0.68 39.70±1.59 2.947±0.028 0.586±0.011
0.50 78.35±0.94 33.90±1.43 2.888±0.040 0.666±0.023
1.00 77.45±0.56 35.50±1.15 2.826±0.023 0.652±0.007
Observation.Prior misspecification reduces performance relative to the nominal SPL configuration,
but does not cause a collapse in task completion in either tested environment. With fully reversed
priors (λ=1 ), SPL-MAPPO achieves76.73% TC in MPE-Advanced and77.45% in RWARE-Advanced,
compared with nominal values of78.23% and 80.03%, respectively. These values also remain above the
corresponding Vanilla MAPPO means of64.08%and58.63%reported in the main experiments.
The effect is not strictly monotonic in MPE-Advanced, where TC atλ=1 is slightly higher than at
λ=0.5 . RWARE-Advanced shows a clearer reduction in TC as the assumed prior becomes less accurate,
while full success is more sensitive than TC: FS decreases from42.20% in the nominal setting to33.90%
at λ=0.5 and 35.50% at λ=1 . These results indicate that SPL retains substantial task-completion
performance under validity-prior misspecification in the tested settings, while stricter episode-level
success can be more sensitive.
This experiment perturbs only the validity priors used by the acquisition model. The fixed-valid-task
constraint, probe accuracy, task utilities, and other elements of the structured task model remain cor-
rectly specified. Accordingly, the results provide evidence of tolerance to validity-prior misspecification
in the tested settings. Robustness to arbitrary errors in the full structured task model is not established.
39

Cooperating with Future Collaborators: Multi-Agent RL under Staggered Participation
D.7. Statistical Analysis of Primary Comparisons
We conduct a retrospective statistical analysis of the 60 primary Vanilla–SPL comparisons reported in
the main paper. Each trained policy is summarized by its mean task completion (TC) over 200 final
evaluation episodes, and independent training seeds are treated as the statistical replication units.
Throughout this subsection,∆TC denotes the absolute difference between percentage-valued SPL and
Vanilla TC means,TCSPL −TC Vanilla, and is reported using %.
Same-training-seed pairing is available for 57 of the 60 configurations, providing five paired seed-level
differences in each testable configuration. For these comparisons, we report the mean paired difference,
a two-sided paired Studentt test with four degrees of freedom, and a pointwise 95%t confidence
interval. The Non-overlap MAPPO comparisons in MPE-Advanced, RWARE-Base, and RWARE-Advanced
use different Vanilla and SPL training-seed sets. Their observed five-seed method means remain
available for descriptive comparison, but no paired confidence interval or pairedp-value is reported.
To account for multiplicity, we apply Holm correction over the declared family of all 60 primary
comparisons at familywise level0.05. The three configurations without verified seed pairing are
assigned p=1 internally for the correction and are displayed as unavailable below. This preserves the
original 60-comparison family and yields a conservative adjustment. Pointwise confidence intervals
are not multiplicity-adjusted.
Table D.7: Retrospective statistical analysis for MPE-Base. Each training seed is a replication unit.∆TC is the
absolute SPL-minus-Vanilla difference in percentage-valued TC scores. Confidence intervals are pointwise 95%
intervals from five paired training seeds. Holmp values are adjusted over the declared family of 60 primary
comparisons.
Participation Backbone∆TC (%) 95% CI (%) RawpHolmp
Non-overlap IPPO 7.88 [6.82, 8.93]3.17×10 −5 0.0017
MAPPO 8.23 [7.03, 9.42]4.48×10 −5 0.0023
HAPPO 11.73 [3.01, 20.44] 0.0202 0.3028
Overlap-25 IPPO 11.10 [2.11, 20.09] 0.0266 0.3073
MAPPO 9.48 [8.74, 10.21]3.56×10 −6 2.10×10 −4
HAPPO 9.65 [8.86, 10.44]4.61×10 −6 2.67×10 −4
Overlap-50 IPPO 11.05 [2.81, 19.29] 0.0204 0.3028
MAPPO 9.38 [5.41, 13.34] 0.0028 0.0752
HAPPO 8.70 [6.28, 11.12]5.65×10 −4 0.0237
Dynamic IPPO 13.45 [5.36, 21.54] 0.0099 0.2081
MAPPO 8.65 [7.41, 9.89]4.24×10 −5 0.0022
HAPPO 10.10 [6.97, 13.23]8.59×10 −4 0.0326
Cascaded IPPO 12.08 [2.41, 21.74] 0.0256 0.3073
MAPPO 8.30 [7.06, 9.54]5.01×10 −5 0.0025
HAPPO 8.10 [7.25, 8.95]1.23×10 −5 7.01×10 −4
40

Cooperating with Future Collaborators: Multi-Agent RL under Staggered Participation
Table D.8: Retrospective statistical analysis for MPE-Advanced. Notation and statistical procedure follow Table D.7.
The Non-overlap MAPPO comparison uses different Vanilla and SPL training-seed sets; its∆TC is therefore
descriptive and paired inference is unavailable.
Participation Backbone∆TC (%) 95% CI (%) RawpHolmp
Non-overlap IPPO 7.58 [7.05, 8.10]2.26×10 −6 1.36×10 −4
MAPPO 14.15 – – –
HAPPO 10.75 [2.06, 19.44] 0.0264 0.3073
Overlap-25 IPPO 14.30 [5.25, 23.35] 0.0118 0.2358
MAPPO 11.10 [7.48, 14.72] 0.0010 0.0378
HAPPO 8.63 [6.13, 11.12]6.59×10 −4 0.0264
Overlap-50 IPPO 7.33 [6.43, 8.22]2.23×10 −5 0.0012
MAPPO 9.75 [1.26, 18.24] 0.0332 0.3073
HAPPO 7.28 [6.31, 8.24]3.09×10 −5 0.0017
Dynamic IPPO 11.60 [0.73, 22.47] 0.0414 0.3073
MAPPO 12.03 [3.78, 20.27] 0.0155 0.2784
HAPPO 17.08 [1.68, 32.47] 0.0370 0.3073
Cascaded IPPO 9.13 [1.73, 16.52] 0.0266 0.3073
MAPPO 9.73 [0.98, 18.47] 0.0366 0.3073
HAPPO 7.95 [5.10, 10.80] 0.0015 0.0492
– indicates that paired inference is unavailable because Vanilla and SPL use different training-seed sets. The corresponding
untestable comparison is assignedp=1internally for the 60-comparison Holm correction.
Table D.9: Retrospective statistical analysis for RWARE-Base. Notation and statistical procedure follow Table D.7.
The Non-overlap MAPPO comparison uses different Vanilla and SPL training-seed sets; its∆TC is descriptive and
paired inference is unavailable.
Participation Backbone∆TC (%) 95% CI (%) RawpHolmp
Non-overlap IPPO 20.38 [4.50, 36.25] 0.0235 0.3056
MAPPO 15.33 – – –
HAPPO 13.75 [9.92, 17.58]5.67×10 −4 0.0237
Overlap-25 IPPO 8.05 [-1.30, 17.40] 0.0751 0.3073
MAPPO 14.83 [6.33, 23.32] 0.0084 0.1842
HAPPO 18.20 [9.60, 26.80] 0.0042 0.1049
Overlap-50 IPPO 7.00 [3.73, 10.27] 0.0040 0.1043
MAPPO 13.85 [4.26, 23.44] 0.0160 0.2784
HAPPO 18.53 [12.18, 24.87] 0.0013 0.0440
Dynamic IPPO 16.00 [12.30, 19.70]2.76×10 −4 0.0124
MAPPO 23.35 [7.88, 38.82] 0.0138 0.2624
HAPPO 19.60 [8.63, 30.57] 0.0077 0.1774
Cascaded IPPO 19.45 [13.18, 25.72] 0.0010 0.0371
MAPPO 19.23 [12.63, 25.82] 0.0013 0.0440
HAPPO 19.38 [11.51, 27.24] 0.0024 0.0693
41

Cooperating with Future Collaborators: Multi-Agent RL under Staggered Participation
Table D.10: Retrospective statistical analysis for RWARE-Advanced. Notation and statistical procedure follow
Table D.7. The Non-overlap MAPPO comparison uses different Vanilla and SPL training-seed sets; its∆TC is
descriptive and paired inference is unavailable.
Participation Backbone∆TC (%) 95% CI (%) RawpHolmp
Non-overlap IPPO 27.85 [23.14, 32.56]8.06×10 −5 0.0040
MAPPO 21.40 – – –
HAPPO 21.98 [11.18, 32.77] 0.0048 0.1160
Overlap-25 IPPO 19.05 [14.95, 23.15]2.08×10 −4 0.0096
MAPPO 14.83 [11.13, 18.52]3.71×10 −4 0.0163
HAPPO 20.45 [16.11, 24.79]1.98×10 −4 0.0093
Overlap-50 IPPO 14.20 [9.08, 19.32] 0.0015 0.0492
MAPPO 16.40 [4.79, 28.01] 0.0172 0.2784
HAPPO 16.93 [10.26, 23.59] 0.0021 0.0639
Dynamic IPPO 14.70 [8.73, 20.67] 0.0024 0.0693
MAPPO 19.95 [12.23, 27.67] 0.0020 0.0620
HAPPO 18.98 [16.46, 21.49]3.05×10 −5 0.0017
Cascaded IPPO 26.45 [21.10, 31.80]1.63×10 −4 0.0078
MAPPO 20.43 [15.09, 25.76]4.43×10 −4 0.0190
HAPPO 18.88 [13.19, 24.56]7.69×10 −4 0.0300
Summary.SPL has a higher observed mean TC than its corresponding Vanilla backbone in all 60
primary configurations. The equal-weight descriptive mean difference across these configurations is
14.09%; the corresponding backbone-level mean differences are13.93%, 14.02%, and 14.33% for IPPO,
MAPPO, and HAPPO, respectively. Among the 57 configurations with paired inference, 56 pointwise
95% confidence intervals have a positive lower bound. The single exception is RWARE-Base Overlap-25
with IPPO, whose pointwise interval is[−1.30, 17.40]%. After Holm correction over the declared family
of 60 comparisons, 29 configurations remain significant at familywise level0.05, while 28 testable
comparisons do not. The three remaining configurations have no paired test because same-training-seed
pairing is unavailable.
These results distinguish descriptive consistency from multiplicity-adjusted statistical evidence. Higher
observed SPL means occur in all 60 configurations, but this does not imply that all 60 comparisons are
individually statistically significant. Similarly, failure to reject the null hypothesis after Holm correction
should not be interpreted as evidence of equivalence between SPL and the corresponding Vanilla
method.
Evaluation design and zero standard errors.Final evaluation uses deterministic policies and a fixed
set of 200 reset seeds within each environment protocol, reused across training seeds and methods.
This controls variation due to the sampled evaluation instances while retaining independent policy
training across training seeds.
Four TC cells in the primary results table have an exact seed-level standard error of zero. These
are Vanilla IPPO and Vanilla MAPPO under MPE-Base Non-overlap, MAE-MAPPO under MPE-Base
Non-overlap, and Vanilla IPPO under MPE-Advanced Non-overlap. In each case, the five independently
trained policies produce exactly identical 200-episode mean TC values at full precision. The reported
zero therefore concerns variability among the five seed-level evaluation means; it does not imply that
individual evaluation episodes have zero variability. The available records establish this numerical
42

Cooperating with Future Collaborators: Multi-Agent RL under Staggered Participation
plateau under the fixed deterministic evaluation schedule but do not establish a particular behavioral
mechanism responsible for it.
Limitations of the statistical analysis.This analysis is retrospective and was conducted on the
existing completed runs without additional training or evaluation. The paired tests treat the five
training seeds as independent replications and assume that the seed-level differences are approximately
normally distributed. With only five pairs per configuration, this normality assumption cannot be
assessed convincingly. Furthermore, because the same fixed evaluation-instance schedule is reused
across training seeds and methods, the reported inference is conditional on this evaluation design and
does not quantify uncertainty over an unrestricted distribution of deployment tasks.
The three Non-overlap MAPPO configurations without verified same-seed pairing prevent a complete
60-comparison paired analysis. Assigning these unavailable testsp=1 internally makes the reported
Holm correction conservative while preserving the declared family size, but does not replace the
missing paired evidence. Pointwise confidence intervals should also be interpreted separately from the
Holm-adjusted hypothesis tests.
43
