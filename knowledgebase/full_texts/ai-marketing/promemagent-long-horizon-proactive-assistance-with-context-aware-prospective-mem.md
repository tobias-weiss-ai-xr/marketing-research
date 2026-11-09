---
title: 'ProMemAgent: Long-Horizon Proactive Assistance with Context-Aware Prospective Memory from Sensory
  Perceptions'
url: https://arxiv.org/abs/2610.27400
category: ai-marketing
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Lilin Xu
- Linyang He
- Kaiyuan Hou
- Yuang Fan
- Minghui Zhao
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.27400
pages: 18
chars: 81735
fetched_at: '2026-11-08T13:31:37+00:00'
kb_version: 1
---

# ProMemAgent: Long-Horizon Proactive Assistance with Context-Aware Prospective Memory from Sensory Perceptions

ProMemAgent: Long-Horizon Proactive Assistance with Context-Aware
Prospective Memory from Sensory Perceptions
Lilin Xu Linyang He Kaiyuan Hou Yuang Fan
Minghui Zhao Xuhai Xu Xiaofan Jiang
Columbia University
{lilin.xu, linyang.he, kh3119, yf2676, mz2866, xx2489}@columbia.edu
jiang@ee.columbia.edu
Abstract
Large language model (LLM) agents are mov-
ing beyond reactive responses toward proac-
tive assistance that anticipates user needs with-
out explicit requests. However, existing proac-
tive agents primarily address immediate needs,
while many everyday situations involve delayed
intentions that can only be acted on hours or
days later. Humans handle such intentions
through prospective memory, the ability to re-
member to act on an intention when the right
moment arises. In this paper, we introduce
ProMemAgent, the first proactive agent to in-
corporate prospective memory over everyday
sensory contexts for long-horizon proactive as-
sistance. ProMemAgent organizes past sen-
sory perceptions (e.g., egocentric video and
audio) into context-aware memory, generat-
ing prospective cues and linking earlier events
with subsequent developments for future re-
trieval. Given the current context, it retrieves
relevant past events and performs memory-
augmented proactive reasoning to determine
whether assistance is needed. We further intro-
duce CPMBench, the first benchmark for eval-
uating long-horizon proactive assistance over
sensory contexts, comprising 1,000 instances
across eight everyday categories. 1 Extensive
experiments show that ProMemAgent achieves
the best memory retrieval performance and
consistently outperforms all baselines on long-
horizon proactive assistance.
1 Introduction
Large language model (LLM) agents are moving
beyond reactive responses toward proactive assis-
tance, anticipating user needs and initiating assis-
tance without explicit queries. Existing proactive
agents operate across digital interactions, such as
desktop workflows and mobile interfaces (Lu et al.,
2025; Lyu et al., 2026), and more recently extend
to everyday environments through sensory contexts
1Our dataset and code will be released upon acceptance.
Reactive LLM Agents Existing Proactive Agents
ProMemAgent(Ours): Long-Horizon Proactive Assistance
Explicit Request Required Immediate Needs within the Current Context
Remind me to buy oat milk
when I’m at grocery store.
Sure,tell me when you
arrive, and I’ll remind you.
Implicit Delayed Intention
fromSensory Context
Long-Horizon Assistance over
Context-Aware Memory
Current
Context
Want me to check
the next bus?
Sensory
Context
Context-Aware Memory
of Daily Life
Current
Context
Mon
4 p.m.
…… …
 6p.m.
Personal
Context
Historical
Context
…
You’re out of oat milk
on Tuesday. Want to
grab some at this store?
Wearable
& Mobile
User is walking near a
bus stop and store.
Tue
9 p.m.
Fri
7a.m.
Memory Persona
Figure 1: Comparison of prior work (top) and ours (bot-
tom). Reactive agents require explicit requests, and prior
proactive agents address immediate needs. ProMemA-
gent incorporates context-aware prospective memory to
connect current and historical contexts and assist with
implicit delayed intentions at the right moment.
captured by wearable devices (Yang et al., 2025c,
2026b). However, these agents primarily address
needs that can be inferred and acted on at the same
moment, using historical information mainly to
better infer such needs. Many assistance needs are
instead long-horizon, with their emergence and the
opportunity for action separated by hours or days
of unrelated daily activities. For example, a user
may run out of oat milk and later pass a grocery
store, or need to tell a colleague something and
only later run into them at work.
This temporal separation closely relates to
prospective memory, the human ability to remem-
ber to act on a delayed intention at an appropri-
ate future moment (McDaniel and Einstein, 2000;
Einstein and McDaniel, 2005). Recently released
agents such as Meta’s Muse (Meta, 2026a) and Ope-
nAI’s Dots (OpenAI, 2026a) follow up on users’
goals over time, but still largely rely on users to
explicitly articulate their intentions. Yet many de-
layed intentions arise naturally in everyday life and
arXiv:2610.27400v1  [cs.AI]  19 Oct 2026

are not always stated. Proactive agents can instead
infer such intentions from the user’s everyday con-
text, reducing the need for explicit requests. This
motivateslong-horizon proactive assistance, where
agents connect past and current contexts to identify
opportunities to act on implicit delayed intentions,
as illustrated in Fig. 1.
Making this connection is challenging. Re-
cent work shows that LLMs struggle to reliably
trigger delayed intentions as context length in-
creases (Zhang et al., 2026). Memory retrieval
offers a way to access relevant past information
without processing the full history. However, with-
out an explicit query, the current context serves
as the primary retrieval cue and may be only indi-
rectly associated with the earlier context in which
a delayed intention arose, limiting similarity-based
retrieval. Recent studies on associative memory
move beyond surface similarity (Li et al., 2026;
Guo et al., 2026), but still largely rely on explicit
queries in conversational settings. Therefore, a re-
search gap remains in developing proactive agents
that can retrieve relevant past events based on the
current sensory context and determine when im-
plicit delayed intentions can be acted on.
In this paper, we proposeProMemAgent, the
first proactive LLM agent to incorporate context-
aware Prospective Memory for long-horizon proac-
tive assistance over sensory contexts. ProMemA-
gent first extracts sensory contexts from multi-
modal perceptions captured by wearable and mo-
bile devices. It then constructs context-aware
memory by generating event-based and time-based
prospective cues, and linking earlier events with
their subsequent developments. Given the cur-
rent context, ProMemAgent retrieves relevant past
events through cue-triggered retrieval, and uses a
memory-augmented proactive reasoner to decide
whether any implicit delayed intention should be
acted on. By connecting past experiences with cur-
rent opportunities for action, ProMemAgent takes
a step toward proactive assistants that serve as ex-
ternal prospective memory in everyday life.
To evaluate long-horizon proactive assistance,
we further introduce CPMBench, a Context-aware
Prospective Memory benchmark containing 1,000
instances across eight everyday categories (i.e.,
work, leisure, social, health, food, shopping, transit,
and daily life). We compare ProMemAgent with 19
baselines from proactive agents, full-context LLMs,
RAG-based methods, and memory systems. Exten-
sive evaluation shows that ProMemAgent achieves
state-of-the-art performance in memory retrieval
and long-horizon proactive assistance. We summa-
rize our contributions as follows.
• We introduce the research problem of long-
horizon proactive assistance, where implicit de-
layed intentions arise earlier and become action-
able only later, requiring agents to connect the
current situation with relevant past context.
• We propose ProMemAgent, the first proactive
agent that incorporates context-aware prospec-
tive memory over sensory contexts. It constructs
memory with prospective cues and cross-event
links for future retrieval, and uses a memory-
augmented reasoner to decide whether assistance
is needed for any implicit delayed intention.
• We introduce CPMBench, the first benchmark
for long-horizon proactive assistance over sen-
sory contexts. Extensive experiments show that
ProMemAgent achieves the best memory re-
trieval and outperforms the strongest baseline
on proactive assistance by 9.7 points in F1 score.
2 Related Work
Proactive LLM Agents.Proactive agents initiate
assistance without explicit user requests. Existing
work anticipates needs from interaction histories
in digital environments such as desktop workflows,
mobile GUIs, and multi-session conversations (Lu
et al., 2025; Lyu et al., 2026; Tang et al., 2026;
Yang et al., 2026c). Recent work extends proactive
assistance to everyday environments, using sen-
sory contexts from wearable devices to infer user
needs (Yang et al., 2025c, 2026b). However, these
studies address immediate needs that arise within
the current context, using history mainly to model
recurring user patterns that help infer such needs
and intervention timing. More recently, commer-
cial agents such as Meta’s Muse (Meta, 2026a) and
OpenAI’s Dots (OpenAI, 2026a) run continuously
in the background and follow up on users’ goals
over time, but largely rely on users to state these
goals explicitly. In contrast, long-horizon proactive
assistance over sensory contexts, where needs are
inferred from earlier context and addressed when
an opportunity arises later, remains underexplored.
Long-Term Memory for LLM Agents.Long-
term memory enables LLM agents to retain and
retrieve information across extended interaction his-
tories. Existing approaches span lexical and dense
retrieval (Robertson and Zaragoza, 2009; Reimers
and Gurevych, 2019), structured and graph-based

