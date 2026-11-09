---
title: High-Risk AI Systems and the Problem of Identity in the European AI Act
url: https://arxiv.org/abs/2605.23922
category: digital-marketing
subcategory: empirical
date: 2026-04
venue: ''
authors:
- Andrea Ferrario
source: arxiv
pdf_url: https://arxiv.org/pdf/2605.23922
pages: 23
chars: 81923
fetched_at: '2026-11-08T13:09:21+00:00'
kb_version: 1
---

# High-Risk AI Systems and the Problem of Identity in the European AI Act

HIGH-RISKAI SYSTEMS AND THEPROBLEM OFIDENTITY IN
THEEUROPEANAI ACT
Andrea Ferrario∗1,2,3
1 Institute of Biomedical Ethics and History of Medicine, University of Zürich, Zürich, Switzerland
2 SUPSI, Dalle Molle Institute for Artificial Intelligence (IDSIA), Lugano, Switzerland
3 ETH Zürich, Zürich, Switzerland
Accepted as a non-archival paper atThe 2026 ACM Conference on Fairness, Accountability, and Transparency
(FAccT ’26), June 25–28, 2026, Montreal, QC, Canada.
ABSTRACT
The EU Artificial Intelligence Act (AIA) establishes a lifecycle governance regime for high-risk AI
systems built around ex-ante conformity assessment, post-market monitoring, and re-assessment
upon “substantial modification.” These obligations presuppose AI identity judgments: regulators and
providers must decide when an updated system remains the same system over time. In this work, we
show how this logic is clarified by the function+ framework of artifact identity, which individuates
AI systems by their techno-function together with context-sensitive criteria of appropriate functioning,
captured as “AI trustworthiness.” We further argue that the AIA does not provide an internal, auditable
criterion forsynchronicidentity—when two AI systems at a given time should count as the same
for regulatory purposes—and instead largely defers such sameness determinations to sectoral or
harmonization instruments. function+ supplies a synchronic identity test anchored in techno-
function and trustworthiness profiles and levels, making synchronic identity decisions inspectable in
governance settings such as procurement, liability, and market surveillance. Our contribution is a
conceptual and auditing lens: we provide a correspondence map between AIA lifecycle obligations
and function+ identity components, and we make the synchronic case operationally legible via a
minimal decision flow for audit and dispute contexts. We conclude with two implementation-facing
recommendations: (1) more precise, testable reporting of intended purpose, and (2) standardized,
auditable trustworthiness reporting that supports comparability over time and across deployments.
Keywords:Artificial Intelligence, EU AI Act, AI Governance, Metaphysics, Identity, Time, Audit
∗Corresponding author:aferrario@ethz.ch.
arXiv:2605.23922v3  [cs.CY]  4 Jul 2026

1 Introduction
The European Union Artificial Intelligence Act (AIA) [EU AI Act, 2024] is the first regulatory framework for governing
AI in the EU market, aiming to safeguard health, safety, and fundamental rights while promoting trustworthy AI
(Recital 1, AIA). Notably, the regulation classifies systems into four risk categories while introducing a distinctive
regulatory lifecycle regime for the so-called high-risk AI systems. This regime hinges on ex-ante conformity assessment,
post-market monitoring, and renewed assessment when a change constitutes a “substantial modification” (Article 3(20),
Annex IV; Article 3(23) and Recital 128, AIA). In practice, this regime requires repeated judgments about whether an
AI system is still “the same” system for regulatory purposes as it is updated, re-trained, or re-configured.
We refer to these as “AI identity” judgments in two senses.Diachronic identityconcerns persistence: when does
an updated AI system remain the same system over time, as opposed to becoming (legally) a new system that
must undergo a new conformity assessment?Synchronic identityconcerns sameness-at-a-time: when should two
contemporaneous instantiations (e.g., copies, configurations, or provider variants) be treated as the same AI system
for regulatory comparability? The latter question becomes unavoidable whenever governance actors must decide
whether compliance evidence, documentation, monitoring signals, or corrective actions established for one instantiation
legitimately generalize to another—for example across certification scoping, traceability and incident response, or
comparability claims in procurement and market surveillance.
Motivated by the AIA’s regulatory approach to AI identity over time, this paper advances two claims and is explicitly
scoped as a conceptual and auditing contribution. We do not propose a validated compliance procedure or an empirical
implementation study. Rather, we aim to make explicit the identity assumptions that are already doing work in AIA
lifecycle governance and to provide a structured lens for rendering identity-relevant determinations more transparent
and contestable.Claim 1is that the AIA’s lifecycle mechanism implicitly operationalizes diachronic identity for
high-risk AI systems. Conformity assessment fixes an identity-relevant baseline (intended purpose and requirements of
appropriate functioning), post-market monitoring tracks continued compliance, and “substantial modification” functions
as a legal discontinuity condition that triggers re-certification. We show how this structure is clarified by thefunction+
framework of artifact identity [Carrara and Vermaas, 2009, Ferrario, 2025], which individuates AI systems by their
techno-function together with context-sensitive criteria of appropriate functioning (a trustworthiness profile) and their
satisfaction over time (a trustworthiness level). Figure 1 summarizes this correspondence from AIA lifecycle obligations,
through governance-to-metaphysics identity questions, to function+ identity components.Claim 2is that the AIA
does not provide an internal, auditable criterion for synchronic identity for stand-alone high-risk systems and instead
largely defers sameness determinations to sectoral or harmonization instruments. This allocation is often reasonable, but
it can leave under-specification precisely where governance must adjudicate sameness claims across contemporaneous
instantiations. Figure 2 makes this problem operationally legible by depicting a minimal audit workflow: sameness
claims must be justified at conformity assessment (purpose/profile) and maintained under post-market monitoring
(trustworthiness level at timet), with explicit “no” points that terminate comparability.
Our contributions are therefore: (1) a legally grounded analysis of how identity assumptions are embedded in AIA
lifecycle governance; (2) a structured conceptual alignment between the AIA mechanism and function+ that renders
identity-relevant determinations more transparent and auditable; and (3) two implementation-facing recommendations
focused on documentation and comparability: more precise, testable reporting of intended purpose (including for
2

systems with generative capabilities), and standardized, auditable trustworthiness reporting that supports comparability
across deployments and over time. While an increasing body of literature focuses on ethical challenges and legal
shortcuts affecting the AIA [Floridi, 2021, Smuha et al., 2021, Laux et al., 2024, Wörsdörfer, 2025, Loi et al., 2025], our
paper provides metaphysical grounding for the AIA’s identity-relevant lifecycle logic and frames synchronic identity in
a way that is inspectable in audit and dispute settings.
The remainder of the paper proceeds as follows. Section 2 introduces two motivating cases. Section 3 presents
function+ and the trustworthiness-based characterization of AI systems. Sections 4-6 summarize the relevant AIA
provisions. Sections 7-8 develop Claims 1-2. Section 9 provides recommendations, and Section 10 shares our
conclusions.
2 Motivation: Two Illustrative Cases of AI System Identity Problems
To motivate our analysis of AI identity, we present two stylized but realistic cases involving high-risk AI systems (here,
systems used in sensitive applications; the term is defined below). The cases are not intended as reports of actual
disputes, but as simplified scenarios that isolate identity questions. The first concerns identity over time (diachronic
identity); the second, identity at a given time (synchronic identity).
1. Changes over time in AI systems for clinical triage. Consider an AI system developed by a company and deployed in
the emergency department of a hospital in an EU country. The system outputs a binary classification of incoming patients
into priority levels: low and high. (This strong simplification suffices for the present case.) The classifications feed into
a triage process which seeks to maximize life years and optimize emergency resource allocation. At deployment, the
system exhibits stable performance, as documented by the provider during the extensive pre-market testing that granted
the system official certification.
However, a subsequent respiratory disease outbreak disproportionately affects older patients and causes a distributional
shift: the real-world patient data now diverge from the distributions used to develop the system. In response, the provider
implements a series of overnight updates, retraining the core model on new hospital data for about a month. Furthermore,
different fairness constraints are introduced to mitigate age-related disparities and the explainability module includes
counterfactual explanations.2 In parallel, hospital data engineers apply further modifications through a dedicated API,
outside the direct oversight of the provider. Over time, a chart review reveals anomalous phenomena. Clinicians observe
that the counterfactual explanations and model outcomes of different patients now tautologically align, undermining
their role as actionable explanations in discussions with patients’ family members. Although the provider insists that
the system remains “the same,” and its accuracy remains stable over time, many clinicians believe it is substantially
different from the original version and argue that it requires a full, and costly, re-assessment. Some simply state that
they do not trust the system anymore. The issue eventually escalates to hospital management, while patient advocacy
groups and journalists begin investigating the case: the provider has sold licenses for the AI system to twelve healthcare
institutions in the same country.
2A counterfactual explanation of why Y got a low priority score and, therefore, was denied resource-intensive emergency
treatments could look like this: “if patient Y were ten years older and their illness-severity score below four, then they would have
received a high priority score, other things equal.”
3

