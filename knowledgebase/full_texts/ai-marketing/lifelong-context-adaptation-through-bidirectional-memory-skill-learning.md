---
title: Lifelong Context Adaptation through Bidirectional Memory-Skill Learning
url: https://arxiv.org/abs/2610.32295
category: ai-marketing
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Tianyi Xu
- Huazheng Wang
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.32295
pages: 42
chars: 135119
fetched_at: '2026-11-08T13:35:53+00:00'
kb_version: 1
---

# Lifelong Context Adaptation through Bidirectional Memory-Skill Learning

Lifelong Context Adaptation through Bidirectional Memory–Skill Learning
Tianyi Xu Huazheng Wang *
Oregon State University
{xut2, huazheng.wang}@oregonstate.edu
Abstract
Lifelong LLM agents must learn from an ex-
panding history of interactions while making
each decision within a bounded context win-
dow. Memory makes past experience available,
but the agent may still need to infer how to
solve each new task from the retrieved records.
Skills provide reusable procedures, yet may
omit the task-specific facts needed to apply
them. Because retrieved memory and skills
shape the agent’s behavior, they also influ-
ence the experience available for future learn-
ing. We introduce MEMCRYST, a framework
for lifelong context adaptation through bidi-
rectional learning of memory and skills with
a frozen language model. Recurring episodes
stored in memory support skill creation and
revision, and the interactions guided by those
skills supply new memory for subsequent learn-
ing. Facts retrieved from memory and learned
skills jointly form the agent’s context, while
task outcomes adjust the future retrieval influ-
ence of the records actually served without
rewriting their content. Across ten settings
spanning embodied control, long-document
reading, conversation, mathematics, and code,
MEMCRYSTleads seven reported compar-
isons. On ALFWorld, joint serving achieves
63.17% success, compared with 59.83% for
memory-only and 50.50% for skill-only serv-
ing. Code is available at https://github.
com/tianyi0216/Memcryst.git.
1 Introduction
LLM agents deployed over long periods encounter
tasks whose solutions depend on earlier experience
(Zhao et al., 2023; Yan et al., 2026). An agent may
need to recall an entity’s properties, reuse a success-
ful procedure, or avoid a failure that occurred many
interactions earlier. When the language model re-
mains frozen, this experience can affect decisions
only through the context supplied to it. The inter-
action history grows throughout deployment, while
the context available for any one decision remains
*Corresponding author.
bounded. Lifelong adaptation therefore requires
the agent to extract reusable decision structure from
this history, preserve evidence for the current task,
and adjust retrieval as further outcomes become
available. We study how an agent can learn this ex-
ternal state online so that past experience improves
subsequent decisions.
Previous work has used external memory to store
past interactions, facts, or compressed notes for re-
trieval on later tasks (Xu et al., 2025; Fang et al.,
2026a; Liu et al., 2026). These records provide evi-
dence from earlier experience, but the agent may
still need to work out a procedure each time a sim-
ilar task recurs. Other approaches learn reusable
procedures, or skills, from experience to guide later
tasks (Wang et al., 2024a; Zheng et al., 2025a;
Ni et al., 2026), but these procedures may omit
the task-specific facts and constraints needed to
apply them. Recent systems combine memory
and skills: MUSE-AutoSkill organizes experience
around evolving skills, while MSCE uses stored
evidence and feedback to guide skill development
(Lin et al., 2026; Tang et al., 2026). Maintaining
both, however, does not by itself ensure that the
retrieved facts and skills are useful for the current
task. A fact may be correct but irrelevant, and a
skill may not fit the current situation. Failure can
therefore inform future retrieval without establish-
ing that the retrieved content should be rewritten.
Meanwhile, skill-guided interactions supply new
memory for subsequent skill revision. The chal-
lenge is to learn from this experience while using
task outcomes to adjust which facts and skills enter
later contexts.
We introduce MEMCRYSTto adapt context
through bidirectional memory–skill learning. Even
with frozen model parameters, retrieved context
changes the agent’s actions and thus the experi-
ences available for subsequent learning. MEM-
CRYSTstores experience in memory as episodic
records and typed facts, and consolidates recur-
ring episodes into conditional skills. At deploy-
ment, facts provide task-relevant evidence along-
1
arXiv:2610.32295v1  [cs.AI]  23 Oct 2026

side the procedures supplied by skills. Skill-guided
interactions then enter memory and support later
skill revision, completing the reverse path from
skills to memory through behavior. In parallel,
each task outcome updates the retrieval influence
of the facts and skills actually served. Content con-
struction draws on accumulated experience, while
outcome return adjusts future use without regener-
ating record text. Both processes adapt the agent’s
context while leaving the language model frozen.
Across ten settings spanning embodied control,
long-document reading, conversation, mathemat-
ics, and code, MEMCRYSTleads seven reported
comparisons. On ALFWorld, it reaches 63.17%
success, exceeding memory-only by 3.33 percent-
age points and skill-only serving by 12.67 points.
A separate 2×2 intervention yields an observed
interaction of +5.33 points between fact and skill
return. One shared, domain-scoped state also im-
proves the mean score from 28.30% to 44.50%
over 1,018 queries interleaved across five domains.
Frozen-state controls show higher success with rele-
vant than random records, while skill-based context
uses fewer injected tokens than episodic context.
These results support the following contributions:
• Bidirectional memory–skill learning.We
couple episode-based skill creation and revi-
sion with skill-guided behavior that supplies
new memory for subsequent learning.
• Content and use adaptation.We sepa-
rate evidence-based content updates from
outcome-based updates to the retrieval influ-
ence of served facts and skills, coordinating
both within a bounded context.
• Empirical evidence for the coupled design.
We evaluate the complete system across task
settings and interleaved deployment, and test
joint serving, skill revision, and the interaction
between the two return channels.
2 Related work
Memory construction and retrieval.External
memory preserves experience in forms ranging
from distilled guidance to source-linked evidence.
ExpeL, SAGE, and Dynamic Cheatsheet retain ex-
perience as insights, reflections, or strategies (Zhao
et al., 2023; Liang et al., 2026; Suzgun et al., 2025).
A-Mem organizes linked notes, while TriMem com-
bines source-linked dialogue with atomic facts and
profiles (Xu et al., 2025; Sun et al., 2026). Light-
Mem and SimpleMem compress evidence through
sleep-time and within-session consolidation, re-
spectively (Fang et al., 2026a; Liu et al., 2026).
Repeated textual consolidation can, however, dis-
card useful details (Zhang et al., 2026a). MEM-
CRYSTretains episode evidence for skill learning
alongside independently retrievable typed facts.
Skill construction and revision.V oyager and
SkillWeaver develop executable skills through in-
teraction and refine them through execution feed-
back or testing (Wang et al., 2024a; Zheng et al.,
2025a), while EvoPool evolves executable anno-
tator pools using validation feedback (Xu et al.,
2026a). Agent Workflow Memory abstracts work-
flows from trajectories, while Trace2Skill com-
bines trace-level lessons into portable skill files
(Wang et al., 2024b; Ni et al., 2026). MemP com-
bines trajectories with abstract scripts and supports
revision after failure, and AutoSkill maintains ver-
sioned skills from user interactions (Fang et al.,
2026b; Yang et al., 2026). In MEMCRYST, revi-
sion draws on both new episodes and the supporting
episodes of an existing skill. It preserves the skill’s
identity and accumulated use statistics, while the
revised procedure can be served alongside indepen-
dently retrieved facts.
Context processing and consolidation.For
long-input processing, MemAgent repeatedly up-
dates bounded textual memory, while Multi-Head
Recurrent Memory updates one memory head at a
time (Yu et al., 2025; Li et al., 2026). The Sleep
paradigm consolidates knowledge into model pa-
rameters through distillation and replay (Behrouz
et al., 2026). MEMCRYSTmaintains experience
across deployment events in external stores, using
a frozen model for both task execution and skill
consolidation.
Joint learning and outcome feedback.Memory-
R1 learns memory management and use through
reinforcement learning, whereas Live-Evo adjusts
experience weights from reward differences be-
tween executions with and without memory (Yan
et al., 2026; Zhang et al., 2026b). MUSE-AutoSkill
maintains skill-specific usage notes and revises
skills from execution feedback (Lin et al., 2026).
MSCE uses reflection-weighted terminal values of
traces to guide retrieval and skill evolution, with
skill reliability also governing retrieval (Tang et al.,
2026). EvoChamber extends coevolution to memo-
2

Skill Consolidation
Cluster Synthesize Audit
Episodic Memory
Semantic Facts
Skills Guide New Experience
At sleep boundaries
• Task Evidence
• Diagnosis + lesson
• Entity and Claim
Exposure / Success Counts
• Applicability
• Procedure
• Episode
Ancestry
Utility
Joint Retrieval
Environment
Trajectory + Outcome
Served facts and skills only
Memory Evidence
Outcome Return
Write
Experience
Update
Utility
Verified Feedback
Memory Skill Catalog
Learned Skill
Frozen LLM Actor
Update statistics, preserve text
Figure 1:Bidirectional memory–skill learning through context and behavior.Recurring episodes support skill
creation and revision. Jointly served memory and skills guide the frozen actor, whose completed interactions supply
new memory for later skill consolidation. Task outcomes separately update the retrieval influence of exposed facts
and skills without rewriting their text. Solid arrows show content and behavior flow, and dashed arrows show
statistical updates. Return applies before new records are written.
ries, team collaboration, and population structure
(Zhang et al., 2026c); UCoE co-evolves verifiers
with agent harness state (Xu et al., 2026b), and
EvalResearchBench studies autonomous evaluator
construction (Zhang et al., 2026d). In MEMCRYST,
skill-guided interactions supply episodes for sub-
sequent skill revision. Unlike Live-Evo’s paired
comparison, return uses the observed task outcome
and applies it only to records actually served. It
updates fact exposure and success counts and skill
utilities without rewriting their content. Episode-
based consolidation remains responsible for skill
creation and revision.
3 Method
MEMCRYSTlearns what experience to reuse and
how to use it through the cycle in Figure 1. We first
define adaptation through external context, then
describe how memory supports skills, how skill-
guided behavior supplies new memory, and how
outcomes change later retrieval.
3.1 Problem setup
We consider an agent processing an ordered stream
of deployment eventsq1, . . . , qT . Events either sup-
ply external evidence or require an action or answer.
The agent uses a frozen language model with pol-
icy πθ0 and maintains external state Ξt containing
only information from earlier events. For an event
requiring an action or answer, it constructs context
It =I(q t; Ξt) within the available token budget.
This context defines its effective policy:
πeff t (τ|q) =π θ0(τ|q, I(q; Ξ t)).(1)
The actor produces trajectory τt and receives re-
ward rt ∈[0,1] . After observing the outcome, the
agent may update its external state for subsequent
events. Evidence-ingestion events may also update
the state but are unscored.
The objective is to adapt the external state and
the context it supplies to maximize expected pre-
quential reward E[Spreq]. Let IT index the tran-
sitions scored in evaluation. We consider streams
starting from empty external state:
Spreq = 1 |IT | X t∈IT rt,
θt =θ 0,Ξ 1 =∅.
(2)
Every scored transition counts, including the initial
cold start and later online errors.
3

3.2 Context construction and online updates
To supply both task-specific evidence and reusable
procedures within the context budget, MEMCRYST
maintains episodic memory, typed facts, and skills.
The external state separates stored content from the
statistics controlling its use:
Θt =E t ⊎ Ft ⊎ St,
Ξt = (Θt, ρt). (3)
Memory comprises episodes in Et and typed facts
in Ft. Episodes retain task evidence, outcome di-
agnoses, and lessons for later skill learning. Facts
retain concrete claims about entities, together with
their sources and recurrence support. The skill
catalog St stores applicability conditions and pa-
rameterized procedures, linked to the episodes sup-
porting them. Skills enter context as textual guid-
ance, not executable functions. The actor uses
the task, observations, and retrieved facts to ap-
ply their parameterized steps. The metadata ρt
contains episode weights we, fact exposure and
success counts(n f , hf ), and skill utilitiesU s.
Each adapter chooses which record types to
serve. Retrieval R filters by scope and applicabil-
ity, ranks eligible records by relevance and retrieval
statistics, and formats selected records under the
adapter’s context limits. The retained records bUt
form the contextI t supplied to the frozen actor:
bUt =R ρt(qt,Θ t),
τt ∼π θ0(· |qt, It).
(4)
Exposure is defined by xtv =1[v∈ bUt], so only
records present in the actor’s context count as ex-
posed. Episodes remain available for later skill
learning even when omitted from the actor’s con-
text.
After execution, task evaluation yields ot =
(rt, yt), where rt is the reward and yt ∈ {0,1}is
the evaluator-defined success signal used for state
updates. The external state is then updated in two
stages:
Ξret t =B(Ξ t, ot, bUt),
Ξt+1 =G(Ξ ret t , τt, ot). (5)
The outcome-return operator B updates the re-
trieval statistics of exposed facts and skills with-
out rewriting their content. The content update
operator G combines memory writing after each
event with skill consolidation at scheduled sleep
boundaries. Return precedes new writes, so records
created from the current outcome cannot receive
return from that outcome. Appendices A.3 and A.5
specify the event protocol, eligibility rules, and
context assembly.
3.3 From episodic evidence to reusable skills
Recurring episodes provide evidence for a proce-
dure that can be reused without replaying each
source interaction in the actor’s context. At a sleep
boundary, G begins skill consolidation by mining
related episodes from the episode store after the
current memory write:
(C1, . . . , CM ) = Mine(E wr t , ρwr t ).(6)
The miner ranks recurrent clusters using outcome
quality, size, and cluster stability. It retains failure
evidence as well as successful episodes, allowing a
proposed procedure to address recurring mistakes.
For each cluster, a frozen LM synthesizes a con-
ditional procedure from a small subset of high-
weight episodes. Instance-specific values become
parameter slots, while applicability conditions spec-
ify when the procedure should be used. A separate
audit in a fresh context checks the proposal’s para-
metricity, coverage, and scope against the selected
episodes. Each admitted skill retains links to all
episodes in its source cluster for later revision.
After a proposal passes the initial audit, G
checks whether its complete capability key matches
an existing skill. This key specifies the verb family,
target type, affordance, and output. Unmatched
proposals enter the catalog unless blocked by the
adapter’s duplicate-slug guard. For a match, G
combines the new cluster with the existing skill’s
supporting episodes, synthesizes a revision, and
replaces the skill only after a second audit accepts
it. An accepted revision preserves the skill iden-
tity and accumulated utility while extending its
links to supporting episodes. Later experience can
therefore refine an existing procedure rather than
merely expand the catalog. Appendix A.4 gives the
ordered update, matching fields, and audit details.
3.4 From skill-guided behavior to new
memory
Skills shape the agent’s subsequent interactions,
which supply new evidence for memory and later
skill revision. Together with retrieved facts and
current observations, they condition τt in Eq. 4.
For example, a cleaning skill can guide the agent
to clean an object before placing it at the destina-
tion. The resulting episode preserves evidence of
4

