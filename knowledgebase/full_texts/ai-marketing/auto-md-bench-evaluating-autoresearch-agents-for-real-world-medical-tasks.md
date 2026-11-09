---
title: 'Auto-MD-bench: Evaluating Autoresearch Agents for Real-World Medical Tasks'
url: https://arxiv.org/abs/2610.25069
category: ai-marketing
subcategory: measurement
date: 2026-10
venue: ''
authors: []
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.25069
pages: 24
chars: 81727
fetched_at: '2026-11-08T13:31:22+00:00'
kb_version: 1
---

# Auto-MD-bench: Evaluating Autoresearch Agents for Real-World Medical Tasks

Auto-MD-bench: Evaluating Autoresearch Agents for Real-World
Medical Tasks
Shenqi Zhou1,2,*, Qiran Zou 1,*, Wenhao Zhao 1, Zhenyu Liao 3, Dianbo Liu 1,†
1National University of Singapore 2Zhejiang University 3Amazon
*Equal contribution †Corresponding author Contact: shenqi_zhou@zju.edu.cn, dianbo@nus.edu.sg
Abstract
Autonomous agents are increasingly capable
of developing machine learning (ML) mod-
els end to end. In medical practice, however,
strong performance on the target metric does
not fully characterize how good the models
are in real-world use cases. For example,
medical ML models should also provide well-
calibrated risk estimates and remain robust
across patient populations. Yet autonomous
model development is typically guided by
task objectives that emphasize simple pre-
dictive discrimination (e.g. AUROC). This
raises a key question: are these objectives
sufficient to guide agents toward models that
meet the broader requirements of real-world
medical use? In this study, we introduce
Auto-MD-bench, a benchmark of 15 real-
world medical tasks from 10 clinical datasets,
spanning survival analysis, classification and
sequential prediction, with external valida-
tion across cohorts, hospitals and time pe-
riods. We evaluate four agents: AIDE, AI
Scientist v2, Codex, and Autoresearch. The
strongest agents achieve competitive primary
scores, yet their predicted risks are less cali-
brated than those of the simple baseline mod-
els, which could lead to severe medical acci-
dents. Moreover, models with nearly identi-
cal primary scores can exhibit markedly dif-
ferent calibration, while performance varies
substantially across population shifts. These
findings show that primary task performance
alone is insufficient to assess autonomous
clinical modeling and multiple different met-
rics widely used in healthcare practice need
to be taken into consideration.
1 INTRODUCTION
Autonomous research agents can increasingly develop
machine learning models end to end, from data inspec-
tion and model selection to implementation, valida-
tion, and iterative refinement (Chan et al., 2025; Miller
et al., 2025). Such capabilities are particularly conse-
quential in medicine, where prediction models use pa-
tient data to estimate clinical outcomes and inform pa-
tient care (Steyerberg et al., 2009). Automating their
development could reduce the effort required to build
models for different outcomes and patient populations,
but it also delegates clinically consequential modeling
decisions to autonomous agents.1
In real-world medical settings, however, strong perfor-
mance on a target metric does not fully characterize
a model’s suitability for medical use. A model may
distinguish patients at higher and lower risk while pro-
viding inaccurate estimates of their absolute risk, po-
tentially misleading screening or treatment decisions
(Van Calster et al., 2019). Its performance may also
change when applied to patients from another cohort,
hospital, or time period (Royston and Altman, 2013).
These aspects of model quality are not necessarily
captured by the primary task objective that typically
guides autonomous model development. This raises
a key question:are standard task objectives sufficient
to guide agents toward models suitable for real-world
medical use?
Existing benchmarks evaluate autonomous model
development across general machine learning and
biomedical tasks, but largely focus on primary task
performance. A unified evaluation of primary perfor-
mance, risk calibration, and external validation is still
missing (Table 1). This leaves open whether mod-
els optimized for strong task performance also satisfy
broader requirements for medical use. We address this
gap by evaluating these properties together and ana-
1Code: https://github.com/Edwin0080/Auto-MD-ben
ch. Data for 10 of the 15 tasks: https://huggingface.co/d
atasets/Edwin0080/Auto-MD-bench.
arXiv:2610.25069v1  [cs.LG]  18 Oct 2026

Auto-MD-bench
lyzing how agents’ modeling choices relate to the re-
sulting differences.
We introduce Auto-MD-bench, comprising 15 medical
prediction tasks from 10 clinical datasets spanning sur-
vival analysis, classification, and sequential prediction,
with external validation across cohorts, hospitals, and
time periods. Agents choose their modeling and val-
idation procedures using labeled training data, while
test outcomes remain hidden throughout model devel-
opment. We evaluate the resulting models on primary
task performance, risk calibration, and performance
under population shift, and analyze their code and
development records to characterize how the agents
build and revise their models. Figure 1 summarizes
the benchmark workflow.
We evaluate four agents: AIDE, AI Scientist v2,
Codex, and Autoresearch. Both Codex and Autore-
search exceed the simple baseline models in mean pri-
mary score, while their mean calibration errors are
roughly three times as large. Across agents, mod-
els with similar primary scores can exhibit markedly
different calibration, and performance varies substan-
tially across population shifts. Analysis of the devel-
oped models identifies modeling practices associated
with these calibration differences. In an additional ex-
periment on UCI Diabetes, explicitly including cali-
bration in the stated objective changes agents’ model-
ing choices and reduces mean ECE from 0.172 to 0.016
while maintaining similar AUROC. Together, these re-
sults show that the primary task objective provides an
incomplete specification of model quality for medical
use.
Our contributions are:
•We introduce Auto-MD-bench, a benchmark of 15
medical prediction tasks from 10 clinical datasets
that evaluates autonomous model development
beyond the primary task metric, including risk
calibration and external validation across cohorts,
hospitals, and time periods.
•Across four agents, we show that strong pri-
mary performance can mask substantial differ-
ences in calibration and performance under pop-
ulation shift. We further show in a controlled ex-
periment that explicitly incorporating calibration
into the objective can substantially improve cal-
ibration while maintaining similar predictive dis-
crimination.
•We extend benchmark evaluation beyond final
model outputs by capturing agents’ code and de-
velopment records, enabling systematic analysis
of how autonomous agents construct, validate,
and revise medical prediction models.
2 RELATED WORK
Autonomous Model Development.Benchmarks
for autonomous model development evaluate agents
through executable machine learning tasks and the
performance of their resulting solutions. MLAgent-
Bench measures agents’ ability to improve existing
implementations, while MLE-bench evaluates end-to-
end model development through Kaggle competitions
(Huang et al., 2023; Chan et al., 2025). DSBench cov-
ers both data analysis and predictive modeling (Jing
et al., 2025). Beyond final task performance, FML-
bench compares research strategies within a common
experimental framework and analyzes how agents ex-
plore and select candidate solutions (Zou et al., 2026).
Automated Medical Model Development.Au-
tomated medical model development spans conven-
tionalAutoMLpipelinesandLLM-drivensystemsthat
generate and revise modeling code. AutoPrognosis 2.0
automates preprocessing, model selection, and hyper-
parameter tuning for diagnostic and prognostic mod-
eling (Imrie et al., 2023). More recent work has
used LLMs to develop clinical classifiers from natu-
ral language instructions (Tayebi Arasteh et al., 2024),
construct interpretable clinical scores (Estévez et al.,
2026), and revise cardiovascular prediction models
with evaluation on external cohorts (Dhingra et al.,
2026).
Biomedical Agent Benchmarks.Biomedical
agent benchmarks cover activities ranging from
model development to coding-intensive data analysis
and broader healthcare workflows. BioML-bench
and BioXArena evaluate model development across
diverse biomedical domains, including patient-level
prediction (Miller et al., 2025; Li et al., 2026).
MedAgentGym emphasizes code-centric biomedical
data science, whereas HealthAgentBench and MedA-
gentBoard evaluate agents across broader healthcare
workflows (Xu et al., 2026; Liu et al., 2026; Zhu
et al., 2026). AutoHealth and ACP-Bench report
calibration analyses alongside predictive performance
(Xia et al., 2026; Lin et al., 2026), while BioXArena
includes evaluation across imaging centers (Li et al.,
2026). Table 1 summarizes calibration and external
validation in these benchmarks.
Evaluation for Medical Use.Clinical prediction
research distinguishes discrimination from risk cali-
bration (Steyerberg et al., 2009; Van Calster et al.,
2019). External validation assesses performance
across patient populations (Royston and Altman,
2013). These perspectives motivate evaluating agent-
developed medical models beyond primary task scores
and relating their performance to modeling practices.
2

Zhou et al.
Task
description
+ data
Code + development
records
Explain performance
differences
Real-world
medical tasks
Survival analysis
Classification
Sequential
prediction
Autoresearch agents
Stated primary
objective
Iterative model
development
Final predictions
Auto-MD-bench
Typical benchmark evaluation
Primary task performance
A B C D
Beyond the primary score
Risk calibration
A B C D
External validation
Cohort A Cohort B
Hospital A Hospital B
Earlier period Later period
Analyzing agent behavior Modeling choices Development trajectories Methodological checks
Figure 1: Overview of Auto-MD-bench. Agents develop medical prediction models under a stated primary
objective. We evaluate primary task performance, risk calibration, and performance under population shift, and
analyze code and development records to help explain performance differences. External validation uses test
data from a different cohort, hospital, or time period; the corresponding setting without population shift uses
training and test data from the same population.
3 THE BENCHMARK
Auto-MD-bench evaluates autoresearch agents that
develop models for medical prediction tasks with a
specified primary metric. To test whether the primary
metric adequately specifies model quality for medical
use, we assess primary task performance alongside risk
calibration and performance under population shift.
We also examine the agents’ code and development
records to characterize their modeling choices and re-
late them to calibration. Figure 1 shows the workflow
from task inputs through autonomous model develop-
ment to evaluation.
3.1 Medical Tasks for Autoresearch Agents
The benchmark comprises 15 medical prediction tasks
from 10 clinical datasets, using structured patient data
to predict clinical outcomes. The tasks cover sur-
vival analysis, classification and sequential prediction.
Agents provide survival curves for survival analysis,
event probabilities for classification, and hourly prob-
abilities and alarms for sequential prediction. The full
tasklist, datasources, outcomes, samplesizes, andpri-
mary metrics are reported in Appendix A (Table 8).
Ten tasks use internal validation on test data from
the source population. Five use external validation
on data from another cohort, hospital or period. One
external validation task also provides 500 labeled pa-
tients from the target hospital for model development.
3.2 Medical Task Workflow
Eachtaskprovidesadescription, labeledtrainingdata,
test features, null predictions in the required submis-
sion format, and a format checker. The description
specifies the prediction target, primary performance
metric and task rules. Agents choose their modeling
approach, write and execute code, train and validate
models using the training data, and revise their models
using execution results and validation scores. Test la-
bels and test scores are unavailable throughout model
development.
Agents submit prediction files for evaluation (Chan
et al., 2025). For each run, we select one submission
using the agent-specific rules in Table 10. After model
development is complete, we score the selected predic-
tions outside the agent’s development environment. A
runisvalidifitsselectedsubmissionpassesthesubmis-
sion format checks; missing, unreadable or malformed
files make it invalid. Appendix E gives the detailed
checks.
3

