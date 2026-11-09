---
title: 'Mapping the evolution of digital business research during COVID-19: a bibliometric analysis'
url: https://doi.org/10.1007/s43546-026-01315-1
category: survey
subcategory: review
date: 2026-08
venue: SN Business & Economics
authors:
- Khaled Nawaser
- Hassan Hessari
- Hoda Mohsenifard
source: openalex-oa
pdf_url: https://link.springer.com/content/pdf/10.1007/s43546-026-01315-1.pdf
pages: 30
chars: 86769
fetched_at: '2026-11-08T18:53:18+00:00'
kb_version: 1
---

# Mapping the evolution of digital business research during COVID-19: a bibliometric analysis

ORIGINAL ARTICLE
SN Business & Economics (2026) 6:339
https://doi.org/10.1007/s43546-026-01315-1
Extended author information available on the last page of the article
Received: 24 September 2025 / Accepted: 27 July 2026 / Published online: 26 August 2026
© The Author(s) 2026
Mapping the evolution of digital business research during
COVID-19: a bibliometric analysis
Khaled Nawaser1 · Hassan Hessari2  · Hoda Mohsenifard3 · Azin Yazdi4 ·
Babak Ghahremannasab5
Abstract
The COVID-19 pandemic served as a profound catalyst for digital transformation,
radically reshaping business models, consumer behavior, and organizational strate -
gies globally. This study employs a bibliometric approach, analyzing 527 publica -
tions from the Scopus database to examine how digital business research evolved
during this period. Various tools including R software, VOS viewer software, and
Publish or Perish are utilized. The aim is to portray the knowledge map, explore the
publication years, identify the top authors and their co-occurrence, reliable docu -
ments, institutions, subjects, research hotspots, and pioneering countries and uni -
versities in the study of digital business. Results indicate consistent annual growth
in publication output, accompanied by a decline in average citations per article.
This pattern may reflect the “dilution effect” commonly observed in rapidly ex -
panding fields; however, the absence of a pre-pandemic baseline warrants cautious
interpretation of this trend. International collaboration proved robust, with strong
co-authorship networks led by the United States and China. Thematic analysis iden -
tified core research clusters around e-commerce, consumer behavior, supply chain
resilience, and digital marketing, underpinned by highly cited studies on pandemic-
driven behavioral shifts and technological adaptation. Co-citation analysis revealed
four foundational clusters: direct economic impacts, statistical methodologies, digi -
tal transformation, and policy responses. Despite these advances, significant re -
search gaps remain, including the long-term implications of digital transformation
for business models, the use of advanced analytical methods to study crisis-driven
consumer behavior, and comparative policy analyses extending beyond the Chinese
context. This review maps the intellectual structure of digital commerce during a
global crisis and identifies opportunities for future research to enhance resilience
and adaptability in digital ecosystems.
Keywords Digital transformation · Digital business · Consumer behavior ·
Bibliometric analysis · COVID-19 pandemic

1 3
339 Page 2 of 30
SN Business & Economics (2026) 6:339
Introduction
The emergence of the COVID-19 pandemic has caused a dramatic shift in the digital
business research landscape (Behie et al. 2023; Hussain 2021). Digital transforma -
tion is the process of integrating digital technologies into all aspects of a business,
which is bound to change the way business is done and value is delivered to custom-
ers (Bonnet and Westerman 2021; Nankoomar and Quilling 2023). This is a change
period marked by the accelerated digital transformation, which redefined not just the
operational model but also the strategic orientation of the companies (Hanelt et al.
2021; Burlea-Schiopoiu et al. 2023).
It has become increasingly clear that the pandemic has led to significant changes
in consumer behaviors and market moves (Guthrie et al. 2021). Global e-commerce
sales, one of the trends driven by the demand for contact-free transactions and remote
shopping, experienced 27.6% growth in 2020 Kim (2020) These remarkable growth
figures are indicative of a broader trend towards online in all corners of the economy,
highlighting the increasing pressure on companies to transition to digital commerce
models. Indeed, one clear manifestation of this trend can be seen in the human
service industries like hospitality and tourism, where businesses have increasingly
implemented the adoption of digital technologies for their customer experiences and
engagement due to constraints in physical gatherings (Bolton et al. 2018; Cheng et
al. 2023). Another evidence of such a shift is the fast growth of digital innovation in
marketing, as companies have used data analytics and social media to form new con-
nections with customers (Mariani and Nambisan 2021; Raišys and Raišienė 2023).
The COVID-19 crisis has accelerated the need for businesses to pivot their com -
munication and engagement plans (Sanasi and Ghezzi 2024). Enterprises in all sectors
have leveraged digital technologies to keep running through lockdowns and social
distancing rules (Amankwah-Amoah et al. 2021). Healthcare is one such sector that
observed remarkable innovations in telemedicine and digital health technologies,
touching upon changes in patient-to-patient interactions and service delivery models
during the pandemic (Abdolkhani et al. 2022; Gleiss et al. 2021). There was even
increased preference for online banking and financing products as some of the con -
sumers purportedly became inclined towards digital platforms for financial transac -
tions (Zheng et al. 2024; Gunathilaka and Rupasingha 2022).
Some of the recent trends indicate a phenomenal growth in e-commerce and
online shopping trends, especially from users who have used conventional shopping
systems earlier (Chawla and Kumar 2022). A research study indicated that 67% of
online consumers had increased their scope of online browsing during the pandemic,
indicating a radical change in their shopping behavior that may carry through after
the pandemic (Raihan 2024). As a result, companies that successfully incorporated
digital marketing in their operations did not just survive; they also restructured cus-
tomer relationships (Ahmad et al. 2024; Fatimah et al. 2021; Kim 2020). Companies
are paying more attention to digital marketing innovation in order to reach consum -
ers using personal content and improved online engagement devices (Kshetri et al.
2024; Raišys and Raišienė 2023).
This article provides an in-depth examination of the evolution of digital business
research under COVID-19 by employing bibliometric. The study will be centered