how the procedure was applied, together with an
outcome diagnosis and lessons for later revision.
Appendix D illustrates this path with saved clean-
ing episodes and skill snapshots.
After outcome return, G reflects on the com-
pleted interaction and extracts permitted typed
facts. For a valid episode write,
E wr t =E t ∪ {WE(τt, ot)},
F wr t = Merge(Ft,X F (τt, ot)).(7)
Here WE writes the episode’s evidence, diagnosis,
and lesson, while XF extracts facts and may return
none. Matching facts add recurrence support and
provenance to the existing record for the same en-
tity, scope, and claim, preserving its text and expo-
sure statistics. Unmatched facts create new records.
The new episode is available for subsequent skill
mining, including a sleep pass at the current bound-
ary. Episodes thus support continued skill learning,
while facts remain independently retrievable for
later tasks. Skills influence new memory through
behavior without directly editing fact text.
3.5 Adapting future context through outcomes
A record’s content and its usefulness during deploy-
ment answer different questions. An unsuccessful
task can motivate an adjustment to future retrieval
influence without providing evidence to revise a
factual claim or identify a faulty procedure step.
MEMCRYSTtherefore uses outcome return to up-
date influence separately from content updates:
Ξret t =B(Ξ t, ot, bUt) = (Θt, ρret t ).(8)
The content and membership of Θt remain un-
changed during this stage.
For facts, nf counts exposed tasks and hf counts
successes on those tasks. The fact outcome score
Cf = (h f + 1)/(nf + 2) is a smoothed success
rate over exposed tasks. For each skill, utility Us
summarizes recent outcomes under its persistent
identity. Given update rate αS ∈(0,1] , return
applies
Us ←U s +α Sxts(yt −U s),(9)
nf ←n f +x tf ,
hf ←h f +x tf yt. (10)
Only exposed records change. The step size for Cf
decreases as exposures accumulate, whereas the
constant-step skill update continues to emphasize
recent use. Both scores stay in [0,1] , with deriva-
tions in Appendix A.6. These are success statistics
conditioned on exposure: Cf is not the probability
that a claim is true, and assigning the same outcome
to all served records does not estimate individual
causal contributions.
During later retrieval, Cf and Us weight query
relevance when ranking eligible facts and skills,
respectively. The content update operator carries
these statistics forward when merging facts or revis-
ing skills, while new record identities receive their
own initialization. Consequently, the next context
reflects both new content learned from the interac-
tion and updated influence for previously served
content. Appendix A.2 specifies update ownership
and metadata initialization.
4 Experimental setup
Model.We use frozen Qwen3-8B as our main
backbone (Yang et al., 2025). We also evaluate
Qwen3-1.7B and GPT-4o-mini (OpenAI, 2024)
on ALFWorld to assess performance across back-
bones.
Benchmarks and baselines.We evaluate ten
settings across five domains. ALFWorld covers
embodied control (Shridhar et al., 2021), while
RULER and BABILong cover long-document read-
ing (Hsieh et al., 2024; Kuratov et al., 2024). We
evaluate conversation memory on LoCoMo, Long-
MemEval, and name-substituted DialSim (Maha-
rana et al., 2024; Wu et al., 2025; Kim et al.,
2024). MATH-hard tests mathematical reasoning
(Hendrycks et al., 2021), while MBPP, CodeCon-
tests, and LCB+ cover code generation (Austin
et al., 2021; Li et al., 2022; Jain et al., 2025; Zheng
et al., 2025b). Our main baselines are ReAct with-
out persistent state (Yao et al., 2023), experience-
based ExpeL and MemP (Zhao et al., 2023; Fang
et al., 2026b), and the memory systems Simple-
Mem and LightMem (Liu et al., 2026; Fang et al.,
2026a).
Evaluation.We report prequential mean reward,
scoring each task before its interaction updates the
external state and excluding standalone evidence-
ingestion events. Benchmark metrics include suc-
cess rate, recall, token F1, exact match, and unit-
test reward. All scores are percentages, and abso-
lute differences are in percentage points, denoted
by pp. See Appendix C for detailed settings and
aggregation rules.
5

Panel a: Embodied control and reading long documents
Method ALFWorld RULER BABILong Overall
ReAct51.50 41.30 34.50 42.43
ExpeL44.80 ↓6.70 71.27 ↑29.97 44.50 ↑10.00 53.52 ↑11.09
MemP48.80 ↓2.70 62.55 ↑21.25 43.00 ↑8.50 51.45 ↑9.02
SimpleMem44.30 ↓7.20 35.10 ↓6.20 33.30 ↓1.20 37.57 ↓4.87
LightMem52.30 ↑0.80 12.20 ↓29.10 14.50 ↓20.00 26.33 ↓16.10
MEMCRYST 63.17 ↑11.67 64.70 ↑23.40 59.00 ↑24.50 62.29 ↑19.86
Panel b: Conversation and memory
Method LoCoMo LongMemEval DialSim-subst. Overall
ReAct0.73 4.20 7.54 4.16
ExpeL0.63 ↓0.10 6.85 ↑2.65 11.83 ↑4.29 6.44 ↑2.28
MemP9.64 ↑8.91 5.29 ↑1.09 31.83 ↑24.29 15.59 ↑11.43
SimpleMem26.85 ↑26.12 20.11 ↑15.91 47.85 ↑40.31 31.60 ↑27.45
LightMem0.67 ↓0.06 1.55 ↓2.65 7.54 3.25 ↓0.90
MEMCRYST 31.75 ↑31.02 22.20 ↑18.00 74.24 ↑66.70 42.73 ↑38.57
Panel c: Mathematical reasoning and code generation
Method MATH-hard MBPP CodeContests LCB+ Overall
ReAct57.50 81.30 26.23 35.05 50.02
ExpeL59.16 ↑1.66 82.60 ↑1.30 31.30 ↑5.07 36.04 ↑0.99 52.28 ↑2.26
MemP59.16 ↑1.66 81.70 ↑0.40 28.70 ↑2.47 33.14 ↓1.91 50.68 ↑0.66
SimpleMem58.02 ↑0.52 79.80 ↓1.50 28.00 ↑1.77 36.51 ↑1.46 50.58 ↑0.56
LightMem56.87 ↓0.63 80.70 ↓0.60 27.40 ↑1.17 35.61 ↑0.56 50.15 ↑0.13
MEMCRYST 60.90 ↑3.40 80.42 ↓0.88 28.67 ↑2.44 37.08 ↑2.03 51.77 ↑1.75
Panel d: Overall across categories
Method Overall
ReAct32.20
ExpeL37.41 ↑5.21
MemP39.24 ↑7.04
SimpleMem39.92 ↑7.71
LightMem26.58 ↓5.63
MEMCRYST 52.26 ↑20.06
Table 1:Prequential performance across ten task streams.Scores are percentages, with changes from ReAct in
pp. Overall equally weights benchmarks within panels and the three panel means in panel d.
System RULER BABILong MATH-hard MBPP LoCoMo Overall
ReAct36.90 35.00 61.60 76.00 0.50 28.30
Specialist64.70 ↑27.80 50.00 ↑15.00 60.90 ↓0.70 77.40 ↑1.40 31.80 ↑31.30 48.50 ↑20.20
MEMCRYST 55.90 ↑19.00 52.00 ↑17.00 58.30 ↓3.30 80.00 ↑4.00 25.30 ↑24.80 44.50 ↑16.20
Table 2:Performance on a stream that interleaves five domains.Scores are percentages. Specialist uses separate
domain runs. MEMCRYSTuses one shared external state over 1,088 events. Overall averages 1,018 scored queries.
5 Results
MEMCRYSTleads seven of ten settings.Ta-
ble 1 reports an Overall of 52.26% for MEM-
CRYST, compared with 39.92% for SimpleMem,
the strongest baseline under this aggregate. MEM-
CRYSTleads ALFWorld and BABILong and ranks
second to ExpeL on RULER. In ALFWorld, skills
specify action sequences, while facts supply the
object and environment information needed to ap-
ply them. The joint-serving ablation below tests
this complementarity. The largest gains over ReAct
occur in conversation memory, where MEMCRYST
also exceeds SimpleMem on all three settings.
On name-substituted DialSim, it reaches 74.24%
against SimpleMem’s 47.85%. Here, retrieval sup-
plies names, dates, and events that a general proce-
dure cannot recover from the question alone. The
larger gain after name substitution in Appendix B.7
further supports this role for deployment-specific
evidence. Benefits are smaller in mathematics and
code, where ExpeL leads MBPP and CodeCon-
tests and MEMCRYSTfalls below ReAct on MBPP.
Appendix B.8 shows a modest MBPP gain when
episodes are retained for skill learning but with-
held from the actor, supporting selective context
construction. See Appendices B.4 and B.5 for ad-
6

ALFWorld prequential success rate
Backbone ReAct MEMCRYST∆pp
Qwen3-1.7B13.50 27.67 ↑14.17
Qwen3-8B51.50 63.17 ↑11.67
GPT-4o-mini28.33 40.00 ↑11.67
Table 3:ALFWorld performance across backbones.Rates are percentages. Each task allows at most 30 actions.
Panel a: Memory, skills, and revision
Configuration SR%∆vs. Full
ReAct56.17−7.00
Memory-only59.83−3.33
Skill-only serving50.50−12.67
No skill revision62.00−1.17
Full MEMCRYST 63.17 0.00
Panel b: Outcome-return channels
Skill return
Fact return Off On
Off59.67 57.17
On60.33 63.17
Interaction, pp ↑5.33
Table 4:ALFWorld component ablations over 600 tasks.All configurations use the same revisit guard and
navigation hint. Panel a removes skills, memory retrieval, or skill revision and reports differences from Full in
percentage points. Skill-only serving retains internal memory for skill learning. Panel b switches fact and skill
return while retaining construction and retrieval of memory and skills.
0 100 200 300 400 500 600
Task index
0
50
100
150Cumulative successful deployments
Move
Clean
Cool
Heat
Examine
(a)Persistent skill reuse.
0
5
10Count
Candidates Revisions New skills
0 5 10 15 19
Sleep cycle
0
50
100Task SR (%)
 (b)Skill consolidation.
Figure 2:Evolution and reuse of the learned state.The ALFWorld run with both return channels enabled
processes T= 600 tasks and achieves Spreq = 63.17%. Successful deployments accumulate throughout the stream.
After cycle 2, all accepted updates revise existing skills instead of creating new ones.
ditional baseline comparisons.
A shared state improves overall performance
under interleaving.On the interleaved stream in
Table 2, MEMCRYSTuses one shared, domain-
scoped state to raise mean performance from
28.30% to 44.50% across 1,018 queries in five do-
mains. It retains improvements on both document
slices and about 80% of the isolated LoCoMo gain.
The shared system scores4.00 points below the spe-
cialist mean of 48.50%, while exceeding the sepa-
rate specialists on BABILong and MBPP. These re-
sults show that one evolving state can supply useful
context as deployment alternates between domains.
See Appendix C.2 for the stream composition and
specialist settings.
Gains extend across model sizes and families.
Table 3 shows higher ALFWorld success with all
three frozen backbones. Relative to ReAct, MEM-
CRYSTgains 14.17 percentage points with Qwen3-
1.7B, 11.67 with Qwen3-8B, and 11.67 with GPT-
4o-mini. Each run builds its own external state
from an empty start, adapting the context supplied
to a backbone whose parameters remain frozen.
See Appendix B.1 for additional Qwen3-8B results
across shuffled task orders.
Ablation studies.On the same ALFWorld stream
in Table 4a, joint serving achieves 63.17% suc-
cess, compared with 59.83% for memory-only and
50.50% for skill-only serving. Memory-only re-
tains memory writing, fact retrieval, and fact return
but disables skills. Skill-only serving retains inter-
nal memory for skill learning while withholding
memory from the actor’s context. Each configura-
tion learns from its own trajectories. Allowing skill
revision adds 1.17 points over the 62.00% score
obtained with admitted skill text frozen. The no-
7

All
(n=100)
Clean
(n=24)
Cool
(n=16)
Examine
(n=14)
Heat
(n=19)
Move
(n=27)
0
20
40
60
80
100Success rate (%)
75
72
58
(a) Held-out performance
MemCrystEpisodesRandom
0
500
1000Tokens / task
365
963
369
1,024-token cap
(b) Injected context
MemCrystEpisodesRandom
0
10
20
30
40k tokens / task
25.9
36.6 35.2
(c) Actor input
MemCryst Episode replacement Random selection
Figure 3:Frozen-state context controls on 100 held-out ALFWorld tasks.All conditions use the same learned
state and a 1,024-token injected-context limit. Episode replacement keeps MEMCRYST’s facts and replaces skills
with retrieved episodic records. Random selection matches MEMCRYST’s record types and approximate context
length. Panel a shows overall and task-family success, with task counts below the axis. Panels b and c show mean
injected context and actor input per task, respectively. Actor input includes retries.
revision control still creates and serves skills and
updates their utilities, so this comparison tests the
value of continued procedure revision.
Outcome return further improves joint serving
in Table 4b. Enabling both channels raises success
by 3.50 points over disabling both, with the same
content-construction and retrieval rules. Memory
writing and skill consolidation continue with both
channels off. The gain therefore supports adapting
future use in addition to learning record content.
For a, b∈ {0,1}, let Ba,b enable skill return when
a= 1and fact return whenb= 1. The interaction
between the two return channels is
Jab =E[S preq |B a,b],
γ=J 11 −J 10 −J 01 +J 00. (11)
The observed interaction is +5.33 points: skill re-
turn changes from a −2.50-point effect without
fact return to a +2.83-point effect with it. This de-
pendence supports jointly adapting the retrieval in-
fluence of facts and skills when constructing future
context. See Appendix A.7 for factorial details and
Appendix B.8 for actor-call efficiency and MBPP
context results.
Skill revision continues after catalog growth
stops.Figure 2 records 154 accepted revisions
over the 600-task stream, with all five final skills
present by cycle 2. The skills are served 496 times,
including 338 deployments on successful tasks. For
example, the earlier lamp-examination skill in Fig-
ure 10 accepts lamp visibility or object acquisition
as its trigger. The later version requires both lamp
visibility and possession of the object. This tighter
precondition illustrates how episodes from skill-
guided behavior can refine the procedure supplied
in later contexts under the same skill identity. See
Appendices B.6 and D for lifecycle analyses and
further saved examples.
Relevant selection improves success with a
frozen state.To separate context use from online
learning, we freeze one learned state and compare
three serving conditions on the same 100 held-out
ALFWorld tasks. Figure 3 shows 75% success
for MEMCRYST, versus 58% with approximately
length-matched random records. Random selec-
tion also matches record types, so this contrast
tests which existing facts and skills enter context.
Keeping the facts fixed and replacing skills with
retrieved episodes yields 72%. The skill-based con-
text uses about 62% fewer injected tokens and 29%
fewer actor input tokens than episode replacement.
This second contrast supports representing recur-
ring experience as compact procedures, without
establishing an accuracy advantage over episodic
context. Appendix B.3 explains the protocol.
6 Conclusion
MEMCRYSTadapts a frozen LLM by learning the
evidence and procedures supplied in its bounded
context. Recurring episodes support skill creation
and revision, while skills and retrieved facts guide
behavior that supplies new memory for subsequent
learning. Outcome return separately adjusts which
facts and skills are favored in later retrieval. Across
the evaluated settings, benefits are strongest in con-
versation and mixed in code. ALFWorld ablations
support joint serving and show interaction between
return channels. Frozen-state controls show higher
success with relevant record selection and fewer
injected tokens with skills than with episodic con-
8

text. Together, these results support bidirectional
memory–skill learning as a way to turn accumu-
lated experience into useful context without updat-
ing model parameters.
Limitations
Outcome return assigns the same task outcome to
every served fact and skill, so it does not identify
individual causal contributions or estimate factual
truth. It relies on an observed success signal, and
robustness to erroneous feedback remains untested.
The state and co-serving analyses are descriptive.
The LM-based skill audit screens proposals against
selected episodes but does not guarantee correct-
ness. Our interleaved evaluation uses domain-
scoped retrieval and does not establish transfer of
learned skills to unseen domains.
Ethical Considerations
This study evaluates agents on existing benchmarks
and does not recruit human participants or release
a new foundation model or scraped dataset. Persis-
tent records and provenance can help users inspect
adaptation and diagnose repeated errors, but they
can also retain sensitive or false information. Re-
peated retrieval may amplify biases in either stored
content or outcome feedback. Because the return
mechanism rewards task success, it should not be
interpreted as validating a claim’s accuracy or an
action’s appropriateness.
Deployments with user data should separate
stores by user and domain, restrict access, and pro-
vide retention and deletion controls. Users should
be able to inspect and contest stored information,
with human review before consequential actions.
These deployment safeguards require separate vali-
dation, and our benchmark results do not establish
real-world safety.
References
Jacob Austin, Augustus Odena, Maxwell Nye, Maarten
Bosma, Henryk Michalewski, David Dohan, Ellen
Jiang, Carrie Cai, Michael Terry, Quoc Le, and
Charles Sutton. 2021. Program synthesis with large
language models.arXiv preprint arXiv:2108.07732.
Ali Behrouz, Farnoosh Hashemi, Adel Javanmard, and
Vahab Mirrokni. 2026. Language models need sleep:
Learning to self-modify and consolidate memories.
arXiv preprint arXiv:2606.03979.
Ricardo JGB Campello, Davoud Moulavi, and Jörg
Sander. 2013. Density-based clustering based on
hierarchical density estimates. InPacific-Asia confer-
ence on knowledge discovery and data mining, pages
160–172. Springer.
Jianlyu Chen, Shitao Xiao, Peitian Zhang, Kun
Luo, Defu Lian, and Zheng Liu. 2024. M3-
embedding: Multi-linguality, multi-functionality,
multi-granularity text embeddings through self-
knowledge distillation. InFindings of the Asso-
ciation for Computational Linguistics: ACL 2024,
pages 2318–2335, Bangkok, Thailand. Association
for Computational Linguistics.
Jizhan Fang, Xinle Deng, Haoming Xu, Ziyan Jiang,
Yuqi Tang, Ziwen Xu, Shumin Deng, Yunzhi Yao,
Mengru Wang, Shuofei Qiao, Huajun Chen, and
Ningyu Zhang. 2026a. Lightmem: Lightweight and
efficient memory-augmented generation. InThe
Fourteenth International Conference on Learning
Representations.
Runnan Fang, Yuan Liang, Xiaobin Wang, Jialong Wu,
Shuofei Qiao, Pengjun Xie, Fei Huang, Huajun Chen,
and Ningyu Zhang. 2026b. Memp: Exploring agent
procedural memory. InFindings of the Association
for Computational Linguistics: ACL 2026, pages
17490–17502, San Diego, California, United States.
Association for Computational Linguistics.
Charles R. Harris, K. Jarrod Millman, Stéfan J. van der
Walt, Ralf Gommers, Pauli Virtanen, David Cour-
napeau, Eric Wieser, Julian Taylor, Sebastian Berg,
Nathaniel J. Smith, Robert Kern, Matti Picus,
Stephan Hoyer, Marten H. van Kerkwijk, Matthew
Brett, Allan Haldane, Jaime Fernández del Río, Mark
Wiebe, Pearu Peterson, and 7 others. 2020. Array
programming with NumPy.Nature, 585(7825):357–
362.
Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul
Arora, Steven Basart, Eric Tang, Dawn Song, and Ja-
cob Steinhardt. 2021. Measuring mathematical prob-
lem solving with the MATH dataset.arXiv preprint
arXiv:2103.03874.
Cheng-Ping Hsieh, Simeng Sun, Samuel Kriman, Shan-
tanu Acharya, Dima Rekesh, Fei Jia, Yang Zhang,
and Boris Ginsburg. 2024. Ruler: What’s the real
context size of your long-context language models?
arXiv preprint arXiv:2404.06654.
Naman Jain, King Han, Alex Gu, Wen-Ding Li, Fanjia
Yan, Tianjun Zhang, Sida Wang, Armando Solar-
Lezama, Koushik Sen, and Ion Stoica. 2025. Live-
CodeBench: Holistic and contamination free evalua-
tion of large language models for code. InInterna-
tional Conference on Learning Representations.
Jiho Kim, Woosog Chay, Hyeonji Hwang, Daeun
Kyung, Hyunseung Chung, Eunbyeol Cho, Yeonsu
Kwon, Yohan Jo, and Edward Choi. 2024. Dial-
sim: A dialogue simulator for evaluating long-term
multi-party dialogue understanding of conversational
agents.arXiv preprint arXiv:2406.13144.
9