At what point does an AI system cease to be the “same” system and instead count as asubstantiallyandlegally“new”
one? Do changes to intended purpose, model architecture, or explainability modules alter identity, and if so, how?
Third-party liability, regulatory compliance, and insurance coverage all hinge on how this distinction is drawn. It
seems that criteria relating system design requirements to its post-deployment monitoring are needed to govern such
phenomena.
2. When are AI systems used in biometric border control the same?Consider a public tender for real-time
biometric identification systems in major European airports. National authorities are willing to procure two high-risk
AI systems—let us call them A and B—from the same vendor for two different airports. While revising the system
documentation provided by the vendor, the procurement officials notice that both systems rely on the same open-source
models for generating facial bounding boxes and classifying images within those boxes. The main differences lie in the
user interface and some minor workflow integrations. Importantly, however, systemA shows superior performance:
due to optimization work at the design stage, it achieves lower inference latency and faster outcome retrieval, which
the vendor would use to justify an exceptionally higher monthly licensing fee than for system B. This said, both
systems underwent the same conformity procedures, with identical testing protocols for accuracy, robustness, safety,
and reliability. Authorities conclude that both systems are, in substance, the same biometric control device: accuracy is
the same, and differences in processing speed are not material in airport settings where passengers are queued either
for check-in or customs declarations. In their interpretation of “intended purpose” of the AI system, its operational
context and conditions of use carry equal weight with its techno-function, namely, to biometrically identify subjects.
On this reading, authorities issue an equivalence determination: A and B are the same for the intended use, so A’s
premium brings no material benefit. As a result, the authority can award to B, or require the provider to offer A
at the non-premium rate. The provider disputes this view, arguing that the optimizations in A justify treating it as
asubstantially differentproduct, as these procedures yield, overall, a higher level of what they termed a “system
operational adequacy” index in their documentation. In their view, this index summarizes the operational efficiency
of the system along different dimensions, including throughput and latency; its being higher for A justifies a higher
licensing fee for that system. In this example, what makes A and B thesamesystem for biometric border control? Do
specific system functionality dimensions suffice to declare their sameness (or lack of)substantiallyandlegally? Here,
regulators could resolve the dispute by clarifying whether identical intended use and core functionality are sufficient to
establish system identity in legal terms, and whether quantitative differences in “system operational adequacy” warrant
treating them as legally distinct systems. Importantly, for contracting authorities, procurement processes risk distortion
if bids rest on systems that are not substantially different: it would make it difficult to justify the acquisition of system
A instead of B using taxpayer money. This could result in a diminished public trust in the responsible institutions,
although, in practical terms, for passengers, being screened by systemAorBmakes no difference.
These two cases illustrate how questions of AI identity may arise and affect different societal actors. Both concern,
albeit in different ways, what counts as the adequate functioning of an AI system. Addressing these questions requires
precise criteria that can specify conditions of sameness to guide AI regulations. Introducing these criteria is possible at
the price of engaging with a contested notion in contemporary AI philosophy: “trustworthiness.” This is what we will
do in the next section, showing a way to address these AI identity problems.
4

3 A Trustworthiness-Based Metaphysics of AI Systems
3.1 The traditional perspective on artifactual metaphysics
Artifacts—human-made objects designed to serve purposes—have often been denied a metaphysical standing on a par
with natural entities such as rocks, animals, and persons [Lowe, 2014]. Two reasons are typically invoked: artifacts
admit multiple (intended and unintended) purposes, and the mapping between their purposes and material realizations
is many-to-many. Their disassembly and reassembly also fuel classic puzzles of identity, most famously the Ship
of Theseus [Gallois, 2016]. As a result, for a long time philosophers have defended the idea that it makes no sense
(metaphysically) to ask ourselves whetheridentity criteria for artifacts, namely, formal rules to define the persistence
of artifacts over time or determine whether two artifacts are the same (artifact), can be appropriately defined. 3 The
relation between genuine metaphysics and identity (criteria) is exemplified by Quine’s famous quote: “no entity without
identity” [Quine, 1969, p. 44].
3.2 Thefunction + approach to artifactual identity
Carrara and Vermaas have challenged this longstanding perspective on the metaphysics of artifacts introducing the
function+ framework as a way to account for the dual nature of artifactual identity [Carrara and Vermaas, 2009].
According to this view, artifact identity depends on two interrelated dimensions. The first is thetechno-function, namely,
what the artifact is designed to do, e.g., to fly for airplanes. Only artifacts designed for the same techno-function
can be compared through identity criteria, as they belong to the same artifactual “kind” (e.g., “airplanes,” “robotic
surgery systems”).4 The second is thecontextual embedding—the “+” in function+—which refers to the social and
normative settings in which the artifact is designed and deployed [Carrara and Vermaas, 2009]. Artifacts may share
the same techno-function but differ in identity if they operate in distinct social contexts with different expectations,
norms, and evaluative standards. This contextual embedding comprises an operational principle (the rules by which
components cooperate to realize that function) and a normal configuration (the canonical arrangement judged to
embody that principle, typically shaped by design practice and standards). Compared with mereological essentialism
[Wiggins, 2001], where two artifacts are equal if and only if they are constituted by the same parts, function+ is
more permissive: two tokens can count as the same (artifact) within a kind despite differing materials, provided the
function-operational principle-configuration triple aligns [Carrara and Vermaas, 2009]. That said, Carrara and Vermaas’
function+ framework is not the only possible account of artifact identity. Its relevance lies in the specific problem it
addresses. Their proposal is developed against an anti-realist challenge to artifact identity: if artifacts are individuated
by their functions, then artifact kinds appear too coarse-grained to support genuine identity criteria. This is the worry
associated with Wiggins: very different objects can perform the same function, and therefore function alone cannot
determine what kind of artifact something is, or whether it persists as the same artifact over time [Wiggins, 2001].
Baker and Elder respond to this anti-realist tendency by defending the metaphysical reality of artifacts and by treating
artifact functions as identity-relevant [Baker, 2004, Elder, 2004]. Carrara and Vermaas accept this realist orientation,
3These rules are typically written using propositional logic formalism. They can be introduced, for instance, for mathematical
entities, such as sets. The Axiom of Extensionality is such an example—see [Pinter, 2014]. Identity criteria for human beings are an
object of investigation in the philosophy of mind domain instead [Olson, 2024].
4Techno-functions can be specified at different levels of detail: broader specifications pick out wider artifact kinds, whereas finer
ones carve out narrower ones.
5

but refine it. Function must be supplemented by further features that specify how the function is realized in practice.
This is the role of operational principles and normal configurations. The point of the “+” is therefore to avoid both
material reductionism and function-only coarseness: artifact identity is not fixed by material constitution alone, nor
by function alone, but by function together with the relevant structure of realization. Thus, according to Carrara and
Vermaas, artifacts enjoy genuine metaphysical standing, and identity claims about them are possible. Framed this way,
artifact identity links functional aims to their evolving design.
3.3function + for AI systems
Carrara and Vermaas’ ontological strategy can be transferred to AI systems once their designed function, context of
deployment, and standards of appropriate performance are made explicit. On the one hand, the identity of AI systems
cannot be fixed by material components alone: models, datasets, interfaces, deployment environments, documentation,
and monitoring practices may change while the system remains functionally continuous. On the other hand, function
alone is too coarse-grained for regulatory purposes. Many AI systems may share a nominal function while differing
in the constraints, safeguards, performance expectations, and operational conditions under which they count as
appropriately functioning. The function+ framework can preserve the centrality of techno-function while requiring
further criteria that specify how that function is realized and assessed in practice. Motivated by these considerations,
Ferrario recently adapted Carrara and Vermaas’ function+ framework to AI systems, introducing explicit criteria to
govern the identity of these systems. His approach hinges on the observation that ‘AI trustworthiness’ encodes the
contextual embedding of AI systems, i.e., the social and normative settings in which they are designed and deployed.
This stance on AI trustworthiness has been recently popularized in the human-AI interaction domain [Jacovi et al.,
2021] and descends conceptually from Hawley’s “trust as commitment” account [Hawley, 2014]. As it will become
clearer in Section 5, it is widely endorsed by AI regulations as well. According to Hawley, to “trust someone to do
something is to believe that she has a commitment to doing it, and to rely upon her to meet that commitment” [Hawley,
2014, p. 10]. Commitments typically give us obligations, but they are not necessarily morally-laden. In this framing, an
AI system is considered worthy of our trust if it upholds a set of commitments contextualized by the system’s intended
functioning.5 The trustworthiness of an AI system is encoded in itstrustworthiness profile, a structured set of formal
and informal requirements that fix when an AI system counts as appropriately functioning in its intended use and
context of applicability [Ferrario, 2025]. These profiles span commitments, such as accuracy and robustness over time,
safeguards for fairness and bias mitigation, transparency and explainability, auditability and others. (These requirements
will return in Section 5 when we introduce the approach to AI trustworthiness in the AIA.) Each commitment is
made explicit in appropriate documentation, called “contract” following Hawley’s terminology, that describes the way
and extent to which the AI system would satisfy the commitment over time. Finally, the trustworthiness profile of
an AI system is quantified by atrustworthiness level functionthat summarizes the evolution over time of the degree
of trustworthiness of the system. This function operationalizes context: it aggregates diverse—and many, especially
for complex systems in high-stakes applications—AI trustworthiness requirements into one signal that supports, in
particular, the monitoring of system trustworthiness. While some requirements may decrease over time, e.g., a minor
drop in accuracy, the trustworthiness level function provides an overarching, quantitative perspective to what extent the
5This approach mirrors how we judge trustworthiness in interpersonal relations: an individual is worthy of trust when he upholds
socially recognized commitments, e.g., being an expert in a doxastic domain or upholding moral standards. To increase one’s
trustworthiness in a social context, one typically acts on the relevant capabilities that are seen as trust-enabling.
6