representations (Gutiérrez et al., 2025; Yue et al.,
2026; Rasmussen et al., 2025), agentic systems
that dynamically construct and update memo-
ries (Chhikara et al., 2025; Xu et al., 2025; Zhong
et al., 2024), and system-level architectures that
manage hierarchical memory stores (Packer et al.,
2023; Kang et al., 2025; Li et al., 2025). Recent
work further evaluates retrieval beyond surface-
level semantic similarity. LoCoMo-Plus (Li et al.,
2026) evaluates memory under cue-trigger seman-
tic disconnect, and T-Mem (Guo et al., 2026) intro-
duces a multi-level architecture for both descriptive
and associative recall. However, these approaches
remain centered on query-driven recall, leaving
open how to trigger relevant memories when the
current context is the only cue.
Prospective Memory in LLM Agents.Prospec-
tive memory, the human ability to retain a delayed
intention and act on it when an appropriate condi-
tion arises (McDaniel and Einstein, 2000; Einstein
and McDaniel, 2005), has recently also been stud-
ied in LLMs. One study (Mittal, 2026) examines
failures to follow explicit formatting instructions
under cognitive load. For delayed-intention trigger-
ing, PM-Bench (Liu and Gabriel, 2026) considers
explicitly specified intentions in a text-based sim-
ulated week, while TriggerBench (Zhang et al.,
2026) studies implicit prospective constraints intro-
duced earlier in dialogue. However, existing stud-
ies primarily evaluate delayed intentions that are
explicitly specified or conveyed through dialogue,
leaving prospective memory over rich wearable
sensory context underexplored.
3 Long-Horizon Proactive Assistance
3.1 Task Definition
Unlike existing proactive agents, which infer imme-
diate needs from the current context, we formalize
long-horizon proactive assistance over sensory con-
texts, where needs arise from prior context and
become actionable only at a later opportunity. At
time t, an agent A receives multimodal sensory
perceptions St, personal context P, and a history
Ht = (e1, . . . , et−1) of past events, each capturing
the sensory perceptions of an earlier moment. St
comprises egocentric video, audio, and mobile noti-
fications from wearable and mobile devices, while
P captures relatively stable user information such
as habits, preferences, and personal background.
The agent then decides whether any implicit de-
layed intention should be acted on at the current
moment: (T,ˆy,R) =A(S t,P,H t). Here, T is
the reasoning trace andˆyis the proactive decision.
The agent generates a proactive response R when
it decides to act and remains silent otherwise.
3.2 Task Construction
To evaluate this task, we introduce CPMBench, the
first benchmark for long-horizon proactive assis-
tance over sensory contexts. It consists of daily-life
timelines in which implicit delayed intentions are
first formed and only later become actionable.
Dataset Design.Each instance in CPMBench con-
sists of personal context P and a timeline
(e1, . . . , eN ) of daily-life events, where each event
ei = (ti,C ti) pairs a timestamp with sensory con-
text, textual descriptions of the sensory perceptions
Sti covering egocentric vision, speech, and mobile
notifications. An implicit delayed intention I is an-
chored by aformation moment ef , where it arises
from cues in the sensory context, and a laterdeci-
sion moment ed, where the agent decides whether
proactive assistance is needed. The two moments
are separated by many intervening daily activities.
Ascenariospecifies P and one or more intentions
formed at different moments, all sharing the final
event eN as their decision moment. Proactive assis-
tance is needed only if I has been formed, remains
unresolved, and can be acted on at ed. Each sce-
nario therefore yields four controlled variants, one
instance each, as follows:
•Positivesatisfies all three conditions.
•Negativeoffers no opportunity to act ate d.
•State Change includes an eventesc that resolves
Ibeforee d, so no assistance is needed.
•No Formation replaces ef with an ordinary
event so no intention arises, but keepse d.
In multi-intention scenarios, variants apply to all
intentions jointly. Together, they test whether an
agent can connect the current context to relevant
history and determine whether a delayed intention
exists, remains unresolved, and is actionable.
Data Construction.We construct our dataset in
three stages. First, human annotators write 100
seed scenarios drawn from everyday experiences,
each cross-reviewed by another annotator. We then
use LLMs to generate a larger and more diverse
set of candidate scenarios, followed by human ver-
ification for plausibility and consistency. Finally,
for each scenario, we build the four variant time-
lines by inserting intention-independent daily-life
events before ef and between ef and ed. These
events serve as distractors and are shared across the

0 50 100 150 200
# Instances
Work
Leisure
Social
Health
Food
Shopping
Transit
Daily life
CPMBench
0 40 80 120
# Instances
CPMBench-Omni
Figure 2: Distribution of timeline instances.
variants, enabling a controlled comparison of the
variant-specific events. This process yields CPM-
Bench, comprising 1,000 instances.
Sensor Data Pairing.We further pair a subset of
CPMBench with sensor data to form CPMBench-
Omni. For each event, we retrieve a matching clip
from S-EMBER (Wang et al., 2026), a large-scale
egocentric video dataset, using its visual descrip-
tion, and synthesize audio from its speech text.
When no clip reliably matches or recorded audio
is required, we record egocentric video and audio
ourselves. All videos are captured with Meta smart
glasses (Meta, 2026b), and the resulting instances
are human-verified. Details on benchmark con-
struction and data pairing are in Appendix A.2.
Dataset Statistics.CPMBench comprises 1,000
instances derived from 250 scenarios, of which 200
are single-intention and 50 are multi-intention. As
shown in Fig. 2, the instances involve delayed in-
tentions across eight everyday categories. Each
instance contains N= 200 events, with an average
of 114.5 events between the formation and deci-
sion moments. CPMBench-Omni comprises 500
instances with paired sensor data in total.
4 ProMemAgent Framework
This section presents ProMemAgent, a framework
incorporating context-aware prospective memory
for long-horizon proactive assistance over sensory
contexts. Fig. 3 shows the overview of ProMemA-
gent. It first extracts sensory contexts from multi-
modal sensory perceptions and then organizes them
into context-aware memory for future retrieval.
During inference, it retrieves relevant past events
using the current context and performs memory-
augmented proactive reasoning to decide whether
proactive assistance is needed.
4.1 Context-Aware Memory
4.1.1 Sensory Context Extraction
At each moment t, ProMemAgent converts the
multimodal sensory perceptions St into the sen-
sory context Ct, which together with its timestamp
forms an event et = (t,C t). A vision-language
model (VLM) generates a visual description of
the egocentric video, speech is transcribed with
speaker attribution to distinguish the user from oth-
ers, and mobile notifications are formatted as text.
Each moment thus has a unified representation et
that serves both as the retrieval cue at the current
moment and as the entry organized into memory in
subsequent moments.
4.1.2 Memory Construction and Retrieval
Given each event et, ProMemAgent employs a
memory-construction LLM to organize it into mem-
ory for future retrieval. Without explicit user
queries, long-horizon proactive assistance relies
on the current sensory context as the only cue for
recalling past events. In daily life, however, the cur-
rent context and the relevant past event are often se-
mantically disconnected, making similarity-based
retrieval insufficient. Moreover, delayed intentions
are usually implicit in sensory contexts and rarely
stated explicitly (e.g., “remind me to buy milk”).
As a result, it is often unclear when an event is
observed whether it will later call for assistance,
and subsequent events may also change the an-
swer. Inspired by prospective memory, in which a
delayed intention is retrieved when its associated
cue occurs (McDaniel and Einstein, 2000; Einstein
and McDaniel, 2005), ProMemAgent therefore as-
sociates events with prospective cues describing
when they may become relevant, links them to
their subsequent developments, and retrieves them
once the current context triggers these cues. These
three steps are realized by prospective cue gen-
eration, cross-event linking, and cue-triggered re-
trieval, while the proactive assistance decision is
left to the reasoner during inference (§ 4.2).
Prospective Cue Generation.Motivated by the
two primary forms of prospective memory (Ein-
stein and McDaniel, 1990), ProMemAgent gener-
ates event-based and time-based prospective cues.
For each stored event ei, it summarizes the ob-
served situation as qi and extracts a set of factual
observations Fi from its sensory context. For each
fact f∈ Fi, it constructs a set of event-based cues
Kf , each describing a future situation in which the
fact may become useful, and a set of time-based
cues Wf , each specifying a future time point or
window. Observed situations and event-based cues
share a structured form covering the user’s activity,
location, surrounding context, and people involved,

Sensory Context
Extraction
Visual Description
Generation
Speech Transcription
Notification Formatting
Fact
Prospective Cue Generation
Cross-Event Linking
Context-Aware Memory Construction
Current
Context
Cue-Triggered Retrieval
Memory-Augmented Reasoning
Personal
Context
Historical
Context
Daily-Life
Memory
Situation
Time-based
Event-based
…
Similarity Forward Link
…
Content-
based Cue-based
Reasoning
Distillation
Proactive
Reasoner
 Long-Horizon Proactive
Assistance
You’re out of oat milk.
Want to grab some
at this store?
User ran out of the usual
bedtime oat milk on Tuesday.
The nearby grocery store
offers a chance to restock.
Stay Silent
Current context and retrieved
memory do not suggest a
potential need for assistance.
Figure 3: Overview of ProMemAgent. It extracts sensory contexts and constructs context-aware memory through
prospective cue generation and cross-event linking. During inference, it retrieves past events via cue-triggered
retrieval and performs memory-augmented reasoning to provide long-horizon proactive assistance when needed.
following cognitive models of event representa-
tion (Radvansky and Zacks, 2011). This shared
form allows a cue to be compared directly with
the situation of a later event. The cues are used
for memory retrieval, while the original event ei
remains the evidence for proactive reasoning.
Cross-Event Linking.In human prospective mem-
ory, a finished intention is deactivated and no
longer triggered by its cue (Scullin et al., 2009).
ProMemAgent thus tracks whether earlier observa-
tions have been resolved or changed, connecting
them with their subsequent developments as new
events arrive. For each new event ej, every fact f
extracted from a preceding event ei is scored by its
relevance to ej, taken as the highest of sim(Cj, f),
sim(Cj,C i), and maxκ∈Kf sim(qj, κ), where sim
denotes cosine similarity between text embeddings.
ProMemAgent takes the top-m facts as candidates
and uses the memory-construction LLM to deter-
mine whether ej updates each of them. A cross-
event link is created only when the relation is sup-
ported by evidence explicitly present in ej. Links
are directed forward in time and added incremen-
tally. The memory entry of each evente i is thus

ei, qi,{(f,K f ,W f ,L f )}f∈F i

,(1)
whereL f is the set of later events linked fromf.
Cue-Triggered Retrieval.In prospective mem-
ory, an intention is recalled when its cue is en-
countered, without an explicit request (McDaniel
and Einstein, 2000). During inference, ProMemA-
gent uses the current event et to retrieve k past
events through complementary content retrieval
and cue-triggered retrieval. Content retrieval di-
rectly compares sensory contexts and selects the
kC past events with the highest sim(Ct,C i), de-
noted MC. Cue-triggered retrieval instead reaches
past events through prospective cues. Event-based
cues act as contextual triggers, so each past eventei
is scored by maxf∈F i maxκ∈Kf sim(Ct, κ). Time-
based cues act as temporal triggers, and an event
is time-triggered if t satisfies any time-based cue
of its facts. Events with and without a time trigger
are ranked separately and interleaved into one can-
didate list Q to balance temporal and contextual
relevance. Each candidate is then expanded with
the latest event linked from its facts, when avail-
able. ProMemAgent keeps the top kCT events in
Q that content retrieval has not already selected,
denoted MCT . Together, the k=k C +k CT events
in MC and MCT are ordered chronologically to
formM r for proactive reasoning.
4.2 Memory-Augmented Proactive Reasoning
Existing proactive agents infer immediate needs
from the current context (Lu et al., 2025; Yang
et al., 2025c). Long-horizon assistance, however,
requires interpreting the current context together
with relevant past events. ProMemAgent thus aug-
ments proactive reasoning with retrieved memory.
Memory-Augmented Reasoner.Given the current
sensory context Ct, personal context P, and the re-
trieved events Mr as historical context, ProMemA-
gent develops a proactive reasoner AR that pro-
duces the reasoning trace, proactive decision, and
proactive response, (T,ˆy,R) =A R(Ct,P,M r).
The personal context P is taken from CPMBench,
while in practice it can be extracted from longitudi-
nal sensor streams over months (Yang et al., 2026a).
The reasoner decides whether proactive assistance
is needed by reasoning about whether an implicit
delayed intention has been formed, remains unre-
solved, and can be acted on at the current moment.
Reasoning Distillation.We construct each train-

