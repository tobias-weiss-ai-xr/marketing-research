---
title: 'Right-Sizing LLM-Agent Decomposition in VAT Determination: A Pilot Controlled Sweep'
url: https://arxiv.org/abs/2608.23395
category: ai-marketing
subcategory: empirical
date: 2026-08
venue: ''
authors:
- Pedro Santos
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.23395
pages: 29
chars: 110718
fetched_at: '2026-11-08T13:34:40+00:00'
kb_version: 1
---

# Right-Sizing LLM-Agent Decomposition in VAT Determination: A Pilot Controlled Sweep

Right-Sizing LLM-Agent Decomposition in V AT
Determination:
A Pilot Controlled Sweep
Pedro Santos
Independent Researcher
pedromiguelbsantos@gmail.com
ORCID: 0009-0007-3191-9617
Abstract
Recent LLM-agent systems make conflicting design bets: decompose work across
many narrow agents, or use one strong tool-using agent. This pilot studies that
choice on bounded cross-border V AT determination with reverse charge, where
every case has an oracle label under a fixed rule set and the intermediate decisions
— classification, jurisdiction, rate, exemption, and reverse-charge logic — are
independently scoreable.
We hold the activity surface fixed — subtasks, tools, I/O schemas, validation checks,
orchestrator, base model, and merge policy — and vary only the assignment of
subtasks to workers across four orchestrated configurations, from one wide worker
to five narrow ones, compared against S0, a tuned no-orchestrator ReAct/function-
calling single agent, with a deterministic rule engine as oracle. The program
comprises 4,400 runs: a 40-case, five-repeat main sweep, matched-token arms
separating prompt-budget from agent-count effects, and three failure-injection
arms, all evaluated against pre-registered falsification criteria.
The two intermediate configurations lead on accuracy (0.830, against endpoints
at 0.720 and 0.770) but do not meet the pre-stated bar against the fine endpoint,
so the intermediate-optimum hypothesis remains unsupported at pilot scale — a
directional result. The single agent does not Pareto-dominate the orchestrated set.
The pre-registered matched-token criterion fires: the budget-matched single agent
lands 6.5 points below the leading configuration, but the interval includes zero, so
any advantage is reported as consistent with a prompt-budget explanation. Under
injection, availability faults — timeout and shared-tool outage — are absorbed
at every granularity, with wide-scope restart over-recovering its own baseline by
+0.160, while a single schema-conforming hallucinated record degrades every
configuration and inverts the ordering, hitting fragmented configurations hardest.
The contribution is a bounded, preregistered pilot heuristic for right-sizing agent
decomposition in V AT-style determination — place one partition boundary at the
dependency-layer midpoint — released with oracle, dataset, harness, raw traces,
and analysis pipeline.
1 Introduction
Recent LLM-agent systems make conflicting design bets about whether complex work should be
decomposed across narrow agents or handled by one strong tool-using agent. Anthropic reports
that an orchestrator–subagent research system improved an internal research benchmark by 90.2%
over a single Claude Opus 4 agent, at roughly 15 × the token cost [Anthropic, 2025]. Cognition
argues that multi-agent designs are fragile because context and implicit decisions are dispersed across
Preprint.
arXiv:2608.23395v1  [cs.MA]  24 Aug 2026

agents [Yan, 2025]. Recent single-agent work, including OneFlow and Operand Quant, further
challenges the assumption that orchestration is necessary for strong performance [Xu et al., 2026,
Sahney et al., 2025]. At the same time, Chen et al. [2024] show that compound LLM systems can
scale non-monotonically with the number of calls: more calls can help, then hurt.
The unresolved question is empirical: what changes when only agent scope changes? Many prominent
comparisons vary the orchestration framework, base model, prompt budget, tool surface, and task at
the same time. This leaves the narrower effect of agent-scope granularity under-controlled.
This paper reports a pilot controlled sweep of agent-scope granularity on cross-border V AT deter-
mination with reverse charge. V AT determination is a deliberate testbed choice. Each case has
an oracle label under a bounded V AT rule set, making accuracy unambiguous within the harness.
The workflow decomposes into auditable intermediate decisions — classification, jurisdiction, rate,
exemption, and reverse-charge logic — each independently scoreable. Token cost and median latency
are operationally meaningful metrics. The task combines parallelizable lookups and classifications
with sequential dependency in the final reverse-charge decision.
We hold theactivity surfacefixed: the required subtasks, tools, I/O schemas, validation checks,
base model family, and merge policy remain constant. Across four orchestrated configurations
C1–C4, we vary only how that surface is assigned to workers, from one wide orchestrated worker
to increasingly narrow workers, under a preregistered merge policy. We compare these againstS0,
a tuned ReAct/function-calling single agent with no orchestrator.C1 is not treated as a baseline;
it is the one-worker orchestrated control that separates orchestration overhead from no-orchestrator
single-agent behavior — a distinction usually conflated in the literature. A deterministic rule engine
serves as oracle and validator, not as a competitor.
To address the concern that multi-agent gains may be prompt-budget gains, we run a matched-token
comparison between S0 and a pre-specified orchestrated reference — the dependency-layer midpoint
— with a post-selection sensitivity arm at the best-performing configuration. To probe robustness, we
inject two isolated failure modes — timeout and hallucinated output — plus one shared-tool-outage
condition that tests the boundary of localized fallback under correlated dependency failure.
Findings.The program comprises 4,400 valid runs evaluated against three pre-registered falsification
criteria (§6.6). The two intermediate configurations lead the main sweep at 0.830 accuracy against
endpoints of 0.720 (wide) and 0.770 (fine), and error localization shows why: wide scopes fail earliest
at jurisdiction determination, the finest scope at reverse-charge synthesis, with the intermediates
minimizing the total. The pre-stated material bar against the fine endpoint is nonetheless not met,
so the intermediate-optimum hypothesis remains unsupported for this workload — a directional
pilot reading, not evidence of absence. S0 does not Pareto-dominate the orchestrated set. The
confirmatory matched-token contrast is −0.065 with a confidence interval including zero, so the
pre-registered criterion fires and any C2 advantage is reported as consistent with a prompt-budget
explanation, even though the point estimate favors C2. Under injection, availability faults are
absorbed at every granularity — with wide-scope restart over-recovering its own un-injected baseline
by +0.160 — while a single schema-conforming hallucinated record degrades every configuration,
hits the fragmented ones hardest, and inverts the main-sweep ordering.
Contributions.(1) A controlled pilot methodology that holds the activity surface, tools, model
family, I/O schema, orchestrator, and merge policy fixed across C1–C4, with S0 evaluated separately,
three falsification criteria fixed before results inspection, and a fully released artifact — oracle,
dataset, harness, raw traces, and analysis pipeline. (2) Main-sweep results on 40 oracle-labeled
cases with five stochastic repeats per condition: a non-monotonic granularity curve with both
intermediates at 0.830, case-clustered bootstrap confidence intervals, effect sizes, and earliest-
failing-subtask error localization. (3) A matched-token comparison whose pre-registered criterion
fires, disciplining the prompt-budget-versus-agent-count reading. (4) A failure-injection taxonomy:
availability perturbations — timeout and shared-tool outage — absorbed at every granularity, with a
wide-scope restart overshoot, versus a content perturbation — a schema-conforming hallucinated
record — that degrades all configurations and inverts the ordering.
Research questions.RQ1: how does orchestrated granularity affect accuracy, median latency, token
cost, and error type? RQ2: which configurations are Pareto-efficient or dominated? RQ3: how
much of the observed effect remains under a matched-token comparison with S0? RQ4: how does
granularity affect localized fallback under isolated failures and shared-tool outage?
2

Scope.This is a pilot. We study one V AT-style workload, one base model family, four orchestrated
granularity levels, and synthetic failure injections. The result is a bounded candidate heuristic for
V AT-style determination workflows, not a general design rule for enterprise agents.
2 Related Work
We organize related work around four questions needed for a controlled agent-granularity sweep:
when multi-agent orchestration helps, how prior systems choose role granularity, how compound
LLM systems scale with calls and prompt budget, and how legal-critical agent systems handle
validation and failure.
Agent-proliferation debate.Recent LLM-agent systems provide empirical pressure on both sides of
the multi-agent debate. Magentic-One [Fourney et al., 2024] reports a generalist orchestrator–worker
architecture in which a lead orchestrator plans, tracks progress, and re-plans while delegating to
specialized workers, with statistically competitive results on GAIA, AssistantBench, and WebArena;
it serves as the closest architectural antecedent for our orchestrator. Tian et al. [2025] benchmark
multi-turn multi-agent orchestration against strong single-LLM baselines on GPQA-Diamond, IFEval,
and MuSR, including ablations on authorship visibility and vote observation. Li [2026] studies when
multi-agent systems can be compiled into single-agent skill libraries, reporting a capacity-like phase
transition in skill selection that hierarchical routing can mitigate. Magentic Marketplace [Bansal et al.,
2025] extends this orchestration line to environment-level evaluation, contributing an open-source
simulated two-sided market in which assistant agents representing consumers transact with competing
service agents at scale. These studies motivate agent-count and role-scope questions, but they do not
jointly fix the activity surface, orchestrator, tool set, schema, model family, and merge policy while
varying only agent scope.
Decomposition and role granularity.Classical MAS treats decomposition as a design problem:
role-based methodologies [Pavón and Gómez-Sanz, 2003, Cossentino et al., 2005] and learned role-
discovery systems show that the choice of role scope affects coordination and performance. RODE
[Wang et al., 2020] decomposes joint action spaces into restricted role action spaces; Dynamic Role
Discovery [Xia et al., 2023] reports 55–60% average win-rate drops after ablating role-discovery
components, evidence that role granularity is causally important rather than incidental. Karimadini
and Lin [2009] formalize the stronger point that local decomposition must preserve global behavior,
so granularity choices are not arbitrary. In the LLM era, MetaGPT [Hong et al., 2023], ChatDev
[Qian et al., 2023], and AutoGen [Wu et al., 2023] popularized fixed narrow-role systems, while
Miyazaki et al. [2026] vary decomposition granularity in a financial trading domain and TDAG [Wang
et al., 2025] generates subagents dynamically while emphasizing error propagation. Microservices
granularity studies [Vera-Rivera et al., 2021, Mendonça Filho and Mendonça, 2024, Zhao et al.,
2025] provide a methodological analogue: they treat unit scope as an independent variable and
measure performance, cost, and energy under controlled decompositions. We borrow this controlled-
experiment logic while treating probabilistic outputs, context-window coupling, and non-deterministic
fallback as LLM-MAS-specific phenomena.
Compound-system scaling and prompt-budget confounds.Chen et al. [2024] derive scaling laws
for compound inference systems and show that V ote and Filter-V ote can scale non-monotonically with
call count: additional calls can improve performance and then degrade it. This motivates testing for a
bounded optimum rather than assuming more agents are better. A separate concern is that multi-agent
gains may reflect total prompt budget rather than agent count. OneFlow [Xu et al., 2026] argues that
many homogeneous MAS workflows use the same base LLM and differ mainly by prompts, tools,
and workflow position, and that strong single-agent workflows can match them at lower cost. Operand
Quant [Sahney et al., 2025] adds a complementary single-agent challenge in ML-engineering settings,
reinforcing that S0 must be a tuned tool-using baseline rather than a weak no-agent strawman. Su
et al. [2025] further suggest that workflow complexity should be matched to query difficulty rather
than fixed globally. RQ3 addresses this confound through a matched-token comparison between S0
and the best orchestrated configuration.
Tax/legal-critical agents and fault handling.Gogani-Khiabani et al. [2026] present Synedrion,
the closest tax-prep agent system: a role-based LLM framework with metamorphic testing for
legal-critical tax software, reporting that GPT-4o-mini inside the agentic system outperforms GPT-
4o and Claude 3.5 on complex tax-code tasks (45% worst-case pass rate vs. 9–15%). Synedrion
3

