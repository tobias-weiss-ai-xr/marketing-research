---
title: 'Fisher-R1: Training LLM Agents for Reliable Hypothesis Testing'
url: https://arxiv.org/abs/2608.07437
category: ai-marketing
subcategory: empirical
date: 2026-08
venue: ''
authors:
- Jiacheng Miao
- Jin Mu
- Guanhua Chen
- James Zou
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.07437
pages: 26
chars: 65984
fetched_at: '2026-11-08T13:34:00+00:00'
kb_version: 1
---

# Fisher-R1: Training LLM Agents for Reliable Hypothesis Testing

Fisher-R1: Training LLM Agents for Reliable
Hypothesis Testing
Jiacheng Miao1,2,*, Jin Mu3,*, Guanhua Chen3,4, and James Zou1,5,6
1Department of Biomedical Data Science, Stanford University
2Department of Genetics, Stanford University
3Department of Biostatistics and Medical Informatics, University of Wisconsin–Madison
4Department of Statistics, University of Wisconsin–Madison
5Department of Electrical Engineering, Stanford University
6Department of Computer Science, Stanford University
*These authors contributed equally to this work
Code
Abstract
Reliable hypothesis testing is the foundation of many empirical scientific claims.
Large language model (LLM) agents are increasingly used to automate this process,
as they can inspect datasets, generate code, and produce analyses end-to-end. How-
ever, we show that they frequently make subtle inferential errors that lead to incorrect
conclusions despite correctly executed analyses. Existing benchmarks fail to capture
this failure mode, as they rarely assess whether a reported p-value is statistically valid
given the assumptions underlying the data. We address this gap by buildingP-Bench,
a benchmark comprising 425 open-ended, realistic hypothesis-testing tasks spanning
economics, biology, and medicine. Each task requires an agent to select a statistical
method, compute a p-value, and draw a conclusion given only a scientific hypothe-
sis and a dataset. We further introduceFisher-R1, an open-weight LLM agent trained
for rigorous hypothesis testing using synthetic tasks and reinforcement learning. On
P-Bench, Fisher-R1-14B substantially improves over its backbone andoutperforms
strong proprietary and open-source baselines, including GPT-5.4 and DeepSeek-
V4-Pro, achieving a 21% average relative improvement in single-trial success over
DeepSeek-V4-Pro, with gains up to 26% on the most challenging tasks. Our results
demonstrate that current LLM agents lack reliable statistical reasoning for hypothesis
testing and that reinforcement learning on tasks with verified statistical reward sub-
stantially improves reliability.
1 Introduction
Many areas of empirical science follow a common workflow: a researcher begins with a scientific
question and a dataset, translates the question into a testable hypothesis, selects an appropri-
ate statistical test, computes a p-value, and then draws a conclusion [1]. This hypothesis-testing
framework appears in high-stakes settings across disciplines, from medicine to economics. For ex-
ample, in clinical trials, researchers test whether a new treatment is more effective than a placebo,
while in economics, policymakers evaluate whether interventions such as minimum wage in-
creases affect employment outcomes. The method must match the question and data; otherwise,
a precise p-value can support the wrong scientific conclusion.
Large language model (LLM) coding agents can now execute much of the empirical workflow:
1
arXiv:2608.07437v1  [cs.AI]  7 Aug 2026

Use dataset: dataset.csv. Test whether mutation burden is associated with tumor purity.
Report the statistical method, p-value, and conclusion.
GPT-5.4 False discovery
mutation burden
tumor purity
2 outliers
Trace
sees Spearman p = 0.085 (not significant)
sees linear regression has warning signs
but sayskeeps linear regression anyway
"Despite this, the linear association test
supports a positive association."
Answer
Method linear regression test
Conclusion p < 2.2e-16 -> Reject null hypothesis
Fisher-R1 Correct inference
ranked mutation burden
ranked tumor purity
outliers compressed by ranking
Trace
sees outliers: tumor purity reaches 2.47
sees linear looks strong; rank looks weak
so saysuses rank test as main answer
"Given non-normality and outliers,
Spearman rank correlation is appropriate."
Answer
Method Spearman rank test
Conclusion p = 0.085 -> Fail to reject null
 Prompt:
P−Bench (Easy)
0 20 40 60 80 100
Fisher−R1−14B
Fisher−R1−7B
GPT−5.4
GPT−OSS−120B
DeepSeek V4 Pro
Qwen3−32B
Qwen2.5−14B
Qwen2.5−7B
64.2
65.7
64.7
26.3
54.2
46.1
41.4
36.3
P−Bench (Hard)
0 20 40 60 80 100
Fisher−R1−14B
Fisher−R1−7B
GPT−5.4
GPT−OSS−120B
DeepSeek V4 Pro
Qwen3−32B
Qwen2.5−14B
Qwen2.5−7B
Accuracy (%)
33.0
30.6
30.5
18.2
26.3
27.2
23.7
13.2
Figure 1:Open-ended hypothesis testing with coding agents.Left: GPT-5.4 identifies outliers
but still applies linear regression, leading to a false discovery. Fisher-R1 instead uses a rank-based
test and correctly fails to reject the null. Right: P-Bench accuracy on easy and hard splits.
inspecting datasets, generating code, running analyses, and drafting reports [2–4]. However, hy-
pothesis testing is not merely code execution. Consider a cancer genomics task testing whether
mutation burden is associated with tumor purity. The dataset contains a few high-leverage out-
liers: a linear analysis reports a highly significant association driven by these points, whereas a
rank-based test does not. As shown in Figure 1, a frontier LLM agent recognizes these warn-
ing signs yet proceeds with linear regression, producing runnable code and a fluent but incorrect
conclusion. In contrast, a Spearman test correctly fails to reject the null.
This example highlights how LLM agents can generate technically valid analyses while mak-
ing flawed inferential choices that lead to false discoveries. Existing evaluations do not directly
measure this ability. General data-analysis benchmarks [5–8] often reward a plausible answer or
an executable workflow, but they rarely isolate the inferential method itself: which test was exe-
cuted, whether the reported p-value is grounded in that execution, and whether the conclusion
follows from the computed evidence. The gap is especially consequential for open-ended scien-
tific discovery, where agents may search many datasets and hypotheses, and for private scientific
and medical data, where reliable local or open-weight agents are needed.
Closing this evaluation gap requires verified statistical tasks: a scientific question, a dataset,
an executable analysis, and a checked answer key for the method, p-value, and conclusion. Such
tasks are scarce. Papers report selected results, public datasets require cleaning, and statistical
methods are not packaged as machine-checkable targets.
To address this gap, we introduceP-Bench(P-value Bench), a benchmark of 425 open-ended
hypothesis-testing tasks built on real scientific data. Each task gives an agent a scientific question,
a dataset, and a data description. The agent must choose a statistical method, execute the anal-
ysis, report a p-value, and draw a conclusion. Tasks are drawn from peer-reviewed economics
and biology papers and from authoritative biostatistics teaching materials. Every answer key is
2

grounded in a logged execution of the canonical reference analysis and audited by domain ex-
perts. To make this construction tractable, we use an automated reproducibility pipeline that links
each published claim to its dataset and analysis code. The pipeline is described in the appendix.
We further trainFisher-R1, an open-weight LLM agent for rigorous hypothesis testing. To
enable training at scale, we design a synthetic task generator that produces realistic hypothesis-
testing scenarios with verified answer keys. Fisher-R1 is trained on these tasks with supervised
fine-tuning followed by reinforcement learning. On P-Bench, Fisher-R1-14B outperforms strong
proprietary and open-source baselines, including GPT-5.4 and DeepSeek-V4-Pro.
To summarize, our contributions are:
• We introduceP-Bench, an expert-verified, executable benchmark of 425 open-ended hypothesis-
testing tasks on real scientific data, evaluating LLM agents on p-value accuracy and conclu-
sion correctness.
• We trainFisher-R1, an open-weight hypothesis-testing agent, using synthetic executable
tasks and outcome-grounded reinforcement learning. Fisher-R1 substantially improves over
its backbone and outperforms GPT-5.4 and DeepSeek-V4-Pro on P-Bench.
2 Problem Formulation
2.1 Settings
We consider open-ended hypothesis testing with LLM coding agents. Each task gives the agent a
scientific questionq, a datasetD, and a data descriptions, but not the statistical method. Given
x= (q,D,s), the agent must choose a method, execute the analysis, return a p-value ˆp, and a
decision ˆδ, where ˆδindicates whether to reject the null hypothesis at a pre-specified significance
level.
Evaluation compares the agent output with a hidden answer keyk
∗
= (p
∗
,δ
∗
). The agent inter-
acts with an R environment through a multi-turn loop, reflecting the statistical software ecosystem
used in many empirical analyses and providing a fixed execution backend for evaluation. At step
t, the history ish t = (x,a 1,o 1, . . . ,at−1,o t−1), wherea i is an agent action ando i is the correspond-
ing environment observation. An action may contain R code, an intermediate analysis decision,
or the final answer. The environment executes code actions and returns observations such as data
summaries, warnings, model outputs, diagnostics, test statistics, and p-values. The completed
trajectory is
τ∼π θ(· |x),
whereτincludes both the executed code trace and the final report. At evaluation time, we parse
τto compare the reported p-value and the final decision withk
∗
.
2.2 Related works
LLM agents for data analysis and statistical reasoning.Recent work has evaluated LLM agents
that write code, inspect data, execute programs, and iteratively revise their solutions, building
on the ReAct paradigm of interleaved reasoning and tool use [9]. A substantial body of data-
analysis benchmarks evaluates whether such agents can answer factoid queries about a dataset
(e.g., “what is the mean ofX?”) or build predictive models on tabular data through executable
workflows [6, 7, 10–15]. These benchmarks score the executability of the workflow and the exact-
match correctness of a final factoid or model accuracy, but they neither require nor verify that the
3