ing context by combining key events with distractor
events, so that the reasoner learns to account for
historical context in its proactive reasoning. Specif-
ically, we consider three key-event configurations,
E ∈ {{ef },{e f , esc},∅} , representing cases with
formation evidence only, with formation followed
by a subsequent development, and without forma-
tion evidence. For each context size K, we con-
struct the historical context HK =E ∪ DK with
|HK|=K , where DK contains distractor events
randomly sampled from earlier in the timeline.
Varying E and K diversifies both the reasoning
conditions and the amount of historical context. To
obtain reasoning supervision, a frontier LLM takes
(Ct,P,H K) and generates an evidence-grounded
reasoning trace explaining how they support the tar-
get proactive decision and response. We fine-tune
AR with LoRA (Hu et al., 2022) to generate the
distilled trace followed by the proactive decision
and response. During inference, HK is replaced by
the retrieved events Mr, enabling the reasoner to
apply the learned reasoning to retrieved memory.
5 Experiments
5.1 Experimental Setup
Baselines.We compare ProMemAgent against
four families of baselines.Proactive Agents
include Proactive Agent (Lu et al., 2025) and
ContextAgent (Yang et al., 2025c), which in-
fer assistance needs without explicitly retriev-
ing relevant past events.Full-Contextbaselines
use open-source and proprietary LLMs (Yang
et al., 2025a,b; Meta AI, 2024; OpenAI, 2026b)
to reason directly over the full historical con-
text.RAG-Basedbaselines retrieve past events
using BM25 (Robertson and Zaragoza, 2009), all-
MiniLM-L6-v2 (Reimers and Gurevych, 2019), or
text-embedding-3-small (OpenAI, 2024).Memory
Systemsinclude Mem0 (Chhikara et al., 2025), A-
Mem (Xu et al., 2025), MemOS (Li et al., 2025),
and T-Mem (Guo et al., 2026), which construct and
retrieve long-term memories before reasoning.
Metrics.We evaluate long-horizon proactive assis-
tance along three dimensions.Memory Retrieval.
Delayed intention recall(DIR)is the fraction of
delayed intentions in Positive instances whose
formation moment ef is retrieved, and state change
recall(SCR)is the fraction of State Change in-
stances in which both ef and the state-change event
esc are retrieved.Proactive Decision.Following
prior work (Yang et al., 2025c; Lu et al., 2025),
we use false detection rate(FD)and proactive pre-
diction accuracy(Acc-P)to evaluate whether the
agent correctly decides to assist or remain silent.
End-to-End Assistance.We further evaluate re-
sponse content using an LLM judge (Zheng et al.,
2023; Li et al., 2024). Since an instance may con-
tain multiple delayed intentions, we use set-level
precision(Set-P), recall(Set-R), and F1(Set-F1).
Proactive assistance accuracy(Acc-PA)extends
Acc-P by also requiring the assistance to be correct.
Metric details are in Appendix D.
Implementation Details.We split CPMBench by
scenario into 60% training and 40% testing, so all
variants of a scenario share a split. For sensory con-
text extraction, ProMemAgent uses Qwen3-VL-
32B and WhisperX (Bain et al., 2023). Unless
otherwise specified, ProMemAgent and proactive-
agent baselines use Qwen3-8B, fine-tuned with
LoRA under the same training settings. Reason-
ing traces for distillation are generated by Claude-
Opus-4.6. By default, applicable methods use GPT-
4o-mini for LLM-based memory construction and
text-embedding-3-small for embeddings. We set
k= 10 for top-k retrieval methods except T-Mem,
for which we evaluate its default setting and a
variant that retrieves the top-10 scenes using only
horizon triggers. ProMemAgent uses m= 8 for
cross-event linking, kC = 2for content retrieval,
and kCT = 8 for cue-triggered retrieval. RAG-
based and memory-system baselines use GPT-5.4
for proactive reasoning. We use GPT-5-mini as
the LLM judge, which shows high agreement with
human annotators (Appendix E). Implementation
and prompt details are in Appendices B and C.
Overall performance on CPMBench.Table 1
shows that ProMemAgent, with an 8B reasoner,
achieves the best overall performance across mem-
ory retrieval, proactive decision making, and end-
to-end assistance. It improves Set-F1 by 9.7 points
over the strongest baseline, full-context GPT-5.4,
indicating its effectiveness for long-horizon proac-
tive assistance. Proactive agents designed for im-
mediate needs miss most delayed intentions. Ac-
cess to the full history is not sufficient either. With
relevant events buried among many unrelated ones,
full-context LLMs either overlook many intentions
or, like GPT-5.4, achieve higher Set-R at the cost of
a high false detection rate. Similarity-based RAG
methods and memory systems rarely reach relevant
past events, which are often semantically discon-
nected from the current context. Retrieving with
T-Mem’s horizon triggers alone improves DIR, in-

Method Memory Retrieval Proactive Decision End-to-End Assistance
DIR↑SCR↑FD↓Acc-P↑Acc-PA↑Set-P↑Set-R↑Set-F1↑
Proactive
Agents
Proactive Agent (8B) - - 7.0 77.8 74.7 63.8 30.1 40.9
ContextAgent (8B) - - 43.3 59.8 46.8 17.7 22.8 19.9
Full-Context
LLMs
(Open- and
Closed-Source)
Qwen2.5-32B - - 15.7 73.2 68.3 43.4 29.3 35.0
Qwen3-4B - - 19.0 69.8 63.8 32.1 22.0 26.1
Qwen3-8B - - 27.0 69.8 63.4 37.7 39.8 38.7
Qwen3-14B - - 16.0 74.8 70.2 48.4 36.6 41.7
Qwen3-32B - - 41.3 64.8 60.0 38.6 63.4 48.0
Llama-3.3-70B - - 16.3 72.8 68.6 44.3 31.7 37.0
GPT-4o - - 13.0 82.0 77.3 62.9 53.7 57.9
GPT-4.1 - - 5.3 86.0 81.3 78.9 48.8 60.3
GPT-5.4-mini - - 5.3 77.5 73.3 61.9 21.1 31.5
GPT-5.4 - - 24.0 79.8 76.4 56.977.265.5
RAG-based
Methods
(GPT-5.4)
all-MiniLM-L6-v2 14.6 10.03.077.2 73.0 66.7 14.6 24.0
BM25 19.5 13.0 5.0 77.0 72.8 60.5 18.7 28.6
text-embedding-3-small 21.1 13.0 6.3 76.8 72.1 55.8 19.5 28.9
Memory
Systems
(GPT-5.4)
Mem0 - - 6.3 74.5 70.2 45.7 13.0 20.3
A-Mem 32.5 25.0 7.3 79.5 74.9 63.9 31.7 42.4
MemOS 30.9 6.0 12.0 74.8 70.2 47.8 26.8 34.4
T-Mem 28.5 19.0 9.0 74.5 70.2 47.1 19.5 27.6
T-Mem (Horizon-based) 49.6 25.0 15.0 75.0 70.9 50.0 36.6 42.3
Ours ProMemAgent (8B)81.3 72.04.3 90.0 87.2 86.366.7 75.2
Table 1: Main results on CPMBench. All metrics are in percentages (%). The best and second-best results are in
boldand underlined , respectively. “-” denotes inapplicable retrieval metrics.
MethodDIR↑SCR↑Set-P↑Set-R↑Set-F1↑
Proactive Agent (8B) - - 63.6 21.5 32.2
ContextAgent (8B) - - 11.0 12.3 11.6
Qwen3-32B - - 35.2 49.2 41.0
GPT-5.4 - - 50.0 61.5 55.2
text-embedding-3-small 20.0 10.7 55.6 15.4 24.1
T-Mem (Horizon-based) 26.2 14.3 44.8 20.0 27.7
ProMemAgent (8B)83.1 66.1 74.5 58.5 65.5
Table 2: Main results on CPMBench-Omni.
dicating the value of anticipating future use during
memory construction. ProMemAgent achieves the
highest DIR and SCR, highlighting the benefit of
prospective cues and cross-event links for retriev-
ing relevant past events from sensory contexts.
Overall performance on CPMBench-Omni.As
shown in Tab. 2 (complete results in Appendix F),
all methods show lower end-to-end performance on
CPMBench-Omni than on CPMBench, reflecting
the additional challenge of imperfect sensory con-
text extraction. ProMemAgent still maintains its
advantage over all baselines and outperforms full-
context GPT-5.4 by 10.3 points in Set-F1. Its high
DIR and SCR show that it effectively retrieves both
intention-formation events and their subsequent de-
velopments from noisy sensory contexts. Fig. 4
illustrates two cases in which ProMemAgent as-
sists when a delayed intention becomes actionable
06-08 19:20
User walks on a wet pavement…
enter through the revolving door into
a bright lobbywith yellow reception…
Lives in an apartment with a staffed lobby.
Right now user is standing in the lobby
… appear to call home, so they are at the
exact location where they could collect
the package… I should speak now.
Welcomeback.
Welcome back! By the way, you might
want to grab yourdelivery while you're here.
10-22 09:10 User moves
approaching the desk. They sit and
interact with the keyboard, turning
on the left monitor which displays…
Lives with partner. Plans family trips…
…
User sits facing a …
User sits at a desk…
…
…
…
User sits at a desk, holds
asmartphone, showing an email …
Email: Your order has been delivered…
…
User is in their living space…appear to
be starting work…On Wed at 20:40, user
discussed…set up an open task. However,
the moment on Thu at 08:20 shows this was
already resolved…Since the only relevant
open item was already handled, there is
nothing needing action, so I stay silent.
10-21 20:40
10-22 08:20
06-08 12:20
Figure 4: Qualitative results of ProMemAgent in proac-
tive and non-proactive cases.
and remains silent when it has been resolved.
5.2 Ablation Study and Discussion
Memory Components.Tab. 3 shows that all
memory components contribute to ProMemAgent’s
performance. Removing cue-triggered retrieval
(MCT ) degrades both retrieval and assistance per-
formance, indicating that relevant past events are of-
ten semantically disconnected from current context.
Event-based (Kf ) and time-based (Wf ) cues pro-
vide complementary contextual and temporal trig-
gers. Cross-event linking (Lf ) helps retrieve subse-
quent developments and avoid acting on resolved
intentions. Content retrieval (MC) complements
cue-triggered retrieval by preserving similarity-

