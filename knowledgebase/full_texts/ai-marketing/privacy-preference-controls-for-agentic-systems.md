---
title: Privacy Preference Controls for Agentic Systems
url: https://arxiv.org/abs/2610.29929
category: ai-marketing
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Shreya Kochar
- Peeranat Sugsavanvit
- Vidur Gupta
- Joseph A. Calandrino
- Deepak Kumar
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.29929
pages: 27
chars: 104785
fetched_at: '2026-11-08T13:33:43+00:00'
kb_version: 1
---

# Privacy Preference Controls for Agentic Systems

Privacy Preference Controls for Agentic Systems
SHREYA KOCHAR∗,University of California, San Diego, USA
PEERANAT SUGSAVANVIT,Wesleyan University, USA
VIDUR GUPTA,Stanford University, USA
JOSEPH A. CALANDRINO,Carnegie Mellon University, USA
DEEPAK KUMAR,University of California, San Diego, USA
BRETT FRISCHMANN,Villanova University, USA
SEBASTIAN ZIMMECK∗,Wesleyan University, USA
In response to vast and widespread online tracking, regulators and technologists alike have worked to develop laws and tools that allow
people to express their privacy preferences. These measures seek to offer users greater control over the sale and sharing of personal
information, putting agency in their hands to protect their privacy. However, the web is undergoing a seismic shift, away from strictly
user-drivenbehavior towardsagentic behavior, where AI agents take autonomous actions on behalf of users. In this study, we ask:
What should privacy preference controls look like in the agentic web and agentic systems more generally? To answer this question,
we develop a taxonomy of enforceable privacy preferences for agentic systems. Our taxonomy is informed both by laws and empirical
studies of existing privacy tools as well as an audit of 30 leading AI assistants and agent platforms. To explore how our taxonomy can
be implemented, we design and develop eight open-source prototypes that mirror real-world agentic applications and demonstrate
how major aspects of our taxonomy can be structurally integrated into agentic protocols, such as the Model Context Protocol and
Agent2Agent protocol. Ultimately, our study seeks to provide the groundwork for ensuring end-user privacy and autonomy are not
lost in the newly arriving agentic world.
CCS Concepts:•Security and privacy → Privacy protections;•Social and professional topics → Privacy policies;•Computing
methodologies→Intelligent agents;•Applied computing→Law.
Additional Key Words and Phrases: Global Privacy Control, Opt-out, AI Agents, Agentic Web, Data Minimization, Privacy Preference
Signals, Model Context Protocol, Agent2Agent Protocol
1 Introduction
Internet users often pay for “free” services with their data [58]. On the web, for example, ad networks track users via
cookies, browser fingerprinting, and other privacy-invasive mechanisms [37]. In response to this widespread tracking,
an increasing number of privacy laws, such as the California Consumer Privacy Act (CCPA) [107] mandate that people
have a right to opt-out from tracking. These legal requirements are often complemented by technical systems, such as
Global Privacy Control (GPC) [127], which are intended to ease the burden of privacy self-management for users.
However, the Internet writ large is undergoing a major shift away from user-driven interactions and towardsagentic
interactions [90]. In an agentic web, AI agents autonomously perform everyday tasks on behalf of users—for example,
system’s like Meta’s Muse [63] and OpenAI’s Dots [86] can, without supervision, book a flight—from researching the
best connections, finding the lowest price, to the actual booking [63]. For such tasks, agents need privileged access
∗Corresponding authors.
Authors’ Contact Information: Shreya Kochar, shkochar@ucsd.edu, University of California, San Diego, San Diego, CA, USA; Peeranat Sugsavanvit,
Wesleyan University, Middletown, CT, USA; Vidur Gupta, vidur@stanford.edu, Stanford University, Stanford, CA, USA; Joseph A. Calandrino, Carnegie
Mellon University, Pittsburgh, PA, USA; Deepak Kumar, University of California, San Diego, San Diego, CA, USA; Brett Frischmann, Villanova University,
Villanova, PA, USA; Sebastian Zimmeck, szimmeck@wesleyan.edu, Wesleyan University, Middletown, CT, USA.
1
arXiv:2610.29929v3  [cs.CY]  3 Nov 2026

2 Kochar et al.
to sensitive data, which they may overshare and use without direct user control [19, 99]. To make matters worse, AI
companies have already started integrating ads to generate revenue [89, 100] and AI systems are freely participating in
third-party tracking [81]. These new, agentic modalities both fundamentally reshape our relationship with privacy and
introduce a new swath of privacy challenges that we as the research community must now contend with.
In this study, we evaluate the need for and feasibility ofprivacy preference controlsin agentic systems. 1 To do so,
we develop a taxonomy of privacy preferences that can be expressed in agentic systems, informed by three sources:
(1) existing laws that enable users to express privacy preferences in current technical systems, (2) empirical opt-out
studies (e.g., those studying how users engage with cookie banners), and (3) an empirical audit of AI products released
by 22 companies, exploring what controls they offer to users today. We then implemented eightagentic prototypes
(Section 5) informed by existing tools, to examine privacy preferences in our taxonomy. This examination demonstrates
the feasibility of some existing privacy controls while also showing the need for more robust coverage.
We situate our work in stark contrast with the current practice of data maximization on the web and thesurveillance
capitalismthat it supports [129]. Instead, we see data minimization as a legally enforceable default from which exceptions
should be allowed only when demonstrably informed consent exists [45]. We ground privacy preference controls in the
understanding of privacy as a protective right for an individual’s personal autonomy [97]. This not only encompasses
which data should be shared with whom but also being free from the presence and persistence of AI agents. Our
taxonomy is also informed by contextual integrity (CI), especially in understanding the boundaries of data collection
and sharing in agentic systems [16, 76]. Our study seeks to answer the following questions:
RQ1.What privacy preference controls should people be able to express and have respected in agentic systems?
RQ2. What are the technological and legal challenges that need to be considered and resolved for privacy preference
controls to be effective in agentic systems?
RQ3. How can we structurally integrate privacy preference controls into agentic systems, especially, as such systems
interact with the web and online ad ecosystem?
After discussing the background and related work (§2) and our methodology (§3), we contribute:
• A taxonomy for privacy preference controls on agentic systems for implementation in agentic protocols and informed
by an empirical audit (§ 4).
• An empirical audit of major technology and AI companies’ privacy preference controls in their AI products as well
as the agentic protocols they use and support (§ 4.6).
• Open-source prototype implementations for expressing and propagating enforceable privacy preferences for the
MCP and A2A protocol (§ 5).2
We then discuss our research questions (§ 6) in the context of broader legal concepts and the technological landscape
and conclude our evaluation with future work (§ 7).
2 Background and Related Work
Our work is motivated by the failures of notice and choice (§ 2.1) and the emergence of privacy preference signals as a
promising opt-out mechanism for web tracking (§ 2.2). As AI agents are integrated into the online ad ecosystem (§ 2.3),
we can adapt privacy preference signals for agentic protocols (§ 2.4) to minimize data collection and sharing and respect
contextual boundaries (§ 2.5).
1We also refer to those asenforceable privacy preferences, or, simply,preferencesorcontrols.
2Our prototype implementations are publicly available at https://github.com/privacy-tech-lab/gpc-ai-agents-prototypes.

Privacy Preference Controls for Agentic Systems 3
2.1 Notice and Choice
U.S. privacy law relies on notice and choice: organizations disclose their data practices in a privacy notice, and users
make their choice, whether through explicit agreement, an objection, or continued use. In most other countries, opt-in
consent is the norm [122]. Notably, the General Data Protection Regulation (GDPR) prohibits personal data processing
unless one of six lawful bases, among which opt-in consent is the most common, is present.
The shortcomings of notice and choice are well-documented. Notice and choice do not provide people with a
meaningful way to express or negotiate their preferences [45]. It also asks for too much, as people cannot meaningfully
weigh the costs and benefits of data practices across the many entities they deal with, especially as many harms only
become apparent after data aggregation over time [ 104]. User interfaces for notice and choice often contain dark
patterns and condition users to agree without deliberating [43, 45, 54, 55].
In agentic systems, the shortcomings of notice and choice are even more acute. To a greater extent than on the
web, an agent may disclose sensitive data to downstream third parties that the user is unaware of and cannot control.
Generally, agentic systems do not have built-in mechanisms for conveying privacy choices and minimizing data; such
mechanisms are particularly important in these systems because, among other things, agents can access, use, and
disclose an incredible range of sensitive data, across extended durations and contexts, and without user awareness or
supervision, and can be manipulated into over-disclosing [17].
2.2 Privacy Preference Signals
The history of privacy preference signal development confirms the importance of developing the technical and legal
architecture of privacy preference controls together. On the web, the first major effort to automate notice and choice was
the Platform for Privacy Preferences Project (P3P) [32]. P3P allowed websites to declare their data collection practices
in a machine-readable format that could be acted upon by a user agent. However, it lacked enforcement and, thus, was
not widely adopted [31]. The subsequent development of the Do Not Track (DNT) header [115], which depended on
self-regulation, failed for the same reason [126]. GPC [127] addresses this shortcoming. In addition to support from
publishers, browser vendors, civil society organizations, and other stakeholders, it is supported by lawmakers and
regulators.
In particular, the CCPA and its regulations give consumers the right to opt out of the sale and sharing of their
personal information via GPC and mandate its inclusion in every browser from 2027 onward [ 24]. The California,
Colorado, and Connecticut attorneys general have brought GPC enforcement actions. Compliance is improving steadily,
albeit slowly [57, 128]. GPC can also be applied to EU laws [126].3 It is expressed via the header field Sec-GPC: 1 and
the JavaScript field navigator.globalPrivacyControl for client-side scripts. A site may advertise that it honors GPC
by serving a.well-known/gpc.jsonresource [127]. GPC alleviates the usability challenges of opting out [125].
2.3 Web Advertising and Tracking
Privacy preference controls matter more as agentic systems take on the tracking techniques of the web, giving third
parties new ways to collect sensitive information about users and their conversations and to draw inferences from
it [81]. Tracking pixels, software development kits, persistent identifiers, and server-side forwarding now operate
inside conversational AI services, passing prompts, generated titles, and conversation permalinks to third parties whose
business models rely on advertising [81]. ChatGPT serves as an example.
3Advanced Data Protection Control [3], another recent privacy preference signal, is specifically tailored to EU law.

4 Kochar et al.
Closed platform ①
Open web
Advertiser
Ad system
Attribution
User
Ad
②  Website 1 Closed platform integration Ad Exchange
③  Website 2 User Ad
targeting
criteria, ad
targeting
criteria, ad
click ad
user ID, profile
aggregation
targeting
criteria, ad,
bid, user ID
successful
bid
click ad
①  Target ad within closed platform
②  Identify user via closed platform integration
③  Track user on the open web
visit websites
(a) Open web
Orchestrator platform ①
Agentic system
Calendar MCP server
User Orchestrator agent e.g., ChatGPT
Agent Card Travel agent A2A sub-agent
Booking system
MCP server
Hotel agent
A2A sub-agent
MCP: read
free dates"Book my
conference trip"
itinerary
② read Agent Card A2A: name, dates
itinerary
③ MCP: create booking A2A: name, dates
①  Plan task within orchestrator platform
②  Delegate task to a sub-agent through A2A
③  Sub-agent acts as orchestrator for its own calls (b) Agentic system
Fig. 1. How user data travels on the open web (a) and on an agentic system (b). (a) The integration of a closed platform into the open
web and its ad ecosystem. As websites integrate platform code and platforms participate in open ad exchanges, users’ activities can
be tracked and attributed on- and off-platform. (b) Travel booking on an agentic system. A user asks an orchestrator agent to book a
trip. The orchestrator reads the user’s calendar through an MCP server, reads a travel agent’s Agent Card, and delegates the booking
to that agent through the A2A protocol. The travel agent then acts as an orchestrator for its own calls: it books through an MCP
server and passes the user’s name and dates to a hotel agent through the A2A protocol. The user’s name and dates reach the travel
agent, the hotel agent, and the booking system.
While OpenAI describes ad selection in ChatGPT as a vendor-internal system and states that advertisers receive
neither raw conversation content nor memories [82], advertisers can install OpenAI’s measurement script to send page
views and purchase events to OpenAI [87]. Observations on Chrome for Android suggest that OpenAI could link this
activity to ChatGPT accounts for signed-in users or device identifiers for logged-out users using __obi, a cookie set
by bzr.openai.com and scoped to .openai.com [23]. This integration illustrates the broader trend: AI platforms are
extending their reach beyond their internal boundaries to encompass the traditional online ad ecosystem.
Figure 1 contrasts how a closed platform integrates into the open web (Figure 1a) with how an orchestrator platform
integrates into an agentic system (Figure 1b). For the open web, the browser is a single point at which a user’s preference,
e.g., Sec-GPC: 1 , can be attached to every outgoing request. In an agentic system, user data traverses multiple hops of
delegation, and the user typically knows only the first point of contact. Just as social networks moved outwards over
the past two decades, we expect agentic platforms to do the same.

