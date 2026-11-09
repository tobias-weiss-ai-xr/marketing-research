---
title: Design and Implementation of Agentic Orchestrations and Orchestration of Agents
url: https://arxiv.org/abs/2606.31518
category: ai-marketing
subcategory: empirical
date: 2026-06
venue: ''
authors:
- Stefanie Rinderle-Ma
- Juergen Mangler
- Johannes Loebbecke
- Dominik Voigt
- Nataliia Klievtsova
source: arxiv
pdf_url: https://arxiv.org/pdf/2606.31518
pages: 15
chars: 41573
fetched_at: '2026-11-08T13:36:05+00:00'
kb_version: 1
---

# Design and Implementation of Agentic Orchestrations and Orchestration of Agents

Agentic Orchestration and Orchestration of
Agents: Design, Implementation, and Assessment
Stefanie Rinderle-Ma, Juergen Mangler, Johannes Loebbecke, Dominik Voigt,
Nataliia Klievtsova, Matthias Ehrendorfer
Technical University of Munich, TUM School of Computation, Information and
Technology, Garching, Germany,firstname.lastname@tum.de
Abstract.Agentic Business Process Management has gained momen-
tum recently. The prospect is that the autonomy of AI agents, i.e., pre-
dominantly LLM-based agents, can be balanced with a certain level of
robustness,correctness,andtraceabilitythroughacombinationwithpro-
cess technology. In this paper, we provide a classification framework for
agentic orchestration options and discuss them along properties such as
autonomy, task specificity, reactivity, correctness assurance, traceabil-
ity, and human involvement. We provide metrics for the quantitative
assessment of selected properties and show them through different agen-
tic implementations of a predictive light sensing scenario in CPEE and
a blood donation scenario in Langchain. Altogether, this work aims at
providing properties and metrics to decide on and assess the design and
implementation of agentic orchestrations and orchestration of agents.
Keywords:Agentic Orchestration·Agentic Workflow·Orchestration
of Agents·Process-Awareness·Agentic BPM·LLM Agents
1 Introduction
Recently, Agentic Business Process Management (ABPM) has gained increased
attention, resulting in manifestos and perspectives [2,3,18]. In the ABPM area,
agents have been employed for the design and redesign of process and agentic
orchestrations [6,14,10,11] as well as for agentic process automation (cf. [13] and
autobpmn.ai). In doing so, the ABPM approaches adopt a top-down perspective
by conceptualizing an explicit model for the agentic orchestration. This, in turn,
provides the opportunity to define frames for agentic orchestration (7→framed
autonomy), trace their execution, and give assurances regarding the correctness
of outputs. Simultaneously, tools such ascrewai.comorlangchain.comhave
been developed to support the implementation and execution of agent orches-
trations. They follow a bottom-up approach where a frame is added to improve
results when implementing agent orchestrations.
However, for both, ABPM and tools, a systematic classification framework to
assess different modeling and implementation options for agentic orchestrations
is missing, e.g., deciding which functionality is realized by an agent or which
agent requires a frame. Choosing an option in an ad-hoc manner can result in
arXiv:2606.31518v2  [cs.AI]  26 Sep 2026

2 S. Rinderle-Ma et al.
insufficient solutions w.r.t. agent properties such as specificity, autonomy, and
reactivity on the one side and process properties such as traceability and correct-
ness assurance on the other side. Hence, in this work, we combine properties of
agents [15] with process properties on framed autonomy [2] as well as properties
of human involvement [18] and assess them along the followingOrchestration
Options (OO)for realizing scenarios by agents and their orchestrations, illus-
trated in Fig. 1. Note that the transition between the OOs can be fluid, especially
if the process is declarative, resulting in a solution similar to [7].
OO1 Process-agnosticAgenticOrchestration:Oneagentorchestratesmul-
tiple work steps, using, for example, protocols such as MCP (Model Context
Protocol)1 for tool connection and A2A (Agent-to-Agent)2 for agent collab-
oration. The agent is not aware of any explicit process frame or logic.
OO2 Process-Aware Agentic Orchestration:An agent executes a process
orchestration and is (partly) aware of a frame for the execution, stemming
from, e.g., regulatory documents or Service Level Agreements (SLAs). No
additional frame, “outside the agent” is provided.
OO3 Orchestration of Process Agnostic Agents:A (partial) process spec-
ification serves as frame in which AI agents are invoked. The agents them-
selves are process-agnostic.
OO4 Orchestration of Process-Aware Agents:An explicitly defined pro-
cess orchestrates agents that autonomously execute tasks or sub processes.
The agents themselves can also be aware of a frame or process.
Fig. 1.Classification of Options for Agentic Orchestration and Orchestration of Agents
The remainder is as follows: Section 2 defines the orchestration options de-
picted in Fig. 1 and enriches the classification framework with properties from
1 https://modelcontextprotocol.io/docs/getting-started/intro
2 https://a2aprotocol.ai/

