---
title: 'Generalized Agent Iteration: One Formal Framework for Iterative Policy Improvement and Recursive
  Self-Improvement'
url: https://arxiv.org/abs/2609.13406
category: ai-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Hongyao Tang
- Yi Ma
- Pengyi Li
- Yifu Yuan
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.13406
pages: 16
chars: 65175
fetched_at: '2026-11-08T13:31:58+00:00'
kb_version: 1
---

# Generalized Agent Iteration: One Formal Framework for Iterative Policy Improvement and Recursive Self-Improvement

Generalized Agent Iteration: One Formal Framework for
Iterative Policy Improvement and Recursive Self-Improvement
Hongyao Tang1 Yi Ma1,2 Pengyi Li1 Yifu Yuan1
1Tianjin University, 2Shanxi University
✉Contact: tanghongyao@tju.edu.cn
Abstract.When we speak of recursive self-improvement (RSI), are we speaking of a phenomenon, a
mechanism, or a prospect? Towards autonomous and evolving intelligence, RSI is being claimed at
many scales, while no single framework that formally describes these emerging instances exists. Its
counterpart in the classical realm, iterative policy improvement, is characterized by generalized policy
iteration (GPI), a framework of broad applicability with well-understood theoretical properties, but
only where the update principle and the evaluation base lie outside the agent. In this paper, we propose
Generalized Agent Iteration (GAI), a formal framework that describes iterative policy improvement and
RSI as two cases of a single learning paradigm. GAI defines the agent as a configuration of modifiable
components within a system and models the learning process as a cycle ofagent evaluationandagent
improvement. Two pivotal dials then distinguish the instances, in particular the systems that self-identify
as RSI in recent work: whether the improving mechanism is part of the agent and whether the standard
it is measured against is grounded outside it. The former dial delineates the boundary between GPI
and RSI, and the latter determines a system’s polarity as anchored, goal drift, or fully self-referential.
Moreover, we use these coordinates to place existing systems on the same two axes and make the defects
of recursive self-improvement statable one condition at a time. We see this paper as a first step toward
exploring a formal characterization of RSI that rests on the classical account, makes existing systems
comparable, and provides a principled basis for analyzing and designing new ones.
1 Introduction
Self-improvement is an old yet persistent ambition in artificial intelligence. It is the premise of Good’s
ultraintelligent machine, the last invention that human beings would need to make (Good, 1965), and the
engine of the later accounts in which a system that improves its own improvement mechanism compounds into
a rapid rise in capability (Yudkowsky, 2013). How such systems are built, and where they fail, is therefore
worth stating precisely.
Nowadays, self-improvement is claimed at many scales: agents that refine their own outputs (Madaan et al.,
2023; Shinn et al., 2023); systems that rewrite the routine that improves them, from code-level self-modification
(Robeyns et al., 2025; Zelikman et al., 2023) to self-referential agent frameworks (Kakade et al., 2026; Yin et al.,
2024; Zhang et al., 2025, 2026); research loops that search programs or experiments under fixed evaluators (Lu
et al., 2024; Novikov et al., 2025); and, at the far end, systems that co-evolve the standard they are judged by
(Iacob et al., 2026) or propose to do without one (Schaul, 2024). A recent survey of the area observes that
such labels are used loosely, for ambitions that differ substantially (Chen et al., 2026). Existing works in this
space describe themselves as recursive self-improvement (RSI); we call themself-identified RSI, orRSI-labeled
for short. What is missing isa criterion rather than another example: a learning-paradigm account that
separates genuine recursive self-improvement from systems that only carry the label, and says what changes
once they do. The classical counterpart of this pursuit is iterative policy improvement, for which generalized
policy iteration (GPI) is the formal framework: in a finite MDP, its alternation of evaluation and improvement
converges to an optimal policy (Sutton and Barto, 2018). GPI assumes that the improvement mechanism and
the reward both lie outside the agent; in the recursive case they do not, and no account of comparable scope
exists (Chen et al., 2026; Zhang, 2026).
In this paper, we propose a new formal framework calledGeneralized Agent Iteration (GAI)with the
aim of describing iterative policy improvement and RSI as two cases of a single learning paradigm. Beyond
Apparently, Generalized Agent Iteration is a salute to the Generalized Policy Iteration (Sutton and Barto, 2018, Section 4.6,
pp. 104–105).
1
arXiv:2609.13406v2  [cs.AI]  29 Oct 2026

Generalized Agent Iteration: One Formal Framework for Iterative Policy Improvement and Recursive Self-Improvement
these two cases, it is meant to cover contemporary agent-based learning systems, whose improving components
take the form of code, parameters, or harness, and can be edited (Gao et al., 2025). Concretely, we first define
the agent within a learning system as a configuration of modifiable system components. In analogy with the
alternating iteration of GPI, we present the learning paradigm of GAI as a cyclic iteration of two operations:
♦Agent evaluation: multifaceted critics score the agent part against an evaluation base.
♦Agent improvement: the modifier proposes a new agent instance that the system adopts.
Specific instances of GAI then depend mainly on two open choices, which we call thetwo dials:Dial1 ,
whether the mechanism that improves the agent is part of the agent itself, andDial2 , whether the standard
that improvement is measured against is grounded outside the agent. The first dial admits two settings: in
GPI the mechanism that improves the agent stays external, and in recursive self-improvement it becomes part
of the agent. This dial decides which RSI-labeled systems are RSI in the GAI sense and which are GPI. In
GPI the second dial is fixed as well, with the reward supplied by the world. The setting of the second dial
then determines thepolarityof self-improvement: anchored, when the standard remains fixed outside the
agent; goal drift, when the agent can rewrite it; and fully self-referential, when no external standard remains.
Further, we position existing self-improvement systems on the two dials, from the Gödel machine and its
descendants to co-evolving evaluators and closed-system proposals. Lastly, we collect the defects of the settings
that leave the anchored end, and state the scope and the open questions that remain.
The main content is summarized below:
• We propose a single formal framework that describes both iterative policy improvement and recursive
self-improvement as two cases of a single learning paradigm defined by GAI.
• We provide a way of understanding both classical and contemporary learning systems through positioning
the two dials and agent components under GAI.
• We present four defects of recursive self-improvement, each tied to a condition of classical GPI that a
self-improving system violates.
The remainder of this paper is organized as follows. Section 2 introduces the background of classical GPI,
existing RSI works, and etc. We deliver the GAI framework in Section 3, along with its connection to
representative self-improvement systems in Section 4. We present the defects of recursive self-improvement in
Section 5, and close in Section 6.
2 Background
ReinforcementLearningandGeneralizedPolicyIteration(GPI)Reinforcementlearning(Suttonand
Barto, 2018) is usually formalized as a Markov decision process (MDP)(S,A,p,r,γ ): a policyπ:S→ ∆(A)
selects actions, and its value is the expected discounted returnVπ(s) = E [∑ t≥0γtr(St,At)|S 0 =s, At∼
π(·|S t)
]
, with an action-valueQπ(s,a )conditioning on the first action. Generalized policy iteration (GPI) is
the shared structure of most single-agent algorithms:evaluationmoves the value toward consistency with
the current policy,V→V π, andimprovementmoves the policy toward being better in that value, with
π→greedy(V)the canonical case, as Figure 1 illustrates.
What makes the frameworkgeneralizedis that neither step is tied to a concrete implementation: evaluation
may be a Bellman backup, a temporal-difference or Monte-Carlo update, or any operator that drives a value
estimate toward agreement with a policy, and improvement may be greedy but equally softmax, truncated, or
any operator that yields a policy preferred by the current value. Because only the interaction of an evaluation
and an improvement matters, GPI is a general description of a broad range of iterative policy-optimization
systems, from dynamic programming to model-free reinforcement learning, and even of such systems when
they are not framed as reinforcement learning at all.
Recursive Self-Improvement AgentsThe literature uses recursive self-improvement for the prospect
that a system improves the very mechanism by which it improves, an idea that dates to Good’s ultraintelligent
machine (Good, 1965) and grounds seed AI (Yudkowsky, 2013), the instrumental-drive view (Omohundro,
2008), and formal distinctions between self-modification, self-improvement, and recursive self-improvement
2

