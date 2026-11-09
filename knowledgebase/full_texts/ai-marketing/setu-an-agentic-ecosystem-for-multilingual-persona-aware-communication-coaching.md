---
title: 'SETU: An Agentic Ecosystem for Multilingual, Persona-Aware Communication Coaching'
url: https://arxiv.org/abs/2608.27524
category: ai-marketing
subcategory: empirical
date: 2026-08
venue: ''
authors:
- Jonnalagadda Maruthi Tejas
- Uponika Barman Roy
- Tilottama Goswami
- Samir Goswami
- Mousita Dhar
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.27524
pages: 6
chars: 27452
fetched_at: '2026-11-08T13:31:24+00:00'
kb_version: 1
---

# SETU: An Agentic Ecosystem for Multilingual, Persona-Aware Communication Coaching

SETU: An Agentic Ecosystem for Multilingual,
Persona-Aware Communication Coaching
Jonnalagadda Maruthi Tejas 1 , Uponika Barman Roy 2, Tilottama Goswami 3 , Samir Goswami 1, Mousita Dhar 1
1Quanta People Solutions Pvt. Ltd., Hyderabad, India 2Panorama AI Solutions, London, Canada
3University College of Engineering, Osmania University, Hyderabad, India
jmtejas.work@gmail.com, uponika@panoramaai.org, goswami.tilottama@gmail.com
samirgoswami@tminetwork.com, mousitad@quantapeople.com
Abstract—Corporate training teams need scalable and explain-
able tools to improve workforce communication in multilingual
settings. Existing systems often score text, audio, or video in iso-
lation, or produce black-box outputs that are difficult to audit for
coaching use. This paper presents SETU, an agentic ecosystem for
corporate communication coachingaimed atrecruiters, frontline
sales professionals and training unitswho prepare for audience-
specific conversations. SETU is designed for two scoped scenarios:
(i) recruiter-candidate eligibility-and-interest calls with persona
context and (ii) sales pitches with target-audience adaptation;
owing to limited evaluation resources, this paper reports results
on scenario (ii) only. The ecosystem decomposes analysis into
specialized video, audio–speech, text–relevance, scoring, notifi-
cation and reporting agents coordinated through trust-aware
orchestration. It generates modality-attributed coaching reports
for formative training, with human reviewers retaining final
judgment. The name SETU (“bridge” in several Indic languages)
reflects the goal of bridging communication gaps across regional
languages and audience expectations.
Index Terms—multimodal AI, agentic AI, communication
coaching, multilingual speech, persona-based analysis
I. INTRODUCTION
Professional communication in high-stakes workplace set-
tings is a multimodal problem. Trainees are evaluated through
what they say, how clearly they say it and how well they
adapt to a specific audience. This challenge appears in recruit-
ment calls, sales conversations and client-facing presentations,
where the same message must be tuned to listener role, intent
and context.
In multilingual Indian workplace settings, trainees may
speak in English, Hindi, Telugu, or code-mixed forms such
as English–Bengali. Existing coaching tools often provide
generic textual feedback or single-modality scoring. They
rarely combine visual, acoustic, linguistic and persona-aware
reasoning in one auditable pipeline. Users therefore receive
incomplete guidance on how to improve for a particular
audience or task.
Recent progress in large language models (LLMs), speech
processing and multimodal learning has improved commu-
nication support systems. PresentCoach [1] uses dual-agent
presentation coaching, while PersoPilot [2] shows the value
of persona-aware personalization. However, most prior sys-
tems are monolithic. They do not decompose coaching into
specialized, replaceable and explainable units. This limits
debugging, modality attribution and governance in enterprise
training workflows.
This paper presents SETU, an agentic ecosystem for mul-
tilingual interviews and persona-aware communication coach-
ing. SETU is designed for corporate training and assessment
platforms that require transparent evaluation of spoken com-
munication. Beyond recruitment, the ecosystem can support
sales profiling, needs gathering and product mapping. In
this study, evaluation is scoped to the sales-pitch scenario;
recruiter–candidate interactions are supported by design but
are not evaluated here owing to limited resources.
Anagentic ecosystemis adopted rather than a single end-to-
end model for four reasons. First, each modality has different
failure modes and update cycles. Second, agent boundaries
make it clear which component produced each score. Third,
one agent can be replaced without retraining the full system.
Fourth, trust-weighted orchestration allows unreliable signals
(e.g., noisy audio) to be down-weighted during aggregation.
The work has the following four contributions:
1) A multimodal agentic ecosystem that decomposes com-
munication coaching into video, audio–speech, text–
relevance, scoring, notification and reporting agents.
2) A persona-aware analysis layer that adapts feedback
to performer role, target audience, task prompt and
multilingual language conditions.
3) A trust-aware orchestration formulation for routing sub-
tasks and aggregating modality evidence into structured
coaching reports.
4) A human-in-the-loop design that positions SETU as a
formative coaching assistant rather than an autonomous
hiring or sales decision system.
The rest of this paper is organized as follows. Section II
reviews related work. Section III describes the SETU agentic
ecosystem and sales pitch mapping methodology. Section IV
presents the experimental case study and results. Sections V
and VI discuss limitations and future work. Section VII
concludes the paper.
II. RELATEDWORK
AI-supported sales and presentation coaching draws from
presentation simulation, multimodal assessment, multilingual
arXiv:2608.27524v1  [cs.AI]  27 Aug 2026