Yuri Kuratov, Aydar Bulatov, Petr Anokhin, Ivan Rod-
kin, Dmitry Sorokin, Artyom Sorokin, and Mikhail
Burtsev. 2024. BABILong: Testing the limits of
LLMs with long context reasoning-in-a-haystack. In
Advances in Neural Information Processing Systems,
volume 37, pages 106519–106554.
Jiatong Li, Samuel Yeh, and Sharon Li. 2026. Multi-
head recurrent memory agents.arXiv preprint
arXiv:2607.01523.
Yujia Li, David Choi, Junyoung Chung, Nate Kushman,
Julian Schrittwieser, Rémi Leblond, Tom Eccles,
James Keeling, Felix Gimeno, Agustin Dal Lago,
et al. 2022. Competition-level code generation with
AlphaCode.Science, 378(6624):1092–1100.
Xuechen Liang, Yangfan He, Yinghui Xia, Xinyuan
Song, Meiling Tao, Kuan Lu, Jianhui Wang, Li Sun,
Xinhang Yuan, Keqin Li, Jiaqi Chen, TIANYU SHI,
and Yang Jingsong. 2026. Self-evolving agents with
reflective and memory-augmented abilities. InLLM-
based Multi-Agent Systems: Towards Responsible,
Reliable, and Scalable Agentic Systems.
Huawei Lin, Peng Li, Jie Song, Fuxin Jiang, and Tieying
Zhang. 2026. Muse-autoskill: Self-evolving agents
via skill creation, memory, management, and evalua-
tion.Preprint, arXiv:2605.27366.
Jiaqi Liu, Yaofeng Su, Peng Xia, Siwei Han, Zeyu
Zheng, Cihang Xie, Mingyu Ding, and Huaxiu Yao.
2026. SimpleMem: Efficient lifelong memory for
LLM agents.arXiv preprint arXiv:2601.02553.
Adyasha Maharana, Dong-Ho Lee, Sergey Tulyakov,
Mohit Bansal, Francesco Barbieri, and Yuwei Fang.
2024. Evaluating very long-term conversational
memory of LLM agents. InProceedings of the An-
nual Meeting of the Association for Computational
Linguistics.
Jingwei Ni, Yihao Liu, Xinpeng Liu, Yutao Sun,
Mengyu Zhou, Pengyu Cheng, Dexin Wang, Er-
chao Zhao, Xiaoxi Jiang, and Guanjun Jiang.
2026. Trace2skill: Distill trajectory-local lessons
into transferable agent skills.arXiv preprint
arXiv:2603.25158.
OpenAI. 2024. GPT-4o mini: Advancing cost-efficient
intelligence.
Sentence Transformers. 2021. all-MiniLM-L6-v2. Hug-
ging Face model card.
Noah Shinn, Federico Cassano, Ashwin Gopinath,
Karthik Narasimhan, and Shunyu Yao. 2023. Re-
flexion: Language agents with verbal reinforcement
learning. InAdvances in Neural Information Pro-
cessing Systems.
Mohit Shridhar, Xingdi Yuan, Marc-Alexandre Côté,
Yonatan Bisk, Adam Trischler, and Matthew
Hausknecht. 2021. ALFWorld: Aligning text and
embodied environments for interactive learning. In
International Conference on Learning Representa-
tions.
Jingwei Sun, Jianing Zhu, Jiangchao Yao, Tongliang
Liu, and Bo Han. 2026. Rethinking how to remem-
ber: Beyond atomic facts in lifelong llm agent mem-
ory.Preprint, arXiv:2605.19952.
Mirac Suzgun, Mert Yuksekgonul, Federico Bianchi,
Dan Jurafsky, and James Zou. 2025. Dynamic cheat-
sheet: Test-time learning with adaptive memory.
arXiv preprint arXiv:2504.07952.
Bo Tang, Yang Zhang, Guomian Zhuang, Wenqiang
Wei, Gaoyang Zheng, Lindong Xie, Yanchao Tan,
Feiyu Xiong, Qingyu Yang, Edward Chung, and
Zhiyu Li. 2026. From memory to skills: Evidence-
grounded co-evolution governance for long-horizon
LLM agents.arXiv preprint arXiv:2607.16621.
Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Man-
dlekar, Chaowei Xiao, Yuke Zhu, Linxi Fan, and An-
ima Anandkumar. 2024a. V oyager: An open-ended
embodied agent with large language models.Trans-
actions on Machine Learning Research.
Zora Zhiruo Wang, Jiayuan Mao, Daniel Fried, and
Graham Neubig. 2024b. Agent workflow memory.
arXiv preprint arXiv:2409.07429.
Di Wu, Hongwei Wang, Wenhao Yu, Yuwei Zhang, Kai-
Wei Chang, and Dong Yu. 2025. LongMemEval:
Benchmarking chat assistants on long-term interac-
tive memory. InInternational Conference on Learn-
ing Representations.
Tianyi Xu, Yaolun Zhang, Xuan Ouyang, and Huazheng
Wang. 2026a. EvoPool: Evolutionary programmatic
annotation for label-efficient specialized supervision.
Preprint, arXiv:2606.01617.
Tianyi Xu, Yaolun Zhang, Yiran Wu, Joe Nguyen,
Shengyu Dai, Saba Moeinizade, Zhenwen Shao,
Qingyun Wu, and Huazheng Wang. 2026b.
Verifier-harness co-evolution for training-free
self-improvement on open-ended tasks.Preprint,
arXiv:2610.17609.
Wujiang Xu, Zujie Liang, Kai Mei, Hang Gao, Juntao
Tan, and Yongfeng Zhang. 2025. A-mem: Agentic
memory for LLM agents. InThe Thirty-ninth An-
nual Conference on Neural Information Processing
Systems.
Sikuan Yan, Xiufeng Yang, Zuchao Huang, Ercong
Nie, Zifeng Ding, Zonggen Li, Xiaowen Ma, Jinhe
Bi, Kristian Kersting, Jeff Z. Pan, Hinrich Schuetze,
V olker Tresp, and Yunpu Ma. 2026. Memory-r1:
Enhancing large language model agents to manage
and utilize memories via reinforcement learning. In
Proceedings of the 64th Annual Meeting of the As-
sociation for Computational Linguistics (Volume 1:
Long Papers), pages 12805–12825, San Diego, Cali-
fornia, United States. Association for Computational
Linguistics.
An Yang, Anfeng Li, Baosong Yang, Beichen Zhang,
Binyuan Hui, Bo Zheng, Bowen Yu, Chang Gao,
Chengen Huang, Chenxu Lv, et al. 2025. Qwen3
technical report.arXiv preprint arXiv:2505.09388.
10

Yutao Yang, Junsong Li, Qianjun Pan, Bihao Zhan, Yux-
uan Cai, Lin Du, Jie Zhou, Kai Chen, Qin Chen,
Xin Li, Bo Zhang, and Liang He. 2026. Autoskill:
Experience-driven lifelong learning via skill self-
evolution.arXiv preprint arXiv:2603.01145.
Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak
Shafran, Karthik R Narasimhan, and Yuan Cao. 2023.
React: Synergizing reasoning and acting in language
models. InThe Eleventh International Conference
on Learning Representations.
Hongli Yu, Tinghong Chen, Jiangtao Feng, Jiangjie
Chen, Weinan Dai, Qiying Yu, Ya-Qin Zhang, Wei-
Ying Ma, Jingjing Liu, Mingxuan Wang, and Hao
Zhou. 2025. Memagent: Reshaping long-context
llm with multi-conv rl-based memory agent.arXiv
preprint arXiv:2507.02259.
Dylan Zhang, Yanshan Lin, Zhengkun Wu, Yihang Sun,
Bingxuan Li, Dianqi Li, and Hao Peng. 2026a. Use-
ful memories become faulty when continuously up-
dated by LLMs.arXiv preprint arXiv:2605.12978.
Yaolun Zhang, Yiran Wu, Yijiong Yu, Qingyun Wu, and
Huazheng Wang. 2026b. Live-evo: Online evolu-
tion of agentic memory from continuous feedback.
Preprint, arXiv:2602.02369.
Yaolun Zhang, Tianyi Xu, Shengyu Dai, Zhenwen Shao,
Qingyun Wu, and Huazheng Wang. 2026c. Evocham-
ber: Test-time co-evolution of multi-agent system at
individual, team, and population scales.Preprint,
arXiv:2605.11136.
Yaolun Zhang, Tianyi Xu, Yujie Zhao, Jishen Zhao,
Qingyun Wu, and Huazheng Wang. 2026d. EvalRe-
searchBench: Can AI agents build their own feed-
back for recursive self-improvement?Preprint,
arXiv:2610.04184.
Andrew Zhao, Daniel Huang, Quentin Xu, Matthieu
Lin, Yong-Jin Liu, and Gao Huang. 2023. ExpeL:
LLM agents are experiential learners.arXiv preprint
arXiv:2308.10144.
Boyuan Zheng, Michael Y . Fatemi, Xiaolong Jin,
Zora Zhiruo Wang, Apurva Gandhi, Yueqi Song,
Yu Gu, Jayanth Srinivasa, Gaowen Liu, Graham Neu-
big, and Yu Su. 2025a. Skillweaver: Web agents
can self-improve by discovering and honing skills.
Preprint, arXiv:2504.07079.
Zihan Zheng, Zerui Cheng, Zeyu Shen, Shang Zhou,
Kaiyuan Liu, Hansen He, Dongruixuan Li, Stanley
Wei, Hangyi Hao, Jianzhu Yao, Peiyao Sheng, Zix-
uan Wang, Wenhao Chai, Aleksandra Korolova, Pe-
ter Henderson, Sanjeev Arora, Pramod Viswanath,
Jingbo Shang, and Saining Xie. 2025b. Live-
codebench pro: How do olympiad medalists judge
llms in competitive programming?Preprint,
arXiv:2506.11928.
11

A Formal and algorithmic details
This appendix specifies the records and updates
that turn stored experience into context for later
decisions. It follows the online loop from retrieval
through outcome return and memory writing to
skill consolidation, then derives the properties of
the outcome statistics used in retrieval.
A.1 Notation
A.2 Record schemas and update ownership
The episode and fact stores hold episodic and se-
mantic memory, respectively, while the skill cata-
log holds reusable procedures. The record fields
that govern behavior are
e=⟨q e, δe, ℓe, εe, ae⟩,
f=⟨ent f , φf , zf , cf , Pf , εf ⟩,
s=⟨name s,desc s, χs, ψs,
As, εs⟩.
(12)
For an episode, qe is task evidence, δe is the out-
come diagnosis, and ℓe is the reusable lesson. The
lifecycle field ae ∈ {active,archived}controls or-
dinary wake retrieval. For a fact, entf , φf , and
zf are its entity, claim, and type. The field cf
records recurrence support and Pf records prove-
nance from source events. For a skill, χs contains
its applicability conditions and capability key, ψs
is its procedure, and As contains the IDs of its ac-
cepted supporting episodes. Each record carries
a domain or stream scope stamp εv. The stored
records also include identifiers, timestamps, and
cached embeddings, which do not appear as evi-
dence in the policy input. The runner saves diag-
nostic skill usage counts, fact base rate accumu-
lators, and links between facts and skills served
together. These diagnostic fields lie outside Ξt for
the transition defined here. Of the statistics updated
by outcome return, retrieval R uses only the fact
countsn f andh f and the skill utilityU s.
The metadata inρ t is keyed by record identity:
ρt =

{we}e∈Et,{n f , hf }f∈F t,
{Us}s∈St

,
Cf = hf + 1 nf + 2.
(13)
The fact counts determine the outcome score Cf .
Retrieval R reads the state without changing it.
Outcome return B changes (nf , hf ) and Us for ex-
posed records while leaving payloads, store mem-
bership, and episode weights fixed. Memory writ-
ing and skill consolidation belong to the content
update operator G. This operator may add or merge
payloads, change support and provenance, admit or
revise skills, and archive the source episodes of ac-
cepted proposals. It carries the metadata produced
by B into the next state so that retained records
keep their use history.
The empty state condition in Eq. 2 expands to
E1 =F 1 =S 1 =∅ and ρ1 =∅ . An episode from
an input event starts withwe = 1, while a transition
episode uses Eq. 14. A new fact starts with cf = 1,
Pf ={t} , and nf =h f = 0, giving Cf =.5 . A
new skill stores the IDs of every episode in its pro-
posal’s full source cluster in As and initializes Us
as specified in Section A.4. An accepted revision
preserves the skill identifier and its accumulated
utility, combines the old and new ancestry, and
replaces only the audited skill content.
A.3 Full online algorithm and causal
chronology
Learning changes subsequent contexts rather than
the context that produced the current outcome. To
make this chronology explicit, define
H− t =σ(q t,{q i, τi, oi, υi}i<t)
as the information available just before event t is
processed. The variable υi contains the randomness
used for extraction, clustering, synthesis, and audit
at event i. For input events, τi =o i =∅ . Both
Ξt and bUt are measurable with respect to H− t . The
adapter sets ιt = 0 for input events, so IT ={t:
mt = transition, ιt = 1}. We write Gwrite for the
memory writing stage of G, which runs after each
event and before any scheduled skill consolidation.
Algorithm 1 applies outcome return before mem-
ory writing and consolidates skills at scheduled
sleep boundaries. The runner appends the episode,
applies return to previously served facts, writes new
facts, and then applies return to previously served
skills. This order produces the same state as B fol-
lowed by Gwrite: outcome return does not update
episodes, fact return precedes new fact insertion,
and skill return does not change memory content.
Skill consolidation follows all four substeps at a
sleep boundary. Because the action context is fixed
before ot arrives, these updates influence only later
decisions.
Memory writing preserves the interaction for
later retrieval and skill learning. For transition
events, the main configuration extracts facts only
when yt = 1, though declared adapters may also
12

Symbol Meaning Symbol Meaning
t, Tevent index and stream horizonq t, mt, ιt,I T event, mode, scoring flag, and scored set
πθ0 , τt frozen policy and produced trajectoryo t = (rt, yt)reward and evaluator-defined success
Et,F t,S t episode store, fact store, and skill catalog Θt disjoint union of the three content stores
ρt mutable retrieval and outcome statisticsΞ t behaviorally active external state
As supporting episode IDse, f, sone episode, fact, and skill record
δ, ℓ, φ, z,
χ, ψ, ε diagnosis, lesson, claim, type, applicabil-
ity, procedure, and scope
Pf , ae fact provenance and episode lifecycle
state
R, G, B retrieval, content update, and outcome
return operators
gS, gF skill and fact return switches
bUt, xtv served records and exposure indicatorI t, KX , Lt actor context and channel/token budgets
cf , nf , hf , Cf fact support, exposures, successes, and
outcome score
Us, αS skill utility and return step size
we episode retrieval weightϕ, ηembedding and merge threshold
Ccand t , AC candidate clusters and audit scoreS preq, Sterm prequential and terminal metrics
Jab, γfactorial cell mean and interactionL,H − t sleep boundaries and information avail-
able before a decision
Table 5: Notation used throughout the paper. The indexX∈ {E, F, S}identifies one of the three stores.
retain facts from failed trajectories. For a valid
episode returned by WE, the memory write in Eq. 7
is
et =W E(τt, ot),
E wr t =E t ∪ {et},
wet = 1 +.3(2y t −1),
(14)
Zt =X F (τt, ot),
F wr t = Merge.86(Ft, Zt). (15)
If the episode call or parse fails, the episode store
remains E wr t =E t, but fact extraction and merg-
ing still follow Eq. 15. The stores E wr t and F wr t
therefore describe the state after writing and before
sleep. The corresponding metadata ρwr t extends
ρret t to include the newly written records. It as-
signs the weight above to each successfully written
episode and initializes new facts with zero expo-
sures and successes.
Fact merging increases recurrence support with-
out treating recurrence as an exposed success.
Write Zt = ( ef1, . . . ,ef|Zt|) in extraction order and
set a working store F ← Ft. Mergeη processes
extracted facts sequentially, allowing later facts
from the same event to match records inserted or
updated earlier in that event. For any fact f, let
ent(f) and φ(f) denote its entity and claim. For
each extracted fact ef, it scans the working store
in stable order and takes the first record with the
same entity and scope whose similarity meets the
threshold:
f ⋆ = first  f∈ F:
ent(f) = ent( ef),
εf =ε ef ,
cos