AI system is maintaining its correct functioning—see Section 5.1 and Figure 1 in [Ferrario, 2025] for a few examples of
trustworthiness level functions.
In summary, in Ferrario’s formulation of Carrara and Vermaas’function+ account, AI systems are metaphysically
characterized by their (1) techno-function, (2) trustworthiness profile, and (3) trustworthiness level function. Ferrario’s
account does not assume that AI systems are bare individuals that can be identified independently of the kind to which
they belong [Lowe, 2014]. Rather, individuals are tokens or instantiations of a kind, and the kind is fixed by the
relevant identity criteria. These criteria are governance-based: AI systems belong to the same kind when they share the
same techno-function and the same trustworthiness profile. This level of individuation is higher than ordinary product
categories such as ‘chatbots,” ‘automated vehicles,” or “clinical triage systems.” Once this kind is fixed, the relevant AI
system tokens are the instantiations that fall under it, and diachronic or synchronic identity judgments can then ask
whether theyalsopreserve the relevant trustworthiness level. Within this framework, two identity criteria emerge—see
definition 5.1 in [Ferrario, 2025]:
• Diachronic identity( DIfunction+): An AI system persists at two times t1 and t2 if it maintains the same
techno-function and trustworthiness profile att 1 andt 2, and the same trustworthiness levels at those times.
• Synchronic identity( SIfunction+): Two AI systems are identical at time t if they perform the same techno-
function, have the same trustworthiness profile and trustworthiness level att.
Applying DIfunction+ and SIfunction+ to the two use cases from Section 2 yields: in triage, adding fairness constraints
and counterfactual modules alters the trustworthiness profile, while overnight retraining likely reflects a drop in the
trustworthiness level. Unless these changes were pre-determined in the trustworthiness contracts and the trustworthiness-
level function is robust to the observed accuracy drop, DIfunction+ indicates that the system stops persisting. In the
second use case, A and B can be identical if operational efficiency measured by latency is a trustworthiness contract for
both systems. In that case, if the trustworthiness levels at the time of assessment—i.e., the levels of “system operational
adequacy” in the provider’s terminology—are equal, then the systems A and B are identical as border control AI
systems, followingSI function+.
Now that we clarified the metaphysical perspective on AI identity, we explore how AI regulation manages it. To do so,
we move forward by briefly introducing the AIA, and discussing its management of AI trustworthiness in relation to
high-risk AI systems.
4 A Minimal Introduction to the AIA
The AIA establishes a unified legal framework for the development, deployment, and use of AI systems within the EU
(Recital 1, AIA). Its enforcement aims to promote the uptake of human-centered and trustworthy AI while ensuring
the protection of health, safety, fundamental rights and mitigating the potential harms posed by AI systems (Recital 1,
AIA). The regulation promotes rules that should be in line with the Union’s trade commitments, taking into account
other regulatory approaches, such as the European Declaration on Digital Rights and Principles for the Digital Decade
[EU Declaration Digital Rights, 2022] and the Ethics guidelines for trustworthy AI of the High-Level Expert Group on
Artificial Intelligence (AI HLEG) [EU AI HLEG, 2019]. It applies to providers of AI systems in the EU, irrespective of
whether they are established in the Union, so long as their AI systems impact the EU market (AIA, Article 2). Thus, the
7

AIA isaterritorial[Floridi, 2021], fostering the “Brussels effect,” namely, thede factoalthough notde jureadoption of
EU regulatory standards by non-EU countries to streamline cross-border economic exchanges [Bradford, 2020, Petit,
2020]. Within the AIA, anAI systemis
a machine-based system that is designed to operate with varying levels of autonomy and that may
exhibit adaptiveness after deployment, and that, for explicit or implicit objectives, infers, from the
input it receives, how to generate outputs such as predictions, content, recommendations, or decisions
that can influence physical or virtual environments (Art. 3, [EU AI Act, 2024]).6
Notably, the AIA follows a risk-based approach to the regulation of AI systems in the EU market, whereby the legal
obligations of responsible actors are determined by the assigned risk category of each system. It distinguishes four
categories: low or minimal risk, limited risk, high risk, and unacceptable risk. 7 High-risk AI systemsfall into two
categories. First, they may either constitute a safety component of a product8 or be themselves products governed by
one of the Union harmonization legislations listed in Annex I of the AIA. These legislations cover sectors such as
machinery, toys, lifts, medical devices, and civil aviation technology. In this case, AI systems inherit their high-risk
status from being the safety component of aregulatedproduct category (or the product itself). Second, systems are
deemed high-risk if theirintended purpose, i.e., “the use for which an AI system is intended by the provider, including
the specific context and conditions of use, as specified in the information supplied by the provider [...] in the technical
documentation” (Article 3(12), AIA), are one of the specific cases enumerated in Annex III of the AIA. These use cases
include biometric identification and categorization of individuals, the management of critical infrastructure, education
and vocational training, access and enjoyment of private and public essential services, law enforcement, migration,
asylum and border control management, as well as the administration of justice and democratic processes. These
high-risk AI systems are called “stand-alone.”9 Over time, the list of stand-alone high-risk AI systems may be updated
by the European Commission under the procedure outlined in Article 7 of the AIA.
5 AI Trustworthiness in the AIA
The AI HLEG guidelines on Trustworthy AI form the backbone of the AIA’s approach to AI trustworthiness [Floridi,
2021, Smuha et al., 2021, Ho and Caals, 2024, Wörsdörfer, 2025, Laux et al., 2024].10 These guidelines rest on the
non-trivial assumption that AI systems can themselves be objects of human trust, i.e., the same assumption endorsed
6Although this definition has received some criticism, as some argue that it is too broad [Kazim et al., 2023, Mökander et al.,
2022], nevertheless, it allows accommodating a wide range of tools, including those with generative capabilities, that are already
present or anticipated to enter the EU market. The definition includes “general-purpose AI systems,” which are defined in Article
3(66)-(69), AIA.
7Minimal risk AI systems are not subject to regulatory obligations, while limited risk AI systems must meet general transparency
requirements. Unacceptable risk AI systems are prohibited from entering the EU market.
8In the AIA’s Article 3(14), one reads: “‘safety component’ means a component of a product or of an AI system which fulfils a
safety function for that product or AI system, or the failure or malfunctioning of which endangers the health and safety of persons or
property.”
9See, for instance, the AIA’s Recital 52: “As regards stand-alone AI systems, namely high-risk AI systems other than those that
are safety components of products, or that are themselves products, it is appropriate to classify them as high-risk if, in light of their
intended purpose, they pose a high risk of harm to the health and safety or the fundamental rights of persons, taking into account
both the severity of the possible harm and its probability of occurrence [...].”
10The interested reader may consult the literature for an analysis of “Legally Trustworthy AI” [Smuha et al., 2021], the socio-
epistemological perspective on trust and trustworthiness promoted in the AIA [Ho and Caals, 2024], and the supposed conflation
between AI trustworthiness and acceptance of risk in the AIA [Laux et al., 2024].
8

