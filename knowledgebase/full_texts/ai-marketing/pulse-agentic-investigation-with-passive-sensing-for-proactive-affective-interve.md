---
title: 'PULSE: Agentic Investigation with Passive Sensing for Proactive Affective Intervention in Cancer
  Survivorship'
url: https://arxiv.org/abs/2605.17679
category: ai-marketing
subcategory: empirical
date: 2026-05
venue: ''
authors:
- Zhiyuan Wang
- Subigya Nepal
- Ariful Islam
- Indrajeet Ghosh
- Xinyu Chen
source: arxiv
pdf_url: https://arxiv.org/pdf/2605.17679
pages: 30
chars: 118649
fetched_at: '2026-11-08T13:36:08+00:00'
kb_version: 1
---

# PULSE: Agentic Investigation with Passive Sensing for Proactive Affective Intervention in Cancer Survivorship

PULSE: Agentic Investigation with Passive Sensing for Proactive
Affective Intervention in Cancer Survivorship
ZHIYUAN WANG,Department of Systems and Information Engineering, University of Virginia, United States
SUBIGYA NEPAL,Department of Computer Science, University of Virginia, United States
ARIFUL ISLAM,Department of Systems and Information Engineering, University of Virginia, United States
INDRAJEET GHOSH,Dept. of Systems and Information Engineering, University of Virginia, United States
XINYU CHEN,Department of Systems and Information Engineering, University of Virginia, United States
KATHARINE E. DANIEL,Center for Behavioral Health and Technology, University of Virginia, United States
LAURA E. BARNES,Dept. of Systems and Information Engineering, University of Virginia, United States
PHILIP CHOW,Center for Behavioral Health and Technology, University of Virginia, United States
Diary alone: ambiguous
D I A RY E N T RY
"Had my follow-up call.
Just sitting around since."
Three possible readings:
Relieved after good news
Devastated by bad results
Just tired, routine check-up
+
Passive sensing reveals
Key behavioral signals:
Home all day (z = +2.8 vs. norm)
96.5% stationary, 256 steps today
3.4h screen, frequent unlocks
Agent disambiguates
get_behavioral_timeline
compare_to_baseline
find_peer_cases
find_similar_days
5 tool calls, ~45 sec
Binary state prediction
Predicted Actual
Positive affectTypical Typical
Negative affectElevated Elevated
Regulation desireElevated Elevated
Intervention avail.Yes Yes
Should we intervene? Yes!
Proactive Affective Agent: vague diary + agentic passive sensing investigation → precise, actionable intervention prediction
Fig. 1. Conceptual illustration of thePulseinterface. A brief diary can admit several interpretations (left); smartphone
sensing supplies additional behavioral measurements (center); and an LLM queries purpose-built tools before returning
study-target predictions (right). The figure does not represent a validated intervention decision rule.
Authors’ Contact Information: Zhiyuan Wang, vmf9pr@virginia.edu, Department of Systems and Information Engineering, University of
Virginia, Charlottesville, Virginia, United States; Subigya Nepal, sknepal@virginia.edu, Department of Computer Science, University of
Virginia, Charlottesville, Virginia, United States; Ariful Islam, xef4hb@virginia.edu, Department of Systems and Information Engineering,
University of Virginia, Charlottesville, Virginia, United States; Indrajeet Ghosh, vkw4ze@virginia.edu, Dept. of Systems and Information
Engineering, University of Virginia, Charlottesville, Virginia, United States; Xinyu Chen, dfs3mc@virginia.edu, Department of Systems and
Information Engineering, University of Virginia, Charlottesville, Virginia, United States; Katharine E. Daniel, ked4fd@virginia.edu, Center for
Behavioral Health and Technology, University of Virginia, Charlottesville, Virginia, United States; Laura E. Barnes, lb3dp@virginia.edu, Dept.
of Systems and Information Engineering, University of Virginia, Charlottesville, Virginia, United States; Philip Chow, pic2u@virginia.edu,
Center for Behavioral Health and Technology, University of Virginia, Charlottesville, Virginia, United States.
Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that
copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page.
Copyrights for components of this work owned by others than the author(s) must be honored. Abstracting with credit is permitted. To copy
Proc. ACM Interact. Mob. Wearable Ubiquitous Technol., Vol. 0, No. 0, Article 0. Publication date: September 2026.
arXiv:2605.17679v2  [cs.HC]  7 Aug 2026

0:2•Zhiyuan Wang, Subigya Nepal, Ariful Islam, Indrajeet Ghosh, Xinyu Chen, Katharine E. Daniel, Laura E. Barnes, and Philip Chow
Cancer survivors face elevated rates of depression, anxiety, and emotional distress, yet self-report may be unavailable at
some moments when support is relevant, a challenge we term thediary paradox. We presentPulse, a system foragentic
sensing investigation: LLM agents equipped with eight purpose-built tools query smartphone sensing data, compare current
behavior with personal baselines, and retrieve outcome-labeled historical cases. Rather than receiving only a fixed feature
summary, agents choose which modalities and time windows to inspect. We evaluate PULSE through a 2×2 design crossing
system architecture (structured single-pass vs. multi-turn agentic) with concurrent input modality (no current diary vs.
sensing plus current diary) on 50 cancer survivors. The agentic multimodal condition achieves balanced accuracy of 0.743 for
emotion-regulation desire; the agentic no-current-diary condition achieves 0.713 for self-reported intervention availability.
This is a system-level comparison because the architecture conditions also differ in tool-mediated information access. The
results provide a retrospective benchmark for interactive sensing investigation and motivate prospective evaluation at diary
non-response moments.
CCS Concepts:•Human-centered computing → Ubiquitous and mobile computing systems and tools;•Computing
methodologies→Natural language processing.
Additional Key Words and Phrases: Just-in-time adaptive interventions, passive sensing, large language models, affective
computing, cancer survivorship, agentic AI
ACM Reference Format:
Zhiyuan Wang, Subigya Nepal, Ariful Islam, Indrajeet Ghosh, Xinyu Chen, Katharine E. Daniel, Laura E. Barnes, and Philip
Chow. 2026. PULSE: Agentic Investigation with Passive Sensing for Proactive Affective Intervention in Cancer Survivorship.
Proc. ACM Interact. Mob. Wearable Ubiquitous Technol.0, 0, Article 0 (September 2026), 30 pages. https://doi.org/10.1145/
nnnnnnn.nnnnnnn
1 Introduction
More than 18 million cancer survivors live in the United States [ 65], and depression and anxiety are well-
documented concerns in this population. [40]. Clinical guidelines recommend routine screening and management
of these symptoms [5], yet timely and scalable mental-health support remains difficult to provide. Just-in-time
adaptive interventions (JITAIs) use mobile technology to adapt support across decision points to suit the needs
of users [43]. Systems that target mental health may need to estimate both whether a person wants to regulate
their current emotional state and whether they report being available to engage. In JITAI terminology, tailoring
variables, intervention options, decision points, and decision rules jointly specify when, whether, and how support
is offered [44].
Ecological momentary assessment (EMA) provides repeated self-report through brief mobile surveys [ 57].
It is valuable as research ground truth and as a potential model input, but mobile-health missingness can be
non-random; in some cohorts, affective states also predict subsequent prompt nonresponse [19, 42]. We call the
resulting design tension thediary paradox: when a support system that depends on a completed current diary has
no diary text to use at omitted prompts. CALLM [73], for example, uses diary text effectively when it is available.
This motivates evaluating how well a system performs when the current diary is withheld.
Passive smartphone sensing provides continuous, unobtrusive streams of behavioral data—movement patterns,
location traces, screen usage, sleep timing, and communication proxies—that can accumulate without a contem-
poraneous diary response. A decade of research, from StudentLife [69] and early digital phenotyping [49, 55]
otherwise, or republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee. Request permissions from
permissions@acm.org.
©2026 Copyright held by the owner/author(s). Publication rights licensed to ACM.
ACM 2474-9567/2026/9-ART0
https://doi.org/10.1145/nnnnnnn.nnnnnnn
Proc. ACM Interact. Mob. Wearable Ubiquitous Technol., Vol. 0, No. 0, Article 0. Publication date: September 2026.

PULSE: Agentic Investigation with Passive Sensing for Proactive Affective Intervention in Cancer Survivorship•0:3
to GLOBEM [79], has established associations between these signals and mental-health outcomes. Generaliza-
tion remains difficult: performance can approach chance in cross-dataset or population-level settings, although
within-population personalization can perform substantially better [1, 36, 79].
Why do sensing models often struggle outside the settings in which they were trained? Several factors are
plausible, including sensor missingness, distribution shift, label noise, and limited representation of person-
specific context. We study one of these factors: how behavioral evidence is assembled and interpreted for a
particular person and decision point. Fixed pipelines apply the same feature transform to every example, even
though an absolute value may mean very different things across people. A late-night screen session may be
routine for one person but anomalous for another; a day of low mobility may matter differently after an active
week than after a consistently sedentary one. An interactive system can request the evidence needed to make
those comparisons and relate observations to personal history. We refer to this capability ascontextual behavioral
signal interpretation[45].
Recent advances in large language models (LLMs) suggest a different path forward. LLMs can synthesize
behavioral evidence in natural language, and prior work has shown that they can reason about both mental
health text and wearable sensing summaries [25, 77, 80]. Most systems, however, still provide a pre-formatted
summary whose contents are fixed before inference. The model cannot decide what to inspect, which anomaly to
pursue, or how to compare today’s behavior against the right personal baseline.
In this paper, we pose two questions:(1) how accurately do LLM-based systems predict the study’s affect and
availability targets with and without the current diary, and (2) how does a multi-turn, tool-mediated system compare
with a structured single-pass system?
We introducePulse, which gives an LLM eight sensing-query tools implemented through the Model Context
Protocol [6]. Across multiple turns, the model selects modalities and lookback windows, requests personal-
baseline comparisons, and returns a prediction. The prompt constrains the task and available tools but does not
prescribe one fixed query sequence; the implementation follows a ReAct-style alternation between generated
analysis and tool actions [82]. We compare this interface with a structured single-pass baseline.
Figure 1 gives a high-level view of how these sensing queries add behavioral context to an ambiguous diary
entry.
We evaluatePulsethrough a 2×2 design crossing (1)system design—structured (fixed summary, single LLM
call) versus agentic (multi-turn tool use)—and (2)concurrent input—no current diary versus sensing plus the
current diary. This yields Struct-Sense, Auto-Sense, Struct-Multi, and Auto-Multi, evaluated retrospectively on
50 cancer survivors from the BUCS (Better Understanding Cancer Survivors) observational study and 4,112
completed EMA entries.
We define a candidateintervention opportunityas the conjunction of two complementary constructs.Emotion
regulation desiremeasures whether the user wants to regulate their current emotional state, whileintervention
availabilityrecords whether the user reports being available to engage with support. Modeling them separately
preserves the distinction between a desire to change one’s affect and the practical availability to do so.
Our contributions are:
(1) A tool-mediated sensing investigation design.We introduce LLM agents that query passive-sensing
data through eight purpose-built MCP tools and compare the design with a structured summary pipeline.
The architecture and tools can be extended to other passive-sensing domains.
(2) A 2×2 evaluation of architecture and concurrent input modality.We compare a structured single-pass
pipeline with the agentic system under matched current-input conditions. This is a system-level comparison
because the architectures differ in their interactive tool access and in the historical context available through
that interface.
Proc. ACM Interact. Mob. Wearable Ubiquitous Technol., Vol. 0, No. 0, Article 0. Publication date: September 2026.

0:4•Zhiyuan Wang, Subigya Nepal, Ariful Islam, Indrajeet Ghosh, Xinyu Chen, Katharine E. Daniel, Laura E. Barnes, and Philip Chow
(3) Retrospective affect and availability prediction in a clinical population.Pulseachieves 0.743
balanced accuracy on emotion-regulation desire when a current diary is available and 0.713 for self-reported
intervention availability without a current diary.
(4) A target-dependent current-diary association.In this retrospective benchmark, incorporating the
current diary substantially improves emotion-regulation desire prediction (0.651→0.743 BA) but has only a
marginal effect on intervention availability prediction (0.713→0.722 BA), motivating separate modeling of
motivational state and stated availability.
The manuscript is organized as follows. Section 2 reviews related work at the intersection of passive sensing,
LLMs for health, agentic AI, and JITAIs. Section 3 presents thePulsesystem design, including the factorial
framework, tool interfaces, and agent architectures. Section 4 describes the evaluation methodology, and Section 5
presents results. Section 6 discusses implications and limitations, Section 7 outlines future work, and Section 8
concludes.
2 Related Work
Pulsesits at the intersection of four research threads: passive mobile sensing for mental health, large language
models for health and affective computing, agentic AI with tool use, and JITAIs.
2.1 Passive Sensing for Mental Health
The foundational insight that smartphone sensor data correlates with mental-health outcomes dates to Stu-
dentLife [69], which demonstrated associations between passively sensed behavioral patterns and depression,
stress, and academic performance in college students. Saeb et al. [55] further reported correlations between GPS
features and depressive symptom severity, while Canzian and Musolesi [10] studied mobility traces for tracking
depressive states. Onnela and Rauch [49] formalized “digital phenotyping, ” and Torous et al. [59] connected it
to the Research Domain Criteria framework. Subsequent work has examined relapse and symptom change in
schizophrenia [68], depression dynamics [70], digital biomarkers of mood disorders [23], behavioral changes
during the COVID-19 pandemic [22, 48], and depression onset from longitudinal passive data [11]. Instrumen-
tation frameworks such as AWARE [18], long-running cohort studies [46], and recent reviews [9, 12] further
characterize this literature.
Alongside these advances, cross-context generalization remains a persistent challenge. GLOBEM [79] evaluated
18 algorithms across four longitudinal sensing datasets and found that many cross-dataset depression-detection
results were near chance. Meegahapola et al. [36] likewise reported weak population-level mood inference across
countries, while also showing that country-specific personalization can be much stronger. Adler et al. [1] found
that pooling longitudinal datasets sometimes helped but did not consistently solve transportability. These findings
motivate careful separation of cross-population, within-population, and personalized evaluation rather than
a single universal “accuracy ceiling. ” As Adler et al. [2] argued in “Beyond Detection, ” the field must connect
detected correlates to actionable clinical support. One open design question is how to represent person- and
episode-specific context. For example, 500 steps may have different meanings for users with very different
personal baselines, and interpretation may depend on time of day, phone usage, location, and longitudinal history.
Pulseexplores one possible interface for assembling such context: an LLM can request selected behavioral
summaries and personal-baseline comparisons through tools.
2.2 LLMs for Affective Computing and Health
The application of LLMs to health prediction builds on few-shot prompting [ 8] and instruction following in
aligned models [ 50]. Singhal et al. [ 58] evaluated clinical knowledge in LLMs, while Khasentino et al. [ 24]
studied personal-health data including sleep and fitness metrics. Health-LLM [25] evaluated 12 models on 10
Proc. ACM Interact. Mob. Wearable Ubiquitous Technol., Vol. 0, No. 0, Article 0. Publication date: September 2026.

