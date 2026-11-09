---
title: Designing Proactive Thought Partners for Writing
url: https://arxiv.org/abs/2609.01588
category: ai-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Chao Zhang
- Abe Davis
- Chih-Wei Chen
- Chin-Chia Hsu
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.01588
pages: 30
chars: 108162
fetched_at: '2026-11-08T13:33:07+00:00'
kb_version: 1
---

# Designing Proactive Thought Partners for Writing

Designing Proactive Thought Partners for Writing
Chao Zhang*, 1, Abe Davis1, Chih-Wei Chen2 and Chin-Chia Hsu2
*Work done during an internship at Google DeepMind.,1Cornell University,2Google DeepMind
Writing involves diverse cognitive activities, from ideation to revision, and writers’ needs vary across in-
dividuals and moments. Proactive AI promises to provide the right support at the right time, yet existing
proactive tools largely focus on generic textual assistance, such as autocomplete. This paper studies the
designspaceofproactive thought partners: AIagentsthatproactivelyoffercustomizable, higher-levelcog-
nitive support during writing. We instantiated this concept in a technology probe and deployed it with 16
participants for one week. The probe allows users to create partners by configuring their roles and proac-
tivity. As users write, relevant partners take the initiative at appropriate moments to offer suggestions.
Our findings show that participants configured proactive support through prospective planning, used
suggestions for both idea generation and self-monitoring, and valued lightweight visual representations
alongside non-directive rhetorical framing for non-intrusive interventions. We derive implications for
designing proactive writing assistants around customization, timing, engagement, and representation.
Keywords: Writing, Proactive AI, Human-AI Interaction
1. Introduction
Writing is a dynamic cognitive process (Flower and Hayes, 1981). From one moment to the next,
a writer might shift between developing ideas, selecting prose, and evaluating written text in light of
broader narrative goals. The support they need can therefore change throughout the writing process.
At one moment, a writer may benefit from an example that makes an abstract claim concrete; at
another, they may need help considering an alternative perspective or deciding how to develop the
next section. These needs also vary across writers. Some writers may want support that helps them
develop and evaluate their own ideas, while others may prefer information-seeking assistance, such as
suggesting evidence from outside their domains. An ideal writing assistant should therefore support
this shifting and personal cognitive work byoffering the right kind of help at the right moment.
Existing proactive writing assistance approaches this ideal in a narrower setting. At the level of
local text production, writing is relatively structured and predictable: the surrounding text often
provides strong signals about useful continuations, while observable interaction events, such as pauses,
can provide natural opportunities for intervention (Chen et al., 2019). Prior work has therefore
leveraged such signals to proactively provide local textual assistance, such as autocomplete and next-
phrase suggestions (Bhat et al., 2023; Buschek et al., 2021; Jakesch et al., 2023). However, writing
involves more than choosing words. Higher-level cognitive activities such as ideation, reflection, and
revision are more dependent on the writer’s preferences and evolving context (Flower and Hayes,
1981). In contrast to local textual assistance, support for these higher-level activities has largely
relied on reactive interfaces, where tools respond only after users explicitly request assistance through
prompts, buttons, or menus (Gero et al., 2022; Reza et al., 2023; Zhang et al., 2025a).
WestudyproactiveAIassistantsthatsupportthesehigher-level,personalcognitiveneedsinwriting,
which we callproactive thought partners(Fig. 1). We instantiated this concept in a technology
probe (Hutchinson et al., 2003), using customization as both an interaction design mechanism and an
inquiry instrument for exploring the design space. The probe allows users to create thought partners
by customizing both theirrolesandproactivity. First, users define each partner’s role to specify the
Corresponding author(s): Chao Zhang, cz468@cornell.edu
©2026 Google. All rights reserved
arXiv:2609.01588v1  [cs.HC]  1 Sep 2026

Designing Proactive Thought Partners for Writing
Figure 1 | Proactive thought partners in the design space of intelligent writing assistants.We position
intelligent writing assistants along two dimensions: initiative, distinguishing reactive user-invoked
support from proactive system-initiated support, and level of support, distinguishing textual assistance
from higher-level cognitive assistance. Proactive thought partners fall within the proactive and
cognitive quadrant, where AI offers higher-level cognitive support during writing without requiring
explicit user prompting.
type of cognitive support they need. Second, users define timing conditions to specify when the
partner should intervene. As users write, relevant partners take the initiative at appropriate moments
to offer suggestions, which users can easily dismiss, use as inspiration, or ask the partner to apply
directly to the document.
We deployed this probe with 16 participants in a one-week diary study followed by semi-structured
interviews. Our findings show how users customized, engaged with, and experienced this new form of
proactive support for writing. Participants used customization to translate anticipated needs and likely
difficulties into different forms of cognitive support and timing conditions, treating configuration as an
act of prospective planning. During writing, they often ignored interventions to preserve flow, while en-
gaged suggestions supported both idea generation and self-monitoring. Participants also found proac-
tive support less intrusive when it was presented through lightweight visual representations and non-
directive rhetorical framing. Our findings suggest design implications for proactive thought partners
across four dimensions of the design space: customization, timing, engagement, and representation.
In this work, we contribute:
• Proactivethoughtpartners, a new design concept for intelligent writing assistants that proactively
provide higher-level and personal cognitive support through customizable AI partners.
• A technology probethat enables writers to create proactive thought partners by configuring their
roles and proactivity, allowing us to study customizable, proactive cognitive support in situated
writing practice.
• Empirical insights and design implicationsfrom a one-week diary study with 16 participants,
revealing how users customize proactive cognitive support to suit their needs and how they engage
with proactive suggestions during writing. These findings articulate a design space for proactive
thought partners in writing.
2

Designing Proactive Thought Partners for Writing
2. Related Work
In this section, we first situate our work within the broader landscape of intelligent writing tools. We
then review prior research on proactive AI assistants and customizable AI agents to discuss how our
work extends these lines of research.
2.1. Intelligent Writing Tools
Flower and Hayes’s cognitive process theory of writing understands writing as a recursive cognitive
process involving planning, translating ideas into text, and reviewing what has been written (Flower
and Hayes, 1981). Intelligent writing tools have long supported parts of this process by helping
writers produce, correct, or refine text (Lee et al., 2024). For example, autocomplete and predictive
text systems offer word- or phrase-level continuations (Arnold et al., 2020; Bhat et al., 2023; Buschek
et al., 2021; Jakesch et al., 2023), while spelling, grammar, and style checkers (Chang and Chang,
2015; Chung et al., 2025; Grammarly, 2025) help identify local errors or improve surface-level
expression. These systems can reduce the effort of text production and revision by providing relatively
narrow forms of (sometimes proactive) assistance focused on the immediate text.
Recent advances in large language models (LLMs) have expanded the scope of AI writing support.
Rather than only correcting or completing text, LLM-based systems can help writers brainstorm
ideas (Chou et al., 2023; Gero et al., 2022; Huang et al., 2020), generate outlines (Wan et al., 2023,
2025), draft passages (Zhang and Davis, 2026; Zhang et al., 2026a,b), rewrite text (Ito et al., 2023;
Lee et al., 2022; Masson et al., 2025), provide feedback (Benharrak et al., 2024; Liu et al., 2026b;
Zhang et al., 2025a), and explore alternatives (Reza et al., 2023; Zhang et al., 2025b) across a wide
range of writing contexts (Chung et al., 2022; Huang et al., 2020; Shen et al., 2023; Sun et al., 2024;
Yuan et al., 2022; Zhang et al., 2025a, 2023). This line of work shows that AI writing assistants
can support higher-level cognitive activities such as ideation (Gero et al., 2022; Huang et al., 2020),
reflection (Zhang et al., 2025a), and revision (Zhang et al., 2025b) than accelerating text production.
However, much of this richer cognitive support remains reactive. Writers often need to leave the flow
of writing to compose prompts, select text, click buttons, or otherwise explicitly invoke the system.
This places the burden on writers to recognize when they need help, formulate the right request,
and decide which kind of support to seek. At the same time, more proactive writing support has
largely been associated with predictive text, grammar diagnosis, and next-phrase suggestions (Arnold
et al., 2020; Bhat et al., 2023; Buschek et al., 2021; Chang and Chang, 2015; Jakesch et al., 2023;
Tsai et al., 2020). This creates a gap between two forms of assistance: systems that are proactive
but focused on text continuation/correction, and systems that provide broader cognitive support
but require explicit user initiation. Our work explores the design space in this gap that combines
proactivity and cognitive support in writing, which we term “proactive thought partners.”
2.2. Proactive AI Assistants
Rather than waiting for users to formulate a prompt or click a menu, proactive AI assistants take
the initiative by offering assistance when they anticipate it may be useful. This idea builds on a
long tradition of mixed-initiative interaction, where both users and systems can take initiative in
pursuit of a shared task (Horvitz, 1999). Recent work has explored proactive AI in domains such as
programming (Chen et al., 2025a; Kuo et al., 2026; Pu et al., 2025), meetings (Chen et al., 2025b),
design (Son et al., 2026), surveys (Liu et al., 2026a), tool manipulation (Prasongpongchai et al.,
2025), scholarly recommendation (Siangliulue et al., 2026), storytelling games (Kreminski et al.,
2020), web search (Huang and Narechania, 2026), problem-solving (Luo et al., 2026), and group
collaboration (Mukhopadhyay et al., 2026; Zhou et al., 2026), where systems may surface relevant
3

Designing Proactive Thought Partners for Writing
information, reflect on goals, or suggest next steps. In line with the most recent work on proactive
AI (Chen et al., 2025a,b; Pu et al., 2025) and an early Wizard-of-Oz study simulating proactive AI
for writing (Yin et al., 2026), we define proactivity as the system actively inferring user needs and
offering suggestions without requiring explicit user prompting.
Timing is key to system initiative (Bailey et al., 2001; Horvitz, 1999). Existing proactive writ-
ing assistants often tie the timing of interventions to observable interaction events. For example,
autocomplete systems surface continuations as writers type (Arnold et al., 2020; Bhat et al., 2023;
Buschek et al., 2021; Chen et al., 2019; Jakesch et al., 2023), while Lehmann et al. (2026) allowed
users to bundle autonomous tasks with triggers such as pauses, edits, or saves. In these systems, such
events directly cue system action. However, the same event can reflect different writing states. A
pause, for example, may indicate concentration, being stuck for ideas, or reviewing recently written
text. For higher-level cognitive support, interaction events alone may therefore be insufficient to
determine whether assistance is needed and what kind of support would be useful. Our work extends
this event-based approach by introducingcontextual heuristics, which specify more specific timing
conditions under which a partner should intervene when a broader interaction event occurs. This
distinction also allows us to study how users conceptualize these two forms of timing differently:
event triggers as broad opportunities for the system to check whether support may be relevant, and
contextual heuristics as more specific conditions for determining whether and which support should
actually be provided. In doing so, we examine how users expect proactive cognitive support to
interpret their evolving writing context when deciding whether and which support to provide.
More closely aligned with our vision, Yin et al. (2026) conducted a Wizard-of-Oz study in which
a human simulated proactive AI by interpreting the writing context and offering suggestions while
another human wrote a story. The study provides quantitative evidence that proactive AI, as simulated
by a human, can enhance creativity by serving as a catalyst for inspiration rather than as a direct
contentprovider. However, itremainsunclearhowsuchproactivecognitivesupportshouldbedesigned
in a functional system, how writing context should be interpreted to determine when support is
appropriate, and how users might customize proactive thought partners to suit their own needs.
In this paper, we instantiate proactive cognitive support in a functional system with customizable
thought partners and deploy it in a diary study to investigate how users configure, experience, and
evaluate such support in practice.
2.3. Customizable AI Agents
A growing body of HCI research has explored customizable AI agents as a way to better align LLM-
based systems with users’ goals, preferences, and contexts. Prior work has examined customization in
domains such as writing (Benharrak et al., 2024; Lehmann et al., 2026), emotional support (Zheng
et al., 2025), social chatbots (Ha et al., 2024), research ideation (Liu et al., 2026c), and collaborative
brainstorming (Quan et al., 2026). Across these settings, customization allows users to shape how
an AI system should behave, what role it should take, and how it should respond to domain-specific
needs. For emerging AI interaction concepts, customization can also serve as a probe mechanism in a
study (Zheng et al., 2025): by observing what users choose to customize, researchers can surface
latent needs, preferences, and expectations that may be difficult to anticipate a priori.
Customization is particularly important for writing because useful support depends on the writer’s
goals, genre, audience, voice, and stage in the writing process. Given so, prior work has explored
writer-defined AI personas for on-demand feedback (Benharrak et al., 2024), multiple user-defined
agents and tasks in collaborative document editing (Lehmann et al., 2026), and layered interfaces for
aligning content development with rhetorical strategy (Siddiqui et al., 2025). Recent work on just-in-
time objectives further shows how AI systems can infer a user’s in-the-moment goals from observed
4

