---
title: 'StartupBench: Benchmarking General-Purpose Agents on Market-Validated End-to-End Workflows'
url: https://arxiv.org/abs/2608.17800
category: ai-marketing
subcategory: empirical
date: 2026-08
venue: ''
authors:
- Liya Zhu
- Xin Ma
- Tao Liu
- Haodong Wang
- Ge Zhang
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.17800
pages: 24
chars: 77243
fetched_at: '2026-11-08T13:23:07+00:00'
kb_version: 1
---

# StartupBench: Benchmarking General-Purpose Agents on Market-Validated End-to-End Workflows

StartupBench: Benchmarking General-Purpose Agents
on Market-Validated End-to-End Workflows
1ByteDance Seed, 2Nanjing University, 3M-A-P, 4TokenWave.AI
Full author list in Contributions
Abstract
Recent advances in Large Language Models(LLMs) and agents have substantially improved the
ability of AI systems to execute complex tasks. Yet existing benchmarks largely rely on researcher-
selected tasks, leaving uncertain whether such progress extends to the work that real-world users
actually demand from AI systems. We introduceStartupBench, an E2E agent benchmark grounded
in market-validated AI startup products. Rather than defining tasks from pre-defined assumptions
about useful agent capabilities, we systematically study AI products with demonstrated adoption,
together with their product workflows and users, to identify real-world tasks for which AI has
established practical demand across diverse professional domains. We translate these workflows
into complete deliverable-oriented tasks and evaluate them with fine-grained rubrics capturing
their complex requirements. Across representative models evaluated under a unified agent harness,
even the strongest model successfully completes only approximately 30% of StartupBench, despite
making substantial partial progress on many tasks. Further analysis identifies aspects like complex
instruction following and domain-specific expertise as major sources of failure. Our results reveal
that many market-validated workflows remain beyond the reliable capabilities of current general-
purpose agents, establishing StartupBench as an empirical measure of progress toward E2E
completions of real-world user tasks.
Project Page:https://startupbench.github.io/
Date:August 19, 2026
1 Introduction
Large language models (LLMs) are increasingly evolving from systems that primarily retrieve information or
answer questions[5, 12, 26] into agents capable of completing complex real-world tasks. Current AI systems
are expected to execute end-to-end (E2E) workflows, coordinate multiple capabilities, and produce deliverables
that satisfy practical requirements under realistic constraints. As AI becomes increasingly integrated into
professional work, autonomously completing user-delegated tasks has become an important measure of model
capability. Evaluating whether AI systems can reliably translate their capabilities into professionally usable
deliverables is therefore a central challenge for the next generation of benchmarks.
Recent benchmarks have made important progress toward evaluating E2E task execution under realistic
settings. Nevertheless, several important limitations remain. First, many benchmark tasks are still largely
defined from researchers’ perspectives rather than grounded in workflows that have demonstrated practical
demand through real-world AI adoption [12, 18, 19], limiting their ability to reflect authentic user needs
and deliverable requirements. Second, although several benchmarks evaluate complete deliverables [23, 24],
their evaluation protocols are often substantially coarser than the deliverables themselves. Real-world work
1
arXiv:2608.17800v1  [cs.AI]  18 Aug 2026

A
Act as a biotech CMO and draft a confidential
board memo. Explain why China-only single-arm
Phase II data and organoid/MPS ethnic bridging
are insufficient for FDA approval, and propose a
regulatory-compliant MRCT strategy.
Interaction
Environment
Slides Preview
Long-horizon Task
Healthcare Finance LegalManagement STEM & CS Education & Social Science
Multi-format DeliverablesSix Domains
DOCX XLSX PPTX PDF Markdown
……
Understand &
Decompose
❏ Analyze task
❏ Identify key
issues
Search & Retrieve
* Scientific literature
* Guidelines
Generate & Refine
Analyze & Reason
1.Assess MPS limitations
2.Design MRCT strategy
3.Draft memo
Figure 1Overview of StartupBench: real AI-product workflows, long-horizon agent execution, six-domain coverage,
and multi-format deliverable generation.
products typically involve numerous functional, structural, formatting, and domain-specific requirements that
holistic evaluations cannot faithfully assess. Consequently, existing benchmarks still provide only limited
evidence ofhow well current models and agents can satisfy complex real-world user requirements and reliably
produce professionally usable deliverables.
To address these limitations, we observe that AI-native startups offer a natural source of real-world AI
workflows: their products have been validated through real-world adoption and commercial demand, providing
direct evidence that users value and seek to delegate these tasks to AI. We therefore introduceStartupBench,
a survey- and interview-driven benchmark that draws on these workflows to capture realistic E2E user
requirements across domains. StartupBench spans 97 tasks across 6 primary domains and is built around the
following design principles:
• Adoption-grounded task sourcing.We systematically survey AI-native startups and their products,
complemented by product demonstrations and user interviews, to identify workflows with demonstrated
real-world demand. We then construct these workflows into benchmark tasks that preserve their core
user objectives and practical requirements.
• E2E deliverables.Each task requires producing the complete deliverables that users ultimately expect in
realistic workflows, rather than intermediate outputs or simplified demonstrations.
• Fine-grained rubric-based evaluation.Each StartupBench task is evaluated using multiple independent
rubrics covering distinct dimensions of the expected deliverable, including functionality, structure,
formatting, and domain-specific quality, ensuring a comprehensive and faithful assessment of real-world
task completion.
We evaluate representative models on StartupBench under unified agentic harness. Results show that even
the strongest model successfully completes only about 30% of benchmark tasks, indicating that current
general-purpose systems remain far from reliably producing professionally usable deliverables. Performance
varies substantially across domains, with Finance, STEM & Computer Science and Education & Humanities
proving particularly challenging. Deeper analysis further attributes these failures primarily to limitations
in complex instruction following and domain-specific expertise, highlighting promising directions for future
foundation models and agent systems.
To summarize, our contributions are as follows:
2

• We propose a survey- and interview-driven methodology for constructing agent benchmarks from real
AI adoption scenarios.
• We construct StartupBench, a benchmark built through AI-native startup research, enterprise-user
interviews, user-oriented task abstraction, expert data construction, and multi-stage quality control.
• We present a comprehensive empirical study of current foundation models and general-purpose agents
on startup-derived workflows, providing a practical evaluation signal for assessing whether AI agents are
progressing from answering questions toward reliably completing real work.
2 Related Work
2.1 Commercial AI agents and Vertical Workflows
Recent advances in foundation models have enabled AI agents to gradually acquire planning, tool-use, file-
processing, and multi-step execution capabilities [21, 30], pushing AI systems from general conversational
assistants toward workflow-oriented products. In practice, commercial AI products increasingly package these
capabilities into vertical workflows such as document processing, data analysis, financial research, enterprise
operations, and knowledge work. This trend suggests that real-world AI value is not determined only by
isolated model capabilities, but also by whether these capabilities can be productized into useful work products.
However, existing academic benchmarks rarely use commercial adoption itself as a source of task discovery.
StartupBench addresses this gap by deriving tasks from market-validated AI-native startups and their deep
users, moving task construction from researcher-defined settings toward demand-driven workflow construction.
2.2 End-to-end evaluation of AI agents
Agent benchmarks have evolved from capability evaluation toward end-to-end task completion. Early
benchmarks mainly focus on tool use, multi-step reasoning, and general assistant abilities, as in AgentBench
and GAIA [10, 12]. Later work extends evaluation to more realistic interactive environments, including web
interaction and computer-use tasks [27, 34]. More recent benchmarks further move toward professional work
and economically meaningful tasks, covering enterprise software, simulated workplaces, occupational tasks,
and long-horizon workflows [4, 7, 11, 18, 28, 35]. These works reflect a clear transition from isolated capability
tests to realistic task-completion evaluation. StartupBench follows this direction, but differs in its task source:
rather than relying primarily on public environments, occupational taxonomies, or simulated workplaces, it
derives tasks from AI-native startup products, ToB user needs, and expected business deliverables.
2.3 Agent-as-a-Judge for complex deliverable evaluation
As agent tasks shift from short answers to heterogeneous deliverables such as reports, spreadsheets, slides,
code patches, and structured files, evaluation must move from capability-centric scoring to deliverable-centric
assessment[31]. LLM-as-a-Judge has been widely used for open-ended response evaluation, with MT-Bench and
Prometheus studying preference-based or rubric-conditioned judging [8, 33]. For agentic workflows, however,
judging often requires evidence retrieval, file inspection, state verification, and constraint checking over
final artifacts. Agent-as-a-Judge extends LLM judging by equipping evaluators with tools and environment
interaction, while AJ-Bench further studies judge agents on information acquisition, state verification, and
process verification [22, 36]. StartupBench adopts this deliverable-centric evaluation paradigm by combining
expert rubrics with automated judge agents that inspect original artifacts and evidence views, evaluating
whether agents can transform model capabilities into usable work products.
3 StartupBench
StartupBench is designed to evaluate whether models and agents can complete realistic workflows that
users already delegate to AI products. This objective requires data that reflects authentic user demand
while supporting controlled evaluation. We therefore require each task to be realistic, answerable, evaluable,
and discriminative: it should originate from actual AI product usage, provide sufficient information for a
3

