---
title: 'SkillNEO: Non-Elitist Evolutionary Optimization of Agent Skills'
url: https://arxiv.org/abs/2610.20926
category: ai-marketing
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Enze Ma
- Chunyu Miao
- Yankai Chen
- Jie Yang
- Liancheng Fang
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.20926
pages: 38
chars: 148836
fetched_at: '2026-11-08T13:35:27+00:00'
kb_version: 1
---

# SkillNEO: Non-Elitist Evolutionary Optimization of Agent Skills

Preprint version
SKILL NEO: N ON-E LITIST EVOLUTIONARY
OPTIMIZATION OF AGENT SKILLS
Enze Ma1, Chunyu Miao1, Yankai Chen2, Jie Yang1, Liancheng Fang1, Kening Zheng1,
Hanrong Zhang1, Muyao Xu5, Xinle Yu3, Chengze Li1, Wei-Chieh Huang1, Ziwei Ren4,
Yunhao Du4, Zhixiang Shen1, Xue Liu2, Philip S. Yu1, Zhen Wang6
1 University of Illinois at Chicago 2 Mohamed bin Zayed University of Artiﬁcial Intelligence
3 University of California, San Diego 4 University of California, Los Angeles
5 Independent Researcher 6 University of Texas at Arlington
ABSTRACT
Agent skills turn procedural knowledge into reusable artifacts, allowing LLM
agents to accumulate and reﬁne expertise through experience. Building on this,
skill evolution uses execution feedback to improve skills over successive revisions.
However, improvement may require several interdependent edits, so a low-reward
version can still be worth developing. Requiring immediate reward gains can
therefore discard useful partial repairs before their beneﬁts emerge. Non-elitist
evolution allows new versions to receive further edits even when they score below
earlier ones. For agent skills, this opportunity also calls for evidence of what to
preserve and what to repair in the next edit. We introduce SkillNEO (Non-Elitist
Evolutionary Optimization for Agent Skills), which separates the choice of a skill
version to use from the choice of versions to keep improving. By comparing
how related versions carry out the same task, it identiﬁes working steps to pre-
serve and remaining failures to ﬁx. It can also return to earlier versions and revise
them using what later attempts reveal. Across 86 SkillsBench tasks spanning soft-
ware engineering, ofﬁce work, and six other domains, SkillNEO raises GPT-5.4
Mini’s average reward from 49.1% to 66.4%, bringing it into GPT-5.5 and GPT-
5.6 Luna’s original-skill performance range. Mini executes tasks, proposes revi-
sions, and edits skills, with ﬁnal evaluation using the same task instances. Gains
extend across all eight domains. The same skills also improve stronger models
without further editing. On the 41 tasks with modiﬁed skills, reuse improves
Luna by 10.5 percentage points and places GPT-5.5 10.6 points above its pub-
lished original-skill reference on those tasks. Execution records show that these
skills can beneﬁt stronger models even when Mini still fails some task require-
ments. Recorded searches also show lower-scoring versions leading to the skills
ultimately selected for use. Together, these ﬁndings show that skill evolution can
turn a weaker model’s partial progress into reusable procedural knowledge for
improving more capable agents.
1 I NTRODUCTION
LLM agents increasingly perform tasks that require procedural expertise, including how to use do-
main tools, coordinate dependent steps, and verify intermediate results ( Li et al., 2026; Zhang et al.,
2026b). Agent skills make this expertise reusable through natural-language guidance, executable
programs, and workﬂows ( Wang et al. , 2023; 2025; Li et al. , 2026). Such reusable procedures al-
ready support web interaction, memory management, and even skill learning itself ( Zheng et al. ,
2025; Zhang et al. , 2026c;a). Beyond guiding execution, these artifacts can also retain and reﬁne
lessons from earlier attempts ( Wang et al. , 2025; Zhou et al. , 2026a; Ni et al. , 2026). Building on
this, skill evolution revises instructions, scripts, and resources using execution feedback, then selects
versions for further development by task performance ( Alzubi et al., 2026; Wang et al., 2026b).
However, a skill’s current task reward can conceal partial progress within its procedure. We call the
skills provided for a task and their associated ﬁles a skill bundle. Because the instructions, scripts,
and supporting resources within a bundle can be coupled ( Li et al. , 2026; Zhang et al. , 2026b),
1
arXiv:2610.20926v2  [cs.AI]  20 Oct 2026

Preprint version
s0 s1 s3 s5
s2 s4
?
revisit
original
partial repair
previous best
new best
earlier later
compare traces
guide editss0
s1 s3 s5
s2
s4
s6
s7
(a) Single-direction refinement (b) SkillNEO: non-elitist development + trace comparison
Figure 1: Non-elitist evolution allows weaker revisions to lead to better skills. (a) Single-
direction reﬁnement discards alternative revisions, potentially losing useful partial repairs. (b) Skill-
NEO develops and revisits such revisions, using execution-trace comparisons to guide further re-
pairs that can yield a new best skill. States si pair skill bundles with their execution records. The
dark-blue node marks the new deployment incumbent; crossed-out nodes in (a) denote discarded
revisions. Solid tree edges denote edits; in (b), the dashed orange arrow denotes reselection.
completing a repair may require several interdependent edits. For example, a revision can correct
input processing while leaving output construction incomplete, so the whole-task reward remains
unchanged or even declines. Y et requiring improvement over the parent (Wang et al., 2026b; Shastri
et al. , 2026) or retaining the highest-scoring candidates across generations ( Alzubi et al. , 2026;
Sun et al. , 2026) can exclude this partial repair from further editing. The challenge is therefore to
distinguish a version’s readiness for deployment from its value as a starting point for further repair.
Non-elitist evolutionary selection provides a concrete way to preserve these opportunities for further
repair ( Beyer & Schwefel , 2002; Oliveto et al. , 2018). In offspring-only replacement, unchanged
parents do not compete for the next generation’s places, while candidates still compete on measured
performance within their generation. A partially repaired child can therefore receive further edits
even when its parent or an earlier version scores higher. For skill evolution, this permits a sequence
of revisions to continue before a reward gain emerges, while the best available version remains
deployed. Further development requires guidance on how to complete each repair. Task reward
alone cannot identify working steps or unresolved failures ( Agrawal et al., 2026).
We realize this opportunity in SkillNEO, a framework for Non-Elitist Evolutionary Optimization
for Agent Skills that guides non-elitist skill development through comparative execution evidence
(Figure 1). Each candidate pairs a skill bundle with its execution history, preserving both a starting
point for further edits and the evidence needed to direct them. We organize comparisons of these
executions along the revision tree, building on execution-guided skill diagnosis and reﬁnement ( Gao
et al. , 2026; Ni et al. , 2026). Parent-child comparisons relate behavioral changes to edits, while
sibling comparisons contrast alternative repairs from a shared starting point. These comparisons
reveal working procedures and unresolved failures, guiding coordinated changes to instructions,
scripts, and resources, including reuse across branches. Archive revisiting extends this process to
earlier versions, allowing them to be revised using evidence gathered after their creation.
We evaluate task-conditioned skill development on 86 SkillsBench tasks, with ﬁnal evaluation using
the same task instances. With GPT-5.4 Mini ( OpenAI, 2026b) performing task execution, pro-
posal generation, and editing, SkillNEO raises its average reward from 49.1% to 66.4%, within
GPT-5.5 and GPT-5.6 Luna’s original-skill performance range. Recorded searches show lower-
scoring versions becoming ancestors of deployed bundles and supplying useful procedures to other
branches. Beyond Mini’s own gains, the frozen skills deliver substantial improvements when reused
by stronger executors. On the 41 modiﬁed tasks, reuse improves Luna by 10.5 percentage points;
GPT-5.5 exceeds its published original-skill reference on these tasks by 10.6 points. Together, these
results suggest that skill evolution can accumulate procedural knowledge across revisions and extend
the beneﬁts of one model’s experience to more capable agents.
2 R ELATED WORK
Agent skills and reusable knowledge. Agent skills take forms such as natural-language guidance,
executable programs, workﬂows, and learned policies ( Wang et al., 2023; 2025; Jiang et al. , 2026).
These skills support web operations (Zheng et al., 2025), shared interfaces across websites (Y u et al.,
2

Preprint version
2026a), and further skill development ( Zhang et al. , 2026a). Previous studies also show that skills
can transfer across models ( Zheng et al. , 2025; Zhang et al. , 2026b; Y ang et al., 2026; Tan et al. ,
2026; Xiong et al., 2026). Related agent research covers memory management and auditing ( Zhang
et al., 2026c; Ma et al., 2026), as well as scientiﬁc workﬂows and their evaluation ( Gao et al., 2025;
Wang et al., 2026c). Skill and agent evolution reﬁne reusable artifacts over successive rounds using
execution feedback ( Zhou et al. , 2026a; Tan et al. , 2026; Hu et al. , 2026). ACE reﬁnes context as
an evolving playbook (Zhang et al., 2026e), while Meta Context Engineering evolves the skills used
to construct and update context ( Y e et al., 2026). We study how to choose versions for continued
development and use their execution records to guide revisions.
Search and candidate selection. Search methods explore alternative candidates for reasoning ( Hao
et al., 2023; 2024; Wang et al. , 2026a) and scientiﬁc discovery ( Liu et al. , 2026; Y u et al., 2026b).
Prompt optimizers use feedback and beam search ( Pryzant et al. , 2023; Singla et al. , 2024), error-
guided tree search ( Wang et al., 2024), prompt-score histories ( Y ang et al., 2024), or evolving mu-
tation prompts ( Fernando et al. , 2024). NPO reports that single-lineage search is competitive in its
evaluated settings (Chang & Chen , 2026).
Candidate retention determines which skill versions receive further edits. Evolutionary comma se-
lection replaces parents with offspring, allowing the active population’s best ﬁtness to decline across
generations (Beyer & Schwefel, 2002). Skill-evolution methods differ in the conditions they impose
on continued development. Once its validation-ranked frontier is full, EvoSkill admits only candi-
dates that outperform its lowest-scoring member ( Alzubi et al., 2026). GraphSkillEvo uses mutation
and crossover on graph-structured skills, retaining the highest-scoring candidates from the com-
bined parent-child pool ( Sun et al. , 2026). MetaSkill-Evolve retains failed revisions as inspiration
but requires positive parent-relative gain for future parent eligibility ( Wang et al., 2026b).
Several methods preserve alternatives through tree search, multiple populations, or an archive. BON-
SAI revisits weaker branches through an evolvability-guided tree policy, supports grafting, and sep-
arates search from deployment; ordinary rewrites must improve on their parent on the reﬂection
minibatch (Shastri et al. , 2026). DIVE retains parents alongside children, targets lower-performing
skills for exploratory revision, evolves independent populations, and selects complementary skills
for inference ( Xiong et al. , 2026). DGM evolves coding agents by sampling archived implementa-
tions for further self-modiﬁcation ( Zhang et al. , 2026d). Our ordinary update selects parents only
from eligible, fully measured children in the current generation. Previous parents do not compete,
and children need no parent-relative gain. Eligible earlier bundles can return to the parent pool
through a separate archive-revisiting rule.
Execution-guided skill reﬁnement. Execution feedback can supply both reusable guidance and ev-
idence for its revision. AWM abstracts workﬂows from execution histories (Wang et al., 2025), while
SkillRL co-evolves an experience-derived skill library with a reinforcement-learned policy ( Xia
et al. , 2026). OpenClaw-Skill searches skill compositions across subtasks ( Lin et al. , 2026b);
our tree records alternative versions of a complete bundle. Reﬂexion stores reﬂections for later
attempts ( Shinn et al. , 2023), while ExpeL compares successful and failed executions to update
reusable insights ( Zhao et al. , 2024). GEPA reﬂects on trajectories and merges prompts across lin-
eages (Agrawal et al., 2026); EvoSkill and MetaSkill-Evolve reuse proposal histories or retrieved in-
spirations (Alzubi et al., 2026; Wang et al., 2026b). Trace2Skill consolidates trajectory-level patches
into a portable skill directory ( Ni et al. , 2026); SkillAudit compares executions with and without a
skill to guide revision ( Gao et al. , 2026). Branch2Skill compares shared-preﬁx reasoning paths for
local supervision ( Ren et al. , 2026); SkillLift learns an oracle-aligned rubric to guide revisions be-
tween costly evaluations (Kang & Wen, 2026). SkillNEO links executions to saved bundle versions,
comparing repeated runs of the same version and parent-child or sibling executions. This evidence
guides joint edits to instructions and supporting ﬁles, including reuse of working procedures from
versions with unresolved failures. Later executions can guide edits to saved bundles.
3 S KILL NEO FOR NON-E LITIST EVOLUTION OF AGENT SKILLS
SkillNEO maintains a deployed bundle while developing alternatives that may need further repair
(Figure 2). Two decisions govern this process. Deployment determines whether a measured can-
didate should replace the incumbent; development determines which versions can receive another
edit. Non-elitist selection keeps these decisions separate. Comparisons of related executions guide
these revisions by identifying working procedures to preserve and unresolved failures to address.
3

Preprint version
Non-elitist development
Saved bundles and their executions
Trace-guided revision
Proposer
Compare saved executions
Propose targeted edits
Skill Editor
Revise instructions,
scripts and resources
Executor
Execute the candidate
Score with task verifier
Edit Validation
Check files, scripts,
and content rules
Proposal
Candidate
Pass
Repair
Execution history
Versions
Instructions
scripts, resources
Executions
Traces, outputs,
rewards
Deploy one Renew parents
Retain or replace
the incumbent
Current children or
archive survivors
Figure 2: SkillNEO separates choosing a skill to use from choosing versions to improve. A
version can receive further edits (green) even when it scores below the version selected for use
(blue). To guide these edits, the Proposer compares saved task executions to identify steps that work
and failures that need repair. The Skill Editor applies the proposed changes to instructions, scripts,
and resources. Edit V alidation checks the revised ﬁles before the Executor runs the task with the new
version. The resulting scores inform selection, and execution records guide the next round. Mini
ﬁlls every model-based role in our experiments.
3.1 P ROBLEM FORMULATION
Given a task and an initial skill bundle, we seek revisions that improve a frozen agent’s expected
task reward. Let t denote a task with a ﬁxed instruction, execution environment, and veriﬁer Vt.
SkillsBench supplies each task with a set of relevant skills ( Li et al. , 2026). Each skill contains its
own SKILL.md document and optional executable tools and resources. A bundle L stores a version
of this entire set, and SkillNEO evolves each task’s bundle independently. A frozen agent Am with
model m executes t using L, producing a trajectory τ and an outcome y containing the submitted
artifacts and ﬁnal environment state. The veriﬁer assigns reward Vt(y) ∈ [0, 1]. We deﬁne Jm(L; t)
as this agent’s expected reward on task t with bundle L.
(τ, y) ∼ Am(t, L), J m(L; t) = E(τ,y)∼Am(t,L)[Vt(y)]. (1)
The expectation is over execution variability for the same task, model, and bundle. An execution
record e = ( τ, y, r, d) contains the trajectory, outcome, reward r = Vt(y), and ﬁltered veriﬁer ﬁnd-
ings d. Traces and ﬁndings guide revisions; rewards measure task performance. Controlled bundle
comparisons use the same task instruction, execution environment, veriﬁer, and model conﬁguration.
Starting from the original bundle L0 t , edits deﬁne a space of reachable bundles Lt. An edit a =
(target, operator, speciﬁcation) produces L′ = Apply(L, a) and may revise instructions, executable
code, or resources within the bundle. The ideal objective and the output of a ﬁnite search are
max
L∈Lt
Jm(L; t), bLt = Sκ(t, L0 t , m), (2)
where Sκ denotes the search procedure and κ speciﬁes its generation limit, candidate width, and
evaluation repeats. We estimate Jm(L; t) from a ﬁnite number of executions, retaining evaluated
bundles and their execution records to guide subsequent edits. Once development ends for task t,
we freeze its selected deployment bundle bLt. Running this procedure independently across tasks
D yields the task-indexed assignment bL = ( bLt)t∈D. Cross-model reuse then evaluates these same
task-bundle pairs with another frozen model, without repeating skill development for the receiver.
3.2 N ON-E LITIST SKILL DEVELOPMENT
We retain both the bundle and its execution history so that a saved version can serve as a starting
point for further repair. For task t, a rooted tree Tt = ( Vt, At) records revisions. Node v stores
sv = ( Lv, Ev), where Lv is a complete bundle and Ev contains its execution records. An edit au
4

