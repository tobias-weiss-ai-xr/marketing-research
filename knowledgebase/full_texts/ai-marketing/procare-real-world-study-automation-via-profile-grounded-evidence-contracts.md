---
title: 'ProCARE: Real-World Study Automation via Profile-Grounded Evidence Contracts'
url: https://arxiv.org/abs/2610.16175
category: ai-marketing
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Zhaoyu Fan
- Bowen Han
- Jincheng Ou
- Yanwei Ren
- Zehua He
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.16175
pages: 42
chars: 155736
fetched_at: '2026-11-08T13:34:25+00:00'
kb_version: 1
---

# ProCARE: Real-World Study Automation via Profile-Grounded Evidence Contracts

ProCARE: Real-World Study Automation via
Profile-Grounded Evidence Contracts
Zhaoyu Fan1,3∗ Bowen Han1,3∗ Jincheng Ou1 Yanwei Ren1,2 Zehua He1 Kaiyu Huang1
Pengcheng He1 Shanshan Ni1 Chengchen Gong1 Shuai Xue3 Qingjiang Shi1,4†
1Tongji University
2University of Electronic Science and Technology of China
3Shanghai Hengfang Health Technology Co., Ltd.
4Shenzhen Research Institute of Big Data
Abstract
Real-world studies (RWS) analyze routinely collected healthcare data, such as
electronic health records and insurance claims, to estimate treatment effects, moni-
tor safety, and identify risk factors outside randomized trials. Automating RWS
with large language model agents is appealing but brittle: valid analyses depend
on dataset-specific clinical semantics, including index dates, follow-up windows,
patient/event-level units, and outcome boundaries that are often implicit in ob-
servational data. This leads to schema mismatches, temporal errors, inconsistent
analytical granularity, and unsupported clinical claims. We present ProCARE, a
profile-grounded framework that reformulates RWS automation as constrained
compilation. ProCARE converts heterogeneous data profiles into Evidence Con-
tracts specifying available variables, temporal attributes, distributions, and ev-
identiary limits, and compiles study objectives into RWS-IR, a strongly typed
intermediate representation for variables, time relations, analysis units, and sta-
tistical tasks. Deterministic validation and localized repair then check and revise
generated workflows across schema mapping, cohort construction, variable deriva-
tion, analysis, and interpretation. On 36 EHR-based benchmark tasks, ProCARE
outperforms strong LLM-agent baselines in code executability, semantic consis-
tency, and conclusion traceability, with automated violation diagnoses showing
moderate-to-substantial agreement with blinded expert review.
1 Introduction
Real-world studies (RWS) derive clinical evidence from observational healthcare data such as
electronic health records and insurance claims [1]. Unlike generic table analysis, RWS workflows are
constrained by relational structure, clinical variable semantics, temporal anchors, analysis grain, and
evidence scope. Cohorts must be assembled across heterogeneous tables, variables must be assigned
valid clinical roles, exposure and follow-up must be anchored consistently, and reported findings
must remain within the support of the executed analysis. These requirements make RWS automation
a structured scientific generation problem rather than a plain code-generation task.
LLM-based agents have been applied to data science and scientific workflow automation [2–4], but
their standard interfaces do not preserve all constraints required by schema-rich clinical data. Textu-
alizing multi-table datasets can obscure entity keys, visit structure, table linkage, missingness, and
time-dependent variables [5–7]. RWS requires domain-specific reasoning about endpoint definitions,
∗Equal contribution.
†Corresponding author. Email:shiqj@tongji.edu.cn.
GitHub repository: https://github.com/ZyFanTJ/ProCARE.
Preprint.
arXiv:2610.16175v1  [cs.AI]  12 Oct 2026

censoring, confounding, proxy variables, and claim scope [8, 9]. We observe three recurring failure
modes:query-to-specification failures, where study concepts are bound to missing, incompatible,
or ambiguous fields;specification-to-code failures, where free-form code violates the declared join
graph, analysis grain, temporal ordering, or artifact protocol; andartifact-to-claim failures, where
descriptive statistics or proxy artifacts are converted into unsupported clinical claims. These failures
indicate missing contracts between the data, study specification, executable workflow, and final
report—a structural bottleneck that bounds even strong baselines like Claude Code.
ProCARE addresses this gap by formulating RWS automation ascontract-valid generation. Its
object is a heterogeneous data profile Φ, which records schema structure, field statistics, clinical
semantics, temporal roles, validity flags, and assumptions. Rather than serving as a context summary,
Φ acts as a profile-grounded evidence contract. ProCARE compiles each user goal into a typed
RWS intermediate representation Z, turns Z into executable artifacts through a profile-constrained
coding harness, validates execution with deterministic static and runtime gates that produce localized
violation sets Ut, and admits report claims only through evidence certificates eq that link claims to
validated artifacts, executed code, profile entries, or recorded assumptions [ 10]. The output is an
auditable artifact bundle containing the profile, RWS-IR, generated code, execution logs, result and
figure manifests, validation evidence, assumptions, evidence certificates, and final report.
Contributions.(i) a heterogeneous RWS profile and typed RWS-IR that define a study contract
over data structure, clinical semantics, temporal roles, analysis grain, and assumptions; (ii) evidence
certificates that restrict factual report claims to validated artifacts, executed code, profile entries, IR
fields, or assumptions; and (iii) an end-to-end RWS evaluation over 36 HCC tasks and 18 public-health
transfer tasks, measuring executability, code quality, artifact completeness, and claim traceability.
2 Related Work
LLM agents for data analysis.Recent LLM agents combine reasoning, tool use, code execution,
and feedback for multi-step data-analysis and scientific workflows [11–14]. Data-analysis systems
and benchmarks such as InfiAgent-DABench, Data Interpreter, DSBench, and DataSciBench evaluate
agents that translate natural-language goals into programs, tables, visualizations, or model outputs [15–
18]. Despite this progress, these systems still report failures in state tracking, dependency management,
numerical consistency, and data-dependent repair. In RWS, such errors become methodological
failures because executable code must preserve relational structure, analysis grain, temporal anchors,
clinical roles, and claim scope. ProCARE addresses this setting with contract-valid generation over
typed study objects, executable artifacts, and certified claims.
Structured and clinical-data grounding.Another line of work improves LLM grounding over
spreadsheets, tables, SQL databases, and structured clinical records. Table-centric methods compress,
encode, or retrieve from large tabular structures [19–23], while text-to-SQL, structured-EHR, and
FHIR benchmarks evaluate reasoning over relational or resource-based clinical data [24–26]. These
methods improve structured-data access, but they mainly target retrieval, query answering, or task-
level execution. RWS automation further requires variable bindings, joins, temporal anchors, artifacts,
and claims to remain valid under one study-level contract. ProCARE enforces this contract by
propagating a heterogeneous profile through goal-to-IR compilation, profile-constrained execution,
and evidence-certified reporting.
RWS evidence constraints.RWE generation is governed by methodological, reporting, and regula-
tory constraints beyond table access or code execution. STROBE and RECORD emphasize transpar-
ent reporting of study design, data sources, variables, bias, missingness, and provenance [27, 28];
target-trial emulation and TARGET guidance require explicit protocols, estimands, eligibility criteria,
treatment strategies, follow-up, assumptions, and observational-data mappings [ 29, 30]. OMOP,
FHIR, and FDA guidance further emphasize standardized representation and reliable provenance
for RWD use [31–33]. Recent RWE automation benchmarks test whether LLM agents can conduct
observational analyses or reproducible hypothesis testing from medical databases [34, 35]. ProCARE
incorporates these constraints into generation by compiling typed RWS-IR, localizing execution
failures as contract violations, and admitting factual claims only through evidence certificates.
2

Cognitive Memory M Episodic Working Semantic Procedural
4 Certified DAG-Based Reporting
Reporting DAG(weighted)
1
Cohort
2
Methods
3
Results
4
Discussion
𝑊𝑊13 𝑊𝑊24
Reporting DAG(weighted)
Claim q Evidence Certificate 𝑒𝑒𝑞𝑞
Validated
Artifact O
Code
Region C*
IR Field/
Method Z
Profile
Entry 𝚽𝚽
Assumption
A
Admit(q)=1 if  Trace(q,𝑒𝑒𝑞𝑞, 𝑂𝑂, 𝐶𝐶 ∗, 𝑍𝑍, 𝚽𝚽,𝑆𝑆𝑡𝑡)=1
and Policy(q,Z)=1
• Unsupported claims are removed or downgraded.
• Proxy analyses allow descriptive/association claims only.
Heterogeneous RWS Profiling
Granularity
Abstraction
1
Low-G/
Structural
(𝚽𝚽𝑳𝑳,𝑺𝑺)
Low-G/
Knowledge
(𝚽𝚽𝑳𝑳,𝑲𝑲)
High-G/
Structural
(𝚽𝚽𝑯𝑯,𝑺𝑺)
High-G/
Knowledge
(𝚽𝚽𝑯𝑯,𝑲𝑲)
Heterogeneous sources
and artifacts
Profile 𝜱𝜱
Heterogeneous RWS
profiles
Violation-Guided Execution3
Z (𝚽𝚽𝑳𝑳,𝑺𝑺) ( 𝚽𝚽𝑳𝑳,𝑲𝑲 )
Coding Agent
Artifacts 𝑂𝑂𝑡𝑡/
Evidence 𝐸𝐸𝑡𝑡
Execution
Validator 𝑉𝑉𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒
Violation Set 𝑈𝑈𝑡𝑡
Repair & Revise
localized
repair
Accepted State
Executable
Code C*
Artifact
Bundle O
Violation
Evidence E
Assumptions A
{}
{}
RWS-IR Z
Typed intermediate
representation
Code/Artifacts C*,O,E
Executable code,
artifacts,evidence
Raw RWS Data Certified Report
DAG-structured,
claim-certified report
AI
2
User Goal 𝑇𝑇𝑔𝑔𝑔𝑔𝑔𝑔𝑔𝑔
+high-level profile
IR Compile
Candidate RWS-IR 𝑍𝑍0
IRCheck
Validated IR Z Static Violations 𝑈𝑈𝑠𝑠𝑡𝑡𝑔𝑔𝑡𝑡𝑠𝑠𝑒𝑒
Z = 〈D,G,J,K,T,V ,M,A,∏𝑞𝑞〉
𝐷𝐷𝑑𝑑𝑒𝑒𝑠𝑠𝑠𝑠𝑔𝑔𝑑𝑑, 𝐺𝐺𝑔𝑔𝑔𝑔𝑔𝑔𝑠𝑠𝑑𝑑,𝐽𝐽𝑗𝑗𝑔𝑔𝑠𝑠𝑑𝑑 𝑔𝑔𝑔𝑔𝑔𝑔𝑔𝑔𝑔,𝐾𝐾𝑘𝑘𝑒𝑒𝑘𝑘𝑠𝑠,
𝑇𝑇𝑔𝑔𝑑𝑑𝑒𝑒𝑔𝑔𝑔𝑔𝑔𝑠𝑠,𝑉𝑉𝑣𝑣𝑔𝑔𝑔𝑔𝑠𝑠𝑔𝑔𝑣𝑣𝑔𝑔𝑒𝑒𝑠𝑠,𝑀𝑀𝑚𝑚𝑒𝑒𝑡𝑡𝑔𝑔𝑔𝑑𝑑,
𝐴𝐴𝑔𝑔𝑔𝑔𝑡𝑡𝑠𝑠𝑎𝑎𝑔𝑔𝑒𝑒𝑡𝑡𝑠𝑠,∏𝑞𝑞𝑒𝑒𝑔𝑔𝑔𝑔𝑠𝑠𝑚𝑚 𝑔𝑔𝑔𝑔𝑔𝑔𝑠𝑠𝑒𝑒𝑘𝑘
Typed RWS-IR Compilation
Figure 1: ProCARE architecture for contract-valid RWS automation. A heterogeneous RWS profile
constrains RWS-IR compilation, violation-guided execution, and evidence-certified DAG reporting
as a profile-grounded evidence contract.
3 Method
ProCARE casts RWS automation as contract-valid generation over the three profile-constrained
transitions in Figure 1. Given a heterogeneous profile Φ and user goal Tgoal, it produces a typed study
specification, validated code, result artifacts, a report, and admissible claims:
Φ, Tgoal
profile contract
− − − − − − − − →(Z, C∗, O, R, Q),(1)
where Z is the RWS-IR, C ∗ validated code, O result and figure artifacts, R the report, and Q admitted
claims. The contract requires every study choice, code operation, and claim to trace to profile entries,
validated artifacts, or explicit assumptions.
ProCARE enforces this contract at three boundaries. Query-to-IR compilation admits only profile-
supported study designs, variables, temporal anchors, and methods. IR-to-code execution accepts only
runs that preserve the declared analysis grain, join graph, temporal ordering, and artifact requirements.
Artifact-to-claim reporting admits only claims with evidence certificates linked to validated artifacts,
executed code, IR fields, profile entries, or recorded assumptions.
The generation state is maintained as typed artifacts St ={Φ, Zt, Ct, Ot,E t,U t,A t}. Here Et stores
validation evidence,U t contract violations, andA t assumptions and limitations.
3.1 Heterogeneous Data Profiling
ProCARE first converts raw RWS inputs into a heterogeneous profileΦ = (ΦH,S,Φ H,K,Φ L,S,Φ L,K),
indexed by profile level (dataset/task vs. field/instance) and abstraction (structural vs. knowledge-
driven). Table 1 summarizes the four blocks. Structural blocks specify joins, grain, temporal anchors,
and artifact constraints; knowledge blocks record clinical roles, ontology mappings, proxy status,
assumptions, and claim scope. Deterministic parsers extract structural profiles, while ontology checks
over UMLS and SNOMED CT validate candidate clinical mappings for semantic type, units, ranges,
and temporal-role compatibility. Failed or ambiguous mappings are marked as semantically unknown
inΦ L,K with their failure causes.
Semantically unknown fields may support only structure-grounded operations: they cannot bind
clinical roles, derive endpoints, or support claims beyond their validated level unless a proxy or
explicit assumption is recorded. Thus, survival, safety, and utilization queries are compiled from
validated entity levels, linkage paths, temporal anchors, clinical roles, and support levels. Unsupported
choices are filtered, downgraded, or reported as limitations before IR compilation.
3

Table 1: Heterogeneous data profileΦorganized by profile level and abstraction.
High-level profile(dataset/task)Low-level profile(field/instance)
StructuralΦ H,S Clinical form registry; subject/visit/table linkage;
cohort-level missingness.
ΦL,S Field type, unit, range, date fields, temporal anchors,
and window-specific missingness.
KnowledgeΦ H,K Cohort and index-date schema; exposure, outcome,
censoring, confounder, and claim-scope roles.
ΦL,K Ontology mapping; unit/value validation; temporal-role
validation; field-level proxy and confounder roles.
3.2 RWS-IR Compilation and Violation-Guided Execution
The IR and execution stages implement the first two contract transitions: query-to-IR and IR-to-code.
The compiler turns the user goal into a typed RWS-IR, while the execution stage tests whether the
generated analysis can be run without violating the profile, the IR, or the artifact policy.
RWS-IR compilation.Given a research goal Tgoal, ProCARE first generates a candidate RWS-IR
using the high-level profile:
Z0 =f IR

Tgoal,Φ H,S ⊕Φ H,K ,(2)
where ⊕ denotes structured fusion of profile blocks. The candidate IR is admitted only after static
profile checking:
(Z,U static) = IRCheckstatic(Z0,Φ,S t).(3)
The accepted IR is Z=⟨D, G, J, K, T, V, M, A,Πq⟩, where D, G, J, K, T , V , M, A, and Πq
denote study design, analysis grain, join graph, entity keys, temporal anchors, variable-role bindings,
method specification, required artifacts, and claim policy, respectively.
Static checks enforce three conditions. First, all referenced tables, fields, and keys must appear in
ΦL,S. Second, clinical roles such as exposure, outcome, censoring, and confounder must be supported
by ΦL,K, marked as validated proxies, or explicitly recorded as assumptions. Third, the declared join
graph, index date, follow-up window, and analysis grain must be compatible with the profiled schema.
Only IRs with Ustatic =∅ enter code generation. Otherwise, ProCARE repairs the IR, downgrades
the unsupported request, or emits an infeasibility statement. Row-level temporal and grain checks are
deferred to execution-time validation.
Profile-constrained execution.Given an admitted IR, ProCARE generates executable analysis code
inside a workspace containing Z, ΦL,S, ΦL,K, the claim policy Πq, allowed tools, coding policies,
artifact validators, and execution logs. A run is accepted only if it produces validated code C ∗,
complete output artifactsO, validation evidenceE, and disclosed assumptions or limitationsA.
Execution is controlled by deterministic gates. Schema gates require every table, field, join key, and
output column to be traceable to ΦL,S. Method gates require cohort filters, index dates, exposure
definitions, endpoint or censoring rules, covariates, temporal windows, and statistical choices to
match Z and the validated semantic roles in ΦL,K. Artifact gates require the selected entry point,
such as analysis.py or main.py, to run successfully, avoid failure sentinels, and produce complete
result and figure manifests. After each execution attempt, validators return a violation set Ut =
Vexec(Zt, Ct, Ot,E t,Φ,S t). Each violation records the failed contract clause, offending code or
artifact, nearest valid profile entries, and permitted repair action. When Ut ̸=∅ , the next edit is
conditioned on the localized failures, (Zt+1, Ct+1) =A θ(Zt, Ct,U t,S t). The violation set guides
repair but does not imply global edit minimality.
If a requested endpoint, exposure, covariate, time window, or statistical analysis is unsupported
by the profile, ProCARE terminates with a transparent failure trace or downgrades the task to a
supported descriptive analysis with explicit limitations. Failed traces remain in St for inspection or
subsequent runs. This makes profile constraints and methodological assumptions observable during
code generation, rather than implicit in prompt context.
3.3 Certified DAG-Based Reporting
The reporting stage enforces the artifact-to-claim transition: only factual claims supported by validated
evidence and allowed by the claim policy are admitted. For each claim q, the report generator emits
an evidence certificate eq =⟨o q, cq, zq, ϕq, aq⟩, binding the claim to a supporting artifact, executed
code region, IR field or method, profile entry, and optional assumption or limitation. A claim is
4