Table 1Comparison of StartupBench with existing benchmarks. E2E denotes end-to-end workflow completion;
Item-wise Eval. denotes criterion-level judging.✓,✗, and△indicate full, no, and partial support.
Benchmark Task Source Final Output E2E Item-wise Eval. Process Logic Open- ended Evaluation Method
GAIA [12] Manual Text△✗ ✗ ✗Rule
OSWorld [27] Real+Manual Env State△✗ ✗ ✗Execution
DAComp [9] Real+Manual Workspace✓ ✗ ✗ ✓Hybrid
GDPval [18] Manual Work products✓ ✗ ✗△Manual
Workspace-Bench [24] Sim.+Manual Workspace✓ ✗ ✗ ✓Agent-as-Judge
OneMillionBench [29] Expert-authored Text△✗△✓LLM-judge
Agents’ Last Exam [23] Occupation-guided Workspace✓ ✗△ △Hybrid
OfficeQA Pro [17] Corpus-grounded Text✗ ✗ ✗ ✗Answer match
StartupBench (Ours) Market-vetted + Expert-built Workspace✓ ✓ ✓ ✓Agent-as-Judge
 Startup Agent Selection
Startup-agent Candidates
Funding > USD 1M
Active product or demo
Clear target users
Qualified Startup Agents
Validate Scenario Usability
Qualified startup-agent pool
Fix & retry or drop out
Append in raw data
Collect product documents
Study product demos
Identify target users
User Scenario Candidates
• Interview ToB users
• Collect example inputs
• Collect expected outputs
• Identify business constraints
 Interview & Task Scoping
• Real user need
• Clear input / output
• Suitable for agent evaluation
Collect Workflow Evidence
Scenario Validation
Task specifications
 Quality Control & Difficulty Calibration❶ ❷
• Realistic instructions
• Reference materials
• Expected deliverables
Produce Workflow Tasks
Construct Task Artifacts
Raw Benchmark Data
Domain Experts Real Users
Build Task Instances
Instruction
Scoring points
Context
Files
Prompt   Reference
Deliverable Format Rubric Draft
Ground Truth
❸  Data Production ❹
Task Admission Check
Manual Quality Review
Rubric  Verification
Scoring Calibration
Human scoring
model responses
Discriminability?
Save
• Clear user scenario
• Clear deliverable
• Reproducible workflow
• Complete task materials
scenario realism
instruction clarity
consistency
ambiguous
Map requirements
Check ground-truth
Check completeness
Evaluation Quality Criteria
User-Centricity
Reflect real-world needs
Validity
Ensure accuracy and construct validity
Reliability
Ensure consistency and reproducibility
Diversity
Cover varied scenarios and difficulty levels
Transparency
Document process and evaluation clearly
Error analysis &
keypoint revision
Refinable?
Discard or Revise Refine
No
No
Yes
Yes
Figure 2StartupBench data construction pipeline. We select market-validated startup agents, collect real user
workflows, construct task artifacts and instances, and calibrate quality and difficulty through multi-stage review.
valid solution, specify clear output requirements and assessment criteria, and remain challenging enough to
distinguish current models and agents.
Neither manual task design nor direct extraction from product demonstrations is sufficient to obtain such data.
The former is controllable but may be detached from real demand, while the latter is realistic but often lacks
context, success criteria, or reproducible specifications. We therefore adopt a survey- and interview-driven
multi-stage pipeline shown in Figure 2. We first survey market-validated AI-native startups, interview deep
users to identify usage contexts, task goals, and expected deliverables, recruit domain experts to convert
validated scenarios into benchmark instances, and finally apply quality control for realism, answerability,
evaluability, and discriminative difficulty.
3.1 Dataset Construction
3.1.1 Startup Survey for Market-Validated Agent Scenarios
We first survey AI-native startups that build agent products across diverse domains. To identify workflows
with market validation, we retain startups with more than USD 1M in funding and require evidence of real
adoption, either through paid usage or substantial user traction. Funding provides a coarse signal of market
expectation, while payment or user-scale evidence indicates that the product is used beyond exploratory
4

demonstrations. The output of this stage is a pool of candidate products and workflows for user interviews.
During this stage we collect 20+ start-up agents as the basis for subsequent stage.
3.1.2 User Interviews for Scenario and Requirement Discovery
For each candidate Startup-product, we interview deep users of the corresponding agent from different domains
to recover practical usage beyond public product descriptions. The interviews elicit the usage context, user
goal, input information, expected deliverable, success criteria, and common constraints. We summarize
these findings into scenario specifications and representative demo cases, which serve as anchors for later
annotation stage. During this stage we interview over 30 deep users and collected at least one demo case for
each candidate Agent.
3.1.3 Expert Construction of Domain Tasks
Given the interview-derived workflow specifications and representative user scenarios as a reference or seed task,
we recruit over 50 domain experts to reconstruct benchmark tasks that preserve the original workflow objectives,
practical constraints, and expected deliverables while adapting them into reproducible evaluation instances.
Rather than designing synthetic problems, experts standardize authentic user requests into benchmark tasks
that faithfully represent real professional workflows.
Every task is required to satisfy three principles: it must originate from a realistic work request that users
would naturally delegate to AI agents, involve an end-to-end workflow rather than an isolated subtask, and
produce concrete professional deliverables with clearly defined success criteria and fine-grained evaluation
rubrics for objective evaluation.
To standardize these tasks for evaluation, each task is represented as a triple
T= (q,E,R),
where q is a natural-language user request describing the task,E denotes the workspace containing all input
files and resources required to complete the task, andR = {(pi, wi)}n i=1 is a set of weighted evaluation
rubrics that assess complementary aspects of deliverable quality. Detailed task specifications and annotation
guidelines are provided in Appendix A.1. During this stage, we collect over 150 candidate tasks for further
quality control.
3.1.4 Quality Control
To ensure benchmark quality and consistency, every task undergoes the following multi-stage quality control
process:
Expert Cross Validation.Every task is independently reviewed by at least one additional domain expert.
Reviewers verify four aspects of task quality: (1) the authenticity and correctness of the task description and
workspace, (2) the fidelity of the reconstructed workflow, (3) the validity of the evaluation rubrics, and (4) the
consistency between the reference deliverable and the finalized evaluation protocol. Detailed review criteria
are provided in Appendix A.2.
Difficulty Control.We calibrate task difficulty through pilot executions using several frontier models under
the same evaluation harness adopted in the benchmark1. Tasks that are consistently completed with high
quality are excluded due to limited discriminative value. Pilot results also serve as an additional quality
assurance stage: when failures are attributed to ambiguous instructions, incomplete workspace information,
or inadequately specified evaluation criteria rather than intrinsic task difficulty, the corresponding task is
revised and re-validated before inclusion.
1We randomly select models from GPT-5.5, Seed-2.1-Pro and GLM-5.1 as the model for pilot executions, intending to construct
a challenging and discriminative benchmark rather than to estimate performance over the natural task distribution.
5

Table 2Statistics of StartupBench. The benchmark contains 97
real-world workflow tasks across six top-level domains and requires
diverse deliverable formats.
Category Count Percentage (%)
Overall statistics
Total tasks97 100.0
Top-level domains6–
Domain distribution
Medical & HealthCare21 21.6
Finance18 18.6
Legal16 16.5
Business & Management19 19.6
STEM & Computer Science16 16.5
Education & Humanities7 7.2
Output formats:DOCX, XLSX, PPTX, PDF, Markdown, images, and
text-based deliverables.
3.2 Statistics for StartupBench
StartupBenchcontains 97 real-world workflow tasks across 6 top-level domains: Medical & HealthCare,
Finance, Legal, Business & Management, STEM & Computer Science, and Education & Humanities. These
tasks are designed to reflect deliverable-oriented workflows in realistic office settings, requiring agents to
understand task contexts, follow complex constraints, process heterogeneous files, and produce usable work
products. For evaluation, each task is evaluated using an average of25.3fine-grained rubrics, spanning6
dimensions and 3 importance levels, enabling detailed assessment of complex, long-horizon workflows and
diverse work deliverables. The summary of the domain coverage and main output formats of StartupBench is
shown in Table 2.
3.3 Automatic Evaluation of StartupBench Tasks
As stated above, every task in StartupBench is defined as a tripleT= (q,E,R). Given(q,E), the evaluated
model produces a set of deliverablesD. Before evaluation, we construct a lightweight evidence viewV(D),
consisting of extracted textual content and rendered page images, to facilitate navigation over heterogeneous
artifacts while allowing the judge to access the original files whenever necessary.
Rather than relying on a single holistic judgment, StartupBench evaluates each rubric item independently
through a dedicated AgentJudge session. Most tasks contain 20+ fine-grained rubric items covering diverse
aspects of the expected deliverables, including functionality, completeness, formatting, and domain-specific
requirements. Evaluating these criteria separately allows each rubric to receive dedicated reasoning and
tool usage without interference from unrelated evaluation dimensions, while ensuring that every requirement
is assessed explicitly. The final task score is then obtained by aggregating the outcomes of all rubric-level
evaluations.
FollowingAgent-as-a-Judge, each rubric evaluation is carried out by a lightweight agent rather than a single
forward pass. LetJ denote the judging prompt and evaluation protocol used by the AgentJudge, given the
task specification, deliverables, evidence view, and the target rubric itempi, the judge produces both a binary
decisiony i ∈ {0,1}indicating whether the rubric is satisfied and a textual justificationei:
(yi, ei) = AgentJudge