Generalized Agent Iteration: One Formal Framework for Iterative Policy Improvement and Recursive Self-Improvement
policyπ
valueV
evaluation
V→V π
improvement
π→greedy(V)
Figure 1Generalized policy iteration as a cycle: evaluation moves the value toward consistency with the
current policy (V→V π); improvement moves the policy toward being greedy in the value (π→greedy (V )).
Each step may be partial and interleaved (Sutton and Barto, 2018).
(Nivel et al., 2013; Yampolskiy, 2015). Its formal formulation is the Gödel machine (Schmidhuber, 2003, 2007),
a self-referential program that may rewrite any part of itself whenever it can prove that the rewrite raises
a fixed external utility. Because proof search is intractable, practical descendants trade proof for empirical
validation: the Gödel Agent (Yin et al., 2024) pairs a language agent’s policy with a self-modifiable learning
algorithm that validates each rewrite on a benchmark; the Darwin Gödel Machine (Zhang et al., 2025) adds
archive-based open-ended search; Polaris (Kakade et al., 2026) targets small models via auditable policy repair;
and the Red Queen Gödel Machine (Iacob et al., 2026) co-evolves the evaluator under changing objectives.
Even code-level descendants such as the Self-Improving Coding Agent (SICA) (Robeyns et al., 2025) rewrite
their own implementation, yet validate each change against an external coding benchmark with no gradient
update.
A parallel, largely empirical line refines today’s language agents in closed loops without retraining: Self-Refine
(Madaan et al., 2023) and Reflexion (Shinn et al., 2023) improve an agent’s own outputs, and coding agents
such as STOP (Zelikman et al., 2023) modify their own implementation. At the scale of a research loop,
AlphaEvolve searches programs under fixed evaluators (Novikov et al., 2025) and the AI Scientist runs
idea-to-paper cycles (Lu et al., 2024). One survey organizes such systems by what evolves, be it parameters,
prompts, memory, tools, or scaffolds (Gao et al., 2025), and another separates bounded self-refinement, which is
convergent and evaluable, from open-ended recursive self-improvement, ordering candidate verification signals
from formal verifiers down to intrinsic self-assessment (Chen et al., 2026). As deployed, these RSI-labeled
loops, and the scaffold self-modifiers above, keep some component fixed outside the loop, be it model weights,
a prompt template, an outer loop, or a verifier; the agent then improves within, but not beyond, that fixed
mechanism, so the attainable quality is bounded by it. Most such loops are therefore instances of bounded
self-improvement inside a fixed mechanism. What the literature calls strong RSI is, under GAI, the case in
which the improver is an agent component; that is the first dial (Zhang, 2026).
The Absence of a Unified Formal FrameworkA recent roadmap survey grades self-improvement
systems by how much of the improvement responsibility the AI internalizes, from executing human-specified
updates to revising the mechanism that governs later improvement (Duan et al., 2026). Taken together, these
strands still lack a unified formal account in which GPI is a special case, recursive self-improvement is a
nearby and definable case, and the guarantees of the former can be located, one by one, as they fail when the
underlying scheme is made self-referential. Existing terminologies, such as Gödel agents, meta-learning, and
agentic loops, do not make explicit that these processes live on one continuum. We develop such an account
in the next section.
The classical methods and the self-improvement systems above differ along two informal axes that we formalize
in the next section: whether the mechanism that improves the agent lies inside the agent, and whether the
standard that improvement is measured against stays grounded. Table 1 places a few representative methods
on these axes as a preview.
3

Generalized Agent Iteration: One Formal Framework for Iterative Policy Improvement and Recursive Self-Improvement
Table 1A schematic preview of classical policy-iteration methods and of self-improvement agents along three
axes, two of which the next section formalizes as dials: what the method modifies, whether its improvement
mechanism lies inside the agent, and whether its evaluation basis is fixed outside it.
Method 0 Modification 1 Improvement
Mechanism
2 Evaluation Basis Guarantee
Policy / value
iteration (Sutton
and Barto, 2018)
•policy
•value
external, fixed (greedy;
Bellman backup)
environment reward converges to an
optimal policy
DQN (Mnih
et al., 2013) •deep Q-network (action values)
•implicit greedy
policy
external, fixed
(temporal-difference
update; greedy)
environment reward no exact guarantee
under function
approximation
Reflexion /
Self-Refine
(Madaan et al.,
2023; Shinn et al.,
2023)
•own outputs
•reflection memory
external, fixed (retry
loop; the model rewrites
its own output)
task feedback /
self-critique
empirical gains,
bounded by the
fixed loop
STOP (Zelikman
et al., 2023) •own optimizer (for code generation) internal (the optimizer rewrites itself) validation examples empirical gains
Gödel Agent /
Darwin Gödel
Machine (Yin
et al., 2024;
Zhang et al.,
2025)
•own code
•policy and
improvement
mechanism
•open-ended archive
search (Darwin)
internal (the
self-modification routine
is modifiable)
external benchmark each rewrite
empirically
validated
Red Queen Gödel
Machine (Iacob
et al., 2026)
•the agent
•its evaluator
internal (the agent and
its evaluator co-evolve)
co-evolving evaluator;
no fixed external basis
no guarantee
relative to a fixed
external basis
3 The Generalized Agent Iteration (GAI) Framework
Although GPI describes a broad class of policy-improvement methods, it fails to describe the more complex
systems that improve recursively, in which the mechanism that improves the agent is itself part of what the
agent can change. To this end, we propose a formal framework, which we call Generalized Agent Iteration
(GAI), a learning paradigm that extends GPI to describe agent-based learning systems whose improving
components can themselves be edited. GAI keeps the alternating cycle of evaluation and improvement at its
center, and treats GPI and recursive self-improvement as two instances of it. The two instances differ in two
choices, which we call thetwo dialsof the framework:1 whether the mechanism that improves the agent lies
inside the agent, and2 whether the standard that improvement is measured against stays grounded in what
lies outside it.
The rest of this section turns the two dials into formal definitions: it defines the system and the agent
(Section 3.1) and reads GPI and recursive self-improvement as two settings of the dials (Section 3.2). It
closes by characterizing the polarity of self-improvement and reducing recursive self-improvement back to GPI
(Section 3.3).
3.1 The Self-Improving System and Agent
A self-improving system acts in a world and is measured against a goal. We keep the world as a Markov
decision processW = (S,A,p,r,γ ), and writeG for an external goal that the system is expected to serve.
Both belong to the environment, and neither is part of the system itself.
The objective of the system is to serve the external goalG, whose scalar instance in the world is the rewardr.
4

