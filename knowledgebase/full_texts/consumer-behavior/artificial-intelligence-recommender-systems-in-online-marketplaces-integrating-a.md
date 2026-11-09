---
title: Artificial intelligence recommender systems in online marketplaces integrating architectures consumer
  behavior and personalization
url: https://doi.org/10.1007/s44163-026-02182-3
category: consumer-behavior
subcategory: empirical
date: 2026-09
venue: Discover Artificial Intelligence
authors:
- Arianis Chan
- Rani Sukmadewi
- Che Aniza Che Wel
source: openalex-oa
pdf_url: https://link.springer.com/content/pdf/10.1007/s44163-026-02182-3.pdf
pages: 29
chars: 101123
fetched_at: '2026-11-08T19:03:05+00:00'
kb_version: 1
---

# Artificial intelligence recommender systems in online marketplaces integrating architectures consumer behavior and personalization

Discover Artificial IntelligenceChan et al. Discover Artificial Intelligence          (2026) 6:1131
https://doi.org/10.1007/s44163-026-02182-3
REVIEW Open Access
Artificial intelligence recommender systems
in online marketplaces integrating architectures
consumer behavior and personalization
Arianis Chan1*, Rani Sukmadewi2, Che Aniza Che Wel3, Aurora Yupita Achmada1 and Cecep Safa’atul Barkah1
*Correspondence:
Arianis Chan
arianis.chan@unpad.ac.id
1Department of Business
Administration, Faculty of Social
and Political Sciences, Universitas
Padjadjaran, Bandung, Indonesia
2Sekolah Vokasi, Universitas
Padjadjaran, Bandung, Indonesia
3Faculty of Economics and
Management, Universiti
Kebangsaan Malaysia, Bangi,
Malaysia
© The Author(s) 2026. Open Access  This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use,
sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the
source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article
are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the
article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to
obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.
Abstract
Artificial intelligence (AI)-based recommender systems have become a key
component of personalization in online marketplaces. However, research remains
fragmented across technological, behavioral, and implementation perspectives.
This study synthesizes the literature using a PRISMA-guided systematic review
and bibliometric analysis of 135 Scopus-indexed publications published between
2007 and 2026. The findings reveal rapid growth in scholarly interest, particularly
after 2020, driven by the increasing adoption of AI-driven personalization.
Methodologically, the field is dominated by machine learning, collaborative filtering,
deep learning, and hybrid recommender approaches. Six thematic clusters were
identified, covering recommendation techniques, consumer behavior, predictive
analytics, user experience, platform environments, and system integration. The
review also highlights a persistent gap between experimental model performance
and scalable marketplace deployment. By integrating technological, behavioral, and
infrastructural perspectives, this study provides directions for developing transparent,
scalable, and consumer-centered AI personalization strategies in digital commerce.
Keywords AI-based recommender systems, Online marketplaces, Personalization,
Explainable AI, Consumer behavior
1 Introduction
The rapid integration of artificial intelligence (AI) into digital commerce has trans -
formed online marketplaces from transaction-oriented platforms into intelligence-
driven ecosystems. AI is increasingly positioned as a central mechanism associated
with consumer–platform interactions through automated decision processes and data-
driven personalization [10]. AI-based recommender systems are altering how customers
explore, assess, and choose products in modern marketplace situations by progressively
mediating product discovery, recommendation, and user engagement [ 62, 70]. This shift
is directly related to the increasing strategic significance of personalization and predic -
tive analytics in highly competitive digital markets, where AI makes it possible to imple -
ment adaptive strategies that may be associated with customer satisfaction and loyalty,

Page 2 of 29
Chan et al. Discover Artificial Intelligence           (2026) 6:1131
such as tailored product offerings, targeted communications, and personalized pricing
[3, 43]. The increased reliance on algorithmic tools to improve user experience, effi -
ciency, and responsiveness was exacerbated by the post-pandemic acceleration of online
adoption. But while the ethical use of AI systems is widely acknowledged as essential to
maintaining customer trust, this expansion has also brought up important issues around
data privacy, algorithmic bias, and transparency [ 19, 52]. AI-based recommender sys -
tems have a growing impact on consumer journeys and platform performance as mar -
ketplaces move toward more automated and adaptive architectures. These mechanisms
operate through both technical optimization and cognitive and affective processes that
may support psychological engagement and long-term customer relationships [28, 32].
To synthesize the expanding body of research on AI-based recommender systems, it is
essential to anchor the analysis in established behavioral and psychological frameworks.
Prior studies frequently employ the Stimulus–Organism–Response (S–O–R) model to
explain how algorithmic design features such as personalization intensity, transparency
cues, and adaptive interfaces function as stimuli that shape internal cognitive and affec -
tive states, ultimately influencing behavioral outcomes [4, 18, 29, 37, 49, 53]. Within digi-
tal marketplaces, these algorithmic stimuli are associated with consumers’ perceptions
of relevance, usefulness, and trust, thereby structuring decision-making processes.
Complementing this perspective, the Theory of Planned Behavior (TPB) explains how
attitudes, subjective norms, and perceived behavioral control shape purchase inten -
tions in online environments [ 2, 51]. Recent studies further confirm the continued rel -
evance of TPB in AI-driven digital commerce contexts, particularly in shaping consumer
responses to algorithmic recommendations [ 15, 29, 45, 63, 71]. In particular, transpar -
ency mechanisms such as explanation interfaces may enhance perceived behavioral con-
trol and may reduce uncertainty in algorithmic decision-making, while personalization
depth and ranking logic may influence consumers’ attitudes toward recommendations
[1, 46].
While S–O–R and TPB provide robust behavioral foundations for understanding
consumer responses [ 2, 51], prior research has predominantly examined algorithmic
performance and behavioral outcomes in isolation [ 10]. In AI-driven marketplace envi -
ronments, algorithmic features such as personalization depth, adaptive ranking, and
explainability function not merely as technological tools but as structured stimuli that
shape cognitive evaluations, perceived control, trust formation, and subsequent behav -
ioral responses [ 14]. Despite the explanatory value of these frameworks, existing stud -
ies rarely integrate behavioral theories with specific AI architectures and infrastructural
considerations, resulting in a conceptual divide between algorithmic optimization and
consumer psychology. Consequently, limited efforts have systematically mapped archi -
tectural characteristics onto established behavioral mechanisms. By synthesizing archi -
tectural, behavioral, and infrastructural perspectives, this review seeks to bridge this
divide and clarify how AI-based recommender systems are associated with consumer
decision-making processes in digital marketplace environments.
Recent years have witnessed a rapid expansion of scholarly interest in AI-based rec -
ommender systems within online marketplace contexts. The proliferation of stud -
ies reflects the accelerating integration of machine learning, deep learning, and hybrid
architectures into digital commerce environments. However, this rapid growth has also
produced conceptual dispersion, methodological heterogeneity, and uneven attention to

Page 3 of 29
Chan et al. Discover Artificial Intelligence           (2026) 6:1131
infrastructural and behavioral dimensions. As research advances across technological,
consumer, and platform-level perspectives, a structured synthesis is needed to consoli -
date fragmented findings and clarify dominant research trajectories. This review con -
tributes to the artificial intelligence literature by clarifying how recommender system
architectures, behavioral mechanisms, and marketplace deployment considerations
interact within digital commerce environments. In addition, the review highlights
emerging challenges related to explainability, scalability, transparency, and real-world
implementation of AI-based recommender systems. Furthermore, the review synthe -
sizes the roles of machine learning, deep learning, collaborative filtering, and hybrid
recommender architectures in shaping personalization outcomes and deployment strat -
egies across digital marketplace environments.
1.1 Identification of research gaps
Despite the rapid expansion of AI-based recommender systems research, several criti -
cal limitations hinder both theoretical advancement and practical deployment. First,
an implementation gap persists between high-performing algorithmic prototypes and
production-ready marketplace systems. While numerous studies emphasize predictive
accuracy and model optimization, limited attention is given to issues of infrastructure
scalability, data governance, privacy compliance, and integration with existing enterprise
architectures [ 26]. This imbalance constrains the translation of experimental models
into sustainable marketplace solutions.
Second, a conceptual fragmentation exists between algorithm-centric and behavior-
centric research streams. Technical studies frequently conceptualize consumers as opti -
mization targets, focusing primarily on error reduction and predictive performance.
Conversely, behavioral research often treats AI systems as undifferentiated “black boxes, ”
without distinguishing between specific architectural features and their psychological
implications [12]. The absence of integrative frameworks linking algorithmic design to
consumer-level mechanisms limits cumulative knowledge development. Third, ethical
and long-term considerations remain insufficiently synthesized. As AI-driven personal -
ization intensifies, concerns related to transparency, explainability, algorithmic bias, and
consumer autonomy become increasingly salient [12].
However, systematic integration of these concerns with marketplace performance
outcomes—such as trust sustainability, brand loyalty, and algorithm fatigue—remains
underdeveloped [ 29]. A structured synthesis is therefore necessary to clarify how
technological, behavioral, and ethical dimensions interact within evolving digital mar -
ketplaces. Collectively, these limitations indicate that the field lacks an integrative per -
spective capable of linking AI architectures, consumer responses, and marketplace
deployment considerations. Addressing this gap is essential for advancing both theoreti -
cal understanding and practical implementation of AI-based recommender systems.
1.2 Research urgency and contribution
The increasing integration of AI-based recommender systems into online marketplaces
underscores the need for a structured and integrative synthesis. As digital commerce
environments become more automated and data-intensive, understanding how algo -
rithmic architectures interact with consumer-level psychological mechanisms becomes
essential for both theory development and practical implementation. Without such

Page 4 of 29
Chan et al. Discover Artificial Intelligence           (2026) 6:1131
integration, the growing body of research risks remaining fragmented across technical,
behavioral, and organizational domains, limiting its cumulative contribution to both AI
scholarship and marketplace practice. To address this challenge, this study conceptu -
ally bridges fragmented research streams by integrating S–O–R and TPB perspectives
with AI-specific architectural considerations, thereby providing an integrative view of
how recommender system architectures, consumer-level mechanisms, and marketplace
deployment considerations interact within digital commerce environments.
Existing review studies have generally focused on recommender system algorithms,
recommendation accuracy, or consumer-related outcomes separately. While these
reviews have generated valuable insights, they rarely examine the interactions among
AI architectures, behavioral mechanisms, and marketplace implementation challenges
within a unified analytical perspective. Unlike prior reviews that predominantly empha -
size either algorithmic performance or isolated behavioral outcomes, this study offers
an integrative synthesis that simultaneously examines technological architectures, con -
sumer-level mechanisms, and infrastructural implementation within online marketplace
environments.
Methodologically, the study employs a hybrid Bibliometric–Systematic Literature
Review (B-SLR) approach, combining qualitative synthesis with quantitative mapping
techniques [22, 54]. This approach enables the identification of dominant research tra -
jectories, conceptual gaps, and underexplored domains. By clarifying the implementa -
tion gap between experimental models and scalable marketplace systems, the review
provides a structured roadmap for future research on transparent, scalable, and con -
sumer-centered AI personalization strategies.
1.3 Research objectives
The primary aim of this study is to examine the evolution of AI-based recommender sys-
tems in online marketplaces and their relationship with consumer behavior. To achieve
this, the study addresses the following research questions (RQ):
RQ1 How has the scholarly production of AI-based recommender systems evolved
between 2007 and 2026, and what are the dominant thematic clusters identified through
bibliometric mapping?
RQ2 How are different AI recommender architectures associated with consumer cogni-
tion, trust formation, and personalization outcomes?
RQ3 What infrastructural and integration barriers limit the transition from experimen-
tal recommender models to production-ready marketplace systems?
RQ4 How do ethical and transparency concerns shape the future research agenda for
responsible AI-driven personalization in digital commerce?
By addressing these questions, this study provides an integrative synthesis of techno -
logical, behavioral, and infrastructural dimensions, offering a structured roadmap for
future research on transparent, scalable, and consumer-centered recommender systems
in online marketplaces. This manuscript is submitted as a review article.

