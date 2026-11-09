---
title: Bibliometric Analysis of Publications on Impulsive Buying from 2000 to 2025 in the Scopus Database
  Using R and VOSviewer
url: https://doi.org/10.21203/rs.3.rs-9195074/v1
category: survey
subcategory: review
date: 2026-04
venue: Research Square
authors:
- XuZheng Qiu
- Ree Chan Ho
- Sharif Hassan
source: openalex-oa
pdf_url: https://www.researchsquare.com/article/rs-9195074/latest.pdf
pages: 29
chars: 46204
fetched_at: '2026-11-08T18:54:34+00:00'
kb_version: 1
---

# Bibliometric Analysis of Publications on Impulsive Buying from 2000 to 2025 in the Scopus Database Using R and VOSviewer

Bibliometric Analysis of Publications on Impulsive
Buying from 2000 to 2025 in the Scopus Database
Using R and VOSviewer
XuZheng Qiu 
Taylor's University
Ree Chan Ho 
Taylor's University
Sharif Hassan Md 
Taylor's University
Systematic Review
Keywords: bibliometric analysis, impulsive buying, Scopus, Biblioshiny application, Bibliometrix package,
R, VOSviewer
Posted Date: April 24th, 2026
DOI: https://doi.org/10.21203/rs.3.rs-9195074/v1
License:   This work is licensed under a Creative Commons Attribution 4.0 International License.  
Read Full License
Additional Declarations: No competing interests reported.
Page 1/29

Abstract
Buying trend has become one of the key topic of research in consumer behavior studies due to
psychological events and online marketing phenomena. Although many researches have explored
consumer decision-making, little research has analyzed the research trends of impulsive buying based
on bibliometrics. The aim of this study was to explore the global publication trends and research
hotspots of the impulsive buying from 2000 to 2025 based on the bibliometric analysis. The searched
deﬁned term was “impulsive buying”, which produced 464 hits across the articles, reviews, conference
papers and book chapters in Scopus. With the help of Bibliometrix, Biblioshiny in R and VOSviewer, were
used for data organization and visualization. The examination similarly demonstrated an increasing
number of papers, especially post 2018, with China, India, and Malaysia acting as dominant knowledge
producers. The most proliﬁc authors were Luo X and Parsad C, and Journal of Retailing and Consumer
Services was the leading source of publications. The main research themes were hedonic motivation,
online shopping, social commerce, and self-control. The intellectual structure, theme progress and 
global cooperation of impulsive buying research were systematically summarized in this study. Such
understanding could help scholars, practitioners, and policy makers address the trajectory of the
research ﬁeld and ﬁnd further research opportunities.
1. Introduction
During the last two and half decades, impulsive purchasing has gained great attention in marketing,
consumer psychology, behavioral economics, and online commerce (Chandrasekhar et al., 2024; Gulfraz
et al., 2022). When the retail environment in the world changes dramatically to become digital ones,
learning about impulsive purchasing is essential for academics and practitioners in order to avoid that
what causes their business. The proliferation of e-commerce websites, mobile shopping apps, digital
ads, and social media inﬂuencers have radically transformed the conventional models of consumer
decision making, giving new relevance to impulsive buying in the online market environment
(Chandrasekhar et al., 2024; Rajib & Roy, 2023).
Impulse purchase is buying something spontaneously, without advance intention to do so (Gonzalez,
2021). This behavior has been positively associated with a wide range of psychological, environmental
and situational features, including time-pressures, mood states, product saliency, scarcity cues, and
digital nudges. Virtual spaces offer many opportunities for such behavior because of their vibrant and
interactive nature. Elements such as personalized recommendations, one-click payment facilities, and 
constant access have increased the chances that a person will engage in impulse buying (Barauskaitė,
2025; Chandrasekhar et al., 2024). This topic has attracted much academic interest and there is growing
number of research papers on the antecedents, mechanisms, and consequences of this topic (Thomas
& Gupta, 2022).
Impulsive buying research keeps growing, it is critically important to systematically review the
development of the related area (Kaur & Sharma, 2024). In spite of the growing body of conceptual and
Page 2/29

