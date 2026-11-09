---
title: 'EGI-BENCH: An Enterprise General Intelligence Benchmark Suite'
url: https://arxiv.org/abs/2610.27234
category: ai-marketing
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Zhiwei Liu
- Zhujun Lan
- Jielin Qiu
- Zixiang Chen
- Liangwei Yang
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.27234
pages: 15
chars: 55063
fetched_at: '2026-11-08T13:34:22+00:00'
kb_version: 1
---

# EGI-BENCH: An Enterprise General Intelligence Benchmark Suite

Salesforce AI Research2026-06-15
EGI-BENCH: An Enterprise General Intelligence Benchmark Suite
Zhiwei Liu∗, Zhujun Lan ∗, Jielin Qiu, Zixiang Chen, Liangwei Yang,
Ming Zhu, Akshara Prabhakar, Wenting Zhao, John Emmons, Jason Wu,
Shafiq Rayhan Joty, Junnan Li, Shelby Heinecke, Silvio Savarese, Huan Wang †
Salesforce AI Research
Abstract
Enterprise adoption of LLMs in agentic workflows is gated by evaluations that span a wide arc of
abilities: CRM operations, heterogeneous-document retrieval, personal data understanding, multi-turn
planning, tool use, function calling, long-horizon research, and long-context software engineering.
These evaluations live today in separate repositories with divergent runners, dependencies, and
scoring conventions, which makes cross-benchmark comparison difficult and obscures what a single
aggregate number actually represents. We release EGI-BENCH, a unified LLM agent benchmark suite
that consolidates eight enterprise-facing agent benchmarks (CRMARENA, HERB, PERSONABENCH,
USERBENCH, MCP-UNIVERSE, MCPEVAL, BENCHFORCE, LOCOBENCH) behind a single
command-line interface with two runtime-budgeted execution modes. On top of the suite we define the
Enterprise General Intelligence(EGI) Score, a six-dimensional framework (M 1–M6) whose buckets
are populated byfine-grained sub-metricsrouted from each benchmark rather than by benchmark-
level averages. We describe the suite, the sub-metric routing, and the quick/deep budgets, and report
results for fourteen frontier and cost-efficient LLMs spanning the GPT, Claude, and Gemini families
under quick mode. Top-line EGI ranges from 39.6 (GPT-4o mini) to 65.6 (gpt-5.5), and no
single model dominates every capability axis: gpt-5.5 leads task outcome, planning, and retrieval
grounding; Claude Sonnet 4.5 leads tool actioning and safety/abstention; and Claude Haiku 4.5 leads
engineering quality. Code is available at https://github.com/SalesforceAIResearch/egi-bench.
1 Introduction
Large language models are now deployed inside agentic systems that plan, use tools, and act inside real software
environments [14, 17, 21]. In the enterprise, these systems answer customer-support tickets, search internal documents,
navigate CRM objects, plan travel, invoke business APIs, and maintain large codebases. For any given deployment, the
question a release-gating team asks is whether the underlying LLM isreadyfor these workflows: can it produce correct
business outcomes, call tools reliably, plan efficiently, ground answers in retrieved evidence, abstain when appropriate,
and produce artifacts of acceptable engineering quality? Answering that question requires many signals at once, and no
single benchmark captures all of them. EGI-BENCHmeasures the LLM that drives these workflows; each contributing
benchmark exercises it through its own native scaffold (ReAct loops, multi-turn dialog, function-calling harnesses), and
the resulting EGI score is therefore a model-level signal across enterprise-shaped tasks.
Despite this demand, existing benchmarks each cover a narrow slice of the space. The agent-evaluation literature
has grown rapidly but is fragmented along capability lines. AGENTBENCH[ 8] and AGENTBOARD[ 11] evaluate
general agentic behavior across heterogeneous environments; GAIA [12] targets general AI-assistant questions with
verifiable answers. SWE-BENCH[ 6] focuses on resolving real-world GitHub issues; WEBARENA[ 23] places agents
inside a realistic web environment. TOOLLLM [ 14], the Berkeley Function Calling Leaderboard [20], and MINT [ 19]
probe tool use and multi-turn tool-augmented interaction; τ-bench [22] measures tool-agent-user dialog in realistic
domains. Holistic LLM evaluations such as HELM [ 7] aggregate scores across many tasks but are not agent-centric. In
the enterprise setting specifically, recent benchmarks cover CRM workflows [4, 5], deep search over heterogeneous
enterprise data [3], personalized QA over private user data [18], multi-turn user-facing dialog [13], function calling [16],
MCP-based tool use [9, 10], and long-context software engineering [15]. Each of these benchmarks lives in its own
repository, with its own runner, dependencies, and scoring conventions.
Because these benchmarks live in separate repositories with divergent runners and scoring conventions, a practitioner
who wants a single EGI signal today must run many tools, reconcile their outputs by hand, and decide how to weigh
∗Equal contribution.
†Corresponding author:huan.wang@salesforce.com.
1
arXiv:2610.27234v1  [cs.AI]  19 Oct 2026

Salesforce AI Research2026-06-15
them. Naively averaging each benchmark’s reported overall score dilutes signal: a benchmark that internally averages
nine sub-scores contributes one number, while a benchmark with a single sub-metric contributes the same one number.
Worse, each benchmark’s “overall” collapses sub-metrics that probe very different capabilities (e.g. policy-violation
detection vs. named-entity disambiguation inside CRMARENA[ 4]). The result is that existing leaderboards cannot
answer capability-grounded questions like “is this model safe enough to ship?” or “does it plan multi-step workflows
reliably?”. Table 1 makes this gap concrete: the four most prominent agent-benchmark reference points each cover only
a strict subset of the six EGI dimensions we argue are needed for release decisions. This is the gap EGI-BENCHfills.
Contributions.
This report describes EGI-BENCH, a unified LLM agent benchmark suite and scoring framework for enterprise-shaped
tasks. Our contributions are:
• Unified suite.We consolidate eight enterprise-facing LLM agent benchmarks [ 3, 4, 9, 10, 13, 15, 16, 18] into one
repository behind the egi-bench CLI, with per-benchmark virtual environments, a shared LiteLLM model-routing
proxy, and a single run -model ... -mode {quick,deep} entry point. Each benchmark retains its own
scaffold (ReAct, MCP client, multi-turn dialog, etc.); the unit of evaluation is the LLM.
• Fine-grained sub-metric routing.Rather than averaging benchmark-level scores, we routeindividual sub-metrics
into a six-dimensional EGI framework (M 1–M6) that captures task-outcome accuracy, tool actioning, planning,
retrieval grounding, safety/abstention, and engineering quality. The routing is declarative and auditable (Appendix C).
• Runtime-budgeted modes.Quick mode targets ≤180 min total wall-clock; deep mode targets ∼12 h. Which
categories or tasks get subsetted is determined by a per-benchmark runtime budget rather than by hand-picked
coverage.
•Open release with a fourteen-model benchmark.We release the suite, configuration, and full quick-mode results
across fourteen frontier and cost-efficient LLMs spanning the GPT, Claude, and Gemini model families. The results
expose capability-level specialization that is invisible in any single benchmark’s overall score.
The rest of the report surveys related evaluation work (Section 2), positions EGI-BENCHagainst comparable benchmarks
(Section 3), defines the M1–M6 framework and the eight benchmark contributors (Section 4), reports results and analysis
(Sections 5–6), and lists limitations (Section 7). The sub-metric routing table and execution-mode details are deferred
to Appendices C and E.
2 Related Work
We situate EGI-BENCHrelative to four lines of work: holistic LLM evaluations, general agent benchmarks, tool-use
and function-calling benchmarks, and enterprise-facing agent benchmarks.
Holistic LLM evaluations.
HELM [ 7] proposed a multi-metric view of language-model evaluation, separating accuracy, robustness, calibration,
and other axes across many tasks. While HELM is primarily task-level rather than agent-level, it established the
principle that a single benchmark should exposemultiple interpretable dimensions. EGI-BENCHadopts the same spirit
but applies it to LLM evaluation in enterprise agentic workflows by defining six enterprise-relevant dimensions (M1–M6)
and routing each contributing benchmark’s native sub-metrics into them, rather than averaging benchmark-level scores.
General agent benchmarks.
AGENTBENCH[ 8] evaluates LLM agents across eight heterogeneous environments (code, games, web, reasoning, etc.)
and reports per-environment success rate with an overall average; it does not expose a cross-environment capability
decomposition, so planning, tool use, and abstention collapse into a single scalar per environment. AGENTBOARD[ 11]
introducesprogress rate, a fine-grained mid-trajectory metric across nine environments — the closest prior art to our
“don’t just report the final number” philosophy, but operating within a single benchmark family rather than composing
across independently authored benchmarks. GAIA [ 12] benchmarks general AI-assistant questions with verifiable
ground truth and public/private test sets; the only axis of decomposition is its three-level difficulty partition (Level 1–3),
and a failed web-search step and a failed arithmetic step are indistinguishable in the scored output. WEBARENA[ 23]
places agents in a realistic, self-hosted web environment with full interaction traces and reports end-to-end task
success. These benchmarks target breadth of capability, not enterprise readiness: none of them decomposes scores into
enterprise-interpretable buckets such as safety/abstention or engineering quality, and none composes signals across
independently authored benchmark families.
2

