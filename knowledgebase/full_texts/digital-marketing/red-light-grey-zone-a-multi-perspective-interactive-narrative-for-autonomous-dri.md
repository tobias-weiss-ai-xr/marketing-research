---
title: 'Red Light, Grey Zone: A Multi-Perspective Interactive Narrative for Autonomous Driving Ethics'
url: https://arxiv.org/abs/2607.15888
category: digital-marketing
subcategory: empirical
date: 2026-07
venue: ''
authors:
- Mengyi Wei
- Nianhua Liu
- Chenyu Zuo
- Liqiu Meng
source: arxiv
pdf_url: https://arxiv.org/pdf/2607.15888
pages: 11
chars: 60356
fetched_at: '2026-11-08T13:21:32+00:00'
kb_version: 1
---

# Red Light, Grey Zone: A Multi-Perspective Interactive Narrative for Autonomous Driving Ethics

Red Light, Grey Zone: A Multi-Perspective Interactive Narrative for Autonomous
Driving Ethics
Mengyi Wei1, Nianhua Liu1, Chenyu Zuo2, Liqiu Meng1
1Technical University of Munich
2University of Augsburg
mengyi.wei@tum.de, nianhua.liu@tum.de, chenyu.zuo@uni-a.de, liqiu.meng@tum.de
Abstract
Autonomous driving ethics is not only an expert concern,
but also a public issue involving risk, responsibility, and
governance. However, non-experts often struggle to interpret
these issues in concrete incidents, especially when responsi-
bility is distributed across multiple stakeholders. This paper
investigates interactive narrative as a public-facing method
for eliciting situated ethical reflection on autonomous driv-
ing. We presentRed Light, Grey Zone, a web-based, multi-
perspective interactive narrative prototype inspired by a real-
world autonomous-driving incident. The prototype invites
participants to compare stakeholder perspectives, examine
scene materials, and make responsibility judgments in the
face of ethical ambiguity. We report an exploratory user study
(N= 12) examining how differently non-experts responded
to the prototype. Our analysis focuses on three dimensions
of reflection: ethical cognition, responsibility-focused crit-
ical thinking, and multi-perspective reasoning. Exploratory
pre-post results showed the strongest self-reported shift in
responsibility-focused critical thinking among participants
who completed the intended stakeholder-comparison pro-
cess, while ethical cognition and multi-perspective reason-
ing showed positive directional trends. Qualitative findings
further show how participants reflected on safety and mar-
ket trade-offs, responsibility ambiguity, transparency and pri-
vacy, and governance gaps. Participants also used stakeholder
comparison to corroborate evidence and, in many cases,
broaden responsibility judgments from single-actor blame to-
ward more distributed interpretations of accountability. Over-
all, the study suggests that multi-perspective interactive nar-
ratives may support non-expert reflection on accountability,
evidence, and governance in AI-enabled systems.
Introduction
As Artificial Intelligence (AI) becomes increasingly embed-
ded in everyday life, ethical concerns have become more vis-
ible, more consequential, and more difficult to separate from
questions of governance. These concerns do not typically
appear as a single, general problem of “AI ethics.” Rather,
they emerge in specific sociotechnical settings where re-
sponsibility, risk, and value trade-offs are distributed across
multiple actors. Autonomous driving is a particularly signif-
icant case because AI-driven decisions are enacted in public
space, involve the possibility of physical harm, and require
ongoing negotiation among companies, users, bystanders,
and regulators. In this field, ethical debates often center
on the question of responsibility: companies prioritize de-
ployment and commercial viability, users value convenience
and liability protection, pedestrians seek safety and fairness,
while regulators must balance innovation, public account-
ability, and acceptable risk. These objectives can conflict,
and their conflicts rarely admit a single correct solution. Eth-
ical governance in autonomous driving therefore requires
attention to sociotechnical and normative questions beyond
technical performance alone.
However, a practical challenge is that meaningful public
engagement with autonomous driving ethics remains diffi-
cult. Much of the existing discussion is shaped either by
expert discourse or by simplified moral-dilemma framings,
leaving limited room for understanding how ordinary peo-
ple make sense of responsibility, risk, and governance in
more situated ways. In this paper, we use non-experts to
refer to members of the public who do not have formal
training in the technical, legal, or ethical dimensions of au-
tonomous driving, such as passengers, pedestrians, family
members, and other affected citizens. Traditional awareness-
raising approaches, including policy documents and educa-
tional lectures, often rely on abstract concepts and gener-
alized explanatory frameworks. While such materials may
communicate principles, they do not necessarily help non-
experts understand how stakeholder positions differ in con-
crete situations, how risks are distributed, or how ethical
conflict unfolds across a chain of events (Wei et al. 2025).
As a result, public-facing reflection on autonomous driv-
ing ethics often remains broad and generalized, limiting the
formation of more specific judgments about responsibility,
accountability, and governance. Therefore, supporting non-
expert reflection on these issues is an important challenge for
AI ethics research and public-facing AI governance (Kwak,
Ahn, and Seo 2022).
At the same time, existing work on autonomous driving
ethics has largely relied on surveys, vignette-based moral
dilemmas, trust and acceptance models, or scenario-based
evaluations (Zhang et al. 2024; Ng et al. 2024; Beckers et al.
2022; Zhai et al. 2024). These approaches have generated
important insights into public preferences, blame attribution,
and adoption attitudes. However, they tend to examine eth-
ical responses as isolated judgments, with less attention to
how interpretations develop across multiple stakeholder per-
spectives and stages of a contested event (Zhang et al. 2024;
arXiv:2607.15888v1  [cs.CY]  17 Jul 2026

Stilgoe et al. 2021). They also often foreground a single de-
cision point, such as a collision dilemma, while giving less
attention to the broader sociotechnical chain through which
responsibility is interpreted, negotiated, and assigned (Rhim
et al. 2021; Kirchmair 2023). As a result, we still know rel-
atively little about how non-experts reflect on autonomous
driving ethics when they are asked to engage with ambigu-
ity, compare stakeholder viewpoints, and reason about ac-
countability across an unfolding scenario.
This study investigates interactive narrative as a public-
facing engagement format and as a research method. It ex-
amines how non-experts make sense of controversial re-
sponsibility in autonomous driving. Interactive narrative en-
ables participants to engage with unfolding events through
choices, perspective shifts, and consequence-based progres-
sion. By situating ethical issues in concrete scenarios, it
makes stakeholder positions, conflicting values, and possi-
ble consequences more legible (Naul and Liu 2020; Buijs-
Spanjers et al. 2020; Belman and Flanagan 2010; da Silva
and Schrier 2025). In autonomous driving, ethical disagree-
ment emerges across events involving various actors and
constraints. Interactive narrative presents ethical issues ac-
cessibly and enables closer examination of concerns that
non-experts find important. It shows how interpretations of
responsibility differ across stakeholder perspectives(Belman
and Flanagan 2010). The study moves beyond asking if non-
experts can identify ethical issues. It examines how multi-
perspective engagement shapes non-expert reasoning about
responsibility and governance in AI systems (Stilgoe et al.
2021; Rhim et al. 2021).
Building on this rationale, we investigate how aweb-
based multi-perspective interactive narrative prototypecan
support non-experts’ reflection on ethics in autonomous
driving incidents:
•RQ1:What ethical themes become salient to non-experts
when engaging with the interactive narrative about au-
tonomous driving ethics?
•RQ2:How does comparing stakeholder perspectives
shape non-experts’ interpretations of ethical conflict in
autonomous driving?
To address these questions, we develop Red Light, Grey
Zone, an interactive narrative prototype grounded in a real-
world autonomous driving ethics incident. 1 The prototype
is designed as a multi-perspective experience in which par-
ticipants examine a contested autonomous vehicle incident
through the perspectives of different stakeholders. Through
a branching narrative, participants review scene materi-
als, compare stakeholder accounts, and make judgments
about responsibility and possible responses. By situating
autonomous driving ethics within a specific sociotechnical
context, the design allows non-experts to engage with am-
biguity, conflicting interpretations, and distributed responsi-
bility.
This paper makes three contributions. First, we introduce
Red Light, Grey Zone, a web-based multi-perspective in-
teractive narrative prototype that translates a real-world au-
1https://incidentdatabase.ai/cite/8
tonomous driving incident into situated scenarios, stake-
holder accounts, and responsibility-judgment tasks. Second,
we articulate a design approach for using interactive nar-
rative to examine how non-experts reason about contested
responsibility under incomplete information and divergent
stakeholder accounts. Third, as part of the early-stage pro-
totyping of AI ethics systems, through an exploratory user
study (N=12), we provide empirical insight into what ethical
themes become salient to non-experts and how stakeholder
comparison shapes their interpretations of responsibility in
an autonomous driving incident.
Related Work
Interactive Narrative for Public Engagement with
Autonomous Driving Ethics
Research on autonomous driving ethics has revealed how
public attitudes shape risk, blame, trust, and adoption. Most
studies use surveys, vignettes, or models that isolate deci-
sions or abstract trade-offs (Zhang et al. 2024). These ap-
proaches identify preferences and judgments but fail to cap-
ture how non-experts interpret ethical conflict as ongoing,
socially situated events. This is critical, as ethical questions
in autonomous driving arise across multiple stages—system
design, deployment, accident interpretation, accountability,
and governance(Stilgoe and Cohen 2021). Abstract or static
scenarios can be difficult for non-experts because they offer
limited support for situating stakeholder positions, system
behavior, and consequences within a coherent context.
To address these limitations, interactive narrative offers
a useful response to the methodological challenge outlined
above. It situates ethical issues within unfolding scenarios
and enables participants to engage through choices, perspec-
tive shifts, and consequence-based progression. Prior work
suggests that narrative-based and game-based formats can
support engagement, reflection, and situated sense-making
by making complex issues more concrete and easier to fol-
low (Naul and Liu 2020). Interactive narrative is there-
fore relevant as both a communication format and a re-
search method for eliciting how participants interpret am-
biguity, conflict, and responsibility in context. In this study,
perspective-taking is treated as comparative reasoning rather
than as empathy training.
Despite narrative and serious-game approaches being
adopted in education and social studies, their use to study
non-expert reasoning about autonomous driving ethics re-
mains underexplored. Specifically, there is a limited under-
standing of how interactive narrative supports non-experts
in expressing ethical concerns and responsibility judgments
during a contested incident. This study directly addresses
this gap, employing an interactive narrative prototype to re-
veal which ethical themes non-experts prioritize and how
they make sense of responsibility in context.
Multi-Perspective Interaction in Autonomous
Driving
A core challenge in the ethics of autonomous driving lies
in the fact that responsibility rarely rests with a single en-
tity. Instead, it is dispersed among companies, engineers,