chosen statistical procedure is valid for the data at hand. A complementary line, exemplified by
StatQA, asks whether LLMs can select an appropriate statistical procedure in a multiple-choice
format, without executing the analysis with code [8]. P-Bench targets a regime that neither cap-
tures the full open-ended hypothesis-testing loop, method selection, executed analysis, p-value,
nor the reject/fail-to-reject decision, and is evaluated against an answer key derived from the
canonical reference analysis on real scientific data.
Scientific claim verification and reproducibility.Scientific claim verification has been studied
as an evidence-retrieval and textual-entailment problem: SciFact asks models to verify scientific
claims against evidence-containing abstracts and supply supporting rationales [16], with follow-
on benchmarks scaling this to larger and multimodal corpora [17, 18]. This line evaluates whether
claims are supported or refuted by the literature, but does not reconstruct the underlying statistical
analysis. Large-scale replication efforts such as SCORE further show that re-running and checking
empirical claims is important but costly, requiring substantial human effort to assess robustness
and test replicability [19]. These efforts target manuscript-level verification of whether published
numbers can be reproduced. In contrast, P-Bench evaluates the upstream act of inference itself:
given the same data and question, does the agent select a method that yields a statistically valid
p-value?
Autonomous research agents.A recent line of work pursues end-to-end autonomous scientific
discovery, with LLM agents that propose hypotheses, generate code, run experiments, and draft
manuscripts [20–22]. The reliability of such pipelines is, however, bounded by the statistical rea-
soning of the underlying agent at every stage. As our P-Bench experiments show, current LLM
agents may make subtle inferential errors even on well-defined hypothesis-testing tasks, under-
mining the validity of any conclusion drawn downstream and casting doubt on whether fully
autonomous end-to-end discovery is presently achievable. Fisher-R1 directly targets this bottle-
neck.
3 P-Bench
P-Bench is a benchmark of open-ended hypothesis-testing tasks built from real scientific data
spanning economics, biology, and medicine. Each task is anchored to a statistical claim from a
high-quality source, such as peer-reviewed top scientific journals and canonical course notes, so
the answer key reflects a hypothesis test that domain experts have already computed and acted
on.
3.1 Task Formulation
A P-Bench task provides the agent with (Figure 2): (i) an analysis request describing a scientific
question and the associated data, and (ii) a dataset in CSV format. The agent must explore the
data, write and execute R code in a logged sandbox environment, and return a structured output
consisting of a selected statistical method, ap-value, and a reject/fail-to-reject decision. Impor-
tantly, the task does not prescribe a statistical method. Instead, the agent must autonomously
select an appropriate analysis strategy, and its output is evaluated against a hidden answer key
comprising thep-value, and a decision derived from the canonical analysis.
4

Task Architecture
Given to agent
Execution Sandbox
R code
> df <- read.csv("dataset.csv")
> summary(df$mutation_count)
   Median     Mean      Max
    289      850   15,981
> cor.test(df$age, df$mutation_count,
           method = "pearson")
Pearson correlation
r = 0.134,  p-value = 0.011
Answer
method    Pearson correlation
p-value   0.011
decision  reject H0
Evaluation
Ground truth vs Agent
p-value conclusion
ground truth 0.053 fail to reject
agent 0.011 reject H0
Question: Is patient age associated with
somatic mutation burden in cutaneous
melanoma?
Study design:
Type: Observational cancer genomics cohort
Unit of observation: Melanoma case in the
TCGA SKCM study
analysis_request.txt
dataset.csv
age mutation_count
⋮ ⋮
n = 361 rows
p-value closeness
conclusion correctness
✗
Accuracy
Figure 2: A P-Bench task is composed of an analysis request, a CSV dataset, and a hidden answer
key derived from the canonical reference analysis. The agent writes and executes R code inside a
logged sandbox and returns a chosen statistical method,p-value, and reject/fail-to-reject decision,
which are then compared against the answer key.
3.2 Dataset Construction and Verification
P-Bench is built from three high-quality source families: economics papers in top journals with
datasets hosted on Harvard Dataverse [23], peer-reviewed biology papers with datasets hosted
on cBioPortal[24–26], and authoritative teaching materials from Vanderbilt Biostatistics[27] with
datasets distributed through R packages. Each task is derived from a real scientific analysis orig-
inally conducted by domain experts. To ensure diversity and balance, we first collected a broad
pool of candidate tasks and randomly sampled from them to construct an evenly distributed
benchmark. We also introduced controlled perturbations to the datasets to better reflect the noise,
inconsistencies, and irregularities commonly encountered in real-world data analysis.
Starting from statistical claims extracted from the sources, we applied a three-stage pipeline:
(1) reproduce the reference analysis on a clean machine and log the execution; (2) filter out anal-
yses that could not be reproduced, and ground each remaining claim in the execution log; and
(3) generate a self-contained executable task paired with a structured answer key in the P-Bench
format. As a result, every released task is reproducible, traceable to an executed reference run,
and self-contained.
P-Bench tasks and their answer keys are trustworthy by construction: keys are computed from
canonical reference code (not transcribed from paper text), cross-validated against the published
claim, and every task is audited by domain experts. (i) Reproducible execution. Everyp-value,
test statistic, and decision is read off a logged run of canonical reference code: a deposited replica-
tion script for economics, a methods-section re-implementation on the released tables for biology,
or the published course-notes analysis for biostatistics. (ii) Expert review. Reviewers trained in
statistics and biostatistics independently audit each finalized task, verifying that the analysis re-
quest, released data subset, and answer key all align with the source; tasks failing review are
repaired or removed.
5

3.3 Composition
After verification, P-Bench contains425high-quality open-ended hypothesis-testing tasks, strati-
fied into Easy (203) and Hard (222) splits using deterministic, metadata-only rules: a task is Hard
if it belongs to a reference-method family that requires careful model specification and assump-
tion checking (e.g., Cox regression, IV/2SLS, Tobit model) or it carries an adversarial data-quality
perturbation. Several properties make P-Bench distinctive:
Diverse and realistic methods.P-Bench covers17hypothesis-testing method categories span-
ning commonly used tests (t-test,χ 2, OLS coefficient test, Fisher exact test) and specialized meth-
ods routinely used in real published analyses (e.g., Cox proportional-hazards regression, IV / 2SLS
estimators, mixed-effects models, log-rank tests, Mann–Whitney, Tobit model, probit model).
Figure 3: Task Composition of P-Bench
No single category exceeds 19%, so an agent
cannot succeed by defaulting to a fixed recipe.
Cross-domain coverage.Tasks span eco-
nomics, biology, and medicine, covering both
randomized experiments and observational
studies. Each setting has its own modeling as-
sumptions and inferential targets, so an agent
must transfer statistical reasoning across disci-
plines.
Realistic statistical traps.P-Bench con-
tains adversarial data-quality and assumption-
checking traps, including outliers, heteroskedas-
ticity, and clustered observations, where naive
methods yield confident-but-wrong results.
These are textbook assumption violations that arise routinely in real-world data and that any
trained statistician is expected to detect and handle.
4 Fisher-R1 Training
4.1 Synthetic Data
We train on synthetic tasks with executable data-generating processes, known target analyses,
and programmatically checkable answer keys. To generate each task, we use an LLM to write
both the simulation code (which produces the dataset) and the accompanying analysis question.
The simulation runs the canonical statistical method on its own simulated data, and the resulting
p-value, decision, and method label form the answer key. This gives us a scalable, verified reward
signal for RL, which is the bottleneck for training on real, published data. By construction, it also
keeps P-Bench fully out of the training set, allowing us to test out-of-distribution generalization.
Task taxonomy.Each training task is generated by combining six independent factors: a statis-
tical method (M), a domain scenario (S m), a sample size (N), an effect size (E), a prompt style (P),
and a random seed (K). Formally, the task taxonomy is the Cartesian grid
M|{z}
method
×S m|{z}
scenario
×N |{z}
sample size
×E |{z}
effect size
×P |{z}
prompt style
×K|{z}
seed
,
6

