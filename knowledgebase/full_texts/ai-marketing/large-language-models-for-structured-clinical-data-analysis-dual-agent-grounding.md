---
title: 'Large Language Models for Structured Clinical Data Analysis: Dual-Agent Grounding and Validation'
url: https://arxiv.org/abs/2609.34039
category: ai-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Erfan D. Dehkalani
- Seetha Shankaran
- Abbot R. Laptook
- C. Michael Cotten
- P. Ellen Grant
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.34039
pages: 22
chars: 55999
fetched_at: '2026-11-08T13:32:09+00:00'
kb_version: 1
---

# Large Language Models for Structured Clinical Data Analysis: Dual-Agent Grounding and Validation

Large Language Models for Structured Clinical Data Analysis:
Dual-Agent Grounding and Validation
Erfan D. Dehkalani*1, Seetha Shankaran2, Abbot R. Laptook3, C. Michael Cotten4, P. Ellen
Grant1, and Yangming Ou1
1Fetal-Neonatal Neuroimaging and Developmental Science Center, Boston Children’s Hospital, and Harvard Medical
School, Boston, MA, USA
2Department of Pediatrics, Wayne State University School of Medicine, Detroit, MI, USA
3Department of Pediatrics, Women & Infants Hospital of Rhode Island, and Warren Alpert Medical School of Brown
University, Providence, RI, USA
4Division of Neonatology, Department of Pediatrics, Duke University School of Medicine, Durham, NC, USA
Abstract
Objective:To develop and characterize CLEAR-Med, a dual-agent framework for natural-language
analysis of structured clinical data that separates SQL-based invocation from independent validation.
Methods:CLEAR-Med uses one agent to translate a question into executable Structured Query Lan-
guage (SQL), retain the executed query and database result, and produce a draft. Deterministic checks
and a separately invoked cross-provider Validation Agent then accept the draft, request one bounded
repair, or abstain. We formalized the system as a bounded selective pipeline and evaluated CLEAR-
Med’s configuration and scalability, and the Invocation Agent’s accuracy and consistency on a 25-query
development benchmark, using a harmonized 21-site neonatal hypoxic-ischemic encephalopathy table
containing 532 de-identified infant records and approximately 1,300 variables.
Results:CLEAR-Med completed all six nominal scalability configurations, including500×1300.
Across 25 development-benchmark queries repeated five times, the Invocation Agent answered 83 of
125 responses correctly (66.4%; query-cluster bootstrap 95% CI, 48.0–83.2%), compared with 15 of
125 (12.0%; 95% CI, 3.2–22.4%) for the ungrounded ChatGPT baseline, a paired improvement of 54.4
percentage points (95% CI, 36.8–72.0%).
Conclusion:CLEAR-Med provides a general architecture for traceable analysis of structured clini-
cal data: numerical claims remain linked to executed SQL, and unresolved cases can fail closed. The re-
ported experiments characterize CLEAR-Med’s configuration and scalability and the Invocation Agent’s
accuracy, while the formal analysis establishes the encoded-property guarantee of the complete control
flow; a prospective full-pipeline evaluation of the validation and abstention stages is the next stage of
this work.
Keywords:Clinical informatics, Large language models, Text-to-SQL, AI agents, Structured data, Valida-
tion
*Corresponding author: Erfan.Darzi@childrens.harvard.edu
1
arXiv:2609.34039v1  [cs.AI]  28 Sep 2026

1 Introduction
Large language models (LLMs) can summarize biomedical prose, but governed clinical tables require a dif-
ferent kind of grounding: the answer must follow the schema, cohort definition, denominator, and executed
calculation. An ungrounded model can produce a plausible numerical statement without access to the rows
that support it, and fluent wording does not expose whether the value came from the intended population
[1, 2].
We use neonatal hypoxic-ischemic encephalopathy (HIE) as the study domain. HIE follows impaired
oxygen and blood supply around birth and can be associated with neonatal brain injury visible on mag-
netic resonance imaging [3]. Its trial data combine treatment assignments, physiological measurements,
imaging variables, and longitudinal outcomes, making cohort selection and denominator fidelity central to
retrospective analysis.
The analysis table harmonizes two multicenter Neonatal Research Network trials across 21 sites and
contains 532 de-identified infant records with approximately 1,300 variables per record [4, 5]. Each row
represents one participant, and all variables follow NRN definitions.
Three technical problems follow. First, a relational answer depends on exact columns, joins, filters, and
aggregation operators. Second, serializing a532×1300clinical table into a prompt discards the database
interface and does not scale as a general query mechanism. Third, the system must translate a natural-
language question into SQL and translate the executed result back into an answer without changing the
cohort or numerical meaning. The executed database must therefore remain the numerical source of record.
We proposeCLEAR-Med(Clinical Enhanced Analysis and Retrieval System for Medicine), a dual-agent
framework that coordinates two separately invoked components with distinct roles. TheInvocation Agent
generates and executes SQL against the structured HIE database and produces a draft response. TheClinical
Validation Agentchecks the draft, its executed SQL, and its database result against deterministic and clinical
constraints before the system accepts, repairs, or abstains.
Contributions.This work makes three contributions:
(1) a provenance-preserving dual-agent architecture that separates SQL generation and execution from
deterministic checks, independent validation, bounded repair, and fail-closed abstention (Figure 1 and
Algorithm 1);
(2) an oracle-scored evaluation of CLEAR-Med’s configuration and scalability, and of the Invocation
Agent’s accuracy and consistency, across 25 clinical query templates forming a development bench-
mark with repeated trials and task-level breakdowns (Section 3.7); and
(3) a bounded selective-decision model and a property-specific encoded-validity guarantee for the com-
plete dual-agent control flow (Section 3.2 and Appendix A.4).
The formal contribution is deliberately property-specific. If faithful database execution and sound exe-
cutable checks establish a stated property, CLEAR-Med can emit only an answer that satisfies that property;
unresolved cases abstain. This guarantee does not extend to clinical judgments that have not been encoded
as executable checks. Section 3.2 states the result, and Appendix A.4 gives its compact proof.
2

