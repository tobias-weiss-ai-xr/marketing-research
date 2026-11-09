---
title: 'DrugHarness: An Evolvable Agent Harness for Computational Drug Discovery'
url: https://arxiv.org/abs/2610.23791
category: ai-marketing
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Yuxing Chen
- Zhisheng Zhang
- Cheng Tang
- Wei Li
- Minghui Zhang
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.23791
pages: 28
chars: 84900
fetched_at: '2026-11-08T13:32:55+00:00'
kb_version: 1
---

# DrugHarness: An Evolvable Agent Harness for Computational Drug Discovery

DRUGHARNESS: ANEVOLVABLEAGENTHARNESS
FORCOMPUTATIONALDRUGDISCOVERY
Yuxing Chen1,∗, Zhisheng Zhang2,∗, Cheng Tang1,3, Wei Li1,4, Minghui Zhang1,4,
Ziyan Huang1, Shaocong Wei1, Jiawei Chen1, Junru Hu1,3, Hongze Zhu5, Jianghan Shen1,6,
Min Cen1, Xinyuan Zhu7, Yaxue Zhao4, Jubo Wang2, Yuqiang Li1, Chun-Mei Feng8,
Zongyuan Ge9, Rui Su10, Jie Xu1, Yirong Chen1, Xi Xu2,†, Ming Hu1,†
1Shanghai Artificial Intelligence Laboratory 2China Pharmaceutical University
3University of the Chinese Academy of Sciences 4Shanghai Jiao Tong University
5Westlake University 6Nanjing University 7Ant Group
8Tongji University 9Monash University 10Shenzhen Loop Area Institute
∗Equal contribution.†Corresponding authors.
ABSTRACT
Computational drug discovery requires agents to compose scientific operations
and adapt to changing evidence and constraints. Here we introduce DrugHar-
ness, an evolvable agent harness coupling composable scientific execution with
conditional skill induction. Its environment integrates over 80 scientific opera-
tions, biomedical resources and task-specific code, preserving associations among
candidates, results and artifacts. From execution trajectories and outcome feed-
back, DrugHarness induces action hypotheses with observable applicability con-
ditions, recommended actions and supporting evidence. An independent review
agent evaluates candidate skills derived from these hypotheses through source ver-
ification and, when needed, targeted execution trials. Admitted skills guide sub-
sequent tasks and are revised through feedback. Evaluation on MolBench and
SMDD-Bench demonstrates capabilities in molecular screening, optimization and
constrained design. Without evolution, DrugHarness exceeds reported MolClaw-
CC results by 10.8 percentage points in affinity-comparison accuracy and 55%
in mean top-three active hits on MolBench. Retrospective evaluation on skill-
development tasks shows that evolution increases Qwen’s affinity-comparison ac-
curacy from 62.2% to 81.1% and optimization success from 79.5% to 87.2%. In a
prospective HPK1 study, DrugHarness achieves a more favorable median docking
score than Biomni among system-specific candidates. A synthesized compound
achieves a cellular IC50 of 14.19 nM, a 2.64-fold potency improvement over the
best input reference, with activity competitive with two selected compounds de-
signed by experienced medicinal chemists. These results support conditional skill
evolution for scientific agents and demonstrate a workflow connecting computa-
tional drug design with experimental validation.
1 INTRODUCTION
Drug discovery requires coordinating evidence and computation across molecular screening, op-
timization, and design. Experimental activity records, molecular representations, and property or
binding predictors provide complementary information for candidate selection (Liu et al., 2025;
RDKit contributors; Swanson et al., 2024; Passaro et al., 2025). Turning these capabilities into a
solution requires a sequence of decisions: which evidence to retrieve, which candidates to modify,
which calculations to perform, and when a set of molecules satisfies the objective. Recent agent
systems have begun to automate these multi-step tasks, making the organization of scientific actions
and the reuse of effective strategies central questions for autonomous drug discovery (Averly et al.,
2025; Wang et al., 2026).
Progress spans three connected directions.Tool and environment integrationmakes scientific re-
sources accessible through specialized interfaces, code-based composition, and reusable infrastruc-
ture (Bran et al., 2024; Huang et al., 2026; Gao et al., 2025b).Workflow orchestrationorganizes
these operations through domain skills, specialist collaboration, and stateful processes that maintain
1
arXiv:2610.23791v1  [cs.AI]  16 Oct 2026

intermediate results and guide subsequent actions (Zhang et al., 2026b; Gao et al., 2025a; Cao et al.,
2026).Experience and skill reusebrings earlier solutions back into execution: prior designs in-
form new molecular proposals, historical tool trajectories guide lead optimization, and accumulated
scientific experience supports later reasoning and tool selection (Gao et al., 2025a; Li et al., 2026;
Tang et al., 2025; 2026b). Together, these directions establish a basis for agents that both execute
scientific workflows and accumulate guidance from their use.
Despite this progress, turning heterogeneous scientific experience into dependable action guidance
presents three coupled challenges.(1) Grounding a recommendation in the right evidence.An
activity measurement, a predicted property, an agent’s interpretation, and a final task score answer
different questions; their objects, endpoints, and observation times determine which action claims
they support.(2) Preserving applicability across tasks.A useful source-task action may become
inappropriate when the candidate state or remaining constraints change. For example, a set with ade-
quate molecular properties but insufficient diversity may benefit from broader structural exploration
rather than further optimization of similar candidates.(3) Establishing executable and revisable
guidance.A plausible recommendation may rest on an unchecked scientific premise or an opera-
tion that behaves differently from its description. Its critical assumptions and execution path need
active examination, and subsequent task feedback must inform revisions as new evidence becomes
available. These challenges call for a learning process that connects scientific evidence, observable
conditions, and active scientific review to the continuing use of a skill.
We introduceDrugHarness, a unified system for composable scientific execution and conditional
skill learning. Its scientific environment provides over 80 scientific operations across ten capabil-
ity categories, connecting tools, biomedical resources, and code while retaining associations among
candidates, results, and artifacts. To ground reusable guidance, the learner compares these experi-
ences and forms action hypotheses with explicit sources and applicability conditions. It translates
each hypothesis into a skill whose conditions the executor assesses against the new task’s visible
state. An independent review agent examines evidence, applicability, and executability, using the
same scientific tools and code environment for targeted checks when needed. Admitted skills be-
come available to subsequent tasks, whose trajectories and native outcome feedback support further
revision. Review records also allow rejected or deferred proposals to inform later changes. This
design connects scientific judgment with the formation, use, and revision of action strategies.
We evaluate DrugHarness on two benchmarks and a prospective molecular design study. On Mol-
Bench, DrugHarness without evolution achieves 91.9% affinity-comparison accuracy and 1.24 mean
Hits@3, exceeding the reported MolClaw-CC results by 10.8 percentage points and 55%, respec-
tively. On SMDD-Bench, it satisfies all evaluation criteria in 24 of 40 lead-optimization tasks
and supports structurally constrained design (Tables 1 and 2). In retrospective evaluation on skill-
development tasks, frozen learned skills increase Qwen’s affinity-comparison accuracy from 62.2%
to 81.1% and optimization success from 79.5% to 87.2% relative to historical runs without skills (Ta-
ble 3). In prospective HPK1 design, DrugHarness achieves a more favorable median docking score
than Biomni among system-specific candidates (Figure 2). A synthesized compound achieves a Ju-
rkat p-SLP76 IC50 of 14.19 nM, a 2.64-fold potency improvement over the best input reference, with
activity competitive with two selected compounds independently designed by experienced medic-
inal chemists (Section 4.4). These results demonstrate scientific execution capabilities, in-domain
benefits from skill evolution, and experimentally validated molecular design.
Our main contributions are:
•Composable execution for molecular discovery.DrugHarness integrates over 80 sci-
entific operations, biomedical resources, and task-specific code, preserving associations
among candidates, results, and artifacts to support adaptive scientific workflows. We will
release the implementation, tool interfaces, and environment configurations.
•Evidence-reviewed evolution of conditional skills.DrugHarness induces action hypothe-
ses with explicit applicability conditions and supporting evidence. An independent agent
reviews candidate skills through source checks and targeted scientific trials when needed,
while subsequent execution feedback refines their content and scope.
•Evaluation from benchmarks to prospective validation.We assess execution on two
benchmarks, skill evolution through retrospective in-domain evaluation, and prospective
2

HPK1 design through computational comparison with Biomni and experimental evaluation
alongside reference and selected expert-designed compounds.
2 RELATEDWORK
Scientific agents for drug discovery.Scientific agents organize capabilities through tool augmen-
tation, code-based execution, and reusable environments, as illustrated by ChemCrow, Biomni, and
ToolUniverse (Bran et al., 2024; Huang et al., 2026; Gao et al., 2025b). SciToolAgent further repre-
sents tool dependencies and compatibility in a knowledge graph for tool-chain planning (Ding et al.,
2025). Drug-discovery workflows use hierarchical domain skills, specialist collaboration, or state-
ful skill graphs to coordinate research stages (Zhang et al., 2026b; Gao et al., 2025a; Cao et al.,
2026); CAi and LIDDiA organize candidate evidence and feedback-driven molecular exploration
(Wang et al., 2026; Averly et al., 2025). Experience already participates in these workflows: Phar-
mAgents summarizes earlier designs, and TRACE retrieves optimization trajectories to guide tool
sequencing (Gao et al., 2025a; Li et al., 2026).
Experience-driven skill learning.Experience can be distilled into rules and examples, context-
aware guidelines, or consolidated skills (Zhao et al., 2024; Fu et al., 2024; Ni et al., 2026). ACE
maintains guidance incrementally, while SkillOpt and WikiSkill combine skill revision with
execution-based selection and persistent learning state (Zhang et al., 2026c; Yang et al., 2026;
Tang et al., 2026a). Concurrent work on SkillCommit examines how replay-supported behavior gov-
erns skill consolidation and scope expansion (He & Yang, 2026). Scientific applications learn differ-
ent objects: ChemAgent maintains chemical subproblem solutions, DrugSAGE reuses experience in
property-prediction model development, and SciToolAgent-Evo acquires scientific tool chains and
situation-dependent selection guidance (Tang et al., 2025; Zhang et al., 2026d; Tang et al., 2026b).
These studies provide complementary mechanisms for experience reuse across reasoning, modeling,
and tool-use tasks.
3 METHOD
3.1 SYSTEMOVERVIEW ANDSCIENTIFICEXECUTIONENVIRONMENT
DrugHarness integrates composable scientific execution with conditional skill learning (Figure 1).
Task execution produces experiences for learning, and an independent review agent uses the same
scientific environment to examine candidate skills. Admitted guidance supports subsequent tasks,
whose feedback informs further revision.
DrugHarness provides over 80 agent-accessible scientific operations across ten capability cate-
gories, spanning evidence retrieval, target and structure preparation, molecular design, and compu-
tational evaluation (Table 6). Biomedical resources and specialized tools such as BindingDB, RD-
Kit, ADMET-AI, and Boltz-2 work alongside a scientific Python environment to support candidate
assessment and design (Liu et al., 2025; RDKit contributors; Swanson et al., 2024; Passaro et al.,
2025).
In the shared scientific workspace, the agent selects and combines these operations according to
the task’s goals, constraints, and intermediate results. DrugHarness preserves associations among
scientific objects, computational conditions, sources, and outputs across tool calls and task-specific
code. As a result, evaluations from different tools remain linked to the same candidate, and returned
structures or datasets can become inputs to further analysis. The runtime maintains the action loop
as the agent uses this evidence to select further computations, revise candidates, and produce a final
deliverable. Trajectories, deliverables, and permitted outcome feedback then provide material for
skill learning.
3.2 INDUCINGCONDITIONALSCIENTIFICSTRATEGIES
Learning starts from recorded scientific decisions: the task being pursued, actions and observations
during execution, the deliverable, and permitted outcome feedback. Each experience is
ei = (xi, τi, yi, fi), τ i =

