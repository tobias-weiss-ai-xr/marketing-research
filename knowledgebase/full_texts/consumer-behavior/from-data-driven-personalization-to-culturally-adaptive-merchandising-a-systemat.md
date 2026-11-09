---
title: 'From Data-Driven Personalization to Culturally Adaptive Merchandising: A Systematic Review and
  the CAMI-DM Framework'
url: https://doi.org/10.21203/rs.3.rs-11309275/v1
category: consumer-behavior
subcategory: framework
date: 2026-10
venue: Research Square
authors:
- Claude Issa Nombré
- KOUADIO PROSPER KIMOU
- TANON KODJO
source: openalex-oa
pdf_url: https://www.researchsquare.com/article/rs-11309275/latest.pdf
pages: 21
chars: 55705
fetched_at: '2026-11-08T19:26:53+00:00'
kb_version: 1
---

# From Data-Driven Personalization to Culturally Adaptive Merchandising: A Systematic Review and the CAMI-DM Framework

From Data-Driven Personalization to Culturally
Adaptive Merchandising: A Systematic Review and
the CAMI-DM Framework
CLAUDE ISSA NOMBRE 
Institut National Polytechnique Félix Houphouët-Boigny
KOUADIO PROSPER KIMOU 
Institut National Polytechnique Félix Houphouët-Boigny
TANON KODJO 
Institut National Polytechnique Félix Houphouët-Boigny
Research Article
Keywords: culturally adaptive merchandising, artiﬁcial intelligence, behavioral data, retail personalization,
cross-cultural consumer behavior, QAP , phygital retail, CAMI-DM
Posted Date: October 21st, 2026
DOI: https://doi.org/10.21203/rs.3.rs-11309275/v1
License:   This work is licensed under a Creative Commons Attribution 4.0 International License.  
Read Full License
Additional Declarations: No competing interests reported.

From Data-Driven Personalization to Culturally Adaptive Merchandising: A Systematic
Review and the CAMI-DM Framework
NOMBRE Claude Issa, KIMOU Kouadio Prosper, KADJO Tanon
Polytechnic Doctoral School
National Polytechnic Institute Houphouet Boigny – Yamoussoukro
Research Laboratory of Computer Science and Technology

Abstract
Artificial intelligence (AI), behavioral analytics, recommender systems, and digital retail technologies
are increasingly used to personalize consumer experiences. Yet personalization based primarily on
observed behavior may remain insensitive to cultural meaning, local practices, language, symbolic
preferences, and context. This study revisits the literature on data-driven intelligent multicultural
merchandising and develops an integrative research framework rather than a descriptive inventory of
technologies. A PRISMA-guided systematic review was conducted using Scopus. A broad search
retrieved 129 records; after restricting the corpus to Articles and Reviews, 60 records were screened
by title and abstract. Thirty-four records remained after title/abstract screening; 12 were e xcluded at a
preliminary eligibility check, and 22 reports were advanced to retrieval. Three could not be retrieve d
and 19 were assessed for eligibility; nine were excluded, leaving ten studies in the confirmed synthesis
set. The included studies cover big-data and machine-learning analytics, Transformer-based sentiment
analysis, chatbot recommendation, automated retail, cross-border AI promotion, phygital retail
environments, cultural-product recommendation, and culturally contingent consumer responses. The
evidence is fragmented across these streams. Within the screened corpus, no confirmed study
operationalized in one end-to-end framework the joint sequence of behavioral data, multidime nsional
cultural context, intelligent adaptation, merchandising decisions, observed consumer response, and
feedback-driven updating. Building on this gap, the paper proposes CAMI-DM (Culturally Adaptive,
AI- and Data-driven Merchandising), an architecture linking behavioral signals, cultural and situational
context, adaptive intelligence, customer experience, trust, behavioral response, and commercial
performance. A quadratic assignment problem (QAP) is proposed as the spatial optimiza tion layer,
with distance constraints that preserve metric consistency. The study concludes with a set of testable
hypotheses and an empirical protocol for physical, digital, and phygital retail settings.
Keywords: culturally adaptive merchandising; artificial intelligence; behavioral data; retail
personalization; cross-cultural consumer behavior; QAP; phygital retail; CAMI-DM
1. Introduction
Retailing is increasingly organized around the continuous collection and interpretation of consumer
data. Transaction histories, product interactions, browsing paths, loyalty-program records, mobile
interactions, digital reviews, and in-store traces can be transformed into signals for recommendation,
segmentation, demand prediction, and experience design. In parallel, artificial intelligence (AI) has
expanded the ability of retailers to infer preferences, automate decisions, and personalize interactions
at increasingly fine temporal scales (Davenport et al., 2020; Wedel & Kannan, 2016). These
developments have also extended merchandising beyond static product placement toward dynamic
combinations of assortment, presentation, promotion, recommendation, and spatial configuration.
However, the increasing technical capacity to personalize does not resolve a more fundamental
question: personalized according to which context? Consumer behavior is shaped not only by
individual history but also by meanings, social norms, values, language, religious and belief-related
practices, visual conventions, household routines, seasonal events, and locally embedded preferences.