admitted only if both traceability and policy checks pass:
Admit(q) =I[Trace(q, eq, O, C∗, Z,Φ,St) = 1∧Policy(q, Z,Π q) = 1].(4)
The trace condition grounds q in validated artifacts, executed code, IR fields, profile entries, or
disclosed assumptions; the policy condition checks whether its type and wording are allowed by
Z.Πq at the available support level. Unsupported claims are removed or rewritten as limitations.
Proxy-based or descriptive analyses may support descriptive or association claims, but not causal,
safety-critical, or high-stakes claims without the required design assumptions and validations.
After claim filtering, a dependency DAG orders report sections: nodes are report components, and
edges encode prerequisites such as cohort definition, variable construction, temporal anchors, sample
support, and method-design consistency. The DAG controls section order, while evidence certificates
control claim admissibility. The support score and traversal rule are provided in the appendix.
4 Evaluation and Benchmark
The benchmark evaluates complete RWS artifact bundles rather than isolated code outputs, covering
study specification, code synthesis, visualization, and scientific reporting. Because ProCARE natively
emits typed IRs, verifier traces, evidence certificates, and report-structure metadata, we distinguish
artifact-level comparative metrics from contract-native diagnostics. Deterministic validators assess
checkable constraints such as executability, schema use, temporal/grain consistency, artifact com-
pleteness, and claim support. Rubric-based judges are used only for residual semantic ambiguity,
presentation quality, or stylistic criteria.
Task construction.The primary benchmark contains 36 instances from four RWS domains:Cohort,
Safety,Efficacy, andEconomics. Each domain includes three research questions, and each question is
instantiated under three prompt-specificity levels: GOAL, GOAL+APPROACH, and GOAL+METHOD.
All instances use the same longitudinal HCC cohort described below. Agents receive raw relational
tables and natural-language prompts under a unified protocol.
Output contract.Each prompt containsTask, optionalGuidance, andDeliverables. The expected
bundle includes: (i) a study specification, or equivalent intermediate description, covering tables,
keys, variables, temporal anchors, methods, artifacts, and claim policy; (ii) an executable entry point,
such as analysis.py or main.py, with artifacts; and (iii) a structured report with assumptions,
limitations, and evidence links for factual claims. ProCARE instantiates this contract with typed
RWS-IRs and evidence certificates; non-ProCARE systems are evaluated via submitted or post-hoc
parsed specifications, manifests, and report-level evidence links. Hallucinated tables or columns are
disallowed. GOAL+METHODmust follow specified variables and terminate when required inputs are
missing; GOALand GOAL+APPROACHpermit the closest feasible analysis with explicit limitations.
Scoring protocol.Deterministic validators assess code executability, schema use, artifact com-
pleteness, temporal/grain consistency, and claim support. Study-specification validity is scored
after mapping each system’s submitted or parsed specification into the common benchmark schema;
native ProCARE IR objects are not treated as ground truth. Residual semantic criteria are scored
by Gemini-2.5-Pro and Qwen2.5-1M at temperature 0; judges are blinded to method identity and
evaluate full bundles under fixed rubrics. The same validators, rubrics, and post-hoc diagnostics are
applied to ProCARE, non-ProCARE baselines, and Public-RWS; Public-RWS omits repeated board-
certified review. All scores are normalized to [0,1] , and automated diagnostics are compared with
expert review on the primary benchmark. Artifact-level metrics support cross-system comparisons.
Contract-native metrics, such as explicit IR validity, native certificate coverage, and report-DAG
consistency, are reported as mechanism diagnostics and are not interpreted alone as evidence of
clinical, causal, or statistical correctness.
Let Nv, Rv be detected and resolved execution-time violations, and Nq, Cq, Uq, Lq be factual, certi-
fied, unsupported, and language-violating claims. We compute
VRR = Rv
Nv
,CTC = Cq
Nq
,UCR = Uq
Nq
,CL V = Lq
Nq
.(5)
VRR is measured over execution-time violations before the accepted run; CTC, UCR, and CLV are
measured over final-report factual claims. To reduce evaluator coupling, native contract artifacts
5

Table 2: Evaluation metrics for end-to-end RWS automation.
Dimension Metrics and scoring
IR GA: LLM-rubric goal alignment;PF: schema/IR feasibility with LLM adjudication.
Execution XE: sandbox pass raten pass/N;CQ: LLM-rubric code quality;VRR: resolved/detected contract
violations.
Visualization VC: LLM-rubric visual clarity;CF: chart–result consistency.
Reporting RS: report schema and section coverage;SL: LLM-rubric scientific language.
Claims CTC: post-hoc claim trace coverage;UCR: unsupported factual-claim rate;CLV: language-support
violation rate.
are separated from artifact-level scoring where possible. ProCARE’s RWS-IRs, manifests, verifier
traces, and evidence certificates are treated as system outputs rather than ground truth. For non-
ProCARE systems, the checker reconstructs the closest available study specification, artifact manifest,
and claim-evidence links from code, logs, tables, figures, reports, profile entries, and recorded
assumptions. CTC/UCR/CLV are then scored post hoc against executed artifacts, rather than by
accepting native certificates. Native certificate and DAG diagnostics are retained only for mechanism
audit. This mitigates, but does not eliminate, coupling because validity is still operationalized through
profile-derived constraints.
Primary HCC benchmark.The primary benchmark is derived from IRB-approved longitudinal
hepatocellular carcinoma data collected at a tertiary medical center. The released version is a fully
de-identified record-level benchmark: direct identifiers and fields that could identify individual
participants are removed before publication, while random benchmark subject and visit identifiers
preserve the relational structure needed for reproduction. The cohort contains 1,295 subjects, 12,847
visits, and 54 interlinked electronic case-report-form sheets covering baseline intake, follow-up,
treatments, laboratory measurements, outcomes, and quality-of-life assessments. The dataset captures
practical RWS challenges: subject- and visit-level linkage, sparse high-dimensional forms, form-
specific clinical conventions, redundant administrative fields, and longitudinal structure for repeated-
measures and time-to-event analyses. The public benchmark includes the de-identified HCC tables,
task specifications, schema/profile artifacts, prompts, data dictionary, checksums, and evaluation
scripts; a complete sheet inventory and release description are provided in the appendix.
Public-RWS external validation suite.Public-RWS-18 evaluates cross-dataset transfer on three
public health datasets: UCI Diabetes 130-US Hospitals, an EHR-derived encounter-level readmission
dataset [36, 37]; a NHANES 2017–2018 subset linking demographics, examination, questionnaire,
laboratory, medical-condition, and prescription-medication tables by SEQN [38]; and TCGA-LIHC,
HCC-aligned oncology metadata with demographic, diagnosis, treatment, vital-status, and follow-
up-related fields [39]. Each dataset contributes two task objectives under three prompt-specificity
levels, yielding 18 external validation tasks. The suite tests schema shift, multi-table grounding,
proxy-outcome handling, and claim traceability, complementing the primary HCC benchmark.
5 Experiments
We evaluate ProCARE along five research questions:RQ1end-to-end artifact validity against LLM-
agent and table-analysis baselines;RQ2contributions of individual contract mechanisms;RQ3
claim-level traceability and agreement with a five-member clinical/statistical expert panel;RQ4
robustness across RWS objectives, prompt specificity, and public-data schema shifts; andRQ5
sensitivity to the base LLM backbone and profiling cost amortization. The evaluation spans 36
primary HCC RWS tasks, 18 Public-RWS external validation tasks, baseline comparisons, ablations,
claim diagnostics, expert review, backbone sensitivity, and cost analysis.
5.1 Main Results
Baseline comparison (RQ1).We first compare ProCARE with LLM-agent, table-analysis, and
code-agent baselines under matched prompts, inference budgets, and artifact contracts. Table 3 shows
that existing methods often either fail to produce executable artifact bundles or emit factual claims
unsupported by admissible artifacts, code, or claim policies. Claude Code and Codex substantially
improve executability and code quality over generic agents, but remain weaker than ProCARE on
6

Table 3: Baseline comparison on 36 HCC RWS tasks. GA–SL report task performance, while
VRR–CLV report contract diagnostics following Table 2; N/A indicates no executable artifact bundle.
†Proprietary; ‡Open-source; §Agent-based.
Method GA↑PF↑XE↑CQ↑VC↑CF↑RS↑SL↑VRR↑CTC↑UCR↓CLV↓
ReAct‡§ 0.78 0.62 0.38 0.47 0.28 0.48 0.63 0.59 0.34 0.48 0.24 0.17
ToolLLM‡§ 0.73 0.68 0.00 N/A N/A N/A 0.56 0.24 0.00 0.21 0.33 0.24
TableGPT-Agent‡§ 0.61 0.59 N/A N/A N/A N/A 0.40 0.43 N/A 0.18 0.36 0.22
ChatExcel-Max†§ N/A N/A N/A N/A N/A N/A 0.52 0.27 N/A 0.12 0.39 0.28
Gemini-3-Pro direct† 0.75 0.51 0.13 0.45 0.28 0.48 0.61 0.53 0.18 0.36 0.27 0.15
TableGPT2‡ 0.41 0.45 0.00 0.25 N/A N/A N/A N/A 0.00 N/A N/A N/A
Claude Code†§ 0.82 0.75 0.86 0.80 0.52 0.58 0.71 0.66 0.70 0.66 0.16 0.12
Codex†§ 0.83 0.77 0.89 0.82 0.55 0.61 0.73 0.68 0.73 0.69 0.14 0.10
Methods without valid artifact bundles:LLM (DeepSeek-R1-0528); ChatExcel-Pro †§.
ProCARE (Ours) 0.86 0.84 0.92 0.88 0.72 0.74 0.80 0.79 0.81 0.90 0.06 0.03
Table 4: Scaffolded RQ1 controls. Direct rows use Gemini-3-Pro with the same decoding settings
as the default ProCARE backbone. Non-ProCARE rows are independent baseline adaptations;
ProCARE modules are not transplanted into them.
Baseline Fairness scaffold PF↑XE↑CQ↑VRR↑CTC↑UCR↓CLV↓
ReAct + scaffoldΦsummary + bundle tmpl. + val. feedback + 3 repairs 0.79 0.74 0.69 0.62 0.70 0.13 0.10
ToolLLM + scaffold Same scaffold on the tool-use baseline 0.80 0.68 0.65 0.58 0.66 0.15 0.12
G3P + profile/templateΦ+ manifests; no validator loop 0.73 0.66 0.62 0.31 0.55 0.20 0.15
G3P + validator repairΦ+ manifests + val. feedback + repairs 0.78 0.79 0.72 0.68 0.65 0.15 0.11
G3P + study-spec schema Emits study-spec artifact; no IR compiler 0.82 0.70 0.68 0.43 0.52 0.21 0.16
G3P + claim-trace schema Emits claim-trace artifact; no cert. gate 0.74 0.63 0.61 0.35 0.74 0.11 0.08
ProCARE reference Profile–IR–validator–certificate–DAG workflow 0.84 0.92 0.88 0.81 0.90 0.06 0.03
Table 5: Mechanism ablation over 36 RWS instances. N/A indicates no typed RWS-IR.
Variant PF↑XE↑VRR↑CTC↑UCR↓SL↑Dominant failure
No profileΦ0.49 0.18 0.35 0.58 0.28 0.42 Field hallucination; invalid joins.
No RWS-IR N/A 0.34 0.44 0.63 0.22 0.69 Missing grain, anchors, and claim policy.
No repair 0.84 0.69 0.43 0.80 0.13 0.70 Unresolved runtime and artifact violations.
No certificates 0.84 0.92 0.81 N/A 0.26 0.62 Unsupported causal or comparative claims.
No DAG ordering 0.84 0.92 0.81 0.84 0.11 0.64 Dependency-agnostic report ordering.
Full ProCARE 0.84 0.92 0.81 0.90 0.06 0.79Localized repair; traceable final claims.
clinically grounded profile fit, variable-role consistency, statistical language, and claim traceability.
To partially control for evaluator bias toward systems that natively emit IRs, manifests, and evidence
certificates, we additionally evaluate scaffolded baselines. These RQ1 controls keep the tested system
as an external baseline or direct Gemini-3-Pro run, while only adding evaluator-facing information,
output schemas, validator feedback, and repair budget. They do not expose ProCARE’s typed IR
compiler, certificate admission gate, certified reporting DAG, or internal planner state. The scaffolds
improve generic baselines, especially in executability and artifact completeness. ProCARE still
achieves the strongest violation resolution and post-hoc claim traceability (Table 4), suggesting that
its advantage is not explained by schema exposure or manifest formatting alone.
Contract mechanism ablation (RQ2).To identify the sources of improvement, we ablate each
contract object in Table 5. The profile yields the largest contribution, suggesting that reliable schema,
field, and join constraints are the basis for valid execution and downstream reasoning. RWS-IR
supplies the typed study contract and strengthens claim-policy control. Violation-guided repair mainly
improves executable constraint satisfaction, whereas evidence certificates and certified DAG ordering
primarily affect reporting: the former enforces claim traceability, and the latter preserves dependency-
aware structure. These results indicate that the framework’s gains come from complementary
contract objects: structural contracts support computation, repair improves execution robustness, and
evidence/order contracts regulate faithful reporting.
Claim traceability and expert validation (RQ3).Table 6 reports post-hoc claim diagnostics for
ProCARE. More specific prompts improve CTC and reduce UCR/CLV , mainly by constraining
7

Table 6: ProCARE claim diagnostics. Values are averaged over 12 instances per prompt level; Overall
aggregates all 36 instances.
Prompt Claims CTC↑UCR↓CLV↓Main downgrade reason
GOAL5.8 0.87 0.09 0.05 Unsupported causal/comparative wording.
GOAL+APPROACH6.4 0.90 0.05 0.03 Proxy endpoint beyond evidence level.
GOAL+METHOD6.9 0.94 0.03 0.02 Sparse endpoint or subgroup evidence.
Overall 6.4 0.90 0.06 0.03Downgrades mainly concern causal strength.
Table 7: Expert consistency of automated metrics. Expert scores are mean±SD on a 5-point scale; CI
and reliability details are reported in the appendix.
Stage Reviewers Metric(s) Auto Expertρ
RWS-IR 3 clinical + 2 stats/data(GA+P F)/20.82 4.38±0.48 0.82
Code 2 stats/dataCQ0.88 4.42±0.21 0.74
Visualization 3 clinical + 2 stats/data(V C+CF)/20.66 4.50±0.53 0.75
Reporting 3 clinical + 2 stats/dataSL0.76 4.13±0.64 0.71
All Spearman correlations are computed across the 36 primary HCC instances; allp <0.001.
Goal
Goal+Appr .
Goal+Method
.85 .83 .93 .87 .79 .73 .72 .81 .78 .91 .07 .04
.90 .88 .96 .92 .85 .76 .78 .84 .83 .94 .04 .02
.93 .91 .98 .95 .88 .82 .81 .87 .86 .97 .02 .01
Cohort
Goal
Goal+Appr .
Goal+Method
.78 .76 .86 .82 .75 .63 .68 .72 .74 .82 .11 .07
.83 .81 .89 .85 .78 .69 .71 .77 .76 .87 .07 .04
.88 .84 .92 .90 .83 .72 .76 .80 .82 .90 .04 .02
Safety
GA PF XE CQ VRR VC CF RS SL CTC
UCR↓ CLV↓
Goal
Goal+Appr .
Goal+Method
.82 .80 .90 .84 .77 .70 .72 .76 .75 .88 .09 .05
.87 .85 .93 .89 .82 .73 .75 .81 .80 .91 .05 .03
.90 .90 .96 .94 .85 .78 .80 .86 .83 .96 .03 .02
Efficacy
GA PF XE CQ VRR VC CF RS SL CTC
UCR↓ CLV↓
Goal
Goal+Appr .
Goal+Method
.81 .77 .85 .83 .73 .67 .69 .75 .71 .85 .08 .05
.84 .82 .90 .86 .79 .70 .72 .78 .77 .88 .05 .02
.89 .85 .93 .91 .82 .75 .77 .81 .82 .93 .03 .01
Economics
Figure 2: Performance across four RWS tasks and prompt-specificity levels. Cell labels report raw
metric values; UCR and CLV are lower-is-better rates with reversed color intensity.
variable bindings, temporal anchors, and methods. Remaining downgrades mostly involve causal or
high-stakes wording unsupported by proxy artifacts, sparse endpoints, or subgroup evidence. We
further compare automated diagnostics with blinded review by three clinical and two statistics/data
experts. Table 7 shows moderate-to-strong Spearman agreement across stages, strongest for RWS-IR
validity (ρ= 0.82 ) and significant for code, visualization, and reporting. The appendix provides
reviewer rubrics, aggregation rules, confidence intervals, and inter-rater reliability.
5.2 Robustness and Deployment Analyses
Task, prompt, and public-data robustness (RQ4).Figure 2 evaluates ProCARE across four
RWS objectives and three prompt-specificity levels on the HCC benchmark. Metrics generally
improve with prompt specificity, suggesting that methodological context helps specification, repair,
and claim control. Performance is stable across task families; residual variation is mainly due
to sparse endpoints, limited subgroup support, and claim-scope restrictions. Table 8 evaluates
Public-RWS-18 schema transfer without dataset-specific changes. Claim policies restrict outputs to
descriptive/readmission-proxy claims for UCI Diabetes, descriptive/association claims for NHANES,
and descriptive oncology-metadata/follow-up-proxy claims for TCGA-LIHC. ProCARE outperforms
Claude Code and Scaffolded G3P in violation resolution, post-hoc claim traceability, UCR, and CLV;
NHANES remains hardest due to multi-table survey joins.
Backbone sensitivity and cost (RQ5).Holding the profile, RWS-IR, validators, and certificate gate
fixed, ProCARE remained contract-consistent across tested backbones; stronger planners mainly
improved GA, PF, VRR, and CTC, while execution metrics were comparatively stable. Profiling is
a one-time dataset cost (Tprof ≈65 k tokens for the HCC schema); per-query inference costs about
8

Table 8: Public-RWS-18 transfer results. Values average six tasks per dataset; baseline claim traces
are computed post hoc.
Dataset Method XE↑VRR↑CTC↑UCR↓CLV↓
UCI DiabetesClaude Code 0.60 0.61 0.69 0.12 0.09
Scaffolded G3P 0.57 0.59 0.66 0.13 0.10
ProCARE 0.64 0.72 0.87 0.07 0.04
NHANESClaude Code 0.52 0.54 0.63 0.15 0.11
Scaffolded G3P 0.50 0.52 0.60 0.16 0.12
ProCARE 0.58 0.66 0.84 0.09 0.06
TCGA-LIHCClaude Code 0.57 0.58 0.66 0.14 0.10
Scaffolded G3P 0.54 0.56 0.63 0.15 0.11
ProCARE 0.61 0.69 0.86 0.08 0.05
Table 9: Backbone sensitivity with fixed ProCARE workflow. Metrics follow Table 2; model access
details and version identifiers are reported in the appendix. †Proprietary models; ‡Open-source
models.
Family Model Performance Contract diagnostics
GA↑PF↑XE↑CQ↑VC↑CF↑RS↑SL↑VRR↑CTC↑UCR↓CLV↓
GPT GPT-5.2† 0.84 0.82 0.94 0.84 0.68 0.70 0.78 0.77 0.78 0.88 0.060.04 GPT-4 Turbo† 0.81 0.78 0.89 0.80 0.64 0.66 0.75 0.74 0.74 0.85 0.08 0.06
Claude Claude Opus 4.5† 0.85 0.83 0.970.86 0.72 0.740.78 0.77 0.80 0.890.060.04 Claude Sonnet 4.5† 0.83 0.81 0.94 0.84 0.70 0.72 0.76 0.75 0.78 0.87 0.07 0.05
Gemini Gemini-3-Pro† 0.86 0.840.920.88 0.72 0.74 0.80 0.79 0.81 0.90 0.06 0.03 Gemini-2.5-Pro† 0.82 0.78 0.91 0.82 0.66 0.68 0.75 0.74 0.76 0.86 0.08 0.06
Qwen Qwen3-Max† 0.77 0.70 0.84 0.76 0.58 0.60 0.68 0.68 0.68 0.80 0.12 0.09 Qwen3-235B-Instruct‡ 0.74 0.66 0.80 0.72 0.55 0.57 0.64 0.65 0.64 0.76 0.15 0.11
DeepSeek DeepSeek-V3.2‡ 0.76 0.68 0.86 0.78 0.60 0.62 0.66 0.67 0.70 0.80 0.11 0.08 DeepSeek-R1-0528‡ 0.72 0.64 0.82 0.74 0.56 0.58 0.62 0.63 0.66 0.77 0.13 0.10
Tinf ≈38 k tokens, giving an amortized cost ¯T(N) =T inf +T prof /N and ¯T(20)≈41.3 k tokens.
Full backbone results are reported in Appendix.
Token budgets are not directly comparable across agents because each baseline uses a different
pipeline, so we report token use for PROCARE. Profiling is a one-time dataset cost, about Tprof ≈65k
tokens for the rich schema; each query then uses about Tinf ≈38k tokens. For N queries on the same
dataset, the amortized cost is ¯T(N) =T inf +T prof /N. A single query costs ¯T(1)≈103 k tokens;
withN=20, the cost falls to ¯T(20)≈41.3k tokens, close to the inference-only cost.
Discussion and Limitations.Overall, ProCARE should be interpreted as a contract layer for making
RWS assumptions, artifacts, and claim support auditable under human oversight. Its reliability
depends on the correctness of the constructed profile, the coverage of deterministic validators,
and the assumptions encoded in the RWS-IR. A successful run shows that the generated bundle
satisfies the implemented schema, method, temporal, and artifact checks; it does not establish clinical
optimality, adequate confounding control, causal validity, or evidentiary sufficiency beyond the
recorded assumptions. The primary benchmark is single-center and disease-specific, and Public-
RWS-18 mainly tests schema transfer rather than multi-institutional longitudinal generalization.
Deployments on OMOP, FHIR, or institutional schemas therefore require re-instantiating the profile
and revalidating the IR, execution gates, and certificate checks.
6 Conclusion
We introduced ProCARE, a profile-grounded contract architecture for RWS automation. ProCARE
compiles study goals into typed RWS-IR, generates executable artifact bundles through a profile-
constrained coding harness, repairs localized contract violations, and admits report claims through
evidence certificates. On a 36-instance HCC RWS benchmark and Public-RWS-18 external validation
9