Agentic Orchestration 3
agent [15] and process [2,18] literature. The properties are qualitatively as-
sessed along a predictive light-sensing scenario. Implementations of OO1–OO4
for the predictive light-sensing scenario, using process enginecpee.org, are pro-
vided in Sect. 3. Metrics for quantitatively assessing the properties are added
to the framework in Sect. 4 and evaluated for the predictive light sensing im-
plementations. Section 5 implements a complex blood donation scenario using
langchain.comto demonstrate the generalizability of the classification frame-
work. Section 6 discusses related work, Sect. 7 closes with a summary.
2 Properties of Agentic Orchestrations Options
We start by providing a definition for the orchestration options depicted in Fig.
1 in order to derive significant properties in the following.
Definition 1 (Agentic Orchestration).LetAbe the set of all LLM agents,
Hthe set of all human agents,Sthe set of all other services, andPthe set of
all process orchestrations described by an orchestration notation such as BPMN
or process trees. An agentic orchestrationAO:= (A, po, ho, P a, P)comprises:
one or several agentsA⊆ A; a (potentially empty) process orchestrationP; a
certain degree of process-supportpo:P7→N 0, wherepo= 0implies that the
level of process-support is unknown (i.e., hidden in the model logic), whilepo >0
implies that more orchestration logic is handled explicitly 3; and a certain level of
human involvementho∈{implicit, explicit} where implicit refers to monitoring
and input provision and explicit refers to invocation of human agents. Moreover,
letpa:A7→ {aware, agnostic}andP a={(a, pa(a))|a∈A}determine for each
agent in AO whether it is process-aware or agnostic. If po=explicit, thenP∈ P
describes the process orchestration based onA∪H∪S; if ho=explicit,H⊆ H
denotes the set of involved human agents (otherwise:H=∅);S⊆ Sif other
services are involved (otherwise:S=∅).
Consider the orchestration options depicted in Fig. 1: Given two AgentsA
andB, an AO under orchestration option OO could be defined as AOOO1 =
({A}, 0, implicit, {(A, agnostic)},∅), AOOO2 = ({A}, 0, implicit, {(A, aware)},
∅), AOOO3 = ({A,B},po >0, explicit, {(A, agnostic), (B, agnostic)}, P on {A,
B, Service, User Task}), and AOOO4 = ({A,B},po >0, explicit, {(A, aware),
(B, aware)}, P on {A,B, Service, User Task}). The properties of an AO under
orchestration option OO can be derived from properties of the involved agents,
processes, and human involvement.
Agent Propertiescomprise autonomy, task specificity, and reactivity [15].Au-
tonomyrefers to the ability to take decisions with minimal human intervention.
The autonomy of an agent can be restricted by a frame (i.e., framed autonomy
[2]). The frame can be realized using rules in a declarative process description or
by imperative process fragments. The autonomy of an agent could be measured,
for example, by the number of decisions an agent can take. However, as agent be-
havior is often black box, it is hard to estimate the full decision space. Autonomy
3 We propose two metrics to calculate the degree of explicit process support in Sec. 4

4 S. Rinderle-Ma et al.
is connected totask specificityof agents which refers to the granularity an agent
is operating on. For OO3 and OO4, task specificity is mapped to the granularity
of the process tasks which invoke the agents, i.e., we can describe the degree of
process-support by analyzing how much orchestration logic is handled explicitly.
As such, in Sect. 4, we propose and investigate Cyclomatic complexity [12] and
ABC Complexity [5] as metrics to assess task specificity.Reactivityrefers to the
ability of an agent to respond to environment changes and can be most probably
only observed during runtime. We propose to use reactivity-speed as a metric to
partially capture reactivity in Sect. 4.
Process Propertiesrefer to properties that are induced by frames and pro-
cesses according to [2] and include (among others) correctness assurance and
traceability.Correctness assurancerefers to the ability to give guarantees for
an achieved state or outcome. It can be assessed using precision, recall, and F1
score.Traceabilityrefers to the ability to understand whya decision in the agen-
tic orchestration was taken and how a certain state or outcome was achieved.
We propose to assess traceability based on the event logs generated by executing
the agentic orchestration compared to all events that have actually occurred.
Human Involvement Propertiesinclude, according to [18], human-agent col-
laboration and balance as well as involvement of humans.Human-agent collab-
oration and balancemeans to establish clear responsibilities and leverage on the
strengths of both, agent and human. Moreover, this property refers to enabling
humans to act in case of agent failure.Human-agent involvementcan range from
human as peer of the agent to human as its supervisor. For OO1 and OO2, the
human involvement refers to the providing input to the agent and to human tasks
potentially being invoked by the agent. For OO3 and OO4, the explicit process
definition contributes to a clear picture on which tasks are invoking an agent,
service, or human task. A simple metric could be to calculate some ratio between
agent and human tasks. Moreover, data flow dependencies between agent and
human tasks can be analyzed. Due to space, we will not provide quantitative
metrics for human involvement in Sect. 4, but in future work.
In the following, we illustrate each OO based on a light sensing agent orches-
tration similar to the scenarios described in [1,15]:
BASIC (OO1)
Ambient light conditions are constantly measured by light sensors. Depending
on the light intensity, the light in the room is switched on, off, or maintained.
BASIC can be realized by OO1, i.e., by process-agnostic agentic orchestration
where the agent orchestrates and executes services and other agents, possibly via
protocols such as MCP, and can take input from users. No process logic or frame
is defined, i.e., AOOO1 = ({Agent}, 0, implicit, {(Agent, agnostic)},∅)
BASIC (OO1)Agent Properties:As the agent in OO1 acts independently of
any frame or process, its autonomy and reactivity are high, and the task speci-
ficity might be medium to low. Due to the low task specificity, the functionality