empirical work on impulsive purchase behavior in oﬄine and online modes, few meta-analyses have
been conducted to map the intellectual structure of this ﬁeld of inquiry. Bibliometric analysis, as an 
effective methodological means, provides a quantitative and visual way to analyze the scientiﬁc
evolution, cooperation network and hotspots in a speciﬁc domain during a period of time (Pessin et al.,
2022). It enables the researchers to determine the publishing trends, productive authors and institutions,
inﬂuential documents, and changes in research focus (Yan & Zhiping, 2023).
Bibliometric software, and in particualr R-based softwares like Bibliometrix and software for visualization
like VOSviewer, have led to the possibility of performing large-scale and reproducible analysis on large
sets of bibliographic records (Dahish & Miah, 2022; Shi & Duan, 2024). These provide functionality that
allows researchers to explore different citation-based indicators such as co-authorship networks,
keyword co-occurrence and thematic clustering, allowing researchers to delve deep into the structural
and dynamic properties of a research domain. These methods have been extensively used in various
ﬁelds from medical sciences to environmental science ﬁelds, technology management and social
science, but little bibliometric analyzes of impulsive buying can be seen (Dalal et al., 2023).
This study has been designed, in order to bridge this gap through a bibliometric analysis of the
documents on impulsive buying behavior published during the period 2000–2025 and indexed in
Scopus. Scopus is the database selected because it covers the most inﬂuential journals and is
conducive to bibliometric study (Singh et al., 2021). The analysis not only provides historical picture of
the publication trends but also traces the evolution of research fronts, patterns of collaboration between
authors and countries, and intellectual base leading the ﬁeld. In light of this, the present research
provides useful insights into the development of impulsive buying as a topic and the possible future
research directions.
The rapid growth of e-retailing (especially after 2010) has been a driving force in pushing academic
research in understanding consumer impulsivity in the online context. The interdisciplinary character of
research on impulsive buying subject, psychology, marketing, decision sciences and information
systems- requires an exhaustive survey to comprehend the knowledge structure. The utilization of data-
driven approaches like bibliometric analysis contributes to evidence-based decision-making in academic
planning, journal growth, and funding distribution. With help of the bibliometric mapping approach,
underexplored ﬁelds can be identiﬁed, research collaboration discouraged, and direction for doctoral or
postdoctoral research be provided.
A ﬁrst analysis of the literature indicates that impulsive buying has been dealt with from the
perspectives of emotional intelligence, self-control, web site design, social inﬂuence, and consumer
personality. The COVID-19 crisis and lockdown measures have also led to renewed interest in online
impulsivity given increased digital use and stress-related consumption (Pautrat et al., 2022). Despite
this increasing interest, however, no study ever has amalgamated this divergent stream of research 
output into an overarching bibliometric review. Current reviews are often narrative or thematic and do
not have the quantitative rigor nor visual analytics as provided by bibliometric approaches.
Page 3/29

This study utilized a stringent bibliometric approach leveraging R (Bibliometrix and Biblioshiny), and
VOSviewer to decode the trends, patterns and networks implicit in impulsive buying research. It aims to
answer the main following research questions:
RQ1: What are the annual publication trends in impulsive buying research from 2000 to 2025?
RQ2: Who are the most productive and inﬂuential authors, institutions, and countries in this ﬁeld?
RQ3: What are the prominent themes, keywords, and conceptual structures emerging from the
literature?
RQ4: How has the intellectual and social structure of impulsive buying research evolved over time?
RQ5: What research gaps and future directions can be derived from the bibliometric ﬁndings?
The research implications of this study are theoretical and practical. In theory, it presents an integrated
picture of the knowledge map and development topic of impulsive purchasing. It provides researchers,
educators, and marketers with the means to consider new perspectives on impulsive buying and
develop interdisciplinary models and consumer engagement strategies in digital media.
This paper is arranged as follows: Section 2 describes the materials and methods, which consist of data
collection and analytical methods. Section 3 provides the main results of the bibliometric analysis, and
Section 4 addresses ﬁndings. A brief conclusion is given in Section 5 and Section 6 provides future
research trend and directions according to existing gaps and emerging trends.
2. Materials and Methods
Through bibliometric studies, researchers are offered a robust method of a quantitative nature with
which to investigate and map the intellectual structure of a research domain. These are all systematic,
reproducible data-driven analyses, as opposed to traditional literature reviews which tend to be
qualitative and are inﬂuenced by interpretive bias. The present work uses bibliometric analysis to
analyze the scholarly research of impulsive buying behavior between the year 2000–2025. The Scopus
database extracted the data, the R-based package Bibliometrix and its web interface Biblioshiny was
used for the analysis, and data visualization was made with VOSviewer.
Bibliometrics is one of the methodological tools for the quantitative analyses of the tons of scientiﬁc
literature (Singh et al., 2021). It uncovers patterns, authorship constellations, pivotal articles, thematic
clusters, and intellectual bridges statistically. Descriptive analysis and content analysis were used for
this study. Descriptive analysis was used to measure temporal patterns in publications, and content
analysis of keyword occurrences and citation analysis revealed thematic tendencies in impulsive buying
literature.
2.1 Database Source and Search Strategy
Page 4/29