Cross-cultural research shows that the same interface, recommendation mechanism, or visual
presentation can be interpreted differently across cultural contexts (Wang et al., 2023). Recent retail
studies similarly show that cultural constructs can alter responses to AI-mediated recommendations,
trust, and automated shopping environments (Baingam & Wittayakom, 2026; Landim et al., 2025; Niu
et al., 2026).
This issue is especially important for multicultural retail environments, where customers may share a
country, city, or store while differing in language practices, values, beliefs, consumption traditions, or
symbolic expectations. A national label is therefore an incomplete representation of cultural context.
Hofstede’s dimensions remain useful for comparative analysis, but they do not by themselves capture
intra-cultural heterogeneity, hybrid identities, digitally mediated communities, or context-dependent
behavior (Hofstede, 2001; de Mooij, 2019). For a data-driven merchandising system, cultural context
should therefore be represented as a multidimensional and updateable construct rather than as a fixed
country code.
The literature is developing rapidly, but it remains fragmented. One group of studies focuses on AI-
enabled personalization and recommendation. Another examines cultural differences in consumer
responses to AI. A third investigates behavioral analytics and data-driven retail. A fourth addresses
physical or phygital retail environments, visual presentation, or spatial experience. Recent empirical
studies provide strong evidence for individual pieces of the problem. Putri et al. (2025), for example,
use big-data analytics and machine learning to identify drivers of demand in modest fashion e-
commerce. Liu and Pareti (2026) analyze 33,464 online wine reviews from China and Italy with
Transformer-based natural language processing and cultural dimensions. Landim et al. (2025) compare
a chatbot recommender across Brazilian and English consumers. Wang et al. (2023) demonstrate
culturally contingent effects of product-image background. Yet these contributions do not establish a
unified, feedback-driven merchandising architecture.
The original version of this study was framed primarily as a bibliographic description of intelligent
multicultural merchandising. The present paper deliberately changes that positioning. Instead of using
approximate literature-volume ranges or simply listing technologies, it uses a reproducible Scopus
search, an explicit PRISMA-guided selection process, a structured synthesis of the studies that passed
relevance screening, and a theory-building framework intended to explain how the different streams
can be integrated. The contribution is therefore not the claim that AI, personalization, culture, or
merchandising are individually new. The contribution is the integration of these streams into a single
research architecture and an empirical agenda for testing that architecture.
The study addresses six research questions: RQ1, how has the research landscape at the intersection of
AI, data-driven retail, and cultural context evolved within the retrieved corpus? RQ2, which types of
technologies, data, retail settings, and consumer outcomes are represented? RQ3, how is culture
operationalized in data-driven retail and AI studies? RQ4, how do the included studies connect
behavioral data, AI-enabled personalization, cultural adaptation, and merchandising? RQ5, what
methodological and conceptual gaps remain? RQ6, how can these gaps be translated into an integrative,
testable framework for culturally adaptive merchandising?

2. Theoretical Background
2.1. Merchandising as a decision system
Merchandising traditionally concerns the selection, placement, presentation, and promotion of products
to facilitate consumer choice while supporting commercial objectives. Research on shelf-space
allocation and store layout has long shown that spatial decisions can influence attention, search,
convenience, and sales (DrŁze et al., 1994; Hübner et al., 2013). More recent retailing research  treats
the store as part of a broader experience system in which physical and digital touchpoints interact. The
implication for this paper is that merchandising should be treated not only as a static arrangement but
as a sequence of decisions that can be updated when new information becomes available.
2.2. Behavioral data and customer journeys
Behavioral data capture what consumers do rather than only what they declare that they prefer. In
digital retail, such data may include clicks, search queries, product views, dwell time, recommendation
responses, cart additions, purchases, and reviews. In physical stores, tracking technologies can add
movement paths, dwell time, aisle visits, product interactions, queue behavior, and location-based
exposure. The customer-journey literature emphasizes that experience is distributed across multiple
touchpoints and stages (Lemon & Verhoef, 2016; Becker & Jaakkola, 2020). A CAMI-DM system
consequently needs a temporal representation of behavior rather than a one-time customer profile.
2.3. AI-enabled personalization
AI-enabled personalization uses machine learning, recommender systems, natural-language
processing, computer vision, predictive analytics, or generative systems to infer preferences and select
relevant interventions. Davenport et al. (2020) argue that AI changes marketing by increasing
prediction and automation capacity, while subsequent retail studies show how recommendation
systems can be embedded into customer interfaces. The important distinction for CAMI-DM is between
technological personalization and contextual adaptation. The former asks which option is likely to fit
an individual based on observed signals; the latter asks whether that option, presentation, message, or
placement remains culturally appropriate in the situation in which the consumer encounters it.
2.4. Culture as a multidimensional consumer context
Culture influences interpretation, expectations, information processing, social meaning, and
consumption practices. Hofstede’s framework provides a comparative language for dimensions such
as individualism-collectivism and uncertainty avoidance, while de Mooij emphasizes the relationship
between culture and consumer behavior. Yet a data-driven merchandising model should avoid
collapsing culture into nationality. Recent research illustrates the diversity of operationalizations:
individualism in AI-chatbot research, Buddhist reflective cognition in Thailand, mianzi in Chinese
business settings, and holistic versus analytic thinking in cross-border e-commerce (Baingam &
Wittayakom, 2026; Niu et al., 2026; Wang et al., 2023). These studies suggest a broader formulation
in which cultural context is represented by a vector of relevant, ethically collected attributes and not by
a single country variable.
2.5. Experience, trust, and consumer response
AI-mediated decisions can influence perceptions of relevance, convenience, agency, and trust. The
consumer response may therefore occur through multiple mechanisms rather than through purchase

alone. The service and customer-experience literature emphasizes perceived value, emotional response,
cognitive processing, and subsequent behavioral response (Lemon & Verhoef, 2016; Becker &
Jaakkola, 2020). CAMI-DM consequently positions customer experience and trust between adaptive
merchandising decisions and behavioral outcomes. This structure also creates space for privacy,
transparency, and consumer autonomy as design constraints rather than after-the-fact ethical additions.
3. Research Questions and Contribution
RQ1. What are the main technological, data, cultural, and retail characteristics of research at the
intersection of AI-enabled retail and cultural adaptation in the retrieved Scopus corpus?
RQ2. Which consumer outcomes and adaptation mechanisms are currently studied?
RQ3. How is cultural context represented across the included studies?
RQ4. To what extent are behavioral data, AI, culture, and merchandising integrated rather than studied
separately?
RQ5. Which conceptual, methodological, and operational gaps limit the development of end-to-end
culturally adaptive merchandising?
RQ6. What integrative framework and empirical propositions can connect the identified evidence
streams?
3.1. Contributions
The paper makes four contributions. First, it replaces non-reproducible estimates of literature volume
with an explicit and auditable Scopus search and screening process. Second, it separates technological
personalization from cultural adaptation, showing that the two are complementary rather than
synonymous. Third, it synthesizes evidence from data-driven retail, culturally contingent consumer
response, visual merchandising, and phygital experience into a single CAMI-DM architecture. Fourth,
it translates the conceptual gap into a testable empirical design and a spatial optimization module based
on the quadratic assignment problem (QAP).
4. Methodology
4.1. Review design
The review follows a PRISMA 2020-guided reporting structure. PRISMA 2020 provides a checklist
and flow-diagram templates for reporting why a review was conducted, how evidence was identified
and selected, and what was ultimately included (Page et al., 2021). The present review is a systematic
evidence synthesis with theory-building objectives; it is not presented as a meta-analysis because the
included studies are heterogeneous in design, data, constructs, and outcomes.
4.2. Search strategy
Scopus was used as the sole bibliographic database for study identification. This choice was made to
provide a structured, reproducible, and sufficiently broad documentary corpus covering the scientific
literature relevant to the research question. The main search was conducted on September 22, 2026.
An expanded search query was developed around three mandatory conceptual blocks: smart
technologies and data, retail or merchandising, and culture or cultural adaptation. A narrower
sensitivity search additionally required the explicit presence of terms related to consumer behavior and
personalization and returned 32 records. These records were included within the 129 records retrieved

