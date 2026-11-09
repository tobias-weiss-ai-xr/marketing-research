---
title: 'AD-Bench: A Real-World, Trajectory-Aware Advertising Analytics Benchmark for LLM Agents'
url: https://arxiv.org/abs/2602.14257
category: ai-marketing
subcategory: empirical
date: 2026-02
venue: ''
authors:
- Lingxiang Hu
- Yiding Sun
- Tianle Xia
- Wenwei Li
- Ming Xu
source: arxiv
pdf_url: https://arxiv.org/pdf/2602.14257
pages: 16
chars: 50192
fetched_at: '2026-11-08T13:15:20+00:00'
kb_version: 1
---

# AD-Bench: A Real-World, Trajectory-Aware Advertising Analytics Benchmark for LLM Agents

AD-Bench: A Real-World, Trajectory-Aware Advertising Analytics
Benchmark for LLM Agents
Lingxiang Hu∗, Yiding Sun∗, Tianle Xia∗, Wenwei Li∗, Ming Xu∗†
Lan Xu,Siying Wang,Wei Xu,Jie Jiang
Tencent
{lingxianghu,emanuelsun,tianlexia,wenweiwwli,flemingxu}@tencent.com
{lanxu,siyingwang,davidxu,zeus}@tencent.com
∗Equal contribution. †Corresponding author.
Abstract
While Large Language Model (LLM) agents
have made remarkable progress on complex
reasoning, evaluating them in real-world envi-
ronments remains an open problem. Existing
benchmarks are largely confined to idealized
simulations and fail to capture specialized do-
mains such as advertising and marketing analyt-
ics, where tasks require multi-round interaction
with professional tools and where ground-truth
answers quickly become obsolete as data and
platform rules evolve.
To address this, we proposeAD-Bench, a
benchmark built from real user marketing-
analysis requests on a production advertising
platform. AD-Bench introduces two key de-
signs: (i) adynamic ground-truth pipelinethat
replays expert tool-call trajectories to regener-
ate answers consistent with the current environ-
ment, mitigating answer obsolescence; and (ii)
atrajectory-aware evaluationthat jointly mea-
sures end-to-end answer correctness (Pass@k)
and trajectory coverage. Requests are stratified
into three difficulty levels (L1–L3) to probe
multi-round, multi-tool collaboration. Experi-
ments show that the best model, Claude-Opus-
4.7, attains Pass@1 = 76.9% and Pass@3 =
80.4% with 82.7% trajectory coverage overall,
yet drops sharply on L3 to Pass@1 = 61.4% and
Pass@3 = 65.1%, revealing that even state-of-
the-art agents have substantial gaps in complex
advertising analytics.
1 Introduction
LLMs evolve from passive knowledge-retrieval
interfaces into autonomous agents that can rea-
son, plan, and take actions in real-world environ-
ments (Wang et al., 2024a; Xi et al., 2025; Team
et al., 2025; Zeng et al., 2025; Xia et al., 2025).
Unlike conventional question answering (QA), real-
world agents must interact with tools through mul-
tiple steps, including retrieval-augmented gener-
ation (RAG) (Lewis et al., 2020) and access to
user-private data, ultimately producing effective
answers.
However, most existing agent evaluation bench-
marks are built on fixed tasks in idealized or simu-
lated settings (Mialon et al., 2023; Wei et al., 2025;
Zhou et al., 2023; Chen et al., 2025a; Wong et al.,
2025; Yao et al., 2024; Barres et al., 2025; Patil
et al., 2025), and thus struggle to capture the dy-
namics and complexity of real-world production
settings arising from continuously evolving envi-
ronment states and multi-tool interactions. This
limitation is particularly pronounced in advertising
and marketing, manifesting in the following three
challenges:
•Challenge 1: Ground-Truth Obsolescence.
This challenge is particularly evident in advertising
and marketing, where user data, campaign delivery
conditions, and platform policies are frequently up-
dated. Consequently, benchmarks based on static
QA pairs can quickly become obsolete: once the
underlying data or governing rules change, previ-
ously correct answers may no longer remain valid,
compromising the reliability of the ground truth.
•Challenge 2: Lack of Evaluation for Adver-
tising Trajectories.In advertising analytics, user
queries often require an agent to plan and exe-
cute an execution trajectory over a complex set
of tools. This involves selecting appropriate tools
and skills (Xia et al., 2026; Li et al., 2026) from a
diverse toolkit and specifying the correct parame-
ters at each step. Although end-to-end evaluation
can measure the accuracy of the final answer, it is
insufficient for assessing the validity of the agent’s
execution trajectory in advertising and marketing
scenarios.
•Challenge 3: Long-Tail Distribution of Ad-
vertising Analytics.Customer analytics needs
served by marketing platforms vary substantially.
In real online traffic, the frequency of analytics
tasks typically follows a long-tail distribution: ba-
sic descriptive analyses account for the majority
1
arXiv:2602.14257v2  [cs.CL]  22 Jun 2026