Agentic Orchestration 5
could be also realized by a service instead of an agent, especially if the rules for
switching the light on/off are fixed.
BASIC (OO1)Process Properties:As the agent behavior is black box, OO1
is low in traceability, tractability, and correctness assurance, i.e., we can neither
provide information on how an outcome was achieved nor give any assurances on
the outcome correctness or quality. In BASIC, this means that we can observe
the outcome, i.e., light on or off, but not reproduce why.
BASIC (OO1)Human Properties:Human involvement is confined to possible
prompting. BASIC does neither require human oversight of internal steps nor
involves human work/actions.
Assume now that a condition on switching the light off after a certain period
of time is added to BASIC, resulting in FRAME:
FRAME (OO2)
Ambient light conditions are constantly measured by light sensors. Depending
on the light intensity, the light in the room switched on, switched off, or
maintained. If the light has been on for 10 hours, it should be switched off.
FRAME could be realized by OO2 where the agent is aware of a frame
given by, e.g., process descriptions, regulatory documents, or documentations.
The frame can be directly included in the prompt or extracted from additional
sources by the agent, i.e., AOOO2 = ({Agent}, 0, implicit, {(Agent, aware)},∅).
FRAME (OO2)Agent Properties:The autonomy and reactivity might be
restricted when compared to OO1 due to the imposed frame. Task specificity
remains similar.
FRAME (OO2)Process Properties:As OO2 is aware of a frame, this results
in higher traceability and tractability while the autonomy of the agent is still
high. The frame might result in reduced reactivity, especially if it restricts the
action space to react on changes in the environment. For FRAME, this might be
the case if the outside light conditions become suddenly very dark, e.g., due to a
thunderstorm, but the lighting has been on for10hours. Correctness assurance
might be the same or a bit higher than for OO1, depending on the influence of
the frame on the outcome of the agentic orchestration.
FRAME (OO2)Human Properties:Human involvement is confined to pos-
sible prompting. OO2 does neither include human oversight of internal steps
and/or human interaction nor involves human work/actions.
Assume that FRAME is augmented with an initial collection of user prefer-
ences, resulting in FRAME-USER:
FRAME-USER (OO3)
User preferences regarding the lighting in the building are collected. Ambient
light conditions are constantly measured by light sensors. Depending on the
light intensity and user preferences, the light in the room is switched on,

