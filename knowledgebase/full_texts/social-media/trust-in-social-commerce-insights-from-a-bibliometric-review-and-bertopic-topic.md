---
title: 'Trust in Social Commerce: Insights from a Bibliometric Review and BERTopic Topic Modelling Analysis'
url: https://doi.org/10.32479/irmm.24322
category: social-media
subcategory: framework
date: 2026-09
venue: International Review of Management and Marketing
authors:
- Yang Shao
- Nadzirah Rosli
- Sharizal Hashim
source: openalex-oa
pdf_url: https://econjournals.com/index.php/irmm/article/download/24322/10360
pages: 14
chars: 74938
fetched_at: '2026-11-08T18:53:18+00:00'
kb_version: 1
---

# Trust in Social Commerce: Insights from a Bibliometric Review and BERTopic Topic Modelling Analysis

International Review of Management and
Marketing
ISSN: 2146-4405
available at http: www.econjournals.com
International Review of Management and Marketing, 2026, 16(6), 559-572.
International Review of Management and Marketing | V ol 16 • Issue 6 • 2026
559
Trust in Social Commerce: Insights from a Bibliometric Review
and BERTopic Topic Modelling Analysis
Yang Shao1, Nadzirah Rosli2*, Sharizal Hashim2
1Graduate School of Business, Universiti Kebangsaan Malaysia, Bangi, Selangor, Malaysia, 2Faculty of Economics and
Management, Universiti Kebangsaan Malaysia, Bangi, Selangor, Malaysia. *Email: nadzirah.rosli@ukm.edu.my
Received: 05 April 2026 Accepted: 28 July 2026 DOI: https://doi.org/10.32479/irmm.24322
ABSTRACT
This study integrates bibliometric analysis and BERTopic topic modelling to systematically examine the development and thematic structure of trust
research in social commerce. Following the SPAR-4-SLR protocol, this study analyses 1,055 publications retrieved from Web of Science and Scopus
from 2005 to May 2026. Bibliometric analysis examines the publication trends, influential contributors, key journals, and institutional concentrations
of trust research in social commerce. BERTopic analysis identifies 13 distinct research themes and traces their evolution over two decades. Building on
these findings, an integrative framework is proposed that positions three types of trust as the central construct, shaped by five antecedent dimensions
(technology, business, social, information, and consumer), leading to three behavioural outcomes (social commerce adoption, impulsive buying
behaviour, and technology acceptance), moderated by cultural differences, and contextualized within live streaming commerce and COVID-19. The
study offers a structured synthesis of trust research in social commerce and identifies directions for future research.
Keywords: Trust, Social Commerce, Bibliometric Analysis, BERTopic Topic Modelling
JEL Classifications: M31, L81
1. INTRODUCTION
Social commerce has emerged as one of the fastest-growing
forms of digital commerce, transforming traditional online
transactions into socially embedded and interactive purchasing
experiences (Leong et al., 2024). Rather than serving merely as
a transaction channel, social commerce provides an environment
where consumers can discover products, exchange opinions,
seek recommendations, and engage with other users throughout
the purchasing process (Abbas et al., 2023; Attar et al., 2022). In
contrast to traditional e-commerce, which primarily emphasizes
transactional efficiency, social commerce relies heavily on user-
generated content, online communities, social interactions, and
peer influence to support consumer decision-making (Bugshan
and Attar, 2020; Sheikh et al., 2019). Reflecting its growing
significance, the global social commerce market was valued
at approximately USD 1.63 trillion in 2025 and is projected
to reach USD 7.55 trillion by 2031, representing a compound
annual growth rate of 29.12% (Mordor Intelligence, 2026). As
commercial activities become increasingly intertwined with social
interactions in digital environments, understanding the factors
that shape consumer behavior in social commerce has become a
critical research priority.
Among the various factors influencing consumer behavior in
social commerce, trust has consistently been recognized as one
of the most critical determinants of consumer participation and
purchasing decisions. The socially mediated nature of social
commerce introduces substantial uncertainty regarding product
quality, information credibility, seller reliability, transaction
security, and privacy protection (Sembada and Koay, 2021; Tseng
et al., 2023). Consequently, trust plays a pivotal role in reducing
perceived uncertainty and facilitating consumers’ willingness to
engage in online transactions (Gefen et al., 2003; McKnight et al.,
This Journal is licensed under a Creative Commons Attribution 4.0 International License

Shao, et al.: Trust in Social Commerce: Insights from a Bibliometric Review and BERTopic Topic Modelling Analysis
International Review of Management and Marketing | V ol 16 • Issue 6 • 2026
560
2002). Despite the continuous evolution of social commerce, trust
remains one of the most critical and enduring issues in the field
(Ma’ady and Wardhani, 2022; Shao et al., 2026). The literature
about trust in social commerce has expanded considerably
over time, encompassing a broad range of contexts, research
perspectives, and application settings. While this growth has
enriched scholarly understanding of trust in social commerce, it
has also produced a fragmented knowledge base, making it difficult
to form a comprehensive understanding of the field.
Given the expanding and increasingly fragmented body of trust
research in social commerce, bibliometric analysis provides a
useful approach for systematically understanding the field. As
a quantitative literature review method, bibliometric analysis
employs objective and reproducible procedures to systematically
examine large volumes of scientific publications, enabling the
identification of influential contributors, publication trends, and
the evolutionary trajectory of a research field (Donthu et al., 2021).
Such insights provide a comprehensive understanding of the field
and help identify promising avenues for future research.
However, bibliometric analysis has certain limitations, particularly
in theme identification. Shao et al. (2026) highlighted two major
challenges. First, thematic interpretation based on bibliometric
techniques often relies on keyword-based analyses, which may
not fully use the rich information in the abstract (Yu and Xiang,
2023). Second, although researchers supplement bibliometric
findings with manual reviews to improve theme identification,
such procedures can be labor-intensive. To address these
limitations, recent studies have increasingly adopted topic
modeling techniques to automatically identify latent themes from
large document collections. Among topic modelling techniques,
BERTopic has attracted growing attention due to its ability to
leverage transformer-based language models to capture contextual
meanings and semantic relationships (Grootendorst, 2022). By
automatically extracting latent themes from large collections of
textual data, BERTopic reduces the reliance on labor-intensive
manual theme identification while providing more nuanced,
semantically coherent, and scalable topic discovery than traditional
keyword-based approaches (Egger and Yu, 2022).
By integrating bibliometric analysis with BERTopic-based topic
modelling, this study examines both the development and thematic
structure of trust research in social commerce. The bibliometric
analysis facilitates the identification of influential contributors,
publication trends, and key journals and institutions, while BERTopic
topic modelling enables the discovery of latent research themes
embedded within the literature. Building upon these advantages,
the present study aims to systematically examine the development
of trust research in social commerce and develop a comprehensive
understanding of its thematic evolution and future research directions.
Accordingly, the following research questions are proposed:
RQ1:  What are the publication trends, influential contributors,
publications, journals and institutions of trust research in
social commerce?
RQ2: What are the major research themes in trust research?
RQ3:  What integrative framework and future research frontiers
can be identified for trust research in social commerce?
2. LITERATURE REVIEW
2.1. Social Commerce
Social commerce emerged as a distinct form of digital commerce
following its introduction by Yahoo in 2005 (Cui et al., 2018;
Esmaeili and Hashemi, 2019), and has since grown into one of
the most active and rapidly evolving areas in both industry and
academic research. Three defining characteristics distinguish social
commerce from traditional e-commerce. First, social commerce is
technology-driven, leveraging Web 2.0 technologies and mobile
platforms to enable real-time, interactive commercial activities
(Huang and Benyoucef, 2013; Shao et al., 2026). Second, social
interaction are central to the consumer experience, as purchasing
decisions are shaped not only by seller-provided information but
increasingly by user-generated content, peer recommendations,
influencer endorsements, and community discussions (Attar et al.,
2022; Sheikh et al., 2019). Within social commerce environments,
consumers can build social relationships, communicate, review
others’ opinions, rate and recommend products, and share
experiences (Hajli, 2013; W. Zhao et al., 2023). Third, social
commerce offers a more convenient and seamless shopping
experience, enabling consumers to complete the entire purchase
process within a single platform through purchase button
(shopping cart or checkout button), without redirecting to separate
e-commerce sites or brand websites (Han, 2023).
2.2. Trust in Social Commerce
Trust is defined as a psychological state comprising the intention
to accept vulnerability based on positive expectations of the
intentions or behaviour of another (Mayer et al., 1995; Rousseau
et al., 1998), and has been recognised as a mechanism that reduces
decision-making complexity by allowing individuals to act
without needing to fully evaluate all available information (Gvili
and Levy, 2023). In social commerce contexts, trust takes on
particular significance due to the heightened levels of uncertainty
consumers face. Many social commerce platforms originated
as social media platforms rather than dedicated commerce
infrastructure, resulting in comparatively inadequate privacy
protection, where personal data including identification details,
addresses, and banking information may be exposed to misuse or
leakage (Sembada and Koay, 2021; Wang et al., 2020). Beyond
privacy risks, consumers also contend with other concerns, such
as counterfeit and low-quality products (Wongkitrungrueng and
Assarut, 2020), and misleading information circulated through
user-generated content (Tseng et al., 2023; Zhao et al., 2020).
These compounding uncertainties amplify the role of trust as a
prerequisite for consumer participation, as individuals who choose
to rely on others in risky environments necessarily place greater
weight on trust as a guide to action (Gefen, 2000). Empirical
evidence confirms that when consumer trust toward social
commerce diminishes, consumers may postpone or refrain from
using and purchasing (Laradi et al., 2024; Tseng, 2023), directly
limiting the growth potential of social commerce. Understanding
trust in social commerce environments therefore represents a
critical research priority for both scholars and practitioners.
Despite growing scholarly attention, the field lacks an up-to-date
synthesis of its research landscape, particularly with respect

