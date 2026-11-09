---
title: 'IDP AutoOpt: Agent-Driven Optimization of Document Processing Pipeline Configurations'
url: https://arxiv.org/abs/2607.26075
category: ai-marketing
subcategory: empirical
date: 2026-07
venue: ''
authors:
- David Kaleko
- Sergey Ivanov
- Md Mofijul Islam
source: arxiv
pdf_url: https://arxiv.org/pdf/2607.26075
pages: 14
chars: 55299
fetched_at: '2026-11-08T13:21:24+00:00'
kb_version: 1
---

# IDP AutoOpt: Agent-Driven Optimization of Document Processing Pipeline Configurations

IDP AutoOpt: Agent-Driven Optimization of Document Processing Pipeline
Configurations
David Kaleko, Sergey Ivanov, Md Mofijul Islam
Amazon Web Services
Abstract
We present IDP AutoOpt, an autonomous LLM
agent that discovers high-performing config-
urations for intelligent document processing
(IDP) pipelines. Tuning IDP prompts, models,
OCR settings, and schemas jointly currently
costs domain specialists 20 to 80+ person-hours
per document type and does not scale as enter-
prises add document classes. IDP AutoOpt
runs a closed loop: it scores a configuration
on a small labeled set, diagnoses field-level er-
rors, generates targeted edits, and re-evaluates,
guided by human-authored domain skills that
encode production expertise. Across extrac-
tion, classification, and packet-splitting tasks
deployed in healthcare, marketing-intelligence,
and financial-services settings, IDP AutoOpt
matches or exceeds human-expert accuracy at
equal or lower cost (on an extraction bench-
mark, 88.0% vs 81.6% at 4.6× lower per-page
cost), cutting configuration time from weeks to
under two hours. We further show a sharp ca-
pability gap among the agent LLMs we tested,
below which optimization fails outright, and
that curated domain skills tend to outperform
raw source-code access as a means of supply-
ing domain expertise to the agent. We also
share practical lessons on context management
and variance mitigation. Requiring only a con-
figurable pipeline, a scoring function, and a
small labeled set, we expect the approach to
extend beyond IDP to other enterprise AI sys-
tems, such as RAG and multi-agent workflows,
where configuration bottlenecks deployment.
1 Introduction
Intelligent document processing (IDP) systems
extract structured information from unstructured
documents by orchestrating OCR engines, large
language models, classification logic, and post-
processing rules into configurable pipelines (Yoon
et al., 2024; Wang and Shen, 2025; Islam et al.,
2026a). These systems have become critical in-
frastructure across industries, with deployments
processing hundreds of thousands of documents
daily.
Achieving high accuracy requires extensive con-
figuration: document schemas, OCR settings,
model selection, document classification, extrac-
tion prompts strategies must all be tuned jointly.
This configuration space is fundamentally hetero-
geneous, spanning natural language, categorical
choices, continuous parameters, structural deci-
sions, and semi-structured data. Unlike classical
hyperparameter tuning (Lin et al., 2025; Zhou et al.,
2024), IDP configuration requires the kind of rea-
soning a human engineer performs: diagnosing fail-
ure patterns, rewriting prompts based on observed
errors, and making structural pipeline changes.
Recent work has shown that LLM agents can
optimize software through closed-loop iteration
(Zhou et al., 2024; Lin et al., 2025; Chi et al.,
2024; Yang et al., 2024; Wang et al., 2024; Yük-
sekgönül et al., 2025). However, none of these sys-
tems address the challenges of IDP configuration,
where the search space is broader, compossible and
more heterogeneous than numeric knobs, code, or
prompt text alone.
To address this, we developed IDP AutoOpt,
an autonomous LLM agent that automates IDP
configuration through iterative evaluation-driven
optimization. Given a small labeled set of docu-
ments and a minimal starting configuration, the
agent operates in a closed loop: analyzing errors,
generating targeted modifications, evaluating, and
iterating, guided by domain skills encoding pro-
duction expertise. Our extensive experimental eval-
uations show that IDP AutoOpt exceeds human
expert accuracy on extraction, classification, and
packet splitting tasks while reducing configuration
effort from weeks to under 2 hours, and we provide
ablations on LLM choice, domain skills vs. source
code access, and practical deployment considera-
tions including convergence, variance, and context
management. Throughout, we report results under
arXiv:2607.26075v2  [cs.IR]  22 Aug 2026

a strict eval/test selection protocol (Section 4) and
assess accuracy comparisons against a noise-aware
threshold derived from repeated runs (Section 5).
2 Real-World Deployment
IDP AutoOpt is deployed in production and has
been applied to customer engagements spanning
healthcare document management, marketing intel-
ligence, and financial services. In this section, we
describe the deployment context that motivates our
system and the production results that validate it.
The configuration bottleneck:Based on data
from multiple engagements, domain specialists typ-
ically invest 20 to 80+ person-hours per document
type to achieve target accuracy. Complex multi-
class deployments (one customer manages 80+ doc-
ument configurations) require several weeks of it-
erative refinement. As organizations scale IDP to
more document types and higher volumes, manual
per-type tuning becomes unsustainable.
Production results:In one deployment process-
ing tens of millions of pages per month, a team
of specialists spent several weeks creating an ex-
traction configuration that achieved 88% accuracy.
Starting from scratch, IDP AutoOpt produced a
configuration reaching 89.5% accuracy at 3.7 ×
lower cost per page in a few hours of autonomous
operation. On a separate public benchmark, the
agent improved extraction accuracy from 75.5%
to 89.3% without model changes or cost increases
(see Section 5.5).
3 IDP AutoOpt: System Design
We frame the task as constrained optimization over
a compound processing pipeline. Consider a multi-
component system P (in our case, a document
processing pipeline combining OCR, classifica-
tion, and extraction stages) whose behavior is gov-
erned by a configuration c (a YAML file specify-
ing pipeline setup details, prompts, model choices,
schemas, and parameters). Given a small labeled
evaluation set D and a scoring function S that
measures how well the pipeline’s output matches
ground truth, we seek:
c∗ = arg max
c∈C
S(P(c), D), c∈Ω(1)
where Ω encodes operational constraints such as
cost budgets, latency requirements, or model avail-
ability. In our IDP instantiation, S computes field-
level extraction accuracy (how many fields were
extracted correctly), and the primary constraint Ω
imposes a per-page inference cost ceiling that re-
flects real customer budgets.
3.1 Architecture and Optimization Loop
IDP AutoOpt consists of three components (Fig-
ure 1):(1)anIDP pipeline, the document process-
ing platform invoked programmatically through an
evaluation API;(2)anevaluation harnessthat com-
putes field-level accuracy, generates per-document
error breakdowns, and versions every configuration
the agent produces; and(3)anautonomous opti-
mization agent, a multimodal LLM with tool access
that reasons over evaluation metrics, inspects doc-
ument images, and produces configuration edits
without any human intervention.
The optimization loop proceeds iteratively. At
each step, the agent receives feedback describing
which fields failed, on which documents, and with
what patterns. It diagnoses root causes, sometimes
inspecting document images via multimodal vi-
sion (e.g., to understand why a checkbox field fails
when text-only OCR cannot detect it), then gener-
ates targeted edits: rewriting a prompt, adding a
field description, switching an OCR backend, or
inserting a few-shot example. The modified config-
uration is evaluated over the full labeled set, and
the results inform the next decision. Throughout,
the agent maintains an append-onlyoptimization
logrecording every decision, rationale, and out-
come, which serves as both long-term memory and
a human-readable audit trail.
The agent terminates at a fixed iteration bud-
get (50), a wall-clock timeout (8 hours), or when
optimization cost exceeds a limit. Optionally, it
has read-only access to the target pipeline’s source
code, a realistic scenario for teams optimizing their
own systems (impact measured in Section 5).
3.2 Configuration Space
The YAML configuration governs a multi-stage
processing pipeline, each with independent set-
tings. The agent can modify:(1)natural-language
system/task prompts, JSON Schema field defini-
tions, and few-shot examples;(2)per-stage LLM
choice and hyperparameters (temperature, max to-
kens, top-p);(3)pipeline structure (extraction strat-
egy, classification method, splitting logic, assess-
ment granularity);(4)OCR backend, feature tog-
gles (layout analysis, table detection), and image