by the expanded search. Therefore, the latter was retained for the screening process in order to reduce
the risk of excluding potentially relevant studies.
The broad Scopus query was:
TITLE-ABS-KEY(
 ("artificial intelligence" OR "machine learning" OR "deep learning" OR "intelligent system*" OR
"recommender system*" OR "recommendation system*" OR "predictive analytics" OR "big data" OR
"generative AI") AND
 (retail* OR merchandising OR "visual merchandising" OR "product placement" OR planogram* OR
"store layout" OR "shelf management" OR "smart retail*" OR "digital retail*" OR omnichannel) AND
 (culture OR "cultural adaptation" OR "cultural preference*" OR multicultural OR "cross-cultural" OR
"cross cultural" OR "cultural context" OR "cultural diversity" OR "local preference*")
)
AND PUBYEAR > 2018
AND PUBYEAR < 2027
AND LANGUAGE(english)
4.3. Search refinement and eligibility
The broad query returned 129 records. The corpus was then limited to Articles and Reviews, yielding
60 records: 54 Articles and 6 Reviews. The title/abstract screening excluded 26 clearly irrelevant
records. Thirty-four records remained for preliminary eligibility. At that stage, 12 were excluded for
an explicit mismatch with the prespecified scope, leaving 22 reports for retrieval and detailed eligibility
assessment. Three could not be retrieved. Nineteen reports were assessed and nine were excluded for
lack of a substantive connection to the intersection of AI/data, retail/merchandising, and cultural
context. Ten studies remained in the confirmed synthesis set. The selection flow is summarized in
Figure 1.
4.3.1 Screening procedure
Screening was conducted using a prespecified eligibility grid derived from the research questions and
inclusion/exclusion criteria. Titles and abstracts were first examined to remove records that were
clearly outside the scope. The remaining records were subjected to a preliminary eligibility assessment,
followed by full-text retrieval where available. Eligibility decisions were recorded in a structured
screening table. Ambiguous records were re-examined against the predefined criteria before the final
inclusion decision.
Because the review was conducted as a doctoral theory-building study, the screening process was
designed to maximize traceability of decisions rather than to claim inter-rater reliability that was not
formally calculated.
4.3.2 Methodological quality and relevance appraisal
Because the included studies differed substantially in design, data sources, analytical methods, and
research objectives, a single risk-of-bias instrument was not applied uniformly to all studies. Instead, a
structured domain-based appraisal was conducted to assess methodological transparency and relevance
to CAMI-DM.
Each study was examined across six domains: (1) clarity of research objective, (2) transparency of data
and sample description, (3) appropriateness of the analytical method, (4) explicitness of the cultur al
construct, (5) clarity of the link to retail or consumer decision making, and (6) transparency of study
limitations. Each domain was coded as fully reported, partially reported, or insufficiently reported.
This appraisal was used primarily to qualify the strength and transferability of the evidence rather than
to exclude studies solely on the basis of methodological score.

Table 1: Summary of Included Studies
Study Objective Data/sample Method Culture Retail link Limitations Overall relevance
Putri et al. (2025) ✓ ✓ ✓ ✓ ✓ ✓ Direct
Liu & Pareti (2026) ✓ ✓ ✓ ✓ ✓ ✓ Direct
Landim et al. (2025) ✓ ✓ ✓ ✓ ✓ ✓ Direct
Baingam &
Wittayakom (2026) ✓ ✓ ✓ ✓ ✓ ✓ Complementary
Niu, Yu & Dong (2023) ✓ ✓ ✓ ✓ ✓ ✓ Direct
Ratnayake et al. (2026) ✓ ✓ ✓ ✓ ✓ ✓ Direct
Sun (2025) ✓ ✓ ✓ ✓ ✓ ✓ Direct
Niu et al. (2026) ✓ ✓ ✓ ✓ ✓ ✓ Complementary
Akhtar et al. (2022) ✓ ✓ ✓ ✓ ✓ ✓ Direct
Wang et al. (2023) ✓ ✓ ✓ ✓ ✓ ✓ Direct
Direct – contribution to merchandising in the strict sense / Complementary – contributes to merchandising
in a complementary way

4.4. Inclusion and exclusion criteria

Table 2: Inclusion and Exclusion Criteria
Criterion Include Exclude
Population/context
Retail consumers, retail organizations,
digital or physical retail environments,
cross-border commerce, fashion retail,
cultural-product retail.
Non-retail contexts unless they
directly inform a transferable retail
mechanism.
Technology/data
AI, machine learning, NLP,
recommender systems, behavioral
analytics, big data, IoT/AR/VR or
related intelligent technologies used
substantively.
AI/data mentioned only incidentally
or used solely for bibliometric
clustering.
Culture
Explicit cultural, cross-cultural,
locally embedded, religious/belief-
related, symbolic, or culturally
contextual construct.
Culture used only as a generic word or
only as organizational culture.
Outcome/decision
Consumer behavior, customer experience,
recommendation, merchandising, purchase,
engagement, trust, satisfaction, or retail
decision outcomes
Studies with no meaningful connection to
consumer, retail, or merchandising
decisions
Publication type Scopus Article or Review, English, 2019–2026 search window. Conference-only records, editorials, notes, non-English records, or out-of- window records.

4.5. Data extraction and synthesis
For each retained study, the review extracted year, retail setting, method, technology, data type, cultural
construct, consumer or business outcome, adaptation mechanism, and relevance to CAMI-DM. The
synthesis was thematic and integrative: findings were grouped into (1) behavioral data and analytics,
(2) AI-enabled personalization and recommendation, (3) cultural contingency, (4) physical/phygital
merchandising and experience, and (5) feedback and optimization. This approach avoids treating
heterogeneous effect estimates as directly commensurable while still identifying structural
complementarities across studies.

