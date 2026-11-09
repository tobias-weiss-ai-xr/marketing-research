---
title: 'Reflexive Digital Twin Marketing Theory: Governing Algorithmic Marketing Agents Through Reinforcement
  Learning'
url: https://doi.org/10.21203/rs.3.rs-10403290/v1
category: analytics
subcategory: empirical
date: 2026-07
venue: Research Square
authors:
- Atantra Dasgupta
- Kirti Sharma
source: openalex-oa
pdf_url: https://www.researchsquare.com/article/rs-10403290/latest.pdf
pages: 22
chars: 87845
fetched_at: '2026-11-08T17:28:39+00:00'
kb_version: 1
---

# Reflexive Digital Twin Marketing Theory: Governing Algorithmic Marketing Agents Through Reinforcement Learning

Reﬂexive Digital Twin Marketing Theory: Governing Algorithmic Marketing
Agents Through Reinforcement Learning
Atantra Dasgupta 
Management Development Institute
Prof Kirti Sharma 
Management Development Institute
Research Article
Keywords: Digital twin marketing, Algorithmic marketing systems, AI governance in marketing, Reﬂexive marketing theory, Reinforcement learning marketing,
Consumer data and identity, Marketing analytics AI, Ethical AI marketing, Markov decision process marketing, Value alignment algorithms, Predictive
consumer modeling, Sociotechnical marketing systems
Posted Date: July 21st, 2026
DOI: https://doi.org/10.21203/rs.3.rs-10403290/v1
License:   This work is licensed under a Creative Commons Attribution 4.0 International License.   Read Full License
Additional Declarations: The authors declare no competing interests.
Page 1/22

Abstract
Marketing scholarship has been slow to catch up with a marketing reality that now runs largely on algorithms. Recommendation engines shape what
consumers see before they know what they are looking for. Dynamic pricing systems adjust in real time. Personalization engines build behavioral proﬁles
that follow consumers across their entire journey. Existing theory tends to treat these systems either as eﬃciency tools or as sources of ethical risk, but
rarely as the central phenomenon marketing theory needs to explain. This paper develops Reﬂexive Digital Twin Marketing Theory (RDTMT), which reframes
algorithmic marketing as a sociotechnical system that co-evolves with consumers, ﬁrms, and regulators through continuous feedback instead of one-
directional persuasion.
The theory is built empirics-ﬁrst. A PRISMA-ScR scoping review of 742 records (2000–2025) across Web of Science, Scopus, PubMed, and Google Scholar
narrowed to 42 core studies at the intersection of digital twin applications, marketing analytics, and AI governance. A co-occurrence network analysis using
VOSviewer surfaced four convergent clusters (continuous synchronization, adaptive intelligence, reﬂexive governance, and societal co-evolution), which we
use as the empirical basis for three theoretical constructs: Digital Reﬂexivity, Ethical Feedback Elasticity, and the Value Coherence Index. We then formalize
the relationships among these constructs as a Markov Decision Process, translating RDTMT's causal logic into nine reinforcement-learning equations that
specify how algorithmic marketing systems can be evaluated not just for predictive accuracy, but for responsiveness to the people they affect.
RDTMT's contribution is twofold. Theoretically, it gives marketing scholars a vocabulary for treating algorithmic systems as active participants in shaping
consumer identity instead of neutral instruments executing ﬁrm strategy. Practically, the constructs translate into a diagnostic toolkit ﬁrms can use to audit
how reﬂexive, adaptive, and legitimacy-responsive their marketing systems actually are. This is work we see as most valuable for consumers with limited
digital literacy or bargaining power, who bear the highest cost when these systems misrepresent who they are. As a scoping review feeding theory
construction, RDTMT's constructs still need empirical validation across industries and ﬁrm contexts. We treat that as the natural next stage of this research
program rather than a limitation to be explained away.
1. Introduction
Please have a look at courier new font provided for text in article.
Marketing now operates in a new era driven by algorithmic systems that learn, adapt, and respond continuously based on real-time consumer data.
Recommendation engines inﬂuence what consumers encounter before they even realize what they want. Dynamic pricing algorithms adjust in milliseconds.
(Zhou et al., 2025). Predictive personalization engines construct detailed behavioral proﬁles that inﬂuence decisions across the full consumer journey.
(Wang, 2025). These systems aren't just faster versions of the marketing tools that came before them. They amount to a different kind of marketing system
altogether: reﬂexive, self-updating, and embedded in sociotechnical arrangements that extend well beyond any single ﬁrm’s control.
Despite these developments, marketing theory has not kept pace. Core frameworks such as consumer behavior models, relationship marketing, service-
dominant logic, and digital marketing extensions were primarily developed in environments before the rise of algorithms. (Hasan & Mayr, 2026). They view
technology as a tool that implements human-crafted strategies, not as an active participant inﬂuencing consumer identity and market results. (Uzoka, 2020).
When algorithmic systems are addressed, they tend to appear as contextual moderators or ethical risk factors, not as the central theoretical object requiring
explanation. (Rodgers et al., 2023). This leaves marketing theory with a fundamental blind spot: it cannot adequately explain how modern marketing systems
simultaneously construct the consumers they claim to serve, adapt to the feedback those consumers generate, and govern themselves in response to the
social legitimacy pressures they provoke.
Three speciﬁc gaps follow from this blind spot, and each has gone unanswered in the literature for a different reason. First, existing accounts of algorithmic
marketing systems, including recent work that extends marketing-systems theory to nonhuman agents (Commuri & Aggarwal, 2026), treat the algorithm’s
decision authority as the object of study, but stop short of theorizing how that authority is continuously reconstituted through the consumer’s own behavioral
feedback. How consumer identity and algorithmic representation co-produce one another over repeated interaction remains conceptually open. Second, the
marketing ethics literature treats governance as something imposed on algorithmic systems from outside, through compliance rules, audits, or regulation,
not as a property the system itself can be more or less responsive to. There is no construct in the marketing literature for how elastic a system’s behavior is
to the value signals it receives, only whether it complies with predeﬁned rules. Third, no existing framework speciﬁes how legitimacy and commercial
optimization interact formally, instead of leaving them as separate concerns to be traded off in a discussion section. This paper takes up these three gaps
directly, organized around three research questions: RQ1: how do algorithmic marketing systems recursively construct the consumer representations they
act upon, and with what consequence for consumer autonomy? RQ2: what determines whether an algorithmic marketing system’s adaptation to stakeholder
feedback produces accountable behavior rather than entrenching problematic patterns? RQ3: how can value alignment between an algorithmic marketing
system’s objectives and societal expectations be formally speciﬁed as a constraint on the system’s optimization problem, rather than treated as an external
check on its outputs?
This paper answers these questions by developing Reﬂexive Digital Twin Marketing Theory (RDTMT). Conceptually, RDTMT reframes algorithmic marketing
systems as reﬂexive, adaptive, and governance-laden sociotechnical arrangements, addressing RQ1 and RQ2 through two new theoretical constructs, Digital
Reﬂexivity and Ethical Feedback Elasticity, introduced in Section 5. Formally, RDTMT answers RQ3 by introducing Reinforcement Learning (RL) as its
mathematical backbone: we formalize the algorithmic marketing system as a Markov Decision Process (MDP) and derive nine equations that make value
alignment, operationalized as the Value Coherence Index, a constraint on the optimization problem itself rather than an afterthought applied to whatever the
optimization already produced. The paper’s contribution is therefore twofold. Theoretically, it supplies marketing scholarship with constructs and a formal
mechanism for a phenomenon that existing frameworks were not built to explain: algorithmic systems that construct the consumers they serve. Commuri
and Aggarwal (2026) theorize how algorithmic authority redistributes across market actors, RDTMT theorizes the consumer-level and governance-level
Page 2/22