Salesforce AI Research2026-06-15
Tool-use and function-calling benchmarks.
TOOLLLM [ 14] introduced ToolBench with 16,000+ real-world APIs and trained a tool-augmented LLM; its headline
metric is a pass-rate-with-retries aggregated across APIs. The Berkeley Function Calling Leaderboard (BFCL) [20]
standardizes evaluation of function calling across API families and provides the most fine-grained tool-use report to
date: AST vs. executable evaluation, simple / multiple / parallel / parallel-multiple settings, multi-turn and multi-step
categories, language axes (Python, REST, SQL, Java, JavaScript), Function Relevance Detection (an explicit abstention
test in which the correct response to an irrelevant toolset is to call nothing), and cost-per-1000-calls with latency as first-
class signals. BFCL’s taxonomy on the tool-calling axis is stronger than what EGI-BENCH’s MCP contributors currently
surface; EGI-BENCH’s advantage is the enterprise context that surrounds the tool calls, not the tool-calling depth itself.
MINT [ 19] measures multi-turn interaction with tools under language feedback, reporting success atk tool calls and tool-
type breakdowns. τ-bench [22] and its dual-control follow-on τ 2-bench [2] target tool-agent-user interaction in realistic
retail, airline, and (in τ 2) telecom domains, with passk (k up to 8) as the headline metric plus an auto error-identification
pipeline that classifies failures by fault assignment (agent / user / environment) and fault type (used_wrong_tool,
used_wrong_tool_argument,took_unintended_action,goal_partially_completed).
This multi-trial reliability signal is missing from EGI-BENCHv1 and is concrete future work. Within EGI-BENCH,
tool-use signals come from MCP-UNIVERSE[ 10] and MCPEVAL[ 9], which instantiate the Model Context Protocol [1]
server/agent contract, while BENCHFORCE[ 16] complements these with WebSocket-driven enterprise function-calling
environments. Where prior tool-use benchmarks expose a single success rate, EGI-BENCHroutes the component
metrics (tool-name match, parameter match, ordering, strict vs. flexible success) into separate enterprise buckets so that
drift, over-action, and planning-order errors are surfaced independently.
Code and long-context benchmarks.
SWE-BENCH[ 6] evaluates whether LLMs can resolve real-world GitHub issues in 12 Python repositories using unit
tests as verifiers; its per-instance pipeline surfaces four signals (applied / tests-pass / regression / resolved), with the
headline leaderboard reporting the resolve rate. Hidden-test ground truth certified by the original issue authors makes
SWE-bench the stronger instrument for pure coding correctness, but it does not measure code quality, patch-size
minimization, planning or search behavior separate from the final patch, or tool-call efficiency. LOCOBENCH[ 15]
extends software-engineering evaluation to long-context scenarios spanning ten programming languages and context
lengths up to ∼1M tokens, using a four-dimensional rubric (functional correctness, software engineering excellence,
code quality, long-context utilization). EGI-BENCHuses LOCOBENCHas its software-engineering contributor and
routes its four dimensions into M 1, M 3, and M 6; the rubric is softer than SWE-bench’s hidden tests, which we
acknowledge as a trade-off.
Enterprise-facing agent benchmarks.
A newer wave of benchmarks targets enterprise workflows specifically. CRMARENA[ 4, 5] evaluates Salesforce-style
CRM operations (case routing, analytical queries, policy-violation detection) against a sandbox org. HERB [ 3]
benchmarks multi-hop retrieval over realistic, heterogeneous enterprise corpora (documents, Slack, meeting transcripts,
URLs) and mixes answerable and unanswerable queries to test anti-hallucination. PERSONABENCH[ 18] measures
personalized QA over synthetic private user data with controllable noise injection. USERBENCH[ 13] exercises multi-
turn travel-planning dialog with user-preference satisfaction as the reward signal. Each of these benchmarks is valuable
on its own; what is missing is a principled way to read themtogetheras an EGI signal.
Cross-domain aggregation.
Prior practice aggregates cross-benchmark signal either by picking a headline benchmark per capability or by averaging
benchmark-level overall scores. Both lose information. EGI-BENCHinstead routes individual sub-metrics into the
M1–M6 framework (Appendix C), preserves per-benchmark sub-scores for diagnosis (Section 5), and optionally applies
release-gate floors on M5 (safety/abstention) and M2 (tool actioning) so that a single aggregate number cannot hide a
capability regression that matters for deployment.
3 Benchmark Comparison and Positioning
We position EGI-BENCHagainst four representative open-source agent/LLM benchmarks: τ 2-bench [2] (the dual-
control follow-on to the original τ-bench [22]), SWE-bench [ 6], GAIA [ 12], and the Berkeley Function Calling
3