Preprint version
creates child u from a saved primary parent p(u),
Lu = Apply(Lp(u), au), (p(u), u) ∈ A t. (3)
The root stores L0 ≡ L0 t . A graft can reuse another version’s procedure while retaining one primary
parent edge. At the end of generation g, hg indexes the deployment incumbent, and Bg contains the
versions eligible to parent edits in generation g + 1.
The ordinary development update selects parents from the current generation’s children. With
parent-pool capacity k, we screen admitted children and promote up to k for repeated evaluation.
Let Cg contain the promoted children with complete evaluations and available bundles. We form the
ordinary parent set from these children,
Bord g = Topk(Cg). (4)
Previous parents do not compete for places in this pool. This offspring-only replacement follows
non-elitist comma selection ( Beyer & Schwefel, 2002). Children compete on measured task reward
within their generation, without needing to outperform their own parents or enter the historical top-k.
A child can therefore receive another edit even when its current reward is too low for deployment.
This ordinary update supplies the default parent set. Archive revisiting can replace it with eligible
earlier versions under the conditions in Section 3.4. We then add the measured root if fewer than
two parents remain and the root is absent. The resulting Bg supplies the next round of edits, while
the deployment decision separately determines hg.
3.3 C OMPARATIVE EVIDENCE FOR SKILL REVISION
Task rewards rank outcomes; the executions behind those outcomes help identify a useful next edit.
We compare repeated runs of one version to examine execution variability, parent-child runs to relate
behavioral changes to an edit, and sibling runs to examine alternative repairs. Generation one uses
repeated root executions. Later generations add population scores, traces, tool outputs, submitted
artifacts, routing records, and edit differences linked to their bundle versions. This evidence includes
screening-only children outside the parent pool, so a version can inform a revision even when it is
ineligible to supply its starting bundle.
The Proposer uses these comparisons to identify unresolved failures and successful procedures
worth preserving. Routing records distinguish failure to consult a skill from failure after consult-
ing it. The ﬁrst can call for revising the skill’s visible description; the second calls for examining
its procedure and supporting ﬁles. We instruct the Proposer to rank suspected causes by the failed
runs they explain and check them against passing executions. Errors that an agent recovers from
do not by themselves justify a revision. Each proposal identiﬁes a primary parent from Bg−1, an
intended change, and supporting evidence. V eriﬁer ﬁndings are ﬁltered before entering the proposal
context. The prompt also discourages repeating edit directions previously measured as net losses;
this constraint on proposed edits does not change parent eligibility.
The Skill Editor turns a proposal into a complete child bundle while preserving the saved parent. A
repair can require coordinated changes across instructions, scripts, and resources, such as adding a
helper together with the instruction that invokes it. The editor can rewrite, add, remove, or reorganize
these ﬁles, or graft a procedure from another eligible parent. We instruct it to preserve unrelated
content. Appendix B speciﬁes the operators and proposal constraints.
Edit V alidation checks operation constraints, referenced ﬁles, new scripts, and candidate content
before task evaluation. Fixable failures return to the Skill Editor for repair and rechecking; rejected
candidates do not enter evaluation. Admitted candidates are scored by the benchmark veriﬁer Vt.
Appendix B.2 speciﬁes the checks and repair paths.
3.4 E VALUATION , D EPLOYMENT , AND ARCHIVE REVISITING
Repeated evaluation determines which revisions are ready for deployment. The Executor runs a task
with a bundle and records trajectories, tool outputs, and submitted artifacts. We estimate bundle
performance by averaging veriﬁer rewards over an execution batch (Equation 6). The root receives
R initial executions. Each generation requests b children, screens each admitted child once, and
promotes up to k for R − 1 additional executions. The incumbent receives R fresh executions.
Deployment ranks promoted children by their mean reward over all R executions, including screen-
ing. Compatible auxiliary scores break ofﬁcial-score ties at both screening and deployment. Our
experiments use (b, k, R) = (6 , 3, 3).
5

Preprint version
Table 1: Overall rewards and cross-model reuse. Average task reward (%) for the 86-task assign-
ment (a) and 41 modiﬁed tasks (b); ∆ is in percentage points. † GPT-5.4 compares V als (87 tasks,
OpenHands) with ﬁnal evaluation on 86 tasks using Codex. GPT-5.5 uses published, task-aligned
SkillsBench references; Luna uses post-freeze evaluations of both conditions. Subset gains/ties/
losses are 29/12/0 (Mini), 15/18/8 (GPT-5.5), and 11/23/7 (Luna), with ties within ±0.05 pp.
(a) Overall performance
Model
Original /
reference Final ∆ (pp)
GPT-5.4 Mini 49.1 66.4 +17.3
GPT-5.5 66.1 69.6 +3.5
GPT-5.6 Luna 67.3 71.9 +4.6
GPT-5.4† 51.7 65.5 +13.8†
(b) 41 modiﬁed tasks
Model
Original /
reference Final ∆ (pp)
GPT-5.4 Mini 31.5 67.8 +36.3
GPT-5.5 60.5 71.1 +10.6
GPT-5.6 Luna 63.9 74.4 +10.5
GPT-5.4 subset reference unavailable.
We compare the best fully measured child with the incumbent under the conﬁgured acceptance rule.
The current-batch criterion requires an ofﬁcial-score gain beyond the margin, or an ofﬁcial-score tie
with sufﬁcient auxiliary-score gain. Under the strict-ﬂoor conﬁguration, the child’s mean must also
exceed the larger pooled ofﬁcial score of the root and incumbent. A failed comparison leaves the
incumbent deployed and produces a H OLD . Appendix B gives the margins, historical checks, and
handling of incomplete evaluation records.
Archive revisiting allows development to return to an earlier branch with evidence collected since
that version was created. When enabled, it can replace the ordinary parent set after a H OLD in
which the best child’s ofﬁcial mean reward is below the incumbent’s. Retirement rules determine
which saved versions can re-enter development. The incumbent remains deployed as the parent set
changes. Search allows up to ﬁve generations and stops after two consecutive holds, with additional
termination conditions speciﬁed in Appendix B. Algorithm 1 gives the complete procedure. The
output bLt = Lhg is frozen before cross-model reuse.
4 E XPERIMENTS
4.1 E XPERIMENTAL SETUP
Evaluation scope. We evaluate how much SkillNEO improves Mini’s task performance, then ex-
amine recorded search paths to understand how intermediate versions contribute to later revisions.
We also test whether the frozen bundles remain useful to stronger executors. Development and ﬁnal
evaluation use the same task and input instances. Appendix A discusses the limitations.
Benchmark and metric. We use 86 professional tasks from SkillsBench 1.1, spanning eight broad
categories ( Li et al. , 2026). Each task’s supplied skills form its initial bundle, which we develop
independently. For task set D, model m, and bundle assignment L = ( Lt)t∈D, repeat q produces
(τt,q, yt,q) ∼ Am(t, Lt). We average three rewards per task, then take the mean across tasks,
Sm(L) = 100 |D| X t∈D 1 3 3X q=1 Vt(yt,q). (5)
Average reward is reported as a percentage and retains fractional rewards; it equals success rate only
for binary tasks. Published references retain their documented aggregation.
Models and skill reuse. GPT-5.4 Mini/Codex (OpenAI, 2026a) at high reasoning performs every
LLM call during development, including task execution, proposal generation, and skill editing. Let
L0 denote the original bundle assignment and bL the frozen assignment selected by development.
The latter contains 41 modiﬁed bundles and 45 bundles byte-identical to their originals. We eval-
uate these same task-bundle pairs with GPT-5.4/Codex xhigh, GPT-5.5/Codex xhigh, and GPT-5.6
Luna/Codex max. Reuse involves no further skill search or feedback to development.
Final evaluation protocol. Mini’s 41 modiﬁed bundles receive three post-evolution executions
per task, separate from search and selection. The 45 unchanged bundles share the three original-
skill executions because their original and ﬁnal conﬁgurations are identical. Mini’s 86-task score
6

Preprint version
Table 2: Mini’s rewards across eight domains. Average task reward (%) on the same 86 tasks. No
skill† is a published GPT-5.4 Mini/OpenHands reference, reaggregated by domain; Original skills
and SkillNEO use our Mini/Codex high evaluation. ∆ = SkillNEO − Original skills, in percentage
points. The Overall row averages all 86 tasks.
Domain N No skill† Original skills SkillNEO ∆ (pp)
Software engineering 16 26.9 48.3 75.7 +27.4
Ofﬁce / white collar 14 40.5 47.6 61.9 +14.3
Natural science 14 38.3 53.0 71.4 +18.4
Industrial / physical 14 28.6 48.3 53.9 +5.6
Finance / economics 9 18.5 22.2 48.1 +25.9
Mathematics / formal 7 38.1 61.9 79.5 +17.6
Cybersecurity 7 15.0 57.1 69.8 +12.7
Media / content 5 20.0 66.7 80.0 +13.3
Overall 86 29.9 49.1 66.4 +17.3
Software
eng. (16)
Office / white
collar (14)
Natural
science (14)
Industrial /
physical (14)
Finance /
economics (9)
Math. /
formal (7)
Cybersecurity
(7)
Media /
content (5)
0
20
40
60
80
100
Average reward (%)
75.7
(+27.4)
61.9
(+14.3) 71.4
(+18.4)
53.9
(+5.6)
48.1
(+25.9)
79.5
(+17.6)
69.8
(+12.7) 80.0
(+13.3)
No skill† Original skills SkillNEO
Figure 3: Mini improves across all eight domains. No skill † uses the OpenHands reference in
Table 2; Original skills and SkillNEO use our Mini/Codex high evaluation. Parenthesized gains are
SkillNEO minus Original skills (pp). Domain counts sum to 86.
combines these measurements. Luna evaluates both assignments after skill freezing, yielding 516
valid executions. Appendix B gives the reference sources and execution details.
4.2 P ERFORMANCE ACROSS TASKS AND DOMAINS
Mini reaches the performance range of stronger models using original skills. With Mini in every
model-based development role, SkillNEO raises its average reward across 86 tasks from 49.1% to
66.4% (Table 1a). The ﬁnal score lies between GPT-5.5’s published original-skill reference of 66.1%
and Luna’s original-skill score of 67.3%. On the 41 modiﬁed tasks, fresh post-evolution evaluation
gives Mini 67.8% against the original-skill 31.5%, with 29 gains, 12 ties, and no observed losses.
The other 45 tasks retain their original bundles and Mini scores.
Mini improves across all eight domains. Improvements range from 5.6 pp in industrial / physical
tasks to 27.4 pp in software engineering (Figure 3; Table 2). Both domains start near 48.3%. Execu-
tion records show how revisions translate task requirements into concrete actions and where those
requirements remain unenforced.
Revised skills help Mini check and satisfy task requirements. In SimPO, the original runs already
produce loss vectors numerically matching passing runs, but use Python 3.12 despite the Python
3.10 requirement. The evolved skill puts environment activation before installation and testing; ﬁnal
executions satisfy the requirement and pass. In Data-to-D3, the revised skill requires interaction
checks. One ﬁnal execution ﬁxes and retests a bug that clears a row when selected twice.
However, some revised workﬂows still leave a requirement unchecked or unenforced. Adaptive
Cruise Control improves only partially; its remaining failed execution checks speed and distance
summaries without verifying that emergency mode occurs. Manufacturing Codebook Normaliza-
tion’s completed runs use test-item context for electrical-fault labels where the revised skill requires
7

Preprint version
Final evaluation:  Mini 0.0 33.3% Final evaluation:  Mini 75.7 100.0%
Gravitational Wave Detection
Keep e01 selected while developing e04.
Sales Pivot Analysis
b04 XLSX skill
b05 PDF extraction
Candidate c04
XLSX
PDF
+
trace-guided reuse
Later revisions: c04 d09 e02 f07 selected
G0 G0G1 G1G2 G2G3 G3G4 G4G5
revisit d06
G3 parent reused in G5
root rootb07 c03 d06
e03
e03f08
run 1
earlier trace informs edit
restart from original
b06
d08
1 2 3 4 5
Generation
0
33.3
66.7
100
e01
select f04
continue e04
Selected bundle
Final skill's path
Reward (%)
(a) Continue a partial repair (b) Reuse a sibling procedure
(c) An earlier parent yields the final bundle (d) Restart from root, reuse earlier traces
Figure 4: Case studies of skill evolution in SkillNEO. (a) A zero-reward partial repair leads to
the next selected skill in Gravitational Wave Detection. (b) Sales Pivot Analysis reuses a sibling’s
PDF extraction procedure in another branch. (c) Revisiting an earlier parent produces the ﬁnal skill
in Paratransit. (d) Restarting from the original bundle uses execution evidence collected later in
Wyckoff. Panel (a) reports three-run mean rewards at creation. In (c) and (d), solid edges show
primary parents, broken arrows show reuse or reselection, and rewards come from independent ﬁnal
Mini evaluations (Appendices H and I).
component evidence from the raw segment, and still fail codebook checks. Appendix D.1 links the
skill revisions to all 24 executions of the original and ﬁnal bundles.
4.3 S EARCH PATHS AND EXECUTION EVIDENCE
We examine the 41 modiﬁed bundles’ development histories to trace how intermediate versions
contribute to later skills. The records show continued repairs, procedure reuse across branches, and
edits informed by later executions. Candidate letters b through f denote generations 1 through 5;
e04, for example, is candidate 04 in generation 4.
Lower-scoring versions can lead to better ﬁnal skills. Among the 29 tasks with ﬁnal Mini gains,
22 (75.9%) use a non-incumbent parent on the ﬁnal path. Sixteen paths pass through a candidate
that scored below the deployed bundle when it was created. Across the 41 searches, 163 such lower-
scoring versions receive further edits, and 45 have a later deployed descendant. For 18 of these 45
versions, the ﬁrst deployed descendant lies at least two edits away (Appendix H).
Zero reward can hide steps that already work. In Gravitational Wave Detection (Figure 4a), e04
scores zero despite passing eight of nine checks in every execution. Generation four deploys e01
but retains e04 in a three-parent pool despite three higher-scoring saved versions. The remaining
failure concerns the numerical result, with all three runs using the 15 Hz conditioning cutoff for
search despite a separate skill specifying 20 Hz. Child f04 consolidates the two skills, placing the
20 Hz search setting alongside the 15 Hz conditioning steps without changing helper code. All three
child executions follow these settings and pass every check. The search deploys f04 at 100.0%
mean reward against the re-measured incumbent’s 66.7% (Appendix I.2).
The ﬁgure’s orange curve follows the ﬁnal skill’s ancestry through the decline to e04 and its sub-
sequent repair; the blue curve records the deployment incumbent. Final evaluation raises Mini from
0.0% to 100.0%, while Luna retains 100.0%. Appendix H documents a similar case in Data-to-D3,
where d03 remains in a three-parent pool despite three higher-scoring saved versions.
Comparing runs reveals reusable steps in lower-scoring skills. Eight graft edits on six ﬁnal
ancestries draw from donors outside those primary paths. In Sales Pivot Analysis, the lower-scoring
b05 contributes state-name handling to a sibling branch (Figure 4b). Its two failed runs pass state-
validity checks but fail pivot conﬁguration; a third run succeeds. Citing that successful execution, the
8

Preprint version
Table 3: Execution behavior with the same ﬁnal skill bundle. Models differ in which requirements
they satisfy despite receiving identical guidance. Counts give passes out of three executions; skipped
checks are not passes. For Sales Pivot, V alid pivot objects requires the row-ﬁeld, aggregation, and
cache-ﬁeld checks to pass. Reward is mean task reward (%).
(a) Software Dependency Audit
Model Reward
Intended
scan scope
Correct
output ﬁelds
Mini 66.7 3/3 2/3
GPT-5.4 100.0 3/3 3/3
GPT-5.5 100.0 3/3 3/3
Luna 100.0 3/3 3/3
(b) Sales Pivot Analysis
Model Reward
V alid
state values
V alid
pivot objects
Mini 33.3 3/3 1/3
GPT-5.4 66.7 2/3 3/3
GPT-5.5 0.0 0/3 3/3
Luna 100.0 3/3 3/3
c04 proposal selects b04 as parent and b05 as donor. The edit preserves b04’s spreadsheet skill
for pivot construction and imports b05’s PDF extraction procedure. Both passing c04 executions
use the adopted extraction pattern with full state names. Although the historical-score check keeps
b04 deployed, c04 remains eligible for further edits and enters the ﬁnal ancestry. The comparison
recovers a useful procedure from a bundle with lower reward (Appendix I.4).
Comparing runs shows what to keep and what to ﬁx next. Software Dependency Audit requires
vulnerabilities in production dependencies, and its original command example already uses that
scope. Revision b06 adds deduplication and checks that the saved CSV matches the scan-derived
records. Its failed execution veriﬁes 22 ﬁndings but still expands the scan to development dependen-
cies; passing executions report three production-dependency ﬁndings. Checking the report against
the scan cannot correct the scan’s scope. The next revision, c01, makes that scope explicit while
preserving the reporting checks. All three search-time executions follow the intended scope and
pass. As in Gravitational Wave Detection, the revision places an existing requirement where the
agent needs to apply it (Appendix I.1).
Later runs guide new revisions of earlier skill versions. Revisiting a saved bundle gives its next
edit access to executions unavailable when the bundle was created. Paratransit illustrates the return to
an earlier parent: the search reselects d06 from generation three after evaluating its generation-four
children. Its generation-ﬁve child f08 becomes the ﬁnal bundle, raising Mini from 0.0% to 33.3%
(Figure 4c). Wyckoff also shows how later execution evidence informs the new edit (Figure 4d;
Appendix H): the search returns to the original bundle in generation three and uses b06’s ﬁrst-
generation execution to make ﬁle-based analysis and structured output requirements explicit in d08.
A new execution follows that guidance, and d08’s generation-four child e03 becomes the ﬁnal
bundle, raising Mini’s independent ﬁnal reward from 75.7% to 100.0%.
Skill instructions shrink and scripts grow on average. Across the 41 modiﬁed tasks, SKILL.md
ﬁles shrink by 35.0 lines per task on average, support scripts grow by 74.0 lines, and 18 scripts are
added. Total source length increases by 1.5% (Table 13). Erlang SSH (Appendix I) compresses a
485-line guide into a 31-line task procedure with perfect ﬁnal scores for both Mini and Luna.
4.4 C ROSS -MODEL REUSE
Mini’s skills raise stronger models’ average rewards. On the 41 modiﬁed tasks, frozen Mini-
developed bundles raise Luna from 63.9% to 74.4% (+10.5 pp), with both conditions evaluated after
freezing. GPT-5.5 scores 71.1% against its published original-skill reference of 60.5% (+10.6 pp).
The two models improve on six shared tasks and on 20 distinct tasks in total (Appendix C).
Across all 86 tasks, Luna rises from 67.3% to 71.9%. Modiﬁed bundles contribute +5.0 pp to this
aggregate, while separately re-executed unchanged bundles contribute -0.4 pp. On the 41 modiﬁed
tasks, Luna has 11 gains, 23 ties, and seven losses.
Mini’s skills help stronger models even when Mini still makes errors. Mini stays below 100.0%
on six of Luna’s 11 improved tasks. Table 3 shows how four executors satisfy different requirements
with identical frozen bundles. In Software Dependency Audit, original-skill Mini and Luna scan
beyond production dependencies. With the revised skill, all ﬁnal executions follow the intended
9

