---
title: Evaluating Agentic Bioinformatics through Function, Evidence, and Validation
url: https://arxiv.org/abs/2607.27556
category: ai-marketing
subcategory: empirical
date: 2026-07
venue: ''
authors:
- Phuc Pham
- Truong-Son Hy
source: arxiv
pdf_url: https://arxiv.org/pdf/2607.27556
pages: 47
chars: 262255
fetched_at: '2026-11-08T13:31:34+00:00'
kb_version: 1
---

# Evaluating Agentic Bioinformatics through Function, Evidence, and Validation

Agentic Bioinformatics through Function, Evidence, and Validation, 2026, pp.
1–48
Evaluating Agentic Bioinformatics through Function,
Evidence, and Validation
Phuc Pham1 and Truong Son Hy 1,∗
1 Department of Computer Science, The University of Alabama at Birmingham, USA
∗Corresponding author. thy@uab.edu
Abstract
Large language model agents increasingly plan, execute, and interpret biological analyses, yet fluent responses, successful tool calls, and benchmark
performance alone do not establish scientific credibility. Existing reviews primarily organize biological agents by application, architecture, and agentic
capability, but do not jointly operationalize the accountability of agent-generated workflows. We address this gap by treating the inspectable workflow
trajectory, rather than architecture or final output alone, as the primary unit of analysis. We introduce the Function–Evidence–Validation (FEV)
framework, which separates demonstrated workflow operations, traceable support for actions and claims, and use-case-specific validation. Using FEV,
we map 109 agentic or agent-adjacent systems and 28 benchmark or evaluation resources, representing 128 unique publications across genomics, single-
cell and spatial omics, protein science, drug discovery, computational pathology, and general bioinformatics automation. Across domains, planning and
tool-mediated execution have advanced more rapidly than replayability, provenance, robust scientific assessment, external validation, and prospective
empirical testing. We therefore argue that agentic bioinformatics should be assessed through workflow correctness rather than final-answer correctness
alone. FEVprovidesapracticalbasisforcomparingsystemsanddesigningtransparent, auditable, andscientificallyaccountablebioinformaticsworkflows.
Keywordsagentic AI, bioinformatics, large language models, scientific workflows, workflow validation, evidence grounding, reproducibility,
computational biology
AbbreviationsAI, artificial intelligence; FEV, Function–Evidence–Validation; LLM, large language model; scRNA-seq, single-cell RNA sequencing
Introduction
Motivation, Definition, and Contributions
Bioinformatics increasingly relies on interdependent workflows linking
biological questions to data acquisition, quality control, preprocessing,
statistical analysis, visualization, and interpretation. Reliable automation
therefore requires more than successful software execution. It also depends
on appropriate data and metadata, defensible analytical assumptions, preserved
parameters and intermediate artifacts, and conclusions supported by traceable
evidence (21; 34; 129).
Large language models (LLMs) provide natural-language interfaces for
literature retrieval, code generation, database interaction, and scientific
interpretation (157; 172; 141). Agentic systems extend these capabilities
through multistep planning, tool-mediated execution, workflow-state management,
critique, repair, and adaptive decision-making. Recent systems span multi-
omics analysis, single-cell workflows, protein design, and experimentally
evaluated biomolecular discovery (173; 148; 37; 123). We useagentic
bioinformaticsto describe systems that adaptively coordinate data, evidence,
models, tools, and analytical actions across a biological workflow.
Operational capability, however, does not establish scientific reliability.
A system may execute an inappropriate analysis, retrieve authoritative but
irrelevant evidence, preserve a replayable computation supporting an unjustified
interpretation, or experimentally test only a restricted part of its principal
claim. Scientific credibility therefore depends on theinspectable workflow
trajectory: the objective, data and metadata, analytical decisions, tools and
parameters, intermediate artifacts, failures and repairs, supporting evidence,
and evaluation procedures connecting a biological question to its reported
conclusion (69; 171; 108).
This motivates a shift fromfinal-answer correctnesstoworkflow correctness.
The central question is not simply whether an agent produces a plausible or
benchmark-matching answer, but whether the process supporting that answer is
appropriate, executable, traceable, replayable, and scientifically defensible.
Recent reviews have organized biological agents by application domain,
architecture, agent capability, interaction mode, evaluation strategy, and
resource integration (171; 157; 108; 28; 10). They have also identified evidence
grounding, reproducibility, robustness, and validation as important concerns.
The remaining gap is therefore not the absence of these topics, but the lack of a
common framework that jointly operationalizes them at the level of individual
evaluated workflows.
Architecture, tool access, or final performance alone cannot determine
what operations a system performed, what evidence supported its actions and
claims, or what assurance its evaluation established. Systems with similar
architectures may provide substantially different forms of assurance, whereas
systems with different architectures may expose comparable workflow traces,
evidence records, and validation procedures. We therefore treat the inspectable
workflow trajectory, rather than the architecture or final answer alone, as the
primary unit of analysis. Table S2 places this perspective relative to recent
reviews.
Received:Date Month Year.Revised received:Date Month Year.Accepted:Date Month Year
©The Author(s) 2026. Copyright and licence statements to be updated by the publisher during production.
arXiv:2607.27556v1  [cs.AI]  30 Jul 2026

2 Agentic Bioinformatics through Function, Evidence, and Validation, 2026, Volume , Issue
Biological
Question
Planner /
Coordinator
Agents
Experimental
Execution
Verification
Gate
Specialist Agents
Accumulated Experimental Knowledge
T ools
 Knowledge
Sources
Human Expert
Expert Review
Replanning Refinement
Protocol Guidance
Figure S1 Conceptual overview of agentic bioinformatics.High-level biological questions and/or input data are translated by planner or coordinator agents
into coordinated actions across specialist agents, external tools, and knowledge sources. Intermediate outputs pass through a verification gate informed by
accumulated experimental knowledge or memory and expert review, enabling iterative replanning and refinement. Depending on workflow scope and the
assurance established for the evaluated use case, outputs may support computational interpretation, protocol guidance, or empirically grounded execution.
Table S1 Functional distinction among bioinformatics copilots, workflow engines, and agentic bioinformatics layers.The categories describe workflow
roles and are not mutually exclusive.
Dimension Bioinformatics copilot Workflow engine Agentic bioinformatics layer
Primary role Assists user-led analysis. Executes predefined workflows. Adaptively controls scientific workflows.
InputPrompts, documents, or code. Data, scripts, parameters, and
environments.
Biological objectives, data, evidence, constraints, and
tools.
Output Suggestions, explanations, or code
snippets.
Outputs, logs, reports, and
intermediate files.
Plans, tool calls, artifacts, evidence records, and
interpretations.
PlanningPrimarily user-directed. Specified in advance. Goal-directed, multistep, and revisable.
Tool execution Optional or user-mediated. Central but predefined. Adaptive and responsive to workflow state.
Workflow stateMostly conversational and transient. Tracks predefined job execution. Tracks results, assumptions, failures, and pending
actions.
Traceability Usually limited. Strong execution provenance. Computational traces and evidentiary provenance.
VerificationPrimarily performed by the user. Checks execution and predefined
conditions.
Assesses outputs and escalates when evidence is
insufficient.
Typical failure Plausible but unsupported advice. Correct execution of an inappropriate
workflow.
Incorrect planning, evidence use, or insufficient
validation.
To address this gap, we introduce theFunction–Evidence–Validation(FEV)
framework as an accountability-oriented complement to existing application and
architectural taxonomies. Rather than asking only what an agent contains or
which task it completes, FEV asks what the reported workflow demonstrates
and what scientific conclusions that the workflow can support.
Functionrecords the workflow operations that a system demonstrably
performs, including planning, coordination, tool-mediated execution, workflow-
state and trace maintenance, repair, and verification or escalation.
Evidencerecords traceable literature, structured biological knowledge,
biological measurements and metadata, software and statistical outputs,
scientific-model outputs, and experimental or clinical observations supporting
workflow actions and claims.
Validationrecords the assurance established for the evaluated workflow
and its claims. These dimensions are complementary but non-interchangeable.
Broader Function does not imply stronger Evidence, and access to stronger
Evidence does not establish deeper Validation. For example, a published
experimental observation used by a workflow contributes to its Evidence profile,
whereas prospective testing of a workflow-generated output contributes to
Validation. Similarly, benchmark performance does not establish replayability
without identifiable inputs, parameters, dependencies, intermediate artifacts,
and execution traces. A complete FEV description combines a Function profile,
an Evidence profile, and a use-case-specific reported Validation stage. Function
and Evidence describe different workflow properties rather than ordinal levels
of maturity. Validation comprises five cumulative assurance stages: illustrative
output (V0), demonstrated execution (V1), replayable computation (V2),

Agentic Bioinformatics through Function, Evidence, and Validation, 2026, Volume , Issue3
Table S2Feature-based positioning of recent reviews of biological and bioinformatics agents. Symbols indicate whether each
feature is systematically operationalized (✓), explicitly discussed but not used as a principal system-level dimension (△), or
not separately operationalized (—). The comparison concerns analytical design rather than overall review quality.
Review
Application coverage
Architecture taxonomy
Capability taxonomy
Trajectory as unit
Explicit evidence profile
Replayability gate
Cumulative validation
Evidence–testing distinction
Standardized system coding
Zhou et al. (171)✓ ✓ ✓△ △— —△ △
Yang et al. (157)✓ ✓ ✓△ △— —△ △
Qi et al. (108)✓ ✓ ✓ ✓△ △ △ △✓
Dip et al. (28)✓ ✓ ✓ ✓△ △ △ △✓
Branda et al. (10)✓ ✓ ✓ ✓ ✓△ △ △ △
Present FEV review✓△✓ ✓ ✓ ✓ ✓ ✓ ✓
“Trajectory as unit” indicates that the inspectable sequence from a scientific objective to an evidence-supported conclusion is the primary unit of analysis.
“Replayability gate” separates demonstrated execution from computation reported with sufficient inputs, parameters, dependencies, artifacts, and traces for
reconstruction or replay. “Cumulative validation” requires each higher stage to satisfy the requirements of lower stages.
“Evidence–testing distinction” separates previously available empirical observations used as evidence from prospective testing of a workflow-generated output
and from closed-loop empirical refinement.
A dash does not imply complete absence of a topic; it indicates that the feature is not defined and applied as a distinct analytical component.
scientifically evaluated computation (V3), and prospective empirical evaluation
(V4). Each stage applies to a specific evaluated use case rather than an
entire platform. Separate qualifiers preserve the reported forms of assessment:
benchmark or baseline comparison, protocol-based human or expert assessment,
statistical or uncertainty analysis, robustness or failure analysis, external or
independent validation, prospective empirical testing, and closed-loop empirical
refinement. The stage and qualifiers reported should therefore be interpreted
together with the corresponding Function and Evidence profiles. Using FEV ,
we construct a structured cross-domain evidence map comprising 109 agentic or
agent-adjacent system entries and 28 benchmark or evaluation resources. Nine
publications contribute to both categories, yielding 128 unique publications
after accounting for overlap. The map spans genomics and gene editing,
single-cell and spatial omics, proteomics and protein design, drug discovery,
computational pathology and imaging, and general bioinformatics workflow
automation. It compares the reported workflow capabilities and forms of
scientific assurance rather than ranking systems, platforms, or biological fields.
Our contributions are fourfold:
• We define agentic bioinformatics as an adaptive workflow-control layer and
establish the inspectable workflow trajectory, rather than architecture or final
output alone, as the primary unit of analysis.
• We introduce FEV to separate demonstrated workflowFunction,
traceableEvidence, and use-case-specificValidation, thereby distinguishing
operational breadth from scientific assurance.
• We construct a cross-domain evidence map of 109 system entries and 28
benchmark or evaluation resources, representing 128 unique publications
after accounting for overlap.
• We derive a workflow-correctness agenda spanning analytical appropriateness,
execution, replayability, provenance, evidentiary traceability, uncertainty,
robustness, external validation, expert escalation, and prospective empirical
testing.
Together, these contributions shift the evaluation of agentic bioinformatics
from asking onlywhat an agent can doto askingwhat scientific conclusions its
reported workflow can support.
From Bioinformatics Copilots to Agentic
Bioinformatics
Large language models increasingly provide natural-language access to
biological data, analytical software, databases, and scientific literature (69; 28).
Many applications function asbioinformatics copilots, assisting user-directed
analysis through scripting, visualization, retrieval, and interpretation while
leaving the biological objective, analytical design, tool selection, and execution
primarily under human control (140; 134; 135). Although such systems can
reduce computational barriers, they generally do not maintain or adapt a
persistent scientific workflow.
Conventional workflow engines address a complementary problem.
Frameworks such as Nextflow and nf-core provide dependency management,
environment specification, scalable execution, and provenance for predefined
pipelines (26; 62). They improve procedural reproducibility, but generally do
not determine whether a workflow, method, or parameterization is appropriate
for the biological objective. A workflow engine can therefore execute an
analytically inappropriate pipeline correctly.
Anagentic bioinformatics layeradds adaptive workflow control. It interprets
biological objectives, decomposes them into computational tasks, selects and
invokes tools, maintains the workflow state, inspects intermediate outputs,
responds to failures, and determines when additional evidence, revision, or
review is required (118; 171; 28). Rather than replacing workflow engines, this
layer can use them as execution substrates while providing planning, evidence
integration, and workflow-level decision-making. Table S1 summarizes these
distinctions. The categories are functional rather than mutually exclusive:
a platform may combine conversational assistance, predefined workflow
execution, and agentic control across different tasks.
For this review, a full agentic bioinformatics layer demonstrates three
minimum capabilities:
1.Goal-directed multistep control:translation of a biological objective into
an ordered and revisable computational plan;

4 Agentic Bioinformatics through Function, Evidence, and Validation, 2026, Volume , Issue
2.Stateful tool-mediated execution:invocation or coordination of analytical
tools while retaining sufficient workflow state to interpret intermediate
outputs and respond to failures; and
3.Inspectable scientific support:preservation of explicit evidence,
execution traces, verification outputs, or escalation records beyond single-
turn response generation.
Systems demonstrating only a subset of these capabilities are retained as
agent-adjacentwhen they provide relevant evidence for the emerging workflow
paradigm. This boundary captures the transition from interactive assistance
to adaptive workflow control without assuming that planning, tool access, or
multi-agent architecture alone establishes scientific reliability. Unless otherwise
stated, aggregate analyses include both full agentic and agent-adjacent system
entries retained in the evidence map.
A Three-Dimensional Framework for Scientific
Workflow Accountability
The Function–Evidence–Validation (FEV) framework characterizes the
scientific accountability of agentic bioinformatics workflows through three
complementary but non-interchangeable dimensions.Functiondescribes the
workflow operations demonstrated by a system. Theevidencedescribes the
traceable sources used to inform these operations and support the resulting
interpretations.Validationdescribes the procedures used to test whether
workflow outputs and scientific claims are reliable. Figure S2 provides an
integrated overview of these three dimensions. The dimensions represent
different analytical views of the same workflow trajectory rather than sequential
processing stages. Greater functional capability does not imply stronger
evidence grounding, and access to stronger evidence does not by itself constitute
deeper validation. A complete FEV description therefore combines a Function
profile, an Evidence profile, and a use-case-specific reported Validation stage.
Function: Demonstrated Workflow Operations
The Function dimension characterizes the workflow operations that an agentic
system demonstrably performs. This dimension is architecture-agnostic: a
system may be implemented as a single agent, a multi-agent team, a tool-
augmented language model, or a hybrid workflow controller. Its Function profile
is determined by observable workflow behavior rather than by model family,
agent count, or architectural label.
Across the reviewed systems, six recurring dimensions emerge: planning
and task decomposition; role specialization and coordination; tool selection
and workflow execution; workflow-state maintenance and trace capture;
self-evaluation and repair; and verification and escalation. Together, these
dimensions describe how systems move from conversational assistance toward
adaptive workflow control. They are descriptive and non-ordinal: broader
Function profiles do not necessarily imply stronger evidence grounding,
replayability, or scientific Validation. Table S3 operationalizes each dimension
through an observable question, representative mechanisms, and its contribution
to the workflow.
Planning, coordination, and execution.
Planning requires more than generating a plausible list of analytical steps.
A planning-capable system translates a biological objective into an ordered
workflow, identifies inputs and dependencies, and revises its plan when
information is missing, execution fails, or intermediate results make the
initial strategy unsuitable. This distinction is particularly important in omics
workflows, where choices that involve quality control, normalization, sample
grouping, feature selection, and batch correction affect downstream inference
(173; 148; 82; 23).
Role specialization records whether the responsibilities for planning,
execution, biological interpretation, critique, or review are connected through
explicit task allocation, shared state, and interpretable handoffs (28; 11; 148).
The presence of multiple agents alone is insufficient to establish coordination.
Similarly, access to a tool library does not establish tool-mediated execution.
The system must select an appropriate tool, construct valid inputs, supply
parameters, monitor execution, parse its outputs, and pass the resulting artifacts
to subsequent workflow steps. Successful execution demonstrates operational
capability, but the suitability of the method and the resulting interpretation must
be assessed separately through Evidence and Validation (49; 86; 94; 40).
Workflow state and trace capture.
Long-running analyses require more than conversational memory. Workflow-
state maintenance allows a system to retain completed steps, intermediate
outputs, active assumptions, failures, and unresolved decisions. Trace capture
instead exposes what occurred through records such as tool calls, parameters,
software versions, dataset identifiers, intermediate artifacts, and output lineage.
The two functions are related, but not equivalent: a system may maintain
a rich internal state while exposing little usable provenance, whereas a
conventional workflow engine may preserve strong execution traces without
agent-like memory (30; 46; 58; 59). Function records whether state and traces
are captured; whether the reported records are sufficient to reconstruct or replay
the evaluated computation is determined under Validation.
Self-evaluation, repair, and verification.
Self-evaluation and repair require a system to detect an execution failure, weak
intermediate result, or unsupported interpretation and consequently modify its
plan, code, tool use, candidate selection, or interpretation. Relevant mechanisms
include execution monitoring, error diagnosis, critic feedback, tool substitution,
code correction, and replanning (158; 114; 87). The presence of a critic or
reflection component alone is insufficient, unless its assessment changes the
workflow or output.
Verification and escalation address a different question: is an intermediate
artifact, a final output, or a proposed claim sufficiently supported to proceed.
Verification may involve schema and file checks, analytical diagnostics,
biological plausibility assessment, evidence-coverage checks, uncertainty
signaling, clarification requests, refusal, or approval gates. Its result may allow
an output to proceed, flag or defer it, trigger an additional review, or lead
to escalation when available evidence is insufficient (95; 84). Verification as
a Function records that such an assessment occurs; whether the procedure
is scientifically adequate or improves reliability belongs to the Validation
dimension.
Together, the six dimensions form a profile of what a system can plan,
coordinate, execute, retain, repair, and verify. The breadth of the functions
describes the scope of the workflow rather than autonomy, quality, or
trustworthiness. A broadly capable system may rely on weak or poorly traceable
evidence, whereas a narrowly scoped system may provide strong Evidence and
Validation for a specific task. Function must therefore be interpreted jointly with
the sources supporting workflow actions and the assurance established for the
evaluated use case.
Evidence: Traceable Support for Workflow Actions and
Claims
The Evidence dimension characterizes the sources used to inform workflow
actions and support scientific interpretations. It is evaluated separately from
Function because planning, tool use, and report generation may still rely on
generic model priors, untraceable retrieval, inappropriate data, or unsupported
intermediate outputs.

Agentic Bioinformatics through Function, Evidence, and Validation, 2026, Volume , Issue5
WORKFLOW CONTEXT
(Input)
Biological objective
or scientific question
Datasets, samples,
metadata, and prior
results
User constraints,
preferences, and
resource limits
Prior knowledge,
assumptions, and
context
DIMENSION III - REPORTED
VALIDATION STAGE
 What assurance is established for the
evaluated use case ?
Prospective empirical
evaluation
Scientifically evaluated
computation
Replayable computation
Demonstrated execution
Illustrative output
V4
V3
V2
V1
V0
B H S R
X P C
VALIDATION QUALIFIERS
 (orthogonal to V-stage)
EVALUATED WORKFLOW TRAJECTORY
Objective
understanding
Planning and
task decomposition
Tool selection and
workflow execution
Intermediate
artifacts and states Claim / output
A concrete workflow or workflow component is executed by one or more agents
DIMENSION I - FUNCTION PROFILE
Which workflow operations are demonstrated ?
F1
Planning and
task decomposition
F2
Role specialization
and coordination
F3
Tool selection and
workflow execution
F4
Workflow-state
maintenance and
trace capture
F5
Self-evaluation and
repair
F6
Verification and
escalation
DIMENSION II - EVIDENCE PROFILE
Which traceable sources support actions and claims ?
E1
Scientific literature
E2
Structured biological
knowledge
E3
Biological data
E4
Software and
statistical outputs
E5
Scientific-model
outputs
E6
Experimental or
clinical observations
 Function and Evidence describe workflow scope and support, whereas
Validation determines whether the resulting outputs and claims have been adequately tested.
Qualifier describe how validation was
performed. They do not override unmet
cumulative-stage requirements.
Figure S2 Integrated overview of the Function–Evidence–Validation (FEV) framework for agentic bioinformatics.A biological objective, associated data and
metadata, user constraints, and prior context define the evaluated workflow trajectory.Function(F1–F6) describes the workflow operations demonstrated
by the system, including planning, coordination, tool-mediated execution, workflow-state and trace maintenance, self-evaluation and repair, and verification
or escalation.Evidence(E1–E6) identifies the traceable sources supporting workflow actions and scientific claims, including literature, structured biological
knowledge, biological measurements and metadata, software and statistical outputs, scientific-model outputs, and experimental or clinical observations.
Validationreports the cumulative assurance established for a specific evaluated use case, progressing from illustrative output (V0) and demonstrated execution
(V1) to replayable computation (V2), scientifically evaluated computation (V3), and prospective empirical evaluation (V4). Validation qualifiers specify the
reported forms of assessment: benchmark or baseline comparison (B), human or expert assessment (H), statistical or uncertainty analysis (S), robustness or
failure analysis (R), external or independent validation (X), prospective empirical testing (P), and closed-loop empirical refinement (C). Function and Evidence
are complementary profiles, whereas the reported V-stage is use-case-specific and does not constitute a global ranking of the system or platform.
Table S3 Function dimension of the FEV framework.The table summarizes observable workflow operations that an agentic bioinformatics system
may demonstrate; these capabilities do not constitute a maturity score.
Functional capability Operational question Typical mechanisms Workflow contribution
Planning and task decomposition Can the system translate a biological
objective into an ordered and revisable
plan?
Goal decomposition, dependency-aware planning,
step ordering, decision points, and replanning.
Converts biological intent into computational
subtasks.
Role specialization and
coordination
Can the system coordinate specialized
agents, modules, tools, or human
contributors?
Planner–executor–reviewer roles, specialist
modules, shared state, task allocation, and
explicit handoffs.
Coordinates biological reasoning, execution,
interpretation, and review.
Tool selection and workflow
execution
Can the system select, parameterize,
invoke, and monitor appropriate tools or
databases?
API calls, code execution, database queries,
parameter selection, output parsing, and
workflow-engine invocation.
Produces executable analyses and intermediate
artifacts.
Workflow-state maintenance and
trace capture
Can the system retain workflow context
and record what occurred?
Persistent task state, intermediate results, tool
logs, parameters, versions, dataset identifiers,
and artifact lineage.
Supports continuity, inspection, replay, and
audit.
Self-evaluation and repair Can the system detect failures or weak
outputs and revise its actions?
Execution monitoring, error diagnosis, critic
feedback, consistency checks, code repair, and
replanning.
Limits error propagation across multistep
analyses.
Verification and escalationCan the system assess output sufficiency
and determine when additional review is
required?
Tool checks, analytical diagnostics, plausibility
checks, uncertainty flags, refusal, clarification
requests, and approval gates.
Supports verification and appropriate
escalation.

6 Agentic Bioinformatics through Function, Evidence, and Validation, 2026, Volume , Issue
Table S4 Evidence dimension of the FEV framework.Evidence categories describe the sources supporting workflow actions and scientific claims; they
do not constitute an ordinal ranking.
Evidence category Workflow role Traceability requirement Principal limitations
Scientific literature Supports method selection, hypothesis
generation, and interpretation.
Citations, persistent identifiers, retrieved
passages, publication version, and retrieval
date.
Incomplete coverage, publication bias, outdated
findings, and weak dataset-specific support.
Structured biological knowledgeSupports entity normalization, annotation,
pathway reasoning, and known biological
relationships.
Database name and version, identifiers,
mappings, query records, and evidence
codes.
Curation lag, incomplete coverage, identifier
mismatch, and context-insensitive
relationships.
Biological measurements and
metadata
Supports dataset-specific analysis and empirical
inference.
Dataset accession, sample metadata, assay
description, preprocessing history, and data
lineage.
Noise, confounding, batch effects, missing
metadata, and preprocessing bias.
Software and statistical outputsSupports intermediate decisions, diagnostics,
repair, and downstream interpretation.
Tool and version, inputs, parameters,
execution logs, intermediate artifacts, and
output lineage.
Tool assumptions, invalid inputs, parameter
sensitivity, parsing errors, and silent failures.
Scientific-model outputs Supports prediction, simulation, representation,
ranking, or design.
Model and version, input representation,
inference settings, calibration status, and
output scores.
Distribution shift, miscalibration, model bias,
instability, and limited interpretability.
Experimental or clinical
observations
Provides empirical context, corroboration, or
feedback for computational claims.
Protocol, sample or cohort definition,
endpoint, assay conditions, provenance,
and relation to the evaluated claim.
Cost, limited scale, protocol dependence,
measurement noise, and restricted
generalizability.
Across the reviewed systems, six recurring evidence categories emerge:
scientific literature; structured biological knowledge; biological measurements
and metadata; software and statistical outputs; scientific-model outputs; and
experimental or clinical observations. These categories form a descriptive
and non-ordinal Evidence profile. Their relevance depends on the workflow
and claim: literature may support method selection or interpretation,
biological measurements may support dataset-specific inference, and empirical
observations may provide context, corroboration, or feedback.
The quality of the evidence depends not only on source type but also
on traceability, specificity, independence, reliability, and analytical role. An
identifiable source may still be outdated, methodologically weak, contextually
irrelevant, or insufficiently specific to the evaluated claim. Evidence objects
should therefore remain linked to their origins and versions and be distinguished
according to whether they serve as inputs, intermediate artifacts, contextual
support, corroboration, or Validation targets. Table S4 summarizes these
categories, their workflow roles, traceability requirements, and principal
limitations.
Literature and structured biological knowledge.
The scientific literature supports method selection, hypothesis generation, and
biological interpretation, while databases, ontologies, pathway resources, and
knowledge graphs support entity normalization and relationship retrieval. These
sources can improve factual grounding and attribution, but their availability does
not make a claim self-validating. Their evidentiary value depends on the quality
of the source, the publication or database version, the mapping of the identifier,
the retrieval procedure and the relevance to the biological context evaluated
(76; 8; 97; 3; 92; 2). Systems should therefore preserve citations, retrieved
passages, database versions, identifiers, and query records while distinguishing
established findings from extrapolation and newly generated hypotheses.
Biological measurements and computational outputs.
Biological measurements provide dataset-specific evidence through sequencing
reads, expression matrices, variants, spatial coordinates, protein-abundance
measurements, images, perturbation readouts, or clinical variables. Their
interpretation depends on associated metadata, including sample identity, assay
type, tissue, treatment, batch, cohort definition, and experimental design.
Empirical origin does not guarantee reliability: noise, confounding, batch
effects, missing metadata, limited sample size, and preprocessing choices may
substantially affect downstream inference (162; 82; 88; 113). Software and
statistical outputs provide derived computational evidence, including quality-
control reports, alignments, fitted models, differential-expression results,
enrichment analyses, rankings, plots, and execution logs. These artifacts
often connect one workflow step to the next, but inherit the assumptions and
failure modes of the tools that produced them. Their interpretation therefore
requires identifiable inputs, software versions, parameters, execution status,
parsing procedures, and artifact lineage. Computational outputs should be
treated as provenance-bearing evidence objects rather than automatically correct
observations (59; 1; 26). Whether the preserved artifacts are sufficient to
establish replayability or scientific validity is determined separately under
Validation.
Scientific-model outputs.
Scientific models contribute to predictions, representations, simulations,
rankings, and design candidates. Examples include structure predictors, protein
language models, single-cell foundation models, variant-effect predictors,
docking systems, and generative molecular models (57; 70; 24; 41; 125; 17).
Such outputs can support candidate prioritization and hypothesis generation
but should not be treated as equivalent to biological observations. The systems
should record the model and version, the input representation, the inference
settings, the confidence or calibration information, and the status of each output
as a prediction. Additional computational or empirical testing belongs to the
Validation dimension.
Experimental or clinical observations.
Experimental and clinical observations include perturbation measurements,
binding or functional assays, clinical outcomes, and other empirical readouts
available to the workflow. These observations may serve as prior evidence,
retrospective corroboration, or feedback for subsequent planning. Their
presence does not, however, automatically establish prospective Validation.
Previously generated or published observations used by a workflow are coded
asE6. By contrast, prospective testing of an analysis, recommendation,
hypothesis, or design generated by the evaluated workflow contributes toV4and
qualifierP, provided that the test is aligned with the principal claim. Qualifier
Cis assigned only when the newly generated empirical result is returned to the

