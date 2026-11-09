---
title: 'Appearing Legitimate is Not Enough: Interrogating Synthetic Agents in Representational Processes
  through a Participatory Design Lens'
url: https://arxiv.org/abs/2608.17099
category: digital-marketing
subcategory: empirical
date: 2026-08
venue: ''
authors:
- Aditya Nayak
- Aditi Vashistha
- Alissa Centivany
- Aakash Gautam
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.17099
pages: 13
chars: 73726
fetched_at: '2026-11-08T13:20:57+00:00'
kb_version: 1
---

# Appearing Legitimate is Not Enough: Interrogating Synthetic Agents in Representational Processes through a Participatory Design Lens

Appearing Legitimate is Not Enough: Interrogating Synthetic Agents in
Representational Processes through a Participatory Design Lens
Aditya Nayak*1, Aditi Vashistha*2, Alissa Centivany2, Aakash Gautam1
1University of Pittsburgh
2FIMS, Western University
aditya.nayak@pitt.edu, avashi4@uwo.ca, acentiva@uwo.ca, aakash@pitt.edu
Abstract
Synthetic agents built atop LLM-based foundation mod-
els are gaining popularity as substitutes for human par-
ticipants across research contexts, including user-testing,
market-research, computational social science, surveys, and
qualitative research. We are also witnessing an extension of
synthetic agents into experimental implementations of pol-
icy consultation, jury deliberation, humanitarian diplomacy,
and similar contexts where human participation and repre-
sentation are central to the perceived legitimacy of the in-
stitutional processes. The value of participation extends be-
yond informational contributions and consensus generation;
participation is a necessary, legitimizing condition for demo-
cratic political institutions and processes. Treating synthetic
agents as human substitutes raises serious political, represen-
tational, and ethical concerns. Participatory Design’s modes
of engagement — probing, priming, understanding, and gen-
erating — offer helpful tools for engaging with representa-
tional questions of personhood. We apply the lens to three
case studies of synthetic agents substituting for personhood
at varying representational scales: local policy, enterprise jury
deliberation, and global diplomacy. We argue that legitimacy
and personhood are integral and mutually constitutive while
identifying the ethical, representational, and methodological
risks of using synthetic agents in representational processes.
We conclude by proposing soft and hard boundaries for de-
signing oversight on LLMs and synthetic agents in represen-
tational processes.
Introduction
Large Language Models and agents built on top of the foun-
dational models are increasingly being deployed as substi-
tutes for human participants in domains like user-testing
(Yang 2026), market-research (Simile.ai 2026), computa-
tional social science (Wang, Morgenstern, and Dickerson
2025), surveys (Ball et al. 2025), and qualitative research
(Nguyen and Welch 2026). Synthetic agents, that is, LLM-
based systems trained or augmented with domain-specific
data to mimic context-bound personas, are now being ex-
tended into experimental implementations of policy consul-
tation (Reshef Kera et al. 2024), jury deliberation (Ersoz
2026), and humanitarian diplomacy (Albrecht 2025). Their
*These authors contributed equally.
Copyright © 2026, Association for the Advancement of Artificial
Intelligence (www.aaai.org). All rights reserved.
proponents claim these systems can perceive contextual en-
vironments, make decisions, and take actions in ways that
approximate human decision-making.
The use of synthetic agents is often justified as a solution
to the difficulty of recruiting suitable participant groups. One
could argue that in low-risk domains, like market research,
the stakes of this substitution are limited to participant rep-
resentativeness and data quality (Maden 2026; Su 2026) for
building better products. While that in itself is contentious,
the use of synthetic agents in domains like policy making,
diplomatic consultation, and legal juries is alarming. These
are deliberative and representational processes where partic-
ipation and representation extend beyond informational con-
tribution and consensus generation. We use representational
process to mean a deliberative or decision-making process
whose legitimacy is procedural. It derives from the inclusion
and participation of those affected by the decision instead
of the correctness of the outcome (Habermas 1996; Young
2000). Participation is a necessary and legitimizing condi-
tion of the democratic process, and importantly, it is funda-
mental to the institutional legitimacy these processes claim.
Substituting synthetic agents for human participants in these
contexts raises political, representational, and ethical con-
cerns, including the exclusion of the lived experiences of the
marginalized groups who would otherwise have been partic-
ipants.
The concept of personhood has been made and remade
whenever societies need new vocabulary for new circum-
stances (Leibo et al. 2025). But most conceptions of person-
hood in moral and legal domains rest on consciousness, in-
tentionality, the capacity for reciprocal moral relations, and
responsibility and accountability for the consequences of
one’s actions (Baeyaert 2025; Bronner-Martin 2025). Syn-
thetic agents do not possess these properties, and prior work
argues that this limitation cannot be overcome through tech-
nical fixes (Bronner-Martin 2025). Despite this, synthetic
agents are being deployed in roles that presuppose them.
In this paper, we investigate how synthetic agents come
to appear legitimate as substitutes for human participants in
representational processes. We approach this through three
case studies at different scales, namely local policy (Ana,
a community-voice chatbot), enterprise legal deliberation
(Synthetic Juror), and global diplomacy (Ask Amina and
Ask Abdalla). To analyze these cases, we draw on Sanders
arXiv:2608.17099v1  [cs.HC]  17 Aug 2026

et al.’s framework of Participatory Design (PD), which iden-
tifies four modes through which a participant is produced
from a person, namely,probing, priming, understanding,
andgenerating(Sanders, Brandt, and Binder 2010). These
modes give us process-oriented perspectives to evaluate
what representational work the synthetic agents are doing,
and what they leave out. We ask two research questions:
RQ1: How do synthetic agents in representational processes
construct an appearance of legitimate participation?RQ2:
What boundaries should guide the design and deployment
of synthetic agents in representational processes?
Across the three cases, we trace a four-step process
through which personhood is manufactured. First, through
the framing of the problem. Then, through the institutional-
ized curation of data. This is followed by the design of user
encounters with the persona. Finally, through the technical
evaluation of validity. We argue that these four steps col-
lectively producemanufactured personhood, an appearance
of legitimate participation that bypasses the representational
processes from which institutional legitimacy is derived. We
contrast our position against existing evaluation frameworks
for synthetic agents, such asbelievability(Xiao et al. 2024),
faithfulness(Maden 2026; Agarwal, Tanneru, and Lakkaraju
2024),plausibility(Agarwal, Tanneru, and Lakkaraju 2024),
andalgorithmic fidelity(Argyle et al. 2023), all of which
cannot detect this bypass because they measure similarity of
outputs rather than the integrity of the underlying processes.
With this paper, we make three contributions. First, by ex-
amining three case studies, we offer a four-step account of
how synthetic agents manufacture personhood across rep-
resentational scales. Second, we use the PD modes of en-
gagement to develop a process-oriented critique of synthetic
agents, complementing the outcome-centric evaluations that
dominate the existing literature. Third, we propose desider-
ata for design consisting ofsoft boundariesthat separate an-
alytic and indexing uses of LLMs from anthropomorphized
interfaces, andhard boundariesthat categorically separate
anthropomorphized interfaces from systems that substitute
for human participants in representational processes. We
make these proposals at a moment when synthetic agents
in representational contexts remain experimental, and the
boundaries are still tractable.
Related Works
Synthetic Agents as Research Participants
The use of synthetic agents as substitutes for human par-
ticipants raises a set of interrelated concerns. These include
positionality, validity, epistemic and ethical risks, and the
boundaries of knowledge production (Alvarado Garcia et al.
2025; Wang, Morgenstern, and Dickerson 2025; Nguyen
and Welch 2026; Agnew et al. 2026; Jowsey et al. 2025;
Maden 2026). Scholars have cautioned against using syn-
thetic agents as wholesale replacements for human partici-
pants (Arawjo 2026), and a recent ACM workshop (Agnew
et al. 2026) has begun to consolidate standards and docu-
mentation practices for LLM use as simulated research par-
ticipants (Su 2026; Kuric, Demcak, and Krajcovic 2026;
Kim, Yun, and Hyun 2026; Sampson, Lurie, and Metaxa
2026; Maden 2026; Yang 2026).
A recurring critique concerns how synthetic agents han-
dle social identity. To represent humans, LLMs would need
to capture the influence of positionality, including the rele-
vance of social identities like race and gender (Wang, Mor-
genstern, and Dickerson 2025). In practice, they fail, for ex-
ample, with misportrayal and category error (Wang, Mor-
genstern, and Dickerson 2025; Nguyen and Welch 2026),
group flattening, and identity essentialization (Su 2026).
Since these systems are trained on data dominated by ma-
jority populations, they gravitate toward median experiences
and reject tail cases, marginalizing the populations who al-
ready are disproportionately and negatively impacted by
technology (Su 2026; Smith et al. 2025), and producing cul-
tural scarcity (Alvarado Garcia et al. 2025). Models reduce
complex demographic dynamics, such as systemic inequal-
ity produced through discriminatory policies, historical ne-
glect, or economic exclusion, to mere demographic proxies
(Maden 2026). Simulation results can appear believable on
the surface while the underlying logic, that of treating iden-
tity as a collection of inherent traits, is inaccurate (Maden
2026; Su 2026).
A second strand of critique concerns embodiment. Syn-
thetic agents lack the embodied lived experiences that hu-
man participants bring to research (Agnew et al. 2026),
and in spatial usability evaluation they perform poorly on
embodied experience criteria (Kim, Yun, and Hyun 2026).
Their implementations often treat surface-level markers of
human realism as evidence of behavioral or experiential va-
lidity (Su 2026).
Problems in evaluation follow naturally from these con-
cerns. Human participation evaluation centers on identity
verification grounded in lived experience. LLMs have no
lived experience to verify, and the task shifts from verifica-
tion to characterization, such as ‘does this simulated entity
faithfully reflect properties of the population the researcher
intends to study?’ With human participants, data quality
is assessed through depth, richness, and experiential speci-
ficity, none of which can be automatically measured (Maden
2026). In this space, scholars have proposed alternative
evaluation frameworks:believability, defined through met-
rics of consistency with human-like output and robustness
under disturbance (Xiao et al. 2024);faithfulness(Maden
2026; Agarwal, Tanneru, and Lakkaraju 2024);plausibil-
ity(Agarwal, Tanneru, and Lakkaraju 2024); andalgorith-
mic fidelity(Argyle et al. 2023). However, these frameworks
are all output-centric. They do not examine the processes
that lead to those outputs. Beyond evaluation, prior work
identifies ethical concerns around retrospective consent and
the moral alignment of models (Agnew et al. 2026), and
epistemic risks including category error, misattribution, the
oracle effect, and anthropomorphic fallacies (Nguyen and
Welch 2026; Stark 2024; Maeda and Stark 2025; Maeda and
Quan-Haase 2024). While some work examine legal impli-
cations of agents in e-commerce (Riedl and Desai 2025), and
socio-political implications of “agency-washing” (Timaite
and Castelle 2025), empirical studies of application of syn-
thetic agents as participants in representational processes re-
main underexplored, and importantly, the high stakes of pol-