ϕ(ent(f) :φ(f)),
ϕ(ent( ef) :φ( ef))  ≥η 	 .
(16)
Whenf ⋆ exists,Merge η applies
(cf ⋆, Pf ⋆)←(c f ⋆ + 1, Pf ⋆ ∪ {t}).(17)
Otherwise, it appends ef to F with c ef = 1, n ef =
h ef = 0 , and provenance P ef ={t} . After all
extracted facts have been processed,F wr t =F.
A.4 Skill mining, synthesis, and admission
Skill consolidation turns recurring episodes into
reusable procedures at scheduled sleep bound-
aries. Because it follows the current mem-
ory write, its evidence may include the newly
completed episode. Before each sleep pass,
the miner reactivates archived episodes and in-
cludes them in the pool. It clusters their em-
beddings and reads the weights we stored in Ξwr t
to score the candidate groups. HDBSCAN uses
Euclidean distance, min_cluster_size= 3 ,
min_samples= 1, and excess of mass selection
(Campello et al., 2013). Let NonNoise drop the
HDBSCAN noise group. For each non-noise group
H, FamilySplit3(H) returns {H} when H con-
tains one family or when no family has three mem-
bers. Otherwise, it returns each family subgroup
with at least three members and drops the rest. Each
13

Algorithm 1:Full MEMCRYSTonline loop
1: Input:an ordered stream q1:T , a declared adapter, a frozen policy πθ0, return switches gS and gF , and sleep boundaries
L. The stream must contain at least one scored transition.
2:Initialize:E 1 =F 1 =S 1 =∅,ρ 1 =∅, score sumR sum ←0, and scored countN←0.
3:fort= 1, . . . , Tdo
4: Parse modem t, scoring flagι t, scopeε t, and payload from the adapter.
5:ifm t = inputthen
6: Require ιt = 0. Obtain Ξwr t from Ξt by appending the declared episode with we = 1 and sequentially merging the
declared facts. Carry metadata for retained identities, initialize new facts withn f =h f = 0, and do not callπ θ0
orB.
7:elseprocess a transition event
8: Retrieve and format bUt into It under the adapter’s context limits. Count as exposed only records represented in It.
9: Sampleτ t ∼π θ0 (· |qt, It)and observeo t = (rt, yt). Ifι t = 1, setR sum ←R sum +r t andN←N+ 1.
10:Ξ ret t ←B gS ,gF (Ξt, ot, bUt). Update only served facts and skills without changing record text or membership.
11:Ξ wr t ←G write(Ξret t , τt, ot). Append the episode if writing succeeds and merge valid permitted facts. New records
receive no return fromo t.
12:end if
13:ift∈ Lthen
14: Reactivate archived episodes, compute ranked candidate clusters C1, . . . , CM from the resulting pool at sleep time
using Eqs. 18 and 19, and set the working catalogS ← St.
15:forj= 1, . . . , Mdo
16: Synthesize skill proposales Cj from up to five episodes inC j with the highest weights. Audit the proposal in a
fresh context and setu←0.
17:ifthe first audit acceptsthensets ⋆ ←Match(esCj ,S).
18:ifs ⋆ =∅thenconsult the declared duplicate-slug guard. If it permits insertion, set
S ← S ∪ {Insert(esCj , Cj)}. Set u←1 whether insertion occurs or the duplicate-slug guard intercepts it.
19: elseretrieve the episodes indexed by As⋆, pool those records with Cj, synthesize a revision sCj , and audit
it in a fresh context. If accepted, replaces ⋆ byReplace(s ⋆, sCj , Cj)and setu←1.
20:end if
21:end if
22:ifu= 1thenarchive the episodes in the current clusterC j from ordinary wake retrieval.
23:end for
24: SetΞ t+1 to the state after writing with the updated working catalog and lifecycle flags.
25:elsesetΞ t+1 ←Ξ wr t .
26:end if
27:end for
28: SetS preq ←R sum/Nandreturn(Ξ T+1 , Spreq). ForS term, holdΞ T+1 fixed, run retrieval, the policy, and the task
evaluator, and do not callB,G, or sleep updates.
returned subgroup inherits the HDBSCAN persis-
tence of its parent H. The Mine operator in Eq. 6
uses
Q(C) = 1 |C| X e∈C clip(we/1.5,0,1),
Rt = NonNoise