6 S. Rinderle-Ma et al.
switched off, or maintained. If the light has been on for 10 hours, it should
be switched off.
We can realize FRAME-USER using OO3 with an agent that handles the
user preferences and is process-agnostic. The frame, i.e., switching off the light
after10hours, is realized by embedding the agent into a process orchestration.
FRAME-USER (OO3)Agent and Process Properties:For OO3, the frame
realized by the orchestration can provide increased correctness assurance. In the
example, it can be ensured that the light is switched off for sure after 10 hours.
Deciding which parts of the frame are realized “outside” the agent is related to
deciding on the decision space of the agent and hence on its autonomy, reactivity,
and task specificity. As the agent itself is process-agnostic and rather black box,
the behavior realized by the agent lacks traceability and tractability.
FRAME-USER (OO3)Human Properties:OO3 could be desirable for sce-
narios that do not require human oversight of certain steps, but involve human
work/actions.
We now extend the light sensing example to a smart building example by
additionally collecting user preferences regarding the temperature and turning
the heating on/off accordingly:
ORCHESTRATE (OO4)
<FRAME-USER>. In parallel, the room temperature is measured and the
heater is turned on/off based on collected user preferences.
ORCHESTRATE can be realized by OO4 where (multiple) agents are in-
voked by a process orchestration (frame) and are process-aware themselves.
ORCHESTRATE (OO4)Agent and Process Properties:OO4 refers to the
(framed) orchestration of process-aware AI agents, resulting in actions spaces of
varying autonomy of multiple agents, higher correctness assurance, and higher
traceability and tractability.
ORCHESTRATE (OO4)Human Properties:OO4 could be desirable for sce-
narios that include human oversight of internal steps and/or human interaction
as well as involve human work/actions.
Note that the options for realizing the different scenario variants BASIC,
FRAME, FRAME-USER, and ORCHESTRATE are fluid, i.e., different options
can be chosen for the different scenarios. It would be also possible to realize the
scenario entirely without an agent, i.e., by a process orchestration.
3 Design and Implementation of Agentic Light Sensing
This section designs, implements, and simulates OO1–OO4 (cf. Fig. 1) for the
predictive light sensing scenario introduced in Sect. 2: we consider a cyber-
physical scenario which measures lighting based on lux (Lumens Area ), movement,
and occupancy count inside a room and adjusts the lumen according to the sen-
sor values, user inputs and/or specifications (which are either integrated into

Agentic Orchestration 7
the frame, process orchestration, or can be considered via using MCP tools) us-
ing an LLM agent. We create an artificial dataset consisting of x measurement
events, for which occupancy count and movement is assumed minimal during
night hours. For each measurement we calculate a range of ground truth lu-
men values according to the set of rules in Tab. 1 using the assumption of a
single lamp that can produce any lumen value between 0 and 5000 and is po-
sitioned at 3 meters above the floor with a circular beam angle of60 ◦ that
uniformly covers the entire room4. To simulate real sensors, the measurement
events and a lamp endpoint are provided via REST interfaces, which are con-
nected to an LLM agent via MCP. We experimented with the following LLMs,
i.e.,mistralai/Ministral-3-14B-Reasoning-2512,google/gemma-4-31B-it,
Qwen/Qwen3.6-35B-A3B, andqwen-35-35b-coding. Details on the implementa-
tion can be found on GitHub5.
Prio Condition Consequence
0 User input present React to user input request
1 Occupancy<1and current lumen == 0 Do not change lamp lumen
2 Occupancy<1and current lumen =! 0 Set lumen to0
3 Night (23–6) and movement detected Target50lux
4 Night (23–6) and no movement Set lumen to0
5 Morning (6–9) and occupancy≥1Target100–200lux
6 Midday (9–14) and occupancy≥1Target300–500lux
7 Afternoon (14–18) and occupancy≥1Target200–300lux
8 Evening (18–23) and occupancy≥1Target200–300lux
9 Else: (default deny) Do not change lamp lumen
T able 1.Rules considered as the ground truth for the lighting scenario using default
deny semantics. User-input rule 0 is only applicable in the LLM-based variants.
For implementing OO1, the agent is not framed and contains minimal context
information through the following prompt which refines BASIC in Sect. 2:
PROMPT OO1 (→BASIC)
Adjust the lighting based on standard guidelines for brightness during
day/night and sleep/being awake. Also consider that the light should be
turned on whenever it is dark and I want to go somewhere! Make sure this
is done for the next 72 seconds which corresponds to 12 hours in simulated
time (check for the conditions every second - i.e., every 10 minutes in simu-
lated time)! Log the tools you use along with their parameters (apart from
the logging tool itself)!
For OO2, the agent is not framed by a process, but aware of a frame provided
to the agent via context information through the following prompt:
4 Lux formula: Lux= Lumens 2π(3)2(1−cos(30◦)) = Lumens 18π  1− √ 3 2  ≈ Lumens 7.5761
5 https://anonymous.4open.science/r/AgenticProcessOrchestration/README.md

8 S. Rinderle-Ma et al.
PROMPT OO2 (→FRAME)
Adjust the lighting based on the following rules: Do not change the lumen
of the lamp unless any of the following rules hold: (1) If there is user input
react to user input, (2) If the occupancy is less than 1 then lower lumen to 0,
(3) In the night (23-6) if there is movement aim for 50 lux, (4) In the night
(23-6) if there is no movement lower lumen to 0, (5) In the morning (6-9) if
occupancy is greater or equal 1 then aim for 100-200 lux, (6) during midday
(9-14) if occupancy is greater or equal 1 then aim for 300-500 lux, (7) In
the afternoon (14-18) if occupancy is greater or equal 1 aim for 200-300 lux,
and (8) In the evening (18-23) if occupancy is greater or equal 1 then aim for
200-300 lux! Make sure this is done for the next 72 seconds which corresponds
to 12 hours in simulated time (check for the conditions every second - i.e.,
every 10 minutes in simulated time)! Log the tools you use along with their
parameters (apart from the logging tool itself)!
For the implementation of OO3 and OO4, the agent is framed by a process
illustrated in Fig. 2 that ensures some rules are deterministically enforced, either
provided a simple prompt for OO3 or a complex prompt for OO4 (without the
deterministically enforced rule). Note that here the scenario partly deviates from
the simplistic descriptions in Sect. 2.
PROMPT OO3
It is currently {time}, the lamp is currently at {current} and the current am-
bient lux is at {ambient}. Return a lumen value based on standard guidelines
for brightness during day/night and sleep/being awake. Also consider that the
light should be turned on whenever it is dark and I want to go somewhere!
Return just the lumen value as an int.
PROMPT OO4
It is currently {time}, the lamp is currently at {current} and the current
ambient lux is at {ambient}. Return the lumen value that a lamp should take
according to the following rules: (1) If it is night, turn of the Light if it is
running. (2) If it is morning aim for 100-200 lux, (3) If it is midday aim for
300-500 lux, (4) If it is afternoon aim for 200-300 lux, and (5) If it is evening
aim for 200-300 lux! Return just the Lumen Value as an Int.
Finally,toprovideabettercomparisonwecreateapurelydeterministic(man-
ually modeled) version of OO4 denoted asGT, which correctly enforces rules
1→9 (cf.6).
Evaluation and Conclusion:The design and implementation of the scenarios
show the feasibility of the framework presented in Fig. 1. Moreover, the following
qualitative observations have been made: (1) higher autonomy is often assumed
for agent solutions, but the actual information and action space of agents is
6 https://cpee.org/hub/server/Papers.dir/AgenticFundamentals.dir/005.xml/open?stage=view