Agentic Bioinformatics through Function, Evidence, and Validation, 2026, Volume , Issue7
Table S5 Validation dimension of the FEV framework.V-stages represent cumulative assurance gates for a specific evaluated use case, not global
maturity rankings of entire platforms.
Stage Validation stage Minimum operational requirement Typical supporting evidence
V0 Illustrative output The system produces explanations, hypotheses,
recommendations, or workflow plans without demonstrated
reliable execution.
Prompt outputs, qualitative examples, illustrative plans,
screenshots, or informal expert impressions.
V1Demonstrated execution The system successfully invokes a tool, executes code,
completes a workflow component, or generates an expected
computational artifact.
Successful tool calls, completed scripts, example runs, execution
outputs, or case demonstrations.
V2 Replayable computation The system satisfies V1 and reports sufficient information to
replay the evaluated computation, including identifiable
inputs, parameters, dependencies, intermediate artifacts, and
execution traces.
Scripts, notebooks, workflow definitions, versioned
environments, parameter records, logs, intermediate files, and
replay checks.
V3Scientifically evaluated
computation
The system satisfies V2 and evaluates workflow outputs using
task-appropriate scientific checks beyond successful execution.
Relevant benchmarks or baselines, statistical diagnostics,
robustness analyses, external datasets, uncertainty
assessment, biological consistency checks, or protocol-based
expert evaluation.
V4 Prospective empirical evaluation The system satisfies V3 and prospectively tests an
agent-generated output using empirical evidence appropriate
to the principal scientific claim.
Perturbation experiments, binding or functional assays,
prospective preclinical or clinical evaluation, or
design–test–refine cycles.
system and changes a subsequent computational or experimental action. This
distinction separates access to empirical evidence from prospective testing and
genuine design–test–refine feedback.
Validation: Reported Assurance for Workflow Outputs and
Claims
The Validation dimension characterizes the assurance established for the outputs
and scientific claims of an evaluated workflow. It is distinct from Function,
which records demonstrated workflow operations, and Evidence, which records
the sources supporting workflow actions and interpretations. Validation instead
asks whether the workflow has been shown to execute, can be replayed, has
undergone task-appropriate scientific evaluation, or has received prospective
empirical support. This distinction is necessary because successful execution
does not establish scientific correctness. A workflow may run without error
while using inappropriate inputs, normalization procedures, sample groupings,
parameters, statistical assumptions, or biological interpretations. Similarly,
access to literature, databases, model predictions, or experimental observations
does not necessarily validate the current workflow or claim (84; 94; 40; 136).
We define five Validation stages, denotedV0–V4. These stages are cumulative
assurance gates for a specific evaluated use case:V1requires demonstrated
execution;V2additionally requires sufficient information for replay;V3
requires task-appropriate scientific evaluation; andV4requires prospective
empirical testing of an agent-generated output aligned with the principal claim.
The stages are not global certifications of entire platforms, and the same
system may satisfy different stages across tasks. Because a single stage cannot
represent every form of support, Validation qualifiers are recorded separately:
Bfor quantitative benchmark or relevant baseline comparison,Hfor protocol-
based human or expert assessment,Sfor statistical diagnostics, calibration, or
uncertainty analysis,Rfor robustness, sensitivity, ablation, or failure analysis,
Xfor external or independent validation,Pfor prospective empirical testing,
andCfor closed-loop empirical refinement. V-stages and qualifiers apply to
evaluated use cases and should be interpreted with the corresponding Function
and Evidence profiles.
Illustrative output and demonstrated execution.
AtV0, a system produces explanations, hypotheses, recommendations, or
workflow plans without demonstrated reliable execution. Such outputs may
support ideation but remain proposals rather than executed computational
artifacts. Qualitative examples, screenshots, and informal expert impressions
do not establish execution or scientific reliability. AtV1, at least one tool-
mediated operation or workflow component is successfully demonstrated, such
as a database query, tool call, executed script, notebook run, or expected
computational artifact. V1 establishes operational feasibility beyond text
generation, but not replayability or scientific appropriateness. Benchmark
performance may be recorded as a qualifier, but does not establish V2 without
sufficient information to replay the evaluated computation.
Replayable computation.
AtV2, an informed user should be able to reconstruct or replay the evaluated
analytical trajectory. Relevant information includes identifiable inputs, data and
metadata assumptions, parameters, software or model versions, dependencies,
executable workflow definitions, intermediate artifacts, and execution traces.
Containers and complete environment specifications provide strong support
but are not the only acceptable forms of replayability. Replayability supports
inspection, but does not establish scientific correctness. A replayable workflow
may still apply an inappropriate method, omit relevant covariates, use unstable
parameters, or over-interpret weak biological signals. Therefore, V2 establishes
reconstructability, while V3 requires evaluation of scientifically meaningful
properties of the workflow or claim.
Scientifically evaluated computation.
AtV3, the system satisfies V2-level replayability and evaluates its outputs using
scientific checks appropriate to the task and claim. These checks may include
relevant baselines, statistical diagnostics, uncertainty analysis, robustness or
sensitivity testing, external datasets, biological consistency assessment, or
expert evaluation under a defined protocol. V3 should not be assigned solely
because a publication reports an accuracy value, qualitative demonstration,
informal expert impression, or agreement with existing biological knowledge.
The evaluation must test a meaningful property of the workflow or claim
beyond successful execution. Because different forms of assessment provide
non-equivalent assurance, qualifiers should be reported explicitly. For example,
V3 [B,R]denotes benchmark and robustness support, whereasV3 [B,H,X]
additionally records protocol-based expert assessment and external validation.
Prospective empirical evaluation.
AtV4, an output generated by the evaluated workflow is tested prospectively
using empirical evidence aligned with its principal claim. Examples include

8 Agentic Bioinformatics through Function, Evidence, and Validation, 2026, Volume , Issue
testing a proposed guide RNA through gene editing, evaluating a designed
binder in a binding assay, or assessing a prioritized intervention in a prospective
preclinical or clinical study. Experimental data do not automatically establish
V4. Previously generated measurements used as workflow inputs belong to the
Evidence profile, while evaluation on archived experimental datasets remains
retrospective computational Validation. V4 requires a direct relationship
between the workflow-generated output and its prospective empirical test.
The scope of V4 is claim-specific. For example, confirmation of a designed
peptide’s secondary structure does not establish binding, biological function,
developability, or therapeutic utility. V4 therefore records empirical support for
the evaluated claim rather than global certification of the platform. Prospective
testing is also distinct from closed-loop refinement. A one-time empirical
test supports the qualifierP. QualifierCapplies only when the resulting
observation is returned to the system and changes a subsequent computational
or experimental action.
Validation qualifiers.
The V-stage identifies the highest cumulative assurance gate satisfied by the
evaluated use case, whereas qualifiers preserve the reported forms of support.
Qualifiers are descriptive and non-ordinal, and they do not override unmet
stage requirements. A system cannot satisfy V3 through benchmark or expert
assessment alone if the evaluated computation does not meet V2 replayability.
Validation therefore distinguishes whether an operation was demonstrated, the
computation can be replayed, its outputs were scientifically evaluated, and a
workflow-generated claim was prospectively tested. Function profiles, Evidence
profiles, V-stages, and qualifiers should be interpreted together rather than
collapsed into a single system score.
Cross-System Synthesis through the FEV Framework
Overall FEV landscape.
Figure S3 summarizes the 109 mapped system entries. Planning, tool-mediated
execution, workflow-state maintenance, and self-evaluation or repair are widely
represented, while role specialization and explicit verification or escalation are
less common. Evidence profiles are dominated by software outputs, structured
biological knowledge, and retrospective biological data; experimental or clinical
observations are comparatively rare. Most systems are classified as V3, while
only seven reach V4 and none are assigned V0. Benchmark comparison and
robustness analysis are the dominant Validation qualifiers, whereas prospective
testing and closed-loop refinement remain exceptional. The mapped landscape
is therefore driven primarily by evaluated computation rather than prospective
empirical closure. Domain-level differences reflect task definition, benchmark
availability, experimental cost, and claim scope rather than global differences in
scientific maturity.
Cross-domain differences.
Figure S4 compares the within-domain composition of Function, Evidence,
and Validation support. Planning is common across all domains, whereas
coordination, workflow-state capture, and verification are more unevenly
distributed. Tool-mediated execution and trace capture are especially prominent
in pathology, drug discovery, and general workflow automation but less
consistently reported in genomics. Explicit verification or escalation remains
uncommon in genomics, protein engineering, and single-cell or spatial analysis,
indicating that neither multi-agent organization nor formal verification is
universal among systems described as agentic or agent-adjacent.
Evidence profiles largely reflect data modality. Biological measurements are
prominent in single-cell, spatial, and imaging workflows, whereas scientific-
model outputs are especially common in pathology, protein engineering,
and drug discovery. Software and statistical outputs are nearly universal,
but experimental or clinical observations remain the least frequent Evidence
category across domains.
Benchmark comparison and robustness analysis are the most widespread
forms of Validation support. External evaluation is concentrated in single-
cell, spatial, and pathology systems, while statistical analysis and protocol-
based expert assessment remain unevenly reported. Prospective testing is
concentrated in protein engineering, with fewer examples in genomics and
general biomedical research; closed-loop empirical refinement appears in a
single mapped framework.
These domain profiles describe different forms of reported assurance rather
than rankings of scientific maturity. A V3 annotation workflow and a V3
therapeutic-design workflow satisfy the same cumulative gate but may rely
on different benchmarks, statistical checks, expert assessments, and external
datasets. Validation must therefore be interpreted relative to the intended use
and principal scientific claim.
Capability breadth and priorities for future systems.
Figure S5 examines the relationship between Function and Evidence breadth,
reported Validation, and the remaining cross-domain gaps.
As shown in panel a, most systems implement multiple Function and
Evidence dimensions, yet the majority remain at V3. Broader operational scope
therefore does not imply stronger scientific assurance: additional agents, tools,
databases, memory modules, or predictive models may expand a workflow
without establishing replayability, verification, or empirical support for its
principal claim.
Panel b reports an observed gap score, defined as one minus the within-
domain share reporting each capability or Validation practice. The largest
recurring gaps are related to prospective empirical testing and closed-loop
refinement, while verification, expert assessment, uncertainty analysis, and
external validation remain unevenly reported. These gaps are descriptive rather
than universal requirements and should be interpreted in relation to the scope,
intended use, and claim of the workflow.
Progress should therefore be assessed by workflow accountability rather
than by the number of agents or tools. Priorities include inspectable shared
state, provenance-preserving handoffs, explicit verification gates, calibrated
uncertainty, external evaluation, and claim-aligned prospective testing. Where
experimentation is feasible, empirical results should inform subsequent
candidate selection, experimental design, or analysis, enabling scientifically
accountable design–test–refine cycles.
The reported proportions describe the structured review sample rather
than the complete literature and depend on publication-level reporting.
Unreported or insufficiently documented capabilities were not coded. System-
level assignments and supporting details are provided in Supplementary Tables
S1–S28.
Evaluation, Trustworthiness, and Benchmarking
Evaluation of agentic bioinformatics must extend beyond final-answer quality
because biological conclusions emerge from workflows involving data
and metadata selection, method choice, parameterization, tool execution,
intermediate artifacts, statistical assumptions, and interpretation. A plausible
endpoint may therefore conceal an inappropriate analysis, lost provenance,
failed tool call, or unsupported biological claim. Recent benchmarks
increasingly assess process-level behavior, including planning, tool selection,
execution, artifact generation, failure recovery, citation grounding, and
trajectory completeness (9; 16; 94; 40; 136; 93). However, most remain
measures of computational competence rather than prospective biological,
clinical, or experimental validity.

Agentic Bioinformatics through Function, Evidence, and Validation, 2026, Volume , Issue9
(a)
F1 F2 F3 F4 F5 F6 E1 E2 E3 E4 E5 E60%
20%
40%
60%
80%
100%Share of systems
94%
43%
88%
81%
86%
38%
55%
91% 87%
99%
69%
28% (b)
V0 V1 V2 V3 V40
10
20
30
40
50
60
70
80Number of systems
0
15 18
69
7
(c)
0% 20% 40% 60% 80% 100%
Share of systems
Closed-loop refinement
Prospective testing
Human / expert
Statistics / uncertainty
External / independent
Robustness
Benchmark
1
6
27
37
39
80
86 (d)
0% 20% 40% 60% 80% 100%
Within-domain share
Genomics / CRISPR
Single-cell / spatial
Protein / proteomics
Drug discovery
Pathology / imaging
General workflows Stage
V1
V2
V3
V4
Figure S3 Cross-domain quantitative synthesis of the Function–Evidence–Validation landscape. (a)Overall prevalence of Function and Evidence dimensions
across the mapped systems.(b)Distribution of reported Validation stages; V0 is retained as part of the complete scale although no mapped system was
assigned to this stage.(c)Prevalence of Validation qualifiers, including benchmark comparison, expert assessment, statistical analysis, robustness testing,
external evaluation, prospective testing, and closed-loop refinement.(d)Within-domain composition of reported Validation stages. Counts and percentages
were derived from the system-level tables in Supplementary Section S2 and describe the structured review sample rather than the complete literature.
(a)
F1 F2 F3 F4 F5 F6
Function dimension
Genomics / CRISPR
Single-cell / spatial
Protein / proteomics
Drug discovery
Pathology / imaging
General workflows
 0%
20%
40%
60%
80%
100%
Share of systems (b)
E1 E2 E3 E4 E5 E6
Evidence dimension
Genomics / CRISPR
Single-cell / spatial
Protein / proteomics
Drug discovery
Pathology / imaging
General workflows
 0%
20%
40%
60%
80%
100%
Share of systems (c)
B H S R X P C
Validation qualifier
Genomics / CRISPR
Single-cell / spatial
Protein / proteomics
Drug discovery
Pathology / imaging
General workflows
 0%
20%
40%
60%
80%
100%
Share of systems
Figure S4 Cross-domain comparison of Function, Evidence, and Validation profiles. (a)Within-domain prevalence of Function dimensions F1–F6.(b)Within-
domain prevalence of Evidence dimensions E1–E6.(c)Within-domain prevalence of Validation qualifiers B, H, S, R, X, P, and C. Percentages were calculated
within each biological domain from the system-level tables in Supplementary Section S2. The panels describe differences in the composition of the mapped
sample and should not be interpreted as rankings of fields or prevalence estimates for the complete literature.
From Answer Correctness to Workflow Assurance
Answer correctness measures agreement with a reference answer or expert
judgment, whereas workflow assurance asks whether the actions producing
that answer were appropriate, inspectable, and sufficiently tested for the
claim being made. Relevant criteria include method selection, valid tool
inputs and parameters, required artifacts, trace completeness, evidentiary
attribution, failure detection, and uncertainty reporting. This distinction is
particularly important in long-horizon workflows, where a locally successful
but inappropriate step may invalidate downstream results.
Workflow assurance is also claim-dependent. A database lookup, raw-
data analysis, disease-mechanism claim, therapeutic recommendation, and
experimentally consequential design require different forms of support.
Benchmark results should therefore be interpreted relative to workflow scope,
risk, and intended use rather than treated as interchangeable measures of system
quality.

10 Agentic Bioinformatics through Function, Evidence, and Validation, 2026, Volume , Issue
(a)
0 1 2 3 4 5 6
Function breadth (number of F codes)
0
1
2
3
4
5
6Evidence breadth (number of E codes)
V0
V1
V2
V3
V4
V-stage (b)
F4 F5 F6 E6 H S R X P C
Capabilities and validation practices to strengthen
Genomics / CRISPR
Single-cell / spatial
Protein / proteomics
Drug discovery
Pathology / imaging
General workflows
 0%
20%
40%
60%
80%
100%
Observed gap (1 − share)
Figure S5 Capability breadth, reported Validation stage, and research gaps in agentic bioinformatics. (a)Relationship among Function breadth, Evidence
breadth, and reported Validation stage; marker size indicates the number of systems sharing each FEV profile.(b)Cross-domain gaps in workflow capabilities
and Validation practices, calculated as one minus the within-domain share reporting each dimension; darker cells indicate larger observed gaps. The analysis is
derived from the system-level tables in Supplementary Section S2 and highlights verification, prospective testing, and closed-loop refinement as priorities for
future agentic bioinformatics systems.
Under FEV , evaluation should report three complementary properties:
demonstrated workflow operations, the appropriateness and traceability of
supporting Evidence, and the Validation established for the evaluated use case.
These properties should not be collapsed into a single accuracy score. A system
may complete a task using an inappropriate method, retrieve relevant evidence
without preserving a replayable workflow, or perform strongly on a benchmark
without external or empirical validation.
Benchmark Design for Agentic Bioinformatics
The mapped resources suggest three complementary benchmark families.
Outcome-oriented benchmarksassess the correctness of an answer, prediction,
annotation, design, ranking, or report.Process-oriented benchmarksassess
planning, tool selection, parameterization, execution, artifact generation,
repair, citation grounding, and trajectory completeness.Domain-calibrated
benchmarkstest whether these behaviours are appropriate for particular settings,
including genomics, single-cell and spatial omics, protein design, drug
discovery, and computational pathology. Detailed benchmark profiles are
provided in Supplementary Tables S29–S33.
Effective benchmark suites should combine these families using realistic
multistep tasks with biological data, metadata constraints, software
dependencies, expected intermediate artifacts, and criteria for both
computational and biological outputs. Table S6 summarizes the principal task
types.
Benchmark tasks should combine deterministic grading of execution, files,
parameters, and artifacts with domain-sensitive assessment of biological
interpretation. They should also evaluate robustness under missing or
contradictory metadata, corrupted inputs, unavailable tools, software-version
changes, task reformulation, irrelevant retrieval, and conflicting evidence.
A correct endpoint should not receive full credit when required tools were
not invoked, evidence was fabricated, or the workflow cannot be replayed;
conversely, a well-documented trajectory does not compensate for an incorrect
biological conclusion. Finally, benchmark reports should state the claims that
their results cannot support. Performance in question answering, tool selection,
execution, or retrospective datasets does not establish prospective biological,
preclinical, or clinical utility. Evaluation should therefore identify the highest
Validation stage directly supported and the remaining requirements for external
or empirical testing.
Challenges and Future Directions
The FEV synthesis shows that planning, retrieval, and tool-mediated execution
are advancing more rapidly than replayability, formal verification, and
prospective empirical testing. Therefore, progress depends less on increasing the
number of agents or tools than on strengthening the accountability of workflow
actions, evidence, and claims.
Reliable and Replayable Workflows
Real bioinformatics workflows contain incomplete metadata, heterogeneous
files, missing dependencies, ambiguous objectives, and confounded study
designs. Future systems should validate inputs and assumptions, detect
underspecified tasks, recover from execution failures, and request clarification
or additional review when available evidence is insufficient. Robustness should
be tested under changes in metadata, task formulation, tool availability,
software versions, and biological domains rather than only on curated
demonstrations. Systems should also preserve the information required to
inspect and replay their workflows, including dataset identifiers, metadata,
analytical assumptions, tool calls, parameters, software and model versions,
generated code, intermediate artifacts, failures, repairs, and evidence links.
Agentic layers should be built on workflow engines, notebooks, containers,
provenance standards, and institutional infrastructure rather than replacing
them. Standardized interfaces for tools, artifacts, and evidence would improve
portability between models and laboratories.
Claim-Calibrated Validation and Empirical Closure
Validation requirements should be proportional to the claim. Database retrieval,
raw-data analysis, disease-mechanism inference, therapeutic recommendation,
and protein design require different forms of assurance. Computational
assessment may include relevant baselines, statistical diagnostics, uncertainty
analysis, robustness testing, external datasets, biological consistency checks,
and protocol-based expert review. Claims about biological function or
intervention also require prospective testing aligned with the principal claim.
Prospective testing should remain distinct from closed-loop refinement. A one-
time assay evaluates an agent-generated output, whereas a closed loop returns
the empirical result to the system and changes the next computational or
experimental action. Greater autonomy is not inherently preferable: requesting

Agentic Bioinformatics through Function, Evidence, and Validation, 2026, Volume , Issue11
Table S6Benchmark task types for evaluating agentic bioinformatics systems.
Benchmark task type What it evaluates Example bioinformatics task Failure modes captured
Workflow construction Ability to translate biological intent into an
appropriate analysis plan.
Design a differential-expression or single-cell
analysis workflow from a dataset description
and research question.
Wrong method choice, missing
preprocessing, ignored covariates, or
unsuitable analysis design.
Tool-mediated executionAbility to call tools, run code, and produce
expected artifacts.
Execute quality control, normalization, clustering,
enrichment, or variant-annotation steps.
Invalid tool calls, dependency failures,
malformed inputs, or incomplete
outputs.
Debugging and repair Ability to detect and recover from workflow
failures.
Fix broken scripts, missing packages, incorrect
file paths, or failed tool calls.
Superficial repair, repeated failures, or
silent output corruption.
Evidence-grounded
interpretation
Ability to connect results to biological evidence
without overclaiming.
Interpret gene-set enrichment, cell-type markers,
perturbation effects, or candidate targets.
Hallucinated claims, unsupported
mechanisms, or weak evidence
attribution.
Reproducibility challenge Ability to preserve sufficient information to replay
and audit the workflow.
Reproduce an analysis from agent-generated
scripts, logs, parameters, and outputs.
Missing provenance, untracked
versions, non-deterministic results, or
incomplete artifact lineage.
Validation and robustnessAbility to assess whether results are statistically
and biologically reliable.
Compare against baseline pipelines, test
parameter sensitivity, or assess biological
consistency.
Overfitting, unstable conclusions,
ignored uncertainty, or limited
biological plausibility.
clarification, refusing unsupported inference, or recommending additional
validation may represent more reliable scientific behavior.
Governance, Oversight, and Reporting Standards
The appropriate degree of autonomy should depend on the risk of workflow.
Exploratory analyses may permit broader automation, while patient-derived
data, clinical interpretation, therapeutic reasoning, gene editing, and
experimental design require stronger access controls, approval gates, audit
logs, privacy protections, and expert oversight. Human involvement should
be operationally defined by specifying which decisions require review and
how the intervention changes the workflow. A minimum reporting standard
should document workflow scope, models and tools, data and evidence
sources, parameters and environments, intermediate artifacts, failures and
repairs, approval points, reported Validation stage, and the specific forms of
computational or empirical support. The most valuable agentic bioinformatics
systems will therefore not necessarily be those with the greatest autonomy, but
those that accelerate scientific work while preserving replayability, evidentiary
traceability, uncertainty, appropriate oversight, and claim-calibrated Validation.
Conclusion
Agentic bioinformatics is extending biological computation from conversational
assistance toward adaptive workflow control. Its scientific value lies not
only in making analytical tools accessible through natural language, but
in translating biological objectives into workflows whose actions, evidence,
artifacts, and limitations can be inspected. The Function–Evidence–Validation
(FEV) framework separates three properties that should not be conflated: the
workflow operations a system demonstrates, the traceable evidence supporting
its decisions and claims, and the assurance established for its outputs. The
reviewed literature shows rapid progress in planning, retrieval, and tool-
mediated execution, but less consistent support for replayable computation,
evidentiary provenance, robust scientific evaluation, and prospective empirical
testing. The next stage of agentic bioinformatics therefore depends less
on maximizing autonomy than on strengthening scientific accountability.
Reliable systems should preserve inspectable workflow trajectories, distinguish
observations from predictions and hypotheses, expose uncertainty, support
meaningful human oversight, and apply validation appropriate to the claims
being made. Ultimately, agentic systems should be judged not only by the
answers they produce but also by whether the workflows supporting those
answers can be replayed, evaluated, challenged, and, where necessary, tested
empirically.
Key Points
• Agentic bioinformatics should be evaluated through inspectable workflow
trajectories rather than architecture or final answers alone.
• The Function–Evidence–Validation framework separates demonstrated
workflow operations, traceable evidentiary support, and use-case-specific
scientific assurance.
• Among 109 system entries, planning and tool-mediated execution are more
common than explicit verification, prospective testing, and closed-loop
refinement.
• Replayability, provenance-preserving evidence linkage, calibrated validation,
and expert escalation are priorities for scientifically accountable agentic
workflows.
Author Contributions
Phuc Pham: Conceptualization, Methodology, Investigation, Data curation,
Formal analysis, Visualization, Writing—original draft, Writing—review
and editing. Truong Son Hy: Conceptualization, Methodology, Supervision,
Writing—review and editing.
Funding
This work received no specific funding.
Conflict of Interest
The authors declare no competing interests.
Data Availability
All data supporting this review are derived from published sources cited in the
manuscript and Supplementary Material.

12 Agentic Bioinformatics through Function, Evidence, and Validation, 2026, Volume , Issue
References
1. The galaxy platform for accessible, reproducible, and collaborative data
analyses: 2024 update.Nucleic acids research, 52(W1):W83–W94, 2024.
2. Uniprot: the universal protein knowledgebase in 2025.Nucleic acids
research, 53(D1):D609–D617, 2025.
3. The gene ontology knowledgebase in 2026.Nucleic Acids Research,
54(D1):D1779–D1792, 2026.
4. Tejumade Afonja, Ivaxi Sheth, Ruta Binkyte, Waqar Hanif, Shubhi
Ambast, Charles Mwangi Kaumbutha, Matthias Becker, and Mario
Fritz. Llm4grn: Discovering causal gene regulatory networks with llms–
evaluation through synthetic data generation. InICLR 2025 Workshop on
Machine Learning for Genomics Explorations.
5. Gautam Ahuja, Alex Antill, Yi Su, Giovanni Marco Dall ˘2019Olio,
Sukhitha Basnayake, Göran Karlsson, and Parashar Dhapola. Multi-agent
ai enables evidence-based cell annotation in single-cell transcriptomics.
bioRxiv, pages 2025–11, 2025.
6. Samuel Alber, Bowen Chen, Eric Sun, Alina Isakova, Aaron J Wilk, and
James Zou. Cellvoyager: Ai compbio agent generates new insights by
autonomously analyzing biological data.Nature Methods, 23(4):749–759,
2026.
7. Abdel Rahman Alsabbagh, Mahmoud Zahran, Ali Balubaid,
Sumeer Ahmad Khan, Robert Lehmann, Xabier Martinez de Morentin,
Vincenzo Lagani, Narsis A Kiani, David Gomez-Cabrero, and Jesper
Tegnér. Tactic: An explainable multi-agent architecture for classification
& interpretable reasoning in spatial transcriptomics. InICML 2025
Generative AI and Biology (GenBio) Workshop.
8. Lameck Mbangula Amugongo, Pietro Mascheroni, Steven Brooks, Stefan
Doering, and Jan Seidel. Retrieval augmented generation for large
language models in healthcare: A systematic review.PLOS Digital Health,
4(6):e0000877, 2025.
9. Jonathan Bragg, Mike D’Arcy, Nishant Balepur, Dan Bareket, Bhavana
Dalvi, Sergey Feldman, Dany Haddad, Jena D Hwang, Peter Jansen,
Varsha Kishore, et al. Astabench: Rigorous benchmarking of ai agents
with a scientific research suite.arXiv preprint arXiv:2510.21652, 2025.
10. Francesco Branda, Mohamed M Ahmed, Massimo Ciccozzi, Pietro Hiram
Guzzi, and Fabio Scarpa. The next paradigm in bioinformatics: a review
of multi-agent systems and foundational models for end-to-end scientific
discovery.Briefings in Bioinformatics, 27(3):bbag245–bbag245, 2026.
11. Dechao Bu, Jingbo Sun, Kun Li, Zihao He, Wei Huang, Jinlin Hu,
Shanshan Zhang, Shuangshuang Lei, Peipei Huo, Zhihao Wang, et al.
Empowering ai data scientists using a multi-agent llm framework with self-
evolving capabilities for autonomous, tool-aware biomedical data analyses.
Nature Biomedical Engineering, pages 1–16, 2026.
12. He Cao, Siyu Liu, Fan Zhang, Zijing Liu, Hao Li, Bin Feng, Shengyuan
Bai, Leqing Chen, Kai Xie, and Yu Li. Mozi: Governed autonomy for drug
discovery llm agents.arXiv preprint arXiv:2603.03655, 2026.
13. Lei Cao, Yuntain Li, Hua Qin, Yanbang Shang, Yilin Zhang, Bogdan
Jovanovic, Lazar Djokic, Tianyi Xia, Luni Hu, Haiyang Hou, Xingxing
Ning, Li’ang Lin, Hao Qiu, Ziqing Deng, Yuxiang Li, Yong Zhang,
and Shuangsang Fang. Biomics: A foundational agent for grounded and
autonomous multi-omics interpretation.bioRxiv, 2026.
14. Jingyun Chen, Linghan Cai, Zhikang Wang, Yi Huang, Songhan Jiang,
Shenjin Huang, Hongpeng Wang, and Yongbing Zhang. Pathagent: Toward
interpretable analysis of whole-slide pathology images via large language
model-based agentic reasoning.arXiv preprint arXiv:2511.17052, 2025.
15. Yuheng Chen, Shi Han, Zitong Chao, Yuyao Liu, Fan Zhang, Hao
Chen, Jiguang Wang, Jiashun Xiao, and Can Yang. Stat: A multi-agent
framework for integrated and interactive spatial transcriptomics analysis.
bioRxiv, pages 2026–05, 2026.
16. Ziru Chen, Shijie Chen, Yuting Ning, Qianheng Zhang, Boshi Wang, Botao
Yu, Yifei Li, Zeyi Liao, Chen Wei, Zitong Lu, et al. Scienceagentbench:
Toward rigorous assessment of language agents for data-driven scientific
discovery. InInternational Conference on Learning Representations,
volume 2025, pages 96934–96990, 2025.
17. Jun Cheng, Guido Novati, Joshua Pan, Clare Bycroft, Akvil ˙e Žemgulyt˙e,
Taylor Applebaum, Alexander Pritzel, Lai Hong Wong, Michal Zielinski,
Tobias Sargeant, et al. Accurate proteome-wide missense variant effect
prediction with alphamissense.Science, 381(6664):eadg7492, 2023.
18. Jihye Choi, Nils Palumbo, Prasad Chalasani, Matthew M Engelhard,
Somesh Jha, Anivarya Kumar, and David Page. Malade: Orchestration
of llm-powered agents with retrieval augmented generation for
pharmacovigilance.arXiv preprint arXiv:2408.01869, 2024.
19. Olivier Cinquin. Chip-gpt: a managed large language model for robust data
extraction from biomedical database records.Briefings in bioinformatics,
25(2):bbad535, 2024.
20. Olivier Cinquin. Steering veridical large language model analyses by
correcting and enriching generated database queries: first steps toward
chatgpt bioinformatics.Briefings in Bioinformatics, 26(1):bbaf045, 2025.
21. Sarah Cohen-Boulakia, Khalid Belhajjame, Olivier Collin, Jérôme
Chopard, Christine Froidevaux, Alban Gaignard, Konrad Hinsen, Pierre
Larmande, Yvan Le Bras, Frédéric Lemoine, et al. Scientific workflows for
computational reproducibility in the life sciences: Status, challenges and
opportunities.Future Generation Computer Systems, 75:284–298, 2017.
22. Omar Coser. Elisa: An interpretable hybrid generative ai agent for
expression-grounded discovery in single-cell genomics. InThe 2026
Workshop on Generative and Agentic AI for Biology.
23. Raquel Cuevas-Diaz Duran, Haichao Wei, and Jiaqian Wu. Data
normalization for addressing the challenges in the analysis of single-cell
transcriptomic datasets.BMC genomics, 25(1):444, 2024.
24. Haotian Cui, Chloe Wang, Hassaan Maan, Kuan Pang, Fengning Luo, Nan
Duan, and Bo Wang. scgpt: toward building a foundation model for single-
cell multi-omics using generative ai.Nature methods, 21(8):1470–1480,
2024.
25. Bernardo P de Almeida, Guillaume Richard, Hugo Dalla-Torre,
Christopher Blum, Lorenz Hexemer, Priyanka Pandey, Stefan Laurent,
Chandana Rajesh, Marie Lopez, Alexandre Laterre, et al. A multimodal
conversational agent for dna, rna and protein tasks.Nature Machine
Intelligence, 7(6):928–941, 2025.
26. Paolo Di Tommaso, Maria Chatzou, Evan W Floden, Pablo Prieto Barja,
Emilio Palumbo, and Cedric Notredame. Nextflow enables reproducible
computational workflows.Nature biotechnology, 35(4):316–319, 2017.
27. Ning Ding, Shang Qu, Linhai Xie, Yifei Li, Zaoqu Liu, Kaiyan Zhang,
Yibai Xiong, Yuxin Zuo, Zhangren Chen, Ermo Hua, et al. Automating
exploratory proteomics research via language models.arXiv preprint
arXiv:2411.03743, 2024.
28. Sajib Acharjee Dip, Dipanwita Mallick, Uddip Acharjee Shuvo,
Shovito Barua Soumma, Fazle Rafsani, Bikash Kumar Paul, Nazifa
Ahmed Moumi, Shafayat Ahmed, and Liqing Zhang. Large language
model agents for biological intelligence across genomics, proteomics,
spatial biology, and biomedicine.Briefings in Bioinformatics,
27(2):bbag110, 2026.
29. Sajib Acharjee Dip and Liqing Zhang. Can lightweight llm agents improve
spatial transcriptomics annotation?bioRxiv, pages 2025–11, 2025.
30. Pengfei Du. Memory for autonomous llm agents: Mechanisms, evaluation,
and emerging frontiers.arXiv preprint arXiv:2603.07670, 2026.
31. Dionizije Fa, Marko Culjak, Bruno Pandza, and Mateo Cupic. Bioagent
bench: An ai agent evaluation suite for bioinformatics.arXiv preprint
arXiv:2601.21800, 2026.
32. Gabriele Fossi, Youssef Boulaimen, Leila Outemzabet, Nathalie Jeanray,
Stephane Gerart, Sebastien Vachenc, Joanna Giemza, and Salvatore Raieli.
Swiftdossier: tailored automatic dossier for drug discovery with llms and
agents.arXiv preprint arXiv:2409.15817, 2024.