by function+, see Section 3. They operationalize AI trustworthiness in four steps. First, Trustworthy AI is defined
as asocietal standardthat requires systems to be lawful, ethical, and robust throughout their lifecycle. Second, this
standard is articulated through fourethical principles, namely, respect for human autonomy, prevention of harm,
fairness, and explicability, alongside a discussion of tensions among them. Third, these principles are translated into
seven requirementsof AI trustworthiness: human agency and oversight; technical robustness and safety; privacy and
data governance; transparency; diversity, non-discrimination, and fairness; societal and environmental well-being; and
accountability. Finally, the guidelines link these requirements totechnicalandnon-technical methodsfor assessing and
fostering AI trustworthiness, which have since inspired a broad landscape of frameworks and tools [Mattioli et al., 2024,
Kaur et al., 2022, Ala-Pietilä et al., 2020, Zicari et al., 2021, Li et al., 2023, Mökander and Floridi, 2021, Loi et al.,
2019]. In particular, the AI HLEG’s Assessment List for Trustworthy AI (ALTAI) operationalizes these requirements
as a voluntary self-assessment tool [Ala-Pietilä et al., 2020]. The AIA refers to the AI HLEG guidelines explicitly in
its Preamble. For instance, in Recital 7, it is stated that the AIA “should take into account” these guidelines, while in
Recital 27 the seven requirements are discussed while offering an invitation to operationalize them. Finally, Recital
165 encourages providers of high -risk AI systems to voluntarily adopt additional requirements inspired by the AI
HLEG guidelines, among others. In summary, the AIA does not treat trustworthiness as a governance ideal. In fact,
trustworthiness is translated into auditable criteria of appropriate functioning. This is where the AIA connects to the
function+ framework. The next section and Figure 1 show how this structure is operationalized diachronically through
conformity assessment, post-market monitoring, and substantial modification.
6 Diachronic Identity in the AIA
The AIA regulates the change over time of high-risk AI systems with a governance mechanism that comprises (1) an ex-
ante conformity assessment, (2) a post-market monitoring system, and (3) the assessment of “substantial modifications.”
We discuss these procedures and their relations in the following sections, emphasizing their relation with the AI HLEG
guidelines and their Trustworthy AI paradigm.
6.1 The ex-ante conformity assessment
The AIA mandates anex-ante conformity assessmentfor high-risk AI systems as a prerequisite for their entry into the
EU market. This assessment is defined as “the process of demonstrating whether the requirements set out in Chapter III,
Section 2 relating to a high-risk AI system have been fulfilled” (Article 3(20), AIA). These requirements are described
in some detail in Articles 8-15; they include the design of a risk management system and data governance procedures,
the drafting of technical documentation,11 the recording of events over the lifetime of the system, the enforcement of
transparency criteria and the provision of information about deployers, human oversight processes, accuracy, robustness
and cybersecurity procedures. They implement the AI HLEG guidelines’seven requirementsof Trustworthy AI among
others. Crucially, if the conformity assessment presented by a provider certifies that the high-risk AI system satisfies
these requirements, the system is granted a CE marking as a formal declaration of conformity (Article 44, AIA). For
high-risk AI that is part of a regulated product (or is itself such a product), the conformity assessment can be done
under the relevant EU product legislation. In contrast, stand-alone high-risk AI systems (Annex III AIA) must follow a
11Article 11 reads “It shall contain, at a minimum, the elements set out in Annex IV .” We describe the documentation in Annex IV
in what follows.
9

separate route: either an internal control procedure or an independent assessment by a third-party notified body—see
Figure 2 in Mökander et al. [2022].12
Further, the AIA specifies in Annex IV the technical documentation that is required for the conformity assessment of
high-risk AI systems. This documentation is rather comprehensive, spanning nine sections. Among other obligations,
providers must submit a general description of the AI system, including its intended purpose, key components, and the
development process (Annex IV , Sections 1–2, AIA). It also requires providers to document detailed information on the
monitoring, functioning, and control mechanisms of the AI system, along with a description of the performance metrics
used and their justification (Annex IV , Sections 3-4, AIA). These requirements cover multiple AI HLEG guidelines’
technicalandnon-technical methods. Additionally, it mandates disclosure of the risk management system and any
relevant changes occurring throughout the system’s lifecycle (Annex IV , Sections 5-6, AIA)—an issue we will examine
in detail in the following section.
6.2 The post-market monitoring system
Annex IV further specifies that providers must include a list of any applicable harmonized standards, a copy of the EU
declaration of conformity, and the system’s post-market monitoring plan (Annex IV , Sections 7-8, AIA). Central to the
monitoring plan is thepost-market monitoring system, which is intended to evaluate the performance of high-risk
AI systems after they have entered the market (Annex IV , Section 9, AIA).13 This monitoring system is designed to
continuously collect, document, and analyze data and assess system performance throughout its operational lifetime,
drawing on information provided by deployers and other relevant sources. Its goal is to allow providers to evaluate “the
continuous compliance of AI systems with the requirements set out in Chapter III, Section 2” (Article 72(2), AIA).
However, at the time of writing, not much else is known about the monitoring plan and system as only their scope and
general governance recommendations are provided. That said, the EU Commission plans to establish a template for the
post-market monitoring plan in the course of 2026.
6.3 The ‘substantial modifications’ of high-risk AI systems
The AIA characterizes the possible changes—referred to as “modifications” therein—affecting CE-certified high-risk
AI systems throughout their lifetime by using the concept ofsubstantial modification, which is defined in Article 3(23)
as follows (emphasis ours):
‘substantial modification’ is a change to an AI system after its placing on the market or putting into
service which isnot foreseen or planned in the initial conformity assessmentcarried out by the
provider and as a result of which the compliance of the AI system with the requirements set out in
Chapter III, Section 2 is affected or results in a modification to theintended purposefor which the AI
system has been assessed.
This concept is the AI-specific translation of substantial modification already regulated in Union harmonization
legislation. For instance, under the Machinery Regulation [EU Machinery Regulation, 2023], a substantial modification
12The internal audit route is available only to stand-alone systems that fully comply with the requirements set out in Chapter 2 of
Title III of the AIA [Mökander et al., 2022].
13For further discussion on the interplay between ex-ante conformity assessment and post-market monitoring, see Mökander et al.
[2022, Section 4].
10

refers to a change to machinery14 that is not foreseen or planned by the manufacturer and that affects the safety of the
machinery by creating a new hazard or increasing an existing risk (Article 3). Similarly, under the Cyber Resilience
Act [EU Cyber Resilience, 2024], a substantial modification to a product with digital elements is defined as a change
that either affects the product’s compliance with the cybersecurity requirements listed in that regulation, or alters its
intended purpose. The key point is that substantial modifications of high-risk AI systems result in the emergence of a
“new” AI system that requires a “new” conformity assessment. In fact, Recital 128 reads (emphasis ours):
In line with the commonly established notion of substantial modification for products regulated by
Union harmonization legislation, it is appropriate that whenevera change occurs which may affect
the compliance of a high-risk AI system with this Regulation(e.g. change of operating system or
software architecture), or whenthe intended purpose of the system changes, that AI system should be
considered to be a new AI system which should undergo a new conformity assessment.
Thus, substantial modifications force providers of high-risk AI systems to finalize new conformity assessments and wait
for new CE certificates. Recital 128 in the AIA also describes the changes thatdo notinterrupt persistence of a high-risk
AI system and, therefore, do not require a new conformity assessment: these are all modifications to the system that
have been pre-determined by the provider and assessed at the moment of the conformity assessment.
A summary of the AIA’s governance mechanism of diachronic identity of high-risk AI systems. Requirements specified
in Chapter III, Section 2 (Articles 8-15) define high-level obligations for high-risk AI systems that must be operational-
ized in practice considering the context, i.e., intended purpose, technical properties as well as deployment environment,
of the AI system. This occurs through the procedures and documentation that constitute the conformity assessment.
After deployment, the post-market monitoring system “continuously” assesses whether the system still meets the
requirements operationalized in the conformity assessment, scanning for substantial modifications, which would require
the management of a fresh CE certification for the “new” AI system instead. We summarize these regulatory components
in Figure 1.
7 Claim 1: AIA’s Lifecycle Governance Implementsfunction +’s Diachronic Identity
At this stage, it should be clear that the AIA’s lifecycle regime for high-risk AI systems operationalizes the diachronic
component of the function+ account of artifactual identity. Figure 1 summarizes this alignment: AIA lifecycle
obligations are linked to governance-to-metaphysics identity questions, and to the (diachronic) function+ account. To
see this in some detail, we first note that both approaches require a function-related specification of the AI system, but
they do so at different levels. Infunction+, the relevant function is thetechno-function: the core technical operation that
identifies the AI kind to which the system belongs. In the AIA, by contrast, the relevant legal notion isintended purpose,
defined as the use for which the system is intended by the provider, including its specific context and conditions of use.
Techno-function and intended purpose should therefore not be simply equated. Rather, intended purpose presupposes
or contains a techno-function, but contextualizes it through a use setting, domain, target population, operational
constraints, and conditions of deployment. For task-specific high-risk AI systems, the distance between techno-function
14Machinery is defined as an assembly of linked parts that satisfies specific functional relations with energy sources, its working
environment, and with software components—see Article 3(1) in [EU Machinery Regulation, 2023].
11