Designing Proactive Thought Partners for Writing
context, such as screenshots and webpage text, and use these objectives to generate specialized expert
responses or customized tools for the user’s current task (Lam et al., 2025). These systems show
that customization can help writers access diverse perspectives, delegate specialized tasks, generate
situated tools, and better align AI support with their communicative intentions.
However, existing customizable writing agents are primarily invoked on demand: writers can
define who the AI should be, what it should do, or what objectives it should optimize for, but they
must still invoke it manually. Our work introduces a new customization dimension: theproactivityof
AI writing agents. In our probe, writers can shape both the type of cognitive support they receive and
the moments when that support enters the writing process. These user configurations provide unique
empirical insights into how writers imagine, configure, and bound proactive AI support, helping us
map the broader design space of proactive cognitive support for writing.
3. Design Goals
We designed our system as a technology probe:an instrument deployed to investigate an open-ended
design space and return useful or interesting data about users’ practices, needs, and values(Hutchinson
et al., 2003). Thus, rather than aiming to build an optimal writing system, our goal was to create a
functional, deployable writing environment in which users could create and use proactive thought
partners for their own writing tasks. This allowed us to surface insights into how users would
appropriate proactive thought partners and how they would experience customizable, proactive AI
support during writing. Specifically, we designed the probe around three goals.
[DG1] Support user-configurable proactive partners:We use customization as a lens to understand
how users expect proactive thought partners to support their writing practices and needs. Based
on prior work on customizable AI agents (Benharrak et al., 2024; Lehmann et al., 2026; Zheng
et al., 2025) and mixed-initiative systems (Bailey et al., 2000, 2001; Chen et al., 2025a; Horvitz,
1999; Luo et al., 2026; Pu et al., 2025), we focus on two basic forms of user customization: the role
and proactivity of partners. The role specifies what kind of support the partner should provide, a
dimension emphasized in much prior work on customizable AI agents. The proactivity, by contrast,
specifies when and under what writing contexts the partner should intervene, including the moments
that should be treated as candidates for support and the contextual conditions under which the
partner should take the initiative.
[DG2]Enableflexibleengagementwithproactivesupport:Proactivesupportcanarriveatmoments
whenusersmayormaynotwantassistance. Atdifferentmoments,usersmayalsodesiredifferentlevels
of AI involvement in their writing process (e.g., inspiration or direct text generation). Thus, the probe
needs to preserve user agency over how AI engages in writing (Horvitz, 1999). Informed by prior work
onhuman-AIco-writing(Carreraetal.,2025;Draxleretal.,2024;FundalandBizzoni,2026;Yehetal.,
2025; Yin et al., 2026), we investigate three forms of engagement: users can ignore a suggestion, use
it as inspiration, or ask the partner to apply changes directly to the document. Together, these options
allow users to treat proactive suggestions as peripheral cues, sources of inspiration, or actionable
edits, while allowing us to observe how users dismiss, accept, or use proactive AI support in practice.
[DG3] Embed proactive support in a lightweight writing environment:To study proactive thought
partners in use, the probe needs to support writing as an ongoing activity rather than a one-off inter-
action with an assistant. We therefore aim to embed proactive support in a lightweight but functional
and deployable writing environment that provides the basic affordances needed for composing and
revising text while minimizing additional interface complexity. This allows users to engage with
proactive support during their own writing tasks without making the writing environment itself the
5

Designing Proactive Thought Partners for Writing
Figure 2 | Writing environment with proactive thought partners.The probe consists of a lightweight
Markdown editor (A) and a side panel (B) for proactive suggestions. As writers compose text, relevant
partners take the initiative to surface contextually relevant suggestions alongside the draft. Here, the
Evidence Partner notices an unfinished example and suggests concrete ways to support the claim
about training habits.
primary focus of the study. At the same time, the environment should enable the partners to monitor
writing traces, detect candidate moments for intervention, and surface proactive support in context.
4. Proactive Thought Partners: A Technology Probe
In this section, we describe the design and implementation of our technology probe, guided by the
design goals above and inspired by Horvitz’s principles of mixed-initiative user interfaces (Horvitz,
1999). The probe consists of three main interfaces. First, an onboarding panel allows users to log
in and describe their writing goals for a writing session. Second, a partner configuration panel allows
users to create, configure, and enable proactive thought partners (Fig. 3). Third, a lightweight
Markdown editor allows users to write with their enabled partners (Fig. 2). The following subsections
describe the probe in four parts: how users create and configure proactive thought partners (§4.1),
how the probe activates relevant partners at opportune moments in the ongoing writing process
(§4.2), how the activated partners generate thought-provoking suggestions (§4.3), and how users
can engage with proactive suggestions once they appear (§4.4).
4.1. Partner Customization
In the configuration panel, users can create a proactive thought partner by specifying a name and
emoji, a role, one or more event triggers, and a contextual heuristic. Together, these fields allow users
to customize both the partner’s role and its proactivity (DG1): what kind of support the partner should
provide, when it may intervene, and under what contextual conditions its intervention may be useful.
• Partner Roledefines the partner’s expected responsibility and capability, such as helping generate
ideas, identifying weak evidence, or challenging an argument. This field follows prior work on
customizable AI agents by allowing users to define the kind of support they want from an AI
collaborator (Benharrak et al., 2024; Lehmann et al., 2026; Zheng et al., 2025).
• Event Trigger(s)define an observable user action that may indicate an opportunity for proactive
support, such as pausing, completing a sentence, or selecting text. Inspired by prior work on
proactive AI (Bailey et al., 2000, 2001; Chen et al., 2025a; Luo et al., 2026; Pu et al., 2025), this
6

Designing Proactive Thought Partners for Writing
Figure 3 | Configuring proactive thought partners.The configuration panel allows users to design and
enable their own proactive thought partners. Users first specify a name and emoji for a partner, then
define the role (A), select event triggers (none is selected by default to avoid anchoring effects), (B),
and specify a contextual heuristic that determines when the partner should take the initiative after a
selected event (C). In this example, the Evidence Partner is configured to help strengthen claims by
suggesting evidence when the writer pauses and the current context calls for examples.
field allows users to specify broad candidate moments when a partner may consider intervening.
Users can select one or more triggers for each partner.
• Contextual Heuristicdefines the contextual criteria under which the partner should take the
initiative following a triggering event. Drawing on work in context-aware computing (Byun and
Cheverst, 2002; Dey, 2001), this field reflects how users expect the proactive system to interpret
the writing context and make judgments. By specifying contextual heuristics, users definespecific
timing conditions (such as when a claim lacks evidence or an argument may need a counterpoint)
under which a particular partner would be relevant and helpful whenbroadevent triggers occur.
4.2. Partner Activation
Event triggers and contextual heuristics together determine when a partner may step in (Fig. 4):
triggers identify broad candidate moments for intervention, while heuristics determine whether a
partner is relevant to the current writing context in a more precise way. First, we implemented three
event triggers, each grounded in a different rationale from prior work on proactive AI (Chen et al.,
2025a; Pu et al., 2025; Yin et al., 2026), interruption management (Bailey et al., 2001; Czerwinski
et al., 2000; Iqbal et al., 2005; Miyata and Norman, 1986), and keystroke analysis of writing (Baaijen
et al., 2012; Galbraith and Baaijen, 2019; Matsuhashi, 1981; Schilperoord, 2022). These triggers
are rule-based and operate on user keystrokes monitored in real time within the editor.
• Long Pause:The first rationale is that opportune moments for interruption often occur during
natural breaks in user activity (Bailey et al., 2000, 2001; Czerwinski et al., 2000). In writing,
pauses have long been seen as natural breaks in writers’ cognitive processes (Barkaoui, 2019;
Chenu et al., 2014; Medimorec and Risko, 2017). In our probe, the pause trigger fires after a
period of user inactivity in the editor, set to 5 seconds by default and customizable by users.
• Sentence End:The second rationale is that interventions are often perceived as less disruptive at
task or subtask boundaries (Czerwinski et al., 2000; Iqbal et al., 2005; Miyata and Norman, 1986).
7

Designing Proactive Thought Partners for Writing
Figure 4| System pipeline for proactive thought partners.When an event trigger (e.g., a pause, sentence
end, or text selection) occurs, the system gathers contextual information about the writer’s session
goal, current text, and writing behaviors, including keystroke logs. It then evaluates the user-defined
contextual criteria of all enabled partners and activates the partner or partners, if any, whose criteria
best match the current situation. Each activated partner generates a suggestion that includes both an
acknowledgment of the inferred user intent and a question-style suggestion based on its role.
We operationalize this rationale through a sentence-end trigger, because completing a sentence
creates a natural boundary in the flow of writing. To avoid interrupting rapid typing, the system
waits for a short idle period after sentence completion, set to 1 second by default and customizable.
• Text Selection:The third rationale draws from proactive AI tools that treat users’ implicit actions
as signals of possible need (Nam et al., 2024; Pu et al., 2025). Although text selection is a more
explicit signal than passive inactivity, we followed recent work on proactive AI (Pu et al., 2025) and
included it as a trigger because it still enables a lightweight form of proactivity: the writer does
not need to formulate a prompt or select a specific command for a partner to offer support. When
a user selects text and remains idle for a short period, set to 5 seconds by default and customizable
by users, the system treats the selected span as the local focus for possible partner intervention.
When an event trigger occurs, the system sends the writer’s session goal, the current text in the
editor, the recent writing behaviors, and the list of enabled partners associated with that event trigger
to an LLM-based decision engine (Fig. 4). The writing behaviors include the current cursor position,
the trigger event, and the keystroke logs from the 15 seconds1 before the trigger. Based on this
contextual information, the decision engine selects at most two enabled partners, if any, to intervene
at that moment by checking whether their user-defined contextual heuristics are satisfied. Activated
partners appear as small floating tags in the right-side panel (Fig. 5A.1), aligned with the user’s
current cursor position. Each tag displays the partner’s emoji and name, providing a lightweight
peripheral cue before users decide how to engage with it (§4.4).
4.3. Suggestion Generation
The activated partner will generate a suggestion based on the current writing context. Users see this
suggestion after they click the floating tag (Fig. 5C). Each suggestion contains two components.
• Acknowledgement: First, the partner briefly acknowledges what the writer has just done, is
currently doing, or may be trying to do next. This component is inspired by writing-feedback
research emphasizing that effective feedback should first locate itself in the writer’s current draft
and make visible what the responder understands the writer to be attempting, before offering
guidance for next steps (Nicol and Macfarlane-Dick, 2006; Sommers, 1982).
1We use a 15-second window, following prior keystroke-analysis studies that used similarly short windows to infer user
states such as boredom and engagement (Bixler and D’Mello, 2013; Kuvar et al., 2023).
8