Expert trajectory collection for SFT
4.6 k
Instances
Open-ended
hypothesis testing
AI model
(Claude)
samples   Quality control 3.8 k
trajectories
Thought Code Observation Answer
RL Training
SFT Warm Start
from expert
trajectories
8.6 K
Tasks
Open-ended
hypothesis testing
Policy
model
<think> Let me start by explore the data </think>
<code> summary(data) </code>
<observation> max = 42.1, median = 3.8 </observation>
<answer> P-value = 0.051, Conclusion = reject </answer>
RL loss
Executable environment
rollout
Rule–based reward
P-value
closeness Conclusion
Feedback
Figure 4:Top: Expert trajectories are collected for SFT. The model generates reasoning traces
containing thoughts, code, observations, and final answers; quality control filters for high-quality
trajectories.Bottom: The policy is initialized from the SFT model and optimized with RL. During
rollout, it interacts with an executable environment to generate trajectories. Rule-based rewards
score p-value accuracy and conclusion correctness.
Each method is paired with multiple domain scenarios that wrap a shared data-generating pro-
cess in different realistic study descriptions. Effect size takes one of three regimes (null, borderline,
medium); the borderline regime is auto-calibrated by simulation, so tasks fall in a genuinely am-
biguous significance range. Prompt style controls whether the question states only the research
question (non-hint) or additionally flags a methodologically relevant feature of the data, such as
endogeneity or clustering (hint). Sample size and seeds are varied for coverage and reproducibil-
ity. Full per-axis level lists, the end-to-end generation pipeline, and example tasks are given in
Appendix C.2.
On top of the clean grid, we add data-quality perturbations such as missing values and extreme
or invalid observations. These test whether the agent notices and handles problematic data instead
of applying an analysis mechanically. The full corpus contains 8,642 tasks with balanced coverage.
4.2 Supervised Fine-tuning
We warm-start the policy model with supervised fine-tuning on teacher-generated analysis trajec-
tories. The teacher trajectories are generated by Claude-Sonnet-4.6 [28] on a randomly sampled
subset of synthetic tasks, yielding 4,611 trajectories in total. For every task, the teacher follows
a fixed five-step workflow: (i) basic exploratory data analysis (EDA) (data shape, column types,
variable roles); (ii) detailed EDA (distributions, missingness, balance, correlations); (iii) assump-
tion checking tailored to the candidate method (e.g., normality, proportional hazards, instrument
strength, parallel trends); (iv) method selection and analysis; and (v) conclusion.
We then apply automatic quality control. A trajectory is retained only if it produces a valid
multi-turn trace and a parseable conclusion. It must also match the ground-truth reject/fail-to-
7

reject decision. When ap-value is reported, it must agree with the answer key in significance
atα=0.05 and within one order of magnitude. We further remove teacher-only metadata and
any answer-key leakage from training prompts and targets. After filtering, we keep 3851/4611≈
83.5% of trajectories for SFT.
Each trajectory is formatted in ReAct (CodeAct) style [9, 29], with the same<think>,<code>,
<observation>,<answer>tags as the RL environment. Only assistant turns are optimized; user
prompts and tool observations are provided as context. LetDSFT ={(x i,y i)}n i=1 denote the filtered
trajectory set, wherex i is the task prompt andy i = (yi,1, . . . ,yi,Ti )is the teacher response sequence.
We minimize the masked autoregressive negative log-likelihood
LSFT(θ) =− 1 ∑i ∑t mi,t n ∑ i=1 Ti ∑ t=1 mi,t logπ θ(yi,t |x i,y i,<t ),
wherem i,t =1 for assistant tokens and 0 for prompt and observation tokens.
4.3 Reinforcement Learning
Algorithm.Starting from the SFT-initialized policyπ θ, we use the Decoupled Clip and Dynamic
Sampling Policy Optimization (DAPO) algorithm [30] . For each promptq, we sample a group of
Gmulti-turn rollouts{o i}G i=1 ∼π θold(· |q)and score each rollout with the Fisher rewardR(o i).
The group-relative advantage is
ˆAi = R(oi)−µ q σq +ϵ ,µ q = 1 G G ∑ j=1 R(o j),σ 2 q = 1 G G ∑ j=1 (R(o j)−µ q)2.
For rollouto i = (yi,1, . . . ,yi,Ti ), whereT i =|o i|denotes the number of generated assistant tokens
in rollouto i that are included in the policy-gradient loss, the token-level importance ratio is
ri,t(θ) = πθ(yi,t |h i,t) πθold(yi,t |h i,t),
whereh i,t denotes the full interaction history before tokent, including the prompt, previous assis-
tant tokens, and environment observations. We maximize the DAPO objective
JDAPO(θ) =E q,{oi}
"
1
∑G i=1 Ti
G
∑
i=1
Ti
∑
t=1
min

ri,t(θ) ˆAi, clip (ri,t(θ), 1−ϵ ℓ, 1+ϵ h) ˆAi 
#
,
where we use the asymmetric clipping range(ϵ ℓ,ϵ h) = (0.20, 0.28). The asymmetric range, with
ϵh >ϵ ℓ, permits larger updates for tokens from positive-advantage rollouts while retaining the
lower clip to control excessively large probability decreases. Following DAPO, we usedynamic
sampling: groups satisfyingσ 2 q =0 are discarded and re-sampled. Thus, each policy update is
computed from groups with non-degenerate relative advantages.
Reward.For each rollouto, we compute a scalar reward from two outcome-grounded compo-
nents, gated by a hard format constraint:
R(o) =I valid(o)

wprp(o) +wcrc(o)

,w p +w c =1.
We setw p =0.9,w c =0.1. The conclusion reward is assigned a smaller weight because it
primarily checks whether the reported decision is consistent with the reportedp-value. Here
8

Ivalid(o) =1 only if the trajectory contains reasoning, executable code, and a parseable terminal
<answer>...</answer>block; otherwiseR(o) =0. Thep-value component compares the reported
ˆpwith the answer-key valuep
∗
on a two-sided normal test-statistic scale:
z(p) =Φ −1(1−p/2),r p(o) =exp

− |min{z( ˆp), 5} −min{z(p
∗
), 5}|
σ

,σ=1.
The mapz(p) =Φ −1(1−p/2)doesnotassume that the underlying data are Gaussian; it is a
monotonic, distribution-free re-labeling of thep-value as the two-sided standard-normalz-score
whose tail probability equalsp, and applies regardless of which test (parametric or nonparametric)
producedp. We score inz-space because rawp-values are heavily compressed near 0, where the
most informative differences in evidence live. For example, the pair{p=0.5,p=0.6}and the
pair{p=0.1,p=10 −10}both have|∆p| ≈0.1, yet the first represents essentially no change
in evidence while the second spans many orders of magnitude in statistical significance. The
z-scale addresses this compression and is a widely used convention in statistical practice, such
as meta-analysis. The conclusion componentr c ∈ {0, 1}checks whether the final reject/fail-to-
reject decision agrees with the answer key atα=0.05. We do not include an explicit method-
correctness term in the reward because multiple statistical procedures may be defensible for the
same hypothesis-testing task. Instead, method choice is evaluated indirectly through the outcome-
grounded reward: an inappropriate method will typically produce a p-value that deviates from
the reference analysis, and therefore receive a lower z-space p-value closeness reward.
5 Experiment
5.1 Experimental Setting
Models and BaselinesWe include Qwen2.5-Coder-7B and 14B [31] as our backbone models to
compare different baselines. We compare Fisher-R1 with strong proprietary models: GPT-5.4 [32].
We also include four outstanding open-source models: DeepSeek-V4-Pro [33], GPT-OSS-120B [34],
Qwen3-Coder-30B [35] and Qwen3-32B [36], and DataMind [37] has been trained for data analysis.
Evaluation metrics.We evaluate each model on two splits of P-Bench: P-Easy and P-Hard. For
each task, we sample three independent rollouts and report results under two correctness criteria.
Rawmeasures whether the model reaches the correct hypothesis-testing conclusion atα=0.05,
i.e., whether its final reject/fail-to-reject decision matches the ground-truth decision. Unparseable
rollouts are counted as incorrect.Strictfurther requires the reportedp-value to be numerically
close to the ground-truth value in two-sidedz-space:
Strict=Raw∧

z( ˆp)−z(p ∗ )

 <0.5,z(p) =Φ −1(1−p/2).
Thus, Raw evaluates conclusion-level correctness, while Strict evaluates whether the model reaches
the correct conclusion with a sufficiently accurate reportedp-value. For each model, we run
three independent trials per task, pass@1 averages the per-trial success rate; pass@3 counts a
task as solved if any of its three trials succeed. Because the canonical analyses come from peer-
reviewed papers or authoritative course materials and are expert-audited, scoring is reproducible
and expert-grounded.
9