Table 1: Statement of Significance
Problem or IssueNatural-language analysis of governed clinical tables can produce fluent numerical
answers without exposing the cohort, calculation, or supporting rows.
What is Already
Known
Language models can generate SQL and use external tools, but query generation alone
does not establish that a reported number preserves the executed result and intended
clinical constraints.
What this Paper
Adds
CLEAR-Med separates schema-guided SQL invocation from deterministic checks and an
independently invoked Validation Agent. The pipeline retains SQL provenance, permits
one bounded repair, abstains on unresolved failures, and provides a property-specific
encoded-validity guarantee.
Who would benefit
from the new
knowledge in this
paper
Biomedical-informatics researchers and clinical-data teams building auditable
natural-language interfaces to governed relational data.
2 Related Work
Biomedical language models have been adapted for medical dialogue, consultation, multilingual question
answering, and domain knowledge [6–12]. Healthcare-agent research extends this line toward planning, tool
use, and multi-agent collaboration; a recent JBI survey organizes those systems around agent capabilities,
applications, and evaluation requirements [13]. CLEAR-Med addresses a narrower informatics problem:
producing an auditable numerical answer from a governed relational table.
Clinical text-to-SQL systems translate natural-language requests into database operations. UniQA used
a unified encoder–decoder architecture for complex electronic health-record questions [14]; MedT5SQL
studied healthcare-domain text-to-SQL conversion [15]; and Criteria2Query 3.0 used a generative language
model to construct executable cohort queries from clinical-trial eligibility criteria [16]. Other work has
examined context-aware pharmacovigilance SQL and generalization across medical text-to-SQL datasets
[17, 18]. CLEAR-Med treats query generation as the first stage rather than the endpoint: the executed SQL,
raw database result, and natural-language draft form an evidence record for a separate validation decision.
Document-retrieval RAG grounds generation in retrieved passages [19, 20], while tool-using language
models can select and invoke external functions [21]. A relational aggregate requires a different evidentiary
chain because its value is determined by the selected table, cohort predicate, denominator, and aggregation
operator. The dual-agent design combines tool-mediated execution with explicit provenance, executable
checks, independent review, bounded repair, and abstention; the formal analysis distinguishes guarantees
for encoded properties from residual clinical judgment.
3 Methods
3.1 Overview
CLEAR-Medis a dual-agent framework for natural-language analysis of structured disease-specific clinical
data. Figure 1 shows the two-agent workflow. Section 3.3 introduces the SQLite database, Sections 3.4 and
3

3.5 describe the two agents, and Section 3.6 specifies the complete control flow.
3.2 Formal Dual-Agent Guarantee
Letxbe a question,Dthe fixed database, andz j = (q j, dj, rj,c j)the SQL, executed result, draft, and
checker outcomes at attemptj∈ {0,1}. CLEAR-Med maps eachz j toaccept,repair, orabstain, permits
at most one repair, and emitsY∈ {r0, r1,⊥}, where⊥denotes abstention.
Theorem 1(Bounded encoded-validity guarantee).Let each executable checkerC k be sound for its encoded
propertyP k, soC k(z) = 1⇒P k(z) = 1for every reachable state. Under faithful database execution and
Algorithm 1’s fail-closed control flow,
N≤2, Y̸=⊥=⇒
K^
k=1
Pk(zτ ),Pr µ

Y̸=⊥,¬
K^
k=1
Pk(zτ )
!
= 0(1)
for any distributionµover admissible questions, whereNis the number of SQL-generation attempts and
τ∈ {0,1}is the accepted attempt. Every unresolved path terminates in⊥.
The result follows because acceptance requires every checker to pass, checker soundness transfers those
passes to their encoded properties, and the only other terminal outcome is abstention after zero or one repair.
Appendix A.4 gives the proof and the risk–coverage definitions used in evaluation.
The result follows because acceptance requires every checker to pass,
checker soundness transfers those passes to their encoded properties, and
the only other terminal outcome is abstention after zero or one repair. Ap-
pendix A.4 gives the proof and the risk–coverage definitions used in evalua-
tion.
INPUT
Clinical
question
input x
AGENT 1
Invocation
generate SQL q
execute result d
compose draft r
SAFETY GATE
Deterministic checks
SQL safety + provenance
cohort + numeric checks
units + ranges
AGENT 2
Independent validation
review (x, q, d, r)
constraint card
+ check report
ACCEPT
Validated response y
SQL + result +
checks retained
REPAIR ONCE
structured instruction
returns to Agent 1
ABSTAIN
fail closed on unresolved,
malformed, or un-
available evidence
DUAL-AGENT EVIDENCE PIPELINE
evidence record all checks pass accept
failed check
repair abstain
one bounded retry; rerun every check second failure
Figure 1: CLEAR-Med’s complete dual-agent architecture. Agent 1 produces an SQL-
grounded evidence record; deterministic checks and Agent 2 independently validate that
record before the system accepts with provenance, performs one bounded repair, or fails
closed with explicit abstention.
3.3. Convert Excel to SQLite Database
Our harmonized 21-site HIE database was originally stored as an Excel
table with 532 participant rows and approximately 1,300 variable columns.
This exact row count describes the analysis table; the500× 1300 size used
later is a nominal synthetic scalability configuration.
We converted the Excel table into an SQLite database—a lightweight,
serverless, single-file relational engine—to enable querying via Structured
Query Language (SQL).
Each de-identified participant occupies a row and each variable a col-
umn; site information is likewise de-identified. All variables follow estab-
lished Neonatal Research Network (NRN) protocols, so direct transfer to
datasets with different variable definitions may require further adaptation
and validation.
Beyond more expressive queries than Excel (worked examples appear in
Appendix A), SQLite enforces a schema—table definitions, data types, and
inter-variable relationships—which improves data consistency and retrieval.
A minimal HIEpatient schema illustrates this:
CREATE TABLE HIEpatient (
6
 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
Figure 1: CLEAR-Med’s complete dual-agent architecture. Agent 1 produces an SQL-grounded evidence
record; deterministic checks and Agent 2 independently validate that record before the system accepts with
provenance, performs one bounded repair, or fails closed with explicit abstention.
3.3 Convert Excel to SQLite Database
Our harmonized 21-site HIE database was originally stored as an Excel table with 532 participant rows and
approximately 1,300 variable columns. This exact row count describes the analysis table; the500×1300
size used later is a nominal synthetic scalability configuration.
We converted the Excel table into an SQLite database—a lightweight, serverless, single-file relational
engine—to enable querying via Structured Query Language (SQL).
4

Each de-identified participant occupies a row and each variable a column; site information is likewise de-
identified. All variables follow established Neonatal Research Network (NRN) protocols, so direct transfer
to datasets with different variable definitions may require further adaptation and validation.
Beyond more expressive queries than Excel (worked examples appear in Appendix A), SQLite enforces
a schema—table definitions, data types, and inter-variable relationships—which improves data consistency
and retrieval. A minimalHIEpatientschema illustrates this:
CREATE TABLE HIEpatient (
patientID INTEGER PRIMARY KEY ,
birthYear INTEGER ,
oneMinApgar INTEGER ,
expertMRIScore TEXT ,
normalOutcomeOrNot TEXT
);
This 5-column schema scales to the thousands of columns in the HIE dictionary and encodes constraints such
as thePRIMARY KEYonpatientID. Querying it requires translating clinicians’ natural-language questions
into SQL—the role of the Invocation Agent described next.
3.4 Invocation Agent
patientID INTEGER PRIMARY KEY ,
birthYear INTEGER ,
on eMi nAp gar INTEGER ,
e x p e r t M R I S c o r e TEXT ,
n o r m a l O u t c o m e O r N o t TEXT
) ;
This 5-column schema scales to the thousands of columns in the HIE
dictionary and encodes constraints such as thePRIMARY KEY on patientID.
Querying it requires translating clinicians’ natural-language questions into
SQL—the role of the Invocation Agent described next.
3.4. Invocation Agent
Invocation evidence
packet
question x; executed
SQL q
database result d; draft
r
constraint card Cx
Deterministic layer
read-only SQL; complete
provenance
cohort/column fidelity;
denominator
arithmetic; units; declared
ranges
Cross-provider review
operationally independent
invocation
reads x, q, d, r, check report,
Cx
returns a structured decision
only
accept
emit final y = r
retain SQL/result
provenance
repair
send correc-
tion instruction
back to Invo-
cation Agent
abstain
direct decision
or unresolved
after the one repair
emit no nu-
merical answer
Invocation Agent
generate and execute
new SQL
produce a new draft evi-
dence packet
checks pass
failed-check codes
one repair only
new (q, d, r); full revalidation
Figure 2: Detailed validation and repair flow. The Invocation Agent emits only a draft
response r in an evidence packet. The validation stage never edits a numerical answer: a
repair returns a structured instruction to SQL generation and execution, after which the
entire deterministic and cross-provider validation sequence runs again.
The Invocation Agent (Figure 2) takes two inputs—a natural-language
queryx (e.g., “What is the association between cord blood pH and neurode-
velopmental outcome in HIE patients?”) and the disease-specific databaseD
with its schemaS—and produces a draft response through four stages:
* Parsing and planning – take the natural-language query, extract
relevant tables and fields, load the invocation model, and read the
schema;
* SQL generation– translate the natural-language query into a schema-
aware SQL queryq;
* SQL execution against the clinical database– executeq against
SQLite and retrieve resultd; and
7
 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