Agentic Bioinformatics through Function, Evidence, and Validation, 2026, Volume , Issue13
33. Bowen Gao, Yanwen Huang, Yiqiao Liu, Wenxuan Xie, Wei-Ying Ma, Ya-
Qin Zhang, and Yanyan Lan. Pharmagents: Building a virtual pharma with
large language model agents.arXiv preprint arXiv:2503.22164, 2025.
34. Shanghua Gao, Ada Fang, Yepeng Huang, Valentina Giunchiglia, Ayush
Noori, Jonathan Richard Schwarz, Yasha Ektefaie, Jovana Kondic, and
Marinka Zitnik. Empowering biomedical discovery with ai agents.Cell,
187(22):6125–6151, 2024.
35. Shanghua Gao, Richard Zhu, Zhenglun Kong, Ayush Noori, Xiaorui Su,
Curtis Ginder, Theodoros Tsiligkaridis, and Marinka Zitnik. Txagent: an
ai agent for therapeutic reasoning across a universe of tools.arXiv preprint
arXiv:2503.10970, 2025.
36. Fukang Ge, Jiarui Zhu, Linjie Zhang, Haowen Xiao, Xiangcheng Bao,
Fangnan Xie, Danyang Chen, Yanrui Lu, Yuting Wang, Ziqian Guan,
et al. Autobinder agent: An mcp-based agent for end-to-end protein binder
design.arXiv preprint arXiv:2602.00019, 2026.
37. Alireza Ghafarollahi and Markus J Buehler. Protagents: protein discovery
via large language model multi-agent collaborations combining physics
and machine learning.Digital Discovery, 3(7):1389–1409, 2024.
38. Alireza Ghafarollahi and Markus J Buehler. Sparks: Multi-agent artificial
intelligence model discovers protein design principles.arXiv preprint
arXiv:2504.19017, 2025.
39. Juraj Gottweis, Wei-Hung Weng, Alexander Daryin, Tao Tu, Petar
Sirkovic, Artiom Myaskovsky, Grzegorz Glowaty, Felix Weissenberger,
Alessio Orlandi, Dan Popovici, et al. Accelerating scientific discovery
with co-scientist.Nature, pages 1–3, 2026.
40. Wenbin Guo, Minzhe Zhang, Bowei Han, Youjia Ma, Yang Leng,
Shishir Hebbar, Xiaoyuan Zhou, Wenhao Gu, Xiao Yang, and Shashi
Dhar. Promptbio-bench: Benchmarking llm-based bioinformatics agents
for end-to-end data analysis.bioRxiv, pages 2026–05, 2026.
41. Minsheng Hao, Jing Gong, Xin Zeng, Chiming Liu, Yucheng Guo, Xingyi
Cheng, Taifeng Wang, Jianzhu Ma, Xuegong Zhang, and Le Song. Large-
scale foundation model on single-cell transcriptomics.Nature methods,
21(8):1481–1491, 2024.
42. Minsheng Hao, Hanchen Wang, Gabriele Scalia, Aviv Regev, et al.
Perturboagent: An llm-based agent for designing iterative perturb-seq
experiments. InMachine Learning in Computational Biology, pages
44–64. PMLR, 2025.
43. Bing He, Chenchen Qin, Yu Zhao, Long-Kai Huang, Zihan Wu, Fang
Wang, Fandi Wu, Fan Yang, and Jianhua Yao. Functional protein
design and enhancement with ontology reinforcement iteration.Nature
Communications, 17(1):4158, 2026.
44. George Hong and Daniel Trejo Banos. Nano bio-agents (nba): Small
language model agents for genomics.arXiv preprint arXiv:2509.19566,
2025.
45. Elias Hossain, Mehrdad Shoeibi, Ivan Garibay, and Niloofar Yousefi.
Biogen: evidence-grounded multi-agent reasoning framework for
transcriptomic interpretation in antimicrobial resistance.Frontiers in
Bioinformatics, 6:1846404, 2026.
46. Yuyang Hu, Shichun Liu, Yanwei Yue, Guibin Zhang, Boyang Liu, Fangyi
Zhu, Jiahang Lin, Honglin Guo, Shihan Dou, Zhiheng Xi, et al. Memory
in the age of ai agents.arXiv preprint arXiv:2512.13564, 2025.
47. Chao Hui Huang. Qust-llm: Integrating large language models
for comprehensive spatial transcriptomics analysis.arXiv preprint
arXiv:2406.14307, 2024.
48. Di Huang, Hao Li, Wenyu Li, Heming Zhang, Patricia Dickson, Ming
Zhan, J Philip Miller, Carlos Cruchaga, Michael Province, Yixin Chen,
et al. Omnicellagent: Towards ai co-scientists for scientific discovery in
precision medicine.bioRxiv, 2025.
49. Kexin Huang, Serena Zhang, Hanchen Wang, Yuanhao Qu, Yingzhou Lu,
Ryan Li, Yusuf Roohani, Lin Qiu, Shiyi Cao, Gavin Li, et al. Autonomous
biomedical research with an artificial intelligence agent.Science, page
eadz4351, 2026.
50. Kexin Huang, Serena Zhang, Hanchen Wang, Yuanhao Qu, Yingzhou Lu,
Ryan Li, Yusuf Roohani, Lin Qiu, Shiyi Cao, Gavin Li, et al. Autonomous
biomedical research with an artificial intelligence agent.Science, page
eadz4351, 2026.
51. Wenxuan Huang, Mingyu Tsoi, Yanhao Huang, Xinjie Mao, Xue
Xia, Hao Wu, Jiaqi Wei, Yuejin Yang, Lang Yu, Cheng Tan,
et al. Harmonycell: Automating single-cell perturbation modeling under
semantic and distribution shifts.arXiv preprint arXiv:2603.01396, 2026.
52. Xiuyu Jiang, Liqin Tan, Jianhuan Cen, and Qingsong Zou. Molbench: A
benchmark of ai models for molecular property prediction. InInternational
Symposium on Benchmarking, Measuring and Optimization, pages 53–70.
Springer, 2023.
53. Qiao Jin, Yifan Yang, Qingyu Chen, and Zhiyong Lu. Genegpt:
augmenting large language models with domain tools for improved access
to biomedical information.Bioinformatics, 40(2):btae075, 2024.
54. Ruofan Jin, Yucheng Guo, Yuanhao Qu, Ming Yang, Chun Shang, Qirong
Yang, Linlin Chao, Yi Zhou, Ruilai Xu, Ziyao Xu, et al. Biolab:
End-to-end autonomous life sciences research with multi-agents system
integrating biological foundation models.BioRxiv, pages 2025–09, 2025.
55. Ruofan Jin, Zaixi Zhang, Mengdi Wang, and Le Cong. Stella:
Self-evolving llm agent for biomedical research.arXiv preprint
arXiv:2507.02004, 2025.
56. Shreya Johri, Erica Maria Pimenta, Josephine Yates, Jingxin Fu, Erik L
Bao, Hyeji Jun, Brendan Reardon, Sasha Bacot, Maha Shady, Doris Fu,
et al. Evaluating agentic ai for biological discovery in autonomous and
copilot settings.bioRxiv, pages 2026–06, 2026.
57. John Jumper, Richard Evans, Alexander Pritzel, Tim Green, Michael
Figurnov, Olaf Ronneberger, Kathryn Tunyasuvunakool, Russ Bates,
Augustin Žídek, Anna Potapenko, et al. Highly accurate protein structure
prediction with alphafold.nature, 596(7873):583–589, 2021.
58. Sehrish Kanwal, Farah Zaib Khan, Andrew Lonie, and Richard O
Sinnott. Investigating reproducibility and tracking provenance–a genomic
workflow case study.BMC bioinformatics, 18(1):337, 2017.
59. Farah Zaib Khan, Stian Soiland-Reyes, Richard O Sinnott, Andrew Lonie,
Carole Goble, and Michael R Crusoe. Sharing interoperable workflow
provenance: A review of best practices and their practical application in
cwlprov.GigaScience, 8(11):giz095, 2019.
60. Hyomin Kim, Sang-Yeon Hwang, Jaechang Lim, Yinhua Piao, Yunhak
Oh, Woo Youn Kim, Chanyoung Park, Sungsoo Ahn, and Junhyeok Jeon.
Progressive multi-agent reasoning for biological perturbation prediction.
arXiv preprint arXiv:2602.07408, 2026.
61. Jeonghyeon Kim and Philip Romero. Benchmarking and behavioral
characterization of llm agents for protein design.bioRxiv, pages 2026–05,
2026.
62. Björn E Langer, Andreia Amaral, Marie-Odile Baudement, Franziska
Bonath, Mathieu Charles, Praveen Krishna Chitneedi, Emily L Clark,
Paolo Di Tommaso, Sarah Djebali, Philip A Ewels, et al. Empowering
bioinformatics communities with nextflow and nf-core.Genome Biology,
26(1):228, 2025.
63. Namkyeong Lee, Edward De Brouwer, Ehsan Hajiramezanali, Tommaso
Biancalani, Chanyoung Park, and Gabriele Scalia. Rag-enhanced
collaborative llm agents for drug discovery. InProceedings of the AAAI
Conference on Artificial Intelligence, volume 40, pages 561–569, 2026.
64. Haoyang Li, Weishen Pan, Suraj Rajendran, Chengxi Zang, and Fei Wang.
Empowering clinical trial design with agentic intelligence and real-world
data.Nature Communications, 17(1):5501, 2026.
65. Kun Li, Zhennan Wu, Shoupeng Wang, Jia Wu, Shirui Pan, and Wenbin
Hu. Drugpilot: Llm-based parameterized reasoning agent for drug
discovery.arXiv preprint arXiv:2505.13940, 2025.

14 Agentic Bioinformatics through Function, Evidence, and Validation, 2026, Volume , Issue
66. Loka Li, Duzhen Zhang, Xingbo Du, Leonard Song, Zixiao Wang,
Assanali Aukenov, Noel Thomas, Shakhnazar Sailaukan, Yonghan Yang,
Feilong Chen, et al. Bioxarena: Benchmarking llm agents on multi-modal
biomedical machine learning tasks.arXiv preprint arXiv:2605.15766,
2026.
67. Songhao Li, Jonathan Xu, Tiancheng Bao, Yuxuan Liu, Yuchen Liu,
Yihang Liu, Lilin Wang, Wenhui Lei, Sheng Wang, Yinuo Xu, et al. A
co-evolving agentic ai system for medical imaging analysis.arXiv preprint
arXiv:2509.20279, 2025.
68. Yuci Liang, Xinheng Lyu, Wenting Chen, Meidan Ding, Jipeng Zhang,
Xiangjian He, Song Wu, Xiaohan Xing, Sen Yang, Xiyue Wang, et al.
Wsi-llava: A multimodal large language model for whole slide image.
InProceedings of the IEEE/CVF International Conference on Computer
Vision, pages 22718–22727, 2025.
69. Anqi Lin, Junpu Ye, Chang Qi, Lingxuan Zhu, Weiming Mou, Wenyi Gan,
Dongqiang Zeng, Bufu Tang, Mingjia Xiao, Guangdi Chu, et al. Bridging
artificial intelligence and biological sciences: a comprehensive review of
large language models in bioinformatics.Briefings in Bioinformatics,
26(4):bbaf357, 2025.
70. Zeming Lin, Halil Akin, Roshan Rao, Brian Hie, Zhongkai Zhu, Wenting
Lu, Nikita Smetanin, Robert Verkuil, Ori Kabeli, Yaniv Shmueli, et al.
Evolutionary-scale prediction of atomic-level protein structure with a
language model.Science, 379(6637):1123–1130, 2023.
71. Zuwan Lin, Wenbo Wang, Arnau Marin-Llobet, Qiang Li, Samuel D
Pollock, Xin Sui, Almir Aljovic, Jaeyong Lee, Jongmin Baek, Ningyue
Liang, et al. Spatial transcriptomics ai agent charts hpsc-pancreas
maturation in vivo.bioRxiv, pages 2025–04, 2025.
72. Fengze Liu, Haoyu Wang, Joonhyuk Cho, Dan Roth, and Andrew Lo.
Autoct: Automating interpretable clinical trial prediction with llm agents.
InProceedings of the 2025 Conference on Empirical Methods in Natural
Language Processing, pages 30933–30958, 2025.
73. Haoyang Liu, Shuyu Chen, Ye Zhang, and Haohan Wang. Genotex: An
llm agent benchmark for automated gene expression data analysis, 2025.
74. Haoyang Liu, Yijiang Li, and Haohan Wang. Genomas: A multi-
agent framework for scientific discovery via code-driven gene expression
analysis.arXiv preprint arXiv:2507.21035, 2025.
75. Ruofan Liu, Pengcheng Chen, and Eric J Seibel. Lsm-copilot: A skill-flow
agent for fluorescence microscopy analysis. InFirst Workshop on Agent
Skills, 2026.
76. Siru Liu, Allison B McCoy, and Adam Wright. Improving large language
model applications in biomedicine with retrieval-augmented generation:
a systematic review, meta-analysis, and clinical development guidelines.
Journal of the American Medical Informatics Association, 32(4):605–615,
2025.
77. Sizhe Liu, Yizhou Lu, Siyu Chen, Xiyang Hu, Jieyu Zhao, Yingzhou
Lu, and Yue Zhao. Drugagent: Automating ai-aided drug discovery
programming through llm multi-agent collaboration.arXiv preprint
arXiv:2411.15692, 2024.
78. Wei Liu, Jun Li, Yitao Tang, Yining Zhao, Chaozhong Liu, Meiyi
Song, Zhenlin Ju, Shwetha V Kumar, Yiling Lu, Rehan Akbani,
et al. Drbioright 2.0: an llm-powered bioinformatics chatbot for large-
scale cancer functional proteomics analysis.Nature communications,
16(1):2256, 2025.
79. Yang Liu, Lu Zhou, Xiawei Du, Ruikun He, Xuguang Zhang, Rongbo
Shen, and Yixue Li. Benchmarking llm-based agents for single-cell omics
analysis.Genome Biology, 27(1):123, 2026.
80. Yungeng Liu, Zan Chen, Yu Guang Wang, and Yiqing Shen. Toursynbio-
search: A large language model driven agent framework for unified search
method for protein engineering. In2024 IEEE International Conference on
Bioinformatics and Biomedicine (BIBM), pages 5395–5400. IEEE, 2024.
81. Yungeng Liu, Zan Chen, Yuguang Wang, and Yiqing Shen.
Autoproteinengine: A large language model driven agent framework for
multimodal automl in protein engineering. InProceedings of the 31st
International Conference on Computational Linguistics: Industry Track,
pages 422–430, 2025.
82. Malte D Luecken and Fabian J Theis. Current best practices in
single-cell rna-seq analysis: a tutorial.Molecular systems biology,
15(6):MSB188746, 2019.
83. Xinheng Lyu, Yuci Liang, Wenting Chen, Meidan Ding, Jiaqi Yang, Guolin
Huang, Daokun Zhang, Xiangjian He, and Linlin Shen. Wsi-agents:
A collaborative multi-agent system for multi-modal whole slide image
analysis.arXiv preprint arXiv:2507.14680, 2025.
84. Chang Ma, Junlei Zhang, Zhihao Zhu, Cheng Yang, Yujiu Yang, Yaohui
Jin, Zhenzhong Lan, Lingpeng Kong, and Junxian He. Agentboard: An
analytical evaluation board of multi-turn llm agents.Advances in neural
information processing systems, 37:74325–74362, 2024.
85. Jiabo Ma, Cheng Jin, Yihui Wang, Hao Jiang, Ling Liang, Yingxue
Xu, Junlin Hou, Zhengrui Guo, Zhengyu Zhang, Yifei Xia, et al.
Democratizing and accelerating ai-driven pathology research through
agentic intelligence.arXiv preprint arXiv:2606.20677, 2026.
86. Youjia Ma, Bo-Wei Han, Minzhe Zhang, Yang Leng, Wenhao Gu,
KC Shashidhar, and Xiao Yang. Toolsgenie 2.0: A scalable and extensible
multi-agent system for bioinformatics automation.bioRxiv, pages 2026–
01, 2026.
87. Aman Madaan, Niket Tandon, Prakhar Gupta, Skyler Hallinan, Luyu Gao,
Sarah Wiegreffe, Uri Alon, Nouha Dziri, Shrimai Prabhumoye, Yiming
Yang, et al. Self-refine: Iterative refinement with self-feedback.Advances
in neural information processing systems, 36:46534–46594, 2023.
88. Guangyao Mao, Yi Yang, Zhuojuan Luo, Chengqi Lin, and Peng
Xie. Spatialqc: automated quality control for spatial transcriptome data.
Bioinformatics, 40(8):btae458, 2024.
89. Marc Boubnovski Martell, Josefa Lia Stoisser, Lawrence Phillips, Aditya
Misra, Robert Kitchen, Jesper Ferkinghoff-Borg, Jialin Yu, Philip Torr,
and Kaspar Märtens. Causalpert: Grounding llm hypotheses in regulatory
networks for gene perturbation prediction. InICLR 2026 Workshop on
Machine Learning for Genomics Explorations.
90. Vlastimil Martinek, Andrea Gariboldi, Dimosthenis Tzimotoudis, Mark
Galea, Elissavet Zacharopoulou, Aitor Alberdi Escudero, Edward Blake,
David ˇCechák, Luke Cassar, Alessandro Balestrucci, et al. Agentomics:
an agentic system that autonomously develops novel state-of-the-art
solutions for biomedical machine learning tasks.Bioinformatics,
42(Supplement_1):btag250, 2026.
91. Nils Mechtel, Hugo Dettner Källander, Songtao Cheng, Hanzhao
Zhang, AI4Life Horizon Europe Program Consortium, and Wei Ouyang.
Bioengine: scalable execution and adaptation of bioimage ai through
agent-readable interfaces.bioRxiv, pages 2026–04, 2026.
92. Marija Milacic, Deidre Beavers, Patrick Conley, Chuqiao Gong, Marc
Gillespie, Johannes Griss, Robin Haw, Bijay Jassal, Lisa Matthews, Bruce
May, et al. The reactome pathway knowledgebase 2024.Nucleic acids
research, 52(D1):D672–D678, 2024.
93. Henry E Miller, Matthew Greenig, Benjamin Tenmann, and Bo Wang.
Bioml-bench: Evaluation of ai agents for end-to-end biomedical ml.
bioRxiv, pages 2025–09, 2025.
94. Ludovico Mitchener, Jon M Laurent, Alex Andonian, Benjamin Tenmann,
Siddharth Narayanan, Geemi P Wellawatte, Andrew White, Lorenzo Sani,
and Samuel G Rodriques. Bixbench: a comprehensive benchmark for llm-
based agents in computational biology.arXiv preprint arXiv:2503.00096,
2025.
95. Mahmoud Mohammadi, Yipeng Li, Jane Lo, and Wendy Yip. Evaluation
and benchmarking of llm agents: A survey. InProceedings of the 31st
ACM SIGKDD Conference on Knowledge Discovery and Data Mining V .

Agentic Bioinformatics through Function, Evidence, and Validation, 2026, Volume , Issue15
2, pages 6129–6139, 2025.
96. Devam Mondal and Atharva Inamdar. Seqmate: A novel large
language model pipeline for automating rna sequencing.arXiv preprint
arXiv:2407.03381, 2024.
97. Victor M Montori, Marek Smieja, and Gordon H Guyatt. Publication bias:
a brief review for clinicians. InMayo Clinic Proceedings, volume 75,
pages 1284–1288. Elsevier, 2000.
98. Sahar Almahfouz Nasser, Juan Francisco Pesantez Borja, Jincheng Liu,
Sandeep Manandhar, Shikhar Shiromani, Mohammad Tanvir Hasan,
Zenghan Wang, Suman Ghosh, Jinchu Li, Xuejian Xu, et al. Sage: Agentic
framework for interpretable and clinically translatable computational
pathology biomarker discovery.arXiv preprint arXiv:2602.00953, 2026.
99. Thao Nguyen and Heng Ji. Mollingo: Molecule-native representations for
llm-powered scientific agents.arXiv preprint arXiv:2605.27853, 2026.
100. Bo Ni and Markus J Buehler. Vibegen: Agentic end-to-end de novo protein
design for tailored dynamics using a language diffusion model.Matter,
9(5), 2026.
101. Zhangming Niu, Xianglu Xiao, Wenfan Wu, Qiwei Cai, Yinghui Jiang,
Wangzhen Jin, Minhao Wang, Guojian Yang, Lingkang Kong, Xurui Jin,
et al. Pharmabench: Enhancing admet benchmarks with large language
models.Scientific Data, 11(1):985, 2024.
102. Seyednami Niyakan and Xiaoning Qian. Phenograph: A multi-agent
framework for phenotype-driven discovery in spatial transcriptomics data
augmented with knowledge graphs.bioRxiv, pages 2025–06, 2025.
103. Nima Nouri, Ronen Artzi, and Virginia Savova. An agentic ai framework
for ingestion and standardization of single-cell rna-seq data analysis.npj
Artificial Intelligence, 2(1):8, 2026.
104. Song Ouyang, Zhijie Dong, Yong Luo, Kehua Su, Huangxuan Zhao,
Miaojing Shi, and Bo Du. Pdagent: An llm-driven autonomous agent
framework towards* in silico* protein design via directed mutation. In
Forty-third International Conference on Machine Learning.
105. Joshua Pickard, Ram Prakash, Marc Andrew Choi, Natalie Oliven, Cooper
Stansbury, Jillian Cwycyshyn, Nicholas Galioto, Alex Gorodetsky, Alvaro
Velasquez, and Indika Rajapakse. Automatic biomarker discovery and
enrichment with brad.Bioinformatics, 41(5):btaf159, 2025.
106. Manvitha Ponnapati, Sam Cox, Cade W Gordon, Michael J Hammerling,
Siddharth Narayanan, Jon M Laurent, James D Braza, Michaela M Hinks,
Michael D Skarlinski, Samuel G Rodriques, et al. Proteincrow: A language
model agent that can design proteins. InICML 2025 Generative AI and
Biology (GenBio) Workshop, 2025.
107. Manvitha Ponnapati, Brian Lynch, and JOSEPH JACOBSON. Goagent:
Tool-orchestrating language agents for protein function annotation. InThe
2026 Workshop on Generative and Agentic AI for Biology.
108. Cong Qi, Wenbo Wang, Siqi Jiang, Qin Liu, Xun Song, Hanzhang Fang,
and Zhi Wei. Artificial intelligence agents for biological research: a survey.
Briefings in Bioinformatics, 27(1):bbag075, 2026.
109. Yuanhao Qu, Kaixuan Huang, Ming Yin, Kanghong Zhan, Dyllan Liu,
Di Yin, Henry C Cousins, William A Johnson, Xiaotong Wang, Mihir
Shah, et al. Crispr-gpt for agentic automation of gene-editing experiments.
Nature Biomedical Engineering, 10(2):245–258, 2026.
110. Sahil Rahman and Maxx Richard Rahman. Agentplm: Agentic protein
language models with reasoning-augmented decoding for protein sequence
design.arXiv preprint arXiv:2606.02386, 2026.
111. Mohammad R. Rezaei, Reza Saadati Fard, Jayson L. Parker, Rahul G.
Krishnan, and Milad Lankarany. Agentic medical knowledge graphs
enhance medical question answering: Bridging the gap between LLMs and
evolving medical knowledge. In Christos Christodoulopoulos, Tanmoy
Chakraborty, Carolyn Rose, and Violet Peng, editors,Findings of the
Association for Computational Linguistics: EMNLP 2025, pages 12682–
12701, Suzhou, China, November 2025. Association for Computational
Linguistics.
112. Yusuf Roohani, Andrew Lee, Qian Huang, Jian V ora, Zachary Steinhart,
Kexin Huang, Alexander Marson, Percy Liang, and Jure Leskovec.
Biodiscoveryagent: An ai agent for designing genetic perturbation
experiments. InInternational Conference on Learning Representations,
volume 2025, pages 26417–26466, 2025.
113. Agus Salim, Dharmesh D Bhuva, Carissa Chen, Chin Wee Tan, Pengyi
Yang, Melissa J Davis, and Jean YH Yang. Spanorm: spatially-
aware normalization for spatial transcriptomics data.Genome Biology,
26(1):109, 2025.
114. Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan,
and Shunyu Yao. Reflexion: Language agents with verbal reinforcement
learning.Advances in neural information processing systems, 36:8634–
8652, 2023.
115. Ksenia Sokolova, Sanketh Vedula, Keerthana Nallamotu, Guillermo
Sapiro, and Olga G Troyanskaya. Alvessa: An agentic evidence-grounded
research assistant for genomics. InNeurIPS 2025 AI for Science Workshop.
116. Haoyang Su, Shaoting Zhang, and Xiaosong Wang. Lammi-pathology:
A tool-centric bottom-up lvlm-agent framework for molecularly informed
medical intelligence in pathology.arXiv preprint arXiv:2602.18773, 2026.
117. Houcheng Su, Junning Feng, Yawen Lu, Yucheng Xu, Jinming Yang,
Haojie Lu, Jixin Yang, Xu Yang, Sirui Xie, Weicai Long, et al.
Biomaster: multi-agent system for automated bioinformatics analysis
workflow.Patterns, 2026.
118. Houcheng Su, Weicai Long, and Yanlin Zhang. Biomaster: Multi-agent
system for automated bioinformatics analysis workflow.bioRxiv, pages
2025–01, 2025.
119. Xiaorui Su, Yibo Wang, Shanghua Gao, Xiaolong Liu, Valentina
Giunchiglia, Djork-Arné Clevert, and Marinka Zitnik. Kgarevion: an ai
agent for knowledge-intensive biomedical qa. InInternational Conference
on Learning Representations, volume 2025, pages 40572–40599, 2025.
120. Jinyuan Sun, Auston Li, Yifan Deng, and Jiabo Li. Chatmol copilot:
An agent for molecular modeling and computation powered by llms. In
Proceedings of the 1st Workshop on Language+ Molecules (L+ M 2024),
pages 55–65, 2024.
121. Yuxuan Sun, Yixuan Si, Chenglu Zhu, Kai Zhang, Zhongyi Shui,
Bowen Ding, Tao Lin, and Lin Yang. Cpathagent: An agent-
based foundation model for interpretable high-resolution pathology image
analysis mimicking pathologists’ diagnostic logic.Advances in Neural
Information Processing Systems, 38:101673–101731, 2026.
122. Yuxuan Sun, Yunlong Zhang, Yixuan Si, Chenglu Zhu, Kai Zhang,
Zhongyi Shui, Jingxiong Li, Xuan Gong, Xinheng Lyu, Tao Lin, et al.
Pathgen-1.6 m: 1.6 million pathology image-text pairs generation through
multi-agent collaboration. InInternational Conference on Learning
Representations, volume 2025, pages 94611–94653, 2025.
123. Kyle Swanson, Wesley Wu, Nash L Bulaong, John E Pak, and James Zou.
The virtual lab of ai agents designs new sars-cov-2 nanobodies.Nature,
646(8085):716–723, 2025.
124. Xiangru Tang, Zhuoyun Yu, Jiapeng Chen, Yan Cui, Yanjun Shao,
Fang Wu, Kexu Li, Wangchunshu Zhou, Weixu Wang, Zhi Huang,
et al. scagents: A multi-agent framework for fully autonomous end-to-
end single-cell perturbation analysis. InICML 2025 Generative AI And
Biology (GenBio) Workshop, 2025.
125. Christina V Theodoris, Ling Xiao, Anant Chopra, Mark D Chaffin, Zeina R
Al Sayed, Matthew C Hill, Helene Mantineo, Elizabeth M Brydon, Zexian
Zeng, X Shirley Liu, et al. Transfer learning enables predictions in network
biology.Nature, 618(7965):616–624, 2023.
126. Florian Trost, Bide Zhang, Ines Aring, Marcus Bauer, Lennert Glamann,
Michael Wessolly, Kyra Johnson, Heike Göbel, Tristan Lerbs, Taban
Sangenne, et al. An agentic framework for autonomous scientific discovery
in cancer pathology.Nature Medicine, pages 1–13, 2026.