Page 5 of 29
Chan et al. Discover Artificial Intelligence           (2026) 6:1131
1.4 Proposed multi-level framework
Based on the synthesis of prior literature and the identified research gaps, this review
proposes a multi-level framework that integrates three interrelated dimensions of AI-
based recommender systems in online marketplaces. The framework links (1) AI archi -
tecture and system design, (2) consumer cognition and behavioral mechanisms, and
(3) marketplace implementation and deployment outcomes. By integrating technologi -
cal, behavioral, and organizational perspectives, the framework provides a structured
lens for understanding how recommender system architectures are associated with
consumer responses and marketplace-level outcomes. Figure  1 presents the proposed
framework. It is important to note that this framework is conceptual rather than empiri-
cally validated: it is based on a synthesis of the reviewed literature rather than statisti -
cal testing, and it is intended to organize existing knowledge and guide future research
rather than to represent a model with directly tested relationships.
The proposed framework also addresses the implementation gap identified through -
out the reviewed literature by connecting AI architectures, consumer behavioral mech -
anisms, and marketplace-level outcomes within a single analytical structure. While
previous studies have often examined algorithmic performance, consumer responses,
or deployment issues separately, the framework highlights their interdependencies and
provides an integrative perspective for understanding AI-driven personalization in dig -
ital commerce. Furthermore, it offers a foundation for future research on explainable,
scalable, and trustworthy recommender systems.
2 Research method
This study adopts a Systematic Literature Review (SLR) approach guided by the Pre -
ferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA) frame -
work to synthesize research on AI-based recommender systems in online marketplace
contexts and their implications for consumer behavior. The use of PRISMA enhances
methodological transparency, rigor, and reproducibility, thereby strengthening the reli -
ability of the review process [ 56]. The research design follows a structured, multi-stage
procedure encompassing literature search, screening, data extraction, and bibliometric
analysis, as detailed in the following sections.
Fig. 1 Proposed multi-level framework of AI-based recommender systems in online marketplaces

Page 6 of 29
Chan et al. Discover Artificial Intelligence           (2026) 6:1131
2.1 Literature search strategy
The literature search was designed to identify peer-reviewed studies examining AI-
based recommender systems in online marketplace contexts and their implications for
consumer behavior. A structured query was applied to the Title, Abstract, and Keywords
fields (TITLE-ABS-KEY) within the Scopus database to ensure that the core constructs
were central to the retrieved publications.
The query was structured around three conceptual clusters. The first cluster captured
AI-based recommendation technologies, incorporating terms such as recommender
system, artificial intelligence, and machine learning. The second cluster focused on the
marketplace context, including online marketplace  and e-commerce. The third cluster
addressed consumer-related outcomes, such as consumer behavior, purchase intention,
engagement, and loyalty.
Within each cluster, synonymous terms were connected using the Boolean opera -
tor OR, while the three clusters were combined using AND to ensure that only stud -
ies addressing all three dimensions: technology, marketplace context, and consumer
behavior—were retrieved. This approach ensured a focused yet comprehensive identi -
fication of relevant empirical and conceptual studies investigating how AI-powered rec -
ommender systems operate in online marketplaces and are associated with consumer
behavioral responses. The finalized search string is as follows:
TITLE-ABS-KEY ((“recommendation system*” OR recommender*) AND (“artificial
intelligence” OR “machine learning”)) AND TITLE-ABS-KEY ((“online marketplace*” OR
e-commerce)) AND TITLE-ABS-KEY ((“consumer behavior” OR “customer behavior” OR
“purchase intention” OR engagement OR loyalty)))
2.2 Database selection
This study relies exclusively on the Scopus database to retrieve relevant publications.
Scopus was selected because it offers broad multidisciplinary coverage, high-quality
indexing standards, and comprehensive representation of research across artificial intel -
ligence, information systems, and digital commerce disciplines. Its extensive coverage
makes it particularly suitable for systematic literature reviews and bibliometric analy -
ses in rapidly evolving interdisciplinary fields. Furthermore, Scopus provides advanced
bibliometric functionalities that support systematic mapping, trend analysis, and knowl -
edge structure visualization [54].
Given the fast-evolving nature of AI and digital commerce research, the database’s
continuous updating ensures access to recent scholarly contributions. However, reliance
on a single database may limit coverage of certain publications not indexed in Scopus.
While this may introduce potential selection bias, Scopus remains widely recognized as
a robust and reliable source for bibliometric and systematic review studies [22].
2.3 Screening and selection procedure
The search was executed on January 28, 2026, utilizing the constructed search string
within the Title, Abstract, and Keywords fields of the Scopus database. The initial search
yielded a total of 162 records. The screening and selection procedure followed a multi-
stage process aligned with the PRISMA framework [ 56], involving two independent
reviewers (R1 and R2) to enhance reliability and reduce subjective bias.

Page 7 of 29
Chan et al. Discover Artificial Intelligence           (2026) 6:1131
In the first stage (identification), all 162 records retrieved from Scopus were exported
in BibTeX and CSV formats for processing. No duplicate records were identified within
the single-database retrieval. In the second stage (screening), both reviewers indepen -
dently assessed each record based on title and abstract. Studies were evaluated against
predefined inclusion and exclusion criteria (see Table  1). Records were excluded if they:
(a) were not published as journal articles or conference papers ( n = 22); (b) were not
written in English ( n = 1); (c) focused on general AI applications, algorithmic develop -
ment without marketplace contexts, or consumer studies unrelated to AI-driven person-
alization (n = 4); or (d) contained incomplete or erroneous metadata, such as the absence
of author-provided or indexed keywords, which would hinder classification and subse -
quent analysis (n = 0). In total, 27 records were excluded during the screening stage.
Inter-reviewer agreement was assessed upon completion of independent screening.
In cases of disagreement regarding the inclusion or exclusion of specific records, both
reviewers discussed the case and reached a consensus decision. Where consensus could
not be achieved, the third author (senior researcher) served as an adjudicator. Following
this procedure, 135 studies were retained for inclusion in the final analytical dataset.
Figure 2 presents the PRISMA flow diagram summarizing the identification, screen -
ing, eligibility, and inclusion stages.
2.4 Inclusion and exclusion criteria
To ensure systematic and transparent selection of studies, predefined inclusion and
exclusion criteria were established prior to the screening stage. These criteria were
designed to retain publications that directly address the intersection of AI-based rec -
ommender systems, online marketplace contexts, and consumer behavioral outcomes,
Table 1 Inclusion and exclusion criteria
Criteria Inclusion Exclusion Rationale
Topic relevance Studies examining
AI-based recommender
systems in online mar-
ketplace or e-commerce
contexts with implica-
tions for consumer
behavior
Studies on general AI applica-
tions, algorithmic develop-
ment without marketplace
context, pricing/marketing
strategies unrelated to
recommender systems, or
consumer studies not linked
to AI-driven personalization
Ensures alignment with the
three conceptual pillars of the re-
view: AI technology, marketplace
context, and consumer behavior
Document type Peer-reviewed journal
articles and conference
papers
Book chapters, editorials,
letters, reviews, preprints,
theses, and other non-peer-
reviewed documents
Maintains quality control and en-
sures that included studies have
undergone peer evaluation
Language Publications written in
English
Publications not written in
English
Ensures accessibility for synthesis
and minimizes translation-relat-
ed misinterpretation
Database
indexing
Studies indexed in Sco-
pus at the time of search
(January 28, 2026)
Studies not indexed in
Scopus
Scopus provides broad interdis-
ciplinary coverage and advanced
bibliometric functionalities suit-
able for B-SLR studies [22]
Metadata
completeness
Records with complete
bibliographic metadata,
including author-provid-
ed or indexed keywords
Records with incomplete or
erroneous metadata (e.g.,
missing keywords)
Complete keywords are required
for accurate keyword co-occur-
rence analysis, thematic map-
ping, and bibliometric clustering
Timespan Publications from 2007 to
January 2026
No temporal exclusion ap-
plied within this range
Captures the full evolution of the
field from early explorations to
contemporary developments

Page 8 of 29
Chan et al. Discover Artificial Intelligence           (2026) 6:1131
while excluding studies that fall outside this scope. Table  1 summarizes the criteria,
along with the rationale for each decision.

2.5 Data extraction process
Following the selection of the final 135 studies, a structured data extraction protocol was
implemented. Both reviewers independently extracted data from each included publi -
cation using a standardized extraction form. The extraction form captured the follow -
ing information: (a) bibliographic metadata (authors, year, title, source, document type);
(b) research design and methodology (e.g., machine learning, deep learning, collabora -
tive filtering, hybrid models, sentiment analysis, survey-based); (c) AI architecture or
technique employed; (d) marketplace or platform context (e.g., e-commerce, mobile
commerce, social commerce); (e) consumer-level constructs examined (e.g., trust, satis -
faction, purchase intention, engagement, loyalty); and (f) key findings and contributions.
The extraction results from both reviewers were cross-checked for consistency. Dis -
crepancies in coding or categorization were resolved through discussion and, where
necessary, re-examination of the original study. This dual-reviewer extraction process
was designed to enhance the reliability and accuracy of the synthesized dataset.
2.6 Coding procedure and analytical integration
A coding procedure was applied to classify each study along multiple analytical dimen -
sions. Methodological coding categorized each study according to the primary AI
technique(s) employed, based on keyword-based content analysis of abstracts and
author keywords. Because many studies employ multiple techniques, methodological
categories were not treated as mutually exclusive. Thematic coding assigned each study
to one or more conceptual domains (e.g., algorithmic optimization, consumer behavior,
platform infrastructure, ethical considerations) based on the dominant focus identified
in the abstract and full text.
The coding results served as input for two complementary analytical approaches.
First, descriptive bibliometric indicators were generated from the Scopus CSV file using
Fig. 2 PRISMA flow diagram