Method CPMBench Direct QA
DIR↑SCR↑FD↓Set-R↑Set-F1↑Recall@10↑
ProMemAgent 81.3 72.0 4.3 66.7 75.2 98.1
w/oL f 81.3 38.0 14.7 66.7 65.9 98.1
w/oK f 47.2 42.0 2.7 32.5 46.8 99.5
w/oW f 66.7 61.0 3.0 54.5 67.3 98.1
w/oM CT 26.0 15.0 4.0 21.1 32.3 99.5
w/oM C 80.5 72.0 4.3 65.0 74.1 70.0
Table 3: Memory components ablation on CPMBench.
0
20
40
60
80
100Set-F1 (%)
ProMemAgent (8B): 75.2
46.6
57.0 62.6
38.3
w/o SFT
ICL-CoT
Vanilla ICL
SFT w/o History
(a) Reasoning components.
0
20
40
60
80
100Set-F1 (%)
75.2 69.8 76.4 77.1 79.6
ProMemAgent (8B) K={8,10,12}
K={10}
Qw3-14B
K={6,8,10,12,14}
Qw3-32B (b) Backbone andK.
Figure 5: Impact of reasoner variants on CPMBench. K
denotes training context sizes and “Qw” denotes Qwen.
based access to memory. On a direct QA set built
from CPMBench, where queries ask about informa-
tion explicitly observed in past events, removing it
reduces Recall@10 from 98.1 to 70.0.
Reasoning Components.Fig. 5a compares rea-
soner variants given the same retrieved memory.
Even with relevant past events, the base Qwen3-8B
reasoner (w/o SFT) struggles with implicit delayed
intentions. In-context learning with 10 demonstra-
tions (Vanilla ICL) improves it, and adding the
reasoning traces used for distillation (ICL-CoT)
improves it further, showing the value of explicit
reasoning. Fine-tuning on the current context alone
(SFT w/o History), as in ContextAgent, performs
poorly, indicating the need to train the reasoner
with historical context. On three randomly selected
categories excluded from fine-tuning, ProMemA-
gent still achieves 74.0 Set-F1 and outperforms all
baselines (detailed results in Appendix F), showing
the generalizability of its proactive reasoning.
Sensory and Personal Context.On CPMBench-
Omni, removing vision or audio at inference lowers
Set-F1 by 20.0 and 4.9 points, respectively, show-
ing that both modalities are important. Without per-
sonal context, Set-F1 drops by 5.1 points, mainly in
recall, suggesting that personal context helps recog-
nize delayed intentions tied to the user’s habits and
background. Replacing the 32B VLM with Qwen3-
VL-8B lowers Set-F1 by 6.2 points, suggesting
that a stronger VLM for sensory context extraction
benefits long-horizon proactive assistance.
40
60
80Retrieval (%)
(a) add kCT (kC = 2)
40
60
80
(b) split k = 10 (kC = 10−kCT)
4 6 8 10 12
cue-triggered budget kCT
60
70
80Set-F1 (%)
65.7 69.4
75.2
69.5 69.4
2 4 6 8 10
cue-triggered budget kCT
60
70
80
65.4 67.6 70.4
75.2 74.1
DIR SCR Set-F1 Default
Figure 6: Sensitivity to the content and cue-triggered
retrieval budgets (kC,k CT ) on CPMBench.
5.3 Sensitivity Analysis
Memory Construction.Memory construction is
robust to both the construction LLM and the num-
ber of candidate facts m for cross-event linking
(Tab. 7 in Appendix F). Replacing GPT-4o-mini
with GPT-4.1-mini or varying m between 4 and 16
changes Set-F1 by less than 3 points.
Retrieval Configuration.Fig. 6 varies the cue-
triggered budget kCT , either with the content bud-
get fixed at kC = 2or with the total budget fixed
at k= 10 . In both settings, increasing kCT first
improves both retrieval and Set-F1, indicating the
need for sufficient cue-triggered retrieval. Further
increasing kCT provides little additional retrieval
benefit and can reduce Set-F1, suggesting that extra
retrieved events may distract the reasoner.
Reasoner Configuration.Fig. 5b varies the
reasoner backbone and training context sizes K.
Scaling the backbone from Qwen3-8B to Qwen3-
32B consistently improves Set-F1, suggesting that
stronger reasoners better exploit the same retrieved
memory. Training with a single context size under-
performs training with multiple sizes, even when it
matches the inference budget k, showing the bene-
fit of varying the amount of historical context.
6 Conclusion
This paper introduces ProMemAgent, the first
proactive LLM agent to incorporate context-aware
prospective memory for long-horizon proactive as-
sistance. ProMemAgent leverages sensory contexts
for effective memory construction and performs
memory-augmented proactive reasoning for im-
plicit delayed intentions. We also introduce CPM-
Bench, the first benchmark for this task. Our work
extends proactive assistance from immediate needs
to delayed intentions, helping users act on them
when the opportunity arises in everyday life.

Limitations
This work evaluates long-horizon proactive assis-
tance over sequences of discrete sensory contexts.
While CPMBench-Omni pairs events with real ego-
centric video and audio, these clips are collected
per event, and our work does not model the full
pipeline from continuous wearable sensing, such as
segmenting continuous streams into events. Evalua-
tion on continuous in-the-wild wearable streams is
left to future work. Although CPMBench includes
eight everyday categories in English, it can be di-
versified across categories and languages to further
test the generality of long-horizon proactive assis-
tance. ProMemAgent converts raw video and audio
into textual sensory contexts before memory con-
struction and reasoning, which may lose some fine-
grained multimodal information. Preserving and
directly reasoning over multimodal representations
throughout the memory and reasoning pipeline re-
mains future work. Memory construction and rea-
soning distillation further rely on LLMs that can
reliably follow instructions, and weaker LLMs may
affect the quality of intermediate representations.
Ethical Considerations
All instances in CPMBench, whether derived from
human-written seeds or LLM-generated scenarios,
contain no identifiable information about real in-
dividuals and include only synthetic personas and
names. The sensory data in CPMBench-Omni are
drawn partly from S-EMBER (Wang et al., 2026),
a publicly released dataset, and partly from our
own data collection. The S-EMBER videos we use
have faces blurred and audio removed, and we use
them in accordance with the dataset’s license for
non-commercial research. Our data collection was
approved by the Institutional Review Board (IRB)
of our institution, with informed consent obtained
from all participants. Faces and other sensitive re-
gions are blurred to protect privacy, and speech
in the recordings followed scripted scenarios with
synthetic names and contains no personal informa-
tion about participants. While ProMemAgent is
evaluated in a controlled setting, a real-world de-
ployment would store long-term sensory contexts
from wearable and mobile devices and personal
information about the user, potentially including
information about bystanders. Such deployment
would require appropriate privacy safeguards, but
questions regarding how such memories should be
stored, retained, or governed in deployed systems
are beyond the scope of this work.
Acknowledgments
This research was partially supported by the Na-
tional Science Foundation under Grant Number
CNS-1943396. The views and conclusions con-
tained here are those of the authors and should not
be interpreted as necessarily representing the offi-
cial policies or endorsements, either expressed or
implied, of Columbia University, NSF, or the U.S.
Government or any of its agencies.
References
Anthropic. 2026a. Claude Opus 4.6 System Card. Tech-
nical report, Anthropic.
Anthropic. 2026b. System card: Claude
Sonnet 4.6. https://www.anthropic.com/
claude-sonnet-4-6-system-card.
Shuai Bai, Yuxuan Cai, Ruizhe Chen, Keqin Chen,
Xionghui Chen, Zesen Cheng, Lianghao Deng, Wei
Ding, Chang Gao, Chunjiang Ge, Wenbin Ge, Zhi-
fang Guo, Qidong Huang, Jie Huang, Fei Huang,
Binyuan Hui, Shutong Jiang, Zhaohai Li, Mingsheng
Li, and 45 others. 2025. Qwen3-vl technical report.
Preprint, arXiv:2511.21631.
Max Bain, Jaesung Huh, Tengda Han, and Andrew Zis-
serman. 2023. Whisperx: Time-accurate speech tran-
scription of long-form audio.INTERSPEECH 2023.
Prateek Chhikara, Dev Khant, Saket Aryan, Taranjeet
Singh, and Deshraj Yadav. 2025. Mem0: Building
production-ready ai agents with scalable long-term
memory.Preprint, arXiv:2504.19413.
Gheorghe Comanici, Eric Bieber, Mike Schaekermann,
Ice Pasupat, Noveen Sachdeva, Inderjit Dhillon, Mar-
cel Blistein, Ori Ram, Dan Zhang, Evan Rosen,
et al. 2025. Gemini 2.5: Pushing the frontier with
advanced reasoning, multimodality, long context,
and next generation agentic capabilities.Preprint,
arXiv:2507.06261.
Gilles O. Einstein and Mark A. McDaniel. 1990. Nor-
mal aging and prospective memory.Journal of Ex-
perimental Psychology: Learning, Memory, and Cog-
nition, 16(4):717–726.
Gilles O. Einstein and Mark A. McDaniel. 2005.
Prospective memory: Multiple retrieval pro-
cesses.Current Directions in Psychological Science,
14(6):286–290.
Weidong Guo, Dakai Wang, Zixuan Wang, Hui Liu, and
Yu Xu. 2026. T-mem: Memory that anticipates, not
archives.Preprint, arXiv:2606.15405. Accepted to
EMNLP 2026 Main Conference.