speech processing, persona-aware interaction and responsible
AI for high-stakes evaluation.
PresentCoach [1] supports presentation practice through
exemplars and interactive feedback. It is not designed for
multilingual sales pitch mapping with buyer-persona relevance
scoring. PersoPilot [2] improves persona-aware response gen-
eration, but it does not jointly analyze posture, prosody and
code-mixed pitch delivery in a modular coaching workflow.
Agentic multimodal advertising frameworks [3] show persona-
targeted reasoning, yet they target campaign outcomes rather
than formative sales coaching. Low-resource language re-
search [4] highlights agentic opportunities for regional lan-
guages, but does not provide a deployable multimodal sales
coaching stack. Work on code-switching automatic speech
recognition (ASR) for Indic languages characterizes the recog-
nition challenges that constrain multilingual coaching systems
[5]–[7].
LLM-as-judge surveys [8], [9] show that automated scoring
is scalable but sensitive to prompt design, bias and calibration.
Fairness studies in AI-driven assessment [10]–[12] warn that
automated evaluation systems may amplify accent, language
and appearance bias. These works motivate transparent rubrics
and human oversight, but they do not by themselves provide
a multimodal sales coaching pipeline.
Despite these advances, three gaps remain in the literature.
First, many systems focus on generic presentation coach-
ing without explicit sales-task and buyer-persona mapping.
Second, persona-aware adaptation is often separated from
multimodal behavioral analysis of spoken pitches. Third, mul-
tilingual and code-mixed sales speech is rarely treated as a
first-class coaching dimension in workforce training systems.
The proposed SETU ecosystem addresses these limitations
by integrating multimodal evidence, buyer-persona context,
multilingual support, trust-aware orchestration and human
oversight in one sales coaching pipeline.
SETU differs from these systems by coupling specialized
agents, explainable scorecards and enterprise sales-training
governance in a single agentic ecosystem.
III. METHODOLOGY
Building on the identified research gaps, this section
presents the SETU agentic ecosystem for sales pitch map-
ping. It introduces the high-level architecture, mathematical
formulation, pitch data design and agent workflow and uses
a running payroll-SaaS pitch case study to show how the
components connect in practice.
A. Running Sales Pitch Case Study Setup
One representative sales pitch session is used to illustrate
the pipeline end-to-end:
•Scenario:First-meeting product pitch to a prospective
small and medium-sized enterprise (SME) buyer.
•Performer:Sales Performer pitching a cloud human
resources (HR) and payroll software-as-a-service (SaaS)
platform.
•Target persona:CEO of an SME company (focused
on return on investment (ROI), time-constrained decision
maker).
•Pitch prompt:“In 90 seconds, convince the CEO to
adopt your payroll automation platform. Cover the SME
pain point, product value, ROI impact and a clear next
step.”
•Language:English–Bengali code-mixed speech.
•Input:78-second webcam pitch recording.
In the weak version of this pitch (Case A), the performer opens
with company background, lists product modules and code-
switches into Bengali without linking benefits to SME cost
savings. In the strong version (Case B), the performer opens
with payroll-compliance pain, cites a concrete ROI example
and closes with a demo call-to-action. This pitch case is
revisited in Subsections III-B to III-J.
B. Proposed High-Level Agentic Framework
Fig. 1 shows the SETU multimodal agentic pipeline. The
system uses a dual-stream design: Step 1A routes the synchro-
nized pitch recording to the speech, video and audio agents,
while Step 1B maps buyer persona and pitch-prompt con-
straints through the relevance mapping agent. Step 2 performs
semantic analysis and multimodal alignment. Step 3 converts
derived metrics into fused scores through the insight and
evaluation core. The pipeline then delivers live pitch alerts and
a coaching scorecard under human-in-the-loop governance.
In the pitch case study, the context agent injects CEO-
of-SME expectations: concise delivery, business impact and
measurable ROI. The speech agent transcribes the spoken
pitch, including code-mixed segments. The relevance agent
checks whether the pitch follows a persuasive structure (pain
point→solution→ROI→close), not merely product feature
listing.
C. Mathematical Representation
The multimodal agentic ecosystem is formulated as:
M= (A, T, S, E, O, C,Mem).(1)
Equation (1) defines the tuple form of SETU.Ais the agent
set,Tis the global coaching task,Sis state,Eis input
environment,Ois orchestrator,Cis communication among
agents andMemis memory.
The core modality agents are instantiated as:
Acore ={v, a, t},(2)
wherevis the video agent,ais the audio/speech agent
andtis the text/relevance agent group. Extended operational
agents (sync, context, insight, scoring, notification, report) are
included in the full setA.
The global task is:
T={t 1, t2, t3, t4, t5, t6}.(3)
In (3),t 1 synchronizes streams,t 2 extracts visual cues,t 3
performs speech and acoustic analysis,t 4 evaluates text quality