of requests, while highly specialized needs are dis-
persed across the long tail. If evaluation covers
only high-frequency tasks, it can introduce selec-
tion bias and thus overestimate the agent’s overall
capability in real-world settings.
To address the challenges above, we introduce
AD-Bench, a benchmark designed to evaluate
agents on real-world advertising and marketing
platforms in terms of trajectory coverage and end-
to-end task success. Our main contributions are as
follows:
•Dynamic Ground-Truth Generation Pipeline.
To mitigate ground-truth obsolescence, when con-
structing our benchmark based on online analyt-
ical requests, we do not directly collect final an-
swers from human experts. Instead, we record their
problem-solving trajectories and associated tool
calls. During evaluation, we replay these trajec-
tories and re-execute the corresponding tool calls
to regenerate ground-truth answers consistent with
the current environment, thereby reducing errors
caused by outdated answers.
•Trajectory-Aware Evaluation.We decompose
evaluation into two complementary aspects: (i) end-
to-end answer correctness on analytical requests,
which directly measures agent reliability; and (ii)
trajectory coverage, i.e., whether the expert refer-
ence trajectory is covered by the agent’s execution,
providing finer-grained analysis.
•Difficulty-Stratified Task Classification.To
counter the long-tail distribution of analytics needs,
we organize the benchmark along a difficulty hi-
erarchy instead of sampling only high-frequency
requests. Using the complexity of expert trajecto-
ries as a proxy for task difficulty, we stratify ana-
lytical requests into three levels (L1–L3), ranging
from single-metric retrieval to multi-condition syn-
thesis and judgment. This stratification mitigates
selection bias toward simple queries and enables a
fine-grained assessment of agent capability across
the full difficulty spectrum.
Experimental results in Section 3 reveal a clear
efficiency–accuracy trade-off across models (Fig-
ure 1): even the best overall model, Claude-Opus-
4.7, attains only 76.9% Pass@1, and its perfor-
mance degrades sharply on the hardest (L3) queries,
dropping to a Pass@3 of 65.1% and a trajectory
coverage of 69.9%. Our error analysis spans six di-
mensions: tool errors, parameter errors, instruction-
following errors, computation errors, hallucina-
tions, and long-context limitations. Consequently,
AD-Bench establishes a more rigorous, sustainable,
40 50 60 70 80
Overall Pass@1 Accuracy (%)
3.0
3.2
3.4
3.6
3.8
4.0
4.2Avg. Interaction Rounds
Efficient
& Inaccurate
Efficient
& Accurate
Costly
& Inaccurate
Costly
& Accurate
Gemini 3.1 ProDeepSeek V4 GPT 5.5
Claude Opus 4.7
Gemini 3.5 Flash
HY 3.0Qwen3 30B
Qwen3 235B
Kimi K2.6
MiniMax M2.7
Figure 1: Efficiency–accuracy trade-off across evaluated
models, plotting overall Pass@1 against the average
number of interaction steps (fewer is better). Claude-
Opus-4.7 attains the best accuracy (76.9% Pass@1), yet
no model reaches high accuracy with consistently short
trajectories, underscoring the difficulty of AD-Bench.
and business-aligned evaluation standard to facil-
itate the development of next-generation action-
oriented marketing agents.
2 AD-Bench
2.1 Benchmark Construction
The construction of AD-Bench relies on a real-
world Online Advertising Environment (Figure 2,
left). We collect 2,000 native user analysis requests,
and human experts resolve each one with stan-
dard marketing tools, recording their tool-call tra-
jectories as (Question,Execution Trajectory) pairs.
Rather than freezing static answers, the reference
answer is regenerated on demand by replaying the
trajectory against the current environment, keep-
ing it correct under evolving business rules. After
cleaning and deduplication, 823 high-quality in-
stances remain, which are further curated into a
final evaluation set of 225 instances (Section 2.3).
2.2 Evaluation Framework
Figure 2 (right) illustrates the evaluation pipeline
of AD-Bench. In the offline environment, a ReAct-
based agent processes benchmark requests, simu-
lating expert reasoning and tool calls. The execu-
tion follows three steps: retrieving business defini-
tions for semantic alignment, fetching advertising
metrics, and conducting analysis to generate a re-
sponse; a detailed L3 case study is provided in
Appendix Figure 10. Finally, an LLM-judge evalu-
ates the generated trajectory and response in terms
of answer correctness and trajectory coverage.
2

Stage 1: Online AdvertisingEnvironment Stage 2: Offline Evaluation Environment
Real User HumanExpert
Online-to-Offline
LLM Agent
LLM Judge
UserData
Knowledge
Query
+ +
Labeled Ground Truth
(Query +Answer + Trajectory)
filter case
Tools
Did all yesterday's
creatives hit
excellent?
AnswerCorrectness
(Pass@k)
TrajectoryCoverage
(subsequence)
Query
Step1:
Searchthedefineofexcellent
Step2:
Acquire creativesdata
Step3:
Perform data analysis
LLMTrajectory
Figure 2: System overview ofAD-Bench. The online advertising environment (left) yields human-validated ground-
truth trajectories, while the offline evaluation environment (right) evaluates LLM agents and uses LLM-as-a-judge
to assess answer correctness and trajectory coverage.
Level Count Definition Example Query
L1 31 Retrieve a metric
for a fixed scope
“Get the total cost across
all accounts yesterday. ”
L2 111 Compute metrics
with filtering or
comparison
“Compute the week-over-
week cost growth rate. ”
L3 83 Synthesize multi-
ple conditions and
make a judgment
“Analyze whether video
and image CTRs both
exceed the excellence
threshold. ”
Table 1: Count, definition, and a representative example
for each difficulty level in AD-Bench.
2.3 Task Classification and
Reference-Trajectory Curation
To prevent the evaluation from being dominated
by high-frequency simple queries while ensuring
coverage of long-tail analytical needs, we stratified
user requests. Specifically, we used the complexity
of human expert trajectories as a proxy for task dif-
ficulty and categorized all requests into three levels.
Through rigorous expert verification, for each of
the 225 retained instances we designate anoptimal
reference trajectory, i.e., the shortest, most direct
expert solution path used to anchor trajectory cov-
erage, while Pass@k still credits correct answers
reached via alternative or self-corrected paths. Ta-
ble 1 summarizes the count, definition, and repre-
sentative examples for each difficulty level (L1, L2,
and L3).
2.4 Evaluation Metrics
We evaluate agents from two complementary and
mutually non-implied angles:whetherthey reach
the correct answer andhowthey get there.
• Answer correctness:We report Pass@ k on the
final answer. Pass@1 measures single-run cor-
rectness, while Pass@3 measures whether at least
one of three independent runs is correct, account-
ing for sampling stochasticity.
• Trajectory coverage:A sample iscoveredonly
when the agent reproduces the expert reference
trajectory, i.e., it calls the required tools in a
valid order, supplies the key parameters correctly,
and follows the instruction constraints—no tool,
parameter, or instruction-following error (Sec-
tion 3.3). As some tools have a vast parameter
space (e.g., RAG queries or code), we verify the
keyparameters rather than exact matches.
3 Experiments and Results
3.1 Experimental Setup
We evaluate a set of open-weight and proprietary
state-of-the-art LLMs. The open-weight models
include Qwen3-235B and Qwen3-30B-A3B (Yang
et al., 2025), DeepSeek-V4 (DeepSeek-AI, 2026),
Kimi-K2.6 (Team et al., 2025), MiniMax-
M2.7 (MiniMax, 2026), and HY-3.0 (Tencent Hun-
yuan Team, 2026). The proprietary models are
accessed via public APIs, including Claude-Opus-
4.7 (Anthropic, 2026), Gemini-3.1-Pro (Google
DeepMind, 2026a), Gemini-3.5-Flash (Google
DeepMind, 2026b), and GPT-5.5 (OpenAI, 2026).
We implement a marketing agent based on the
widely adopted ReAct framework (Yao et al., 2022)
and equip it with 9 domain-specific tools for execut-
ing marketing tasks. We follow the evaluation pro-
tocol defined in Section 2 and use Gemini-3.1-Pro
as the judge to determine answer correctness and
assess trajectory coverage. Additional experimen-
tal settings and results are provided in Appendix A.
3