Designing Proactive Thought Partners for Writing
Figure 5 | Forms of engagement with proactive suggestions.When a writer pauses after typing (A.1), an
activated partner first appears as a lightweight floating tag (A.2). If the writer ignores the tag and
continues writing (B.1), it gradually fades out and disappears (B.2). If the writer clicks the tag, it
expands into a suggestion card (C.1), where the writer can inspect the suggestion and optionally click
the message icon (C.2) to ask follow-up questions. If the writer hovers over the suggestion card and
clicks theHelp Me Writebutton (D.1), the partner directly inserts or revises text in the editor (D.2),
after which the writer can accept or revert the change (D.3).
• Suggestion: Second, the partner offers a thought-provoking suggestion tailored to the current
context. We frame this suggestion as a question because prior work suggests that question-style AI
suggestions can stimulate high-quality ideas while preserving users’ ownership (Maier et al., 2026).
For example, the Evidence Partner responds to a writer who has just introduced the importance
of elite players’ training habits:
It looks like you are moving from general principles to concrete examples from elite players.
How might you introduce a specific anecdote or training philosophy from a top player, such as
Rafael Nadal’s relentless drills or Roger Federer’s recovery routines, to illustrate the principles
you just mentioned?
4.4. Engagement Forms
Once the floating tags of activated partners appear, users can choose whether and how to engage
with the proactive interventions in three ways (DG2).
• Ignoring(Fig. 2B):Ifwritersdonotneedsupportatthatmoment, theycansimplycontinuewriting.
The floating tag gradually fades out and disappears after 15 seconds. This allows proactive support
to remain optional and low-commitment: the system can make a bid for the writer’s attention
without requiring an explicit dismissal or interrupting the writing flow. This also reflects the
principle of allowing efficient direct termination for mixed-initiative user interfaces (Horvitz, 1999).
• Inspiring(Fig. 2C): Users can click the floating tag to reveal a suggestion. The tag expands into a
floatingcardatthesamepositiondisplayingthepartner’ssuggestion. Thesuggestionservesasinspi-
ration for the user to continue developing or refining their prose. Users can also click a message icon
to engage in a follow-up conversation with the partner. This allows them to clarify the suggestion,
ask for alternatives, challenge the partner’s framing, or explore related ideas before continuing.
9

Designing Proactive Thought Partners for Writing
•Executing(Fig. 2D): If writers decide the suggestion should be incorporated into the document,
they can optionally ask the partner to execute it by inserting or revising text directly in the editor.
Executingrepresentsthedeepestformofengagementinourprobe: thepartnermovesfromoffering
cognitive scaffolding to temporarily taking over part of the writing work, while the writer retains
control by explicitly initiating the action and reviewing the resulting change before accepting it.
Together, these three forms of engagement represent increasing levels of AI involvement. Writers
can ignore a partner’s intervention, treat it as inspiration, or delegate concrete writing actions. This
graduated interaction design aims to preserve writer agency while still allowing proactive partners to
provide more substantive support when writers want it. At the same time, these engagement options
serve a probing function: by observing whether writers ignore, open, discuss, or execute proactive
suggestions, we can examine how they prefer AI to engage in their writing process.
4.5. Implementation
Our probe is implemented with Next.js2, which supports server-side rendering and backend API
routes for calling external services, including the Google Gemini APIs3 for LLM-based functions and
Firebase APIs4 for logging user events. The Markdown editor is built with BlockNote5. We also
adapted BlockNote’s AI SDK integration to support partners’ text insertion and revision in the editor
when invoked by users. Keystroke logging is implemented with JavaScript event listeners, following
prior implementation practices from Tian et al. (2025). For the decision engine that selects which
partners should intervene, we usegemini-2.5-flash-lite to minimize latency. In practice, the
decision engine takes less than one second to select partners after an event is triggered. The partner’s
floating tag appears immediately (Fig. 5) after the decision is made to reduce participants’ perceived
latency, while the partner agent takes approximately eight seconds to generate a suggestion. For
other LLM-based tasks, including suggestion generation, follow-up discussion, and text insertion or
revision, we usegemini-2.5-flash. The prompts are provided in the supplementary materials.
5. User Study
We conducted a one-week technology probe study with 16 participants to explore how writers cus-
tomize, experience, and engage with proactive thought partners in writing practice. It is important to
note that a technology probe study is not an evaluative study of a finished product’s efficacy. Instead, it
isanexploratorydeploymentintendedtoinspirenewdesigndirectionsanduncoverhowusersadaptto,
appropriate, and make sense of a nascent technology in practice (Kaur et al., 2020; Lu et al., 2024; Sey-
mour et al., 2020). In this spirit, our deployment aimed to investigate the following research questions:
RQ1 Partner Creation.How do users create and configure their proactive thought partners to suit
their writing needs?
RQ2 Suggestion Engagement.How do users engage with proactive suggestions from these partners
during writing?
RQ3 User Experience.How do users experience this new form of customizable, proactive cognitive
support for writing?
2https://nextjs.org/
3https://ai.google.dev/gemini-api/docs
4https://firebase.google.com/
5https://www.blocknotejs.org/
10

Designing Proactive Thought Partners for Writing
Table 1| Participant demographics and writing activity.This table presents participants’ ages, genders,
role, whether they are native English speakers (NES), self-reported frequency of AI usage for writing
prior to the study, number of completed writing sessions, and writing contexts across sessions. Writing
contexts are categorized based on the taxonomy (i.e., Academic, Creative, Journalistic, Technical,
Professional, Personal) proposed by Lee et al. (2024).
ID Gender Age Job Title NES? AI Usage Writing Sessions and Contexts
P01Male 45 Software Engineer No Daily Creative, Professional, Personal, Technical
P02Male 28 Software Engineer No Weekly Academic (3), Creative
P03Female — Program Manager No Daily Academic (2), Creative, Personal
P04Female 44 Program Manager No Daily Academic (2), Creative, Professional
P05Female 29 Software Engineer No Weekly Academic (2), Personal, Creative
P06Male 37 Customer Engineer Yes Daily Technical (2), Professional (2)
P07Female 34 Software Engineer No Weekly Personal (3), Technical
P08Female 31 Commercial Strategist Yes Weekly Personal (3), Academic
P09Female 38 Content Strategist Yes Daily Academic (2) Journalistic, Creative
P10Female 29 Software Engineer Yes Daily Academic (4)
P11Female 26 Systems Engineer No Weekly Personal (2), Professional, Journalistic
P12Male 38 Pricing Specialist No Weekly Professional (2), Creative, Journalistic
P13Female 42 Program Manager Yes Daily Personal (3) Creative
P14Female 35 Communications Manager No Daily Personal (2) Academic, Technical
P15Female 53 Executive Operations Lead No Daily Personal (2), Academic (2)
P16Male 53 Application Engineer No Daily Technical (3), Professional (2), Personal
5.1. Participants
Werecruited16participantsthroughanorganizationalmailinglistwithmorethan10,000recipientsat
a large global software company (Table 1). Participants ranged in age from 26 to 53 years (𝑀= 37.47,
𝑆𝐷= 8.57; one participant preferred not to disclose their age), with 11 identifying as female and 5
as male. Because the study involved open-ended writing tasks in English, we required participants
to be proficient in reading and writing in English; 5 were native speakers and 11 were non-native
speakers. We did not stratify recruitment by level of professional writing expertise. Instead, we
sought everyday writers with regular writing practices rather than focusing exclusively on expert or
novice writers. Participants therefore came from diverse professional backgrounds, including content
strategy, communications, software engineering, and program management.
To ensure that participants could meaningfully engage with and reflect on the probe, we purpo-
sively sampled individuals with prior experience using AI tools for writing. During the three months
preceding the study, 10 participants reported using AI tools on a daily basis, and 6 used them weekly.
Participants shared their detailed experiences with AI-assisted writing, including specific tools used
and their primary writing purposes. In summary, participants used various AI tools such as ChatGPT,
Gemini, Claude, and Smart Compose in Gmail. They applied these tools to a wide range of tasks,
including drafting technical and professional documentation (e.g., daily reports, policy documents,
research papers), managing routine correspondence, and engaging in personal or creative writing
(e.g., fiction, journaling, scripts). Across these contexts, participants used AI throughout the writing
process to brainstorm outlines, draft content, and iteratively edit for tone, clarity, and conciseness.
11

Designing Proactive Thought Partners for Writing
5.2. Procedure
The study consisted of three phases: an onboarding session, a week-long diary study, and a concluding
semi-structured interview. Before the onboarding session, participants provided informed consent
and completed a demographics questionnaire. After the study, each participant was compensated
$140 for their participation.
Phase 1: Onboarding (60 minutes):We conducted a remote onboarding session with each partic-
ipant. Participants first received a short tutorial on the probe’s core features. To help participants
become familiar with the concept of proactive thought partners, we also provided four preconfigured
partners during onboarding: anIdeation Partner, anEvidence Partner, aRebuttal Partner, and aLogical
FallacyPartner. Thesepartnersweredesignedaroundthewarm-upwritingtaskbelowandinformedby
prior work on AI-assisted argumentative writing, such as VISAR (Zhang et al., 2023). Details of these
preconfigured partners, including their configurations, are provided in the supplementary materials.
After tutorial, they completed a warm-up writing task, in which they wrote a short essay of
approximately 300 words on the positive and negative aspects of AI in daily life. This task was
designed to familiarize participants with the probe before the diary study. During the warm-up task,
participants were asked to (1) create two custom thought partners and optionally enable or update
any preconfigured partners, and (2) complete the essay with their enabled partners to observe how
proactive suggestions were triggered and to practice key interaction features. After the warm-up
session, we provided instructions for the diary study.
Phase2: DiaryStudy(7days):Participantsbeganusingtheprobethefollowingdayforsevendays. To
capture how participants appropriate proactive thought partners in their own writing practices, we did
not constrain the genre, topic, or purpose of their writing. However, we asked participants to complete
at least four substantive writing sessions during the week to ensure sufficient exposure to the probe.
We defined asubstantive sessionas one that met two criteria: (1) at least 20 minutes of active writing or
production of at least 300 words; and (2) completion of a self-contained piece of writing, rather than
randomly connected sentences or artificial text written only for the study. To mitigate privacy risks
associatedwithsystemlogging, weexplicitlyinstructedparticipantsnottoenterpersonallyidentifiable
information, confidential workplace information, or other highly sensitive data into the probe.
Duringdeployment,theprobecollectedinteractionlogs,includingpartnerconfigurations,keystroke
logs, and user interactions with proactive suggestions. For each proactive intervention they received,
participants could optionally provide binary feedback by clicking a thumbs-up or thumbs-down icon
(Fig. 2B). In addition, participants submitted a structured diary entry at the end of each writing
session. The diary included three 10-point scales measuring satisfaction, perceived timeliness, and
perceived helpfulness of the proactive support, as well as four open-ended prompts asking about (1)
the partners they configured and why, (2) the proactive support they received and their feedback on
it, (3) challenges encountered while using the probe, and (4) any other observations. Together, these
data sources allowed us to triangulate automated system logs, immediate feedback on individual
interventions, and longer-form reflections on each writing session.
Phase 3: Semi-Structured Interview (60 minutes):In the final phase, participants first completed
the short-form Usability Metric for User Experience (UMUX-LITE) (Lewis et al., 2013). We then
conducted a semi-structured interview to probe participants’ week-long experiences and elicit their
visions for future proactive thought partners for writing. We began by asking participants to describe
their general experience using the probe during the week. We then asked them to compare the
proactive AI features in our probe with their experiences using reactive AI chatbots, such as ChatGPT
or Gemini, and proactive next-phrase suggestions, such as Smart Compose in Gmail (Chen et al.,
12

Designing Proactive Thought Partners for Writing
2019). Next, we used diary entries, binary feedback logs, and system logs as elicitation artifacts,
asking participants to elaborate on their strategies for configuring thought partners, specific instances
in which proactive suggestions were helpful or intrusive, and their rationales for how they chose to
engage with the proactive support they received. We also explored perceived benefits and challenges
of working with proactive thought partners, as well as participants’ perceived ownership and agency
during the writing process. Building on these reflections, we shifted the discussion beyond the
current prototype’s constraints and asked participants to articulate their ideal future proactive writing
assistants. The interview protocol is provided in the supplementary materials.
5.3. Analysis
We analyzed multiple sources of qualitative and quantitative data, including partner configurations, in-
teraction logs, diary entries, and semi-structured interview transcripts. The interaction logs were used
to characterize participants’ partner creation behaviors and engagement with proactive interventions,
while diary entries and interviews provided insight into participants’ rationales, experiences, and
perceptions. Two researchers conducted a thematic analysis of the qualitative data (Braun and Clarke,
2013). They reviewed the interview transcripts and diary entries to identify recurring concepts,
then met to compare, discuss, and consolidate the codes into a codebook. The researchers then
collaboratively grouped related codes into higher-level themes that addressed our research questions
through multiple rounds of discussion. Throughout the analysis, interaction logs and quantitative
usage metrics were used to triangulate and contextualize the qualitative findings.
6. Findings
In this section, we present findings related to our research questions. We first provide an overview of
participants’ use of the probe during the one-week deployment and their perceptions of its usability.
We then examine how participants created proactive thought partners to anticipate writing needs
(RQ1), how they engaged with proactive suggestions during writing (RQ2), and how they perceived
the customized, proactive cognitive support (RQ3).
6.1. Probe Usage and Usability
Across the 16 participants, we collected 66 writing sessions, excluding onboarding sessions. Partici-
pants completed an average of 4.13 (𝑆𝐷= 0.50) sessions each. Each session produced an average
of 390.34 (𝑆𝐷= 151.41) words and lasted an average of 17.09 (𝑆𝐷= 7.47) minutes. Participants
used the probe for a wide range of writing contexts. Based on the taxonomy from Lee et al. (2024),
these sessions included personal writing (𝑁= 19), academic writing (𝑁= 19), professional writing
(𝑁= 9), creative writing (𝑁= 8), technical writing (𝑁= 8), and journalistic writing (𝑁= 3). The
writing sessions completed by each participant are summarized in Table 1.
The System Usability Scale (SUS) scores calculated from UMUX-LITE collected during the exit
interviews averaged 82.81 (𝑆𝐷= 11.97). This score corresponds to the “Excellent” category defined
by Bangor et al. (2008, 2009), placing it in approximately the 90th-95th percentile. This is consistent
with daily survey measures of overall satisfaction, which averaged 8.16/10 (𝑆𝐷= 1.76). A linear
mixed-effectsmodelwithparticipantasarandomeffectshowedthatsatisfactionincreasedsignificantly
with session index (𝑏= 0.33,𝑆𝐸= 0.16, 𝑝=. 036), indicating that participants became progressively
more satisfied with the probe as they gained experience over the course of the deployment.
13