Bernal Jiménez Gutiérrez, Yiheng Shu, Weijian Qi,
Sizhe Zhou, and Yu Su. 2025. From RAG to memory:
Non-parametric continual learning for large language
models. InForty-second International Conference
on Machine Learning.
Edward J Hu, Yelong Shen, Phillip Wallis, Zeyuan
Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, and
Weizhu Chen. 2022. LoRA: Low-rank adaptation of
large language models. InInternational Conference
on Learning Representations.
Aaron Hurst, Adam Lerer, Adam P. Goucher, Adam
Perelman, Aditya Ramesh, Aidan Clark, AJ Os-
trow, Akila Welihinda, Alan Hayes, Alec Radford,
et al. 2024. Gpt-4o system card.arXiv preprint
arXiv:2410.21276.
Jiazheng Kang, Mingming Ji, Zhe Zhao, and Ting Bai.
2025. Memory OS of AI agent. InProceedings of the
2025 Conference on Empirical Methods in Natural
Language Processing, pages 25961–25970, Suzhou,
China. Association for Computational Linguistics.
Haitao Li, Qian Dong, Junjie Chen, Huixue Su, Yu-
jia Zhou, Qingyao Ai, Ziyi Ye, and Yiqun Liu.
2024. Llms-as-judges: A comprehensive sur-
vey on llm-based evaluation methods.Preprint,
arXiv:2412.05579.
Yifei Li, Weidong Guo, Lingling Zhang, Rongman Xu,
Muye Huang, Hui Liu, Lijiao Xu, Yu Xu, and Jun
Liu. 2026. Locomo-plus: Beyond-factual cognitive
memory evaluation framework for LLM agents. In
Proceedings of the 64th Annual Meeting of the As-
sociation for Computational Linguistics (Volume 1:
Long Papers), pages 25085–25100, San Diego, Cali-
fornia, United States. Association for Computational
Linguistics.
Zhiyu Li, Chenyang Xi, Chunyu Li, Ding Chen, Boyu
Chen, Shichao Song, Simin Niu, Hanyu Wang, Ji-
awei Yang, Chen Tang, Qingchen Yu, Jihao Zhao,
Yezhaohui Wang, Peng Liu, Zehao Lin, Pengyuan
Wang, Jiahao Huo, Tianyi Chen, Kai Chen, and 20
others. 2025. Memos: A memory os for ai system.
Preprint, arXiv:2507.03724.
Genglin Liu and Saadia Gabriel. 2026. Pm-bench: Eval-
uating prospective memory of llm agents. InThird
Conference on Language Modeling.
Yaxi Lu, Shenzhi Yang, Cheng Qian, Guirong Chen,
Qinyu Luo, Yesai Wu, Huadong Wang, Xin Cong,
Zhong Zhang, Yankai Lin, Weiwen Liu, Yasheng
Wang, Zhiyuan Liu, Fangming Liu, and Maosong
Sun. 2025. Proactive agent: Shifting llm agents from
reactive responses to active assistance. InInterna-
tional Conference on Learning Representations, vol-
ume 2025, pages 47431–47457.
Yibo Lyu, Gongwei Chen, Rui Shao, Weili Guan, and
Liqiang Nie. 2026. PersonalAlign: Hierarchical im-
plicit intent alignment for personalized GUI agent
with long-term user-centric records. InProceedings
of the 64th Annual Meeting of the Association for
Computational Linguistics (Volume 1: Long Papers),
pages 36074–36089, San Diego, California, United
States. Association for Computational Linguistics.
Mark A McDaniel and Gilles O Einstein. 2000. Strate-
gic and automatic processes in prospective memory
retrieval: A multiprocess framework.Applied Cog-
nitive Psychology: The Official Journal of the Soci-
ety for Applied Research in Memory and Cognition,
14(7):S127–S144.
Meta. 2026a. Introducing Muse: The world’s
first personal AI agent built for every-
one. https://about.fb.com/news/2026/09/
introducing-muse-personal-ai-agent/. Accessed:
2026-10-12.
Meta. 2026b. Ray-Ban Meta AI glasses. https:
//www.meta.com/ai-glasses/ray-ban-meta/. Ac-
cessed: 2026-10-10.
Meta AI. 2024. Llama 3.3 70B Instruct.
https://huggingface.co/meta-llama/Llama-3.
3-70B-Instruct. Hugging Face model card.
Microsoft Azure. 2026. Text to speech overview, azure
speech service. https://learn.microsoft.com/en-us/
azure/ai-services/speech-service/text-to-speech.
Accessed: 2026-10-02.
Avni Mittal. 2026. Did you forget what I asked?
prospective memory failures in large language mod-
els. InProceedings of the 6th Workshop on Trust-
worthy NLP (TrustNLP 2026), pages 471–488, San
Diego, California. Association for Computational
Linguistics.
OpenAI. 2024. New embedding models
and api updates. https://openai.com/index/
new-embedding-models-and-api-updates/.
OpenAI. 2026a. Introducing dots. https://openai.com/
index/introducing-dots/. Accessed: 2026-10-12.
OpenAI. 2026b. Openai api models. https://developers.
openai.com/api/docs/models. Accessed 2026.
Charles Packer, Sarah Wooders, Kevin Lin, Vivian Fang,
Shishir G Patil, Ion Stoica, and Joseph E Gonzalez.
2023. Memgpt: Towards llms as operating systems.
arXiv preprint arXiv:2310.08560.
Gabriel A Radvansky and Jeffrey M Zacks. 2011. Event
perception.Wiley Interdisciplinary Reviews: Cogni-
tive Science, 2(6):608–620.
Preston Rasmussen, Pavlo Paliychuk, Travis Beauvais,
Jack Ryan, and Daniel Chalef. 2025. Zep: a tempo-
ral knowledge graph architecture for agent memory.
arXiv preprint arXiv:2501.13956.
Nils Reimers and Iryna Gurevych. 2019. Sentence-
BERT: Sentence embeddings using Siamese BERT-
networks. InProceedings of the 2019 Conference on
Empirical Methods in Natural Language Processing
and the 9th International Joint Conference on Natu-
ral Language Processing (EMNLP-IJCNLP), pages

3982–3992, Hong Kong, China. Association for Com-
putational Linguistics.
Stephen Robertson and Hugo Zaragoza. 2009. The
probabilistic relevance framework: Bm25 and be-
yond.Found. Trends Inf. Retr., 3(4):333–389.
Michael K. Scullin, Gilles O. Einstein, and Mark A.
McDaniel. 2009. Evidence for spontaneous retrieval
of suspended but not finished prospective memories.
Memory & Cognition, 37(4):425–433.
Yuanbo Tang, Huaze Tang, Tingyu Cao, Lam Nguyen,
Anping Zhang, Xinwen Cao, Chunkang Liu, Wenbo
Ding, and Yang Li. 2026. Proagentbench: Evaluating
llm agents for proactive assistance with real-world
data.arXiv preprint arXiv:2602.04482.
Xiaodong Wang, Xuanyi Zhao, Pedro Rodriguez, De-
vendra Singh Sachan, Barlas Oguz, Seungwhan
Moon, Shang-Wen Li, Gargi Ghosh, Xin Dong, and
Wen-Tau Yih. 2026. S-ember: A large-scale bench-
mark for streaming egocentric memory retrieval.
arXiv preprint arXiv:2607.02689.
Wujiang Xu, Zujie Liang, Kai Mei, Hang Gao, Juntao
Tan, and Yongfeng Zhang. 2025. A-mem: Agen-
tic memory for llm agents. InAdvances in Neural
Information Processing Systems, volume 38, pages
17577–17604. Curran Associates, Inc.
An Yang, Anfeng Li, Baosong Yang, Beichen Zhang,
Binyuan Hui, Bo Zheng, Bowen Yu, Chang Gao,
Chengen Huang, Chenxu Lv, Chujie Zheng, Day-
iheng Liu, Fan Zhou, Fei Huang, Feng Hu, Hao
Ge, Haoran Wei, Huan Lin, Jialong Tang, and 41
others. 2025a. Qwen3 technical report.Preprint,
arXiv:2505.09388.
An Yang, Baosong Yang, Beichen Zhang, Binyuan Hui,
Bo Zheng, Bowen Yu, Chengyuan Li, Dayiheng Liu,
Fei Huang, Haoran Wei, Huan Lin, Jian Yang, Jian-
hong Tu, Jianwei Zhang, Jianxin Yang, Jiaxi Yang,
Jingren Zhou, Junyang Lin, Kai Dang, and 23 oth-
ers. 2025b. Qwen2.5 technical report.Preprint,
arXiv:2412.15115.
Bufang Yang, Lilin Xu, Yixuan Li, Kaiwei Liu, Xiao-
fan Jiang, and Zhenyu Yan. 2026a. Sensorpersona:
An llm-empowered system for continual persona ex-
traction from longitudinal mobile sensor streams.
Preprint, arXiv:2604.06204.
Bufang Yang, Lilin Xu, Liekang Zeng, Yunqi Guo,
Siyang Jiang, Wenrui Lu, Kaiwei Liu, Yixuan Li, Xi-
aofan Jiang, Guoliang Xing, and Zhenyu Yan. 2026b.
Proagent: Harnessing on-demand sensory contexts
for proactive llm agent systems in the wild.Preprint,
arXiv:2512.06721.
Bufang Yang, Lilin Xu, Liekang Zeng, Kaiwei Liu,
Siyang Jiang, Wenrui Lu, Hongkai Chen, Xiaofan
Jiang, Guoliang Xing, and Zhenyu Yan. 2025c. Con-
textagent: Context-aware proactive llm agents with
open-world sensory perceptions. InAdvances in
Neural Information Processing Systems, volume 38,
pages 167509–167543.
Qinglong Yang, Haoming Li, Haotian Zhao, Xiaokai
Yan, Jingtao Ding, Fengli Xu, and Yong Li. 2026c.
Fingertip 20k: A benchmark for proactive and per-
sonalized mobile LLM agents. InThe Fourteenth
International Conference on Learning Representa-
tions.
Juwei Yue, Chuanrui Hu, Jiawei Sheng, Zuyi Zhou,
Wenyuan Zhang, Tingwen Liu, Li Guo, and Yafeng
Deng. 2026. HyperMem: Hypergraph memory for
long-term conversations. InProceedings of the 64th
Annual Meeting of the Association for Computational
Linguistics (Volume 1: Long Papers), pages 35237–
35254, San Diego, California, United States. Associ-
ation for Computational Linguistics.
Tianhua Zhang, Xinjiang Wang, Qianxi Zhang, Qi Chen,
Kun Li, Yaoqi Chen, Dingdong Wang, Helen Meng,
and Yan Lu. 2026. Triggerbench: Investigating
prospective memory for large language models.
arXiv preprint arXiv:2606.23459.
Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan
Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin,
Zhuohan Li, Dacheng Li, Eric Xing, Hao Zhang,
Joseph Gonzalez, and Ion Stoica. 2023. Judging
llm-as-a-judge with mt-bench and chatbot arena. In
Advances in Neural Information Processing Systems,
volume 36, pages 46595–46623. Curran Associates,
Inc.
Wanjun Zhong, Lianghong Guo, Qiqi Gao, He Ye, and
Yanlin Wang. 2024. MemoryBank: Enhancing large
language models with long-term memory. InPro-
ceedings of the AAAI Conference on Artificial Intelli-
gence, volume 38, pages 19724–19731.
A Dataset Details
A.1 Instance Examples
Fig. 7 presents an example scenario and its four
variants, including Positive, Negative, State
Change and No Formation . Each instance in-
cludes personal context and a timeline of N= 200
timestamped events, each containing sensory con-
text. The hidden gold annotation specifies the
delayed intention and the expected proactive be-
havior. The Negative, State Change , and No
Formation variants are then shown through their
variant-specific event, while all remaining events
are shared with thePositivetimeline.
A.2 Benchmark Construction
Seed Scenario Construction.Three annotators
first create seed scenarios drawn from diverse ev-
eryday experiences. Each scenario contains one
or more implicit delayed intentions, together with
their formation and decision moments, relevant per-
sonal context, and textual descriptions of the visual,