Table 2: Pass@1, Pass@3, and average trajectory length across overall and all difficulty tiers onAD-Bench.
Model Overall L1 L2 L3 Avg. Len.
Pass@1↑Pass@3↑Pass@1↑Pass@3↑Pass@1↑Pass@3↑Pass@1↑Pass@3↑
Claude-Opus-4.776.9 80.4 96.8 100.0 82.9 86.561.4 65.1 3.37
Gemini-3.5-Flash 76.0 79.6 93.5 93.5 82.0 84.7 61.4 67.5 3.49
Gemini-3.1-Pro 75.1 78.796.8 100.077.5 79.363.969.9 3.25
DeepSeek-V4 64.9 77.396.8 100.063.1 73.9 55.473.5 3.25
GPT-5.5 69.3 77.3 90.3 93.5 74.8 81.1 54.2 66.3 3.27
Kimi-K2.6 70.7 76.9 90.3 96.8 82.0 82.9 48.2 61.4 4.01
MiniMax-M2.7 66.7 74.7 90.3 93.5 77.5 82.0 43.4 57.8 4.15
HY-3.0 57.3 68.0 64.5 74.2 71.2 79.3 36.1 50.6 3.68
Qwen3-235B 54.7 64.0 90.3 96.8 62.2 70.3 31.3 43.4 3.81
Qwen3-30B-A3B 39.6 49.3 80.6 83.9 44.1 55.9 18.1 27.7 3.70
3.2 Main Results and Analysis
Performance across difficulty tiers.Table 2 re-
ports the performance of all evaluated models on
AD-Bench. Overall, proprietary models set the
current performance upper bound: Claude-Opus-
4.7 achieves the best Pass@3 (80.4%), followed
closely by Gemini-3.5-Flash (79.6%) and Gemini-
3.1-Pro (78.7%). However, aggregated scores mask
a pronounced stratification by difficulty. While top
models are highly reliable on L1 (Pass@3 > 93%),
performance drops sharply by 25–35 percentage
points from L1 to L3 on tasks requiring complex,
multi-tool orchestration. This indicates that cur-
rent LLM agents are strong at direct information
retrieval, yet remain fragile on the long-horizon
dependency chains characteristic of industrial ad-
vertising analytics. Beyond offline evaluation, we
further use AD-Bench as a continuous evaluation
harness to diagnose and iterate a production agent,
raising its online user satisfaction rate to 88.37%
(Appendix B).
Trajectory coverage and execution robustness.
To diagnose whether failures stem from tool-use
planning or answer generation, we examine tra-
jectory coverage across tiers. As shown in Fig-
ure 4, most models achieve near-saturated cover-
age on L1 (>93%), suggesting they can reliably
identify the appropriate tools and parameters for
low-complexity queries. By contrast, on L3 even
the best overall model, Claude-Opus-4.7, sees its
coverage drop to 69.9%: the model increasingly
deviates from the reference trajectory on complex
tasks, reflecting failures in planning and executing
the required tool-use steps.
Effectiveness of trajectory-based evaluation.
Figure 3 validates our trajectory signal: models
with higher trajectory coverage achieve higher
60 80
40
60
80Pass@1 (%)
Overall  (r = 0.994)
80 100
60
80
100
L1  (r = 0.934)
70 80 90
Trajectory Coverage (%)
40
60
80Pass@1 (%)
L2  (r = 0.904)
20 40 60
Trajectory Coverage (%)
20
40
60
L3  (r = 0.990)
Figure 3: Correlation between trajectory coverage ( x-
axis) and Pass@1 (y-axis) across the ten evaluated mod-
els, with one panel per tier (Overall, L1, L2, L3). Each
point is a model; the line shows a linear fit with its con-
fidence band. The two metrics are strongly correlated at
every tier (r= 0.994 overall; r= 0.934/0.904/0.990
for L1/L2/L3), supporting trajectory coverage as a mean-
ingful proxy of agent evaluation quality.
Pass@1 across all tiers, and the correlation remains
especially strong on L3, where success relies on
maintaining correct multi-step tool dependencies.
This shows that tracking whether an agent follows
mandatory tool calls is predictive of end-to-end
success.
Mismatch between coverage and Pass@3.A
notable exception arises for DeepSeek-V4. De-
spite relatively low Pass@1 on L3 (55.4%), its
Pass@3 on L3 reaches 73.5%, the highest among
all models. This suggests its primary limitation
is not the absence of capability, but instability
in single-trajectory long-horizon planning. With
multiple samples, DeepSeek-V4 benefits from ex-
4

L1 L2 L30
25
50
75
100
Gemini 3.5 Flash
96.8
88.3
71.1
L1 L2 L3
Claude Opus 4.7
93.5 89.2
69.9
L1 L2 L3
Gemini 3.1 Pro
96.8
87.4
69.9
L1 L2 L3
GPT 5.5
93.5
85.6
63.9
L1 L2 L3
Kimi K2.6
96.8
90.1
56.6
L1 L2 L30
25
50
75
100
MiniMax M2.7
93.5 87.4
51.8
L1 L2 L3
DeepSeek V4
96.8
73.0
65.1
L1 L2 L3
HY 3.0
67.7
82.9
50.6
L1 L2 L3
Qwen3 235B
93.5
81.1
39.8
L1 L2 L3
Qwen3 30B
90.3
73.9
26.5
Trajectory Coverage (%)
L1 (Easy) L2 (Medium) L3 (Hard)
Figure 4: Trajectory coverage of each evaluated model across the three difficulty levels (L1/L2/L3). Coverage is
near-saturated on L1 for most models but degrades substantially on L3, revealing reduced execution stability on
complex tasks.
ploratory diversity, discovering alternative yet valid
tool-calling routes even without strictly following
the reference trajectory. These results expose a key
trade-off: reasoning competence may be present
but unreliable, manifesting only under repeated
attempts that compensate for the low success prob-
ability of any single deterministic execution.
Trajectory length.The rightmost column of Ta-
ble 2 reports the average trajectory length (number
of interaction steps) for each model. Most mod-
els complete tasks within 3.25–4.15 steps, with
Gemini-3.1-Pro and DeepSeek-V4 producing the
most concise trajectories (3.25). Longer trajecto-
ries do not yield better performance: MiniMax-
M2.7 has the longest average trajectory (4.15) yet
does not outperform more efficient models, suggest-
ing that extra steps often reflect redundant retries or
error recovery rather than productive exploration.
In contrast, top-performing models execute shorter
trajectories, indicating stronger planning that re-
duces unnecessary interactions.
3.3 Error Analysis
We manually analyzed failed trajectories on AD-
Bench and found that errors in complex advertising
analytics stem not from a single factor, but from
the accumulation of multiple errors along the exe-
cution trajectory. Errors tend to cascade rather than
occur in isolation: a single failed case can exhibit
multiple error types, so their coverage rates need
not sum to 100%. On average, each failed case
Table 3: Distribution of error types across models on
AD-Bench. We categorize each failure according to the
root cause in the execution trace. TE. for Tool Error,
PE. for Parameter Error, IF. for Instruction Following,
CE. for Computation Error, Hal. for Hallucination, LC.
for Long Context Ability. Statistics include all error
types per case (multi-label).Boldfor the best, while
Underlined for the second best performance.
Model Error Types Total
TE. PE. IF. CE. Hal. LC. #Err TotE
Claude-Opus-4.7158 15 103 452 55
Gemini-3.5-Flash15121413 3 154 58
Gemini-3.1-Pro 20 321 16 3 4 56 67
Kimi-K2.6 25 5 24 1523 66 74
GPT-5.5 21 12 19 18 7 4 69 81
DeepSeek-V4 25 22 18 14 4 4 79 87
MiniMax-M2.7 32 18 15 19 3 4 75 91
HY-3.0 22 30 20 21 6 10 96 109
Qwen3-235B 47 14 22 35 8 4 102 130
Qwen3-30B-A3B 61 24 15 48 12 7 136 167
contains about 1.06–1.27 error types. The error
distribution is shown in Table 3.
Tool and parameter errors.Across models, the
dominant sources of failure are tool and parame-
ter errors, together appearing in roughly 40–60%
of failed cases, indicating that multi-step tool or-
chestration remains brittle. Tool errors subsume
planning and dependency mistakes, including in-
correct tool ordering, dependency violations (e.g.,
querying report data before resolving the required
account scope), premature termination, unneces-
sary detours, or invoking irrelevant tools, all of
5