Shao, et al.: Trust in Social Commerce: Insights from a Bibliometric Review and BERTopic Topic Modelling Analysis
International Review of Management and Marketing | V ol 16 • Issue 6 • 2026
561
to thematic structure. Ma’ady and Wardhani (2022) conducted
a systematic literature review on trust mechanisms in social
commerce based on 31 articles, and large-scale bibliometric
reviews of the field remain absent. Ahmad et al. (2025) reviewed
the relationships between consumer trust and social commerce
engagement. By integrating bibliometric analysis with BERTopic
topic modelling, this study provides an up-to-date overview of
trust research in social commerce across 1,055 publications,
offering a comprehensive foundation for researchers seeking to
understand the field.
3. METHODOLOGY
3.1. Research Protocol
The Scientific Procedures and Rationales for Systematic Literature
Reviews (SPAR-4-SLR) protocol was adopted to guide the
review process, which comprises three main stages: Assembling,
arranging, and assessing. SPAR-4-SLR is widely applicable to
different types of systematic reviews, including framework-based,
bibliometric, and conceptual reviews, and addresses the limitation
of the commonly used PRISMA protocol, which has been criticized
for insufficient justification of review decisions (Paul et al., 2021).
The review protocol is illustrated in Figure 1.
The first stage is assembling. Literature was retrieved from two
databases, Web of Science (WoS) and Scopus, both of which
are widely utilized in business and management research and
acknowledged for providing extensive, high-quality academic
coverage. The following search string was constructed using
Boolean operators: TITLE-ABS-KEY (“social commerce” OR
“social shopping” OR “s-commerce” OR “social e-commerce” OR
“s commerce” OR “social media commerce” OR “social electronic
commerce” OR “mobile social commerce”) AND (trust). A total
of 1,466 records were retrieved from the two databases.
The second stage is arranging. All retrieved records were coded
for author, title, publication year, journal, volume, issue, and DOI.
Retrieved records from both databases were first merged and
deduplicated based on digital object identifiers and article titles,
removing 381 duplicate entries. Records published prior to 2005
were subsequently excluded, given that 2005 is broadly recognized
as the year the term social commerce emerged (Cui et al., 2018;
Shao et al., 2026). Non-English publications were then removed,
followed by the exclusion of records lacking author information,
abstracts, or keywords to ensure data completeness for subsequent
analyses. One retracted publication was removed. Following
these sequential screening steps, 1,055 studies were retained for
analysis. Then the last step is assessing. This stage encompassed
bibliometric analysis and topic modelling. Findings are reported
through narrative text, tables, and figures.
3.2. Bibliometric Analysis
Bibliometric analysis is a quantitative literature review method that
enables researchers to systematically examine the development,
structure, and evolution of a research field through bibliographic
data (Aria and Cuccurullo, 2017; Donthu et al., 2021). Owing
to its ability to handle large volumes of scientific publications,
bibliometric analysis has become increasingly popular in business
and management research for identifying influential contributions,
uncovering emerging trends, and generating the comprehensive
understanding of a field (Donthu et al., 2021). In this study,
bibliometric analysis was employed to examine publication
trends, influential authors, publications, journals, and institutions.
Biblioshiny, the web-based interface of the Bibliometrix package
(Aria and Cuccurullo, 2017), was employed to conduct bibliometric
analysis of the retrieved publications. As one of the most widely
used bibliometric tools in business and management research
(Donthu et al., 2021; Gutiérrez-Salcedo et al., 2018), the platform
supports the analysis and visualization of publication trends,
citation performance, influential journals, authors, institutions,
and countries, thereby providing a comprehensive overview of
development of a research field.
3.3. Topic Modelling Analysis
To identify research themes within the collected literature, this
study employed BERTopic, a transformer-based topic modelling
technique developed by Grootendorst (2022). The analytical
process proceeded through four sequential steps. First, the
abstracts of all retrieved documents were pre-processed to
remove noise, including non-English characters, stopwords,
and excessively rare or common terms. Second, document
embeddings were generated using the all-MiniLM-L6-v2
sentence transformer model, which encodes each abstract into
a high-dimensional vector that captures its semantic content.
Third, the dimensionality of these embeddings was reduced
using Uniform Manifold Approximation and Projection (UMAP)
to facilitate clustering. Fourth, the reduced embeddings were
grouped into clusters using Hierarchical Density-Based Spatial
Clustering of Applications with Noise (HDBSCAN), which does
not require a pre-specified number of clusters and is capable of
Figure 1: Review protocol (extraction date: May 05, 2026)

Shao, et al.: Trust in Social Commerce: Insights from a Bibliometric Review and BERTopic Topic Modelling Analysis
International Review of Management and Marketing | V ol 16 • Issue 6 • 2026
562
handling irregular cluster shapes. Topic representations were then
derived from each cluster using a class-based TF-IDF procedure,
which identifies the keywords most distinctive to each topic
relative to the overall corpus (Grootendorst, 2022). Following
topic extraction, temporal analysis was conducted to trace the
evolution of each theme across the study period, providing
insight into how scholarly attention to social commerce trust
has shifted over time.
4. RESULTS
Figure 2  illustrates the annual scientific production on social
commerce from 2008 to 2026. Publication output remained
minimal prior to 2013, reflecting the early and nascent stage of
social commerce as a research domain. A  steady upward trend
emerged from 2013 onwards, with notable acceleration after 2017,
when annual output surpassed 90 articles. Growth momentarily
plateaued between 2019 and 2021, likely reflecting disruptions to
research activities and publication timelines during the COVID-19
pandemic. Output resumed its upward trajectory from 2022,
reaching its peak in approximately 2025 with nearly 150 articles
published. Notably, the figure for 2026 represents only the first
half of the year at the time of data retrieval, and the current
output already approaches 80 articles, suggesting that full-year
production is likely to maintain or exceed the levels observed in
preceding years. Overall, the trajectory indicates sustained and
growing academic attention toward social commerce research
over the past decade.
Table 1 presents the ten most influential documents in the social
commerce literature. Local citations refer to citations received
from within the reviewed corpus, while global citations reflect total
citations across all academic literature. The LC/GC ratios further
reveal that several of these foundational works, particularly Kim
and Park (2013), Ng (2013), and Yahia et al. (2018), exhibit ratios
exceeding 40%, indicating that their influence is concentrated
primarily within the social commerce research community rather
than diffused across broader disciplines. In contrast, works such as
Liang and Turban (2011) and Lu et al. (2016) show comparatively
lower ratios, suggesting that their theoretical contributions have
resonated beyond the field itself.
These works have collectively shaped the theoretical trajectory of
the field by establishing trust as the central mediating mechanism
in social commerce, and by identifying the antecedents and
outcome constructs. Social support and social presence have been
consistently identified as significant antecedents of consumer
trust across these highly cited studies (Liang and Turban, 2011;
Lu et al., 2016), while trust has been shown to exert substantial
influence on purchase intention and word-of-mouth intention
(Kim and Park, 2013; Ng, 2013). Hajli (2015) made a particularly
influential contribution by introducing social commerce constructs
(ratings and reviews, forums and communities, referrals and
recommendations), and tested the impact on trust building. Yahia
et al. (2018) extended this line of inquiry to vendor characteristics,
demonstrating that reputation and price advantage shape consumer
trust in social media commerce contexts. Huang and Benyoucef
(2013) complemented these empirical works by offering a
comprehensive conceptual review and design framework for social
commerce platforms. The most locally cited works in this field
converge on a common theoretical position that trust functions
as a central mediating mechanism connecting its antecedents
to behavioural outcomes such as purchase intention and word-
of-mouth. This shared focus on trust as a bridge between what
precedes and what follows it has exerted a lasting influence on
the field, shaping the questions subsequent scholars have asked
and the theoretical frameworks they have adopted.
Table 2  presents the most productive authors in the social
commerce literature based on the current dataset. Hajli N emerges
as the most prolific and influential contributor, having published
15 articles with a total citation count of 2,578 and an h-index of
21, reflecting sustained and wide-reaching scholarly impact on the
field since 2014. Notably, three of Hajli’s works appear among
the ten most locally cited documents, underscoring his central
role in shaping the theoretical development of social commerce
research. The remaining authors recorded between six and eight
publications within the dataset, with Wang YC (TC = 1,151) and
Liébana-Cabanillas F (TC = 637) standing out in terms of citation
impact among this group. Most of these productive authors began
publishing in social commerce between 2014 and 2020, reflecting
the relatively recent consolidation of the field as a distinct research
domain.
Figure 2: Annual scientific production