icy, juries, and diplomacy make this gap consequential.
Personhood and Legitimacy
The English word “person” is derived from the Latin word
persona which refers to the mask worn by an actor portray-
ing a character within the context of a play (Gunkel and
Wales 2021). There is no fixed concept of personhood; it
is made and remade whenever societies need vocabulary for
new circumstances (Leibo et al. 2025).
Legal literature distinguishes natural and legal persons.
A natural person has intrinsic qualities like consciousness
(Leibo et al. 2025) and is natural by virtue of being born.
This personhood follows from birth, not from legal decree.
Corporations and environmental entities are legal persons by
decree, artificial and non-natural (Gunkel and Wales 2021;
Leibo et al. 2025; Baeyaert 2025). Legal personhood rests
on recognition as a subject of law, possessing both rights and
responsibilities (Gunkel and Wales 2021), and is historically
a pragmatic instrument of governance rather than a recog-
nition of moral worth. Its extension to non-human entities
is justified on three grounds (Baeyaert 2025): arights-based
model grounded in moral subjectivity (self-awareness, sen-
tience, the capacity to experience harm, the ability to par-
ticipate in reciprocal moral relations); afunctionalmodel
where legal status is extended as a juridical tool for coher-
ence, welfare, or governance efficacy; and anagency-based
model grounded in intentionality, goal formation, and bear-
ing responsibility for the consequences of action.
Across all three grounds, AI fits poorly. Even artificial en-
tities like corporations are embedded in networks of human
control, whereas AI systems can produce outcomes unfore-
seen by their developers (Mayne et al. 2025). Moral action,
in particular, requires consciousness, intentionality, and the
capacity to experience and take responsibility for the conse-
quences. Attempts to evaluate LLMs in domains requiring
moral reasoning have found their moral judgment shallow
and misaligned with human reasoning (Jiang et al. 2022;
Chakraborty, Wang, and Jurgens 2025). Prior work argues
that the question of whether AI can be made more ethical
is categorically misplaced since the inability of AI to be
a moral actor is a philosophical limit and cannot be over-
come by technical fixes (Bronner-Martin 2025). The capac-
ity for reciprocal moral relations follows Strawson’s account
of the reactive attitudes that constitute a moral community
(Strawson 1962). Synthetic agents can be objects of such
attitudes but never subjects of them. Moreover, the techni-
cal conceptions of agents do not map to socio-legal con-
ceptions of agency (Riedl and Desai 2025). Conceptions
from sociology and linguistic anthropology identify agency
as ontologically relational, and inseparable from social ac-
countability (Timaite and Castelle 2025). A ‘moral actor’ in
AI ethics is defined as a person who has a ‘will to action’
(Laflamme, College, and Bruneault 2023), and a legitimate
actor is one whose agency, intentionality, and capacity for
reciprocal moral relationships make them bound by moral
responsibility and its consequences (Baeyaert 2025). Syn-
thetic agents do not meet this bar.
Personhood in Participatory Design
Representation of personhood is the central problem in par-
ticipatory design (PD). Sanders et al.’s (Sanders, Brandt, and
Binder 2010) framework categorizes the purpose of design
engagement into four categories: probing, priming (immer-
sion in the domain of interest), understanding (of current
experience) and generating (creating and exploring future
scenarios). Each mode aligns with other aspects of partic-
ipation, including form (making/telling/enacting) and con-
text (stakeholder relationships, online or in-person modali-
ties, venue, group size, and composition) (Sanders, Brandt,
and Binder 2010). Crucially, participatory modes of engage-
ment produce aparticipantfrom a person. The participant is
constituted in the process of participation, but never repre-
sents the person as a whole. The production of a participant
is mediated through the modes of engagement, each in dif-
ferent capacities.
Probing: The foundational work, ‘Cultural Probes’
(Gaver, Dunne, and Pacenti 1999) introduced probing as a
participatory mode. Probing explores ‘functions’, ‘experi-
ences’, and ‘cultural placement’ outside the norm to dis-
cover new pleasures, forms of sociability, and cultural forms
(Gaver, Dunne, and Pacenti 1999; Burrows, Mitchell, and
Nicolle 2015; Madden et al. 2014). It uses provocations
directed towards ‘inspirational data’ rather than ‘informa-
tion’ with the purpose of stimulating imagination and asks
the question ‘What inspires a person’s experience of a phe-
nomenon of interest?’ (e.g., ‘What inspires fear of vaccines
in a population?’), effectively producing thea prioriof a
participant in research.
Priming: Priming is commonly used in behavioral psy-
chology to investigate human judgments and decision-
making. It affects perceptions and behaviors by increasing
cognitive accessibility of specific mental content. In the con-
text of design, priming is achieved by using stimuli, such
as drawings, videos, neutral or hostile sentences (She et al.
2018). Building on memory recall in psychological sciences
(Redelmeier, Katz, and Kahneman 2003), priming seeks to
produce an alterity in a participant’s experience and sense-
making by introducing a shift in the process of recall. Prim-
ing is premised on the idea that a participant’s memory is
not an exact replay of the complete experience but a recall
of selected moments. HCI has adapted priming to support
idea generation in designing creativity support tools (Lewis,
Dontcheva, and Gerber 2011).
Understanding: Understanding is a precursor to genera-
tive engagement. Orr (Orr 1996) looks at technical training
of technicians and their diagnosis of machine breakdown.
Diagnosing the breakdown requires narrative construction
and negotiation between fragments of information from the
customer and the condition of the machine. Suchman (Such-
man 1987) problematizes the notion embedded in the ‘expert
help system’ for machine use, which embodies a conception
of human action shared by designers, behavioral sciences,
and common sense that what people say or do is best under-
stood as the reflection of underlying plans. Suchman shows
that this confusesplanswithsituated action. Plans are not
rigid scripts dictating every move; they are vague guides
used to explain action while navigating unpredictable situ-