5. Results
5.1. Corpus profile and selection
The final search-and-screening structure produces a compact but information-rich synthesis set. The
60 Article/Review records came from a broader 129-record search. The included studies were
published between 2022 and 2026, indicating that the studies satisfying the combined relevance criteria
were concentrated in the most recent part of the search window. This concentration should not be
interpreted as evidence that earlier work on culture, personalization, or merchandising did not exist;
rather, it indicates that earlier work did not survive the joint relevance criteria used here.

Table 3: Study Selection Indicators
Selection indicator Count
Broad Scopus retrieval 129
Article + Review subset 60
Articles 54
Reviews 6
Title/abstract exclusions 26
Reports advanced to retrieval 22
Preliminary eligibility exclusions 12
Reports not retrieved 3
Reports assessed 19
Eligibility exclusions 9
Confirmed included studies 10

5.2. Characteristics of the included studies
Table 4: Comparative Matrix of Included Studies: Methods, Cultural Contexts, and Implications
for the CAMI-DM Framework
Study Method/data Retail context Cultural dimension CAMI-DM implication
Putri et al.
(2025)
Big-data analytics +
ML; e-commerce
fashion
Modesty-
conscious
market; price,
brand, color,
fabric
Culturally/societally
specific segment
Data-driven
customization of
retail strategy
Liu &
Pareti
(2026)
33,464 online reviews;
Transformer/NLP;
Hofstede + SDT
China vs Italy;
digital wine
retail
Hofstede
dimensions;
motivation/expressio
n
Cross-cultural
sentiment matrix
for retail decision
support
Landim et
al. (2025)
Chatbot recommender;
Brazil/England
comparison
Fashion e-
commerce
Cross-
cultural/contextual
differences
Different
experience
responses to the
same
recommender
Baingam &
Wittayako
m (2026)
Survey, n=396;
hierarchical regression
Unmanned
convenience
stores, Thailand
Yonisomanasikara;
Buddhist context
Culturally
embedded
interpretation of
trust, risk and
acceptance
Niu, Yu &
Dong
(2023)
Cross-border co-
opetition/game-
theoretic model
AI livestream
and local retail
channel
Cultural disparities
as cross-border
condition
Adaptive
promotion/chann
el logic

Study Method/data Retail context Cultural dimension CAMI-DM implication
Ratnayake
et al.
(2026)
Systematic review; 50
publications
Luxury fashion
retail interiors;
physical/phygit
al
Digital culture;
cultural storytelling
Integration of
technology, space
and narrative
Sun (2025)
50,000+ visitor
sessions;
RFID/POS/app logs;
Apriori/FP-Growth
Museum
cultural-product
retail
Cultural-product
context
Behavior-aware
personalized
recommendations
Niu et al.
(2026)
Four-study multi-
method; aggregate
N=6,468
Retail precincts;
AI-enabled
brand strategy
Mianzi / Chinese
cultural prestige
AI sophistication
interacts with
culturally specific
motives
Akhtar et
al. (2022)
Digital
transformation/busines
s-model analysis
Textile/apparel;
supra-
omnichannel
retail
Socio-cultural shifts
in consumer
preferences
Real-time data
visibility and
user-driven
innovation
Wang et al.
(2023)
Cross-cultural
experiments; eye-
tracking in Study 3
Cross-border e-
commerce;
product images
Holistic vs analytic
thinking
Culturally
contingent visual
presentation

5.3. Thematic synthesis
5.3.1. Behavioral data enable adaptation, but culture determines meaning
The strongest data-driven evidence comes from studies that transform consumer traces into actionable
representations. Putri et al. (2025) use e-commerce data and machine learning to identify product
attributes associated with demand in a culturally specific fashion segment. Liu and Pareti (2026) use
33,464 reviews and Transformer-based sentiment analysis to distinguish evaluation patterns between
Chinese and Italian consumers. Sun (2025) shows how more than 50,000 visitor sessions can be
transformed into association rules connecting behavior, events, interactions, and cultural-product
purchases. These studies support the first pillar of CAMI-DM: behavioral data can provide a dynamic
signal about what consumers attend to, choose, value, or revisit.
At the same time, data do not determine meaning by themselves. A color, image, product category,
message, or recommendation can carry different meanings in different cultural contexts. Wang et al.
(2023) show that contextual image backgrounds can affect consumers differently depending on holistic
versus analytic thinking. The implication is that the same behavioral predictor may require different
interpretation rules across contexts. CAMI-DM therefore treats behavioral data and cultural context as
complementary inputs rather than substitute explanations.
5.3.2. AI personalization is increasingly effective, but not culturally neutral
Landim et al. (2025) provide direct evidence that an AI-enabled chatbot recommendation interface can
improve customer experience in fashion e-commerce while producing different magnitudes of response
across Brazil and England. Niu et al. (2026) similarly show that advanced AI with real-time analytics
and personalized recommendation changes the relationship between a culturally specific motive,

mianzi, and strategic dependence in retail settings. Baingam and Wittayakom (2026) add a culturally
embedded interpretation of automated retail acceptance, emphasizing trust, perceived risk, and
reflective evaluation. Together, these studies suggest that AI personalization should be treated as a
context-dependent intervention rather than as a culturally invariant treatment.
This distinction is central to the CAMI-DM proposal. A conventional recommender estimates
relevance from a consumer’s history. CAMI-DM adds a contextual layer that asks whether the
recommendation, presentation, placement, or interaction is culturally compatible in the current
environment. The model therefore separates the ability to predict preference from the ability to adapt
the commercial environment responsibly.
5.3.3. Physical, digital and phygital merchandising need a common architecture
The included studies span digital e-commerce, cross-border promotion, automated stores, museum
cultural-product retail, luxury retail interiors, and product-image presentation. Ratnayake et al. (2026)
show how technology, spatial atmosphere, and cultural storytelling can be integrated in phygital luxury
retail. Akhtar et al. (2022) highlight the shift toward digital and supra-omnichannel fashion systems in
which consumer preferences and real-time data influence business models. Wang et al. (2023)
demonstrate that visual presentation itself can be culturally contingent. These streams imply that
merchandising should not be reduced to a planogram: it includes the spatial, visual, informational, and
algorithmic elements that shape a shopping environment.
CAMI-DM therefore defines merchandising decisions broadly enough to include assortment,
placement, facings, adjacency, signage, color and visual presentation, digital recommendations,
promotion, and navigation support. The same adaptation logic can be instantiated physically, digitally,
or across phygital touchpoints, while the specific optimization problem may differ by channel.
5.3.4. The feedback loop is the least developed element
Several studies use real-time, behavioral, or transactional data, but the screened corpus does not
establish a confirmed end-to-end loop in which a retail system observes the current state, adapts
merchandising, measures the resulting consumer response, and then updates the next merchandising
decision with an explicit cultural representation. This is the key dynamic gap addressed by CAMI-DM.
The model is therefore not a static segmentation framework; it is a state-transition architecture in which
the merchandising environment can be updated as evidence accumulates.
5.3.5. Ethics, privacy, and consumer autonomy are constraints on adaptation
Culturally adaptive systems can create value, but they can also intensify profiling and stereotyping.
The relevant design question is not simply whether an algorithm can infer cultural attributes, but
whether those attributes are necessary, proportionate, explainable, and used to support consumer choice
rather than restrict it. The CAMI-DM framework consequently treats privacy, fairness, transparency,
and consumer autonomy as constraints on the adaptation engine. Cultural signals should be derived
from legitimate sources, validated with stakeholders, and used at the level of relevance needed for the
decision rather than as a blanket basis for exclusion.