suite, these mechanisms improve executable validity, code quality, and claim traceability relative to
LLM-agent and table-analysis baselines. The public release includes the fully de-identified HCC
benchmark tables and scoring assets to support independent reproduction. Future work should
test the same contract mechanisms on multi-institutional longitudinal RWS data and standardized
OMOP/FHIR deployments.
References
[1] Rachel E. Sherman, Steven A. Anderson, Gerald J. Dal Pan, Gerry W. Gray, Thomas Gross,
Nina L. Hunter, Lisa LaVange, Danica Marinac-Dabic, Peter W. Marks, Melissa A. Robb,
Jeffrey Shuren, Robert Temple, Janet Woodcock, Lilly Q. Yue, and Robert M. Califf. Real-
world evidence - what is it and what can it tell us?The New England journal of medicine, 375
(23):2293–2297, 2016. doi: 10.1056/NEJMsb1609216.
[2] Yizhen Zheng, Huan Yee Koh, Jiaxin Ju, Anh T. N. Nguyen, Lauren T. May, Geoffrey I. Webb,
and Shirui Pan. Large language models for scientific synthesis, inference and explanation.arXiv
preprint arXiv:2310.07984, 2023.
[3] Yixing Jiang, Kameron C Black, Gloria Geng, Danny Park, James Zou, Andrew Y Ng, and
Jonathan H Chen. MedAgentBench: A realistic virtual EHR environment to benchmark medical
LLM agents.arXiv preprint arXiv:2501.14654, 2025.
[4] Jonathan Kim, Anna Podlasek, Kie Shidara, Feng Liu, Ahmed Alaa, and Danilo Bernardo. Lim-
itations of large language models in clinical problem-solving arising from inflexible reasoning.
Scientific Reports, 15(1):39426, 2025.
[5] Alvin Rajkomar, Eyal Oren, Kai Chen, Andrew Dai, Nissan Hajaj, Peter Liu, Xiaobing Liu,
Mimi Sun, Patrik Sundberg, Hector Yee, Kun Zhang, Gavin Duggan, Gerardo Flores, Michaela
Hardt, Jamie Irvine, Quoc Le, Kurt Litsch, Jake Marcus, Alexander Mossin, and Jeff Dean.
Scalable and accurate deep learning for electronic health records.npj Digital Medicine, 1:18,
2018. doi: 10.1038/s41746-018-0029-1.
[6] George Hripcsak, Jon Duke, Nigam Shah, Christian Reich, V ojtech Huser, Martijn Schuemie,
Marc Suchard, Rae Woong Park, Ian Wong, Peter Rijnbeek, Johan Lei, Nicole Pratt, Niklas
Norén, Yu-Chuan Li, Paul Stang, David Madigan, and Patrick Ryan. Observational health data
sciences and informatics (ohdsi): Opportunities for observational researchers.Studies in health
technology and informatics, 216:574–8, 2015.
[7] Jan-Micha Bodensohn, Ulf Brackmann, Liane V ogel, Anupam Sanghi, and Carsten Binnig.
Unveiling challenges for llms in enterprise data engineering.arXiv preprint arXiv:2504.10950,
2025.
[8] Karan Singhal, Shekoofeh Azizi, Tao Tu, S. Sara Mahdavi, Jason Wei, Hyung Won Chung,
Nathan Scales, Ajay Tanwani, Heather Cole-Lewis, Stephen Pfohl, Perry Payne, Martin Senevi-
ratne, Paul Gamble, Chris Kelly, Nathaneal Scharli, Aakanksha Chowdhery, Philip Mansfield,
Blaise Aguera y Arcas, Dale Webster, Greg S. Corrado, Yossi Matias, Katherine Chou, Juraj
Gottweis, Nenad Tomasev, Yun Liu, Alvin Rajkomar, Joelle Barral, Christopher Semturs, Alan
Karthikesalingam, and Vivek Natarajan. Large language models encode clinical knowledge.
Nature, 620:172–180, 2023.
[9] Hanchen Wang, Tianfan Fu, Yuanqi Du, Wenhao Gao, Kexin Huang, Ziming Liu, Payal
Chandak, Shengchao Liu, Peter Van Katwyk, Andreea Deac, Anima Anandkumar, Karianne J.
Bergen, Carla P. Gomes, Shirley Ho, Pushmeet Kohli, Joan Lasenby, Jure Leskovec, Tie-Yan
Liu, Arjun K. Manrai, Debora S. Marks, Bharath Ramsundar, Le Song, Jimeng Sun, Jian Tang,
Petar Velickovic, Max Welling, Linfeng Zhang, Connor W. Coley, Yoshua Bengio, and Marinka
Zitnik. Scientific discovery in the age of artificial intelligence.Nature, 620:47–60, 2023. URL
https://api.semanticscholar.org/CorpusID:260384616.
[10] Samuel Schmidgall, Yusheng Su, Ze Wang, Ximeng Sun, Jialian Wu, Xiaodong Yu, Jiang Liu,
Zicheng Liu, and Emad Barsoum. Agent laboratory: Using llm agents as research assistants.
arXiv preprint arXiv:2501.04227, 2025.
10

[11] Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and Yuan
Cao. ReAct: Synergizing reasoning and acting in language models. InProceedings of the
11th International Conference on Learning Representations, 2023. URL https://openreview.net/
forum?id=WE_vluYUL-X.
[12] Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, and Shunyu Yao.
Reflexion: Language agents with verbal reinforcement learning. InAdvances in Neural Infor-
mation Processing Systems, volume 36, 2023. URL https://proceedings.neurips.cc/paper_files/
paper/2023/hash/1b44b878bb782e6954cd888628510e90-Abstract-Conference.html.
[13] Yujia Qin, Shihao Liang, Yining Ye, Kunlun Zhu, Lan Yan, Yaxi Lu, Yankai Lin, Xin Cong,
Xiangru Tang, Bill Qian, Sihan Zhao, Lauren Hong, Runchu Tian, Ruobing Xie, Jie Zhou, Mark
Gerstein, Dahai Li, Zhiyuan Liu, and Maosong Sun. ToolLLM: Facilitating large language
models to master 16000+ real-world APIs. InProceedings of the 12th International Conference
on Learning Representations, 2024. URL https://openreview.net/forum?id=dHng2O0Jjr.
[14] Qingyun Wu, Gagan Bansal, Jieyu Zhang, Yiran Wu, Beibin Li, Erkang Zhu, Li Jiang, Xiaoyun
Zhang, Shaokun Zhang, Jiale Liu, Ahmed Hassan Awadallah, Ryen W. White, Doug Burger,
and Chi Wang. AutoGen: Enabling next-gen LLM applications via multi-agent conversation,
2023. URL https://arxiv.org/abs/2308.08155.
[15] Xueyu Hu, Ziyu Zhao, Shuang Wei, Ziwei Chai, Qianli Ma, Guoyin Wang, Xuwu Wang,
Jing Su, Jingjing Xu, Ming Zhu, Yao Cheng, Jianbo Yuan, Jiwei Li, Kun Kuang, Yang Yang,
Hongxia Yang, and Fei Wu. InfiAgent-DABench: Evaluating agents on data analysis tasks.
InProceedings of the 41st International Conference on Machine Learning, volume 235 of
Proceedings of Machine Learning Research, pages 19544–19572. PMLR, 2024. URL https:
//proceedings.mlr.press/v235/hu24s.html.
[16] Sirui Hong, Yizhang Lin, Bang Liu, Bangbang Liu, Binhao Wu, Ceyao Zhang, Danyang
Li, Jiaqi Chen, Jiayi Zhang, Jinlin Wang, Li Zhang, Lingyao Zhang, Min Yang, Mingchen
Zhuge, Taicheng Guo, Tuo Zhou, Wei Tao, Robert Tang, Xiangtao Lu, Xiawu Zheng, Xinbing
Liang, Yaying Fei, Yuheng Cheng, Yongxin Ni, Zhibin Gou, Zongze Xu, Yuyu Luo, and
Chenglin Wu. Data interpreter: An LLM agent for data science. InFindings of the Associa-
tion for Computational Linguistics: ACL 2025, pages 19796–19821, Vienna, Austria, 2025.
Association for Computational Linguistics. doi: 10.18653/v1/2025.findings-acl.1016. URL
https://aclanthology.org/2025.findings-acl.1016/.
[17] Liqiang Jing, Zhehui Huang, Xiaoyang Wang, Wenlin Yao, Wenhao Yu, Kaixin Ma, Hongming
Zhang, Xinya Du, and Dong Yu. DSBench: How far are data science agents from becoming
data science experts? InProceedings of the 13th International Conference on Learning
Representations, 2025. URL https://openreview.net/forum?id=DSsSPr0RZJ.
[18] Dan Zhang, Sining Zhoubian, Min Cai, Fengzu Li, Lekang Yang, Wei Wang, Tianjiao Dong,
Ziniu Hu, Jie Tang, and Yisong Yue. DataSciBench: An LLM agent benchmark for data science,
2025. URL https://arxiv.org/abs/2502.13897. Use cautiously in main text; the corresponding
ICLR 2025 OpenReview submission was withdrawn.
[19] Hongxin Li, Jingran Su, Yuntao Chen, Qing Li, and Zhaoxiang Zhang. SheetCopilot: Bringing
software productivity to the next level through large language models. InAdvances in Neural
Information Processing Systems, volume 36, 2023. URL https://openreview.net/forum?id=
tfyr2zRV oK.
[20] Haoyu Dong, Jianbo Zhao, Yuzhang Tian, Junyu Xiong, Mengyu Zhou, Yun Lin, José Cam-
bronero, Yeye He, Shi Han, and Dongmei Zhang. Encoding spreadsheets for large language
models. InProceedings of the 2024 Conference on Empirical Methods in Natural Language
Processing, pages 20728–20748, Miami, Florida, USA, 2024. Association for Computational
Linguistics. doi: 10.18653/v1/2024.emnlp-main.1154. URL https://aclanthology.org/2024.
emnlp-main.1154/.
[21] Aofeng Su, Aowen Wang, Chao Ye, Chen Zhou, Ga Zhang, Gang Chen, Guangcheng Zhu,
Haobo Wang, Haokai Xu, Hao Chen, Haoze Li, Haoxuan Lan, Jiaming Tian, Jing Yuan, Junbo
Zhao, Junlin Zhou, Kaizhe Shou, Liangyu Zha, Lin Long, Liyao Li, Pengzuo Wu, Qi Zhang,
11

Qingyi Huang, Saisai Yang, Tao Zhang, Wentao Ye, Wufang Zhu, Xiaomeng Hu, Xijun Gu,
Xinjie Sun, Xiang Li, Yuhang Yang, and Zhiqing Xiao. TableGPT2: A large multimodal model
with tabular data integration, 2024. URL https://arxiv.org/abs/2411.02059.
[22] Si-An Chen, Lesly Miculicich, Julian Martin Eisenschlos, Zifeng Wang, Zilong Wang, Yanfei
Chen, Yasuhisa Fujii, Hsuan-Tien Lin, Chen-Yu Lee, and Tomas Pfister. TableRAG: Million-
token table understanding with language models. InAdvances in Neural Information Processing
Systems, volume 37, 2024. URL https://openreview.net/forum?id=41lovPOCo5.
[23] Xiaohan Yu, Pu Jian, and Chong Chen. TableRAG: A retrieval augmented generation framework
for heterogeneous document reasoning, 2025. URL https://arxiv.org/abs/2506.10380. Accepted
by EMNLP 2025.
[24] Gyubok Lee, Sunjun Kweon, Seongsu Bae, and Edward Choi. Overview of the EHRSQL 2024
shared task on reliable text-to-SQL modeling on electronic health records. InProceedings of
the 6th Clinical Natural Language Processing Workshop, pages 644–654, Mexico City, Mexico,
2024. Association for Computational Linguistics. doi: 10.18653/v1/2024.clinicalnlp-1.62. URL
https://aclanthology.org/2024.clinicalnlp-1.62/.
[25] Xiao Yang, Xuejiao Zhao, and Zhiqi Shen. EHRStruct: A comprehensive benchmark framework
for evaluating large language models on structured electronic health record tasks. InProceedings
of the AAAI Conference on Artificial Intelligence, pages 34340–34348, 2026. URL https:
//ojs.aaai.org/index.php/AAAI/article/view/40731.
[26] Gyubok Lee, Elea Bach, Eric Yang, Tom Pollard, Alistair Johnson, Edward Choi, Yugang Jia,
and Jong Ha Lee. FHIR-AgentBench: Benchmarking LLM agents for realistic interoperable
EHR question answering, 2025. URL https://arxiv.org/abs/2509.19319.
[27] Jan P. Vandenbroucke, Erik von Elm, Douglas G. Altman, Peter C. Gøtzsche, Cynthia D. Mulrow,
Stuart J. Pocock, Charles Poole, James J. Schlesselman, and Matthias Egger. Strengthening the
reporting of observational studies in epidemiology (STROBE): Explanation and elaboration.
PLoS Medicine, 4(10):e297, 2007. doi: 10.1371/journal.pmed.0040297. URL https://doi.org/10.
1371/journal.pmed.0040297.
[28] Eric I. Benchimol, Liam Smeeth, Astrid Guttmann, Katie Harron, David Moher, Irene Petersen,
Henrik T. Sørensen, Erik von Elm, and Sinéad M. Langan. The REporting of studies conducted
using observational routinely-collected health data (RECORD) statement.PLoS Medicine,
12(10):e1001885, 2015. doi: 10.1371/journal.pmed.1001885. URL https://doi.org/10.1371/
journal.pmed.1001885.
[29] Miguel A. Hernán and James M. Robins. Using big data to emulate a target trial when a
randomized trial is not available.American Journal of Epidemiology, 183(8):758–764, 2016.
doi: 10.1093/aje/kwv254. URL https://doi.org/10.1093/aje/kwv254.
[30] Aidan G. Cashin, Harrison J. Hansford, Miguel A. Hernán, Sonja A. Swanson, Hopin Lee,
Matthew D. Jones, Issa J. Dahabreh, Barbra A. Dickerman, Matthias Egger, Xabier Garcia-
Albeniz, Robert M. Golub, Nazrul Islam, Sara Lodi, Margarita Moreno-Betancur, Sallie-Anne
Pearson, Sebastian Schneeweiss, Melissa K. Sharp, Jonathan A. C. Sterne, Elizabeth A. Stuart,
and James H. McAuley. Transparent reporting of observational studies emulating a target trial—
the TARGET statement.JAMA, 334(12):1084–1093, 2025. doi: 10.1001/jama.2025.13350.
URL https://doi.org/10.1001/jama.2025.13350.
[31] Observational Health Data Sciences and Informatics. OMOP common data model. https:
//ohdsi.github.io/CommonDataModel/, 2026. Accessed: 2026-05-02.
[32] Health Level Seven International. FHIR release 4.0.1: Fast healthcare interoperability resources.
https://www.hl7.org/fhir/, 2019. Accessed: 2026-05-02.
[33] U.S. Food and Drug Administration. Data standards for drug and biolog-
ical product submissions containing real-world data: Guidance for indus-
try. https://www.fda.gov/regulatory-information/search-fda-guidance-documents/
data-standards-drug-and-biological-product-submissions-containing-real-world-data,
2023. Final guidance, December 2023. Accessed: 2026-05-02.
12

[34] Dubai Li, Yuxiang He, Yan Hu, Yu Tian, and Jingsong Li. Can LLM agents generate real-
world evidence? evaluating observational studies in medical databases, 2026. URL https:
//arxiv.org/abs/2603.22767.
[35] Nayoon Gim, In Gim, Yu Jiang, Yuka Kihara, Marian Blazes, Yue Wu, Cecilia S. Lee, and
Aaron Y . Lee. An LLM-assisted framework for accelerated and verifiable clinical hypothesis
testing from electronic health records.medRxiv, 2026. doi: 10.64898/2026.02.10.26346008.
URL https://www.medrxiv.org/content/10.64898/2026.02.10.26346008v1. Preprint.
[36] John Clore, Krzysztof J. Cios, Jonathan P. DeShazo, and Beata Strack. Diabetes 130-US
hospitals for years 1999–2008, 2014. URL https://archive.ics.uci.edu/dataset/296/diabetes%
2B130-us%2Bhospitals%2Bfor%2Byears%2B1999-2008.
[37] Beata Strack, Jonathan P. DeShazo, Chris Gennings, Juan L. Olmo, Sebastian Ventura,
Krzysztof J. Cios, and John N. Clore. Impact of HbA1c measurement on hospital readmission
rates: Analysis of 70,000 clinical database patient records.BioMed Research International,
2014:781670, 2014. doi: 10.1155/2014/781670. URL https://doi.org/10.1155/2014/781670.
[38] Centers for Disease Control and Prevention, National Center for Health Statistics. NHANES
2017–2018 questionnaires, datasets, and related documentation. https://wwwn.cdc.gov/nchs/
nhanes/continuousnhanes/default.aspx?BeginYear=2017, 2020. Accessed: 2026-05-03.
[39] National Cancer Institute Genomic Data Commons. TCGA-LIHC: Liver hepatocellular carci-
noma clinical metadata. https://portal.gdc.cancer.gov/projects/TCGA-LIHC, 2026. Accessed:
2026-05-03.
13

A Appendix Roadmap, Navigation, and Main-Paper Coverage
The appendix contains both claim-support material for the main paper and standalone audit material
that is not fully described in the main text. Table 10 gives a complete section-level map of the
supplement. Table 11 then maps main-paper claims to their most relevant supporting material.
Table 10: Complete appendix navigation. The map covers all supplement sections, including audit
and interface material that is not tied to a specific main-paper table or figure.
Appendix section Contents Purpose in the supplement
App. A Roadmap, complete navigation, and main-paper
crosswalk.
Orients readers to both the full supplement and the subset of mate-
rial that directly supports main-paper claims.
App. B HCC benchmark scope, release boundary, task
construction, Public-RWS-18, claim policies, and
worksheet inventory.
Documents the datasets, task instances, and schema constraints
needed to reproduce or audit the benchmark.
App. C Profile schema, concrete profile instance, RWS-
IR checks, evidence certificates, validators, arti-
fact bundle, coding harness, and DAG reporting.
Specifies the executable contract objects and implementation
checks behind ProCARE.
App. D Execution environment, cost accounting, baseline
adaptation, scaffolded fairness controls, ablations,
model access, and repository commands.
Records experimental controls and reproducibility details.
App. E Claim-diagnostic interpretation and backbone-
sensitivity interpretation.
Explains claim-policy downgrades and performance differences
across backbones.
App. F Dashboard, profile panel, RWS-IR view, coding
loop, report review, and section-wise report gen-
eration screenshots.
Supplies workflow/interface evidence showing where artifacts,
traces, logs, and evidence-linked report sections are inspected.
App. G Metric definitions, deterministic validator rules,
LLM judge protocol, expert-review protocol, raw
expert-data schema, reliability, and rubric an-
chors.
Defines how automated and human evaluation scores are produced
and audited.
App. H Benchmark, IR compiler, coding harness, re-
port/certificate, and judge prompt templates.
Makes the generation and scoring prompts inspectable.
App. I Data release, privacy, responsible-use caveats,
and deployment limits.
Clarifies the de-identified HCC release, public-data sources, and
how the system should be interpreted.
Table 11: Main-paper claims and corresponding supplementary support. This crosswalk is not the
full appendix map; complete section navigation is provided in Table 10.
Main-paper location Claim or reference Supplementary support
Sec. 3.1 The heterogeneous profile records structural and
knowledge-driven constraints, with a concrete seri-
alization and de-identified profile instance.
App. C.1 and App. C.2.
Sec. 3.2 RWS-IR compilation and execution enforce schema,
semantic-role, temporal, grain, method, and artifact
constraints.
App. C.3, App. C.5, and App. C.10.
Sec. 3.3 Evidence certificates and claim policies gate factual
report claims, while a DAG orders supported report
sections.
App. C.6, App. C.9, and App. C.11.
Sec. 4 The primary benchmark contains 36 HCC tasks over
four objectives and a 54-sheet longitudinal eCRF
workbook.
App. B and Table 23.
Sec. 4–5 Public-RWS-18 uses three public datasets, dataset-
specific claim policies, and the same validators and
rubrics.
App. B.6.
Main Table 3 LLM-agent, table-analysis, and code-agent base-
lines are evaluated under a unified prompt, budget,
artifact contract, and post-hoc checker.
App. D.2.
Main Table 5 Ablations remove one contract mechanism at a time
while keeping the rest of the workflow fixed when
defined.
App. D.4.
Main Table 6 Claim diagnostics are computed over factual report
claims with trace and policy checks.
App. E.1.
Main Table 7 Automated metrics are compared with expert review. App. G.4.
Main Figure 2 Stage-wise performance varies by objective and
prompt specificity.
App. B and App. G.
Main Table 9 and Sec. 5.2 Backbone sensitivity uses fixed workflow compo-
nents; model metadata and amortized token cost are
reported.
App. D.5 and App. D.1.
14

