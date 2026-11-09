---
title: 'SkillGLoW: Procedural-Family Skill Consolidation for Self-Improving Agents on Long-Horizon Task
  Streams'
url: https://arxiv.org/abs/2609.02217
category: ai-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Ao Yan
- Xin Zhang
- Jiawei Du
- Joey Tianyi Zhou
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.02217
pages: 20
chars: 88939
fetched_at: '2026-11-08T13:35:17+00:00'
kb_version: 1
---

# SkillGLoW: Procedural-Family Skill Consolidation for Self-Improving Agents on Long-Horizon Task Streams

SkillGLoW: Procedural-Family Skill Consolidation for Self-Improving Agents on
Long-Horizon Task Streams
Ao Yan1, Zhang Xin2, Jiawei Du2, Joey Tianyi Zhou2∗
1National University of Singapore, Singapore
2Institute of Advanced Intelligence and Computing (IAIC), Singapore
Abstract
LLMagentsincreasinglyself-improvebywritingandreusing
textual skills, kept either as one global document or as a flat
pool of per-task entries, though most of the evidence comes
fromdomainswithstructurallysimilartasks.Onlong-horizon
workloads where each task demands a different solution, the
two forms fail in opposite ways: the document collapses into
generic discipline, while the pool inflates and its entries stay
bound to the instance that wrote them. We argue the missing
unit of reuse is the solving procedure shared by a cluster of
related tasks, and build SkillGLoW (Global–Local Weave)
around it: the local skills a task writes from its own execu-
tion are aggregated into procedural families and compressed
into de-instantiated global priors, while the instance detail
they hold is regenerated per task rather than stored; a commit
gate admits a prior only when real execution shows it does
not degrade the deployed library. Across four benchmarks
(mathematical reasoning, terminal automation, software re-
pair, and embodied control) and three models, the priors gain
17.2 points (hard) over the no-skill baseline on average, with
positivegainsinall12continual-improvementruns,and18.0
with local regeneration, while the library holds one prior per
proceduralfamily,3.6×morecompactthantheper-taskpool.
Under the same protocol GLoW leads a published single-
document optimizer on 15 of 21 cells. Unmodified, the li-
brary lifts success on unseen ALFWorld tasks from 73.9% to
83.9%, evidence that what transfers is procedure rather than
task memory.
1 Introduction
As base models and agent harnesses mature, LLM agents
are moving from short-horizon, closed tasks toward longer-
horizon,morecomplexenvironments(Yaoetal.2023;Shinn
et al. 2023; Liu et al. 2024; Mialon et al. 2024; Jimenez
et al. 2024; Merrill et al. 2026). Such tasks quickly outgrow
fixed prompts and human-written skills, so recent systems
distill reusable skills from their own execution trajectories
(Zhou et al. 2026a; Lin et al. 2026; Ni et al. 2026) and write
successful or failed experience into documents reused by
prompt injection (Kang et al. 2026; Yang et al. 2026a; Zhou
et al. 2025). Once skills are continually generated, revised,
andreused,amorefundamentalquestionarises:inwhatform
should an agent organize and maintain these skills?
SkillsBench offers direct evidence. Human-curated skills
raisethepassrateby16.2points,whileskillsamodelwrites
∗Corresponding author.
...
One entry per task,
Grows with the stream
Tasks Retrieve Top-K
Managment
Retrieve
Score
Edit
Delete
......
(c) GLoW ： Global-Local Weave (Ours)
The Right Granularity: Procedural Families
The Fix - Memory Granularity
Coarse
Too Coarse Too Fine GLoW - The Right Grain
Consolidation
Group the per-task skills, Keep each family's shared procedure
Security
(a) Single Global Document
Granularity: Too Coarse (Over-compressed)
Software Build
Data Analysis
Terminal Ops
Single
Skill.md
Distinct procedures into one document
(b) Flat Skill Library
Granularity: Too Fine (Instance-overfitted)
Unbounded growth, noisy retrieval
Many Small
Task-Specific Entries
Procedures Averaged Unbounded Registry
One Global Document One Procedure Per Family
Task Family
ProcedureTask Family
G1G2
G1     Gk
Family priors
Global SkillsGroup by
procedure
L1L2L3
Per-task
Local Skills
L1 ... Lk
Consolidate ：
keep the shared step,
drop instance detail
Fine
The reusable unit = the procedure shared by a family of tasks
Best
Skill.md
Balanced  Point
Pass
Fail
Commit
Gate
Figure 1: The failure modes of single-document and flat-
library skill organizations on heterogeneous long-horizon
workloads, and the procedural-family unit that GLoW con-
solidates between them.
for itself from the task description alone land1.3pointsbe-
lowtheno-skillbaseline(Lietal.2026a).Recentexperience-
driven methods therefore ground skills in real execution tra-
jectories,buttheirevidenceconcentratesonstructurallysimi-
lartasks;onlong-horizonworkloads,littlebeyondmeta-level
experience transfers across tasks (Kim et al. 2026).
Every organizational form makes an implicit assump-
tion about the task distribution. A single global document
assumes that most tasks share one dominant procedure;
a per-task skill library assumes that old entries can be
arXiv:2609.02217v1  [cs.AI]  2 Sep 2026

reused wholesale. Both assumptions roughly hold in struc-
turallysimilardomains,buttheyfailsimultaneouslyonlong-
horizon workloads with heterogeneous solutions (Figure 1):
no dominant procedure exists, and few old entries fit new
tasks (Kim et al. 2026; Cao et al. 2026), a pattern that sur-
vives when the pool is queried by retrieval (§4.3). Both fail-
ures point to a missing unit of reuse, one that sits between
the single document and the single entry. Solutions differ
from instance to instance, but tasks are not isolated. Simi-
lar tasks form families and share a solving procedure, while
each instance carries local constraints that surface only dur-
ing execution. The shared procedure transfers across tasks;
theinstancedetailsdonot.Anorganizationalschemeshould
keep both.
Building on this observation, we proposeSkillGLoW
(Global–Local Weave; GLoW), a layered skill-organization
framework (Figure 2). GLoW groups execution evidence
intoproceduralfamiliesandsplitsskillsintotwolayers.The
global layer compresses each family’s shared procedure into
astablepriorthatguidessearch;thelocallayerisregenerated
for each task from its own execution feedback, supplies the
instance detail the prior cannot carry, and is what the next
round consolidates. The two are combined at solving time
and separated at consolidation time. The global prior stays
frozen during a solving episode and is revised only offline,
and a revision is committed only when it does not degrade
the deployed library in real execution.
We evaluate GLoW across three models on four bench-
marks: mathematical reasoning, terminal automation, soft-
ware repair, and embodied control, giving 12 continual-
improvement runs in which a multi-setting protocol sepa-
rates the contributions of the frozen prior and within-task
regeneration.Thecommittedpriorsimproveovertheno-skill
baseline by 17.2 points on average, with positive gains in all
12 runs, while the deployed library holds one prior per pro-
cedural family rather than one per task,3.6×more compact
than the per-task pool. Our contributions are as follows:
•Wemeasureallthreepriororganizations—thesingledoc-
ument, the per-task pool, and the pool with retrieval—on
the same streams (§4.3); each gains less than family con-
solidation,identifyingthemissingunitofreuse:thesolv-
ing procedure shared by a cluster of tasks.
•We propose GLoW, which adopts the procedural family
asthisunitandgateslong-termupdatesbyrealexecution
(§3.1–§3.5).
•Weshowthat,acrossthesameruns,thefrozenpriorsraise
the mean success rate on unseen embodied tasks from
73.9% to 83.9%, indicating that what is consolidated is
reusable procedure rather than task memory.
2 Related Work
Skillconstructionandoptimization.Agentskillsarepro-
cedural knowledge reused at inference time (Schick et al.
2023; Li et al. 2026a; Zhou et al. 2026b). An earlier line has
agents discover them as executable code through environ-
ment exploration (Wang et al. 2023; Zheng et al. 2025); the
systems closest to ours write them as text. AutoSkill mines
candidates from long-term conversations under a judge that
governs additions and deletions (Yang et al. 2026b), while
Trace2Skill (Ni et al. 2026) and, earlier, ExpeL (Zhao et al.
2024) pool many trajectories before distilling, since single-
trajectory summaries overfit. SkillOpt trains one skill doc-
ument as the external state of a frozen agent, admitting an
edit only when it improves performance on a held-out split,
and scopes it to a single domain (Yang et al. 2026a). Skills
of this kind belong to a broader line that treats text as an
optimizable parameter, whether through prompt optimizers
(Yuksekgonul et al. 2025; Khattab et al. 2024; Yang et al.
2024a), self-feedback refinement (Madaan et al. 2023), or
context compression (Kang et al. 2026). In that line the op-
timized object need only stay valid on one distribution; ours
has to hold across a family of tasks. These methods ask how
toproduceabetterskill;weaskatwhatgranularitygenerated
skills should be maintained.
Skill organization, transfer, and abstraction.Most sys-
tems store skills in a single layer, either one continually
rewritten document (Yang et al. 2026a) or a flat retrievable
library (Yang et al. 2026b; Zhou et al. 2025), and lean on
retrieval and governance: ReMe deduplicates with a judge
and prunes low-utility entries (Cao et al. 2026). The same
granularityquestionrunsthroughprocedural-memorywork,
whose stored unit ranges over reusable workflows (Wang
etal.2025b),distilledprocedures(Fangetal.2026),reason-
ing traces (Ouyang et al. 2026b), cross-domain experience
entries (Tang et al. 2025), and test-time scratchpads (Suz-
gun et al. 2025). That evidence comes largely from struc-
turally similar tasks; relax the assumption and cross-domain
retrieval induces negative transfer, with abstract memories
traveling better than task-specific detail (Kim et al. 2026).
XSkill is closest architecturally, pairing an action-level ex-
periencestreamwithatask-levelskillstream,bothgrounded
in visual observations for multimodal tool use (Jiang et al.
2026).Itslocalcomponentisretrievedfrompastrecordsand
adapted; ours comes from the current task’s own feedback
and is never written back.
Lifecycleandmulti-skillmaintenance.Athirdlinemain-
tains the skill system under long-term use. SkillOS casts
self-evolution as library governance, freezing the executor
and learning when the library should change (Ouyang et al.
2026a). SkillGraph adds prerequisite structure to retrieval
(Li et al. 2026b); others extend governance to runtime loops
and multi-agent settings (Lin et al. 2026; Pan et al. 2026;
Zhang et al. 2026; Du et al. 2025). All relocate the difficulty
to when and how entries are edited, and all need a utility
scorer, learned or hand-set. GLoW keeps no such policy:
the global layer is re-derived each round from that round’s
local evidence, so retention falls out of consolidation, and
acceptance turns only on measured downstream execution.
3 Method
3.1 Problem Formulation
We define askillas a natural-language procedure inserted
into the agent’s context. Given a frozen agentπ, a taskx,
a skill contexts, and an execution harnessh, one execution
returns a trajectory and a verifier score(τx(s), rx(s)) =

{x1,x2, ... ,xN}
Task Stream Trajectory Difference Localize
Trajectory 1
Trajectory 2
Agent
(a) Local Evidence Generation
Structured Evidence: Skill Card cx
cx = (x, ax ,τx, rx, Lx)
r = 0.4
r = 0.8
(b) Consolidation and Verifier-Grounded Commit
Procedural Clustering
Embeddings
Consensus
Group
Prior Compression
Gk = Compress(Family Lx)
Family Lx
Skill Card cx Condense
Shared Procedure
Filter
Instance Details
Verifier-Grounded Commit
Candidate
Priors
Gk new
Prior Skills Gk
PASS
Commit Gate
Vnew>= Ak - ε
Ak = Vhistory best
Fail
Global Library
Discard
(c) Execution-Time Global-Local Weaving
{x1,x2, ... ,xN}
Task Stream
Global Library
Recall Gx
Recall Execution & Local Skill Regenerate
Agent Prior Skills
Collect Feedback
Regenerate Lx
Figure 2: Overview of GLoW. Each task’s local skill is encapsulated as a skill card; cards are aggregated into procedural
families and compressed into candidate global priors; candidates are committed only through a verifier-grounded gate on real
downstream execution; at execution time, the frozen prior is woven with a freshly generated local skill.
h(π, x, s)withrx(s)∈[0,1]. That is, changingsis our
onlyhandleonthefrozenagent’sbehavior,andr x istheonly
trustworthymeasureofeffect.GLoWmaintainsacommitted
global prior libraryG={G base, G1, . . . , GK}, where each
Gk carries the procedural structure shared by one family of
tasksandKisfarsmallerthanthenumberofhistoricaltasks.
For a taskx, the system recalls the relevant prior fromG:
Gx = Recall(G, x) =Gbase ⊕G k(x),(1)
where⊕denotes context concatenation,G base is injected
unconditionally, andG k(x) is the family prior recalled by
similarity (§3.5). A Localize module generates a task-local
skillL x = Localize(∆τ x, rx), where∆τ x collects the dif-
ferencesbetweensuccessivetrajectoriesofx,andr x denotes
the corresponding verifier scores;Lx depends only on the
current task’s own execution feedback, queries no historical
library,andisnotwrittenintothelong-termlibrary.GLoW’s
objective is to construct and maintainGover the task stream
sothattheexpectedexecutionvalueofthecombinedcontext
is maximized:
max
G
Ex∼D
h
rx