Fig. 1. SETU multimodal agentic pipeline for sales pitch mapping. The ecosystem uses dual-stream perceptual analysis (Step 1A) and contextual constraint
mapping (Step 1B), followed by semantic fusion (Step 2), scoring and evaluation (Step 3) and delivery with human coach review.
and language profile,t 5 computes persona-aware sales rele-
vance andt 6 generates the coaching report.
The orchestration assignment is
O(T, S, A,Mem)→ {(xi, tj)},(4)
wherex i ∈Ais the selected agent for subtaskt j. Equation (4)
is the routing core of the ecosystem: each subtask is mapped
to the most capable agent instead of sending all inputs to one
monolithic model.
For example,
O(T) ={(sync, t1),(v, t2),(a, t3),
(t, t4),(t, t5),(report, t6)}. (5)
Equation (5) means stream sync handles alignment,vhandles
visual behavior,ahandles speech and acoustics,thandles lin-
guistic and relevance reasoning and the report agent compiles
outputs. In the pitch case study, relevance is assigned tot
because it must judge whether the spoken pitch addresses the
CEO prompt using both transcript evidence and buyer-persona
context.
Each agent is represented as
xi = (πi, ϕi, ψi),(6)
whereϕ i is feature extraction,π i is decision policy and
ψi is structured output generation. Equation (6) separates
perception, reasoning and structured output generation for
every agent.
State evolution is
s0 =Raw Input,(7)
s1 =f(s 0, sync),(8)
s2 =f(s 1,{v, a}),(9)
s3 =f(s 2,{a, t}),(10)
s4 =f(s 3, report).(11)
Equations (7)–(11) show progressive enrichment of context.
For the pitch case study,s 2 adds posture and vocal-delivery
features from the recorded pitch;s 3 adds transcript text and
pitch-relevance evidence;s 4 is the final pitch coaching report.
Trust of agentx i is
Trust(xi) =αAcc i +βCons i +γ Ri,(12)
whereAcc i is modality accuracy,Cons i is score consistency
across repeated windows andR i is runtime reliability (latency
failures, API dropout). Equation (12) is applied toagent
outputs, not to the sales trainee. In implementation, trust
weights modality contributions during aggregation, e.g., down-
weighting audio evidence when the signal-to-noise ratio (SNR)
is poor.
The orchestration design criterion is
max
X
i
Ri −λC coord,(13)
whereC coord is coordination cost (extra agent calls and delay).
Equation (13) expresses the trade-off between output reliability
and coordination cost.