users, pedestrians, investigators, regulators, and other af-
fected members of the public. Consequently, the same inci-
dent may be interpreted in radically different ways depend-
ing on the perspective, whether viewed as a technical failure,
a design choice, a governance issue, a communication break-
down, or an inequitable distribution of risk. In this sense,
responsibility in autonomous driving is not only diffuse but
also contentious(Stilgoe and Cohen 2021). Prior work has
shown that responsibility attribution in autonomous driving
is shaped by contextual factors, including system capability,
human control, accident framing, and public expectations.
However, many existing studies still examine responsibility
through single-shot judgments, such as blame allocation in
a scenario, preference for a moral rule, or trust in a system’s
decision. While such approaches are useful for identifying
patterns in public evaluation, they offer less insight into how
people may reinterpret responsibility when exposed to mul-
tiple stakeholder positions and conflicting accounts of the
same event(Zhang et al. 2024).
For this reason, multi-perspective interaction functions as
an analytic design choice in the present study. It allows us
to examine how responsibility judgments are formed, chal-
lenged, and revised when the same incident is encountered
from different stakeholder positions. This is particularly im-
portant in autonomous driving, where ethical disagreement
often arises from divergent priorities, constraints, and inter-
pretations (Rhim et al. 2021). A passenger may focus on
safety and reliance on the system, a company on deploy-
ment and system limits, a regulator on public risk, and a fam-
ily member on accountability and fairness. Comparing these
positions can shift what participants notice, what they con-
sider relevant, and how they assign responsibility. A multi-
perspective interactive structure therefore provides a way to
study contested responsibility in autonomous driving ethics.
It supports closer examination of how non-experts com-
pare stakeholder viewpoints, how ethical conflict becomes
salient through contrast, and how responsibility interpreta-
tions shift during an unfolding incident. This motivates our
use of multi-perspective interaction as a core design mech-
anism for examining non-experts’ ethical reflection and re-
sponsibility judgments (da Silva and Schrier 2025).
Design of the Multi-perspective Interactive
Narrative
Overview and Design Goals
Drawing on the literature reviewed above, we designedRed
Light, Grey Zoneas a web-based, multi-perspective interac-
tive narrative for examining how non-experts interpret eth-
ical conflict in autonomous driving. The prototype was de-
signed to provide a situated and interpretable representation
of an ethically controversial incident. Our design specifi-
cally responds to two challenges identified in prior work:
first, that non-experts often encounter autonomous driving
ethics through abstract or fragmented explanations; and sec-
ond, that responsibility in such incidents is distributed across
multiple actors, making it difficult to understand from a sin-
gle perspective.
The prototype is grounded in a real-world autonomous-
driving incident in which an autonomous vehicle ran a red
light, triggering public debate about safety governance and
responsibility attribution. Public reports and incident doc-
umentation were used to preserve the core event structure
and ethical tensions, including the red-light violation, dis-
puted responsibility, and uncertainty about system behavior
and public oversight. For interaction, these materials were
adapted into fictionalized stakeholder accounts, dialogue,
and scene materials. Contextual details, such as temporal or-
dering and location cues, were added to improve narrative
coherence without changing the incident’s underlying re-
sponsibility structure. To avoid presenting a single authorita-
tive frame, each stakeholder account was designed as partial
and potentially biased, requiring participants to compare ac-
counts before making a responsibility judgment. Additional
details on scenario construction are provided in the supple-
mentary materials.
A central design decision was to organize the prototype
around four stakeholder perspectives:company representa-
tive, eyewitness, company employee, and traffic author-
ity. These perspectives were selected because each captures
a distinct standpoint from which the incident can be inter-
preted: organizational defense and risk management, imme-
diate experiential observation, internal technical or institu-
tional knowledge, and public regulatory accountability. The
goal of this selection was to foreground contrasting posi-
tions that make responsibility attribution ethically and so-
cially contested. In this way, the prototype uses stakeholder
contrast not merely as a narrative device, but as a mecha-
nism for examining how non-experts compare explanations,
notice conflicting priorities, and revise their interpretations
of responsibility.
This design directly supports the study’s two research
goals. First, by engaging participants with a concrete yet
contested incident, the prototype allows us to examine what
ethical themes become salient to non-experts. Second, by
presenting the incident through multiple stakeholder per-
spectives, it enables us to examine how participants’ inter-
pretations of ethical conflict are shaped through comparison
rather than through a single account.
Design Rationale
The prototype was designed to address two challenges iden-
tified in prior work. First, non-experts often encounter au-
tonomous driving ethics through abstract explanations or
simplified moral dilemmas, making it difficult to connect
ethical concepts to concrete situations. Second, responsi-
bility in autonomous driving incidents is distributed across
stakeholders whose interests, institutional roles, and knowl-
edge claims may conflict. To respond to these challenges,
we designed the prototype as a situated, multi-perspective,
and judgment-oriented interactive narrative.
More specifically, the design was guided by three princi-
ples.P1. Situate ethical conflict in a concrete incident.
The prototype is organized around a single autonomous-
driving incident adapted from a real-world case, allowing
participants to consider how safety, accountability, and gov-
ernance emerge through an unfolding situation.P2. High-