Generalized Agent Iteration: One Formal Framework for Iterative Policy Improvement and Recursive Self-Improvement
The configuration that serves it best is
χ⋆∈arg max
χ∈X
E
[∑
t≥0γtr(St,At) ⏐⏐⏐χ ] ,(1)
This objective is fixed by the world and the goal alone, not by the system itself. More generally, the world and
the goal may change over time on their own; we hold both fixed in what follows, since such changes originate
outside the system and leave the analysis below unaffected.
Remark 1 (goalG in the world v.s., self-proposed tasks).Some self-improving systems have the
agent propose its own tasks, questions, or goals as a means of learning. We treat this as a particular
form of agent improvement, since such self-set tasks remain subordinate to an external goal that is
objective and cannot be edited by the agent.
Let χ be a system made of components, withO ={π,V,m,U,ρ} the set of components andCo the content
space of componento; the system then lies in the spaceχ∈X = ∏ o∈OCo. Let Ag⊆O be the set of
components that form the agent; an agent instance is an assignmentξ∈X Ag =∏ o∈AgCo of contents to these
components. Moreover, we writeχ[ξ]for the system obtained by replacing the agent part ofχ with ξ. We use
∆(Y) to denote the set of probability distributions over a spaceY. We define the system and its agent as
follows.
Definition 1 (System and Agent).Over an external worldW = (S,A,p,r,γ )and a goal G, a
system is a configurationχ= (π,V,m,U,ρ), a tuple of the current contents of five components:
•π:S→∆(A): thepolicythat chooses world actions;
•V:S→R: theaction criticthat evaluates how wellπacts;
•m:X→∆(X Ag): themodifierthat proposes how the system should change;
•U:X→R: themodification criticthat evaluates whether a proposed change servesG;
•ρ: theevaluation base, the standard that the critics measure against.
All five roles belong to a system; an instance may leave some of them unused, as the modification critic
U is when the modifier is fixed. The agent is the modifiable parts inside the system. Its membership
varies across systems, such asAg ={π,V} when the modifier is fixed, orAg ={π,V,m,U,ρ} when
the system may also rewrite its modifier and even the evaluation standard.
Remark 2 (roles and substrates).The five components are functional roles, not objects:π acts, V
and U score, m produces the changes, andρ is the standard. Systems edit substrates, such as prompts,
memory, tools, weights, or code; a substrate is one realization of a role, read through the role whose
content it changes. A policy may be realized entirely as code, with no model at deployment (Hu et al.,
2026).
Substrate Read as
weights; prompts, memory, tools, skillsπ: how the agent acts
training data, curricula, collected experience material for the nextπ
trainer, optimizer, scheduler, task proposerm: what produces the changes
evaluator, test sets, release rules the standard (V,U,ρ)
sandbox, schemas, type contracts constraints onm
an artifact that no role reads or writes the world, outside the system
One role may span several substrates, and one substrate may carry several roles: a memory store holds
a tool description in one entry, an acceptance criterion in another. The dials read roles rather than
substrates, so three surfaces (Tan et al., 2026) or nine (Duan et al., 2026) are read the same way, and
the tuple may be extended with further components.
Remark 3 (the interior of the modifier).The modifier is a functional role, and its content may
be a pipeline: a proposer of tasks or questions to learn from, a store of the resulting experience, and
a trainer that turns the experience into the next agent instance, together with a schedule over these
parts. A self-training loop, in which the system sets its own tasks, collects the experience, and learns
5

Generalized Agent Iteration: One Formal Framework for Iterative Policy Improvement and Recursive Self-Improvement
policyπ
criticV/U modifierm(evaluation baseρ)
environment
and goal
evaluation
feedback
evaluation
improvement
improvement
improvement:
modifier may
rewrite itself
Figure 2Generalized agent iteration as a cycle of policy, critic, and modifier. The critic evaluates the policy
and the modifier against the baseρ and returns feedback; the modifier then produces improvements, including
possible rewrites of the critics and itself (gray dashed, conditional on the setting; the dash-dot border of the
modifier marks that it belongs to the agent only whenm∈Ag ). With the modifier fixed outside the agent
the cycle reduces to GPI (Figure 1); with the modifier inside the agent it is recursive self-improvement.
from it, is read as a modifier of this kind, and whether that modifier is itself an agent component is the
question of the first dial below, not of its internal organization. Grading the interior, for instance by
how many of these decisions the system makes, is the work of the level-based accounts discussed in
Section 4, and it leaves both dials unaffected. Self-proposed tasks move the second dial only through
the standard that scores the changes they produce.
Definition 1 fixes the content of a system but not how it evolves. We next define the process by which a
system changes over time.
Definition 2 (Generalized Agent Iteration).A generalized agent iteration is a process that
alternates two operations on the agent part of a system:
• Agent evaluation: the critic in use scores the agent part against the evaluation baseρ, withV at
the policy level andUat the agent level;
• Agent improvement: the modifier produces a new agent instance,ξ∼m (·|χ ), which the system
adopts,χ←χ[ξ].
Definition 1 leaves two choices open: whether the mechanism that improves the agent is among these
components, and what the evaluation base points at. These are the two dials of the framework, and each
formalizes one way in which GPI and recursive self-improvement differ.
1 First dial: whether the mechanism that improves the agent lies inside the agent.The agent
changes only through the modifier: at each stepm draws a new agent instanceξ∼m (·|χ ), and the system
moves toχ[ξ].
• If m /∈Ag, its content is fixed andm acts as an external improvement mechanism, the abstract
evaluation-and-improvement operator that GPI iterates.
• Ifm∈Ag , the system may rewrite its own modifier, so recursion closes atm with no external meta-layer.
2 Second dial: whether the standard that improvement is measured against stays grounded.
Each evaluation regresses toward a standard, its evaluation base; we treat this base as a single standardρ
and write its instancesρV and ρU only where the two critics must be told apart. The base is a component
of the system, and what the second dial asks about is where its content comes from and whether the agent
may rewrite it. An evaluation isgroundedwhen its base draws its content from outside the system, the world
and the goal, and when the base itself lies outside the agent. The agent then cannot rewrite the standard
6

Generalized Agent Iteration: One Formal Framework for Iterative Policy Improvement and Recursive Self-Improvement
it is measured against. A base that draws its content from outside but that the agent may rewrite can
move under the system’s own edits; a base with no external content at all constrains the loop by nothing
beyond self-consistency. In a system that improves recursively, what matters is whether the base that its
self-improvement is measured against stays grounded, which we examine in later subsections.
Running Example (a learning coding agent).Consider an agent that writes code, whose
configuration isχ = (π,V,m,U,ρ ): the policyπ generates candidate solutions, the action criticV scores
them against the current tests, the modifierm proposes changes to the agent, such as rewriting the
prompt that drives the policy or the routine by which the agent revises its own solutions, and the
modification criticU evaluates each proposed change. We keep this agent as the concrete referent for
the roles above, and read off its two dial settings below.
3.2 GPI and Recursive Self-Improvement as Two GAI Instances (Dial 1)
We now re-introduce GPI and recursive self-improvement as two instances of the system definition in the
previous subsection. They differ only in how the two dials are set: for GPI the modifier lies outside the agent
and the evaluation base is grounded in the world reward; for recursive self-improvement the modifier is itself
an agent component. Everything else in the description is shared.
GPI as the anchored instance.The agent consists of the policy and the action critic,Ag ={π,V} , and
the modifier is not part of the agent,m /∈Ag. The content ofm is fixed to an evaluation operator and an
improvement operator, writtenEm andIm to mark that the update principle is the content ofm; sincem is
fixed, both operators are fixed as well. Throughmthe agent changes componentwise as
V← E m(V,π;ρ V )(evaluation), π← I m(V)(improvement),(2)
whilem itself is unchanged. The only evaluation in use is the action critic; the modification criticU is present
but not exercised, sincem is fixed and no alternative modification is scored. The baseρV of the action
critic is grounded, with content the world rewardr. WhenEm is policy evaluation andIm is greedy, the two
updates form exactly policy or value iteration, which in a finite MDP converges to an optimal policyπ⋆ under
standard assumptions. The objective of Equation (1) is then maximized by that same policy, with the action
critic at its valueVπ⋆ .
Recursive self-improvement as the self-modifying instance.Now the modifier is part of the agent,
m∈Ag , canonically Ag ={π,V,m,U} . This is the GAI sense of RSI: the location of the improver, not the
object it improves, is the criterion. The step is unchanged and now reads
policy update:V← E m(V,π;ρ V ), π← I m(V)
agent update:ξ∼m(·|χ), χ←χ[ξ], m ′←(ξ) m, U ′←(ξ) U (3)
The operators in the first line are subscripted bym to mark that they are decided by the current modifier
rather than fixed externally: the policy-level updates of GPI become, in RSI, content thatm may realize.
The second line is the recursion itself:(ξ)m and( ξ)U are the modifier and modification-critic slots of the
proposal, so the next modifier and the next critic are produced by the current one, recursion closes atm,
and no external meta-layer updates it. Every agent component changes only throughm, andm may run the
GPI-style alternation above, but it may equally rewrite itself, replace its critic, or change the rule by which it
chooses. Our definition leaves the second dial, whether the base that governs this recursion stays grounded,
open; different self-improvement systems adopt different choices, and we examine the consequences next.
The reference ideal of a self-improver.Nothing in this description guarantees thatmimproves toward
anything external; improving is a property ofm’s content, not of the framework. Ifm improves toward its
base, its content(m,U )must satisfy a pair of self-consistency conditions, which we state as a reference ideal.
WriteρU(χ,ξ)for the value that the base assigns to adopting agent instanceξfromχ. Then
7

