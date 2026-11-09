---
title: 'Enhancing Trust in Inter-Organisational Data Sharing: Levels of Assurance for Data Trustworthiness'
url: https://arxiv.org/abs/2503.24149
category: consumer-behavior
subcategory: empirical
date: 2025-03
venue: ''
authors:
- Florian Zimmer
- Janosch Haber
- Mayuko Kaneko
source: arxiv
pdf_url: https://arxiv.org/pdf/2503.24149
pages: 13
chars: 58823
fetched_at: '2026-11-08T13:09:45+00:00'
kb_version: 1
---

# Enhancing Trust in Inter-Organisational Data Sharing: Levels of Assurance for Data Trustworthiness

ENHANCING TRUST IN INTER -ORGANISATIONAL DATA SHARING :
LEVELS OF ASSURANCE FOR DATA TRUSTWORTHINESS
A PREPRINT
Florian Zimmer1,
 Janosch Haber2, and
 Mayuko Kaneko3
1Fraunhofer Institute for Software and Systems Engineering ISST, Speicherstraße 6, Dortmund, 44147, Germany
2Fujitsu Research of Europe, 9 Albert St, Slough SL1 2BE, United Kingdom
3Fujitsu Limited, 4-1-1 Kamikodanaka, Nakahara-ku, Kawasaki, Kanagawa 211-8588, Japan
ABSTRACT
As data is increasingly acknowledged as a highly valuable asset, much effort has been put into
investigating inter-organisational data sharing, aiming at utilising the value of formerly unused data.
Moreover, most researchers agree, that trust between actors is key for successful data sharing activities.
However, existing research oftentimes focus on trust from a data provider perspective. Therefore,
our work highlights the unbalanced view of trust, addressing it from a data consumer perspective.
More specifically, our aim is to investigate trust enhancing measures on a data level, that is data
trustworthiness. We found, that existing data trustworthiness enhancing solutions do not meet the
requirements of the domain of inter-organisational data sharing. Therefore, our study addresses this
gap. Conducting a rigorous design science research approach, this work proposes a new Levels
of Assurance for Data Trustworthiness artifact. Built on existing artifacts, we demonstrate, how
it addresses the identified challenges within the domain appropriately. We found that our novel
approach requires more work to be suitable for adoption. Still, we are confident that our solution
can increase consumer trust. We conclude by contributing to the body of design knowledge and
emphasise the need for more attention to be put into consumer trust.
Keywords Data Trustworthiness, Levels of Assurance, Inter-Organisational Data Sharing, Trust, Data Spaces, Design
Science Research.
1 Introduction
The increasing adoption of information driven technology across industries, and its integration in nearly every aspect of
life, are highlighting the ever-growing importance of data. Data is considered a central driver in the acceleration of
digital transformation [32]. Consequently, the European Data Strategy1 was proposed by the European Commission in
2020, acknowledging data as an essential asset for innovation and growth in businesses and societies as a whole. As a
result, inter-organisational data sharing has gained much attention in academia and industry recently, aiming to unlock
the full potential of previously unused and under-utilised data [39].
However, organisations are often hesitant when engaging in data sharing activities. A number of barriers prevent a
more wide-spread adoption of inter-organisational data sharing, with a lack of trust and transparency between actors
mentioned as one of the most fundamental barriers [24]. A main source for the lack of trust in inter-organisational data
sharing, mentioned in research, are challenges to data sovereignty, i.e., the concern of data providers to lose control
over their data once shared with other organisations [42].
In order to address these concerns, the concept of data spaces has emerged to provide a framework for data sharing,
establishing data sovereignty, by enabling mutual trust in the interoperable data exchange between data providers and
consumers [32]. However, the issue of trust here is predominantly considered from the perspective of the data provider.
We found, that approaches often aim at preventing the loss of corporate knowledge or sensitive information [6, 17], or
1https://commission.europa.eu/strategy-and-policy/priorities-2019-2024/europe-fit-digital-age/
european-data-strategy_en [Accessed 30.03.2025]
arXiv:2503.24149v1  [cs.SI]  31 Mar 2025

Levels of Assurance for Data Trustworthiness A PREPRINT
the security of the data exchange itself [17, 38] - but rarely mention the consumer’s risks and their need for trust in data
providers and the data made available by them [32, 39].
Contrarily, in the ISO/IEC 15408-1 standard for information security, data, or more specifically information consumers
are also referred to as risk owners, as they are confronted with the potential risks resulting from data providers taking
insufficient measures to assure data integrity [ 21]. Because data is becoming so essential for decision making [ 9],
leveraging (un-)intentionally modified, incomplete, or compromised data exposes data consumers to potentially severe
consequences from financial losses up to human harm [11]. Still, data consumers usually have no other option than to
trust data providers, as data trustworthiness cannot be established otherwise [1, 37].
In this paper, we argue that trust in inter-organisational data sharing should not be limited to the organisational level
but must also encompass the trustworthiness of the data itself. Following a rigorous design science research (DSR)
approach, we review the literature on data trustworthiness across various domains and identify challenges in ensuring it
in complex sharing scenarios.
As a result, we adopt a multi-dimensional view of the problem and solution space and develop a novel artifact, aiming at
addressing the shortcomings of existing artifacts. We introduce the groundbreaking concept of Levels of Assurance for
Data Trustworthiness, or Data LoA, which offers new means of enhancing trust and transparency among data providers
and data consumers - including additional data assurances to enhance trust for data consumers. In this first iteration, we
aim to build a foundational model, outlining key actors and their interactions. Furthermore, an instantiating artifact is
presented in the form of a proof of concept (PoC) implementation, demonstrating the LoA concept from a technical
data sharing perspective. Our main contributions include:
(i) Compiled design knowledge, identifying existing work and mapping the problem and solution space
(ii) A novel Data LoA artifact, aiming at enhancing data consumer trust
(iii) An experimental proof of concept, showcasing the practical application of the Data LoA
The remainder of this paper is structured as follows: in Section 2, we touch upon relevant related work. Section 3
outlines the research methodology followed in this study. Section 4 presents the design knowledge and objectives
derived from the literature review, and proposes the concept of Data LoA as an artifact. In Section 5, we discuss
implications as well as limitations and touch points for future work. Section 6 concludes the paper with a brief summary.
2 Related Work
2.1 Data Trustworthiness
The trustworthiness of data has been extensively studied across various domains and applications such as healthcare,
defence, traffic control, and manufacturing [11]. The main concentration of work on data trustworthiness however is in
the contexts of internet of things (IoT) and mobile crowd sensing (MCS) - both areas, that face the challenges of an
unknown, potentially insecure network of known and unknown actors.
Data trustworthiness is usually described as the possibility to ascertain the correctness of data provided by a data source
[13]. Yet, a high degree of context and domain dependency have prevented the formulation of a generally accepted
notion of data trustworthiness so far [5, 35, 43]. Circumnavigating a holistic definition, literature oftentimes mentions
and focuses on specific dimensions of data trustworthiness; most commonly data availability, quality, security, and
compatibility - each of which concerned with a number of different aspects themselves [43].
With many different approaches to assure, measure, and define data trustworthiness existing, [23] proposed a taxonomy
for artifacts in IoT. The taxonomy mainly groups them by conceptual trust definitions, mathematical models, or trust
frameworks. For instance, [31] present a trust assessment canvas to gauge the trustworthiness of publicly available
medical data. [10] on the other hand, present a trust score model capable of measuring the trustworthiness of industrial
IoT data sources. Furthermore, [27] propose a trust enhancing framework for data traceability in the context of food
supply chains.
Based on this, some researchers argue that the variety of different approaches and notions, prevents a development of a
comprehensive solution to assure data trustworthiness [5, 7]. Therefore, [13] argues that a combination of different
techniques is required, in order to meet the requirements of data consumers, highlighting the need for overarching
solutions.
2