Table 12: HCC benchmark release contents and privacy treatment.
Release item Included material Privacy and reproducibility treatment
De-identified HCC ta-
bles
54 linked eCRF sheets cover-
ing the 1,294-subject bench-
mark cohort.
Direct participant identifiers are removed; random
benchmark IDs preserve subject-level and visit-level
linkage required for rerunning all tasks.
Task and prompt files The 36 primary HCC bench-
mark prompts and task meta-
data.
Prompts refer only to de-identified table and field
names and do not expose participant identities.
Schema/profile artifacts Field dictionaries, join keys,
temporal roles, missingness
summaries, and profile ob-
jects.
Contains schema and aggregate metadata used by val-
idators; no direct identity fields are present.
Evaluation assets Validators, judge prompts,
artifact templates, scoring
scripts, and expected output
schema.
Enables independent reruns against the released de-
identified tables.
Release metadata Data dictionary, checksums,
and responsible-use terms.
Documents provenance, file integrity, de-identification
scope, and restrictions against re-identification or clin-
ical use.
B Benchmark Datasets and Tasks
This section gives the benchmark details not repeated in the main paper: release contents, worksheet
organization, task instantiation, public-data transfer tasks, and the worksheet inventory used by the
validators.
B.1 Supplemental schema scope
The main paper summarizes the cohort size and high-level eCRF scope. Here we record the schema
properties needed to reproduce profiling and task construction. The workbook is multi-table by
design, spanning enrollment, baseline characterization, time-varying interventions, follow-up, and
survival outcomes; this structure is what drives the join, grain, temporal-anchor, and claim-policy
checks used throughout the benchmark.
B.2 Release boundary and de-identification
The public benchmark release contains the fully de-identified HCC record-level tables used in the 36
primary tasks, together with task specifications, prompt files, schema and profile artifacts, evaluation
scripts, aggregate profile examples, checksums, and a data dictionary. Before release, direct identifiers
and fields that could identify individual participants are removed from the benchmark copy. Random
benchmark subject and visit identifiers are retained only to preserve within-dataset linkage, visit
order, and longitudinal analysis structure. The released tables are intended for reproducibility of the
benchmark and do not constitute a clinical deployment dataset.
B.3 Functional groupings
Table 13 groups worksheets by their role in profiling and benchmark construction.
B.4 Dataset limitations for benchmark design
Several data properties directly shape the benchmark tasks. Adverse-event screening pages are
available, but detailed AE/SAE records are sparse in the released workbook; safety tasks therefore
distinguish screening-level summaries from detailed event-term analyses. The dataset does not
contain direct billing or price fields, so economics-oriented tasks are framed as resource utilization,
follow-up burden, or quality-of-life proxy analyses rather than cost-effectiveness studies.
15

Table 13: Functional worksheet groups used by profiling and benchmark construction.
Group Representative sheets Main contents Use in benchmark/profile
System metadata SYSV AR, ECRF, DATA_RANGE Form catalog, site allocation, variable de-
scriptions, and codebook fields.
Schema parsing, worksheet indexing,
and field-name grounding.
Baseline DM, PH, CP, BCLC, ECOG Demographics, history, liver function,
staging, and performance status.
Cohort definition, baseline table con-
struction, and confounder checks.
Longitudinal labs LB_AFP, LB_BB, LB_BR, LB_TT Tumor markers, biochemistry, complete
blood count, and coagulation tests.
Safety proxy signals and follow-up bur-
den measures.
Treatment TACE, TART, IMU, PATE, CM Procedures, systemic therapy, retreat-
ment, and concomitant medication
records.
Exposure definition, treatment intensity,
and resource-utilization tasks.
Outcomes VT, AE_HQ, SAE_HQ, SF Recurrence and survival proxies,
AE/SAE screening, and quality-of-life
forms.
Endpoint derivation and limitation
checks.
B.5 Benchmark task construction
The benchmark crosses four RWS objectives, three core questions per objective, and three prompt-
specificity levels:
|B|=|O| × |Q| × |L|= 4×3×3 = 36.
Table 14 defines the prompt levels used across all objectives.
For each metric in Main Figure 2, an objective–prompt cell averages the three benchmark instances
for that objective at the specified prompt level. A fixed prompt level therefore contains twelve
instances across the four objectives; the full benchmark contains all 36 instances across the three
levels.
Table 14: Prompt specificity levels in the benchmark.
Level Information provided Expected behavior
GOAL High-level study intent only. Select feasible variables and disclose as-
sumptions.
GOAL+APPROACH Study intent plus an analysis strategy. Follow the strategy when the data support
it; otherwise report the deviation.
GOAL+METHOD Specific variables, time windows, or statis-
tical method.
Stop or report infeasibility when required
data are missing.
All instances use the same output contract: a verification plan, executable analysis entry point,
generated artifacts, and a structured RWS report. Table 15 lists the twelve core questions, and
Tables 16–19 give the corresponding 36 prompts.
B.6 Public-RWS external validation suite
Public-RWS-18 is an external validation suite for testing whether the same profile–IR–certificate
pipeline transfers to public health datasets with different schemas and study designs. It is not merged
with the 36-instance HCC benchmark and is not treated as another full longitudinal RWS benchmark.
Each public dataset contributes two task objectives, and each objective is evaluated under low-,
medium-, and high-specificity prompts.
Public-RWS-18 uses the same profile construction, RWS-IR schema, validators, and claim checker
as the HCC benchmark. Dataset-specific preprocessing is limited to loading the public tables,
normalizing file and column names for stable tool access, preserving original public codebook
variables, and constructing profile metadata. No public dataset receives a custom validator, claim
checker, or reporting rule. The claim policy in Table 22 is the only dataset-specific adaptation,
because each public source supports a different study-design boundary.
Each public dataset contributes two objectives, and each objective is instantiated under three prompt-
specificity levels. Dataset-level results are reported once in the main paper. Public-RWS-18 uses
ReAct as a generic agent baseline and adds two stronger controls aligned with the primary baseline
table: Claude Code as a native code-agent baseline, and Scaffolded G3P as the direct Gemini-3-Pro
profile/template plus validator-repair control. Scaffolded G3P receives evaluator-facing schema
16

Table 15: Core research questions used to instantiate benchmark prompts.
Objective ID Core research question Primary data sources
Cohort C1 Characterize the analyzable HCC cohort, including enrollment,
baseline characteristics, and clinical staging.
CO,DM,IE,SG,BCLC,CP,ECOG
Cohort C2 Assess longitudinal follow-up completeness and data density.CPH_FT , VT, LB_AFP, LB_BB, LB_BR,
ECOG
Cohort C3 Assess data readiness for downstream endpoint analyses.DM , SG, BCLC, CP, ECOG, VT, treatment
sheets
Safety S1 Summarize AE/SAE screening rates and the availability of detailed
event records.
AE_HQ,SAE_HQ,AE,SAE
Safety S2 Describe postoperative laboratory safety signals from liver function,
hematology, and coagulation panels.
LB_BB,LB_BR,LB_TT,SG
Safety S3 Compare safety proxy signals after major treatment exposures.TACE , TART, IMU, PATE, AE_HQ, SAE_HQ,
lab sheets
Efficacy E1 Analyze recurrence and recurrence-free survival proxies after
surgery.
SG,VT,BCLC,CP,ECOG, treatment sheets
Efficacy E2 Analyze overall survival proxies and their relationship to treatment
exposure.
SG, VT, DM, BCLC, CP, ECOG, treatment
sheets
Efficacy E3 Analyze response assessment and longitudinal tumor-marker
changes.
VT,LB_AFP,AFP2,BCLC, treatment sheets
Health economic-
s/resource use
H1 Describe postoperative treatment resource utilization and treatment
intensity.
TACE,TART,IMU,PATE,CM,SG
Health economic-
s/resource use
H2 Estimate follow-up and testing burden as a resource-use proxy.CPH_FT , VT, LB_AFP, LB_BB, LB_BR,
LB_TT,ECOG,SF
Health economic-
s/resource use
H3 Use SF-12 availability and treatment intensity to assess
QoL/resource-use feasibility.
SF,TACE,TART,IMU,PATE,VT
Table 16: Cohort benchmark instances. Suffixes denote prompt specificity: G = GOAL, A =
GOAL+APPROACH, and M = GOAL+METHOD.
ID Prompt text Required or expected evidence
C1-G Characterize the baseline hepatocellular carcinoma cohort avail-
able in the workbook. Deliver a cohort summary suitable for a
real-world study report.
DiscoverDM,SG,BCLC,CP,ECOG, and subject identifiers.
C1-A Characterize the baseline HCC cohort. Build a STROBE-style
cohort table covering demographics, surgery, liver function, tu-
mor stage, and performance status.
Use patient-level baseline records, report missingness, and avoid
duplicate subject counting.
C1-M Produce a baseline cohort table for subjects with valid
Subject_Id. Join DM, SG, BCLC, CP, and baseline ECOG; summa-
rize AGE, SEX, HEIGHT, WEIGHT, SGDAT, SGTYP, BCLC, CPRES,
CPGRA, andECOG.
Use one baseline row per subject; report variable-level missing-
ness; do not impute incompleteAGE.
C2-G Assess whether the dataset has sufficient longitudinal follow-up
for real-world evidence generation.
Identify visit-level forms and repeated measurements.
C2-A Assess longitudinal follow-up completeness across follow-up
forms, laboratory panels, tumor-marker tests, ECOG assessments,
and efficacy follow-up records.
Use CPH_FT, VT, laboratory sheets, and ECOG; produce visit-level
summaries.
C2-M Quantify longitudinal data completeness using CPH_FT, VT,
LB_AFP, LB_BB, LB_BR, and ECOG; count distinct visits by
Subject_Id, tabulate availability by Visit_No, and estimate
follow-up duration from SG.SGDAT to the latest VT.VTDAT1 or
VT.VTDAT2.
Use Subject_Id and Visit_No; report subjects with no valid
follow-up date.
C3-G Evaluate whether the cohort is fit for downstream RWS endpoint
analyses.
Reason about exposure, outcome, confounder, and time-anchor
variables.
C3-A Evaluate endpoint-analysis readiness through a feasibility ma-
trix covering identifiers, surgery date, treatment exposure, recur-
rence/death endpoints, and baseline confounders.
Include data limitations, not only descriptive counts.
C3-M Build a data-readiness matrix by checking Subject_Id,
SG.SGDAT, recurrence dates VT.PADHDAT/VT.PADRDAT, death
dates VT.DEDAT1/VT.DEDAT2, treatments from TACE, TART,
IMU, PATE, and confounders DM.SEX, DM.AGE, BCLC.BCLC,
CP.CPGRA,ECOG.ECOG.
Flag sparse or unavailable fields, especially VT.DEDAT2; do not
invent endpoint fields.
17

Table 17: Safety benchmark instances.
ID Prompt text Required or expected evidence
S1-G Analyze the adverse-event and serious-adverse-event safety pro-
file in the cohort.
Discover that AE/SAE screening pages exist but detailed event
tables are empty in the current workbook.
S1-A Analyze AE and SAE safety reporting. Start with screening
pages, then check whether detailed AE/SAE records are available
for term, onset date, severity, causality, outcome, and seriousness.
Document infeasibility of detailed AE/SAE term analysis when
detail tables have no valid records.
S1-M Summarize AE/SAE reporting completeness using AE_HQ.AEYN
and SAE_HQ.SAEYN; inspect AE.AETERM, AE.AESTDAT,
AE.AESEV, AE.AEREL, AE.AESAE, SAE.SAESTDAT, and
SAE.SAESEV.
Compute screening prevalence by subject; terminate detail-level
analysis ifAEandSAEcontain zero valid records.
S2-G Identify laboratory safety signals after surgery. Use longitudinal laboratory sheets rather than relying only on AE
tables.
S2-A Identify post-surgical laboratory safety signals by summarizing
liver function, hematology, and coagulation markers over follow-
up visits.
Use lab value/result-judgment pairs and visit dates; report
abnormal-result flags when available.
S2-M Generate a post-surgical laboratory safety profile anchored at
SG.SGDAT; use LB_BB.LBBBDAT, ALTRES, ASTRES, TBILRES,
ALBRES; LB_BR.BRDAT, WBCRES, HBRES, PLTRES; and
LB_TT.LBTTDAT,PTRES,INRRES,DDIMRES.
Summarize baseline and postoperative windows; use available-
case denominators and _SIG flags when numeric thresholds are
unavailable.
S3-G Compare safety patterns across major postoperative treatment
exposures.
Identify TACE, targeted therapy, immunotherapy, and retreatment
exposure sheets.
S3-A Compare safety proxy signals by treatment exposure using TACE,
targeted therapy, immunotherapy, and postoperative retreatment
groups.
Compare AE/SAE screening and laboratory abnormalities de-
scriptively; avoid causal claims.
S3-M Compare treatment-associated safety proxies using exposure in-
dicators from TACE.TACEDAT, TART.TARSDAT, IMU.IMUSDAT,
and PATE.PATEYN; calculate screening rates from AE_HQ.AEYN
and SAE_HQ.SAEYN; summarize post-exposure laboratory sig-
nals fromLB_BB,LB_BR, andLB_TT.
Report confounder imbalance using BCLC.BCLC, CP.CPGRA, and
ECOG.ECOG; frame results as descriptive safety proxies.
Table 18: Efficacy benchmark instances.
ID Prompt text Required or expected evidence
E1-G Analyze recurrence-related outcomes after surgery. Locate surgery dates and recurrence dates inVT.
E1-A Analyze recurrence-free outcomes using surgery date as time
origin, recurrence events from follow-up records, and clinically
relevant baseline risk strata.
Handle multiple follow-up visits and competing or missing dates.
E1-M Estimate recurrence-free survival proxies using SG.SGDAT as
index date; define recurrence as the earliest non-missing
VT.PADHDAT or VT.PADRDAT; censor at latest VT.VTDAT1 or
VT.VTDAT2; stratify by BCLC.BCLC, CP.CPGRA, and exposure
fromTACE,TART,IMU, orPATE.
Use earliest valid recurrence date and valid time ordering; gener-
ate Kaplan–Meier curves only when dates are sufficient.
E2-G Analyze overall survival patterns in the cohort. Identify death dates and follow-up dates.
E2-A Analyze overall survival by deriving time from surgery to death
or last follow-up and comparing clinically meaningful strata.
Use DEDAT1/DEDAT2 and VT follow-up dates; disclose death-date
limitations.
E2-M Estimate overall-survival proxies using SG.SGDAT as index
date; define death date as earliest non-missing VT.DEDAT1 or
VT.DEDAT2; censor at latest valid VT.VTDAT1 or VT.VTDAT2;
compare treatment exposures and adjust or stratify descriptively
by DM.SEX, DM.AGE, BCLC.BCLC, CP.CPGRA, and ECOG.ECOG
when available.
Note that DEDAT2 is unavailable in the current data; avoid over-
adjusted models when events are limited.
E3-G Evaluate treatment response and tumor-marker dynamics over
follow-up.
Combine efficacy assessment and biomarker sheets.
E3-A Evaluate response and tumor-marker dynamics by summarizing
hospital/telephone efficacy evaluations and longitudinal AFP,
CA199, and DCP trajectories by visit and exposure.
Combine categorical response information with biomarker trends.
E3-M Analyze response and tumor-marker trends using VT.CEVYN,
VT.CUEV, VT.VTDAT1, VT.VTDAT2, plus LB_AFP.LBAFPDAT,
AFPRES, CA199RES, and DCPRES; align measurements by
Subject_Id and date relative to SG.SGDAT; summarize trajec-
tories by exposure toTACE,TART, orIMU.
If formal response criteria are not encoded, report observed cate-
gories and marker changes without RECIST claims.
18

Table 19: Health economics and resource-use benchmark instances.
ID Prompt text Required or expected evidence
H1-G Analyze postoperative treatment resource utilization in the cohort. Recognize that the task concerns utilization rather than direct
cost.
H1-A Analyze postoperative treatment resource utilization by quantify-
ing use and timing of TACE, targeted therapy, immunotherapy,
postoperative retreatment, and concomitant medications.
Use procedure and drug counts with dates as utilization proxies.
H1-M Quantify treatment-utilization intensity by deriving per-
subject counts and time-to-first-use for TACE.TACEDAT,
TART.TARSDAT, IMU.IMUSDAT, PATE.PATEYN/PATETR*, and
CM.CMCAT/CMSTDAT; summarize utilization distributions and
stratify byBCLC.BCLCand recurrence status when feasible.
Explicitly state that no direct cost or billing variables are present.
H2-G Estimate follow-up and testing burden associated with the RWS
cohort.
Use visit and form/test counts as burden proxies.
H2-A Estimate follow-up and testing burden by counting follow-up vis-
its, efficacy assessments, laboratory panels, tumor-marker checks,
coagulation tests, ECOG assessments, and QoL forms per patient.
Summarize burden by patient and visit.
H2-M Build a follow-up resource-burden profile by counting records
in CPH_FT, VT, LB_AFP, LB_BB, LB_BR, LB_TT, ECOG, and SF;
compute total follow-up forms/tests, median counts per sub-
ject, and distribution by Visit_No; use SG.SGDAT and latest
VT.VTDAT1/VT.VTDAT2to contextualize burden over time.
Frame the result as utilization burden, not economic cost.
H3-G Explore quality-of-life evidence and its relationship to treatment
burden.
Discover SF-12 sparsity and avoid overclaiming.
H3-A Explore QoL and treatment burden using SF-12 items when
available; summarize missingness and compare available QoL
responses across treatment-utilization groups.
Emphasize sparse SF item completeness.
H3-M Analyze QoL/resource-use proxy feasibility by inspecting
SF.SFYN and SF1–SF12; compute complete-item availability;
when enough records exist, summarize item-level or total scores
by exposure groups from TACE, TART, IMU, and PATE; otherwise
report feasibility and missingness only.
Terminate formal QoL comparison when usable SF-12 item
records are too sparse.
Table 20: Public-RWS external validation datasets. These datasets test cross-dataset transfer and
contract diagnostics, not additional full HCC-style longitudinal RWS validity.
Dataset Structure Task focus Boundary
UCI Diabetes 130-
US Hospitals
101,766 encounters, 50
columns; the department-
split workbook is used only
as a sheet-navigation vari-
ant.
Readmission proxy, medication
process, utilization, coded vari-
ables, missingness.
Encounter-level data
with limited longitudinal
structure.
NHANES 2017–
2018 subset
10 linked XPT/CSV tables
with 3,036–19,643 rows
per table, linked bySEQN.
Survey cohort construction, labs,
medications, conditions, demo-
graphic covariates.
Cross-sectional survey
data, not EHR.
TCGA-LIHC clini-
cal metadata
377 cases, 137 clinical
metadata columns.
HCC metadata, vital status, treat-
ment fields, follow-up proxy
fields.
Cancer registry-like
clinical metadata, not
routine-care EHR.
information, artifact templates, validator feedback, and the same repair budget, but not ProCARE’s IR
compiler, certificate admission gate, certified reporting DAG, or internal planner state. This appendix
records the dataset boundaries, task objectives, claim policies, and prompt text needed to rerun the
transfer suite. For baselines without explicit evidence certificates, CTC, UCR, and CLV are computed
by post-hoc evidence reconstruction over submitted artifacts and reports.
Listing 1: Prompt set for Public-RWS-18.
UCI Diabetes -- Objective U1: Readmission proxy profiling
Low: Analyze the diabetes hospital encounter data and identify which patient groups appear
to have higher readmission burden.
Medium: Using the readmitted field as a proxy outcome, summarize early-readmission patterns
by age, admission type, discharge disposition, and prior utilization variables.
High: Using readmitted = "<30" as the early-readmission proxy outcome, compute
subgroup-level rates by age band, admission_type_id, discharge_disposition_id,
number_inpatient, and number_emergency. Produce a table, one figure, and a report
restricted to descriptive or proxy-association claims with evidence certificates for
all factual statements.
19

