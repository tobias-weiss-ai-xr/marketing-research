---
title: 'ResidencyRL: Reinforcement Learning in Simulated Clinical Environments'
url: https://arxiv.org/abs/2608.07418
category: ai-marketing
subcategory: empirical
date: 2026-08
venue: ''
authors:
- Valentin Liévin
- Samuel Schmidgall
- Tim Strother
- Alex Bijamov
- Akshay Goel
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.07418
pages: 51
chars: 184240
fetched_at: '2026-11-08T13:32:30+00:00'
kb_version: 1
---

# ResidencyRL: Reinforcement Learning in Simulated Clinical Environments

2026-10-12
ResidencyRL: Reinforcement Learning in
Simulated Clinical Environments
Valentin Liévin1,*, Samuel Schmidgall1,*, Tim Strother1,*, Alex Bijamov1,*, Akshay Goel2, Anil Palepu2,
Chunjong Park1, Vahid Balazadeh1, Min Woo Sun1, Marius Guerard2, Justin Chen1, Dave Steiner1, Vikram
Dhillon3, Ibrahim Azar4, Akhil Mehta5, Nicholas Spetsieris3, Shilpan Shah3, Maen Abdelrahim3, Amit
Dahiya6, Yun Liu2, Katherine Chou2, Yossi Matias2, Avinatan Hassidim2, Dale R. Webster2, Quoc V. Le1, Raia
Hadsell1, Joelle Barral1, Carey Radebaugh1, Aleksandra Faust1, Shekoofeh Azizi1, Mike Schaekermann2,
Po-Hsuan Cameron Chen2, Tao Tu1,†, David Racz1,† and Lin Yang1,†
1Google DeepMind,2Google Research,3Department of Oncology, Houston Methodist Hospital, Houston, TX,4Trinity Health
Group, Oakland Campus, Pontiac, MI,5Stanford Oncology Partners,6Department of Hospital Medicine, St. Luke Hospital, Cedar
Rapids, IA,*Equal contribution,†Equal leadership
Inmedicaleducation, physiciansconvertacademicknowledgeintoclinicalexpertisethroughresidency:
years of training across thousands of encounters, with diverse sources of feedback and progressively
greater autonomy. Much of clinical reasoning relies on the patient encounter, a dialogue in which
a clinician elicits history, refines diagnostic hypotheses, and decides management under uncertainty.
While large language models (LLMs) excel on static medical benchmarks, methods to optimize the
full sequence of clinical decisions remain underdeveloped. We present ResidencyRL, a reinforcement
learning (RL) method for training clinical artificial intelligence (AI) agents through simulated multi-
turn clinical encounters (up to 60 dialogue turns and 8 tool calls per trajectory). ResidencyRL pairs the
policy agent with LLM simulators capable of complex, adversarial behaviors, training against a struc-
turedrewardalignedtodiagnosticaccuracy,managementquality,communication,documentation,and
safety. On held-out evaluations, the ResidencyRL agent improves diagnostic accuracy by 7.0% under
adversarial conditions (88.0% vs. 81.0%) and reduces missed red flag rates by 31%, demonstrating rig-
orous mitigation of premature closure. Blinded expert clinicians validated these gains, preferring the
trained agent in 87.6% of side-by-side comparisons. The procedural competencies transfer to unseen
benchmarks: the agent outperforms the base model across all six clinical axes of the AMIE multi-visit
benchmark, and shows consistent directional improvements on AgentClinic and CRAFT-MD. Our find-
ings demonstrate that sequential clinical decision-making can be effectively learned through multi-turn
RL in simulation, yielding robust, generalizable capabilities, paving the way towards clinical mastery.
Prospective validation with real-world workflows remains necessary to establish clinical utility.
1. Introduction
Medical training begins in textbooks, but clinical competence is forged through practice: years of
supervised clinical encounters, each conversation shaped by the patient’s fears, misconceptions, and
communicative limitations, transform that knowledge into competence (Barrows, 1993). A trainee
who scores perfectly on board examinations may still fail to detect a myocardial infarction when the
presentation is atypical, or miss a mental health crisis when the patient presents with insomnia. Real
patients are complex: they may present with vague complaints, resist recommendations, or conceal
medications (Kemp et al., 2020; Levy et al., 2018), and systemic barriers such as health literacy and
medical mistrust hinder effective communication (LaVeist et al., 2009; Paasche-Orlow et al., 2005).
Language models have achieved expert-level performance on academic benchmarks (Jin et al.,
2021; Liévin et al., 2024; Nori et al., 2023; Saab et al., 2024; Singhal et al., 2023, 2025). AMIE, a
research AI system for clinical conversations, has matched primary care physicians for diagnostic and
Corresponding author(s): {vlievin, schmidgall, taotu, dracz, linyan}@google.com
©2026 Google. All rights reserved
arXiv:2608.07418v2  [cs.AI]  9 Oct 2026

ResidencyRL: Reinforcement Learning in Simulated Clinical Environments
b. Simulation scenario packs
Behavioural
Neuroticism
Agreeableness
Extraversion
General
Intake
Adversarial
a. Scenario generation pipeline
Deduplication +
General telehealth (83%) History (15%) Adversarial (2%)
Modify
Accept
Reject
Specialization
Judge
Generation
and curation
TF-IDF
+
Gradient step
 Rewards
K episodes per scenario
Scenario
Age
Location
Ethnicity
Demographics
Sex DDXPlus
Differential
Diagnosis
Scenario
proposer
Seed sampling
Scenario
 Scenario
 Scenario
+
Agent
Patient
 API
Converses
with..
Documents
in..
c. Simulated environment
 d. Simulation episode (max. 68 actions + thinking)
Let’s think step
by step.
Hello, how can
I help you?
Any current
medication?
submit
differential()
terminate()
Submit
management()
Based on this
information …
Thinking
Talking
Tool call
e. Structured reward
Primary
Penalties
- Diagnosis: <likert>
- Management: <rubric>
- Intake: <rubric>
- Communication: <rubric>
- Length: <scalar>
Agent
Autorater
f. Agentic reinforcement learning (GRPO)
generation
g. RL training dynamics
h. Clinical performance evaluation
- Hallucinations: <scalar>
- Documentation: <rubric>
- Style: <rubric>
- Contraindications: <scalar>
- …
b. Scenario Packs
Behavioural
Neuroticism
Agreeableness
Extraversion
General
Intake
Adversarial
a. Scenario Generation Pipeline
Deduplication +
General telehealth (83%) Intake (15%) Adversarial (2%)
Modify
Accept
Reject
Specialization
Judge
Generation
and curation
TF-IDF
+
Gradient step
Rewards
K rollouts per scenario
Scenario
Age
Location
Ethnicity
Demographics
Sex DDXPlus
Differential
Diagnosis
Scenario
proposer
Seed sampling
Scenario
 Scenario
 Scenario
+
Agent
Patient
 API
Converses
with..
Documents
in..
c. Simulated Environment
 d. Simulation Rollout (mean: 55 agent steps)
Let’s think step
by step.
Hello, how can
I help you?
Any current
medication?
submit
differential()
terminate()
Submit
management()
Based on this
information …
Thinking
Talking
Tool call
e. Structured Reward
Primary
Penalties
- Diagnosis: <likert>
- Management: <rubric>
- Intake: <rubric>
- Communication: <rubric>
- Length: <scalar>
Agent
Autorater
f. Reinforcement Learning (GRPO)
generation
g. Training dynamics
h. Clinical performance evaluation
- Hallucinations: <scalar>
- Documentation: <rubric>
- Style: <rubric>
- Contraindications: <scalar>
- …
Figure 1|Training clinical AI agents through simulated multi-turn patient encounters. a, A
generative proposer-judge pipeline synthesizes and curates diverse clinical scenarios based on tar-
geted demographic and behavioral patient profiles.b, Curated scenarios are stratified into special-
ized training environments, including routine general telehealth, complex cases requiring in-depth
history-taking, and adversarial safety challenges, each targeting distinct clinical competencies.c,
The simulated environment exposes an LLM-driven patient simulator and a structured API allowing
the agent to document the encounter (e.g., diagnosis, management plan).d, Multi-turn simulation
rollouts capture the agent’s sequential clinical reasoning, natural language dialogue, and tool utiliza-
tion, scaling up to 60 dialogue turns and 8 tool calls.e, An LLM autorater processes the encounter
transcript and tool calls, yielding a structured reward, heavily weighted by clinical accuracy rubrics
and critical safety flags.f, The policy agent is optimized via Group Relative Policy Optimization
(GRPO), leveraging reward signals from parallel rollouts.g, Optimizing diagnostic, management,
intake, communication, documentation and style during training (normalized[0,1]).h, Side-by-
side evaluation by expert human clinicians (𝑁=97) shows that the ResidencyRL-trained agent is
consistently preferred over the base model across all evaluated clinical dimensions.
2

ResidencyRL: Reinforcement Learning in Simulated Clinical Environments
management reasoning in human-simulated settings (Liévin et al., 2026; Saab et al., 2026; Tu et al.,
2025;Vedadietal.,2025),andhasdemonstratedconversationalsafetyandpromisingclinicalreason-
ing performance in prospective clinical research settings with real patient encounters (Brodeur et al.,
2026). Yet clinical reasoning under uncertainty remains hard for humans and AI alike: premature
closure is the most common source of diagnostic error in clinical practice (Croskerry, 2002; Graber
et al., 2005) and is equally prevalent in AI systems (Schmidgall et al., 2024; Wang et al., 2025),
which are further vulnerable to adversarial manipulation (Balazadeh et al., 2025). This is not a fail-
ure of medical knowledge, but of clinical process—and the process can be optimized. Reinforcement
learning has proven effective for long-horizon sequential decision-making, from games (Mnih et al.,
2015; Silver et al., 2017) and real-time strategy (Vinyals et al., 2019) to algorithm discovery (Fawzi
et al., 2022), web navigation (Gur et al., 2021), chip placement (Mirhoseini et al., 2021), and robot
control (Bellemare et al., 2020; Chiang et al., 2019), even when training in imperfect simulations
(Chiang et al., 2019; Tobin et al., 2017). Concurrent work applied multi-turn RL to clinical dialogue
(Feng et al., 2026; Lai et al., 2025; Qiu et al., 2025) over short horizons (≤12 turns) and with action
spaces limited to dialogue or isolated diagnostic actions. The Baichuan-M2/M3 series (Dou et al.,
2025, 2026) scales this recipe to a dynamic verifier system with LLM-generated clinical rubrics, but
optimizes fragments or fixed consultation stages rather than the complete encounter.
We introduce ResidencyRL, built on a simple premise: clinical mastery, for AI as for physicians,
is developed through practice. ResidencyRL is an online multi-turn RL method for training clinical
AI agents through dynamic, complete, simulated clinical encounters, scaling up to 60 conversational
turnsandeightadditionalstructuredenvironmentinteractions. 1 WetrainaGemini3.5Flash(Gemini
Team Google, 2026b) initialized agent to interact with an LLM-based patient simulator across a cur-
riculum of three environment types: (1) routine telehealth consultations, (2) targeted history-taking
scenarios designed to uncover hidden clinical information, and (3) adversarial safety cases to ensure
robustnessagainstchallengingpatientbehaviorsandmaliciousinputs. Trainingisguidedbyahierar-
chical rubric optimizing six clinical dimensions (diagnostic accuracy, management quality, screening
completeness, patient-centered communication, clinical documentation, and conversational style),
complemented by safety-critical penalty flags.
We evaluate the ResidencyRL-trained agent across both held-out in-domain scenarios and five
out-of-domain evaluation frameworks. On held-out in-domain cases, the agent improves over the
base model across all targeted metrics, including diagnostic accuracy (rubric score≥4/5: 81.0%
to 88.0% under adversarial conditions), management quality (3.98 to 4.52 on a 1–5 Likert scale),
and patient-centered communication (e.g., responding to emotions: 2.63 to 3.06). These improve-
ments generalize broadly: on the AMIE Mx multi-visit benchmark (Liévin et al., 2026), the agent
outperforms the base model across all six evaluation categories, with the largest gains in manage-
ment reasoning (80.1% to 88.4%) and patient communication (83.7% to 92.2%). On specialist
oncology cases curated by experts, a domain never seen during training, the agent shows signifi-
cant improvements in clinical accuracy, completeness, and actionability. On AgentClinic (Schmidgall
et al., 2024) and CRAFT-MD (Johri et al., 2025), which expose models’ tendency toward premature
closure and insufficient information gathering, the agent shows consistent improvements. Critically,
these improvements persist even when operating within an expert-optimized scaffolding: in blinded
side-by-side evaluations (𝑛=97cases) by board-certified clinicians, the ResidencyRL-trained agent
was preferred in 87.6% of cases for overall clinical impression, with significant advantages in com-
pleteness of information gathering (90.7% win rate) and management plan appropriateness (75.3%
win rate). Under adversarial conditions, the agent reduces missed red flag rates by approximately
one third, demonstrating rigorous mitigation of premature closure.
1Real consultations average 21 turns (Tu et al., 2025) and demand diagnostic and management documentation.
3

ResidencyRL: Reinforcement Learning in Simulated Clinical Environments
The core contributions of our work are as follows: (1)Long-horizon multi-turn RL for sequen-
tial clinical reasoning:We present ResidencyRL and demonstrate that training clinical AI agents
through simulated patient encounters significantly improves sequential clinical reasoning, manage-
ment quality, and safety relative to the base model. (2)Cross-specialty and cross-environment
generalization:We provide extensive empirical evidence that the procedural competencies devel-
oped through simulation-based RL training generalize to out-of-domain settings, including unseen
specialties (oncology), longitudinal multi-visit care (AMIE Mx), and clinician-curated telehealth sce-
narios, confirmed by both automated rubric evaluation and human expert evaluations. (3)Safer
and more thorough clinical reasoning:We establish that this training paradigm actively reduces
dangerous diagnostic pitfalls, including premature closure and missed safety-critical red flags, un-
deradversarialconditions. ProspectivevalidationoftheResidencyRL-trainedagentwithrealpatients
remains necessary to confirm that these simulation-trained competencies translate to patient-level
efficacy and safety.
2. Related Work
While early medical AI demonstrated the potential of narrow, task-specific models (Rajpurkar et al.,
2022;Topol,2019), generalistfoundationmodelswithadvancedmedicalreasoningabilitiespromise
a new paradigm for medical AI (Moor et al., 2023). Built through self-supervision on large, diverse
datasets, these models learn medicine without ever practicing it. Much as medical residents develop
competence through supervised practice with real patients, ResidencyRL trains an agentic policy to
navigate complete, multi-turn clinical encounters in simulation via online reinforcement learning.
Foundational Medical AI.Foundation models encode clinical knowledge, which translates to reach-
ing expert-level performance on medical question-answering benchmarks like the MedQA-USMLE
(Jin et al., 2021; Liévin et al., 2024; Nori et al., 2023; Saab et al., 2024; Singhal et al., 2023,
2025). Retrieval-augmentation and tool-use extend this knowledge (Liévin et al., 2023; Lopez et al.,
2025; Zakka et al., 2024; Zhao et al., 2025) and single-turn reinforcement learning on verifiable
medical questions pushes reasoning further (Lai et al., 2026; Pan et al., 2025). However, these
advances remain confined to a single-turn paradigm: early fine-tuned clinical models (Han et al.,
2023; Li et al., 2023; Wang et al., 2023; Wu et al., 2024) demonstrated conversational form but
lacked rigorous multi-turn evaluation. AMIE (Tu et al., 2025) marked a paradigm shift: self-play
supervised fine-tuning combined with blinded OSCE-style evaluations showed an LLM matching pri-
mary care physicians on history-taking, communication, and diagnostic accuracy. Subsequent work
scaled this paradigm to complex differential diagnosis (McDuff et al., 2025), multimodal special-
ist domains (Saab et al., 2026), multi-visit disease management (Liévin et al., 2026), physician-
centered oversight (Vedadi et al., 2025), consumer symptom elicitation and triage (Breda et al.,
2026), and prospective clinical deployment with real patients (Brodeur et al., 2026). Yet none of
these approaches optimize across the chain of decisions that constitutes an encounter. Per-turn su-
pervision, whether from demonstrations or preferences, cannot teach an agent when to transition
from history-taking to investigation, how to triage urgent presentations, or how to converge on a
diagnosis efficiently.
Long-horizonreinforcementlearning.Whiletraditionalreinforcementlearningachievedsuperhu-
man capabilities in long-horizon environments (Silver et al., 2017; Vinyals et al., 2019), RL for LLMs
initially collapsed into single-turn Reinforcement Learning from Human Feedback (RLHF) (Ouyang
et al., 2022) and its derivatives. These methods optimize a degenerate Markov Decision Process
(𝑇=1) in a static space: the prompt is the state, the response is the action, and reward is imme-
diate. However, dialogue, including clinical dialogue, is a dynamic environment that necessitates
both an LLM and an interactive simulator. To capture this shift, Zhang et al. (2025) distinguish
4

ResidencyRL: Reinforcement Learning in Simulated Clinical Environments
Table 1|RL & Clinical simulation.Systems are categorized by encounter horizon (𝑇= max turns),
action space, training optimization (Prompting= no parameter update), training or interaction en-
vironment, and clinical domain. GRPO = Group Relative Policy Optimization; SFT = supervised
fine-tuning; RLHF = RL from human feedback.
Model & Citation Horizon Action Space Optimization Training / Interaction Env. Domain
AI Clinician(Komorowski
et al., 2018)
𝑇≲20Discrete fluid &
vasopressor
Off-policy (tabular RL) Offline retrospective EHR
(MIMIC-III / eICU)
ICU resuscitation
AgentClinic(Schmidgall
et al., 2024)
𝑇≤20Dialogue + measurement
requests
Prompting (structured)Multi-agent clinical env.
(MedQA, NEJM, MIMIC-IV)
Clinical benchmark
eval.
Multi-Agent CFlow(Wang
et al., 2025)
𝑇≲20Inquiry + orders + dx +
Rx
Prompting (structured)Consultation flow env.
(derived from medical
records)
Multi-stage
diagnosis
MAI-DxO(Nori et al., 2025) – Questions + test orders +
dx
Prompting (orchestrated)Gatekeeper-mediated
NEJM-CPC sim (304 cases)
Sequential
diagnosis
AMIE(Tu et al., 2025)𝑇≲25Dialogue Self-play SFT Self-play patient sim
(multi-specialty)
Diagnostic
consultation
AMIE Mx(Liévin et al.,
2026)
𝑇≤75Dialogue + management
plan
Self-play SFT + RLHF Self-play multi-visit patient
sim (guideline-grounded)
Longitudinal
disease mgmt.
SymptomAI(Breda et al.,
2026)
𝑇≤6Dialogue + HPI/DDxPrompting (structured)Patient-facing Fitbit app incl.
wearable data (N=13,917)
Consumer symptom
assessment
SALUS(Gao et al., 2026)𝑇≲25Diagnostic test orders Step-wise RL (GRPO) EHR diagnostic env. (8.6K
cases)
Diagnostic testing
DoctorAgent-RL(Feng
et al., 2026)
𝑇≤10Proactive dialogue Online agentic RL (GRPO) MTMedDialog (8,086
dialogues)
Proactive consult
DiagAgent(Qiu et al., 2025)𝑇≤12Exam & lab orders Online agentic RL (GRPO) DiagGym EHR sim (118K
MIMIC-IV)
Diagnostic ordering
Doctor-R1(Lai et al., 2025)𝑇≲10Dialogue Online agentic RL (GRPO) Qwen3-8B patient sim (up to
100K)
Clinical
history-taking
Baichuan-M2(Dou et al.,
2025)
Fragment-
level
Dialogue Multi-stage RL Record-grounded patient sim
+ LLM rubrics generator
Consultation and
advice
Baichuan-M3(Dou et al.,
2026)
𝑇𝑎𝑣𝑔≈21(4
stages)
Dialogue + DDx +
lab/imaging orders
Segmented pipeline RL
(SPAR, GSPO-style)
Passive-personality patient
sim; rubric + fact verifiers
Inquiry, testing and
diagnosis
ResidencyRL (Ours) T≤68 Dialogue +
documentation API
Online agentic RL (GRPO) Gemini 3.5 sim (57K cases,
incl. adversarial scenarios)
Diagnostic consult
and management
single-step LLM-based RL fromagentic reinforcement learning. This paradigm restores multi-turn
optimization by situating the LLM in a temporally extended Partially Observable Markov Decision
Process (POMDP), where the agent receives sequential observations𝑜𝑡, selects actions from a het-
erogeneous spaceA=A lang∪A tool, and maximizes trajectory-wide reward. When this formulation
is paired with high-fidelity simulation, well-crafted reward, and long-horizon optimization, emer-
gent capability follows, as recently demonstrated in general LLM agents (Xi et al., 2025). Clinical
encounters constitute a natural instance of this setting (Wei et al., 2018): the patient’s pathophysio-
logical state is latent, information emerges sequentially through questioning and investigation, and
outcomes depend on the cumulative trajectory of decisions. Yet prior clinical dialogue RL has op-
erated without either ingredient at scale. Real-world clinical visits average∼150spoken utterance
turns in audio transcripts and AMIE’s own text-based consultations average∼21dialogue turns (Tu
et al., 2025); yet concurrent medical RL systems (Feng et al., 2026; Lai et al., 2025; Qiu et al., 2025)
train on shorter horizons𝑇≤12.
From treatment optimization to clinical agents.Reinforcement learning has a long history in
healthcare for optimizing treatment regimes from retrospective records (Komorowski et al., 2018;
Peineetal.,2021;Raghuetal.,2017),thoughthesesystemsoperateoverstructured,low-dimensional
state and action spaces (see Coronato et al. (2020); Yu et al. (2021) for reviews). Training clinical
AI agents to converse moves the action space into natural language, building on RL for task-oriented
dialogue (Singh et al., 2002; Young et al., 2013) and automatic diagnosis (Wei et al., 2018). Several
concurrent systems extend clinical dialogue RL beyond𝑇=1, applying Group Relative Policy Opti-
5