Auto-MD-bench
Table 1: Coverage of evaluation dimensions relevant to medical use in related agent benchmarks.✓: reported;
✗: not reported. Calibration denotes explicit assessment of probability calibration; external validation uses a
distinct cohort, site, or time period.† MedAgentGym reports task categories.
Evaluation for medical use
Benchmark Domain Tasks Calibration External validation
MLE-bench General ML (Kaggle) 75✗ ✗
HealthAgentBench Healthcare workflows 54✗ ✗
MedAgentBoard Diverse medical tasks 100✗ ✗
MedAgentGym Biomedical data science 129 † ✗ ✗
AutoHealth Health prediction 17✓ ✗
ACP-Bench Computational pathology 41✓ ✗
BioML-bench Biomedical ML 24✗ ✗
BioXArena Biomedical ML 76✗ ✓
Auto-MD-bench (ours)Clinical prediction 15✓ ✓
3.3 Evaluation Metrics
Predictive Performance.We evaluate survival
predictions with adjusted Antolini time-dependent
concordanceC td (Antolini et al., 2005). Classification
tasks use AUROC, except for PhysioNet 2012, which
uses the minimum of sensitivity and positive predic-
tive value (Silva et al., 2012). Sequential prediction
tasks use the PhysioNet/CinC 2019 normalized util-
ity, which rewards timely alarms and penalizes false
and missed alarms (Reyna et al., 2019b).
We normalize each task’s raw scoremrelative to the
scorem 0 of its null predictions:
s= min

1,max

0, m−m 0
1−m 0

.(1)
Here,m 0 = 0.5forC td and AUROC, andm 0 = 0
for the other metrics. Penalized scores assign zero to
invalid runs; non-penalized scores use valid runs only.
Both weight tasks equally (Table 2). See Appendix E
for details.
Simple Baseline Models.We use Cox neural net-
works implemented inpycoxas simple baseline models
for survival analysis (Katzman et al., 2018; Kvamme
et al., 2019) andscikit-learn’s histogram-based
gradient-boosted trees for classification and sequen-
tial prediction. Each simple baseline model uses fixed
hyperparameters and the task’s training data, and is
evaluated with the same metrics and evaluation code
as the agent-developed models. We train each simple
baseline model five times per task and average its pre-
dictive scores and calibration errors across these rep-
etitions. Appendix D gives the model configurations
and training procedures.
Risk Calibration.We use expected calibration er-
ror (ECE) to compare predicted probabilities with ob-
served outcome frequencies (Table 3). For survival
analysis, we group patients by predicted survival prob-
ability at each of three time points. We compare the
mean prediction in each group with its Kaplan–Meier
survival estimate, which accounts for censoring. For
sequential prediction, ECE is computed over patient-
hours. Appendix F defines the bins, time points and
aggregation.
External Validation.We report normalized scores
on the five external validation tasks and their ratios to
the corresponding scores without the population shift
(Table 5). Agents develop models separately for the
internal and external validation tasks. We compare
these ratios with those of the simple baseline models.
Appendix E gives the calculation.
Subgroup Performance.We compare perfor-
mance across age, sex, and recorded race/ethnicity
groups, using AUROC for classification and time-
dependent concordance for survival analysis. Ap-
pendix F gives the group definitions and calculations.
Modeling Methodology.For valid submissions,
we examine the prediction code and supporting devel-
opment records to identify model families, validation
strategies, and approaches to class imbalance and cen-
soring. We use Claude Opus 5.5 for annotation, with
each annotation citing supporting code by file and line
number. We assess annotation consistency through re-
peated annotation (Table 21). We examine how using
averaged ranks as probabilities, class imbalance han-
dling and recalibration relate to differences in ECE
from the simple baseline models (Figure 2). Table 6
summarizes the modeling methods, and Appendix I
defines the calibration groups. We also compare the
code for sampled pairs of submission versions to char-
acterize modeling changes during agent search (Fig-
ure 3; Appendix H).
4

Zhou et al.
Real-Time Rule and Masking Test.At hourt,
sequential predictions may use only the patient’s ob-
servations throughtand information learned from the
training data. To detect violations of this rule, we
mask later observations by removing the end of each
patient’s record, rerun the code that produced the
selected submissions, and compare alarms at the re-
tained hours. We apply this test to valid submissions
from AIDE and AI Scientist v2 on the three sequential
prediction tasks. Appendix G describes the procedure
and reports the results.
4 EXPERIMENTS
4.1 Experimental Setup
Autoresearch Agents and Harness.We evaluate
fourautoresearchagents: Codex, Autoresearch, AIDE,
and AI Scientist v2. Codex is a general-purpose coding
agent (OpenAI, 2025). Autoresearch uses Codex with
the autoresearch protocol (Karpathy, 2026), which in-
structs Codex to build an initial model, then propose
and evaluate one change at a time, retaining changes
thatimprovetheprimarymetriconitsvalidationdata.
AIDE uses greedy tree search (Jiang et al., 2025),
whereas AI Scientist v2 uses best-first tree search orga-
nized into four stages: initial implementation, tuning,
experimentation, and ablation (Yamada et al., 2025).
Experimental Conditions.In the main experi-
ments, all four agents use Qwen3.8 Flash (Alibaba
Cloud, 2026). We evaluate each agent three times on
each of the 15 tasks, with a 12-hour wall-clock budget
for each repetition. Each repetition uses a dedicated
virtual machine with eight CPU threads and 16 GB of
RAM. All agents receive the same task description and
data for a given task. They run in Apptainer contain-
ers with the same preinstalled software and no internet
access.
Implementation Details.We adapt each frame-
work’s input interface to provide the benchmark’s task
descriptions and data. For AI Scientist v2, we use its
experiment stages and disable paper writing and re-
view. Toapplythe12-hourbudget, weraiseAIDE’sit-
eration limit and allocate time across AI Scientist v2’s
stages in proportion to their original iteration quotas.
Appendix C provides configuration and implementa-
tiondetails, includingsoftwareversions, ataskdescrip-
tion example, and the autoresearch instructions.
4.2 Performance on Medical Tasks
The general coding agents achieve higher mean nor-
malized scores than the research agents (Table 2).
Codex and Autoresearch score 0.517 and 0.518, respec-
tively, compared with 0.474 for AIDE and 0.355 for AI
Scientistv2. CodexandAutoresearchexceedthemean
score of the simple baseline models (0.487), and each
exceeds the simple baseline score on 14 of the 15 tasks
(Appendix E). Codex and Autoresearch have similar
mean scores, but Codex achieves a better mean rank
across tasks (1.60 versus 1.80).
AIScientistv2istheonlyagenttoproduceinvalidsub-
missions, with 12 invalid submissions across 45 exper-
iments. Excluding these submissions raises its mean
normalized score from 0.355 to 0.467, close to AIDE’s
0.474 but below Codex and Autoresearch.
4.3 Risk Calibration
High primary scores do not imply well-calibrated pre-
dictions. Codex and Autoresearch exceed the sim-
ple baseline models in mean primary score, but have
roughly three times their average ECE (0.086 and
0.075 versus 0.027; Table 3). For example, two indi-
vidual UCI Diabetes submissions from Codex and AI
Scientist v2 have nearly identical AUROC values of
0.670 and 0.671, but ECE values of 0.006 and 0.154,
respectively.
Most of the ECE difference from the simple baseline
models is concentrated in two groups of experiments
(Figure 2). Experiments using averaged ranks as prob-
abilities account for 75% of this difference and 14% of
valid experiments. Among the remaining experiments,
those that handle class imbalance without recalibra-
tion account for a further 18% of the difference and
9% of all valid experiments. Averaged ranks express
relative ordering rather than event probabilities, while
handling class imbalance changes the relative weight
of events and non-events during training and can dis-
tort the resulting probabilities. For experiments that
handle class imbalance but do not use averaged ranks,
mean ECE is 0.008 with subsequent recalibration and
0.160 without it.
To test whether explicitly specifying calibration
changes model development, we compare the main ex-
periment’s AUROC objective on UCI Diabetes with
two alternatives: Brier score, which reflects both dis-
crimination and calibration, and AUROC with ECE.
We specify each objective in the task description and
use three repetitions of each of the four agents, with
thesameLLM,data, andtimebudget. AddingECEto
the stated AUROC objective reduces mean ECE from
0.172to0.016whilemaintainingsimilarmeanAUROC
(0.676 versus 0.683; Table 4). In this condition, nei-
ther using ranks as probabilities nor handling class im-
balance without recalibration is observed. With Brier
score, mean ECE also decreases, to 0.061, but mean
5