Figure 2: Detailed validation and repair flow. The Invocation Agent emits only a draft responserin an evi-
dence packet. The validation stage never edits a numerical answer: a repair returns a structured instruction to
SQL generation and execution, after which the entire deterministic and cross-provider validation sequence
runs again.
The Invocation Agent (Figure 2) takes two inputs—a natural-language queryx(e.g., “What is the asso-
ciation between cord blood pH and neurodevelopmental outcome in HIE patients?”) and the disease-specific
databaseDwith its schemaS—and produces a draft response through four stages:
*Parsing and planning– take the natural-language query, extract relevant tables and fields, load the
invocation model, and read the schema;
*SQL generation– translate the natural-language query into a schema-aware SQL queryq;
5

*SQL execution against the clinical database– executeqagainst SQLite and retrieve resultd; and
*Draft response– interpretdas a natural-language draftr. This is not the final validated responsey.
At its core, the agent uses LangChain’sSQLDatabaseToolkitto generate, execute, and interpret SQL
from natural-language inputs, with built-in error-checking for invalid syntax or empty result sets. The de-
sign follows [21], in which language models self-supervise external tool use; unlike encoder–decoder EHR
question-answering systems that require extensive fine-tuning [14], ours needs none. This mechanism is
schema-guided agentic text-to-SQL, not conventional document-retrieval RAG: schema queries place ta-
ble definitions, column names, and data types in the model context, while the executed relational database
remains the source of numerical evidence.
3.5 Clinical Validation Agent
The Clinical Validation Agent (Figure 2) converts the Invocation Agent record(q, d, r)—the executed SQL
q, raw resultd, and draft responser—into a final responsey. Validation first applies deterministic checks
for read-only SQL, complete SQL/result provenance, cohort and column fidelity, non-missing denomina-
tors, arithmetic, units, and declared ranges. A cross-family language model then independently reviews
the question, SQL, result, draft, deterministic-check report, and prospectively authored clinical constraint
card. It must return one structured decision:accept,repair, orabstain. Here,independentdenotes
operational separation: the validator is a separately invoked, cross-provider model that did not generate or
execute the original SQL.
An accepted response retains the executed SQL provenance. A repair decision cannot directly author a
replacement number; instead, it supplies a structured correction instruction to the Invocation Agent, which
generates and executes new SQL and undergoes the complete validation sequence again. CLEAR-Med
permits exactly one repair. Any second failure, missing evidence, malformed validator response, or unavail-
able validator produces an explicit abstention. This fail-closed design distinguishes factual support by the
database from broader clinical plausibility and prevents a plausible but unsupported number from passing
validation.
Theorem 1 formalizes this fail-closed guarantee for encoded properties. The reported empirical analyses
characterize CLEAR-Med’s configuration, scalability, accuracy, and consistency.
3.6 Pseudocode for CLEAR-Med
Notation.Here,xis the question,qthe executed SQL,dits database result,rthe Invocation Agent’s draft,
vthe deterministic-check report,ythe final output, andDthe fixed database. Acceptance setsy=r; an
unaccepted draft is never emitted.
Algorithm 1 summarizes the provenance-preserving invocation, independent validation, single repair,
and fail-closed abstention workflow.
6

Algorithm 1CLEAR-Med Dual-Agent Workflow
Require:Natural language queryx; domain schemaS; databaseD; clinical constraintsC; invocation model
LI; validation modelL V
Ensure:Validated clinical responseyor explicit abstention
1:Initialize read-only database tools and load the reviewed constraint cardC x
2:forj∈ {0,1}do
3:(q j, dj, rj)←INVOCATIONAGENT(x,S,D, L I )
4:v j ←DETERMINISTICCHECKS(x, q j, dj, rj,C x)
5:ifv j failsthen
6:a j ←repairwith the failed-check codes
7:else
8:a j ←CLINICALVALIDATIONAGENT(x, q j, dj, rj, vj,C x, LV )
9:end if
10:ifa j =acceptthen
11:y←r j
12:returnywith(q j, dj, vj)provenance
13:else ifa j =abstainorj= 1then
14:returnexplicit abstention with failure codes
15:else
16:append the structured repair instruction to the next invocation
17:end if
18:end for
3.7 Evaluation Design
The reported evaluation comprises three analyses: configuration screening, an end-to-end scalability com-
parison, and an oracle-scored development benchmark of Invocation Agent accuracy and consistency.
Model details.The configuration screen compared ChatGPT Thinking (OpenAI) with ChatGPT Instant
(OpenAI) at temperature 0.7. The dual-agent architecture pairs the selected ChatGPT Thinking invocation
configuration with Claude through the Anthropic API at temperature 0 for independent validation using a
structured decision schema. The development benchmark measures the Invocation Agent; the validation and
abstention stages are specified here and evaluated prospectively in a full-pipeline study. No model training
or fine-tuning was performed.
Benchmark set and scoring.The development benchmark contained 25 natural-language clinical ques-
tions covering counts, percentages, group comparisons, odds ratios, and multi-condition filters over the har-
monized HIE database. Each question was posed five times to the Invocation Agent and to an ungrounded
ChatGPT baseline, yielding 125 responses per condition. Responses were scored against deterministic ora-
cles: percentages and counts within 5%, percentage-point differences within 2 points, and odds ratios within
10%. Query-template bootstrap resampling preserved the five repeated trials when estimating confidence
intervals and the paired accuracy difference.
Coverage, accepted-output accuracy, and incorrect-emission risk for the validation and abstention stages are
7