ations, designed to accommodate the unforeseeable contin-
gencies of actual situations of action. Understanding, then,
engages a person to produce a participant who is in the pro-
cess of sensemaking.
Generating: In early PD works, generating developed as
a mode of engagement in the UTOPIA project (Bødker et al.
1987). It presents a ‘tool perspective’ where a computing
system is designed as a collection of tools for skilled work-
ers to use by building upon their tacit skills as a basis for
analysis and design. In order to develop their technical imag-
ination the users have to gain insight into technical possibil-
ities as well. Thus, generating engages a person to produce a
participant who becomes familiar with technical affordances
in the design process.
The modes of engagement in PD produce a participant
from a person in different aspects of processes. PD produces
ana priorito the participant (probing); a participant in the
process of memory recall (priming); a participant in the pro-
cess of sensemaking (understanding); and a participant who
is familiar with technical affordances (generating). There are
degreesof participation and representation afforded by the
different modes of engagement but never representation of
personhood as a whole.
Methodology
This research is a comparative case study of three synthetic
agents deployed in representational processes. The three
cases were selected to provide variation along two dimen-
sions. First, is the scope of representation where the cases
span local (Ana, a community-voice chatbot in Pittsburgh),
enterprise (Synthetic Juror, a legal trial-preparation tool),
and global scales (Ask Amina and Ask Abdalla, two AI
avatars developed by the United Nations University Centre
for Policy Research). Second, populations represented span
community members in local policy consultation, jurors in
legal deliberation, and refugees and combatant leaders in
humanitarian diplomacy. We restricted ourselves to cases
with publicly accessible documentation sufficient for close
reading. The three cases also vary in technical architecture
(Retrieval Augmented Generation (RAG)-based personas in
Ana and Amina/Abdalla; a hybrid neuro-symbolic system
in Synthetic Juror) and in interface (chatbot, AI avatar, and
Slack integration), but variation along these dimensions was
not a selection criterion.
Despite the range in scope, relative to other technological
systems and infrastructures, synthetic agents in representa-
tional processes are an emerging domain, and the cases we
examine are pilots, enterprise trials, and prototypes rather
than mature deployments. We see this as the tractable mo-
ment for articulating boundaries, before institutional inertia
and sunk investments make them harder to draw.
Analytical Approach
The analysis proceeded through close reading of the publicly
available documentation for each case. This included project
reports, blog posts, marketing materials, founder writings,
and secondary coverage where available. For Ask Amina
and Ask Abdalla, our primary source was the UNU-CPR
working paper (Albrecht 2025), supplemented by investiga-
tive journalism (Gault 2025). For Ana, we drew on the New
Sun Rising organizational materials and the Community
V oice project documentation (Horn 2025; Rising 2025). For
Synthetic Juror, we drew on the company’s published blog
posts and product documentation (Abbey 2024a,b; Hooger-
huis 2024; Juror 2025).
Rather than conducting a formal thematic analysis, we
worked through iterative paired discussion. The first and sec-
ond authors collected and read the documentation, and de-
veloped initial codes for each case. The four authors then
discussed the cases in pairs, comparing codes across cases
and refining them through successive rounds. We iterated
until our codes were stable across cases, focusing on how
each synthetic agent framed its problem context, curated
its data, designed its user encounters, and evaluated its out-
puts. These four dimensions emerged as analytically useful
through the iterative comparison and now structure the Find-
ings section.
While discussing the codes, the limited focus on pro-
cesses prompted our examination and subsequent applica-
tion of PD. In particular, Sanders, Brandt, and Binder (2010)
helped us gain a process-oriented vocabulary to set against
the outcome-centric evaluations that dominate the existing
literature.
Positionality
We are four researchers based in Global North, three of
us originally come from the Global South. The first and
second authors are graduate students working at the inter-
section of Science and Technology Studies and Human-
Computer Interaction (HCI). The third author is a faculty
member with expertise in information science, technology
ethics and law who leads action-oriented research projects.
The fourth author is a faculty member in HCI who has con-
ducted community-based participatory research over the last
decade in both the Global South and the Global North.
Our shared concern in pursuing this work is the over-
reach of technology into representational contexts, partic-
ularly where the populations being represented are already
structurally marginalized. We are aware of the tension that
we critique tools that are framed as offering support to pop-
ulations with limited resources, often from our location in
well-resourced Global North institutions. We hold onto this
tension. Our critique is not that synthetic agents serve these
populations poorly (indeed they may speak for these com-
munities well), but that the legitimacy and value of any ap-
proach comes from people having the agency and power to
speak and act for themselves (i.e., representation). We have
tried to maintain this distinction throughout the analysis.
We also acknowledge that our materials are drawn pre-
dominantly from documentation published by the organiza-
tions themselves. Much of this material is targeted at poten-
tial clients or funders, and some claims may be more aspi-
rational. We treat the documentation as evidence of how the
systems are envisioned and justified.

Case studies
The three synthetic agents selected for this research are sit-
uated in the context of policy, diplomacy, and legal jury.
Collectively, they constitute synthetic agents in political
and representational contexts at three different scales: local
(Ana), enterprise (Synthetic Juror), and global (Ask Abdal-
la/Ask Amina).
Ask Abdalla/Ask Amina
Ask Amina and Ask Abdalla are two AI avatars that were
created as an experimental tool by the United Nations Uni-
versity Centre for Policy Research (UNU-CPR) for explor-
ing use of AI in Conflict Prevention. Both are RAG-based
implementations with curated knowledge bases targeted at
specific populations, presented through voice-conversational
avatars. Amina is positioned as a digital representation of a
refugee living in a camp in Chad, and Abdalla as a digital
replica of a combatant leader in the Rapid Support Forces
(RSF), a group active in the southeastern part of Sudan from
which many refugees are fleeing.
The use-case of these avatars is justified by citing the dif-
ficulties in recruiting participants for diplomatic consulta-
tion and deliberation. The documentation argues that cur-
rent methods, including surveys, focus groups, and ques-
tionnaires, are time- and resource-intensive, and that partic-
ipation can be limited by time constraints, geographical re-
moteness, or unwillingness to participate. It also notes that
respondents may have “an incentive to provide false or in-
complete information when replying, especially if respon-
dents believe that a certain type of answer may benefit them
in some way” (Albrecht 2025, p. 4).
The stated goals for the two are operational, which the
document states as“if Amina works, ’her’ rapid responses
could be of great value. For example, they could be used
to quickly make a case to donors (often in very differ-
ent locations and with very little time) on what popula-
tion needs to be prioritized when earmarking aid to the re-
gion. If Abdalla works, ’his’ responses could help negotia-
tors and mediators prepare for more targeted real-world en-
gagement“(Albrecht 2025, p. 8).
Figure 1: Screenshot of the AI avatar Amina (Gault 2025).
The development team also expresses an intention to ex-
tend the synthetic agents to group deliberation, integrat-
ing AI agent-generated personas of stakeholders, including
community leaders, government officials, and military lead-
ers, into diplomatic negotiation and mediation simulations
Figure 2: Screenshot of the AI chatbot Ana (New Sun Rising
Pittsburgh 2025).
(Albrecht 2025, pp. 4). The two avatars were briefly online
for public use but are no longer accessible.
Ana (New Sun Rising)
Ana is a chatbot created by New Sun Rising, a Pittsburgh
(Pennsylvania, USA)-based organization, as part of their vir-
tual support center. Like Amina and Abdalla, Ana is a RAG-
based implementation, but rather than mimicking a regional
demographic persona, it surfaces quoted excerpts and syn-
thesized insights from a community dataset. The underly-
ing dataset is the organization’s Community V oice project,
which gathers feedback and testimonials from community
leaders and members on the present strengths and challenges
of their community, as well as their hopes, fears, and expec-
tations for the future (Rising 2025).
The organization coded the dataset using its Impact
Framework (mapped to the UN Sustainable Development
Goals), a Resource Framework (Community Capitals), and
sentiment analysis (Rising 2025). Ana“...specializes in data
analysis and communication, assisting users in exploring the
Community Voice qualitative data-set to enhance grant pro-
posals, communications, and advocacy campaigns“(Horn
2025). Ana 1 is targeted towards non-profits and local policy
makers who require inputs from community members in or-
der to make better informed decisions. It acts as an interface
for exploring and discovering existing data relevant to the
query.
Synthetic Juror
Synthetic Juror is a legal technology platform that utilizes a
hybrid neuro-symbolic architecture to simulate juror behav-
ior, reasoning, and decision-making. The LLM layer handles
the “human” elements of communication, processing case
files and evidence to understand natural language, and pat-
terns in emotional nuances (Juror 2025).
The system aims to extract deep patterns from the psy-
chographic and demographic data provided by its integrated
workbench, ‘Lairm’, to create synthetic juror profiles. Legal
teams can use these to replace traditional mock trials with
simulations that include geo-specific modeling, adjusting to
1Accessible at: https://vibrancy.newsunrising.org/