Auto-MD-bench
Table 2: Primary task performance on 15 tasks with Qwen3.8 Flash. Scores and valid run rates are mean±
SD over three repetitions; ranks are mean±SD across tasks. Penalized scores assign zero to invalid runs; non-
penalized scores exclude them. Bold: best agent value per metric.
Normalized score↑Mean rank↓Valid
System penalized non-pen. penalized non-pen. runs
Simple baseline models0.487 – –
AIDE 0.474±0.032 0.474±0.032 2.93±0.88 3.13±0.99 100.0%±0.0%
Codex 0.517±0.003 0.517±0.0031.60±0.511.60±0.51 100.0%±0.0%
Autoresearch0.518±0.0060.518±0.006 1.80±0.77 1.80±0.77 100.0%±0.0%
AI Scientist v2 0.355±0.064 0.467 3.67±0.82 3.47±0.83 73.3%±13.3%
Table 3: Expected calibration error (ECE; lower is better) by agent and task class. Bold: lowest value per
column.
All Survival analysis Classification Sequential prediction
AIDE 0.128 0.045 0.280 0.066
Codex 0.086 0.076 0.113 0.065
Autoresearch 0.075 0.061 0.087 0.090
AI Scientist v2 0.072 0.048 0.102 0.078
Simple baseline models0.027 0.027 0.031 0.018
0 25 50 75
Contribution to the ECE gap (%)
Averaged ranks as
probabilities
Imbalance handling
without recalibration
Other experiments
75%
18%
7%
Without
recalibration
With
recalibration
0.0
0.2
0.4
0.6
ECE
0.160
0.008
Experiment
Mean
(a) Modeling practices (b) Recalibration after imbalance handling
Figure 2: Calibration error and modeling practices. (a) Contributions to the ECE gap relative to task-specific
simple baseline models. (b) ECE after agents handle class imbalance, with or without recalibration. Circles show
individual experiments; diamonds show group means. Group definitions are in Appendix I.
Table 4: Calibration under three evaluation objectives
on UCI Diabetes (mean±SD over valid runs). Bold:
best value across objectives.
Objective AUROC↑ECE↓
AUROC 0.676±0.023 0.172±0.211
Brier score 0.640±0.107 0.061±0.157
AUROC and ECE0.683±0.0160.016±0.023
AUROC is lower at 0.640. These results show that in-
cluding calibration in the stated objective can change
modeling choices and improve calibration on this task.
Appendix F.1 provides results by agent and code an-
notations.
4.4 Generalization across Different
Populations
External Validation.Performance under popula-
tion shift varies substantially across tasks (Table 5).
OnRotterdam→GBSG,scoresunderpopulationshift
6

Zhou et al.
Table 5: Performance under population shift. Entries are mean normalized scores; parentheses give ratios to the
corresponding score without the population shift. Bold: best score per setting;∗ one valid run.
External validation setting
Simple baseline
models AIDE Codex Autoresearch AI Scientist v2
Rotterdam→GBSG (cohort) 0.372 (100%) 0.306 (86%)0.385(99%) 0.371 (97%) 0.332 (85%)
SEER (temporal) 0.724 (99%) 0.730 (97%)0.745(103%) 0.735 (99%) 0.670 ∗ (–)
eICU (hospital) 0.736 (99%) 0.748 (99%)0.751(100%)0.751(100%) 0.705 (100%)
Sepsis (hospital) 0.199 (52%) 0.168 (41%) 0.231 (52%)0.268(61%) 0.228 ∗ (63%)
Sepsis + 500 target labels 0.248 (65%) 0.217 (54%)0.299(67%) 0.253 (57%) 0.124 ∗ (34%)
are 85–86% of the corresponding scores without the
shift for the research agents and 97–99% for the coding
agents. Ratios are lower on both sepsis tasks: 41–63%
onSepsis, new hospitaland 34–67% onSepsis, 500
local labels. OnSEER, later periodandeICU, new
hospitals, performance changes little under the popu-
lation shift, with ratios close to 100%.
Codex and Autoresearch achieve higher scores under
population shift than the two research agents on all
five tasks. Codex exceeds the simple baseline score on
every task, while Autoresearch exceeds it on four and
closely matches it on Rotterdam→GBSG. The corre-
sponding ratios for Codex and Autoresearch are also
close to those of the simple baseline models. The ra-
tios for AIDE and AI Scientist v2 are approximately 8
and 9 percentage points lower than the corresponding
simple baseline ratios, respectively, on average. These
results show that performance under population shift
isanadditionalpropertythatmustbeevaluatedrather
than inferred from the primary score alone.
Subgroup Performance.Aggregate scores also
mask differences between patient subgroups. In the
four ICU mortality tasks, the oldest age tertile is the
lowest-scoring age group in every valid experiment
(Appendix Table 14). The mean difference between
the highest- and lowest-scoring age groups ranges from
0.065 to 0.084, similar to the 0.065–0.078 differences
for the simple baseline models. Across all tasks, agents
check performance by age or sex in only six of 168 valid
experiments. Appendix F reports the full subgroup re-
sults, including sex and race/ethnicity.
4.5 Machine Learning Model Choice by
Different Autoresearch Agents
We examine the methods used to build these models
to assess their handling of validation, probability cali-
bration, and clinical information.
Model Families and Ensembles.Gradient-
boosted trees dominate model choice, appearing in 76–
89% of valid experiments across the four agents (Ta-
ble 6). The agents differ more in how they combine
models: Codex and Autoresearch average predictions
across seeds or folds in 89% of experiments, compared
with 62% for AIDE and 31% for AI Scientist v2. AI
Scientist v2 uses a single model in 36% of experiments,
compared with 2–13% for the other agents.
Validation and Calibration.AI Scientist v2 also
relies on a single holdout split more often: 37% of ex-
periments, versus 4–13% for the other agents. Proba-
bility calibration is uncommon across all four agents,
appearing in 2–22% of experiments.
Modeling Changes during Agent Search.
Changes to ensembling are frequent for Codex and Au-
toresearch, appearingin64–89%ofsampledpairs(Fig-
ure 3). Hyperparameter tuning is less frequent in late
than in early pairs for all four agents. Feature changes
alsodeclineinCodexandAutoresearch, reaching3–4%
in late pairs. AI Scientist v2, which follows a prede-
fined four-stage workflow, instead shows more feature
changes in later pairs.
Censoring and Temporal Information.Code re-
view identifies errors in handling censored outcomes
in eight of the 79 valid survival submissions. The er-
rors occur in ensemble members and include treating
censored patients as observed deaths or as known sur-
vivors at later time points, and using incorrect cen-
soring weights. All eight submissions exceed their
task’s simple baseline score despite these errors. Thus,
success on the primary score can coexist with errors
in how the underlying medical prediction problem is
modeled.
The masking test detects violations of the real-time
rule in three of the 13 valid sequential prediction ex-
periments tested for AIDE and AI Scientist v2. All
three occur in AIDE and use information from later
hours to determine earlier predictions or alarms. Ap-
pendix G reports the cases and test results.
7

Auto-MD-bench
Table 6: Modeling methods in valid experiments (mean±SD over three repetitions; categories can overlap).
Method AIDE Codex Autoresearch AI Scientist v2
Model family
Gradient-boosted trees 87%±0% 89%±8% 89%±8% 76%±13%
Neural networks 11%±8% 31%±17% 38%±10% 36%±10%
Ensembling and validation
Averaging across seeds or folds 62%±14% 89%±4% 89%±10% 31%±7%
Single model only 13%±12% 2%±4% 4%±8% 36%±10%
Single holdout split only 9%±4% 4%±4% 13%±7% 37%±16%
Calibration
Probability calibration 2%±4% 22%±10% 22%±8% 14%±12%
Early Middle Late
0%
20%
40%
60%
80%
100%
AIDE
Early Middle Late
Codex
Early Middle Late
 Early Middle Late
AI Scientist v2
Ensembling Hyperparameter tuning Feature engineering
Autoresearch
Solution pairs with change (%)
Search progress
Figure 3: Modeling changes during agent search. Points show the percentage of sampled solution pairs containing
each type of modeling change. Early, middle, and late indicate relative positions in the chronologically ordered
sequence of solution pairs within each run, rather than equal intervals of elapsed time. Pairs may contain multiple
types of change.
Table 7: Codex with three LLMs. Scores are mean
±SD over three repetitions; ECE is averaged across
tasks. Bold: best value per metric.
LLM Normalized score↑ECE↓
Qwen3.8 Flash 0.517±0.003 0.086
gpt-6-luna 0.517±0.004 0.041
Gemini 3.8 Flash0.520±0.0060.029
4.6 Effect of the LLM
Keeping Codex fixed, we evaluate two additional
LLMs on all 15 tasks, with three repetitions per task,
the same data, and a 12-hour time budget. Mean
normalized scores are similar across Qwen3.8 Flash,
gpt-6-luna, and Gemini 3.8 Flash, ranging from 0.517
to 0.520 (Table 7). Calibration differs substantially:
mean ECE is 0.086, 0.041, and 0.029, respectively.
Gemini 3.8 Flash’s mean ECE is close to the simple
baseline models’ mean ECE of 0.027. The three LLMs
achieve nearly identical mean primary scores, but their
calibration differs substantially. Appendix J reports
submission validity and token usage.
5 CONCLUSION
We introduced Auto-MD-bench to examine whether
the common practice of guiding autonomous agents
with a single primary metric is sufficient for develop-
ing models that satisfy broader requirements for med-
ical use. Across 15 tasks from 10 clinical datasets,
models with similar primary performance could dif-
fer markedly in risk calibration and in performance
under population shift. Our analysis connected these
differences to concrete modeling choices, while explic-
itly incorporating calibration into model development
substantially improved calibration while maintaining
similar discrimination. These results show that pri-
mary task performance provides only a partial view
of the models produced by autonomous agents. More
broadly, the metric used to guide model development
can influence which properties of the resulting model
are prioritized. Evaluating autonomous medical model
development should therefore look beyond a single pri-
mary metric and consider the broader properties re-
quired by the intended medical use.
8