light the perspectives of conflicting stakeholders.The in-
cident is presented from four perspectives: a company repre-
sentative, an eyewitness, a company employee, and a traffic
authority. These roles represent organizational defense, di-
rect observation, internal knowledge, and public regulatory
responsibility, making visible how the same event can be in-
terpreted differently.P3. Support responsibility reasoning
under uncertainty.Participants are positioned as investi-
gators who examine scene materials, compare stakeholder
accounts, and make a responsibility judgment under incom-
plete and sometimes conflicting information. Together, these
principles operationalize ethical reflection as a sequence of
actions: examining evidence, contrasting perspectives, rec-
ognizing uncertainty, and making a justified judgment.
Prototype Structure and Interaction Flow
Figure 1 summarizes how the design rationale is translated
into the prototype structure. The prototype consists of four
connected components: an incident background, selected
stakeholder perspectives, an interaction loop, and interface
stages. Together, these components implement the three de-
sign principles described above.
First, the prototype is anchored in a real-world incident in-
volving an autonomous vehicle running a red light (Figure 1,
top left). This incident provides a concrete entry point for re-
flecting on responsibility attribution, safety governance, and
the public legitimacy of autonomous driving systems.
Second, the incident is presented through four stakeholder
perspectives:company representative,eyewitness,company
employee, andtraffic authority(Figure 1, top center). These
perspectives were selected to foreground different interpre-
tive positions rather than to provide an exhaustive map of all
affected actors.
Third, participant interaction is organized as a loop in
which users move across stakeholder accounts, request ad-
ditional information, compare competing claims, and make
a final judgment (Figure 1, top right). Participants do not re-
ceive all information at once; instead, they work through par-
tial and sometimes conflicting materials, which encourages
them to assess credibility, notice uncertainty, and reconsider
initial assumptions.
Fourth, these design choices are implemented through
four interface stages: a start interface, an introduction inter-
face, a stakeholder interface, and a decision interface (Fig-
ure 1, bottom row). This staged progression guides partic-
ipants from contextual orientation, to perspective compari-
son, and finally to explicit responsibility attribution. In this
way, the prototype provides a structured setting in which
non-experts can articulate ethical concerns and reconsider
responsibility through multi-perspective engagement.
Content Production and Implementation
The prototype combines textual narrative with comic-style
visual scenes to make the progression of the incident, the
contrast between stakeholder accounts, and the points of eth-
ical tension more immediately interpretable to non-expert
participants. These visuals support comprehension of the un-
folding scenario and highlight key moments of conflict, un-
certainty, and investigation. Their function is illustrative and
interpretive, focusing on how participants follow the inci-
dent and its ethical tensions. In this way, the visual layer
complements the interactive narrative structure by making
the incident easier to follow while maintaining a relatively
low interpretive barrier.
The content production process was organized around the
prototype’s incident-centered and multi-perspective design.
For each scene, we first defined its narrative function in rela-
tion to the overall responsibility reasoning process, includ-
ing what new information, uncertainty, or stakeholder po-
sition the scene was intended to introduce. We then devel-
oped scene-specific dialogue, materials, and participant op-
tions so that each perspective contributed a distinct interpre-
tive standpoint rather than merely repeating previously pre-
sented facts. Comic-style visual panels were subsequently
created to reinforce the main contextual or affective cues of
each scene, such as conflict, doubt, institutional positioning,
or evidentiary tension. To support iterative development and
maintain stylistic consistency across scenes, we used gener-
ative AI tools to produce these illustrations. Their role was
primarily practical, enabling rapid prototyping and visual
coherence across the prototype. The study analyzed partici-
pants’ interaction with the narrative experience, rather than
the generative AI production process itself.
As far as its implementation is concerned, the proto-
type was developed as a lightweight web-based applica-
tion using HTML5, CSS, and JavaScript. This choice al-
lowed the system to remain easily deployable and accessible
through a standard browser, which was appropriate for an
exploratory user study with non-expert participants. The nar-
rative structure was implemented as a modular set of scene
objects, each containing perspective-specific content, avail-
able actions, and branching transitions. Participant progres-
sion, selected options, and collected materials were managed
through client-side state tracking, allowing the prototype to
preserve the interaction flow across scenes. At each stage,
the interface presents narrative text, a scene illustration, and
two to four actionable options. These options determine the
next step in the narrative and shape the information avail-
able to participants as they move toward a final responsi-
bility judgment. Overall, the prototype emphasizes situated
ethical interpretation over technically detailed simulation. It
provides a structured, accessible, and multi-perspective set-
ting for non-experts to examine ethical conflict arising from
a contested autonomous-driving incident.
User Study
We conducted an exploratory user study to clarify how non-
experts engage with and interpret ethical issues inRed Light,
Grey Zone, a web-based, multi-perspective interactive nar-
rative about a contested autonomous-driving incident. The
study aimed to determine what ethical topics became salient
during interaction and how stakeholder perspective compar-
isons influenced views of responsibility. Instead of evaluat-
ing the prototype as a broad educational tool, we used it as
a research instrument to elicit situated ethical reflection, re-
sponsibility reasoning, and governance-relevant trade-offs.
All study procedures were approved by the IRB before re-
cruitment.