regional attitudes, and narrative testing to identify resonat-
ing emotional appeals. The company emphasizes the geo-
specific dimension as a distinguishing feature, claiming that
the platform “understands the cultural, demographic, and re-
gional nuances that shape juror perspectives” and lets attor-
neys tailor strategies to address biases and emotional triggers
specific to the jurisdiction (Juror 2025).
The platform supports running thousands of simulations
and is integrated into the Slack interface of the enterprise
client, where synthetic agents interact as individual personas
across Slack channels. Synthetic Juror is an enterprise soft-
ware available for trial upon request sent to the company.
Findings
Across the three cases we trace a four-step process (framing
the problem, curating data, designing the encounter, evaluat-
ing validity) through which synthetic agents become a rep-
resentational entity.
Manufacturing the Problem for Synthetic Agents
Establishing the need for a synthetic agent product is the first
stage that enables conceptualization of a field of intervention
in the representational process. While synthetic agents are
generally proposed as a solution to the difficulty in recruit-
ing participants for consultation, each of them speaks to a
different problem.
For Ask Amina and Ask Abdalla, the stated objective is
to enable humanitarian and relief workers to ask questions
about refugee experiences, needs, and sentiments, and to re-
ceive responses that closely mirror real refugee perspectives
(Albrecht 2025, p. 3). Amina is positioned to enhance the
feasibility of needs assessments for UN staff in determining
the type of intervention (Albrecht 2025), placing the syn-
thetic agent in a role that makes allocative choices about
whose interests come first. Ask Abdalla, on the other hand,
is designed to let diplomats, negotiators, and mediators prac-
tice their skills with a persona that responds in ways con-
sistent with a real combatant’s known behavioural patterns
(Albrecht 2025, p. 3).
Collectively, probing and understanding the field is ac-
knowledged as central to the domain enquiry of diplomacy.
However, the complexities of probing are reduced to a feasi-
bility concern in synthetic agents. The framing focuses on
manufacturing a “person-who-probes” instead of the pro-
cess of probing. These two AI avatars are, in fact, proposed
as “Anthropologist Agents” that can“act as ‘investigators’
dedicated to studying a person and their context ... they must
become similar to anthropologists”(Albrecht 2025, pp. 6).
They further list four skill sets for these agents, covering lit-
erature review, fieldwork, culturally responsive analysis, and
continuous knowledge base updates (Albrecht 2025, p. 6).
This frames the synthetic agent as an expert on the lived ex-
periences of the community whom it claims to represent, and
importantly, generates a tension between the two incompat-
ible positionalities, as an embodied refugee or combatant on
the one hand, and the external observer and investigator on
the other.
Ask Amina/Abdalla seeks to configure a mechanized
probe tool which can be attributed the legitimacy of an an-
thropologist expert. In contrast, Ana draws out synthesized
insights and quoted interview excerpts from the Commu-
nity V oice dataset (Horn 2025). In doing so, it makes moral
choices on behalf of its users by prioritizing some voices
over others on grounds of relevance, even as it does not claim
to embody a persona.
Synthetic Juror intervenes in legal trial preparation for
lawyers as an enterprise solution addressing the feasibility
challenges of conducting a mock trial. The company frames
traditional trial preparation as relying on mock trials, fo-
cus groups, and intuition, and positions itself as bringing
“a new level of precision by simulating thousands of jurors’
reactions using AI. ”(Abbey 2024a). The system claims to
model“how real jurors think, incorporating their biases,
emotional triggers, and regional quirks ... These aren’t just
static profiles. They’re active participants ...You can present
any evidence to them (depositions, expert witness, poten-
tial outcomes, interrogatories, motions, arguments and the
list goes on) ... they respond ... with nuanced feedback that
mimics how real jurors think“(Abbey 2024a). The appeal
to legitimacy is the ability to narrativize and imitate the case
context like a person sitting in the jury. This claim invites in-
terrogation: can synthetic jurors be probed for bias and im-
partiality, which is the established procedure ofvoir direin
legal jury deliberations?
Across the cases, synthetic agents address an identified
feasibility gap by targeting needs like quick surveys, data-
driven insights, and variety of mock-simulation of personas.
While the promise of quick, real-time qualitative insights are
the core offering, it could have been delivered as reports or
dashboards. The personas appear as a separate layer that an-
thropomorphizes the interaction through narrativization.
Manufacturing Persona through Data Access
The synthetic agents across representational contexts use
qualitative datasets, surveys, and reports in their RAG im-
plementation. For Amina and Abdalla, the knowledge base
contains surveys, reports, articles, and issue briefs from UN
agencies, multilateral organizations, think tanks, and NGOs
working with refugees and combatants in Chad and Sudan
(Albrecht 2025, p. 8). A separate persona-curation dataset
draws from cultural artifacts of the community being mim-
icked, including“... seminal works of literature, folkloric
traditions and key religious texts, but also items from the cul-
ture’s contemporary digital footprint, including local news
media, social media activity and online diaspora community
discussion forums. ”(Albrecht 2025, p. 8). The voice-avatar
also attempts to mimic the tone and filler-sounds between
sentence pauses. An investigative article found that the con-
temporary digital footprint likely included voice and video
recordings of community members (Gault 2025).
Persona curation is also central to Synthetic Juror, given
its intention to simulate a diverse mix of jury positionalities.
As the document states, it“uses advanced patent-pending
technology to simulate juror responses based on a broad
range of data”(Hoogerhuis 2024). Another document indi-
cates“the synthetic character samples are built using a com-
bination of public data, subscription databases, your firm’s

proprietary information, and client-specific data, ensuring a
high degree of realism and relevance”(Abbey 2024b).
Both Amina/Abdalla and Synthetic Juror manufacture
personas through a specifically curated dataset that is sep-
arate from their knowledge base. Ana, in contrast, draws its
data from the Community V oice project curated by the same
organization to“gather feedback and testimonials both digi-
tally and in person”, in which people were“invited to share
their perspectives on the present strengths and challenges of
their community, as well as their hopes, fears, and expecta-
tions for the future”(Rising 2025). The community data was
coded by the organization before using it to train the chatbot
model (Rising 2025). Unlike Amina/Abdalla and Synthetic
Juror, the chatbot Ana does not appear to mimic a region-
specific demographic persona.
This data work bypasses the participatory mode of un-
derstanding, where sensemaking is constructed through nar-
rative negotiation between participant, researcher, and con-
text (Suchman 1987; Orr 1996). Synthetic agents collapse
sensemaking into static dataset curation. Datasets drawn
from institutional sources reflect the plans and blueprints
of the institutions that collected them, leading to an over-
representation of institutionally prioritized data. Paradoxi-
cally, the embedded presence of institutional blueprint sab-
otages the very grounds that necessitate ethnographic in-
quiry for understanding to complement and evaluate the in-
stitutional paradigms. There is also a clear demarcation be-
tween the datasets that generate insights, and the datasets
for persona-curation which focuses on drawing positionality
from demographic data and the ability to mimic personhood
in the context of the prompt.
Manufacturing Encounters for User Interaction
The three cases offer widely varying affordances to target
users. The documentation on Amina and Abdalla justifies
the AI avatar persona by contrasting it with NLP-based
sentiment analysis, where NLP can only examine existing
opinions, personas can engage in dialogue about hypotheti-
cal scenarios“offering predictive insights into how people
might respond to future activities and actions”(Albrecht
2025, p. 4). This establishes a clear distinction between anal-
ysis of existing data and predicted or hypothetical data, and
importantly, it positions synthetic agents as interaction sur-
faces for predicted scenarios. While probing and priming
could potentially reveal asymmetric power relations, such
modes of inquiry are no longer viable for hypothetical and
predicted scenarios. Priming is thereby bypassed since there
is no recall of lived experience to shift.
Synthetic Juror extends this affordance to legal practition-
ers through integration with Slack.”All of this happens right
in Slack. Lawyers can @mention a simulated juror just like
they would a colleague. They can create sub-channels for
different aspects of the case... use Slack’s huddle feature to
do mock cross-examinations with AI witnesses... ”(Abbey
2024a). It further claims that the“Lairm Workbench in-
cludes a sophisticated character creation tool that allows
you to build incredibly detailed synthetic individuals for
your case simulations”(Abbey 2024b).
This affordance directly bypasses priming as it operates in
actual jury deliberation. Priming in juries takes the form of
implicit bias instructions designed to make jurors reflect on
their own biases, and theSommers effect(Sommers 2006)
shows that racial diversity among jurors primes individu-
als to exchange a wider range of information. By offering
the ability to calibrate specific demographic positionalities
at will, Synthetic Juror removes the moment of reflexivity
that is integral to priming and replaces it with essentialized
and flattened identities.
Ana’s interaction is a chat interface. That leaves a wide-
open possibility for interaction and risks confusing users.
The organization recognized this risk and in response,
they delivered an information session that included sample
prompt templates (New Sun Rising Pittsburgh 2025). A rep-
resentative template asks Ana to identify the primary themes
in the Community V oice data relevant to a specified organi-
zation, issue, and audience, and to draft a 500-word sum-
mary including quotes from community members (New Sun
Rising Pittsburgh 2025). Since templates scaffold the user
toward indexing and summarization instead of encounter
with a person, there is no moment of recall to prime.
We see these design affordances as different approaches
of engaging the user in speculative inquiry and visualization.
The synthetic agents either lead the user into visualizing an
actual embodied individual (e.g., a refugee from Chad), the
opinions of an individual (e.g., Slack messages of a jury
member), or the reported insight of an individual (e.g., an
insight reported by Ana). In all cases, the synthetic agents
give an impression of personhood while mechanically draw-
ing data and inferences from their existing knowledge base.
Manufacturing Validity with Technical Measures
We note that the validity of the synthetic agents is justified
by manufacturing the problem context. However, a parallel
move occurs at the level of outcome evaluation.
Synthetic Juror claims“99% accuracy rate in predict-
ing case outcomes. That’s not just a marketing claim. It’s
based on comparing the system’s predictions to actual trial
results”(Abbey 2024a). The documentation on Amina de-
scribes a study where Amina was fed 20 questions drawn
from four surveys not included in her knowledge base, with
the delta between her responses and the actual human re-
sponses measured as the indicator of accuracy;“she cor-
rectly answered 16 out of 20 questions, achieving an 80
per cent accuracy rate” (Albrecht 2025, p. 7). In contrast,
“Abdalla’s responses, [were] qualitatively assessed. A brief
conversation between the two [will] also be qualitatively as-
sessed” (Albrecht 2025, p. 7).
The available documentation does not describe any eval-
uation method for Ana. They measure the similarity of syn-
thetic outputs to human outputs (a delta, a percentage ac-
curacy, a qualitative comparison) and treat that similarity
as the warrant for representational validity. This evaluation
logic bypasses the participatory mode of generating, where
the process of setting up a deliberative mechanism is as in-
tegral to legitimacy as the artifact it produces. PD tools for
generating design through group deliberation reveal that out-
comes are not automatic products but are closely tied to the
underlying process (Simonsen, Karasti, and Hertzum 2020).