Table 1: Main results on P-Bench. Raw denotes correct conclusion direction, while Strict addi-
tionally requires|∆z|<0.5, wherezis the two-sidedz-score derived from the reportedp-value.
pass@1 is reported as mean±stdev over three independent runs.
Model P-Easy P-Hard
Raw Strict Raw Strict
pass@1 pass@3 pass@1 pass@3 pass@1 pass@3 pass@1 pass@3
Proprietary Models
GPT-5.492.9 ±1.0 95.6 64.7 ±3.3 73.4 58.3 ±0.9 68.0 30.5 ±1.6 39.2
Open-source Models
DeepSeek V4 Pro 70.9 ±0.5 93.1 54.2 ±0.5 71.9 46.8 ±1.2 69.7 26.3 ±3.0 42.5
GPT-OSS-120B 48.1 ±4.3 86.2 26.3 ±3.6 55.2 37.4 ±4.3 71.2 18.2 ±3.5 38.7
Qwen-3-Coder-30B 76.9 ±2.2 87.7 45.0 ±1.1 57.6 59.8 ±0.9 68.0 27.8 ±1.8 36.0
Qwen-3-32B 82.8 ±0.0 90.6 46.1 ±1.7 56.2 58.4 ±0.7 71.6 27.2 ±0.7 38.7
Qwen-2.5-Coder-7B 61.4 ±8.5 83.7 36.3 ±5.5 54.7 37.5 ±2.8 63.1 13.2 ±0.5 25.2
DataMind-7B 60.3 ±1.0 84.2 31.5 ±1.0 49.8 44.4 ±4.2 66.7 19.1 ±1.7 32.0
Fisher-R1-7B 87.0±1.6 96.6 65.7±1.2 74.9 63.4±2.5 82.4 30.6±1.2 44.1
Qwen-2.5-Coder-14B 78.5 ±1.2 88.2 41.4 ±2.5 49.8 51.5 ±4.3 66.7 23.7 ±1.6 33.3
DataMind-14B 69.0 ±5.2 88.2 39.6 ±3.0 53.7 48.2 ±2.1 67.1 22.1 ±1.2 33.8
Fisher-R1-14B 87.4±1.9 94.1 64.2±0.6 75.9 65.8±0.8 81.1 33.0±1.7 45.5
5.2 Main Results
Fisher-R1 turns its Qwen-2.5-Coder backbones into the strongest open-source hypothesis-testing
agents on P-Bench (Table 1). With the 7B backbone, Raw pass@1 rises from 61.4 to 87.0 on P-Easy
and from 37.5 to 63.4 on P-Hard, while Strict pass@1 jumps from 36.3 to 65.7 (P-Easy) and 13.2 to
30.6 (P-Hard); the 14B variant achieves the best P-Hard Strict scores in the table (33.0 pass@1, 45.5
pass@3). Run-to-run standard deviations also drop sharply (e.g.,±8.5→ ±1.6 on P-Easy Raw
pass@1 for the 7B), so Fisher-R1 is not only more accurate but also more stable across rollouts.
Fisher-R1 also outperforms substantially larger open-source baselines. Despite using 7B/14B
backbones, it beats DeepSeek V4 Pro, GPT-OSS-120B, Qwen-3-Coder-30B, and Qwen-3-32B on ev-
ery Strict metric, indicating that for hypothesis testing, targeted training with a verified statistical
reward is more effective than scaling the underlying coding model. Fisher-R1-14B further exceeds
GPT-5.4 on three of four Strict metrics (P-Easy pass@3: 75.9 vs 73.4; P-Hard pass@1: 33.0 vs 30.5;
P-Hard pass@3: 45.5 vs 39.2), trailing only narrowly on P-Easy Strict pass@1 (64.2 vs 64.7).
Across all baselines, Strict scores are far below Raw scores, especially on P-Hard. GPT-5.4, for
example, scores 58.3 Raw but only 30.5 Strict on P-Hard pass@1: it reports the correct reject/fail-
to-reject direction nearly twice as often as it produces ap-value close to the canonical analysis.
This pattern is robust to the choice of Strict threshold: using a relaxed criterion of|∆z|<1 leads
to the same qualitative conclusion (Table 5) as the main criterion of|∆z|<0.5. Fisher-R1 shrinks
this gap, suggesting that conclusion-only evaluation overstates agent reliability in open-ended hy-
pothesis testing, and that explicitly rewardingp-value accuracy is what gets the model to ground
its decision in the executed analysis.
10

5.3 Ablation Analysis
Table 2 shows that combining the SFT warm-start with DAPO is essential to reach Fisher-R1’s full
performance: SFT+DAPO achieves the best score on every metric, substantially above either stage
alone. DAPO applied directly to the backbone lifts single-run accuracy (e.g., P-Hard Strict pass@1
13.2 to 25.2), but plateaus well below SFT+DAPO. SFT alone improves pass@3 by broadening the
solution distribution, but does not reliably improve pass@1.
Table 2: Ablation of SFT warm-start and DAPO training on P-Bench with the 7B backbone.
Backbone P-Easy P-Hard
Raw Strict Raw Strict
pass@1 pass@3 pass@1 pass@3 pass@1 pass@3 pass@1 pass@3
Qwen-2.5-Coder-7B 61.4±8.5 83.7 36.3±5.5 54.7 37.5±2.8 63.1 13.2±0.5 25.2
+DAPO 81.6 ±2.8 86.9 44.4 ±0.9 48.2 52.3 ±3.6 62.6 25.2 ±0.8 30.3
+SFT 51.6 ±6.1 84.2 30.2 ±4.6 59.6 33.5 ±3.9 68.0 14.3 ±1.1 30.2
+DAPO 87.0±1.6 96.6 65.7±1.2 74.9 63.4±2.5 82.4 30.6±1.2 44.1
5.4 Generalization, not Memorization
To verify that gains on P-Bench reflect generalization rather than memorization, we quantify the
distance between the evaluation set and the SFT and RL training corpus in semantic-embedding
space. For each input, we extract the research question and study description, i.e., the user prompt,
and embed it with OpenAI’stext-embedding-3-small[38]. We then compute, for each sample,
the mean cosine similarity to its top-5 nearest neighbors in the training pool.
0.0 0.2 0.4 0.6 0.8 1.0
cosine similarity
0
5
10
15
20density (KDE)
train ↔ train
eval ↔ train
Figure 5: Similarity Analysis
As shown in Fig. 5, train-to-train similari-
ties form a tight high-similarity “memorization
band” that reflects the templated structure of
generated RL prompts, while eval-to-train sim-
ilarities sit clearly below this band. The 425 P-
Bench tasks, therefore, have no near-duplicate
counterparts in the RL corpus, indicating that
gains on P-Bench reflect generalization rather
than retrieval of training prompts. The two
distributions also differ by construction: train-
ing tasks are synthetic simulations, whereas P-
Bench tasks are real-world hypothesis-testing
tasks.
6 Discussion
We introduced P-Bench, a benchmark of 425 real-world hypothesis-testing tasks with expert-
audited answer keys, and Fisher-R1, an open-weight agent trained on synthetic statistical tasks
via SFT and RL with verified-outcome rewards. Our results show that even current frontier mod-
els still lack reliable statistical reasoning for open-ended hypothesis testing. Fisher-R1-14B out-
performs strong proprietary and open-source baselines, including GPT-5.4 and DeepSeek-V4-Pro.
11