5.4. Cross-study gap matrix
Table 5: Identified Gaps in the Literature and Responses Provided by the CAMI-DM
Framework
Gap What the corpus provides What remains missing CAMI-DM response
Joint
integration
Studies provide separate
building blocks for
AI/data, culture,
recommendation, and
merchandising.
No confirmed end-to-end
framework links all four
dimensions in one
adaptive decision system.
CAMI-DM integrates
the streams at the
architecture level.
Dynamic
feedback
Real-time analytics and
behavior traces are
increasingly available.
Explicit state → decision
→ response → update
loops are under-specified
for multicultural
merchandising.
Introduce temporal
feedback and state
transition.
Cultural
representation
Hofstede, individualism,
mianzi, Buddhist
reflection,
holistic/analytic thinking
are used.
Cultural context is often
single-construct or
country-level.
Use a multidimensional
cultural ontology.
Spatial
optimization
Studies address visual
presentation, space and
retail interiors.
Cultural adaptation is not
jointly optimized with
shelf/slot assignment.
Use QAP with cultural
utility and distance
constraints.
Physical-digital
integration
Studies are rich within
individual channels.
A common decision
architecture across
physical, digital and
phygital contexts is
missing.
Model merchandising
decisions as channel-
adaptive outputs.
Business and
experience
outcomes
Studies report purchase,
satisfaction, trust,
engagement, or strategic
outcomes.
No common chain from
cultural relevance to
CX/trust/behavior and
commercial KPIs.
Link perceptual
outcomes to POS/e-
commerce and journey
metrics.

Research gap
Despite significant advances in AI-enabled retail analytics, data-driven personalization, consumer
behavior modeling, and merchandising optimization, the existing literature remains fragmented across
technological, behavioral, commercial, and cultural dimensions. In particular, cultural factors are often
treated as contextual or geographic attributes rather than as multidimensional variables that can
dynamically influence merchandising decisions. Moreover, existing approaches provide limited
conceptual integration between behavioral data, cultural context, real-time situational factors,
merchandising adaptation, customer response, and feedback mechanisms. This fragmentation reveals
a need for an integrated framework capable of dynamically adapting merchandising decisions to
heterogeneous cultural and behavioral contexts while incorporating consumer responses into a
continuous learning process. To address this gap, this study proposes the Culturally Adaptive, AI- and

Data-driven Merchandising (CAMI-DM ) framework, which conceptualizes the sequential and
feedback-based relationships between behavioral data, cultural context, Adaptive Cultural Intelligence,
context-aware adaptation, merchandising decisions, customer experience, and behavioral response.
Scopus was selected as the primary bibliographic database because of its broad multidisciplinary
coverage and its relevance to the intersection of artificial intelligence, data analytics, retail, consumer
behavior, marketing, and cultural studies. Its advanced search functions and structured bibliographic
metadata also facilitate the reproducible identification, screening, and bibliometric analysis of the
literature relevant to the CAMI-DM framework
6. The CAMI-DM Framework
CAMI-DM (Culturally Adaptive, AI- and Data-driven Merchandising) is proposed as an integrative
architecture for translating consumer signals and contextual knowledge into adaptive merchandising
decisions. The framework contains five layers:
1. data and context sensing,
2. adaptive cultural intelligence,
3. context-aware adaptation,
4. merchandising optimization, and
5. consumer/commercial response with feedback.
The architecture is intentionally modular so that a retailer can implement a subset of the components
while preserving the conceptual relationships.

Figure 2 : CAMI-DM conceptual architecture

:

With :
𝑆௧  =  {ܤ௧, ܥ௧, ܺ௧, ܴ௧−1}
ܫܥܣ௧  =  ܹ(ߪ஻ܤ௧ + ܹ஼ܥ௧ + ܹ௑ܺ௧ + ܹோܴ௧−1 + )ܾ
ܧܣܥ௧  =  ܫܥܣ(݃௧ܥ௧, 𝑆௧, ܯ௧ ௖௔௡ௗ௜ௗ௔௧௘, ݏݐ݊݅ܽݎݐ݊݋ܿ௧)
And
ܯ௧ ∗  =   ݃ݎܽ min ௫ [ ݐݏ݋ܿ ݈ܽ݅ݐܽ݌ݏ −  ݕݐ݈݅݅ݐݑ ݈ܽݎ݋݅ݒܽℎܾ݁/݈ܽݎݑݐ݈ݑܿ]
6.1. State representation
Let the retail state at time t be represented as St = {Bt, Ct, Xt, Rt-1}, where Bt denotes behavioral signals, Ct
denotes multidimensional cultural context, X t denotes situational and operational conditions such as stock, price,
seasonality, store load, channel, and local events, and R t−1 summarizes the observed response from the previous
decision cycle. The state representation is dynamic because each merchandising decision can modify the subsequent
behavioral and commercial environment. The state transition can therefore be expressed as :
CULTURAL CONTEXT (Ct)
BEHAVIORAL DATA (Bt)
ACIt
Adaptive
Cultural
Intelligence
CAEt
Context-
aware
Adaptation
SITUATIONAL
CONTEXT(Xt)

ܯ௧ ∗ ܫܦܰܪܥܴܧܯ𝑆ܩܰܫ

PHYSICAL
/
SPACIAL

DIGITAL
/
PHYGITAL

