---
title: 'NeSyFS: A Neuro-symbolic Fast-Slow Thinking Framework for LLM Agent under Partial Observability'
url: https://arxiv.org/abs/2607.28942
category: ai-marketing
subcategory: empirical
date: 2026-07
venue: ''
authors:
- Duo Xu
- Faramarz Fekri
source: arxiv
pdf_url: https://arxiv.org/pdf/2607.28942
pages: 14
chars: 71549
fetched_at: '2026-11-08T13:34:08+00:00'
kb_version: 1
---

# NeSyFS: A Neuro-symbolic Fast-Slow Thinking Framework for LLM Agent under Partial Observability

NeSyFS: A Neuro-symbolic Fast-Slow Thinking Framework for LLM Agent under
Partial Observability
Duo Xu, Faramarz Fekri∗
Georgia Institute of Technology
225 North Ave NW, Atlanta, GA 30332
dxu301@gatech.edu
Abstract
Recently Large Language Models (LLMs) have been increas-
ingly deployed as autonomous agents in applications such as
self-reflection, retrieval-augmented generation, and scientific
discovery. In these settings, agents must act based on limited
observations rather than full environmental states, leading to
partialobservability.Thisintroducesseveralkeychallenges:be-
lief state inference, task objective misalignment, and planning
underuncertainty.Priorapproachestypicallyconditionactions
on full or summarized action-observation histories whose re-
dundant and irrelevant information can mislead the decision
making of LLM agent. Inspired by human cognition, we pro-
pose a novelNeuro-SymbolicFast-Slow thinking (NeSyFS)
framework for LLM agent, addressing the challenges intro-
duced by partial observability in a unified approach. We use a
knowledge graph (KG) to represent the belief state, providing
triplets as context for every module of NeSyFS. The fast-
thinkingmoduleperformsreactiveaction,whileslow-thinking
conducts a new uncertainty-aware planning by following the
high-levelstructureoftwistedsequentialMonteCarlo(TSMC)
algorithm. To mitigate the misalignment of task objective, a
reflection module is used to reflect fast-thinking actions, and
also switches to the slow-thinking module whenever reactive
actions repeatedly fail. Experiments on three representative
benchmarks, i.e. ALFWorld, Webshop, and ScienceWorld,
demonstrate significant advantages over previous methods.
Introduction
Large Language Models (LLMs) have achieved notable suc-
cess in agentic applications by extending beyond static text
generationtosupportautonomousdecision-making,enabling
capabilities such as tool use (Schick et al. 2023), retrieval-
augmented reasoning (Gao et al. 2023), multi-step planning
(Rawat et al. 2025), and self-reflection (Renze and Guven
2024) in complex environments. These advances have al-
lowed LLM agents to perform tasks in domains ranging from
embodied interaction to software automation (Jin et al. 2024)
and scientific workflows (Yamada et al. 2025). However,
a fundamental challenge arises from partial observability:
unlike supervised settings with complete input context, agen-
tic environments typically reveal only local and immediate
observations, while the true underlying state remains latent
(Shridhar et al. 2020; Yao et al. 2022a). As a result, LLM
agents must infer a belief over the hidden state from incom-
pleteandpotentiallynoisyinteractionhistories(Xietal.2024;
∗This work is supported by ARO grant under Award #W911NF-
23-1-0146 and a gift by Open Philanthropy.
Act t+1:
go to shelf 1
Retrieved
triplets
KG t-2
KG t-1
KG t
Act t+1:
go to drawer 1
...
Obs t-2: On shelf 1,
you see nothing
Act t-1: go to fridge 1
Obs t-1: The fridge 1
  is closed.
Act t: open fridge 1
Obs t: You open the
  fridge 1. The fridge 1
  is open. In it, you
  see cup 1.
Previous
agent
NeSyFS
agent
Figure1:ComparisonofpreviousandNeSyFSagent.Previous
agent uses full or summarized interaction history as context
for decision making, while our agent updates a KG-based
memorydynamicallyandusesKG-retrievedtripletsascontext.
TheKG Gt−1 isupdatedwithaction at andobservation ot,i.e.
Gt =Update(G t−1, ot, at). The triplets related with solving
task η are retrieved from KG, i.e.τt =R(G t, η), which
can provide structured context to help LLM make correct
decision.
Maetal.2024),whichareoftenlonganddifficulttocompress
effectively within limited context windows. In addition, since
the agent must act without access to the true underlying state,
increased amount of uncertainty is introduced, and planning
under uncertainty becomes a challenge for the LLM agent.
Moreover,theuncertaintyandmissingstateinformationfrom
partialobservabilitycanmaketheLLMagentproduceactions
misaligned with task objective, degrading the performance
of task completion.
In this work, we propose a novel neuro-symbolic fast–slow
thinking framework (NeSyFS) for LLM agents that addresses
the challenges of partial observability in a unified manner,
enabling latent state inference, mitigating task-objective mis-
alignment,andsupportingplanningunderuncertainty.Unlike
prior full-history-based or summarization-based approaches
that rely on unstructured memory, we employ a knowledge
graph (KG) to represent the latent state of the environment,
thereby encoding interaction histories into a structured and
symbolic memory. Specifically, each incoming observation
is transformed into triplets that capture relationships and
attributes of entities and events. Newly acquired facts are
arXiv:2607.28942v3  [cs.AI]  27 Sep 2026

incorporated into the KG, while outdated triplets in KG are
pruned, ensuring a consistent and dynamically updated rep-
resentation of the latent state. The KG-retrieved triplets are
used as context in every module of NeSyFS.
Furthermore, inspired by human cognition (Kahneman
2011),theproposedframeworkdecomposesdecision-making
into fast and slow thinking processes. The fast thinking mod-
ule generates reactive actions by retrieving relevant triplets
from the KG to construct a symbolic approximation of the
latent state. In contrast, the slow thinking module performs
deliberative planning under uncertainty. Slow thinking is
used only when fast-thinking decision making has too much
uncertainty or is unreliable. To this end, we propose a new
uncertainty-awareplanningalgorithmwhichfollowsthehigh-
level structure of twisted sequential Monte Carlo (TSMC)
(DelMoral,Doucet,andJasra2006).Specifically,itmaintains
a set of particles and uses resampling to guide them toward
the target distribution modeling task-completing trajectories.
LLMispromptedtopredictnextobservationandexistenceof
taskprogressinthestatetransition.Thesamplingmechanism
of this method can make the particles robust to mistakes in
LLM-based evaluations of task progress, and reach a good
balance between exploration and exploitation. As far as we
know, we are the first to develop a TSMC-style planning
method for LLM agent.
Althoughfastthinkingemphasizeslocallyplausibleactions,
itdoesnotexplicitlyguaranteealignmentwithglobaltaskob-
jectives.Toaddressthislimitation,weincorporateareflection
modulethatevaluatestheconsistencyoffast-thinkingactions
with the task objective, conditioned on relevant triplets re-
trievedfromtheKG.Tocontrolcomputationaloverhead,slow
thinkingisinvokedonlywhenfast-thinkingactionsrepeatedly
fail in this reflective evaluation. With KG-provided triplets as
context, stepwise reflection is enabled and is more efficient
and robust than conventional trajectory-wise reflection.
Our contributions are summarized as follows.
• We propose a neuro-symbolic fast-slow thinking frame-
work that addresses challenges introduced by partial ob-
servability in a unifying manner.
• Based on the context retrieved from the KG, a neuro-
symbolic TSMC-style planning algorithm is introduced
withintheslow-thinkingmoduletoaddresstheuncertainty
under partial observability.
• We design a KG-augmented reflection module that aligns
fast-thinking actions with task objectives. Using KG-
retrieved triplets, the module enables stepwise reflec-
tion that is more efficient and robust than conventional
trajectory-level reflection.
• Experiments on three benchmarks demonstrate that us-
ing KG-retrieved triplets as context improves the LLM
performance on decision-making, reflection, and world
modeling.
Preliminary Background
Partial Observability
We consider agentic tasks in which an autonomous LLM
responds to a user query through iterative interaction with
an external environmentE. Each episode begins with a user
query and unfolds over a finite horizonH.
SuchagentictaskscanbenaturallyformulatedasaPartially
Observable Markov Decision Process (POMDP) (He et al.
2024; Zhang et al. 2025), represented by the tupleM=
(S,A,O,T, O, R). Here,S denotes the latent state space of
the environment,A the action space, andO the observation
space consisting of textual environmental response. The
environmentdynamicsaregovernedbythetransitionfunction
T(s ′ |s, a) and the observation modelO(o|s, a) . The
reward functionR(s) is defined only on terminal states and
indicates task success.
At time stept, the agent executes an actionat, after which
the environment transitions to a latent statest ∼ T(· |
st−1, at)and returns an observationot ∼O(· |st, at). Dur-
inginference,neitherthelatentstate stnortherewardfunction
is directly observable to the agent. This results in partial ob-
servability, which introduces several fundamental challenges,
including latent state inference, task objective misalignment,
and planning under uncertainty. In particular, inferringst
from the interaction history is difficult because the history
often contains substantial redundant and noisy information.
Moreover, not knowingst creates a lot of uncertainty and
further complicates the prediction of future situations in plan-
ning.Inthiswork,weproposeanovelframeworktounifiedly
resolve these challenges.
Knowledge Graph
Knowledgegraphs(KGs)(EhrlingerandWöß2016)represent
informationasgraph-structureddata,wherenodescorrespond
to entities and edges encode relationships among them. KGs
canbeconstructedfromdiversesources,includingstructured
databases, unstructured text, and other heterogeneous data
modalities. Similar to traditional databases, graph databases
support structured querying mechanisms, such as the Cypher
query language (Francis et al. 2018).
The relationship between a pair of nodes in a KG is com-
monly referred to as a triplet of subject, predicate, and object.
In this work, we consider the following triplet forms:
•(entity 1, relationship, entity 2)
•(entity 1, attribute, boolean/value)
•(entity 1, verb in the past tense, entity 2)
which describe relationships, attributes and historic events
of entities. A KG is denoted asG= (V, E) where V is
a set of semantic vertices corresponding to entities in the
environment, andE is a set of semantic edges representing
triplets in the above forms. Our framework has a retrieval-
augmented generation (RAG) component which retrieves
the relevant triplets from a KG and feeds them to LLM as
context approximating the underlying state of the POMDP
environment.
Twisted Sequential Monte Carlo
Twisted Sequential Monte Carlo (TSMC) (Doucet, De Fre-
itas, and Gordon 2001; Del Moral, Doucet, and Jasra 2006;
Chopin, Papaspiliopoulos et al. 2020; Zhao et al. 2024b;
Feng et al. 2025b) is a probabilistic inference framework