evaluates one architecture; we instead sweep granularity on a bounded V AT workflow with oracle
labels. LegalBench [Guha et al., 2023] and SARA [Holzenberger et al., 2020] provide adjacent
statutory-reasoning context, while rule-based tax engines motivate deterministic validation rather
than learned baselines. On recovery, work on fault-tolerant “graceful degradation” [Lin et al., 2019]
distinguishes full recovery to the original specification from recovery to states satisfying only a
critical subset of requirements; this pilot reports the narrower quantity of localized fallback under
isolated injections. Large-scale failure taxonomies of LLM multi-agent systems [Cemri et al., 2025]
further document coordination and recovery failures in deployed frameworks, but do not provide
controlled measurements of fallback quality as a function of agent scope. RQ4 addresses that gap
with timeout, hallucinated-output, and shared-tool-outage injections.
Position.To our knowledge, this is the first controlled pilot on V AT-style tax determination to vary
only agent scope under a fixed activity surface — holding the orchestrator, base model family, tools,
I/O schema, and merge policy fixed — while including a tuned no-orchestrator single-agent baseline
(S0) kept distinct from the one-worker orchestrated condition (C1), a matched-token control, and a
localized-fallback protocol.
3 V AT Determination as a Testbed
We use cross-border V AT determination with reverse charge as the testbed for the granularity sweep.
The choice is methodological rather than domain-specific: V AT determination is bounded enough to
support oracle-labeled evaluation, yet structured enough to expose the coordination trade-offs that
motivate agent decomposition. In particular, it has three properties useful for this study. First, each
case has an unambiguous label under the bounded rule set used in the harness, so accuracy is well-
defined. Second, the task decomposes into a fixed sequence of intermediate decisions — classification,
jurisdiction, rate, exemption, and reverse-charge logic — that can be scored independently. Third,
token cost and median latency are meaningful metrics because tax determination is commonly
executed at transactional volume and must preserve an auditable decision trace.
3.1 Bounded V AT task
Each case represents a structured cross-border transaction with invoice-level attributes, party attributes,
and one or more line items. The input schema includes supplier country, customer country, customer
V AT-registration status, B2B/B2C status, line-item descriptions, line-item amounts, and a bounded
product/service classification vocabulary. The output is a structured V AT determination containing
the applicable jurisdiction, rate treatment, exemption status, reverse-charge status, liable party, V AT
amount or non-charging reason, and rule references.
The rule set is modeled on EU-style V AT treatment for domestic supply, intra-community B2B
supply with reverse charge, B2C supply with rate differences, and mixed goods/services invoices.
For reverse-charge scenarios, the harness includes rules modeled on general B2B place-of-supply and
reverse-charge logic of the kind associated with Council Directive 2006/112/EC. The implementation
is deliberately bounded: it does not attempt to encode the full V AT law of any Member State,
special-sector schemes, or real-time legislative updates. Its purpose is to provide a controlled activity
surface with oracle labels, not to serve as a deployable V AT engine, and the harness makes no
legal-compliance claims.
3.2 Activity surface
We define the activity surface as the tuple A= (T,I,O,V,F,D,R) , where T is the set of required
subtasks, I and O are typed input and output schemas, V is the validation-check set, F is the tool set,
D is the dependency partial order, and R is the fixed set of read-only reference materials available to
the harness.
The required subtasksTare fixed across all experimental conditions:
1. Goods/services classification.Classify each line item into the bounded product/service vocabulary
used by the rule engine.
4

2. Jurisdiction determination.Determine the place of supply and applicable V AT jurisdiction using
supplier country, customer country, customer V AT-registration status, B2B/B2C status, and the
classification result.
3.Rate lookup.Retrieve the applicable rate treatment for the jurisdiction and classification.
4.Exemption check.Evaluate the line item against the bounded exemption table.
5. Reverse-charge decision.Determine whether V AT is charged by the supplier or self-accounted
for by the customer, using the prior decisions and the transaction status.
The tool set F is also fixed: a classification reference, a V AT-registration validity check, a rate-table
lookup, and a rule-citation retrieval tool. Each subtask emits a structured JSON record containing the
decision, supporting fields, and rule reference.
In this pilot, R consists of the bounded exemption table. Any additional static reference material
must be declared in the released configuration and held fixed across all conditions. Unlike tools in F,
references in R are not callable external operations; they are static, read-only materials that condition
decisions but do not execute computation.
Validation checksV enforce schema conformance, required-field presence, rule-citation presence, and
internal consistency between the emitted decision and the cited rule. For example, a reverse-charge
output must be consistent with the jurisdiction decision, customer status, and B2B/B2C classification;
a rate output must correspond to an entry in the bounded rate table; and an exemption output must
cite an exemption-table rule when an exemption is asserted.
The dependency relation D reflects both parallel and sequential structure. Line-item classification
can be performed directly from the initial line-item fields and does not depend on jurisdiction, rate,
exemption, or reverse-charge outputs. The V AT-registration validity check can be called directly
from the customer V AT-registration field and is consumed by jurisdiction determination. Jurisdiction
determination depends on classification and customer status. Rate lookup and exemption checking
depend on the jurisdiction and classification decisions and can proceed in parallel once those inputs
are available. The final reverse-charge decision depends on all prior subtasks. This structure makes
V AT determination suitable for testing agent granularity: some work can be decomposed across
narrow workers, while final correctness still depends on coordinated synthesis.
All orchestrated configurations C1–C4 and the no-orchestrator baseline S0 implement the same
activity surface. The required subtasks, tools, schemas, validation checks, reference materials, and
dependency structure do not change across conditions. Within the orchestrated sweep C1–C4, only
the assignment of subtasks to workers changes; S0 is evaluated separately as a no-orchestrator
comparator.
3.3 Ground truth and dataset
The dataset contains 40 synthetic V AT cases generated under the bounded rule set. The deterministic
rule engine emits both the final V AT determination and the labeled intermediate decisions for each
subtask. The rule engine is used as the oracle and validator for evaluation; it is not treated as a
competing agentic baseline.
Cases are stratified across four scenario families, with ten cases per family:
1. Domestic supply.Supplier and customer are in the same jurisdiction, with standard rate or
exemption treatment.
2. Intra-community B2B with reverse charge.Supplier and V AT-registered customer are in
different jurisdictions, exercising reverse-charge logic.
3. B2C with rate differential.Customer status changes the applicable place-of-supply and rate
treatment.
4. Mixed goods/services invoices.A single case includes line items requiring different classification,
rate, or exemption handling.
A stratified subset of cases — at least one per scenario family, with additional coverage of cases that ex-
ercise reverse-charge eligibility, exemption handling, B2B/B2C transitions, and mixed goods/services
classification — is manually spot-checked after generation. The spot check is not used to alter model
5

outputs; it is used only to verify that the oracle labels generated by the rule engine conform to the
bounded rule specification.
3.4 Auditable intermediate evaluation
Because each subtask emits a structured record with a rule citation, the testbed scores both final
determinations and intermediate decisions. Final-answer accuracy measures whether the resulting
V AT treatment matches the oracle label. Step-level accuracy measures whether each subtask output
matches the corresponding oracle intermediate label. Citation completeness measures whether each
emitted decision includes the required rule reference. Consistency checks measure whether the trace
is internally coherent, even when the final answer is incorrect.
A final V AT error can arise from different sources: misclassification, incorrect jurisdiction selection,
wrong rate lookup, missed exemption, or incorrect reverse-charge synthesis. Because every config-
uration emits the same structured trace, the testbed can localize where errors enter as agent scope
changes. The granularity sweep can therefore measure not only whether a configuration is correct,
but also how its error profile changes when work is assigned to wider or narrower agents.
3.5 Scope of the testbed
The testbed is synthetic and bounded by design. It does not cover the full V AT rule space of any
jurisdiction, real invoice parsing, supplier master-data defects, or production posting and reporting
semantics. It also does not make legal-compliance claims.
Within those limits, the harness is appropriate for a pilot controlled sweep. It is rule-faithful enough
to make oracle labels meaningful, structured enough to support auditable step-level evaluation,
and narrow enough that the activity surface can be fully specified and held constant across all
configurations. The resulting evidence should therefore be read as a bounded heuristic for V AT-style
determination workflows, not as a general claim about tax automation or enterprise agents.
4 Configurations
This section defines the experimental conditions used in the granularity sweep. All orchestrated
configurations C1–C4 implement the activity surface A defined in §3.2. The no-orchestrator baseline
S0 implements the same activity surface without an orchestrator. Across conditions, the required
subtasks, tools, reference materials, schemas, validation checks, dependency structure, base model
family, decoding settings, timeout threshold, and logging protocol are held fixed. Retry opportunities
are fixed within each condition’s natural repair unit and reported explicitly because S0 and C1–C4
expose different repair granularities.
Within the orchestrated sweep C1–C4, the experimental variable is the assignment of subtasks
to workers. S0 is not part of that sweep; it is a separate no-orchestrator comparator that differs
from C1–C4 in two respects simultaneously — it has no task ledger, no progress ledger, and no
dependency-ordered dispatch, and its repair unit is the whole trace rather than the subtask. S0 is
therefore analyzed alongside C1–C4 rather than as a point on the granularity curve, and is kept
distinct from C1 throughout (§4.5).
4.1 Agent definition
Anagentin this study is a tuple
a= (r, Pr, Fr, Sr, πr),
where r is the role, Pr is the role-scoped prompt, Fr ⊆ Fis the tool-permission subset, Sr ⊆
I ∪ O ∪ Ris the subset of input fields, prior outputs, and read-only reference materials visible to
the agent, and πr is the interaction protocol governing how the agent receives inputs and returns
structured outputs. Here R denotes the set of static reference materials available to the harness —
bounded lookup tables and reference documents that are read-only and not callable as tools. In this
pilot, R consists of the bounded exemption table; any additional static reference material must be
6

declared in the released configuration and held fixed across all conditions. I and O are as defined in
§3.2.
Two agents are treated as distinct when they differ in role, tool permissions, state scope, or interaction
protocol. Prompt wording alone is not sufficient. This definition addresses the homogeneity critique
of multi-agent systems [Xu et al., 2026]: in the narrower configurations, workers differ not only by
prompt, but also by permitted tools, visible state, expected schema, and position in the dependency
graph.
We distinguishtool permissions Fr fromvisible state Sr. Tools are callable external operations from
the fixed set F defined in §3.2. Visible state is the subset of case fields, prior subtask outputs, and
static reference materials that the agent receives as input. The two are kept conceptually separate
throughout §4.3 to avoid the impression that workers in narrower configurations are differently
advantaged on tooling when they merely receive different state slices.
4.2 Orchestrator and fixed controls
All orchestrated configurations use the same Magentic-One-style orchestrator [Fourney et al., 2024].
The orchestrator maintains two ledgers. Thetask ledgerrecords open subtasks for the current case
and their dependency status. Theprogress ledgerrecords completed subtasks, emitted structured
records, validation outcomes, retry counts, and unresolved failures.
For each case, the orchestrator dispatches subtasks according to the dependency partial order D.
Independent subtasks may be dispatched in parallel when D permits. If a worker output fails
validation, times out, or emits an incomplete structured record, the orchestrator retries that subtask
up to the fixed per-subtask retry budget. After the budget is exhausted, the case is marked with the
corresponding failure status and the available trace is retained for error analysis. The orchestrator
is implemented as deterministic control logic over these ledgers: because the dependency order D
is fixed and known, dispatch, validation, and retry require no orchestrator-level model calls, and all
model calls in C1–C4 are worker calls.
The following controls are invariant across C1–C4:
• the orchestrator implementation and ledger semantics;
• the base model family, pinned model version, and decoding settings;
• the tool setFand tool implementations;
• the reference setR;
• the input and output schemasI,O;
• the validation checksV;
• the dependency orderD;
• the timeout threshold, the per-subtask retry budget, and the concurrency cap;
• trace logging, token accounting, and latency measurement.
The orchestrator is therefore not a variable in the sweep. Only the partition of subtasks across workers
changes.
4.3 Orchestrated configurations C1–C4
The five subtasks inTare abbreviated as follows:
•CLS:goods/services classification;
•JUR:jurisdiction determination;
•RAT:rate lookup;
•EXM:exemption check;
•RCH:reverse-charge synthesis.
The four orchestrated configurations are defined by the following partitions ofT:
7