which drive execution away from the intended so-
lution path.
Parameter errors frequently co-occur with plan-
ning issues and amplify their impact. Even when
the agent selects an appropriate tool, it often mis-
specifies key parameters such as date ranges, ac-
count or campaign filters, attribution windows, and
aggregation definitions. These deviations are sub-
tle but critical: individual steps can appear lo-
cally plausible while still yielding answers that
disagree with ground truth. Such errors persist
even in strong proprietary models, underscoring
that maintaining precise alignment over long execu-
tion chains remains an open challenge in dynamic
marketing settings.
Instruction-following errors.A distinct failure
mode is instruction following: the agent constructs
a plausible tool trajectory yet violates explicit con-
straints stated in the query, such as the requested
time range, account or campaign filter, ranking cri-
terion, or output format. Unlike tool errors, these
failures occur even when the execution path is oth-
erwise valid, showing that a correct tool sequence
does not guarantee faithful adherence to user intent.
Retrieval failures and hallucination.Halluci-
nation becomes particularly salient in tasks that
require combining platform knowledge with live
data. A recurring failure mode is that the agent
produces a confident answer from prior assump-
tions instead of following the intended workflow
to retrieve supporting evidence. Once the initial
premise is incorrect, subsequent reasoning may
remain coherent yet factually ungrounded, lead-
ing to high-confidence but unverifiable conclusions.
This pattern is more pronounced in smaller mod-
els, suggesting limitations in evidence seeking and
robust integration of retrieved knowledge under
long-horizon interactions.
Computation and post-processing errors.As
task complexity grows, agents must post-process
large volumes of intermediate outputs, often via
programmatic transformations. For tasks requir-
ing Python-based processing, we observe a clear
drop in code reliability as business logic becomes
more complex, including syntax/runtime failures,
missing key fields, incorrect slicing, and aggrega-
tion mismatches. Stronger models mitigate but do
not eliminate these issues, indicating that translat-
ing natural-language intent into correct executable
computation remains a major reliability bottleneck.
Long-context degradation.Although tool feed-
back can in principle enable self-correction (Asai
et al., 2023), in practice error recovery frequently
triggers repeated retries and verbose traces, rapidly
expanding the interaction history. As context
grows, agents struggle to track and reuse interme-
diate variables and to accurately localize the true
source of failure. This often creates a negative
feedback loop in which early mistakes lengthen
the trajectory, which further degrades state tracking
and induces additional errors, ultimately reducing
both success rate and execution efficiency.
4 Related Work
QA benchmarks, which construct fact-based ques-
tions across multiple dimensions, are extensively
employed to evaluate the response effectiveness of
LLMs or Deep Research systems. By providing
static questions, these benchmarks aim to achieve
comprehensive coverage (Hendrycks et al., 2020;
Rein et al., 2024; Zhong et al., 2024) or construct
more complex problems (Wang et al., 2024b; Chen
et al., 2025b; Phan et al., 2025) to enhance discrim-
inability. Beyond static QA, a growing line of agent
benchmarks evaluates interactive tool use, span-
ning general assistants (Mialon et al., 2023), func-
tion calling (Patil et al., 2025), conversational tool
agents (Yao et al., 2024; Barres et al., 2025), and
profession-aligned real-world tasks (Chen et al.,
2025a). Moving beyond static environments and
fixed knowledge corpora,AD-Benchintroduces a
suite of tools for accessing real-time accounts. It fa-
cilitates QA within a live sandbox environment that
mirrors real-world advertising and marketing inter-
actions, thereby enhancing the robustness of evalu-
ations. Driven by a similar rationale, benchmarks
like Mind2Web (Deng et al., 2023) and Webwalk-
erQA (Wu et al., 2025) also utilize unpredictable
sandbox simulations to ensure real-time interactiv-
ity and environmental unpredictability.
5 Conclusions
We introducedAD-Bench, a real-world, trajectory-
aware advertising analytics benchmark for LLM
agents. AD-Bench couples execution trajectories
with ground truths validated by human experts, en-
abling evaluation of both answer correctness and
trajectory coverage. Experiments across a diverse
set of models show strong performance stratifica-
tion by difficulty and reveal that difficult queries
remain a major bottleneck for current LLM agents.
6