Page 9 of 29
Chan et al. Discover Artificial Intelligence           (2026) 6:1131
Biblioshiny, the web-based interface of the bibliometrix R package, with the application’s
default calculations and without custom weighting or formula modifications [ 7]. The
Main Information module was used to report the number of sources and documents,
annual growth rate, document average age, average citations per document, cited refer -
ences, authorship, collaboration, and document-type composition. The annual growth
rate represents the compound annual rate of change in publication output across the
observed publication-year series; document average age represents the mean elapsed
time between each publication year and the year of analysis; and average citations per
document represents the arithmetic mean of the Scopus total citation counts across the
135 records. VOSviewer software (version 1.6.20) was then used to generate keyword
co-occurrence networks, identify thematic clusters, and map the intellectual structure of
the field. Second, qualitative thematic synthesis was performed to interpret the substan -
tive content of each cluster, linking bibliometric patterns to theoretical, methodological,
and practical insights. The integration of quantitative bibliometric mapping with quali -
tative synthesis follows the hybrid Bibliometric-Systematic Literature Review (B-SLR)
approach recommended by Donthu et al., [22] and Prada Núñez et al., [54].
2.7 Keyword normalization
Prior to the bibliometric analysis, a keyword normalization process was conducted to
improve the consistency and reliability of the dataset. This process involved standard -
izing semantically identical keywords that appeared in different lexical forms. Keyword
normalization was applied to both author-provided and indexed keywords to reduce
redundancy and enhance the accuracy of keyword co-occurrence mapping, thematic
clustering, and bibliometric analyses.
The normalization was performed manually by both reviewers (R1 and R2) working
independently. Each reviewer examined the complete keyword list exported from Sco -
pus and identified semantically equivalent terms that appeared in variant forms (e.g.,
differences in capitalization, hyphenation, singular versus plural, or abbreviation). After
independent review, the two normalization lists were compared. Discrepancies were
resolved through discussion until full consensus was achieved. The final normalized key-
word list was then applied to the dataset prior to importing it into VOSviewer for biblio-
metric analysis.
No automated software or algorithmic tool was used for the normalization process.
The decision to rely on manual normalization was made to ensure that domain-specific
judgments, particularly regarding the semantic equivalence of technical terms in AI and
e-commerce research, were accurately applied. Table 2 presents the keyword normaliza -
tion decisions applied to the dataset.
Table 2 Keyword normalization
Before normalization After normalization
Artificial Intelligence (a.i.) Artificial Intelligence
Content based filtering Content-based filtering
E- commerce E-commerce
Electronic commerce E-commerce
Machine-learning Machine learning
Personalization Personalization
Recommender systems Recommender system
Users’ experiences User experience

Page 10 of 29
Chan et al. Discover Artificial Intelligence           (2026) 6:1131
2.8 Treatment of methodological quality
Because this study was designed as a hybrid bibliometric-systematic mapping review
rather than a meta-analysis or an effectiveness review, a formal risk-of-bias or meth -
odological quality appraisal tool was not applied. The review instead used predefined
eligibility criteria, independent dual-reviewer screening and data extraction, consensus-
based coding, and metadata completeness checks to support relevance and procedural
consistency. This decision reflects the study’s primary objective of mapping publication
structures, methodological tendencies, and thematic configurations rather than estimat -
ing pooled effects or ranking the strength of evidence from individual studies [ 22]. Nev-
ertheless, the absence of a formal quality assessment means that the synthesis does not
differentiate the included studies according to methodological rigor and should there -
fore be interpreted as a structured map of the available literature rather than a graded
assessment of evidence quality.
3 Results and discussion
3.1 Bibliometric data overview
Following the PRISMA-guided systematic review process, the final dataset consists of
135 publications published between 2007 and 2026 across 52 academic sources. The
annual growth rate of 14.35% indicates a sustained expansion of scholarly attention
toward AI-based recommender systems in online marketplace contexts, particularly in
recent years. The relatively low average document age (2.49 years) further suggests that
this is a rapidly developing and emergent research domain closely aligned with ongoing
technological advancements in artificial intelligence.
From an impact perspective, the reviewed studies exhibit an average of 4.25 cita -
tions per document, supported by a cumulative reference base of 5946 cited works. This
suggests that while the field is relatively young, it is grounded in an established body
of interdisciplinary scholarship. Authorship analysis reveals strong collaborative pat -
terns, with 521 contributing authors and an average of 4.62 co-authors per publication,
reflecting the interdisciplinary and technology-intensive nature of the research area. The
predominance of conference papers, alongside peer-reviewed journal articles, further
highlights the dynamic and innovation-driven character of research on AI-powered rec -
ommender systems in digital marketplace environments (Table 3).
These descriptive indicators collectively suggest that research on AI-based recom -
mender systems in the online markets is still in its early stages but is rapidly consolidat -
ing, with strong collaborative authorship and an increasing interdisciplinary knowledge
base. In terms of research on AI recommender systems, the evidence suggests that the
field is rapidly consolidating but has not yet reached full theoretical and methodological
maturity.
3.2 Scientific production progress
Figure 3 illustrates the temporal distribution of publications, revealing a clear and accel -
erating growth trajectory in research on AI-based recommender systems within market-
place contexts. Prior to 2020, scholarly output was sporadic, reflecting an exploratory
phase of the field. A notable increase emerged in 2020, followed by a sharp surge from
2023 onward, with publication peaks recorded in 2024 (44 documents) and 2025 (48

Page 11 of 29
Chan et al. Discover Artificial Intelligence           (2026) 6:1131
documents). This pattern indicates the maturation of AI-driven personalization research
in parallel with the broader digital transformation of commerce.
The rapid expansion of AI research between 2021 and 2025 may partly reflect struc -
tural shifts in consumer behavior during and after the COVID-19 pandemic. The pan -
demic was associated with accelerated digital adoption and intensified reliance on online
marketplaces, leading firms to prioritize scalable and automated personalization mecha -
nisms [ 10, 27]. As digital consumption increased, marketplaces increasingly leveraged
AI-based recommender systems to enhance user experience, manage large volumes of
behavioral data, and optimize product discovery processes [ 10, 20]. This shift reflects
a transition from transactional e-commerce models toward intelligence-driven ecosys -
tems centered on data analytics and adaptive personalization.
Advancements in machine learning and data analytics further contributed to
this growth. Contemporary recommender systems increasingly employ advanced
Table 3 Data description
Description Results
Timespan 2007–2026
Sources (Journals, Proceedings, etc.) 52
Documents 135
Annual Growth Rate (%) 14.35
Document Average Age (years) 2.49
Average Citations per Document 4.25
References 5,946
Author Keywords (DE) 562
Authors 521
Authors of Single-Authored Documents 0
Single-Authored Documents 0
Co-Authors per Document 4.62
Document Types
Conference Paper 96
Article 39
Total 135
Fig. 3 Scientific production progress

Page 12 of 29
Chan et al. Discover Artificial Intelligence           (2026) 6:1131
architectures to model complex user–item interactions and support personalized rec -
ommendations at scale [57]. Beyond technical performance, the reviewed literature indi-
cates that perceived usefulness and personalization quality are associated with consumer
purchase intentions and engagement in digital marketplaces [14, 45]. As platforms adopt
advanced recommendation algorithms that incorporate historical behavior, contextual
signals, and dynamic profiling, user satisfaction and interaction intensity have become
central performance indicators.
Moreover, the integration of complementary technologies such as augmented reality
(AR) and real-time analytics has expanded the personalization landscape in e-commerce
environments. Immersive and context-aware recommendation mechanisms have been
associated with greater consumer interaction, lower uncertainty, and greater decision
confidence and engagement levels [ 34]. These developments illustrate that personaliza -
tion has evolved beyond static recommendation lists toward interactive and adaptive
consumer journeys.
Finally, predictive analytics capabilities may help marketplaces anticipate consumer
needs and align offerings with emerging demand patterns. By leveraging behavioral data
and advanced modeling techniques, firms may improve operational processes while
achieving closer alignment between product recommendations and consumer prefer -
ences [10, 33]. Rather than merely being associated with conversion-related outcomes,
AI-driven analytics may function as strategic assets that support long-term customer
relationships and sustainable competitive positioning in digital marketplaces.
In summary, the accelerated growth of AI technologies in marketplace research
reflects a structural transformation toward intelligence-based personalization. Driven
by digital adoption, advances in machine learning, and enhanced predictive capabili -
ties, recommender systems have become foundational infrastructures shaping consumer
engagement and marketplace performance. In the context of research on artificial intel -
ligence (AI)-based recommender systems, this growth trajectory indicates that the field
is transitioning from isolated technical experiments toward a more established area of
research, where the adoption of digital technologies, methodological advancements, and
predictive analytics collectively reinforce the strategic relevance of personalization for
market competitiveness.
3.3 Most relevant sources
Figure 4 shows that research on AI-based recommender systems and consumer behavior
in marketplace contexts is predominantly disseminated through conference proceedings
and book series. Lecture Notes in Networks and Systems  appears as the most produc -
tive outlet, followed by ACM International Conference Proceeding Series  and Lecture
Notes in Computer Science , indicating that studies in this field emphasize technologi -
cal innovation and data-driven consumer behavior analysis. This distribution reflects the
fast-evolving nature of AI applications for understanding, predicting, and influencing
consumer decision-making, where conference-oriented venues enable the rapid dissemi-
nation of insights on personalized marketing, recommendation algorithms, and con -
sumer interaction in digital marketplaces.
Figure 5 shows the top ten authors with the highest number of publications. The
author productivity analysis indicates a concentrated contribution pattern, with Loukili,
M. and Messaoudi, F. emerging as the most prolific authors, each contributing five

Page 13 of 29
Chan et al. Discover Artificial Intelligence           (2026) 6:1131
publications. The remaining authors in the top ten—such as Achan, K., Chaudhari, A.,
Fu, Z., Ge, Y., Ghazi, M.E., Kumar, S., Liu, S., and Raut, R.—each contributed two publi -
cations, reflecting a relatively even distribution among secondary contributors. Overall,
this pattern suggests that research on AI-based recommender systems and consumer
behavior in marketplace contexts is driven by a small core of highly productive authors,
supported by a broader network of researchers contributing selectively to the field.
As shown in Fig.  6, the country-level distribution reveals a highly concentrated pat -
tern of publication output, with India leading substantially (52 publications), followed
by China (20) and the United States (11). A second tier of contributors includes Indo -
nesia (8), Morocco (7), and Malaysia (6), while publication output declines sharply
beyond these countries. The concentration of research in India, China, and the United
States suggests a close relationship between scholarly productivity and the availability of
Fig. 5 Most prolific authors

Fig. 4 Most relevant sources