defined in Appendix A.4.3 as the endpoints of that full-pipeline evaluation.
3.8 Optimization of CLEAR-Med
3.8.1 Choosing the ChatGPT configuration
We compared ChatGPT Thinking (OpenAI) and ChatGPT Instant on the time-based and operational diag-
nostics defined in Table A.1, Panel A. Where speed and successful SQL generation conflicted, we prioritized
successful generation over latency.
3.8.2 Optimizing other hyperparameters
We screened four hyperparameters—Max Iterations (10/50/100), Max Execution Time (10/30/60 s), Agent
Type (openai-tools vs. tool-calling), and Top K (10/50/100)—varying each in isolation. Table A.1, Panel
C, defines the six recorded diagnostics. We first required successful SQL generation and execution, then
preferred fewer errors and lower execution cost; SQL length and complexity serve as descriptive query
characteristics.
3.9 End-to-End Scalability Comparison
3.9.1 Language-Model Comparators and Interface
For the end-to-end scalability screen, we selected five language models spanning biomedical, medical-
dialogue, and general-purpose configurations. All systems used the same six nominal table sizes, five-minute
timeout, and success definition. CLEAR-Med retained each table in SQLite and used ChatGPT Thinking
(OpenAI) with schema-guided SQL tools; the comparison models ran on the hosted HPC GPU allocation
and processed a serialized table in context. Table 2 compares the tested interfaces end to end.
•OpenBioLLM-8B(aaditya/Llama3-OpenBioLLM-8B) [6]: an 8B biomedical language model.
•open-bio-med-8B(timberrific/open-bio-med-merge) [8]: an 8B biomedical language model.
•Med-ChimeraLlama-3-8B(ChenWeiLi/Med-ChimeraLlama-3-8B SHERP) [7]: an 8B medical lan-
guage model.
•Daredevil-8B(mlabonne/Daredevil-8B-abliterated) [22]: a general-purpose 8B language model.
•DISC-MedLLM[11]: a medical-dialogue language model.
Exact public identifiers are listed for unambiguous model identification. These five comparators appear
in the scalability screen (Section 3.9.2); accuracy and consistency are reported for the separate benchmark
in Section 3.9.3.
8

3.9.2 Scalability Metric
The scalability grid contains six row-by-column configurations:50×50,50×100,100×50,100×100,
50×1000, and500×1300. A configuration is successful only when it completes within 300 seconds
without a GPU out-of-memory failure. We report the percentage of the six configurations completed, the
largest successful configuration by cell count, and elapsed time at that configuration.
3.9.3 Accuracy and Consistency Metrics
CLEAR-Med’s second objective was accurate and consistent numerical analysis on real HIE data. For
numeric predictionx q,i and nonzero deterministic oracleGT q, we computed signed relative errore q,i, its
mean absolute value over defined predictions, and the percentage of all attempts within 5% of the oracle:
eq,i = 100 xq,i −GT q |GTq| ,Err = 1 |M| X (q,i)∈M |eq,i|,
GT5% = 100 #{|xq,i −GT q| ≤0.05|GTq|} all attempts .
(2)
Oracle-zero, missing, and nonnumeric outputs are excluded from Err because relative error is undefined, but
missing and nonnumeric outputs count as failures forGT 5%. Repeated-run consistency is summarized by
the range and standard deviation ofe q,i within each query, averaged over queries with at least two defined
errors.
4 Results
4.1 Optimization of CLEAR-Med
4.1.1 Choosing the ChatGPT configuration
We compared ChatGPT Thinking (OpenAI) and ChatGPT Instant on the SQL-generation task (Table A.1,
Panel B). Agent invocation dominated runtime: ChatGPT Instant invoked in 29.23 s versus 167.44 s for
ChatGPT Thinking (a 5.7×speedup). ChatGPT Instant produced three errors, hit the iteration limit, and
returned no valid SQL, whereas ChatGPT Thinking completed without errors and generated a usable query.
Both issued two database invocations, but only ChatGPT Thinking produced a usable result, indicating that
optimization should target the invocation step.
Setup, database, and file-loading times were negligible relative to invocation. We therefore selected
ChatGPT Thinking (OpenAI) because it completed the SQL-generation task successfully.
4.1.2 Setting up other key hyperparameters
Max iterations.Varying the iteration limit (10/50/100; ChatGPT Thinking (OpenAI), openai-tools, Top
K=10), the 50-iteration setting was fastest (134.19 s), used one database invocation, and retained the high-
est observed SQL-complexity score (6). The 10-iteration setting was slowest and required three database
9

invocations, while 100 iterations produced a substantially simpler query. Under the stated rule, we selected
Max Iterations=50 for the reported configuration.
Max execution time.Varying the time limit (10/30/60 s), errors remained constant at three per run, but
only the 60 s setting reached a database invocation. We therefore selected 60 s. Total runtime can exceed the
nominal per-step limit because the agent may complete or retry other steps before termination.
Setting Agent Type.In the one-factor screen (Table A.1, Panel D), openai-tools completed the task in roughly
half the time of tool-calling (80.57 s vs. 165.39 s); both invoked the database once. We chose openai-tools
for its lower execution cost.
Setting Top K Threshold.In the one-query screen, Top K=10 was fastest (119.01 s) and retained more
SQL operations than 50 or 100 (complexity 16 vs. 2). We therefore retained Top K=10 for the reported
configuration. This screen assesses execution and query structure, not answer correctness; numerical validity
is evaluated against deterministic oracles and by the complete validation pipeline.
4.2 End-to-End Scalability Results
4.2.1 Scalability
CLEAR-Med was the only evaluated system to process the largest nominal500×1300test table (Table
2), using≈19.71 GB of the 39.56 GB GPU memory; four comparison models reached GPU memory limits
beyond100×100(≈16,000 tokens), and one exceeded the timeout beyond50×50. Configuring the
largest table took 28 s, comparable to the 2–26 s required by the comparison models for a table 1/65 its size.
CLEAR-Med completed six of six fixed configurations, versus four of six or one of six for the comparison
models, under the deployment interfaces described in Section 3.9.
Table 2: End-to-end scalability across six fixed table configurations under the deployment interfaces de-
scribed in Section 3.9. The table reports deterministic completion status and elapsed time for each tested
configuration.
System50×50 50×100 100×50 100×100 50×1000 500×1300
Max
Time (s) Notes
OpenBioLLM-8B [6]✓ ✓ ✓ ✓× ×2.19 CUDA OOM
open-bio-med-8B [8]✓ ✓ ✓ ✓× ×11.78 CUDA OOM
Med-ChimeraLlama-3-8B [7]✓ ✓ ✓ ✓× ×26.05 CUDA OOM
Daredevil-8B [22]✓ ✓ ✓ ✓× ×26.00 CUDA OOM
DISC-MedLLM [11]✓× × × × ×32.86 Timeout
CLEAR-Med✓ ✓ ✓ ✓ ✓ ✓28.12–
✓: Successful execution;×: Failed execution
All experiments were conducted on a hosted HPC GPU node with 39.56 GB of available device memory.
CUDA OOM: Memory allocation exceeded available GPU memory.
Timeout: Execution exceeded 5 minutes without producing results.
10