PULSE: Agentic Investigation with Passive Sensing for Proactive Affective Intervention in Cancer Survivorship•0:5
wearable-sensing targets. Mental-LLM [80] reported competitive depression- and stress-detection performance
from online text. Zhang et al. [84] combined LLMs with structured smartphone-sensing summaries and reported
gains over traditional ML in some configurations. SensorLLM [33] aligned LLMs with motion-sensor data for
activity recognition, and a recent survey [17] reviews LLM applications for wearable health data. Zhang et al. [85]
also document limitations relevant to LLM-based affect prediction.
The most directly comparable published LLM baseline for the same population and targets is CALLM [73],
which combines diary text, TF–IDF cross-user retrieval, and longitudinal memory. CALLM requires a current
diary;Pulseadditionally evaluates a condition in which the current diary is withheld.
Several systems combine LLMs with sensing or personal-tracking data. MindScape [47] contextualizes journal
prompts; GLOSS [13] uses generated code for open-ended sensing analysis; LENS [78] aligns sensing data with
language models; and Vital Insight [32] supports expert sensemaking through visualization and human-in-the-
loop analysis. PHIA [37] generates and executes code to answer retrospective wearable-health questions, while
IoT-LLM [4] addresses general IoT data. Their tasks, populations, inputs, and evaluation protocols differ, so we
use them for design context rather than performance comparison.
2.3 Agentic AI and Tool Use
Agentic LLM systems combine multi-step generation with actions such as tool calls. Chain-of-thought prompting
is an influential technique for eliciting intermediate reasoning [75]; ReAct [82] interleaves reasoning traces and
actions. Toolformer [56] studied self-supervised tool use, Gorilla [52] studied API calling, and Voyager [66] used
an embodied agent with a growing skill library. Separately, retrieval-augmented generation [30] supplies external
examples or knowledge to generation, and a recent review summarizes its healthcare applications [3].Pulse
combines these design patterns through behavioral-data tools and outcome-labeled retrieval.
Wang et al. [67] survey LLM agents in terms of planning, memory, and tool use, and Huang et al. [21] focus
on planning. The Model Context Protocol [ 6] specifies an interface between models, tools, and data sources.
ContextAgent [81] studies proactive agents over wearable observations. ReflecTool [34] studies reflection and
tool verification on clinical tasks; its episode-level memory is conceptually related toPulse’s reflection document,
but the implementations and evaluations differ.
LLMs can be unreliable numerical reasoners when asked to manipulate tabular data directly.Pulsetherefore
assigns counting, aggregation, thresholding, and temporal retrieval to deterministic tool code, while the model
decides what to inspect and how to interpret the returned evidence.
2.3.1 Agentic and LLM-Based Approaches in Health Sensing.Table 1 comparesPulsewith several families of
behavioral-health systems rather than presenting a linear progression. Conventional sensing systems such
as GLOBEM [79] and Mishra et al. [39] use engineered features and supervised models. LLM-based systems—
including Health-LLM [25], Mental-LLM [80], Zhang et al. [84], Feng et al. [16], MindScape [47], and CALLM [73]—
use preformatted sensor or diary representations for different tasks and populations. GLOSS [13] and PHIA [37]
allow an LLM to generate and execute analysis code for open-ended sensemaking or retrospective question
answering.Pulseinstead exposes domain-specific sensing queries and outcome-labeled retrieval for retrospec-
tive prediction of study-defined affect and availability targets. PH-LLM [24], Time2Lang [53], AMIE [61], and
ReflecTool [34] provide adjacent context but are not direct performance baselines.
The systems also differ in what the model is allowed to do. GLOSS and PHIA give LLMs code-generation
capabilities for exploratory analysis or retrospective questions, whereas ContextAgent [81] reasons over wearable
observations and ReflecTool [34] studies reflection and tool verification for clinical tasks.Pulseuses a narrower
action space: its tools expose predefined sensing summaries, temporal queries, personal comparisons, and retrieval
operations. This restriction keeps aggregation and thresholding in deterministic code while allowing the model to
Proc. ACM Interact. Mob. Wearable Ubiquitous Technol., Vol. 0, No. 0, Article 0. Publication date: September 2026.

0:6•Zhiyuan Wang, Subigya Nepal, Ariful Islam, Indrajeet Ghosh, Xinyu Chen, Katharine E. Daniel, Laura E. Barnes, and Philip Chow
choose which evidence to request. It trades the flexibility of arbitrary code generation for a reproducible interface
tailored to repeated affect and availability prediction.
Table 1. Positioning ofPulserelative to prior systems for health sensing and LLM-based health prediction. “Domain Tools”
denotes whether the system provides purpose-built tools for autonomous investigation, as distinct from code generation or
fixed prompting.
System Year Data Source LLM Agentic Domain Tools Clinical Pop. Prediction
Mishra et al. [39] 2021 Sensing No No No No Receptivity
GLOBEM [79] 2022 Sensing No No No No Affect/Depression
Health-LLM [25] 2024 Wearable Yes No No Partial 10 Health Tasks
Mental-LLM [80] 2024 Text Yes No No Partial MH from Text
Zhang et al. [84] 2024 Sensing Yes No No No Affect
MindScape [47] 2024 Sensing+LLM Yes No No No Journaling
CALLM [73] 2026 Diary+RAG Yes No No Yes Affect+Receptivity
GLOSS [13] 2025 Sensing Yes Partial Code Gen. No Sensemaking
Feng et al. [16] 2026 Sensing Yes No No No MH Forecasting
PHIA [37] 2026 Wearable Yes Yes Code Gen. No Retrospective Q&A
Pulse2026 Sensing+Diary Yes Yes 8 MCP Tools Yes Affect+Desire/Availability
Table 1 is therefore a map of design choices rather than a performance ranking.Pulsediffers from the
closest systems along three axes: it uses a multi-turn query loop rather than a single preformatted prompt; it
exposes domain-specific sensing operations rather than unrestricted code execution; and it evaluates repeated
study-target predictions in a cancer-survivor cohort rather than retrospective question answering or general-
population sensemaking. These differences motivate the comparison but do not make scores across studies
directly comparable.
2.4 Just-in-Time Adaptive Interventions
The JITAI framework [43, 44] identifies six components: decision points, intervention options, tailoring variables,
decision rules, proximal outcomes, and distal outcomes. Tailoring variables are measurements used to adapt
delivery at decision points. A recent meta-analysis reported small average mental-health benefits alongside
substantial heterogeneity and risk-of-bias concerns [64].
Kunzler et al. [29] examined state-level receptivity to mHealth interventions using response and engagement
measures. Mishra et al. [39] studied in-the-wild receptivity detection with smartphone and wearable context,
including time, activity, and phone use. These operationalizations are related to, but not identical with, the
self-reported desire and availability labels used here. Klasnja et al. [ 26] developed the microrandomized trial
(MRT) methodology for evaluating JITAI components, later applied in HeartSteps [27]. IntelliCare [41] and MRT
use notification timing [7] to provide some intervention context.
Pulse’s emotion-regulation desire (ER_desire) and self-reported intervention availability (INT_availability)
targets can be treated as candidate tailoring variables. Gross’s emotion-regulation framework [20] motivates
the former broadly. The two study labels are related to, but distinct from, established receptivity constructs; we
therefore analyze them separately and treat their joint use as a study-specific operationalization.
Estimating a tailoring variable is only one part of JITAI design. A complete JITAI must also specify decision
points, intervention options, decision rules, and proximal outcomes, and then test how those components affect
behavior or well-being [ 26, 44].Pulsefocuses on the upstream state-estimation problem: how to assemble
behavioral evidence when the available inputs vary across decision points. Prediction performance alone does
not establish that acting on the estimate improves an intervention outcome.
Proc. ACM Interact. Mob. Wearable Ubiquitous Technol., Vol. 0, No. 0, Article 0. Publication date: September 2026.

PULSE: Agentic Investigation with Passive Sensing for Proactive Affective Intervention in Cancer Survivorship•0:7
SENSE
Passive smartphone + diary
Motion & Activity
GPS & Location
Screen & App Usage
Keyboard & Typing
Diary Text
THINK
LLM Agent (ReAct Loop)
REASONING LOOP
Thought
Action
Observation
Done?
No
MCP SENSING TOOLS (8)
daily_summary cmp_baseline
beh_timeline receptivity_hist
query_sensing similar_days
query_raw_evts ﬁnd_peer_cases
CROSS-USER RAG
Diary RAG Sensing RAG
Yes
INFERENCE
Positive / Negative Affect
PREDICTED AFFECT
Emotion Regulation
PREDICTED DESIRE
Intervention Opportunity
PREDICTED AVAILABILITY
reasoning conﬁdence (0-1)
REAL OUTCOME
Receptivity = GT Desire ↑  ∧  Avail = Yes
only observable signal for agent reﬂection
AGENT REFLECTION
what worked, what failed, when receptive
USER MEMORY
user understanding receptivity history
successful JITAI? agent reﬂections
Fig. 2. System architecture ofPulse. Passive smartphone sensing streams and optional diary text (Sense) feed an LLM agent
that conducts a multi-turn ReAct investigation using eight domain-specific MCP tools and cross-user retrieval-augmented
generation (Think). The agent produces predicted affect, desire, and availability along with reasoning and confidence scores
(Inference). The baselines and 2×2 design are described in Sections 3.2 and 4.2.
3 System Design
Figure 2 presents thePulsearchitecture:Senseassembles smartphone sensing and, in multimodal conditions, the
current diary;Thinkuses a ReAct-style loop with eight MCP tools and outcome-labeled retrieval; andInference
returns affect, desire, stated availability, a reasoning trace, and self-reported confidence.
3.1 Problem Formulation
Given the data assembled for a completed EMA entry 𝑡—which may include sensing history, the current diary, a
user profile, and memory—Pulsepredicts (1) three continuous targets: Positive Affect, Negative Affect [ 74], and
emotion-regulation desire; and (2) sixteen binary indicators, including individualized positive and negative affect
states, discrete emotions, interaction quality, physical pain, future outlook, emotion-regulation desire state, and
intervention availability.
We focus on four study-defined, clinically relevant targets that could be evaluated as candidate JITAI tailoring
variables [15, 43]. The two intervention-related targets areER_desire, which asks whether the user currently
wants to regulate their emotional state, andINT_availability, which asks whether the user reports being
available to engage with an intervention. The affect targets,PA_StateandNA_State, indicate whether positive
or negative affect is high relative to the user’s personal baseline.
For this study, we operationalize the conjunction of ER_desire and INT_availability as a candidate intervention
opportunity. This definition is a modeling choice, not a validated decision rule or a measure of actual intervention
engagement.
3.2 Factorial Design
To compare the agentic system across concurrent input modalities, we employ a 2 ×2 design crossing two
dimensions (Table 2):
Proc. ACM Interact. Mob. Wearable Ubiquitous Technol., Vol. 0, No. 0, Article 0. Publication date: September 2026.

0:8•Zhiyuan Wang, Subigya Nepal, Ariful Islam, Indrajeet Ghosh, Xinyu Chen, Katharine E. Daniel, Laura E. Barnes, and Philip Chow
Table 2. The 2×2 factorial design. Each cell represents a primary condition evaluated on the same 50 users. CALLM is
evaluated as a diary-only baseline outside the factorial design.
No Current Diary Sensing + Current Diary
StructuredStruct-Sense Struct-Multi
AgenticAuto-Sense Auto-Multi
Reasoning Architecture.Structured agents(Struct-Sense, Struct-Multi) receive all available data as a pre-
formatted summary and produce predictions in a single LLM call. Their fixed pipeline considers sleep, mobility,
social signals, and peer comparisons before producing the final prediction.Agentic agents(Auto-Sense, Auto-Multi)
instead receive a user profile, optional diary text, and access to eight MCP tools. They choose what to investigate
through a multi-turn tool-use loop, typically making 6–12 tool calls per prediction.
Data Modality.No-current-diaryconditions (labeled Struct-Sense and Auto-Sense for continuity) omit the diary
for the current prediction while still permitting temporally prior self-report outcomes through the historical
channels described below.Multimodalconditions (Struct-Multi, Auto-Multi) provide both passive sensing data
and the user’s diary entry for that time point.
Additional Condition.We include one additional condition: CALLM [ 73], which uses diary text with TF-IDF
cross-user retrieval and no sensing data, serving as a diary-dependent LLM baseline.
This design supports two primary comparisons. Within each concurrent-input condition, Auto-Multi vs.
Struct-Multi and Auto-Sense vs. Struct-Sense compare multi-turn tool-mediated investigation with a structured
single-pass pipeline. Because the interfaces expose different information, these contrasts compare the implemented
systems; they do not isolate reasoning style alone. Within each architecture, multimodal vs. no-current-diary
conditions estimate the association with supplying the current diary. CALLM provides an additional diary-only
reference outside the factorial design.
3.3 The BUCS Dataset
Pulseis evaluated on the BUCS dataset [15], a longitudinal study of 407 adult cancer survivors who completed
5 weeks of data collection. The dataset was obtained in collaboration with the original study team and used
with institutional review board approval. Participants completed three daily ecological momentary assessments
(EMA) [57], randomly delivered in the morning, afternoon, and evening. The surveys captured positive and
negative affect ratings, discrete emotions, emotion regulation desire, intervention availability, and brief diary
entries about emotional drivers.
Passive smartphone sensingcontinuously recorded accelerometer-based motion (stationary, walking, run-
ning, automotive activity), GPS location (distance traveled, time at home, location variance), screen usage (session
counts, durations, lock/unlock patterns), app usage (category-level durations; Android only), and accelerometer-
derived sleep periods. Keyboard activity (typing sessions and character counts) is sparsely available because
participants could choose whether to share this modality.User profilescontain baseline demographic information,
cancer type and treatment history, and validated psychological trait measures.
Platform differences between iOS and Android affect data availability: app-level usage is available only on
Android (approximately 36% of the test sample). The sensing tools are designed to gracefully handle missing
modalities, returning explicit “data not available” responses that the agent incorporates into its reasoning. The data
collection protocol was approved by the institutional review board (anonymized for review), and all participants
provided informed consent.
Proc. ACM Interact. Mob. Wearable Ubiquitous Technol., Vol. 0, No. 0, Article 0. Publication date: September 2026.