Preprint version
scope. Mini rises from 0.0% to 66.7% despite a remaining output-ﬁeld failure, while Luna, GPT-5.4,
and GPT-5.5 reach a mean task reward of 100.0%.
Sales Pivot Analysis reveals complementary difﬁculties (Appendix F.1). Final Mini executions sat-
isfy state-value checks, but two omit Excel pivot objects; original-skill Luna builds pivots but in-
cludes an excluded category. The evolved skill speciﬁes operation order and intermediate checks.
Luna adapts the abbreviated whitelist example to the input’s full state names and passes both state-
value and pivot-object checks. In one successful execution, Luna saves, reopens, and checks the
source sheet before adding pivots. A later call to the bundled helper fails because a dependency is
missing, but the workbook already produced passes veriﬁcation with full reward.
Models can still misread input images or leave required output ﬁles unsaved. In JPG OCR
Statistics, Luna writes correctly structured workbooks but misreads receipt month tokens; the revised
parsing rules leave the perception error unresolved. In Paratransit Routing, two GPT-5.5 executions
ﬁnd and check better feasible solutions but fail to save them as the required output. Appendix F
provides these receiver execution records.
5 C ONCLUSION
SkillNEO separates the skill version used for deployment from the versions kept for further de-
velopment, using comparative execution evidence to guide their revision. The recorded searches
show why this distinction matters. Partially repaired bundles lead to later deployed descendants,
and branches with lower overall reward contribute working procedures to other revisions. On Skills-
Bench, development using GPT-5.4 Mini alone raises its average reward into GPT-5.5 and Luna’s
original-skill range. The frozen bundles also beneﬁt stronger executors on the same tasks. These
ﬁndings connect the value of an intermediate version to the further repairs and procedures it makes
possible. Future work should test the evolved skills on new instances within their intended task
scope and study how to accumulate their improvements in a shared skill library.
REFERENCES
Lakshya A Agrawal, Shangyin Tan, Dilara Soylu, Noah Ziems, Rishi Khare, Krista Opsahl-Ong, Ar-
nav Singhvi, Herumb Shandilya, Michael J Ryan, Meng Jiang, Christopher Potts, Koushik Sen,
Alexandros G. Dimakis, Ion Stoica, Dan Klein, Matei Zaharia, and Omar Khattab. GEPA: Re-
ﬂective prompt evolution can outperform reinforcement learning. In The F ourteenth International
Conference on Learning Representations, 2026.
Salaheddin Alzubi, Noah Provenzano, Jaydon Bingham, Weiyuan Chen, and Tu Vu. EvoSkill:
Automated skill discovery for multi-agent systems. arXiv preprint arXiv:2603.02766, 2026.
Hans-Georg Beyer and Hans-Paul Schwefel. Evolution strategies – a comprehensive introduction.
Natural Computing, 1(1):3–52, mar 2002. doi: 10.1023/A:1015059928466.
Y uan Chang and Xiaoqi Chen. Naive prompt optimization: Rethinking the need for complex prompt
search. arXiv preprint arXiv:2608.27266, 2026.
Chrisantha Fernando, Dylan Sunil Banarse, Henryk Michalewski, Simon Osindero, and Tim Rock-
täschel. Promptbreeder: Self-referential self-improvement via prompt evolution. In Proceedings
of the 41st International Conference on Machine Learning , volume 235 of Proceedings of Ma-
chine Learning Research, pp. 13481–13544. PMLR, 2024.
Haowen Gao, Haoran Chen, Can Wang, Shasha Guo, Liang Pang, Zhaoyang Liu, Huawei Shen, and
Xueqi Cheng. SkillAudit: Ground-truth-free skill evolution via paired trajectory auditing. arXiv
preprint arXiv:2606.14239v1, 2026.
Yiming Gao, Zhen Wang, Jefferson Chen, Mark Antkowiak, Mengzhou Hu, JungHo Kong, Dexter
Pratt, Jieyuan Liu, Enze Ma, Zhiting Hu, and Eric P . Xing. scPilot: Large language model reason-
ing toward automated single-cell analysis and discovery. In The Thirty-ninth Annual Conference
on Neural Information Processing Systems , 2025.
Shibo Hao, Yi Gu, Haodi Ma, Joshua Jiahua Hong, Zhen Wang, Daisy Zhe Wang, and Zhiting
Hu. Reasoning with language model is planning with world model. In Proceedings of the 2023
10

Preprint version
Conference on Empirical Methods in Natural Language Processing , pp. 8154–8173. Association
for Computational Linguistics, 2023. doi: 10.18653/v1/2023.emnlp-main.507.
Shibo Hao, Yi Gu, Haotian Luo, Tianyang Liu, Xiyan Shao, Xinyuan Wang, Shuhua Xie, Haodi
Ma, Adithya Samavedhi, Qiyue Gao, Zhen Wang, and Zhiting Hu. New evaluation, library, and
analysis of step-by-step reasoning with large language models. In First Conference on Language
Modeling, 2024.
Zhengding Hu, Mingge Lu, Zhen Wang, Jixuan Ruan, Chang Chen, Zaifeng Pan, Y ue Guan,
Ruiyi Wang, Zhongkai Y u, Chao Zhang, and Y ufei Ding. FlashEvolve: Accelerating agent self-
evolution with asynchronous stage orchestration. arXiv preprint arXiv:2605.08520, 2026.
Y anna Jiang, Delong Li, Haiyu Deng, Baihe Ma, Xu Wang, Qin Wang, and Guangsheng Y u. SoK:
Agentic skills – beyond tool use in LLM agents. arXiv preprint arXiv:2602.20867, 2026.
Haoxiang Kang and Ming Wen. SkillLift: Learning dense rubrics from sparse oracles for efﬁcient
skill evolution. arXiv preprint arXiv:2609.15396, 2026.
Xiangyi Li, Yimin Liu, Wenbo Chen, Bingran Y ou, Zonglin Di, Yifeng He, Shenghan Zheng, Ky-
oung Whan Choe, Jiankai Sun, Shuyi Wang, Chujun Tao, Binxu Li, Xuandong Zhao, Hejia Geng,
Xiaojun Wu, Junwei Zhou, Xiaokun Chen, Hanwen Xing, Y ubo Li, Qunhong Zeng, Di Wang,
Y uanli Wang, Roey Ben Chaim, Penghao Jiang, Haotian Shen, Luyang Kong, Xinyi Liu, Run-
hui Wang, Xuanqing Liu, Jiachen Li, Xin Lan, Y ueqian Lin, Wengao Y e, Junwei He, Songlin
Li, Y ue Zhang, Yipeng Gao, Yijiang Li, Ze Ma, Liqiang Jing, Tianyu Wang, Kaixin Li, Yiqi
Xue, Haoran Lyu, Yizhuo He, Y uchen Tian, Shutong Wu, Bowei Wang, Yixuan Gao, Bo Chen,
Litong Liu, Sikai Cheng, Jiajun Bao, Shuaicheng Tong, Shuwen Xu, Terry Y ue Zhuo, Tinghan
Y e, Qi Qi, Miao Li, Longtai Liao, Zelin Tan, Chang Shi, Xilin Tang, Srinath Tankasala, Bo-
qin Y uan, Y aoyao Qian, Jianhong Tu, Chenguang Wang, Yizhou Sun, Wei Wang, Aaron Taylor,
Ziyue Y ang, Changkun Guan, Zhikang Dong, Xinyu Zhang, Steven Dillmann, Han chung Lee,
and Dawn Song. SkillsBench: Benchmarking how well agent skills work across diverse tasks.
arXiv preprint arXiv:2602.12670, 2026.
Huawei Lin, Peng Li, Jie Song, Fuxin Jiang, and Tieying Zhang. MUSE-Autoskill: Self-
evolving agents via skill creation, memory, management, and evaluation. arXiv preprint
arXiv:2605.27366v2, 2026a.
Tianyi Lin, Chuanyu Sun, Jingyi Zhang, Changxu Wei, Huanjin Y ao, Shunyu Liu, Xikun Zhang, Liu
Liu, and Jiaxing Huang. OpenClaw-Skill: Collective skill tree search for agentic large language
models. arXiv preprint arXiv:2606.16774, 2026b.
Jieyuan Liu, Mengzhou Hu, Jefferson Chen, JungHo Kong, Pratibha Jagannatha, Yiming Gao, Dex-
ter Pratt, Hsin-Y uan Lee, Zhiting Hu, Trey Ideker, Wei Wang, Eric P . Xing, and Zhen Wang. Hy-
poEvolve: Genetic algorithms enable multi-agent LLMs to discover scientiﬁc hypotheses. arXiv
preprint arXiv:2609.15938, 2026.
Enze Ma, Y ufan Zhou, Wei-Chieh Huang, Jie Y ang, Huanhuan Ma, Zixuan Wang, Chengze Li,
Chunyu Miao, Philip S. Y u, and Zhen Wang. MemAudit: Auditing long-term agent memory via
hidden user-state recovery. arXiv preprint arXiv:2606.24595, 2026.
Jingwei Ni, Yihao Liu, Xinpeng Liu, Y utao Sun, Mengyu Zhou, Pengyu Cheng, Dexin Wang, Er-
chao Zhao, Xiaoxi Jiang, and Guanjun Jiang. Trace2Skill: Distill trajectory-local lessons into
transferable agent skills. arXiv preprint arXiv:2603.25158, 2026.
Pietro S Oliveto, Tiago Paixão, Jorge Pérez Heredia, Dirk Sudholt, and Barbora Trubenová. How to
escape local optima in black box optimisation: When non-elitism outperforms elitism. Algorith-
mica, 80(5):1604–1633, 2018.
OpenAI. Codex CLI, 2026a. Software documentation. Accessed September 17, 2026.
OpenAI. GPT-5.4 Mini model, 2026b. API model documentation. Accessed September 12, 2026.
11

Preprint version
Reid Pryzant, Dan Iter, Jerry Li, Yin Tat Lee, Chenguang Zhu, and Michael Zeng. Automatic
prompt optimization with "gradient descent" and beam search. In Proceedings of the 2023 Con-
ference on Empirical Methods in Natural Language Processing , pp. 7957–7968. Association for
Computational Linguistics, 2023. doi: 10.18653/v1/2023.emnlp-main.494.
Y anwei Ren, Haotian Zhang, Likang Xiao, Jiaxing Huang, Jiayan Qiu, Baosheng Y u, Quan Chen,
and Liu Liu. Branch2Skill: Efﬁcient skill evolution through reasoning trees. arXiv preprint
arXiv:2608.08677, 2026.
Y ash Priya Shastri, Anand Eswaran, Adnan Qidwai, Pankaj Thorat, and Sachin Joshi. BONSAI:
Evolvability-guided tree search over skills. arXiv preprint arXiv:2608.07056, 2026.
Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, and Shunyu Y ao. Reﬂexion:
language agents with verbal reinforcement learning. In Thirty-seventh Conference on Neural
Information Processing Systems, 2023.
Somanshu Singla, Zhen Wang, Tianyang Liu, Abdullah Ashfaq, Zhiting Hu, and Eric P . Xing. Dy-
namic rewarding with prompt optimization enables tuning-free self-alignment of language mod-
els. In Y aser Al-Onaizan, Mohit Bansal, and Y un-Nung Chen (eds.), Proceedings of the 2024
Conference on Empirical Methods in Natural Language Processing , pp. 21889–21909, Miami,
Florida, USA, November 2024. Association for Computational Linguistics. doi: 10.18653/v1/
2024.emnlp-main.1220.
Rui Sun, Zhi Zheng, Zhenkun Wang, and Zhichao Lu. GraphSkillEvo: Evolutionary optimization
of graph-structured agent skills. arXiv preprint arXiv:2609.21749, 2026.
Shangyin Tan, Lakshya A Agrawal, Rohit Sandadi, Dan Klein, Koushik Sen, Alexandros G. Di-
makis, and Matei Zaharia. Automatically learning skills for coding agents. GEPA Blog, Feb
2026.
Guanzhi Wang, Y uqi Xie, Y unfan Jiang, Ajay Mandlekar, Chaowei Xiao, Y uke Zhu, Linxi Fan,
and Anima Anandkumar. V oyager: An open-ended embodied agent with large language models.
arXiv preprint arXiv:2305.16291, 2023.
Peihao Wang, Ruisi Cai, Zhen Wang, Hongyuan Mei, Qiang Liu, Pan Li, and Zhangyang Wang.
∇-Reasoner: LLM reasoning via test-time gradient descent in latent space. In The F ourteenth
International Conference on Learning Representations , 2026a.
Xinyuan Wang, Zhen Wang, Chenxi Li, Fan Bai, Haotian Luo, Jiayou Zhang, Nebojsa Jojic, Eric
Xing, and Zhiting Hu. PromptAgent: Strategic planning with large language models enables
expert-level prompt optimization. In The Twelfth International Conference on Learning Repre-
sentations, 2024.
Zefeng Wang, Minxi Y an, Jinhe Bi, Sikuan Y an, V olker Tresp, and Y unpu Ma. MetaSkill-Evolve:
Recursive self-improvement of LLM agents via two-timescale meta-skill evolution.arXiv preprint
arXiv:2607.05297, 2026b.
Zhen Wang, Fan Bai, Zhongyan Luo, Jinyan Su, Kaiser Sun, Xinle Y u, Jieyuan Liu, Kun Zhou,
Claire Cardie, Mark Dredze, Zhiting Hu, and Eric P . Xing. FIRE-Bench: Evaluating AI agents
on the rediscovery of scientiﬁc insights. In F orty-third International Conference on Machine
Learning, 2026c.
Zora Zhiruo Wang, Jiayuan Mao, Daniel Fried, and Graham Neubig. Agent Workﬂow Memory. In
Proceedings of the 42nd International Conference on Machine Learning, volume 267 of Proceed-
ings of Machine Learning Research , pp. 63897–63911. PMLR, 2025.
Peng Xia, Jianwen Chen, Hanyang Wang, Jiaqi Liu, Kaide Zeng, Y u Wang, Siwei Han,
Yiyang Zhou, Xujiang Zhao, Haifeng Chen, Zeyu Zheng, Cihang Xie, and Huaxiu Y ao.
SkillRL: Evolving agents via recursive skill-augmented reinforcement learning. arXiv preprint
arXiv:2602.08234v2, 2026.
Siheng Xiong, Ali Payani, Oguzhan Gungordu, and Faramarz Fekri. DIVE: Unlocking self-
improvement in frozen language models through diversity-driven skill evolution. arXiv preprint
arXiv:2608.12486, 2026.
12

Preprint version
Chengrun Y ang, Xuezhi Wang, Yifeng Lu, Hanxiao Liu, Quoc V . Le, Denny Zhou, and Xinyun
Chen. Large language models as optimizers. In The Twelfth International Conference on Learning
Representations, 2024.
Yifan Y ang, Ziyang Gong, Weiquan Huang, Qihao Y ang, Ziwei Zhou, Zisu Huang, Y an Li, Xuemei
Gao, Qi Dai, Bei Liu, Kai Qiu, Y uqing Y ang, Dongdong Chen, Xue Y ang, and Chong Luo.
SkillOpt: Executive strategy for self-evolving agent skills. arXiv preprint arXiv:2605.23904,
2026.
Haoran Y e, Xuning He, Vincent Arak, Haonan Dong, and Guojie Song. Meta context engineer-
ing via agentic skill evolution. In Proceedings of the 43rd International Conference on Ma-
chine Learning, volume 306 of Proceedings of Machine Learning Research, pp. 148325–148368.
PMLR, 2026.
Simon Y u, Gang Li, Weiyan Shi, and Peng Qi. PolySkill: Learning generalizable skills through
polymorphic abstraction for continual learning. In The F ourteenth International Conference on
Learning Representations, 2026a.
Xinle Y u, Fan Bai, Kaiser Sun, Hengshuo Miao, Abhay Anand, Zhongyan Luo, Kun Zhou, and
Zhen Wang. PrimeScientist: Strategic allocation of research effort in autonomous research. arXiv
preprint arXiv:2609.17846, 2026b.
Genrui Zhang, Erle Zhu, Jinfeng Zhou, Caiyan Jia, and Hongning Wang. SkillEvolver: Skill learning
as a meta-skill. arXiv preprint arXiv:2605.10500, 2026a.
Hanrong Zhang, Shicheng Fan, Henry Peng Zou, Y ankai Chen, Zhenting Wang, Jiayu Zhou,
Chengze Li, Wei-Chieh Huang, Yifei Y ao, Kening Zheng, Xue (Steve) Liu, Xiaoxiao Li, and
Philip S. Y u. CoEvoSkills: Self-evolving agent skills via co-evolutionary veriﬁcation. arXiv
preprint arXiv:2604.01687, 2026b.
Haozhen Zhang, Quanyu Long, Jianzhu Bao, Tao Feng, Weizhi Zhang, Haodong Y ue, and Wenya
Wang. MemSkill: Learning and evolving memory skills for self-evolving agents. arXiv preprint
arXiv:2602.02474, 2026c.
Jenny Zhang, Shengran Hu, Cong Lu, Robert Lange, and Jeff Clune. Darwin Gödel Machine:
Open-ended evolution of self-improving agents. In The F ourteenth International Conference on
Learning Representations, 2026d.
Qizheng Zhang, Changran Hu, Shubhangi Upasani, Boyuan Ma, Fenglu Hong, V amsidhar Kama-
nuru, Jay Rainton, Chen Wu, Mengmeng Ji, Hanchen Li, Urmish Thakker, James Zou, and Kunle
Olukotun. Agentic context engineering: Evolving contexts for self-improving language models.
In The F ourteenth International Conference on Learning Representations, 2026e.
Andrew Zhao, Daniel Huang, Quentin Xu, Matthieu Lin, Y ong-Jin Liu, and Gao Huang. ExpeL:
LLM agents are experiential learners. In Proceedings of the AAAI Conference on Artiﬁcial Intel-
ligence, volume 38, pp. 19632–19642, 2024. doi: 10.1609/aaai.v38i17.29936.
Boyuan Zheng, Michael Y . Fatemi, Xiaolong Jin, Zora Zhiruo Wang, Apurva Gandhi, Y ueqi Song,
Y u Gu, Jayanth Srinivasa, Gaowen Liu, Graham Neubig, and Y u Su. SkillWeaver: Web agents
can self-improve by discovering and honing skills. arXiv preprint arXiv:2504.07079, 2025.
Huichi Zhou, Siyuan Guo, Anjie Liu, Zhongwei Y u, Ziqin Gong, Bowen Zhao, Zhixun Chen, Men-
glong Zhang, Yihang Chen, Jinsong Li, Runyu Y ang, Qiangbin Liu, Xinlei Y u, Jianmin Zhou,
Na Wang, Chunyang Sun, and Jun Wang. Memento-Skills: Let agents design agents. arXiv
preprint arXiv:2603.18743, 2026a.
Y ang Zhou, Zihan Dong, Zhenting Wang, Can Jin, Shiyu Zhao, Bangwei Guo, Difei Gu, Linjun
Zhang, Mu Zhou, and Dimitris N. Metaxas. Evidence over plans: Online trajectory veriﬁcation
for skill distillation. arXiv preprint arXiv:2605.09192, 2026b.
13