ResidencyRL: Reinforcement Learning in Simulated Clinical Environments
mization (GRPO) to multi-turn training: Doctor-R1 (Lai et al., 2025) introduces experience replay
to ground policy learning in retrieved past trajectories; DoctorAgent-RL (Feng et al., 2026) validates
proactivequestioningwithrealpatients; DiagAgent(Qiuetal.,2025)trainswithinanEHR-grounded
world model. SALUS (Gao et al., 2026) applies per-step GRPO with multi-agent role decomposition,
while Multi-Agent CFlow (Wang et al., 2025) addresses premature closure via hierarchical action
spaces. Baichuan-M2 (Dou et al., 2025) replaces static answer verifiers with a dynamic verifier sys-
tem pairing a record-grounded patient simulator with a clinical rubrics generator, trained via multi-
stage GRPO; however, its multi-turn stage optimizes fragments, a slice of dialogue history is scored
against locally generated rubrics. Baichuan-M3 (Dou et al., 2026) instead decomposes the consulta-
tion into a four-stage pipeline (inquiry, differential, laboratory testing, diagnosis) with stage-specific
rewards and quality-gated transitions. Both establish that rubric-verified simulation is an effective
training signal, but both trade end-to-end trajectory optimization for tractability: reward is defined
over a fragment or a stage rather than the full encounter, and neither trains documentation or man-
agement planning as first-class actions. These systems remain constrained in action space: either
homogeneous dialogue (Alang only, as in Doctor-R1, DoctorAgent-RL, and Baichuan-M2) or narrow
structured orders (as in SALUS and DiagAgent). Furthermore, while some of these systems incor-
porate multi-dimensional rewards (e.g., scoring empathy or efficiency), their clinical scope remains
limited to isolated sub-tasks (diagnostic inquiry, test ordering, or structured diagnosis) rather than
the complete encounter. In contrast, ResidencyRL optimizes the full clinical encounter over extended
horizons, jointly training multi-turn inquiry, tool utilization, clinical documentation, comprehensive
management planning, and adversarial safety.
Scaling clinical simulation.As in human medical education, the competence ceiling of simulation-
based training is bounded by environment fidelity (Barrows, 1993; Cook et al., 2010). Early clinical
dialogue benchmarks rely on rigid symptom ontologies (Fansi Tchango et al., 2022), with evaluation
benchmarksscalingtomulti-agentfree-formdialogue(Johrietal.,2025;Schmidgalletal.,2024)and
recent work advancing multi-agent virtual hospitals (Li et al., 2024), and generative simulation of
patient state evolution (Mu et al., 2026). On the patient simulation axis, state-aware memory (Liao
et al., 2024) and persona-driven behavioral profiles (Kyung et al., 2026) have increased realism,
but prior simulators remain cooperative benchmarks: real patients minimize symptoms, withhold
history, and resist recommendations (Barrows, 1993). Finally, a dialogue-only environment can train
history-taking but cannot train consequential clinical decisions such as documentation, management
planning, or triage, a limitation increasingly recognized by recent evaluation frameworks (Jiang
et al., 2025; Luo et al., 2026). ResidencyRL scales all of these axes simultaneously on a frontier
model: 57K generated scenarios, adversarial patient simulation, a composite autorater aligned with
validated clinical evaluation criteria, and a heterogeneous action space (Alang∪Atool) within a long-
horizon RL framework (𝑇≤68actions;60messages and8tool calls). Table 1 provides detailed
comparison of these works.
3. Methods
TheResidencyRLtrainingframeworkiscomposedoffourmaincomponents. (1)AScenariogenera-
tion pipelinesynthesizes and curates diverse, medically rigorous clinical cases and safety challenges
providing the foundations for encounters spanning the full complexity spectrum of primary care and
telehealth medicine. (2) ASimulatedenvironmentlets the agent (doctor) interact with a simulated
patient and a documentation API during training. (3) AStructured autoraterevaluates the agent’s
diagnostic accuracy, communication skills, and strict adherence to clinical safety constraints based
on a multi-level rubric grounded in the scenario data. (4) AReinforcement learning algorithm
iteratively improves the agent based on live environment feedback. At evaluation time, we deploy
6

ResidencyRL: Reinforcement Learning in Simulated Clinical Environments
Name:                Wendi
Age:                 33
Sex:                 Female
Ethnicity:           White
Location:            Decatur, Illinois, United States
Occupation:          Office administrator
Living Situation:    Lives with spouse
Health Literacy:     Moderate
Conversation effort: Minimal (effort level 2)
Smoking:             Never smoker
Alcohol:             Social drinker (1--2 drinks on weekends)
Substances:          None
Exercise:            Sedentary
Diet:                Standard American diet
Stress Level:        Moderate work-related stress
Recent Travel:       None
Sexual Activity:     Sexually active with one partner
Symptom Duration:    12 hours
Symptom Severity:    Moderate to severe (worsening swelling)
Medical History:     Hypertension
Medications:         Lisinopril 10mg daily
Allergies:           Penicillin — rash
Summary: Wendi is a 33-year-old female presenting with acute
onset of swelling in her upper and lower lips, which she
suspects is an allergic reaction. She denies any new foods,
insect stings, or changes in environmental exposures. She has
no hives or itching, just uncomfortable, tense swelling that
began late last night and has progressively worsened. She has
a history of mild hypertension but considers herself generally
healthy.
CRITICAL HIDDEN INFORMATION — DO NOT VOLUNTEER
Evidences (reveal when asked):
  • Where is the swelling located? → upper lip(R)
  • Where is the swelling located? → bottom lip(R)
  • Where is the swelling located? → mouth
  • Where is the affected region located? → upper lip(R)
  • Where is the affected region located? → bottom lip(R)
  • Do you have swelling in one or more areas of your body? → Yes
  • Are you consulting because you have high blood pressure? → Yes
  • Do you have high blood pressure or do you take medications to treat high
    blood pressure? → Yes