J, q,D,V(D), pi

,(1)
The final task score is computed by aggregating the weighted decisions across all rubric items:
6

Kimi-K3 GPT-5.6-sol GPT-5.5 Seed-2.1-ProDeepseek-v4-Pro GLM-5.1 Kimi-2.6 Qwen-3.6-max Gemini-3.1-Pro
0
10
20
30
40
50
60
70
80Score
73.67 73.61 72.79
67.19
61.11 60.79 59.95 59.46
49.73
29.55 31.27
26.80
22.34
16.49 16.49
13.06
15.12
6.53
Average Score (0 100)
 Success Rate (scoring 90)
 Bootstrap 95% CI
Figure 3Leaderboard of StartupBench.
score(D,T) =
Pn
i=1 wiyiPn
i=1 wi
∈[0,1].(2)
4 Experiments
4.1 Experimental Setup
We evaluate 9 representative models on StartupBench, spanning both closed- and open-source families:
• Closed-source: GPT-5.6-sol [15], GPT-5.5 [16], Gemini-3.1-Pro [6], Seed-2.1-Pro [2],Qwen-3.6-Max [20]
•Open-source: DeepSeek-V4-Pro [3],Kimi-K3 [25], Kimi-K2.6 [13], GLM-5.1 [32].
To improve the reliability of our results, we conduct3independent runs for each model and report 95%
bootstrap confidence intervals for the task scores, computed using 10,000 resamples. All models are executed
under the same Nanobot harness with an identical tool configuration, and every task is capped at a maximum
of200interaction steps. For each task, the agent is initialized with the task-specific workspace and input
query, and its deliverables are collected from the designated output directory. Following the evaluation
protocol described in the previous section, the deliverables are evaluated by the judge agent against the task
specification, workspace context, and rubric set.
For automatic evaluation, the judge agent also runs under the same Nanobot harness to ensure a consistent
execution environment, while using GPT-5.5 as the underlying judge model. Apart from the continuous task
score, we also reportsuccess rate, the fraction of runs that are successfully completed, pooled over the three
runs. A task is considered successful if its final score is at least90; otherwise, it is counted as a failure.
4.2 Main Results
Startup tasks remain far from saturated under a general-purpose agent harness.Although the strongest
models, Kimi-K3 and GPT-5.6-sol, achieve average scores of 73.67% and 73.61%, respectively, no model
successfully completes even one third of the benchmark under the strict acceptance criterion (score≥ 90).
More broadly, the average scores of most models lie between roughly 55 and 75, indicating that current
agents are generally capable of making substantial progress toward solving realistic professional workflows.
However, high average scores do not necessarily translate into high task completion rates. This is particularly
7

Table 3Model performance of StartupBench, averaged over three independent runs.Top block:importance-weighted
mean per-task score (0–100);bottom block:success rate, the fraction of samples scoring≥ 90(%), pooled over the
three runs. Per-columnbest in bold, second-best underlined.
Model Overall Med Finance Legal Business STEM Education
Average score
Kimi-K373.67 80.03 62.3869.4583.9068.3477.71
GPT-5.6-sol 73.61 79.32 61.6673.5377.6174.7773.94
GPT-5.5 72.79 78.59 62.09 71.75 79.59 72.14 68.32
Seed-2.1-Pro 67.19 73.15 57.26 61.35 77.83 65.61 62.91
Kimi-K2.6 59.95 67.70 51.17 54.62 71.91 51.38 58.60
GLM-5.1 60.79 65.66 51.22 50.20 78.53 52.18 66.50
Qwen-3.6-Max 59.46 66.51 52.45 50.33 75.03 48.83 59.26
DeepSeek-V4-Pro 61.11 69.42 51.11 54.53 73.69 54.89 57.03
Gemini-3.1-Pro 49.73 54.05 41.00 43.49 61.18 45.88 51.23
Success rate(≥90)
Kimi-K3 29.55 34.9220.37 20.8352.6316.67 23.81
GPT-5.6-sol31.2733.33 27.7822.92 38.6033.33 28.57
GPT-5.5 26.80 30.16 22.22 25.0038.60 22.92 9.52
Seed-2.1-Pro 22.34 19.05 16.67 14.58 45.61 20.83 4.76
Kimi-K2.6 13.06 15.87 14.81 6.25 24.56 4.17 4.76
GLM-5.1 16.49 12.70 16.67 8.33 36.84 8.33 9.52
Qwen-3.6-Max 15.12 11.11 16.67 10.42 33.33 6.25 4.76
DeepSeek-V4-Pro 16.49 20.63 16.67 8.33 29.82 10.42 0.00
Gemini-3.1-Pro 6.53 6.35 11.11 6.25 8.77 0.00 4.76
evident for the Kimi series: Kimi-K3 achieves the highest average score overall but a lower success rate than
GPT-5.6-sol, while Kimi-K2.6 similarly attains a higher average score than Qwen-3.6-Max but a lower success
rate. These discrepancies suggest that some models can satisfy a substantial fraction of task requirements
while still falling short of complete delivery. More generally, all models exhibit substantially lower success rate
than average score, suggesting that the primary bottleneck is no longer executing large portions of a workflow,
but consistently producing artifacts that satisfy the standards required for direct professional use.
This gap has two important implications. First, it helps explain why specialized vertical agents continue to
provide practical value in many market-validated workflows, where consistently meeting professional standards
remains essential. Second, it suggests that the next frontier for foundation models is not merely performing
professional tasks, but reliably producing work products that users can adopt without further verification or
revision. We further investigate the underlying causes of this gap in Section 4.4.2.
Performance varies substantially across professional domains.Table 3 reveals that current general-purpose
agents do not exhibit uniform competence across real-world workflows. Among the six domains, Business is
consistently the easiest: every model achieves an average score above 60, and the average success rate across
models is also substantially higher than in any other domain. In contrast, Finance is the most challenging,
with the lowest average score of 54.48%. The large gap between Business and Finance suggests that current
models handle structured, relatively standardized tasks more reliably than workflows requiring sustained
quantitative reasoning, cross-document consistency, and multi-step verification.
The results also reveal pronounced domain specialization. While Kimi-K3 and GPT-5.6-sol achieve nearly
identical average scores overall (73.67 vs. 73.61), their strengths differ substantially across domains. Under
success rate, Kimi-K3 performs best in Medical and Business, whereas GPT-5.6-sol leads in Finance, STEM,
and Education; GPT-5.5 remains strongest in Legal. A similar pattern emerges in average score, where
8

Kimi-K3 leads in Medical, Business, Finance and Education, GPT-5.6-sol in Legal and STEM. Thus, even
among the strongest models, no single agent consistently dominates across professional domains. These
results suggest that current general-purpose agents still exhibit substantial domain-dependent variation,
leaving considerable room for improving the robustness and transferability of end-to-end task execution across
heterogeneous professional workflows.
4.3 Effectiveness of Proposed Evaluation Framework
To validate the reliability of our evaluation framework, we compare its judgments against expert annotations.
We sample outputs from two representative models for all tasks and ask domain experts to independently
evaluate each submission using the predefined rubrics. At the rubric level, the automatic evaluator achieves
an overall agreement of92.78%with expert judgments. We further examine whether these local agreements
translate into consistent task-level decisions by comparing the resulting success labels, where a submission
is considered successful if its aggregated score reaches 90. The automatic and expert evaluations agree on
92.84%of these success decisions. Notably, the similarly high agreement at both rubric and success levels,
despite their substantially different label distributions, suggests that the observed consistency is not merely
an artifact of label imbalance.
We further investigate the necessity of evaluating each rubric independently. As an ablation, instead of
assigning one rubric to one judge agent, we directly provide the complete model output together with the
full rubric list to a single judge agent, requiring it to score all rubrics in one end-to-end inference. This
alternative reduces the agreement with human experts to83%. More importantly, the holistic setting proves
considerably less stable in practice. Since the judge agent must simultaneously perform long-context reasoning,
maintain consistency across numerous evaluation criteria, and finally generate a structured output covering all
rubric scores, failures such as malformed outputs or incomplete formatting frequently occur, forcing repeated
executions. On average, each evaluation requires more than two runs before a valid result is obtained. In
contrast, our rubric-wise evaluation decomposes the assessment into a collection of independent, lightweight
judging tasks, yielding both substantially higher agreement with human experts and significantly better
execution robustness.
4.4 Failure-Mode Analysis
4.4.1 Outcome-level Failure Analysis
Capability differences across rubric dimensions.Figure 4 further breaks down model performance by
rubric dimension. Overall, current models achieve consistently higher scores on Structure & Completeness,
Information Integration, and especially Output & Presentation, indicating that they are generally capable
of organizing heterogeneous information into well-structured and visually polished deliverables. In contrast,
Domain-Specific Compliance emerges as the most challenging dimension across all evaluated models, while
Calculation Precision also remains substantially weaker than the other dimensions. This suggests that although
modern foundation models can produce artifacts that appear complete and professional, reliably satisfying
domain-specific regulations, business conventions, and numerical correctness continues to be a major obstacle
for real-world deployment.
The two strongest models, GPT-5.6-sol and Kimi-K3, outperform the remaining systems across nearly all
rubric dimensions rather than relying on a single specialized capability. Their largest advantages are observed
in Structure & Completeness, Calculation Precision, Information Integration, and Output & Presentation,
demonstrating stronger end-to-end workflow execution and artifact construction capabilities. Nevertheless,
even these leading models obtain their lowest scores on Domain-Specific Compliance, indicating that adherence
to professional standards and domain-specific requirements remains the primary bottleneck even for state-of-
the-art systems.
Models often satisfy peripheral requirements while missing what matters most.Table4reportstask-normalized
rubric satisfaction rates across the three importance levels. Averaged across models, satisfaction decreases
from68.67%for Auxiliary rubrics to65.89%for Important rubrics and63.45%for Core rubrics, with 8 of the 9
models exhibiting the same overall trend. Importantly, these levels reflect each requirement’s contribution to
9