Outcome-centric evaluation makes the process invisible, and
importantly it makes the process un-evaluable.
Discussion
The synthetic agents in our three cases are early-stage and
experimental, and they reflect the broader nature of repre-
sentational synthetic agents as an emerging domain. This is
the moment when boundaries are most tractable, before in-
stitutional inertia and sunk investments make them harder to
articulate. In this section, we make explicit what is at stake
in the four-step manufacture we traced in Findings, and ar-
ticulate what synthetic agents categorically cannot do.
Bypassing Representational Process
As the Findings showed, the need for synthetic agents is
manufactured by emphasizing the difficulty of recruiting
participants as the central bottleneck of representational pro-
cesses, for which a sophisticated mechanical process is of-
fered as the solution. This amounts to a “machinal bypass”
(Kaplan, Palitsky, and Raison 2025) of a multidimensional
process where representation is integral to any claims of le-
gitimacy for an institution.
The central function of representation in participatory
processes is the fidelity to the participant population (Prem-
ananda 2026). From this view, the limited access to partici-
pants is not a mere problem to solve with a single solution. It
is a symptom of deeper structural failures of representation,
and PD scholarship has long questioned whether slow pro-
totyping or feasibility are bottlenecks at all (Elavsky 2026).
Existing evaluation frameworks for synthetic agents (be-
lievability(Xiao et al. 2024),plausibility(Agarwal, Tanneru,
and Lakkaraju 2024),faithfulness(Maden 2026),algorith-
mic fidelity(Argyle et al. 2023)) all measure similarity be-
tween human and synthetic responses, treating outcome re-
semblance as the warrant for representational validity. The
table in Fig. 3 contrasts this with PD modes of engagement
applied to the same three domains. PD treats representation
as a process whereas synthetic agents reduce it to an out-
come. Let us consider the strongest version of the case these
frameworks make, a synthetic agent whose responses are
statistically indistinguishable from those of the population it
stands in for. Even at this limit of perfect fidelity, the agent
delivers the resemblance of participation and not participa-
tion itself, and, as established above, it is the participation
that legitimacy requires. The bypass thus becomes structural
since existing outcome-centric evaluation makes emphasis
and orientation on the processes impossible.
Reckoning Replaces JudgmentThe distinction between
reckoningandjudgmentclarifies why this bypass is conse-
quential (Weizenbaum 1976; Smith 2019). Reckoning is es-
timation or calculation that can be sophisticated but oper-
ates within a well-defined space governed by simple logi-
cal rules. For instance, a game of chess is reckoning. Judg-
ment is a different form of intelligence requiring dispassion-
ate and deliberate thought guided by ethical commitments
and awareness of consequences, producing actions appro-
priate to an undefined situation (Weizenbaum 1976). In our
case studies, jury deliberation is paradigmatically a process
of judgment. The jury constructs a story from evidence to ar-
rive at a verdict, and importantly, the evidence interpretation
cannot be reduced to the verdict itself.
LLMs are reckoning machines due to their epistemic
method of reproducing the cosine distances present in their
vector-embeddings in the high-dimensional space. These
vector-embeddings are abstracted from the past training data
and hence are constrained by them. Related literature on
simulation of judgment in LLMs argues that the very no-
tion of judgment is operationalized when decisions are made
by LLMs, where similarity of outputs ‘appear as alignment‘
but may conceal deeper epistemic shift where normative rea-
soning is replaced by statistical approximation. The authors
ask what heuristics are encoded in this process of delega-
tion (Loru et al. 2025)? Such a system cannot orient itself
towards the concerns of the future or the consequences of
its actions. As we saw in the Findings section, synthetic
agents mimic human personhood by imitating human re-
sponses and even have a separate dataset curated just for
the purpose of imitation. The deliberate use of anthropomor-
phic terminology, such as ‘reasoning’, ‘thinking’, ‘halluci-
nations’, indicate an attempt to conflate the human and ma-
chine processes. Importantly, it stretches the logic of context
representation to claim that reckoning machines are capable
of judgment.
This has deep consequences beyond poorly made moral
choice. Allocative choices, such as whose needs to prioritize
when earmarking aid (Amina/Abdalla), and choices about
which voices to prioritize (Ana), are political judgments. In
fact, when they are represented as output of a calculation en-
gine, they are often removed from the domain of contestable
political judgment and relabeled as technical fact. It laun-
ders judgment, conferring on the synthetic agent the func-
tional status of a moral actor while remaining categorically
incapable of intentionality or of entering into reciprocal rela-
tions as a subject of rights and duties. This relocation of po-
litical choice into the seemingly neutral output of a machine
is what later allows those in authority to defer accountability
for it, a deferral we take up in the next section. Substituting
a synthetic agent for a human participant is, in the end, the
application of a reckoning mechanism in a context that cat-
egorically requires judgment.
Reflexivity Cannot Be MechanizedA related bypass oc-
curs at the level of reflexivity. Synthetic agents often draw
their imitation data from “seed-interviews” (Narasimhan
2026, p. 6) which collect opinions and associate them with
their demographic data. In our case studies, Ana draws
on the Community V oice project, and Amina/Abdalla draw
on social media data and surveys. Beyond identity flatten-
ing and essentialization (Su 2026; Wang, Morgenstern, and
Dickerson 2025), this epistemic method amounts to a claim
of mechanically reproducing reflexivity.
Participation in representational processes requires reflex-
ivity. When a citizen responds to a policy consultation or a
juror weighs evidence, they reflect on their positionality (as
a citizen, as a juror) before generating a response. This re-
sponse is shaped in the act of reflection. Synthetic agents
bypass this moment and replace it with a probabilistic algo-