Zhou et al.
AI Use Statement
Claude and OpenAI Codex assisted with experiment
design, implementation, data preparation, literature
searches, analysisofexperimentalresults, figureprepa-
ration, and manuscript drafting and revision. Chat-
GPT assisted with manuscript revision. Claude Opus
5.5 annotated the agents’ code using the procedure in
Appendix I. The LLMs evaluated in the benchmark
are described in Section 4.1 and Appendix J. The au-
thors take responsibility for the final content of this
work.
References
Alibaba Cloud. Qwen3.8-Flash.https://www.alibab
acloud.com/help/en/model-studio/qwen3-8-f
lash, 2026. Model Studio documentation. Accessed:
2026-10-06.
Laura Antolini, Patrizia Boracchi, and Elia Bigan-
zoli. A time-dependent discrimination index for sur-
vival data.Statistics in medicine, 24(24):3927–3944,
2005.
Jun Shern Chan, Neil Chowdhury, Oliver Jaffe, James
Aung, Dane Sherburn, Evan Mays, Giulio Starace,
Kevin Liu, Leon Maksin, Tejal Patwardhan, et al.
Mle-bench: Evaluating machine learning agents on
machine learning engineering. InInternational Con-
ference on Learning Representations, volume 2025,
pages 50466–50494, 2025.
John Clore, Krzysztof Cios, Jon DeShazo, and Beata
Strack. Diabetes 130-US Hospitals for Years 1999-
2008. UCIMachineLearningRepository, 2014. DOI:
https://doi.org/10.24432/C5230J.
Alfred F Connors, Neal V Dawson, Norman A Desbi-
ens, William J Fulkerson, Lee Goldman, William A
Knaus, Joanne Lynn, Robert K Oye, Marilyn
Bergner, Anne Damiano, et al. A controlled trial
to improve care for seriously iii hospitalized pa-
tients: The study to understand prognoses and pref-
erences for outcomes and risks of treatments (sup-
port).Jama, 274(20):1591–1598, 1995.
Christina Curtis, Sohrab P Shah, Suet-Feung Chin,
GulisaTurashvili, OscarMRueda, MarkJDunning,
Doug Speed, Andy G Lynch, Shamith Samarajiwa,
Yinyin Yuan, et al. The genomic and transcriptomic
architecture of 2,000 breast tumours reveals novel
subgroups.Nature, 486(7403):346–352, 2012.
Lovedeep S Dhingra, Bruno Batinica, Ryan B Choi,
Philip M Croon, Evangelos K Oikonomou, and
Rohan Khera. Autonomous agents for auditable
cardiovascular artificial intelligence development.
medRxiv, pages 2026–07, 2026.
Silas Ruhrberg Estévez, Christopher Chiu, and Mi-
haela van der Schaar. Automatic construction of
clinical scoring systems with llm agents.arXiv
preprint arXiv:2601.22324, 2026.
Qian Huang, Jian Vora, Percy Liang, and Jure
Leskovec. Mlagentbench: Evaluating language
agents on machine learning experimentation.arXiv
preprint arXiv:2310.03302, 2023.
Fergus Imrie, Bogdan Cebere, Eoin F McKinney, and
Mihaela van der Schaar. Autoprognosis 2.0: De-
mocratizing diagnostic and prognostic modeling in
healthcare with automated machine learning.PLOS
digital health, 2(6):e0000276, 2023.
Zhengyao Jiang, Dominik Schmidt, Dhruv Srikanth,
Dixing Xu, Ian Kaplan, Deniss Jacenko, and Yuxi-
ang Wu. Aide: Ai-driven exploration in the space
of code.arXiv preprint arXiv:2502.13138, 2025.
Liqiang Jing, Zhehui Huang, Xiaoyang Wang, Wen-
lin Yao, Wenhao Yu, Kaixin Ma, Hongming Zhang,
Xinya Du, and Dong Yu. Dsbench: How far are data
science agents from becoming data science experts?
InInternational Conference on Learning Represen-
tations, volume 2025, pages 32597–32649, 2025.
Alistair Johnson, Lucas Bulgarelli, Tom Pollard, Brian
Gow, Benjamin Moody, Steven Horng, Leo Anthony
Celi, and Roger Mark. MIMIC-IV.PhysioNet,
October 2024. doi: 10.13026/kpb9-mt58. URL
https://doi.org/10.13026/kpb9-mt58. Version
3.1.
AlistairEWJohnson, LucasBulgarelli, LuShen, Alvin
Gayles, Ayad Shammout, Steven Horng, Tom J Pol-
lard, Sicheng Hao, Benjamin Moody, Brian Gow,
et al. Mimic-iv, a freely accessible electronic health
record dataset.Scientific data, 10(1):1, 2023.
Andrej Karpathy. autoresearch.https://github.com
/karpathy/autoresearch, 2026. Accessed: 2026-
10-06.
Jared L Katzman, Uri Shaham, Alexander Cloninger,
Jonathan Bates, Tingting Jiang, and Yuval Kluger.
Deepsurv: personalized treatment recommender
system using a cox proportional hazards deep neural
network.BMC medical research methodology, 18(1):
24, 2018.
Håvard Kvamme, Ørnulf Borgan, and Ida Scheel.
Time-to-event prediction with neural networks and
cox regression.Journal of machine learning re-
search, 20(129):1–30, 2019.
Loka Li, Duzhen Zhang, Xingbo Du, Leonard Song,
Zixiao Wang, Assanali Aukenov, Noel Thomas,
Shakhnazar Sailaukan, Yonghan Yang, Feilong
Chen, et al. Bioxarena: Benchmarking llm agents
on multi-modal biomedical machine learning tasks.
arXiv preprint arXiv:2605.15766, 2026.
9

Auto-MD-bench
Jie Lin, Zongyi Chen, Qiaoling Zheng, Liuyi Wang,
Hengyi Jiang, Jiabao Chen, Xiang Liu, Yinghong
Yang, and Liansheng Wang. Evaluating agentic har-
ness systems for autonomous computational pathol-
ogy.arXiv preprint arXiv:2607.02598, 2026.
Qianchu Liu, Sheng Zhang, Guanghui Qin, Jeya
Maria Jose Valanarasu, Maximilian Rokuss, Mingyu
Lu, Timothy Ossowski, Juan Manuel Zambrano
Chaves, Cliff Wong, Peniel Argaw, et al. Healtha-
gentbench: A unified benchmark suite of realis-
tic agentic healthcare environments for challenging
frontier ai agents.arXiv preprint arXiv:2606.31179,
2026.
Henry E Miller, Matthew Greenig, Benjamin Ten-
mann, and Bo Wang. Bioml-bench: Evaluation of ai
agents for end-to-end biomedical ml.bioRxiv, pages
2025–09, 2025.
National Center for Health Statistics Division of
Analysis and Epidemiology. Continuous NHANES
Public-use Linked Mortality Files, 2019. Hyattsville,
Maryland. Available from:https://www.cdc.go
v/nchs/data-linkage/mortality-public.htm,
2022.
OpenAI. Codex CLI.https://github.com/openai/
codex, 2025. Accessed: 2026-10-06.
Tom Pollard, Alistair Johnson, Jesse Raffa, Leo An-
thony Celi, Omar Badawi, and Roger Mark. eICU
Collaborative Research Database.PhysioNet, April
2019. doi: 10.13026/C2WM1R. URLhttps:
//doi.org/10.13026/C2WM1R. Version 2.0.
Tom Pollard, Benjamin E. Moody, Li-wei H. Lehman,
Brian J. Gow, Chrystinne Fernandes, Chen Xie, Al-
istair Johnson, Roger G. Mark, and Thomas Heldt.
PhysioNet as a global platform for biomedical re-
search.Nature Health, 1(8):792–795, August 2026.
ISSN 3005-0693. doi: 10.1038/s44360-026-00096-z.
URLhttps://doi.org/10.1038/s44360-026-000
96-z.
Tom J Pollard, Alistair EW Johnson, Jesse D Raffa,
Leo A Celi, Roger G Mark, and Omar Badawi. The
eicu collaborative research database, a freely avail-
able multi-center database for critical care research.
Scientific data, 5(1):180178, 2018.
Matthew Reyna, Chris Josef, Russell Jeter, Supreeth
Shashikumar, Benjamin Moody, M. Brandon West-
over, Ashish Sharma, Shamim Nemati, and Gari D.
Clifford. Early Prediction of Sepsis from Clini-
cal Data: The PhysioNet/Computing in Cardiol-
ogy Challenge 2019.PhysioNet, August 2019a. doi:
10.13026/v64v-d857. URLhttps://doi.org/10.1
3026/v64v-d857. Version 1.0.0.
Matthew A Reyna, Chris Josef, Salman Seyedi, Rus-
sell Jeter, Supreeth P Shashikumar, M Brandon
Westover, Ashish Sharma, Shamim Nemati, and
Gari D Clifford. Early prediction of sepsis from clin-
ical data: the physionet/computing in cardiology
challenge 2019. In2019 Computing in Cardiology
(CinC), pages Page–1. IEEE, 2019b.
Patrick Royston and Douglas G Altman. External val-
idation of a cox prognostic model: principles and
methods.BMC medical research methodology, 13
(1):33, 2013.
Ikaro Silva, George Moody, Daniel J Scott, Leo A Celi,
and Roger G Mark. Predicting in-hospital mortality
oficupatients: Thephysionet/computingincardiol-
ogy challenge 2012. In2012 computing in cardiology,
pages 245–248. IEEE, 2012.
Ewout W Steyerberg et al.Clinical prediction models:
a practical approach to development, validation, and
updating, volume 19. Springer, 2009.
Beata Strack, Jonathan P DeShazo, Chris Gennings,
Juan L Olmo, Sebastian Ventura, Krzysztof J Cios,
and John N Clore. Impact of hba1c measurement on
hospital readmission rates: analysis of 70,000 clin-
ical database patient records.BioMed research in-
ternational, 2014(1):781670, 2014.
Surveillance, Epidemiology, and End Results (SEER)
Program. SEER*Stat Database: Incidence - SEER
Research Data, 17 Registries, Nov 2025 Sub (2000-
2023) - Linked To County Attributes - Time Depen-
dent (1990-2024) Income/Rurality, 1969-2024 Coun-
ties. National Cancer Institute, DCCPS, Surveil-
lance Research Program, released April 2026, based
on the November 2025 submission.https://www.
seer.cancer.gov, 2026.
Soroosh Tayebi Arasteh, Tianyu Han, Mahshad
Lotfinia, Christiane Kuhl, Jakob Nikolas Kather,
Daniel Truhn, and Sven Nebelung. Large language
models streamline automated machine learning for
clinical studies.Nature Communications, 15(1):
1603, 2024.
Ben Van Calster, David J McLernon, Maarten
Van Smeden, Laure Wynants, Ewout W Steyerberg,
Topic Group ‘Evaluating diagnostic tests, and pre-
diction models’ of the STRATOS initiative Bossuyt
Patrick Collins Gary S. Macaskill Petra McLernon
David J. Moons Karel GM Steyerberg Ewout W.
Van Calster Ben van Smeden Maarten Vickers An-
drew J. Calibration: the achilles heel of predictive
analytics.BMC medicine, 17(1):230, 2019.
Tong Xia, Weibin Li, Gang Liu, and Yong Li. Au-
tohealth: An uncertainty-aware multi-agent sys-
tem for autonomous health data modeling.arXiv
preprint arXiv:2602.01078, 2026.
Ran Xu, Yuchen Zhuang, Yishan Zhong, Yue Yu,
Zifeng Wang, Xiangru Tang, Hang Wu, May Dong-
10