16 Agentic Bioinformatics through Function, Evidence, and Validation, 2026, Volume , Issue
127. Van Q Truong, Shu Yang, Li Shen, and Marylyn D Ritchie. A
comprehensive benchmark of tool-augmented large language models
for biomedical knowledge retrieval and integration. In2025 IEEE
International Conference on Bioinformatics and Biomedicine (BIBM),
pages 6599–6606. IEEE, 2025.
128. Rajat Vashistha, Sandra Brosda, Clemence J Belle, Lauren G Aoude, Nic
Waddell, Soumen Ghosh, Caroline Cooper, Andrew P Barbour, and Viktor
Vegh. Agent spi-wsi: In context learning for computationally spatial
pathway inferring on whole slide histopathology images conditioned on
bulk rna sequencing using pathologist in the loop.bioRxiv, pages 2025–10,
2025.
129. Thanh Hoa V o and Nguyen Quoc Khanh Le. Toward trustworthy artificial
intelligence in multi-omics: a review of reproducibility, stability, and
interpretability.Briefings in Bioinformatics, 27(3):bbag227, 05 2026.
130. Eric Wang, Samuel Schmidgall, Paul F Jaeger, Fan Zhang, Rory
Pilgrim, Yossi Matias, Joelle Barral, David Fleet, and Shekoofeh Azizi.
Txgemma: Efficient and agentic llms for therapeutics.arXiv preprint
arXiv:2504.06196, 2025.
131. Fiona Y Wang, Di Sheng Lee, David L Kaplan, and Markus J Buehler.
Swarms of large language model agents for protein sequence design with
experimental validation.arXiv preprint arXiv:2511.22311, 2025.
132. Hanchen Wang, Yichun He, Paula P Coelho, Matthew Bucci, Abbas
Nazir, Bob Chen, Linh Trinh, Serena Zhang, Kexin Huang, Vineethkrishna
Chandrasekar, et al. Spatialagent: An autonomous ai agent for spatial
biology.bioRxiv, pages 2025–04, 2025.
133. Jieyi Wang, Bingxuan Li, Nanyi Jiang, Desong Meng, Zirui Fan, Yuxin
Guo, Jiayu Liu, Kunlun Zhu, Eddie Yang, Xiusi Chen, et al. Bioinsight:
Multi-agent orchestration for interactive biomedical knowledge discovery.
arXiv preprint arXiv:2606.20997, 2026.
134. Jinge Wang, Zien Cheng, Qiuming Yao, Li Liu, Dong Xu, and Gangqing
Hu. Bioinformatics and biomedical informatics with chatgpt: Year one
review.Quantitative Biology, 12(4):345–359, 2024.
135. Lei Wang, Xijin Ge, Li Liu, and Gangqing Hu. Code interpreter for
bioinformatics: are we there yet?Annals of Biomedical Engineering,
52(4):754–756, 2024.
136. Liang Wang. Open-rosalind: tool-first biomedical llm agents with process-
aware benchmarking.bioRxiv, pages 2026–05, 2026.
137. Songhan Wang, Haoang Chi, He Li, Zhiheng Zhang, Jiayan Yuan, Cheems
Wang, Hao Peng, Xinwang Liu, and Wenjing Yang. Spacellagent: A self-
evolving llm-based multi-agent framework for trajectory analysis.arXiv
preprint arXiv:2607.07467, 2026.
138. Xiting Wang, Yuanrong Wang, Wenqing Dong, Shanshan Guo, Kai Wang,
Shuangshuang He, Yuqi Wang, Haorui Li, Jian Lyu, Meng Liu, et al. Tcm-
agent: Advancing network pharmacology and herbal medicine discovery
with llm-based multi-agent systems.Journal of Pharmaceutical Analysis,
page 101581, 2026.
139. Xuefei Wang, Jonathan Chen, Alexander R Farhang, Sophia Stiles, Kai A
Horstmann, Atharva Sehgal, Jonathan Light, David Van Valen, Yisong
Yue, and Jennifer J Sun. Agentic superoptimization of bioimaging analysis
workflows. InLLM for Scientific Discovery: Reasoning, Assistance, and
Collaboration.
140. Yongheng Wang, Weidi Zhang, Siyu Lin, Matthew S Farruggio, and
Aijun Wang. Bioinformatics copilot 1.0: A large language model-powered
software for the analysis of transcriptomic data.bioRxiv, pages 2024–04,
2024.
141. Zhenyu Wang, Zikang Wang, Jiyue Jiang, Pengan Chen, Xiangyu Shi, and
Yu Li. Large language models in bioinformatics: A survey. InFindings
of the Association for Computational Linguistics: ACL 2025, pages 3602–
3615, 2025.
142. Zhizheng Wang, Qiao Jin, Chih-Hsuan Wei, Shubo Tian, Po-Ting Lai,
Qingqing Zhu, Chi-Ping Day, Christina Ross, Robert Leaman, and
Zhiyong Lu. Geneagent: self-verification language agent for gene-set
analysis using domain databases.Nature Methods, 22(8):1677–1685,
2025.
143. Zifeng Wang, Zheng Chen, Ziwei Yang, Xuan Wang, Qiao Jin, Yifan
Peng, Zhiyong Lu, and Jimeng Sun. Empowering biomedical evidence
exploration and synthesis with deep knowledge graph research.Nature
Machine Intelligence, pages 1–15, 2026.
144. Luca L. Weishaupt, Chengkuan Chen, Drew F. K. Williamson, Richard J.
Chen, Guillaume Jaume, Tong Ding, Bowen Chen, Anurag Vaidya,
Long Phi Le, Guillaume Jaume, Ming Y . Lu, and Faisal Mahmood.
Evidence-based diagnostic reasoning with multi-agent copilot for human
pathology, 2026.
145. Kenny Workman, Zhen Yang, Harihara Muralidharan, Aidan Abdulali, and
Hannah Le. scbench: Evaluating ai agents on single-cell rna-seq analysis.
arXiv preprint arXiv:2602.09063, 2026.
146. Kenny Workman, Zhen Yang, Harihara Muralidharan, and Hannah Le.
Spatialbench: Can agents analyze real-world spatial biology data?arXiv
preprint arXiv:2512.21907, 2025.
147. Yuxuan Wu and Fuchou Tang. scextract: leveraging large language models
for fully automated single-cell rna-seq data annotation and prior-informed
multi-dataset integration.Genome Biology, 26(1):174, 2025.
148. Yihang Xiao, Jinyi Liu, Yan Zheng, Shaoqing Jiao, Jianye Hao, Xiaohan
Xie, Limingzhi, Ruitao Wang, Fei Ni, Yuxiao Li, Zhen Wang, Xuequn
Shang, Zhijie Bao, Changxiao Yang, and Jiajie Peng. Cellagent:
Llm-driven multi-agent framework for natural language-based single-
cell analysis. InInternational Conference on Learning Representations
(ICLR), 2026.
149. Yihang Xiao, Jinyi Liu, Yan Zheng, Xiaohan Xie, Jianye Hao, Mingzhi
Li, Ruitao Wang, Fei Ni, Yuxiao Li, Jintian Luo, et al. Cellagent: An
llm-driven multi-agent framework for automated single-cell data analysis.
arXiv preprint arXiv:2407.09811, 2024.
150. Elliot Xie, Lingxin Cheng, Jack Shireman, Yujia Cai, Jihua Liu, Chitrasen
Mohanty, Mahua Dey, and Christina Kendziorski. Cassia: a multi-agent
large language model for automated and interpretable cell annotation.
Nature Communications, 2025.
151. Qi Xin, Quyu Kong, Hongyi Ji, Yue Shen, Yuqi Liu, Yan Sun, Zhilin
Zhang, Zhaorong Li, Xunlong Xia, Bing Deng, et al. Bioinformatics
agent (bia): unleashing the power of large language models to reshape
bioinformatics workflow.BioRxiv, pages 2024–05, 2024.
152. Wei Xu, Gang Luo, Weiyu Meng, Xiaobing Zhai, Keli Zheng, Ji Wu,
Yanrong Li, Abao Xing, Junrong Li, Zhifan Li, et al. Mragent: an
llm-based automated agent for causal knowledge discovery in disease via
mendelian randomization.Briefings in Bioinformatics, 26(2):bbaf140,
2025.
153. Xiaopeng Xu, Chenjie Feng, Chao Zha, Wenjia He, Maolin He, Bin Xiao,
and Xin Gao. Proteinmcp: An agentic ai framework for autonomous
protein engineering.Protein Science, 35(4):e70547, 2026.
154. Zhengyang Xu, Han Li, Jingsong Liu, Linrui Xie, Xun Ma, Xin You,
Shihui Zu, Ayako Ito, Xinyu Hao, Hongming Xu, et al. Mmnavagent:
Multi-magnification wsi navigation agent for clinically consistent whole-
slide analysis.arXiv preprint arXiv:2603.02079, 2026.
155. Ei-Wen Yang and Enrique Velazquez-Villarreal. Ai-hope: an ai-driven
conversational agent for enhanced clinical and genomic data integration
in precision medicine research.Bioinformatics, 41(7):btaf359, 2025.
156. Jian Yang, Liqi Shu, Huilong Duan, and Haomin Li. Rdguru: a
conversational intelligent agent for rare diseases.IEEE Journal of
Biomedical and Health Informatics, 29(9):6366–6378, 2024.
157. Tiantian Yang, Yihang Xiao, Zhijie Bao, Jianye Hao, and Jiajie
Peng. The rise and potential opportunities of large language model
agents in bioinformatics and biomedicine.Briefings in Bioinformatics,
26(6):bbaf601, 2025.

Agentic Bioinformatics through Function, Evidence, and Validation, 2026, Volume , Issue17
158. Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik
Narasimhan, and Yuan Cao. ReAct: Synergizing reasoning and
acting in language models. InInternational Conference on Learning
Representations (ICLR), 2023.
159. Li Yiyao, Nirvi Vakharia, Weixin Liang, Aaron T Mayer, Ruibang Luo,
Alexandro E Trevino, and Zhenqin Wu. Omicsnavigator: an llm-driven
multi-agent system for autonomous zero-shot biological analysis in spatial
omics.bioRxiv, pages 2025–07, 2025.
160. Nicholas D Youngblut, Christopher Carpenter, Jaanak Prashar, Chiara
Ricci-Tam, Rajesh Ilango, Noam Teyssier, Silvana Konermann, Patrick D
Hsu, Alexander Dobin, David P Burke, et al. scbasecount: an ai agent-
curated, uniformly processed, and continually expanding single cell data
repository.bioRxiv, pages 2025–02, 2025.
161. Behnam Yousefi, Nora Constanze Laubach, Sven Heins, Lucia Testa,
Søren W Gersting, and Stefan Bonn. Biochemaigent: An ai-driven protein
modeling and docking framework for structure-based drug discovery.
bioRxiv, pages 2025–12, 2025.
162. Ying Yu, Yuanbang Mai, Yuanting Zheng, and Leming Shi. Assessing
and mitigating batch effects in large-scale omics studies.Genome biology,
25(1):254, 2024.
163. YuCheng Yuan, Yuanfeng Ji, Zhongxiao Li, and Ruijiang Li. Sp-mind: An
autonomous reasoning agent for spatial proteomics analysis. InForty-third
International Conference on Machine Learning.
164. Fan Zhang, Yalong Zhao, Weihan Zhang, and Lipeng Lai. Bioscientist
agent: Designing llm-biomedical agents with kg-augmented rl reasoning
modules for drug repurposing and mechanistic of action elucidation.
bioRxiv, pages 2025–08, 2025.
165. Haotian Zhang, Yu H Sun, Wenxing Hu, Xu Cui, Zhengyu Ouyang,
Derrick Cheng, Xinmin Zhang, and Baohong Zhang. Compbioagent: An
llm-powered agent for single-cell rna-seq data exploration.bioRxiv, pages
2025–03, 2025.
166. Lisheng Zhang, Lilong Wang, Xiangyu Sun, Wei Tang, Haoyang Su,
Yuehui Qian, Qikui Yang, Qingsong Li, Zhenyu Tang, Haoran Sun, et al.
Molclaw: An autonomous agent with hierarchical skills for drug molecule
evaluation, screening, and optimization.arXiv preprint arXiv:2604.21937,
2026.
167. Yiqing Zhang, Xiaozhong Liu, and Fabricio Murai. Pubmed reasoner:
Dynamic reasoning-based retrieval for evidence-grounded biomedical
question answering. InProceedings of the 64th Annual Meeting of the
Association for Computational Linguistics (Volume 1: Long Papers), pages
16753–16763, 2026.
168. Weike Zhao, Chaoyi Wu, Yanjie Fan, Pengcheng Qiu, Xiaoman Zhang,
Yuze Sun, Xiao Zhou, Shuju Zhang, Yu Peng, Yanfeng Wang, et al. An
agentic system for rare disease diagnosis with traceable reasoning.Nature,
651(8106):775–784, 2026.
169. Yue Zhao, Melih Yilmaz, Edward Lee, Chuanyui Teh, Lan Guo, Kemal
Sonmez, Luca Giancardo, Gordon Trang, Fangda Xu, Madelyn Espinosa-
Cotton, et al. Agent-guided de novo design of nanobody binders against a
novel cancer target.bioRxiv, pages 2026–04, 2026.
170. Fernando Zhapa-Camacho, Olga Mashkova, Robert Hoehndorf, and Maxat
Kulmanov.LLM Agent Based Protein Function Prediction, pages 508–
519.
171. Juexiao Zhou, Jindong Jiang, Zhongyi Han, Zijian Wang, and Xin Gao.
Streamline automated biomedical discoveries with agentic bioinformatics.
Briefings in Bioinformatics, 26(5):bbaf505, 2025.
172. Juexiao Zhou, Haoyang Li, Siyuan Chen, Zhangtianyi Chen, Zhongyi Han,
and Xin Gao. Large language models in biomedicine and healthcare.npj
Artificial Intelligence, 1(1):44, 2025.
173. Juexiao Zhou, Bin Zhang, Guowei Li, Xiuying Chen, Haoyang Li,
Xiaopeng Xu, Siyuan Chen, Wenjia He, Chencheng Xu, Liwei Liu, et al.
An ai agent for fully automated multi-omic analyses.Advanced Science,
11(44):2407094, 2024.
174. Xinyang Zhou, Yongyong Ren, Qianqian Zhao, Daoyi Huang, Xinbo
Wang, Tingting Zhao, Zhixing Zhu, Wenyuan He, Shuyuan Li, Yan Xu,
et al. An llm-driven multi-agent debate system for mendelian diseases.
arXiv preprint arXiv:2504.07881, 2025.
175. Yuyang Zhou, Jin Su, Jiawei Zhang, Wangyang Hu, Tianli Tao, Guanqi Li,
Xibin Zhou, Li Fan, and Fajie Yuan. Prime: A multi-agent environment for
orchestrating dynamic computational workflows in protein engineerings.
bioRxiv, pages 2025–09, 2025.
176. Kaiwen Zuo, Zixuan Zhong, Peizhou Huang, Shiyan Tang, Yuyan Chen,
and Yirui Jiang. Heal-kggen: A hierarchical multi-agent llm framework
with knowledge graph enhancement for genetic biomarker-based medical
diagnosis.bioRxiv, pages 2025–06, 2025.

18 Agentic Bioinformatics through Function, Evidence, and Validation, 2026, Volume , Issue
Supplementary Material
Supplementary Section S1. Scope and Literature
Selection Methodology
Review design and scope.This study presents a structured narrative review
and evidence map of emerging agentic bioinformatics systems. The review
was designed to support conceptual synthesis and cross-system comparison
rather than exhaustive systematic coverage or meta-analysis. We useagentic
bioinformaticsin a workflow-centered sense to describe computational systems
that coordinate biological objectives, data, models, databases, software tools,
and analytical actions across one or more stages of a scientific workflow.
Systems were considered agentic or agent-adjacent when they demonstrated
one or more substantive workflow-level capabilities beyond unconstrained
conversational response generation. These capabilities included biological-
goal interpretation, multi-step planning, task decomposition, adaptive retrieval,
tool or code execution, workflow-state maintenance, error repair, evidence-
grounded interpretation, verification, provenance capture, or coordination
among specialized agents or modules.
Information sources and temporal scope.Relevant studies were identified
through targeted searches of PubMed, Google Scholar, Semantic Scholar, arXiv,
bioRxiv, medRxiv, and major publisher or digital-library platforms, including
Oxford Academic, Nature Portfolio, ACM, IEEE, and Elsevier. The primary
search window covered January 2022 through July 2026. Earlier publications
were retained when needed to contextualize bioinformatics workflow execution,
reproducibility, provenance, retrieval, and verification. Peer-reviewed articles,
conference papers, and preprints were included because many systems in this
rapidly evolving field were initially reported outside archival journals.
Search strategy.Searches combined terms describing agentic-computing
paradigms with biological workflow domains. Agent-oriented terms included
“agentic bioinformatics”, “biological LLM agents”, “biomedical LLM agents”,
“multi-agent systems bioinformatics”, “autonomous bioinformatics agent”,
“tool-augmented LLM bioinformatics”, and “scientific discovery agents
biology”. Domain-oriented terms covered genomics, transcriptomics, single-
cell and spatial omics, proteomics, structural biology, protein design, gene
editing, drug discovery, computational pathology, biological imaging, and
general bioinformatics workflow automation. Additional searches used terms
related to workflow execution, benchmarking, provenance, reproducibility,
verification, error repair, and experimental validation. Backward and forward
citation tracing, together with targeted system-name searches, was used to
identify primary system papers, companion benchmarks, updated versions, and
additional studies referenced by recent reviews.
Eligibility criteria.We included AI-based systems, frameworks, benchmarks,
or workflow infrastructures applied to biological or biomedical computational
tasks when the publication reported sufficient information to characterize at
least one workflow-relevant agentic function, evidence source, or validation
procedure. The scope covered genomics, transcriptomics, multi-omics,
single-cell and spatial biology, proteomics, structural biology, protein
design, perturbation analysis, gene editing, drug discovery, therapeutic
reasoning, computational pathology, biological imaging, biomedical data
analysis, and general bioinformatics workflow automation. We excluded purely
conversational or educational LLM applications without substantive retrieval,
tool use, execution, verification, or evidence-grounded analysis; generic
agents without a biological or biomedical application; and conventional fixed
workflow engines that lacked adaptive biological-goal interpretation, planning,
or workflow-level decision-making. Duplicate preprint and journal versions
were consolidated under the most complete publication record. Systems
spanning multiple application areas were assigned to the domain representing
their primary workflow contribution to avoid duplicate system counts.
Counting and interpretation.The final evidence map contains 109 agentic
or agent-adjacent system entries and 28 benchmark or evaluation entries. Nine
publications introduce both a system and an associated benchmark or evaluation
resource; therefore, the complete map represents 128 unique publications. The
system and benchmark counts describe the composition of this structured review
sample and should not be interpreted as prevalence estimates in the complete
literature.
Supplementary Section S2. Domain-Specific FEV
System Maps
This section expands the representative mapping in the main text through
domain-specific system tables. All tables use a common set of columns
to compare demonstrated workflow Function, supporting Evidence, and
reported use-case-specific Validation. The tables also retain the task scope,
reported artifacts, provenance information, evaluation procedures, and principal
limitations needed to interpret each classification. The extended mapping is
organized into seven groups: Genomics, Transcriptomics, Perturbation, and
CRISPR Agents; Single-Cell, Spatial Biology, Cell Annotation, and Spatial-
Omics Agents; Proteomics, Structural Biology and Protein-Design Agents;
Drug Discovery, Therapeutic Reasoning, and Molecular Design Agents;
Computational Pathology, Microscopy, and Spatial Imaging Agents; General
Bioinformatics Workflow Agents and Automation Systems; and Benchmarks,
Evaluation Suites, and Workflow Infrastructure. Within each biological domain,
systems are ordered according to their primary contribution to the workflow
rather than alphabetically, chronologically, or by assumed maturity ranking.
The tables generally progress from data access, metadata curation, retrieval,
and interactive assistance to tool-mediated execution, analytical interpretation,
diagnostic or discovery-oriented reasoning, and, where reported, prospective
empirical evaluation. This ordering is intended to clarify differences in
workflow scope; it does not imply that a later system is globally more capable,
more reliable, or better validated than an earlier system. Systems spanning
multiple domains are assigned to the section that best represents their principal
contribution to workflow. Cross-domain capabilities are retained in their
Function and Evidence profiles rather than represented through duplicate system
entries whenever possible. Benchmark and evaluation resources are organized
separately by evaluation scope, including evidence retrieval and verification,
executable workflow completion, domain-specific analysis, robustness and
failure assessment, artifact generation, and execution-trajectory evaluation.
FEV profile notation.
Function profiles are coded asF1, planning and task decomposition;F2, role
specialization and coordination;F3, tool selection and workflow execution;F4,
workflow-state maintenance and trace capture;F5, self-evaluation and repair;
andF6, verification and escalation. Evidence profiles are coded asE1, scientific
literature;E2, structured biological knowledge;E3, biological measurements
and metadata;E4, software and statistical outputs;E5, scientific-model
outputs; andE6, experimental or clinical observations. Reported Validation
stages are coded asV0, illustrative output;V1, demonstrated execution;
V2, replayable computation;V3, scientifically evaluated computation; and
V4, prospective empirical evaluation. Validation qualifiers are coded as
B, quantitative benchmark or relevant baseline comparison;H, protocol-
based human or expert assessment;S, statistical diagnostics, calibration, or
uncertainty analysis;R, robustness, sensitivity, ablation, or failure analysis;
X, external or independent validation;P, prospective empirical testing; andC,
closed-loop empirical refinement. Function and Evidence codes are descriptive
and non-ordinal. Reported V-stages and qualifiers apply to specific evaluated
use cases and do not constitute global platform rankings. The V-stages are

Agentic Bioinformatics through Function, Evidence, and Validation, 2026, Volume , Issue19
cumulative, and the qualifiers do not override the unmet cumulative-stage
requirements. QualifierCis assigned only when a newly generated empirical
result is returned to the system and changes a subsequent computational or
experimental action.
Genomics, Transcriptomics, Perturbation, and CRISPR
Agents
Tables S7– S10 map systems spanning genomic data access, transcriptomic
analysis, evidence-grounded interpretation, diagnostic reasoning, perturbation
design, and CRISPR experiment support. Representative tasks include
sequencing-data processing, metadata extraction, genomic database querying,
differential-expression and gene–trait analysis, gene-set and regulatory-network
interpretation, rare-disease diagnosis, perturbation prioritization, and guide-
RNA design. The mapped systems range from agent-adjacent extraction or
prediction components to stateful, tool-executing workflows and experimentally
connected gene-editing systems.
Despite this diversity, the systems share several recurring workflow
requirements, summarized in Figure S6. A biological objective must be
translated into an appropriate analytical plan; sequencing, variant, phenotype,
cohort, and perturbation data must be linked to their metadata; and domain
tools must be selected and executed with traceable inputs, parameters, and
outputs. Subsequent analyses may involve differential expression, association
or survival modeling, regulatory-network inference, causal analysis, diagnostic
prioritization, or perturbation-response prediction. Resulting claims should
remain linked to identifiable molecular data, literature, databases, ontologies,
pathways, and computational artifacts.
Workflow-state maintenance, trace capture, verification, repair, and
escalation operate in these activities rather than as isolated final steps. Their
importance increases for diagnostic and intervention-oriented output, where
errors in sample grouping, genome building, batch handling, variant identity,
statistical assumptions, or evidence attribution can propagate into consequential
conclusions. Prospective empirical testing remains optional and relatively
uncommon; archived perturbation or clinical data contribute to the Evidence
profile but do not establish prospective Validation of a newly generated
recommendation.
Table S11 translates these recurring patterns into domain-specific design
requirements. It identifies the molecular inputs, metadata, analytical artifacts,
evidence links, execution records, verification outputs, and empirical readouts
that should remain inspectable. Together, the system maps, the synthesis figure
and the design-requirement table separate workflow functionality, evidentiary
traceability, and use-case-specific validation.
Single-Cell, Spatial Biology, Cell Annotation, and
Spatial-Omics Agents
Tables S12–S16 map systems spanning single-cell data access, spatial-
omics analysis, cell-type annotation, trajectory inference, cell–cell interaction
modelling, perturbation prediction, and autonomous biological discovery.
Representative tasks include public scRNA-seq dataset reuse, metadata
extraction, preprocessing and integration, reference-free annotation, spatial-
region analysis, ligand–receptor inference, pseudotime reconstruction,
perturbation-response modelling, and multiomic hypothesis generation. The
mapped systems range from natural-language data interfaces to stateful agents
that execute, evaluate, and repair single-cell and spatial workflows. Despite
this diversity, the systems share several recurring workflow requirements,
summarized in Figure S7.
Single-cell or spatial data must first be linked to their assay, sample, tissue,
species, condition, cohort, and study metadata. Cells and tissue regions
must then be represented through expression states, markers, clusters, spatial
coordinates, neighborhoods, tissue domains, and perturbation contexts. Domain
tools are subsequently executed for preprocessing, integration, annotation,
trajectory inference, cell–cell communication, segmentation, registration,
and spatial analysis. Resulting annotations and biological claims should
remain linked to marker evidence, reference atlases, pathway resources,
literature, analytical outputs, and spatial context. Workflow-state maintenance,
uncertainty assessment, critique, repair, verification, and provenance-preserving
reporting operate across these activities rather than as isolated final steps.
Their importance increases when systems infer cell identities, developmental
trajectories, regulatory programs, ligand–receptor interactions, perturbation
responses, or disease-associated spatial regions. Errors in sample metadata,
batch handling, marker selection, spatial alignment, neighborhood construction,
or annotation confidence can propagate into unsupported biological conclusions.
Prospective testing remains optional and relatively uncommon; archived
perturbation, spatial, or clinical observations contribute to the Evidence profile
but do not establish prospective Validation of a newly generated result.
Table S17 translates these recurring patterns into domain-specific design
requirements. It identifies the expression objects, sample metadata, marker
tables, spatial coordinates, neighborhood graphs, analytical outputs, annotation
scores, workflow traces, evidence links, and empirical readouts that should
remain inspectable. Together, the system maps, synthesis figure, and design-
requirement table separate workflow functionality, evidentiary traceability, and
use-case-specific validation.
Proteomics, Structural Biology, and Protein-Design Agents
Tables S18–S21 map systems spanning proteomics exploration, evidence-
grounded protein interpretation, molecular modelling, protein-engineering
workflow execution, de novo sequence design, binder optimization, and
experimentally evaluated nanobody or enzyme discovery. Representative
tasks include protein-database retrieval, functional-proteomics analysis, Gene
Ontology prediction, structure prediction, docking, molecular simulation,
sequence redesign, developability filtering, and functional assay validation. The
mapped systems range from interactive retrieval platforms to stateful design
agents and experimentally connected protein-engineering workflows.
Despite this diversity, the systems share several recurring workflow
requirements, summarized in Figure S8. Protein objectives must first be
translated into explicit sequence, structure, binding, function, stability, or
proteomics tasks. Proteins and candidate designs must then be represented
through identifiable sequences, structures, domains, complexes, assay
measurements, and design constraints. Domain tools are subsequently executed
for structure prediction, docking, sequence design, simulation, scoring,
visualization, and candidate filtering. Resulting claims should remain linked to
protein records, structural models, physical scores, proteomics measurements,
literature, and mechanistic evidence.
Workflow-state maintenance, design critique, quality control, candidate
filtering, repair, expert review, and provenance-preserving reporting operate
across these activities rather than as isolated final steps. Their importance
increases for functional or translational claims, where errors in sequence
identity, structure preparation, binding-site selection, scoring, conserved
residues, developability assessment, or assay interpretation can propagate into
unsupported candidate prioritization. Archived assay measurements contribute
to the Evidence profile but do not establish prospective Validation unless an
output generated by the evaluated workflow is directly tested.
Table S22 translates these recurring patterns into domain-specific design
requirements. It identifies the protein sequences, structures, proteomics
measurements, tool calls, simulation outputs, candidate rankings, design
traces, and experimental readouts that should remain inspectable. Together, the

20 Agentic Bioinformatics through Function, Evidence, and Validation, 2026, Volume , Issue
Table S7 Genomics, transcriptomics, perturbation, and CRISPR systems: retrieval, metadata, and foundational analysis.
System Task Function profile Evidence profile Reported V-stage and qualifiers
Retrieval, Metadata, and Foundational Analysis
ChIP-GPT (19) ChIP-seq and SRA
metadata extraction
Agent-adjacent; F1, F5.Structures
extraction requests and iteratively resolves
incomplete or inconsistent SRA metadata.
E1, E2, E4.SRA/GEO records, abstracts,
protocols, expertlabels, extractedfields, and
model outputs.
V1 [B,H].Evaluated against curated
metadata labels; replayable end-to-end
analysis is not established.
GeneGPT (53) Genomic database
QA and sequence
alignment
F1, F3.Decomposes genomic questions
into NCBI E-utilities or BLAST calls and
combines returned records.
E2, E4.NCBI Gene, SNP, OMIM,
Nucleotide, API calls, BLAST results, and
returned identifiers.
V2 [B].Code, benchmark data, API
trajectories, and returned records support
replay of GeneTuring and GeneHop tasks.
Nano Bio-Agent
(44)
Small-model genomic
question answering
F1, F3, F4.Classifies tasks, retrieves
plans, infers parameters, executes APIs,
and aggregates results through reusable
templates.
E2, E4, E5.NCBI records, API outputs,
execution traces, and small-language-model
or AlphaGenome predictions.
V1 [B,R].Benchmarked across tasks,
models, scales, runtime, memory, and cost;
complete replayability is not established.
ChatNT (25) Conversational
biological-sequence
prediction
Agent-adjacent predictive component.
Performs language-conditioned DNA, RNA,
and protein prediction without stateful tool
orchestration.
E3, E5.Biological sequences, model
predictions, confidence estimates, and
feature attributions.
V1 [B,S].Evaluated on multitask prediction,
calibration, and attribution benchmarks; V2
workflow replayability is not established.
SeqMate (96) RNA-seq
preprocessing and
differential expression
F1, F3.Plans and executes preprocessing,
alignment, quantification, differential
expression, filtering, and reporting.
E1, E2, E3, E4.FASTQ files, sample
metadata, reference genomes, QC reports,
alignments, count matrices, differential-
expression results, and retrieved knowledge.
V1.End-to-end execution is demonstrated,
but versioned environments, complete
parameters, traces, andreplaychecksarenot
reported.
Table S8 Genomics, transcriptomics, perturbation, and CRISPR systems: executable transcriptomic workflows.
System Task Function profile Evidence profile Reported V-stage and qualifiers
Executable Transcriptomic Workflows
GenoAgent (73) Gene-expression and
gene–trait analysis
F1, F2, F3, F4, F5.Coordinates dataset
selection, preprocessing, modelling, code
review, debugging, and gene prioritization.
E2, E3, E4.GEO/TCGA data, clinical
metadata, genomic databases, generated
code, regression outputs, and ranked genes.
V2 [B,R].GenoTEX provides identifiable
data, expert workflows, execution artifacts,
quantitative evaluation, and ablations.
GenoMAS (74) Code-driven gene–
trait discovery
F1, F2, F3, F4, F5.Generates and executes
analysis code while using shared state,
review, backtracking, and correction.
E2, E3, E4.Expression and clinical
data, identifier resources, generated code,
statistical models, ranked genes, and review
traces.
V3 [B,S,R].Evaluated through GenoTEX,
confounder-aware modelling, execution
analysis, baselines, ablations, and memory-
reuse experiments.
BIOGEN (45) Evidence-grounded
transcriptomic
interpretation
F1, F2, F4, F5, F6.Coordinates retrieval,
interpretation, and critics; preserves
intermediate evidence and flags weak
support.
E1, E2, E3, E4.RNA-seq modules,
PubMed and UniProt records, enrichment
outputs, semantic metrics, critic scores, and
traceability reports.
V3 [B,S,R,X].A reproducible local
implementation is evaluated on five
bacterial RNA-seq datasets using baselines,
grounding metrics, ablations, sensitivity
analyses, and cross-organism tests.
LLM4GRN (4) Gene-regulatory-
network inference
Agent-adjacent; F1.Generates candidate
regulatory edges and combines them with
statistical network inference.
E2, E3, E4, E5.Expression data,
transcription-factor lists, biological
knowledge, inferred networks, and synthetic-
data outputs.
V1 [B,S].Evaluated using synthetic-data
similarity and biological metrics; a replayable
multistep workflow is not demonstrated.
GeneAgent (142) Gene-set
interpretation with
verification
F1, F3, F5.Generates interpretations,
verifies claims through domain databases,
and revises unsupported statements.
E1, E2, E4.Gene sets, pathway and disease
databases, literature, enrichment outputs,
and verification reports.
V2 [B,H].Evaluated on 1,106 gene sets with
identifiable queries, verification outputs,
quantitative metrics, and expert review.
MRAgent (152) Mendelian-
randomization causal
analysis
F1, F3, F4, F5, F6.Retrieves GWAS data,
executes MR analyses, checks reporting
quality, and produces reviewed causal
reports.
E1, E2, E3, E4.PubMed/PMC,
OpenGWAS, UMLS, MR estimates,
sensitivity analyses, STROBE-MR checks,
and reports.
V3 [B,H,S].Evaluated across retrieval,
dataset selection, statistical execution,
sensitivity analysis, reporting, baselines, and
expert review.
AI-HOPE (155) Clinical-genomic
association and
survival analysis
F1, F3, F4.Executes cohort selection,
association testing, variable scanning,
survival analysis, and reporting.
E1, E3, E4.TCGA genomic and clinical
data, association statistics, odds ratios,
hazard ratios, Kaplan–Meier outputs, and
literature.
V2 [S].Provides executable analyses on
identifiable retrospective datasets, but
evaluation is limited to selected case studies.
system maps, synthesis figure, and design-requirement table separate workflow
functionality, evidentiary traceability, and use-case-specific validation.
Drug Discovery, Therapeutic Reasoning, and Molecular
Design Agents
Tables S23– S25 map systems spanning target assessment, drug repurposing,
mechanism-of-action reasoning, therapeutic recommendation, predictive
modelling, molecular design, pharmacovigilance, and target-trial emulation.
Representative tasks include target-dossier generation, drug–disease prioritization,
ADMET and drug–target prediction, molecular screening and optimization,
adverse-event extraction, clinical-trial outcome prediction, and causal analysis
of real-world clinical data. The mapped systems range from evidence-retrieval
assistants to stateful agents that execute, evaluate, and revise computational or
clinical-analysis workflows.
Despite this diversity, the systems share several recurring workflow
requirements, summarized in Figure S9. Therapeutic objectives must first be
translated into explicit target-identification, molecular-design, safety, treatment,
or trial-analysis tasks. Drugs, targets, molecules, patients, cohorts, and trials
must then be represented through normalized identifiers, structures, indications,
endpoints, eligibility criteria, and safety attributes. Domain tools, databases,