Figure 1: Overview of the design and implementation ofRed Light, Grey Zone. The figure shows four connected layers of
the prototype: (1) the real-world incident background that grounds the narrative, (2) the four stakeholder perspectives used to
structure contested interpretations of the event, (3) the interaction loop through which participants compare accounts and make
a final responsibility judgment, and (4) the main interface stages that realize the web-based interactive narrative experience.
Participants
We recruited 12 adult participants via university postings
and internal channels. Participants were university-affiliated
adults from mixed disciplinary backgrounds. None reported
formal training or professional experience in autonomous
driving, AI ethics, traffic law, or autonomous vehicle gov-
ernance. Prior knowledge of autonomous driving was not
required, allowing participants to engage as lay interpreters
rather than domain specialists.
This convenience sample should not be considered sta-
tistically representative of the general public. However, it
aligns with the exploratory objective of gaining preliminary
insight into how non-experts interpret ethical conflict and
responsibility through a multi-perspective interactive narra-
tive. All participants signed informed consent forms prior to
participation.
Experimental Procedure
We used a within-subjects pre-post design to capture partic-
ipants’ self-reported shifts before and after interacting with
the prototype. Because the study was exploratory and the
sample size was small, pre-post comparison identified direc-
tional changes rather than strong causal or population-level
claims. Sessions lasted about 30 minutes and consisted of
three phases: a pre-interaction survey, the interaction ses-
sion, and a post-interaction survey, with the full question-
naire provided in the supplementary materials.
Pre-survey(about 5 minutes). Participants rated their
general knowledge and understanding of autonomous driv-
ing ethics on a 7-point scale. Items covered their self-
perceived knowledge, understanding of ethical challenges,
ability to spot ethical issues, and whether they tended to con-
sider multiple viewpoints about autonomous driving. These
items were the baseline for comparison.
Interaction session(about 10 minutes). Participants used
Red Light, Grey Zone, which showed the incident back-
ground, stakeholder views, evidence, and a task for judging
responsibility. They worked at their own pace and were told
there was no single right answer. There was no time limit,
but it usually took about 10 minutes.
Post-survey(about 15 minutes). After finishing the proto-
type, participants answered a post-survey with 7-point scale
questions and open-ended questions. The scale questions
asked if the prototype helped them understand ethical is-
sues, notice complexity, see conflicts between safety, effi-
ciency, and fairness, consider different sides, and reflect on
the event. Open-ended questions asked them to describe eth-
ical issues they saw, explain their responsibility judgment,
and reflect on how comparing views changed their interpre-
tation.
Measures and Data Collection
The study collected both quantitative and qualitative data.
Quantitative data consisted of pre- and post-interaction