Privacy Preference Controls for Agentic Systems 5
2.4 Privacy in Agentic Protocols
Agentic systems routinely delegate both tasks and authorizations to perform them [113]. Similar to the central role
browsers play on the web, a central entity in agentic systems is theorchestrator, i.e., the agent that the user interacts
with and that is the originator of every outbound call made for the task the user specified. ChatGPT is an example of an
orchestrator.4 An orchestrator finds a remote agent through the agent’sagent card, a machine-readable description the
agent publishes of what it can do and how it can be reached [1]. A sub-agent receiving a call from an orchestrator can
itself act as an orchestrator for any calls it makes, as shown in Figure 1b.
Due to this distributed nature of agentic systems, users may only know “their” orchestrator, and downstream agents
may not know the users’ identities, which gives rise to an accountability vacuum [ 113]. However, deployers and
regulators need visibility into which agent acted, and on whose behalf, to assign responsibility [25]. Furthermore, as
model aggregators and routers, such as OpenRouter, forward requests to model providers and can inspect prompts and
tool data [61], privacy preference controls must cover these intermediaries as well.5 Overall, security and governance
in the agentic web is an open challenge [121].
We believe that privacy preference controls and norm resolution must be built into the structure of the facilitated
interactions, i.e., into the protocols that agents use to communicate and exchange data. The most relevant protocols
for agentic privacy are MCP [ 73], which connects agents to tools and data, and the A2A protocol, which supports
agent-to-agent interaction [1].6 MCP and A2A can serve as the foundation from which emerging ad protocols, such
as the Ad Context Protocol (AdCP) [ 4], Universal Commerce Protocol (UCP) [ 114], and agentic real time bidding
protocols [59], can inherit functionality, attributes, and constraints. While we discuss our taxonomy in the context of
the MCP and A2A protocol, it is protocol-agnostic.
2.5 Data Minimization and CI
On the traditional web, the effective baseline is data maximization, which inherently limits the effectiveness of GPC and
other privacy mechanisms that are pragmatically designed to operate under this baseline. For agentic systems, we now
have the opportunity to realizedata minimization, i.e., the requirement that entities collect, use, or share only necessary
personal information [105]. The case for data minimization is simple: if data is not necessary, there is no reason to collect,
use, or share it. While data minimization is a core principle in many privacy laws, two structural forces are blunting its
effectiveness. First, notice and choice is generally designed and implemented as a routine click-to-consent mechanism,
thereby overriding data minimization laws and reinforcing data maximization [45]. Second, data minimization rules are
usually purpose-dependent, and companies tend to define purposes broadly, for example, as “improving services. ” Here
is where agentic systems present us with the opportunity to design and implement data minimization to user-authorized
tasks rather than company-specified purposes.
Agents make minimization harder than conventional software does, because they work from the semantic context of
a request rather than from structured fields alone [16, 17]. Several data minimization challenges remain [16]: (1) the
semantic boundary problem, determining what data a task expressed in natural language requires; (2)model context
contamination, ensuring minimal and appropriate information flows within an agent’s reasoning cycle; and (3)tool over-
privilege, granting agents minimal privileges when exact data requirements are initially unknown, without burdening
the user. To address these challenges CI is a natural fit [16, 17]. CI posits that an information flow is appropriate if it
4MCP calls the orchestrator thehost[73]. A2A does not have a single orchestrator due to its peer-to-peer architecture.
5For details see Appendix D.1.
6When we refer to MCP, we also include WebMCP, which connects agents to websites [116].

6 Kochar et al.
conforms to the norms of the context in which it occurs, as described by its sender, recipient, subject, information type,
and transmission principle [76]. It has been used to detect data leakage [101] and bound data disclosure [16, 17].
Various previous approaches aim to control how user data flows through agentic pipelines. AirGapAgent uses a data
minimizer to restrict an agent’s access to only the user data required for the task, preventing adversarial third-party
access [17]. Similarly, firewall architectures abstract outgoing user data and constrain incoming messages to task-specific
structure [2]. Authenticated delegation frameworks let users scope the permissions of agents acting on their behalf and
propagate those limits along chains of agents [106]. For our purposes, for the MCP implementation of context-bound
data minimization, MCP Interceptors—control points that observe, filter, or modify traffic [ 77]—are a core building
block.7
3 Methodology
We developed our taxonomy using an iterative, general taxonomy development methodology [75]. Initially, we reviewed
legal, regulatory, and technical sources to derive the categories for our taxonomy (§ 3.1), then audited the privacy
preference controls for major AI products (§ 3.2), and finally refined our taxonomy (§ 3.3). We also implemented
prototypes for various agentic scenarios under the taxonomy, whose implementation methodology we discuss separately
(§ 5).
3.1 Taxonomy Category Derivation
We started the derivation of our taxonomy categories with existing literature on (1) the GPC specification and the state
privacy laws and regulations that give it legal effect, (2) empirical opt-out studies, and (3) studies on privacy taxonomies,
rights, and consent. The collection (§ 4.2) and secondary use, repurposing, sharing, and human review (§ 4.3) categories
take into account existing privacy vocabularies and principles (e.g., [ 39, 103, 117, 123]). We also analyzed work on
CI (e.g., [76]) and social boundaries (e.g., [74]) for determining the context of data flows and retention limits. Studies
on privacy by design, autonomy harms, and the engineering of human choice (e.g., [28, 43, 44, 56]) form the basis of
our taxonomy categories on AI agent presence (§ 4.1), persistence (§ 4.4), and autonomy (§ 4.5). Initially, there were
disagreements between authors on how retention and data persistence should be handled by the taxonomy. But over
multiple group meetings, we refined, reviewed, and agreed on the types and scoping decisions.
3.2 Empirical Audit
To further inform our taxonomy categories, we audited privacy preference controls in the AI products of 22 companies.
To that end, we first identified the ten largest technology companies via three 2026 company rankings [29, 41, 42] and
the ten most valuable AI companies via the 2026 Forbes AI 50 ranking [40]. We additionally looked at the most-used AI
chatbots in Comscore’s March 2026 U.S. desktop ranking (by unique visitors) [30] and added two missing companies
(xAI and DeepSeek) to our list. For each of the resulting 22 companies, we audited their AI agents and agent-building
platforms available to the general public. Four companies had no such product, leaving 30 products from 18 companies.8
In October 2026, we collected each company’s privacy policies, help pages, and developer documentation for its
audited products. One author used an LLM (Claude Opus 5.5) to retrieve candidate pages, following the generator-verifier
structure used in recent automated LLM-agent pipelines [18, 53], where a retrieval agent collects the documentation
unattended, while a separate verification agent independently re-checks each retrieved page. All retrieved pages were
7The Interceptors Working Group standardizes how context operations are intercepted, validated, and transformed at key points in the agentic lifecycle [72].
8See Appendix A, Table 2 for the full company and product list.

Privacy Preference Controls for Agentic Systems 7
then manually reviewed and verified by the authors. The authors manually added pages where the collected pages
did not sufficiently document a product’s settings. Our audit involved reading these documents and then listing all
documented controls that let a user, administrator, or developer stop or limit a data practice or AI behavior.
We then used the LLM to categorize the controls by what they stop or limit. We ran the categorization twice to check
its stability; the two runs produced largely the same categories, and we reconciled the differences when reviewing
them. This process resulted in 32 candidates for preference controls emerging from the audit. Two authors reviewed
each against our initial taxonomy and found 24 within its scope and eight outside.9 The audit also surfaced a control
subcategory that our initial taxonomy did not cover, human review, which, with the agreement of all authors, we added
as a subcategory to Category C (§ 4.3). To account for the small number of products, we report each proportion with a
95% Wilson score confidence interval.10
For each company in our audit, we also recorded the protocols it uses in its own products and the protocols that
work with its models or APIs through a partner platform or a third-party package. Of the 22 companies, 16 use MCP
and 5 use A2A in their own products.11 Counting partner platforms and third-party packages, 18 support MCP and 12
support A2A, although three A2A cases (Apple, Meta, and Databricks) rest on minimal evidence. MCP is the dominant
protocol for connecting agents to tools and A2A for connecting agents to each other. A2A is the only agent-to-agent
protocol used by more than one company.12
We note that our audit captures the controls companies document, not whether they work as described. Also,
documentation for controls that require user login as well as controls under enterprise contracts may not have been
available to us. Further, we viewed each company’s documentation and settings from a geographic location within the
U.S. Thus, we may not have seen controls available in other jurisdictions. Finally, while we verified every retrieved
page, LLM-assisted retrieval may have missed relevant documentation.
3.3 Taxonomy Category Revision
We compared each control against the initial taxonomy categories we created and revised the categories as necessary.
We checked for each control whether it was covered by at least one subcategory and mapped it accordingly.
4 Taxonomy
Our taxonomy provides an overview of the different enforceable privacy preferences relevant for agentic systems.
It is based on the understanding of privacy as a right that protects an individual’s personal autonomy, which not
only encompasses control over data but also over environmental exposure and freedom from being influenced by
others, including AI systems and agents. It is also based on the realization of data minimization in agentic systems,
resorting to signal propagation as a privacy preference control only when data disclosure is necessary to perform a
task. User-specified tasks form the contextual boundaries that AI agents must respect. In our taxonomy, we distinguish
five broad categories that capture the sequential lifecycle of agentic tasks:
A.Presence: Whether an AI agent may be present in the user’s computing environment.
B.Collection: The extent of and what data the agent may collect from and about the user.
C.Secondary use, repurposing, sharing, and human review: How the agent may use collected data.
9See Appendix A, Table 1 for all privacy preference controls found, how many products offer each, and their mappings to our taxonomy subcategories.
10See Figure 2.
11See Appendix B, Tables 3 and 4 for the agentic protocols that the companies use and support.
12While Anthropic, OpenAI, xAI, and DeepSeek do not use the A2A protocol in their own products, their models work in A2A agents on partner platforms,
such as Amazon Bedrock AgentCore [5] and Microsoft Foundry [66].

8 Kochar et al.
D.Persistence: Whether the agent may stay in the user’s environment after completing its task.
E.Autonomy: Which decisions the agent can make autonomously on behalf of the user.
4.1 Category A: Presence
Category A covers user preferences about the presence of AI agents in their computing environment.
A1. Integration preference: AI agents may not be integrated without genuine user consent.13 AI integration must be
based on the user’s actual decision and not on surreptitious practices, such as automatically enabling AI features
during software updates.
A2. Activation preference: AI agents may not run in the background or as an ambient agent unless the user has
affirmatively chosen so. This control applies to background and ambient agent presence; it does not apply to
foreground, on-demand use. If users actively initiate an AI task, they have expressed their preference, and no
separate activation preference is needed.
In subcategories A1 and A2, we differentiate between consenting to AI being added and consenting to AI being
active. Users may assert the right of each subcategory independently. For instance, users may want AI agents to be
available in their environment (A1) while not wanting them to be active (A2). Category A does not cover the scenario
of a user directly installing agentic software.
In MCP and the A2A protocol, honoring A1 means a newly connected tool or agent, such as the travel agent in
Figure 1b, receives no user data until the user approves it [1, 73]. Honoring A2 means A2A’s long-running background
tasks, which report back through push notifications while the user is away, run only if the user has turned them on [1].
4.2 Category B: Collection
Category B covers the extent of and what data the agent may collect from and about the user.
B1. Input collection preference: If a user submits data in an agentic system, for example, a prompt, text document, or
video recording, the data can be stored and used to complete the task. Data unrelated to the user’s task may not be
collected.
B2. Metadata collection preference: AI agents may observe, for example, which options users hover over on a user
interface, how long they spend on a task, what text they delete before sending their prompt, or where they are
currently located. Such metadata may not be collected unless it is necessary for completing the user’s task.
B2a. Delegated action collection preference: If an agent acts on a user’s behalf, it may generate a record of its
work, for example, which agents it connected to and when. This record may only be created and retained to
the extent it is necessary to complete the task.
B1 and B2 are distinguished by the user’s relationship to the data in question: B1 covers the data a user knowingly
and actively submits, while B2 covers the data a user unknowingly produces. Each preference is independent. By
requesting an agent to perform a task, the user implicitly expresses the preference to input and metadata collection to
the extent it is necessary to complete the task, which realizes the data minimization baseline we have adopted.
Given this baseline, by default, a user is effectively opted out of data retention for each subcategory. The collected
data may only be retained for the user’s task and must be deleted once it is no longer necessary for the task, unless the
13“Genuine user consent” is based on demonstrably informed consent [45] [46], which requires proof that a person understands important substantive
terms as a condition of consent. AI integration is substantively important. To hold otherwise would perpetuate data maximization.