Structure & Completeness
Calculation PrecisionInformation Integration
Domain-Specific Compliance
Engineering & FormatOutput & Presentation
Kimi-K3
Gemini-3.1-Pro
GPT-5.6-sol
Qwen-3.6-Max
GPT-5.5
Kimi-K2.6
Seed-2.1-Pro
GLM-5.1
DeepSeek-v4-Pro
80.7 75.0 79.5 70.7 80.0 82.0
56.9 48.0 63.2 44.2 56.9 60.4
80.0 74.0 82.2 70.5 81.1 82.8
68.9 62.0 66.5 52.5 63.8 71.5
79.3 74.5 79.8 69.8 76.3 84.4
66.9 60.8 70.8 52.6 60.7 73.7
76.0 69.0 76.6 61.8 66.1 81.0
71.9 62.6 69.9 49.5 63.4 74.7
70.6 64.2 68.6 53.1 62.4 72.5
 40
45
50
55
60
65
70
75
80
85
Weighted pass rate (%)
Figure 4Performance across rubric dimensions. Importance-weighted pass rates (%) of different models on the six
rubric dimensions in StartupBench. Higher values indicate better performance under the corresponding evaluation
dimension.
successful task completion rather than its expected difficulty. This pattern reveals a characteristic failure
mode of current agents: they can often fulfill auxiliary or surface-level requirements while failing on the core
requirements that determine whether the task is actually completed successfully. In other words, substantial
apparent progress can be driven by satisfying less consequential parts of the task, while critical omissions still
prevent the final deliverable from being practically usable.
A typical case of models struggling with requirements central to task completion is shown in Figure 5. In
this mechanical process task, models often complete peripheral workbook requirements but fail on the core
technical operations: extracting dimensions accurately from engineering drawings, validating specifications
against the provided documents, and linking identified discrepancies to the corresponding rectification actions.
These failures prevent the resulting workbook from fulfilling its primary purpose even when many auxiliary
requirements are successfully completed.
Output format non-compliance.Some failures arise from models not producing deliverables in the file
type explicitly required by the task. Unlike most failure modes discussed above, this requirement involves
neither complex reasoning nor domain knowledge and can be verified deterministically from file extensions.
Nevertheless, no model achieves perfect compliance on the 56 tasks with explicit output-format requirements
(Table 5), with success rates ranging from97.6%to86 .3%. Most violations fall into two recurring patterns:
generating an incorrect file type (e.g., returning.md/.txt instead of the required.pdf) and omitting part
of the requested deliverables (e.g., producing only one of the required.xlsx and .docx files). These errors
suggest that even elementary deliverable-level constraints remain a non-negligible source of failures for current
foundation models.
10

Table 4Task-normalized rubric satisfaction rates (%) across different importance levels. For each model–task–trial,
we first compute the satisfaction rate within each importance level and then average across tasks and trials.
Model Auxiliary Important Core
Kimi-K3 77.89 75.12 73.40
GPT-5.6-sol 77.59 74.47 73.07
GPT-5.5 75.12 75.09 72.07
Seed-2.1-Pro 70.83 69.85 65.77
Kimi-K2.6 66.64 63.56 57.82
GLM-5.1 64.58 61.40 60.68
Qwen-3.6-Max 65.39 62.17 58.08
DeepSeek-V4-Pro 66.50 62.97 60.05
Gemini-3.1-Pro 53.48 48.41 50.13
Average 68.67 65.89 63.45
Table 5Output-format compliance on the 56 StartupBench tasks with explicit output-file requirement rubrics. Models
are ranked by compliance rate.
Model Compliance (%)
Kimi-K3 97.6
Seed-2.1-Pro 95.2
GPT-5.6-sol 94.6
Qwen-3.6-Max 94.6
DeepSeek-V4-Pro 94.0
GPT-5.5 93.5
Kimi-K2.6 92.9
Gemini-3.1-Pro 86.9
GLM-5.1 86.3
4.4.2 Behavior-level Failure Analysis
Complex Instruction Following.Complex real-world workflows typically impose numerous constraints on the
final deliverable, including structural organization, computation logic, formatting, and executable correctness.
Although these requirements are explicitly specified in the task description, current models frequently
exhibit partial compliance: they satisfy the most visible requirements while overlooking other equally critical
constraints. As a result, the generated artifact appears largely complete from a superficial inspection, yet fails
to satisfy the complete acceptance criteria required for direct use. This behavior indicates that models often
optimize for producing outputs that look correct, rather than ensuring that every instruction governing the
final deliverable has been faithfully executed.
A representative example is shown in Figure 6. The task requires generating a complete HR payroll workbook
from multiple source sheets under a diverse set of structural, computational, and formatting constraints.
Although the model produces an artifact that appears largely complete—including all required worksheets,
formulas, charts, and dashboard layouts—the artifact-level evaluation reveals that several critical acceptance
conditions remain unsatisfied. Specifically, key cached values required for downstream verification are missing,
rendering the workbook unverifiable despite its polished appearance. This case illustrates a common pattern
of partial compliance, where the model satisfies the most visible requirements while overlooking less obvious
but equally essential deliverable constraints.
Self-Verification Hallucination.We also observe that many models fail not because they cannot complete
the required workflow, but because they incorrectly assume that successful execution implies successful
delivery. After producing a plausible artifact, the model often summarizes the intended reasoning process
or completed steps as evidence that the task has been verified, without independently inspecting the final
deliverable against the original user requirements. Consequently, subtle yet critical errors—such as incorrect
cell values, unmatched identifiers, missing constraints, or formatting inconsistencies—remain undetected
despite an otherwise convincing output. This behavior reflects a form of self-verification hallucination, where
11

Figure 5A representative case of models failing on core rubrics though passing auxiliary rubrics on StartupBench.
the model mistakes confidence in its own reasoning process for evidence that the generated artifact satisfies
the acceptance criteria. In real-world office workflows, however, successful completion requires validating the
final deliverable itself rather than merely confirming the execution process, making this a common source of
deployment-critical failures. A typical case is shown at Appendix D.1.
Domain-Specific Expertise.Another major source of failure arises from insufficient domain-specific expertise,
consistent with the relatively poor performance on the Domain-Specific Compliance dimension. Unlike general
instruction-following errors, these failures are driven by the unique operational requirements of different
professional domains. Although models often generate outputs that appear fluent and professionally formatted,
they frequently fail to satisfy the domain-specific constraints that determine whether a deliverable is actually
usable. As a result, the dominant failure patterns vary substantially across domains, reflecting different
notions of correctness, evidence, precision, and actionability required by real-world workflows.
From a domain perspective, different professional areas expose distinct failure characteristics. Business and
management tasks primarily stress artifact correctness, particularly for spreadsheets, dashboards, formulas, and
structured reports. Finance tasks emphasize source attribution, numerical precision, valuation assumptions,
and temporal consistency, where errors commonly arise from insufficient reconciliation, inadequate numerical
self-verification, or inconsistent accounting conventions. Legal tasks are less constrained by legal writing style
than by the completeness and correctness of legal reasoning, including missing citations, incomplete factual
coverage, insufficient statutory support, or incorrect mapping between facts and applicable rules. Medical
tasks achieve relatively higher average scores but pose substantially greater safety risks, since mistakes in
medication timing, continuation criteria, or discharge planning directly undermine clinical usability. STEM
and Computer Science tasks instead require precise object-level grounding, demanding accurate relationships
among code, engineering drawings, images, bills of materials, and system components. Finally, education and
humanities tasks place greater emphasis on fine-grained rule following, such as curriculum requirements, credit
allocation, document organization, and textual coherence. A typical example of failure caused by insufficient
domain-specific expertise is shown at Appendix D.2.
4.5 Impact of Harness on Startup Tasks
12