Generalized Agent Iteration: One Formal Framework for Iterative Policy Improvement and Recursive Self-Improvement
Table 2Polarity of self-improvement for systems with the modifier in the agent, determined by the state of
the evaluation baseρ; the last column lists representative systems.
Polarity State ofρConsequence Representative systems
Anchored external content,
ρ /∈Ag, so the agent
cannot rewrite it
Improves toward a fixed
external standard; a
modifier satisfying the
self-consistency conditions
above tracks it.
Gödel machine (Schmidhuber,
2007); STOP (Zelikman et al.,
2023); MetaRSI (Tan et al.,
2026)
Goal Drift external content, but
ρ∈Ag, so the agent
may rewrite it
The standard itself can be
rewritten, so
self-improvement can drift
away from the external goal.
Red Queen Gödel Machine
(Iacob et al., 2026)
Fully
Self-Referential
no external content:
empty, orρdepends
onU
No external signal reaches
the self-improvement loop,
and the critic equation
reduces to internal
self-consistency.
Socratic learning (Schaul, 2024)
(position paper)
agent evaluation:U(χ) =E ξ∼m(·|χ)
[
ρU(χ,ξ) +γU
(
χ[ξ]
)]
agent improvement:suppm(·|χ)⊆arg max
ξ∈XAg
[
ρU(χ,ξ) +γU
(
χ[ξ]
)] (4)
where the first condition calibrates the modification critic to the base and the second requires the modifier to
propose only agent instances that improve in the critic’s estimate. These are characterization conditions, not
enforced updates: they describe the internal structure a self-improver must have, and no external mechanism
guarantees them. Whether the base that appears here is grounded is the polarity question we turn to next.
Running Example (Anchored Learning v.s., Recursive Self-Improvement).The coding agent
above realizes the two instances just described.
• Anchored learning (GPI style).The agent isAg ={π,V} , andm is a fixed external update
routine, for instance a PPO-style loop (Schulman et al., 2017) that trains the policy against the
reward of passing its unit tests. The system improves within the routine but cannot change the
routine itself.
• Recursive self-improvement.The agent isAg ={π,V,m,U} , and the proposalξ that m draws
carries the next modifier, so the system may rewrite the very routine that improves it. STOP is
one concrete instance, in which the improvement routine rewrites its own code against a fixed set of
validation examples (Zelikman et al., 2023).
3.3 Polarity of Self-Improvement: Anchored, Goal Drift, and Fully Self-Referential (Dial 2)
The second dial applies to the base of the action critic and to the base of the modification critic alike. It
separates polarities only when the modifier is part of the agent: in GPI the modification critic is never
exercised, so the only base in use is that of the action critic, grounded in the world reward, and the polarity
entry for GPI is Anchored. Form∈Ag , the second dial decides thepolarityof self-improvement, namely
whether the evaluation baseρstays grounded; Table 2 lists the three states it can take.
Remark 4 (learned proxies).An external judge or reward model is anchored, whatever data it was
trained on: the dial asks where the standard sits, not how faithful it is to the goal. A proxy can be
anchored and still be satisfied without serving the goal; the same judge as an agent component is the
Goal Drift case.
The rows of Table 2 are ordered by how much anchoring remains. The middle row is namedGoal Driftfor the
8

Generalized Agent Iteration: One Formal Framework for Iterative Policy Improvement and Recursive Self-Improvement
drift of the system away from its fixed goal, not for a change in the goal itself: what moves is the standard
that measures progress toward it. In current practice, most demonstrated RSI systems fall into the Anchored
row; the two lower rows are so far represented mainly by boundary cases and by position papers.
The two dials, taken together, place every instance. Setting the modifier outside the agent and fixing the only
base in use to the world reward gives the GPI loop withAg ={π,V} , of which the PPO-trained coding agent
in the running example is an instance. Keeping the modifier inside the agent while keepingρ grounded gives
anchored recursive self-improvement, as in STOP, with its fixed validation examples, or the Gödel machine,
whose proof gate restricts which rewrites are tried. Lettingρ enter the agent, or vanish or point at itself,
gives the unanchored end, whose consequences we examine after mapping existing systems onto the dials.
Freezing the modifier as an external procedure and removing the modification critic and its baseρU recover
the classical loop over policy and value.
4 Connections to Existing Self-Improvement Systems
The two dials of the previous section give the main families discussed in Section 21, and the recent systems
that extend them, a uniform reading. The reading is the GAI classification, not a report of the literature’s
labels: several RSI-labeled systems keep the modifier outside the agent and fall into the fixed-outer-loop row.
We state that reading here for the fixed-loop practice that dominates current work, for the closest formal
counterpart of recursive self-improvement, and for the empirical families that follow it; Table 3 summarizes it.
1 Fixed Outer LoopsA large body of practice improves a model or a harness inside a pipeline whose
control loop is fixed by its designers: proposal, update, and selection are scripted, and the system cannot
change the loop itself (Gao et al., 2025). Research loops such as AlphaEvolve and the AI Scientist are the
same setting: the search is scripted and the evaluator is fixed (Lu et al., 2024; Novikov et al., 2025). This is
the Anchored setting with the modifier frozen outside the agent: the mechanism of improvement is not itself
changed. The first row of Table 3 is the special case in which the agent holds the policy and its action critic;
in the pipelines above, the agent is typically a single optimized object, a model or a harness. Recent systems
fill out the setting and sharpen a distinction that the literature blurs. Dream-RSI improves the policy that
steers its search while the revision loop, the underlying agent, and the evaluator stay fixed, and its guarantee
that the revised policy is never worse on the replay score is monotonicity of the classical kind, available
exactly because the modifier and the base both sit outside the agent (Zheng et al., 2026). The literature
calls this meta-layer self-improvement, since the object it improves governs later improvements. GAI has
no separate meta-layer setting: the first dial asks who produces the changes, so a system that improves a
meta-level object remains a fixed outer loop as long as the producer stays fixed. NeoHorse-1 runs one pass
of a fixed post-training pipeline on traces of its own deployment, measured on a held-out suite (NeoHorse
Team et al., 2026). SoL-Pi scales this loop over 535 environments and freezes candidates before a held-out
evaluation that never flows back (Liu et al., 2026). Terminal-RSI fixes its five-stage schedule (Yang et al.,
2026), and The Trinity keeps its Creator and Evolver outside the evaluated harness under a fixed topology
(Tang et al., 2026); under GAI both are fixed outer loops, not RSI in the GAI sense. The same reading covers
the recent embodied systems: a policy written entirely as code by an offline coding agent (Hu et al., 2026) and
a weight-level adaptation driven by simulated rollouts under fixed round and data quotas (Lang et al., 2026)
keep both the improver and the base outside the agent, and join this family rather than adding a setting.
2 The Gödel Machine and Its DescendantsThe Gödel machine (Schmidhuber, 2003, 2007) is the
closest formal neighbor: a program that may rewrite any part of itself when it proves that the rewrite raises a
fixed external utility. In the present terms it is an anchored self-improver: the modifier lies in the agent, the
base is the external utility, and a proof gate restricts which rewrites are admissible. The Gödel-agent family
keeps the pattern while replacing proof with empirical validation: these systems rewrite their own code or
harness and are judged on a benchmark that stays outside the agent, so they also sit in the Anchored row
(Kakade et al., 2026; Robeyns et al., 2025; Srikanth et al., 2026; Yin et al., 2024; Zelikman et al., 2023; Zhang
et al., 2025). Memento 3 freezes the underlying model and accepts a rulebook or world-model revision only
when replay reproduces the observations (Zhao et al., 2026a). Hyperagents goes further: it places the task
1Output-level refinement loops such as Reflexion and Self-Refine are outside Table 3: the optimized object is the output, not
an agent component, and the base is the model’s own critique.
9