Environment
Knowledge
Graph
Fast-Thinking
Module
Slow-Thinking
Module
If "Yes"
observation
context triplets
udpate copy
context triplets
If "No" repeatedly
action
planned
action
reactive action
If "No", thought
is transmitted
Reflection
Module
Figure 2:Diagram of NeSyFS framework. Knowledge graph (KG),
representing the latent state of environment, is updated by fast-
thinking module with new observation and retrieved by all the
modules. Every reactive action is reflected. If "No", fast-thinking is
calledagainwiththoughtfromreflectionmodule.If"No"repeatedly
for K number of times, the slow-thinking module is initiated to
search optimal action via planning, where memory KG is copied to
initialize the simulation of future latent states and observations.
that incrementally guides particles toward high-probability
regionsofatargetdistribution σthroughintermediatetwisted
distributions ψt.Ateachstep,particlesarepropagatedusinga
proposal distribution and resampled according to importance
weights, allowing computational effort to focus on promising
trajectories while reducing variance. In this work, to address
uncertainty under partial observability, the slow-thinking
module follows a TSMC-like structure, where LLMs are
used to propose future states and observations and to score
particles.
Sequential Monte Carlo (SMC) and its variants have been
applied into planning and reinforcement learning by many
previous work (Piché et al. 2018; Macfarlane et al. 2024;
Abdulsamad, Iqbal, and Sarkka 2026). Compared with other
planning methods, such as Monte Carlo Tree Search (MCTS)
(Chen et al. 2024), SMC-style methods can better address the
uncertainty of states and reduce computational complexity,
sinceparticlesrepresentingless-likelystateswillbediscarded
andnotbranchedinlargeprobability.However,intree-search-
based methods, every state will be branched and its child
nodes will be evaluated. In this work, we develop a TSMC-
style LLM-based planning method for slow-thinking module,
where the state is approximated by related triplets retrieved
from memory KG. As far as we know, this work is the first of
doing so.
Methodology
In this section, we introduce the NeSyFS framework, which
maintains a memory KG as a proxy for the latent state of
the environment. The diagram of the proposed framework is
shown in Figure 2. Using triplets retrieved from the memory
KG as a context, the fast-thinking module generates reactive
Task
State (KG) Reactive Action
 Retrieved
TripletsRetriever
Figure3:Diagramofdecisionmakinginfast-thinkingmodule.
actions,whiletheslow-thinkingmoduleperformsuncertainty-
awaredeliberativeplanning.Areflectionmoduleevaluatesthe
fast-thinking actions with respect to the task objective, where
the KG-retrieved triplets facilitate reflection in the stepwise
granularity. We will first introduce the fast-thinking module,
including the memory KG. Then, reflection module will be
presented with details. Finally, the slow-thinking module,
including the proposed TSMC-style planning algorithm, is
introduced.
Fast Thinking Module
WeuseaKG G= (V, E)asworkingmemorytorepresentthe
latentstateoftheenvironment(POMDP M).Insteadofusing
the entire interaction history or its summary as unstructured
context, this memory organizes environmental knowledge
intostructuredtripletswhichdescribeattributesandrelations
of entities and past events, in the forms in Section .
At each time stept, given the current observationot and
task description η, the fast-thinking module first retrieves
task-relevant tripletsτt from memory KGGt by calling the
retrieval methodR(Gt, η). The details ofR are introduced
in Appendix . Then,τt are then provided as contextual input
to the LLM which is prompted to produce the next action
for accomplishing taskη with observation ot. During this
process,chain-of-thought(CoT)reasoning(Weietal.2022)is
employed, making the fast-thinking action selection process
analogoustotheReActmethod(Yaoetal.2022b).Thiscanbe
formallyexpressedas at =LLM(P fast;R(G t), ot, η),where
Pfast is the reactive decision making prompt template,Gt is
the KG representing current latent state. Diagram of decision
making in the fast-thinking module is shown in Figure 3.
Whenever at is applied into the environment, the agent
receives a new observationot. The KGGt will be updated
with ot and at to produceGt+1 to represent next state. This
process is denoted asGt+1 =Update(G t, ot, at), where new
triplets from ot and at will be added toGt, and outdated
triplets inGt will be removed. The details of update process
are presented in Appendix .
Reflection Module
Due to incomplete information about the underlying environ-
ment state, partial observability can introduce misalignment
between the agent’s actions and the task objective, which has
emerged as a major challenge for LLM agents (Fang, Zhu,
and Gurevych 2025; Kim et al. 2025; Chung et al. 2025). To
mitigate this issue, we introduce a prompt-based reflection
module that detects misalignment between the actions pro-

Act. t+1: open
fridge 1
Act. t+1:
go to sofa 1
Obs. t: You move
cd1 to sofa 1
KG t: KG t+1
Particle 1
Act. t+1: go to
countertop 1
Obs. t+1:
On countertop 1, you
see bread 2 and knife 1
Obs. t: Fridge 1 is
closed
KG t:
Particle 2
1
t+1
1
t+1
KG t+1
Obs. t+1:
In fridge 1, you see
apple 1 and cup 2
2
t+1
2
t+1
Obs. t: You pick up
cd2 from sidetable 1
KG t:
Particle 3
Obs. t+1: In fridge 1,
you see apple 1 and
cup2
KG t+1:
Particle 2
Obs. t+1: On sofa 1,
you see mug 1 and
fork 2
KG t+1:
Particle 3
KG t+1
Obs. t+1:
On sofa 1, you see
mug 1 and fork 2
3
t+1
3
t+1
Obs. t+1: In fridge 1,
you see apple 1 and
cup2
KG t+1:
Particle 1
Figure 4: Diagram of the proposed TSMC-style uncertainty-aware planning algorithm, where three particles are updated in the
planning stept, consisting of propagation, weight update and resampling processes. The red box shows the propagation process,
where the prediction of KG at timet+ 1 is essentially updating KG att with at+1 and ot+1. The blue box is the weight update
process, where the blue circle represents the value of an updated weight. The green box represents the process of resampling.
Every particle stores all the historic observations, actions, states (KG), and weights.
duced by the fast-thinking component and the task objective.
Unlike self-reflection methods (Shinn et al. 2023), in which
the agent introspects and explains its own behavior, the pro-
posed reflection module adopts a third-person perspective to
verify whether a candidate action aligns with the task objec-
tive. Our innovation here is to use the KG-retrieved triplets
as context to facilitate reflection in the stepwise granularity,
since context triplets provide sufficient state information for
reflection.
The reflection can be expressed as Y ref =
LLM(P ref;a t, ot,R(G t), η), where Pref is the prompt for
refection, at is the fast-thinking action,R is the operation
of KG retrieval introduced in previous section,η is the task
description, and outputY ref ∈ {Yes,No}which indicates
whether atalignswith ηornot.Tomitigatetherandomnessof
LLM output, we propose to adopt a self-consistency method
(Wang et al. 2022b) which drawsn samples of Y ref from
LLM and sets the final output¯Y ref as "Yes" only when80%
ofY ref samples are "Yes". We usen= 5in experiments.
As shown in Figure 2, if the final reflection answer¯Y ref
is "Yes", thenat is applied to the environment. Otherwise,
the thought of reflection module which produces "No" is sent
back to the fast-thinking module and a new reactive action is
produced by calling the fast-thinking module again. If¯Y ref is
repeatedly not "Yes" forK number of times, sayK= 3 , the
slow thinking module is activated.
Slow Thinking Module
AsshowninFigure2,whenthefast-thinkingisunreliable,the
agenttransitionstotheslow-thinkingmodule,whichperforms
deliberative planning by explicitly searching over candidate
action sequences in a step-by-step manner. To handle the
uncertainty arising from partial observability, we propose a
novel neuro-symbolic uncertainty-aware planning algorithm
which follows the high-level framework of twisted sequential
Monte Carlo (TSMC) algorithm introduced in Section .
The proposed planning algorithm is illustrated in Figure
4. Specifically, the algorithm maintains a set of weighted
particles that represent possible future observations, latent
states (i.e., KGs), and actions over a planning horizonH. To
identify an optimal plan, these particles are guided toward
high-probability regions of a target distributionσ, which
corresponds to trajectories that successfully accomplish the
task. At each planning step, every particle is propagated
by predicting the next action, observation, and latent state
(KG). The particle weights are then updated according to the
likelihoodofthenewlypredictedstateachievingtaskprogress.
Finally,aresamplingprocedurebasedontheupdatedweights
preserves particles that make meaningful task progress while
filtering out less promising particles with a large probability.
To address the difficulty LLMs face in evaluating task
progress (Setlur et al. 2025; Zheng et al. 2025), particle
weights are updated using binary LLM feedback indicating
whether a given state transition makes task progress or not.
Moreover,theconcisestaterepresentationprovidedbyKGcan
improve the correctness of LLM judgment. In addition, the
resampling mechanism can make our approach more robust
to LLM’s mistakes, as it still allows promising particles to
survive even when they are temporarily misjudged by LLM.
Compared with previous tree-search planning methods,
such as MCTS (Chen et al. 2024), the proposed TSMC-style
method is better at addressing state uncertainty and more
computationally efficient. Previous methods are difficult at
predicting next state or observation under partial observabil-
ity, while the proposed method leverages memory KG to
accurately predict next KG by updating current KG with new
action and observation. In addition, in tree-search methods,
everyleafnodeisexpandedbypredictingmultiplenextstates
as child nodes. However, in the proposed method, particles
withpoortaskprogresswillbediscardedandnotbeexpanded