Scopus was selected as the primary data source due to its extensive indexing of high-impact peer-
reviewed literature across disciplines. The Scopus database also allows for the export of complete
bibliographic metadata, which is necessary for conducting a robust bibliometric evaluation (Caputo &
Kargina, 2022). The document search was conducted by applying the following query string:
"Impulsive buying"
This search was performed for indexing terms in the title, abstract, and author keyword ﬁelds to retrieve
all potentially relevant publications. The search period was from January 2000 to April 2025. Only
English language articles were included to ensure linguistic consistency and minimize ambiguities in
content analysis from translation.
The primary search yielded 464 Scopus records. The types of document consisted of journal article,
conference paper, book chapter, and review.
2.2 Inclusion and Exclusion Criteria
The study carefully selected the peer-reviewed journal articles, conference papers, book chapters, and
review articles to maintain quality and relevancy of the dataset. Editorials, short notations, letters to the
editors, and preprints were not considered. The title and abstract were manually screened for duplicate
entries and for irrelevant records (e.g., DRM and “impulsive buying” in a non-consumer behavior
context), and the records of irrelevant articles were deleted.
2.3 Data Preparation and Cleaning
The bibliographic records were exported in .CSV, with metadata such as title, authors, abstract,
keywords, source title, aﬃliations, country, document type, and citations. The dataset was then imported
into RStudio and the R package Bibliometrix was utilized to preprocess and analyze the data. The study
launched the web interfaces of the package, Biblioshiny, by executing the command biblioshiny() so that
it becomes accessible to users who are not quite proﬁcient in programming.
Bibliometrix package provided the possibility to obtain publication trends, impact of sources, productivity
of authors, collaboration networks at country level and keywords co-occurrence maps. It further allowed
the application to Bradford's law to characterize the core journals and to the law of Lotka to assess the
productivity of the authors (Agrawal, 2025).
2.4 Network Visualization with VOSviewer
Biblioshiny, alongside VOSviewer, was used for network mapping and visualization of bibliometric data.
VOSviewer allows the creation and visualisation of bibliometric networks construced from co-
authorship, co-occurrence, citation, bibliographic coupling and co-citation data. The application makes
it possible to interactively map the graph of terms, keywords and authors.
The keyword co-occurrence network was built with VOSviewer’s text mining function, which accounts for
VOSviewer internal algorithm to determine relatedness and clustering of keywords by reference to the
Page 5/29

co-appearance in the titles and abstracts. Citation and co-authorship networks were generated to
identify key participants and collaborate institutions. For the mapping and the identiﬁcation, the
VOSviewer enables the use of clustering algorithm and customization in content viewing (enlarging,
color & density), thus fostering an easy comprehension about thematic concentration and research
gaps.
2.5 Data Analysis Objectives
The bibliometric analysis focused on answering the following core objectives:
Descriptive Analytics: Identify annual publication trends, top publishing journals, most cited
documents, and most productive authors.
Geographical Analysis: Determine the leading countries and institutions contributing to impulsive
buying research.
Authorship and Collaboration Patterns: Map co-authorship networks and institutional aﬃliations.
Keyword and Thematic Evolution: Analyze keyword frequency and co-occurrence to detect emerging
research themes and conceptual shifts.
Citation Structures: Identify the most cited papers and sources to determine intellectual inﬂuence.
The processed results were exported in graphical formats (e.g., .PNG, .CSV) and integrated into the
study’s ﬁndings section to provide clear evidence supporting the bibliometric conclusions.
3. Results
The bibliometrtc research based on 464 records obtained from the Scopus data base and coverage of
the period from 2000 to 2025 was able to offer a robust understanding of the map in impulsive buying
research ﬁeld. The main bibliometric indicators computed from the Scopus database by using the
Biblioshiny application of the Bibliometrix R package are shown in Table 1. It gives a macro impression
on the dataset with the number of documents, the types of documents, the collaboration among the
authors, and the occurrence of keywords.
Page 6/29

Table 1
Main Information
Description Results
Key Information About Data  
Time Span 2000:2025
Sources (Journals, Books, etc.) 130
Documents 464
Average Number of Citations per Document 6.85
References 18,204
Types of Documents  
Article 375
Conference Paper 100
Book Chapter 28
Review 12
Content of Documents  
Plus Keywords (ID) 4,380
Keywords Used by Authors (DE) 2,145
Authors  
Single-Authored Document Authors 65
Multi-Authored Document Authors 738
Collaboration Among Authors  
Single-Authored Docs 48
Co-Authors per Document 3.72
International Co-authorships % 31.04%
3.1 Publication Growth and Citations Over Time
The temporal spread of publication indicates that over the years, there has been a steady, moderate
interest towards IB research from 2000 and onwards, but the spike in the last decade is quite noticeable.
The “Average Citations per Year” line graph (Fig. 1) shows the trend in the number of citations over time.
Early 2000s had better average cites per paper ranging from around 2003. But subsequently there was
“a stark decline” before some spikes in 2017 and in early 2020 and early 2022, perhaps associated with
Page 7/29