Generalized Agent Iteration: One Formal Framework for Iterative Policy Improvement and Recursive Self-Improvement
Table 3Existing systems under the GAI reading: the agent set, whether the modifier is modifiable (Dial 1),
the resulting polarity and evaluation base (Dial 2), and the classification. The fixed-outer-loop row includes
RSI-labeled systems; under GAI their modifier stays outside the agent. The evaluator of the Red Queen row
is the modification criticU, which is an agent component whenever it is modifiable.
System AgentAg
Dial 1
mmodifiable?
Dial 2
Polarity Classification
Policy/value
iteration, PPO
(Schulman et al.,
2017; Sutton and
Barto, 2018)
{π,V}no;mis the fixed update
principle (Bellman backup
and greedy improvement; the
clipped policy update for
PPO)
Anchored; the evaluation base
is the environment reward
(Anchored) GPI
Fixed outer loops
(Gao et al., 2025;
Hu et al., 2026;
Lang et al., 2026;
Liu et al., 2026;
NeoHorse Team
et al., 2026; Tang
et al., 2026; Yang
et al., 2026; Zheng
et al., 2026)
the optimized
object (πor a
harness)
no; the outer loop is fixed by
its designers
Anchored; the evaluation base
is the objective or validation
metric set outside
(Anchored) GPI
Gödel machine
(Schmidhuber,
2003, 2007)
{π,m}(solver and
its rewriter)
yes;m is the rewriting routine
that edits the program when a
proof succeeds
Anchored; the evaluation base
is a fixed external utility, with
a proof gate on rewrites
Anchored RSI
(guarded)
Gödel Agent,
Darwin Gödel
Machine, STOP,
SICA, Polaris,
Hyperagents,
AIDE2 (Kakade
et al., 2026;
Robeyns et al.,
2025; Srikanth
et al., 2026; Yin
et al., 2024;
Zelikman et al.,
2023; Zhang et al.,
2025, 2026)
{π,m} (the harness;
model weights and
benchmark outside)
yes;mis the self-modification
routine that edits prompts,
memory, tools, or code
Anchored; the evaluation base
is an external benchmark or
validation set
Anchored RSI
MetaRSI (Tan
et al., 2026)
{π,m}(data,
weights, and
scaffold, and the
schedule over them)
yes; the operators’ proposal
policies and their schedule are
revised at a meta level
Anchored; a sealed evaluator,
task set, and release gate stay
outside every write surface at
every level
Anchored RSI (a
fixed meta level
ends the hierarchy)
Red Queen Gödel
Machine (Iacob
et al., 2026)
{π,m,U}(the
agent and its
evaluator, which
co-evolve)
yes;m rewrites both the agent
and its evaluator
Goal Drift; the evaluation
base is updated during the
process, so no fixed external
standard remains
Drifting RSI
Closed-system
proposals (Schaul,
2024)
all components,ρ
included
yes;mmay rewrite any
component, the base included
Fully Self-Referential; the
evaluation base is empty or
self-referential, so no external
signal remains
Fully
Self-Referential
RSI
agent and the meta agent that improves it in a single editable program, so that the modification procedure
itself can be rewritten, while the evaluation remains an external benchmark (Zhang et al., 2026). Since only
the scaffold is modifiable, such systems are bounded in what they can improve. MetaRSI widens the editable
set to data, weights, and scaffold, and revises the schedule by which its operators are composed, while a sealed
evaluator, the task set, and the release gate stay outside every write surface at every level, so the anchoring is
enforced by construction rather than assumed (Tan et al., 2026). Its meta level, which revises the schedule, is
in turn fixed, so the hierarchy terminates at a level the system does not rewrite. In the same months, a wave
of harness- and weight-level work keeps the scoring outside the agent while spanning both settings of the
first dial (Dong et al., 2026; Tian et al., 2026; Ye et al., 2026; Zhao et al., 2026b); RSIGym provides such an
10

Generalized Agent Iteration: One Formal Framework for Iterative Policy Improvement and Recursive Self-Improvement
environment (Meng et al., 2026b).
Remark 5 (language agents as model and harness).Contemporary language agents are described
as a model plus a harness. The harness, holding prompts, memory, tools, and control flow, is what a
modifier changes; the weights and the evaluation benchmark usually stay outside the admissible set.
3 Co-Evolving EvaluatorsThe Red Queen Gödel Machine (Iacob et al., 2026) co-evolves the agent with
its evaluator, so the standard that self-improvement is measured against is itself updated during the process.
This places it at the Goal Drift row: the external objective may remain fixed in name while the mechanism
that measures progress toward it changes. At the far end, fully self-referential self-improvement, in which no
external signal reaches the loop, has been proposed as a position rather than demonstrated (Schaul, 2024).
What the GAI Framework AddsThe nearest prior formal work fixes one design rather than comparing
designs: the Gödel machine is anchored and proof-gated by construction, and statistical variants add a risk
budget to that gate (Wu et al., 2025). The recent ladder and the dials answer different questions: the ladder
grades how much of the improvement responsibility the AI carries, and where the standard sits is not part of
the grade; that is what the second dial reads. Nor does the ladder ask whether the improver is inside the
agent; the first dial does, and it separates systems the ladder groups together. The defects below follow from
the dials rather than from a rung, and the ladder’s own caution that a higher level does not by itself yield a
better improvement process is the same observation read from the other side (Duan et al., 2026). The two
dials turn these choices into coordinates, the polarity classifies the resulting systems, and the defect catalogue,
which we take up next, records what each departure from the GPI setting costs.
Takeaways from existing RSI-labeled work.
• Harness/code is the main substrate.Most RSI-labeled systems edit prompts, memory, tools, or code, with weights
frozen and evaluation outside (Robeyns et al., 2025; Yin et al., 2024).
• Weight-level work is a second, compute-heavy cluster.It updates parameters, but usually under a fixed
schedule or evaluator; it is not a separate kind of RSI (Lang et al., 2026; NeoHorse Team et al., 2026).
• World-model and rulebook updates are emerging.A smaller group improves an external world model or
rulebook with frozen weights (Cui et al., 2026; Zhao et al., 2026a); Dream-RSI is a steering-policy boundary case
(Zheng et al., 2026).
• Self-proposed tasks and data are components, not a paradigm.They sit inside the modifier; the scoring
standard, not the act of self-proposing, decides the polarity, and evaluation remains anchored (Meng et al., 2026b; Tan
et al., 2026).
• The label does not determine the class.Here, strict RSI is still the larger group, but several RSI-labeled systems
are fixed outer loops under GAI (Liu et al., 2026; Yang et al., 2026).
5 Defects of Recursive Self-Improvement
The two dials of GAI also locate the failures. The classical guarantees rest on two conditions: the improvement
step is cheap and monotone, and both the objective and the instrument that evaluates it lie outside the agent.
Under them, the anchored instance converges to an optimal policy in a finite MDP. Recursive self-improvement
may give up both. The defects below are those of the self-modifying case,m∈Ag ; the fixed outer loops of
Section 4, including RSI-labeled ones, are outside the scope of this catalogue. Each entry states the condition
it violates, is markedstructural(it follows from the definitions), and is markedobservedwhere existing systems
exhibit it. The list is short by design: it records where the classical guarantees end, not how far RSI can go.
5.1 Search over Candidate Selves and Self-Evaluation
GPI improves because its improvement step is cheap and its evaluation is external. The first property is lost
when the modifier is an agent component, the second when the modification critic is. The improvement step is
the argmax in Equation (4), taken over an unbounded content space, where no general procedure decides which
candidate is best. The Gödel machine’s proof gate is the established workaround, admitting only rewrites
whose benefit can be proved (Schmidhuber, 2007), with statistical variants placing a risk budget on that same
gate (Wu et al., 2025). Evaluation is lost for a related reason: whenU is an agent component, the object
evaluated and the instrument of evaluation coincide, and the value it reports is itself modifiable. A system
11