with a large probability, hence reducing the computation
complexity.
Definition.Denote N asnumberofparticles.Denoteparticle
iattheplanningstep τ as pi τ = ( ˆoi 1:τ , ˆG i 1:τ , ˆai 1:τ , ωi τ ),where
oi 1:τ = (ˆoi 1, . . . ,ˆoi τ )isthesequenceofobservationspredicted
by LLM until time stepτ, and same forˆG i 1:τ and ˆai 1:τ.
Initialization.Denote t0 as the time step when slow thinking
is activated. For each particle, set the first observation, latent
stateandactionascopiesoftheactualobservation,state(KG),
and action at time stept0, i.e.ˆoi 1 =o t0 , ˆGi 1 =G t0 ,ˆai 1 =a t0
for i= 1, . . . , N, so that every particle starts from the same
origin. Set the weight of each particle to be 1, i.e.ωi 1 = 1.
Propagation.As shown in the red box of Figure 4, in each
planning stepτ, every particlepi τ is propagated forward to
generate a new particlepi τ+1 by predicting the next action
ˆai τ+1, observationˆoi τ+1, and latent stateˆGi τ+1 one-by-one.
First, the next action is produced by an LLM-based policy,
describedas ˆai τ+1 =LLM(P fast;R( ˆGi τ ),ˆoi τ , η),where Pfast
is the prompt template used in the fast-thinking module, and
ηis the task description.
Subsequently,foreachparticle i,weneedtopredictthenext
observation ˆoi τ+1 caused by actionˆai τ+1. Specifically, task-
relevant context triplets are retrieved from the current KGˆGi τ
andusedasstateinformation,whichisthesameprocessasthe
retrieval R( ˆGi τ , η)describedinthefast-thinkingsection.Then
with these triplets andˆai τ+1 as input, LLM is prompted to
predictthenextobservation ˆoi τ+1.Thiscanbeformallywritten
as ˆoτ+1 =LLM(P obs;R( ˆGi τ , η),ˆai τ+1 ). In this prediction,
the LLM is asked to infer plausible future observations using
its commonsense knowledge and reasoning capabilities.
Then, ˆoi τ+1 is parsed into triplets which are incorporated
into ˆGi τ to produce the next latent state (KG)ˆGi τ+1, following
the process of updating KG introduced in the fast-thinking
section, i.e. ˆGi τ+1 =Update( ˆGi τ ,ˆoi τ+1 ,ˆaτ+1 ). The newly
acquired triplets in updating process are denoted asτnew.
Weight Update.As shown in the blue box of Figure 4,
each particle i is assigned a new weightωi τ+1 which is
updated as ωi τ+1 ←exp(λδ i τ+1 ). Specifically, δi τ+1 is
the task progress detector and is the LLM evaluation on
whether the transition( ˆGi τ ,ˆai τ , ˆGi τ+1 ) makes progress toward
task completion or not. Formally, we can writeδi τ+1 =
LLM(P prog; ˆai τ ,R( ˆGi τ ), τnew, η), wherePprog is the prompt
template in the task progress evaluation,δi τ+1 ∈ {0,1}, and
τnew is obtained in the propagation process. In contrast to
previous LLM-based evaluation methods (Zheng et al. 2025),
in our approach, the binary response of LLM and concise
representation provided by context triplets can reduce hallu-
cination and make LLM focus on task-related information in
the input.
Resampling.The resampling step is to probabilistically keep
particleswithgoodtaskprogressanddiscardparticleswithout
poor progress. At planning stepτ, the likelihood of a particle
ibeing kept is proportional to its weightωi τ.
Repeating the operations of propagation, weight update
and resampling over the planning horizonH, the remaining
particles are close to successful trajectories with a large prob-
ability.Thiscanbeguaranteedbythetheoreticalpropertiesof
TSMC (Del Moral, Doucet, and Jasra 2006). After planning
step H, uniformly sample a particlej∼Unif([1, . . . , N]),
and apply the first action in the particlej (i.e. ˆaj 1) to the
actual environment, as shown in Figure 2. The theoretical
justification is in Appendix .
Experiments
Experimental Settings
Benchmarks.We benchmarked NeSyFS on three widely
used text-based environments: ALFWorld (Shridhar et al.
2021),WebShop(Yaoetal.2022a),andScienceWorld(Wang
etal.2022a).ALFWorldevaluatesembodiedagentsonhouse-
hold tasks, WebShop (Yao et al. 2022a) emulates multi-step
decision-making tasks in an online shopping website envi-
ronment, and ScienceWorld (Wang et al. 2022a) assesses
procedural and scientific reasoning in educational scenarios.
For evaluation, ALFWorld uses binary task success, while
WebShop and ScienceWorld provide dense reward signals,
enabling evaluation based on both success rate and aver-
age reward, calculated as the mean reward across all tasks.
Additional benchmark details are presented in Appendix .
AgentModels.Intheevaluations,weuseGPT-5,GPT-5-mini
(Singh et al. 2025) and Llama-3.3-70B-Instruct (Grattafiori
et al. 2024) as the underlying models. GPT-5 variants serve
as proprietary models, while Llama-3.3 represents the open-
source counterpart.
In the following, we first conduct experiments to compare
the overall framework against some previous representative
methods. Then, the effect of reflection module is investi-
gatedempirically,independentlyoftheslow-thinkingmodule.
Finally, the performance of planning algorithm in the slow-
thinking module is specifically evaluated in Appendix by
removing the reflection module. Every result reported here is
an average of three random seeds.
Overall Evaluation
Baseline.Some representative decision making methods of
LLM agent are selected as baselines. Details of each baseline
are introduced in Appendix .
• ReAct (Yao et al. 2022b): This method reasons about
next action by using CoT (Wei et al. 2022), laying the
foundation of LLM decision making.
• Reflexion (Shinn et al. 2023): This method reflects every
failedtrajectoryandhelpsLLMsimproveaftereachfailed
attempt.
• ABBEL (Lidayan et al. 2025): It uses LLM to summarize
observation and full interaction history to infer the belief
state.
• RAFA (Liu et al. 2023): At each time step, the agent first
conducts a short-horizon planning through tree search,
executes the first action of the plan, and then replans at
next step.
• SwiftSage (Lin et al. 2023): In this fast-slow thinking
framework, the Swift module represents fast and intuitive
thinking,andtheSagemoduleplansandgroundssubgoals
to emulate deliberate thought processes.