Agentic Bioinformatics through Function, Evidence, and Validation, 2026, Volume , Issue21
Table S9 Genomics, transcriptomics, perturbation, and CRISPR systems: evidence-grounded diagnostic reasoning.
System Task Function profile Evidence profile Reported V-stage and qualifiers
Evidence-Grounded Diagnostic Reasoning
HEAL-KGGen
(176)
Genetic-biomarker
diagnostic QA
F1, F2, F3, F5.Routes questions
to specialist agents, normalizes entities,
retrieves knowledge-graph evidence, and
verifies answers.
E1, E2, E4.Biomedical literature, medical
knowledge graphs, retrieved subgraphs, and
specialist-agent outputs.
V2 [B].Publiccode, requirements, testdata,
graph files, and instructions support replay
of the evaluated QA setting.
RDguru (156) Phenotype-grounded
rare-disease diagnosis
F1, F3, F4.Normalizes phenotypes,
combines diagnostic modules, maintains
differential state, and selects follow-up
questions.
E1, E2, E3, E4, E5.Clinical descriptions,
HPO terms, rare-disease databases, retrieval
outputs, and diagnostic rankings.
V1 [B].Evaluated on simulated and 238
retrospective cases; complete replayability
and prospective clinical validation are not
established.
MD2GPS (174) Mendelian diagnosis
and gene prioritization
F1, F2, F3, F5.Coordinates variant
annotation, gene–phenotype reasoning, and
multi-agent debate to rank candidate genes.
E2, E3, E4, E5.VCF and HPO inputs,
ClinVar/HGMD evidence, annotations,
similarity scores, and ranked genes.
V1 [B,X].Evaluated on 1,185 samples
across four datasets and 72 additional
difficult cases; complete replayability is not
established.
DeepRare (168) Phenotype- and
genotype-based rare-
disease diagnosis
F1, F2, F3, F4, F5, F6.Coordinates
phenotype, genotype, retrieval, and
normalization services; maintains patient
evidenceanditerativelyreassessesdiagnoses.
E1, E2, E3, E4, E5, E6.Clinical narratives,
HPO and WES/VCF data, confirmed
diagnoses, literature, rare-disease resources,
Exomiser results, variant rankings, and
diagnostic hypotheses.
V3 [B,H,R,X].Public code and documented
workflows support replay. Evaluation
includes multi-centre datasets, diagnostic
and physician baselines, specialist review,
ablations, backbone comparisons, and
failure analysis.
Table S10 Genomics, transcriptomics, perturbation, and CRISPR agents: perturbation prediction, experiment design, and gene-editing intervention.
Reported V-stages follow the cumulative V0–V4 criteria.
System Task Function profile Evidence profile Reported V-stage and qualifiers
Perturbation-Response Prediction
CausalPert (89) Gene-perturbation
response prediction
F1, F2, F5.Generates and aggregates
regulatory hypotheses and selects anchor
genes for response prediction.
E2, E3, E4, E5, E6.Interaction networks,
archived Perturb-seq profiles, predicted
regulators, confidence scores, and consensus
rankings.
V1 [B,R].Evaluated retrospectively across
four cell lines using baselines, low-data
experiments, and ablations; V2 replayability
is not established.
PBIO-AGENT
(60)
Chemical and genetic
response prediction
F1, F2, F4, F5.Coordinates mechanism,
network, synthesis, and judge agents
while propagating high-confidence reasoning
traces.
E2, E3, E4, E5, E6.Biological networks,
LINCS and Perturb-seq data, predicted
responses, confidence measures, and
candidate rankings.
V1 [B,R].Evaluated on LINCSQA and
PerturbQA with multiple baselines and
component analyses; complete replayability
is not established.
Perturbation Experiment Design
BioDiscoveryAgent
(112)
Single-gene and
combinatorial
perturbation design
F1, F3, F4, F5.Plans sequential screens,
searches literature and pathways, analyzes
previous results, and revises candidates
through critique.
E1, E2, E3, E4, E6.PubMed, Reactome,
archived perturbation screens, phenotypic
scores, hit curves, candidate lists, and critic
outputs.
V3 [B,S,R,X].Public artifacts support
replay. Evaluation spans multiple screens,
repeated runs, Bayesian, random, and
human baselines, tool ablations, and single-
gene and combinatorial tasks. Rounds use
archived outcomes, so P and C are not
assigned.
PerTurboAgent
(42)
Sequential Perturb-
seq panel design
F1, F3, F4, F5.Selects CRISPRi panels
through prediction, enrichment, reflection,
refinement, and action memory.
E2, E3, E4, E5, E6.Archived Perturb-
seq data, pathway resources, embeddings,
enrichment outputs, predictions, action logs,
and hit curves.
V1 [B,R].Evaluated retrospectively on
11 phenotype tasks using active-learning
baselinesandablations; roundsaresimulated
and V2 replayability is not established.
Prospective Gene-Editing Intervention
CRISPR-GPT
(109)
CRISPR experiment
design and analysis
F1, F2, F3, F4, F5, F6.Plans editing
workflows, coordinates specialists, selects
modalities and delivery strategies, invokes
design tools, and supports expert oversight.
E1, E2, E4, E6.CRISPR literature
and protocols, Primer3, CRISPRitz,
CRISPResso2, and prospective knockout
and activation measurements.
V4 [B,H,P].GeneEditingBench and expert
evaluation are combined with prospective
knockout and activation experiments. C is
not assigned because assay feedback did not
drive a subsequent editing round.
knowledge graphs, predictive models, docking workflows, and clinical-analysis
methods are subsequently executed to generate inspectable computational
evidence. Resulting claims should remain linked to molecular structures,
target records, mechanistic paths, safety evidence, trial assumptions, statistical
outputs, and retrieved biomedical sources.
Workflow-state maintenance, safety checking, critique, repair, verification,
expert review, and provenance preservation operate across these activities
rather than as isolated final steps. Their importance increases for patient-
specific recommendations, toxicity assessment, clinical-trial reasoning, and
therapeutic candidate prioritization, where errors in entity normalization,
cohort construction, endpoint definition, causal assumptions, molecular
scoring, or evidence attribution can lead to unsupported conclusions. Archived
pharmacological, preclinical, or clinical observations contribute to the Evidence
profile but do not establish prospective Validation unless an output generated by
the evaluated workflow is directly tested.
Table S26 translates these recurring patterns into domain-specific design
requirements. It identifies the molecular representations, target records,
retrieved evidence, model outputs, safety checks, statistical artifacts, workflow
traces, and empirical readouts that should remain inspectable. Together, the

22 Agentic Bioinformatics through Function, Evidence, and Validation, 2026, Volume , Issue
Table S11 Cross-cutting design requirements for genomics, transcriptomics, perturbation, and CRISPR agents.The requirements distinguish workflow
Function, inspectable Evidence, and use-case-specific Validation.
Workflow requirement Domain-specific principle Inspectable evidence and artifacts FEV interpretation
Genomic objective and planning Define the sequencing, association, diagnostic,
perturbation, or gene-editing objective and its
analytical steps.
Research question, assay requirements, workflow
plan, constraints, endpoints, and decision points.
F1.Planning defines the workflow
but does not establish execution or
validity.
Analytical role coordination Coordinate molecular-data processing, statistical
analysis, biological interpretation, review, and
experimental oversight.
Agent assignments, shared state, analytical
handoffs, critic outputs, review notes, and approval
records.
F2.Coordination does not
independently establish reliability or
a higher V-stage.
Molecular data grounding Resolve samples, assays, genome builds,
phenotypes, cohorts, batches, treatments, and
perturbation conditions.
FASTQ/BAM files, count matrices, SRA/GEO
accessions, VCF/WES records, HPO terms, cohort
metadata, and perturbation measurements.
E3.Traceable molecular inputs are
necessary, but not sufficient, for
replayability.
Genomics tool execution Run preprocessing, alignment, quantification,
variant annotation, enrichment, database queries,
guide design, and editing analysis.
Commands, parameters, logs, intermediate
files, and outputs from tools such as HISAT,
featureCounts, ANNOVAR, Exomiser, Primer3,
CRISPRitz, and CRISPResso2.
F3; E4.Execution supports V1;
V2 additionally requires replayable
inputs, environments, parameters,
and traces.
Statistical and mechanistic
analysis
Evaluate expression, association, survival,
regulation, causality, diagnostic ranking, and
perturbation response.
Differential-expression results, regression and
survival models, regulatory networks, variant
rankings, model predictions, and perturbation
scores.
E4; E5for predictive or generative
models. Scientific adequacy requires
separate evaluation.
Evidence-grounded interpretation Link genes, variants, pathways, phenotypes,
diagnoses, and perturbation effects to identifiable
biological sources.
PubMed, OMIM, ClinVar, HPO, GO, KEGG,
Reactome, UniProt, database identifiers, retrieved
passages, and evidence-linked reports.
E1; E2.Source access supports
attribution but does not itself
establish Validation.
Genomic trace capture Preserve molecular inputs, analytical decisions,
software execution, failures, repairs, and output
lineage.
Accessions, sample identities, genome builds,
software versions, parameters, scripts, notebooks,
intermediate artifacts, and repair logs.
F4; E4.Trace capture supports V2
only when the evaluated workflow
can be reconstructed or replayed.
Verification and escalation Check sample grouping, batch effects, QC, model
assumptions, identifiers, evidence attribution,
uncertainty, and claim sufficiency.
QC and batch reports, sensitivity analyses,
critic outputs, repaired code, evidence checks,
uncertainty flags, and expert-review records.
F5; F6.Verification effectiveness
must be established through task-
appropriate Validation.
Prospective perturbation or
editing validation
Test an agent-generated gene, perturbation, guide
RNA, editing protocol, diagnostic claim, or
intervention recommendation.
Guide sequences, assay protocols, knockout or
activation measurements, editing-efficiency results,
functional readouts, and experimental records.
E6; P.V4 also requires the lower
cumulative gates;Crequires
empirical feedback to change a
subsequent action.
Note.Requirements 1–6 define the core workflow in Figure S6; requirements 7–8 operate across that workflow. Requirement 9 is optional. Archived experimental or clinical
observations contribute to Evidence but not to prospective Validation unless an output of the evaluated workflow is directly tested.
system maps, synthesis figure, and design-requirement table separate workflow
functionality, evidentiary traceability, and use-case-specific validation.
Computational Pathology, Microscopy, and Spatial Imaging
Agents
Tables S27–S30 map systems spanning pathology image–text generation,
bioimage infrastructure, microscopy analysis, spatial-molecular interpretation,
whole-slide navigation, biomarker discovery, and cross-modal imaging
automation. Representative tasks include model screening, registration,
segmentation, cell quantification, region selection, multiscale diagnostic
reasoning, spatial pathway analysis, prognostic modelling, and multimodal
biomarker discovery. The mapped systems range from agent-readable imaging
infrastructure to stateful pathology agents that execute, verify, and interpret
image-analysis workflows.
Despite this diversity, the systems share several recurring workflow
requirements, summarized in Figure S10. Images must first be linked to their
modality, tissue, magnification, assay, cohort, acquisition conditions, and
biological objective. They must then be converted into inspectable regions,
cells, tissue compartments, spatial neighborhoods, morphological features, or
molecularly informed representations. Domain tools are subsequently executed
for registration, segmentation, quantification, navigation, model adaptation,
spatial analysis, and statistical modelling. Resulting claims should remain
linked to identifiable image regions, molecular measurements, pathology
knowledge, clinical observations, and analytical artifacts.
Workflow-state maintenance, quality control, uncertainty assessment, repair,
verification, expert review, and provenance preservation operate across these
activities rather than as isolated final steps. Their importance increases
for diagnostic, prognostic, and biomarker-oriented outputs, where errors in
registration, segmentation, region selection, magnification, cohort construction,
statistical assumptions, or evidence attribution can propagate into consequential
conclusions. Archived images, molecular measurements, clinical outcomes, and
independent cohorts contribute to the Evidence profile or external-validation
qualifier, but do not establish prospective Validation unless an output generated
by the evaluated workflow is directly tested.
Table S31 translates these recurring patterns into domain-specific design
requirements. It identifies the image inputs, tissue metadata, region and cell
representations, image-analysis outputs, quality-control records, navigation
traces, molecular evidence, statistical artifacts, and empirical readouts that
should remain inspectable. Together, the system maps, synthesis figure,
and design-requirement table separate workflow functionality, evidentiary
traceability, and use-case-specific validation.
General Bioinformatics Workflow Agents and Automation
Systems
Tables S32–S33 map general-purpose systems spanning biomedical database
access, omics analysis, biomarker discovery, executable workflow automation,
biomedical machine learning, evidence verification, self-evolving tool use,
and experimentally connected scientific discovery. Unlike domain-specific
agents, these systems provide reusable workflow-control layers across multiple
biological data types, tools, and analytical tasks.
Despite their breadth, the systems share several recurring requirements,
summarized in Figure S11. A biological objective must first be translated

Agentic Bioinformatics through Function, Evidence, and Validation, 2026, Volume , Issue23
1. Genomic objective and planning
Define the sequencing,
association, diagnostic,
perturbation, or gene-editing task
2. Analytical role coordination
Coordinate data processing,
statistical modelling, biological
review, and oversight
3. Molecular data grounding
Resolve samples, assays,
genome builds, phenotypes,
cohorts, batches, and
perturbation conditions
Workflow
formulation
6. Genomic interpretation
Ground genes, variants, pathways,
diagnoses, and perturbation
effects in traceable evidence
5. Statistical and causal analysis
Evaluate differential expression,
gene–trait associations,
survival, regulation, and
perturbation response
4. Genomics tool execution
Run alignment, quantification,
variant annotation, enrichment,
database queries, and guide design
Workflow
operation
Shared genomic evidence and artifacts:FASTQ/BAM files, count matrices, SRA/GEO records,
VCF/WES files, HPO and cohort metadata, database records, QC outputs, differential-expression
results, variant annotations, fitted models, ranked genes, guide designs, and evidence-linked reports
Shared genomic
evidence
and artifacts
7. Genomic trace capture:record accessions, sample identities, genome builds, database and
software versions, parameters, code, intermediate artifacts, failures, repairs, and output lineage
8. Genomic verification and escalation:check sample grouping, batch effects, QC, model
assumptions, identifiers, evidence support, and uncertainty; revise or escalate unsupported claims
Cross-
cutting across
requirements 1–6
9. Optional perturbation or editing validation
Test prioritized genes, perturbations, guide RNAs, diagnostic claims, or editing
protocols. Closed-loop refinement requires the result to guide a subsequent action
Optional empirical
extension
Figure S6 Cross-cutting workflow blueprint for genomics, transcriptomics, perturbation, and CRISPR agents.The blueprint summarizes the domain-specific
requirements in Table S11. The core trajectory progresses from formulation of a sequencing, association, diagnostic, perturbation, or gene-editing objective
to molecular-data grounding, execution of genomics tools and databases, statistical or mechanistic analysis, and evidence-linked interpretation. Genomic
evidence and artifacts are used or generated across this trajectory. State and trace capture preserve sample, genome, software, parameter, and artifact lineage,
while verification checks data quality, analytical assumptions, identifier consistency, evidentiary support, and uncertainty. Prospective perturbation or editing
validation is optional. It constitutes closed-loop refinement only when the resulting empirical evidence changes a subsequent workflow action.
into an explicit workflow plan and routed to the appropriate data modality,
tools, databases, and analytical methods. Relevant documentation, protocols,
examples, and biological evidence are then retrieved to support executable
code or pipeline generation. The resulting workflow should preserve its inputs,
environment, parameters, intermediate artifacts, execution traces, and analytical
outputs.
Workflow-state maintenance, critique, debugging, verification, provenance
capture, and escalation operate across these activities rather than as isolated
final steps. Claims of generality additionally require evaluation across multiple
biological domains, datasets, tools, and task formulations. Prospective testing
remains uncommon; archived experimental observations contribute to the
Evidence profile but do not establish prospective Validation unless an output
generated by the evaluated workflow is directly tested.
Table S34 translates these patterns into domain-general design requirements.
It identifies the workflow plans, retrieved evidence, scripts, environments,
intermediate artifacts, repair traces, benchmark outputs, provenance records,
and experimental readouts that should remain inspectable. Together, the
system maps, synthesis figure, and design-requirement table separate workflow
functionality, evidentiary traceability, and use-case-specific validation.
Benchmarks, Evaluation Suites, and Workflow Infrastructure
Tables S35–S39 summarize resources used to evaluate agentic bioinformatics
systems. Unlike the domain-specific system tables, these resources assess
whether agents can retrieve evidence, select tools, execute workflows, generate
artifacts, recover from failures, preserve provenance, and produce scientifically
interpretable outputs.
The evaluation landscape spans evidence retrieval and verification, file-
and code-centric workflow execution, biomedical machine learning, domain-
specific analysis, tool-use trajectories, robustness testing, and long-horizon
orchestration. General workflow benchmarks test whether agents can
interpret task descriptions, manipulate biological files, generate and execute
code, recover from errors, and reproduce graded outputs. Domain-specific
benchmarks extend these criteria to genomics, gene editing, single-cell and
spatial omics, protein design, drug discovery, and pathology.
Evidence-centred resources complement executable benchmarks by testing
whether biomedical claims remain linked to literature, databases, knowledge
graphs, retrieved passages, entity mappings, and statement-level provenance.
Process-aware resources additionally inspect tool calls, intermediate artifacts,
execution traces, citation grounding, and failure recovery rather than relying
only on final-answer accuracy.
Together, these resources provide the evaluation substrate for assigning use-
case-specific FEV profiles and Validation stages. Demonstrated benchmark
execution may support V1; replayable environments, inputs, parameters,
artifacts, and traces are additionally required for V2; and V3 requires
task-appropriate scientific evaluation beyond executability alone. Benchmark

24 Agentic Bioinformatics through Function, Evidence, and Validation, 2026, Volume , Issue
Table S12 Single-cell and spatial-omics agents: data access and executable workflows.
System Task Function profile Evidence profile Reported V-stage and qualifiers
Data Access and Standardization
SRAgent (160) Agent-curated
scRNA-seq repository
F1, F3, F4, F5.Discovers 10X scRNA-
seq studies, extracts metadata, and
routes raw reads through standardized
Nextflow/STARsolo workflows.
E2, E3, E4.SRA accessions and metadata,
raw reads, chemistry assignments, processed
count matrices, workflow logs, and
CELLxGENE comparisons.
V3 [B,S,R,X].Public code and data support
replay; large-scale evaluation spans more
than 230 million cells, 21 organisms, and
72 tissues, with analyses of processing
consistency and technical confounding.
CellAtria (103) Document-to-analysis
scRNA-seq reuse
F1, F3, F4.Extracts study metadata,
resolves GEO accessions, retrieves datasets,
and launches standardized CellExpress
workflows.
E1, E2, E3, E4.Research articles, GEO
metadata, sample annotations, AnnData
objects, workflow records, and HTML
reports.
V2 [R].Executable retrieval and
standardized analysis artifacts support
replay; biological evaluation remains
limited.
CompBioAgent
(165)
Natural-language
scRNA-seq
exploration
F1, F3.Converts biological questions
into CellDepot queries and Cellxgene VIP
visualization requests.
E2, E3, E4.Public scRNA-seq datasets,
structured queries, UMAPs, violin plots,
heatmaps, and filtered cell-level outputs.
V1.Interactive data access and visualization
are demonstrated, but systematic replay and
scientific evaluation are not established.
Executable Single-Cell and Spatial Workflows
BioInformatics
Agent (BIA)
(151)
End-to-end scRNA-
seq analysis
F1, F3, F4, F5.Retrieves datasets and
metadata, generates and executes Scanpy
workflows, repairs failures, and produces
analytical reports.
E1, E2, E3, E4.ENA/GEO/ArrayExpress
records, FASTQ and AnnData inputs,
metadata, QC outputs, clusters,
annotations, interaction results, and
pseudotime.
V2 [B,R].Demonstrates executable
workflows and high metadata-extraction
accuracy across 11 tasks; broader scientific
evaluation remains limited.
CellAgent (149) Automated single-cell
and spatial analysis
F1, F2, F3, F4, F5.Coordinates planning,
execution, and evaluation agents to select
tools, parameters, and revised workflows.
E2, E3, E4.Single-cell and spatial datasets,
workflow traces, clustering, marker,
annotation, and downstream-analysis
outputs.
V3 [B,H,R].Evaluated across single-cell
tasks against computational workflows and
human experts, with iterative optimization
analyses.
STAT (15) Integrated spatial
transcriptomics
analysis
F1, F3, F4, F5, F6.Maintains a persistent
spatial session, selects compatible skills,
executes code, reflects on errors, interprets
regions, and exports notebooks.
E1, E2, E3, E4.Visium, MERFISH, Xenium,
and Visium HD data; H&E images, ROI
annotations, tool outputs, spatial statistics,
notebooks, and reports.
V3 [B,S,R,X].Evaluated across 11
task categories, multiple platforms and
resolutions, with baselines, backbone
ablations, and reproduction of a published
study.
Table S13 Single-cell and spatial-omics agents: spatial execution, annotation, and uncertainty.
System Task Function profile Evidence profile Reported V-stage and qualifiers
Executable Spatial-Omics Workflows
SpatialAgent
(132)
Autonomous spatial-
biology analysis
F1, F3, F4, F5, F6.Plans and executes
workflows for gene-panel design, annotation,
cell–cell communication, reporting, and
hypothesis generation.
E1, E2, E3, E4.Visium, MERFISH and
Xenium data, marker databases, pathway
resources, annotations, communication
outputs, and reports.
V3 [B,H,R,X].Evaluated across tissues
and species against computational baselines
and human experts; prospective wet-lab
validation is not established.
STAgent (71) Spatial analysis and
visual reasoning
F1, F3, F4, F5.Combines planning,
code retrieval, Python execution, visual
reasoning, literature retrieval, and
autonomous reporting.
E1, E2, E3, E4.STARmap expression
and coordinate data, spatial maps,
Scanpy/Squidpy outputs, interaction
analyses, retrieved literature, and reports.
V3 [B,R,X].Reproduces major spatial
analyses and published findings across
developmental time points; conclusions
remain computational.
SP-Mind (163) Spatial-proteomics
workflow automation
F1, F3, F4, F5.Uses curated skills,
tool execution, failure diagnosis, and self-
correction for multiplexed tissue-imaging
workflows.
E2, E3, E4.CODEX, CyCIF, MIBI,
and IMC data; registration, segmentation,
quantification, clustering, and annotation
outputs.
V3 [B,R,X].Evaluated on 102 SP-Bench
tasks with quantitative execution and
annotation metrics; performance depends on
curated skill templates.
Annotation, Evidence, and Uncertainty
scExtract (147) Published-data
annotation and
integration
F1, F3, F4.Extracts study metadata,
configures preprocessing, annotates cells,
and integrates datasets using publication-
derived priors.
E1, E2, E3, E4.Research articles, AnnData
objects, extracted metadata, marker
evidence, annotation outputs, integration
results, and reference benchmarks.
V3 [B,R,X].Outperforms reference-transfer
baselines and integrates 14 datasets into a
440,000-cell human skin atlas.
Lightweight ST
LLM Agent (29)
Spatial-region
annotation
F2, F5.Combines prototype niche cards,
low-confidence LLM correction, multi-role
review, spatialchecks, andgraphsmoothing.
E2, E3, E4, E5.STARmap and MERFISH
data, marker profiles, spatial neighborhoods,
annotation predictions, and clustering
metrics.
V1 [B,S,R].Benchmarked on six datasets
using NMI, ARI, CHAOS, and ASW;
agentic variants mostly match deterministic
baselines, and replayability is not
established.
CASSIA (150) Reference-free cell-
type annotation
F1, F2, F5, F6.Generates competing
annotations, validates marker support,
scores quality, merges labels, and reports
uncertainty.
E1, E2, E3, E4, E5.Marker tables, reference
knowledge, annotation hypotheses, quality
scores, uncertainty estimates, subclusters,
and HTML reports.
V3 [B,S,R,X].Broadly benchmarked across
cell types and tissues with quality scoring
and annotation refinement; biological
validation remains computational.
TACTIC (7) Explainable spatial
cell-type annotation
F1, F2, F5.Combines expression, marker
and spatial embeddings with junior–senior
agent review to assign labels and confidence.
E2, E3, E4, E5.MERFISH, MIBI-TOF
and Stereo-seq data, marker genes, spatial
graphs, embeddings, annotations, and
classification metrics.
V3 [B,S,R,X].Evaluated across three spatial
platforms with quantitative annotation
metrics and structural ablations; revised
labels lack prospective testing.

Agentic Bioinformatics through Function, Evidence, and Validation, 2026, Volume , Issue25
Table S14 Single-cell and spatial-omics agents: trajectory, interaction, and perturbation modelling.
System Task Function profile Evidence profile Reported V-stage and qualifiers
Annotation and Uncertainty
CyteType (5) Uncertainty-aware
cell-type annotation
F1, F2, F5, F6.Builds cluster context,
generates competing cell-type hypotheses,
validates marker evidence, detects
heterogeneity, and reports confidence.
E1, E2, E3, E4, E5.Expression profiles,
marker and ontology resources, pathway
evidence, annotation hypotheses, confidence
scores, and semantic-similarity metrics.
V3 [B,S,R,X].Evaluated across 205 clusters
and 16 model backbones against established
annotation methods, with confidence and
heterogeneity analyses.
Trajectory, Interaction, and Regulatory Modelling
SpaCellAgent
(137)
Single-cell and spatial
trajectory inference
F1, F3, F4, F5.Generates, executes,
evaluates, and repairs trajectory workflows
while retaining validated templates.
E1, E3, E4.Single-cell and spatial datasets,
executable code, pseudotime orderings,
lineage topologies, evaluator feedback,
plots, and reports.
V3 [B,S,R,X].Benchmarked across real
and synthetic datasets against trajectory-
inference baselines using topology, ordering,
and efficiency metrics.
Perturbation and Multiomic Modelling
HarmonyCell (51) Virtual-cell
perturbation
modelling
F1, F3, F4, F5.Harmonizes perturbation
metadata and searches model architectures
through adaptive MCTS and execution
feedback.
E2, E3, E4, E5, E6.Archived CRISPR and
drug-perturbation data, canonical metadata,
generated models, execution traces, and
prediction metrics.
V3 [B,S,R,X].Evaluated across
heterogeneous perturbation datasets,
unseen tasks, execution robustness, and
expert-designed baselines; no prospective
wet-lab testing is reported.
scAgents (124) Single-cell
perturbation-model
design
F1, F2, F3, F4, F5.Retrieves evidence,
designs perturbation models, generates
executable code, and evaluates predicted
responses.
E1, E2, E3, E4, E5, E6.Literature, archived
multimodal perturbation data, persistent
knowledge, generated models, executable
code, and prediction outputs.
V3 [B,S,R,X].Evaluated across multiple
modalities against specialized predictive
baselines; validation remains retrospective
and in silico.
M3A (56) Agentic single-cell
multiome discovery
F1, F2, F4, F5, F6.Coordinates autonomous
and copilot multiomic reasoning over
persistent states, with step-level telemetry
and expert review.
E1, E2, E3, E4, E5, E6.Pan-cancer
snRNA/snATAC data, cNMF programs,
TCGA cohorts, clinical endpoints, reasoning
traces, and ranked hypotheses.
V3 [B,H,S,R,X].Evaluated across pan-
cancer tasks using held-out cohorts,
workflow telemetry, blinded expert
review, and autonomous-versus-copilot
comparisons.
Table S15 Single-cell and spatial-omics agents: interactive and autonomous discovery.
System Task Function profile Evidence profile Reported V-stage and qualifiers
Interactive and Autonomous Discovery
ELISA (22) Expression-grounded
interactive discovery
F1, F3, F4.Routes natural-language
queries to expression retrieval, pathway
scoring, interaction prediction, comparison,
visualization, and reporting.
E2, E3, E4, E5.CELLxGENE datasets,
expression and semantic embeddings,
differential expression, pathways, ligand–
receptor pairs, and retrieval outputs.
V3 [B,S,R,X].Evaluated on six datasets and
100 retrieval queries against CellWhisperer,
with replication of published findings.
CellVoyager (6) Autonomous scRNA-
seq exploration
F1, F3, F4, F5.Generates, executes,
critiques, debugs, and replans notebook-
based scRNA-seq analyses and hypotheses.
E1, E3, E4, E5.Published study
context, scRNA-seq datasets, generated
notebooks, code, plots, interpretations, and
independent-dataset analyses.
V3 [B,H,R,X].Benchmarked on analyses
from 76 publications with expert-reviewed
case studies and independent computational
validation; no prospective wet-lab testing is
reported.
Table S16 Single-cell and spatial-omics agents: knowledge-grounded discovery and hypothesis validation.
System Task Function profile Evidence profile Reported V-stage and qualifiers
Knowledge-Grounded Discovery
BiOmics (13) Knowledge-grounded
multi-omics reasoning
F1, F2, F3, F4, F5, F6.Coordinates
knowledge retrieval, multi-omics tools,
graphreasoning, prediction, verification, and
evidence-linked reporting.
E1, E2, E3, E4, E5.A large biomedical
knowledge graph, literature, multi-omics
datasets, tool outputs, graph paths,
predictions, and reports.
V3 [B,S,R,X].Evaluated across retrieval,
annotation, variant prioritization, trajectory,
drug repurposing, spatial, network, and
proteomics tasks.
OmniCellAgent
(48)
Single-cell discovery
and hypothesis
generation
F1, F2, F3, F4, F5.Coordinates dataset
retrieval, differential analysis, enrichment,
KG reasoning, literature review, expert
synthesis, and reporting.
E1, E2, E3, E4, E5.CELLxGENE/GEOdata,
enrichment outputs, PrimeKG subgraphs,
literature, statistical analyses, ranked
hypotheses, and PDF reports.
V2 [R,X].Executable case studies and
persistent state support replay, but
evaluation remains limited and does not
establish broad V3 scientific assessment.
PhenoGraph
(102)
Phenotype-driven
spatial discovery
F1, F3, F4, F5.Retrieves phenotype-
matched cohorts, adapts Scissor to spatial
data, tunes parameters, and interprets
phenotype-associated regions.
E2, E3, E4, E5, E6.Visium and TCGA data,
clinical phenotypes, spatial regions, DEGs,
survival outputs, and PrimeKG subgraphs.
V2 [R,X].End-to-end execution is
demonstrated across breast- and pancreatic-
cancer case studies; broad benchmarked
evaluation is not established.
OmicsNavigator
(159)
Auditable spatial-
omics hypothesis
validation
F1, F3, F4, F5, F6.Curates priors, profiles
spatial regions, retrieves biomarkers, and
validates hypotheses through pre-registered
statistics and human audit.
E1, E2, E3, E4, E5, E6.CODEX/IMC data,
morphology and protein profiles, clinical
severity, verification blueprints, mixed
models, FDR outputs, and audit records.
V3 [B,H,S,R,X].Evaluated across kidney
and lung datasets using human labels,
ablations, semantic retrieval, pre-registered
statistics, and clinical severity associations.
success does not establish V4, which requires prospective empirical testing of
an output generated by the evaluated workflow.