Generalized Agent Iteration: One Formal Framework for Iterative Policy Improvement and Recursive Self-Improvement
can still restrict itself, as the proof gate does, but the restriction is then part of its content, not an external
constraint. Both defects are structural, and both are also observed. A recent anchored-RSI benchmark where
agents revise their own training-data strategies under a fixed target model and a fixed external evaluation
reports that 58.33% of settings improve on the first valid attempt, yet 78.26% of searches that continue past
their best score end with a lower-scoring final attempt (Meng et al., 2026a): the improvement step is not
monotone even when the standard outside is fixed. The second defect is observed in MASS, which runs its
workflow search with the same model as optimizer and evaluator, soU∈Ag , with external judges withheld
from the loop, and reports that the search selects the best self-judged workflow rather than a certified optimum
(Lee et al., 2026); a world-model RSI system keeps a revision only after its own component and compatibility
checks pass (Cui et al., 2026).
5.2 The Consequences of an Ungrounded Base
When ρU is not grounded, the self-consistency conditions constrain only the pair(m,U ): the modifier must
propose changes that its own critic rates highly, and the critic must be tied to its evaluation base. Nothing in
the conditions refers to the goalG. Two consequences follow. First, they do not single out a unique system,
and they admit members that serveG poorly or not at all. Second, they give no faithfulness guarantee: a
self-consistent system may report improvement while the standard it reports against moves, since calibrating
U and honoringρU are choices of content, not properties enforced from outside. An engineering audit reaches
the same conclusion: from inside a loop, better capability and a better definition of success give the same
number, so trust is measured by what the system cannot rewrite (Tan et al., 2026). The case has an early
formal analog: Ring and Orseau let an agent rewrite its own inputs and find that a reinforcement-learning
agent can then satisfy its criterion without the cooperation of the world, the case they call the delusion box
(Ring and Orseau, 2011). Both consequences follow from the definitions.
Minimal Example (three placements of the same standard).Consider a coding agent whose
modification critic scores a proposed change by the fraction of tests it passes, and whose modifier
proposes changes that raise that fraction. The same construction satisfies the self-consistency conditions
under three placements of the tests, which play the role of the baseρU. Held out and fixed, they make
the reported improvement track the goal of producing working code, the anchored case. Placed in the
agent’s own repository, they admit an improvement that edits the tests, the Goal Drift case of the next
subsection. Replaced by the agent’s own judgment of what counts as an improvement, they depend on
the critic itself, the fully self-referential case. The conditions hold in all three; only the first serves the
goal.
5.3 Goal Drift
The middle row of Table 2 is the case in which the base still measures the world and the goal, but the agent
may rewrite it. Formally,G stays fixed whileρU is an agent component: what moves is the mechanism
that measures progress, not the objective. It is the harder of the two unanchored settings to notice: the
objective keeps its name, and a system that reports progress against it need not track it. The Red Queen
Gödel Machine is an instance: its evaluator co-evolves with the agent (Iacob et al., 2026). The row has a
formal counterpart: an agent able to rewrite its own utility function is harmless only when its value function
anticipates the rewrite and evaluates the future with the utility it currently holds (Everitt et al., 2016), a
condition secured for model-based utilities (Hibbard, 2012). Both results make the fixity of the standard
something to be secured rather than a default. The defect is structural, and the table marks it as observed.
Table 4 collects the four defects. Each row is a site where a guarantee of GPI stops applying, and each is
either immediate from the definitions or exhibited by a cited system. Whether a faithfulness monitor inside
the system could detect its own drift is a further question, which we leave open.
6 Discussion, Limitations, and Conclusion
Scope and LimitationsThe framework describes how a system changes, not how to compute the change.
The configuration space of Section 3.1 is a reference idealization: writing that an agent instance is drawn
12

Generalized Agent Iteration: One Formal Framework for Iterative Policy Improvement and Recursive Self-Improvement
Table 4Defects of recursive self-improvement, the dial setting that triggers each one, the condition of GPI
that it violates, and the support for the claim.
Defect Trigger GPI condition violated Status
Search over candidate
selves
Dial 1 :m∈Ag/timesImprovement is cheap and monotone Structural;
observed
Self-evaluation Dial 1 :U∈Ag/timesThe evaluator stands outside what it evaluates Structural;
observed
Ungrounded base Dial 2 :ρ U not
grounded
/timesThe objective is evaluated from outside the agent Structural
Goal Drift Dial 2 :ρ U ∈Ag/times The objective is evaluated from outside the agent, lost
when the base is rewritten
Structural;
observed
from the modifier states what is chosen, not that the choice is reachable or affordable. Four limits follow.
First, the definitions carry no reachability or complexity claims, and the defects above are properties of the
formulation; where an existing system exhibits one, we cite it rather than measure it. Second, we do not
model time scales: the alternation between world actions and agent updates is counted in steps, not compute.
Third, practical guards, such as the proof gate of the Gödel machine or a coding benchmark, are treated as
external mechanisms that restrict what a modifier may propose; whether a guard should itself be an agent
component is a design choice we leave open. Fourth, the framework describes systems that run without
human intervention, the case we study; a reviewer who accepts, audits, or rolls back an update is outside the
formalism, although in practice a human still sets the direction and reviews the result (Favaro and Clark,
2026). One objection is worth answering directly: recursive self-improvement is not simply an MDP over
configurations. An MDP fixes its transition law and its reward outside the agent, whereas here the next
configuration is drawn by a modifier inside the agent, and the standard of evaluation may be inside it as well.
From Catalogue to ResultsThe defects above are stated as consequences of the definitions, and only some
of them are candidates for theorems. Three targets are concrete. First, the solution set of the self-consistency
conditions is uncharacterized: how many solutions they admit, and when one of them serves the goal, remains
open. Second, the reduction from recursive self-improvement to GPI is prose rather than a proposition with
explicit hypotheses. Third, whether a monitor inside the system could decide the faithfulness of its own
modification critic is left open, and it is the one question we would expect to require a self-reference argument
rather than a construction. The remaining defects are structural and would not change under any of these
results.
ConclusionIn this paper, we show that GPI and recursive self-improvement are two settings of one
alternating cycle defined by the GAI formal framework. They differ in two dials: whether the improving
mechanism lies inside the agent, and whether the standard it is measured against stays grounded. We use these
coordinates to place existing systems, including RSI-labeled ones, on the same two axes, separate those that
are GPI from those that are RSI in the GAI sense, and make the defects of recursive self-improvement statable
one condition at a time. We believe that this will be a first step toward exploring a formal characterization of
RSI that makes existing systems comparable, and provides a principled basis for analyzing and designing new
ones.
References
Mingguang Chen, Licheng Wang, and Bo Qu. Recursive self-improvement in AI: From bounded self-refinement to
autonomous research loops, 2026. arXiv:2607.07663.
Taoyong Cui, Pinxian Zeng, Wanghan Xu, Hao Xiao, Shuhan Xue, Qiang Gao, Wanli Ouyang, Pheng Ann Heng,
Zhenfei Yin, Yingcheng Wu, and Ling Yang. RSI-Anything: Unlocking recursive self-improvement with world
models, 2026. arXiv:2610.13912.
Haoyu Dong, Yuhang Zhou, Zihao Lin, Yifan Wu, Bo Peng, Mingyi Wang, Xiangjun Fan, Lizhu Zhang, and Zhuokai
Zhao. Mixture of self-improving branches for agent harness optimization, 2026. arXiv:2609.37834.
Yi Duan, Ying Liu, Zirui Tang, Haodong Chen, Jun Zhou, Yumou Liu, Bangrui Xu, Yukai Wu, Sidi Chen, Yuhan Zhou,
Haoyu Wang, Xiaoyou Yu, Shaokun Han, Xuzhou Zhu, Le Zhou, Bolin Lu, Wei Zhou, Jiachen Liu, Nuozhou Fang,
Jiaxin Tian, Ruoyu Chen, Yuxuan Li, Kai Zuo, Kaiyan Zhang, Qianyu Yang, Zijie Wang, Jiantao Qiu, Conghui He,
13