Recall(G, x)⊕Lx
i
,(2)
whereDdenotes the task distribution of the stream. Library
size is set by the family structure rather than by the stream,
sinceconsolidationmaintainsonepriorperfamily(§3.3),so
|G|tracks the number of distinct procedures found, not the
number of tasks seen. Optimizing Eq. (2) is hard because
rx is a black box, the granularity ofGis unknown, and
language compression is lossy; §3.2–§3.5 address these in
turn (Algorithm 1).
3.2 Local Evidence and Skill Cards
A local skill is generated from trajectory differences be-
tween multiple real executions of the same task. Localize
compareswhatchangedbetweenadjacentrunsand,together
withverifierfeedback,judgeswhichchangestrulyadvanced
the task, retaining the operational hypotheses that execu-
tion feedback has already supported on the current task.
To support subsequent clustering and consolidation, GLoW
encapsulates each task’s local experience as askill card
cx = (x, ax, τx, rx, Lx): the task instruction, an abstract
signature naming what the solution did, the trajectory text,
theverifierscore,andthelocalskill.∆τ x feedsLocalizeand
is not carried on the card.
3.3 ProceduralClusteringandPriorCompression
The basic unit of offline consolidation is a family of proce-
durally similar local skillsLx. GLoW groups by “how it is
solved” rather than “what the task is about”. Each card sup-
plies four textual views—the signatureax, the instructionx,
the skill textLx, and the trajectoryτx—encoded separately
(Reimers and Gurevych 2019) and fused with fixed weights
intoϕ(c). The signature carries the largest weight andLx
the smallest, so grouping follows the procedure rather than

Algorithm 1: GLoW: one pass over a task stream
Require:agentπ, harnessh, streamD, roundsT, sub-
roundsJ
Ensure:committed prior libraryG
1:G ← {Gbase}
2:fort= 1toTdo
3:Stage 1local evidence;C ← ∅
4:forj= 1toJdo
5:for alltaskx∈ Ddo
6:G x ←Recall(G, x)▷frozen for the episode
7:(τ x, rx)←h(π, x, Gx)
8:repeat
9:L x ←Localize(∆τ x, rx)▷no library lookup
10:(τ x, rx)←h(π, x, Gx ⊕L x)
11:untiliteration budget exhausted
12:C ← C ∪ {(x, a x, τx, rx, Lx)}▷card;L x never
entersG
13:end for
14:end for
15:Stage 2consolidation
16:{C k}k≤K ←ConsensusCluster(ϕ(C))▷auto-K
17: ˆGk ←Compress(C k)for allk≤K ▷de-instantiate
18:Stage 3admission
19:G ′ ← {Gbase} ∪ {ˆGk}k≤K ▷the round’s candidate
revision
20:G ← G ′ ifGate(G ′,G)accepts▷one decision per
round; §3.4
21:end for
22:returnG
either wording. Views and weights are fixed across bench-
marks;valuesareintheappendix.Asinglehierarchicalclus-
tering is sensitive to the linkage rule and to the number of
clusters (Ward 1963). GLoW therefore runs many of them,
varying both, and records how often each pair of tasks lands
inthesamegroup.Thatco-occurrencefrequencybecomesa
consensus similarity (Monti et al. 2003), and the final fam-
ilies come from clustering on it. The number of clusters is
selected automatically by the Kneedle knee point (Satopää
et al. 2011) of the silhouette curve (Rousseeuw 1987). Each
family is compressed into one candidate prior:
G(t) k = Compress  C(t) k  .(3)
Whether a candidate prior enters the library is decided by
the verifier-grounded gate of §3.4. The goal of prior com-
pression is de-instantiated induction over the group’s local
skills: extract the recurring solving skeleton and filter out
bindingsthatholdonlyinasingleinstance.Ageneratedcan-
didatepriorretainsonlythreekindsofcontent:applicability
conditions, the core solving procedure, and common failure
modes;thefilteredinstancedetailsarerecoveredbythelocal
skillL x that is freshly regenerated at execution time.
3.4 Verifier-Grounded Commit
Acandidatepriorisnotwrittenintothelibrarydirectly:com-
pression can widen a rule or drop a constraint, and the text
offers no way to tell. Admission therefore rests on measured
execution.Theexecutionvalueofdeployingpureglobalpri-
ors on a task setDis
V(G;D) = 1 |D| X x∈D rx  Recall(G, x)  ,(4)
wheretheargumenttor x istherecalledprioralone,withno
Lxappended,sothatthemeasuredvalueisattributabletothe
prior rather than to task-local adaptation. A round’s candi-
dates come from three routes. The first is fresh compression
ofthatround’slocalskills(§3.3).Thesecondisappend-only
repair:wherethedeployedpriorlostground,scope-restricted
guards distilled from the degraded tasks’Lx are appended,
leaving the verified structure intact. The third carries for-
ward, for each family, whichever version has scored best so
far. Every route yields one prior per family, and the priors
of a round together form a candidate revisionG(v), scored
under Eq. (4). The gate keeps the best:
V real = max
v
V

G(v);D  ,
commit⇐ ⇒V real ≥A−ϵ. (5)
ThewinneriscommittedonlywhenEq.(5)holds;otherwise
the library is left untouched. Admission is decided once per
roundovertherevisionasawhole,notseparatelyperfamily.
The anchorA= max

V ⋆, Vns is the larger of the stand-
ing library’s value and the No-Skill baseline, andϵ= 0.02
absorbs fluctuation.Ais floored further at the highest value
any measurement in the previous round reached, so a re-
vision cannot pass by clearing the standing commit alone.
The maximum therefore selects among candidate texts, not
among repeated measurements of one, and since the anchor
is itself measured, a round can change the library only by
performing at least on par with the standing result, up to
measurement noise (ϵ= 0.02).
3.5 Execution-Time Global–Local Weaving
At test time, the committed global prior library stays frozen.
For a new taskx, Recall implements Eq. (1) in two lev-
els: the base prior is always present; on the family-prior
side, the system builds an embedding for the full text of
each committed prior (Zhang et al. 2025), embeds the task
instruction as the query, takes the cosine-similarity top-1,
and injects it only when similarity exceeds a fixed threshold
shared across benchmarks, otherwise falling back toGbase
alone (fail-closed). Recall completes before the task starts
and stays fixed throughout the task’s execution. The agent
then executes underGx and collects feedback from the cur-
renttask.LocalizegeneratesafreshlocalskillL x asin§3.2.
In subsequent solving, the agent usesGx ⊕L x as the skill
context and keeps updatingLx. ThisL x is staged as local
evidenceofthecurrentsub-round.Aftertheround,theseL x
feed consolidation and admission (Alg. 1, Stages 2–3).
4 Experiments
4.1 Setup
Benchmarks.We use four benchmarks, ordered from low
to high cross-task procedure sharing: Terminal-Bench-Pro
(TBP) (Wang et al. 2025a), SWE-bench Verified (Jimenez

TBP↑SWE↑ALFWorld↑LMB↑Avg.↑
Methodhard soft hard soft hard soft hard=soft hard soft
DeepSeek-V4-Pro
No-Skill 34.4 68.9 45.0 47.5 57.1 67.9 13.2 37.4 49.4
SkillOpt† 43.8↑9.4 64.8↓4.1 60.0↑15.0 64.8↑17.3 90.5↑33.4 94.4↑26.5 22.6↑9.4 54.2↑16.8 61.7↑12.3
GLoW (Global)50.0 ↑15.6 74.9↑6.0 70.0↑25.0 72.4↑24.9 83.3↑26.2 88.1↑20.2 37.7↑24.5 60.3↑22.9 68.3↑18.9
GLoW (Global+Local) 43.8 ↑9.4 81.0↑12.1 70.0↑25.0 72.5↑25.0 81.0↑23.9 81.0↑13.1 39.6↑26.4 58.6↑21.2 68.5↑19.1
MiniMax-M3
No-Skill 40.6 77.1 35.0 39.8 76.2 90.5 22.6 43.6 57.5
SkillOpt† 43.8↑3.1 76.2↓0.9 55.0↑20.0 55.0↑15.2 95.2↑19.0 97.6↑7.1 28.3↑5.7 55.6↑12.0 64.3↑6.8
GLoW (Global)53.1 ↑12.5 86.7↑9.6 60.0↑25.0 62.5↑22.7 92.9↑16.7 94.5↑4.0 28.3↑5.7 58.6↑15.0 68.0↑10.5
GLoW (Global+Local)53.1 ↑12.5 83.6↑6.5 65.0↑30.0 67.5↑27.7 90.5↑14.3 93.7↑3.2 35.8↑13.2 61.1↑17.5 70.2↑12.7
GPT-5.4-mini
No-Skill 28.1 75.6 35.0 37.4 42.9 60.9 15.1 30.3 47.2
SkillOpt† 40.6↑12.5 80.0↑4.4 40.0↑5.0 42.4↑5.0 61.9↑19.0 74.2↑13.3 13.2↓1.9 38.9↑8.7 52.5↑5.2
GLoW (Global)50.0 ↑21.9 83.0↑7.4 45.0↑10.0 47.4↑10.0 61.9↑19.0 77.8↑16.9 18.9↑3.8 43.9↑13.6 56.8↑9.6
GLoW (Global+Local) 46.9 ↑18.8 85.8↑10.2 50.0↑15.0 55.7↑18.3 66.7↑23.8 76.0↑15.1 18.9↑3.8 45.6↑15.3 59.1↑11.9
Table1:Mainresults(%,12continual-improvementruns).Subscriptsgivethechangeoverthatmodel’sNo-Skillrow,computed
before rounding (↑gain,↓loss; the arrow, not the color, carries the sign). LMB is binary multiple-choice, so hard=soft. Best
per column within a model block inbold.†Run protocol is given in §4.2.
et al. 2024) (solved through an agentic harness (Yang et al.
2024b)), ALFWorld (Shridhar et al. 2021), and LiveMathe-
maticianBench (LMB) (He et al. 2026). In the first two each
taskisanindependentrepositoryorterminalscenariowitha
distinct solution, which is the long-horizon, heterogeneous-
solution regime this paper targets. The four streams contain
32, 20, 42, and 53 tasks, respectively.
Models and settings.Each run uses one of three models
as its single frozen base model for solving, extraction, and
compression: DeepSeek-V4-Pro, MiniMax-M3, and GPT-
5.4-mini, giving 12 runs. Every setting is a measurement
point inside one continual run; they differ only in what oc-
cupies the skill context.No-Skillleaves it empty and es-
tablishes the baseline.Local-onlycarries the skill the task
regeneratedfromitsownfeedbackandrecallsnothing,isolat-
ing within-task adaptation.Global-onlycarries the recalled
prior with regeneration disabled, isolating what consolida-
tion has taken from the local skills.Global+Localcarries
both. A fifth setting,Base-only, replaces the library with a
single compressed document and appears only in the abla-
tions.Allfiveareconfigurationsofourownsystem.Hardand
soft are readings of the verifier scorerx (§3.1):hardis each
benchmark’sownall-or-nothingflag.Softisthepartial-credit
signalthebenchmarkdefines,oroneofourswhereitdefines
none; on software repair it is multiplicative, so breaking a
passingtestzeroesthescore.Hardissparseonlong-horizon
tasks;softrecordsprogressshortofit.Per-benchmarkdefini-
tionsareintheappendix.RecallusesQwen3-Embedding-8B
under 4-bit quantization (Zhang et al. 2025), with a cosine-
similarity threshold of0.45across benchmarks; below it a
taskreceivesnoprior.Everymain-tablecellisasinglerunat
provider defaults (temperature0.7); seeds fix the splits and
thetaskorder.Theheld-outsoftware-repairnumbersaverage
three trials. The base models are hosted APIs; recall runs on
one GPU (16GB VRAM) with 32GB host RAM on Linux
(WSL2).
4.2 Main Results
Both GLoW settings improve on No-Skill in every one of
the 12 runs (Table 1; Wilcoxon signed-rankp= 0.000488,
the smallest value attainable atn= 12): the frozen priors
gain17.2/13.0points (hard/soft) on average, and18.0/14.6
once local regeneration is added. The gain holds up at the
software-repairend,whereeachtaskisaseparaterepository
and the two existing organizations have the least to work
with: the largest gain anywhere in Table 1, on both read-
ings, falls there (MiniMax-M3,+30.0/+27.7with regener-
ation), and DeepSeek-V4-Pro adds+25.0/+25.0, whereas
the mathematical end, whose tasks share the most procedu-
ral structure, is where two of three models gain least (+3.8
and+5.7).Thatistheorderingtheframeworkpredicts,since
familygranularitypaysoffpreciselywhereasingledocument
has no dominant procedure to summarize.
SkillOpt (Yang et al. 2026a) tests that ordering. We run
the authors’ own implementation with their internal hyper-
parameters untouched, match only the launch protocol (task
stream,trials,decoding)toours,andscoreitthroughthesame
adaptersaseveryotherrow,soallnumbersshareonesource;
its entry is the peak over training epochs, matching GLoW’s
peak-over-rounds reading (appendix). Across all 21 cells,
GLoWleadson15,SkillOpton4andtwotie.SkillOpt’sfour
are all ALFWorld, the one benchmark whose tasks share a