CXt
TRUSTt
BRt
Pt
Rt
ACIt+1

𝑆௧+1 =  (݂𝑆௧, ܯ௧, ܴ௧,  ௧ )
where M t is the merchandising decision, R t is the observed response, and  ௧ represents unobserved
factors and stochastic variation.
This formulation makes CAMI-DM explicitly adaptive : a subsequent merchandising decision is
allowed to differ from the previous decision when behavioral, cultural, situational, or response
information changes.
6.2. Adaptive Cultural Intelligence
The latent computational layer ACI t (Adaptive Cultural Intelligence) combines behavioral and
contextual information:
ACIt  =  σ(WBBt + WCCt + WXXt + WRRt−1 + b)
Here, σ() is a bounded activation or calibration function, the W terms are learned weights, and b is an
intercept. In a machine-learning implementation, ACI t may be implemented through a supervised
model, embedding model, graph model, or hybrid recommender. In a managerial implementation, it
can be represented by a weighted score. The important theoretical point is that cultural context is an
explicit input rather than an afterthought.
6.3. Context-Aware Adaptation Engine
The Context-Aware Adaptation Engine (CAE t) translates ACI t into a candidate set of merchandising
actions while applying cultural, operational, ethical, and inventory constraints. Conceptually:
CAEt  =  g(ACItCt, St, Mt candidate, contraintst)
The candidate set may include changes in product adjacency, facings, shelf position, visual display,
signage language, promotional emphasis, digital recommendation order, or navigation cues. Cultural
adaptation should be expressed as compatibility or relevance, not as deterministic assumptions about
individuals.
6.4. Spatial optimization with QAP
For shelf, aisle, or planogram decisions, CAMI-DM treats spatial merchandising as an assignment
problem. Let i and j index products or categories, k and l index locations, F ij,t be a behavioral flow or
affinity between products i and j, Dkl be the distance between locations k and l, and Uik,t be the expected
utility of assigning product i to location k after cultural and behavioral adaptation. Let xik,t equal 1 when
product i is assigned to location k and 0 otherwise. The proposed optimization is:
ܯ௧ ∗ =   ݃ݎܽ min ௫ [ ∑ ܨ௜௝,௧ܦ௞௟ݔ௜௞,௧ݔ௝௟,௧  −  
௜,௝,௞,௟
∑ ܷ௜௞,௧ݔ௜௞,௧
௜,௞
]
subject to one-to-one assignment and capacity constraints, with x ik,t ∈ {0,1}. The first term represents
flow-weighted movement or interaction cost; the second term rewards culturally and behaviorally
relevant placements. The distance matrix should satisfy the metric property D kl ≤ D km + D ml for all
feasible locations k, l, and m. The triangle inequality is therefore used as a consistency condition on
the spatial metric, not as a claim that the resulting planogram is automatically optimal.
This formulation creates a clear division of labor. Machine learning or analytics estimates F and U; the
cultural ontology informs U and adaptation constraints; the QAP solves the spatial assignment layer;

and observed responses feed the next cycle. The approach also permits direct comparisons between a
conventional objective function and an adaptation-aware objective function.
7. Testable Propositions and Hypotheses
Table 6: Research Hypotheses, Structural Relationships, and Theoretical Foundations of the
CAMI-DM Framework
Hypothesis Path Rationale
H1 PBD  ACI
Higher-quality and more relevant behavioral signals improve
the adaptive system’s ability to infer actionable consumer
context.
H2 CCR  CAE A richer representation of cultural context improves contextual relevance of merchandising actions.
H3 SAR  CAE Seasonality, store load, channel, and local context improve adaptation when incorporated alongside cultural information.
H4 Feedback  ACI Observed prior responses improve subsequent adaptive intelligence through model updating.
H5 ACI  CAE
Stronger adaptive cultural intelligence improves the
consistency between inferred context and merchandising
actions.
H6 CAE  CX
Greater contextual relevance of merchandising improves
customer experience.

H7 CX  Trust A more contextually appropriate experience improves trust and perceived value, subject to privacy and transparency conditions.
H8 CAE  BR
Greater contextual relevance of merchandising actions directly improves
consumer behavioral response, including engagement, purchase
intention, or purchase probability.
H9 TRUST  BR Higher trust and greater perceived control strengthen favorable consumer responses to AI-mediated merchandising.
H10
(moderation)
CAE  CX 
TRUST  BR
(Mediation by CX
and TRUST)
The effect of merchandising contextual relevance on behavioral response
can be indirectly transmitted through improved customer experience and
enhanced trust.
H11
(moderation) ACI×CCR  BR The effect of adaptive cultural intelligence on behavioral response varies according to the consumer’s cultural-context representation.

8. Empirical Validation Agenda
The systematic review does not empirically test H1 –H11. They are propositions derived from the
synthesis and should be validated in a subsequent field or experimental study. A suitable design is a
two-condition comparison between conventional merchandising and culturally adaptive
merchandising, with random assignment where feasible. The target setting can combine physical-store
observation with digital interaction data so that perceptual measures from a questionnaire are linked to
behavioral and commercial indicators.

8.1. Measurement model
For a subsequent PLS-SEM study, behavioral-data quality (PBD), AI adaptiveness (AIA), cultural-
context representation (CCR), situational adaptation (SAR), customer experience (CX), trust/perceived
control (TRUST), and behavioral response (BR) can be operationalized as reflective or formative
constructs depending on their theoretical definitions. Items should be adapted from validated scales
and pretested in the target population. The measurement assessment should report indicator reliability,
internal consistency, convergent validity, discriminant validity, and collinearity diagnostics. SmartPLS
documentation currently summarizes common benchmarks such as outer loadings around 0.70 or
above, AVE ≥ 0.50, HTMT ≤ 0.85 as a conservative criterion, and VIF ≤ 3 as a common target; these
are guidelines rather than mechanical acceptance rules (SmartPLS, 2026).
8.2. Classical versus culturally adaptive conditions
A controlled scenario experiment can compare a standard merchandising condition with a culturally
adaptive condition while holding prices, availability, product quality, store size, and promotional
budget constant. The manipulation should vary only the elements justified by the cultural adaptation
logic, such as product adjacency, visual context, signage, language, or recommendation ordering.
Manipulation checks should verify perceived relevance and authenticity without inducing demand
characteristics. Consumer autonomy should remain explicit: participants should be free to ignore,
reject, or override recommendations.
8.3. Multi-group and predictive analysis
When comparing culturally distinct groups, measurement invariance should be examined before
interpreting between-group path differences. MICOM followed by an appropriate multigroup analysis
can be used in SmartPLS. Out-of-sample predictive performance should also be evaluated, for example
with PLSpredict, rather than relying only on in-sample explanatory power (SmartPLS, 2026).
8.4. Outcome variables
Table 7: Outcome Families and Candidate Measures for Evaluating the CAMI-DM Framework
Outcome family Candidate measures
Behavioral Conversion, purchase probability, basket composition, repeat visit, dwell time, path length, recommendation acceptance.
Experience Perceived relevance, cognitive ease, emotional response, satisfaction, perceived personalization.
Relational Trust, perceived transparency, perceived control, privacy concern.
Commercial Average basket value, sales by category, cross-selling, revenue per visit, margin contribution, ROI.
Spatial Walking distance, aisle congestion, product visibility, adjacency quality, travel cost.
Equity/ethics Disparate recommendation exposure, unnecessary profiling, opt-out availability, perceived autonomy.