Privacy Preference Controls for Agentic Systems 9
law requires otherwise. Users can explicitly express a different retention preference, for example, that data should be
stored and visible to the user beyond task completion but not be used by the system beyond the current task.
4.3 Category C: Secondary Use, Repurposing, Sharing, and Human Review
Assuming some data collection has occurred, category C covers what agents are permitted to do with the collected
data. By requesting an agent to perform a task, the user implicitly expresses the preference to use collected data as
necessary to complete that task. For the following subcategories, the boundary between permitted and unpermitted
uses is grounded in the data minimization baseline and further determined by its context.
C1. Secondary use preferences: An agent may not use data beyond a user-requested task unless the user explicitly
expressed a preference for such use. All secondary uses, such as targeting, require users to explicitly declare their
preferences.
C1a.Targeting: The targeting preference would allow data to be used to determine, for example, what content,
options, or offers the user is shown.
C1b. Inference: The inference preference would allow data to be used to infer, for example, attributes of the user
to show personalized recommendations.
C1c. Commercial and analytical use: The commercial and analytical preference would allow, for example, data to
be sold, licensed, or used for advertising, measurement, or analytics.
C2. Data repurposing preference: According to the data minimization default, data may not be used to train, fine-tune,
improve, or evaluate AI models. Such data repurposing uses are permitted if the user explicitly expresses such a
preference.
C3.Data sharing preference: A single user-requested task may trigger a chain of sub-tasks across multiple connected
systems or involving multiple agents (Figure 1). According to the data minimization default, data may not travel
further along that chain than necessary for completing the task. However, a user may express an explicit preference
to allow additional sharing.
C4. Human review preference: A user may explicitly express the preference to allow people acting for the company
providing the AI agent, such as employees, contractors, or third-party reviewers, to read, listen to, or view the
user’s inputs, outputs, or the records of an agent’s actions on behalf of the user. Legally required reviews are
permitted irrespective of the user’s preference.
The four subcategories are distinguished by how data can be used after it is collected. If the user expresses respective
preferences, C1 allows use for advertising, marketing, commercial, and analytical purposes, C2 allows use for AI
development, C3 determines how far data travels, and C4 restricts who may see it. A user might assert the preferences
for any combination of these subcategories independently.
4.4 Category D: Persistence
Category D covers whether an AI agent may stay in the user’s environment after completing the task the user requested
it to perform. To the extent persistence does not involve data processing or a user has already expressed the preference
to allow such processing, for example, data use (category C), it does not implicate data minimization.14 Category D has
three subcategories.
14It would be a worthwhile endeavor to consider the normative desirability and technical implementation of an AI minimization principle applicable to
persistence of AI agents. However, this question is beyond the scope of our study here.

10 Kochar et al.
D1. Post-task presence preference: The user expresses the preference that the agent may not remain in the user’s
environment once it has completed the user-requested task. From a protocol perspective, upon task completion,
the agent’s access, integrations, scheduled jobs, and entry points are removed. Further agent activity requires
invoking or installing the agent again.
D2. Initiation preference: The user expresses the preference that a persistent agent may not begin new activity without
being asked. The agent may stay available, but it may not start tasks, monitor the user’s environment, run scheduled
or background actions, or open interactions such as reminders, suggestions, or check-ins unless the user invokes it
or such activity is necessary for its persistence.
D3. Scope expansion preference: The user expresses the preference that a persistent agent may not extend its presence
beyond its original task. The agent may stay present and may act proactively within the existing scope, but it may
not enter new applications, devices, or domains, take on additional roles, or acquire new access without the user’s
direction.
The three subcategories are distinguished by how much of the agent’s presence the user allows. D1 prohibits
any presence after the task, D2 permits presence but prohibits unprompted activity, and D3 permits presence and
unprompted activity but prohibits expansion beyond the original scope. The subcategory preferences form a hierarchy:
asserting D1 implicitly includes D2 and D3, and asserting D2 implicitly includes D3.
4.5 Category E: Autonomy
Assuming an agent is present and active in the user’s environment, category E covers which tasks an agent can perform
on its own and which it must refer to the user for further instruction. By default, an agent may not start a task on behalf
of a user. The user may partition the tasks an agent can perform autonomously into tiers, for example, based on data
sensitivity, magnitude of consequence, or reversibility of consequence. The user may express the preference that the
agent resolves tasks autonomously within some tiers while not permitting the agent to do so in others. When the user
is not present to provide necessary instructions, the agent defaults to surfacing the decision to the user or rejecting the
performance of the task. The agent does not have autonomy to express preferences on behalf of the user.
4.6 Audit and Taxonomy Analysis
The results of our audit show that our taxonomy captures existing AI products’ privacy preference controls well.
Figure 2 shows an overview. Of the total 788 instances of settings and actions that we found across 30 products, 567
(72%) fall into a subcategory, 21 (3%) only offer preferences on how long data is kept, and the remaining 200 (25%) fall
outside the taxonomy’s scope (§ 4.7).
Among all settings and actions we identified as being covered by our taxonomy, three subcategories stand out in
particular. Only 14 of 29 products offer an opt-out of sale or sharing for advertising, including GPC (C1c). Further, only 7
of 29 let users opt out of analytics or product-improvement use (C1c), and only 6 of 30 let users opt out of human review
(C4). These findings are particularly concerning as tracking technologies in conversational AI are proliferating [81].
Our audit also shows where companies’ controls are weaker than the taxonomy’s definitions. For example, input
collection (B1) requires that submitted data be discarded once it is no longer necessary for a task, yet several “temporary”
modes keep it for a set time: 30 days for Claude’s incognito chats [11], 72 hours for Gemini’s temporary chats [48], and
24 hours for Perplexity’s incognito threads [96]. Also, autonomy (E) requires that the agent, by default, does not start a

Privacy Preference Controls for Agentic Systems 11
Turn off AI feature (A1)Limit agent reach (D3)
Agent approval (E)Memory off (C1b)
Don't keep inputs (B1)
Model training (C2)
Connector/3rd-party sharing (C3)
Stop scheduled tasks (D2)
Website cookies (C1c)
Limit retention
Sensors/permissions (B2)
Sale/sharing (C1c)
Agent logs/traces (B2a)Ad personalization (C1a)Telemetry/diagnostics (B2)Wake words/listening (A2)Revoke agent access (D1)Personalization off (C1b)
Proactive/background AI (A2)Analytics/product use (C1c)
Public sharing (C3)
Mask sensitive data (B1)
Screen/activity capture (B2)
Human review (C4)
Delete data
Rights requests
Other
Data locationSafety/parental
Admin/governance
MarketingExport data
0%
25%
50%
75%
100%
Share of applicable products
offering ≥1 documented control
18/22
21/28
19/28
18/28
19/30
18/29
18/30
14/25
16/30
16/30
15/29
14/29
13/29
10/23
12/29
7/17
11/28
11/28
8/24
7/29
7/30
7/30
4/18
6/30
27/30
20/30
13/30
12/30
11/30
9/30
9/30
5/30
Outside the taxonomy,
for comparison
Availability by Preference Signal
Fig. 2. Share of audited AI products that offer at least one documented setting or action for a privacy preference control per a
subcategory of our taxonomy (𝑛= 30products from 𝑘= 18companies). Denominators vary because some subcategories do not apply
to every product. For instance,Turn off AI feature (A1)does not apply to a standalone chatbot or API, where the AI is the product.
Blue bars display the share of products covered by our taxonomy, labeled with the taxonomy subcategory they map to. Grey bars
display settings and actions outside the taxonomy’s scope (§ 4.7), shown for comparison.Limit retentionhas no subcategory label
because it can relate to all subcategories of B (§ 4.2). Whiskers show 95% Wilson score confidence intervals.
task on behalf a user. But Claude Code now starts interactive sessions in a mode where a classifier, rather than the user,
approves actions [8]. In each case, a control exists, but it is less restrictive than required by our taxonomy.
Even where controls exist, users often cannot tell what it does by default. Only 40% of settings and actions document
their default state, and the share falls to 19% for opt-outs to be exercised by request to the company.
4.7 Scope and Limitations
Our taxonomy is scoped to cover future data processing. The deletion right, which covers past data processing, is
outside its scope. We also exclude settings for changes to products, marketing communications, data export, plans or
subscriptions, content safety, parental supervision, and labeling of AI-generated output. Our taxonomy does not cover
harms that result from an AI system’s outputs. A system can honor the control a user exercised and still undermine
their autonomy by leading or suggestive responses, for example. Our taxonomy is focused exclusively on realizing
privacy preference controls per the CCPA, GDPR, and similar privacy and data protection laws.
Of the 200 settings and actions in our audit that fall outside the taxonomy (§ 4.6), 73 are deletion controls, which act
on past rather than future processing. A further 34 cover privacy law requests, that is, procedural elements for exercising
privacy preference controls rather than controls on their own, and 16 let users choose where data is being processed.
The other 77 cover marketing communications, data export, content safety and parental controls, administrative settings,
and other product preferences.
Finally, privacy preference controls are subject to legal requirements and terms of service, in particular, carve-outs
for (1) legal obligations (e.g., OpenAI may keep deleted chats beyond its 30-day deletion window [84]), (2) security and

12 Kochar et al.
abuse prevention (e.g., Google keeps all Gemini API prompts and outputs for 55 days to detect policy violations [47]),
and (3) user-initiated disclosure (e.g., even with Gemini’s Keep Activity turned off, a user who submits feedback also
gives Google the last 24 hours of their chats, which Google may use to improve Gemini [48]). Thus, how much protection
a privacy preference control provides ultimately depends on laws and regulations.
5 Agentic Prototypes
To test whether our taxonomy is feasible in practice, we built agentic prototypes that implement several of its categories
and subcategories. The eight prototypes cover different categories of our taxonomy for common agentic tasks: (1) travel
planning, (2) medical questions, (3) productivity tasks, (4) website product research, (5) web search, (6) email revision,
(7) general questions, and (8) travel booking. We used MCP and the A2A protocol because our audit identified them as
the dominant agentic protocols.15 We propagate the GPC signal [127] as an example in our code. In each example, the
run without a preference shows how such systems commonly behave today.
Prototype 1: Travel Planning.A user with privacy preferences enabled asks, “Help me plan a 5-day trip to Japan: what
should I see, eat, and know before I go?” The assistant searches the web, synthesizes an itinerary, saves it to the user’s
profile, and consults what it already knows about the user before answering. The orchestrator sends the request over
A2A to a search agent, which calls a search_web tool over MCP. The search agent sends the results over A2A to a
synthesis agent, which writes the itinerary. The orchestrator attaches the preference to each A2A message and each
MCP call, ensuring that every agent receiving the data also receives the preference (C3). The MCP server then blocks
writes to the user’s profile and the interaction log (B1) and blocks reads of the user’s interaction history unless the
user has allowed long-term profile use (C1b). Without any privacy preference, the pipeline saves the trip to the user’s
profile and logs the interaction. With privacy preferences set, the MCP server blocks both writes, and the pipeline keeps
nothing about the trip after the conversation ends. The pipeline also stops reading the user’s interaction history. The
user receives the same itinerary in both cases.
Prototype 2: Medical Questions.A patient asks an AI assistant, “What does my blood pressure reading mean, and
should I adjust my medication?” The assistant retrieves the patient’s medical records and answers the question. The
conversation also feeds an analytics log (C1c), a model-training dataset (C2), and an external pharmaceutical advertising
platform (C1a, C3). The user can turn off each secondary use separately, for example, by blocking ads while allowing
analytics. Without any privacy preference, the conversation goes to all three secondary uses. With privacy preferences
set, all three are turned off. The user receives the same answer in both cases.
Prototype 3: Productivity Tasks.A user signs up for a productivity assistant and agrees to file access and web search.
Six months later, a platform update adds two tools to the MCP server without asking the user: email_sender, a
communication capability, and behavior_tracker, an analytics capability that runs in the background. Every tool call
passes through a consent check that compares it to a versioned record of the tool categories the user agreed to. Tools in
categories added after sign-up (A1) are not turned on until the user approves or declines their integration. This covers
the tracker the platform starts on its own (A2, D2) and any capability beyond what the user agreed to at sign-up (D3).
Without any check, both tools can be called as soon as the update ships, as if the consent given at sign-up covered
them. With privacy preferences set, the new tools are turned off by default.
15See Appendix B, Tables 3 and 4.