CLS JUR
RAT
EXM
RCH
L1 L2 L3 L4
 (transitive
reduction)
dependency-layer midpoint
C1 CLS JUR RAT EXM RCH 1 worker
C2 CLS JUR RAT EXM RCH 2 workers
C3 CLS JUR RAT EXM RCH 3 workers
C4 CLS JUR RAT EXM RCH 5 workers
S0 CLS JUR RAT EXM RCH no orchestrator
Figure 1: The fixed activity surface and the experimental conditions. Top: the five subtasks and the
transitive reduction of the dependency order D, with dependency layers L1–L4. Bottom: worker
partitions C1–C4 and the no-orchestrator baseline S0; the dashed vertical line marks the dependency-
layer midpoint used by the merge policy (§4.4) and the matched-token reference (§6.3).
Configuration Worker count Worker assignment
C11{CLS, JUR, RAT, EXM, RCH}
C22{CLS, JUR},{RAT, EXM, RCH}
C33{CLS},{JUR},{RAT, EXM, RCH}
C45{CLS},{JUR},{RAT},{EXM},{RCH}
Figure 1 depicts the dependency orderDand these partitions alongside S0.
For C1–C3, each worker receives the union of visible state and tool permissions required by the
subtasks assigned to that worker; C4 is listed explicitly below because it is the finest decomposition
and exposes the most restrictive permission slices.
C1is the one-worker orchestrated control. A single worker receives the full case, has access to
the full tool set F, and emits all five structured subtask records under the orchestrator’s ledger and
validation loop.
C2separates pre-rate determination from downstream tax treatment. The first worker performs
classification and jurisdiction determination. The second worker receives the validated outputs from
the first worker and performs rate lookup, exemption checking, and reverse-charge synthesis.
C3separates classification from jurisdiction while keeping downstream rate, exemption, and reverse-
charge reasoning co-resident. This configuration tests whether isolating the two earliest decision
points reduces error propagation without fully fragmenting the downstream synthesis step.
C4is the finest decomposition. Each worker is responsible for exactly one subtask and receives only
the visible state required for that subtask. Tool permissions are restricted to the subset of F relevant
to each subtask:
• the classification worker receives the line-item descriptions as visible state and the classification
reference tool;
• the jurisdiction worker receives supplier country, customer country, B2B/B2C status, customer
V AT-registration status, and the classification output as visible state, and the V AT-registration
validity check and rule-citation retrieval tools;
8

• the rate worker receives the jurisdiction and classification outputs as visible state and the rate-table
lookup tool;
• the exemption worker receives the jurisdiction and classification outputs as visible state, the
bounded exemption table fromRas visible state, and the rule-citation retrieval tool;
• the reverse-charge worker receives the case line items and all prior structured records as visible state,
and the rule-citation retrieval tool. The line items are included because reverse-charge synthesis
computes the V AT amount from the applicable rate and the line-item amounts; every field required
by a subtask’s contractual output is part of that subtask’s visible state.
The bounded exemption table is treated as visible state from the reference set R rather than as a
tool because it is a static reference distributed to whichever worker handles EXM, not a callable
operation in F. The fixed tool set F in §3.2 — classification reference, V AT-registration validity
check, rate-table lookup, and rule-citation retrieval — is therefore unchanged across all conditions.
C1 is not treated as a single-agent baseline. It is an orchestrated one-worker condition. Its comparison
with S0 isolates the cost and behavior of the orchestrator itself. Comparisons among C1–C4 isolate
the effect of changing worker scope under a fixed orchestrator.
4.4 Merge policy
The C1–C4 partitions follow a single pre-specified merge policy:dependency-layer clustering.
Starting from the finest decomposition in C4, adjacent subtasks are merged only when doing so
preserves the topological order of D. Parallel-eligible subtasks that share immediate dependencies
are kept co-resident in coarser configurations and separated only in the finest configuration. The
policy was committed to the project repository under version control before any results from the main
sweep were inspected.
This policy yields the progression from C4 to C1 as follows. C4 assigns one worker per subtask. C3
merges the downstream rate, exemption, and reverse-charge subtasks because they all depend on
validated jurisdiction and classification outputs. C2 further merges classification with jurisdiction,
producing a pre-treatment worker and a downstream treatment worker. C1 merges all subtasks into
one wide orchestrated worker.
Two alternative policies were considered before the sweep but excluded from the primary analysis:
tool-locality clustering, which groups subtasks by shared tools, andsemantic-similarity clustering,
which groups subtasks by overlap in rule families. Including them would introduce a second
experimental variable. The primary study therefore evaluates granularity under one fixed, dependency-
respecting merge policy; robustness across merge policies is deferred to follow-on work and discussed
as a limitation in §10.
4.5 No-orchestrator baseline S0
S0 is a tuned ReAct/function-calling single agent with no orchestrator, no task ledger, and no progress
ledger. It receives the full case, has access to the full tool set F and the full reference set R, and
emits the same structured trace as the orchestrated configurations. Its output is evaluated using the
same schemas and validation checks.
S0 is designed as a strong comparator rather than a weak strawman. It uses:
1. the same base model family and decoding settings as C1–C4;
2. the same tools and tool implementations;
3. the same input and output schemas;
4. the same validation checksV, applied after trace emission;
5. up to three whole-trace repair attempts after validation failure, which is the natural repair unit
available without an orchestrator;
6. a prompt tuned on a held-out development split separate from the 40 evaluation cases.
The held-out development split contains eight cases drawn from the same generator as the evaluation
set. These cases are used only for prompt tuning and are excluded from all reported evaluation results.
The final S0 prompt, tuning budget, and development-case identifiers are reported in the appendix.
9

Fairness principle for retries.Each condition is granted equal retry opportunities at its natural
repair unit: subtask-level for C1–C4, whole-trace-level for S0. This creates different worst-case call
counts across conditions. We therefore treat retry-induced call volume as part of the measured cost of
each architecture, rather than forcing an artificial equal-call cap that would distort either S0 or the
orchestrated configurations.Per-condition retry counts, tool calls, and token usage are recorded per
run in the released artifact; §7 reports total token cost as the primary cost metric.
S0 and C1 are kept separate throughout the analysis. S0 measures no-orchestrator single-agent
behavior. C1 measures one-worker behavior under the orchestrator, ledgers, validation loop, and retry
policy. Conflating these conditions would mix orchestration overhead with agent-scope effects.
4.6 Execution controls and logging
All conditions use fixed decoding settings: temperature 0.2 and a fixed maximum-token cap per call.
Nucleus sampling (top-p) is left at the provider default because the provider API rejects requests that
set temperature and top-p simultaneously; sampling is therefore controlled through temperature alone.
Tool ordering, case ordering, and validation execution are deterministic. The provider API does not
expose decoding-seed control, so stochastic variance is estimated from repeated executions under the
same decoding settings.
Each (condition, case) pair is run five times to support bootstrap confidence intervals over stochastic
and case-level variance (§6). The timeout threshold is fixed at 120 s per model call across all
conditions.
Concurrency is capped so that parallel-eligible workers in C2–C4 do not contend for provider-side
rate-limit capacity. This avoids attributing provider queuing delays to agent granularity. Wall-clock
latency is measured from case submission to final validated trace or terminal failure. Token usage
is logged per call and aggregated per case. The logs also record tool calls, validation failures, retry
counts, timeout events, emitted rule citations, and final error categories.
The main sweep uses one pinned base model family. Heterogeneous-model variants are not run in
this pilot; their omission is treated as a scoping decision and discussed in §10 (Threats to Validity).
5 A Chain-Error Model
We introduce a small analytical model to state prior expectations for the granularity sweep and to give
§7 a vocabulary for interpreting observed patterns. The model isinterpretive, not predictive: we do
not use it to forecast configuration-level results, and we do not fit it to held-out configurations before
reporting the sweep. Following Chen et al. [2024], we treat the relationship between decomposition
and end-to-end quality as potentially non-monotonic rather than assuming that more calls or more
workers necessarily improve performance.
5.1 Chain-error baseline and cross-step dependence
Each orchestrated configuration implements the activity surface A at fixed logical depth d= 5
corresponding to the required subtasks T={CLS,JUR,RAT,EXM,RCH} . The worker count k
varies across C1–C4; the logical depth does not. Let Ci ∈ {0,1}indicate whether subtask i emits
the oracle-correct structured decision under configuration c, with marginal correctness probability
p(c) i =P(C i = 1|c) , and let A(c) =P(C 1 = 1, . . . , Cd = 1|c) denote trace-level case
accuracy. Under independent per-step correctness and no retry repair, A(c) indep = Qd i=1 p(c) i . Because
all five subtasks are required, improvements to any required subtask affect trace-level accuracy
multiplicatively.
The independence baseline is a reference point, not an assumption. Errors in LLM-agent pipelines are
rarely independent: a wrong classification can bias jurisdiction, rate, exemption, and reverse-charge
reasoning, while shared visible state and handoff dependencies can induce correlated failures across
workers. Observed trace accuracy can therefore deviate from Q i p(c) i in either direction — upward when errors cluster on the same hard cases, downward when they are dispersed or introduced by
handoff-specific failures. We do not estimate a single correlation parameter in this pilot. §7 reports
10

error-type breakdowns by earliest failing subtask; full step-error co-occurrence tables ship with the
released analysis outputs.
S0 is not a point on the C1–C4 granularity curve. It implements the same activity surface without an
orchestrator, ledgers, or subtask-level repair. We therefore use the model primarily for C1–C4 and
treat the S0–C1 contrast separately in §5.4.
5.2 Worker scope
Worker scope affects the marginal terms p(c) i , and the expected sign is not fixed. Wider workers have
access to more neighboring context and may perform better on synthesis-heavy subtasks — especially
RCH, which depends on all prior decisions — but longer prompts and broader visible state can also
increase interference between unrelated rule contexts. Narrower workers reduce role scope, tool
access, and visible state, which can improve local decision quality by limiting irrelevant context, but
can also fragment information across handoffs and increase dependence on inter-worker message
quality. Different subtasks may therefore prefer different scopes within the same configuration. The
sweep is designed to measure these effects rather than impose a monotonic expectation.
5.3 Retry repair
Validation and retry change effective step accuracy for failures that are detectable and repairable
within budget. Let q(c) i denote the conditional probability that an initially incorrect or invalid subtask
output for i is detected by V and successfully repaired within the retry budget under configuration c.
The effective post-retry step accuracy is
˜p(c) i =p (c) i +  1−p (c) i  q(c) i .
This expression folds together detectability by validation and successful correction after retry; it
therefore applies only to validation-visible failures. Silent semantic errors that satisfy the schema and
cite a plausible rule may not be repaired even when they are wrong under the oracle.
For C1–C4, repair occurs at the subtask level exposed by the orchestrator’s ledgers: a failed CLS
record can be retried before JUR consumes it; a failed RAT record can be retried without regenerating
the full trace. S0 differs structurally. It emits a complete trace and receives whole-trace repair
attempts after validation failure, so its repair effect is better represented at the joint-trace level:
˜A(S0) =A (S0) +  1−A (S0) Q(S0). Critically, Q(S0) folds together detection,localization, and
correction in a way that subtask-levelq(c) i does not: orchestrated repair benefits from validation-driven
localization of the failing step, while S0 retries the entire trace whether the original failure was in
CLS or RCH. This asymmetry, not the per-call retry budget, is the substantive difference between S0
and C1 in the model.
5.4 Cost, latency, and qualitative expectations
The logical dependency order D is fixed across C1–C4, but the execution graph induced by the
worker partition is not. Finer decompositions expose parallel fanout — especially for RAT and EXM,
which are parallel-eligible once jurisdiction and classification are available — and add subtask-level
validation points, but also multiply model calls, handoff messages, and orchestration overhead. Wider
decompositions reduce handoff overhead but may serialize work inside a larger call and increase
prompt and context size. Granularity should therefore trace out a non-trivial cost-quality response
rather than collapse to a single dominant point; §7 measures token cost and wall-clock latency directly
and reports them per configuration.
Three expectations follow for interpreting the sweep.
First, accuracy may peak at an intermediate worker count. Very wide workers may benefit from
shared context but suffer from prompt interference and coarse repair. Very narrow workers may
improve local focus and subtask-level repair but introduce handoff errors and fragmented context.
Intermediate decompositions can therefore dominate either extreme when the gains from local focus
and repair exceed the costs of coordination.
11