WORKFLOW CASE STUDY | HR PAYROLL
Complex Instruction Following
A multi-sheet HR workﬂow is largely constructed, but key computed results remain unreadable in the ﬁnal ﬁle.
WORKBOOK FLOW
7 source sheets > 6 analysis sheets > 4 native charts
1 Task description
2024 HR payroll and talent-review workbook
Convert seven source sheets into one auditable workbook covering
payroll, performance, talent, labor cost, and management reporting.
7
source sheets
696
populated rows
6,189
source cells
INPUT HETEROGENEITY
Roster (41 rows), attendance (466), performance (158), plus salary
adjustments, contribution rates, tax brackets, and department budgets.
OUTPUT EXPANSION
Preserve 7 raw sheets and build 6 analysis sheets: 1,747 populated
rows and 26,425 populated cells in the submitted XLSX.
CALCULATION DEPENDENCIES
Handle ﬁve month formats, salary changes, leavers, department
transfers, beneﬁt caps/ﬂoors, cumulative tax, forced ranking, and
nine-box logic.
VISUAL AND FILE CONSTRAINTS
Produce 4 KPI cards, 4 native Excel charts, ﬁlters, frozen headers,
conditional formats, number formats, and 3 named ranges.
Cleaning + business rules + formulas + charts + ﬁle validation
2 Required execution path
1
Inspect seven source sheets
Connect roster, attendance, performance, adjustments, rates, tax brackets, and
budgets.
2
Clean attendance
Normalize employee IDs and ﬁve month formats; compute deductions, overtime, and
net adjustment.
3
Calculate monthly payroll
Build 465 employee-month rows; apply raises, exits, transfers, beneﬁt caps/ﬂoors,
and cumulative tax.
4
Calibrate annual performance
Combine quarterly weights, rank within departments, and apply ROUNDUP-based
forced distribution.
5
Build the talent nine-box
Join annual performance with potential scores; assign nine categories and
development actions.
6
Reconcile department cost
Aggregate six departments; compare wages and employer contributions with annual
budgets.
7
Build dashboard and verify
Create 4 KPIs and 4 native charts; reopen the ﬁnal XLSX and inspect computed result
cells.
OBSERVED FAILURE POINTS
Monthly payroll: I2 and S13 | Management dashboard: B3
Formula text exists, but reopening the workbook returns no readable cached result.
3 Artifact outcome and judge evidence
What looked complete
13 sheets; 465 payroll rows; 4 native
charts.
What failed
Three computed results are
unreadable after reopening.
Submitted workbook excerpt (translated) formula view + cached state
Monthly Payroll Dashboard Performance Attendance Cleaning
Employee ID Month Attendance deduction Overtime subsidy Gross pay Monthly tax
EMP001 2024-01 =IFERROR(SUMIFS(...),0) =IFERROR(SUMIFS(...),0) =E2+F2-G2+H2
Cached: None
=MAX(0,T2)
Cached: None
EMP001 2024-02 =IFERROR(SUMIFS(...),0) =IFERROR(SUMIFS(...),0) =E3+F3-G3+H3
Cached: None
=MAX(0,T3-T2)
Cached: None
EMP001 2024-12 =IFERROR(SUMIFS(...),0) =IFERROR(SUMIFS(...),0) =E13+F13-G13+H13
Cached: None
=MAX(0,T13-T12)
Cached: None
English rendering; formulas are shortened for legibility.
Artifact-level judge evidence
I2
Expected: gross pay 26000-27500
Judge: formula exists; data_only None
S13
Expected: taxable income 170k-182k
Judge: formula exists; cached None
B3
Expected: total payroll 8.4M-8.6M
Judge: dashboard KPI cached None
Formula presence does not conﬁrm readable computed outputs.
Pattern: partial compliance The agent completes the visible construction steps, but its ﬁnal validation checks formula text rather than the computed-result state needed for a usable workbook.
Figure 6A representative case of complex instruction following failure. Although the generated workbook appears
complete, artifact-level evaluation reveals that several critical acceptance conditions remain unsatisfied, illustrating a
common pattern of partial compliance.
Table 6Performance under different general-purpose agent frameworks. For each model, we report the average score
under three general-purpose frameworks and the performance range (max–min) across frameworks.
Model Hermes Claude Code Nanobot Max--Min
GPT-5.5 71.00 70.11 72.79 2.68
GLM-5.1 60.20 60.18 60.79 0.61
Qwen-3.6-Max 59.10 57.38 59.46 2.08
Average 63.43 62.56 64.35 1.79
4.5.1 Effect of General-Purpose Harness
In the main experiment, all models are evaluated under nanobot Agent framework. To examine whether the
observed performance is primarily determined by the choice of agent framework rather than the underlying
model, we re-evaluate the benchmark using two more representative general-purpose agent frameworks:
Hermes [14] and Claude Code [1]. All frameworks are evaluated under the same task set and identical
evaluation protocol, with only the execution framework replaced.
As shown in Table 6, replacing the general-purpose framework leads to only minor performance differences.
Across all evaluated models, the average variation between the best and worst framework is only 1.79 points.
GLM-5.1 is almost completely unaffected (0.61 points), while even the largest difference observed on GPT-5.5
is only 2.68 points. More importantly, the relative ordering of models remains unchanged across all three
frameworks. These results suggest that StartupBench is largely robust to the choice of general-purpose
agent framework. Although different frameworks adopt different prompting strategies, tool interfaces, and
interaction mechanisms, simply replacing one general-purpose framework does not substantially alter end-
to-end task performance. Consequently, the performance gap observed on StartupBench primarily reflects
the capability of the underlying foundation models rather than implementation-specific characteristics of a
particular framework.
13

Table 7General-purpose versus specialized agent systems. Oracle General denotes the averages of the highest score
achieved in all trials for every model.
Agent System Avg Score Success Rate
General (All Runs avg) 64.26 19.74
General (Oracle) 71.75 28.06
Specialized Agent83.50 39.18
4.5.2 General-Purpose Agents versus Specialized Agents
To further understand the role of agent frameworks, we compare general-purpose agent frameworks with
the specialized startup agents from which StartupBench tasks are derived. Unlike the previous experiment,
this comparison evaluates each task using its corresponding production startup agent, which has been
specifically optimized for its target workflow through domain-specific model selection, prompting strategies,
tool orchestration, and workflow design.
Table 7 summarizes the comparison between general-purpose and specialized agent systems. Across all
executions, general-purpose agents achieve an average score of 64.26 and a success rate of 19.74%, substantially
below the specialized agents at 83.50 and 39.18%, respectively. Since specialized agents are explicitly designed
and optimized for their target domains, we further consider a stronger oracle setting for the general-purpose
agents: for each model–task pair, we retain the best result among three independent trials. This oracle
selection raises the average score to 71.75 and success rate to 28.06%, but still falls well short of the specialized
agents, with gaps of 11.75 points in average score and 11.12 percentage points in success rate. Thus, the
performance gap cannot be explained simply by stochastic variation or occasional execution failures: even when
general-purpose agents are allowed multiple attempts and evaluated by their best observed outcome, specialized
agent systems remain substantially more effective on these tasks. Combined with the failure-mode analysis
presented earlier, these findings provide a more complete picture of the remaining gap between general-purpose
foundation models and specialized startup agents. While today’s foundation models still cannot fully replace
domain-specialized agents under a unified general-purpose framework, their shortcomings are concentrated
in a relatively clear set of capabilities, including complex instruction following, domain-specific knowledge,
professional operational conventions, and long-horizon workflow execution. This suggests that the observed
advantage of specialized systems does not necessarily require fundamentally different agent architectures, but
may instead reflect capabilities that current general-purpose models have yet to acquire reliably. As these
underlying capabilities continue to improve, general-purpose agents may increasingly accomplish valuable
professional end-to-end tasks without relying on domain-specific agent harness designs.
5 Conclusion
We introduceStartupBench, a benchmark for evaluating models on end-to-end professional workflows derived
from market-validated AI-native products and real-world user demands. Across multiple tasks spanning
diverse domains, our evaluation reveals a substantial gap between making meaningful progress on professional
work and producing deliverables that fully satisfy practical acceptance criteria. This gap is primarily driven
by limitations in complex instruction following, domain-specific expertise, professional conventions, and
long-horizon workflow execution. By grounding evaluation in workflows that users already seek to delegate to
AI, StartupBench provides a realistic measure of practical agent capabilities and highlights concrete directions
for future improvement. We hope StartupBench supports the development of models and agents that can not
only perform valuable professional work, but reliably deliver results ready for direct use.
14