P-Bench currently evaluates a single hypothesis test per task. Extending it to multi-test pipelines
with multiple-comparison correction is a natural next step. Reliable statistical agents can im-
prove scientific reproducibility by catching method-driven errors before they enter the literature.
They could also lend false legitimacy to weak claims. We therefore release P-Bench and Fisher-
R1 as evaluation and oversight tools, not as substitutes for human statistical review. Future work
should further study how to make agents explicitly justify assumptions, quantify uncertainty over
method choice, and recognize when no single hypothesis test is adequate for a scientific question.
References
[1] Ronald L. Wasserstein and Nicole A. Lazar. The asa statement on p-values: Context, process,
and purpose.The American Statistician, 70(2):129–133, 2016. doi: 10.1080/00031305.2016.
1154108. URLhttps://doi.org/10.1080/00031305.2016.1154108.
[2] Wenqi Zhang, Yongliang Shen, Weiming Lu, and Yueting Zhuang. Data-copilot: Bridging
billions of data and humans with autonomous workflow.arXiv preprint arXiv:2306.07209,
2023.
[3] Shaolei Zhang, Ju Fan, Meihao Fan, Guoliang Li, and Xiaoyong Du. Deepanalyze: Agentic
large language models for autonomous data science.arXiv preprint arXiv:2510.16872, 2025.
[4] Sirui Hong, Yizhang Lin, Bang Liu, Bangbang Liu, Binhao Wu, Ceyao Zhang, Danyang Li,
Jiaqi Chen, Jiayi Zhang, Jinlin Wang, et al. Data interpreter: An llm agent for data science. In
Findings of the Association for Computational Linguistics: ACL 2025, pages 19796–19821, 2025.
[5] Xueyu Hu, Ziyu Zhao, Shuang Wei, Ziwei Chai, Qianli Ma, Guoyin Wang, Xuwu Wang,
Jing Su, Jingjing Xu, Ming Zhu, Yao Cheng, Jianbo Yuan, Jiwei Li, Kun Kuang, Yang Yang,
Hongxia Yang, and Fei Wu. Infiagent-dabench: Evaluating agents on data analysis tasks,
2024. URLhttps://arxiv.org/abs/2401.05507.
[6] Alex Egg, Martin Iglesias Goyanes, Friso Kingma, Andreu Mora, Leandro von Werra, and
Thomas Wolf. Dabstep: Data agent benchmark for multi-step reasoning.arXiv preprint
arXiv:2506.23719, 2025.
[7] Yiming Huang, Jianwen Luo, Yan Yu, Yitong Zhang, Fangyu Lei, Yifan Wei, Shizhu He,
Lifu Huang, Xiao Liu, Jun Zhao, and Kang Liu. DA-code: Agent data science code gen-
eration benchmark for large language models. In Yaser Al-Onaizan, Mohit Bansal, and
Yun-Nung Chen, editors,Proceedings of the 2024 Conference on Empirical Methods in Nat-
ural Language Processing, pages 13487–13521, Miami, Florida, USA, November 2024. As-
sociation for Computational Linguistics. doi: 10.18653/v1/2024.emnlp-main.748. URL
https://aclanthology.org/2024.emnlp-main.748/.
[8] Yizhang Zhu, Shiyin Du, Boyan Li, Yuyu Luo, and Nan Tang. Are large language models
good statisticians?Advances in Neural Information Processing Systems, 37:62697–62731, 2024.
[9] Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and
Yuan Cao. React: Synergizing reasoning and acting in language models.arXiv preprint
arXiv:2210.03629, 2022.
[10] Yuhang Lai, Chengxi Li, Yiming Wang, Tianyi Zhang, Ruiqi Zhong, Luke Zettlemoyer, Wen-
tau Yih, Daniel Fried, Sida Wang, and Tao Yu. Ds-1000: A natural and reliable benchmark for
12

data science code generation. InInternational Conference on Machine Learning, pages 18319–
18345. PMLR, 2023.
[11] Xueyu Hu, Ziyu Zhao, Shuang Wei, Ziwei Chai, Qianli Ma, Guoyin Wang, Xuwu Wang, Jing
Su, Jingjing Xu, Ming Zhu, et al. Infiagent-dabench: Evaluating agents on data analysis tasks.
arXiv preprint arXiv:2401.05507, 2024.
[12] Dan Zhang, Sining Zhoubian, Min Cai, Fengzu Li, Lekang Yang, Wei Wang, Tianjiao Dong,
Ziniu Hu, Jie Tang, and Yisong Yue. Datascibench: An llm agent benchmark for data science.
arXiv preprint arXiv:2502.13897, 2025.
[13] Jun Shern Chan, Neil Chowdhury, Oliver Jaffe, James Aung, Dane Sherburn, Evan Mays,
Giulio Starace, Kevin Liu, Leon Maksin, Tejal Patwardhan, et al. Mle-bench: Evaluating
machine learning agents on machine learning engineering.arXiv preprint arXiv:2410.07095,
2024.
[14] Jinyang Li, Nan Huo, Yan Gao, Jiayi Shi, Yingxiu Zhao, Ge Qu, Yurong Wu, Chenhao Ma,
Jian-Guang Lou, and Reynold Cheng. Tapilot-crossing: Benchmarking and evolving llms
towards interactive data analysis agents.arXiv preprint arXiv:2403.05307, 2024.
[15] Hanyu Li, Haoyu Liu, Tingyu Zhu, Tianyu Guo, Zeyu Zheng, Xiaotie Deng, and Michael I
Jordan. Ida-bench: Evaluating llms on interactive guided data analysis.arXiv preprint
arXiv:2505.18223, 2025.
[16] David Wadden, Shanchuan Lin, Kyle Lo, Lucy Lu Wang, Madeleine van Zuylen, Arman
Cohan, and Hannaneh Hajishirzi. Fact or fiction: Verifying scientific claims. InProceedings
of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP), pages
7534–7550, 2020.
[17] Sujit Kumar, Anshul Sharma, Siddharth Hemant Khincha, Gargi Shroff, Sanasam Ranbir
Singh, and Rahul Mishra. Sciclaimhunt: A large dataset for evidence-based scientific claim
verification. In2025 International Joint Conference on Neural Networks (IJCNN), pages 1–10.
IEEE, 2025.
[18] Yash Kumar Lal, Manikanta Bandham, Mohammad Saqib Hasan, Apoorva Kashi, Mahnaz
Koupaee, and Niranjan Balasubramanian. Musciclaims: Multimodal scientific claim verifi-
cation. InProceedings of the 14th International Joint Conference on Natural Language Processing
and the 4th Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics,
pages 3285–3307, 2025.
[19] Olivia Miske, Anna Lou Abatayo, Mason Daley, Mirka Dirzo, Nicholas Fox, Noah Haber,
Krystal M Hahn, Melissa Kline Struhl, Brinna Mawhinney, Priya Silverstein, et al. Investi-
gating the reproducibility of the social and behavioural sciences.Nature, 652(8108):126–134,
2026.
[20] Chris Lu, Cong Lu, Robert Tjarko Lange, Yutaro Yamada, Shengran Hu, Jakob Foerster, David
Ha, and Jeff Clune. Towards end-to-end automation of ai research.Nature, 651(8107):914–919,
2026.
[21] Jiabin Tang, Lianghao Xia, Zhonghang Li, and Chao Huang. Ai-researcher: Autonomous
scientific innovation.arXiv preprint arXiv:2505.18705, 2025.
13

[22] Yutaro Yamada, Robert Tjarko Lange, Cong Lu, Shengran Hu, Chris Lu, Jakob Foerster, Jeff
Clune, and David Ha. The ai scientist-v2: Workshop-level automated scientific discovery via
agentic tree search.arXiv preprint arXiv:2504.08066, 2025.
[23] Abdul Latif Jameel Poverty Action Lab (J-PAL). Development economics field experiments
(dfeep). Harvard Dataverse, 2026. URLhttps://dataverse.harvard.edu/dataverse/
DFEEP. Accessed: 2026-04-20.
[24] Ethan Cerami, Jianjiong Gao, Ugur Dogrusoz, Benjamin E Gross, Selcuk Onur Sumer, Bü-
lent Arman Aksoy, Anders Jacobsen, Caitlin J Byrne, Michael L Heuer, Erik Larsson, et al.
The cbio cancer genomics portal: an open platform for exploring multidimensional cancer
genomics data.Cancer discovery, 2(5):401–404, 2012.
[25] Jianjiong Gao, Bülent Arman Aksoy, Ugur Dogrusoz, Gideon Dresdner, Benjamin Gross,
S Onur Sumer, Yichao Sun, Anders Jacobsen, Rileen Sinha, Erik Larsson, et al. Integrative
analysis of complex cancer genomics and clinical profiles using the cbioportal.Science signal-
ing, 6(269):pl1–pl1, 2013.
[26] Zifeng Wang, Benjamin Danek, and Jimeng Sun. Biodsa-1k: Benchmarking data science
agents for biomedical research, 2025. URLhttps://arxiv.org/abs/2505.16100.
[27] Frank E. Harrell. Vanderbilt biostatistics datasets (hbiostat.org).https://hbiostat.org/
data/, 2024. Accessed 2026-04-20.
[28] Anthropic. Introducing claude sonnet 4.6.https://www.anthropic.com/news/
claude-sonnet-4-6, February 2026. Accessed: 2026-05-06.
[29] Xingyao Wang, Yangyi Chen, Lifan Yuan, Yizhe Zhang, Yunzhu Li, Hao Peng, and Heng
Ji. Executable code actions elicit better llm agents. InForty-first International Conference on
Machine Learning, 2024.
[30] Qiying Yu, Zheng Zhang, Ruofei Zhu, Yufeng Yuan, Xiaochen Zuo, Yu Yue, Weinan Dai,
Tiantian Fan, Gaohong Liu, Lingjun Liu, et al. Dapo: An open-source llm reinforcement
learning system at scale.arXiv preprint arXiv:2503.14476, 2025.
[31] Binyuan Hui, Jian Yang, Zeyu Cui, Jiaxi Yang, Dayiheng Liu, Lei Zhang, Tianyu Liu, Jiajun
Zhang, Bowen Yu, Keming Lu, Kai Dang, Yang Fan, Yichang Zhang, An Yang, Rui Men,
Fei Huang, Bo Zheng, Yibo Miao, Shanghaoran Quan, Yunlong Feng, Xingzhang Ren, Xu-
ancheng Ren, Jingren Zhou, and Junyang Lin. Qwen2.5-coder technical report, 2024. URL
https://arxiv.org/abs/2409.12186.
[32] OpenAI. Introducing gpt-5.4.https://openai.com/index/introducing-gpt-5-4/, March
2026. Accessed: 2026-05-06.
[33] DeepSeek-AI. Deepseek-v4: Towards highly efficient million-token context intelligence.
https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro, April 2026. Model card and tech-
nical report for DeepSeek-V4-Pro. Accessed: 2026-05-06.
[34] OpenAI. Introducing gpt-oss.https://openai.com/index/introducing-gpt-oss/, 2025.
Accessed: 2026-05-07.
[35] Qwen Team. Qwen3-coder-30b-a3b-instruct.https://huggingface.co/Qwen/
Qwen3-Coder-30B-A3B-Instruct, 2025. Model card. Accessed: 2026-05-06.
14