Preprint version
A L IMITATIONS AND FUTURE DIRECTIONS
Understanding skill search. Our experiments evaluate the complete framework, and recorded his-
tories characterize how its development paths are used. Matched-budget comparisons are needed to
isolate the effects of non-elitist selection, comparative execution evidence, and cross-branch reuse.
Relevant selection policies include single-path reﬁnement, selection from the union of current par-
ents and children, and a persistent historical top- k frontier with the same number of parent slots.
Disabling archive revisitation would assess its contribution within each policy. Such comparisons
should use the same tasks, initial bundles, developer, veriﬁer, model-call budgets, and task-execution
budgets. Search currently stops after repeated deployment holds; future work could assess stopping
criteria that track progress across the development population.
Generalization beyond development tasks. We evaluate frozen bundles on the same tasks and
input instances used during development. Fresh executions measure performance on those instances
but do not establish generalization to unseen tasks or inputs. Future work should test whether these
procedures remain effective on new task variants.
Search and developer capability. Mini performs all model-based development roles in this study.
Extending the framework to developers with different capabilities and model families would help
establish how search depth and developer capability jointly shape skill improvement. A central
question is whether and when deeper search can compensate for limited developer capability, and
which capabilities remain necessary for productive skill development.
Developing shared skill libraries. SkillNEO evolves the bundle supplied for each task. A shared
library would need to accumulate improvements across tasks while managing interactions with pre-
viously learned procedures. Future work could study how to combine broadly useful procedures
with task-speciﬁc guidance and assess revisions across the tasks that depend on them.
B D EVELOPMENT PROTOCOL
Development starts from the skills supplied for each SkillsBench task ( Li et al., 2026), keeping their
SKILL.md documents and optional tools and resources together as a bundle. Harbor executes tasks;
SkillNEO compares traces, edits bundles, evaluates candidates, and selects versions.
The planned per-task conﬁguration requests six children, promotes up to three, measures each pro-
moted child and the incumbent over three repeats, and allows at most ﬁve generations. A full gen-
eration with six admitted children and three promotions contains six screening executions, six addi-
tional promoted-child executions, and three incumbent executions. Search width counts candidate
bundles and is distinct from execution concurrency.
B.1 S EARCH CONFIGURATION
With generation limit G, width b, promotion count k, and repeat count R, the complete planned
schedule contains R + G[b + k(R − 1) +R] task executions, giving 78 for (G, b, k, R) = (5 , 6, 3, 3).
Actual execution counts depend on the completed generations and measured candidates; proposal
and skill-editing calls and ﬁnal evaluations are separate. Algorithm 1 summarizes the loop.
The later-generation proposer chooses its primary parent from the eligible pool, with a per-parent
cap of ⌈b/|Bg−1|⌉+2. Graft donors are drawn from the same eligible pool, while execution evidence
used for diagnostic comparisons also includes screening-only candidates. Diagnostic summaries in-
clude up to four bundle versions from each end of the ranking. The later-generation prompt lists edit
directions previously measured as net losses and asks the Proposer to avoid closely similar direc-
tions with the same operator and target skill. This proposal-level constraint leaves parent eligibility
to Equation 4 and the archive rules below.
Operators include rewriting, extending, pruning, removing, rerouting, adding executable support,
and grafting from an eligible donor. Every child retains one primary parent edge, including grafted
children. Output checks and deduplication can reduce the requested six children to fewer distinct
bundles. Under conﬁguration ϕ, the edit-admission check is Ct,ϕ(Lp(v), Lv, av); its constraints and
repair paths appear in Appendix B.2.
Execution feedback. The Proposer combines a ﬁxed prompt template with agent-visible traces,
rewards, and ﬁltered veriﬁer ﬁndings. Feedback ﬁltering and candidate-content checks address
14

Preprint version
Algorithm 1 SkillNEO uses non-elitist replacement and comparative execution evidence.
Require: Task t, frozen actor Am, original L0; b = 6, k = 3, R = 3, G = 5
Require: Deployment conﬁguration θ (including δoﬀ , δaux), validation conﬁguration ϕ, archive ﬂag
1: Evaluate root 0 on R repeats; initialize tree, h0← 0, B0←{ 0}, z← 0, gstop← 0
2: if root is measured-perfect then return L0
3: for g = 1, . . . , G do
4: Assemble root evidence ( g = 1) or previous-population and saved execution evidence
5: Proposer speciﬁes b edits from Bg−1; Skill Editor materializes candidate bundles
6: Apply Edit V alidationCt,ϕ and permitted repairs; discard rejected drafts
7: Save distinct admitted survivors Dg and their edit edges
8: Screen Dg once; rank complete children by single-execution reward
9: if fewer than two children have complete screening records then
10: Interrupt with hg−1, Bg−1, z unchanged; resume generation g after completion
11: end if
12: Promote up to k top-ranked screened children
13: Add repeats 2:R to promoted children; measure hg−1 on R fresh repeats
14: Check task, model, environment, and veriﬁer consistency
15: Rank complete R-execution means, including screening for promoted children
16: if the incumbent has no complete comparison record then
17: hg← highest-ranked complete bundle
18: else
19: c← highest-ranked child; h← hg−1
20: d← Sg(c)− Sg(h); a← Ag(c)− Ag(h)
21: w← [d > δ oﬀ ]∨ [d = 0 ∧ a > δ aux]
22: hg← c if w and Acceptθ(c, h; Qg, E≤g) = 1 ; otherwise hg← h
23: end if
24: gstop← g
25: z← 0 if a new child is deployed; otherwise z← z + 1
26: Bg← Bord g from Equation 4
27: On an enabled negative H OLD , use eligible archive survivors with R repeats ﬁrst, then thinner records
28: If archive revisit ﬁnds no survivor, retain the ordinary set or stop if it is also empty
29: Append measured root if absent and|Bg| < 2
30: if z≥ 2 or (z≥ 1∧ 100− Sg(hg) < δ oﬀ ) then break
31: end for
32: return Lhgstop ▷ Deployment incumbent
evaluator-private answer material; public task requirements and observed behavior guide revisions.
Appendix B.2 speciﬁes these checks.
Screening and repeated evaluation. For bundle Lv, the mean reward over a nonempty execution
batch Q with outcomes yv,q is
bJv(Q) = 1 |Q| X q∈Q Vt(yv,q ). (6)
The execution batch Q identiﬁes the runs used in each comparison. The root is measured on three
repeats and becomes the ﬁrst incumbent; search stops if all three receive perfect reward. Otherwise,
every admitted child receives one screening execution. Infrastructure failures are separated from
ofﬁcial timeouts, memory limits, and veriﬁer failures. Incomplete records do not enter the ranking.
Screening ranks children by their single-execution ofﬁcial reward, using compatible auxiliary scores
to break ties. Promotion requires at least two children with complete screening records. If fewer
are available, execution of the generation is interrupted without a deployment decision or a hold-
count update. The saved incumbent and parent set are retained, and the same generation can resume
after the missing screening measurements are completed. Up to three top-ranked complete children
retain their screening measurement and receive repeats two and three; their resulting three-execution
means determine the deployment ranking. The incumbent receives three fresh repeats interleaved
in the same comparison batch without using a promotion slot. Deployment compares only fully
replicated records with matching task, model, environment, and veriﬁer settings.
Deployment acceptance. For the best fully measured child cg, deployment updates as
hg =
cg, Acceptθ(cg, hg−1; Qg, E≤g) = 1 ,
hg−1, otherwise (H OLD ), (7)
15

Preprint version
where Qg = ( Qg,v )v records the execution batch for each compared node and E≤g collects saved
development evidence. The deployment conﬁguration θ speciﬁes the improvement margins and
historical-score checks. These evidence arguments are suppressed below.
Write Sg(v) for a bundle’s ofﬁcial mean reward in the current comparison batch and Ag(v) for
its auxiliary score, both on a scale from 0 to 100. Candidates rank ﬁrst by Sg, then by Ag. The
auxiliary score uses the percentage of passed veriﬁer tests only when the compared evaluations have
compatible test coverage; otherwise it uses ofﬁcial reward. The incumbent wins an exact tie on both
scores; candidate ties use a deterministic tie-break.
Let c be the highest-ranked fully measured child and h the incumbent. For the current decision, write
S(v) = Sg(v), A(v) = Ag(v), ∆S = S(c) − S(h), and ∆A = A(c) − A(h). For the strict-ﬂoor
rule, let Pg(v) be the mean ofﬁcial reward on the 0–100 scale over saved executions of bundle v
in this task search, up to and including the current comparison batch. This pool includes its child
evaluations, subsequent incumbent re-evaluations, and root initialization where applicable. Records
sharing an execution identiﬁer are ﬁrst averaged, so each distinct execution contributes once. At
each deployment decision, recompute Fg as the maximum available Pg(v) for v ∈ {0, h}; if neither
pooled score is available, set Fg = −∞. The strict-ﬂoor acceptance rule uses improvement margins
δoﬀ and δaux for ofﬁcial and auxiliary scores and accepts a child according to
Acceptθ(c, h) = 1

S(c) > F g ∧

∆S > δ oﬀ ∨ (∆S = 0 ∧ ∆A > δ aux)

. (8)
The improvement margins are conﬁgurable, with defaults δoﬀ = 0 and δaux = 30 pp. The auxiliary
margin limits incumbent replacement due to small auxiliary-score ﬂuctuations when ofﬁcial scores
tie. Without a complete incumbent batch, selection uses the highest-ranked fully measured bundle.
Developmental selection and archive revisit. Ordinary parent selection takes the top k fully mea-
sured current-generation children whose complete bundles remain available, excluding the incum-
bent’s repeat-evaluation entries. The previous parent pool does not enter this ranking, so its best
member need not remain eligible. Neither parent-relative improvement nor acceptance for deploy-
ment is required. Rejected drafts and deduplicated bundles cannot become parents. If fewer than
two parents remain after selection, the measured root is added if absent.
When enabled, archive revisit activates on a H OLD with ∆S < 0. It retires fully measured children
that score below the incumbent. It also retires a parent if that parent has an available score in the
same comparison and all of its evaluated children score below that parent. Archive candidates are
unretired nodes with no children remaining after deduplication and retirement. Eligible survivors
with R repeats are ranked ﬁrst by ofﬁcial score. If that tier is empty, the remaining measured
survivors form the fallback tier. If no archive survivor exists, selection uses the ordinary parent set
when available; otherwise search stops as exhausted. The measured root is then added if fewer than
two parents remain and it is absent. This revisit occurs in nine decisions across seven tasks. Seven
decisions use fully repeated survivors, and two use one-repeat fallback candidates.
Stopping. Search returns the root if its initial measurements are perfect. Deployment updates reset
the hold counter; holds increment it. Search stops after two consecutive holds, after a hold with
100 − Sg(hg) < δ oﬀ , at the generation limit, or on archive exhaustion.
B.2 C ANDIDATE CONSTRUCTION AND CHECKS
Edit V alidation programmatically checks operation constraints, referenced ﬁles, new scripts, and
introduced content. Fixable failures return to the Skill Editor; evaluation uses only admitted bundles.
The Proposer receives public instructions, agent-visible execution evidence, ofﬁcial rewards, and
ﬁltered evaluator ﬁndings. The Skill Editor receives the edit speciﬁcation and current skill. Public
task requirements and agent-computed results can guide task-speciﬁc changes; the checks target
evaluator-private answers copied into deployed artifacts.
Before proposal generation, veriﬁer-text ﬁltering removes comparison-shaped answer text and
known private literals. Redaction and rejection use reference material from test and speciﬁcation
ﬁles, excluding the reference solution. Where applicable, matching rules exclude public-instruction
vocabulary and imported API names.
After editing, new SKILL.md lines and added or replaced support ﬁles are checked for exact private
ﬁve-word sequences, normalized lines, literals, and distinctive identiﬁers. When a match triggers re-
jection, the Skill Editor receives a generic message without the matched answers. Fixable rejections
16

Preprint version
permit one revision; a missing promised executable permits an additional repair limited to that ﬁle.
Repaired artifacts are checked again, and rejected children do not enter evaluation.
A conﬁgurable content heuristic uses default rejection thresholds of 20 new bare numeric entries,
or six new entries on lines containing values with at least four decimal places. V alidation also
checks for instructions that depend on unavailable grader messages and missing promised helper
ﬁles. Script checks execute Python helpers and check syntax for other supported languages. Text-
only revisions do not require a helper check. Broader grounding or skill-routing concerns may be
reported without rejecting the candidate.
These checks target newly introduced content and speciﬁed matching patterns. Admitted bundles
are then executed and scored by the task veriﬁer.
Table 4: No-skill and original-skill references. Original skills increase average reward in each listed
conﬁguration on the aligned 86 tasks. Rewards are percentages and ∆ is in percentage points.
Ofﬁcial rows are reaggregated from the published per-task registry. Differences are computed from
the displayed means. No Luna no-skill result has been measured.
Model / agent No skill Original skill ∆
Mini / OpenHands (ofﬁcial) 29.9 40.7 +10.8
Mini / Codex high (this study) 39.1 49.1 +10.0
GPT-5.5 / OpenHands (ofﬁcial) 50.9 66.9 +16.0
GPT-5.5 / Codex (ofﬁcial) 46.2 66.1 +19.9
B.3 E VALUATION SETTINGS AND COMPARISON CONTEXT
Final evaluation uses the frozen task-bundle assignment and the model settings in Section 4.1.
Reference source. The ofﬁcial rows in Table 4 and the GPT-5.5 original-skill reference use the
published SkillsBench results, reaggregated over the 86 tasks. GPT-5.4’s 51.7% original-skill refer-
ence comes from V alsand uses 87 tasks, OpenHands, and xhigh reasoning. The +13.8 pp difference
between our 86-task Codex ﬁnal score and this reference compares different settings.
Table 5: Reported skill-development results on SkillsBench. Average rewards (%) use each study’s
task cohort and evaluation protocol. Human denotes each study’s human-skill reference; Developed
uses its resulting skills. SkillEvolver and CoEvoSkills instead report complete-pass frequencies.
SkillAudit, MUSE-Autoskill, and SkillNEO use the listed model for development and execution;
SPARK uses stronger-model teacher trajectories; SPARK’s scores follow Section 4.1 of the source.
SkillAudit and SkillNEO reﬁne supplied skills; MUSE-Autoskill and SPARK generate skills, with
Human as a separate reference. MUSE counts its 28 uncovered tasks as zero. SPARK describes an
86-task suite; exact Mini task alignment is unavailable. For SkillNEO, 41 modiﬁed bundles receive
new ﬁnal executions; 45 retained bundles share their original Mini measurements.
Study Executor Tasks Human Developed
SkillAudit (Gao et al., 2026) Opus 4.8 89 56.7 73.9
MUSE-Autoskill (Lin et al., 2026a) GPT-5.5 75 59.67 53.42
SPARK (Zhou et al., 2026b) GPT-5.4 Mini 86 ≈ 47 ≈ 52
SkillNEO (this study) GPT-5.4 Mini 86 49.1 66.4
Reported skill-development results on SkillsBench. Table 5 summarizes average reward reported
by three prior studies alongside our results. Reported averages are 66.4% for SkillNEO, 53.42% for
MUSE-Autoskill with GPT-5.5, and approximately 52% for Mini with SPARK skills, each under its
own task set and evaluation protocol. SkillAudit reports 73.9%, using Opus 4.8 for task execution,
PACE auditing, skill editing, and ﬁnal evaluation ( Gao et al. , 2026).
Comparative auditing and continued development. The studies also differ in how they develop
skills. MUSE-Autoskill creates skills from executions, and SPARK distills stronger-model trajecto-
ries. To repair supplied skills, SkillAudit ( Gao et al. , 2026) uses PACE to compare executions with
and without the current skill, combines these diagnostics with a ﬁxed structural veriﬁer, and can roll
back to the previous saved skill version. Its reported loop maintains one active skill state. SkillNEO
also develops supplied bundles with Mini and permits continued editing of children without parent-
relative improvement. Parent-child and sibling records organize evidence across revisions, and graft-
17