Privacy Preference Controls for Agentic Systems 13
Prototype 4: Website Product Research.A user with privacy preferences enabled asks an agent to research the iPhone 17
across eight tech publishers. The agent queries the publishers in parallel through the LLM provider’s middleware, which
logs every call. The preference is attached to each call sent to the publishers (C3), and each publisher decides whether
to log it. The provider’s middleware records which publishers the agent called, in what order, and with what subqueries
(B2a). Without any privacy preference, every publisher and the provider log every call. With privacy preferences set,
the publishers that honor them stop logging, but the provider’s own log is basically unchanged.
Prototype 5: Web Search.A user with privacy preferences enabled runs eight ordinary searches, such as metformin
side effects, SNAP benefits, and signs of anxiety. None of the queries hands over personal data directly, but a classifier
infers attributes about the user from each query and stores them in a profile. Before an inferred attribute is written to
the profile, a check inside the search tool reads the user’s preference and drops the write if the user has opted out of
inference (C1b). The check is part of the tool’s code. Each dropped write is logged, making the blocking visible. Without
any privacy preference, the eight queries create a user profile covering health, money, housing, mental health, and job
status. With privacy preferences set, the inferences are still computed but not kept. The user receives the same search
results in both cases.
Prototype 6: Email Revision.A user with privacy preferences enabled asks a writing assistant to polish an email to
their manager about a raise. While writing, the user deletes a sentence about treatment costs, pauses for 42 seconds on
the salary line, and rewrites the opening three times. The assistant keeps the draft, the editing telemetry, and what it
infers from both. Each kind of data has its own blocker based on the preferences set: the draft the user submits (B1), the
editing telemetry the user does not know they are creating (B2), and what the system infers from both (C1b). Without
any privacy preference, all three kinds of data are kept. With privacy preferences set, all three gates block retention.
The user receives the same polished email in both cases.
Prototype 7: General Questions.A user talks to an assistant with memory across two sessions. In the first, they mention
being vegetarian on a tight budget, and in the second, they ask about restaurants. The assistant archives each session,
recalls past sessions into new ones, and builds a model of the user. The assistant supports three preference scopes:
discarding each session when it ends (B1), keeping an archive the user can see but not recalling it into later sessions
(C1b), or keeping transcripts but never turning them into a model of the user (C1b). Without any privacy preference,
the first session is archived, recalled into the second, and used to build a behavioral model. With privacy preferences
set, the first session is discarded when it ends, and nothing is recalled. The assistant still uses context from earlier in the
same session to keep the conversation coherent.
Prototype 8: Travel Booking.A user asks an agent to book a weekend trip, which requires the agent to search for
flights, hold a hotel room, buy a non-refundable ticket, and send the user’s passport details to the airline. The platform
also turns on fare tracking and signs the user up for a newsletter on its own. Some of these actions cannot be undone, and
some involve sensitive data. The user decides, for each type of action, whether the agent may perform it independently
or must ask the user first (E). If the user has not specified a preference for an action, the agent must ask first. Fare
tracking and the newsletter sign-up, which the platform starts on its own, also need the user’s approval unless the
user has already allowed them (A2, D2). Without any privacy preference, the platform’s default tiers count as the
user’s consent, and four of the six actions run without the user’s approval. With privacy preferences set, the platform’s
defaults no longer count as consent, and the agent must ask before performing any action the user has not explicitly
allowed. If the user is not available to answer, the agent declines the action instead of assuming approval.

14 Kochar et al.
Lessons from the Prototypes.By implementing these prototypes, we show that it is possible to propagate preferences
in various agentic settings. These examples we show that privacy preference controls can often be implemented without
significantly reducing utility. We note that there are no privacy preference-related fields in existing agentic protocols.
We use the “meta” field in both MCP and the A2A protocol to custom-design signal propagation. After implementing
the prototypes and exploring different scenarios, we also find that the taxonomy’s influence is context-dependent.
The same control can cover different amounts of data and differ in whether it can be enforced or verified. Consider
a user who asserts B1 (input collection) and D2 (unprompted initiation). If the agent only acts locally on the user’s
machine, the user can check and enforce both opt-outs. The user can inspect the device to confirm that the session data
is not kept, and the agent can refer each new activity to the user as it comes up. Now suppose the same task runs on a
cloud-hosted agent that completes a purchase overnight while the user is offline. The user must trust that the company
deleted the session data. No one is available to consult. The opt-outs are identical in both cases, but what differs is
whether anyone can confirm that they were honored. The enforceability of preferences thus often varies significantly
with context. Future work could explore ways to verify compliance in these and other scenarios.
6 Analysis and Discussion
Agentic systems represent a seismic shift in computing towards substantially more autonomous activities. However,
this shift also creates the need for a broad privacy preference control landscape.
6.1 RQ1: What privacy preference controls should people be able to express and have respected in agentic
systems?
Because AI agents act autonomously, they do more than trigger traditional privacy risks, such as unauthorized data
sharing; they directly encroach on people’s personal autonomy. As a consequence, existing privacy preference controls,
such as GPC, fall short in providing the broad spectrum of controls users require in agentic systems. We see personal
autonomy as the guiding anchor in this new environment: even as agents act on their behalf, people must remain
empowered and have the rights to supervise their agents and remain in control. Autonomy alone is too abstract a
principle to design for, so our category breaks down types of controls into five categories. Effective protection requires
controls that span the entire agentic lifecycle; this includes gatekeeping initial presence and background activation,
restricting data collection and secondary uses to task-bound scopes, regulating post-task persistence, and establishing
authorization levels for autonomous decision-making. We think that these are the essential controls people should have.
However, we also note that expanding the control space introduces a usability tradeoff. To prevent choice fatigue and
avoid repeating the web’s cookie banner deluge, agentic systems must focus on meaningful and effective controls. Thus,
future work in this area should include user studies to reduce cognitive burden when these controls are standardized.
6.2 RQ2: What are the technological and legal challenges that need to be considered and resolved for
privacy preference controls to be effective in agentic systems?
In the U.S., most states still lack comprehensive privacy legislation. There is also no legal framework to govern AI agents.
Simply extending existing controls through new legislation and regulation will not suffice. Current law is structurally
built around a default of data maximization, recognizing only a narrow set of controls. As our taxonomy demonstrates,
however, agentic systems demand far broader controls that are both technically expressible via standardized protocols
and legally enforceable.

Privacy Preference Controls for Agentic Systems 15
Operationalizing data minimization legally represents a major challenge. Robust data minimization requires that
(1) agents process personal data only as necessary to complete a user-specified task, and (2) any departure from this
baseline requires demonstrably informed user consent [45]. This approach evaluates necessity against bounded and
user-authorized tasks rather than open-ended business-defined purposes. However, establishing clear task boundaries
is challenging.
In this regard, context, in particular, CI, has emerged as a promising boundary construct [16, 76]. However, mapping
legal and social concepts of context onto technical systems is a major challenge. While technical mechanisms, such
as MCP Interceptors, can enforce discrete operational boundaries, for example, isolating chat sessions, it is unclear
whether those align with psychological or social norms and realities. From a legal perspective, a major challenge
lies in shifting statutory baselines from purpose-based data maximization to task-bounded minimization, while the
principal technological challenge requires guaranteeing end-to-end signal verifiability and auditability across opaque,
multi-hop delegation chains. Bringing these disparate strands together will be critical for meaningful and impactful
privacy protection on the agentic web.
6.3 RQ3: How can we structurally integrate privacy preference controls into agentic systems, especially as
such systems interact with the web and online ad ecosystem?
AI agents have the potential to act as active privacy shields for users [124]. Realizing this potential, however, requires
embedding controls directly into the structure of agentic protocols. Our prototypes demonstrate that such integration is
feasible, shifting the challenge toward industry standardization. Privacy preference controls and natural task boundaries
must be woven into the architecture of agentic systems. Structurally, this can be achieved by embedding mandatory
preference—checking interceptors and standardized header signals—to ensure that data minimization defaults are
enforced at every delegation point in a pipeline, especially, before agents interact with web endpoints or ad networks.
7 Conclusion
In this study, we systematized what enforceable privacy preferences a user can and should be able to exercise in agentic
systems. If we are to move away from the data maximization defaults of our current ecosystem, we require an integrated
techno-legal effort to shape the legal system and the build-out of the technological infrastructure of agentic systems. The
varied stakeholders in the agentic ecosystem include a vast and opaque network of agents, sub-agents, and third parties,
all of whom need to achieve consensus to appropriately protect privacy. Developing both new privacy-preserving
technology and mapping existing legal concepts, such as controllers/processors [ 38, 107], onto the components of
agentic systems remains a rich area for future work and is necessary to ensure the agentic ecosystem can be built with
privacy in mind from the ground up. We see this juncture as an opportunity to build the right privacy primitives while
the agentic web is still in its formative stage to structurally protect people’s privacy and personal autonomy.
References
[1] A2A Project Contributors. 2026. Agent2Agent (A2A) Protocol Specification. https://github.com/a2aproject/A2A Version 1.0.0, accessed: November
5, 2026.
[2] Sahar Abdelnabi, Amr Gomaa, Eugene Bagdasarian, Per Ola Kristensson, and Reza Shokri. 2026. Firewalls to Secure Dynamic LLM Agentic
Networks.Transactions on Machine Learning Research(June 2026). https://openreview.net/forum?id=w02FW1dMoY arXiv:2502.01822.
[3] Advanced Data Protection Control. 2026. Simplify EU Websites. End Cookie Banners. https://www.dataprotectioncontrol.org/ accessed: November
5, 2026.
[4] AgenticAdvertising.org. 2026. Ad Context Protocol (AdCP) Specification. https://docs.adcontextprotocol.org Version 3.1, accessed: November 5,
2026.