(ai,j, oi,j)
Ti
j=1,(1)
3

3  Revise & update
Review
record
Revise insights
& history
Checks · Trials · Decision
· Unresolved questions
Skill version update
Completed admit:
Otherwise:
Subsequent tasks
𝐾!"#←𝐾!
𝐿
𝑉
𝐾!"#←𝐾! ’
Scientific workspace
Target
evidence
· Literature
· Databases
· Biological
context
Structure
& pocket
· 3D structure
· Pocket analysis
· Binding modes
Candidate
discovery
· Virtual
screening
· De novo design
· Similarity
search
Property
optimization
· Property
prediction
· Multi-objective
opt.
· Structure editing
Synthesis
analysis
· Retrosynthesis
· Synthetic
feasibility
· Building blocks
Public evidence Scientific tools Scientific code
𝐸
Task · Actions & observations ·
Deliverable · Allowed feedback
Task
Goals ·Constraints
Public inputs
Skills
Fixed within thetasks
Scientific agent
Select · Act· Observe
Input
Read & use
𝐾#
Final deliverable
• Selected candidates
• Analyses & rationale
• Reproducible record
Evaluation & feedback
• Task evaluation
• Later evidence
1  Induce conditional guidance
Insights · Current skills ·History𝐿 𝐾# 𝑉
Candidate
· When to use
· Recommended
actions
· Limits &
references
𝐾! ’Source experiences
Task
Observation
Action
Outcome
Induce hypothesis
· When: observable
conditions
· Prefer: action over
alternative
· Sources  Unknowns
h
B   Conditional skill learning
A   Composable scientific execution
2  Scientific review
Independent
review agent
Evidence check
· Action &
result
· Tools & code
· Consistency
Targeted trial
· Reproduction
· Ablation
· Comparison
· Uncertainty
Next inductionReview decision: admit · reject · defer
Actions
Traces
Observations
Update
Update
Experience
Figure 1:Overview of DrugHarness.(A) The agent composes public evidence, scientific tools, and code
into task-specific workflows around shared scientific objects. Traces and permitted outcome feedback form
experiences. (B) The learner induces conditional action hypotheses and translates them into candidate skills. An
independent reviewer checks their evidence and conducts targeted trials in the same workspace when needed.
Admitted skills guide subsequent tasks, while review records update insights and history for further learning.
wherex i contains the task objective, constraints, and public inputs;τi recordsT i steps, witha i,j and
oi,j denoting the action and visible observation at stepj;y i is the deliverable; andf i is permitted
outcome feedback. Distinguishing contemporaneous observations, the executor’s interpretations,
and subsequent evaluations lets the learner relate a decision to the evidence available at execution
time and to feedback obtained afterward.
The learner identifies recurring decision problems across experiences and compares the relevant
scientific objects, endpoints, methods, and evidence states. It examines decision-relevant conditions,
such as which constraints have been met and whether the evidence needed for a decision has been
obtained, rereading permitted sources when a specific question requires clarification.
Compatible conditions and consistent recommendations allow support to be combined; different
conditions retain separate applicability scopes. For conflicting evidence under comparable condi-
tions, the learner narrows or splits a recommendation when justified and retains unresolved dis-
agreements. These comparisons connect the circumstances of an action to the evidence supporting
a proposed change for a stated objective.
The result is a conditional action hypothesis specifying when an action should be preferred, what
objective it serves, and the grounds for that choice:
h= (g, c, a0, a, Rh, Uh).(2)
Heregis the goal andcdescribes conditions observable by the executor;a 0 andadenote the current
or alternative action and the recommended action. SourcesR h support or limit the hypothesis, and
Uh records unresolved information. For illustration, when individual molecules meet property re-
quirements but set diversity is insufficient, a hypothesis may prioritize expanding structural sources
over further optimization of similar candidates.
An LLM carries out this induction within a researcher-defined scopeΩof tasks, quality objectives,
permitted materials, execution environment, and evaluation rules. At learning roundt, it reads a
batchB t ⊆Efrom the experience collectionE, together with accumulated insightsL t, current
4

skillsK t, and revision historyV t. Under reading and generation allowanceB t, the update is
(eLt, ht) = Induce(Bt, Lt, Kt, Vt; Ω,Bt).(3)
The learner compares the proposed change with current skills and revision history to identify existing
coverage and relevant prior findings. It returns revised insights eLt and a hypothesish t for one
proposed action change; when no reusable modification is warranted, it returnsh t =∅while
updating insights. Algorithm 2 details this process.
3.3 CANDIDATESKILLCONSTRUCTION ANDEVIDENCEREVIEW
The learner converts the action hypothesis into a skill update with one intended change in the ex-
ecutor’s behavior. The revised guidance preserves the hypothesis’s goal, applicability conditions,
recommended action, and supporting evidence. Together with the remaining skills, it forms the
complete candidate versionK ′ t = Edit(K t, ht). The skill’s name and description support discov-
ery; its body explains when and how to apply the recommendation, including relevant limits, while
accompanying resources retain the scientific basis.
Each candidate states the decision situations it addresses and observable checks of its intended
change. An independent review agent checks the supporting sources and scientific premises, asking
whether they justify the recommendation under the stated conditions. It also examines whether the
executor can assess those conditions from available information and carry out the instructions. The
reviewer can retrieve original sources, inspect interfaces, and use the same scientific tools and code
environment as the task executor. When a scientific or operational question requires computation, it
conducts a targeted trial and retains the inputs, outputs, and limitations.
Review produces an admission decision and evidence for subsequent learning. A completed review
returns
ρt = Review(K ′ t, ht, Rht ; Ω)∈ {admit,reject,defer}.(4)
Admission makes the complete candidate version available for subsequent tasks. Conflicts with
critical facts or constraints support rejection; insufficient evidence supports deferral. Completed
source checks, trial findings, and unresolved questions remain available for later induction regardless
of the decision.
3.4 TASK-TIMEUSE ANDFEEDBACK-DRIVENREVISION
For each candidate branch, review determines whether the current guidanceK t is updated to the
candidate versionK ′ t:
Kt+1 =
K ′ t,review completed andρ t = admit,
Kt,otherwise. (5)
Each task binds a specified skill version, whose contents remain fixed throughout that execution.
The executor discovers relevant skills from their names and descriptions and reads their bodies and
resources as needed. For a hypothesishand its conditioncexpressed in the skill, applicability is
assessed against the visible states j:
bχj(h) = Assess(c;s j)∈ {supported,contradicted,unknown}.(6)
The executor makes this semantic judgment from the available evidence. Supported conditions allow
the recommendation to inform action selection; contradicted conditions direct the executor to other
grounds for action. When a critical condition is unknown, the executor decides whether further
information would help. These judgments inform which recommendations to use and how to adapt
the actions to the current task.
Review and execution provide complementary inputs to the next learning round. Completed source
checks, trial findings, and unresolved questions update insightsLand historyVwhether or not
a candidate is admitted. Subsequent task trajectories, deliverables, and permitted outcome feed-
back add new experiences toEas they become available. Later induction draws on the updated
experiences, insights, and history to reconsider action recommendations and their applicability con-
ditions. Proposed changes then return to candidate construction and independent scientific review.
Appendix C provides the learning loop and induction procedure.
5

4 EXPERIMENTS
We evaluate three aspects of DrugHarness: scientific execution without learned skills, execution with
experience-derived skills, and prospective evaluation of designed molecules. Model and runtime
comparisons support the execution analysis, while task trajectories clarify how learned guidance
enters scientific decisions. Appendix D presents four case studies of scientific execution, feedback
use, and skill refinement.
4.1 EXPERIMENTALSETUP
System configurations.DrugHarness (w/o Evol.)uses the full scientific environment with-
out cross-task learned skills; its main configuration is Codex (OpenAI, 2026) with GPT-5.6
Terra/xhigh. Model comparisons use Codex with Qwen3.7-Max, and runtime comparisons use Her-
mes (Nous Research, 2026) with Terra/xhigh. Both comparisons cover all 190 MolBench tasks;
runtime comparisons additionally cover 202 SMDD Types 1–5 tasks. We also evaluate the origi-
nal SMDD harness with Terra/xhigh on the same SMDD task set.DrugHarness (Evol.)uses ad-
mitted, frozen skills: Qwen3.8-Max/xhigh performs automatic refinement and independent review.
DrugHarness uses a default execution budget of one hour per benchmark task and six hours for the
HPK1 design task.
Evaluation tasks and metrics.We use the two benchmarks for complementary purposes. SMDD-
Bench evaluates DrugHarness on diverse constrained molecular-design problems and serves as a
broad test of scientific execution (Han et al., 2026). MolBench provides a fine-grained decom-
position of molecular decision-making and operations, spanning property filtering, similarity fil-
tering, affinity comparison, virtual screening, molecular editing, and optimization, together with
task-specific quantitative feedback (Zhang et al., 2026b). We therefore use MolBench as the pri-
mary testbed for studying experience-driven evolution, where such fine-grained feedback enables
systematic analysis of skill induction, use, and revision. SMDD-Bench uses task success rates; we
evaluate a fixed 40-task lead-optimization (LO) subset spanning 25 targets and the complete remain-
ing families. MolBench metrics include accuracy, mean active hits among the top three candidates
(Hits@3), and positive-improvement success rate. Task breakdowns and metric definitions appear
in Appendix A. The prospective HPK1 task evaluates analog design under collaborator-provided
references and constraints (Section 4.4).
4.2 MAINRESULTS
Table 1:Results on SMDD-Bench.Success rates (%) on the same task set, including a fixed subset
of 40 lead-optimization tasks.
Method / Runtime Model 2D Pharm.↑IP↑SH↑LO↑FA↑
SMDD harness
Claude Sonnet 4.628.00.0 3.8 47.5 0.0
GPT-5.4 12.0 0.0 3.8 55.01.7
Gemini 3.1 Pro 20.0 4.0 0.0 47.51.7
Kimi K2.5 Thinking 12.0 0.0 1.9 32.5 0.0
DeepSeek V3.2 8.0 0.0 3.8 22.5 0.0
MiniMax M2.7 16.0 0.0 1.9 27.5 0.0
Qwen3.5 397B A17B 4.0 0.0 1.9 45.0 0.0
GPT5.6-Terra† 16.0 0.09.650.0 0.0
DrugHarness/ Hermes (w/o Evol.) GPT5.6-Terra 12.0 20.0 3.8 37.5 0.0
DrugHarness/ Codex (w/o Evol.) GPT5.6-Terra 12.028.07.760.00.0
† We ran the original SMDD harness with GPT-5.6 Terra. Other SMDD results are from
Han et al. (2026).
Overall Performance.We use Codex with GPT-5.6 Terra as the main configuration to evaluate
scientific execution without evolution. On SMDD-Bench, DrugHarness/Codex achieves 28.0% suc-
cess in interaction point discovery versus 0.0% for the original SMDD harness, and 60.0% versus
50.0% on the same 40 lead-optimization tasks, with both systems using GPT-5.6 Terra (Table 1). On
MolBench, affinity accuracy reaches 91.9%, 10.8 percentage points above MolClaw-CC, and mean
6