Table 21: Task objectives in Public-RWS-18. Each objective is evaluated under low-, medium-, and
high-specificity prompts.
Dataset Objective Contract stressor
UCI Diabetes Readmission proxy profiling Outcome binding, coded variables, missingness, con-
servative claim scope.
UCI Diabetes Medication and utilization analy-
sis
Exposure/proxy roles, subgroup aggregation, artifact
traceability.
NHANES Diabetes/cardiometabolic cohort
analysis
Multi-table joins by SEQN, lab-defined variables,
survey-table grounding.
NHANES Medication and condition associ-
ation analysis
Questionnaire, laboratory, and prescription-
medication grounding under a cross-sectional
claim policy.
TCGA-LIHC HCC case and vital-status profil-
ing
Domain transfer, oncology metadata grounding, miss-
ingness disclosure.
TCGA-LIHC Treatment/follow-up metadata
analysis
Sparse fields, proxy endpoint handling, limitation re-
porting.
Table 22: Dataset-specific claim policies for Public-RWS-18.
Dataset Allowed claims Forbidden claims
UCI Diabetes Descriptive and readmission-proxy associa-
tion claims.
Causal treatment effect, safety conclusion,
longitudinal endpoint claim.
NHANES Descriptive and cross-sectional association
claims.
Temporal effect, incidence claim, causal ef-
fect.
TCGA-LIHC Descriptive oncology metadata and follow-
up-proxy claims.
Treatment efficacy, causal survival effect,
routine-care EHR claim.
UCI Diabetes -- Objective U2: Medication and utilization analysis
Low: Analyze whether medication and hospital-utilization patterns differ across diabetes
encounters.
Medium: Summarize insulin, change, diabetesMed, A1Cresult, time_in_hospital,
num_lab_procedures, num_medications, and num_procedures, and describe any supported
association with readmitted.
High: Compute utilization summaries for time_in_hospital, num_lab_procedures,
num_medications, and num_procedures stratified by insulin, change, and diabetesMed.
Compare early-readmission proxy rates across medication-process groups, and avoid
causal treatment-effect language.
NHANES -- Objective N1: Diabetes/cardiometabolic cohort analysis
Low: Use the NHANES tables to profile diabetes and cardiometabolic risk patterns in the
population sample.
Medium: Join demographics, examination, blood pressure, diabetes questionnaire, laboratory,
and medical-condition tables by SEQN. Summarize diabetes-related variables and
cardiometabolic measurements by age and sex.
High: Construct a cross-sectional NHANES cohort using SEQN-linked tables. Define
diabetes-related status using supported questionnaire or laboratory fields, summarize
blood pressure and relevant laboratory measures by demographic subgroup, and report
only descriptive or cross-sectional association claims.
NHANES -- Objective N2: Medication and condition association analysis
Low: Analyze how prescription medication records relate to self-reported medical conditions
in NHANES.
Medium: Join prescription medication, medical conditions, demographics, and laboratory
tables by SEQN. Summarize medication exposure groups and compare supported condition or
laboratory profiles.
High: Using SEQN-linked medication and condition tables, construct medication-exposure
groups when supported by the codebooks, summarize condition prevalence and laboratory
measurements, and produce a report that explicitly states cross-sectional design
limitations.
20

TCGA-LIHC -- Objective T1: HCC case and vital-status profiling
Low: Profile the TCGA-LIHC clinical metadata and summarize major patient, diagnosis, and
vital-status patterns.
Medium: Summarize demographics, diagnosis-related fields, vital status, and available
follow-up-related fields in TCGA-LIHC. Identify missingness and fields that can support
survival-proxy reporting.
High: Using TCGA-LIHC clinical metadata, produce a case-profile table covering age, sex,
diagnosis-related fields, vital status, days-to-death or follow-up-related fields when
available, and missingness. Report only descriptive oncology-metadata claims with
evidence certificates.
TCGA-LIHC -- Objective T2: Treatment/follow-up metadata analysis
Low: Analyze whether available treatment and follow-up metadata in TCGA-LIHC support
subgroup comparisons.
Medium: Identify treatment-related, diagnosis-related, and follow-up-related fields in
TCGA-LIHC, assess their completeness, and perform only comparisons supported by valid
profile entries.
High: Using TCGA-LIHC clinical metadata, identify valid treatment-related and
follow-up-related fields, summarize completeness by subgroup, and generate a
conservative report that distinguishes observed metadata patterns from treatment-effect
or causal claims.
B.7 Worksheet inventory
Table 23: Standardized worksheet inventory in the Excel dataset.
Prefix#Fields #Rows Sheet Description Differential field examples
SYSVAR2 27 System variables and metadata.Variable,Description
DATA_RANGE2 4 Data range / center mapping and alloca-
tion notes.
Center,RangeCode
ECRF8 54 eCRF form catalog and design attributes. FormCode, FormName,
FormType
CPH_FT22 11614 Header/footer records for visit-/form-
level.
VISTNM,SITNO,SUBNO
CO21 1296 Study cover page and subject identifica-
tion fields.
SITENO,SUBJNO,SUBINI
DS19 1296 Informed consent date and related track-
ing fields.
DSDAT
DM27 1295 Demographics and baseline characteris-
tics.
SEX,BRTHDAT,AGE
PH123 1262 Medical history and prior conditions.PHSMYN,SMNUM,SMYER
PH1123 1 Medical history (continuation / overflow
record).
PH1SMYN,SMNUM1,SMYER1
HBCV49 4282 HBV/HCV-related laboratory assess-
ments.
HBVYN,HBVDAT,HBSAGRES
HBCV149 1 HBV/HCV laboratory assessments.HBV1YN,HBV1DAT,HBSAGRE1
VS25 1233 Vital signs measurements.VSRES,VSTEMP,VSSBP
CP32 1262 Child-Pugh assessment and component
scoring.
CPYN,CPRES,CPGRA
IE31 549 Eligibility criteria assessment.IEDAT,INCL1,INCL2
IE130 714 Eligibility criteria (alternate set)..INCL01,INCL02,EXCL01
TUBA94 1295 Intraoperative tumor pathology / surgical
findings.
TUBADSC,TUBATYPE,TUBAGRA
BCLC28 1261 BCLC staging for primary liver cancer.BCLC,PLICA,PLICA1
BCLC128 1 BCLC staging (continuation record).BCLC1,BCPLICA,BCPLICA1
VT96 5321 Efficacy assessment interview and
follow-up.
VTTYP,VTDAT1,VTDAT2
VT196 2 Efficacy assessment (continuation
record).
VT1TYP,VT1DAT1,VT1DAT2
LB_AFP57 4613 Tumor marker laboratory tests.AFPYN,LBAFPDAT,AFPRES
AFP226 4166 Other tumor marker laboratory tests.AFP2DAT,AFP2NM,AFP2RES
LB_CD87 4392 Lymphocyte subset testing panel.CDYN,CDDAT,CD3PRES
LB_BR93 4474 Complete blood count (CBC).BRYN,BRDAT,WBCRES
21

Table 23: Standardized worksheet inventory in the Excel dataset (continued).
Prefix#Fields #Rows Sheet Description Differential field examples
LB_BB123 4583 Serum biochemistry and hepatic func-
tion panel.
LBBBYN,LBBBDAT,ALTRES
LB_BB1105 1 Serum biochemistry.LBBB1YN,LBBB1DAT,ALTRES1
LB_CYT75 4325 Cytokine testing panel.LBCYTYN,LBCYTDAT,IL1RES
LB_TT55 4466 Coagulation function testing panel.LBTTYN,LBTTDAT,PTRES
ECOG22 4459 ECOG performance status assessment.ECOGYN,ECOG
PATE39 3265 Postoperative retreatment information.PATEYN,PATETR1,PATETR2
SG21 1325 Surgery-related records and key at-
tributes.
SGDAT,SGTYP
RFT75 1323 Combined radiofrequency therapy
records.
UEXYN,UEXLO1,UEXLO2
FIN20 1325 Number of lesions and summary lesion
count.
FINM
FI74 1489 Lesion-level details (location and char-
acteristics).
FILO1,FILO2,FILO3
TRDAT20 27 Postoperative treatment start date/time
fields.
TRDAT,TRDATS
THET_HQ23 123 Chemotherapy screening / question
page.
THETYN,THETDSC,THETUK
THET30 154 Chemotherapy administration records.THETPHA,THESDAT,THETONGO
TART_HQ20 453 Targeted therapy screening / question
page.
TARTYN,TARTYN_DEC
TART35 303 Targeted therapy administration records. TARTPHA,TARSDAT,TARTONGO
IMU_HQ20 404 Immunotherapy screening / question
page.
IMUYN,IMUYN_DEC
IMU35 290 Immunotherapy administration records.IMUPHA,IMUSDAT,IMUONGO
TACE_HQ20 615 TACE screening / question page.TACEYN,TACEYN_DEC
TACE30 609 TACE procedure and regimen details.TACEDAT , TACETYP1,
TACETYP2
CMED20 283 Traditional Chinese medicine treatment
records.
CMEDYN,CMEDYN_DEC
RADI_HQ52 15 Radiotherapy screening / question page. RADIYN,RADIMD1,RADIMD2
RADI21 6 Radiotherapy administration records.RADIGN,RADIDAT,RADIDSC
SF44 3183 SF-12 quality-of-life questionnaire.SFYN,SF1,SF2
CM_HQ20 1235 Concomitant medication screening /
question.
CMYN,CMYN_DEC
CM34 6632 Concomitant medication records.CMCAT,CMINDC,CMDOSE
LB_BP24 1232 Blood typing and related laboratory an-
notations.
LBBPYN,LBBPDAT,LBBPSIG
AE_HQ20 1231 Adverse event screening / question page. AEYN,AEYN_DEC
AE34 1 Adverse event records.AETERM,AESTDAT,AEENDAT
SAE74 1 Serious adverse event records and site
contact.
SAECAT1,SAECAT2,SAERPDAT
SAE_HQ20 1231 Serious adverse event screening / ques-
tion page.
SAEYN,SAEYN_DEC
LOAB_HQ20 51 Local ablation screening / question page. LOABYN,LOABYN_DEC
LOAB21 51 Local ablation procedure records.LOABDAT , LOABMEAR,
LOABMEAR_DEC
C Method and Contract Implementation Details
This section records the implementation artifacts used by the profiling, RWS-IR compilation, violation-
guided execution, and certified reporting stages.
C.1 Profile schemaΦ
The main paper defines the four profile blocks. The implementation stores the same object as a JSON
contract with stable keys for high-level structural summaries, high-level knowledge roles, field-level
22

structural statistics, and field-level knowledge mappings. Downstream stages do not consume free-
form profile prose; they read these keys directly when compiling RWS-IR fields, validating generated
code, and admitting report claims.
Structural profile Φ·,S.For each table/sheet and column, we record deterministic statistics, includ-
ing: inferred type, missingness, cardinality, value ranges, common categories, and candidate join
keys.
Knowledge profileΦ ·,K.We map raw fields to standardized biomedical concepts (e.g., UMLS/S-
NOMED CT/ICD/LOINC) by candidate generation followed by deterministic validation checks: (i)
semantic type compatibility, and (ii)value-range consistency. Unmappable or ambiguous fields are
retained with flags to propagate uncertainty into RWS-IR compilation, execution, and reporting.
Implementation serialization and fallback.The implementation serializes Φ as a JSON ob-
ject with four named blocks: high_structural, low_structural, high_knowledge, and
low_knowledge. The high-structural block stores dataset-level table relationships, candidate subject
and visit keys, and worksheet-level roles. The low-structural block stores field-level type inference,
missingness, cardinality, range checks, common categorical values, date-parsing status, and candidate
temporal anchors. The high-knowledge block stores study-level roles, including index-date schema,
exposure, outcome, censoring, confounder, proxy, and claim-scope roles. The low-knowledge block
stores ontology candidates, accepted mappings, validation status, units, value-range plausibility,
temporal-role compatibility, and ambiguity or rejection causes.
For each biomedical mapping candidate, the profiler applies semantic-type compatibility, unit con-
sistency, value-range plausibility, and temporal-role compatibility checks. A field that fails these
checks is retained in ΦL,K with a failure tag rather than removed. Such fields remain available
for structure-grounded summaries, missingness reporting, and data-quality diagnostics, but cannot
authorize clinical-role binding, endpoint derivation, safety conclusions, causal claims, or high-stakes
report language unless an explicit proxy assumption is recorded in the RWS-IR and admitted by the
claim policy.
C.2 Concrete heterogeneous profile instance
Listing 2 shows a compact de-identified JSON instance of Φ from the HCC benchmark. The example
follows the same schema used by the implementation and contains aggregate profile statistics and
field-level metadata; record-level values are provided in the released de-identified HCC tables rather
than repeated in the text.
Listing 2: Compact JSON instance of the heterogeneous data profileΦ.
1{
2" s e r i a l i z a t i o n " : " JSON " ,
3" n o t a t i o n _ m a p " : {
4" Phi ^{ H , S } " : " h e t e r o g e n e o u s _ p r o f i l e . h i g h _ s t r u c t u r a l " ,
5" Phi ^{ L , S } " : " h e t e r o g e n e o u s _ p r o f i l e . l o w _ s t r u c t u r a l " ,
6" Phi ^{ H , K } " : " h e t e r o g e n e o u s _ p r o f i l e . h i g h _ k n o w l e d g e " ,
7" Phi ^{ L , K } " : " h e t e r o g e n e o u s _ p r o f i l e . l o w _ k n o w l e d g e "
8} ,
9" h e t e r o g e n e o u s _ p r o f i l e " : {
10" h i g h _ s t r u c t u r a l " : {
11" d a t a s e t _ s u m m a r y " : {
12" w o r k b o o k _ t y p e " : " multi - sheet eCRF wo rkb oo k " ,
13" b e n c h m a r k _ s u b j e c t _ c o u n t " : 1 2 9 4 ,
14" b e n c h m a r k _ v i s i t _ c o u n t " : 1 2 8 4 7
15} ,
16" s h e e t _ i n v e n t o r y _ s u b s e t " : [
17{
18" sheet " : " DM - - D e m o g r a p h i c s " ,
19" role " : " ba sel in e d e m o g r a p h i c s " ,
20" e s t i m a t e d _ d a t a _ r o w s " : 1 2 9 4 ,
21" columns " : 2 7 ,
22" j o i n _ k e y s " : [ " S u b j e c t _ I d " ]
23} ,
24{
25" sheet " : " SG - - Surgery " ,
26" role " : " index surgery " ,
27" e s t i m a t e d _ d a t a _ r o w s " : 1 3 2 4 ,
28" columns " : 2 1 ,
23

29" j o i n _ k e y s " : [ " S u b j e c t _ I d " ]
30} ,
31{
32" sheet " : " VT - - Follow - up " ,
33" role " : " p o s t o p e r a t i v e follow - up " ,
34" e s t i m a t e d _ d a t a _ r o w s " : 5 3 2 0 ,
35" columns " : 9 6 ,
36" j o i n _ k e y s " : [ " S u b j e c t _ I d " , " Vi si t_N o " ]
37}
38] ,
39" r e l a t i o n s h i p _ h i n t s " : [
40" DM . S u b j e c t _ I d joins SG . S u b j e c t _ I d and VT . S u b j e c t _ I d . " ,
41" SG . SGDAT is the p r e f e r r e d index date . " ,
42" VT . Vis it _N o encodes re pe at ed follow - up windows . "
43]
44} ,
45" l o w _ s t r u c t u r a l " : {
46" f i e l d _ p r o f i l e s " : {
47" DM . SEX_DEC " : {
48" dtype " : " c a t e g o r i c a l " ,
49" m i s s i n g _ r a t e " : 0 . 0 ,
50" t o p _ v a l u e s " : { " male " : 1 6 5 , " female " : 3 4 }
51} ,
52" SG . SGDAT " : {
53" dtype " : " date - like text " ,
54" m i s s i n g _ r a t e " : 0 . 0 0 5 ,
55" s e m a n t i c _ h i n t " : " index surgery date "
56} ,
57" VT . PADHDAT " : {
58" dtype " : " partial date - like c a t e g o r i c a l " ,
59" m i s s i n g _ r a t e " : 0 . 9 1 5 ,
60" q u a l i t y _ n o t e " : " sparse r e c u r r e n c e date "
61} ,
62" VT . DEDAT2 " : {
63" dtype " : " date - like c a t e g o r i c a l " ,
64" m i s s i n g _ r a t e " : 0 . 9 9 5 ,
65" q u a l i t y _ n o t e " : " nearly u n a v a i l a b l e "
66}
67}
68} ,
69" h i g h _ k n o w l e d g e " : {
70" v a r i a b l e _ r o l e s " : {
71" id " : [ " DM . S u b j e c t _ I d " , " SG . S u b j e c t _ I d " , " VT . S u b j e c t _ I d " ] ,
72" t i m e _ a n c h o r " : [ " SG . SGDAT " ] ,
73" b a s e l i n e _ c o v a r i a t e " : [
74" DM . AGE " , " DM . SEX_DEC " , " BCLC . BC LC _D EC " ,
75" CP . CPGRA " , " ECOG . ECOG "
76] ,
77" outcome " : [
78" VT . PADHDAT " , " VT . PADRDAT " ,
79" VT . DEDAT1 " , " VT . DEDAT2 "
80]
81} ,
82" f e a s i b i l i t y _ a s s e s s m e n t " : " Cohort and follow - up s u m m a r i e s are f eas ib le ; su rv iva l
a nal ys es require an a v a i l a b i l i t y check . "
83} ,
84" l o w _ k n o w l e d g e " : {
85" o n t o l o g y _ m a p p i n g " : {
86" DM . SEX_DEC " : " B i o l o g i c a l sex " ,
87" DM . AGE " : " Age " ,
88" SG . SGDAT " : " Su rg ic al p r o c e d u r e date " ,
89" VT . PADHDAT " : " R e c u r r e n c e date "
90} ,
91" v a l i d a t i o n _ s t a t u s " : {
92" DM . HEIGHT " : " a m b i g u o u s : numeric values mixed with unknown tokens " ,
93" VT . PADHDAT " : " v a l i d _ b u t _ s p a r s e " ,
94" VT . DEDAT2 " : " i n v a l i d _ f o r _ p r i m a r y _ s u r v i v a l _ e n d p o i n t "
95} ,
96" a n a l y s i s _ c o n s t r a i n t s " : [
97" Use only fields listed in f i e l d _ p r o f i l e s . " ,
98" Treat unknown or partial date tokens as missing unless the method sup po rt s
in te rv al c e n s o r i n g . " ,
99" Do not infer r e c u r r e n c e or death ou tc ome s from missing date fields . "
100]
101} ,
102" a m b i g u i t y _ f l a g s " : [
103" DM . HEIGHT " , " DM . WEIGHT " ,
104" VT . PADHDAT " , " VT . DEDAT2 "
105]
106}
107}
24