PULSE: Agentic Investigation with Passive Sensing for Proactive Affective Intervention in Cancer Survivorship•0:9
3.4 Structured Agents
The structured agents (Struct-Sense, Struct-Multi) implement a fixed pipeline in which all available data is
pre-assembled and the LLM produces a prediction in a single call. This design mirrors the predominant approach
in prior LLM-for-sensing work [25, 84].
Input Assembly.For each prediction, the system pre-computes a sensing summary covering all available
modalities for the current day up to the EMA timestamp (sleep metrics, mobility statistics, screen usage patterns,
activity breakdowns). This summary, along with the user’s trait profile, a longitudinal memory document, and
outcome-labeled peer examples, is assembled into a structured prompt.
Cross-User Outcome Retrieval.Both structured and agentic conditions receive outcome-labeled peer cases.
Structured agents use TF–IDF text retrieval in multimodal mode or cosine similarity over daily sensing fingerprints
in no-current-diary mode. The top 10 positive-similarity entries and their ground-truth EMA outcomes are
included in the prompt.
Prompting Strategy.Within a single LLM call, the prompt asks the model to consider the available behavioral
modalities (sleep, mobility and activity, and social signals), reference the peer outcome examples, and produce a
final prediction. The model’s natural-language reasoning is open-ended, but its input context and output schema
are fixed across predictions. The modality order is a fixed implementation choice and was not varied in this study.
3.5 Agentic Investigation Agents
The agentic conditions (Auto-Sense, Auto-Multi) use a multi-turn loop that alternates generated analysis with
tool actions, drawing on chain-of-thought prompting [75] and ReAct [82]. The model receives a task prompt, a
user profile, a pre-generated memory document, access to eight MCP tools, and the current diary only in the
multimodal condition. Tool selection is generated under the prompt’s standing instructions, including mandatory
peer retrieval. Appendix A documents the prompt structure.
3.5.1 MCP Tools.A core design choice is to keep aggregation, retrieval, and temporal filtering in deterministic tool
code while using the LLM for contextual interpretation. The tools support broad orientation (get_daily_summary,
get_behavioral_timeline), targeted follow-up (query_sensing, query_raw_events), within-person contex-
tualization (compare_to_baseline,find_similar_days), and cross-user retrieval (find_peer_cases).
The eight tools are implemented via the Model Context Protocol (MCP) [6]. Table 3 summarizes their signatures
and returned information. The tools use the following query windows and defaults: 0–7 prior days forget_daily_
summary, 1–48 hours before the EMA forquery_sensing, and 14 days forget_receptivity_history, matching
the two-week recall period standard in affect measurement [28]. compare_to_baseline returns a time-of-day-
specific mean, dispersion, z-score, and qualitative bands at|𝑧|=. 5, 1, 2; find_similar_days searches pre-EMA
same-user history and returns the top three days; and find_peer_cases defaults to ten positive-similarity cases
from other participants. These bounds are design defaults matched to each tool’s temporal granularity, in line
with window lengths common in longitudinal mobile-sensing and EMA studies [39, 55, 69]; they were fixed a
priori rather than tuned, and the agent chooses its actual lookback within them at query time. Retrieval depths
follow the same pool-scaled logic: find_peer_cases returns 10–20 outcome-labeled peer cases as few-shot
in-context examples [8, 30], a range validated in prior work on this population [73] that balances inference gains
against token cost, whilefind_similar_daysreturns three days from the far smaller within-user history.
Deterministic data-access code enforces the temporal boundary: sensing records, historical outcomes, memory,
retrieval results, and structured summaries are restricted to information available before the current EMA
timestamp. The current diary is supplied only in the multimodal conditions.
3.5.2 Investigation Loop.ThePulseagent operates through a multi-turn conversation with tool-use capabilities.
A typical investigation begins with the user profile and any available diary text, followed by a broad view
Proc. ACM Interact. Mob. Wearable Ubiquitous Technol., Vol. 0, No. 0, Article 0. Publication date: September 2026.

0:10•Zhiyuan Wang, Subigya Nepal, Ariful Islam, Indrajeet Ghosh, Xinyu Chen, Katharine E. Daniel, Laura E. Barnes, and Philip Chow
get_daily_summary(date,lookback_days=0..7)
Natural-language summary of a day’s behavioral patterns, with optional multi-day lookback.
get_behavioral_timeline(date,segment_hours=1..6)
Chronological reconstruction of the day before the EMA.
query_sensing(modality,hours_before_ema=1..48,hours_duration=1..24,granularity)
Aggregates for one modality (GPS, motion, screen, keyboard, music, light) in a chosen window.
query_raw_events(modality,hours_before_ema,hours_duration,max_events=30)
Raw event stream: app sessions, screen locks, activity transitions, typing sessions.
compare_to_baseline(modality,feature,hours_before_ema)
Current value, time-of-day-specific historical mean/SD, z-score, and qualitative bands at|𝑧|=.5,1,2.
get_receptivity_history(lookback_days=14)
Prior numeric regulation-desire scores and availability labels over the selected lookback.
find_similar_days(top_k=3)
Same-user past days by cosine similarity, with prior desire, availability, and diary snippets.
find_peer_cases(search_mode=text|sensing,top_k=10default; the prompt instructs 10–20)
Outcome-labeled cases fromotherparticipants (TF–IDF diary or sensing-fingerprint similarity); non-positive matches
are omitted.
Table 3. The eight MCP tools used by the agentic conditions: signatures, parameter ranges, and returned information.
from get_daily_summary and get_behavioral_timeline. The agent can then issue targeted sensing queries,
compare observations with the user’s baseline, or retrieve similar days and peer cases before producing the final
predictions, reasoning trace, and confidence estimate.
The prompt does not require this order. The agent may skip uninformative steps, revisit an earlier query after
new evidence, or select a different investigation path. The maximum number of tool-use turns is capped at 16 to
bound inference time, though most predictions complete in 6–12 turns (30–90 seconds).
3.5.3 Per-User Session Memory.As the agent processes sequential EMA entries for a user, it appends a brief
reflection to a session-memory document. The reflection receives the investigation summary, the prediction,
and a binary composite of elevated regulation desire and self-reported availability from the completed EMA.
Prior desire and availability also enter through history tools and outcome-labeled peer cases, so the ablation in
Section 5.8.4 removes only the reflection document.
3.6 Outcome-Labeled Cross-User RAG
Pulseuses cross-user retrieval-augmented generation [ 30] to return cases with similar behavioral patterns or
diary entries and their EMA outcomes. These cases provide outcome-labeled reference points for the model.
Retrieval uses TF–IDF similarity over diary text in multimodal conditions and cosine similarity over normalized
daily sensing vectors in no-current-diary conditions. In the agentic conditions, find_peer_cases exposes both
modes and the agent selects between them based on the available input.
The peer database is constructed from the 349-user training pool and excludes all 50 evaluation users.
Proc. ACM Interact. Mob. Wearable Ubiquitous Technol., Vol. 0, No. 0, Article 0. Publication date: September 2026.

PULSE: Agentic Investigation with Passive Sensing for Proactive Affective Intervention in Cancer Survivorship•0:11
4 Evaluation Methodology
4.1 Evaluation Setup
We evaluatePulseon a test sample of 50 users randomly selected from the 399 BUCS participants with sufficient
data (mean 82.2 entries per user, range 74–96). The remaining 349 participants form the training pool for trained
baselines and cross-user retrieval. We chose 50 users as a balance between inference cost and coverage. Each
agentic user consumes roughly seven million input tokens across∼80 multi-turn predictions, making full-cohort
evaluation of all 399 users across five systems prohibitively expensive. The main comparison includes the four
2×2 conditions plus CALLM, each on 4,112 EMA entries for the 50 users. The 50 participants were aged 30–77
(M = 53.5, SD = 10.9), predominantly female (90%) and White (94%), with breast cancer the most common diagnosis
(56%) across stages from in-situ to stage IV (Table 11, Appendix D).
4.1.1 Representativeness Analysis.We compared the 50 randomly selected evaluation users with the remaining
349 BUCS participants (Table 10, Appendix B.7). The NA_State base rate and mean NA differed with small
effect sizes (𝑟≤0.20); platform mix also differed. The factorial comparisons use the same 50 participants across
conditions.
4.2 Baselines
4.2.1 Reference Baselines.We report three families of reference baselines to contextualize the aggregate results.
First, we include traditional sensing baselines (Random Forest, XGBoost, and Logistic Regression) trained on
hourly sensing features across six modalities: motion (stationary, walking, running, automotive minutes), screen
(total minutes, session count), GPS (travel distance, time at home, location variance), keyboard (session count,
character count), app usage (total and per-category minutes), and light (ambient lux). For each EMA timestamp,
features are extracted from hourly windows preceding the prediction point, yielding a flat feature vector (e.g.,
h0_screen_on_min, h1_motion_walking_min, etc.). The lookback horizon (1, 2, 4, 6, 12, or 24 hours), number
of selected features, and model hyperparameters are optimized within the 349-user training set. Second, we
include text-only baselines: TF-IDF+Logistic Regression, Bag-of-Words+Logistic Regression, and MiniLM sentence
embeddings+Logistic Regression. Third, we include combined baselines (Random Forest and Logistic Regression)
over the concatenation of hourly sensing features and diary embeddings. All trained baselines are evaluated on
the same held-out 50-user set used for the LLM systems.
These baselines provide context but differ fromPulsein training population, feature representation, and data
access. The primary comparison therefore remains the factorial contrast between structured and agentic systems
evaluated on the same 50 participants under the same current-input conditions.
4.2.2 LLM Baseline.CALLM [ 73] serves as the most directly comparable published diary-based LLM baseline
for the same cancer-survivor population and targets. It uses diary text with TF–IDF cross-user retrieval and
longitudinal memory.
4.3 Metrics
Balanced Accuracy (BA) is the primary metric for binary targets, defined as the arithmetic mean of sensitivity
and specificity. BA is preferred over standard accuracy for health data with class imbalance, as it gives equal
weight to both classes regardless of base rates.
We report pooled, entry-level balanced accuracy across the 50 users, with 95% bootstrap intervals from 10,000
entry resamples. The reported 𝑝-values likewise come from entry-level resampling of the BA difference. Because
this resampling does not account for entries nested within users, we treat the tests as descriptive. Section 5.6
reports per-user dispersion for Auto-Multi.
Proc. ACM Interact. Mob. Wearable Ubiquitous Technol., Vol. 0, No. 0, Article 0. Publication date: September 2026.

0:12•Zhiyuan Wang, Subigya Nepal, Ariful Islam, Indrajeet Ghosh, Xinyu Chen, Katharine E. Daniel, Laura E. Barnes, and Philip Chow
4.4 Implementation
All LLM inference uses Claude Sonnet (Anthropic), a transformer-based [63] LLM, via the Claude CLI, with up
to 16 tool-use turns per prediction. The tools are served via an MCP server launched as a subprocess for each
prediction, ensuring per-user data isolation. Inference time ranges from 30 to 90 seconds per prediction depending
on the number of tool calls. Each of the five systems (four factorial plus CALLM) produces 4,112 predictions on
the 50-user sample. All experiments use Claude Sonnet 4.6 (claude-sonnet-4-6). All code, prompts, and tool
implementations will be released publicly upon publication.
5 Results
5.1 The 2×2 System Comparison
Within the 2×2 design, the agentic conditions score higher than their structured counterparts in both concurrent-
input conditions. These are differences between the evaluated conditions: the agentic arms add interactive tool
access, personal-baseline comparisons, and selected temporal detail to context shared with the structured arms.
Diary effects are target-dependent and are stated per target below (Sections 5.2–5.5). Table 4 presents results for
the four focus targets and their mean.
Table 4. 2×2 system comparison. Balanced accuracy for the four focus targets and their mean; Δ is the observed difference
between the agentic and structured conditions.
Modality Architecture PA_State NA_State ER_desire INT_availability Mean BA
No current diary
Struct-Sense .502 .510 .507 .542 .515
Auto-Sense .595 .591 .651 .713 .637
Δ+.093 +.082 +.145 +.170 +.122
Multimodal
Struct-Multi .530 .666 .655 .552 .601
Auto-Multi.720 .716 .743 .722 .725
Δ+.190 +.051 +.088 +.171 +.124
The analysis reports mean-BA differences of+0.124in the multimodal condition and +0.122in the no-current-
diary condition, with entry-level bootstrap 𝑝<. 0001for each target. The largest observed difference is on
PA_State in the multimodal condition (Δ=+ 0.190). Intervention availability differs by+0.171in the multimodal
condition and+0.170in the no-current-diary condition.
5.1.1 Matched-Call Sensitivity Analysis.Each agentic prediction uses multiple LLM calls (mean 6.2), compared
with one call for the structured pipeline. We therefore reran Struct-Multi 𝑘 times per entry and combined its
predictions by majority vote—self-consistency sampling [72], the standard method for converting additional
inference calls on a fixed prompt into accuracy—sweeping 𝑘 from 1 to 7, where 𝑘=7approximates the agentic
condition’s mean call count. The observed mean gap changes from+.131BA at 𝑘=1to+.126at 𝑘=7(Appendix B.1).
Repeated structured sampling does not close the gap in this test, although the control matches call count rather
than token use or the information available through tools.
5.2 Intervention Opportunity Detection
The central empirical question is whether the system can estimate both components of the study’s candidate
intervention opportunity: emotion-regulation desire and self-reported availability. Table 6 summarizes the four
focus targets across systems.
Proc. ACM Interact. Mob. Wearable Ubiquitous Technol., Vol. 0, No. 0, Article 0. Publication date: September 2026.