Shao, et al.: Trust in Social Commerce: Insights from a Bibliometric Review and BERTopic Topic Modelling Analysis
International Review of Management and Marketing | V ol 16 • Issue 6 • 2026
563
Figures 3 and 4 present the most relevant publication sources and
the most locally cited sources in the social commerce literature
respectively. In terms of publication output, the Journal of
Retailing and Consumer Services leads with 36 articles, followed
by Sustainability with 28 articles and Electronic Commerce
Research and Applications with 23 articles. The International
Journal of Information Management appears prominently in both
figures, ranking among the top publication venues and recording
the highest local citation count of 2,555, establishing it as the most
influential journal in the field. The presence of MIS Quarterly
among the most locally cited sources, despite its absence from
the publication ranking, indicates that foundational information
systems theories drawn from this outlet have significantly informed
social commerce research without the journal itself serving as a
primary outlet for such studies. The presence of both commerce-
oriented journals such as Journal of Business Research and Journal
of Retailing and Consumer Services alongside information systems
outlets such as Computers in Human Behavior and Information and
Management further underscores the interdisciplinary theoretical
foundations upon which social commerce research is built.
Figure 5  illustrates the most relevant institutional affiliations
contributing to social commerce research. Bina Nusantara
University leads with 30 articles, followed by Swansea University
and Universiti Sains Malaysia, each contributing 26 articles.
The distribution reveals a pronounced concentration of research
output from Southeast Asian institutions, with five of the ten most
productive affiliations located in Malaysia and Indonesia, reflecting
the region’s growing scholarly engagement with social commerce.
The presence of Swansea University is notably associated with
the prolific contributions of Hajli N, identified earlier as the most
influential author in the dataset. Chinese institutions, represented
by Zhejiang Gongshang University and Hangzhou Dianzi
University, alongside the Indian Institute of Management, further
indicate that social commerce research is largely driven by scholars
from Asia, consistent with the rapid growth of social commerce
adoption across the region.
Figure 6  presents the corresponding authors’ countries
contributing to social commerce research. China dominates
overwhelmingly with approximately 340 articles, more than
four times the output of the second-ranked country, Malaysia,
which contributed around 80 articles. The United States,
Indonesia, India, Korea, and the United Kingdom follow,
each contributing between 40 and 65 articles. The distribution
confirms that social commerce research is predominantly driven
by scholars based in Asia, with China, Malaysia, Indonesia,
India, and Korea collectively accounting for the majority of
global output, reflecting the region’s position as both a major
market and a primary research hub for social commerce. In
terms of international collaboration, most countries show a
higher proportion of single-country publications relative to
multi-country publications, with China in particular exhibiting
a notably large SCP share, suggesting that Chinese scholars
tend to publish predominantly within domestic research teams.
The presence of Middle Eastern countries such as Saudi Arabia
and Jordan, alongside European contributors including the
United Kingdom, Spain, and Germany, indicates that social
commerce research has achieved a degree of global reach, though
the field remains heavily concentrated in Asia.
Table 1: Most influential cited documents
Author Title Local citations Global citations LC/GC ratio (%)
Kim and Park
(2013)
Effects of Various Characteristics of Social Commerce
on Consumers’ Trust and Trust Performance
300 678 44.25
Liang et al. (2011) What Drives Social Commerce: The Role of Social
Support and Relationship Quality
241 877 27.48
Lu et al. (2016) Social Presence, Trust, and Social Commerce Purchase
Intention: An Empirical Research
211 736 28.67
Huang and
Benyoucef (2013)
From E-Commerce to Social Commerce: A Close Look
at Design Features
204 615 33.17
Hajli (2015) Social Commerce Constructs and Consumer’s Intention
to Buy
203 500 40.60
Hajli et al. (2017) A Social Commerce Investigation of the Role of Trust in
a Social Networking Site on Purchase Intentions
178 446 39.91
Chen and Shen
(2015)
Consumers’ Decisions in Social Commerce Context: An
Empirical Investigation
159 374 42.51
Ng (2013) Intention to Purchase on Social Commerce Websites
Across Cultures: A Cross-Regional Study
143 325 44.00
Hajli (2014) Social Commerce for Innovation 123 370 33.24
Yahia et al. (2018) Investigating the Drivers for Social Commerce in Social
Media Platforms: Importance of Trust, Social Support
and the Platform Perceived Usage
111 227 48.90
Table 2: Most productive authors
Author h_
index
g_
index
m_
index
TC NP PY_
start
HAJLI N 15 21 1.154 2578 21 2014
DWIVEDI YK 8 11 0.667 256 11 2015
ZHOU T 8 12 0.727 203 12 2016
WANG YC 7 8 0.538 1151 8 2014
AKRAM U 6 6 0.75 360 6 2019
AL-ADWAN AS 6 6 0.667 388 6 2018
LI Y 6 9 0.6 446 9 2017
LIÉBANA-
CABANILLAS F
6 7 0.667 637 7 2018
RANA NP 6 7 0.75 173 7 2019
SARKER P 6 7 0.857 106 7 2020

Shao, et al.: Trust in Social Commerce: Insights from a Bibliometric Review and BERTopic Topic Modelling Analysis
International Review of Management and Marketing | V ol 16 • Issue 6 • 2026
564
Figure 7  presents a treemap of the most frequently occurring
keywords across the social commerce literature. Beyond trust,
keywords reflecting its antecedents, such as support and perceived
risk, indicate sustained scholarly attention toward identifying
the conditions under which consumer trust is formed in social
commerce environments. On the outcome side, the prominence
of purchase intention, behavior, and intention confirms that
behavioural consequences of trust remain the primary dependent
variables of interest across the literature. The presence of
methodological terms such as antecedents, framework, and pls-
sem signals a field that is not only theoretically active but also
increasingly concerned with model development and empirical
Figure 4: Most locally cited sources
Figure 3: Most relevant publication sources
Figure 5: Most relevant institutions

Shao, et al.: Trust in Social Commerce: Insights from a Bibliometric Review and BERTopic Topic Modelling Analysis
International Review of Management and Marketing | V ol 16 • Issue 6 • 2026
565
validation. Taken together, the keyword distribution reveals
that research in this domain has consistently gravitated toward
understanding how trust is formed and how it subsequently shapes
consumer behavioural outcomes.
BERTopic analysis was applied to the abstracts of all 1,055
retrieved documents, yielding 13 distinct topics. Consistent
with recent topic modelling studies, the most relevant keywords
associated with each topic were examined to support topic labelling
(Crain et al., 2012; Mishra, 2025). Each topic was labelled based
on its keywords and documents, as presented in Table 3, topics
are numbered from 0 following BERTopic’s default indexing
convention.
Topic 0 concentrates on trust in the live streaming context. For
example, Cai (2022) found that streamer expertise and interactivity
positively influence consumer trust and purchase intention in live
streaming commerce. Topic 1 captures technology acceptance
research, where trust consistently mediates the relationship
between perceived usefulness and adoption (Gibreel et al., 2018),
with studies also showing that trust in mobile payments transfers
positively to trust in social commerce (Leong et al., 2021). Topic 2
addresses how user-generated content shapes consumer trust, with
recommendations and ratings from other users positively influencing
trust (Hajli, 2015), and trust built through peer endorsement
transferring to trust that drives purchase intention (Cheng et al.,
2019). Topic 3 covers social commerce adoption across diverse
sectors, with Lucila and Ching (2025) extending adoption research
to the agricultural context through a systematic review. Topic 4
centers on impulsive buying behaviour, where interactivity triggers
cognitive and emotional trust responses that lead to impulsive social
shopping (Wu et al., 2024). Topic 5 covers brand trust and influencer
Figure 6: Most relevant countries
Figure 7: Keyword treemap