6 Contributions
Project Leads
Liya Zhu, Xin Ma, Tao Liu, Haodong Wang, Ge Zhang
Core Contributors
Jingzhe Ding, Qingshui Gu, Yongjie Zhong, Jinxiang Meng, Yuan Gao, Yunqiu Zhou, Hao Zhu, Jifeng He,
Yongzhi Liao, Xinyi Zhang, Chaoxin Li, Yi Zhu, Xi Lin, Duju Zeng, Xiang Gao, Wen Zhang, Yunyang Wang,
Duo Wang
Contributors
Huan Zhou, Zuo Wang, Jin Chen, Kaiyuan Zhang, Chuqian Yu, Tianhao Yu, Longxiang Liu, Jianbo Xue,
Huimin Che, Jiahao Wang
Sponsor Committee
Yujia Qin, Jiaheng Liu
Corresponding Authors
Ge Zhang (gezhang@umich.edu)
Shen Yan (sheny@bytedance.com)
Xiaolong Chang (changxiaolong@bytedance.com)
Wenhao Huang (huang.wenhao@bytedance.com)
15

References
[1] Anthropic. Claude code.https://github.com/anthropics/claude-code. GitHub repository.
[2] ByteDance Seed. Seed2.1 model card: Agentic intelligence for productivity. Technical report, ByteDance,
2026. URL https://lf3-static.bytednsdoc.com/obj/eden-cn/lapzild-tss/ljhwZthlaukjlkulzlp/seed2.1/
Seed2_1_Model_Card.pdf.
[3] DeepSeek-AI. Deepseek-v4: Towards highly efficient million-token context intelligence, 2026. URL https:
//huggingface.co/collections/deepseek-ai/deepseek-v4. Technical Report.
[4] Alexandre Drouin, Maxime Gasse, Massimo Caccia, Issam H Laradji, Manuel Del Verme, Tom Marty, Léo Boisvert,
Megh Thakkar, Quentin Cappart, David Vazquez, et al. Workarena: How capable are web agents at solving
common knowledge work tasks?, 2024.URL https://arxiv. org/abs/2403.07718.
[5] Xeron Du, Yifan Yao, Kaijing Ma, Bingli Wang, Tianyu Zheng, Minghao Liu, Yiming Liang, Xiaolong Jin, Zhenlin
Wei, Chujie Zheng, et al. Supergpqa: Scaling llm evaluation across 285 graduate disciplines.Advances in Neural
Information Processing Systems, 38, 2026.
[6] Google Cloud. Gemini 3.1 Pro Model Card, 4 2026. URL https://docs.cloud.google.com/vertex-ai/
generative-ai/docs/models/gemini/3-1-pro?hl=zh-cn.
[7] Xiaomeng Hu, Yinger Zhang, Fei Huang, Jianhong Tu, Yang Su, Lianghao Deng, Yuxuan Liu, Yantao Liu,
Dayiheng Liu, and Tsung-Yi Ho. Occubench: Evaluating ai agents on real-world professional tasks via language
environment simulation, 2026. URLhttps://arxiv.org/abs/2604.10866.
[8] Seungone Kim, Jay Shin, Joel Jang, Shayne Longpre, Hwaran Lee, Sangdoo Yun, Ryan Shin, Sungdong Kim,
James Thorne, Minjoon Seo, et al. Prometheus: Inducing fine-grained evaluation capability in language models.
In International Conference on Learning Representations, 2024.
[9] Fangyu Lei, Jinxiang Meng, Yiming Huang, Junjie Zhao, Yitong Zhang, Jianwen Luo, Xin Zou, Ruiyi Yang,
Wenbo Shi, Yan Gao, et al. Dacomp: Benchmarking data agents across the full data intelligence lifecycle.arXiv
preprint arXiv:2512.04324, 2025.
[10] Xiao Liu, Hao Yu, Hanchen Zhang, Yifan Xu, Xuanyu Lei, Hanyu Lai, Yu Gu, Hangliang Ding, Kaiwen
Men, Kejuan Yang, et al. Agentbench: Evaluating llms as agents. InInternational Conference on Learning
Representations, 2024.
[11] Jinxiang Meng, Shaoping Huang, Fangyu Lei, Jingyu Guo, Haoxiang Liu, Jiahao Su, Sihan Wang, Yao Wang,
Enrui Wang, Ye Yang, et al. Dv-world: Benchmarking data visualization agents in real-world scenarios.arXiv
preprint arXiv:2604.25914, 2026.
[12] Grégoire Mialon, Clémentine Fourrier, Thomas Wolf, Yann LeCun, and Thomas Scialom. Gaia: a benchmark for
general ai assistants. InInternational Conference on Learning Representations, 2024.
[13] Moonshot AI. Kimi K2.6: Advancing open-source coding. https://www.kimi.com/blog/kimi-k2-6, 2026.
Accessed: 2026-06-02.
[14] Nous Research. Hermes agent: The ai agent that learns from you.https://github.com/hermes-agent-org/
hermes, 2026. GitHub repository.
[15] OpenAI. Gpt-5.6 system card. Technical report, OpenAI, 7 2026. URLhttps://deploymentsafety.openai.
com/gpt-5-6/gpt-5-6.pdf.
[16] OpenAI. Introducing gpt-5.5, 4 2026. URLhttps://openai.com/index/introducing-gpt-5-5/. System Card:
https://deploymentsafety.openai.com/gpt-5-5/gpt-5-5.pdf.
[17] Krista Opsahl-Ong, Arnav Singhvi, Jasmine Collins, Ivan Zhou, Cindy Wang, Ashutosh Baheti, Owen Oertell,
Jacob Portes, Sam Havens, Erich Elsen, et al. Officeqa pro: An enterprise benchmark for end-to-end grounded
reasoning. arXiv preprint arXiv:2603.08655, 2026.
[18] Tejal Patwardhan, Rachel Dias, Elizabeth Proehl, Grace Kim, Michele Wang, Olivia Watkins, Simón Posada
Fishman, Marwan Aljubeh, Phoebe Thacker, Laurance Fauconnet, et al. Gdpval: Evaluating ai model performance
on real-world economically valuable tasks.arXiv preprint arXiv:2510.04374, 2025.
[19] Long Phan, Alice Gatti, Ziwen Han, Nathaniel Li, Josephina Hu, Hugh Zhang, Chen Bo Calvin Zhang, Mohamed
Shaaban, John Ling, Sean Shi, et al. Humanity’s last exam.arXiv preprint arXiv:2501.14249, 2025.
16