Levels of Assurance for Data Trustworthiness A PREPRINT
2.2 Levels of Assurance
Levels of Assurance (LoA) refer to the degree of confidence that can be assigned to some kind of entity, process, or
system acting or operating as claimed [ 20]. LoAs are an assurance technique, used to evaluate and grade complex
scenarios, simplifying and improving decision making and risk management [ 30]. More formally, a relying party
utilises provided LoA information to determine their level of confidence in the credibility of aclaimant’s claim. Usually,
there is at least one other party involved, namely the assurance provider, which audits and assures the claimant’s claim
[29, 20]. If there is no external assurance provider, claims are self-asserted.
LoAs are mainly used in the domain of identity validation, for example in the ISO/IEC 291152 standard, the eIDAS3
regulation as proposed by the European Commission, or the NIST 800-63-A 4 guidelines. The concrete LoA levels
define the processes, management activities, and technologies needed in order to establish different levels of confidence
in the claimed identity. Nonetheless, LoAs are also adopted widely within other domains, such as the ISO 26262-35
standard for automotive safety or the CSA STAR6 program for cloud security.
LoAs are usually risk-based, defining which dimensions of risk must be addressed and mitigated in order to assure
the credibility of a claim. Hence, the higher the perceived risk for the relying party, the higher the required level of
confidence in the claim’s validity, and thus the LoA should be [29, 20]. A comprehensive LoA concept should guide
the claimant on how to mitigate risks, while providing the relying party with assurances needed for informed decision
making.
Besides providing risk management capabilities, the eIDAS regulation also mentions improving trust among adopters.
They achieve this by providing assurances of audited identification techniques and clearly defining liabilities to specify
each party’s responsibilities. Therefore, commonly used identification techniques are certified at different LoAs within
eIDAS. This provides standardised assurances relevant for assessments of mutual trust, that enable interoperability in
the heterogeneous identification techniques landscape of the EU [8].
3 Methodology
This paper aims to address the lack of trust enhancing means for data consumers in inter-organisational data sharing.
More specifically, we address the assurance of the trustworthiness of data by designing a new artifact for Levels of
Assurance for Data Trustworthiness (Data LoA). The ultimate goal of this artifact is twofold: on the one hand, it aims
to provide data consumers with risk assessment capabilities. On the other, it equips data providers with standardised
principles on how to establish different degrees of data trustworthiness assurances. Together, these mechanisms are
aimed at enhancing trust in inter-organisational data sharing and enabling interoperability among existing trust assuring
solutions.
To develop our artifact, we conducted a rigorous DSR approach, following [33]. More specifically, we followed an
objective-centred approach. This is based on our finding, that a range of data trustworthiness assuring artifacts already
exist. Yet, they fail to provide comprehensive means of assuring trust in the broader context of inter-organisational data
sharing in a standardised, interoperable manner.
Furthermore, we found that previous artifacts were not necessarily developed following DSR. Thus, current literature
does not provide a sound foundation of design knowledge to build upon on. We therefore started by identifying the
relevant problem and solution space, specifying the challenges, motivations, and goals addressed by existing artifacts.
We did so by following a rigorousstructured literature review (SLR)as described by [40], deriving design knowledge by
empirical means. According to the authors, literature reviews are a proven method on justifying the novelty of design
ideas, as well as informing the design process. The SLR process is pictured in Figure 1.
Therefore, as suggested by [40], we first started with an unstructured exploration of relevant literature, mainly using
Google Scholar, in order to increase the familiarity with the subject. Then, we continued with a structured keyword
search in the IEEExplore, ACM, and ScienceDirect databases. These resources were chosen due to their importance in
the first stage, as well as their relevance to related subjects, and coverage of adjacent fields. We used the search term
("Data" AND ("Trustworthiness" OR "Trustworthy")), matching titles in research articles only to narrow down the scope
and improve the relevance of matches. We executed the search in December 2024, which returned 318 matches. 148 of
2https://iso.org/standard/45138.html [Accessed 30.03.2025]
3https://digital-strategy.ec.europa.eu/en/policies/eidas-regulation [Accessed 30.03.2025]
4https://pages.nist.gov/800-63-3/sp800-63a.html [Accessed 30.03.2025]
5https://iso.org/standard/68385.html [Accessed 30.03.2025]
6https://cloudsecurityalliance.org/star [Accessed 30.03.2025]
3