Page 14 of 29
Chan et al. Discover Artificial Intelligence           (2026) 6:1131
large-scale digital marketplaces, consumer data infrastructures, and active AI research
ecosystems. The prominence of India may also reflect the strong representation of con -
ference publications in the dataset, consistent with the fast-moving and technology-ori -
ented nature of AI research.
The presence of emerging economies such as Indonesia, Morocco, and Malaysia high -
lights the growing diffusion of AI-driven personalization research beyond traditionally
dominant technological hubs. This pattern suggests that recommender system research
increasingly develops alongside broader investments in digital transformation, AI inno -
vation, and marketplace modernization. Overall, the findings indicate that advances in
AI-based recommender systems tend to co-evolve with the maturity of digital market
ecosystems, reinforcing the role of recommender systems as a key enabling infrastruc -
ture in contemporary e-commerce environments.
This distribution of sources and geographic production locations indicates that knowl-
edge in this field is largely generated by a few countries through technology-oriented
platforms with rapid publication cycles. This has the potential to accelerate the dissemi -
nation of technical innovations, while theoretical contributions, which progress more
slowly and are published in journals, are relatively underrepresented.
3.4 Most cited documents
An examination of the most cited publications within the dataset provides insight into
the intellectual foundations and dominant research trajectories shaping the field of AI-
based recommender systems in online marketplaces. Rather than merely reflecting pop -
ularity, citation frequency signals influential methodological approaches and conceptual
orientations that have guided subsequent scholarship. Analyzing these highly cited
works allows identification of the paradigms, technological priorities, and behavioral
emphases that structure current research in this domain.
Table 4 presents the three most cited publications in the dataset, providing an over -
view of their key contributions and citation counts.
Fig. 6 Scientific production by country

Page 15 of 29
Chan et al. Discover Artificial Intelligence           (2026) 6:1131
This study analyzes the three most cited publications within the dataset to identify
foundational contributions shaping research on AI-based recommender systems in
online marketplaces. The most highly cited work, Loukili et al., [ 40], with 74 citations,
exemplifies the dominance of performance-oriented algorithmic research in the field.
The study emphasizes the strategic role of recommender systems in enhancing person -
alization and customer engagement within e-commerce environments. By employing
data-driven association rule mining techniques, the authors report the effectiveness of
leveraging historical behavioral data to optimize product recommendations.
The prominence of this study suggests that research impact in this domain has been
strongly associated with methodological innovation and measurable performance
improvements. However, the focus on algorithmic optimization also reflects a broader
trend in which technical efficiency is prioritized over long-term behavioral, ethical, or
infrastructural considerations. This pattern aligns with the fragmentation identified ear -
lier between algorithm-centric and consumer-centric research streams.
From a broader perspective, the prominence of Loukili et al., [ 40] indicates the foun -
dational role of behavior-based and association-rule-driven recommendation techniques
in shaping early-stage personalization research within e-commerce contexts. The study
reflects a phase in which transactional data mining and pattern discovery were central
mechanisms for improving recommendation accuracy and enhancing consumer engage-
ment. Its citation impact suggests that association-rule-based systems have served as a
methodological baseline, providing a reference point for subsequent advancements in
more sophisticated AI-driven approaches.
The second most cited study, Messaoudi and Loukili [44], represents the methodologi-
cal progression toward deep learning–based architectures. By employing deep neural
collaborative filtering to model complex user–item interactions, the study highlights
the shift from rule-based systems to representation learning frameworks capable of cap -
turing nonlinear preference patterns. The citation prominence of this work indicates
growing scholarly emphasis on predictive sophistication and model performance opti -
mization in marketplace environments.
Taken together, these highly cited publications illustrate an evolutionary trajectory
in the field—from rule-based personalization models to advanced neural architec -
tures—highlighting a dominant research orientation toward algorithmic performance
Table 4 Top three most cited documents in the dataset
Author(s) Year Title & key contribution Citations
(Scopus)
Loukili et al. 2023 Machine Learning Based Recommender System for E-Commerce; introduced a
machine learning-based recommender system for e-commerce using associa-
tion rule mining on historical behavioral data; established a widely referenced
methodological baseline for behavior-based personalization.
74
Messaoudi
& Loukili
2024 E-Commerce Personalized Recommendations: A Deep Neural Collaborative Filter-
ing Approach; reported  a transition to deep neural collaborative filtering for
e-commerce personalization; modeled complex nonlinear user–item interac-
tions using representation learning architectures.
44
Geetha &
Renuka
2023 Deep Learning Architecture Towards Consumer Buying Behaviour Prediction Using
Multitask Learning Paradigm; introduced multitask deep learning architectures
for consumer buying behavior prediction; expanded personalization beyond
transactional data by incorporating affective and attitudinal signals from user-
generated content.
12
Citation counts are based on Scopus records as retrieved on May 25, 2026. Only studies present in the final 135-document
dataset are included.

Page 16 of 29
Chan et al. Discover Artificial Intelligence           (2026) 6:1131
enhancement. At the same time, the concentration of impact around methodologi -
cal innovation reinforces the earlier observation that infrastructural scalability, ethi -
cal considerations, and long-term consumer trust dynamics remain comparatively
underexplored.
In the broader research trajectory, this study reflects the ongoing transition from
rule-based and classical machine learning recommender systems toward deep learn -
ing–driven architectures. The citation prominence of this work suggests that scalable,
data-intensive AI techniques have become central to personalization research in digital
marketplace environments. At the same time, the study implicitly highlights persistent
challenges related to data quality and system scalability, which continue to inform subse-
quent methodological advancements.
The third most cited study introduces a complementary perspective by emphasizing
the strategic value of user-generated content (UGC) in recommender systems. Geetha
and Renuka, [25] suggest how deep learning architectures incorporating multitask learn-
ing can capture affective and attitudinal signals extracted from reviews and ratings to
enhance personalization beyond transactional data. This shift toward incorporating
emotional and cognitive dimensions marks a methodological expansion from purely
behavior-based prediction to multidimensional consumer insight modeling.
Collectively, these highly cited works illustrate an intellectual progression in the field
from rule-based optimization to deep learning–driven predictive enhancement, and
toward behavior-aware and sentiment-informed personalization frameworks. However,
the continued dominance of performance-oriented innovation underscores the relatively
limited integration of long-term trust dynamics, ethical considerations, and infrastruc -
tural scalability within the most influential studies. Several of the most-cited articles
suggest that academic recognition has so far been more consistent in valuing method -
ological innovation and predictive performance than contributions addressing trust,
ethics, or application, indicating where the field’s intellectual influence is most evident at
present and where future contributions may discover opportunities to stand out.
3.5 Methodological comparison
Methodologies were identified through keyword-based content analysis of abstracts and
author keywords. As many studies employ multiple techniques, categories are not mutu-
ally exclusive. The methodological comparison reveals that traditional machine learning
approaches dominate the literature, reflecting their early adoption and relative ease of
implementation in recommender systems. The comparative accessibility of traditional
machine learning approaches allows for the rapid development and deployment of rec -
ommender systems. Early efforts in this area focused heavily on simpler algorithms that
required less computational power and could be implemented with relatively limited
data [26].
Collaborative filtering and deep learning methods represent the second most prevalent
approaches, highlighting a clear shift toward data-driven personalization and represen -
tation learning. Collaborative filtering (CF), which includes user-based and item-based
filtering, remains a foundational method in recommender systems. This technique ana -
lyzes patterns of user interactions and preferences to generate recommendations based
on similar users’ behaviors [ 31, 69]. CF is particularly effective in situations where user
preferences are sparse, making it a go-to strategy for many platforms, especially early

Page 17 of 29
Chan et al. Discover Artificial Intelligence           (2026) 6:1131
e-commerce and streaming services [ 31]. Moreover, deep learning allows for the anal -
ysis of intricate patterns within data, enabling personalized recommendations that go
beyond simple user-item interactions. Models that employ convolutional neural net -
works or stacked denoising autoencoders may capture deeper relationships within the
data than traditional CF and are associated with improved personalization performance
[64].
The growing presence of hybrid models and sentiment analysis techniques indicates
an increasing emphasis on integrating behavioral and emotional consumer signals into
recommendation processes. The reviewed literature suggests that hybrid models are
associated with higher recommendation accuracy and user engagement by adapting
dynamically to shifting user preferences and contextual conditions [5, 36].
The methodological distribution in Table 5 shows that the field of AI, particularly rec -
ommender systems is still dominated by engineering-based approaches, with a continu -
ing reliance on traditional machine learning as well as a growing (though still secondary)
adoption of hybrid approaches and sentiment-aware approaches. This indicates a grad -
ual shift rather than a comprehensive one, toward recommendation techniques that are
more behavior-based.
3.6 Co-occurrence analysis
A co-occurrence analysis was conducted using VOSviewer—a specialized software for
building and visualizing bibliometric networks that facilitates the understanding of bib -
liometric relationships by mapping keyword connections, author collaborations, and
journal impact, thereby providing a comprehensive overview of a research field’s devel -
opment [9]. Bibliometric analysis using VOSviewer has been applied in various research
trend mapping studies [ 38]. By examining publication trends over time, this tool helps
detect emerging research directions and open research gaps, thus guiding further stud -
ies. In this study, network visualization generated by VOSviewer based on selected key -
words facilitated the interpretation of complex bibliometric data from Scopus. Figure
7 presents the network visualization generated by VOSviewer, revealing six thematic
clusters: Cluster 1 (red), Cluster 2 (green), Cluster 3 (blue), Cluster 4 (yellow), Cluster 5
(purple), and Cluster 6 (cyan) (Table 6) .
To facilitate a more integrated interpretation of these themes, the findings are subse -
quently discussed through the proposed multi-level framework. The framework orga -
nizes the literature into three interconnected levels: AI architecture, consumer cognition
and behavioral mechanisms, and marketplace implementation outcomes. This perspec -
tive provides a basis for interpreting how technological developments in recommender
systems are associated with consumer responses, marketplace performance, and deploy -
ment outcomes. Accordingly, the thematic clusters identified in this review can be
Table 5 Methodological approaches identified in the reviewed studies
Methodology Number of Studies
Machine Learning (Traditional) 87
Collaborative Filtering 37
Deep Learning / Neural Networks 32
Hybrid Recommender Systems 20
Sentiment Analysis / NLP 19
Association Rule / FP-Growth 7
Bibliometric / SLR / Review 3

Page 18 of 29
Chan et al. Discover Artificial Intelligence           (2026) 6:1131
understood as reflecting different but interconnected aspects of AI-based recommender
systems in digital marketplace environments. In general, Clusters 1 and 3 primarily
relate to AI architecture, Clusters 2 and 4 emphasize consumer cognition and behavioral
mechanisms, while Clusters 5 and 6 focus on marketplace implementation and deploy -
ment considerations.
3.6.1 Cluster 1: AI techniques for recommendation and text-based analysis
Cluster 1 represents the technological foundation of AI-based recommender systems in
e-commerce, emphasizing the use of machine learning, deep learning, natural language
processing (NLP), and sentiment analysis to model consumer preferences and enable
personalization. The literature consistently shows that AI techniques are employed
to transform consumer behavior data, textual feedback, and interaction histories into
actionable recommendation insights. According to Neetika et al., [ 48] and Wu [67], the
reviewed studies suggest that different AI architectures may function as distinct stimu -
lus mechanisms within the S–O–R framework. Deep learning models appear to generate
highly personalized stimuli through latent feature representations, while collaborative
filtering relies on social proof and behavioral similarity. Hybrid architectures may pro -
vide richer and more context-aware stimuli by combining multiple recommendation
approaches and addressing data sparsity and cold-start limitations [ 13]. The depth and
specificity of these stimuli vary across architectures and may be associated with different
organism-level responses, such as perceived relevance, emotional involvement, and trust
[42].
A prominent theme within this cluster is the integration of sentiment analysis and
hybrid AI models to capture emotional and attitudinal dimensions of consumer behav -
ior. Studies by Renjith et al., [ 55] and Geetha and Renuka [ 25] report that combining
Fig. 7 Network visualization