Zhou et al.
mei Wang, Peifeng Ruan, Donghan Yang, et al.
Medagentgym: A scalable agentic training environ-
ment for code-centric reasoning in biomedical data
science. InInternational Conference on Learning
Representations, volume 2026, pages 89688–89730,
2026.
Yutaro Yamada, Robert Tjarko Lange, Cong Lu,
Shengran Hu, Chris Lu, Jakob Foerster, Jeff Clune,
and David Ha. The ai scientist-v2: Workshop-
level automated scientific discovery via agentic tree
search.arXiv preprint arXiv:2504.08066, 2025.
Yinghao Zhu, Ziyi He, Haoran Hu, Xiaochen Zheng,
Xichen Zhang, Jiyao Wang, Junyi Gao, Liantao Ma,
and Lequan Yu. Medagentboard: Benchmarking
multi-agent collaboration with conventional meth-
ods for diverse medical tasks.Advances in Neural
Information Processing Systems, 38, 2026.
Qiran Zou, Hou Hei Lam, Wenhao Zhao, Tingting
Chen, Yiming Tang, Samson Yu, Yingtao Zhu,
Srinivas Anumasa, Zufeng Zhang, Tianyi Zhang,
et al. Fml-bench: A controlled study of ai research
agent strategies from the perspective of search dy-
namics.arXiv preprint arXiv:2605.17373, 2026.
11

Auto-MD-bench: Supplementary Materials
A DATASETS
Table 8: The 15 tasks in Auto-MD-bench. Sample sizes are patients unless noted; UCI Diabetes counts encoun-
ters. Matching symbols indicate shared test sets.C td: time-dependent concordance; Utility: PhysioNet/CinC
2019 challenge score.
Task Data source Outcome Validation Metric Train / test
Survival analysis
SUPPORT Cohort Death InternalC td 7,098 / 1,775
METABRIC Cohort Death InternalC td 1,523 / 381
Rotterdam Cohort Recurrence or death InternalC td 2,385 / 597
Rotterdam→GBSG Cohort→trial Recurrence or death External (cohort)C td 2,982 / 686
SEER† Registry Breast-cancer death InternalC td 232,625 / 49,291
SEER, later period† Registry Breast-cancer death External (period)C td 183,334 / 49,291
NHANES Survey Death InternalC td 11,639 / 2,910
Classification
UCI Diabetes EHR 30-day readmission Internal AUROC 81,347 / 20,419
PhysioNet 2012 EHR (ICU) In-hospital death Internalmin(Se,PPV)4,000 / 8,000 stays
MIMIC-IV EHR (ICU) In-hospital death Internal AUROC 41,471 / 10,368
eICU‡ EHR (ICU) In-hospital death Internal AUROC 94,823 / 11,133 stays
eICU, new hospitals‡ EHR (ICU) In-hospital death External (hospital) AUROC 83,626 / 11,133 stays
Sequential prediction
Sepsis EHR (ICU) Sepsis onset Internal Utility 32,268 / 8,068
Sepsis, new hospital§ EHR (ICU) Sepsis onset External (hospital) Utility 20,336 / 4,000
Sepsis, 500 local labels§ EHR (ICU) Sepsis onset External (hospital) Utility 20,336 + 500 / 4,000
Table 9: Source datasets.
Dataset Content Access
SUPPORT (Connors et al., 1995)∼9,100 seriously ill inpatients, 5 US hospitals, 1989–94 public
METABRIC (Curtis et al., 2012)∼2,000 breast tumors with genomic profiles public
Rotterdam, GBSG (Royston and Altman,
2013)
breast cancer registry (1978–93) and trial (1984–89) public
UCI Diabetes (Strack et al., 2014; Clore
et al., 2014)
101,766 encounters involving patients with diabetes, 130
US hospitals, 1999–2008
public
PhysioNet/CinC 2012 (Silva et al., 2012) 12,000 ICU stays, first 48 h public
PhysioNet/CinC 2019 (Reyna et al.,
2019b,a)
hourly ICU records labeled for sepsis onset, 40,336
patients, 2 hospital systems
public
MIMIC-IV (Johnson et al., 2023, 2024) Beth Israel Deaconess EHR, 2008–22 credentialed
eICU-CRD (Pollard et al., 2018, 2019)∼200,000 ICU stays, 208 US hospitals, 2014–15 credentialed
SEER (Surveillance, Epidemiology, and
End Results (SEER) Program, 2026)
US cancer registry, breast cancer 2010–15 data agreement
NHANES (National Center for Health
Statistics Division of Analysis and
Epidemiology, 2022)
US health survey linked to death records public
Task Construction.Test sets are fixed across runs; Table 8 gives the sample sizes. Unless specified below,
we use an 80/20 patient split with random seed 42.

Zhou et al.
A.1 Survival Analysis
SUPPORT and METABRIC.These tasks predict time to death from the processed datasets distributed
withpycox(Connors et al., 1995; Curtis et al., 2012). SUPPORT has 14 clinical covariates and follow-up in
days; METABRIC has four gene-expression markers and five clinical covariates, with follow-up in months. Both
use generic covariate names and unstratified patient splits.
Rotterdam and Rotterdam→GBSG.The Rotterdam and GBSG cohorts are distributed together in the
Rsurvivalpackage. Both tasks predict recurrence or death from eight harmonized clinical covariates (Royston
and Altman, 2013). For Rotterdam, follow-up is the minimum of the recorded recurrence and death times in
days; either outcome counts as an event. The internal task splits Rotterdam patients with stratification by event
status. The external task trains on the full Rotterdam cohort and tests on the independent GBSG cohort, using
its supplied recurrence-free survival time and event status.
SEER and SEER, Later Period.The cohort includes women with a first malignant breast-cancer diagnosis
in 2010–2015. Inputs are 22 coded demographic, tumor and treatment variables (Surveillance, Epidemiology,
and End Results (SEER) Program, 2026). The outcome is breast-cancer death, with follow-up in months; deaths
from other causes are censored at death. We exclude deaths with unknown cause and retain records flagged as
having complete dates and positive follow-up. Both tasks test on the same randomly selected half of patients
diagnosed in 2014–2015. SEER trains on all remaining patients, whereasSEER, later periodtrains only on
diagnoses from 2010–2013.
NHANES.The task predicts all-cause mortality after examination from the 2011–2016 survey cycles linked to
mortality follow-up through 2019 (National Center for Health Statistics Division of Analysis and Epidemiology,
2022). We retain linkage-eligible adults aged at least 20 years with positive follow-up and examination weights.
The 25 inputs include clinical and demographic variables, survey weight, stratum, primary sampling unit and
cycle. Follow-up is measured in months, and the patient split is stratified by event status.
Survival Time Grids.The time grid specifies when models must report survival probabilities. We use the
unique quantiles of event times in the training data at 100 evenly spaced levels from 0 to 1, adding time zero.
The two SEER tasks share the grid from the 2010–2013 training data.
A.2 Classification
UCI Diabetes.The task predicts readmission within 30 days of a hospital encounter (Strack et al., 2014).
We remove three fields with more than 40% missing values and ordinal-encode categorical variables, leaving
44 predictors. Patients are split with stratification by whether they ever have a positive readmission label; all
encounters of a patient remain together. Patient identifiers are retained in training data and removed from test
features.
PhysioNet 2012.The task predicts in-hospital death from irregular observations over the first 48 hours of
an ICU stay (Silva et al., 2012). Inputs are supplied in long format with observation times, variable names and
values. Challenge set A supplies training data; sets B and C together form the test set.
MIMIC-IV.The task predicts in-hospital death for adults whose first ICU stay lasts at least 24 hours (Johnson
et al., 2023). Its 73 inputs combine first-24-hour vital-sign and laboratory summaries with demographics and
additional clinical variables. The patient split is stratified by the mortality label.
eICU and eICU, New Hospitals.Both tasks predict in-hospital death for adult ICU stays of at least one
day with APACHE predictor records (Pollard et al., 2018). Their 80 inputs combine first-24-hour vital-sign and
laboratory summaries with demographics, clinical assessments and admission information. We randomly select
hospitals until they cover at least 20% of cohort stays, then use half of their patients for the shared test set. The
eICU task trains on all non-test patients;eICU, new hospitalstrains only on the other hospitals. Every stay of
a test patient is excluded from both training sets. Hospital identifiers are not supplied as predictors.
13