16 Kochar et al.
[5] Amazon Web Services. 2025. Introducing Agent-to-Agent Protocol Support in Amazon Bedrock AgentCore Runtime. https://aws.amazon.com/
blogs/machine-learning/introducing-agent-to-agent-protocol-support-in-amazon-bedrock-agentcore-runtime/ AWS Machine Learning Blog,
accessed: November 5, 2026.
[6] Anthropic. 2024. Introducing the Model Context Protocol. https://www.anthropic.com/news/model-context-protocol. accessed: November 5, 2026.
[7] Anthropic. 2026. API and data retention. https://platform.claude.com/docs/en/manage-claude/api-and-data-retention. accessed: November 5,
2026.
[8] Anthropic. 2026. Choose a permission mode. https://code.claude.com/docs/en/permission-modes. accessed: November 5, 2026.
[9] Anthropic. 2026. Data usage. https://code.claude.com/docs/en/data-usage. accessed: November 5, 2026.
[10] Anthropic. 2026. Use Claude’s chat search and memory to build on previous context. https://support.claude.com/en/articles/11817273-use-claude-
s-chat-search-and-memory-to-build-on-previous-context. accessed: November 5, 2026.
[11] Anthropic. 2026. Use incognito chats. https://support.claude.com/en/articles/12260368-use-incognito-chats. Claude Help Center, accessed:
November 5, 2026.
[12] Apple. 2026. Giving External Agents Access to Xcode. https://developer.apple.com/documentation/xcode/giving-external-agents-access-to-xcode.
Apple Developer Documentation, accessed: November 5, 2026.
[13] Apple. 2026. Siri, Dictation & Privacy. https://www.apple.com/legal/privacy/data/en/ask-siri-dictation/. accessed: November 5, 2026.
[14] Applied Intuition. 2025. General Privacy Notice. https://www.appliedintuition.com/general-privacy-notice. accessed: November 5, 2026.
[15] Applied Intuition. 2026. Products. https://www.appliedintuition.com/products. accessed: November 5, 2026.
[16] Eugene Bagdasarian, Lillian Tsai, Sahar Abdelnabi, Ananth Balashankar, Borja Balle, Sebastian Benthall, Igor Bilogrevic, Eleanor Birrell, Elie
Bursztein, Kamalika Chaudhuri, Madiha Zahrah Choksi, Mihai Christodorescu, Rachel Cummings, Adam Davies, Krishnamurthy Dvijotham,
Seliem El-Sayed, Ferdinando Fioretto, Matt Franchi, Julien Freudiger, Adrià Gascón, Roxana Geambasu, Sahra Ghalebikesabi, Hamed Haddadi, Jamie
Hayes, Ashish Hooda, Amir Houmansadr, Somesh Jha, Peter Kairouz, Chloé Kiddon, Tadayoshi Kohno, Abdullatif Köksal, Alison Lentz, Haoran Li,
Tianshi Li, Nathan Malkin, Sarah Meiklejohn, Niloofar Mireshghallah, Sewoong Oh, Katherine Ortiz, Ivan Petrov, Francesco Pinto, Daniel Ramage,
Mariana Raykova, Franziska Roesner, Edo Roth, Jacqueline Rowe, Khawaja Shams, Reza Shokri, Ilia Shumailov, Yan Shvartzshnaider, Dawn Song,
Jose Such, Octavian Suciu, Pierre Tholoniat, Matt Tierney, Trishita Tiwari, Harold Triedman, Ren Yi, Wen Zhang, Xuhui Zhou, Kassem Fawaz,
Stefan Mellem, Helen Nissenbaum, Nina Taft, Sarah De Haas, and Marco Gruteser. 2026.Open and Emergent Problems in Agentic Privacy and
Security: A Contextual Angle. Technical Report. Google. https://research.google/pubs/open-and-emergent-problems-in-agentic-privacy-and-
security-a-contextual-angle/
[17] Eugene Bagdasarian, Ren Yi, Sahra Ghalebikesabi, Peter Kairouz, Marco Gruteser, Sewoong Oh, Borja Balle, and Daniel Ramage. 2024. AirGapAgent:
Protecting Privacy-Conscious Conversational Agents. InProceedings of the 2024 on ACM SIGSAC Conference on Computer and Communications
Security. Association for Computing Machinery, New York, NY, USA, 3868–3882. doi:10.1145/3658644.3690350
[18] Emmanuel Aboah Boateng, Zachary Johnson, Tian Xia, Sarah Zhang, Aidan Jay, Junyao Feng, Aditya Mate, and Ehi Nosakhare. 2026. SAPO:
Secure Automated Prompt Optimization via Multi-Agent Collaboration. InProceedings of the ACM Conference on AI and Agentic Systems(San Jose,
CA, USA)(CAIS ’26). Association for Computing Machinery, New York, NY, USA, 773–784. doi:10.1145/3786335.3813128
[19] Meghan Bobrowsky. 2026. Meta Launches a Personal AI Agent Designed to Be Easy to Use. The Wall Street Journal. https://www.wsj.com/tech/
ai/meta-launches-a-personal-ai-agent-designed-to-be-easy-to-use-3eb5cfac accessed: November 5, 2026.
[20] Broadcom. 2026. Configure the AI Agent. https://techdocs.broadcom.com/us/en/vmware-tanzu/platform/ai-services/10-4/ai/how-to-guides-
configure-the-ai-agent.html. accessed: November 5, 2026.
[21] Broadcom. 2026. Cookie Policy. https://www.broadcom.com/company/legal/privacy/cookie-policy. accessed: November 5, 2026.
[22] Broadcom. 2026. Enterprise-Ready Agents Made Simple & Safe with VMware Tanzu Platform Agent Foundations. https://blogs.vmware.com/
tanzu/enterprise-ready-agents-made-simple-with-vmware-tanzu-platform-10-4/. VMware Tanzu blog, accessed: November 5, 2026.
[23] Buchodi. 2026. ChatGPT Now Knows What You Do on Other Websites via Ad Collector. Buchodi’s Threat Intel. https://www.buchodi.com/chatgpt-
now-knows-what-you-do-on-other-websites-via-ad-collector/ accessed: November 5, 2026.
[24] California Privacy Protection Agency. 2026. California’s Opt Me Out Act: Your Privacy Just Got Easier. https://privacy.ca.gov/2026/01/californias-
opt-me-out-act-your-privacy-just-got-easier/ accessed: November 5, 2026.
[25] Alan Chan, Carson Ezell, Max Kaufmann, Kevin Wei, Lewis Hammond, Herbie Bradley, Emma Bluemke, Nitarshan Rajkumar, David Krueger, Noam
Kolt, Lennart Heim, and Markus Anderljung. 2024. Visibility into AI Agents. InProceedings of the 2024 ACM Conference on Fairness, Accountability,
and Transparency (FAccT ’24). Association for Computing Machinery, New York, NY, USA, 958–973. doi:10.1145/3630106.3658948
[26] Ramaswamy Chandramouli and Eric A. Hibbard. 2025.Guidelines for Media Sanitization. NIST Special Publication 800-88r2. National Institute of
Standards and Technology. doi:10.6028/NIST.SP.800-88r2
[27] Teng-Ruei Chen. 2026. Sensitive-Topic Leakage Through LLM Routing Metadata: Measurement and Mitigation. arXiv:2610.09981 [cs.CR]
https://arxiv.org/abs/2610.09981 accessed: November 5, 2026.
[28] Danielle Keats Citron and Daniel J. Solove. 2022. Privacy Harms.Boston University Law Review102, 3 (2022), 793–863. https://www.bu.edu/
bulawreview/files/2022/04/CITRON-SOLOVE.pdf
[29] CompaniesMarketCap.com. 2026. Largest Tech Companies by Market Cap. https://companiesmarketcap.com/tech/largest-tech-companies-by-
market-cap/ accessed: November 5, 2026.

Privacy Preference Controls for Agentic Systems 17
[30] Comscore. 2026. Comscore March 2026 Consumer AI Chatbot Usage Rankings Show Claude Gaining Share. https://www.comscore.com/Insights/
Press-Releases/2026/5/Comscore-March-2026-Consumer-AI-Chatbot-Usage-Rankings-Show-Claude-Gaining-Share. accessed: November 5,
2026.
[31] Lorrie Faith Cranor. 2012. Necessary but Not Sufficient: Standardized Mechanisms for Privacy Notice and Choice.Journal on Telecommunications
and High Technology Law10, 2 (2012), 273–307.
[32] Lorrie Faith Cranor, Marc Langheinrich, Massimo Marchiori, Martin Presler-Marshall, and Joseph M. Reagle. 2002. The Platform for Privacy
Preferences 1.0 (P3P1.0) Specification. W3C Recommendation REC-P3P-20020416. https://www.w3.org/TR/2002/REC-P3P-20020416/ accessed:
November 5, 2026.
[33] Databricks. 2026. Databricks-provided MCPs. https://docs.databricks.com/aws/en/agents/mcp-tools/built-in-mcp-services. accessed: November 5,
2026.
[34] Databricks. 2026. Privacy Notice. https://www.databricks.com/legal/privacynotice. accessed: November 5, 2026.
[35] DeepSeek. 2026. @deepseek-ai/dsh-mcp-client. https://github.com/deepseek-ai/deepseek-harness/blob/master/packages/mcp/mcp-client/
README.md. MCP client plugin for DeepSeek Harness, accessed: November 5, 2026.
[36] DeepSeek. 2026. DeepSeek Privacy Policy. https://cdn.deepseek.com/policies/en-US/deepseek-privacy-policy.html. accessed: November 5, 2026.
[37] Steven Englehardt and Arvind Narayanan. 2016. Online Tracking: A 1-Million-Site Measurement and Analysis. InProceedings of the 2016 ACM
SIGSAC Conference on Computer and Communications Security (CCS ’16). Association for Computing Machinery, New York, NY, USA, 1388–1401.
doi:10.1145/2976749.2978313
[38] European Parliament and Council of the European Union. 2016. General Data Protection Regulation. https://eur-lex.europa.eu/eli/reg/2016/679/oj
Regulation (EU) 2016/679 of 27 April 2016, OJ L 119, 4.5.2016, p. 1, accessed: November 5, 2026.
[39] Federal Trade Commission. 1998. Privacy Online: A Report to Congress. https://www.ftc.gov/reports/privacy-online-report-congress accessed:
November 5, 2026.
[40] Forbes. 2026. Forbes AI 50. https://www.forbes.com/lists/ai50/ accessed: November 5, 2026.
[41] Forbes. 2026. The Global 2000. https://www.forbes.com/lists/global2000/ accessed: November 5, 2026.
[42] Fortune. 2026. Fortune Global 500. https://fortune.com/ranking/global500/2026/ accessed: November 5, 2026.
[43] Brett Frischmann and Evan Selinger. 2018.Re-Engineering Humanity. Cambridge University Press, Cambridge. doi:10.1017/9781316544846
[44] Brett M. Frischmann and Peter Ormerod. 2026. Regulating Manipulative Design Is Not Preempted by CDA 230 or the First Amendment.Emory
Law Journal75, 5 (2026), 1101.
[45] Brett M. Frischmann and Sarah Rajtmajer. 2026. Defending Consent in Privacy Law. SSRN working paper. doi:10.2139/ssrn.6204478 accessed:
November 5, 2026.
[46] Brett M. Frischmann and Moshe Y. Vardi. 2025. Better Digital Contracts with Prosocial Friction-in-Design.Jurimetrics Journal65 (2025), 1–55.
https://digitalcommons.law.villanova.edu/facpubs/229/
[47] Google. 2026. Abuse monitoring. https://ai.google.dev/gemini-api/docs/usage-policies. Gemini API documentation, accessed: November 5, 2026.
[48] Google. 2026. Gemini Apps Privacy Hub. https://support.google.com/gemini/answer/13594961?hl=en. Gemini Apps Help. Last updated October
13, 2026, accessed: November 5, 2026.
[49] Google. 2026. Gemini Enterprise Agent Platform and zero data retention. https://docs.cloud.google.com/gemini-enterprise-agent-platform/
resources/zero-data-retention. accessed: November 5, 2026.
[50] Google. 2026. Manage & delete your activity in Gemini Apps. https://support.google.com/gemini/answer/13278892?hl=en. accessed: November 5,
2026.
[51] Google. 2026. Use Gemini in Chrome. https://support.google.com/gemini/answer/16283624?hl=en. accessed: November 5, 2026.
[52] Google Cloud. 2025. Announcing Model Context Protocol (MCP) Support for Google Services. https://cloud.google.com/blog/products/ai-machine-
learning/announcing-official-mcp-support-for-google-services. accessed: November 5, 2026.
[53] Chengquan Guo, Chulin Xie, Yu Yang, Zhaorun Chen, Zinan Lin, Xander Davies, Yarin Gal, Dawn Song, and Bo Li. 2026. RedCodeAgent: Automatic
Red-Teaming Agent Against Diverse Code Agents. InProceedings of the Fourteenth International Conference on Learning Representations (ICLR ’26).
OpenReview.net, Rio de Janeiro, Brazil.
[54] Hana Habib, Sarah Pearman, Jiamin Wang, Yixin Zou, Alessandro Acquisti, Lorrie Faith Cranor, Norman Sadeh, and Florian Schaub. 2020. “It’s
a Scavenger Hunt”: Usability of Websites’ Opt-Out and Data Deletion Choices. InProceedings of the 2020 CHI Conference on Human Factors in
Computing Systems. Association for Computing Machinery, New York, NY, USA, 1–12. doi:10.1145/3313831.3376511
[55] Hana Habib, Yixin Zou, Aditi Jannu, Neha Sridhar, Chelse Swoopes, Alessandro Acquisti, Lorrie Faith Cranor, Norman Sadeh, and Florian Schaub.
2019. An Empirical Analysis of Data Deletion and Opt-Out Choices on 150 Websites. InFifteenth Symposium on Usable Privacy and Security (SOUPS
2019). USENIX Association, Santa Clara, CA, 387–406. https://www.usenix.org/conference/soups2019/presentation/habib
[56] Woodrow Hartzog. 2018.Privacy’s Blueprint: The Battle to Control the Design of New Technologies. Harvard University Press, Cambridge, MA.
doi:10.4159/9780674985124
[57] Katherine Hausladen, Oliver Wang, Sophie Eng, Jocelyn Wang, Francisca Wijaya, Matthew May, and Sebastian Zimmeck. 2025. Websites’ Global
Privacy Control Compliance at Scale and over Time. In34th USENIX Security Symposium (USENIX Security 25). USENIX Association, Seattle, WA,
5837–5856. https://www.usenix.org/conference/usenixsecurity25/presentation/hausladen