Base-only Local-only AWM
Bench Model(w/o families) (w/o global) (flat+recall)
TBP
DeepSeek-V4-Pro 25.1 ↓9.3 48.5↑14.1 37.5↑3.1
MiniMax-M3 46.9 ↑6.3 50.0↑9.4 34.4↓6.2
GPT-5.4-mini 34.4 ↑6.3 46.9↑18.8 40.6↑12.5
SWE
DeepSeek-V4-Pro 45.0 57.5 ↑12.5 65.0↑20.0
MiniMax-M3 30.0 ↓5.0 50.0↑15.0 30.0↓5.0
GPT-5.4-mini 30.0 ↓5.0 45.0↑10.0 40.0↑5.0
ALFWorld
DeepSeek-V4-Pro 73.8 ↑16.7 73.8↑16.7 76.2↑19.1
MiniMax-M3 78.6 ↑2.4 79.8↑3.6 85.7↑9.5
GPT-5.4-mini 50.0 ↑7.1 53.6↑10.7 45.2↑2.3
LMB
DeepSeek-V4-Pro 20.8 ↑7.6 24.5↑11.3 13.2
MiniMax-M3 18.9 ↓3.7 32.1↑9.5 24.5↑1.9
GPT-5.4-mini 15.1 14.2 ↓0.9 13.2↓1.9
Mean — 39.1 ↑2.0 48.0↑10.9 42.1↑5.0
Table2:Threealternativeskillorganizations,onthesame
12 runs.Hard score (%); a subscript gives the change over
that row’s No-Skill in Table 1, rendered as there, and a cell
withoutonedidnotmove.AWMisaflatpoolwithretrieval.
singleactionspace:whereoneskeletoncoversthewholeset,
asingledocumentisalreadytherightgranularity.Elsewhere
themarginrunstheotherway(+8.3onTBP,+6.7onSWE,
and+6.9on LMB, hard, averaged over the three models).
Onunseentaskstheprioralonecarriesthegain(appendix).
The accumulation is also achieved on a bounded library;
across the 12 runs the committed library is smaller than the
per-task skill pool by a factor of3.6.
4.3 Component Ablations
The two organizational extremes are a single merged docu-
ment (Ni et al. 2026) and a per-task entry library (Lin et al.
2026;Yangetal.2026b).Table1carriesapublishedinstance
of the first; here we place our own library at each extreme
instead, so that both ends are measured under identical con-
ditions (Table 2): Base-only compresses the whole library
intoasingleinjectedskill,andLocal-onlyusesonlytheskill
regenerated from each task’s own feedback.
Granularity (w/o families / w/o global).Removing the
procedural-family layer collapses the system to one extreme
or the other, and the two fail in opposite ways. Base-only is
theweakformofthesingle-documentorganization,onecom-
pressionpasswithnoiteration.Itaverages+2.0points,flips
sign across benchmarks (−9.3to+16.7), and loses ground
on4ofthe12cells.SkillOptisthestateoftheartforasingle
persistent document, and clears Base-only on 10 of the 12
cells(Tables1,2);thedistancebetweenthemmeasuresopti-
mizationeffortratherthanorganization.Base-onlysucceeds
consistently only on ALFWorld, for the reason §4.2 gives.
Elsewhere a merged document yields generic discipline the
model has already internalized. On software repair it never
helps: the resolved count is flat for one model and lower for
the other two, and an independent benchmark of authored
Figure 3: Mean gain over No-Skill (hard, points), 12 runs;
band is the 15th–85th percentile.Solid: what the gate ad-
mitted, held flat on a rejection.Dashed: that round’s candi-
date, admitted unconditionally. Rounds are compared inde-
pendently.
skills reports 39 of 49 leaving the pass rate unchanged (Han
et al. 2026). Per-task skills carry the opposite defect. They
help, by+10.9points, but the entry is built around the in-
stance (§4.4), and the pool grows linearly with the stream;
appending such entries without curation is known to accu-
mulatenoiseandstalenessratherthanreuse(Caoetal.2026;
Ouyang et al. 2026a), and cross-task recall over them trans-
ferslittle(Kimetal.2026).ThesettingstilltrailsGlobal-only.
Adding retrieval to that pool does not close the gap. Work-
flowsinducedinthestyleofAWM(Wangetal.2025b)from
thesamefirst-roundevidence,pooledandretrievedpertask,
average+5.0pointsacrossthe12cells,eightup,threedown
andoneflat,whileourownoneroundoffamilyconsolidation
gives+11.2(appendix).
Admission(w/ogate).Ablatingthegate(§3.4)requiresno
separatecontrolrun,asthegatealreadyevaluateseverycan-
didateunderrealdeployment,sothecostofanerroneousad-
missionismeasuredratherthansimulated(Figure3).Across
the 12 runs, the gate made 26 admission decisions, accept-
ing 19 and rejecting 7. Decisions depend on the workload
rather than the model. On terminal tasks, candidates for all
three models were admitted in both rounds; on software re-
pair,allthreewereadmittedinthefirstroundandrejectedin
the second. A cheaper criterion would not reproduce these
rejections, as 4 of the 7 would have been admitted under
the consolidation-time score alone. A representative case is
MiniMax-M3 on mathematical reasoning, whose round-2
candidate scored0.283on the soft signal the gate uses, ex-
ceeding the anchor, yet achieved only0.151in deployment
(−13.2points, more than twice the largest run-to-run range
we measure). Averaged over the 12 runs, the library the gate
kept reaches+14.7points by the final round, while that
round’s candidates average+9.6(Figure 3).
4.4 Analysis
Priors are organized by procedure.ALFWorld’s own
task labels give a partition we did not produce. Consoli-
dation returns 15 priors over 42 tasks: 13 sit wholly inside

Task class Tasks Priors Solved Fix/Break
(dataset) (skill num) (no skill→with global)
Examine-in-light 7 1 4→7↑3
Pick-and-place 7 3 7→7 —
Clean-then-place 7 3 4→5↑2↓1
Cool-then-place 7 2 5→6↑1
Heat-then-place 7 3 5→7↑2
Two-instance 7 3 7→7 —
All six classes 42 15 32→39↑8↓1
Table 3: Priors consolidated onto ALFWorld’s six canonical
taskclasses(MiniMax-M3).Theclassesarethedataset’sown
labels,producedindependentlyofouralgorithm.Solved:No-
Skill→round 2, in-sample.Fix/Break: tasks that flipped
0→1and1→0; the arrow, not the color, carries the sign.
onelabeledclass,andtwostraddleapairandarecountedby
majority type (Table 3). No class is left uncovered and none
isinvented.ThisisalsowhyBase-onlyisreliablypositiveon
thisbenchmarkalone(Table2):hereasharedskeletonexists
at the scale of the whole task set. Terminal-Bench-Pro’s 32
tasks each carry their own subject matter, yet compression
still returns ten procedure classes. Five read asbinarywork,
butthebyte-scanningpriorhelpsonlythetwoactuallysolved
byscanningrawbytes,andleavestheotherthreeuntouched.
The appendix gives the full terminal mapping.
What a prior keeps.Compression is meant to strip the
instance and retain the procedure (§3.3), and the committed
text is where that can be checked. The local skill for the
cell-phone instance ofexamine-in-lightspends 989
words on seven steps built around a memorized location ta-
ble: receptacles ranked “soft furnishings>dresser-top>
desk>drawers ...desk for desklamp, bedside/nightstand
for bedlamp.” The prior its seven-task class compresses into
spends440wordsonfoursteps,andthetableisgone.Step1
replaces it with a read: scan the initial observation for the
illuminator-class object, “do not default todesk...verify
againstthevisibleobjectlistbeforeanygo to.”Therestis
thechainthatfollows:gotothesourcereceptacleandtakethe
target without pre-examining it; carry it to the illuminator’s
receptaclewithoutexploratoryexaminecallsenroute;ter-
minate withuse <illuminator>and append nothing
after. Every pitfall in the chain guards one thing: turns spent
on probes that return no new information. That is what the
seven tasks share; which furniture holds what is regenerated
per task.
An aligned class repairs failures without memorizing
them.On Terminal-Bench-Pro (GPT-5.4-mini) the same
accounting gives 9 repairs against one pass-to-fail; ALF-
World’s counts are in Table 3, where the single regres-
sion falls inside one class and the gain concentrates where
a class had failures to repair. The three tasks fixed in
examine-in-lightare an alarm clock, a book, and a
cell phone: one prior, three different objects. The reverse
caseisequallyvisible.ThelargestfamilyputeightTerminal-
Model No-Skill Global
DeepSeek-V4-Pro 71.788.3 ↑16.7
GPT-5.4-mini 66.775.0 ↑8.3
MiniMax-M3 83.388.3 ↑5.0
Mean 73.983.9 ↑10.0
Table 4: Transfer to unseen ALFWorld tasks (hard, %; the
lastrowaveragesthethreemodels;subscriptsasinTable1).
All three models improve.
Bench-Pro tasks together, among them a debugger session,
a write-ahead-log recovery, and a logic-gate CRC32 build,
and took its name,segfault_debugging_with, from
onemember.Itspriorrepairedoneoftheeightandbrokean-
other, the onlylarge family in thestudy with no net gain.On
the same 32 tasks a second model drew ten families instead,
none larger than five. Procedure sharing is therefore a prop-
ertyofhowthefamilyisdrawnratherthanofthebenchmark.
Families are re-derived from each round’s own evidence, so
a bad grouping is not carried into the next.
4.5 Transfer to Unseen Tasks
Doesthelibrarytransfer,orhasitmemorizedthestream?We
inject the library the training stream produced, unmodified,
into 60 unseen tasks of ALFWorld valid_unseen, a split that
sharestaskcategorieswiththetrainingtasksbutnoinstances.
Allthreemodelsimprove(Table4),andthegainissmallest
for the model with the highest baseline, consistent with a
ceiling effect.
On software repair the same library lifts the resolve rate
on30unseeninstancesfrom40.0%to45.6%(MiniMax-M3,
mean of three trials), the workload where transfer should be
hardest, since every instance is a different repository. For
reference, Kim et al. (2026) report a3.7%average gain for
cross-domain memory transfer, in a setting that pools het-
erogeneousdomainsratherthanholdingoutinstancesofone
benchmark.
5 Conclusion
Neither a single global document nor a flat per-task library
survivesastreamwhosetaskseachneedadifferentsolution.
Experiments across 12 continual-improvement runs show
themissingunitistheproceduralfamily:compressthelocal
skills of each cluster into one de-instantiated prior, regener-
ate instance detail per task rather than storing it, and admit
priors only through measured execution. This recipe gains
17.2 points over No-Skill on a library3.6×smaller than
the per-task pool, and transfers unmodified to unseen tasks
(73.9%to83.9%).Transferwasshownwheretaskcategories
recur; whether a prior survives a genuine domain change re-
mainsopen.Becauseapriorisplaintext,onemodel’slibrary
could in principle be handed to another; such cross-model
inheritanceremainsuntested.Bothpointtowardalibraryany
open-endedworkflowcouldaccumulate,ratherthanonetied
to a benchmark.