Auto-MD-bench
A.3 Sequential Prediction
Hourly Inputs and Target.All three tasks use PhysioNet/CinC 2019 records from hospitals A and B (Reyna
et al., 2019b). Each patient-hour has 40 variables covering vital signs, laboratory measurements and demographic
or administrative information, plus a hospital indicator. The supplied label becomes positive six hours before
sepsis onset and remains positive thereafter.
Internal and External Tasks.TheSepsistask splits patients from both hospitals, stratified by hospital and
whether they ever develop sepsis. The two external tasks use the hospital-B patients in this test set as their
shared test set.Sepsis, new hospitaltrains on all hospital-A patients.Sepsis, 500 local labelsadds 500 labeled
hospital-B patients sampled from outside the test set, stratified by whether they ever develop sepsis.
B DATA ACCESS AND HANDLING
Data Sources and Access.Table 9 lists the data sources and access conditions. MIMIC-IV and eICU-CRD
require credentialed access through PhysioNet (Pollard et al., 2026); SEER Research data require a data-use
agreement. The other sources are publicly accessible. The National Center for Health Statistics is responsible
only for the initial NHANES linked mortality data, not for the analyses, interpretations or conclusions in this
paper.
Data Handling.Agents access training data and test features through code executed in Apptainer containers.
Test outcomes remain outside the agent environment and are used for evaluation after each run. LLM interactions
can include data excerpts and summaries returned by the agents’ code.
C AGENT CONFIGURATIONS
Table 10: Agent systems, search strategies and submission selection.
Agent Type Search strategy Submission selection
Codex coding agent agent-directed finalsubmission.csv
Autoresearch coding agent greedy search finalsubmission.csv
AIDE research agent greedy tree search best self-reported validation score
AI Scientist v2 research agent best-first tree search submission from the selected node in the
latest stage with a saved submission
Implementations and Task Inputs.We use Codex CLI v0.149.1, AIDE v0.2.2 and AI Scientist v2 (commit
96bd516). Codex reads the task description from its working directory. Autoresearch also receivesprogram.md,
reproduced below, and instructions to follow it. Neither Codex configuration receives starter code. AIDE
receives the description through its task-description interface and the task files in its data directory. AI Scientist
v2 receives the full description in both the Abstract and Experiments fields of its idea file, with task files copied
into each node’s working directory. We disable AIDE’s final report and AI Scientist v2’s writing and review
stages.
Search and Execution Settings.We enforce a 12-hour wall-clock limit for each experiment. AIDE’s step
limit is 100,000. AI Scientist v2 allocates time across its four experimental stages in proportion to their original
iteration quotas,20:12:12:18. At the start of each main stage, it divides the remaining time among the remaining
stages in these proportions. Each stage allows 100,000 iterations. AI Scientist v2 uses four workers, three initial
drafts, a maximum debugging depth of three, and three-seed evaluation of its selected node at stage transitions.
Both frameworks allow 3,600 seconds per node execution.
Framework Adaptations.We patch AIDE and AI Scientist v2 to record failed script executions as failed
nodes and treat metrics with incompatible types or optimization directions as incomparable. If an AI Scientist
v2 sub-stage has no usable implementation, the framework can use the best implementation from the most recent
earlier sub-stage within the same main stage that has a usable implementation.
14

Zhou et al.
Submission Selection.For Codex and Autoresearch, we evaluatesubmission.csvwhen the run ends. For
AIDE, we use its reported validation metric to select the highest-ranked node that is not marked as faulty by
the agent and has an available prediction file. For AI Scientist v2, we inspect sub-stages from latest to earliest.
In each, we use the saved best-node identifier if that node is not marked as faulty; otherwise, we compare nodes
not marked as faulty using the agent’s metric rule. We select the first such node with its own saved submission,
skipping sub-stages whose selected node has none. If this procedure finds no prediction file, we evaluate the file
left in the working directory. Selection does not use test scores.
Table 11: Tokens per run (millions; mean±SD over three repetitions).
Agent Input Output
AIDE 0.65±0.05 0.28±0.02
Codex 26.88±1.86 0.17±0.01
Autoresearch 51.44±13.23 0.30±0.08
AI Scientist v2 4.29±0.63 1.69±0.24
Example Task Description.The following is an excerpt from the task description for UCI Diabetes.
# Task: 30-day readmission prediction (Diabetes, 130 US hospitals)
Predict whether a hospital encounter of a diabetic patient is followed by a
**readmission within 30 days**. One row per ENCOUNTER; columns:
-`encounter_id`— the unit you predict for
-`patient_nbr`— patient identifier, **train only**. Patients can have
several encounters; the hidden test split is at PATIENT level. The test file
has NO patient identifier and its rows are shuffled: every test row stands
on its own.
- ~40 features (demographics, admission details, diagnoses, lab counts,
medications). Categorical columns arrive ordinal-encoded; missing = NaN.
-`label`(train only): 1 = readmitted within 30 days (~11% of encounters).
## Files
| file | contents |
|---|---|
|`train.csv`| ~81k encounters WITH labels |
|`test_features.csv`| ~20k encounters, features only |
|`sample_submission.csv`| valid null: the training prevalence for every encounter |
|`validate.py`| format checker —`python validate.py submission.csv`|
## What to submit
`./submission.csv`with exactly:`encounter_id, PredictedProbability`
(probability of readmission within 30 days, in [0,1]), one row per test
encounter.
## Scoring (hidden labels, from your file alone)
- **`auroc`** — primary, higher better
15

Auto-MD-bench
Autoresearch Protocol.In the main experiments, all Autoresearch runs receive the following instructions
(Karpathy, 2026):
# Research program: greedy iterative improvement
Your objective is the task in`description.md`: maximize its primary metric
on the hidden test via`./submission.csv`.
## Phase 0 -- working baseline first
Write your own experiment script that goes end-to-end as simply as possible:
load the provided data, hold out an internal validation split from the
training data, fit a deliberately simple model, print your validation
score(s), and write a format-valid`./submission.csv`. Confirm
`python validate.py submission.csv`passes before any improvement work -- a
valid submission on disk is your safety net.
## Loop (repeat until the time budget is spent)
1. Propose ONE focused change (features, preprocessing, model class,
hyperparameters -- one idea at a time).
2. Run the script; read the validation score.
3. Append one line to`journal.md`: what you changed, the numbers, and
KEEP or REVERT.
4. KEEP the change only if the validation primary metric beat the best so
far; otherwise revert it exactly.
## Hard rules
- Your experiment script(s) and`journal.md`are yours to edit; do not modify
the provided data files,`validate.py`, or this file.
- Tune only against your internal validation split, never against the test
features.
- Keep individual runs short enough to iterate many times; a long training
needs a clear reason in`journal.md`.
- The final`./submission.csv`must come from your best-validated version
(re-run it if you experimented after your best result).
- Everything happens inside this directory; no network access.
D SIMPLE BASELINE MODELS
Training and Aggregation.The simple baseline models use the same training data and evaluation code as
the agents’ models. We train each model with random seeds 0–4 and average the five separately computed scores
and calibration errors. Model settings are fixed across tasks within each family.
Survival Analysis.We use thepycoxCox proportional-hazards model with two hidden layers of 32 units,
batch normalization, dropout 0.1 and no output bias. Training uses Adam with learning rate10−3, batch size
256 and 64 epochs on the full training set, without early stopping. For SUPPORT, we standardize columnsx0
andx7–x13using training-set statistics and retainx1–x6as supplied. For the other survival tasks, we one-hot
encode nonnumeric columns using the training categories, impute missing values with training medians, and
standardize features. We estimate the baseline hazard from the training data and evaluate survival curves on
the supplied time grid as right-continuous step functions.
Classification.We useHistGradientBoostingClassifierwith 300 boosting iterations, learning rate 0.1 and
early stopping disabled. For UCI Diabetes, MIMIC-IV and both eICU tasks, the model uses the supplied numeric
features, excluding the outcome, record identifiers and the UCI patient grouping identifier. The estimator handles
missing values. For PhysioNet 2012, we summarize each measured variable by its mean, minimum, maximum
and last value over the observation window and use these summaries as predictors.
Sequential Prediction.We sort records by patient and ICU hour and forward-fill measurements within each
patient. Features include the current-hour measurements, ICU hour and a hospital indicator; columns with
no observed training values are excluded. We useHistGradientBoostingClassifierwith the classification
settings above and a maximum of 31 leaves per tree. We reserve 15% of training patients, stratified by whether
16

Zhou et al.
sepsis occurs, to select the alarm threshold. Among 40 quantiles from 0.80 to 0.999 of the holdout probabilities,
we choose the threshold with the highest utility. The model trained on the remaining patients produces the test
predictions. We repeat this procedure for each task, including the 500 labeled target-hospital patients where
provided.
E PER-TASK RESULTS AND INV ALID RUNS
Submission Validity.A run is valid if its selected submission has exactly the required columns and test-set
identifiers, with no duplicate identifiers. Probabilities must be finite and in[0,1], binary predictions must be in
{0,1}, and survival curves must be non-increasing, as applicable. Missing, unreadable or malformed files make
a run invalid. Masking-test results do not change validity or scores.
Score Aggregation.Penalized scores assign zero to invalid runs. For each agent and repetition, we average
normalized scores equally across tasks, then report the mean and sample SD of the three averages. Non-penalized
scores first average valid runs within each task, then weight tasks equally. Their SD is reported only when all
runs are valid. Negative sequential-prediction utility scores are clipped to zero in the reported primary-score
tables. Under each convention, we rank agents within each task by their mean normalized score. Rank 1 is best,
ties receive their average rank, and the simple baseline model is not ranked. Table 2 reports the mean and SD
of these ranks across tasks.
For each external-validation comparison, we divide the normalized score on the external-validation task by the
score on the corresponding task without the population shift for the same agent and repetition index. We average
ratios over pairs with two valid runs and a positive score on the corresponding task without the population shift.
Simple baseline ratios use the mean scores over five repetitions.
Table 12: Primary scores by task for valid runs (mean±SD).†Two valid runs;‡one valid run.
Task
Simple
baseline
models AIDE Codex Autoresearch AI Scientist v2
SUPPORT 0.6220.639±0.010 0.651±0.000 0.656±0.005 0.630±0.013
METABRIC 0.6420.658±0.004 0.659±0.008 0.676±0.007 0.647±0.018 †
Rotterdam 0.6850.677±0.022 0.694±0.002 0.692±0.004 0.694±0.002
Rotterdam→GBSG 0.6860.653±0.028 0.693±0.007 0.686±0.021 0.666±0.023
SEER 0.8650.749±0.216 0.862±0.019 0.870±0.003 0.861±0.011 †
SEER, later period 0.8620.865±0.014 0.872±0.002 0.868±0.011 0.835 ‡
NHANES 0.8350.858±0.003 0.863±0.007 0.860±0.001 0.852±0.004 †
UCI Diabetes 0.6680.659±0.042 0.682±0.011 0.688±0.002 0.677±0.009 †
PhysioNet 2012 0.4970.512±0.034 0.532±0.022 0.538±0.005 0.524±0.010
MIMIC-IV 0.8840.893±0.000 0.893±0.001 0.892±0.000 0.889±0.003
eICU 0.8710.877±0.001 0.877±0.001 0.874±0.007 0.871±0.008 †
eICU, new hospitals 0.8680.874±0.001 0.875±0.000 0.875±0.000 0.852±0.033
Sepsis 0.3810.415±0.036 0.446±0.017 0.440±0.009 0.181±0.256 †
Sepsis, new hospital 0.1990.168±0.146 0.231±0.021 0.268±0.020 0.228 ‡
Sepsis, 500 local labels 0.2480.217±0.102 0.299±0.031 0.253±0.056 0.124 ‡
Invalid Submissions.AI Scientist v2 produced all 12 invalid submissions: five had malformed survival
columns, five had incorrect patient-hour rows, one had incorrect patient identifiers, and one had incorrect en-
counter identifiers.
F CALIBRATION AND SUBGROUP PERFORMANCE
Expected Calibration Error.We compute ECE from the selected predictions in each valid run. For classi-
fication and sequential prediction, we partition probabilities into ten equal-width bins and compute
ECE =
X
b
nb
N |¯pb −¯yb|,
17