Designing Proactive Thought Partners for Writing
Table 2 | Examples of proactive thought partners created by participants.The examples illustrate
variation in partner roles and contextual heuristics, as well as participants’ frequent use of all three
event triggers. Triggers are abbreviated as P = Long Pause, E = Sentence End, and S = Text Selection.
Partners Roles Triggers Heuristics
Research Partner[Information Seeking]Provide examples
of similar research topics and findings
to augment my essay.
P / E / S[Writing-Activity &
Anticipated-Need]When I’m trying
to quote examples and trying to
back it up with broader facts.
India Partner[Information Seeking]Bring up
India-centric market scenarios that
drive pricing, including behavior of the
Indian customer across industries.
P / E / S[Draft-State & Writing-Activity]
When I talk about India as a country
and drill down into specific
scenarios.
Internal Monologue
Partner
[Ideation Support]Provides quotes for
what could be running through a
character’s head at certain moments
within the story.
P / E / S [Anticipated-Need]When it would be
helpful to know what the
protagonist is thinking.
Ethical partner[Critical Reflection]You’re a senior
ethical program manager. Defend the
ethical boundaries of ideas without
losing sights of values.
P / E / S[Draft-State]When there are cases
of challenging ethical issues when
using AI.
Synthesis Partner [Argument Development]Help integrate
positive and negative arguments into a
coherent conclusion.
P / E / S[Draft-State & Writing-Activity &
Anticipated-Need]When I have
presented both sides of the
argument, or will soon need to unify
my points.
Corporate Speak
Partner
[Textual Assistance]Up-level the
language to make it more professional
and integrate business speak.
E[Draft-State]When my language is
too casual and does not reference
business talk.
6.2. RQ1: Partner Creation
Participants created 54 partners, with an average of 3.38 (𝑆𝐷= 1.96) partners created per participant.
Among these, 35 (64.81%) were enabled in only one writing session, while 19 (35.19%) were used
across multiple sessions. Table 2 shows examples of these partners. We next examine the overarching
strategies participants used to create partners (KF1), the types of roles these partners took on (KF2),
and how participants configured their partners’ proactivity (KF3).
KF1: Creating partners by anticipating writing needs:Participants configured partners prospec-
tively, reasoning about what cognitive support they would need before writing began. This took two
forms. Ingoal-driven design, participants started from a mental image of the finished piece and
worked backward to infer the expertise it required. P04 described the approach directly: “I try to
envision what the end product would look like and then, if I had a human writer, I imagine what that per-
son’s expertise should be.” Indifficulty-driven design, participants instead began from self-knowledge
of their own recurring writing difficulties and designed partners to preemptively address those gaps.
P13 articulated this explicitly: “I knew myself well enough to know what potential blockers I would
have towards reaching that goal... where I anticipated myself struggling.” Both strategies required
participants to mentally simulate the writing task before it began: either from the perspective of the
intended output or from the perspective of their own likely difficulties.
KF2: Partner roles clustered around distinct forms of cognitive support:Participants configured
43 of 54 partners (79.63%) for higher-level cognitive support and 11 (20.37%) for localtextual assis-
14

Designing Proactive Thought Partners for Writing
tancesuch as language and style refinement. This pattern aligns with our expectation that proactive
thought partners would primarily support cognitive activities beyond phrasing and text production.
Specifically, 14 partners (25.93%) focused on seeking evidence or domain knowledge (information
seeking), 12 (22.22%) on argument development and reasoning (argument development), 10
(18.52%)onperspective-takingandcriticalreflection(criticalreflection), and7(12.96%)onideation
and creative development (ideation support). These roles show that participants envisioned proac-
tive partners as specialized sources of knowledge, reasoning support, reflective scaffolds, alternative
perspectives, and inspiration that could assist different forms of cognitive work during writing.
KF3: Partner proactivity is configured through broad event triggers and context-specific heuris-
tics.:We then analyzed how participants configured event triggers and contextual heuristics to
control partners’ proactivity. We found that event triggers were generally configured broadly: 31 of
54 partners (57.41%) were enabled with all three triggers. Specifically,pauseswere enabled for 40
of 54 partners (74.07%),sentence endingsfor 40 partners (74.07%), andtext selectionsfor 44
partners (81.48%). In contrast, participants used contextual heuristics to specify more particular
writing situations in which a partner’s support would be relevant. We identified three recurring
forms of contextual cues. First,draft-state cuesdescribed what was currently present in the text,
such as language being too casual, an argument presenting only one perspective, or the writing
becoming repetitive or boring 35/54 (64.81%). Second,writing-activity cuesdescribed what the
writer was currently doing in the writing process, such as introducing a concept, developing a claim,
analyzing an issue, or moving from listing arguments toward a conclusion 38/54 (70.37%). Third,
anticipated-need cuesdescribed the support the writer might need at that moment or next, such as
an example, another perspective, clarification of a concept, or a stronger argument 36/54 (66.67%).
Together, these patterns suggest a division of labor between the two timing mechanisms: event
triggers specifiedwhen the system should look, while contextual heuristics specifiedwhat it should look
forwhen determining whether and which partner should intervene. Participants viewed interaction
events as broader opportunities for support, while whether support was actually needed depended
on how those events were interpreted in relation to the writer’s evolving state and goals.
RQ1 Takeaway
Participants configured proactive thought partners through a form of prospective planning. They
anticipated the goals and difficulties of an upcoming writing task, translated these expectations into
specialized partner roles, and specified when those roles might become relevant. While event triggers
were configured broadly as candidate moments for intervention, contextual heuristics encoded more
specific expectations about the evolving draft, current writing activity, and anticipated support needs.
6.3. RQ2: Suggestion Engagement
The probe provided 1,100 proactive interventions across all participants and their writing sessions
(Table 3). Among these, participants opened 41.73% of the surfaced interventions (459/1,100).
Below, we first present our findings on how participants leveraged proactive suggestions in their
writing process (KF4). We then examine why they ignored many surfaced interventions (KF5) and
why, in some cases, they asked the AI to take over and execute edits directly in the document (KF6).
KF4: Suggestions supported both idea generation and self-monitoring:Participants described
using proactive suggestions primarily in two ways. First, suggestions were generative: they introduced
ideas, connections, or directions that writers had not reached on their own. The most memorable cases
involved unexpected connections that extended participants’ thinking. P12 described a suggestion
15

Designing Proactive Thought Partners for Writing
Table 3 | Distribution of engagement forms across trigger events.Each row describes interventions
surfaced by a trigger event and how participants engaged with them: whether they ignored the
intervention, used it as inspiration, or asked the partner to execute follow-up changes. Because
Executing required first opening the suggestion, Executing cases are coded only under Executing
rather than double-counted under Inspiring. Percentages are calculated within each row.
Trigger Events Engagement Forms Total
Ignoring Inspiring Executing
Pause425 (64.39%) 155 (23.48%) 80 (12.12%) 660
Sentence165 (55.93%) 45 (15.25%) 85 (28.81%) 295
Selection51 (35.17%) 15 (10.34%) 79 (54.48%) 145
Total641 (58.27%) 215 (19.55%) 244 (22.18%) 1,100
linking Buddhist and Abrahamic religious concepts as “an eye opener I hadn’t thought about it,” while
P01 recalled a suggestion connecting database behavior to memory leak debugging: “I never related
the database to memory leak...it just gave me some suggestion and then you know it became like a kind
of my idea right.”
Second, suggestions were regulatory: they helped writers assess whether their writing remained
aligned with their goals and arguments. P13 valued prompts that surfaced when they were “veering off
track,” and prompting them to reflect on whether their goal had changed. Others valued suggestions
that surfaced gaps or neglected perspectives. For P06, even a simple prompt such as “have you thought
about it” was useful because it prevented them from missing a potentially important point. Similarly,
P04 found that the partner helped reveal when they were “leaning on just one side of the coin” rather
than considering another point of view.
KF5: Ignoring preserved writing flow and occurred more often after pauses:Across all surfaced
interventions (Table 3), the most common response was to ignore the displayed tag and continue
writing without clicking to view the suggestion, accounting for 58.27% of interventions (641/1,100).
Participants described keep typing as a natural, low-cost behavior to dismiss the interventions. When
users already knew what to write next, they simply ignored the appeared interventions. As P13 noted,
“There are times I did not click on the little bubble thing and I was like, ‘No, I’m good.’” P05 similarly
characterized ignoring as part of the natural interaction rhythm: “if I have time I will read it, or if I think
I need it I will read it, and then it just helps in a more organic way.” Interventions surfaced after a pause
were especially likely to be ignored (64.39%), which echos the inherent ambiguity of event triggers: a
pause in typing can signal genuine cognitive need, but equally indicates focused concentration (P01).
KF6: Executing was selective and depended on readiness to externalize text:Executing repre-
sentedamorecommittedformofengagementandaccountedfor22.18%ofinterventions(244/1,100),
with 84.43% (206/244) of the generated text accepted. Interventions triggered by text selection were
more likely to lead to executing (54.48%) than those triggered by a pause (20.61%) or sentence
end (28.81%). Participants described letting the AI to write for them in three situations. First, they
sometimes used it out of curiosity, as a low-stakes way to preview how the AI might develop a direction
before deciding whether to write it themselves (P03). Second, when they already knew what they
wanted to say but struggled to phrase it, execution helped translate a clear intention into fluent text
(P04, P11, P12). Third, after an idea had been sufficiently developed through a short back-and-forth
with a partner, execution could become the natural final step of the interaction (P11).
Participants’ willingness to have the AI write for them also depended on the partner’s role and the
type of suggestion. For ideation-oriented partners, executing could serve as a useful shortcut once the
16