References
Cao, Z.; Deng, J.; Yu, L.; Zhou, W.; Liu, Z.; Ding, B.; and
Zhao,H.2026. RememberMe,RefineMe:ADynamicPro-
cedural Memory Framework for Experience-Driven Agent
Evolution. InFindingsoftheAssociationforComputational
Linguistics: ACL 2026, 16803–16822.
Du,J.;Wu,J.;Chen,Y.;Hu,Y.;Li,B.;andZhou,J.T.2025.
Rethinking Agent Design: From Top-Down Workflows to
Bottom-Up Skill Evolution. arXiv:2505.17673.
Fang, R.; Liang, Y.; Wang, X.; Wu, J.; Qiao, S.; Xie, P.;
Huang,F.;Chen,H.;andZhang,N.2026. Memp:Exploring
Agent Procedural Memory. InFindings of the Association
for Computational Linguistics: ACL 2026, 17490–17502.
Han, T.; Zhang, Y.; Song, W.; Fang, C.; Chen, Z.; Sun,
Y.; and Hu, L. 2026. SWE-Skills-Bench: Do Agent
Skills Actually Help in Real-World Software Engineering?
arXiv:2603.15401.
He, L.; Yu, Q.; Dong, H.; Liao, B.; Xu, X.; Goldblum, M.;
Bian,J.;andMesgarani,N.2026. LiveMathematicianBench:
ALiveBenchmarkforMathematician-LevelReasoningwith
Proof Sketches. arXiv:2604.01754.
Jiang,G.;Su,Z.;Qu,X.;andFung,Y.R.2026. XSkill:Con-
tinual Learning from Experience and Skills in Multimodal
Agents. InInternational Conference on Machine Learning.
Jimenez, C. E.; Yang, J.; Wettig, A.; Yao, S.; Pei, K.; Press,
O.; and Narasimhan, K. 2024. SWE-bench: Can Language
ModelsResolveReal-WorldGitHubIssues? InInternational
Conference on Learning Representations (ICLR).
Kang, M.; Chen, W.-N.; Han, D.; Inan, H. A.; Wutschitz,
L.; Chen, Y.; Sim, R.; and Rajmohan, S. 2026. ACON:
Optimizing Context Compression for Long-horizon LLM
Agents. InInternational Conference on Machine Learning.
Khattab, O.; Singhvi, A.; Maheshwari, P.; Zhang, Z.; San-
thanam, K.; Vardhamanan, S.; Haq, S.; Sharma, A.; Joshi,
T. T.; Moazam, H.; Miller, H.; Zaharia, M.; and Potts, C.
2024. DSPy: Compiling Declarative Language Model Calls
into Self-Improving Pipelines. InInternational Conference
on Learning Representations.
Kim, K.; Kang, M.; Kim, T.; Yang, Y.; Ren, M.; and
Hwang, S. J. 2026. Memory Transfer Learning: How Mem-
ories are Transferred Across Domains in Coding Agents.
arXiv:2604.14004.
Li, X.; Chen, W.; Liu, Y.; Zheng, S.; Chen, X.; et al. 2026a.
SkillsBench: Benchmarking How Well Agent Skills Work
Across Diverse Tasks. arXiv:2602.12670v1.
Li, X.; Li, M.; Bao, K.; Ma, Y.; Wang, W.; Liu, D.;
and Feng, F. 2026b. SkillGraph: Skill-Augmented Rein-
forcement Learning for Agents via Evolving Skill Graphs.
arXiv:2605.12039.
Lin,H.;Li,P.;Song,J.;Jiang,F.;andZhang,T.2026.MUSE-
Autoskill:Self-EvolvingAgentsviaSkillCreation,Memory,
Management, and Evaluation. arXiv:2605.27366.
Liu, X.; Yu, H.; Zhang, H.; Xu, Y.; Lei, X.; Lai, H.; Gu, Y.;
Ding, H.; Men, K.; Yang, K.; Zhang, S.; Deng, X.; Zeng,
A.; Du, Z.; Zhang, C.; Shen, S.; Zhang, T.; Su, Y.; Sun,
H.; Huang, M.; Dong, Y.; and Tang, J. 2024. AgentBench:
EvaluatingLLMsasAgents. InInternationalConferenceon
Learning Representations (ICLR).
Madaan, A.; Tandon, N.; Gupta, P.; Hallinan, S.; Gao, L.;
Wiegreffe, S.; Alon, U.; Dziri, N.; Prabhumoye, S.; Yang,
Y.; Gupta, S.; Majumder, B. P.; Hermann, K.; Welleck, S.;
Yazdanbakhsh, A.; and Clark, P. 2023. Self-Refine: Itera-
tive Refinement with Self-Feedback. InAdvances in Neu-
ral Information Processing Systems (NeurIPS), volume 36,
46534–46594.
Merrill, M. A.; Shaw, A. G.; Carlini, N.; Li, B.; Raj, H.;
Bercovich, I.; Shi, L.; Shin, J. Y.; Walshe, T.; Buchanan,
E. K.; Shen, J.; Ye, G.; Lin, H.; Poulos, J.; Wang, M.;
et al. 2026. Terminal-Bench: Benchmarking Agents on
Hard,RealisticTasksinCommandLineInterfaces. InInter-
national Conference on Learning Representations (ICLR).
ArXiv:2601.11868.
Mialon, G.; Fourrier, C.; Swift, C.; Wolf, T.; LeCun, Y.;
and Scialom, T. 2024. GAIA: A Benchmark for General AI
Assistants. InInternational Conference on Learning Repre-
sentations (ICLR).
Monti,S.;Tamayo,P.;Mesirov,J.;andGolub,T.2003. Con-
sensus Clustering: A Resampling-Based Method for Class
DiscoveryandVisualizationofGeneExpressionMicroarray
Data.Machine Learning, 52: 91–118.
Ni, J.; Liu, Y.; Liu, X.; Sun, Y.; Zhou, M.; Cheng, P.; Wang,
D.;Zhao,E.;Jiang,X.;andJiang,G.2026. Trace2Skill:Dis-
till Trajectory-Local Lessons into Transferable Agent Skills.
arXiv:2603.25158.
Ouyang, S.; Yan, J.; Chen, Y.; Han, R.; Wang, Z.;
Dalvi Mishra, B.; Meng, R.; Li, C.-L.; Jiao, Y.; Zha, K.;
Shen, M.; Tirumalashetty, V.; Lee, G.; Han, J.; Pfister, T.;
and Lee, C.-Y. 2026a. SkillOS: Learning Skill Curation for
Self-Evolving Agents. arXiv:2605.06614.
Ouyang,S.;Yan,J.;Hsu,I.-H.;Chen,Y.;Jiang,K.;Wang,Z.;
Han, R.; Le, L. T.; Daruki, S.; Tang, X.; Tirumalashetty, V.;
Lee, G.; Rofouei, M.; Lin, H.; Han, J.; Lee, C.-Y.; and Pfis-
ter, T. 2026b. ReasoningBank: Scaling Agent Self-Evolving
with Reasoning Memory. InInternational Conference on
Learning Representations.
Pan, S.; Liu, Y.; Gao, J.; Gao, T.; Liu, W.; Lin, J.; Fu,
Z.; Wang, J.; Zhang, W.; and Yu, Y. 2026. SkillMAS:
Skill Co-Evolution with LLM-based Multi-Agent System.
arXiv:2605.09341.
Reimers, N.; and Gurevych, I. 2019. Sentence-BERT: Sen-
tenceEmbeddingsUsingSiameseBERT-Networks. InCon-
ferenceonEmpiricalMethodsinNaturalLanguageProcess-
ing (EMNLP-IJCNLP), 3982–3992.
Rousseeuw, P. J. 1987. Silhouettes: A Graphical Aid to the
InterpretationandValidationofClusterAnalysis.Journalof
Computational and Applied Mathematics, 20: 53–65.
Satopää, V.; Albrecht, J.; Irwin, D.; and Raghavan, B. 2011.
Finding a “Kneedle” in a Haystack: Detecting Knee Points
in System Behavior. In31st International Conference on
DistributedComputingSystemsWorkshops(ICDCSW),166–
171.
Schick, T.; Dwivedi-Yu, J.; Dessì, R.; Raileanu, R.; Lomeli,
M.;Hambro,E.;Zettlemoyer,L.;Cancedda,N.;andScialom,

T. 2023. Toolformer: Language Models Can Teach Them-
selves to Use Tools. InAdvances in Neural Information
Processing Systems, volume 36, 68539–68551.
Shinn, N.; Cassano, F.; Gopinath, A.; Narasimhan, K.; and
Yao, S. 2023. Reflexion: Language Agents with Verbal Re-
inforcement Learning. InAdvances in Neural Information
Processing Systems (NeurIPS), volume 36, 8634–8652.
Shridhar, M.; Yuan, X.; Côté, M.-A.; Bisk, Y.; Trischler, A.;
and Hausknecht, M. 2021. ALFWorld: Aligning Text and
Embodied Environments for Interactive Learning. InInter-
national Conference on Learning Representations (ICLR).
Suzgun,M.;Yuksekgonul,M.;Bianchi,F.;Jurafsky,D.;and
Zou,J.2025. DynamicCheatsheet:Test-TimeLearningwith
Adaptive Memory. arXiv:2504.07952.
Tang, X.; Qin, T.; Peng, T.; Zhou, Z.; Shao, D.; Du, T.;
Wei, X.; Xia, P.; Wu, F.; Zhu, H.; Zhang, G.; Liu, J.; Wang,
X.; Hong, S.; Wu, C.; Cheng, H.; Wang, C.; and Zhou, W.
2025. Agent KB: Leveraging Cross-Domain Experience for
Agentic Problem Solving. arXiv:2507.06229.
Wang, G.; Xie, Y.; Jiang, Y.; Mandlekar, A.; Xiao, C.;
Zhu, Y.; Fan, L.; and Anandkumar, A. 2023. Voyager: An
Open-EndedEmbodiedAgentwithLargeLanguageModels.
arXiv:2305.16291.
Wang, W.; Xu, X.; An, W.; Dai, F.; Gao, W.; et al. 2025a.
LetItFlow:AgenticCraftingonRockandRoll,Buildingthe
ROMEModelwithinanOpenAgenticLearningEcosystem.
arXiv:2512.24873.
Wang, Z. Z.; Mao, J.; Fried, D.; and Neubig, G. 2025b.
Agent Workflow Memory. InProceedings of the 42nd In-
ternational Conference on Machine Learning, volume 267,
63897–63911.
Ward, J. H., Jr. 1963. Hierarchical Grouping to Optimize
an Objective Function.Journal of the American Statistical
Association, 58(301): 236–244.
Yang, C.; Wang, X.; Lu, Y.; Liu, H.; Le, Q. V.; Zhou, D.;
andChen,X.2024a. LargeLanguageModelsasOptimizers.
InInternational Conference on Learning Representations
(ICLR).
Yang, J.; Jimenez, C. E.; Wettig, A.; Lieret, K.; Yao, S.;
Narasimhan, K.; and Press, O. 2024b. SWE-agent: Agent-
Computer Interfaces Enable Automated Software Engineer-
ing. InAdvances in Neural Information Processing Systems
(NeurIPS), volume 37, 50528–50652.
Yang, Y.; Gong, Z.; Huang, W.; Yang, Q.; Zhou, Z.; Huang,
Z.; Li, Y.; Gao, X.; Dai, Q.; Liu, B.; Qiu, K.; Yang, Y.;
Chen, D.; Yang, X.; and Luo, C. 2026a. SkillOpt: Executive
Strategy for Self-Evolving Agent Skills. arXiv:2605.23904.
Yang, Y.; Li, J.; Pan, Q.; Zhan, B.; Cai, Y.; Du, L.; Zhou,
J.; Chen, K.; Chen, Q.; Li, X.; Zhang, B.; and He, L. 2026b.
AutoSkill: Experience-Driven Lifelong Learning via Skill
Self-Evolution. arXiv:2603.01145.
Yao, S.; Zhao, J.; Yu, D.; Du, N.; Shafran, I.; Narasimhan,
K.; and Cao, Y. 2023. ReAct: Synergizing Reasoning and
ActinginLanguageModels. InInternationalConferenceon
Learning Representations (ICLR).
Yuksekgonul, M.; Bianchi, F.; Boen, J.; Liu, S.; Lu, P.;
Huang, Z.; Guestrin,C.; and Zou, J.2025. OptimizingGen-
erative AI by Backpropagating Language Model Feedback.
Nature, 639(8055): 609–616.
Zhang, Y.; Li, M.; Long, D.; Zhang, X.; Lin, H.; Yang, B.;
Xie, P.; Yang, A.; Liu, D.; Lin, J.; Huang, F.; and Zhou, J.
2025. Qwen3 Embedding: Advancing Text Embedding and
RerankingThroughFoundationModels. arXiv:2506.05176.
Zhang, Z.; Shi, K.; Huang, S.; Nie, A.; Zeng, Y.; Zhao,
Y.; Fang, Z.; Su, Q.; Qiu, H.; Yang, W.; Ren, Q.; Zou, S.;
Huang,W.;Chen,L.;Chen,Z.;andZhao,F.2026.SkillFlow:
Benchmarking Lifelong Skill Discovery and Evolution for
Autonomous Agents. arXiv:2604.17308.
Zhao,A.;Huang,D.;Xu,Q.;Lin,M.;Liu,Y.-J.;andHuang,
G.2024. ExpeL:LLMAgentsAreExperientialLearners. In
AAAI Conference on Artificial Intelligence (AAAI).
Zheng, B.; Fatemi, M. Y.; Jin, X.; Wang, Z. Z.; Gandhi, A.;
Song, Y.; Gu, Y.; Srinivasa, J.; Liu, G.; Neubig, G.; and Su,
Y. 2025. SkillWeaver: Web Agents Can Self-Improve by
Discovering and Honing Skills. arXiv:2504.07079.
Zhou, H.; Chen, Y.; Guo, S.; Yan, X.; Lee, K. H.; Wang,
Z.; Lee, K. Y.; Zhang, G.; Shao, K.; Yang, L.; and Wang,
J. 2025. Memento: Fine-tuning LLM Agents without Fine-
tuning LLMs. arXiv:2508.16153.
Zhou,H.;Guo,S.;Liu,A.;Yu,Z.;Gong,Z.;Zhao,B.;Chen,
Z.; Zhang, M.; Chen, Y.; Li, J.; Yang, R.; Liu, Q.; Yu, X.;
Zhou,J.;Wang,N.;Sun,C.;andWang,J.2026a. Memento-
Skills: Let Agents Design Agents. arXiv:2603.18743.
Zhou, Y.; Wang, S.; Su, Y.; Du, W.; Fang, Y.; and Lin, X.
2026b.AComprehensiveSurveyonAgentSkills:Taxonomy,
Techniques, and Applications. arXiv:2605.07358.