Agentic Orchestration 9
GetSensor
night & no motion & light off
Set umen to 0
night & no motion & ight on
m_ca
user input no occupancy & ight off
Set umen to 0
no occupancy & ight on
m_ca
change umen
wait for next
event
True
otherwise
AI Agent
 Service
Legend:
Fig. 2.Orchestration of agents for lighting scenario implementation (OO3 and OO4)
clearly restricted through the connected tools, which have to be connected like
in a traditional workflow orchestration. (2) Any temporal constraints are chal-
lenging to enforce, as the reasoning times of LLMs are unpredictable, so they
require frames/tools to enforce temporal relationships. (3) Relying on agents for
logging is generally not recommended, even when logging tools are provided.
(4) It is challenging to control the LLM context window for long workflows. (5)
The less framed the orchestration the more challenging it is to debug, due to
the different software layers which require extensive boilerplate code to ensure
messages are correctly propagated (i.e., LLM-Agent calls MCP tool, which calls
a REST service, which connects to a MQTT server, which connects to a sen-
sor). (6) The less framed the orchestration, the more confounding variables via
textual descriptions are added. (7) An unframed orchestration does not require
translating textual requirements into a formal language.
4 Metrics for Orchestration Option Assessment
Section3discussestheagent,process,andhumanpropertiesintroducedinSect.2
for the lighting scenario in a qualitative way. To additionally enable their quanti-
tative assessment along the metrics in Fig. 3, we propose first metrics to capture
task specificity, correctness, reactivity, and traceability, whereas autonomy and
tractability are subject to future work. Figure 3 shows how the scenarios (i.e.,
Agentic Orchestration as in OO1 and OO2 as well as Orchestration of Agents as
in OO3 and OO4) are implemented and on which data the calculation of metrics
is based. A represents the ground truth (manually created based on rules 1→9),
B the logs created by the invoked (either by the agent in the case of Agentic
Orchestration or by the Process Execution Engine in the case of Orchestration
of Agents) services (e.g. check the light sensor or change the lumen), andC the
logs created by the orchestrator (i.e., either the Agent or Process Execution En-
gine). Execution Metrics are calculated based on a comparison betweenA , B ,

10 S. Rinderle-Ma et al.
and C while Structural Metrics are based on analyzing the specification of the
underlying scenario. We present proposed metrics with associated calculation
methods and their values based on10runs of the implemented Agentic Light
Sensing Scenario (Sect. 3) using thegoogle/gemma-4-31B-itmodel below.
MCP HTTP
 AgentUser Input
Agentic Orchestration
LOG B
Services Human Tasks
Environment
Execution Metrics
• Correctness: B vs P,R,F1A
B• Reactivity:vs RsA
• Traceabiity: Δevent_typeC vs B
Structura Metrics
• T ask Specificity:
M  8722  5,
Process ExecutionEngine
enacts
Process Mode
Orchestration of Agents
User T askService  Agent A
X X
 Agent B
Input
LOG CLOG A
M,〈A, B, C〉vsAgent Process Mode
〈0, 4, 1〉 〈A, B, C〉= ⇒ |4.12|
M  0  0  2 ∗ 1  2,
〈0, 1, 0〉 〈A, B, C〉= ⇒ |1.00|
Fig. 3.Overview of Proposed Metrics
Task Specificity:As illustrated in Fig. 3, we propose two structural mea-
sures for task specificity of agent orchestrations based on well-established soft-
ware complexity measures, i.e., the Cyclomatic complexityM[12] and the ABC
Complexity⟨ABC⟩[5]. The intuition is to consider a (potentially imagined)
process that surrounds the agent orchestration: In the case of orchestrations in
OO1/OO2, the agent(s) are not included in a surrounding process, and as such
the task specificity is minimal, while if the agents are included in a workflow
(such as in a process orchestration of style OO3/OO4), the task specificity in-
creases depending on how much agent logic is moved to the process logic. As the
amountoflogicintheprocesscanbecapturedusingsoftwarecomplexitymetrics,
they can be used to compare the task specificity of different agent orchestrations
for a process/workflow. An overview of different example orchestrations with the
respective measures is in Tab. 2 and calculation scripts are provided on GitHub5.
The Cyclomatic complexity of a process is defined asM:=E−N+2Pwhere
Erefers to the number of edges andNto the number of nodes on the longest
path resp., andPrefers to the number of connected components. ForMit is
irrelevant whether the start/end nodes as well as its connectors are considered
for the process model as they add a single node/edge each and thus cancel
out. The same applies regarding whether every decision/parallel leads back to
a decision/parallel (i.e., block structuredness) or directly to the next node. For
OO1 and OO2, i.e., a single agent without any process frame, the agent is the
only connected component; thus:M= 0−0 + 2∗1 = 2. For OO3 and OO4,
the task specificity increases depending on how much logic is explicitly included
in the process model vs how much logic is implicitly left to the agent. E.g., in
Fig. 3, the orchestration model has 8 Edges, 7 Nodes on the longest path and 2
agents (software components), i.e.,M= 8−7 + 2∗2 = 5.
ABC complexity has been proposed as a metric that can be calculated in
a single pass over the data structure (O(N)) while presenting better insights
and being more adaptable than other simple metrics such as lines of code. ABC