Second, the cost-quality frontier may exclude some configurations. A configuration that adds calls,
retries, or handoffs without a corresponding accuracy gain should be Pareto-dominated; conversely, a
configuration with slightly lower accuracy may remain relevant if it substantially reduces token cost
or latency.
Third, the S0–C1 contrast estimates thecombinedeffect of adding the orchestrator, ledgers, validation
loop, and subtask-level repair at one-worker scope. It does not isolate “the orchestrator” as a single
mechanism. Comparisons among C1–C4 estimate the effect of changing worker scope under a
fixed orchestrator; the S0–C1 comparison estimates the effect of moving from no-orchestrator to
orchestrated execution at fixed scope.
These expectations define the interpretive vocabulary used in §7 and revisited in §9. They are not
claims about what the results will show.
6 Methodology
This section specifies metrics, the baseline and oracle, the matched-token control for RQ3, the
failure-injection protocol for RQ4, statistical analysis, falsification criteria stated before results,
and reproducibility artifacts. The dataset (40 cases, §3.3), configurations (C1–C4 and S0, §4), and
execution controls (§4.6) are defined earlier and are not repeated here.
6.1 Metrics
Three metric families are measured per (condition, case, repeat): accuracy, cost, and latency.
Accuracy.Final-answer accuracyis the indicator that the emitted V AT determination matches
the oracle label across the structured output fields enumerated in §3.1: jurisdiction, rate treatment,
exemption, reverse-charge status, liable party, and V AT amount or non-charging reason.Step-level
accuracyis the indicator that each subtask record matches its oracle intermediate label, scored per
subtask in T : CLS, JUR, RAT, EXM, and RCH.Trace consistencyis the indicator that all validation
checks in V pass on the emitted trace; rule-citation completeness and citation–decision consistency
are scored as components of trace consistency, following §3.4.Error typeattributes each incorrect
trace to its earliest failing subtask, supporting the error-propagation analysis for RQ1. If multiple
subtasks at the same dependency layer fail, all are recorded for error-type analysis; for single-label
summary plots, we use the fixed order CLS, JUR, RAT, EXM, RCH.
Terminal-failure scoring.A case isterminally failedunder a condition if its trace cannot be brought
to validation pass within the condition’s natural repair budget: subtask-level for C1–C4 and whole-
trace for S0. Terminal failures are scored as final-answer incorrect and trace-inconsistent. Step-level
fields not emitted because of terminal failure are marked missing for step-level reporting and counted
as incorrect in end-to-end trace accuracy. Token cost and latency for terminal failures are reported in
full, including all retries up to the budget.
Cost.Token costis the sum of prompt and completion tokens across all model calls for the case,
including retries. It is the primary cost metric because it captures the retry asymmetry between S0 and
C1–C4 (§4.5).Tool callsandretry countsare reported separately to support interpretation.Dollar
costis computed from a single pinned price sheet to permit comparison; it is treated as derived from
token cost rather than as an independent metric.
Latency.Wall-clock latencyis measured from case submission to final validated trace or terminal
failure. We report median latency per condition with bootstrap confidence intervals. We deliberately
do not report p95/p99 latency: with 40×5 = 200 observations per condition, tail-percentile estimates
are too noisy for reliable inference. Tail behavior is deferred to follow-on work with larger trial
counts.
6.2 Baseline and oracle
One baseline and one oracle anchor the comparisons.S0(§4.5) is the tuned no-orchestrator
ReAct/function-calling single-agent baseline; it is the comparator against which the combined
effect of the orchestrator, ledgers, validation loop, and subtask-level repair is measured.
12

Thedeterministic rule engine(§3.3) is the oracle. It generates ground-truth labels and intermediate
evaluation targets. It is not treated as a competing agentic baseline, does not run under stochastic
repeats, and does not appear in cost or latency comparisons. The oracle labels are used for evaluation
and analysis; they are not exposed to the LLM agents during generation or repair.
6.3 Matched-token comparison (RQ3)
To separate worker-count effects from total-prompt-budget effects, we run a matched-token compari-
son between S0 and orchestrated configurations on the same 40 cases with five stochastic repeats.
The procedure has two parts.
Pre-specified comparison.Before inspecting main-sweep results, we designateC2, the dependency-
layer midpoint, as the orchestrated reference for the matched-token control. We measure mean total
token cost per case for C2 on the main sweep, ¯BC2, then re-tune S0 to a budget cap yielding per-case
token usage within ±10% of ¯BC2 on the held-out development split (§4.5). Additional budget is
allocated across role description, exemplars, and intermediate scratchpad. We denote this variant
S0′ C2 and compare it against C2 under the inferential procedure of §6.5. This is the confirmatory
matched-token comparison.
Post-selection sensitivity.After the main sweep, we identify the orchestrated configuration with
highest mean final-answer accuracy, C ⋆, repeat the matched-token tuning to budget ¯BC⋆, and denote
the resulting variant S0′ C⋆. Because C ⋆ is selected on the accuracy outcome it is then tested on, this
comparison is reported as a post-selection sensitivity analysis, not as a confirmatory test.
For both matched-token variants, token matching is performed only on the development split.
Evaluation-case token usage is reported as observed. If evaluation token usage falls outside the±10%
target band, we report the deviation and do not retune on the evaluation cases.
The matched-token analysis estimates how much of any S0–orchestrated accuracy gap remains once
prompt budget is equalized. It does not isolate every confound. Residual differences, including
orchestrator ledgers, subtask-level repair, and validation-driven failure localization, are discussed in
§9.
6.4 Failure-injection protocol (RQ4)
We inject three failure types into each condition and measure localized fallback. Injections are applied
to a separate copy of the 40-case set so that injected and un-injected results are paired by case identity.
For each case, a singletarget subtask identity τ∈T is sampled deterministically from a fixed seed.
The same τ is used across all conditions and repeats for that case, so injection sites are paired across
conditions.
The injection unit is theworker invocation responsible for τ, not necessarily a single model call to a
single subtask. Under C4, the worker covers exactly τ. Under C2 and C3, the responsible worker
may cover several subtasks including τ, and the entire invocation is affected. Under C1, the single
worker covers all subtasks and is therefore the affected invocation. For S0, the injection unit is the
trace-generation call whose emitted trace would cover the subtask-τ slot. This convention sacrifices
strict per-call comparability in order to respect the worker scope induced by each configuration.
Timeout (isolated).The worker invocation responsible for τ is forced to time out at the fixed timeout
threshold (§4.6). For S0, the whole trace-generation call that would emit the subtask-τ slot is forced
to time out. The orchestrator and S0 then exercise their natural repair mechanisms within their
per-condition retry budgets. In implementation, the forced timeout is raised immediately rather than
by holding the call open to the fixed 120 s threshold: the affected worker’s state is identical to that of
a genuine threshold timeout — the task bundle is delivered and no assistant turn completes — while
avoiding threshold-length idle waits across the arm. None of the reported injection metrics depends
on wall-clock latency, so this substitution leaves them unchanged; wall-clock latency under timeout
injection is consequently not reported.
Hallucinated output (isolated).Under C1–C4, the structured record for subtask τ is replaced,
after worker emission and before validation, with a schema-conforming but oracle-incorrect record
carrying a plausible-but-wrong rule citation. Under S0, the same substitution is applied: after the
emitted trace is produced and before validation, the subtask-τ slot of the trace is overwritten with the
13

same schema-conforming oracle-incorrect record. The injected record is constructed deterministically
from the case so that all repeats receive the same injection.
This condition tests silent semantic-error propagation. When the injected record satisfies V, no
validation-triggered retry fires. Recovery is only possible if downstream subtasks or cross-subtask
consistency checks expose a contradiction. Otherwise, the trace may validate while remaining oracle-
incorrect, especially when τ is the terminal subtask RCH or when the condition lacks a downstream
worker with the responsibility and visible state to expose the contradiction.
Shared-tool outage (correlated).Each scenario family of ten cases is split into two blocks of five,
yielding eight blocks across the 40-case evaluation set. For one deterministically selected case ID
per block, fixed by seed, the rate-table lookup tool returns a transient error on the first invocation
reaching RAT and recovers on subsequent attempts. Thusm= 1 for the shared-tool-outage condition,
with eight affected cases (20% of the evaluation set). Selection of affected cases is independent of
execution scheduling, so the outage is paired across all configurations and repeats.
This condition tests a correlated dependency failure rather than localized worker failure: every
configuration that reaches RAT on an affected case observes the same unavailable external tool on the
first RAT lookup attempt. Recovery therefore depends on retry timing and per-condition fallback
policy rather than sibling-worker substitution.
For each (injection, configuration) cell, we report:
• substitution success rate: the fraction of injected cases reaching a validated trace within the
per-condition repair budget;
• all-case accuracy under injection: final-answer accuracy computed over all injected cases, with
terminal failures and validated-but-wrong traces both counted as incorrect;
• validated-trace accuracy under injection: final-answer accuracy on the subset reaching a validated
trace, reported as a secondary descriptive metric;
•cost penalty: additional tokens relative to the un-injected baseline on the paired case.
All-case accuracy is the primary degradation metric so that terminal failures are not separated from
validated-but-wrong traces in a way that hides total degradation.
For the hallucinated-output condition we additionally report therecord substitution rate: the fraction
of injected cases in which the injected record is subsequently replaced by a repair before the final
trace. This quantity separates exposure of the poisoned record from mere trace validation, since
an injected record that satisfies V can validate without ever being corrected; it is undefined for the
timeout and shared-tool-outage conditions. We also report, for each (injection, configuration) cell,
the paired per-case accuracy delta relative to its un-injected main-sweep baseline, with case-clustered
bootstrap confidence intervals computed as in §6.5. The record substitution rate and the paired deltas
are descriptive quantities outside the pre-specified headline family of §6.5.
6.5 Statistical analysis
Because the same 40 cases appear across all conditions with five stochastic repeats each, headline
comparisons are paired by case and clustered within case.
Primary procedure.We first aggregate the five repeats per (condition, case) to case-level summaries:
mean for accuracy, mean for token cost, and median for latency. For paired comparisons between
conditions, we use acase-clustered paired bootstrapwith 1,000 resamples drawn at the case level.
Each resample computes the paired difference in the statistic of interest: mean accuracy, mean token
cost, or median latency across case-level summaries. Reported intervals are 95% percentile bootstrap
CIs on the paired difference.
For named pairwise hypotheses, we additionally reportpaired permutation testsover case-level
summaries, using 1,000 permutations of within-case condition labels, withHolm–Bonferroni
correction across the family of headline tests.
Effect sizes.We reportCohen’s dz for headline paired comparisons. The sign of dz follows the
direction of the named contrast. For superiority claims, the small-effect threshold is directional:
a configuration is treated as materially better only when the paired bootstrap CI for the accuracy
difference excludes zero in the positive direction andd z ≥0.2.
14

Descriptive supplement.Mann–Whitney U is computed as a robustness check; values ship with the
released analysis tables. It is not used for confirmatory inference.
Pre-specified family of headline tests.The pre-specified family, fixed before results inspection, is:
1. S0 vs. C1: orchestrated-control contrast at one-worker scope;
2. C1 vs. C4: granularity endpoints under fixed orchestrator;
3. C2 vs. C1: dependency-layer midpoint vs. wide endpoint under fixed orchestrator;
4. S0 ′ C2 vs. C2: confirmatory matched-token comparison for RQ3.
Holm–Bonferroni correction is applied across these four tests. All other comparisons, including best-
among-C1–C4 versus worst-among-C1–C4 cost-quality contrasts and the post-selection sensitivity
S0′ C⋆ vs.C ⋆, are reported descriptively outside the corrected family.
We note explicitly that 40 cases with five repeats each is a pilot-scale sample. We do not run an a
priori power analysis; we report paired CIs and effect sizes and let readers judge inferential weight.
Wide CIs are reported as wide, not interpreted as null findings. Non-significant results in the headline
family should be read as inconclusive rather than as evidence of no effect.
6.6 Falsification criteria
We pre-state three criteria, fixed before results inspection. For accuracy comparisons,materially
outperformsmeans that the paired bootstrap CI for the accuracy difference excludes zero in the
positive direction and the paired effect size satisfiesd z ≥0.2.
1. Intermediate-optimum granularity (RQ1).If neither intermediate configuration, C2 nor C3,
materially outperforms both endpoints, C1 and C4, on final-answer accuracy, the intermediate-
optimum version of the non-monotonic-granularity hypothesis is unsupported for this workload.
If the C1–C4 accuracy sequence is monotonic in either direction, this criterion is automatically
unmet.
2. Orchestration benefit (RQ2).If S0 weakly Pareto-dominates all of C1–C4 on the token-cost/final-
answer-accuracy plane under main-sweep conditions, the orchestrated multi-worker hypothesis is
unsupported for this workload.
3. Prompt-budget confound (RQ3).If the S0′ C2 vs. C2 accuracy difference is not significant under
the paired permutation test with Holm–Bonferroni correction and its paired bootstrap CI includes
zero, we report that any C2 main-sweep advantage is consistent with a prompt-budget explanation
rather than an agent-count explanation. All three criteria, the harness, and the analysis plan were
committed under version control before any results were inspected; the released artifact’s commit
history provides timestamped evidence.
These criteria are not the only signals in the results, but they discipline how headline claims are
reported in §7.
6.7 Reproducibility
The released artifact contains: the orchestrator implementation; prompt sets for C1–C4, S0, S0′ C2,
and S0′ C⋆; the deterministic rule oracle; the 40 evaluation cases and 8 development cases with oracle
labels; the failure-injection seeds, target-subtask assignments, affected-case lists, and shared-tool-
outage setting m= 1 ; pinned model identifiers and decoding settings; per-(condition, case, repeat)
raw traces; and the analysis scripts that produce all reported tables and figures from the raw traces.
The harness follows an AutoGenBench-style controlled-isolation pattern: each (condition, case,
repeat) executes in a clean process with no shared mutable state. The supplementary package is
prepared in two forms: an anonymized version for double-blind venues and an attributed version for
non-anonymous venues, with author-identifying metadata restored after review or at submission to a
non-anonymous venue.
15