feedback dynamics that determine how that authority is exercised over time, a complementary, non-overlapping contribution we return to in Section 2.4.
Practically, it gives ﬁrms and regulators a diagnostic vocabulary (detailed in Section 7) for auditing systems that are otherwise assessed only on predictive
accuracy.
Figure 1 displays the full RDTMT process map, illustrating the theory’s operational logic from the algorithmic marketing context, through the three core
constructs of Digital Reﬂexivity, Ethical Feedback Elasticity, and Value Coherence Index, to societal outcomes, while highlighting the recursive feedback
pathways that set RDTMT apart from linear causal models.
RDTMT Process Map: Reﬂexive Governance Framework for Algorithmic Consumer Systems
Note
Developed by the authors based on the conceptual framework proposed in this study.
The rest of the paper builds toward that formalization in stages. Section 2 positions RDTMT against the marketing theories it draws on and departs from.
Section 3 lays out the empirics-ﬁrst methodology behind the scoping review. Section 4 reports the four convergent clusters the review surfaced. Section 5
develops the three constructs and nine propositions those clusters motivate, along with the conditions under which the theory does and doesn't apply.
Section 6 turns the theory into the reinforcement-learning system summarized above. Section 7 works through the theoretical, practical, and policy
implications, and Section 8 closes with limitations and a concrete research agenda.
2. Theoretical Background and Positioning
2.1 The Limits of Existing Marketing Theory in Algorithmic Environments
Marketing theory has always evolved in response to technological change, from mass media to relationship marketing and from digital marketing to social
media analytics. (Pascucci et al., 2023). Yet the current wave of algorithmic transformation is different in kind, not just degree. It introduces three theoretical
challenges that existing frameworks are poorly equipped to handle.
The ﬁrst problem is reﬂexive representation. Modern marketing systems don't just react to consumer behavior. They also create representations of
consumers, such as behavioral proﬁles, predictive models, and algorithmic identities, that subsequently inﬂuence and shape the behavior they aim to
understand. (Zuboff, 2019). This is a recursive, constitutive dynamic that lies outside the scope of models treating the consumer as a stable, pre-existing
entity. Service-dominant logic (Vargo & Lusch, 2004) acknowledges co-creation but does not theorize the algorithmic mediation of that co-creation, nor its
governance implications.
The second problem is adaptive governance. When marketing systems learn and self-adapt, the question of who governs them, and how, becomes
theoretically central. Traditional marketing ethics frameworks address compliance and responsibility at the managerial level. (Kamila & Jasrotia, 2023). But in
algorithmic systems, governance is distributed across code, data, platform architectures, and regulatory environments. (Gritsenko & Wood, 2020). Existing
marketing theory lacks conceptual tools for theorizing this distributed, emergent governance.
The third is the problem of societal legitimacy. As algorithmic marketing systems become more pervasive, they increasingly encounter legitimacy pressures
from consumers, regulators, civil society, and media. (Bikowski, 2025). These pressures are not simply risk factors to be managed. They are feedback signals
that shape how systems evolve. (Hastuti et al., 2025). Marketing theory needs a framework that treats legitimacy dynamics as endogenous to the system’s
development, not as external constraints.
2.2 Digital Twins as a Theoretical Lens for Marketing
The digital twin concept originated in engineering and manufacturing (Grieves & Vickers, 2017), where it refers to a computational model that maintains
continuous, bidirectional synchronization with a physical asset, learning from real-time behavior and generating predictions that inform its management.
Over the past decade, digital twin concepts have been extended to healthcare (Menon et al., 2026), smart cities (Zahedi & Khanizad, 2025), and
organizational systems (Ukko et al., 2026). In this paper, we apply the digital twin concept as a theoretical lens for marketing, not as a description of any
speciﬁc technology, but as a conceptual framework for understanding the reﬂexive, adaptive, and governance-laden dynamics of algorithmic consumer
systems. The novelty of RDTMT lies in its use of the digital twin’s relational and governance logic as the theoretical foundation for a new marketing theory.
2.3 Reinforcement Learning as a Bridge Between Theory and Formalism
Reinforcement learning (RL) is a branch of machine learning in which an agent learns to make decisions by interacting with an environment, receiving reward
signals, and updating its policy to maximize cumulative reward over time (Alkam et al., 2025). In marketing contexts, RL algorithms already power
recommendation engines, dynamic pricing systems, and adaptive content delivery (Segbenu et al., 2025), precisely the systems that RDTMT theorizes. Here,
RL serves a different purpose than it does in those applications: rather than a technical backdrop, it becomes the formal language RDTMT is written in.
Figure 3 presents the complete MDP architecture and equation mapping, showing how each RL component corresponds to an RDTMT construct and how all
nine equations interrelate within the Bellman optimization system.
2.4 Positioning RDTMT Within Marketing Theory
RDTMT builds on and extends several existing theoretical traditions. Relationship marketing inherits the emphasis on ongoing, dynamic relationships
between marketing actors. (Albérico & Casaca, 2024). From service-dominant logic (Lusch, 2006), it inherits an emphasis on co-creation and value-in-use.
Page 3/22

Institutional theory (Vellesalu et al., 2023) draws on concepts of legitimacy and isomorphic pressure, with systems theory (Freitas & Guimarães, 2007), and
complexity theory draws on feedback loops, emergence, and adaptive behavior. RDTMT synthesizes these traditions within a digital twin framework,
augmented by a reinforcement learning formalism (Olayemi et al., 2024), to produce a theory speciﬁcally suited to the algorithmic marketing environment.
This kind of borrowing across ﬁelds is itself a recognized route to theoretical advancement in marketing, provided the borrowed elements are integrated into
something that does new explanatory work rather than simply imported wholesale (Varadarajan, 2020); RL is not appended to RDTMT as a computational
add-on but supplies the formal vocabulary the theory is written in, developed fully in Section 6.
The theory closest to RDTMT in both timing and ambition is Commuri and Aggarwal’s (2026) Algorithmic Sovereignty Framework, which extends marketing-
systems theory to nonhuman agents and theorizes how constitutive market authority (the capacity to determine what is visible, transactable, and choosable)
redistributes across human-algorithmic assemblages. The overlap is real: both frameworks treat algorithms as market actors, not as tools, and both draw on
marketing-systems and institutional thinking to do it. The difference is in what each theory is built to explain. Algorithmic Sovereignty operates at the level of
market structure: it asks how authority moves across the system as a whole, tracking ﬁve sovereignty dimensions (cognitive, temporal, informational,
relational, and normative) across the phases of a market’s evolution from human-dominant to hybrid conﬁgurations. RDTMT operates one level down, at the
level of the recursive loop between a single algorithmic system and the consumer it is modeling: it asks how that system’s internal representation of a
consumer feeds back to shape the consumer’s behavior, how responsive the system is to the value signals that behavior generates, and whether the resulting
policy stays coherent with the values it is supposed to serve. Put differently, Algorithmic Sovereignty explains why authority sits where it does across a
market. RDTMT explains what happens inside the loop once an algorithmic system has that authority over a given consumer relationship. The two are
compatible, not competing: a system that Algorithmic Sovereignty would characterize as holding high conﬁguration sovereignty over a market segment is
exactly the kind of system whose Digital Reﬂexivity, Ethical Feedback Elasticity, and Value Coherence Index RDTMT gives researchers the tools to measure.
We treat this as a genuine complementarity here instead of resolving it, since testing how the two frameworks’ constructs relate empirically is itself a natural
extension of both research programs.
Table 1 lays out how RDTMT compares with the main marketing theories that shaped its development.
Table 1
Positioning the Reﬂexive Digital Transformation and Marketing Theory (RDTMT) Relative to Contemporary Marketing Theories
Theory Primary Focus Key Contribution Limitations of Algorithmic
Marketing
RDTMT Extension
Service-Dominant
Logic (Vargo & Lusch,
2004)
Value co-creation Service exchange and
resource integration
Does not explain recursive
algorithmic learning or AI-
driven behavioral
adaptation
Introduces Digital Reﬂexivity to explain how
algorithmic systems actively shape
consumer preferences through continuous
feedback loops.
Consumer Culture
Theory (Arnould &
Thompson, 2005)
Consumer meaning
and identity
Cultural construction
of consumption
Primarily human-centered
and less attentive to
algorithmic mediation
Extends identity formation by modeling
algorithmically generated behavioral
representations that inﬂuence future
consumption.
Dynamic Capabilities
Theory (Teece et al,
1997)
Organizational
adaptation
Sensing, seizing and
transforming
capabilities
Focuses on ﬁrms, not
adaptive algorithmic
systems
Introduces Ethical Feedback Elasticity as an
adaptive governance capability embedded
within algorithmic decision systems.
Adaptive Structuration
Theory (DeSanctis &
Poole, 1994)
Technology–human
interaction
Mutual adaptation
between technology
and users
Does not incorporate
autonomous machine
learning or reinforcement
learning
Extends adaptive structuration through
recursive AI learning, algorithmic adaptation,
and consumer reﬂexivity.
Sociotechnical
Systems Theory (Trist
& Bamforth, 1951)
Joint optimization of
social and technical
systems
Human–technology
interaction
Limited treatment of
autonomous AI
optimization and
algorithmic governance
Positions algorithmic marketing systems as
continuously learning socio-technical
environments inﬂuenced by ethical and
societal feedback.
Institutional Theory
(Suchman, 1995; Scott,
2014)
Legitimacy and
institutional
conformity
Organizational
legitimacy and
governance
Explains legitimacy
outcomes but not
computational value
alignment
Introduces the Value Coherence Index to
operationalize legitimacy by measuring the
alignment between optimization objectives
and stakeholder values.
Relationship
Marketing (Morgan &
Hunt, 1994)
Trust and long-term
relationships
Commitment and
trust between ﬁrms
and customers
Assumes predominantly
human-managed
relationships
Explains how algorithmic responsiveness
(Ethical Feedback Elasticity) inﬂuences trust,
loyalty, and long-term stakeholder
relationships through adaptive governance.
Source
Developed by the authors, synthesizing contemporary marketing theories with the proposed Reﬂexive Digital Twin and Marketing Theory (RDTMT).
2.5 Positioning Within Prior Research: A Summary of Key Studies
Table 2 summarizes ten studies spanning 1998 to 2026 that anticipate, overlap with, or bear directly on RDTMT’s three constructs, deliberately reaching
beyond the recent scoping-review window to show where each gap in Section 1 actually comes from. Read across the rows, a pattern emerges:
personalization research (Blom, 2000; Bleier & Eisenbeiss, 2015) treats the algorithmic system as a ﬁrm-controlled lever, not a co-evolving actor; service and
assemblage theory (Hoffman & Novak, 2018; Huang & Rust, 2021) grants the system agency but does not theorize how that agency reconstitutes the
Page 4/22

consumer it acts on; the ethics-of-algorithms literature (Mittelstadt et al., 2016; Zuboff, 2019) identiﬁes the governance problem but stops at critique instead
of offering a measurable construct. The two most recent entries (Raﬁeian, 2024; Obiegbu & Larsen, 2025) empirically anticipate exactly the autonomy and
responsiveness effects RDTMT formalizes as propositions, without generalizing them into a reusable theoretical vocabulary. No single study in this table
speciﬁes how consumer-level reﬂexivity, system-level responsiveness, and value alignment relate to one another as parts of one causal system. That is the
gap Section 5 closes.
Page 5/22