Generalized Agent Iteration: One Formal Framework for Iterative Policy Improvement and Recursive Self-Improvement
Guoliang Li, Bowen Zhou, Zhiyuan Liu, Zhoufutu Wen, Jihua Kang, Xuanhe Zhou, and Fan Wu. The last AI built
by humans: Toward genuine recursive self-improvement, 2026. arXiv:2609.11873.
Tom Everitt, Daniel Filan, Mayank Daswani, and Marcus Hutter. Self-modification of policy and utility function in
rational agents. InArtificial General Intelligence (AGI), volume 9782 ofLecture Notes in Computer Science, pages
1–11. Springer, 2016. arXiv:1605.03142.
Marina Favaro and Jack Clark. When AI builds itself, 2026. Anthropic Institute, https://www.anthropic.com/
institute/recursive-self-improvement.
Huan-ang Gao, Jiayi Geng, Wenyue Hua, Mengkang Hu, Xinzhe Juan, Hongzhang Liu, Shilong Liu, Jiahao Qiu, Xuan
Qi, Yiran Wu, Hongru Wang, Han Xiao, Yuhang Zhou, Shaokun Zhang, Jiayi Zhang, Jinyu Xiang, Yixiong Fang,
Qiwen Zhao, Dongrui Liu, Qihan Ren, Cheng Qian, Zhenhailong Wang, Minda Hu, Huazheng Wang, Qingyun Wu,
Heng Ji, and Mengdi Wang. A survey of self-evolving agents: What, when, how, and where to evolve on the path to
artificial super intelligence, 2025. arXiv:2507.21046.
Irving John Good. Speculations concerning the first ultraintelligent machine. InAdvances in Computers, volume 6,
pages 31–88. Academic Press, 1965.
Bill Hibbard. Model-based utility functions.Journal of Artificial General Intelligence, 3(1), 2012. arXiv:1111.3934.
Kairui Hu, Siyuan Hu, Fangzhou Hong, Zhaoxi Chen, and Ziwei Liu. Embodied Turing machines: Stateful code for
robot recursive self-improvement, 2026. arXiv:2610.12369.
Alex Iacob, Andrej Jovanović, William F. Shen, Daniel Burkhardt, Meghdad Kurmanji, Nurbek Tastan, Lorenzo Sani,
Niccolò Alberto Elia Venanzi, Ambroise Odonnat, Zeyu Cao, Bill Marino, Xinchi Qiu, and Nicholas D. Lane. The
Red Queen Gödel machine: Co-evolving agents and their evaluators, 2026. arXiv:2606.26294.
Aditya Kakade, Vivek Srivastava, and Shirish Karande. Polaris: A Gödel agent framework for small language models
through experience-abstracted policy repair, 2026. arXiv:2603.23129.
Haoran Lang, Haotao Lu, Shiyu Sang, Haoyang Luo, Guo Chen, Qun Li, Jingyi Yu, Ye Shi, and Jingya Wang.
EmbodiRSI: Recursive self-improvement for data-efficient robot adaptation, 2026. arXiv:2609.38905.
Hyunin Lee, Jinglue Xu, Jeffrey Seely, Donghyun Lee, Somayeh Sojoudi, Matei Zaharia, and Yujin Tang. Recursive
self-improvement through multi-agent self-supervision, 2026. arXiv:2610.12176.
Haozhe Liu, Tian Ye, Sensen Gao, Qihang Cao, Yitong Li, Mingchen Zhuge, Duomin Wang, Ruihua Zhang, Ping Luo,
Jiawang Bian, Lei Zhu, Ligeng Zhu, Enze Xie, and Song Han. SoL-Pi: Recursively scaling auto-research loops for
efficient agent harness, 2026. arXiv:2609.20519.
Chris Lu, Cong Lu, Robert Tjarko Lange, Jakob Foerster, Jeff Clune, and David Ha. The AI scientist: Towards fully
automated open-ended scientific discovery, 2024. arXiv:2408.06292.
Aman Madaan, Niket Tandon, Prakhar Gupta, Skyler Hallinan, Luyu Gao, Sarah Wiegreffe, Uri Alon, Nouha Dziri,
Shrimai Prabhumoye, Yiming Yang, Shashank Gupta, Bodhisattwa Prasad Majumder, Katherine Hermann, Sean
Welleck, Amir Yazdanbakhsh, and Peter Clark. Self-Refine: Iterative refinement with self-feedback. InAdvances in
Neural Information Processing Systems, 2023. arXiv:2303.17651.
Fanqing Meng, Lingxiao Du, Qiguang Chen, Ziqi Zhao, Haocheng Lu, Mengkang Hu, and Michael Qizhe Shieh.
RSIBench-Data: Benchmarking data-centric research for recursive self-improvement, 2026a. arXiv:2607.25886.
Fanqing Meng, Lingxiao Du, Haocheng Lu, Qiguang Chen, Ziqi Zhao, Zijian Wu, Jiayuan Zhuo, Mengkang Hu, and
Michael Qizhe Shieh. RSIGym: A flexible environment for recursive self-improvement, 2026b. arXiv:2610.10310.
Volodymyr Mnih, Koray Kavukcuoglu, David Silver, Alex Graves, Ioannis Antonoglou, Daan Wierstra, and Martin
Riedmiller. Playing Atari with deep reinforcement learning. InNIPS Deep Learning Workshop, 2013. arXiv:1312.5602.
NeoHorse Team, Guoliang Cao, Guohao Dai, Tianyu Guo, Kai Han, Hailin Hu, Zihan Jiang, Xiang Kuang, Boxun Li,
Yulong Li, Zehua Pei, Yuchuan Tian, Jiamin Wang, Yu Wang, Yunhe Wang, Yihong Wu, Haiyang Xu, Shuo Zhang,
Hang Zhou, Siyang Cheng, Jiayu Fan, Wei He, Qingrui Jiao, Hongguang Li, Zhiyuan Li, Runke Liu, Xi Liu, Xinchen
Liu, Sinno Jialin Pan, Yi Ren, Liuyang Song, Chenyu Wang, Bei Yu, Quanlu Zhang, Xiangyu Zhang, Mengyu
Zheng, and Yingjie Zong. NeoHorse-1: Towards recursive self-improvement via agentic post-training with routing
harness, 2026. arXiv:2609.08183.
E. Nivel, K. R. Thórisson, B. R. Steunebrink, H. Dindo, G. Pezzulo, M. Rodriguez, C. Hernandez, D. Ognibene,
J. Schmidhuber, R. Sanz, H. P. Helgason, A. Chella, and G. K. Jonsson. Bounded recursive self-improvement, 2013.
arXiv:1312.6764.
Alexander Novikov, Ngân V˜ u, Marvin Eisenberger, Emilien Dupont, Po-Sen Huang, Adam Zsolt Wagner, Sergey
Shirobokov, Borislav Kozlovskii, Francisco J. R. Ruiz, Abbas Mehrabian, M. Pawan Kumar, Abigail See, Swarat
Chaudhuri, George Holland, Alex Davies, Sebastian Nowozin, Pushmeet Kohli, and Matej Balog. AlphaEvolve: A
coding agent for scientific and algorithmic discovery, 2025. arXiv:2506.13131.
Stephen M. Omohundro. The basic AI drives. InArtificial General Intelligence, volume 171 ofFrontiers in Artificial
Intelligence and Applications, pages 483–492. IOS Press, 2008.
Mark Ring and Laurent Orseau. Delusion, survival, and intelligent agents. InArtificial General Intelligence (AGI),
volume 6830 ofLecture Notes in Computer Science, pages 11–20. Springer, 2011.
14