Preprint version
ing allows procedures from another saved branch to enter a candidate. These mechanisms preserve
alternatives both as starting points for further edits and as sources of useful procedures; Section 4.3
traces both uses in the recorded executions. SkillAudit excludes external task rewards during evolu-
tion, whereas SkillNEO uses benchmark rewards to evaluate candidates and select versions.
C A NALYSIS ACROSS RECEIVING MODELS
We analyze the three-repeat task means from the 86-task evaluation. The 41 modiﬁed tasks divide
into 29 Mini-positive and 12 Mini-tied tasks under the ±0.05 pp tie band; the other 45 tasks retain
their original bundles. These Mini-outcome subgroups are deﬁned by the ﬁnal evaluation results.
Table 6: Receiver rewards grouped by Mini’s outcome. GPT-5.5 and Luna have larger mean gains
on tasks where Mini improves than on tasks where Mini ties. Scores report average reward (%); Gap
is evolved minus original reward in percentage points. The 41 modiﬁed tasks are grouped post hoc
by Mini’s ﬁnal evaluation outcomes, using its ±0.05 pp display band. Evolved denotes the same
frozen Mini-developed bundle for each task. GPT-5.4 reports frozen-skill endpoints; original-skill
subgroup scores are not reported. Evaluation settings follow Section 4.1.
GPT-5.4 GPT-5.5 GPT-5.6 Luna
Mini outcome n Evolved Original Evolved Gap Original Evolved Gap
All modiﬁed 41 66.8 60.5 71.1 +10.6 63.9 74.4 +10.5
Mini improved 29 69.1 64.3 78.1 +13.8 62.8 81.0 +18.3
Mini tied 12 61.1 51.4 54.2 +2.8 66.7 58.3 -8.3
Reward by Mini outcome. Table 6 reports receiver rewards and their differences from available
original-skill references. In the Mini-improved group, GPT-5.5 and Luna gain 13.8 and 18.3 pp,
respectively. In the Mini-tied group, GPT-5.5 gains 2.8 pp while Luna loses 8.3 pp.
Why selected revisions can tie the original bundle in ﬁnal evaluation. Selection compares a
candidate with that generation’s incumbent, whereas ﬁnal evaluation compares the frozen bundle
with the original skill in separate execution batches. Both the reference bundle and observed reward
can therefore differ. Eleven of the 12 Mini-tied bundles were adopted with higher ofﬁcial reward
than the incumbent. Grid was adopted at 100 with a 33.3-point incumbent gap, while its ﬁnal original
and evolved scores were both 66.7.
The ﬁnal ties consist of four ceiling cases, three partial-score cases, and ﬁve zero-score cases. Perfect
original reward leaves no room for observed improvement; when both conditions yield zero reward,
neither resolves the recorded failures.
Absolute success and agreement. Among the 41 modiﬁed tasks, 14 achieve 100.0% average reward
with all three receivers, 15 with one or two, and 12 with none. Achieving 100.0% requires all three
saved repeats to receive full reward. Three tasks receive zero with all three receivers: Manufacturing
Codebook Normalization, Paratransit Routing, and Quantum Numerical Simulation. Comparisons
with original skills distinguish full reward from improvement for GPT-5.5 and Luna.
Table 7: Joint directions of receiver reward changes. Gains and losses need not coincide across
GPT-5.5 and Luna on the 41 modiﬁed tasks. Rows use GPT-5.5 reference differences; columns use
Luna differences from post-freeze evaluations. Both axes use the existing ±0.05 pp display band.
Original-skill reference sources appear in Appendix B.
GPT-5.5 direction Luna gain Luna tie Luna loss Total
Gain 6 6 3 15
Tie 4 13 1 18
Loss 1 4 3 8
Total 11 23 7 41
Direction depends on the receiving model and its comparison. Table 7 groups tasks by the
directions of their GPT-5.5 and Luna reward differences. Six tasks gain in both, while 20 gain in
at least one. Four have opposite nonzero signs. Civ6 Adjacency Optimizer, Grid Dispatch, and
Organize Messy Files decrease in both; Appendix F details each model’s failures.
18

Preprint version
Table 8: Contributions to Luna’s overall reward difference. Gains on modiﬁed tasks outweigh the
decrease on retained tasks. Rewards are percentages; ∆ and Full-set contribution are in percentage
points. The Mini-positive and Mini-tied subsets partition the 41 modiﬁed tasks. The 41 modiﬁed and
45 retained tasks partition the benchmark. Their contributions are n∆/86 and sum using unrounded
values. Mini-positive/tied strata are deﬁned post hoc from Mini’s ﬁnal evaluation outcomes.
Stratum n Original Evolved ∆ Full-set contribution
Modiﬁed skills 41 63.9 74.4 +10.5 +5.0
Mini positive subset 29 62.8 81.0 +18.3 +6.2
Mini tied subset 12 66.7 58.3 -8.3 -1.2
Original retained 45 70.4 69.6 -0.7 -0.4
Contributions to the full-cohort differences. Table 8 weights each subset’s mean reward difference
by its share of the 86 tasks. Luna’s modiﬁed and retained subsets contribute approximately +4.99
and −0.39 pp to the +4.60 pp aggregate gain; the retained subset’s own mean differs by −0.74
pp between separate original- and ﬁnal-assignment execution batches, although its skill bundles are
identical. GPT-5.5’s contributions of +5.05 and −1.55 pp yield a +3.50 pp difference.
Table 9: Luna transfer by observed original performance. Among the 41 modiﬁed tasks, the group
with zero original reward has the largest mean gain. Rewards are percentages, ∆ is in percentage
points, and G/T/L counts gains, ties, and losses with the ±0.05 pp display tolerance of Table 1.
Groups are deﬁned post hoc from Luna’s three original-skill repeats.
Original-performance stratum n Original Evolved ∆ G/T/L
Zero observed reward 8 0.0 50.0 +50.0 4/4/0
Partial observed reward 16 57.5 61.4 +3.9 7/3/6
Perfect observed reward 17 100.0 98.0 -2.0 0/16/1
To relate reuse gains to starting performance, Table 9 groups the 41 modiﬁed tasks by their observed
reward on Luna when using the original skills. Four of the eight tasks with zero original reward
improve and four tie. Outcomes are more mixed among the 16 tasks with partial original reward:
seven improve, three tie, and six lose reward. Of the 17 tasks with perfect original reward, 16 retain
perfect reward and one receives a lower reward.
D D OMAIN RESULTS
Mini improves in every domain, while Luna’s domain-level differences include gains and losses.
Table 2 reports Mini’s domain scores from Figure 3. Table 10 adds Mini and Luna differences on
the modiﬁed-task subsets and Luna’s full-domain differences.
Table 10: Domain-level improvement and transfer. Mini improves in every domain, while Luna
differences vary by domain. Differences are percentage points. All and Modiﬁed give task counts;
the modiﬁed-task and full-domain differences use their respective denominators.
Domain All Modiﬁed Mini mod. Luna mod. Luna all
Cybersecurity 7 4 +22.2 +44.4 +25.4
Finance / economics 9 4 +58.3 +25.0 +3.7
Industrial / physical 14 7 +11.3 -11.9 -10.7
Mathematics / formal 7 3 +41.1 -10.6 +0.2
Media / content 5 2 +33.3 +0.0 +13.3
Natural science 14 6 +42.9 +11.1 +9.5
Ofﬁce 14 6 +33.3 +11.1 -2.4
Software engineering 16 9 +48.7 +14.8 +10.4
19

Preprint version
D.1 R ESOLVED AND REMAINING WORKFLOW OBSTACLES
To contrast resolved and remaining workﬂow obstacles, we examine original and ﬁnal skills with
three Mini executions per condition for four tasks (24 executions).
Removing an execution barrier . In SimPO Code Reproduction, original executions log Python
3.12, violating the required version 3.10 and stopping veriﬁcation at the Python-version assertion.
Comparing the saved outputs separately shows that all original runs’ 100 loss values numerically
match those from passing ﬁnal executions. The evolved skill makes creating and activating the
required environment precede installation, logging, and testing. All ﬁnal executions use Python
3.10 and pass, raising reward from 0.0 to 100.0.
Data-to-D3 also rises from 0.0 to 100.0. Original executions write the required ﬁles and check syn-
tax, but do not perform browser or DOM interaction checks; all fail tooltip behavior. The evolved
skill explicitly requires checking the rendered page and linked interactions. All ﬁnal executions per-
form interaction checks (two with Chromium and one with jsdom) and pass all 15 tests. One check
reveals that repeated selection clears the selected row; the agent changes toggling to idempotent
selection before submission. The skill guides the agent’s construction of execution-time checks.
Failures can remain after a targeted edit. Adaptive Cruise Control rises from 33.3 to 66.7. Its
evolved skill requires checking fresh simulation outputs, but names a helper path that is unavailable
during execution. All ﬁnal runs implement their own checks. The remaining failed run checks
aggregate metrics but leaves emergency behavior absent, failing safety and scenario checks. The
bundled checker omits these conditions and cannot verify the complete controller.
Manufacturing Codebook Normalization exposes inconsistent rule application, with a ﬁnal reward
of 0.0. The revised rule requires component evidence in the raw segment for certain electrical-fault
labels. All ﬁnal runs read the skill, but the two completed runs also admit contextual test-item
evidence; one further replaces the required raw-text cue with a higher matching threshold. Both
retain mismatched component assignments and pass 15 of 16 tests, failing the remaining codebook
check based on lexical overlap. Another ﬁnal run times out without the required output.
E C OMPLETE TASK -L EVEL RESULTS
Table 11: Complete task-level rewards. Each row reports mean reward (%) on one of the 86 tasks. M denotes
modiﬁed bundles; R denotes byte-identical retained bundles. O/E denote original/ﬁnal assignments. Mini’s R
rows reuse the same original three-run score in both columns. Evaluation follows Section 4.1; Appendix B
identiﬁes the sources of the original-skill references.
Task Mini O Mini E 5.5 O 5.5 E Luna O Luna E
3d-scan-calc R 100.0 100.0 100.0 100.0 100.0 100.0
ada-bathroom-plan-repair R 33.3 33.3 100.0 100.0 100.0 100.0
adaptive-cruise-control M 33.3 66.7 33.3 100.0 66.7 100.0
azure-bgp-oscillation-route-leak R 0.0 0.0 0.0 0.0 0.0 0.0
citation-check R 100.0 100.0 100.0 100.0 100.0 100.0
civ6-adjacency-optimizer M 0.0 23.3 95.0 63.3 63.3 31.7
court-form-ﬁlling M 33.3 66.7 33.3 66.7 33.3 100.0
crystallographic-wyckoff-position-
analysis
M 75.7 100.0 100.0 100.0 100.0 100.0
dapt-intrusion-detection R 100.0 100.0 100.0 100.0 100.0 100.0
data-to-d3 M 0.0 100.0 33.3 100.0 0.0 0.0
debug-trl-grpo M 41.7 61.7 91.7 83.3 100.0 100.0
dialogue-parser M 83.3 83.3 83.3 83.3 100.0 100.0
drone-planning-control M 42.2 54.4 56.7 70.0 84.4 67.8
dynamic-object-aware-egomotion R 0.0 0.0 33.3 0.0 66.7 0.0
earthquake-phase-association R 66.7 66.7 100.0 100.0 100.0 100.0
earthquake-plate-calculation R 100.0 100.0 100.0 100.0 100.0 100.0
econ-detrending-correlation M 0.0 100.0 100.0 100.0 100.0 100.0
edit-pdf M 0.0 33.3 100.0 100.0 100.0 100.0
energy-ac-optimal-power-ﬂow R 100.0 100.0 100.0 100.0 100.0 100.0
energy-market-pricing M 66.7 100.0 33.3 66.7 66.7 0.0
energy-unit-commitment R 0.0 0.0 100.0 0.0 0.0 0.0
enterprise-information-search R 0.0 0.0 0.0 0.0 0.0 0.0
20

Preprint version
Task Mini O Mini E 5.5 O 5.5 E Luna O Luna E
exam-block-sequencing R 100.0 100.0 100.0 66.7 0.0 0.0
exceltable-in-ppt R 100.0 100.0 100.0 100.0 100.0 100.0
exoplanet-detection-period M 0.0 66.7 100.0 100.0 66.7 100.0
ﬁnancial-modeling-qa R 66.7 66.7 100.0 100.0 100.0 33.3
ﬁx-build-agentops M 66.7 100.0 66.7 66.7 100.0 100.0
ﬁx-build-google-auto R 0.0 0.0 0.0 66.7 66.7 33.3
ﬁx-druid-loophole-cve R 100.0 100.0 66.7 66.7 100.0 100.0
ﬁx-erlang-ssh-cve M 100.0 100.0 33.3 66.7 100.0 100.0
ﬁx-visual-stability R 100.0 100.0 33.3 0.0 66.7 100.0
ﬂink-query R 0.0 0.0 33.3 0.0 0.0 33.3
ﬂood-risk-analysis R 0.0 0.0 0.0 0.0 33.3 0.0
glm-lake-mendota R 100.0 100.0 0.0 100.0 100.0 100.0
gravitational-wave-detection M 0.0 100.0 100.0 100.0 100.0 100.0
grid-dispatch-operator M 66.7 66.7 66.7 33.3 66.7 0.0
hvac-control M 100.0 100.0 100.0 100.0 33.3 100.0
invoice-fraud-detection M 0.0 100.0 0.0 100.0 0.0 100.0
jax-computing-basics R 100.0 100.0 100.0 100.0 100.0 100.0
jpg-ocr-stat M 0.0 66.7 33.3 33.3 33.3 0.0
lab-unit-harmonization R 100.0 100.0 100.0 100.0 100.0 100.0
lake-warming-attribution M 66.7 100.0 66.7 33.3 66.7 100.0
latex-formula-extraction R 33.3 33.3 0.0 0.0 100.0 0.0
lean4-proof R 100.0 100.0 100.0 100.0 100.0 100.0
llm-preﬁx-cache-replay R 100.0 100.0 100.0 100.0 100.0 100.0
manufacturing-codebook-
normalization
M 0.0 0.0 0.0 0.0 0.0 0.0
manufacturing-equipment-
maintenance
R 33.3 33.3 100.0 66.7 66.7 100.0
manufacturing-fjsp-optimization R 0.0 0.0 33.3 0.0 100.0 66.7
mario-coin-counting M 100.0 100.0 0.0 100.0 100.0 100.0
mars-clouds-clustering M 33.3 66.7 100.0 100.0 100.0 100.0
multilingual-video-dubbing M 33.3 100.0 33.3 100.0 100.0 100.0
offer-letter-generator R 100.0 100.0 100.0 100.0 100.0 100.0
organize-messy-ﬁles M 0.0 0.0 100.0 33.3 66.7 0.0
paper-anonymizer M 0.0 33.3 100.0 100.0 100.0 100.0
parallel-tﬁdf-search M 33.3 100.0 100.0 100.0 66.7 100.0
paratransit-routing M 0.0 33.3 100.0 0.0 0.0 0.0
pddl-airport-planning M 33.3 100.0 66.7 100.0 100.0 100.0
pddl-tpp-planning R 100.0 100.0 100.0 100.0 33.3 66.7
pdf-excel-diff R 100.0 100.0 100.0 100.0 100.0 100.0
powerlifting-coef-calc R 100.0 100.0 100.0 100.0 100.0 100.0
pptx-reference-formatting R 100.0 100.0 100.0 100.0 100.0 100.0
protein-expression-analysis R 100.0 100.0 100.0 100.0 33.3 100.0
python-scala-translation M 0.0 100.0 33.3 100.0 0.0 100.0
quantum-numerical-simulation M 0.0 0.0 0.0 0.0 0.0 0.0
r2r-mpc-control M 100.0 100.0 66.7 100.0 100.0 66.7
radar-vital-signs R 66.7 66.7 100.0 100.0 66.7 100.0
react-performance-debugging M 66.7 66.7 66.7 33.3 66.7 66.7
reserves-at-risk-calc R 0.0 0.0 0.0 0.0 0.0 0.0
sales-pivot-analysis M 0.0 33.3 0.0 0.0 0.0 100.0
sec-ﬁnancial-report M 33.3 66.7 66.7 0.0 66.7 66.7
seismic-phase-picking R 33.3 33.3 100.0 100.0 100.0 100.0
setup-fuzzing-py M 0.0 22.0 55.3 83.0 5.3 83.0
shock-analysis-demand R 0.0 0.0 0.0 0.0 0.0 0.0
shock-analysis-supply M 0.0 0.0 0.0 0.0 66.7 66.7
simpo-code-reproduction M 0.0 100.0 0.0 100.0 100.0 100.0
software-dependency-audit M 0.0 66.7 66.7 100.0 0.0 100.0
spring-boot-jakarta-migration R 100.0 100.0 100.0 100.0 100.0 100.0
suricata-custom-exﬁl M 0.0 0.0 100.0 100.0 100.0 100.0
syzkaller-ppdev-syzlang R 100.0 100.0 100.0 100.0 100.0 100.0
threejs-structure-parser R 100.0 100.0 100.0 100.0 33.3 100.0
threejs-to-obj R 100.0 100.0 100.0 100.0 100.0 100.0
tictoc-unnecessary-abort-detection M 81.7 100.0 100.0 100.0 100.0 100.0
travel-planning R 100.0 100.0 100.0 100.0 100.0 100.0
21