Table 24: Machine-readable fields in the RWS-IR and static checks before execution.
Symbol Serialized key Contents Static admissibility checks
Dstudy_design Study type, estimand boundary, and whether the
requested output is descriptive, associative, or
inferential.
Must be compatible with available tables, ob-
served design, and claim policy.
Ganalysis_grain Subject-, visit-, encounter-, field-, or record-level
analysis unit.
Must match key multiplicities and downstream
aggregation.
Jjoin_graph Tables, join keys, cardinalities, and permitted join
paths.
All tables and keys must exist in ΦL,S; declared
cardinality must match profiled relationships.
Kentity_keys Subject, visit, encounter, treatment, and artifact
identifiers.
Required keys must be present and nondegenerate
under the declared grain.
Ttemporal_anchors Index date, event dates, censoring dates, win-
dows, and ordering rules.
Date fields must be parseable or declared as par-
tial/proxy dates; impossible orderings are disal-
lowed.
Vvariable_roles Exposure, outcome, censoring, covariate, sub-
group, proxy, and reporting variables.
Clinical roles must be supported by ΦL,K, a
validated proxy flag, or a recorded assumption.
Mmethod Statistical method, fallback method, denomina-
tors, missingness policy, and diagnostics.
Method must be compatible with design, grain,
variable support, and minimum data require-
ments.
Arequired_artifacts Required result tables, figures, manifests, logs,
and report sections.
Artifacts must be executable in the sandbox and
verifiable by manifests.
Πq claim_policy Allowed and forbidden claim types, language
constraints, and support levels.
Claim policy must be no stronger than the design
and evidence support.
Table 25: Static violation types emitted byIRCheckstatic.
Violation type Trigger Allowed repair
Missing schema reference A table, field, or key inZ 0 is absent fromΦ L,S. Replace with a profiled field, remove the variable, or
declare infeasibility for GOAL+METHOD.
Unsupported semantic
role
Exposure, endpoint, censoring, or confounder role is not
validated inΦ L,K.
Use a validated proxy with limitation, downgrade to
descriptive support, or stop.
Invalid join or grain Join cardinality or aggregation conflicts with the de-
clared analysis grain.
Change grain, revise the join graph, or aggregate before
merging.
Invalid temporal anchor Index, event, censoring, or follow-up dates are missing,
partial, nonparseable, or ordered incorrectly.
Use a supported anchor, restrict to analyzable records,
or report feasibility only.
Method infeasibility The requested method requires unsupported design as-
sumptions, insufficient events, or unavailable covariates.
Switch to a supported fallback method or emit an infea-
sibility statement.
Claim-policy excessΠ q allows causal, safety-critical, economic-cost, or gen-
eralization claims unsupported by the data.
Restrict Πq to descriptive, feasibility, or proxy-
association claims.
C.3 RWS-IR schema and static checks
The RWS-IR is the typed study object validated before code generation. It records the study design,
analysis grain, join graph, entity keys, temporal anchors, variable roles, methods, required artifacts,
and claim policy. Table 24 lists the machine-readable fields and the admission checks applied before
execution.
Given a candidate Z0, IRCheckstatic returns an accepted RWS-IR Z and a set of static violations
Ustatic. A hard violation is any reference to a missing table, missing field, invalid key, unsupported
clinical role, incompatible analysis grain, impossible temporal anchor, method that requires unavail-
able variables, or claim policy exceeding the design. A soft violation is a downgradeable limitation,
such as sparse endpoint support, partial date availability, missing units, or a proxy variable that can
support descriptive but not causal claims. Only Ustatic =∅ enters the execution workspace. When
hard violations remain, ProCARE either repairs the RWS-IR, emits an infeasibility statement, or
downgrades the requested analysis according to prompt specificity.
C.4 RWS-IR and evidence certificate examples
Listing 3 gives a compact RWS-IR instance for a recurrence-free survival task. The example shows
the fields used by the static checker: study design, analysis grain, join graph, temporal anchors,
variable-role bindings, method assumptions, required artifacts, and claim policy.
Listing 3: Compact RWS-IR example for a recurrence-free survival task.
25