Table 2
Summary of Prior Research Positioning RDTMT’s Contribution
Study Design Context Focus / IV(s) DV(s) Mediator/Moderator Theoretical
Lens
Key Finding
Bucklin,
Lehmann,
& Little
(1998)
Marketing decision
automation,
conceptual/predictive
Firm decision
processes
(general)
Degree of
automation in
marketing
decisions
— — Marketing
decision-
support
theory
Predicted
marketing wou
shift from
decision suppo
to decision
automation by
2020
Blom
(2000)
Personalization
taxonomy,
conceptual
HCI /
personalized
systems
Type of
personalization
(content,
structure,
presentation)
User perception
of relevance
— HCI design
theory
Distinguished
personalizatio
dimensions bu
treated the
system as a st
tool
Bleier &
Eisenbeiss
(2015)
Field experiment Online retail
advertising
Ad
personalization
depth, timing,
placement
Click-through,
purchase
Privacy concern Persuasion
knowledge
model
Personalizatio
effectiveness
depends on
interplay of
what/when/wh
moderated by
privacy concer
Hoffman
& Novak
(2018)
Conceptual Internet of
Things/consumer
objects
Object agency,
assemblage
structure
Consumer
experience
— Assemblage
theory
Reframes sma
objects as co-
actors in
consumer
experience, no
passive tools
Huang &
Rust
(2021)
Conceptual, typology AI-driven service
encounters
AI task type
(mechanical,
thinking,
feeling)
Service
outcomes,
employment
effects
— Service
marketing
theory
Classiﬁed AI ro
in service but
stopped at tas
substitution, no
consumer co-
construction
Mittelstadt
et al.
(2016)
Conceptual review Algorithmic
decision systems
(cross-domain)
Algorithmic
opacity,
epistemic and
normative
concerns
— — Ethics of
algorithms
Mapped six
ethical concern
types but did n
propose a
construct for
measuring a
system's
responsivenes
them
Zuboff
(2019)
Conceptual / critical
theory
Digital platforms
and surveillance
Behavioral
surplus
extraction
Societal power
asymmetry
— Surveillance
capitalism
Argued platfor
reshape social
norms through
data extraction
societal scale
Note. This table is illustrative of the positioning logic behind RDTMT’s three constructs, not an exhaustive systematic review. The full 42-study scoping-review
protocol are reported in Section 3.
Page 6/22

Study Design Context Focus / IV(s) DV(s) Mediator/Moderator Theoretical
Lens
Key Finding
Raﬁeian
(2024,
working
paper)
Structural/empirical
model
Recommendation
systems
Personalization
accuracy over
time
Consumer
preference
learning,
algorithmic
dependence
Information
advantage
Information
economics
Personalized
recommendati
improves welfa
short-term but
erode
independent
preference
learning long-t
Obiegbu &
Larsen
(2025)
Qualitative, interview-
based
Music streaming
services
Algorithm
personalization
success/failure
Brand loyalty,
depersonalization
Perceived
relationship
breakdown
Consumer-
brand
relationship
theory
Introduces
'depersonaliza
as the felt cost
algorithmic no
responsivenes
Commuri
&
Aggarwal
(2026)
Conceptual Market systems
(cross-industry)
Distribution of
algorithmic
market
authority
Market
outcomes,
conﬁguration
sovereignty
— Marketing-
systems
theory,
exchange
theory
Theorizes how
constitutive
market authori
redistributes
across human-
algorithmic
assemblages v
ﬁve sovereignt
dimensions
Note. This table is illustrative of the positioning logic behind RDTMT’s three constructs, not an exhaustive systematic review. The full 42-study scoping-review
protocol are reported in Section 3.
3. Methodology: Empirics-First Theory Development
Having positioned RDTMT against the theoretical traditions it builds on, we turn now to how the theory itself was built. The three theoretical challenges
identiﬁed in Section 2 (reﬂexive representation, adaptive governance, and societal legitimacy) are not things we deduced from ﬁrst principles. They are
patterns we found by reviewing how the empirical literature already talks about algorithmic marketing systems, which is the approach we describe below.
3.1 Philosophical Orientation
RDTMT is developed using an empirics-ﬁrst approach, in which theoretical constructs and propositions are grounded in patterns identiﬁed through
systematic empirical review, and not deduced from pre-existing theory. (Odoom, 2025) This choice follows guidance on what makes conceptual scholarship
rigorous, as opposed to merely speculative: a conceptual contribution should be judged by whether it organizes and extends what is already known into a
testable structure, not by whether it is deduced from a single parent theory (Vargo & Koskela-Huotari, 2020). This approach is particularly appropriate when
the phenomenon under investigation, algorithmic consumer systems, is rapidly evolving and not yet adequately captured by existing theoretical frameworks.
3.2 Scoping Review Design
We conducted a PRISMA-ScR-guided scoping review (Tricco et al., 2018) to map the empirical landscape of digital twin applications, marketing analytics, and
AI governance. The three review domains were selected because each addresses a distinct dimension of the theoretical problem: the digital twin literature
provides the synchronization and feedback architecture. The marketing analytics literature provides the consumer representation and personalization
dynamics; and the AI governance literature provides the legitimacy and accountability frameworks.
3.3 Search Protocol, Eligibility, and Selection
We searched Web of Science, Scopus, PubMed, and Google Scholar using a structured Boolean search strategy combining terms related to digital twins,
algorithmic marketing, AI personalization, and governance. The search covered January 2000 to December 2025. Articles were included if they: (1)
addressed digital twin concepts, algorithmic marketing systems, or AI governance in consumer-facing contexts; (2) were published in peer-reviewed journals
or conference proceedings; and (3) were available in English. Two researchers independently screened all 742 records, achieving interrater reliability of κ = 
0.84. Full-text review of 187 records identiﬁed 42 articles as the core analytic sample (interrater reliability κ = 0.79 for category assignment).
3.4 Co-occurrence Network Analysis
To identify convergent empirical clusters, we conducted co-occurrence network analysis using VOS-viewer (Jan & Ludo, 2010).A minimum term-frequency
threshold of 5 occurrences and association-strength normalization were applied. Modularity optimization yielded four clusters. A caveat worth stating
plainly: co-occurrence analysis reveals structural patterns, not the substantive meaning of themes, and it establishes no causal relationships on its own.
Page 7/22

(Vocino, 2026).The theoretical interpretation of the clusters is the researchers' work, grounded in full-text coding and guided by the theoretical problem
identiﬁed in Section 2.
4. Scoping Review Findings: Four Convergent Clusters
The scoping review identiﬁed recurring empirical patterns across studies on digital twins, algorithmic marketing, AI governance, and consumer–technology
interactions. Using iterative coding and thematic synthesis, these patterns were organized into four interconnected yet distinct categories.
Clusters: Continuous Synchronization, Adaptive Intelligence, Reﬂexive Governance, and Societal Co-evolution. As depicted in Fig. 2, each cluster contributes
to a speciﬁc element of the Reﬂexive Digital Twin and Marketing Theory (RDTMT) and interacts with the others through recursive feedback. In sum, these
clusters underpin our understanding of how algorithmic systems perpetually build consumer proﬁles, learn and adapt, respond to governance cues, and co-
evolve with societal values and institutional contexts.
4.1 Cluster 1: Continuous Synchronization
Across healthcare digital twins (Saratkar et al., 2025), marketing analytics systems (Lamberton & Stephen, 2016), and customer data platforms, a consistent
pattern emerges: these systems continuously ingest behavioral signals, update consumer models, and generate revised predictions in near real time.
Continuous synchronization produces dynamic, personalized representations that change with consumer behavior and inﬂuence future interactions.
Theoretically, this means consumer identity in algorithmic systems isn't a ﬁxed input for marketing but an ongoing output of the synchronization process.
(Ledro et al., 2025). This motivates the construct of Digital Reﬂexivity.
4.2 Cluster 2: Adaptive Intelligence
Reinforcement learning, multi-armed bandit algorithms, and adaptive recommendation systems can update decision rules based on observed outcomes,
improving predictive accuracy over successive interactions (Tang et al., 2026). This adaptive intelligence is not programmed in advance. It emerges from the
system’s interaction with its environment. The theoretical implication is that modern marketing systems are generating novel behavioral patterns through
adaptive learning, (Nordin & Ravald, 2023) raising fundamental questions about agency, accountability, and governance that existing marketing frameworks
are not designed to address.
4.3 Cluster 3: Reﬂexive Governance
A consistent ﬁnding across AI governance literature (Mittelstadt et al., 2016) and marketing ethics research is that governance of algorithmic systems
cannot be reduced to ex ante rule-setting. It must be understood as an ongoing, adaptive process in which systems respond to legitimacy signals and adjust
their behavior accordingly. This reﬂexive governance dynamic motivates the development of the construct of Ethical Feedback Elasticity.
4.4 Cluster 4: Societal Co-evolution
Research on surveillance capitalism (Zuboff, 2019), consumer privacy (Acquisti, no date), and digital rights (Susser et al., 2018) shows that algorithmic
systems do more than just inﬂuence individual choices. They actively reshape social, economic, and institutional contexts. Through ongoing data collection,
predictive analytics, and behavioral targeting, organizations inﬂuence consumer expectations about privacy, personalization, transparency, and autonomy.
Simultaneously, increased public awareness of data practices has led to stricter regulations, accountability measures, and calls for transparency in
algorithms. (Saura et al., 2024). These shifts are also changing cultural norms as consumers, advocacy groups, policymakers, and companies develop new
understandings of fairness, consent, trust, and digital citizenship. These changes are not one-sided. Societal expectations create new pressures for
organizations to redesign algorithms, update governance, enhance ethical safeguards, and align more closely with stakeholder values. As a result,
algorithmic systems and social environments inﬂuence each other reciprocally, evolving together through ongoing feedback. This co-evolution plays out over
long societal timeframes, which is exactly why a measure of alignment between organizational practices, consumer values, and societal expectations
matters. The proposed Value Coherence Index (VCI) aims to evaluate how well algorithmic marketing systems remain ethically, culturally, and regulatorily
consistent over time, supporting sustainable development. legitimacy, stakeholder trust, and socially responsible digital innovation.
Empirical Foundations of RDTMT: Mapping Four Convergent Clusters to Theoretical Constructs
Note
Developed by authors based on scoping literature review ﬁndings and VOSViewer mappings.
5. Reﬂexive Digital Twin Marketing Theory: Constructs, Relationships, and Propositions
5.1 Theoretical Architecture
RDTMT is built on three core constructs that map onto the empirical clusters identiﬁed in Section 4. These constructs are not independent dimensions of a
taxonomic framework. They are theoretically speciﬁed components of an integrated causal system (see Fig. 3). Digital Reﬂexivity (DR) is the antecedent
mechanism: it describes the process by which algorithmic systems construct and continuously revise consumer representations, generating the feedback
dynamics that the other constructs explain. Ethical Feedback Elasticity (EFE) is the moderating process: it describes how responsive the system is to
governance and legitimacy signals, which determines whether the reﬂexive dynamics of Digital Reﬂexivity (DR) produce adaptive, accountable behavior or
entrench problematic patterns. The Value Coherence Index (VCI) is the integrative outcome: it assesses the degree to which the system’s behavior aligns
with broader societal values, capturing the net result of the interplay between DR and EFE.
Page 8/22