Preprint version
Task Mini O Mini E 5.5 O 5.5 E Luna O Luna E
video-silence-remover R 0.0 0.0 0.0 0.0 0.0 0.0
weighted-gdp-calc R 100.0 100.0 100.0 100.0 100.0 100.0
xlsx-recover-data R 0.0 0.0 0.0 0.0 0.0 0.0
Table 11 reports the full 86-task comparison underlying the aggregate results. Each row corre-
sponds to one task and its complete collection of skills. A modiﬁed marker denotes an evolved
bundle; a retained marker denotes a byte-identical original bundle. Mini’s 41 modiﬁed bundles use
post-evolution ﬁnal executions. Its 45 retained rows represent the same skill conﬁguration in both
columns and use the same original three-run score. Together these rows describe the ﬁnal skill as-
signment for each task. Section 4.1 speciﬁes aggregation; Appendix B gives the reference sources.
F C ROSS -M ODEL EXECUTION ANALYSIS
We ﬁrst examine how evolved skills help receivers when the developer’s ﬁnal performance remains
imperfect, then analyze unresolved failures. The matched Luna comparison yields 11 gains, 23 ties,
and seven losses among the 41 modiﬁed tasks.
F.1 R EUSABLE WORKFLOW IMPROVEMENTS AND RECEIVER EXECUTION
On six of Luna’s 11 improved tasks, Mini’s ﬁnal mean reward is below 100.0. We examine Software
Dependency Audit and Sales Pivot Analysis through 33 executions: 24 with ﬁnal evolved skills, six
with original skills on Luna, and three original-skill Mini audit executions. For each task, the ﬁnal-
skill executions use the same frozen bundle across all four models. Both tasks use binary execution
rewards, so a mean of 33.3 or 66.7 denotes one or two successes out of three.
A shared workﬂow error is corrected, while a downstream failure remains. In the original-
skill evaluations, all three Mini executions and two of Luna’s three expand the scan to development
dependencies and report 22 ﬁndings. Luna’s remaining original execution keeps the intended scope
but truncates a ﬁx list. With the ﬁnal audit bundle, c01 (Appendix I.1), all 12 ﬁnal executions across
the four models keep the intended production scope and report three HIGH-severity ﬁndings. Mini
rises from 0.0 to 66.7, and Luna from 0.0 to 100.0. Mini’s failed ﬁnal execution writes an incorrect
CVSS score of 9.8; the source-priority rule requires 8.1. It also truncates a three-version ﬁx list to
one version. All three receivers preserve the required ﬁelds. The remaining Mini error concerns a
pre-existing ﬁeld rule, beyond the added row-count and record-key checks.
The receiver must apply the correction to the actual input. With the ﬁnal Sales Pivot bundle,
f07 (development in Appendix I.4), all Mini executions pass state validation, but two write sum-
mary tables without actual pivot objects. Luna’s original-skill executions create pivots but fail state
validation by retaining Other Territories . With the evolved bundle, Luna ﬁlters to the eight
full state and territory names in the input, excludes four out-of-scope records, and builds pivots over
the remaining 2,450 regions. Its executions satisfy both requirements. This requires adapting the
skill’s whitelist example, which still uses abbreviations such as NSW. GPT-5.4’s failed execution
uses those abbreviations; its two successes retain full names. GPT-5.5 builds pivots but retains the
excluded category in all three executions. These outcomes depend on adapting the guidance to the
input’s state representation and completing both requirements.
Reusable guidance can coordinate operations across saved artifacts. The ﬁnal Sales Pivot skill
also speciﬁes dependencies between operations: clean missing income markers before computing
quartiles, and write, save, reopen, and check the source sheet before attaching pivot objects. Mini’s
successful ﬁnal execution computes quartiles over valid income values and maps the labels back to
the merged data. Section 4.4 describes a successful Luna execution that follows the same sequence
of saving, reopening, and checking through its own builder.
F.2 U NRESOLVED FAILURES IN LUNA REUSE
For Luna’s seven loss tasks, we compare three original-skill and three evolved-skill executions per
task (42 total), together with the corresponding edits. Table 12 reports mean rewards.
Optimization and directory contracts. Energy and Grid each fall from two successes to none after
independently replacing demand Pd with Pd + Gs, motivated by passing development evidence. All
22

Preprint version
Table 12: Luna tasks with observed transfer losses. Seven modiﬁed tasks lose reward under evolved
bundles. V alues are mean rewards (%); Change (pp) uses unrounded measurements.
Task Original Evolved Change (pp)
Energy Market Pricing 66.7 0.0 −66.7
Grid Dispatch Operator 66.7 0.0 −66.7
Organize Messy Files 66.7 0.0 −66.7
Civ6 Adjacency Optimizer 63.3 31.7 −31.7
Drone Planning Control 84.4 67.8 −16.7
JPG OCR Statistics 33.3 0.0 −33.3
R2R MPC Control 100.0 66.7 −33.3
six evolved executions apply this rule and pass schema and feasibility checks, but fail cost optimality
in the high-cost direction. The benchmark uses Pd. The four passing original executions use Pd;
the remaining original execution of each task fails the cost check in the opposite direction. Passing
development evidence therefore did not establish that the revised demand rule was correct.
Organize also falls from two successes to none. Every evolved execution places correctly classi-
ﬁed documents in destinations below the source directory, /root/papers/all/. Its inventory,
manifest, and exact-once audits check the destination tree, whereas the veriﬁer treats documents
remaining below the source directory as unsorted leftovers. The failed original execution makes
the same choice, while the two passing ones use sibling destinations under /root/papers/. The
stronger self-check leaves source-directory clearance unspeciﬁed. For Mini, Energy improves, while
Grid and Organize tie their original-skill scores.
Saving the solution. Civ6’s zero-reward executions (one original and two evolved) ﬁnd competitive
legal layouts but continue enumeration without saving the required JSON before timeout. Two
other executions time out with valid outputs and receive 0.95 normalized adjacency reward. Missing
artifacts account for the loss; the submitted layouts remain competitive. The evolved workﬂow lacks
a requirement to save each new best layout before continuing. Its helper checks serialization and
supplied-score sums but omits the stated adjacency recomputation. The observed missing-output
failures occur before an artifact is available for that check.
Computation and perception. Drone’s three low-scoring executions use quintic proﬁles; three
high-scoring executions use clamped cubic interpolation. Although the task text permits broader
continuous trajectories, the original skill and oracle specify cubic interpolation. The mismatch be-
tween these quintic trajectories and the oracle’s cubic interpolation explains 13 common command
failures, including all failures in the low-scoring original execution. The revised skills target hover
and completion, but hover succeeds throughout, the cubic-planning skill is unchanged, and the re-
vision does not resolve the choice between these planners. Scoring counts successful commands
individually, so all enclosing pytest groups pass even at low reward.
JPG workbooks cover all 22 receipts with correct structure and monetary values. Five failed exe-
cutions misread one or two month tokens on the same receipts across conditions; the errors do not
involve swapping day and month. Replacing multi-pass guidance with deterministic parsing leaves
perception errors despite image review; parsing cannot verify recognition accuracy.
The only failed R2R execution passes the structure, linearization, safety, and local artifact checks,
but fails the veriﬁer’s settling-time test. The agent’s local settling-time metric uses an all-channel
absolute-error band and a post-step time origin; the veriﬁer uses the changed roller’s band relative
to reference-step magnitude and the logged starting time. These metric conventions also differ
in passing executions under both skill conditions; the task speciﬁes a settling target without fully
deﬁning the measurement convention. Applying the veriﬁer’s rule to the failed execution’s saved
log reproduces its settling-time failure.
Saturation and unresolved tasks. Beyond these seven loss cases, the 23 tied tasks comprise 16
perfect, four zero, and three partial comparisons with two successes per condition. The zero ties are
Data-to-D3, Paratransit Routing, Manufacturing Codebook Normalization, and Quantum Numerical
Simulation; only the ﬁrst two improved on Mini. The partial ties are React Performance Debugging,
SEC Financial Report, and Shock Analysis Supply; only SEC improved on Mini. Perfect ties leave
no room for observed gains; other ties include failures under both skill conditions.
23

Preprint version
F.3 A DDITIONAL RECEIVER EVIDENCE
Shared tasks, different failures. GPT-5.5 also loses reward on Grid, Organize, and Civ6. Grid
has two failures at a 0.0111% cost gap against a 0.01% limit, yet every execution reads Pd + Gs,
including the passing one. That instruction alone does not determine reward. Organize’s failed
executions misclassify one paper; only one also violates directory clearance, and another execution
passes. Civ6 has one missing-output timeout and two 0.95 outcomes, showing the same checkpoint
weakness with a different frequency.
Saving an improved solution. All three Paratransit GPT-5.5 executions time out, submitting reports
serving 0, 440, and 442 trips against a minimum of 443. Two ﬁnd and locally check better feasible
reports under other ﬁlenames but fail to save them as the graded output. The remaining execution
continues optimization after saving a below-threshold report. These executions expose the need to
save the best available solution as the graded output.
Answer and execution checks. GRPO’s two 0.75 GPT-5.5 outcomes fail only the epsilon source-
pattern check. Their patches bind a named constant to 10−4, whereas the veriﬁer requires the denom-
inator to contain std_grouped_rewards plus an inline numeric literal. The passing execution
uses that literal. The quarter-point loss reﬂects the code pattern despite the correct numeric value.
Lake Warming’s two GPT-5.5 failures attribute the dominant contribution to Human; the passing
execution reports Heat. The attribution calculation differs across these outcomes, while formatting
does not explain the difference. React’s two failures pass ten other checks but violate the external-
API check because checkout times of 8 and 11 ms fall below the 400 ms minimum. SEC’s three
normally completed executions fail answer checks on the newly acquired-position list in one case
and on the number of reported holdings in two.
G C HANGES TO SKILL ARTIFACTS
Table 13 summarizes changes between original and deployed skill bundles. Counts cover the ﬁles
supplied to the agent, distinguishing core instructions from executable support. Each skill package
is counted separately for each task that uses it. Across all 86 tasks, 62 of 228 task-skill pairs change
(27.2%); within the 41 modiﬁed tasks, these 62 changes occur among 125 pairs (49.6%). Denom-
inators use the union of original and evolved packages. Per-task means, medians, and correlations
use the 41 modiﬁed tasks, whose total source length grows by 1.5%.
Table 13: Changes from original to deployed skill bundles. Core instructions become shorter on
average while support scripts grow. The ﬁrst two rows cover all 86 tasks; remaining statistics use
the 41 modiﬁed tasks. Means and medians are per task. Packages and ﬁles are counted separately
for each task; 228 counts the union of original and deployed packages. Line edits = insertions +
deletions; net change = insertions − deletions. ρ is Spearman correlation.
Property V alue
Tasks with changed skill bundles 41/86 (47.7%)
Skill packages changed (counted per task) 62/228 (27.2%)
Total lines: original→ deployed 106,632→ 108,233 (+1.5%)
Inserted + deleted lines: total / mean / median 8,147 / 198.7 / 157
Mean net line change per task: SKILL.md -35.0
Mean net line change per task: support scripts +74.0
Files added / deleted / modiﬁed a 18 / 2 / 60
Line edits vs. reward change: ρ (Mini / Luna) 0.25 / 0.06
a All added support ﬁles are scripts (17 Python, one shell).
Line edits count insertions plus deletions; net length change counts insertions minus deletions. Files
are matched by skill and relative path within each task; a rename counts as deletion plus addition.
Core instructions, scripts, and references are classiﬁed by their bundle paths.
H S EARCH HISTORIES AND DEVELOPMENT PATHS
We trace each frozen non-root deployment back to its recorded search root along primary-parent
links. The 41 task histories contain 1,283 candidate entries: 971 retained candidates and 312 dupli-
cate entries removed by deduplication. Duplicate entries are not additional independently evaluated
24

Preprint version
candidates. GPT-5.4 Mini performs diagnosis and writing throughout, including the 126 edits on
ﬁnal adopted paths. These search-process summaries cover the 41 modiﬁed tasks and exclude the
45 tasks that retain their original bundles.
Evaluation coverage. Decision rankings contain 705 means from three executions each, covering
529 candidate versions and 176 incumbent comparisons.
Actual expansion and later deployment. An expansion event identiﬁes a task, generation, and
parent with at least one observed child. It is non-incumbent when that parent differs from the de-
ployment incumbent entering the generation. This label records parent identity within a run; the
survivor-selection rule determines whether development is non-elitist. We count an event as lead-
ing to deployment when one of its generated children, or a descendant of that child, is selected for
deployment in that generation or a later one. Eligibility alone does not count as an expansion event.
There are 418 expansion events, of which 289 use non-incumbent parents. Of these 289 events,
76 (26.3%) have a descendant later deployed, and 61 (21.1%) enter the ﬁnal deployed ancestry;
each outcome spans 30 tasks. Among the 76, 74 lead to a descendant accepted through a reward
improvement or tie-break. The remaining two lead to Python-to-Scala deployments without a com-
plete incumbent comparison. Deployment decisions are available for 178 of 180 groups deﬁned by
task and generation; unavailable decisions are not assigned outcomes.
Continuation from strictly lower-scoring candidates. We measure relative reward against the
deployment selected in each candidate’s birth generation. This comparison is distinct from a can-
didate’s reward change relative to its own parent. Among the 529 fully measured candidate ver-
sions, 247 have a three-execution mean more than 0.05 percentage points below the deployment
selected in the same generation’s decision ranking. Both scores use that ranking’s complete three-
execution records, including the freshly measured incumbent when it remains deployed. Of these
lower-scoring candidates, 163 are later expanded; 45 (27.6%) have a subsequently deployed descen-
dant across 20 tasks, and 35 lie on a ﬁnal deployment’s primary-parent path.
For the 45 observed continuations, primary-parent distance to the ﬁrst deployed descendant is one,
two, three, or four edits in 27, 12, three, and three cases. Thus 18 candidates (40.0%) are separated
from that descendant by at least two edits. The corresponding generation gaps are one, two, three,
or four in 26, 12, four, and three cases. Revisiting an earlier node can skip generations along a single
edge. These are candidate-level counts; several candidates can belong to one task or ancestry.
Figure 4a traces the ﬁnal Gravitational Wave Detection path from root through b05 (0.0), c05 (0.0),
d01 (33.3), e04 (0.0), and f04 (100.0). Data-to-D3 follows the path b05 (33.3), c02 (66.7),
d03 (33.3), e01 (100.0), and f01 (100.0). Generation three retains c04 for deployment while
keeping d03 eligible, then generation four deploys d03’s child e01. These are birth-generation
three-execution means in percent. Both tasks raise ﬁnal Mini reward from 0.0 to 100.0.
Table 14: Parent eligibility beyond the historical top three. Both searches retain a parent despite three
higher-scoring saved versions. Scores give each version’s latest complete three-execution mean (%)
at that generation. Independent ﬁnal Mini evaluation gives both tasks 100.0, up from 0.0.
Task Generation Retained parent Higher-scoring saved versions
Gravitational Wave 4 e04: 0.0 e01: 66.7; d01, b07: 33.3
Data-to-D3 3 d03: 33.3 c01, c02, b02: 66.7
Parent eligibility differs from a global score ranking. Among the saved candidates recorded
at each stated generation, both searches retain a parent outside the historical top three (Table 14).
Descendants of both retained parents enter the ﬁnal deployed ancestry.
Explicit information sources outside the ﬁnal path. Search produces 75 graft candidates: 64
retained and 11 removed as duplicates. Eight retained graft nodes lie on ﬁnal primary-parent paths
across six tasks. Their proposals identify donors outside their tasks’ ﬁnal paths; six donors were
not selected for deployment in their own birth generation. Each proposal distinguishes the primary
parent from the source of donated material. Appendix I follows the donated procedure through the
revised Sales Pivot bundle and its executions.
Depth and edit operators. The 41 adopted lineages contain 126 edits, with 35 lineages having at
least two edits and 11 reaching depth ﬁve. Mean depth is 126/41 = 3 .07.
25

Preprint version
Table 15: Adopted lineage depth. The 41 adopted lineages have mean depth 3.07 and median depth
three. Depth counts primary-parent edits from the recorded root to deployment. It can be smaller
than the generation number when a search revisits an earlier node.
Adopted lineage depth Tasks
1 6
2 13
3 5
4 6
5 11
Table 16: Recorded edit operators. Counts cover the 41 experiment trees that produced adopted
non-root skills. Candidates counts retained candidate versions, Edits on ﬁnal paths counts adopted
ancestry edges, and Final edits counts the 41 edges producing the ﬁnal deployed bundles. These
frequencies do not measure operator success rates. The 971 candidate records and 126 edits on ﬁnal
paths all record Mini as both diagnosis and writing model.
Operator Candidates Edits on ﬁnal paths Final edits
consolidate 60 2 2
create 12 3 2
distilla 129 13 7
drop 5 0 0
extend 244 39 7
graft 64 8 3
narrow_desc 77 12 6
prune 63 9 3
rewrite 317 40 11
a The name distill denotes a skill-edit operator, not teacher-model distillation.
Tables 15 and 16 summarize complementary aspects of this history. Depth counts successive edits
from the recorded search root to the deployed bundle along primary-parent links. Operator counts
cover the 971 retained candidates and the edits on adopted paths, excluding the 312 duplicate entries.
The deployed Wyckoff and Exoplanet lineages begin with root children generated after the ﬁrst
generation. The Paratransit and Suricata lineages contain parent links that skip the immediately
preceding generation. Primary-parent depth can be smaller than generation number because the
search can revisit a bundle from before the immediately preceding generation.
Non-incumbent parents appear on ﬁnal revision paths. Of the 87 adopted edits generated after
generation one, 61 (70.1%) use a parent other than the preceding generation’s deployment incum-
bent, spanning 30 of the 41 adopted lineages (73.2%). Every chosen parent belongs to the eligible
set. This ﬁnal-path statistic has a different denominator from the 289 non-incumbent expansion
events above; it includes two later-generation edits whose parent is root.
Among the 29 tasks with improved ﬁnal Mini reward, 22 (75.9%) use a non-incumbent parent on the
ﬁnal path, accounting for 46 of their 65 post-generation-one edges. The corresponding counts for
the 12 tied tasks are eight tasks and 15 of 22 edges. Sixteen of the 29 improved-task ﬁnal paths pass
through an expanded candidate that scored strictly below its birth-generation deployment under the
deﬁnition above. We use the same 0.05-percentage-point display band as in the endpoint analysis.
Suricata retains b05 for deployment after the generation-two hold, while reselecting b01 and root
as parents. The reselected b01 produces the non-incumbent d05 in generation three, and the ﬁnal
ancestry continues through e06 and f01. The d05 edit distills a validate-then-compose workﬂow
for HTTP-ﬁeld rules. Independent ﬁnal rewards remain 0.0% for Mini and 100.0% for Luna.
Paratransit provides a ﬁnal-path revisit with a positive ﬁnal Mini difference (Figure 4c). Generation
four retains d06 for deployment and reselects d06, c05, and d04 as parents. Generation-ﬁve f08
is a child of generation-three d06 and becomes the ﬁnal selected bundle. The complete path is root
→ b07 → c03 → d06 → f08; d06 also has generation-four children, including e03. Mini’s
independent ﬁnal score rises from 0.0 to 33.3, while Luna remains at 0.0.
26