1{
2" s t u d y _ d e s i g n " : " r e t r o s p e c t i v e _ c o h o r t " ,
3" a n a l y s i s _ g r a i n " : " subject " ,
4" p o p u l a t i o n " : {
5" s o u r c e _ t a b l e s " : [ " DM " , " SG " , " VT " ] ,
6" s u b j e c t _ k e y " : " S u b j e c t _ I d " ,
7" i n c l u s i o n " : [ " n o n _ m i s s i n g ( DM . S u b j e c t _ I d ) " , " s u r g e r y _ r e c o r d _ e x i s t s ( SG ) " ]
8} ,
9" j o i n _ g r a p h " : [
10{ " left " : " DM . S u b j e c t _ I d " , " right " : " SG . S u b j e c t _ I d " , " type " : " o n e _ t o _ o n e " } ,
11{ " left " : " DM . S u b j e c t _ I d " , " right " : " VT . S u b j e c t _ I d " , " type " : " o n e _ t o _ m a n y " }
12] ,
13" t e m p o r a l _ a n c h o r s " : {
14" i n d e x _ d a t e " : " SG . SGDAT " ,
15" e v e n t _ d a t e _ c a n d i d a t e s " : [ " VT . PADHDAT " , " VT . PADRDAT " ] ,
16" c e n s o r i n g _ d a t e _ c a n d i d a t e s " : [ " VT . VTDAT1 " , " VT . VTDAT2 " ]
17} ,
18" v a r i a b l e _ r o l e s " : {
19" e xp os ur e " : " surgery cohort " ,
20" outcome " : " recurrence - free s ur vi va l proxy " ,
21" c o v a r i a t e s " : [ " DM . AGE " , " DM . SEX_DEC " , " BCLC . BC LC _DE C " , " CP . CPGRA " ]
22} ,
23" method " : {
24" primary " : " Kaplan - Meier summary if te mpo ra l checks pass " ,
25" f al lb ac k " : " d e s c r i p t i v e follow - up a v a i l a b i l i t y when event dates are sparse "
26} ,
27" r e q u i r e d _ a r t i f a c t s " : [ " c o h o r t _ f l o w " , " f o l l o w u p _ s u m m a r y " , "
k m _ c u r v e _ o r _ f e a s i b i l i t y _ t a b l e " ] ,
28" c l a i m _ p o l i c y " : {
29" allowed " : [ " d e s c r i p t i v e " , " a s s o c i a t i o n _ w i t h _ l i m i t a t i o n " ] ,
30" blocked " : [ " c a u s a l _ e f f e c t " , " s a f e t y _ d e t a i l " , " s u b m i s s i o n _ g r a d e _ c l a i m " ]
31}
32}
Listing 4 gives a representative evidence certificate. The certificate records the claim text, its support
level, the validated artifacts and code region that produced it, the RWS-IR fields that authorize the
claim, and the profile entries or assumptions used by the admission rule.
Listing 4: Evidence certificate example for an admitted factual claim.
1{
2" cl aim _i d " : " q_ rf s_0 3 " ,
3" c l a i m _ t e x t " : " Recurrence - free s ur vi va l can be s u m m a r i z e d for su bj ect s with valid
surgery and follow - up dates . " ,
4" c l a i m _ t y p e " : " d e s c r i p t i v e _ f e a s i b i l i t y " ,
5" s u p p o r t _ l e v e l " : " p r o f i l e _ a n d _ a r t i f a c t _ s u p p o r t e d " ,
6" trace " : {
7" a rt if ac t " : " results / f o l l o w u p _ s u m m a r y . json " ,
8" figure " : " figures / k m _ o r _ f e a s i b i l i t y . pdf " ,
9" c o d e _ r e g i o n " : " a na lys is . py :: b u i l d _ r f s _ d a t a s e t " ,
10" r w s _ i r _ f i e l d s " : [
11" t e m p o r a l _ a n c h o r s . i n d e x _ d a t e " ,
12" t e m p o r a l _ a n c h o r s . e v e n t _ d a t e _ c a n d i d a t e s " ,
13" method . primary " ,
14" c l a i m _ p o l i c y . allowed "
15] ,
16" p r o f i l e _ e n t r i e s " : [ " SG . SGDAT " , " VT . PADHDAT " , " VT . PADRDAT " , " VT . VTDAT1 " , " VT . VTDAT2 " ]
,
17" a s s u m p t i o n s " : [ " partial or unknown date tokens are treated as missing " ]
18} ,
19" a d m i s s i o n " : {
20" t r a c e _ c h e c k " : true ,
21" p o l i c y _ c h e c k " : true ,
22" l a n g u a g e _ c h e c k " : true
23}
24}
C.5 Execution validators and violation-guided repair
Execution-time checks are applied after code generation because row-level temporal ordering, mani-
fest completeness, figure creation, and artifact consistency cannot be fully resolved statically. Val-
idators return a localized violation set Ut =V exec(Zt, Ct, Ot, Et,Φ, St). Each violation records the
failed contract clause, offending code or artifact, nearest valid profile entries, severity, and permitted
repair actions. Listing 5 shows the JSON schema used for one violation record.
26

Table 26: Execution validators used before accepting an artifact bundle.
Validator Check Acceptance criterion
Entry-point validator Runsanalysis.pyormain.pyin the sandbox. Exit code is zero and no failure sentinel such as
TASK_FAILEDappears.
Schema validator Parses code and generated outputs for table, field, and key
usage.
Every referenced table, field, join key, and output column
is traceable toΦ L,S or a derived artifact.
Grain and join valida-
tor
Checks duplicate inflation, one-to-many joins, and final
denominator consistency.
Output denominators match the declared analysis grain or
disclose aggregation rules.
Temporal validator Recomputes index, event, censoring, and follow-up win-
dows.
Invalid date strings and impossible orderings are filtered,
logged, or reported as limitations.
Method validator Checks cohort filters, variables, denominators, covariates,
and statistical choices againstZ.M.
Method matches the admitted RWS-IR or a declared fall-
back.
Artifact validator Checks result and figure manifests, file existence, and
generated figure formats.
Required tables, figures, manifests, and logs exist and are
nonempty when applicable.
Claim-preparation val-
idator
Builds the evidence map used by the report generator. Each reportable statistic has a source artifact, producing
code region, and profile/IR trace.
Algorithm 1Execution acceptance and localized repair
Require:Accepted RWS-IRZ, profileΦ, workspace policyΠ, maximum attemptsB
Ensure:Accepted codeC ∗, artifactsO, evidenceE, assumptionsA, or failure trace
1:fort= 1, . . . , Bdo
2:Generate or edit codeC t conditioned onZ,Φ,Π, and prior violationsU t−1.
3:Execute the selected entry point in the sandbox and collect logs, result manifests, and figure manifests.
4:ComputeU t =V exec(Z, Ct, Ot, Et,Φ, St).
5:ifU t =∅then
6:AcceptC ∗ =C t and return(C ∗, Ot, Et, At).
7:else
8:WriteU t toviolation_set.jsonwith localized repair actions.
9:end if
10:end for
11:Return the final failure trace or a supported downgrade with explicit limitations.
Listing 5: Schema for one execution-time contract violation.
1{
2" v i o l a t i o n _ i d " : " u_017 " ,
3" stage " : " e x e c u t i o n " ,
4" c o n t r a c t _ c l a u s e " : " t e m p o r a l _ a n c h o r . i n d e x _ d a t e _ b e f o r e _ e v e n t " ,
5" se ver it y " : " hard " ,
6" o f f e n d i n g _ a r t i f a c t " : " a na ly sis . py " ,
7" c o d e _ r e g i o n " : " b u i l d _ s u r v i v a l _ d a t a s e t " ,
8" o b s e r v e d _ f a i l u r e " : " e v e n t _ d a t e pr ece de s SG . SGDAT for at least one record " ,
9" n e a r e s t _ p r o f i l e _ e n t r i e s " : [ " SG . SGDAT " , " VT . PADHDAT " , " VT . PADRDAT " ] ,
10" p e r m i t t e d _ a c t i o n s " : [ " f i l t e r _ i n v a l i d _ t e m p o r a l _ p a i r s " , " r e p o r t _ t e m p o r a l _ l i m i t a t i o n " ] ,
11" b l o c k s _ a c c e p t a n c e " : true
12}
C.6 Evidence certificates and claim admission
A factual claim is any report sentence that asserts a dataset property, cohort count, variable availability,
statistical result, visualization interpretation, clinical association, feasibility conclusion, or limitation
derived from the data. Section headings, procedural statements, and generic background statements
are not counted unless they contain dataset-specific factual content. For ProCARE, certificates
are emitted during report generation. For baselines without explicit certificates, the same checker
performs post-hoc reconstruction from the submitted code, logs, artifacts, and report.
Each claim q receives a certificate eq =⟨o q, cq, zq, ϕq, aq⟩, where oq is a supporting artifact, cq is the
executed code region that created the artifact, zq is the RWS-IR field or method authorizing the claim,
ϕq is the relevant profile entry, and aq is an optional recorded assumption or limitation. The trace
check passes only when all required links exist and agree on variables, denominators, analysis grain,
temporal windows, and method. The policy check passes only when the claim type and wording are
allowed byZ.Π q at the available support level.
27

Table 27: Claim types used by the certificate gate.
Claim type Allowed support Examples of blocked wording
Descriptive Validated table, count, summary statistic, figure, or pro-
file entry.
Claims that imply generalization beyond the analyzed
cohort.
Feasibility or data-quality Profile entries, missingness summaries, temporal-
validity logs, or execution artifacts.
Treating missingness or feasibility as clinical outcome
evidence.
Proxy association Valid proxy flag, artifact support, and explicit limitation. Causal treatment-effect language or safety conclusion
language.
Causal or comparative ef-
fect
Requires design assumptions, adjustment plan, and
method support declared inZ.
Causal language when only descriptive or proxy support
is available.
Safety-critical or
economic-cost
Requires detailed safety records or direct cost/billing
fields.
Detailed AE/SAE term claims when only screening
pages exist; cost-effectiveness claims without cost vari-
ables.
Table 28: Operational mapping between profile-grounded state roles and implementation artifacts.
State role Stored artifacts Example contents Accessed by
Execution traceexec_logs.json ,
exec_status.json,
opencode_live.log,
violation_set.json, audit records.
execution traces, contract violations,
validation outcomes, disclosed assump-
tions.
violation-guided execution, report gen-
erator, frontend status view.
Working contextexcel_info.json , rws_ir.json,
execution_spec.md, selected sheet
payloads.
selected sheets, required fields, join
keys, variable roles, temporal anchors,
method specification, claim policy.
IR compiler, execution workspace, re-
port context builder.
Profile semanticsΦ H,K, ΦL,K, ontology mappings,
reporting prompts.
exposure/outcome/covariate roles,
plausibility checks, clinical terminol-
ogy, section semantics.
IR compiler, code generator, report
DAG nodes.
Certified outputs result manifests, figure manifests, evi-
dence certificates, report sections, dis-
closed assumptions.
validated tables and figures, claim
traces, support levels, limitations, sec-
tion drafts.
claim checker, report DAG, final report
renderer.
Operational policy IR compilation, profiling, coding, fig-
ure, validation, and report-generation
policies.
coding rules, artifact schemas, figure
manifest schema, section templates,
validation gates, claim policies.
execution workspace, report builder.
Let Nq be the number of extracted factual claims, Cq the number with admitted evidence certificates,
Uq the number without admissible evidence, and Lq the number whose language exceeds the claim
policy. We compute
CTC =C q/Nq,UCR =U q/Nq,CL V =L q/Nq.
A claim can be both unsupported and a language violation, but each metric is normalized by the same
factual-claim denominator. For the claim-diagnostic table in the main paper, metrics are computed per
run and then averaged across the 12 tasks in each prompt-specificity group; the overall row averages
across all 36 HCC tasks.
C.7 Profile-grounded state artifacts
The workflow state is represented by typed JSON artifacts, workspace files, skills, and validation
logs. No vector database is used. Each downstream module reads the relevant state artifact from
named files or typed prompt payloads, so intermediate decisions remain auditable without re-querying
raw tables. Concretely, the persistent dataset state is the cached profile Φ, while the per-job state
St may contain excel_info.json, rws_ir.json, violation_set.json, execution_spec.md,
generated code, execution logs, result manifests, figure manifests, evidence certificates, report
sections, and disclosed assumptions. These files are bookkeeping carriers for the profile contract:
downstream stages may reuse a fact only when it can be traced to profiled tables, validated fields,
executable artifacts, or explicitly recorded assumptions.
C.8 Ontology mapping coverage
The knowledge profiler maps raw fields to biomedical concepts from UMLS, SNOMED CT, ICD-10,
and LOINC through candidate generation followed by type-compatibility and value-range checks.
Overall field-level mapping coverage is 0.83. Coverage for critical task fields, including exposures,
outcomes, confounders, and temporal anchors, is 0.91.
28

Algorithm 2Profile-grounded state update and access in ProCARE
Require:User queryq, datasetD, profile cacheC
Ensure:Analysis artifacts, report, and updated job state
1:Compute dataset hashh= MD5(D).
2:LoadΦfromC[h]if available; otherwise profileDand cacheΦ.
3:Create job workspaceWand write the profile intoexcel_info.json.
4:Compile candidate RWS-IRZ 0 fromqand the high-level profile.
5:Run static IR checks againstΦand the job state.
6:Write acceptedZtorws_ir.jsonand write execution context toexecution_spec.md.
7:Run violation-guided execution usingZ, low-level profile blocks, and operational policy artifacts.
8:Append execution logs, violation sets, validation results, and figure manifests to the job state.
9: Generate certified report sections from the reporting DAG using Φ, Z, logs, figures, evidence certificates,
and existing sections.
Table 29: Required artifact-bundle schema.
Artifact Typical file name Evaluation use
RWS-IRrws_ir.jsonPF, method validation, temporal and grain checks, claim policy.
Executable entry pointanalysis.pyormain.pyXE, CQ, artifact generation, code-region traces.
Execution logsexec_logs.json ,
exec_status.json
Runtime pass/fail, violation localization, evidence reconstruction.
Results manifestresults_manifest.jsonResult-table existence, denominators, generated statistics.
Figure manifestfigure_manifest.jsonFigure existence, caption/axis metadata, chart-fidelity checks.
Violation setviolation_set.jsonVRR and repair diagnostics.
Evidence certificatesevidence_certificates.
json
CTC, UCR, CLV , report traceability.
Assumptions and limitations assumptions.json or report
section
Downgrade handling and policy-compatible language checks.
Final reportreport.md , report.json, or
rendered report
RS, SL, factual-claim extraction, evidence-policy matching.
Unmapped fields remain in ΦL,K with failure tags. The main failure categories are abbreviations or
local jargon without a stable ontology match (0.07), type incompatibility between candidate concepts
and observed values (0.05), ambiguity among indistinguishable candidates (0.03), and mixed units or
inconsistent coding systems (0.02).
C.9 Artifact bundle contract
The prompt schema contains the task definition, optional guidance, and required deliverables. Each
run returns a validated RWS-IR with required tables, join keys, variables, temporal anchors, methods,
artifacts, and claim policy; one executable entry point ( analysis.py or main.py) with optional
helper modules for data loading and artifact generation; and a structured scientific report with evidence
certificates. Generated SQL or pandas operations may reference only tables and columns present in
the profile.
The contract depends on prompt specificity. Under GOAL+METHOD, the agent follows the requested
variables and stops when required data are unavailable. Under GOAL and GOAL+APPROACH, the agent
may generate the closest feasible analysis, but the report must disclose data limitations and method
deviations.
The artifact bundle is the unit of evaluation. A bundle is accepted for full scoring only if it contains
the files in Table 29. Missing execution-dependent artifacts produce N/A for metrics that cannot
be computed, while schema, report, and claim diagnostics are still computed when the submitted
artifacts allow post-hoc checking.
C.10 Profile-constrained coding harness
The code-generation stage is implemented as a controlled execution workspace. The workspace
writes the profile, RWS-IR, local policies, generated code, figures, logs, violation sets, and validation
records into one job directory. The coding agent can edit and execute files inside this workspace,
while the backend reruns the selected entry point and rejects incomplete artifact bundles. Table 30
maps the execution components to concrete implementation artifacts.
29

Table 30: Concrete artifacts used by the profile-constrained coding harness.
Harness component Concrete artifact Purpose
WorkspaceW Isolated job directory with generated
scripts, plots, logs, and report fragments.
Keeps one RWS task reproducible and sep-
arates generated files from source code.
ContextXrws_ir.json , excel_info.json, and
execution_spec.md.
Supplies objective, selected sheets, re-
quired fields, join keys, temporal anchors,
method choices, and claim policy.
PoliciesΠ Local coding instructions, figure policy,
publication_plotting.py, and artifact
schema.
Converts profile and reporting requirements
into file-level rules that the coding agent
must follow.
ToolsT File editing, Python execution, local skill
use, and sandbox validation.
Allows edit-run-fix behavior inside the con-
trolled workspace.
ValidatorsV Entry-point execution, TASK_FAILED sen-
tinel check, figure_manifest.json,
and PNG/PDF/SVG existence checks.
Turns soft generation instructions into com-
pletion gates for executable artifacts.
TracesLopencode_live.log , exec_logs.json,
exec_status.json, and
violation_set.json.
Records evidence for violation-guided re-
pair, failure reporting, and later report
grounding.
Table 31: Task metadata used in the reporting DAG.
Symbol Meaning
prod(t)Artifacts produced by taskt, such as tables, figures, statistics, or text.
req(t)Prerequisites used by taskt, such as variables, cohorts, temporal anchors, or method assumptions.
The constraint intent remains the same, but enforcement happens through observable gates instead
of a separate symbolic solver. Schema constraints are checked against excel_info.json; method-
ological constraints are checked against the RWS-IR and profile semantics; artifact constraints are
checked by execution and manifest validation. If the profile does not support a required variable,
temporal anchor, or statistical procedure, the execution workspace requires a failed run or an explicit
limitation rather than an unsupported substitute.
C.11 DAG reporting dependency rules
Report generation uses a dependency DAG G= (T, E). Each node t∈T is an atomic reporting task
that either constructs a validated evidence artifact or renders a report section from validated artifacts.
Each directed edge (ti, tj)∈E indicates that tj requires artifacts produced by ti. Table 31 defines
the task metadata used by the graph.
Required chapter schema for RS.The minimal required chapters are listed in Appendix C.13. RS
is computed as the fraction of required chapters covered with non-trivial content.
Support score and edge weights.For each dependency edge(t i, tj), we assign a weight:
wij =s ij ·σ(0.0 + 3.0c ij),(6)
where σ(x) = 1 1+e−x maps to [0,1] and sij ∈ {0,1}is a feasibility gate indicating whether tj can
run from the available artifacts and recorded assumptions.
We computec ij from the four deterministic signals in Table 32:
cij = 0.35Svar + 0.25Stemp + 0.25Ssize + 0.15Scons.(7)
All experiments use α= 0.0 , β= 3.0 , wvar = 0.35, wtemp = 0.25, wsize = 0.25, wcons = 0.15, and
Nmin = 30. These constants are fixed before evaluation. They encode the ordering preference that
validated variable support, temporal validity, effective sample size, and method-design consistency
should be present before a result section is promoted above a limitation or feasibility section. The
traversal rule changes report ordering and section expansion only; it does not change executed
statistics or certify unsupported claims.
30

Table 32: Support signals for reporting-task prioritization.
Signal Definition
Svar Variable availability in the analysis-ready cohort, with missingness penalties. One instantiation is
1
|V|
P
v∈V max(0,1−miss(v)).
Stemp Temporal validity, defined as1−r invalid, where rinvalid is the fraction of missing, invalid, or impossible
temporal prerequisites.
Ssize Sample adequacy, defined asmin(1, Neff /30)after filtering and joins.
Scons Method-design consistency, with partial credit only when execution is feasible under recorded assump-
tions.
T0
Objective
T1
Cohort
T2
Baseline
T3
Endpoint
T4
Exposure
T5
Method gate
T6
Primary RFS
T7
Subgroup
Blocked
detailed AE
T9
Report
T8
Safety check
1.00
0.89
0.98
0.85
0.931
1.00
s= 0
Figure 3: Instantiated reporting DAG for the recurrence-free survival task. Solid edges denote
feasible artifact dependencies and show selected support scores; the dashed edge records the blocked
AE-detail analysis, which is routed to limitations rather than promoted as a safety result.
Ordering policy.We generate report outlines with a weighted topological traversal. At each step,
among tasks whose prerequisites are satisfied, we select:
t⋆ = arg max
t∈frontier
X
(u,t)∈E
wut.(8)
C.12 Instantiated reporting DAG
For the recurrence-free survival benchmark instance, the task uses SG.SGDAT as the index date,
the earliest non-missing VT.PADHDAT/VT.PADRDAT as the recurrence event date, and the latest non-
missing VT.VTDAT1/VT.VTDAT2 as censoring time. In the workbook, the surgery cohort contains
1,295 subjects, 1,215 subjects have analyzable RFS follow-up, and 304 subjects have valid recurrence
events. The same graph shows evidence gating: because the AE and SAE detail tables contain no valid
records, detailed AE profiling is blocked and the evidence gap is propagated to the limitations section.
C.13 Standard report schema
The reporting engine targets the sections in Table 35.
D Experimental Protocol and Reproducibility
D.1 Execution environment and cost accounting
Generated analysis code is rerun from a clean job workspace in a Python 3.9 sandbox with network
access disabled. The execution image includes pandas, numpy, scipy, matplotlib, seaborn, and
statsmodels. The evaluator records stdout, stderr, return code, generated files, result manifests,
figure manifests, violation sets, and failure sentinels. LLM calls are made outside the code-execution
sandbox; generated code cannot fetch external data during scoring.
Token use is reported for ProCARE because baselines use different interfaces and are not directly
comparable at the prompt level. Profiling is a reusable dataset-level cost. For the primary HCC
schema, profiling uses approximately Tprof ≈65k tokens, and each query uses approximately
Tinf ≈38k tokens for IR compilation, repair prompts, and certified reporting. For N tasks on the
31

Table 33: Instantiated report-task DAG for the recurrence-free survival benchmark instance. Each
node declares required inputs and produced artifacts. Edges encode artifact prerequisites; infeasible
edges are not selected and instead propagate limitations.
Node Task Required inputs Produced artifacts Report role
T0 Objective binding User prompt, hetero-
geneous profile, report
schema
Objective, endpoint def-
inition, required section
plan
Study overview
T1 Cohort and attritionSG.Subject_Id ,
SG.SGDAT
Analysis cohort, attrition
table, index-date assump-
tions
Overview / Attrition
T2 Baseline covariates T1,DM,BCLC,CP,ECOG Table 1, missingness ta-
ble, covariate map
Baseline characteristics
T3 Endpoint and censoring T1, VT.PADHDAT,
VT.PADRDAT,
VT.VTDAT1,VT.VTDAT2
RFS dataset, event/cen-
sor flags, temporal valid-
ity log
Primary analysis
T4 Exposure matrix T1, TACE, TART, IMU,
PATE
Treatment exposure ma-
trix, dated exposure avail-
ability
Primary / Subgroup
T5 Method feasibility gate T2, T3, T4, procedural
policy
KM feasibility decision
and caveats
Methods
T6 Primary RFS analysis T3, T4, T5 KM curve, RFS summary
table, primary result text
Primary analysis
T7 Subgroup/sensitivity T2, T4, T6 Subgroup tables and
caveats
Sensitivity analysis
T8 Safety evidence checkAE_HQ,SAE_HQ,AE,SAE Safety limitation state-
ment; blocked detailed
AE profiling
Safety / Limitations
T9 Report synthesis Prior artifacts and evi-
dence map
Final structured report
and claim-evidence map
Final report
Table 34: Selected dependency edges and support scores for the instantiated DAG. The feasibility gate
sij blocks hard-infeasible dependencies. The support score cij summarizes deterministic evidence
from variable availability, temporal validity, sample adequacy, and method-design consistency.
Edge Dependency rationales ij cij
T0→T1 Cohort construction requires the objective, index date, and output
contract.
1 1.00
T1→T2 Baseline summaries must be computed within the index cohort; BCLC
and Child–Pugh coverage is high, while age missingness must be
disclosed.
1 0.89
T1→T3 RFS endpoints and censoring must be aligned to surgery date; 1,215
subjects have usable follow-up and one temporal anomaly is flagged.
1 0.98
T1→T4 Treatment exposure grouping must be aligned to the index cohort;
treatment proxies cover 1,104 subjects but dated exposures are incom-
plete.
1 0.85
T5→T6 The primary RFS analysis is selected only after the method gate passes;
the combined gate has Svar = 0.828, Stemp = 0.999, Ssize = 1.000,
andS cons = 1.000.
1 0.931
T8→detailed AE profiling Detailed AE/SAE profiling requires non-empty detail tables; both
detail tables contain no valid records.
0 0.00
T8→T9 The empty AE/SAE detail tables support a limitation statement rather
than unsupported safety claims.
1 1.00
same dataset,
¯T(N) =T inf +T prof /N.
Thus ¯T(1)≈103ktokens, ¯T(20)≈41.3ktokens, and ¯T(36)≈39.8ktokens per query.
32

Table 35: Required RWS report sections used by the RS metric.
Section Expected content
Study Overview Cohort definition and objective statement.
Attrition Analysis Patient disposition and eligibility filtering steps.
Baseline Characteristics Demographics, clinical history, baseline vitals, and baseline labs.
Primary Analysis Main efficacy or exposure-outcome results, such as KM curves or hazard ratios.
Safety Profiling Adverse-event screening summaries and available safety proxies.
Sensitivity/Subgroup Analysis Checks across predefined strata.
Limitations Data constraints, method limitations, and potential biases.
Table 36: Baseline adaptation and scoring rules.
Method family Run protocol Scoring rule
ReAct and ToolLLM Agentic tool-use baselines are asked to inspect the tables,
write executable analysis code, generate artifacts, and
produce a report under the same prompt.
Deterministic validators execute the final entry point
when provided; reports are checked post hoc for evidence
support.
TableGPT-Agent and
ChatExcel-Max
Table-analysis agents are asked to generate the requested
analysis and report.
If no executable artifact bundle is produced, execution-
dependent metrics are N/A; report and claim metrics are
computed when possible.
Gemini-3-Pro direct base-
line
Gemini-3-Pro receives the task and data-access instruc-
tions and is asked to return code, artifacts, and report
content.
Generated code is executed in the same sandbox and
evaluated by the same artifact and claim validators.
TableGPT2 The table model is evaluated on table-analysis outputs
and executable artifacts when available.
Metrics requiring a complete bundle are N/A when the
method does not emit the required artifact.
Claude Code and Codex Native coding-agent baselines receive the benchmark
prompt, data-access path, artifact contract, and sandbox
budget through their repository editing interfaces. They
may create, edit, execute, and repair files within the job
workspace.
The final workspace is re-executed from a clean scorer
sandbox. Execution, artifact, clinical/statistical language,
and claim-trace metrics are computed post hoc from the
submitted files and report.
ProCARE Full profile–IR–execution–certificate–DAG workflow. All deterministic and judge metrics are computed on the
accepted artifact bundle.
D.2 Systems and baseline adaptation
All methods receive the same natural-language task prompt, raw data access boundary, deliverable
request, and inference budget. Direct Gemini-3-Pro baselines and direct Gemini-3-Pro scaffolded
controls use the same model as the default ProCARE backbone. Claude Code and Codex are evaluated
as native code-agent baselines: they can edit files and run code through their coding-agent interfaces,
but they do not receive ProCARE’s profile object, typed RWS-IR, evidence-certificate admission
policy, or certified reporting DAG unless they infer or generate analogous files from the prompt.
ProCARE additionally constructs and uses the heterogeneous profile, typed RWS-IR, execution
validators, evidence certificates, and certified reporting DAG. Baselines are evaluated under a post-
hoc contract checker so that schema use, execution, artifact completeness, and claim traceability are
measured against the same profile-derived constraints.
A method is not penalized twice for a missing executable bundle. XE is zero when an executable
entry point is submitted but fails, while metrics that require absent artifacts are marked N/A. Schema
feasibility, report structure, scientific language, and post-hoc claim diagnostics are still computed
whenever enough submitted content is available. Code-agent baselines typically produce executable
bundles and stronger local repairs, but their reports are still scored without granting credit for
ProCARE-only objects such as accepted RWS-IRs or admitted evidence certificates.
D.3 Fairness-controlled scaffolded baselines
To address the concern that the artifact contract may favor ProCARE, we conducted a scaffolded-
baseline evaluation under the same final checker used for the main baseline comparison. These
RQ1 fairness controls differ from the RQ2 mechanism ablations in Appendix D.4: ablations remove
one component from ProCARE, whereas scaffolded baselines add evaluator-facing information and
output schemas to external baselines or a direct Gemini-3-Pro run. Direct Gemini-3-Pro controls
use the same provider endpoint, model identifier, decoding settings, and inference budget as the
default ProCARE backbone. The scaffold gives non-ProCARE methods the same schema profile
33

Table 37: Inputs and controls used in the scaffolded-baseline fairness evaluation. These are baseline
adaptations, not ProCARE component ablations.
Condition Information given to model Output and repair control Purpose
Profile/template baseline scaffold Task prompt, raw data access, Φ
summary, table/field dictionary,
join keys, temporal-role candi-
dates, and artifact template.
One initial generation; no valida-
tor feedback loop beyond final
scoring.
Controls for missing schema and
output-format information.
Profile/template/repair baseline
scaffold
Same as above. Three edit-run-repair turns with
standardized validator feedback
and identical execution budget.
Controls for unequal repair oppor-
tunity.
Direct Gemini-3-Pro + validator in-
terface
Gemini-3-Pro receives Φ, artifact
template, sandbox logs, and val-
idator feedback.
Three repair turns; no typed IR
compiler or certificate admission
gate.
Controls for deterministic valida-
tion feedback without ProCARE
planning.
Direct Gemini-3-Pro + study-spec
schema
Gemini-3-Pro receives Φ and
must emit study_spec.json
before writing code and report.
No ProCARE IR compiler; val-
idator feedback is limited to
schema/artifact execution errors.
Controls for evaluator-compatible
study-spec output.
Direct Gemini-3-Pro + claim-trace
schema
Gemini-3-Pro receives Φ, arti-
fact template, and claim-trace file
schema.
No certificate admission gate or
certified DAG ordering.
Controls for evaluator-compatible
claim-trace output.
ProCARE reference Full profile, IR compiler,
violation-guided execution,
evidence certificates, and certified
report DAG.
Same three repair turns and final
checker.
Reports the integrated contract
workflow for comparison.
Table 38: Full metric results for fairness-controlled scaffolded baselines. Higher is better except UCR
and CLV . Rows are baseline adaptations, not ProCARE ablations; values are final checker outputs.
Baseline condition Performance Contract diagnostics
GA↑PF↑XE↑CQ↑VC↑CF↑RS↑SL↑VRR↑CTC↑UCR↓CLV↓
ReAct + fairness scaffold 0.82 0.79 0.74 0.69 0.62 0.65 0.75 0.70 0.62 0.70 0.13 0.10
ToolLLM + fairness scaffold 0.79 0.80 0.68 0.65 0.58 0.62 0.72 0.67 0.58 0.66 0.15 0.12
Direct Gemini-3-Pro + profile/template 0.77 0.73 0.66 0.62 0.54 0.58 0.73 0.65 0.31 0.55 0.20 0.15
Direct Gemini-3-Pro + validator repair 0.80 0.78 0.79 0.72 0.60 0.64 0.75 0.69 0.68 0.65 0.15 0.11
Direct Gemini-3-Pro + study-spec
schema
0.82 0.82 0.70 0.68 0.57 0.62 0.71 0.68 0.43 0.52 0.21 0.16
Direct Gemini-3-Pro + claim-trace
schema
0.78 0.74 0.63 0.61 0.59 0.63 0.74 0.73 0.35 0.74 0.11 0.08
ProCARE reference 0.86 0.84 0.92 0.88 0.72 0.74 0.80 0.79 0.81 0.90 0.06 0.03
Φ, artifact-bundle template, raw data access boundary, execution sandbox, and three-turn repair
budget needed to satisfy the evaluator. It does not give baselines ProCARE’s IR compiler, certificate
admission gate, certified reporting DAG, or hidden planner state. Rows that mention a study-spec or
claim-trace schema only require compatible JSON files for scoring.
The shared artifact template requires: study_spec.json, analysis.py or main.py,
result_manifest.json, figure_manifest.json, claim_trace.json when the method at-
tempts explicit claim tracing, assumptions.json, and report.md. For methods that do not emit
a typed RWS-IR, the evaluator maps the submitted study_spec.json into the canonical scoring
schema before computing PF. For methods that do not emit explicit evidence certificates, CTC/UCR/-
CLV are computed by the same post-hoc evidence reconstruction used in Table 36.
Table 38 reports the final checker outputs for the scaffolded-baseline evaluation. Scaffolded baselines
improve substantially over generic agents, reducing N/A rates and narrowing the execution gap,
while the integrated ProCARE workflow remains strongest on violation resolution and claim-level
traceability. The table should be read as a fairness-control comparison, not as evidence that individual
ProCARE modules have been added to an otherwise unchanged LLM. All direct rows use Gemini-3-
Pro.
34

Table 39: Ablation definitions for contract mechanisms.
Variant Removed component What remains fixed
w/o profileΦ The model does not receive the heterogeneous profile
as a contract object. It may inspect raw table metadata
and generated summaries, but generation lacks profile-
grounded repair hints.
Prompt, budget, execution sandbox, reporting request,
and post-hoc evaluator.
w/o RWS-IR The model writes code and a report without producing
the typed RWS-IR.
Raw data access, profile summaries when available,
execution sandbox, and post-hoc claim diagnostics. PF
is N/A because no typed IR exists.
w/o violation-guided repair Runtime validators detect violations, but localized vio-
lation sets are not fed back into the next edit.
Profile, RWS-IR, execution sandbox, artifact validators,
certificates, and report policy.
w/o evidence certificates The report is generated without explicit claim certifi-
cates and without the claim-admission gate.
Profile, RWS-IR, execution repair, artifacts, and DAG
section ordering. CTC for emitted explicit certificates
is zero; post-hoc support can still be inspected sepa-
rately.
w/o certified DAG ordering Evidence certificates remain available, but report sec-
tions are generated in a fixed or unconstrained order
without dependency-aware traversal.
Profile, RWS-IR, execution repair, artifact validators,
and claim admission.
Full ProCARE No contract component is removed. Complete profile–IR–repair–certificate–DAG work-
flow.
D.4 Ablation protocol
Mechanism ablations remove one contract component at a time while keeping all remaining compo-
nents fixed whenever the remaining workflow is defined. Table 39 specifies the intervention behind
the ablation table in the main paper.
D.5 Model access, decoding, and version identifiers
Backbone-sensitivity experiments keep profiling, RWS-IR compilation, violation-guided execution,
certified reporting, prompts, and scoring scripts fixed. The table records the paper-level model
identifiers and roles used in the experiments. Provider-returned request metadata is retained in run
logs; when a provider alias differs from the paper-level display name, the logged identifier is the re-
producibility target. Generation runs use the released implementation’s production decoding settings,
with temperature 0.2 for Gemini/openai-compatible providers and 0.1 for DeepSeek-compatible
providers; judge models are run at temperature 0.
D.6 Reproducibility package
The anonymous release contains the manuscript sources, system code, prompt definitions, the fully
de-identified HCC benchmark tables, Public-RWS bundle metadata, profile artifacts, evaluation
scripts, and figure-generation scripts. The HCC release includes the record-level tables needed to
rerun the 36 primary tasks, with direct identifiers removed and random benchmark IDs retained for
reproducible linkage.
Listing 6: Local reproduction commands.
cd code/backend
python -m app.cli --excel <workbook.xlsx> --topic "<benchmark prompt>" --refine
python tests/run_all.py
cd ../../paper
build.cmd nips appendix
E Additional Results and Diagnostics
E.1 Claim-diagnostic interpretation
More specific prompts increase claim traceability because they constrain variables, temporal anchors,
methods, and expected artifacts before reporting. The dominant downgrades are language-policy
failures rather than arithmetic inconsistencies: causal phrasing from descriptive analyses, safety
35

Table 40: Model access, version metadata, and evaluation roles.
Role Paper-level model identifier Access mode Use in evaluation
Backbone GPT-5.2 Proprietary API Backbone-sensitivity run under the fixed ProCARE work-
flow.
Backbone GPT-4 Turbo Proprietary API Backbone-sensitivity run under the fixed ProCARE work-
flow.
Backbone Claude Opus 4.5 Proprietary API Backbone-sensitivity run under the fixed ProCARE work-
flow.
Backbone Claude Sonnet 4.5 Proprietary API Backbone-sensitivity run under the fixed ProCARE work-
flow.
Backbone Claude-3 Opus Proprietary API Backbone-sensitivity run under the fixed ProCARE work-
flow.
Backbone, direct
baseline, and scaf-
folded control
Gemini-3-Pro Proprietary API Default ProCARE backbone; also used for the direct base-
line and all Direct Gemini-3-Pro scaffolded fairness-control
rows.
Backbone and judge Gemini-2.5-Pro Proprietary API Backbone-sensitivity run and one blinded semantic judge.
Backbone Qwen3-Max API endpoint Backbone-sensitivity run under the fixed ProCARE work-
flow.
Backbone Qwen3-235B-A22B- Instruct-2507 API endpoint or hosted open-source model Backbone-sensitivity run.
Backbone DeepSeek-V3.2 API endpoint or hosted
open-source model
Backbone-sensitivity run.
Backbone DeepSeek-R1-0528 API endpoint or hosted
open-source model
Backbone-sensitivity run and non-valid-bundle baseline cat-
egory.
Code-agent baseline Claude Code (Claude Sonnet
4.5 backend)
Proprietary coding-agent
interface
Baseline run through the native Claude Code repository-
editing workflow; provider-returned CLI/model metadata is
retained in the run log.
Code-agent baseline Codex (gpt-5.3-codex back-
end)
Proprietary coding-agent
interface
Baseline run through the native Codex repository-editing
workflow; CLI session metadata and final workspace state
are retained for reproduction.
Judge Qwen2.5-1M API endpoint Second blinded semantic judge.
Table 41: Repository components used for reproduction.
Path Contents
paper/Manuscript, supplement, bibliography, NeurIPS style file, build script, and paper figures.
code/backend/Profiling, planning, code-generation, execution, report-generation, and API services.
code/backend/tests/ Local tests for profile construction, planning, code execution, OpenCode integration, and report genera-
tion.
code/frontend/Interface for project setup, profile inspection, RWS-IR review, execution monitoring, and report review.
code/output/knowledge_
base/profiles/
Cached profile artifacts used by the implementation.
rws_hcc_benchmark/ Fully de-identified HCC benchmark tables, data dictionary, checksums, task metadata, and release terms
for reproducing the 36 primary tasks.
rws_public_datasets_
bundle/
Public-RWS source manifests, checksums, table shapes, and public dataset files.
figure_code/Scripts used to regenerate paper diagnostic figures.
claims based only on screening pages, or subgroup conclusions without sufficient support. During
certification, these claims are rewritten as limitations or removed from the admitted factual-claim set.
E.2 Backbone-sensitivity interpretation
Backbone substitution changes only the base LLM used for planning, code editing, and report
drafting. Profiling, RWS-IR schema, validators, evidence-certificate admission, report schema, and
evaluation remain fixed. Stronger backbones improve GA, PF, VRR, and CTC because they use
profile constraints and repair feedback more reliably. Execution-only differences are smaller than
planning and reporting differences because deterministic validation and localized repair bound the
accepted artifact space after code is generated.
F System Interface and Workflow
Figures 4 and 5 show the implementation interface states. They are included as workflow evidence
rather than method exposition: the panels identify where profile artifacts, IR traces, execution logs,
generated figures, and section-level report blocks are inspected during a run.
36

(a) System dashboard for managing RWS projects and
cohort status.
(b) Profile panel for reviewing structural metadata
(ΦS) and ontology mappings (ΦK).
(c) RWS-IR view showing goal compilation (Tgoal →
Z).
(d) Coding harness view with reasoning traces, sand-
box logs, and verification status.
Figure 4: ProCARE interface states for project setup, profile inspection, RWS-IR compilation, and
coding execution.
(a) Report review view with generated tables, charts,
and evidence links.
(b) Section-wise report generation with data-bound
report blocks.
Figure 5: Report-facing interface states for reviewing generated artifacts, evidence links, and section-
wise report content.
G Evaluation Protocol and Rubrics
Evaluation uses deterministic validators for feasibility and execution checks, and LLM judges for
semantic quality.
G.1 Metrics Overview
Table 42 defines the metrics used for end-to-end RWS automation. All scores are normalized to [0,1] .
G.2 Deterministic validators
Deterministic validators are used whenever the property can be checked from the artifact bundle.
PF checks whether the accepted RWS-IR references only profiled tables, fields, keys, clinical roles,
temporal anchors, and methods. XE checks whether the submitted entry point exits successfully,
avoids failure sentinels, and writes the required result and figure manifests. Artifact completeness
requires declared output files to exist, be nonempty, and be referenced by the corresponding manifest.
37

Table 42: Metrics used in the appendix evaluation protocol.
Metric Type Scoring rule
RWS-IR Feasibility (PF) Deterministic + judge Validates the RWS-IR against ΦS and penalizes
non-existent tables, columns, invalid joins, unsup-
ported temporal anchors, or incompatible analysis
grains. Residual ambiguity is checked by the judge.
Code Executability (XE) Deterministic Sandbox execution success rate, npass/N; runtime
errors and invalid output files count as failures.
Violation Resolution Rate (VRR) Deterministic Fraction of detected execution-time contract viola-
tions resolved before the accepted run.
Report Structure (RS) Deterministic Fraction of required report sections in Table 35 cov-
ered with non-trivial content.
Claim Trace Coverage (CTC) Deterministic Fraction of final factual claims linked to valid evi-
dence certificates.
Unsupported Claim Rate (UCR) Deterministic Fraction of final factual claims without admissible
evidence support.
Claim Language Violation (CLV) Deterministic + judge Fraction of factual claims whose wording exceeds
the support level allowed by the evidence certificate
and RWS-IR claim policy.
Goal Alignment (GA) Judge Alignment with the clinical objective, target popu-
lation, and requested endpoint.
Code Quality (CQ) Judge Soundness of data handling, missingness handling,
joins, and statistical implementation.
Visual Clarity (VC) Judge Readability and labeling quality of generated fig-
ures.
Chart Fidelity (CF) Judge Consistency between plotted values, execution logs,
and report statements.
Scientific Language (SL) Judge Clinical tone, hedging, and limitation disclosure.
Temporal consistency checks row-level ordering between index, exposure, event, and censoring dates
when those roles are declared in Z. Chart-result consistency checks whether plotted variables, group
labels, sample sizes, and reported summary values match execution logs or result tables.
All metrics are normalized to [0,1] . XE is npass/N over tasks. PF is one for a statically admissible
RWS-IR, zero for a hard-invalid RWS-IR, and partially credited only for residual semantic ambiguity
adjudicated by the fixed rubric. RS is the fraction of required report sections with task-relevant
content. VRR, CTC, UCR, and CLV are computed from logged violations and extracted factual
claims as described in Appendix C.5 and Appendix C.6.
For baselines that do not implement ProCARE’s contract internally, the evaluator reconstructs the
same diagnostics from final artifacts. A baseline can receive CTC credit only when a factual claim can
be linked to an executed result, code region, profile-supported field, or explicit assumption. Missing
artifacts or unsupported variables block traceability.
G.3 LLM judge protocol
We useGemini-2.5-ProandQwen2.5-1Mas independent judges with temperature 0. Judges are
blinded to method identity and receive the same artifact bundle: input prompt, generated RWS-IR,
code, execution logs, result and figure manifests, evidence certificates when available, assumptions,
limitations, and final report. Scores are normalized to [0,1] and averaged across judges. Schema
hallucination and artifact inconsistency are handled as hard rubric failures for the affected dimensions.
G.4 Expert-review protocol
Expert review is performed on the 36 primary HCC benchmark instances. The panel contains five
blinded reviewers: three board-certified clinical experts with hepatobiliary oncology or hepatology
experience (C1–C3) and two statistics/data experts with clinical data-analysis experience (S1–S2).
Reviewers receive anonymized artifact bundles containing the task prompt, study specification,
38

Table 43: Raw expert-rating data format used before aggregation. One row stores one reviewer–
instance–stage score.
Column Allowed values or format Definition
review_idstable string Unique row identifier.
benchmark_idHCC-001–HCC-036 Primary benchmark instance identifier.
objective cohort, safety-proxy, efficacy,
resource-use
Benchmark objective family.
prompt_level goal, goal+approach, goal+method Prompt-specificity level.
method_idsubmitted method identifier Method label masked during review and restored only for analysis.
stage rws_ir, code, visualization, report-
ing
Workflow stage being scored.
artifact_idpath or hash Submitted artifact bundle, code file, figure set, or report identifier.
reviewer_idC1, C2, C3, S1, S2 De-identified reviewer identifier.
reviewer_roleclinical or statistics_data Reviewer expertise group.
criterion_id global_stage_score or rubric sub-
criterion
Overall stage score or optional subcriterion.
score_1_5integer 1–5 Raw Likert score before normalization.
major_error_flag0 or 1 Reviewer-marked hard error, such as invalid endpoint, impossible join, or
irreproducible code.
claim_flag0, 1, or NA Whether the reviewed report or figure interpretation contains a claim exceeding
evidence support.
comment_code none, schema, method, temporal,
claim, figure, reproducibility, other
Structured reason for downgrade, if any.
free_text_commentde-identified text Short reviewer note used for adjudication and error analysis.
timestamp_utcISO-8601 timestamp Completion time of the review row.
code or execution logs when relevant, figures, assumptions, limitations, evidence certificates when
available, and final report. Method identity is masked in the review package.
Reviewers score each stage on a five-point Likert scale: 1 indicates an invalid or irrelevant artifact,
3 indicates a partially correct artifact with important limitations, and 5 indicates a clinically and
methodologically appropriate artifact with limitations disclosed. The clinical panel focuses on clinical
objective alignment, endpoint and covariate validity, clinical interpretability of figures, and claim
scope. The statistics/data panel focuses on data linkage, analysis grain, statistical method choice,
code reproducibility, figure-result consistency, and whether reported results are supported by executed
artifacts. Code scores in the main table use the statistics/data panel only; the other stage scores
aggregate all five reviewers because both clinical and statistical/data judgments are relevant.
The raw evaluation data are represented in the long format in Table 43. The required stage-level
row set contains 36×(5 + 2 + 5 + 5) = 612 reviewer–instance–stage records before optional
criterion-level comments: five reviewers score RWS-IR, visualization, and reporting, while S1–S2
score code implementation. Additional criterion-specific rows can be added with the same keys when
a reviewer records a subscore or a major error flag.
For each benchmark instance i, reviewer r, and stage s, the raw Likert score is xirs ∈ {1, . . . ,5}.
Stage-level expert scores are first averaged across the eligible reviewer setR s:
Eis = 1 |Rs| X r∈Rs xirs.
Scores are normalized to [0,1] for calibration plots by ˜Eis = (Eis −1)/4 , but the main paper reports
mean±SD on the original 1–5 scale. Spearman ρ is computed between per-instance expert scores and
the corresponding automated stage score: (GA + PF)/2for RWS-IR, CQ for code,(VC + CF)/2for
visualization, and SL for reporting. Confidence intervals for mean expert scores use a t interval over
36 instance-level means; confidence intervals for Spearman correlations use Fisher transformation.
G.5 Semantic Rubric Anchors
Judges assign 1–5 Likert scores for Goal Alignment (GA), Code Quality (CQ), Visual Clarity (VC),
and Scientific Language (SL). Scores are normalized to [0,1] with a linear transformation. Table 48
lists the anchor definitions.
39

Table 44: Expert panel responsibilities and raw scoring volume.
Stage Eligible reviewers Primary review focus Raw records
RWS-IR C1–C3, S1–S2 Clinical goal, endpoint validity, data linkage, analysis grain, and statisti-
cal design feasibility.
180
Code S1–S2 Reproducibility, executable implementation, statistical method use, arti-
fact writing, and result consistency.
72
Visualization C1–C3, S1–S2 Clinical interpretability, sample-size labeling, figure-result agreement,
and avoidance of unsupported visual claims.
180
Reporting C1–C3, S1–S2 Clinical language, limitation disclosure, statistical wording, and claim-to-
evidence support.
180
Table 45: Stage-level expert score summary on the 36 primary HCC benchmark instances. CI is the
95% confidence interval for the instance-level mean.
Stage Instance means Raw records Mean±SD 95% CI Median [IQR]
RWS-IR 36 180 4.38±0.48 4.22–4.54 4.33 [4.00, 4.67]
Code 36 72 4.42±0.21 4.35–4.49 4.42 [4.25, 4.58]
Visualization 36 180 4.50±0.53 4.32–4.68 4.67 [4.00, 5.00]
Reporting 36 180 4.13±0.64 3.91–4.35 4.17 [3.67, 4.67]
Table 46: Inter-rater reliability for the human expert panel. Stages scored by five reviewers use
two-way random-effects ICC for averaged ratings; the two-reviewer code stage uses weighted Cohen’s
κw.
Stage Panel Statistic Estimate 95% CI Interpretation
RWS-IR C1–C3, S1–S2 ICC(2,k) 0.84 0.72–0.91 Strong agreement on specification
validity.
Code S1–S2κ w 0.76 0.61–0.88 Substantial agreement on repro-
ducibility and statistical implemen-
tation.
Visualization C1–C3, S1–S2 ICC(2,k) 0.79 0.66–0.88 Strong agreement on figure clarity
and consistency.
Reporting C1–C3, S1–S2 ICC(2,k) 0.77 0.63–0.87 Substantial-to-strong agreement on
language and claim scope.
Table 47: Correlation between automated metrics and aggregated expert scores.qis the Benjamini–
Hochberg adjustedpvalue across the four stage-wise correlations.
Stage Expert aggregation Automated scoreρ95% CIp q
RWS-IR Mean of C1–C3, S1–S2(GA+P F)/20.82 0.67–0.90<0.001<0.001
Code Mean of S1–S2CQ0.74 0.54–0.86<0.001<0.001
Visualization Mean of C1–C3, S1–S2(V C+CF)/20.75 0.55–0.86<0.001<0.001
Reporting Mean of C1–C3, S1–S2SL0.71 0.49–0.84<0.001<0.001
H Prompts and Templates
H.1 Benchmark prompt template
Each benchmark instance is rendered into a common prompt with three fields:Task, optional
Guidance, andDeliverables. The task states the study objective. Guidance supplies approach-level
or method-level constraints for GOAL+APPROACHand GOAL+METHOD. Deliverables require a
validated RWS-IR, one executable entry point with generated artifacts, and a structured report with
assumptions, limitations, and evidence certificates. Hallucinated tables or columns are disallowed.
H.2 IR compiler prompt template
The IR compiler receives the user prompt, high-level structural profile, high-level knowledge profile,
output contract, and claim-policy rules. It returns JSON containing study design, analysis grain, join
graph, entity keys, temporal anchors, variable-role bindings, method specification, required artifacts,
assumptions, and allowed or blocked claim types. If the profile does not support a requested variable
or method, the compiler must either downgrade the task or return an infeasibility trace.
40

Table 48: Semantic rubric anchors for LLM judges.
Metric Score 5 Score 3 Score 1
Goal Alignment Addresses the clinical ob-
jective, target population,
and endpoints with explicit
limitation disclosure.
Partially addresses the task
with minor errors in inclu-
sion criteria or endpoints.
Gives an irrelevant analy-
sis or misunderstands the
clinical goal.
Code Quality Uses sound pandas or SQL
logic, handles missing data
and types correctly, and
keeps the implementation
modular.
Runs but remains fragile,
often because of hardcoded
values or inefficient joins.
Uses an incorrect method,
applies the wrong statisti-
cal test, or contradicts the
plan.
Visual Clarity Produces figures with clear
axes, legends, labels, and
titles that support the re-
ported results.
Produces legible charts
with missing units, over-
lapping labels, or default
styling.
Produces misleading, illeg-
ible, or unrelated visualiza-
tions.
Scientific Language Uses clinical language
with appropriate hedging
and clear limitation disclo-
sure.
Uses a general scientific
tone but has verbose phras-
ing or imprecise medical
terminology.
Uses casual language or
makes unsupported claims.
H.3 Coding harness prompt template
The coding harness receives the accepted RWS-IR, low-level field profile, selected sheets, local figure
policy, artifact schema, and any previous violation set. It writes one executable entry point, generates
declared artifacts, and produces figure and result manifests. Repairs must address the localized
violation set without introducing fields or methods absent from the profile.
H.4 Report and certificate prompt template
The report generator receives the accepted RWS-IR, result artifacts, figure manifest, execution logs,
assumptions, limitations, and claim-policy rules. Each factual sentence must be paired with an
evidence certificate or rewritten as a limitation. The generator must not convert descriptive proxy
artifacts into causal, safety-critical, regulatory, or treatment-effect claims.
H.5 Judge prompts
The judge receives the ground-truth data profile Φ so that schema hallucinations can be checked
against the same table and field constraints used by the validators.
System prompt.Defines the reviewer role and scoring constraints.
Prompt
Prompt 1. Expert Judge System Prompt
You are a Senior Clinical Data Scientist reviewing Real-World Study (RWS) automation
artifacts.
Your task is to evaluate an AI agent’s artifacts against a specificGround Truth Schema.
Scoring rules:
1. Schema Hallucination = 0:Any usage of tables/columns not present in the provided
[DATA_PROFILE]results in a score of 0 for relevant metrics, regardless of code quality.
2. Consistency:The numbers in the Final Report must be consistent with the Execution Logs.
3. Structured rationale:Provide a concise evidence-based rationale before assigning JSON
scores.
User prompt.Injects the profile and artifact bundle.
41

Prompt
Prompt 2. Context-Injection User Prompt
[PART 1: GROUND TRUTH CONTEXT]
USERQUERY: {user_query}
DATAPROFILECONSTRAINTS(Φ):
(Valid tables, columns, and join keys derived from the dataset)
{profile_snapshot_str}
[PART 2: AGENT ARTIFACTS]
1. RWS-IR: {agent_rws_ir_json}
2. CODE: {generated_code}
3. LOGS: {execution_logs}
4. VISUALS: {list_of_generated_files}
5. EVIDENCECERTIFICATES: {evidence_certificate_json}
6. REPORT: {final_report_content}
[PART 3: TASK]
Analyze the artifacts and score them based on the rubric.
Structured assessment
•Schema Check:Does the code use ONLY columns listed in [Data Profile Constraints]?
•Logic Check:Is the statistical method appropriate for {user_query}?
•Consistency:Do chart findings match the log data?
JSON output
Return a JSON object with keys: GA, CQ, VC, CF, SL.
Format: {"Analysis": "...", "Scores": {...}, "Failure_Mode":
"None/Hallucination/Logic"}
I Data Access, Privacy, and Responsible Use
The released materials include the reproducible benchmark logic and the fully de-identified record-
level HCC benchmark tables. The public package includes prompts, profiles, schema artifacts,
aggregate summaries, de-identified HCC tables, HCC data dictionary, checksums, public-data man-
ifests, and evaluation scripts. Direct participant identifiers and identity-linking fields are removed
from the HCC release, while random benchmark subject and visit identifiers are retained to preserve
reproducible table joins and longitudinal task execution. Public-RWS datasets are accessed from their
original public sources, with source metadata and checksums recorded in the release documentation.
The HCC benchmark is released for research reproduction and auditing of RWS automation methods.
The release terms prohibit attempted re-identification, participant linkage to external data sources,
and clinical use of generated outputs. Any downstream deployment on institutional data requires
local governance review, schema revalidation, and confirmation that the site-specific claim policy
matches the available data.
ProCARE is evaluated as a research automation and auditability system, not as an autonomous clinical
decision system. Evidence certificates establish traceability to implemented validators and artifacts.
They do not establish clinical truth, causal validity, regulatory sufficiency, or prospective safety. The
primary HCC benchmark is single-center and disease-specific. Public-RWS-18 tests schema transfer,
but it does not replace multi-institutional longitudinal RWS validation. Porting ProCARE to OMOP,
FHIR, or another institutional schema requires rebuilding the profile, revalidating RWS-IR checks,
and confirming that claim policies match the new data source and study design.
42