Page 19 of 29
Chan et al. Discover Artificial Intelligence           (2026) 6:1131
sentiment analysis with deep learning and collaborative filtering is associated with
improved recommendation performance by incorporating consumer emotions into the
decision-making process. Similarly, Maher et al., [ 41] highlight the effectiveness of deep
learning architectures in modeling complex buying behavior through multitask learn -
ing and semantic emotion analysis. The growing adoption of hybrid approaches, as
evidenced by Alrashidi et al., [ 5] and Ko et al., [ 33], reflects a broader shift toward com -
bining algorithmic accuracy with behavioral insight. Advances in NLP , including BERT-
based frameworks, further strengthen this trend by enabling nuanced interpretation of
user-generated content. Collectively, Cluster 1 illustrates how AI-driven, text-aware, and
hybrid recommendation models form the methodological backbone of contemporary
research, while also raising emerging concerns related to data privacy, transparency, and
ethical deployment that shape future research directions [12].
Collectively, the findings suggest that recommender systems are evolving from accu -
racy-driven models toward human-centered personalization. Recent developments
increasingly integrate contextual and behavioral signals, highlighting the importance of
balancing algorithmic performance with trust, explainability, and scalable deployment
in digital marketplace environments. The findings also highlight an important trade-off
between predictive accuracy and explainability. While increasingly sophisticated deep-
learning models are often associated with improved recommendation performance, they
Table 6 Keyword clusters
No Cluster 1 Cluster 2 Cluster 3 Cluster 4 Cluster 5 Cluster 6
1 Adversarial ma-
chine learning
Artificial intelligence Classification of
information
Commerce
platforms
Customer
behavior
Data inte-
gration
2 Collaborative
filtering
Behavioral research Consumer behavior Content-based
filtering
E-com-
merce
websites
Online
systems
3 Contrastive
learning
Competition Data handling Learning
algorithms
Websites Recom-
mender
system
4 Deep learning Customer
satisfaction
Data mining Machine learn-
ing algorithms
5 E-commerce
recommender
systems
Customer
segmentation
Decision trees Machine learn-
ing techniques
6 Federated
learning
Decision making E-commerce Mobile
commerce
7 Language
processing
Personalized
recommendation
Forecasting Personalization
8 Machine learning
models
Personalized recom-
mender systems
Learning systems Personalized
products
9 Marketplaces Real-time Machine learning User experience
10 Natural language
processing
Recommender
system
Product
recommendation
User
preferences
11 Online shopping Sales Purchase intention
12 Recommenda-
tion algorithms
User engagement Predictive analytics
13 Sentiment
analysis
User satisfaction Consumer analytics
14 Social media Personalization Decision support
15 E-commerce
16 Recommender
systems

Page 20 of 29
Chan et al. Discover Artificial Intelligence           (2026) 6:1131
may reduce transparency and interpretability, potentially affecting consumer trust and
acceptance.
3.6.2 Cluster 2: Consumer behavior and personalization outcomes
Cluster 2 focuses on the behavioral outcomes of AI-based recommender systems,
emphasizing how personalization is associated with consumer decision-making, satis -
faction, trust, and purchase intention in e-commerce and marketplace environments.
Several studies adopt established behavioral frameworks to explain these effects. For
example, Beyari and Garamoun [11], using the UTAUT framework, show that AI-driven
recommendations were associated with higher purchase intentions by shaping behav -
ioral intentions in online retailing. Similarly, Santo and Marques, [ 59] show that trust
plays a critical mediating role in personalization effectiveness, where AI-generated rec -
ommendations were associated with lower perceived risk and greater willingness to
transact online. Extending this viewpoint, studies on explainable AI (XAI) suggest that
the inclusion of explanations in recommender systems, particularly attribute-based
reasoning, is associated with higher user trust and lower algorithmic anxiety [ 17, 21].
Additionally, XAI systems that deal with bias detection and fairness improve views of
ethical compliance, which in turn have a beneficial impact on customer satisfaction and
purchase intentions [ 4]. Additionally, the kind of explanation is important: user-based
explanations are better suited to hedonic domains, whereas attribute-based explanations
work better in utilitarian contexts like product recommendations [ 60]. These findings
collectively highlight that the success of recommender systems is not only technical but
also deeply rooted in consumer perceptions and behavioral responses.
From a theoretical perspective, Cluster 2 is strongly grounded in behavioral and mar -
keting theories, particularly the Stimulus–Organism–Response (S-O-R) model and the
Theory of Planned Behavior (TPB). Studies applying the S-O-R framework [ 23, 27] sug-
gest that personalized recommendations may function as external stimuli associated
with consumers’ internal states—such as trust and emotions—which, in turn, may be
related to engagement and purchase behavior. Likewise, TPB-based research [ 1, 46]
suggests that positive attitudes toward AI-driven personalization are associated with
higher purchase intentions. Complementing these findings, research on e-service quality
and relationship marketing [ 47, 50] shows that personalized AI interactions are associ -
ated with satisfaction, loyalty, and long-term consumer relationships. Overall, Cluster
2 underscores that AI-based recommender systems are most effective when they align
technological personalization with established consumer behavior mechanisms, posi -
tioning personalization as a strategic factor associated with sustained consumer engage -
ment and value creation.
Collectively, the findings suggest that trust may emerge through multiple mechanisms,
including transparency, explainability, perceived fairness, and recommendation rel -
evance. Furthermore, trust appears to be a multidimensional construct encompassing
trust in the recommender system, trust in the platform, and trust in the recommenda -
tions themselves. These dimensions are shaped by factors such as perceived accuracy,
privacy protection, organizational credibility, and recommendation usefulness. Conse -
quently, the effectiveness of AI recommender systems should be assessed not only by
predictive accuracy but also by their ability to foster long-term trust, acceptance, and
consumer engagement.

Page 21 of 29
Chan et al. Discover Artificial Intelligence           (2026) 6:1131
3.6.3 Cluster 3: Data mining and predictive consumer analytics
Cluster 3 highlights the application of data mining and predictive analytics to model
and forecast consumer behavior and purchase intentions in e-commerce environments.
Studies in this cluster predominantly employ classification algorithms, decision trees,
random forests, ensemble learning, and deep learning models to analyze large-scale
consumer data and generate predictive insights. For example, Azad et al., [ 8] integrated
the Theory of Planned Behavior (TPB) with multiple machine learning algorithms and
found that behavioral factors—such as attitude, subjective norms, and perceived behav -
ioral control—can be effectively translated into predictive features, with Random Forest
models achieving superior performance.
Beyond structured behavioral data, several studies extend predictive analytics by
incorporating temporal, textual, and multimodal inputs. Salamai et al., [ 58] show the
effectiveness of recurrent neural networks in forecasting e-commerce transaction pat -
terns, revealing hidden temporal dynamics that traditional statistical models fail to cap -
ture. Complementing this, Filahi et al., [ 24] shows that integrating sentiment analysis
with machine learning and deep learning models enables more accurate prediction of
purchase intentions by capturing emotional signals embedded in consumer reviews.
Collectively, these studies position Cluster 3 as a critical analytical bridge between raw
consumer data and actionable recommendation outcomes, emphasizing that robust per-
sonalization and decision support systems depend not only on recommendation algo -
rithms but also on accurate, data-driven prediction of consumer behavior and future
demand.
3.6.4 Cluster 4: Personalization techniques and user experience
Cluster 4 emphasizes personalization mechanisms and user experience (UX) as central
elements in the effectiveness of AI-based recommender systems across e-commerce and
mobile commerce platforms. Studies in this cluster primarily employ content-based fil -
tering, collaborative filtering, deep learning, and hybrid personalization models to align
recommendations with individual user preferences and contextual behaviors. Maher et
al., [41] and Geetha and Renuka [ 25] suggest that deep learning–based personalization,
including session-based and multitask learning models, is associated with higher per -
sonalization accuracy and may support greater engagement and satisfaction during the
shopping process.
Beyond algorithmic personalization, several studies highlight the role of adaptive and
real-time personalization strategies in shaping user experience. Alti and Lakehal, [ 6]
illustrate how generative AI–driven systems enable context-aware and responsive per -
sonalization by dynamically adjusting interfaces and recommendations based on evolv -
ing user behavior. Complementing these findings, Renjith et al., [ 55] and Song and Xing
[61] show that incorporating sentiment-based clustering and multimodal data is associ -
ated with greater recommendation relevance and user engagement. Supporting evidence
from UX-oriented studies indicates that effective personalization reduces cognitive load,
increases perceived usefulness, and strengthens satisfaction and loyalty [ 39]. Overall,
Cluster 4 underscores that the success of AI-driven recommender systems depends not
only on predictive accuracy but also on their ability to deliver adaptive, intuitive, and
user-centered experiences associated with sustained consumer engagement.

Page 22 of 29
Chan et al. Discover Artificial Intelligence           (2026) 6:1131
3.6.5 Cluster 5: E-commerce platforms and contextual environments
Cluster 5 highlights the platform-level context in which AI-based recommender systems
operate, emphasizing the role of e-commerce websites, system architecture, and inter -
face design in shaping consumer interactions and personalization effectiveness. Prior
studies consistently indicate that the performance of recommendation algorithms is
closely associated with platform design features, including user interface layout, content
presentation, and system integration. For instance, Ko et al., [ 33] found that well-struc -
tured platform design is associated with higher user engagement and greater recom -
mender-system effectiveness of recommender systems, while Wang et al.,  65 show that
context-aware product information encounters embedded within platform environ -
ments significantly support consumer decision-making. These findings suggest that rec -
ommender systems should be evaluated not only as standalone algorithms but also as
embedded components of broader platform ecosystems.
From a consumer behavior perspective, research in this cluster emphasizes the medi -
ating role of e-service quality, trust, and usability in translating personalization into
positive consumer outcomes. Fan et al., [23] report that high-quality e-service features—
such as secure systems, responsive interfaces, and personalized recommendations—are
associated with customer engagement and trust. Similarly, Chen et al., [ 16] and Hassan
et al., [29] suggest that platform characteristics, including perceived usefulness and cred-
ibility, may be associated with satisfaction, loyalty, and repurchase intentions, particu -
larly when supported by personalized recommendation features. Complementing these
findings, studies on AI-enhanced architectures and generative personalization highlight
that adaptive platform design is associated with higher user satisfaction and engagement
[6]. Overall, Cluster 5 underscores that effective AI-driven personalization depends on
seamless integration within platform environments, reinforcing the importance of align-
ing recommendation technologies with platform design, service quality, and contextual
user experience.
3.6.6 Cluster 6: System integration and infrastructure
Cluster 6 underscores the system-level integration and infrastructural foundations that
enable AI-based recommender systems to operate at scale within e-commerce environ -
ments. Prior research emphasizes that robust data integration frameworks, modular sys-
tem architectures, and real-time processing capabilities are essential for handling large
and heterogeneous data streams generated by online platforms. Comprehensive surveys
and bibliometric analyses highlight that as recommendation models become more com -
plex, the need for scalable backend architectures and efficient data pipelines becomes
increasingly critical to sustain performance and reliability [ 10, 33]. Studies leveraging
advanced architectures—such as graph-based models and dual-tower frameworks—fur -
ther suggest that effective system design facilitates the integration of multi-dimensional
behavioral data while supporting dynamic, session-aware recommendations [61, 68].
From an operational and governance perspective, this cluster also highlights the
importance of real-time adaptability, privacy preservation, and regulatory compliance
in infrastructure design. The reviewed studies suggest that architectures optimized for
real-time processing may be associated with improved personalization outcomes while
helping address privacy concerns [ 35, 66]. Complementary work on data governance
indicates that compliance-aware backend infrastructures are associated with greater