Salesforce AI Research2026-06-15
Table 1:Domain coverage, task count, and M 1–M6 enterprise-metric coverage across representative agent/LLM
benchmarks. ✓ = the benchmark evaluates this dimension as a core part of its design; ∼ = exercised as part of tasks but
not a primary axis;✗= outside scope.
EGI-BENCHτ 2-bench SWE-bench GAIA BFCL
Domains 8 benchmarks;∼20
sub-domains
3 domains
(dual-control): retail,
airline, telecom
1 domain: SWE
(Python)
1 domain:
generalist
1 domain: function
calling
Tasks∼1,500+ a few hundred /
domain
2,294 / 500 / 300∼466∼2,000
M1 Task Outcome✓ ✓ ✓ ✓ ✓
M2 Tool Actioning✓ ✓∼ ∼✓
M3 Planning✓ ✓∼✓ ✓
M4 Retr./Grounding✓∼ ∼✓∼
M5 Safety/Abstention✓ ✓ ✗ ✗ ✓
M6 Engineering✓ ✗ ✓ ✗ ✗
# M-dimensions (✓) 64 2 3 4
Leaderboard (BFCL) [20]. The head-to-head coverage matrix is shown in Table 1; here we discuss the trade-offs the
matrix encodes.
Each of the four comparison benchmarks is a strong instrument on a narrow subset of axes: τ 2-bench on dialog
reliability and passk-style multi-trial correctness with a dual-control user simulator, SWE-bench on code-resolution
correctness with hidden-test ground truth, GAIA on multi-step generalist-assistant tasks, and BFCL on tool-calling
taxonomy and cost/latency telemetry. EGI-BENCH’s contribution is not to beat any of them on its home axis but tocover
all sixEGI dimensions through a composition of eight independently authored benchmarks, route their sub-metrics into
a shared frame (Appendix C), and add release-gate semantics via configurable M5 and M2 floors. Practitioners who
need the maximum-rigor instrument on a single axis should continue to use the specialist benchmark; practitioners who
need a capability-grounded readiness score for an enterprise deployment should use EGI-BENCH.
4 The EGI Framework
We evaluate LLMs along six enterprise-level metrics and combine them into a single EGI score. The metrics, definitions,
and weights are summarized in Table 2.
Table 2:The six enterprise metrics (M1–M6) and their weights in the EGI score. Weights are inherited from the internal
PR #28 proposal and are applied uniformly across the suite.
Metric Weight What it measures
M1 Task Outcome Accuracy 28% Did the agent produce the correct business outcome or final answer?
M2 Tool Actioning Reliability 22% Correct tool selection, parameters, ordering; no extraneous calls.
M3 Planning & Workflow 16% Multi-step and multi-turn execution that is step-efficient.
M4 Retrieval & Evidence Grounding 14% Grounded answers, correct citations, effective context use.
M5 Safety, Abstention & Policy 14% Abstain when appropriate, flag policy violations, no unsafe actions.
M6 Engineering & Maintainability 6% Code quality and structural/process discipline.
EGI= 0.28M 1 + 0.22M2 + 0.16M3 + 0.14M4 + 0.14M5 + 0.06M6
These six metrics capture capabilities that enterprise stakeholders evaluate independently: M 1 asks “did the agent
produce the correct answer?”; M 2 asks “did it use tools correctly?”; M 3 asks “did it plan efficiently across steps
and turns?”; M 4 asks “are its answers grounded in retrieved evidence?”; M 5 asks “does it abstain and obey policy
when it should?”; and M 6 asks “is the artifact it produced of acceptable engineering quality?”. The weights
0.28/0.22/0.16/0.14/0.14/0.06 bias the score toward the outcomes that matter most in production deployments
(task accuracy and tool reliability) while keeping a non-trivial safety floor. Each metric is computed over the outputs the
LLM produces inside the contributing benchmark’s native scaffold.
4

Salesforce AI Research2026-06-15
To compute EGI, each sub-metric is first normalized to [0,100] ; lower-is-better sub-metrics (e.g. step counts in MCP-
UNIVERSE) are clipped against a stable ceiling and inverted. For each bucket Mk, its score is the (equal-weighted by
default) mean of the normalized sub-metrics routed into it. The aggregate is then
EGI= 0.28M 1 + 0.22M2 + 0.16M3
+ 0.14M4 + 0.14M5 + 0.06M6.
When a sub-metric is missing (e.g. a benchmark run failed), we reweight the remaining sub-metricswithinthat bucket
only; we never globally reweight across M 1–M6. If an entire benchmark is missing, all sub-metrics it contributes
are skipped and affected buckets are renormalized locally. This keeps buckets comparable while signalling missing
coverage honestly.
Beyond the aggregate, M5 (safety/abstention) and M2 (tool actioning) can optionally gate release: if either drops below
a configurable threshold (default 70), the run is flaggednot release-readyregardless of EGI. Release-gate floors are
reported alongside EGI but do not modify the score itself. For the routing to be well-posed, every benchmark must
contribute to at least one bucket and every bucket must be populated by at least two routed sub-metrics. M 6 draws
both of its sub-metrics (software_engineering, code_quality) from a single benchmark (LOCOBENCH);
all other buckets receive sub-metrics from three or more benchmarks. The full coverage view is deferred to Appendix B,
Table 5, and the sub-metric routing is described in Appendix C.
The eight benchmarks that populate M1–M6 are: CRMARENA[4, 5] for Salesforce CRM operations (nine task types,
including policy violation and knowledge QA); HERB [ 3] for deep search over heterogeneous enterprise data with
answerable/unanswerable splits; PERSONABENCH[ 18] for personalized QA over synthetic private user data under
controllable noise; USERBENCH[ 13] for multi-turn travel-planning dialog with a 20-turn budget; MCP-UNIVERSE[ 10]
for Model Context Protocol [1] tool use across six server ecosystems under a ReAct agent; MCPEVAL[ 9] for auto-
synthesized tool-call tasks with strict/flexible matching; BENCHFORCE[ 16] for enterprise function calling (hospital,
HR, order-management); and LOCOBENCH[ 15] for long-context software engineering across ten languages at context
lengths up to 1 M tokens. Appendix B reports per-benchmark task counts under quick and deep modes.
5 Results
Table 3 reports EGI and its M 1–M6 constituents for fourteen frontier and cost-efficient LLMs under quick mode.
Figure 1 compares all fourteen models on each M 1–M6 dimension as grouped bars, and Figure 2 renders the same
matrix as a heatmap so per-model specialization patterns are visible at a glance.
Across the fourteen models, gpt-5.5 leads on overall EGI (65.61), driven by best-in-class M1 (Task Outcome, 82.95),
M3 (Planning, 30.89), and M4 (Retrieval & Grounding, 54.86). Claude Sonnet 4.5 sits a hair behind at EGI 65.25
and tops M2 (Tool Actioning, 87.17) and M5 (Safety & Abstention, 80.28) – the only safety score above 76 in the
roster. Gemini 3.1 Pro Preview and Claude Opus 4.5 round out the top tier at EGI 63.51 and 63.31, with Gemini 3.1’s
strong M1 of 78.45 second only to gpt-5.5. The most striking specialization signal sits at rank 6: Claude Haiku 4.5’s
M6 (Engineering Quality, 61.28) is column-best in the entire roster despite its mid-pack EGI. The cost-efficient tier
(GPT-4o mini, GPT-5 nano, Gemini 2.0/2.5 Flash) trails the frontier tier on EGI by roughly6–26 points, with the GPT-5
mini / Gemini 2.5 Flash boundary a near-tie at 51.91 vs 51.36. M3 is uniformly the weakest dimension (16–31 across
all fourteen models), driven by USERBENCH’s low per-environment reward, indicating multi-turn planning remains an
open frontier. The heatmap in Figure 2 makes these per-row/per-column patterns directly visible: hot cells flag weak
scores and cool cells mark strong ones, so M3 forms a uniformly hot column and M2 a uniformly cool one, while the
coolest cell in each row marks the model’s strongest dimension.
6 Analysis
Figure 3 overlays the top six models on M1–M6 as a radar chart, which makes the capability-level specializations visible
at a glance. Three observations follow.
First, top-line EGI hides meaningful capability-level specialization. gpt-5.5 wins overall but is only third on M2
(tool actioning, 79.56) and fifth on M5 (safety & abstention, 63.47); Claude Sonnet 4.5, second overall by just 0.36
EGI points, has the strongest tool-actioning and safety profile ( 87.17 on M2 and 80.28 on M5, the only safety score
above 76). The strongest specialization signal sits below the top tier: Claude Haiku 4.5’s M 6 (Engineering Quality,
61.28) is the column-best in the entire roster, edging every frontier model from rank 6. This is precisely the kind of
decision the scalar EGI cannot surface on its own and that the M 1–M6 decomposition was designed to expose.
5