Table 1: Main sweep: final-answer accuracy, token cost, and median latency per condition, with 95%
case-clustered bootstrap CIs (§6.5). Latency is the median of case-level medians.
Condition Accuracy [95% CI] Tokens [95% CI] Med. latency, s [95% CI] Trace cons. Term. fail.
S0 0.755 [0.665, 0.840] 11,899 [11,217, 12,628] 11.8 [11.0, 12.7] 1.000 0/200
C1 0.720 [0.625, 0.810] 11,317 [10,599, 12,000] 12.1 [11.3, 12.6] 1.000 0/200
C2 0.830 [0.750, 0.910] 14,590 [12,971, 16,416] 15.8 [15.2, 16.3] 0.985 3/200
C3 0.830 [0.745, 0.915] 13,591 [12,507, 14,928] 16.7 [16.2, 17.4] 0.985 3/200
C4 0.770 [0.685, 0.855] 15,845 [15,457, 16,238] 18.4 [17.8, 19.7] 1.000 0/200
S0 C1
k = 1
C2
k = 2
C3
k = 3
C4
k = 5
0.60
0.65
0.70
0.75
0.80
0.85
0.90
0.95final-answer accuracy
0.755
0.720
0.830 0.830
0.770
orchestrated C1–C4
S0 (no orchestrator)
Figure 2: Main-sweep final-answer accuracy by condition with 95% case-clustered bootstrap CIs
(Table 1). The orchestrated sequence C1–C4 is non-monotonic; S0 is plotted separately because it is
not a point on the granularity curve (§4.5).n= 40cases×five repeats (200 runs per condition).
7 Results
We report 4,400 valid runs: the main sweep (five conditions × 40 cases × 5 repeats = 1,000), two
matched-token arms (2 × 200), and three failure-injection arms (3,000; reported in §8). All numbers
are produced by the released analysis pipeline from the released raw traces (§6.7); headline inference
follows §6.5, and the pre-stated falsification criteria of §6.6 discipline every verdict. Three harness
defects were discovered and repaired during execution; the affected arms were re-run under the
corrected harness, superseded attempts are archived in the released artifact and are not reported as
results, and the defects are disclosed in §10.2.
7.1 Main sweep (RQ1, RQ2)
Table 1 reports the main sweep. All intervals are 95% case-clustered bootstrap CIs (§6.5); latency is
the median of case-level medians.
The accuracy sequence over C1–C4 is non-monotonic: 0.720, 0.830, 0.830, 0.770 (Figure 2). The
two intermediate configurations tie at the top, consistent with their sharing the identical downstream
{RAT, EXM, RCH} worker (§4.3); separating JUR from CLS — the only difference between C2
and C3 — leaves accuracy unchanged. Median latency rises monotonically with worker count, from
≈12 s (S0, C1) to 18.4 s (C4), reflecting sequential dispatch along the dependency order. C1 is the
cheapest condition in tokens and C4 the most expensive; dollar cost is derived from the pinned price
sheet and tracks tokens (§6.1). Terminal failures occur only in the intermediate configurations (three
runs each, 1.5%, all validation-budget exhaustion).
Table 2 reports the pre-specified headline family (§6.5) with Holm–Bonferroni correction; no test in
the family survives correction.
RQ1 (falsification criterion §6.6(1): triggered).Both intermediates materially outperform the wide
endpoint under the pre-stated bar — C2 vs. C1: +0.110, CI [+0.010, +0.210], dz = 0.34; C3 vs. C1:
+0.110, CI [+0.005, +0.215], dz = 0.31 (descriptive, outside the corrected family) — but neither
16

Table 2: Pre-specified headline family (§6.5) with Holm–Bonferroni correction. No test in the family
survives correction.
Contrast∆accuracy [95% CI]d z Perm.pHolmpReject
S0 vs. C1+0.035[−0.035,+0.110] 0.14 0.436 0.843 no
C1 vs. C4−0.050[−0.160,+0.050]−0.150.422 0.843 no
C2 vs. C1+0.110[+0.010,+0.210] 0.34 0.043 0.172 no
S0′ C2 vs. C2−0.065[−0.165,+0.025]−0.200.265 0.794 no
11000 12000 13000 14000 15000 16000 17000
mean total tokens per case
0.60
0.65
0.70
0.75
0.80
0.85
0.90
0.95final-answer accuracy
S0C1
C2C3
C4
S0'C2
S0'C ⋆
non-dominated set {C1, S0, C3}
Figure 3: Cost–quality plane: mean total tokens per case vs. final-answer accuracy, with 95% CIs on
both axes (Table 1). The dashed staircase traces the non-dominated set {C1, S0, C3}; open diamonds
are the matched-token arms S0′ C2 and S0′ C⋆ (Table 4). Each point aggregates n= 40 cases × five
repeats (200 runs per condition).
materially outperforms the fine endpoint: C2 vs. C4 is +0.060 with CI [ −0.005, +0.125] and C3
vs. C4 is +0.060 with CI [ −0.020, +0.135], both including zero, the former missing the bar by its
lower bound. Per §6.6(1), the intermediate-optimum hypothesis is thereforeunsupported for this
workload. We note the descriptive shape — intermediates highest, endpoints lower — is suggestive
of the hypothesized non-monotonicity, and the C2/C4 interval only narrowly includes zero; at pilot
scale this is an inconclusive reading, not evidence of absence (§6.5).
RQ2 (falsification criterion §6.6(2): not triggered).S0 does not weakly Pareto-dominate C1–C4
on the (token-cost, accuracy) plane: C2 and C3 are more accurate at higher cost, and C1 is cheaper
at lower accuracy. Descriptively, the non-dominated set is {C1, S0, C3 } (Figure 3): C3 weakly
dominates C2 (equal accuracy, fewer tokens) and dominates C4 (higher accuracy, fewer tokens).
The orchestrated multi-worker hypothesis survives its falsification test, at a measured price: the
accuracy gain along the non-dominated set (S0 → C3, +0.075) costs +14% tokens and +42% median
latency.
7.2 Error localization
Table 3 attributes each incorrect trace to its earliest failing subtask (§6.1), over the 219 incorrect
main-sweep runs.
CLS and EXM never appear as earliest failures in any condition. The wide-scope conditions fail
earliest at jurisdiction determination (JUR: 30 of 49 for S0, 23 of 56 for C1); giving JUR a dedicated
or co-resident-with-CLS worker eliminates JUR-earliest failures entirely under C2 (0) and nearly so
under C3 and C4 (7 and 6). Fragmentation relocates rather than removes error: under C4, failures
concentrate at the terminal synthesis step (RCH: 39 of 46), where the narrowest worker must reconcile
17

Table 3: Error localization: earliest failing subtask per incorrect main-sweep run (§6.1), over the 219
incorrect runs.
Condition CLS JUR RAT EXM RCH Total
S0 0 30 0 0 19 49
C1 0 23 0 0 33 56
C2 0 0 15 0 19 34
C3 0 7 10 0 17 34
C4 0 6 1 0 39 46
Table 4: Matched-token arms (§6.3). Tuning used only the development split; evaluation-set usage is
reported as observed.
Arm Accuracy [95% CI] Tokens (eval) Target Deviation In±10%band
S0 0.755 [0.665, 0.840] 11,899 — — —
S0′ C2 0.765 [0.655, 0.865] 13,230 14,590−9.3%yes
S0′ C⋆ 0.760 [0.650, 0.860] 12,864 13,591−5.3%yes
all upstream records. This relocation pattern — early-stage failures in wide scopes, synthesis failures
in narrow scopes, with the intermediates minimizing totals (34 each) — is the error-propagation
texture behind the non-monotonic accuracy sequence, and we return to it in §9.
7.3 Matched-token comparison (RQ3)
Table 4 reports the S0 family. Tuning used only the development split (§6.3); evaluation-set usage is
reported as observed.
Three protocol disclosures. First, C ⋆ resolved toC3: C2 and C3 tied exactly on mean accuracy
(0.830), and the tie was broken by lowest mean token cost (13,591 < 14,590), a Pareto-consistent
rule fixed only after the tie was observed and disclosed as such. Second, the tuning ladder is discrete,
and both budget targets resolved to the same rung (extended role description, scratchpad instruction,
three development-case exemplars); the two matched-token arms therefore ran an identical tuned
prompt, and the post-selection arm functions as anindependent replicationof the confirmatory arm
rather than a distinct budget point — a replication it passes (0.765 vs. 0.760 on disjoint runs). Third,
evaluation-set usage landed below both targets ( −9.3%, −5.3%) but within the pre-stated ±10%
band.
RQ3 (falsification criterion §6.6(3): triggered).The confirmatory contrast S0′ C2 vs. C2 is −0.065
with CI [ −0.165, +0.025], dz =−0.20 , permutation p= 0.265 , Holm-adjusted p= 0.794 : not
significant, with an interval including zero. Per the pre-registered rule, we therefore report that
any C2 main-sweep advantage is consistent with a prompt-budget explanation rather than an
agent-count explanation. Per §6.5, this is an inconclusive finding, not a null: the point estimate
favors C2 — the budget-matched single agent remains 6.5 points below it, at the small-effect threshold
in magnitude — and the added budget bought S0 essentially nothing (+0.010 and +0.005 accuracy
for +11% and +8% tokens over plain S0). The data lean toward an agent-count effect, but at n= 40
the pilot cannot exclude the budget explanation, and the pre-registered criterion requires saying so.
Failure-injection results (RQ4) are reported in §8.
8 Localized Fallback under Injected Failures (RQ4)
The three injection arms comprise 3,000 runs: for each mode — forced worker timeout, hallucinated
output, and shared-tool outage (§6.4) — every condition runs the full 40-case set with five repeats,
paired by case identity and target subtask τ with the un-injected main sweep. Exactly one mode
applies per run. The timeout arm reported here executed under the corrected forced-timeout dispatch;
the original arm carried a harness defect, is archived with the artifact, and is not reported (§10.2).
RQ4 carries no falsification criterion: all quantities in this section are descriptive under the §6.4
reporting specification, with paired per-case accuracy deltas and case-clustered 95% bootstrap CIs
(§6.5).
18

Table 5: Localized fallback under injection (§6.4), per (injection, configuration) cell. ∆ accuracy is
the paired delta against the condition’s own un-injected baseline (Table 1), with case-clustered 95%
bootstrap CIs.
Injection Cond. Subst. success All-case acc. Val.-trace acc.∆acc. [95% CI] Token penalty
Timeout
S0 1.000 0.735 0.735−0.020[−0.110,+0.065]−1,442
C1 1.000 0.880 0.880+0.160[+0.065,+0.265]+21,793
C2 0.965 0.810 0.839−0.020[−0.090,+0.045]+4,611
C3 0.965 0.835 0.865+0.005[−0.030,+0.045]+4,433
C4 0.995 0.775 0.779+0.005[−0.055,+0.065]−87
Outage
S0 1.000 0.780 0.780+0.025[−0.060,+0.110]+1,138
C1 1.000 0.705 0.705−0.015[−0.095,+0.065]+660
C2 1.000 0.840 0.853+0.010[−0.040,+0.055]+363
C3 0.975 0.840 0.862+0.010[−0.060,+0.065]+622
C4 1.000 0.810 0.814+0.040[−0.025,+0.105]+623
Hallucination
S0 1.000 0.560 0.560−0.195[−0.335,−0.060]+3,290
C1 0.885 0.405 0.458−0.315[−0.470,−0.140]+5,735
C2 0.900 0.345 0.383−0.485[−0.640,−0.325]+2,152
C3 0.890 0.345 0.388−0.485[−0.625,−0.335]+3,111
C4 0.925 0.310 0.335−0.460[−0.610,−0.305]+2,009
−0.5 0.0
S0
C1
C2
C3
C4
+0.160
Timeout
−0.5 0.0
paired Δ accuracy vs. un-injected baseline (95% CI)
Shared-tool outage
−0.5 0.0
Hallucinated output
Figure 4: Paired per-case accuracy deltas under injection, by condition, with case-clustered 95%
bootstrap CIs (Table 5). Availability perturbations (left, center) straddle zero in every cell except the
C1 timeout overshoot (+0.160); the content perturbation (right) is negative in every condition. Each
cell aggregatesn= 40cases×five repeats (200 runs per (injection, condition) cell).
Table 5 reports the §6.4 metrics per (injection, configuration) cell.Substitution success— the fraction
of injected cases reaching a validated trace within the repair budget — is computed among fired
injections: all 40 cases for timeout and hallucination, the eight affected cases (20%) for outage. ∆
accuracy is the paired delta against the condition’s own un-injected baseline (Table 1). Figure 4 plots
the paired deltas.
8.1 Availability perturbations are absorbed
Under shared-tool outage, every configuration recovers. Among the eight affected cases, 39 or 40
of the 40 injected runs per condition reach a validated trace (substitution success 0.975–1.000), all
five paired deltas straddle zero, and token penalties are small (+363 to +1,138). S0 pays the largest
penalty, consistent with whole-trace re-emission being the bluntest available retry instrument for a
single transient tool call.
Forced timeout is likewise absorbed in four of five conditions. Substitution success is 0.965–1.000;
the paired deltas for S0, C2, C3, and C4 all straddle zero. The token signature tracks the scope of the
affected worker: the half-pipeline workers of C2 and C3 pay +4,433 to +4,611 tokens to regenerate
19