Generalized Agent Iteration: One Formal Framework for Iterative Policy Improvement and Recursive Self-Improvement
Maxime Robeyns, Martin Szummer, and Laurence Aitchison. A self-improving coding agent, 2025. arXiv:2504.15228.
Tom Schaul. Boundless Socratic learning with language games, 2024. arXiv:2411.16905.
Jürgen Schmidhuber. Gödel machines: Self-referential universal problem solvers making provably optimal self-
improvements, 2003. arXiv:cs/0309048.
Jürgen Schmidhuber. Gödel machines: Fully self-referential optimal universal self-improvers. In Ben Goertzel and
Cassio Pennachin, editors,Artificial General Intelligence, pages 199–226. Springer, 2007.
John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal policy optimization
algorithms, 2017. arXiv:1707.06347.
Noah Shinn, Federico Cassano, Edward Berman, Ashwin Gopinath, Karthik Narasimhan, and Shunyu Yao. Reflexion:
Language agents with verbal reinforcement learning. InAdvances in Neural Information Processing Systems, 2023.
arXiv:2303.11366.
Dhruv Srikanth, Bingchen Zhao, Dixing Xu, Yuxiang Wu, and Zhengyao Jiang. Recursive self-improvement of AI
research agents, 2026. arXiv:2609.26457.
Richard S. Sutton and Andrew G. Barto.Reinforcement Learning: An Introduction. MIT Press, 2nd edition, 2018.
Zihan Tan, Leixin Sun, Zitong Shi, Yitao Liu, Jiajun Wu, Nathaniel Brooks, Jiaru Qian, Xiaoran Shang, Suyuan
Huang, Yi Ding, Yangxu Liao, Mukai Li, Qiushi Sun, Shudong Liu, Xuankun Rong, Xiaohang Yu, Zhuo Chen, Hejia
Geng, Chenxin Li, Aozhou Wang, Zengji Tu, Robert Tang, Yuxin Zhan, Eric Jiang, Yuxin Wu, Jianqing Zhang,
Xiao Liang, Fang Wu, Haochi Zhang, Alexander Marlow, and Guancheng Wan. MetaRSI / RSI2: A meta-recursive
self-improving system for recursive self-improving systems themselves, 2026. arXiv:2609.06396.
Weidong Tang, Ruiheng Wang, Jingxuan Zhang, Hexin Wang, Haoyuan Chen, Zhengfeiyang Zhang, Yixing Ma, Zichen
Jiang, Ziyu Guo, Haodong Li, Zhengbo Jiao, Zhiqing Cui, Xinxiang Yin, Shuo Liang, Zhenglin Wan, Hongzhan Lin,
Wangbo Zhao, Kaipeng Zhang, Pengfei Zhou, Odin Zhang, and Yang You. The Trinity: Capability-driven recursive
self-improvement for multimodal agents, 2026. arXiv:2610.36077.
Wenqing Tian, Zeyu Zhang, Zhaocheng Liu, Fengwei Liu, Qiang Liu, and Liang Wang. PhysEvo: Astra can act, let it,
2026. arXiv:2610.08995.
Xuening Wu, Shenqin Yin, Yanlan Kang, Xinhang Zhang, Qianya Xu, Zeping Chen, and Wenqiang Zhang. SGM: A
statistical Gödel machine for risk-controlled recursive self-modification, 2025. arXiv:2510.10232.
Roman V. Yampolskiy. From seed AI to technological singularity via recursively self-improving software, 2015.
arXiv:1502.06512.
Junyao Yang, Zongxia Li, Yucheng Shi, Zhongzhi Li, Ruhan Wang, Ruiwen Zhou, Haitao Mi, Shuicheng Yan, and
Leowei Liang. Terminal-RSI: Recursive self-improving terminal agents via recursive self-rewrite and policy-refine,
2026. arXiv:2610.22192.
Haoran Ye, Yuxing Lu, Haonan Dong, Zhaochen Su, and Guojie Song. Harness-zero: Harness distillation via
agent-as-harness, 2026. arXiv:2609.24974.
Xunjian Yin, Xinyi Wang, Liangming Pan, Li Lin, Xiaojun Wan, and William Yang Wang. Gödel agent: A self-referential
agent framework for recursive self-improvement, 2024. arXiv:2410.04444.
Eliezer Yudkowsky. Intelligence explosion microeconomics, 2013. MIRI Technical Report.
Eric Zelikman, Eliana Lorch, Lester Mackey, and Adam Tauman Kalai. Self-taught optimizer (STOP): Recursively
self-improving code generation, 2023. arXiv:2310.02304.
Jenny Zhang, Shengran Hu, Cong Lu, Robert Lange, and Jeff Clune. Darwin Gödel machine: Open-ended evolution of
self-improving agents, 2025. arXiv:2505.22954.
Jenny Zhang, Bingchen Zhao, Wannan Yang, Jakob Foerster, Jeff Clune, Minqi Jiang, Sam Devlin, and Tatiana
Shavrina. Hyperagents, 2026. arXiv:2603.19461.
Yuxuan Zhang. RSI: A conditional theory, not an achieved milestone, 2026. Blog post,https://www.cs.ubc.ca/
~reacher/blog/rsi/.
Haoyu Zhao, Zhengxu Yu, Zhiyuan He, Meng Fang, Rasul Tutunov, Haitham Bou-Ammar, Weilin Luo, and Jun Wang.
Memento 3: Model-based recursive self-improvement through reflective rulebooks, 2026a. arXiv:2610.11794.
Sijie Zhao, Zeqi Zhou, Heli Qi, Xuanchao Fu, Zhuo Zheng, Junshi Xia, Junjue Wang, Weihao Xuan, and Naoto Yokoya.
The last remote sensing model built by humans? casting any earth observation task as recursive self-improvement,
2026b. arXiv:2610.18845.
Tong Zheng, Xidong Wu, Zheng Zhang, Zhankui He, Chaoyi Zhang, Benjamin Coleman, Ruoqiao Wei, Di Bai, Haolin
Liu, Rui Liu, Xue Wang, Yue Zhuan, Wang-Cheng Kang, Renkai Xiang, Heng Huang, Xinwu Cheng, and Yunsong
Guo. Dream-RSI: Recursive self-improvement through evolving worlds, 2026. arXiv:2609.14858.
15

Generalized Agent Iteration: One Formal Framework for Iterative Policy Improvement and Recursive Self-Improvement
Appendix: Notation
World, goal, and RL background.
Symbol Meaning
Wworld= (S,A,p,r,γ); states, actions, transition, reward, discount
S,Aworld state / action spaces
rworld reward; the grounded content ofρ V (Section 3.1)
Gexternal goal / preference; the grounded content ofρ U
γdiscount factor
Eexpectation
Em,I m evaluation / improvement operators carried by the modifier
Components and roles.
Symbol Meaning
Oset of components in the system
oa component;C o its content space
πpolicy: chooses world actions,S→∆(A)
Vaction critic: evaluation of the policy,S→R
mmodifier: proposes how the system changes,X→∆(X Ag)
Umodification critic: evaluation of the modifier,X→R
ρevaluation base of the critics; instancesρ V,ρ U where the two must be told apart
System and agent.
Symbol Meaning
χa system,χ∈X
Xfull system space,X=
∏
o∈OCo
Ag⊆Othe agent: the set of modifiable components
XAg agent subspace,X Ag =
∏
o∈AgCo⊆X
ξan agent instance,ξ∈X Ag
χ[ξ]system with its agent part replaced byξ
∆(Y)set of probability distributions overY
16