4.3 CLEAR-Med Development-Benchmark Results
We evaluated 25 natural-language clinical queries over the harmonized HIE database—counts, percent-
ages, group comparisons, odds ratios, and multi-condition filters spanning the Optimizing Cooling and Late
Hypothermia cohorts—each posed five times (K= 5), yielding 125 responses per condition and 250 re-
sponses overall. The comparator was the ChatGPT baseline answering directly from an in-context table
without database tools. Every response was scored against a deterministic oracle (percent/count within 5%;
percentage-point differences within 2 points; odds ratios within 10%).
The Invocation Agent answered correctly on 83 of 125 responses (66.4%; query-cluster bootstrap 95%
CI 48.0–83.2%) versus 15 of 125 (12.0%; 95% CI 3.2–22.4%) for the ungrounded ChatGPT baseline (Ope-
nAI API), a paired improvement of 54.4 percentage points (95% CI 36.8–72.0). Task-type values with their
denominators appear in Table 4; difficulty-stratified values appear in Table A.1, Panel E. Across the 12
percentage-valued queries (60 responses per condition), the Invocation Agent was within 5% of the oracle
on 39 of 60 responses versus 4 of 60 for the baseline; the corresponding error and repeated-run dispersion
measures appear in Table 3.
Table 3: Accuracy and consistency on numerical queries across repeated trials (K= 5repetitions, 12
percentage-valued queries). Err = mean absolute percentage error vs. the deterministic data oracle; 5%-GT
= share of responses within 5% of ground truth; SD and Range are computed across repetitions and averaged
over queries. Arrows (↓/↑) indicate the preferred direction.
Condition Err (%) ↓ 5%-GT (%)↑ SD (%)↓ Range (%)↓
ChatGPT baseline (OpenAI API) 55.74 6.67 58.80 146.58
Invocation Agent 33.67 65.00 35.07 78.55
Table 4: Per-task accuracy across 25 queries×5 repetitions.nis the number of responses per condition in
each subgroup. Overall accuracy (n= 125per condition) is reported with a query-cluster bootstrap 95%
confidence interval.
Task typen/condition ChatGPT baseline Invocation Agent
comparison 30 0.0 30.0
count 25 36.0 100.0
multi-condition 20 5.0 50.0
odds ratio 10 20.0 100.0
percentage 40 7.5 72.5
Overall (95% CI) 12512.0 [3.2, 22.4]66.4 [48.0, 83.2]
5 Discussion
5.1 Principal Findings and Interpretation
The experiments establish two findings. CLEAR-Med completed all six nominal scalability configurations,
including500×1300, under the tested SQL-tool interface. Across the 25-query development benchmark, the
11

Invocation Agent achieved 66.4% accuracy against deterministic numerical oracles, compared with 12.0%
for the ungrounded ChatGPT baseline. The comparison reflects the full invocation configuration, combining
database access, schema guidance, and prompt design.
CLEAR-Med keeps the relational database as the numerical source of record. Unlike document-retrieval
RAG, which retrieves passages for synthesis, the Invocation Agent exposes schema metadata, generates
SQL, executes it, and retains the query and result with the draft. The second agent then evaluates that
evidence record through deterministic checks and a separately invoked cross-provider review. This division
supports governed retrospective analysis and hypothesis generation.
ChatGPT Thinking (OpenAI) was slower than ChatGPT Instant but produced usable SQL in the reported
task. The one-factor screens identified the operating settings used for the development configuration.
5.2 Comparison with Related Approaches
Clinical text-to-SQL work has shown that language models can translate clinical criteria and questions
into executable queries [14–16]. CLEAR-Med extends that interface into a selective evidence pipeline:
query generation, execution, answer composition, deterministic checking, and independent validation are
represented as distinct operations with explicit terminal decisions. The architectural claim is therefore not
that a second model substitutes for a database oracle, but that a separately invoked validator can inspect the
complete evidence record after deterministic properties have been checked and can trigger bounded repair
or abstention.
This distinction also separates CLEAR-Med from passage-based retrieval augmentation. A retrieved
passage remains evidence that must be interpreted, whereas a relational aggregate is determined by exe-
cutable operations over a fixed database. Retaining the SQL, result, check report, and validation decision
makes the provenance chain inspectable and provides a natural unit for auditing structured-data analyses.
5.3 Applicability
The demonstrated use case is retrospective, research-oriented analysis of a harmonized neonatal HIE schema.
The same architecture can be configured for other governed relational clinical datasets by replacing the
schema description, executable constraint cards, and deterministic oracles while retaining the invocation–
validation control flow. Such transfer calls for dataset-specific validation.
5.4 Limitations
The study remains limited to one harmonized HIE schema, sequential rather than joint configuration screen-
ing, and a 25-query development benchmark whose errors informed prompt and oracle corrections. Finally,
the conditional guarantee covers only properties represented by sound executable checkers under faithful
database execution; open-ended clinical reasoning, individualized prognosis, and transfer to other schemas
remain outside the demonstrated scope.
12

6 Conclusion
CLEAR-Med provides a dual-agent, schema-guided framework for structured clinical data analysis with
SQL provenance, deterministic checks, independent validation, bounded repair, and explicit abstention. The
component studies show that CLEAR-Med’s SQL interface can scale to the full nominal HIE table and
that its Invocation Agent substantially outperformed an ungrounded ChatGPT baseline on oracle-scored
development queries. Held-out testing and a full-pipeline evaluation of the validation and abstention stages
form the next stage of this work. By making acceptance contingent on an inspectable evidence record,
the architecture defines a general route from natural-language questions to auditable numerical answers in
governed relational data.
A Extended Methods and Supporting Material
A.1 System and Dataset Summary
•Intended use:research and educational analysis of structured neonatal HIE trial data via natural-
language querying.
•Models:ChatGPT Thinking (OpenAI) at temperature 0.7 for invocation and Claude through the
Anthropic API at temperature 0 for independent validation; no fine-tuning. Requested and API-
returned identifiers and access timestamps are retained per run.
•Data:de-identified, harmonized NRN HIE database (Optimizing Cooling and Late Hypothermia
trials, 21 sites); variables defined by established NRN protocols; access restricted (see Data Availabil-
ity).
•Reported metrics:configuration diagnostics, scalability success, numerical accuracy, oracle error,
repeated-run dispersion, and task- and difficulty-stratified accuracy.
•Safety controls:every accepted number retains SQL provenance and passes deterministic and inde-
pendent validation; unresolved or malformed cases abstain after at most one repair.
A.2 Supporting Tables
A.3 Illustrative SQL Examples
The following worked examples illustrate the querying advantages of the SQLite formulation described in
Section 3.3.
Example A.1.Compared to Excel, one advantage of SQLite is that it enables more powerful and flexible
querying capabilities, particularly for complex data operations. For instance, in Excel, performing a query
to analyze the correlation between neonatal brain injury severity and long-term neurodevelopmental out-
comes would require complex formulas or Visual Basic for Applications (VBA) scripting. In contrast, SQLite
allows for such operations using a simple SQL query. An example SQL query in SQLite might look like this:
13