Auto-MD-bench
wheren b is the number of observations in binb,Nis the total number of observations, and¯p b and¯yb are
the bin’s mean predicted probability and event frequency. Empty bins contribute zero. For sequential predic-
tion, observations are patient-hours. We evaluate averaged ranks submitted as probabilities without applying
recalibration.
For survival analysis, we use the grid points nearest the 25th, 50th and 75th percentiles of test event times. At
each time, we sort patients by predicted survival into ten equal-size groups and compare mean predicted survival
with the within-group Kaplan–Meier estimate. We weight absolute differences by group size and average the
resulting errors over the three times. Groups with fewer than five patients are skipped.
For Table 3, we first average valid runs within each task, then weight tasks equally within each class or across
all tasks. All simple baseline calibration errors are averaged over the same five repetitions per task as the simple
baseline scores.
Subgroups.Classification subgroup scores use AUROC, including for PhysioNet 2012. We divide age into
test-set thirds and retain the four largest race/ethnicity categories, grouping the remainder asOther. Subgroup
metrics require at least 50 observations for AUROC and 80 for survival concordance. Survival subgroup scores
use Antolini concordance without the adjustment used for the primary score. Table 14 reports the mean gap
between each valid run’s highest and lowest subgroup scores. Subgroup scores for the simple baseline models
are averaged over five repetitions. SUPPORT and METABRIC use generic covariate names and are excluded;
sequential-prediction tasks are also excluded.
Table 13: ECE by task for valid runs (mean±SD).†Two valid runs;‡one valid run.
Task
Simple
baseline
models AIDE Codex Autoresearch AI Scientist v2
SUPPORT 0.0320.049±0.027 0.035±0.008 0.044±0.013 0.057±0.036
METABRIC 0.0540.048±0.003 0.132±0.152 0.081±0.033 0.053±0.001 †
Rotterdam 0.0420.059±0.045 0.042±0.011 0.055±0.027 0.082±0.050
Rotterdam→GBSG 0.0390.112±0.096 0.040±0.001 0.160±0.170 0.103±0.111
SEER 0.0060.027±0.040 0.015±0.010 0.016±0.011 0.008±0.005 †
SEER, later period 0.0070.008±0.005 0.253±0.210 0.005±0.001 0.013 ‡
NHANES 0.0110.011±0.003 0.016±0.010 0.064±0.019 0.022±0.000 †
UCI Diabetes 0.0080.440±0.090 0.133±0.221 0.005±0.001 0.079±0.106 †
PhysioNet 2012 0.0960.153±0.180 0.015±0.012 0.009±0.001 0.051±0.030
MIMIC-IV 0.0200.270±0.214 0.137±0.222 0.137±0.222 0.146±0.215
eICU 0.0130.269±0.224 0.140±0.224 0.271±0.222 0.015±0.003 †
eICU, new hospitals 0.0160.271±0.222 0.141±0.223 0.013±0.002 0.219±0.192
Sepsis 0.0140.003±0.002 0.004±0.005 0.166±0.284 0.215±0.075 †
Sepsis, new hospital 0.0210.025±0.036 0.023±0.028 0.096±0.097 0.002 ‡
Sepsis, 500 local labels 0.0200.171±0.142 0.167±0.276 0.009±0.004 0.016 ‡
18

Zhou et al.
Table 14: Subgroup performance gaps across valid runs. “Same lowest group” is the share matching the simple
baseline models’ lowest-scoring subgroup.
Task Grouping
Simple baseline models’
lowest group Same lowest group Agent gap
Simple
baseline
models’ gap
Rotterdam Age Oldest 92% 0.074 0.089
Rotterdam→GBSG Age Oldest 25% 0.019 0.033
SEER Age Youngest 73% 0.023 0.024
SEER Race/ethnicity American Indian/Alaska Native 73% 0.036 0.049
SEER, later period Age Youngest 80% 0.027 0.026
SEER, later period Race/ethnicity American Indian/Alaska Native 70% 0.035 0.048
NHANES Age Youngest 91% 0.158 0.222
NHANES Sex Male 100% 0.035 0.032
NHANES Race/ethnicity Other 100% 0.041 0.056
UCI Diabetes Age Oldest 100% 0.080 0.080
UCI Diabetes Sex Male 73% 0.006 0.008
UCI Diabetes Race/ethnicity Caucasian 9% 0.100 0.080
PhysioNet 2012 Age Oldest 100% 0.066 0.074
PhysioNet 2012 Sex Female 100% 0.012 0.021
MIMIC-IV Age Oldest 100% 0.084 0.078
MIMIC-IV Sex Female 100% 0.008 0.005
eICU Age Oldest 100% 0.065 0.065
eICU Sex Female 100% 0.009 0.006
eICU, new hospitals Age Oldest 100% 0.069 0.066
eICU, new hospitals Sex Female 100% 0.010 0.008
F.1 Effect of Evaluation Objectives
Setup.We compare modeling choices and predictions under three evaluation objectives on UCI Diabetes, the
binary 30-day readmission task. Each group contains three repetitions of AIDE, Codex, Autoresearch and AI
Scientist v2, all using Qwen3.8 Flash with a 12-hour budget. Group A reuses the main experiment’s AUROC
runs; groups B and C are new runs with the same data, submission format and task rules. The task descriptions
specify:
•A: maximize AUROC.
•B: minimize Brier score.
•C: maximize AUROC and minimize ECE, using ten equal-width bins.
Group C provides no weights or rule for combining the two objectives. For Autoresearch, we also change the
protocol’s instruction to “maximize its primary metric” to “minimize its primary metric” in B and “optimize its
primary metrics” in C.
Evaluation.We evaluate the submitted probabilities using the same AUROC, Brier score and ECE procedures
as in the main experiment. The Brier score is
Brier = 1 N
NX
i=1
(pi −y i)2,
wherep i is the predicted readmission probability andyi the binary outcome. ECE uses the ten equal-width
bins defined above. Each group has 11 valid runs out of 12: one AI Scientist v2 run in each group submitted
20,000 predictions for the 20,419 test admissions. We pool all valid runs across the four agents and report means
and sample standard deviations. Table 15 reports results by agent, and Figure 4 shows the AUROC and ECE
distributions.
Calibration and Discrimination.With AUROC and ECE as objectives, mean ECE falls from0.172±0.211
in A to0.016±0.023in C, while mean AUROC is0.683±0.016, compared with0.676±0.023in A. The Brier
19

Auto-MD-bench
Table 15: Results by agent and evaluation objective on UCI Diabetes (mean±SD over valid runs).
Agent Objective Valid AUROC Brier score ECE
AIDE AUROC 3/3 0.659±0.042 0.335±0.068 0.440±0.090
AIDE Brier score 3/3 0.606±0.142 0.099±0.010 0.037±0.054
AIDE AUROC and ECE 3/3 0.685±0.005 0.095±0.002 0.022±0.027
Codex AUROC 3/3 0.682±0.011 0.161±0.117 0.133±0.221
Codex Brier score 3/3 0.688±0.001 0.093±0.000 0.005±0.002
Codex AUROC and ECE 3/3 0.690±0.002 0.093±0.000 0.005±0.001
Autoresearch AUROC 3/3 0.688±0.002 0.093±0.000 0.005±0.001
Autoresearch Brier score 3/3 0.688±0.000 0.093±0.000 0.004±0.001
Autoresearch AUROC and ECE 3/3 0.689±0.002 0.093±0.000 0.004±0.001
AI Scientist v2 AUROC 2/3 0.677±0.009 0.113±0.026 0.079±0.106
AI Scientist v2 Brier score 2/3 0.545±0.199 0.274±0.255 0.265±0.368
AI Scientist v2 AUROC and ECE 2/3 0.658±0.034 0.099±0.007 0.039±0.046
0.0 0.2 0.4 0.6
ECE ↓
AUROC
and ECE
Brier score
AUROC
baseline
0.4 0.5 0.6 0.7
AUROC ↑
baseline
Averaged ranks as probabilities
Imbalance handling, no recalibration
Other
Figure 4: AUROC and ECE under three evaluation objectives on UCI Diabetes. Points are valid runs; bars
show means and dashed lines the simple baseline model. Colors mark the two modeling practices associated with
large calibration error.
20