Limitations
Overlap between the judge and the evaluated
models.Gemini-3.1-Pro is both an evaluated
agent and the automatic judge, which risks self-
preference bias; this is limited by rubric-based judg-
ing against an explicit reference trajectory rather
than open-ended scoring.
Imbalanced distribution across difficulty tiers.
Sampled from real long-tail traffic, AD-Bench has
uneven tiers (L1=31, L2=111, L3=83), so overall
scores favor the larger tiers and the small L1 tier
gives limited resolution—close rankings there are
effectively ties.
Ethical Statement
Our research strictly adheres to ethical guidelines to
safeguard user rights and privacy. All data within
the evaluation benchmark has been anonymized
and is used solely for scientific research purposes,
aiming to advance more reliable evaluations in deep
research systems.
References
Anthropic. 2026. Claude opus 4.7 system card. Closed-
source large language model.
Akari Asai, Zeqiu Wu, Yizhong Wang, Avirup Sil, and
Hannaneh Hajishirzi. 2023. Self-RAG: Learning to
retrieve, generate, and critique through self-reflection.
InThe Twelfth International Conference on Learning
Representations.
Victor Barres, Honghua Dong, Soham Ray, Xujie Si,
and Karthik Narasimhan. 2025. τ 2-bench: Evaluat-
ing conversational agents in a dual-control environ-
ment.arXiv preprint arXiv:2506.07982.
Kaiyuan Chen, Yixin Ren, Yang Liu, Xiaobo Hu, Hao-
tong Tian, Tianbao Xie, Fangfu Liu, Haoye Zhang,
Hongzhang Liu, Yuan Gong, and 1 others. 2025a.
xbench: Tracking agents productivity scaling with
profession-aligned real-world evaluations.arXiv
preprint arXiv:2506.13651.
Zijian Chen, Xueguang Ma, Shengyao Zhuang, Ping
Nie, Kai Zou, Andrew Liu, Joshua Green, Kshama
Patel, Ruoxi Meng, Mingyi Su, and 1 others. 2025b.
Browsecomp-plus: A more fair and transparent eval-
uation benchmark of deep-research agent.arXiv
preprint arXiv:2508.06600.
DeepSeek-AI. 2026. Deepseek-v4 technical report.
Open-weights MoE model, MIT license.
Xiang Deng, Yu Gu, Boyuan Zheng, Shijie Chen, Sam
Stevens, Boshi Wang, Huan Sun, and Yu Su. 2023.
Mind2web: Towards a generalist agent for the web.
Advances in Neural Information Processing Systems,
36:28091–28114.
Google DeepMind. 2026a. Gemini 3.1 pro model card.
Closed-source (API only).
Google DeepMind. 2026b. Gemini 3.5 flash model card.
Closed-source (API only).
Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou,
Mantas Mazeika, Dawn Song, and Jacob Steinhardt.
2020. Measuring massive multitask language under-
standing.arXiv preprint arXiv:2009.03300.
Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio
Petroni, Vladimir Karpukhin, Naman Goyal, Hein-
rich Küttler, Mike Lewis, Wen-tau Yih, Tim Rock-
täschel, and 1 others. 2020. Retrieval-augmented gen-
eration for knowledge-intensive nlp tasks.Advances
in neural information processing systems, 33:9459–
9474.
Xiangyi Li and 1 others. 2026. Skillsbench: Bench-
marking how well agent skills work across diverse
tasks.arXiv preprint arXiv:2602.12670.
Grégoire Mialon, Clémentine Fourrier, Thomas Wolf,
Yann LeCun, and Thomas Scialom. 2023. Gaia: a
benchmark for general ai assistants. InThe Twelfth
International Conference on Learning Representa-
tions.
MiniMax. 2026. Minimax-m2.7 model card. Condi-
tionally open-weights (Modified MIT).
OpenAI. 2026. Gpt-5.5. Closed-source large language
model, released April 2026.
Shishir G. Patil, Huanzhi Mao, Charlie Cheng-Jie Ji,
Fanjia Yan, Vishnu Suresh, Ion Stoica, and Joseph E.
Gonzalez. 2025. The berkeley function calling leader-
board (bfcl): From tool use to agentic evaluation of
large language models. InForty-second International
Conference on Machine Learning (ICML).
Long Phan, Alice Gatti, Ziwen Han, Nathaniel Li,
Josephina Hu, Hugh Zhang, Chen Bo Calvin Zhang,
Mohamed Shaaban, John Ling, Sean Shi, and 1 oth-
ers. 2025. Humanity’s last exam.arXiv preprint
arXiv:2501.14249.
David Rein, Betty Li Hou, Asa Cooper Stickland, Jack-
son Petty, Richard Yuanzhe Pang, Julien Dirani, Ju-
lian Michael, and Samuel R Bowman. 2024. Gpqa:
A graduate-level google-proof q&a benchmark. In
First conference on language modeling.
Kimi Team, Yifan Bai, Yiping Bao, Guanduo Chen,
Jiahao Chen, Ningxin Chen, Ruijue Chen, Yanru
Chen, Yuankun Chen, Yutian Chen, and 1 others.
2025. Kimi k2: Open agentic intelligence.arXiv
preprint arXiv:2507.20534.
Tencent Hunyuan Team. 2026. Tencent hunyuan hy3
preview. Open-weights MoE (295B total params),
Tencent Hunyuan Community License.
7

Lei Wang, Chen Ma, Xueyang Feng, Zeyu Zhang, Hao
Yang, Jingsen Zhang, Zhiyuan Chen, Jiakai Tang,
Xu Chen, Yankai Lin, and 1 others. 2024a. A survey
on large language model based autonomous agents.
Frontiers of Computer Science, 18(6):186345.
Yubo Wang, Xueguang Ma, Ge Zhang, Yuansheng Ni,
Abhranil Chandra, Shiguang Guo, Weiming Ren,
Aaran Arulraj, Xuan He, Ziyan Jiang, and 1 others.
2024b. Mmlu-pro: A more robust and challenging
multi-task language understanding benchmark.Ad-
vances in Neural Information Processing Systems,
37:95266–95290.
Jason Wei, Zhiqing Sun, Spencer Papay, Scott McK-
inney, Jeffrey Han, Isa Fulford, Hyung Won Chung,
Alex Tachard Passos, William Fedus, and Amelia
Glaese. 2025. Browsecomp: A simple yet challeng-
ing benchmark for browsing agents.arXiv preprint
arXiv:2504.12516.
Ryan Wong, Jiawei Wang, Junjie Zhao, Li Chen, Yan
Gao, Long Zhang, Xuan Zhou, Zuo Wang, Kai Xiang,
Ge Zhang, and 1 others. 2025. Widesearch: Bench-
marking agentic broad info-seeking.arXiv preprint
arXiv:2508.07999.
Jialong Wu, Wenbiao Yin, Yong Jiang, Zhenglin Wang,
Zekun Xi, Runnan Fang, Linhai Zhang, Yulan He,
Deyu Zhou, Pengjun Xie, and 1 others. 2025. Web-
walker: Benchmarking llms in web traversal. In
Proceedings of the 63rd Annual Meeting of the As-
sociation for Computational Linguistics (Volume 1:
Long Papers), pages 10290–10305.
Zhiheng Xi, Wenxiang Chen, Xin Guo, Wei He, Yi-
wen Ding, Boyang Hong, Ming Zhang, Junzhe Wang,
Senjie Jin, Enyu Zhou, and 1 others. 2025. The
rise and potential of large language model based
agents: A survey.Science China Information Sci-
ences, 68(2):121101.
Tianle Xia, Liang Ding, Guojia Wan, Yibing Zhan,
Bo Du, and Dacheng Tao. 2025. Improving complex
reasoning over knowledge graph with logic-aware
curriculum tuning. InProceedings of the AAAI Con-
ference on Artificial Intelligence, volume 39, pages
12881–12889.
Tianle Xia and 1 others. 2026. Grasp: Graph-structured
skill compositions for llm agents.arXiv preprint
arXiv:2604.17870.
An Yang, Anfeng Li, Baosong Yang, Beichen Zhang,
Binyuan Hui, Bo Zheng, Bowen Yu, Chang
Gao, Chengen Huang, Chenxu Lv, and 1 others.
2025. Qwen3 technical report.arXiv preprint
arXiv:2505.09388.
Shunyu Yao, Noah Shinn, Pedram Razavi, and Karthik
Narasimhan. 2024. τ-bench: A benchmark for tool-
agent-user interaction in real-world domains.arXiv
preprint arXiv:2406.12045.
Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak
Shafran, Karthik R Narasimhan, and Yuan Cao. 2022.
React: Synergizing reasoning and acting in language
models. InThe eleventh international conference on
learning representations.
Zhiyuan Zeng, Jiashuo Liu, Siyuan Chen, Tianci He,
Yali Liao, Yixiao Tian, Jinpeng Wang, Zaiyuan Wang,
Yang Yang, Lingyue Yin, and 1 others. 2025. Futurex:
An advanced live benchmark for llm agents in future
prediction.arXiv preprint arXiv:2508.11987.
Wanjun Zhong, Ruixiang Cui, Yiduo Guo, Yaobo Liang,
Shuai Lu, Yanlin Wang, Amin Saied, Weizhu Chen,
and Nan Duan. 2024. Agieval: A human-centric
benchmark for evaluating foundation models. In
Findings of the association for computational linguis-
tics: NAACL 2024, pages 2299–2314.
Shuyan Zhou, Frank F Xu, Hao Zhu, Xuhui Zhou,
Robert Lo, Abishek Sridhar, Xianyi Cheng, Tianyue
Ou, Yonatan Bisk, Daniel Fried, and 1 others.
2023. Webarena: A realistic web environment
for building autonomous agents.arXiv preprint
arXiv:2307.13854.
8