PULSE: Agentic Investigation with Passive Sensing for Proactive Affective Intervention in Cancer Survivorship•0:13
5.2.1 Regulation Desire (ER_desire).Auto-Multi achieves 0.743 BA, compared with 0.655 for Struct-Multi, 0.629
for CALLM, and 0.651 for Auto-Sense. Thus, the structured–agentic difference within the multimodal condition
is 0.088, while the Auto-Multi–Auto-Sense difference associated with providing the current diary is 0.092. Diary
text can express the user’s current feelings and regulation concerns directly, making the latter pattern plausible,
although the comparison does not isolate which part of the diary representation carries the signal.
5.2.2 Intervention Availability (INT_availability).The corresponding current-diary difference for intervention
availability is only 0.010 (Auto-Sense 0.713; Auto-Multi 0.722), compared with 0.092 for regulation desire. Auto-
Sense also exceeds CALLM (0.545) and Struct-Multi (0.552) on this target. This target-dependent pattern is notable
because the diary contributes much less to stated availability than to regulation desire. The simple baselines yield
BA .485 from time-of-day features and .540 after adding pre-EMA-hour motion-state minutes (Appendix B.5).
Time and recent motion therefore provide a useful reference but do not reproduce the Auto-Sense result.
5.2.3 Joint Intervention Opportunity Framing.Under our study-specific framing, both desire and availability
would be relevant at a decision point. Auto-Multi achieves BA values of 0.743 and 0.722 on these two components,
respectively. We do not introduce a separate conjunction metric, and the evaluation does not test an intervention-
delivery rule. Whether these predictions improve a JITAI decision therefore remains a prospective question.
5.3 Aggregate Performance Across All Conditions
Table 6 brings the target-level results into one view. It includes the four factorial conditions, the diary-based
CALLM baseline, and the conventional reference models, with mean BA shown as a compact summary across
the four focus targets.
Struct-Sense is near chance on the four focus targets, whereas Auto-Sense reaches a mean BA of 0.637. In the
multimodal condition, mean BA is 0.601 for Struct-Multi and 0.725 for Auto-Multi. The fact that the structured
LLM conditions do not automatically exceed the conventional references suggests that replacing a supervised
model with a single prompted LLM call is not sufficient by itself.
Auto-Multi has the highest mean BA among the five main systems and is above each reference baseline in the
aggregate table. These broader comparisons provide context but are not directly controlled: the systems differ in
training population, feature access, temporal resolution, and retrieval. The within-design contrasts therefore
remain the more informative comparisons.
MiniLM is the strongest lightweight reference. Auto-Multi exceeds MiniLM+LR by .027BA on PA, .037on NA,
.062on regulation desire, and .119on intervention availability. MiniLM+LR is trained on roughly 16,000 labeled
entries from the other 349 participants, whereas Auto-Multi receives outcome-labeled examples through retrieval
at inference time. The comparison is therefore descriptive rather than directly controlled (Appendix B.5).
5.4 Affect State Detection
Affect state detection follows the same factorial pattern (Table 4). PA_State differs by 0.190 BA in the multimodal
condition (Auto-Multi: 0.720; Struct-Multi: 0.530), the largest single-target difference in the design. Struct-Multi
predicts the positive class on 7% of entries against a roughly 55% base rate (sensitivity .09, specificity .95), while
Auto-Multi predicts it on 54%. One plausible explanation is that personal-baseline and retrieved-outcome cues
help the agentic condition recognize positive states more often, although these channels were not independently
manipulated. The result is therefore driven not merely by a small improvement around the decision boundary,
but by a large difference in how often the positive state is recognized.
For NA_State, the BA values are 0.641 for CALLM, 0.666 for Struct-Multi, and 0.716 for Auto-Multi; the Struct-
Multi–Auto-Multi difference is 0.051. Diary text is often directly expressive of negative emotion, which may help
explain why the structured and diary-only systems are stronger here than on PA_State. Auto-Multi nevertheless
Proc. ACM Interact. Mob. Wearable Ubiquitous Technol., Vol. 0, No. 0, Article 0. Publication date: September 2026.

0:14•Zhiyuan Wang, Subigya Nepal, Ariful Islam, Indrajeet Ghosh, Xinyu Chen, Katharine E. Daniel, Laura E. Barnes, and Philip Chow
Table 5. Descriptive pairwise contrasts. Bootstrap tests resample entries (10,000 resamples) and do not account for within-user
dependence.
Comparison TargetΔBA𝑝-value 95% CI
Auto-Multi vs. Struct-Multi
PA_State +.190<.0001[+.173, +.208]
NA_State +.051<.0001[+.037, +.064]
ER_desire +.088<.0001[+.072, +.105]
INT_availability +.171<.0001[+.152, +.190]
Mean BA +.124<.0001[+.113, +.136]
Auto-Sense vs. Struct-Sense
PA_State +.093<.0001[+.077, +.110]
NA_State +.082<.0001[+.064, +.099]
ER_desire +.145<.0001[+.128, +.161]
INT_availability +.170<.0001[+.153, +.186]
Mean BA +.122<.0001[+.112, +.133]
remains higher, indicating that the additional context available in that condition contributes information beyond
the diary-only result.
5.5 No Current Diary vs. Multimodal: Observed Difference
Table 7 reports the observed difference associated with including the current diary within the agentic condition.
Mean BA changes from 0.637 to 0.725. The differences are 0.125 for both affect states and 0.092 for regulation
desire, but only 0.010 for intervention availability. The current diary is therefore associated with a substantial
change for affect and regulation desire, whereas the availability result is comparatively stable when the current
diary is withheld. This distinction motivates the construct-level discussion in Section 6 rather than a single
conclusion about the value of diary input.
5.6 Statistical Significance and Effect Sizes
The entry-level bootstrap analysis uses 10,000 resamples and reports𝑝<. 0001for all four target contrasts in both
concurrent-input conditions. Table 5 reports the observed differences and 95% bootstrap intervals. The directional
tests evaluate whether BA is higher for the agentic condition than for the structured condition. Because entry
resampling ignores within-user dependence, we treat these tests as descriptive.
Table 8 complements the pooled contrasts with across-user dispersion for Auto-Multi; SDs range from .091 to
.116 across the four focus targets.
5.7 Continuous-Score Bias and Failure Modes
The continuous outputs show systematic bias. Auto-Multi over-predicts Negative Affect (predicted mean∼6.2 vs.
observed mean∼3.2; MAE 4.21) and under-predicts Positive Affect (predicted mean∼16.7 vs. observed mean
∼18.0; MAE 5.42), with compressed PA variance (predicted SD 4.7 vs. observed SD 8.1). ER desire has MAE 1.74
and correlation𝑟=.61; these are agreement measures, not a calibration test.
The model emits continuous scores and binary state labels as separate fields; the binary results therefore
do not establish that the continuous scores are well calibrated. The non-agentic LLM systems show smaller
continuous-scale error on some targets but lower binary BA. We therefore report the continuous and binary
results separately. The continuous negativity bias remains a failure mode.
Proc. ACM Interact. Mob. Wearable Ubiquitous Technol., Vol. 0, No. 0, Article 0. Publication date: September 2026.

PULSE: Agentic Investigation with Passive Sensing for Proactive Affective Intervention in Cancer Survivorship•0:15
5.8 Agentic Investigation Patterns
5.8.1 Tool Usage Patterns.Three core tools appear in 99.7% of Auto-Multi predictions. They are get_daily_
summary, get_behavioral_timeline, and find_peer_cases; the last follows a standing prompt instruction.
compare_to_baselineappears in 60.7%, and the remaining tools in 4.3–14.2%.
Two analyses examine negativity bias. The system predicts elevated NA on 30.0% of entries against an observed
base rate of roughly 32%, with a 16.9% false-positive rate. Tool–prediction co-occurrence is higher for several
optional drill-down tools, but this correlational pattern does not show whether tool use causes negative predictions
or follows initial suspicion. In a controlled neutral-prompt comparison, the observed negative-prediction rate,
false-positive rate, and balanced accuracy each change by less than .01 (Appendix B.4).
5.8.2 Confidence Stratification.Each prediction includes a self-reported confidence score between 0 (not at all
confident) and 1 (entirely confident) (mean 0.76, SD = 0.10 sample-wise). Accuracy differs across confidence bands:
predictions below 0.65 achieve 66.9% average accuracy across the four focus targets, predictions from 0.65–0.80
achieve 74.1%, and predictions above 0.80 achieve 82.5%. These bands describe an association, not probabilistic
calibration. We examine regulation desire in Section 5.9.
5.8.3 Computational Footprint.Each prediction consumes approximately 88,000 input tokens and 4,000 output
tokens, with session memory growing to roughly 50K characters per user by the end of the evaluation. Each
prediction takes 30–90 seconds wall-clock time, including MCP server startup, multi-turn tool use, and response
generation.
5.8.4 Session-Memory Reflection Ablation.Removing the per-entry reflection document while retaining the
other memory and history channels reduces regulation-desire BA by approximately .025; no consistent difference
appears for PA, NA, or intervention availability (Appendix B.2). This analysis isolates the reflection document
rather than the full memory system.
Appendix C presents one constructed interface example and two selected rationales that illustrate which
historical-outcome channels appeared in model context.
5.9 Confidence over Entry Position
Self-reported confidence rises from 0.69 to 0.76 across the first 70 entry positions. Because entry position also
tracks accumulated history and sensing coverage, this trend is descriptive.
Confidence stratifies accuracy (Figure 3a): for regulation desire, balanced accuracy rises across confidence bands,
from 65.5% (confidence≈0.40, 𝑛=55) through 70.8% and 81.6% to 92.2% at confidence≥0.85 (𝑛=348). Verbalized
confidence is known to be informative but often miscalibrated [76], so we test only whether accuracy rises with
reported confidence.
6 Discussion
6.1 Interpreting the Structured–Agentic Difference
The structured–agentic comparison changes both interaction style and available information. The structured
condition receives a preassembled sensing summary, a longitudinal memory document, and outcome-labeled peer
examples in a single prompt. The agentic condition instead works through a multi-turn interface: it can request
additional temporal detail, compare an observation with a personal baseline, and retrieve similar days before
producing a prediction. We therefore interpret the result as a comparison between the two implemented systems.
One candidate explanation isselective evidence assembly. A fixed summary presents the same categories in the
same order for every entry. The interactive condition can begin with a broad overview and then spend additional
queries on the modalities or time windows that appear relevant for that person and moment. A possible sleep
Proc. ACM Interact. Mob. Wearable Ubiquitous Technol., Vol. 0, No. 0, Article 0. Publication date: September 2026.

0:16•Zhiyuan Wang, Subigya Nepal, Ariful Islam, Indrajeet Ghosh, Xinyu Chen, Katharine E. Daniel, Laura E. Barnes, and Philip Chow
0.40 0.55 0.70 0.85+
Model confidence
60
80
100
ER desire acc. (%)
65.5%
70.8%
81.6%
92.2%
(a) Confidence stratification.
0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0
Confidence
0
500
1000
Count (b) Confidence distribution.
Fig. 3. Self-reported confidence. (a) Regulation-desire balanced accuracy by confidence band, increasing from 65.5% to 92.2%;
this is stratification rather than a probabilistic calibration test. (b) Confidence distribution.
disruption, unusual screen pattern, or mobility change can lead to different follow-up queries. This flexibility
does not guarantee that the selected evidence is useful, but it allows the available context to depend on the entry
rather than solely on a template.
A second candidate explanation is explicit access topersonal comparison and episodic examples. The compare_
to_baseline tool turns an absolute observation into a within-person deviation, while find_similar_days
returns earlier same-user cases and their outcomes. The agentic condition can decide when to request these
comparisons and combine them with outcome-labeled peer cases. The structured conditions also receive peer
examples, so peer retrieval alone cannot account for the observed difference; the distinction lies in the broader
combination of interactive querying, personal comparison, and accessible history.
These design choices instantiate contextual behavioral signal interpretation [45, 77]: meaning is assembled
from a person’s recent behavior, baseline, and related episodes rather than from a single population-level feature
vector. Because these components were not independently ablated, they remain candidate explanations. The
matched-call analysis (Section 5.1.1) shows that repeated structured sampling does not close the observed gap.
6.2 The Diary Paradox and Graceful Degradation
Prompt-level EMA work shows that affective states can predict subsequent nonresponse in some cohorts [42],
and broader mHealth work documents bias from non-random missingness [ 19]. We use “diary paradox” to
describe the resulting design tension: diary text can be highly informative when it is present, yet a system that
depends on the current diary cannot use that text when a prompt is omitted. The present benchmark evaluates
the first technical step in that problem—withholding the current diary on completed EMA occasions—rather than
performance at the omitted occasions themselves.
With the current diary withheld, mean BA drops from 0.725 to 0.637. The size of the difference depends strongly
on the target. It is 0.125 for both affect states and 0.092 for regulation desire, but only 0.010 for intervention
availability. The no-current-diary condition therefore preserves much more of the availability result than of the
affect and desire results. This pattern is more informative than the aggregate difference because it shows where a
current diary changes the prediction problem most.
This result supports a fallback design in which the system can still return an estimate when the current diary is
unavailable, while recognizing that the estimate may degrade differently across targets. It does not establish that
such a fallback is adequate for intervention delivery. The same circumstances that reduce diary completion may
also change sensing coverage: a phone may be left behind, turned off, or used differently. A prospective study
Proc. ACM Interact. Mob. Wearable Ubiquitous Technol., Vol. 0, No. 0, Article 0. Publication date: September 2026.