This document supplies the material the paper defers to.
Sectionletters(§§A–O),tables(TablesA1–A28)andfigures
(Figures A1–A3) are local to this document; a table, figure,
equation or §-number without a letter points into the main
paper. Reviewers are not obliged to consult this document,
and the paper is self-contained without it. The method is
SkillGLoWin the title andGLoWfor short throughout.
A Metric Definitions
Thehardmetric is the all-or-nothing flag the benchmark
ships with. Thesoftmetric is the benchmark’s own contin-
uous partial credit; ALFWorld has no official partial credit,
so its soft score is derived by our verifier.
Benchmark hard soft
Terminal-Bench-
Pro
allpytest
tests pass
thefractionofpytesttests
passed;shipswiththebench-
mark
SWE-bench Veri-
fied
binary
resolved
a multiplicative gate on the
fail-to-pass and pass-to-pass
rates
ALFWorld binary suc-
cess flag
the larger of the subgoal
completion ratio and the
TextWorld intermediate re-
ward; derived here
Live-
Mathematician-
Bench
binary multi-
ple choice
≡hard
Table A1: hard and soft, one benchmark at a time.
Table A1 gives them one benchmark at a time. SWE’s soft
is a multiplicative gate: if either side is zero the soft score is
zero,sobreakingatestthatusedtopassisneverrecordedas
partial success.
Thefoursoftmetricsliveondifferentscales,sotheAvg.soft
column of Table 1 averages across read-outs and should be
read only as relative movement across settings within one
row; the per-benchmark columns are the comparable ones.
The hard columns are unaffected.
Thecommitgaterunsonsoftwhiletheheadlinereportshard.
InV(G;D) = 1 |D| P x rx of §3.4,r x is each benchmark’s
soft. On long-horizon tasks hard is too sparse — the four
benchmarks’ No-Skill hard lies between 13.2% and 76.2%
— and using it as the gate signal would frequently give the
wrong verdict, because a single task flipping can decide it.
Accordingly the two scores in §4.3, candidate0.283against
deployed0.151, are both soft.
B Multi-View Fusion and Consensus
Clustering
Each local skill card is encoded as up to five view vectors;
eachisL 2-normalisedandtheweightedsumgivesϕ(c).The
body describes four views, with the signature taking two of
them — one compact and one verbose granularity, encoded
separately.
Channel Content
S Signature, compact the 2–5-word abstract operation
name
L Signature, verbose a 10–15 word description of the
procedure
I Task instruction the task text as given
T Trajectory text the goal and actions of the execu-
tion plan and the checks and ob-
servations of the plan trace,≈500
characters
F Full local skill the skill description concatenated
with every section, truncated at
8000 characters
Table A2: The five view channels.
The five channels are listed in Table A2. The tier is decided
at run time by which fields the round’s cards actually carry,
and the twelve runs trigger only the two tiers of Table A3.
Tier Trigger S L I T F
Five-view any card carries a
trajectory
0.30 0.20 0.20 0.20 0.10
Four-view no trajectory, full
skill present
0.25 0.25 0.25 — 0.25
Table A3: The two weight tiers actually deployed. A dash
means the channel is absent in that tier.
The sweep behind the four-view values is Table A4. Both
tiers share the property that the signature channels together
carry the most weight, 0.50 in each, and the full skill text
theleast—consistentwiththebody’s“groupingfollowsthe
procedure rather than either wording”. A missing channel
falls back to that card’s task instruction; the weights there-
fore still sum to one. Across rounds the vectors accumulate
under an exponential moving average withα= 0.2. Both
tiers’ weights are hard-coded constants, unadjusted across
four benchmarks and three models.
The five-view tier is the global optimum of one five-view
gridsweepatstep0.1.Thefour-viewequalweightingcomes
from a separate sweep at the same granularity, scored by
ARI against the dataset’s labels; the parenthesised value is
the number of clusters selected automatically.
Weights S/L/I/F ALFWorld ARI Second domain Mean
0.40 / 0.40 / 0.20 / — 0.799 (6) 0.557 (15) 0.678
0.40 / 0.20 / 0.20 / 0.20 0.799 (6) 0.520 (6) 0.660
0.30 / 0.20 / 0.20 / 0.30 0.799 (6) 0.690 (13) 0.745
0.30 / 0.30 / 0.10 / 0.30 0.799 (6) 0.671 (11) 0.735
0.25 / 0.25 / 0.25 / 0.25 0.878 (7) 0.733 (16) 0.806
0.50 / 0.20 / 0.10 / 0.20 0.799 (6) 0.448 (17) 0.624
— / 0.40 / 0.20 / 0.40 0.775 (6) 0.592 (21) 0.684

Table A4: The four-view weight sweep. The second domain
is a spreadsheet-manipulation benchmark and is not one of
ourfour;ofthose,onlyALFWorldtookpartinthisselection,
and the other three inherited the result directly.
The cosine similarity matrixSis min-max normalised to
[0,1]and the distance isD= 1−S. There are nine base
partitions: average and complete linkage onD, and Ward
linkage onS, each run forK∈ {K 0 −1, K0, K0 + 1},
whereK 0 is a seed value from a first pass. The consensus
matrix is the co-assignment frequency
COij = 1 9
9X
p=1
1

ℓp(i) =ℓ p(j)

,(6)
and the final families come from one more average-linkage
clustering on1−CO.
KistheKneedlekneeofthesilhouettecurve,searchedover
K∈[3,min(n−1,⌊n/2⌋+ 2)]: both axes are normalised
and theKwith the largest perpendicular distance from the
chord joining the endpoints is taken. The criterion has no
tunable parameter and prefers fewer clusters than a plain
argmax. TheKvalues in §N.1 are produced this way.
C Run Protocol of the Compared Methods
C.1 SkillOpt
The SkillOpt row of Table 1 comes from the official imple-
mentation,microsoft/SkillOpt, not from a reimple-
mentation of our own. Apart from the alignments below, its
internal hyperparameters are the authors’ defaults: learning
rate 4, minibatch 8, four epochs, batch 40, with the skill
length budget and all prompts untouched.
Aligned
item
Our reference run SkillOpt base-
line
Task set train 53/42/32/20 the same batch
Model one model does solving,
extraction and compres-
sion
same
Trials per
task
1 1
thinking off for LMB, on for the
other three
same
Maxinterac-
tion turns
5/30/15/25 same
Scoring our evaluation adapter same
Table A5: Item-by-item alignment between our reference
runs and the SkillOpt baseline. Every item that could move
the comparison — task set, base model, trials per task,
thinking, turn limit and scoring — is held identical. Two
further items — the initial skill and the optimiser model
— are not listed in the table and are settled in the text
below. Every slash-separated quadruple is in the order
LMB/ALFWorld/TBP/SWE.
Table A5 lists the alignment item by item, and the two it
leaves to the text are settled the same way on both sides —
each departs from SkillOpt’s official default, and each does
sointhedirectionthatremovesanasymmetryratherthanone
that creates one. The official release provides hand-written
initial skills for LMB and ALFWorld only. Keeping them
would leave the four benchmarks at different starting points
and would mix the contribution of the human prior into the
same number as the optimisation loop, so all four use one
neutral99-byteskeletonandthegainisattributableentirelyto
theoptimisationloop.Thatchoicewasverified:onMiniMax-
M3×ALFWorldtheblankstartandtheofficialhand-written
skill give digit-for-digit identical weighted scores across all
three epochs, so the hand-written document’s net contribu-
tioninthatcellis0.0ppandthe+19.0ppisproducedbythe
optimisation loop.
The original method allows the optimiser to be a stronger
model distilling into the target model. Our own pipeline has
nosuchchannel—onefrozenmodeldoessolving,extraction
and compression — so we switch it off on SkillOpt too,
putting optimiser and solver on the same base model. What
remains is a comparison between two ways of organising
skills for one and the same model, with no distillation on
either side.
All four benchmarks go through our evaluation adapter, so
hardandsoftcarrythesamemeaningasineveryothertable.
SkillOpt’s native environments cover only ALFWorld and
LMB,andthoseenvironments’read-outsarenotcomparable
withours:nativeALFWorldhard-codessoftas1onsuccess,
and native LMB brings its own prompt and choice shuffling
and returns0.077on the same 53 tasks where our No-Skill
baseline is0.226. Once both sides go through our adapter,
SkillOpt’s score on that benchmark is higher than its own
native environment can produce.
SkillOpt splits each epoch into a 40-task batch and a re-
mainder batch, so a full pass exists only after merging an
epoch’s batches with weights; the figure in the body is that
epoch-weighted merged train peak.
C.2 AWM
AWM induces, from experience, workflows that are shared
acrosstasks,andisconceptuallytheclosestroutetoaproce-
dural family prior. It is the AWM column of Table 2.
We use the offline setting (Wang et al., arXiv:2409.07429):
given a batch of already-attempted tasks, one LLM call ex-
tracts the sub-procedures that recur across them as work-
flows, and the result is prepended whole to the agent’s
prompt. The official repository ships only WebArena and
Mind2Webbranches,butthemethodcarriesnoweb-specific
assumption.Twodecisionswereneededfortheport.Thein-
duction instruction is used verbatim from the official repos-
itory, read from it at run time. The one-shot example, by
contrast,isreplacedbyoneofthesamestructuredrawnfrom
the target benchmark’s own action vocabulary, because the
official 138 lines of WebArena click actions would push the
model to write click-shaped workflows for an environment
that has no clicking.
ThetrajectoriesthatinductionusesarerolloutsundertheNo-
Skillcondition:thefirststepofaSkillOptrunstartedfroma
blank skill, taken before the optimiser has made any update
andwithanemptyskilldocument.Thatisthesamecondition
the No-Skill row of Table 1 reports, so AWM induces from