Appendix
A Prompt Templates
This appendix presents the complete prompt tem-
plates used in AD-Bench for the agent system, re-
port generation, and two-stage error analysis. Each
prompt is shown verbatim (translated to English)
to ensure full reproducibility.
A.1 Agent System Prompt
The following prompt which defines the core sys-
tem instruction for the advertising analytics agent
is shown in Figure 6, including tool descriptions
and output constraints.
A.2 Report Generation Prompt
This prompt shown in Figure 7 instructs the agent
to generate a structured analytical report given data
context and the user’s query.
A.3 Error Analysis: Stage 1 Prompt
The Stage 1 prompt shown in Figure 8 and 9 per-
forms a rapid assessment of result correctness, tra-
jectory coverage, instruction compliance, parame-
ter errors, redundant calls, and dependency viola-
tions.
B Real-World Deployment:
Benchmark-Guided Iteration
Beyond one-off offline evaluation, AD-Bench is
deployed as a continuous evaluation harness for
a production advertising-analytics agent. Each
candidate version is scored on AD-Bench, and its
trajectory-level diagnostics localize concrete fail-
ure modes that directly inform the next iteration.
We track real-world impact with an online user sat-
isfaction rate—the fraction of thumbs-up collected
from a crowd-sourced evaluation. As shown in
Table 4, benchmark-guided iteration steadily im-
proves this metric from 65.55% to 88.37% over
three versions. Crucially, the online satisfaction
rate moves in lockstep with the agent’s overall ac-
curacy on AD-Bench, which rises from 57.62% to
70.22% over the same versions, confirming that
gains diagnosed on AD-Bench translate into a bet-
ter user experience in production.
C Tool Inventory
The advertising analytics agent is equipped with
nine tools shown in Table 5.
Metric (%) V1 V2 V3
AD-Bench Pass@1 57.62 63.9970.22
Online user satisfaction 65.55 84.4588.37
Table 4: Benchmark-guided iteration of a production
advertising-analytics agent across successive versions.
Improvements on AD-Bench track closely with the on-
line user satisfaction rate (thumbs-up ratio from a crowd-
sourced evaluation), which rises to88.37%.
Figure 5 shows a typical tool invocation tree. The
agent begins with the user query, then issues
parallel calls to retrieve domain knowledge, re-
solve account scope, and fetch peer benchmarks
(Round 2). Subsequent rounds depend on earlier
results: ad-level configuration requires account res-
olution (Round 3), data retrieval requires ad con-
text (Round 4), computation integrates all prior
outputs (Round 5), and the final report is generated
(Round 6).
D Case Studies Across Difficulty Levels
To illustrate the progressive complexity of AD-
Bench, we present three representative cases solved
by Gemini-3.1-Pro, one from each difficulty level.
All account IDs and user IDs are anonymized. Fig-
ure 10 provides a side-by-side comparison of the
three cases, highlighting the escalating demands in
tool usage and reasoning depth.
E Error Analysis Examples
Using the L3 case as a reference, Figure 11 illus-
trates four representative error patterns observed
during LLM agent evaluation. Each subplot pairs
the ground-truth trajectory (left, green) with an
erroneous trajectory (right), with error steps high-
lighted:E1tool & parameter errors,E2instruction-
following errors,E3retrieval failure & hallucina-
tion, andE4computation & post-processing errors.
9

Tool Description
get_user_account_list Retrieve the list of authorized advertising accounts for a given
user, including account ID, company name, industry, and last
consumption date.
get_account_info Fetch account metadata: company name, industry, daily budget,
audit status, and audit reason.
get_account_adgroup_info Fetch ad-level configuration: ad name, status, schedule, targeting,
bid, placement, and marketing objective.
daily_data_by_group_and_field Fetch daily-granularity report data (cost, clicks, impressions,
CTR, conversions, etc.) with flexible grouping dimensions (date,
account, ad, creative, region, etc.).
hourly_data_by_group_and_field Fetch hourly-granularity report data for a single specified day,
supporting grouping by hour, ad, or creative.
search Retrieve domain knowledge, best practices, and industry bench-
marks via keyword query.
calculator Execute Python code snippets for arithmetic and statistical com-
putation on retrieved data.
get_top_good_creative Fetch top-performing peer creatives from the past 3 days by
industry, placement, and creative type.
summarize_results Terminate the session and summarize findings; mark the query
as resolved or unresolved.
Table 5: Tool inventory of the advertising analytics agent.
User Query
natural-language question
R1
search
domain knowledge
get_user_account_list
resolve accounts
get_top_good_creative
peer benchmarks
R2
get_account_adgroup_info
ad-level configuration
R3
requires account
daily_data_*
daily metrics
hourly_data_*
hourly metrics
R4
calculator
compute & analyze
R5
summarize_results
output report
R6
Figure 5: A typical tool invocation tree. Solid arrows
indicate direct dependencies; dashed arrows indicate
indirect dependencies (domain knowledge and bench-
marks feed into computation).
10