Levels of Assurance for Data Trustworthiness A PREPRINT
Exploratory Pre-Study
Keyword-based Search n = 318
Title Screenlining n = 177
Abstract Screenlining n = 47
Back- and Forward Search n = 62
Figure 1: Conducted literature search approach.
these came from IEEExplore, 121 from ACM, and 49 from ScienceDirect. We screenlined these articles’ titles and
removed unequivocal false positives, which resulted in 177 articles that were more thoroughly investigated.
We then excluded articles that were not related to measuring, evaluating, or assuring the trustworthiness of data. This
resulted in a total of 47 articles. Using this collection, we conducted backward and forward searches by thoroughly
reading each article, looking for key references, and using Google Scholar to execute a targeted forward search.
According to [40] back- and forward searches are a good way to ensure sufficient coverage of relevant literature. Doing
this left us with an additional 35 articles, 20 of which were already part of our set of identified literature. Thus, we
ended up with a total of 62 articles to consider.
After analysis of these articles, we empirically derived design knowledge for two topics: i) challenges and motivations
for means to measure or assure data trustworthiness, and ii) common objectives of existing artifacts. We did this in
order to ground the relevancy of our to be designed artifact and guide our develop and design efforts by goals often
followed. Doing this provides a strong foundation to build a new artifact on top of, facilitating existing research, as also
highly suggested by [41].
We continued our DSR objective-centred approach as pictured in Figure 2 by posing the leading question, as suggested
by [33]: What would a better artifact accomplish? To address this question, we derived and selected a set of design
objectives aligned with our overall goal of enhancing data trustworthiness in inter-organisational data sharing, and used
these objectives to guide the development of our artifact. As we have been already familiar with the concept of LoAs
for identity validation, it quickly became evident that LoAs serve a similar purpose. Thus, we used them as foundation
to build upon on, adjusting the design goals accordingly.
Based on this, a cross-functional team of researchers and practitioners developed the Data LoA artifact. Doing this,
we mainly focused on defining central actors as well as their relations, in order to establish a sound foundation for
future iterations to build on top of. We therefore did not define specific levels yet, as a lack of a common notion of data
trustworthiness made it hard to specify them at this early stage.
Step 1
Define
Objectives
Step 2
Design &
Develop-
ment
Step 3
Demon-
stration
Step 4
Evaluation
Step 5
Communi-
cation
Figure 2: The objective-centred DSR approach following [33] applied in this study.
We then proceeded with evaluating our artifact by instantiating a PoC in the context of data spaces, which was deemed to
be a relevant and informative domain for investigating trust effects in inter-organisational data sharing. By conducting an
experimental simulation, the PoC allowed us to assess the technical feasibility of our concept and determine limitations
and considerations for future work. The communication step, as proposed by [ 33], is performed by publishing this
paper.
4 Results
The aim of this paper is to create a new trust enhancing technique that addresses the lack of trust from a consumer
perspective in inter-organisational data sharing. To do so, we adopted an objective-centred DSR approach to develop an
artifact based on design knowledge of existing literature. Therefore, we first identify both problem and solution space
by conducting a literature review in order to derive such design knowledge, following [41]. Based on this, we derive
design objectives stipulated by existing solutions, and describe and demonstrate our resulting artifact.
4

Levels of Assurance for Data Trustworthiness A PREPRINT
4.1 Design Knowledge & Grounding
Adopting an objective-centred approach comes with the assumption, that the problem space is already well-defined and
investigated in literature [33]. Therefore, we conducted a SLR in order to extract and derive existing design knowledge,
in order to build our artifact upon on. The domain distribution of the 62 investigated articles can be seen in Figure 3. It
is apparent that most of the data trustworthiness related studies were conducted in the broader area of IoT, as well as
Web & Cloud. The commonalities in regards to the problem space, thus acknowledged problems and motivation, are
described in the following. For brevity, only key literature is referenced. A full overview of considered articles, as well
as a detailed overview of the derived clusters can be found in [44].
IoT 53.2%
Web & Cloud 16.1%
Data Management 14.5%
Other 9.7% CPS 6.5%
Figure 3: The domain distribution of the 62 investigated articles.
Undeterminable Risk. A major issue and motivation for enhanced trust in data are undeterminable risks. Most studies
agree that consuming untrustworthy data, i.e., data for which trustworthiness is not assured, is linked to great risks.
According to [13, 25] this is because data is usually utilised for some form of decision making. The reliability and
accuracy of this decision making therefore is greatly influenced by the data that it is grounded on. Consequently,
using untrustworthy data can lead to severe consequences - as incidents in healthcare or power supply have previously
demonstrated [22, 28]. Ensuring data trustworthiness is therefore primarily motivated by better risk management
capabilities, where, e.g., low trustworthy data will only be used for low risk applications.
Challenging Complexity. Many previous papers argue that assuring and measuring data trustworthiness is a complex
and challenging task. According to [ 5], e.g., addressing the different facets of data trustworthiness also requires a
complex combination of different approaches and techniques. [13] further emphasise this by reflecting on the complexity
added by heterogeneous IoT environments, and [ 34] recognise data trustworthiness in the context of MCS as key
challenge. What is more, data trustworthiness measuring techniques often incorporate an array of individual metrics to
compile a final trust score. In a concrete example, [26] employ multiple trust metrics such as device malfunction, data
tampering, and battery problems to measure and determine trustworthiness.
Increasing Demand. At different points in time, studies have emphasised the growing need for trustworthy data as
well as assurance and quantification means. For instance, [5] states that “[...] today’s demand for data trustworthiness is
stronger than ever. As many organizations are increasing their reliance on data for daily operations and critical decision
making, data trustworthiness is arguably one of the most critical issues.” More recently, [19] suggest trust estimation of
data as one way to tackle the growing challenges of data related risks and vulnerabilities, and [3] highlight the growing
need for trustworthy data for use in artificial intelligence (AI).
Success Factor .Another widely acknowledged fact in literature is, that establishing and ensuring data trustworthiness is
a major driver for success. Although this is closely related to the problem of undeterminable risk, it is often emphasised
as integral part of the motivation for adopting trust ensuring solutions. For example, [2] argue, that data is useless if it
cannot be trusted and that it is a key to success. This is in line with [4] stating, that system automation is assuming data
to be trustworthy, which if failed to meet, results in wrong untrusted services. On top of that, the authors claim the
higher the trustworthiness of the data, the higher the decision accuracy. This is further emphasised by [25] which state
that trustworthy data is increasing the reliability of applications. [4] also found, that decisions need to be verifiable in
order to provide accountability of e.g. autonomous systems. Therefore they argue, that trustworthy data is necessary to
ensure this.
4.2 Design Objectives
In order to define our design objectives, it is imperative that prior research is investigated, thus the solution space is
outlined. Therefore, based on our SLR, we identified 51 previous artifacts concerned with enhancing data trustworthiness.
Building on top of [23], the following four categories were used in order to classify the identified artifacts: conceptual,
mathematical, architectural, and framework. The resulting distribution is pictured in Figure 4.
We found that although there are many artifacts already, especially in the domain of IoT, most of the existing artifacts
were not yet at a stage at which they can be easily adopted, with the majority of papers describing artifacts on a
theoretical level. Most artifacts do however have common goals, upon which we based our design objectives. They are
described in the following.
5