Instance Example: One Scenario and Its Four Variants
Personal ContextLives alone in a small apartment. Works at a downtown office.
TimelineFri 2026-07-03 07:33| vision: The user taps the tablet screen propped against a salt shaker, scrolling a page of densely spaced
text with a narrow sidebar of grey icons. A half-eaten piece of toast rests on a yellow plate to the left.
[ 53 daily-life events, e.g., office work, commuting, reading at home ]
Mon 2026-07-06 07:50| vision: The user stands at the bathroom sink and squeezes a flattened toothpaste tube over the toothbrush, rolling it
tightly from the bottom. Only a tiny smear reaches the bristles. After squeezing it once more with no visible result, the user drops the tube into
the trash bin beside the sink. ←e f
[ 143 daily-life events ]
Tue 2026-07-07 18:05 | vision: The user stands in a crowded subway car gripping a metal pole, a folded newspaper under one arm, as station
lights and tiled walls streak past the dark window. | audio: Next stop, Central Station. Doors will open on the left.
Tue 2026-07-07 18:35 | vision: The user walks into a supermarket through the automatic doors and picks up a shopping basket from the stack
by the entrance. Aisles of packaged food stretch ahead under bright ceiling lights.←e d (current moment)
AnnotationDelayed intention: Buy a new tube of toothpaste the next time the user is at a store that sells toiletries. Decision: assist.
Other VariantsEach variant changes one event of thePositivetimeline (key event); all other events are identical.
Variant Key event Decision ate d
Negative
ed Tue 2026-07-07 18:35 | vision: The user steps into a small perfume shop, where illuminated
shelves display glass fragrance bottles and boxed gift sets. A staff member rearranges sample
strips on a counter near the entrance.
Stay silent: a per-
fume shop does not sell
toothpaste.
State Change
esc Mon 2026-07-06 08:05 | vision: The user opens the cabinet under the sink, reaches inside, and
takes out an unopened tube of toothpaste. The user places it beside the toothbrush cup on the sink.
Stay silent: a new tube
is already at home.
No Formation
ef Mon 2026-07-06 07:50 | vision: The user crouches to lace brown leather shoes by the front door,
tugging each knot tight, then stands and slips a slim wallet and a ring of keys into a jacket pocket.
Stay silent: no intention
is formed.
Figure 7: An example scenario from CPMBench and its four variants, showing representative events from the
Positivetimeline and its annotation, followed by the variant-specific events of the other three variants.
speech, and notification context at each key mo-
ment. Annotators additionally specify the variant-
specific events required to construct the four con-
trolled variants and provide reasoning traces ex-
plaining whether proactive assistance should be
provided or withheld. All seed scenarios are cross-
reviewed by another annotator.
Scenario Diversification and Validation.Starting
from seed scenarios, we then use LLMs with the
prompts in Fig. 12 to generate a larger and more di-
verse set of candidate scenarios across everyday cat-
egories. The generated scenarios are subsequently
reviewed by human annotators to remove implausi-
ble or redundant cases and verify the consistency
of the annotated intentions and variants.
Timeline Construction.For each validated sce-
nario, we construct four timeline variants with a
shared temporal structure. We first build an ini-
tial timeline containing the variant-specific events
and additional scenario-specific daily-life events
generated consistently with the personal context.
These additional events are intention-independent
and serve as distractors between the key moments
of the scenario. The formation momentef is placed
earlier in the timeline, while the shared decision
moment ed is the final event. We further augment
each timeline with a pool of shared daily-life back-
ground events, inserted both before and between
the scenario-specific events. Unlike the scenario-
specific distractors, these background events are
reused across scenarios, with their timestamps ad-
justed to fit each timeline. Both types of distractor
events are designed to be independent of the target
intention and to neither reveal nor resolve it. Within
a scenario, all non-variant events are shared across
the four variants so that they differ only in their
controlled variant-specific events. Each resulting
timeline containsN= 200events.
Sensor Data Pairing.For CPMBench-Omni, we
pair events represented by textual descriptions with
egocentric video and audio. We first retrieve video
clips from S-EMBER (Wang et al., 2026) using the
visual descriptions in each event and synthesize the
corresponding audio from its textual speech con-
tent using text-to-speech (Microsoft Azure, 2026).
S-EMBER is released under the CC BY-NC 4.0
license, and our use of the dataset complies with
its terms. We record the original video identifier
and the start and end timestamps of each clip, so
that every clip can be traced back to its source in S-

EMBER. When retrieval cannot reliably match the
visual description or recorded audio is required, par-
ticularly for key formation and decision moments,
we self-record additional egocentric video and au-
dio. Both retrieved and self-recorded videos were
captured using Meta smart glasses (Meta, 2026b).
All paired video and audio are verified by human
annotators against the corresponding event descrip-
tions. Our self-recorded sensor collection was ap-
proved by the institutional IRB, and all participants
provided informed consent prior to data collection.
Faces and other visually identifying or sensitive
regions were blurred to protect participant privacy.
Speech in the recordings followed scripted scenar-
ios with synthetic names and contains no personal
information about participants.
B Implementation Details
Default Setup.We conduct all experiments on a
server with two NVIDIA RTX PRO 6000 GPUs.
We randomly split CPMBench into 60% training
and 40% testing, assigning all variants from the
same scenario to the same split. Unless otherwise
specified, ProMemAgent and fine-tuned proactive-
agent baselines use Qwen3-8B with LoRA of rank
8 and are trained for five epochs using AdamW
with a learning rate of 5×10 −4 and 10% warmup,
with a fixed random seed for all experiments for
fair comparison. Claude-Opus-4.6 (Anthropic,
2026a) is used to generate reasoning traces for dis-
tillation. For LLM-based memory construction,
we use GPT-4o-mini and text-embedding-3-small
for embedding-based similarity. RAG-based and
memory-system baselines use GPT-5.4 for proac-
tive reasoning. Unless otherwise specified, the
reasoner receives the personal context and current
event together with the historical context provided
by each method. For methods using top-k retrieval,
we setk= 10unless otherwise specified.
ProMemAgent.For context extraction, ProMemA-
gent employs Qwen3-VL-32B (Bai et al., 2025) to
caption each egocentric video clip using the prompt
in Fig. 8, and WhisperX (Bain et al., 2023) to tran-
scribe speech with speaker diarization. For cross-
event linking in memory construction, ProMemA-
gent considers the top- m candidate facts with
m= 8 for each new event. At the decision mo-
ment, it retrievesk= 10past events, withk C = 2
for content retrieval and kCT = 8for cue-triggered
retrieval. For reasoner training, each historical con-
text contains K∈ {8,10,12} past events from
the initial timeline. For Positive,Negative, and
State Changeinstances, the formation moment ef
is always included, whileState Change instances
additionally include esc. The remaining events are
sampled at random.
Baseline Implementations.For Proactive
Agent (Lu et al., 2025) and ContextAgent (Yang
et al., 2025c), we follow their original input and
prompting setups while adapting them to our task.
Proactive Agent receives the complete timeline as
event history without personal context, and predicts
whether to provide proactive assistance together
with a response. ContextAgent receives only the
current sensory context and personal context, with-
out access to past events. We follow the original
data-construction procedures of both methods un-
der the default training setup above. Full-context
LLMs use the complete past timeline as histori-
cal context, with the default generation settings
of each model. RAG-based methods use the cur-
rent event as the query and retrieve past events
according to their respective lexical or embedding
similarity. For memory-system baselines, we use
the official implementations of Mem0 (Chhikara
et al., 2025), A-Mem (Xu et al., 2025), MemOS (Li
et al., 2025), and T-Mem (Guo et al., 2026). Mem0
processes up to five consecutive same-day events
per memory update, while A-Mem and MemOS
process one event per update. Except for T-Mem,
all retrieval-based baselines use k= 10 at their na-
tive retrieval granularity (e.g., raw events for RAG,
facts for Mem0). For T-Mem, we evaluate its de-
fault setting, which retrieves 5 scenes and 15 items,
and a horizon-based variant that ranks scenes solely
by similarity between the current event and each
scene’s horizon trigger and retrieves top-10 scenes.
For a fair comparison, all full-context, RAG-based,
and memory-system baselines pass their retrieved
results to the reasoner together with the same per-
sonal context from the dataset.
C Prompts
This section presents the details of the prompts
used in this study, including those for sensory con-
text extraction, memory construction, and proactive
reasoning in ProMemAgent, as well as prompts for
the baselines, data generation, and the LLM judge.
Sensory Context Extraction in ProMemAgent.
Fig. 8 shows the summarized prompt used to ex-
tract visual context from egocentric video clips cap-
tured by smart glasses from the user’s perspective.