boosted interest in digital consumer behavior as a result of COVID-19 lockdowns. There is a slow drop
to 2024–2025, which may be attributed to the reference lag of younger publications.
3.2 Authors' Productivity
The study provided a time-based view of top producers in this ﬁeld in Fig. 2 “Authors’ Production Over
Time”. Authors like Badgaiyan A.J., Prashar S., Parsad C., Luo X. are consistent with their publications
for several years. The size of a blue bubble represents TC per year and productive history is indicated by
line length. It is also noteworthy that Cheah J.H. shows up as a fairly substantial contributor in recent
times (2023–2024) in terms of citation rates, and an average number of lower, but highly cited papers.
These results are indicative of a mix of 'old' and innovative organizations shaping the trajectory of the
ﬁeld.
3.3 Co-authorship Networks
"Authors Collaboration Network" (Fig. 3) shows co-authorship groups and highlights scholarly
relationships in the impulsive buying literature. At the second step, nodes (e.g., those of Luo X, Prashar S,
and Lim X.J) with a larger size have higher productivity and collaborative centrality. The strength of co-
authors collaboration (ties) is depicted by the width of the connecting lines (edges). There were authors
like Vijay T.S., Cheah J.H and etc., who could be seen as gatekeeping authors, connecting different
author clusters and then disseminating information across institutional or geographic boundaries. This
summary underscores the interdisciplinary, intercultural approach of impulsive buying research.
3.4 Institutional Collaboration
Figure 4 “Aﬃliations Collaboration Network” present the collaboration network in the macro scale, where
collaboration among different institution can be seen. Universiti Putra Malaysia, UCSI University,
Shenzhen University and University of East Anglia appear as leading nodes. The close collaborations
between Asian universities, especially Malaysian and Chinese ones, suggest that Southeast Asia has an
increasing critical mass of research output. This visual density of connections also suggests the cross-
continental relationships with institutions such as the University of Portsmouth and Sun Yat-Sen
University, indicating impulsive buying research as a global interdisciplinary involving marketing,
psychology, and information systems.
3.5 Most Relevant Authors and Aﬃliations
The top contributors in the area of impulsive buying are plotted in Fig. 5 “Most Relevant Authors”. The
following authors (Luo X, Parsad C, and Prashar S) appeared frequently with ﬁve articles, and Badgaiyan
A.J., Cheah J-H, and Japutra A with the same frequency of 4 articles each. They are not only leading
pioneers in the ﬁeld but also key fountainheads whose research underpins much of what is known to
date about impulsive buying. Their work is largely concentrated in digital consumption hedonic
motivation and behavioral decision making, positioning them as major inﬂuencers in theoretical and
applied research.
Page 8/29

Figure 6, “Most Relevant Aﬃliations,” presents the institutional output according to their number of
articles. Leading the way is Universiti Putra Malaysia with 17 articles published, testifying to its broaders
standing in consumer behavior literature but more particularly in the context of South-East Asia. These
are augmented by Universitas Indonesia (15), Kyung Hee University (14) and UCSI University (14). The
high representation of Malaysian and Indonesian institutions indicates a regional focus for research
which may be due to the fast pace of digitalisation and expansion of consumer markets in these
economies.
3.6 Country Contributions and Global Collaboration
Patterns
In Fig. 7, the research results of impulsive buying display a high level of international collaboration. China
occupies the core position, the number of co-authorship links to which is largest, between Malaysia,
Indonesia, USA and Pakistan. The thick web of lines suggests active bilateral and multilateral research
collaboration, especially among Asian countries. Partnership provide indication of common emphasis on
digital consumer behaviour, online marketplaces and marketing strategies for economic development.
This is further exempliﬁed in Fig. 8 (Country Production Over Time) where the longitudinal increase of
country publication output can be observed. China, especially after 2015, as well as India, Indonesia,
Malaysia, and the USA, expressed the steepest growth curve. The trending point for the number of
publications in China shifted to 2012, and the growth could be attributed to funding and policy support
in China in the ﬁeld of digital commerce analytics. Meanwhile, nations such as Malaysia and Indonesia
have been ramping up steadily as e-commerce and smartphone usage spreads through their
populations.
3.7 Conceptual Structure and Emerging Research Themes
A deep analysis of conceptual clusters was conducted using two keyword co-occurrence maps: author
keywords and Keywords Plus.
In the “Author Keywords Co–occurrence Network” of Fig. 9, “impulsive buying” represents the central
node, strongly connected to related issues such as “purchase intention”, “consumer psychology”,
“hedonic motivation” and “online shopping”. Notable links also include “self-control”, “COVID-19”, “trust”,
and “social commerce”. This relationship suggests the psychological foundations behind impulsive
shopping and its environmental triggers, especially in digital environments. The large number of
references to COVID-19 suggests the development of literature on the pandemic-related changes in
consumer behavior, and particularly on the Internet.
Corroborating with this, Fig. 10 “Keywords Plus Co-occurrence Network” indicates broader thematic
associations in the ﬁeld. There are several clear clusters for “consumption behavior”, “electronic
commerce”, “marketing” and “consumer behavior”. The keywords represent interdisciplinary linkage to
marketing, retail science, behavioral economics, and technology. “Empirical analysis”, “Adolescents”,
“Shopping activity”, and “Decision-making” frequently appeared, indicating interest in demographic
Page 9/29