Levels of Assurance for Data Trustworthiness A PREPRINT
Mathematical
42.9% Framework
28.6%
Architectural
16.3%
Conceptual
12.2%
Figure 4: The artifact distribution of the 51 investigated artifacts, partially following [23].
Decrease Risk. A central part of the identified problem space are the risks related to using data for which no assumptions
about the trustworthiness can be made. This factor has been addressed by a number of existing artifacts. One way of
mitigating this is by providing the consumer with enhanced decision making capabilities, for example by explicitly
communicating additional information. [36] for instance suggest to provide consumers in an IoT network with the ID
of participating nodes, timestamps and the data flow, which were involved in the creation as well the transfer of the data.
Based on this, the consumer is enabled to estimate whether the perceived risk of using this data is at an acceptable level.
This is in line with [10] which proposed a model in order to compile the quality of data sources, data storage, and the
data provider into a trust score ranging from 0 to 1.
Therefore, this way of decreasing risk aims at the consumer to avoid using data which might not be appropriate for their
use-case. This approach however requires the consumer to have an in-depth understanding of how different techniques
and pieces of information relate to what degree of risk. This is further emphasised by [13], who argue that most trust
models leave it up to the user to decide whether the provided trustworthiness assessment, represented either as binary
state, or a range of values, is appropriate for them.
Consequently, another way of decreasing risk is by directly employing concrete measurements. This is to ensure, that
different risks are mitigated right at the source or before they even reach the consumer. For example, [ 37] propose
a secure data collection scheme, which aims to enhance data trustworthiness, by only delivering data which meets
a predefined set of quality criteria. Another way of tackling this issue is presented in [ 18]. In the study, the authors
present a reputation-based mechanism, which aims to defend against internal attacks. Their aim was to increase data
trustworthiness by ensuring data veracity.
Based on our findings, we choose to adopt the goal of decreasing risk. We do so, because one major goal of our study is
to tackle the risks consumers face when using data, therefore we aim to achieve the same goal as existing artifacts do.
Decrease Complexity. Addressing the problem of complexity, most artifacts share the objective of decreasing the
complexity of trust assessment for the consumer. This is the reason why most of the artifacts identified in our SLR
opted for computing a trust score, providing an intuitive metric. This is in line with [22], arguing that e.g. complete
provenance graphs are too complex for users to grasp in order to assess the trustworthiness of data. On top of that, the
authors found that users need to be able to understand the measurement in order to feel the data is trustworthy.
We, too, adopt this design goal, as it is a central aspect of our target domain of inter-organisational data sharing. Many
different users with different backgrounds will need to grow confident in the assessment of data trustworthiness. As a
result, they need to be able to understand the given information, so they can base their decisions on it.
Enhance Trust. By far the most important goal existing solutions aim to address is trust, i.e., increasing the confidence
of the consumer in the data they use. [ 2] highlight that by arguing that data trustworthiness is essential for users to
utilise the data confidently. This is in line with research on inter-organisational data sharing, stating that trust is the
most important factor for it to succeed [39]. Consequently, most artifacts address this point by increasing transparency.
In [26] e.g., the authors enhance the trustworthiness of traceability data, by providing tamper-proof evidence of the
provenance of data using blockchain.
Following this, we adopt this design objective as well, as one major goal of our study is to enhance the overall trust of
consumers on a data level. And although the goals of trust and risk seem quite similar, there are some clear distinctions
to be made. This is due to the fact that in order to decrease risks, one is mostly concerned with avoiding doing
something or employing measurements in order to prevent something to happen. Contrarily, trust in a general sense, is
quite subjective to the entity which perceives it and comprised of many different dimensions [45]. Therefore, being
transparent about the data itself and the measurements in place in order to ensure different criteria is as important as
employing them in the first place. Still, both goals are closely related.
Enable Interoperability. One design objective we did not find among the identified artifacts is interoperability. Most
of the existing artifacts aim at tackling a very specific case or a broader domain such as IoT. Still, the existing solutions
could play a major important role in the context of inter-organisational data sharing, to measure, assess or ensure
trustworthiness. This is because many of the trust models and frameworks could be applied to other domains or
combined in order to cover the whole data flow in inter-organisational data sharing. Yet, there is no standardised trust
6

Levels of Assurance for Data Trustworthiness A PREPRINT
model or overarching solution, which aims at utilising the existing technologies to enhance trustworthiness at a data
level [7].
For a similar reason, the identity LoA-based assurance technique eIDAS was introduced by the EU. More specifically,
the eIDAS directive mentions the fragmented approach to identity verification and a lack of interoperability among
identification techniques as key drivers for passing the regulation [8].
We therefore believe that the current heterogeneous landscape of existing artifacts can benefit from taking a similar
approach. This way, a combination of existing solutions could be utilised to assure data trustworthiness in the challenging
environment of inter-organisational data sharing. Hence, we apply and adopt this design goal from the domain of LoAs.
4.3 Artifact Description
provides claim Provider
Assurance
Provider
audits claimassures claim
Consumer
Figure 5: Abstract actor model of Data LoA.
Based on the derived design knowledge and the defined design goals, the artifact was developed by a cross-functional
team of researchers and practitioners in an agile way. The resulting artifact described in the following is an LoA-based
assurance technique. We call it Levels of Assurance for Data Trustworthiness, or short Data LoA. As it is a first-iteration
DSR artifact, it specifically concentrates on outlining the overall idea as well as actors and their relationships. This
ensures that the most important elements are identified as a first, allowing for incremental additions and modifications.
The definition of the specific levels however was not part of our scope in this iteration.
Similar to LoAs within other domains, we define Data LoA as follows: Levels of Assurances for Data Trustworthiness
refer to the degree of confidence which with a dataset’s underlying information can be trusted to be actually true. Thus,
it aims at grading the confidence a relying party should put into it, in respect to the risk which potentially arise in case
the assurance does not hold true. Moreover, we propose the three following actors as well as their interactions, based on
an abstract model pictured in Figure 5.
4.3.1 Data Consumer
The data consumer is the relying party, speaking in the sense of LoAs. In the context of the ISO/IEC 15408-1 standard
another suitable terminology could be risk owner. It is the party which consumes the data, thus it at risk in case the data
trustworthiness claim does not hold true. Therefore, the data consumer utilises the Data LoA in order to decide whether
or not to use a certain set of data, based on the related risks.
4.3.2 Data Provider
The data provider is - in the sense of LoAs - the claimant. Thus, it is the party which claims that a certain set of data
offers a certain degree of trustworthiness. More specifically, by claiming a certain Data LoA the data provider claims
that appropriate care was taken in order to reach some degree of confidence about the data’s trustworthiness.
4.3.3 Assurance Provider
The assurance provider is employed in the same sense as in LoAs. It is usually a third-party, which acts as trustworthy
auditor and assurer between the data provider and the consumer. Although not strictly necessary, it greatly influences
the amount of trust the data consumer can put into the assured claims. Self-asserted claims are usually not trusted to a
great extend. Therefore, it can be beneficial to have a trustworthy third-party which audits the measurements taken by
the data provider.
7