D. Sales Pitch Mapping Design and Data Acquisition
The sales pitch mapping design is a structured training
matrix for spoken product-pitch practice. Each entry defines
what product to pitch,to which buyer personaandwhich pitch
objectivemust be achieved within the time limit.
The design contains four layers:
1)Performer role:Sales Performer delivering the pitch.
2)Target buyer persona:CEO of SME, dual-income, no-
kids (DINK) professional in an information technology
(IT) firm, Retired Government Officer, School Teacher,
or Mid-level Manager.
3)Pitch stage:Lead Generation, Connecting, Profiling,
Needs Gathering, or Product Mapping.
4)Pitch prompt:A timed instruction such as “Pitch the
payroll SaaS platform to an SME CEO in 90 seconds
with ROI and next-step close.”
Each matrix cell also specifies language condition and
exemplar quality. Language conditions are English, Hindi,
Telugu, English–Hindi, English–Bengali and English–Telugu.
Exemplar bands are Good, Fair and Poor. Good/Fair/Poor
pitch clips are used as mirroring references for personalized
feedback, not as automatic pass/fail labels.
For pitch data collection, video quality is controlled at
720p webcam capture with single-speaker framing. Audio is
recorded in typical office noise conditions. Pitch duration is
45–120 seconds per clip. Sales coaches mark each pitch as
Good, Fair, or Poor based on pitch-specific rubrics: opening
hook, buyer relevance, evidence/ROI, delivery quality and
closing call-to-action.
In the running pitch example, the performer must convince
an SME CEO that payroll automation reduces compliance risk
and operating cost. The pitch should be persuasive and buyer-
specific, not a generic product brochure delivered aloud.
E. Video Agent
The video agent (v) extracts posture stability, eye-contact
approximation, facial expressiveness and head movement us-
ing MediaPipe Holistic landmarks. Sub-scores are temporally
smoothed and combined into a visual performance score.
In Case A, the performer looked away from the camera
while stating pricing and lost upright posture during the ROI
segment. This produced a visual score of 3.8/10. The report
noted that weak non-verbal delivery reduced perceived pitch
confidence, independent of language choice.
F . Speech and Audio Agents
The audio/speech agent (a) performs two functions. First, it
transcribes multilingual and code-mixed speech using the Sar-
vam speech-to-text (STT) model (saaras:v3,codemix).
Second, it computes acoustic features with Librosa: root-mean-
square (RMS) energy, pitch variation, silence ratio, SNR,
words-per-minute (WPM) and filler density.
Language detection combines API confidence, script-based
fallback and parallel language probes. This is important for
Indian code-mixed sales speech where script cues and audio
cues may disagree.
In Case A, the pitch transcript contained frequent “um/uh”
pauses before key value statements and Bengali code-
switching appeared during the ROI explanation. English and
Bengali were detected. Filler density was high and SNR was
moderate, yielding audio score 4.1/10 with a coaching alert to
slow down and emphasize benefit statements clearly.
G. Text Agent
The text agent (t) evaluates grammar, fluency, profession-
alism and semantic completeness using rubric-constrained
LLM scoring. It compares the transcript against the sales-task
prompt and buyer persona context. A performer is scored for
delivery quality and for addressing the correct sales commu-
nication objective.
Code-switching is not penalized by default. The agent flags
excessive language switching only when more than three
languages appear in one session (English plus up to two
regional languages is the coaching target).
In Case A, the performer said: “Our company was founded
in 2018... we have attendance, payroll, leave modules...” with-
out converting features into buyer outcomes. Text score was
4.6/10, with feedback on fragmented pitch flow and missing
value proposition language.
H. Relevance Agent
The relevance agent evaluates whether the pitch satisfies the
persona-task prompt. It enriches the prompt with performer
and target buyer descriptions before LLM rubric scoring on a
0–50 scale, normalized to 0–10.
In Case A, the pitch did not answer the CEO prompt. It
omitted payroll-compliance pain, offered no ROI figure and
ended without a next-step ask. Relevance was partial (5.4/10),
with deductions for missing pain point, missing ROI evidence
and missing close. By contrast, Case B opened with “Manual
payroll errors cost SMEs time and penalties,” cited “up to 30%
admin-time reduction,” and closed with “Can we schedule a
15-minute demo Thursday?”
I. Orchestrator
The orchestrator realizes the routing and trust-weighted ag-
gregation of Equations (4)–(12) in a LangGraph workflow with
sharedAgentState. It routes subtasks, stores intermediate
outputs and applies trust-weighted aggregation when modality
reliability is unequal.
For the case study, audio trust was reduced due to noise,
while text/relevance trust remained stable. This prevented
noisy acoustics from dominating the final score.
J. Overall Coaching Report and Recommendations
The session report includes visual, audio, text, relevance,
language profile, overall score and recommendations. Each
recommendation is linked to modality evidence and deduction
traces.
For Case A, the pitch coaching report recommended a four-
part rewrite: (i) open with SME payroll pain, (ii) present two
buyer-relevant benefits with one ROI metric, (iii) maintain eye
contact during price/value statements and (iv) close with a