26 Agentic Bioinformatics through Function, Evidence, and Validation, 2026, Volume , Issue
Table S17 Cross-cutting design requirements for single-cell, spatial biology, cell annotation, and spatial-omics agents.The requirements distinguish
workflow Function, inspectable Evidence, and their contribution to use-case-specific Validation.
Workflow requirement Domain-specific principle Inspectable evidence and artifacts FEV interpretation
Dataset and context grounding Identify the assay, samples, tissue, species,
condition, cohort, metadata, and analytical
objective before selecting tools.
AnnData or Seurat objects, expression matrices,
GEO/GSM accessions, sample annotations, tissue
labels, disease states, assay metadata, and study
context.
F1; E3.Grounded inputs support
workflow formulation but do not
independently establish replayability.
Cell and spatial representation Represent cells and regions through expression
states, markers, clusters, coordinates,
neighborhoods, tissue domains, and perturbation
contexts.
Marker tables, UMAPs, cell labels, spatial
coordinates, neighborhood graphs, ROI
annotations, tissue domains, and multimodal
cell profiles.
E3; E5when learned representations
are used. Representation quality
requires separate evaluation.
Single-cell and spatial tool
execution
Execute preprocessing, integration, clustering,
annotation, trajectory, interaction, registration,
segmentation, and spatial-analysis workflows.
Scanpy, Seurat, CellTypist, scVelo, CellChat,
LIANA, Squidpy, MCMICRO, commands,
parameters, logs, notebooks, and intermediate
outputs.
F3; E4.Execution supports V1;
V2 additionally requires replayable
environments, parameters, inputs,
and traces.
Annotation and uncertainty
assessment
Validate cell-type and tissue-region labels using
marker support, confidence, spatial coherence,
consensus reasoning, and expert review.
Marker evidence, annotation scores, confidence
estimates, heterogeneity flags, consensus labels,
spatial-coherence metrics, and reviewer records.
F5; F6; E4; E5.Annotation
quality must be established through
benchmarks, diagnostics, or expert
assessment.
Biological evidence grounding Link annotations, trajectories, interactions, and
spatial patterns to reference atlases, marker
databases, pathways, and literature.
CellMarker, PanglaoDB, CELLxGENE, Cell
Ontology, PubMed, GO, Reactome, ligand–receptor
resources, retrieved passages, and evidence-linked
reports.
E1; E2.Biological sources support
attribution but do not independently
establish Validation.
Workflow state, critique, and
repair
Preserve analysis state, detect failed tools or
implausible outputs, revise plans, repair code, and
rerun affected analyses.
Planner and executor traces, failed calls, corrected
code, revised notebooks, critic outputs, memory
records, repair logs, and workflow histories.
F4; F5.State and repair records
support inspection and replay
when the complete workflow is
reconstructable.
Provenance-preserving reporting Report the complete trajectory from molecular
inputs to annotations, spatial findings, biological
interpretations, and limitations.
Executed code, notebooks, dataset identifiers,
parameters, plots, UMAPs, spatial maps, HTML
reports, intermediate artifacts, evidence links,
uncertainty, and limitations.
F4; F6; E4.Provenance supports
replay, audit, and expert review but
is not itself a scientific Validation
result.
Prospective biological validation Where required, test an agent-generated
annotation, trajectory, interaction, perturbation
response, spatial pattern, or biological hypothesis.
Prospective perturbation assays, imaging validation,
lineage tracing, targeted marker measurements,
functional readouts, and design-linked experimental
records.
E6; P.V4 also requires the lower
cumulative gates;Crequires the
new readout to change a subsequent
workflow action.
Note.Requirements 1–5 describe the core analytical trajectory summarized in Figure S7. Requirements 6–7 operate across that trajectory. Requirement 8 is optional and claim-
dependent. Archived perturbation, clinical, or spatial observations contribute to Evidence but not to prospective Validation unless an output of the evaluated workflow is directly
tested.

Agentic Bioinformatics through Function, Evidence, and Validation, 2026, Volume , Issue27
1. Dataset and context grounding
Resolve assays, samples, tissues,
species, conditions, cohorts,
metadata, and analytical goals
2. Cell and spatial representation
Represent expression states,
markers, clusters, coordinates,
neighborhoods, and tissue domains
3. Single-cell and
spatial tool execution
Run preprocessing, integration,
clustering, annotation, trajectory,
interaction, and spatial analysis
Data grounding
and execution
5. Biological evidence grounding
Link annotations, trajectories,
interactions, and spatial patterns
to traceable biological sources
4. Annotation and
uncertainty assessment
Check marker support, confidence,
heterogeneity, spatial coherence,
consensus, and expert review
Interpretation
and assessment
Shared single-cell and spatial evidence and artifacts:AnnData and Seurat objects, expression
matrices, marker tables, UMAPs, spatial coordinates, neighborhood graphs, ROI annotations,
tool outputs, annotation scores, pathway results, notebooks, plots, and evidence-linked reports
Shared evidence
and artifacts
6. Workflow state, critique, and repair:preserve analytical state, inspect failed calls and
implausible outputs, revise plans, repair code, rerun affected steps, and record workflow history
7. Provenance-preserving reporting:retain dataset identifiers, parameters, code, notebooks,
intermediate artifacts, spatial maps, evidence links, uncertainty, review records, and limitations
Cross-
cutting across
requirements 1–5
8. Optional prospective biological validation
Test an agent-generated annotation, trajectory, interaction,
perturbation response, spatial pattern, or biological hypothesis. Closed-
loop refinement requires the result to change a subsequent action
Optional empirical
extension
Figure S7 Cross-cutting workflow blueprint for single-cell, spatial biology, cell annotation, and spatial-omics agents.The core trajectory connects dataset and
context grounding with cell-level and spatial representation, domain-tool execution, uncertainty-aware annotation, and evidence-linked biological interpretation.
Shared artifacts include expression objects, marker tables, spatial coordinates, neighborhood graphs, annotation scores, analytical outputs, and reports.
Workflow-statemaintenance, repair, andprovenance-preservingreportingoperateacrossthetrajectory. Prospectivebiologicalvalidationisoptional. Itconstitutes
closed-loop refinement only when the resulting empirical evidence changes a subsequent workflow action.

28 Agentic Bioinformatics through Function, Evidence, and Validation, 2026, Volume , Issue
Table S18 Proteomics, structural-biology, and protein-design agents: protein access, proteomics analysis, and evidence-grounded interpretation.
System Task Function profile Evidence profile Reported V-stage and qualifiers
Protein Access and Proteomics Exploration
TourSynbio-
Search (80)
Protein information
retrieval and structure
access
F1, F3.Interprets protein-engineering
queries, routes them to literature or protein-
database search, refines parameters, and
retrieves structures.
E1, E2, E4.Retrieved papers, UniProt and
PDB records, search parameters, PDB files,
and PyMOL visualizations.
V1.Literature and protein-database retrieval
with structure visualization is demonstrated,
but replayable workflow artifacts and
systematic scientific evaluation are not
established.
DrBioRight 2.0
(78)
Cancer functional
proteomics
exploration
F1, F3, F5.Translates proteomics questions
into statistical analyses, visualizations,
generated or corrected code, and reports.
E2, E3, E4.RPPA, TCGA and CCLE data,
antibody annotations, pathway resources,
statistical outputs, generated code, plots,
and reports.
V1 [H].Protein-centric cancer analyses
and curated expert-facing functionality
are demonstrated, but complete workflow
replay and systematic evaluation are not
established.
Evidence-Grounded Protein Interpretation
BioInsight (133) Disease-centred
protein interpretation
F1, F2, F3, F4, F5, F6.Coordinates pathway
analysis, literature retrieval, protein-level
reasoning, citation checking, evidence
synthesis, and dashboard generation.
E1, E2, E3, E4.Protein tables, cohort
metadata, pathway enrichment, literature,
UniProt, STRING, Open Targets, ranked
results, evidence packets, and dashboards.
V3 [B,H,R].Replayable analytical artifacts
are evaluated on BioASQ, BioInsight-100,
and end-to-end disease-level synthesis, with
expert assessment of coverage, validity,
traceability, prioritization, and usability.
GOAgent (Zhapa-
Camacho et al.)
(170)
Evidence-grounded
protein-function
prediction
F1, F3, F5, F6.Uses protein evidence and
specialized tools to inspect, verify, and revise
Gene Ontology predictions with rationales.
E1, E2, E3, E4, E5.Protein sequences,
UniProtKB, PubMed, InterPro, GO
constraints, homology outputs, model
predictions, revised scores, and rationales.
V3 [B,S,R,X].Evaluated on temporally
separated SwissProt data across three GO
sub-ontologies using multiple baselines,
four metrics, repeated runs, and evidence-
source ablations. Predictions remain
computational.
PROTEUS (27) Automated
proteomics analysis
and hypothesis
generation
F1, F3, F4, F5, F6.Plans proteomics
analyses, executes specialist tools, interprets
intermediate results, revises objectives, and
generates testable hypotheses.
E1, E2, E3, E4, E5, E6.CyTOF and
mass-spectrometry data, clinical metadata,
proteomics tools, statistical outputs,
biological hypotheses, and retrospective
clinical observations.
V3 [B,H,R,X].Evaluated across 12
proteomics datasets and 191 generated
hypotheses using workflow-level assessment
and expert review of reliability, coherence,
novelty, biological significance, and
testability.
Molecular Modelling and Tool Execution
ChatMol Copilot
(120)
Protein and small-
molecule computation
F1, F3, F4.Invokes molecular microservices,
generates code, maintains cached molecular
objects, and visualizes protein or ligand
results.
E2, E3, E4, E5.Protein and ligand
structures, database records, predicted
structures, docking outputs, designed
sequences, generated code, and
visualizations.
V2.Multi-step molecular workflows, tool
calls, cached state, and generated code
support replay of reported use cases. Broad
scientific benchmarking and prospective
testing are not established.

Agentic Bioinformatics through Function, Evidence, and Validation, 2026, Volume , Issue29
Table S19 Proteomics, structural-biology, and protein-design agents: executable protein-analysis and engineering workflows.
System Task Function profile Evidence profile Reported V-stage and qualifiers
Executable Protein-Analysis and Engineering Workflows
AutoProteinEngine
(AutoPE) (81)
Protein-engineering
AutoML
F1, F3, F4, F5.Validates task scope,
retrievesproteindata, configuresmultimodal
models, optimizes hyperparameters,
executes training, and summarizes results.
E1, E2, E3, E4, E5.Protein sequences and
structures, PDB and UniProt records, model
outputs, optimization traces, performance
metrics, and generated summaries.
V3 [B,S,R].Evaluated on sweetness
classification and enzyme-activity regression
against zero-shot and manually tuned
baselines, with automated hyperparameter
optimization and task-specific predictive
metrics.
GOAgent
(Ponnapati et
al.) (107)
Tool-orchestrated
protein-function
annotation
F1, F3, F4, F5.Orchestrates sequence,
structure, and GO tools; maintains multi-
turn execution trajectories; and produces
sequence- or domain-level annotations with
auditable rationales.
E2, E3, E4, E5.Protein sequences,
structure-derived features, motif, topology,
signal-peptide, binding-site, and Rosetta
outputs, GO relations, tool traces, predicted
terms, and rationales.
V3 [B,S,R,X].Evaluated on CAFA5 and
temporal holdouts against zero-shot, tool-
using, trained-agent, and multimodal
baselines, with repeated rollouts, bootstrap
confidence intervals, tool ablations, and
sandbox-execution tests. Predictions remain
computational.
AutoBinder Agent
(36)
End-to-end protein-
binder design
F1, F3, F4, F5.Plans and executes
target analysis, site prediction, seed
matching, fragment grafting, sequence
redesign, structure prediction, and error
recovery through MCP tools.
E2, E3, E4, E5.Target structures, MaSIF
outputs, Rosetta grafts, ProteinMPNN
sequences, AlphaFold3 complexes, execution
logs, and predicted design metrics.
V2 [B,R].A reproducible MCP workflow is
evaluated on five standardized behavioural
tasks covering planning, tool selection,
parameter parsing, recovery, and design
execution. Binder quality is not prospectively
tested.
PRIME (175) Dynamic protein-
engineering
orchestration
F1, F2, F3, F4, F5, F6.Plans DAG-based
workflows, selects tools, validates inputs and
outputs, recovers from failures, and executes
design or model-training tasks.
E2, E3, E4, E5.Protein databases,
more than 65 computational tools,
workflow DAGs, execution traces, predicted
structures, model outputs, and candidate
designs.
V3 [B,R].Evaluated on 213 multi-step
tasksusingcompletion, tool-use, robustness,
and hallucination measures, with additional
protein-classification and antibody- design
case studies.
ProteinMCP
(153)
MCP-based
protein-engineering
automation
F1, F3, F4, F5.Wraps protein software
as reusable MCP tools and executes fitness
modelling, binder design, and nanobody-
engineering workflows.
E2, E3, E4, E5.MCP tool definitions,
sequence and structure inputs, generated
models, binder candidates, structural scores,
interaction metrics, and execution artifacts.
V2 [B,R].Reusable tool servers and end-to-
end case studies support replay of fitness,
binder, and nanobody workflows. Candidate
quality remains computational and lacks
prospective empirical testing.
ProtAgents (37) Protein design and
mechanics analysis
F1, F2, F3, F5.Coordinates knowledge
retrieval, structure analysis, physics-based
simulation, critique, and interpretation for
de novo protein design.
E1, E2, E3, E4, E5.Protein sequences,
retrieved literature, predicted structures,
secondary structures, mechanical
predictions, simulations, and tool outputs.
V2.Executable in-silico design and
mechanics workflows are demonstrated with
inspectable computational outputs. Broad
standardized evaluation and prospective
wet-lab testing are not established.
Table S20 Proteomics, structural-biology, and protein-design agents: computational protein design and discovery.
System Task Function profile Evidence profile Reported V-stage and qualifiers
Computational Protein Design and Discovery
SPARKS (38) Discovery of protein-
design principles
F1, F2, F3, F4, F5.Generates hypotheses,
designs computational experiments,
executes simulations, refines hypotheses,
and produces plots and manuscript-style
reports.
E1, E3, E4, E5.Generated sequences,
predicted structures, secondary-structure
annotations, force and energy predictions,
molecular-dynamics traces, plots, and
reports.
V3 [S,R].Replayable simulations, quality
checks, statistical analyses, and iterative
computational experiments support
evaluation of generated protein-mechanics
hypotheses. Prospective wet-lab validation
is not reported.
PDAgent (104) Conservation-aware
protein redesign
F1, F3, F4, F5.Translates property
requirements into design constraints,
retrieves templates, protects conserved
residues, proposes mutations, scores
candidates, and iteratively revises sequences.
E2, E3, E4, E5.UniProt templates,
homologous sequences, multiple-sequence
alignments, conservation scores, stability
filters, predicted structures, and design
histories.
V3 [B,S,R].Evaluated across 100 design
tasks using generation success, foldability,
constraint satisfaction, model comparisons,
and ablations of iterative reasoning
components.
VibeGen (100) Dynamics-
conditioned protein
design
Agent-adjacent generative–predictive loop;
F3, F5.Executes structural and dynamics
evaluation within a coupled design loop and
revises candidates using predictive feedback.
E3, E4, E5.Target dynamics, generated
sequences, predicted structures, simulations,
and dynamic-accuracy metrics.
V3 [B].Evaluated on 1,293 held-out
proteins using structural, dynamic, diversity,
and novelty analyses; validation remains
computational.
ProteinCrow
(106)
Protein redesign and
binder optimization
F1, F3, F4, F5.Plans and executes stability
optimization, functional-site-preserving
redesign, binder generation, sequence
filtering, and deimmunization.
E1, E2, E3, E4, E5.Literature, UniProt
records, protein structures, design-model
outputs, Rosetta scores, structural-
confidence measures, epitope predictions,
and ranked candidates.
V3 [B,R].Evaluated across stability,
constrained redesign, binder generation, and
epitope-reduction tasks using computational
baselines, structural checks, design filters,
and tool-trajectory analyses.
AgentPLM (110) Tool-guided protein-
sequence design
Model-level tool-using agent;F3, F4,
F5.Interleaves sequence generation with
biophysical tool calls, retains trajectory
memory, and redirects decoding using
structural, stability, and binding feedback.
E2, E3, E4, E5.Protein datasets, generated
sequences, ESMFold, FoldX and Vina
outputs, fitness predictions, and trajectory
records.
V3 [B,R].Evaluated across five protein-
design settings against passive and tool-
augmented baselines, with ablations and
trajectory analyses; validation remains in
silico.

30 Agentic Bioinformatics through Function, Evidence, and Validation, 2026, Volume , Issue
Table S21 Proteomics, structural-biology, and protein-design agents: prospective experimental evaluation.
System Task Function profile Evidence profile Reported V-stage and qualifiers
Prospective Functional Evaluation
ProteinSwarm /
Swarms of LLM
Agents (131)
Swarm-based protein-
sequence design
F1, F2, F3, F4, F5.Coordinates
residue-specific agents that propose, score,
remember, and revise mutations using local
structural context and design objectives.
E3, E4, E5, E6.Generated sequences,
predicted structures, Rosetta energies,
secondary- structure outputs, design
histories, and prospective circular-dichroism
measurements.
V4 [B,R,P].Computational design is
combined with prospective circular-
dichroism testing of two agent-generated
peptides. The assays validate intended
helix and coil structures, although complete
protein function and binding remain
untested.
Agent-Guided
Cancer Nanobody
Design (169)
De novo nanobody
design against a
cancer target
F1, F3, F4, F5, F6.Identifies epitope
hotspots, generates and scores VHH
candidates, applies developability filters,
performs Pareto selection, and prioritizes
candidates for binding assays.
E2, E3, E4, E5, E6.Target sequences and
predicted structures, nanobody designs,
structural and binding scores, liability
profiles, yeast-display results, FACS
enrichment, and SPR kinetics.
V4 [B,S,R,P].Agent-guided candidates
are prospectively evaluated by yeast
surface display, FACS, and SPR, yielding
experimentally confirmed binders with
nanomolar to sub-nanomolar affinities.
Epitope and cell-based validation remain
future work.
Virtual Lab (123) AI–human nanobody
discovery
F1, F2, F3, F4, F5, F6.Coordinates
principal-investigator, specialist, and
critic agents to design pipelines, evaluate
structures, prioritize nanobodies, and
support experimental testing.
E1, E2, E3, E4, E5, E6.Literature, designed
sequences, ESM and AlphaFold-Multimer
outputs, Rosetta scores, expression and
solubility results, antigen-array binding, and
ELISA measurements.
V4 [B,H,P].Computationally prioritized
nanobody candidates are prospectively
tested through expression, solubility,
antigen-array, and ELISA assays in an
AI–human scientific workflow.
ORI (43) Closed-loop protein
engineering
Agent-adjacent model–laboratory
framework;F3, F4, F5.Generates and
filters proteins, preserves iterative design
state, and updates optimization using
wet-lab feedback.
E2, E3, E4, E5, E6.Ontology constraints,
generated proteins, model outputs, quality
checks, functional assays, and feedback
records.
V4 [B,P,C].Generated proteins undergo
prospective functional testing, and assay
outcomes update subsequent reinforcement-
based optimization.
Note.Prospective empirical testing of an agent-generated protein or peptide contributes qualifier P. Qualifier C is assigned only when the resulting experimental measurement changes
a subsequent design or optimization action. The scope of V4 remains claim-specific: structural validation of a peptide does not establish protein function, binding, developability,
or therapeutic utility.

Agentic Bioinformatics through Function, Evidence, and Validation, 2026, Volume , Issue31
Table S22 Cross-cutting design requirements for proteomics, structural biology, and protein-design agents.The requirements distinguish workflow
Function, inspectable Evidence, and their contribution to use-case-specific Validation.
Workflow requirement Domain-specific principle Inspectable evidence and artifacts FEV interpretation
Protein objective and constraints Define the proteomics, structural-analysis, docking,
sequence-design, simulation, or candidate-
prioritization objective and its design constraints.
Research question, target protein, desired
function, binding site, sequence constraints, assay
requirements, design objectives, and candidate-
selection criteria.
F1.Objective formulation defines
the workflow but does not establish
execution or scientific validity.
Protein and proteomics data
grounding
Resolve protein identities, sequences, structures,
domains, complexes, proteomics measurements,
ligands, templates, and candidate designs.
UniProt identifiers, FASTA sequences, PDB
structures, AlphaFold models, RPPA or mass-
spectrometry data, antibody panels, ligand
structures, multiple-sequence alignments, and assay
metadata.
E2; E3.Traceable molecular inputs
are necessary, but not sufficient, for
replayability.
Molecular tool execution Execute structure prediction, sequence design,
docking, simulation, visualization, proteomics
analysis, and candidate-scoring workflows.
Tool calls, parameters, versions, logs, generated
code, intermediate files, and outputs from
AlphaFold, ESMFold, ProteinMPNN, RFdiffusion,
Rosetta, AutoDock Vina, RDKit, and related tools.
F3; E4.Execution supports V1;
V2 additionally requires replayable
inputs, environments, parameters,
and traces.
Structural and functional
evaluation
Assess candidate structures, interfaces, dynamics,
stability, binding, developability, and predicted
biological function.
Predicted structures, pLDDT and ipTM scores,
docking poses, binding scores, Rosetta energies,
molecular-dynamics traces, secondary structures,
stability estimates, and developability metrics.
E4; E5.Computational scores
support candidate assessment,
but scientific adequacy requires
benchmark, robustness, or expert
evaluation.
Biological and mechanistic
grounding
Connect proteomics results and candidate designs
to protein function, pathways, conserved residues,
bindingmechanisms, diseasecontext, andliterature.
PubMed, UniProt, PDB, InterPro, Gene Ontology,
pathway resources, homology evidence, conserved
sites, protein–protein interactions, mechanistic
rationales, and evidence-linked reports.
E1; E2.Biological sources support
interpretation and attribution but
do not independently establish
Validation.
Design critique, filtering, and
repair
Reject implausible candidates, detect failed tools
or structural defects, apply functional and
developability filters, and revise the design workflow.
Critic outputs, failed calls, repaired code,
revised sequences, structure-quality checks, energy
thresholds, conservation constraints, liability filters,
and ranked candidates.
F4; F5; F6.Critique and filtering
are workflow capabilities whose
effectiveness must be established
through task-appropriate Validation.
Trace and provenance
preservation
Preserve the trajectory from protein inputs and
design constraints to tool execution, candidate
evaluation, selection, and reporting.
Dataset and structure identifiers, software versions,
parameters, scripts, notebooks, JSON records,
design histories, intermediate structures, simulation
files, molecular visualizations, rankings, and
limitations.
F4; E4.Provenance supports replay
and audit only when the evaluated
workflow can be reconstructed from
the reported artifacts.
Prospective functional validation Test an agent-generated protein, peptide, binder,
nanobody, or enzyme using an assay aligned with
the principal structural or functional claim.
Expression and solubility measurements, circular
dichroism, yeastsurfacedisplay, FACS,SPR,ELISA,
binding assays, enzyme-activity measurements,
thermostability assays, and design-linked
experimental records.
E6; P.V4 also requires the lower
cumulative gates;Crequires the
experimental result to change a
subsequent design action.
Note.Requirements 1–5 define the core workflow summarized in Figure S8. Requirements 6–7 operate across that workflow. Requirement 8 is optional and claim-dependent.
Archived assay measurements contribute to Evidence but not to prospective Validation unless an output generated by the evaluated workflow is directly tested.

32 Agentic Bioinformatics through Function, Evidence, and Validation, 2026, Volume , Issue
1. Protein objective
and constraints
Define the proteomics, structure,
binding, function, stability,
or sequence-design task
2. Protein and proteomics
data grounding
Resolve sequences, structures,
domains, complexes,
measurements, templates,
and candidate designs
3. Molecular tool execution
Run structure prediction, docking,
sequence design, simulation,
scoring, and visualization
Workflow
formulation
and execution
5. Biological and
mechanistic grounding
Link designs and proteomics
results to functions,
pathways, conserved sites,
mechanisms, and literature
4. Structural and
functional evaluation
Assess structures, interfaces,
dynamics, stability, binding,
function, and developability
Candidate
evaluation
and interpretation
Shared protein evidence and artifacts:FASTA sequences, UniProt and PDB records, proteomics
measurements, predicted structures, docking poses, Rosetta energies, molecular-dynamics traces, stability
and developability scores, candidate rankings, experimental protocols, and evidence-linked reports
Shared evidence
and artifacts
6. Design critique, filtering, and repair:inspect sequence and structure quality, conserved residues, docking or
energy scores, failed tools, functional constraints, developability liabilities, and revise weak candidates or workflows
7. Trace and provenance preservation:retain identifiers, design constraints, tool versions, parameters, code,
intermediate structures, simulation files, design histories, candidate rankings, expert-review records, and limitations
Cross-
cutting across
requirements 1–5
8. Optional prospective functional validation
Test an agent-generated protein, peptide, binder, nanobody, or enzyme
using expression, structural, binding, stability, or functional assays. Closed-
loop refinement requires the result to change a subsequent design action
Optional empirical
extension
Figure S8 Cross-cutting workflow blueprint for proteomics, structural biology, and protein-design agents.The core trajectory connects protein-objective
formulation and molecular-data grounding with tool-mediated structure prediction, docking, simulation, sequence design, candidate evaluation, and evidence-
linked interpretation. Shared artifacts include protein sequences, structures, proteomics measurements, docking poses, energy scores, simulation outputs,
candidate rankings, and reports. Design critique, filtering, repair, and provenance preservation operate across the workflow. Prospective functional validation
is optional. It constitutes closed-loop refinement only when the resulting experimental evidence changes a subsequent design action.

Agentic Bioinformatics through Function, Evidence, and Validation, 2026, Volume , Issue33
Table S23 Drug-discovery, therapeutic-reasoning, and molecular-design agents: target intelligence, evidence-grounded reasoning, and predictive
modelling.
System Task Function profile Evidence profile Reported V-stage and qualifiers
Target Intelligence and Evidence Access
SwiftDossier (32) Drug-target dossier
generation
F1, F3, F4, F5.Plans target assessment,
retrieves biomedical evidence, executes
sequence and enrichment tools, and
compiles traceable target dossiers.
E1, E2, E4.PubMed/PMC, UniProt,
Open Targets, DrugBank, PDB, STRING,
BLAST, enrichment outputs, citations, and
generated PDF or PowerPoint dossiers.
V2 [H,R].Executable retrieval and analysis
artifacts support replay of reported dossiers.
Expert-facing review and source checks are
reported, but broader scientific evaluation
remains limited.
Evidence-Grounded Therapeutic Reasoning
BioScientist
Agent (164)
Drug repurposing and
mechanism-of-action
reasoning
F1, F2, F3, F4, F5.Combines drug–disease
prediction, graph-path search, causal-
literature retrieval, evidence scoring, and
mechanistic report generation.
E1, E2, E4, E5.RTX-KG2, DrugBank,
ChEMBL, UniProt, DisGeNET, PubMed
causal statements, predicted links, ranked
mechanism paths, and evidence scores.
V3 [B,R].Evaluated against graph and KG-
based baselines for drug-repurposing and
mechanism-path ranking, with component
analyses. Predictions remain computational
hypotheses.
TCM-Agent (138) Traditional-
medicine network
pharmacology
F1, F2, F3, F4, F5, F6.Normalizes
herbs, compounds, targets, and diseases;
executes network, ADMET, similarity, PPI,
and enrichment analyses; and generates
evidence-graded reports.
E1, E2, E3, E4, E5, E6.TCM and
chemical databases, PubMed, compound–
target records, ADMETpredictions, PPIand
pathway outputs, mechanistic reports, and
archived experimental observations.
V3 [B,H,R,X].Evaluated on 100 curated
studies and 563 questions using multiple
model backbones, expert scoring, workflow
comparisons, and a liver-fibrosis case study.
Therapeutic claims lack prospective targeted
validation.
TXAGENT (35) Therapeutic
reasoning and
treatment
recommendation
F1, F3, F4, F5, F6.Selects tools,
retrieves current drug evidence, checks
interactions and contraindications, and
synthesizes patient- or indication-specific
recommendations.
E1, E2, E4, E5, E6.FDA labels, openFDA,
OpenTargets, HPO,PrimeKG,tooloutputs,
interaction records, treatment predictions,
and benchmark cases.
V3 [B,R].Evaluated on large drug-reasoning
and treatment benchmarks with explicit tool
traces and routing analyses. Prospective
clinical deployment and patient-outcome
validation are not established.
CLADD (63) Molecular reasoning
and prediction
F1, F2, F3, F5.Coordinates planning,
molecular retrieval, knowledge-graph
reasoning, molecular interpretation, and
predictive agents across zero-shot tasks.
E2, E3, E4, E5.SMILES strings, PubChem
annotations, PrimeKG paths, retrieved
molecular anchors, generated captions,
similarity scores, and molecular predictions.
V3 [B,R].Evaluated across drug–target,
molecular-captioning, toxicity, and
antibacterial-activity tasks against predictive
and language-model baselines. Performance
depends on retrieval and anchor coverage.
Predictive Modelling and Tool-Grounded Execution
TxGemma /
Agentic-Tx (130)
Generalist therapeutic
prediction and
reasoning
F1, F3, F4, F5.Routes therapeutic tasks
to predictive models and external knowledge
for property, toxicity, pharmacokinetic,
interaction, and trial reasoning.
E2, E3, E4, E5, E6.Therapeutics
Data Commons, molecular and biological
sequences, clinical-trial records, property
predictions, adverse-event outputs, and
reasoning traces.
V3 [B,R,X].Broadly evaluated across
therapeutic prediction, molecular reasoning,
and clinical-trial tasks with model and
retrieval comparisons. Evaluation remains
computational and retrospective.
DrugAgent (77) Drug-discovery
machine-learning
programming
F1, F2, F3, F4, F5.Coordinates solution
planning, molecular featurization, model
selection, code generation, unit testing,
execution, and self-debugging.
E2, E3, E4, E5.ADMET, HTS, and
DTI datasets; SMILES and protein
sequences; generated training code,
molecular descriptors, predictions, and
submission files.
V3 [B,R].Evaluated across ADMET,
screening, and drug–target tasks against
CoT, ReAct, and ResearchAgent, with
execution and debugging analyses.
Validation remains in silico.