HDBSCAN(ϕ(E wr t ))  ,
Rqual t ={H∈ Rt :Q(H)≥.4},
Dt =
[
H∈R qual t
FamilySplit3(H),
Ccand t = Topd 10
{C∈ Dt :|C| ≥3, Q(C)≥.4}

.
(18)
Let p(C) be the HDBSCAN persistence of a cluster.
The ranking used byTop d 10 in Eq. 18 is
d(C) =Q(C)|C|max{.05, p(C)}.(19)
At most ten ranked candidate clusters are processed
per sleep boundary. Under the main episode ini-
tialization, even a failure episode has we/1.5> .4,
so this quality threshold does not exclude failure-
only clusters. The quality score instead helps rank
candidate clusters and sets the initial utility of an
admitted skill.
A separate frozen-LM call synthesizes a struc-
tured skill proposal from up to five members of C
with the largest we. The parser requires a name
and description, and it rejects a proposal whose
procedure contains no parameter slot. The stored
ancestry As contains the IDs of all episodes in the
accepted proposal’s source cluster, including those
omitted from the synthesis prompt. The audit calls
the same frozen LM in a fresh context containing
the complete skill proposal, cluster statistics, and
the selected episodes. Its prompt requests one ver-
dict for each of the 13 checks in Table 6, and the
admission rule counts the returned PASS verdicts.
Let bmC be the number of valid dictionary objects
in the returned checks, with aCk = 1 exactly when
the parser reads PASS for returned object k. The
14

implemented score is
AC =
bmCX
k=1
aCk .(20)
The parser skips entries that are not objects and
rejects unparseable JSON. Unrecognized verdicts
count as failures, and a skill proposal passes the
first screen exactly when AC ≥10 . Candidate
clusters are processed in the fixed ranking or-
der. A matching capability still requires revision
synthesis and a second audit before the catalog
changes. For a new capability, the implementa-
tion initializes AesC ={id(e) :e∈C} and
UesC = clip(Q(C), .4, .95). The audit does not
treat affordances fixed by the domain as instance
literals.
Catalog updates accumulate evidence for a capa-
bility across sleep passes. Set the working catalog
S ← St and process the ranked clusters in order,
so each cluster sees earlier accepted updates from
the same pass. For candidate cluster C, synthesis
produces skill proposal esC. After the first audit
accepts it, matching searches the working catalog:
esC = Synth(C),
s⋆ C = Match(esC,S)
∈ S ∪ {∅}.
(21)
The complete capability key is (verb family,
target type,affordance,output) . Matching returns
∅ when the catalog has no skill with that complete
key. For a match, G pools C with the episodes
indexed by the incumbent’s ancestry, selects up to
five records with the highest weights, and synthe-
sizes revision sC for a second audit. The catalog
transition is
S ←



S ∪ {Insert(esC, C)},
accepted new skill,
S \ {s⋆ C}  ∪
{Replace(s⋆ C, sC, C)},
accepted revision,
S,
otherwise.
(22)
Insertion creates a fresh identity whose ancestry
contains every episode in C. Replacement regen-
erates the incumbent’s text and capability fields
while preserving its identifier, creation time, and
utility after outcome return. It also combines the
old and new ancestry, so evidence for an existing
capability supports revision under the same skill
identity. An accepted insertion or revision archives
the current cluster from ordinary wake retrieval.
Some adapters also apply a duplicate-slug guard
that archives the cluster even when it intercepts an
insertion and leaves the catalog unchanged. These
episodes remain stored for provenance and are re-
activated at the next sleep boundary.
After the ordered pass, St+1 is the working
catalog and Et+1 includes the resulting lifecycle
flags. Skill consolidation leaves the fact store at
Ft+1 =F wr t . The completed state is
Θt+1 =E t+1 ⊎ Ft+1 ⊎ St+1,
Ξt+1 = (Θt+1, ρt+1). (23)
For retained records, ρt+1 carries forward ρwr t , in-
cluding the updated(n f , hf )for merged facts and
Us for revised skills. New skill identities receive
their cluster-based initial utility. Away from a sleep
boundary, the catalog remains St and Ξt+1 = Ξwr t .
A.5 Exact retrieval scores and exposure
Retrieval determines which parts of the evolving
state can affect the next decision. The retriever first
checks scope and applicability, then ranks eligible
records by relevance and retrieval influence. An
episode is eligible for ordinary wake retrieval only
when it is active and scope compatible. Archived
episodes remain stored for provenance and later
mining. A fact must satisfy the adapter’s scope,
type, and minimum support filters. For skills, it
extracts the four-field capability key defined in Sec-
tion A.4 and first searches for an exact match. If
none exists, the main capability route relaxes the
affordance requirement and then both the verb and
affordance requirements. This route does not fall
back to global cosine retrieval. All routing choices
and thresholds are fixed before a stream begins, and
KX = 0disables channelX.
Let O be the channel order declared by
the adapter and let ε(qt) be the query scope.
EligibleX (qt,Θ t) denotes the records from chan-
nel X that pass the preceding constraints.
TopKKX returns the KX records with the high-
15

Check Passing condition
1 Instance literals No names, identifiers, or varying numeric values from a single episode are baked into the
procedure.
2 Borrowed framing The skill is a reusable procedure rather than a paraphrase of one episode.
3 Runtime probes Relevant preconditions are checked when the action space supplies a probe, or are stated
explicitly otherwise.
4 Parametricity Values that vary across uses appear as parameter slots.
5 Necessary setup The procedure contains no setup step that cannot contribute to the task.
6 Workflow integrity No declared tool call or required stage is silently bypassed.
7 Traceability Correctness claims are grounded in observable state.
8 Stable shape The procedure does not assume incompatible concrete shapes across uses.
9 Cluster coverage The procedure applies to a majority of the source cluster.
10 Failure coverage It addresses at least half of the nonempty recorded failures or improvements, or passes
vacuously when none exist.
11 Scope control It does not claim task shapes unsupported by the cluster.
12 Model invariance It abstracts style tied to one model family when multiple model families appear and
passes when only one family appears.
13 Capability consistency Verb, target, affordance, and output fields are complete and agree with the procedure.
Table 6:Skill audit checks.Each skill proposal is evaluated in a fresh context.
est scores. The serving rule is
Vt = ConcatX∈O TopKKX

EligibleX (qt,Θ t),
RX (·, qt)

,
bUt = PackLt,ε(qt)(Vt),
It = Fmtε(qt)( bUt).
(24)
Here Pack denotes context assembly under the
adapter’s limits, using the same rendering rule as
It. The online actor path uses retrieval quotas and
field-length limits, while the frozen-state controls
enforce an explicit token budgetL t.
In the retrieval scores below, qe, δe, and ℓe de-
note an episode’s task evidence, outcome diagnosis,
and lesson. For a fact f, ent(f) and φ(f) denote
its entity and claim. The fields names and descs
form the skill retrieval text. The operator ⊕ de-
notes text concatenation. The channel scores used
in Eq. 24 are
RS(s, q) = max(.05, Us)
cos(ϕ(q), ϕ(names ⊕descs)), (25)
Cf = hf + 1 nf + 2,
RF (f, q) = cos

ϕ(q),
ϕ(ent(f) :φ(f))

(1 +.05 min(cf ,6)) (.5 +C f ),
(26)
RE(e, q) =we cos

ϕ(q),
ϕ(qe ⊕δe ⊕ℓe)

. (27)
These equations reproduce the implemented signed
cosine products. Their multiplicative influence fac-
tors increase a score when its cosine relevance is
nonnegative. When cosine relevance is negative,
increasing the factor makes the signed score more
negative. Before exact or relaxed lookup, the skill
router maps the verb, target, affordance, and output
to their predefined canonical values. The fact fil-
ter checks type, support, and the optional domain
stamp. For dialogue, define
blex(v, q) =.12 min

|Tok(q)∩Tok(v)|,4

using lowercased whitespace tokens. The episode’s
dense retrieval text is vden e =q e ⊕δ e ⊕ℓ e. The
lexical retrieval texts concatenate fields with spaces:
vlex f = ent(f)⊕φ(f) and vlex e =q e ⊕ℓ e. The
dialogue retriever adds this lexical anchor to the
dense score:
Rdlg F (f, q) =RF (f, q)
+b lex(vlex f , q),
Rdlg E (e, q) =we  cos(ϕ(q), ϕ(vden e ))
+b lex(vlex e , q)  .
(28)
The lexical bonus helps retrieve names and dates
alongside dense semantic matches. The context
formatter renders an episode as (qe, δe, ℓe). Facts
contribute their entity, claim, and support, while
skills contribute their name, description, applicabil-
ity, and procedure. MEMCRYST’s actor formatter
limits skill applicability text to 300 characters and
procedure text to 600 characters before assembly,
so the actor may receive only a prefix of a stored
procedure. The metadata Cf and Us affect ranking
16

but are not presented as textual evidence. Con-
text assembly preserves the adapter’s channel order
in Vt. Thus bUt contains exactly the records rep-
resented in It, while any omitted candidate has
xtv = 0and receives no return.
A.6 Outcome return properties
The fact and skill statistics differ in how they
weight past exposures. To derive their behavior
and bounds, we first write the return updates for an
existing record with both binary switches explicit:
U ret s =U s +g SαSxts(yt −U s),
nret f =n f +g F xtf ,
hret f =h f +g F xtf yt,
(29)
where(g S, gF )∈ {0,1}2.
The reported implementation uses αS =.2 . Let
ys,1, . . . , ys,m be the outcomes from the firstm≥1
tasks that expose skills. For gS = 1 and 0< αS <
1, unrolling Eq. 9 gives
U (m) s = (1−α S)mU (0) s
+α S
mX
i=1
(1−α S)m−iys,i. (30)
For 0< αS <1 , the displayed coefficients are non-
negative and sum to one, so U (m) s ∈[0,1] when-
ever U (0) s , ys,i ∈[0,1] . The endpoint αS = 1 fol-
lows directly from applying the recurrence once.
When gS = 0, B leaves the utility of every existing
skill unchanged. The constant step size gives more
weight to recent exposures while retaining part of
the cluster-based initialization. Because revisions
preserve identity and utility, this history remains
associated with the skill as its text changes.
For gF = 1, an exchangeable Bernoulli working
model treats outcomes on tasks that expose fact
f as conditionally independent with a common
success probability pf . A Beta(1,1) prior on pf
smoothsh f successes fromn f exposures:
pf |h f , nf ∼Beta(h f + 1, nf −h f + 1),
E[pf |h f , nf ] = hf + 1 nf + 2 =C f .
(31)
Under this working model, Cf estimates smoothed
success conditional on exposure, not factual truth.
The interpretation explains the smoothing rule, al-
though adaptive retrieval and changing skills can
alter the exposed-task distribution during deploy-
ment. When xtf = 1, one more exposed outcome
yt gives the recursion
Cret f −C f = yt −C f nf + 3 .(32)
When gF = 0, both counts and the derived score
remain unchanged. The fact’s step size decreases
with accumulated exposures, whereas the skill’s
fixed step size continues to emphasize recent use.
Equations 30 and 32 bound both scores in [0,1]
without requiring the Bernoulli working model. Be-
cause all exposed records share the task outcome,
neither statistic identifies an individual record’s
causal contribution. Retrieval uses these summaries
to adjust which stored facts and procedures enter
later contexts.
A.7 Interpretation of the outcome-return
factorial
The four cell means in Eq. 11 determine the satu-
rated expansion
Jab =µ+αa+βb+γab,
µ=J 00,
α=J 10 −J 00,
β=J 01 −J 00,
γ=J 11 −J 10 −J 01 +J 00.
(33)
Under additivity, γ= 0 . The observed success
counts give the interaction in percentage points:
100bγ= 100379−343−362 + 358 600
≈5.33pp.
(34)
Relative to both channels enabled, disabling fact
return lowers success by6.00 points, disabling skill
return by2.83, and disabling both by3.50.
The interaction measures how the effect of skill
return changes when fact return is enabled, or
equivalently how the effect of fact return changes
when skill return is enabled. All four cells use
the same content update algorithm G and retrieval
rules, differing only in the return switches. Because
each run develops its own trajectories and state, the
contrast includes the interventions’ downstream ef-
fects on context and learning. The joint-serving
ablation separately tests the value of supplying
memory and skills together.
B Additional results and analyses
These analyses examine how deployment condi-
tions affect performance, how learned records are
reused, and how much actor effort they require.
17

ALFWorld navigation adaptation.On the same
600-task ALFWorld stream with frozen Qwen3-
8B and a 30-action limit, MEMCRYSTachieves
63.17% success with the revisit guard and 57.00%
without it. The navigation hint and all other settings
remain fixed. Appendix C.2 describes the guard’s
task-local navigation rule.
B.1 ALFWorld performance across shuffled
task orders
Performance across orders.Across the four shuf-
fled task orders in Table 7, MEMCRYSTachieves
success rates from 57.50% to 63.83%, with a mean
of 61.08% and a sample standard deviation of 2.96
percentage points. One run exceeds the original
fixed-order score of 63.17%, one matches it, and
two score lower. The lowest shuffled-order score re-
mains above the fixed-order references of 52.70%
for Reflexion in Table 9 and 56.17% for guarded
ReAct.
Settings.We reconstruct the original 600-game
pool from ALFWorld’s train ordering and apply
four global permutations with NumPy (Harris et al.,
2020) RandomState seeds 101, 202, 303, and
404. Each run starts with an empty episode store,
fact store, and skill catalog and scores every task
before writeback. Skill consolidation follows each
block of 30 tasks for 20 cycles. The Full configu-
ration uses frozen Qwen3-8B, at most 30 actions
per task, and retrieval of up to four facts and two
skills. Both outcome-return channels, skill creation
and revision, the revisit guard, and the navigation
hint remain enabled. Episodic records support skill
learning but do not enter the actor’s context in this
configuration. The recorded game files match each
prescribed permutation exactly, with 600 distinct
games and no missing tasks or environment ex-
ceptions. The four shuffled runs share one code
snapshot and configuration. We report the original
fixed-order result separately.
Variation across runs.Variation is largest for ex-
amine, with a standard deviation of 11.4 points
compared with 1.4–4.7 points for the other fami-
lies. Clean success exceeds the fixed-order result
in every shuffled run, while move remains compar-
atively stable. The run-level Student- t 95% con-
fidence interval for the mean is [56.37,65.80]% ,
based on four runs and three degrees of freedom.
B.2 Terminal evaluation
Protocol.Prequential evaluation measures perfor-
mance during learning, while terminal evaluation
measures performance with the accumulated state
after learning stops. For every benchmark in this
evaluation, we freeze the final state and score tasks
held out from the learning stream:
Sterm =E q∼Qheldout [r(q,Ξ T+1 )].(35)
Table 8 reports held-out performance with the fi-
nal state alongside the prequential results from Ta-
ble 1. The terminal scores are higher on ALFWorld,
RULER, and MBPP, but lower on BABILong and
LoCoMo.
B.3 Frozen-state context controls
Serving conditions.We evaluate three context
conditions on the same 100 held-out ALFWorld
games using frozen Qwen3-8B and one learned
external state. The state content and retrieval statis-
tics remain fixed throughout evaluation, with no
memory writes, outcome return, or skill consolida-
tion. All conditions retain the revisit guard, nav-
igation hint, and 30-action limit. All conditions
have a 1,024-token injected-context limit, mea-
sured with the backbone tokenizer and including
block headings. MEMCRYSTretrieves facts and
skills, whereas episode replacement keeps the same
facts and fills the remaining budget with retrieved
episodes, including archived records. The replace-
ment serves an average of 10.8 episodes per task.
Random selection samples facts and skills from the
same state while matching record types and approx-
imate context length. Its length is within 10% of
MEMCRYSTon every task, with a mean absolute
relative deviation of 2.6%. All 300 evaluations are
valid, the game files match across conditions, and
no injected context is truncated.
Paired outcomes and actor cost.Compared with
episode replacement, MEMCRYSTalone solves 12
tasks and the replacement alone solves nine. The
corresponding counts against random selection are
24 and seven. Two-sided exact McNemar tests
give p=.664 and p=.0033 , respectively. The
episode comparison does not establish accuracy
equivalence. Although all conditions share the
same limit, their mean injected contexts differ: 365
tokens for MEMCRYST, 963 for episode replace-
ment, and 369 for random selection. Mean actor
input, including retries, is 25.9k, 36.6k, and 35.2k
tokens per task in the same order. These costs
cover serving the frozen state but not constructing
it. This experiment is separate from both the online
prequential scores and the terminal evaluation in
Table 8.
18

Order Successes SR% Clean Cool Examine Heat Move
Seed 101 359/60059.83 60.2 54.3 66.1 62.2 59.6
Seed 202 383/60063.83 62.2 60.9 86.4 62.2 61.0
Seed 303 379/60063.17 61.2 62.0 83.1 62.2 60.3
Seed 404 345/60057.50 57.1 56.5 64.4 52.7 57.8
Mean61.08 60.2 58.4 75.0 59.8 59.7
Sample SD2.96 2.2 3.6 11.4 4.7 1.4
Original fixed order 379/60063.17 53.1 62.0 81.4 63.5 63.2
Table 7:ALFWorld performance across four shuffled-order runs.Scores are percentages, and standard
deviations are in percentage points computed over the four new runs only. Each run contains 98 clean, 92 cool, 59
examine, 74 heat, and 277 move tasks.
Benchmark Metric Terminal score Prequential score∆
ALFWorld Success rate70.00 63.17 ↑6.83
RULER Recall65.70 64.70 ↑1.00
BABILong Mean reward57.00 59.00 ↓2.00
LoCoMo Token F123.70 31.75 ↓8.05
MBPP Unit test reward81.59 80.42 ↑1.17
Table 8:Terminal and prequential performance of MEMCRYST.Scores are percentages, and ∆ = 100(Sterm −
Spreq)is in percentage points.
B.4 Additional baselines and dialogue
diagnostics
Additional ALFWorld systems.Table 9 extends
the comparison to six systems adapted to the ALF-
World interface: Reflexion and SAGE (Shinn et al.,
2023; Liang et al., 2026), Live-Evo and Dynamic
Cheatsheet (Zhang et al., 2026b; Suzgun et al.,
2025), and A-Mem and AWM (Xu et al., 2025;
Wang et al., 2024b). The retrieval-only control
retains memory writing and fact retrieval but dis-
ables skills and fact return. It therefore differs from
the memory-only configuration in Table 4, which
keeps fact return enabled.
Collection and serving.ExpeL scores 44.8%
when its serving path injects the collected insights.
A collection-only run scores 52.8%, but never
presents those insights to the policy and therefore
does not implement lifelong ExpeL. For Reflexion,
we report the first attempt under the matched ac-
tion budget, rather than success across any of three
attempts.
Reader and dialogue settings.The document-
reading results compare complete context-
construction systems under an 8,192-token
answer-context budget. Each item supplies a
document and question together. The external
readers rebuild their stores from each document,
whereas MEMCRYSTretains one persistent
external state across the fixed sequence.
On the common DialSim prefix, SimpleMem an-
swers 457 of 955 scored questions correctly, giving
the 47.85% entry in Table 1. This metric excludes
the 200 session ingestion operations.
B.5 Comparison with MSCE
Comparison settings.We compare MEMCRYST
with MSCE, which also learns memory and skills
from experience (Tang et al., 2026), on ALFWorld
and name-substituted DialSim. All systems use
frozen Qwen3-8B, and persistent runs start from
empty state. Table 10 reports the highest-scoring
MSCE configuration tested on DialSim. MEM-
CRYSTachieves higher success on both bench-
marks.
ALFWorld: learning reusable procedures.
MEMCRYSTachieves 63.17% success, compared
with 49.33% for MSCE and 56.17% for ReAct un-
der the same navigation settings. MSCE retrieves
experience on 503 of 600 tasks but produces more
invalid actions and reaches the action limit more
often than either reference system. Its skill candi-
dates include procedures tied to particular objects
and destinations, which may offer little guidance
when either changes. MEMCRYSTinstead learns
parameterized procedures from recurring episodes
and retrieves task-specific facts separately, so the
same procedure can apply to different objects and
destinations.
DialSim: retrieving relevant facts.MEMCRYST
19

Method SR%∆vs. ReAct
ReAct51.5n/a
Reflexion52.7 ↑1.2
SAGE49.5 ↓2.0
Live-Evo49.0 ↓2.5
Dynamic Cheatsheet47.8 ↓3.7
A-Mem43.2 ↓8.3
AWM41.5 ↓10.0
Retrieval only60.67 ↑9.17
Table 9:Additional ALFWorld success rates under the benchmark interface.
Panel a: ALFWorld, with the revisit guard and navigation hint enabled
System Successes /NSR% 30 actions reached Invalid actions
ReAct 337/60056.17268 905
MSCE 296/60049.33308 1,082
MEMCRYST379/60063.17226 661
Panel b: Name-substituted DialSim
System Successes /NSR% Timed Untimed Unanswerable
ReAct 72/9557.54 0.0 3.448.8
MSCE 157/95716.41 3.2 32.9 33.9
MEMCRYST709/95574.24 97.0 44.448.0
Table 10:Comparison with MSCE on ALFWorld and DialSim.Scores are percentages. The “30 actions reached”
count includes tasks solved on the final allowed action. Panel b uses the highest-scoring tested MSCE configuration,
with 957 questions and 535 timed questions. ReAct and MEMCRYSTanswer 955 questions, including 533 timed
questions. All three runs include 295 untimed and 127 unanswerable questions.
reaches 74.24% success, compared with 16.41%
for MSCE and 7.54% for ReAct. The largest gap
is on timed questions, where accuracy is 97.0% for
MEMCRYSTand 3.2% for MSCE. In the selected
MSCE run, only 347 of 995 recorded retrieval re-
sults contain source conversation passages, and
the actor repeats the same incorrect answer on 153
questions. MSCE selects experience by its assessed
value, but these observations suggest that a useful
past interaction may still lack the names or dates
required by a new question. MEMCRYSTretrieves
typed facts with explicit name and date anchors to
provide these details in the answer context.
B.6 State dynamics and skill lifecycle
Recorded deployments and joint exposure.The
state audit follows skill deployments and the facts
served alongside them in the 600-task ALFWorld
run with both return channels enabled. The task
ledger records deployments and outcomes, while
the terminal co-serving relation identifies facts and
skills that have entered the context together. Let
Co(f) denote the deduplicated list of skill identi-
ties serialized beside terminal fact f. Restricted to
the five final persistent skill identities, the terminal
relation is
Gco T =  (f, s)∈ FT+1 × ST+1 :
id(s)∈Co(f)

. (36)
Of the 367 terminal facts, 223 have degree at least
one, forming 453 distinct edges to the five final
skill identities. An edge indicates at least one joint
exposure, possibly to an earlier version of the skill,
but does not record its count, timestamp, or out-
come. These diagnostic links describe joint context
rather than synthesis provenance and do not affect
retrieval.
Continued reuse and revision.The final catalog
contains one skill for each ALFWorld task family,
with 496 deployments and 338 successes across the
stream. Figure 4a shows how deployments and suc-
cess rates differ across these skills, while Figure 4c
groups their co-served facts by type. The consol-
idation history records 159 accepted operations,
of which five create skills and 154 revise existing
skills. Thus the catalog continues to change after it
covers all task families, as also shown in Figure 2.
One skill’s lifecycle.The place-object skill is ad-
mitted near task 30 and remains active through-
out the stream. Its deployment history, changes in
20

0 50 100 150 200 250 300
Deployments
Move
Clean
Cool
Heat
Examine
155 201 · 77.1%
51 93 · 54.8%
54 88 · 61.4%
44 69 · 63.8%
34 45 · 75.6%
Successful Failed
(a)Final task family coverage.
0 100 200 300 400 500 600
Task index
0
50
100
150Cumulative successful deployments
Move
Clean
Cool
Heat
Examine (b)Cumulative skill reuse.
Move Clean Cool Heat Examine
Skill family
0
20
40
60
80
100Distinct fact–skill links
94
54
41 42
8
82
51
34
26 21
Affordance Location
(c)Fact–skill co-serving links.
0
5
10Count
Candidates Revisions New skills
0 5 10 15 19
Sleep cycle
0
50
100Task SR (%)
 (d)Skill consolidation and selection.
Figure 4:ALFWorld state dynamics with both return channels enabled.Panel a reports deployments, successes,
and success rates by family. Panels b and c show cumulative successful deployments and terminal co-serving links
by fact type. Panel d shows candidates as a dashed line, accepted new skills and revisions as stacked bars, and task
success in each cycle.
name and scope, and final episode ancestry show
reuse under a persistent identity as the procedure
evolves. The snapshot comparison in Figure 10
gives concrete examples of these textual changes.
B.7 Prospective intervention on
name-substituted DialSim
Intervention and findings.The advantage of
persistent state grows when the original character
names are removed from DialSim. We consistently
renamed every character while preserving the dia-
logue structure and answers. Before running the in-
tervention, we specified that persistent state should
improve the name-substituted condition by at least
8 percentage points and that this gain should exceed
the gain with the original names. We also expected
ReAct to perform better with the original names.
All three criteria were met. MEMCRYST’s gain
over ReAct increased from 47.0 points with the
original names to 66.7 points after renaming, while
ReAct fell from 26.9% to 7.54%. The result sup-
ports the value of retrieving deployment-specific
evidence when cues associated with familiar names
are unavailable.
B.8 Actor-call efficiency and an MBPP
context case study
Measurement.We measure actor effort from the
completed runs. For ALFWorld, logical actor calls
include action steps and logged invalid-action re-
tries on scored wake tasks, excluding held-out eval-
uation. For MBPP, the saved trajectories report ac-
tor steps but not a complete call counter. Both mea-
sures describe actor effort rather than total LLM
cost because they exclude memory writes, synthe-
sis, audit, and transport retries. The retrieval quotas
below are configured limits, not measured token
counts.
21

Named
states
Admission · t = 30
place-object-at-destination
4 intermediate names
t = 330–390
Terminal · t = 599
place-object
0
50
100
150
200
Cumulative
deployments
201
155
All deployments
Successful deployments
0 100 200 300 400 500 600
Task index
0
25
50
75
100
Terminal ancestry
(by episode time)
97176 co-serving fact links at stream end (untimed)
Figure 5:Lifecycle of the most frequently deployed final skill.From top to bottom, the traces show admission and
recorded name changes, all 201 deployments with 155 successes, and the 97 episodes in the final synthesis ancestry.
The 176 distinct terminal fact co-serving links have no timestamps and may involve earlier skill texts. Same-name
revisions overwrite prior versions, so the records do not recover every revision or ancestry size over time.
ALFWorld improves both completion and actor-
call efficiency.MEMCRYSTraises success from
51.50% to 63.17% while using 15.22% fewer actor
calls than ReAct. Figure 6 compares six configu-
rations over 600 tasks using the original ReAct
baseline. The full system uses 11,636 calls, com-
prising 10,975 action steps and 661 invalid-action
retries. ReAct uses 13,725 calls, comprising 12,851
steps and 874 retries. Fact return alone uses slightly
fewer calls at 11,612 but solves 362 tasks rather
than 379. In these runs, enabling both returns there-
fore yields 17 more completions for 24 additional
calls.
Shared successful tasks.On the 250 tasks solved
by both systems, mean actor calls fall from 12.90
to 10.13, a 21.49% reduction. MEMCRYSTuses
fewer calls on 146 of these tasks, the same number
on 41, and more on 63. The reduction in overall
actor effort is therefore also present among tasks
that both systems solve.
MBPP context case study.Retaining episodes for
learning does not require serving them on every
task. Figure 7 compares two configurations on the
same 252 MBPP tasks, differing only in whether
past episodes enter the actor’s context. Both con-
figurations learn online from their own trajectories
and retrieve up to four facts and two skills. They
use the same code execution and self-test interface,
deduplicate skills, and require fact support of at
least two.
Reward and actor steps.Removing episodic con-
text raises mean reward from 80.42% to 81.22%, a
gain of 0.79 percentage points computed before
rounding. Actor steps fall from 363 to 343, a
5.51% reduction. This comparison supports keep-
ing episodes available for learning while selecting
more narrowly what enters the immediate action
context.
22

19 20 21 22 23
Actor calls per task (including retries)
50
55
60
65Prequential success (%)
ReAct
51.50%
Retrieval only
Neither return
Skill return only
Fact return only
MemCryst  63.17%
(a)Cost vs. performance.
0 10 20 30 40
ReAct: actor calls
0
10
20
30
40MemCryst: actor calls
Fewer: 146 Equal: 41 More: 63
Tasks
1
5
10 (b)Paired calls on shared successes.
Figure 6:ALFWorld actor-call efficiency.All methods use Qwen3-8B and 600 tasks. ReAct uses its original
unguarded setting, while the other configurations retain the revisit guard. Calls include action retries but exclude
memory maintenance. Panel b shows the 250 shared successes, with marker size indicating task count.
0 50 100 150 200 250
Scored MBPP tasks
75
80
85
90
95
100Cumulative mean unit-test reward (%)
80.42%
81.22%
With episodic context
Without episodic context
(a)Higher reward.
0 50 100 150 200 250
Scored MBPP tasks
0
100
200
300
400Cumulative actor steps
363
343
With episodic context
Without episodic context (b)Fewer actor steps.
Figure 7:MBPP with and without episodic context.Curves show cumulative mean reward and actor steps over
the same 252 tasks with Qwen3-8B and retrieval limits of four facts and two skills.
C Experimental details
C.1 Default framework settings
Shared settings.Table 11 specifies the common
rules for memory writing, skill learning, and out-
come return. Each benchmark adapter sets the
state lifetime, retrieval depth, encoder, sleep sched-
ule, and task budget for its interface. The default
text encoder is all-MiniLM-L6-v2 (Sentence
Transformers, 2021).
C.2 Benchmark evaluation configuration
Comparison settings.Within each benchmark
comparison, all methods share the evaluator, an-
swer or action interface, and backbone. State life-
time and serving behavior follow the evaluated sys-
tem. We use frozen Qwen3-8B for the ten-setting
comparison, the interleaved stream, and the mech-
anism studies, including MEMCRYST’s memory
and skill updates. Table 13 gives the number of
items scored for MEMCRYST, with additional base-
lines in Appendix B.4 and the MSCE comparison
in Appendix B.5.
ALFWorld comparisons.The headline compar-
ison pairs unguarded ReAct with guarded MEM-
CRYSTand therefore compares deployed systems.
The component and return ablations instead share
the same 600 tasks, task order, and guard. The no-
revision configuration freezes admitted skill text
but retains skill creation, serving, and utility up-
dates.
Reader and dataset variants.For RULER and
BABILong, ReAct reads only the document tail,
while the external readers rebuild their stores for
each document as described in Section B.4. MEM-
CRYSTretains one persistent external state across
each fixed document sequence, so these compar-
isons evaluate complete reader systems rather than
isolate memory lifetime. LongMemEval uses a re-
23

Block Hyperparameter Default
LLM Primary backbone Frozen Qwen3-8B Role temperatures actor0, writer.2, synthesizer.3, and auditor0
State Initial external state empty episode store, fact store, and skill catalog
Memory
Episode weight 1.3after success and.7after failure
Prior for a new fact nf =h f = 0, henceC f =.5
Fact merge same entity and scope with cosine thresholdη=.86
Retrieval
Default text encoder all-MiniLM-L6-v2
Skill utility floor max{.05, Us}
Fact score constants support coefficient.05, support cap6, outcome-score offset.5
Return Skill update rate EMA rateα S =.2 Eligible records facts and skills served in the current action context
Skill
consolidation
Clusterer HDBSCAN, Euclidean distance, EOM selection
HDBSCAN settings minimum cluster size3, minimum samples1, and selectionϵ= 0
Cluster gate |C| ≥3andQ(C)≥.4
Cluster order Q(C)|C|max{.05, p(C)}
Limits per pass at most10candidate clusters and up to5representative episodes
Skill catalog
Audit gate at least10returned passes, with13checks requested
Initial skill utility Us = clip(Q(C), .4, .95)
Capability match revise an exact match in place and insert a new skill otherwise
Table 11:Default MEMCRYSTframework settings.
duced haystack, and DialSim-subst. denotes the
name-substituted version of DialSim. LCB+ com-
bines LiveCodeBench with a LiveCodeBench Pro
extension (Jain et al., 2025; Zheng et al., 2025b).
Interleaved stream.The 1,088-event stream in
Table 2 includes 70 unscored LoCoMo session in-
gestions, followed or interleaved with 120 RULER,
100 BABILong, 151 MATH-hard, 150 MBPP, and
497 LoCoMo queries. The frozen backbone uses
one evolving external state throughout, with do-
main stamps restricting evidence and capability
routing selecting skills. Task adapters provide the
action interfaces. The specialist reference uses sep-
arate domain runs, with BABILong and MBPP
scores from contemporaneous runs that preceded
the later sweeps in Table 1.
Online protocol.Persistent runs start from empty
state and score each item before writing its com-
pleted interaction. Standalone ingestion events con-
tribute evidence but are unscored. Each run follows
a fixed task order, with some baseline runs ending
at different fixed prefixes. Unless stated otherwise,
each result comes from one run. Appendix A.3
specifies the event chronology, and Appendix B.2
reports supplementary evaluations with the final
state frozen. The native reward rt enters Spreq,
whereas the binary signal yt updates the influence
of exposed records through Eqs. 9 and 10. Table 12
specifies the scoring metric and return signal for
each benchmark.
Some baseline runs score more items than the
MEMCRYSTcounts in Table 13. The main Di-
alSim comparison in Table 1 uses the common
955-question prefix, whereas Table 10 reports the
MSCE run over 957 questions with its original de-
nominator.
Score aggregation.Benchmark scores are percent-
ages, and absolute differences are in percentage
points. In Table 1, Overall equally weights bench-
marks within panels and the three panel means in
panel d. Trailing zeros standardize table format-
ting without increasing the precision of recorded
summaries. We compute averages and differences
before final display rounding and report Overall
only when all required scores are available.
Adapter settings.For ALFWorld, MEMCRYST
uses a navigation hint and a task-local revisit guard.
If the agent holds no object and attempts to revisit a
location, the guard substitutes the first valid naviga-
tion action to an unvisited location, when available.
This adaptation changes within-task action execu-
tion while leaving the memory and skill update
rules unchanged. The LoCoMo adapter uses BGE-
M3 (Chen et al., 2024), retrieves 12 facts, and may
serve verbatim excerpts within an answer budget
of four steps. The code adapter retains episodic
records and retrieves two deduplicated skills and
four facts with support of at least two. It uses the
same execution and self-test interface as ReAct.
24

Benchmark State scope Evaluation mode Native rewardr t Return signaly t
Embodied control and reading long documents
ALFWorld persistent legal text actions with a limit of 30 steps binary successr t
RULER persistent for
MEMCRYST
one document and one question per item with
an answer context of 8,192 tokens
mean recall reward 1[rt ≥.99]
BABILong persistent for
MEMCRYST
one document and one question per item with
an answer context of 8,192 tokens
mean reward1[r t ≥.99]
Conversation and memory
LoCoMo per dialogue session ingestion followed by short answers token F11[F1≥.5]
LongMemEval per instance reduced haystack ingestion followed by a short
answer
token F11[F1≥.5]
DialSim-subst. persistent session ingestion followed by short answers binary successr t
Mathematical reasoning and code generation
MATH-hard persistent unconstrained reasoning and answer exact answer re-
ward
1[rt ≥.99]
MBPP persistent generate code, execute it, and test it unit test reward1[r t ≥.99]
CodeContests persistent generate code, execute it, and test it unit test reward1[r t ≥.99]
LCB+ persistent generate code, execute it, and test it unit test reward1[r t ≥.99]
Table 12:Benchmark evaluation settings.Persistent streams begin empty and score each item before writeback.
Benchmark DomainNMetric
ALFWorld Embodied control 600 Success rate
RULER Long document reading 400 Recall
BABILong Long document reading 200 Mean reward
LoCoMo Conversation memory 1,977 Token F1
LongMemEval Conversation memory 60 Token F1
DialSim-subst. Conversation memory 955 Success rate
MATH-hard Mathematics 261 Exact match
MBPP Code generation 252 Unit test reward
CodeContests Code generation 160 Unit test reward
LCB+ Code generation 232 Unit test reward
Table 13:Benchmarks, sample counts, and metrics.Ncounts the items scored for MEMCRYST.
C.3 Generated state and parser contracts
Memory writes.The episode writer turns a com-
pleted trajectory and its outcome into one JSON
record containing task evidence, diagnosis, and a
reusable lesson. If the call or parse fails, the writer
skips the episode. The fact extractor produces
typed entity and claim records, while dialogue
adapters parse one entity | fact record per
line. The parser drops malformed items and adds
no facts from an unparseable response. A com-
pleted task can therefore update the influence of
previously served records even if writing new con-
tent fails.
Skill writes.The synthesizer receives candidate-
cluster statistics and up to five episodes with the
highest weights. It returns a SKILL.md record
with the required frontmatter and a parameterized
procedure, which the parser rejects if it is mal-
formed or nonparametric. The auditor then reads
the complete skill proposal, cluster statistics, and
the same episodes in a fresh context without the
synthesis transcript. The prompt requests the 13
checks in Table 6, and admission requires at least
10 returned PASS verdicts. The parser also rejects
unparseable audit JSON. A rejected proposal does
not enter the skill catalog, but the sleep pass con-
tinues with the remaining candidates.
C.4 Compute resources
Inference resources.We served Qwen3-8B and
Qwen3-1.7B locally on NVIDIA L40 GPUs. For
the Qwen3 experiments, local inference supported
task execution as well as memory writing, skill syn-
thesis, and auditing. The GPT-4o-mini experiments
used the OpenAI API with API-key authentication.
25

D Qualitative examples of joint memory and skill evolution
These examples show how stored experience becomes procedural guidance and context for task execution.
Section D.1 presents memory records and skill snapshots from the 600-task ALFWorld run with both
return channels enabled. The saved improvement fields contain the memory writer’s lessons, whereas
Section D.4 presents the actual inputs and outputs of four task executions. Source wording and any
truncation in the logged context are preserved, with line wrapping for readability. The cards display skill
utilities and derived outcome scores as percentages. Repeated prompt blocks appear once, followed by
each call’s changing input, complete response, and environment return. Task indices start at zero.
The cleaning and heating records link experience with different objects to persistent skills. Later skill
snapshots give more direct placement guidance and require both lamp visibility and possession of the
target object. The cooling example combines object-location facts with a procedure, while the dialogue
example preserves the evidence needed to answer a purchase question. All four task executions include
retrieved memory in the actor’s input, and ALFWorld, MATH-hard, and MBPP also include skills. These
selected examples show the supplied evidence and recorded behavior without isolating the contribution of
individual records.
D.1 Original memory records and skill snapshots
Successful cleaning: original memory
Task 31 / episode 5b2000b6
QUESTION
clean a <target> and place it in a
<destination>
IMPROVEMENT
go to countertop 2, take mug 1 from
countertop 2, go to sinkbasin 1, clean
mug 1 with sinkbasin 1, go to
coffeemachine 1, move mug 1 to
coffeemachine 1
SUCCESStrueSTEPS15
SERVED SKILLe654d0ba
Cleaning skill: terminal procedure
Persistent skill e654d0ba
ORIGINAL PROCEDURE EXCERPT
Clean Before Placing: Do not place <target_object>
at<destination>until you have runclean
<target_object> with sink. Apply this when
holding the correct object, before any placement.
ANCESTRY EXCERPT5b2000b6
Figure 8:A cleaning lesson and a terminal skill excerpt.The episode belongs to the skill’s terminal ancestry.
Bread: original stored lesson
Task 2 / episode 2501fa18
QUESTION
heat a <target> and place it in a
<destination>
IMPROVEMENT
go to countertop 1, take bread 1 from
countertop 1, go to microwave 1, heat
bread 1 with microwave 1, go to
countertop 1, move bread 1 to
countertop 1
SUCCESStrueSTEPS22
SERVED SKILLS[]
TERMINAL SKILL ANCESTRY3b5e1faf
Cup: original stored lesson
Task 38 / episode 51c73cdf
IMPROVEMENT
go to cabinet 5, open cabinet 5, take
cup 2 from cabinet 5, go to microwave
1, open microwave 1, heat cup 2 with
microwave 1, go to sidetable 1, move
cup 2 to sidetable 1
SUCCESStrueSTEPS14
SERVED SKILL3b5e1faf
FACTS FROM TASK 38
cup: often stored in cabinets
sidetable: often used to place
objects after heating
Figure 9:Heating lessons for different objects and destinations.Both episodes belong to the heating skill’s
terminal ancestry.
26

Object placement Same persistent skill d94f43bc
Earlier saved skill
WHEN TO NA VIGATE
Apply this when the target object is in hand andthe
destination is in view.
HOW TO DELIVER
Once at<destination>, put<target_object>
in/on<destination>.
WHAT TO A VOID
Failing to search systematically for the target object.
40 supporting episodes / 33 successes in 49 deployments
UtilityU= 81.57%
Terminal saved skill
WHEN TO NA VIGATE
Apply thisafter confirmingthe correct object is in hand.
HOW TO DELIVER
Once at<destination>, put<target_object>
in/on<destination>with no detours.
WHAT TO A VOID
Assuming the object is at the expected locationwithout
searching
97 supporting episodes / 155 successes in 201 deployments
UtilityU= 68.66%
Examination with a lamp Same persistent skill b6188de6
Earlier saved skill
WHEN TO USE THE LAMP
Apply this as soon as the desklamp is in vieworright after
acquiring<target_object>.
8 supporting episodes / 2 successes in 7 deployments
Terminal saved skill
WHEN TO USE THE LAMP
Apply this when the desklamp is in viewand the target
object is in inventory.
23 supporting episodes / 34 successes in 45 deployments
Figure 10:Procedure revisions under persistent skill identities.The nonconsecutive snapshots retain the saved
wording, with emphasis added.
Cleaning skill: saved terminal statistics
Skill e654d0ba /clean-and-place
USE_COUNT93
FAILURE_COUNT42
ANCESTRY ENTRIES55
UTILITY AS A PERCENTAGE
U= 66.81%
Sink fact: saved terminal record
Fact ade31094
ENTITYsinkbasin
FACT“can be used to clean objects”
SUPPORT18USED24HELPED18
DERIVED OUTCOME SCORE
C= 18 + 1 24 + 2 ≈73.1%.
Figure 11:Terminal use statistics for a skill and a fact.The fact score is computed from the saved used and
helpedcounts.
Vase fact: one successful exposure
Original terminal fact 22d3a8ce
ENTITYvase
FACT“can be picked up and examined”
FROM_EPISODES[81]
USED1HELPED1
SUPPORTS_SKILLS[d94f43bc]
DERIVED OUTCOME SCOREC= 66.7%
Figure 12:A fact record after one successful exposure. from_episodes identifies the source task and
supports_skillslists co-served skills.
27

D.2 Served context on a successful held-out task
Goal: “cool some bread and put it in countertop”
Held-out task 40 / success in 9 actions / 376 context tokens
SERVED SKILL EXCERPT
Skill 1: cool-and-place
“Prep Cooling Appliance: Go to the fridge and open it so it
is ready. Apply this as soon as the fridge is in view or right
after acquiring<target_object>.”
SERVED FACT EXCERPTS
“bread: can be cooled using a fridge (4×)”
“bread: often located on a countertop (9×); often located on
a diningtable (2×)”
Figure 13:Served context from the frozen-state evaluation in Appendix B.3.Excerpts show the cooling skill and
bread facts from a 376-token context. This record contains the input and outcome counters, but no action transcript.
D.3 Conversation memory and answer outcomes
Successful recall and completion-linked memory
Task 13 / name-substituted DialSim
ORIGINAL CONVERSATION
September 23, 1994 / source task 10
Elena: How’d you pay for them?
Diana: Uh, credit card.
Elena: And who pays for that?
Diana: Um... my... father.
SOURCE EPISODE76845064
TERMINAL FACT7bb0e489
ENTITYdad’s credit card
FACT
“Diana used Dad’s credit card to buy the swanky new
boots”
FROM_EPISODES EXCERPT
[13, 14, 21, 35, 40, ...]
ORIGINAL QUESTION
“So, you remember eavesdropping on that chat back on Septem-
ber 23, 1994, could you be any more secretive about how Diana
snagged those swanky new boots?”
OPTIONS
She found money outside Central Perk / She got a job / Dad’s
credit card / Elena lent her some money because she felt bad
for her / I don’t know. (None of the above)
“Answer with the exact option text.”
REFERENCE ANSWERDad’s credit card
SUCCESStrueSTEPS1
Figure 14:Conversation evidence and a completion-linked fact.The answer shown is the dataset reference. This
task record preserves the outcome but not the actor’s context or response.
28

D.4 Task execution trajectories across four benchmarks
D.4.1 ALFWorld
6 actor calls / 1 skill / 4 facts
Retrieved record inventory
skills: 1
b6188de6: examine-with-desklamp
facts: 4
9c5b3e4e: desklamp | often located on a sidetable
c2432ef9: desklamp | can be used to examine objects
810edf1e: bowl | can be found on a desk or sidetable
e6e9e249: desklamp | can be turned on to provide light
reference episodes: 0
System message for all six calls
You are an autonomous agent solving an ALFWorld household task.
# Action policy
When a skill block is provided, follow its Procedure step by step. Identify which
step of the procedure you are currently executing and pick the action that advances
that step.
# Action priority (apply in order)
1. **If the target object is visible in the current observation AND you are not
holding it yet, your next action MUST be ‘take <target_object> from
<receptacle>‘.**
Do NOT navigate to another location once you have seen the target. Acting beats
exploring.
2. If you are already holding the target object and the next procedure step is a
manipulation primitive (‘cool <obj> with fridge‘, ‘heat <obj> with microwave‘,
‘clean <obj> with sink‘, ‘use <lamp>‘), execute it directly.
3. **Process exactly once. ** After you have run ‘cool‘ / ‘heat‘ / ‘clean‘ / ‘use‘
on the target ONE time, do NOT run another manipulation primitive on it. The
next action is either ‘go to <destination>‘ or ‘put <object> in/on
<destination>‘.
4. **Destination vs appliance. ** In a task like ‘put a cool tomato in microwave‘,
‘microwave‘ is the DESTINATION, not the appliance. The cooling appliance is
‘fridge‘. After cooling, your action at the microwave MUST be
‘put <target> in/on microwave‘, NOT ‘heat <target> with microwave‘. The same
rule applies for sink, fridge, and lamp when they appear as destinations.
5. If you are holding the target object and at the destination, execute
‘put <object> in/on <destination>‘.
6. Only emit ‘go to <X>‘ when you are not yet at the location required by the
next procedure step. Pick ‘take‘ or ‘put‘ over ‘go to‘ whenever both are valid.
7. The target object in the task is the noun that follows "a/some/the". For
example in "put a cool tomato in microwave" the target is ‘tomato‘. The
appliance words (microwave, fridge, sink, lamp) are NOT the target.
# Output
Output exactly one action from the valid actions list. Be efficient.
Shared user prefix A: task and complete retrieved context
# Task
look at bowl under the desklamp
# Retrieved context (skill+afford+loc)
## Procedure to follow (HOW -- the step order; fill in WHERE from below + the room)
Skill 1: examine-with-desklamp
description: Use a desklamp to examine a target object.
capability: verb=examine affordance=desklamp output=object_examined
when_to_use: - Examine an object with a desklamp
- Locate and use a desklamp to inspect a target item
procedure:
- Systematic Object Hunt: Sweep unvisited surfaces and open closed containers
until <target_object> is found; never revisit empty spots. Apply this right after
parsing the goal, before holding anything.
- Confirm Object Match: After picking something up, verify it is
<target_object>; if not, put it back and resume searching. Apply this whenever you
acquire an object but the goal object is still unmet.
29

- Locate Light Source: Find and go to a desklamp; if it is not visible,
systematically check unvisited receptacles. Apply this when the target object is
identified but the desklamp is not in view
## Constraints -- rules about how things work (RESPECT THESE)
These are reliable facts about how appliances/containers behave. Violating them
causes failure.
- desklamp: can be used to examine objects (20×); can be turned on to provide
light (12×)
## Where to look -- location priors (HINTS, verify against the room)
Where these object types are usually found. Use to decide where to search first,
then trust what THIS room actually shows over the prior.
- desklamp: often located on a sidetable (7×)
- bowl: can be found on a desk or sidetable (2×)
Shared user suffix C: action rules and response format
# Rule
You can only take / put / clean / heat / cool / use an object at a receptacle you
are CURRENTLY at. If the action you want is not in the Valid actions list above,
you are not there yet -- ‘go to <receptacle>‘ first, then act.
# Your response format
Thought: <one sentence about the next subgoal>
Action: <exactly one action copied verbatim from the valid actions list>
User message for calli: A + B i + C.
Call 1
B1: complete call-specific user input
# Locations you have NOT yet checked (try these for the target)
bed 1, desk 2, desk 1, drawer 6, drawer 5, drawer 4, drawer 3, drawer 2, drawer 1,
garbagecan 1, laundryhamper 1, safe 1, shelf 6, shelf 5, shelf 4, shelf 3, shelf 2,
shelf 1
# Current observation
-= Welcome to TextWorld, ALFRED! =-
You are in the middle of a room. Looking quickly around you, you see a bed 1, a
desk 2, a desk 1, a drawer 6, a drawer 5, a drawer 4, a drawer 3, a drawer 2, a
drawer 1, a garbagecan 1, a laundryhamper 1, a safe 1, a shelf 6, a shelf 5, a shelf
4, a shelf 3, a shelf 2, and a shelf 1.
Your task is to: look at bowl under the desklamp.
# Valid actions
- go to bed 1
- go to desk 1
- go to desk 2
- go to drawer 1
- go to drawer 2
- go to drawer 3
- go to drawer 4
- go to drawer 5
- go to drawer 6
- go to garbagecan 1
- go to laundryhamper 1
- go to safe 1
- go to shelf 1
- go to shelf 2
- go to shelf 3
- go to shelf 4
- go to shelf 5
- go to shelf 6
- help
- inventory
- look
Call 1: complete actor response
Thought: I need to locate the desklamp first to examine the bowl.
Action: go to desk 1
30

Call 1: environment return
observation:
You arrive at desk 1. On the desk 1, you see a desklamp 1, a keychain 3, a mug 2, a
pen 2, a pen 1, and a pencil 2.
reward: 0.0
done: false
Call 2
B2: complete call-specific user input
# Locations you have already checked (do NOT revisit unless retrieving)
- desk 1: a desklamp 1, a keychain 3, a mug 2, a pen 2, a pen 1, and a pencil 2
# Locations you have NOT yet checked (try these for the target)
bed 1, desk 2, drawer 6, drawer 5, drawer 4, drawer 3, drawer 2, drawer 1,
garbagecan 1, laundryhamper 1, safe 1, shelf 6, shelf 5, shelf 4, shelf 3, shelf 2,
shelf 1
# Recent history
obs: -= Welcome to TextWorld, ALFRED! =-
You are in the middle of a room. Looking quickly around you, you see a bed 1, a
desk 2, a desk 1, a drawer 6, a drawer 5, a drawer 4, a drawer 3, a drawer 2, a dra
action: go to desk 1
# Current observation
You arrive at desk 1. On the desk 1, you see a desklamp 1, a keychain 3, a mug 2, a
pen 2, a pen 1, and a pencil 2.
# Valid actions
- take keychain 3 from desk 1 [PRIORITY: target visible, take now]
- take mug 2 from desk 1
- take pen 1 from desk 1
- take pen 2 from desk 1
- take pencil 2 from desk 1
- use desklamp 1
- go to bed 1
- go to desk 2
- go to drawer 1
- go to drawer 2
- go to drawer 3
- go to drawer 4
- go to drawer 5
- go to drawer 6
- go to garbagecan 1
- go to laundryhamper 1
- go to safe 1
- go to shelf 1
- go to shelf 2
- go to shelf 3
- go to shelf 4
- go to shelf 5
- go to shelf 6
- examine desk 1
- help
- inventory
- look
Call 2: complete actor response
Thought: I need to use the desklamp to examine the bowl, but first I should check
if the bowl is already visible or needs to be located.
Action: use desklamp 1
Call 2: environment return
observation:
You turn on the desklamp 1.
reward: 0.0
done: false
Call 3
31

B3: complete call-specific user input
# Locations you have already checked (do NOT revisit unless retrieving)
- desk 1: a desklamp 1, a keychain 3, a mug 2, a pen 2, a pen 1, and a pencil 2
# Locations you have NOT yet checked (try these for the target)
bed 1, desk 2, drawer 6, drawer 5, drawer 4, drawer 3, drawer 2, drawer 1,
garbagecan 1, laundryhamper 1, safe 1, shelf 6, shelf 5, shelf 4, shelf 3, shelf 2,
shelf 1
# Recent history
obs: -= Welcome to TextWorld, ALFRED! =-
You are in the middle of a room. Looking quickly around you, you see a bed 1, a
desk 2, a desk 1, a drawer 6, a drawer 5, a drawer 4, a drawer 3, a drawer 2, a dra
action: go to desk 1
obs: You arrive at desk 1. On the desk 1, you see a desklamp 1, a keychain 3, a
mug 2, a pen 2, a pen 1, and a pencil 2.
action: use desklamp 1
# Current observation
You turn on the desklamp 1.
# Valid actions
- take keychain 3 from desk 1
- take mug 2 from desk 1
- take pen 1 from desk 1
- take pen 2 from desk 1
- take pencil 2 from desk 1
- use desklamp 1
- go to bed 1
- go to desk 2
- go to drawer 1
- go to drawer 2
- go to drawer 3
- go to drawer 4
- go to drawer 5
- go to drawer 6
- go to garbagecan 1
- go to laundryhamper 1
- go to safe 1
- go to shelf 1
- go to shelf 2
- go to shelf 3
- go to shelf 4
- go to shelf 5
- go to shelf 6
- examine desk 1
- help
- inventory
- look
Call 3: complete actor response
Thought: I need to examine the bowl using the desklamp, so I should look for the
bowl in the current location or nearby locations.
Action: examine desk 1
Call 3: environment return
observation:
On the desk 1, you see a desklamp 1, a keychain 3, a mug 2, a pen 2, a pen 1, and a
pencil 2.
reward: 0.0
done: false
Call 4
B4: complete call-specific user input
# Locations you have already checked (do NOT revisit unless retrieving)
- desk 1: a desklamp 1, a keychain 3, a mug 2, a pen 2, a pen 1, and a pencil 2
# Locations you have NOT yet checked (try these for the target)
bed 1, desk 2, drawer 6, drawer 5, drawer 4, drawer 3, drawer 2, drawer 1,
garbagecan 1, laundryhamper 1, safe 1, shelf 6, shelf 5, shelf 4, shelf 3, shelf 2,
shelf 1
32

# Recent history
obs: -= Welcome to TextWorld, ALFRED! =-
You are in the middle of a room. Looking quickly around you, you see a bed 1, a
desk 2, a desk 1, a drawer 6, a drawer 5, a drawer 4, a drawer 3, a drawer 2, a dra
action: go to desk 1
obs: You arrive at desk 1. On the desk 1, you see a desklamp 1, a keychain 3, a
mug 2, a pen 2, a pen 1, and a pencil 2.
action: use desklamp 1
obs: You turn on the desklamp 1.
action: examine desk 1
# Current observation
On the desk 1, you see a desklamp 1, a keychain 3, a mug 2, a pen 2, a pen 1, and a
pencil 2.
# Valid actions
- take keychain 3 from desk 1 [PRIORITY: target visible, take now]
- take mug 2 from desk 1
- take pen 1 from desk 1
- take pen 2 from desk 1
- take pencil 2 from desk 1
- use desklamp 1
- go to bed 1
- go to desk 2
- go to drawer 1
- go to drawer 2
- go to drawer 3
- go to drawer 4
- go to drawer 5
- go to drawer 6
- go to garbagecan 1
- go to laundryhamper 1
- go to safe 1
- go to shelf 1
- go to shelf 2
- go to shelf 3
- go to shelf 4
- go to shelf 5
- go to shelf 6
- examine desk 1
- help
- inventory
- look
Call 4: complete actor response
Thought: I need to examine the bowl using the desklamp, but the bowl is not visible
yet. I should continue searching for the bowl in other locations.
Action: go to desk 2
Call 4: environment return
observation:
You arrive at desk 2. On the desk 2, you see a alarmclock 1, a bowl 1, and a cd 3.
reward: 0.0
done: false
Call 5
B5: complete call-specific user input
# Locations you have already checked (do NOT revisit unless retrieving)
- desk 1: a desklamp 1, a keychain 3, a mug 2, a pen 2, a pen 1, and a pencil 2
- desk 2: a alarmclock 1, a bowl 1, and a cd 3
# Locations you have NOT yet checked (try these for the target)
bed 1, drawer 6, drawer 5, drawer 4, drawer 3, drawer 2, drawer 1, garbagecan 1,
laundryhamper 1, safe 1, shelf 6, shelf 5, shelf 4, shelf 3, shelf 2, shelf 1
# Recent history
obs: -= Welcome to TextWorld, ALFRED! =-
You are in the middle of a room. Looking quickly around you, you see a bed 1, a
desk 2, a desk 1, a drawer 6, a drawer 5, a drawer 4, a drawer 3, a drawer 2, a dra
action: go to desk 1
33

obs: You arrive at desk 1. On the desk 1, you see a desklamp 1, a keychain 3, a
mug 2, a pen 2, a pen 1, and a pencil 2.
action: use desklamp 1
obs: You turn on the desklamp 1.
action: examine desk 1
obs: On the desk 1, you see a desklamp 1, a keychain 3, a mug 2, a pen 2, a pen 1,
and a pencil 2.
action: go to desk 2
# Current observation
You arrive at desk 2. On the desk 2, you see a alarmclock 1, a bowl 1, and a cd 3.
# Valid actions
- take alarmclock 1 from desk 2 [PRIORITY: target visible, take now]
- take bowl 1 from desk 2
- take cd 3 from desk 2
- go to bed 1
- go to desk 1
- go to drawer 1
- go to drawer 2
- go to drawer 3
- go to drawer 4
- go to drawer 5
- go to drawer 6
- go to garbagecan 1
- go to laundryhamper 1
- go to safe 1
- go to shelf 1
- go to shelf 2
- go to shelf 3
- go to shelf 4
- go to shelf 5
- go to shelf 6
- examine desk 2
- help
- inventory
- look
Call 5: complete actor response
Thought: The target object "bowl" is visible on desk 2, so I should take it.
Action: take bowl 1 from desk 2
Call 5: environment return
observation:
You pick up the bowl 1 from the desk 2.
reward: 0.0
done: false
Call 6
B6: complete call-specific user input
# Locations you have already checked (do NOT revisit unless retrieving)
- desk 1: a desklamp 1, a keychain 3, a mug 2, a pen 2, a pen 1, and a pencil 2
- desk 2: a alarmclock 1, a bowl 1, and a cd 3
# Locations you have NOT yet checked (try these for the target)
bed 1, drawer 6, drawer 5, drawer 4, drawer 3, drawer 2, drawer 1, garbagecan 1,
laundryhamper 1, safe 1, shelf 6, shelf 5, shelf 4, shelf 3, shelf 2, shelf 1
# Recent history
obs: -= Welcome to TextWorld, ALFRED! =-
You are in the middle of a room. Looking quickly around you, you see a bed 1, a
desk 2, a desk 1, a drawer 6, a drawer 5, a drawer 4, a drawer 3, a drawer 2, a dra
action: go to desk 1
obs: You arrive at desk 1. On the desk 1, you see a desklamp 1, a keychain 3, a
mug 2, a pen 2, a pen 1, and a pencil 2.
action: use desklamp 1
obs: You turn on the desklamp 1.
action: examine desk 1
obs: On the desk 1, you see a desklamp 1, a keychain 3, a mug 2, a pen 2, a pen 1,
and a pencil 2.
action: go to desk 2
34

obs: You arrive at desk 2. On the desk 2, you see a alarmclock 1, a bowl 1, and a
cd 3.
action: take bowl 1 from desk 2
# Current observation
You pick up the bowl 1 from the desk 2.
# Valid actions
- go to bed 1
- go to desk 1
- go to drawer 1
- go to drawer 2
- go to drawer 3
- go to drawer 4
- go to drawer 5
- go to drawer 6
- go to garbagecan 1
- go to laundryhamper 1
- go to safe 1
- go to shelf 1
- go to shelf 2
- go to shelf 3
- go to shelf 4
- go to shelf 5
- go to shelf 6
- examine bowl 1
- examine desk 2
- help
- inventory
- look
- move bowl 1 to desk 2
Call 6: complete actor response
Thought: I need to examine the bowl using the desklamp, so I should go to the
desklamp’s location.
Action: go to desk 1
Call 6: environment return
observation:
You arrive at desk 1. On the desk 1, you see a desklamp 1, a keychain 3, a mug 2, a
pen 2, a pen 1, and a pencil 2.
reward: 1.0
done: true
Figure 15:ALFWorld task trajectory.The six calls include every changing input, actor response, and environment
return. The shared prompt blocks appear once.
35

D.4.2 DialSim-subst.
1 actor call / 0 skills / 12 facts / 10 reference episodes
Retrieved record inventory
skills: 0
facts: 12
0c58d947: diana | Diana snagged new boots using Dad’s credit card
7bb0e489: dad’s credit card | Diana used Dad’s credit card to buy the swanky new
boots
c2c7c7ef: diana | Diana used Dad’s credit card to buy the swanky new boots on
September 24, 1994.
1c388d07: diana | Diana is asking about the method used to get the new boots
2a94a7d5: diana | Diana found money outside Central Perk
1c533b0b: diana | Diana snagged swanky new boots
b2df521d: money | Elena lent Diana some money
9ee778e7: elena | Elena lent money to Diana because she felt bad for her
1d23b70b: diana | Diana got a job
66652c40: speaker | The options provided were Lincoln High, Central Perk High,
New York High School, Liberty High, and "I don’t know"
00ac36c6: diana | Answered the question about the high school with "Lincoln High"
739c2e59: diana | discusses her job search and purchase of boots on September 23,
1994
reference episodes: 10
prompt indices: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
Complete user message: task, provided context, and answer instructions
You answer questions about people from your accumulated memory of their
conversations. Today is September 23, 1994.
## Answer style (follow these formats exactly)
- "When did X attend the workshop?" -> 7 May 2023
- If a session dated 27 June 2023 says something happened "last week" -> The week
before 27 June 2023
- "What did X cook for the party?" -> spaghetti with meatballs
- "How long did X’s trip last?" -> two weeks
## Where to look -- location priors (HINTS, verify against the room)
Where these object types are usually found. Use to decide where to search first,
then trust what THIS room actually shows over the prior.
- diana: Diana used Dad’s credit card to buy the swanky new boots on September 24,
1994. (234×); Diana snagged new boots using Dad’s credit card (193×); Answered the
question about the high school with "Lincoln High" (31×); Diana snagged swanky new
boots (28×); Diana is asking about the method used to get the new boots (16×);
Diana found money outside Central Perk (1×); Diana got a job (1×); discusses her
job search and purchase of boots on September 23, 1994 (1×)
- dad’s credit card: Diana used Dad’s credit card to buy the swanky new boots
(243×)
- money: Elena lent Diana some money (1×)
- elena: Elena lent money to Diana because she felt bad for her (1×)
- speaker: The options provided were Lincoln High, Central Perk High, New York High
School, Liberty High, and "I don’t know" (41×)
## Reference episodes (from PAST situations -- the procedure may transfer; specific
places/objects WILL differ here. Trust the current observations over these.)
Experience 1 (weight=1.00):
question: Review the conversation session dated October 13, 1995 and remember the
important facts about the speakers. (part 2)
improvement: VERBATIM EXCERPT:
then maybe um brush the hair away from my face, and look far into my eyes in a way
that let’s me know that something amazing is about to happen.
Victor: Uh-huh.
Diana: And then, I don’t know, I mean you’d pull me really close to you so that, so
that I’d be pressed up, you know, right against you. And, um, it would get kind of
sweaty and uh, and blurry, and then it’s just happen
Experience 2 (weight=1.00):
question: Review the conversation session dated October 12, 1995 and remember the
important facts about the speakers. (part 2)
improvement: VERBATIM EXCERPT:
s, what did you think a nubbin was?
Tobias: I don’t know, you see somethin’, you hear a word, I thought that’s what it
was. Let me see it again.
36