and intended purpose may be small. For generative and multi-purpose systems, such as large language models,
the distance becomes substantial: the same techno-function, such as next-token prediction or autocompletion, may
support many intended uses, including drafting, summarization, tutoring, translation, or entertainment. The function+
framework therefore uses techno-function to anchor identity at the level of AI kind, while trustworthiness profiles
(and levels) capture the contextualized conditions under which that function counts as appropriate in a given intended
use. We return on this point later in Section 9, when we will collect a few recommendations for the implementation
of function+. Second, both approaches make use of AI trustworthiness, in the form of contracts under function+
and conformity assessment requirements in the AIA, as a cornerstone of their approaches to diachronic identity. We
believe there is no bijective mapping between contracts and conformity assessment requirements, where the latter
are enumerated in Articles 8-15 in the AIA; first and foremost, it would be difficult to prove the contrary, given the
absence of a widespread, standardized template for contracts, which at the time of writing remain a rather high-level
construct. It seems, however, that, while some conformity requirements are more precise in terms of contracts—such
as Article 10 that focuses on fairness—others may encompass distinct contracts—such as Article 13 that discusses
explainability, accuracy/performance and human oversight altogether. To give shape to this relation, and improve the
pragmatics of trustworthiness contracts, practitioners could use, for instance, the AI HLEG’s ALTAI and craft their own.
The conceptual compatibility in the treatment of AI trustworthiness between function+ and the AIA’s governance
mechanism descends from the fact that contracts collect and discuss the AI requirements that, in the AIA, constitute
the conformity assessment of the system. However, while function+ provides a necessary and sufficient condition
for persistence via the DIfunction+ criterion, the AIA specifies a sufficient condition only, namely, the emergence of
substantial modifications. Arguably, this difference stems from the different aims of the metaphysical framework and the
AIA. In fact, the latter aims to provide a mechanism to recognize substantial modifications and trigger a re-certification
procedure. For this legal purpose, a sufficient discontinuity condition is enough to trigger renewed assessment, even if it
does not amount to a complete metaphysical criterion of persistence. The added value offunction+ is precisely to make
explicit what is being tracked. The individual dimensions of a trustworthiness profile—for instance accuracy, robustness,
fairness, explainability, or cybersecurity—may vary over time as they are measured through post-market monitoring.
Such variation does not by itself settle the identity question. What matters for persistence is the trustworthiness level
function, namely, the aggregated perspective on whether the system still satisfies its profile to the required degree. This
function must therefore be chosen and tested as part of AI governance: it should be robust to reasonable classes of
multidimensional variation in the profile, otherwise AI systems would implausibly flicker in and out of existence under
ordinary monitoring fluctuations, as noted by Ferrario [2025]. At the same time, the function must remain sensitive
to changes that are identity-relevant. Persistence is preserved only if the system maintains the same techno-function,
the same trustworthiness profile, and the same trustworthiness level. If the aggregated trustworthiness level changes,
then the system no longer satisfies the diachronic identity criterion. In AIA terms, this marks the kind of identity-
relevant change that qualifies as a substantial modification when it affects compliance with the Chapter III, Section 2
requirements or modifies the intended purpose, thereby triggering renewed conformity assessment. Furthermore, by
definition of substantial modification in Recital 128 in the AIA, this condition encodes sameness of techno-function
and trustworthiness profile of the diachronic identity criterion DIfunction+. However, at first glance, the trustworthiness
level identity that appears in DIfunction+ is missing in the AIA formulation. Upon a closer look, reminders to the
quantification of conformity assessment requirements or, in the jargon of function+, trustworthiness contracts are
12

EU AIA
(AI Governance)
AI Identity Questions
(Governance to Metaphysics)
function+
(AI Metaphysics)
Ex-ante conformity assess-
ment
Art. 3(20); Arts. 8-15; Annex
IV .
Requirements:intended pur-
pose; technical documentation;
risk mgmt. and data gover-
nance; event recording; trans-
parency around stakeholders
and processes.
What is the system?
Which techno-function is be-
ing assessed, and under which
intended purpose, and what
counts as appropriate function-
ing for that context?
1.Techno-function(AI kind)
2.Trustworthiness profile
(criteria of appropriate function-
ing)
Post-market monitoring
Art. 72; Annex IV(9).
Requirements:Post-market
monitoring plan and system to
collect, document, and analyze
data and assess system perfor-
mance.
Is the system still compliant
over time?
Which monitored signals indi-
cate degradation of appropriate
functioning?
Trustworthiness level
(time-indexed level of satisfac-
tion of trustworthiness profile)
e.g., plateau transitions on a
step-wise function.
“Substantial modification”
Art. 3(23); Recital 128.
Key decision point:under a
substantial modification, an AI
system should be considered
to be a new AI system and
undergo a new conformity as-
sessment
Same vs. new system?
Was change foreseen? Did it
affect compliance or the in-
tended purpose of the system?
Diachronic identity criterion
Criterion DIfunction+: same
techno-function + same trust-
worthiness profile + same trust-
worthiness levels prae-post
change.
Figure 1: Side-by-side alignment of AIA governance requirements for the lifecycle of high-risk AI systems with the
function+ framework.
ubiquitous in the AIA, see, for instance, Recitals 64, 74, 102 and Articles 13 and 15. Further, the regulation introduces
the expression “high levels of trustworthiness” in relation to the mitigation of risks from high-risk AI systems, see
Recitals 64 and 123. However, what is missing is the precise quantification of these “(high) levels” as a function of
the quantifications of its trustworthiness components. This is what function+ explicitly provides. We believe this
quantification offered by function+ will become especially relevant in the future, given the upcoming specifications
for the post-market monitoring plan expected in 2026. We will discuss this point in Section 9.
8 Claim 2:function + Fills the AIA’s Synchronic Identity Gap
While the AIA regulates diachronic identity extensively by requiring providers to assess whether updates or modifications
constitute a “substantial modification” and thus, legally, a new system, by contrast, it leaves synchronic identity to
Union harmonization legislation—see Annex I in the AIA. In fact, the AIA contains no explicit criterion for when two
high-risk AI systems (either as safety components of a product, as products themselves, or as stand-alone systems)
placed on the market should be considered legally “the same” system at any time. Logically, this division of labor
13

avoids duplication of efforts, as mentioned in Recital 124 and Articles 8 and 72 in the AIA: existing product regulations
may already contain implicit or explicit synchronic identity criteria. However, this approach is not free from limitations
that deserve our attention.
First, no criteria for synchronic identity of stand-alone high-risk AI systems are provided. (This applies to generative
AI systems as well.) In fact, by definition, no existing Union harmonization legislation can apply to these systems. As
a result—see the synchronic identity use case in Section 2—this gap implies that providers and governance bodies
lack a basis for determining whether two stand-alone high-risk AI systems should be regarded as identical. Second,
for high-risk AI systems that are safety components of products and services, it is not clear how the relevant Union
harmonization legislation is to be applied. For instance, in EU pharmaceutical law, a medicinal product applicant is not
required to document the results of toxicological and pharmacological tests or the results of clinical trials if they can
prove that the medicinal product is “essentially similar” to a medicinal product authorized in the Member State and has
the same intended “therapeutic use” among others—see Article 10 in [EU Directive Medicinal Products, 2001]. In the
EU Medical Device Regulation (MDR), the notion of “equivalence” permits clinical trial data from one device to be
used in the clinical evaluation of another device, provided that technical, biological, and clinical similarities between
the two devices can be demonstrated—see Annex XIV , PART A, (3) in [EU Regulation MDR, 2017].15 Ultimately, the
MDR requires that claims of device equivalence be supported by sound scientific reasoning, and that manufacturers
have adequate access to the reference device’s data to substantiate such claims. The problem is that identity criteria in
this and other regulations target products as a whole, not AI subsystems embedded as safety components. This generates
a mereological problem: since Baker’s seminal work on the ontology of artifacts [Baker, 2004], modern philosophy
treats constitution and identity as distinct relations, and the criteria for establishing the identity of a component need not
coincide with those of the whole they refer to [Gallois, 2016]. (For instance, identity criteria of water molecules are
different from identity criteria of rivers they are part of.) Further, even where regulations such as the MDR provide
proxies for synchronic identity under the notion of equivalence, these criteria rely heavily on expressions such as
“(essentially) similar”, and “same” with the effect of diluting definitional precision. Equivalence across technical,
biological, and clinical dimensions may be treated as a proxy for trustworthiness, but it remains an underspecified
criterion for AI synchronic identity, especially when combined with the mereological challenge mentioned above.
(Think about the ubiquitous use of open-source generative AI models in products and services, such as AI agents.)
In summary, synchronic identity matters whenever governance must decide whether compliance evidence, documen-
tation, monitoring signals, and corrective actions for one high-risk AI system instantiation legitimately generalize to
another instantiation at a given point in time, e.g., across certification scoping, traceability issues, incident response
cases, comparability issues with white-labeling, and procurement. While this is something other EU regimes handle via
grouping identifiers and “essential characteristics,” stand-alone high-risk AI lacks an equally auditable sameness crite-
rion under the AIA. Three recurring governance situations make the AIA’s synchronic identity gap practically salient.
Market surveillance and corrective-action propagation:when a serious incident, complaint, or non-compliance
finding concerns one stand-alone high-risk AI instantiation, authorities must decide whether mitigation, rollback,
user notification, or withdrawal obligations generalize to other contemporaneous instantiations marketed as “different”
systems.White-labeling and reseller variants:providers may distribute functionally comparable stand-alone high-risk
15Note that the term “equivalence” does not appear in the AIA. The adjective “equivalent” does, but it is not referred to synchronic
identity—e.g., it is used in the context of general AI systems with systemic risk, see Article 51 in the AIA.
14