[36] An Yang, Anfeng Li, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu,
Chang Gao, Chengen Huang, Chenxu Lv, Chujie Zheng, Dayiheng Liu, Fan Zhou, Fei Huang,
Feng Hu, Hao Ge, Haoran Wei, Huan Lin, Jialong Tang, Jian Yang, Jianhong Tu, Jianwei
Zhang, Jianxin Yang, Jiaxi Yang, Jing Zhou, Jingren Zhou, Junyang Lin, Kai Dang, Keqin Bao,
Kexin Yang, Le Yu, Lianghao Deng, Mei Li, Mingfeng Xue, Mingze Li, Pei Zhang, Peng Wang,
Qin Zhu, Rui Men, Ruize Gao, Shixuan Liu, Shuang Luo, Tianhao Li, Tianyi Tang, Wenbiao
Yin, Xingzhang Ren, Xinyu Wang, Xinyu Zhang, Xuancheng Ren, Yang Fan, Yang Su, Yichang
Zhang, Yinger Zhang, Yu Wan, Yuqiong Liu, Zekun Wang, Zeyu Cui, Zhenru Zhang, Zhipeng
Zhou, and Zihan Qiu. Qwen3 technical report.arXiv preprint arXiv:2505.09388, 2025.
[37] Shuofei Qiao, Yanqiu Zhao, Zhisong Qiu, Xiaobin Wang, Jintian Zhang, Zhao Bin, Ningyu
Zhang, Yong Jiang, Pengjun Xie, Fei Huang, and Huajun Chen. Scaling generalist data-
analytic agents, 2026. URLhttps://arxiv.org/abs/2509.25084.
[38] OpenAI.text-embedding-3-smallmodel.https://developers.openai.com/api/docs/
models/text-embedding-3-small, 2026. Accessed: 2026-05-06.
[39] Aman Madaan, Niket Tandon, Prakhar Gupta, Skyler Hallinan, Luyu Gao, Sarah Wiegr-
effe, Uri Alon, Nouha Dziri, Shrimai Prabhumoye, Yiming Yang, Shashank Gupta, Bod-
hisattwa Prasad Majumder, Katherine Hermann, Sean Welleck, Amir Yazdanbakhsh, and
Peter Clark. Self-refine: Iterative refinement with self-feedback, 2023. URLhttps://arxiv.
org/abs/2303.17651.
[40] Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, and Shunyu Yao.
Reflexion: Language agents with verbal reinforcement learning.Advances in neural informa-
tion processing systems, 36:8634–8652, 2023.
[41] Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, Chaowei Xiao, Yuke Zhu, Linxi Fan,
and Anima Anandkumar. Voyager: An open-ended embodied agent with large language
models.arXiv preprint arXiv:2305.16291, 2023.
[42] John Yang, Carlos E Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik
Narasimhan, and Ofir Press. Swe-agent: Agent-computer interfaces enable automated soft-
ware engineering.Advances in Neural Information Processing Systems, 37:50528–50652, 2024.
[43] John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal
policy optimization algorithms.arXiv preprint arXiv:1707.06347, 2017.
[44] Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll Wainwright, Pamela Mishkin,
Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, et al. Training language models
to follow instructions with human feedback.Advances in neural information processing systems,
35:27730–27744, 2022.
[45] Rafael Rafailov, Archit Sharma, Eric Mitchell, Christopher D Manning, Stefano Ermon, and
Chelsea Finn. Direct preference optimization: Your language model is secretly a reward
model.Advances in neural information processing systems, 36:53728–53741, 2023.
[46] Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang,
Mingchuan Zhang, YK Li, Yang Wu, et al. Deepseekmath: Pushing the limits of mathematical
reasoning in open language models.arXiv preprint arXiv:2402.03300, 2024.
15

[47] Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Peiyi Wang, Qihao Zhu, Runxin Xu,
Ruoyu Zhang, Shirong Ma, Xiao Bi, et al. Deepseek-r1: Incentivizing reasoning capability in
llms via reinforcement learning.arXiv preprint arXiv:2501.12948, 2025.
[48] Xuefeng Li, Haoyang Zou, and Pengfei Liu. Torl: Scaling tool-integrated rl.arXiv preprint
arXiv:2503.23383, 2025.
[49] Jiazhan Feng, Shijue Huang, Xingwei Qu, Ge Zhang, Yujia Qin, Baoquan Zhong, Chengquan
Jiang, Jinxin Chi, and Wanjun Zhong. Retool: Reinforcement learning for strategic tool use in
llms.arXiv preprint arXiv:2504.11536, 2025.
[50] Cheng Qian, Emre Can Acikgoz, Qi He, Hongru Wang, Xiusi Chen, Dilek Hakkani-Tür,
Gokhan Tur, and Heng Ji. Toolrl: Reward is all tool learning needs.arXiv preprint
arXiv:2504.13958, 2025.
[51] Jeff Da, Clinton Wang, Xiang Deng, Yuntao Ma, Nikhil Barhate, and Sean Hendryx. Agent-
rlvr: Training software engineering agents via guidance and environment rewards.arXiv
preprint arXiv:2506.11425, 2025.
[52] Madeline McKelway, Abhijit Banerjee, Erin Grela, Frank Schilbach, Miriam Sequeira, Garima
Sharma, Girija Vaidyanathan, and Esther Duflo. Effects of cognitive behavioral therapy and
cash transfers on older persons living alone in india: a randomized trial.Annals of internal
medicine, 176(5):632–641, 2023.
[53] Bastien Nguyen, Christopher Fong, Anisha Luthra, Shaleigh A Smith, Renzo G DiNatale,
Subhiksha Nandakumar, Henry Walch, Walid K Chatila, Ramyasree Madupuri, Ritika Kun-
dra, et al. Genomic characterization of metastatic patterns from prospective clinical sequenc-
ing of 25,000 patients.Cell, 185(3):563–575, 2022.
[54] William A Knaus, Frank E Harrell, Joanne Lynn, Lee Goldman, Russell S Phillips, Alfred F
Connors, Neal V Dawson, William J Fulkerson, Robert M Califf, Norman Desbiens, et al.
The support prognostic model: Objective estimates of survival for seriously ill hospitalized
adults.Annals of internal medicine, 122(3):191–203, 1995.
[55] Yaowei Zheng, Richong Zhang, Junhao Zhang, Yanhan Ye, Zheyan Luo, Zhangchi Feng, and
Yongqiang Ma. Llamafactory: Unified efficient fine-tuning of 100+ language models, 2024.
URLhttps://arxiv.org/abs/2403.13372.
[56] Guangming Sheng, Chi Zhang, Zilingfeng Ye, Xibin Wu, Wang Zhang, Ru Zhang, Yanghua
Peng, Haibin Lin, and Chuan Wu. Hybridflow: A flexible and efficient rlhf framework. In
Proceedings of the Twentieth European Conference on Computer Systems, pages 1279–1297, 2025.
16

A Additional Related Works
Agentic execution and reinforcement learning.Beyond static prompting, recent LLM agents
solve tasks through iterative interaction with external environments, using tool observations to
revise plans, correct errors, and sustain long-horizon execution [39–42]. Reinforcement learning
has become a central post-training approach for improving such reasoning and tool-use behaviors,
evolving from preference-based alignment [43–45] to outcome-verifiable reasoning: DeepSeek-
Math introduces GRPO for critic-free RL, DeepSeek-R1 scales RL to induce extended reasoning,
and DAPO improves large-scale RL training with decoupled clipping and dynamic sampling
[30, 46, 47]. A related line studies RL for tool-using agents that decide when and how to call
external tools during multi-turn problem solving [48–51]. Whereas these systems reward correct-
ness of a final answer in math, coding, or SQL, Fisher-R1’s reward must scoreinferential validity: a
p-value compared on az-score scale, plus consistency between the chosen method, the computed
evidence, and the reported reject/fail-to-reject decision.
B More details on P-bench
B.1 Data curation pipeline.
Automating verifications
Papers Main claims Parse
Reproduce
Extract
Claims in json format
Executed results
Inputs
Outputs
{
“claim”: “drug improves patient outcome”,
“method”: “paired t- test”,
“p”: 0.013,
“conclusion”: “reject the null hypothesis”
}
Claim 1  p = 0.013
Claim 2  p < 0.001
Claim 3  p = 0.042
Claim 1  p = 0.013
Claim 2  p < 0.001
Claim 3  p = 0.042
analysis.R
# paired t test
t. test(x, y, paired = TRUE)
      p = 0.013