Optimization LoopInput Output
STARTING
CONFIG
model: sonnet
prompt: "Extract"
ocr: none
fields:
  Agency: null
  Date: null
  Total: null
EVAL SET
IDP PIPELINE
OCR → Splitting → Classification
→ Extraction → Post-proc
EVALUATION HARNESS
✗  Agency: 8/25
✗  Date: 5/25
✓  Total: 25/25
Overall: 81.2%
Cost: $0.02/pg
AUTONOMOUS OPTIMIZATION
AGENT
Agency entity accuracy is low, I will
investigate problematic files
🤖
file_read(eval_doc_1.pdf)
...
🔧
Agency usually appears in lower left, I will
update extraction prompt
🤖
edit_config_prompt("Agency name is
often in the lower left")
🔧
launch_new_evaluation()🔧
OPTIMIZED
CONFIG
model: sonnet
prompt: "Extract
  all fields..."
temperature: 0.1
ocr: textract
  dpi: 200
fields:
  Agency: "The
    agency name,
    usually in
    lower left"
  Date: "Date in
    MM/DD/YY
    format"
  Total: "Gross
    total in
    dollars"
predictions
feedback: errors + metrics
action: config edits
Figure 1: IDP AutoOpt optimization loop. The system takes a starting configuration (YAML) and a labeled
evaluation set as input. Inside the loop, the IDP pipeline produces predictions that the evaluation harness scores
per-field. The autonomous optimization agent diagnoses errors and generates targeted configuration edits. After
iterating, the system outputs an optimized configuration.
resolution; and(5)operational knobs (confidence
thresholds, prompt caching, regex bypasses, feature
flags). This space simultaneously includes natural
language, categorical variables, continuous param-
eters, structural choices, and semi-structured data,
which distinguishes it from tuning numeric knobs
or optimizing prompts in isolation.
3.3 Domain Skills
Domain skills are structured knowledge modules
encoding expert heuristics from production engage-
ments, each specifying a trigger condition, diag-
nostic steps, and resolution strategy. The sys-
tem includes 27 skills distilled from 8+ engage-
ments. For example,token-limit-fixis triggered
when documents produce truncated JSON at 0%
accuracy and prescribes increasing the output token
limit or decomposing the schema;visual-spatial-
extractionis triggered when fields depend on spa-
tial position (checkboxes, tables) and prescribes
enabling layout-aware OCR features;multilingual-
documentsis triggered for non-Latin scripts and
prescribes switching to a backend with broader lan-
guage coverage. Unlike auto-generated approaches
(Liu et al., 2026; Ouyang et al., 2026), our skills
are human-authored from experience, trading scal-
ability for reliability. The authoring cost is modest:
a domain expert starting cold takes roughly an hour
per skill, and in practice most skills are a byprod-
uct of engagement work already being performed,
since the diagnostic reasoning they encode is what
the expert did to resolve the customer’s issue in the
first place. The 27 skills used here were written
incrementally across 8+ engagements rather than
as a dedicated authoring effort. Whether this invest-
ment outperforms zero-effort alternatives is tested
in Section 5. A complete example skill is provided
in Appendix C.
3.4 Context Management
Long optimization runs exceed any model’s context
window. IDP AutoOpt uses proactive compaction:
when token usage exceeds a threshold (% of context
window), older history is summarized while the
optimization log is re-injected to preserve decision
continuity. Details are in Appendix B.
4 Experimental Setup
Dataset:We evaluate on the RealKIE FCC-
Verified dataset (Amazon AGI, 2024) a collection
of 75 real-world broadcast advertising invoices
spanning 18 distinct visual layouts from different
TV stations and media companies. The dataset is
split into aneval setof 25 documents (manually
selected to represent all layout templates) and a
held-outtest setof 49 documents (one excluded
due to annotation quality issues). The agent op-
timizes exclusively on the eval set; the test set is
reserved for final evaluation of selected configu-
rations. This relatively small dataset was chosen

because it reflects a common user pain point of
generating extensive high quality labeled data.
Test-set isolation protocol:The test set is in-
accessible to the optimizer by construction, not
merely by convention. The test documents are
never uploaded to the AWS account in which the
agent runs, so no tool available to the agent can
read them or score against them. Every configura-
tion the agent selects, and every decision it makes,
is based solely on eval-set accuracy. Test-set in-
ference is performed post hoc, after optimization
has terminated, in a separate account: we take the
configurations selected by eval accuracy and run
them against the test set purely to measure gen-
eralization and to draw Figure 2. Consequently
the test curves we report are diagnostic rather than
selective, and no reported number is obtained by
maximizing over test performance.
Task and metrics:The task is key information
extraction: given an invoice document, extract 7
top-level fields (Agency, Advertiser, GrossTotal,
PaymentTerms, AgencyCommission, NetAmount-
Due) and a variable-length array of line items
(each with 5 sub-fields). All fields use strict exact-
match evaluation; strings must match character-for-
character and numbers must match exactly. We
report two metrics, both of which select config-
urations using eval accuracy only. (1)Peak test
accuracyis the held-out test accuracyof the con-
figuration that scored highest on the eval setwhile
respecting the cost constraint. It is deliberately
not the maximum of the test curve: taking that
maximum would require the test set to inform se-
lection, which our protocol forbids. (2)AUC-50-
Calibratedis the area under the test accuracy curve
over 50 iterations, baseline-subtracted (zero means
no improvement), where the sequence of configu-
rations is the running maximumof eval accuracy
and each such configuration is then scored on test.
Both metrics therefore answer “how well do the
configurations a user would actually have chosen
generalize?” rather than “what is the best test score
obtainable in hindsight?”
Initial configuration and human baseline:All
experiments begin from the same minimal con-
figuration: field names with null descriptions, a
generic prompt, no few-shot examples, no OCR,
and Claude Sonnet 4.6 as extraction model (∼70%
test accuracy, zero human effort). As a comparison,
Table 1 shows domain specialists manually tun-
Version Acc. $/page Description
V1 76.2% 0.102 Haiku + Textract full
V3 78.3% 0.027 Nova 2 Lite + layout OCR
V5 75.2% 0.028 Simplified prompt
V_current 81.6% 0.102 Rich descriptions
Table 1: Human expert configuration trajectory on Re-
alKIE test set. Each version represents days to weeks
of iterative manual tuning. Weeks of effort plateau at
81.6% accuracy.
ing the same dataset over several weeks, reaching
81.6% at $0.102/page. The comparison is matched
on access: the human experts and the agent oper-
ated over the same labeled documents, the same
set of available models and OCR backends, and the
same configuration space, and both were scored by
the same evaluation harness on the same held-out
test set. The specialists were optimizing for accu-
racy, so 81.6% represents their best effort rather
than a configuration abandoned once a business tar-
get was met. There is one intentional asymmetry:
the agent was subject to a $0.05/page cost con-
straint, whereas the human baseline was uncapped
and its final configuration costs $0.102/page. The
agent therefore reached higher accuracy while con-
fined to less than half of the human’s per-page cost
budget. The two sides differ in effort rather than
access: weeks of specialist time against a few hours
of unattended computation.
Ablation conditions:We vary both the agent
LLM (Claude Opus 4.7, Claude Sonnet 4.6, Claude
Haiku 4.5, Kimi K2.5, Llama 4 Maverick) and the
domain knowledge available for the agent to read
(skills + source code, skills only, source code only,
neither). Each condition is repeated 2–3 times with
identical starting conditions to measure run-to-run
variance. All runs use 50 iterations, an 8-hour time-
out, and a cost constraint of $0.05/page.
5 Experimental Results
5.1 Comparison Against Human Experts
Figure 2 shows the trajectory of a single Sonnet
4.6 optimization run. Starting from a minimal 70%
configuration, the agent surpasses the human ex-
pert baseline (81.6%, produced over weeks of man-
ual tuning) by its 4th iteration, after adding robust
field descriptions and enabling OCR. It continues
improving through prompt refinement, few-shot
examples, and date format fixes (iterations 5–20),
then makes increasingly targeted discoveries such
as a Y/N bitmask encoding for date-type fields (iter-

Figure 2: IDP AutoOpt optimization trajectory (Sonnet 4.6, skills + source code). Blue: eval set accuracy. Red:
held-out test set accuracy. Dotted: human expert baseline on held-out test set (81.6%, $0.102/page). The agent
surpasses the expert by iteration 4. At the point of maximum eval accuracy (iteration 41, marked⋆; the configuration
a user would actually select), test accuracy is 88.0% at $0.022/page: +6.4 pp accuracy at 4.6× lower cost. The two
curves rise and fall together, with no systematic divergence. Late iterations continue improving with no saturation at
iteration 50, suggesting longer runs could push accuracy further.
ations 20–50). Eval accuracy is highest at iteration
41; that configuration scores 88.0% on the held-out
test set at $0.022/page, which is 6.4 percentage
points above the human expert at 4.6× lower cost
per page. We stress that 88.0% is the test score of
the eval-selected configuration, not the maximum
of the test curve. Individual later iterations do reach
higher test accuracy, but selecting them would re-
quire test-set access the agent does not have, so we
do not report them.
The agent also makes mistakes. At iteration 34,
it experiments with a cheaper model that causes
a regression, but detects the accuracy drop and
reverts to the prior configuration. This ability to
explore risky changes and recover is a structural
advantage of versioned configuration history. No-
tably, the test accuracy (red in Figure 2) tracks the
eval accuracy (blue) throughout, with no system-
atic divergence, showing no evidence of overfitting
when optimizing on 25 documents.
Finding 1.IDP AutoOpt exceeds the accu-
racy of human expert configurations (+6.4 pp) at
4.6× lower inference cost, reducing configura-
tion time from weeks of specialist effort to under
2 hours of autonomous operation.
Cost accounting.The 4.6 × figure comparesfinal
per-page inference cost, computed with the same
formula for the human and agent configurations
($0.102/page vs. $0.022/page). It excludes the cost
of optimization itself, which we report separately
here. The run shown in Figure 2 cost $139.47
in agent and evaluation inference. This is a one-
time cost per document type, incurred once and
amortized over the deployment’s lifetime, and it
should be weighed against the corresponding one-
time cost on the human side — the salaries paid
for weeks of specialist and domain-expert time —
which is larger by orders of magnitude.
5.2 Effect of Agent LLM Choice
Table 2 reveals a sharp division among the models
we tested. Sonnet, Opus, and Kimi all produce
meaningful optimization trajectories with substan-

Agent LLM AUC-50 Peak Acc. $/page
Claude Sonnet 4.6 5.28 88.5% 0.008
Claude Opus 4.7 3.89 84.9% 0.019
Kimi K2.5 3.72 84.1% 0.016
Claude Haiku 4.5 0.38 77.6% 0.034
Llama 4 Maverick 0.00 76.4% 0.011
Table 2: Agent LLM comparison (skills + source code,
best of 2–3 runs; peak accuracy is the test score of the
eval-selected configuration). A sharp capability gap
separates the models we tested; the weaker two fail to
improve upon the baseline.
tial accuracy gains. On the other side of the gap,
Haiku 4.5 barely improves (AUC 0.38) and Llama
4 Maverick fails entirely (AUC 0.00), never recov-
ering from early missteps. The separation is large
relative to run-to-run noise: the accuracy differ-
ence between the best and worst model is 10.9
pp, roughly twice the 5.4 pp minimum credible
improvement we derive below, and the AUC val-
ues on either side of the gap differ by an order
of magnitude. The two failing models fail in dif-
ferent ways (one cannot execute the optimization
protocol at all, the other executes it faithfully but
cannot find improving edits), which suggests the
binding constraint is model capability rather than
any single missing skill or infrastructure issue. The
optimization task requires simultaneously diagnos-
ing complex error patterns across multiple fields,
generating syntactically valid prompt edits, and
reasoning about trade-offs between accuracy and
cost. Models that lack the capacity to perform
all three of these in concert produce degenerate
trajectories. Additionally, Sonnet and Opus bene-
fit from 1-million-token context windows, which
reduce compaction frequency and preserve better
continuity between iterations. We describe this as
a gap among the five models we tested rather than
a universal threshold; with only five models, and a
frontier that moves quickly, we cannot locate a pre-
cise capability boundary or rule out that a smaller
model with different training would succeed.
Finding 2.A sharp capability gap separates the
agent LLMs we tested: the weaker two cannot
optimize at all (AUC ≤ 0.38), while the stronger
three produce consistent improvements well out-
side run-to-run noise. The optimization task re-
quires joint diagnosis, generation, and multi-step
reasoning capabilities, and a model lacking them
fails outright rather than optimizing more slowly.
Agent LLM Condition AUC-50 Peak Acc.
Sonnet 4.6 Skills + source 5.28 88.5%
Sonnet 4.6 Skills only 5.14 87.3%
Sonnet 4.6 Neither 4.95 87.0%
Sonnet 4.6 Source only3.0584.7%
Opus 4.7 Skills only 4.10 85.6%
Opus 4.7 Skills + source 3.89 84.9%
Opus 4.7 Neither 3.83 84.5%
Opus 4.7 Source only 3.16 86.2%
Table 3: Domain knowledge ablation (best of 2–3 runs;
peak accuracy is the test score of the eval-selected con-
figuration). Conditions with skills rank above source-
only for both models. Differences between adjacent
rows are small and we do not treat them as separable.
5.3 Domain Skills vs. Source Code Access
Across both models, the conditions with skills oc-
cupy the top of Table 3 and source-only sits at
the bottom, and the pattern is most pronounced
for Sonnet 4.6, where providing source code read
accesswithoutskills lowers AUC from 4.95 (no
knowledge at all) to 3.05 (source only). Individ-
ually these accuracy differences are small — the
largest gap between any two conditions is 3.8 pp —
so we treat the ordering as a tendency rather than
a precise ranking, and we do not claim that any
single pair of adjacent rows is separable.
The mechanism behind the tendency is visible
in the optimization logs, and is more informative
than the accuracy ordering. Source code is volu-
minous and unstructured; without skills to direct
attention, the agent spends iterations reading imple-
mentation details and exploring dead-end options
instead of making targeted improvements. Agents
without skills issue far more exploratory source-
code searches per run than agents with skills, and
they compact their context correspondingly more
often, spending budget on orientation rather than
on edits. Skills act as an attention filter, indicat-
ing what patterns to look for and what to do about
them. For Opus the effect is smaller, likely because
stronger models filter irrelevant information more
effectively on their own.
Finding 3.Curated domain skills tend to out-
perform raw source code read access as a means
of supplying domain expertise. We do not ob-
serve unstructured source access improving on
a no-knowledge baseline, and the optimization
logs show it diverting the agent’s budget toward
orientation rather than targeted edits, suggest-
ing that structured expertise matters more than
volume of information.

5.4 Practical Considerations
Run-to-run variance and a threshold for credi-
ble improvement.With identical starting condi-
tions, peak accuracy varies with a standard devia-
tion of 1.4–3.6 percentage points across runs, be-
cause the agent explores different configuration re-
gions depending on early stochastic choices. Skills
reduce this variance (0.9 pp with Sonnet + skills-
only across 4 runs). Pooling across 44 runs span-
ning eight ablation conditions gives a standard de-
viation of 2.7 pp, which we use to set aminimum
credible improvement of roughly 5.4 pp(two
pooled standard deviations). We apply this thresh-
old to our own results. The capability gap of Find-
ing 2 clears it comfortably (10.9 pp between the
best and worst model), as do the individual configu-
ration changes that drive most of the gains, such as
adding field descriptions (+29.9 pp) and enabling
layout-aware OCR (+12.6 pp). The differences
among the knowledge conditions of Finding 3 do
not clear it, which is why we present that ordering
as a tendency. Running k times and selecting the
best by eval accuracy is necessary in practice; this
multiplies the one-time optimization cost byk.
Context management.A 50-iteration trajectory
generates far more tokens than any model can at-
tend to at once. Before every model call, a hook
checks token usage against a configurable threshold
percentage of the context window. When exceeded,
the context window is compacted (details in Ap-
pendix B). At a 50% threshold, compaction fires
every ∼18 iterations with minimal impact on accu-
racy. At 10%, it fires ∼5 timesperiteration with
substantial negative impact on accuracy. We use
50% throughout .
Deployment infrastructure.The system runs on
Amazon Bedrock AgentCore, deployed via Cloud-
Formation with DynamoDB state persistence, S3
artifact storage, and a web frontend that allows non-
technical users to launch and monitor asynchronous
multi-hour optimization runs.
5.5 Generalization Across IDP Tasks
Table 4 confirms that the approach generalizes
beyond the extraction task. On classification (9
classes, 293 documents from the OCR-Benchmark
(OmniAI, 2025)), the agent matches human expert
accuracy at 21% lower cost in 4 iterations, by dis-
covering that OCR is unnecessary for multimodal
classification with detailed class descriptions. On
Task System Metric $/page
Extraction Human 81.6% 0.102 Agent88.0% 0.022
Classification Human 100% 0.0052 Agent 100%0.0041
Packet Split Human 75.9% 0.0052 Agent84.1%0.0052
Table 4: Agent vs. human expert across three IDP tasks
(agent: Sonnet 4.6, skills + source code). Agent matches
or beats the expert on all tasks at equal-or-lower cost.
packet splitting (15 classes, 500 documents from
DocSplit-Poly-Seq (Islam et al., 2026b)), the agent
achieves a 11% relative improvement over the hu-
man expert at identical cost, in 7 iterations.
Before running any of the experiments reported
in this paper, in a separate exploratory run, the
agent discovered that document class information
was encoded in file names and wrote a regex-
based strategy that bypassed LLM inference en-
tirely, reaching 100% accuracy at near-zero cost.
We treated this as objective leakage rather than a
result: we anonymized every file name to a UUID
before conducting the experiments reported here,
so no filename signal remains for the agent to ex-
ploit. No metrics anywhere in this paper were im-
pacted by this event. We retain the incident as a
reward-hacking case study because it illustrates a
general property worth designing around: the agent
optimizes the stated objective using any available
mechanism in the configuration space, and will
reach for structural, rule-based, or metadata-driven
strategies when they score well.
6 Related Work
Our work builds on three lines of research. First,
modern IDP systems (Zhang et al., 2024; Yoon
et al., 2024; Islam et al., 2026a; Wang and Shen,
2025; Kim et al., 2022) have advanced individ-
ual pipeline components (extraction, classification,
splitting) but do not address the joint optimization
of the full pipeline configuration. Second, LLM
agents have been applied to closed-loop optimiza-
tion of databases (Zhou et al., 2024; Lin et al.,
2025), ML pipelines (Chi et al., 2024), prompts
(Yang et al., 2024; Wang et al., 2024; Yüksekgönül
et al., 2025), workflows (Zhang et al., 2025b), and
hardware kernels (Zhang et al., 2025a), but each
operates over a single modality (numeric knobs,
code, or prompt text) rather than the mixed space of
prompts, models, schemas, and structural choices
that IDP requires. Third, structured skill injec-

tion (Khattab et al., 2024; Liu et al., 2026; Ouyang
et al., 2026) improves agent performance, but prior
work generates skills automatically; we show that
human-authored skills from production experience
provide more reliable value. A detailed discussion
is provided in Appendix D.
7 Conclusion
We presented IDP AutoOpt, a deployed agent that
autonomously optimizes IDP pipeline configura-
tions in under two hours, exceeding human expert
accuracy at lower cost across extraction, classifica-
tion, and packet splitting tasks. The architecture
is domain-agnostic and applies to any compound
processing system with a configurable pipeline, a
scoring function, and a small labeled set. Our abla-
tions show a sharp capability gap among the agent
LLMs we tested, below which optimization fails
outright, that curated skills tend to outperform raw
source code read access, and that context manage-
ment is necessary but robust across a range of set-
tings. We expect these findings to transfer beyond
IDP to RAG pipelines, multi-agent workflows, and
other enterprise AI systems where configuration
bottlenecks deployment at scale, though we have
not tested this: such settings may lack the clean
per-field diagnostic signal that makes IDP failures
straightforward to attribute. Run-to-run variance
remains a practical challenge, and domain skills
demand upfront authoring effort that may not scale
without automation.
Future work includes structured search methods
(tree search, evolutionary strategies) as alternatives
to free-form LLM reasoning, automated skill gen-
eration from optimization logs to reduce author-
ing cost, and extending time horizons to explore
whether accuracy continues improving beyond 50
iterations as our trajectories suggest.
8 Limitations
Run-to-run variance remains substantial, requiring
multiple optimization runs to reliably find strong
configurations. Pooled across 44 runs the standard
deviation of peak accuracy is 2.7 pp, which means
differences below roughly 5.4 pp are not credibly
separable from noise; several of our ablation com-
parisons fall below that bar and we present them as
tendencies rather than rankings. This increases the
total cost of using the system and means a single
run cannot guarantee a near-optimal result.
Domain skills require deliberate authoring effort
by experienced practitioners, on the order of an
hour per skill for an expert starting cold. Teams ap-
plying this approach to a new domain would need
to invest in creating analogous knowledge, or ac-
cept whatever performance the skills-free condition
affords them in that domain.
Our experiments use a fixed 25-document eval
set. This size was a deliberate choice rather than a
convenience: customers often have limited labeled
data available at the start of an engagement, and
labeling is expensive enough that requiring hun-
dreds of documents would defeat the purpose of
the system. We have not systematically studied the
effect of eval set size on optimization quality other
than validating that such a relatively small eval set
is sufficient for optimization. We therefore cannot
say how the method behaves with a substantially
larger or smaller eval set, nor where the point of
diminishing returns lies.
Our optimization trajectories show no evidence
of convergence at 50 iterations, suggesting that
longer runs could yield further accuracy gains. We
leave extending time horizons to hundreds of itera-
tions to future work.
9 Broader Impact
Generality of the method:Although we instan-
tiate IDP AutoOpt for document processing, its
design is not specific to documents. The approach
applies to any compound system that exposes a
configurable pipeline, a scoring function over a
small labeled set, and an interface for reading errors
and applying edits. The heterogeneous configura-
tion space we optimize, spanning natural-language
prompts, categorical model choices, continuous
parameters, structural decisions, and schemas, is
shared by most modern AI systems. Plausible tar-
gets include retrieval-augmented generation, multi-
agent workflows, and AutoML pipelines, where
prior agentic optimizers typically operate over a
single modality; IDP AutoOpt instead optimizes
the full mixed space jointly. We have not evaluated
the approach in these settings, and we expect the
transfer to depend on how readily failures can be at-
tributed to specific components: IDP supplies a per-
field diagnostic signal that tells the agent precisely
what went wrong and where, whereas in retrieval
or multi-agent settings a poor final answer is harder
to trace to the configuration choice responsible for
it.

Transferable findings and assets:Our empiri-
cal results offer guidance beyond IDP. The capabil-
ity threshold indicates that the optimizing model
should not be economized, since a weaker model
fails to optimize rather than merely optimizing
more slowly. The tendency of curated skills to
outperform unstructured source-code access points
to a lesson in context engineering: for long-horizon
agents, what matters appears to be structured rel-
evance rather than raw volume of available infor-
mation. Our context-management and variance-
mitigation procedures generalize to any agent that
runs for extended horizons and exceeds its con-
text window. Several assets are reusable in isola-
tion, including the evaluation harness that versions
configurations to make exploration reversible, the
append-only log that serves as memory and an au-
dit trail, and the domain-skill format for encoding
expert heuristics.
Accessibility:By reducing specialist configura-
tion effort from tens of person-hours to hours of
autonomous operation, this class of system low-
ers the expertise barrier to deploying compound
AI. We view the effect as augmentation rather than
replacement, shifting expert effort from repetitive
per-task tuning toward encoding reusable knowl-
edge and reviewing outcomes.
Risks and responsible use:An agent that opti-
mizes any available signal will exploit unintended
ones; in an exploratory run preceding the experi-
ments reported here, ours discovered a filename-
based shortcut that leaked classification labels (Sec-
tion 5.5). Objective specifications and evalua-
tion sets must therefore be audited for leakage be-
fore optimization begins, and identifying metadata
anonymized, as we did by replacing every file name
with a UUID. Held-out validation remains essen-
tial, as optimizing on a small labeled set can yield
configurations that do not generalize. We note that
leakage is defined relative to the deployment condi-
tion rather than in the abstract: if a customer’s file
names genuinely encode document class at infer-
ence time, then a filename rule is a legitimate and
highly efficient solution for them, and the failure in
our case was that our evaluation set carried a signal
the production setting would not. Because such
systems process sensitive data, including health-
care and financial documents, they should operate
within the data owner’s boundary and receive only
the labeled samples required, and autonomously
generated configurations should be reviewed be-
fore deployment.
References
Amazon AGI. 2024. RealKIE-FCC-Verified. Hugging
Face Datasets. CC-BY-NC 4.0. Test set of 75 in-
voices from the FCC for key information extraction.
Yizhou Chi, Yizhang Lin, Sirui Hong, Duyi Pan, Yay-
ing Fei, Guanghao Mei, Bangbang Liu, Tianqi Pang,
Jacky Kwok, Ceyao Zhang, Bang Liu, and Chenglin
Wu. 2024. SELA: Tree-search enhanced LLM agents
for automated machine learning.arXiv preprint
arXiv:2410.17238.
Gaye Colakoglu, Gürkan Solmaz, and Jonathan Fürst.
2025. AgenticIE: An adaptive agent for informa-
tion extraction from complex regulatory documents.
arXiv preprint arXiv:2509.11773.
Xi Fang, Haoyi Tao, Shuwen Yang, Chaozheng Huang,
Suyang Zhong, Haocheng Lu, Han Lyu, Junjie
Wang, Xinyu Li, Linfeng Zhang, and Guolin Ke.
2025. Uni-Parser technical report.arXiv preprint
arXiv:2512.15098.
Md Mofijul Islam, Md Sirajus Salekin, Nivedha Balakr-
ishnan, Vincil C. Bishop III, Niharika Jain, Spencer
Romo, Bob Strahan, Boyi Xie, and Diego A. Socol-
insky. 2026a. DocSplit: A comprehensive bench-
mark dataset and evaluation approach for document
packet recognition and splitting.arXiv preprint
arXiv:2602.15958.
Md Mofijul Islam, Md Sirajus Salekin, Nivedha Balakr-
ishnan, Vincil C. Bishop III, Niharika Jain, Spencer
Romo, Bob Strahan, Boyi Xie, and Diego A. Socolin-
sky. 2026b. Docsplit: A comprehensive benchmark
dataset and evaluation approach for document packet
recognition and splitting.
Omar Khattab, Arnav Singhvi, Paridhi Maheshwari,
Zhiyuan Zhang, Keshav Santhanam, Sri Vard-
hamanan, Saiful Haq, Ashutosh Sharma, Thomas T.
Joshi, Hanna Moazam, Heather Miller, Matei Zaharia,
and Christopher Potts. 2024. DSPy: Compiling
declarative language model calls into self-improving
pipelines. InThe Twelfth International Conference
on Learning Representations.
Geewook Kim, Teakgyu Hong, Moonbin Yim,
JeongYeon Nam, Jinyoung Park, Jinyeong Yim, Won-
seok Hwang, Sangdoo Yun, Dongyoon Han, and Se-
unghyun Park. 2022. OCR-free document under-
standing transformer. InComputer Vision – ECCV
2022, volume 13688 ofLecture Notes in Computer
Science, pages 498–517. Springer.
Qizheng Li, Yifei Zhang, Xiao Yang, Xu Yang, Zhuo
Wang, Weiqing Liu, and Jiang Bian. 2026. FT-Dojo:
Towards autonomous LLM fine-tuning with language
agents.arXiv preprint arXiv:2603.01712.

Qi Lin, Zhenyu Zhang, Viraj Thakkar, Zhenjie Sun,
Mai Zheng, and Zhichao Cao. 2025. StorageXTuner:
An LLM agent-driven automatic tuning framework
for heterogeneous storage systems.arXiv preprint
arXiv:2510.25017.
Xingyan Liu, Xiyue Luo, Linyu Li, Ganghong Huang,
Jianfeng Liu, and Honglin Qiao. 2026. Skill-
Forge: Forging domain-specific, self-evolving agent
skills in cloud technical support.arXiv preprint
arXiv:2604.08618. Accepted at ACM SIGIR 2026
Industry Track.
OmniAI. 2025. OmniAI OCR Benchmark Re-
sults (February 2025). https://getomni.ai/
ocr-benchmark. Source code: https://github.
com/getomni-ai/benchmark.
Siru Ouyang, Jun Yan, Yanfei Chen, Rujun Han,
Zifeng Wang, Bhavana Dalvi Mishra, Rui Meng,
Chun-Liang Li, Yizhu Jiao, Kaiwen Zha, Maohao
Shen, Vishy Tirumalashetty, George Lee, Jiawei
Han, Tomas Pfister, and Chen-Yu Lee. 2026. Skil-
lOS: Learning skill curation for self-evolving agents.
arXiv preprint arXiv:2605.06614.
Phillipe R. Sampaio and Helene Maxcici. 2025.
Unsupervised document and template clustering
using multimodal embeddings.arXiv preprint
arXiv:2506.12116.
Xinyuan Wang, Chenxi Li, Zhen Wang, Fan Bai, Hao-
tian Luo, Jiayou Zhang, Nebojsa Jojic, Eric Xing, and
Zhiting Hu. 2024. PromptAgent: Strategic planning
with language models enables expert-level prompt op-
timization. InThe Twelfth International Conference
on Learning Representations.
Zilong Wang and Xiaoyu Shen. 2025. Hybrid OCR-
LLM framework for enterprise-scale document in-
formation extraction under copy-heavy task.arXiv
preprint arXiv:2510.10138.
Chengrun Yang, Xuezhi Wang, Yifeng Lu, Hanxiao
Liu, Quoc V . Le, Denny Zhou, and Xinyun Chen.
2024. Large language models as optimizers. In
The Twelfth International Conference on Learning
Representations.
Chang Oh Yoon, Wonbeen Lee, Seokhwan Jang, Kyu-
won Choi, Minsung Jung, and Daewoo Choi. 2024.
Language, OCR, form independent (LOFI) pipeline
for industrial document information extraction. In
Proceedings of the 2024 Conference on Empirical
Methods in Natural Language Processing: Industry
Track, pages 1056–1067, Miami, Florida, US. Asso-
ciation for Computational Linguistics.
Mert Yüksekgönül, Federico Bianchi, Joseph Boen,
Sheng Liu, Pan Lu, Zhi Huang, Carlos Guestrin,
and James Zou. 2025. Optimizing generative AI by
backpropagating language model feedback.Nature,
639(8055):609–616.
Boyang Zhang, Sebastián G. Acosta, Preston Carlson,
Sacha Bron, Pierre-Loïc Doulcet, Daniel B. Ospina,
and Simon Suo. 2026. ParseBench: A document
parsing benchmark for AI agents.arXiv preprint
arXiv:2604.08538.
Genghan Zhang, Shaowei Zhu, Anjiang Wei, Zhenyu
Song, Allen Nie, Zhen Jia, Nandita Vijaykumar,
Yida Wang, and Kunle Olukotun. 2025a. Ac-
celOpt: A self-improving LLM agentic system for
AI accelerator kernel optimization.arXiv preprint
arXiv:2511.15915. MLSys 2026.
Jiayi Zhang, Jinyu Xiang, Zhaoyang Yu, Fengwei Teng,
Xiong-Hui Chen, Jiaqi Chen, Mingchen Zhuge, Xin
Cheng, Sirui Hong, Jinlin Wang, Bingnan Zheng,
Bang Liu, Yuyu Luo, and Chenglin Wu. 2025b.
AFlow: Automating agentic workflow generation. In
The Thirteenth International Conference on Learning
Representations. ICLR 2025 Oral.
Qintong Zhang, Bin Wang, Victor Shea-Jay Huang, Jun-
yuan Zhang, Zhengren Wang, Hao Liang, Conghui
He, and Wentao Zhang. 2024. Document parsing
unveiled: Techniques, challenges, and prospects for
structured information extraction.arXiv preprint
arXiv:2410.21169.
Xuanhe Zhou, Guoliang Li, Zhaoyan Sun, Zhiyuan Liu,
Weize Chen, Jianming Wu, Jiesi Liu, Ruohang Feng,
and Guoyang Zeng. 2024. D-Bot: Database diagno-
sis system using large language models.Proceedings
of the VLDB Endowment, 17(10):2514–2527.

A Qualitative Analysis: Single Run Trace
We present a detailed trace of one optimization
run (Sonnet 4.6 for the agent LLM, skills + source
code, 50 iterations, 4h 55m) to illustrate the agent’s
decision-making process. The agent improved ac-
curacy from 28.5% to 85.2% (+56.7 pp) while re-
ducing cost per page by 21%.
A.1 Starting and Final Configurations
Starting configuration:All field descriptions
empty, generic extraction prompt, Claude Sonnet
4.6 as extraction model, no OCR, no few-shot ex-
amples. Achieves 28.5% accuracy at $0.047/page.
Final configuration (v42):Claude Haiku 4.5
with Textract LAYOUT OCR, domain-specific sys-
tem prompt, text-only extraction (no document im-
ages), 2 text-only few-shot examples, rich field
descriptions with column-label guidance. Achieves
85.2% at $0.038/page.
Key differences between starting configuration
→final configuration:
• Model:Sonnet 4.6 → Haiku 4.5 (cheaper,
sufficient with good prompts)
• OCR:Disabled → Textract LAYOUT (pro-
vides structured text)
• Modality:Multimodal (text+image) → Text-
only (images removed)
• Descriptions:Empty → Rich with column-
label guidance
• Few-shot:None → 2 complementary text-
only examples
• Prompts:Generic → Domain-specific with
verbatim extraction rules
A.2 Optimization Trajectory
Table 5 shows key milestones. The run naturally
divides into phases: bootstrap (model/OCR selec-
tion), field-level refinement, few-shot examples,
and a late-stage breakthrough when the agent dis-
covers that removing document images improves
accuracy.
A.3 Agent Trace: Selected Iterations
We highlight three iterations that illustrate different
aspects of the agent’s reasoning.
Iter Acc. Key Change∆
1 28.5% Baseline (empty config) —
2 58.4% Rich field descriptions +29.9
4 71.0% Haiku + LAYOUT OCR +12.6
15 73.9% Domain system prompt +2.9
19 74.8% 2 few-shot examples +0.9
35 77.2% Verbatim extraction rules +2.4
36 81.0% Remove document images +3.8
38 83.2% Column-label guidance +2.2
42 85.2% Description column labels +2.0
Table 5: Key milestones from a single 50-iteration opti-
mization run. ∆ shows improvement over the previous
milestone.
Iteration 2: Field descriptions (+29.9 pp).
Observation:LineItemDays at 15% — model ex-
tracting “1” (spots count) instead of day patterns.
LineItems truncated at 10 items on long docu-
ments.
Diagnosis:Empty field descriptions provide no
guidance; the model guesses field semantics from
names alone.
Action:Populate all 11 field descriptions with
rich context. For LineItemDays: “7-character
MTWTFSS pattern where each position is Y/N or
the day letter. Example: MTWTF--”.
Result:+29.9 pp overall. LineItemStartDate +50
pp, LineItemEndDate +58 pp, LineItemRate +50
pp.
Iteration 36: Removing document images (+3.8
pp).
Observation:Text-only Sonnet reference (v12)
achieved 76.2% vs. Haiku multimodal at 77.2%.
OCR text appears sufficient for tabular invoices.
Diagnosis:Document images may add noise for
structured tabular extraction — OCR text pro-
vides cleaner column-aligned signal.
Action:Remove {DOCUMENT_IMAGE} from task
prompt. Model receives only Textract OCR out-
put.
Result:+3.8 pp overall, false negatives halved
(88→45). The largest single improvement in the
run. Cost reduced 13% (no image tokens).
Iteration 38: Column-label guidance (+2.2 pp
with spillover).
Observation:LineItemEndDate regressed after re-
moving images — model confuses date columns
without visual layout cues.
Diagnosis:In text-only mode, the model needs
explicit column-name guidance to identify the cor-
rect fields.
Action:Add to LineItemEndDate description:
“Extract from columns labeled End Date, Thru,
Through, To, or End.”
Result:+2.2 pp overall — but improvement oc-
curred acrossallfields, not just EndDate. Column-
label guidance helped the model build a better
mental model of the table structure.
For example, the final LineItemEndDate field de-
scription (starting from an empty placeholder)
reads:

“The end date of the advertising spot airing. Ex-
tract from columns labeled ‘End Date’, ‘Thru’,
‘Through’, ‘To’, or ‘End’. Usually shown in
MM/DD/YY format. Return null if the invoice has
no separate end date column. If shown, extract
exactly as printed. ”
A.4 Notable Patterns
Several patterns were observed consistently
throughout this run:
• Null instructions cause cascade regression:
Any instruction telling the model “return null
when X” caused Haiku to over-generalize,
leading to false positive increases across un-
related fields. Confirmed 6 times across itera-
tions.
• Two few-shot examples is optimal:Three
examples always caused regression regardless
of content. Two complementary examples
(one with populated fields, one showing null
patterns) was the consistent optimum.
• Text-only examples suffice:Removing im-
ages from few-shot examples matched or im-
proved accuracy (+0.26 pp), suggesting struc-
tured text demonstrations are sufficient.
• Changes interact non-locally:Adding “ver-
batim” to the system prompt unexpectedly
halved LineItemDays false positives — a field
the instruction was not targeting.
B Context Management Details
A 50-iteration optimization trajectory accumulates
detailed metrics, tool outputs, and source document
images, far exceeding what any model can attend
to simultaneously. Before every model call, a hook
checks current token usage against a configurable
threshold expressed as a percentage of the model’s
context window. When exceeded, the system: (1)
summarizes older conversation history via a sep-
arate LLM call, producing structured bullet-point
summaries of past decisions, tool results, and key
findings; (2) preserves the most recent messages in-
tact, maintaining immediate working context; and
(3) re-injects the full optimization log, ensuring the
agent retains its complete decision history regard-
less of how many compaction cycles have occurred.
The threshold percentage trades information reten-
tion against context budget. In our experiments, all
runs would have exceeded the 1M-token context
window without compaction. At a 50% threshold,
compaction occurs roughly every 18 iterations with
minimal accuracy impact. At 10%, it fires approx-
imately 5 times per iteration, consuming the time
budget on summarization; affected runs complete
fewer than half their allotted iterations within the 8-
hour timeout. Thresholds of 30–60% are practical;
we use 50% throughout.
C Example Domain Skill
Each domain skill is a structured markdown doc-
ument retrieved by the agent on demand. Below
we present one representative skill (simplified for
exposition) that illustrates the format. Skills begin
with a Y AML header specifying the skill name and
a short description used for retrieval, followed by
sections defining when the skill applies, how to
diagnose the issue, and what configuration changes
to make.
C.1 Skill Header
---
name: visual-spatial-extraction-challenges
description: Document known challenges with fields
requiring complex visual parsing (checkboxes,
damage diagrams, spatial alignment) and provide
mitigation strategies within the current
architecture.
---
The header’s description field is used by the
agent’s skill retrieval mechanism to match observed
error patterns to relevant skills.
C.2 Skill: Visual-Spatial Extraction
Challenges
Trigger:Specific fields have very low accuracy
(<60%) while overall extraction performs well.
The failing fields involve visual elements: check-
boxes, spatial table alignment, or handwritten an-
notations.
Diagnosis:
1. Identify low-accuracy fields from per-field
evaluation metrics.
2. Inspect source documents to confirm the fail-
ing fields require spatial reasoning (e.g., distin-
guishing left-column vs. right-column check
marks in a grid).
3. Confirm the model is extractingwrongvalues
from adjacent visual elements (spatial confu-
sion) rather than extracting nothing (prompt
issue).

Resolution:Apply one or more mitigation strate-
gies in order of increasing cost:
1. Spatial prompts:Add highly specific loca-
tion instructions to the field description (e.g.,
“Look for a check mark to the LEFT of the
code value. Do NOT confuse with marks on
the RIGHT side of the same row.”).
2. Image resolution:Increase DPI and target
image dimensions to give the model better
visual input for spatial parsing.
3. Stronger model:Switch to a more capable
multimodal model for the extraction stage.
4. Exclude and flag:If accuracy remains unac-
ceptable, set the field’s evaluation weight to
zero and recommend human review for that
field.
C.3 Skill Format Summary
All 27 skills follow this same structure: a YAML
header (name + description for retrieval), followed
by trigger conditions, diagnostic steps, and ordered
resolution strategies. The key design properties
are:
• Self-contained:Each skill can be applied in-
dependently without reading other skills.
• Actionable:Resolution strategies include spe-
cific tool calls and configuration edits, not just
general advice.
• Observable triggers:Trigger conditions are
defined in terms of metrics the agent can di-
rectly observe (accuracy scores, error patterns,
output format).
• Ordered strategies:When multiple fixes ex-
ist, they are ordered by cost or invasiveness,
allowing the agent to try the least disruptive
option first.
C.4 Reproducibility
The benchmark datasets underlying our reported re-
sults are publicly available: RealKIE FCC-Verified
for extraction, and the classification and splitting
benchmarks cited in Section 5.5. The evaluation
protocol is specified in Section 4, including the
eval/test split and the exact-match scoring criteria,
so the accuracy numbers we report are reproducible
by anyone with a comparable configurable pipeline.
The domain skills themselves are proprietary.
They encode diagnostic knowledge from customer
engagements and cannot be released in full, which
is why we provide one representative skill above in
complete form rather than the whole library. The
format is fully specified, and the skills are the kind
of artifact a practitioner would author from their
own engagement experience rather than reuse ver-
batim from ours; we consider the format and the
authoring process, not the specific 27 documents, to
be the transferable contribution. The pipeline being
optimized is likewise an internal production system,
so the specific configuration space in Section 3.2 is
not reproducible verbatim, though the method re-
quires only that some configurable pipeline expose
an equivalent surface.
D Extended Related Work
Intelligent Document Processing.IDP has
evolved from template-based systems to LLM-
powered pipelines combining OCR, layout anal-
ysis, and generative models (Zhang et al., 2024;
Fang et al., 2025; Kim et al., 2022). Recent work
addresses specific pipeline challenges: flexible ex-
traction architectures (Yoon et al., 2024), multi-
document packet splitting (Islam et al., 2026a),
hybrid OCR-LLM strategies for enterprise-scale
throughput (Wang and Shen, 2025), adaptive agents
for regulatory documents (Colakoglu et al., 2025),
unsupervised template discovery via multimodal
embeddings (Sampaio and Maxcici, 2025), and
evaluation benchmarks for agentic parsing (Zhang
et al., 2026). While these works advance indi-
vidual components or adaptation methods, none
address the joint optimization of an entire IDP
pipeline configuration (prompts, models, OCR set-
tings, schemas, and parameters), which we perform
with our solution.
LLM Agents for System Optimization.A grow-
ing body of work applies LLM agents to closed-
loop optimization. OPRO (Yang et al., 2024) for-
malizes the pattern as iterative solution genera-
tion conditioned on past (solution, score) pairs;
TextGrad (Yüksekgönül et al., 2025) generalizes it
by backpropagating textual feedback through com-
pound AI system graphs. This pattern has been
applied to database tuning (Zhou et al., 2024; Lin
et al., 2025), AutoML pipeline search via MCTS
(Chi et al., 2024), prompt optimization (Wang
et al., 2024), agentic workflow generation (Zhang
et al., 2025b), hardware kernel optimization with

experience memory (Zhang et al., 2025a), and au-
tonomous LLM fine-tuning (Li et al., 2026). Our
work shares this closed-loop pattern but operates
over a configuration space that is broader than any
single prior work, requiring simultaneous modi-
fication of natural language prompts, categorical
model choices, continuous parameters, structural
pipeline decisions, and JSON schemas.
Domain Knowledge in LLM Agents.Injecting
structured expert knowledge into agents improves
both accuracy and efficiency. DSPy (Khattab et al.,
2024) encodes task structure as compilable pipeline
specifications. SkillForge (Liu et al., 2026) it-
eratively refines domain skills for cloud support
through failure diagnosis. SkillOS (Ouyang et al.,
2026) manages skills as structured files in an OS-
like repository, achieving performance gains with
fewer interaction steps. Our domain skills follow a
similar paradigm: self-contained knowledge mod-
ules that the agent retrieves on demand for specific
IDP failure patterns, but authored by human experts
from production engagements rather than automat-
ically generated.