Shao, et al.: Trust in Social Commerce: Insights from a Bibliometric Review and BERTopic Topic Modelling Analysis
International Review of Management and Marketing | V ol 16 • Issue 6 • 2026
566
marketing in social commerce. For instance, trust in branded posts
has been found to be driven by influencer credibility including
expertise and message quality (Shamim et al., 2024), while celebrity
endorsement and eWOM referrals positively influence brand trust
on Instagram (Danniswara et al., 2020).
Topic 6 examines social influence in social commerce, where
social influence has been found to shape consumer trust and
purchase intention (Karakurt and Bayram, 2021), and social
learning from other users further drives purchase decisions (Riaz
et al., 2021). Topic 7 addresses social relationship dynamics as
antecedents of consumer trust, with social support (Liu et al.,
2019), social capital (Cheng et al., 2019), and social presence
(Anantharaman et al., 2023) each found to positively influence
trust in social commerce. Topic 8 focuses on AI and algorithmic
personalisation in social commerce. Farhan et al. (2025) found
that perceived personalisation from AI product recommendations
significantly enhances consumer trust and purchase intention on
social commerce platforms such as TikTok Shop and Instagram
Shop, while Hsu et al. (2026) showed that recommendation source
shapes consumer trust differently depending on whether it is human
or AI-generated. Topic 9 covers vendor credibility across social
commerce contexts, where consumers evaluate sellers through their
reputation and competence-based signals to form trust (Kubaisi
and Shanab, 2022; Stouthuysen et al., 2018). Topic 10 clusters
research on social commerce trust and purchase behaviour during
and after the COVID-19 pandemic, with studies examining how
trust drives purchase intention in pandemic contexts (Eldin, 2024;
Elshaer et al., 2024; Handarkkho et al., 2024). Topic 11 addresses
privacy concerns, where privacy assurance positively influences
consumer trust in social commerce (Wang and Herrando, 2019).
Topic 12 examines cultural differences in social commerce trust
and purchase intention. Cross-cultural variation in interpersonal
trust in social commerce has been documented across cultural
contexts (Qin, 2020), and the effect of social interaction on trust has
been found to vary across cultural backgrounds (Yin et al., 2019).
Figure 8 presents the proportional distribution of the 13 topics from
2012 to 2025. In the early period, Topic 7 (Social Relationships),
Topic 1 (Technology Acceptance), Topic 2 (User-Generated
Content), and Topic 3 (Social Commerce Adoption) collectively
dominated the literature, reflecting the field’s foundational
interest in social influence mechanisms, platform adoption, and
information-based trust. Topic 11 (Privacy Concerns) also held
a notable share in the early period before gradually declining,
suggesting that privacy issues received relatively more attention
in the early stages of the field. As social commerce became more
widely adopted, research interest in Topic 3 (Social Commerce
Adoption) naturally receded.
From around 2019 onwards, Topic 0 (Live Streaming Commerce)
expanded rapidly and emerged as the largest topic by 2025,
indicating a significant shift in research attention toward real-
time interactive commerce. Topic 10 (COVID-19) showed a
brief elevated presence around 2020-2021 before receding,
reflecting the pandemic’s temporary influence on the research
agenda. Topic 8 (AI in Social Commerce), while minimal before
2022, shows a growing presence in recent years, suggesting an
emerging research frontier. Topic 5 (Brand Trust and Influencer
Marketing) and Topic 4 (Impulsive Buying Behaviour) maintained
relatively stable shares throughout the period, reflecting sustained
research interest in these areas. Topic 6 (Social Influence), Topic 9
(Vendor Credibility), and Topic 12 (Cultural Differences) similarly
maintained stable but modest shares across the entire period.
5. DISCUSSION
This study integrated bibliometric analysis and BERTopic topic
modelling to systematically examine the performance and thematic
characteristics of trust research in social commerce, drawing on
1,055 publications retrieved from Web of Science and Scopus
from 2005 to May 2026. The bibliometric analysis reveals a
field that has grown substantially over the past two decades,
driven predominantly by Asian scholars and anchored within a
concentrated set of influential journals and institutions. Keyword
analysis confirms that trust and its antecedents and outcomes have
consistently occupied the core of the research agenda, a pattern
corroborated by citation analysis showing that a small number of
Table 3: BERTopic research themes
Topic Theme Keywords
Topic 0 Live streaming commerce Live, streaming, streamer, interactivity, video, stream, entertainment, authenticity,
attachment, real
Topic 1 Technology acceptance Mobile, acceptance, payment, tam, adoption, banking, usefulness, ease, neural, artificial
Topic 2 User-generated content Recommendation, transaction, trust_transfer, rating, prediction, fuzzy, reputation,
experimental, supply, issue
Topic 3 Social commerce adoption Adoption, review, area, agricultural, content, collaboration, systematic, evolution, creator, sector
Topic 4 Impulsive buying behaviour Impulse, stimulus, organism, response, flow, cognitive, affective, emotional, similarity, utilitarian
Topic 5 Brand trust and influencer marketing Brand, influencer, authenticity, celebrity, equity, content, attractiveness, credibility,
identification, reliance
Topic 6 Social influence Follower, learning, commercial, professional, educational, scarcity, visit, rank, power, heuristic
Topic 7 Social relationships Social_support, social_capital, social_presence, loyalty, satisfaction, belief, mooring,
emotional, performance, indian
Topic 8 AI in social commerce AI, algorithmic, personalization, expectancy, impulse, retail, recommendation, driven,
governance, recommender
Topic 9 Vendor credibility Vendor, green, innovative, brand, conversion, reputation, buy, competence, food, individual
Topic 10 COVID-19 COVID19, trusting, strategic, jordan, gender, credible, satisfaction, strategy, crisis, age
Topic 11 Privacy concerns Privacy, ethical, concern, interface, smart, institutional, disclosure, trustworthiness, security, longer
Topic 12 Cultural differences Culture, national, cross, adaptation, distance, beauty, intelligence, luxury, identity, meta

