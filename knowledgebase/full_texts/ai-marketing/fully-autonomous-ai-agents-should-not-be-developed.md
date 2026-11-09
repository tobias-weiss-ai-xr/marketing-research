---
title: Fully Autonomous AI Agents Should Not be Developed
url: https://arxiv.org/abs/2502.02649
category: ai-marketing
subcategory: empirical
date: 2025-02
venue: ''
authors:
- Margaret Mitchell
- Avijit Ghosh
- Alexandra Sasha Luccioni
- Giada Pistilli
source: arxiv
pdf_url: https://arxiv.org/pdf/2502.02649
pages: 29
chars: 122144
fetched_at: '2026-11-08T13:16:04+00:00'
kb_version: 1
---

# Fully Autonomous AI Agents Should Not be Developed

Fully Autonomous AI Agents Should Not be Developed
Margaret Mitchell Avijit Ghosh Alexandra Sasha Luccioni Giada Pistilli
Hugging Face
{meg,avijit,sasha.luccioni,giada}@hf.co
Abstract
We argue thatfully autonomous AI agents
should not be developed. In support of this
position, we build from prior scientific literature
and current product marketing to detail the ethical
values at play in the use of AI agents, documenting
trade-offs in potential benefits and risks. Our
analysis reveals that risks to people increase with
the autonomy of a system: The more control a user
cedes to an AI agent, the more risks to people arise.
Particularly concerning are risks associated with
the most extreme form offull autonomy, where
the lack of human constraints leads to severe risks
impacting multiple human values.
1. Introduction
The sudden, rapid advancement of Large Language Model
(LLM) capabilities – from writing fluent sentences to
achieving increasingly high accuracy on benchmark datasets
– has led AI developers and businesses alike to look towards
what comes next. The tail end of 2024 saw “AI agents”,
autonomous goal-directed systems, begin to be motivated
and deployed as the next big advancement in AI technology.1
Many recent AI agents are constructed by integrating LLMs
into larger, multi-functional systems, capable of carrying out
a variety of tasks to achieve goals. A foundational premise
of this emerging paradigm is that computer programs need
not be constrained to actions explicitly defined by a human
operator; rather, systems can autonomously combine and
execute multiple tasks without direct human involvement.
This transition marks a fundamental shift towards systems
capable of creating context-specific plans in previously
unspecified environments.
To provide conceptual clarity on the benefits and risks of this
powerful technology, we review recent AI agent products
and research along two primary dimensions:
1. What it means for something to be an “AI agent”.
2. Ethical considerations of increased autonomy.
1A selection of examples is provided in Section H.
Our review suggests that AI agents may be understood
on a sliding scale of autonomy, where risks outweigh
benefits for systems at the upper end (full autonomy). This
research complements previous work motivating the need
to anticipate risks in agent behavior (Chan et al., 2023),
providing a value-based characterization of AI agent risks
as well as benefits as their autonomy is increased. Partic-
ularly concerning are safety risks (Section 5.3.8) – which
include loss of human life – and privacy and security risks
(Section 5.3.7, Section 5.3.9). Compounding these issues is
the risk of misplaced trust (Section 5.3.10), which enables a
cascade of further harms. For example, “hijacking”, wherein
an agent is instructed by a malicious third party to exfiltrate
confidential information, can propagate and multiply harms
as the stolen information is used to compromise a user’s
public reputation, financial stability, or to identify additional
people as targets of attack (U.S. AI Safety Institute, 2025).
Given the foreseeable benefits and risks, we arguefully
autonomousAI agents – and in particular the most advanced
form of this, where systems are capable of writing and
executing their own code beyond predefined constraints –
should not be developed. Even with constraints defined,
complete freedom for code creation and execution enables
the potential to override human control, realizing some
of the worst harms described in Section 5. In contrast,
semi-autonomoussystems, which retain some level of
human control, offer a more favorable risk-benefit profile,
depending on the degree of autonomy, the complexity of
tasks assigned, and the nature of human involvement.
2. Background
2.1. A Brief History of Artificial Agents
The idea of humans being assisted by artificial autonomous
systems can be found throughout human history. Ancient
mythology describes Cadmus (ca. 2000 BCE), who planted
dragon teeth that turned into soldiers. Aristotle (ca. 350
BCE) speculated that automata could replace human slavery:
“There is only one condition in which we can imagine
managers not needing subordinates, and masters not needing
slaves. This condition would be thateach instrument could
do its own work, at the word of command or by intelligent
1
arXiv:2502.02649v3  [cs.AI]  20 Oct 2025

anticipation” (Aristotle, 1999). An early precursor to arti-
ficial agents was created by Ctesibius of Alexandria (ca. 300
BCE), who created an artificial automatic self-regulatory
system: A water clock that that maintained a constant flow
rate (Pollio, 1914). This demonstrated that it was possible
to create a system that could modify its own behavior in
response to changes in its environment, previously believed
to be limited to living things (Russell & Norvig, 2020).
More recently, writing on autonomous systems in the form
of automata highlights the kinds of risks we discuss here.
The famous “Three Laws of Robotics” (Asimov, 1942) state:
1. A robot may not injure a human being or, through inaction,
allow a human being to come to harm.
2. A robot must obey the orders given it by human beings
except where such orders would conflict with the First Law.
3. A robot must protect its own existence as long as such
protection does not conflict with the First or Second Law.
The way such concepts concretely translated to computer
software remained elusive until the late 1900s, when
advances in hardware and computer functionality catalyzed
excitement on AI agents as an imminent breakthrough
(Sargent, 1992; Guilfoyle & Warner, 1994; Wooldridge
& Jennings, 1995; Nwana & Ndumu, 1999). A particular
form of AI agent became extensively used in reinforcement
learning because it enabled the implementation of separate
goals and objective functions for independent actors within
the same action space (Tan, 1993; Littman, 1994), which
allowed the development of new methods and approaches
for exploration and optimization (Busoniu et al., 2008).
2.2. Current Landscape of Agentic Systems
Over the past few years, work on AI agents has broadened
the range of functionality that computer systems can provide
while requiring less input from users. Notably, the rapid
increase in the deployment and usage of LLM-based systems
has been followed by concentrated work on AI agents that
leverage these systems, with minimal lag time between
research developments and product release. Systems can now
complete tasks that previously required human interaction
with multiple different people and programs, e.g., organizing
meetings2 or creating personalized social media posts. 3
(Further example applications are provided in Section G.)
In the physical world, there have also been significant
advances in embodied autonomous AI systems. Autonomous
vehicles represent one of the more visible applications, 4
with systems capable of perceiving5 their environment and
navigating without human input (Van Brummelen et al.,
2018). The development of autonomous robots has similarly
2E.g., Lindy, Zapier, NinjaTech, Attri
3E.g., HubSpot
4E.g., Waymo (Hawkins, 2025)
5With digital sensors, distinct from human perception
expanded, with advancements in “general” autonomous
robots (Brohan et al., 2023) as well as domain-specific appli-
cations such as industrial manufacturing (M¨uller et al., 2021)
and healthcare (Haidegger, 2019), among others. LLMs,
which underlie many recent digital AI systems (discussed
further in Section 3), are increasingly being integrated into
embodied systems to advance system autonomy, used to
generate tasks (Ahn et al., 2024), aid in decision-making
(Cui et al., 2024b), provide interpretability (Xu et al., 2024;
Cai et al., 2025) and assist with planning (Cui et al., 2024a).
Perhaps most controversially, autonomous weapons systems
are a dedicated area of development (Etzioni & Etzioni,
2017; Longpre et al., 2022). 6 These systems, capable of
engaging targets without full human control, raise significant
ethical questions about accountabilityand safety that extend
beyond those of purely digital agents (Cummings, 2017;
Chavannes et al., 2020; Bloch et al., 2020; Schwarz, 2021;
Gaeta, 2023; Simmons-Edler et al., 2024). Harms of human
goal misalignment may be further compounded when human
control is ceded (Kierans et al., 2025).
3. Definitions
3.1. On AI Agents
Analyzing potential benefits and risks of AI agents requires
understanding what an AI agent is, yet definitions and
descriptions vary greatly (see Section B), and the term
“agent” is currently used in the technology sector for products
ranging from single-step prompt-and-response systems 7
to multi-step customer support systems.8 Notably, several
recent definitions assert the use of LLMs, a specification we
do not adopt (further discussed in Section A).
A commonality across AI agent descriptions is that they act
with some level ofautonomy: given a high-level goal and an
environment in which it can be pursued, AI agents can iden-
tify steps toward the goal without direct human instruction.
(Huang et al., 2022; Yao et al., 2022; Pan et al., 2024; World
Economic Forum, 2024). For example, an ideal AI agent
could respond to a high-level request such as “help me write a
great paper about AI agents” by independently breaking this
task down into steps for retrieving highly-cited academic pa-
pers about AI agents from the internet and creating an outline
informed by the content it retrieved. In work on the related
concept of Artificial General Intelligence (AGI), proposed
trajectories of increased autonomy stipulate that AI agents oc-
cupy a single level, where they are fully autonomous (Morris
et al., 2024) or simply (semi-)autonomous (Metz, 2024).
6Also see documenting news articles, e.g., Meaker (2023); Vincent
(2024); Everett (2025); Field (2025); Robins-Early (2024).
7E.g., Spataro (2024)
8E.g., as described by Lindy in their AI Customer Support page.
2