the same experience every arm starts out from, and from
nothing our method produced.
Retrieval follows the official implementation and is global.
Every test task queries the index, but the results are pooled
rather than kept per task, and the top-kare written into one
filethatistheninjectedwholeandidenticallyintoeverytask.
Embedding follows the officialtext-embedding-ada-
002.Theoneknobnotinheritedistop-k,setto3ratherthan
theofficialdefaultof10.ThechangeisinAWM’sfavour:the
induced libraries here hold roughly 4 to 30 entries per cell,
so the official value would have degenerated retrieval into
whole-library injection and removed the retrieval step the
method depends on. At deployment the workflow document
is injected as the initial skill, with one epoch and a single
batch covering the whole task stream.
AWM hard AWM soft
Model Benchnvalue∆value∆
MiniMax-M3
ALFWorld 42 85.7↑9.5 93.7↑3.2
TBP 32 34.4↓6.2 75.1↓2.0
SWE 20 30.0↓5.0 34.9↓4.9
LMB 53 24.5↑1.9 24.5↑1.9
DeepSeek-V4-Pro
ALFWorld 42 76.2↑19.185.7↑17.8
TBP 32 37.5↑3.1 70.4↑1.5
SWE 20 65.0↑20.067.5↑20.0
LMB 53 13.2 — 13.2 —
GPT-5.4-mini
ALFWorld 42 45.2↑2.3 61.1↑0.2
TBP 32 40.6↑12.5 78.3↑2.7
SWE 20 40.0↑5.0 45.8↑8.4
LMB 53 13.2↓1.9 13.2↓1.9
Mean 42.1↑5.0↑3.9
TableA6:AWMacrossalltwelvecells.∆isagainstNo-Skill
in the same cell of Table 1, on the same scale as Table 2 —
median↑2.7 and↑1.7, eight up, one flat, three down. As
there,thearrowandnotthecolourcarriesthesign,andacell
with no∆did not move.
Table A6 gives every cell. Across the twelve cells AWM
averages+5.0with a per-cell range from−6.2to+20.0.
GLoW’sGlobalarmonthesametwelvecellsis12/12same-
signed with a mean of+17.2.
Three differences correspond to our mechanism. AWM in-
duces over the task set as a whole without first forming fam-
ilies. That shows up most clearly on LMB, the benchmark
withthefewestmergeabletasks:thethreemodelsgive+1.9,
0.0and−1.9,ameanofzero,against+24.5,+5.7and+3.8
for GLoW’s Global arm in the same cells. Its induced work-
flows enter reuse with no admission step grounded in real
execution, whereas the margins of the candidates rejected
in §D.3 lie between−0.05and−0.13. And after retrieval
it injects one identical document into every task, whereas
GLoW’s Recall is per task.
The body compares “one round of family consolidation”
against AWM’s+5.0; that figure is the round-0 committed
library’srealdeploymentscoreinthefirstsub-roundofround
1,minusthesamecell’sNo-Skill,onhard,averagedoverthe
twelve cells.
D Statistical Tests
D.1 Paired Tests Across Runs
The twelve cells of the main table are paired measurements
on the same tasks under the same harness. The per-cell dif-
ferences of the Global arm, in percentage points:
Model TBP SWE ALFWorld LMB
DeepSeek-V4-Pro+15.6 +25.0 +26.2 +24.5
MiniMax-M3+12.5 +25.0 +16.7 + 5.7
GPT-5.4-mini+21.9 +10.0 +19.0 + 3.8
Table A7: Per-cell difference of the Global arm against No-
Skill (hard, pp).
Test Statistic Two-sidedp
Sign test 12/12 positive0.000488
Wilcoxon signed-rankW − = 0,n= 120.000488
Table A8: Paired tests over the twelve runs.
The two paired tests are Table A8. The Global+Local arm
is likewise 12/12 positive, with a mean of+18.0pp and the
same statistics. When every difference has the same sign the
two tests collapse top= 2/212, the smallestpattainable at
n= 12. The significance is established at the level of the
twelve runs; per-cell resolution is in §J.2.
D.2 What the Peak Read-out Is Taken Over
The main table reports a peak across rounds, and the range
that peak is taken over is restricted. GLoW’s best-across-
rounds is taken only among libraries that passed the com-
mit gate and were actually deployed, never among candidate
versions: a candidate that scores higher but is rejected by
the gate does not enter the pool. The solid line of Figure 3
is that deployed trajectory and the dashed line is the same
round’scandidate;inthelastroundtheyare+14.7ppagainst
+9.6pp,sotheretainedolderlibraryis5.1ppabovethenew
candidate.
The compared side is on the same scale. The SkillOpt row
takes the epoch-weighted merged train peak; like GLoW’s
peakacrossrounds,itisamaximumalongitsownoptimisa-
tion axis.
D.3 Gate Decisions and the Tolerance
Din Eq. (5) is the training task stream itself; held-out eval-
uation enters no gate decision. Both terms of the anchor
A= max(V ⋆, Vns)can be read off the supplementary ma-
terial:V ⋆ is the real deployment score of the last committed
round, recorded in each run’s library state, andVns is that
cell’s no-skill baseline, kept in a file of its own. In the first
roundthereisnocommittedroundyet,sotheanchorreduces
to the baseline.
Candidates are adjudicated late: the candidate of roundk
is decided by the first real deployment of roundk+1. The

direct consequence of that discipline is that every prior in
the library carries the evidence of one real deployment, and
a candidate that was never adjudicated enters none of the
libraries reported in this paper.
ϵ= 0.02did change outcomes.Two candidates scored be-
lowtheanchorbutfellinsidethetoleranceband,withmargins
of−0.0108and−0.0181on the soft scale — that is,−1.08
and−1.81percentagepoints—bothonTBP,andbothwere
admitted; atϵ= 0both would have been rejected. Both are
smaller than the 2.71pp reproduction standard deviation of
repeated measurement (§J.1), so what the tolerance absorbs
isadipofthesizeofthenoiseratherthanarealdegradation
— which is the setting §3.4 describes as “ϵabsorbs fluctu-
ation”. The rejected candidates’ margins lie between−0.05
and−0.13, i.e.−5to−13percentage points, far outside the
tolerance ofϵ= 0.02(2pp), andϵ= 0would not change
those decisions.
The gate includes equality, so a tie passes. That is a design
choice, not a conclusion we verify. The reason for admitting
atieisthatonceapriorisinthelibrarythenextroundsolves
ontopofitandlocalskillsareextractedfromthosesolutions,
so a candidate that merely holds level can still change what
the following round produces. Whether that helps or hurts
on balance was not tested.
E Library-Size Accounting
The compression ratio compares that run’s last-round com-
mitted global priors against the pool of local skills, one per
task,fromthesameround.Theentryratiocountsentries;the
wordratiosumswordcountsonbothsides.Thedenominator
takes only the final state of the local skills, not the per-sub-
roundintermediatesnapshots:onALFWorld,countingthose
too would give42 + 3×42 = 168entries in place of 42,
inflating the denominator fourfold.
Entries Words
Benchmark Model
priors local tasks
expected
entry
ratio
prior local word
ratio
TBP
DeepSeek-V4-Pro 16 31 32 0.516 11955 32335 0.370
MiniMax-M3 10 32 32 0.312 8700 53778 0.162
GPT-5.4-mini 11 32 32 0.344 8067 36089 0.224
SWE
DeepSeek-V4-Pro 8 20 20 0.400 5741 16251 0.353
MiniMax-M3 8 20 20 0.400 7589 21658 0.350
GPT-5.4-mini 6 20 20 0.300 4434 9900 0.448
ALFWorld
DeepSeek-V4-Pro 15 42 42 0.357 10876 36212 0.300
MiniMax-M3 16 42 42 0.381 15204 57912 0.263
GPT-5.4-mini 12 42 42 0.286 7801 36059 0.216
LMB
DeepSeek-V4-Pro 13 53 53 0.245 9123 28546 0.320
MiniMax-M3 6 53 53 0.113 5104 25708 0.199
GPT-5.4-mini 3 53 53 0.057 692 5266 0.131
Table A9: All twelve cells at the last round. Lower is more
compression.
All twelve cells Entries Words
ratio1/ratio ratio1/ratio
round 1 0.299×3.35×0.278×3.60×
round 2, last0.309×3.23×0.278×3.60×
Table A10: Summary over both rounds and both read-outs.
Table A9 gives every cell and Table A10 the summary; all
four combinations of read-out land between0.28and0.31.
The body takes the reciprocal of the last round’s word ratio
andstatesituniformlyas3.6×compression.Ofthethreeag-
gregationsavailable,thebodyreportstheoneleastfavourable
to us: pooling the word counts on both sides before dividing
gives3.8×, and the mean of the per-cell reciprocals gives
4.1×.
F Held-Out Transfer Results
F.1 ALFWorld Held-Out
§4.2,“Onunseentaskstheprioralonecarriesthegain”,refers
totheGlobalcolumnofTable4:thefrozenconsolidatedprior
injectedonitsown,withnolocalregeneration.Thethreerows
come from the runs below, all on the 60-task official unseen
split at a single trial.
Model No-Skill Global Runs
DeepSeek-V4-Pro 71.788.3heldout_alf60_ds_t1_
noskill_0722/..._t1_
global_0722
GPT-5.4-mini 66.775.0heldout_alf60_gpt_
t1_noskill_0722/..._
globalR1_0723
MiniMax-M3 83.388.3heldout_alf60_m3_t1_
noskill_0722b/..._t1_
global_0722b
Mean 73.983.9
Table A11: ALFWorld held-out, 60 unseen tasks, hard (%).
All three models move the same way, and MiniMax-M3,
which starts highest, gains least — consistent with a ceiling
effect. The library received no modification of any kind for
the unseen tasks: what is injected is the version committed
on the training stream.
F.2 SWE Held-Out
The body’s40.0→45.6comes from the matched pair of
three-trial runs named in the table below, each reported as
the mean resolve rate over its three trials. The benchmark
is SWE’s 30-task held-out split, disjoint from train20; the
model is MiniMax-M3.
Run trials priors resolve rate
heldout_swe30_noskill_
m3_0709
3 00.4000
heldout_swe30_global_
round0_m3_0709
3 50.4556