Table 1: Performance comparison of NeSyFS with ReAct, Reflexion, RAFA and SwiftSage across ALFWorld, WebShop and
ScienceWorld. SR and AR denote success ratio and average reward, respectively.
Model Method ALFWorld WebShop ScienceWorld AverageSR AR SR AR SR
GPT-5-mini
ReAct 71.2 42.5 32.7 65.1 28.3 44.1
Reflexion 75.6 49.5 35.7 69.7 31.5 47.6
ABBEL 72.1 43.2 33.3 65.9 29.5 44.9
RAFA 73.5 40.1 27.3 70.2 34.5 45.1
SwiftSage 76.7 52.3 38.2 72.1 35.7 51.0
NeSyFS 91.1 61.2 51.3 82.2 61.2 63.5
GPT-5
ReAct 78.2 49.6 38.7 72.2 35.5 50.8
Reflexion 80.3 52.3 40.2 75.7 38.9 53.1
ABBEL 77.6 51.2 39.8 73.9 36.0 51.1
RAFA 83.2 48.1 35.3 76.3 42.7 53.7
SwiftSage 81.9 56.3 41.2 75.3 40.2 54.4
NeSyFS 93.6 69.4 63.3 86.1 69.4 75.3
Llama-3.3-70B
ReAct 79.6 45.6 37.1 69.2 33.1 49.9
Reflexion 81.2 47.3 38.9 73.1 36.9 52.3
ABBEL 78.6 45.1 36.9 70.1 32.5 49.3
RAFA 82.3 47.2 37.1 75.1 39.2 52.9
SwiftSage 80.6 51.2 39.9 76.1 41.3 53.9
NeSyFS 89.6 68.1 62.5 85.2 67.1 73.0
Results.Table 1 presents the performance comparison be-
tweenNeSyFSandseveralrepresentativebaselines,including
ReAct, Reflexion, ABBEL, RAFA, and SwiftSage, across
ALFWorld, WebShop, and ScienceWorld. The results show
that NeSyFS consistently and significantly outperforms all
baseline methods. In particular, NeSyFS achieves nearly a
100% improvement over ReAct and Reflexion, which serve
as the foundation of many state-of-the-art LLM agents, high-
lighting the effectiveness of the proposed KG-based memory,
reflection, and slow-thinking modules.
Furthermore, the substantial improvement over
summarization-based method, such as ABBEL, sug-
gests that KG-based contextual representations provide more
effective state representations for decision making than
summarization-based belief states, since the summarization
of history may lose critical information for belief updates.
RAFA performs short-horizon planning at each time step
through tree search, a mechanism conceptually related to
our slow-thinking module. The superior performance of
NeSyFS over RAFA therefore underscores the importance of
integrating KG-based memory and reflection mechanisms in
additiontoplanning.SwiftSagerepresentsatypicalfast–slow
thinking framework, and the advantage of NeSyFS further
demonstrates the benefits of KG-based memory in enhancing
the synergy between fast and slow reasoning processes.
Comparisons with previous KG-augmented LLM-agent
methods (Agarwal et al. 2025; Anokhin et al. 2025) are
provided separately in the next section.
KG-provided Context and Reflection
In this section, we first evaluate the correctness of the KG-
augmented reflection module, and then demonstrate the ad-
vantage and effect of KG-retrieved context triplets in the
overall task-completion evaluations.
The reflection module of NeSyFS leverages KG-retrieved
triplets as contextual information. In the first part of ex-
periment, to evaluate the effect of KG-provided context in
reflection, we compare the correctness of our reflection mod-
uleagainstbaselinesthatusetheentireinteractionhistoryand
LLM-summarized belief state as context, which are short as
"history" and "belief", respectively. The proposed reflection
method is short as "KG". All the methods are evaluated on a
setofrandomly-collectedtrajectoriesinwhichthecorrectness
of each action is manually annotated.
Weadopttwoevaluationmetrics.ThefirstisTotalDetection
Errors(TDE),definedasthesumoffalsepositives(misaligned
actions that are not detected) and false negatives (correct
actions incorrectly classified as misaligned). TDE measures
the overall number of reflection errors. The second metric is
EffectiveReliability(ER),definedas T P−F P T P+F P,where T Pand
F Pdenote the numbers of true positives and false positives,
respectively. Hence, ER evaluates the reliability of actions
that are approved by the reflection module.
The performance comparison is shown in Table 2. We can
see that the reflection method using KG-provided context
significantly outperforms that of using interaction history or
LLM-summarized belief state as context. This is because
KG-retrievedtripletscanprovideconcisestaterepresentation,
making the LLM focus on decision-making-related informa-
tion in the prompt when reflecting. Notably, the ER of "KG"
method is significantly higher than baselines, meaning that
KG-provided context could prevent more wrong actions from
beingappliedintotheenvironment."History"performsworse
since the noisy and redundant information in the interaction
history can distract LLM. The problem of "Belief" is that the
LLM-based summarization can lose important information.
Inthesecondpartoftheexperiment,weempiricallyinvesti-
gatetheeffectofKG-providedcontextwithinthefast-thinking

Table 2: Comparison of reflection with different representations of context.
Model Method ALFWorld WebShop ScienceWorld TDE ER TDE ER TDE ER
GPT-5
History 57 0.55 87 0.51 95 0.53
Belief 52 0.59 89 0.50 89 0.55
KG 42 0.71 61 0.66 77 0.65
GPT-5-mini
History 82 0.45 113 0.43 135 0.42
Belief 77 0.41 110 0.42 125 0.45
KG 58 0.65 72 0.58 91 0.59
(a) GPT-5-mini
(b) GPT-5
Figure 5: Performance comparison of different reflection
methods.
and reflection modules by comparing different methods of
forming the context to approximate the underlying environ-
ment state. Both GPT-5 and GPT-5-mini are used as the
underlying LLMs in these evaluations. The evaluation metric,
corresponding to y-axis in the plots, is the task success rate.
The methods “History Fast”, “Belief Fast”, and “KG Fast”
use the full interaction history, an LLM-summarized belief
state,andKG-retrievedtriplets,respectively,ascontextforac-
tion selection in the fast-thinking module, without employing
any reflection module or slow-thinking module. In contrast,
“History Ref”, “Belief Ref”, and “KG Ref” incorporate the
reflection module while using the same three forms of con-
text representations. Specifically, in the fast-thinking and
reflection modules, the KG is retrieved and updated using
the same procedures as those employed in NeSyFS, as de-
scribed in Section . Besides, the belief state is updated using
the same method as ABBEL introduced in Appendix . No
slow-thinkingmoduleisusedinanyoftheseevaluationshere.
Notably, the “Fast” method are conceptually equivalent to
previous KG-augmented LLM agents (Agarwal et al. 2025;
Anokhin et al. 2025).
AsillustratedinFigure5,incorporatingthereflectionmod-
uleconsistentlyimprovesperformanceacrossallbenchmarks.
Moreover, the use of KG-provided context leads to additional
performance gains, demonstrating both the importance of
reflectioninmitigatingmisalignmentwithtaskobjectivesand
the effectiveness of the symbolic, structured representations
provided by the KG.
Conclusion
In this work, we propose a neuro-symbolic framework which
addresses the challenges introduced by partial observability
in a unified manner. Under partial observability, the agent
may have difficulties on latent state inference, task objective
misalignment, and planning under uncertainty. In NeSyFS,
the latent state of the environment is represented and main-
tained as a memory KG, and triplets retrieved from KG are
used as context in every module of NeSyFS. In addition,
a KG-augmented reflection module is proposed to address
the misalignment of the task objective. Besides, a neuro-
symbolic TSMC-style planning algorithm is proposed to
tackle the uncertainty in observation prediction and task
progress evaluation. We empirically validate the proposed
framework and its modules in three popular benchmarks.
References
Abdulsamad,H.;Iqbal,S.M.;andSarkka,S.2026.Sequential
Monte Carlo for policy optimization in continuous POMDPs.
Advances in Neural Information Processing Systems, 38:
41241–41269.
Agarwal, K.; Jiang, Y.; Hu, J.; Liu, B.; and Stone, P. 2025.
L3M+ P: Lifelong Planning with Large Language Models.
In2025 IEEE/RSJ International Conference on Intelligent
Robots and Systems (IROS), 3344–3351. IEEE.
Anokhin, P.; Semenov, N.; Sorokin, A.; Evseev, D.;
Kravchenko, A.; Burtsev, M.; and Burnaev, E. 2025. Ari-
Graph:learningknowledgegraphworldmodelswithepisodic
memoryforLLMagents. InProceedingsoftheThirty-Fourth
International Joint Conference on Artificial Intelligence, 12–
20.
Chen, G.; Qiao, Z.; Chen, X.; Yu, D.; Xu, H.; Zhao, W. X.;
Song, R.; Yin, W.; Yin, H.; Zhang, L.; et al. 2025a. IterRe-
search: Rethinking Long-Horizon Agents with Interaction
Scaling.arXiv preprint arXiv:2511.07327.
Chen, Z.; Li, M.; Huang, Y.; Du, Y.; Fang, M.; and Zhou,
T. 2025b. Atlas: Agent tuning via learning critical steps. In
Findings of the Association for Computational Linguistics:
ACL 2025, 25334–25349.
Chen, Z.; White, M.; Mooney, R.; Payani, A.; Su, Y.; and
Sun, H. 2024. When is tree search useful for llm planning? it