PULSE: Agentic Investigation with Passive Sensing for Proactive Affective Intervention in Cancer Survivorship•0:17
should therefore include prompted occasions whether or not a diary was completed, record the sensing available
at those moments, and evaluate whether target-specific performance changes under actual nonresponse.
6.3 Regulation Desire and Stated Availability
The observed current-diary difference is larger for regulation desire (+0.092) than for intervention availability
(+0.010), suggesting that the two labels capture different predictive information. Regulation desire records
whether the participant wants to regulate their current emotional state. Intervention availability records whether
the participant reports being available to engage with support. They are related at a decision point, but neither is
a substitute for the other: someone may want to change how they feel while being occupied, or may be available
without currently wanting to regulate emotion.
One plausible interpretation of the result is that diary text is closer to the internal experience represented by
regulation desire. A diary can directly express distress, conflict, gratitude, or uncertainty, all of which may inform
a desire to regulate emotion. Availability may align more strongly with contextual patterns such as time, activity,
and recent phone interaction, which remain visible without the current diary. The simple-baseline analysis,
however, shows that time of day and recent motion alone reach only .485 and .540 BA, respectively; these two
cues do not reproduce the availability result.
Taken together, these results support modeling and evaluating desire and stated availability separately as
candidate tailoring variables [29, 39, 43]. A single receptivity label or aggregate score would obscure their different
associations with current-diary input.
6.4 Outcome-Labeled Peer Retrieval
The cross-user RAG mechanism differs from factual RAG in question answering [3, 30]. Rather than retrieving
documents that contain an answer, it returns cases selected as similar together with their observed study outcomes.
We therefore call itoutcome-labeled peer retrieval. These examples provide a local empirical reference: the model
can see how affect, desire, and availability were labeled for participants whose diary text or sensing fingerprint
resembles the current case.
This design is potentially useful when the same behavioral measurement has different meanings across
contexts. Retrieved outcomes can supply cohort-specific examples alongside the model’s general knowledge and
the person’s own history. In the agentic condition, peer retrieval can also be considered together with same-user
similar days and explicit baseline comparisons. That combination offers one route for relating a current pattern
to both idiographic and population context.
Because peer retrieval exposes the model to outcome distributions from the cancer-survivor cohort, its utility
may depend on how well the reference cohort matches the target population. A database dominated by one
demographic group or care context may provide less relevant analogies for another. Peer retrieval is part of the
evaluated system and was not independently ablated, so we do not attribute the performance difference to it
alone.
6.5 Limitations
Retrospective evaluation.Pulsewas evaluated on existing BUCS data, not in a prospective deployment. Real-
time use would introduce latency, network, model-availability, and interface constraints that are not captured
here and require prospective evaluation.
Sample size and dependence.The evaluation includes 50 users. Because entries are repeated within users, the
pooled entry bootstrap does not support population-level significance claims. The sample is also predominantly
female (90%) and White (94%), which limits generalizability.
Proc. ACM Interact. Mob. Wearable Ubiquitous Technol., Vol. 0, No. 0, Article 0. Publication date: September 2026.

0:18•Zhiyuan Wang, Subigya Nepal, Ariful Islam, Indrajeet Ghosh, Xinyu Chen, Katharine E. Daniel, Laura E. Barnes, and Philip Chow
Baseline and condition comparability.The broader baselines differ in training data and feature access.
Within the factorial design, the structured and agentic conditions share users and current-input modality but not
identical information interfaces. The design therefore supports system comparison rather than a causal claim
about reasoning architecture.
Model dependency.All experiments used a single LLM (Claude Sonnet). While another tool-capable model
could instantiate the system, performance may vary. Open-weight alternatives such as LLaMA [60] could improve
reproducibility and support research on local deployment. The MCP tool interface facilitates future cross-model
evaluation.
Inference cost.Each prediction requires 30–90 seconds and roughly 90K tokens of LLM inference, making
full-cohort evaluation expensive and real-time deployment cost-sensitive. This cost constrained our evaluation to
50 of 399 available users. Model distillation or on-device inference could reduce cost, but whether they preserve
the observed performance is unknown.
6.6 Implications for JITAI Design
The study suggests four priorities for JITAI research [43]:
(1) Model desire and availability separately.A decision point may depend on both the desire to regulate
emotion and the practical availability to engage. Their different associations with the current diary argue
against collapsing them into a single receptivity target before each component is understood.
(2) Compare interactive and preassembled information access.The agentic interface lets the model
request personal comparisons and follow up on selected observations. Future studies should compare it
with non-agentic systems that receive comparable information so that the value of interaction, retrieval,
and additional context can be distinguished.
(3) Plan explicitly for missing current input.A system may use the current diary when available while
retaining a no-current-diary pathway. The target-dependent differences here show why the quality of that
fallback should be evaluated separately for affect, regulation desire, and availability rather than summarized
by one average.
(4) Evaluate outcome-labeled retrieval as a component.Similar cases can provide useful empirical context,
but they also carry cohort-specific outcome distributions. Retrieval databases, similarity functions, and
cross-population transfer should therefore be examined directly before they inform intervention timing.
These priorities complement rather than replace established JITAI development methods. Observational studies
can identify candidate tailoring variables, and microrandomized trials can estimate the proximal effects of
intervention options at decision points [26].Pulseaddresses a different layer: how behavioral observations can be
assembled into state estimates when inputs vary across moments. The resulting decision rules and interventions
would still require prospective experimental evaluation.
6.7 Ethical Considerations
This study was conducted under IRB oversight, and all participants provided informed consent for passive
smartphone sensing and EMA data collection. Data were de-identified before analysis, with participant IDs
replaced by numeric study identifiers.
The combination of passive sensing data and LLM-based inference raises privacy considerations. Sensing
data, although it contains no message or diary content, can reveal sensitive behavioral patterns (location history,
communication patterns, sleep disruption). As Coravos et al. [14] emphasize, digital biomarkers must be developed
with safety and effectiveness frameworks from the outset. In this study, data were processed in a research context
with appropriate safeguards. Future deployment would require careful attention to data handling practices [51],
Proc. ACM Interact. Mob. Wearable Ubiquitous Technol., Vol. 0, No. 0, Article 0. Publication date: September 2026.

PULSE: Agentic Investigation with Passive Sensing for Proactive Affective Intervention in Cancer Survivorship•0:19
user control over data sharing, transparency about how predictions are generated [38], and compliance with
applicable privacy regulations.
We emphasize thatPulseis a prediction layer, not a clinical intervention or diagnostic system [ 31, 62]. Its
predictions are intended to inform intervention delivery decisions within a broader JITAI framework, not to
replace clinical assessment. The system should not be the sole determinant of clinical action. False-positive
predictions could increase unnecessary check-ins or alerts, so deployment studies should evaluate alert burden
alongside missed opportunities for support.
The use of LLM APIs for behavioral-health data raises questions about transmission and storage. In the current
implementation, model inputs are de-identified. On-device models [54, 71, 83] could reduce external transmission
and, under a fully local architecture, eliminate model-input transmission to an external provider.
7 Future Work
Several directions follow from this work. First, a prospective study should evaluate the system at actual decision
points, including occasions with no completed diary, and use a microrandomized or related design if predictions
are connected to intervention delivery [26]. Such a study should record sensor coverage and retain outcomes
independently of whether the participant answers the current prompt. Second, a future component study could
provide comparable information and inference budgets while varying personal-baseline queries, same-user
retrieval, peer retrieval, and the reflection document separately. This would test the candidate explanations in
Section 6 beyond the full-system comparison reported here. Third, cross-model and local-model experiments
can test whether the observed patterns depend on Claude Sonnet and whether smaller or on-device models can
support the same tool interface [54, 71, 83]. Finally, evaluation beyond cancer survivors should examine how the
tool design, retrieved cohort, and target definitions transfer to other populations and sensing settings.
8 Conclusion
This paper introducesPulse, an LLM system that combines multi-turn sensing queries, personal-baseline
comparisons, and outcome-labeled historical retrieval. Rather than relying on one preassembled summary, the
model can request additional behavioral context before returning the study-target predictions.
In a 50-user retrospective benchmark, the agentic conditions score above structured single-pass systems
under both concurrent-input settings. Because the conditions also differ in accessible information, these results
characterize the implemented systems rather than isolate one causal mechanism. The matched-call analysis
narrows one alternative explanation, while the remaining contribution of interaction, personal comparison,
retrieval, and memory requires component-level study.
The association with the current diary is also target-dependent. Emotion-regulation desire and affect change
appreciably when the diary is withheld, whereas self-reported availability changes little in this evaluation. This
distinction motivates separate treatment of desire and availability and a fallback pathway when current self-report
is absent. More broadly, the study shows how interactive sensing investigation can be operationalized for affect
and availability prediction. Its value for JITAI decisions, omitted-prompt settings, and other populations now
requires prospective evaluation with comparable information access across conditions.
References
[1] Daniel A. Adler, Fei Wang, David C. Mohr, and Tanzeem Choudhury. 2022. Machine Learning for Passive Mental Health Symptom
Prediction: Generalization Across Different Longitudinal Mobile Sensing Studies.PLOS ONE17, 4 (2022), e0266516. doi:10.1371/journal.
pone.0266516
[2] Daniel A. Adler, Yuewen Yang, Thalia Viranda, Xuhai Xu, David C. Mohr, Anna R. Van Meter, Julia C. Tartaglia, Nicholas C. Jacobson,
Fei Wang, Deborah Estrin, and Tanzeem Choudhury. 2024. Beyond Detection: Towards Actionable Sensing Research in Clinical Mental
Proc. ACM Interact. Mob. Wearable Ubiquitous Technol., Vol. 0, No. 0, Article 0. Publication date: September 2026.

0:20•Zhiyuan Wang, Subigya Nepal, Ariful Islam, Indrajeet Ghosh, Xinyu Chen, Katharine E. Daniel, Laura E. Barnes, and Philip Chow
Healthcare.Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies8, 4, Article 160 (2024), 33 pages.
doi:10.1145/3699755
[3] Lameck Mbangula Amugongo, Pietro Mascheroni, Steven Brooks, Stefan Doering, and Jan Seidel. 2025. Retrieval-Augmented Generation
for Large Language Models in Healthcare: A Systematic Review.PLOS Digital Health4, 6 (2025), e0000877. doi:10.1371/journal.pdig.
0000877
[4] Tuo An, Yunjiao Zhou, Han Zou, and Jianfei Yang. 2026. IoT-LLM: A Framework for Enhancing Large Language Model Reasoning from
Real-World Sensor Data.Patterns7, 1 (2026), 101429. doi:10.1016/j.patter.2025.101429
[5] Barbara L. Andersen, Christina Lacchetti, Kimlin Ashing, Jonathan S. Berek, Barry S. Berman, Sage Bolte, Don S. Dizon, Barbara Given,
Larissa Nekhlyudov, William Pirl, Annette L. Stanton, and Julia H. Rowland. 2023. Management of Anxiety and Depression in Adult
Survivors of Cancer: ASCO Guideline Update.Journal of Clinical Oncology41, 18 (2023), 3426–3453. doi:10.1200/JCO.23.00293
[6] Anthropic. 2024. Introducing the Model Context Protocol. https://www.anthropic.com/news/model-context-protocol.
[7] Lauren Bell, Claire Garnett, Yihan Bao, Zhaoxi Cheng, Tianchen Qian, Olga Perski, Henry W. W. Potts, and Elizabeth Williamson. 2023.
How Notifications Affect Engagement With a Behavior Change App: Results From a Micro-Randomized Trial.JMIR mHealth and
uHealth11 (2023), e38342. doi:10.2196/38342
[8] Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam,
Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh,
Daniel M. Ziegler, Jeffrey Wu, Clemens Winter, Christopher Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess,
Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya Sutskever, and Dario Amodei. 2020. Language Models are Few-Shot
Learners. InAdvances in Neural Information Processing Systems (NeurIPS 2020), Vol. 33. 1877–1901.
[9] Pasquale Bufano, Marco Laurino, Sara Said, Alessandro Tognetti, and Danilo Menicucci. 2023. Digital Phenotyping for Monitoring
Mental Disorders: Systematic Review.Journal of Medical Internet Research25 (2023), e46778. doi:10.2196/46778
[10] Luca Canzian and Mirco Musolesi. 2015. Trajectories of Depression: Unobtrusive Monitoring of Depressive States by means of
Smartphone Mobility Traces Analysis. InProceedings of the 2015 ACM International Joint Conference on Pervasive and Ubiquitous
Computing. 1293–1304.
[11] Prerna Chikersal, Afsaneh Doryab, Michael J. Tumminia, Daniella K. Villalba, Janine M. Dutcher, Xinwen Liu, Sheldon Cohen, Kasey G.
Creswell, Jennifer Mankoff, J. David Creswell, Mayank Goel, and Anind K. Dey. 2021. Detecting depression and predicting its onset
using longitudinal symptoms captured by passive sensing: a machine learning approach with robust feature selection.ACM Transactions
on Computer-Human Interaction (TOCHI)28, 1 (2021), 1–41.
[12] Adrien Choi, Aysel Ooi, and Danielle Lottridge. 2024. Digital Phenotyping for Stress, Anxiety, and Mild Depression: Systematic Literature
Review.JMIR mHealth and uHealth12 (2024), e40689. doi:10.2196/40689
[13] Akshat Choube, Ha Le, Jiachen Li, Kaixin Ji, Vedant Das Swain, and Varun Mishra. 2025. GLOSS: Group of LLMs for Open-Ended
Sensemaking of Passive Sensing Data for Health and Wellbeing.Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous
Technologies9, 3, Article 76 (2025), 32 pages. doi:10.1145/3749474
[14] Andrea Coravos, Sean Khozin, and Kenneth D. Mandl. 2019. Developing and Adopting Safe and Effective Digital Biomarkers to Improve
Patient Outcomes.npj Digital Medicine2, 1 (2019), 14. doi:10.1038/s41746-019-0090-4
[15] Katharine E. Daniel, James W. Kinchen, Angela Chang, Patrick H. Finan, and Philip I. Chow. 2025. Identifying Time-Variant Predictors of
Interest in Completing Brief Digital Mental Health Interventions Among Adult Survivors of Cancer: Ecological Momentary Assessment
Study.JMIR mHealth and uHealth13 (2025), e69244. doi:10.2196/69244
[16] Kaidong Feng, Zhu Sun, Roy Ka-Wei Lee, Xun Jiang, Yin-Leng Theng, and Yi Ding. 2026. A Comparative Study of Traditional Machine
Learning, Deep Learning, and Large Language Models for Mental Health Forecasting using Smartphone Sensing Data.arXiv preprint
arXiv:2601.03603(2026). https://arxiv.org/abs/2601.03603
[17] Emilio Ferrara. 2024. Large Language Models for Wearable Sensor-Based Human Activity Recognition, Health Monitoring, and
Behavioral Modeling: A Survey of Early Trends, Datasets, and Challenges.Sensors24, 15 (2024), 5045. doi:10.3390/s24155045
[18] Denzil Ferreira, Vassilis Kostakos, and Anind K. Dey. 2015. AWARE: Mobile Context Instrumentation Framework.Frontiers in ICT2
(2015), 6. doi:10.3389/fict.2015.00006
[19] Simon B Goldberg, Daniel M Bolt, and Richard J Davidson. 2021. Data Missing Not at Random in Mobile Health Research: Assessment
of the Problem and a Case for Sensitivity Analyses.Journal of Medical Internet Research23, 6 (2021), e26749. doi:10.2196/26749
[20] James J. Gross. 2015. Emotion Regulation: Current Status and Future Prospects.Psychological Inquiry26, 1 (2015), 1–26. doi:10.1080/
1047840X.2014.940781
[21] Xu Huang, Weiwen Liu, Xiaolong Chen, Xingmei Wang, Hao Wang, Defu Lian, Yasheng Wang, Ruiming Tang, and Enhong Chen. 2024.
Understanding the Planning of LLM Agents: A Survey.arXiv preprint arXiv:2402.02716(2024). https://arxiv.org/abs/2402.02716
[22] Jeremy F. Huckins, Alex W. daSilva, Weichen Wang, Elin Hedlund, Courtney Rogers, Subigya K. Nepal, Jialing Wu, Mikio Obuchi, Eilis I.
Murphy, Meghan L. Meyer, Dylan D. Wagner, Paul E. Holtzheimer, and Andrew T. Campbell. 2020. Mental Health and Behavior of
College Students During the Early Phases of the COVID-19 Pandemic: Longitudinal Smartphone and Ecological Momentary Assessment
Study.Journal of Medical Internet Research22, 6 (2020), e20185. doi:10.2196/20185
Proc. ACM Interact. Mob. Wearable Ubiquitous Technol., Vol. 0, No. 0, Article 0. Publication date: September 2026.