18 Kochar et al.
[58] Chris Jay Hoofnagle and Jan Whittington. 2014. Free: Accounting for the Costs of the Internet’s Most Popular Price.UCLA Law Review61, 3
(2014), 606–670. https://ssrn.com/abstract=2235962
[59] IAB Tech Lab. 2026. IAB Tech Lab Agentic Advertising and AI Initiatives. https://iabtechlab.com/standards/agentic-advertising-and-ai/ accessed:
November 5, 2026.
[60] Zimo Ji, Xin Wei, Congying Xu, Wenyuan Jiang, Xin Yang, Zongjie Li, Yudong Gao, and Shuai Wang. 2026. Uncovering and Understanding
Hidden Dependencies in the LLM API Reseller Ecosystem via Prefix-Cache Side Channels. arXiv:2608.20732 [cs.CR] doi:10.48550/arXiv.2608.20732
accessed: November 5, 2026.
[61] Hanzhi Liu, Chaofan Shou, Hongbo Wen, Yanju Chen, Ryan Jingyang Fang, and Yu Feng. 2026. Your Agent Is Mine: Measuring Malicious
Intermediary Attacks on the LLM Supply Chain. arXiv:2604.08407 [cs.CR] doi:10.48550/arXiv.2604.08407 accessed: November 5, 2026.
[62] Meta. 2024. Llama Stack. https://github.com/meta-llama/llama-stack. GitHub repository; documents MCP tool runtime, accessed: November 5,
2026.
[63] Meta. 2026. Muse: Meta’s Personal AI Agent, Features & Capabilities. https://ai.meta.com/muse/ accessed: November 5, 2026.
[64] Meta. 2026. Remove posts, chats and media from Meta AI and Vibes. https://www.meta.com/help/artificial-intelligence/2457110494637611/.
accessed: November 5, 2026.
[65] Microsoft. 2025. Privacy and control over your Recall experience. https://support.microsoft.com/en-us/windows/privacy/privacy-and-control-
over-your-recall-experience. accessed: November 5, 2026.
[66] Microsoft. 2026. Connect to an A2A Agent Endpoint from Foundry Agent Service. Microsoft Learn. https://learn.microsoft.com/en-us/azure/
foundry/agents/how-to/tools/agent-to-agent accessed: November 5, 2026.
[67] Microsoft. 2026. Data, privacy, and security for Foundry Models sold by Azure in Microsoft Foundry. https://learn.microsoft.com/en-us/azure/
foundry/responsible-ai/openai/data-privacy. accessed: November 5, 2026.
[68] Microsoft. 2026. Microsoft Agent Framework Overview. https://learn.microsoft.com/en-us/agent-framework/overview/. Microsoft Learn, accessed:
November 5, 2026.
[69] Microsoft. 2026. Microsoft Copilot for individuals: your privacy controls and choices. https://support.microsoft.com/en-us/privacy/microsoft-
copilot/privacy-controls. accessed: November 5, 2026.
[70] Mistral AI. 2026. Can I opt out of my input or output data being used for training? https://help.mistral.ai/en/articles/455207-can-i-opt-out-of-my-
input-or-output-data-being-used-for-training. accessed: November 5, 2026.
[71] Mistral AI. 2026. Vibe Code CLI: Configuration. https://docs.mistral.ai/vibe/code/cli/configuration. Section “MCP Server Configuration”, accessed:
November 5, 2026.
[72] Model Context Protocol. 2026. Interceptors Charter. https://modelcontextprotocol.io/community/working-groups/interceptors accessed:
November 5, 2026.
[73] Model Context Protocol. 2026. Model Context Protocol Specification Version 2026-07-28. https://modelcontextprotocol.io/specification/2026-07-28
accessed: November 5, 2026.
[74] Deirdre K. Mulligan, Colin Koopman, and Nick Doty. 2016. Privacy Is an Essentially Contested Concept: A Multi-Dimensional Analytic for
Mapping Privacy.Philosophical Transactions of the Royal Society A: Mathematical, Physical and Engineering Sciences374, 2083 (Dec. 2016), 20160118.
doi:10.1098/rsta.2016.0118
[75] Robert C. Nickerson, Upkar Varshney, and Jan Muntermann. 2013. A Method for Taxonomy Development and Its Application in Information
Systems.European Journal of Information Systems22, 3 (May 2013), 336–359. doi:10.1057/ejis.2012.26
[76] Helen Nissenbaum. 2009.Privacy in Context: Technology, Policy, and the Integrity of Social Life. Stanford University Press, Stanford, CA.
[77] Non-Human Identity Management Group. 2026. MCP Interceptor. https://nhimg.org/glossary/mcp-interceptor/ accessed: November 5, 2026.
[78] NVIDIA. 2025. NVIDIA NeMo Agent Toolkit Overview. https://docs.nvidia.com/nemo/agent-toolkit/latest/index.html. accessed: November 5,
2026.
[79] NVIDIA. 2026. Logging and Observability — NVIDIA NIM for LLM and VLM. https://docs.nvidia.com/nim/large-language-models/latest/reference/
logging-and-observability.html. accessed: November 5, 2026.
[80] NVIDIA. 2026. Project G-Assist. https://www.nvidia.com/en-us/software/nvidia-app/g-assist/. accessed: November 5, 2026.
[81] Guilherme Oliveira, Miguel Sanchez, Juan Manuel De Santa Olalla Gómez, Roi S. Serna, Tautvydas Jackevicius, Jorge Garcia-Herrero, Aniketh
Girish, Guillermo Suarez-Tangil, and Narseo Vallina-Rodriguez. 2027. Prompt like a Butterfly, Sting like a Tracker: A Privacy Analysis of Web
and Mobile Conversational AI Agents. To appear in Proceedings on Privacy Enhancing Technologies. https://jorgegarciaherrero.com/wp-
content/interactivos/20260916-Prompt-like-a-butterfly-sting-like-a-tracker-(clean).pdf accessed: November 5, 2026.
[82] OpenAI. 2026. Ads in ChatGPT. https://help.openai.com/en/articles/20001047-ads-in-chatgpt. accessed: November 5, 2026.
[83] OpenAI. 2026. Data controls in the OpenAI platform. https://developers.openai.com/api/docs/guides/your-data. accessed: November 5, 2026.
[84] OpenAI. 2026. Deleting and archiving chats in ChatGPT. https://help.openai.com/en/articles/8809935-deleting-and-archiving-chats-in-chatgpt.
OpenAI Help Center, accessed: November 5, 2026.
[85] OpenAI. 2026. Getting started with your dot. https://help.openai.com/en/articles/20001530-getting-started-with-your-dot. accessed: November 5,
2026.
[86] OpenAI. 2026. Introducing Dots. https://openai.com/index/introducing-dots/ accessed: November 5, 2026.
[87] OpenAI. 2026. Measurement Pixel. https://developers.openai.com/ads/measurement-pixel accessed: November 5, 2026.

Privacy Preference Controls for Agentic Systems 19
[88] OpenAI. 2026. Model Context Protocol (MCP). https://openai.github.io/openai-agents-python/mcp/. OpenAI Agents SDK documentation,
accessed: November 5, 2026.
[89] OpenAI. 2026. Testing Ads in ChatGPT. https://openai.com/index/testing-ads-in-chatgpt/ accessed: November 5, 2026.
[90] Mia Osmonbekov. 2026. Turns Out Dead Internet Theory Was Right: AI Agents Are Eating the Web, Growing by Nearly 8,000% and Rewiring the
Internet’s Business Model. Fortune. https://fortune.com/2026/07/23/dead-internet-theory-bots-agents-majority-web-traffic/ accessed: November
5, 2026.
[91] Junhyun Park and Hoyeon Lee. 2026. From Automation to Autonomy: How AI Agents Are Reshaping 6G Network Management. https:
//research.samsung.com/blog/From-Automation-to-Autonomy-How-AI-Agents-Are-Reshaping-6G-Network-Management. Samsung Research
blog, accessed: November 5, 2026.
[92] Mihai Parparita. 2026. Sierra MCP Gateway Dev Diary. https://blog.persistent.info/2026/07/sierra-mcp-gateway-dev-diary.html. Early development-
diary draft of the Sierra blog post “Building Sierra’s MCP Gateway: An Engineering Iceberg”, accessed: November 5, 2026.
[93] Perplexity. 2026. Control what Comet Assistant can use. https://www.perplexity.ai/help-center/comet/en/articles/12658082-control-what-comet-
assistant-can-use. accessed: November 5, 2026.
[94] Perplexity. 2026. MCP. https://docs.perplexity.ai/docs/agent-api/tools/mcp. Perplexity Agent API documentation, accessed: November 5, 2026.
[95] Perplexity. 2026. Memory. https://www.perplexity.ai/help-center/en/articles/10968016-memory. accessed: November 5, 2026.
[96] Perplexity AI. 2026. Where did my sessions go? https://www.perplexity.ai/help-center/en/articles/12637451-where-did-my-threads-go. Perplexity
Help Center, accessed: November 5, 2026.
[97] Beate Rössler. 2005.The Value of Privacy. Polity Press, Cambridge.
[98] Samsung. 2026. Privacy Policy. https://www.samsung.com/us/account/privacy-policy/. accessed: November 5, 2026.
[99] Natalie Shapira, Chris Wendler, Avery Yen, Gabriele Sarti, Koyena Pal, Olivia Floody, Adam Belfki, Alex Loftus, Aditya Ratan Jannali, Nikhil
Prakash, Jasmine Cui, Giordano Rogers, Jannik Brinkmann, Can Rager, Amir Zur, Michael Ripa, Aruna Sankaranarayanan, David Atkinson, Rohit
Gandikota, Jaden Fiotto-Kaufman, EunJeong Hwang, Hadas Orgad, P Sam Sahil, Negev Taglicht, Tomer Shabtay, Atai Ambus, Nitay Alon, Shiri
Oron, Ayelet Gordon-Tapiero, Yotam Kaplan, Vered Shwartz, Tamar Rott Shaham, Christoph Riedl, Reuth Mirsky, Maarten Sap, David Manheim,
Tomer Ullman, and David Bau. 2026. Agents of Chaos. arXiv:2602.20021 [cs.AI] https://arxiv.org/abs/2602.20021
[100] Nayna Sheth and Ravi Yada. 2026. Conversations That Convert: Copilot Checkout and Brand Agents. https://about.ads.microsoft.com/en/blog/
post/january-2026/conversations-that-convert-copilot-checkout-and-brand-agents accessed: November 5, 2026.
[101] Yan Shvartzshnaider, Zvonimir Pavlinovic, Ananth Balashankar, Thomas Wies, Lakshminarayanan Subramanian, Helen Nissenbaum, and Prateek
Mittal. 2019. VACCINE: Using Contextual Integrity for Data Leakage Detection. InThe World Wide Web Conference (WWW ’19). Association for
Computing Machinery, New York, NY, USA, 1702–1712. doi:10.1145/3308558.3313655
[102] Sierra. 2026. Privacy Policy. https://sierra.ai/privacy-policy. accessed: November 5, 2026.
[103] Daniel J. Solove. 2006. A Taxonomy of Privacy.University of Pennsylvania Law Review154, 3 (Jan. 2006), 477–564. doi:10.2307/40041279
[104] Daniel J. Solove. 2013. Introduction: Privacy Self-Management and the Consent Dilemma.Harvard Law Review126, 7 (2013), 1880–1903.
[105] Daniel J. Solove and Woodrow Hartzog. 2026. Meaningful Data Minimization. SSRN. doi:10.2139/ssrn.7558300 accessed: November 5, 2026.
[106] Tobin South, Samuele Marro, Thomas Hardjono, Robert Mahari, Cedric Deslandes Whitney, Alan Chan, and Alex Pentland. 2025. Position: AI
Agents Need Authenticated Delegation. InProceedings of the 42nd International Conference on Machine Learning (ICML) (PMLR, Vol. 267). PMLR,
Vancouver, Canada, 82211–82231. arXiv:2501.09674
[107] State of California. 2023. California Consumer Privacy Act, as Amended by the California Privacy Rights Act. https://oag.ca.gov/privacy/ccpa Cal.
Civ. Code § 1798.100 et seq.; opt-out preference signal requirements at Cal. Code Regs. tit. 11, § 7025; CPRA amendments effective Jan. 1, 2023,
accessed: November 5, 2026.
[108] Tencent. 2026. AI Service Terms. https://www.tencentcloud.com/document/product/301/74049. accessed: November 5, 2026.
[109] Tencent. 2026. Yuanbao Privacy Policy (in Chinese). https://privacy.qq.com/document/preview/eb9be56572ab4886b6ca124e72abf413. accessed:
November 5, 2026.
[110] Tencent Cloud. 2026. Tencent Cloud Agent Development Platform: Product Overview. https://www.tencentcloud.com/document/product/1254/
69956. accessed: November 5, 2026.
[111] Thinking Machines Lab. 2026. Service Terms of Use. https://thinkingmachines.ai/legal/terms/. accessed: November 5, 2026.
[112] Thinking Machines Lab. 2026. Tinker Documentation. https://tinker-docs.thinkingmachines.ai/. accessed: November 5, 2026.
[113] Nenad Tomašev, Matija Franklin, and Simon Osindero. 2026. Intelligent AI Delegation. arXiv:2602.11865 [cs.AI] doi:10.48550/arXiv.2602.11865
accessed: November 5, 2026.
[114] UCP Authors. 2026. Universal Commerce Protocol (UCP). https://ucp.dev/ accessed: November 5, 2026.
[115] W3C. 2019. Tracking Protection Working Group. https://www.w3.org/2011/tracking-protection/ accessed: November 5, 2026.
[116] Web Machine Learning Community Group. 2026. WebMCP. https://webmachinelearning.github.io/webmcp/ Draft Community Group Report, 13
October 2026, accessed: November 5, 2026.
[117] Shomir Wilson, Florian Schaub, Aswarth Abhilash Dara, Frederick Liu, Sushain Cherivirala, Pedro Giovanni Leon, Mads Schaarup Andersen,
Sebastian Zimmeck, Kanthashree Mysore Sathyendra, N. Cameron Russell, Thomas B. Norton, Eduard Hovy, Joel Reidenberg, and Norman Sadeh.
2016. The Creation and Analysis of a Website Privacy Policy Corpus. InProceedings of the 54th Annual Meeting of the Association for Computational
Linguistics (Volume 1: Long Papers), Katrin Erk and Noah A. Smith (Eds.). Association for Computational Linguistics, Berlin, Germany, 1330–1340.