9. Discussion
The literature synthesized in this review suggests that the central challenge is no longer whether
retailers can personalize. The challenge is whether personalization can remain contextually appropriate
when consumers, products, channels, and situations change. The included studies provide a strong
empirical and conceptual basis for each component of that challenge but stop short of a unified
architecture. The CAMI-DM framework addresses the fragmentation by treating behavioral signals,
cultural context, and situational context as joint determinants of an adaptive merchandising state.
The framework also changes how culture is conceptualized in retail analytics. Rather than coding a
consumer by nationality and applying a fixed cultural rule, CAMI-DM proposes a multidimensional
representation that can include values, beliefs, language practices, symbolic preferences, seasonal
patterns, local product affinity, digital behavior, and explicit feedback. Such a representation is close r
to the way contemporary multicultural markets operate and better aligned with the need for dynamic
updating. It also creates a methodological requirement: cultural variables must be measured or inferred
transparently and validated rather than assumed from demographic labels.
The QAP component extends the framework from recommendation to physical decision making.
Traditional AI personalization can decide which product or message is relevant to whom, but a store
also has to decide where products should be placed, which products should be adjacent, and how the
arrangement affects travel and interaction costs. QAP provides a mathematically explicit way to
connect behavioral flows and spatial distances. The cultural utility term makes it possible to c ompare
a purely efficiency-oriented planogram with one that incorporates contextual relevance. The triangle
inequality constraint protects the internal consistency of the distance metric but does not by itself
establish commercial superiority.
9.1. Theoretical implications
CAMI-DM contributes to retailing theory by connecting four research traditions that are often
separated: consumer-behavior analytics, AI-enabled personalization, cross-cultural consumer research,
and spatial/experiential merchandising. It also shifts the role of culture from a descriptive moderator to
an actionable input in a decision architecture. Finally, the state-and-feedback formulation turns
adaptive merchandising into a sequential decision problem, creating a bridge between static
segmentation models and dynamic learning systems.
9.2. Managerial implications
For retailers, the framework suggests that data collection should be organized around decisions rather
than around technology acquisition. The relevant question is which signal can improve a merchandising
decision and whether the signal is legitimate and sufficiently reliable. Physical stores can combine POS
and movement data with carefully designed cultural-context information. Digital retailers can combine
browsing, review, and recommendation responses with culturally relevant interface variables. Phygital
systems can connect the two. Across all settings, the adaptation engine should preserve customer
choice, provide understandable explanations when appropriate, and minimize unnecessary profiling.
For emerging markets, the framework also supports locally grounded experimentation. In a Côte
d’Ivoire setting, for example, a research program could compare conventional and culturally ad aptive
presentation of locally relevant products, language/signage choices, visual conventions, seasonal
assortments, and product adjacencies, while measuring customer response and operational effects. Such

work would provide evidence from a context that is underrepresented in the current corpus without
assuming that one national profile captures all consumers.
10. Limitations and Future Research
Several limitations should be acknowledged. First, Scopus was the sole bibliographic database used,
and the search was limited to scientific articles and reviews published in English. This choice made it
possible to establish a focused corpus based on an international bibliographic source widely used for
scientific literature reviews. However, relevant studies indexed in other databases or published in other
languages may not have been identified. This limitation may therefore introduce a bibliographic
coverage bias and restrict the comprehensiveness of the corpus analyzed.
Second, 2026 is an incomplete publication year because the search was conducted in September.
Third, the joint relevance criteria intentionally prioritized studies located at the intersection of AI and
data, retail, and culture. This approach produces a focused synthesis, but one that is relatively narrow
in scope.
Fourth, three reports could not be retrieved during the eligibility assessment stage and were therefore
not included in the final synthesis.
Fifth, the study proposes the CAMI-DM framework but does not yet undertake its empirical validation.
Its hypotheses and mathematical components therefore remain to be empirically tested.

11. Conclusion
This review reframes intelligent multicultural merchandising as an integration problem. The screened
literature demonstrates that AI and behavioral analytics can support personalization, that cultural
context can alter responses to AI and retail environments, and that physical, digital, and phygital
merchandising can be increasingly data-driven. What remains fragmented is the end-to-end connection
between these elements. The CAMI-DM framework addresses this gap by linking behavioral and
contextual sensing, adaptive cultural intelligence, context-aware merchandising, spatial optimization,
customer experience, trust, behavioral response, commercial performance, and feedback- driven
updating. The QAP formulation provides a specific mathematical layer for physical placement
decisions, while the proposed empirical agenda provides a pathway for testing the framework in real
retail settings. The framework should be regarded as a research architecture to be validated and refined,
not as a claim that cultural adaptation is universally beneficial or that AI should determine consumer
choices. Its core objective is to enable context-sensitive retail decision making while preserving
measurement rigor, transparency, and consumer autonomy.
Declarations
Funding: No external funding is declared in this manuscript draft; replace this statement if funding
applies.
Conflict of interest: The author declares no conflict of interest, subject to journal requirements.
Data availability: The Scopus export underlying the search can be made available to reviewers or
readers where permitted by Scopus licensing and institutional access conditions.
Generative AI disclosure: Generative AI tools were used for language editing, document structuring,
and research-writing assistance during manuscript preparation. The author remains fully responsible
for the accuracy of the references, search strategy, screening decisions, data extraction, interpretations,
mathematical formulations, and scientific claims presented in the manuscript.