depends on the discriminator. InProceedings of the 62nd An-
nualMeetingoftheAssociationforComputationalLinguistics
(Volume 1: Long Papers), 13659–13678.
Chopin,N.;Papaspiliopoulos,O.;etal.2020.Anintroduction
to sequential Monte Carlo, volume 4. Springer.
Chung, A.; Zhang, Y.; Lin, K.; Rawal, A.; Gao, Q.; and Chai,
J. 2025. Evaluating Long-Context Reasoning in LLM-Based
WebAgents. InNeurIPS Workshop on Bridging Language,
Agent, and World Models for Reasoning and Planning.
Del Moral, P.; Doucet, A.; and Jasra, A. 2006. Sequential
montecarlosamplers.JournaloftheRoyalStatisticalSociety
Series B: Statistical Methodology, 68(3): 411–436.
Doucet, A.; De Freitas, N.; and Gordon, N. 2001. An intro-
duction to sequential Monte Carlo methods. InSequential
Monte Carlo methods in practice, 3–14. Springer.
Ehrlinger, L.; and Wöß, W. 2016. Towards a definition of
knowledgegraphs.SEMANTiCS(Posters,Demos,SuCCESS),
48(1-4): 2.
Fang, H.; Zhu, X.; and Gurevych, I. 2025. Preemptive detec-
tion and correction of misaligned actions in llm agents. In
Proceedings of the 2025 Conference on Empirical Methods
in Natural Language Processing, 222–244.
Feng,L.;Xue,Z.;Liu,T.;andAn,B.2025a. Group-in-group
policy optimization for llm agent training.arXiv preprint
arXiv:2505.10978.
Feng, S.; Kong, X.; Ma, S.; Zhang, A.; Yin, D.; Wang, C.;
Pang, R.; and Yang, Y. 2025b. Step-by-Step Reasoning
for Math Problems via Twisted Sequential Monte Carlo.
InThe Thirteenth International Conference on Learning
Representations.
Francis, N.; Green, A.; Guagliardo, P.; Libkin, L.; Lindaaker,
T.; Marsault, V.; Plantikow, S.; Rydberg, M.; Selmer, P.; and
Taylor, A. 2018. Cypher: An evolving query language for
property graphs. InProceedings of the 2018 international
conference on management of data, 1433–1445.
Freitag,M.;andAl-Onaizan,Y.2017. Beamsearchstrategies
for neural machine translation. InProceedings of the First
Workshop on Neural Machine Translation, 56–60.
Gao, Y.; Xiong, Y.; Gao, X.; Jia, K.; Pan, J.; Bi, Y.; Dai, Y.;
Sun,J.;Wang,M.;andWang,H.2023. Retrieval-Augmented
Generation for Large Language Models: A Survey.arXiv
preprint arXiv:2312.10997.
Grattafiori,A.;Dubey,A.;Jauhri,A.;Pandey,A.;Kadian,A.;
Al-Dahle,A.;Letman,A.;Mathur,A.;Schelten,A.;Vaughan,
A.; et al. 2024. The llama 3 herd of models.arXiv preprint
arXiv:2407.21783.
He, J.; Chen, S.; Zhang, F.; and Yang, Z. 2024. From Words
toActions:UnveilingtheTheoreticalUnderpinningsofLLM-
Driven Autonomous Systems. InInternational Conference
on Machine Learning, 17807–17841. PMLR.
Jin,H.;Huang,L.;Cai,H.;Yan,J.;Li,B.;andChen,H.2024.
From llms to llm-based agents for software engineering: A
survey of current, challenges and future.arXiv preprint
arXiv:2408.02479.
Kahneman, D. 2011.Thinking, fast and slow. macmillan.
Kang, M.; Chen, W.-N.; Han, D.; Inan, H. A.; Wutschitz, L.;
Chen,Y.;Sim,R.;andRajmohan,S.2025. Acon:Optimizing
context compression for long-horizon llm agents.arXiv
preprint arXiv:2510.00615.
Kim, J.; Rhee, S.; Kim, M.; Kim, D.; Lee, S.; Sung, Y.; and
Jung, K. 2025. Reflact: World-grounded decision making in
llm agents via goal-state reflection. InProceedings of the
2025 Conference on Empirical Methods in Natural Language
Processing, 33421–33453.
Lei, Y.; Xu, J.; Liang, C. X.; Bi, Z.; Li, X.; Zhang, D.; Song,
J.; and Yu, Z. 2025. Large Language Model Agents: A
Comprehensive Survey on Architectures, Capabilities, and
Applications.
Li, H.; Liao, X.; et al. 2009. Multi-task Reinforcement
Learning in Partially Observable Stochastic Environments.
Journal of Machine Learning Research, 10(5).
Lidayan, A.; Bjorner, J. B.; Golechha, S.; and Suhr, A. 2025.
ABBEL: LLM Agents Acting through Belief Bottlenecks
Expressed in Language. InNeurIPS Workshop on Bridging
Language, Agent, and World Models for Reasoning and
Planning.
Lin, B. Y.; Fu, Y.; Yang, K.; Brahman, F.; Huang, S.; Bha-
gavatula, C.; Ammanabrolu, P.; Choi, Y.; and Ren, X. 2023.
Swiftsage: A generative agent with fast and slow thinking for
complex interactive tasks.Advances in Neural Information
Processing Systems, 36: 23813–23825.
Liu, Z.; Hu, H.; Zhang, S.; Guo, H.; Ke, S.; Liu, B.; and
Wang, Z. 2023. Reason for future, act for now: A principled
framework for autonomous llm agents with provable sample
efficiency.arXiv preprint arXiv:2309.17382.
Lu, M.; Sun, W.; Du, W.; Ling, Z.; Yao, X.; Liu, K.; and
Chen, J. 2025. Scaling llm multi-turn rl with end-to-end
summarization-based context management.arXiv preprint
arXiv:2510.06727.
Ma, C.; Zhang, J.; Zhu, Z.; Yang, C.; Yang, Y.; Jin, Y.; Lan,
Z.; Kong, L.; and He, J. 2024. Agentboard: An analytical
evaluationboardofmulti-turnllmagents.Advancesinneural
information processing systems, 37: 74325–74362.
Macfarlane, M.; Toledo, E.; Byrne, D. J.; Duckworth, P.;
and Laterre, A. 2024. Spo: Sequential monte carlo policy
optimisation. InThe Thirty-eighth Annual Conference on
Neural Information Processing Systems.
Pan, Z.; Wu, Q.; Jiang, H.; Luo, X.; Cheng, H.; Li, D.; Yang,
Y.; Lin, C.-Y.; Zhao, H. V.; Qiu, L.; et al. 2026. SeCom: On
Memory Construction and Retrieval for Personalized Conver-
sational Agents. InThe Thirteenth International Conference
on Learning Representations.
Piché, A.; Thomas, V.; Ibrahim, C.; Bengio, Y.; and Pal, C.
2018. Probabilistic planning with sequential monte carlo
methods. InInternational Conference on Learning Represen-
tations.
Qin, Y.; Liang, S.; Ye, Y.; Zhu, K.; Yan, L.; Lu, Y.; Lin, Y.;
Cong,X.;Tang,X.;Qian,B.;etal.2023. Toolllm:Facilitating
largelanguagemodelstomaster16000+real-worldapis.arXiv
preprint arXiv:2307.16789.

Rawat, M.; Gupta, A.; Goomer, R.; Di Bari, A.; Gupta, N.;
and Pieraccini, R. 2025. Pre-act: Multi-step planning and
reasoning improves acting in llm agents.arXiv preprint
arXiv:2505.09970.
Renze, M.; and Guven, E. 2024. Self-reflection in llm agents:
Effects on problem-solving performance.arXiv preprint
arXiv:2405.06682.
Rodriguez, A.; Parr, R.; and Koller, D. 1999. Reinforcement
learning using approximate belief states.Advances in Neural
Information Processing Systems, 12.
Roy,N.;Gordon,G.;andThrun,S.2005.Findingapproximate
POMDP solutions through belief compression.Journal of
artificial intelligence research, 23: 1–40.
Schick, T.; Dwivedi-Yu, J.; Dessì, R.; Raileanu, R.; Lomeli,
M.; Hambro, E.; Zettlemoyer, L.; Cancedda, N.; and Scialom,
T. 2023. Toolformer: Language models can teach themselves
to use tools.Advances in neural information processing
systems, 36: 68539–68551.
Setlur, A.; Nagpal, C.; Fisch, A.; Geng, X.; Eisenstein, J.;
Agarwal, R.; Agarwal, A.; Berant, J.; and Kumar, A. 2025.
RewardingProgress:ScalingAutomatedProcessVerifiersfor
LLM Reasoning. InThe Thirteenth International Conference
on Learning Representations.
Shinn, N.; Cassano, F.; Gopinath, A.; Narasimhan, K.; and
Yao, S. 2023. Reflexion: Language agents with verbal rein-
forcement learning.Advances in neural information process-
ing systems, 36: 8634–8652.
Shridhar, M.; Yuan, X.; Côté, M.-A.; Bisk, Y.; Trischler, A.;
and Hausknecht, M. 2020. Alfworld: Aligning text and em-
bodied environments for interactive learning.arXiv preprint
arXiv:2010.03768.
Shridhar, M.; Yuan, X.; Cote, M.-A.; Bisk, Y.; Trischler,
A.; and Hausknecht, M. 2021. ALFWorld: Aligning Text
and Embodied Environments for Interactive Learning. In
International Conference on Learning Representations.
Singh, A.; Fry, A.; Perelman, A.; Tart, A.; Ganesh, A.;
et al. 2025. Openai gpt-5 system card.arXiv preprint
arXiv:2601.03267.
Song, Y.; Yin, D.; Yue, X.; Huang, J.; Li, S.; and Lin, B. Y.
2024. Trial and error: Exploration-based trajectory optimiza-
tion of LLM agents. InProceedings of the 62nd Annual
Meeting of the Association for Computational Linguistics
(Volume 1: Long Papers), 7584–7600.
Wang, R.; Jansen, P.; Côté, M.-A.; and Ammanabrolu, P.
2022a. Scienceworld:Isyouragentsmarterthana5thgrader?
InProceedingsofthe2022ConferenceonEmpiricalMethods
in Natural Language Processing, 11279–11298.
Wang, X.; Wei, J.; Schuurmans, D.; Le, Q.; Chi, E.; Narang,
S.; Chowdhery, A.; and Zhou, D. 2022b. Self-consistency
improves chain of thought reasoning in language models.
arXiv preprint arXiv:2203.11171.
Wei, J.; Wang, X.; Schuurmans, D.; Bosma, M.; Xia, F.; Chi,
E.;Le,Q.V.;Zhou,D.;etal.2022. Chain-of-thoughtprompt-
ing elicits reasoning in large language models.Advances in
neural information processing systems, 35: 24824–24837.
Xi, Z.; Ding, Y.; Chen, W.; Hong, B.; Guo, H.; Wang, J.;
Yang, D.; Liao, C.; Guo, X.; He, W.; et al. 2024. Agentgym:
Evolving large language model-based agents across diverse
environments.arXiv preprint arXiv:2406.04151.
Xiang, X.; and Foo, S. 2021. Recent advances in deep
reinforcement learning applications for solving partially ob-
servable markov decision processes (pomdp) problems: Part
1—fundamentals and applications in games, robotics and nat-
ural language processing.Machine Learning and Knowledge
Extraction, 3(3): 554–581.
Yamada, Y.; Lange, R. T.; Lu, C.; Hu, S.; Lu, C.; Foerster, J.;
Clune, J.; and Ha, D. 2025. The ai scientist-v2: Workshop-
level automated scientific discovery via agentic tree search.
arXiv preprint arXiv:2504.08066.
Yao, S.; Chen, H.; Yang, J.; and Narasimhan, K. 2022a.
Webshop: Towards scalable real-world web interaction with
grounded language agents.Advances in Neural Information
Processing Systems, 35: 20744–20757.
Yao, S.; Zhao, J.; Yu, D.; Du, N.; Shafran, I.; Narasimhan,
K. R.; and Cao, Y. 2022b. React: Synergizing reasoning and
acting in language models. InThe eleventh international
conference on learning representations.
Zhang,G.;Geng,H.;Yu,X.;Yin,Z.;Zhang,Z.;Tan,Z.;Zhou,
H.; Li, Z.-Z.; Xue, X.; Li, Y.; et al. 2025. The Landscape
of Agentic Reinforcement Learning for LLMs: A Survey.
Transactions on Machine Learning Research.
Zhang, J.; Lan, T.; Murthy, R.; Liu, Z.; Yao, W.; Zhu, M.;
Tan, J.; Hoang, T.; Liu, Z.; Yang, L.; et al. 2024. Agentohana:
Design unified data and training pipeline for effective agent
learning.arXiv preprint arXiv:2402.15506.
Zhao, A.; Huang, D.; Xu, Q.; Lin, M.; Liu, Y.-J.; and Huang,
G. 2024a. Expel: Llm agents are experiential learners. In
ProceedingsoftheAAAIConferenceonArtificialIntelligence,
volume 38, 19632–19642.
Zhao, S.; Brekelmans, R.; Makhzani, A.; and Grosse, R. B.
2024b. Probabilistic Inference in Language Models via
TwistedSequentialMonteCarlo. InInternationalConference
on Machine Learning, 60704–60748. PMLR.
Zheng, C.; Zhu, J.; Ou, Z.; Chen, Y.; Zhang, K.; Shan,
R.; Zheng, Z.; Yang, M.; Lin, J.; Yu, Y.; et al. 2025. A
survey of process reward models: From outcome signals
to process supervisions for large language models.arXiv
preprint arXiv:2510.08049.