concrete demo call-to-action. It also advised keeping English–
Bengali switching only where it improves rapport, not during
core value delivery.
K. Human in the Loop
SETU is a coaching assistant, not an autonomous decision
engine. Human sales coaches validate reports, inspect modality
evidence, adjust rubrics and approve final feedback before
trainee delivery.
In enterprise use, this human validation step supports au-
ditability and fairness governance.
IV. EXPERIMENTS ANDPERFORMANCEANALYSIS
After describing the SETU agentic ecosystem, this section
evaluates it through a sales pitch mapping case study. It reports
the pitch evaluation setup, quantitative results, comparative
baselines and coaching-time impact on sales trainers.
A. Case Study Scope and Objectives
SETU is evaluated through a pilot case study with a
corporate sales training partner. The evaluation is scoped to
sales pitch mapping only. Every session is a timed product
pitch: a sales performer presents a solution to a defined buyer
persona within 45–120 seconds.
Pitch stages include Lead Generation, Connecting, Profil-
ing, Needs Gathering and Product Mapping. However, each
recording is evaluated as a persuasive pitch, not as a free-form
conversation. The core question is: “Did the spoken pitch fit
the buyer persona and achieve the prompt objective?”
Objectives are to measure (i) pitch delivery scoring validity,
(ii) multilingual pitch handling quality, (iii) buyer-persona
pitch relevance, (iv) explainability of pitch feedback and (v)
coaching-time reduction for human sales trainers.
B. Dataset Characteristics
The pilot dataset contains 18 recorded sales pitch videos.
Each video captures one complete pitch attempt against a fixed
prompt:
•Products pitched:HR–payroll SaaS (8), EdTech learning
platform (5), insurance cross-sell plan (5).
•Target personas:CEO of SME (6), School Teacher (4),
Mid-level Manager (4), DINK in IT firm (2), Retired
Government Officer (2).
•Pitch stages:Lead Generation (4), Connecting (3), Pro-
filing (3), Needs Gathering (4), Product Mapping (4).
Pitch length is 45–120 seconds (mean 78 seconds, SD 19
seconds). Resolution is 720p webcam capture. Audio is mono
microphone input in office environments. Language distribu-
tion: English (4), Hindi (3), Telugu (2), English–Hindi (5),
English–Telugu (4). Coaches label each pitch as Good, Fair, or
Poor using pitch rubrics (hook, relevance, evidence, delivery,
close).
TABLE I
REPRESENTATIVE SALES PITCH MAPPING SCORES(0–10)
Pitch Session Vis. Aud. Text Rel.
Case A: Weak payroll
SaaS pitch to SME CEO
(English–Bengali)
3.8 4.1 4.6 5.4
Case B: Strong payroll
SaaS pitch to SME CEO
(English–Bengali)
7.6 7.3 7.8 8.1
Case C: EdTech pitch to
School Teacher (English)
6.9 6.5 7.2 8.4
C. Evaluation Protocol
Each video is processed by the SETU batch pipeline: audio
extraction, STT, language profiling, video analytics, acoustic
analytics, LLM rubric scoring and weighted aggregation. Live-
mode tests are run on a 6-session subset to measure alert
latency.
Baselines:
•B1:Text-only LLM feedback (transcript-only).
•B2:Non-agentic multimodal prompt (single-pass sum-
mary without agent-level traces).
D. Metrics
The evaluation reports modality sub-scores (0–10), overall
score, coach agreement (Spearmanρ), explainability rating
(coach 1–5), language macro-F1, end-to-end latency and
coaching-time reduction.
E. Representative Pitch Case Study Results
Table I shows three representative pitch sessions, including
the running methodology example (Case A).
Overall scores were 4.6 (Case A), 7.7 (Case B) and 7.4
(Case C) using batch weights0.20visual,0.25audio,0.20
text,0.35relevance.
Across all 18 sales sessions, SETU obtained a mean batch
latency of 38.6 s per clip, live alert refresh 2–4 s, coach
agreementρ= 0.78, explainability 4.3/5 and language macro-
F1 0.86.
F . Comparative Analysis
SETU outperformed B1 (ρ= 0.61, explainability 2.9/5)
and B2 (ρ= 0.69, explainability 3.4/5) on the same pilot set.
Buyer-persona-conditioned relevance improved agreement by
0.11 inρover non-persona prompting.
Coach review time was reduced from 22 to 13 minutes per
session (40.9% reduction) and the average number of practice
cycles needed to reach Fair/Good decreased from 4.1 to 2.6.
G. Case Study Insights
The sales pitch case study shows that multimodal agent
decomposition produces pitch feedback that coaches can act
on immediately. Buyer-persona context is especially important
for relevance scoring: the same product language can score
high for a School Teacher pitch but low for an SME CEO
pitch if ROI is missing. Code-mixed pitch delivery is feasible