34 Agentic Bioinformatics through Function, Evidence, and Validation, 2026, Volume , Issue
Table S24 Drug-discovery, therapeutic-reasoning, and molecular-design agents: tool-grounded execution, molecular screening, and lead optimization.
System Task Function profile Evidence profile Reported V-stage and qualifiers
Tool-Grounded Molecular Execution
BioChemAIgent
(161)
Protein modelling and
molecular docking
F1, F3, F4, F5, F6.Coordinates MCP
tools for molecular preparation, structure
modelling, docking, interaction analysis,
visualization, and error handling.
E2, E3, E4, E5.PubChem and PDB records,
protein and ligand structures, predicted
models, docking poses, interaction outputs,
tool logs, and molecular visualizations.
V3 [B,H,R].Evaluated using expert-curated
tasks, corrupted-query robustness tests,
four realistic expert-reviewed scenarios,
and a COX-1 docking case study. Binding
and pharmacological activity remain
computational.
DrugPilot (65) Parameterized
drug-discovery tool
execution
F1, F3, F4, F5.Maintains structured
parameters across turns, invokes predictive
and generative tools, corrects invalid calls,
and continues multi-step workflows.
E2, E3, E4, E5.TCDD tasks, molecular
and pharmacological datasets, structured
memory, tool parameters, model predictions,
generated molecules, and execution logs.
V3 [B,R].Evaluated on simple, multi-tool,
and multi-turn scenarios against ReAct,
CoT, and LoT, with ablations of memory,
feedback, and fine-tuning components.
Evaluation measures computational tool
competence.
Molecular Design and Lead Optimization
MolLingo (99) Molecular design and
lead optimization
F1, F2, F3, F4, F5.Coordinates
literature and chemistry agents for target
identification, hit discovery, fragment
growth, docking, and ADMET-aware
optimization.
E1, E2, E3, E4, E5, E6.PubMed,
UniProt, ChEMBL, molecular structures,
docking poses, ADMET predictions, toxicity
records, candidate rankings, and shared
design memory.
V3 [B,S,R,X].Evaluated across ADMET
optimization, docking-guided design,
property optimization, and hit discovery
against language-model and molecular-
design baselines. Generated leads remain
computational candidates.
MolClaw (166) Hierarchical molecular
screening and
optimization
F1, F3, F4, F5, F6.Composes validated tool
and workflow skills, applies scientific quality
gates, recovers from failures, preserves
provenance, and executes long-horizon
molecular-discovery workflows.
E2, E3, E4, E5.Molecular and protein
databases, docking and dynamics outputs,
interaction profiles, ADMET predictions,
optimized molecules, execution traces, and
quality-control records.
V3 [B,S,R].Evaluated on MolBench
screening, editing, optimization, and end-
to-end tasks, including workflows spanning
8–50 or more steps, with statistical
comparison and failure-recovery analyses.
PharmAgents(33) Virtual
pharmaceutical
discovery
F1, F2, F3, F4, F5.Coordinates target
discovery, lead generation and optimization,
docking, toxicity and metabolism
assessment, synthesizability analysis,
and experience-based refinement.
E2, E3, E4, E5.Drug and target databases,
predicted structures, generated molecules,
docking and interaction outputs, toxicity
and metabolism predictions, synthesis
assessments, reports, and experience
memory.
V2 [R].The reported virtual-pharma
workflows provide traceable multi-step
computational artifacts and iterative
refinement. Broad independent scientific
evaluation and empirical testing are not
established.
Mozi (12) Governed drug-
discovery workflow
F1, F2, F3, F4, F5, F6.Uses supervisor–
worker control, role-isolated tools, stateful
skill graphs, reflection, human checkpoints,
and auditable execution across discovery
stages.
E1, E2, E3, E4, E5.Biomedical databases,
molecular tools, workflow states, docking
and DTI scores, toxicity filters, generated
candidates, human-review records, and
execution traces.
V3 [B,H,R].Evaluated through
PharmaBench, governed tool-routing
tests, role isolation, error-containment
analyses, human checkpoints, and three
end-to-end disease case studies. Candidates
remain in silico.
Table S25 Drug-discovery, therapeutic-reasoning, and molecular-design agents: safety analysis and clinical translation.
System Task Function profile Evidence profile Reported V-stage and qualifiers
Safety and Clinical Translation
MALADE (18) Pharmacovigilance
and adverse-event
extraction
F1, F2, F3, F4, F5, F6.Selects
representative drugs, retrieves FDA labels,
extracts adverse events, aggregates evidence
by drug category, and validates outputs
through critics.
E1, E2, E3, E4, E6.FDA drug labels, NDC
records, MIMIC-IV prescriptions, OMOP
adverse-event references, retrieved passages,
confidence estimates, rationales, and critic
logs.
V3 [B,S,R].Evaluated against OMOP
adverse-event references with structured
confidence, rationales, and critic-
supported verification. Results depend
on label coverage, category mapping, and
retrospective ground truth.
AUTOCT (72) Clinical-trial outcome
prediction
F1, F3, F4, F5.Proposes, retrieves, builds,
evaluates, and refines interpretable clinical-
trial features through MCTS and classical
predictive models.
E1, E2, E3, E4, E5, E6.ClinicalTrials.gov
records, PubMed evidence, historical trial
outcomes, generated feature schemas,
predictive models, SHAP explanations, and
ROC-AUC results.
V3 [B,S,R].Evaluated on TrialBench-
derived approval, dropout, mortality, and
adverse-event tasks using interpretable
models and iterative feature refinement.
Cohorts are sampled and evaluation remains
retrospective.
EmulatRx (64) Target-trial design
and emulation
F1, F2, F3, F4, F5, F6.Coordinates trialist,
informatician, clinician, and statistician
agents to translate protocols into cohort
definitions, SQL, causal analyses, and
reviewed trial-emulation reports.
E1, E2, E3, E4, E6.Trial protocols,
MIMIC-IV and INSIGHT records, OMOP
concepts, generated SQL, propensity scores,
IPTW and clone–censor–weight outputs,
Cox models, Kaplan–Meier curves, and
endpoint analyses.
V3 [B,H,S,R,X].Evaluated on acute
and chronic target-trial emulations using
protocol, SQL, cohort, and causal-analysis
metrics, with clinical and statistical review
across multiple health-data settings.
Prospective trial-design impact is not
established.
Note.Clinical records, trial outcomes, adverse-event observations, and historical pharmacological measurements contribute to the Evidence profile, including E6 where appropriate.
They do not constitute prospective Validation unless an output generated by the evaluated workflow is directly tested in a new experimental, preclinical, or clinical setting.

Agentic Bioinformatics through Function, Evidence, and Validation, 2026, Volume , Issue35
Table S26 Cross-cutting design requirements for drug discovery, therapeutic reasoning, and molecular-design agents.The requirements distinguish
workflow Function, inspectable Evidence, and their contribution to use-case-specific Validation.
Workflow requirement Domain-specific principle Inspectable evidence and artifacts FEV interpretation
Therapeutic objective and
planning
Define whether the task concerns target assessment,
drug repurposing, molecular design, safety analysis,
treatment reasoning, trial prediction, or target-trial
emulation.
Disease indication, target or drug names, molecular
objectives, treatment constraints, trial protocols,
cohort definitions, endpoints, analysis plans, and
decision criteria.
F1.Planning defines the workflow
but does not establish execution,
therapeutic validity, or clinical utility.
Therapeutic entity grounding Resolve drugs, molecules, targets, pathways,
patients, cohorts, adverse events, trial arms, and
clinical endpoints using normalized and traceable
representations.
SMILES strings, protein sequences, compound
and target identifiers, disease ontologies, OMOP
concepts, NCT identifiers, eligibility criteria,
endpoints, adverse events, and cohort metadata.
E2; E3.Identifiable therapeutic
entities and observations are
necessary, but not sufficient, for
replayability or scientific validity.
Tool, database, and RAG
execution
Query biomedical databases, knowledge graphs,
molecular tools, safety resources, literature, and
clinical-trial repositories using traceable inputs and
explicit tool calls.
PubMed, ClinicalTrials.gov, DrugBank, ChEMBL,
UniProt, Open Targets, openFDA, PubChem,
PrimeKG, RTX-KG2, retrieved passages, API calls,
generatedSQL,toolparameters, andexecutionlogs.
F3; E1; E2; E4.Execution supports
V1; V2 additionally requires
replayable inputs, dependencies,
parameters, environments, artifacts,
and traces.
Prediction, screening, and
molecular design
Predict, generate, prioritize, or optimize therapeutic
properties, drug–target interactions, molecular
structures, toxicity, treatment responses, and trial
outcomes.
ADMET, HTS, DTI and drug-response datasets,
generated molecules, docking poses, binding scores,
toxicity predictions, synthesizability estimates,
feature schemas, model outputs, SHAP values, and
ranked candidates.
E3; E4; E5.Computational outputs
support predictive and design claims,
but require benchmark, robustness,
statistical, or expert evaluation for
V3.
Mechanistic therapeutic
reasoning
Connect predictions and recommendations to
biological mechanisms, drug–target relations,
pathways, causal evidence, disease processes, and
literature-supported rationales.
Knowledge-graph paths, mechanism-of-action
reports, pathway enrichment, drug–disease
relations, causal statements, Bradford–Hill-style
evidence, retrieved literature, citations, and
evidence-linked dossiers.
E1; E2.Mechanistic grounding
supports interpretation and
attribution but does not
independently establish therapeutic
efficacy or clinical benefit.
Safety and trial analysis Evaluate adverse events, contraindications, drug
interactions, cohort definitions, eligibility criteria,
endpoints, causal assumptions, and statistical
analysis plans.
FDA labels, openFDA records, OMOP adverse-
event references, drug–drug interactions, trial
protocols, generated SQL, propensity scores, IPTW
outputs, clone–censor–weight analyses, Cox models,
Kaplan–Meier curves, and diagnostic checks.
E3; E4; E6.Historical safety,
pharmacological, or clinical
observations contribute to Evidence
but do not independently establish
prospective Validation.
Critique, verification, and
provenance
Detect unsupported mechanisms, invalid molecules,
unsafe recommendations, weak retrieval, failed
tools, code errors, and inadequate causal or
trial assumptions; revise or escalate consequential
outputs.
Workflow states, critic logs, repaired code,
safety flags, revised protocols, retrieved citations,
knowledge-graph paths, docking files, model
outputs, tool traces, uncertainty statements,
expert reviews, approval records, and documented
limitations.
F4; F5; F6; E4.Critique, verification,
and provenance support replay and
audit, but their effectiveness must be
established through task-appropriate
Validation.
Prospective therapeutic
validation
Test an agent-generated molecule, target,
mechanism, safety prediction, treatment
recommendation, or trial decision using evidence
aligned with the principal therapeutic or clinical
claim.
Binding and functional assays, toxicity
measurements, pharmacokinetic readouts,
prospective preclinical studies, clinical-trial
outcomes, patient follow-up, treatment-response
measurements, and design-linked empirical records.
E6; P.V4 also requires the lower
cumulative gates;Crequires the
new empirical result to change
a subsequent computational,
experimental, or clinical workflow
action.
Note.Requirements 1–6 define the core therapeutic workflow summarized in Figure S9. Requirement 7 operates across that workflow, while requirement 8 is optional and claim-
dependent. Archived pharmacological, preclinical, safety, or clinical observations contribute to the Evidence profile but not to prospective Validation unless an output generated by
the evaluated workflow is directly tested. Independent retrospective cohorts may support qualifierX, but do not by themselves establish qualifierPor V4.

36 Agentic Bioinformatics through Function, Evidence, and Validation, 2026, Volume , Issue
1. Therapeutic
objective and planning
Define the target-assessment,
molecular-design, safety,
treatment, or trial-analysis task
2. Therapeutic entity grounding
Resolve drugs, SMILES, targets,
pathways, patients, cohorts, trials,
endpoints, and safety events
3. Tool, database,
and RAG execution
Query biomedical databases,
knowledge graphs, molecular tools,
safety resources, and trial records
Workflow formulation
and grounding
6. Safety and trial analysis
Evaluate adverse events,
contraindications, cohorts,
endpoints, causal assumptions,
and statistical plans
5. Mechanistic
therapeutic reasoning
Link predictions to pathways,
drug–target relations, causal
evidence, and literature
4. Prediction, screening,
and molecular design
Predict or optimize efficacy,
binding, ADMET, toxicity,
molecules, and trial outcomes
Prediction, reasoning,
and safety
Shared therapeutic evidence and artifacts:SMILES strings, targets, molecular structures,
cohort and trial metadata, retrieved passages, knowledge-graph paths, docking poses, ADMET
and toxicity predictions, causal estimates, safety records, candidate rankings, and reports
Shared evidence
and artifacts
7. Critique, verification, and provenance:preserve workflow state and traces; inspect unsupported mechanisms,
invalid molecules, safety risks, failed code, causal assumptions, uncertainty, and expert-review records
Cross-cutting
requirements 1–6
8. Optional prospective therapeutic validation
Test an agent-generated molecule, target, mechanism, safety
prediction, treatment recommendation, or trial decision using
aligned experimental, preclinical, or clinical evidence. Closed-
loop refinement requires the result to guide a subsequent action
Optional prospective
validation
Figure S9 Cross-cutting workflow blueprint for drug discovery, therapeutic reasoning, and molecular-design agents.The core trajectory connects therapeutic-
objective formulation and entity grounding with tool execution, predictive modelling, molecular design, mechanistic reasoning, and safety or trial analysis.
Shared evidence includes molecular representations, target records, retrieved sources, model outputs, safety data, causal estimates, candidate rankings, and
reports. Critique, verification, expert escalation, and provenance preservation operate across the workflow. Prospective therapeutic validation is optional and
constitutes closed-loop refinement only when the resulting evidence guides a subsequent workflow action.

Agentic Bioinformatics through Function, Evidence, and Validation, 2026, Volume , Issue37
Table S27 Computational pathology, microscopy, and spatial-imaging agents: infrastructure and image-analysis execution.
System Task Function profile Evidence profile Reported V-stage and qualifiers
Data and Model Infrastructure
PathGen-1.6M
(122)
Pathology image–text
generation
Agent-adjacent multi-agent pipeline;F2, F4,
F5.Coordinates patch-selection, captioning,
and revision models within a predefined
data-generation workflow.
E3, E4, E5.WSIs, selected patches,
captions, revision records, trained models,
and downstream predictions.
V3 [B,X].The generated resource
is evaluated on external pathology
classification, VQA, and whole-slide
benchmarks; it is not an adaptive workflow
agent.
BioEngine (91) Agent-readable
bioimage AI
infrastructure
F1, F3, F4, F6.Plans service calls, screens
andexecutesmodels, preservesartifacts, and
rejects incompatible models.
E2, E3, E4, E5.BioImage.IO models,
microscopy data, segmentation references,
analytical outputs, execution records, and
deployed applications.
V3 [B,S,R,X].Evaluated on HPA, PlantSeg,
and Lucchi++ using model comparisons,
held-out segmentation metrics, repeated
fine-tuning, and external datasets.
Microscopy and Image-Analysis Execution
Agentic
Superoptimization
(139)
Bioimaging workflow
optimization
F1, F3, F4, F5.Generates preprocessing
code, executes imaging workflows, evaluates
downstream metrics, and iteratively revises
preprocessing functions.
E3, E4, E5.Microscopy and medical images,
generated OpenCV functions, segmentation
and detection outputs, execution feedback,
validation scores, and production workflow
records.
V3 [B,S,R,X].Evaluated across spot
detection, cell segmentation, and medical-
image segmentation against expert and
AutoML baselines, with held-out scoring,
iterative optimization, and production
deployment.
LSM-Copilot (75) Fluorescence
microscopy analysis
F1, F3, F4, F5, F6.Coordinates
search, processing, and interpretation
skills for microscopy loading, segmentation,
quantification, evidenceretrieval, repair, and
reporting.
E1, E2, E3, E4.Microscopy files, method
evidence, typed skill handoffs, segmentation
and localization outputs, artifact bundles,
provenance logs, and reports.
V3 [B,S,R,X].The same skill package is
evaluated across four host settings and
public 2D/3D localization benchmarks, with
quantitative gains over raw-model baselines
and agreement with independent Imaris
measurements.
Spatial and Molecular Interpretation
QuST-LLM (47) Spatial
transcriptomics
interpretation
F1, F3, F4.Processes selected spatial
regions, extracts key genes, performs
enrichment analysis, generates biological
summaries, and maps text descriptions back
to spatial regions.
E1, E2, E3, E4, E5.WSIs, Xenium
data, registered regions, expression profiles,
GO enrichment, selected genes, language
interpretations, and region-retrieval outputs.
V2 [B].Executable spatial analysis is
demonstrated on an identifiable Xenium
dataset with reported retrieval performance.
Evaluation remains limited to case-study-
scale analysis.

38 Agentic Bioinformatics through Function, Evidence, and Validation, 2026, Volume , Issue
Table S28 Computational pathology, microscopy, and spatial-imaging agents: spatial evidence and whole-slide reasoning.
System Task Function profile Evidence profile Reported V-stage and qualifiers
Spatial and Molecular Evidence Grounding
Agent SPI-WSI
(128)
Spatial pathway
inference from RNA-
seq and WSI
F1, F3, F4, F5, F6.Generates pathway-
morphology prompts, retrieves literature,
incorporates pathologist critique, revises
prompts, and maps approved concepts onto
WSI regions.
E1, E2, E3, E4, E5, E6.WSIs, bulk RNA-
seq and pathway scores, PubMed evidence,
pathologist feedback, spatial heatmaps,
manual regions, and spatial-transcriptomics
observations.
V3 [B,H,S,R,X].Evaluated using model
comparisons, pathologist scoring, manual-
region agreement, hotspot ablations, and
spatial-transcriptomics validation across in-
house and external cohorts. The findings
remain retrospective.
LAMMI-
Pathology (116)
Molecularly informed
pathology reasoning
F1, F2, F3, F4, F5.Coordinates domain-
adapted tool agents, constructs grounded
execution trajectories, and performs
multistep image and molecular reasoning.
E1, E2, E3, E4, E5.Histopathology
images, spatial literature, molecular APIs,
tool trajectories, caption and expression-
alignment outputs, and consistency and
hallucination metrics.
V3 [B,R].Evaluated on PathSpatial-DocQA,
ST-Traj, and PathMMU against agent
and tool-use baselines, with trajectory,
consistency, redundancy, and hallucination
analyses.
CPathAgent (121) Multiscale pathology
image analysis
F1, F3, F4, F5, F6.Screens WSIs,
prioritizes regions, plans navigation,
changes magnification, integrates multiscale
evidence, and generates diagnostic reports.
E2, E3, E4, E5.WSIs, pathology
reports, selected regions, navigation traces,
visual representations, region descriptions,
diagnostic summaries, and benchmark
outputs.
V3 [B,H,R,X].Evaluated across patch,
large-region, WSI, and out-of-distribution
tasks using expert-validated questions,
pathologist assessment, and component
comparisons. Diagnostic trajectories remain
computational.
MMNavAgent
(154)
Adaptive multiscale
WSI navigation
F1, F3, F4, F5.Selects regions and
magnifications, accumulates evidence
in memory, and uses iterative zoom,
movement, and stopping decisions for slide
diagnosis.
E3, E4, E5, E6.Skin WSIs, eye-tracking
maps, tumor masks, selected patches,
navigation histories, diagnostic predictions,
and spatial-attention metrics.
V3 [B,S,R,X].Evaluated on 918 WSIs
against fixed-magnification and navigation
baselines, with classification, navigation-
consistency, tumor-overlap, and cross-
magnification ablation analyses.
PathAgent (14) Interpretable WSI
reasoning and
navigation
F1, F3, F4, F5, F6.Selects relevant regions,
extracts morphology, assesses evidence
sufficiency, requests additional regions or
magnification, and reports interpretable
diagnostic reasoning.
E2, E3, E4, E5.WSIs, retrieved RoIs,
multiscalepatches, morphologydescriptions,
navigation traces, diagnostic outputs, and
benchmark metrics.
V3 [B,H,R].Evaluated across five WSI
and pathology VQA benchmarks against
pathology and general vision–language
models, with navigation ablations and
pathologist-collaboration assessment.
WSI-Agents (83) Collaborative whole-
slide analysis
F1, F2, F3, F4, F5, F6.Routes WSI tasks
to specialist agents and models, verifies
outputs through logic, external knowledge,
and model consensus, and produces visual
reports.
E1, E2, E3, E4, E5.WSIs, pathology
knowledge, model outputs, attention maps,
verification records, consensus reports, and
VQA and reporting metrics.
V3 [B,R].Evaluated on WSI-Bench and
WSI-VQA against pathology models and
agent frameworks, with ablations of
allocation, verification, consensus, and
summarization components.
SlideSeek +
PathChat+ (144)
Whole-slide
diagnostic reasoning
F1, F2, F3, F4, F5, F6.Coordinates
supervisor and explorer agents to navigate
WSIs, formulate diagnostic hypotheses,
inspect selected regions, aggregate
multiscale evidence, and draft confidence-
aware reports.
E2, E3, E4, E5.WSIs, selected RoIs,
navigation records, morphology descriptions,
differential diagnoses, confidence scores,
diagnostic reports, and benchmark outputs.
V3 [B,H,R].Evaluated on DDxBench and
multiple RoI-level pathology benchmarks
using diagnostic accuracy, reporting metrics,
rare-disease analysis, and architecture
ablations. Evaluation remains retrospective.
Table S29 Computational pathology, microscopy, and spatial-imaging agents: biomarker and spatial-biology discovery.
System Task Function profile Evidence profile Reported V-stage and qualifiers
Biomarker and Spatial-Biology Discovery
SPARK (126) Cancer-pathology
biomarker discovery
F1, F2, F3, F4, F5, F6.Generates biological
concepts, converts them into executable
image-analysis parameters, verifies code
and outputs, and evaluates biomarker and
prognostic hypotheses.
E2, E3, E4, E5, E6.H&E WSIs, spatial-
proteomics data, cell and tissue masks,
clinical outcomes, generated code, spatial
features, survival models, SHAP values, and
ranked biomarkers.
V3 [B,S,R,X].Evaluated retrospectively
across 18 cohorts, more than 5,400 patients,
five cancer types, and multiplexed spatial-
imaging data, with reproducible feature
extraction and prognostic modelling.
SAGE (98) Knowledge-guided
pathology biomarker
discovery
F1, F2, F3, F4, F5, F6.Builds disease-
specific knowledge graphs, generates and
debates biomarker hypotheses, refines them
with human input, discovers datasets,
executes analyses, and interprets results.
E1, E2, E3, E4, E5, E6.Biomedical
knowledge graphs, literature, multimodal
patient cohorts, segmentation outputs,
pathology features, survival analyses,
treatment outcomes, hypotheses, debate
traces, and expert scores.
V3 [B,H,S,R].Evaluated through
hypothesis-quality assessment, debate
ablations, coding-agent analysis, expert
novelty and feasibility scoring, and
retrospective bladder-cancer biomarker
studies. Prospective clinical validation is not
established.
Note.Clinical outcomes and archived molecular or imaging observations contribute to the Evidence profile. Multi-cohort retrospective evaluation may support qualifiers S, R, or X,
but does not establish prospective Validation of an agent-generated biomarker or prognostic claim.

Agentic Bioinformatics through Function, Evidence, and Validation, 2026, Volume , Issue39
Table S30 Computational pathology, microscopy, and spatial-imaging agents: cross-cutting workflow platforms.
System Task Function profile Evidence profile Reported V-stage and qualifiers
Cross-Cutting Pathology Platforms
PathLab (85) Computational
pathology automation
F1, F2, F3, F4, F5, F6.Translates research
objectives into executable pathology
workflows, coordinates specialist agents,
enforces methodological guardrails, and
supports training, evaluation, interpretation,
deployment, and reporting.
E1, E2, E3, E4, E5, E6.Public
pathology datasets, image and clinical
inputs, generated DAGs, model and
segmentation outputs, survival predictions,
guardrail records, execution traces, and user-
study results.
V3 [B,H,S,R,X].Evaluated across 12
datasets and four pathology task families
using prespecified non-inferiority testing,
adversarial prompts, hallucination analysis,
workflow timing, and studies with
researchers and pathologists.
TissueLab /
TLAgent (67)
Cross-modal medical-
imaging analysis
F1, F2, F3, F4, F5, F6.Plans
explainable workflows across pathology,
radiology, and spatial omics; executes
segmentation, classification, measurement,
retrieval, visualization, memory updates,
and clinician-guided adaptation.
E1, E2, E3, E4, E5, E6.WSIs, radiology
and spatial-omics data, guideline evidence,
clinician annotations, segmentation and
classification outputs, spatial analyses,
visualizations, memory records, and
execution logs.
V3 [B,H,R,X].Evaluated across pathology,
radiology, volumetric imaging, and spatial-
omics tasks with benchmark comparisons,
expert feedback, visual provenance, and
active-learning adaptation. Prospective
deployment and outcome validation remain
unestablished.
Table S31 Cross-cutting design requirements for computational pathology, microscopy, and spatial-imaging agents.The requirements distinguish
workflow Function, inspectable Evidence, and their contribution to use-case-specific Validation.
Workflow requirement Domain-specific principle Inspectable evidence and artifacts FEV interpretation
Image objective and context
grounding
Identify the imaging modality, tissue, magnification,
spatial assay, cohort, acquisition context, and
biological or clinical objective.
H&E WSIs, microscopy images, spatial-omics data,
pathology reports, cohort metadata, acquisition
settings, modality labels, and analysis goals.
F1; E3.Grounded image inputs
support workflow formulation but
do not independently establish
replayability.
Region, cell, and spatial
representation
Convert images into biologically meaningful regions,
cells, tissue compartments, spatial neighborhoods,
and multiscale morphological features.
WSI tiles, RoIs, nuclei and cell masks,
tumor/stroma regions, cell coordinates, spatial
graphs, morphology captions, and marker profiles.
E3; E5when learned representations
are used. Representation quality
requires separate evaluation.
Image-analysis tool execution Execute registration, segmentation, quantification,
navigation, classification, model adaptation, and
spatial-analysis workflows.
QuPath, QuST, Cellpose-SAM, MCMICRO,
BioImage.IO models, generated code, parameters,
model checkpoints, execution logs, masks, and
overlays.
F3; E4.Execution supports V1;
V2 additionally requires replayable
inputs, environments, parameters,
artifacts, and traces.
Quality control and uncertainty Assess registration, segmentation, region selection,
magnification, model confidence, missing evidence,
and analytical failure modes.
Registration metrics, segmentation scores,
confidence estimates, QC logs, failed calls,
corrected regions, uncertainty flags, and pathologist
review.
F5; F6; E4; E5.Quality-control
effectiveness must be established
through benchmarks, diagnostics,
robustness analysis, or expert
assessment.
Biological and spatial grounding Link image-derived observations to molecular
measurements, tissue architecture, spatial
organization, pathways, biomarkers, and pathology
knowledge.
Spatial transcriptomics, multiplexed markers, GO
terms, gene-expression outputs, biomarker labels,
spatial neighborhoods, literature, and evidence-
linked interpretations.
E1; E2; E3; E6.Molecular,
pathological, or clinical observations
support interpretation but do not
independently establish prospective
Validation.
State, navigation, and repair Preserve image-analysis state, navigation history,
region selections, tool failures, corrections, and
revised analytical decisions.
Navigation traces, selected tiles, magnification
histories, planner states, failed tool calls, repaired
code, revised parameters, and reviewer feedback.
F4; F5.State and repair records
support inspection and replay when
the complete workflow can be
reconstructed.
Provenance-preserving reporting Report the complete image-to-evidence trajectory,
including source images, regions, analytical
outputs, biological interpretations, uncertainty, and
limitations.
Captions, overlays, RoI coordinates, heatmaps,
JSON records, code, parameters, navigation paths,
model outputs, statistical results, and review
records.
F4; F6; E4.Provenance supports
replay, audit, and expert review but
is not itself a scientific Validation
result.
Prospective biological or clinical
validation
Test an agent-generated diagnosis, biomarker,
spatial interpretation, prognostic claim, or imaging-
derived hypothesis using evidence aligned with the
principal claim.
Prospective cohorts, molecular assays, functional
experiments, clinical follow-up, treatment-response
evaluation, and design-linked empirical records.
E6; P.V4 also requires the lower
cumulative gates;Crequires the
new result to change a subsequent
workflow action.
Note.Requirements 1–5 define the core image-to-evidence trajectory summarized in Figure S10. Requirements 6–7 operate across that trajectory. Requirement 8 is optional
and claim-dependent. Retrospective cohorts, clinical outcomes, independent datasets, and pathologist review contribute to Evidence or Validation qualifiers but do not establish
prospective Validation unless an output of the evaluated workflow is directly tested.