Table 2:Results on MolBench.Baseline results are from Zhang et al. (2026b) and Wang et al.
(2026). Metric definitions are provided in Appendix A.1.
Method MolClaw comparison group CAi DrugHarness(w/o Evol.)
Model Sonnet 4.6 Sonnet 4.6 Qwen3.7- Max Qwen3.7- Max Qwen3.7- Max GPT5.6- Terra GPT5.6- Terra
Runtime Claude Code† Claude Code N/R CAi Codex Hermes Codex
Screening
Accuracy (%)↑ 98.0 98.0 18.0 96.0 96.0 98.098.0
Precision (%)↑ — — 32.0 98.0 98.0 98.0100.0
Recall (%)↑ — — 44.5 97.0 97.0 98.099.0
F1 (%)↑ — — 33.8 97.3 97.3 98.099.3
Specificity (%)↑ — — 44.0 98.0 100.0 98.0100.0
Validity (%)↑ — — 78.0 100.0 98.0 100.0100.0
Affinity comparison
Accuracy (%)↑ 51.4 81.1 54.1 54.1 62.2 83.891.9
Valid choice (%)↑ — — 100.0 100.0 100.0 100.0100.0
Virtual screening
Hit@3 (%)↑ — — 52.0 40.0 60.0 48.060.0
Mean Hits@3↑ 0.56 0.80 0.76 0.56 0.72 0.921.24
Top-3 rate (%)↑ — — 25.3 18.7 24.0 30.741.3
Mean GT rank↓ — — 56.23 55.49 29.05 27.6917.27
Hit count↑ — — 13/25 10/25 15/25 12/2515/25
Editing
Add (%)↑ — — 70.0 100.0 100.0 100.0100.0
Delete (%)↑ — — 88.9 100.0 100.0 100.0100.0
Substitute (%)↑ — — 95.0 95.0 95.0 100.0100.0
Overall (%)↑ 97.4 100.0 87.2 97.4 97.4 100.0100.0
Validity (%)↑ — — 100.0 100.0 100.0 100.0100.0
Optimization
Mean∆↑ 0.8660 1.7240 0.1352 0.2263 0.6054 0.4530 0.5988
Success rate (%)↑ —100.048.7 79.5 79.5 84.6 94.9
Valid SMILES (%)↑ — — 97.4 100.0 87.2100.094.9
Scaffold hard (%)↑ — —71.8 46.2 38.5 59.0 35.9
Scaffold soft (%)↑ — —88.9 76.5 61.8 77.0 63.6
N/R: Runtime not reported.†: Claude Code without MolClaw skills.
Hits@3 reaches 1.24 versus 0.80. Screening accuracy is 98.0%, all 39 editing tasks are solved,
and 37 of 39 optimization tasks yield positive improvement (94.9%; Table 2). Together, these re-
sults establish support for candidate judgments, precise molecular operations, and designs with joint
structural and property constraints.
Backbone and Runtime Comparisons.We vary the model within Codex to assess backbone
dependence, and compare Hermes with Codex under Terra to assess runtime effects. With Qwen3.7-
Max, DrugHarness attains 62.2% affinity accuracy versus 54.1% for both CAi and MolClaw, and
60.0% Hit@3 versus 40.0% and 52.0%, respectively; screening (96.0%) and editing (97.4%) match
CAi (Wang et al., 2026). With Terra, both runtimes achieve 98.0% screening and 100% editing
accuracy, while Codex leads Hermes in affinity accuracy (91.9% versus 83.8%) and mean Hits@3
(1.24 versus 0.92). Codex/Terra achieves the strongest overall performance among the DrugHarness
configurations tested.
4.3 EXPERIENCE-DRIVENEVOLUTION
Beyond backbone and runtime choices, we examine whether execution experience can improve
DrugHarness through reusable skills.
Domain-specific guidance raises screening accuracy to 100%, affinity accuracy from 62.2% to
81.1%, and optimization success from 79.5% to 87.2%, while retaining 97.4% editing accuracy
(Table 3). All 39 optimization tasks produce valid JSON submissions, compared with 34 in histori-
cal no-skill runs.
Learned guidance makes retrieved evidence actionable. In affinity task ms2-029, both skill versions
led the executor to materialize the same collection of 933 records. The earlier guidance prompted
text searches and structural reasoning; the revision prompted RDKit structure matching to associate
7

Table 3:Experience-driven evolution on MolBench.Codex/Qwen3.7-Max with historical no-
skill runs and retrospective in-domain evaluation using frozen domain-specific skills. Proportions
are percentages. Complete metrics: Appendix A.2.
Setting Screening Affinity Virtual screening Editing Optimization
Acc.↑Acc.↑Hit@3↑ Mean Hits@3↑ Mean GT rank↓ Acc.↑SR↑ Valid JSON↑
w/o Evol. 96.0 62.260.0 0.7229.0597.479.5 87.2
Evol.100.0 81.148.0 0.6426.01 97.4 87.2 100.0
candidates with activity records and distinguishKi from IC50. The decision changed from incorrect
to correct. Across the domain, the learned skill corrects nine historical errors and retains twenty-one
previously correct answers.
Optimization experience yields guidance for checking the actual deliverable. From formatting fail-
ures and their repairs, the learner forms instructions to read back and validate the saved answer be-
fore submission. The independent reviewer tests this procedure in a targeted execution trial before
deployment; subsequent runs produce valid JSON on all 39 tasks, with positive property improve-
ment on 34. The learned skills achieve 30/37 correct affinity comparisons and 34/39 successful
optimizations, approaching the fixed researcher-written references of 33/37 and 35/39, respectively.
Virtual screening illustrates feedback-driven skill revision. The initial skill emphasized recovery of
missing jobs, but runs exposed missing submissions and incomplete candidate coverage. DrugHar-
ness used these trajectories and feedback to revise the skill. With the frozen revision, complete
coverage of the original 60 candidates increased from 14/25 to 25/25 tasks. Revised runs achieved a
top-three hit on 12 tasks and a mean reference rank of 26.01 versus the historical no-skill 29.05.
4.4 PROSPECTIVEVALIDATION OFDESIGNEDMOLECULES
We design human HPK1 (MAP4K1) inhibitors from four experimentally characterized references,
aiming to improve Jurkat p-SLP76 inhibition over the best reference (IC50: 37.47 nM). Designs pre-
serve the shared core and specified double-bond geometry, modifying only terminal amide nitrogen
substituents.1 DrugHarness uses Codex/Qwen3.8-Max; Biomni uses its default configuration.
DrugHarness
−8.180
Biomni
−7.825
−8.5
−8.2
−7.9
−7.6MOE docking score
(a) MOE docking
0 0.25 0.5 0.75 1
Predicted inhibition score
CYP2C19
CYP2B6
OATP1B1
OATP1B3
0.078
0.470
0.066
0.492
0.113
0.554
0.133
0.458 (b) Selected inhibition predictions
Figure 2:Computational evaluation of HPK1 candidates.Four system-specific structures per group remain
after excluding six shared structures from ten evaluated entries each. Colors: DrugHarness; Biomni.
Symbols: molecules (•), medians ( ). Lower is favorable. The four inhibition endpoints were selected post
hoc for lower DrugHarness medians; its median hERG inhibition was higher (0.949 versus 0.663) and QED
lower (0.3645 versus 0.4085).
In Silico Evaluation of Designed Molecules.Among the four system-specific candidates per
evaluated set, DrugHarness achieves a more favorable median MOE docking score than Biomni
1Candidate molecules are reported using coded identifiers; their chemical structures are withheld for confi-
dentiality.
8

(−8.180versus−7.825; Figure 2(a)). It also has lower median inhibition predictions for CYP2C19
(0.078 versus 0.470), CYP2B6 (0.066 versus 0.492), OATP1B1 (0.113 versus 0.554), and OATP1B3
(0.133 versus 0.458; Figure 2(b)).
Experimental Validation of Designed Molecules.
A DrugHarness-designed compound was synthe-
sized and experimentally evaluated by our medic-
inal chemistry collaborators. It achieved a Ju-
rkat p-SLP76 IC50 of 14.19 nM, lower than
those of all four reference compounds (37.47–
227.77 nM), together with 96.92% HPK1 inhibition
at 1 nM. On the same design task, the DrugHarness-
designed compound showed competitive biochemi-
cal and cellular activity compared with two selected
compounds independently designed by medicinal
chemists with over five years of experience (Fig-
ure 3).
10 30 100 300
Jurkat p-SLP76 IC50 (nM)
85
90
95
100HPK1 inhibition at 1 nM (%)
DH
H01
H04
DrugHarness
References
Chemist designs
Figure 3:Comparison with selected chemist de-
signs.Lower cellular IC50 and higher 1 nM HPK1
inhibition indicate stronger activity.
5 LIMITATIONS ANDCONCLUSION
Limitations.Systematic comparisons of runtime, computational cost, and resource requirements
against other agent frameworks and human experts remain open. Skill evolution is evaluated on
a single benchmark with a limited number of tasks under a retrospective, in-domain setting; its
effectiveness at larger scales and generalization to unseen targets and task families remain to be es-
tablished. Experimental validation is also limited in scale and coverage of developability properties.
Future work will expand evaluation across benchmarks and targets, conduct held-out assessments,
and broaden experimental validation under matched conditions.
Conclusion.DrugHarness provides a mechanism for evolving scientific agent strategies through
conditional skill learning. It turns execution experience into reusable guidance with explicit appli-
cability conditions, independent scientific review, and feedback-driven revision. Evaluation on two
benchmarks demonstrates broad molecular task capabilities, while retrospective results on skill-
development tasks show improvements in screening, affinity comparison, and optimization. A
prospective design study further links computational predictions to experimental activity, yielding a
synthesized compound with improved cellular potency over all input references and activity com-
petitive with selected expert-designed compounds. These findings support evidence-reviewed skill
evolution as a promising approach to improving scientific agents and motivate broader evaluation of
its generalization and experimental utility.
REFERENCES
Reza Averly, Frazier N Baker, Ian A Watson, and Xia Ning. LIDDIA: Language-based intelligent
drug discovery agent. InProceedings of the 2025 Conference on Empirical Methods in Natural
Language Processing, pp. 12004–12028, 2025.
C´edric Bouysset and S ´ebastien Fiorucci. ProLIF: a library to encode molecular interactions as
fingerprints.Journal of Cheminformatics, 13(1):72, 2021. doi: 10.1186/s13321-021-00548-6.
URLhttps://doi.org/10.1186/s13321-021-00548-6.
Andres M. Bran, Sam Cox, Oliver Schilter, Carlo Baldassari, Andrew D. White, and Philippe
Schwaller. Augmenting large language models with chemistry tools.Nature Machine Intelli-
gence, 6(5):525–535, 2024. doi: 10.1038/s42256-024-00832-8. URLhttps://doi.org/
10.1038/s42256-024-00832-8.
Annalisa Buniello, Daniel Suveges, Carlos Cruz-Castillo, Manuel Bernal Llinares, Helena Cornu,
Irene Lopez, Kirill Tsukanov, Juan Mar ´ıa Rold ´an-Romero, Chintan Mehta, Luca Fumis, et al.
Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery.Nucleic
Acids Research, 53(D1):D1467–D1475, 2025. doi: 10.1093/nar/gkae1128. URLhttps://
doi.org/10.1093/nar/gkae1128.
9