Likert-scale responses. Because there is no established stan-
dard scale to measure non-experts’ reflection on autonomous
driving ethics through interactive narrative, we developed
study-specific questionnaire items informed by our research
questions and the prototype’s goals. These items are in-
tended as exploratory indicators, not validated psychometric
scales.
We organized the questionnaire items into three analytic
dimensions:ethical cognition,responsibility-focused crit-
ical thinking, andmulti-perspective reasoning(Table 1).
Ethical cognitionrefers to participants’ awareness and un-
derstanding of ethical issues in autonomous driving, in-
cluding responsibility attribution, safety trade-offs, fairness,
transparency, and privacy.Responsibility-focused critical
thinkingrefers to participants’ self-reported tendency to
question simplified explanations, examine competing claims
about responsibility, and recognize evidentiary uncertainty
in autonomous-driving incidents. This dimension was mea-
sured with a single paired item and is therefore interpreted
as an exploratory item-level indicator rather than as a val-
idated measure of general critical thinking ability.Multi-
perspective reasoningrefers to participants’ tendency to
consider how different stakeholders may interpret the same
incident differently.
These three categories were selected to capture comple-
mentary aspects of ethical reflection. Ethical cognition cap-
tures whether participants recognized and understood ethical
issues in general. Responsibility-focused critical thinking
captures whether participants noticed ambiguity and trade-
offs, rather than accepting just one version of the event.
Multi-perspective reasoning checks if participants compared
different views, which is important to the prototype and
RQ2.
As shown in Table 1, ethical cognition was represented by
three paired pre-post items. Responsibility-focused critical
thinking and multi-perspective reasoning were each repre-
sented by one paired item. Because the latter two dimen-
sions were measured with single paired items, the quan-
titative analysis of these constructs was treated as indica-
tive rather than definitive. We therefore relied on qualitative
analysis to provide a more detailed account of participants’
reasoning, especially regarding responsibility interpretation
and stakeholder comparison.
The qualitative data included participants’ open-ended re-
sponses after the interaction, including descriptions of ethi-
cal issues, explanations of responsibility, and reflections on
stakeholder perspectives. These responses were used to an-
swer the research questions by identifying ethical themes
important to participants and by examining how they un-
derstood responsibility through comparing stakeholder ac-
counts.
Data Analysis
We used a mixed-methods approach combining descrip-
tive quantitative analysis with qualitative thematic analysis.
Given the exploratory nature of the study, the analysis aimed
to characterize self-reported shifts and written reflections af-
ter participants interacted with the prototype, rather than to
provide confirmatory evidence of intervention effectiveness.
For the quantitative analysis, we grouped Likert-scale
items into the three analytic dimensions shown in Ta-
ble 1. Ethical cognition was computed as each participant’s
mean score across three paired items before and after in-
teraction. Responsibility-focused critical thinking and multi-
perspective reasoning were each represented by one paired
item and were therefore treated as exploratory item-level in-
dicators. We used paired-samplest-tests to describe within-
participant pre-post changes (Mara and Cribbie 2012) and
report Cohen’s within-subjects effect sized z = ¯d/Sd
(Goulet-Pelletier and Cousineau 2018), where ¯dis the mean
paired difference andS d is the standard deviation of the
paired differences.
Because RQ2 concerns stakeholder comparison, the quan-
titative pre-post analysis focused on then= 10participants,
from the full sample ofN= 12, who engaged with at least
three stakeholder perspectives before making the final re-
sponsibility judgment. The two limited-engagement partic-
ipants were retained in the qualitative analysis as boundary
cases. This distinction allowed us to describe self-reported
shifts among participants who experienced the prototype’s
intended comparison mechanism while still examining vari-
ation in how participants engaged with that mechanism.
For the qualitative analysis, we conducted thematic analy-
sis of participants’ open-ended responses (Willig and Rogers
2017). The analysis focused on two questions aligned
with the research questions: what ethical themes partici-
pants foregrounded, and how they described the role of
stakeholder comparison in responsibility judgment. Two re-
searchers independently reviewed the responses, generated
initial codes related to ethical concerns, trade-offs, stake-
holder interpretations, uncertainty, and responsibility attri-
bution, and then discussed and consolidated these codes into
higher-level themes. Participant quotes were lightly edited
for grammar and clarity without changing their substantive
meaning. The goal was not to produce a comprehensive the-
ory of autonomous-driving ethics, but to characterize recur-
ring patterns in how participants made sense of the incident
through the prototype.
Because the quantitative measures were study-specific
and the sample was small, qualitative responses were used
to interpret participants’ reasoning rather than to validate the
questionnaire results. In this sense, the quantitative analy-
sis provides a coarse overview of self-reported shifts, while
the qualitative analysis offers a richer account of the ethi-
cal themes and responsibility interpretations elicited by the
interactive narrative.
Results
We report findings from participants’ interactions withRed
Light, Grey Zone. We first present exploratory pre-post ques-
tionnaire results to provide an overview of self-reported
shifts among participants who completed the prototype’s in-
tended stakeholder-comparison process. We then use quali-
tative analysis to examine the two research questions: what
ethical themes became salient to participants after engag-
ing with the interactive narrative (RQ1), and how compar-
ing stakeholder perspectives shaped their interpretations of
ethical conflict (RQ2).

Table 1: Study-specific questionnaire items organized by analytic dimension.
Pre-interaction item Post-interaction item Analytic dimension
Q3. I am familiar with ethical issues related
to autonomous driving.
Q1. The prototype helped me reflect on eth-
ical issues related to autonomous driving.
Ethical cognition
Q4. I understand what autonomous driving
ethics means.
Q2. I became more aware of the complexity
of ethical issues in autonomous driving.
Ethical cognition
Q5. I understand the ethical challenges in-
volved in autonomous driving.
Q4. I noticed conflicts among efficiency,
safety, and fairness in autonomous driving.
Ethical cognition
Q6. I can identify potential ethical issues in
autonomous driving applications.
Q5. I am more likely to critically exam-
ine competing claims about responsibility
in autonomous driving incidents.
Resp.-focused CT
Q7. I tend to consider multiple viewpoints
when thinking about autonomous driving
events.
Q3. The prototype helped me consider how
different stakeholders may interpret the
same autonomous driving incident.
Multi-perspective rea-
soning
Note.The items are study-specific exploratory indicators rather than validated scales. Pre- and post-items were paired by
analytic dimension, with different wording. Resp.-focused CT = responsibility-focused critical thinking
Overview of Exploratory Self-reported Shifts
Before turning to the qualitative findings, we first report
exploratory pre-post questionnaire results to provide an
overview of participants’ self-reported shifts after interact-
ing with the prototype. Because the central mechanism of
Red Light, Grey Zoneis stakeholder comparison, the quan-
titative analysis focused on participants who completed the
intended comparison process. We defined completion as en-
gaging with at least three of the four stakeholder perspec-
tives before making the final responsibility judgment. Ten
of the twelve participants met this criterion. The remaining
two participants engaged with only one or two perspectives;
rather than treating them as invalid cases, we retained them
in the qualitative analysis as boundary cases that help char-
acterize when and why multi-perspective engagement may
be limited.
Table 2 reports exploratory paired-samples comparisons
for the perspective-comparison subgroup (n= 10, from
the full study sample ofN= 12). The clearest descrip-
tive self-reported shift was observed for the responsibility-
focused critical thinking item (+1.50,t(9) = 3.55,p=
.009,d z = 1.25), with seven of ten participants report-
ing higher post-interaction scores. Ethical cognition and
multi-perspective reasoning also showed positive directional
changes; however, given the small sample and study-specific
measures, these results should be interpreted as descriptive
trends rather than confirmatory evidence.
These quantitative trends provide context for the quali-
tative findings reported below, especially participants’ at-
tention to conflicting accounts, evidentiary uncertainty, and
responsibility attribution. The positive trends in ethical
cognition and multi-perspective reasoning are further un-
packed through the ethical themes participants foregrounded
and the ways they compared stakeholder perspectives. The
two limited-engagement cases are discussed as boundary
cases, illustrating that the prototype’s reflective potential de-
pends partly on how participants take up the stakeholder-
comparison mechanism.
Table 2: Exploratory paired-samples comparisons for the
perspective-comparison subgroup (n= 10, full sample
N= 12).
MeasurenDiff.t(d f)p d z Imp.
Ethical cognition 10 +1.42 2.57(9) .037 0.91 6/10
Resp.-focused CT 10 +1.50 3.55(9) .009 ∗ 1.25 7/10
Multi-persp. reasoning 10 +1.13 2.05(9) .080 0.72 5/10
Note.Diff. = post-pre score. Resp.-focused CT = responsibility-
focused critical thinking. Ethical cognition averages three paired
items. Resp.-focused CT and multi-persp. reasoning are single-
item exploratory indicators. Imp. = participants with higher post
scores, using all valid paired cases as the denominator.d z = Co-
hen’s within-subjects effect size.α adj =.0167. ∗p < .0167.
RQ1: Salient Ethical Themes After Interactive
Narrative Engagement
Participants’ open-ended responses showed four recurring
ethical themes: safety versus market incentives, ambiguity in
responsibility attribution, transparency and privacy, and le-
gal or institutional governance gaps. Together, these themes
suggest that participants interpreted the incident through
broader questions of accountability, evidence, and gover-
nance in autonomous driving, extending beyond the imme-
diate traffic violation.
Safety versus market incentives.Participants frequently
treated the red-light incident as a concern about whether
autonomous driving systems are deployed before sufficient
validation or oversight. Several argued that safety should
outweigh efficiency, convenience, or commercial pressure.
As P01 stated,“I am more inclined to prioritize safety over
efficiency. ”This suggests that participants understood au-
tonomous driving ethics as a trade-off between technical
performance, safety governance, and organizational incen-
tives.
Responsibility ambiguity.Nearly all participants identi-
fied responsibility attribution as central. Rather than locating