Preprint version
Later execution evidence guides revisions of earlier bundles. Wyckoff returns to the original
bundle after generation two, producing d08 in generation three and ﬁnal e03 in generation four
(Figure 4d). The root-to- d08 edge bypasses two intervening generations, while the edit uses ev-
idence from executions performed after the root bundle was created. Its editing input explicitly
quotes the generation-one b06 execution’s batch analysis of mounted CIF ﬁles. The new skill adds
a ﬁle-based recipe, Wyckoff-letter grouping, and structured output requirements. In d08’s second
execution, the agent reads the added guidance and runs a batch analysis over those ﬁles. The re-
vision makes the task workﬂow explicit using the symmetry-analysis method already available in
the original reference material. The d08 search rewards are 100.0, 82.0, and 100.0, giving a 94.0
mean. Generation three deploys d04 but retains d08 as a parent, whose child e03 is selected in
generation four. Independent evaluation of the complete ﬁnal e03 bundle raises Mini from 75.7 to
100.0, while Luna’s reward remains unchanged at 100.0.
Table 17: Skill-revision cases and ﬁnal bundle performance. Scores show original → evolved
reward (%) for complete bundles. These cases illustrate recorded revisions; the scores do not isolate
individual edit effects. Evaluation settings follow Section 4.1.
Task Revision illustrated Mini Luna
Software dependency
audit
Compare executions; reﬁne report
checks, then scan scope
0.0→ 66.7 0 .0→ 100.0
PDDL airport planning Complete a missing helper;
strengthen saved-plan checks
33.3→ 100.0 100 .0→ 100.0
Sales pivot analysis Graft PDF extraction from a
non-deployed sibling
0.0→ 33.3 0 .0→ 100.0
Gravitational wave
detection
Consolidate a non-deployed
branch’s conditioning and search
workﬂow
0.0→ 100.0 100 .0→ 100.0
I C ONCRETE EXAMPLES OF SKILL EVOLUTION
These cases connect execution contrasts, proposals, and bundle changes. Table 17 reports repre-
sentative ﬁnal task scores. The generation-level scores below are means over three search-time
executions, expressed as percentages and distinct from ﬁnal evaluations. Mini performs execution,
diagnosis, and editing throughout these development runs.
I.1 A PERSISTENT FAILURE MOVES THE REPAIR UPSTREAM
Software Dependency Audit follows root → b06 → c01. Root and b06 each have a mean reward
of 66.7%. The failed root execution expands the scan with -include-dev-deps and writes 22
ﬁndings; the two passing executions use the default production-dependency scope and write three
rows. The b06 reporting edit keys vulnerabilities by package, version, CVE identiﬁer, and severity,
removes duplicates, and checks the saved CSV against the scan-derived set. Its failed execution
deduplicates the 22 rows and veriﬁes their count and key uniqueness, but still expands the scan.
Both failures pass the structural tests but fail the content comparison. Checking the report against
an expanded scan leaves the required scan scope unveriﬁed.
The c01 proposal therefore moves the repair upstream. Its scanning instructions prohibit
-include-dev-deps while leaving b06’s reporting skill unchanged. All three executions use
the production scope, write three rows, and check the saved count and key set, yielding 100.0%
mean reward. The revision makes explicit the ﬂag’s omission from the original command example.
I.2 W ORKFLOW CONSOLIDATION ON A RETAINED BRANCH
In Gravitational Wave Detection, generation four deploys e01 but retains e04 as a parent (Fig-
ure 4a; full path in Appendix H). Although e04’s mean reward is 0.0%, each execution passes
eight of nine tests and fails only the expected numerical-result comparison. In all three runs, wave-
form generation and matched ﬁltering use the 15 Hz conditioning cutoff, violating the 20 Hz cutoff
speciﬁed in the separate search skill.
The f04 proposal consolidates the two-skill bundle. It moves the search, ﬁnal write, and readback
procedure into the conditioning document, then removes the separate matched-filtering
27

Preprint version
document. The helper ﬁle is unchanged. The merged workﬂow speciﬁes 15 Hz conditioning along-
side the 20 Hz cutoff for waveform generation and matched ﬁltering.
With the consolidated bundle, all three f04 runs use 20 Hz for search while retaining 15 Hz condi-
tioning. All three executions of each bundle, e04 and f04, write and reread a correctly structured
CSV . The f04 runs pass every test and win deployment with a 100.0% mean reward, compared
with 66.7% for e01’s fresh batch. Workﬂow consolidation accompanies a change in the executed
computation, and a zero-reward parent produces the next deployed version.
I.3 H ELPER REPAIR AND DIRECT WORKFLOW EXECUTION
In PDDL Airport Planning, root’s search-time mean reward is 0.0%. The generation-one b06 pro-
posal responds to failed plan syntax by requiring writer-based serialization and parsing the saved
plan against the same problem inputs. The initial edit omits its promised helper; validation feedback
prompts a repair that adds the executable and its invocation in SKILL.md. Although the repaired
bundle now includes the helper, the agent cannot locate it in the ﬁrst b06 execution. The agent
implements the prescribed writing, parsing, and validation workﬂow directly through the planning
library. The saved plan passes ofﬁcial veriﬁcation.
I.4 A NON -DEPLOYED SIBLING CONTRIBUTES AN EXECUTED PROCEDURE
Sales Pivot Analysis separates the value of a bundle for deployment from the value of its individual
procedures. Generation one deploys b04, which revises spreadsheet construction and has a mean
reward of 100.0%. Sibling b05 revises PDF extraction and has a mean reward of 33.3%. Its ﬁrst
two executions fail pivot-conﬁguration checks while passing state validity. The c04 proposal selects
b04 as parent and b05 as donor, citing the donor’s successful third execution.
The c04 bundle contains b05’s continuation-aware PDF procedure, including header handling and
state ﬁltering, while leaving b04’s spreadsheet skill unchanged. Its two passing executions use
header-aware extraction and retain full state names. The third converts those names to abbreviations
and fails state validity, yielding a search-time mean reward of 66.7%.
Generation two retains b04 after the historical-score check but selects c04 for further development.
The ﬁnal bundle descends from c04; its primary-parent path therefore includes the revision that
imports the procedure from b05 (Figure 4b).
Procedural compression retains perfect scores. Erlang SSH’s generation-one b09 prunes a 485-
line penetration-testing guide to 31 lines focused on reproducing an unauthenticated channel-open
attempt and verifying rejection, adds no script, and preserves perfect ﬁnal scores on Mini and Luna.
J P ROPOSER AND SKILL EDITOR PROMPT EXCERPTS
These excerpts from recorded Mini calls for Software Dependency Audit show how the Proposer
compares executions and speciﬁes an edit for the Skill Editor. For brevity, some background and
runtime details are omitted; operational rules and output formats are retained. Complete templates
accompany the source ﬁles. Here, distill encodes procedures from executions in the bundle.
Listing 1: Generation-one Proposer excerpt. The prompt provides root execution evidence, instruc-
tions for diagnosing failures, and the proposal output format.
Differential evolution of a skill library, generation 1 from root
(1-task pool). Evidence: fresh root rollouts below (failures and
behavior).
[ROOT_EXECUTION_EVIDENCE]
## Already proposed this generation (do NOT repeat or near-duplicate)
[PREVIOUS_PROPOSALS]
## Proposals REJECTED so far and why (each cost a round and produced no
child)
[REJECTION_FEEDBACK]
## Allowed operators (one per child)
28

Preprint version
prune / rewrite / extend / create / consolidate. Every one of these
writes a COMPLETE SKILL.md, so any of them can change the description,
the body, or both, and, where the scripts section below appears, the
script-capable ones can ship a file under scripts/ in the same child.
Choose by what the evidence says is broken; there is no default
operator. create ONLY if no host skill exists: narrow description naming
a concrete task domain, max 2 per generation.
consolidate MERGES: the target skill survives under its own name and
every OTHER skill in the library is folded into it and its directory
deleted. The merged description must still fire wherever each folded
skill fired -- it is rejected if it drops the trigger terms no surviving
skill carries -- and the merged body must teach each folded procedure in
one order an agent can follow, not concatenate them. Only these can
survive a fold here: cvss-score-extraction,
trivy-offline-vulnerability-scanning, vulnerability-csv-reporting.
A child may also ship EXECUTABLE files: rewrite, extend, create,
consolidate may add new files under the target skill’s scripts/, and
every one of them is run inside this task’s own container before the
child is accepted. Aim a direction there where the evidence shows the
agent doing something EVERY RUN that a program could do once and better:
deriving a value it cannot look up, or confirming a result it cannot
otherwise observe before submitting. Prose cannot supply the first and
does not help with the second. A helper that only restates the text can
merely break. Shipping one means writing the file AND the sentence that
makes it reachable; those are one edit, not two.
## Existing skills
[EXISTING_SKILL_NAMES]
## Consistency review (advisory, not a content lock)
An unmet grader noun is not an edit direction. If a grader says an
object is invalid,
missing, extra, or unreachable, first use the visible run state to
decide whether the
losing run added it, omitted it, or transformed it wrongly. Do not turn
the noun alone
into an instruction to add or preserve that object.
Agent-visible executable source and a state/action from a run that
PASSED are consistency evidence which the diagnosis must reconcile.
They are not immutable content: a proposal may replace existing behavior
when the failing/passing contrast explains why and states the narrower
invariant that should replace it. For each proposal, quote the relevant
executable line when the target skill has one in the evidence block, and
quote a concrete successful state/action when a passing run is shown. A
recovered exception, a command line by itself, or "Process exited with
code 0" is not successful-state evidence. Then state specifically
whether the direction preserves, narrows, or deliberately replaces the
quoted behavior and why that is consistent with the measured contrast.
These fields are retained for audit. Missing or imperfect quotation is
advisory and never discards a proposal; official evaluation remains the
only arbiter of the edit. Use NONE only when the corresponding kind of
evidence is genuinely absent.
## How to read the evidence, decide, and rank
How to read the evidence. The grader’s verdict blocks above are WHAT
decides the score: a run scores zero because a requirement was still
standing when it ended, and each requirement’s shown / lost / survived
counts are beside it. The rollout blocks are WHY -- that is where you do
the actual thinking. They are long and full of things going wrong, and
most of it is the agent finding its own errors and fixing them; a block
tagged as coming from a replicate that PASSED is proof its errors were
recoverable. An error a run recovered from, or a requirement that also
29

Preprint version
appears in runs that passed, is not what loses the task, however often
it appears.
A cause has to EXPLAIN the verdict, not appear in it. A cause you cannot
trace to the verdict at all is a detour; one the verdict never names but
that explains it is usually the real one, and you reach it only through
the runs.
The verdict is for YOU, not for the agent. The agent never sees the
verifier; it grades after the agent has finished. So a direction must be
actionable on what the agent CAN observe before it finishes: the source
it was given, the files in its working tree, the output of a command it
can run. And the verdict LOCATES the problem; it is not an answer to
hand over. An edit that transcribes the names the grader mentions has
cached this instance’s answer -- the agent can already reach them. Aim
the direction at how to OBTAIN the required surface.
What you are deciding is what would make this task succeed RELIABLY
rather than sometimes. You have root’s replicates above; the writer
downstream sees one direction and the file it edits, so the judgement
has to be made here and stated in the direction, specifically enough
that someone who cannot see these runs could carry it out exactly. So
the other half of every finding is the path that WORKED: at the point a
failing run went wrong, what did a passing run do instead? Where the
replicates contain a pass/fail pair, that is the cleanest source -- the
library text was identical, so whatever differs is the path. Quote it in
what_passing_runs_did; "no run has ever got past this" is a real answer,
and it labels the edit an untested guess, which is worth knowing.
Rank the causes before you propose. State each cause as a SENTENCE
naming a mechanism. Rank by how many replicates LOST because of it, not
how many show it, and report both plus how many showed it and passed
anyway. If a cause is outside what any skill edit could address, still
rank it honestly and mark it "skill_can_address": false -- the attack
quota below then applies to the highest cause a skill CAN address.
One signature deserves priority whenever it appears: the GRADED VALUE
clusters. When the number the grader checks comes out in a few tight
groups across runs of the SAME library -- within a group the values
agree to far more precision than chance would allow -- that is not
noise: the runs took different deterministic computation paths at some
step, and which path a run takes decides the score. Diff a run from each
cluster at the step that produces the graded number, name the divergence
as a cause, and propose pinning the passing path as an explicit
procedure in the skill -- the exact ordering/normalization/formula, not
the target value. Rank it through the same evidence rules as every other
cause.
At least 2 of your 6 proposals must attack the first-ranked addressable
cause (causes tied at the top score count as jointly first) and at least
3 must attack the top two; the rest are free, and that is where a small
or odd observation belongs.
Before committing to each proposal, check it against the runs: the cause
accounts for the runs that lost; it is absent from, or visibly overcome
in, the runs that passed; and the direction is executable by someone who
cannot see these runs. A proposal that fails any of these wastes its
child.
## Output strict JSON only
{"loses_the_task": [{"cause": "<one sentence naming the MECHANISM that
loses the task; it must EXPLAIN the grader’s complaint and may name
things the verdict never mentions>", "skill_can_address": <false ONLY if
no skill edit could act on this cause; omit otherwise>, "runs_showing":
<how many runs show it at all>, "runs_affected": <of those, how many
30

Preprint version
LOST because of it -- a run that showed it and still passed does not
count>, "also_in_passing_runs": <how many showed it and passed anyway; 0
is a strong cause, a large number means you are looking at a symptom>,
"what_passing_runs_did": "<the step a run that PASSED took at this same
point, quoted from its trace -- the command, the line it wrote, the
order it did things in. "no run has ever got past this" is a real answer
and says the fix is not yet in the evidence>", "evidence_quote":
"<verbatim>"}, ...],
"diagnoses": [{"parent": "root", "operator":
"prune|rewrite|extend|create|consolidate",
"target_skill": "<name>", "direction": "<one-line edit>",
"problem": "<what the evidence shows>",
"failing_test": "<the test that fails in most replicates, by name>",
"diverged_at": "<the step in the FAILING run that produced what that
test rejects -- the command it ran or the file it wrote, quoted from the
trace. If no run ever opened this skill there is no such step: say so,
and that absence is itself the finding>",
"would_change": "<what the agent does differently at that step, and
whether it could have known there that it was wrong -- if it could not,
say what makes it observable>",
"executable_consistency_quote": "<verbatim tagged line from this
target skill’s AGENT-VISIBLE EXECUTABLE block, or NONE only if absent>",
"passing_consistency_quote": "<verbatim tagged successful state/action
from a passing run, or NONE only if absent>",
"consistency_check": "<whether this direction preserves, narrows, or
replaces the quoted behavior, and why the measured pass/fail contrast
supports that relationship>",
"ships_file": "<true if this edit delivers an executable file. Say
true whenever the cause is that runs submit something they never checked
-- an instruction can only say what to do, a check reports whether it
was done. The contract is that a declaration means a file: say true and
the writer must emit it in a ===SCRIPT block, and prose describing a
file is not the file>",
"attacks": "<the exact ‘cause‘ string from loses_the_task this edit is
aimed at>",
"evidence_quote": "<verbatim from evidence above>"}, ...]}
They are asked for because an edit that cannot say where in a run it
acts has changed a topic and not a run. Answer them from the trace, and
answer them honestly -- "no run opened this skill, so there is no such
step" is a real answer and points at the description; an invented step
is worth less than none.
Exactly 6 diagnoses, diverse targets and operators. [...]
Listing 2: Later-generation Proposer excerpt. The prompt supplies candidate comparisons, parent
and donor constraints, and the proposal output format.
Differential evolution of a skill library, generation 2. Breeding
parents: b06, b01, b04 (lineages of root + accumulated single edits).
Evidence below: grader verdicts, the previous generation’s population
contrast, and raw run traces.
[POPULATION_EXECUTION_EVIDENCE]
## Already proposed this generation (do NOT repeat these or
near-duplicates)
[PREVIOUS_PROPOSALS]
## Edits already MEASURED as net losses (closely similar directions --
same operator and target -- are auto-rejected)
[PREVIOUSLY_MEASURED_LOSING_EDITS]
## Proposals REJECTED so far and why (each cost a round and produced no
child)
31

Preprint version
[REJECTION_FEEDBACK]
## Allowed operators (one per child)
prune / rewrite / graft / extend / create / drop / narrow_desc /
consolidate. Every one of these except narrow_desc and drop writes a
COMPLETE SKILL.md, so any of them can change the description, the body,
or both, and rewrite / graft / extend / create / distill / consolidate
can also ship a file under scripts/ in the same child -- writing that
file and the sentence that makes it reachable is ONE edit, not two.
Choose by what the evidence says is broken; there is no default and no
preferred operator. graft may source a section from ANY of b06, b01, b04
into a breeding parent (name source_node). create ONLY if no host
exists: narrow description naming a concrete task domain, max 2 per
generation.
distill: encode the method a winning run actually used. YOU are the one
reading those runs, so state the method itself in ‘direction‘ and
‘would_change‘ -- the steps in order, the commands or checks that
mattered, what the losing runs did instead. The editor places what you
write; it does not see the runs and cannot re-derive them.
DELIVERY MECHANISM: before the task instruction the agent is shown EVERY
mounted skill as name + full description, permanently, and is told that
a task clearly matching a skill’s description MUST use that skill.
Nothing is hidden behind a directory listing. The description decides
whether the body is ever opened; the body decides what the agent DOES --
and the body delivers in two forms, not one. It can INSTRUCT, which the
agent then follows as well as it happens to, or it can SHIP A FILE UNDER
scripts/ and name the command that runs it, which reports. An
instruction can only say what to do; a check says whether it was done.
Where a cause is that runs submit something unverified, the file is the
stronger edit and the operators rewrite / extend / graft / distill /
consolidate / create can all carry one. This library holds 3 skills:
nothing is buried and there is no sibling to win attention from, so the
only useful description edit makes the skill fire more reliably --
ENUMERATE the concrete triggers of the task it serves, in that task’s
own vocabulary. Taking trigger surface away (narrowing, disclaiming what
the skill is not for) has no competitor to beat here and can only stop
the skill firing. The leverage is in the body’s procedure.
drop REMOVES one whole skill from the library -- propose it where the
evidence shows a skill actively misleads the agent on this task; the
removal is the child’s entire edit. narrow_desc rewrites ONLY a skill’s
description line, leaving the body byte-identical; what that line should
then say is set by the DELIVERY MECHANISM paragraph above, which depends
on how many skills this library holds.
consolidate MERGES THE LIBRARY DOWN: the target skill survives under its
own name and every OTHER skill of that parent is folded into it and its
directory deleted. Both halves are checked mechanically, so propose it
only where they hold: the merged description must still fire wherever
each folded skill fired (it is rejected if it drops the trigger terms no
surviving skill carries), and the merged body must teach each folded
procedure in one order an agent can follow rather than concatenating
them. Which skill may survive a fold, by parent -- b06, b01, b04:
cvss-score-extraction, trivy-offline-vulnerability-scanning,
vulnerability-csv-reporting.
A child may also ship EXECUTABLE files: rewrite, graft, extend, create,
distill, consolidate may add new files under the target skill’s
scripts/, and every one of them is run inside this task’s own container
before the child is accepted. Aim a direction there where the evidence
shows the agent doing something EVERY RUN that a program could do once
and better: deriving a value it cannot look up, or confirming a result
it cannot otherwise observe before submitting. Prose cannot supply the
first and does not help with the second. A helper that only restates the
skill’s prose adds risk without adding information. Shipping one means
writing the file AND the sentence that makes it reachable; those are one
edit, not two.
32