Zhou et al.
group has mean ECE0.061±0.157and AUROC0.640±0.107. Across nine of its 11 valid runs, mean ECE is
0.005±0.001and mean AUROC is0.688±0.001; the simple baseline model has ECE 0.008 and AUROC 0.668.
The other two runs contain modeling failures. AIDE uses patient-level features derived from identifiers available
only in training and substitutes their means at test time, despite applying temperature scaling (AUROC 0.442,
ECE 0.099). AI Scientist v2 uses SMOTE without recalibration (AUROC 0.404, ECE 0.525).
Two runs in C also retain appreciable calibration error after isotonic calibration. AIDE maps its test predictions
to the distribution of out-of-fold predictions, then fits and evaluates isotonic regression on those same out-of-fold
predictions (test ECE 0.052). AI Scientist v2 includes the outcome label in an aggregate feature used for training
and validation, then fits isotonic regression on predictions affected by this target leakage (ECE 0.071).
Changes in Modeling Practice.We use Claude Opus 5.5 to annotate the code and execution records for all
22 valid runs in B and C without providing test scores, using the main experiment’s definitions of averaged ranks
as probabilities, class-imbalance handling and probability calibration. Seven runs are annotated again using the
same model; the repeated annotations agree on all recorded categories. Group A uses the main experiment’s
annotations.
Table 16 reports the resulting counts. Agents use averaged ranks as probabilities in 3/11 runs in A and none in
B or C. Class weighting or oversampling without subsequent recalibration occurs in 3/11, 1/11 and 0/11 runs,
respectively. Explicit calibration steps appear in 1/11 runs in A, 6/11 in B and 10/11 in C. A seventh run in
B uses logistic stacking, which the agent selects as an ensemble rather than as a calibration step; it is excluded
from the explicit-calibration count.
Table 16: Modeling practices under the three UCI Diabetes objectives. Each objective has 11 valid runs;
categories can overlap.
Practice AUROC (A) Brier score (B) AUROC and ECE (C)
Averaged ranks as probabilities 3 0 0
Class-imbalance handling without recalibration 3 1 0
Explicit probability calibration 1 6 10
G CENSORING AND REAL-TIME RULE VIOLATIONS
Table 17: Censoring errors in valid survival submissions; parentheses show the affected ensemble weight.
Agent Task Repetition Problem
Codex SUPPORT 2 The labels of the XGBoost Cox member are all positive, so
censored patients are treated as events (about 20%)
Codex SUPPORT 3 The labels of the XGBoost Cox member are all positive
(about 20%)
Codex SEER, later period 1 The XGBoost Cox member adds 100,000 to censoring times,
so censored patients stay in the risk set throughout (about
37% on average, about half after 36 months)
Autoresearch SEER 1 The labels of the XGBoost Cox member are not negated for
censored patients (about 1.5%)
Autoresearch SEER 3 The binary members for 24, 48 and 60 months label patients
censored before the time point as survivors (about 27%)
Autoresearch NHANES 1 The per-time-point IPCW classifiers take weights from a
KM estimate that ignores the survey cycle, while censoring
is determined entirely by the cycle; predicted survival in
some cycles collapses to 0.1–0.3 (about 71%)
Autoresearch NHANES 3 As above; the per-time-point members carry more than half
of the weight at later time points
Autoresearch SEER, later period 1 IPCW weights only the cases and not the controls who
survive past the time point, so death probabilities at later
time points are systematically overestimated (about 60%)
21

Auto-MD-bench
Masking Procedure.To detect violations of the real-time rule, we remove later records from each test
patient’s time series. For a patient withnhourly records, we drawu∼Uniform(0.40,0.90)and retain the
firstmin(n,max(4,⌊un⌋))records in time order. One masked test file is reused across runs of the same task.
Training data and all other task files, including the sample prediction file, remain unchanged. We rerun the code
producing the selected submission and compare alarms at retained hours with those from the complete records.
We compute the fraction of changed alarms over all retained rows and over the last retained row of each patient.
A fraction above 0.1% on either measure flags a violation; zero on both is reported asno change. For the detected
violations, rerunning the code on the unmodified input changed no alarms.
Among the 13 valid AIDE and AI Scientist v2 runs tested, three AIDE runs violate the rule: one onSepsis, new
hospitaland two onSepsis, 500 local labels. One AI Scientist v2 rerun on the full input did not reproduce the
selected predictions; its masked and full reruns nevertheless agreed on all retained alarms.
H MODEL DEVELOPMENT
We archive prediction files during model development and evaluate each version on the test set after the run
ends. A submission version is valid if its prediction file passes the submission-format checks.
Development Trajectories and Selection.Figure 5 shows test performance over development time, and
Table 18 summarizes development pace and submission selection.
Table 18: Development and submission-selection summary.
AIDE Codex Autoresearch AI Scientist v2
Versions per run 25.3 6.4 7.8 41.0
Time to first valid version (min) 30 64 17 30
Run time (min) 720 295 429 720
Ended before 12 h 0% 98% 100% 0%
Selected submission has highest test score 22% 32% 36% 21%
Reported validation−test score † +0.047 +0.006 +0.008 +0.012
†AUROC andC td tasks only.
Version-Pair Analysis.Figure 3 compares valid submission versions from valid runs. For AIDE and AI
Scientist v2, we pair a version with the latest earlier valid version from the nearest ancestor node that saved one.
For AI Scientist v2, some file-to-node and parent links are inferred. For Codex and Autoresearch, pairs contain
consecutive valid versions in time; the earlier version need not be the basis for the later one.
Within each run, we order pairs chronologically. If there are more than three, we divide them into three
0 3 6 9 12
Hours
0.0
0.2
0.4
Normalized score
(a) All 15 tasks
0 3 6 9 12
Hours
0.0
0.2
0.4
(b) Survival analysis
7 tasks
0 3 6 9 12
Hours
0.0
0.2
0.4
0.6
(c) Classification
5 tasks
0 3 6 9 12
Hours
0.0
0.1
0.2
0.3
(d) Sequential prediction
3 tasks
AIDE Codex AI Scientist v2 BaselineAutoresearch
Figure 5: Test performance over development time, averaged across runs; curves are zero before the first valid
submission.
22

Zhou et al.
consecutive groups of approximately equal size and sample one pair at random from each group. With at most
three pairs, we retain all and assign them to early, middle and late in order. Group boundaries are based on pair
counts.
Annotations compare the paired code and supporting execution records. Figure 3 counts only changes recorded
as affecting the submitted predictions. Ensembling covers members, weights or averaging; hyperparameter tuning
covers settings within a model family; feature engineering covers constructing, removing or selecting predictors.
Imputation, encoding and scaling are classified separately as preprocessing. A pair can belong to multiple
categories but counts once in each. Each share is the fraction of sampled pairs with that change for the same
agent and group. Runs with fewer than three pairs contribute to fewer groups. Table 19 reports score changes
in pairs containing each change type.
Table 19: Score changes for sampled version pairs containing each revision type, pooled across agents. Mean
score change is later minus earlier normalized test score.
Share of pairs
Change Score increase Score decrease Mean score change
Ensembling 58% 41%+0.010
Hyperparameter tuning 50% 49%+0.004
Feature engineering 51% 46%+0.015
Model family 79% 18%+0.084
Bug fix 66% 32%+0.059
I MODELING METHODS AND CODE ANNOTATION
Code Annotation.We use Claude Opus 5.5 to annotate the code and execution records for the selected
submissions from all 180 runs. Method frequencies and modeling-practice statistics use the 168 valid runs. For
AIDE and AI Scientist v2, the inputs include the selected node’s script and execution output. For Codex and
Autoresearch, they include the scripts and commands that produced the selected prediction file. Each annotation
gives a categorical response and cites supporting evidence by file and line number.
The codebooks cover model families, features, missing-data handling, validation, tuning, ensembling and output
processing, together with modeling practices such as handling censoring and class imbalance. We record practices
used to produce the submitted predictions separately from exploratory checks, such as evaluating demographic
subgroups. The practice codebook permits uncertain and not-applicable responses. Changes during model
development are annotated from sampled version pairs (Appendix H).
Repeated annotation by the same model assesses consistency. It covers 10 runs for modeling methods and 36 for
modeling practices (Table 21). The repeated practice annotations use the same codebook, with instructions not
to consult the first annotations. Agreement was 124 of 130 method fields and 273 of 288 modeling-practice fields.
The modeling-practice comparison excludes free-text fields and treats equivalent response labels as matches.
Modeling-practice disagreements that changed reported categories were checked against the cited code and
execution records. Final summaries include the recorded corrections. Table 21 also compares these annotations
with earlier code annotations for missingness features and an earlier review of validation designs.
Modeling Practices.Table 20 reports each practice as a percentage of eligible valid runs. Averaged ranks
as probabilities and performance checks by age or sex use all valid runs. Class-imbalance handling includes
class weighting or resampling and is evaluated on classification and sequential-prediction tasks. Missingness
features include missing-value indicators and counts; we assess them on EHR tasks and NHANES. Validation
under population shift means choosing a model or threshold using labeled target-hospital patients, or source data
modified to resemble the target population or split by hospital or ICU unit. This analysis covers Rotterdam→
GBSG and the two sepsis external-validation tasks.
Calibration Differences by Modeling Practice.Figure 2(a) groups valid runs into those that submit
averaged ranks as probabilities, those that handle class imbalance without recalibration and do not submit
23

Auto-MD-bench
averaged ranks, and all remaining runs (“Other experiments”). Figure 2(b) compares classification and sequential-
prediction runs that handle class imbalance and do not submit averaged ranks, with or without subsequent
recalibration. Recalibration includes isotonic regression, Platt scaling or prevalence correction after handling
class imbalance; it is annotated separately fromProbability calibrationin Table 6.
For a valid runron taskt(r), defined r = ECE r −ECE ref t(r), where the simple baseline ECE is the mean over
the five simple baseline repetitions. LetVcontain all valid runs andG⊆Va practice group. The group’s
share of runs is|G|/|V|, and its share of the total ECE difference isP r∈G dr/ P r∈V dr. Negative differences are
retained. Practice-group means and shares pool runs across agents and tasks; Table 3 first averages within each
task. Table 6 in the main text reports the frequencies of model families and validation methods.
Table 20: Modeling practices by agent (percentage of eligible valid runs).
Practice AIDE Codex Autoresearch AI Scientist v2
Averaged ranks as probabilities 20% 18% 9% 6%
Class-imbalance handling, no recalibration 21% 4% 13% 35%
Performance checked by age or sex 0% 4% 9% 0%
Validation under population shift 33% 89% 89% 40%
Missingness features 81% 89% 89% 58%
Table 21: Agreement in repeated annotations and comparisons with earlier code reviews.
Comparison Agreement
Modeling methods, repeated annotation 95% (130 fields, 10 runs)
Modeling practices, repeated annotation 95% (288 fields, 36 runs)
Missingness features vs. earlier records 91% (100 runs)
Validation under population shift vs. earlier checks 95% (22 runs)
J OTHER LLMS
We also evaluate Codex with gpt-6-luna and Gemini 3.8 Flash, using three repetitions on each of the 15 tasks (45
runs per LLM). The Qwen3.8 Flash results come from the main Codex evaluation. Table 22 reports normalized
scores, ECE, submission validity and token usage, using the scoring and ECE procedures in Appendices E and F.
Table 22: Codex with three LLMs across 15 tasks. Values are mean±SD over three repetitions; ECE is averaged
across tasks and token counts are millions per run.
LLM Normalized score↑ECE↓Valid runs Input tokens Output tokens
Qwen3.8 Flash 0.517±0.003 0.086 100.0%±0.0% 26.88±1.86 0.17±0.01
gpt-6-luna 0.517±0.004 0.041 100.0%±0.0% 2.77±0.12 0.04±0.00
Gemini 3.8 Flash 0.520±0.006 0.029 100.0%±0.0% 7.29±0.24 0.05±0.00
24