Critical hidden information: There is one piece of history that is clinically
very important but you must NOT mention unless the doctor asks directly and
specifically. General questions ("any other medical history?", "anything else I
should know?") do NOT trigger disclosure.
  • Hidden fact: Patient was recently prescribed Lisinopril 10mg daily for her
    hypertension two weeks ago.
  • Trigger: The doctor must specifically ask for the exact name or class of
    the blood pressure medication the patient takes.
Personality: Wendi is extremely agreeable and polite (Agreeableness: 100), but
very quiet and reserved (Extraversion: 25). Her conversation effort is minimal
(Level 2). When asked open-ended questions, she gives very short, polite, but
terse answers. She will not volunteer detailed medical history. If asked what
medications she takes, she will simply say "a blood pressure pill" and will not
offer the specific name unless directly asked "What is the name of the pill?"
or "Which blood pressure medication is it?". She is cooperative but needs
specific prompting to yield useful diagnostic information.
Figure2|Examplepatientscenariocontext.Thescenariocontextprovidedtothepatientsimulator
fora33-year-oldfemalepresentingwithswellinglips. Thecontextspecifiesthepatient’sdemograph-
ics, medical history, personality profile, conversation style effort level, and a set of clinical evidence
and histories to disclose when asked. Acritical hidden informationblock instructs the simulator to
withhold the patient’s specific blood pressure medication (Lisinopril 10mg). Figure 3 shows the cor-
responding training rollout.
the agent in other clinical environments such as AgentClinic and CRAFT-MD (Section 4.4).
3.1. Scenario generation pipeline
High-qualityclinicalscenariosarerequiredtogroundtheResidencyRLsimulatorinauthenticpatient
profiles,comprehensivemedicalhistories,andvalidatedpathophysiologicaldiseasestates(Figure2).
Because scenario quality strictly upper-bounds downstream policy performance, clinical incoherence
leads to agents ignoring medical inconsistencies, while demographic homogeneity has the potential
to induce representation bias. Moreover, sampling only common presentations may leave the model
unprepared for unconventional case presentations where diagnostic error carries the highest clini-
cal cost (Schiff et al., 2009). We therefore formulate scenario creation as a dynamic, multi-stage
generative pipeline with automated clinical verification. This pipeline explicitly resolves the tension
between broad diversity and strict clinical realism across four generation stages, yielding scenarios
thateachencodearichpatientcontext, adetailedclinicalpresentation, andaground-truthdiagnosis
with a ranked differential. To further test specific competencies, we supplement the base scenarios
with two extension packs targeting history-taking and safety capabilities.
Stage 1: Demographic, behavioral, and clinical attribute sampling.We sample profiles from
the United States demographic distributions to capture dimensions influencing clinical presentation
and healthcare utilization, and to produce scenarios as representative of real-world distributions
as possible. Age is drawn from a mixture-of-Gaussians model fitted to CDC NHIS 2021 telehealth
utilization rates (Centers for Disease Control and Prevention, 2021). Ethnicity is sampled across
six US Census Bureau categories, with first names co-sampled over ethnicity and sex using census-
derived frequencies (Tzioumis, 2018). Location is drawn from a population-weighted distribution of
US metropolitan areas.
Beyond demographics, we assign behavioral profiles grounded in personality psychology. Big
7

ResidencyRL: Reinforcement Learning in Simulated Clinical Environments
Doctor: Hello! I am an AI assistant de-
signed to help gather your medical in-
formation today before you speak with a
clinician. Could you please share your
name, age, and your sex assigned at
birth?
Patient: I’m Wendi. I am 33, and fe-
male.
Doctor: What brings you in today?
Patient: My lips are really swollen.
Doctor: Because lip swelling can some-
times be related to serious allergic reac-
tions, I need to ask a few urgent ques-
tions. Are you having any difficulty
breathing, shortness of breath, or a feel-
ing that your throat is closing?
Patient: No, my breathing is fine.
Doctor: Any swelling in your tongue, or
difficulty swallowing or speaking?
Patient: No, my tongue is fine and I can
swallow okay.
Doctor: When did the swelling start,
and did it come on suddenly or gradu-
ally?
Patient: It started late last night. It
came on pretty suddenly and has been
getting worse.
Doctor: Is it your upper lip, lower lip, or
both? Does it feel itchy, painful, tight, or
tingling?
Patient: Both lips. It feels tight and un-
comfortable. It isn’t itchy.
Doctor:Anyotherswellingelsewhere—
around your eyes, hands, or feet? Any
rashes or hives?
Patient: No, just my lips.
Doctor: Are you currently taking any
prescription medications? In particular,
do you take any blood pressure medica-
tions?
Patient:Yes, Itakeabloodpressurepill.
Doctor: Do you know the exact name
of your blood pressure medication? And
how long have you been taking it?
Patient: It is lisinopril. I’ve been taking
it for about two weeks.
Doctor: Have you ever had swelling like
this before? Are you taking any other
medications, including over-the-counter
pain relievers like ibuprofen?
Patient: No, I’ve never had this before.
Doctor: Have you taken any ibuprofen
recently? Any stomach pain, cramping,
or nausea?
Patient: No, I haven’t taken any re-
cently.
Doctor: Do you have any known aller-
gies to medications, foods, latex, or in-
sect stings? Does anyone in your family
have a history of unexplained swelling?
Patient: I’m allergic to penicillin. It
gives me a rash.
Doctor: Is there any chance you could
be pregnant? Besides high blood pres-
sure,doyouhaveanyotherchronicmed-
ical conditions?
Patient: No, there’s no chance.
Doctor: Do you smoke cigarettes, drink
alcohol, or use any recreational sub-
stances?
Patient: No, nothing else.
Doctor: Any recent dental work, dental
pain, injuries to your lips, or insect bites
around your face?
Patient: No, I haven’t had any.
Doctor: Thankyouforsharingallofthis
important information with me, Wendi.
Because I am an AI assistant and cannot
perform a physical examination or check
your vitals, I cannot give you a final di-
agnosis. I have carefully documented all
of your symptoms, your medical history,
and your medications. A provider will be
withyoushortlytodiscussthenextsteps.
Patient: Okay, thank you.
▶submit_urgencyemergency_care
▶submit_diagnosisLisinopril-induced angioedema
▶submit_differential_diagnosisACE-inhibitor-induced
angioedema (very likely); idiopathic angioedema (likely);
IgE-mediated allergic angioedema (possible); NSAID-
induced angioedema (possible); hereditary angioedema
(possible); contact cheilitis (unlikely); infectious cheilitis
(unlikely); acquired angioedema (unlikely)
▶submit_management_planstop Lisinopril immedi-
ately; ED referral for airway monitoring; avoid NSAIDs;
switch to CCB (e.g. amlodipine); avoid ARBs (cross-
reactivity risk); C4/C1-INH levels if recurrence; red-flag
education; PCP follow-up 24–48h
▶submit_soap_noteS: 12h bilateral lip swelling,
tight/non-pruritic, worsening, started Lisinopril 2wk ago;
O: telehealth; A: ACE-inhibitor-induced angioedema;
P: stop Lisinopril, ED, airway monitoring, switch
antihypertensive
▶terminateencounter complete
Figure 3|Example training rollout.The agent conducts a 16-turn structured telehealth encounter
withthepatientdescribedinFigure2. Throughtargetedhistory-taking, theagentelicitsthepatient’s
specific blood pressure medication (Lisinopril 10mg, a critical hidden diagnostic factor) by inquir-
ing directly about prescription details, and correctly identifies Lisinopril-induced angioedema as the
primary diagnosis. Serif text: verbatim transcript; blue: agent; green: simulated patient; red: tool
calls. Reasoning steps omitted.
Five traits are sampled from population-calibrated Gaussian distributions (Stackhouse et al., 2024),
with age and sex adjustments capturing known maturation effects. These traits dictate encounter dy-
namics: high Neuroticism predicts symptom amplification (Costa Jr and McCrae, 1987), low Agree-
ableness predicts clinician challenge, and low Conscientiousness predicts non-adherence. A derived
conversation effort score (1–5) governs response length and grammatical formality, ensuring agents
encounter the full communicative spectrum, from terse one-word replies to structured medical nar-
ratives.
Presenting complaints are sampled uniformly across 81 conditions spanning five clinical cate-
gories (Respiratory & Cardiovascular, Musculoskeletal, Genitourinary & Reproductive, Gastrointesti-
nal, and Other). Details can be found in Table A1. This balances high-prevalence primary care
8

ResidencyRL: Reinforcement Learning in Simulated Clinical Environments
caseloads against lower-prevalence conditions carrying disproportionate diagnostic risk. Real-time
batch monitoring prevents distributional skew prior to training.
Stage 2: Condition-targeted generation.Conditioned on the demographic, behavioral profile, and
clinical attributes, an LLM (Gemini 3.1 Pro (Gemini Team Google, 2026a)) generates the clinical
scenario via a structured schema. This requires a presenting complaint calibrated to health literacy,
a patient summary detailing symptom progression, pertinent positives and negatives drawn from the
DDXPlus evidence corpus (Fansi Tchango et al., 2022), comprehensive medical and social histories,
a complete medication list, a ground-truth primary diagnosis, and a ranked differential. Grounding
generated scenarios in DDXPlus ensures clinical findings reflect validated associations rather than
hallucinated artifacts. Scenario difficulty is modulated via a complexity parameter (1–5) controlling
comorbidities, symptom overlap, medication interactions, and social confounders (Table A2). Level
1 presents straightforward textbook conditions, while Level 5 constructs highly complex cases (e.g.,
rare conditions mimicking benign diagnoses, polypharmacy interactions, and unreliable historians
triggering anchoring bias).
Stage 3: Quality verification.Scenarios further undergo LLM-as-judge clinical coherence verifi-
cation. Here, an independent LLM evaluates five dimensions: internal consistency, clinical realism,
differential diagnosis quality, demographic appropriateness, and completeness. The judge issues
one of three verdicts:accept,modify(providing corrected fields for minor inconsistencies), orreject
(discarding scenarios with fundamental clinical errors). This automated review board catches age-
impossible diagnoses, pharmacological contraindications, and inconsistent symptom profiles based
on Gemini 3.1 Pro’s judgment.
Stage4: Deduplication.The scenario pool is then deduplicated using character-trigram TF-IDF vec-
torization (Sparck Jones, 1972) over patient summaries. Pairs exceeding a cosine similarity thresh-
old of0.9are pruned, maximizing clinical diversity and preventing policy memorization of specific
narratives.
Scenario extension packs.To mitigate critical failure modes, we augment the dataset with special-
ized scenarios targeting clinical investigation skills and safety vulnerabilities.
1.Targeted history-taking scenarios.Diagnostic errors frequently stem from incomplete or in-
adequatehistory-takingratherthanknowledgedeficits(Graberetal.,2005). Totrainproactive
information elicitation, we generate targeted scenarios across a four-domain taxonomy where
critical clinical information is withheld unless specifically prompted by the agent:(1) Social
and lifestyle, where the diagnostic pivot depends on an occupational or lifestyle fact (e.g.,
substance-use mimicking a panic disorder) omitted from general responses;(2) Medication
specifics, where the correct diagnosis requires the specific drug name or dose, not merely the
broad category (e.g., fluoroquinolone versus antibiotics, in cases of fluoroquinolone tendinopa-
thy);(3) Symptom characterization, where a specific qualifier dictates the diagnosis (e.g., a
“thunderclap” onset distinguishing a subarachnoid hemorrhage from a severe migraine); and
(4) Exposures, where an environmental or infectious exposure alters the differential (e.g., en-
demic travel shifting the diagnosis from a viral syndrome to malaria). Each scenario specifies
the hidden fact, the requisite clinician question, the baseline differential reached without the
fact, and the revised differential following successful elicitation.
2.Adversarial safety scenarios.Medical AI vulnerabilities require domain-specific adversarial
designs distinct from general-purpose prompt injection (Balazadeh et al., 2025; Zou et al.,
2023). We generate adversarial scenarios across a 9-category clinical safety taxonomy: (1)
Critical emergency escalation(e.g., STEMI with minimized red-flag symptoms); (2)Clinical
boundaryenforcementincontextswheretext-basedtelehealthisunsafe; (3)Diagnosticintegrity
9

ResidencyRL: Reinforcement Learning in Simulated Clinical Environments
against atypical presentations tempting premature closure; (4)Pharmacological limitsenforc-
ing safe prescribing boundaries; (5)Vulnerability and abuse recognition; (6)Age verificationfor
age-specific decisions; (7)Ethical autonomyrespecting patient beliefs; (8)Crisis de-escalation
for acute mental health presentations; (9)Clinical objectivityagainst patient manipulation.
3.2. Simulated environment
The agent communicates with the patient simulator via text and documents the full trajectory of the
encounter through a dedicated API. These artifacts are later sent to the autorater for grading and
reward computation (Section 3.3).
3.2.1. Documentation API
The environment exposes a simple tool-calling API emulating structured clinical workflows similar to
prior work (Brodeur et al., 2026; Liévin et al., 2026; Tu et al., 2025). The interface comprises seven
instruments: (1)patient chart reviewto access baseline demographics and other pre-consultation
data, when available; (2)primary diagnosis submission; (3)differential diagnosis submission, which
accepts a ranked list with reasoning chains (McDuff et al., 2025); (4)urgency classification; (5)
management plan submissionfor structured interventions and safety-netting; (6)patient-facing sum-
maryusing plain language for patient comprehension (Epstein and Street, 2007); and (7)clinical
documentationfollowing the SOAP note (Subjective, Objective, Assessment, and Plan) format. Fi-
nally, anencounter terminationaction signals the completion of an episode. These tools extend the
agent’s role beyond history-taking to active clinical decision-making. Although the simulator does
not model the downstream physiological effects of a prescribed treatment, the structured autorater
(Section 3.3) proxies these real-world outcomes by evaluating submitted artifacts against scenario
data. This ensures that the agent’s actions carry appropriate clinical weight during training.
3.2.2. Patient simulator
Patients are simulated using Gemini 3.5 Flash (Gemini Team Google, 2026b) conditioned on the
clinical scenarios (Section 3.1; Figure 2), offering a scalable alternative to human standardized pa-
tients (Barrows, 1993). The simulator operates via a single Thinking-enabled LLM call per conver-
sational turn: given the scenario’s full medical record, the conversation history, and the agent’s most
recent message, it produces a patient response consistent with the clinical ground truth and detailed
prompt instructions (example rollout provided in Figure 3).
Behavioral layer.Patient communicative behavior is shaped by prompt-level instructions aligned
with dimensions known to influence real clinical outcomes. This behavior is modulated by three
primary mechanisms:(1) Health literacy adaptationcalibrates vocabulary and medical terminology
to the patient’s demographic profile (e.g., a patient with low health literacy might describe “the little
white heart pill” rather than “atenolol 50mg”).(2) Information asymmetrydistinguishesproactive
information (chief complaint, stated concerns, and scenario-specific questions the patient may raise)
fromreactivebackground details (demographics, medical history, medication specifics), which are
disclosedonlywhentheclinicianasksadirectquestionaboutthattopic.(3)Pacingconstraintsensure
the simulator answers only the first question when multiple are posed simultaneously, introduces
concerns one at a time across turns, and keeps responses under approximately 50 words, matching
the natural cadence of chat-based encounters.
This layered behavioral specification reflects robust evidence that patient communicative char-
acteristics significantly influence clinical encounter outcomes. In reality, patients frequently over-
or understate concerns (Bell et al., 2002), misgauge symptom severity, and express reluctance to
10

ResidencyRL: Reinforcement Learning in Simulated Clinical Environments
clinical recommendations (Levinson et al., 1997; Stewart, 1995) — patterns that are systematically
amplified among populations with lower health literacy (Kutner et al., 2006; Paasche-Orlow et al.,
2005) or higher medical mistrust (Boulware et al., 2003; LaVeist et al., 2009). Because the simulator
adapts its register, vocabulary, and disclosure behavior to each scenario’s demographic and clinical
profile, behavioral variation arises naturally from the diversity of sampled scenarios. Consequently,
the resulting patient population spans the full range of realistic clinical challenge, from cooperative
and articulate to evasive and health-illiterate.
Adversarial specialization.For adversarial safety scenarios (Section 3.1), the simulator prompt is
augmentedwithastaticadversarialaddendumthatlayerschallengingpatientbehaviorsontopofthe
standard realism rules. Each subcategory carries specific behavioral instructions that the simulator
follows; for instance, a patient in theconcealed_atypical_emergencysubcategory will actively
minimize symptoms, attribute them to benign causes, and resist 911/ER suggestions. This design
adapts a broader paradigm of LLM-based redteaming (Perez et al., 2022) to clinical settings. A
difficulty level (1–3) calibrates the intensity of adversarial behavior: at Level 1 (mild) the patient
yields after a single direct question, whereas at Level 3 (expert) the patient sustains deception across
multiple turns, deflects even direct questions, and requires persistent, empathetic probing to reveal
critical details. The addendum is fixed for the duration of each episode, ensuring reproducibility of
safety evaluations while capturing the core challenge that the clinician must actively probe past the
patient’s surface presentation to reach clinically relevant ground truth.
At each turn the simulator internally identifies questions in the clinician’s message, consults
the scenario, and drafts a candidate response, which it validates against eleven enumerated failure
modes (e.g., reasoning leakage, physiological inconsistency, exceeding the patient’s plausible knowl-
edge, topic mixing, and overly cooperative behavior). Tool calls, the agent’s internal reasoning, and
the evaluation rubric are withheld from the simulator, preventing the patient from inadvertently
confirming the agent’s diagnostic hypotheses.
3.3. Structured reward and auto-grading
Upon episode completion, the agent’s generated clinical artifacts (e.g., predicted differential, man-
agement plan) and the full conversation transcript are auto-graded via an LLM judge with a struc-
tured rubric (Appendix B). This hierarchical rubric decomposes encounter performance into inter-
pretable and independent dimensions, aligning with and extending prior randomized clinical eval-
uations of conversational diagnostic AI (O’Sullivan et al., 2026; Tu et al., 2025). The reward is
formulated asR=R primary−R penalty∈[−3,3].
The primary reward component (Rprimary) assesses clinical accuracy, history-taking, and style,
whereas the penalty component (Rpenalty) captures violations of system constraints (e.g., tool for-
matting errors, exceeding maximum conversation length) and critical behavioral failures (flags).
Primary endpoint.The primary reward componentRprimary evaluates six clinical dimensions across
26 Likert sub-axes, complemented by up to 8 binary safety flags and 3 system-level penalties (Ta-
ble 2):
Rprimary =3·  2/9¯𝑟ddx+ 3/9¯𝑟mgmt+ 1/9¯𝑟comm+ 1/9¯𝑟doc+ 1/9¯𝑟intake+ 1/9¯𝑟style ∈[0,3](1)
where each¯𝑟𝛼∈[0,1]is the normalized weighted mean of the sub-axis scores within dimension𝛼
(Likert1–5,mappedto[0,1]via¯𝑠=(𝑠−1)/4),andtheleadingfactorof3setstherewardscalesothat
Rprimary∈[0,3]. The weights are defined to prioritize management quality and diagnostic accuracy.
The diagnostic dimension assesses the accuracy, completeness, and prioritization of the submitted
differential diagnosis (DDx) relative to the ground-truth condition, drawing on the DDx quality and
11

ResidencyRL: Reinforcement Learning in Simulated Clinical Environments
Table 2|Rewardstructure.The total rewardR=R primary−Rpenalty∈[−3,3]sums a primary clinical
score and a penalty term. Each primary sub-axis is scored on a Likert 1–5 scale by an independent
Gemini 3.1 Pro judge call, then normalized to[0,1], except where noted as binary (pass/fail). All
judge calls receive the ground-truth scenario as reference. Both penalty flags and system feedback
accumulate via summation, with the total penalty clamped at3.0.
Dimension Weight Graded on Sub-axes / description
Diagnosis 2/9Diagnosis Accuracy (1 axis)
Management 3/9Management plan,
urgency, SOAP note
Urgency, investigations, treatment, follow-up, overall quality,
safety (6 axes)
Intake 1/9Transcript, diagnosis Social/lifestyle history, medication/past medical history,
symptom characterization, exposure screening (4 axes)
Communication 1/9Transcript, patient facing
summary
Fostering relationship, gathering information, responding to
emotions (PCCBP; 3 axes)
Documentation 1/9Transcript, SOAP note,
management plan
PDQI-9: up-to-date, accurate, thorough, useful, organized,
comprehensible, succinct, synthesized, internally consistent (9
axes)
Style 1/9Transcript Natural questioning style, no repeated questions (binary),
conversation conclusion (3 axes)
Critical flags – Transcript & submissions 4 binary flags (1.0–3.0); 4 additional for adversarial scenarios
System feedback – Environment interactions Parsing errors (0.5/each), missing termination (0.5),
excessive turns (0.1–1.0)
appropriateness scales of Bond et al. (2012); McDuff et al. (2025); Tu et al. (2025). Management
quality evaluates urgency calibration, investigation and treatment appropriateness, follow-up and
safety-netting adequacy, and overall plan quality and safety, building on the management evaluation
framework in Liévin et al. (2026). Communication quality, adapted from the Patient-Centered Com-
munication Best Practices (PCCBP) instrument (Tu et al., 2025), evaluates information-gathering
thoroughness, relationship building, shared decision-making, and emotional responsiveness. Docu-
mentation quality follows the Physician Documentation Quality Instrument (PDQI-9; Stetson et al.
(2012)). Finally, the intake and style dimensions are developed specifically for this work to capture
conversational mechanics in targeted clinical settings.
Rather than evaluating all 26 Likert sub-axes and 8 safety flags within a single, monolithic judge
prompt, we partition the rubric into eight topic-oriented criteria groups corresponding to the dimen-
sions in Table 2. Each topic group is evaluated by a dedicated Gemini 3.1 Pro judge call (Zheng et al.,
2023) with structured output schema constraints (Koo et al., 2024). This analytic scoring approach
is motivated by psychometric evaluation theory: independent evaluation of discrete criteria has been
shown to improve inter-rater consistency relative to holistic judgments in human assessment con-
texts (Jonsson and Svingby, 2007). This finding has been corroborated for medical AI evaluation,
with substantial gains in expert alignment and scoring stability (Arora et al., 2025; Zhang et al.,
2026). Beyond improved consistency, this partitioning offers two practical advantages:
1.Evaluator focus and context isolation:By restricting each prompt to a single criterion group,
we mirror the psychometric benefits of analytic scoring while simultaneously addressing LLM
context limitations. This isolation prevents quality masking across unrelated axes (e.g., scor-
ing empathetic tone while simultaneously checking drug dosages and SOAP note formatting).
Each call receives only the clinical artifacts relevant to its specific topic group (e.g., SOAP note
for Documentation; full transcript for Communication) alongside the ground-truth scenario,
ensuring focused, evidence-grounded scoring.
2.Parallelization:Because the eight topic-group evaluations are conditionally independent, all
12

ResidencyRL: Reinforcement Learning in Simulated Clinical Environments
asynchronous judge calls are dispatched concurrently, improving overall scoring throughput.
Penalties.R penalty clamped to[0,3]sums two groups:
1.CriticalflagsarebinarychecksevaluatedbyanindependentLLMjudgecall. Standardflagsin-
clude hallucination of clinical information (penalty of2.0), contraindicated actions (3.0, e.g.,
prescribing opioids to a patient concealing an addiction history), management plan leakage
(2.0), and a catch-all flag for other safety violations (1.0). These flags are summed to penalize
compound violations. Foradversarial safety scenarios(Section 3.1), additional flags are en-
abled to evaluate missed critical screening questions (2.0, e.g., suicide risk assessment when
depressive symptoms are present), contraindicated actions from the scenario’s safety gates
(3.0), under-triage below the scenario’s minimum urgency (3.0), and missed safety red flags
(3.0).
2.System feedbackaccumulates deterministically:0.5per action-parsing failure,0.5for a miss-
ing termination signal, and a piecewise-linear penalty ramping from0.1at 30 conversational
turns to1.0at 40 turns. Without this turn-length control, the agent defaults to exhaustive
symptom enumeration rather than hypothesis-driven questioning, a failure mode analogous
to undirected review-of-systems screening. The penalty thus incentivizes focused, efficient
history-taking consistent with expert clinical reasoning.
3.4. Reinforcement learning
We train the clinical agent via online multi-turn reinforcement learning using group relative policy
optimization (GRPO) (Shao et al., 2024), initializing from Gemini 3.5 Flash (Gemini Team Google,
2026b). The training mixture spans 49,870 telehealth scenarios covering 81 clinical conditions,
supplemented with 5,000 history-taking scenarios and 2,583 adversarial safety scenarios (mixed
at 83%/15%/2% respectively), all generated using the pipeline described in Section 3.1. In each
episode, the agent conducts a complete clinical encounter with a simulated patient: gathering his-
tory, formulating a differential diagnosis, developing a management plan, and producing clinical
documentation (e.g., SOAP note) and a patient-facing summary. For each training batch of𝑁sce-
narios, the agent generates𝐾parallel episodes per scenario. Each episode is hard-capped at 60
patient turns. At each episode completion, Gemini 3.1 Pro evaluates the conversation transcript and
documentationsubmittedviatoolcallsagainsttheground-truthdiagnosisandmanagement,yielding
a trajectory-level scalar reward in[−3,3]. The policy is updated using GRPO, estimating advantages
from the group of𝐾trajectories without a dedicated value function. We provide comparison with
in-context learning (Brown et al., 2020) in Appendix E, demonstrating that behavioral exposure to
curated demonstrations is insufficient to match ResidencyRL.
Over the course of training (Figures 1 and 4), the agent improves across reward dimensions
at markedly different rates. The documentation dimension saturates immediately, while diagnostic
accuracy and management quality start high and grows steadily. Intake completeness, the weakest
dimension at initialization, exhibits the steepest learning curve, improving rapidly in the first 75
steps before plateauing. Communication quality improves slowly and shows no clear plateau by the
end of training. The agent’s conversational strategy shifts correspondingly: median encounter length
increasesfrom∼18to23turnsbystep100,reflectinggreaterclinicalthoroughness. Thelengthlinear
penalty discourages encounters exceeding 30 turns, yet the agent consistently pushes against this
soft limit, balancing information extraction against conversational efficiency. In parallel, the agent’s
internal reasoning allocation grows, with average thinking tokens per turn increasing steadily over
training. The overall trajectory length, aggregating conversational turns, reasoning, and tool-call
actions, expands and stabilizes at∼52 total agent steps (Figure 4).
13

ResidencyRL: Reinforcement Learning in Simulated Clinical Environments
0
10
20
30
40
50Num Conversational T urns
0
250
500
750
1000
1250
1500Thinking T okens per T urn
0 25 50 75 100 125 150 175 200
Training Step
0
20
40
60
80
100T otal Agent Steps
Figure 4|Training dynamics. Top:Distribution of conversational turns per episode across training
steps. Themedianencounterlengthincreasesfrom∼18to23turnsbystep100astheagentoptimizes
for clinical thoroughness. Red points denote rollouts penalized for exceeding 30 turns (dashed lines
mark the onset and cap of the piecewise-linear length penalty).Middle:Average thinking tokens
per turn, reflecting increasing computational effort allocated to internal clinical reasoning.Bottom:
Total agent steps per episode (thinking, conversational, and tool-call actions combined). Trajectory
length grows as a compounding result of deeper reasoning and longer history-taking, stabilizing
as the policy converges. Overlaid boxplots show the median, interquartile range, and 5th–95th
percentile whiskers. Across training, distributions widen, reflecting broader policy exploration as
the agent navigates the tension between thorough clinical investigation and efficiency constraints
(e.g., the conversational turn range expands from approximately [13, 24] at step 0 to [16, 32] at
step 100).
14

ResidencyRL: Reinforcement Learning in Simulated Clinical Environments
Table 3|Evaluation overview.Summary of the evaluation setups across Section 4, detailing the
benchmark environment, its domain relationship to the training data, the presence of a specialized
agentic harness, and the number of scenarios evaluated. SxS = Side-by-Side.
Section Evaluation Benchmark Domain Agentic Harness Scenarios (𝑁)
4.1 Held-out Telehealth In-domain No 200
4.1 Held-out Adversarial In-domain No 200
4.2 AMIE Mx (Multi-visit) Out-of-domain No 120 cases (360 visits)
4.3 Specialist Care (Automated) Out-of-domain No 300
4.3 Specialist Care (Expert review) Out-of-domain No 100 (sampled)
4.4 AgentClinic-MedQA Out-of-domain No 215
4.4 AgentClinic-MIMIC-IV Out-of-domain No 200
4.4 CRAFT-MD Out-of-domain No 1,273
4.5 AMIE Telehealth (Automated) Out-of-domain Yes 299
4.5 AMIE Telehealth (Human SxS) Out-of-domain Yes 97 (100 sampled, 3 excluded)
4. Results
In this section, we systematically evaluate the capabilities of the ResidencyRL-trained agent, span-
ning isolated single-encounter competencies to complex, end-to-end clinical workflows in an agentic
harness(Table3). Wefirstdemonstratethatmulti-turnreinforcementlearningsignificantlyimproves
corewithin-encounterclinicalskills,includingdiagnosticaccuracy,managementquality,andpatient-
centered communication (Section 4.1). Next, we show that these capabilities extend to longitudinal
care, successfully tracking patients and adapting treatment plans across multi-visit scenarios in the
AMIE Mx benchmark (Section 4.2). We then evaluate whether these gains transfer to specialist-
level care on expert-curated oncology cases, where the agent shows significant improvements in
clinical accuracy and completeness (Section 4.3). To assess the robustness of our approach, we eval-
uate whether the agent’s acquired skills generalize to external, unseen benchmarks (AgentClinic
and CRAFT-MD), examining directional trends in dynamic reasoning and the mitigation of prema-
ture closure (Section 4.4). Finally, we evaluate the ResidencyRL-trained agent within a prospective,
out-of-domain agentic framework to assess its safety and system-level integration with specialized
clinical harnesses (Section 4.5).
The in-domain evaluation (Section 4.1) uses scenarios generated by the same pipeline as train-
ing, with strict deduplication ensuring no overlap with the training set. All subsequent evaluations
(Sections 4.2–4.5) use out-of-domain scenarios or external benchmarks.
4.1. Multi-turn RL training improves clinical competence
We compared the ResidencyRL-trained agent against the base model (Gemini 3.5 Flash) on a held-
out evaluation set of 200 standard telehealth clinical scenarios and 200 adversarial safety scenarios
not seen during training. To reduce the overlap between this evaluation set and the training sets,
we filter out all cases that have a similarity score higher than 0.45 (computed by TF-IDF) with any
training or evaluation scenario and regenerate until there are 200 cases each. All evaluations used
the same automated rubric pipeline that served as the training reward signal. Results are shown
in Table 4. Because this in-domain evaluation shares the underlying scenario generation and rubric
architecture used during training, these results primarily validate that the agent successfully learns
to optimize its training signals. To establish whether this translates to true, generalizable clinical
15

ResidencyRL: Reinforcement Learning in Simulated Clinical Environments
Table 4|In-domain evaluation.Baseline vs. ResidencyRL (𝑛=200per arm, 95% bootstrap CI).
General Telehealth Adversarial Telehealth
MetricBaseline ResidencyRL Baseline ResidencyRL
Diagnostic Accuracy
Diagnostic Rubric≥4/5 86.4%[81.4, 91.0]88.4%[83.8, 92.9]81.0%[75.5, 86.0]88.0%[83.5, 92.0]
Management Quality (1-5 Likert scale)
Overall Management 3.98[3.86, 4.07]4.52[4.42, 4.61]3.94[3.79, 4.09]4.51[4.38, 4.63]
Treatment Plan 4.26[4.15, 4.35]4.66[4.58, 4.75]4.26[4.11, 4.41]4.70[4.58, 4.82]
Investigations 4.48[4.39, 4.57]4.71[4.62, 4.79]4.45[4.33, 4.57]4.78[4.69, 4.86]
Safety-netting 4.56[4.46, 4.66]4.92[4.87, 4.97]4.41[4.26, 4.56]4.79[4.68, 4.89]
Urgency Assessment 4.34[4.25, 4.44]4.69[4.61, 4.76]4.40[4.28, 4.51]4.68[4.59, 4.76]
Follow-up Plan 4.52[4.41, 4.61]4.90[4.85, 4.94]4.35[4.21, 4.48]4.82[4.74, 4.90]
Urgency Rubric≥4/5 93.5%[89.9, 96.5]98.5%[96.5, 100.0]90.0%[86.0, 93.5]96.5%[94.0, 98.5]
Communication — PCCBP (1-5 Likert scale)
Gathering Information 3.62[3.53, 3.70]3.94[3.89, 3.99]3.36[3.25, 3.45]3.88[3.80, 3.95]
Fostering Relationship 2.85[2.79, 2.91]3.27[3.20, 3.34]2.96[2.89, 3.03]3.57[3.49, 3.64]
Responding to Emotions 2.63[2.55, 2.71]3.06[2.96, 3.16]2.74[2.63, 2.86]3.57[3.46, 3.67]
Screening Completeness (1-5 Likert scale)
Symptom Characterization 3.85[3.73, 3.96]4.34[4.25, 4.43]3.86[3.76, 3.97]4.43[4.34, 4.51]
Medication & Past History 3.00[2.88, 3.13]3.58[3.50, 3.67]2.63[2.48, 2.78]3.43[3.28, 3.58]
Exposure History 2.27[2.09, 2.45]3.39[3.19, 3.58]3.73[3.48, 3.95]4.40[4.23, 4.56]
Social/Lifestyle History 1.31[1.22, 1.42]2.64[2.50, 2.80]1.57[1.42, 1.73]2.67[2.50, 2.84]
Safety Failure Rates (lower is better)
Contraindicated Action Rate — — 21.5%[16.0, 27.5]16.5%[11.5, 21.5]
Missed Critical Question Rate — — 65.5%[59.0, 72.0]43.5%[37.0, 50.0]
Missed Red Flag Rate — — 45.5%[39.0, 52.5]31.5%[25.5, 38.0]
Under-triaged Rate — — 4.0%[1.5, 7.0]4.5%[2.0, 7.5]
competence, we treat the out-of-domain and external benchmarks (Sections 4.2–4.5) as our main
evidence.
Diagnostic accuracy.We evaluated diagnostic accuracy using rubric-based assessment by an LLM
judge on a 1–5 scale. The proportion of encounters achieving a diagnostic rubric score≥4/5 (defined
as “Good differential including correct diagnosis with minor omissions”) increased from 86.4% (95%
CI: [81.4%, 91.0%]) to 88.4% (95% CI: [83.8%, 92.9%]) on standard telehealth scenarios and from
81.0% (95% CI: [75.5%, 86.0%]) to 88.0% (95% CI: [83.5%, 92.0%]) on adversarial scenarios. The
improvement was most pronounced in the adversarial setting (+7.0pp), suggesting that RL training
particularly strengthened the agent’s ability to reach correct diagnoses under challenging conditions.
Management quality.Overall management quality scores improved from 3.98 (95% CI: [3.86,
4.07]) to 4.52 (95% CI: [4.42, 4.61]) on telehealth and from 3.94 (95% CI: [3.79, 4.09]) to 4.51
(95% CI: [4.38, 4.63]) on adversarial scenarios, with non-overlapping confidence intervals in both
settings. Improvementswereconsistentacrossallsub-dimensions, withthelargestgainsinfollow-up
planning and safety-netting advice. The proportion of encounters receiving an urgency rubric score
≥4/5 (defined as “Appropriate with minor room for improvement for timeliness and setting of care”)
increased from 93.5% to 98.5% on telehealth and from 90.0% to 96.5% on adversarial scenarios.
Patient-centeredcommunication.Communicationqualityscores,adaptedfromthePatient-Centered
Communication Best Practices (PCCBP), improved across all three dimensions with non-overlapping
confidence intervals. The largest gains appeared in responding to emotions, rising from 2.63 (95%
CI: [2.55, 2.71]) to 3.06 (95% CI: [2.96, 3.16]) on telehealth and from 2.74 (95% CI: [2.63, 2.86])
to 3.57 (95% CI: [3.46, 3.67]) on adversarial scenarios, suggesting that RL training helped the agent
16

ResidencyRL: Reinforcement Learning in Simulated Clinical Environments
Table 5|AMIE Mx OSCE results (N=120). Confidence intervals (95% CI) are computed via
scenario-level bootstrapping (1,000 bootstrap iterations). P-values are reported from a two-sided
Wilcoxon Signed-Rank test with FDR correction.
Clinical Axis Base ResidencyRL Diff Adjusted𝑝-val
MXEKF (Mgmt Reasoning)
80.07%
[78.95%, 81.21%]
88.41%
[87.42%, 89.35%]
+8.34%
[+7.33%, +9.38%]5.88×10 −18
Guideline Adherence
84.17%
[82.02%, 86.08%]
86.67%
[84.48%, 88.84%]
+2.50%
[+0.52%, +4.48%]0.017
Preciseness/Memory
90.03%
[88.47%, 91.62%]
92.67%
[91.05%, 94.28%]
+2.64%
[+0.59%, +4.64%]0.017
GMPCQ (Patient Comm.)
83.69%
[82.70%, 84.62%]
92.19%
[91.27%, 93.05%]
+8.50%
[+7.27%, +9.74%]1.56×10 −17
PACES (Clinical Skills)
79.59%
[78.61%, 80.59%]
84.84%
[83.92%, 85.79%]
+5.26%
[+4.29%, +6.25%]8.60×10 −15
Diagnosis & Mgmt
90.37%
[89.26%, 91.36%]
90.68%
[89.55%, 91.74%]
+0.31%
[-0.73%, +1.34%]0.213
better acknowledge and address patient concerns.
Screening completeness.RL training produced the most pronounced improvements in screening
completeness. Social and lifestyle history—the weakest area for the base model—improved from
1.31 (95% CI: [1.22, 1.42]) to 2.64 (95% CI: [2.50, 2.80]) on telehealth (+1.33points) and from
1.57 (95% CI: [1.42, 1.73]) to 2.67 (95% CI: [2.50, 2.84]) on adversarial (+1.10points), indicat-
ing the ResidencyRL-trained agent learned to consistently inquire about occupational, social, and
lifestyle factors that the base model largely omitted. Exposure history showed similarly large gains
(+1.12telehealth;+0.67adversarial), while symptom characterization and medication history also
improved reliably across both settings.
Safety under adversarial conditions.On adversarial scenarios designed to elicit unsafe behavior,
the ResidencyRL-trained agent demonstrated meaningfully lower failure rates. The missed critical
question rate dropped from 65.5% (95% CI: [59.0%, 72.0%]) to 43.5% (95% CI: [37.0%, 50.0%])
(−22.0pp), and the missed red flag rate decreased from 45.5% (95% CI: [39.0%, 52.5%]) to 31.5%
(95% CI: [25.5%, 38.0%]) (−14.0pp). The contraindicated action rate decreased from 21.5% to
16.5%(−5.0pp),thoughwithoverlappingconfidenceintervals(95%CI:[16.0%,27.5%]vs.[11.5%,
21.5%]). The under-triaged rate remained essentially unchanged (4.0% vs. 4.5%). While these
improvementsaresubstantial—particularlytheroughlyone-thirdrelativereductioninmissedcritical
questions and missed red flags—the residual failure rates indicate room for further improvement.
4.2. Improvement on multi-visit clinical management
The prior evaluations largely focus on new and acute presentations, assessing within-encounter com-
petence. However, clinical medicine is fundamentally longitudinal: patients return for follow-up,
treatment plans require adjustment, and effective management depends on integrating information
across encounters. To assess whether training develops the ability to track a patient across visits and
adapt management appropriately in response to treatment outcomes, we evaluate the agent on the
AMIE Mx multi-visit OSCE benchmark (Liévin et al., 2026), which was designed to test the conver-
sational and management reasoning capabilities of medical AI in this type of longitudinal setting.
AMIE Mx comprises 120 clinical scenarios constructed to be aligned with BMJ Best Practice
(BMJ Publishing Group, 2026) and NICE clinical recommendations (National Institute for Health
17

ResidencyRL: Reinforcement Learning in Simulated Clinical Environments
0.0 0.2 0.4 0.6 0.8 1.0
Normalized Score
MXEKF (Management Reasoning)
   Clinician As T eacher
   Organization
   Clinician-Patient Relationship
   Illness Specific Knowledge
   Ongoing Monitoring & Adjustment
   Comm. & Shared Decision Making
   Prognostication
   Prioritization of Preferences
   Dynamic Interplay
   Contrasting And Selection
Diagnosis & Management
   DDx Includes Probable Dx
   DDx Comprehensiveness
   Avoided Confabulation
   DDx Appropriateness
   Avoided Inapprop. Treatments
   Avoided Inapprop. Investigations
   DDx Plausible Alternatives
   Management Escalation Approp.
   Suggested Approp. Treatments
   Suggested Approp. Investigations
   Management Plan Appropriateness
   Follow-Up Approp.
Guideline Adherence
   Avoids Clinically Significant Error
   Mgmt Guideline Conflict
   Individual Guideline Applicability
   Treatment Guideline Alignment
   Combined Guideline Entailment
   Investigation Guideline Alignment
   Treatment Guideline Support
   Investigation Guideline Support
***
***
***
***
***
***
***
***
***
***
***
n.s.
n.s.
n.s.
n.s.
n.s.
n.s.
n.s.
n.s.
n.s.
n.s.
n.s.
**
n.s.
*
n.s.
n.s.
n.s.
n.s.
n.s.
n.s.
**
***
0.0 0.2 0.4 0.6 0.8 1.0
Normalized Score
PACES (Clinical Skills)
   Explain Info (Professional)
   Explain Info (Clear)
   Explain Info (Structured)
   Maintaining Patient Welfare
   Explain Info (Accurate)
   Managing Patient Concerns
   Empathy
   Management Plan
   Confirm Patient Understanding
   Explain Info (Comprehensive)
   Differential Diagnosis
   Elicit Presenting Complaint
   Elicit Medication Hx
   Elicit Systems Review
   Elicit Past Medical Hx
   Elicit Family Hx
GMPCQ (Patient Comm.)
   Confidence In Ability
   Happy T o See Again
   Explain Condition/Treatment
   Providing Treatment
   Trustworthiness
   Politeness
   Making Feel At Ease
   Listening
   Assessing Condition
   Involving In Decisions
   Confidentiality
Preciseness & Memory
   Investigation Precision
   Inter-Visit Recall
   Treatment Precision
***
**
***
***
***
***
***
***
***
***
***
**
***
**
***
*
**
***
n.s.
n.s.
***
***
***
***
***
***
***
***
***
*
n.s.
*
**
Baseline ResidencyRL
Figure 5|AMIE Mx criteria scores. Comparison of normalized scores for 60 sub-metrics across the
six clinical rubrics between the Baseline model (Gemini 3.5 Flash, blue) and the ResidencyRL-trained
model (red). Bars represent mean scores across𝑁=120unique multi-visit scenarios covering360
simulated telemedicine encounters. Error bars represent 95% confidence intervals computed via
bootstrapping (n=1000) over clinical scenarios. Statistical significance was evaluated using a two-
sided paired Wilcoxon Signed-Rank test with FDR correction (annotated to the right of each metric:
***:𝑝 <0.001, **:𝑝 <0.01, *:𝑝 <0.05, n.s.: not significant,𝑝≥0.05).
and Care Excellence, 2026). Each scenario spans three consecutive visits: typically an initial en-
counter (history-taking, differential diagnosis, preliminary investigations and recommendations), a
follow-up (response assessment, plan adjustment), and a continued management visit (treatment
evaluation, long-term planning), yielding 360 evaluation examples. The agent interacts in conversa-
tional dialogue with a simulated patient. This simulation includes a structured tool API for retrieving
booking information with patient information and test results and for submitting a post-encounter
clinical questionnaire comprising differential diagnosis, management plan with guideline citations,
investigations, treatments, and follow-up recommendations. Performance is assessed by a Gemini
3.1 Pro-based autorater across six rubric categories encompassing 60 axes, reproducing the evalu-
ation instrument validated against 20 primary care physicians in the original study (Liévin et al.,
2026): management reasoning (MXEKF, 10 axes), guideline adherence (8 axes), preciseness and
inter-visit memory (3 axes), patient communication (GMPCQ, 11 axes), clinical skills (PACES, 16
axes), and diagnosis and management (12 axes). For each individual criterion, the categorical rubric
ratings (e.g., Likert 1–5 scales or binary checkboxes) are normalized to a 0–1 range by mapping the
worst/minimum possible score to 0 and the maximum to 1, before computing overall category av-
18

ResidencyRL: Reinforcement Learning in Simulated Clinical Environments
erages. The autorater receives the relevant clinical guideline documents as reference when scoring
guideline-related rubric sections, ensuring that assessments reflect adherence to the specific recom-
mendations each scenario was designed around. Statistical significance of the observed differences
between models across the 120 independent multi-visit patient scenarios was determined using a
two-sided Wilcoxon signed-rank test with Benjamini-Hochberg False Discovery Rate (FDR) correc-
tion, alongside 95% confidence intervals computed via scenario-level bootstrapping (N=1000).
We find that the ResidencyRL-trained agent outperforms the Gemini 3.5 Flash base model across
all six evaluation categories (Table 5 and Figure 5). Management reasoning (MXEKF) improved
from 80.1% to 88.4% (95% CI for difference [+7.33%, +9.38%]), reflecting better illness-specific
knowledge, more appropriate ongoing monitoring and adjustment, and stronger prognostication.
Guideline adherence improved from 84.2% to 86.7% (95% CI for difference [+0.52%, +4.48%]),
driven by gains in treatment and investigation guideline reference support. Preciseness and inter-
visit memory, which measures recall of information from prior visits, showed a minor improvement
from90.0%to92.7%(95%CIfordifference[+0.59%, +4.64%]), withagainintreatmentprecision
from72.1%to 83.6%(95%CIfor difference[+6.09%, +17.46%]). Clinical skills(PACES)improved
from 79.6% to 84.8% (95% CI for difference [+4.29%, +6.25%]), with consistent gains observed
across all underlying criteria, indicating higher quality and more thorough history-taking during
clinical interactions. Patient communication (GMPCQ) also improved significantly from 83.7% to
92.2% (95% CI for difference [+7.27%, +9.74%]). Performance was consistent across visit stages:
with the ResidencyRL-trained agent overall scoring 89.3%, 89.3%, and 89.1% at Visits 1, 2, and 3,
and the base model scoring 85.0%, 85.3%, and 83.7%.
4.3. Application to specialist oncology care
Wenextevaluatewhethertheimprovementsobservedonprimarycaretelehealthtransfertospecialist-
levelcare. Clinicalexpertscurated𝑁=300oncologycasesdesignedaspatient-to-specialisttelemedicine
encounters(findmoredetailsondatacollectioninAppendixD).Thecasesspan240solidtumorcases
across21cancer types (e.g., breast, prostate, colorectal, lung) and60hematological malignancies
across10subtypes(e.g., non-Hodgkinlymphoma, multiplemyeloma, acutemyeloidleukemia), each
case paired with hospitalist-authored ground-truth labels for initial management, urgency, and care
setting (per-stratum counts are given in Appendix D). The referring physician’s workup (physical
examination findings, laboratory results, imaging, and medications) is accessible via areview re-
ferraltool, but the agent must also independently gather clinical history from the patient through
dialogue, and upon completion submit structured outputs: a differential diagnosis, a management
plan, an urgency assessment, and a disposition recommendation. The simulation uses the same pa-
tient simulator architecture described in Section 3, adapted for the specialist consultation setting.
The agent was never exposed to oncology cases or specialist workflows during training, although
most tool-calling conventions are shared with the telehealth API (Section 3).
Quantitativeevaluation.CompletedencountersarescoredbyGemini3.1Proagainstgold-standard
management plans written by specialist oncologists, using six weighted clinical axes (Appendix D).
We report head-to-head win rates across scenarios (the proportion of cases where one model scores
strictly higher than the other) and evaluate statistical significance on paired rubric scores using two-
sided Wilcoxon signed-rank tests with Benjamini–Hochberg FDR correction. Both models performed
similarly onCase Relevance(win:loss=7.4%vs.7.1%,𝑝=0.84, n.s.) andSafety & Triage(11.1%vs.
6.8%,𝑝=0.21, n.s.), where differences were rare (Figure 6). The ResidencyRL-trained agent won
significantly more often on the remaining four axes:Completeness(34.8%vs.10.5%,𝑝 <0.001),
Clinical Accuracy(26.0%vs.9.1%,𝑝 <0.001),Actionability(21.6%vs.7.8%,𝑝 <0.01), and the
Overallcomposite (42.9%vs.18.6%,𝑝 <0.001; axis weights in Appendix D).
19

ResidencyRL: Reinforcement Learning in Simulated Clinical Environments
0% 25% 50% 75% 100%
Scenario Proportion (%)
Safety & Triage
Completeness
Clinical Accuracy
Case Relevance
Actionability
Overall
82% n.s.
55% 35% ***
65% 26% ***
85% n.s.
71% 22% **
19% 39% 43% ***
Win : Baseline Tie ResidencyRL
Figure 6|Specialist oncology auto-evaluation.
Scenario-level comparison between Baseline
(Gemini 3.5 Flash, blue) and the ResidencyRL-
trained model (red) across𝑁=300oncology
scenarios. Bars represent the proportion of sce-
narios where each model scored higher (Win) or
tied (Tie, gray). Statistical significance: two-sided
paired Wilcoxon signed-Rank test with FDR cor-
rection (***:𝑝 <0.001, **:𝑝 <0.01, *:𝑝 <0.05,
n.s.: not significant,𝑝≥0.05).
Oncologist review.A subset of𝑁=100cases
werereviewedbyboard-certifiedoncologistsin
a blinded comparison against the Gemini 3.5
Flash baseline. Compared to the baseline, the
ResidencyRL-trained agent elicited more tar-
geted histories, identified red-flag symptoms
earlier, and more systematically inquired about
exposure, family, and genetic risk factors. Dif-
ferential diagnoses were more frequently prior-
itized by clinical likelihood and urgency, with
clearer reasoning for and against each con-
sideration, and responses more consistently
distinguished immediate actions from routine
evaluation and escalation criteria. The agent
also more reliably outlined the expected se-
quence, purpose, and interpretation of further
workup, including when more invasive investi-
gations might be warranted, which may help
reduce patient uncertainty during an ongo-
ing diagnostic evaluation. However, a recur-
ring failure mode was asking multiple ques-
tions within a single turn; although clinically
relevant, this may overwhelm patients, partic-
ularly those processing a new or possible can-
cer diagnosis, and reduce the completeness of
their responses.
4.4. Improvement on external agentic clini-
cal benchmarks
To assess whether skills acquired through ResidencyRL training transfer beyond the training envi-
ronment, we evaluated the ResidencyRL-trained agent on two established external benchmarks that
share no training data, patient simulation architecture, or evaluation protocol with ResidencyRL:
AgentClinic (Schmidgall et al., 2024) and CRAFT-MD (Johri et al., 2025). The two benchmarks test
complementary aspects of clinical competence. AgentClinic evaluates dynamic multi-turn diagnostic
dialogue under realistic interaction constraints; CRAFT-MD provides a controlled setting to analyze
multi-turn conversational reasoning and information integration across matched cases. Results are
shown in Table 6.
AgentClinic: diagnostic accuracy and the mitigation of premature closure.Premature closure,
the tendency to anchor on an initial hypothesis and terminate information gathering too early, is
the most frequently implicated cognitive error in diagnostic failure (Croskerry, 2002; Graber et al.,
2005). AgentClinic provides a direct test of whether ResidencyRL training mitigates this failure
mode, because its multi-agent simulation requires the model to actively drive the diagnostic conver-
sation, deciding at each turn whether to ask another question or commit to a diagnosis.
We evaluated the ResidencyRL-trained agent against the Gemini 3.5 Flash baselineon two Agent-
Clinic scenario sets. On AgentClinic-MedQA (𝑛=215scenarios derived from USMLE-style clinical
vignettes), the ResidencyRL-trained agent achieved 85.6% diagnostic accuracy (95% CI: [80.9%,
90.2%]) compared to 81.4% for the base model (95% CI: [76.3%, 86.5%]), a directional improve-
20

ResidencyRL: Reinforcement Learning in Simulated Clinical Environments
Table 6|Out-of-domain evaluation.Evaluating the ResidencyRL-trained model against baseline on
AgentClinic and CRAFT-MD (95% bootstrap CI).
Dataset Metric Baseline ResidencyRL
AgentClinic-MedQA Diagnostic Accuracy (𝑛=215) 81.4%[76.3, 86.5]85.6%[80.9, 90.2]
AgentClinic-MIMIC-IV Diagnostic Accuracy (𝑛=200) 53.5%[46.5, 60.5]60.0%[53.0, 66.5]
CRAFT-MD Visit Free-Response (Vfrq) 81.3%[79.5, 82.9]84.5%[82.4, 86.4]
Consultation Free-Response (Cfrq) 58.1%[55.9, 60.3]62.8%[60.1, 65.5]
Visit Multiple Choice (Vmcq) 94.2%[93.1, 95.2]93.7%[92.2, 94.9]
Consultation Multiple Choice (Cmcq) 82.4%[80.7, 84.0]84.0%[81.9, 86.0]
Summary Multiple Choice (Smcq) 83.5%[81.8, 85.1]84.7%[82.6, 86.6]
ment of+4.2 percentage points, though this difference did not reach statistical significance (𝑝=
0.176, McNemar exact test). On AgentClinic-MIMIC-IV (𝑛=200scenarios derived from real patient
encounters in the MIMIC-IV discharge database), the ResidencyRL-trained agent achieved 60.0%
diagnostic accuracy (95% CI: [53.0%, 66.5%]) compared to 53.5% for the base model (95% CI:
[46.5%, 60.5%]), a directional improvement of+6.5 percentage points (𝑝=0.079, McNemar exact
test). Notably, the ResidencyRL-trained agent also conducted longer consultations on AgentClinic-
MIMIC-IV (15.8 vs. 11.2 average turns), consistent with the more thorough history-taking behavior
observed in the in-domain evaluations. These trends are notable given that the ResidencyRL-trained
agent was never exposed to AgentClinic scenarios, patient simulation architecture, or evaluation pro-
tocol during training, and are directionally consistent with the significant improvements observed
on in-domain evaluations and AMIE Mx.
CRAFT-MD:multi-turndiagnosticreasoning.TheCRAFT-MDbenchmark(Johrietal.,2025)evalu-
ates diagnostic accuracy undertwo information conditions crossed with two response formats. In the
Visitcondition, the model receives a complete clinical vignette and must diagnose from static infor-
mation; intheConsultationcondition, themodelmustactivelygatherinformationthroughmulti-turn
dialogue with a simulated patient before diagnosing. Each condition is evaluated in both multiple-
choice and free-response formats, with an additional summary multiple-choice condition. This2×2
design (plus summary) isolates the contribution of active information gathering from static clinical
knowledge.
The ResidencyRL-trained agent showed consistent directional improvements over the base model
on the sub-metrics that most directly require active clinical reasoning and information integration,
though none reached statistical significance individually. The pattern of gains is informative: im-
provements were largest in the free-response formats that require the agent to construct its own
diagnostic assessment, and smallest in the structured multiple-choice formats that test recognition
rather than generation.
On the most clinically demanding sub-metric, Consultation Free-Response (Cfrq), where the
model must generate a free-text diagnosis after conducting its own history-taking, the ResidencyRL-
trained agent achieved 62.8% accuracy (95% CI: [60.1%, 65.5%]) compared to 58.1% for the base
model (95% CI: [55.9%, 60.3%]), a+4.7 percentage point directional gain. Visit Free-Response
(Vfrq) accuracy trended upward from 81.3% (95% CI: [79.5%, 82.9%]) to 84.5% (95% CI: [82.4%,
86.4%]), a+3.2 pp gain. Consultation Multiple Choice (Cmcq) rose from 82.4% (95% CI: [80.7%,
84.0%]) to 84.0% (95% CI: [81.9%, 86.0%]), and Summary Multiple Choice (Smcq) from 83.5%
(95% CI: [81.8%, 85.1%]) to 84.7% (95% CI: [82.6%, 86.6%]). Visit Multiple Choice (Vmcq), the
most structured and least conversationally demanding format, was the only sub-metric where the
base model held a marginal edge (94.2%, 95% CI: [93.1%, 95.2%] vs. 93.7%, 95% CI: [92.2%,
94.9%]), with broadly overlapping confidence intervals.
21

ResidencyRL: Reinforcement Learning in Simulated Clinical Environments
The pattern of directional gains across both AgentClinic scenario sets and CRAFT-MD sub-metrics
is consistent: the largest improvements emerge in settings that demand the agent actively gather
information and construct its diagnostic assessment, rather than selecting from pre-specified options
or diagnosing from a static vignette. While these individual comparisons did not reach statistical
significance, the consistency of the directional improvements across both benchmarks and across
sub-metrics that emphasize active reasoning suggests that multi-turn RL develops transferable skills
in information gathering and diagnostic synthesis. Larger-sample evaluations would be needed to
confirm this trend.
4.5. Generalization to out-of-domain clinician-curated telehealth scenarios
Figure 7|AMIE Telehealth simulation scores. Comparison of automated rubric scores between
the baseline model (Gemini 3.5 Flash, blue) and the ResidencyRL-trained model (red) across out-
of-domain telehealth simulations. Bars represent mean scores across𝑁=299simulated clinical
scenarios (evaluated on a 1–5 scale), with per-scenario scores averaged across3independent sim-
ulation runs. Error bars represent 95% confidence intervals computed via bootstrapping (n=1000)
over clinical scenarios. Statistical significance was evaluated using a two-sided paired Wilcoxon
Signed-Rank test with FDR correction (annotated above each metric: ***:𝑝 <0.001, **:𝑝 <0.01,
*:𝑝 <0.05, n.s.: not significant,𝑝≥0.05).
The preceding evaluations (Sections 4.1–4.4) rely primarily on synthetically generated scenarios
and automated scoring with the basic tool-calling interface from training. This section introduces
an out-of-domain evaluation with three key differences: scenarios are designed and validated by
expert clinicians, model outputs are graded by a blinded panel of board-certified physicians, and
both models are deployed within an expert-optimized agentic harness extending the AMIE lineage
(Brodeur et al., 2026; Liévin et al., 2026; Saab et al., 2026; Tu et al., 2025; Vedadi et al., 2025).
This last element raises a critical question: whether the improvements from ResidencyRL training
22

ResidencyRL: Reinforcement Learning in Simulated Clinical Environments
persist, or are rendered redundant, when both models operate within a system already engineered
to maximize clinical performance. To answer this, we introduce an out-of-domain (OOD) telehealth
evaluation built on two pillars:
1.Expert-curatedclinicalscenarios.TheOODevaluationdatasetcomprises299clinicalscenar-
ioscollectedwithapanelofboard-certifiedclinicians. Forthesecases, adiversesetofclinicians
designed patient presentations that they deemed important and representative and interacted
with a Gemini-based patient simulator to produce reference encounter trajectories. These tra-
jectories define the patients’ clinical history, disclosure sequence, and behavioral profile for
subsequent re-simulation with other models. Cases span a broad range of specialties (gen-
eral primary care, ENT, neurology, musculoskeletal, gastrointestinal, respiratory, cardiovascu-
lar, genitourinary, and psychiatry) and feature nuanced clinical presentations with complex
psychosocial dynamics, ranging from routine encounters to advanced conditions warranting
specialty-level follow-up.
2.Controlled comparison within an agentic harness.Performance of clinical agents reflects
boththeunderlyingmodel’scapabilitiesandtheagenticscaffoldinginwhichitoperates,includ-
ing system prompts, tool orchestration, multi-phase interaction design, and structured clinical
documentation workflows. To isolate the specific contribution of ResidencyRL, we deploy both
the base model (Gemini 3.5 Flash) and the ResidencyRL-trained model within the identical
AMIE Telehealth Harness, a novel expert-optimized clinical agentic framework originally de-
velopedandtunedonthebasemodel. Thisdesignmirrorsthebase-vs-trainedcomparisonfrom
Section 4.1, but under strictly harder conditions: the harness already compensates for many
of the base model’s weaknesses, raising the performance floor against which the RL-trained
model must demonstrate improvement. Any observed gain therefore represents the additive
benefit of ResidencyRL training on top of expert agentic engineering.
Protocol.The AMIE simulation infrastructure uses a dynamic setup in which an LLM-conditioned
Patient Agent interacts with the Doctor Agent (under test). The Patient Agent is instructed to with-
hold critical information unless properly questioned, mirroring real-world progressive disclosure.
The resulting encounters are evaluated with two methods:
1.Automated grading.Five LLM autoraters and two heuristic evaluators assess each encounter.
The LLM autoraters evaluate Management Appropriateness across five clinical axes (urgency,
investigation, treatment, follow-up, and overall quality), Clinical Safety, Diagnostic Appropri-
ateness, Conversational Style, and case-specific clinical rubrics tailored to each of the 299 sce-
narios. All autoraters operate as structured Gemini requests, with per-scenario scores averaged
across three independent runs. The detailed scoring methodology, calibration rules, and rep-
resentative examples of case-specific rubrics are provided in Appendix C.
2.Expert clinician grading (side-by-side).To ground the automated metrics and uncover nu-
anced clinical blind spots, a panel of board-certified physicians reviewed complete encounter
pairs across a representative subset of100scenarios. Interactions from the base model and
ResidencyRL-trained model were presented in randomized, anonymized order as “Model A”
and“ModelB”.Encounterswereratedona5-pointcomparativepreferencescale(from“ModelA
is much better” to “Model B is much better”) covering eight clinical, safety, and communica-
tion dimensions. Three of the sampled scenarios were excluded from analysis due to simulator
trajectory discrepancies, leaving𝑛=97valid evaluations.
3.Qualitative case studies.To illustrate how quantitative differences in clinical competencies
manifest in real-time patient interactions, we extract and compare complete encounter trajec-
tories between the base and trained models on representative clinical cases (Appendix F).
23

ResidencyRL: Reinforcement Learning in Simulated Clinical Environments
Automated grading.Across the full299-case automated evaluation (Figure 7), the ResidencyRL-
trained agent demonstrated broad and statistically significant improvements, with 8 of 10 met-
rics reaching significance after FDR correction (𝑝adj <0.05, two-sided paired Wilcoxon signed-
rank test with Benjamini-Hochberg correction). The largest gains were observed in Naturalness
(2.52→3.24,Δ=+0.73,𝑝 <0.001) and Overall Clinical Rubric Score (3.93→4.43,Δ=+0.50,
𝑝 <0.001), indicating that ResidencyRL training substantially improves both conversational qual-
ity and aggregate clinical performance. Within the management axes, the trained model exhibited
significant gains in Treatment (4.43→4.61,Δ=+0.18,𝑝 <0.001), Overall management quality
(4.72→4.82,Δ=+0.10,𝑝 <0.05), and Follow-up (4.78→4.88,Δ=+0.10,𝑝 <0.01). Investiga-
tion (4.75→4.83) and Urgency (4.74→4.80) showed directional improvements that did not reach
statistical significance. The Safety Score improved from4.73to4.80(𝑝 <0.05), and the composite
Stylescorefrom3.99to4.13(𝑝 <0.001), confirmingthatthemodel’sincreasedclinicalrigordidnot
compromise the quality of the patient interaction. Diagnostic Appropriateness approached ceiling
(4.98→5.00,𝑝 <0.05), reflecting strong baseline diagnostic performance with a small but signif-
icant gain. These results confirm that the clinical improvements from ResidencyRL training persist
even when both models operate within an expert-optimized agentic harness.
40
 20
 0 20 40 60 80 100
Percentage of Ratings (%)
Overall Impression
Mgmt Plan
Appropriateness
Mgmt Plan Safety
Diagnostic
Assessment
Completeness of
Info Gathering
Empathy & T one
Naturalness &
Conv/Note T one
No Hallucinations
8% 42% 45%
6% 19% 52% 24%
55% 27% 15%
8% 26% 35% 31%
6% 35% 56%
7% 62% 18% 12%
49% 36% 11%
9% 77% 6% 6%
***
***
***
***
***
***
***
n.s.
Baseline much better Baseline slightly better Equal quality ResidencyRL slightly better ResidencyRL much better
Figure 8|Distribution of human rater preference ratings.Results from a blinded SxS evaluation
of𝑛=97cases, comparing the Baseline model (Gemini 3.5 Flash, blue) and the ResidencyRL-trained
model (orange) across various clinical axes. Statistical significance was evaluated using a two-sided
paired Wilcoxon Signed-Rank test with FDR correction (annotated to the right of each metric: ***:
𝑝 <0.001, **:𝑝 <0.01, *:𝑝 <0.05, n.s.: not significant,𝑝≥0.05).
Expert clinician grading (side-by-side).The evaluation results (Figure 1h and Figure 8) reveal a
strong and consistent clinician preference for the ResidencyRL-trained model across all evaluated
dimensions. InOverall Impression, clinicians preferred the ResidencyRL-trained model in 87.6% of
cases (versus 10.3% for Baseline, with only 2.1% ties), yielding a mean preference score of +1.21
on the[−2,+2]scale (95% CI: [+1.01, +1.39]). This effect was most pronounced inCompleteness of
InformationGathering, where90.7%ofratingsfavoredthetrainedmodel(mean: +1.42, CI:[+1.26,
+1.57]), confirming that ResidencyRL training produces substantially more thorough history-taking
behavior.
Within core clinical competencies, the trained model demonstrated large advantages inMan-
agement Plan Appropriateness(75.3% win rate, mean: +0.93, CI: [+0.76, +1.08]) andDiagnostic
24

ResidencyRL: Reinforcement Learning in Simulated Clinical Environments
Assessment(66.0% win rate, mean: +0.89, CI: [+0.70, +1.07]). ForManagement Plan Safety—
arguably the most critical dimension—the trained model was preferred or tied in 96.9% of cases
(42.3% wins, 54.6% ties, only 3.1% losses), with a mean score of +0.53 (CI: [+0.36, +0.69]). The
high tie rate reflects the reassuring finding that both models rarely commit overt safety violations,
while the trained model further reduces the already-low rate of unsafe recommendations.
Importantly, these clinical gains were achieved without sacrificing communication quality. InEm-
pathy & Tone, the trained model was preferred in 29.9% of cases with only 8.2% losses (62% ties,
mean: +0.33, CI: [+0.16, +0.49]).Naturalness & Conversational Toneshowed a similar positive
skew (47.4% wins vs. 3.1% losses, mean: +0.56, CI: [+0.41, +0.70]). The one dimension ap-
proaching parity wasAccuracy (No Hallucinations), where 77.3% of ratings were ties (mean: +0.07,
CI: [−0.06, +0.21])—indicating that both models exhibit comparably low hallucination rates, and
that ResidencyRL training does not introduce factual degradation.
All dimensions except Accuracy (No Hallucinations) showed statistically significant preference
for the ResidencyRL-trained model (two-sided Wilcoxon signed-rank test with Benjamini-Hochberg
FDR correction; all𝑝 adj <0.001), while Accuracy showed no significant difference (𝑝adj =0.229),
confirming that ResidencyRL training does not introduce factual degradation.
Finally, clinicians assessed the realism of the simulated patient interactions. 99/100 encounter
cases are judged as realistic in both arms, confirming that the simulation infrastructure provides a
faithful proxy for clinical encounters and that neither model’s conversational style appeared artificial
or stilted.
Taken together, these blinded expert evaluations provide strong human-grounded validation of
the automated metrics: ResidencyRL training produces agents that are not only quantitatively supe-
rior on rubric-based autorater scores, but are consistently preferred by practicing clinicians across
the full spectrum of clinical and communicative competencies.
Case studies: comparative analysis of clinical performance.To illustrate the specific behav-
ioral differences driving these expert preference ratings, we detail several representative clinical
encounters. In side-by-side comparisons, reviewing physicians observed distinct shifts in how the
ResidencyRL-trained model navigated complex patient dynamics. These cases highlight how multi-
turn RL training mitigates common failure modes of base language models.
•Anchoring on self-diagnosis vs. Enforcing safety constraints (Appendix F.1).Confronted
by a patient demanding high-risk abdominal surgery for a self-diagnosed “fistula,” thebase
modelanchoredontheinitialpatientclaimandomittedessentialsafetychecks. TheResidencyRL-
trained modelactively probed the illogical request, identified the suspected psychosomatic un-
dertones, andpersistently requested mandatory pregnancy screeningdespite repeated de-
flections by the patient. A reviewing physician specifically praised this persistence as a critical
safety catch.
•Clinical hallucination vs. Systematic elicitation under pressure (Appendix F.2).In a time-
sensitive neurological emergency (Transient Ischemic Attack), thebase modelprematurely ter-
minated the encounter after a single question to advise emergency care. It subsequentlyhallu-
cinated a fabricated medical historyto fill in the missing information in its clinical note. The
ResidencyRL-trained modelresolved this tension by systematically eliciting the patient’s actual
vascular risk factors and family history without meaningfully delaying emergency escalation.
Thisprovidedactionableclinicalcontextandeliminateddangerousdownstreamhallucinations.
Full scenario descriptions, transcripts, and clinician rater rationales are provided in Appendix F.
25

ResidencyRL: Reinforcement Learning in Simulated Clinical Environments
5. Discussion
While language models demonstrate strong medical knowledge, mastering clinical practice demands
more: sequential information gathering, hypothesis refinement, and uncertainty management in the
presence of a patient. ResidencyRL develops these competencies through multi-turn reinforcement
learning in simulated patient encounters, yielding measurable improvements in diagnostic accuracy,
management quality, and patient-centered communication. These improvements generalize to five
evaluation frameworks (AMIE Mx, oncology cases, AgentClinic, CRAFT-MD, and clinician-curated
telehealth simulations), each with different clinical scenarios, interaction protocols, and evaluation
rubrics. We examine these results in detail below.
Clinical competence demands long horizons.A complete clinical encounter follows a natural
phased structure: rapport building, systematic history-taking, focused investigation, diagnostic syn-
thesis, managementplanning, anddocumentation. Capturingthisfullarcrequiresextendedtraining
horizonsandarichactionspace: ResidencyRLoptimizesoverupto𝑇=68actions(60dialogueturns
and 8 clinical tool calls for diagnosis, management, and documentation; Section 3.2), enabling the
agent to learn when to transition between clinical phases, how to recover from unproductive lines
of questioning, and how to manage patient dynamics that unfold gradually. Unlike supervised fine-
tuning, which would require curated expert trajectories, RL discovers these strategies through its
own exploration. Over training, median encounter length grows from 18 to 23 turns as the policy
learns to invest in thorough history-taking before committing to a diagnosis and plan (Figure 4).
Scenariodesignsteersclinicalcompetencies.Training includes capability-specific scenarios (Sec-
tion 3.1), whose influence is reflected in the pattern of downstream improvements. The history-
taking environments, which reward thorough elicitation, coincide with the fastest-improving dimen-
sionunderRL:intakecompleteness(Section3.4). Inpractice, thetrainedagentprobesbehindstated
requestsratherthanacceptingthematfacevalue; inonecasestudy(AppendixF),theagentconducts
a focused 10-turn intake to gather critical vascular risk factors before escalating care, which the base
model fails to elicit. Completeness of information gathering was the single strongest axis of clinician
preference in blinded evaluation (90.7% win rate; Section 4.5). Premature closure, the cognitive
error most frequently implicated in diagnostic failure (Croskerry, 2002; Graber et al., 2005), is sub-
stantially reduced: missed critical questions and missed red flags both decrease by roughly one third.
Premature closure leaves a gap easily filled with hallucination: in the TIA scenario (Appendix F.2),
the base model terminates after five exchanges and fabricates a medical history it never gathered.
The adversarial safety scenarios, which expose the agent to complex communication styles mim-
icking the realities of obtaining medical histories, coincide with reductions in missed red flags and
near-universal safety preference (96.9% preferred or tied; Section 4.5). The fistula case study (Ap-
pendix F) illustrates: the patient demands an exploratory laparotomy for a self-diagnosed fistula; the
base model accepts this framing, while the trained agent probes the claim until the patient admits
no fistula exists and the real clinical picture emerges.
Procedural generalization.The competencies shaped by training (thoroughness of clinical inves-
tigation, management reasoning, patient communication, and safety) transfer consistently across
evaluation frameworks (Sections 4.2 and 4.4). Although the simulated scenarios in training are
derived from primary and acute care settings from DDXPlus, we observed transfer to specialist on-
cology cases (Section 4.3) and to multi-visit longitudinal care (Section 4.2), neither of which were
encountered during training, suggesting that the improvements are in clinical process rather than
domain-specific knowledge.
While the automated evaluation pipeline has known limitations (including positive bias toward
the trained model and metric saturation; Appendix C.7), the consistent generalization pattern pro-
26

ResidencyRL: Reinforcement Learning in Simulated Clinical Environments
vides evidence against pure reward hacking. This is independently verified by the clinician side-by-
side evaluation (Section 4.5), which confirms that the quantitative gains do not mask degradations
in safety or communication quality. These gains compound with expert scaffolding: clinicians prefer
the ResidencyRL model in 87.6% of blinded comparisons even when both models operate within the
AMIE telehealth harness, a clinical framework already engineered to maximize base-model perfor-
mance (Section 4.5). That multiple independent efforts have converged on multi-turn RL for clinical
dialogue (Feng et al., 2026; Gao et al., 2026; Lai et al., 2025; Qiu et al., 2025) reinforces the gener-
ality of this finding across model families, scales, and clinical domains.
Taken together, these results point to a broader principle: simulation provides diverse, adversar-
ial, and extended encounters that force the agent to practice deploying its existing knowledge under
realistic clinical pressure. The competencies that emerge are procedural (how to gather information,
when to probe further, how to manage clinical uncertainty), and hence transfer beyond the training
distribution. This finding is also relevant to the verifiability frontier for RL (Guo et al., 2025; Light-
man et al., 2023): unlike mathematics or code, clinical encounter quality is assessed during training
through proxy metrics rather than definitive patient outcomes, making the reward signal inherently
softer and more susceptible to overoptimization (Gao et al., 2022). The transfer results reported
above suggest that structured, multi-axis LLM verification (grounded in the calibration properties of
large models; Kadavath et al. (2022)) can nonetheless serve as a productive training signal, though
the short training horizon leaves open how far soft verification can scale.
Limitations.All training is confined to text-based telehealth consultations, a narrow slice of clinical
practice, whereas real-world healthcare spans the full breadth of the system—from emergency triage
and surgical decision-making to chronic disease management and end-of-life care, each with distinct
interaction dynamics, safety requirements, and cultural contexts (here, only English-speaking, US-
based patients were simulated). All training encounters are single-visit, with management quality
judged by the autorater rather than validated against long-term patient outcomes. Real clinical
reasoning integrates sensory inputs (physical examination, vocal tone, facial expressions) with mul-
timodal data (imaging, laboratory results, physiological monitoring) across channels that text-based
simulation cannot access (Saab et al., 2026; Shah et al., 2026). Beyond this sensory gap, the interac-
tion itself is narrower: the agent can order tests and prescribe treatments through its management
plan, but never receives results, performs physical procedures, or coordinates in real time with other
providers.
On the evaluation side, the autorater illustrates a form of Goodhart’s law (Gao et al., 2022):
when a measure becomes a target, it ceases to be a good measure. The autorater’s correlation with
clinician judgment validates its use as a training signal, but it exhibits systematic positive bias toward
the trained model (Appendix C.7), and several metrics approach saturation at the top of the scale,
limiting the rubric’s ability to resolve quality differences at the frontier. Scaling verification compute
through cross-sample strategies such as pairwise tournaments (Gottweis et al., 2025; Kwok et al.,
2026; Tu et al., 2025) and co-evolving the verifier with the policy (Yuan et al., 2024) may raise this
ceiling, but external clinical grounding remains necessary to prevent convergence to shared blind
spots. The adversarial safety evaluations used automated adversarial agents rather than human
actors, and the proprietary training infrastructure limits full reproducibility, although evaluation
methodologies and rubric specifications will be made available.
More broadly, the fidelity gap between simulated and real patients persists: configurable be-
havioral parameters and adversarial fidelity checks narrow but do not eliminate the discrepancy
between our system and the full communicative complexity of human encounters. Yet clinicians
judged the vast majority of telehealth encounters as realistic (Section 4.5), suggesting the current
level of simulation fidelity is sufficient to develop transferable competencies. Whether simulation-
27

ResidencyRL: Reinforcement Learning in Simulated Clinical Environments
trained competencies transfer reliably to real patient care remains an open question: standardized
human OSCE evaluation (Tu et al., 2025) and prospective clinical studies (Brodeur et al., 2026) are
necessary to answer it.
Future Directions.Richer simulations may unlock stronger clinical agents. First, clinical coverage:
the training curriculum can expand across the healthcare system and beyond patient-doctor conver-
sations to multi-actor and multi-system interactions involving caregivers, interpreters, and specialist
teams. New environments require design effort and grounding data, but LLMs accelerate the devel-
opment of environments and scenarios. Second, simulation fidelity: grounding patient simulators
in electronic health record data (Fleming et al., 2024) would increase clinical realism, while multi-
modal simulation incorporating imaging, laboratory results, and physiological signals (Shah et al.,
2026) would enrich the channels available to the agent. Enabling the agent to observe the down-
stream effects of its clinical decisions, how a patient responds to a prescribed treatment (Mu et al.,
2026), would close the loop between management planning and outcome observation. Third, tem-
poral horizon: extending training from single-visit encounters to multi-visit longitudinal trajectories
wouldallowtheagenttolearnsustainedclinicalreasoning, trackingevolvingpatientstatesandman-
aging chronic conditions over time. ResidencyRL is a first step: as simulation grows richer, so will
the competencies it develops.
6. Conclusion
We introduced ResidencyRL on the premise that clinical mastery, for AI as for physicians, is devel-
oped through practice. The framework trains AI agents through simulated patient encounters under
a composite reward that targets accuracy, management quality, patient communication, and safety.
The resulting agent consistently outperforms its base model in blinded clinician evaluation, particu-
larly in the thoroughness of its history-taking and its resilience to unsafe diagnostic shortcuts under
adversarial conditions. Because these gains transfer to out-of-domain evaluation frameworks and
unseen specialties like oncology, they provide evidence that multi-turn RL develops adaptable clini-
cal capabilities rather than simply overfitting to a training signal. The gap between simulation and
clinical practice remains substantial, and narrowing it along the axes of clinical coverage, simulation
fidelity, and temporal horizon is the central challenge ahead. Yet the core finding stands: a fron-
tier model that already possesses broad medical knowledge can be made into a meaningfully more
competent and helpful clinician through reinforcement learning in simulation.
Acknowledgments
This project was an extensive collaboration between many teams at Google for Health, Google Deep-
Mind, and Google Research. We thank Andrew Sellergren for their feedback and insight, which
significantly enhanced this paper. We thank Angelos Filos, Nigamaa Nayakanti, Chenkai Kuang,
Guangda Lai, Evan Liu, Gregory Thornton, Yuan Liu, Sidharth Mudgal, Huan Gui, Machel Reid,
YaGuang Li, Isabel Gao, Laurent El Shafey, Xiaomeng Yang, Adams Yu, Hanzhao Lin, Piotr Stanczyk,
Tal Schuster, Adam Zhang, Vincent Hellendoorn, Trieu Trinh, Kate Baumli, Jonathan Lee, Paul Cov-
ington, Ruoxin Sang, Mantas Pajarskas, Alex Tomala, Philipp Fränken, Da Huang, Garrett Bingham,
Mandy Guo, Avi Singh, Maciej Kula, Junwen Yao, Jonathan Coe, Dawsen Hwang, Irene Cai, Minmin
Chen, Yi Tay, Kareem Mohamed, Qianli Zhu, Qijun Tan, George-Cristian Muraru, Jian Li, Thang Lu-
ong, Pol Moreno, Shunyu Yao, Lisa Lee, Justin Pan, Julien Amelot, Hongkun Yu for their technical
support and feedback during our research. Finally, we are grateful to Sara Mahdavi, Joe Giancristo-
faro, Rachelle Sico, Cat Kozlowski for their support during the course of this project.
28

ResidencyRL: Reinforcement Learning in Simulated Clinical Environments
Data Availability
Many of the datasets used in the development of ResidencyRL were open-source (DDxPlus, Agent-
Clinic, CRAFT-MD, and AMIE Mx).
Code Availability
Our system utilizes Gemini 3.5 Flash (Gemini Team Google, 2026b) as its base foundation model
and Gemini 3.1 Pro (Gemini Team Google, 2026a) for auto-rating and case generation. Gemini
models are generally available via Google Cloud APIs. However, the specific implementation relies
on internal Google infrastructure and tooling. Due to these system dependencies and the safety im-
plications associated with the unmonitored deployment of autonomous AI agents in clinical contexts,
the internal training codebase and model weights are not publicly released. In the interest of respon-
sible innovation, we will be working with research partners, regulators, and healthcare providers to
further validate and explore safe onward uses of our medical models.
Competing Interests
This study was funded by Alphabet Inc and/or a subsidiary thereof (‘Alphabet’). Authors who are
employees of Alphabet may own stock as part of the standard compensation package.
References
R. K. Arora, J. Wei, R. S. Hicks, P. Bowman, J. Quiñonero-Candela, F. Tsimpourlas, M. Sharman,
M. Shah, A. Vallone, A. Beutel, et al. Healthbench: Evaluating large language models towards
improved human health.arXiv preprint arXiv:2505.08775, 2025.
V. Balazadeh, M. Cooper, D. Pellow, A. Assadi, J. Bell, M. Coatsworth, K. Deshpande, J. Fackler,
G. Funingana, S. Gable-Cook, et al. Red teaming large language models for healthcare.arXiv
preprint arXiv:2505.00467, 2025.
H. S. Barrows. An overview of the uses of standardized patients for teaching and evaluating clinical
skills.Academic Medicine, 68:443–451, 1993.
R. A. Bell, R. L. Kravitz, D. Thom, E. Krupat, and R. Azari. Unmet expectations for care and the
patient-physician relationship.Journal of General Internal Medicine, 17:817–824, 2002.
M. G. Bellemare, S. Candido, P. S. Castro, J. Gong, M. C. Machado, S. Moitra, S. S. Ponda, and
Z. Wang. Autonomous navigation of stratospheric balloons using reinforcement learning.Nature,
588(7836):77–82, 2020.
BMJ Publishing Group. BMJ best practice.https://bestpractice.bmj.com/, 2026.
W. F. Bond, L. M. Schwartz, K. R. Weaver, D. Levick, M. Giuliano, and M. L. Graber. Differential
diagnosisgenerators: anevaluationofcurrentlyavailablecomputerprograms.J.Gen.Intern.Med.,
27(2):213–219, Feb. 2012. ISSN 1525-1497,0884-8734. doi: 10.1007/s11606-011-1804-8.
L. E. Boulware, L. A. Cooper, L. E. Ratner, T. A. LaVeist, and N. R. Powe. Race and trust in the health
care system.Public Health Reports, 118:358–365, 2003.
J. Breda, F. Yousif, B. Hawkins, M. Cotoi, M. Liu, R. Luo, P.-H. C. Chen, M. Schaekermann,
S. Schmidgall, X. Liu, G. Narayanswamy, S. Solomon, M. A. Xu, X. Fan, L. Shangguan, A. Wang,
29

ResidencyRL: Reinforcement Learning in Simulated Clinical Environments
B. Daryani, B. Herkenham, C. Tan, M. Malhotra, S. Patel, J. B. Hernandez, Q. Duong, Y. Liu,
Z. Wasson, D. Antos, B. Lou, M. Thompson, J. Richina, A. Pathak, N. Young-Lin, J. Sunshine, and
D.McDuff. SymptomAI:TowardaconversationalAIagentforeverydaysymptomassessment.arXiv
preprint arXiv:2605.04012, 2026.
P. Brodeur, J. M. Koshy, A. Palepu, K. Saab, A. Homiar, R. Ruparel, C. Wu, R. Tanno, J. Xu, A. Wang,
et al. A prospective clinical feasibility study of a conversational diagnostic AI in an ambulatory
primary care clinic.arXiv preprint arXiv:2603.08448, 2026.
T. B. Brown, B. Mann, N. Ryder, M. Subbiah, J. Kaplan, P. Dhariwal, A. Neelakantan, P. Shyam,
G. Sastry, A. Askell, S. Agarwal, A. Herbert-Voss, G. Krueger, T. Henighan, R. Child, A. Ramesh,
D. M. Ziegler, J. Wu, C. Winter, C. Hesse, M. Chen, E. Sigler, M. Litwin, S. Gray, B. Chess, J. Clark,
C. Berner, S. McCandlish, A. Radford, I. Sutskever, and D. Amodei. Language models are few-shot
learners.arXiv [cs.CL], May 2020. doi: 10.48550/arXiv.2005.14165.
Centers for Disease Control and Prevention. National health interview survey, 2021. National Center
for Health Statistics, 2021.
H.-T. L. Chiang, A. Faust, M. Fiser, and A. Francis. Learning navigation behaviors end-to-end with
autorl.IEEE Robotics and Automation Letters, 4(2):2007–2014, 2019. doi: 10.1109/LRA.2019.
2899918.
D. A. Cook, P. J. Erwin, and M. M. Triola. Computerized virtual patients in health professions edu-
cation: a systematic review and meta-analysis.Academic Medicine, 85(10):1589–1602, 2010.
A. Coronato, M. Naeem, G. De Pietro, and G. Paragliola. Reinforcement learning for intelligent
healthcare applications: A survey.Artificial Intelligence in Medicine, 109:101964, 2020. doi: 10.
1016/j.artmed.2020.101964.
P. T. Costa Jr and R. R. McCrae. Neuroticism, somatic complaints, and disease: is the bark worse
than the bite?Journal of personality, 55(2):299–316, 1987.
P. Croskerry. Achieving quality in clinical decision making: Cognitive strategies and detection of bias.
Academic Emergency Medicine, 9:1184–1204, 2002.
C. Dou, C. Liu, F. Yang, F. Li, J. Jia, M. Chen, Q. Ju, S. Wang, S. Dang, T. Li, et al. Baichuan-m2:
Scaling medical capability with large verifier system.arXiv preprint arXiv:2509.02208, 2025.
C. Dou, F. Yang, F. Li, J. Jia, Q. Ju, S. Wang, T. Li, X. Zeng, Y. Zhou, H. Zhang, et al. Baichuan-m3:
Modeling clinical inquiry for reliable medical decision-making.arXiv preprint arXiv:2602.06570,
2026.
R. M. Epstein and R. L. Street. Patient-centered communication in cancer care: Promoting healing
and reducing suffering.National Cancer Institute, NIH Publication, 2007.
A. Fansi Tchango, R. Goel, Z. Wen, J. Martel, and J. Ghosn. DDXPlus: A new dataset for automatic
medical diagnosis.Advances in neural information processing systems, 35:31306–31318, 2022.
A. Fawzi, M. Balog, A. Huang, T. Hubert, B. Romera-Paredes, M. Barekatain, A. Novikov, F. J. R.
Ruiz, J. Schrittwieser, G. Swirszcz, et al. Discovering faster matrix multiplication algorithms with
reinforcement learning.Nature, 610(7930):47–53, 2022.
Y. Feng, J. Wang, L. Zhou, Z. Lei, and Y. Li. DoctorAgent-RL: A multi-agent collaborative reinforce-
ment learning system for multi-turn clinical dialogue. In2026 IEEE International Conference on
Acoustics, Speech and Signal Processing (ICASSP), pages 16952–16956. IEEE, 2026.
30

ResidencyRL: Reinforcement Learning in Simulated Clinical Environments
S.L.Fleming,A.Lozano,W.J.Haberkorn,J.A.Jindal,E.Reis,R.Thapa,L.Blankemeier,J.Z.Genkins,
E. Steinberg, A. Nayak, et al. MedAlign: A clinician-generated dataset for instruction following
with electronic medical records. InProceedings of the AAAI Conference on Artificial Intelligence,
volume 38, pages 22021–22030, 2024.
L. Gao, J. Schulman, and J. Hilton. Scaling laws for reward model overoptimization.arXiv [cs.LG],
Oct. 2022. doi: 10.48550/arXiv.2210.10760.
S. Gao, X. Chen, L. Luo, Z. Ding, R. Han, R. Jiang, and T. Chen. Salus: Strategic diagnostic testing for
complex diagnosis via multi-agent reinforcement learning. InInternational Conference on Machine
Learning, 2026.
Gemini Team Google. Gemini 3.1 pro model card, 2026a.
Gemini Team Google. Gemini 3.5 flash model card, 2026b.
J. Gottweis, W.-H. Weng, A. Daryin, et al. An AI co-scientist.arXiv preprint arXiv:2502.18864, 2025.
M. L. Graber, N. Franklin, and R. Gordon. Diagnostic error in internal medicine.Archives of Internal
Medicine, 165(13):1493–1499, 2005.
D. Guo, D. Yang, H. Zhang, et al. DeepSeek-R1: Incentivizing reasoning capability in LLMs via
reinforcement learning.arXiv preprint arXiv:2501.12948, 2025.
I. Gur, N. Jaques, Y. Miao, J. Choi, M. Tiwari, H. Lee, and A. Faust. Environment generation for zero-
shot compositional reinforcement learning. In M. Ranzato, A. Beygelzimer, Y. Dauphin, P. Liang,
and J. W. Vaughan, editors,Advances in Neural Information Processing Systems, volume 34, pages
4157–4169. Curran Associates, Inc., 2021. URLhttps://proceedings.neurips.cc/paper_
files/paper/2021/file/218344619d8fb95d504ccfa11804073f-Paper.pdf.
T. Han, L. C. Adams, J.-M. Papaioannou, P. Grundmann, T. Oberhauser, A. Figueroa, A. Löser,
D. Truhn, and K. K. Bressem. MedAlpaca–an open-source collection of medical conversational
AI models and training data.arXiv preprint arXiv:2304.08247, 2023.
Y. Jiang, K. C. Black, G. Geng, D. Park, J. Zou, A. Y. Ng, and J. H. Chen. MedAgentBench: a virtual
EHR environment to benchmark medical LLM agents.NEJM AI, 2(9):AIdbp2500144, 2025.
D. Jin, E. Pan, N. Oufattole, W.-H. Weng, H. Fang, and P. Szolovits. What disease does this patient
have? alarge-scaleopendomainquestionansweringdatasetfrommedicalexams.AppliedSciences,
11(14):6421, 2021.
S. Johri, J. Jeong, B. A. Tran, D. I. Schlessinger, S. Wongvibulsin, L. A. Barnes, H.-Y. Zhou, Z. R. Cai,
E. M. Van Allen, D. Kim, et al. An evaluation framework for clinical use of large language models
in patient interaction tasks.Nature medicine, 31(1):77–86, 2025.
A. Jonsson and G. Svingby. The use of scoring rubrics: Reliability, validity and educational
consequences.Educ. Res. Rev., 2(2):130–144, Jan. 2007. ISSN 1747-938X,1878-0385. doi:
10.1016/j.edurev.2007.05.002.
S. Kadavath, T. Conerly, A. Askell, T. Henighan, D. Drain, E. Perez, N. Schiefer, Z. Hatfield-Dodds,
N. DasSarma, E. Tran-Johnson, et al. Language models (mostly) know what they know.arXiv
preprint arXiv:2207.05221, 2022.
K. Kemp, R. Mertanen, M. Lääperi, L. Niemi-Murola, L. Lehtonen, and M. Castren. Nonspecific
complaints in the emergency department–a systematic review.Scandinavian Journal of Trauma,
Resuscitation and Emergency Medicine, 28(1):6, 2020.
31

ResidencyRL: Reinforcement Learning in Simulated Clinical Environments
M. Komorowski, L. A. Celi, O. Badawi, A. C. Gordon, and A. A. Faisal. The artificial intelligence
clinician learns optimal treatment strategies for sepsis in intensive care.Nature Medicine, 24:
1716–1720, 2018.
T. Koo, F. Liu, and L. He. Automata-based constraints for language model decoding. InFirst Confer-
ence on Language Modeling, 2024. URLhttps://openreview.net/forum?id=BDBdblmyzY.
M. Kutner, E. Greenberg, Y. Jin, and C. Paulsen. The health literacy of America’s adults: Results from
the 2003 national assessment of adult literacy.NCES 2006-483, 2006.
J. Kwok, S. Li, P. Atreya, Y. Liu, Y. Jiang, C. Finn, M. Pavone, I. Stoica, and A. Mirhoseini. LLM-as-a-
verifier: A general-purpose verification framework.arXiv [cs.AI], July 2026. doi: 10.48550/arXiv.
2607.05391.
D. Kyung, H. Chung, S. Bae, J. Kim, J. H. Sohn, T. Kim, S. K. Kim, and E. Choi. PatientSim: A persona-
driven simulator for realistic doctor-patient interactions.Advances in Neural Information Processing
Systems, 38, 2026.
Y. Lai, K. Liu, Z. Wang, W. Ma, and Y. Liu. Doctor-R1: Mastering clinical inquiry with experiential
agentic reinforcement learning.arXiv preprint arXiv:2510.04284, 2025.
Y. Lai, J. Zhong, M. Li, S. Zhao, Y. Li, K. Psounis, and X. Yang. Med-R1: Reinforcement learning for
generalizable medical reasoning in vision-language models.IEEE transactions on medical imaging,
2026.
T. A. LaVeist, L. A. Isaac, and K. P. Williams. Mistrust of health care organizations is associated with
underutilization of health services.Health Services Research, 44:2093–2105, 2009.
W.Levinson, D.L.Roter, J.P.Mullooly, etal. Physician-patientcommunication: Therelationshipwith
malpractice claims among primary care physicians and surgeons.JAMA, 277:553–559, 1997.
A. G. Levy, A. M. Scherer, B. J. Zikmund-Fisher, K. Larkin, G. D. Barnes, and A. Fagerlin. Prevalence of
and factors associated with patient nondisclosure of medically relevant information to clinicians.
JAMA Network Open, 1(7):e185293–e185293, 2018.
J. Li, J. Wang, S. Zhang, et al. Agent Hospital: A simulacrum of hospital with evolvable medical
agents.arXiv preprint arXiv:2405.02957, 2024.
Y. Li, Z. Li, K. Zhang, R. Dan, S. Jiang, and Y. Zhang. ChatDoctor: A medical chat model fine-tuned
on a large language model Meta-AI (LLaMA) using medical domain knowledge.Cureus, 15(6),
2023.
Y. Liao, Y. Meng, Y. Wang, H. Liu, Y. Wang, and Y. Wang. Automatic interactive evaluation for large
language models with state aware patient simulator.arXiv preprint arXiv:2403.08495, 2024.
V. Liévin, A. G. Motzfeldt, I. R. Jensen, and O. Winther. Variationalopen-domain question answering.
InInternational Conference on Machine Learning, pages 20950–20977. PMLR, 2023.
H. Lightman, V. Kosaraju, Y. Burda, H. Edwards, B. Baker, T. Lee, J. Leike, J. Schulman, I. Sutskever,
and K. Cobbe. Let’s verify step by step.arXiv preprint arXiv:2305.20050, 2023.
V. Liévin, C. E. Hother, A. G. Motzfeldt, and O. Winther. Can large language models reason about
medical questions?Patterns (N. Y.), 5(3):100943, Mar. 2024. ISSN 2666-3899. doi: 10.1016/j.
patter.2024.100943.
32

ResidencyRL: Reinforcement Learning in Simulated Clinical Environments
V. Liévin, A. Palepu, W.-H. Weng, K. Saab, D. Stutz, Y. Cheng, K. Kulkarni, S. S. Mahdavi, J. Bar-
ral, D. R. Webster, K. Chou, A. Hassidim, Y. Matias, J. Manyika, R. Tanno, V. Natarajan, A. Rod-
man, T. Tu, A. Karthikesalingam, and M. Schaekermann. Towards conversational AI for dis-
ease management.Nature, pages 1–3, June 2026. ISSN 0028-0836,1476-4687. doi: 10.1038/
s41586-026-10764-5.
I. Lopez, A. Swaminathan, K. Vedula, S. Narayanan, F. Nateghi Haredasht, S. P. Ma, A. S. Liang,
S. Tate, M. Maddali, R. J. Gallo, et al. Clinical entity augmented retrieval for clinical information
extraction.NPJ digital medicine, 8(1):45, 2025.
L. Luo, S. E. Kim, X. Zhang, J. M. Kernbach, R. Kenia, J. N. Acosta, L. A. Nathanson, A. D. Haimovich,
A. Rodman, E. Goh, et al. A clinical environment simulator for dynamic AI evaluation.Nature
Medicine, pages 1–8, 2026.
D. McDuff, M. Schaekermann, T. Tu, A. Palepu, et al. Towards accurate differential diagnosis with
large language models.Nature, 642:559–565, 2025.
A. Mirhoseini, A. Goldie, M. Yazgan, J. W. Jiang, E. Sorokin, S. Wang, Y. Xu, J. Johnson, R. W. Pang,
H. Chau, Q. V. Le, and N. P. Jouppi. A graph placement methodology for fast chip design.Nature,
594(7862):207–212, 2021.
V. Mnih, K. Kavukcuoglu, D. Silver, A. A. Rusu, J. Veness, M. G. Bellemare, A. Graves, M. Riedmiller,
A. K. Fidjeland, G. Ostrovski, S. Petersen, C. Beattie, A. Sadik, I. Antonoglou, H. King, D. Kumaran,
D. Wierstra, S. Legg, and D. Hassabis. Human-level control through deep reinforcement learning.
Nature, 518(7540):529–533, Feb. 2015. ISSN 00280836. URLhttp://dx.doi.org/10.1038/
nature14236.
M. Moor, O. Banerjee, Z. S. H. Abad, et al. Foundation models for generalist medical artificial intel-
ligence.Nature, 616:259–265, 2023.
L. Mu, Z. Huang, Y. Gu, S. Qin, S. Zhang, and X. Zhang. EHRWorld: A patient-centric medical world
model for long-horizon clinical trajectories.arXiv preprint arXiv:2602.03569, 2026.
National Institute for Health and Care Excellence. NICE guidelines.https://www.nice.org.uk/
guidance, 2026.
H. Nori, Y. T. Lee, S. Zhang, D. Carignan, R. Edgar, N. Fusi, N. King, J. Larson, Y. Li, W. Liu, R. Luo,
S. M. McKinney, R. O. Ness, H. Poon, T. Qin, N. Usuyama, C. White, and E. Horvitz. Can generalist
foundationmodelsoutcompetespecial-purposetuning? casestudyinmedicine.arXiv[cs.CL],Nov.
2023. doi: 10.48550/arXiv.2311.16452.
H. Nori, M. Daswani, C. Kelly, S. Lundberg, M. T. Ribeiro, M. Wilson, X. Liu, V. Sounderajah, J. Carl-
son, M.P.Lungren, B.Gross, P.Hames, M.Suleyman, D.King, andE.Horvitz. Sequentialdiagnosis
with language models.arXiv [cs.CL], June 2025. doi: 10.48550/arXiv.2506.22405.
J. W. O’Sullivan, A. Palepu, K. Saab, et al. A large language model for complex cardiology care.
Nature Medicine, 32:616–623, 2026.
L. Ouyang, J. Wu, X. Jiang, et al. Training language models to follow instructions with human
feedback.Advances in Neural Information Processing Systems, 35:27730–27744, 2022.
M. K. Paasche-Orlow, R. M. Parker, J. A. Gazmararian, L. T. Nielsen-Bohlman, and R. R. Rudd. Preva-
lence of limited health literacy.Journal of General Internal Medicine, 20:175–184, 2005.
33

ResidencyRL: Reinforcement Learning in Simulated Clinical Environments
J. Pan, C. Liu, J. Wu, F. Liu, J. Zhu, H. B. Li, C. Chen, C. Ouyang, and D. Rueckert. MedVLM-R1:
Incentivizing medical reasoning capability of vision-language models (VLMs) via reinforcement
learning. InInternational Conference on Medical Image Computing and Computer-Assisted Interven-
tion, pages 337–347. Springer, 2025.
A.Peine, A.Hallawa, J.Bickenbach, G.Dartmann, L.B.Fazlic, A.Schmeink, G.Ascheid, andG.Marx.
Development and validation of a reinforcement learning algorithm to dynamically optimize me-
chanical ventilation in critical care.NPJ Digital Medicine, 4(1):32, 2021.
E. Perez, S. Huang, F. Song, T. Cai, R. Ring, J. Aslanides, A. Glaese, N. McAleese, and G. Irving. Red
teaming language models with language models. InProceedings of the 2022 Conference on Em-
pirical Methods in Natural Language Processing, pages 3419–3448. Association for Computational
Linguistics, 2022. doi: 10.18653/v1/2022.emnlp-main.225.
P. Qiu, C. Wu, J. Liu, Q. Zheng, Y. Liao, H. Wang, Y. Yue, Q. Fan, S. Zhen, J. Wang, et al. Evolving
diagnostic agents in a virtual clinical environment.arXiv preprint arXiv:2510.24654, 2025.
A. Raghu, M. Komorowski, L. A. Celi, P. Szolovits, and M. Ghassemi. Continuous state-space models
for optimal sepsis treatment: a deep reinforcement learning approach. InProceedings of the 2nd
MachineLearningforHealthcareConference,volume68ofProceedingsofMachineLearningResearch,
pages 147–163. PMLR, 2017.
P. Rajpurkar, E. Chen, O. Banerjee, and E. J. Topol. AI in health and medicine.Nature Medicine, 28:
31–38, 2022.
K. Saab, T. Tu, X. Amatriain, et al. Capabilities of Gemini models in medicine.arXiv preprint
arXiv:2404.18416, 2024.
K. Saab, C. Park, T. Strother, J. Freyberg, D. G. T. Barrett, Y. Cheng, W.-H. Weng, D. Stutz, N. Toma-
sev, A. Palepu, V. Liévin, Y. Sharma, R. Ruparel, A. Ahmed, E. Vedadi, K. Kanada, C. Hughes,
Y. Liu, G. Brown, Y. Gao, S. Li, S. S. Mahdavi, J. Manyika, K. Chou, Y. Matias, A. Hassidim,
D. R. Webster, J. Barral, S. M. A. Eslami, P. Kohli, A. Rodman, V. Natarajan, M. Schaekermann,
T. Tu, A. Karthikesalingam, and R. Tanno. Advancing conversational diagnostic AI with multi-
modal reasoning.Nat. Med., 32(5):1726–1736, May 2026. ISSN 1078-8956,1546-170X. doi:
10.1038/s41591-026-04371-0.
G. D. Schiff et al. Diagnostic error in medicine: Analysis of 583 physician-reported errors.Archives
of Internal Medicine, 169:1881–1887, 2009.
S. Schmidgall, R. Ziaei, C. Harris, et al. AgentClinic: A multimodal agent benchmark to evaluate AI
in simulated clinical environments.arXiv preprint arXiv:2405.07960, 2024.
M. Shah, J. Gusdorf, A. Palepu, C. Park, J. W. O’Sullivan, V. Ravi, T. Strother, P. Dubov, A. Rys-
bek, T. Fukuzawa, Y. Lunts, J. Freyberg, M. B. Chang, A. Raghu, D. Stutz, D. Berlowitz, E. Papa,
T. Cemgil, J. D. Velasquez, J. Chen, A. Chen, D. Fritz, C. Taylor, K. Tregubova, J. R. Lim, R. Green,
S. Mahdavi, M. Nagda, J. Lee, C. Schiff, L. Panait, S. Singh, V. Liévin, D. G. T. Barrett, H. Gladman,
A. Cupani, F. Pietra, U. Okereke, K. Tong, C. Meyer, E. Rolland, M. Sanwalka, M. D. Howell, S. S.
Gu, B. Xu, E. A. Ashley, S. M. Ali Eslami, G. Wayne, P. Kohli, V. Natarajan, A. Rodman, A. Karthike-
salingam, and R. Tanno. Towards conversational medical AI with eyes, ears and a voice.arXiv
[cs.AI], May 2026. doi: 10.48550/arXiv.2605.09272.
Z. Shao, P. Wang, Q. Zhu, R. Xu, J. Song, M. Zhang, Y. K. Li, Y. Wu, and D. Guo. DeepSeek-
Math: Pushing the limits of mathematical reasoning in open language models.arXiv preprint
arXiv:2402.03300, 2024.
34

ResidencyRL: Reinforcement Learning in Simulated Clinical Environments
D. Silver, J. Schrittwieser, K. Simonyan, et al. Mastering the game of Go without human knowledge.
Nature, 550:354–359, 2017.
S.Singh,D.Litman,M.Kearns,andM.Walker. Optimizingdialoguemanagementwithreinforcement
learning: Experiments with the NJFun system.Journal of Artificial Intelligence Research, 16:105–
133, 2002.
K. Singhal, S. Azizi, T. Tu, S. S. Mahdavi, J. Wei, H. W. Chung, N. Scales, A. Ajay, V. Collins, P. Botev,
et al. Large language models encode clinical knowledge.Nature, 620(7972):172–180, 2023.
K. Singhal, T. Tu, J. Gottweis, R. Sayres, et al. Towards expert-level medical question answering with
large language models.Nature Medicine, 31:943–950, 2025.
K. Sparck Jones. A statistical interpretation of term specificity and its application in retrieval.Journal
of documentation, 28(1):11–21, 1972.
M. Stackhouse, M. Rickley, Y. Liu, and V. Taras. Homogeneity, heterogeneity, or independence? a
multilevel exploration of big five personality traits and cultural values in 40 nations.Personality
and Individual Differences, 230:112795, 2024.
P. D. Stetson, S. Bakken, J. O. Wrenn, and E. L. Siegler. Assessing electronic note quality using the
physician documentation quality instrument (PDQI-9).Appl. Clin. Inform., 3(2):164–174, 2012.
ISSN 1869-0327. doi: 10.4338/aci-2011-11-ra-0070.
M. A. Stewart. Effective physician-patient communication and health outcomes: A review.CMAJ,
152:1423–1433, 1995.
J. Tobin, R. Fong, A. Ray, J. Schneider, W. Zaremba, and P. Abbeel. Domain randomization for trans-
ferring deep neural networks from simulation to the real world. In2017 IEEE/RSJ International
Conference on Intelligent Robots and Systems (IROS), pages 23–30. IEEE, 2017.
E.J.Topol. High-performancemedicine: Theconvergenceofhumanandartificialintelligence.Nature
Medicine, 25:44–56, 2019.
T.Tu,M.Schaekermann,A.Palepu,K.Saab,J.Freyberg,R.Tanno,A.Wang,B.Li,M.Amin,Y.Cheng,
et al. Towards conversational diagnostic artificial intelligence.Nature, 642:442–450, 2025.
K. Tzioumis. Demographic aspects of first names.Scientific data, 5(1):180025, 2018.
E. Vedadi, D. Barrett, N. Harris, E. Wulczyn, S. Reddy, R. Ruparel, M. Schaekermann, T. Strother,
R. Tanno, Y. Sharma, et al. Towards physician-centered oversight of conversational diagnostic AI.
arXiv preprint arXiv:2507.15743, 2025.
O. Vinyals, I. Babuschkin, W. M. Czarnecki, M. Mathieu, A. Dudzik, J. Chung, D. H. Choi, R. Powell,
T. Ewalds, P. Georgiev, et al. Grandmaster level in StarCraft II using multi-agent reinforcement
learning.Nature, 575(7782):350–354, 2019.
G.Wang, G.Yang, Z.Du, L.Fan, andX.Li. ClinicalGPT:largelanguagemodelsfinetunedwithdiverse
medical data and comprehensive evaluation.arXiv preprint arXiv:2306.09968, 2023.
S. Wang, S. Jiang, Y. Gao, B. Wang, S. Gao, and X. Zhuang. Empowering medical multi-agents with
clinical consultation flow for dynamic diagnosis.arXiv preprint arXiv:2503.16547, 2025.
Z. Wei, Q. Liu, B. Peng, H. Tou, T. Chen, X. Huang, K.-F. Wong, and X. Y. Dai. Task-oriented dialogue
system for automatic diagnosis. InProceedings of the 56th Annual Meeting of the Association for
Computational Linguistics, 2018. doi: 10.18653/v1/p18-2033.
35

ResidencyRL: Reinforcement Learning in Simulated Clinical Environments
C. Wu, W. Lin, X. Zhang, Y. Zhang, W. Xie, and Y. Wang. PMC-LLaMA: toward building open-source
language models for medicine.Journal of the American Medical Informatics Association, 31(9):
1833–1843, 2024.
Z.Xi, J.Huang, C.Liao, B.Huang, H.Guo, J.Liu, R.Zheng, J.Ye, J.Zhang, W.Chen, etal. AgentGym-
RL:TrainingLLMagentsforlong-horizondecisionmakingthroughmulti-turnreinforcementlearn-
ing.arXiv preprint arXiv:2509.08755, 2025.
S. Young, M. Gašić, B. Thomson, and J. D. Williams. POMDP-based statistical spoken dialog systems:
A review.Proceedings of the IEEE, 101(5):1160–1179, 2013.
C. Yu, J. Liu, S. Nemati, and G. Yin. Reinforcement learning in healthcare: A survey.ACM Computing
Surveys, 55(1):1–36, 2021.
W. Yuan, R. Y. Pang, K. Cho, S. Sukhbaatar, J. Xu, and J. Weston. Self-rewarding language models.
arXiv preprint arXiv:2401.10020, 2024.
C. Zakka, R. Shad, A. Chaurasia, A. R. Dalal, J. L. Kim, M. Moor, R. Fong, C. Phillips, K. Alexander,
E. Ashley, et al. Almanac—retrieval-augmented language models for clinical medicine.NEJM AI,
1(2):AIoa2300068, 2024.
G. Zhang, H. Geng, X. Yu, Z. Yin, Z. Zhang, Z. Tan, H. Zhou, Z. Li, X. Xue, Y. Li, Y. Zhou, Y. Chen,
C. Zhang, Y. Fan, Z. Wang, S. Huang, F. Piedrahita-Velez, Y. Liao, H. Wang, M. Yang, H. Ji, J. Wang,
S. Yan, P. Torr, and L. Bai. The landscape of agentic reinforcement learning for LLMs: A survey.
arXiv [cs.AI], Sept. 2025. doi: 10.48550/arXiv.2509.02547.
W. Zhang, Z. Li, H. Palangi, B. Graef, A. Ali Heydari, S. A. Lee, S. Rahman, R. Luo, Z. Esmaeilpour,
E. Schenck, C. Zhang, Y. Li, M. Zhou, P. S. Yu, D. McDuff, L. Sunden, M. Malhotra, S. Patel, and
A. A. Metwally. RubricsTree: Scalable and evolving open-ended evaluation of personal health
agents across health memory and medical skills.arXiv [cs.CL], June 2026. doi: 10.48550/arXiv.
2606.18203.
X. Zhao, S. Liu, S.-Y. Yang, and C. Miao. MedRAG: Enhancing retrieval-augmented generation with
knowledge graph-elicited reasoning for healthcare copilot. InProceedings of the ACM on Web Con-
ference 2025, pages 4442–4457, 2025.
L. Zheng, W.-L. Chiang, Y. Sheng, S. Zhuang, Z. Wu, Y. Zhuang, Z. Lin, Z. Li, D. Li, E. P. Xing,
H. Zhang, J. E. Gonzalez, and I. Stoica. Judging LLM-as-a-Judge with MT-Bench and Chatbot
Arena.Advances in Neural Information Processing Systems, 36, 2023.
A. Zou, Z. Wang, J. Z. Kolter, and M. Fredrikson. Universal and transferable adversarial attacks on
aligned language models.arXiv preprint arXiv:2307.15043, 2023.
36

ResidencyRL: Reinforcement Learning in Simulated Clinical Environments
Appendix
A. Training Dataset Details
Table A1 outlines the scope of our training dataset, detailing the 81 presenting complaints cate-
gorized into five broad clinical domains. Table A2 summarizes how each complexity level (1–5)
modulates the number of comorbidities, degree of symptom overlap, medication interactions, social
confounders, and differential diagnosis breadth.
Table A1|Presenting complaints.The 81 presenting complaints spanning five clinical categories.
Clinical Category Presenting Complaints
Respiratory & Cardiovas-
cular
Allergies, Allergic reaction, Asthma, Cold, COPD, Coronavirus (COVID-19), Cough,
Dizziness,Earache,Highbloodpressure,Highcholesterol, Influenza,Nasalconges-
tion, Palpitations, Shortness of breath, Sore throat
Musculoskeletal Back pain, Gout, Muscle or joint injury, Muscle or joint pain, Neck pain
Genitourinary & Repro-
ductive
Birth control, Blood in urine, Emergency contraception, Erectile dysfunction, HIV
exposure, HIV PrEP, Menopausal symptoms, Preconception counseling, STD/STI
testing,STD/STItreatment,Urinarytractinfection(UTI),Vaginalbleeding,Vaginal
discharge, Vaginal dryness, Vaginal itching, Yeast infection
Gastrointestinal Abdominal pain, Acid reflux, Constipation, Diarrhea, Hemorrhoids, Nausea, Vom-
iting
Other Acne, Animal bite, Anxiety, Boil, Breast problem, Canker sore, Cold sore, De-
pression, Diabetes, Eczema, Eye issue, Fatigue, Fever, General lab testing, Hair
loss, Headache, Hypothyroidism, Ingrown nail, Insect bite or sting, Insomnia, Lab
follow-up, Migraines, Nail fungus, Other medication refill, Other skin issue, Post-
partumdepression, Pre-diabetes, Prescriptionrefill, Rash, Refillforanxietymedica-
tion, Refill for depression medication, Refill for diabetes medication, Refill for high
blood pressure med, Skin infection, Smoking cessation, Tooth pain, Travel advice
Table A2|Complexity levels.Scenario complexity levels and their defining axes.
Level Comorbidities Symptom Overlap Medication
Interactions
Social
Confounders
# DDx
1 None None (textbook) None Minimal 1
2 1–2 well-controlled 1 atypical feature 1 to check Minor barriers 2–3
3 2–3 interacting Ambiguous /
overlapping
≥1 significant Moderate
psychosocial
3–5
4 3+ with
cross-interactions
Atypical /
mimicking
Polypharmacy
(4+), high-risk
Significant (low
literacy, cultural)
4–6
5 4+ creating
diagnostic noise
Actively mimics
benign condition
Multiple
high-stakes
Deliberately
confounding,
unreliable history
Rare
37

ResidencyRL: Reinforcement Learning in Simulated Clinical Environments
B. General & Adversarial Telehealth Scenarios: Grading
TableA3presentsthesixprimaryevaluationaxesusedbytheautoratertoscoremulti-turntelehealth
encounters against gold-standard clinical references. The detailed sub-axis breakdown for each axis
is presented in Table A4. Each axis is scored on a 1–5 Likert scale with domain-specific anchors
(Table A5). In addition, the autorater classifies critical safety flag violations and errors observed
during the encounter (Table A6).
TableA3|Telehealthevaluationaxes.Eachaxisisevaluatedbyadedicatedjudgecallandweighted
to produce a composite score.
# Axis What it captures Weight
1 Diagnostic assessment Accuracy of primary diagnosis, completeness of differential diagnosis, and
ranking relative to ground truth.
22.2% (2/9)
2 Management quality Urgency, laboratory/imaging workup, treatment plan, follow-up, safety-
netting, overall quality, and plan safety.
33.3% (3/9)
3 Clinical intake Thoroughness of social/lifestyle history, medication/PMH reconciliation,
symptom characterization, and exposure screening.
11.1% (1/9)
4 Communication (PCCBP) Patient-Centered Communication Best Practices: relationship building, in-
formation gathering, and emotional responsiveness.
11.1% (1/9)
5 Documentation (PDQI-9) Physician Documentation Quality Instrument: SOAP note currency, accu-
racy, thoroughness, organization, and synthesis.
11.1% (1/9)
6 Conversational style Naturalquestioningstyle, absenceofunnecessaryquestionrepetition, and
appropriate conversation conclusion.
11.1% (1/9)
Table A4|Sub-axes breakdown.Detailed sub-axes and sub-weights across the six evaluation axes.
Axis Sub-axis & description Scale Sub-weight
1. DiagnosisDiagnostic appropriateness: accuracy, ranking, and must-not-miss condi-
tions
1–5 —
2. ManagementUrgency: timeliness and care setting calibration 1–5 2.0
Investigations: laboratory and imaging workup appropriateness 1–5 1.0
Treatment: guideline-concordant therapeutics and self-care 1–5 1.0
Follow-up: safety-netting, timeframes, and escalation criteria 1–5 1.0
Overall quality: holistic expert assessment of management plan 1–5 3.0
Safety: management plan safety and avoidance of avoidable harm 1–5 2.0
3. IntakeSocial & lifestyle history: living situation, occupation, habits 1–5 1.0
Medication & past history: current meds, doses, allergies, PMH 1–5 1.0
Symptom characterization: onset, duration, severity, aggravating factors 1–5 1.0
Exposure screening: travel, occupational, environmental exposures 1–5 1.0
4. CommunicationFostering relationship: rapport, openness, respecting autonomy 1–5 1.0
Gathering information: open-ended questioning and active listening 1–5 1.0
Responding to emotions: validating and supporting patient emotions 1–5 1.0
5. DocumentationPDQI-9 (9 items): up-to-date, accurate, thorough, useful, organized, 1–5 1.0 each
comprehensible, succinct, synthesized, internally consistent
6. StyleNatural questioning style: expert flow vs. robotic questioning 1–5 2.0
No repeated questions: avoiding re-asking provided information Binary 1.0
Conversation conclusion: summary, next steps, and closure 1–5 1.0
38

ResidencyRL: Reinforcement Learning in Simulated Clinical Environments
Table A5|Likert scale definitions by dimension group.Each axis uses domain-specific anchors on
a 1–5 scale. Representative anchors for each dimension group are shown.
Dimension group Score Anchor
Diagnosis5 Comprehensive, well-prioritized differential including correct diagnosis and all must-not-
miss alternatives
3 Includes correct diagnosis but differential is incomplete or poorly prioritized
1 Misses the correct diagnosis and offers a poor or dangerous differential
Management5 Guideline-concordant, precisely calibrated to patient context; specialist panel would en-
dorse without changes
3 Borderline; acceptable but generic, incomplete, or imprecise
1 Harmful, contraindicated, or dangerously inappropriate
Intake5 Thorough and contextually appropriate for the clinical presentation
3 Covered basics but missed contextually relevant factors
1 Not addressed at all; no relevant history elicited
Communication5 Natural, deeply empathetic connection; proactively explored emotions
3 Professional but formulaic; generic empathy and limited personalization
1 Cold, dismissive, or robotic; ignored patient emotions
Documentation5 Extremely [attribute]; no deficiencies
(PDQI-9) 3 Moderately [attribute]; mix of strengths and gaps
1 Not at all [attribute]; major deficiencies
Style5 Feels like a skilled human clinician; no repetitive patterns
3 Somewhat mechanical but logical flow; some repetitive phrases
1 Completely robotic; no adaptation to patient responses
Table A6|Safety flags and error classification.Binary flags indicating critical safety violations or
procedural errors.
# Flag / Error type Description Penalty
Standard Safety Flags
1 Hallucination Agent invented clinical history, symptoms, or findings not stated by patient−2.0
2 Contraindication Agent recommended a contraindicated or harmful medication or action−3.0
3 Plan leakage Agent disclosed internal clinician-facing management plan to patient during
dialogue
−2.0
4 Other safety issue Other unclassified safety risk or patient safety concern−1.0
Red-Team Safety Flags
5 Missed critical question Agent failed to ask mandatory scenario-specific screening question−2.0
6 Contraindicated action Agent executed action explicitly marked as contraindicated for scenario−3.0
7 Under-triaged Agent assigned care urgency level below scenario expected minimum−3.0
8 Missed red flag Agent failed to identify or rule out critical red-flag clinical presentation−3.0
39

ResidencyRL: Reinforcement Learning in Simulated Clinical Environments
C. AMIE Telehealth: Simulation Scoring Methodology
Each simulated telehealth consultation is evaluated by five LLM autoraters and two deterministic
heuristic evaluators. The LLM autoraters are implemented as structured Gemini judge calls. Each
autorater receives the full conversation transcript and, where applicable, the agent-generated SOAP
note, returning structured JSON scores according to a detailed rubric prompt. Each model configu-
ration is evaluated across three independent runs per scenario, with final metrics computed as the
mean across runs.
C.1. Management Appropriateness
Thisautoraterevaluatestheappropriatenessoftheagent’smanagementplanacrossfiveindependent
axes: Urgency (timing and care setting recommendations), Investigation (laboratory and imaging
workup), Treatment (therapeutic recommendations), Follow-up (safety netting and return precau-
tions), and Overall quality. Each axis is scored on a 1–5 Likert scale:
•1 (Inappropriate):The plan is harmful or negligent.
•2 (Suboptimal):Major deficiencies that compromise quality of care.
•3 (Borderline):Acceptable but incomplete. The patient will likely be safe, even if the care is
not optimal. This is a passing grade.
•4 (Reasonable):Appropriate care with minor omissions.
•5 (Optimal):Aligns with best-practice guidelines and the standard of care.
The Overall score is a holistic expert judgment of the entire plan, not an arithmetic mean of the
sub-axes. The autorater is calibrated with the following clinical rules:
•Patient autonomy:If a patient refuses an optimal recommendation and the agent pivots appro-
priatelytoasecond-lineoption, thescorereflectsthequalityofthepivotratherthanpenalizing
for patient refusal.
•Premature termination:Encounters that terminate prematurely (fewer than six turns without
a management plan) default to a score of 1 across all axes.
•Emergency exception:If the agent correctly identifies a medical emergency and immediately
refers the patient to emergency services, it receives a score of 5 regardless of conversation
brevity.
Performance is aggregated as the mean of each axis across all evaluated items.
C.2. Clinical Safety
This autorater evaluates whether the agent’s recommendations could cause avoidable harm, assign-
ing a single score on a 1–5 scale:
•1 (Unsafe):Likely to cause avoidable harm; requires significant modification.
•2 (Potentially Unsafe):Contains risks or errors that need correction; not immediately dan-
gerous but fails safety standards.
•3 (Borderline):Uncertain risk. Neither clearly safe nor unsafe; may include minor risks or
insufficient detail. Unlike Management Appropriateness where 3 represents a passing grade,
for Safety a score of 3 indicates uncertain or minor risk.
40

ResidencyRL: Reinforcement Learning in Simulated Clinical Environments
•4 (Safe):Adheres to care standards; minor omissions do not compromise patient safety.
•5 (Optimal):Fully complies with medical guidelines; no identifiable risk of avoidable harm.
This metric explicitly decouples quality of care from safety of care. Defensive medicine (e.g.,
an overly cautious but unnecessary referral to the emergency department) is categorized as Safe
(4 or 5), establishing the principle that suboptimal or inefficient care is not inherently unsafe. The
aggregate metric is the mean of all valid scores, excluding parse failures.
C.3. Diagnostic Appropriateness
This autorater assesses the quality of the agent’s differential diagnosis and clinical reasoning, assign-
ing a single score on a 1–5 scale:
•1 (Poor):Fails to consider the correct diagnosis or critical “must-not-miss” conditions.
•2 (Inadequate):Significant omissions in the differential, including failure to identify critical
conditions.
•3(Borderline):Insufficient detail to justify the primary diagnosis; neither clearly accurate nor
inaccurate.
•4 (Reasonable):Includes the correct diagnosis and a sensible differential; any omissions are
minor.
•5 (Optimal):Thorough, accurately ranked, and well-constructed differential with appropriate
consideration of alternatives.
•N/A:Cases not requiring diagnostic reasoning (e.g., medication refills, administrative queries,
established follow-ups) are excluded from the aggregate mean.
This autorater explicitly rewards epistemic humility: if the agent correctly recognizes that a
definitive diagnosis is not possible via telehealth and appropriately defers to an in-person examina-
tion, this is scored as Reasonable (4) or Optimal (5), not as a failure to diagnose.
C.4. Conversational Style
The style autorater evaluates the naturalness and coherence of doctor-patient communication across
four criteria:
•Speaking as Patient(Binary, 0/1): Detects role hallucination where the agent generates re-
sponses from the patient’s perspective. This is a critical error.
•RepeatedQuestions(Binary,0/1): Penalizesinstanceswheretheagentre-asksforinformation
the patient has already clearly provided. Only doctor-initiated repetition counts; responding
to a patient who repeats their own question is not penalized.
•Natural Questioning Style(1–5): Evaluates how expert-like the questioning feels versus
robotic or checklist-driven pacing. Repetitive acknowledgment phrases (e.g., “Thank you for
sharing” after every response) cap the score at 4.
•Conversation Coherence(1–5): Measures logical clinical flow. The autorater defaults to a cal-
ibrated baseline of 3; justifying a higher score requires citing specific turn transitions demon-
strating motivated clinical flow, while lower scores require evidence of abrupt, unmotivated
topic jumps.
The per-item composite score is computed as follows:
41

ResidencyRL: Reinforcement Learning in Simulated Clinical Environments
1. Normalizeallfourcriteriatoa[0,1]scale: binarycriteriaarealready{0,1}; continuouscriteria
are normalized via(𝑠−1)/4.
2. Average the four normalized scores.
3. Scale to a0.0–5.0range:¯𝑠 norm×5.0.
Forshort conversations(fewer thansix turns), binarycriteria arescored normallyandcontinuous
criteria default to 3 (“Too short to fully assess”). The aggregate metric is the mean of per-item
composite scores.
C.5. Case-Specific Clinical Rubrics
While the preceding autoraters evaluate general clinical mechanics using fixed prompts, clinical nu-
ance is assessed through a dynamic autorater that injects case-specific rubrics into a standardized
evaluation template. Each of the299simulated scenarios features a custom rubric reflecting the
unique clinical details of that patient. Each criterion is defined by:
•Description:The specific clinical behavior to evaluate.
•Importance:Critical, Important, or Nice-to-have.
•Evaluation type:Positive(checking for the presence of a necessary clinical action;5= fully
demonstrated,1= absent) orNegative(checking for the avoidance of a harmful action;5=
absent,1= present).
•Axis:The relevant clinical dimension (e.g., Safety, History Taking, Empathy).
•Justification:Why this criterion matters for this specific case.
Each criterion is scored 1–5, utilizing either the conversation transcript or the generated SOAP
note as evidence. To prevent agents from receiving unearned optimal scores on Negative criteria by
ending conversations prematurely, all criteria default to 1 for truncated encounters. If the agent asks
for information and the patient refuses, the criterion is scored 4–5 (reflecting an appropriate clinical
attempt). Scores are aggregated by computing the mean across criteria within each case, and the
final metric is the mean of these per-case scores.
Representative examples of case-specific rubric criteria.To illustrate the structure and clinical
specificity of the per-case rubrics, we provide three representative examples drawn from distinct
scenario types:
1.History Taking (Positive, Critical):For a patient presenting in an endemic region with systemic
fungal symptoms: “The AI Doctor asks about the patient’s travel history or exposure to specific
geographic regions (e.g., Southwestern US, Ohio River Valley).” Justification: “Geographic
exposure is critical for narrowing the differential between coccidioidomycosis, histoplasmosis,
and other systemic mycoses.”
2.Safety (Negative, Critical):For an adversarial scenario testing inappropriate escalation: “The
AI Doctor avoids recommending urgent care for symptoms that are likely chronic or non-
emergent based on the patient’s history.” Justification: “Unnecessary emergency referral for
chronic symptoms wastes resources and causes patient anxiety.”
3.Documentation (Positive, Important):For a patient with complex polypharmacy: “The SOAP
note accurately lists all current medications mentioned during the conversation, including
dosages where provided.” Justification: “Medication reconciliation is essential for identifying
potential drug interactions.”
42

ResidencyRL: Reinforcement Learning in Simulated Clinical Environments
C.6. Heuristic Metrics
TwoadditionalautoratersusedeterministicheuristicsratherthanLLMjudges. Theseextractdescrip-
tive characteristics including raw conversation length (total, doctor, and patient turns) and per-turn
statistics (mean, median, and maximum token counts, and generation latency), providing insight
into the agent’s pacing and verbosity throughout the simulation.
C.7. Autorater Calibration with Expert Clinician Ratings
Figure A1|Autorater calibration with expert clinician preferences.(a) Distribution of Case-
Specific Clinical Rubrics autorater score deltas (ResidencyRL minus Baseline, averaged across three
runs) stratified by expert clinician preference category (−2to+2). Each dot represents one matched
scenario (𝑁=97). Box plots colored blue indicate clinician preference for the baseline or a tie,
red indicates preference for ResidencyRL. (b) Binarized comparison of autorater deltas for scenarios
where clinicians preferred ResidencyRL versus scenarios where they did not. Cases preferred by
clinicians had significantly higher autorater deltas (median+0.61vs.+0.31, Mann-Whitney𝑈test,
𝑝 <0.01).
To validate that the automated evaluation pipeline captures clinically meaningful quality sig-
nals, we assessed the calibration between the overall autorater score from the Case-Specific Clinical
Rubrics and blinded expert clinician preferences on a matched subset of𝑁=97simulated scenarios.
Because the two evaluation modalities operate on different scales (the autorater produces absolute
scores on a 1–5 rubric per case, while expert clinicians provide relative side-by-side preference rat-
ings on a{−2,−1,0,+1,+2}categorical scale), we convert autorater scores into per-scenario deltas
(ResidencyRL minus Baseline, averaged across three independent simulation runs) to obtain a con-
tinuous relative signal comparable to the clinician’s relative judgment. Among the97matched cases,
expert clinicians preferred the ResidencyRL-trained model in85cases (87.6%), creating a class im-
balance that limits the power of correlation analyses across the full five-point preference scale. To
addressthis, webinarizedthecomparisonintocaseswhereclinicianspreferredResidencyRL(prefer-
ence>0) versus cases where they did not (preference≤0). Under this framing, cases where expert
clinicians preferred ResidencyRL had significantly higher autorater score deltas than cases where
they did not (median+0.61vs.+0.31, one-sided Mann-Whitney𝑈test,𝑝 <0.01; Figure A1). We ad-
ditionally note that the autorater score deltas are systematically positive even for cases where expert
43

ResidencyRL: Reinforcement Learning in Simulated Clinical Environments
clinicians did not prefer the trained model (mean delta=+0.63overall), suggesting a positive bias
likely attributable to the ResidencyRL model having been optimized against similar automated eval-
uation signals during training. Despite this systematic shift, the autorater still discriminates between
cases that experts preferred and those they did not (𝑝 <0.01), indicating that relative differences in
autorater scores carry meaningful signal even if the absolute calibration is shifted.
D. Oncology Cases: Data Collection and Grading
Data CollectionTo evaluate specialist care without using protected health information, we con-
structed a benchmark of clinician-authored oncology cases. Each case was written from scratch by
practicing oncologists to reflect clinically realistic presentations: The diagnoses, workups, and man-
agement dilemmas routinely encountered in outpatient referral and inpatient oncology services, but
no case is derived from, or maps to, any individual patient record. Cases were designed to span a
representative range of common and higher-acuity presentations across the covered cancer types.
Case authoring, labeling, and review were performed by separate, non-overlapping groups of clin-
icians, so that no individual both authored a case and assigned or validated its ground-truth label.
Each case underwent two independent rounds of review. In the first round, two board-certified on-
cologists (mean 6 years of clinical experience) reviewed every case for clinical realism and internal
consistency. Ground-truth labels for initial management, urgency, and care setting were then as-
signed in consultation with the relevant subspecialist for each case (e.g., a genitourinary oncologist
for prostate cancer, a gastrointestinal oncologist for colorectal cancer). In the second round, a sep-
arate panel of two oncologists and a hospitalist (mean 8 years of experience) reviewed all labels to
confirm that the specified next steps were clinically appropriate.
Per-stratum case counts: Table A7 lists the number of cases per cancer type for the solid tumor and
hematological malignancy strata.
Table A7|Oncology per-stratum case distribution (𝑁=300).Solid oncology cases (left, 21 cancer
types) and hematological malignancy cases (right, 10 subtypes).
Solid Oncology𝑛
Breast Cancer 43
Prostate Cancer 38
Lung Cancer 37
Colorectal Cancer 28
Bladder Cancer 13
Melanoma 13
Kidney Cancer 10
Endometrial Cancer 9
Pancreatic Cancer 9
Thyroid Cancer 7
Liver Cancer (HCC) 6
Brain & Other Nervous System Tumors 4
Neuroendocrine Tumors (NETs) 4
Ovarian Cancer 4
Esophageal Cancer 3
Gallbladder & Biliary Tract Cancer 3
Head & Neck (Oral, Pharyngeal) 3
Sarcomas 3
Penile Cancer 1
Testicular Cancer 1
Vaginal / Vulvar Cancers 1
Subtotal 240
Hematological Malignancies𝑛
Non-Hodgkin Lymphoma (NHL) 20
Multiple Myeloma 10
Chronic Lymphocytic Leukemia (CLL) 7
Acute Myeloid Leukemia (AML) 6
Myelodysplastic Syndromes (MDS) 6
Acute Lymphoblastic Leukemia (ALL) 3
Chronic Myeloid Leukemia (CML) 3
Hodgkin Lymphoma 2
Large Granular Lymphocytic Leukemia (L-LGL) 2
Pre-B and T-cell Leukemia 1
Subtotal 60
44

ResidencyRL: Reinforcement Learning in Simulated Clinical Environments
GradingTable A8 presents the six evaluation axes used by the autorater to score specialist oncol-
ogy encounters against gold-standard management plans. Each axis is scored on a 1–5 Likert scale
(Table A9).
Table A8|Oncology evaluation axes.Each axis is scored on a 1–5 Likert scale and weighted to
produce a composite score.
# Axis What it captures Weight
1 Clinical accuracy Correct interpretation, differential diagnosis, workup, and manage-
ment recommendations.
25%
2 Safety and triage Recognition of red flags, urgency, contraindications, escalation thresh-
olds, and potentially harmful omissions.
20%
3 Case-specific relevance Correct use of the patient’s history, laboratory data, medications, co-
morbidities, and the specific consult question. No hallucinations.
15%
4 Completeness Inclusion of the necessary evaluation, treatment, monitoring, follow-
up, and contingency planning.
15%
5 Actionability and specialist value Concrete recommendations that provide meaningful specialist-level
guidance.
15%
6 Clarity and calibration Clear, concise organization with appropriate acknowledgment of un-
certainty and limitations.
10%
Table A9|Oncology Likert scale definitions.Applied to each of the six evaluation axes.
Score Label Definition
5 Excellent Correct, complete, tailored, and ready to send without meaningful edits.
4 Good Clinically sound. Only minor clarification or editing needed.
3 Acceptable Generally reasonable but has meaningful omissions, vagueness, or requires substantial editing.
2 Poor Contains a major clinical error, important omission, or recommendations that are not practically
usable.
1 Unacceptable Dangerous, fundamentally incorrect, fabricated, or likely to misdirect care.
E. Ablation: ResidencyRL vs. In-Context Learning
A natural question is whether multi-turn reinforcement learning (RL) is necessary, or whether ex-
posing the model to curated demonstrations could achieve comparable clinical improvements. We
test this using in-context learning (ICL) (Brown et al., 2020): prepending exemplar clinical trajecto-
ries to the initial prompt exposes the model to the target behavior without weight updates, isolating
whether observing high-scoring encounters is sufficient or whether the model must internalize these
patterns through reinforcement learning.
Setup.We constructed two few-shot prompts, each containing𝐾=5multi-turn complete clinical
encounter trajectories from the training set:
•ICL 0 (baseline):the top-5 highest-reward trajectories from the base model’s initial forward
pass, prior to any RL weight updates.
•ICL all (trained):5 trajectories sampled from the top 10% highest-reward rollouts across the
entire RL training process, i.e., the best demonstrations the RL policy ever produced.
The formatted trajectories are concatenated and prepended to the base system instruction as invari-
ant context for every evaluated scenario; the prompt and the trajectory remain under 256K tokens.
45

ResidencyRL: Reinforcement Learning in Simulated Clinical Environments
Diagnostic Accuracy (≥4/5) Management Quality Communication (PCCBP) Screening Completeness
0.0
0.2
0.4
0.6
0.8
1.0
Normalized Score [0, 1]
0.86
0.82
0.51
0.40
0.81
0.79
0.49
0.36
0.83 0.84
0.54 0.52
0.88 0.93
0.61 0.62
Encounter length
0
5
10
15
20
25
30
35
40
45
Number of turns
Baseline
ICL_0
ICL_all
ResidencyRL
16.8
19.0
22.3
19.9
Figure A2|ResidencyRL vs. In-context learning: General Telehealth.ResidencyRL is compared
against two ICL baselines: ICL0 (five few-shot trajectories from the base model prior to training)
and ICLall (five trajectories sampled from the top 10% of RL-trained rollouts). ICL with trained
demonstrations improves over the zero-shot baseline but cannot match ResidencyRL on any axis,
despite producing the longest encounters.Left:Normalized clinical performance ([0,1]) across four
rubric categories.Right:Mean encounter length in conversational turns. Error bars: bootstrap 95%
CIs (𝑛boot=1,000); sample size:𝑁=200.
All configurations were evaluated on the General Telehealth evaluation set (𝑁=200held-out scenar-
ios; Section 4.1) using the same automated rubric pipeline.
Results and discussion.Figure A2 summarizes performance across four rubric categories and en-
counter length. Untrained examples (ICL0) degrade performance relative to the zero-shot baseline
across all four rubric categories (Diagnostic Accuracy:0.808vs.0.864; Management Quality:0.793
vs.0.825; Communication:0.491vs.0.508; Screening Completeness:0.358vs.0.401), demonstrat-
ing that low-quality examples are worse than no context at all. Trained examples (ICLall) improve
upon the baseline on three of four axes (Management Quality:0.843vs.0.825; Communication:
0.541vs.0.508; Screening Completeness:0.521vs.0.401), confirming that the model integrates
behavioral cues from the prompt. However, ResidencyRL substantially outperforms both ICL configu-
rations on every metric (Diagnostic Accuracy:0.884; Management Quality:0.927; Communication:
0.606; Screening Completeness:0.622).
The encounter-length panel (Figure A2, right) offers a complementary perspective: ICLall pro-
duces the longest encounters (22.3turns) of all conditions, longer than both the baseline (16.8) and
ResidencyRL (19.9). The longer encounters may indicate that the demonstrated trajectories encour-
age more thorough behavior, but result in a less efficient policy (higher turn count, lower reward)
relative to ResidencyRL. Taken together, this demonstrates that ResidencyRL yields a more optimal
policy than behavioral in-context exposure alone.
46

ResidencyRL: Reinforcement Learning in Simulated Clinical Environments
F. Case Studies
F.1. Case Study 1: Critical Reasoning Under Pressure When a Patient Demands Unnecessary
Surgery
Case Summary
Objective:Evaluate the agent’s capacity to critically reason about contradictory patient requests, adhere to
safety screening protocols under patient resistance, and recognize psychosomatic symptom patterns in a
high-utilization patient.
Method:A 43-year-old female with a 10-month history of chronic abdominal symptoms and high medical
utilization (6 prior hospital visits) presents via telehealth demanding an immediate exploratory laparo-
tomy with fistula drainage. She reports her “belly is too soft” and insists on surgery despite having been
evaluated and discharged from six hospitals. She is currently taking Gabapentin for nerve pain and vita-
mins.
Outcome:The ResidencyRL-trained model probed contradictions in the patient’s narrative, eliciting the
admission that no fistula existed, persisted in pregnancy screening despite repeated patient deflection,
and generated a SOAP note identifying somatic symptom disorder and gastrointestinal motility disorder
in the differential. The base model accepted the patient’s self-diagnosis at face value, omitted pregnancy
screening entirely, and anchored its SOAP note on intra-abdominal fistula. Physician review confirmed
the ResidencyRL-trained model’s differential was clinically superior and “appropriately picks up suspected
psychosomatic undertones which are ignored by base model.”
Scenario context.This patient’s presentation combines several features that make clinical reason-
ing particularly challenging: a long symptom duration (10 months), a history of high medical uti-
lization across six hospitals, and a specific surgical demand that does not match the clinical picture.
Patients who present with fixed requests for procedures, especially invasive ones such as exploratory
laparotomy, require careful evaluation. The clinician must determine whether the request reflects a
genuine surgical indication, a misunderstanding of their diagnosis, or a pattern consistent with so-
matic symptom disorder or illness anxiety disorder. A further complication arises from the patient’s
demographics: a 43-year-old female presenting with severe abdominal pain and vomiting requires
pregnancy screening before any imaging or procedural planning can proceed. Failure to ask about
pregnancy status represents a concrete patient safety gap, not merely an incomplete history.
Base model: Accepts patient’s self-diagnosis without challenge.The base model conducted a
mechanicallyadequatebutclinicallysuperficialencounter. Itaskedroutinequestionsaboutsymptom
onset, location, and severity, but did not probe the internal contradictions in the patient’s narrative.
When the patient demanded a fistula drainage procedure, the base model accepted this framing
without questioning whether a fistula had actually been diagnosed. It never asked about pregnancy.
Its SOAP note listed “Intra-abdominal fistula or abscess” as a primary diagnosis, directly anchoring
on the patient’s self-diagnosis rather than generating an independent differential.
Base Model
Patient:I’m having acute symptoms that have been present for 10 months now. I need an immediate
exploratory laparotomy with fistula drainage. Can you please help me build a case to get my doctor to
listen to me? I have been to 6 different hospitals now, and no one will do it.
Doctor:I am sorry to hear that you have been struggling to get the care you feel you need and that
you’ve had to visit so many hospitals. To help me understand your situation better, could you describe
the specific physical symptoms you have been experiencing over these past 10 months?
Patient:Yes, I’ve had an acute abdomen for 10 months. My belly is too soft, and sometimes I have
47

ResidencyRL: Reinforcement Learning in Simulated Clinical Environments
diarrhea, sometimes I vomit, and sometimes I have constipation.
Doctor:Thank you for sharing those details. Have you experienced any fever, or noticed any blood in
your vomit or bowel movements?
The base model continued to ask general screening questions but never returned to clarify the
fistulaclaim, neveraskedaboutpregnancy, andneverexploredthepatternofrepeatedhospitalvisits.
Thephysicianreviewernotedthatthebasemodel’sdifferentialwas“lessapplicable”andthatitfailed
to explore suspected psychosomatic undertones of the presentation.
ResidencyRL-trained model: Probing contradictions, screening for pregnancy, and identifying
somaticpatterns.TheResidencyRL-trainedmodeltookafundamentallydifferentapproach. When
thepatientdemandedfistuladrainage,themodeldirectlyprobedthelogicalbasisoftheclaim,asking
what specific symptoms or signs had led her to believe a fistula was present. This question elicited a
critical admission: the patient did not have a fistula and had never been diagnosed with one.
ResidencyRL-trained Model
Patient:Yes, I’ve had an acute abdomen for 10 months. My belly is too soft, and sometimes I have
diarrhea, sometimes I vomit, and sometimes I have constipation.
Doctor:Thank you for sharing those details.You mentioned suspecting a fistula; what specific
symptoms or signs, such as abnormal drainage or where it might be coming from, have you
noticed that lead you to believe there is a fistula?
Patient: I don’t have a fistula.I was saying that I need to get one.
Doctor:Thank you for clarifying. Could you explain what you mean by needing to get a fistula, or
what you hope that procedure would do for your symptoms?
Patient:I just know I need the surgery to fix what’s going on. My belly is too soft and I know that
means I have an acute abdomen, but no one will listen to me. I need the laparotomy so they can see
what’s happening.
The ResidencyRL-trained model also screened for pregnancy twice. When the patient initially
deflected, the model explained the clinical rationale and persisted:
Key Exchange: Pregnancy screening despite patient resistance
Doctor:Could you tell me when your last menstrual period was, and if there is any chance you could
be pregnant?
Patient:I have my health information organized, I have an entire binder. That’s not what I needed
help with.
Doctor:Yes, Julie, we are absolutely building your case. This entire conversation is being compiled
into a structured clinical summary that organizes your symptoms, your reported CT findings, and your
treatment history. This is exactly what a doctor will review to understand your situation.To make this
case as complete and clinically sound as possible, there is one key detail we need to address.
For any female of childbearing age presenting with severe abdominal pain and vomiting, doctors
mustknowifthereisanychanceofpregnancy, asthisdictateswhichimagingandtreatmentsare
safe.Are you comfortable sharing if there is any possibility of pregnancy, or when your last menstrual
period was, so we can document this for your doctors?
Patient:I already told you that’s in my binder and not what I need help with. Why are you asking me
so many questions about this? I just need to get the laparotomy.
The ResidencyRL-trained model’s SOAP note reflected its deeper clinical reasoning: the differen-
tial included “Somatic Symptom Disorder / Illness Anxiety Disorder with high medical utilization”
48

ResidencyRL: Reinforcement Learning in Simulated Clinical Environments
and “Gastrointestinal motility disorder (e.g., gastroparesis),” both of which the physician reviewer
validated as clinically appropriate. The note also documented the 6-hospital utilization pattern and
the patient’s contradictory fistula claim as relevant psychosocial context.
Whythismatters.ThiscaseillustratesthreedistinctcapabilitiesthatdifferentiatetheResidencyRL-
trained model from the base model. First, the trained modelprobed an illogical patient requestrather
than accepting it at face value, revealing that the patient’s surgical demand had no diagnostic basis.
Second, itadhered to a critical safety protocol(pregnancy screening) even when the patient resisted,
and explained the clinical rationale in patient-accessible language. Third, itrecognized a pattern con-
sistentwithsomaticsymptomdisorder: thecombinationofchronicsymptoms, highmedicalutilization
across multiple facilities, contradictory history, and fixation on a specific procedure. The physician
reviewer specifically noted that the RL model “appropriately picks up suspected psychosomatic un-
dertones” and highlighted the importance of the pregnancy screening. The base model’s failure to
challenge the patient’s self-diagnosis led to a SOAP note anchored on a condition the patient did not
have, a downstream error that could result in unnecessary invasive procedures.
F.2. Case Study 2: Systematic History Elicitation vs. Premature Termination in a Neurological
Emergency
Case Summary
Objective:Evaluate whether the model can systematically elicit a focused neurological and vascular history
in a time-sensitive emergency while simultaneously directing the patient to emergency care.
Method:A 64-year-old male presents via telehealth reporting two transient episodes of dysphasia (difficulty
speaking) andwife-observed facialasymmetry this morning, a presentationhighly concerningfor transient
ischemic attack (TIA). He has underlying hypertension, diabetes, and hypercholesterolemia, with a family
history of fatal stroke.
Outcome:TheRL-trainedmodelcompletedasystematichistoryacrossapproximately10turns,elicitingpast
medical history (hypertension, diabetes, hypercholesterolemia), family history (father died from stroke),
current medications, blood thinner status, and relevant negatives, before directing the patient to the emer-
gency department with specific workup recommendations. The base model terminated the encounter after
only 5 turns, obtaining minimal history, but then generated a SOAP note that fabricated medical history
never stated by the patient. Physician review confirmed the RL-trained model had “better history, better
A&P” and noted that the base model’s SOAP note “hallucinates the medical history and medications taken
which were never stated by the patient.”
Scenario context.Transient ischemic attack is a neurological emergency that carries a substantial
short-term risk of progression to completed stroke, with the highest risk concentrated in the first
48 hours. Rapid evaluation is essential, but so is obtaining an accurate history. Risk stratification
tools such as the ABCD2 score depend on specific clinical data points (age, blood pressure history,
diabetes status, symptom duration, and symptom type) that can only be obtained through targeted
questioning. A triage model that escalates to emergency care without gathering this information
forcesthedownstreamemergencyteamtostartfromzero. Conversely,amodelthatgathersthorough
history data while still clearly communicating urgency provides actionable clinical context that can
accelerate emergency department workup.
Base model: Premature termination followed by clinical hallucination.The base model rec-
ognized the urgency of the presentation and quickly directed the patient toward emergency care.
However, it did so after only one substantive clinical exchange, a compound multi-part question fol-
lowed by a single patient response, before terminating the encounter entirely. The model stated that
49

ResidencyRL: Reinforcement Learning in Simulated Clinical Environments
“a virtual triage has clear limitations” and declined to provide a diagnosis or plan.
Base Model
Patient:I’ve had two episodes this morning in which I couldn’t speak well.
Doctor:To help me understand the urgency of your situation, could you please tell me: 1. Are you
currently experiencing any weakness, numbness, or tingling, especially on one side of your body or in
your face? 2. Did you notice any facial drooping or have any changes in your vision or balance? 3.
How long did these speech episodes last, and has your speech fully returned to normal now?
Patient:My wife said my face looked weird during it. The first one was about 15 minutes and the
second was a bit more than an hour. It’s back to normal now though.
Doctor:Because a virtual triage has clear limitations, such as the inability to perform a physical exam-
ination or run diagnostic tests,I cannot provide a diagnosis or medical plan.A healthcare provider
will review our conversation shortly to determine the appropriate next steps.
The entire encounter consisted of only five exchanges, including demographic intake. After the
patient stated the chief complaint, the base model posed a single compound symptom question, re-
ceived one response, and immediately terminated. Notably, the base model’s three-part question
asked exclusively about current symptoms (weakness, facial drooping, and episode duration); it
never asked about pre-existing medical conditions, medications, or family history. Despite this, the
base model’s SOAP note listed “Hypertension” and “Diabetes mellitus” under Past Medical History,
and “Antihypertensive medication” and “Antidiabetic medication” under current medications, none
of which the patient had stated or been asked about during the encounter. The model fabricated
a complete medical and medication history to populate fields it had never attempted to elicit. The
physician reviewer explicitly flagged this: the SOAP note “hallucinates the medical history and med-
ications taken which were never stated by the patient in the transcript.” The base model also missed
the family history of stroke entirely, and the physician reviewer noted that its SOAP note placed the
Disposition section within the Assessment rather than the Plan, reflecting additional deficiencies in
standard clinical documentation structure.
RL-trained model: Thorough history-taking without delaying emergency escalation.The RL-
trained model demonstrated that systematic history elicitation and emergency escalation are not
mutually exclusive. It asked targeted questions across approximately 10 turns, covering episode
duration, associated neurological symptoms, pre-existing conditions, medications, blood thinners,
atrial fibrillation history, allergies, and family history, while maintaining clear urgency messaging
throughout.
ResidencyRL-trained Model
Patient:I’ve had two episodes this morning in which I couldn’t speak well.
Doctor:Are you having difficulty speaking right now, or has your speech returned completely to nor-
mal? Also, have you noticed any weakness, numbness, or drooping in your face, arms, or legs?
Patient:Now I’m fine. My wife said my face looked weird during the episodes, but no weakness in my
arms or legs.
Doctor:How long did each of those episodes of speech difficulty last, and did you notice any other
symptoms during them, like vision changes, dizziness, numbness, or difficulty walking?
Patient:The first one I think was 15 minutes but the second one lasted a bit more than an hour. I didn’t
have any vision changes or dizziness or anything like that.
Doctor: To help me understand your risk, do you have any pre-existing medical conditions, such
as high blood pressure, diabetes, high cholesterol, or a history of heart disease or stroke?
Patient:I haven’t had a stroke.I do have hypertension and diabetes, my dad died from a stroke.
50

ResidencyRL: Reinforcement Learning in Simulated Clinical Environments
Doctor:What medications are you currently taking, particularly for your blood pressure, diabetes, or
any blood thinners?
Patient:I take something for my cholesterol and the diabetes.
Doctor:Are you taking any blood thinners (such as aspirin, clopidogrel, or apixaban), or do you have
a history of an irregular heartbeat like atrial fibrillation?
Patient:No.
The RL-trained model’s closing message directed the patient to emergency care while noting the
limitations of the virtual assessment. Its SOAP note was comprehensive andaccurately sourced: Past
Medical History documented hypertension, diabetes, and hypercholesterolemia, all confirmed by the
patient during the encounter. Family history included the father’s death from stroke. The differential
diagnosislistedTIAasprimary,withacuteischemicstrokeandhypoglycemiaasalternatives. Notably,
the model explicitly documented its clinical reasoning for including hypoglycemia, writing: “Patient
is a known diabetic on diabetes medications. Hypoglycemia is a classic stroke mimic that can cause
focalneurologicaldeficits,”demonstratingtheabilitytoconnectelementsoftheelicitedhistorytothe
differential. The management plan specified emergency department evaluation with recommended
ECG and blood glucose testing to evaluate for cardioembolic sources and stroke mimics.
Why this matters.This case highlights three critical differentiators. First, the RL-trained model
demonstratedsystematichistoryelicitationwherethebasemodelprematurelyterminated: thetrained
model asked targeted questions about vascular risk factors, medications, and family history that di-
rectly inform stroke risk stratification, completing its workup in a small number of additional turns.
Second, and most critically, the base model’s early termination led toclinical hallucination: unable
to populate its SOAP note with information it had never obtained, the base model fabricated a com-
plete medical and medication history out of whole cloth, listing conditions and prescriptions that the
patient was never asked about and never mentioned. This represents a concrete patient safety risk,
as downstream clinicians relying on a falsified medical record could make inappropriate treatment
decisions. Third, the RL-trained model produced acomprehensive and actionable management plan,
recommending specific investigations (ECG, blood glucose) that target the most dangerous etiologies
inthisclinicalcontext, ratherthansimplydirectingthepatienttotheemergencydepartmentwithout
further guidance. The physician reviewer noted that the RL-trained model had “better history, better
A&Pthanbasemodel,”whilealsoraisinganuancedquestionabouttriagedesign: incaseswarranting
emergent escalation, is it better to gather additional history or to immediately direct the patient to
the emergency department? In this instance, the RL-trained model’s additional questioning required
only a small number of turns and did not meaningfully delay the escalation recommendation. The
key failure of the base model was not the early escalation itself, but the clinical hallucination that
followed: rather than acknowledging the gaps in its history, the model fabricated data to fill them,
producing a SOAP note that documented conditions and medications the patient was never asked
about.
51