differences and implications of impulsive buying. Together of these networks illustrate a research ﬁeld
which is settling down into a mix of theoretical and experimental investigation of data.
3.8 Trend Topics and Term Frequency
Understanding the intellectual history of research on impulse purchasing is an important step in
identifying the intellectual trajectory in which key terms have been used over time. The “Trend Topics”
(Fig. 11) depicts the appearance and lasting of the terms that frequently appear over time, as well as
their appearance on timeline in the literature.
The most featured or persistent ones, such as ‘impulse buying’, ‘consumer behaviour’, and ‘materialism’,
have also remained frequently used over the years, particularly from 2015 onwards. New words, such
as “social commerce”, “perceived usefulness”, “urge to buy impulsively”, “COVID-19”, and “inﬂuencer
marketing” capture this more focused change toward digital behavioral inﬂuences and their connection
to pandemics around 2020. More recent terms such as “generation Z” and “ﬂow experience” emerge with
an augmented focus on generation- and experience-related dimensions in impulsive buying.
The size of each bubble on the timeline corresponds to the term frequency. The most cited keywords
are "hedonic motivation", "e- commerce", "purchase intention" and "online shopping", demonstrating
these words are placed at the core of the debate. This emerging terminology reﬂects the shift from
studying consumption behavior in general to specialized psychological and technology-mediated
concepts.
3.9 Conceptual Hotspots: Word Cloud Analysis
To summarize keyword prominence, a word cloud (Fig. 12) was produced based on all author keywords
in the dataset. The higher number is that the term has occurred in the corpus of literature. The top
themes are “impulse buying”, “impulsive buying behaviour”, “consumer behaviour”, “compulsive buying”
and “materialism”. These results signal that there is an emerging interest in the overlap between the
categories of planned, unplanned and compulsive consumption. Finally, the dominance of “e-commerce”,
“social media”, and “inﬂuencer marketing” suggests technological channels are the key issue in
evaluating emerging forms of impulsivity.
Variables such as “self-control”, “hedonic value”, “ﬂow experience”, and “positive affect” add emphasis
to the continued highlighting of emotional and psychological antecedents. As an aggregate, the word
cloud is a thematic ﬁngerprint of the ﬁeld, showcasing age-old constructs, and fresh emerging themes.
3.10 Most Relevant Countries and International
Contributions
Figure13 “Corresponding Author's Countries” displays top depositing countries with regard to article
contribution. First by quantity, in China, then by India, Indonesia, USA, and Malaysia. Figure also
differentiates between SCP (Single Country Publications) and MCP (Multiple Country Publications).
Page 10/29

Dominant in total production, China exhibits a nice balance between SCP and MCP, which is a sign of its
strong involvement in international cooperative research.
The USA and the UK, with fewer overall articles, have a high proportion of MCPs, which indicates a
strong focus on international collaborations. In contrast, larger proportions of single-country studies are
observed for nations like India and Malaysia, indicating the recent development of national-level research
centers that have potential to be engaged more in international cooperation. This global spread is a
testimony to the fact that impulsive buying is not just any longer a Western-dominated research ﬁeld,
but an area of global signiﬁcance, particularly in the emerging digital markets of Asia.
3.11 Most Relevant Sources and Publishing Trends
Figure 14 displays the source productivity proﬁling: “Most Relevant Sources”. The Journal of Retailing
and Consumer Services is the most prominent outlet with 19 articles, alongside Sustainability
(Switzerland) and Journal of Business Research with 8 articles, and Young Consumers- with 8 articles.
Other signiﬁcant publications are Asia Paciﬁc Journal of Marketing and Logistics, Cogent Business and
Management, and International Journal of Retail and Distribution Management.
This distribution slices to the theme of impulsive purchasing across several ﬁelds of academia such as
retail management, sustainability, consumer psychology, digital commerce. The substantial number of
Sustainable references found point out an increasingly interconnectedness of in-pulse buying with the
Sustainable or Ethical purchase a theme notably salient in the context of the post-pandemic, new-
normal where consumer awareness is changing.
Figure 15, Sources’ Production Over Time, shows the publications that have appeared cumulatively at
and above some of the highest-ranked journals. The trend map indicates that after 2018 there is clear
increase of publications, and three journals (Journal of Retailing and Consumer Services, Sustainability
and Journal of Business Research) have exponential rise curves after 2020. This trend is consistent with
worldwide disturbances of consumption style and the explosive development of online consumerism in
the context of COVID-19.
3.12 Country Collaboration Network (VOSviewer Analysis)
The country-level collaboration network is displayed in Fig. 16 based on VOSviewer. Its network
indicators reveal China, India, Malaysia, and the United Kingdom as key producers, with widely stretched 
international research collaboration. These nations serve as important hubs linked by various co-
authored papers, demonstrating their collaborative efforts in developing knowledge on impulsive
buying.
China and India exhibit the most cooperation not only within Asia, but also with Europe as well, and their
joint publications with Pakistan, Saudi Arabia, Malaysia and the United Kingdom can be observed
frequently. In contrast, the U.S and South Korea exhibit partnerships not only with Vietnam but also
Page 11/29