Designing Proactive Thought Partners for Writing
content or direction was sufficiently settled (P06, P11). In contrast, participants were more hesitant
to generate text from partners intended to provoke reflection, such as bias or rebuttal partners. P06
explained that when “just testing an idea... I’m not like rewriting anything, I’m just saying do I really
need this kind of stuff? So that is where I don’t really need help me write,” while P10 avoided execution
when further development would “deviate us too much from what... we just want one nudge and move
on from there.” Several participants further cautioned that making the AI write for users available for
every suggestion could encourage over-reliance and prematurely narrow the directions they might
otherwise explore (P03, P05, P11). For example, P05 deliberately avoided generating text when he
instead wanted to “guide it to write deeper” through further suggestions. He also argued thatnot
always offering the button could be beneficial because otherwise “we are prone to just maybe always
click it and actually it would limit the creativity... the human part of it.”
RQ2 Takeaway
Participants engaged with proactive suggestions through graduated levels of attention and control.
Ignoring was the most common response and used to preserve writing flow, especially after pauses.
When support was needed, writers opened suggestions and treated them as prompts for idea
generation and self-monitoring. Executing represented a more committed form of engagement and
was most appropriate when writers had a clear direction or sufficiently developed idea to externalize,
particularly after selecting text as a specific target for support; participants were more hesitant to
let the AI execute suggestions intended primarily to provoke reflection.
6.4. RQ3: User Experience
Participants’ overall impressions of this new form of customizable, proactive cognitive support were
positive. In the daily diary surveys, participants gave an average rating of 8.11/10 (𝑆𝐷= 1.87) for help-
fulnessand7.85/10( 𝑆𝐷= 1.86)fortimeliness. Wenextpresentinterviewfindingsonhowparticipants
perceivedsysteminitiative(KF7), howtheythoughtproactivecognitivesupportshouldbetimed(KF8),
and how they perceived the visual (KF9) and rhetorical (KF10) representations of proactive support.
KF7: Proactivity shifted support from pulling to pushing:Participants contrasted proactive support
with conventional chatbot interactions. Interacting with chatbots required writers to leave compo-
sition, formulate a prompt, wait for a response, and then re-enter the writing task; this was especially
difficult when writers did not yet know what help to request. As P08 put it, “sometimes it’s like I don’t
even know what question to ask.” P15 described chatbot interaction as a fragmented “spot” experience:
“working with Gemini, it’s kind of here’s a spot, there’s a spot, there’s a spot.” Proactive support, by
contrast, felt more continuous because partners could surface help from within the writing context;
P15 described it as “a kind of flow and then it’s a little bit like waves.” This shift came from the
context-aware “push mechanism” afforded by proactivity: as P10 explained, “it’s a push mechanism
rather than a pull mechanism... I don’t need to again click and put the information in a different thing
and ask. It’s sort of automated on what I want to ask since it’s a partner.”
KF8: Good timing depended on contextual alignment with writers’ momentary intentions:
Participants define a good timing as whether the assistance matched what they were trying to do
at that particular moment. They did not judge timing by whether a suggestion appeared after the
“right” interaction event but more by the alignment with their defined contextual heuristics. The
same observable event could correspond to different writing states and intentions. For example,
a pause could reflect being stuck and needing help, but it could also reflect developing an idea or
thinking through what to write next. P16 described a well-timed intervention as appearing when they
17

Designing Proactive Thought Partners for Writing
were thinking “this time I need a help,” while P12 described pauses caused by “brain fade or writer’s
block mid-sentence” as moments when a partner could help carry a thought forward. Similarly, P06
distinguished sentence endings as just textual boundaries and as moments when “I wrote a sentence,
I’m done with that, now I want to move on to the next one.” Poor timing occurred when this alignment
broke down, for example when the support did not match what the writer currently needed or when
a relevant partner remain silent when they should appear. P13 recalled one such missed opportunity:
“Oh, come on. That was a good time for one to like pop in.”
KF9: Peripheral and fading visual representations made proactive support feel non-intrusive:
Participants emphasized that the visual representation of proactive suggestions shaped whether
system initiative felt intrusive. Two design features were particularly important: peripheral place-
ment, through the right-side panel and small floating tags, and fading presence, through automatic
dismissal after periods of inaction. The right-side placement kept suggestions outside the main writing
workspace and made them easy to ignore when writers wanted to stay focused. P10 noted that
suggestions “come on the right tab and not on the main writing screen... they’re very small which means
that they don’t take up a lot of your space even on the right side.” P16 similarly explained, “it’s in the set
panel right so it’s not blocked my main... if it’s good then I look at that if not I just ignore.” The initial
floating tags further reduced disruption by signaling a suggestion without immediately expanding
its content. P13 valued that “it’s just a little icon and it’s not opening this whole box like out of here.”
The fading presence of suggestions further reinforced this optionality: when writers did not engage,
suggestions automatically disappeared rather than remaining in the workspace. As P12 put it, it was
“perfect because when I didn’t want them, it kind of disappeared.”
KF10: Acknowledgments built trust, while questions preserved sense of control:Participants
also reflected on how the rhetorical form of proactive suggestions shaped their experience. The
acknowledgment at the beginning of each suggestion often served a trust-building function by showing
that the partner had interpreted the current writing context before offering support. P12 described
this as a “same wavelength” signal: “that gives me the confidence that what it’s going to propose next
will be relevant... otherwise it could just be like a random suggestion.” P15 similarly noted that the
acknowledgment prompted a useful check on whether the partner had correctly understood their
intention. For writers with a clear sense of direction, however, this framing could feel unnecessary;
P07 remarked, “I know what I write; I just want to know what goes next.” Participants also generally
preferred the second part of the suggestion to be framed as a question rather than a directive because
questions preserved room for interpretation and choice. As P13 explained, “it’s a partner. it’s not telling
me what to do; it’s just offering me suggestions,” while P15 said that questions gave “the impression
that I have still everything under control and I can decide.” This framing was less effective when writers
lacked the knowledge needed to interpret the question. P08 described this as an “unknown unknowns”
problem: “You can tell me that I missed something, but you actually have to tell me what I missed because
the reason why I didn’t think about it is because I don’t know about it.” In such cases, participants often
continued the interaction by asking the partner for examples or additional options.
RQ3 Takeaway
Participants valued proactive cognitive support because it reduced the effort of explicitly seeking help
and allowed assistance to emerge within the flow of writing. However, system initiative was experi-
enced positively when the support aligned with writers’ momentary intentions and remained easy to
ignore or reject. Visual presentation and rhetorical framing all shaped this experience: peripheral
and fading visual cues reduced disruption, acknowledgments signaled contextual understanding,
and question-based suggestions preserved writers’ sense of control.
18

Designing Proactive Thought Partners for Writing
7. Discussion
In this paper, we explored proactive thought partners, a design concept that combines system initiative
with customizable, cognitive support for writing. Drawing on findings from our probe study, we
discuss design implications for future proactive writing support across four dimensions: customization,
timing, engagement, and representation (Table 4).
7.1. Designing Customization as Prospective Planning
Participants used customization to envision how proactive support could fit an upcoming writing
task (KF1). Configuration externalized a situated model of forthcoming writing work: the goals they
wanted to achieve, the difficulties they anticipated, and the kinds of cognitive support that might
become useful. This extends prior work on customizable AI agents for writing feedback (Benharrak
et al., 2024) after writing. In proactive writing contexts, however, writers needs to anticipate support
before and/or during writing. Future systems should therefore support this prospective planning
by helping writers translate anticipated goals and difficulties into specialized partners for different
forms of cognitive work, such as information seeking, argument development, critical reflection,
and ideation (DI1–DI2). Systems could help writers assemble a set of partners whose expertise and
responsibilities reflect the demands of a particular writing task.
At the same time, prospective planning is necessarily imperfect because writers may not know in
advance which configurations will be useful once writing unfolds. Future systems should therefore
treat partner configuration as an iterative design activity instead of a one-time setup step. Writers
could preview a partner’s likely interventions on a sample passage, simulate how its role and timing
conditions would behave in different writing situations, or revise configurations based on use. For
example, a system might surface patterns such as a partner being repeatedly ignored, rarely activated,
or frequently invoked for follow-up, and use these traces to suggest refinements to its role or scope.
Such mechanisms could make proactive partners easier to test and adapt while preserving writers’
authority over what kinds of cognitive support they want in their writing process.
7.2. Designing Timing as Contextual Alignment
Our findings show that observable interaction events should be treated as candidate moments for
proactive support, not as sufficient evidence that an intervention is needed (DI3). Participants
frequently configured pauses, sentence endings, and text selections as triggers, yet the same event
could correspond to different writing states (KF3,KF8). A pause might indicate writer’s block, focused
reflection, or a moment when the writer already knows what to write next; a sentence ending might
signal completion, extension, verification, or reconsideration. This distinction complements prior
work on interruption management (Bailey et al., 2001; Czerwinski et al., 2000; Iqbal et al., 2005) and
complicates proactive and autonomous writing systems that tie system action directly to predefined
events (Lehmann et al., 2026; Pu et al., 2025). For higher-level cognitive support, an event can
indicate when the system should assess the situation, but it does not by itself determine whether
support is appropriate.
Future proactive writing systems should therefore add a layer of contextual inference between
event detection and intervention (DI4). Our participants’ contextual heuristics drew on draft-state
cues, ongoing writing activities, and anticipated support needs, suggesting that systems should
interpret interaction events in relation to what is currently in the draft, what the writer appears to be
doing, and what kind of help may be useful next. Behavioral events such as pauses and selections
remain informative, but their meaning is shaped by the recursive interplay of planning, translating,
19

Designing Proactive Thought Partners for Writing
Table 4| Design dimensions, factors, and implications.This table summarizes the design dimensions of
proactive thought partners explored through our probe, the design factors examined in the study,
and the resulting implications for future customizable proactive writing support.
Design Dimension Design Factors Design Implications
Customization
Configuration Strategies:
goal-driven or difficulty-driven
planning.
[DI1]Support prospective planning by helping writers
anticipate the goals, difficulties, and forms of assistance
relevant to an upcoming writing task, and translate these
expectations into partner configurations.
Partner Functionality:
information seeking, argument
development, critical reflection,
and ideation support.
[DI2]Support specialized partners for distinct forms of
cognitive work rather than defaulting to general-purpose
assistants. Systems should make it easy to assemble partners
around the knowledge, reasoning, reflection, or ideation
support relevant to a particular writing task.
Timing
Event Triggers:long pause,
sentence end, and text selection.
[DI3]Treat observable interaction events as candidate
moments for intervention rather than sufficient evidence of
need. The same event may reflect different writing states, so
triggers should initiate further assessment rather than
directly determine system action.
Contextual Cues:draft-state
cues, writing-activity cues, and
anticipated-need cues.
[DI4]Infer intervention opportunities from multiple
contextual cues that capture what is present in the draft,
what the writer is currently doing, and what support they
may need next. Systems should align assistance with the
writer’s momentary intention before deciding whether and
which support to provide.
Engagement
Ignoring:users can naturally
ignore proactive interventions by
continuing to write.
[DI5]Make ignoring a first-class response to system
initiative. Proactive suggestions should be easy to bypass
without requiring explicit dismissal or disrupting the writing
flow.
Inspiring:users can inspect
suggestions and optionally
continue a dialogue.
[DI6]Provide low-commitment ways to use proactive
suggestions as material for thinking. Writers should be able
to inspect, question, elaborate, or adapt a suggestion
without immediately incorporating AI-generated text into
the draft.
Executing:writers can ask
partners to insert or revise text
directly.
[DI7]Reserve direct text generation for moments when
writers are ready to externalize a sufficiently settled
intention. Systems should allow writers to escalate from
cognitive support to execution when they have a clear
direction or target for revision, while avoiding making
execution the default for suggestions intended to provoke
reflection or exploration.
Representation
Visual Form:peripheral
placement and fading presence.
[DI8]Represent proactive suggestions as lightweight,
peripheral bids for attention. Suggestions should remain
noticeable without occupying the primary writing space and
should recede when writers choose not to engage.
Suggestion Framing:
acknowledgment of writer
intention and thought-provoking
questions.
[DI9]Make the system’s contextual interpretation visible
while preserving room for writer judgment. Brief
acknowledgments can communicate what the system
believes the writer is doing, while question-based
suggestions can invite reflection without prescribing a
particular response.
20