System A
System B
Conformity Assessment
Question:do the systems
(1) have the same intended pur-
pose, and
(2) the same trustworthiness pro-
file?
Post-market Monitoring
Question:at time t, do the sys-
tems
have the same trustworthiness
level? The systems are the same system for reg-
ulatory purposes
The systemsare not
the same system for
regulatory purposes
yes
yes
no
no
no
Figure 2:Claim 2: Synchronic identity decision flow. Systems A and B are the “same” for regulatory purposes only if
they have the same intended purpose and trustworthiness profile at conformity assessment, and their trustworthiness
level matches at timetunder post-market monitoring.
systems under different product names, interfaces, or integration wrappers; without an auditable sameness criterion,
documentation and monitoring evidence can be fragmented across labels, undermining traceability and comparability.
Procurement and equivalence disputes:contracting authorities must decide whether two bids are substantively
comparable—for instance, whether a premium-priced variant is materially distinct or whether conformity evidence
and trustworthiness claims for one variant can be relied upon for another. (This is the case we explored in Section 2.)
Figure 2 makes this governance problem explicit: it represents a minimal audit workflow in which sameness claims
must be justified first at conformity assessment (purpose and profile) and then maintained under post-market monitoring
(trustworthiness level at timet). The figure also highlights when a regulatory non-sameness outcome obtains, making
the synchronic criterion operationally legible. Appendix 10 (Table 1) translates this decision flow into a minimal set
of auditable fields and indicates where each field should appear in AIA lifecycle artifacts. Concretely, SIfunction+
turns a sameness claim into a three-step audit question: do the systems share the same intended purpose, the same
trustworthiness profile, and the same trustworthiness level at the relevant time? If any of these elements fails, the
systems should not be treated as the same for regulatory comparability—see Figure 2. In summary, the function+
approach to synchronic identity and, in particular, criterionSIfunction+, provide the definitional precision needed to close
this gap in the AIA, anchoring the comparison of AI systems in techno-function, intended purpose, and requirements of
appropriate functioning. However, its utilization is conditional on the implementation of a few recommendations we
discuss in the following section.
9 Recommendations for Regulating AI System Identity
Through the use cases in Section 2, we showed that clarifying AI identity is key for effective governance. In Sections
7 and 8 we then argued that function+ aligns with the AIA’s lifecycle treatment of diachronic identity and supplies
a feasible approach for synchronic identity. However, its practical uptake is limited by underspecified components,
especially the precise statement of techno-function and intended purpose and the operationalization of measurable
trustworthiness profiles. Let us address these gaps, providing a few recommendations to improve the applicability
of function+ in the AI regulation domain. We refer to Appendix 10, Table 1, for a minimal checklist that maps
our recommendations to specific AIA artifacts (intended purpose statement, risk management file, and post-market
monitoring plan) and to the decision points in Figure 2.
15

9.0.1 Test and document high-risk AI system functions in relation to their intended purpose.
What is the function of a large language model-based conversational agent such as ChatGPT? In the sense relevant
to function+, the answer concerns itstechno-function: for paradigmatic large language models, this is next-token
prediction or autocompletion, operationalized as the generation of text continuations from prompts. This should be
distinguished from the system’sintended purposein the AIA sense, namely, the use for which the system is provided,
including its specific context and conditions of use. The same techno-function can support many intended uses: creating
poetry, summarizing documents, drafting code, assisting education, or producing administrative text. These uses may
differ in their social meaning, risk profile, user expectations, and regulatory relevance, even when the underlying
techno-function remains the same. This distinction matters for applying function+. The techno-function anchors the
identity of the AI kind; the intended purpose contextualizes that function for governance. Philosophy of technology
helps articulate this distinction by separatingtechno-functions(core technical operations),use-functions(practical
affordances for users), andsocial functions(societal roles emerging from interaction with the system) [Vermaas and
Houkes, 2003]. For instance, a conversational agent may have the techno-function of next-token autocompletion while
being used as a summarizer, a tutor, a therapist-like companion, or a “stern reviewer of scientific papers.” These
social functions affect the system’s societal impact and the vulnerability of its users and need to be considered in the
regulatory mechanism of the system’s identity: auditing of generative AI technology is a timely and complex challenge
[Mökander et al., 2025, 2024]. Thus, specifying the AI techno-function is necessary for anchoring system identity
over time, but it is not sufficient for regulating the effects of its deployment. Providers should therefore document both
the techno-function and the intended uses for which the system is offered, including context and conditions of use,
explicit exclusions, non-intended uses, and non-compliant uses. Governance bodies should encourage or require this
documentation in conformity assessment, post-market monitoring, and the assessment of substantial modifications.
Further, non-compliant intended uses should be enumerated and discussed as much as possible. A prominent class
of such non-compliant uses is promoted by the rise of AI anthropomorphization [Floridi and Nobre, 2024, Shanahan
et al., 2023, Ferrario et al., 2025, Akbulut et al., 2024, Ferrario et al., 2026]. Pre-market, this points to extensive social
role-sensitive testing; post-market, to guardrails that surface limits to users and reduce “social misattributions” due to
multi-purpose conversational and agentic affordances.
9.0.2 Promote standardization of contracts, conformity, post-market assessments, and trustworthiness
reporting.
In the absence of standardized reporting of trustworthiness contracts, assessments of AI identity may vary across EU
countries, and market surveillance authorities may struggle to determine whether functionally identical systems are truly
distinct or whether equivalent systems receive divergent regulatory treatment. Although it is not the goal of a regulation
such as the AIA to provide exhaustive details on trustworthiness contracts, conformity, and post-market assessments,16
the vagueness in interpretation of the levels of detail in these procedures may encourage exploiting ambiguity to avoid
re-assessment among organizations competing in the EU market. Providers may try to avoid excessive procedural
16Authors have already raised criticism against the material scope and other definitional ambiguities of the AIA—see, for instance,
Mökander et al. [2022], Nolte et al. [2025], Laux et al. [2024]. Furthermore, the requirements specified in Chapter III, Section 2
(Articles 8-15) in the AIA define context-independent obligations for high-risk AI systems. Finally, the contextualization of these
obligations, e.g., an employment opportunity domain vs. healthcare, should occur through the procedures and documentation that
constitute the conformity assessment and the guardrails in the post-market monitoring system and would further increase complexity.
16

t1
t0
Accuracy
Safety
(1,0)
(0,1)
1
2
3
Figure 3: Illustrative piecewise-constant trustworthiness levels over accuracy and safety. The system exhibits three
plateaus (high, medium, and low levels of trustworthiness). Small fluctuations within a plateau do not change the
overall system trustworthiness, as shown by the portion of the accuracy-safety curve betweent0 and t1. Conformity
re-assessment should be considered when a plateau boundary is crossed, e.g., a transition from level three (high) to two
(medium) occurs att 1.
burden and triggering of the conformity re-assessment disproportionately, a fact that would have a serious impact on
their system operations, incurring costs and important investment of resources to obtain a fresh conformity certification.
However, the idea that all permissible changes of a high-risk AI system’s components could be anticipated, analyzed
for the conformity assessment and assessed during post-market monitoring is practically untenable. These challenges
arise especially with generative AI-based systems, where intended use is vague, changes are hard to anticipate, and the
documentation burden may easily become prohibitive.
Thus, regulators should promote standardization of reporting practices for trustworthiness contracts, conformity, and
post-market monitoring, as in medical device regulation (e.g., structured post-market clinical follow-up templates
in the MDR) and cybersecurity certification (e.g., NIST SP 800-53 Rev. 5 control families). Developing analogous
templates and taxonomies for AI would require time, expert working groups, and iterative revision, but the earlier
such processes start, the more feasible they become. From the point of view of standardization, however, reliance on
trustworthiness contracts does not lead to an increase in complexity as they respond to AIA’s conformity assessment
requirements—see Section 7. Existing initiatives already point in this direction: ISO/IEC JTC 1/SC 42 has issued
standards on AI lifecycle management17 and CEN/CENELEC JTC 21 is developing harmonized standards in support
of the AI Act. 18 However, we argue that regulating AI identity based on contracts individually and the changes
affecting them is both inefficient and prone to over-sensitivity: small deviations in any of the dimensions constituting
AI trustworthiness may trigger unnecessary regulatory alerts. What matters is not each component in isolation but the
system’s overall capacity to remain worthy of trust at a given point in time, as suggested by function+’s treatment
17https://www.iso.org/committee/6794475.html
18https://jtc21.eu/
17