Levels of Assurance for Data Trustworthiness A PREPRINT
4.3.4 Interactions
In order to establish a Data LoA, the following interactions between the three mentioned actors are performed. First off,
the data provider needs to create a claim. Then, based on this, the assurance provider needs to conduct an audit of the
given claim. To do so, the data provider needs to provide the assurance provider with sufficient evidence, proving that
the claim indeed holds true. After that, it is at the discretion of the assurance provider to make an assurance. This can
either be in the form of certifications, reports or other ways of communicating proofs.
Using the assured claim in combination with a dataset, provided by the data provider, the data consumer can then
choose to put its confidence in the trustworthiness of the data or not. Hence, it is up to the data consumer, whether to
believe the assured claim or the assurance provider as a whole.
4.4 Demonstration & Evaluation
Proceeding the DSR approach, we aim at evaluating the artifact through demonstration. Therefore, we follow [ 15]
by opting to conduct an experimental simulation, as well as an informed argument as part of a descriptive evaluation.
According to [12], the evaluation through a PoC is sufficient for novel artifacts.
Hence, we implement the Data LoA artifact in the domain of data spaces, in order to employ it in a sophisticated
environment for inter-organisational data sharing. This allows us to build upon a strong landscape of proven data
sharing enabling technologies.
On top of that, our aim is to investigate the impact of our artifact to the domain and the implications it might have for
data spaces. Additionally, in this PoC we solely focus on the interaction between provider and consumer in order to
reduce complexities. Therefore, we assume a self-asserted claim.
The PoC reflects a minimal data space. It includes only required parts, in order to showcase and evaluate our artifact.
Hence, it comprises the following components, as pictured in Figure 6: Data Source, Data Sink and Data Space.
Dataspace
«EDC»
Consumer
Connector
«EDC»
Provider
Connector
Negotiation & Transfer
«Backend»
Data Source
Data
«Backend»
Data Sink
Data
LoA
selects and
publishes data
ProviderConsumer
LoA
decides whether
to use data
Figure 6: Proof of concept for Data LoA, as used in experimental setup.
The Data Space is comprised of twodata space connectors, each offering all required functionalities for a sovereign data
exchange in a data space, both for provider and consumer. Thus, they offer features for data discovery, policy negotiation
as well as data transfer. The connectors were implemented using a community-driven open-source framework, namely
the Eclipse Data Space Components7.
The Data Source and Data Sink naturally resemble a data generating or consuming entity or process, respectively. They
both are simple Python backends, aiming to provide or accept data over a REST API.
Furthermore, the PoC is deployed using Docker on a virtual machine running Linux Ubuntu. With everything in place,
the following steps are performed: First of, the provider selects a dataset from his data source, which they want to
publish to the data space. Upon publishing, an asset gets registered at the provider connector, making the dataset
available to the data space. The asset is part of a data catalog and describes the dataset as well as the usage policies
which are linked to it. Furthermore, the provider can include miscellaneous information in it. Therefore, the provider
includes the respective Data LoA claim in the newly created asset as well.
7https://projects.eclipse.org/projects/technology.edc [Accessed 30.03.2025]
8

Levels of Assurance for Data Trustworthiness A PREPRINT
After the asset is successfully made available in the data space, the consumer utilises their connector, in order to request
the provider’s catalog. Upon retrieval, the consumer is able to inspect the registered asset. Usually, the consumer
decides whether or not to request and use the asset, based on the provided information in the catalog. However, the
information provided is often times rather sparse, defining only a general description of the data. Yet, in this case, the
consumer is provided with an additional Data LoA claim. We assume that the Data LoA claim in this experiment is
suitable for the consumer. Therefore, the consumer decides to request and negotiate the data offer. After that, the data is
successfully transferred and ready for use for the consumer.
The experimental simulation showcases how the Data LoA claim is presented and communicated between both actors in
the context of inter-organisational data sharing. Therefore, it demonstrates how the consumer is first of all provided with
details about the data trustworthiness. This approach, is well-suited to increase overall trust by enhancing transparency.
Also, only if the degree of confidence of the data trustworthiness claim is feasible for their case, the consumer decides
to actually request and use the data. This enables the consumer to greatly decrease risks, by using only data which suits
their needs. Furthermore, the overall concept of LoAs is well-suited to decrease complexity for the consumer. Although
this simulation lacked a concrete definition of different levels, one can easily imagine that a few levels are easy for the
consumer to comprehend.
Furthermore, considering the derived design knowledge, it clearly shows how existing problems are met and most
design goals are addressed. Solely the design goal of interoperability could not be demonstrated in this experiment as
emphasise was put on enhanced risk management capabilities by providing an easy to comprehend trust-enhancing
claim.
5 Discussion
In this study we designed and proposed a novel artifact for assuring the trustworthiness of data. Our aim was to address
the unbalanced view of trust in inter-organisational data sharing. We chose to focus on trust enhancing techniques on a
data level. We therefore conducted a DSR approach, building on top of existing data trustworthiness solutions, as well
as the commonly adopted technique of LoAs. This resulted in the Data LoA as a first iteration concept. We proceed by
discussing the implications of our study, as well as limitations and future work.
First, we identified and emphasised the need for an increased research effort in the domain of consumer trust in
inter-organisational data sharing. We highlighted the related risks consumers are prone to, when blindly trusting data.
Based on this, this paper investigated existing solutions for measuring and assuring data trustworthiness by conducting
a SLR, trying to find suitable methods that fit our domain. We found, that the current solution landscape is quite
heterogeneous and lacks a common standardised trust model. Furthermore, we identified the commonly acknowledged
challenges of undetermined risks, trustworthiness complexity and demand.
Second, it was demonstrated, how the Data LoA artifact was able to address most of the identified challenges, by
integrating it in a data sharing environment. It was showcased, how the Data LoA claim can be communicated and
exchanged, enabling the consumer to make informed decisions, addressing the aim of enhanced risk management
capabilities, specifically. Furthermore, by providing the consumer with more details related to the trustworthiness of
data, transparency and thus the overall consumer trust could be enhanced. On top of that, we adopted a commonly
acknowledged goal of LoAs, i.e., decreasing the overall complexity by laying the foundation for LoAs for data
trustworthiness. However, concrete levels are yet to be defined and the design objective of interoperability to be
addressed.
Lastly, we contribute to the body of design knowledge, using our derived problem and solution space. To the best of
our knowledge, this is the first work which explicitly stated design knowledge as well as design objectives. Hence, we
achieved to establish a sound foundation to build our artifact upon on. According to [12], our contributed artifact is
classified as an improvement, as it is built on top of existing artifacts. We therefore add to the community, by providing
an enhancement of existing solutions, as well as design knowledge for future work to build upon on.
5.1 Limitations & Future Work
Despite conducting a rigorous design approach, our study is subject to limitations. First, our design knowledge, acting
as foundation for our design activities, was derived using a SLR approach. Naturally, literature reviews are limited by
the coverage they achieve. Therefore, in order to increase the coverage and mitigate missing relevant literature, we
conducted a back- and forward search as part of the SLR.
Second, our designed artifact is still in an early stage. We therefore didn’t specify the different levels of assurance,
missing a concrete definition of measurements necessary in order to achieve different degrees of confidence. We chose
9