Preprint version
## Existing skills
[EXISTING_SKILL_NAMES]
## Consistency review (advisory, not a content lock)
An unmet grader noun is not an edit direction. If a grader says an
object is invalid,
missing, extra, or unreachable, first use the visible run state to
decide whether the
losing run added it, omitted it, or transformed it wrongly. Do not turn
the noun alone
into an instruction to add or preserve that object.
Agent-visible executable source and a state/action from a run that
PASSED are consistency evidence which the diagnosis must reconcile.
They are not immutable content: a proposal may replace existing behavior
when the failing/passing contrast explains why and states the narrower
invariant that should replace it. For each proposal, quote the relevant
executable line when the target skill has one in the evidence block, and
quote a concrete successful state/action when a passing run is shown. A
recovered exception, a command line by itself, or "Process exited with
code 0" is not successful-state evidence. Then state specifically
whether the direction preserves, narrows, or deliberately replaces the
quoted behavior and why that is consistent with the measured contrast.
These fields are retained for audit. Missing or imperfect quotation is
advisory and never discards a proposal; official evaluation remains the
only arbiter of the edit. Use NONE only when the corresponding kind of
evidence is genuinely absent.
## Rank the causes BEFORE you propose anything
[PREVIOUS_GENERATION_LEADING_CAUSE]
Its evidence is STILL PRESENT in the block above. Rank it again, or
state as its own entry why it is no longer what loses this task -- an
edit landed and worked, or the runs moved on. Dropping it silently is
the one thing that is not an answer.
How to read the evidence. The grader’s verdict (the first block above)
is WHAT decides the score: a run scores zero because a requirement was
still standing when it ended, and each requirement’s shown / lost /
survived counts are beside it. The trajectories are WHY -- that is where
you do the actual thinking. They are long and full of things going
wrong, and most of it is the agent finding its own errors and fixing
them; an error a run recovered from, or a requirement that also appears
in runs that PASSED, is not what loses the task, however often it
appears.
A cause has to EXPLAIN the verdict, not appear in it. A cause you cannot
trace to the verdict at all is a detour; one the verdict never names but
that explains it is usually the real one, and you reach it only through
the runs.
The verdict is for YOU, not for the agent. The agent never sees the
verifier; it grades after the agent has finished. So a direction must be
actionable on what the agent CAN observe before it finishes: the source
it was given, the files in its working tree, the output of a command it
can run. And the verdict LOCATES the problem; it is not an answer to
hand over. An edit that transcribes the names the grader mentions has
cached this instance’s answer -- the agent can already reach them. Aim
the direction at how to OBTAIN the required surface.
What you are deciding is what would make this task succeed RELIABLY
rather than sometimes. You have the replicates and contrasts above; the
writer downstream sees one direction and the file it edits, so the
33

Preprint version
judgement has to be made here and stated in the direction, specifically
enough that someone who cannot see these runs could carry it out
exactly. So the other half of every finding is the path that WORKED: at
the point a failing run went wrong, what did a passing run do instead?
Where the evidence contains a same-library pass/fail pair, that is the
cleanest source -- the text was identical, so whatever differs is the
path. Quote it in what_passing_runs_did; "no run has ever got past this"
is a real answer, and it labels the edit an untested guess, which is
worth knowing.
Rank the causes before you propose. State each cause as a SENTENCE
naming a mechanism. Rank by how many runs LOST because of it, not how
many show it, and report both plus how many showed it and passed anyway.
If a cause is outside what any skill edit could address, still rank it
honestly and mark it "skill_can_address": false -- the attack quota
below then applies to the highest cause a skill CAN address.
One signature deserves priority whenever it appears: the GRADED VALUE
clusters. When the number the grader checks comes out in a few tight
groups across runs of the SAME library -- within a group the values
agree to far more precision than chance would allow -- that is not
noise: the runs took different deterministic computation paths at some
step, and which path a run takes decides the score. Diff a run from each
cluster at the step that produces the graded number, name the divergence
as a cause, and propose pinning the passing path as an explicit
procedure in the skill -- the exact ordering/normalization/formula, not
the target value. Rank it through the same evidence rules as every other
cause.
Being DRAWN to a vivid failure is fine and often useful; being drawn
entirely to it is not. At least 2 of your 6 proposals must attack the
first-ranked addressable cause (causes tied at the top score count as
jointly first) and at least 3 must attack the top two; the rest are
free, and that is where a small or odd observation belongs.
Before committing to each proposal, check it against the runs: the cause
accounts for the runs that lost; it is absent from, or visibly overcome
in, the runs that passed; and the direction is executable by someone who
cannot see these runs. A proposal that fails any of these wastes its
child.
## Output strict JSON only
{"loses_the_task": [{"cause": "<one sentence naming the MECHANISM that
loses the task; it must EXPLAIN the grader’s complaint and may name
things the verdict never mentions>", "skill_can_address": <false ONLY if
no skill edit could act on this cause; omit otherwise>, "runs_showing":
<how many runs show it at all>, "runs_affected": <of those, how many
LOST because of it -- a run that showed it and still passed does not
count>, "also_in_passing_runs": <how many runs showed it and passed
anyway; 0 is a strong cause, a large number means you are looking at a
symptom>, "what_passing_runs_did": "<the step a run that PASSED took at
this same point, quoted from its trace -- the command, the line it
wrote, the order it did things in. "no run has ever got past this" is a
real answer and says the fix is not yet in the evidence>",
"evidence_quote": "<verbatim>"}, ...],
"diagnoses": [{"parent": "b06|b01|b04", "operator":
"prune|rewrite|graft|extend|create|drop|narrow_desc|distill|consolidate",
"source_skill": "<for graft ONLY, optional: donor SKILL name when
transplanting a section into a different skill>",
"target_skill": "<name>", "source_node": "<for graft ONLY: the LIBRARY
id to copy the section FROM, one of the comparison set above - NOT a
skill name; omit otherwise>",
34

Preprint version
"task": "<OPTIONAL: the pool task this edit aims to improve, exactly
as named in the evidence; when given, the editor receives that task’s
instruction text>",
"direction": "<one-line edit>", "problem": "<what the evidence shows>",
"failing_test": "<the test that fails in most replicates, by name>",
"diverged_at": "<the step in the FAILING run that produced what that
test rejects -- the command it ran or the file it wrote, quoted from the
trace. If no run ever opened this skill there is no such step: say so,
and that absence is itself the finding>",
"would_change": "<what the agent does differently at that step, and
whether it could have known there that it was wrong -- if it could not,
say what makes it observable>",
"executable_consistency_quote": "<verbatim tagged line from this
target skill’s AGENT-VISIBLE EXECUTABLE block, or NONE only if absent>",
"passing_consistency_quote": "<verbatim tagged successful state/action
from a passing run, or NONE only if absent>",
"consistency_check": "<whether this direction preserves, narrows, or
replaces the quoted behavior, and why the measured pass/fail contrast
supports that relationship>",
"ships_file": "<true if this edit delivers an executable file. Say
true whenever the cause is that runs submit something they never checked
-- an instruction can only say what to do, a check reports whether it
was done. The contract is that a declaration means a file: say true and
the writer must emit it in a ===SCRIPT block, and prose describing a
file is not the file>",
"attacks": "<the exact ‘cause‘ string from loses_the_task that this
edit is aimed at>",
"evidence_quote": "<verbatim from evidence above>"}, ...]}
They are asked for because an edit that cannot say where in a run it
acts has changed a topic and not a run. Answer them from the trace, and
answer them honestly -- "no run opened this skill, so there is no such
step" is a real answer and points at the description; an invented step
is worth less than none.
Exactly 6 diagnoses, diverse targets and operators, each grounded in the
evidence above. [...]
J.1 S KILL EDITING FROM A PROPOSAL
The Skill Editor receives the proposal, parent skill, and task context. The excerpt below illustrates a
rewrite call; the current skill is represented by an input slot.
Apply ONE rewrite edit to an agent skill (SKILL.md with YAML frontmatter
name/description + markdown body) used by a frozen CLI coding agent on
these tasks -- software-dependency-audit.
## The edit to make -- a specification to execute, not text to copy
{
"operator": "rewrite",
"target_skill": "trivy-offline-vulnerability-scanning",
"direction": "Rewrite the scan instructions to keep this audit on
‘/root/package-lock.json‘ with the default offline production-dependency
scope and explicitly reject ‘--include-dev-deps‘.",
"problem": "Some runs broaden the vulnerability universe and write a
dev-inclusive CSV that does not match the grader’s expected set.",
"failing_test":
"test_outputs.py::TestSecurityAuditTask::test_csv_matches_ground_truth",
"diverged_at": "trivy fs /root/package-lock.json --format json
--output /root/trivy_report_dev.json --scanners vuln --skip-db-update
--offline-scan --include-dev-deps --cache-dir /root/.cache/trivy",
"what_should_happen_there": "At the scan command, the flag choice is
directly observable, so the agent should omit the dev-deps flag and
continue only with the production-only report.",
"decided_from_this_line_in_the_runs": "trivy fs
/root/package-lock.json --format json --output
35

Preprint version
/root/trivy_report_dev.json --scanners vuln --skip-db-update
--offline-scan --include-dev-deps --cache-dir /root/.cache/trivy",
"executable_consistency_evidence": "[...]",
"successful_state_consistency_evidence": "trivy fs
/root/package-lock.json --scanners vuln --offline-scan --skip-db-update
--cache-dir /root/.cache/trivy --format json -o /root/trivy_report.json",
"diagnosis_consistency_check": "Narrows the command path to the
observed passing scan while preserving the offline Trivy workflow."
}
Objective: this edit is judged on one thing -- whether the frozen agent
passes this task’s own tests more often, repeatably across independent
runs rather than once by luck. Wording that does not change what the
agent DOES scores nothing.
Your reader is an agent doing this task. The diagnosis upstream read the
runs and decided what that agent needs; the decision is the direction
above, and your job is to make it real in the file. The form is yours --
a procedure, a rule, a check it runs, a fact it was missing -- except
where the direction itself names one.
When the specification contains executable_consistency_evidence or
successful_state_consistency_evidence, reconcile the completed edit with
them. They are evidence, not frozen content: preserve them when they
describe the working invariant, or deliberately revise them only where
the supplied diagnosis_consistency_check explains the failing/passing
boundary.
A skill reaches the agent in two layers. The DESCRIPTION is always in
the agent’s context and decides whether the body is ever opened. The
BODY then delivers one of two things: instructions, which the agent
follows as well as it happens to, or a file it runs, which can report
whether the work was actually done. The direction and problem above tell
you which layer this edit acts on.
Three rules for what goes in the body:
- The agent NEVER sees the verifier; it grades after the agent has
finished. Never write anything triggered by grader output (’if the
verifier reports X...’). Write triggers the agent can observe before
finishing: the source it was given, the files in its working directory,
the output of a command it can run itself. Stating a requirement as a
fact about the task is fine.
- Teach how to OBTAIN what the task requires, not what it is. ’Read the
spec the task mounts and match the names it imports before writing the
implementation’ transfers; a table enumerating this task’s own names is
a cached answer that transfers nowhere. One or two names as an example
of the shape is fine.
- Every line must act on the cause the direction names. General
procedure is welcome when it does; material that is merely about the
same subject, however correct, is padding. Test each line: at the step
where runs were losing, does an agent that has read it do something
different?
The agent cannot edit the skill and cannot see this prompt, so never
write body text telling its reader to name a script or amend the skill;
if a script should run, ship it and give the command that runs it.
Place the change where the agent will be standing when it matters. If,
at that point, the agent could not have known it was about to go wrong,
no added sentence will move it -- what changes the run is something that
makes the wrongness observable there: a file it runs whose output it
must read before going on.
Carry the direction out in full: a file named means the file shipped and
named at the point the agent runs it; a step named means the step placed
where the agent will reach it; a removal named means it is gone. Before
returning, read the file as the agent will: every path, command and name
in it must exist; nothing you added may contradict what you kept; if you
would not follow it yourself, it is not done.
ONE EDIT IS ONE INTENT, not one file. If the change you decide on needs
more than one part to exist at all -- a new script is unreachable until
36

Preprint version
a sentence names it, a moved section is dangling until its pointer moves
-- those parts ARE the edit, and shipping them together is not two
edits. What "one" forbids is two unrelated intents in the same child,
because then no measurement can say which of them paid.
RETURN THE REST OF THE FILE BYTE FOR BYTE. You are asked for the whole
SKILL.md because that is the only way to receive a change, not because
the whole file is in scope. Lines you are not editing come back exactly
as they arrived -- same bold markers, same quote characters, same
dashes, same wrapping. Retyping them costs something real: the reader of
this lineage cannot see which lines carry the intent, the duplicate
check reads a large change where there was a small one, and the
measurement that follows cannot attribute what it measures.
Rules: the response starts with the complete new SKILL.md, beginning
with ---. frontmatter name: must be exactly
"trivy-offline-vulnerability-scanning". The description is the ROUTING
LAYER: every skill’s description sits in the agent’s context
permanently, while bodies are opened only when a description wins the
agent’s attention. This library holds 3 skills, so routing pressure is
low -- there is little sibling overlap to remove and the agent has few
descriptions to choose between, so the body’s procedure is usually where
the leverage is. Which layer THIS edit acts on is settled by the
direction, not by that tendency. Never widen the description into a
claim the body cannot serve. ASCII only, no emoji, at most 315 lines
(the current version is 243); do not delete material gratuitously -- but
material the direction or problem identifies as unused or misleading may
go. Preserve what still serves the task.
<<<TASK-INSTRUCTION software-dependency-audit
## the task instruction for software-dependency-audit -- the agent reads
this in full at every run
The agent already has every line of it. Repeating any of it in the skill
changes nothing the agent does; contradicting it (a different output
path, a different library version) costs the run.
You are a software security engineer. Given a dependency file, you need
to perform a security audit to identify vulnerabilities in third-party
dependencies.
The dependency file is given in ‘/root/package-lock.json‘.
You can use offline tools or database.
Only detect the vulnerabilities with severity levels of HIGH and
CRITICAL.
For each vulnerability, collect the following information:
- Package name
- Installed version
- CVE ID
- Severity level
- CVSS score (e.g. from NVD, GHSA, or RedHat)
- Fixed version (if available; if not available, leave it N/A)
- Vulnerability title/description
- Reference URL
Write the results to ‘/root/security_audit.csv‘ with the following
columns as
‘Package,Version,CVE_ID,Severity,CVSS_Score,Fixed_Version,Title,Url‘
>>>END-TASK-INSTRUCTION
## Measured routing fact (15 rollout(s); opened in 14 of 15)
14 of 15 previous rollout(s) opened
trivy-offline-vulnerability-scanning/SKILL.md, and none of them opened
any file under its references/, scripts/ or assets/.
37

Preprint version
## Trigger surface (the description decides whether this body is ever
opened)
The task’s own vocabulary is: audit, dependencies, dependency, engineer,
file, given, identify, party, perform, security, software, third,
vulnerabilities. A description that DISCLAIMS one of these stops the
skill firing on the task it exists for; excluding a task the skill does
help costs score directly, and excluding one it does not help gains
nothing unless a sibling skill is being confused with it.
trivy-offline-vulnerability-scanning shares at most 5 distinctive
term(s) with any of the 2 other skill(s) in this library.
## Shipping an executable helper
You may append one or more files after the SKILL.md, each introduced by
its own line:
===SCRIPT scripts/<filename>===
<complete file content>
Gates, each enforced mechanically:
- at most 4 files, all under scripts/, 40000 bytes total
- the SKILL.md must NAME every file you ship, at the point in the
procedure where the agent should run it; an unnamed file is unreachable
and the child is rejected
- every file is EXECUTED inside this task’s own container before the
child is accepted: its module level must run to completion and it must
survive being run with no arguments -- import only what that container
image already has, and stop cleanly when inputs are missing rather than
assuming them
- a direction that names an executable, answered with prose alone, has
not made the edit; deliver the file
A file the skill ALREADY ships is changed by re-emitting the whole file
with your change in it; keep everything that still works -- the diff
against the inherited version is recorded. Change one only where the
direction says that file is what is wrong.
When the direction does not name a file you may still ship one, and
where the cause is that runs submit something unchecked, you usually
should: an instruction can only say what to DO, while a check the agent
runs can say whether it was DONE, and a check is followed every time
while a sentence is followed as well as it happens to be. What a file is
FOR: to derive a value the agent has no way to look up, or to let it
OBSERVE a result it otherwise submits unchecked. Not for decoration --
ship one that acts on the cause, not one that demonstrates the
capability. The file and the sentence that makes it reachable are one
edit (see ONE EDIT IS ONE INTENT above).
## Current version
[CURRENT SKILL DOCUMENT]
## What to output, now that you have read
trivy-offline-vulnerability-scanning
- the COMPLETE new SKILL.md, starting with ---
- you MAY append files after it, each introduced by a line ===SCRIPT
scripts/<filename>===, and should where the direction or the cause is
that runs submit something unchecked
- make this one edit and no other: Rewrite the scan instructions to
keep this audit on ‘/root/package-lock.json‘ with the default offline
production-dependency scope and explicitly reject ‘--include-dev-deps‘.
- every line you add has to change what the agent DOES at the step
where runs were losing; material that reads like the rest of this file
but does not act on that is padding
38