All: Yeah, show it. Show it. The nubbin, the nubbin, the nubbin.
Marcus: Tobias was in a porno movie.
All: Huuh.
Marcus: If I’m goin’ down, I’m takin’ everybody with me.
Victor: You were in a porno?
Tobias: Ahh, alright, alright, alright
Experience 3 (weight=1.00):
question: Review the conversation session dated October 6, 1995 and remember the
important facts about the speakers. (part 2)
improvement: VERBATIM EXCERPT:
, and then, all of a sudden, it’s just magically broken?
Elena: Iris, tell her!
Iris: Ok, I didn’t see it, because I was putting on my jacket, but I uh want to
believe you.
Diana: Hey Marcus. Elena just broke my seashell lamp.
Marcus: Neat. I’m gonna die alone.
Diana: Ok, you win.
Elena: Marcus, you’re not gonna die alone.
Marcus: Paula was my safety net, ok? And now I have to ge
Experience 4 (weight=1.00):
question: Review the conversation session dated September 28, 1995 and remember
the important facts about the speakers. (part 2)
improvement: VERBATIM EXCERPT:
e little toys move? Opposable thumbs. Without evolution, how do you explain
opposable thumbs?
Iris: Maybe the overlords needed them to steer their spacecrafts.
Victor: Please tell me you’re joking.
Iris: Look, can’t we just say that you believe in something, and I don’t.
Victor: No, no, Pheebs, we can’t, ok, because-
Iris: What is this obsessive need you have to make everyone ag
Experience 5 (weight=1.30):
question: review a conversation session and remember important facts about the
speakers
improvement: analyze the conversation to identify key speakers, extract their
statements, and note recurring themes and relationships
VERBATIM EXCERPT:
Read this past conversation session and note the important facts (dated September
23, 1994):
Diana: Oh God, come on you guys, is this really necessary? I mean, I can stop
charging anytime I want.
Elena: C’mon, you can’t live off your parents your whole life
Experience 6 (weight=1.30):
question: Review a conversation session and remember important facts about the
speakers
improvement: Identify all speakers in the conversation, note their key statements
and interactions, and summarize their roles and relationships within the dialogue.
VERBATIM EXCERPT:
Read this past conversation session and note the important facts (dated September
23, 1994):
Tobias: Of course it was a line!
Elena: Why?! Why? Why, why would anybody do something like that?
Victor: I assume we’re looking for a
Experience 7 (weight=1.30):
question: Review a conversation session and remember important facts about the
speakers
improvement: Identify the date and speakers involved, note key themes and
relationships, summarize each speaker’s contribution, and extract main facts about
the conversation’s context and outcome
VERBATIM EXCERPT:
Read this past conversation session and note the important facts (dated November 24,
1994):
Tobias: Nope, not that one.
Elena: Can you go any faster with that?
Tobias: Hey, I got one keyhole and a
Experience 8 (weight=1.30):
question: review a conversation session and remember important facts about the
speakers
37