Algorithm Description
Algorithm1:Neuro-symbolicFast-slowThinkingFramework
for LLM Agent
Require: Task descriptionη; memory KGG; number of re-
flections for one fast-thinking actionK; prompts for fast-
thinking action generationPfast and reflectionPref; oper-
ationsofupdatingKG Update(G, o, a)andretrievalfrom
KG R(G, η); planning algorithm in the slow-thinking
module TSMC-plan(η,G, o), described in Algorithm 2;
1:Initialize the memory KGG0 ← ∅;
2: Initialize the environment and get initial observationo0;
3:fort= 1, . . . , Hdo
4:a t ∼LLM(P fast;R(G t−1, η), ot−1, η);%Generate
fast-thinking action
5:k←0;
6:whilek < Kdo
7:¯r, h∼LLM(P ref;a t, ot−1,R(G t−1, η), η);
%Reflect with thinking step-by-step, wherehis the think-
ing of reflection
8:if¯ris Nothen
9:a t ∼LLM(P fast;R(G t−1, η), ot−1, η, h);
%Generate fast-thinking action with reflection thinking
10:k←k+ 1;
11:else
12:Break;
13:end if
14:end while
15:ifk≥Kthen
16: ˆG ← Gt−1;%Copy current KG
17:a t ∼TSMC-plan(η, ˆG, at, ot−1);Initiate the
planning algorithm in the slow-thinking module
18:end if
19: Apply at into the environment, and obtain new ob-
servationo t and rewardrt;
20:G t ←Update(G t−1, ot, at);
21:end for
The algorithm table of the proposed NeSyFS framework is
presented in Algorithm 1. In every iteration, the fast-thinking
action is first generated in line 4. Then, from line 5 to 14, the
reflection is conducted to ensure the alignment of action and
task objective. If reflection fails repeatedly, the slow-thinking
moduleisinitiatedinline16,wherethefirstactionofthebest
particle is produced as output. In line 18, the selected action
at isappliedintotheenvironment.Inline19,thememoryKG
is updated with actionat and new observationot. In every
experiment, if not stated specifically,Kis selected to be3.
The proposed planning algorithm in the slow-thinking
module is presented in Algorithm 2. The operations for
propagation of every particle is conducted in lines 4, 5 and
6. The weight update of every particle is from line 7 to 8.
Resamplingisfromline10to14,wherethehistoricalactions
of every particle are kept in the particle replacement. Finally,
inline17,thefirstaction ˆal 2,nottheinitialone a0,isreturned.
In every experiment, the number of particlesN is set to 6,
and the planning horizonL is 5. Because the observation
prediction may not be accurate and prediction mistakes can
Algorithm 2: TSMC-plan(η,G0, a0, o0)
Require: Task description η; initial memory KGG0; ini-
tial observation o0; number of particlesN; planning
horizon L; prompts for fast-thinkingPfast, observation
prediction Pobs and task progress detection Pprog in
the slow-thinking module; Operation of updating KG
Update(G, o, a)and retrieval from KGR(G, η);
1: Initialize ˆoi 1 ←o 0, ˆGi 1 ← G0,ˆai 1 ←a 0, for i=
1, . . . , N;
2:forτ= 2, . . . , Ldo
3:fori= 1, . . . , Ndo
4:ˆa i τ ←LLM(P fast;R( ˆGi τ−1 , η),ˆoi τ−1 , η);
5:ˆo i τ ←LLM(P obs;R( ˆGi τ−1 , η),ˆai τ );
6: ˆGi τ ←Update( ˆGi τ−1 ,ˆoi τ ,ˆai τ ), where the newly
acquired triplets are denoted asνi new;
7:δ i τ ←LLM(P prog; ˆai τ−1 ,R( ˆGi τ−1 , η), νi new, η);
8:ω i τ ←exp(λδ i τ );
9:end for
10: Define new particles ({˜ai ι}τ ι=1,˜oi, ˜Gi, ˜δi,˜ωi)←
({ˆai ι}τ ι=1,ˆoi τ , ˆGi τ , δi τ , ωi τ ), fori= 1, . . . , N;
11:fori= 1, . . . , Ndo
12:Samplej∼Categorical(˜ω 1, . . . ,˜ωN );
13:({˜a i ι}τ ι=1,ˆoi τ , ˆGi τ , δi τ , ωi τ )←
({˜aj ι }τ ι=1,˜oj, ˜Gj, ˜δj,˜ωj);
14:end for
15:end for
16:Samplel∼Uniform(1, . . . , N);
17:returnˆa l 2;
be accumulated along the time axis,L cannot be too large.
In order to control the token consumption,N cannot be too
large as well. The temperature parameterλis selected to 1.
Related Work
In traditional RL, partial observability is addressed by esti-
matingthebeliefstate(Rodriguez,Parr,andKoller1999;Roy,
Gordon, and Thrun 2005; Li, Liao et al. 2009), maintaining
anestimateofthelatentenvironmentstate.However,suchap-
proaches typically rely on accurate knowledge or estimate of
transitionorobservationmodels(XiangandFoo2021),which
are difficult to satisfy in complex and heterogeneous agentic
settings. In LLM, many previous works on LLM agents ad-
dress partial observability by treating interaction history as a
surrogateforthelatentstate(Yaoetal.2022b;Maetal.2024;
Xi et al. 2024; Shinn et al. 2023; Zhao et al. 2024a; Lei et al.
2025). However, because agentic data are typically collected
under outcome-level supervision—where a single terminal
success signal is assigned to an entire episode—such histo-
ries frequently contain weakly informative or task-irrelevant
content. Consequently, conditioning the decision making of
LLM on full trajectories entangles state-relevant signals with
spuriousdetails(Chungetal.2025),incurssubstantialcompu-
tational overhead (Kang et al. 2025), and ultimately degrades
performance (Lei et al. 2025).
Some previous work on the LLM agent has leveraged

Old State
 Updated State