Stephen K. Burley, Charmi Bhikadiya, Chunxiao Bi, Sebastian Bittrich, Henry Chao, Li Chen,
Paul A. Craig, Gregg V . Crichlow, Kenneth Dalenberg, Jose M. Duarte, et al. RCSB Protein
Data bank: Tools for visualizing and understanding biological macromolecules in 3D.Protein
Science, 31(12):e4482, 2022. doi: 10.1002/pro.4482. URLhttps://doi.org/10.1002/
pro.4482.
Duanhua Cao, Geng Chen, Jiaxin Jiang, Jie Yu, Runze Zhang, Mingan Chen, Wei Zhang, Li-
fan Chen, Feisheng Zhong, Yingying Zhang, et al. Generic protein–ligand interaction scor-
ing by integrating physical prior knowledge and data augmentation modelling.Nature Ma-
chine Intelligence, 6(6):688–700, 2024. doi: 10.1038/s42256-024-00849-z. URLhttps:
//doi.org/10.1038/s42256-024-00849-z.
He Cao, Siyu Liu, Fan Zhang, Zijing Liu, Hao Li, Bin Feng, Shengyuan Bai, Leqing Chen, Kai
Xie, and Yu Li. Mozi: Governed Autonomy for Drug Discovery LLM Agents, 2026. URL
https://arxiv.org/abs/2603.03655v1.
Ethan Cerami, Jianjiong Gao, Ugur Dogrusoz, Benjamin E. Gross, Selcuk Onur Sumer, B ¨ulent Ar-
man Aksoy, Anders Jacobsen, Caitlin J. Byrne, Michael L. Heuer, Erik Larsson, et al. The cBio
Cancer Genomics Portal: An Open Platform for Exploring Multidimensional Cancer Genomics
Data.Cancer Discovery, 2(5):401–404, 2012. doi: 10.1158/2159-8290.CD-12-0095. URL
https://doi.org/10.1158/2159-8290.CD-12-0095.
John S. Delaney. ESOL: Estimating Aqueous Solubility Directly from Molecular Structure.Jour-
nal of Chemical Information and Computer Sciences, 44(3):1000–1005, 2004. doi: 10.1021/
ci034243x. URLhttps://doi.org/10.1021/ci034243x.
Ji Ding, Shidi Tang, Zheming Mei, Lingyue Wang, Qinqin Huang, Haifeng Hu, Ming Ling, and
Jiansheng Wu. Vina-GPU 2.0: Further Accelerating AutoDock Vina and Its Derivatives with
Graphics Processing Units.Journal of Chemical Information and Modeling, 63(7):1982–1998,
2023. doi: 10.1021/acs.jcim.2c01504. URLhttps://doi.org/10.1021/acs.jcim.
2c01504.
Keyan Ding, Jing Yu, Junjie Huang, Yuchen Yang, Qiang Zhang, and Huajun Chen. SciToolAgent: a
knowledge-graph-driven scientific agent for multitool integration.Nature Computational Science,
5(10):962–972, 2025. doi: 10.1038/s43588-025-00849-y. URLhttps://doi.org/10.
1038/s43588-025-00849-y.
Ian Dunn and David R. Koes. FlowMol3: flow matching for 3D de novo small-molecule generation.
Digital Discovery, 5(5):2052–2066, 2026. doi: 10.1039/D5DD00363F. URLhttps://doi.
org/10.1039/D5DD00363F.
Jerome Eberhardt, Diogo Santos-Martins, Andreas F. Tillack, and Stefano Forli. AutoDock Vina
1.2.0: New Docking Methods, Expanded Force Field, and Python Bindings.Journal of Chem-
ical Information and Modeling, 61(8):3891–3898, 2021. doi: 10.1021/acs.jcim.1c00203. URL
https://doi.org/10.1021/acs.jcim.1c00203.
Peter Ertl and Ansgar Schuffenhauer. Estimation of synthetic accessibility score of drug-like
molecules based on molecular complexity and fragment contributions.Journal of Cheminfor-
matics, 1(1):8, 2009. doi: 10.1186/1758-2946-1-8. URLhttps://doi.org/10.1186/
1758-2946-1-8.
Vendy Fialkov´a, Jiaxi Zhao, Kostas Papadopoulos, Ola Engkvist, Esben Jannik Bjerrum, Thierry
Kogej, and Atanas Patronov. LibINVENT: Reaction-based Generative Scaffold Decoration for
in Silico Library Design.Journal of Chemical Information and Modeling, 62(9):2046–2063,
2022. doi: 10.1021/acs.jcim.1c00469. URLhttps://doi.org/10.1021/acs.jcim.
1c00469.
Yao Fu, Dong-Ki Kim, Jaekyeom Kim, Sungryull Sohn, Lajanugen Logeswaran, Kyunghoon Bae,
and Honglak Lee. AutoGuide: Automated generation and selection of context-aware guide-
lines for large language model agents. In A. Globerson, L. Mackey, D. Belgrave, A. Fan,
U. Paquet, J. Tomczak, and C. Zhang (eds.),Advances in Neural Information Processing
Systems, volume 37, pp. 119919–119948. Curran Associates, Inc., 2024. doi: 10.52202/
10

079017-3811. URLhttps://proceedings.neurips.cc/paper_files/paper/
2024/file/d8efbb5dd415974eb095c3f06bff1f48-Paper-Conference.pdf.
Bowen Gao, Yanwen Huang, Yiqiao Liu, Wenxuan Xie, Wei-Ying Ma, Ya-Qin Zhang, and Yanyan
Lan. PharmAgents: Building a Virtual Pharma with Large Language Model Agents, 2025a. URL
https://arxiv.org/abs/2503.22164v2.
Jianjiong Gao, B ¨ulent Arman Aksoy, Ugur Dogrusoz, Gideon Dresdner, Benjamin Gross, S. Onur
Sumer, Yichao Sun, Anders Jacobsen, Rileen Sinha, Erik Larsson, et al. Integrative Analysis of
Complex Cancer Genomics and Clinical Profiles Using the cBioPortal.Science Signaling, 6(269),
2013. doi: 10.1126/scisignal.2004088. URLhttps://doi.org/10.1126/scisignal.
2004088.
Shanghua Gao, Richard Zhu, Pengwei Sui, Zhenglun Kong, Sufian Aldogom, Yepeng Huang,
Ayush Noori, Reza Shamji, Krishna Parvataneni, Theodoros Tsiligkaridis, and Marinka Zit-
nik. ToolUniverse: An open platform for democratizing AI scientists, 2025b. URLhttps:
//arxiv.org/abs/2509.23426v3.
Mahdi Ghorbani, Leo Gendelev, Paul Beroza, and Michael J. Keiser. Autoregressive fragment-based
diffusion for pocket-aware ligand design.arXiv, 2024. doi: 10.48550/arXiv.2401.05370. URL
https://doi.org/10.48550/arXiv.2401.05370.
Kevin Han, Renfei Zhang, Kathy Wei, Hamed Mahdavi, Niloofar Mireshghallah, and Amir Barati
Farimani. SMDD-Bench: Can LLMs solve real-world small molecule drug design tasks?arXiv
preprint arXiv:2605.21740, 2026.
Jiazhen He, Eva Nittinger, Christian Tyrchan, Werngard Czechtizky, Atanas Patronov, Esben Jannik
Bjerrum, and Ola Engkvist. Transformer-based molecular optimization beyond matched molecu-
lar pairs.Journal of Cheminformatics, 14(1):18, 2022. doi: 10.1186/s13321-022-00599-3. URL
https://doi.org/10.1186/s13321-022-00599-3.
Yu He and Weikai Yang. SkillCommit: Evolving Agent Skills through Behaviorally Validated Scope
Expansion, 2026. URLhttps://arxiv.org/abs/2608.15165v1.
Kexin Huang, Tianfan Fu, Wenhao Gao, Yue Zhao, Yusuf Roohani, Jure Leskovec, Connor W.
Coley, Cao Xiao, Jimeng Sun, and Marinka Zitnik. Therapeutics data commons: Machine
learning datasets and tasks for drug discovery and development. InProceedings of the
Neural Information Processing Systems Track on Datasets and Benchmarks, 2021. URL
https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/
hash/4c56ff4ce4aaf9573aa5dff913df997a-Abstract-round1.html.
Kexin Huang, Serena Zhang, Hanchen Wang, Yuanhao Qu, Yingzhou Lu, Ryan Li, Yusuf Roohani,
Lin Qiu, Shiyi Cao, Gavin Li, Junze Zhang, Di Yin, Rick Wierenga, Deniz Kavi, Sherry Liu,
Tianwei She, Shruti Marwaha, Jennefer N. Carter, Xin Zhou, Matthew T. Wheeler, Jonathan A.
Bernstein, Mengdi Wang, Peng He, Jingtian Zhou, Michael P. Snyder, Le Cong, Aviv Regev, and
Jure Leskovec. Autonomous biomedical research with an artificial intelligence agent.Science,
393(6813):eadz4351, 2026. doi: 10.1126/science.adz4351. URLhttps://doi.org/10.
1126/science.adz4351.
Sofia Karlstr ¨om, Gunnar Nordvall, Daniel Sohn, Andreas Hettman, Dominika Turek, Kristofer
˚Ahlin, Annika Kers, Martina Claesson, Can Slivo, Yvonne Lo-Alfredsson, Carl Petersson, Galina
Bessidskaia, Per H. Svensson, Tobias Rein, Eva Jerning, ˚Asa Malmberg, Charlotte Ahlgen, Colin
Ray, Lauri Vares, Vladimir Ivanov, and Rolf Johansson. Substituted 7-amino-5-thio-thiazolo[4,5-
d]pyrimidines as potent and selective antagonists of the fractalkine receptor (CX 3CR1).Journal
of Medicinal Chemistry, 56(8):3177–3190, 2013. doi: 10.1021/jm3012273.
Sunghwan Kim, Jie Chen, Tiejun Cheng, Asta Gindulyte, Jia He, Siqian He, Qingliang Li, Ben-
jamin A Shoemaker, Paul A Thiessen, Bo Yu, et al. PubChem 2025 update.Nucleic Acids
Research, 53(D1):D1516–D1525, 2025. doi: 10.1093/nar/gkae1059. URLhttps://doi.
org/10.1093/nar/gkae1059.
KinHub. KinHub: Human kinases.https://www.kinhub.org/kinases.html. Human
kinase annotation resource.
11