Salesforce AI Research2026-06-15
Table 3:Main results: EGI score and its M 1–M6 constituents across fourteen frontier and cost-efficient LLMs under
quick mode. Rows sorted by EGI. Scores are 0–100; higher is better. Bold = column best.
Model Mode EGI M 1 M2 M3 M4 M5 M6
gpt-5.5quick65.61 82.9579.5630.89 54.8663.47 56.23
Claude Sonnet 4.5 quick 65.25 69.8987.1727.48 53.0480.2857.34
Gemini 3.1 Pro Prev. quick 63.51 78.45 76.82 19.57 54.43 75.56 55.30
Claude Opus 4.5 quick 63.31 74.29 75.58 27.95 52.08 75.56 58.98
GPT-4o quick 59.38 66.18 84.22 23.88 39.47 53.61 51.95
Claude Haiku 4.5 quick 59.13 69.02 73.98 24.05 48.61 65.6961.28
Gemini 2.5 Pro quick 59.10 76.05 65.60 27.16 50.58 60.83 57.25
GPT-4.1 quick 58.31 69.88 81.60 27.36 44.99 49.03 54.19
GPT-5 mini quick 51.91 59.10 67.74 21.75 43.05 54.17 56.12
Gemini 2.5 Flash quick 51.36 59.25 64.10 24.72 40.99 54.58 55.48
Claude 3.5 Haiku quick 50.78 48.16 75.81 18.39 44.35 58.61 54.36
Gemini 2.0 Flash quick 49.29 48.57 72.53 20.65 42.54 51.67 53.96
GPT-5 nano quick 45.14 42.38 72.05 15.68 43.31 41.25 51.25
GPT-4o mini quick 39.56 30.91 64.45 16.66 39.33 39.17 51.14
M1
Task
Outcome
M2
Tool
Actioning
M3
Planning
M4
Retr. &
Ground.
M5
Safety &
Abst.
M6
Eng.
Quality
0
20
40
60
80
100Score (0 100)
GPT-5.5
Claude Sonnet 4.5
Gemini 3.1 Pro Prev.
Claude Opus 4.5
GPT-4o
Claude Haiku 4.5
Gemini 2.5 Pro
GPT-4.1
GPT-5 mini
Gemini 2.5 Flash
Claude 3.5 Haiku
Gemini 2.0 Flash
GPT-5 nano
GPT-4o mini
Figure 1:M 1–M6 scores across fourteen LLMs under quick mode. Models are ordered by EGI; each bucket is a cluster
of bars. The M3 (Planning) dimension is uniformly low across models, while M2 (Tool Actioning) is the strongest axis
for nearly every frontier model. The best M2 (Tool Actioning, 87.17) and M5 (Safety & Abstention, 80.28) are held by
Claude Sonnet 4.5, while the best M1 (Task Outcome, 82.95), M3 (Planning, 30.89), and M4 (Retrieval & Grounding,
54.86) are all held bygpt-5.5, illustrating that top-line EGI can mask capability-level specialization.
Second, two axes have consistent frontier limits across all fourteen models. M3 (planning/workflow orchestration) tops
out at 30.89 (gpt-5.5) and is below 25 for nine of fourteen models, driven almost entirely by USERBENCH’s low
micro-average reward (no model exceeds 29 on its travel envs; most cluster in the 10–22 range). The low absolute
numbers are not a scoring artifact: USERBENCH’s micro_avg averages the per-turn reward acrosseveryturn of an
episode rather than scoring only the final answer, so a model that wanders through ten turns of generic chat before
eventually recommending the correct itinerary scores substantially below one that asks a single clarifying question and
resolves the task in three turns – even though both end with the correct answer. This is precisely the step-efficiency
signal M3 is designed to measure, so the low scores reflect a genuine finding rather than a quirk of how the metric is
constructed: no frontier model today is consistently turn-efficient in multi-turn user-alignment tasks. Long-horizon
user-preference planning therefore remains an open frontier; current LLMs do not yet saturate the multi-turn travel
scenario. By contrast M6 (engineering quality) is compressed into a 51–61 band, because its two routed sub-metrics
(LOCOBENCH’s software_engineering and code_quality) are saturated LLM-judged rubrics that reward
coherent output over strict correctness.
6

Salesforce AI Research2026-06-15
M1
Task
Outcome
M2
Tool
Actioning
M3
Planning
M4
Retr. &
Ground.
M5
Safety &
Abst.
M6
Eng.
Quality
GPT-5.5
Claude Sonnet 4.5
Gemini 3.1 Pro Prev.
Claude Opus 4.5
GPT-4o
Claude Haiku 4.5
Gemini 2.5 Pro
GPT-4.1
GPT-5 mini
Gemini 2.5 Flash
Claude 3.5 Haiku
Gemini 2.0 Flash
GPT-5 nano
GPT-4o mini
83 80 31 55 63 56
70 87 27 53 80 57
78 77 20 54 76 55
74 76 28 52 76 59
66 84 24 39 54 52
69 74 24 49 66 61
76 66 27 51 61 57
70 82 27 45 49 54
59 68 22 43 54 56
59 64 25 41 55 55
48 76 18 44 59 54
49 73 21 43 52 54
42 72 16 43 41 51
31 64 17 39 39 51
0
20
40
60
80
100
score
Figure 2:M 1–M6 score matrix (14 models × 6 metrics),
sorted by EGI. Hot cells flag weak scores, while cool cells
mark strong performance. M 3 (Planning) is therefore
the hottest column, since no model surpasses 31; M 2
(Tool Actioning) is the coolest, with most frontier models
performing above 70. Within each row, the coolest
cell identifies that model’s strongest dimension (e.g.
gpt-5.5 is coolest on M 1, Claude Sonnet 4.5 on M 2
and M5, and Claude Haiku 4.5 holds the column-best on
M6).
M1
Task
Outcome
M2
Tool
Actioning
M3
Planning
M4
Retr. &
Ground.
M5
Safety &
Abst.
M6
Eng.
Quality
20
40
60
80
100
GPT-5.5
Claude Sonnet 4.5
Gemini 3.1 Pro Prev.
Claude Opus 4.5
GPT-4o
Claude Haiku 4.5
Figure 3:M 1–M6 profiles of the top six models by
EGI. No single model dominates every axis: gpt-5.5
leads on task outcome (M1), planning (M3), and retrieval
grounding (M4); Claude Sonnet 4.5 on tool actioning (M2)
and safety and abstention (M5); and Claude Haiku 4.5 on
engineering quality (M6).
Third, the cost/capability boundary is fuzzier than parameter count alone suggests. Gemini 2.5 Pro reaches EGI 59.10 –
virtually tied with GPT-4o (59.38) and Claude Haiku 4.5 (59.13) – powered by an M1 of 76.05 that beats every other
cost-tier model and lands within 7 points of gpt-5.5. At the lower frontier edge, GPT-5 mini and Gemini 2.5 Flash
are a near-tie at EGI 51.91 vs 51.36, with GPT-5 mini’s stronger M5 (54.17) and M6 (56.12) offsetting Gemini 2.5
Flash’s higher M3 (24.72). At the smallest tier, GPT-5 nano holds the lowest-in-roster M3 (15.68) and a near-floor M1
(42.38) that leave it second-from-last on overall EGI despite a competitive M2 (72.05). The M1–M6 decomposition
therefore exposeswhichcapability lets a smaller model close the gap, rather than onlywhetherit does.
7 Limitations
We note four limitations of this release. First, quick mode subsets CRMARENA, HERB, USERBENCH, MCP-
UNIVERSE, MCPEVAL, BENCHFORCE, and LOCOBENCHto fit inside the 180-minute budget, so sub-metric averages
are computed over fewer items and have wider confidence intervals. Readers should therefore treat quick-mode EGI as a
directional indicator and rely on deep-mode runs for release decisions. Second, the 28/22/16/14/14/6 weighting over
M1–M6 is based on expert judgment and has not yet been empirically recalibrated on EGI-BENCH; a calibration study
that fits the weights to observed enterprise risk (e.g., deployment incident rates correlated with sub-metric patterns) is
future work. Third, EGI is a scalar, and any single scalar over diverse capabilities compresses information. Fourth,
parts of MCP-UNIVERSE’s evaluator use LLM-based grading via the configurable EVALUATOR_MODEL, and judge
choice and judge drift can shift absolute numbers across runs even when the evaluated LLM is identical. We fix the
judge model in configuration so that comparisons within a release are stable, but cross-release comparisons should note
the judge version.
7