PERSONHOOD SYNTHETIC
AGENTS
PROBING PRIMING UNDERSTANDING GENERATING
POLICY
Deliberative inquiry,
and cultural probes
Awareness of nudging and choice architecture Citizen ethnography Generative co-design
and participatory
budgeting
Opinions of the agent closely
match the opinions of the
target population
DIPLOMACY
Probing the nature
of conflicts
Symbolic gestures in picking negotiation
venues
Ethnography and
field enquiry
Consulting affected
communities for
negotiation
The agent's knowledge of the
conflict situation and culture
matches the target population
JURY
DELIBERATION
“Voir Dire” - probing
for bias in the jury
“Implicit bias instructions”- make the jury
check their own bias; “Sommers effect” –
presence of other jury members primes
individuals to act in a certain way
“Evidence interpretation”-
building a story to make
sense of evidence
“Deliberation”-
construction of verdict
through arguments and
voting among the jury
Agents can enact responses
similar to those of target
jury demography
PROCESS ORIENTED OUTCOME CENTRIC
Figure 3: Synthetic agents seek to replace a complex representational process.
rithm of mechanical context estimation. The extreme case
in our findings was the proposedanthropologist agent(Al-
brecht 2025, p. 6), which conflates the positionality of the
embodied refugee or combatant with that of the external ob-
server studying them.
Synthetic Juror represents the inverse extreme. The plat-
form allows users to curate demographic identities for syn-
thetic jurors and claims the resulting agents respond as peo-
ple from those positionalities would. An individual is re-
duced to a tuple of social and systemic categories. The train-
ing data of foundational models and the RAG implemen-
tations built on them are constrained by the computational
requirement to converge on the most probable output, which
means generated responses identify with the median of the
training data and exclude marginalized voices that exist in
the tails (Su 2026). Essentialization is, thus, structurally pro-
duced by these epistemic methods.
Personhood is constituted relationally through political,
legal, and moral dimensions that together determine the rela-
tionships a person holds with other persons and institutions.
Participation, representation, and legitimacy are entangled in
this relational notion. But synthetic agent reproduces the ap-
pearance of participation while removing its substance, the
process, the judgment, and the reflexivity that make partic-
ipation legitimate. That is, it “manufactures personhood”.
When synthetic agents manufacture personhood, they re-
duce these relational dimensions to essentialized identities
and produce an appearance of legitimate participation with-
out the underlying process. Nobodyparticipates.
Boundaries for Design
The manufacture of personhood enables a further deferral.
When LLMs substitute for human participants, those in au-
thority can claim that representational choices were algorith-
mically determined by a calculation engine that cannot itself
be evaluated. This problem has been examined in the context
of e-commerce as the principal-agent-third-party problem of
trust and verification (Riedl and Desai 2025), but it has not
been conceptualized for representational decision-making.
Related work has named the broader pattern anaccount-
ability shield(Timaite and Castelle 2025) andalgorithmic
governmentality(Rouvroy and Berns 2013; Nayak 2021).
Representational contexts intensify the stakes because the
choices are political. Drawing boundaries becomes critical
to ensure we can center people’s power and agency in the
political processes.
Drawing on the manufactured personhood we traced
above, we propose two boundaries for researchers and de-
signers working with LLM-based systems in representa-
tional contexts. The first is “soft” and context-dependent.
The second is “hard” and categorical. We build this distinc-
tion because hedged versions of the second boundary erode
under pressure from precisely the actors most likely to scale
or transfer these systems beyond their experimental scope
(Larson et al. 2016).
The soft boundary separates LLMs functioning as ana-
lytic, indexing, or scaffolding tools from LLMs that present
themselves as person-like interlocutors. This boundary is
contextual. Anthropomorphization is sometimes useful. For
example, it can make complex data more navigable and thus
accessible (Tan et al. 2025). Other times, it is harmful when
it naturalizes claims a system cannot make (Lifshitz and
Hung 2024).
The hard boundary separates anthropomorphized inter-
faces, which are mere “evocative animations” (Stark 2024),
from systems that substitute for human participants in repre-
sentational processes. This boundary is categorical and ab-
solute in the sense that no degree of fidelity, believability, or
algorithmic sophistication moves a system across it.
We draw this categorical boundary based on the fact that
representational processes (e.g., policy consultation, jury de-
liberation, diplomatic negotiation) derive their legitimacy
not from arriving at the right outcome but from being consti-
tuted by the participation of persons. The participation is in
the service of legitimacy. For example, a jury verdict in the
US is legitimate because twelve persons from society delib-
erated and not because a tribunal predicted what they would
have said. Similarly, a policy consultation rests its legitimacy
on having citizens’ input.
On the Hardness of Hard BoundariesSynthetic agents
categorically lack the properties that participation requires,
which are consciousness, intentionality, embodied experi-
ence, the capacity to bear consequences, and the capacity
for reciprocal moral relations. These are conditions of per-

Manufactured
Personhood
Anthro-
pomorphization
Mechanical
Reckoning
Systems
Claim to personhood;
bypassing representational
processes integral to
institutional legitimacy
E
a
s
e

o
f

c
o
m
p
r
e
h
e
n
s
i
o
n

a
n
d

n
a
v
i
g
a
t
i
o
n
D
e
c
e
p
t
i
o
n

a
n
d

h
a
r
m
s
A
n
a
l
y
t
i
c
,

i
n
d
e
x
i
n
g
,

o
r

s
c
a
f
f
o
l
d
i
n
g

t
o
o
l
s
R
e
q
u
i
r
e
s

c
o
n
t
e
x
t

m
a
n
a
g
e
m
e
n
t
;

A
n
t
h
r
o
p
o
m
o
r
p
h
i
z
a
t
i
o
n

i
s

s
o
m
e
t
i
m
e
s

h
e
l
p
f
u
l

f
o
r

m
a
k
i
n
g

d
a
t
a

a
c
c
e
s
s
i
b
l
e
,

b
u
t

c
a
u
s
e
s

h
a
r
m
s

w
h
e
n

u
s
e
d

f
o
r

d
e
c
e
p
t
i
o
n
S
e
p
a
r
a
t
e
s

a
n
t
h
r
o
p
o
m
o
r
p
h
i
z
e
d

i
n
t
e
r
f
a
c
e
s

f
r
o
m

s
y
s
t
e
m
s

t
h
a
t

s
u
b
s
t
i
t
u
t
e

f
o
r

h
u
m
a
n

p
a
r
t
i
c
i
p
a
n
t
s

i
n

r
e
p
r
e
s
e
n
t
a
t
i
o
n
a
l

p
r
o
c
e
s
s
e
s
Anthropomorphized
Interfaces
Claim of Legitimacy
Hard Boundaries
Soft Boundaries
Figure 4: Soft boundaries and hard boundaries to develop oversight for synthetic agents.
sonhood that constitute representational processes.
We understand that this may rule out reasonable middle-
ground positions that are argued in the literature and popular
media.Community-consented synthetic representationas-
sumes a community can authorize a synthetic agent to be its
representation in deliberative settings. However, participa-
tion is non-transferable. No one can consent on another’s be-
half to having that other’s participation substituted, because
the participation is the thing legitimacy requires (Agnew
et al. 2026).Augmentation-as-supplementassumes a syn-
thetic agent can speak alongside human participants with-
out displacing them. But the synthetic voice in a representa-
tional process is doing representational work, howsoever it
may be framed.Training simulations for real deploymentas-
sume practice on a simulation transfers to competence in the
real thing. But what is practiced is engagement with a text-
prediction system, and importantly, not engagement with a
refugee, a juror, or a combatant leader and all the contingen-
cies and uncertainties that are at play in those contexts.
From our perspective, the single remaining use case is
education or training that is explicitly scaffolded as non-
transferable, where the discontinuity between the simulated
encounter and the real one can be a lesson. A diplomat-
in-training can encounter a system like Ask Abdalla pro-
vided the encounter is framed as engagement with a text-
prediction system, and importantly, not as preparation for
engaging with actual combatant leaders. A law student can
practice argumentation against a synthetic juror to improve
the students’ argument skills and not as a way to learn how
to engage with the judicial system. In these cases, a carefully
created scaffold to draw boundaries is necessary.
Soft Boundaries Require MaintenanceOf our three
cases, Ana sits closest to the soft boundary because it sur-
faces existing community voices through quoted excerpts.
However, the representational problem remains. The chat-
bot persona, by lending mediated authority to the indexed
material, performs legitimation work. This instability is in-
trinsic to soft boundaries. As community members continue
to engage with such a system, as organizational staff cite its
outputs in communications, and as it becomes the default
interface to the community dataset, the system accrues rep-
resentational status that was never formally claimed for it.
Indeed, the legal recognition of this drift has been estab-
lished. InMoffatt v. Air Canada, the British Columbia Civil
Resolution Tribunal held the airline responsible for its chat-
bot’s statements, rejecting the argument that the chatbot was
a separate legal entity from the company it served (Lifshitz
and Hung 2024). The tribunal recognized that the deploy-
ment of a chatbot in a customer-facing role makes the chat-
bot a functional representative.
Maintaining the soft boundary, therefore, requires active
design and governance work, and importantly, it is not a
property the system possesses on its own. Interfaces should
clarify and explicitly emphasize the system’s role in index-
ing data rather than being a voice. Outputs that quote or sum-
marize community data should route attribution back to the
community sources rather than aggregate into a single chat-
bot persona. Importantly, evaluation processes should test
for representational drift over time and, building on partici-
patory design tradition, ask process-oriented questions. This
includes asking questions likeWhose voices and processes
are informing the system?A system that is informed by the
researcher’s analytic process is differently situated than one
that purports to involve a community’s participatory process.
Does the system create or reduce opportunities for differ-
ent stakeholders to participate in their own terms?A sys-
tem that points researchers toward community voices they
had not heard expands participation.What would the repre-
sented community say about the system, in conditions where
their assessment carries weight?This shifts the evaluative
locus from the researcher’s judgment of fidelity to the com-
munity’s judgment of the system’s relation to them.
Limitations
To conclude, given the experimental nature of the cases
available for studying, we acknowledge that our case ma-
terials are drawn from the documentation published by the
organizations. Since a lot of this material is targeted towards
their potential clients, some of their claims may be more as-
pirational than material. The inability to interact with the
three AI agents directly is another limitation which could
have added more analytical depth to our analysis. Ana chat-
bot was available for interaction, but its terms of use limit us
from discussing the generated responses.