1 3
Page 3 of 30 339
SN Business & Economics (2026) 6:339
on the year 2020–2024, and it aims to examine where digital commerce and the
effects of the pandemic on consumer behavior and the market landscape converge.
The research aims to integrate previous works to obtain a perspective on how digital
transformation strategies have helped organizations cope with the day-after difficul -
ties brought on by the pandemic. While still early in the trajectory of digital business,
grasping these dynamics is essential for informing both research agendas and mana-
gerial practices in this field.
The COVID-19 pandemic-induced changes in motion offer an important field
of study for both scholars and implementers. The imperative for organizations to
engage in digital transformation to address the changing expectations of consumers
serves as a powerful context for this study, which highlights the critical importance
of continuing investigation and adjustment in the domain of digital business research
(Azzahra et al. 2022).
The study on digital business research evolution during the COVID-19 pandemic
is of great interest to researchers in academia and industry. The distinctive contribu-
tion of this study to research in this field is the treatment of digital transformation
literature in a bibliometric framework to explore the dynamics of the field in an age
of turbulence. This methodological triangulation contributes to theory development
while closing the gap in research for a nuanced understanding of digital business in a
global crisis (Khoshroo and Talari 2023).
An important gap in the current research is the paucity of in-depth examination
regarding the long-term implications of COVID-19 on business models and digi -
tal commerce. Although many studies have already mentioned some cases of com-
panies` strategies for survival and growth during the pandemic, scarce are systematic
reviews that can aggregate these results to a wider panorama about the trends of digi-
tal transformational and research implications (Almasri et al. 2021; Rahawarin et al.
2023). Finally, the purpose of this study is to investigate the development of digital
business research in the era of COVID-19. The study seeks to explore the large-scale
changes in business models, especially digital transformation in direct response to
disruptions caused by the pandemic. This paper contributes to the literature through
the application of bibliometric analysis and content analysis to identify emerging
trends and major research themes in the area of digital business during and post-
pandemic. It will do so by systematically mapping out how all types of organizations
shifted their digital strategies to deal with unexpected challenges and how this shift
in turn transformed business and consumer behavior.
To accomplish this, the following specific research questions will be addressed in
the study:
1. How have digital business studies changed during COVID-19?
2. What are the long-term effects of COVID-19 on digital business strategies?
3. How have companies changed their approach to digital transformation as a result
of the pandemic?
The remainder of the paper is organized as follows. In the second section, the
research method and its mechanism are described. In the third part, according to the
purpose of the research, performance results, network, in addition, to content regions

1 3
339 Page 4 of 30
SN Business & Economics (2026) 6:339
are introduced. A discussion of the results is presented in the fourth section. The fifth
and final section of the article: Research limitations, and areas for future research
are discussed.
Research methodology
Given the exponential growth of scientific knowledge across disciplines, systematic
approaches that enable the categorization of research outputs and the identification of
emerging trends have become increasingly important for scholars. Accordingly, this
study employs a systematic review approach using bibliometric analysis (Yuan et al.
2016; Yazdi et al. 2024a; Nawaser et al. 2024), which allows the examination of large
volumes of scientific data and facilitates the detection of evolutionary patterns and
emerging areas within a research field. Bibliometric techniques are generally divided
into two main categories: performance analysis and science mapping. Performance
analysis evaluates the contributions of research constituents such as authors, institu -
tions, countries, and journals, whereas science mapping explores the relationships
among research elements, including co-authorship, co-citation, and keyword co-
occurrence networks (Donthu et al. 2021; Nawaser et al. 2026; Yazdi et al. 2024b).
The present study incorporates both approaches to provide a comprehensive under -
standing of the intellectual structure and development of research on digital business
during the COVID-19 pandemic (Kokol 2023).
The Scopus database was selected as the source of data because it is one of the
largest curated abstract and citation databases of peer-reviewed literature, offering
extensive and balanced coverage across scientific disciplines, particularly in the
fields of business, management, and social sciences (Pranckutė 2021; Stahlschmidt
and Stephen 2020; Ball and Tunger 2006). In addition, its advanced analytical tools
and standardized bibliometric indicators enable systematic and reliable analyses,
and prior comparative studies have confirmed its broader disciplinary coverage and
analytical capabilities relative to the Web of Science database. Data collection was
conducted on April 30, 2024.
Following a preliminary review of the literature and identification of relevant
synonyms, keywords related to digital business and COVID-19 were determined,
and a Boolean search query was applied to titles, abstracts, and keywords in Sco -
pus. The search was limited to English-language publications within the subject area
of Business, Management, and Accounting. The initial search yielded 1,987 docu -
ments. In the preprocessing stage, Scopus refinement filters were applied according
to the criteria presented in Table 1; Fig. 1, resulting in 540 scientific documents.
This study focuses on publications addressing digital business during the COVID-19
pandemic indexed in Scopus between 2020 and 2024. The inclusion criteria were
peer-reviewed journal articles or conference papers written in English and relevant to
digital business and COVID-19 based on their titles, abstracts, and keywords. Non-
peer-reviewed documents, book chapters, grey literature, and studies not primarily
focused on digital business during the pandemic were excluded. In the final stage,
the titles and abstracts were manually reviewed to ensure relevance, and thirteen

1 3
Page 5 of 30 339
SN Business & Economics (2026) 6:339
documents were removed due to duplication or lack of relevance, resulting in a final
dataset of 527 articles for analysis.
Bibliometric analyses were conducted using R (Bibliometrix package, version
4.2) and VOSviewer (version 1.6.21). Bibliometrix was employed for performance
analysis, science mapping, descriptive statistics, and the generation of bibliometric
indicators and visualizations, as it enables comprehensive data processing, statistical
modeling, and the production of precise graphical outputs for bibliometric research
(Aria and Cuccurullo 2017). VOSviewer was used to construct and visualize biblio -
metric networks, including keyword co-occurrence, co-citation, and thematic cluster-
ing maps. The minimum occurrence threshold for keywords was set to five, and the
minimum co-citation threshold for references was set to ten. The clustering resolu -
tion parameter was fixed at 1.0, while default layout settings were applied unless
otherwise specified.
Data analysis and results
Table 2 provides information on digital commerce data from 2020–2024 concerning
COVID-19. These data have been gathered from 308 varying sources that consist of
527 documents and grows at a rate of 9.1% annually. The documents are not very
old and the average age of the source documents is 1. 86 years, and the average of
citations received by these scholars has been 8,362 praising their contribution in the
field. Moreover, the specificity of topics is also seen from 1, 152 Keywords Plus and
1, 762 Author’s Keywords. Under the authorship section, it was found out that a total
of 1483 authors have contributed to these documents while 70 authors accomplished
writing their documents by themselves. On average, there are 3 authors per a docu -
Attributes Set criteria
Search within results Title, Abstract, and Keywords
Timespan 2019–2024
Database Scopus
Search theme (“digital business" OR "online busi-
ness" OR "internet business" OR "vir-
tual business" OR "electronic
business" OR "e-commerce" OR "in-
ternet-based business" OR "web-based
business" OR "cyber busi-
ness" OR "web business" OR "digi-
tal enterprise" OR "digital
commerce" OR "home-based
business" OR "internet enter-
prise" OR "tech-driven business" OR "tech-
nology-based firm" OR "digital
industry" AND (“corona*" OR "covid”))
Document type Article+conference paper+Review
Source type Journal
Subject area Business, Management and Accounting
Language English
Table 1 Prime information re-
garding the research methodol-
ogy adopted
Source: Authors’ own
elaboration

1 3
339 Page 6 of 30
SN Business & Economics (2026) 6:339
ment. Recorded interactivity among researchers working in this field was at 01%,
which was relatively high. Additionally, 23. More than half of the documents have
international co-authors from different countries as evidenced by 53% international
co-authorship; this is a testimony to the fact that the COVID-19 digital commerce is
a global challenge. Last, the type of documents having access within this collection
can be classified as 418 journal articles 101 conference papers, and 8 revealed, which
highlight that researchers prefer publishing their works in scientific journals and pre-
senting them at conferences. The outcomes indicate that digital commerce during the
COVID-19 period can be regarded as an object of study and development of interest
for different branches of science and remains relevant.
Publications and citations
Figure 2 shows quantitative analysis of the published articles and citation for these
articles in the area of digital business and COVID-19 from 2020 to 2024. Strong
evidence of this is reflected in the chart below where the number of published articles
has steadily risen within this period, and the period between 2020 and 2023 mainly.
This reveals increased attention to this research sector and the necessity to expand the
knowledge of the effects of COVID-19 on digital sales. However, the average num -
Fig. 1 PRISMA flow diagram of the study selection process

1 3
Page 7 of 30 339
SN Business & Economics (2026) 6:339
    



     
    














 




Fig. 2 Distribution of documents and citations by year (2020–2024)

Description Results
MAIN INFORMATION ABOUT DATA
Timespan 2020:2024
Sources (Journals, Books, etc.) 308
Documents 527
Annual Growth Rate % 9.1
Document Average Age 1.86
Average citations per doc 8.362
References 26,772
DOCUMENT CONTENTS
Keywords Plus (ID) 1152
Author’s Keywords (DE) 1762
AUTHORS
Authors 1483
Authors of single-authored docs 70
AUTHORS COLLABORATION
Single-authored docs 74
Co-Authors per Doc 3.01
International co-authorships % 23.53
DOCUMENT TYPES
Article 418
Conference paper 101
Review 8
Table 2 COVID-19 and Digital
Business: A Comprehensive
Data Overview (2020–2024)
Source: Authors’ own
elaboration based on Scopus
data

1 3
339 Page 8 of 30
SN Business & Economics (2026) 6:339
ber of citations per article has been declining over the time which can be construed as
a sign of emergence of more and more articles and the scatter of attention.
Most-cited documents
The ten most-cited articles regarding digital business issues in the context of COVID-
19 are presented in Table 3. Each of them focuses on the effect of COVID-19 on
digital commerce and underlines that COVID-19 became a catalyst which triggered
unprecedented growth and changes of digital commerce. These articles demonstrate a
wide-ranging set of changes and improvements brought about by the pandemic, from
altered consumer behavior to the need to improve digital infrastructure and build
supply chain resilience.
The list leads with the article entitled “The Impact of COVID-19 on Consumers:
Preparing for Digital Sales,” which enjoys 251 citations. This article represents a
deep analysis of changing consumer behavior in the COVID-19 period, pointing out
how important digital preparedness is, together with the integration of new technolo-
gies, in satisfying emerging demand. The article entitled “Managing the Effective -
ness of E-commerce Platforms in a Pandemic,” which is from 2021 and has 176
Table 3 Top documents that received the most citations
Rank Auther Year Title Source title Citation
1 KIM RY 2020 The Impact of COVID-19 on Consum-
ers: Preparing for Digital Sales
IEEE Engineering Man-
agement Review
251
2 TRAN
LTT
2021 Managing the effectiveness of e-
commerce platforms in a pandemic
Journal of Retailing and
Consumer Services
189
3 GUTH-
RIE C
2021 Online consumer resilience during a
pandemic: An exploratory study of e-
commerce behavior before, during and
after a COVID-19 lockdown
Journal of Retailing and
Consumer Services
184
4 GU S 2021 Impact of the COVID-19 Pandemic on
Online Consumer Purchasing Behavior
Journal of Theoretical
and Applied Electronic
Commerce Research
133
5 MODG-
IL S
2022 Artificial intelligence for supply chain
resilience: learning from Covid-19
The International
Journal of Logistics
Management
132
6 SHEN
ZM
2023 Strengthening supply chain resilience
during COVID-19: A case study of
JD.com
Journal of operetions
management
123
7 BECK-
ERS J
2021 COVID-19 and retail: The catalyst for
e-commerce in Belgium?
Journal of Retailing and
Consumer Services
92
8 CLEM-
ENT
ADDO P
2021 Customer engagement and purchase
intention in live-streaming digital mar-
keting platforms
The Service Industries
Journal
88
9 MODG-
IL S
2022 Has Covid-19 accelerated opportunities
for digital entrepreneurship? An Indian
perspective
Technological Forecast-
ing and Social Change
85
10 LIN J 2020 How do agribusinesses thrive through
complexity? The pivotal role of e-
commerce capability and business agility
Decision Support
Systems
79
Source: Authors’ own elaboration based on Scopus data

1 3
Page 9 of 30 339
SN Business & Economics (2026) 6:339
citations, refers to challenges regarding the governance of e-commerce platforms
during the pandemic and the need for infrastructure improvement in pursuit of better
customer experience. This article will represent a basic contribution to improving
the performance of digital platforms. Guthrie C (2021), with 162 citations, examines
online consumer behavior across three periods: before, during, and after COVID-19
restrictions. The study reveals that consumers quickly adapted to online shopping,
with many of these changes likely to become permanent. Gu S (2021), with 147
citations, analyzes the pandemic’s impact on online consumer purchasing behavior,
highlighting the significant increase in online shopping and the shift in purchasing
patterns. The findings of this article have played a key role in research related to mar-
ket changes and consumer behavior.
Modgil S (2022) has been cited 132 times in an article discussing how AI is impor-
tant for strengthening supply chain resilience during the COVID-19 pandemic. It
is considered one of the helpful references for current studies on supply chain risk
management with advanced technologies. Correspondingly, Shen ZM (2023) looks
into how JD.com used AI and robotics to enhance supply chain resilience during the
pandemic, with 119 citations. The article provides good insight into how technology
influenced supply chains.
The article COVID-19 and retail: The catalyst for e-commerce in Belgium? “With
102 citations sits down with Based on its primary objective, this article concentrates
on dealing with regional issues and future consequences of the pandemic in the mar-
kets at large. With 98 citations “Customer Engagement and Purchase Intention in
Live-Streaming Digital Marketing Platforms” highlights the effect of live-streaming
marketing on customer perceptions and purchase behaviors. This unit of marketing
got quite popular in the time of COVID-19 and is accepted as a method to engage
with the customers better. The last two articles in this list with 88 and 81 cites respec-
tively, discusses prospect of digital entrepreneurship in India and how e commerce
capabilities influence success of horticultural ventures in dynamic environments
including the COVID 19 era. Such pieces of writing show that the pandemic saw
the advancement of entrepreneurial revolution with online businesses benefiting for
change.
 Most influential authors in digital commerce and COVID-19
Based on the data analysis (Table 4), DWIVEDI YK emerges as the most influential
researcher in this list, with 88 citations, reflecting the broad and significant impact
of their work within their research field. ALI I, with a g-index of 3 and a total of 17
citations, clearly indicates that several of their publications have attracted notable
attention and have been frequently cited. HOANG LN and GOGONEA R-M, with
high m-indices, have demonstrated their scientific productivity over a relatively short
period, showcasing their effective and sustained influence in their respective research
domains. In comparison, CASSANDRA C and ENI Y , with lower total citation
counts, exhibit comparatively less impact in this group, suggesting that their publica-
tions have received less attention and citation.

1 3
339 Page 10 of 30
SN Business & Economics (2026) 6:339
Most productive universities in digital commerce and COVID-19
From Table 5, it is clear that high-output universities, located in Asia, especially
Malaysia and Indonesia, have surprisingly active research culture and sufficient aca-
demic stature. Of course, Multimedia University, Universiti Putra Malaysia, and Uni-
versitas Negeri Jakarta are counted as the top-rated research institutions in the said
region as each contributed ten publications. These universities contribute to scientific
and technological advancement due to the vast concentration on applied and innova-
tive research. Tsinghua University of China and Inha University of South Korea also
demonstrate considerable international academic capability through their publication
volumes. Tsinghua University is noted for its expertise in technology and engineer -
ing, while the Inha University is well-recognized in areas of scientific research and
emerging technologies.
In Europe, universities like the Bucharest University of Economic Studies and
Babeș-Bolyai University boast high outputs that ensure their academic prominence in
Table 4 Top-10 authors’ production impact
Authors h_index g_index m_index TC NP PY_start
ABASOV A S 2 2 0.5 24 2 2021
ALI I 2 3 0.667 17 3 2022
BELOTSERKOVICH D 2 2 0.5 24 2 2021
CASSANDRA C 2 2 0.5 5 2 2021
DWIVEDI YK 2 2 0.667 88 2 2022
ENI Y 2 2 0.5 5 3 2021
GOGONEA R-M 2 2 0.667 33 2 2022
GUO Q 2 2 0.667 18 2 2022
HASSAN R 2 2 0.5 26 2 2021
HOANG LN 2 2 1 8 2 2023
Source: Authors’ own elaboration based on Scopus data
Rank Affiliation country Articles
1 MULTIMEDIA UNIVERSITY Malaysia 10
2 UNIVERSITAS NEGERI
JAKARTA
Indonesia 10
3 UNIVERSITI PUTRA MALAYSIA Malaysia 10
4 BUCHAREST UNIVERSITY OF
ECONOMIC STUDIES
Romania 9
5 UNIVERSITI TEKNOLOGI
MARA
Malaysia 8
6 BABEȘ-BOLYAI UNIVERSITY Romania 7
7 TSINGHUA UNIVERSITY china 7
8 INHA UNIVERSITY South
Korea
6
9 UNIVERSITI UTARA
MALAYSIA
Malaysia 6
10 V ASILE ALECSANDRI
UNIVERSITY
Romania 6
Table 5 Top-10 most productive
universities
Source: Authors’ own
elaboration based on Scopus
data

1 3
Page 11 of 30 339
SN Business & Economics (2026) 6:339
the continent by showing intense research output in various fields. More significantly,
these institutions have been regarded as leading centers of learning in economics and
humanities studies. Another remarkable case within Romania is Vasile Alecsandri
University, which has managed to develop six publications, reflecting impressive
research capacity.
This distribution and analysis reveal that scientific and research activities are
well-distributed globally, allowing each continent and country to contribute to the
advancement of global knowledge and address scientific and social challenges. It is
with such a vision of research contribution to global knowledge and addressing scien-
tific and social challenges that Asian and European universities are coming forward,
while such geographical diversity strengthens academic and cultural exchanges, with
more opportunities for international collaboration.
Most influential sources in digital commerce and COVID-19
The journal “Journal of Retailing and Consumer Services”, according to Table 6,
presents the biggest scientific impact about digital commerce and COVID-19, having
13 published articles and high values of the h-index and g-index, which demonstrates
the biggest impact with 668 citations. It has gained this prominence because it pub -
lishes rigorous and impactful research on digital commerce and consumer services
during the pandemic. In comparison, “Journal of Theoretical and Applied Electronic
Commerce Research” has a total of 18 published works with an impressive g-index,
which has a significantly strong impact in the field of electronic commerce. However,
its citation counts of 300 is lower compared to the citation count of the top journal
Table 6 Metrics on the Top-10 Production Sources
Journal h_index g_index m_index TC NP PY_start
JOURNAL OF RETAILING AND CON-
SUMER SERVICES
9 13 2.25 668 13 2021
JOURNAL OF THEORETICAL AND
APPLIED ELECTRONIC COMMERCE
RESEARCH
7 17 1.75 300 18 2021
INTERNATIONAL JOURNAL OF LO-
GISTICS MANAGEMENT
4 5 1.333 187 5 2022
JOURNAL OF RISK AND FINANCIAL
MANAGEMENT
4 5 1 26 6 2021
TECHNOLOGICAL FORECASTING
AND SOCIAL CHANGE
4 6 1.333 148 6 2022
FORUM SCIENTIAE OECONOMIA 3 3 0.75 42 3 2021
IEEE TRANSACTIONS ON ENGINEER-
ING MANAGEMENT
3 4 0.75 23 4 2021
INTERNATIONAL JOURNAL OF PRO-
DUCTION RESEARCH
3 5 1 51 5 2022
JOURNAL OF ASIAN FINANCE, ECO-
NOMICS AND BUSINESS
3 3 0.6 51 3 2020
JOURNAL OF FINANCIAL SERVICES
MARKETING
3 3 1.5 40 3 2023
Source: Authors’ own elaboration based on Scopus data

1 3
339 Page 12 of 30
SN Business & Economics (2026) 6:339
and probably reflects the specific focus of the journal or its comparative recent estab-
lishment in digital commerce or COVID-19 studies.
Other journals, such as the “International Journal of Logistics Management”
and “Technological Forecasting and Social Change”, which contain 5 and 6 articles
respectively, have lower h-index and g-index indicators, which has resulted in less
impact within the disciplines of logistics and technology forecasting concerning
digital commerce and the pandemic. On the other hand, with fewer publications,
the “Forum Scientiae Oeconomia” and “IEEE Transactions on Engineering Manage-
ment” have worse scientific indices and lower impact according to economics and
engineering management also with regard to digital commerce and COVID-19.
Conclusively, the “Journal of Financial Services Marketing” and “Journal of Asian
Finance, Economics and Business”, with similar h-index values and fewer articles,
have lower impact and sharper focus on financial and economic aspects of digital
commerce during the pandemic. The aforementioned analysis identifies specific
scientific impact and publication output for the various types of journals covered,
informing about their impact according to scientific metrics and their focus on spe -
cific fields of research.
Leading countries in digital commerce and COVID-19
Table 7 shows the scientific output of countries represented in terms of the number of
articles (Freq), total citations awarded (TC), and average citations per article. China
is first with the highest scientific output, represented by 172 articles and 338 citations
awarded to its articles, with an average of 12.45 citations awarded per article. The
United States, comprising 92 articles, possesses a comparable tally of citations (338),
yielding an average citation rate of 10.90, which substantiates the significant quality
and impact of American scholarly contributions. Conversely, India and Indonesia,
with higher article counts of 123 and 189 respectively, exhibit lower average citation
figures of 7.55 and 7.25, suggesting a relatively diminished influence. In contrast,
Italy and the United Kingdom have a smaller number of articles-60 and 54, respec -
tively-but a higher average citation rate-8.75 and 12.21. Malaysia has 64 articles with
an average citation rate of 2.93, and Australia has 47 articles with an average citation
rate of 4.64; hence, both show relatively lower impact. These figures reveal lower
Country Freq TC Average article citations
INDONESIA 189 145 7.25
CHINA 172 338 12.45
INDIA 123 287 7.55
USA 92 338 10.90
MALAYSIA 64 41 2.93
ITALY 60 140 8.75
UK 54 171 12.21
ROMANIA 53 88 8.80
AUSTRALIA 47 51 4.64
BRAZIL 38 49 6.13
Table 7 Top-10 productive
countries and Influential in digi-
tal commerce and COVID-19
Source: Authors’ own
elaboration based on Scopus
data

1 3
Page 13 of 30 339
SN Business & Economics (2026) 6:339
scientific productivity and relatively narrower visibility of Malaysian publications
compared with other countries.
In summary, the data indicates that the scholarly influence of publications dif -
fers significantly by country and is not exclusively determined by article volume;
in certain nations, the emphasis on quality supersedes that of quantity. Generally,
the presented table suggests that nations such as China and the United States are
characterized by both a high output of publications and substantial scholarly impact.
Conversely, certain nations, even with substantial scientific production, may exhibit
diminished impact, a phenomenon potentially attributable to the caliber of the publi-
cations, the subjects of research, or the ease of access.
Figure 3 shows graphically the worldwide collaborations in research related to
COVID-19 and e-commerce, showing how much different countries participate in
or contribute to the international system of scientific research and innovation. The
figure shows that China is outstanding for having the highest number of linkages,
particularly with the United States with 10 linkages and the United Kingdom with 6
linkages. This shows that China is highly engaged in producing articles and studies
related to COVID-19 and e-commerce, the results of which it shares with developed
countries and international researchers.
The United States has extensive scientific collaborations with many countries,
like Canada, France, Italy, and South Korea, and thus holds an indispensable role
in the global research structure on COVID-19 and digital commerce. Countries like
Australia and Brazil, though less collaborating in their interactions, play an integral
role in the scientific network and are likely a part of research projects and scholarly
communications focusing on COVID-19 and digital business. For instance, Australia
is involved in science cooperation with countries like Pakistan and Finland, proving
that it is actively part of fields related to public health and advanced technologies.
Fig. 3 International Collaboration of Authors in Digital Commerce and COVID-19

1 3
339 Page 14 of 30
SN Business & Economics (2026) 6:339
Word-cloud analysis
Word cloud diagram illustrates (see Fig. 4) the areas of focus and direction of research
in the recent years. This figure, which is based on term frequency analysis, provides
a better means to explore scientific interests and their changes. The term “E-com -
merce” is emphasized since it appears 177 times, emphasizing that this domain is
increasingly crucial in the digital world. Such high frequency reflects technologi -
cal changes, business paradigm shifts, and transformations in commercial activities
online. The second term is “COVID-19,” which took precedence with 164 hits and
signified its wide and deep impact on several dimensions of scientific and social
investigations. The increased focus on COVID-19 reflected an in-depth investigation
into the health, economic, and social impacts of the pandemic, which signals further
and deeper reviews of this global crisis.
The terms “online shopping” and “pandemic,” which feature 30 and 26 times,
respectively, indicate changes in consumer behavior and global impacts of crises on
purchasing habits and e-commerce activities. These concepts also suggest significant
changes in buying and selling behaviors during the crisis. The term “digital trans -
formation,” which has been mentioned 24 times, refers to an emphasis on the wide -
spread changes brought about by digital technologies in various fields. This would
relate to how organizations are adapting to technological changes and alterations in
their procedures and business models. The terms “consumer behavior” and “digital
marketing,” each found 14 times, reflect a focus on detailed analyses of consumer
behaviors and digital marketing strategies as reactions to new changes. It enhances
the understanding of consumer interactions with digital channels and effectiveness of
digital promotional techniques.
In summary, this word cloud distinctly underlines the following significant research
trends: e-commerce and COVID-19 as primary research dimensions, supplemented
by online shopping, pandemics, and digital transformation with regard to changes in
consumer behavior and marketing approach. These show the broad-ranging changes
Fig. 4 Word Cloud

1 3
Page 15 of 30 339
SN Business & Economics (2026) 6:339
in priorities of scholarly investigation into the digital impacts and global emergencies
that shape commerce and consumer behavior.
Keyword co-occurrence analysis
Beyond thematic categorization, the co-occurrence analysis reveals a multi-layered
transformation of digital business research during the COVID-19 crisis. The six clus-
ters collectively indicate that the pandemic acted not merely as a temporary disrup -
tion but as an accelerator of structural digitalization across consumer, organizational,
and technological dimensions.
The co-occurrence word cloud analysis is represented, giving a clear view of focus
and research trends related to the field of digital commerce and COVID-19. It helps
in spotting and analyzing interactions and relationships of various keywords in these
two areas. The result depicted that 28 key terms are divided into 6 clusters. Figure 5
depicts these clusters as follows:
Dark blue cluster
The main items that fall into this cluster are as follows: consumer behaviour, cus -
tomer satisfaction, e-commerce, online shopping, and structural equation modelling.
Most of the literature is about how e-commerce and online shopping influence cus -
tomer satisfaction and the nature of consumer behaviour. Structural equation models
are used in the consideration of complex relationship tests between customer satis -
faction and online shopping behaviors. These analyses in this cluster help businesses
Fig. 5 Keyword co-occurrence network

1 3
339 Page 16 of 30
SN Business & Economics (2026) 6:339
have an effective customer needs and expectations map, thus developing efficient
techniques to boost their customer experiences and satisfaction.
This cluster reflects the market-facing dimension of digital transformation. The
strong linkage between e-commerce, consumer behaviour, and structural equa-
tion modelling suggests that researchers have moved beyond descriptive analy-
sis toward causal modelling of digital consumption patterns. This indicates a
shift from adoption-focused research to behaviorally grounded digital market
analysis, reinforcing the argument that COVID-19 institutionalized online con-
sumption rather than temporarily increasing it.
Green cluster
This cluster deals with some important themes: supply chain resilience, digital trans-
formation, and innovation due to the COVID-19 pandemic. It discusses the impacts
of digitalization and innovation on SMEs and supply chains and assesses the way
changes have managed to enable better resilience and adaptability in crisis situations.
The discussion centers on the role of emerging technologies and digital transforma -
tion in supply chain resilience and quality business performance against adversities.
Light blue cluster
This cluster provides keywords like digitalization, supply chain management, and
technology. The cluster shall debate the various impacts that new technologies and
digitalization have on supply chain management and analyze how supply chain pro -
cesses can be further optimized through new technologies. The investigation of such
subjects contributes to a deeper understanding of how supply chain management can
be extended and amplified and how digitalization influences process efficiency and
effectiveness.
The yellow cluster
covers the most relevant areas, including logistics management, supply chain resil -
ience, and sustainability. This cluster discusses the study of logistics process opti -
mization along with the development of supply chain resilience that would enable
the organization to face crisis situations and adversities. Another important factor
for consideration is how far sustainability might influence the improvement in per -
formance and reduction of environmental impacts. Emphasis on sustainability and
resilience within logistics brings up the capability to be better prepared for future
eventualities and to manage unexpected problems efficiently.
The prominence of supply chain resilience, logistics management, digitaliza -
tion, and sustainability signals an organizational-level restructuring of business
systems. Unlike pre-pandemic efficiency-oriented supply chains, the post-
COVID literature emphasizes resilience, agility, and technological integration.

1 3
Page 17 of 30 339
SN Business & Economics (2026) 6:339
This reflects a paradigmatic shift from cost-minimization logic toward risk-
aware and digitally integrated supply ecosystems.
The integration of sustainability within this cluster further suggests that post-
crisis digital transformation is increasingly aligned with long-term systemic
resilience rather than short-term operational survival.
Purple cluster
This cluster covers some core areas like electronic service quality, e-commerce, and
entrepreneurship. It evaluates the impact of online service quality on various perfor-
mances and achievements of e-commerce and entrepreneurship ventures. Enhanced
electronic service quality would result in an improved customer experience and satis-
faction, thus promoting expansion and growth of the online enterprise.
This cluster highlights the micro-foundational dynamics of digital business
growth. The focus on electronic service quality and entrepreneurship suggests
that digital competitiveness during crises depends not only on technological
adoption but also on experiential differentiation and service excellence. This
aligns with broader debates on value co-creation and platform-based competi -
tion in digital markets.
Red cluster
This is a cluster that emphasizes the following key concepts: digital marketing, mar-
keting, pandemic, purchase intention, social media, and trust. It was able to represent
the impact of digital marketing during crises; in this case, the pandemic. The pan -
demic has drastically affected consumer behavior and their intention to buy things.
This cluster also looks into the effect of social media and trust on purchase decision-
making and how changes in each of these components challenge companies to cre -
ate new marketing strategies that effectively influence consumer behavior and foster
trust.
The emphasis on trust, social media, and purchase intention reflects the socio-
technical dimension of digital transformation. During crisis periods character -
ized by uncertainty, trust becomes a critical moderating mechanism in digital
interactions. This cluster indicates that digital marketing research has shifted
from visibility-driven strategies toward trust-building and relationship-centered
approaches in volatile environments.
Overall, the keyword co-occurrence structure demonstrates that digital business
research during COVID-19 evolved along three interconnected levels: (1) digi-
tal market behavior transformation, (2) organizational and supply chain restruc-
turing, and (3) technological and platform-based enablement. This multi-level

1 3
339 Page 18 of 30
SN Business & Economics (2026) 6:339
configuration supports the argument that the pandemic accelerated systemic
digital transformation rather than triggering isolated digital adoption initiatives.
Co-citation analysis
While the co-occurrence analysis reveals thematic trends, the co-citation network
uncovers the intellectual foundations shaping digital business research during the
pandemic. The four clusters collectively illustrate how crisis-driven research inte -
grates economic disruption, behavioral theory, digital transformation scholarship,
and governance perspectives.
The following co-citation network is based on publications that have been cited
at least 7 times by other research studies. These articles have been labelled into four
clusters, each focused on different aspects of Digital Business and the impacts of
COVID-19. The clusters above represent the scholarly links between these articles
and their topics.
Red cluster: direct effects of COVID-19 on commercial enterprises and economic
sectors
This cluster explores the significant changes brought about by the COVID-19 pan -
demic with respect to business models and market behavior. The most influential
scholarly articles, such as “The Impact of COVID-19” by Kim R.Y ., and “Effect
of COVID-19” by Donthu N. and Gustafsson A., primarily focus on measuring the
structural changes in organizations and challenges arising from the recession. This
specific collection looks at how businesses adapt during crisis times and the social
and economic implications of the pandemic on various industries. The topics most
emphasized in this collection include consumer behavior changes and new busi -
ness model innovations. This cluster represents the crisis-shock perspective, where
COVID-19 is conceptualized as an exogenous disruption triggering structural eco -
nomic and organizational change. The literature here primarily adopts a reactive lens,
focusing on adaptation and survival mechanisms.
 Green cluster: statistical tools and theories for consumer behavior analysis
This cluster also employs statistical methods and fundamental theories in analyzing
changes in consumer behavior and the effects of COVID-19. The core works like
“The Theory of Planned Behavior” by Ajzen I. and “Statistical Power Analysis” by
Cohen J. introduce theoretical and empirical tools for investigation that are crucial for
studying the effects of crises. Advanced statistical models are developed and applied
in this cluster to analyze changes in consumer behavior and predict the impacts of
crises. Fundamentally, these papers offer statistical tools and basic theories for more
accurate analysis of pandemic-related data.
The presence of foundational theories such as the Theory of Planned Behavior
indicates that digital business research during COVID-19 relied heavily on estab -

1 3
Page 19 of 30 339
SN Business & Economics (2026) 6:339
lished behavioral frameworks to interpret rapid consumption changes. This suggests
theoretical continuity despite contextual disruption, meaning that crisis-driven digital
shifts were interpreted through pre-existing behavioral paradigms rather than entirely
new theoretical models.
Blue cluster: digital transformation and the E-commerce landscape during the
pandemic
The blue cluster focuses on the phenomenon of digital transformation and e-com -
merce development during the COVID-19 pandemic. Among those scientific contri-
butions are “Impact of COVID-19 on Consumer Behavior” by Sheth J. and “Digital
Transformation in COVID-19 Era” by Eger L., focused on changing consumer
behavior and influences of digital technologies on business adaptation strategies.
This cluster clearly focuses on the role of emerging technologies in accelerating digi-
tal transformation and developing new strategies for enterprises facing global crises.
Changes in consumer-brand interaction and their impact on digital business strategy
are central to the discussions in this cluster.
This cluster bridges crisis response and long-term transformation narratives. It
conceptualizes digital transformation not merely as a coping mechanism but as a
strategic reconfiguration of business models. The prominence of this cluster sig -
nals that scholars increasingly view the pandemic as a catalyst for enduring digital
restructuring.
Yellow cluster: COVID-19 challenges for businesses in China and the government’s
role
The yellow cluster reflects on the effect of COVID-19 on companies operating in
China and examines the relationship between governmental measures taken for crisis
management. Contributions such as “COVID-19 and Digital Business in China” by
Gao X. et al. review China’s experience during the pandemic and the strategic role
of the government in enabling digital transition. This cluster compares governance
policies and reviews their effects on the performance of digital enterprises at the
international level. More precisely, these articles discuss how governments react in
crises and their role regarding business success in times of global crises.
The governance-oriented cluster highlights the institutional dimension of digital
transformation. It suggests that post-crisis digital evolution is not solely firm-driven
but significantly shaped by national policies, regulatory frameworks, and state inter-
vention strategies.
Each cluster represents a distinct thematic domain in the area of digital business
research, reflecting interrelatedness among academic articles and hot topics in this
field, further exacerbated by the COVID-19 pandemic.
Taken together, the co-citation structure reveals a transition from crisis-response
scholarship toward a more integrated understanding of digital transformation that
incorporates behavioral theory, organizational resilience, and institutional gover -

1 3
339 Page 20 of 30
SN Business & Economics (2026) 6:339
nance. This confirms that COVID-19 functioned as a structural turning point in the
intellectual trajectory of digital business research (Fig. 6).
Identifying and analyzing research gaps in digital commerce and
COVID-19
Scholars have identified a number of key shortcomings in the area of digital busi -
ness and COVID-19 based on the reviews that have emerged from Sect. 2.7, 2.8,
and 2.9. In fact, such results should give appropriate guidelines for future research
and help to further build new research directions. Several stated research gaps have
been clearly pointed out through word cloud and co-occurrence network analyses,
which reinforce further investigation. Addressing these deficiencies will heighten our
knowledge and drive further developments of new emerging challenges in the area.
The following sections review each of these identified gaps in greater detail, present-
ing how our knowledge can be enhanced to encourage further research in these areas.
Research gap identified through the word-cloud analysis: long-term implications
for business models and market dynamics
Word cloud analysis suggests that themes such as “e-commerce,” “COVID-19,”
and “digital transformation” are discussed very frequently, evidencing that high
importance is attached to these fields in recent studies. However, a clear gap exists
regarding how COVID-19 had long-lasting effects on business models and market
mechanisms. While the short-term effects of the pandemic have been widely studied,
long-term examination on how these shocks will shape new economic and social
trends remains scant. It would be necessary to consider the way traditional and new
business models adapt themselves and change in response to such sustained changes.
The study would also involve the development of more sophisticated economic mod-
els that predict changes in the business environment and market behavior in a post-
pandemic scenario.
Fig. 6 Reference co-citation network

1 3
Page 21 of 30 339
SN Business & Economics (2026) 6:339
Research gap identified through the co-occurrence network analysis:
development of new statistical models and theoretical frameworks
The examination of co-occurrence networks highlights important clusters, such as
“consumer behavior,” “supply chain resilience,” and “digital transformation.” How-
ever, despite such analysis, there remains a significant lack of new statistical models
and theoretical frameworks to explore consumer behavior in a crisis situation. The
existing models provide a simple understanding, but they lack the novel, innovative
methodologies for in-depth analysis on how crises affect consumer behavior towards
digital platforms. Qualitative research investigating businesses’ experiences of digi -
tal transformation holds the potential to enhance such understanding. More sophis -
ticated statistical modeling will continue to provide detail about how new business
strategies and consumer behavior function in both crisis and post-crisis situations.
Research gap identified through the co-citation network analysis: comparative
analysis of government policies
Co-citation network analysis shows large clusters of research focusing on themes
such as direct impacts of COVID-19, statistical methods and consumer theories, and
digital transformation. However, there is a large gap in the comparative study of
governmental policies among heterogeneous geopolitical environments. Insufficient
research has been done on how different governmental policies influence the func -
tioning of digital companies and their managing of crises. Comparative studies can
identify successful policies and valuable experiences in crisis management, contrib -
uting to the development of effective strategies for future crises. Understanding how
different governments respond to crises and the impact of these responses on business
success globally is essential for crafting effective policies and improving governmen-
tal strategies for managing digital business challenges.
Discussion
Our bibliometric analysis paints a vivid picture of how COVID-19 has reshaped digi-
tal commerce research, with a consistent 9.1% growth in publications from 2020 to
2023 that echoes patterns observed in Şimandan (2023) and Gecit (2021), though our
dataset of 527 documents offers a wider lens than Gecit’s 345. The drop in average
citations per article, averaging around 8,362 across the board, seems to stem from
this explosion of new work, much like what Gecit ( 2021) described as a dilution
effect in rapidly expanding fields. The decline in average citations per article, aver -
aging around 8.362 across the dataset, coincided with the rapid growth in publica -
tion output. This pattern is consistent with what Gecit (2021) described as a dilution
effect in rapidly expanding fields. However, because the present study focuses exclu-
sively on the COVID-19 period and does not include a pre-pandemic baseline for
comparison, this interpretation should be treated with caution. Future studies could
compare pre- and post-pandemic publication trends to determine whether this pattern
is uniquely associated with the COVID-19 era or reflects a broader characteristic of

1 3
339 Page 22 of 30
SN Business & Economics (2026) 6:339
rapidly growing research domains. On the collaboration front, the 53% international
co-authorship rate, bolstered by China’s robust links (e.g., 10 with the USA), aligns
well with the global trends Şimandan (2023) highlighted, suggesting a truly intercon-
nected research community tackling these issues.
Diving deeper, the word cloud’s emphasis on terms like “e-commerce” (177
times) and “online shopping” (30 times) complements the six co-occurrence clusters,
which span everything from consumer behavior and supply chain resilience to digital
marketing strategies. For instance, the dark blue cluster on consumer satisfaction ties
neatly into highly cited pieces like Kim ( 2020) and Gu (2021, 133 citations), which
explore behavioral shifts during lockdowns. Similarly, the green and yellow clus -
ters on supply chain innovation and logistics resonate with Modgil (2022) and Shen
(2023, 123 citations), illustrating how AI and technology have become lifelines for
businesses. According to Sajja et al. (2025), the lessons learned from the COVID-19
pandemic suggest that resilient supply chains depend not only on digital technologies
but also on proactive risk assessment, reactive recovery capabilities, business conti -
nuity planning, and organizational learning. These strategies enable firms to respond
more effectively to unexpected shocks while maintaining operational stability and
long-term adaptability. Such insights extend the supply chain resilience cluster iden-
tified in this study by highlighting practical approaches that can strengthen prepared-
ness for future crises.
Building upon these strategic insights, the literature further highlights the pivotal
role of digital technologies in navigating these challenges. Reviews by Wei et al.
(2026) and Dura et al. ( 2026) synthesize findings on how technologies such as IoT
and AI contribute to enhanced visibility, transparency, collaboration, and risk mitiga-
tion in supply chains during disruptive periods. These insights collectively reinforce
the growing emphasis on resilient supply chain structures, enabled by technological
integration and strategic planning, thereby addressing the need for a more substan -
tive analysis of resilience strategies and lessons learned from the pandemic. The co-
citation network adds another layer, grouping influential works into four clusters:
the red one on direct economic impacts (e.g., Donthu & Gustafsson, 2020), green on
statistical tools (Ajzen, 1991; Cohen, 1992), blue on digital transformation (Sheth,
2020; Eger, 2021), and yellow on China’s policy responses (Gao et al.). This structure
reveals a field that’s not just reactive but deeply analytical, with authors like Dwivedi
YK (88 citations) and institutions like Multimedia University leading the charge,
particularly in Asia.
Compared to Scutariu et al. ( 2021), who zeroed in on seven behavioral clusters
among 31 European firms showing modest sales growth (16.45%–17.87%), our
broader scope uncovers a richer tapestry of global themes, from live-streaming mar-
keting (Clement Addo, 2021) to regional e-commerce dynamics (Beckers, 2021).
Yet, it is clear that not all regions shine equally Malaysia’s lower average citations
(2.93 per article) and journals like Forum Scientiae Oeconomia point to variations in
research depth and visibility.
That said, the gaps we have identified are particularly telling. The word cloud
analysis flags a shortfall in long-term studies on business models, where short-term
adaptations dominate but enduring market shifts remain underexplored. From the
co-occurrence networks, there’s room for fresh statistical models to dissect con -

1 3
Page 23 of 30 339
SN Business & Economics (2026) 6:339
sumer behavior in crises, moving beyond basic frameworks to more nuanced, quali -
tative approaches. The co-citation insights highlight a need for comparative policy
research across geopolitics, as China’s government strategies are well-documented
(Gao et al.). Similar analyses for other regions could reveal best practices for digital
resilience. An important observation emerging from the co-citation analysis is the
geographical concentration of policy-oriented research. The policy cluster is largely
shaped by studies examining governmental responses within the Chinese context,
reflecting the country’s prominent role in the digital transformation discourse during
the pandemic. While these studies provide valuable insights into regulatory interven-
tions and digitalization strategies, the relative absence of comparable evidence from
other national settings limits the generalizability of current knowledge. This con -
centration suggests that future comparative policy analyses across countries could
provide a more comprehensive understanding of how different institutional environ-
ments, regulatory frameworks, and crisis-response strategies influence digital busi -
ness resilience and transformation.
These oversights are not just academic; they represent opportunities to refine strat-
egies for future disruptions, blending theory with practical innovation in ways that
could truly fortify digital commerce.
The findings of this bibliometric analysis can be interpreted in light of well-estab-
lished theoretical frameworks in the literature on digital business and crisis manage-
ment. The sustained growth of topics such as e-commerce and the development of
digital platforms aligns with the broader trajectory of digital transformation, sug -
gesting that these developments represent not merely short-term responses to the
COVID-19 crisis, but rather structural and strategic shifts in digital business models
(Cardoso et al. 2025).
The prominence of themes such as supply chain resilience and organizational agil-
ity can be examined through the lens of dynamic capabilities theory, which empha -
sizes firms’ capacity to reconfigure resources and respond rapidly to environmental
shocks (Held et al. 2026). Furthermore, the research focus on network interactions,
international collaborations, and platform ecosystems highlights the critical role of
platform ecosystems in digital value creation and interorganizational innovation
(Jovanovic et al. 2022). Such theoretical linkages enhance the analytical depth of the
findings and provide a coherent framework for interpreting the results, as well as for
guiding future research and informing practical policymaking in the field of digital
commerce.
Previous bibliometric studies in the field of digital business and COVID-19 have
demonstrated that this domain has been characterized by a rapid growth in scholarly
publications and an expansion of international collaborations, encompassing a wide
range of research themes. For instance, Pratama (2025), in a comparative analysis of
the pre- and post-pandemic periods, showed that emerging topics such as sustainabil-
ity, the circular economy, and technological innovation gained increased prominence
following COVID-19, findings that are consistent with the thematic clusters identi -
fied in the present study (Pratama 2025).
Zare and Persaud (2025), through a bibliometric analysis of the scientific literature
on digital transformation (DT) and business model innovation (BMI) spanning the
period from 1999 to 2023, mapped the intellectual structure of the field and identified

1 3
339 Page 24 of 30
SN Business & Economics (2026) 6:339
key themes as well as significant research gaps, including the need to further examine
the relationship between digital transformation and business model innovation
and the role of emerging technologies.
In comparison, the present study, with a specific focus on the COVID-19
period (2020–2024), investigates emerging research trends in digital business
and identifies thematic clusters related to consumer behavior, supply chains,
digital marketing, and emerging technologies. Thus, whereas the study by Zare
and Persaud provides a broad historical and integrative perspective, the cur -
rent research offers a more precise and up-to-date account of evolving schol -
arly trends during the pandemic by emphasizing crisis impact and employing
network-based cluster analysis, thereby delivering distinct methodological and
substantive added value (Zare and Persaud 2025).
The study by Petropoulou et al. ( 2024) demonstrates that in the aftermath
of COVID-19, small and medium-sized enterprises (SMEs) have increasingly
moved toward the adoption of digital technologies and innovation in their busi -
ness models. This trajectory is likewise reflected in the thematic clusters identi -
fied in the present article.
By providing a more fine-grained analysis of scholarly interactions, mapping
the network structure of themes, and identifying emerging research trajecto -
ries, the current study offers a more comprehensive, up-to-date, and practice-
oriented account of research trends during the pandemic period. In doing so,
it also reveals scholarly gaps that have received comparatively limited atten -
tion in prior studies. Accordingly, the findings of this article are consistent with
the general trends identified in prior research. However, by concentrating on
emerging themes and employing thematic cluster analysis as well as co-citation
network analysis, the study provides a more precise and practically relevant
depiction of the intellectual structure of the digital business field during the
pandemic period.
Conclusion
This bibliometric analysis, drawing on 527 documents from 308 sources, reveals a
dynamic and rapidly evolving research landscape on digital commerce in the wake
of COVID-19, marked by a steady 9.1% annual growth rate from 2020 to 2024 and a
notable 53% international co-authorship rate. Key insights from highly cited works—
such as Kim ( 2020) with 251 citations on consumer behavior shifts, Tran (2021)
on managing e-commerce platforms amid crises, and Modgil (2022) on AI’s role in
supply chain resilience—align closely with prominent terms in the word cloud, like
“e-commerce” (177 occurrences) and “COVID-19” (164 occurrences), and the six
co-occurrence clusters covering consumer behavior, supply chain resilience, and dig-
ital marketing. The co-citation network further organizes the field into four thematic
clusters, emphasizing direct pandemic effects, statistical tools for consumer analy -
sis, digital transformation, and government roles in China. Influential contributors,
including authors like Dwivedi YK (88 citations) and institutions such as Multime -

1 3
Page 25 of 30 339
SN Business & Economics (2026) 6:339
dia University (10 articles), alongside top journals like the Journal of Retailing and
Consumer Services (668 citations), underscore the global, interdisciplinary nature of
this research. China and the USA emerge as leaders in both output and impact, with
strong collaborative ties evident in the network.
Interestingly, while the pandemic has clearly accelerated digital innovation, the
analysis also highlights persistent gaps, such as the need for deeper exploration of
long-term business model implications, advanced statistical frameworks for crisis-
era consumer behavior, and comparative studies of government policies across
regions. These findings not only map the intellectual structure of the field but also
provide practical guidance for policymakers and business leaders aiming to build
more resilient digital ecosystems. Moving forward, addressing these gaps through
targeted, longitudinal studies could yield even richer insights into how global crises
reshape commerce in the digital age.
Practical implications
The present study carries several implications for managers, policymakers,
and digital entrepreneurs navigating the post-pandemic business environment.
First, the consistent growth of research on e-commerce and online enterprises
highlights the importance for firms to embed digital transformation as a long-
term strategic priority rather than a temporary crisis response. Organizations
that invested in digital infrastructure, contactless services, and online customer
engagement during COVID-19 should continue refining these capabilities to
remain competitive in an increasingly digital marketplace.
Second, the prominence of consumer behavior and supply chain resilience as
research themes suggests that firms must place equal emphasis on agility and
customer-centricity. Businesses can benefit from developing data-driven tools to
anticipate shifts in consumer expectations during periods of uncertainty, while
also strengthening digital supply chains through technologies such as AI, block -
chain, and real-time analytics.
Third, the strong international collaboration reflected in the literature under -
scores the value of cross-border knowledge sharing. Policymakers and indus -
try leaders can leverage these insights to design coordinated strategies for
digital resilience, including regulatory frameworks that foster innovation while
safeguarding consumer trust. Expanding comparative policy research beyond
dominant economies like China and the USA would enable more inclusive and
adaptable approaches to global disruptions.
Finally, the identified research gaps, such as the need for longitudinal per -
spectives and advanced analytical frameworks, suggest that managers and prac -
titioners should not only adopt short-term digital solutions but also invest in
resilient, adaptable business models. Building these models with a focus on sus -
tainability, inclusivity, and preparedness will position enterprises to better with -
stand future crises and capitalize on emerging opportunities in digital commerce.

1 3
339 Page 26 of 30
SN Business & Economics (2026) 6:339
Limitations and future research directions
This study has several limitations. First, the dataset covers publications from 2020
to 2024, which may exclude recent or forthcoming research capturing post-pandemic
developments. Second, reliance on bibliometric indicators emphasizes structural pat-
terns but cannot fully assess the theoretical depth or practical impact of individual
studies. Third, the field shows a geographic concentration, with China and the United
States dominating output and collaborations, which may overshadow insights from
emerging economies and alternative policy contexts. Finally, the exclusion of practi-
tioner reports and grey literature limits the scope, as these often document real-time
digital innovations not yet reflected in academic research. Future research should
address these gaps by conducting longitudinal studies that track the durability of digi-
tal transformation strategies and business model innovations beyond the pandemic.
Comparative analyses across countries and industries would provide a richer under -
standing of cultural, institutional, and sectoral differences in digital adoption. Meth -
odological advances, such as predictive analytics and simulation modeling, could
enhance insights into consumer behavior during crises. Integrating academic and
practitioner perspectives, as well as examining underrepresented sectors like educa -
tion, tourism, and small enterprises, will also broaden the field. Such efforts can guide
the development of resilient and sustainable digital ecosystems to better prepare for
future global disruptions.
Future research could employ longitudinal designs to examine the sustainability
and evolution of digital transformation strategies and business model innovation over
the long term. Moreover, the adoption of methodological innovations such as predic-
tive analytics, simulation modeling, and mixed quantitative–qualitative approaches
may yield a more nuanced understanding of consumer behavior, supply chain resil -
ience, and organizational decision-making under conditions of uncertainty.
Comparative analyses across countries, industries, and policy regimes, particu -
larly within emerging economies, would further enrich the existing literature and
contribute to the development of more inclusive and context-sensitive policy frame -
works. Finally, expanding the scope of inquiry to relatively underexplored sectors,
such as small and medium-sized enterprises, education, and tourism, and integrating
academic and practitioner perspectives could facilitate the development of sustain -
able and resilient digital ecosystems capable of withstanding future crises.
Among the limitations of this study is the exclusion of grey literature. Although
this approach may have resulted in the omission of certain non-formally published
works, it was a deliberate and methodologically informed decision aimed at ensuring
the quality, standardization, and comparability of the bibliometric data. While the
concentration of scientific output in a limited number of countries, particularly the
United States and China might be considered another limitation, this pattern reflects
less a methodological bias or data constraint and more the global structure of knowl-
edge production under crisis conditions. Within this structure, differences in digital
infrastructure capacity, research funding, and innovation ecosystems play a decisive
role in shaping scholarly outputs. It should also be noted that publication and citation
metrics for 2024 are inherently incomplete, due to the time lag in indexing and cita -

1 3
Page 27 of 30 339
SN Business & Economics (2026) 6:339
tion accrual processes. Consequently, growth rates and citation-based indicators for
the most recent year should be interpreted with caution.
Authors’ contributions The authors jointly contributed to the conception and design of the study, data col-
lection and analysis, interpretation of the findings, and drafting and revision of the manuscript. All authors
read and approved the final manuscript.
Funding The authors declare that no funds, grants, or other support were received during the preparation
of this manuscript.
Data availability The data analyzed during the current study are available from the corresponding author
upon reasonable request.
Code availability No custom code was developed for this study. The analyses were conducted using the
Bibliometrix package in R and VOSviewer.
Declarations
Competing interests The authors have no relevant financial or non-financial interests to disclose.
Open Access  This article is licensed under a Creative Commons Attribution 4.0 International License,
which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long
as you give appropriate credit to the original author(s) and the source, provide a link to the Creative
Commons licence, and indicate if changes were made. The images or other third party material in this
article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line
to the material. If material is not included in the article’s Creative Commons licence and your intended use
is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission
directly from the copyright holder. To view a copy of this licence, visit  h t t p : / / c r e a t i v e c o m m o n s . o r g / l i c e n
s e s / b y / 4 . 0 /     .
References
Abdolkhani R, Petersen S, Walter R, Zhao L, Butler-Henderson K, Livesay K (2022) The impact of digital
health transformation driven by COVID-19 on nursing practice: Systematic literature review. JMIR
Nurs 5(1):e40348. https://doi.org/10.2196/40348
Ahmad Z, AlWadi BM, Kumar H, Ng BK, Nguyen DN (2024) Digital transformation of family-owned
small businesses: A nexus of internet entrepreneurial self-efficacy, artificial intelligence usage and
strategic agility. Kybernetes. https://doi.org/10.1108/K-01-2024-0032
Ajzen I (1991) The theory of planned behavior. Organ Behav Hum Decis Process 50(2):179–211.  h t t p s : / /
d o i . o r g / 1 0 . 1 0 1 6 / 0 7 4 9 - 5 9 7 8 ( 9 1 ) 9 0 0 2 0 - T
Almasri H, Zakuan N, Amer MS, Majid MR (2021) A developed systematic literature review procedure
with application in the field of digital transformation. Stud Appl Econ 39(4).  h t t p s : / / d o i . o r g / 1 0 . 2 5 1
1 5 / e e a . v 3 9 i 4 . 5 0 9 6
Amankwah-Amoah J, Khan Z, Wood G, Knight G (2021) COVID-19 and digitalization: The great accel-
eration. J Bus Res 136:602–611. https://doi .org/10.101 6/j.jbusres .2021.08 .011
Aria M, Cuccurullo C (2017) Bibliometrix: An R-tool for comprehensive science mapping analysis. J
Informetrics 11(4):959–975. https://doi.org/10.1016/j.joi.2017.08.007
Azzahra S, Ayunanda SN, Suhendra ES (2022) How digitalisation affecting employees’ well-being during
Covid-19 outbreak: A meta-analysis study. Jurnal Ilmiah Ekonomi Bisnis 27(1):44–57.  h t t p s : / / d o i . o
r g / 1 0 . 3 5 7 6 0 / e b . 2 0 2 2 . v 2 7 i 1 . 4 8 3 3
Ball R, Tunger D (2006) Science indicators revisited–Science Citation Index versus SCOPUS: A biblio -
metric comparison of both citation databases. Inform Serv use 26(4):293–301

1 3
339 Page 28 of 30
SN Business & Economics (2026) 6:339
Behie SW, Pasman HJ, Khan FI, Shell K, Alarfaj A, El-Kady AH, Hernandez M (2023) Leadership 4.0:
The changing landscape of industry management in the smart digital era. Process Saf Environ Prot
172:317–328. https://doi.org/10.1016/j.psep.2022.12.061
Bolton RN, McColl-Kennedy JR, Cheung L, Gallan A, Orsingher C, Witell L, Zaki M (2018) Customer
experience challenges: Bringing together digital, physical and social realms. J Service Manage
29(5):776–808. https://doi.org/10.1108/JOSM-04-2018-0113
Bonnet D, Westerman G (2021) The new elements of digital transformation. MIT Sloan Manage Rev
62(2):82–89
Burlea-Schiopoiu A, Borcan I, Dragan CO (2023) The impact of the COVID-19 crisis on the digital trans-
formation of organizations. Electronics 12(5):1205. https://doi.org/10.3390/electronics12051205
Cardoso A, Figueiredo J, Oliveira I, Pocinho M (2025) From crisis to opportunity: Digital transformation,
digital business models, and organizational resilience in the post-pandemic era. Administrative Sci
15(6):193
Chawla N, Kumar B (2022) E-commerce and consumer protection in India: The emerging trend. J Bus
Ethics 180(2):581–604. https://doi.org/10.1007/s10551-021-04820-x
Cheng X, Xue T, Yang B, Ma B (2023) A digital transformation approach in hospitality and tourism research.
Int J Contemp Hospitality Manage 35(8):2944–2967. https://doi.org/10.1108/IJCHM-05-2022-0667
Clement Addo P, Fang J, Asare AO, Kulbo NB (2021) Customer engagement and purchase intention in
live-streaming digital marketing platforms. Serv Ind J 41(11–12):767–786.  h t t p s  : / / d o i  . o r g /  1 0 . 1  0 8 0 /
0 2 6 4 2 0 6 9 . 2 0 2 1 . 1 9 0 5 7 9 8
Cohen J (1992) Statistical Power Analysis: Current Directions. Psychol Sci 1(3):98–101.  h t t p s : / / d o i . o r g / 1
0 . 1 1 1 1 / 1 4 6 7 - 8 7 2 1 . e p 1 0 7 6 8 7 8 3
Donthu N, Gustafsson A (2020) Effects of COVID-19 on business and research. J Bus Res 117:284–289.
https://doi .org/10.101 6/j.jbusres .2020.06 .008
Donthu N, Kumar S, Mukherjee D, Pandey N, Lim WM (2021) How to conduct a bibliometric analysis:
An overview and guidelines. J Bus Res 133:285–296. https://doi .org/10.101 6/j.jbusres .2021.04 .070
Dura BS, Nadeem SP, Garza-Reyes JA, Alemu AE, Tabar R, Zapata B, D. H., Kreie A (2026) The role of
technology in developing resilient supply chains: a systematic literature review during the COVID-
19 pandemic and the disruptions of economic sanctions. J Humanitarian Logistics Supply Chain
Manage 16(1):27–49
Eger L, Komárková L, Egerová D, Mičík M (2021) The effect of COVID-19 on consumer shopping
behaviour: Generational cohort perspective. J Retailing consumer Serv 61:102542.  h t t p s  : / / d o i  . o r g /  1
0 . 1  0 1 6 / j . j r e t c o n s e r . 2 0 2 1 . 1 0 2 5 4 2
Fatimah P, Sodri A, Hamzah US (2021) Smart technology in the construction industry: Opportunity during
the COVID-19 pandemic. Jurnal Riset Teknologi dan Inovasi Pendidikan 4(1):1–13.  h t t p s : / / d o i . o r g /
1 0 . 1 2 3 4 5 / j r t i p . 2 0 2 1 . 0 4 . 0 1
Gecit BB (2021) Electronic commerce during the Covid-19 pandemics: A bibliometric analysis approach.
Int J Acad Res Bus Social Sci 11(11):2435–2444. https://doi .org/10.600 7/IJARBSS/v 11-i11/1 1731
Gleiss A, Kohlhagen M, Pousttchi K (2021) An apple a day–How the platform economy impacts value
creation in the healthcare market. Electron Markets 31(4):849–876.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 1 2 5 2
5 - 0 2 1 - 0 0 4 6 7 - 7
Gunathilaka P, Rupasingha R (2022) Customer satisfaction on digital banking during the Covid-19 pan -
demic: A case study of banking customers in Sri Lanka. Sri Lankan J Bank Finance, 5(2): 35-57.
https://doi.org/10.4038/sljbf.v5i2.30
Guthrie C, Fosso-Wamba S, Arnaud JB (2021) Online consumer resilience during a pandemic: An explor-
atory study of e-commerce behavior before, during and after a COVID-19 lockdown. J Retailing
Consumer Serv 61:102570. https://doi .org/10.101 6/j.jretcon ser.2021 .102570
Hanelt A, Bohnsack R, Marz D, Antunes Marante C (2021) A systematic review of the literature on digital
transformation: Insights and implications for strategy and organizational change. J Manage Stud
58(5):1159–1197. https://doi.org/10.1111/joms.12639
Held P, Heubeck T, Meckl R (2026 ) Boosting SMEs’ digital transformation: the role of dynamic capabili-
ties in cultivating digital leadership and digital culture. RMS 20: 1687-1715.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0
7 / s 1 1 8 4 6 - 0 2 5 - 0 0 9 1 9 - 5
Hussain Z (2021) Paradigm of technological convergence and digital transformation: The challenges of
CH sectors in the global COVID-19 pandemic and commencing resilience-based structure for the
post-COVID-19 era. Digit Appl Archaeol Cult Herit 21:e00182.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . d a a c h . 2 0
2 1 . e 0 0 1 8 2

1 3
Page 29 of 30 339
SN Business & Economics (2026) 6:339
Jovanovic M, Sjödin D, Parida V (2022) Co-evolution of platform architecture, platform services, and
platform governance: Expanding the platform value of industrial digital platforms. Technovation
118:102218
Khoshroo M, Talari M (2023) Scientific mapping of digital transformation strategy research studies in the
Industry 4.0: A bibliometric analysis. Nankai Bus Rev Int 14(1):3–34.  h t t p s : / / d o i . o r g / 1 0 . 1 1 0 8 / N B R
I - 0 4 - 2 0 2 1 - 0 0 2 7
Kim RY (2020) The impact of COVID-19 on consumers: Preparing for digital sales. IEEE Eng Manage
Rev 48(3):212–218. https://doi.org/10.1109/EMR.2020.2990115
Kokol P (2023) Discrepancies among Scopus and Web of Science: Implications for bibliometrics How to
combine and clean bibliometric data and use … by W. M. Lim et al. (2024). Scientometrics.  h t t p s : / /
d o i . o r g / 1 0 . 1 0 0 7 / s 1 1 1 9 2 - 0 2 3 - 0 4 6 8 0 - w
Kshetri N, Dwivedi YK, Davenport TH, Panteli N (2024) Generative artificial intelligence in marketing:
Applications, opportunities, challenges, and research agenda. Int J Inf Manag 75:102716.  h t t p s  : / / d o i
. o r g /  1 0 . 1  0 1 6 / j . i j i n f o m g t . 2 0 2 3 . 1 0 2 7 1 6
Liu CH, Robertson PJ (2024) Spirituality in the workplace: Theory and measurement. J Manage Inq
20(1):35–50. https://doi.org/10.1177/1056492610387225
Mariani MM, Nambisan S (2021) Innovation analytics and digital innovation experimentation: The rise of
research-driven online review platforms. Technol Forecast Soc Chang 172:121009.  h t t p s  : / / d o i  . o r g /  1
0 . 1  0 1 6 / j . t e c h f o r e . 2 0 2 1 . 1 2 1 0 0 9
Nankoomar T, Quilling R (2023) Impact of coronavirus on digital transformation in private sector organ-
isations in developing countries. Int J Res Bus Social Sci 12(10):1–12.  h t t p s : / / d o i . o r g / 1 0 . 2 0 5 2 5 / i j r b
s . v 1 2 i 1 0 . 2 9 8 8
Nawaser K, Jafarkhani F, Khamoushi S, Yazdi A, Mohsenifard H, Gharleghi B (2024) The dark side of
digitalization: A visual journey of research through digital game addiction and mental health. IEEE
Eng Manage Rev
Nawaser K, Yazdi A, Mohsenifard H (2026) Women in Digital Entrepreneurship: A Bibliometric Explo -
ration of Trends, Barriers, and Strategies Across Global Contexts. The Entrepreneurial Narratives
of Women Driving Economic and Social Transformation in Latin America. IGI Global Scientific
Publishing, pp 1–36
Petropoulou A, Angelaki E, Rompogiannakis I, Passas I, Garefalakis A, Thanasas G (2024) Digital trans-
formation in SMEs: pre-and post-COVID-19 era: a comparative bibliometric analysis. Sustainability
16(23):10536
Pranckutė R (2021) Web of Science (WoS) and Scopus: The titans of bibliographic information in today’s
academic world. Publications 9(1):12
Pratama FC (2025) A Bibliometric Analysis of Digital Business Models: Comparative Insights Before and
After COVID-19. SISFO 12(1):32–45
Rahawarin FR, Soetjipto BE, Wardoyo C (2023) Digital transformation and MSME financial performance:
Systematic literature review and bibliometric analysis. Econ Bus J (ECBIS) 1(4):313–322.  h t t p s : / / d
o i . o r g / 1 0 . 2 2 2 1 9 / e c b i s . v 1 i 4 . 2 5 8 9 1
Raihan A (2024) A review of the digitalization of the small and medium enterprises (SMEs) toward sus -
tainability. Global Sustain Res 3(2):1–16. https://doi.org/10.1016/j.gsr.2024.100028
Raišys SJ, Raišienė AG (2023) Management theories’ potential for better digital service customer experi-
ence. Manage Organizations: Syst Res 89(1):91–106. https://doi.org/10.1515/mosr-2023-0006
Sajja GS, Meesala MK, Ravipati P, Addula SR (2025), June Strengthening supply chain resilience through
lessons learned from the COVID-19 pandemic and implementing strategies for future preparedness.
In AIP Conference Proceedings (V ol. 3306, No. 1, p. 040032). AIP Publishing LLC
Sanasi S, Ghezzi A (2024) Pivots as strategic responses to crises: Evidence from Italian companies navi -
gating Covid-19. Strategic Organ 22(3):495–529. https://doi.org/10.1177/14761270231175742
Scutariu AL, Șuşu Ș, Huidumac-Petrescu CE, Gogonea RM (2021) A cluster analysis concerning the
behavior of enterprises with e-commerce activity in the context of the COVID-19 pandemic. J Theo-
retical Appl Electron Commer Res 17(1):47–68. https://doi.org/10.3390/jtaer17010003
Sheth J (2020) Impact of Covid-19 on consumer behavior: Will the old habits return or die? J Bus Res
117:280–283. https:   //d oi. or g/10 . 1016/j. jbus re s .2020.05.059
Şimandan R (2023) Electronic commerce research during the COVID-19 pandemic: A bibliometric analy-
sis. J Int Commer Econ Policy 14(2):2350010. https://doi.org/10.1142/S1793993323500100
Stahlschmidt S, Stephen D (2020) Comparison of web of science, scopus and dimensions databases. KB
forschungspoolprojekt 2020(10):37

1 3
339 Page 30 of 30
SN Business & Economics (2026) 6:339
Wei S, Jiang J, Chen J, Wang Q (2026) Digital technology and supply chain resilience: A literature review
and emerging themes. Int Trans Oper Res 33(4):2167–2189
Yazdi A, Ramachandran S, Mohsenifard H, Nawaser K, Sasani F, Gharleghi B (2024a) The ebb and flow
of brand loyalty: A 28-year bibliometric and content analysis. arXiv
Yazdi A, Nawaser K, Pezeshgi S, Mohsenifard H, Golamian E (2024b) Artificial intelligence in social
sustainability: A bibliometric and content analysis-based review. Multidisciplinary Reviews
Yuan W, Wang N, Lai J, Zuo J, Chen G, Du H (2016) Characteristics and trends of research on waste-to-
energy incineration: A bibliometric analysis, 1999–2015. Renew Sustain Energy Rev 66:95–104.
https://doi.org/10.1016/j.rser.2016.07.006
Zare J, Persaud A (2025) Digital transformation and business model innovation: a bibliometric analysis of
existing research and future perspectives. Manage Rev Q 75(3):1999–2032
Zheng H, Li Q, Xia C (2024) Does financial literacy contribute to facilitating residents in safeguarding
their rights as financial consumers? A three-stage study based on the perspective of fraud phenom -
enon. Int Rev Econ Finance 93:720–735. https://doi.org/10.1016/j.iref.2023.09.012
Authors and Affiliations
Khaled Nawaser1 · Hassan Hessari2  · Hoda Mohsenifard3 · Azin Yazdi4 ·
Babak Ghahremannasab5
 Hassan Hessari
hassanhessari@vt.edu
Khaled Nawaser
khalednawaser56@gmail.com
Hoda Mohsenifard
hoda.mohsenifard@gmail.com
Azin Yazdi
azinyazdi36@gmail.com
Babak Ghahremannasab
B.Ghahremannasab@yahoo.com
1 Arvandan Non-Profit Higher Education Institute, Khorramshahr, Iran
2 Department of Business Information, Technology, Pamplin College of Business, Virginia
Tech, Blacksburg, V A, USA
3 Shahid Chamran University of Ahvaz, Ahvaz, Iran
4 Payame Noor University, Tehran, Iran
5 Department of Management and Accounting, University of Zanjan, Zanjan, Iran