Salesforce AI Research2026-06-15
8 Conclusion
EGI-BENCHunifies eight enterprise-facing LLM agent benchmarks behind a single CLI and introduces a sub-metric-
level routing framework (M 1–M6) that produces an interpretable EGI score without collapsing capability-specific
signal. The unit of evaluation is the LLM: each contributing benchmark exercises the model through its own native
scaffold (ReAct, MCP client, multi-turn dialog, function-calling harness). Runtime-budgeted quick and deep modes
make the suite tractable both for smoke tests and for release evaluations. We release the suite, configuration, and
full quick-mode results across fourteen frontier and cost-efficient LLMs spanning the GPT, Claude, and Gemini
families (Table 3). The results expose capability-level specialization that is invisible in any single benchmark’s overall
score: gpt-5.5 leads EGI and sweeps M 1, M 3, and M 4, but Claude Sonnet 4.5 holds the column-best on M 2
and M5, and Claude Haiku 4.5 – ranked sixth on EGI – holds the column-best on M 6. The source is available at
https://github.com/SalesforceAIResearch/egi-bench; we invite extensions to the benchmark roster and contributions to
the routing table.
References
[1] Anthropic. Model context protocol specification. https://modelcontextprotocol.io, 2024. Accessed 2026-04-29.
[2] Victor Barres, Honghua Dong, Soham Ray, Xujie Si, and Karthik Narasimhan. τ 2-bench: Evaluating conversational agents in a
dual-control environment.arXiv preprint arXiv:2506.07982, 2025. URL https://arxiv.org/abs/2506.07982.
[3] Prafulla Kumar Choubey, Xiangyu Peng, Shilpa Bhagavath, Kung-Hsiang Huang, Caiming Xiong, and Chien-Sheng Wu.
Benchmarking deep search over heterogeneous enterprise data.arXiv preprint arXiv:2506.23139, 2025. URL https://arxiv .org/
abs/2506.23139.
[4] Kung-Hsiang Huang, Akshara Prabhakar, Sidharth Dhawan, Yixin Mao, Huan Wang, Silvio Savarese, Caiming Xiong, Philippe
Laban, and Chien-Sheng Wu. CRMArena: Understanding the capacity of LLM agents to perform professional CRM tasks in
realistic environments. InProceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for
Computational Linguistics: Human Language Technologies (NAACL-HLT), 2025. URL https://arxiv.org/abs/2411.02305.
[5] Kung-Hsiang Huang, Akshara Prabhakar, Onkar Thorat, Divyansh Agarwal, Prafulla Kumar Choubey, Yixin Mao, Silvio
Savarese, Caiming Xiong, and Chien-Sheng Wu. CRMArena-Pro: Holistic assessment of LLM agents across diverse business
scenarios and interactions.Transactions on Machine Learning Research, 2026. URL https://arxiv.org/abs/2505.18878.
[6] Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, and Karthik Narasimhan. SWE-
bench: Can language models resolve real-world GitHub issues?arXiv preprint arXiv:2310.06770, 2023. URL https:
//arxiv.org/abs/2310.06770.
[7] Percy Liang, Rishi Bommasani, Tony Lee, Dimitris Tsipras, Dilara Soylu, Michihiro Yasunaga, Yian Zhang, Deepak Narayanan,
Yuhuai Wu, Ananya Kumar, et al. Holistic evaluation of language models.arXiv preprint arXiv:2211.09110, 2022. URL
https://arxiv.org/abs/2211.09110.
[8] Xiao Liu, Hao Yu, Hanchen Zhang, Yifan Xu, Xuanyu Lei, Hanyu Lai, Yu Gu, Hangliang Ding, Kaiwen Men, Kejuan Yang,
et al. Agentbench: Evaluating llms as agents.arXiv preprint arXiv:2308.03688, 2023. URL https://arxiv .org/abs/2308.03688.
[9] Zhiwei Liu, Jielin Qiu, Shiyu Wang, Jianguo Zhang, Zuxin Liu, Roshan Ram, Haolin Chen, Weiran Yao, Shelby Heinecke,
Silvio Savarese, Huan Wang, and Caiming Xiong. MCPEval: Automatic MCP-based deep evaluation for AI agent models.
arXiv preprint arXiv:2507.12806, 2025. URL https://arxiv.org/abs/2507.12806.
[10] Ziyang Luo, Zhiqi Shen, Wenzhuo Yang, Zirui Zhao, Prathyusha Jwalapuram, Amrita Saha, Doyen Sahoo, Silvio Savarese,
Caiming Xiong, and Junnan Li. MCP-Universe: Benchmarking large language models with real-world Model Context Protocol
servers.arXiv preprint arXiv:2508.14704, 2025. URL https://arxiv.org/abs/2508.14704.
[11] Chang Ma, Junlei Zhang, Zhihao Zhu, Cheng Yang, Yujiu Yang, Yaohui Jin, Zhenzhong Lan, Lingpeng Kong, and Junxian
He. AgentBoard: An analytical evaluation board of multi-turn LLM agents.arXiv preprint arXiv:2401.13178, 2024. URL
https://arxiv.org/abs/2401.13178.
[12] Grégoire Mialon, Clémentine Fourrier, Craig Swift, Thomas Wolf, Yann LeCun, and Thomas Scialom. GAIA: A benchmark
for general AI assistants.arXiv preprint arXiv:2311.12983, 2023. URL https://arxiv.org/abs/2311.12983.
[13] Cheng Qian, Zuxin Liu, Akshara Prabhakar, Zhiwei Liu, Jianguo Zhang, Haolin Chen, Heng Ji, Weiran Yao, Shelby Heinecke,
Silvio Savarese, Caiming Xiong, and Huan Wang. UserBench: An interactive gym environment for user-centric agents.arXiv
preprint arXiv:2507.22034, 2025. URL https://arxiv.org/abs/2507.22034.
8