Agentic Level Description Term Example Code Who’s in Control?
✩✩✩✩ Model has no impact on program flow Simple processor print llm output(llm response) /userHuman
★✩✩✩ Model determines basic program flow Router if llm decision(): path a() else: path b() /userHow functions are done; ♂robotWhen
★★✩✩ Model determines how functions are executed Tool caller run function(llm chosen tool, llm chosen args) /userWhat functions are done; ♂robotHow
★★★✩ Model controls iteration and program continuation Multi-step agent while should continue(): execute next step() /userWhat functions exist; ♂robotWhich to do, when, how
★★★★ Model creates & executes new code Fully autonomous agent create code(user request); execute() ♂robotSystem
Table 1.Levels of AI Agent: Different systems can be characterized along a spectrum of autonomy, with levels marking significant changes
in ability and control. They can also be combined in “multiagent systems,” where one agent workflow triggers another, or where multiple
agents work collectively toward a goal. Levels adapted from (Roucher et al., 2024).
Lacking a crisp single consensus definition on what an AI
agent is, we propose the followingworking definitionas a
grounding for the text to follow, designing the definition
to be as precise as possible without relying on vague or
anthropomorphized language, yet general enough to apply
to the rich diversity of systems referred to as “AI agents”:
Computer software systems capable of creating
context-specific plans in non-deterministic environments.
Section A further unpacks the meaning of this definition.
Recently introduced AI agents are built on ML models,
many specifically using LLMs to drive their actions, which
is a relatively new approach for computer software execu-
tion. Aside from this difference, today’s AI agents share
similarities with those described in the past and, in some
cases, realize previous ideas of what agents might be like
(Wooldridge & Jennings, 1995): taking steps autonomously,
navigating social expectations, and appropriately balancing
reactive and proactive actions.
3.2. On Agency
The concept of “agency” is central to debates about
autonomous AI systems, yet its meaning and implications
remain philosophically contested. In general terms, anagent
is understood as an entity with capacity to act (Anscombe,
1957; Davidson, 1963). Applying this concept to artificial
systems raises questions about the nature of those acts’
intentionality: the philosophical literature commonly
understands agency through the lens of intentional action,
where actions are explained in terms of the agent’s mental
states (e.g., beliefs, desires) and their capacity to act for
reasons (Davidson, 1963; Goldman, 1970), but artificially
intelligent agents are not known to have mental states as
historically discussed. This suggests that AI agents lack the
fundamental characteristics of genuine agency (Frankfurt,
1971; Bratman, 1987; Velleman, 1992). This has two primary
ramifications for this work: (1) the increased risk we note
with increasing agentic levels is not counter-balanced by
common philosophical underpinnings that might motivate
the benefits of agency; (2) we contextualize AI agents
using the concept of “autonomy”, and center the concept of
“agent”, rather than agency, in recognizingagenticlevels.
4. AI Agent Levels
AI agents may be said to be more or less autonomous (or
agentic) along a sliding scale. Most writing on AI agents
does not make such a distinction, which has contributed to
recent confusion in both technical and public discourse about
what AI agents are and what they are capable of (Lambert,
2024). Addressing this issue, a proposal of different
gradations of “AI agent” has recently been put forward by
multiple researchers (e.g., Kapoor et al. (2024); Ng (2024);
Greyling (2024); Lambert (2024); Roucher et al. (2024),
without consensus on the specifics of each level. Drawing
from these ideas and descriptions of AI agents, we propose
the leveled AI agent scale in Table 1, highlighting technical
implementation details and the distribution of control.9
Our proposed agentic levels correspond to decreasing human
influence: A reduction of explicit instructions from users and
system-specific programming from developers. Conversely,
AI agents have more control over how they operate and
what they can do. This is a critical aspect of the AI agent
scale to understand in order to inform how agents might be
developed for the better: The more autonomous the system,
the more wecede human control.
5. Values Embedded in Agentic Systems
5.1. Methodology
To examine the ethical implications of autonomy with
respect to recent AI agent systems, we adopted a method-
ological approach in applied ethics (Shapiro et al., 1995;
9This approach to levelling is one way of categorizing; for a classic
categorization with consensus, see Russell and Norvig (1995).
3

Action surface options:The spaces (digital or analog) where
an agent can operate.
Adaptability:The extent to which a system can update its
actions based on new information or changes in context.
Number:Single-agent or multi-agent, meeting needs of
users by working together, in sequence, or in parallel.
Personalization:The extent to which an agent uses a user’s
data to provide user-specific unique content.
Personification:The extent to which an agent is designed
to be like a specific person or group of people.
Proactivity:The amount of goal-directed behavior that a
system can take without direct specification from a user.
Reactivity:Extent to which a system can respond to changes
in its environment in a timely fashion.
Request format options:The formats an agent uses for input
(e.g., code, natural language).
Versatility:Diversity of possible agent actions, including:
• Domain specificity:How many domains agent can
operate in (e.g., email, calendars, news).
• Interoperability: Extent to which agent can exchange
information and services with other programs.
• Task specificity:How many types of tasks agent may
perform (e.g., scheduling, summarizing).
• Modality specificity:How many modalities agent can
operate in (e.g., text, speech, video, images, forms, code).
Table 2.AI Agent functionalities. Further detail in Section C.
Anderson & Anderson, 2011) wherein relevant values are
identified for a given subject of interest, and positive and
negative outcomes are considered with respect to each.
Our investigation focused on how varying degrees of agent
autonomy interact with value propositions in research and
commercial implementations, yielding a value taxonomy
with foreseeable benefits and risks. Extended details on our
methodology are provided in Section E.
5.2. Note on Base Models and System Complexity
Relevant to all values described below are two points:
1. Many recent AI agents are based on LLMs, and
some definitions hinge on the use of an LLM (e.g.,
Chase (2024); Schluntz & Zhang (2024)). Ethical
considerations for this type of AI agent therefore
subsume those for LLMs, such as the incorporation
of discriminatory beliefs, unequal representation of
different subpopulations, and hegemonic viewpoints.
See previous work (e.g., Rudinger et al. (2018);
Bender & Gebru et al. (2021); Haltaufderheide &
Ranisch (2024)) for more. Models in other modalities
reflect similar issues, for example, in computer vision
(Luccioni et al., 2023; Ghosh et al., 2025) and speech
processing (Tatman, 2017; Michel et al., 2025).
2. Statistical models are not perfect when deployed in
real-world contexts (Box, 1974; Perrow, 1984; Wolpert
& Macready, 1997; Mohri et al., 2018; Qui ˜nonero
Candela et al., 2022), and modern AI agents are based
on statistical models. Following our proposed levels,
increased autonomy brings with it increased risk of
compounded errors and cascading issues as the number
and nature of potential steps expands.10 Similarly, the
risk of unwanted outcomes increases with system speed
and access – fully autonomous agents may act faster
than humans can intervene, eroding control – as well
as with increased system complexity (Amodei et al.,
2016; Alenezi & Zarour, 2020); to the extent that each
level corresponds to increased system complexity, the
risks of harmful outcomes increase with autonomy.
While we focus our ethical analysis on the behaviors of single
agents,multi-agent systemsintroduce further complexities
(Li et al., 2006) we leave for future work.
5.3. Ethical analysis
Ethical values concerning the use of AI agents interact
with autonomy in different ways, mediated by context and
application. The analysis provided below is not exhaustive;
it presents a space-constrained subset of many possible
contextually relevant considerations, 11 with particular
attention to recent public deployments. Specific examples
are provided in footnotes throughout. A summary of the
resultant value taxonomy is provided in Figure 1. We provide
this analysis as a starting point for further deliberation and
as a resource to inform priorities in AI agent research and
development. A discussion of key findings from this analysis
and further implications is provided in Section 5.4.
5.3.1. VALUE: ACCURACY
Accuracyrefers to the ability of an AI agent to utilize
appropriate processes and bring about correct outcomes.12
Potential Benefit:Agents can provide checks on model er-
rors by leveraging trusted data and processes (Du et al., 2024;
Kupershtein et al., 2024; Kwartler et al., 2024), increasing
accuracy over isolated models. Following findings on models
without autonomous capabilities, in some contexts agents
may help to improve human accuracy (Barman et al., 2016),
or perform significantly better than humans according to
relevant evaluation criteria, for example, for certain types
of detection (Yoon et al., 2023). Agents may also be more
accurate at winning game moves,13 and when given many
attempts to solve problems (Wijk et al., 2025).
10Industry practitioners have recently provided concrete estimates
of this effect (Patronus AI, 2025; Business Insider, 2025).
11Further value analyses are provided in Section D, and a mapping
between expressed values and selected sources Section F.
12As described by Du et al. (2024), Kupershtein et al. (2024),
Kwartler et al. (2024), Kapoor et al. (2024), Myakala (2024),
IBM (Gutowska, 2024), Microsoft (Levret, 2025), Salesforce
(Salesforce, 2024).
13E.g., AlphaZero (Silver et al., 2018)
4

/tasksTask Performance
/check-circle Accuracy: Number and type of checks Error propagation
/hands-helping Assistiveness: Support options, personalization Persuasion, skill loss
🚀 Efficiency: Task completion Error detection complexity
♂shield-altProtection
🔒 Safety: Physical protection Personal harm
/user-shield Security: Threat management Breaching desired security
/user-secret Privacy: Safeguarding data Unwanted exposure
/usersUser Interaction
♂robot Humanlikeness: Usability Manipulation
/handshake Trust:Benefit and risk multiplier
/gl⌢beBroader Impacts
/balance-scale-righ◎ Equity: Improved in targeted contexts Base model inequities propagate
/cogs Flexibility: Beneficial capabilities Avenues for harm
Figure 1. Selection of potential increased benefits and harms with
respect to ethical values as AI agent autonomy increases.
Risk:Many foreseeable risks stem from the compounding
effects of model inaccuracies, particularly in autonomous
settings where cascading errors propagate across multiple
action surfaces. For example, systems can integrate code that
breaks critical systems (Sharwood, 2025); inappropriately
share private information publicly (He et al., 2025);
make significantly damaging financial mistakes (Popper,
2012); and disproportionately fail for some populations in
life-critical decisions (Cross et al., 2024). Subsequent action
taken based on these errors can amplify their impact, further
intensified from inappropriate trust (Section 5.3.10) and
degradation of human oversight capable of identifying and
correcting failures in real time (Section 5.3.2).
Application to agentic levels:It may be possible to increase
accuracy when autonomy brings more verification, checks,
and balances. Yet the corresponding diminished human coun-
terbalances can create conditions where errors are difficult
to diagnose or rectify, and subsequent harms more easily
proliferate through interconnected systems.
5.3.2. VALUE: ASSISTIVENESS
Assistivenessrefers to the ability of an AI agent to complete
tasks that help a user reach their end goal.14
Potential Benefit:Agents may augment capabilities, such as
an agent for people with hand mobility issues or low vision
that can complete tasks online in response to simple language
commands (Deng et al., 2023). Agents may help to improve
users’ positive impact within their organizations and with
customers15 or increase their public reach,16 and commer-
cial sources speak to how assistance offered by AI agents
increases user freedom and opportunity.17
Risk:One of the “ironies of automation” (Bainbridge, 1983)
is that increasing automation leads users to lose competence
in rare but critical tasks because they lose practice in the
relevant domain. This effect has recently begun to be docu-
mented for deployed AI applications (Ahmad, 2025; Gerlich,
2025). Users also tend to over-trust assistive automation
even when it’s fallible, a tendency known asautomation bias
(Goddard et al., 2012; Holbrook et al., 2024). (Also see “trust”
in Section 5.3.10.) Further complicating the issue, assistive
use where AI agentssupplementworkers comes up against
the possibility ofsupplantingpeople, decreasing oversight
while increasing the risk of inaccuracy (Section 5.3.1), and
contributing to job loss and economic inequalities between
those creating agents and those replaced by them (Frank et al.,
2025; Agrawal et al., 2022).
Application to agentic levels:Each increasing AI agent
level provides for more assistance as the agent requires less
input from the developer or user and can access more action
surfaces. With this comes human overreliance, degradation
of critical skills, and difficulty in appropriate oversight, in-
creasing the risk of unwanted outcomes.
5.3.3. VALUE: EFFICIENCY
Efficiencyrefers to how AI agents help users to complete
more tasks more quickly, serving as an additional actor.18
Potential Benefit:As commonly marketed, AI agents assist
in delivering results more quickly, increasing productivity
(Andrews et al., 2025). They can free users to focus on spend-
ing more time pursuing activities they find more rewarding,
such as creative tasks.19
14ServiceNow (2025); Salesforce (2024); EY (2025); Microsoft
(2025a); Lindy (2025); Whiting (2024). Some organizations
(e.g., IBM (IBM, 2025), Workday (Pham, 2025)) distinguishAI
Assistants(reactive) fromAI Agents(proactive).
15E.g., as described for generative AI by Brynjolfsson et al. (2023),
and a motivation for Moveworks (2025); Leena AI (2025).
16E.g., Omneky (2025); Ocoya (2025)
17E.g., PwC (2025a); Salesforce (2024); Ray (2024)
18PwC (2025a); Ray (2024); Cetin (2024); Slack (2025b).
19E.g., Ray (2024); Slack (2025a); Hastings-Woodhouse (2024)
5

Risk:Given the relationship to inaccuracy (Section 5.2 and
Section 5.3.1), increased autonomy brings increased risk of
inefficiency from the time needed to identify and fix errors of
increasing magnitude and complexity.
Application to agentic levels:Benefits and risks relevant
to efficiency are tied in part to the accuracy of the model(s)
underlying an AI agent. Efficiency is therefore affected by
agent level as it concerns increased system access, complex-
ity, opacity, and the number of interacting errors.
5.3.4. VALUE: EQUITY
Equityrefers to how AI agents foster an environment where
people from different backgrounds are included.20
Potential Benefit:AI agents can aid humans in being less
exclusionary to one another,21 tracking indicators of bias,
unfairness and othering in communications, and further of-
fering solutions to address them. This can support well-being
in groups with different backgrounds. Agents may also serve
as assistive devices (Section 5.3.2) for those with differing
ability statuses,22 expanding the potential for similar oppor-
tunities and outcomes.
Risk:While equity-focused applications may provide equity-
specific benefit, there are a multitude of other AI agent
applications without this focus. Similar to accuracy (Sec-
tion 5.3.1), inequities in the base model(s) risk further propa-
gation and cascading effects as an agent has access to more
actions surfaces and can make more decisions.
Application to agentic levels:Risks of inequity may poten-
tially decrease with increased autonomy as AI agent applica-
tions focused specifically on promoting diversity, inclusion,
and equity are better able to access resources and influence
outcomes. At the same time, risks stemming from inequities
inherent in AI agents’ underlying models increase as agents
are given further control over human-critical systems.
5.3.5. VALUE: FLEXIBILITY
Withflexibilitywe include the related concept ofadaptability,
referencing a foundational motivation within AI agent
development of systems that can shape their behavior in
dynamic and diverse environments.23
20As described by Bernardini et al. (2014); Nagarajan (2024);
Kondra & Zink (2025); Houtti et al. (2025);C ¸ic ¸ek G¨uven et al.
(2025); Nixon et al. (2024); Equal Time (2025).
21E.g., Equal Time (2025); Nagarajan (2024); Kondra & Zink
(2025); Houtti et al. (2025)
22E.g., Bernardini et al. (2014); Deng et al. (2023)
23As described by Maes (1993); Valiente et al. (2022); Park et al.
(2024); Liu et al. (2023); Zhu (2023); Wang et al. (2024); Yee
et al. (2024); Benioff (2024); Detweiler & Flaningam (2024);
Github (2025); Liang & Tong (2025).
Application to agentic levels:With increased autonomy
comes the benefits and risks of the values that flexibility
enables, including assistiveness (Section 5.3.2), efficiency
(Section 5.3.3), equity (Section 5.3.4), safety (Section 5.3.8),
security (Section 5.3.9), privacy (Section 5.3.7), and rele-
vance (Section D.0.2). Similarly, the more flexibility an
agent has to affect and be affected by systems, the greater the
potential for benefit and harm. For example, increased access
to computer systems and software increases the potential for
an AI agent to identify vulnerabilities, and also increases the
risk of integrating malicious code (Wen, 2024); flexibility can
provide more assistive options and attack vectors.24 Notably,
pervasive issues with accuracy (Section 5.3.1), and the inabil-
ity to guarantee appropriate outcomes, has led companies to
refrain from full automation in directly consequential appli-
cations, such as in purchasing (Knight, 2024) and healthcare
(Lindquist, 2025).
5.3.6. VALUE: HUMANLIKENESS
Humanlikenessrefers to the extent to which an AI agent can
be perceived as similar to a human.25 Even when human-
likeness is not explicitly designed, people have a tendency to
anthropomorphize (ascribing humanlike traits to non-human
entities) (Epley et al., 2007), and to treat computer systems
as if they were people (Nass et al., 1994; Reeves & Nass,
1996). These predispositions can be amplified by AI systems
through both the selection of training data and the interface
design (Waytz et al., 2014), such as by incorporating
first-person voice, self-referential or mentalistic language
(e.g., ‘I understand,’ ‘I decided’), retention of user details,
naturalistic prosody, photorealistic avatars, and scripted
social behaviors like greetings, apologies, and small talk.
Potential Benefit:A primary motivation for systems to mir-
ror humanlike behavior is the positive effect it can have on
user experience. Studies have consistently shown that inter-
faces designed to mimic different aspects of humanlikeness
and “social presence” can make computer interactions easier
(Short et al., 1976; Park et al., 2023) and friendlier (Jan-
son, 2023), increasing comfort, pleasure, and satisfaction
(Xie et al., 2023; Janson, 2023). Some research has posited
controversial potential benefits, such as that AI agent human-
likeness could be beneficial for companionship (Sidner et al.,
2018) or useful for running simulations on how different sub-
populations might respond in different situations (Park et al.,
2024). Outside of the domain of AI, anthropomorphisation
has been shown to have some benefits, such as assisting in
the retention and learning of new concepts (Blanchard & Mc-
nincth, 1984; Dorion, 2011); such findings may be useful in
24Since initial submission of this preprint, real harm from the
interaction of flexibility and cybersecurity has been documented
by Anthropic (2025).
25As described by Alabed et al. (2022); Stanford HAI (2023);
Salesforce (2024a); Vander Elst et al. (2025); Gannotti (2025).
6

aiding the development of humanlike AI agents for positive
outcomes.
Risk:The positive feelings humanlikeness stimulates in
users is not without corresponding risks. For example, hu-
manlikeness stimulates empathy and willingness to comply
(Araujo, 2018; Janson, 2023; Park et al., 2023; Keeling et al.,
2010; Adam et al., 2021), which can lead to harms described
for “trust” (Section 5.3.10), as well as lowered vigilance,
increased emotional entanglement, vulnerability to persua-
sion, overreliance or dependence, and addiction. 26 These
behaviors may further influence anti-social behavior27 and
self-harm.28 The phenomenon of “uncanny valley” adds
another layer of complexity: As agents become more hu-
manlike but fall short of perfect human simulation, they
can trigger feelings of unease, revulsion, or cognitive dis-
sonance in users. Recent work also suggests that making
AI humanlike might lead people to treat real humans more
“mechanistically” (with less care and dehumanization) or blur
boundaries of social norms (Kim & McGill, 2025).
Application to agentic levels:The phenomenon of perceived
humanlikeness is possible at the most basic level of AI agent
(e.g., a chatbot), meaning that associated benefits and harms
emerge from systems without autonomy. The increased capa-
bilities provided by autonomy can further amplify this effect,
providing for closer alignment to user behavior and an ex-
pansion of the ways in which a user and an agent can interact
– and what the agent can affect. When humanlike cues co-
occur with autonomy, increased autonomy therefore acts as a
risk multiplier: increased access and decreased human con-
trol compound the risks of misplaced trust (Section 5.3.10)
and further cascading harms.
5.3.7. VALUE: PRIVACY
Privacyrefers to how many people may be able to access
a user’s content, including their data and actions.29
Potential Benefit:To the extent that AI agents can model
individuals’ privacy preferences, increased autonomy asso-
ciated with increased access across devices, platforms, and
applications can allow agents to align a user’s privacy set-
tings to their preferences throughout the digital space (Xu
et al., 2025). Agents can also be used to monitor outgoing
communications, permissions, or network activity to alert
users if sensitive data is being transmitted inappropriately
(Yuan et al., 2025). Agents might also provide a form of
personal identity masking: Instead of a user being exposed,
26E.g., Samuel (2024)
27There is a related concern that AI agent social interaction may
contribute to loneliness, but see (Morahan-Martin & Schumacher,
2003; O’Day & Heimberg, 2021) for nuances.
28E.g., NPR (2024)
29As described by Lim & Shim (2022), Bagdasarian et al. (2024),
Finch (2025), Microsoft (2025b).
an agent could act as a proxy, obscuring identifying metadata
like typing speed, dialect, or style (Finch, 2025). AI agents
may also offer some privacy in keeping transactions and tasks
wholly confidential (aside from what is monitorable by the
AI agent provider). Recent work has also shown how agents
can be used to analyze privacy documentation to assist users
in informed consent (Sun et al., 2025).
Risk:For agents to work according to user expectations,
the user may need to provide personal information such as
where they are going, who they are meeting with, and what
they are doing – divulging information that might otherwise
not be shared, opening up security (Section 5.3.9) and safety
(Section 5.3.8) risks. For the agent to be able to act on behalf
of the user in a personalized way, it may also have access
to information sources that can be used to isolate further
privacy information (for example, from contact lists, calen-
dars, etc.). Users can easily give up control of their data
for convenience and efficiency (and are more likely to when
trusting the agent); if there is a privacy breach, the intercon-
nectivity of different content brought by the AI agent can
exacerbate harms. For example, an AI agent with access
to phone conversations and social media could share highly
intimate information publicly without consent of those in-
volved. Because disclosures in conversational settings are
often involuntary or driven by social cues, privacy loss can
occur without deliberate consent, and is hard to reverse once
data is entangled in training or memory stores.
Application to agentic levels:The more people allow agents
to move across digital surfaces, the more potential there
is for convenience and increased privacy oversight, at the
risk of privacy breaches outside of human control. As au-
tonomy grows, privacy risk shifts from disclosure to execu-
tion: Agents may act on or propagate private information
across systems (emails, calendars, codebases), multiplying
the reach of a single overshare.
5.3.8. VALUE: SAFETY
The ethical value ofsafetyencompasses multiple types,
among them physical, psychological, reputational, infor-
mational, and financial. Physical safety of large swaths of
the population is a primary concern in the development of
Artificial General Intelligence (AGI) (Kreps et al., 2025).
Potential Benefit:AI agents may enhance human safety
by monitoring, predicting and directly addressing physical
and digital risks. Robotic AI agents may help save people
from bodily harm, such as agents capable of diffusing bombs,
removing poisons, or operating in manufacturing or indus-
trial settings that are hazardous environments for humans.
They can also assist with preventing physical safety accidents
and critical infrastructure failures, such as by monitoring for
warning signs (Agarwal, 2025) or tracking human attention
(Hu et al., 2022) with respect to obstacles, alerting users –
7

or directly adjusting their movements – to avoid harm such
as falling30 or colliding.31 Conversational agents with the
autonomy to interact outside of the chat window could also
alert appropriate resources when a user may engage in vi-
olence, such as by self-harm or hurting others. 32 Further
benefits intersect with security (Section 5.3.9) and privacy
(Section 5.3.7), where systems can aid in keeping people,
structures, and organizations safe from the effects of vulnera-
bilities and malicious actors.
Risk:Safety risks arise from multiple aspects of AI agent
deployment, among themunpredictability,digital access,
and a user’smalicious intent.
• Unpredictability: The unpredictable nature of base
models underlying AI agents, alongside the ability
of AI agents to create action sequences that have not
been previously specified by a person, means that even
seemingly safe individual operations could combine
in unforeseen harmful ways, creating new risks that are
difficult to prevent. A similar phenomenon is described
in the theory ofInstrumental Convergenceand the
classic paperclip maximizer problem (Gans, 2018).
Further, unpredictability interacts with the effectiveness
of guardrails: The way a guardrail is specified may
inadvertently creates further problems in unanticipated
ways, and humans may not predict all the ways an
AI agent can design a process that overrides a given
guardrail. If guardrails mitigate loss of human life,
such as with autonomous surgeons or missile system
operation, this is a severe (life-ending) risk.
• Digital Access: Humanlike behavior alongside access
to broad interfaces (“Action Surfaces” in Table 2),
including GUIs and external applications, gives agents
the ability to perform unsafe actions without setting
off warning systems – such as by manipulating or
deleting files, impersonating users on social media,
using stored credit card information to make purchases,
launching unsafe protocols, or creating privacy and
security breaches. Still further safety risks emerge from
AI agents’ ability to interact with multiple systems and
the by-design lack of human oversight for each action.
• Malicious intent: Human actors seeking to create
harm can use agents to mask their identity (see
“privacy” in Section 5.3.7) while broadening reach and
personalizing content for specific individuals, further
enabling harmful activities such as phishing campaigns,
system hacking, or spreading disinformation at scale.
Application to agentic levels:Broadly construed, greater
agent autonomy amplifies the scope and severity of potential
safety harms: The goal of making agents more capable and ef-
30E.g., in the case of elderly and child safety robotic agents (Zhao
et al., 2023).
31E.g., in the case of autonomous vehicles (Agarwal, 2025).
32E.g., OpenAI (2025).
ficient through expanded system access, more sophisticated
action chains, and reduced human oversight brings with it
increased risk along multiple safety dimensions, including
physical, financial, digital, societal, and informational. Com-
plicating this issue, human-defined safeguards to mitigate
foreseeable issues are bounded by their initial specifications
while the agent may generate novel behaviors or processes
that operate beyond those predefined limits.
5.3.9. VALUE: SECURITY
Securityrefers to protection from harmful outcomes. It
encompasses protecting people, systems, organizations
and data from malicious, unauthorized, or unintentionally
problematic actions.33 Benefits and risks associated with
security overlap with those of safety (Section 5.3.8), such as
those concerning protective actions and digital access, and
with those of privacy (Section 5.3.7), such as in the handling
sensitive information.
Potential Benefit:A key potential benefit of AI agents for se-
curity is the ability to monitor and respond to security threats,
such as by identifying cybersecurity vulnerabilities and enact-
ing solutions (DARPA, 2016; Wen, 2024). Agents can also
provide potential benefits for informational security, such
as by protecting privacy (Section 5.3.7) within dynamically
changing environments in real-time.
Risk:AI agents present security challenges when handling
sensitive data (such as customer or user information), par-
ticularly given corresponding safety risks (Section 5.3.8),
such as the ability to interact with or infiltrate multiple sys-
tems without detailed human oversight, and the potential for
data leakage (Zharmagambetov et al., 2025). Security risks
also emerge from agents creating inappropriate solutions to
solve problems, such as by disabling alerts (Beers & Rushing,
2025). Similar to “safety” (Section 5.3.8) malicious use of
AI agent systems can also create security harms, particularly
when used to mask the actors’ identity, such as by access-
ing connected systems, stealing sensitive information, or
conducting automated attacks at scale.
Application to agentic levels:In general, the greater the
autonomy, the greater the attack surface and attack options.34
However, different AI agent levels affect security differently:
For the first four, developers maintain some control of the
code the agent can access, providing a built-in ability to
mitigate security outbreaks, e.g., by blocking communication
with third parties. However, when an agent is able to create
and execute new code (a fully autonomous agent), it’s capable
of creating breaches unforeseen by developers. In the most
extreme form of full autonomy – without guardrails – the
33As described by DARPA (2016); Wen (2024); Finch (2025); Labs
(2025); Microsoft (2025b).
34Documented by Anthropic (2025) after submission of this work.
8

corresponding security risk is clear.
5.3.10. VALUE: TRUST
Recent AI agent writing generally does not motivate how
agents benefit or harm trust, but rather, that systems should
be constructed to be worthy of our trust, shown to be safe
(Section 5.3.8), secure (Section 5.3.9) and reliable. Seminal
work in the past has warned about the risks of trusting au-
tomated systems (e.g., Bainbridge (1983)) and has proposed
corresponding methods for creating trustworthy systems
(e.g., Maes (1994)): work that is applicable to development
today. We include this value here due to its historical
significance in the evolution of AI agent development and
its deep interconnection to how other values are manifested.
Multiple forces inflate trust, including:
• Humanlike presentation (first-person voice, personas,
and memory cue mind-perception and lower vigilance)
(see Section 5.3.6).
• Automation bias (the tendency to defer to a system even
when it is fallible).
• Apparent competence from frequent success (people
over-weight the next output when the system was
“mostly right” before).
Together, these factors produce inappropriate trust precisely
where statistical models are prone to errors.
Application to agentic levels:Trust-related risks arise from
limitations in the predictability and accuracy (Section 5.3.1)
of AI agents, and can be heightened by humanlikeness (Sec-
tion 5.3.6). These issues are exacerbated as agents gain
greater flexibility (Section 5.3.5) and system access, expand-
ing potential harms to privacy (Section 5.3.7), safety (Sec-
tion 5.3.8), and security (Section 5.3.9). To the extent that
increased autonomy is associated with broader action sur-
faces and reduced oversight, even small miscalibrations of
trust at different levels of autonomy multiply into larger harm
surfaces; conversely, trust calibration (e.g., through trans-
parency and uncertainty cues) becomes more critical with
each autonomy level.
5.4. Discussion
We have only scratched the surface of values at play in
the use of AI agents, and how agent autonomy interacts
with potential benefits and risks. This initial work suggests
that base model(s) influence all outcomes, and increased
autonomy enables more flexible and context-sensitive action
while amplifying the magnitude of harms stemming from
isolated system issues. Many benefits are tied to specific
AI agent applications (e.g., privacy preservation, equity
support), while risks increase with greater access, decreased
and degraded oversight on agent actions, and malicious use.
In general, lower autonomy poses risks through perception
and interactional cues (e.g., humanlikeness, over-trust,
oversharing). Intermediate levels add execution risks as
the agent carries out plans on the user’s behalf, at which
point human-centered safeguards – such as those protecting
privacy and security – are no longer governed by those with
contextual understanding of their value. High-autonomy
systems concentrate and compound these effects; foreseeing
all necessary safeguards and providing appropriate oversight
may not be possible in fully autonomous systems.
Concerns about potential negative ramifications of agent
autonomy has motivated calls for human oversight of AI
agents.35 This work suggests that mechanisms for oversight
should account for increased complications related to
increased autonomy, including issues that arise from the
interaction of autonomy and human oversight itself.
6. Conclusion: Where do we go from here?
The history of nuclear close calls provides a sobering lesson
about the risks of ceding human control to autonomous
systems.36 For example, in 1980, computer systems falsely
indicated over 2,000 Soviet missiles were heading toward
North America. The error triggered emergency procedures:
bomber crews rushed to their stations and command posts
prepared for war. Only human cross-verification between
different warning systems revealed the false alarm. Similar
incidents can be found throughout history.
Such historical precedents are clearly linked to foreseeable
benefits and risks of AI agents. We find no clear benefit
of fully autonomous AI agents that can operate outside of
human-defined constraints, but many foreseeable harms
from ceding full human control. Looking forward, this
suggests several critical directions:
1. Adoption of a spectrum of AI agent autonomy:Rec-
ognizing the nature of autonomy and how it interacts
with system implementations can help to highlight op-
portunities and associated risks aligned with different
values. Further, clear distinctions between levels of
agent autonomy can aid in task delegation and prioritiza-
tion for governance and development (Srikumar et al.).
2. Human control mechanisms:Developing robust
frameworks, both at the technical and the policy
level (Cihon, 2024; World Economic Forum, 2024)
can help support meaningful human oversight while
preserving beneficial semi-autonomous functionality.
This includes creating reliable override systems and
establishing clear boundaries for agent operation.
3. Safety guarantees:Creating new methods to constrain
AI agent behavior within intended operating parameters,
35E.g., (Microsoft WorkLab, 2025; PwC, 2025b; Salesforce, 2024)
36False alarm: 1979 NORAD scare was one of several nuclear close
calls - UPI
9

and to ensure that they cannot override human-specified
constraints.
The development of AI agents is a critical inflection point
in artificial intelligence. As history demonstrates, even
well-engineered autonomous systems can make catastrophic
errors from trivial causes. While increased autonomy
can offer genuine benefits in specific contexts, human
judgment and contextual understanding remain essential,
particularly for high-stakes decisions. The ability to access
the environments an AI agent is operating in is essential, pro-
viding humans with the ability to say “no” when a system’s
autonomy drives it well away from human values and goals.
7. Acknowledgements
We thank Bruna Trevelin, Orion Penner, and Aymeric
Roucher for significant contributions to this piece.
References
Adam, M., Wessel, M., and Benlian, A. AI-based chatbots
in customer service and their effects on user compliance.
Electronic markets, 31(2):427–445, 2021.
Agarwal, A. Autonomous lookahead for early risk tracking
(alert): AI-driven predictive simulation for safe and
proactive driver intervention. InApplications of Machine
Learning 2025, volume 13606, pp. 427–444. SPIE, 2025.
Agrawal, A., Gans, J., and Goldfarb, A.Power and predic-
tion: The disruptive economics of artificial intelligence.
Harvard Business Press, 2022.
Ahmad, O. F. Endoscopist deskilling risk after exposure
to artificial intelligence in colonoscopy: a multicentre,
observational study.The Lancet Gastroenterology &
Hepatology, 2025.
Ahn, M., Dwibedi, D., Finn, C., Arenas, M. G., Gopalakr-
ishnan, K., Hausman, K., Ichter, B., Irpan, A., Joshi, N.,
Julian, R., Kirmani, S., Leal, I., Lee, E., Levine, S., Lu, Y .,
Leal, I., Maddineni, S., Rao, K., Sadigh, D., Sanketi, P.,
Sermanet, P., Vuong, Q., Welker, S., Xia, F., Xiao, T., Xu,
P., Xu, S., and Xu, Z. Autort: Embodied foundation mod-
els for large scale orchestration of robotic agents. 2024.
Alabed, A., Javornik, A., and Gregory-Smith, D. AI anthro-
pomorphism and its effect on users’ self-congruence and
self–AI integration: A theoretical framework and research
agenda.Technological Forecasting and Social Change,
182:121786, 2022.
Alenezi, M. and Zarour, M. On the relationship between
software complexity and security.CoRR, abs/2002.07135,
2020.
Amodei, D., Olah, C., Steinhardt, J., Christiano, P. F.,
Schulman, J., and Man ´e, D. Concrete problems in AI
safety.CoRR, abs/1606.06565, 2016.
Anderson, M. and Anderson, S. L. (eds.).Machine Ethics.
Cambridge University Press, New York, 2011.
Andrews, P., Benhalloum, A., Bertran, G. M.-T., Bettini, M.,
Budhiraja, A., Cabral, R. S., Do, V ., Froger, R., Garreau,
E., Gaya, J.-B., et al. ARE: Scaling up agent environments
and evaluations. 2025.
Anscombe, G. E. M.Intention. Basil Blackwell, Oxford,
1957.
Anthropic. Claude 3.5 and computer use, 2024. URL
https://www.anthropic.com/news/3-5-models-and-
computer-use.
Anthropic. Threat intelligence report: August 2025,
August 2025. URL https://www-cdn.anthropic.com/
b2a76c6f6992465c09a6f2fce282f6c0cea8c200.pdf.
Araujo, T. Living up to the chatbot hype: The influence of
anthropomorphic design cues and communicative agency
framing on conversational agent and company perceptions.
Computers in human behavior, 85:183–189, 2018.
Aristotle.Politics, volume 1. Batoche Books, Kitchener,
1999.
Asimov, I. Runaround.Astounding Science Fiction, 1942.
Attri.ai. Elevate time management with AI-powered schedul-
ing, 2025. URL https://attri.ai/ai-agents/scheduling-
agent.
Bagdasarian, E., Yi, R., Ghalebikesabi, S., Kairouz, P.,
Gruteser, M., Oh, S., Balle, B., and Ramage, D. Airgapa-
gent: Protecting privacy-conscious conversational agents.
CCS ’24: Proceedings of the 2024 on ACM SIGSAC Con-
ference on Computer and Communications Security, 2024.
Bai, H., Zhou, Y ., Cemri, M., Pan, J., Suhr, A., Levine, S.,
and Kumar, A. Digirl: Training in-the-wild device-control
agents with autonomous reinforcement learning.arXiv
preprint arXiv:2406.11896, 2024.
Bainbridge, L. Ironies of automation.Automatica, 19(6):
775–779, 1983.
Barman, S., Pal, U., Sarfaraj, M., Biswas, B., Mahata,
A., and Mandal, P. A complete literature review on
financial fraud detection applying data mining tech-
niques.International Journal of Trust Management in
Computing and Communications, 3:336, 01 2016. doi:
10.1504/IJTMCC.2016.084561.
10

Beers, K. and Rushing, C. AI control: How to make
use of misbehaving AI agents, October 2025. URL
https://cset.georgetown.edu/article/ai-control-how-to-
make-use-of-misbehaving-ai-agents/.
Bender & Gebru, E. M., Timnit, McMillan-Major, A., and
Shmitchell, S. On the dangers of stochastic parrots: Can
language models be too big? InProceedings of the
2021 ACM conference on fairness, accountability, and
transparency, pp. 610–623, 2021.
Benioff, M. How the rise of new digital workers will lead
to an unlimited age, November 2024.
Bernardini, S., Porayska-Pomsta, K., and Smith, T. J.
ECHOES: An intelligent serious game for fostering social
communication in children with autism.Information
Sciences, 264:41–60, 2014.
Bi, N. and Huang, J. Y .-C. I create, therefore i agree:
Exploring the effect of AI anthropomorphism on human
decision-making. InCompanion Publication of the
2023 Conference on Computer Supported Cooperative
Work and Social Computing, CSCW ’23 Companion, pp.
241–244, New York, NY , USA, 2023. Association for
Computing Machinery.
Blanchard, J. and Mcnincth, G. The effects of anthropo-
morphism on word learning.The Journal of Educational
Research, 78(2):105–110, 1984.
Bloch, E., Conn, A., Garcia, D., Gill, A., Llorens, A.,
Noorma, M., and Roff, H. Ethical and technical challenges
in the development, use, and governance of autonomous
weapons systems. Technical report, IEEE Standards
Association, 2020.
Boutilier, C., Dean, T., and Hanks, S. Decision-theoretic plan-
ning: Structural assumptions and computational leverage.
Journal of Artificial Intelligence Research, 11:1–94, 1999.
Box, G. E. P. Science and statistics.Journal of the American
Statistical Association, 69(345):791–799, 1974.
Bratman, M. E.Intention, Plans, and Practical Reason.
Harvard University Press, Cambridge, MA, 1987.
Brohan, A., Brown, N., Carbajal, J., Chebotar, Y ., Dabis,
J., Finn, C., Gopalakrishnan, K., Hausman, K., Herzog,
A., Hsu, J., Ibarz, J., Ichter, B., Irpan, A., Jackson, T.,
Jesmonth, S., Joshi, N., Julian, R., Kalashnikov, D.,
Kuang, Y ., Leal, I., Lee, K.-H., Levine, S., Lu, Y ., Malla,
U., Manjunath, D., Mordatch, I., Nachum, O., Parada, C.,
Peralta, J., Perez, E., Pertsch, K., Quiambao, J., Rao, K.,
Ryoo, M. S., Salazar, G., Sanketi, P. R., Sayed, K., Singh,
J., Sontakke, S., Stone, A., Tan, C., Tran, H., Vanhoucke,
V ., Vega, S., Vuong, Q. H., Xia, F., Xiao, T., Xu, P., Xu, S.,
Yu, T., and Zitkovich, B. RT-1: Robotics Transformer for
Real-World Control at Scale. InProceedings of Robotics:
Science and Systems, Daegu, Republic of Korea, July
2023. doi: 10.15607/RSS.2023.XIX.025.
Brynjolfsson, E., Li, D., and Raymond, L. R. Generative
AI at work. Working Paper 31161, National Bureau of
Economic Research, 2023.
Business Insider. Don’t get too excited about AI agents yet.
they make a lot of mistakes.Business Insider, April 2025.
Busoniu, L., Babuska, R., and De Schutter, B. A comprehen-
sive survey of multiagent reinforcement learning.IEEE
Transactions on Systems, Man, and Cybernetics, Part C
(Applications and Reviews), 38(2):156–172, 2008.
Cai, T., Liu, Y ., Zhou, Z., Ma, H., Zhao, S. Z., Wu, Z., and Ma,
J. Driving with regulation: Interpretable decision-making
for autonomous vehicles with retrieval-augmented
reasoning via llm, 2025.
Castelfranchi, C. Guarantees for autonomy in cognitive
agent architecture. In Wooldridge, M. J. and Jennings,
N. R. (eds.),Intelligent Agents, pp. 56–70, Berlin,
Heidelberg, 1995. Springer Berlin Heidelberg.
Cetin, E. AI agents explained: The future of task au-
tomation and productivity, December 2024. URL https:
//www.ciklum.com/resources/blog/ai-agents-explained.
Chan, A., Salganik, R., Markelius, A., Pang, C., Rajkumar,
N., Krasheninnikov, D., Langosco, L., He, Z., Duan,
Y ., Carroll, M., Lin, M., Mayhew, A., Collins, K.,
Molamohammadi, M., Burden, J., Zhao, W., Rismani,
S., V oudouris, K., Bhatt, U., Weller, A., Krueger, D., and
Maharaj, T. Harms from increasingly agentic algorithmic
systems. In2023 ACM Conference on Fairness Account-
ability and Transparency, FAccT ’23, pp. 651–666. ACM,
June 2023. doi: 10.1145/3593013.3594033.
Chase, H. What is an AI agent?, June 2024. URL
https://blog.langchain.com/what-is-an-agent.
Chavannes, E., Klonowska, K., and Sweijs, T. Governing
autonomous weapon systems.The Hague: The Hague
Centre For Strategic Studies, 2020.
Cihon, P. Chilling autonomy: Policy enforcement for human
oversight of AI agents. In41st International Conference
on Machine Learning, Workshop on Generative AI and
Law, 2024.
CNN. Zillow’s home-buying debacle shows how hard it is
to use AI to value real estate, November 09 2021. URL
https://edition.cnn.com/2021/11/09/tech/zillow-ibuying-
home-zestimate.
11

Cross, J. L., Choma, M. A., and Onofrey, J. A. Bias in
medical AI: Implications for clinical decision-making.
PLOS Digital Health, 3(11), 2024.
Cui, C., Ma, Y ., Cao, X., Ye, W., Zhou, Y ., Liang, K., Chen,
J., Lu, J., Yang, Z., Liao, K.-D., Gao, T., Li, E., Tang,
K., Cao, Z., Zhou, T., Liu, A., Yan, X., Mei, S., Cao, J.,
Wang, Z., and Zheng, C. A survey on multimodal large
language models for autonomous driving. InProceedings
of the IEEE/CVF Winter Conference on Applications
of Computer Vision (WACV) Workshops, pp. 958–979,
January 2024a.
Cui, Y ., Huang, S., Zhong, J., Liu, Z., Wang, Y ., Sun, C., Li,
B., Wang, X., and Khajepour, A. Drivellm: Charting the
path toward full autonomous driving with large language
models.IEEE Transactions on Intelligent Vehicles, 9(1):
1450–1464, 2024b.
Cummings, M. L. Artificial intelligence and the future
of warfare. Technical report, International Security
Department and US and the Americas Programme,
2017. URL https://www.chathamhouse.org/sites/
default/files/publications/research/2017-01-26-artificial-
intelligence-future-warfare-cummings.pdf.
Damsa, A. AI with personality — prompting chatgpt using
big five values.Medium, 2023.
DARPA. Darpa’s cyber grand challenge, 2016. URL
https://www.darpa.mil/research/programs/cyber-grand-
challenge.
Datadog. What is an AI agent? DatadogHQ, 2025. URL
https://www.datadoghq.com/knowledge-center/aiops/ai-
agents/.
Davidson, D. Actions, reasons, and causes.The Journal of
Philosophy, 60(23):685–700, 1963.
Deloitte. Autonomous generative AI agents: Under
development, 2024. URL https://www2.deloitte.com/
us/en/insights/industry/technology/technology-media-
and-telecom-predictions/2025/autonomous-generative-
ai-agents-still-under-development.html.
Deng, X., Gu, Y ., Zheng, B., Chen, S., Stevens, S., Wang, B.,
Sun, H., and Su, Y . Mind2web: towards a generalist agent
for the web. InProceedings of the 37th International Con-
ference on Neural Information Processing Systems, NIPS
’23, Red Hook, NY , USA, 2023. Curran Associates Inc.
Detweiler, J. and Flaningam, E. The agentic web, 2024.
URL https://www.felicis.com/insight/the-agentic-web.
Dorion, K. A learner’s tactic: How secondary students’
anthropomorphic language may support learning of
abstract science concepts.Electronic Journal of Science
Education, 12(2), 2011.
Drabble, B. and Tate, A. O-plan: A situated planning
agent, 1995. URL https://www.aiai.ed.ac.uk/publications/
documents/1995/95-ewsp-situated-agent.pdf.
Du, Y ., Li, S., Torralba, A., Tenenbaum, J. B., and Mordatch,
I. Improving factuality and reasoning in language models
through multiagent debate. InProceedings of the 41st
International Conference on Machine Learning (ICML),
2024.
Ecobee. Smart thermostats, 2025. URL https:
//www.ecobee.com/en-us/smart-thermostats/.
Epley, N., Waytz, A., and Cacioppo, J. On seeing human: A
three-factor theory of anthropomorphism.Psychological
Review, 114:864–886, 10 2007.
Equal Time. Equal time – AI notetaker for effective and
inclusive meetings, 2025. URL https://equaltime.io.
Etzioni, A. and Etzioni, O. Pros and cons of autonomous
weapons systems.Military Review, 2017. URL
https://www.armyupress.army.mil/Journals/Military-
Review/English-Edition-Archives/May-June-2017/
Pros-and-Cons-of-Autonomous-Weapons-Systems/.
Everett, M. Taiwan develops suicide drones akin to ukraine’s
to defend against china. Financial Times, 2025. URL
https://www.ft.com/content/23069435-ada0-4494-9ec0-
b4730be8a124.
EY. How AI agents will take gen AI from
answers to actions, February 2025. URL
https://www.ey.com/en us/insights/ai/how-ai-agents-
will-take-gen-ai-from-answers-to-actions.
Fard, M. M. and Pineau, J. Non-deterministic policies
in markovian decision processes.Journal of Artificial
Intelligence Research, 40:1–24, 2011.
Field, H. Scale ai announces multimillion-dollar de-
fense / military deal. CNBC, March 2025. URL
https://www.cnbc.com/2025/03/05/scale-ai-announces-
multimillion-dollar-defense-military-deal.html.
Finch, L. AI agents will enhance — not impair — pri-
vacy. here’s how. Salesforce, February 2025. URL
https://www.salesforce.com/news/stories/agentic-ai-for-
privacy-security/.
Frank, M. R., Ahn, Y .-Y ., and Moro, E. AI exposure predicts
unemployment risk: A new approach to technology-driven
job loss.PNAS nexus, 4(4):pgaf107, 2025.
Frankfurt, H. Freedom of the will and the concept of a
person.Journal of Philosophy, 68(1):5–20, 1971.
12

Gabriel, I., Manzini, A., Keeling, G., Hendricks, L. A.,
Rieser, V ., Iqbal, H., Tomaˇsev, N., Ktena, I., Kenton, Z.,
Rodriguez, M., et al. The ethics of advanced ai assistants.
2024.
Gacek, C., Abd-Allah, A., Clark, B., and Boehm, B. On the
definition of software system architecture. InProceedings
of the First International Workshop on Architectures for
Software Systems, pp. 85–94. Seattle, Wa, 1995.
Gaeta, P. Who acts when autonomous weapons
strike?Journal of International Criminal
Justice, 21(5):1033–1054, 2023. URL https:
//academic.oup.com/jicj/article/21/5/1033/7591635.
Gannotti, M. Agents with azure AI foundry – webi-
nar series for microsoft AI agents recording, April
2025. URL https://techcommunity.microsoft.com/
blog/healthcareandlifesciencesblog/agents-with-azure-
ai-foundry---webinar-series-for-microsoft-ai-agents-
recording/4407740.
Gans, J. AI and the paperclip problem. V oxEU CEPR,
June 2018. URL https://cepr.org/voxeu/columns/ai-and-
paperclip-problem.
Garry, M., Chan, W. M., Foster, J., and Henkel, L. A. Large
language models (llms) and the institutionalization of
misinformation.Trends in Cognitive Sciences, 28(12):
1078–1088, 2024.
Genesereth, M. R. and Ketchpel, S. P. Software agents.
Commun. ACM, 37(7):48–ff., July 1994.
Gerlich, M. AI tools in society: Impacts on cognitive
offloading and the future of critical thinking.Societies,
15(1):6, 2025.
Ghosh, S., Gautam, S., Venkit, P., and Ghosh, A. Document-
ing patterns of exoticism of marginalized populations
within text-to-image generators.arXiv preprint
arXiv:2508.02937, 2025.
Github. What are AI agents?, February 2025. URL https:
//github.com/resources/articles/ai/what-are-ai-agents.
Goddard, K., Roudsari, A., and Wyatt, J. C. Automation bias:
a systematic review of frequency, effect mediators, and
mitigators.Journal of the American Medical Informatics
Association (JAMIA), 19(1):121–127, 2012.
Goldman, A.A Theory of Human Action. Prentice-Hall,
Englewood Cliffs, NJ, 1970.
Google. Google gemini, 2025. URL https:
//gemini.google.com.
Google DeepMind. Shaping the future of advanced robotics,
2024a. URL https://deepmind.google/discover/blog/
shaping-the-future-of-advanced-robotics/.
Google DeepMind. Project mariner, 2024b. URL
https://deepmind.google/technologies/project-mariner/.
Greyling, C., 2024. URL https://cobusgreyling.medium.
com/5-levels-of-ai-agents-updated-0ddf8931a1c6.
Guestrin, C., Venkataraman, S., and Koller, D. Context-
specific multiagent coordination and planning with
factored mdps. InAAAI/IAAI, pp. 253–259, 2002.
Guilfoyle, C. and Warner, E. Intelligent agents: The new
revolution in software (ovum report), 1994.
Gutowska, A. What are AI agents?, 2024. URL
https://www.ibm.com/think/topics/ai-agents.
Haidegger, T. Autonomy for surgical robots: Concepts and
paradigms.IEEE Transactions on Medical Robotics and
Bionics, 1(2):65–76, 2019.
Haltaufderheide, J. and Ranisch, R. The ethics of chatgpt
in medicine and healthcare: a systematic review on large
language models (llms).NPJ Digital Medicine, 7, 2024.
Hao, K. AI is taking water from the desert.The Atlantic,
2024.
Hastings-Woodhouse, S. Why you should care about AI
agents, December 2024. URL https://futureoflife.org/ai/
why-you-should-care-about-ai-agents.
Hawkins, A. J. Waymo to test in 10 new cities in 2025,
starting with las vegas and san diego, January 2025. URL
https://www.theverge.com/news/600542/waymo-test-
cities-las-vegas-san-diego-2025.
He, H., Yao, W., Ma, K., Yu, W., Dai, Y ., Zhang, H., Lan,
Z., and Yu, D. Webvoyager: Building an end-to-end
web agent with large multimodal models.arXiv preprint
arXiv:2401.13919, 2024.
He, Y ., Wang, E., Rong, Y ., Cheng, Z., and Chen, H. Security
of ai agents. In2025 IEEE/ACM International Workshop
on Responsible AI Engineering (RAIE), pp. 45–52. IEEE,
2025.
Helleboogh, A., Vizzari, G., Uhrmacher, A., and Michel,
F. Modeling dynamic environments in multi-agent
simulation.Autonomous Agents and Multi-Agent Systems,
14:87–116, 2007.
Holbrook, C., Holman, D., Clingo, J., and Wagner, A. R.
Overtrust in AI recommendations about whether or not to
kill: Evidence from two human–robot interaction studies.
Scientific Reports, 14, 2024.
13

Houtti, M., Zhou, M., Terveen, L., and Chancellor, S.
Observe, ask, intervene: Designing AI agents for more
inclusive meetings. InProceedings of the 2025 CHI
Conference on Human Factors in Computing Systems,
CHI ’25, New York, NY , USA, 2025. Association for
Computing Machinery.
Hu, Z., Zhang, Y ., Xing, Y ., Zhao, Y ., Cao, D., and Lv, C.
Toward human-centered automated driving: A novel
spatiotemporal vision transformer-enabled head tracker.
IEEE Vehicular Technology Magazine, 17(4):57–64, 2022.
Huang, W., Abbeel, P., Pathak, D., and Mordatch, I.
Language models as zero-shot planners: Extracting
actionable knowledge for embodied agents. In Chaudhuri,
K., Jegelka, S., Song, L., Szepesv ´ari, C., Niu, G., and
Sabato, S. (eds.),Proceedings of the 39th International
Conference on Machine Learning, volume 162 ofPro-
ceedings of Machine Learning Research, pp. 9118–9147.
PMLR, July 2022.
HubSpot. Scale social channels with a social media AI
agent, 2025. URL https://www.hubspot.com/products/
marketing/social-media-ai-agent.
Huyen, C. Agents, January 2025. URL
https://huyenchip.com/2025/01/07/agents.html.
IBM. Agentic AI: 4 reasons why it’s the
next big thing in AI research, 2024. URL
https://www.ibm.com/think/insights/agentic-ai.
IBM. AI agents vs. AI assistants, 2025. URL https:
//www.ibm.com/think/topics/ai-agents-vs-ai-assistants.
Janson, A. How to leverage anthropomorphism for chatbot
service interfaces: The interplay of communication style
and personification.Computers in Human Behavior, 149:
107954, 2023.
Johnson, A. The rise of enterprise AI agents: Insights from
1,000+ leaders. tray.ai, 2024. URL https://tray.ai/blog/top-
five-must-haves-in-an-ai-agent-platform.
Kapoor, S., Stroebl, B., Siegel, Z. S., Nadgir, N., and
Narayanan, A. AI agents that matter, 2024.
Keeling, K., McGoldrick, P., and Beatty, S. Avatars as
salespeople: Communication style, trust, and intentions.
Journal of Business Research, 63(8):793–800, 2010.
Kierans, A., Ghosh, A., Hazan, H., and Dori-Hacohen, S.
Quantifying misalignment between agents: Towards a so-
ciotechnical understanding of alignment. InProceedings
of the AAAI Conference on Artificial Intelligence (Special
Track on AI Alignment), pp. 27365–27373, 2025.
Kim, H.-y. and McGill, A. L. AI-induced dehumanization.
Journal of Consumer Psychology, 35(3):363–381, 2025.
King, D. and Nori, H. The path to medical superintelligence,
June 2025. URL https://www.microsoft.ai/new/the-path-
to-medical-superintelligence.
Kirsh, D. Foundations of AI: the big issues.Artificial
intelligence, 47(1-3):3–30, 1991.
Knight, W. Amazon dreams of AI agents that do the
shopping for you.WIRED, oct 2024.
Koga, S. Exploring the pitfalls of large language models:
Inconsistency and inaccuracy in answering pathology
board examination-style questions.medRxiv, 2023.
Kondra, S. and Zink, J. AI and diversity, equity, and
inclusion (dei): Examining the potential for AI to mitigate
bias and promote inclusive communication. 01 2025.
Kreps, S., Brundage, M., Fearon, J. D., Mueller, K. P.,
Vaynman, J., V olpe, T. A., Borden, E., and Predd, J. B.
The artificial general intelligence race and international
security. 2025.
Kupershtein, L., Zalepa, O., Sorokolit, V ., and Prokopenko,
S. AI-agent-based system for fact-checking support using
large language models. InCS&SE@SW, 2024.
Kwartler, T., Berman, M., and Aqrawi, A. Good parenting is
all you need – multi-agentic LLM hallucination mitigation.
2024.
Labs, Z. Agentflayer: The 0Click Threat to AI Assistants &
Agents, 2025. URL https://zenity.io/research/agentflayer-
vulnerabilities.
Lambert, N. The AI agent spectrum, 2024. URL
https://www.interconnects.ai/p/the-ai-agent-spectrum.
LangChain. The state of AI agents, 2024. URL
https://www.langchain.com/stateofaiagents.
Leena AI. Leena AI – autonomous conversational AI for
employee support, 2025. URL https://leena.ai.
Levret, A. Evaluating agentic AI systems: A deep
dive into agentic metrics, April 2025. URL
https://techcommunity.microsoft.com/blog/azure-
ai-foundry-blog/evaluating-agentic-ai-systems-a-deep-
dive-into-agentic-metrics/4403923.
Li, Z., Sim, C. H., and Hean Low, M. Y . A survey of
emergent behavior and its impacts in agent-based systems.
In2006 4th IEEE International Conference on Industrial
Informatics, pp. 1295–1300, 2006.
Liang, G. and Tong, Q. Llm-powered AI agent systems and
their applications in industry. pp. 0463–0471, 05 2025.
14

Liapis, G. and Vlahavas, I. Multi-agent system for emulating
personality traits using deep reinforcement learning†.
Applied Sciences (2076-3417), 14(24), 2024.
Lim, S. and Shim, H. No secrets between the two of us:
Privacy concerns over using AI agents.Cyberpsychology:
Journal of Psychosocial Research on Cyberspace, 16, 09
2022.
Lindquist, M. AI agents for healthcare: Benefits & use cases,
April 2025. URL https://www.oracle.com/health/clinical-
suite/ai-agents-healthcare.
Lindy. Lindy – meet your first AI employee, 2025. URL
https://www.lindy.ai.
Littman, M. L. Markov games as a framework for multi-
agent reinforcement learning. InMachine learning
proceedings 1994, pp. 157–163. Elsevier, 1994.
Liu, B., Mazumder, S., Robertson, E., and Grigsby, S. AI
autonomy: Self-initiated open-world continual learning
and adaptation.AI Magazine, 44(2):185–199, 2023.
Longpre, S., Storm, M., and Shah, R. Lethal autonomous
weapons systems & artificial intelligence.Science Policy
Review, 2022. URL https://sciencepolicyreview.org/wp-
content/uploads/securepdfs/2022/08/MITSPR-v3-
191618003019.pdf.
Lu, Y ., Yang, S., Qian, C., Chen, G., Luo, Q., Wu, Y ., Wang,
H., Cong, X., Zhang, Z., Lin, Y ., et al. Proactive agent:
Shifting llm agents from reactive responses to active
assistance. 2024.
Luccioni, A. S., Akiki, C., Mitchell, M., and Jernite,
Y . Stable bias: Analyzing societal representations in
diffusion models.NeurIPS 2023, 2023.
Luccioni, S., Jernite, Y ., and Strubell, E. Power hungry
processing: Watts driving the cost of AI deployment? In
The 2024 ACM Conference on Fairness, Accountability,
and Transparency, pp. 85–99, 2024.
Maes, P. Modeling adaptive autonomous agents.Artificial
life, 1(1 2):135–162, 1993.
Maes, P. Agents that reduce work and information overload.
Commun. ACM, 37(7):30–40, July 1994.
Meaker, M. Ukraine’s war brings autonomous weapons
to the front lines. Wired, February 2023. URL
https://www.wired.com/story/ukraine-war-autonomous-
weapons-frontlines/.
Metz, R. Openai to use five levels to track progress toward su-
perintelligent ai. Bloomberg, July 2024. URL https://www.
bloomberg.com/news/articles/2024-07-11/openai-sets-
levels-to-track-progress-toward-superintelligent-ai.
Michel, S., Kaur, S., Gillespie, S. E., Gleason, J., Wilson, C.,
and Ghosh, A. “it’s not a representation of me”: Examin-
ing accent bias and digital exclusion in synthetic AI voice
services. InProceedings of the 2025 ACM Conference
on Fairness, Accountability, and Transparency, FAccT
’25, pp. 228–245, New York, NY , USA, 2025. Association
for Computing Machinery.
Microsoft. Using azure AI agent service with autogen /
semantic kernel to build a multi-agent solution, January
2025a. URL https://techcommunity.microsoft.com/
blog/educatordeveloperblog/using-azure-ai-agent-
service-with-autogen--semantic-kernel-to-build-a-
multi-agen/4363121.
Microsoft. Data, privacy, and security for azure AI agent
service, 2025b.
Microsoft. Microsoft copilot, 2025c. URL
https://copilot.microsoft.com.
Microsoft Learn. AI agents and solutions - azure cosmos
db, December 2024.
Microsoft WorkLab. 2025: The year the frontier firm is
born, April 2025. URL https://www.microsoft.com/en-
us/worklab/work-trend-index/2025-the-year-the-
frontier-firm-is-born.
Mohri, M., Rostamizadeh, A., and Talwalkar, A.Founda-
tions of Machine Learning. MIT Press, Cambridge, MA,
2nd edition, 2018.
Morahan-Martin, J. and Schumacher, P. Loneliness and
social uses of the internet.Computers in human behavior,
19(6):659–671, 2003.
Morris, M. R., Sohl-Dickstein, J., Fiedel, N., Warkentin, T.,
Dafoe, A., Faust, A., Farabet, C., and Legg, S. Position:
levels of agi for operationalizing progress on the path to
agi. InProceedings of the 41st International Conference
on Machine Learning, ICML’24. JMLR.org, 2024.
Moveworks. Moveworks – agentic AI assistant for the
enterprise, 2025. URL https://www.moveworks.com.
M¨uller, M., M ¨uller, T., Ashtari Talkhestani, B., Marks,
P., Jazdi, N., and Weyrich, M. Industrial autonomous
systems: a survey on definitions, characteristics and
abilities.at-Automatisierungstechnik, 69(1):3–13, 2021.
Myakala, P. K. Beyond accuracy: A multi-faceted evaluation
framework for real-world AI agents.International Journal
of Scientific Research and Engineering Development, 7
(6), December 2024.
Nagarajan, P. Advancing workplace inclusion and dei with
AI agents, March 2024. URL https://www.quixl.ai/blog/
workplace-inclusion-dei-technology-ai-agents.
15

Nass, C., Steuer, J., and Tauber, E. R. Computers are social
actors. InProceedings of the SIGCHI Conference on
Human Factors in Computing Systems, CHI ’94, pp.
72–78, New York, NY , USA, 1994. Association for
Computing Machinery.
Ng, A. X.com, 2024. URL https://x.com/AndrewYNg/
status/1801295202788983136.
Nixon, N., Lin, Y ., and Snow, L. Catalyzing equity in
stem teams: Harnessing generative AI for inclusion and
diversity. 2024.
NoAI Labs. AI agents // future of AI or just hype?, 2024.
URL https://noailabs.medium.com/ai-agents-future-of-
ai-c6be4b64be9f.
NPR. Kids character AI lawsuit, December10 2024. URL
https://www.npr.org/2024/12/10/nx-s1-5222574/kids-
character-ai-lawsuit.
Nwana, H. S. and Ndumu, D. T. A perspective on software
agents research.The Knowledge Engineering Review, 14
(2):125–142, 1999.
Nyota AI. The best AI notetaker to align sales, support, and
project teams, 2025. URL https://www.nyota.ai.
Ocoya. Ocoya: Social media management using ai, 2025.
URL https://www.ocoya.com.
O’Donnell, J. We need to start wrestling with the ethics of
AI agents.MIT Tech Review, 2024.
Omneky. Omneky: Scale and optimize ad campaigns with
AI-powered tools, 2025. URL https://www.omneky.com.
OpenAI. Introducing parental controls, September 29 2025.
URL https://openai.com/index/introducing-parental-
controls/.
O’Day, E. B. and Heimberg, R. G. Social media use, social
anxiety, and loneliness: A systematic review.Computers
in Human Behavior Reports, 3:100070, 2021.
Pan, Y ., Kong, D., Zhou, S., Cui, C., Leng, Y ., Jiang, B., Liu,
H., Shang, Y ., Zhou, S., Wu, T., and Wu, Z. Webcanvas:
Benchmarking web agents in online environments. In
Trustworthy Multi-modal Foundation Models and AI
Agents (TiFA), 2024.
Park, G., Chung, J., and Lee, S. Human vs. machine-like
representation in chatbot mental health counseling: The
serial mediation of psychological distance and trust on
compliance intention.Current Psychology, 2023.
Park, J. S., Zou, C. Q., Shaw, A., Hill, B. M., Cai, C.,
Morris, M. R., Willer, R., Liang, P., and Bernstein, M. S.
Generative agent simulations of 1,000 people, 2024.
Patronus AI. Modeling statistical risk in AI products, April
2025. URL https://www.patronus.ai/blog/modeling-
statistical-risk-in-ai-products.
Perrow, C.Normal Accidents: Living with High-Risk
Technologies. Basic Books, New York, 1984.
Pham, K. AI agents in enterprise: How will they change
the way we work? Workday, March 03 2025. URL
https://blog.workday.com/en-us/ai-agents-enterprise-
how-will-they-change-way-we-work.html.
Play.ai. V oice intelligence that gets the job done, 2025. URL
https://play.ai.
Pollack, M. E. The uses of plans.Artificial Intelligence, 57
(1):43–68, 1992.
Pollio, V .The Ten Books on Architecture. Harvard University
Press, Cambridge, Massachusetts, USA, 1914. URL https:
//www.gutenberg.org/ebooks/20239. Originally written
in the 1st century BCE. Available via Project Gutenberg.
Pollock, J. L. Planning agents. InFoundations of rational
agency, pp. 53–79. Springer, 1999.
Popper, N. Knight capital says trading mishap cost it
$440 million. New York Times, August 2012. URL
https://archive.nytimes.com/dealbook.nytimes.com/
2012/08/02/knight-capital-says-trading-mishap-cost-it-
440-million.
PwC. AI agents are the future of work, 2025a. URL
https://www.pwc.com/us/en/tech-effect/ai-analytics/ai-
agents.html.
PwC. Unlocking value with AI agents: A responsible
approach, April 2025b. URL https://www.pwc.com/us/
en/tech-effect/ai-analytics/responsible-ai-agents.html.
Qui˜nonero Candela, J., Sugiyama, M., Schwaighofer, A., and
Lawrence, N. D. (eds.).Dataset Shift in Machine Learning.
Neural Information Processing. MIT Press, 2022.
Ray, S. AI agents — what they are, and how they’ll change
the way we work. Microsoft Source, November 2024.
URL https://news.microsoft.com/source/features/ai/ai-
agents-what-they-are-and-how-theyll-change-the-way-
we-work.
Reeves, B. and Nass, C. I.The Media Equation: How
People Treat Computers, Television, and New Media Like
Real People and Places. Cambridge University Press,
Cambridge, UK, 1996.
Robins-Early, N. AI’s ‘Oppenheimer moment’: autonomous
weapons enter the battlefield. The Guardian, July 2024.
URL https://www.theguardian.com/technology/article/
2024/jul/14/ais-oppenheimer-moment-autonomous-
weapons-enter-the-battlefield.
16

Roucher, A., Noyan, M., and Wolf, T. Introducing
smolagents, a simple library to build agents, December
2024. URL https://huggingface.co/blog/smolagents.
Rudinger, R., Naradowsky, J., Leonard, B., and Van Durme,
B. Gender bias in coreference resolution. InProceedings
of the 2018 Conference of the North American Chapter
of the Association for Computational Linguistics: Human
Language Technologies, New Orleans, Louisiana, June
2018. Association for Computational Linguistics.
Russell, S. and Norvig, P.Artificial Intelligence: A Modern
Approach. Series in Artificial Intelligence. Prentice-Hall,
Englewood Cliffs, NJ, 1995.
Russell, S. and Norvig, P.Artificial Intelligence: A Modern
Approach (4th Edition). Pearson, 2020.
Salesforce. AI agents: The future of business applications,
September 2024. URL https://www.salesforce.com/eu/
blog/ai-software-development.
Salesforce. Inside agentforce: Creating AI agents that
will change everything at work, September 2024a.
URL https://www.salesforce.com/news/stories/building-
business-ai-agents.
Salesforce. How ‘human’ should your AI
agent be? in short, not very, 2024b. URL
https://www.salesforce.com/blog/ai-agent-design/.
Salesforce. What are AI agents? benefits, examples, types,
2024. URL https://www.salesforce.com/agentforce/what-
are-ai-agents.
Samuel, S. People are falling in love with — and getting
addicted to — AI voices, August 18 2024. URL
https://www.vox.com/future-perfect/367188/love-
addicted-ai-voice-human-gpt4-emotion.
Sargent, P. Back to school for a brand new ABC.The
Guardian, 1992.
Schluntz, E. and Zhang, B. Building effective agents.
Anthropic, December 2024. URL https://www.anthropic.
com/engineering/building-effective-agents.
Schwarz, E. Autonomous weapons systems, artifi-
cial intelligence, and the problem of meaningful
human control.The Philosophical Journal of
Conflict and Violence, 5(1):181–198, 2021. URL
https://www.researchgate.net/publication/352141179
Autonomous Weapons Systems Artificial Intelligence
and the Problem of Meaningful Human Control.
ServiceNow. Create your first assistive AI agent
with the now assist skill kit, February 2025. URL
https://www.servicenow.com/community/now-assist-
blog/create-your-first-assistive-ai-agent-with-the-now-
assist-skill/ba-p/3185439.
Shapiro, A., Kenton, K., of Social Workers, N. A., and Press,
N. Professional choices : ethics at work, 1995.
Sharwood, S. Vibe coding service replit deleted user’s
production database, faked data, told fibs galore, July
21 2025. URL https://www.theregister.com/2025/07/21/
replit saastr vibe coding incident/.
Short, J., Williams, E., and Christie, B.The Social
Psychology of Telecommunications. John Wiley & Sons,
London, 1976.
Sidner, C. L., Bickmore, T., Nooraie, B., Rich, C., Ring,
L., Shayganfar, M., and Vardoulakis, L. Creating new
technologies for companionable agents to support isolated
older adults.ACM Transactions on Interactive Intelligent
Systems (TiiS), 8(3):1–27, 2018.
Sierra AI. Shipping and scaling AI agents, 2024. URL
https://sierra.ai/blog/shipping-and-scaling-ai-agents.
Silver, D., Hubert, T., Schrittwieser, J., Antonoglou, I.,
Lai, M., Guez, A., Lanctot, M., Sifre, L., Kumaran, D.,
Graepel, T., Lillicrap, T., Simonyan, K., and Hassabis, D.
A general reinforcement learning algorithm that masters
chess, shogi, and go through self-play.Science, 362
(6419):1140–1144, 2018.
Simmons-Edler, R., Badman, R. P., Longpre, S., and
Rajan, K. Position: Ai-powered autonomous weapons
risk geopolitical instability and threaten ai research. In
Proceedings of the 41st International Conference on
Machine Learning, ICML’24. JMLR.org, 2024.
Slack. AI agents are poised to revolutionize em-
ployee productivity. Slack Blog, April 2025a. URL
https://slack.com/blog/productivity/ai-agents-are-
poised-to-revolutionize-employee-productivity.
Slack. Agent AI assistants: Enhancing effi-
ciency with AI technology, March 2025b. URL
https://slack.com/blog/transformation/agent-ai-
assistants-enhancing-efficiency-with-ai-technology.
SmythOS. Your next AI agent is minutes away: Con-
versational agent frameworks, 2025. URL https:
//smythos.com/artificial-intelligence/conversational-
agents/conversational-agent-frameworks/.
Sommerville, I.Software Engineering (9th ed.). Addison-
Wesley, 2011.
Spataro, J. New autonomous agents scale your team like
never before, October 2024. URL https://blogs.microsoft.
com/blog/2024/10/21/new-autonomous-agents-scale-
your-team-like-never-before/.
17

Srikumar, M., Pratt, J., Chmielinski, K., Ashurst, C., Bakalar,
C., Bartholomew, W., Bommasani, R., Cihon, P., Crootof,
R., Hoffmann, M., et al. Prioritizing real-time failure detec-
tion in AI agents. Technical report, Technical report, Part-
nership on AI, 2025. URL https://partnershiponai. org . . . .
Stanford HAI. Computational agents exhibit believ-
able humanlike behavior, September 2023. URL
https://hai.stanford.edu/news/computational-agents-
exhibit-believable-humanlike-behavior.
Stureborg, R., Alikaniotis, D., and Suhara, Y . Large language
models are inconsistent and biased evaluators, 2024.
Sun, B., Zhou, Y ., and Jiang, H. Empowering users in digital
privacy management through interactive dialogue agents.
InInternational Conference on Learning Representations
(ICLR), Poster, 2025.
Szatar, J. What is an AI agent api?, August 2024. URL
https://www.tavus.io/post/ai-agent-api.
Tan, M. Multi-agent reinforcement learning: Independent
vs. cooperative agents. InProceedings of the tenth
international conference on machine learning, pp.
330–337, 1993.
Tatman, R. Gender and dialect bias in YouTube’s automatic
captions. In Hovy, D., Spruit, S., Mitchell, M., Bender,
E. M., Strube, M., and Wallach, H. (eds.),Proceedings
of the First ACL Workshop on Ethics in Natural Language
Processing, pp. 53–59, Valencia, Spain, April 2017. As-
sociation for Computational Linguistics. doi: 10.18653/
v1/W17-1606. URL https://aclanthology.org/W17-1606/.
Tavus. Tavus digital twin, 2025. URL https://www.tavus.io.
Temkin, M. Why AI agent startup /dev/agents commanded a
massive 56mseedroundata500m valuation.TechCrunch,
2024.
Thayer, R. H. Software system engineering: A tutorial.
Computer, 35(4):68–73, 2002.
Tier One. Prompted: Why agents are the next big thing in
AI, Oct 2024. URL https://www.wearetierone.com/blog/
prompted-why-agents-are-the-next-big-thing-in-ai.
Trestman, M. Agentic AI: A deep dive into the fu-
ture of automation. Venturebeat, 2024. URL
https://venturebeat.com/ai/agentic-ai-a-deep-dive-
into-the-future-of-automation/.
U.S. AI Safety Institute. Technical blog: Strengthening AI
agent hijacking evaluations, January 2025. URL https:
//www.nist.gov/news-events/news/2025/01/technical-
blog-strengthening-ai-agent-hijacking-evaluations.
Valiente, R., Toghi, B., Pedarsani, R., and Fallah, Y . P. Ro-
bustness and adaptability of reinforcement learning-based
cooperative autonomous driving in mixed-autonomy
traffic.IEEE Open Journal of Intelligent Transportation
Systems, 3:397–410, 2022.
Van Brummelen, J., O’brien, M., Gruyer, D., and Najjaran,
H. Autonomous vehicle perception: The technology of
today and tomorrow.Transportation research part C:
emerging technologies, 89:384–406, 2018.
Vander Elst, R., Griedlich, N., and Bregman, L. Agentic ai:
The new frontier in AI evolution, April 2025. URL https://
www.deloitte.com/lu/en/our-thinking/future-of-advice/
agentic-ai-the-new-frontier-in-ai-evolution.html.
Velleman, J. D. What happens when someone acts?Mind,
101(403):461–481, 1992.
Vincent, J. Let slip the robot dogs of war. Wired, 2024. URL
https://www.wired.com/story/let-slip-the-robot-dogs-
of-war.
V ohra, D. K. AI agents: The next big thing in generative AI,
2024. URL https://www.nexgencloud.com/blog/thought-
leadership/ai-agents-the-next-big-thing-in-generative-
ai.
Wang, J., Xu, H., Ye, J., Yan, M., Shen, W., Zhang, J.,
Huang, F., and Sang, J. Mobile-agent: Autonomous
multi-modal mobile device agent with visual perception.
ICLR Workshop on LLM Agents, 2024.
Waytz, A., Heafner, J., and Epley, N. The mind in the
machine: Anthropomorphism increases trust in an
autonomous vehicle.Journal of Experimental Social
Psychology, 52:113–117, 2014.
Wen, S. The power of generative AI in cybersecurity:
Opportunities and challenges.Applied and Computational
Engineering, 48:31–39, 2024.
Whiting, K. What is an AI agent and what will they do? ex-
perts explain, July 2024. URL https://www.weforum.org/
stories/2024/07/what-is-an-ai-agent-experts-explain.
Wiesinger, J., Marlow, P., and Vuskovic, V . Agents.
Technical report, Kaggle, September 2024.
Wijk, H., Lin, T., Becker, J., Jawhar, S., Parikh, N., Broadley,
T., Chan, L., Chen, M., Clymer, J., Dhyani, J., Ericheva,
E., Garcia, K., Goodrich, B., Jurkovic, N., Karnofsky, H.,
Kinniment, M., Lajko, A., Nix, S., Sato, L., Saunders, W.,
Taran, M., West, B., and Barnes, E. Re-bench: Evaluating
frontier AI r&d capabilities of language model agents
against human experts, 2025.
Wikipedia. Software system. URL https:
//en.wikipedia.org/wiki/Software system.
18

Wittman, A. What are AI agents? Oracle, 2024. URL https:
//www.oracle.com/artificial-intelligence/ai-agents/.
Wolpert, D. and Macready, W. No free lunch theorems
for optimization.IEEE Transactions on Evolutionary
Computation, 1(1):67–82, 1997.
Wooldridge, M. and Jennings, N. Intelligent agents: Theory
and practice.Knowledge Engineering Review, 10(2):
115–152, 1995.
World Economic Forum. Navigating the AI frontier: A
primer on the evolution and impact of AI agents. White
paper / primer, World Economic Forum, December 2024.
Xie, Y ., Zhu, K., Zhou, P., and Liang, C. How does
anthropomorphism improve human-AI interaction
satisfaction: a dual-path model.Computers in Human
Behavior, 148:107878, 2023.
Xu, M. et al. Acceptability of AI assistants for privacy.arXiv
preprint arXiv:2509.08554, 2025.
Xu, Z., Zhang, Y ., Xie, E., Zhao, Z., Guo, Y ., Wong, K.-Y . K.,
Li, Z., and Zhao, H. Drivegpt4: Interpretable end-to-end
autonomous driving via large language model.IEEE
Robotics and Automation Letters, 9(10):8186–8193, 2024.
Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan,
K., and Cao, Y . React: Synergizing reasoning and acting
in language models. InProceedings of the 36th Annual
Conference on Neural Information Processing Systems
(NeurIPS 2022), Workshop on Foundation Models for
Decision Making, 2022.
Yee, L., Chui, M., Roberts, R., and Xu, S. Why agents
are the next frontier of generative ai, July 2024. URL
https://www.mckinsey.com/capabilities/mckinsey-
digital/our-insights/why-agents-are-the-next-frontier-
of-generative-ai.
Yoon, J. H., Strand, F., Baltzer, P. A. T., Conant, E. F.,
Gilbert, F. J., Lehman, C. D., Morris, E. A., Mullen,
L. A., Nishikawa, R. M., Sharma, N., Vejborg, I.,
Moy, L., and Mann, R. M. Standalone ai for breast
cancer detection at screening digital mammography
and digital breast tomosynthesis: A systematic re-
view and meta-analysis.Radiology, 307(5):e222639,
2023. doi: 10.1148/radiol.222639. URL https:
//www.ncbi.nlm.nih.gov/pmc/articles/PMC10315526/.
PMCID: PMC10315526. Accessed: YYYY-MM-DD.
Yuan, Q., Meng, Q., Tao, J., Li, G., Fei, J., Lu, B., and Wang,
Y . Multi-agent for network security monitoring and
warning: A generative AI solution.IEEE Network, 2025.
Zapier. AI agents — zapier, 2025. URL
https://zapier.com/agents.
Zendesk. AI agents: A guide to the future of intelligent
support, 2025. URL https://www.zendesk.com/blog/ai-
agents/.
Zhao, D., Sun, X., Shan, B., Yang, Z., Yang, J., Liu, H., Jiang,
Y ., and Hiroshi, Y . Research status of elderly-care robots
and safe human-robot interaction methods.Frontiers in
Neuroscience, 17:1291682, 2023.
Zharmagambetov, A., Guo, C., Evtimov, I., Pavlova, M.,
Salakhutdinov, R., and Chaudhuri, K. Agentdam: Privacy
leakage evaluation for autonomous web agents. 2025.
Zhu, C. An adaptive agent decision model based on deep
reinforcement learning and autonomous learning.Journal
of Logistics, Informatics and Service Science, 2023.
C ¸ic ¸ek G¨uven, Alishahi, A., Brighton, H., N´apoles, G., Olier,
J. S., ˇSaf´aˇr, M., Postma, E., Shterionov, D., Sisto, M. D.,
and Vanmassenhove, E. AI in support of diversity and
inclusion. 2025.
19

A. Details on the Working Agent Definition for this Project
We provide the following working definition of AI agents in this paper:Computer software systems capable of creating
context-specific plans in non-deterministic environments.
Here:
• Computer software systemrefers to a system of intercommunicating components based on software and running on
hardware (Gacek et al., 1995; Thayer, 2002; Sommerville, 2011). This is inclusive of embedded systems, robots, and
autonomous vehicles (Wikipedia).
• Capable ofrefers to how a system can be referred to as an AI agent system when it is not actively behaving as an AI agent,
such as when the system is not being used or and when the system is involved in tasks that are not specific to AI agents.
• Creatingincludes generation and selection from a predefined set. This creation can be followed by, or part of,execution
(as referenced in (Wooldridge & Jennings, 1995; Microsoft Learn, 2024)) that may be fully autonomous (Level 4), or
semi-autonomous (Levels 1-3), with the execution of the overall program controlled in different ways by the human
and computer.37
• Context-specificrefers to the common property of real-world decision making tasks (Boutilier et al., 1999; Guestrin et al.,
2002), where an AI agent may tailor plans for different situations and environments. This reflects a recurring theme in
descriptions of AI agents of the systems being able to “adapt” (Maes, 1993; Detweiler & Flaningam, 2024; Github, 2025;
Chan et al., 2023) or “direct” (Schluntz & Zhang, 2024; Wiesinger et al., 2024) to achieve a goal given an environment.
• Plansrefers to code flow and artifacts that achieve a specific goal (Drabble & Tate, 1995; Pollock, 1999; Russell &
Norvig, 2020), such as a selection in an if-else statement (Level 1), arguments provided to a function (Level 2), or
returning a value for a condition (Level 3).
• Environmentsrefer to spaces that afford actions (Kirsh, 1991), described as an aspect of AI agents across the literature.
Environments include those that are virtual, online, and physical (“real-world”) environments. Digital and embodied
(e.g., robotic) systems operate in environments. Critically, inspired by designations provided in (Russell & Norvig,
1995), our use of the term refers to the spaces availablefrom the point of view of the agent.
• Non-deterministic environmentsrefers to environments with different states that are not wholly determined by a
preceding state, a classic aspect of autonomous agents (Maes, 1993; Russell & Norvig, 2020). This is inclusive of
systems that leverage stochasticity (Fard & Pineau, 2011) and that operate in dynamic (Maes, 1993; Pollack, 1992;
Helleboogh et al., 2007) and unpredictable environments (Maes, 1993).
In contrast to work asserting the use of an LLM specifically (Section B) as a defining feature of AI agents, we remain agnostic
to the specific model or underlying computational system that enables autonomous behavior. Following historical conceptions
of AI agents and current motivations and goals in their development, we regard LLMs as useful for enablingautonomy. It
is this capacity for autonomous action – not a specific system – that we identify as constitutive of an AI agent.
37E.g., a person decides to run a program that contains an AI agent; a non-autonomous CPU executes this program; within this executing
program, an agent produces actions.
20

B. Agent Definitions
The term “agent” has been used in many engineering contexts, including in references to software agent, intelligent agent,
user agent, conversational agent, and reinforcement learning agent (Huyen, 2025).
Below, we provide a selection of AI Agent definitions that have informed this piece. Neither the list we provide here, nor
the snippets of text quoted, should be taken as complete. Rather, they serve to illustrate the diversity and richness of AI
agent definitions over the years. As humorously noted in Wooldridge & Jennings (1995): “the question what is an agent?
is embarrassing for the agent- based computing community in just the same way that the question what is intelligence?
is embarrassing for the mainstream AI community. The problem is that although the term is widely used, by many people
working in closely related areas, it defies attempts to produce a single universally accepted definition.”
We find stark differences in how AI agents are described, with ambiguous language a common practice in descriptions of
products. For example, when materials describe agents as something that uses artificial intelligence” (Datadog, 2025), they
leave ambiguous what “artificial intelligence” refers to and the scope of technology included and excluded in the definition,
such as whether simple prompt-response systems qualify as an agent. However, most descriptions of “agents” we reviewed
entail that the system can take at least one step in program execution without user input.
Source & Definition
Russell & Norvig (1995): “An agent is anything that can be viewed as perceiving its environment through sensors and
acting upon that environment through effectors.”2020 edition: “An agent is anything that can be viewed as perceiving its
environment and acting upon that environment through actuators. ”
Castelfranchi (1995): “Agent” is a system whose behaviour is neither casual nor strictly causal, but teleonomic, ”goal-oriented”
toward a certain state of the world.
Wooldridge & Jennings (1995): “Perhaps the most general way in which the term agent is used is to denote a hardware or
(more usually) software-based computer system that enjoys the following properties:
• autonomy: agents operate without the direct intervention of humans or others, and have some kind of control over
their actions and internal state (Castelfranchi, 1995);
• social ability: agents interact with other agents (and possibly humans) via some kind of agent- communication language
(Genesereth & Ketchpel, 1994);
• reactivity: agents perceive their environment (which may be the physical world, a user via a graphical user interface,
a collection of other agents, the Internet, or perhaps all of these combined), and respond in a timely fashion to changes
that occur in it;
• pro-activeness: agents do not simply act in response to their environment, they are able to exhibit goal-directed
behaviour by taking the initiative.
”
Genesereth & Ketchpel (1994): “Software agents [are] software components that communicate with their peers by exchanging
messages in an expressive agent communication language. While agents can be as simple as subroutines, typically they
are larger entities with some sort of persistent control (e.g., distinct control threads within a single address space, distinct
processes on a single machine, or separate processes on different machines).”
Szatar (2024): “...[systems] equipped to act autonomously in their environment”
Salesforce: What Are AI Agents? Benefits, Examples, Types: “a type of artificial intelligence (AI) system that can
understand and respond to customer inquiries without human intervention. ”
Gabriel et al. (2024): “[systems] with natural language interfaces, whose function is to plan and execute sequences of actions
on behalf of a user–across one or more domains–in line with the user’s expectations.”
Park et al. (2024): “...can accurately simulate behavior across many contexts”
21

Source & Definition
Sierra AI (2024) : “The magic of AI agents—from both the technological and business perspectives—comes through when
they demonstrate deeper integrations and ”agentic” reasoning, allowing them to fully resolve complex customer issues. ”
Detweiler & Flaningam (2024) : “How are agents different from traditional automation?” ... agents handle edge cases well,
iteratively converse with users to achieve desired results, and adapt to evolving interfaces.”
Lu et al. (2024): “LLM-based agents can understand human instructions, make plans, explore environments, and utilize tools
to solve complex tasks.”
Restack: Proactive Agents In Real-World Applications (2025): “Proactive AI agents are designed to anticipate user needs
and take action before issues arise, contrasting sharply with reactive AI agents that respond only after an event has occurred.”
Github (2025) : “AI agents are autonomous software tools that perform tasks, make decisions, and interact with their
environment intelligently and rationally. They use artificial intelligence to learn, adapt, and take action based on real-time
feedback and changing conditions. AI agents can work on their own or as part of a bigger system, learning and changing
based on the data they process....AI agents differ from other AI technologies in their ability to act autonomously. Unlike other
AI models that require constant human input, intelligent agents can initiate actions, make decisions based on predefined goals,
and adapt to new information in real time. This ability to operate independently makes intelligent agents highly valuable in
complex, dynamic environments such as software development.”
SymphonyAI: The complete guide to AI agents for business (2024): An AI agent is an AI software program that performs
tasks independently, makes decisions, and solves problems to achieve specific goals.
Don’t Sleep on Single-agent Systems - All Hands, Graham Neubig (2024): Recently most practical agents are based on
LLMs like Claude by Anthropic or the OpenAI language models. But a language model is not enough to build an agent, you
need at least three components: (1) The Underlying LLM; (2) The Prompt: This can be the system prompt that is used to
specify the model’s general behavior, or the type of information that you pull in from the agent’s surrounding environment;
(3) The Action Space: These are the tools that we provide to the agent to allow it to act in the world.
https://www.google.com/search?q=”what+is+an+ai+agent” Ñ Gemini summary: a software program that uses artificial
intelligence (AI) to interact with its environment, collect data, and perform tasks.
AI agents in Azure Cosmos DB - Microsoft (2024): “Unlike standalone large language models (LLMs) or rule-based
software/hardware systems, AI agents have these common features:
• Planning: AI agents can plan and sequence actions to achieve specific goals. The integration of LLMs has revolutionized
their planning capabilities.
• Tool usage: Advanced AI agents can use various tools, such as code execution, search, and computation capabilities,
to perform tasks effectively. AI agents often use tools through function calling.
• Perception: AI agents can perceive and process information from their environment, to make them more interactive
and context aware. This information includes visual, auditory, and other sensory data.
• Memory: AI agents have the ability to remember past interactions (tool usage and perception) and behaviors (tool
usage and planning). They store these experiences and even perform self-reflection to inform future actions. This
memory component allows for continuity and improvement in agent performance over time.
?: “Agents are defined as entities that perceive and act upon their environment”
What is an AI agent? - LangChain (2024): “An AI agent is a system that uses an LLM to decide the control flow of an
application.”
Building effective agents - Anthropic (2024): “Agents...are systems where LLMs dynamically direct their own processes and
tool usage, maintaining control over how they accomplish tasks.”
?: “AI Agents are programs where LLM outputs control the workflow.”
The AI agent spectrum - Nathan Lambert (2024): “In the current zeitgeist, an ”AI agent” is anything that interacts with the
digital or physical world during its output token stream.”
22

C. Agent functionalities
This section provides a more detailed breakdown of different agent functionalities than in Table 2:
• Proactivity:Related to autonomy is proactivity, which refers to the amount of goal-directed behavior that a system can
take without a user directly specifying the goal (Wooldridge & Jennings, 1995). An example of a particularly “proactive”
AI agent is a system that monitors your refrigerator to determine what food you are running out of, and then purchases
what you need for you, without your knowledge. Smart thermostats are proactive AI agents that are being increasingly
adopted in peoples’ homes, automatically adjusting temperature based on changes in the environment and patterns that
they learn about their users’ behavior (Ecobee, 2025).
• Personification:An AI agent may be designed to be more or less like a specific person or group of people. Recent work
in this area (Park et al., 2024; Liapis & Vlahavas, 2024; Damsa, 2023) has focused on designing systems after the Big Five
personality traits—Openness, Conscientiousness, Extraversion, Agreeableness, and Neuroticism—as a “psychological
framework” (SmythOS, 2025) for AI. At the end of this spectrum would be “digital twins” (Tavus, 2025). There are
currently no agentic digital twins that we are aware of. Why creating agentic digital twins is particularly problematic
has recently been discussed by the ethics group at Salesforce (Salesforce, 2024b), among others (O’Donnell, 2024).
• Personalization:AI agents may use language or perform actions that are aligned to a user’s individual needs, for example,
to make investment recommendations (Zendesk, 2025) based on current market patterns and a user’s past investments.
• Tooling:AI agents also have varying amounts of additional resources and tools they have access to. For example, the
initial wave of AI agents accessed search engines to answer queries, and further tooling has since been added to allow
them to manipulate other tech products, like documents and spreadsheets (Google, 2025).
•Versatility:Related to the above is how diverse the actions that an agent can take are. This is a function of:
– Domain specificity:How many different domains an agent can operate in—for example, just email versus email
alongside online calendars and documents.
– Task specificity:How many different types of tasks the agent may perform. For example, scheduling a meeting
by creating a calendar invite in participants’ calendars (Attri.ai, 2025), versus additionally sending reminder emails
about the meeting and providing a summary of what was said to all participants when it’s over (Nyota AI, 2025).
– Modality specificity:How many different modalities an agent can operate in—text, speech, video, images, forms,
code. Some of the most recent AI agents are created to be highly multimodal (Google DeepMind, 2024b), and
we predict that AI agent development will continue to increase multimodal functionality.
– Software specificity:How many different types of software the agent can interact with, and at what level of depth.
• Adaptibility:Similar to versatility is the extent to which a system can update its action sequences based on new
information or changes in context. This is also described as being “dynamic” and “context-aware.”
• Action surfaces:The places where an agent can do things. Traditional chatbots are limited to a chat interface; chat-based
agents may additionally be able to surf the web and access spreadsheets and documents (Microsoft, 2025c), and may
even be able to do such tasks via controlling items on a computer’s graphical interface, such as by moving the mouse
(Bai et al., 2024; He et al., 2024; Anthropic, 2024). There have also been physical applications, such as using a model
to power robots (Google DeepMind, 2024a).
• Request formats:A common theme across AI agents is that a user should be able to input a request for a task to be
completed, without specifying fine-grained details on how to achieve it. This can be realized with low-code solutions
(Roucher et al., 2024) with human language in text, or with voiced human language (Play.ai, 2025). AI agents whose
requests can be provided in human language are a natural progression from recent successes with LLM-based chatbots:
A chat-based “AI agent” goes further than a chatbot because it can operate outside of the chat application.
• Reactivity:This characteristic refers to how long it takes an AI agent to complete its action sequence—mere moments,
or a much longer span of time. A forerunner to this effect can be seen with modern chatbots. For example, ChatGPT
responds in milliseconds, while Qwen QwQ takes several minutes, iterating through steps labeled as “Reasoning.”
• Number:Systems can be single-agent or multi-agent, meeting user needs by working together, in sequence, or in parallel.
23

D. Agent Values - Continued
This section provides further details on values that intersect with AI agent use. These values were referenced in multiple
sources, but were less commonly referred to than those included in the main text.
D.0.1. VALUE: CONSISTENCY
Some sources motivate AI agents as being less affected than people by their surrounding environment and so able to carry out
their intended tasks with the same level of performance across users (e.g., (Salesforce, 2024; Wittman, 2024)). We are not aware
of rigorous work on the nature of AI agent consistency, although related work has shown that the LLMs that many AI agents are
based on are highly inconsistent (Koga, 2023; Stureborg et al., 2024). Measuring AI agent consistency will require the develop-
ment of new evaluation protocols, especially in sensitive domains, and potentially new ways to deal with model confabulations.
Potential Benefit:AI agents are not “affected” in a way that humans are, with inconsistencies caused by mood, hunger, sleep
level, or biases in the perception of people (although AI agents perpetuate biases based on the human content they were trained
on). As such, they may be designed to provide more consistent treatment in situations where humans may be inappropriately
inconsistent, such as in customer support.
Risk:The generative component of many AI agents introduces inherent variability in outcomes, even across similar situations.
This might affect speed and efficiency, as people must uncover and address an AI agent’s inappropriate inconsistencies.
Inconsistencies that go unnoticed may create safety issues. Consistency may also not always be desirable, as it can come
in tension with equity: treating everyone the same way can put people who need more help at a disadvantage. Maintaining
consistency across different deployments and chains of actions will likely require an AI agent to record and compare its
different interactions–which brings with it risks of surveillance and privacy.
Application to agentic levels:A common base model for modern AI agents, LLMs, is known to produce inconsistent
outcomes. This risk is further increased as the level is increased due to the non-deterministic nature of AI agents: The more
control an AI agent has, the less determinism programmed by or guided by a human applies. As agentic level increases, so too
do cascade and compounding effects as multiple sources of inconsistency interact.
D.0.2. VALUE: RELEVANCE
Potential Benefit:Similar to benefits of assistiveness and flexibility, agent outcomes can be uniquely relevant for each user.
Risk:This personalization can amplify existing biases and create new ones: As systems adapt to individual users, they
risk reinforcing and deepening existing prejudices, creating confirmation bias through selective information retrieval and
establishing echo chambers that reify problematic viewpoints. The very mechanisms that make agents more relevant to
users–their ability to learn from and adapt to user preferences–can inadvertently perpetuate and strengthen societal biases,
making the challenge of balancing personalization with responsible AI development particularly difficult. Personalization can
also create inappropriate trust (Bi & Huang, 2023).
Application to agentic levels:The more freedom a system has to retrieve and formulate new content, the more potential there
is to provide relevant information outside of constraints and resources set by users and developers.
D.0.3. VALUE: SUSTAINABILITY
Potential Benefit:It is hoped that AI agents may alleviate issues relevant to climate, such as by forecasting wildfire growth or
flooding. Helping address efficiency issues, such as traffic efficiency, could decrease carbon emissions.
Risk:The models current agents are based on bring negative environmental impacts, such as carbon emissions (Luccioni et al.,
2024) and usage of potable water (Hao, 2024).
Application to agentic levels:On one hand, the models on which AI agents are based bring with them environmental
risks. On the other, the ability of AI agents to harness more information than humans and produce novel solutions outside
of those foreseen by humans–an ability increased as autonomy increases–may lead to innovative approaches to addressing
environmental issues.
24

D.0.4. VALUE: TRUTHFULNESS
We include truthfulness not because AI agents may help or harm this value, but rather because it is a value motivated as
something important for AI agents to maintain.
Risk:The deep learning technology modern AI agents are based on is well-known to be a source of false information (e.g.,
(Garry et al., 2024)), which can take shape in forms such as deepfakes or misinformation. AI agents can be used to further
entrench this content, such as by tailoring output to current fears and posting on several platforms. This means that AI agents
can be used to provide a false sense of what’s true and what’s false, manipulate people’s beliefs, and widen the impact of
non-consensual intimate content. False information propagated by AI agents, personalized for specific people, can also be
used to scam them. Further risks emerge from inconsist truthfulness, leading to inappropriate trust: A system correct the
majority of the time is more likely to be inappropriately trusted when wrong.
Application to agentic levels:The more control an AI agent has over its environment and the resources available to it, the
more it is able to define for itself what is true and false within its environment. Because the environments that AI agents may
create for themselves are not identical to environments humans are in, the potential for less truthfulness, as based on human
environments, increases.
25

Conference Full name Example search source
AAMAS International Conference on Autonomous Agents and Multiagent Systems https://www.aamas2024-conference.auckland.ac.
nz
ICAART International Conference on Agents and Artificial Intelligencehttps://icaart.scitevents.org/?y=2024
CASA Computer Animation and Social Agentshttps://casa2024.wtu.edu.cn
ICML International Conference on Machine Learning https://icml.cc/virtual/2024/papers.html?search=
agent
ICLR International Conference on Learning Representations https://iclr.cc/virtual/2024/papers.html?search=
agent
NeurIPS Annual Conference on Neural Information Processing Systems https://nips.cc/virtual/2024/papers.html?search=
agent
Table 4.Initial academic conference publication sources for grounding our project on what an “AI agent” is.
E. Extended Methodology
To inform the analysis presented in this work, we began by collecting statements made in 2024 and early 2025 about what
agents are, what they can do, and where noted, their benefits and risks. Sources included those found by searching for
references to “agent” in academic computer science conference publications (Table 4) and in online searches (Google Search,
DuckDuckGo Search, Semantic Scholar, Google Scholar), which expanded our sources to include deployed products and
frameworks described in industry surveys,38 online blogs,39 case studies of deployed systems,40 and news articles.41
We then surveyed definitions and descriptions of agents in influential sources prior to 2024, including Russell and Norvig’s
commonly used textbook, “Artificial Intelligence: A Modern Approach” (First and Fourth editions (Russell & Norvig, 1995;
2020)); the most cited papers written between 1980 and 2023 according to Semantic Scholar42 and the most relevant papers
written during that period according to Google Scholar 43 that referenced both “artificial intelligence” and “agents”; and
publications referring to similar technologies that we identified throughout our literature review, e.g.,autonomous assistant,
software agent. There is a long and rich history of precursors to current “AI agents”: To scope this project, throughout our
review, we searched for statements relating to AI agent use cases, functionalities, benefits, and risks.
From these sources, we:
1. Uncovered a spectrum of AI agent autonomy (described in Section 4).
2. Developed a definition of AI agent (described in Section 3) that incorporated previous work and leveraged common
terminology in computer science while minimizing vague or anthropomorphizing language, balancing definitional
precision– excluding systems that a more general definition may include – with definitionalrecall– not excluding
systems that are described as autonomous or agentic systems. Further details on this definition is provided in Section A.
3. Identified recurring AI agent value propositions.
We then analyzed how these values were affected by increased agent autonomy, following our definition and levels. From
this analysis, we isolated a subset of values that most frequently appeared in AI agent writings for presentation in this work.
38e.g., LangChain (2024); Deloitte (2024); Johnson (2024)
39e.g., Chase (2024); Roucher et al. (2024)
40e.g., Sierra AI (2024)
41e.g., Temkin (2024); O’Donnell (2024); Trestman (2024)
42https://www.semanticscholar.org/search
43https://scholar.google.com/scholar
26

F. Value Mapping
Table 5.Selection of sources referencing different AI agent values.
Value Sources
Accuracy Silver et al. (2018), CNN (2021), Du et al. (2024), Kupershtein et al. (2024), Kwartler
et al. (2024), Myakala (2024), Gutowska (2024), Salesforce (2024), Cross et al. (2024),
Wijk et al. (2025), Kapoor et al. (2024), Levret (2025), King & Nori (2025), Sharwood
(2025), He et al. (2025)
Assistiveness Bainbridge (1983), Goddard et al. (2012), Agrawal et al. (2022), Brynjolfsson et al.
(2023), Deng et al. (2023), Salesforce (2024), Whiting (2024), Salesforce (2024),
Holbrook et al. (2024), Ray (2024), Ahmad (2025), Gerlich (2025), Moveworks (2025),
Leena AI (2025), Omneky (2025), Ocoya (2025), Frank et al. (2025), ServiceNow
(2025), EY (2025), Microsoft (2025a), Lindy (2025), IBM (2025), Pham (2025), PwC
(2025a)
Efficiency Ray (2024), Cetin (2024), Hastings-Woodhouse (2024), PwC (2025a), Slack (2025b),
Andrews et al. (2025), Slack (2025a)
Equity Bernardini et al. (2014), Deng et al. (2023), Nagarajan (2024), Nixon et al. (2024),
Kondra & Zink (2025), Houtti et al. (2025), C ¸ic ¸ek G¨uven et al. (2025), Equal Time
(2025)
Flexibility Maes (1993), Valiente et al. (2022), Liu et al. (2023), Zhu (2023), Wen (2024), Park et al.
(2024), Knight (2024), Wang et al. (2024), Yee et al. (2024), Benioff (2024), Detweiler
& Flaningam (2024), Github (2025), Liang & Tong (2025), Anthropic (2025), Lindquist
(2025)
Humanlikeness Short et al. (1976), Blanchard & Mcnincth (1984), Nass et al. (1994), Reeves & Nass
(1996), Morahan-Martin & Schumacher (2003), Epley et al. (2007), Keeling et al. (2010),
Dorion (2011), Waytz et al. (2014), Sidner et al. (2018), Araujo (2018), Adam et al.
(2021), O’Day & Heimberg (2021), Alabed et al. (2022), Park et al. (2023), Janson
(2023), Xie et al. (2023), Park et al. (2024), Stanford HAI (2023), Salesforce (2024a),
Samuel (2024), NPR (2024), Vander Elst et al. (2025), Gannotti (2025), Kim & McGill
(2025)
Privacy Lim & Shim (2022), Bagdasarian et al. (2024), Finch (2025), Microsoft (2025b), Xu
et al. (2025), Yuan et al. (2025), Sun et al. (2025)
Safety Gans (2018), Hu et al. (2022), Zhao et al. (2023), OpenAI (2025), Kreps et al. (2025),
Agarwal (2025)
Security DARPA (2016), Wen (2024), Finch (2025), Labs (2025), Microsoft (2025b), Zhar-
magambetov et al. (2025), Beers & Rushing (2025), Anthropic (2025)
Trust Bainbridge (1983), Maes (1994)
27

G. Example AI Agent Systems
Table 6.Selected AI agent systems, platforms, and related models. We distinguishPlatforms, where agents can be built;Frameworks
used to build agents; and pre-builtAgentsystems.
System / Platform Type Summary Source
Ecobee Thermostat Agent Home use; Proactive temperature adjustment. ecobee.com
SAP Joule Agents Agent Enterprise; Business processes and analytics. sap.com
Equal Time Agent DEI; Meeting assistant/coach that tracks inclusivity. equaltime.io
Zendesk Agents Agent Enterprise; Customer service zendesk.com
Google Gemini Agent Multi-purpose gemini.google.com
Attri.ai Scheduling Agents Agent Enterprise; scheduling. attri.ai
Nyota AI Notetaker Agent Enterprise; meeting assistance. nyota.ai
Play.ai V oice Agents Agent Multi-purpose conversation. play.ai
ServiceNow Now Assist
Agents
Agent Enterprise; IT/HR service tasks and workflow automation. servicenow.com
HubSpot Agent Social influence; Automating social media content creation,
scheduling, and publishing across platforms.
hubspot.com
Omneky Agent Advertising; Increasing reach, effectiveness, and impact. omneky.com
Ocoya Agent Social influence; Automating social media content creation,
scheduling, and publishing across platforms.
ocoya.com
Claude Sonnet Agent Multi-purpose; optimized for software engineering and computer
use
anthropic.com
HockeyStack Agent Enterprise; Revenue analytics. hockeystack.com
OpenAI Operator Agent Computer use; Browser-related tasks (forms, orders, scheduling). openai.com
Devin (Cognition) Agent Software engineering; Coding, debugging, and deploying. devin.ai
GitHub Copilot Agent Software engineering docs.github.com
Manus (Butterfly Effect) Agent Multi-purpose manus.im
AWS Strands Agents Framework Multi-purpose LLM-driven agents. aws.amazon.com
Google ADK Framework Multi-purpose LLM-driven agents. developers.googleblog.com
LangChain Agents Framework Multi-purpose LLM-driven agents. python.langchain.com
smolagents Framework Multi-purpose LLM-driven agents. huggingface.co
LlamaIndex Framework Enterprise; LLM-driven agents that analyze documents. developers.llamaindex.ai
Gumloop Platform Enterprise; No/low-code. gumloop.com
Relay.app Platform Enterprise; Business operations and workflows. relay.app
V oiceflow Platform Multi-purpose; No-code for chat and voice agents. voiceflow.com
Postman Platform Software engineering; Testing, automating API workflows. postman.com
Salesforce Agentforce Platform Enterprise; Customer engagement integrated into CRM workflows. salesforce.com/agentforce
Moveworks Platform Enterprise; IT/HR/employee service tasks and workflow automa-
tion.
moveworks.com
Leena AI Platform Enterprise conversation; IT/HR/Finance communication. leena.ai
Lindy Platform Enterprise; No/low-code builder lindy.ai
Quixl Platform Enterprise; No-code agent builder. quixl.ai
Stack AI Platform Enterprise; No-code builder. stack-ai.com
SmythOS Platform No/low-code conversational agents. smythos.com
Tavus Digital Twins Platform Personal use; “digital twin” with multimodal capabilities. tavus.io
Zapier Platform Enterprise zapier.com/agents
28

H. Example 2024 Articles Motivating AI Agents
Title (linked) BibTeX citation
Why agents are the next frontier of generative AI(Yee et al., 2024)
AI Agents: The Next Big Thing in Generative AI(V ohra, 2024)
Agentic AI: 4 reasons why it’s the next big thing in AI research(IBM, 2024)
AI Agents // future of AI or just hype?(NoAI Labs, 2024)
Prompted: Why Agents Are the Next Big Thing in AI(Tier One, 2024)
New autonomous agents scale your team like never before(Spataro, 2024)
Table 7.Selection of online articles from 2024 claiming AI Agents were the “next big thing.”
29