Agent System Prompt
You are an advertising marketing assistant, specializing in decomposing complex data query tasks
into specific tool calls to retrieve data, providing users with precise marketing data.
Core Task
1. Analyze the user’s request and conversation history, plan the data needed at the current stage, and
execute tool calls accordingly.
Output Requirements
1. Responses must include planning and tool calls. Output the following tags:
<plan>PLAN: </plan>What objective information the current step expects to collect.
<tools></tools>List of tool calls.
2.<plan>format:
<plan>
PLAN: Describe the current step goal and what information to collect.
</plan>
3.<tools>format (strict):
<tools>
<tool>
TOOL_NAME: tool_name
INPUT: tool input (JSON)
</tool>
</tools>
Note: Each turn outputs one <tools> block. Nest multiple <tool> for parallel calls. Results
appear in<tool_res>...</tool_res>.
Working Rules
1. Answer based on the user’s account data, providing customized solutions.
2.<plan>specifies what information to collect;<tools>implements the plan.
3. Multiple queries can nest multiple<tool>blocks. ‘#’ comments are prohibited in INPUT.
4. For unavailable data/parameters, usesummarize_resultsto indicate inability to retrieve.
5. If no specific account is mentioned, analyze all accounts with permissions.
6. All authorized accounts must be obtained from get_user_account_list with full
account_id_list.
7. Calculator results must useprint().
8. “Last week” refers to last Monday through last Sunday.
Available Tools
•search– Knowledge retrieval (query: str, max 20 chars)
•daily_data_by_group_and_field– Daily-granularity report data
(user_id,begin,end,group_by_type,fields,account_id_list,page_size, . . . )
•hourly_data_by_group_and_field– Hourly-granularity report for a specific date
(user_id,date,group_by_type,fields,page_size, . . . )
•calculator– Execute business computation code (code: str)
•get_account_info– Account basic info (user_id,account_id_list)
•get_account_adgroup_info– Ad group info (user_id,account_id,adgroup_id_list)
•get_user_account_list– List of authorized accounts (user_id,page_size, . . . )
•summarize_results– Summarize results (query: “Resolved”|“Unresolved”)
•get_top_good_creative– Top peer creatives (industry,site_set,creative_type)
Figure 6: Agent system prompt for the advertising marketing assistant. The agent decomposes user queries into
structured planning and tool-call sequences.
11

Report Generation Prompt
You are an advertising data analyst. Based on the user’s question and the data context, summarize
the situation and provide a direct, precise answer to the data metrics the user cares about, strictly
following the user’s requirements.
Output Requirements
1. Output data directly without scientific notation or comma-separated formats.
2. Round to two decimal places (e.g., 0.11 and 0.1091 are the same).
3. Analyze and answer based on the user’s question, not indiscriminate summarization.
4. For knowledge-based Q&A, provide a brief explanation of 10–20 words.
Input
User Question:{query}
Data Context:
<context>
{context}
</context>
Figure 7: Prompt template for report generation. The LLM analyst synthesizes tool-returned data into a precise,
user-facing answer.
12

Error Analysis Stage 1: Correctness and Coverage Prompt
Evaluate the execution quality of the following advertising analytics case.
Available Tools and Dependencies
Independent Tools(no dependencies, can be called directly)
1.search– Retrieve advertising/marketing domain knowledge
• Parameters:query(required, max 20 chars)
• Dependencies: None
2.get_top_good_creative– Get top-performing creatives from the platform
• Parameters:query(filter description: industry/placement/creative type/keywords)
• Dependencies: None
3.get_user_account_list– Get all account IDs under the user
• Parameters:user_id(required),page_size
• Returns: Account ID list
• Dependencies: None (but is a prerequisite for data query tools)
Data Query Tools(requireaccount_id)
4.daily_data_by_group_and_field– Daily-granularity report data
• Parameters: user_id, begin, end, group_by_type, fields, account_id_list, page_size,
adgroup_id(opt.),order_by(opt.)
•group_by_type : SUM / DATE / MONTH / WEEK / SITE_SET / ADGROUP_ID / AC-
COUNT_ID / CREATIVE_ID / MATERIAL_VIDEO / MATERIAL_IMAGE / MARKET-
ING_ASSET / GENDER / AGE / REGION / CITY
•fields : cost / valid_click_count / view_count / ctr / cpc / conversions_cost / conversions_count
/ conversions_rate / deep_conversions_count / deep_conversions_rate / deep_conversions_cost
• Dependencies: Requiresaccount_id_list(fromget_user_account_list)
5.hourly_data_by_group_and_field– Hourly-granularity report for a specific date
• Parameters: user_id, date, group_by_type, fields, page_size, account_id_list (opt.),
adgroup_id(opt.),order_by(opt.)
•group_by_type : SUM / HOUR / ACCOUNT_ID / ADGROUP_ID / AD-
GROUP_ID_AND_HOUR / CREATIVE_ID / CREATIVE_ID_AND_HOUR
• Dependencies: Requiresaccount_id_list(fromget_user_account_list)
6.get_account_info– Get account basic information
• Parameters:user_id,account_id_list
• Returns: Account name, industry, daily budget, review status, etc.
• Dependencies: Requiresaccount_id_list
7.get_account_adgroup_info– Get ad group list / ad details
• Parameters:user_id,account_id,adgroup_id_list(opt.)
• Returns: Ad name, status, dates, bid, budget, targeting, placement, etc.
• Dependencies: Requiresaccount_id
Computation Tool
8.calculator– Write Python code to compute business metrics
• Parameters:code(required)
• Dependencies: Usually requires data to be fetched first
• Note: Return field names are like “Cost (CNY)”, “Click Count”, “Target Conversions”, etc.
Figure 8: Prompt template for Stage 1 error analysis (Part 1: Tool Definitions). Lists all available tools, their
parameters, and dependency requirements.
13