Salesforce AI Research2026-06-15
[14] Yujia Qin, Shihao Liang, Yining Ye, Kunlun Zhu, Lan Yan, Yaxi Lu, Yankai Lin, Xin Cong, Xiangru Tang, Bill Qian, et al.
ToolLLM: Facilitating large language models to master 16000+ real-world APIs.arXiv preprint arXiv:2307.16789, 2023. URL
https://arxiv.org/abs/2307.16789.
[15] Jielin Qiu, Zuxin Liu, Zhiwei Liu, Rithesh Murthy, Jianguo Zhang, Haolin Chen, Shiyu Wang, Ming Zhu, Liangwei Yang, Juntao
Tan, Zhepeng Cen, Cheng Qian, Shelby Heinecke, Weiran Yao, Silvio Savarese, Caiming Xiong, and Huan Wang. LoCoBench:
A benchmark for long-context large language models in complex software engineering.arXiv preprint arXiv:2509.09614,
2025. URL https://arxiv.org/abs/2509.09614.
[16] Salesforce AI Research. Benchforce: A function-calling benchmark for enterprise agent workflows. https://github .com/
SalesforceAIResearch/benchforce, 2025. Accessed 2026-04-29.
[17] Timo Schick, Janice Dwivedi-Yu, Roberto Dessì, Roberta Raileanu, Maria Lomeli, Luke Zettlemoyer, Nicola Cancedda, and
Thomas Scialom. Toolformer: Language models can teach themselves to use tools.arXiv preprint arXiv:2302.04761, 2023.
URL https://arxiv.org/abs/2302.04761.
[18] Juntao Tan, Liangwei Yang, Zuxin Liu, Zhiwei Liu, Rithesh Murthy, Tulika Manoj Awalgaonkar, Jianguo Zhang, Weiran Yao,
Ming Zhu, Shirley Kokane, Silvio Savarese, Huan Wang, Caiming Xiong, and Shelby Heinecke. PersonaBench: Evaluating AI
models on understanding personal information through accessing (synthetic) private user data.arXiv preprint arXiv:2502.20616,
2025. URL https://arxiv.org/abs/2502.20616.
[19] Xingyao Wang, Zihan Wang, Jiateng Liu, Yangyi Chen, Lifan Yuan, Hao Peng, and Heng Ji. MINT: Evaluating LLMs in
multi-turn interaction with tools and language feedback.arXiv preprint arXiv:2309.10691, 2023. URL https://arxiv .org/abs/
2309.10691.
[20] Fanjia Yan, Huanzhi Mao, Charlie Cheng-Jie Ji, Tianjun Zhang, Shishir G. Patil, Ion Stoica, and Joseph E. Gonzalez. Berkeley
function calling leaderboard. https://gorilla.cs.berkeley.edu/leaderboard.html, 2024. Accessed 2026-04-29.
[21] Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and Yuan Cao. ReAct: Synergizing reasoning
and acting in language models.arXiv preprint arXiv:2210.03629, 2022. URL https://arxiv.org/abs/2210.03629.
[22] Shunyu Yao, Noah Shinn, Pedram Razavi, and Karthik Narasimhan. τ-bench: A benchmark for tool-agent-user interaction in
real-world domains.arXiv preprint arXiv:2406.12045, 2024. URL https://arxiv.org/abs/2406.12045.
[23] Shuyan Zhou, Frank F. Xu, Hao Zhu, Xuhui Zhou, Robert Lo, Abishek Sridhar, Xianyi Cheng, Tianyue Ou, Yonatan Bisk,
Daniel Fried, Uri Alon, and Graham Neubig. WebArena: A realistic web environment for building autonomous agents.arXiv
preprint arXiv:2307.13854, 2023. URL https://arxiv.org/abs/2307.13854.
A CLI Reference
The egi-bench CLI is the preferred entry point. The lower-level run_all.py script is also supported; the CLI
delegates to it internally.
Installation.
scripts/install_all.sh provisions the root egi-bench CLI, the per-benchmark virtual environments, the
LiteLLM proxy venv, and the benchmark data in one idempotent step:
git clone https://github.com/SalesforceAIResearch/egi-bench.git
cd egi-bench
bash scripts/install_all.sh
source .venv/bin/activate
Credentials.
A single .env file at the repository root supplies all credentials. OPENAI_API_KEY is required even when the model
under test is non-OpenAI, because the judge and simulator calls are pinned to OpenAI for apple-to-apple scoring; add
the other provider keys for whichever upstreams you route through:
OPENAI_API_KEY=your-openai-api-key # also powers judge/simulator pins
ANTHROPIC_API_KEY=... # optional, for Claude routes
GEMINI_API_KEY=... # optional, for Gemini routes
# optional deep-mode keys:
SERP_API_KEY=... # MCP-Universe web_search
GOOGLE_MAPS_API_KEY=... # MCP-Universe location_navigation
NPS_API_KEY=... # MCPEval national_parks
9

Salesforce AI Research2026-06-15
Table 4:The eight benchmarks unified under EGI-BENCH. Task counts reflect the quick and deep mode profiles defined
inbenchmark_config.yaml. Full benchmark descriptions are in Section 4.
Benchmark Domain Tasks (quick / deep) Primary metric
CRMARENACRM operations 9 types×6 /×3 Task accuracy
HERB Enterprise search 80 Qs / full F1+content correctness
PERSONABENCHPersonal data QA 3 people×2 /×4 noises QA accuracy
USERBENCHTravel planning 3 envs×60 / all envs Micro-avg. reward
MCP-UNIVERSEMCP tool use 1 dom.×20 / 3 dom. Sub-eval pass rate
MCPEVALMCP tool use 1 dom.×50 / 3 dom.×50 Flex. avg. score
BENCHFORCEFunction calling 1 env×40 / 2 envs full Accuracy
LOCOBENCHLong-context SWE 30 easy / 500 full 0–5 rubric
Model routing.
All LLM inference routes through a local LiteLLM proxy onhttp://localhost:8008/v1 (OpenAI-compatible).
Each -model is mapped to a provider vialitellm_proxy/litellm_config.yaml, so the sameegi-bench
run -model X works for OpenAI, Anthropic, Gemini, Bedrock, Vertex, Azure, OpenRouter, and self-hosted
backends (vLLM, Ollama, TGI). egi-bench run auto-spawns the proxy on demand; power users can manage a
long-lived proxy directly:
egi-bench proxy start # long-lived proxy across runs
egi-bench proxy status
egi-bench proxy logs -f # tail upstream provider errors
egi-bench proxy stop
Benchmark environments and data.
egi-bench doctor
egi-bench setup # install per-benchmark .venv’s + data
egi-bench setup --skip-data
egi-bench data # refresh data only
Running evaluations.
egi-bench run --model gpt-4o-mini --mode quick --parallel
egi-bench run --model gpt-4o-mini --mode deep --parallel --max-workers 2
egi-bench run --model gpt-4o-mini --mode quick \
--benchmarks crmarena herb userbench
Reporting.
egi-bench report # latest aggregate
egi-bench report --rescore --model <m> --mode quick
egi-bench report --rescore --model <m> --mode quick \
--egi-weights M1=0.20,M5=0.30
egi-bench clean
report -rescore re-derives every benchmark’s sub-metric values from cached raw outputs and re-runs the
aggregator, enabling routing or weight changes without re-running inference.
B Benchmark Scope and Metric Coverage Tables
This appendix collects the two reference tables summarizing the eight benchmarks: Table 4 lists each benchmark’s
domain, task counts under quick and deep modes, and its native primary metric; Table 5 shows which benchmarks (and
which sub-metrics) contribute to each of the M1–M6 enterprise metrics.
10