The key theoretical claim is that Digital Reﬂexivity creates the conditions for both beneﬁcial personalization and harmful manipulation, and that Ethical
Feedback Elasticity determines which outcome prevails, with the Value Coherence Index providing the evaluative criterion against which system performance
is assessed.
What ties these three constructs into one theory, rather than three loosely related ideas sharing a name, is a single conceptual move: applying the structure-
agency relationship that structuration theory (Giddens, 1984, as extended to information systems by Jones & Karsten, 2008) describes for human institutions
to an algorithmic one. Structuration theory’s core claim is that social structures are simultaneously the medium and the outcome of the practices they
organize: structures shape agents, but agents also reproduce or transform structures through their own action. Digital Reﬂexivity is what that duality looks
like when the structure in question is an algorithmic representation, not a social institution: the representation shapes consumer behavior, and consumer
behavior in turn reshapes the representation, in a loop with no single origin point. This is precisely why DR cannot be treated as a static antecedent in a
conventional input-output model. It is a relationship, not a variable. The theory then borrows its second move from institutional theory’s account of legitimacy
(Suchman, 1995): organizations retain legitimacy not through one-time compliance but through ongoing responsiveness to the institutional environment
judging them. Ethical Feedback Elasticity names that same responsiveness at the level of an algorithmic system’s policy, and the Value Coherence Index
names the cumulative legitimacy judgment institutional theory says stakeholders form over repeated observation. Read together, the three constructs are not
a taxonomy of separate phenomena but a single structuration-and-legitimacy account of algorithmic marketing systems, applied at three different points in
the same causal chain: DR describes the structure-agency loop itself, EFE describes how responsively that loop is governed, and VCI describes how
legitimate the resulting system looks once judged over time.
5.2 Construct 1: Digital Reﬂexivity (DR)
Deﬁnition
Digital Reﬂexivity refers to the recursive, constitutive process by which algorithmic marketing systems generate behavioral representations of consumers
that feed back to shape the very consumer behaviors they model. The construct extends sociological theorizations of reﬂexivity (Jones & Karsten, 2008) into
algorithmic domains: in digital reﬂexivity, monitoring and adjustment are carried out by the algorithmic system, not by the human actor. This aspect of Digital
Reﬂexivity is what makes algorithmic marketing systems performative. (Vosselman, 2022)The marketing system doesn't just represent consumer
preferences from the outside. It takes an active hand in constituting them.
DR varies along three analytically separable dimensions: Representational Density (the granularity and multidimensionality of algorithmic consumer models);
Temporal Coupling (the latency between behavioral data generation and model updating); and Feedback Visibility (the degree of consumer awareness
regarding how their data shapes their algorithmic treatment). The diagnostic scoring of each dimension on a 1–5 scale is illustrated in Fig. 3, which provides
practitioners with observable organizational indicators for each score level.
The three propositions below follow from a single structurationist premise, not from three separate observations. Giddens’ duality of structure holds that
agents can only reﬂexively monitor and modify a structure they can perceive acting on them. Applied here, the algorithmic representation is the structure, and
the consumer is the agent whose capacity for reﬂexive monitoring depends entirely on whether that structure is visible. This premise generates all three
propositions as a set: if depth and coupling determine how much the structure constrains the agent (P1), and the constraint operates by feeding back into
the agent’s own expressed preferences (P2), then visibility is not a fourth, independent variable. It is the one lever structuration theory says can restore the
agent’s capacity to monitor and resist the structure shaping them (P3).
P1
Higher Digital Reﬂexivity depth, characterized by denser representation and tighter temporal coupling, increases the effectiveness of personalization but
systematically decreases consumer autonomy by constraining the behavioral options the system surfaces.
P2
Digital Reﬂexivity generates performative feedback loops in which algorithmic predictions become self-fulﬁlling by structuring the informational
environments through which consumer preferences are expressed.
P3
Greater feedback visibility moderates the autonomy-reducing effects of Digital Reﬂexivity by enabling consumers to understand, anticipate, and strategically
respond to their algorithmic treatment.
5.3 Construct 2: Ethical Feedback Elasticity (EFE)
Deﬁnition
Ethical Feedback Elasticity measures the degree to which an algorithmic marketing system adjusts its behavior in response to stakeholder value signals,
including consumer complaints, regulatory interventions, civil society pressures, and internal ethical audits. (Filippucci et al., no date). EFE is theoretically
distinct from compliance (adherence to predeﬁned rules) and from accountability (transparency about past actions): EFE is prospective and adaptive,
concerning the system’s capacity to learn from value conﬂicts and modify its behavior accordingly. (Verschraegen, 2026). EFE comprises three interacting
components: Stakeholder Voice Mechanisms, System Adaptability, and Value Alignment Metrics. The distinction between Low (1), Medium (3), and High (5)
Page 9/22

performance on each component is operationalized in Fig. 3, enabling practitioners to diagnose their system’s EFE proﬁle and identify governance gaps
before they escalate into public controversy.
Institutional theory’s account of organizational legitimacy (Suchman, 1995) supplies the logic behind the propositions that follow. Organizations retain
legitimacy not by eliminating stakeholder pressure but by remaining elastic to it, adjusting practices as expectations shift, rather than treating every
complaint as noise to be managed away. EFE is the algorithmic-system analog of that elasticity, which yields three linked predictions, not three unrelated
ones. If elasticity is what legitimacy theory says stakeholders read as responsiveness, it should predict trust directly (P4). But because Digital Reﬂexivity is
what makes a system’s behavior consequential enough for elasticity to matter in the ﬁrst place, the trust effect of reﬂexivity should itself depend on how
elastic the system is. That is why DR and EFE interact rather than operate independently (P5). And because anticipating institutional pressure before it
hardens into regulation is the central adaptive advantage legitimacy theory attributes to elastic organizations, the same logic extends to regulatory
anticipation at the system level (P6).
P4
Higher Ethical Feedback Elasticity is positively associated with consumer trust in algorithmic marketing systems, mediated by perceived responsiveness to
value concerns.
P5: The relationship between Digital Reﬂexivity depth and consumer trust is moderated by Ethical Feedback Elasticity: at high EFE levels, high DR depth is
associated with trust through personalization quality; at low EFE levels, high DR depth is associated with distrust through perceived surveillance.
P6
Ethical Feedback Elasticity signal sensitivity is positively associated with the system’s ability to anticipate regulatory interventions, reducing compliance
costs and reputational risk.
5.4 Construct 3: The Value Coherence Index (VCI)
Deﬁnition
The Value Coherence Index is a multidimensional assessment of how well an algorithmic marketing system’s optimization objectives, behavioral outputs,
and governance arrangements align with the value expectations of its key stakeholder groups, including consumers, regulators, and civil society. VCI extends
the concept of organizational legitimacy in institutional theory (Suchman, 1995) to algorithmic systems. VCI varies along three dimensions: Objective
Speciﬁcation (from narrow, single-metric objectives to holistic, multi-stakeholder objectives); Value Plurality Recognition (the degree to which the system
acknowledges competing stakeholder value commitments); and Temporal Orientation (the time horizon over which system success is evaluated). Table 3
illustrates how common marketing optimization objectives generate potential value conﬂicts and suggests coherence-enhancing strategies. Figure 3
operationalizes VCI scoring across all three dimensions, providing observable indicators for each score level and linking each dimension to its corresponding
RL equation.
Table 3
Optimization Objectives, Value Conﬂicts, and Coherence-Enhancing Strategies
Optimization Objective Potential Value Conﬂicts Coherence-Enhancing Strategies
Maximize engagement Addiction, attention manipulation, compulsive use Engagement quality metrics; time-well-spent design principles
Maximize conversion Pressure tactics, dark patterns, cognitive exploitation Voluntary conversion tracking; post-purchase satisfaction
monitoring
Maximize revenue Pricing exploitation, accessibility barriers, and inequality Fair pricing audits; accessibility provisions for vulnerable
consumers
Maximize eﬃciency Dehumanization, worker displacement, and autonomy
reduction
Human-in-the-loop requirements; worker protection
mechanisms
Maximize
personalization
Surveillance, identity manipulation, ﬁlter traps Transparency logs; consumer proﬁle control; opt-out
mechanisms
Source
Created by the authors, this work is based on a scoping literature review and a theoretical synthesis that combines organizational legitimacy (Suchman,
1995), consumer privacy and surveillance capitalism (Acquisti et al., 2016; Zuboff, 2019), as well as digital rights and AI governance (Susser et al., 2019).
The propositions below extend the same institutional logic one step further, from responsiveness to alignment. Legitimacy theory treats an organization’s
standing with stakeholders as something judged cumulatively, over repeated observation, not as a single compliance event. VCI is what that cumulative
judgment looks like when the observed party is an algorithmic system instead of a ﬁrm. Read this way, the three propositions are stages of one argument
rather than three separate claims. Elasticity should build coherence over time because repeated responsiveness is exactly what cumulative legitimacy
judgments reward, and that effect should be strongest when reﬂexivity is high because a highly reﬂexive system’s choices are more visible and more
consequential to the stakeholders forming that judgment (P7). Because legitimacy judgments are inherently temporal, coherence should show up in
outcomes that are themselves temporal: brand equity and loyalty accumulated over repeated interactions, not any single transaction (P8). And because
Page 10/22