Sensory Context Extraction
Task Given timestamped frames from a short egocentric clip
captured by the user’s smart glasses, describe what the user sees
and does. Refer to the camera wearer as “the user” and describe
other visible people from the user’s perspective.
Instruction Summarize the visible sensory context, including
the surrounding place, the user’s movement and ongoing activity,
interactions with other people, relevant objects and their states,
readable text, and visible weather when applicable. Focus on
concrete details that characterize the current situation and stage
of activity. Describe only what is visually observable, without infer-
ring sounds, intentions, feelings, identities, or other unobserved
information.
Input{frames}
Output Write a concise description in the third person and
present tense, using 2–3 sentences (25–50 words).
Examples Seven examples demonstrate the expected content,
style, and level of detail.
Figure 8: Summarized prompt for sensory context ex-
traction in ProMemAgent.
The VLM is instructed to describe the surrounding
environment, the user’s movement and activity, and
visible objects together with their states, providing
the contextual elements needed to represent the
observed event (Radvansky and Zacks, 2011).
Memory Construction in ProMemAgent.Fig. 9
and Fig. 10 show the prompts for prospective cue
generation and cross-event linking. Inspired by
the event-based and time-based forms of prospec-
tive memory (Einstein and McDaniel, 1990),
the cue-generation prompt instructs the memory-
construction LLM to extract factual observations
and anticipate observable contextual or temporal
cues under which the specific factual observation
may become useful. The linking prompt instructs
the LLM to determine whether a newly observed
event is a subsequent development of an earlier
fact in memory, enabling ProMemAgent to capture
how stored observations evolve over time, which is
important for long-horizon proactive assistance.
Proactive Reasoning in ProMemAgent.Fig. 11
presents the prompt for proactive reasoning. The
prompt includes the personal context, retrieved past
events in temporal order as historical context, and
the current sensory context. The task instructions
guide the reasoner to determine whether the his-
torical context provides evidence of an unresolved
delayed intention and whether the current situa-
tion provides an appropriate opportunity to act on
it. The reasoner provides proactive assistance only
when both conditions are satisfied. Otherwise, it
remains silent.
Prompts for Baselines.To ensure a fair compari-
Prospective Cue Generation
Task Given one observed moment from the user’s day, index it
into memory by describing the current situation, recording what
the moment establishes, and anticipating future situations in which
the recorded information may become relevant.
Instruction Describe the current activity, location, salient con-
text, people, time, and a short “The user . . . ” summary as the
current situation. Extract up to three facts grounded in the moment.
For each fact, generate up to two anticipated future situations only
when supported by the observation or clear commonsense knowl-
edge, specifying the expected context and optional future time.
Avoid unsupported details and generic future situations.
Input{event}
Output A structured JSON object containing the current situa-
tion, extracted facts, and any relevant future situations.
Figure 9: Summarized prompt for prospective cue gen-
eration in ProMemAgent’s memory construction.
Cross-Event Linking
Task Given a newly observed moment and a set of earlier candi-
date facts, determine how the new moment relates to the specific
matter described by each fact.
Instruction For each candidate, label the relation as
same_matter if the new moment provides a later development
about the same specific matter, and summarize what has changed.
Usesame_episode when the two moments belong to the same con-
tinuing activity or occasion. Use none when they are unrelated,
merely similar, or the referent is ambiguous. Base the decision
only on the context in the new moment.
Input{event},{candidates}
Output A structured JSON object listing each candidate’s rela-
tion and any observed change.
Figure 10: Summarized prompt for cross-event linking
in ProMemAgent’s memory construction.
son, we keep the task instructions and output format
consistent with those used in ProMemAgent for
full-context LLMs, retrieval-based methods, and
memory systems used in our evaluation. These
baselines differ only in how historical information
is provided to the reasoner, using either the full
event history, the top- k retrieved events, or the
memories retrieved by the corresponding memory
system. For Proactive Agent (Lu et al., 2025) and
ContextAgent (Yang et al., 2025c), we follow their
original prompting and input formulations to pre-
serve their designed proactive reasoning settings.
Prompt for Data Generation.Fig. 12 summarizes
the prompts used for scenario generation in CPM-
Bench. To further diversify the generated data,
we use multiple frontier LLMs, including GPT-
4o (Hurst et al., 2024), Claude-Sonnet-4.6 (An-
thropic, 2026b), and Gemini-2.5-Flash (Comanici
et al., 2025), and human annotators subsequently
verify all generated samples.
Prompt for LLM Judge.Fig. 13 shows the prompt

Proactive Reasoning
Task Given the user’s persona, retrieved earlier moments, and
current moment, decide whether proactive assistance is appropri-
ate now.
Instruction Speak only when an earlier moment indicates some-
thing that needs doing and the current situation provides an op-
portunity to act on it. Stay silent if it has already been resolved,
cannot be acted on now, or does not require assistance. Do not
provide status updates or general advice.
Input{persona},{memory},{current}
Output A JSON object indicating whether to speak and, if so,
the assistance to provide.
Figure 11: Summarized prompt for proactive reasoning
in ProMemAgent.
used by the LLM judge for Positive instances.
The judge determines whether a response addresses
the same intention as the reference and interprets
relative time expressions based on the provided
event timestamps. Generic assistance that does not
identify the delayed intention, such as “You should
take care of that”, is not considered sufficient. For
State Change instances, the judge additionally
receives the state-change event and classifies the
response as still pursuing the resolved intention,
appropriately following up on the state change, or
unrelated to either.
D Evaluation Metrics
We evaluate each method at the decision moment
ed along three dimensions, including memory re-
trieval, proactive decision, and end-to-end assis-
tance. At ed, the agent should provide proactive as-
sistance forPositive timelines and remain silent
for the other three variants.
Memory Retrieval.Delayed intention recall (DIR)
is computed onPositive instances and measures
the fraction of gold delayed intentions whose for-
mation moment ef is retrieved. State-change recall
(SCR) is computed on State Change instances
and measures the fraction of timelines for which
both the formation moment ef and correspond-
ing state-change event esc are retrieved for all in-
tentions. These two variants require recovering
specific historical evidence for correct reasoning,
whileNegative andNo Formation primarily eval-
uate whether the agent appropriately remains silent.
For RAG-based methods and ProMemAgent, re-
trieval is evaluated over the top-k events passed to
the reasoner. For A-Mem and MemOS, an event is
considered retrieved if a retrieved memory is con-
structed from it, while for T-Mem, if it is covered
Data Generation (Core Pair)
Task Generate new scenario pairs for a target category follow-
ing validated seed examples. Each pair contains an intention-
formation moment (T1) and a later decision moment (T2) in which
the intention becomes actionable.
Instruction Describe T1 and T2 as natural, continuous egocen-
tric clips of about 15 seconds using visually observable information,
along with optional conversation and mobile device notifications.
The intention should be inferable from T1, while T2 should provide
an appropriate opportunity to act on it without directly revealing
the intended action. Any self-talk at T1 should describe only the
current situation without explicitly stating the intention or future
plan. Avoid directly revealing the connection between T1 and T2.
Input{n},{category},{examples}
Output A structured JSON object containing the generated sce-
nario pairs, including persona, delayed intention, T1 and T2 con-
texts, and the inference linking the two moments.
Data Generation (Variants)
Task Given a formation–decision pair, generate the additional
assets needed to construct its controlled variants and long-horizon
timelines without modifying the original pair.
Instruction Generate a negative decision context where the in-
tention remains unresolved but cannot be acted on, an observable
state-change event that resolves the intention before the original
decision moment, and an ordinary intention-independent event
to replace the formation moment. Keep all scenes natural and
grounded in observable context, while avoiding cues that reveal
the intended action or duplicate the scripted events.
Input{formation–decision pair}
Output A structured JSON object containing the generated
variant-specific events.
Figure 12: Summarized prompt for data generation.
by a retrieved scene or item. The retrieval metrics
are not applicable to Mem0 because each mem-
ory update jointly represents multiple events, or to
proactive agents and full-context LLMs, which do
not explicitly retrieve past events.
Response Judgment.For Positive instances, an
LLM judge evaluates whether the response cor-
rectly addresses each gold delayed intention using
the prompt in Fig. 13. A delayed intention counts
as a true positive (TP) if the response provides ap-
propriate assistance for the intention, and as a false
negative (FN) otherwise, including when the agent
remains silent. For the other three variants, where
the agent should remain silent ated, an unnecessary
response counts as a false positive (FP), while cor-
rectly remaining silent is counted as a true negative
(TN). For State Change instances, if the agent
responds, the judge further determines whether it
appropriately follows up on the state-change event
esc. Such a follow-up is counted as a TN, while
responses that still act on the resolved intention or
are unrelated are counted as FPs.
Proactive Decision.Following prior work on
proactive agents (Yang et al., 2025c; Lu et al.,

LLM Judge
Task Determine whether the assistant’s response correctly con-
veys the reference delayed intention.
Instruction Judge whether the response refers to the same core
action and specific matter as the reference intention, allowing para-
phrases and omission of secondary details. When the intention
involves relative timing, resolve it using the timestamps and ensure
that the response is temporally appropriate. Generic reminders,
status updates, related mentions without the intended action, or
unspecific inquiries do not count as matches.
Input{t1},{t2},{gold_intention},{assistance}
Output A JSON object containing a brief justification and
whether the response matches the reference intention.
Figure 13: Summarized judge prompt in the evaluation.
2025), we evaluate proactive decision-making us-
ing the false detection rate (FD) and proactive pre-
diction accuracy (Acc-P). FD measures the rate of
unnecessary assistance among instances where the
agent should remain silent and is computed as
FD = FP FP + TN.(2)
Acc-P measures whether the agent makes the cor-
rect proactive decision at ed. Both metrics evaluate
the decision to provide assistance without consid-
ering the correctness of the assistance content.
End-to-End Assistance.To further evaluate the
content of proactive assistance, we report set-level
precision, recall, and F1 based on TP, FN, and FP.
Since an instance may contain multiple gold de-
layed intentions at ed, these metrics operate over
the set of intentions, while for instances with a sin-
gle intention, these metrics are the same as standard
precision, recall, and F1. They are computed as
Set-P = TP TP + FP,Set-R = TP TP + FN,
Set-F1 = 2 Set-P Set-R Set-P + Set-R. (3)
Unlike Acc-P, proactive assistance accuracy (Acc-
PA) further requires the provided assistance to be
correct and is computed as
Acc-PA = TP + TN TP + FN + FP + TN.(4)
We use Set-F1 as the primary end-to-end metric be-
cause it jointly captures missed delayed intentions
and unnecessary proactive responses. All metrics
are reported as percentages in the evaluation.
E Reliability of the LLM Judge
To validate the reliability of the LLM-as-a-judge
evaluation for long-horizon proactive assistance,
Annotator 1 Annotator 2 GPT-5-mini GPT-5.6 Luna
Annotator 1 - 93.9 95.7 89.6
Annotator 2 93.9 - 94.8 95.7
GPT-5-mini 95.7 94.8 - 92.2
GPT-5.6 Luna 89.6 95.7 92.2 -
Table 4: Pairwise agreement (%) between two human
annotators and two LLM judges.
we evaluate judge robustness along two aspects,
following prior work (Li et al., 2026), including
alignment with human judgment and consistency
across different judge LLMs. We compare GPT-5-
mini, the judge used in the experiments, against two
independent human annotators and an additional
frontier LLM judge, GPT-5.6 Luna.
Response Sample.We sample 100 responses
containing proactive assistance from results on
CPMBench, with 20 responses from each method
family, including proactive agents, full-context
LLMs, RAG-based methods, memory systems, and
ProMemAgent.
Human Annotation.Two annotators who did
not participate in benchmark construction indepen-
dently evaluate all sampled responses. They re-
ceive the same inputs as the LLM judge, without
the LLM-as-a-judge outputs.
Results.Table 4 shows strong agreement between
the human annotators and the LLM judges. The av-
erage agreement between GPT-5-mini and the two
annotators is 95.3%, indicating that the LLM judge
used in our main evaluation closely aligns with
human judgments. We further assess robustness
to the choice of judge LLM using GPT-5.6 Luna.
Although its agreement with the human annota-
tors is lower on average, it remains around 90%.
Further analysis of the disagreements shows that
GPT-5.6 Luna applies a stricter evaluation criterion,
with most disagreements occurring when human
annotators and GPT-5-mini accept a response but
GPT-5.6 Luna marks it as unacceptable. Overall,
the high agreement and consistency between hu-
man annotators and LLMs indicate the reliability
of LLM-based evaluation for our task.
F Full Results
Overall performance on CPMBench-Omni.
Tab. 5 reports the complete results on CPMBench-
Omni. Compared with CPMBench, all methods
show lower performance under raw sensory inputs.
This is because raw sensory observations are noisy,
and context extraction may miss fine-grained de-
tails or introduce errors. When accumulated over