Page 23 of 29
Chan et al. Discover Artificial Intelligence           (2026) 6:1131
trust and may support lawful data integration without compromising recommendation
responsiveness [ 30]. Additionally, studies on centralized and multi-channel architec -
tures indicate that API-driven integration and unified data normalization are crucial for
delivering consistent personalization across platforms and touchpoints. Overall, Clus -
ter 6 positions system integration and infrastructure as critical enablers that translate
advanced AI models into reliable, real-time, and scalable recommendation services in
digital marketplaces.
A recurring theme across the reviewed studies is the implementation gap between
experimental recommender models and large-scale marketplace deployment. While
many algorithms exhibit strong predictive performance, fewer studies address scalabil -
ity, interoperability, real-time processing, and organizational integration. This highlights
the need for greater attention to implementation-oriented AI solutions that support sus-
tainable deployment in real-world marketplace environments.
In research on artificial intelligence (AI)-based recommender systems, the co-occur -
rence structure indicates that themes related to technology, behavior, and implemen -
tation in this field are conceptually distinct but remain insufficiently integrated in the
current literature, thereby reinforcing the need for an integrative approach offered by
the multi-level framework proposed in the following section.
3.7 Integrative interpretation through the proposed multi-level framework
The six bibliometric clusters found by VOSviewer co-occurrence analysis were linked
to the narrative themes that emerged from the coding of the examined studies at each
level of the proposed framework through a qualitative synthesis. The correspondence
between framework levels and clusters (Clusters 1 and 3 with the AI architecture level,
Clusters 2 and 4 with the consumer cognition level, and Clusters 5 and 6 with the mar -
ketplace implementation level) is an interpretive grouping of thematically related key -
words and findings rather than a statistical test. Rather than establishing statistically
proven correlations between the three levels, the goal of this integrative reading is to
conceptually arrange the examined literature.
The findings of this review provide conceptual support for the proposed multi-level
framework by suggesting that AI-based recommender systems can be understood
through interconnected technological, behavioral, and implementation dimensions. At
the first level, AI architectures—including machine learning, deep learning, collabora -
tive filtering, and hybrid recommender models—provide the technical foundation for
generating personalized recommendations. As identified in Clusters 1 and 3, these tech -
nologies enable predictive analytics, sentiment interpretation, and adaptive recommen -
dation capabilities that shape recommendation quality and relevance.
At the second level, consumer cognition and behavioral mechanisms explain how
users respond to AI-driven personalization. As reflected in Clusters 2 and 4, recommen -
dation effectiveness is influenced not only by algorithmic performance but also by con -
sumer perceptions of relevance, transparency, explainability, satisfaction, and trust. The
integration of S–O–R and TPB perspectives suggests that AI system features may func -
tion as stimuli associated with cognitive and affective responses, which in turn may be
related to purchase intentions, engagement, and acceptance.
At the third level, marketplace implementation outcomes determine whether AI rec -
ommender systems can be successfully deployed in real-world environments. Clusters 5

Page 24 of 29
Chan et al. Discover Artificial Intelligence           (2026) 6:1131
and 6 highlight the importance of platform infrastructure, data integration, scalability,
governance, and organizational readiness. The findings indicate that many studies focus
on algorithmic performance, whereas fewer address the practical challenges associated
with large-scale implementation and system interoperability.
Collectively, the framework helps resolve the fragmentation observed in prior litera -
ture by linking AI architectures, consumer behavioral mechanisms, and marketplace
deployment considerations within a single analytical perspective. Rather than treating
technical performance, consumer outcomes, and implementation challenges as sepa -
rate streams of research, the framework illustrates how these dimensions interact to
shape the overall effectiveness of AI-based recommender systems in digital marketplace
environments.
More importantly, the review suggests that successful AI recommender systems rely
on more than algorithmic performance alone. Their effectiveness depends on the inter -
action between AI capabilities, consumer responses, and implementation readiness.
Even highly accurate recommendation models may fail to create value when users do not
engage with them or when organizations face deployment challenges. This finding high -
lights the importance of adopting a more integrated perspective that connects technol -
ogy, consumer behavior, and marketplace implementation.
3.8 Future research directions
The findings of this review point to several avenues for future research, reorganized here
into theoretical, methodological, ethical, technological, and managerial directions.
Theoretical directions  Stronger theoretical integration between behavioral frame -
works and AI architectures is needed. While many studies adopt performance-oriented
metrics, fewer explicitly embed consumer behavior theories—such as trust formation,
decision-making under uncertainty, and relationship marketing—into the design and
evaluation of recommender systems. Integrating theoretical constructs with algorithmic
features may enhance explanatory depth and theoretical accumulation in the field.
Methodological directions Longitudinal and dynamic research designs remain under -
developed, as existing studies predominantly examine short-term behavioral outcomes
such as engagement and purchase intention; future work should trace long-term conse -
quences, including customer loyalty trajectories, over-personalization effects, algorithm
fatigue, and resistance to automated recommendations. The dominance of quantitative,
data-driven approaches also suggests a need for complementary qualitative and mixed-
method designs that incorporate consumer narratives and experiential data to provide
deeper insight into emotional responses and perceived manipulation.
Ethical directions  As AI-driven personalization becomes increasingly complex and
opaque, future research should examine how explainable AI (XAI) mechanisms, algo -
rithmic bias mitigation, fairness safeguards, and privacy governance jointly shape con -
sumer trust, perceived fairness, system acceptance, and long-term platform legitimacy,
particularly in contexts involving sensitive data and heightened regulatory scrutiny.
Technological directions  Context-aware and adaptive personalization represents an
emerging frontier, with research needed on how real-time recommender systems adjust
to evolving consumer preferences and situational variables while balancing personal -
ization depth against cognitive load and usability. The rapid evolution of digital com -
merce also calls for research on emerging paradigms such as generative AI, multimodal

Page 25 of 29
Chan et al. Discover Artificial Intelligence           (2026) 6:1131
interfaces, and immersive commerce environments, and how these technologies interact
with behavioral dynamics, trust formation, and regulatory constraints.
Managerial directions Greater attention to platform-level and infrastructural consid -
erations is needed from an organizational standpoint: managers and platform operators
must weigh how system architecture, scalability, interoperability, and regulatory com -
pliance affect the practical, large-scale deployment of AI-based recommender systems.
Bridging technological innovation with implementation feasibility and organizational
readiness remains a critical managerial challenge for translating algorithmic advances
into sustainable marketplace value.
3.9 Limitations
This review is subject to several limitations. First, the study relied exclusively on the Sco-
pus database, which may have excluded relevant publications indexed in other databases
such as Web of Science, IEEE Xplore, ACM Digital Library, or PubMed. Although Sco -
pus provides broad multidisciplinary coverage, the use of a single database may limit the
comprehensiveness of the retrieved literature.
Second, the dataset was dominated by conference papers, which account for 96 of
the 135 included publications (approximately 71%). While this composition reflects the
rapidly evolving nature of AI research and provides timely insight into emerging tech -
nological developments, conference publications often place greater emphasis on proto -
type development and technical innovation than on theoretical elaboration, longitudinal
validation, or marketplace-scale implementation. Consequently, the synthesis may over -
represent algorithmic and methodological advances relative to behavioral mechanisms,
consumer trust formation, and sustained deployment outcomes. The shorter publication
and review cycles typical of conference venues may also limit the stability and generaliz -
ability of some reported findings.
Third, the review included only English-language publications, which may have intro -
duced language bias and excluded relevant studies from major e-commerce regions such
as China, South Korea, and Latin America. Although the screening and coding proce -
dures involved two independent reviewers, the thematic synthesis inevitably contains a
degree of interpretive subjectivity.
Finally, bibliometric indicators primarily capture publication characteristics, cita -
tion patterns, and structural relationships within the corpus; they do not directly mea -
sure the methodological quality, risk of bias, or validity of individual studies. No formal
quality-assessment instrument was applied because the review’s primary purpose was
bibliometric mapping and thematic synthesis rather than effect estimation. Accord -
ingly, citation frequency, publication volume, and keyword prominence should not be
interpreted as indicators of research quality or theoretical validity, and the conclusions
represent patterns in the available evidence base rather than a graded assessment of its
methodological strength.
4 Conclusion
An important insight emerging from this review is that the effectiveness of AI-based
recommender systems cannot be explained by algorithmic performance alone. Suc -
cessful personalization depends on the interaction between AI architectures, consumer
cognition, and marketplace implementation capabilities. This finding highlights a shift