their scope, the single-subtask worker of C4 pays essentially nothing (−87), and S0 lands slightly
negative (−1,442 ) — the forced initial dispatch bills no tokens, and the single repair regeneration
replaces, rather than adds to, the baseline generation. A prediction recorded in the project log before
the corrected arm was executed anticipated absorption in all five cells; four cells confirmed it, and the
fifth exceeded it.
8.2 The C1 timeout overshoot
C1 under forced timeout reaches 0.880 — the highest accuracy of any cell in the program, 0.160 above
its own un-injected baseline, and the only availability cell whose interval excludes zero (CI [+0.065,
+0.265]). The cost signature identifies what happened: +21,793 tokens — a total of ≈2.9× the
un-injected C1 cost — i.e., the repair budget was consumed as roughly two additional full-pipeline
attempts. After a forced restart, repair at full scope behaves as validation-filtered redraw of the
entire pipeline, and the redraw more than recovers the discarded attempt. The effect scales with
worker scope exactly as that account requires: full pipeline (C1, +0.160) ≫ half pipeline (C2/C3,
≈0) ≈ single subtask (C4, ≈0), and S0 — whose normal repair unit is already the whole trace —
gains nothing (−0.020). Why validation-filtered redraw at wide scope outperforms the baseline’s
single-draft path, and does so only there, is taken up in §9. We flag the finding’s status explicitly:
descriptive, at pilot scale, outside the corrected family.
8.3 The content perturbation degrades every configuration and inverts the ordering
Hallucinated output is the only mode in which every paired delta excludes zero, and all five are
negative: S0 −0.195 [−0.335,−0.060 ] is the mildest; C1 −0.315; C4 −0.460; C2 and C3, the
main-sweep leaders, the worst at −0.485. The main-sweep ordering inverts: S0 (0.560) is now the
most accurate condition, C1 (0.405) second, and the fragmented configurations fall to 0.310–0.345.
Validation offers no content defense — by construction (§6.4), and the data confirm it emphatically.
Injected runs almost always still reach a validated trace: substitution success is 0.885–0.925 for the
orchestrated conditions and 1.000 for S0, and most of those validated traces are wrong (validated-
trace accuracy 0.335–0.458 orchestrated). A schema-conforming, oracle-incorrect record passes V
essentially unimpeded; as §6.4 anticipated, recovery requires a downstream contradiction to surface,
and where none does, the poison validates and ships.
The record substitution rate (§6.4) exposes the sharpest tension in the program. The orchestrated
conditions replace the injected record in 77.5–78.0% of cases, S0 in only 58.0% — yet the orchestrated
conditions end at 0.310–0.405 accuracy while S0 retains 0.560. Replacing the record is not correcting
the determination: the replacement can be wrong again, and downstream workers that consumed
the poisoned record before its replacement have already propagated its content across the hand-off.
The record-based interfaces that give fragmented configurations their clean seams are, under content
perturbation, equally clean propagation channels — downstream workers treat validated upstream
records as ground truth precisely because label isolation and schema validation license them to. Token
penalties are moderate (+2,009 to +5,735), largest for C1, consistent with wide-scope redraws when
contradictions do surface. We return to the propagation mechanism in §9.
8.4 Summary
The three arms separate cleanly into a two-class taxonomy.Availabilityperturbations — forced
timeout and transient shared-tool outage — are absorbed by natural repair at every granularity tested,
and at the widest orchestrated scope the restart is over-compensated into the program’s best cell.
Thecontentperturbation — a single schema-conforming hallucinated record — degrades every
configuration, degrades the fragmented ones most, and inverts the main-sweep ordering. Localized
fallback, as measured here, defends availability, not content.
9 Discussion
Reading the curve through the chain-error model.The sweep realizes the first expectation of
§5.4 in shape — accuracy peaks at the intermediate configurations — while failing the pre-registered
material bar against the fine endpoint (§7.1), so this pilot reads the non-monotonicity as directional
20

rather than established. The error-relocation table (§7.2) supplies the marginal-term evidence §5.1
asked for: wide scopes concentrate earliest failures at jurisdiction determination (interference in
pJUR under broad visible state), the finest scope concentrates them at reverse-charge synthesis
(fragmentation in pRCH when the terminal worker must reconcile records it did not produce), and
the intermediates minimize the total by placing their single boundary between the two error masses.
Both signs that §5.2 declined to fix materialized at once: wider was worse early, narrower was worse
late. Consistent with boundary placement rather than worker count being the operative variable, C2
and C3 — which share the downstream synthesis worker byte-for-byte and differ only in whether
CLS and JUR are co-resident — land on identical accuracy; the tie doubles as an internal-consistency
check that the harness passes.
Repair as resampling.The timeout overshoot (§8.2) gives the repair term q(c) i of §5.3 an unantici-
pated reading. A forced restart at full scope converts repair into validation-filtered redraw of the entire
chain, and roughly two extra filtered drafts lifted C1 to 0.160 above its own baseline — effective ˜p
exceeding single-draft p not through targeted correction but through selection over resamples. The
effect requires wide scope (redraw at half- or single-subtask scope bought nothing) and is invisible to
S0, whose whole-trace retry is already its normal mechanism (Q(S0)). Validation-filtered resampling
therefore looks like a reliability lever on the same axis the sweep varies — at a measured ≈2.9×
token cost — and one separable from decomposition in a follow-up arm.
Seams defend availability and propagate content.§5.3 scoped q to validation-visible failures;
the injection arms measure the complement directly. Availability faults were absorbed at every
granularity (§8.1), while the single schema-conforming content fault degraded every configuration
and hit the fragmented ones hardest (−0.460 to −0.485, against C1’s −0.315). The mechanism is the
hand-off itself: downstream workers treat validated upstream records as ground truth, so the record
contract that gives orchestration its clean coordination is, under content perturbation, an equally clean
propagation channel. Two cautions attach. Record replacement is not correction — the orchestrated
conditions replaced the poisoned record in ≈78% of cases yet finished at 0.310–0.405 — and the
S0 row of that arm partly reflects the injection convention of §6.4, under which S0’s remaining
fields predate the poison while orchestrated hand-offs consume it in-band; we therefore weight the
within-orchestrated gradient, which the convention does not touch.
What matched tokens did and did not buy.The RQ3 verdict stands as pre-registered (§7.3). What
the arm adds mechanistically is that prompt budget was not S0’s binding constraint: +8–11% tokens
of tuned role text, exemplars, and scratchpad moved accuracy by +0.005 to +0.010, while S0’s modal
earliest failure remained jurisdiction determination — precisely the subtask the successful partitions
isolate. The data lean toward an agent-count reading; atn= 40, the criterion rightly withholds it.
A candidate heuristic, scoped to this workload.For V AT determination on this rule set, model, and
harness — as measured, not as deployment guidance — the pilot supports: place one boundary at the
dependency-layer midpoint, separating preparation (CLS, JUR) from synthesis (RAT, EXM, RCH);
prefer C3 over C2 on cost alone (equal accuracy, ≈7% fewer tokens); do not fragment further, since
the finest scope pays the synthesis penalty without an accuracy return; where transient availability
faults dominate, wide scope with restart-on-stall was the strongest cell we measured; and at no
granularity should schema validation be expected to stop content faults. Each clause is a hypothesis
for the full study, not a rule. The pilot’s sizing contribution is concrete: the effects worth confirming
ran at dz ≈0.3 , so a paired design with 0.8 power at α=.05 requires on the order of 90 cases —
roughly twice this pilot — before any clause graduates from heuristic to finding.
10 Threats to Validity
We organize threats by what each one limits: external validity, construct validity, statistical validity,
and internal validity. The study is a bounded pilot: it is designed to isolate agent-scope granularity on
one V AT-style activity surface, not to establish a general design rule for enterprise agents.
10.1 External validity
Single workload.The evaluation uses one bounded V AT activity surface (§3). Findings should be
read as a candidate heuristic for V AT-style determination workflows with oracle-labeled intermediate
steps and a fixed rule set, not as a general claim about enterprise agents, tax automation, or legal
21

compliance. The harness does not cover the full V AT rule space of any jurisdiction, special-sector
schemes, real invoice parsing, supplier master-data defects, production posting, or statutory reporting
(§3.5). Cross-workload replication — for example, single-jurisdiction sales tax, HS-code or tariff
classification, claims adjudication, and KYC-style determinations — is deferred to follow-on work.
Synthetic cases and generator–oracle coupling.The 40 evaluation cases are generated under the
bounded rule set rather than sampled from production invoices (§3.3). They exercise the specified
activity surface but underrepresent real-world distribution shifts such as malformed inputs, ambiguous
product descriptions, master-data errors, stale registration data, adversarial vendor behavior, and
jurisdiction-specific edge cases. They also share an origin with the oracle: the same deterministic
rule engine generates both cases and labels. This shared origin is necessary to obtain unambiguous
step-level ground truth, but it can inflate measured accuracy if model outputs happen to align with
rule-engine surface patterns rather than with the underlying V AT logic. Manual spot-checking (§3.3)
verifies oracle conformance within the harness; it does not establish production realism.
Model homogeneity.The main sweep uses one pinned base model family across C1–C4 and S0
(§4.6). Heterogeneous-model variants are not run in this pilot. Conclusions about the granularity–
performance relationship may shift under deployments where a stronger orchestrator model delegates
to smaller or cheaper workers, or where different workers use different model families. We therefore
report the result only for the homogeneous-model pilot and treat heterogeneous-model sweeps as
outside the present scope.
Model-version drift.Model identifiers and decoding settings are pinned and released (§6.7), which
supports replication on the same versions but does not establish stability across providers, model
generations, or capability tiers. The reported results should be interpreted as controlled comparisons
among configurations under one pinned model family, not as absolute capability claims.
Operating point of the model choice.The pinned base model is a lower-cost tier, and that choice
fixes a capability–difficulty operating point for the sweep rather than threatening internal validity:
every condition faces the same model, and main-sweep accuracies (0.720–0.830) sit away from
both floor and ceiling, so configuration differences remain observable. At other operating points the
granularity curve could compress or reorder — a stronger model may saturate the task toward ceiling
and shrink the differences, while a weaker one may push conditions toward floor, where retry and
fallback dominate behavior. The reported granularity effect is therefore an estimate at this operating
point, and the difficulty band itself is among what a replication on another model tier would vary.
10.2 Construct validity
Merge-policy dependence.The C1–C4 partition follows one pre-specified dependency-layer merge
policy (§4.4). Alternative policies, including tool-locality clustering and semantic-similarity cluster-
ing, were considered but excluded from the primary sweep to avoid introducing a second experimental
variable. The observed granularity pattern may therefore depend partly on the merge policy. Robust-
ness across merge policies is deferred and reported as a limitation rather than implied by silence.
Agent differentiation.Section 4 defines agents as distinct by role, tool permissions, visible state,
schema scope, and interaction protocol, not by prompt wording alone. This addresses the strongest
version of the homogeneity critique [Xu et al., 2026], but it does not prove that workers exhibit deep
functional specialization. Under a single base model family, workers in C2–C4 may behave similarly
despite different permissions and state slices. The pilot therefore measures the effect of architectural
scope differences enforced by the harness, not specialization that would emerge from differentiated
training, fine-tuning, or per-role model selection.
Matched-token residual confounding.The matched-token comparison (§6.3) addresses the concern
that multi-agent gains may reflect larger prompt budgets rather than agent count. It does not eliminate
all structural differences. Even at matched token budgets, S0 and the orchestrated configurations
differ in context segmentation, ledger state, validation localization, retry unit, and handoff structure.
The matched-token result is therefore a sensitivity analysis for prompt-budget effects, not a complete
causal decomposition of agent count, orchestration, and context structure.
Matched-token band resolution.The ±10% band check (§6.3) is enforced on the development split
with one repeat over eight cases, and measurement at that scale is coarse: the configuration ultimately
selected measured roughly 15% apart across the two independent tuning runs. Both budget targets
22