improvement: listen to the conversation, identify all speakers, note key topics
discussed, and record relationships and themes between participants
VERBATIM EXCERPT:
Read this past conversation session and note the important facts (dated April 27,
1995):
Tobias: How could someone get a hold of your credit card number?
Elena: I have no idea. But look how much they spent!
Diana: Elena, would you calm down? Th
Experience 9 (weight=1.30):
question: review a conversation and remember important facts about the speakers
improvement: analyze the conversation to identify key speakers and their
statements, then extract and remember the important facts about each speaker’s role
and statements
VERBATIM EXCERPT:
Read this past conversation session and note the important facts (dated September
22, 1994):
Elena: Now I’m guessing that he bought her the big pipe organ, and she’s really not
happy about it.
Marcus: Tuna or egg salad?
Experience 10 (weight=1.30):
question: review a conversation session and remember important facts about the
speakers
improvement: listen to the conversation session, identify the date and speakers,
note key themes and speaker contributions, summarize the main points and character
dynamics
VERBATIM EXCERPT:
Read this past conversation session and note the important facts (dated March 6,
1995):
Victor: So, you gals wanna hand over your money now? That way, we don’t have to go
through the formality of actually playing.
Diana
Question: So, could we BE any more curious about how Diana snagged those new boots?
Options: She found money outside Central Perk / She got a job / Dad’s credit card /
Elena lent her some money because she felt bad for her / I don’t know. (None of the
above)
Answer with the exact option text.
Answer with ONLY a short phrase (a few words, a date, or a name). Give your best
short answer whenever ANY fact or excerpt relates to the question -- only if
absolutely nothing relates, answer: No information available.
Answer:
Complete actor response
Dad’s credit card
Adapter submission
Answer: Dad’s credit card
Environment return
observation:
(answered)
reward: 1.0
done: true
Evaluation result
reference_answer: Dad’s credit card
token F1: 100%
Figure 16:DialSim task trajectory.The complete prompt contains facts and conversation records without a skill.
The answer matches the reference.
38