Salesforce AI Research2026-06-15
Table 5:Which benchmarks contribute to each enterprise metric after fine-grained decomposition. Every benchmark
feeds at least one bucket and every bucket receives at least two routed sub-metrics; M 6 is the only bucket whose
sub-metrics come from a single benchmark (LOCOBENCH).
Metric Contributing benchmarks (sub-metric sources)
M1 CRMARENA(NCR, HTU, TCU, TII, BRI, MTA), BENCHFORCE(accuracy_all), LOCOBENCH
(functional_correctness)
M2 MCP-UNIVERSE(per-domain pass rate), MCPEVAL(flexible average score), BENCHFORCE(finished ratio)
M3 USERBENCH(micro_avg), LOCOBENCH(longcontext_utilization)
M4 CRMARENA(NED, KQA), HERB (per-entity F1, content correctness), PERSONABENCH(QA accuracy)
M5 CRMARENA(PVI), HERB (unanswerable null rate), BENCHFORCE(unsafe-failure gap)
M6 LOCOBENCH(software_engineering, code_quality)
C Fine-Grained Sub-Metric Routing
The routing table (Table 6) is the operational heart of EGI-BENCH. Every row lists a sub-metric that a benchmark
natively reports and the enterprise bucket (M1–M6) it feeds. No benchmark’s overall score is consumed directly.
Why sub-metric routing.
Different sub-metrics inside the same benchmark often probe very different capabilities. In CRMARENA, PVI (Policy
Violation Identification) is a direct safety signal, KQA is a retrieval-grounded knowledge task, and NCR is a business-
action routing task; averaging the three loses the distinction that enterprise stakeholders care about. By routing PVI into
M5, KQA and NED into M4, and the remaining six task types into M1, we avoid dilution across capabilities and retain
diagnostic signal at the bucket level. The same logic applies to HERB, whose grounded per-entity F1 and content
correctness feed M4 while its unanswerable null rate feeds M5 as a dedicated anti-hallucination signal.
Table 6:Fine-grained sub-metric routing. Each row shows a native sub-metric reported by a benchmark, the enterprise
metric (M1–M6) it is routed into, and a short rationale. No benchmark’s overall score is consumed directly; the routing
is the unit of aggregation.
Benchmark Sub-metric Bucket Rationale
CRMARENANCR (Case Routing) M 1 Business action correctness
HTU (Handle Time) M 1 Analytical task outcome
TCU (Transfer Count) M 1 Analytical task outcome
TII (Top Issue ID) M 1 Analytical task outcome
BRI (Best Region ID) M 1 Analytical task outcome
MTA (Monthly Trend) M 1 Task outcome
NED (Named Entity Disamb.) M 4 Entity resolution is grounded retrieval
KQA (Knowledge QA) M 4 Knowledge retrieval correctness
PVI (Policy Violation ID) M 5 Direct policy / safety signal
HERB Per-entity F1 (person/url/pr/company) M 4 Extraction / grounding quality
Content correctness M 4 Evidence-grounded answering
Unanswerable null rate M 5 Primary anti-hallucination signal
PERSONABENCHPer-(noise×type) QA accuracy M 4 Context-grounded personalized retrieval
MCP-UNIVERSEPass rate:financial_analysisM 2 Tool actioning in domain (quick)
Pass rate:web_searchM 2 Tool actioning in domain (deep)
Pass rate:location_nav.M 2 Tool actioning in domain (deep)
MCPEVALFlexible per-domain average score M 2 Tool actioning reliability
USERBENCHPer-envmicro_avgM 3 Multi-turn planning quality
BENCHFORCEaccuracy_allper env M 1 Task outcome correctness
finished_entries/totalM 2 Operational actioning reliability
acc_finished−acc_allgap M 5 Unsafe-failure proxy
continued on next page
11

Salesforce AI Research2026-06-15
Table 6 continued from previous page
Benchmark Sub-metric Bucket Rationale
LOCOBENCHfunctional_correctness M 1 Solves the task
software_engineering M 6 Engineering discipline
code_quality M 6 Maintainability
longcontext_utilization M 3 Long-horizon planning over context
Normalization and aggregation.
Sub-metrics are first rescaled to [0,100] with each benchmark’s native conventions (F1 ∈[0,1] becomes [0,100] ; pass
rates stay proportional). Lower-is-better signals are converted to higher-is-better before routing (e.g. BENCHFORCE’s
reliability gap enters M 5 as 100−(acc_finished−acc_all) ). Within each bucket we default to an equal-
weighted mean of all routed sub-metrics; benchmark_config.yaml supports per-sub-metric weights when a
principled override is warranted.
Missing-data handling.
If a sub-metric is unavailable (e.g. a benchmark was skipped), we reweightwithinits bucket only, never globally. If a
whole benchmark run fails, all of its contributed sub-metrics are dropped from their buckets and every affected bucket
is renormalized locally. The per-run aggregate report explicitly flags which sub-metrics were missing so readers can
judge coverage.
Routing is auditable.
The routing is stored declaratively in benchmark_config.yaml so reviewers can override it and rerun aggregation
without touching code. Section E describes the CLI’s report -rescore subcommand that re-derives EGI from
stored raw outputs when the routing changes.
D Extended Routing Rationale
This appendix expands on the routing table in Section C with the reasoning behind the more debatable assignments.
CRMARENA.
Six analytical task types (NCR, HTU, TCU, TII, BRI, MTA) go to M1 because each produces a single business-facing
answer whose correctness is measured by exact or structured match. NED (Named Entity Disambiguation) goes to M4
because the ground truth depends on resolving entities from retrieved records; KQA (Knowledge QA) similarly tests
retrieval-grounded QA. PVI (Policy Violation Identification) goes to M5 because it is the only task type whose ground
truth is a policy judgment — a direct safety signal.
HERB.
Per-entity F1 (over person, url, pr, and company fields) and content correctness measure grounded retrieval quality and
feed M4. The unanswerable null rate measures whether the LLM abstains when no answer exists; it feeds M5 and is in
practice our primary anti-hallucination signal.
MCPEVAL.
The routed signal is the flexible per-domain average score, which feeds M2 (tool actioning reliability). The scorer also
computes decomposed components — tool-name match, parameter match, order, and strict success — but these are not
yet surfaced to the aggregate runner. When they are, the order component is slated to route to M3 (tool sequencing is
planning) and the strict success rate to M5 (all-or-nothing, hence sensitive to drift and over-action).
LOCOBENCH.
functional_correctness goes to M1 (solves the task). software_engineering and code_quality
feed M6 (engineering discipline; maintainability). longcontext_utilization feeds M3 because the dimension
12