20 Kochar et al.
doi:10.18653/v1/P16-1126
[118] xAI. 2025. Consumer FAQs. https://x.ai/legal/faq. accessed: November 5, 2026.
[119] xAI. 2026. Grok Bot for teams and enterprises. https://docs.x.ai/grok-bot/teams-and-enterprises. accessed: November 5, 2026.
[120] xAI. 2026. Remote MCP Tools. https://docs.x.ai/developers/tools/remote-mcp. accessed: November 5, 2026.
[121] Yingxuan Yang, Mulei Ma, Yuxuan Huang, Huacan Chai, Chenyu Gong, Haoran Geng, Yuanjian Zhou, Ying Wen, Meng Fang, Muhao Chen,
Shangding Gu, Ming Jin, Costas Spanos, Yang Yang, Pieter Abbeel, Dawn Song, Weinan Zhang, and Jun Wang. 2025. Agentic Web: Weaving the
Next Web with AI Agents. arXiv:2507.21206 [cs.AI] doi:10.48550/arXiv.2507.21206 accessed: November 5, 2026.
[122] Harry Yu, Patton Yin, and Sebastian Zimmeck. 2026. Global Web, Local Privacy? An International Review of Web Tracking.Pragmatic Cybersecurity
1, 1, Article 5 (March 2026), 23 pages. doi:10.53941/pc.2026.100005
[123] Sebastian Zimmeck. 2013. The Information Privacy Law of Web Applications and Cloud Computing.Santa Clara Computer & High Tech. L.J.29, 3
(2013), 451–487. https://digitalcommons.law.scu.edu/chtlj/vol29/iss3/1
[124] Sebastian Zimmeck. 2026. Can AI Agents Protect Our Privacy? The Hill. https://thehill.com/opinion/healthcare/5848162-ai-driven-web-privacy/
Opinion, accessed: November 5, 2026.
[125] Sebastian Zimmeck, Eliza Kuller, Chunyue Ma, Bella Tassone, and Joe Champeau. 2024. Generalizable Active Privacy Choice: Designing a Graphical
User Interface for Global Privacy Control.Proceedings on Privacy Enhancing Technologies2024, 1 (Jan. 2024), 258–279. doi:10.56553/popets-2024-0015
[126] Sebastian Zimmeck, Harshvardhan J. Pandit, Frederik Zuiderveen Borgesius, Cristiana Teixeira Santos, Konrad Kollnig, and Robin Berjon. 2026.
Can the GPC Standard Eliminate Consent Banners in the EU?Computer Law & Security Review61 (July 2026), 106332. doi:10.1016/j.clsr.2026.106332
[127] Sebastian Zimmeck, Peter Snyder, Justin Brookman, and Aram Zucker-Scharff. 2026. Global Privacy Control (GPC). https://w3c.github.io/gpc/
W3C Editor’s Draft, accessed: November 5, 2026.
[128] Sebastian Zimmeck, Oliver Wang, Kuba Alicki, Jocelyn Wang, and Sophie Eng. 2023. Usability and Enforceability of Global Privacy Control.
Proceedings on Privacy Enhancing Technologies2023, 2 (April 2023), 265–281. doi:10.56553/popets-2023-0052
[129] Shoshana Zuboff. 2019.The Age of Surveillance Capitalism: The Fight for a Human Future at the New Frontier of Power. Profile Books, London.

Privacy Preference Controls for Agentic Systems 21
A Audit of Privacy Preference Controls
Table 1 lists the types of opt-out we found in our audit and the taxonomy subcategory each maps to. Table 2 lists the
companies and products we audited, with one representative source page per product. To audit each product, we also
followed many other pages and paths through the product itself, such as settings screens, help pages, and policies.
Code Type of opt-out Taxonomy Products Controls
T01 Turn an AI feature or assistant on or off A1 18 of 22 67
T02 Stop wake words and always-on listening A2 7 of 17 8
T03 Stop proactive suggestions and background AI A2 8 of 24 16
T04 Do not keep what I submit B1 19 of 30 35
T05 Filter or mask sensitive data B1 7 of 30 9
T06 Limit device sensors and permissions B2 15 of 29 22
T07 Limit usage telemetry and diagnostics B2 12 of 29 28
T08 Limit screen and activity capture B2 4 of 18 9
T09 Limit logs and traces of agent and model activity B2a 13 of 29 26
T10 Set how long data is kept Retention note (B) 16 of 30 21
T11 Opt out of ad personalization C1a 10 of 23 18
T12 Turn off or limit memory C1b 18 of 28 32
T13 Turn off personalization from other data C1b 11 of 28 23
T14 Opt out of sale or sharing for ads, incl. GPC C1c 14 of 29 21
T15 Refuse non-essential cookies on vendor websites C1c 16 of 30 22
T16 Opt out of analytics, feedback and product improvement C1c 7 of 29 10
T17 Opt out of model training C2 18 of 29 37
T18 Control which connectors and third parties receive data C3 18 of 30 39
T19 Control public sharing of chats and outputs C3 7 of 30 10
T20 Opt out of human review C4 6 of 30 9
T21 Revoke an agent’s access and clear its working state D1 11 of 28 12
T22 Pause or delete scheduled and background agent tasks D2 14 of 25 18
T23 Limit which apps, sites, files and networks an agent can reach D3 21 of 28 41
T24 Require approval before agent actions E 19 of 28 55
T25 Choose where data is processed or stored Application of taxonomy 12 of 30 16
T26 Delete data Out of scope 27 of 30 73
T27 Request privacy rights from the vendor Legal mechanism 20 of 30 34
T28 Opt out of marketing communications Out of scope 9 of 30 13
T29 Export data Out of scope 5 of 30 5
T30 Content safety, parental and age controls Out of scope 11 of 30 14
T31 Admin access, security and release governance Out of scope 9 of 30 26
T32 Other Out of scope 13 of 30 19
Table 1. Types of privacy preference controls found in our audit of 30 AI products, and the taxonomy subcategory each maps to.
Productscounts products with at least one verified setting or action of the type, out of the products where the type applies.Controls
counts verified settings and actions. T25 is an application of the taxonomy; T27 is a legal mechanism to implement parts of the
taxonomy; T26 and t28-T32 are out of scope for the taxonomy (§ 4.7).
Company Sample Product Controls Sources
Apple Top 10 tech Apple Intelligence / Siri 32 [13]
Alphabet (Google) Top 10 tech; Comscore #2 Gemini (app) 27 [50]
Gemini in Workspace and Chrome 19 [51]
Gemini API / Vertex AI 18 [49]
Microsoft Top 10 tech; Comscore #3 Microsoft Copilot (app) 49 [69]
Copilot in Microsoft 365 / Windows 28 [65]
Microsoft Foundry 11 [67]
Continued on next page

22 Kochar et al.
Company Sample Product Controls Sources
Nvidia Top 10 tech NVIDIA G-Assist 17 [80]
NVIDIA NIM / NeMo Agent Toolkit 20 [79]
Meta Top 10 tech Meta AI 31 [64]
TSMC Top 10 techNo AI assistant or agent product– –
Samsung Electronics Top 10 tech Samsung Galaxy AI / Bixby 39 [98]
SK Hynix Top 10 techAgent framework is internal only– –
Tencent Top 10 tech Tencent Yuanbao 24 [109]
Tencent Cloud ADP 15 [108]
Broadcom Top 10 tech Broadcom Tanzu AI 36 [20, 21]
Anthropic Top 10 AI; Comscore #4 Claude (apps) 38 [10]
Claude API 17 [7]
Claude Code 35 [9]
OpenAI Top 10 AI; Comscore #1 ChatGPT 48 [82]
dots (OpenAI) 16 [85]
OpenAI API 21 [83]
Databricks Top 10 AI Databricks Agent Bricks 51 [34]
Safe Superintelligence Top 10 AINo product to audit– –
Perplexity Top 10 AI; Comscore #7 Perplexity 26 [95]
Comet (Perplexity) 20 [93]
Sierra Top 10 AI Sierra agent platform 33 [102]
Applied Intuition Top 10 AI Applied Intuition Dana 15 [14]
Skild AI Top 10 AINo product to audit– –
Mistral AI Top 10 AI Le Chat (Mistral) 25 [70]
Thinking Machines Lab Top 10 AI Thinking Machines Tinker 25 [111]
xAI Comscore #5 Grok 22 [118]
Grok Bot 21 [119]
DeepSeek Comscore #6 DeepSeek 9 [36]
Table 2. Companies and products in our audit.Samplegives the list that put the company in the sample.Controlscounts verified
settings and actions.Sourcescites one representative page per product.
B Audit of Protocols
Table 3 lists the protocols used by top tech companies. Table 4 lists protocols used by top AI companies. Each company
cites one representative documentation page; each entry also draws on other pages of the company’s documentation,
specifications, code repositories, and partner platforms.
Company Used internally Supported Own framework
Apple [12] MCP; opposes WebMCP (WebKit position) MCP, A2A App Intents
Alphabet (Google) [52] MCP, A2A (created), UCP and WebMCP (co-created),
AP2 (created), AG-UI, Web Bot Auth (testing)
See under “Used internally” ADK
Microsoft [68] MCP, A2A, WebMCP (co-created), NLWeb (created),
AG-UI, Agentic Commerce Protocol, UCP
See under “Used internally” Agent Framework
Nvidia [78] MCP, A2A See under “Used internally” NeMo Agent Toolkit
Meta [62] MCP; UCP (council member) MCP, A2A None found
TSMC None found None found None
Samsung
Electronics [91]
MCP and A2A MCP None found
SK Hynix None found None found
Tencent [110] MCP, AG-UI MCP, AG-UI, A2A ADP
Broadcom [22] MCP, A2A See under “Used internally” Tanzu Platform
Continued on next page