Shao, et al.: Trust in Social Commerce: Insights from a Bibliometric Review and BERTopic Topic Modelling Analysis
International Review of Management and Marketing | V ol 16 • Issue 6 • 2026
567
highly cited foundational works established trust as the central
theoretical bridge in social commerce research. Complementing
the bibliometric findings, BERTopic analysis identified 13 research
themes and revealed the thematic evolution of the field. The
following sections discuss the three types of trust identified across
the literature and propose an integrative framework that organises
these themes into a unified structure of antecedents, trust types,
and behavioural outcomes.
5.1. Trust in Social Commerce Research
Although trust permeates all 13 identified topics, a closer
examination of keyword distributions reveals that trust does not
manifest in a single form. Keywords such as institutional in Topic
11 point to institutional trust, while streamer and influencer in
Topics 0 and 5, alongside social_support and social_capital in
Topic 7, implicitly reflect the interpersonal dimensions of trust in
social commerce. Topic 8, with keywords such as ai, algorithmic,
and recommender, signals technology trust as an emerging
dimension. The appearance of trust_transfer in Topic 2 further
suggests the existence of migration pathways between different
trust objects.
Institutional trust is defined as the public’s belief and confidence
that formal organizations, such as social commerce platforms, will
act with integrity, competence, and fairness, and widely regarded
as the foundation of platform-based commerce (Lu and Yi, 2023).
This trust is primarily reflected in Topic 11 (privacy concerns),
where research has concentrated on how platform-level safeguards,
privacy protection mechanisms, and transaction security shape
consumers’ willingness to use social commerce platforms and
make purchases through them. Studies have shown that privacy
assurance positively influences institutional trust (Wang and
Herrando, 2019), while platform governance mechanisms such
as transaction security and seller verification have been found to
strengthen consumers’ confidence in the platform as a reliable
commercial environment (Sembada and Koay, 2021). The
persistent prominence of institutional trust across the literature
reflects the structural vulnerability inherent in social commerce,
where many platforms originated as social networking applications
rather than dedicated commerce infrastructure, leaving consumers
exposed to risks of data misuse and inadequate payment security
(Sembada and Koay, 2021; Wang et al., 2020).
Among the trust objects identified across the literature,
interpersonal trust has attracted sustained and growing attention.
Earlier literature distinguished interpersonal trust from institutional
trust, with interpersonal trust defined as trust between people,
specifically a person’s perception that other people will not act in
ways that harm their interests (Abbas et al., 2023). While early
studies focused predominantly on institutional trust, interpersonal
trust has become increasingly central as social commerce has
evolved into a more social environment. Unlike traditional
e-commerce where trust was primarily directed at the platform or
seller as a single entity, social commerce introduces a considerably
broader range of human actors toward whom consumers may
direct interpersonal trust, including influencers, live streamers,
and fellow consumers, as reflected across Topic 5 (Brand Trust
and Influencer Marketing) and Topic 0 (Live Streaming). Topic
6 (Social Influence) and Topic 7 (Social Relationships) further
reveal the relational and normative mechanisms through which
interpersonal trust is formed and sustained. For example, user
behaviours such as likes, comments, and shares function as social
cues that shape consumer trust (George et al., 2023), and social
support positively influences trust in fellow consumers through
strengthened peer relations (Yang, 2021).
A third trust target emerging from the literature concerns technology
itself. Within social commerce, trust has been conceptualised as
encompassing both trust in people and companies and trust in
the technology that mediates commercial interactions (Sharma
et al., 2019). As social commerce platforms increasingly rely on
technological features, consumers are required to evaluate not
only the human actors they encounter but also the technological
systems through which these interactions occur (Califf et al., 2020).
This dimension of trust has gained growing scholarly attention, as
reflected in Topic 8 (AI in Social Commerce), which captures an
emerging body of research on how consumers form trust toward
AI-driven tools such as recommendation systems, chatbots, and
virtual streamers. Notably, trust in these technological actors might
operate through mechanisms that differ from both institutional and
interpersonal trust. For example, Hsu et al. (2026), comparing
human and machine-generated recommendations in social
commerce, found that trust formation follows distinct patterns
depending on whether the recommendation source is human or
AI. As AI becomes more deeply embedded in social commerce
Figure 8: Evolution of research topics (2012-2025)

Shao, et al.: Trust in Social Commerce: Insights from a Bibliometric Review and BERTopic Topic Modelling Analysis
International Review of Management and Marketing | V ol 16 • Issue 6 • 2026
568
platforms, understanding how consumers form, maintain, and act
upon technology trust represents one of the field’s most pressing
emerging research priorities.
Trust transfer refers to the process by which trust formed
toward a known entity extends to a related but less familiar
entity (Stewart, 2003). In the social commerce literature, trust
transfer has emerged as one of the most frequently employed
theoretical lenses, as reflected in its prominence as a keyword
in Topic 2. The transfer from institutional trust to interpersonal
trust has been a consistent finding across online commerce
research. Foundational e-commerce studies established early on
that platform-level structural assurances facilitate buyers’ trust
in sellers (Pavlou and Gefen, 2004), and this pathway has since
been confirmed in social commerce contexts, where institutional
trust transfers to trust in sellers and streamers (Chen et al., 2024;
Korsakul et al., 2025).
However, in social commerce a reverse transfer pathway, from
interpersonal trust to institutional trust, has also been observed,
reflecting one of its defining characteristics. Some consumers
develop close relationships with sellers (Su et al., 2021) or fellow
users (Leong et al., 2020). When such interpersonal trust is already
established, it can serve as a functional substitute for institutional
trust where platform-level assurances are absent or insufficient (Su
et al., 2021). Robust interpersonal relationships have further been
shown to diminish individuals’ dependency on formal platform
mechanisms (Cheng et al., 2026). This interpersonal trust can
also transfer upward to the platform itself, as consumers who
experience trustworthy interpersonal interactions come to regard
the platform as a credible environment (Cheng et al., 2019).
5.2. Integrative Framework
Building on the discussion of trust targets and their transfer
relationships, this study proposes an integrative framework to
consolidate the findings and provide a coherent foundation for
future inquiry. As illustrated in Figure 9, the framework organizes
the identified research themes into five antecedent dimensions,
namely technology, business, social, information, and consumer,
with trust as the central construct, three behavioural outcomes
comprising social commerce adoption, impulsive buying
behaviour, and technology acceptance, cultural differences as a
moderating variable, and live streaming commerce and COVID-19
as contextual layers.
The framework organises the 13 identified topics into a unified
structure of antecedents, trust mechanisms, and behavioural
outcomes. On the antecedent side, the topics are grouped into
five dimensions: Technology (Topics 1 and 8), Business (Topics
5 and 9), Social (Topics 6 and 7), Information (Topic 2), and
Consumer (Topic 11), each representing a distinct pathway through
which trust is shaped in social commerce contexts. The three
trust types at the center of the framework, namely institutional
trust, interpersonal trust, and technology trust, are derived from
the thematic analysis discussed in the preceding section rather
than from any single topic. On the outcome side, the framework
captures technology acceptance, social commerce adoption,
and impulsive buying behaviour (Topics 1, 3, and 4). Topic 12
(Cultural Differences) is positioned as a moderator, and Topics 0
and 10 (Live Streaming Commerce and COVID-19) are treated
as contextual layers that shape the antecedent-trust relationships
without constituting antecedents themselves.
While this framework is consistent with prior social commerce
frameworks in retaining technology, social, business, and
consumer dimensions as core antecedents (Cui et al., 2018;
Leong et al., 2024; Shao et al., 2026), it differs in several
ways. First, the framework in this study separates the Business
and Information dimensions as distinct antecedent pathways,
reflecting differences in how these factors shape consumer trust.
For example, information-based factors, such as user-generated
content, influence trust through consumers’ active evaluation of
content quality and credibility (Acikgoz et al., 2023). Business-
side factors, including brand credibility, influencer endorsement,
and vendor reputation, operate through commercially generated
signals that consumers use to assess the trustworthiness of
market actors (Shao et al., 2026). Distinguishing these pathways
separately allows for a more precise account of how each
mechanism shapes consumer trust. Second, the framework
incorporates contextual and moderating layers that prior
frameworks have not addressed. Live streaming commerce, while
recognised as a branch of social commerce (Luo et al., 2025),
operates through distinct trust-building mechanisms involving
real-time interaction, streamer, and parasocial relationships
that differ substantially from general social commerce contexts.
COVID-19 is similarly positioned as a contextual layer given its
role as an external disruption that temporarily but substantially
reshaped trust dynamics in social commerce. Cultural differences
are treated as a moderating variable rather than an antecedent,
consistent with evidence that culture does not directly shape
trust but instead alters the strength of relationships between trust
antecedents and their outcomes (Hossain et al., 2021; Qin and
De-Juan-Vigaray, 2021).
Figure 9: Integrated framework