responsibility in one actor, they described it as distributed
across companies, drivers or users, system designers, and
regulators. For example, P02 noted that“the company, de-
veloper, and regulator all share responsibility. ”Some also
recognized institutional constraints; P03 suggested that em-
ployees may hold important information but lack authority
to make it public. These responses frame responsibility as
contested and institutionally mediated.
Transparency, evidence, and privacy.Many participants
emphasized data access, public records, and independent ev-
idence when stakeholder accounts conflict. As P08 put it,
“system logs should be released for independent review. ”
At the same time, several noted that transparency may con-
flict with privacy protection or create risks of data misuse.
Participants therefore treated transparency as a governance
trade-off involving accountability, evidence access, and pri-
vacy constraints.
Legal and institutional governance gaps.Participants
also connected the incident to certification, accident inves-
tigation, legal standards, and regulatory oversight. Several
called for clearer rules or third-party investigation mecha-
nisms to support fair responsibility attribution and public
trust. P10, for instance, called for“clearer rules before test-
ing on public roads. ”This theme shows how participants
moved from the immediate incident toward broader gover-
nance concerns.
Overall, the interactive narrative connected the vehicle’s
traffic-signal violation to wider concerns about safety gov-
ernance, contested responsibility, evidentiary transparency,
and institutional accountability.
RQ2: How Stakeholder Comparison Shaped
Responsibility Interpretation
Participants’ responses indicate that stakeholder comparison
shaped responsibility interpretation in three ways: it encour-
aged corroboration across accounts, made conflicting prior-
ities more visible, and broadened some judgments from im-
mediate fault to distributed accountability. It also revealed
boundary cases in which participants minimized perspective
comparison because of prior beliefs or evidentiary prefer-
ences.
From single account to corroboration.Several par-
ticipants reported that comparing stakeholder perspectives
helped them avoid relying on a single account. As P02 noted,
“I would not rely on only one side of the story. ”Participants
evaluated claims from the company representative, eyewit-
ness, company employee, and traffic authority by consider-
ing which accounts appeared subjective, self-protective, or
more verifiable. Some treated eyewitness testimony as use-
ful but incomplete, while others placed greater weight on in-
stitutional records or technical explanations. This suggests
that stakeholder comparison supported evidence-oriented
responsibility reasoning: participants considered not only
what was said, but also who said it and under what con-
straints.
Making stakeholder conflict visible.The multi-
perspective structure made ethical conflict more visible by
presenting the same incident through different institutional
and experiential positions. Participants identified tensions
between corporate self-protection and public accountability,
rapid deployment and safety validation, and transparency
and privacy. P05 described this tension as“The company
wants to protect itself, but the public needs accountability. ”
These conflicts became more salient through comparison,
suggesting that the prototype helped reveal how ethi-
cal disagreement emerges from divergent priorities and
responsibilities.
From individual blame to distributed responsibility.
Many participants moved beyond attributing responsibility
to a single actor and instead described responsibility as dis-
tributed among the company, system developers, regulators,
and broader governance structures. As P02 wrote,“Respon-
sibility should be shared among the company, engineers,
and regulators. ”This was especially visible when partici-
pants connected the incident to system validation, regulatory
oversight, or organizational decision-making. In this sense,
stakeholder comparison broadened the interpretation of re-
sponsibility from immediate fault to sociotechnical account-
ability.
Boundary cases: limited perspective exploration.Two
participants, P04 and P09, consulted only one or two stake-
holder perspectives before reaching a judgment. We treat
them as boundary cases rather than invalid responses. P04
attributed responsibility to the company after confirming
that the car ran a red light, explaining that companies of-
ten release immature technologies for profit and that addi-
tional viewpoints were unlikely to change this view. P09 was
skeptical of subjective accounts and preferred verifiable ev-
idence, treating some stakeholder testimony as potentially
biased and emphasizing the need for extensive simulation
and on-road validation before deployment.
These cases complicate a simple positive account of
multi-perspective interaction: stakeholder comparison sup-
ported responsibility reasoning for many participants, but its
role depended on prior beliefs, trust in evidence, and willing-
ness to treat stakeholder accounts as relevant to judgment.
Discussion
Our findings suggest that the value of a multi-perspective
interactive narrative lies less in teaching predefined ethi-
cal principles and more in making responsibility, evidence,
and institutional constraints available for non-expert rea-
soning. InRed Light, Grey Zone, participants did not en-
gage with autonomous driving ethics only as an abstract
question of whether an autonomous vehicle behaved cor-
rectly. Instead, many interpreted the incident through con-
crete concerns such as safety validation, commercial in-
centives, evidence access, information disclosure, privacy
constraints, and regulatory accountability. We discuss three
implications: how non-experts reasoned about autonomous
driving ethics through situated responsibility problems, how
interactive narrative can function as an elicitation method
for public-facing AI ethics research, and what the multi-
perspective structure reveals about stakeholder comparison.