of AI trustworthiness levels—see DIfunction+ and SIfunction+. In other regulated domains, this challenge is addressed
through composite or global assessments: cars receive ‘roadworthiness’ certificates (e.g., Euro NCAP star ratings)
that condense numerous safety checks into a single judgment; similar considerations hold for other machinery, such
as aircraft, as well as medical devices (e.g., ISO 14971 risk indices integrating performance, safety, and usability).
By analogy, the standardization of trustworthiness reporting for AI should move toward specifying an aggregated
perspective, namely a trustworthiness level function integrating dimensions such as accuracy, safety, robustness, fairness,
and explainability into a composite indicator. Thus, a temporary decline in one dimension could be tolerable if others
remain high, but sustained or joint reduction would indicate a degradation in trustworthiness and an end to the AI
system’s persistence and the triggering of a new conformity assessment. A practical, but non-exclusive, way to model
AI trustworthiness levels is with multi-dimensional piecewise-constant functions that map regions of the metric space
of trustworthiness-relevant dimensions (e.g., accuracy, safety, and transparency) to a finite number of trustworthiness
plateaus. These simple and interpretable functions can be learned by classification and regression trees, providing a
data-driven approach to the standardization of AI trustworthiness reporting. Figure 3 provides an illustration. Here, what
matters is that the chosen trustworthiness level function, including its dimensions, thresholds, aggregation rules, and
robustness to reasonable multidimensional variation, is explicitly justified and auditable. On the one hand, as part of the
conformity assessment, providers should disclose how the trustworthiness-level function is derived, including a detailed
description of training data.19 Weightings, metric choices, and aggregation rules for trustworthiness-level functions
are not assumed to be universal: they are context- and designer-dependent, reflecting domain-specific risk priorities,
stakeholder expectations, and operational constraints. Rabanser et al. [2026] illustrate this approach in the context of
AI agents by identifying relevant trustworthiness dimensions, e.g., robustness and safety, operationalizing them via
concrete measures, aggregating them into a composite assessment, and employing the resulting scoring scheme in
empirical studies that include established benchmarks. On the other hand, as part of standardization efforts, governance
bodies can adopt such metrics as part of standardized post-market monitoring, reducing opportunities for providers
to exploit loosely specified regulations to avoid new conformity assessments and making substantial modifications
auditable in practice.
What matters for governance is that these choices areexplicitly declared and justifiedin a standardized, comparable
format, so that oversight bodies can audit trade-offs consistently across providers and track them over time.
10 Conclusions
The AIA is the most ambitious attempt so far to regulate AI in Europe. By requiring conformity assessments, substantial
modification checks, and post-market monitoring, it implicitly commits to a position on the diachronic identity of AI
systems. Yet, it leaves synchronic identity unaddressed, except by reference to sectoral legislation. This asymmetry
risks creating regulatory blind spots in procurement, liability, and market surveillance. We argued that thefunction+
framework can fill this gap, providing both identity criteria within a single frame, clarifying intended purpose,
trustworthiness commitments, and measurable indicators for conformity and monitoring. As a result, it provides a
metaphysical framework for the AIA’s lifecycle approach while supplying the missing criteria for synchronic cases.
The philosophical analysis proposed in this work is a conceptual and auditing lens that can help make identity-relevant
19Alternatives are possible: rule-based specifications or a scoring scheme. Similar considerations on reporting apply.
18

determinations in high-risk AI system lifecycle documentation transparent and contestable within the AIA framework.
It does not replace legal interpretation, technical standards, conformity assessment procedures, or empirical validation:
it helps make identity-relevant determinations in high-risk AI system lifecycle documentation more explicit, transparent,
and contestable within the AIA framework. Clarifying identity conditions of AI systems helps make legal obligations
enforceable, procurement fair, and accountability tractable across traceability and comparability issues, and incident
responses. As generative and agentic AI proliferate across domains, metaphysical clarity will be needed for the
governance of the technologies that increasingly shape our societies.
Acknowledgments
The author acknowledges partial support by the Swiss National Science Foundation (SNSF), grant no. 229061. The
author thanks Michele Loi for insightful comments on a preliminary version of this work.
19

Appendix
Minimal audit checklist for synchronic identity
Table 1 displays minimal auditable content for synchronic identity (Claim 2) and its placement in AIA artifacts. The
table operationalizes Figure 2 as a checklist for audit, procurement, and dispute contexts.
Table 1: Minimal auditable content for synchronic identity (Claim 2) and its placement in AIA artifacts. The table
operationalizes Figure 2 as a checklist for audit, procurement, and dispute contexts.
Decision point AIA artifact (where) Minimal auditable fields (what)
D1: Intended pur-
pose match
Annex IV technical docu-
mentation; instructions for
use
Declared intended purpose; context and conditions of use; target population;
deployment constraints; explicit exclusions / non-intended uses; stated de-
pendencies on environment assumptions (e.g., sensors, latency constraints,
human oversight conditions).
D2: Trustworthi-
ness profile match
Annex IV (metrics and jus-
tification); risk management
documentation
Trustworthiness dimensions claimed (e.g., robustness, safety, fairness, trans-
parency); operational definitions and metrics; evaluation protocols and
datasets; acceptance thresholds; aggregation rule (incl. weightings) with
justification; known limitations and trade-offs.
D3: Trustworthi-
ness level match at
timet
Post-market monitoring plan
and records; change logs
Current measured levels at time t (per D2 metrics); monitoring cadence;
drift/degradation indicators and triggers; incident history relevant to the
profile; version/configuration identifiers; evidence that the level uses the
same aggregation rule as in D2.
Outcome: “same”
for regulatory com-
parability
Audit / procurement / surveil-
lance file
Explicit rationale that D1–D3 are satisfied; scope of evidence portability
(what can be re-used: tests, documentation, corrective actions); validity
window and re-check triggers.
Outcome: “not
same” for regula-
tory comparability
Audit / procurement / surveil-
lance file
Failure point (D1, D2, or D3) and evidence; implication statement: compli-
ance evidence does not generalize; required next step (separate assessment
scope, additional documentation, or separate monitoring).
20

References
Canfer Akbulut, Laura Weidinger, Arianna Manzini, Iason Gabriel, and Verena Rieser. All too human? Mapping
and mitigating the risk from anthropomorphic AI. InProceedings of the AAAI/ACM Conference on AI, Ethics, and
Society, volume 7, pages 13–26, 2024.
Pekka Ala-Pietilä, Yann Bonnet, Urs Bergmann, Maria Bielikova, Cecilia Bonefeld-Dahl, Wilhelm Bauer, Loubna
Bouarfa, Raja Chatila, Mark Coeckelbergh, Virginia Dignum, et al.The Assessment List for Trustworthy Artificial
Intelligence (ALTAI). European Commission, 2020.
Lynne Rudder Baker. The ontology of artifacts.Philosophical Explorations, 7(2):99–111, 2004.
Anu Bradford.The Brussels Effect. Oxford University Press, Oxford, UK, 2020.
Massimiliano Carrara and Pieter E Vermaas. The fine-grained metaphysics of artifactual and biological functional kinds.
Synthese, 169(1):125–143, 2009.
Crawford L Elder.Real natures and familiar objects. The MIT Press, 2004.
EU AI Act. Regulation (EU) 2024/1689 of the European Parliament and of the Council of 13 June 2024 laying
down harmonised rules on artificial intelligence. Technical report, European Union, June 2024. URL https:
//eur-lex.europa.eu/eli/reg/2024/1689/oj.
EU AI HLEG. Ethics Guidelines for Trustworthy AI. Technical report, European Commission, April 2019. URL
https://digital-strategy.ec.europa.eu/en/library/ethics-guidelines-trustworthy-ai.
EU Cyber Resilience. Regulation (EU) 2024/2847 of the European Parliament and of the Council of 23 October 2024
on horizontal cybersecurity requirements for products with digital elements (Cyber Resilience Act). Official Journal
of the European Union L 2847, European Union, November 2024. URL https://eur-lex.europa.eu/eli/
reg/2024/2847/oj.
EU Declaration Digital Rights. European declaration on Digital Rights and Principles for the Digi-
tal Decade. Technical report, 2022. URL https://digital-strategy.ec.europa.eu/en/library/
european-declaration-digital-rights-and-principles.
EU Directive Medicinal Products. Directive 2001/83/EC of the European Parliament and of the Council of 6 November
2001 on the Community code relating to medicinal products for human use. Technical Report 2001/83/EC, November
2001. URLhttps://eur-lex.europa.eu/eli/dir/2001/83/oj/eng.
EU Machinery Regulation. Regulation (EU) 2023/1230 of the European Parliament and of the Council of 14 June
2023 on machinery and repealing Directive 2006/42/EC of the European Parliament and of the Council and Council
Directive 73/361/EEC (Text with EEA relevance). Official Journal of the European Union L 165, European Union,
June 2023. URLhttps://eur-lex.europa.eu/eli/reg/2023/1230/oj.
EU Regulation MDR. Regulation (EU) 2017/745 of the European Parliament and of the Council of 5 April 2017
on medical devices, amending Directive 2001/83/EC, Regulation (EC) No 178/2002 and Regulation (EC) No
1223/2009 and repealing Council Directives 90/385/EEC and 93/42/EEC. Technical report, April 2017. URL
https://eur-lex.europa.eu/eli/reg/2017/745/oj/eng.
Andrea Ferrario. A trustworthiness-based metaphysics of artificial intelligence systems. InProceedings of the 2025
ACM Conference on Fairness, Accountability, and Transparency, pages 1360–1370, 2025.
21