Shao, et al.: Trust in Social Commerce: Insights from a Bibliometric Review and BERTopic Topic Modelling Analysis
International Review of Management and Marketing | V ol 16 • Issue 6 • 2026
569
6. FUTURE DIRECTIONS
The bibliometric analysis reveals a research field that has expanded
substantially over the past two decades. Geographic concentration
remains pronounced, with Asian institutions dominating output
while contributions from Western contexts remain limited. This
imbalance is further reflected in Topic 12 (Cultural Differences),
which has maintained a consistently small share throughout the
study period, suggesting that cross-cultural variations in trust
formation remain underexplored relative to the field’s overall
growth. Scholars have similarly noted that the understanding
of cultural factors on trust remains limited, with only a handful
of studies examining variations across cultural contexts and
have called for more cross-country studies to enhance the
generalizability of findings (Hossain et al., 2021; Qin and De-
Juan-Vigaray, 2021). Future research should expand beyond the
current Asian-dominant focus to include underrepresented regions,
with comparative studies across diverse cultural contexts shedding
light on how cultural factors moderate the relationships between
trust antecedents and outcomes in social commerce.
The thematic evolution identified through BERTopic analysis
reveals a gradual narrowing of themes that once dominated the
early literature. The declining shares of Topic 1 (Technology
Acceptance), Topic 3 (Social Commerce Adoption), and Topic 11
(Privacy Concerns) collectively suggest that social commerce has
matured into a mainstream consumer activity, with foundational
trust concerns around adoption and privacy becoming less central
to the research agenda. Trust research in social commerce is
therefore entering a new phase in which sustaining consumer
trust over time is more critical than securing initial adoption.
Future research should examine how platforms and sellers
maintain consumer confidence, manage trust repair after negative
experiences, and retain consumers in an increasingly competitive
landscape, with trust’s role in continuance intention (Acikgoz
et al., 2023) and loyalty (Attar et al., 2023; Nadeem et al., 2020;
Yeon et al., 2019) representing particularly promising avenues.
Topic 5 (Brand Trust and Influencer Marketing) and Topic 4
(Impulsive Buying Behaviour) have maintained a relatively
stable presence throughout the study period, reflecting sustained
scholarly interest in how commercial actors shape consumer
trust and purchasing behaviour. Much of the existing research
on influencer marketing and brand trust has been conducted
in social media contexts rather than social commerce settings
specifically. The introduction of embedded checkout features and
one-click purchasing within social commerce platforms (Han,
2023) compresses the time between trust formation and purchase
execution, potentially altering how trust is established. Under these
conditions, the role of influencer and brand in triggering impulsive
purchases warrants closer examination. For example, future
research can further explore the distinction between impulsive
and planned buying in social commerce (Gvili and Levy, 2023),
with particular attention to the potentially different roles that trust
plays in each.
The rapid rise of Topic 0 (Live Streaming Commerce) and the
emerging presence of Topic 8 (AI in Social Commerce) signal
that social commerce is entering an increasingly interactive and
technologically mediated phase, opening new frontiers for trust
research. Within the AI domain alone, existing studies have
begun to focus on chatbots (Sindhu and Bharti, 2024) and AI
personalization (Emini et al., 2025), presenting opportunities to
further investigate how these AI-driven features relate to consumer
trust. Beyond these, emerging technologies including AI beings,
augmented and virtual reality, and metaverse commerce are
beginning to enter the social commerce landscape (Al-Makhmari
et  al., 2024; Duong, 2025; Xiong et al., 2024), with their
implications for consumer trust remaining largely unexplored.
Future research should examine how consumers form trust
toward these novel technological actors, how such trust transfers
to products and sellers, and under what conditions technology-
mediated trust breaks down, as understanding these dynamics
will be critical for both scholars and practitioners navigating an
increasingly AI-driven social commerce environment.
Finally, the thematic analysis points to the need for a more
multidimensional conceptualization of trust in social commerce.
Scholars have long recognized that trust is a complex construct
that operates through multiple bases and toward multiple entities,
and have called for research to move beyond treating trust as
a single, unidimensional construct (Khamitov et al., 2024).
The three types of trust identified in the present study, namely
institutional trust, interpersonal trust, and technology trust,
offer a multidimensional lens through which future research can
advance. As social commerce infrastructure matures, institutional
trust may attract comparatively less scholarly attention, while
interpersonal trust, as a defining characteristic of social commerce,
is likely to sustain continued research interest. Technology trust,
however, represents the most consequential emerging frontier,
as evidenced by the rapid growth after 2022. As AI-driven tools
and immersive technologies become more deeply embedded in
social commerce environments, understanding how trust formed
toward technology will be essential for both theory development
and practice. The trust transfer process involving technology trust
remains underexplored, and future research can further investigate
the conditions under which trust transfers successfully or fails
between them.
7. CONCLUSION
This study integrated bibliometric analysis and BERTopic topic
modelling to systematically examine the intellectual landscape of
trust research in social commerce, drawing on 1,055 publications
retrieved from Web of Science and Scopus spanning from 2005 to
May 2026. In response to the three research questions, the study
mapped publication trends, identified influential contributors,
journals, and institutions, and uncovered 13 distinct research
themes through topic modelling. The bibliometric findings reveal a
field that has grown substantially over the past two decades, driven
predominantly by Asian scholars and concentrated within a small
number of influential journals and institutions. The BERTopic
analysis demonstrates that the thematic landscape of trust research
has undergone considerable evolution, with foundational themes
such as technology acceptance and social commerce adoption
declining in prominence as the field matures, and newer themes

Shao, et al.: Trust in Social Commerce: Insights from a Bibliometric Review and BERTopic Topic Modelling Analysis
International Review of Management and Marketing | V ol 16 • Issue 6 • 2026
570
such as live streaming commerce and AI in social commerce
emerging as significant research frontiers. Building on these
findings, the study proposed an integrative framework that
organizes trust research in social commerce around five antecedent
dimensions, a central trust construct, three behavioural outcomes,
a moderating variable, and two contextual layers, providing a
coherent foundation for future inquiry.
This study makes several contributions to both research and
practice. Methodologically, integrating bibliometric analysis
with BERTopic topic modelling offers a more comprehensive
and semantically nuanced mapping of the field than keyword-
based or manual approaches alone. Theoretically, the proposed
integrative framework consolidates trust research across five
antecedent dimensions in a manner more granular than prior social
commerce frameworks, and the identification of institutional,
interpersonal, and technology trust as distinct but interrelated
trust targets provides a multidimensional lens for future inquiry.
For practitioners, the prominence of business-side trust signals
suggests that platforms and sellers should invest in transparent
credibility mechanisms and verified seller programmes, while
the rise of live streaming and AI-driven personalization calls for
attention to the distinct trust-building demands these environments
introduce. The persistence of privacy concerns further underscores
the importance of robust data protection practices as a foundational
condition for consumer trust.
Several limitations should be acknowledged. First, the literature
corpus was drawn exclusively from Web of Science and Scopus,
and non-English publications were excluded, which may have
resulted in the omission of relevant studies published in other
languages or indexed in other databases. Second, while BERTopic
topic modelling provides a scalable and systematic approach to
theme identification, the analysis is based on abstracts rather than
full-text content, which may result in a partial representation
of the conceptual nuances within each theme. For instance, the
finer-grained distinctions within trust, such as its dimensionality
and the specific types of trust examined across studies, may not
be fully captured through abstract-level analysis alone. Future
research could complement the present findings by conducting
in-depth systematic literature reviews of specific themes, enabling
more detailed synthesis of how trust is conceptualized and
operationalized across different social commerce contexts.
REFERENCES
Abbas, S., Alnoor, A., Sin Yin, T., Mohammed Sadaa, A., Raad Muhsen, Y .,
Wah Khaw, K., Ganesan, Y . (2023), Antecedents of trustworthiness of
social commerce platforms: A case of rural communities using multi
group SEM & MCDM methods. Electronic Commerce Research and
Applications, 62, 101322.
Acikgoz, F., Busalim, A., Gaskin, J., Asadi, S. (2023), An integrated model
for information adoption&trust in mobile social commerce. Journal
of Computer Information Systems, 64, 797-819.
Ahmad, A., Ghani, N.A., Hamid, S. (2025), Examining the predictors
of consumer trust and social commerce engagement: A  systematic
literature review. Journal of Theoretical and Applied Electronic
Commerce Research, 20(3), 247.
Al-Makhmari, L., Tarhini, A., Nikhashemi, S.R., Nusair, K., Al Shaqsi, J.
(2024), Factors influencing user adoption of social commerce in the
metaverse: The moderating role of technology comfort, e-word-
of-mouth, and endowment effect. International Journal of Human
Computer Interaction, 14, 1-16.
Anantharaman, R., Prashar, S., Vijay, T.S. (2023), Uncovering the role of
consumer trust and bandwagon effect influencing purchase intention:
An empirical investigation in social commerce platforms. Journal of
Strategic Marketing, 31(6), 1199-1219.
Aria, M., Cuccurullo, C. (2017), bibliometrix : An R-tool for
comprehensive science mapping analysis. Journal of Informetrics,
11(4), 959-975.
Attar, R.W., Almusharraf, A., Alfawaz, A., Hajli, N. (2022), New
trends in e-commerce research: Linking social commerce and
sharing commerce: A  systematic literature review. Sustainability
(Switzerland), 14(23), 16024.
Attar, R.W., Amidi, A., Hajli, N. (2023), The role of social presence and
trust on customer loyalty. British Food Journal, 125(1), 96-111.
Bugshan, H., Attar, R.W. (2020), Social commerce information sharing
and their impact on consumers. Technological Forecasting and Social
Change, 153, 119875.
Cai, H. (2022), Examining social E-commerce platforms by mediating
the effect of perceived usefulness and perceived trust using the
technology acceptance model. Journal of Organizational and End
User Computing, 34(8), 1-20.
Califf, C.B., Brooks, S., Longstreet, P. (2020), Human-like and system-like
trust in the sharing economy: The role of context and humanness.
Technological Forecasting and Social Change, 154, 119968.
Chen, J., Shen, X.L. (2015), Consumers’ decisions in social commerce
context: An empirical investigation. Decision Support Systems,
79, 55-64.
Chen, Y ., Li, M., Chen, A., Lu, Y . (2024), Trust development in live
streaming commerce: Interaction-based building mechanisms and
trust transfer perspective. Industrial Management and Data Systems,
124(12), 3218-3239.
Cheng, X., Gu, Y ., Shen, J. (2019), An integrated view of particularized
trust in social commerce: An empirical investigation. International
Journal of Information Management, 45, 1-12.
Cheng, X., Xu, Y ., Yang, B., Liu, Y . (2026), Understanding streamers’
intention to live stream in the context of rural live streaming commerce:
A mixed-methods study. Internet Research, 36(2), 822-846.
Crain, S.P., Zhou, K., Yang, S.H., Zha, H. (2012), Dimensionality
reduction and topic modeling: From latent semantic indexing to
latent dirichlet allocation and beyond. Mining Text Data, 129-161.
Cui, Y ., Mou, J., Liu, Y . (2018), Knowledge mapping of social commerce
research: A visual analysis using CiteSpace. Electronic Commerce
Research, 18, 837-868.
Danniswara, R., Sandhyaduhita, P., Munajat, Q. (2020), The Impact of
EWOM Referral, Celebrity Endorsement, and Information Quality
on Purchase Decision. In: Global Branding. United States: IGI
Global. p882-905.
Donthu, N., Kumar, S., Mukherjee, D., Pandey, N., Lim, W.M. (2021),
How to conduct a bibliometric analysis: An overview and guidelines.
Journal of Business Research, 133, 285-296.
Duong, N.T. (2025), Factors affecting users’ continuance intention to use
social network sites: A sample of Vietnamese Facebookers. International
Journal of Mobile Learning and Organisation, 19(1), 87-112.
Egger, R., Yu, J. (2022), A topic modeling comparison between lda,
nmf, top2vec, and bertopic to demystify twitter posts. Frontiers in
Sociology, 7, 886498.
Eldin, A. (2024), Understanding purchase intentions in crisis: The role
of trust and perceived value in Sudan’s F-commerce during the
COVID-19 pandemic. International Journal of Advanced and Applied
Sciences, 11(9), 76-87.