consequently resolved to the same discrete tuning rung, so the two matched-token arms share one
tuned prompt and the post-selection arm functions as an independent replication rather than a distinct
budget point (§7.3). Evaluation-set usage is reported as observed and landed within the band for both
arms (−9.3% and−5.3%).
S0 tuning.S0 is tuned on an eight-case held-out development split (§4.5), with the final prompt and
tuning budget disclosed. A larger development set, different prompt-search method, or different whole-
trace repair strategy could change S0 performance. We treat S0 as a strong, disclosed comparator
rather than an exhaustively optimized single-agent upper bound. The development split also contains
no exempt-outcome line, so S0’s prompt is tuned without exposure to the exempt output shape that
accounts for roughly 20% of evaluation-set line determinations; the schema and output contract still
specify that shape, but tuning-time coverage is absent.
Failure-injection realism.The fallback protocol (§6.4) covers two isolated synthetic failures, timeout
and hallucinated output, plus one correlated shared-tool outage with m= 1 . Real deployments
may experience more complex failures: provider-wide rate limiting, partial tool degradation, stale
rate tables, refusal-policy interactions, cross-case context contamination, and upstream classification
drift. The reported substitution-success and degradation metrics should therefore be read as localized-
fallback measurements under controlled injections, not as a general fallback characterization across
correlated failure modes. In addition, the injection unit follows each architecture’s own structure
(§6.4): for S0 the subtask-τ slot is overwritten after the full trace is emitted, while orchestrated hand-
offs consume the injected record in-band. The S0-versus-orchestrated contrast under hallucinated
output therefore partly reflects this timing convention; contrasts among C1–C4, which share the
convention, do not.
Oracle scope.The deterministic rule engine defines correctness only within the bounded V AT rule set
(§3.3). Oracle labels are not exposed to agents during generation or repair (§6.2). The oracle can score
emitted decisions against labels, but it cannot prove that a label-correct trace was reached through
legally valid reasoning. A trace may match the oracle while containing superficial or coincidental
reasoning. Step-level labels, rule-citation checks, and trace-consistency checks (§3.4) reduce this
risk but do not eliminate it. In addition, the rule set’s exemption-over-reverse-charge precedence is
never exercised by any evaluation or development case — no exempt-category line occurs within
an intra-community B2B transaction — so the sweep cannot observe configuration behavior at that
edge; a constructed probe confirms the oracle itself resolves it correctly.
Harness defects discovered and repaired during execution.Three defects in the experiment harness
were discovered during the measured program — each caught by the design’s own instruments before
analysis of the affected arm — and each was repaired, with the arm re-run under the corrected harness.
First, the activity-surface specification omitted the line-item operand from the reverse-charge worker’s
input state; the operand reached that worker only through a voluntary upstream echo that varied
across partitions, deterministically failing amount-bearing cases under C2. The specification was
amended under a closed-operand principle — every field required by a subtask’s contractual output
belongs to that subtask’s visible state (§4.3) — and the main sweep was re-run in full. Second, the
forced-timeout injection initially skipped the worker dispatch entirely, so repair attempts ran against
an empty conversation and the arm was uniformly fatal: it simulated “task never delivered” rather
than the specified “task delivered, call lost” (§6.4). The dispatch was corrected and the timeout arm
re-run. Third, the matched-token arms initially executed with an untuned prompt identical to S0:
the tuning step had been skipped and the harness fell back silently to the plain baseline. Both arms
were re-run after tuning on the development split, and the silent fallback was replaced by a hard
failure. All superseded attempts are archived in the released artifact alongside the repair history; only
corrected-arm results are reported. The defects sit on the harness side of the construct: the oracle,
dataset, and frozen hashes were unaffected throughout.
10.3 Statistical validity
Pilot sample size.Forty cases with five stochastic repeats per condition is a pilot-scale sample (§6.5).
We report paired bootstrap confidence intervals and effect sizes, including when intervals are wide.
Non-significant comparisons in the headline family are interpreted as inconclusive rather than as
evidence of no effect. We deliberately do not report p95 or p99 latency at this sample size; tail
behavior requires a larger trial count. Per-scenario-family comparisons, drawing on ten cases each,
are reported descriptively only.
23

Multiplicity outside the headline family.Holm–Bonferroni correction is applied only to the four
pre-specified headline tests (§6.5). Other comparisons, including post-selection sensitivity results,
per-subtask error breakdowns, and best-versus-worst cost-quality contrasts, are descriptive. They
should be interpreted as exploratory patterns rather than confirmatory hypothesis tests.
Post-selection sensitivity.The S0′ C⋆ comparison is selected after observing which orchestrated
configuration has the highest mean final-answer accuracy (§6.3). It is reported as a post-selection
sensitivity analysis, not as a confirmatory test. The confirmatory matched-token comparison is S0′ C2
versus C2.
Case-level aggregation.Repeats are aggregated to case-level summaries before paired inference
(§6.5). This preserves the paired, case-clustered design and avoids treating stochastic repeats as
independent cases. It also compresses repeat-level variance into a single case-level statistic. The raw
repeat-level traces are released so that alternative analyses can be reproduced.
10.4 Internal validity
Concurrency and provider effects.The concurrency cap (§4.6) prevents parallel-eligible workers
from contending for provider-side rate-limit capacity. This avoids attributing provider queuing delays
to agent granularity, but it also means the reported latencies do not characterize throughput-saturated
deployments. Production settings with higher contention or provider-side throttling may shift the
latency and cost frontier.
Single orchestrator implementation.All orchestrated conditions share one Magentic-One-style
orchestrator (§4.2). The S0–C1 contrast estimates the combined effect of adding the orchestrator,
ledgers, validation loop, and subtask-level repair at one-worker scope. It does not isolate which
component contributes which share of the effect. A different orchestrator design could change both
the S0–C1 contrast and the C1–C4 trajectory.
Repair-unit asymmetry.C1–C4 repair at subtask granularity, while S0 repairs at whole-trace
granularity (§4.5). This asymmetry is intentional because it reflects the natural repair unit exposed
by each architecture. It also means that retry-induced call count is not equal across conditions. We
therefore report token usage, retry counts, and cost penalties explicitly rather than treating retries as
hidden infrastructure.
Validation visibility.The validation checks in V detect schema errors, missing fields, missing
citations, and some citation–decision inconsistencies. They do not detect all semantically wrong
but schema-conforming outputs. This matters most in the hallucinated-output injection, where the
injected record is intentionally validation-conforming (§6.4). Such cases test silent semantic-error
propagation rather than ordinary validation failure.
Harness and prompt dependence.Implementation choices may affect measured behavior: prompt
wording, tool-call wrappers, timeout handling, retry ordering, and ledger serialization can all influ-
ence results. We release the harness, prompts, rule engine, and configuration files (§6.7) so that
these choices are inspectable, but releasing them does not neutralize their influence on the specific
numbers reported here. Replication on the released artifact establishes that the pattern holds for this
implementation; it does not establish that the pattern is implementation-independent.
The study therefore establishes a controlled pilot methodology and a bounded heuristic for V AT-style
determination workflows. It does not establish a general design rule for LLM-agent decomposition,
enterprise tax automation, or fault-tolerant agent systems.
11 Conclusion
We presented a pilot controlled sweep of agent-scope granularity on a fixed activity surface for
synthetic EU-style V AT determination: a tuned no-orchestrator baseline and four orchestrated
partitions of the same five subtasks, 40 oracle-labeled cases with five stochastic repeats, matched-
token controls, and three failure-injection arms — 4,400 valid runs evaluated against pre-registered
falsification criteria. The intermediate configurations led on accuracy (0.830 for both) but did not
meet the pre-stated material bar against the fine endpoint, so the intermediate-optimum hypothesis
remains unsupported for this workload — a directional reading at pilot scale, not evidence of absence;
the single agent did not Pareto-dominate the orchestrated set; and the matched-token criterion fired,
24

so any C2 main-sweep advantage is reported as consistent with a prompt-budget explanation, even
though the point estimate favors C2. Under injection, availability faults were absorbed at every
granularity — with wide-scope restart over-recovering its own baseline by +0.160 — while a single
schema-conforming content fault degraded every configuration and inverted the main-sweep ordering.
Together these results support one bounded heuristic — a single partition boundary at the dependency-
layer midpoint of a V AT-style workflow — and one concrete sizing target for the full study, on the
order of 90 cases; the oracle, dataset, harness, raw traces, and analysis pipeline are released to make
both directly testable.
Artifact availability.The artifact — oracle, dataset, harness, prompts, injection seeds, raw
traces, and analysis pipeline (§6.7) — is available at https://github.com/pedro-santos-eng/
Right-sizing-LLM-agent-decomposition-in-VAT-determination (archived at DOI
10.5281/zenodo.22083282).
References
Anthropic. How we built our multi-agent research system. Anthropic Engineering blog, 2025. URL
https://www.anthropic.com/engineering/built-multi-agent-research-system.
Gagan Bansal, Wenyue Hua, Zezhou Huang, Adam Fourney, et al. Magentic marketplace: An
open-source environment for studying agentic markets, 2025. arXiv:2510.25779.
Mert Cemri, Melissa Z. Pan, et al. Why do multi-agent LLM systems fail?, 2025. arXiv:2503.13657.
Lingjiao Chen, Jared Quincy Davis, Boris Hanin, Peter Bailis, Ion Stoica, Matei Zaharia, and James
Zou. Are more LLM calls all you need? towards scaling laws of compound inference systems. In
Advances in Neural Information Processing Systems, volume 37, 2024. arXiv:2403.02419.
Massimo Cossentino, Salvatore Gaglio, Luca Sabatucci, and Valeria Seidita. The PASSI and
agile PASSI MAS meta-models compared with a unifying proposal. InMulti-Agent Systems
and Applications IV (CEEMAS), volume 3690 ofLNCS, pages 183–192. Springer, 2005. doi:
10.1007/11559221_19.
Adam Fourney, Gagan Bansal, Hussein Mozannar, et al. Magentic-one: A generalist multi-agent
system for solving complex tasks, 2024. arXiv:2411.04468.
Sina Gogani-Khiabani, Ashutosh Trivedi, Diptikalyan Saha, and Saeid Tizpaz-Niari. An LLM
agentic approach for legal-critical software: A case study for tax prep software. InProceedings of
the 48th IEEE/ACM International Conference on Software Engineering (ICSE ’26), 2026. doi:
10.1145/3744916.3764575. arXiv:2509.13471.
Neel Guha et al. LegalBench: A collaboratively built benchmark for measuring legal reasoning in
large language models, 2023. arXiv:2308.11462; NeurIPS 2023 Datasets and Benchmarks.
Nils Holzenberger, Andrew Blair-Stanek, and Benjamin Van Durme. A dataset for statutory reasoning
in tax law entailment and question answering. InProceedings of the Natural Legal Language
Processing Workshop (KDD), 2020. arXiv:2005.05257.
Sirui Hong et al. MetaGPT: Meta programming for a multi-agent collaborative framework, 2023.
arXiv:2308.00352; published at ICLR 2024.
Mohammad Karimadini and Hai Lin. Synchronized task decomposition for cooperative multi-agent
systems, 2009. arXiv:0911.0231.
Xiaoxiao Li. When single-agent with skills replace multi-agent systems and when they fail, 2026.
arXiv:2601.04748.
Yiyan Lin, Sandeep Kulkarni, and Arshad Jhumka. Automation of fault-tolerant graceful degradation.
Distributed Computing, 32(1):1–25, 2019. doi: 10.1007/s00446-017-0319-x.
Renato C. Mendonça Filho and Nabor C. Mendonça. Performance impact of microservice gran-
ularity decisions: An empirical evaluation using the service weaver framework. InSoftware
Architecture (ECSA 2024), volume 14889 ofLNCS, pages 191–206. Springer, 2024. doi:
10.1007/978-3-031-70797-1_13.
25