Table A12: The pair of runs behind the+5.6pp.
G What the Committed Priors Contain
G.1 Agreement With the Dataset’s Labels
Of the four benchmarks only ALFWorld carries solution-
typelabelsindependentofouralgorithm,seventasksineach
of six types.
RoundKpurity ARI NMI
single-type
families
clustered
tasks
round 2 150.9500.605 0.801 13/15 40
Table A13: Agreement between our families and ALF-
World’s six canonical task types.
Table A13 gives the agreement scores. Purity is high while
ARIismiddling,andthegapcomesfromover-segmentation
rather than from mixing types.K= 15against 6 types, and
ARI penalises splitting one type, and splitting is exactly the
design intent: families are finer-grained than task types. The
high purity is not bought with fragmentation either — 5 of
the15familiesaresingletons,andremovingthemleavesthe
remaining 35 tasks still at a purity of 0.943.
Two families cut across the dataset’s goal taxonomy along
a shared procedure. The quotations are the procedure sum-
maries written by the compression stage.
Cross-cutting
family
Member
type
Procedure summary Shared pro-
cedure
household_
pick-and-
place:_
locate
pick_
and_
place
“locate egg on surfaces,open
fridge, move object to inte-
rior compartment”
place into a
closed con-
tainer
pick_
two
“Glassbottle placement into
closed fridge via single-
carry open-before-place
gate”
household_
object_
pick-cool-
place
pick_
cool
“locate item,cool via appli-
ance, depositat target recep-
tacle”
deposit after
an appliance
transform
pick_
heat
“locate, pick up,heat via ap-
pliance,placeintargetrecep-
tacle”
Table A14: The dataset’s six types are divided by goal, and
both cross-cuts fall where the goals differ and the procedure
doesnot.Thesecondistheclearercase:bothtasksareanEgg,
onecooledandthenplacedinthemicrowave,theotherheated
and then placed in the fridge — appliance and receptacle
swapped, procedural skeleton identical.
G.2 The Family Mapping for the Terminal
Benchmark
The mapping §4.4 points at: TBP×GPT-5.4-mini, round 2
against the round-0 baseline, hard, paired task by task.
Familynbase→r2 fixed broken
postgresql_
recovery_
sanitization
5 1→3↑2 —
flooded-grid_
escape_planning
5 4→4↑1↓1
stripped_binary_
feature-flag
5 0→2↑2 —
two-dimensional_
gaussian_mixture
4 2→2 — —
csv-to-json_
organizational_
merge
3 0→1↑1 —
latex_document_
build
3 1→3↑2 —
shellcode_network_
tracing
2 1→1 — —
user_profile_grpc2 0→0 — —
apache_virtual_
host
2 0→1↑1 —
distributed_
tensor-parallel_
matrix
1 0→0 — —
Ten families 32 9→17↑9↓1
Table A15: The full terminal mapping: ten families over
32 tasks, nine repairs against one break — §4.4, “9 repairs
againstonepass-to-fail”.Adashmeansnotaskmovedinthat
direction.
ThemappingisTableA15,andthesplitinsideonefamilyis
TableA16.Thematchhappensattheprocedurelevel:allfive
tasksinstripped_binary_feature-flagareabout
binaries by subject, but they split on whether the solving
procedurereallyoperatesatthebytelevel.Thatfamily’sprior
opens with “Scan repeated markers”, followed by validating
a candidate manifest and decrypting bitmaps.
Member task Actual solving proce-
dure
matches the
family priorno-skill round 2
detect-c-
feature-
flags
reverse the ELF, vali-
datethemanifest,decrypt
bitmaps
✓0PASS
implement-
lz77-file-
compressor
scanrawbytesforgreedy
longest-match packing
✓0PASS
implement-
crc32-with-
logic-gates
synthesise a logic-gate
netlist
0 fail
recover-
stream-
cipher-key
brute-force the keystream
mathematically
0 fail
regex-
bitcoin-
p2pkh-
extraction
construct a regular ex-
pression
0 fail

Table A16: The prior’s procedure is scanning for markers
and parsing fields, and it repaired only the two tasks that
really do work at the byte level. The test does not depend on
clustering quality: both input columns are facts external to
the algorithm — each task’s real solution is read from the
trajectory, and whether it passed is decided by the verifier.
G.3 Excerpts of Prior Text
Three excerpts, ordered by how much the family actually
shares, from least to most.
The least shared comes from a DeepSeek run on a 16-task
TBP split whose families were formed by pre-partitioning
the tasks by domain; that run isnotone of the twelve in the
maintable.Itsdebuggingfamilypriorrunsto500wordsand
describes itself as
Establish baseline execution, gather direct runtime evidence,
and report conclusions conservatively.
The merge note the compressor wrote for itself is “These 2
tasks span unrelated domains andshare only generic en-
gineering discipline”. The notes of the same run’s security
and machine-learning family priors likewise record that no
shared algorithm was found; the three are 500, 426 and 384
words.Thisisdirectevidencefor§4.3,“amergeddocument
yieldsgenericdisciplinethemodelhasalreadyinternalized”.
A finer family comes from round 2 of TBP×GPT-5.4-mini
—thepriorofthestripped_binary_feature-flag
family of §G.2, 650 words.
Scan repeated markers, validate candidate manifests, decrypt
feature bitmaps, and emit ordered flags.
Thisisalsoaterminaltask,butbecausethefamily’smembers
genuinely share byte-level work, compression kept domain-
levelstepssuchasmanifestvalidationandbitmapdecryption.
Theremainingpriorsofthesameruncarrydomainshapetoo:
recovering a PostgreSQL key from the WAL (833 words),
step selection for flood-grid hazard avoidance (786), deter-
ministic EM fitting of a two-dimensional Gaussian mixture
(814),andbuildingadeterministicLaTeXPDFinanisolated
temporary directory (777).
Themostsharedcomesfromaround-1familypriorofALF-
World×MiniMax-M3, 926 words in all, of which its proce-
dure section is 440.
Step1|Action:Scantheinitialobservationfortheilluminator-
class object (lamp/mirror/magnifier/lantern) and record its
receptacleasthefixedfinaldestination|Pitfall:Do not default
to ‘desk’—illuminatorsfrequentlysitondressers,nightstands,
or shelves.
Step 2|Action: Issuego to <source_receptacle>
thentake <target> from <source_receptacle>
directly|Pitfall: A separateexaminewastes a turn...
§4.4, “What a prior keeps”, corresponds to this one. One
of the seven local skills in that family uses 989 words for
sevenstepsandembedsamemorisedlocationtable;thecom-
pressedfamilypriorstatesthesamejobinfourstepsand440
words of procedure, the table is gone, and Step 1 becomes a
singleread.Thedifferencefromthefirstexcerptisnotlength
butexecutability:thisonecarriesconcreteactioncommands
and a turn-budget consideration and can change the search
path, while the first can only change the wording. Its merge
notealsorecordsthatthecompressorchosebetweentwomu-
tually exclusive strategies rather than concatenating them.
H Benchmarks and Splits
Thereisonesetofsplitsinthispaper,andeverythingreadsit.
All four task streams are laid out once and held fixed across
rounds;thetwelverunsandbothcomparedmethodsreadthe
samesplitfiles,andnocellusesatasksetdrawnseparatelyfor
it.Allfoursplitfilesrecordseed=42,andthatseedcontrols
the TBP, SWE and LMB splits; the ALFWorld split is a
deterministic selection and does not depend on it. The split
files ship with the supplementary material, each recording
its split name, seed and size; the LMB and ALFWorld files
additionally carry a hash of the task identifiers.
Benchmark Stream size Basis of the split
Terminal-Bench-
Pro
32 tasks,
tbp_hard_
train32
the hard subset, 4 tasks
from each of 8 classes
SWE-bench Veri-
fied
20 instances,
swe_
15min1h_
train20
theofficialVerifiedset,fil-
tered by the official diffi-
culty annotation to the 15
min – 1 hour band
ALFWorld 42 tasks,
alfworld_
train42
derived from
alfworld_train60,
taking the lexicographi-
cally first 7 of each task
type — deterministic, not
random sampling
Live-
Mathematician-
Bench
53 tasks,
lmb_
train53
the official HuggingFace
monthly files 202511–
202602, merging the up-
stream train (35) and val
(18)
Table A17: The four task streams and how each was cut.
The four streams are Table A17. This paper has exactly two
held-outevaluations,listedinTableA18,andtheycomefrom
different places.
Used for Set Origin
Transfer, Table 4 ALFWorld
valid_
unseen, 60
tasks
thedataset’sownofficial
unseen split
§4.5,softwarere-
pair
swe_15min1h_
test30, 30
instances
cut here, same source
andsameseedastrain20
Table A18: The two held-out sets. They differ in origin, so
they carry different kinds of evidential weight.
seed=42governs the sampled splits and the task traversal
order, not generation. The base models are called through
vendorAPIsanddecodeatthedefaulttemperature,measured
at 0.7, and the seed does not enter the LLM request.

I Run Artefacts and Execution Volume
EverycellofTable1correspondstooneindependentcontin-
ual run. The outputs of all twelve ship with the supplemen-
tary material, one directory per cell, holding the per-round
summaries, the complete configuration, the library state, the
per-task results, and both the committed priors and the per-
task local skills.
Thetwelverunsshareoneloopsize:3rounds×3sub-rounds,
one trial per task. A sub-round is one real deployment over
the whole task stream. The loop size is the same for every
benchmark and every model; no cell was given a longer run
than another.
Benchmark Tasks
deployments
per run
all three
models
Terminal-Bench-Pro 32 288 864
SWE-bench Verified 20 180 540
ALFWorld 42 378 1134
LiveMathematicianBench 53 477 1431
Total 3969
Table A19: Training deployments.
The deployment count is Table A19. Searching over the
three candidate routes buys no extra rollouts: the routes are
not scored by running the task stream again for each; their
scores are read off the nine deployments already executed,
and whether a candidate enters the library is settled by the
first deployment of the next round, which is already inside
the budget. The table above is therefore the entire training
cost, and none of the machinery this paper adds is paid for
outside it.
Sub-rounds have diminishing returns. Pooling the twelve
runs, three rounds and all tasks gives 1323 task-×-round
pairs.Thesecondsub-roundgenuinelyimprovesatask’sbest
local skill 162 times, 12.2%, and the third 70 times, 5.3%.
J Reproduction Dispersion and Resolution
J.1 Reproduction Dispersion of a Single Trial
Decoding is not deterministic, so the reproduction spread is
measured rather than assumed. On the four splits the main
table uses, we take every round-0 no-injection measurement
matching on split, model, trial count and time limit — 18
measurements in six groups.
Split×Model reps mean s.d. range
SWEtrain20×DeepSeek-
V4-Pro
3 45.00%0.000.0pp
SWEtrain20×MiniMax-
M3
2 37.50% 3.54 5.0pp
ALFWorldtrain42×
MiniMax-M3
2 73.81% 3.37 4.8pp
ALFWorldtrain42×
DeepSeek-V4-Pro
2 59.52% 3.37 4.8pp
LMBtrain53×MiniMax-
M3
3 24.53% 3.27 5.7pp
LMBtrain53×GPT-5.4-
mini
6 14.78% 2.51 5.7pp
Table A20: Repeated round-0 No-Skill measurements.
Table A20 lists the six groups. The pooled within-group
standard deviation is 2.71pp on 12 degrees of freedom. The
main table’s mean Global gain over no-skill is 17.2 points,
6.4 times that standard deviation, and all twelve runs share a
sign.
J.2 Per-Cell Resolution
The significance in §D.1 belongs to the level of the twelve
runs and cannot be pushed down to a single cell. Single-cell
resolution is taken from the measured value in §J.1: with a
reproductionstandarddeviationof2.71pp,twostandardde-
viations is±5.4pp, and a reading inside that range is within
reproduction spread. That scale comes from 18 real repe-
titions and does not rest on an assumption that tasks are
independent and identically distributed. Under that assump-
tion, 42 and 53 tasks would give±9to15pp, two to three
times wider than what was measured.
K Hyperparameters
Thereisonehyperparametersettinginthispaper,nottwelve.
Every entry in Table A21 takes one value across all four
benchmarks×three models, and not one of them was ad-
justed for a cell by that cell’s own result. The gains in the
twelve cells are therefore not the product of per-cell search;
the price is that this paper does not report a sensitivity anal-
ysis for any of these values.