Indonesia and Taiwan, demonstrating increasing scholarly exchanges between developed and
emerging economies.
The network clusters correspond to speciﬁc regional groupings of collaboration. One group zeroes in on
relations between China, India, Pakistan and Saudi Arabia. A second cluster focuses on UK-German-
Lithuanian collaboration, frequently via multidisciplinary European opportunities. There are some more
clusters indicating the emerging academic collaboration activities between institutions in Southeast
Asia (Indonesia, Vietnam and Taiwan). This map highlights this trend of internationalization in the 
impulsive buying research based on strong regional collaborations and growing cross-border networks.
3.13 Institutional Collaboration Network
The partnership network among the institutions is shown in Fig. 17, which illustrates the interconnection
between the universities according to common scholarly output. Important stakeholders in this area
include COMSATS University Islamabad, ITM University (India), Coventry University (UK), Chang Jung
University (Taiwan) and Fore School of Management (India).
Institutional clusters refer to the regional concentration of collaboration and thematic focus. One group
comprises tourism and management-oriented institutions, among them the Fore School of Management
and College of Hotel and Tourism Management. The other category consists of technology-focused
collaborations, such as those between Taibah University and British institutions. A third cluster is based
on the active interaction between South Asian business and hospitality schools, working together on
areas involving consumer behavior in tourism, digital marketing, and retail management. These trends
reﬂect the increasing cross-disciplinary and regional focus of impulsive buying research, especially in
emerging disciplines (e.g., e-commerce, smart consumption, and consumer tourism).
3.14 Author Collaboration Network
Figure 18 depicts the authorship collaboration network, showing lead authors and co-authorship
relationships among academics. Main authors such as Ooi Keng-Boon, Cheah Jun-Hwa, Luo Xi, Lim Xin-
Jean, and Dwivedi Yogesh K. are also well established in the intellectual pillar of some research clusters
in Malaysia, China, and the United Kingdom.
Ooi Keng-Boon and his Malaysian partners to thank for their studies on online impulse buying, e-
commerce adoption and digital system behavior. A research cluster, led by Cheah Jun-Hwa, Luo Xi & Lim
Xin-Jean, emphasizes on marketing communication tactics, hedonic motivation and customer
psychology, depicting high cross-border collaborations between Chinese and Malaysian academicians. A
group includes Garry Wei-Han Tan, Cham Tat-Huei and Aw Eugene Cheng-Xi who focus on social media
inﬂuence, materialism and online trust.
The form of this network embodies coherent communities of authors with common interests and
frequent cooperation. These co-authorship bonds reveal the existence of specialized research groups
that have made an important contribution to the development and academic impact of the discipline.
Page 12/29

4. Discussion
There are various ﬁndings and implications of this bibliometric and network analysis of im pulse buying
literature over the last 25 years. There has been a particularly rapid increase in scientiﬁc output on this
topic in the past decade, and a remarkable spike after 2018, paralleling in part the development of
digitized economy, online social networking and inﬂuencer-based marketing. This growth highlights the
changing relevance of impulse buying as a psychological construct as well as a marketing-driven
concept in the area of consumer studies.
There was a total of 464 documents identiﬁed in the present study indexed in the Scopus database and
the most frequently encountered type of documents were journal articles. More than 80% of the papers
were the result of cooperation between two or more researchers; thus a high level of research
collaboration prevailed. The strong international and inter-institutional networks, plotted in the
collaboration maps, further support the idea that impulsive buying is a universal research issue that
crosses ﬁelds of psychology, technology, and marketing.
Both the three-ﬁeld Sankey diagram and the authorship visualizations also highlight the importance of
speciﬁc key actors in the ﬁeld. The study by Luo X, Parsad C and Prashar S is found to be the most
productive, and their research has been greatly related to topics such as materialism, consumer
behavior, and social commerce. These researchers largely come from universities in Malaysia, China and
India, again underscoring the growing importance of Asia in consumer research. The production
schedule demonstrates that these authors have really only gathered pace in the past few years,
reﬂecting the dynamic and developing nature of the ﬁeld.
Keyword clustering identiﬁed ﬁve majors theme clusters. The ﬁrst cluster mainly nodes around the
central term “impulse buying” is a linked with hedonicc motivattion, online shopping and purchase
intention, and is focusing on the emotional and affective drivers of impulsive purchasing behaviour.
Another important group is self-regulation, social commerce and materialism, which indicates a
continued curiosity on the effect of impulsiveness in relation to inner control and external digital factors.
The keywords Generation Z, COVID-19, and inﬂuencer marketing in recent publications evidence a
generational and contextual broadening of research views.
The conceptual structure map constructed by keyword co-occurrence and thematic evolution gives it a
knowledge frame that shows how the domain evolves at a certain time. Hedonic shopping value and
consumer psychology are early themes and as additional research emerges it extends into trust in e-
commerce, social media inﬂuence, and technology acceptance models. These ﬁndings correspond with
current trends toward complexity and interdisciplinarity in contemporary consumer behavior research.
Scientiﬁc mapping by VOSviewer showed international partnership was active. Nations such as China, 
India, Malaysia, and the UK were identiﬁed as key players in the global research network. China’s strong
cooperation with Malaysia and Pakistan, domestically and internationally, further solidify its leading role
in digital commerce research. The United States and South Korea also had major bilateral academic
Page 13/29