From Ethical Awareness to Situated Responsibility
Reasoning
The ethical themes identified in the study suggest that non-
experts can engage with autonomous-driving ethics in con-
crete, governance-relevant ways when ethical issues are situ-
ated in a specific incident. Participants’ reflections clustered
around safety versus market incentives, responsibility am-
biguity, transparency and privacy, and legal or institutional
governance gaps. Rather than treating these themes as sep-
arate opinions, we interpret them as indications that partici-
pants often understood the incident as part of a broader so-
ciotechnical responsibility structure. The red-light violation
became a starting point for considering how autonomous
driving systems are developed, deployed, explained, and
governed.
This finding shifts the emphasis from general “ethics
awareness” toward situated responsibility reasoning. Partic-
ipants did not necessarily use formal ethical vocabulary, yet
they reasoned about core AI ethics issues through practical
questions: whether the company had adequately validated
the system, whether evidence should be disclosed, whether
privacy should limit transparency, and whether independent
investigation or regulatory oversight was needed. These con-
cerns map onto broader questions of accountability and gov-
ernance, but they appeared in participants’ responses as con-
crete judgments about evidence, responsibility, and institu-
tional procedure.
Thus, incident-based interactive narratives may help make
governance questions more accessible by translating them
into interpretive problems: What evidence is available? Who
has access to it? Which stakeholder account should be
trusted? Who has the authority to disclose information, halt
deployment, or assign responsibility? This suggests that
public-facing AI ethics engagement need not begin with ab-
stract principles alone; it can also begin with situated ques-
tions about how responsibility is made visible, contested,
and governed.
Interactive Narrative as an Elicitation Method for
Public AI Ethics
The study also points to the methodological value of interac-
tive narrative for AI ethics research. Existing public-facing
approaches often rely on surveys, vignettes, or abstract ex-
planations. These methods can identify preferences or atti-
tudes, but they provide limited insight into how participants
navigate ambiguity, weigh evidence, or reinterpret respon-
sibility as a scenario unfolds. By contrast,Red Light, Grey
Zoneelicited final responsibility judgments as well as partic-
ipants’ explanations of how they compared stakeholder ac-
counts, evaluated evidence, and reasoned about institutional
constraints.
In this sense, interactive narrative should not be under-
stood only as an educational or communication format. It
can also serve as an elicitation method for studying situated
ethical interpretation. Because participants encounter infor-
mation sequentially and through stakeholder perspectives,
researchers can observe how they take up, reject, or reweight
different accounts. This is particularly useful for studying
domains such as autonomous driving, where responsibility
is contested, evidence may be incomplete, and ethical dis-
agreement is distributed across technical, organizational, le-
gal, and public actors.
This methodological contribution is distinct from claim-
ing that the prototype directly improved ethical compe-
tence. Our quantitative findings provide exploratory evi-
dence of self-reported shifts among participants who com-
pleted the intended perspective-comparison process, espe-
cially in responsibility-focused critical thinking. However,
the qualitative findings are more central to our contribution:
they show how participants articulated responsibility, un-
certainty, and governance concerns after working through
the narrative. The prototype, therefore, functioned less as
a tool for measuring whether participants learned a prede-
fined lesson, and more as a structured setting for eliciting
how non-experts make sense of contested responsibility in
an AI-enabled sociotechnical system.
The Role and Limits of Multi-Perspective
Comparison
The multi-perspective structure shaped participants’ inter-
pretations of responsibility by making visible how the same
autonomous-driving incident could be framed from different
positions, interests, and information constraints. For many
participants, comparing company, eyewitness, employee,
and traffic authority perspectives appeared to support a shift
from single-point blame toward more relational interpreta-
tions of accountability. Responsibility was not confined to
the vehicle’s immediate behavior or to one actor’s deci-
sion; participants also linked it to organizational deployment
choices, evidentiary access, disclosure practices, and regula-
tory oversight.
This suggests that multi-perspective interaction can help
turn uncertainty into an object of reasoning rather than sim-
ply a barrier to judgment. When participants encountered
conflicting accounts, they often asked which forms of ev-
idence were more reliable, which stakeholders had incen-
tives to withhold or frame information, and what institu-
tional mechanisms might be needed to resolve uncertainty.
In this way, the prototype made contested responsibility vis-
ible as a problem of evidence, position, and governance.
At the same time, our findings caution against assuming
that access to multiple perspectives automatically leads to
multiperspective reasoning. The boundary cases show that
participants entered the narrative with prior assumptions,
evidentiary preferences, and trust judgments that shaped
whether they considered additional perspectives useful. P04
relied on a strong prior framing that companies may re-
lease immature technologies for profit, while P09 privileged
verifiable evidence over subjective stakeholder testimony.
These cases suggest that multi-perspective systems should
not merely provide different viewpoints; they may also need
to prompt users to reflect on why they privilege some ac-
counts over others.
This also reframes the role of empathy in the prototype.
Although perspective shifts may encourage participants to
consider stakeholder constraints, our data do not justify
strong claims about immersion, embodied role-taking, or