Parameter Value Selection criterion
RoundsT3 performance peaks at round 1
and then decays; three rounds are
enough to expose that
Sub-roundsJ3 marginal returns in §I
Trials per task 1 cost; dispersion in §J.1, resolution
in §J.2
Clustering view
weights
five-view 0.30/0.20/0.20/
0.20/0.10; four-view
0.25×4
hard-coded constants; provenance
in §B
Number of clus-
tersK
Kneedleknee,chosenauto-
matically
not set by hand; see §B
Recall top-k1 injectedonlyabovethreshold,oth-
erwise the base prior alone
Recall similarity
threshold
0.45 a single value shared by all four
benchmarks
Commit-gatetol-
eranceϵ
0.02 smaller than the measured repro-
duction standard deviation, so that
it absorbs noise; see §D.3
Embedding
quantisation
4-bit 8-bit was measured not to change
routing decisions
Decoding tem-
perature
vendor default, measured
0.7
unchanged
Table A21: The complete hyperparameter table.
L Compute Environment
Item Value
CPU AMD Ryzen AI 9 365, 18 logical cores
GPU NVIDIA RTX 5080 Laptop, 16GB
VRAM, driver 610.74
Memory 21GB allocated to WSL2, host 31GB
Operating system Windows+WSL2, Linux kernel
6.18.33.2
Container Docker 29.3.0, for the SWE-bench and
Terminal-Bench-Pro task containers
Python 3.13.12, conda environment
Key libraries torch 2.11.0·transformers 5.8.0·scikit-
learn 1.8.0·bitsandbytes 0.49.2
Embedding model Qwen3-Embedding-8B, 4-bit quantisa-
tion, about 5.8GB resident VRAM
Base models DeepSeek-V4-Pro, MiniMax-M3, GPT-
5.4-mini, all through vendor APIs
Table A22: Compute environment.
The environment is Table A22. The WSL2 memory ceiling
is a measured constraint rather than a preference: at 24GB
a fully loaded SWE run exhausts host memory, so it was
lowered to 21GB, and the concurrency of SWE and TBP
is bounded by that. The GPU is used only for embedding
retrieval and takes no part in base-model inference.
M Consolidation-Pipeline Prompts
Theconsolidationpipelineuses24prompttemplatesintotal,
and every one of them is phrased benchmark-independently:
no benchmark name and no task identifier, and the only
domain-specific text anywhere in them is a single category
phrase, described at the end of this section. The five core
promptsbelowaregiveninpipelineorderandarethevariants
actually deployed in the twelve runs; the placeholders are
filled with card content at run time.
Theyaresetfullwidthsothattheykeeptheexactlinebreak-
ing of the source; nothing has been re-wrapped or abridged.
None of the five contains a benchmark name, a task iden-
tifier or an answer. The only domain interface is one
placeholder, which at run time is replaced by the current
benchmark’s category phrase —terminal,software
engineering,household taskandresearch-
level math MCQrespectively. Family names are gener-
ated by the compression stage itself and are not drawn from
any preset taxonomy.
N Family Structure
For each benchmark we take the run whose family structure
is most evenly balanced, by the measure below. ALFWorld
is selected by ARI against the dataset’s labels; the other
three have no independent labels and are selected by the
balance of the size distribution,

H(sizes)/lnK

×(1−
singleton fraction). Prior counts follow the read-out of §E
and include the one base prior injected unconditionally into
every library, so they are always the number of familiesK
plus one; thePriorscolumn of Table 3 counts family priors
only.
N.1 Size and Distribution
Benchmark×Model
task
stream
clus-
teredKFamily sizes
committed
priors
prior
words
ALFWorld×
MiniMax-M3
42 40 15 7,5,5,4,3,3,2,2,2,
2,1×5
16 15,204
TBP×GPT-5.4-mini 32 32 10 5,5,5,4,3,3,2,2,2,
1
11 8,067
SWE×GPT-5.4-mini 20 11 5 4,2,2,2,1 6 4,434
LMB×MiniMax-M3 53 14 5 5,4,3,1,1 6 5,104
Table A23: Family structure, one run per benchmark.
N.2 Family Names and the Clustering Axis
Family names are generated by the compression stage after
clustering is finished, and were not rewritten by hand.The
name is not the clustering axis.The namer takes the sub-
ject wording of some salient member of the family, which
is why SWE’s family names carry a repository name and
LMB’scarrythenameofabranchofmathematics—butthe
members are not grouped along either of those axes.

Local skill extractionwritten into the procedure section after a task turns from failing to passing; de-instantiation is enforced at the top of the pipeline
A task just succeeded (pass_rate=1.0) after previously failing (pass_rate=0.0).
Extract MINIMAL, reusable procedure knowledge for the skill’s procedure slot.
Successful trajectory (key steps): {traj}
Final code (key part): {code}
Rules:
- Output 2-4 concise bullet points describing the STEPS that made this work
- Focus on FLOW: what to do first, what to check, what to call
- Include at most ONE short code snippet (<=8 lines) only if it encodes a
non-obvious pattern
- Do NOT include task-specific file paths, test constants, or verifier output
- Each bullet must be actionable: start with a verb
- Total output: <=80 words
Failure attribution drives the append-only repair route
An AI agent attempted a task but failed. Your job: identify which skill slot’s
guidance was missing or wrong, based on the agent’s actual code.
Extract the missing reusable knowledge, rule, mapping, schema invariant, parser
assumption, API/library usage rule, numeric/statistical criterion, or
algorithmic constraint that would have prevented this failure.
Do NOT default to generic process advice such as "avoid loops", "stop earlier",
or "be more careful" unless the evidence clearly proves that is the primary
missing rule.
Figure A1: The two prompts that read a single task’s own execution.
Benchmark Family name Member composition
SWE
django_numeric_
expression
django×3+sympy×1
astropy_ascii_htmlastropy×1+django×1
matplotlib_image_
normalization
matplotlib×1+xarray×1
django_queryset_
filtering
django×2
LMB
asymptotically_
flat_nonnegative
manifold mass inequality, stochastic
heat equation, dispersive PDE
exponential_o-
minimal_theory
character varieties, ultrafilter orders,
graph 1-factors, hyperbolic groups,
transseries
primitive_
permutation_group
permutation groups, Chow quotients
of flag varieties, Willmore surfaces,
commutator length
TableA24:ThreeofSWE’sfourmulti-memberfamiliescross
repositories,andallthreemulti-memberLMBfamiliescross
branches of mathematics.
Table A24 sets the names beside the member composition.
What the members really share sits in their procedure sig-
natures. The three LMB families’ signatures are “pick the
strongest provable one among nested propositions”, “order
by provable strength” and “give a complete classification”;
SWE’sare“locatetheexpression-handlingtableandaddone
case” and “guard before passing downstream”. That is con-
sistentwith§3.3,“groupsbyhowitissolvedratherthanwhat
the task is about”.
A reader who looks only at the family names would come
away with the opposite impression, which is why this sec-
tion gives the member composition. The namer sees only
the text inside a family, never the relations between fami-
lies, and making the name reflect the clustering axis is not
among its objectives. §4.4 records another instance of the
same phenomenon on the other TBP run: TBP×MiniMax-
M3formsK= 9families,oneofwhichholdseighttasks—
a debugger session, WAL recovery and a logic-gate CRC32
among them — and is namedsegfault_debugging_
withafter one member. That is a different partition from
the TBP×GPT-5.4-mini run of §G.2, which formsK= 10
families with at most five tasks in any of them. The name is
stored exactly as printed here.
N.3 Per-Family Gains
Round 2 against the round-0 baseline, hard, paired task by
task. The corresponding table for the terminal benchmark is
in §G.2.

Pairwise procedure judgementthe LLM channel of clustering; this is how the body’s “groups by how it is solved rather than what the task is about” is implemented
You are given two task descriptions.
Task 1: {a}
Task 2: {b}
Decide whether they share the SAME reusable procedure: would one procedure,
written once, correctly accomplish the core of BOTH tasks? Judge by the
underlying operation and the shape of the data flow, not by surface wording
or subject matter.
Return ONLY JSON: {"same": true | false, "reason": "<short>"}
Canonical signature generation feeds the signature channels of multi-view fusion
You are organizing {n} skill cards into a small set of canonical operation
categories. Group these {n} cards into K canonical operation buckets where K is
your choice in [{min_k}, {max_k}]. Two cards belong in the same bucket iff they
perform the SAME FUNDAMENTAL OPERATION (differing only in surface details:
column names, thresholds, file paths, domain). They MUST NOT be merged just
because they touch the same surface tech.
For each bucket, emit ONE canonical_label (3-5 lowercase words, lead with a
generic verb). All cards in a bucket get this EXACT canonical_label as their
new compact signature.
Figure A2: The two prompts that decide grouping.
FamilynComposition
base
→r2fixed
textworld_
receptacle-based_
object
7 look_at×7 4→7↑3
locate_source_
receptacle
5 pick_and_place×5 5→5 —
household_object_
pick-cool-place
5 pick_cool×5 4→5↑1
household_object_
pick-clean-place
4 pick_clean×4 3→4↑1
multi-instance_
pick-and-place
3 pick_two×3 3→3 —
carryable_
household_object
3 pick_heat×3 1→3↑2
⋆household_pick-
and-place:_locate
2 pick_and_place×1+
pick_two×1
2→2 —
⋆household_
object_pick-cool-
place
2 pick_cool×1+
pick_heat×1
2→2 —
household_food_
object
2 pick_heat×2 2→2 —
bowl_multi-
instance_pick-
and-place
2 pick_two×2 2→2 —
five singleton families 1×5 pick_and_place /
pick_clean×2/pick_two
/ pick_heat
3→4↑1
Table A25: ALFWorld×MiniMax-M3.Compositiongives
the dataset’s ground-truth types;⋆marks a family that cuts
acrosstwoofthem.Familynamesaregeneratedbythecom-
pression stage and are not guaranteed distinct: the two rows
namedhousehold_object_pick-cool-placeare
different families with disjoint members.
Familynbase→r2 fixed
django_numeric_expression4 1→2↑1
astropy_ascii_html2 2→2 —
django_queryset_filtering2 1→2↑1
matplotlib_image_
normalization
2 1→2↑1
astropy_fits_diff1 1→1 —
TableA26:SWE×GPT-5.4-mini;9tasksenterednocluster.
Familynbase→r2 fixed
exponential_o-minimal_
theory
5 4→5↑1
primitive_permutation_
group
4 1→4↑3
asymptotically_flat_
nonnegative
3 2→3↑1
wythoff_combinatorial_
game
1 0→1↑1
hankel-matrix_special-
fiber-ring
1 1→1 —

Family compressiongathers a family’s local skills into one candidate global prior, i.e. Eq. (3)
You are distilling {n_tasks} task-specific skills into ONE reusable
family-level skill.
These tasks were grouped by an automated clustering step and may or may not
share a real solving procedure - do not assume they do. Before writing
anything, judge honestly: would solving one of these tasks actually teach you
concrete, reusable steps for solving the others (same algorithm family, same
class of checks, same kind of artifact), or do they only share generic
competent-engineering discipline (read the spec first, probe the environment,
enumerate edge cases, validate formally)? If a candidate Step/Pattern would
only ever fire for 1 of the {n_tasks} tasks, DO NOT include it - leave it out
rather than force it in. It is a CORRECT and USEFUL output for
section_procedure to end up short and generic if that is what genuinely
generalizes; a short honest skill is far more useful downstream than a long one
that silently overfits to whichever task you processed last.
Figure A3: The compression step. The compressor is explicitly permitted to return something short and generic and is told that
a forced step is harmful; the first excerpt of §G.3 is what this instruction produces.
TableA27:LMB×MiniMax-M3;39tasksenterednoclus-
ter.
The three per-benchmark tables are Table A25, Table A26
and Table A27. Two notes on the read-out. More than one
candidateprioriskeptperfamilywhilecandidatesarebeing
generated, but exactly one per family is committed to the
library, so the prior count is the number of families plus
one base prior, and the counts above are the ones actually
committed. Agreement with the dataset’s labels can only be
measuredonALFWorld,theonlyoneofthefourbenchmarks
carrying independent solution-type labels.
O Other Ways to Organise a Library
O.1 Prior Repair
The second candidate route of §3.4 is append-only repair.
Its net effect, taken as the soft difference between two con-
secutive sub-round evaluations of the same run, is↑3.1 for
DeepSeek,↓3.4 for GPT and↑4.8 for MiniMax-M3. The
three are of comparable magnitude and the sign flips with
the model, so repair is not guaranteed to help and is adju-
dicated by the commit gate in real execution. This is also
whythethreecandidateroutesareallsentintothesamegate
rather than being given a fixed priority order.
O.2 A Flat Retrieval Library
The other opposing form is a flat library that stores every
historical local skill and retrieves across tasks. That control
was run on LMB’s 15-task validation split with the same
model, the same injection channel and the same retriever,
changing only how the library is built.
Library construction
en-
tries
has
Gbase
val15
soft
No-Skill 0 — 0.267
Flat library, all local skills 53 no 0.333
Flat library, rebuilt after fixing re-
trieval
49 yes 0.333
Flat library, construction three 54 yes 0.333
Flat library, construction four 54 yes 0.467
Family library, faithful LLM merge22yes 0.400
Family library, another construction22yes0.467
Table A28: Flat versus family libraries on LMB val15.
ThecomparisonisTableA28.Thefamilylibraryreachesthis
group’s top score, 0.467, with0.42×the entries, matching
a flat library 2.4 times its size, and both family arms are
above the median of the four flat arms. This is the same
kind of statement as the compression ratio of §E: the library
is smaller without being worse. The control is a 15-task
validationsplitatasingletrial.Theflatpoolwithretrievalin
Table 2 is carried by the AWM column, which is a read-out
over all twelve cells.