Method Memory Retrieval Proactive Decision End-to-End Assistance
DIR↑SCR↑FD↓Acc-P↑Acc-PA↑Set-P↑Set-R↑Set-F1↑
Proactive
Agents
Proactive Agent (8B) - - 4.8 77.7 74.7 63.6 21.5 32.2
ContextAgent (8B) - - 38.7 59.8 47.6 11.0 12.3 11.6
Full-Context
LLMs
(Open- and
Closed-Source)
Qwen2.5-32B - -3.075.4 72.1 50.0 7.7 13.3
Qwen3-4B - - 19.6 67.9 62.2 23.3 15.4 18.5
Qwen3-8B - - 28.6 62.9 57.9 23.8 23.1 23.4
Qwen3-14B - - 12.5 74.1 69.1 40.0 21.5 28.0
Qwen3-32B - - 35.1 67.0 60.5 35.2 49.2 41.0
Llama-3.3-70B - - 7.1 74.6 71.2 45.5 15.4 23.0
GPT-4o - - 16.1 74.6 70.8 47.1 36.9 41.4
GPT-4.1 - - 9.5 79.0 75.5 60.0 36.9 45.7
GPT-5.4-mini - - 4.2 75.4 72.5 53.3 12.3 20.0
GPT-5.4 - - 23.8 75.0 72.1 50.061.555.2
RAG-based
Methods
(GPT-5.4)
all-MiniLM-L6-v2 10.8 8.9 4.8 74.1 71.2 42.9 9.2 15.2
BM25 15.4 5.4 5.4 73.7 70.8 40.0 9.2 15.0
text-embedding-3-small 20.0 10.7 4.8 75.9 73.0 55.6 15.4 24.1
Memory
Systems
(GPT-5.4)
Mem0 - - 4.8 74.1 70.8 38.5 7.7 12.8
A-Mem 24.6 19.6 8.3 75.4 72.5 51.7 23.1 31.9
MemOS 18.5 5.4 5.4 75.0 71.2 43.8 10.8 17.3
T-Mem 30.8 19.6 8.3 75.4 71.2 46.2 18.5 26.4
T-Mem (Horizon-based) 26.2 14.3 9.5 73.7 70.8 44.8 20.0 27.7
Ours ProMemAgent (8B)83.1 66.17.7 85.7 82.8 74.5 58.5 65.5 ProMemAgent (32B)83.1 66.15.488.4 85.4 81.6 61.5 70.2
Table 5: Main results on CPMBench-Omni. All metrics are in percentages (%). The best and second-best results are
inboldand underlined , respectively. “-” denotes inapplicable retrieval metrics.
long histories, these imperfections further chal-
lenge long-context reasoning. This degradation is
particularly evident for several full-context LLMs,
whose recall drops substantially under noisier sen-
sory contexts. In contrast, ProMemAgent main-
tains comparatively robust retrieval from context-
aware memory, suggesting that prospective cues
can remain effective when coarse contextual sig-
nals are preserved. The remaining performance
drop results from downstream proactive reasoning,
where missing fine-grained information can make
it harder to recognize and act on implicit delayed
intentions.
Out-of-Domain Evaluation.Table 6 shows the
overall results of baseline methods and ProMemA-
gent under the out-of-domain setting. We split
the eight everyday categories into five training cat-
egories and three categories excluded from rea-
soner fine-tuning. Results indicate that ProMemA-
gent maintains retrieval performance comparable
to that under the main split, indicating that its
memory retrieval remains effective across differ-
ent scenario categories. With the same retrieved
context, fine-tuning improves Set-F1 by more than
20 points over the base Qwen3-8B reasoner on the
held-out categories, showing that the learned proac-
tive reasoning transfers beyond category-specific
assistance patterns. Notably, even without fine-
tuning, ProMemAgent’s retrieval combined with
the base reasoner (w/o SFT) outperforms full-
context Qwen3-8B by more than 10 points in Set-
F1, further indicating the benefit of retrieving rele-
vant historical context for long-horizon proactive
assistance. Overall, ProMemAgent retains its ad-
vantage over all baselines on unseen categories,
consistent with the main evaluation.
mBackbone Memory Retrieval Proactive Decision End-to-End Assistance
DIR↑SCR↑FD↓Acc-P↑Set-P↑Set-R↑Set-F1↑
4 GPT-4o-mini 81.3 71.0 4.3 89.0 85.7 63.4 72.9
8 GPT-4o-mini 81.3 72.0 4.3 90.0 86.3 66.7 75.2 GPT-4.1-mini 80.5 71.0 3.3 90.5 89.2 67.5 76.9
12 GPT-4o-mini 81.3 73.0 3.0 90.5 89.9 65.0 75.5
16 GPT-4o-mini 80.5 71.0 3.3 90.2 88.6 63.4 73.9
Table 7: Sensitivity of ProMemAgent’s memory con-
struction to the backbone LLM and the number of can-
didate factsmconsidered for cross-event linking.
Sensitivity to Memory Construction.Table 7
shows ProMemAgent’s results with different mem-
ory construction LLMs and candidate budgets m
for cross-event linking, using the same retrieval
configuration and proactive reasoner. When re-
placing the default memory construction model,
GPT-4o-mini, with GPT-4.1-mini, ProMemA-
gent achieves comparable retrieval and end-to-end
performance, indicating robustness to the choice
of construction model. Performance also remains

Method Memory Retrieval Proactive Decision End-to-End Assistance
DIR↑SCR↑FD↓Acc-P↑Acc-PA↑Set-P↑Set-R↑Set-F1↑
Proactive
Agents
Proactive Agent (8B) - - 6.9 77.9 74.4 65.6 30.5 41.7
ContextAgent (8B) - - 37.9 60.5 48.3 15.3 16.0 15.7
Full-Context
LLMs
(Open- and
Closed-Source)
Qwen2.5-32B - - 12.4 73.0 67.5 41.5 20.6 27.6
Qwen3-4B - - 13.4 70.8 64.8 30.5 13.7 18.9
Qwen3-8B - - 24.5 70.1 64.1 39.5 37.4 38.4
Qwen3-14B - - 13.4 74.3 68.9 46.8 27.5 34.6
Qwen3-32B - - 28.1 73.0 67.7 46.9 58.0 51.9
Llama-3.3-70B - - 18.6 69.6 64.8 37.4 26.0 30.6
GPT-4o - - 15.4 79.9 75.1 59.5 52.7 55.9
GPT-4.1 - - 10.5 83.3 79.2 69.2 55.0 61.3
GPT-5.4-mini - - 6.2 76.0 70.7 53.7 16.8 25.6
GPT-5.4 - - 22.2 80.9 77.3 59.576.366.9
RAG-based
Methods
(GPT-5.4)
all-MiniLM-L6-v2 6.1 4.93.375.2 69.6 44.4 6.1 10.7
BM25 13.7 7.8 4.9 75.0 70.3 51.6 12.2 19.8
text-embedding-3-small 13.7 8.8 5.9 75.2 69.6 47.1 12.2 19.4
Memory
Systems
(GPT-5.4)
Mem0 - - 4.9 75.2 68.9 40.0 7.6 12.8
A-Mem 22.9 17.6 6.5 77.0 71.6 57.4 20.6 30.3
MemOS 22.9 4.9 9.2 74.5 69.3 47.2 19.1 27.2
T-Mem 29.0 19.6 7.2 75.2 69.6 47.6 15.3 23.1
T-Mem (Horizon-based) 55.7 21.6 16.3 76.2 71.4 52.8 42.7 47.3
Ours ProMemAgent (8B)80.2 69.63.9 89.2 86.5 87.564.1 74.0 w/o SFT 80.2 69.6 17.6 77.9 72.8 55.0 50.4 52.6
Table 6: Out-of-domain results on CPMBench, with three categories excluded from reasoner fine-tuning.
stable as m varies from 4 to 16, showing that the
design of cross-event linking is robust to the candi-
date budget.