Page 26 of 29
Chan et al. Discover Artificial Intelligence           (2026) 6:1131
in the literature from a predominantly technology-centered perspective toward a more
integrated view of AI-driven personalization in digital commerce.
This study synthesizes and systematizes the evolving body of research on AI-based
recommender systems in online marketplace environments. The findings reveal a domi -
nant focus on algorithmic performance enhancement through machine learning, deep
learning, and hybrid architectures, alongside comparatively limited attention to behav -
ioral theory, infrastructural scalability, and ethical design considerations. By mapping
methodological trajectories, thematic clusters, and citation patterns, this review clarifies
the evolution of the field from rule-based personalization to advanced AI-based recom -
mender systems.
The findings suggest that recommender systems are increasingly moving beyond
accuracy-driven optimization toward more human-centered approaches that empha -
size trust, explainability, transparency, and user experience. At the same time, the review
identifies a persistent implementation gap between experimentally validated models and
large-scale marketplace deployment. While many studies report strong predictive per -
formance, fewer address challenges related to scalability, interoperability, governance,
and organizational integration. Furthermore, trust emerges as a multidimensional con -
struct encompassing trust in the recommender system, the platform, and the recom -
mendations provided.
Overall, this study advances the recommender-system literature by proposing a uni -
fied multi-level framework that integrates AI architectures, consumer behavioral mecha-
nisms, and marketplace implementation outcomes. Unlike previous reviews that focused
on these dimensions separately, the framework offers a more holistic understanding of
AI-driven personalization in digital marketplaces.
Theoretically, this review contributes to the recommender-system literature by inte -
grating AI architecture, consumer cognition and behavioral mechanisms, and mar -
ketplace implementation within a unified conceptual framework, thereby bridging
previously fragmented technological and behavioral research streams. Practically, the
findings suggest that managers and platform operators should evaluate AI-based recom-
mender systems not only in terms of predictive accuracy but also in relation to explain -
ability, consumer trust, scalability, interoperability, and governance. These conclusions
should nevertheless be interpreted in light of the review’s reliance on a single database,
the predominance of conference papers in the dataset, and the absence of a formal meth-
odological quality assessment.
Acknowledgements
This research was funded through the EQUITY Program by the Indonesian Endowment Fund for Education (LPDP), on
behalf of the Indonesian Ministry of Higher Education, Science and Technology, and managed by Universitas Padjadjaran
(Contract Nos. 4303/83/DT.03.08/2025 and 3927/UN6.RKT/HK.07.00/2025).
Author contributions
A.C. = Arianis Chan, R.S. = Rani Sukmadewi, C.A.C.W. = Che Aniza Che Wel, A.Y.A = Aurora Yupita Achmada, C.S.B = Cecep
Safa'atul Barkah. A.C. conceptualized the study, designed the research framework, conducted the systematic literature
review and bibliometric analysis, and wrote the main manuscript. R.S. contributed to data collection, literature screening,
and assisted in manuscript preparation. C.A.C.W. provided conceptual guidance, reviewed the analytical framework, and
critically revised the manuscript. A.Y.A. and C.S.B. contributed to manuscript revision and refinement of the analysis. All
authors reviewed and approved the final version of the manuscript.
Funding
Open access funding provided by University of Padjadjaran. This research was funded through the EQUITY Program
by the Indonesian Endowment Fund for Education (LPDP), on behalf of the Indonesian Ministry of Higher Education,
Science and Technology, and managed by Universitas Padjadjaran (Contract Nos. 4303/83/DT.03.08/2025 and 3927/UN6.
RKT/HK.07.00/2025).

Page 27 of 29
Chan et al. Discover Artificial Intelligence           (2026) 6:1131
Data availability
No datasets were generated or analysed during the current study.
Declarations
Ethics approval and consent to participate
Not applicable.
Consent for publication
Not applicable.
Competing interests
The authors declare no competing interests.
Received: 16 March 2026 / Accepted: 31 August 2026
References
1. Abdullah MF, Ibrahim MA, Bahtar AZ, Khan NRM. Conceptualizing the implications of artificial intelligence (AI) tools and
personalization marketing on consumer purchase intention: insights from the Malaysian E-Commerce market. Inform
Manage Bus Rev. 2024;16(3):430–6. https://doi.org/10.22610/imbr.v16i3s(i)a.4145. S(I)a.
2. Ajzen I. The theory of planned behavior. Organ Behav Hum Decis Process. 1991;50(2):179–211.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / 0 7 4
9 - 5 9 7 8 ( 9 1 ) 9 0 0 2 0 - T     .
3. Aksoy NC, Kabadayi ET, Yilmaz C, Alan AK. Personalization in marketing: how do people perceive personalization practices
in the business world? J Electron Commer Res. 2023;24(4):269–97.
4. Almamy ASM, Habib S, Nasser LK, Hamadneh NN Effect of explainable AI features on user satisfaction and purchase inten-
tion in Saudi mobile shopping apps. J Theoretical Appl Electron Commer Res. 2026.  h t t p s : / / d o i . o r g / 1 0 . 3 3 9 0 / j t a e r 2 1 0 4 0 1 2
0     .
5. Alrashidi M, Selamat A, Ibrahim R, Krejcar O. A deep hybrid system for recommendation leveraging social traits. J Cases
Inform Technol. 2025;27(1):1–20. https://doi.org/10.4018/jcit.394258.
6. Alti A, Lakehal A. AI-MDD-UX: revolutionizing e-commerce user experience with generative AI and model-driven develop-
ment. Future Internet. 2025;17(4):180. https://doi.org/10.3390/fi17040180.
7. Aria M, Cuccurullo C. bibliometrix: An R-tool for comprehensive science mapping analysis. J Informetrics. 2017;11(4):959–
75. https://doi.org/10.1016/j.joi.2017.08.007.
8. Azad MS, Khan SS, Hossain R, Rahman R, Momen S. Predictive modeling of consumer purchase behavior on social media:
integrating theory of planned behavior and machine learning for actionable insights. PLoS ONE. 2023;18(12):e0296336.
https://doi.org/10.1371/journal.pone.0296336.
9. Barra A, Saputro D, Widianingsih P . Bibliometric analysis of spline regression model for trend mapping and strategy devel-
opment research using vosviewer. NUCLEUS. 2024;5:74–81. https://doi.org/10.37010/nuc.v5i02.1760.
10. Bawack RE, Wamba SF, Carillo K, Akter S. Artificial Intelligence in e-commerce: a bibliometric study and literature review.
Electron Markets. 2022;32(1):297–338. https://doi.org/10.1007/s12525-022-00537-z.
11. Beyari H, Garamoun H. The effect of artificial intelligence on end-user online purchasing decisions: toward an integrated
conceptual framework. Sustainability. 2022;14(15):9637. https://doi.org/10.3390/su14159637.
12. Beyari H, Hashem T. The role of Artificial Intelligence in personalizing social media marketing strategies for enhanced
customer experience. Behav Sci. 2025;15(5):700. https://doi.org/10.3390/bs15050700.
13. Biswas PK, Liu S A hybrid recommender system for recommending smartphones to prospective customers. Expert Syst
Appl. 2022. https://doi.org/10.1016/j.eswa.2022.118058.
14. Bleier A, Eisenbeiss M. The importance of trust for personalized online advertising. J Retail. 2015;91(3):390–409.  h t t p s : / / d o i .
o r g / 1 0 . 1 0 1 6 / j . j r e t a i . 2 0 1 5 . 0 4 . 0 0 1     .
15. Bülbül N, Çayırağası F, Efendioglu IH. SORCIS Model: Social media marketing dimensions, consumer decision-making
styles, and purchase intention. Mercados y Negocios. 2026;27(57):107–42. https://doi.org/10.32870/myn.vi57.7998.
16. Chen C-W, Chih M, Nguyen DTT How E-Commerce platform features impact post-adoption consumer behaviors: evi-
dence from Vietnam’s online cosmetic sector. Asia Pac J Mark Logistics. 2025. https://doi.org/10.1108/apjml-04-2025-0625.
17. Chen C, Tian AD, Jiang R. When Post hoc explanation knocks: Consumer responses to explainable AI recommendations. J
Interact Mark. 2024;59(3):234–50. https://doi.org/10.1177/10949968231200221.
18. Cheng Y-M. How to animate learners to persist in learning massive open online courses? An application of the stimulus-
organism-response paradigm. Inform Discovery Delivery. 2025;53(1):124–43. https://doi.org/10.1108/IDD-11-2023-0130.
19. Cho E, Rha J-Y. Does consumer autonomy matter? Consumer perceptions of AI-driven recommendations and the mediat-
ing role of consumer autonomy in consumer satisfaction. Int J Hum Comput Interact. 2026.  h t t p s  : / / d o i  . o r g /  1 0 . 1  0 8 0 / 1 0 4 4 7
3 1 8 . 2 0 2 5 . 2 5 8 7 9 2 7     .
20. Davenport T, Guha A, Grewal D, Bressgott T. How artificial intelligence will change the future of marketing. J Acad Mark Sci.
2020;48(1):24–42. https://doi.org/10.1007/s11747-019-00696-0.
21. de Campos LM, Fernández-Luna JM, Huete JF. An explainable content-based approach for recommender systems: a case
study in journal recommendation for paper submission. User Model User-Adapt Interact. 2024;34:1431–65.  h t t p s : / / d o i . o r g
/ 1 0 . 1 0 0 7 / s 1 1 2 5 7 - 0 2 4 - 0 9 4 0 0 - 6     .
22. Donthu N, Kumar S, Mukherjee D, Pandey N, Lim WM. How to conduct a bibliometric analysis: an overview and guidelines.
J Bus Res. 2021;133:285–96. https://doi .org/10.101 6/j.jbusres .2021.04 .070.
23. Fan W, Shao B, Dong X Effect of e-service quality on customer engagement behavior in community E-Commerce. Front
Psychol. 2022. https://doi.org/10.3389/fpsyg.2022.965998.