Error Analysis Stage 1: Correctness and Coverage Prompt (cont.)
Tool Dependency Graph
search / get_top_good_creative (independent, callable anytime)
get_user_account_list (prerequisite for data queries)
|-> daily_data_by_group_and_field (needs account_id_list)
|-> hourly_data_by_group_and_field (needs account_id_list)
|-> get_account_info (needs account_id_list)
|-> get_account_adgroup_info (needs account_id)
|-> daily_data/hourly_data (can query by adgroup_id)
After data retrieval -> calculator (perform computation)
Common Error Patterns
• Calling tools that requireaccount_idwithout first callingget_user_account_list
• Mixing updaily_dataandhourly_data(different granularity scenarios)
• Incorrectgroup_by_type(e.g., using SUM when aggregation by account is needed)
• Redundant calls toget_user_account_list
• Wrong field names in calculator (e.g., using “cost” instead of “Cost (CNY)”)
User Query:{query}
Ground-Truth Answer:{ground_truth}
Expected Trajectory:{expected_trajectory}
Actual Trajectory:{trajectory}
Model’s Final Answer:{final_answer}
Based on the tool definitions and dependency relationships, respond in the following JSON format
only (no other content):
{
"result_correct": true/false, "trajectory_covered": true/false,
"has_instruction_violation": true/false, "has_error_parameters": true/false,
"has_redundant_calls": true/false, "has_dependency_error": true/false,
"brief_reason": ""
}
Field descriptions:
•result_correct : Whether the model’s answer matches the ground truth (format differences like
thousands separators or units are acceptable)
•trajectory_covered : Whether the actual trajectory covers all necessary tool calls in the expected
trajectory
•has_instruction_violation: Whether there are turns with no tool calls (status “no tool call”)
•has_error_parameters : Whether parameters are incorrect (e.g., target is ad ID but parameter is
filled with account ID; target is conversions but parameter is cost)
•has_redundant_calls : Whether there are unnecessary repeated calls (previously called tools
forgotten)
•has_dependency_error: Whether tool dependency relationships are violated (e.g., calling tools
that needaccount_idwithout first obtaining it; calling calculator without fetching data first)
•brief_reason: Reasoning for the judgment (max 50 words)
Figure 9: Prompt template for Stage 1 error analysis (Part 2: Dependency Graph, Error Patterns, and Evaluation
Output). The LLM judge evaluates execution correctness, trajectory coverage, instruction compliance, parameter
accuracy, redundancy, and dependency violations.
14

Level 1 Simple Data Retrieval 2 tools  |  3 rounds  |  54s  |  PASS
QUERY
Get the total number of deep conversions across all accounts for the past 7 days.
1 get_user_account_list Retrieve 155 authorized accounts
2 daily_data_by_group_and_field Query aggregated deep conversions (SUM) -> 16,931
3 summarize_results Report: total deep conversions = 16,931
ANSWER Total deep conversions (7 days): 16,931
Direct aggregation -- no intermediate computation needed.
Level 2 Conditional Counting + Computation 3 tools  |  4 rounds  |  80s  |  PASS
QUERY
Count how many days in the past 30 days had total daily cost exceeding 3,000,000.
1 get_user_account_list Retrieve 155 authorized accounts
2 daily_data_by_group_and_field Query daily cost grouped by DATE (30 records)
3 calculator Iterate records, count days where cost > 3M -> 23
4 summarize_results Report: 23 out of 30 days exceeded threshold
ANSWER Days with cost > 3M: 23 / 30
Requires conditional filtering + counting via code execution.
Level 3 Multi-source Reasoning + Knowledge Retrieval 4 tools  |  5 rounds  |  102s  |  PASS
QUERY
Analyze whether video and image creatives of account acct_076 both meet the excellence threshold yesterday.
1 get_user_account_list Retrieve 155 authorized accounts, verify acct_076
2 search Retrieve industry benchmark: CTR excellence threshold = 5%
3 daily_data_by_group_and_field Fetch video + image click/impression data (2 calls)
4 calculator Video CTR=6.29% PASS, Image CTR=5.35% PASS
5 summarize_results Report: both creative types meet the threshold
ANSWER Yes -- Video 6.29% PASS, Image 5.35% PASS
Requires knowledge retrieval, parallel data fetching, dual CTR computation, and comparison.
Figure 10: Overview comparison of three representative cases across difficulty levels. L1 requires direct retrieval; L2
adds conditional computation; L3 demands knowledge retrieval, parallel data fetching, and dual-metric verification.
15

E1: Tool & Parameter Errors
Ground Truth Error Pattern
1
get_user_account_li..
Verify acct_076
2
search
Threshold = 5%
3
daily_data_*
Fetch video+image
4
calculator
CTR: 6.29%, 5.35%
5
summarize_results
Both PASS
 CORRECT
1
daily_data_*
No acct verify
2
search
Threshold = 5%
3
calculator
7-day avg
4
summarize_results
Wrong result
 WRONG
Root cause: Skipped account verification; wrong date range (7-day vs yesterday)
E2: Instruction-Following Errors
Ground Truth Error Pattern
1
get_user_account_li..
Verify acct_076
2
search
Threshold = 5%
3
daily_data_*
Fetch video+image
4
calculator
CTR: 6.29%, 5.35%
5
summarize_results
Both PASS
 CORRECT
1
get_user_account_li..
Verify acct_076
2
search
Threshold = 5%
3
daily_data_*
Fetch video only
4
calculator
CTR: 6.29%
5
summarize_results
Video PASS only
 INCOMPLETE
Root cause: Ignored explicit 'both video and image' request; analyzed video only
E3: Retrieval Failures & Hallucination
Ground Truth Error Pattern
1
get_user_account_li..
Verify acct_076
2
search
Threshold = 5%
3
daily_data_*
Fetch video+image
4
calculator
CTR: 6.29%, 5.35%
5
summarize_results
Both PASS
 CORRECT
1
get_user_account_li..
Verify acct_076
2
search
'what is excellent'
3
daily_data_*
Fetch video+image
4
calculator
Compare vs 3%
5
summarize_results
Both PASS (wrong)
 WRONG
Root cause: Vague search query; hallucinated 3% threshold (correct: 5%)
E4: Computation & Post-processing Errors
Ground Truth Error Pattern
1
get_user_account_li..
Verify acct_076
2
search
Threshold = 5%
3
daily_data_*
Fetch video+image
4
calculator
CTR: 6.29%, 5.35%
5
summarize_results
Both PASS
 CORRECT
1
get_user_account_li..
Verify acct_076
2
search
Threshold = 5%
3
daily_data_*
Fetch video+image
4
calculator
view/click inverted
5
summarize_results
1589% PASS?!
 WRONG
Root cause: CTR formula inverted: view_count/click_count  1589%
Error Analysis: L3 Case Study
Query: "Analyze whether video and image creatives of acct_076
both meet the excellence threshold yesterday."
Figure 11: Error analysis of the L3 case. Each subplot pairs the correct trajectory (left) with one error pattern (right).
Error steps are marked with ✗. E1: tool & parameter; E2: instruction-following; E3: retrieval & hallucination; E4:
computation & post-processing.
16