40 Agentic Bioinformatics through Function, Evidence, and Validation, 2026, Volume , Issue
1. Image objective
and context grounding
Resolve modality, tissue,
magnification, spatial assay,
cohort, acquisition, and objective
2. Region, cell, and
spatial representation
Represent regions, cells, tissue
compartments, morphology,
spatial neighborhoods, and scale
3. Image-analysis tool execution
Run registration, segmentation,
quantification, navigation,
classification, and spatial analysis
Image grounding
and execution
5. Biological and spatial grounding
Link image findings to
molecular measurements,
tissue architecture, pathways,
biomarkers, and literature
4. Quality control and uncertainty
Check registration, segmentation,
region selection, magnification,
confidence, and missing evidence
Quality control
and interpretation
Shared imaging evidence and artifacts:WSIs, microscopy and spatial-omics data, RoIs,
image tiles, cell and tissue masks, spatial coordinates, morphology features, model outputs,
QC metrics, molecular measurements, biomarker records, statistical results, and reports
Shared evidence
and artifacts
6. State, navigation, and repair:preserve selected regions, magnification paths,
workflow state, failed calls, corrected code, revised parameters, and expert feedback
7. Provenance-preserving reporting:retain source images, RoIs, overlays, navigation traces,
parameters, analytical outputs, molecular evidence, uncertainty, review records, and limitations
Cross-cutting
controls 6–7
8. Optional prospective biological or clinical validation
Test an agent-generated diagnosis, biomarker, spatial interpretation,
prognostic claim, or imaging-derived hypothesis using aligned
biological, experimental, or clinical evidence. Closed-loop
refinement requires the result to guide a subsequent action
Optional prospective
validation
Figure S10 Cross-cutting workflow blueprint for computational pathology, microscopy, and spatial-imaging agents.The core trajectory connects image and
tissue-context grounding with biologically meaningful spatial representation, domain-tool execution, quality control, and evidence-linked interpretation. Shared
artifacts include source images, regions, cells, spatial coordinates, analytical outputs, molecular measurements, quality metrics, and reports. State maintenance,
navigation capture, repair, verification, and provenance preservation operate across the workflow. Prospective biological or clinical validation is optional and
constitutes closed-loop refinement only when the resulting evidence guides a subsequent action.

Agentic Bioinformatics through Function, Evidence, and Validation, 2026, Volume , Issue41
Table S32 General bioinformatics workflow agents: evidence access and executable workflow orchestration.
System Task Function profile Evidence profile Reported V-stage and qualifiers
Assistance and Evidence Access
GFA / NagGPT
(20)
Interactive genomics
querying and analysis
F1, F3, F5.Rewrites invalid database
requests, correctsAPIcalls, injectswarnings,
and supports sequence retrieval, alignment,
prediction, and exploration.
E2, E4.NCBI, Ensembl, UniProt and
FlyBase records, transformed queries,
Biopython outputs, alignments, predictions,
and interaction traces.
V1 [R].Interactive execution and
middleware-based correction are
demonstrated, but silent errors remain and
complete replayability is not established.
BRAD (105) Biomarker and
enrichment workflow
assistance
F1, F3, F4, F5.Combines document
retrieval, database search, enrichment
analysis, external software execution,
logging, and report generation.
E1, E2, E3, E4.RNA-seq inputs, PubMed
and arXiv passages, GO and Enrichr results,
citations, JSON logs, reasoning traces, and
generated reports.
V2[B,R].Openworkflowartifactsandaction
logs support replay. Evaluation includes
enrichment recovery, citation accuracy, and
reproducibility analyses, but the system
remains primarily assistive.
Executable Workflow Orchestration
AutoBA (173) Autonomous omics
analysis
F1, F3, F4, F5.Plans analyses, installs
tools, writes and executes Bash workflows,
records completed steps, and revises failed
operations.
E2, E3, E4.WGS/WES, RNA-seq, scRNA-
seq, ChIP-seq, ATAC-seq and spatial data;
generated plans, scripts, tool outputs, logs,
and reports.
V2 [H,R].Executable plans, code, and
outputs support replay of representative
workflows. Expert bioinformaticians assessed
several omics use cases, but broader
scientific evaluation remains limited.
BioMaster (117) Multi-step
bioinformatics
automation
F1, F2, F3, F4, F5, F6.Coordinates
planning, task execution, debugging,
and checking agents; retrieves workflow
knowledge, generates scripts, repairs
failures, and validates intermediate outputs.
E1, E2, E3, E4.Multi-omics datasets,
workflow and tool documentation, retrieved
examples, generated scripts, execution
traces, debugginglogs, andcheckedoutputs.
V3 [B,R].Replayable workflows are
evaluated across 20 bioinformatics tasks
against AutoBA and ChatGPT, with
ablations of planning, tool retrieval, and
checking components.
Agentomics (90) Autonomous
biomedical ML
experimentation
F1, F3, F4, F5, F6.Explores datasets,
selects representations and models,
generates reusable code, executes iterative
experiments, evaluates hidden test sets, and
exports complete artifacts.
E2, E3, E4, E5.Twenty biomedical datasets,
foundation models, generated training and
inference code, containerized environments,
model artifacts, deterministic metrics, and
complete execution traces.
V3 [B,S,R,X].Evaluated through 60
runs across 20 datasets using held-out
tests, triplicate execution, deterministic
metrics, workflow-completion analysis, and
comparisons with agentic and reported
human solutions.
Biomni (50) General-purpose
biomedical task
execution
F1, F3, F4, F5.Composes and executes
workflows over a unified biomedical action
space for database querying, sequence
analysis, multi-omics tasks, and tool-
supported reasoning.
E1, E2, E3, E4, E5.Biomedical databases,
sequence and omics inputs, tool calls,
intermediate outputs, model predictions,
workflow traces, and benchmark answers.
V3 [B,R].Evaluated on biomedical database,
sequence, and workflow benchmarks with
tool-use and task-level comparisons.
Validation remains computational and
depends on a largely curated action space.
BioMedAgent
(11)
Self-evolving
biomedical data
analysis
F1, F2, F3, F4, F5, F6.Plans,
codes, executes, repairs, and summarizes
biomedical analyses while building reusable
planning, coding, and tool memories.
E1, E2, E3, E4, E5.BioMed-AQA tasks,
omicsandclinicaldatasets, specializedtools,
generated code, statistical and visualization
outputs, memory records, and milestone
traces.
V3 [B,R,X].Evaluated on 327 executable
tasks and 172 knowledge questions using
milestone scoring, tool and memory
ablations, biomedical case studies, and
external generalization to BixBench.

42 Agentic Bioinformatics through Function, Evidence, and Validation, 2026, Volume , Issue
Table S33 General bioinformatics workflow agents: verification, self-evolution, and experimentally grounded discovery.
System Task Function profile Evidence profile Reported V-stage and qualifiers
Verification and Self-Evolution
STELLA (55) Self-evolving
biomedical research
F1, F2, F3, F4, F5.Coordinates
manager, developer, critic, and tool-creation
agents while expanding reusable reasoning
templates and computational tools.
E1, E2, E4, E5.PubMed, ClinVar, PDB,
biomedical benchmarks, model and tool
outputs, reasoning templates, tool-creation
records, and iterative trial traces.
V3 [B,R].Evaluated on biomedical
knowledge, literature, and database
benchmarks, with repeated computational
trials showing test-time template and tool
adaptation. Prospective empirical validation
is not established.
Alvessa (115) Evidence-grounded
functional genomics
F1, F2, F3, F4, F5, F6.Recognizes
entities and intent, orchestrates validated
tools, generates source-grounded answers,
verifies individual statements, and revises
unsupported claims.
E1, E2, E4, E5.Functional-genomics and
drug databases, retrieved records, predicted
structures and pockets, citations, tool
outputs, verifier feedback, and revision
traces.
V3 [B,R].Evaluated through GenomeArena
and LAB-Bench DbQA, tool-routing
accuracy, statement-level provenance,
adversarial verification, and drug-target
assessment case studies.
Experimentally Grounded Discovery
Co-Scientist (39) Hypothesis generation
and experimental
planning
F1, F2, F4, F5, F6.Generates, critiques,
ranks, debates, and evolves scientific
hypotheses through persistent memory,
tournament-style comparison, and scientist
oversight.
E1, E2, E4, E5, E6.Literature and web
evidence, ranked hypotheses, debate and
review traces, drug and target candidates,
experimental plans, and prospective in-vitro
readouts.
V4 [B,H,R,P].Scientist-reviewed hypotheses
are connected to prospective experiments in
drug repurposing, fibrosis-target discovery,
and antimicrobial-resistance research.
Closed-loop computational refinement from
the new assay results is not consistently
established.
BioLab (54) End-to-end life-
sciences research
F1, F2, F3, F4, F5, F6.Coordinates
planning, reasoning, memory, retrieval, code
execution, critique, reporting, biological
models, protocol design, and experimental
feedback.
E1, E2, E3, E4, E5, E6.Literature,
xBio-Tools, biological foundation models,
computational predictions, workflow traces,
CRISPR measurements, antibody-assay
results, and experimental reports.
V4 [B,H,R,P].Benchmarked against general
and biomedical agents and prospectively
evaluated through T-cell perturbation and
PD-1 antibody assays. Physical experiments
remain human-mediated, and closed-loop
autonomous experimental refinement is not
clearly established.
Note.Prospective testing of an agent-generated hypothesis, target, perturbation, or candidate contributes qualifier P. Qualifier C should be assigned only when the resulting empirical
measurement is returned to the system and changes a subsequent computational or experimental action.
Table S34 Cross-cutting design requirements for general bioinformatics workflow agents.The requirements distinguish workflow Function, inspectable
Evidence, and their contribution to use-case-specific Validation.
Workflow requirement Domain-general principle Inspectable evidence and artifacts FEV interpretation
Research objective and planning Translate a biological question into explicit data
requirements, analytical steps, dependencies,
outputs, constraints, and stopping criteria.
Research goal, dataset description, task
decomposition, workflow plan, expected outputs,
constraints, and decision points.
F1.Planning defines the workflow
but does not establish execution or
validity.
Data and task routing Identify the biological modality and route each task
to appropriate tools, databases, APIs, models, or
specialist agents.
RNA-seq, ChIP-seq, WGS/WES, single-cell, spatial,
protein and molecular inputs; routing decisions, tool
assignments, and modality-specific metadata.
F2; F3; E3.Correct routing is
necessary for execution but does not
independently establish replayability.
Evidence-grounded workflow
specification
Ground analytical choices in literature, software
documentation, biological databases, protocols, and
validated workflow examples.
PubMed passages, database records, tool
documentation, protocols, workflow examples,
citations, software requirements, and retrieved
evidence.
E1; E2.Retrieved evidence supports
workflow selection and interpretation
but does not itself establish
Validation.
Executable code and pipeline
generation
Translate the grounded plan into executable scripts,
notebooks, commands, or pipeline stages while
managing dependencies and outputs.
Bash, Python and R code, notebooks,
environments, tool calls, parameters, command
histories, intermediate files, execution logs, and
final artifacts.
F3; E4.Execution supports V1;
V2 additionally requires replayable
environments, inputs, parameters,
artifacts, and traces.
Workflow state, critique, and
repair
Maintain state, inspect failed calls and weak
intermediate results, revise plans, repair code, and
rerun affected workflow steps.
Shared state, critic outputs, debug logs, failed
commands, corrected plans, repaired scripts,
memory updates, revision histories, and tool-
creation records.
F4; F5.Repair effectiveness must
be established through benchmark,
robustness, or task-appropriate
scientific evaluation.
Verification and provenance
preservation
Verify outputs and preserve the complete trajectory
from research objective and evidence retrieval to
execution, interpretation, review, and reporting.
Dataset identifiers, software versions, scripts,
notebooks, logs, citations, intermediate artifacts,
verification records, expert reviews, uncertainty, and
limitations.
F4; F6; E4.Provenance supports
replay and audit when the evaluated
workflow can be reconstructed from
reported artifacts.
Cross-domain robustness and
transfer
Evaluate whether the workflow-control layer
transfers across biological modalities, tools,
datasets, and unseen task formulations.
Multi-domain benchmarks, unseen datasets, prompt
perturbations, execution trajectories, ablations,
failure analyses, external tasks, and expert
comparisons.
B; R; Xwhere supported. Cross-
domain claims require evaluation
beyond isolated demonstrations.
Prospective experimental
validation
Test an agent-generated hypothesis, candidate,
perturbation, protocol, or intervention using
evidence aligned with the principal claim.
Prioritized hypotheses, perturbation assays,
CRISPR readouts, antibody assays, functional
measurements, experimental reports, and feedback
records.
E6; P.V4 also requires the lower
cumulative gates;Crequires the
new empirical result to change a
subsequent workflow action.
Note.Requirements 1–4 define the core workflow summarized in Figure S11. Requirements 5–7 operate across that workflow. Requirement 8 is optional and claim-dependent.
Archived experimental observations contribute to Evidence but not to prospective Validation unless an output generated by the evaluated workflow is directly tested.

Agentic Bioinformatics through Function, Evidence, and Validation, 2026, Volume , Issue43
1. Research objective and planning
Translate the biological goal
into data requirements,
analytical steps, outputs,
constraints, and decisions
2. Data and task routing
Identify the biological
modality and assign suitable
tools, databases, models,
APIs, or specialist agents
3. Evidence-grounded
workflow specification
Ground analytical choices in
literature, documentation,
protocols, databases,
and workflow examples
Workflow formulation
and grounding
4. Executable code
and pipeline generation
Generate and run scripts,
notebooks, commands, or
pipeline stages while managing
dependencies and artifacts
Executable workflow
generation
Shared workflow evidence and artifacts:research goals, dataset descriptions, modality
metadata, retrieved documentation, protocols, citations, workflow plans, generated scripts,
software environments, intermediate files, execution logs, analytical outputs, and reports
Shared evidence
and artifacts
5. Workflow state, critique, and repair:maintain analytical state; inspect failed calls and
weak intermediate results; revise plans, repair code, update memory, and rerun affected steps
6. Verification and provenance preservation:retain dataset identifiers, evidence links, software versions,
parameters, code, intermediate artifacts, verification outputs, uncertainty, expert-review records, and limitations
7. Cross-domain robustness and transfer:evaluate workflow control across biological
modalities, tools, datasets, unseen tasks, prompt variations, and external benchmarks
Cross-cutting
controls 5–7
8. Optional prospective experimental validation
Test an agent-generated hypothesis, candidate, perturbation, protocol,
or intervention using evidence aligned with the principal claim.
Closed-loop refinement requires the result to guide the next action
Optional prospective
validation
Figure S11 Cross-cutting workflow blueprint for general bioinformatics workflow agents.The core trajectory connects research-objective formulation and
data routing with evidence-grounded workflow specification and executable pipeline generation. Shared artifacts include retrieved evidence, scripts, software
environments, intermediate files, execution logs, analytical outputs, and reports. State maintenance, repair, verification, provenance preservation, and cross-
domain evaluation operate across the workflow. Prospective experimental validation is optional and becomes closed-loop refinement only when the resulting
evidence guides a subsequent action.

44 Agentic Bioinformatics through Function, Evidence, and Validation, 2026, Volume , Issue
Table S35 Benchmarks and evaluation infrastructure for agentic bioinformatics: evidence retrieval and general workflow evaluation.
Resource Evaluation scope What it evaluates FEV contribution Principal limitation
Evidence Retrieval and Verification
Tool-Augmented
Biomedical LLM
Benchmark (127)
Biomedical API and
tool calling
Tests structured function calling for rsID-to-
position and rsID-to-gene mapping through
NCBI dbSNP and Entrez Gene across more
than 100 model endpoints.
Evaluates tool selection and invocation (F3),
integration of structured database records (E2),
returned API outputs (E4), factual consistency,
latency, and expert-scored correctness under
multiple tool-access conditions.
Covers a small set of atomic
retrieval tasks rather than complete
bioinformatics workflows.
PubMed Reasoner
(167)
Dynamic literature
retrieval and
biomedical QA
Evaluates self-critical MeSH query
refinement, iterative PubMed retrieval,
evidence sufficiency, early stopping, and
citation-grounded answer generation.
Tests retrieval planning and revision (F1, F5),
literaturegrounding(E1), PMID-levelprovenance,
query precision and recall, retrieval depth, answer
quality, and computational cost.
Focuses on biomedical QA rather
than executable molecular-data
analysis or experimental workflow
validation.
AMG-RAG (111) Dynamic medical
knowledge-graph
retrieval
Evaluates confidence-scored entity–relation
extraction, knowledge-graph construction
and updating, adaptive traversal, and graph-
grounded medical QA.
Supports structured evidence grounding (E2)
through graph relations, confidence values,
provenance metadata, Neo4j records, and
benchmarked QA over MEDQA and MedMCQA.
Evaluation is centred on medical QA
and depends on source authority,
extraction quality, and expert
oversight.
KGAREVION (119) Biomedical
knowledge-graph
verification
Evaluates generation, review, and revision
of biomedical triplets before answering
knowledge-intensive questions from verified
graph evidence.
Tests self-evaluation and repair (F5), structured
knowledge (E2), inspectable triplets, UMLS
mappings, graph verification, benchmark
performance, generalization, and Review/Revise
ablations.
Does not evaluate executable
sequencing, omics, perturbation, or
protein-design workflows.
DeepEvidence (143) Long-horizon
biomedical evidence
synthesis
Evaluates multi-agent exploration of
literature, biomedical databases, clinical-
trial resources, and APIs while constructing
provenance-preserving evidence graphs.
Tests coordinated retrieval and synthesis (F1, F2,
F3, F4), literature and structured knowledge (E1,
E2), conflict detection, evidence-gap analysis,
target prioritization, and clinical-trial reasoning.
Produces computational evidence
syntheses that still require expert,
experimental, or clinical evaluation.
Process-Aware and Executable Workflow Evaluation
Open-Rosalind
BioBench (136)
Process-aware
biological-agent
evaluation
Evaluates bounded tools, deterministic
skills, hybrid routing, workflow-constrained
execution, citation-grounded synthesis, and
replayable traces across sequence and
protein tasks.
Operationalizes Function through tool routing
and execution (F1, F3, F4), Evidence through
mandatory tool-derived support (E2, E4), and
Validation support through accuracy, tool
correctness, citationpresence, tracecompleteness,
and failure rate.
The benchmark is small and
partly internal; external hold-out
performance shows sensitivity to
routing, tool coverage, and scorer
normalization.
BioML-bench (93) End-to-end
biomedical machine
learning
Tests whether agents can interpret task
capsules, build data pipelines, train
predictive models, and submit held-out
predictions across protein, single-cell,
imaging, and drug-discovery tasks.
Evaluates planning and executable model
development (F1, F3), biological inputs and
software outputs (E3, E4, E5), completion rates,
leaderboard percentiles, AUROC, Spearman
correlation, and other task-specific metrics.
Focused on supervised prediction;
failures may reflect execution
scaffolding rather than biological
reasoning alone.

Agentic Bioinformatics through Function, Evidence, and Validation, 2026, Volume , Issue45
Table S36 Benchmarks and evaluation infrastructure for agentic bioinformatics: general executable workflow evaluation.
Resource Evaluation scope What it evaluates FEV contribution Principal limitation
General Executable Workflow Evaluation
BioXArena (66) Multimodal
biomedical ML
coding
Tests dataset inspection, representation and
model selection, code generation and repair,
training, and held-out prediction across 76
tasks and nine biomedical domains.
Evaluates planning, execution, and repair (F1,
F3, F5); multimodal biological data and model
outputs (E3–E5); hidden graders, execution
traces, robustness tests, ablations, failure modes,
and cost.
Performance combines biological
modelling, data-interface handling,
scaffold reliability, and backbone
capability under a limited compute
budget.
ScienceAgent
Bench (16)
Scientific code
generation
Evaluates generation of self-contained
Python programs for 102 data-analysis
and visualization tasks derived from 44
publications across several scientific fields.
Tests executable code production (F3; E4),
valid execution, task success, CodeBERTScore,
contamination controls, API cost, rubric-based
assessment, and the effect of supplied expert
knowledge.
Not specific to bioinformatics and
limited to Python-centric tasks; even
strong systems complete only a
minority of problems.
PromptBio-Bench
(40)
File-centric
bioinformatics
workflows
Evaluates 194 expert-curated tasks spanning
genomics, transcriptomics, proteomics,
single-cell analysis, multi-omics, statistics,
and machine learning from natural-language
prompts and input files.
Tests task interpretation and execution (F1,
F3), heterogeneous biological and computational
artifacts (E3, E4), completion, accuracy, output-
file similarity, runtime, token usage, and text or
image judging.
Expert reference files may represent
only one valid workflow, while
LLM-based grading and single-pass
evaluation can introduce bias.
BixBench (94) Realistic
bioinformatics
analysis
Evaluates 61 analysis capsules and 205
open-answer questions requiring dataset
exploration, notebook execution, multistep
analysis, and biological interpretation.
Tests planning, code execution, and interpretation
(F1, F3); biological datasets and notebook
artifacts (E3, E4); and realistic analysis
trajectories rather than final-answer recall alone.
Frontier-model accuracy remains
low, human baseline coverage
is incomplete, and open-answer
evaluation partly depends on model-
based judging.
BioAgent Bench
(31)
Multistep
bioinformatics
pipelines and
robustness
Evaluates ten genomics and omics workflows
requiring tool use, file handling, pipeline
execution, progress tracking, outcome
validity, and concrete output artifacts under
controlled perturbations.
Tests execution, state, and repair (F3–F5);
biological inputs and pipeline artifacts (E3, E4);
and robustness to prompt bloat, decoy references,
corrupted inputs, model changes, and harness
changes.
The relatively small task set and
model-based grader limit coverage;
benchmarksuccessdoesnotestablish
biological validity of downstream
findings.
BioMed-AQA (11) Biomedical data-
analysis agents
Evaluates planning, tool selection, code
execution, repair, statistics, visualization,
interpretation, and reporting across 327
executable tasks and 172 knowledge
questions.
Tests most Function categories (F1–F6) using
milestone-based assessment, tool-use evaluation,
repair analysis, memory ablations, and external
generalization to BixBench; artifacts contribute
primarilyE3–E5.
Combines heterogeneous tasks and
scoring procedures and remains
limited to computational workflow
competence.

46 Agentic Bioinformatics through Function, Evidence, and Validation, 2026, Volume , Issue
Table S37 Domain-specific agent benchmarks: genomics, gene editing, and single-cell analysis.
Resource Evaluation scope What it evaluates FEV contribution Principal limitation
Genomics and Gene-Editing Evaluation
GenoTEX (73) Gene-expression and
gene–trait analysis
Evaluates dataset selection, expression
and clinical-data preprocessing, batch and
confounder control, statistical workflow
construction, and recovery of trait-
associated genes.
Provides 1,384 problems from 911 GEO
and TCGA datasets with expert workflows,
intermediate artifacts, Lasso and mixed-model
outputs, and reference genes. It tests planning
and execution (F1, F3) withE3–E5artifacts and
scientific outcome evaluation.
Restricted to transcriptomic gene–
trait workflows; alternative valid
preprocessing and modelling choices
may differ from reference analyses.
GenomeArena (115) Evidence-grounded
functional genomics
Evaluates entity recognition, database and
tool routing, evidence synthesis, statement-
level provenance, verification, and revision of
unsupported functional-genomics claims.
Tests planning, tools, and verification (F1, F3,
F5, F6); literature, structured knowledge, and
software outputs (E1, E2, E4); source-linked
claims; and adversarial fabricated identifiers or
numerical assertions.
Centred on database-oriented
research assistance rather than
raw-data bioinformatics pipelines;
performance depends on database
and tool coverage.
GeneEditingBench
(109)
CRISPR and gene-
editing planning
Evaluates interpretation of editing
objectives, CRISPR modality selection,
guide and primer design, delivery reasoning,
experimental constraints, specialized tool
use, and downstream plans.
Tests planning, coordination, tool execution, and
verification (F1, F3, F6) over literature, structured
CRISPR knowledge, and design-tool outputs (E1,
E2, E4). Its associated system study also reports
prospectively tested editing workflows.
Cannot represent all cell-type,
delivery, off-target, biosafety, and
laboratory constraints; benchmark
performance alone does not establish
prospective validity.
Single-Cell Analysis Evaluation
scBench (145) Executable scRNA-
seq analysis
Evaluates data-grounded single-cell tasks
from realistic workflow snapshots, each
containing a data state, natural-language
instruction, and deterministic grader.
Tests planning and execution (F1, F3) onE3/E4
artifacts through 394 problems, six sequencing
platforms, seven task categories, deterministic
grading, and task- and platform-level accuracy.
Snapshot-based tasks cover bounded
analytical steps and do not establish
experimental validity of newly
generated findings.
Single-Cell Omics
Agent Benchmark
(79)
Cross-framework
single-cell workflows
Evaluates 50 scRNA-seq, spatial, scATAC-
seq, and multi-omics tasks across multiple
agent frameworks, language models, and
Python or R environments.
Tests planning, tools, retrieval, execution, and
repair (F1, F3–F5); biological and computational
artifacts (E3, E4); 18 metrics, ground-truth
scripts, robustness tests, module ablations, and
failure diagnosis.
Performance depends on benchmark-
specific environments, retrieval
resources, reference scripts, and
included analytical modules.
CellBench (6) Published scRNA-seq
workflow reproduction
Evaluates whether agents can infer, execute,
and interpret analyses reported across 76
published scRNA-seq studies and extend the
analyses through new hypotheses.
Tests workflow planning, execution, state, and
interpretation (F1, F3, F4) using published
dataset contexts, notebook artifacts, author-
conducted analyses, and expert-reviewed
trajectories.
Published analyses are neither unique
nor necessarily optimal; agreement
does not validate newly generated
biological hypotheses.

Agentic Bioinformatics through Function, Evidence, and Validation, 2026, Volume , Issue47
Table S38 Domain-specific agent benchmarks: spatial omics, protein design, and drug discovery.
Resource Evaluation scope What it evaluates FEV contribution Principal limitation
Spatial and Spatial-Proteomics Evaluation
SpatialBench (146) Executable spatial-
transcriptomics
analysis
Evaluates interaction with real-world spatial
data, platform-aware workflow execution,
andrecoveryofcomputationalandbiological
results using deterministic graders.
Tests planning and execution (F1, F3) using
E3/E4artifacts across 146 problems, five
spatial technologies, seven task categories, data
snapshots, deterministic graders, models, and
harnesses.
Success demonstrates bounded
spatial-analysis competence rather
than biological or clinical validity of
new interpretations.
SP-Bench (163) Spatial-proteomics
workflow execution
Evaluates preprocessing, illumination
correction, registration, segmentation,
quantification, clustering, phenotyping,
annotation, and interpretation across 102
tasks and 18 categories.
Tests domain-tool execution and workflow
completion (F3, F4) using multiplexed tissue-
imaging inputs and computational outputs (E3,
E4), including quantification and annotation-
quality metrics.
Performance depends on expert-
curated skills, templates, workflow
contracts, and the included spatial-
proteomics tools.
Protein-Design Agent Evaluation
BioDesignBench
(61)
Protein-design
workflow behaviour
Evaluates 76 expert-curated antibody,
enzyme, binder, scaffold, and fluorescent-
protein design tasks using 17 wrapped
design tools and human, algorithmic, and
agent baselines.
Tests planning, tool selection, design, candidate
scoring, comparison, and filtering (F1, F3, F5)
over sequences, structures, model outputs, and
biophysical scores (E3–E5), including trace-level
behaviour.
All evaluation is in silico; scoring
and model-based judging do not
experimentally validate generated
proteins.
Drug-Discovery Workflow Evaluation
TCDD (65) Drug-discovery tool
calling
Evaluates tool selection, parameter
extraction, structured memory, multi-
function and multi-turn execution, and
recovery from parameter errors using 2,800
annotated examples.
Tests routing, execution, state, and repair (F1,
F3–F5) across eight predictive or generative drug
tools, with function and parameter accuracy and
controlled error scenarios.
Assesses tool-use behaviour rather
than the pharmacological validity of
generated molecules or predictions.
PharmaBench (101) Governed therapeutic
workflows
Evaluates 88 tasks covering target
identification, DTI, ADMET, toxicity,
drug response, preclinical reasoning, and
experimental decision-making.
Tests stage-aware planning and tool use (F1, F3)
over structured therapeutic inputs and predictions
(E3–E5) using accuracy, F1, SMAPE, exact
match, and comparisons across agents and model
backbones.
Aggregate scores conflate model
knowledge, tool-interface quality,
and workflow orchestration; success
does not establish therapeutic
validity.
MolBench (52) Molecular screening
and optimization
Evaluates molecular screening, editing,
physicochemical optimization, and long-
horizon structure-based discovery workflows
spanning 8–50 or more steps.
Tests multistep execution, recovery, quality
gates, and provenance (F3–F5) over molecular
structures, docking outputs, property predictions,
and optimized candidates (E3–E5), with expert
rubrics and formal statistical analyses.
Evaluation remains in silico and does
not establish experimental affinity,
activity, toxicity, or safety.
Table S39 Domain-specific agent benchmarks: computational pathology and whole-slide reasoning.
Resource Evaluation scope What it evaluates FEV contribution Principal limitation
Pathology Agent Evaluation
WSI-Bench (68) Whole-slide
morphology and
reasoning
Evaluates gigapixel WSI understanding
across morphology, diagnosis, treatment-
oriented reasoning, reporting, and pathology
VQA using 180,000 question–answer pairs
from 9,850 slides and 30 cancer types.
Tests image-grounded reasoning and
interpretation (F1, F3) using WSIs, morphology
evidence, model outputs, and report artifacts
(E3–E5), with pathology-specific precision,
relevance, and VQA metrics.
Itisaretrospectivebenchmarkrather
than an autonomous diagnostic
workflow, and success does not
establish prospective clinical validity.
ST-Traj (116) Pathology tool-
execution trajectories
Evaluates tool selection and ordering,
intermediate-observation interpretation,
trajectory consistency, redundant calls,
hallucination, and answer agreement over
6,818 multistep trajectories.
Tests execution, state maintenance, and
verification (F3, F4, F6) using grounded tool
interactions and computational traces (E4),
including Tool Consistency F1, Trajectory
Success, Answer Consistency, redundancy, and
hallucination metrics.
Higher-level trajectories are partly
model-assembled and bounded by
theincludedpathologyandmolecular
tools.
DDxBench (144) Whole-slide
differential diagnosis
Evaluates WSI navigation, region
and magnification selection, iterative
diagnostic refinement, multiregion evidence
integration, and visually grounded reports
across 150 slides and 55 neoplastic diseases.
Tests planning, navigation, state, and verification
(F1, F3, F4, F6) using WSI regions, morphology
evidence, confidence values, diagnostic outputs,
pathologist review, architecture ablations, and
failure analysis.
The benchmark is small, single-
institution, non-public, and limited
toneoplasticdiagnoses; retrospective
accuracy does not establish clinical
deployment validity.
Note.Benchmark and evaluation resources are not assigned independent V-stages in these tables. Instead, they provide evidence for classifying evaluated system use cases.
Demonstrated benchmark execution may support V1; V2 additionally requires sufficient environments, inputs, parameters, artifacts, and traces for replay; and V3 requires task-
appropriate scientific evaluation. Benchmark comparisons, expert assessment, statistical analysis, robustness testing, and external evaluation may be recorded through qualifiersB,
H,S,R, andX, respectively. Benchmark performance alone does not establish prospective empirical Validation, qualifierP, or V4.