PULSE: Agentic Investigation with Passive Sensing for Proactive Affective Intervention in Cancer Survivorship•0:21
[23] Nicholas C. Jacobson, Hilary Weingarden, and Sabine Wilhelm. 2019. Digital Biomarkers of Mood Disorders and Symptom Change.npj
Digital Medicine2, 1 (2019), 3. doi:10.1038/s41746-019-0078-0
[24] Justin Khasentino, Anastasiya Belyaeva, Xin Liu, Zhun Yang, Nicholas A. Furlotte, Chace Lee, Erik Schenck, Yojan Patel, Jian Cui,
Logan Douglas Schneider, Robby Bryant, Ryan G. Gomes, Allen Jiang, Roy Lee, Yun Liu, Javier Perez, Jameson K. Rogers, Cathy Speed,
Shyam Tailor, Megan Walker, Jeffrey Yu, Tim Althoff, Conor Heneghan, John Hernandez, Mark Malhotra, Leor Stern, Yossi Matias,
Greg S. Corrado, Shwetak Patel, Shravya Shetty, Jiening Zhan, Shruthi Prabhakara, Daniel McDuff, and Cory Y. McLean. 2025. A personal
health large language model for sleep and fitness coaching.Nature Medicine31, 10 (2025), 3394–3403. doi:10.1038/s41591-025-03888-0
[25] Yubin Kim, Xuhai Xu, Daniel McDuff, Cynthia Breazeal, and Hae Won Park. 2024. Health-LLM: Large Language Models for Health
Prediction via Wearable Sensor Data. InProceedings of Machine Learning Research (CHIL), Vol. 248. 522–539.
[26] Predrag Klasnja, Eric B Hekler, Saul Shiffman, Audrey Boruvka, Daniel Almirall, Ambuj Tewari, and Susan A Murphy. 2015. Mi-
crorandomized Trials: An Experimental Design for Developing Just-in-Time Adaptive Interventions.Health Psychology34, S (2015),
1220–1228.
[27] Predrag Klasnja, Shawna Smith, Nicholas J. Seewald, Andy Lee, Kelly Hall, Brook Luers, Eric B. Hekler, and Susan A. Murphy. 2019.
Efficacy of Contextually Tailored Suggestions for Physical Activity: A Micro-randomized Optimization Trial of HeartSteps.Annals of
Behavioral Medicine53, 6 (2019), 573–582. doi:10.1093/abm/kay067
[28] Kurt Kroenke, Robert L Spitzer, and Janet BW Williams. 2001. The PHQ-9: validity of a brief depression severity measure.Journal of
general internal medicine16, 9 (2001), 606–613.
[29] Florian Künzler, Varun Mishra, Jan-Niklas Kramer, David Kotz, Elgar Fleisch, and Tobias Kowatsch. 2019. Exploring the State-of-
Receptivity for mHealth Interventions.Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies3, 4, Article
140 (2019), 27 pages. doi:10.1145/3369805
[30] Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich Küttler, Mike Lewis, Wen-tau
Yih, Tim Rocktäschel, Sebastian Riedel, and Douwe Kiela. 2020. Retrieval-augmented generation for knowledge-intensive nlp tasks.
Advances in Neural Information Processing Systems33 (2020), 9459–9474.
[31] Han Li, Renwen Zhang, Yi-Chieh Lee, Robert E. Kraut, and David C. Mohr. 2023. Systematic Review and Meta-Analysis of AI-Based
Conversational Agents for Promoting Mental Health and Well-Being.npj Digital Medicine6, 1 (2023), 236. doi:10.1038/s41746-023-00979-5
[32] Jiachen Li, Xiwen Li, Justin Steinberg, Akshat Choube, Bingsheng Yao, Xuhai Xu, Dakuo Wang, Elizabeth Mynatt, and Varun Mishra.
2025. Vital Insight: Assisting Experts’ Context-Driven Sensemaking of Multi-modal Personal Tracking Data Using Visualization and
Human-in-the-Loop LLM.Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies9, 3, Article 101 (2025),
37 pages. doi:10.1145/3749508
[33] Zechen Li, Shohreh Deldari, Linyao Chen, Hao Xue, and Flora D Salim. 2025. SensorLLM: Aligning Large Language Models with Motion
Sensors for Human Activity Recognition. InProceedings of the 2025 Conference on Empirical Methods in Natural Language Processing
(EMNLP 2025). 354–379. doi:10.18653/v1/2025.emnlp-main.19
[34] Yusheng Liao, Shuyang Jiang, Yanfeng Wang, and Yu Wang. 2025. ReflecTool: Towards Reflection-Aware Tool-Augmented Clinical Agents.
InProceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL). 13507–13531. doi:10.18653/v1/2025.acl-
long.663
[35] Stephanie Lin, Jacob Hilton, and Owain Evans. 2022. Teaching Models to Express Their Uncertainty in Words.Transactions on Machine
Learning Research(2022).
[36] Lakmal Meegahapola, William Droz, Peter Kun, Amalia de Götzen, Chaitanya Nutakki, Shyam Diwakar, Salvador Ruiz-Correa, Donglei
Song, Hao Xu, Miriam Bidoglia, George Gaskell, Altangerel Chagnaa, Amarsanaa Ganbold, Tsolmon Zundui, Carlo Caprini, Daniele
Miorandi, Alethia Hume, José Luis Zarza, Luca Cernuzzi, Ivano Bison, Marcelo Rodas Britez, Matteo Busso, Ronald Chenu-Abente, Can
Günel, Fausto Giunchiglia, Laura Schelenz, and Daniel Gatica-Perez. 2022. Generalization and Personalization of Mobile Sensing-Based
Mood Inference Models: An Analysis of College Students in Eight Countries.Proceedings of the ACM on Interactive, Mobile, Wearable
and Ubiquitous Technologies6, 4 (2022), 1–32. doi:10.1145/3569483
[37] Mike A. Merrill, Akshay Paruchuri, Naghmeh Rezaei, Geza Kovacs, Javier Perez, Yun Liu, Erik Schenck, Nova Hammerquist, Jake
Sunshine, Shyam Tailor, Kumar Ayush, Hao-Wei Su, Qian He, Cory Y. McLean, Mark Malhotra, Shwetak Patel, Jiening Zhan, Tim Althoff,
Daniel McDuff, and Xin Liu. 2026. Transforming Wearable Data into Personal Health Insights using Large Language Model Agents.
Nature Communications17 (2026), 1143. doi:10.1038/s41467-025-67922-y
[38] Munib Mesinovic, Peter Watkinson, and Tingting Zhu. 2025. Explainability in the Age of Large Language Models for Healthcare.
Communications Engineering4, 1 (2025), 128. doi:10.1038/s44172-025-00453-y
[39] Varun Mishra, Florian Künzler, Jan-Niklas Kramer, Elgar Fleisch, Tobias Kowatsch, and David Kotz. 2021. Detecting Receptivity for
mHealth Interventions in the Natural Environment.Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies
5, 2, Article 74 (2021), 24 pages. doi:10.1145/3463492
[40] Alex J. Mitchell, Melissa Chan, Henna Bhatti, Marie Halton, Luigi Grassi, Christoffer Johansen, and Nicholas Meader. 2011. Prevalence
of Depression, Anxiety, and Adjustment Disorder in Oncological, Haematological, and Palliative-Care Settings: A Meta-Analysis of 94
Interview-Based Studies.The Lancet Oncology12, 2 (2011), 160–174. doi:10.1016/S1470-2045(11)70002-X
Proc. ACM Interact. Mob. Wearable Ubiquitous Technol., Vol. 0, No. 0, Article 0. Publication date: September 2026.

0:22•Zhiyuan Wang, Subigya Nepal, Ariful Islam, Indrajeet Ghosh, Xinyu Chen, Katharine E. Daniel, Laura E. Barnes, and Philip Chow
[41] David C. Mohr, Kathryn Noth Tomasino, Emily G. Lattie, Hannah L. Palac, Mary J. Kwasny, Kenneth Weingardt, Chris J. Karr, Susan M.
Kaiser, Rebecca C. Rossom, Leland R. Bardsley, Lauren Caccamo, Colleen Stiles-Shields, and Stephen M. Schueller. 2017. IntelliCare: An
Eclectic, Skills-Based App Suite for the Treatment of Depression and Anxiety.Journal of Medical Internet Research19, 1 (2017), e10.
doi:10.2196/jmir.6645
[42] Aja Louise Murray, Ruth Brown, Xinxin Zhu, Lydia Gabriela Speyer, Yi Yang, Zhouni Xiao, Denis Ribeaud, and Manuel Eisner. 2023.
Prompt-level predictors of compliance in an ecological momentary assessment study of young adults’ mental health.Journal of Affective
Disorders322 (2023), 125–131. doi:10.1016/j.jad.2022.11.014
[43] Inbal Nahum-Shani, Shawna N Smith, Bonnie J Spring, Linda M Collins, Katie Witkiewitz, Ambuj Tewari, and Susan A Murphy. 2018.
Just-in-Time Adaptive Interventions (JITAI) in Mobile Health: Key Components and Design Principles for Ongoing Health Behavior
Support.Annals of Behavioral Medicine52, 6 (2018), 446–462.
[44] Inbal Nahum-Shani, Shawna N. Smith, Ambuj Tewari, Katie Witkiewitz, Linda M. Collins, Bonnie J. Spring, and Susan A. Murphy. 2014.
Just-in-Time Adaptive Interventions (JITAIs): An Organizing Framework for Ongoing Health Behavior Support. Technical Report 14-126.
The Methodology Center, Penn State University.
[45] Shrikanth Narayanan and Panayiotis G. Georgiou. 2013. Behavioral Signal Processing: Deriving Human Behavioral Informatics from
Speech and Language.Proc. IEEE101, 5 (2013), 1203–1233. doi:10.1109/JPROC.2012.2236291
[46] Subigya Nepal, Wenjun Liu, Arvind Pillai, Weichen Wang, Vlado Vojdanovski, Jeremy F. Huckins, Courtney Rogers, Meghan L. Meyer,
and Andrew T. Campbell. 2024. Capturing the College Experience: A Four-Year Mobile Sensing Study of Mental Health, Resilience and
Behavior of College Students during the Pandemic.Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies
8, 1 (2024), 1–37. doi:10.1145/3643501
[47] Subigya Nepal, Arvind Pillai, William Campbell, Talie Massachi, Michael V. Heinz, Ashmita Kunwar, Eunsol Soul Choi, Xuhai Xu,
Joanna Kuc, Jeremy F. Huckins, Jason Holden, Sarah M. Preum, Colin Depp, Nicholas Jacobson, Mary P. Czerwinski, Eric Granholm,
and Andrew T. Campbell. 2024. MindScape Study: Integrating LLM and Behavioral Sensing for Personalized AI-Driven Journaling
Experiences.Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies8, 4 (2024), 1–44. doi:10.1145/3699761
[48] Subigya Nepal, Weichen Wang, Vlado Vojdanovski, Jeremy F Huckins, Alex Dasilva, Meghan Meyer, and Andrew Campbell. 2022.
COVID student study: A year in the life of college students during the COVID-19 pandemic through the lens of mobile phone sensing.
InProceedings of the 2022 CHI conference on human factors in computing systems. 1–19. doi:10.1145/3491102.3502043
[49] Jukka-Pekka Onnela and Scott L. Rauch. 2016. Harnessing Smartphone-Based Digital Phenotyping to Enhance Behavioral and Mental
Health.Neuropsychopharmacology41, 7 (2016), 1691–1696. doi:10.1038/npp.2016.7
[50] Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll L. Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina
Slama, Alex Ray, John Schulman, Jacob Hilton, Fraser Kelton, Luke Miller, Maddie Simens, Amanda Askell, Peter Welinder, Paul F.
Christiano, Jan Leike, and Ryan Lowe. 2022. Training Language Models to Follow Instructions with Human Feedback. InAdvances in
Neural Information Processing Systems (NeurIPS 2022), Vol. 35. 27730–27744.
[51] Sarthak Pati, Sourav Kumar, Amokh Varma, Brandon Edwards, Charles Lu, Liangqiong Qu, Justin J Wang, Anantharaman Lakshmi-
narayanan, Shih-Han Wang, Micah J Sheller, Ken Chang, Praveer Singh, Daniel L Rubin, Jayashree Kalpathy-Cramer, and Spyridon
Bakas. 2024. Privacy Preservation for Federated Learning in Health Care.Patterns5, 7 (2024), 100974. doi:10.1016/j.patter.2024.100974
[52] Shishir G. Patil, Tianjun Zhang, Xin Wang, and Joseph E. Gonzalez. 2024. Gorilla: Large Language Model Connected with Massive APIs.
InAdvances in Neural Information Processing Systems (NeurIPS 2024), Vol. 37. https://arxiv.org/abs/2305.15334
[53] Arvind Pillai, Dimitris Spathis, Subigya Nepal, Amanda C. Collins, Daniel M. Mackin, Michael V. Heinz, Tess Z. Griffin, Nicholas C.
Jacobson, and Andrew Campbell. 2025. Beyond Prompting: Time2Lang—Bridging Time-Series Foundation Models and Large Language
Models for Health Sensing. InProceedings of the Conference on Health, Inference, and Learning (CHIL), Vol. 287. PMLR, 268–288.
https://proceedings.mlr.press/v287/pillai25a.html
[54] Guanqiao Qu, Qiyuan Chen, Wei Wei, Zheng Lin, Xianhao Chen, and Kaibin Huang. 2024. Mobile Edge Intelligence for Large Language
Models: A Contemporary Survey.arXiv preprint arXiv:2407.18921(2024). https://arxiv.org/abs/2407.18921
[55] Sohrab Saeb, Mi Zhang, Christopher J Karr, Stephen M Schueller, Marya E Corden, Konrad P Kording, and David C Mohr. 2015. Mobile
Phone Sensor Correlates of Depressive Symptom Severity in Daily-Life Behavior: An Exploratory Study.Journal of Medical Internet
Research17, 7 (2015), e175.
[56] Timo Schick, Jane Dwivedi-Yu, Roberto Dessì, Roberta Raileanu, Maria Lomeli, Eric Hambro, Luke Zettlemoyer, Nicola Cancedda, and
Thomas Scialom. 2023. Toolformer: Language Models Can Teach Themselves to Use Tools. InAdvances in Neural Information Processing
Systems (NeurIPS 2023). https://arxiv.org/abs/2302.04761
[57] Saul Shiffman, Arthur A Stone, and Michael R Hufford. 2008. Ecological momentary assessment.Annual Review of Clinical Psychology4,
1 (2008), 1–32.
[58] Karan Singhal, Shekoofeh Azizi, Tao Tu, S. Sara Mahdavi, Jason Wei, Hyung Won Chung, Nathan Scales, Ajay Tanwani, Heather
Cole-Lewis, Stephen Pfohl, Perry Payne, Martin Seneviratne, Paul Gamble, Chris Kelly, Abubakr Babiker, Nathanael Schärli, Aakanksha
Chowdhery, Philip Mansfield, Dina Demner-Fushman, Blaise Agüera y Arcas, Dale Webster, Greg S. Corrado, Yossi Matias, Katherine
Chou, Juraj Gottweis, Nenad Tomasev, Yun Liu, Alvin Rajkomar, Joelle Barral, Christopher Semturs, Alan Karthikesalingam, and Vivek
Proc. ACM Interact. Mob. Wearable Ubiquitous Technol., Vol. 0, No. 0, Article 0. Publication date: September 2026.