Radoslav Kriv ´ak and David Hoksza. P2Rank: machine learning based tool for rapid and ac-
curate prediction of ligand binding sites from protein structure.Journal of Cheminformatics,
10(1):39, 2018. doi: 10.1186/s13321-018-0285-8. URLhttps://doi.org/10.1186/
s13321-018-0285-8.
Melissa J Landrum, Shanmuga Chitipiralla, Kuljeet Kaur, Garth Brown, Chao Chen, Jennifer Hart,
Douglas Hoffman, Wonhee Jang, Chunlei Liu, Zenith Maddipatla, et al. ClinVar: updates to
support classifications of both germline and somatic variants.Nucleic Acids Research, 53(D1):
D1313–D1321, 2025. doi: 10.1093/nar/gkae1090. URLhttps://doi.org/10.1093/
nar/gkae1090.
Catherine L Lawson, Helen M Berman, Li Chen, Brinda Vallat, and Craig L Zirbel. The Nucleic
Acid Knowledgebase: a new portal for 3D structural information about nucleic acids.Nucleic
Acids Research, 52(D1):D245–D254, 2024. doi: 10.1093/nar/gkad957. URLhttps://doi.
org/10.1093/nar/gkad957.
Vincent Le Guilloux, Peter Schmidtke, and Pierre Tuffery. Fpocket: An open source platform for
ligand pocket detection.BMC Bioinformatics, 10(1):168, 2009. doi: 10.1186/1471-2105-10-168.
URLhttps://doi.org/10.1186/1471-2105-10-168.
Hao Li, He Cao, Bin Feng, Yanjun Shao, Xiangru Tang, Zhiyuan Yan, Yonghong Tian, Li Yuan,
and Yu Li. Beyond chemical QA: Evaluating LLM's chemical reasoning with modular chemical
operations. In D. Belgrave, C. Zhang, H. Lin, R. Pascanu, P. Koniusz, M. Ghassemi, and N. Chen
(eds.),Advances in Neural Information Processing Systems, Datasets and Benchmarks Track,
volume 38. Curran Associates, Inc., 2025. doi: 10.52202/085713-5122.
Lingxiao Li, Haobo Zhang, Ruohao Fan, Bin Chen, and Jiayu Zhou. Molecular Lead Optimization
via Agentic Tool Planning. InProceedings of the 32nd ACM SIGKDD Conference on Knowledge
Discovery and Data Mining V .2, pp. 11328–11338, 2026. doi: 10.1145/3770855.3819017. URL
https://doi.org/10.1145/3770855.3819017.
Tiqing Liu, Linda Hwang, Stephen K Burley, Carmen I Nitsche, Christopher Southan, W Patrick
Walters, and Michael K Gilson. BindingDB in 2024: a FAIR knowledgebase of protein-small
molecule binding data.Nucleic Acids Research, 53(D1):D1633–D1644, 2025. doi: 10.1093/nar/
gkae1075. URLhttps://doi.org/10.1093/nar/gkae1075.
Hannes H. Loeffler, Jiazhen He, Alessandro Tibo, Jon Paul Janet, Alexey V oronov, Lewis H.
Mervin, and Ola Engkvist. Reinvent 4: Modern AI–driven generative molecule design.Jour-
nal of Cheminformatics, 16(1):20, 2024. doi: 10.1186/s13321-024-00812-5. URLhttps:
//doi.org/10.1186/s13321-024-00812-5.
Milot Mirdita, Konstantin Sch ¨utze, Yoshitaka Moriwaki, Lim Heo, Sergey Ovchinnikov, and Mar-
tin Steinegger. ColabFold: making protein folding accessible to all.Nature Methods, 19(6):
679–682, 2022. doi: 10.1038/s41592-022-01488-1. URLhttps://doi.org/10.1038/
s41592-022-01488-1.
Jingwei Ni, Yihao Liu, Xinpeng Liu, Yutao Sun, Mengyu Zhou, Pengyu Cheng, Dexin Wang, Er-
chao Zhao, Xiaoxi Jiang, and Guanjun Jiang. Trace2Skill: Distill Trajectory-Local Lessons into
Transferable Agent Skills, 2026. URLhttps://arxiv.org/abs/2603.25158v5. Read-
ing version: 2603.25158v5.
Nous Research. Hermes Agent, 2026. URLhttps://github.com/NousResearch/
hermes-agent. Software repository. Accessed October 16, 2026.
OpenAI. Codex, 2026. URLhttps://github.com/openai/codex. Software repository.
Accessed October 16, 2026.
Saro Passaro, Gabriele Corso, Jeremy Wohlwend, Mateo Reveiz, Stephan Thaler, Vignesh Ram
Somnath, Noah Getz, Tally Portnoi, Julien Roy, Hannes Stark, et al. Boltz-2: Towards Accurate
and Efficient Binding Affinity Prediction.bioRxiv, 2025. doi: 10.1101/2025.06.14.659707. URL
https://doi.org/10.1101/2025.06.14.659707.
12