Figure 6: Data curation for P-bench
Figure 6 summarizes how we convert scientific
artifacts into verified hypothesis-testing tasks.
Given a paper, released data, and available
analysis code. It identifies statistical claims
with inferential results and parses them into
structured records, and links each claim to the
corresponding executable analysis. Our sys-
tem is built on Claude Code with Sonnet 4.5.
Verification and filtering.The agent repro-
duces the analysis in a clean execution envi-
ronment and extracts p-values, test statistics,
and conclusions from the execution logs rather
than from paper text alone. Claims are kept
only when the reported result can be matched
to an executed computation with a consistent
hypothesis-testing decision; ambiguous, failed, or inconsistent cases are discarded. The remaining
claims are further checked by expert review and packaged as P-Bench tasks with hidden answer
keys.
B.2 P-bench Examples
We provide one representative task from each of the three source families. Each example shows
the analysis request and the hidden answer key; the dataset itself is provided to the agent as a
CSV file.
17

B.3 Example from economics
Source: McKelway, Madeline, et al. "Effects of cognitive behavioral therapy and cash transfers on older
persons living alone in India: a randomized trial." Annals of internal medicine 176.5 (2023): 632-641. [52]
A randomized controlled trial assigning elderly persons living alone to one of four arms (control,
CBT only, cash only, both) with three measurement waves.
analysis_request.txt
Research question:Does phone-based cognitive behavioral therapy without cash support reduce de-
pression among elderly persons living alone in Tamil Nadu, India at 3 weeks after the intervention,
relative to the control group?
Hypothesis:
H0: CBT does not affect depression at 3 weeks relative to the control group.
H1: CBT only reduces depression at 3 weeks relative to the control group.
Study design:Randomized controlled trial; individual-level randomization; three waves (baseline, 3
weeks, 3 months).
Variable glossary:GDS(Geriatric Depression Scale, integer 0–15) [OUTCOME];itreat(treatment
arm, 0–3) [TREATMENT];T(time period, 0–2);elderly_ID_anon(individual id); plus covariates.
dataset.csv (first 3 rows, selected columns)
elderly_ID_anon, T, itreat, GDS, ADL, bl_female
211101, 2, 0, 8, 22, 1
143101, 2, 0, 8, 4, 1
232501, 2, 0, 9, 14, 1
...
answer_key.json(hidden)
{
"test_type": "mixed-effects linear regression",
"treatment_variable": "1.T#1.itreat (CBT only x 3 weeks)",
"treatment_coefficient": -0.0873,
"treatment_p_value": 0.876,
"significant_at_005": false,
"conclusion": "Fail to reject H0",
"n_observations": 3009,
"n_groups": 1113
}
B.4 Example from biology
Source: Nguyen et al., “Genomic characterization of metastatic patterns from prospective clinical sequenc-
ing of 25,000 patients.” Cell, 2022 [53].
18

analysis_request.txt
Research question:Is PTEN mutation status associated with metastatic disease among colorectal can-
cer patients in this tumor sequencing cohort, accounting for basic patient demographics?
Hypothesis:
H0: PTEN mutation status is not associated with metastatic disease among colorectal cancer patients.
H1: PTEN mutation status is associated with metastatic disease among colorectal cancer patients.
Study design:Observational tumor sequencing cohort; 2,396 primary tumor samples; metastatic sta-
tus recorded at the patient level.
Variable glossary:is_metastatic_patient(binary) [OUTCOME];pten_mutated(binary) [TAR-
GET];sex_numeric,age_at_sequencing(covariates).
dataset.csv (first 3 rows, selected columns)
sample_id, is_metastatic_patient, pten_mutated, sex_numeric, age_at_sequencing
P-0000520-T01-IM3, 1, 0, 1, 66.63
P-0000625-T01-IM3, 1, 0, 0, 69.77
P-0000674-T01-IM3, 1, 0, 0, 65.33
...
answer_key.json(hidden)
{
"test_type": "Logistic regression",
"treatment_variable": "pten_mutated",
"treatment_coefficient": -0.5059,
"odds_ratio": 0.603,
"treatment_p_value": 0.0146,
"significant_at_005": true,
"conclusion": "Reject H0",
"n_observations": 2396
}
B.5 Example from medicine
Source:Knaus et al., “The SUPPORT prognostic model. Objective estimates of survival for seriously ill hos-
pitalized adults.” Annals of Internal Medicine, 1995, 122:191–203 [54]Prospective cohort of seriously
ill hospitalized adults.
analysis_request.txt
Research question:Among seriously ill hospitalized adults in the SUPPORT study, is in-hospital mor-
tality associated with patient disease class, particularly the Coma category?
Hypothesis:
H0: Patients in the Coma disease class do not differ in in-hospital mortality from the reference disease
class.
H1: Patients in the Coma disease class differ in in-hospital mortality from the reference disease class.
Study design:Prospective cohort; 9,105 observations; reference analysis usesN=5,732 after task-
specific filtering and missing-data handling.
Variable glossary:hospdead(binary) [OUTCOME];dzclass(categorical: ARF/MOSF w/Ma-
lignancy, ARF/MOSF w/Sepsis, COPD/CHF/Cirrhosis, Coma, Cancer) [TARGET];age,num.co,
meanbp,hrt,resp,crea,alb(covariates).
19

dataset.csv (first 3 rows, selected columns)
age, sex, hospdead, dzclass, num.co
62.85, male, 0, Cancer, 0
60.34, female, 1, COPD/CHF/Cirrhosis, 2
52.75, female, 0, COPD/CHF/Cirrhosis, 2
...
answer_key.json(hidden)
{
"test_type": "Logistic regression",
"treatment_variable": "dzclass (Coma)",
"treatment_coefficient": 0.9477,
"treatment_p_value": 0.0001,
"significant_at_005": true,
"conclusion": "Reject H0",
"n_observations": 5732
}
C Fisher-R1 Training Details
C.1 Why R rather than Python
We use R rather than Python because the canonical implementations of the statistical methods P-
Bench covers — Cox proportional-hazards regression, mixed-effects models, instrumental-variable
estimators, robust and rank-based tests — are most mature and standardized in R packages such
assurvival,lme4,rms, andAER, whose outputs are widely treated as canonical in biomedicine,
biostatistics, and economics. Python’s statistical stack (statsmodels,scipy.stats,lifelines) is
less complete on these methods and frequently differs in default settings (e.g., degrees-of-freedom
corrections, link parameterizations, robust-variance estimators) that are standardized across R
packages. Statisticians typically use R for these analyses, making it easier for domain experts
to verify the agent’s executions against the reference analysis in a single software ecosystem.
C.2 Synthetic Data Generations
This appendix gives the full implementation of the synthetic-task pipeline summarised inS4.3.
C.2.1 End-to-end pipeline
For each cell of the Cartesian gridM×S m ×N×E×P×Kin the task taxonomy, we construct
one task in five stages.
Stage 1: simulation template.For each statistical methodM, we use an LLM to draft a param-
eterised simulation script. The script implements a canonical data-generating process for that
method (e.g., a two-stage least-squares DGP for IV with an instrument, an endogenous treatment,
an outcome, and covariates) and exposes the relevant parameters as variables (sample size, effect
size, error variance, clustering, fixed effects, etc.). All templates were drafted by Claude Sonnet
4.6 and checked by the authors to fix syntax errors and standardise the parameter-slot naming.
Templates are written once per method and reused across all tasks for that method.
Stage 2: parameter instantiation.Each cell of the grid specifies a sample size, an effect size, and
a seed. We plug these into the simulation template to fix all parameter values.
20