Table A.1: Supporting definitions and results. Panel A: operational definitions for the efficiency and execu-
tion diagnostics used to compare ChatGPT configurations. The final column gives the preferred direction;
an em dash denotes a descriptive metric. All time measures are in seconds.
Metric Operational definition Goal
Time-based diagnostics
Setup environment time Time to initialize the computational environment↓
Load files to database Time to load data files into the database↓
Setup database time Time to configure the database for query processing↓
Setup language model time Time to initialize the language model↓
Create agent time Time to instantiate the SQL agent↓
Invoke agent time Time for the agent to process a request and generate SQL↓
Execution time Total duration from invocation start to final response↓
Total time Aggregate duration of all setup and processing steps↓
Operational diagnostics
Number of errors Count of SQL syntax errors and execution failures↓
SQL query generated Binary indicator (yes/no) of successful SQL generation↑
Number of database invoca-
tions
Count of successful database connections and queries —
Table A.1: Supporting definitions and results (continued). Panel B: efficiency and SQL-agent diagnostics
for the two ChatGPT configurations. Arrows (↓/↑) indicate the preferred direction.
Function execution times (seconds)
Configuration
Setup↓
environment
Load files↓
to DB
Setup↓
database
Setup↓
LLM
Create↓
agent
Invoke↓
agent
ChatGPT Thinking
(OpenAI) 1.10×10 −5 0.02 0.14 0.04 0.24 167.44
ChatGPT Instant1.10×10 −5 0.02 0.14 0.05 0.004 29.23
SQL-agent task performance
Configuration
Execution↓
time (s)
Total↓
time (s)
Number of↓
errors
SQL query↑
generated
Number of
DB invocations
ChatGPT Thinking
(OpenAI) 170.64 171.14 0 Yes 2
ChatGPT Instant 87.00 87.23 3 No 2
14

Table A.1: Supporting definitions and results (continued). Panel C: diagnostics used in the one-factor-at-
a-time configuration screen. The final column gives the preferred direction where applicable; an em dash
denotes a descriptive diagnostic.
Metric Operational definition Goal
Performance diagnostics
Execution time Duration from invocation start to final response↓
Total time Execution time plus all setup operations↓
Number of database invoca-
tions
Count of successful database connections and queries —
Number of errors Count of SQL syntax errors and execution failures↓
Query diagnostics
SQL length Character count of the generated SQL statement —
SQL complexity Sum of joins (J), conditions (C), aggregations (A), and
subqueries (S): J+C+A+S
—
Table A.1: Supporting definitions and results (continued). Panel D: one-factor-at-a-time configuration
screen for CLEAR-Med. The check mark identifies the setting selected for the reported configuration.
Selection first required successful SQL generation and execution, then used errors and execution cost; SQL
length and complexity are descriptive. An em dash indicates that the diagnostic was not recorded for that
factor.
Factor Setting Exec. (s) Total (s) Errors DB inv. SQL len. SQL compl. Selected
Max iterations
10 317.12 317.30 – 3 503 5
50 134.19 134.71 – 1 555 6✓
100 139.08 139.28 – 1 208 2
Max execution time
10 s 38.52 38.71 3 0 – –
30 s 49.90 50.13 3 0 – –
60 s 85.40 85.60 3 1 – –✓
Agent type openai-tools 80.57 81.06 – 1 208 2✓ tool-calling 165.39 165.64 – 1 350 3
Top K
10 119.01 – – – 717 16✓
50 133.16 – – – 294 2
100 134.29 – – – 196 2
Table A.1: Supporting definitions and results (continued). Panel E: accuracy by query difficulty.nis the
number of responses per condition; the clustered interval for the overall result appears in Table 4.
Difficultyn/condition ChatGPT baseline Invocation Agent
easy 45 24.4 86.7
medium 25 8.0 80.0
hard 55 3.6 43.6
15

SELECT severity,
AVG(cognitive_score) as avg_cognitive,
AVG(language_score) as avg_language,
AVG(motor_score) as avg_motor
FROM hie_patients
GROUP BY severity
ORDER BY severity;
This query efficiently analyzes the relationship between HIE severity and various neurodevelopmental out-
comes, a task that would be cumbersome in Excel.
Example A.2.Another advantage of SQLite over Excel is its ability to handle large datasets more efficiently.
While Excel has limitations on the number of rows or columns it can process, SQLite can manage millions
of records with ease. For example, an SQL query to analyze temporal changes in various clinical variables
for HIE patients could be written in SQLite as:
SELECT patient_id,
AVG(CASE WHEN time_point <= 6 THEN core_temp END) as avg_temp_0_6h,
AVG(CASE WHEN time_point > 6 AND time_point <= 24 THEN core_temp END) as avg_temp_6_24h,
AVG(CASE WHEN time_point > 24 AND time_point <= 48 THEN core_temp END) as avg_temp_24_48h,
AVG(CASE WHEN time_point > 48 AND time_point <= 72 THEN core_temp END) as avg_temp_48_72h,
MAX(sarnat_score) as max_sarnat_score,
MIN(umbilical_cord_ph) as min_umbilical_cord_ph,
SUM(CASE WHEN treatment = ’cooling’ THEN 1 ELSE 0 END) as cooling_sessions,
AVG(cooling_blanket_temp) as avg_cooling_blanket_temp
FROM hie_patient_data
GROUP BY patient_id;
This query efficiently analyzes and summarizes multiple clinical variables across different time points for
HIE patients, including core temperature changes, neurological assessments (Sarnat score), biochemical
markers (umbilical cord pH), treatment interventions (cooling sessions), and physiological measurements
(cooling blanket temperature). Such a comprehensive analysis would be challenging and potentially crash
Excel with a sufficiently large dataset, while SQLite can handle it with ease.
A.4 Formal Analysis of the Dual-Agent Selective Pipeline
This appendix supplies the transition semantics and proof underlying Theorem 1, then defines the selective-
evaluation quantities for prospective full-pipeline evaluation. It also separates gatewise residual risk without
assuming independence between agents and states the predictive-uncertainty identity that motivates deter-
ministic grounding. The guarantee itself applies only to properties represented by sound executable check-
ers.
A.4.1 State and Transition Semantics
For attemptj∈ {0,1}, letXbe the question,Q j the generated SQL,D j = Exec(Q j,D)its faithfully
executed result,R j the draft, andH j the repair history. The reachable state and conjunction of deterministic
16