Andrea Ferrario, Alberto Termine, and Alessandro Facchini. Social misattributions in conversations with large language
models. InProceedings of the AAAI/ACM Conference on AI, Ethics, and Society, volume 8, pages 913–925, 2025.
Andrea Ferrario, Rasita Vinay, Matteo Casserini, and Alessandro Facchini. A scoping review of the ethical perspectives
on anthropomorphising large language model-based conversational agents. InProceedings of the 2026 ACM
Conference on Fairness, Accountability, and Transparency, FAccT ’26, pages 3626–3650, New York, NY , USA,
2026. Association for Computing Machinery.
Luciano Floridi. The European legislation on AI: A brief analysis of its philosophical approach.Philosophy &
Technology, 34(2):215–222, 2021.
Luciano Floridi and Anna C Nobre. Anthropomorphising machines and computerising minds: The crosswiring of
languages between artificial intelligence and brain & cognitive sciences.Minds and Machines, 34(1):5, 2024.
A. Gallois.The Metaphysics of Identity. Routledge, 2016.
Katherine Hawley. Trust, distrust and commitment.Noûs, 48(1):1–20, 2014.
Calvin Wai-Loon Ho and Karel Caals. How the EU AI act seeks to establish an epistemic environment of trust.Asian
Bioethics Review, 16(3):345–372, 2024.
Alon Jacovi, Ana Marasovi´c, Tim Miller, and Yoav Goldberg. Formalizing trust in artificial intelligence: Prerequisites,
causes and goals of human trust in AI. InProceedings of the 2021 ACM Conference on Fairness, Accountability, and
Transparency, pages 624–635, 2021.
Davinder Kaur, Suleyman Uslu, Kaley J Rittichier, and Arjan Durresi. Trustworthy artificial intelligence: A review.
ACM Computing Surveys, 55(2):1–38, 2022.
Emre Kazim, Osman Güçlütürk, Denise Almeida, Charles Kerrigan, Elizabeth Lomas, Adriano Koshiyama, Airlie
Hilliard, and Markus Trengove. Proposed EU AI Act—Presidency compromise text: Select overview and comment
on the changes to the proposed regulation.AI and Ethics, 3(2):381–387, 2023.
Johann Laux, Sandra Wachter, and Brent Mittelstadt. Trustworthy artificial intelligence and the European Union AI
Act: On the conflation of trustworthiness and acceptability of risk.Regulation & Governance, 18(1):3–32, 2024.
Bo Li, Peng Qi, Bo Liu, Shuai Di, Jingen Liu, Jiquan Pei, Jinfeng Yi, and Bowen Zhou. Trustworthy AI: From principles
to practices.ACM Computing Surveys, 55(9):1–46, 2023.
Michele Loi, Christoph Heitz, Andrea Ferrario, Anita Schmid, and Markus Christen. Towards an ethical code for
data-based business. In2019 6th Swiss Conference on Data Science (SDS), pages 6–12. IEEE, 2019.
Michele Loi, Matteo Fabbri, and Andrea Ferrario. Regulating the undefined: Addressing systemic risks in the digital
services act (with an appendix on the AI Act).Philosophy & Technology, 38(2):1–29, 2025.
E. J. Lowe. How real are artefacts and artefact kinds? In Maarten Franssen, Peter Kroes, Thomas A. C. Reydon, and
Pieter E. Vermaas, editors,Artefact Kinds: Ontology and the Human-Made World, pages 17–26. Springer, 2014.
Juliette Mattioli, Henri Sohier, Agnès Delaborde, Kahina Amokrane-Ferka, Afef Awadid, Zakaria Chihani, Souhaiel
Khalfaoui, and Gabriel Pedroza. An overview of key trustworthiness attributes and KPIs for trusted ML-based
systems engineering.AI and Ethics, 4(1):15–25, 2024.
22

Jakob Mökander and Luciano Floridi. Ethics-based auditing to develop trustworthy AI.Minds and Machines, 31(2):
323–327, 2021.
Jakob Mökander, Maria Axente, Federico Casolari, and Luciano Floridi. Conformity assessments and post-market
monitoring: A guide to the role of auditing in the proposed European AI regulation.Minds and Machines, 32(2):
241–268, 2022.
Jakob Mökander, Jonas Schuett, Hannah Rose Kirk, and Luciano Floridi. Auditing large language models: A three-
layered approach.AI and Ethics, 4(4):1085–1115, 2024.
Jakob Mökander, Justin Curl, and Mihir Kshirsagar. A blueprint for auditing generative AI. InResearch Handbook on
the Law of Artificial Intelligence, pages 307–327. Edward Elgar Publishing, 2025.
Henrik Nolte, Miriam Rateike, and Michèle Finck. Robustness and cybersecurity in the EU Artificial Intelligence Act.
InProceedings of the 2025 ACM Conference on Fairness, Accountability, and Transparency, pages 283–295, 2025.
Eric T. Olson. Personal identity. In Edward N. Zalta and Uri Nodelman, editors,The Stanford Encyclopedia of
Philosophy. Metaphysics Research Lab, Stanford University, Stanford, CA, winter 2024 edition, 2024. URL
https://plato.stanford.edu/archives/win2024/entries/identity-personal/.
Nicolas Petit.Big Tech and the Digital Economy. Oxford University Press, Oxford, UK, 2020.
Charles C. Pinter.A Book of Set Theory. Dover Publications, Mineola, NY , 2014.
W. V . O. Quine.Ontological Relativity and Other Essays. Columbia University Press, New York, 1969.
Stephan Rabanser, Sayash Kapoor, Peter Kirgis, Kangheng Liu, Saiteja Utpala, and Arvind Narayanan. Towards a
science of AI agent reliability.arXiv preprint arXiv:2602.16666, 2026.
Murray Shanahan, Kyle McDonell, and Laria Reynolds. Role play with large language models.Nature, 623(7987):
493–498, 2023.
Nathalie A Smuha, Emma Rengers, Adam Harkens, Wenlong Li, James MacLaren, Riccardo Piselli, and Karen Yeung.
How the EU can achieve legally trustworthy AI: A response to the European Commission’s proposal for an Artificial
Intelligence Act.SSRN Electronic Journal, August 2021. doi: 10.2139/ssrn.3899991.
Pieter E Vermaas and Wybo Houkes. Ascribing functions to technical artefacts: A challenge to etiological accounts of
functions.The British Journal for the Philosophy of Science, 54(2):261–289, 2003.
David Wiggins.Sameness and Substance Renewed. Cambridge University Press, Cambridge, 2001.
Manuel Wörsdörfer. The EU’s Artificial Intelligence Act: An ordoliberal assessment.AI and Ethics, 5(1):263–278,
2025.
Roberto V Zicari, John Brodersen, James Brusseau, Boris Düdder, Timo Eichhorn, Todor Ivanov, Georgios Kararigas,
Pedro Kringen, Melissa McCullough, Florian Möslein, et al. Z-inspection®: A process to assess trustworthy AI.
IEEE Transactions on Technology and Society, 2(2):83–97, 2021.
23