Designing Proactive Thought Partners for Writing
and reviewing in writing (Flower and Hayes, 1981). Systems could use triggers to initiate contextual
assessment, then combine recent writing behavior, local and document-level content, and writer-
defined goals to decide whether and which partner should intervene. They should also reassess this
interpretation close to delivery time, since a need inferred at one moment may no longer be relevant
after the writer has moved on.
7.3. Designing Engagement as Graduated Commitment
Participants engaged with proactive suggestions through distinct levels of attention and commitment:
ignoring them, opening them for inspiration or reflection, and selectively asking partners to execute
changes directly in the document. This finding speaks to recent concerns about agency and ownership
in AI co-writing. Prior work has shown that AI-generated text can complicate writers’ perceptions
of authorship (Draxler et al., 2024), while interaction designs can preserve agency by giving writers
meaningful control over how AI contributions enter a draft (Carrera et al., 2025; Yeh et al., 2025). In
our study, ignoring wasthe most common response and functioned as anatural way to preserve writing
flow when writers did not need help (KF5). Future systems should therefore make non-engagement
an effortless and legitimate response to system initiative, allowing writers to continue composing
without requiring explicit dismissal (DI5). When support was useful, participants opened suggestions
as prompts for idea generation and self-monitoring (KF4), suggesting that proactive assistance should
first offer low-commitment material that writers can inspect, question, or adapt without immediately
changing the draft (DI6).
Direct execution represented a deeper level of commitment and was most appropriate when
writers were ready to externalize a sufficiently settled intention, such as when they had a clear
direction or target for revision, or had developed an idea through interaction with a partner (KF6). At
the same time, participants often preferred not to execute suggestions intended primarily to provoke
reflection or exploration, where the suggestion itself could be sufficient. This suggests that proactive
systems should separate the initiation of support from the authority to modify the document and
treat execution as a selective escalation (DI7). A system may proactively surface an idea, question,
or possible revision, while direct insertion or rewriting should remain a deliberate user action. Future
interfaces could support smooth escalation across these levels, letting proactive AI take initiative
without assuming control over whether or how its contributions ultimately enter the draft.
7.4. Designing Representation as Lightweight and Non-directive
Participants valued proactive support when its visual and rhetorical representation made system
initiative feel optional and easy to assess (KF9–KF10). Peripheral placement, small floating tags, and
fading presence allowed suggestions to remain available without competing with the main writing
task, suggesting that proactive systems should present interventions as lightweight bids for attention
that can recede when writers choose not to engage (DI8). Rhetorical framing also shaped how writers
interpreted these interventions. Acknowledgments helped establish trust by making the system’s
understanding of the local context visible, while non-directive suggestions (i.e., questioning) preserved
room for interpretation and choice (DI9). Future systems should therefore communicate enough of
their contextual interpretation for writers to judge whether a suggestion is relevant, while avoiding
forms that make the intervention feel directive or demanding.
This finding aligns with work on interruption management showing that interruption costs depend
not only on timing but also on how an intervention is presented (Bailey et al., 2000; Czerwinski
et al., 2000; Pu et al., 2025). Future representations could make this grounding visible at multiple
levels of the document. Local interventions might reference the sentence or passage that motivated a
21

Designing Proactive Thought Partners for Writing
suggestion, while partners concerned with argument flow, section coherence, or narrative direction
could surface their interpretation of broader document structure through outlines, highlighted gaps,
or cross-section references. Such representations could help writers understand why a proactive
suggestion appeared while keeping the intervention lightweight and subordinate to the writing task.
8. Ethical Considerations
Proactive writing support raises privacy concerns because providing timely assistance requires contin-
uous observation of both the evolving document and the writer’s interaction traces. In our probe,
the system used the current draft, cursor position, behavioral events, and recent keystroke logs to
infer when support might be needed. Such data may expose sensitive content as well as distinctive
writing habits that could reveal aspects of a writer’s identity. Although we instructed participants not
to enter personally identifiable, confidential, or highly sensitive information, this mitigation places
responsibility on users and may be unrealistic in everyday writing contexts. Future systems should
therefore adopt privacy-by-design practices (Spiekermann, 2012), including data minimization, local
or ephemeral processing of behavioral traces, strict retention limits, clear disclosure of what is moni-
tored, and granular controls for pausing monitoring or deleting collected data. Proactive assistance
should also avoid treating inferred cognitive states as definitive and should not reuse writing traces
for model training, profiling, or identity inference without separate, explicit consent.
9. Limitations
Our study has several limitations. First, as a probe study, it was intended to explore an emerging
design space rather than evaluate a finished system. Accordingly, our findings do not establish causal
effects on writing quality, productivity, learning, or long-term agency. Longer deployments or a larger
scale of comparative, quantitative lab studies against reactive AI assistants and conventional writing
tools can be valuable in the future. A related limitation is that our study can only offer preliminary
insight into how proactive support may influence writers’ sense of ownership. Although participants
retained control over whether to ignore, check, or execute suggestions, proactive interventions may
still shape what writers notice, how they frame problems, and which directions they pursue. These
effects may become more consequential over longer periods of use, especially if writers begin to rely on
partners to identify writing problems or propose next steps. Future work could examine how proactive
support affects perceived authorship, confidence, skill development, and dependence over time.
Our participant sample may limit generalizability. Participants were English-proficient daily
writers who engaged with a range of writing genres during the study, and all had prior experience
with AI writing tools. This background allowed them to compare proactive support with existing
AI writing tools (e.g., chatbots, autocomplete) during interviews, but their expectations, comfort
with AI, and willingness to engage with proactive support may differ from those of writers with
less AI experience or different linguistic backgrounds. In addition, our privacy instruction to avoid
confidential workplace content likely excluded the high-stakes writing these participants do most.
Future work could address these limitations by evaluating proactive thought partners with a more
demographically and linguistically diverse participant population, including writers with varying
levels of AI experience, and across a broader range of professional and high-stakes writing contexts.
Our probe also has several limitations. First, current LLMs may not reliably interpret writing
context well enough to infer writers’ momentary intentions or anticipated support needs. Our findings
around contextual heuristics provide a starting point for future work by identifying three forms of
contextual cues that may be useful for this inference: draft-state cues, writing-activity cues, and
anticipated-need cues. Future research could develop models and benchmarks that evaluate whether
22

Designing Proactive Thought Partners for Writing
AI systems can recognize these cues, distinguish among different writing states that produce similar in-
teraction events, and determine which forms of support are appropriate in context. Second, suggestion
quality and timing depended on a particular LLM-based implementation. Different models, prompts,
contextual representations, or orchestration strategies may produce different intervention patterns
and user experiences. Our findings should therefore be interpreted as reflecting both the broader
interaction paradigm of proactive thought partners and the specific capabilities and limitations of
the system we implemented.
10. Conclusion
We introduced proactive thought partners, a design concept for AI writing assistants that proactively
provide customizable, higher-level cognitive support during writing. Through a one-week deployment
of our technology probe, we found that writers used customization as a form of prospective planning,
engaged with proactive suggestions through graduated levels of commitment, and experienced good
timing as contextual alignment between offered support and their momentary intentions. Our findings
further show that effective proactivity depends on more than deciding when to intervene: writers
need ways to shape the kinds of support they receive, ignore or deepen engagement with suggestions
as needed, and receive proactive support through non-intrusive visual and rhetorical representations.
We believe our design and insights can inform future proactive AI systems for complex cognitive work.
References
K. C. Arnold, K. Chauncey, and K. Z. Gajos. Predictive text encourages predictable writing. In
Proceedings of the 25th International Conference on Intelligent User Interfaces, IUI ’20, pages 128–138,
New York, NY, USA, Mar. 2020. Association for Computing Machinery. ISBN 978-1-4503-7118-6.
doi: 10.1145/3377325.3377523.
V. M. Baaijen, D. Galbraith, and K. de Glopper. Keystroke analysis: Reflections on procedures and
measures.Written Communication, 29(3):246–277, July 2012. ISSN 0741-0883. doi: 10.1177/
0741088312451108.
B. P. Bailey, J. A. Konstan, and J. V. Carlis. Measuring the effects of interruptions on task performance
in the user interface. InProceedings of the 2000 IEEE International Conference on Systems, Man, and
Cybernetics, volume 2, pages 757–762, Piscataway, NJ, 2000. IEEE. doi: 10.1109/ICSMC.2000.
885940.
B. P. Bailey, J. A. Konstan, and J. V. Carlis. The effects of interruptions on task performance, annoyance,
andanxietyintheuserinterface. InM.Hirose, editor,Human-ComputerInteraction: INTERACT2001
Conference Proceedings, pages 593–601, Amsterdam, 2001. IOS Press. ISBN 978-1-58603-188-6.
A. Bangor, P. T. Kortum, and J. T. Miller. An empirical evaluation of the system usability scale.
Int. J. Human–Computer Interact., 24(6):574–594, July 2008. ISSN 1044-7318. doi: 10.1080/
10447310802205776.
A. Bangor, P. Kortum, and J. Miller. Determining what individual sus scores mean: Adding an adjective
rating scale.J. Usability Stud., 4(3):114–123, May 2009. ISSN 1931-3357.
K. Barkaoui. What can l2 writers’ pausing behavior tell us about their l2 writing processes?Studies
in Second Language Acquisition, 41(3):529–554, July 2019. ISSN 0272-2631, 1470-1545. doi:
10.1017/S027226311900010X.
23

Designing Proactive Thought Partners for Writing
K. Benharrak, T. Zindulka, F. Lehmann, H. Heuer, and D. Buschek. Writer-defined ai personas
for on-demand feedback generation. InProceedings of the CHI Conference on Human Factors in
Computing Systems, pages 1–18, Honolulu HI USA, May 2024. ACM. ISBN 979-8-4007-0330-0. doi:
10.1145/3613904.3642406.
A. Bhat, S. Agashe, P. Oberoi, N. Mohile, R. Jangir, and A. Joshi. Interacting with next-phrase
suggestions: How suggestion systems aid and influence the cognitive processes of writing. In
Proceedings of the 28th International Conference on Intelligent User Interfaces, IUI ’23, pages 436–452,
New York, NY, USA, Mar. 2023. Association for Computing Machinery. ISBN 979-8-4007-0106-1.
doi: 10.1145/3581641.3584060.
R. Bixler and S. D’Mello. Detecting boredom and engagement during writing with keystroke analysis,
task appraisals, and stable traits. InProceedings of the 2013 International Conference on Intelligent
User Interfaces, IUI ’13, pages 225–234, New York, NY, USA, Mar. 2013. Association for Computing
Machinery. ISBN 978-1-4503-1965-2. doi: 10.1145/2449396.2449426.
V. Braun and V. Clarke.Successful Qualitative Research: A Practical Guide for Beginners. SAGE
Publications Ltd, Los Angeles London New Delhi, 2013. ISBN 978-1-84787-582-2.
D. Buschek, M. Zürn, and M. Eiband. The impact of multiple parallel phrase suggestions on email
input and composition behaviour of native and non-native english writers. InProceedings of
the 2021 CHI Conference on Human Factors in Computing Systems, CHI ’21, pages 1–13, New
York, NY, USA, May 2021. Association for Computing Machinery. ISBN 978-1-4503-8096-6. doi:
10.1145/3411764.3445372.
H. E. Byun and K. Cheverst. Harnessing context to support proactive behaviours. InProceedings of the
ECAI 2002 Workshop on AI in Mobile Systems (AIMS 2002), pages 50–57, Lyon, France, 2002. IOS
Press.
D. Carrera, J. Thomas-Mitchell, and D. Wigdor. Where do i ’add the egg’?: Exploring agency and
ownership in ai creative co-writing systems, Sept. 2025.
J. Chang and J. Chang. Writeahead2: Mining lexical grammar patterns for assisted writing. In
M. Gerber, C. Havasi, and F. Lacatusu, editors,Proceedings of the 2015 Conference of the North
American Chapter of the Association for Computational Linguistics: Demonstrations, pages 106–
110, Denver, Colorado, June 2015. Association for Computational Linguistics. doi: 10.3115/v1/
N15-3022.
M. X. Chen, B. N. Lee, G. Bansal, Y. Cao, S. Zhang, J. Lu, J. Tsay, Y. Wang, A. M. Dai, Z. Chen, T. Sohn,
and Y. Wu. Gmail smart compose: Real-time assisted writing. InProc. 25th ACM SIGKDD Int. Conf.
Knowl. Discov. Data Min., KDD ’19, pages 2287–2295, New York, NY, USA, July 2019. Association
for Computing Machinery. ISBN 978-1-4503-6201-6. doi: 10.1145/3292500.3330723.
V. Chen, A. Zhu, S. Zhao, H. Mozannar, D. Sontag, and A. Talwalkar. Need help? designing proactive
ai assistants for programming. InProceedings of the 2025 CHI Conference on Human Factors in
Computing Systems, CHI ’25, pages 1–18, New York, NY, USA, Apr. 2025a. Association for Computing
Machinery. ISBN 979-8-4007-1394-1. doi: 10.1145/3706598.3714002.
X. Chen, L. Tankelevitch, R. Vanukuru, A. E. Scott, P. Panda, and S. Rintel. Are we on track? ai-assisted
active and passive goal reflection during meetings. InProceedings of the 2025 CHI Conference on
HumanFactorsinComputingSystems,CHI’25,NewYork,NY,USA,2025b.AssociationforComputing
Machinery. ISBN 9798400713941. doi: 10.1145/3706598.3714052.
24