institutional theory’s central prediction is that legitimate organizations face lower-cost, more cooperative relationships with the institutions that could
otherwise sanction them, the same should hold for algorithmic systems judged coherent by regulators (P9).
P7
Value Coherence Index is positively predicted by Ethical Feedback Elasticity, and this relationship is strengthened when Digital Reﬂexivity depth is high.
P8
Value Coherence Index's temporal-coherence dimension is positively associated with long-term brand equity and consumer loyalty, beyond the effects of
personalization quality.
P9
Algorithmic marketing systems with high Value Coherence Index scores are more likely to achieve regulatory co-operation rather than adversarial regulatory
intervention, reducing governance costs and enabling more adaptive innovation.
Table 4 consolidates the nine propositions introduced above, organized by construct and relationship type, to give reviewers and future researchers a single
reference point for RDTMT’s testable claims.
Table 4
Summary of RDTMT Propositions
# Construct(s) Relationship Type Proposition
P1 Digital Reﬂexivity Main effect (trade-off) Higher DR depth, denser representation and tighter temporal coupling, increases the
effectiveness of personalization but systematically reduces consumer autonomy by
narrowing the behavioral options the system surfaces.
P2 Digital Reﬂexivity Mechanism
(performative feedback)
DR generates performative feedback loops in which algorithmic predictions become self-
fulﬁlling by structuring the informational environments through which consumer
preferences are expressed.
P3 Digital Reﬂexivity Moderation (boundary
condition on P1–P2)
Greater feedback visibility moderates the autonomy-reducing effects of DR by letting
consumers understand, anticipate, and strategically respond to their algorithmic treatment.
P4 Ethical Feedback
Elasticity
Mediation Higher EFE is positively associated with consumer trust in algorithmic marketing systems,
mediated by perceived responsiveness to value concerns.
P5 Digital Reﬂexivity ×
Ethical Feedback
Elasticity
Moderation (interaction) EFE moderates the DR–trust relationship: at high EFE, high DR depth builds trust through
personalization quality; at low EFE, high DR depth breeds distrust through perceived
surveillance.
P6 Ethical Feedback
Elasticity
Main effect EFE signal sensitivity is positively associated with a system's ability to anticipate regulatory
interventions, reducing compliance costs and reputational risk.
P7 Value Coherence Index
←  EFE, DR
Main effect (moderated) VCI is positively predicted by EFE, and this relationship strengthens when DR depth is high.
P8 Value Coherence Index Main effect VCI's temporal-coherence dimension is positively associated with long-term brand equity
and consumer loyalty, beyond the effects of personalization quality.
P9 Value Coherence Index Main effect Algorithmic marketing systems with high VCI scores are more likely to achieve regulatory
cooperation rather than adversarial intervention, reducing governance costs and enabling
more adaptive innovation.
Note. DR = Digital Reﬂexivity; EFE = Ethical Feedback Elasticity; VCI = Value Coherence Index. Arrows ( ← ) denote a hypothesized predictor relationship; ×
denotes an interaction term.
5.5 The Integrated RDTMT System: Virtuous and Vicious Cycles
The three constructs form an interconnected theoretical framework. Digital Reﬂexivity drives the recursive feedback dynamics characteristic of algorithmic
marketing systems, which both create value through accurate, responsive personalization and pose risks like manipulation, autonomy erosion, and
surveillance. Ethical Feedback Elasticity (EFE) inﬂuences how the system manages this duality. The Value Coherence Index (VCI) measures systemic
legitimacy. This isn’t a linear cause-and-effect relationship. It’s a recursive system in which high VCI enables deeper Digital Reﬂexivity (DR) without legitimacy
issues, whereas low VCI creates pressures that constrain DR and require more EFE investment. The virtuous cycle (High EFE →  High VCI →  Ongoing
Consumer Trust →  Facilitating Deeper DR) and vicious cycle (Low EFE →  Declining VCI →  Legitimacy Crisis →  Contraction of DR) are illustrated in Fig. 3,
which helps practitioners identify their current pathway and prioritize actions. Figure 3 also includes a 9-axis radar chart, three construct-speciﬁc checklists
(DR, EFE, VCI), and the Action Priority Matrix, serving as this paper’s main practical resource.
RDTMT Practitioner Diagnostic Toolkit: Assessing Digital Reﬂexivity, Ethical Feedback Elasticity, and Value Coherence
Note
The authors developed this through theoretical synthesis and operationalization of the RDTMT constructs, grounded in the systematic literature review and
the conceptual framework outlined in this study.
Page 11/22

5.6 Boundary Conditions
Like any theory built around a speciﬁc mechanism, RDTMT has a domain where it applies well and a domain where it doesn’t. The mechanism at its core is
continuous, high-frequency synchronization between an algorithmic system and a consumer—Digital Reﬂexivity presumes the system sees enough
behavioral signal, often enough, to keep updating its representation of the person it’s modeling. That premise breaks down for infrequent, high-involvement
purchases such as homes, vehicles, or major medical decisions, where a single consumer generates too few interactions for the reﬂexive loop DR describes
to take hold. In these categories, marketing analytics still inform strategy, but the systems in question rarely reach the update frequency RDTMT assumes,
and the theory’s claims should be read as inapplicable, not merely weaker.
A second boundary sits at the human-in-the-loop line. RDTMT theorizes a direct algorithmic feedback loop between system and consumer. In B2B contexts
and other settings, where a human decision-maker sits between the algorithm’s output and the outcome—a sales representative approving a
recommendation, a procurement oﬃcer overriding a pricing suggestion—that loop is interrupted. The system may still learn, but what it learns from is the
human intermediary’s decisions, not the end consumer’s behavior directly, which changes what Digital Reﬂexivity is measuring and likely weakens the DR-to-
trust pathways the propositions describe.
Third, Ethical Feedback Elasticity assumes there’s somewhere for a value signal to go—a regulator, an advocacy group, a functioning complaints channel—
that the system can register and respond to. In markets with thin AI-governance infrastructure or weak consumer-advocacy institutions, that stakeholder-
voice mechanism may simply not exist yet, which doesn’t make EFE zero so much as unmeasurable in the way the construct assumes. RDTMT is silent on
what happens to reﬂexive governance where the institutions it presupposes haven’t developed.
Finally, the MDP formalization assumes a state representation rich enough to support policy learning. Small ﬁrms, new product launches, and other cold-start
settings generate too little behavioral data for the transition dynamics in Eq. 2 to be meaningfully estimated, and RDTMT’s claims about Digital Reﬂexivity
depth presuppose exactly the data density these settings lack. Outside algorithmically mediated marketing altogether—mass media, print, and other
channels with no behavioral feedback loop—the theory simply doesn’t apply; RDTMT is a theory of algorithmic marketing systems, not of marketing in
general.
Within that scope, the constructs and propositions above are stated in ordinary language. The next section restates them mathematically, which is what
turns "higher DR depth reduces autonomy" from a claim you either ﬁnd plausible or don't into a claim with a speciﬁc quantity attached to it that a simulation
or a ﬁeld study could actually estimate.
6. Reinforcement Learning Formalization of RDTMT
6.1 Rationale for Formal Speciﬁcation
Formalizing RDTMT in the language of reinforcement learning serves three purposes. First, it puts the theory's constructs in the same mathematical
language as the systems it describes, rather than describing algorithmic marketing from outside the framework those systems actually run on. Second, it
generates mathematically precise predictions that can be evaluated through simulation and ﬁeld experiments. Third, it enables RDTMT to speak directly to
the growing community of marketing researchers and practitioners who deploy RL-based systems and need theoretical frameworks that match the
mathematical sophistication of their tools. Figure 4 presents the complete MDP architecture, showing the three-actor system (Consumer, Marketing System,
Reward Environment), all nine equations in their relational context, and the Digital Reﬂexivity feedback loop that distinguishes RDTMT from standard RL
formulations. Figure 4 should be read alongside the verbal formalization below: the ﬁgure provides the architectural overview, while the text provides precise
mathematical speciﬁcation.
6.2 The Algorithmic Marketing System as a Markov Decision Process
To formalize the dynamic mechanisms underpinning the Reﬂexive Digital Twin and Marketing Theory (RDTMT), a Reinforcement Learning (RL) framework
based on a Markov Decision Process (MDP) is employed. (Adawadkar & Kulkarni, 2022) As illustrated in Fig. 4, the model conceptualizes interactions among
three interconnected actors—the consumer, the marketing system, and the broader reward environment—through recursive feedback cycles that inﬂuence
decision-making and long-term outcomes. The framework integrates the constructs of Digital Reﬂexivity (DR), Ethical Feedback Elasticity (EFE), and Value
Coherence Index (VCI) into a mathematically grounded architecture that links theoretical propositions to a set of nine reinforcement learning equations.
Within this framework, a Markov Decision Process is formally deﬁned as a tuple , where represents the state space (the set of all
possible consumer states), denotes the action space (the set of all possible marketing interventions), is the transition function
describing the probability of moving from state to state after action , is the reward function specifying the immediate reward associated with
taking action in state , and is the discount factor reﬂecting the relative importance of future rewards compared with immediate rewards. The
objective of the system is to learn an optimal policy, , that maximizes the expected cumulative discounted reward while simultaneously
accounting for ethical constraints, value alignment, and long-term societal consequences. What this formalization captures, in plain terms, is how a
consumer's awareness, a system's ethical responsiveness, and a system's value coherence all evolve together through repeated interaction, rather than being
ﬁxed properties assumed at the outset.
Standard RL formulations model a single agent acting in a single environment. RDTMT departs from that setup by splitting the environment into two distinct
parts: the Marketing System, which is the agent being optimized, and the Reward Environment, which represents the broader societal, regulatory, and
reputational consequences of the system's actions—consequences that unfold on a slower timescale than any single consumer interaction and that a
standard two-party RL model has no place to put. This three-actor structure is not a modeling convenience. It is where Ethical Feedback Elasticity and the
(S, A, P , R, γ ) S−
A− P − (s′ ∣ s, a)
s s′ a R(s, a)
a s γ ∈ [0,1]
π : S → A
Page 12/22