Agentic Orchestration 11
metric is defined as the vector⟨A, B, C⟩where|A|is the amount of Assign-
ments,|B|the amount of Branches, and|C|is the amount of Conditionals, with
the associated ABC score defined as its scalar|ABC|=
√
A2 +B 2 +C 2. As
branches in this context are explicit forward program branches out of scope of
the original program, we can interpretBas the set of activities and subprocesses
(including agents), whileCrefers to the set of exclusive, parallel, and loop op-
erators. Regarding assignmentsA, we consider only script tasks, which contain
(usually short) data object computations, as part ofA. This also enables using
different weights depending on the scenario. For example, it can make sense to
consider activities/subprocesses as making the orchestration less task specific
than moving logic into the process model by including it via operators. In this
case a weighted|ABC w|score such as|ABC w|=
√
A2 + 0.8∗B 2 +C 2 could
be appropriate. Similarly the metric can also be extended to enable different
weights depending on the type of activity. For example aABCDmetric, where
Dcontains all agent tasks can help highlight the degree of autonomy in addition
to comparing task specificity.
Both measures can be applied analogously to compare the task specificity as
defined in current frameworks like crewAI flows or AgentSDK workflow-patterns.
However, it is important to note thatMandABCprovide only a comparative
measure between flows/orchestrations of thesameprocess/workflow, and do not
have any semantic meaning when considering a single orchestration in isolation
or when comparing two orchestrations of different processes/workflows.
Correctness:For correctness, we consider standard execution metrics as illus-
trated using A and B in Fig. 3: We consider a true positive (TP) as an event
ethat was executed and required according to some set of rulesR(i.e.,e∈
B ∧e∈ A ) and a false positive (FP) as an event that was executed, but not
required according toR(e∈ B ∧e /∈A ). Regarding false negative (FN) we
differentiateF Nandtime-sensitiveF N t:F Nonly considers events that were
not executed, but required according toR(e /∈B ∧e∈ A ) and a previously
observed evente ′ (e /∈A ∧ ∃e′ ∈ B ∃r∈R:r=e ′ =⇒e), whileF N t fol-
lows the standardeexists in A but not in B . This differentiation is added, as
F Nt considers events that should have been observed by the orchestration, but
were missed as the agent was still processing a previously observed event as false
negatives, i.e.,F Nt depends on the available computing power. Meanwhile,F N
can be seen asidealFN value, which assumes infinite computing power, such
that the agents do not miss any events. As agents are expensive/slow in practice
we capture the high amount of missed events in time-critical applications using
F Nt. As such, we evaluate correctness using precisionP, recallR, time-sensitive
recallR t, and the combinedF1andF1 t scores calculated as:P= T P T P+F P,
R= T P T P+F N,R t = T P T P+F Nt ,F1 = 2∗ P∗R P+R,F1 t = 2∗ P∗R t P+R t .
Reactivity:We capture the reactivity-speedR s, defined as the average time
between an event that requires a consequence event, according toR.
Traceability:We consider traceability as the correctness of the log created
by orchestrators C compared with the actual execution log B . While this
could theoretically be captured usingP,R, andF1scores, in practice these