Designing Proactive Thought Partners for Writing
F. Chenu, F. Pellegrino, H. Jisa, and F. Michel. Interword and intraword pause threshold in writing.
Frontiers in Psychology, 5:182, Mar. 2014. doi: 10.3389/fpsyg.2014.00182.
J.-P. Chou, A. F. Siu, N. Lipka, R. Rossi, F. Dernoncourt, and M. Agrawala. Talestream: Supporting
story ideation with trope knowledge. InProceedings of the 36th Annual ACM Symposium on User
Interface Software and Technology, UIST ’23, pages 1–12, San Francisco CA USA, Oct. 2023. ACM.
ISBN 979-8-4007-0132-0. doi: 10.1145/3586183.3606807.
J. J. Y. Chung, W. Kim, K. M. Yoo, H. Lee, E. Adar, and M. Chang. Talebrush: Sketching stories
with generative pretrained language models. InProceedings of the 2022 CHI Conference on Human
Factors in Computing Systems, CHI ’22, pages 1–19, New York, NY, USA, Apr. 2022. Association for
Computing Machinery. ISBN 978-1-4503-9157-3. doi: 10.1145/3491102.3501819.
S. Chung, H. Jeon, S. Shin, and M. N. Hoque. Reading.help: Supporting efl readers with proactive
and on-demand explanation of english grammar and semantics, May 2025.
M. Czerwinski, E. Cutrell, and E. Horvitz. Instant messaging: Effects of relevance and timing. In
S. McDonald, Y. Waern, and G. Cockton, editors,People and Computers XIV—Usability or Else!:
Proceedings of HCI 2000, volume 2, pages 71–76, London, 2000. Springer. ISBN 978-1-85233-318-8.
A. K. Dey. Understanding and using context.Personal and Ubiquitous Computing, 5(1):4–7, Feb. 2001.
ISSN 1617-4909, 1617-4917. doi: 10.1007/s007790170019.
F. Draxler, A. Werner, F. Lehmann, M. Hoppe, A. Schmidt, D. Buschek, and R. Welsch. The ai
ghostwriter effect: When users do not perceive ownership of ai-generated text but self-declare as
authors.ACM Trans. Comput.-Hum. Interact., 31(2):25:1–25:40, Feb. 2024. ISSN 1073-0516. doi:
10.1145/3637875.
L. Flower and J. R. Hayes. A cognitive process theory of writing.College Composition & Communication,
32(4):365–387, Dec. 1981. ISSN 0010-096X, 1939-9006. doi: 10.58680/ccc198115885.
H. N. Fundal and Y. Bizzoni. Directional alignment and narrative agency in human-llm co-writing,
Apr. 2026.
D. Galbraith and V. M. Baaijen. Aligning keystrokes with cognitive processes in writing. In E. Lindgren
and K. P. H. Sullivan, editors,Observing Writing: Insights from Keystroke Logging and Handwriting,
volume 38 ofStudies in Writing, pages 306–325. Brill, Leiden, The Netherlands, 2019. ISBN
978-90-04-39252-6. doi: 10.1163/9789004392526_015.
K. I. Gero, V. Liu, and L. Chilton. Sparks: Inspiration for science writing using language models. In
Proceedings of the 2022 ACM Designing Interactive Systems Conference, DIS ’22, pages 1002–1019,
New York, NY, USA, June 2022. Association for Computing Machinery. ISBN 978-1-4503-9358-4.
doi: 10.1145/3532106.3533533.
Grammarly. Grammarly: Free ai writing assistance. https://www.grammarly.com/, 2025.
J. Ha, H. Jeon, D. Han, J. Seo, and C. Oh. Clochat: Understanding how people customize, interact,
and experience personas in large language models. InProc. 2024 CHI Conf. Hum. Factors Comput.
Syst., CHI ’24, pages 1–24, New York, NY, USA, May 2024. Association for Computing Machinery.
ISBN 979-8-4007-0330-0. doi: 10.1145/3613904.3642472.
E. Horvitz. Principles of mixed-initiative user interfaces. InProceedings of the SIGCHI Conference on
Human Factors in Computing Systems, CHI ’99, pages 159–166, New York, NY, USA, May 1999.
Association for Computing Machinery. ISBN 978-0-201-48559-2. doi: 10.1145/302979.303030.
25

Designing Proactive Thought Partners for Writing
C.-Y. Huang, S.-H. Huang, and T.-H. K. Huang. Heteroglossia: In-situ story ideation with the crowd. In
Proceedings of the 2020 CHI Conference on Human Factors in Computing Systems, CHI ’20, pages 1–12,
New York, NY, USA, Apr. 2020. Association for Computing Machinery. ISBN 978-1-4503-6708-0.
doi: 10.1145/3313831.3376715.
Y. Huang and A. Narechania. Facilitating proactive and reactive guidance for decision making on the
web: A design probe with webseek, Jan. 2026.
H. Hutchinson, W. Mackay, B. Westerlund, B. B. Bederson, A. Druin, C. Plaisant, M. Beaudouin-Lafon,
S. Conversy, H. Evans, H. Hansen, N. Roussel, and B. Eiderbäck. Technology probes: Inspiring
design for and with families. InProceedings of the SIGCHI Conference on Human Factors in Computing
Systems, CHI ’03, pages 17–24, New York, NY, USA, Apr. 2003. Association for Computing Machinery.
ISBN 978-1-58113-630-2. doi: 10.1145/642611.642616.
S. T. Iqbal, P. D. Adamczyk, X. S. Zheng, and B. P. Bailey. Towards an index of opportunity. In
Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, pages 311–320, New
York, NY, USA, Apr. 2005. Association for Computing Machinery. ISBN 978-1-58113-998-3. doi:
10.1145/1054972.1055016.
T. Ito, N. Yamashita, T. Kuribayashi, M. Hidaka, J. Suzuki, G. Gao, J. Jamieson, and K. Inui. Use
of an ai-powered rewriting support software in context with other tools: A study of non-native
english speakers. InProceedings of the 36th Annual ACM Symposium on User Interface Software
and Technology, UIST ’23, pages 1–13, New York, NY, USA, Oct. 2023. Association for Computing
Machinery. ISBN 979-8-4007-0132-0. doi: 10.1145/3586183.3606810.
M. Jakesch, A. Bhat, D. Buschek, L. Zalmanson, and M. Naaman. Co-writing with opinionated
language models affects users’ views. InProceedings of the 2023 CHI Conference on Human Factors in
Computing Systems, CHI ’23, pages 1–15, New York, NY, USA, Apr. 2023. Association for Computing
Machinery. ISBN 978-1-4503-9421-5. doi: 10.1145/3544548.3581196.
H. Kaur, H. Nori, S. Jenkins, R. Caruana, H. Wallach, and J. Wortman Vaughan. Interpreting Inter-
pretability: Understanding Data Scientists’ Use of Interpretability Tools for Machine Learning. In
Proceedings of the 2020 CHI Conference on Human Factors in Computing Systems, CHI ’20, pages 1–14,
New York, NY, USA, Apr. 2020. Association for Computing Machinery. ISBN 978-1-4503-6708-0.
doi: 10.1145/3313831.3376219.
M. Kreminski, M. Dickinson, M. Mateas, and N. Wardrip-Fruin. Why are we like this?: The ai
architecture of a co-creative storytelling game. InInt. Conf. Found. Digit. Games, FDG ’20, pages
1–4, Bugibba, Malta, Sept. 2020. ACM. ISBN 978-1-4503-8807-8. doi: 10.1145/3402942.3402953.
N. Kuo, A. Sergeyuk, V. Chen, and M. Izadi. Developer interaction patterns with proactive ai: A
five-day field study. InProceedings of the 31st International Conference on Intelligent User Interfaces,
IUI ’26, pages 349–362, New York, NY, USA, Mar. 2026. Association for Computing Machinery.
ISBN 979-8-4007-1984-4. doi: 10.1145/3742413.3789148.
V. Kuvar, N. Blanchard, A. Colby, L. Allen, and C. Mills. Automatically detecting task-unrelated
thoughts during conversations using keystroke analysis.User Model User-adapt Interact, 33(3):
617–641, 2023. ISSN 0924-1868. doi: 10.1007/s11257-022-09340-z.
M. S. Lam, O. Shaikh, H. Xu, A. Guo, D. Yang, J. Heer, J. A. Landay, and M. S. Bernstein. Just-in-time
objectives: A general approach for specialized ai interactions, Oct. 2025.
26

Designing Proactive Thought Partners for Writing
M. Lee, K. I. Gero, J. J. Y. Chung, S. B. Shum, V. Raheja, H. Shen, S. Venugopalan, T. Wambsganss,
D. Zhou, E. A. Alghamdi, T. August, A. Bhat, M. Z. Choksi, S. Dutta, J. L. Guo, M. N. Hoque, Y. Kim,
S. Knight, S. P. Neshaei, A. Shibani, D. Shrivastava, L. Shroff, A. Sergeyuk, J. Stark, S. Sterman,
S. Wang, A. Bosselut, D. Buschek, J. C. Chang, S. Chen, M. Kreminski, J. Park, R. Pea, E. H. R. Rho,
Z. Shen, and P. Siangliulue. A design space for intelligent and interactive writing assistants. In
Proceedings of the 2024 CHI Conference on Human Factors in Computing Systems, CHI ’24, pages 1–35,
New York, NY, USA, May 2024. Association for Computing Machinery. ISBN 979-8-4007-0330-0.
doi: 10.1145/3613904.3642697.
Y. Lee, T. S. Kim, M. Chang, and J. Kim. Interactive children’s story rewriting through parent-children
interaction. InProceedings of the First Workshop on Intelligent and Interactive Writing Assistants
(In2Writing 2022), pages 62–71, Dublin, Ireland, 2022. Association for Computational Linguistics.
doi: 10.18653/v1/2022.in2writing-1.9.
F. Lehmann, K. Shauchenka, and D. Buschek. Collaborative document editing with multiple users
and ai agents, Feb. 2026.
J. R. Lewis, B. S. Utesch, and D. E. Maher. Umux-lite: When there’s no time for the sus. InProceedings
of the SIGCHI Conference on Human Factors in Computing Systems, CHI ’13, pages 2099–2102, New
York, NY, USA, Apr. 2013. Association for Computing Machinery. ISBN 978-1-4503-1899-0. doi:
10.1145/2470654.2481287.
A. Liu, Y. Karoui, F. Draxler, F. Kreuter, and F. Chiossi. Sensing what surveys miss: Understanding
and personalizing proactive llm support by user modeling, Jan. 2026a.
Y. Liu, J. Gallagher, S. Sterman, and T. August. From crafting text to crafting thought: Grounding ai
writing support to writing center pedagogy. InProc. 2026 CHI Conf. Hum. Factors Comput. Syst.,
pages 1–36, Barcelona Spain, Apr. 2026b. ACM. ISBN 979-8-4007-2278-3. doi: 10.1145/3772318.
3790292.
Y. Liu, V. N. Shah, S. Suh, P. Siangliulue, T. August, and Y. Huang. Perspectra: Choosing your experts
enhances critical thinking in multi-agent research ideation. InProc. 2026 CHI Conf. Hum. Factors
Comput. Syst., pages 1–27, Barcelona Spain, Apr. 2026c. ACM. ISBN 979-8-4007-2278-3. doi:
10.1145/3772318.3791560.
Y. Lu, C. Zhang, Y. Yang, Y. Yao, and T. J.-J. Li. From awareness to action: Exploring end-user
empowerment interventions for dark patterns in ux.Proc. ACM Hum.-Comput. Interact., 8(CSCW1):
59:1–59:41, Apr. 2024. doi: 10.1145/3637336.
Y. Luo, A. Caetano, A. A. Nargund, T. Höllerer, and M. Sra. How users perceive mixed-initiative ai:
Attitudes toward assistance in problem solving, Feb. 2026.
S. Maier, M. Schneider, and S. Feuerriegel. Partnering with generative ai: Experimental evaluation
of model-led and human-led interaction in human-ai co-creation. InProceedings of the 2026 CHI
Conference on Human Factors in Computing Systems, CHI ’26, New York, NY, USA, 2026. Association
for Computing Machinery. ISBN 9798400722783. doi: 10.1145/3772318.3791185.
D. Masson, Y.-H. Kim, and F. Chevalier. Textoshop: Interactions inspired by drawing software to
facilitate text editing. InProceedings of the 2025 CHI Conference on Human Factors in Computing
Systems, pages 1–14, Yokohama Japan, Apr. 2025. ACM. ISBN 979-8-4007-1394-1. doi: 10.1145/
3706598.3713862.
A. Matsuhashi. Pausing and planning: The tempo of written discourse production.Research in the
Teaching of English, 15(2):113–134, 1981. ISSN 0034-527X.
27