Retrieved
TripletsRetriever
Target
+
Triplets
Target
-
Triplets
Obs. t
Action t
New
Triplets
Figure 6: Diagram of updating KG with new observationot
and actionat.
recent advances in context management to address partial
observability and has largely focused on the summarization
and retrieval of interaction histories, including compression-
based summarization and segmented memory retrieval (Lu
et al. 2025; Kang et al. 2025; Chen et al. 2025a; Lidayan
et al. 2025; Pan et al. 2026). While effective for control-
ling context length, these approaches implicitly assume that
the interaction history—whether summarized or selectively
retrieved—constitutes an adequate representation of the un-
derlying state. This assumption introduces additional com-
putational overhead and renders agents susceptible to infor-
mation loss. Besides, unstructured memory (e.g., full history,
compression-based summarization) stores information as
disconnected text fragments, making it difficult to retrieve
logically related facts. In contrast, our framework uses struc-
tured memory, organizing knowledge as a graph. A recent
work (Agarwal et al. 2025) uses an external knowledge graph
to represent the latent state for LLM agent. However, this
work assumes that domain knowledge of the environment, i.e.
PDDL, is provided, and it does not challenges of reconciling
knowledge gap and planning under uncertainty which are
introduced by partial observability.
In addition, many agentic approaches prioritize aligning
LLMs for effective interaction rather than learning com-
pact state representations from histories. For instance, (Qin
et al. 2023; Zhang et al. 2024) unify instruction-following
pipelines, while methods such as Exploration-based Trajec-
tory Optimization (Song et al. 2024) and Group-in-Group
Policy Optimization (Feng et al. 2025a) optimize behavior
using trajectory-level or group-level feedback. AgentEvol
(Xi et al. 2024) incorporates RL rewards into supervised
fine-tuning(SFT),and(Chenetal.2025b)demonstratesgains
from curated interaction subsets. However, these approaches
still uniformly treat the full action–observation history as the
state representation, and their training or fine-tuning process
of LLM is expensive and can incur significant computational
overhead. In contrast, our framework does not change any
parameters of pre-trained LLMs.
Supplementary Materials to Methodology
In this section, we present more details about the proposed
NeSyFS framework.
Fast-thinking Module
Update to KGThe diagram of updating KGGt with new
observation ot and action at is shown in Figure 6, where
ot is the response of the environment toat. Given a new
observation ot, the LLM agent first parsesot into a set of
entities vt and tripletsτt describing attributes and relations
of vt. For example, an observation may generate triplets such
as (apple 1,at,sidetable 1)or (you,cleaned,tomato 1). The
extracted triplets are then filtered by removing those already
contained in the KGGt, resulting in a set of new tripletsτnew
extractedfrom ot.Toidentifypreviouslystoredknowledgere-
latedtotheentitiesin vt,theagentretrievesfrom Gtalltriplets
connected to these entities, denoted as the set of existing
triplets τold. The LLM is subsequently prompted to compare
τnew and τold in order to determine which triplets inτold have
become outdated and should be replaced by corresponding
triplets inτnew. For example, the triplet(you,at,cabinet 1) in
τold may be replaced by(you,at,fridge 1) in τnew to reflect
a change in the entity’s location. Finally, according to the
LLM’s output, outdated triplets are removed fromGt and
replaced with updated triplets inτnew, thereby updatingGt
witho t and producing KGGt+1 for next time step.
Retrieval from KGGiven the task descriptionη (e.g., “put
acooleggintoamicrowave”),ratherthanprovidingtheentire
KG Gt to LLM, our approach first retrieves task-relevant
triplets τt from Gt and usesτt as context for decision making.
Specifically,bypromptingLLM,thelastobservation otisfirst
parsedintoentities vq andrelations Eq whicharerelatedwith
solving the taskη. Subsequently, all incoming and outgoing
triplets associated with each entity inVq are retrieved from
the present KGGt up to a predefined maximum depth, and
retrieved triplets are denoted asτt. The tripletsτt are then
suppliedtotheLLMasstructuredcontextforreactivedecision
making in fast thinking. In addition, the KG and retrieval
method introduced above are also used in the slow thinking
and reflection modules. This KG retrieval method is denoted
asR(·,·).
Slow-thinking Module
Denoteatrajectoryas ξT ={x t}T t=1where xt = (ot,G t, at),
representing observation, latent state (KG), and action at
time step t, respectively. The target distributionσ(ξT ) is
defined as the distribution of trajectories that complete the
task successfully.
Theoretical Justification.Unlike standard sequential
Monte Carlo (SMC) methods (Del Moral, Doucet, and Jasra
2006), we employ twisted SMC (TSMC), which introduces
a sequence of twist functions{ψτ }T−1 τ=1 to bias intermediate
particle distributions toward high-probability regions of the
target distributionσ(ξT ). For a general proposal distribution
q, prior work (Zhao et al. 2024b; Feng et al. 2025b) defines
the incremental importance weight as
ωk τ ← p0(sk τ |s k 1:τ−1 ) q(skτ |s k 1:τ−1 ) ψτ (sk 1:τ ) ψτ−1 (sk 1:τ−1 ) , τ < T;
ωk τ ← p0(sk τ |s k 1:τ−1 ) q(skτ |s k 1:τ−1 ) ϕ(sk 1:τ ) ψτ−1 (sk 1:τ−1 ) , τ=T(1)
Here, p0 and q denote, respectively, the base-model distribu-
tion and the proposal distribution conditioned on the current

history. The twist functionψτ (x1:τ ) is designed so that the
twisted intermediate distribution better approximates the cor-
respondingtargetmarginal σ(x1:τ ).Inparticular,theoptimal
twist is proportional to the expected terminal potential under
future rollouts of the base model and can therefore be inter-
preted as a value-like quantity measuring the expected future
utility of a partial trajectory (Zhao et al. 2024b). Specifically,
ψ∗ τ (x1:τ )∝E p0 [ϕ(x1:T )|x 1:τ ].(2)
This interpretation provides the theoretical basis for relat-
ing the twist ratio to task progress in our planning formu-
lation. Specifically, consider particlei and the transition
ˆGi τ ,ˆai τ , ˆGi τ+1

. We useδi τ+1 in Algorithm 2 to indicate
whether this transition makes measurable progress toward
taskcompletion.Sincetheratio
ψτ+1 (xi 1:τ+1 )
ψτ (xi 1:τ ) measurestherel- ativeincreaseintheestimatedfuturevalueoftheparticleafter
the transition, it is natural to parameterize this multiplicative
change as
ψτ+1 (xi 1:τ+1 )
ψτ (xi 1:τ ) ≈exp

λδi τ+1  , λ >0.(3)
Under this parameterization, when no progress is detected,
δi τ+1 = 0, we obtainexp  λδi τ+1  = exp(0) = 1, so that the
incremental weight remains unchanged. In contrast, when
progress is detected,δi τ+1 >0 , we haveexp  λδi τ+1  >1 ,
therebyassigninggreaterweighttoparticleswhosetransitions
advance the task. The coefficientλ therefore controls the
strength of the progress-based preference.
In our implementation, the same pretrained LLM, e.g.,
GPT-5, is used both as the base model and as the proposal
model. This corresponds to the "base model as proposal"
setting of (Zhao et al. 2024b), for whichq(sk τ |s k 1:τ−1 ) =
p0(sk τ |s k 1:τ−1 ).Consequently,theproposal-correctionfactor
in (1)cancels. The incremental weight therefore simplifies to
ωk τ ← ψτ (sk 1:τ ) ψτ−1 (sk 1:τ−1 ) , τ < T
ωk τ ← ϕ(sk 1:τ ) ψτ−1 (sk 1:τ−1 ) , τ=T(4)
Combining (4) with the progress-based approximation in
(3), the incremental weight for particlei can be written
as ωi τ+1 ≈exp  λδi τ+1  . This establishes the connection
between the progress-based weighting rule in Algorithm 2
andtheincrementalimportanceweightsofTSMC(DelMoral,
Doucet, and Jasra 2006; Feng et al. 2025b).
Experiments
Benchmarks
The detailed introduction of benchmarks is as follows.
• ALFWorld(Shridhar et al. 2021): ALFWorld is a text-
based benchmark derived from the ALFRED dataset,
designed to evaluate an agent’s ability to interpret and
execute natural-language instructions in interactive, multi-
step household environments. By transforming embod-
ied vision-and-language tasks into textual interactions,
it enables systematic evaluation of high-level planning,
language grounding, and sequential decision-making ca-
pabilities within a simulated environment.
• WebShop(Yao et al. 2022a): WebShop is a large-scale
simulated e-commerce benchmark developed for study-
ing grounded language agents in realistic web-interaction
settings. Given a natural-language shopping instruction
specifying product requirements, an agent must navigate
diverse webpage types—including search pages, result
pages, product pages, and product-detail pages—while
performing actions such as generating search queries,
selecting products, choosing item options, reading de-
scriptions, backtracking, and ultimately purchasing the
desired item.
• ScienceWorld(Wangetal.2022a):ScienceWorldisatext-
basedbenchmarkdesignedtoevaluateagentsonscientific
reasoning and procedural task completion. Grounded in
standardizedK–12sciencecurricula,itassessesanagent’s
ability to follow instructions, conduct virtual experiments,
perform causal reasoning, and manipulate objects across
domains such as physics, chemistry, and biology. The
benchmark emphasizes multi-step interaction, hypothesis
testing,andlanguagegroundingindynamicenvironments.
Baselines
The baselines are introduced as below with details.
• ReAct(Yaoetal.2022b):Thismethodlaysthefoundation
for many decision-making methods of LLM agent. In
ReAct,theagentfirstreasonsaboutthenextactionateach
timestepbyusingCoT(Weietal.2022)andthengenerates
an action. The full interaction history is appended into the
prompt for the LLM to infer the latent state. The source
code of ReAct is at https://github.com/ysymyth/ReAct
• Reflexion (Shinn et al. 2023): built upon ReAct, this
method proposes a multi-round approach enabling the
LLM agent to use the history of previously failed trajecto-
ries to refine their planning for the next round. At the end
of every failed episode, the LLM agent infers the reason
why it fails based on the full trajectory, and append the
inferred experience into the prompt to improve its future
decision making. We evaluate Reflexion with 2 shots. The
source code is at https://github.com/noahshinn/reflexion
• ABBEL (Lidayan et al. 2025): ABBEL is a framework for
long-horizonLLMagentsthatreplacesthefullinteraction
history with a compact natural-language “belief state.”
At each step, the agent first updates its belief using the
latestobservation,thenselectsthenextactionconditioned
only on this belief rather than the entire trajectory. This
createsabeliefbottleneckthatkeepsmemoryusagenearly
constant while maintaining interpretability and reasoning
ability. Since each update of belief state can lose some
information, instead of updating at every time step, we
store each observation and update the belief state together
with stored observations only when the length of stored
observations exceeds a threshold. In its implementation,
we modify the ReAct code by using the same prompts as
the original paper.