connections, which were explained by shared attention to technology platforms and behavioral
analytics.
Universiti Putra Malaysia, UCSI University, Shenzhen University, and Kyung Hee University were the most
active institutions with signiﬁcant contribution in both theoretical and practical research. Institutional
collaboration dynamics, as depicted in the VOSviewer maps, show dense, polycentric collaboration
networks, especially within schools of business, tourism, and information technology.
The journal spectrum also mirrors the interdisciplinary nature of the subject. The Journal of Retailing
and Consumer Services, Sustainability, and The Journal of Business Research were the most inﬂuential
journals. A focus on the underlying topics reveals that Sustainability appears as a key source among the
top sources, and backwards, this trend indicates an increased overlap between impulsive buying
behaviour and the dichotomies between ethical consumerism and sustainable marketing or post-
pandemic consumer resilience.
This trajectory from materialism and hedonic value to the latest terms, such as inﬂuencer marketing, 
social media, and COVID-19, captures changing social, technological, and economic dynamics. This
semantic shift also reﬂects that scholars are interested not only in what causes impulsive buying, but
also in properties of environments and technologies that enable it.
The results of this bibliometric study provide some important implications. The ﬁrst reason is that the
ﬁeld is still growing and the high impact authors and institutes, are contributing heavily to the overall
output. Secondly, there is clearly some thematic growth in terms of digital technology, triggers of
emotion, and marketing approaches under research. Internationality also seems to be on the rise, but
again there are still opportunities for more cross-border and cross-disciplinary collaboration.
This paper offers a thorough view of the intellectual, geographical, and thematic orbits of research on
impulsive buying in the last 25 years. It also lays the groundwork for future research directions,
highlighting underexplored clusters, as well as key contributors and methodological trends. In contrast
to the previous systematic reviews, this bibliometric review provides a more comprehensive, data-driven
overview of the range and development trajectory and hot spots of the ﬁeld. As the settings of
consumer behaviour increasingly change with technology, further research should increasingly focus on
hybrid models that combine behavourial psychology, algorithmic targeting and ethical reﬂections.
5. Conclusions
This research provides a wide bibliometric analysis of impulsive buying behavior global output from
2000 to 2025 with records indexed in Scopus. Using the Biblioshiny tool of Bibliometrix package in R
and VOSviewer, the key contributors, journals, organization, nations, keywords and latest research trends
of the study were discovered. Through the analysis of 464 papers, the study found a clear trend of
growing interest, with pronounced increase over the last decade.
Page 14/29

Journal of Retailing and Consumer Services, Sustainability (Switzerland), and Journal of Business
Research were the three most proliﬁc sources. The authors with the most impact were Luo X, Parsad C,
and Prashar S, and institutions like Universiti Putra Malaysia and Universitas Indonesia were among the
highest in number of publications.  China was the top producing and collaborating nation followed by
India, Indonesia, the USA and Malaysia, acknowledging the presence of Asia as the major player in this
domain of research.
In the keyword analysis, " impulse buying "and "impulsive buying behavior" were identiﬁed as the most
frequently used terms. Among visualizations, themes still showed around hedonic motivation, purchase
intention, e-commerce, and materialism, signifying a behavioral or technology-driven focus consisted in
the clusters. In terms of networking within the ﬁeld and the evolution of content, strong cross-national
collaboration networks as well as growing interdisciplinarity and relevance for society is reﬂected.
This bibliometric analysis provides a systematic framework of knowledge map for researchers,
institutions and policymakers to comprehend the evolution and hot spots in impulsive buying
researches. By compiling a quarter century of data, it also exposes new domains for investigation, and
the increasing interpenetration of digital commerce and behavioural sciences within consumer research.
6. Future Directions
Future studies may investigate sophisticated bibliometric and visualization tools such as machine
learning based clustering and predictive map of topic trajectories. Methods like topic dominance
modeling, semantic analysis, and temporal keyword evolution prediction have the potential to increase
the understanding of research priority drift and subﬁeld emergence. While the study only used the
Scopus database in this study due to a comprehensive coverage of citation context, the upcoming study
should also apply some comparative datasets from WoS, Dimensions, PUBMED, and GS to verify these
ﬁndings across different platforms and increase the results robustness.
The creation of interactive bibliometric dashboards or advanced visual analytics tools based on the use
of AI may permit ﬁner exploration of relationships between authors, cooperation between institutions
and interdisciplinary overlap over time. Such utilities would help scholars to customize searches of the
literature, identify gaps in citation, and predict inﬂuential areas.
Future studies could deal with under-researched areas, such as cross-cultural comparisons about
impulsivity, the neuroeconomic determinants of purchase decisions, or the inﬂuence of AI-based
recommendation systems on impulse buying. With the changing landscape of digital platforms and
shifting consumer habits, privacy ethics, algorithmic bias, and issues regarding sustainability will
increasingly need to be included in the research framework. Future work can provide a more nuanced
perspective on developing dynamics of impulsive buying when complemented with increased
methodological sophistication and more extensive coverage of the datasets, and when it is integrated
with new consumer technologies.
Page 15/29