[20] Qwen Team. Qwen3.6-Max-Preview: Smarter, sharper, still evolving, April 2026. URLhttps://qwen.ai/blog?
id=qwen3.6-max-preview.
[21] Timo Schick, Jane Dwivedi-Yu, Roberto Dessì, Roberta Raileanu, Maria Lomeli, Eric Hambro, Luke Zettlemoyer,
Nicola Cancedda, and Thomas Scialom. Toolformer: Language models can teach themselves to use tools.Advances
in neural information processing systems, 36:68539–68551, 2023.
[22] Wentao Shi, Yu Wang, Yuyang Zhao, Yuxin Chen, Fuli Feng, Xueyuan Hao, Xi Su, Qi Gu, Hui Su, Xun-
liang Cai, et al. Aj-bench: Benchmarking agent-as-a-judge for environment-aware evaluation.arXiv preprint
arXiv:2604.18240, 2026.
[23] Yiyou Sun, Xinyang Han, Weichen Zhang, Yuanbo Pang, Tianyu Wang, Yuhan Cao, Yixiao Huang, Chris Duroiu,
Haoyun Zhang, Jeffrey Lin, et al. Agents’ last exam.arXiv preprint arXiv:2606.05405, 2026.
[24] Zirui Tang, Xuanhe Zhou, Yumou Liu, Linchun Li, Yukai Wu, Weizheng Wang, Hongzhang Huang, Wei Zhou,
Jun Zhou, Jiachen Song, et al. Workspace-bench 1.0: Benchmarking ai agents on workspace tasks with large-scale
file dependencies. arXiv preprint arXiv:2605.03596, 2026.
[25] Kimi Team, Tongtong Bai, Yifan Bai, Yiping Bao, Jianfeng Cai, Xinyuan Cai, Peizhou Cao, Yuxuan Cao, Ziwei
Chai, Y Charles, et al. Kimi k3: Open frontier intelligence.arXiv preprint arXiv:2607.24653, 2026.
[26] Yubo Wang, Xueguang Ma, Ge Zhang, Yuansheng Ni, Abhranil Chandra, Shiguang Guo, Weiming Ren, Aaran
Arulraj, Xuan He, Ziyan Jiang, et al. Mmlu-pro: A more robust and challenging multi-task language understanding
benchmark. Advances in Neural Information Processing Systems, 37:95266–95290, 2024.
[27] Tianbao Xie, Danyang Zhang, Jixuan Chen, Xiaochuan Li, Siheng Zhao, Ruisheng Cao, Toh Jing Hua, Zhoujun
Cheng, Dongchan Shin, Fangyu Lei, Yitao Liu, Yiheng Xu, Shuyan Zhou, Silvio Savarese, Caiming Xiong, Victor
Zhong, and Tao Yu. OSWorld: Benchmarking multimodal agents for open-ended tasks in real computer envi-
ronments. InThe Thirty-eight Conference on Neural Information Processing Systems Datasets and Benchmarks
Track, 2024.
[28] Frank Fangzheng Xu, Yufan Song, Boxuan Li, Yuxuan Tang, Kritanjali Jain, Mengxue Bao, Zora Wang, Xuhui
Zhou, Zhitong Guo, Murong Cao, et al. Theagentcompany: benchmarking llm agents on consequential real world
tasks. Advances in Neural Information Processing Systems, 38, 2026.
[29] Qianyu Yang, Yang Liu, Jiaqi Li, Jun Bai, Hao Chen, Kaiyuan Chen, Tiliang Duan, Jiayun Dong, Xiaobo
Hu, Zixia Jia, et al. Onemillion-bench: How far are language agents from human experts? arXiv preprint
arXiv:2603.07980, 2026.
[30] Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and Yuan Cao. React: Syner-
gizing reasoning and acting in language models. In11th International Conference on Learning Representations,
ICLR 2023, 2023.
[31] Runyang You, Hongru Cai, Caiqi Zhang, Qiancheng Xu, Meng Liu, Tiezheng Yu, Yongqi Li, and Wenjie Li.
Agent-as-a-judge. arXiv preprint arXiv:2601.05111, 2026.
[32] Aohan Zeng, Xin Lv, Zhenyu Hou, Zhengxiao Du, Qinkai Zheng, Bin Chen, Da Yin, Chendi Ge, Chenghua Huang,
Chengxing Xie, et al. Glm-5: from vibe coding to agentic engineering.arXiv preprint arXiv:2602.15763, 2026.
[33] Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuohan
Li, Dacheng Li, Eric Xing, et al. Judging llm-as-a-judge with mt-bench and chatbot arena.Advances in neural
information processing systems, 36:46595–46623, 2023.
[34] Shuyan Zhou, Frank F Xu, Hao Zhu, Xuhui Zhou, Robert Lo, Abishek Sridhar, Xianyi Cheng, Tianyue Ou,
Yonatan Bisk, Daniel Fried, et al. Webarena: A realistic web environment for building autonomous agents. In
International Conference on Learning Representations, 2024.
[35] Liya Zhu, Jingzhe Ding, Jian Zhang, Jianbo Xue, Shihao Liang, Ge Zhang, Yi Zhu, Duju Zeng, Xiang Gao,
Qingshui Gu, Mailun Gao, Huimin Che, Yan Zhao, Peiheng Zhou, Haojun Wang, Chaobo Xian, Lili Le, Chi Wu,
Yiwei Liu, Shengda Long, Jiale Yang, Fangzhi Xu, Sijin Wu, Haodong Duan, Chao He, Zhaojian Li, Minchao
Wang, Huan Zhou, Jiani Hou, Chuqian Yu, Weiran Shi, Hongwan Gao, Jiamin Chen, Guanhong Chen, Tingqin
Luo, Kaiyuan Zhang, Zhixin Yao, Qing Hua, Yuhao Jiang, Jin Chen, Pu Chen, Zhenyu Hu, Xingyu Li, Zhengxuan
Jiang, Meng Cao, Tianfeng Long, Haozhe Wang, Mingzhang Wang, Yichen Zhang, Yiming Dai, Chenchen Zhang,
Jiaying Wang, Xinying Liu, Xingzu Liu, Lingling Zhang, Xinjie Chen, Yujia Qin, Wangchunshu Zhou, Zhiyong Wu,
Yang Liu, Jiaheng Liu, Lei Zhang, Shen Yan, Wenhao Huang, Zaiyuan Wang, and Xiaolong Chang. Workflow-gym:
17

Towards long-horizon evaluation of computer-use agentic tasks in real-world professional fields, 2026. URL
https://arxiv.org/abs/2606.11042.
[36] Mingchen Zhuge, Changsheng Zhao, Dylan R. Ashley, Wenyi Wang, Dmitrii Khizbullin, Yunyang Xiong, Zechun
Liu, Ernie Chang, Raghuraman Krishnamoorthi, Yuandong Tian, Yangyang Shi, Vikas Chandra, and Jürgen
Schmidhuber. Agent-as-a-judge: Evaluate agents with agents. In Forty-second International Conference on
Machine Learning, 2025.
18

Appendix
A Tutorial of StartupBench Task Annotation
A.1 Task Construction
Astartuptask can be defined as a tripleT = (q,E,R ). The experts are required to provide all the elements
of a task:
• Input query: The query q is a natural-language statement of the task, specifying the user instruction
that initiates the task. Derived from authentic scenarios of the work of annotators, the input query is
supposed to reflect realistic user intent, including task background, implicit constraints and expected
deliverables.
• Task workspace: The environment E denotes the complete workspace provided to the agent, including
the multimodal source files together with any additional resources and interaction setting required
to complete the task. The task workspace provides a self-contained execution environment for the
agent. Each workspace includes all necessary input artifacts (e.g., files, datasets, or structured resources)
required to complete the task, and ensures that the agent has access to sufficient input information
to solve the problem. This design enables reproducible evaluation under controlled conditions while
preserving realistic workflow structure.
• Evaluation rubrics: The rubric R = {(pi, wi)}n i=1 is a checklist within which every item consists of
a natural-language scoring pointpi and a positive importance weightwi reflecting its importance to
successful task completion. The evaluation rubrics define a set of fine-grained criteria used to assess
task completion quality. Due to the complexity and multi-faceted nature of real-world workflows, each
task is evaluated using multiple rubric items covering different dimensions. We categorize all rubrics in
StartupBench into 6 dimensions and 3 importance levels, which are detailed in Appendix C.
Together, these components preserve the structure of real-world agent workflows while enabling systematic
and objective evaluation. Tasks may require information synthesis, constraint following, structured generation,
or domain-specific reasoning and judgment.
A.2 Cross Validation
To ensure reliability of the quality of data, in our construction process each task is independently reviewed by
at least one additional domain expert with relevant professional experience. Rather than focusing only on
annotation consistency, reviewers validate the realism and correctness of the task from multiple complementary
perspectives.
• Task authenticity.Reviewers verify the authenticity of both the task description and the accompanying
workspace. This includes checking that the input query reflects realistic user requests, that all provided
materials are factually correct, and that no domain-specific knowledge errors exist.
• Workflow fidelity.Reviewers examine whether the task faithfully represents real-world workflows in the
corresponding profession. Tasks that deviate from practical working procedures or fail to reflect genuine
job responsibilities are revised or discarded.
• Rubric validity.Reviewers inspect the evaluation rubrics to ensure that the assessed capabilities are
meaningful for the target workflow, that rubric items are clear and unambiguous, and that their relative
weights reasonably reflect task priorities.
• Ground-truth verification.Reviewers validate the reference solution (ground truth) by evaluating
it against the finalized rubrics. The ground-truth deliverable is required to achieve a full score. If
inconsistencies are identified between the reference solution and the evaluation criteria, both the solution
and the rubrics are revised until they are mutually consistent.
19

Table 8Summary of domain expert backgrounds. Professional experience refers to reported years of experience in the
corresponding or closely related domain.
Expert Statistics Value
Number of domain experts 57
Median professional experience 5 years
Experts with≥3years of experience 68.4%
Experts with≥6years of experience 42.1%
Experts with≥10years of experience 24.6%
StartupBench domain coverage 6 / 6
B Domain Expert Background
We recruit 57 domain experts to support task construction and cross-validation. The expert pool covers all 6
domains in StartupBench and spans a diverse range of professional backgrounds, including clinical medicine,
law, investment and quantitative finance, software development and artificial intelligence, engineering, business
management and consulting, and education and humanities. Experts are assigned to tasks according to their
reported areas of expertise and professional experience, ensuring that task construction and review were
conducted by individuals familiar with the corresponding professional domains.
Table 8 summarizes the professional experience of the expert pool. The median professional experience is 5
years. Among the 57 experts, 68.4% have at least 3 years of professional experience, 42.1% have at least 6
years, and 24.6% have at least 10 years. These backgrounds provide practical domain knowledge for translating
interview-derived user scenarios into reproducible benchmark tasks and for assessing the realism, correctness,
and evaluation criteria of tasks during cross-validation. All experts are reasonably compensated based on the
actual workload associated with task construction and review.
C Rubrics of StartupBench
Rubric Dimensions.To facilitate consistent evaluation across heterogeneous real-world tasks, we organize all
evaluation rubrics into six high-level categories according to the primary capability they assess. Rather than
being tied to specific application domains, these categories capture common dimensions of deliverable quality
that recur across office tasks, including correctness, completeness, data processing, professional reasoning,
engineering quality, and presentation. This taxonomy enables more interpretable analysis of model strengths
and weaknesses while maintaining a unified evaluation framework across different task types.
• Structure & Completeness.Evaluates whether the required deliverables are fully produced with the
correct organization, file structure, required components, and overall completeness.
• Calculation Precision.Evaluates the correctness of numerical results, logical reasoning, formula execution,
factual consistency, and other objective computations.
• Information Integration.Evaluates data cleaning, transformation, aggregation, statistical analysis,
feature engineering, modeling, and other structured data manipulation workflows.
• Domain-Specific Compliance.Evaluates whether outputs satisfy domain-specific professional require-
ments, including business logic, financial principles, legal reasoning, medical practice, educational
standards, and other expert knowledge.
• Engineering & Format.Evaluates implementation quality, coding conventions, spreadsheet engineering,
document formatting, reproducibility, robustness, naming conventions, and compliance with technical
specifications.
• Output & Presentation.Evaluates the quality of visual presentation and communication, including
charts, layouts, formatting, readability, report organization, and overall usability of the final deliverables.
20