empathy generation. The prototype positioned participants
primarily as investigators comparing stakeholder accounts,
not as fully inhabiting each stakeholder’s role. Its contribu-
tion is therefore better understood as perspective comparison
rather than empathy training. This form of comparison fore-
grounds constraints, incentives, and information asymme-
tries as conditions under which responsibility is interpreted.
Implications for Public-facing AI Governance
These exploratory findings suggest implications for public-
facing AI governance. Public engagement with AI ethics is
sometimes framed as a problem of communicating princi-
ples to lay audiences. Our results suggest a complementary
framing: non-experts may be better supported when ethi-
cal principles are translated into situated questions about
responsibility, evidence, and institutional procedure. In the
context of autonomous driving, participants’ concerns often
centered on concrete governance mechanisms, including in-
dependent audits, traceable system logs, standardized dis-
closure, third-party investigation, and regulatory oversight.
These mechanisms helped participants connect an individ-
ual incident to broader questions of accountability and legit-
imacy.
This matters for AI ethics because non-expert reasoning
about governance does not necessarily begin with expert ter-
minology. Participants did not need to use terms such as
“sociotechnical systems” or “algorithmic accountability” to
reason about related issues. Instead, they expressed concerns
about who should disclose evidence, who should be trusted,
how responsibility should be distributed, and what institu-
tional safeguards should be in place. This suggests that in-
teractive narrative may provide one way to bridge every-
day reasoning and AI governance concepts without requir-
ing non-experts to adopt expert language at the outset.
At the same time, the study also indicates that public-
facing tools should be designed with limits in mind. A
short interactive narrative cannot resolve complex gover-
nance questions, replace expert investigation, or represent
all affected stakeholders. It can, however, provide a struc-
tured entry point for examining how non-experts interpret
contested responsibility. In this respect, the prototype com-
plements more formal policy documents, expert reports, and
technical audits by making the interpretive and normative di-
mensions of autonomous driving incidents more accessible
for public discussion.
Limitations and Future Work
This study has several limitations. First, the sample was
small and recruited through convenience sampling, so the
findings should be interpreted as exploratory rather than
generalizable. The quantitative analysis focused on partici-
pants who completed the intended stakeholder-comparison
process, while two participants with limited engagement
were retained as qualitative boundary cases.
Second, the study captured short-term responses imme-
diately after interaction. Future work should use delayed
follow-up or longitudinal designs to examine whether inter-
active narratives based on incidents can sustain engagement
with AI ethics.
Third, the questionnaire items were study-specific ex-
ploratory indicators rather than validated psychometric
scales. Future studies should develop more robust measures
of ethical cognition, responsibility-focused critical thinking,
and multi-perspective reasoning.
Finally, the prototype was based on one autonomous-
driving incident and four selected stakeholder perspectives.
Future work could examine additional incident types, in-
clude a broader range of stakeholders, and test how narrative
complexity and evidence access shape non-experts’ respon-
sibility reasoning.
Overall, our study suggests that multi-perspective inter-
active narrative can support non-expert reflection on con-
tested AI responsibility under uncertainty, rather than forc-
ing a correct ethical answer.
Conclusion
This paper introducedRed Light, Grey Zone, a web-based,
multi-perspective interactive narrative adapted from a real-
world autonomous-driving incident. The study examined
how non-experts reason about ethical ambiguity, stake-
holder conflict, and responsibility attribution in a situ-
ated scenario. Findings suggest that the prototype fore-
grounded governance-relevant concerns, including safety
versus market incentives, responsibility ambiguity, trans-
parency and privacy, and institutional gaps. Exploratory
pre–post results indicated the strongest self-reported shift
in responsibility-focused critical thinking, while qualitative
findings showed that participants compared accounts, evalu-
ated evidence, and often shifted from single-actor blame to-
ward distributed accountability. Overall, the study suggests
that multi-perspective interactive narrative may support non-
expert reflection on responsibility, evidence, and governance
in AI-enabled systems.
Generative AI Use Statement
Generative AI tools were used only to support rapid pro-
totyping of illustrative visual panels. All study design, data
analysis, and manuscript text were authored and verified by
the authors.
References
Beckers, N.; Siebert, L. C.; Bruijnes, M.; et al. 2022. Drivers
of partially automated vehicles are blamed for crashes that
they cannot reasonably avoid.Scientific Reports, 12(1):
16193.
Belman, J.; and Flanagan, M. 2010. Designing games to fos-
ter empathy.International Journal of Cognitive Technology,
15(1): 11.
Buijs-Spanjers, K. R.; Hegge, H. J. A.; Jansen, E.; de Rooij,
S. E.; and de Marcare van der Werf, J. T. 2020. The in-
fluence of a serious game’s narrative on students’ attitudes
and learning experiences regarding delirium: An interview
study.BMC Medical Education, 20: 304.
da Silva, R. L.; and Schrier, K. K. 2025. Learning and Re-
flecting Upon Ethical Frameworks Through Narrative Game
Design.TechTrends.

Goulet-Pelletier, J.-C.; and Cousineau, D. 2018. A review
of effect sizes and their confidence intervals, Part I: The Co-
hen’sd family.The Quantitative Methods for Psychology,
14(4): 242–265.
Kirchmair, L. 2023. How to Regulate Moral Dilemmas In-
volving Self-Driving Cars: The 2021 German Act on Au-
tonomous Driving, the Trolley Problem, and the Search for
a Role Model.German Law Journal, 24(4): 702–726.
Kwak, Y .; Ahn, J.-W.; and Seo, Y . H. 2022. Influence of AI
ethics awareness, attitude, anxiety, and self-efficacy on nurs-
ing students’ behavioral intentions.BMC nursing, 21(1):
267.
Mara, C. A.; and Cribbie, R. A. 2012. Paired-samples tests
of equivalence.Communications in Statistics-Simulation
and Computation, 41(10): 1928–1943.
Naul, E.; and Liu, D. 2020. Why Story Matters: A Review of
Narrative in Serious Games.Journal of Educational Com-
puting Research, 58(3): 687–707.
Ng, Y .-L.; et al. 2024. Understanding Passenger Acceptance
of Autonomous Vehicles through the Prism of the Trolley
Dilemma.International Journal of Human–Computer In-
teraction, 40(9): 2190–2207.
Rhim, J.; Lee, J.-H.; Chen, M.; and Lim, A. 2021. A Deeper
Look at Autonomous Vehicle Ethics: An Integrative Ethical
Decision-Making Framework to Explain Moral Pluralism.
Frontiers in Robotics and AI, 8: 632394.
Stilgoe, J.; and Cohen, T. 2021. Rejecting acceptance: learn-
ing from public dialogue on self-driving vehicles.Science
and Public Policy, 48(6): 849–859.
Stilgoe, J.; et al. 2021. Learning from public dialogue on
self-driving vehicles.Science and Public Policy, 48(6): 849–
859.
Wei, M.; Zhang, P.; Chen, C.; Chen, D.; Zuo, C.; and Meng,
L. 2025. Mapping AI ethics narratives: evidence from Twit-
ter discourse between 2015 and 2022.Humanities and So-
cial Sciences Communications, 12(1): 1–13.
Willig, C.; and Rogers, W. S. 2017.The SAGE handbook of
qualitative research in psychology. Sage.
Zhai, S.; et al. 2024. Not in Control, but Liable? Attributing
Human Responsibility for Fully Automated Car Accidents.
Engineering.
Zhang, Q.; Wallbridge, C. D.; Jones, D. M.; and Morgan,
P. L. 2024. Public perception of autonomous vehicle capa-
bility determines judgment of blame and trust in road traffic
accidents.Transportation research part A: policy and prac-
tice, 179: 103887.