to coach when ASR, script cues and confidence filtering are
combined. Human coach review remains necessary to validate
pitch judgments and avoid over-penalizing natural language
switching.
V. LIMITATIONS
Although the pilot case study provides initial evidence,
SETU has important boundaries that must be stated before
broader deployment. This section summarizes the main tech-
nical, data and governance constraints observed in the current
study.
SETU depends on video/audio quality, ASR accuracy,
prompt design and rubric fairness. Visual cues such as eye
contact may vary with culture, disability, camera angle and
lighting. The current pilot is small (18 sales videos) and
internal. Results should be validated on larger expert-labeled
benchmarks before deployment at scale.
VI. FUTUREWORK
Based on the case study findings and the limitations above,
this section outlines the next steps needed to strengthen SETU
for large-scale sales training use.
Future work will expand the sales dataset across more
buyer personas and task categories, add expert-labeled bench-
marks, improve low-resource language support, add longitu-
dinal coaching analytics and conduct fairness audits across
gender, accent, skin tone, disability and regional language
groups.
VII. CONCLUSION
This paper examined whether an agentic ecosystem can
provide explainable, persona-aware coaching for multilingual
sales pitches.
This paper presented SETU, an agentic ecosystem for multi-
lingual sales pitch mapping and persona-aware communication
coaching. By combining specialized agents, buyer-persona
context, trust-aware orchestration and human oversight, SETU
provides explainable and specific coaching for sales com-
munication training. Case-study evaluation on multilingual
sales pitch scenarios indicates improved coach agreement and
reduced pitch-coaching effort compared with text-only and
non-agentic baselines.
ACKNOWLEDGMENT
The authors thank Quanta People Solutions Pvt. Ltd. for
supporting this research work.
REFERENCES
[1] S. Chen, J. Zhou, X. Xu, X. Yang, L. Guo and Y .-C. Chen, “Pre-
sentCoach: Dual-Agent Presentation Coaching through Exemplars and
Interactive Feedback,” arXiv:2511.15253, 2025.
[2] S. Afzoon, A. Beheshti and U. Naseem, “PersoPilot: An Adaptive
AI-Copilot for Transparent Contextualized Persona Classification and
Personalized Response Generation,” arXiv:2602.04540, 2026.
[3] S. S. Srinivas, A. Das, S. Gupta and V . Runkana, “Agentic Multi-
modal AI for Hyper-Personalized B2B and B2C Advertising in Com-
petitive Markets: An AI-Driven Competitive Advertising Framework,”
arXiv:2504.00338, 2025.
[4] N. Kshetri, “From Challenges to Opportunities: Agentic Artificial Intel-
ligence for Low-Resource Languages,”IT Professional, IEEE Computer
Society, vol. 27, no. 3, pp. 12–20, May–Jun. 2025.
[5] A. Diwan, R. Vaideeswaran, S. Shah, A. Singh, S. Raghavan, S. Khare,
V . Unni, S. Vyas, A. Rajpuria, C. Yarra, A. Mittal, P. K. Ghosh, P. Jyothi,
K. Bali, V . Seshadri, S. Sitaram, S. Bharadwaj, J. Nanavati, R. Nanavati
and K. Sankaranarayanan, “Multilingual and Code-Switching ASR Chal-
lenges for Low Resource Indian Languages,” arXiv:2104.00235, 2021.
[6] H. S. Chadha, P. Shah, A. Dhuriya, N. Chhimwal, A. Gupta and V .
Raghavan, “Code Switched and Code Mixed Speech Recognition for
Indic Languages,” arXiv:2203.16578, 2022.
[7] H. Liu, X. Zhang, H. Zhang, L. P. Garcia-Perera, A. W. H. Khong, E.
S. Chng and S. Watanabe, “Aligning Speech to Languages to Enhance
Code-switching Speech Recognition,” arXiv:2403.05887, 2024.
[8] H. Li, Q. Dong, J. Chen, H. Su, Y . Zhou, Q. Ai, Z. Ye and Y . Liu,
“LLMs-as-Judges: A Comprehensive Survey on LLM-based Evaluation
Methods,” arXiv:2412.05579, 2024.
[9] J. Gu, X. Jiang, Z. Shi, H. Tan, X. Zhai, C. Xu, W. Li, Y . Shen, S. Ma,
H. Liu, S. Wang, K. Zhang, Z. Lin, L. Ni, W. Gao, Y . Wang and J. Guo,
“A Survey on LLM-as-a-Judge,” arXiv:2411.15594, 2024.
[10] D. F. Mujtaba and N. R. Mahapatra, “Fairness in AI-Driven Re-
cruitment: Challenges, Metrics, Methods and Future Directions,”
arXiv:2405.19699, 2024.
[11] D. F. Mujtaba and N. R. Mahapatra, “Behind the Screens: Uncovering
Bias in AI-Driven Video Interview Assessments Using Counterfactuals,”
arXiv:2505.12114, 2025.
[12] S. Biswas, J.-Y . Jung, A. Unnam, K. Yadav, S. Gupta and U. Gadi-
raju, “Hi. I’m Molly, Your Virtual Interviewer! Exploring the Impact
of Race and Gender in AI-powered Virtual Interview Experiences,”
arXiv:2408.14159, 2024.