Salesforce AI Research2026-06-15
measures long-horizon reasoning and planning over extended context, which is a planning/orchestration signal rather
than a retrieval one.
Debatable cases.
The routing of longcontext_utilization to M3 rather than M4 is the most debatable assignment among the
currently active routes; the planned MCPEVALcomponent routing (order → M3, strict → M5 rather than M2) is a
second. All routings are recorded in benchmark_config.yaml and are overridable via egi-bench report
-rescorewithout re-running inference.
E Execution Modes
EGI-BENCHexposes two execution modes, selected per run via -mode quick|deep . Modes are defined bytotal
wall-clock, not by coverage heuristics:
•Quick modetargets a total wall-clock under∼180min with-parallel -max-workers 2.
•Deep modetargets∼12h of wall-clock with similar parallelism.
Coverage decisions (which categories, how many tasks per category) fall out of a per-benchmark runtime budget rather
than being picked by hand. “Fast enough” benchmarks keep their original upstream configuration in both modes; slower
benchmarks get subsetted. Concrete wall-clock numbers depend on the host machine and the inference endpoint, so we
define modes by budget targets rather than by a fixed per-benchmark runtime table.
Subsetting rules.
When a benchmark must be subsetted:
1. Keep at least one task per existing category so every reported sub-metric retains signal.
2. Reducetasks per categorybefore dropping a category, since dropping a category also drops a bucket contributor.
3. If a category must be dropped in quick mode, prefer the one whose routed bucket is most redundantly covered
elsewhere (e.g., a MCP-UNIVERSEdomain whose M 2 signal is already supplied by MCPEVAL/BENCHFORCE).
4. Record subset definitions inbenchmark_config.yaml; do not hard-code them inrun_all.py.
CLI surface.
The preferred entry points are:
egi-bench doctor # dependency check
egi-bench setup # install per-benchmark venvs + data
egi-bench run --model <m> --mode {quick,deep} --parallel
egi-bench report # latest
egi-bench report --rescore --model <m> --mode <m> # re-aggregate
report -rescore re-derives every benchmark’s sub-metric values from cached raw outputs and re-runs the M1–M6
aggregator. This means routing or weighting changes can be evaluated without re-running inference, which is important
for framework stability as Table 6 evolves.
Credentials.
Both modes require OPENAI_API_KEY (it powers the OpenAI routes and the pinned judge/simulator calls, so
it is needed even when the model under test is non-OpenAI), plus whichever provider keys correspond to the
upstreams being routed through the LiteLLM proxy (e.g. ANTHROPIC_API_KEY, GEMINI_API_KEY). Deep mode
additionally benefits from SERP_API_KEY and GOOGLE_MAPS_API_KEY (MCP-UNIVERSE) and NPS_API_KEY
(MCPEVAL). Missing optional keys cause the affected domain to be skipped with a note, not a failure; the resulting
aggregate reports reduced coverage.
F Sub-Metric Catalog
The catalog below lists all sub-metrics currently emitted by each benchmark’s scorer in EGI-BENCH. Sub-metrics
marked “not routed” are filtered out of M1–M6 aggregation as internal diagnostics.
13

Salesforce AI Research2026-06-15
CRMARENA
Sub-metrics: NCR, HTU, TCU, TII, BRI, MTA, NED, KQA, PVI. All routed (six into M1, two into M4, one into M5).
HERB
Sub-metrics: per-entity F1 across {person, url, pr, company} (M4), content correctness (M4), unanswerable null rate
(M5).
PERSONABENCH
Sub-metrics by noise level (0.0,0.3,0.5,0.7 ) and question type (Basic information, Preference, Subjective, Social).
The per-(noise × question-type) QA accuracies all feed M4; the individual result_noise_x_y keys are retained
for diagnosis but not routed separately.
USERBENCH
Sub-metrics: micro_avg per env (travel22, travel33, travel44) → M3. Filtered (not routed): micro_max,
avg_number_of_1,avg_number_of_08.
MCP-UNIVERSE
Sub-metrics: per-domain sub-evaluator pass rate (M2). Quick mode exercises financial_analysis; deep mode
addsweb_searchandlocation_navigation, gated on API-key availability.
MCPEVAL
Routed sub-metric: the flexible per-domainaverage_score(M 2). The scorer also emits decomposed components
(flexible tool-name, parameter-match, order, and strict success rate) into each domain’s*_analysis.json, but these
are not yet surfaced to the aggregate runner; when they are, order is slated for M3 and strict.success_rate
for M5.
BENCHFORCE
Sub-metrics per env (hospital, hr_software): accuracy_all (M1), finished_entries/total (M2),
accuracy_finished−accuracy_all gap (M5). Filtered (not routed): token and turn efficiency — orthogonal
to correctness.
LOCOBENCH
Sub-metrics routed: functional_correctness (M1), software_engineering (M6), code_quality
(M6), longcontext_utilization (M3). Filtered: the 17 finer-grained dimensions and generation statistics used
internally by LoCoBench’s rubric.
G Reproducibility
Software versions.
Python 3.12+ and Node.js 20+; dependencies are installed per-benchmark via uv venv /uv pip install , and
each benchmark’s exact lockfile lives in its subdirectory. The whole stack — root CLI, per-benchmark venvs, the
LiteLLM proxy venv, and benchmark data — is provisioned from the repository root via the idempotent bash
scripts/install_all.sh.
Proxy and models.
All LLM inference routes through a local LiteLLM proxy onhttp://localhost:8008/v1 (OpenAI-compatible);
the model-to-provider mapping is declared in litellm_proxy/litellm_config.yaml. To keep scores
comparable across models, that configpinsthe judge/simulator model names (e.g. gpt-4o, gpt-4.1) to OpenAI
14

Salesforce AI Research2026-06-15
regardless of the model under test, so OPENAI_API_KEY must be set even for non-OpenAI runs. The evaluator model
for MCP-UNIVERSEis configured viaEVALUATOR_MODELin.env(defaults togpt-4.1).
Seeds.
benchmark_config.yaml sets sample_seed: 42 for subsetting where applicable (CRMARENA, MCP-
UNIVERSE). Other benchmarks use deterministic ordering over their native task files.
Quick-mode subset definitions.
For each benchmark, the quick profile is recorded as follows (excerpted frombenchmark_config.yaml):
• CRMARENA: all 9 task types, up to 6 tasks per category.
• HERB: answerable and unanswerable modes; 80 questions total.
• PERSONABENCH: 3 people, communities {0, 1}, noise levels {0.0, 0.7},all-MiniLM-L6-v2retriever.
• USERBENCH: envs {travel22, travel33, travel44}, up to 60 tasks/env, 20 turns, pass_k 1, temperature 1.0.
• MCP-UNIVERSE: domain {financial_analysis}, 20 tasks.
• MCPEVAL: domain {airbnb}, 50 tasks, 20 turns.
• BENCHFORCE: env {hospital}, 40 entries, 15 turns.
• LOCOBENCH: difficultyeasy, 30 scenarios, 1800 s timeout.
Deep-mode counterparts expand each list to its upstream default.
Artifacts.
Each run produces results_aggregated/<model>_<mode>_<timestamp>.json plus per-benchmark
logs under results_aggregated/logs/. The JSON contains the full four-level metrics structure: scalar EGI,
M1–M6 with per-contributor breakdown, per-benchmark sub-metric values, and routing metadata.
Reproducing a quick-mode run.
The end-to-end command sequence is identical across the fourteen-model roster; only the -model string changes.
Claude Sonnet 4.5 is shown as an example.
# .env holds OPENAI_API_KEY (judge/simulator pins) plus the provider
# key for the model under test, e.g. ANTHROPIC_API_KEY.
# egi-bench run auto-spawns the LiteLLM proxy on localhost:8008.
egi-bench run \
--model claude-sonnet-4-5 \
--mode quick --parallel --max-workers 2
egi-bench report
15