Page 28 of 29
Chan et al. Discover Artificial Intelligence           (2026) 6:1131
24. Filahi Y, Gül ÖM, Elghirani A, Arıcan E, Parlak İB, Kadry S, Karpouzis K. Enhanced E-commerce decision-making through
sentiment analysis using machine learning-based approaches and IoT. PLoS ONE. 2025;20(6):e0326744.  h t t p s : / / d o i . o r g / 1 0 .
1 3 7 1 / j o u r n a l . p o n e . 0 3 2 6 7 4 4     .
25. Geetha MP , Renuka DK. Deep learning architecture towards consumer buying behaviour prediction using multitask learn-
ing paradigm. J Intell Fuzzy Syst Appl Eng Technol. 2023;46(1):1341–57. https://doi.org/10.3233/jifs-231116.
26. Guan N. Machine learning algorithms in the development of recommender systems. Appl Comput Eng. 2024;51(1):119–
28. https://doi .org/10.542 54/2755-272 1/51/202 41189.
27. Guthrie C, Wamba SF, Arnaud JB. Online consumer resilience during a pandemic: an exploratory study of e-commerce
behavior before, during and after a COVID-19 lockdown. J Retailing Consumer Serv. 2021;61:102570.  h t t p s  : / / d o i  . o r g /  1 0 . 1  0
1 6 / j . j r e t c o n s e r . 2 0 2 1 . 1 0 2 5 7 0     .
28. Halil Efendioğlu İ. Trends in artificial intelligence marketing: a bibliometric analysis. In: International Journal of Economic
and Administrative Academic Research (Vol. 3, Number 2). 2023 https://orcid.org/0000-0002-4968-375X
29. Hassan N, Abdelraouf M, El-Shihy D. The moderating role of personalized recommendations in the trust–satisfaction–loy-
alty relationship: an empirical study of AI-driven E-commerce. Future Bus J. 2025;11(66):1–15.  h t t p s : / / d o i . o r g / 1 0 . 1 1 8 6 / s 4 3 0
9 3 - 0 2 5 - 0 0 4 7 6 - z     .
30. Huang SJDP , Liu Z. The impact of personalized recommendation systems on consumer purchase decisions under data law
frameworks. J Organizational End User Comput. 2025;37(1):1–28. https://doi.org/10.4018/joeuc.385731.
31. Jain G, Mahara T, Sharma SC, Agarwal S, Kim H. TD-DNN: a time decay-based deep neural network for recommendation
system. Appl Sci. 2022;12(13):6398. https://doi.org/10.3390/app12136398.
32. Kim M, Lee S-M. ChatGPT as a digital dining companion: examining AI perceptions and consumer loyalty in restaurant
recommendations. Int J Hum Comput Interact. 2026. https://doi .org/10.108 0/10447318. 2026.263 6249.
33. Ko H, Lee S, Park Y, Choi A. A survey of recommendation systems: recommendation models, techniques, and application
fields. Electronics. 2022;11(1):141. https://doi.org/10.3390/electronics11010141.
34. Lemon KN, Verhoef PC. Understanding customer experience throughout the customer journey. J Mark. 2016;80(6):69–96.
https://doi.org/10.1509/jm.15.0420.
35. Li R, Shu Y, Cao Y, Luo Y, Zuo Q, Wu X, Yu J, Zhang W. Federated cross-view e-commerce recommendation based on feature
rescaling. Sci Rep. 2024;14(1):29926, 1–19. https://doi.org/10.1038/s41598-024-81278-1.
36. Li T, Wu Y, Liu Y, Li J. Deep learning-based analysis of E-commerce enterprises. J Organizational End User Comput.
2025;37(1):1–36. https://doi.org/10.4018/joeuc.379722.
37. Lin X, Xu Y, Hwang C. Beyond static images: how interactivity, vividness and realism shape consumer responses toward 3D
fashion lookbooks. J Res Interact Mark. 2026;20(4):583–608. https://doi.org/10.1108/JRIM-03-2025-0130.
38. Listya K, Dwi Jati F, Asrin Jazuli M. Bibliometric analysis with VOS Viewer of journal trends in risk management, firm perfor-
mance, and firm value. Jurnal Mantik. 2024;8(1):477–87. https://doi.org/10.35335/mantik.v8i1.5167.
39. Liu Q, Tang H, Wu L, Chao Z. Deep learning-driven e-commerce marketing communication for recommending shopping
system and optimizing user experience. J Organizational End User Comput. 2024;36(1):1–28.  h t t p s : / / d o i . o r g / 1 0 . 4 0 1 8 / j o e u
c . 3 4 3 2 5 8     .
40. Loukili M, Messaoudi F, Ghazi E, M. Machine learning based recommender system for E-commerce. IAES Int J Artif Intell.
2023;12(4):1803–11. https://doi.org/10.11591/ijai.v12.i4.pp1803-  1811.
41. Maher M, Ngoy PM, Rebriks A, Ozcinar C, Cuevas J, Sanagavarapu R, Anbarjafari G. Comprehensive empirical evaluation of
deep learning approaches for session-based recommendation in E-commerce. Entropy. 2022;24(11):1575.  h t t p s : / / d o i . o r g /
1 0 . 3 3 9 0 / e 2 4 1 1 1 5 7 5     .
42. Manthiou A, Ayadi K, Lee S, Chiang L, Tang L. Exploring the roles of self-concept and future memory at consumer events:
the application of an extended Mehrabian–Russell model. J Travel Tourism Mark. 2017;34(4):531–43.  h t t p s  : / / d o i  . o r g /  1 0 . 1  0 8
0 / 1 0 5 4 8 4 0 8 . 2 0 1 6 . 1 2 0 8 7 8 6     .
43. Masih J, Mathur M, Bhagwat A, Mishra S, Rokade K. An evaluation of core factors of predictive analytics in influencing
purchase decision of the consumers in E-business. In: Studies in Computational Intelligence (Vol. 1113). 2023;  h t t p s : / / d o i . o
r g / 1 0 . 1 0 0 7 / 9 7 8 - 3 - 0 3 1 - 4 3 3 0 0 - 9 _ 5
44. Messaoudi F, Loukili M. E-commerce personalized recommendations: a deep neural collaborative filtering approach. Oper
Res Forum. 2024;5(1):5. https://doi.org/10.1007/s43069-023-00286-5.
45. Mican D, Sitar-Tăut D. The effect of perceived usefulness of recommender systems and information sources on purchase
intention. Kybernetes. 2024;53(7):2301–21. https://doi.org/10.1108/K-08-2022-1145.
46. Mofokeng TE The impact of online shopping attributes on customer satisfaction and loyalty: moderating effects of
E-commerce experience. Cogent Bus Manage. 2021. https://doi .org/10.108 0/23311975. 2021.196 8206.
47. Muharam H, Chaniago H, Endraria E, Harun AB. E-service quality, customer trust and satisfaction: market place consumer
loyalty analysis. Jurnal Minds: Manajemen Ide dan Inspirasi. 2021;8(2):237–54. https://doi.org/10.24252/minds.v8i2.23224.
48. Neetika, Abrol V, Agarwal N, Swain AK, Vinchurkar G. Personalization in Digital Marketing: Enhancing Consumer Engage-
ment Using AI. In Communications in Computer and Information Science: 2730 CCIS. 2026;  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / 9 7 8 - 3
- 0 3 2 - 1 2 2 3 2 - 2 _ 1 5
49. Nguyen TCL, Nguyen TTP , Voak A. An S–O–R model perspective on e-commerce: Personalization, hedonic motivation, and
customer experience driving e-satisfaction and repurchase intention in a developing country. J Global Scholars Mark Sci
Bridging Asia World. 2026;36(1):109–40. https:   //d oi. or g/10 .1080/21 6391 59.20 25.2577721.
50. Panda D, Raut SK, Rana S, Shamsudin MN. Leveraging gamification to enhance persuasive behaviour and streamline
online product returns: an approach grounded in multiple case studies. J Bus Industrial Mark. 2024;39(12):2684–98.
https://doi.org/10.1108/jbim-01-2024-0007.
51. Pavlou PA, Fygenson M. Understanding and predicting electronic commerce adoption: An extension of the theory of
planned behavior. MIS Q. 2006;30(1):115–43. https://doi.org/10.2307/25148720.
52. Pons S, Huertas-Garcia R, Lengler J, de Nascimento M, D. L. Psychol Mark. 2025;42(7):1946–57.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 2 / m a r .
2 2 2 1 1     . Natural language processing algorithms to improve digital marketing data quality and its ethical implications.
53. Ponsignon F, Jaud DA, Durrieu F, Lunardo R. The ability of experience design characteristics to elicit epistemic value,
hedonic value, and visitor satisfaction in a wine museum. Int J Contemp Hospitality Manage. 2024;36(8):2582–600.  h t t p s : / /
d o i . o r g / 1 0 . 1 1 0 8 / I J C H M - 0 7 - 2 0 2 3 - 1 0 8 1     .

Page 29 of 29
Chan et al. Discover Artificial Intelligence           (2026) 6:1131
54. Prada Núñez R, Peñaloza Tarazona ME, Rodríguez Moreno J. Trends and challenges of integrating the STEAM approach in
education: a scopus literature review. Data Metadata. 2024;3(424):1–18. https://doi.org/10.56294/dm2024.424.
55. Renjith S, Sreekumar A, Jathavedan M SemRec—an efficient ensemble recommender with sentiment based clustering for
social media text corpus. Concurrency Comput Pract Experience. 2021. https://doi.org/10.1002/cpe.6359.
56. Rethlefsen ML, Kirtley S, Waffenschmidt S, Ayala AP , Moher D, Page MJ, Koffel JB. PRISMA-S: An extension to the PRISMA
statement for reporting literature searches in systematic reviews. Syst Reviews. 2021;10(1):39.  h t t p s : / / d o i . o r g / 1 0 . 1 1 8 6 / s 1 3 6
4 3 - 0 2 0 - 0 1 5 4 2 - z     .
57. Ricci F, Rokach L, Shapira B, Kantor PB, editors. Recommender systems handbook. Springer; 2011.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 /
9 7 8 - 0 - 3 8 7 - 8 5 8 2 0 - 3     .
58. Salamai AA, Ageeli AA, El-kenawy EM. Forecasting E-commerce adoption based on bidirectional recurrent neural net-
works. Comput Mater Continua. 2022;70(3):5091–106. https://doi.org/10.32604/cmc.2022.021268.
59. Santo PE, Marques A. Determinants of the online purchase intention: hedonic motivations, prices, information and trust.
Baltic J Manage. 2022;17(1):56–71. https://doi.org/10.1108/bjm-04-2021-0140.
60. Shin D The effects of explainability and causability on perception, trust, and acceptance: Implications for explainable AI.
Int J Hum Comput Stud. 2021;. https://doi.org/10.1016/j.ijhcs.2020.102551.
61. Song W, Xing X. Dual-tower counterfactual session-aware recommender system. Entropy. 2024;26(6):516.  h t t p s : / / d o i . o r g / 1
0 . 3 3 9 0 / e 2 6 0 6 0 5 1 6     .
62. Talebi A, Mukherjee S, Gera N, Kaur K, Das G. Unveiling coping mechanisms in marketplace discrimination: the allure of
artificial intelligence recommendations. J Prod Innov Manage. 2026;43(1):215–47. https://doi.org/10.1111/jpim.12774.
63. Vindytia M, Balqiah TE. (2024). AI marketing impact on consumer behavior: an SOR model analysis of online food delivery
services. In JDM (Jurnal Dinamika Manajemen) (Vol. 15, Number 2). http://jdm.unnes.ac.id
64. Wang B, Zheng W, Wang R, Lu S, Yin L, Wang L, Yin Z, Chen X. Stacked noise reduction auto encoder–OCEAN: a novel
personalized recommendation model enhanced. Systems. 2024;12(6):188. https://doi.org/10.3390/systems12060188.
65. Wang L, Zhang G, Jiang D. Encountering product information: how flashes of insight improve your decisions on e-com-
merce platforms. J Theoretical Appl Electron Commer Res. 2024;19(3):2180–97. https://doi.org/10.3390/jtaer19030106.
66. Wei Z, Liang Y, Zhang C. Optimization strategies in consumer choice behavior for personalized recommendation systems
based on deep reinforcement learning. J Organizational End User Comput. 2025;37(1):1–35.  h t t p s : / / d o i . o r g / 1 0 . 4 0 1 8 / j o e u c .
3 6 8 0 0 9     .
67. Wu M-H How influencer attractiveness and expertise shape consumer responses through parasocial interaction and trust.
Computers. 2026. https://doi.org/10.3390/computers15040250.
68. Xia L, Huang C, Xu Y, Dai P , Bo L. Multi-behavior graph neural networks for recommender system. IEEE Trans Neural Net-
works Learn Syst. 2024;35(4):5473–87. https://doi.org/10.1109/tnnls.2022.3204775.
69. Yu Y, Chen X, Zhang L, Gao R, Gao H. Neural graph for personalized tag recommendation. IEEE Intell Syst. 2022;37(1):51–9.
https://doi.org/10.1109/mis.2020.3040046.
70. Zhang Q, Lu J, Jin Y. Artificial intelligence in recommender systems. Complex Intell Syst. 2021;7(1):439–57.  h t t p s : / / d o i . o r g / 1
0 . 1 0 0 7 / s 4 0 7 4 7 - 0 2 0 - 0 0 2 1 2 - w     .
71. Zhou T, Ma X. Examining generative AI user continuance intention based on the SOR model. Aslib J Inform Manage.
2026;78(4):969–87. https://doi.org/10.1108/AJIM-08-2024-0620.
Publisher’s note
Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.