Declarations
Competing Interests
The authors have no relevant ﬁnancial or non-ﬁnancial interests to disclose.
Ethics Approval
Not applicable. This study is based on bibliometric analysis of published literature and does not involve
human participants, human data, or animals.
Consent to Participate
Not applicable.
Consent to Publish
Not applicable.
Funding
No funds, grants, or other support were received.
Author Contribution
Author ContributionsX.Z.Q.: Conceptualization, data collection, formal analysis, visualization, and original
draft preparation.H.R.C.: Supervision and critical revision of the manuscript.M.S.H.: Supervision and
review of the manuscript.All authors have read and approved the ﬁnal manuscript.
Data Availability
The dataset supporting the ﬁndings of this study is provided as a supplementary ﬁle submitted with the
manuscript for peer review. The shared material includes the raw bibliographic data exported from the
Scopus database in CSV format, which contains the metadata used for the bibliometric analysis. This
dataset is made available to ensure transparency and allow veriﬁcation of the study’s ﬁndings.
References
1. Agrawal P (2025) Artiﬁcial Intelligence Research (2001–2022): A Bibliometric Journey through
Trends and Patterns. J Data Sci Informetrics Cit Stud 4(1):65–77
Page 16/29

2. Barauskaitė B (2025) The impact of scarcity, discounts, free shipping, personalized recommendations,
social proof, emotional storytelling, and beneﬁts of products and services on social media
advertisements on impulsive purchasing Vilniaus universitetas.]
3. Caputo A, Kargina M (2022) A user-friendly method to merge Scopus and Web of Science data
during bibliometric analysis. J Mark Analytics 10(1):82–88
4. Chandrasekhar K, Das S, Gupta N, Jena SK (2024) Comparative analysis of impulse buying
behaviour across retail channels: a study of physical stores, e-commerce websites and mobile
shopping apps. Economic Affairs 69(2):1109–1120
5. Dahish Z, Miah SJ (2022) A bibliometric analysis to explore sentiment analysis in the domain of
social media research
6. Dalal G, Vyas P, Chugh P (2023) On-the-Spot Decision Making: A Bibliometric Investigation into
Impulse Buying Research Progression, Network Structures and Emerging Trends. IPE J Manage
13(2):49–72
7. Gonzalez E (2021) Value Consciousness, Enjoyment of Mobile Coupons, and Impulse Buying
Tendency. Effects on Mobile Coupon Redemption Intentions. Global J Manage Mark 5(1):1–31
8. Gulfraz MB, Sufyan M, Mustak M, Salminen J, Srivastava DK (2022) Understanding the impact of
online customers’ shopping experience on online impulsive buying: A study on two leading E-
commerce platforms. J Retailing Consumer Serv 68:103000
9. Kaur K, Sharma T (2024) Impulse buying in the digital age: An exploration using systematic literature
review approach. J Consumer Behav 23(5):2553–2584
10. Pautrat M, Le Guen A, Barrault S, Ribadier A, Ballon N, Lebeau J-P, Brunault P (2022) Impulsivity as a
risk factor for addictive disorder severity during the COVID-19 lockdown: results from a mixed
quantitative and qualitative study. Int J Environ Res Public Health 20(1):705
11. Pessin VZ, Yamane LH, Siman RR (2022) Smart bibliometrics: an integrated method of science
mapping and bibliometric analysis. Scientometrics 127(6):3695–3718
12. Rajib RI, Roy P (2023) Inﬂuence of social media on consumer buying behavior and decision making:
insights from surveys and a case. study of Flash Digital Agency in Bangladesh
13. Shi J, Duan Y (2024) Knowledge-map and research trends of circulating tumor cells in breast cancer:
a scientometric analysis. Discover Oncol 15(1):506
14. Singh VK, Singh P, Karmakar M, Leta J, Mayr P (2021) The journal coverage of Web of Science,
Scopus and Dimensions: A comparative analysis. Scientometrics 126:5113–5142
15. Thomas A, Gupta V (2022) Tacit knowledge in organizations: bibliometrics and a framework-based
systematic review of antecedents, outcomes, theories, methods and future directions. J Knowl
Manage 26(4):1014–1041
16. Yan L, Zhiping W (2023) Mapping the literature on academic publishing: A bibliometric analysis on
WOS. SAGE Open 13(1):21582440231158562
Figures
Page 17/29

Figure 1
Publication Growth and Citations Over Time
Figure 2
Authors' Productivity
Page 18/29

Figure 3
Co-authorship Networks
Page 19/29

Figure 4
Aﬃliations Collaboration Network
Page 20/29

Figure 5
Most Relevant Authors
Figure 6
Most Relevant Aﬃliations
Page 21/29

Figure 7
Country Contributions
Page 22/29

Figure 8
Country Production Over Time
Figure 9
Author Keywords Co–occurrence Network
Page 23/29

Figure 10
Keywords Plus Co-occurrence Network
Page 24/29

Figure 11
Trend Topics
Figure 12
Word Cloud Analysis
Page 25/29

Figure 13
Corresponding Author's Countries
Figure 14
Most Relevant Sources
Page 26/29

Figure 15
Sources’ Production Over Time
Page 27/29

Figure 16
Country Collaboration Network
Figure 17
Institutional Collaboration Network
Page 28/29

Figure 18
Author Collaboration Network
Supplementary Files
This is a list of supplementary ﬁles associated with this preprint. Click to download.
scopus9DATAforBB.csv
Page 29/29