References
Akhtar, W. H., Watanabe, C., Tou, Y., & Neittaanmäki, P. (2022). A new perspective on the textile
and apparel industry in the digital transformation era. Textiles, 2(4), 633 –656.
https://doi.org/10.3390/textiles2040037
Baingam, C., & Wittayakom, S. (2026). Consumer attitudes toward unmanned convenience stores in
Thailand: Applying the Yonisomanasikara approach. Journal of Buddhist Anthropology, 11(1),
176–197. https://so04.tci-thaijo.org/index.php/JSBA/article/view/284641
Becker, L., & Jaakkola, E. (2020). Customer experience: Fundamental premises and implications for
research. Journal of the Academy of Marketing Science, 48, 630–648.
Bitner, M. J. (1992). Servicescapes: The impact of physical surroundings on customers and employees.
Journal of Marketing, 56(2), 57–71.
Davenport, T., Guha, A., Grewal, D., & Bressgott, T. (2020). How artificial intelligence will change
the future of marketing. Journal of the Academy of Marketing Science, 48, 24–42.
de Mooij, M. (2019). Consumer behavior and culture: Consequences for global marketing and
advertising (3rd ed.). SAGE.
DrŁze, X., Hoch, S. J., & Purk, M. E. (1994). Shelf management and space elasticity. Journal of
Retailing, 70(4), 301–326.
Henseler, J., Ringle, C. M., & Sarstedt, M. (2016). Testing measurement invariance of composites
using partial least squares. International Marketing Review, 33(3), 405–431.
Hofstede, G. (2001). Culture’s consequences: Comparing values, behaviors, institutions and
organizations across nations (2nd ed.). SAGE.
Hübner, A., Kuhn, H., & Sternbeck, M. G. (2013). Demand and supply chain planning in grocery retail:
A classification of decision situations. International Journal of Retail & Distribution Management,
41(3), 171–199.
Landim, A. R. D. B., Beltrªo Moura, J. A., de Barros Costa, E., Vieira, T., Wanick Vieira, V., Bazaki,
E., & Medeiros, G. P. (2025). Analysing the effectiveness of chatbots as recommendation systems
in fashion online retail: A Brazil and United Kingdom cross-cultural comparison. Journal of Global
Fashion Marketing, 16(3), 295–321. https://doi.org/10.1080/20932685.2025.2491323
Lemon, K. N., & Verhoef, P. C. (2016). Understanding customer experience throughout the customer
journey. Journal of Marketing, 80(6), 69–96.
Liu, Q., & Pareti, M. (2026). AI-driven sentiment analysis of grape wine consumers: A comparative
study between China and Italy. Journal of Retailing and Consumer Services, 93, 104888.
https://doi.org/10.1016/j.jretconser.2026.104888
Niu, B., Yu, X., & Dong, J. (2023). Could AI livestream perform better than KOL in cross-border
operations? Transportation Research Part E: Logistics and Transportation Review, 174, 103130.
https://doi.org/10.1016/j.tre.2023.103130
Niu, Y., Feng, Y., Li, B., & Ma, B. (2026). When “Mianzi” meets artificial intelligence: Exploring
cultural and technological effects on B2B brand dependence. Journal of Business-to-Business
Marketing, 33(1), 25–43. https://doi.org/10.1080/1051712X.2025.2537418
Page, M. J., McKenzie, J. E., Bossuyt, P. M., Boutron, I., Hoffmann, T. C., Mulrow, C. D., et al. (2021).
The PRISMA 2020 statement: An updated guideline for reporting systematic reviews. BMJ, 372,
n71. https://doi.org/10.1136/bmj.n71
Putri, N. F., Hameed, A., Akin, M., Akin, I., Khan, M. Z., Banerjee, S., & Zaidi, S. M. T. (2025).
Analysing the modest fashion market: An empirical study of e-commerce best-selling products.
Journal of Islamic Marketing, 16(3), 841–869. https://doi.org/10.1108/JIMA-03-2024-0142
Ratnayake, J. C., Jayasuriya, N., Suraweera, T., & De Silva, L. (2026). Integrating industry 4.0 and 5.0
technologies in luxury fashion retail interiors: A systematic review of digital transformation,

sensory design, and brand storytelling. Social Sciences & Humanities Open, 13, 102798.
https://doi.org/10.1016/j.ssaho.2026.102798
Schmitt, B. (1999). Experiential marketing. Free Press.
SmartPLS. (2026). Result color thresholds and multigroup procedures in SmartPLS reports. SmartPLS
documentation. https://www.smartpls.com/documentation/functionalities/thresholds/
Sun, Y. (2025). Digital communication insights from museum visitor data: Association rule mining for
targeted engagement. Fonseca, Journal of Communication, 29(2), 51 –69. https://revistas-
fonseca.com/index.php/2172-9077/article/view/735
Turley, L. W., & Milliman, R. E. (2000). Atmospheric effects on shopping behavior: A review of the
experimental evidence. Journal of Business Research, 49(2), 193–211.
Wang, A., Pan, J., Jiang, C., & Jin, J. (2023). Create the best first glance: The cross-cultural effect of
image background on purchase intention. Decision Support Systems, 170, 113962.
https://doi.org/10.1016/j.dss.2023.113962
Wedel, M., & Kannan, P. K. (2016). Marketing analytics for data-rich environments. Journal of
Marketing, 80(6), 97–121.
Appendix A. Recommended empirical implementation of CAMI-DM
A practical field implementation can proceed in four phases. Phase 1 develops and validates the cultural
ontology with local experts and consumers. Phase 2 integrates POS, loyalty, navigation,
recommendation, and contextual data and estimates behavioral-affinity matrices. Phase 3 compares
conventional and culturally adaptive merchandising through controlled scenarios or A/B tests. Phase 4
feeds observed outcomes into the adaptation engine and re-solves the spatial assignment problem. The
same architecture can be used for a small pilot store or a larger multi-store experiment, provided da ta
governance and consent requirements are respected.
For a Côte d’Ivoire pilot, the ontology can be designed to capture language preference, locally relevant
product categories, visual and symbolic conventions, seasonal events, purchase routines, explicit
consumer preferences, and belief/religion-related product requirements only where consumers
voluntarily provide or where legitimate business processes require them. The objective is not to infer
identity from appearance or ethnicity, but to use validated contextual signals to improve relevance and
consumer choice.