Stage 3: execution and answer key.We execute the instantiated script. It writes a CSV dataset
and runs the canonical statistical method on that dataset. The reportedp-value, the reject/fail-
to-reject decision atα=0.05, and the canonical method label are recorded inanswer_key.json.
Crucially, the answer key is theoutput of the canonical method on the simulated data, not the true gen-
erative parameter. This aligns the supervision target with what a correct analysis would actually
produce.
Stage 4: question rendering.Each scenario provides two prompt templates:analysis_nohint
states only the research question, whileanalysis_hintadds a one-sentence study-design sum-
mary (see Table 4). The chosen prompt stylePselects which template is rendered, and the result
is written toanalysis_request.txt.
Stage 5: task package.Each task consists of four files:study_description.txt,analysis_request.txt,
dataset.csv, andanswer_key.json. The agent sees the first three. The answer key is hidden and
used only for scoring.
C.3 Per-axis level lists
Table 3: Levels for each axis of the synthetic-task Cartesian grid.
Axis Levels
Mmethod 27 statistical methods spanning parametric, rank-based, regression, causal, hierarchi-
cal, and survival families
Sm scenario 5–7 domain scenarios per method. Each scenario specifies a column-renaming map, a
study description, andhint/non-hintprompt templates.
Nsample size small, medium, large, xlarge. Exact values are method-specific; across methods,N
ranges from∼30 for paired and small two-sample tests,∼200–500 for typical regres-
sions, up to∼4,800 for hierarchical and panel models.
Eeffect size null, borderline, medium.
Pprompt stylehint,non-hint. See 4 for examples.
Kseeds 0,s 1,s 2. Three deterministic seeds per cell.
Table 4: Examples ofnon-hintandhintprompts across method types. Both variants ask the
same research question; thehintvariant adds a one-sentence study-design summary that flags a
methodologically relevant feature.
Methodnon-hint hint
Mann–Whitney “Does API latency differ between server
A and server B?”
“. . . The latency distribution is heavily
right-skewed.”
Mixed-effects “Does the new ad creative improve user
click-through rate?”
“. . . Each user is shown multiple ads
over time, with users nested within de-
mographic segments.”
Cox PH “Does the new battery formulation ex-
tend laptop battery life?”
“. . . Devices still in use at study end
have right-censored lifetimes.”
21

C.3.1 Example
We give a single fully worked synthetic task to illustrate the pipeline end-to-end. The task uses
the Mann–Whitney scenarioapp_latency_two_servers, with cell valuesN=medium (n=200),
E=medium,K=s 0, and prompt styleP=hint. The four files generated by the pipeline are
shown below.
study_description.txt
Paper: “P50 vs P95 App Request Latency: Two-Pool A/B Comparison”
Study: Independent web requests were routed to one of two server pools.
Variables:request_id,server_pool(0 = pool A, 1 = pool B) [GROUP],request_latency_ms(contin-
uous, heavy right-tailed) [OUTCOME].
Sample: 200 independent requests.
analysis_request.txt
Research question: Do the two server pools have different latency distributions?
Report test statistic,p-value, location shift with 95% CI, conclusion atα=0.05.
dataset.csv(first 6 of 200 rows)
request_id,server_pool,request_latency_ms
1,0,87.32
2,1,142.05
3,0,71.48
4,1,239.71
5,0,103.86
6,1,118.40
...
answer_key.json(hidden from agent)
{
"task_id": "task_app_latency_two_servers_medium_medium_hint_s0",
"method": "mann_whitney_test",
"test_statistic": 4521.0,
"p_value_correct": 0.0184,
"location_shift": 12.4,
"ci_95": [3.1, 24.7],
"conclusion": "Reject H0",
"n_observations": 200,
"naive_method": "Welch’s t-test",
"p_value_naive": 0.0712
}
The agent sees only the first three files. The correct analysis is a Mann–Whitney test, which
yieldsp≈0.018 and rejectsH 0. A naive Welch’st-test would yieldp≈0.07 and reach the wrong
conclusion.
C.3.2 Data-quality perturbations
On top of the clean Cartesian grid, we add 60 perturbed task variants drawn from regression-
method cells. The two perturbation types are: (i)missing— a fraction of values in the outcome or
a covariate are set toNA, requiring the agent to choose how to handle missingness; (ii)outlier— a
small number of rows are injected with extreme or invalid values (e.g., physiologically implausible
22

measurements), requiring the agent to detect and address them before fitting. The answer key for
each perturbed variant is computed by running the canonical method on the perturbed data with
the standard handling protocol for the issue (e.g., listwise deletion formissing, robust standard
errors or trimming foroutlier).
C.4 Training setup and detailed hyperparameters
We conduct SFT using LlamaFactory [55] and RL training usingverl[56]. For SFT, we train for
3 epochs with a learning rate of 1e−5, a cosine learning-rate scheduler, a warmup ratio of 0.1, a
batch size of 16, and a cutoff length of 8192 tokens. For RL, we train for 1 epoch with a learning
rate of 1e−6, constant learning-rate warmup, and 20 warmup steps. The batch size is 16, the
maximum prompt length is 2048 tokens, and the maximum response length is 4096 tokens. We
use asymmetric clipping withϵ low =0.2 andϵ high =0.28. During rollout generation, we use
temperature 0.7, top-p=1.0, and a rollout group size ofG=8. At inference time, we use
temperature 0.3, top-p=0.9, and a batch size of 10.
C.5 Computing Resources
All training and evaluation runs are conducted on a single node with NVIDIA H200 GPUs (141
GB HBM each). For the 14B model, the full RL training run completes in about 36 hours.
C.6 More Experiment Results
Table 5: Results on P-Bench under the relaxed strict threshold. Raw denotes correct conclusion
direction, while Strict additionally requires|∆z|<1.0, wherezis the two-sidedz-score derived
from the reportedp-value. pass@1 is reported as mean ±stdev over three independent runs.
Model P-Easy P-Hard
Raw Strict Raw Strict
pass@1 pass@3 pass@1 pass@3 pass@1 pass@3 pass@1 pass@3
Proprietary Models
GPT-5.492.9 ±1.0 95.672.6 ±2.5 79.3 58.3 ±0.9 68.0 38.4 ±0.7 46.0
Open-source Models
DeepSeek V4 Pro 70.9 ±0.5 93.1 59.1 ±0.9 78.8 46.8 ±1.2 69.7 32.2 ±1.1 49.3
GPT-OSS-120B 48.1 ±4.3 86.2 31.2 ±4.4 64.5 37.4 ±4.3 71.2 23.6 ±2.3 49.1
Qwen-3-Coder-30B 76.9 ±2.2 87.7 53.2 ±1.7 65.0 59.8 ±0.9 68.0 35.4 ±1.0 42.3
Qwen-3-32B 82.8 ±0.0 90.6 55.2 ±0.5 66.0 58.4 ±0.7 71.6 34.2 ±0.5 46.4
Qwen-2.5-Coder-7B 61.4 ±8.5 83.7 41.4 ±6.5 60.1 37.5 ±2.8 63.1 18.6 ±0.7 32.0
DataMind-7B 60.3 ±1.0 84.2 38.6 ±1.4 57.1 44.4 ±4.2 66.7 25.2 ±2.1 40.5
Fisher-R1-7B 87.0±1.6 96.6 71.8±0.8 80.8 63.4±2.5 82.4 40.1±2.5 56.8
Qwen-2.5-Coder-14B 78.5 ±1.2 88.2 50.3 ±1.3 58.1 51.5 ±4.3 66.7 30.8 ±2.1 41.0
DataMind-14B 69.0 ±5.2 88.2 47.8 ±3.7 64.0 48.2 ±2.1 67.1 29.0 ±0.9 42.3
Fisher-R1-14B 87.4±1.9 94.1 70.6±1.4 79.8 65.8±0.8 81.1 42.0±2.2 56.8
23

D Prompt
Training Prompt
# System Prompt
You are a statistician working through a hypothesis-testing task in a multi-turn loop. The
dataset is pre-loaded as ‘data‘ (a data.frame). Do not load it yourself. On every turn, write
exactly one of the following structures and then STOP:
1. An intermediate analysis turn:
<think>
your reasoning about the data, assumptions, and the next analysis step
</think>
<code>
one block of R code (use cat() or print() to display results)
</code>
2. A final answer turn (no code):
<think>
brief summary of what you learned
</think>
<answer>
1. Analysis summary: key EDA findings, assumption check results, method choice and
rationale.
2. Results interpretation: effect estimate, direction, magnitude, p-value, confidence interval.
FINAL ANSWER:
- Treatment effect: [number]
- P-value: [number]
- 95% CI: [lower, upper]
- Conclusion: [Reject H0 / Fail to reject H0] at alpha = 0.05
</answer>
Rules:
- After each <code> block, the runtime will reply with <observation>...</observation> con-
taining the R stdout. Read it before writing the next turn.
- Do NOT write more than one <code> block per turn. Do NOT write <observation> your-
self.
- Do NOT print raw data values, unique values, or large vectors. Use dim(), colnames(), and
class() to inspect data.
- If your code produces an error, read the message carefully and fix the root cause before
retrying.
- Only emit <answer> on the very last turn, and only after you have verified the numerical
results from <observation>.
# User Prompt
## Research Question
24

{analysis_request}
## Dataset
The dataset has been pre-loaded asdata.
25

Figure 7: Full Welch’s t-test simulation template.
26