Kunihiro Miyazaki, Takanobu Kawahara, Stephen Roberts, and Stefan Zohren. Toward expert invest-
ment teams: A multi-agent LLM system with fine-grained trading tasks, 2026. arXiv:2602.23330.
Juan Pavón and Jorge Gómez-Sanz. Agent oriented software engineering with INGENIAS. In
Multi-Agent Systems and Applications III (CEEMAS), volume 2691 ofLNCS, pages 394–403.
Springer, 2003.
Chen Qian et al. ChatDev: Communicative agents for software development, 2023. arXiv:2307.07924;
published at ACL 2024.
Arjun Sahney, Ram Gorthi, Cezary Łastowski, and Javier Vega. Operand quant: A single-agent
architecture for autonomous machine learning engineering, 2025. arXiv:2510.11694.
Jinwei Su, Qizhen Lan, Yinghui Xia, et al. Difficulty-aware agentic orchestration for query-specific
multi-agent workflows, 2025. arXiv:2509.11079.
Aaron Xuxiang Tian, Ruofan Zhang, Jiayao Tang, Young Min Cho, et al. Beyond the strongest LLM:
Multi-turn multi-agent orchestration vs. single LLMs on benchmarks, 2025. arXiv:2509.23537.
Fredy H. Vera-Rivera et al. Defining and measuring microservice granularity — a literature overview.
PeerJ Computer Science, 7:e695, 2021.
Tonghan Wang, Tarun Gupta, Anuj Mahajan, Bei Peng, Shimon Whiteson, and Chongjie Zhang.
RODE: Learning roles to decompose multi-agent tasks. InInternational Conference on Learning
Representations (ICLR), 2020. arXiv:2010.01523; published at ICLR 2021.
Yaoxiang Wang et al. TDAG: A multi-agent framework based on dynamic task decomposition and
agent generation.Neural Networks, 2025. arXiv:2402.10178.
Qingyun Wu, Gagan Bansal, Jieyu Zhang, et al. AutoGen: Enabling next-gen LLM applications via
multi-agent conversation, 2023. arXiv:2308.08155.
Yu Xia, Junwu Zhu, and Liucun Zhu. Dynamic role discovery and assignment in multi-agent
task decomposition.Complex & Intelligent Systems, 9(6):6211–6222, 2023. doi: 10.1007/
s40747-023-01071-x.
Jiawei Xu, Arief Koesdwiady, Sisong Bei, et al. Rethinking the value of multi-agent workflow: A
strong single agent baseline. InInternational Conference on Learning Representations (ICLR),
2026. arXiv:2601.12307.
Walden Yan. Don’t build multi-agents. Cognition AI blog, 2025. URL https://cognition.ai/
blog/dont-build-multi-agents.
Yiming Zhao, Tiziano De Matteis, and Justus Bogner. How does microservice granularity impact
energy consumption and performance? a controlled experiment. InIEEE International Conference
on Software Architecture (ICSA), 2025. arXiv:2502.00482.
26

A S0 prompt and tuning disclosure
The S0 system prompt is assembled deterministically by assemble_s0_prompt() in the released
artifact (src/harness/s0.py) from the shared static components of §4 plus three S0-specific knobs;
the text below is the assembled prompt used in the main sweep (SHA-2569d7ba74fa46456a4).
You are a VAT determination worker in a decomposed multi-agent system. You are responsible
for a fixed slice of the determination and nothing else. Work only from the state you are
given and the tools you may call. Do not restate table values from memory; obtain rates,
category kinds, and citation keys through the tools. Be deterministic and terse.
You solve the ENTIRE VAT determination for a case in one pass, with no orchestrator and no
per-subtask dispatch. You own all five subtasks: CLS, JUR, RAT, EXM, RCH.
You will receive the full case view (parties, transaction type, registration, and line
items).
Tools you may call: classification_reference, rate_table_lookup, rule_citation_retrieval,
vat_registration_check.
CLS — classification. Assign each line item to exactly one category from the closed
vocabulary. Call classification_reference to obtain the vocabulary and each category’s
kind. Cite CLS.ASSIGNED.
JUR — jurisdiction / place of supply. From the supplier and customer countries, the
transaction type, and the customer’s VAT-registration status, determine the jurisdiction
whose regime applies and the path taken (domestic / intra_community_b2b /
b2c_cross_border). You may call vat_registration_check for the registration input and
rule_citation_retrieval for the governing citation.
RAT — rate lookup. The rate band follows the classified category (bounded rule): reduced
band for RED_GOODS, RED_SERVICE; standard band for GEN_GOODS, GEN_SERVICE; no band for
EXEMPT_SUPPLY. For each line with a band, look up the rate for the jurisdiction and that
band with rate_table_lookup; never invent a rate. For an exempt-category line, no rate band
applies: record rate_band and rate as null and cite RATE.NA_EXEMPT.
EXM — exemption check. Using the exemption table provided in your state, decide whether
each line is exempt. An exempt line must cite the exemption rule; a non-exempt line is
taxed according to its band.
RCH — reverse-charge / liable-party synthesis. For each line resolve exactly one outcome
under the precedence EXEMPT > REVERSE_CHARGE > STANDARD_CHARGE, and set reverse_charge,
liable_party, vat_amount, and the non-charging reason accordingly. Cite the governing rule
obtained from rule_citation_retrieval.
CLS record: an object with keys subtask (== "CLS"), decision {category (one of:
"GEN_GOODS", "RED_GOODS", "GEN_SERVICE", "RED_SERVICE", "EXEMPT_SUPPLY")}, support (object
of the inputs you consumed), and rule_reference (exactly one of: "CLS.ASSIGNED").
JUR record: an object with keys subtask (== "JUR"), decision {jurisdiction (one of: "DE",
"FR", "IE", "ES"); jur_path (one of: "domestic", "intra_community_b2b",
"b2c_cross_border")}, support (object of the inputs you consumed), and rule_reference
(exactly one of: "JUR.B2C_CROSS_BORDER", "JUR.DOMESTIC", "JUR.INTRA_EU_B2B").
RAT record: an object with keys subtask (== "RAT"), decision {rate_band (string|null); rate
(number|null)}, support (object of the inputs you consumed), and rule_reference (exactly
one of: "RATE.NA_EXEMPT", "RATE.REDUCED", "RATE.STANDARD").
EXM record: an object with keys subtask (== "EXM"), decision {exempt (boolean)}, support
(object of the inputs you consumed), and rule_reference (exactly one of:
"EXM.EXEMPT_SUPPLY", "EXM.NONE").
RCH record: an object with keys subtask (== "RCH"), decision {outcome (one of:
"standard_charge", "reverse_charge", "exempt"); reverse_charge (boolean); liable_party (one
of: "supplier", "customer", "none"); vat_amount (number); non_charging_reason (one of:
"reverse_charge", "exempt", null)}, support (object of the inputs you consumed), and
rule_reference (exactly one of: "RC.B2B.INTRA_EU", "RC.B2C.SUPPLIER_CHARGES",
"RC.DOMESTIC.SUPPLIER_CHARGES", "RC.EXEMPT.NO_CHARGE").
Exemption table (reference R), authoritative:
EXEMPTION TABLE (bounded reference R). Only categories marked ’yes’ are exempt.
category=GEN_GOODS exempt=no
category=RED_GOODS exempt=no
category=GEN_SERVICE exempt=no
category=RED_SERVICE exempt=no
category=EXEMPT_SUPPLY exempt=yes
Tool-use rules: cite only rule keys returned by rule_citation_retrieval; never guess table
values — call rate_table_lookup for rates and classification_reference for category kinds;
call vat_registration_check for the registration input where relevant.
Emit exactly one JSON object in a single fenced ‘‘‘json block as the LAST content of your
final message, of the complete shape: {"case_id": <id>, "jur": <JUR record>, "lines":
[{"line_id": <id>, "cls": <record>, "rat": <record>, "exm": <record>, "rch": <record>},
...], "final": <aggregation block>}. Produce every record and the final block yourself.
"final": an object whose required keys are: currency (string); total_vat_amount (number);
lines (array). Optional: jurisdiction (one of: "DE", "FR", "IE", "ES"). Emit no other keys.
27

The matched-token arms tune three knob families on the eight-case development split ( dev_001–
dev_008): role-description expansion, worked exemplars, and an explicit scratchpad. The discrete
tuning ladder resolved both budget targets ( ¯BC2 and ¯BC⋆) to the same rung (L5), so both arms ran
one tuned prompt (§7.3); the ladder, the per-rung dev measurements, and the tuned prompt are in the
artifact (tune_s0prime.py). Per-worker prompt hashes for the orchestrated conditions:
Worker SHA-256 (first 16)
C1:CLS+JUR+RAT+EXM+RCH c57df552d55512b4
C2:CLS+JUR 29886613159ed705
C2:RAT+EXM+RCH f01dc26662087cff
C3:CLS e5757066e25a3950
C3:JUR 48b4aed6480e8fca
C3:RAT+EXM+RCH f01dc26662087cff
C4:CLS e5757066e25a3950
C4:EXM 1b2d9d2e6d74e957
C4:JUR 48b4aed6480e8fca
C4:RAT aa5a3fbdb8566ce4
C4:RCH 8f563505f7016930
B Per-scenario-family descriptives
Mean final-answer accuracy per scenario family in the main sweep (ten cases per family, five repeats
aggregated to case level; descriptive only, no inference atn=10). Families derive deterministically
from case inputs: multi-category invoices aremixed; single-category cases split by supplier/customer
country equality (domestic) and transaction type (B2Cvs.intra-community B2B). Row means
reproduce Table 1 exactly.
Family S0 C1 C2 C3 C4
Domestic 0.90 0.96 0.84 0.86 0.90
Intra-community B2B 0.82 0.70 0.88 0.92 0.62
B2C rate differential 0.68 0.62 0.84 0.82 0.86
Mixed invoices 0.62 0.60 0.76 0.72 0.70
The family texture matches the error localization of §7.2: the wide scopes lead ondomestic(C1 0.96)
but pay onintra-community B2B(C1 0.70; C4 0.62), where jurisdiction and reverse-charge synthesis
dominate; the intermediates are the only conditions above 0.70 in every family.
C Failure-injection configuration
All injection assignments are frozen in data/injection_plan.json (generator L3-injection-v1,
seed 20260801); the harness consumes this file, so the assignments below are the executed ones.
Per-case target subtaskτ(shared across conditions and repeats):
eval_001: RCHeval_002: RATeval_003: RCHeval_004: JUR
eval_005: CLSeval_006: JUReval_007: RATeval_008: JUR
eval_009: RATeval_010: CLSeval_011: RCHeval_012: CLS
eval_013: JUReval_014: RCHeval_015: EXMeval_016: JUR
eval_017: RCHeval_018: RCHeval_019: RATeval_020: RCH
eval_021: RATeval_022: JUReval_023: JUReval_024: JUR
eval_025: CLSeval_026: RATeval_027: JUReval_028: RCH
eval_029: JUReval_030: CLSeval_031: EXMeval_032: RCH
eval_033: EXMeval_034: CLSeval_035: JUReval_036: CLS
eval_037: EXMeval_038: RATeval_039: CLSeval_040: RAT
Shared-tool outage affects one seeded case per half-family block: eval_004, eval_009, eval_014,
eval_018, eval_021, eval_029, eval_035, eval_039. Hallucinated records are constructed
deterministically per case by the released generator: a schema-conforming record for τ whose
decision contradicts the oracle label and whose rule citation is drawn from the closed citation set but
does not support the decision; the full 40-record set ships in the plan file. Example (eval_001):
{
28

"decision": {
"liable_party": "customer",
"non_charging_reason": "reverse_charge",
"outcome": "reverse_charge",
"reverse_charge": true,
"vat_amount": 0.0
},
"rule_reference": "RC.B2B.INTRA_EU",
"subtask": "RCH",
"support": {
"category": "GEN_SERVICE",
"jur_path": "domestic"
}
}
D Pinned model, decoding, and price sheet
Model (pinned)claude-haiku-4-5-20251001
Temperature 0.2 (top-pat provider default; §4)
Max tokens per call 4096
Per-call timeout 120 s
Per-subtask retry budget (C1–C4) 3
S0 whole-trace repair budget 3
Within-case concurrency cap 2
Price sheet (pinned 2026-08-02) $1.00 / $5.00 per 1M input/output tokens
Oracle commite2d2bdd22
Dataset SHA-2563dc683ec4186...
Generator seed 42; cases 40 eval + 8 dev
Dollar cost is derived from token counts at scoring time only; any price change during the study is a
new pinned file version recorded in the project log.
29