Levels of Assurance for Data Trustworthiness A PREPRINT
to do so, as our main purpose of this study was to motivate the overall topic as well as lay the foundation for future
work to build upon on. Therefore, we carefully evaluated the artifact in an experimental simulation as PoC, employing
it in a conceptual data sharing environment, focusing solely on the interaction between consumer and provider.
Third, while we identified interoperability as one of our design goals, our first iteration artifact mainly focused on
achieving the other goals. This was to ensure that our development activities stayed focused on addressing what’s
commonly agreed as major problems in the field. Still, having adopted the overall technique of LoAs to the domain of
data trustworthiness, we are confident that future iterations are capable of addressing this.
Consequently, we identify the following touch points and next steps for future work. First off, more work is needed
on the topic of data trustworthiness. As there is currently no commonly accepted notion of data trustworthiness, it is
challenging to come up with a proper definition of levels, let alone make them comprehensible for consumers. Therefore,
a literature survey may be suitable to address this.
Following this, more work should be put into the Data LoA concept by performing additional DSR cycles. We are
confident that the overall idea is capable of addressing the identified challenges sufficiently. Still, as it is a novel concept,
there are many points to investigate in detail. First of all, a proper definition of the levels are needed. This is crucial in
order for providers to be able to make sound claims, as well as for consumers to conduct a proper risk assessment. To
do so, current work on potential risk dimensions and attack taxonomies have to be considered, in order to define the
LoAs in a risk-based manner. Also, other dimensions of data trustworthiness such as reputation of source, or country of
origin have to be considered. Additionally, the body of design knowledge should be enhanced by, e.g., deriving design
principles in order to guide future DSR cycles.
Furthermore, the Data LoA concept itself needs to be looked upon from a greater perspective. Therefore, usage
incentives, challenges in implementing and adopting it, as well as domains have to be identified. This is to enable a
wide-spread adoption by clearly communicating the addressed domains as well as benefits and trade-offs. For instance,
according to [14, 16], there are trade-offs to be made when choosing between data trustworthiness and e.g. costs or
privacy. Therefore, it is important to weigh the required investments with the expected potential risks and their resulting
damages.
For that reason, domains and use-cases have to be identified, in which such a concept could be beneficial. From our
perspective, this is the case e.g. in critical infrastructure, such as water or power supply, or other automated systems
such as in healthcare. But also AI could greatly benefit from the concept, by e.g. weighing data with low LoA lower,
than data with high LoA. This way, less trustworthy data could still be facilitated for training.
6 Conclusions
In this study, we have designed a novel LoA for data trustworthiness artifact, aiming at addressing the shortcomings
of existing solutions. By doing this, we addressed the unbalanced view of trust from a consumer perspective in
inter-organisational data sharing, highlighting the need for trust enhancing solutions. We accomplished this by opting
for a DSR approach, building on top of existing research, deriving challenges and goals.
We found, that although our artifact meets most of the identified challenges and goals in theory, more work is needed in
order for it to be deployable in a real life scenario. Especially the goal of interoperability needs more attention, as well
as the definition of the different levels and the adoption of such. Further DSR cycles should be performed in order to
incrementally enhance the artifact.
Our work contributes to the realm of design research by proposing derived design knowledge, as well as a new artifact.
We encourage researchers to utilise our findings as foundation in order to further investigate the subject. Finally, we
hope our contributions help to increase the research efforts in order to address the shortcomings in regards to consumer
trust, ultimately increasing data sharing activities across organisations.
Acknowledgements
6.1 CRediT author statement
Florian Zimmer: Conceptualisation, Methodology, Software, Validation, Investigation, Writing - Original Draft,
Visualisation. Janosch Haber: Conceptualisation, Writing - Review & Editing, Mayuko Kaneko: Conceptualisation,
Writing - Review & Editing, Project administration.
10