Value Coherence Index actually live. Without a Reward Environment distinct from the immediate transaction, there is no channel through which regulatory
pressure or reputational cost could ever enter the optimization problem, and EFE and VCI would have nothing to formalize.
Vπ(s) = Eπ [ Σ_{t = 0}^{∞} γ^t R(s_t, a_t) | s_0 = s ] (Eq. 1)
6.3 Formalizing Digital Reﬂexivity
Digital Reﬂexivity is formalized as the recursive mapping between the consumer’s behavioral state and the system’s consumer model. Let s_t denote the
consumer’s true behavioral state at time t, and let ś_t denote the system’s internal representation of that state. Digital Reﬂexivity depth is captured by the
recursive update:
ś_{t + 1} = f_θ(s_t), s_{t + 1} = g(s_t, π(ś_t), ε_t) (Eq. 2)
Digital Reﬂexivity depth is measured by the Jacobian norm:
DR_depth = || ∂s_{t + 1} / ∂ś_t || (Eq. 3)
This is the quantity Proposition 1 is actually about. A larger DR_depth means the consumer's next state is more sensitive to the system's internal
representation of them than to their own prior state—in plain terms, the system's model of the person is doing more of the work of determining what happens
next than the person's own behavior is. That is precisely the sense in which higher Digital Reﬂexivity narrows the behavioral options a consumer effectively
has available, even though nothing about the interface has visibly changed.
Temporal coupling is captured by the rate of update of f_θ:
DR_speed = || dθ/dt || = || α · ∇ _θ L(θ) || (Eq. 4)
6.4 Formalizing Ethical Feedback Elasticity
Let v_t ∈  ℝ ^k denote a vector of stakeholder value signals at time t. The system’s reward function is extended to incorporate these signals:
R_EFE(s, a, v_t) = R(s, a) - λ · D(v_t, v_0) (Eq. 5)
Ethical Feedback Elasticity is deﬁned as the partial derivative of the system’s optimal policy with respect to the ethical penalty:
EFE = - ∂π*(s | v_t) / ∂[λ · D(v_t, v_0)] (Eq. 6)
6.5 Formalizing the Value Coherence Index
Let W: S × A →  ℝ  denote the social welfare function. VCI is deﬁned as the cosine similarity between the gradient of the system’s reward function and the
gradient of the social welfare function:
VCI = [ ∇ _{a} R(s,a) · ∇ _{a} W(s,a)] / [|| ∇ _{a} R(s,a)|| · || ∇ _{a} W(s,a)||] (Eq. 7)
where VCI ∈  [-1, 1]. A VCI of + 1 indicates perfect alignment between the system’s optimization direction and the social welfare gradient. A VCI of 0 indicates
orthogonality. A VCI of -1 indicates perfect misalignment.
6.6 The Integrated RL System: The RDTMT Bellman Equation
The three formalizations are integrated into a uniﬁed constrained optimization problem:
V*(s, v_t) = max_{a ∈  A} { R_EFE(s, a, v_t) + γ ∑_{s'} P(s'|s,a) V*(s', v_{t + 1}) } (Eq. 8)
subject to the governance constraint:
VCI(π*) ≥ VCI_min (Eq. 9)
where VCI_min is a minimum value coherence threshold speciﬁed by the governance architecture. This constrained optimization problem formalizes the core
theoretical claim of RDTMT: that the optimal policy for an algorithmic marketing system is not one that maximizes narrow commercial reward, but one that
maximizes reward subject to the constraint that the system’s behavior remains coherent with societal values.
It is worth being explicit about how these equations connect back to the nine propositions in Section 5, since the formalism is meant to make those claims
testable rather than to stand on its own. Equations 2–4 formalize Digital Reﬂexivity and are what P1–P3 are claims about: P1's autonomy trade-off is a claim
about DR_depth (Eq. 3), P2's performative-feedback claim is what the recursive update in Eq. 2 describes mechanically, and P3's claim about feedback
visibility as a moderator implies that consumers' access to ś_t itself should attenuate the DR_depth–autonomy relationship. Equations 5–6 formalize Ethical
Feedback Elasticity and correspond to P4–P6: EFE as deﬁned in Eq. 6 is the sensitivity term that P4 and P6 treat as a predictor, and P5's moderation claim
amounts to an interaction between EFE and DR_depth that a full test would need to estimate jointly rather than in the two equations separately. Eq. 7
formalizes the Value Coherence Index that P7–P9 are about, and the governance constraint in Eq. 9 is the formal version of the claim, made throughout
Section 7, that a policy can be commercially optimal and still be governance-infeasible if it fails to clear VCI_min. Reading the equations without this mapping
risks treating them as decorative. Reading them against Table 4 is how a reviewer—or a future author running the simulation studies proposed in Section 8—
would actually use them to test RDTMT.
Page 13/22

Reinforcement Learning in RDTMT: MDP Architecture and Equation Mapping
Note
Developed by the authors based on the proposed Reﬂexive Digital Transformation and Marketing Theory (RDTMT), integrating reinforcement learning theory
(Sutton & Barto, 2018), Markov Decision Process principles (Puterman, 1994).
6.7 Summary: RDTMT Equations and Their Theoretical Interpretations
Table 5 summarises all nine equations, mapping each to its RDTMT construct and theoretical interpretation. Figure 4 presents these equations in their MDP
architectural context, showing the three-actor cycle (Consumer, Marketing System, Reward Environment) and the Digital Reﬂexivity self-reinforcing loop as a
dashed arc on the consumer node. Together, Table 5 and Fig. 4 provide the complete formal speciﬁcation of RDTMT. Practitioners and researchers wishing to
implement the RDTMT MDP computationally should use Fig. 4 as the architectural blueprint and the equations below as the precise mathematical
speciﬁcation.
Table 5
RDTMT Reinforcement Learning Equations and Theoretical Interpretations
Equation Formula RDTMT Construct Theoretical Interpretation
Eq. 1 Vπ(s) = E[Σ γ^t R(s_t, a_t)] MDP Baseline Cumulative discounted reward under policy π
Eq. 2 ś_{t + 1} = f_θ(s_t); s_{t + 1} = g(s_t, π(ś_t), ε_t) Digital Reﬂexivity Consumer state and representation co-evolve
recursively
Eq. 3 DR_depth = ||∂s_{t + 1}/∂ś_t|| Digital Reﬂexivity — Depth Constitutive inﬂuence of model on consumer behavior
Eq. 4 DR_speed = ||α · ∇ _θ L(θ)|| Digital Reﬂexivity — Speed Rate of representation updating: temporal coupling
Eq. 5 R_EFE = R(s,a) - λ·D(v_t,v_0) Ethical Feedback
Elasticity
Reward penalized by divergence from the value baseline
Eq. 6 EFE = -∂π*/∂[λ·D(v_t,v_0)] Ethical Feedback
Elasticity
Policy sensitivity to ethical signal: governance elasticity
Eq. 7 VCI = [ ∇ _a R· ∇ _a W]/[|| ∇ _a R|| || ∇ _a W||] Value Coherence Index Cosine alignment of commercial and welfare objectives
Eq. 8 V*(s,v_t) = max_a{R_EFE + γΣP(s'|s,a)V*(s',v_{t + 
1})}
Integrated RDTMT Bellman equation: full system optimization
Eq. 9 VCI(π*) ≥ VCI_min Governance Constraint Value coherence ﬂoor on all policy solutions
Source: Developed by the authors through the integration of reinforcement learning, Markov Decision Processes, and algorithmic governance.
6.8 A Worked Illustration
A short example makes the equations concrete. Consider a music-streaming recommendation engine deciding what to queue next for a listener whose
recent history is mostly calm, low-tempo evening listening. The consumer’s true state, s_t, is that listening pattern. The system’s internal representation, ś_t,
is whatever proﬁle the recommender has built from past plays. Suppose the system has learned that faster, more rhythmically intense tracks hold attention
longer and generate more completed plays—a defensible engagement objective on its own. Applying Eq. 2, the system’s next recommendation is a function
of ś_t, not of s_t directly, so if ś_t has drifted toward “this listener responds to higher-tempo content” faster than the listener’s actual taste has changed, the
recommendation queue will nudge the listener toward that content regardless of whether it reﬂects what they’d have chosen unprompted. A high DR_depth in
Eq. 3 is exactly this: the queue is being driven more by the model’s belief about the listener than by the listener’s own prior state.
Now suppose enough listeners complain that the app is pushing them away from music they came to hear—a stakeholder value signal, v_t, in Eq. 5. A system
with high Ethical Feedback Elasticity treats that complaint volume as a cost, D(v_t, v_0), and adjusts its policy to weight completed plays less and stated
preference more. A system with EFE near zero keeps optimizing for engagement regardless of the complaints, because λ in Eq. 5 is small and the penalty
barely moves the reward. Eq. 6 is the difference between these two systems stated as a single number: how much does the optimal policy actually shift
when the ethical penalty tightens.
The Value Coherence Index in Eq. 7 asks a different question of the same scenario: does the direction the system is optimizing in—more engagement, more
completed plays—point the same way as what would actually serve the listener’s stated interest in calm, low-tempo music? If the two gradients point in
similar directions, VCI is close to + 1 and the engagement objective and listener welfare happen to coincide. If the system is optimizing for engagement
speciﬁcally by working against stated preference—the pattern the complaints suggest—the gradients diverge and VCI moves toward 0 or negative. Eq. 9’s
governance constraint is what would stop this in practice: a platform that had committed to VCI_min ≈ 0.3, say, would have to reject any policy that pushed
VCI below that ﬂoor, even if that policy scored higher on raw engagement. That is the sense in which RDTMT treats value coherence as a constraint on the
optimization problem, not an afterthought applied to whatever the optimization already produced.
7. Discussion
Having formalized RDTMT as a constrained optimization problem, we step back from the equations to ask what the theory contributes, what it means for
people running these systems day to day, and what it implies for the regulators trying to govern them.
Page 14/22

7.1 Theoretical Contributions to Marketing Scholarship
RDTMT makes ﬁve primary theoretical contributions. First, it introduces a reﬂexive governance architecture for marketing theory, reconceptualizing
governance as an endogenous, adaptive process that is constitutive of how marketing systems develop and legitimize themselves. Second, it speciﬁes the
constitutive role of algorithmic representation in consumer identity formation through the construct of Digital Reﬂexivity, contributing to consumer culture
theory (Arnould & Thompson, 2005) and digital consumer behavior research. Third, RDTMT provides an integrated theoretical system with formally speciﬁed
relationships: the RL formalization demonstrates that the theory’s constructs correspond to mathematically distinct and interrelated quantities that generate
precise, testable predictions. Fourth, RDTMT bridges marketing theory and computational modeling, enabling simulation studies that test its propositions
using the RDTMT MDP. Fifth, RDTMT integrates critical and managerial perspectives within a single framework.
7.2 Implications for Marketing Practice
RDTMT offers practitioners a structured diagnostic toolkit for assessing their marketing systems—formalized in Fig. 3—which provides a 9-axis radar chart
and three detailed scoring checklists (one per construct). Assessing Digital Reﬂexivity on the radar involves scoring Representational Density, Temporal
Coupling, and Feedback Visibility on a 1–5 scale using the provided observable organizational indicators. Assessing Ethical Feedback Elasticity requires
scoring Stakeholder Voice Mechanisms, System Adaptability, and Value Alignment Metrics—each differentiated into Low (reactive only), Medium (proactive
auditing), and High (anticipatory simulation) performance levels. Assessing Value Coherence requires scoring Objective Speciﬁcation, Value Plurality
Recognition, and Temporal Orientation. The Action Priority Matrix at the base of Fig. 3 translates low scores into speciﬁc remediation steps, enabling
practitioners to move from diagnosis to governance action without requiring specialist RL expertise. Firms that invest in high EFE and sustained VCI may
develop trustworthy personalization as a competitive differentiator (P4, P8, P9).
Beyond its theoretical contribution, RDTMT is intended to be usable: each construct translates into a concrete audit question a marketing organization can
act on today.
Digital Reﬂexivity points a CMO toward a concrete audit question: how much does the ﬁrm's own predictive model of a customer now determine what that
customer sees, versus reﬂecting what they have actually done? A high-reﬂexivity system is not inherently a problem, but a ﬁrm that cannot answer this
question has no way of knowing whether its personalization engine has started manufacturing the behavior it claims to predict.
Ethical Feedback Elasticity translates into a governance decision that most ﬁrms currently handle on an ad hoc basis: how quickly, and through what channel,
does customer pushback—a complaint, an opt-out spike, a public callout—change model behavior, instead of merely triggering a support ticket? Firms with
low elasticity can look healthy on their dashboards right up until a legitimacy crisis hits, because the system has no built-in mechanism for updating on social
signal, only on conversion signal. We regard this as a board-level risk question as much as a data-science one.
The Value Coherence Index gives brand and marketing-operations teams a metric they do not currently have: a way to check whether a personalization
system's optimization target (engagement, conversion, lifetime value) still aligns with the values the brand claims to hold, particularly for the customers with
the least power to contest a poor algorithmic decision. In practice, this looks like adding a coherence check to the same review cycle in which ﬁrms already
audit models for bias or accuracy—not a new department, but a new question asked of an existing one.
Taken together, the three constructs offer a lighter-weight alternative to compliance-driven AI ethics checklists: rather than asking whether the ﬁrm followed
the rules, they ask whether the system remains responsive to the people it is modeling—a question CMOs are arguably better positioned to answer than legal
or compliance teams alone.
7.3 Implications for Policy and Regulation
RDTMT has several implications for regulatory approaches to algorithmic marketing. Transparency mandates are necessary but insuﬃcient: transparency
about what data is collected does not address the reﬂexive feedback dynamics (formalized in Equations 2–4) through which consumer states are
continuously reshaped. The EFE formalization (Equations 5–6) suggests that effective regulation should require ﬁrms to demonstrate measurable EFE—that
their systems’ policies change in response to ethical signals. The VCI constraint (Eq. 9) provides a formal basis for minimum-value coherence requirements:
regulators could specify VCI_min thresholds that marketing systems must maintain, with these thresholds audited via the gradient alignment analysis
speciﬁed in Eq. 7.
8. Conclusions, Limitations, and Future Research
8.1 Conclusions
Marketing has entered an algorithmic era that has outpaced the conceptual frameworks available to scholars and practitioners. This paper has developed
Reﬂexive Digital Twin Marketing Theory (RDTMT) as a response to that conceptual gap. Drawing on a rigorous scoping review of 42 studies, we identiﬁed
four convergent empirical patterns and developed three theoretically grounded constructs—Digital Reﬂexivity, Ethical Feedback Elasticity, and the Value
Coherence Index. We then formalized these constructs within a reinforcement learning framework, deriving nine equations that give the theory mathematical
precision and testability.
Collectively, Figs. 1–4 provide a comprehensive representation of RDTMT, spanning theoretical architecture, empirical foundations, computational
formalization, and practical application. Figure 1 maps the theory's causal process, Fig. 2 demonstrates its empirical derivation from the scoping review,
Fig. 3 translates the framework into a practitioner-oriented diagnostic instrument, and Fig. 4 formalizes its recursive dynamics through reinforcement
learning equations. Together, these ﬁgures illustrate how algorithmic systems, consumers, organizations, and societal institutions co-evolve through
Page 15/22

recursive feedback mechanisms. In doing so, RDTMT addresses a critical gap in marketing theory by providing a framework that explains reﬂexive, adaptive,
and governance-sensitive algorithmic systems while offering tools for empirical investigation and managerial implementation.
8.2 Limitations
RDTMT’s constructs require empirical operationalization and psychometric validation. The RL formalization involves simplifying assumptions, most notably
the Markov property, which may be violated in practice when consumer behavior is path dependent. The scoping review is bounded by the selected
databases and search period. The social welfare function W(s, a) used in the VCI formalization requires empirical speciﬁcation, and determining appropriate
weights for the value expectations of different stakeholder groups is itself a contested normative question.
8.3 Directions for Future Research
We suggest six directions. First, computational simulation studies should implement the RDTMT MDP and test the nine propositions by varying DR-depth,
EFE, and VCI parameters. Second, experimental studies could manipulate EFE by varying the ethical penalty λ within controlled recommendation-system
environments to test P4 and P5. Third, measurement instrument development should operationalize all nine radar dimensions as survey and behavioral
measures. Fourth, longitudinal studies should track the evolution of VCI over the life cycle of speciﬁc algorithmic marketing systems. Fifth, cross-cultural
comparative research should examine how RDTMT dynamics vary across regulatory environments. Sixth, extensions of the RL formalization should explore
non-Markovian consumer dynamics, multi-agent settings, and the role of generative AI in amplifying or disrupting the DR-EFE-VCI system.
Declarations
Funding
This research received no speciﬁc grant from any funding agency in the public, commercial, or not-for-proﬁt sectors.
Competing Interests
The authors declare no competing ﬁnancial or non-ﬁnancial interests that could have inﬂuenced the work reported in this paper.
Ethical Approval
This study is based on a systematic/scoping review of published literature and theoretical development. It did not involve human participants, human
biological material, animals, or identiﬁable personal data. Consequently, ethical approval was not required under the policies of the authors' institution.
Informed Consent
Not applicable. This study did not involve human participants or the collection of primary data.
Data Availability Statement
No primary datasets were generated or analysed during this study. All materials analysed are derived from publicly available scholarly publications cited in
the manuscript. Supplementary materials, including the PRISMA-ScR checklist and supporting documentation, are available in the designated repository (or
as supplementary ﬁles accompanying the manuscript).
Author Contributions
All authors contributed substantially to the conception and design of the study. The authors jointly conducted the literature review, theoretical development,
conceptual modeling, interpretation of ﬁndings, manuscript preparation, and critical revision of the article. All authors reviewed and approved the ﬁnal version
of the manuscript and agree to be accountable for all aspects of the work.
AI-Assisted Technologies Statement
The authors used artiﬁcial intelligence (AI)-assisted language support during the preparation of this manuscript to improve readability, grammar, and
presentation. All theoretical development, literature synthesis, mathematical formulations, interpretation of ﬁndings, and ﬁnal editorial decisions were
undertaken by the authors, who accept full responsibility for the accuracy, originality, and integrity of the work.
Consent for Publication
All authors have reviewed and approved the ﬁnal manuscript and consent to its submission for publication.
Acknowledgements
The authors have no acknowledgments to declare.
Research Transparency Statement
The authors followed the PRISMA Extension for Scoping Reviews (PRISMA-ScR) reporting guidelines in conducting and reporting the literature review. The
completed PRISMA-ScR checklist is provided as supplementary material. 
Page 16/22

Originality Statement
The authors conﬁrm that this manuscript is original, has not been published previously, and is not under consideration for publication elsewhere. All sources
have been appropriately acknowledged, and the manuscript complies with the publication ethics standards of the Journal of the Academy of Marketing
Science and Springer Nature.
References
1. Acquisti A (no date) The Economics of Privacy at a Crossroads, pp. 21–71
2. Adawadkar AMK, Kulkarni N (2022) Cyber-security and reinforcement learning — A brief survey, Engineering Applications of Artiﬁcial Intelligence, 114, p.
105116. Available at: https://doi.org/https://doi.org/10.1016/j.engappai.2022.105116
3. Albérico R, Casaca J (2024) Relationship Marketing and Customer Retention - A Systematic Literature Review, Studies in Business and Economics, 18,
pp. 44–66. Available at: https://doi.org/10.2478/sbe-2023-0044
4. Alkam T, Van Benschoten AH, Tarshizi E (2025) Reinforcement learning in artiﬁcial intelligence and neurobiology, Neuroscience Informatics, 5(3), p.
100220. Available at: https://doi.org/https://doi.org/10.1016/j.neuri.2025.100220
5. Arnould EJ, Thompson CJ (2005) Consumer Culture Theory (CCT): Twenty Years of Research, Journal of Consumer Research, 31(4), pp. 868–882.
Available at: https://doi.org/10.1086/426626
6. Bikowski L (2025) Consumer Responses to Algorithmic Marketing Synthesis of Evidence and a Guiding Framework, SSRN Electronic Journal, 13, pp. 19–
30. Available at: https://doi.org/10.2139/ssrn.6424758
7. Filippucci F, no date) THE IMPACT OF ARTIFICIAL INTELLIGENCE ON PRODUCTIVITY, DISTRIBUTION AND GROWTH KEY MECHANISMS, INITIAL
EVIDENCE AND POLICY CHALLENGES OECD ARTIFICIAL (The impact of Artiﬁcial Intelligence on productivity, distribution and growth : Key mechanisms,
initial evidence and policy challenges, (1)
8. Freitas C, Guimarães T (2007) Isomorphism, institutionalization and legitimacy: operational auditing at the court of auditors, Revista de Administração
Contemporânea, 11, pp. 153–175. Available at: https://doi.org/10.1590/S1415-65552007000500008
9. Grieves M, Vickers J (2017) Digital Twin: Mitigating Unpredictable, Undesirable Emergent Behavior in Complex Systems, in, pp. 85–113. Available at:
https://doi.org/10.1007/978-3-319-38756-7_4
10. Gritsenko D, Wood M (2020) Algorithmic governance: A modes of governance approach, Regulation & Governance, 16. Available at:
https://doi.org/10.1111/rego.12367
11. Hasan S, Mayr A (2026) Consumer Trust in Digital Marketing: A Systematic Literature Review and Conceptual Framework, Global Insights in
Management and Economic Research, 2, pp. 23–34. Available at: https://doi.org/10.53905/Gimer.v2i01.04
12. Hastuti H et al (2025) Algorithmic inﬂuence and media legitimacy: a systematic review of social media’s impact on news production, Frontiers in
Communication, 10. Available at: https://doi.org/10.3389/fcomm.2025.1667471
13. Jan N, Ludo VE (2010) Software survey : VOSviewer, a computer program for bibliometric mapping, pp. 523–538. Available at:
https://doi.org/10.1007/s11192-009-0146-3
14. Jones M, Karsten H (2008) Giddens’s Structuration Theory and Information Systems Research, Management Information Systems Quarterly - MISQ, 32.
Available at: https://doi.org/10.2307/25148831
15. Kamila MK, Jasrotia SS (2023) Ethics and marketing responsibility: A bibliometric analysis and literature review, Asia Paciﬁc Management Review, 28(4),
pp. 567–583. Available at: https://doi.org/https://doi.org/10.1016/j.apmrv.2023.04.002
16. Lamberton C, Stephen A (2016) A Thematic Exploration of Digital, Social Media, and Mobile Marketing Research’s Evolution from 2000 to 2015 and an
Agenda for Future Research, Journal of Marketing, 80. Available at: https://doi.org/10.1509/jm.15.0415
17. Ledro C et al (2025) Artiﬁcial intelligence in customer relationship management: A systematic framework for a successful integration, Journal of
Business Research, 199, p. 115531. Available at: https://doi.org/https://doi.org/10.1016/j.jbusres.2025.115531
18. Menon G et al (2026) Digital twin technologies in medicine: The innovations, barriers, and future directions, Intelligent Hospital, 2(1), p. 100043. Available
at: https://doi.org/https://doi.org/10.1016/j.inhs.2025.100043
19. Mittelstadt BD et al (2016) The ethics of algorithms: Mapping the debate, Big Data \& Society, 3(2), p. 2053951716679679. Available at:
https://doi.org/10.1177/2053951716679679
20. Nordin F, Ravald A (2023) The making of marketing decisions in modern marketing environments, Journal of Business Research, 162, p. 113872.
Available at: https://doi.org/https://doi.org/10.1016/j.jbusres.2023.113872
21. Odoom R (2025) Exploring consumer education and empowerment as a pathway to brand reputation and brand engagement in sustainable digital
marketing, Sustainable Futures, 10, p. 101482. Available at: https://doi.org/https://doi.org/10.1016/j.sftr.2025.101482
22. Olayemi K et al (2024) A Digital Twin Framework for Reinforcement Learning with Real-Time Self-Improvement via Human Assistive Teleoperation.
Available at: https://doi.org/10.48550/arXiv.2406.00732
23. Pascucci F, Savelli E, Gistri G (2023) How digital technologies reshape marketing : evidence from a qualitative investigation, pp. 27–58
24. Rodgers W et al (2023) An artiﬁcial intelligence algorithmic approach to ethical decision-making in human resource management processes, Human
Resource Management Review, 33(1), p. 100925. Available at: https://doi.org/https://doi.org/10.1016/j.hrmr.2022.100925
25. Saratkar SY et al (2025) Digital twin for personalized medicine development, (August), pp. 1–23. Available at:
https://doi.org/10.3389/fdgth.2025.1583466
Page 17/22

26. Saura JR, Škare V, Dosen DO (2024) Is AI-based digital marketing ethical? Assessing a new data privacy paradox, Journal of Innovation & Knowledge,
9(4), p. 100597. Available at: https://doi.org/https://doi.org/10.1016/j.jik.2024.100597
27. Segbenu B et al (2025) Applications of Reinforcement Learning in Dynamic Pricing Models for E-Commerce Businesses, World Journal of Advanced
Research and Reviews, 26, pp. 1562–1573. Available at: https://doi.org/10.30574/wjarr.2025.26.3.2319
28. Suchman M (1995) Managing Legitimacy: Strategic and Institutional Approaches. Academy of Management Review, 20, 571–611, The Academy of
Management Review, 20, p. 571. Available at: https://doi.org/10.2307/258788
29. Susser D, Roessler B, Nissenbaum H (2018) Online Manipulation: Hidden Inﬂuences in a Digital World, SSRN Electronic Journal [Preprint]. Available at:
https://doi.org/10.2139/ssrn.3306006
30. Tang B, Li S, Zhao C (2026) Reinforcement learning framework for computerized adaptive testing using multi armed bandit approach, pp. 1–16
31. Tricco AC et al (2018) PRISMA extension for scoping reviews (PRISMA-ScR): Checklist and explanation, Annals of Internal Medicine, 169(7), pp. 467–
473. Available at: https://doi.org/10.7326/M18-0850
32. Ukko J et al (2026) Digital twins ’ impact on organizational control: perspectives on formal vs social control, 35(8), pp. 253–272. Available at:
https://doi.org/10.1108/ITP-09-2020-0608
33. Uzoka O (2020) Service Dominant Logic, Co-production and Co-creation: Model Development and Speciﬁcations, 64, pp. 49–57. Available at:
https://doi.org/10.7176/JMCR/64-03
34. Varadarajan R (2020) Advancing theory in marketing: insights from conversations in other disciplines, AMS Review, 10(1), pp. 73–84. Available at:
https://doi.org/10.1007/s13162-020-00167-8
35. Vargo SL, Koskela-Huotari K (2020) Advancing conceptual-only articles in marketing, AMS Review, 10(1), pp. 46–53. Available at:
https://doi.org/10.1007/s13162-020-00173-w
36. Vargo SL, Lusch RF (2004) The Four Service Marketing Myths: Remnants of a Goods-Based, Manufacturing Model, Journal of Service Research, 6(4), pp.
324–335. Available at: https://doi.org/10.1177/1094670503262946
37. Vellesalu A et al (2023) Institutional re-conﬁguration and value co-creation in circular product development: A service ecosystem perspective in the
textile and apparel industry, Journal of Cleaner Production, 414, p. 137682. Available at: https://doi.org/https://doi.org/10.1016/j.jclepro.2023.137682
38. Verschraegen G (2026) Adaptive governance : learning from what organizations do and managing the role they play, (June). Available at:
https://doi.org/10.1108/K-11-2020-0759
39. Vocino A (2026) Mapping artiﬁcial intelligence research in the cultural and creative industries: A systematic bibliometric review, Technovation, 154, p.
103551. Available at: https://doi.org/https://doi.org/10.1016/j.technovation.2026.103551
40. Vosselman E (2022) The performativity of accounting: advancing a Posthumanist understanding, Qualitative Research in Accounting & Management,
19(2), pp. 137–161. Available at: https://doi.org/https://doi.org/10.1108/QRAM-04-2021-0062
41. Wang Z (2025) The inﬂuence of AI on consumer behavior: Shaping choices and preferences in the digital marketplace, Systems and Soft Computing, 7,
p. 200397. Available at: https://doi.org/https://doi.org/10.1016/j.sasc.2025.200397
42. Zahedi H, Khanizad R (2025) A Framework for Digital Twin-Enabled Smart Governance: Predictive, Participatory, and Sustainable Urban Management.
Available at: https://doi.org/10.13140/RG.2.2.28827.12321
43. Zhou C et al (2025) Personalized recommendation, behavior-based pricing, or both? Examining privacy concerns from a cost perspective, Omega, 133, p.
103223. Available at: https://doi.org/https://doi.org/10.1016/j.omega.2024.103223
44. Zuboff S (2019) Surveillance Capitalism and the Challenge of Collective Action, New Labor Forum, 28(1), pp. 10–29. Available at:
https://doi.org/10.1177/1095796018819461
Figures
Page 18/22

Figure 1
RDTMT Process Map: Reﬂexive Governance Framework for Algorithmic Consumer Systems
Note. Developed by the authors based on the conceptual framework proposed in this study.
Page 19/22

Figure 2
Empirical Foundations of RDTMT: Mapping Four Convergent Clusters to Theoretical Constructs
Note. Developed by authors based on scoping literature review ﬁndings and VOSViewer mappings.
Page 20/22

Figure 3
Reinforcement Learning in RDTMT: MDP Architecture and Equation Mapping
Note. Developed by the authors based on the proposed Reﬂexive Digital Transformation and Marketing Theory (RDTMT), integrating reinforcement learning
theory (Sutton & Barto, 2018), Markov Decision Process principles (Puterman, 1994).
Page 21/22

Figure 4
RDTMT Practitioner Diagnostic Toolkit: Assessing Digital Reﬂexivity, Ethical Feedback Elasticity, and Value Coherence
Note. The authors developed this through theoretical synthesis and operationalization of the RDTMT constructs, grounded in the systematic literature review
and the conceptual framework outlined in this study.
Page 22/22