D.4.3 MATH-hard
1 actor call / 1 skill / 4 facts
Retrieved record inventory
skills: 1
12190a98: simplify-and-convert
facts: 4
68b4340e: circle | the equation can be transformed into standard form by
rearranging and completing the square
72783530: circle | can intersect with another circle at most twice
1f0be7bd: circle | can overlap with another circle of different radius
3163899d: circular base | area is proportional to the square of the radius
reference episodes: 0
Complete system message
You are an expert problem solver working through a stream of tasks.
Skill blocks and memory notes, when provided, are advisory: use them if they help,
ignore them if they do not apply to the current task.
Work each task IN FULL -- reason step by step as deeply as the problem requires.
Follow the answer-format instructions given in the observation (e.g. include ONE
“‘python block when allowed, and finish with the requested answer line).
Complete user message: task, provided context, and answer instructions
# Task
Solve this competition math problem. Put your final answer in \boxed{}. Find the
center of the circle with equation $x^2 - 6x + y^2 + 2y = 9$.
# Retrieved context (skill+afford)
## Procedure to follow (HOW -- the step order; fill in WHERE from below + the room)
Skill 1: simplify-and-convert
description: Use this skill to simplify mathematical expressions, convert units,
or transform numbers between formats.
capability: verb=examine affordance=none output=object_processed
when_to_use: - Simplify a mathematical expression to a specific form
- Convert a number between different units or number bases
- Transform a repeating decimal into a fraction
- Express a radical in its simplest form
procedure:
- Systematic Expression Analysis: Examine the structure of <target> to identify
the type of transformation needed; look for radicals, repeating decimals, or unit
conversions. Apply this when the task is first parsed.
- Confirm Target Type: If <target> is a repeating decimal, set up an equation
to isolate the repeating part. Apply this when the target is identified as a
repeating decimal.
- Apply Simplification Rules: If <target> contains square roots, rationalize
denominators and combine like terms. Apply this when the target involves radicals.
- Convert Units or Bases: If <target> requires un
## Constraints -- rules about how things work (RESPECT THESE)
These are reliable facts about how appliances/containers behave. Violating them
causes failure.
- circle: the equation can be transformed into standard form by rearranging and
completing the square (1×); can intersect with another circle at most twice (1×);
can overlap with another circle of different radius (1×)
- circular base: area is proportional to the square of the radius (1×)
# Current observation
Solve this competition math problem. Put your final answer in \boxed{}.
Find the center of the circle with equation $x^2 - 6x + y^2 + 2y = 9$.
You may reason, and you may include ONE “‘python block -- I will execute it and show
you the output. Finish with: The answer is <answer>
# Valid actions
- <your reasoning / python / answer>
# Your response format
Free form. Reason step by step as deeply as needed, then follow the answer format
asked for in the observation.
Complete actor response
To find the center of the circle given by the equation:
$$
39

x^2 - 6x + y^2 + 2y = 9
$$
we need to rewrite the equation in the **standard form of a circle **, which is:
$$
(x - h)^2 + (y - k)^2 = r^2
$$
where $(h, k)$ is the center of the circle and $r$ is the radius.
--
### Step 1: Group and complete the square
We start by grouping the $x$-terms and $y$-terms:
$$
(x^2 - 6x) + (y^2 + 2y) = 9
$$
Now, complete the square for both $x$ and $y$.
#### For $x^2 - 6x$:
- Take half of $-6$, which is $-3$, and square it: $(-3)^2 = 9$
- Add and subtract 9:
$$
x^2 - 6x = (x - 3)^2 - 9
$$
#### For $y^2 + 2y$:
- Take half of $2$, which is $1$, and square it: $1^2 = 1$
- Add and subtract 1:
$$
y^2 + 2y = (y + 1)^2 - 1
$$
--
### Step 2: Substitute back into the equation
$$
(x - 3)^2 - 9 + (y + 1)^2 - 1 = 9
$$
Simplify:
$$
(x - 3)^2 + (y + 1)^2 - 10 = 9
$$
$$
(x - 3)^2 + (y + 1)^2 = 19
$$
--
### Step 3: Identify the center
From the standard form $(x - h)^2 + (y - k)^2 = r^2$, we can see that:
- $h = 3$
- $k = -1$
So, the center of the circle is:
$$
(3, -1)
$$
--
### Final Answer
$$
\boxed{(3, -1)}
$$
Environment return
observation:
(submitted)
reward: 1.0
done: true
Evaluation result
reference_answer: (3, -1)
Figure 17:MATH-hard task trajectory.The complete actor response ends with the reference answer.
40

D.4.4 MBPP
1 actor call / 2 skills / 4 facts / 2 reference episodes
Retrieved record inventory
skills: 2
c1a741f2: filter-string-content
0a4e3b3e: string-processing
facts: 4
82ade9b6: python function | can be named to match expected test case names
28f550cb: string | can be modified by replacing specific characters
37dd4687: string | can be indexed to access individual characters
28c906da: function | can be defined to perform specific string manipulation tasks
reference episodes: 2
prompt indices: 1, 2
Complete system message
You are an expert problem solver working through a stream of tasks.
Skill blocks and memory notes, when provided, are advisory: use them if they help,
ignore them if they do not apply to the current task.
Work each task IN FULL -- reason step by step as deeply as the problem requires.
Follow the answer-format instructions given in the observation (e.g. include ONE
“‘python block when allowed, and finish with the requested answer line).
Complete user message: task, provided context, and answer instructions
# Task
Write a python function to find the first repeated character in a given string.
# Retrieved context (skill+afford+raw)
## Procedure to follow (HOW -- the step order; fill in WHERE from below + the room)
Skill 1: filter-string-content
description: Use this skill to filter characters from a string based on specific
criteria.
capability: verb=clean affordance=none output=object_processed
when_to_use: - Filter characters from a string based on specific conditions.
- Remove characters that meet certain criteria from a given string.
- Process a string to retain only characters that do not match a defined set.
procedure:
- Systematic Character Inspection: Iterate through each character in <target>,
checking if it meets the <criteria>; apply this when the target string is in
inventory and the criteria is defined.
- Conditional Character Retention: Keep characters that do not meet the
<criteria> and combine them into a new string; apply this when the character
inspection is complete.
- Result Formation: Combine the filtered characters into a new string and
return it as the result; apply this when all characters have been processed.
Skill 2: string-processing
description: Use this skill to process strings by filtering, transforming, or
reformatting based on specific rules.
when_to_use: - When transforming a string by removing specific characters
- When applying a rule to filter or modify a string
- When reformatting a string according to a defined pattern
procedure:
- Define Processing Rule: Establish the rule that will be applied to <target>
to determine which characters to keep or modify. Apply this before any string
manipulation.
- Filter Characters: Iterate through each character in <target> and apply the
defined rule to determine if it should be included in the result. Apply this when
the rule is defined and the string is in inventory.
- Construct Result: Combine the filtered characters into a new string and
return it as the processed result. Apply this when the filtering is complete and
the result is ready.
- Verify Output: Confirm that the processe
## Constraints -- rules about how things work (RESPECT THESE)
These are reliable facts about how appliances/containers behave. Violating them
causes failure.
- python function: can be named to match expected test case names (5×)
- string: can be modified by replacing specific characters (2×); can be indexed to
access individual characters (2×)
- function: can be defined to perform specific string manipulation tasks (3×)
41

## Reference episodes (from PAST situations -- the procedure may transfer; specific
places/objects WILL differ here. Trust the current observations over these.)
Experience 1 (weight=1.30):
question: write a python function to find the first non-repeated character in a
given string
improvement: count the frequency of each character in the string using a
dictionary, then iterate through the string again to find the first character with a
frequency of 1
Experience 2 (weight=1.30):
question: Write a function to remove first and last occurrence of a given
character from a string
improvement: Use find and rfind to locate first and last occurrence of the
character. If found, slice the string to exclude those positions. Return original
string if character not found.
# Current observation
Write a python function to find the first repeated character in a given string.
Name the function exactly ‘first_repeated_char‘.
Your code should pass tests like: assert first_repeated_char("abcabc") == "a"
You may reason, and you may include ONE “‘python block -- I will execute it and show
you the output. Finish with: The answer is <answer>
For coding tasks, provide the complete solution in the “‘python block (the block
itself is your answer).
# Valid actions
- <your reasoning / python / answer>
# Your response format
Free form. Reason step by step as deeply as needed, then follow the answer format
asked for in the observation.
Complete actor response
To solve the problem of finding the first repeated character in a given string, we
can follow a systematic approach:
1. **Track Character Frequencies **: We can use a dictionary to count the frequency
of each character in the string. This allows us to identify which characters are
repeated.
2. **Identify the First Repeated Character **: Once we have the frequency counts,
we can iterate through the string again and check for the first character that has a
frequency greater than 1.
This approach ensures that we efficiently determine the first repeated character in
the string.
Here is the implementation of the function ‘first_repeated_char‘:
“‘python
def first_repeated_char(s):
# Step 1: Count the frequency of each character
char_count = {}
for char in s:
if char in char_count:
char_count[char] += 1
else:
char_count[char] = 1
# Step 2: Find the first character with a frequency greater than 1
for char in s:
if char_count[char] > 1:
return char
# If no repeated character is found, return None or an appropriate value
return None
“‘
The answer is ‘first_repeated_char‘
Environment return
observation:
(submitted)
reward: 1.0
done: true
Evaluation result
provided tests passed: 3/3
Figure 18:MBPP task trajectory.The original submission passes the three provided tests.
42