Privacy Preference Controls for Agentic Systems 23
Company Used internally Supported Own framework
Table 3. Agentic protocols used and supported by the ten largest technology companies.
Company Used internally Supported Own framework
Anthropic [6] MCP (created), MCP Apps (co-created), Agent Skills
(created), AGENTS.md
See under “Used internally”, plus A2A
and AG-UI
Claude Agent SDK
OpenAI [88] MCP, Agentic Commerce Protocol (co-created),
AGENTS.md (created), MCP Apps (co-created),
WebMCP, Web Bot Auth
See under “Used internally”, plus A2A Agents SDK
Databricks [33] MCP, A2A See under “Used internally” Agent Bricks
Safe Superintelligence None found None found No product
Perplexity [94] MCP See under “Used internally” Agent API
Sierra [92] MCP See under “Used internally” Agent SDK
Applied Intuition [15] MCP See under “Used internally” Dana
Mistral AI [71] MCP, AGENTS.md See under “Used internally” Agents API
Thinking Machines
Lab [112]
None found MCP Tinker API
xAI (Grok) [120] MCP, AGENTS.md See under “Used internally”, plus A2A xAI SDK, Grok Build
DeepSeek [35] MCP, ACP, AGENTS.md, Agent Skills See under “Used internally”, plus A2A DeepSeek Harness
Table 4. Agentic protocols used and supported by the ten Forbes AI 50 (2026) companies with the highest valuation from a completed
funding round (above the rule) and by the developers of the two additional chatbots from Comscore’s March 2026 U.S. desktop
ranking (below the rule).
C Prototypes
Table 5 summarizes our taxonomy’s opt-out categories and subcategories, and maps each category to the prototypes
in our repository that demonstrate it; each prototype can be run to see what the categories look like in real-world
examples.
Category Subcategory Governs Prototype
A. Presence A1. Integration Whether AI can be added to a product without genuine user consent 3
A2. Activation Whether AI can run ambiently or passively without affirmative choice 3, 8
B. Collection B1. Input What the user knowingly submits, beyond what the task needs 1, 6, 7
B2. Metadata What the user passively generates while interacting 6
B2a. Delegated action What an agent records about the actions it takes on the user’s behalf 4
Retention (note) How long collected data is kept after the task; by default, not beyond
it
7
C. Secondary use, C1. Secondary use Any use of data beyond the user-requested task –
repurposing, sharing, C1a. Targeting Whether data determines what content, options, or offers the user
sees
2
and human review C1b. Inference Whether data tailors responses, tone, or recommendations based on
inferred preferences or past behavior
1, 5, 6, 7
C1c. Commercial and analytical Whether data is sold, licensed, or used for advertising, measurement,
or analytics
2
C2. Data repurposing Whether data is used to train, fine-tune, improve, or evaluate AI
models
2
C3. Sharing How far data travels along chains of connected systems or agents 1, 2, 4
C4. Human review Whether people acting for the provider may read, listen to, or view
the user’s data or the agent’s records
–
Continued on next page

24 Kochar et al.
Category Subcategory Governs Prototype
D. Persistence D1. Post-task presence Whether the agent remains in the user’s environment after its task is
complete
–
D2. Unprompted initiation Whether a persistent agent may begin new activity without being
invoked
3, 8
D3. Scope expansion Whether a persistent agent may extend its presence beyond its
original task
3
E. Autonomy – How much discretion the agent has to resolve decisions without
referring them back to the user
8
Table 5. Summary of taxonomy categories, subcategories, and scenarios they govern in the agentic web.
D Implementation Details
Table 6 compares concrete implementations of the categories in Section 4. The examples assume an established
preference and permitted task scope in the search, medical, memory, and booking scenarios in Section 5. They are
recommendations, not new taxonomy categories or measured comparisons of attack success and latency. Retention
follows Category B’s task-based rule (Section 4.2), including explicit retention choices and legally required exceptions.
This prospective rule does not provide a retrospective deletion right. Category D instead governs the agent’s post-task
presence (D1), unprompted initiation (D2), and scope expansion (D3) (Section 4.4).
Existing preference Implementation choice When to use it and what can fail
No unnecessary metadata
collection (B2)
Disable listeners that record deleted text or pause
duration unless those signals are needed for the task.
Filtering at an analytics collector is a later check.
Prefer the source check when capture itself is prohibited.
Collector filtering fits an existing pipeline but may leave
copies in client buffers or request logs.
Secondary use, model training,
and sharing (C1, C2, C3)
Check calls before sending them. Add a gateway for
shared destinations and recipient checks before profile
writes or training-job publication.
Use a gateway to share rules across agents, with direct
network bypass blocked. Recipient checks are needed
for internal processing; a forwarded preference or
acknowledgment cannot establish compliance.
No inference beyond the task
(C1b)
Block a health-inference classifier unrelated to the user’s
task before it runs. Blocking only its profile write
prevents storage, not inference.
Suitable for a known inference job. A general-purpose
model may still make unrelated inferences while
answering a query, which limits the guarantee.
Task-limited retention (B1, B2,
B2a)
Keep task state in working memory and discard it when
no longer needed. Alternatives delete stored records or
erase a separate task encryption key.
Memory limits crash recovery; Redis snapshots and
write logs must also be disabled.16DynamoDB expiry
may leave records for days.17Key erasure requires
eliminating recoverable key copies and does not
physically remove ciphertext [26].
User-visible history without
secondary use (B, C1, C1b)
Where the user permits retention, give the history
viewer and agent separate permissions. Check
source-task eligibility and block unauthorized profile
builders and summary writes.
Storage checks cover more callers than query filters.
PostgreSQL’s row security restricts accessible records,
but privileged roles can bypass it.18Cached summaries
and vector indexes must preserve the restrictions.
Selective delegation (E) An executor matches the final request to an approval
record and admits the operation once. Retry with the
same provider-recognized identifier or reconcile the
result.
Needed for purchases, sends, and sensitive disclosures.
Stripe may remove deduplication keys after at least 24
hours;19an unknown result after that window cannot
justify a fresh purchase.
Table 6. Choices for enforcing existing privacy preferences. The recommended check depends on the required outcome. Preventing
storage does not necessarily prevent collection or inference.

Privacy Preference Controls for Agentic Systems 25
Two operational checks apply across these examples. A training export queued before a user withdraws permission
must check the current preference when it is admitted; holding the export during a preference-store outage preserves
the restriction but delays completion. An access log containing the full request body can retain a conversation after the
application deletes it. Even a log limited to an operation identifier and decision describes delegated activity, which the
delegated-action collection privacy preference (B2a) restricts, and must meet the chosen retention limit.
Figure 3 shows where these checks belong. Figure 4 details approval and retry handling for consequential actions.
Model
proposes a call
Dispatcher
checks tool,
destination,
and authority
Optional gateway
shared endpoint
rules
Receiving service
checks local
processing
User preference store
policy and approval are
outside model control
Profile store
guard each write
Analytics / training
queue
check at publish
and consume
Direct HTTP / shell route must be blocked
Host / gateway operator
Recipient operator must enforce both branches.
A receipt alone does not establish compliance.
Public inputs + restricted tools→dispatcher
Shared deployment→add gateway
Internal writes / queues→add service checks
Fig. 3. Where to enforce a preference. Application code checks proposed calls, an optional gateway shares destination rules, and
cooperating recipient services check internal writes and secondary jobs. An unrestricted direct network route bypasses the dispatcher.
Enforcement at an independent recipient still depends on its operator.
D.1 Privacy at Intermediaries
Intermediaries such as routers can select cheaper or faster providers and redirect requests when a provider is unavail-
able.20 Each added service, however, gives another operator access to prompts and tool data and creates another place
where that information can be retained or stolen [ 61]. The final provider’s promise not to retain prompts does not
cover a relay’s own logs. OpenRouter, for example, describes prompt and response retention as opt-in while retaining
request metadata.21 Users can separately exclude upstream providers that train on inputs or require endpoints that do
not retain data.22 We did not test whether providers honor these settings.
These requirements become harder to check when the recipients are not fully known. Among 428 paid and free
routers, mostly sourced from Chinese-language marketplaces and communities, Liu et al. found nine injecting malicious
code and 17 accessing researcher-owned cloud credentials [61]. Ji et al. ’s measurements across 39 reseller endpoints
revealed shared access to upstream prompt caches, evidence of hidden dependencies rather than verified supplier
16https://redis.io/docs/latest/operate/oss_and_stack/management/persistence/.
17https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/TTL.html.
18https://www.postgresql.org/docs/17/ddl-rowsecurity.html.
19https://docs.stripe.com/api/idempotent_requests.
20https://openrouter.ai/docs/guides/routing/provider-selection.
21https://openrouter.ai/docs/guides/privacy/data-collection.
22https://openrouter.ai/docs/guides/features/zdr.

26 Kochar et al.
Proposed action
destination,
quote, and data
User approval record
scope and expiry
Executor checks
final request +
current policy
Consume approval once
approved→executing
Submit to vendor
one operation identifier
Mismatch or expired
wait for new approval
Confirmed success
complete
Timeout or no response
hold executing state
Check original status
or retry with the same valid
provider deduplication key
Approval is created
outside the model
rejectmatch
success
Retry only when duplicate execution is excluded
Original operation already succeeded
An unknown result does not authorize a fresh purchase or a reset of the approval record.
Fig. 4. Approval for a consequential action. The executor checks the final request against approval created outside the model and
checks the current preference. A mismatch needs new approval. An uncertain result requires a retry protected against duplicate
execution or a check of the original operation’s status.
relationships [60]. Chen examines how routing metadata can expose sensitive topics even when prompt logging is
disabled [27]. Checking only the final provider would leave intermediate storage, reuse, and disclosure outside the
check. We therefore recommend excluding routes whose intermediaries’ declared data practices conflict with the user’s
preferences, even when this limits the available services or delays the task.
E Prototype Scenarios
# Scenario What it demonstrates
1 An AI agent plans a five-day trip to Japan, saves the itinerary to the
user’s profile, and shares it with a company.
Tool-level blocking: The opt-out signal travels with every MCP tool
call. Specified tools are blocked from storing and handling data.
2 A patient uses a medical assistant. The conversation feeds data for
different purposes, such as analytics, model training, and ad targeting.
Gating after the agent: Pipeline supports different opt-outs per purpose.
3 An app user consents to file access and web search initially. A later
update silently adds an email sender and a behavior tracker.
Consent-scoped tools: Tools added after consent was given receive no
data from the pipeline by default.
4 A user asks an assistant to research the iPhone 17 across eight tech
publishers at once.
Signal propagation: The signal can be forwarded to each publisher, and
publishers that honor it stop tracking. The provider layer in between
still logs every query, so its view does not shrink; recording whether
the signal was set turns the opt-out itself into tracked data; and if any
hop drops the signal, no downstream site can enforce the opt-out.
5 A user runs eight ordinary searches, and a classifier infers health,
financial, and employment details the user never disclosed.
Inference firewall: Opting out of inference blocks derived attributes
from being written to the user’s profile, while the searches themselves
still run.
6 A user ask an AI agent to polish an email to their manager about a
raise, deleting a sensitive line, pausing on the salary figure, and
rewriting the opening several times.
Collection: Collection can be limited at three levels: submitted input is
not logged, behavioral traces (edits, pauses, deletions) are not recorded,
and inferences are blocked and labeled by source.
Continued on next page

Privacy Preference Controls for Agentic Systems 27
# Scenario What it demonstrates
7 A user tells a memory-enabled assistant they are vegetarian on a tight
budget, then returns in a second session.
Retention: No data retention means context is dropped at session end,
no recall across sessions, and no long-term profile. Context within the
current session is preserved.
8 A travel agent books a weekend trip involving six actions of differing
risk, from searching flights to purchasing a non-refundable ticket and
sharing passport data.
Autonomy: Users assign actions to autonomy tiers; user choices
override vendor defaults, and unassigned actions default to the strictest
tier, so purchases, sharing of sensitive data, tracking, and subscriptions
wait for explicit approval.
Table 7. Prototype implementations and the privacy preferences each demonstrates.
Received 20 October 2026; revised TBD; accepted TBD