Acknowledgments
An earlier version of this work was presented at the sympo-
sium’Chat Token Vector: Questioning Models of Language
and Neo-Structuralism in AI’organized by the ERC project
AIMODELS at the Department of Philosophy and Cultural
Heritage of Ca’ Foscari University of Venice in partnership
with Cambridge Language Sciences and Cambridge Digi-
tal Humanities. We are thankful to the symposium for their
valuable feedback. We would like to express our gratitude
to Takuya Maeda for the productive discussions around this
paper. We would also like to thank the anonymous review-
ers and the meta-reviewer for their helpful comments which
helped in shaping this paper.
Declaration on Use of AI
We acknowledge the use of Claude (Anthropic) as a copy-
editing tool to improve spelling, grammar, punctuation, clar-
ity, and concision. Gemini (Google) was also used for web-
search.
References
Abbey, S. 2024a. Legal slack: Synthetic Juror.
Abbey, S. 2024b. SyntheticJuror™ and Lairm™ Work-
bench: Revolutionizing Trial Consulting: Synthetic Juror.
Agarwal, C.; Tanneru, S. H.; and Lakkaraju, H. 2024. Faith-
fulness vs. Plausibility: On the (Un)Reliability of Explana-
tions from Large Language Models. ArXiv:2402.04614 [cs].
Agnew, W.; Kapania, S.; Schroeder, H.; Aubin Le Qu ´er´e,
M.; Fox, S. E.; and Heidari, H. 2026. Workshop on Devel-
oping Standards and Documentation For LLM Use as Simu-
lated Research Participants. InProceedings of the Extended
Abstracts of the 2026 CHI Conference on Human Factors in
Computing Systems, 1–4. Barcelona , Spain: ACM. ISBN
979-8-4007-2281-3.
Albrecht, E. 2025. Does the United Nations need agents?
Testing the role of AI agent generated personas in humani-
tarian action.
Alvarado Garcia, A.; Shukla, N. A.; Azmat, M.; and Wong-
Villacres, M. 2025. Disciplinary Practices in the Generation
of Text Synthetic Data: A Critical Discourse Analysis.Pro-
ceedings of the AAAI/ACM Conference on AI, Ethics, and
Society, 8(1): 152–165.
Arawjo, I. 2026. That’s Enough About AI Replacing Users
in User Research. InProceedings of the Extended Abstracts
of the 2026 CHI Conference on Human Factors in Comput-
ing Systems. In Review.
Argyle, L. P.; Busby, E. C.; Fulda, N.; Gubler, J. R.; Ryt-
ting, C.; and Wingate, D. 2023. Out of One, Many: Using
Language Models to Simulate Human Samples.Political
Analysis, 31(3): 337–351.
Baeyaert, J. 2025. Beyond Personhood: The Evolution of
Legal Personhood and Its Implications for AI Recognition.
Technology and Regulation, 2025: 355–386.
Ball, S.; Allmendinger, S.; Kreuter, F.; and K ¨uhl, N. 2025.
Human Preferences in Large Language Model Latent Space:
A Technical Analysis on the Reliability of Synthetic Data in
V oting Outcome Prediction. ArXiv:2502.16280 [cs].
Bronner-Martin, G. 2025. Ethical AI as a Moral Agent is
Impossible: Why Algorithmic Fairness is an Illusion and We
Need Democratic AI Governance.
Burrows, A.; Mitchell, V .; and Nicolle, C. 2015. Cultural
probes and levels of creativity. InProceedings of the 17th
International Conference on Human-Computer Interaction
with Mobile Devices and Services Adjunct, MobileHCI ’15,
920–923. New York, NY , USA: Association for Computing
Machinery. ISBN 978-1-4503-3653-6.
Bødker, S.; Ehn, P.; Kammersgaard, J.; Kyng, M.; and Sund-
blad, Y . 1987. A UTOPIAN Experience: On Design of Pow-
erful Computer-Based Tools for Skilled Graphic Workers.
In Bjerknes, G.; Ehn, P.; and Kyng, M., eds.,Computers and
Democracy, 251–278. Avery. ISBN 0 566 05476 0.
Chakraborty, M.; Wang, L.; and Jurgens, D. 2025. Struc-
tured Moral Reasoning in Language Models: A Value-
Grounded Evaluation Framework. ArXiv:2506.14948
[cs.HC].
Elavsky, F. 2026. On genAI: Was prototyping really a bot-
tleneck?
Ersoz, A. B. 2026. 12 Angry AI Agents: Evaluating Multi-
Agent LLM Decision-Making Through Cinematic Jury De-
liberation. ArXiv:2605.01986 [cs].
Gault, M. 2025. The UN Made AI-Generated Refugees.
Gaver, B.; Dunne, T.; and Pacenti, E. 1999. Design: Cultural
probes.Interactions, 6(1): 21–29.
Gunkel, D. J.; and Wales, J. J. 2021. Debate: what is person-
hood in the age of AI?AI & SOCIETY, 36(2): 473–486.
Habermas, J. 1996.Between facts and norms: contributions
to a discourse theory of law and democracy. Studies in con-
temporary German social thought. Cambridge, Mass: MIT
Press, 1. mit press paperback ed., 3. print edition. ISBN
978-0-262-08243-3 978-0-262-58162-2.
Hoogerhuis, E. 2024. Beyond Mock Trials: How Syn-
theticJurors deliver Data-Driven Insights for Winning Legal
Cases: Synthetic Juror.
Horn, A. 2025. New Sun Rising launches Virtual Support
Center – New Sun Rising.
Jiang, L.; Hwang, J. D.; Bhagavatula, C.; Bras, R. L.; Liang,
J.; Dodge, J.; Sakaguchi, K.; Forbes, M.; Borchardt, J.;
Gabriel, S.; Tsvetkov, Y .; Etzioni, O.; Sap, M.; Rini, R.; and
Choi, Y . 2022. Can Machines Learn Morality? The Delphi
Experiment. ArXiv:2110.07574 [cs.CL].
Jowsey, T.; Braun, V .; Clarke, V .; Lupton, D.; and Fine, M.
2025. We Reject the Use of Generative Artificial Intelli-
gence for Reflexive Qualitative Research.Qualitative In-
quiry, 10778004251401851.
Juror, S. 2025. About- Synthetic Juror.
Kaplan, D. M.; Palitsky, R.; and Raison, C. L. 2025. The
“machinal bypass” and how we’re using AI to avoid our-
selves.Proceedings of the National Academy of Sciences,
122(51): e2518999122.
Kim, D.; Yun, Y .; and Hyun, K. H. 2026. Layer-Specific
LLM Participation in Spatial Usability Evaluation. InPro-
ceedings of the Extended Abstracts of the 2026 CHI Confer-
ence on Human Factors in Computing Systems.