Table 9 summarizes the distribution of all 2,453 rubrics in StartupBench. Calculation Precision constitutes
the largest rubric category (38.9%), reflecting the importance of producing objectively correct work products.
Structure & Completeness and Domain-Specific Compliance together account for another 42.8%, highlighting
that successful completion of realistic office workflows requires not only correct computations but also complete
deliverables and professional domain reasoning.
Table 9Distribution of rubric categories in StartupBench.
Category Percentage
Structure & Completeness 27.31%
Calculation Precision 38.89%
Information Integration 9.46%
Domain-Specific Compliance 15.49%
Engineering & Format 6.20%
Output & Presentation 2.65%
Total 100.00%
Rubric Importance Levels.To account for differences in the importance of individual requirements to successful
task completion, we assign each rubric to one of three importance levels.Corerubrics capture requirements
that directly determine whether the primary user needs are satisfied; violating them would substantially
compromise the correctness, reliability, safety, or usability of the final deliverable.Importantrubrics represent
key requirements for high-quality task completion whose satisfaction materially affects the overall quality
of the deliverable, but whose individual violation does not necessarily render it unusable.Auxiliaryrubrics
capture lower-level requirements whose omission primarily affects details, user experience, visual appeal, or
polish rather than the fundamental usability of the deliverable. We assign weights of5,3, and1to Core,
Important, and Auxiliary rubrics, respectively, and use these weights when aggregating rubric-level judgments
into the task score. A typical case of task containing rubrics of different levels is shown at Figure 7.
Across all tasks, Core, Important, and Auxiliary rubrics account for an average of 59.10%, 34.33%, and 6.57%
of the total task weight, respectively, ensuring that task scores are primarily determined by requirements that
materially affect successful task completion.
D Examples of Behavior-level Failure Modes
D.1 Self-Verification Hallucination
A representative example is shown in Fig. 8. The task requires the model to filter all level-11 members, simulate
route check-ins until each member reaches the level-12 threshold, and generate an Excel workbook satisfying a
set of precise value and formatting constraints. The produced workbook appears largely complete, containing
the required worksheet, member records, and output columns, leading the model to conclude that the task
has been successfully finished. However, artifact-level inspection reveals multiple acceptance-critical errors,
including incorrect effective-point values and mismatched member names. The underlying issue is not that the
model fails to perform the required computation, but that it never verifies the generated artifact itself. Instead,
it treats a successful execution summary as evidence that the final deliverable has been validated. Consequently,
localized yet user-critical errors remain unnoticed, illustrating a form ofself-verification hallucination, where
confidence is derived from the reasoning process rather than from independently checking the completed
artifact against the original task requirements.
D.2 Domain-Specific Failure
A representative example of failure caused by insufficient domain-specific clinical actionability is shown at
Figure 9. The model generates a well-formatted multidisciplinary treatment plan that appears clinically
professional, yet violates multiple safety-critical treatment constraints. The failure stems not from poor
writing quality, but from an inability to convert medical knowledge into actionable and clinically reliable
decisions.
21

Figure 7A representative example of a rubric of a task spanning 3 levels. Core rubrics assess the essential financial
reasoning and calculations required to solve the investment problem, Important rubrics evaluate the correctness
and completeness of the supporting analysis, while Auxiliary rubrics capture presentation quality and additional
quantitative support.
22

Behavior Pattern
Self-Verification Hallucination
The agent checks selected calculations, but does not reconcile the final workbook with source names and output-field semantics.
1 Verification target
Membership anniversary workbook
Filter level-11 members and simulate route check-ins
until each reaches level 12.
Inputs member roster, route table, and store reward table
Rule effective points = total points - expired points
Stop stop immediately at the level-12 threshold
Output XLSX with 8 required columns and specified headers
Acceptance sensitivity
A summary can look correct even when exact-name and
cell-level spot checks fail.
2 Self-check drift
1
Local calculation succeeds
The agent computes thresholds and finds 30 level-11 members.
2
A plausible workbook is generated
The output has one worksheet, 30 data rows, and 8 requested columns.
3
Verification coverage remains partial
The agent checks selected calculations and rows, but
does not reconcile output fields with source semantics.
4
Artifact contradictions are missed
The reopened workbook stores post-upgrade points in the
current effective-points column; this goes undetected.
Model completion summary (translated)
30 level-11 members were selected; each simulation stops
when the level-12 threshold is reached.
3 Claim vs judge evidence
Model self-check
Complete; 30 members; route
simulation done.
Judge check
Artifact checks expose unresolved name
and field-value errors.
Judge-inspected output rows
The model's own summary is positive, but artifact-level spot checks show mismatched cells.
Check Member code Model Needed Judge
Points Member M-01 8497 7347 fail
Points Member M-02 8508 7548 fail
Points Member M-03 8527 7484 fail
Submitted H-column stores post-upgrade points, not current effective points.
Failure evidence
Names Two source labels contain required spaces; submitted labels omit them.
Points Sampled effective-point cells are post-stop values, not current values.
Pattern Partial checks miss name and column-semantic mismatches.
StartupBench compares the submitted workbook with explicit task requirements.
Instruction-level spot checks
The judge checks named members and exact cells
rather than trusting a final summary.
Artifact-first grading
The benchmark reads the submitted XLSX table
and compares values to expected outputs.
Self-check gap
The case separates plausible file generation from
instruction-level verification.
Pattern: overconfident self-verification. The agent reopens
the workbook and checks selected calculations, but fails to
reconcile exact names and the effective-points column with
source data before declaring completion.
Figure 8A representative example of self-verification hallucination. The model generates a plausible workbook and
concludes that the task has been completed based on its execution process. However, artifact-level spot checks expose
acceptance-critical errors in the final deliverable, showing that the model mistakes a progress summary for actual
verification instead of validating the generated artifact against the original task requirements.
23

Domain Profile
Medical Domain: Clinical Actionability
The submitted MDT plan is well structured, but conflicts with case-specific medication, timing, and handoff criteria.
1 Domain pressure
Clinical actionability
This case tests whether domain knowledge becomes
a coordinated plan that meets case-level criteria.
Clinical decision dependencies
Therapy Balance active bleeding control with very-early
post-DES thrombosis protection.
Timing Align anticoagulation restart with the
benchmark-defined window.
Handoff State one unified escalation and discharge
plan.
Representative domain risk
Medication continuation, restart timing, and discharge
step-down are coupled decisions. Surface fluency alone
does not establish case-level clinical actionability.
2 Medical failure chain
1
Conflicting clinical priorities
Upper GI bleeding conflicts with recent DES thrombosis
protection.
2
Case-specific P2Y12 criterion is violated
The case rubric requires uninterrupted clopidogrel; the plan
stops it before hemostasis.
3
Restart timing falls outside the case rubric
The plan uses day 5-7; the rubric specifies day 7-10.
4
Unified cath-lab decision is omitted
The plan does not restate that immediate cath-lab transfer is
not the current priority.
5
Discharge step-down is omitted
The plan defaults to triple therapy rather than the discharge
step-down required by the case rubric.
Fluent MDT structure can still fail case-specific safety criteria.
3 Representative case evidence
What looked complete
Five sections with staged medications;
roles, escalation, and discharge drugs.
What failed
Four case-specific decisions conflict with
or are absent from the submitted plan.
Artifact-level judge findings
P2Y12
Case rubric: clopidogrel uninterrupted
Submitted: stopped before hemostasis
Cath lab
Case condition: state no immediate cath lab
Submitted: not stated as unified decision
DOAC
Case rubric: day 7-10; not earlier than day 7
Submitted: restart day 5-7
Discharge
Case rubric: step down from triple therapy
Submitted: defaults to triple therapy
A structured answer can still fail artifact-level evaluation when
medication timing or unified decisions conflict with case criteria.
StartupBench checks the submitted handoff against the case and benchmark-defined criteria.
Clinical grounding
Medication and escalation decisions are checked
against the stated case and case rubric.
Workflow realism
The task requests a unified MDT plan for direct
adoption in the medical record.
Safety constraints
Continuation, restart timing, and discharge
sequencing are evaluated together.
Pattern: clinical actionability failure. The model produces
a structured MDT plan, but key medication and timing
decisions, together with the unified handoff, conflict with
case-specific evaluation criteria.
Figure 9A representative example of failure caused by insufficient domain-specific clinical actionability.
24