12 S. Rinderle-Ma et al.
are challenging to calculate, as event matching between the two logs, which use
different timestamps/IDs for the same event, is required. We instead compare the
amounts of events per type, captured using the mean and standard deviation
of the difference between B and C in Tab. 2 for every event type: “check
environment” (∆env) and “change lumens” (∆lum).
Metric OO1 OO2 OO3 OO4GT
P0.52±0.20 0.61±0.13 0.69±0.14 0.71±0.14 1.0±0.0
R0.39±0.34 0.58±0.27 1.0±0.0 1.0±0.0 1.0±0.0
Rt 0.16±0.19 0.25±0.19 0.18±0.05 0.29±0.10 1.0±0.0
F1 0.40±0.28 0.55±0.17 0.81±0.10 0.82±0.11 1.0±0.0
F1 t 0.21±0.21 0.33±0.18 0.28±0.07 0.41±0.11 1.0±0.0
Rs 5.46±3.16 4.30±1.45 5.37±2.99 4.41±2.04 0.12±0.01
∆lum 6.1±13.10 1.3±4.24 0.0±0.0 0.0±0.0 0.0±0.0
∆env 35.4±31.92 106.1±118.21 0.0±0.0 0.0±0.0 0.0±0.0
T able 2.Correctness and Reactivity Metric comparison of OO1–GT(cf. Sect. 3).
Results:Analyzing Tab. 2 and 3, we identify thatMandABCcorrectly cap-
ture task specificity as expected, i.e., an orchestration where the agent is only
responsible for more specific cases has higherMandABCscores. Comparing
them we find theABCmetric more useful and adaptable whileMcan capture
the basic relationship in a single value. Regarding correctness, we see how con-
text information always improvesPandR, while including a frame also requires
additional context information to improve correctness. Regarding reactivity, we
cannot identify any relevant information becauseRs depends on too many other
factors such as model load, which are not accounted for. Analyzing traceability
we identify that agents do not generate reliable event logs when provided logging
tools (∆ >0for OO1 and OO2). As such, we argue that logging functionalities
should always be handled through middleware instead, regardless of chosen OO.
Metric OO1 OO2 OO3 OO4GT CN COO4
M2 2 13 13 17 2 12
⟨A, B, C⟩ ⟨0,1,0⟩ ⟨0,1,0⟩ ⟨0,4,2⟩ ⟨1,5,2⟩ ⟨8,4,5⟩ ⟨0,1,0⟩ ⟨6,7,4⟩
|ABC|1.00 1.00 4.47 5.48 10.25 1.00 10.05
T able 3.Structural Metric comparison of OO1–GT(Sect. 3). and CN-COO4 (Sect. 5)
Threats to validity:We only present the results of initial experiments to il-
lustrate our proposed metrics which are subject to several glaring threats of
validity such as the lack of a comparison of different prompts, potential overfit-
ting in prompt engineering, confounding factors such as model load and network
delays, and the chosen models. It is especially important to highlight that for
the ground truth values we did not consider user inputs, which is the primary
reason for including an agent in this scenario.

Agentic Orchestration 13
5 Complex Real World Scenario: Blood Donation
Wefinallyillustrateacomplexrealworldscenario,basedonguidelinesfortheuse
and quality assurance of blood components given in the European Blood Guide7.
Inthisguide,thedonor registrationprocessisstrictlyregulatedandconsistsboth
of activities that can be automated, such as the identify verification and the
provision of relevant information, as well as human tasks where the physician
in charge of the blood donation has to make the final eligibility decision in
specific cases identified through a questionnaire. An OO4 framed/aware agent
orchestration of this process is illustrated in Fig. 4.
Stop Donation
Process
Verify Identity
Provide
Information
Answer User
Queries
 Obtain Consent
Direct Acceptance
Direct Rejection
 Physician
New Potentia Donor
Present Consent
Options
Digita Signature
 Voca Consent
 Signature
Unsuccessfu
Obtain Consent
Offer Verification
Options
FaceScan ID
 Digita ID
Verification Faied
Verify Identity
AI Agent
Agentic
Subprocess
Human Task
Service
Legend:
Conduct Interview
and Questionnaire
Donor Registration
Process
Fig. 4.Process-framed Agentic Blood Donor Registration based on the Blood Directive
(2002/98/EC) & Blood Guide6, May 21. 2026).
A naive orchestration of this scenario would be a single agent with connected
tools and the task tocomplete the registration of a blood donor. In this
scenario, such an unframed/unaware orchestration is unacceptable as there are
strictexecutionanddocumentationrequirementsenforcedbytheblooddirective.
Providing context information, by e.g., uploading the Blood Guide to a vector
database for a Retrieval Augmented Generation Agent orchestration would likely
improve the behavior, but still entails unacceptable risks. Specifically essential
tasks such as a donor always having the opportunity to retract their consent and
abort the donation should be deterministically enforced. As such a framed solu-
tion (i.e., Fig. 4), where the stopping is enabled through a service in parallel with
different agents orchestrated in a workflow is appropriate in this case. A further
question then becomes which task specificity is appropriate for this solution.
For example, the identity verification and the obtaining of consent, can be both
7 https://www.edqm.eu/en/blood-guide

14 S. Rinderle-Ma et al.
pure single agents with connected tools, purely deterministic, agents with ad-
ditional context information or agentic sub-processes, where a frame surrounds
the agent to restrict which choices can actually be taken. However, there are
also tasks where a purely deterministic solution is unsuited, as the constraints
enforce that potential donors have the ability to ask questions regarding the
nature of blood donations, which is suitable for a LLM agent. We implement
the naive (CN in Tab. 2) and a OO4 framed-orchestration solution (COO4 in
Tab. 2) using langchain8 and various simple simulators for different service end-
points, to illustrate how the cyclomatic complexity and ABC metric can also
be used to compare the task specificity of AOs implemented in commonly used
orchestration frameworks9. Due to the use of several simple simulators, we did
not calculate correctness, reactivity, and traceability for CN and COO4.
6 Related Work
The majority of ABPM approaches focus on agentic process modeling and min-
ing, e.g., [14,10,11,16,17,13], and are complementary to this work. Only few
ABPM approaches address the realization and implementation perspective of
agentic orchestrations focusing instead on high level architectures such as [9]. In
[7], the authors propose a chain instructor that creates a sequence of steps for a
given task to be executed by an agent. This is related to OO2. [4] explore the
applicability of conceptual modeling techniques for agent orchestrations via sev-
eral (partially implemented) scenarios which can be classified according to our
framework. [8] extract a set of rules from text to augment RPA tasks (OO2 or
OO3). By contrast, commercial tools such as Langchain, CrewAI, Agents SDK,
Atomic Agents, Pydantic AI, and Agent Development Kit have focused on the
implementation of agentic orchestrations. In an extensive survey of orchestra-
tion frameworks, [19] present decision criteria for choosing the right orchestra-
tion framework, considering ABPM-style frameworks as hierarchical frameworks
suitable in scenarios with several agents and a known structure at design time.
7 Conclusion
According to Gartner10 “[o]ver 40% of agentic AI projects will be canceled by the
end of 2027, due to escalating costs, unclear business value or inadequate risk
controls”.Hence,the systematic assessment of agentic orchestration options is in-
dispensable for choosing the right implementation for a given scenario. This work
provides a first framework with properties and related metrics. Their feasibil-
ity has been demonstrated on two real-world scenarios and two implementation
frameworks. In future work, we will complement the framework with metrics for
human involvement and test it for more real-world applications. Moreover, we
8 https://github.com/langchain-ai/langchain
9 Implementation details on GitHub in the ComplexScenario folder
10 https://tinyurl.com/mrxkr639