Designing Proactive Thought Partners for Writing
S. Medimorec and E. F. Risko. Pauses in written composition: On the importance of where writers
pause.Read Writ, 30(6):1267–1285, June 2017. ISSN 0922-4777, 1573-0905. doi: 10.1007/
s11145-017-9723-7.
Y. Miyata and D. A. Norman. The control of multiple activities. In D. A. Norman and S. W. Draper,
editors,User Centered System Design: New Perspectives on Human-Computer Interaction. Lawrence
Erlbaum Associates, Hillsdale, NJ, 1986. ISBN 978-0-89859-872-8.
A. Mukhopadhyay, K. Salubre, H. Javed, S. Mehrotra, and K. Akash. Exploring the impact of proactive
generative ai agent roles in time-sensitive collaborative problem-solving tasks, Feb. 2026.
D. Nam, A. Macvean, V. Hellendoorn, B. Vasilescu, and B. Myers. Using an llm to help with code
understanding, Jan. 2024.
D. J. Nicol and D. Macfarlane-Dick. Formative assessment and self-regulated learning: A model and
seven principles of good feedback practice.Studies in Higher Education, 31(2):199–218, Apr. 2006.
ISSN 0307-5079. doi: 10.1080/03075070600572090.
T. Prasongpongchai, P. Pataranutaporn, M. Lertsutthiwong, and P. Maes. Talk to the hand: An
llm-powered chatbot with visual pointer as proactive companion for on-screen tasks. InProceedings
of the 2025 CHI Conference on Human Factors in Computing Systems, CHI ’25, pages 1–16, New
York, NY, USA, Apr. 2025. Association for Computing Machinery. ISBN 979-8-4007-1394-1. doi:
10.1145/3706598.3715579.
K. Pu, D. Lazaro, I. Arawjo, H. Xia, Z. Xiao, T. Grossman, and Y. Chen. Assistance or disruption?
exploring and evaluating the design and trade-offs of proactive ai programming support. In
Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems, CHI ’25, pages 1–
21, New York, NY, USA, Apr. 2025. Association for Computing Machinery. ISBN 979-8-4007-1394-1.
doi: 10.1145/3706598.3713357.
K. Quan, D. Albassam, M. Wu, Z. Ding, and J. Chin. Towards ai as colleagues: Multi-agent system
improves structured ideation processes. InProc. 2026 CHI Conf. Hum. Factors Comput. Syst.,
ACM Conferences, pages 1–26, Barcelona Spain, Apr. 2026. ACM. ISBN 979-8-4007-2278-3. doi:
10.1145/3772318.3790375.
M. Reza, N. Laundry, I. Musabirov, P. Dushniku, Z. Y. M. Yu, K. Mittal, T. Grossman, M. Liut,
A. Kuzminykh, and J. J. Williams. Abscribe: Rapid exploration of multiple writing variations
in human-ai co-writing tasks using large language models, Oct. 2023.
J. Schilperoord. It’s about time: Temporal aspects of cognitive processes in text production. InIt’s
about Time. Brill, Leiden, The Netherlands, Mar. 2022. ISBN 978-90-04-45859-8.
W. Seymour, M. J. Kraemer, R. Binns, and M. Van Kleek. Informing the Design of Privacy-Empowering
Tools for the Connected Home. InProceedings of the 2020 CHI Conference on Human Factors in
Computing Systems, CHI ’20, pages 1–14, New York, NY, USA, Apr. 2020. Association for Computing
Machinery. ISBN 978-1-4503-6708-0. doi: 10.1145/3313831.3376264.
H. Shen, C.-Y. Huang, T. Wu, and T.-H. K. Huang. Convxai : Delivering heterogeneous ai explanations
via conversations to support human-ai scientific writing. InCompanion Publication of the 2023
Conference on Computer Supported Cooperative Work and Social Computing, CSCW ’23 Companion,
pages 384–387, New York, NY, USA, Oct. 2023. Association for Computing Machinery. ISBN
979-8-4007-0129-0. doi: 10.1145/3584931.3607492.
28

Designing Proactive Thought Partners for Writing
P. Siangliulue, J. Bragg, D. Downey, J. C. Chang, and D. S. Weld. Omakase: Proactive assistance with
actionable suggestions for evolving scientific research projects, Apr. 2026.
M. N. Siddiqui, R. D. Pea, and H. Subramonyam. Script&shift: A layered interface paradigm for
integrating content development and rhetorical strategy with llm writing assistants. InProceedings
of the 2025 CHI Conference on Human Factors in Computing Systems, CHI ’25, pages 1–19, New
York, NY, USA, Apr. 2025. Association for Computing Machinery. ISBN 979-8-4007-1394-1. doi:
10.1145/3706598.3714119.
N. Sommers. Responding to student writing.College Composition & Communication, 33(2):148–156,
May 1982. ISSN 0010-096X, 1939-9006. doi: 10.58680/ccc198215854.
K. Son, H. Lee, D. Choi, Y. Kim, T. S. Kim, Y. Lee, J. J. Y. Chung, H. Jung, and J. Kim. "when to hand
off, when to work together": Expanding human-agent co-creative collaboration through concurrent
interaction, Mar. 2026.
S. Spiekermann. The challenges of privacy by design.Commun. ACM, 55(7):38–40, July 2012. ISSN
0001-0782. doi: 10.1145/2209249.2209263.
L. Sun, S. Tao, J. Hu, and S. P. Dow. Metawriter: Exploring the potential and perils of ai writing
support in scientific peer review.Proc. ACM Hum.-Comput. Interact., 8(CSCW1):94:1–94:32, Apr.
2024. doi: 10.1145/3637371.
Y. Tian, S. Crossley, and L. V. Waes. The klicke corpus: Keystroke logging in compositions for
knowledge evaluation.Journal of Writing Research, 17(1):23–60, June 2025. ISSN 2294-3307. doi:
10.17239/jowr-2025.17.01.02.
C.-T. Tsai, J.-J. Chen, C.-Y. Yang, and J. S. Chang. Lingglewrite: A coaching system for essay writing. In
A. Celikyilmaz and T.-H. Wen, editors,Proceedings of the 58th Annual Meeting of the Association for
Computational Linguistics: System Demonstrations, pages 127–133, Online, July 2020. Association
for Computational Linguistics. doi: 10.18653/v1/2020.acl-demos.17.
Q. Wan, S. Hu, Y. Zhang, P. Wang, B. Wen, and Z. Lu. "it felt like having a second mind": Investigating
human-ai co-creativity in prewriting with large language models, Aug. 2023.
Q. Wan, J. Li, H. Wang, and Z. Lu. Polymind: Parallel visual diagramming with large language models
to support prewriting through microtasks, Feb. 2025.
C. Yeh, G. Ramos, R. Ng, A. Huntington, and R. Banks. Ghostwriter: Augmenting collaborative
human-ai writing experiences through personalization and agency, July 2025.
Y. Yin, M. Wu, R. Huang, X. Tong, J. Zhou, C. Yu, and Y. Shi. Proactive ai as a catalyst for creativity?
balancing human agency and ai contribution in collaborative story writing. InProc. 2026 CHI Conf.
Hum. Factors Comput. Syst., ACM Conferences, pages 1–16, Barcelona Spain, Apr. 2026. ACM. ISBN
979-8-4007-2278-3. doi: 10.1145/3772318.3790848.
A. Yuan, A. Coenen, E. Reif, and D. Ippolito. Wordcraft: Story writing with large language models. In
27th International Conference on Intelligent User Interfaces, IUI ’22, pages 841–852, New York, NY,
USA, Mar. 2022. Association for Computing Machinery. ISBN 978-1-4503-9144-3. doi: 10.1145/
3490099.3511105.
C. Zhang and A. Davis. Narrative keyframing for generative creative writing, Aug. 2026.
29

Designing Proactive Thought Partners for Writing
C. Zhang, K. Ju, P. Bidoshi, Y.-C. G. Yen, and J. M. Rzeszotarski. Friction: Deciphering writing feedback
into writing revisions through llm-assisted reflection. InProceedings of the 2025 CHI Conference
on Human Factors in Computing Systems, CHI ’25, pages 1–27, New York, NY, USA, Apr. 2025a.
Association for Computing Machinery. ISBN 979-8-4007-1394-1. doi: 10.1145/3706598.3714316.
C. Zhang, K. Ju, Z. Han, Y.-C. G. Yen, and J. M. Rzeszotarski. Synthia: Visually interpreting and
synthesizing feedback for writing revision. InProceedings of the 38th Annual ACM Symposium on
User Interface Software and Technology, UIST ’25, pages 1–16, New York, NY, USA, Sept. 2025b.
Association for Computing Machinery. ISBN 979-8-4007-2037-6. doi: 10.1145/3746059.3747703.
C. Zhang, S. Guo, A. Davis, and E. Koh. Narrix: Remixing narrative strategies from examples for story
writing. InProceedings of the 2026 CHI Conference on Human Factors in Computing Systems, pages 1–
24, Barcelona Spain, Apr. 2026a. ACM. ISBN 979-8-4007-2278-3. doi: 10.1145/3772318.3790813.
C. Zhang, Y. Liu, L. Nie, J. M. Rzeszotarski, Y. Huang, and T. August. From words to widgets for
controllable llm generation, Aug. 2026b.
Z. Zhang, J. Gao, R. S. Dhaliwal, and T. J.-J. Li. Visar: A human-ai argumentative writing assistant with
visual programming and rapid draft prototyping. InProceedings of the 36th Annual ACM Symposium
on User Interface Software and Technology, UIST ’23, pages 1–30, New York, NY, USA, Oct. 2023.
Association for Computing Machinery. ISBN 9798400701320. doi: 10.1145/3586183.3606800.
X. Zheng, Z. Li, X. Gui, and Y. Luo. Customizing emotional support: How do individuals construct and
interact with llm-powered chatbots. InProceedings of the 2025 CHI Conference on Human Factors in
Computing Systems, CHI ’25, pages 1–20, New York, NY, USA, Apr. 2025. Association for Computing
Machinery. ISBN 979-8-4007-1394-1. doi: 10.1145/3706598.3713453.
S. Zhou, D. N. R. Rodriguez, P. Remior, J. Frangi, L. Li, R. Ma, J. G. Johnson, C. Lisetti, and C. Chen.
Exploringneedsanddesignopportunitiesforproactiveinformationsupportinin-personsmall-group
conversations, Jan. 2026.
30