Shao, et al.: Trust in Social Commerce: Insights from a Bibliometric Review and BERTopic Topic Modelling Analysis
International Review of Management and Marketing | V ol 16 • Issue 6 • 2026
571
Elshaer, I.A., Alrawad, M., Lutfi, A., Azazz, A.M.S. (2024), Social
commerce and buying intention post COVID-19: Evidence from a
hybrid approach based on SEM - fsQCA. Journal of Retailing and
Consumer Services, 76, 103548.
Emini, A., Budić, H., Klopotan, I. (2025), AI-driven personalisation and
customer engagement in social commerce: Evidence from Kosovo.
Business Systems Research Journal, 16(2), 145-167.
Esmaeili, L., Hashemi, G.S.A. (2019), A systematic review on social
commerce. Journal of Strategic Marketing, 27(4), 317-355.
Farhan, M.T., Leunufna, K., Halim, E. (2025), Beyond Clicks and
Carts: The Impact of Perceived Personalization via AI Product
Recommendations on Purchase Intention in Social Commerce. In:
2025 8 th International Conference of Computer and Informatics
Engineering (IC2IE). p1-7.
Gefen, D. (2000), E-commerce: The role of familiarity and trust. Omega,
28(6), 725-737.
Gefen, D.V ., Rao, S., Tractinsky, N. (2003), The Conceptualization
of Trust, Risk and Their Relationship in Electronic Commerce:
The Need for Clarifications. In: Proceedings of the 36 th Hawaii
International Conference on System Sciences (HICSS).
George, A., Joseph, A., Abraham, M., Joseph, E.T. (2023), Brand trust and
engagement in social commerce. International Journal of Consumer
Studies, 47(5), 1791-1809.
Gibreel, O., AlOtaibi, D.A., Altmann, J. (2018), Social commerce
development in emerging markets. Electronic Commerce Research
and Applications, 27, 152-162.
Grootendorst, M. (2022), BERTopic: Neural Topic Modeling with a
Class-Based TF-IDF Procedure; [ArXiv Preprint].
Gutiérrez-Salcedo, M., Martínez, M.Á., Moral-Munoz, J.A., Herrera-
Viedma, E., Cobo, M.J. (2018), Some bibliometric procedures for
analyzing and evaluating research fields. Applied Intelligence, 48,
1275-1287.
Gvili, Y ., Levy, S. (2023), I share, therefore I trust: A moderated mediation
model of the influence of eWOM engagement on social commerce.
Journal of Business Research, 166, 114131.
Hajli, M. (2013), A research framework for social commerce adoption.
Information Management and Computer Security, 21(3), 144-154.
Hajli, M.N. (2014), Social commerce for innovation. International Journal
of Innovation Management, 18(04), 1450024.
Hajli, N. (2015), Social commerce constructs and consumer’s intention
to buy. International Journal of Information Management, 35(2),
183-191.
Hajli, N., Sims, J., Zadeh, A.H., Richard, M.O. (2017), A social commerce
investigation of the role of trust in a social networking site on
purchase intentions. Journal of Business Research, 71, 133-141.
Han, M.C. (2023), Checkout button and online consumer impulse-buying
behavior in social commerce: A trust transfer perspective. Journal of
Retailing and Consumer Services, 74, 103431.
Handarkkho, Y .D., Sulistyaningtyas, I.D., Rismayanti, R. (2024), The
influence of social impact and community attribute toward tourist
trust formation on social commerce in the aftermath of the COVID-19
pandemic: A case study of a tourist village in Indonesia. Tourism
and Hospitality Management, 30(1), 133-145.
Hossain, A., Jahan, N., Kim, M., Yesmin, N., Hasan, R. (2021), Social
support for social commerce: An empirical study with trust as a
mediator and culture as moderator. Journal of Korea Trade, 25(7),
75-91.
Hsu, C.L., Lin, J.C.C., Miao, Y .F. (2026), Product recommendation source,
persuasive messages and media richness in social commerce. Journal
of Business Research, 204, 115874.
Huang, Z., Benyoucef, M. (2013), From e-commerce to social commerce:
A close look at design features. Electronic Commerce Research and
Applications, 12(4), 246-259.
Karakurt, N., Bayram, P. (2021), Analysis of factors influencing
consumer’s purchase intention in social commerce: The mediator
role of trust. International Journal of Data and Network Science,
5, 351-360.
Khamitov, M., Rajavi, K., Huang, D.W., Hong, Y . (2024), Consumer
trust: Meta-analysis of 50 years of empirical research. Journal of
Consumer Research, 51(1), 7-18.
Kim, S., Park, H. (2013), Effects of various characteristics of social
commerce (s-commerce) on consumers’ trust and trust performance.
International Journal of Information Management, 33(2), 318-332.
Korsakul, N., Chen, J.S., Tsou, H.T. (2025), Influence of the characteristics
of dual-role platforms and streamers on consumer trust and purchase
intention in live streaming commerce. Service Business, 19(3), 18.
Kubaisi, H.H.A., Shanab, E.A.A. (2022), Factors influencing trust in social
commerce: The case of Qatar. International Journal of Electronic
Business, 17(1), 13.
Laradi, S., Alrawad, M., Lutfi, A., Agag, G. (2024), Understanding
factors affecting social commerce purchase behavior: A longitudinal
perspective. Journal of Retailing and Consumer Services, 78, 103751.
Leong, L.Y ., Hew, T.S., Ooi, K.B., Chong, A.Y .L. (2020), Predicting
the antecedents of trust in social commerce - A hybrid structural
equation modeling with neural network approach. Journal of Business
Research, 110, 24-40.
Leong, L.Y ., Hew, T.S., Ooi, K.B., Chong, A.Y .L., Lee, V .H. (2021),
Understanding trust in ms-commerce: The roles of reported
experience, linguistic style, profile photo, emotional, and cognitive
trust. Information and Management, 58(2), 103416.
Leong, L.Y ., Hew, T.S., Ooi, K.B., Hajli, N., Tan, G.W.H. (2024),
Revisiting the social commerce paradigm: The social commerce
(SC) framework and a research Agenda. Internet Research, 34(4),
1346-1393.
Liang, T.P., Turban, E. (2011), Introduction to the special issue social
commerce: A research framework for social commerce. International
Journal of Electronic Commerce, 16(2), 5-14.
Liu, Y ., Su, X., Du, X., Cui, F. (2019), How social support motivates
trust and purchase intentions in mobile social commerce. Review
of Business Management, 21(4), 839-860.
Lu, B., Fan, W., Zhou, M. (2016), Social presence, trust, and social
commerce purchase intention: An empirical research. Computers
in Human Behavior, 56, 225-237.
Lu, B., Yi, X. (2023), Institutional trust and repurchase intention in the
sharing economy: The moderating roles of information privacy
concerns and security concerns. Journal of Retailing and Consumer
Services, 73, 103327.
Lucila, N.B., Ching, M.R.D. (2025), Understanding social commerce
adoption in agriculture: A  systematic literature review. Electronic
Commerce Research and Applications, 74, 101543.
Luo, X., Lim, W.M., Cheah, J.H., Lim, X.J., Dwivedi, Y .K. (2025), Live
streaming commerce: A  review and research Agenda. Journal of
Computer Information Systems, 65(3), 376-399.
Ma’ady, M.N.P., Wardhani, S.A.K. (2022), Analysis of trust mechanism
in social commerce: A  systematic literature review. International
Journal of Electronic Commerce Studies, 13(2), 223.
Mayer, R.C., Davis, J.H., Schoorman, F.D. (1995), An integrative model
of organizational trust. Academy of Management Review, 20(3),
709-734.
McKnight, D.H., Choudhury, V ., Kacmar, C. (2002), The impact of initial
consumer trust on intentions to transact with a web site: A  trust
building model. The Journal of Strategic Information Systems,
11(3-4), 297-323.
Mishra, M. (2025), A holistic review of customer experience research:
Topic modelling using BERTopic. Marketing Intelligence and
Planning, 43(4), 802-820.