Agentic Orchestration 15
will investigate other process modeling paradigms such as object-centric, declar-
ative, and hybrid.
References
1. An, T., Zhou, Y., Zou, H., Yang, J.: Iot-llm: A framework for enhancing large lan-
guage model reasoning from real-world sensor data. Patterns7(1), 101429 (2026)
2. Calvanese, D., et al.: Agentic Business Process Management: A research manifesto.
Information Systems140, 102738 (2026)
3. Dumas,M.,etal.:AI-augmentedbusinessprocessmanagementsystems:Aresearch
manifesto. ACM Trans. Manag. Inf. Syst.14(1), 11:1–11:19 (2023)
4. Fettke, P., Köpke, J., Fill, H.:Llm, lam, lxmagent:Fromtalking toacting machines
insights from the perspective of conceptual modeling. Enterp. Model. Inf. Syst.
Archit.20(2025)
5. Fitzpatrick, J.: Applying the abc metric to c, c++, and java. More c++ gems pp.
245–264 (1997)
6. Grohs, M., Abb, L., Elsayed, N., Rehse, J.: Large language models can accomplish
business process management tasks. In: BPM Workshops. pp. 453–465 (2023)
7. Guan, Y., Wang, D., Chu, Z., Wang, S., Ni, F., Song, R., Zhuang, C.: Intelligent
agents with llm-based process automation. In: Knowledge Discovery and Data
Mining. pp. 5018–5027. ACM (2024)
8. Kaltenpoth, S., Skolik, A., Müller, O., Beverungen, D.: A step towards cognitive
automation: Integrating LLM agents with process rules. In: Business Process Man-
agement. pp. 308–324 (2025)
9. Kampik, T., Malhi, A.K., Främling, K.: Agent-based business process orchestration
for iot. In: WI. pp. 393–397. ACM (2019)
10. Klievtsova, N., Kampik, T., Mangler, J., Rinderle-Ma, S.: Conversational process
model redesign. Int. J. Cooperative Inf. Syst.35(1), 2650004:1–2650004:37 (2026)
11. Kourani, H., Berti, A., Schuster, D., van der Aalst, W.M.P.: Promoai: Process
modeling with generative AI. In: Artificial Intelligence. pp. 8708–8712 (2024)
12. McCabe, T.J.: A complexity measure. IEEE Transactions on software Engineering
(4), 308–320 (1976)
13. Monti, F., Leotta, F., Mangler, J., Mecella, M., Rinderle-Ma, S.: Nl2processops:
Towards llm-guided code generation for process execution. In: Business Process
Management Forum. pp. 127–143 (2024)
14. Nivon, Q., Salaün, G.: Automated generation of BPMN processes from textual
requirements. In: Service-Oriented Computing. pp. 185–201 (2024)
15. Sapkota, R., Roumeliotis, K.I., Karkee, M.: AI agents vs. agentic AI: A conceptual
taxonomy, applications and challenges. Inf. Fusion126, 103599 (2026)
16. Shen, Q., Polyvyanyy, A., Lipovetzky, N., Kampik, T.: Agent system event data:
Concepts, dimensions, applications. In: Conceptual Modeling. pp. 56–72 (2024)
17. Tour, A., Polyvyanyy, A., Kalenkova, A.A., Senderovich, A.: Agent miner: An
algorithm for discovering agent systems from event data. In: Business Process
Management. pp. 284–302 (2023)
18. Vu, H., Klievtsova, N., Leopold, H., Rinderle-Ma, S., Kampik, T.: Agentic business
process management: Practitioner perspectives on agent governance in business
processes. In: Responsible BPM Forum. pp. 29–43 (2026)
19. Zhu, Y., Liu, L., Yu, J., Zhang, D.: Llm-based multi-agent orchestration: A survey
of frameworks, communication protocols, and emerging patterns. Future Internet
18(6) (2026)