PULSE: Agentic Investigation with Passive Sensing for Proactive Affective Intervention in Cancer Survivorship•0:23
Natarajan. 2023. Large Language Models Encode Clinical Knowledge.Nature620, 7972 (2023), 172–180. doi:10.1038/s41586-023-06291-2
[59] John Torous, Jukka-Pekka Onnela, and Matcheri Keshavan. 2017. New Dimensions and New Tools to Realize the Potential of RDoC:
Digital Phenotyping via Smartphones and Connected Devices.Translational Psychiatry7, 3 (2017), e1053. doi:10.1038/tp.2017.25
[60] Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timothée Lacroix, Baptiste Rozière, Naman
Goyal, Eric Hambro, Faisal Azhar, Aurelien Rodriguez, Armand Joulin, Edouard Grave, and Guillaume Lample. 2023. LLaMA: Open and
Efficient Foundation Language Models.arXiv preprint arXiv:2302.13971(2023). https://arxiv.org/abs/2302.13971
[61] Tao Tu, Mike Schaekermann, Anil Palepu, Khaled Saab, Jan Freyberg, Ryutaro Tanno, Amy Wang, Brenna Li, Mohamed Amin, Yong Cheng,
Elahe Vedadi, Nenad Tomasev, Shekoofeh Azizi, Karan Singhal, Le Hou, Albert Webson, Kavita Kulkarni, S. Sara Mahdavi, Christopher
Semturs, Juraj Gottweis, Joelle Barral, Katherine Chou, Greg S. Corrado, Yossi Matias, Alan Karthikesalingam, and Vivek Natarajan.
2025. Towards conversational diagnostic artificial intelligence.Nature642, 8067 (2025), 442–450. doi:10.1038/s41586-025-08866-7
[62] Aditya Nrusimha Vaidyam, Hannah Wisniewski, John David Halamka, Matcheri S. Kashavan, and John Blake Torous. 2019. Chatbots
and Conversational Agents in Mental Health: A Review of the Psychiatric Landscape.The Canadian Journal of Psychiatry64, 7 (2019),
456–464. doi:10.1177/0706743719828977
[63] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Łukasz Kaiser, and Illia Polosukhin. 2017.
Attention Is All You Need. InAdvances in Neural Information Processing Systems (NeurIPS 2017), Vol. 30. 5998–6008.
[64] Ulrike von Lützow, Nathalie Laura Neuendorf, and Sebastian Scherr. 2025. Effectiveness of Just-in-Time Adaptive Interventions for
Improving Mental Health and Psychological Well-Being: A Systematic Review and Meta-Analysis.BMJ Mental Health28, 1 (2025),
e301641. doi:10.1136/bmjment-2025-301641
[65] Nikita Sandeep Wagle, Leticia Nogueira, Theresa P. Devasia, Angela B. Mariotto, K. Robin Yabroff, Farhad Islami, Ahmedin Jemal, Rick
Alteri, Patricia A. Ganz, and Rebecca L. Siegel. 2025. Cancer treatment and survivorship statistics, 2025.CA: A Cancer Journal for
Clinicians75, 4 (2025), 308–340. doi:10.3322/caac.70011
[66] Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, Chaowei Xiao, Yuke Zhu, Linxi Fan, and Anima Anandkumar. 2024. Voyager:
An Open-Ended Embodied Agent with Large Language Models.Transactions on Machine Learning Research(2024). https://openreview.
net/forum?id=ehfRiF0R3a
[67] Lei Wang, Chen Ma, Xueyang Feng, Zeyu Zhang, Hao Yang, Jingsen Zhang, Zhiyuan Chen, Jiakai Tang, Xu Chen, Yankai Lin, Wayne Xin
Zhao, Zhewei Wei, and Jirong Wen. 2024. A survey on large language model based autonomous agents.Frontiers of Computer Science18,
6 (2024), 186345. doi:10.1007/s11704-024-40231-1
[68] Rui Wang, Min S. H. Aung, Saeed Abdullah, Rachel Brian, Andrew T. Campbell, Tanzeem Choudhury, Marta Hauser, John Kane, Michael
Merrill, Emily A. Scherer, Vincent W. S. Tseng, and Dror Ben-Zeev. 2016. CrossCheck: Toward Passive Sensing and Detection of Mental
Health Changes in People with Schizophrenia. InProceedings of the 2016 ACM International Joint Conference on Pervasive and Ubiquitous
Computing (UbiComp ’16). ACM, 886–897. doi:10.1145/2971648.2971740
[69] Rui Wang, Fanglin Chen, Zhenyu Chen, Tianxing Li, Gabriella Harari, Stefanie Tignor, Xia Zhou, Dror Ben-Zeev, and Andrew T Campbell.
2014. StudentLife: assessing mental health, academic performance and behavioral trends of college students using smartphones. In
Proceedings of the 2014 ACM international joint conference on pervasive and ubiquitous computing. 3–14.
[70] Rui Wang, Weichen Wang, Alex DaSilva, Jeremy F Huckins, William M Kelley, Todd F Heatherton, and Andrew T Campbell. 2018.
Tracking depression dynamics in college students using mobile phone and wearable sensing.Proceedings of the ACM on Interactive,
Mobile, Wearable and Ubiquitous Technologies2, 1 (2018), 1–26.
[71] Xin Wang, Ting Dang, Vassilis Kostakos, and Hong Jia. 2024. Efficient and Personalized Mobile Health Event Prediction via Small
Language Models. InProceedings of the 30th Annual International Conference on Mobile Computing and Networking (MobiCom ’24). ACM,
2353–2358. doi:10.1145/3636534.3698123
[72] Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le, Ed Chi, Sharan Narang, Aakanksha Chowdhery, and Denny Zhou. 2023. Self-
Consistency Improves Chain of Thought Reasoning in Language Models.International Conference on Learning Representations(2023).
[73] Zhiyuan Wang, Katharine E Daniel, Laura E. Barnes, and Philip Chow. 2026. Inferring Affect and Intervention Opportunities for
Cancer Survivors from Digital Diaries with Context-Aware LLMs. InProceedings of the 2026 CHI Conference on Human Factors in
Computing Systems(Barcelona, Spain)(CHI ’26). Association for Computing Machinery, New York, NY, USA, Article 576, 16 pages.
doi:10.1145/3772318.3791352
[74] David Watson, Lee Anna Clark, and Auke Tellegen. 1988. Development and validation of brief measures of positive and negative affect:
The PANAS scales.Journal of Personality and Social Psychology54, 6 (1988), 1063–1070.
[75] Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed Chi, Quoc Le, and Denny Zhou. 2022. Chain-
of-Thought Prompting Elicits Reasoning in Large Language Models.Advances in Neural Information Processing Systems35 (2022),
24824–24837.
[76] Miao Xiong, Zhiyuan Hu, Xinyang Lu, Yifei Li, Jie Fu, Junxian He, and Bryan Hooi. 2024. Can LLMs Express Their Uncertainty? An
Empirical Evaluation of Confidence Elicitation in LLMs. InInternational Conference on Learning Representations (ICLR).
[77] Huatao Xu, Liying Han, Qirui Yang, Mo Li, and Mani Srivastava. 2024. Penetrative AI: Making LLMs Comprehend the Physical World.
InFindings of the Association for Computational Linguistics: ACL 2024. 7324–7341.
Proc. ACM Interact. Mob. Wearable Ubiquitous Technol., Vol. 0, No. 0, Article 0. Publication date: September 2026.

0:24•Zhiyuan Wang, Subigya Nepal, Ariful Islam, Indrajeet Ghosh, Xinyu Chen, Katharine E. Daniel, Laura E. Barnes, and Philip Chow
[78] Wenxuan Xu, Arvind Pillai, Subigya Nepal, Amanda C Collins, Daniel M Mackin, Michael V Heinz, Tess Z Griffin, Nicholas C Jacobson,
and Andrew Campbell. 2025. LENS: LLM-Enabled Narrative Synthesis for Mental Health by Aligning Multimodal Sensing with Language
Models.arXiv preprint arXiv:2512.23025(2025).
[79] Xuhai Xu, Xin Liu, Han Zhang, Weichen Wang, Subigya Nepal, Yasaman Sefidgar, Woosuk Seo, Kevin S. Kuehn, Jeremy F. Huckins,
Margaret E. Morris, Paula S. Nurius, Eve A. Riskin, Shwetak Patel, Tim Althoff, Andrew Campbell, Anind K. Dey, and Jennifer Mankoff.
2022. GLOBEM: Cross-Dataset Generalization of Longitudinal Human Behavior Modeling.Proceedings of the ACM on Interactive, Mobile,
Wearable and Ubiquitous Technologies6, 4, Article 190 (2022), 34 pages. doi:10.1145/3569485
[80] Xuhai Xu, Bingsheng Yao, Yuanzhe Dong, Saadia Gabriel, Hong Yu, James Hendler, Marzyeh Ghassemi, Anind K Dey, and Dakuo Wang.
2024. Mental-llm: Leveraging large language models for mental health prediction via online text data.Proceedings of the ACM on
Interactive, Mobile, Wearable and Ubiquitous Technologies8, 1 (2024), 1–32. doi:10.1145/3643540
[81] Bufang Yang, Lilin Xu, Liekang Zeng, Kaiwei Liu, Siyang Jiang, Wenrui Lu, Hongkai Chen, Xiaofan Jiang, Guoliang Xing, and Zhenyu Yan.
2025. ContextAgent: Context-Aware Proactive LLM Agents with Open-World Sensory Perceptions. InAdvances in Neural Information
Processing Systems (NeurIPS 2025). https://arxiv.org/abs/2505.14668
[82] Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and Yuan Cao. 2023. ReAct: Synergizing Reasoning
and Acting in Language Models. InInternational Conference on Learning Representations.
[83] Shiquan Zhang, Ying Ma, Le Fang, Hong Jia, Simon D’Alfonso, and Vassilis Kostakos. 2024. Enabling On-Device LLMs Personalization
with Smartphone Sensing. InCompanion of the 2024 ACM International Joint Conference on Pervasive and Ubiquitous Computing (UbiComp
’24). ACM, 186–190. doi:10.1145/3675094.3677545
[84] Tianyi Zhang, Songyan Teng, Hong Jia, and Simon D’Alfonso. 2024. Leveraging LLMs to Predict Affective States via Smartphone Sensor
Features. InCompanion of the 2024 ACM International Joint Conference on Pervasive and Ubiquitous Computing (UbiComp ’24). ACM,
Melbourne, Australia, 709–716. doi:10.1145/3675094.3678420
[85] Wenxuan Zhang, Yue Deng, Bing Liu, Sinno Jialin Pan, and Lidong Bing. 2024. Sentiment Analysis in the Era of Large Language Models:
A Reality Check. InFindings of the Association for Computational Linguistics: NAACL 2024. 3881–3906. https://aclanthology.org/2024.
findings-naacl.246/
A Prompt Structure
The complete system prompts, the reflection prompt, and all tool implementations will be released verbatim
with the source code upon publication. Here we document the prompt structure; Table 3 presents the tool
interfaces.
Agentic system prompts.Each agentic prompt contains, in order: a role definition; the task statement for the
concurrent-input condition (multimodal prompts prioritize the current diary, whereas no-current-diary prompts
omit it); an investigation-strategy sketch over the eight tools, including a standing instruction to retrieve peer
cases; the study’s conjunction rule for desire and availability; a description of the EMA-derived composite used
by the reflection step; and the structured JSON output schema covering binary targets, three continuous scores,
a reasoning trace, and a confidence value between 0 and 1, where 0 means not at all confident and 1 means
entirely confident, with no meaning attached to intermediate values, following standard verbalized-confidence
elicitation [35, 76]. Historical diary-derived outcomes can still enter no-current-diary prompts through memory
and retrieval.
Neutral-prompt variant.The variant used in the negativity-bias control (Section 5.8) differs from the standard
multimodal prompt in exactly two passages: “look for behavioral evidence that confirms or contradicts what the
diary suggests . . . Discrepancies are informative” becomes “consider cross-modal patterns: how does their behavior
relate to what they wrote?”, and “check if today’s behavior is unusual for this person” becomes “characterize how
today’s behavior compares to this person’s typical patterns. ” The public release adopts the neutral phrasing; the
reported metrics changed by less than .01 in this comparison.
Reflection prompt.After each prediction, a lightweight model call produces a 1–2 sentence lesson for the
session memory. The prompt provides the investigation summary, the prediction, and an EMA-derived binary
composite of regulation desire and availability; it does not provide the two component labels separately or the
affect scores. The accumulated reflection document is passed in full at subsequent entries and grows to roughly
50K characters per user.
Proc. ACM Interact. Mob. Wearable Ubiquitous Technol., Vol. 0, No. 0, Article 0. Publication date: September 2026.