checker outcomes are
Sj = (j, X,S, Qj, Dj, Rj,C X , Hj), G j =
KY
k=1
Ck(Sj).(A.1)
WhenG j = 1, write the separately invoked validator’s decision asA j; its possible actions areaccept,
repair, andabstain. The fail-closed transition is
∆j =



accept, G j = 1, Aj =accept,
repair, j= 0, G j = 0orA j =repair,
abstain,otherwise.
(A.2)
Operational independence means that the validator is a separate cross-provider invocation that did not gen-
erateQ j or execute it. It does not imply probabilistic independence between generation and validation.
A.4.2 Proof of the Encoded-Validity Guarantee
LetRdenote first-attempt repair. The four terminal paths are first-attempt acceptance, first-attempt absten-
tion, repair followed by acceptance, and repair followed by abstention. They are disjoint and exhaustive,
so
N= 1 +1 R ≤2, Y=



rτ ,on acceptance,
⊥,otherwise,
τ∈ {0,1}.(A.3)
IfY̸=⊥, acceptance givesG τ = 1, henceC k(Sτ ) = 1for everyk. Soundness givesC k(Sτ ) = 1⇒
Pk(Sτ ) = 1, proving the conjunction in Equation (1). The encoded-violation event is therefore empty for
every admissible question; integrating its zero indicator under any input distributionµproves the probability
statement.
A.4.3 Selective Evaluation Quantities
For conditionm, letE (m) =1{Y (m) ̸=⊥}indicate emission and letZ (m) indicate oracle correctness.
CoverageC m, incorrect-emission riskR m, and accepted-output accuracyA m are
Cm =E[E (m)], R m =E[E (m)(1−Z (m))],
Am = Pr(Z (m) = 1|E (m) = 1), R m =C m(1−A m). (A.4)
Fornquestion–repetition trials, the corresponding plug-in estimators are
bCm = 1 n nX ℓ=1 E(m) ℓ , bRm = 1 n nX ℓ=1 E(m) ℓ (1−Z (m) ℓ ),
bAm =
P
ℓ E(m) ℓ Z(m) ℓ
P
ℓ E(m) ℓ , bOm = 1 n nX ℓ=1 E(m) ℓ Z(m) ℓ . (A.5)
17

For conditionsaandb, b∆R = bRa − bRb measures the change in incorrect emission and b∆C = bCb − bCa
records the accompanying coverage change. Paired bootstrap resampling preserves repeated trials from the
same question template. These quantities are the prespecified endpoints for the full-pipeline evaluation.
A.4.4 Dependence-Aware Residual Risk
For attemptj, letI j denote an oracle-incorrect draft,G j a deterministic-gate pass, andL j validator ac-
ceptance, conditional on reaching that attempt (H j). The residual incorrect-acceptance probability factors
exactly as
Pr(Ij ∩G j ∩L j | Hj) = Pr(Ij | Hj) Pr(Gj |I j,H j) Pr(Lj |I j,G j,H j).(A.6)
This is the conditional chain rule, not an independence assumption. WithB j =I j ∩G j ∩L j,Rdenoting
first-attempt repair, andρ= Pr(R), the two disjoint acceptance branches give
Pr(B) = Pr(B0) +ρPr(B 1 |R).(A.7)
If the three conditional factors at attemptjare bounded byε I,j ,ε G,j, andε L,j, respectively, then
Pr(B)≤ε I,0 εG,0εL,0 +ρ εI,1 εG,1εL,1.(A.8)
For an error that violates a property covered by a sound checker, the corresponding deterministic-pass factor
is zero. No such conclusion follows for an unencoded clinical judgment, so the bound does not multiply
unconditional agent error rates.
A.4.5 Conditional Predictive Uncertainty
LetΘrepresent uncertainty over sampled model behavior,Qthe generated SQL,D= Exec(Q,D), andY
the response. For discreteYwith finite conditional entropy,
H(Y|X, D) =I(Y; Θ|X, D) +H(Y|X, D,Θ).(A.9)
The identity follows directly from the definition of conditional mutual information. For a deterministic
aggregate, the target is fixed once the database, cohort, and operator are fixed; repeated runs therefore
characterize model-induced variability in(Q, Y), whereas genuinely predictive clinical targets may retain
irreducible outcome uncertainty. The dual-agent control flow does not eliminate that distinction: it makes
executable properties checkable and routes unresolved cases to abstention.
Acknowledgments
We gratefully acknowledge the Neonatal Research Network (NRN) within the Eunice Kennedy Shriver
National Institute of Child Health and Human Development (NICHD) Neonatal Research Network for pro-
viding us access to the Optimizing Cooling (OC) and Late Hypothermia (LH) trial datasets, through RTI
18

International for their role as the Data Coordinating Center in managing these valuable neonatal medical
datasets (Scott A. McDonald, Jeanette O. Auman). Data from the 21 sites in these 2 trials were recently har-
monized into a unified database at Boston Children’s Hospital (Chuan-Heng Hsiao, Anna N. Foster, Rutvi
Vyas, Ankush Kesri, Rina Bao, Matheus D. Soldatelli, Aseelah Ashraf, Lena Tran, Janet S. Soul), which is
the data analysis center in the Consortium Of MRI Biomarker In Neonatal Encephalopathy (COMBINE).
This research was funded, in part, by NIH R61 NS126792 and R21 NS121735.
Funding
This work was supported, in part, by the National Institutes of Health [grant numbers R61 NS126792 and
R21 NS121735]. The funders had no role in study design; data collection, analysis, or interpretation;
manuscript preparation; or the decision to submit the article for publication.
CRediT authorship contribution statement
Erfan Darzidehkalani:Conceptualization, Methodology, Software, Formal analysis, Writing – original
draft.Seetha Shankaran:Validation, Writing – review & editing.Abbot R. Laptook:Validation, Writing
– review & editing.C. Michael Cotten:Validation, Writing – review & editing.P. Ellen Grant:Supervi-
sion, Funding acquisition, Writing – review & editing.Yangming Ou:Supervision, Funding acquisition,
Writing – review & editing.
Declaration of competing interest
The authors declare that they have no known competing financial interests or personal relationships that
could have appeared to influence the work reported in this paper.
Ethics approval
This study is a secondary analysis of data harmonized from two completed multicenter randomized con-
trolled trials conducted by the NICHD Neonatal Research Network: the Optimizing Cooling (OC) trial
[5] and the Late Hypothermia (LH) trial [4]. The original trials were approved by the institutional review
boards of participating sites, and informed consent was obtained from a parent or legal guardian of each
enrolled infant. For the present study, investigators accessed only fully de-identified records under appli-
cable data-governance arrangements; no new recruitment, intervention, participant contact, or attempt at
re-identification occurred. No separate study-specific ethics reference number applies to the present analy-
sis.
19