Kuric, E.; Demcak, P.; and Krajcovic, M. 2026. Synthetic
Participants Generated by Large Language Models: A Sys-
tematic Literature Review. InProceedings of the Extended
Abstracts of the 2026 CHI Conference on Human Factors in
Computing Systems. In Review.
Laflamme, A. S.; College, A.-L.; and Bruneault, F. 2023. In-
cluding a Social Perspective In AI Ethics: The Contribution
of a Dialogue Between American Pragmatism and Critical
Theory.
Larson, J.; Mattu, S.; Kirchner, L.; and Angwin, J. 2016.
How We Analyzed the COMPAS Recidivism Algorithm.
Leibo, J. Z.; Vezhnevets, A. S.; Cunningham, W. A.; and
Bileschi, S. M. 2025. A Pragmatic View of AI Personhood.
ArXiv:2510.26396 [cs.AI].
Lewis, S.; Dontcheva, M.; and Gerber, E. 2011. Affective
computational priming and creativity. InProceedings of the
SIGCHI Conference on Human Factors in Computing Sys-
tems, 735–744. Vancouver BC Canada: ACM. ISBN 978-1-
4503-0228-9.
Lifshitz, L. R.; and Hung, R. 2024. BC Tribunal Confirms
Companies Remain Liable for Information Provided by AI
Chatbot.
Loru, E.; Nudo, J.; Di Marco, N.; Santirocchi, A.; Atzeni,
R.; Cinelli, M.; Cestari, V .; Rossi-Arnaud, C.; and Quattro-
ciocchi, W. 2025. The simulation of judgment in LLMs.
Proceedings of the National Academy of Sciences, 122(42):
e2518443122.
Madden, D.; Cadet-James, Y .; Atkinson, I.; and Watkin Lui,
F. 2014. Probes and prototypes: a participatory action re-
search approach to codesign.CoDesign, 10(1): 31–45.
eprint: https://doi.org/10.1080/15710882.2014.881884.
Maden, W. v. d. 2026. Three Evaluation Problems for LLM-
Simulated Research Participants. InProceedings of the Ex-
tended Abstracts of the 2026 CHI Conference on Human
Factors in Computing Systems.
Maeda, T.; and Quan-Haase, A. 2024. When Human-AI
Interactions Become Parasocial: Agency and Anthropomor-
phism in Affective Design. InThe 2024 ACM Conference
on Fairness, Accountability, and Transparency, 1068–1077.
Rio de Janeiro Brazil: ACM. ISBN 979-8-4007-0450-5.
Maeda, T.; and Stark, L. 2025. Anthropomorphism as Social
Affordance: Charting the Co-Animation of Chatbots into
Social “Agents”.Proceedings of the AAAI/ACM Conference
on AI, Ethics, and Society, 8(2): 1661–1673.
Mayne, H.; Kearns, R. O.; Yang, Y .; Bean, A. M.; Delaney,
E.; Russell, C.; and Mahdi, A. 2025. LLMs Don’t Know
Their Own Decision Boundaries: The Unreliability of Self-
Generated Counterfactual Explanations.Proceedings of the
2025 Conference on Empirical Methods in Natural Lan-
guage Processing.
Narasimhan, S. 2026. The Flight Simulator for Manage-
ment: Generative-Agent Simulations for Faster, Safer Deci-
sions.
Nayak, A. 2021. Boredom, Time-Perception and Algorith-
mic Governmentality.Journal of AI Humanities, 7: 11–24.
New Sun Rising Pittsburgh. 2025. AI-driven Assistance: In-
troducing the NSR Virtual Support Center.
Nguyen, D. C.; and Welch, C. 2026. Generative Artificial In-
telligence in Qualitative Data Analysis: Analyzing—Or Just
Chatting?Organizational Research Methods, 29(1): 3–39.
Orr, J. E. 1996.Talking about machines: an ethnography of
a modern job. Collection on technology and work. Ithaca,
N.Y: ILR Press. ISBN 978-1-5017-0739-1.
Premananda, H. 2026.Non-Venatus: On the Production of
Wars and Universities. Bloomsbury. ISBN 978-93-6952-
647-5.
Redelmeier, D. A.; Katz, J.; and Kahneman, D. 2003. Mem-
ories of colonoscopy: a randomized trial.Pain, 104(1): 187–
194.
Reshef Kera, D.; Navon, E.; Wellner, G.; and Kalvas, F.
2024. Governance in Silico: Experimental Sandbox for Pol-
icymaking over AI Agents.
Riedl, M. O.; and Desai, D. R. 2025. AI Agents and the Law.
Proceedings of the AAAI/ACM Conference on AI, Ethics,
and Society, 8(3): 2189–2198.
Rising, N. S. 2025. Community V oice – New Sun Rising.
Rouvroy, A.; and Berns, T. 2013. Algorithmic governmen-
tality and prospects of emancipation:Disparateness as a pre-
condition for individuation through relationships?R ´eseaux,
177(1): 163–196.
Sampson, P.; Lurie, E.; and Metaxa, D. 2026. Surveying the
LLM Simulation of Marginalized Identities. InProceedings
of the Extended Abstracts of the 2026 CHI Conference on
Human Factors in Computing Systems.
Sanders, E. B.-N.; Brandt, E.; and Binder, T. 2010. A frame-
work for organizing the tools and techniques of participa-
tory design. InProceedings of the 11th Biennial Participa-
tory Design Conference, 195–198. Sydney Australia: ACM.
ISBN 978-1-4503-0131-2.
She, J.; Seepersad, C. C.; Holtta-Otto, K.; and MacDonald,
E. F. 2018. Priming Designers Leads to Prime Designs. In
Plattner, H.; Meinel, C.; and Leifer, L., eds.,Design Think-
ing Research, 251–273. Cham: Springer International Pub-
lishing. ISBN 978-3-319-60966-9 978-3-319-60967-6. Se-
ries Title: Understanding Innovation.
Simile.ai. 2026. Home|Simile.
Simonsen, J.; Karasti, H.; and Hertzum, M. 2020. Infrastruc-
turing and Participatory Design: Exploring Infrastructural
Inversion as Analytic, Empirical and Generative.Computer
Supported Cooperative Work (CSCW), 29(1-2): 115–151.
Smith, B. C. 2019.The Promise of Artificial Intelligence:
Reckoning and Judgment. Cambridge: MIT Press. ISBN
978-0-262-04304-5 978-0-262-35520-9.
Smith, K. L.; Akanbi, O.; Maqsood, S.; Obar, J. A.; Red-
den, J.; and Bannerman, S. 2025. Crafting an Intersectional
Response to Bill C-27 for the Standing Committee on Indus-
try and Technology.Canadian Journal of Communication,
50(1): 54–67.
Sommers, S. R. 2006. On racial diversity and group deci-
sion making: Identifying multiple effects of racial composi-
tion on jury deliberations.Journal of Personality and Social
Psychology, 90(4): 597–612.

Stark, L. 2024. Animation and Artificial Intelligence. In
The 2024 ACM Conference on Fairness, Accountability, and
Transparency, 1663–1671. Rio de Janeiro Brazil: ACM.
ISBN 979-8-4007-0450-5.
Strawson, P. 1962. Freedom and Resentment.Proceedings
of the British Academy, 48: 187–211.
Su, R. 2026. Toward Risk-Calibrated Standards for LLM-
Simulated Participants in Human Subjects Research. InPro-
ceedings of the Extended Abstracts of the 2026 CHI Confer-
ence on Human Factors in Computing Systems.
Suchman, L. A. 1987.Plans and situated actions: the prob-
lem of human-machine communication. Cambridge [Cam-
bridgeshire] ; New York: Cambridge University Press. ISBN
978-0-521-33137-1 978-0-521-33739-7.
Tan, C. T.; Atmosukarto, I.; Tandianus, B.; Shen, S.; and
Wong, S. 2025. Exploring the Impact of Avatar Represen-
tations in AI Chatbot Tutors on Learning Experiences. In
Proceedings of the 2025 CHI Conference on Human Fac-
tors in Computing Systems, 1–12. Yokohama Japan: ACM.
ISBN 979-8-4007-1394-1.
Timaite, G.; and Castelle, M. 2025. Agents Without Agency:
Anthropological and Sociological Lessons for Contempo-
rary AI Research and Policy.Proceedings of the AAAI/ACM
Conference on AI, Ethics, and Society, 8(3): 2493–2507.
Wang, A.; Morgenstern, J.; and Dickerson, J. P. 2025.
Large language models that replace human participants
can harmfully misportray and flatten identity groups.
ArXiv:2402.01908 [cs].
Weizenbaum, J. 1976.Computer power and human rea-
son: from judgment to calculation. San Francisco: Freeman.
ISBN 978-0-7167-0464-5 978-0-7167-0463-8.
Xiao, Y .; Cheng, Y .; Fu, J.; Wang, J.; Li, W.; and Liu, P.
2024. How Far Are LLMs from Believable AI? A Bench-
mark for Evaluating the Believability of Human Behavior
Simulation. ArXiv:2312.17115 [cs].
Yang, J. 2026. Carrier: Infrastructure for Validating LLMs
as Simulated Research Participants. InProceedings of the
Extended Abstracts of the 2026 CHI Conference on Human
Factors in Computing Systems.
Young, I. M. 2000.Inclusion and Democracy. Oxford po-
litical theory. Oxford: Oxford university press. ISBN 978-0-
19-829755-0.