Table 3: Comparison of proposed task progress detector and baselines.
Model Method ALFWorld WebShop ScienceWorld TDE ER TDE ER TDE ER
GPT-5
History 45 0.61 97 0.55 89 0.58
Belief 40 0.63 87 0.57 78 0.61
Fraction 89 0.51 132 0.46 105 0.49
Proposed 29 0.73 69 0.62 53 0.72
GPT-5-mini
History 63 0.56 112 0.49 99 0.51
Belief 54 0.52 101 0.47 85 0.57
Fraction 102 0.45 153 0.41 124 0.47
Proposed 36 0.69 87 0.57 62 0.65
• RAFA (Liu et al. 2023): This method integrates rea-
soning, planning and acting through an RL perspective.
At each step, the agent first conducts planning through
tree search, executes the first action of the plan, receives
feedback from environment, and then replans at next
step. During planning, the LLM uses past trajectories
as in-context examples to simulate the environment dy-
namics and estimate value functions. For every task, only
the initial episode is executed. The source code is at
https://github.com/agentification/RAFA_code
• SwiftSage (Lin et al. 2023): This is a popular fast-slow
thinking framework consisting of Swift and Sage mod-
ules, where the Swift module represents fast and intu-
itive thinking, and the Sage module plans and grounds
subgoals to emulate deliberate thought processes. For
the fairness of comparison, we do not fine-tune the
LLM in the Swift module and make it the same as
that in the Sage module. The source code is at https:
//github.com/SwiftSage/SwiftSage/tree/science_world
Planning Evaluation
In the slow-thinking module of NeSyFS, we propose a novel
uncertainty-aware planning algorithm that follows the high-
level framework of twisted sequential Monte Carlo (TSMC).
First, we assess the accuracy of the task progress detector
δi t, which is used to update particle weights in the planning
algorithm. Second, we investigate the effect of the proposed
planning method on improving the overall task-completion
performance.
Intheproposedplanningalgorithm,theparticlesarefiltered
by resampling based on weights, so weight update is the key
to guide the particles toward the distribution of successful
trajectories and find the optimal action plan. Since weight
update is based on the task progress detectorδi t, in the first
part of the experiments, we need to evaluate the accuracy
of δi t. Following the previous section, we adopt the total
detection error (TDE) and effective reliability (ER) as the
evaluation metrics. In contrast, here false positive (FP) refers
to transitions that do not make task progress but detected
as positive, and false negative (FN) refers to transitions that
make task progress but detected as negative. We compare
our δi t with two baselines here. In the first baseline, short as
"History", the input state (context) to our detector is replaced
withtheentireinteractionhistoryintext.SameastheABBEL
described above , the input state in the second baseline, short
(a) GPT-5-mini
(b) GPT-5
Figure 7: Performance Comparison of fast-slow thinking
frameworks with different slow-thinking modules.
as"Belief",isthebeliefstateupdatedbyLLMwithsummary
of previous belief state and recent observation. The third
baseline, short as "Fraction", is the same as the critics in
RAFA (Liu et al. 2023) which prompts LLM to produce an
estimate of progress toward task completion, i.e. a fraction
between 0 and 1.
For every environment, all the methods are evaluated on a
set of randomly pre-collected trajectories, where the ground
truth label of making task progress is manually labeled. In
"Fraction"method,onlythestatetransitionwhosecriticvalue
is higher than the previous state in the same trajectory is
labeled as progressive transition. In Table 3, we demonstrate
the comparison of the proposed detector and baselines. It
is obvious that the proposed detector outperforms baselines
significantly. It performs better than "History", because the
KG-retrieved triplets in the proposed method provide concise
state representations and can prevent the LLM from being
distracted by redundant and noisy information in the raw text
of"History"baseline."Belief"performsbetterthan"History",
since it uses LLM to summarize and update belief state with
recent observations, but the LLM-based summary in "Belief"
may lose some important information for decision making,
making "Belief" performs worse than the proposed method.
"Fraction" method performs the worst, since the factional
output in the estimate of task progress is more difficult for
LLM to detect than the binary output.

In the second part of the experiments, we investigate
how much the proposed planning algorithm can improve the
overalltask-completionperformanceofthefast-slowthinking
framework. We design two baselines by replacing the slow-
thinkingmoduleofNeSyFSanddiscardthereflectionmodule,
keeping other parts unchanged. First, we use the Sage part of
SwiftSageagent(Linetal.2023)astheslow-thinkingmodule
which reasons about target subgoal to achieve which is then
appended as subgoal to the prompt of fast-thinking module,
short as "Fast+Sage". Second, we adopt beam search (Setlur
et al. 2025; Freitag and Al-Onaizan 2017) to realize the slow-
thinking module of NeSyFS, short as "Fast+Beam", which
expands every sequence in the beam using 3 next actions,
computes scores, and selects 2 best sequences with highest
score in the expanded sequences to keep in the next iteration
with other sequences discarded. The score of every sequence
in the beam is the sum of task progress values estimated by
δi t. In the "proposed" slow-thinking module, the number of
particlesissetto N= 6 .InbothBeamandproposedmethod,
theplanninghorizonintheslowthinkingischosenas H= 5 .
The performance comparison of NeSyFS and baselines is
shown in Figure 7. These evaluations use GPT-5-mini and
GPT-5 as the base LLMs. To rule out the influence of other
factors, in every evaluated fast-slow thinking framework, the
slow-thinking module is initiated in every 3 steps, and the
reflection module is discarded. We can see that the proposed
planning algorithm in NeSyFS outperforms than other slow-
thinkingmethods.Fast+Sageperformsworstbecauseitsimply
reasons the next subgoal to achieve in the slow-thinking
module, which is not as efficient as the step-by-step planning
in beam search and NeSyFS, since setting the next subgoal
only does not provide clear guidance on the exact next action
to take. Fast+Beam is outperformed by NeSyFS, because
the beam search simply selects the best 2 sequences and
discards others, which is not robust to the mistakes of LLM-
based evaluation on task progress, which can be resolved by
the sampling mechanism in the proposed planning method.
Note that the margin between NeSyFS and others is larger
in WebShop, because the content of website is difficult to
predict and hence the prediction of next observation is more
difficult in WebShop.
Comparison with Tree-search Planning Method
In this section, we compare the planning algorithm employed
in the slow-thinking module of NeSyFS with a conventional
tree-search-basedplanningapproach.Specifically,wereplace
the proposed planning algorithm with the tree-search method
introducedin RAFA (Liuetal. 2023),whilekeepingallother
components of NeSyFS unchanged, thereby constructing a
controlled baseline for comparison. We select RAFA because
its planning procedure represents a relatively fundamental
form of tree-search-based planning, enabling a clear eval-
uation of the differences between the two approaches. To
ensure a fair comparison, the baseline uses the same memory
knowledge graph and observation-prediction mechanism as
NeSyFS.
For both NeSyFS and the baseline, the maximum number
of reflections is set to (K= 1 ). In NeSyFS, the planning
horizon and number of particles are set to (L= 5 ) and
(N= 6 ),respectively.Toensureafaircomparison,thesearch
breadth and search depth of the tree-search baseline are set to
6 and 5, i.e., (B= 6, U= 5). We evaluate the two methods
on all 134 tasks in ALFWorld and the first 100 tasks in
WebShop. Performance is assessed using two metrics: token
consumption (TC), measured in millions of tokens, and task
success rate (SR).
Table 4: Comparison of proposed and basic tree-search plan-
ning method.
Model Method ALFWorld WebShop TC SR TC SR
GPT-5 Baseline 49 0.96 62 0.67 NeSyFS 15 0.92 21 0.64
GPT-5-mini Baseline 56 0.93 69 0.58 NeSyFS 17 0.90 29 0.53
The comparison results are presented in Table 4. The tree-
searchbaselineachievesamodestimprovementintasksuccess
rate but incurs substantially greater token consumption. This
high cost arises because tree-search planning expands multi-
ple successor states of every state at each step, causing the
number of evaluated states to grow exponentially with the
planningdepth.Incontrast,theTSMC-styleplanningmethod
employed by NeSyFS probabilistically eliminates particles
associated with limited task progress while maintaining a
fixed number of particles at each planning step. Although
exhaustive tree search can evaluate a broader range of pos-
sible future trajectories and may therefore attain a slightly
highersuccessrate,predictingandassessingthesetrajectories
requiresconsiderableamountoftokensandcomputationalre-
sources. By selectively discarding unpromising particles, the
proposedplanningalgorithmachievesamorefavorabletrade-
off between task-completion performance and computational
complexity.