Consent to participate
Informed consent was obtained from a parent or legal guardian of each neonatal participant in the original
OC and LH trials. The present analysis involved no new participant enrollment or contact.
Consent for publication
Not applicable. This manuscript does not contain identifiable individual data.
Sex and gender reporting
This study evaluates a software pipeline rather than clinical associations or treatment effects. Sex and gender
were not used as predictors, outcomes, eligibility criteria, or subgroup variables in the reported benchmark;
accordingly, no sex- or gender-stratified analysis was performed.
Data availability
The harmonized analytical table used in this study is not publicly redistributed. De-identified source datasets
for the Optimizing Cooling and Late Hypothermia trials are available by application through the NICHD
Data and Specimen Hub (DASH). Requests are processed through the DASH data-request and data-use-
agreement workflow. Access to the study-specific harmonized table remains subject to applicable NICHD
Neonatal Research Network and institutional governance.
References
[1] E. H ¨ullermeier and W. Waegeman. Aleatoric and epistemic uncertainty in machine learning: An
introduction to concepts and methods.Machine learning, 110(3):457–506, 2021.
[2] T. J. Loftus, B. Shickel, M. M. Ruppert, J. A. Balch, T. Ozrazgat-Baslanti, P. J. Tighe, P. A. Efron,
W. R. Hogan, P. Rashidi, G. R. Upchurch Jr, et al. Uncertainty-aware deep learning in healthcare: a
scoping review.PLOS digital health, 1(8):e0000085, 2022.
[3] M. Douglas-Escobar and M. D. Weiss. Hypoxic-ischemic encephalopathy: a review for the clinician.
JAMA Pediatrics, 169(4):397–403, 2015. doi: 10.1001/jamapediatrics.2014.3269.
[4] A. R. Laptook, S. Shankaran, J. E. Tyson, B. Munoz, E. F. Bell, R. N. Goldberg, N. A. Parikh, N. Am-
balavanan, C. Pedroza, A. Pappas, et al. Effect of therapeutic hypothermia initiated after 6 hours of age
on death or disability among newborns with hypoxic-ischemic encephalopathy: a randomized clinical
trial.Jama, 318(16):1550–1560, 2017.
20

[5] S. Shankaran, A. R. Laptook, A. Pappas, S. A. McDonald, A. Das, J. E. Tyson, B. B. Poindexter,
K. Schibler, E. F. Bell, R. J. Heyne, et al. Effect of depth and duration of cooling on death or disability
at age 18 months among neonates with hypoxic-ischemic encephalopathy: a randomized clinical trial.
Jama, 318(1):57–67, 2017.
[6] A. Pal and M. Sankarasubbu. Llama3-OpenBioLLM-8B.https://huggingface.co/aaditya/
Llama3-OpenBioLLM-8B, 2024. online model documentation.
[7] W.-L. Chen. Med-ChimeraLlama-3-8B sherp.https://huggingface.co/ChenWeiLi/
Med-ChimeraLlama-3-8B_SHERP, 2024. online model documentation.
[8] T. Berger. open-bio-med-merge.https://huggingface.co/timberrific/
open-bio-med-merge, 2024. online model documentation.
[9] H. Zhang et al. Huatuogpt, towards taming language model to be a doctor., 2023. URLhttps:
//arxiv.org/abs/2305.15075.
[10] Y . R. Chen et al. Bianque: Balancing the questioning and suggestion ability of health llms with multi-
turn health conversations polished by chatgpt., 2023. URLhttps://arxiv.org/abs/2310.15896.
[11] Z. J. Bao et al. Disc-medllm: Bridging general large language models and real-world medical consul-
tation., 2023. URLhttps://arxiv.org/abs/2308.14346.
[12] P. Qiu et al. Towards building multilingual language model for medicine., 2024. URLhttps://
arxiv.org/abs/2402.13963.
[13] G. Xu, X. Li, Y . Chen, Y . Duan, S. Wu, H. Yu, C.-H. Chiu, J. Ni, N. Tang, T. J.-J. Li, A. Yuille, W. Jin,
and Y . Shi. A comprehensive survey of ai agents in healthcare.Journal of Biomedical Informatics,
179:105045, 2026. doi: 10.1016/j.jbi.2026.105045.
[14] S. Bae, D. Kim, J. Kim, and E. Choi. Question answering for complex electronic health records
database using unified encoder-decoder architecture.arXiv preprint arXiv:2111.14703, 2021.
[15] A. Marshan, A. N. Almutairi, A. Ioannou, D. Bell, A. Monaghan, and M. Arzoky. Medt5sql: a
transformers-based large language model for text-to-sql conversion in the healthcare domain.Frontiers
in Big Data, 7:1371680, 2024.
[16] J. Park, Y . Fang, C. Ta, G. Zhang, B. Idnay, F. Chen, D. Feng, R. Shyu, E. R. Gordon, M. Spotnitz, and
C. Weng. Criteria2query 3.0: Leveraging generative large language models for clinical trial eligibility
query generation.Journal of Biomedical Informatics, 154:104649, 2024. doi: 10.1016/j.jbi.2024.
104649.
[17] J. L. Painter, V . R. Chalamalasetti, R. Kassekert, and A. Bate. Automating pharmacovigilance
evidence generation: Using large language models to produce context-aware sql.arXiv preprint
arXiv:2406.10690, 2024.
21

[18] R. Tarbell, K.-K. R. Choo, G. Dietrich, and A. Rios. Towards understanding the generalization of
medical text-to-sql models and datasets.arXiv preprint arXiv:2303.12898, 2023.
[19] P. Lewis, E. Perez, A. Piktus, F. Petroni, V . Karpukhin, N. Goyal, H. K ¨uttler, M. Lewis, W.-t. Yih,
T. Rockt¨aschel, S. Riedel, and D. Kiela. Retrieval-augmented generation for knowledge-intensive nlp
tasks. InAdvances in Neural Information Processing Systems, volume 33, 2020.
[20] D. A. Weinert and A. M. Rauschecker. Enhancing large language models with retrieval-augmented
generation: a radiology-specific approach.Radiology: Artificial Intelligence, 7(3):e240313, 2025.
doi: 10.1148/ryai.240313.
[21] T. Schick, J. Dwivedi-Yu, R. Dess ´ı, R. Raileanu, M. Lomel ´ı, L. Zettlemoyer, N. Cancedda, and
T. Scialom. Toolformer: Language models can teach themselves to use tools.arXiv preprint
arXiv:2302.04761, 2023.
[22] M. Labonne. Daredevil-8B-abliterated.https://huggingface.co/mlabonne/
Daredevil-8B-abliterated, 2024. online model documentation.
22