Levels of Assurance for Data Trustworthiness A PREPRINT
References
[1] B. Alhaqbani and C. Fidge. A time-variant medical data trustworthiness assessment model. In 2009 11th
International Conference on e-Health Networking, Applications and Services (Healthcom), pages 130–137, 2009.
doi:10.1109/HEALTH.2009.5406198.
[2] Aseel Alkhelaiwi and Dan Grigoras. The origin and trustworthiness of data in smart city applications. In
Proceedings of the 8th International Conference on Utility and Cloud Computing, UCC ’15, pages 376–382. IEEE
Press, 2015. ISBN 9780769556970. doi:10.1109/UCC.2015.60.
[3] Amin Anjomshoaa, Santiago Cáceres Elvira, Christian Wolff, Juan Carlos Pérez Baún, Manos Karvounis, Marco
Mellia, Spiros Athanasiou, Asterios Katsifodimos, Alexandra Garatzogianni, Andreas Trügler, Martin Serrano,
Achille Zappa, Yury Glikman, Tuomo Tuikka, and Edward Curry. Data platforms for data spaces. In Edward
Curry, Simon Scerri, and Tuomo Tuikka, editors, Data Spaces, Springer eBook Collection, pages 43–64. Springer
International Publishing and Imprint Springer, Cham, 2022. ISBN 9783030986360. doi:10.1007/978-3-030-
98636-0_3.
[4] Claudio A. Ardagna, Rasool Asal, Ernesto Damiani, Nabil El Ioini, Mehdi Elahi, and Claus Pahl. From trustworthy
data to trustworthy iot: A data collection methodology based on blockchain. ACM Trans. Cyber-Phys. Syst., 5(1),
2021. ISSN 2378-962X. doi:10.1145/3418686.
[5] Elisa Bertino. Data trustworthiness—approaches and research challenges. In Joaquin Garcia-Alfaro, Jordi Herrera-
Joancomartí, Emil Lupu, Joachim Posegga, Alessandro Aldini, Fabio Martinelli, and Neeraj Suri, editors, Data
Privacy Management, Autonomous Spontaneous Security, and Security Assurance, volume 8872 of Lecture Notes
in Computer Science, pages 17–25. Springer International Publishing, Cham, 2015. ISBN 978-3-319-17015-2.
doi:10.1007/978-3-319-17016-9_2.
[6] Ruben D’Hauwers and Nils Walravens. Do you trust me? value and governance in data sharing business models. In
Xin-She Yang, Simon Sherratt, Nilanjan Dey, and Amit Joshi, editors,Proceedings of Sixth International Congress
on Information and Communication Technology, volume 235 of Lecture Notes in Networks and Systems, pages
217–225. Springer Singapore, Singapore, 2022. ISBN 978-981-16-2376-9. doi:10.1007/978-981-16-2377-6_22.
[7] Maryam Ebrahimi, Mohammad Hesam Tadayon, Mohammad Sayad Haghighi, and Alireza Jolfaei. A quantitative
comparative study of data-oriented trust management schemes in internet of things. ACM Trans. Manage. Inf.
Syst., 13(3), 2022. ISSN 2158-656X. doi:10.1145/3476248.
[8] European Parliament. Regulation no 910/2014 on electronic identification and trust services fro electronic
transactions in the internal market and repealing directive: eidas regulation, 23 July / 2014.
[9] Faheem Zafar, Abid Khan, Saba Suhail, Idrees Ahmed, Khizar Hameed, Hayat Mohammad Khan, Farhana Jabeen,
and Adeel Anjum. Trustworthy data: A survey, taxonomy and future trends of secure provenance schemes.Journal
of Network and Computer Applications, 94:50–68, 2017. ISSN 1084-8045. doi:10.1016/j.jnca.2017.06.003. URL
https://www.sciencedirect.com/science/article/pii/S1084804517302229.
[10] Harald Foidl and Michael Felderer. An approach for assessing industrial iot data sources to determine their data
trustworthiness. Internet of Things, 22:100735, 2023. ISSN 25426605. doi:10.1016/j.iot.2023.100735.
[11] L. Gomez, A. Laube, and A. Sorniotti. Trustworthiness assessment of wireless sensor data for business applications.
In 2009 International Conference on Advanced Information Networking and Applications, pages 355–362, 2009.
ISBN 2332-5658. doi:10.1109/AINA.2009.92.
[12] Shirley Gregor and Alan R. Hevner. Positioning and presenting design science research for maximum impact.
MIS Quarterly, 37(2):337–355, 2013. ISSN 02767783. doi:10.25300/MISQ/2013/37.2.01.
[13] N. Haron, J. Jaafar, I. A. Aziz, M. H. Hassan, and M. I. Shapiai. Data trustworthiness in internet of things: A
taxonomy and future directions. In 2017 IEEE Conference on Big Data and Analytics (ICBDA), pages 25–30,
2017. doi:10.1109/ICBDAA.2017.8284102.
[14] Daojing He, Sammy Chan, and Mohsen Guizani. User privacy and data trustworthiness in mobile crowd sensing.
IEEE Wireless Communications, 22(1):28–34, 2015. ISSN 1536-1284. doi:10.1109/MWC.2015.7054716.
[15] Alan R. Hevner, Salvatore T. March, Jinsoo Park, and Sudha Ram. Design science in information systems research.
MIS Quarterly, 2004.
[16] C. Hou, C. Zhou, C. G Wu, R. Cong, and K. Li. Optimization of cloud-based multi-agent system for trade-
off between trustworthiness of data and cost of data usage. IEEE Transactions on Automation Science and
Engineering, 21(1):106–122, 2024. ISSN 1558-3783. doi:10.1109/TASE.2022.3224984.
[17] Monika Huber, Sascha Wessel, Gerd Brost, and Nadja Menz. Building trust in data spaces. In Boris Otto, Michael
ten Hompel, and Stefan Wrobel, editors, Designing Data Spaces, Springer eBook Collection, pages 147–164.
11

Levels of Assurance for Data Trustworthiness A PREPRINT
Springer International Publishing and Imprint Springer, Cham, 2022. ISBN 9783030939755. doi:10.1007/978-3-
030-93975-5_9.
[18] Hui Lin, Jia Hu, Chuanfeng Xu, Jianfeng Ma, and Mengyang Yu. Dtrm: A new reputation mechanism to enhance
data trustworthiness for high-performance cloud computing. Future Generation Computer Systems, 83:293–302,
2018. ISSN 0167-739X. doi:10.1016/j.future.2018.01.026. URL https://www.sciencedirect.com/science/
article/pii/S0167739X17317247.
[19] M. M. Islam, G. C. Karmakar, J. Kamruzzaman, M. Murshed, and A. Chowdhury. Trustworthiness of iot
images leveraging with other modal sensor’s data. IEEE Internet of Things Journal, 12(1):163–173, 2025. ISSN
2327-4662. doi:10.1109/JIOT.2024.3459477.
[20] ISO and IEC. Information technology — security techniques — entity authentication assurance framework:
Iso/iec 29115, April, 2013.
[21] ISO and IEC. Information security, cybersecurity and privacy protection — evaluation criteria for it security - part
5: Iso/iec 15408-5:2022, August 2022.
[22] Fariha Tasmin Jaigirdar, Carsten Rudolph, and Chris Bain. Can i trust the data i see? a physician’s concern on
medical data in iot health architectures. In Proceedings of the Australasian Computer Science Week Multiconfer-
ence, ACSW ’19, New York, NY , USA, 2019. Association for Computing Machinery. ISBN 9781450366038.
doi:10.1145/3290688.3290731.
[23] Franklin Magalhaes Ribeiro Junior and Carlos Alberto Kamienski. A survey on trustworthiness for the internet of
things. IEEE Access, 9:42493–42514, 2021. ISSN 2169-3536. doi:10.1109/ACCESS.2021.3066457.
[24] Ilka Jussen, Julia Schweihoff, and Frederik Möller. Tensions in inter-organizational data sharing: Findings from
literature and practice. In 2023 IEEE 25th Conference on Business Informatics (CBI), pages 1–10. IEEE, 2023.
ISBN 979-8-3503-1515-8. doi:10.1109/CBI58679.2023.10187530.
[25] N. Karthik and V . S. Ananthanarayana. Sensor data modeling for data trustworthi-
ness. In 2016 IEEE Trustcom/BigDataSE/ISPA , pages 909–916, 2016. ISBN 2324-9013.
doi:10.1109/Trustcom/BigDataSE/ICESS.2017.330.
[26] O. Leteane, Y . Ayalew, and T. Motshegwa. A multi-package trust model for improving the trustworthiness of
traceability data in blockchain-based beef supply chain. In 2024 IEEE Conference on Dependable and Secure
Computing (DSC), pages 155–162, 2024. doi:10.1109/DSC63325.2024.00040.
[27] Oratile Leteane and Yirsaw Ayalew. Improving the trustworthiness of traceability data in food supply chain using
blockchain and trust model. The Journal of The British Blockchain Association, 7(1):1–12, 2024. ISSN 25163949.
doi:10.31585/jbba-7-1-(2)2024.
[28] H. S Lim, G. Ghinita, E. Bertino, and M. Kantarcioglu. A game-theoretic approach for high-assurance of data
trustworthiness in sensor networks. In 2012 IEEE 28th International Conference on Data Engineering, pages
1192–1203, 2012. ISBN 2375-026X. doi:10.1109/ICDE.2012.78.
[29] Jennifer Martínez-Ferrero and Isabel-María García-Sánchez. The level of sustainability assurance: The effects of
brand reputation and industry specialisation of assurance providers. Journal of Business Ethics, 150(4):971–990,
2018. ISSN 0167-4544. doi:10.1007/s10551-016-3159-x.
[30] Aleksandra Nenadic, Ning Zhang, Li Yao, and Terry Morrow. Levels of authentication assurance: an investigation.
In Third International Symposium on Information Assurance and Security, pages 155–160. IEEE, 2007. ISBN
0-7695-2876-7. doi:10.1109/IAS.2007.88.
[31] A. Ormazabal, D. Berry, and L. Hederman. Co-development of a tool to help clinicians decide upon the
trustworthiness of patient generated health data. In 2024 IEEE 37th International Symposium on Computer-Based
Medical Systems (CBMS), pages 442–449, 2024. ISBN 2372-9198. doi:10.1109/CBMS61543.2024.00079.
[32] Boris Otto, Michael ten Hompel, and Stefan Wrobel, editors. Designing Data Spaces: The Ecosystem Approach
to Competitive Advantage. Springer eBook Collection. Springer International Publishing and Imprint Springer,
Cham, 1st ed. 2022 edition, 2022. ISBN 9783030939755. doi:10.1007/978-3-030-93975-5.
[33] Ken Peffers, Tuure Tuunanen, Marcus A. Rothenberger, and Samir Chatterjee. A design science research
methodology for information systems research. Journal of Management Information Systems, 24(3):45–77, 2007.
ISSN 0742-1222. doi:10.2753/MIS0742-1222240302.
[34] C. Prandi, S. Ferretti, S. Mirri, and P. Salomoni. Trustworthiness in crowd- sensed and sourced georeferenced
data. In 2015 IEEE International Conference on Pervasive Computing and Communication Workshops (PerCom
Workshops), pages 402–407, 2015. doi:10.1109/PERCOMW.2015.7134071.
12