Shao, et al.: Trust in Social Commerce: Insights from a Bibliometric Review and BERTopic Topic Modelling Analysis
International Review of Management and Marketing | V ol 16 • Issue 6 • 2026
572
Mordor Intelligence. (2026), Social Commerce Market Size & Share
Analysis - Growth Trends and Forecast (2026 - 2031). Available
from: https://www.mordorintelligence.com/industry-reports/social-
commerce-market
Nadeem, W., Khani, A.H., Schultz, C.D., Adam, N.A., Attar, R.W.,
Hajli, N. (2020), How social presence drives commitment and loyalty
with online brand communities? the role of social commerce trust.
Journal of Retailing and Consumer Services, 55, 102136.
Ng, C.S.P. (2013), Intention to purchase on social commerce websites
across cultures: A cross-regional study. Information and Management,
50(8), 609-620.
Paul, J., Lim, W.M., O’Cass, A., Hao, A.W., Bresciani, S. (2021), Scientific
procedures and rationales for systematic literature reviews (SPAR‐4‐
SLR). International Journal of Consumer Studies, 45(4), O1-O16.
Pavlou, P.A., Gefen, D. (2004), Building effective online marketplaces with
institution-based trust. Information Systems Research, 15(1), 37-59.
Qin, L. (2020), A cross-cultural study of interpersonal trust in social
commerce. Journal of Computer Information Systems, 60(1), 26-33.
Qin, L., De-Juan-Vigaray, M.D. (2021), Social commerce: Is interpersonal
trust formation similar between U.S.A. and Spain? Journal of
Retailing and Consumer Services, 62, 102642.
Riaz, M.U., Guang, L.X., Zafar, M., Shahzad, F., Shahbaz, M., Lateef, M.
(2021), Consumers’ purchase intention and decision-making process
through social networking sites: A  social commerce construct.
Behaviour and Information Technology, 40(1), 99-115.
Rousseau, D.M., Sitkin, S.B., Burt, R.S., Camerer, C. (1998), Not so
different after all: A  cross-discipline view of trust. Academy of
Management Review, 23(3), 393-404.
Sembada, A.Y ., Koay, K.Y . (2021), How perceived behavioral control
affects trust to purchase in social media stores. Journal of Business
Research, 130, 574-582.
Shamim, K., Azam, M., Islam, T. (2024), How do social media influencers
induce the urge to buy impulsively? Social commerce context.
Journal of Retailing and Consumer Services, 77, 103621.
Shao, Y ., Rosli, N., Hashim, S. (2026), Tracing trends and topics in two
decades of social commerce research: A  bibliometric and topic
modeling analysis. Cogent Business and Management, 13(1),
2604902.
Sharma, S., Menard, P., Mutchler, L.A. (2019), Who to trust? Applying
trust to social commerce. Journal of Computer Information Systems,
59(1), 32-42.
Sheikh, Z., Yezheng, L., Islam, T., Hameed, Z., Khan, I.U. (2019), Impact
of social commerce constructs and social support on social commerce
intentions. Information Technology and People, 32(1), 68-93.
Sindhu, P., Bharti, K. (2024), Influence of chatbots on purchase intention
in social commerce. Behaviour and Information Technology, 43(2),
331-352.
Stewart, K.J. (2003), Trust transfer on the World Wide Web. Organization
Science, 14(1), 5-17.
Stouthuysen, K., Teunis, I., Reusen, E., Slabbinck, H. (2018), Initial
trust and intentions to buy: The effect of vendor-specific guarantees,
customer reviews and the role of online shopping experience.
Electronic Commerce Research and Applications, 27, 23-38.
Su, C., Min, Q., Scornavacca, E., Liu, Z. (2021), A dual-role trust
model for social commerce: A guanxi perspective. Information and
Management, 58(7), 103512.
Tseng, H.T. (2023), Shaping path of trust: The role of information
credibility, social support, information sharing and perceived privacy
risk in social commerce. Information Technology and People, 36(2),
683-700.
Tseng, H.T., Nadeem, W., Hajli, M.S., Featherman, M., Hajli, N. (2023),
Understanding consumers’ interest in social commerce: The role
of privacy, trust and security. Information Technology and People,
38, 472-496.
Wang, X., Tajvidi, M., Lin, X., Hajli, N. (2020), Towards an ethical and
trustworthy social commerce community for brand value co-creation:
A trust-commitment perspective. Journal of Business Ethics, 167(1),
137-152.
Wang, Y ., Herrando, C. (2019), Does privacy assurance on social
commerce sites matter to millennials? International Journal of
Information Management, 44, 164-177.
Wongkitrungrueng, A., Assarut, N. (2020), The role of live streaming
in building consumer trust and engagement with social commerce
sellers. Journal of Business Research, 117, 543-556.
Wu, W., Yang, Q., Gong, X. (2024), Impulsive social shopping in social
commerce platforms: The role of perceived proximity. Information
Systems Frontiers, 26(4), 1527-1541.
Xiong, J., Wang, Y ., Li, Z. (2024), Understanding the relationship between
IT affordance and consumers’ purchase intention in E-commerce live
streaming: The moderating effect of gender. International Journal of
Human Computer Interaction, 40(20), 6303-6313.
Yahia, I.B., Al-Neama, N., Kerbache, L. (2018), Investigating the drivers
for social commerce in social media platforms: Importance of trust,
social support and the platform perceived usage. Journal of Retailing
and Consumer Services, 41, 11-19.
Yang, X. (2021), Exchanging social support in social commerce: The
role of peer relations. Computers in Human Behavior, 124, 106911.
Yeon, J., Park, I., Lee, D. (2019), What creates trust and who gets loyalty
in social commerce? Journal of Retailing and Consumer Services,
50, 138-144.
Yin, X., Wang, H., Xia, Q., Gu, Q. (2019), How social interaction affects
purchase intention in social commerce: A  cultural perspective.
Sustainability, 11(8), 2423.
Yu, D., Xiang, B. (2023), Discovering topics and trends in the field of
Artificial Intelligence: Using LDA topic modeling. Expert Systems
with Applications, 225, 120114.
Zhao, W., Hu, F., Wang, J., Shu, T., Xu, Y . (2023), A systematic literature
review on social commerce: Assessing the past and guiding the
future. Electronic Commerce Research and Applications, 57, 101219.
Zhao, Y ., Wang, L., Tang, H., Zhang, Y . (2020), Electronic word-of-mouth
and consumer purchase intentions in social e-commerce. Electronic
Commerce Research and Applications, 41, 100980.