PULSE: Agentic Investigation with Passive Sensing for Proactive Affective Intervention in Cancer Survivorship•0:25
Table 6. Per-target and aggregate performance across systems. Balanced accuracy for the four focus targets and their mean.
Reference baselines are included for context; the main comparative claim comes from the within-study 2×2 comparison.
System Input ER_desire INT_availability PA_State NA_State Mean BA
Reference baselines
Random Forest Sensing .501 .496 .520 .501 .505
XGBoost Sensing .493 .508 .525 .512 .510
Combined RF Sensing + diary .574 .542 .666 .596 .595
MiniLM Sensing + diary .681 .603 .693 .679 .664
LLM systems
CALLM Diary text .629 .545 .534 .641 .587
Struct-Sense Sensing .507 .542 .502 .510 .515
Auto-Sense Sensing .651 .713 .595 .591 .637
Struct-Multi Sensing + diary .655 .552 .530 .666 .601
Auto-Multi Sensing + diary .743 .722 .720 .716 .725
We document the prompt structure here. Complete prompts and the agentic system code will be released
publicly upon publication.
B Supplementary Results and Robustness Analyses
This appendix provides the expanded results supporting the main comparisons. Tables 6–8 report system-level
performance, the observed differences associated with providing the current diary, and across-user dispersion,
respectively. The remaining sections present the matched-call control, session-memory ablation, cold-start
analysis, negativity-bias control, reference baselines, temporal-boundary implementation, and evaluation-sample
representativeness analysis.
Table 7. Observed difference between multimodal and no-current-diary agentic conditions (Auto-Multi minus Auto-Sense).
Both conditions may access historical self-report outcomes.
Target Auto-Sense Auto-MultiΔ
PA_State .595 .720 +.125
NA_State .591 .716 +.125
ER_desire .651 .743 +.092
INT_availability .713 .722 +.010
Mean BA .637 .725 +.088
Proc. ACM Interact. Mob. Wearable Ubiquitous Technol., Vol. 0, No. 0, Article 0. Publication date: September 2026.

0:26•Zhiyuan Wang, Subigya Nepal, Ariful Islam, Indrajeet Ghosh, Xinyu Chen, Katharine E. Daniel, Laura E. Barnes, and Philip Chow
Table 8. Auto-Multi per-user balanced accuracy across all 50 evaluation users.
Target Mean SD𝑛users
PA_State .682 .095 50
NA_State .704 .093 50
ER_desire .698 .091 50
INT_availability .603 .116 50
B.1 Matched-Call Sensitivity Analysis: Per-Target Results
All control analyses use Claude Sonnet 4.6. Table 9 gives the matched-call results per target, and Figure 4
shows how the observed difference changes as 𝑘 increases. Both arms are independent runs; per-target values
differ slightly from Table 4 under nondeterministic decoding. The analysis matches call count only; it does not
match tokens, latency, or the information available through tools.
Table 9. Matched-call sensitivity analysis: observed difference ( ΔBA, Auto-Multi minus Struct-Multi with 𝑘-sample majority
voting).
Target𝑘=1𝑘=3𝑘=5𝑘=7
PA_State+.194+.190+.190+.189
NA_State+.078+.080+.082+.076
ER_desire+.093+.096+.098+.092
INT_availability+.158+.152+.148+.146
Mean+.131+.129+.129+.126
1 3 5 7
Structured self-consistency samples k (majority vote)
0.00
0.05
0.10
0.15
0.20¢BA (Auto-Multi ¡ Struct-Multi@k)
agentic mean
(6.2 calls)PA_State
NA_State
ER_desire
INT_avail
Mean (4 targets)
Fig. 4. Matched-call sensitivity analysis. Agentic advantage ( ΔBA, Auto-Multi minus Struct-Multi with 𝑘-sample majority
voting) as a function of the structured system’s inference budget. The dashed line marks the agentic system’s mean number
of LLM calls (6.2).
Proc. ACM Interact. Mob. Wearable Ubiquitous Technol., Vol. 0, No. 0, Article 0. Publication date: September 2026.

PULSE: Agentic Investigation with Passive Sensing for Proactive Affective Intervention in Cancer Survivorship•0:27
B.2 Session Memory: Per-Target Contribution and Accumulation
Removing the per-entry reflection document while retaining the initial memory and historical-outcome tools
reduces ER_desire BA by approximately .025. The other targets do not show a consistent pattern. Figure 5 shows
how the ER_desire difference varies with entry position.
1–10 11–25 26–45 46+
Entry position (accumulated receptivity feedback)
−0.01
0.00
0.01
0.02
0.03
0.04
0.05
Memory benefit on ER_desire  (¢BA)
-0.002
+0.012
+0.024
+0.041
Fig. 5. ER_desire difference ( ΔBA, with reflection document minus without) by entry position. The difference grows from
near zero in the first ten entries to+.041beyond entry 45.
B.3 Cold-Start Performance
Relative to entries 41+, pooled four-target BA is−.029over entries 1–10 and−.020over entries 11–20. A similar
difference appears with the reflection document ablated (−.043in the earliest bin). Entry position also tracks
accumulated history and sensing coverage.
B.4 Negativity-Bias Analyses
Across all evaluation investigations, the system predicts elevated NA on 30.0% of entries (ground-truth base
rate∼32%), with an NA false-positive rate of 16.9%. Universal tools show no elevated co-occurrence with negative
predictions (lift 1.0), whereas several optional drill-down tools co-occur more often ( query_raw_events 2.0,
query_sensing 1.6, get_receptivity_history 1.4). This pattern may reflect follow-up after an initial negative
cue; co-occurrence alone does not establish direction. In the neutral-prompt condition (Appendix A), the negative-
prediction rate (.304 vs. .300), false-positive rate (.170 vs. .169), and balanced accuracy (Δ<. 01) remain nearly
unchanged.
B.5 Simple Availability Baseline and Lightweight-Model Comparison
The simple availability baselines use logistic regression trained on the remaining 349 participants and evaluated
on the same 50-user set: time-of-day features alone (sine/cosine hour, weekend) give BA .485, while adding
pre-EMA-hour motion-state minutes gives BA .540. Pre-EMA motion coverage is missing for 21% of entries and
is handled with a missingness flag. MiniLM+LR, trained on roughly 16,000 labeled entries from the same 349
participants, trails Auto-Multi by+.027(PA),+.037(NA),+.062(ER_desire), and+.119(INT_availability).
B.6 Temporal-Boundary Enforcement
The current EMA timestamp is a hard cutoff in deterministic data-access code: sensing records, historical
outcomes, memory, retrieval results, and structured summaries are restricted to information available before that
cutoff.
Proc. ACM Interact. Mob. Wearable Ubiquitous Technol., Vol. 0, No. 0, Article 0. Publication date: September 2026.

0:28•Zhiyuan Wang, Subigya Nepal, Ariful Islam, Indrajeet Ghosh, Xinyu Chen, Katharine E. Daniel, Laura E. Barnes, and Philip Chow
B.7 Representativeness of the Evaluation Sample
Table 10 compares the 50-user evaluation sample with the remaining 349 eligible BUCS participants. The NA_State
base rate and mean NA differ with small effect sizes; platform mix also differs.
Table 10. Representativeness of the 50 test users versus the remaining 349 BUCS participants. Mann-Whitney U tests for
continuous measures; chi-square for categorical. Effect sizes reported as𝑟(rank-biserial correlation).
Measure Test Rest𝑝 𝑟
(𝑁=50) (𝑁=349)
PA_State base rate 0.545 0.561 .101 0.14
NA_State base rate 0.317 0.362 .028* 0.19
ER_desire base rate 0.350 0.385 .256 0.10
INT_availability base rate 0.643 0.593 .295 0.09
Mean PA 17.86 17.27 .527 0.06
Mean NA 3.23 4.38 .024* 0.20
Mean ER_desire 2.32 2.71 .255 0.10
Platform (% Android) 36% 25% .027* –
CV group distribution – – .292 –
*𝑝<.05. Effect sizes for significant differences are small (𝑟≤0.20).
C Case Studies
C.1 Example: Structured vs. Agentic on the Same Entry.
The following constructed example illustrates the interface difference; it is not an evaluation trace. Consider a
diary entry reading: “Feeling tired but trying to stay positive after my appointment. ” A structured agent would
receive a pre-formatted daily summary, while an agentic agent could request additional baseline and retrieval
results.
An illustrative agentic sequence is:
(1) Reads the diary and notes the tension between tiredness and positive coping.
(2) Callsget_daily_summaryand observes the day’s overall patterns.
(3) Notices low walking minutes and calls compare_to_baseline on walking, discovering it is 1.8 standard
deviations below this user’s personal mean.
(4) Calls get_behavioral_timeline and observes a gap in activity during the morning hours, consistent with
a medical appointment.
(5) Calls query_sensing on screen usage and finds a prolonged phone session during the morning gap,
consistent with time spent waiting.
(6) Calls find_similar_days; in this illustration, suppose it retrieves three past days with low mobility and
medical context, when the user’s affect was lower than the diary language alone suggested.
(7) Calls find_peer_cases with the diary text; suppose the returned cases pair similar “trying to stay positive”
language with moderate-to-low positive affect.
(8) Synthesizes the potentially conflicting cues: the diary conveys positive coping, while the behavioral and
retrieved context suggests that positive affect may still be below the user’s personal mean.
This example shows how interactive queries could expose explicit baseline and retrieval anchors. The structured
condition receives some related context in preassembled form but cannot choose or iteratively refine queries.
Proc. ACM Interact. Mob. Wearable Ubiquitous Technol., Vol. 0, No. 0, Article 0. Publication date: September 2026.

PULSE: Agentic Investigation with Passive Sensing for Proactive Affective Intervention in Cancer Survivorship•0:29
Because this is a constructed illustration, it is not evidence that these steps caused the observed performance
difference.
C.2 Selected Rationale: Personal and Peer Outcome History.
The following trace shows a prediction in which the model’s stated rationale places personal history above peer
outcomes. It illustrates how the model uses the available context rather than isolating the contribution of session
memory.
Participant 089 had a positive EMA-derived desire-and-availability composite on 6% of 39 earlier entries. On
one December entry, the diary reads:“Funeral of close friend today. Worried about mother’s declining health. ”The
following five steps summarize the model’s rationale, not verified psychological facts:
(1) Diary analysis.The agent identifies two compounding stressors—grief and caregiving worry—and forms
an initial hypothesis: elevated negative affect and likely elevated ER desire.
(2) Behavioral overview. get_behavioral_timeline and get_daily_summary return a stationary interval
and 2 minutes of screen use by mid-morning. The model interprets these values as possible withdrawal.
(3) Baseline comparison. compare_to_baseline reports 2 minutes of screen use against a typical value
of roughly 14 minutes per hour. The model labels this as disengagement; the tool itself only returns the
comparison.
(4) Peer outcomes. find_peer_cases with “funeral friend” returns grief-related diary cases, many with
elevated ER desire labels. The model treats these labels as evidence favoring elevated desire.
(5) Memory-based override.The injected memory document summarizes multiple low-composite entries
and characterizes a recurring coping pattern. The model uses that summary to predict low ER desire.
This selected entry matches all four binary labels and shows how historical outcomes appear in model context;
the rationale itself is not a mechanism test.
C.3 Selected Rationale: Two Historical-Outcome Channels.
This selected case illustrates two historical information channels available to the model.
Participant 258’s profile records high trait negative affect and moderate depression. On an evening EMA, the
diary reads:“Tired and a bit frazzled not sure why. ”The model’s rationale cites two types of evidence:
Signal 1: Same-user labeled history.Three labeled entries are cited in the rationale. The model groups diary
text as internally or externally focused and associates those groups with the EMA-derived composite. It also
receives 35.7 km of travel (𝑧=+ 1.79relative to the tool’s baseline). These are model-generated interpretations
from a very small sample, not verified coping or receptivity patterns.
Signal 2: Peer outcomes. find_peer_cases returns 15 diary cases containing similar “tired” or “frazzled”
language and their affect and ER labels. The model cites the retrieved label distribution and participant profile
when producing its prediction. This example does not test the effect of retrieval.
Proc. ACM Interact. Mob. Wearable Ubiquitous Technol., Vol. 0, No. 0, Article 0. Publication date: September 2026.

0:30•Zhiyuan Wang, Subigya Nepal, Ariful Islam, Indrajeet Ghosh, Xinyu Chen, Katharine E. Daniel, Laura E. Barnes, and Philip Chow
D Participant Demographics
Table 11. Demographics of the 50 evaluation participants (BUCS baseline survey).
Characteristic Value
Age, mean (SD), range 53.5 (10.9), 30–77
Gender 45 female (90%), 4 male (8%), 1 other (2%)
Race 47 White (94%); 1 Black; 1 American Indian/Alaska Native; 1 other
Ethnicity 1 Hispanic (2%); 1 missing
Cancer type 28 breast (56%); 6 other; 3 melanoma; 3 endometrial; 2 prostate;
2 lung/bronchus; 1 each colorectal, bladder, kidney, pancreatic,
leukemia, non-Hodgkin lymphoma
Cancer stage 10 stage I; 4 stage II; 5 stage III; 11 stage IV; 8 in-situ/0; 12 N/A
Education (years), median (range) 16 (12–30)
Marital status 33 married (66%); 8 divorced; 7 single; 2 widowed
Proc. ACM Interact. Mob. Wearable Ubiquitous Technol., Vol. 0, No. 0, Article 0. Publication date: September 2026.