PDBFixer contributors. PDBFixer. URLhttps://github.com/openmm/pdbfixer. Soft-
ware resource.
RDKit contributors. RDKit: Open-source cheminformatics. URLhttps://www.rdkit.org.
Software resource.
Summer Rosonovski, Maria Levchenko, Rajat Bhatnagar, Umamageswari Chandrasekaran, Lynne
Faulk, Islam Hassan, Matt Jeffryes, Syed Irtaza Mubashar, Maaly Nassar, Madhumiethaa
Jayaprabha Palanisamy, et al. Europe PMC in 2023.Nucleic Acids Research, 52(D1):D1668–
D1676, 2024. doi: 10.1093/nar/gkad1085. URLhttps://doi.org/10.1093/nar/
gkad1085.
Lakshidaa Saigiridharan, Alan Kai Hassen, Helen Lai, Paula Torren-Peraire, Ola Engkvist,
and Samuel Genheden. AiZynthFinder 4.0: developments based on learnings from 3 years
of industrial application.Journal of Cheminformatics, 16(1):57, 2024. doi: 10.1186/
s13321-024-00860-x. URLhttps://doi.org/10.1186/s13321-024-00860-x.
Diogo Santos-Martins, Yiran He, Jerome Eberhardt, Parnika Sharma, Niccol`o Bruciaferri, Matthew
Holcomb, Manuel A. Llanos, Althea Hansel-Harris, Allison Pearl Barkdull, Andreas Frank
Tillack, et al. Meeko: Molecule Parametrization and Software Interoperability for Docking
and Beyond.Journal of Chemical Information and Modeling, 65(24):13045–13050, 2025. doi:
10.1021/acs.jcim.5c02271. URLhttps://doi.org/10.1021/acs.jcim.5c02271.
Philipp Schake, Sarah Naomi Bolz, Katja Linnemann, and Michael Schroeder. PLIP 2025: in-
troducing protein–protein interactions to the protein–ligand interaction profiler.Nucleic Acids
Research, 53(W1):W463–W465, 2025. doi: 10.1093/nar/gkaf361. URLhttps://doi.org/
10.1093/nar/gkaf361.
Arne Schneuing, Charles Harris, Yuanqi Du, Kieran Didi, Arian Jamasb, Ilia Igashov, Weitao Du,
Carla Gomes, Tom L. Blundell, Pietro Lio, et al. Structure-based drug design with equivari-
ant diffusion models.Nature Computational Science, 4(12):899–909, 2024. doi: 10.1038/
s43588-024-00737-x. URLhttps://doi.org/10.1038/s43588-024-00737-x.
Kyle Swanson, Parker Walther, Jeremy Leitz, Souhrid Mukherjee, Joseph C Wu, Rabindra V Shiv-
naraine, and James Zou. ADMET-AI: a machine learning ADMET platform for evaluation of
large-scale chemical libraries.Bioinformatics, 40(7):btae416, 2024. doi: 10.1093/bioinformatics/
btae416. URLhttps://doi.org/10.1093/bioinformatics/btae416.
Damian Szklarczyk, Rebecca Kirsch, Mikaela Koutrouli, Katerina Nastou, Farrokh Mehryary, Radja
Hachilif, Annika L Gable, Tao Fang, Nadezhda T Doncheva, Sampo Pyysalo, et al. The STRING
database in 2023: protein–protein association networks and functional enrichment analyses for
any sequenced genome of interest.Nucleic Acids Research, 51(D1):D638–D646, 2023. doi:
10.1093/nar/gkac1000. URLhttps://doi.org/10.1093/nar/gkac1000.
Liyan Tang, Cyrus Rashtchian, Chun-Sung Ferng, Andrew Tomkins, Da-Cheng Juan, and Tu Vu.
WikiSkill: Compiling Agent Experience into Persistent Knowledge for Skill Evolution, 2026a.
URLhttps://arxiv.org/abs/2608.27454v1. Reading version: 2608.27454v1.
Shidi Tang, Ji Ding, Xiangyu Zhu, Zheng Wang, Haitao Zhao, and Jiansheng Wu. Vina-GPU 2.1:
Towards Further Optimizing Docking Speed and Precision of AutoDock Vina and Its Deriva-
tives.IEEE/ACM Transactions on Computational Biology and Bioinformatics, 21(6):2382–2393,
2024. doi: 10.1109/TCBB.2024.3467127. URLhttps://doi.org/10.1109/TCBB.
2024.3467127.
Xiangru Tang, Tianyu Hu, Muyang Ye, Yanjun Shao, Xunjian Yin, Siru Ouyang, Wangchunshu
Zhou, Pan Lu, Zhuosheng Zhang, Yilun Zhao, Arman Cohan, and Mark Gerstein. ChemAgent:
Self-updating library in large language models improves chemical reasoning. In Y . Yue, A. Garg,
N. Peng, F. Sha, and R. Yu (eds.),International Conference on Learning Representations, volume
2025, pp. 100922–100958, 2025.
Yuqi Tang, Chenyi Zhou, Libin Wang, Keyan Ding, Qiang Zhang, and Huajun Chen. SciToolAgent-
Evo: An Ontology-Aware Self-Evolving Agent for Open-World Scientific Tool Acquisition,
2026b. URLhttps://arxiv.org/abs/2607.28692v1.
13

The ENCODE Project Consortium. Expanded encyclopaedias of DNA elements in the human and
mouse genomes.Nature, 583(7818):699–710, 2020. doi: 10.1038/s41586-020-2493-4. URL
https://doi.org/10.1038/s41586-020-2493-4.
The GTEx Consortium. The GTEx Consortium atlas of genetic regulatory effects across human
tissues.Science, 369(6509):1318–1330, 2020. doi: 10.1126/science.aaz1776. URLhttps:
//doi.org/10.1126/science.aaz1776.
The UniProt Consortium. UniProt: the Universal Protein Knowledgebase in 2025.Nucleic Acids
Research, 53(D1):D609–D617, 2025. doi: 10.1093/nar/gkae1010. URLhttps://doi.org/
10.1093/nar/gkae1010.
Oleg Trott and Arthur J. Olson. AutoDock Vina: Improving the speed and accuracy of docking with
a new scoring function, efficient optimization, and multithreading.Journal of Computational
Chemistry, 31(2):455–461, 2010. doi: 10.1002/jcc.21334. URLhttps://doi.org/10.
1002/jcc.21334.
Mihaly Varadi, Damian Bertoni, Paulyna Magana, Urmila Paramval, Ivanna Pidruchna, Malarvizhi
Radhakrishnan, Maxim Tsenkov, Sreenath Nair, Milot Mirdita, Jingi Yeo, et al. AlphaFold Protein
Structure Database in 2024: providing structure coverage for over 214 million protein sequences.
Nucleic Acids Research, 52(D1):D368–D375, 2024. doi: 10.1093/nar/gkad1011. URLhttps:
//doi.org/10.1093/nar/gkad1011.
Sameer Velankar, Jos´e M. Dana, Julius Jacobsen, Glen van Ginkel, Paul J. Gane, Jie Luo, Thomas J.
Oldfield, Claire O’Donovan, Maria-Jesus Martin, and Gerard J. Kleywegt. SIFTS: Structure
Integration with Function, Taxonomy and Sequences resource.Nucleic Acids Research, 41(D1):
D483–D489, 2013. doi: 10.1093/nar/gks1258. URLhttps://doi.org/10.1093/nar/
gks1258.
Zhu Wang, Jiangyu Chen, Yingjun Shang, Yuhui Yao, Laiao Lu, Tianfan Fu, and Na Zou. Cai copi-
lot: Reducing operational workload in molecular design through intent-driven agentic workflows.
arXiv preprint arXiv:2608.06961, 2026.
John D. Westbrook, Chenghua Shao, Zukang Feng, Marina Zhuravleva, Sameer Velankar, and Jas-
mine Young. The chemical component dictionary: complete descriptions of constituent molecules
in experimentally determined 3D macromolecules in the Protein Data Bank.Bioinformatics, 31
(8):1274–1278, 2015. doi: 10.1093/bioinformatics/btu789. URLhttps://doi.org/10.
1093/bioinformatics/btu789.
Jeremy Wohlwend, Gabriele Corso, Saro Passaro, Noah Getz, Mateo Reveiz, Ken Leidal, Wo-
jtek Swiderski, Liam Atkinson, Tally Portnoi, Itamar Chinn, et al. Boltz-1 Democratizing
Biomolecular Interaction Modeling.bioRxiv, 2024. doi: 10.1101/2024.11.19.624167. URL
https://doi.org/10.1101/2024.11.19.624167.
Yifan Yang, Ziyang Gong, Weiquan Huang, Qihao Yang, Ziwei Zhou, Zisu Huang, Yan Li, Xuemei
Gao, Qi Dai, Bei Liu, Kai Qiu, Yuqing Yang, Dongdong Chen, Xue Yang, and Chong Luo.
SkillOpt: Executive Strategy for Self-Evolving Agent Skills, 2026. URLhttps://arxiv.
org/abs/2605.23904v2. Reading version: 2605.23904v2.
Barbara Zdrazil, Eloy Felix, Fiona Hunter, Emma J Manners, James Blackshaw, Sybilla Corbett,
Marleen de Veij, Harris Ioannidis, David Mendez Lopez, Juan F Mosquera, et al. The ChEMBL
Database in 2023: a drug discovery platform spanning multiple bioactivity data types and time
periods.Nucleic Acids Research, 52(D1):D1180–D1192, 2024. doi: 10.1093/nar/gkad1004. URL
https://doi.org/10.1093/nar/gkad1004.
Lisheng Zhang, Lilong Wang, Xiangyu Sun, Wei Tang, Haoyang Su, Yuehui Qian, Qikui Yang,
Qingsong Li, Zhenyu Tang, Haoran Sun, Yingnan Han, Yankai Jiang, Wenjie Lou, Bowen
Zhou, Xiaosong Wang, Lei Bai, and Zhengwei Xie. MolClaw: An autonomous agent with
hierarchical skills for drug molecule evaluation, screening, and optimization.arXiv preprint
arXiv:2604.21937, 2026a. URLhttps://arxiv.org/abs/2604.21937v2.
14

Lisheng Zhang, Lilong Wang, Xiangyu Sun, Wei Tang, Haoyang Su, Yuehui Qian, Qikui Yang,
Qingsong Li, Zhenyu Tang, Haoran Sun, et al. MolClaw: An autonomous agent with hierarchical
skills for drug molecule evaluation, screening, and optimization.bioRxiv, 2026b. doi: 10.64898/
2026.04.03.716272. URLhttps://www.biorxiv.org/content/10.64898/2026.
04.03.716272v1.
Qizheng Zhang, Changran Hu, Shubhangi Upasani, Boyuan Ma, Fenglu Hong, Vamsidhar Ka-
manuru, Jay Rainton, Chen Wu, Mengmeng Ji, Hanchen Li, Urmish Thakker, James Y Zou,
and Kunle Olukotun. Agentic context engineering: Evolving contexts for self-improving lan-
guage models. In C. V ondrick, B. Hariharan, C. Raffel, L. Pinto, D. Yang, and A. Faust
(eds.),International Conference on Learning Representations, volume 2026, pp. 86069–86100,
2026c. URLhttps://proceedings.iclr.cc/paper_files/paper/2026/file/
8a94ff6f922d995d7d3f4ebf4143e442-Paper-Conference.pdf.
Yikun Zhang, Xiwei Cheng, Tianyu Liu, Yuanqi Du, and Wengong Jin. DrugSAGE: Self-
evolving Agent Experience for Efficient State-of-the-Art Drug Discovery, 2026d. URLhttps:
//arxiv.org/abs/2605.15461v1. Reading version: 2605.15461v1.
Andrew Zhao, Daniel Huang, Quentin Xu, Matthieu Lin, Yong-Jin Liu, and Gao Huang. ExpeL:
LLM Agents Are Experiential Learners. InProceedings of the AAAI Conference on Artificial
Intelligence, volume 38, pp. 19632–19642, 2024.
Ying Zhou, Yintao Zhang, Donghai Zhao, Xinyuan Yu, Xinyi Shen, Yuan Zhou, Shanshan Wang,
Yunqing Qiu, Yuzong Chen, and Feng Zhu. TTD: Therapeutic Target Database describing target
druggability information.Nucleic Acids Research, 52(D1):D1465–D1477, 2024. doi: 10.1093/
nar/gkad751. URLhttps://doi.org/10.1093/nar/gkad751.
15

A BENCHMARK ANDEVALUATIONDETAILS
This section summarizes the task definitions and evaluation quantities of the source benchmarks.
Table 2 uses literature-reported baselines. The SMDD baselines combine published runs, with LO
reaggregated on our fixed 40-task subset, and our Terra evaluation of the original harness.
A.1 MOLBENCH
Task coverage.The 190 MolBench tasks comprise 35 property-filtering, 15 similarity-filtering, 37
affinity-comparison, 25 ranking, 39 editing, and 39 optimization tasks.
Screening.MolBench-MS includes molecular property filtering, binding-affinity comparison, and
docking-based screening (Zhang et al., 2026b). Property filtering selects molecules satisfying the
supplied constraints from ten candidates. Binding-affinity comparison selects one of two molecules
using a target-specific criterion, with experimentalK i defining the reference order. Docking screen-
ing ranks 60 candidates per task, including experimentally active and inactive molecules. The source
study defines mean Hits@3 as
MeanHits@3 = 1 n
nX
i=1
|Top3(i)∩A i|,(7)
whereA i is the active set for taski.
Combined comparison.Table 2 combines the Sonnet baselines reported in MolClaw with the Qwen
baselines reported in CAi and the three DrugHarness NoSkill configurations. The first MolClaw-
group column is the reported Claude Code baseline without MolClaw skills.
Table notation.All proportion metrics in the MolBench tables are percentages. Acc., Prec., Spec.,
and Valid denote accuracy, precision, specificity, and validity; SR denotes success rate. Hit@3 is the
percentage of ranking tasks with at least one active molecule in the top three, whereas Mean Hits@3
is the mean active-molecule count. Top-3 rate is Mean Hits@3 divided by three, expressed as a
percentage; Count gives successful tasks over the total. Mean GT rank is the mean predicted rank of
the reference top-three molecules. In affinity comparison, Valid measures valid candidate choices.
In editing, Subst. denotes substitution and Overall aggregates editing operations. Optimization
Valid is the valid-SMILES percentage; Hard and Soft denote the two scaffold-retention measures.
Percentages are displayed to one decimal place; calculations retain the underlying values.
Editing and optimization.MolBench-MO distinguishes functional-group editing from physico-
chemical property optimization. Editing accuracy is the fraction of outputs satisfying all requested
modifications. Optimization concerns QED, LogP, or LogS and reports both a property-change
quantity and success against predefined criteria. The editing experiment contains 39 tasks. Opti-
mization success uses positive native improvement over 39 tasks. Table 4 reports ordinary means of
saved per-task gains separately by property.
Table 4:Property optimization with Codex/Terra.Valid pairs denote valid scoring pairs; scaffold
retention uses the hard criterion.
Property Tasks Valid pairs Positive gain Mean gain Scaffold
retained
LogP 11 10 10 0.9260 4/11
QED 20 19 19 0.3748 3/20
Solubility 8 8 8 0.7089 7/8
Across the 39 tasks, the hard scaffold-retention rate is 35.90% and mean soft scaffold retention
is 0.6360. These quantities describe structural preservation separately from the 94.9% property-
improvement success rate.
A.2 COMPLETEEVOLUTIONRESULTS
Table 5 reports all 23 MolBench metrics for the Qwen3.7-Max configurations compared in Table 3.
16

Table 5:Complete MolBench evolution metrics.Both configurations use Codex/Qwen3.7-Max.
Proportions are percentages; the mean∆is the descriptive task-wise mean of saved native improve-
ments.
Metric w/o Evol. Evol.
Screening
Accuracy (%)↑96.0 100.0
Precision (%)↑98.0 100.0
Recall (%)↑97.0 100.0
F1 (%)↑97.3 100.0
Specificity (%)↑100.0 100.0
Validity (%)↑98.0 100.0
Affinity comparison
Accuracy (%)↑62.2 81.1
Valid choice (%)↑100.0 97.3
Virtual screening
Hit@3 (%)↑60.0 48.0
Mean Hits@3↑0.72 0.64
Top-3 rate (%)↑24.0 21.3
Mean GT rank↓29.05 26.01
Hit count↑15/25 12/25
Editing
Add (%)↑100.0 100.0
Delete (%)↑100.0 100.0
Substitute (%)↑95.0 95.0
Overall (%)↑97.4 97.4
Validity (%)↑100.0 100.0
Optimization
Mean∆↑0.6054 0.7213
Success rate (%)↑79.5 87.2
Valid SMILES (%)↑87.2 100.0
Scaffold hard (%)↑38.5 48.7
Scaffold soft (%)↑61.8 69.0
A.3 SMDD-BENCH
Our evaluation includes the complete Types 1–3 and 5 and the 40-task LO subset described be-
low. Table abbreviations are 2D Pharm. (2D pharmacophore identification), IP (interaction point
discovery), SH (scaffold hopping), LO (lead optimization), and FA (fragment assembly). The five
source families contain 25, 25, 52, 340, and 60 instances, respectively (Han et al., 2026). The overall
success rate is the fraction of successful instances across these families, rather than an unweighted
average of family-level rates.
2D pharmacophore identification.The input comprises a protein sequence and ten active and ten
inactive molecules. The output is a Python predicate that classifies a supplied molecular SMILES
string. Evaluation measures recall on hidden active molecules and specificity on hidden inactive
molecules.
Interaction point discovery.Given a receptor and pocket specification, the agent submits three
typed three-dimensional points. Type-compatible points are matched one-to-one to reference inter-
action sites using a distance criterion of less than2.5 ˚A. Partial credit equals the number of matched
points divided by three; success requires all three matches.
Scaffold hopping.The output is a molecule with a different scaffold but preserved binding inter-
actions. The detailed evaluator requires molecular validity, Morgan-fingerprint Tanimoto similarity
below0.5, a scaffold maximum-common-substructure ratio below0.65, interaction-fingerprint sim-
ilarity above0.75, and predicted binding probability above0.7.
17

Lead optimization.The agent modifies a reference molecule while satisfying task-specific im-
provement targets, hold-constant intervals, and hard constraints. Evaluation jointly checks molec-
ular validity, scaffold similarity, the property requirements, and predicted binding conditions. The
reference-similarity threshold is at least0.7. Property directions and tolerances belong to individual
task specifications.
LO subset selection.DrugHarness uses a fixed subset of 40 LO tasks spanning 25 targets, with one
or two tasks per target. Six previously selected tasks and a designated DHODH task were retained.
Additional tasks were selected to cover optimization directions, objective counts, and structural
input sizes using public task inputs, with natural task identifiers breaking ties. The subset con-
tains 9/9/9/8/5 tasks with one/two/three/four/five objectives, respectively. Structure sizes comprise
10/18/12 tasks with at most 200, 201–500, and more than 500 ATOM-record residues.
Fragment assembly.One or two spatially placed fragments must be retained within a valid output
molecule. Evaluation checks fragment containment, connectivity where required, hard constraints,
predicted binding probability above0.7, affinity within0.1log units of the witness reference, and
fragment RMSD below2.0 ˚A. Topological containment alone is insufficient.
18

B SCIENTIFICTOOLS ANDCOMPUTATIONALENVIRONMENT
B.1 SCIENTIFICCAPABILITIES
DrugHarness provides a scientific environment spanning biomedical evidence retrieval, molecular
design, and computational evaluation. Table 6 groups representative tools and resources by scientific
function and summarizes their inputs and outputs. Operations can be invoked independently and
combined according to the task, without imposing a fixed sequence of stages.
Table 6:Scientific capabilities of DrugHarness.Representative tools and resources supporting
over 80 agent-accessible scientific operations are organized into ten capability categories. A tool
may support multiple operations; entries summarize capabilities rather than enumerate individual
interfaces.
Capability Tools and resources Inputs→outputs
Biomedical
evidence retrieval
Open Targets (Buniello et al., 2025);
cBioPortal (Cerami et al., 2012; Gao et al.,
2013); TTD (Zhou et al., 2024); ClinVar
(Landrum et al., 2025); GTEx
(The GTEx Consortium, 2020); ENCODE
(The ENCODE Project Consortium, 2020);
STRING (Szklarczyk et al., 2023); Europe
PMC (Rosonovski et al., 2024);
ClinicalTrials.gov and FDA record
interfaces.
Disease, target, variant, or
experimental context→associations,
variants, expression, functional and
network evidence, publications, and
study records with provenance.
Target identity and
structural data
UniProt (The UniProt Consortium, 2025);
RCSB PDB (Burley et al., 2022); SIFTS
(Velankar et al., 2013); AlphaFold DB
(Varadi et al., 2024); NAKB (nucleic-acid
structures) (Lawson et al., 2024); KinHub
(KinHub).
Names, sequences, or database
identifiers→target identities,
sequences, structure candidates and
coordinates, chain/residue mappings,
and family annotations.
Receptor, ligand,
and pocket
preparation
PDBFixer (PDBFixer contributors); Meeko
(Santos-Martins et al., 2025); RDKit
(RDKit contributors); CCD
(Westbrook et al., 2015); fpocket
(Le Guilloux et al., 2009); P2Rank
(Kriv´ak & Hoksza, 2018).
Protein/ligand structures, component
selections, and preparation parameters
→prepared receptors and ligand
states, pocket candidates, docking
grids, and input files.
Interaction and
pharmacophore
analysis
PLIP (Schake et al., 2025); ProLIF
(Bouysset & Fiorucci, 2021); RDKit; atomic
geometry analysis and co-crystal
alignment/clustering.
Complexes, structural ensembles, or
labeled molecules→contacts,
water-mediated paths, interaction
fingerprints, conserved
three-dimensional interaction points,
and molecular features.
Compound sources
and activity
evidence
ChEMBL (Zdrazil et al., 2024); BindingDB
(Liu et al., 2025); PubChem (Kim et al.,
2025); local-library similarity search;
Google Patents retrieval by publication
number.
Target/compound identifiers, reference
molecules, or patent publication
numbers→chemical identities,
measured activities with assay context,
candidate rankings, or patent
documents.
Molecule
generation and
fragment linking
DiffSBDD (Schneuing et al., 2024);
FlowMol3 (Dunn & Koes, 2026);
AutoFragDiff (Ghorbani et al., 2024);
explicit molecular-graph linking.
Generation settings, optional pocket
context, or fragments with attachment
sites→three-dimensional candidates,
fragment mappings, and
linked-molecule proposals.
Continued on next page
19

Table 6 (continued)
Capability Tools and resources Inputs→outputs
Docking, rescoring,
and binding
prediction
AutoDock Vina (Trott & Olson, 2010;
Eberhardt et al., 2021); QuickVina2-GPU
2.1 (Tang et al., 2024; Ding et al., 2023);
EquiScore (Cao et al., 2024); Boltz-2
(Passaro et al., 2025; Wohlwend et al.,
2024); MSA preparation (Mirdita et al.,
2022).
Receptors, ligands, grids/pockets,
sequences, and required MSAs→
poses, rescoring results, predicted
complexes, binding-related values, and
confidence estimates.
Molecular
processing and
property
assessment
RDKit; ESOL (ChemCoTBench refit)
(Delaney, 2004; Li et al., 2025);
PyTDC-compatible penalized LogP
(Huang et al., 2021; Ertl & Schuffenhauer,
2009); ADMET-AI (Swanson et al., 2024).
SMILES/SDF, candidate sets, and
calculation parameters→standardized
molecules, physicochemical
properties, structural alerts,
similarities, solubility, and ADMET
predictions.
Molecular editing
and optimization
proposals
Explicit molecular-graph editing;
REINVENT4 (Loeffler et al., 2024);
Mol2Mol (He et al., 2022); LibINVENT
(Fialkov´a et al., 2022).
Starting molecules, scaffolds, edit
requests, or generation settings→
edited candidates, scaffold
decorations, analogues, and
operation-integrity diagnostics.
Retrosynthetic
analysis
AiZynthFinder (Saigiridharan et al., 2024). Target molecules, stock, and search
settings→candidate retrosynthetic
routes, stock matches, and search
results.
20

C SKILLLEARNINGALGORITHMS
The main loop combines hypothesis induction, independent scientific review, version updates, and
revision from subsequent-task feedback. The induction subroutine specifies how scientific condi-
tions and evidence shape a proposed action change.
Algorithm 1Skill learning and revision from scientific experience
Require:ExperiencesE, insightsL, skillsK, historyV, scopeΩ, budgetB
Ensure:Admitted skill versions, revisedL,E, andV
1:foreach development batchB t withinΩandBdo
2:Incorporate trajectories and permitted native feedback already produced by task runs intoE.
3:( eL, h)←Induce(B t, L, K, V; Ω,Bt)▷One candidate branch
4:L← eL
5:ifh=∅then
6:SaveLand unresolved records; updateV;continue.
7:end if
8:K ′ ←Edit(K, h); retain parentK, full content, sources, and intended change.
9:An independent review agent checks sources, conditions, and executable instructions.
10:Use the shared scientific tools or code for targeted local trials when needed; retain trial
evidence.
11:CompleteReview(K ′, h, Rh; Ω)and recordρ, or record incomplete status.
12:ifreview completed andρ= admitthen
13:Record the admitted versionK ′ for subsequent tasks bound explicitly to that version.
14:K←K ′ for this branch.
15:else
16:KeepK; record rejection, deferral, or incomplete status.
17:end if
18:ReviseL, Vusing the proposal and review records actually available.
19:ifthe stage stopping condition is metthen
20:break
21:end if
22:end for
23:Add subsequent task trajectories and permitted native feedback toEwhen produced.
Multiple proposal directions may be constructed and reviewed in parallel as separate branches. The
update above describes one branch; its admission applies to the complete version reviewed, with no
automatic merge of separately admitted candidates.
Algorithm 2Inducing a conditional action hypothesis
Require:BatchB t, insightsL, skillsK, historyV, scopeΩ, allowanceB t
Ensure:Revised insights eLand one hypothesishor∅
1:Identify recurring decision problems withinΩfrom actions and observations.
2:Separate contemporaneous observations, agent interpretations, and later feedback.
3:Check the scientific objects, endpoints, and result states.
4:Compare decision-relevant conditions; reread permitted sources for specific questions within
Bt.
5:Combine support for compatible conditions and consistent recommendations; retain separate
scopes for different conditions.
6:For conflicts under comparable conditions, narrow or split guidance when justified; otherwise
retain disagreement and uncertainty.
7:Compare withKandVto identify existing coverage and prior revision feedback.
8:ReviseLto obtain eL; propose(g, c, a0, a, R, U)for a testable gap, specifying the expected
action difference.
9:Return one direction for this candidate branch and retain other directions for separate branches;
return∅if no reusable modification is identified.
21

D CASESTUDIES
These cases follow scientific work in DrugHarness from candidate assessment to guidance refine-
ment: coordinating evaluations around a shared molecule, inspecting tool-generated structures,
reusing computational feedback within a task, and revising guidance from prior execution and sci-
entific review.
D.1 CANDIDATE-LINKEDASSESSMENT FORBACE1 OPTIMIZATION
Generating plausible molecules does not guarantee selecting a jointly feasible design. In SMDD-
Bench, Han et al. (2026) report that retrospective evaluation of enumerated candidates recovers suc-
cesses beyond the agents’ original submissions.
Given a reference molecule and protein–ligand complex, the BACE1 task requires decreases of at
least 0.1 from the supplied baselines in four predictions: blood–brain barrier penetration (BBB),
cytochrome P450 3A4 (CYP3A4) inhibition, hERG potassium-channel blockade, and Ames muta-
genicity (AMES). Candidates must also meet four property-holding conditions and physicochemi-
cal, structural and binding constraints. The task specifies these optimization directions and requires
one candidate SMILES satisfying the joint requirements.
DrugHarness generated molecules with Python/RDKit, registered them as shared candidate objects,
and obtained ADMET-AI predictions. The first two batches contained 22 structures including the
reference. Figure 4 compares the reference with B2-09 and B3-02. Second-batch candidate B2-09
met three improvement targets but exceeded the CYP3A4 limit (Table 7).
Reference ligand
B1-01
Batch 2 candidate
B2-09
Submitted candidate
B3-02
Figure 4:Reference and generated BACE1 candidates.B2-09 and B3-02 were both generated from the
reference molecule. Structures are aligned by their shared core.
Table 7:ADMET-AI predictions for the BACE1 candidates.B2-09 meets three of the four improvement
targets but exceeds the CYP3A4 limit. B3-02 meets all four targets, and both candidates satisfy the four
holding conditions.
(a) Improvement targets
Endpoint Task limit B2-09 B3-02
BBB≤0.76800.6093 0.7303
CYP3A4≤0.83870.9311 0.8079
hERG≤0.74820.6720 0.7310
AMES≤0.36960.2871 0.3676
Met3/4 4/4
(b) Holding conditions
Endpoint Task limit B2-09 B3-02
Solubility≥ −4.8248−4.1327−4.5324
Clearance≤47.561839.0512 43.8456
Caco-2≥ −5.3597−5.1867−5.1951
PPB≤95.294789.5430 94.9833
Met4/4 4/4
22

Connecting assessment to the submitted object.After the second-batch predictions returned,
DrugHarness generated ten further structures from the same reference. B3-02, the submitted candi-
date, met all four improvement targets and all four holding conditions. Its CYP3A4 prediction was
0.8079, compared with B2-09’s 0.9311; its BBB, hERG and AMES predictions were higher but re-
mained within their limits (Figure 6). Molecules from the generated SDF were registered as shared
candidate records, allowing ADMET, structural comparison, and binding prediction to address the
same molecule. For B3-02, RDKit computed a reference similarity of 0.7692, above the required
0.70; Boltz-2 returned a binding-probability prediction of 0.9944, above 0.70. DrugHarness then
wrote and read backsolution.smi, submitting the same molecular state used in the prediction
(Figure 5).
Register
Following
assessment
B3-02Shared candidate record
ADMET-AI RDKit Boltz-2
4improvement targets met
4holding conditions met
Morgan
similarity
0.7692 ≥ 0.70
Predicted binding
probability
0.9944 > 0.70
Generate
Third batch:
10 structures
from the reference
Python / RDKit
Delivery
Write and read back
solution.smi
SubmitB3-02
Same molecular
state as assessed
Figure 5:Candidate-linked assessment and submission.The three assessments refer to the same registered
B3-02 molecule. Following assessment, the candidate was written tosolution.smi, read back and submit-
ted in the evaluated molecular state.
The shared candidate representation links each assessment to the delivered molecular structure, al-
lowing results from different scientific tools to be considered together under the task requirements.
Other candidates Reference B2-09 B3-02 Task limit
0.4 0.6 0.8
hERG prediction
0.2
0.4
0.6AMES prediction
(a) Two-target view of the evaluated pool
0.70 0.85 1.00 1.15
Prediction / task limit
BBB
CYP3A4
hERG
AMES
Task limit (b) Four-target trade-off for the highlighted pair
Figure 6:Predicted property trade-offs among BACE1 candidates.(a) All 32 evaluated structures, including
the reference; shading marks the region meeting the hERG and AMES limits. (b) Four predictions divided by
their task upper limits. Connected pairs compare B2-09 and B3-02 at each endpoint; ratios at or below one
meet that target.
23

D.2 STRUCTURALINSPECTION DURINGSCAFFOLDREPLACEMENT
Structural analysis can remain incomplete even when a predictor returns a complex. In the Mol-
Claw run described by Zhang et al. (2026a), ProLIF analysis failed during execution; the Met769
interaction was identified post hoc. In the 8OKQ task below, DrugHarness used the shared scientific
workspace to inspect a returned complex before submission.
The SMDD-Bench 8OKQ scaffold-replacement task (Type 3) provides a reference ligand and a
protein–ligand complex. It requires a new scaffold with Morgan similarity below 0.50, scaffold MCS
ratio below 0.65, preservation of the reference binding interactions, and Boltz-2 binding probability
above 0.70. The requested output is a candidate SMILES.
DrugHarness characterized ten candidate designs with local RDKit code. The selected cyclohexyl
candidate had a Morgan similarity of 0.348 and a scaffold MCS ratio of 0.471 relative to the refer-
ence. Boltz-2 returned a binding-probability prediction of 0.9907 together with a complex structure.
DrugHarness retrieved the predicted complex in CIF format and passed it to scientific code as the
sole structure input. Figure 7 traces this path from the candidate to the geometric analysis.
Reference ligand
 Submitted candidate
(a) Different scaffold, retained sulfonamide motif
Sole structure
input
Geometric report
21 residues
His94 3.27 Å
Thr198 2.73 Å
Geometric analysis
Scientific code
Schematic Minimum atom-pair distance
Residue r atoms Ligand L atoms
Record distance and atom pair
Repeat for 21 selected residues
Executor
Read the full report
Submit the same
candidate
Boltz-2
Predicted complex
Protein + ligand
complex.cif
(b) A returned structure becomes an explicit input to scientific code
Figure 7:Scaffold replacement and structural inspection.(a) The reference ligand and submitted candidate
have different ring scaffolds and share a sulfonamide group. (b) The predicted Boltz-2 complex was retrieved
and used as the code’s sole CIF input. For each selected residuer, the script computed the minimum distance to
an atom of the predicted ligandL. The full 21-residue report was read before the same candidate was submitted.
Arrows follow the recorded scientific handoffs.
24

Geometric evidence returned before submission.The script calculated nearest-ligand distances
for 21 selected protein residues and recorded the atom pair for each minimum. His94 NE2 and
Thr198 OG1 lay 3.27 and 2.73 ˚A from ligand atom N32, respectively. DrugHarness read the com-
plete report before writing and submitting the unchanged candidate. Figure 8 places the recorded
distances alongside the predicted pocket geometry.
Reference Predicted candidate
(a) Pocket overlay for spatial context
0 2 4 6 8
Nearest ligand distance (Å)
Asn67
Gln92
His94
His96
Glu106
His119
Val121
Phe130
Gly131
Val134
Leu140
Val142
Ser196
Leu197
Thr198
Thr199
Pro200
Pro201
Leu203
Val206
Trp208
3.27
2.73 (b) Distances for all 21 selected residues
Figure 8:Local static geometry of the predicted complex.Panel (b) shows the nearest-ligand distances
recorded during task execution. The pocket overlay in (a) uses structures aligned after execution for visualiza-
tion. Orange points identify His94 and Thr198; the remaining selected residues are blue.
DrugHarness carried the predicted complex from a specialized tool into scientific code and re-
turned the geometric report to the executor before submission. Links between the candidate record,
predicted complex, code input and derived report keep this sequence traceable to the submitted
molecule.
25

D.3 QED OPTIMIZATION THROUGHITERATIVEFEEDBACK
Given a source SMILES, this MolBench task asks for an increase in the quantitative estimate of
drug-likeness (QED) through intermediate optimization steps. QED improvement is the evaluation
criterion, with no target-activity preservation constraint; the final SMILES is submitted in JSON.
Starting from a molecule with recorded QED 0.4982, DrugHarness generated and evaluated three
candidate batches using Python/RDKit within the same task. The first batch yielded a leading candi-
date with QED 0.9285. The next script used that exact evaluated structure as its baseline to construct
further variants. The second batch yielded an N-methyl-amide candidate with QED 0.9375, which
the third script likewise used as its baseline before exploring additional substitutions.
DrugHarness selected a third-batch candidate with QED 0.9394, verified its molecular representa-
tion, and submitted the same structure in the requested JSON answer. The archived tables contain
83 records: 80 numerical QED entries and three invalid molecular strings, with repeated candidates
retained. Figure 9 shows the recorded scores and the evaluated structures reused as starting points
for subsequent optimization scripts.
Source
QED 0.4982
Batch 1 best
QED 0.9285
Batch 2 best
QED 0.9375
Submitted
QED 0.9394
Generate + assess Baseline for batch 2 Baseline for batch 3
(a) Evaluated molecules reused as design baselines
0.4
0.6
0.8
1.0Recorded QED
0.9285
 0.9375
 0.9394
Source 0.4982
Batch 1: 26 records Batch 2: 26 records Batch 3: 31 records
3 invalid; no QED
(b) Recorded candidate scores across three batches
Figure 9:QED feedback reused during molecular optimization.(a) The source, first- and second-batch
leaders, and submitted candidate, drawn from the recorded molecular structures. Arrows indicate reuse of
evaluated structures as baselines in subsequent scripts. (b) All 80 numerical entries from batches containing
26, 26, and 31 records, including repeated structures. Orange, light blue, and dark blue indicate batches 1–3.
Diamonds mark batch maxima, the star marks the submitted candidate, and the dashed line denotes the source
QED. Three invalid first-batch entries occupy a separate non-numerical strip. The submitted candidate shares
the highest third-batch QED.
26

D.4 SCIENTIFICREVIEW FORAFFINITYSKILLREFINEMENT
The MolBench affinity comparison labeled 012 here specifies CXCR2 as the target and provides two
candidate SMILES. It asks for the weaker binder (higherK i), with the selected molecule returned
as a SMILES; evaluation checks the candidate choice. Alongside this scientific task, we compare
how executors using the initial skill (S0) and its revised version (S1) gathered evidence and chose a
candidate.
S0 prioritized exact activity records. When candidate mappings were unavailable, it suggested trying
another query or source if budget permitted. During review of S0, an independent review agent
scanned complete BindingDB sources and matched both candidates in each of the source tasks
labeled 003 and 021, recovering the measurements in Table 8. Subsequent executions still showed
incomplete source recovery or candidate mapping. Researchers selected these execution records and
the review’s trial results for a focused learning round.
Table 8:Affinity records recovered by the first independent review.The reviewer matched both candidate
structures in each source task; A/B labels are task-specific.
Source task Records scannedK i(A), nMK i(B), nM
003 2,008 7.9 2,512
021 195 9.5 2,300
The learner explicitly cited the independent checks and automatically authored S1. When result
previews lack candidate mappings, S1 specifies full-source recovery, matching both query structures
and extracting their measured activities. A second independent review applied this procedure to 003
and 021 and recovered both candidates’ activity records in each task (Figure 10).
Automatic
revision
Independent review
Tasks 003 / 021
Full sources recovered;
both candidates matched
to measured activities.
Execution feedback
Researcher-selected
Incomplete source recovery
or candidate mapping;
reliance on heuristics.
Subsequent use
Task 012
Procedure adopted;
matched records used
to select molecule A.
Later use of S1
Second review
S1 on tasks 003 / 021
Full source recovery
and exact A/B matches
reproduced.
S0 Initial guidance
Prioritize exact
activity records
Missing mapping?
Try another
query/source
if budget permits.
S1 Revised guidance
When a result preview lacks
candidate mapping
1
2
3
Recover full source records
Exact matches for A and B
Extract measured activities
Figure 10:From scientific feedback to revised affinity guidance.Independent review results and researcher-
selected execution feedback informed the S0-to-S1 revision. The added recovery-and-matching procedure was
exercised in a second review on 003 and 021 before its use on task 012.
27

Revised guidance adopted in a subsequent task.Task 012 was outside this focused learning
input. The executions using S0 and S1 both received sources containing the relevant measurements.
In the S1 execution, the executor read the revised skill and its reference checklist, then followed the
source-recovery and structure-matching procedure to obtain candidate-linked activity records.
Using these records, the S1 executor selected molecule A, the weaker binder with the higherKi (Fig-
ure 11). The S0 executor selected B after partial source reads and reliance on property or conformer
heuristics. Table 9 summarizes the evidence use and resulting choices.
Task 012 / CXCR2 (P25025)
Molecule A Ki = 9,000 nM
BindingDB:50432424
Molecule B Ki = 64 nM
BindingDB:50432426
Figure 11:CXCR2 candidates and matched affinity records.Molecular structures are task inputs;K i values
were retrieved from BindingDB records associated with Karlstr¨om et al. (2013).
Table 9:Evidence use and candidate selection in task 012.The initial skill (S0) and revised skill (S1) were
each used in one execution of the CXCR2 affinity task, which asks for the weaker binder (higherK i).
Comparison Initial skill (S0) Revised skill (S1)
Source processing Partial source reads Full activity file recovered; 1,523 records
scanned
Decision evidence Property or conformer heuristics One matched record per molecule;
correspondingK i values
Selected molecule B (incorrect) A (correct)
28