Levels of Assurance for Data Trustworthiness A PREPRINT
[35] Hafiz ur Rahman, Guojun Wang, Md Zakirul Alam Bhuiyan, and Jianer Chen. Trustworthy data collection
for cyber systems: A taxonomy and future directions. In Guojun Wang, Abdulmotaleb El Saddik, Xuejia Lai,
Gregorio Martinez Perez, and Kim-Kwang Raymond Choo, editors, Smart City and Informatization, volume 1122
of Communications in Computer and Information Science, pages 152–164. Springer Singapore, Singapore, 2019.
ISBN 978-981-15-1300-8. doi:10.1007/978-981-15-1301-5_13.
[36] S. Suhail, C. S. Hong, M. A. Lodhi, F. Zafar, A. Khan, and F. Bashir. Data trustworthiness in iot. In 2018 Interna-
tional Conference on Information Networking (ICOIN), pages 414–419, 2018. doi:10.1109/ICOIN.2018.8343151.
[37] H. Tao, M. Z. A. Bhuiyan, M. A. Rahman, T. Wang, J. Wu, S. Q. Salih, Y . Li, and T. Hayajneh. Trustdata:
Trustworthy and secured data collection for event detection in industrial cyber-physical system.IEEE Transactions
on Industrial Informatics, 16(5):3311–3321, 2020. ISSN 1941-0050. doi:10.1109/TII.2019.2950192.
[38] Michael ten Hompel and Michael Schmidt. Silicon economy: Logistics as the natural data ecosystem. In Boris
Otto, Michael ten Hompel, and Stefan Wrobel, editors, Designing Data Spaces , Springer eBook Collection,
pages 263–278. Springer International Publishing and Imprint Springer, Cham, 2022. ISBN 9783030939755.
doi:10.1007/978-3-030-93975-5_16.
[39] Fabrice Tocco and Laurent Lafaye. Data platform solutions. In Boris Otto, Michael ten Hompel, and Stefan
Wrobel, editors, Designing Data Spaces , Springer eBook Collection, pages 383–393. Springer International
Publishing and Imprint Springer, Cham, 2022. ISBN 9783030939755. doi:10.1007/978-3-030-93975-5_23.
[40] Jan vom Brocke, Alexander Simons, Kai Riemer, Björn Niehaves, Ralf Plattfaut, and Anne Cleven. Standing on
the shoulders of giants: Challenges and recommendations of literature search in information systems research.
Communications of the Association for Information Systems, 37, 2015. doi:10.17705/1CAIS.03709.
[41] Jan vom Brocke, Robert Winter, Alan Hevner, and Alexander Maedche. Special issue editorial –accumulation
and evolution of design knowledge in design science research: A journey through time and space. Journal of the
Association for Information Systems, 21(3):520–544, 2020. doi:10.17705/1jais.00611.
[42] Franziska von Scherenberg, Malte Hellmeier, and Boris Otto. Data sovereignty in information systems. Electronic
Markets, 34(1), 2024. ISSN 1019-6781. doi:10.1007/s12525-024-00693-4.
[43] Jinying Xu and Kristen MacAskill. A carbon data trustworthiness framework for the construction sector. In
Proceedings of the 2023 European Conference on Computing in Construction and the 40th International
CIB W78 Conference , Computing in Construction. European Council for Computing in Construction, 2023.
doi:10.35490/ec3.2023.261.
[44] Florian Zimmer, Janosch Haber, and Mayuko Kaneko. Enhancing trust in inter-organisational data sharing: Levels
of assurance for data trustworthiness - literature body. Zenodo, https://doi.org/10.5281/zenodo.
14639350, 2025. doi:10.5281/zenodo.14639350.
[45] Tengjian Zou, Gokhan Ertug, Ilya R. P. Cuypers, and Donald L. Ferrin. Trust across borders: a review of the
research on interorganizational trust in international business. Journal of International Business Studies, 54(8):
1379–1401, 2023. ISSN 0047-2506. doi:10.1057/s41267-023-00648-5.
13
