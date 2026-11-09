---
title: Mapping the Evolution of Artificial Intelligence in Digital Marketing
url: https://doi.org/10.51629/ijeamal.v6i2.320
category: ai-marketing
subcategory: empirical
date: 2026-07
venue: International Journal of Educational Administration Management and Leadership
authors:
- Kahfi
source: openalex-oa
pdf_url: https://harpressid.com/IJEAMaL/article/download/320/244
pages: 22
chars: 63232
fetched_at: '2026-11-08T18:17:21+00:00'
kb_version: 1
---

# Mapping the Evolution of Artificial Intelligence in Digital Marketing

International Journal of Educational Administration,
Management, and Leadership
Volume 5, Number 1,  May 2024,  Page 154-175
ISSN 2722-0249 (Print) and  2774-6143 (online)

Mapping the Evolution of Artificial Intelligence in Digital Marketing:
A Bibliometric Analysis Using Biblioshiny
Muhammad Kahfi
Department of Business Administration, Faculty of Administrative Science, Universitas
Brawijaya, Indonesia

E-mail:  muhkahfi46@student.ub.ac.id

 (Received: June-2025; Reviewed: August-2025; Accepted: September-2025;
Available Online:  November-2024; Published: November-2025)

ABSTRACT
Artificial intelligence has become an incr easingly important topic in digital marketing research,
particularly due to the rapid development of machine learning, big data analytics, personalization,
chatbots, generative AI, and digital commerce. This study aims to map the scientific development of
research on artificial intelligence and digital marketing using bibliometric analysis. Bibliographic data
were collected from the Scopus database using the search string TITLE -ABS-KEY (“artificial
intelligence” AND “digital marketing”). After applying filt ers for publication year, document type,
language, and publication stage, 148 journal articles published between 2020 and 2024 were included in
the final dataset. The data were analyzed using Biblioshiny, the web -based interface of the bibliometrix
package in RStudio. The findings show that research on artificial intelligence and digital marketing has
grown rapidly, with an annual growth rate of 56.51%. The number of publications increased from 12
articles in 2020 to 72 articles in 2024. The most productive  source was the Journal of Digital and Social
Media Marketing, while the most globally cited document was Dwivedi et al. (2021), with 1,744
citations. Keyword analysis shows that artificial intelligence, digital marketing, machine learning,
commerce, social media, big data, and deep learning are dominant themes. The thematic map and co -
occurrence network indicate that artificial intelligence and digital marketing form the core conceptual
structure of the field, while ChatGPT, SEO, deep learning, and digital  transformation represent
specialized or emerging themes. This study contributes to the literature by providing a comprehensive
bibliometric overview of AI and digital marketing research and identifying future directions related to
generative AI, personalization, consumer trust, privacy, and AI-driven marketing performance.

Keywords: Artificial intelligence; digital marketing; bibliometric analysis; Biblioshiny; bibliometrix;
machine learning; generative AI; social media marketing

INTRODUCTION

Amidst Artificial intelligence has become one of the most transformative technologies in
contemporary marketing (Davenport et al., 2020; Vlačić et al., 2021). The rapid development of
machine learning, natural language processing, predictive analytics, recommender systems,

Kahfi; Mapping the Evolution of Artificial Intelligence in Digital Marketing …|155

chatbots, and generative AI has changed how firms understand consumers, design marketing
strategies, personalize content, automate communication, and optimize customer experiences
(De Mauro et al., 2022). In digital marketing, AI enables marketers to process large volumes of
consumer data, identify behavioral patterns, deliver personalized recommendations, predict
consumer preferences, and improve the efficiency of marketing decision -making (Gupta &
Chhabria, 2023; Ziakis & Vlachopoulou, 2023). As a result, AI is no longer viewed merely a s a
supporting technology, but as a strategic capability that reshapes the way firms interact with
consumers in digital environments.
The integration of artificial intelligence into digital marketing has become increasingly
important as consumers interact with brands through various digital touchpoints, including
search engines, social media, e -commerce platforms, mobile applications, websites, and online
communities (Bormane & Blaus, 2024; Ziakis & Vlachopoulou, 2023) . These digital
interactions generate large amounts of data that can be used to improve targeting accuracy,
personalize advertising messages, enhance customer engagement, and support real -time
marketing decisions (Sakalauskas & Kriksciuniene, 2024; Theodorakopoulos &
Theodoropoulou, 2024) . AI -powered tools allow firms to move from general marketing
communication toward more individualized and predictive forms of consumer interaction ( V.
Kumar et al., 2019; Şenyapar, 2024). This development has encouraged scholars to examine the
role of AI in areas such as customer relationship management, personalized advertising, digital
consumer behavior, marketing automation, service quality, social media marketing, and ethical
issues in data-driven marketing (Potwora et al., 2024; Van Esch & Black, 2021).
Despite the growing importance of artificial intelligence in digital marketing, the literature in
this field remains fragmented (Mariani et al., 2021; Thakur & Kushwaha, 2023) . Existing
studies have examined differe nt aspects of AI, such as personalization, consumer trust, privacy
concerns, chatbots, recommendation systems, customer engagement, and digital advertising
effectiveness (Babadoğan, 2024; Islam et al., 2024) . However, because these studies are spread
across different journals, disciplines, methods, and theoretical perspectives, it is difficult to
obtain a comprehensive understanding of how the field has evolved (Mariani et al., 2021) .
Furthermore, the rapid development of AI technologies creates new research directions that
require systematic mapping, including the emergence of generative AI, algorithmic
personalization, consumer privacy, ethical marketing, and AI-driven customer experience (Islam
et al., 2024; Thakur & Kushwaha, 2023).
Previous reviews have provided valuable insights into artificial intelligence in marketing and
digital business contexts (Mariani et al., 2021) . However, there is still a need for a focused
bibliometric study that maps the intellectual structure and thematic evolution of research
specifically at the intersection of artificial intelligence a nd digital marketing (Thakur &
Kushwaha, 2023; Verma et al., 2021) . A bibliometric ap proach is useful because it allows
researchers to identify publication trends, influential authors, leading journals, highly cited
articles, productive countries, collaboration patterns, and emerging research themes. Unlike
traditional narrative reviews, bibliometric analysis provides a systematic and quantitative
overview of the development of a research field based on bibliographic data (S. Kumar et al.,
2022; Thakur & Kushwaha, 2023; Verma et al., 2021).
To address this gap, this study conducts a bibliometric analysis of artificial intelligence and
digital marketing research indexed in the Scopus database. The study focuses on journal art icles
published between 2020 and 2024. This period was selected because AI -related research in
digital marketing has expanded rapidly in recent years, particularly with the increasing adoption
of AI-based personalization, automation, and data -driven marketing practices. Using the search
string TITLE-ABS-KEY ("artificial intelligence" AND "digital marketing"), the initial search
produced 1,154 documents. After applying filters for publication year, document type, language,

156    International Journal of Educational Administration, Management, and Leadership
   Volume 6, Number 2,  November 2025,  Page 154-175

and publication stage, 148 final jo urnal articles were obtained and analyzed using Biblioshiny,
the web-based interface of the bibliometrix package in RStudio.
This study aims to map the scientific development of artificial intelligence research in digital
marketing and to identify the key contributors, intellectual structure, and emerging themes in the
field. Specifically, this study addresses the following research questions:
RQ1: How has the scientific production of artificial intelligence and digital marketing
research developed from 2020 to 2024?
RQ2: Which authors, sources, documents, institutions, and countries have contributed most
significantly to the field?
RQ3: What are the most influential keywords and thematic clusters in artificial intelligence
and digital marketing research?
RQ4: How are collaboration patterns among authors, institutions, and countries structured in
this field?
RQ5: What emerging themes and future research directions can be identified from the
bibliometric mapping?
This study contributes to the literature in sev eral ways. First, it provides a comprehensive
bibliometric overview of artificial intelligence and digital marketing research from 2020 to
2024. Second, it identifies the most productive and influential contributors in the field,
including authors, journals, countries, institutions, and documents. Third, it maps the conceptual
structure of the field through keyword analysis, co -occurrence networks, thematic maps, and
trend topics. Fourth, it offers insights into emerging research directions that can guide f uture
studies on AI -driven digital marketing. Finally, the study provides practical value for
researchers, marketers, and decision-makers by clarifying how AI-related topics have developed
within the digital marketing domain.

METHOD
Research Design
This study employed a bibliometric analysis to examine the development of research on
artificial intelligence in digital marketing. Bibliometric analysis was selected because it enables
researchers to systematically evaluate the scientific structure of a researc h field using
publication and citation data. This method is useful for identifying publication trends, influential
authors, leading sources, highly cited documents, productive countries, collaboration patterns,
and emerging themes within a specific research domain (Gutiérrez-Salcedo et al., 2017; Oliveira
et al., 2019).
Unlike traditional literature reviews that rely mainly on qualitative interpretation,
bibliometric analysis provides a quantitative and systematic approach to mapping the
development of academic knowledge (S. Kumar et al., 2022). Therefore, this method is suitable
for understanding how research on artificial intelligence and digital marketing has evolved over
time, especially during the rapid growth of AI -based technologies in marketing practices
(Thakur & Kushwaha, 2023).
This study used Biblioshiny, the web-based interface of the bibliometrix package in RStudio,
to analyze and visualize the bibliographic data. Biblioshiny was selected because it provides an
integrated platform for conducting bibliometric analysis, including descriptive analysis, source
analysis, author analysis, document analysis, keyword analysis, conceptual structure analysis,
and collaboration network analysis (Aria & Cuccurullo, 2017).

Kahfi; Mapping the Evolution of Artificial Intelligence in Digital Marketing …|157

Data Source

To The bibliographic data were collected from the Scopus database. Scopus was selected
because it is one of the largest multidisciplinary academic databases and provides
comprehensive bibliographic metadata, including article titles, abstracts, keywords, authors,
affiliations, citations, source titles, and references (Kumpulainen & Seppänen, 2022). The use of
Scopus was considered appropriate because this study aimed to analyze peer -reviewed journal
articles indexed in a widely recognized international database (Baas et al., 2020).
The search was conducted using the keywords “artificial intelligence” and “digital
marketing”. These keywords were selected because they directly represent the intersection
between AI-related technologies and digital marketing research. The search was limited to the
title, abstract, and keyword fields to ensure that the retrieved documents were directly related to
the topic.

Search Strategy

The search string used in the Scopus database was as follows:
TITLE-ABS-KEY ( "artificial intelligence" AND "digital marketing" ) AND ( LIMIT -TO (
DOCTYPE , "ar" ) ) AND ( LIMIT -TO ( LANGUAGE , "English" ) ) AND ( LIMIT -TO (
PUBSTAGE , "final" ) ) AND PUBYEAR > 2019 AND PUBYEAR < 2025
The initial search using the keywords “artificial intelligence” AND “digital marketing”
resulted in 1,154 documents. The search was then refined by applying several filters. First, the
publication year was limited to 2020 –2024, resulting in 509 documents. Second, the document
type was limited to journal articles, reducing the number of documents to 156. Third, the
language was limited to English, resulting in 150 documents. Finally, the publication stage was
limited to final publications, producing a final dataset of  148 articles.

Inclusion and Exclusion Criteria

This study applied inclusion and exclusion criteria to ensure that the dataset was relevant to the
research objective. The inclusion criteria were: documents indexed in Scopus, articles related to
artificial intelligence and digital marketing, publications from 2020 to 2024, journal articles,
English-language publications, and final-stage publications.
Documents were excluded if they were published before 2020 or after 2024, categorized as
conference papers, book chapters, reviews, editorials, notes, letters, or other non -article
document types, written in languages other than English, or still in press. These criteria were
applied to maintain consistency and ensure that the final dataset consisted only of peer-reviewed
journal articles relevant to the research topic.

Table 1.
Data Screening Process.
Screening Stage Criteria Applied Number of Documents
Initial search “artificial intelligence” AND “digital marketing” 1,154
Year limitation 2020–2024 509
Document type Article only 156
Language English only 150
Publication stage Final publication only 148
Final dataset Documents analyzed using Biblioshiny 148

158    International Journal of Educational Administration, Management, and Leadership
   Volume 6, Number 2,  November 2025,  Page 154-175

Data Export and Analysis Procedure
After the final dataset was obtained, the bibliographic records were exported from Scopus for
further analysis. The exported data included citation information, bibliographical information,
abstracts, author keywords, index keywords, affiliations, references, and source information.
The data were then imported into Biblioshiny through RStudio.
The analysis was conducted using several bibliometric indicators and visualization
techniques. First, descriptive bibliometric analysis was used to identify the  main information
about the dataset, including total documents, annual scientific production, average citations,
number of authors, author collaboration, and annual growth rate. Second, source analysis was
conducted to identify the most relevant journals and publication outlets in the field. Third,
author and affiliation analyses were performed to identify the most productive authors and
institutions.
Fourth, document analysis was used to identify the most globally cited articles, which
represent influentia l works in artificial intelligence and digital marketing research. Fifth,
country analysis was conducted to examine scientific production and collaboration among
countries. Sixth, keyword analysis was used to identify the most frequent author keywords and
index keywords. Finally, conceptual structure analysis was conducted through co -occurrence
network analysis, thematic map, and trend topic analysis to identify major research themes and
emerging topics in the field.

Bibliometric Indicators
Several bibliometric indicators were used in this study. Publication productivity was measured
through annual scientific production, most relevant sources, most productive authors, and
country scientific production. Scientific influence was examined through citation -based
indicators, including most cited documents and source impact. Collaboration patterns were
analyzed through country collaboration and co-authorship networks.
To identify the conceptual structure of the field, keyword co -occurrence analysis was
conducted. This analysis helps reveal the relationships among frequently used keywords and
identifies thematic clusters within the literature. Thematic map analysis was also used to classify
research themes into four categories: motor themes, basic themes, niche themes, and emerging
or declining themes. These analyses provide a more comprehensive understanding of the
intellectual and thematic development of artificial intelligence in digital marketing research.

Research Workflow
The research workflow consisted of fiv e main stages. First, the research topic and search
keywords were determined. Second, the bibliographic data were retrieved from the Scopus
database using a predefined search string. Third, inclusion and exclusion criteria were applied to
obtain the final dataset. Fourth, the data were exported and processed using Biblioshiny in
RStudio. Fifth, the bibliometric results were interpreted to identify publication trends, influential
contributors, collaboration patterns, thematic structures, and future research directions.

Kahfi; Mapping the Evolution of Artificial Intelligence in Digital Marketing …|159

RESULT AND DISCUSSION
Main Information of the Dataset
The bibliometric analysis was conducted using 148 journal articles published between 2020 and
2024. These documents were retrieved from 114 sources, indicating that research on artificial
intelligence and digital marketing has been distributed across a wide range of publication
outlets. The dataset showed an annual growth rate of 56.51%, suggesting a rapid increase in
scholarly attention to this topic during the selected period.
The docu ment average age was 3.13 years, which indicates that the dataset consisted of
relatively recent publications. This is consistent with the rapid development of artificial
intelligence applications in digital marketing, particularly in areas such as personalization,
marketing automation, consumer analytics, social media marketing, and digital customer
experience. The average citation per document was 53.61, indicating that the publications in this
field have received considerable scholarly attention.
The dat aset included 441 Keywords Plus and 543 author keywords, reflecting diverse
research themes in artificial intelligence and digital marketing. It involved 496 authors, with an
average of 3.42 co -authors per document and 29.73% international co -authorship, indicating
moderate global collaboration.

Table 2.
Main Information About the Dataset.

Description Results
Main Information About Data
Timespan 2020:2024
Sources (Journals, Books, etc) 114
Documents 148
Annual Growth Rate % 56.51
Document Average Age 3.13
Average citations per doc 53.61
References 0
Document Contents
Keywords Plus (ID) 441
Author's Keywords (DE) 543
Authors
Authors 496
Authors of single-authored docs 29
Authors Collaboration
Single-authored docs 30
Co-Authors per Doc 3.42
International co-authorships % 29.73
Document Types
article 148

160    International Journal of Educational Administration, Management, and Leadership
   Volume 6, Number 2,  November 2025,  Page 154-175

Overall, the main information indicates that artificial intelligence in digital marketing is an
emerging and rapidly growing research area. The high annual growth rate and relatively re cent
document age demonstrate that the field has gained increasing academic attention in recent
years. The large number of authors and keywords further suggests that this research area is
multidisciplinary and conceptually diverse.

Annual Scientific Production

Annual scientific production was analyzed to identify the publication trend of research on
artificial intelligence and digital marketing from 2020 to 2024. As shown in Table 3, the number
of publications increased steadily during the selected period . In 2020, there were 12 articles
published on this topic. The number increased to 17 articles in 2021, 21 articles in 2022, and 26
articles in 2023. A substantial increase occurred in 2024, with 72 articles published.
This trend indicates that scholarly attention to artificial intelligence in digital marketing has
grown significantly in recent years. The sharp increase in 2024 suggests that AI has become an
increasingly important topic in digital marketing research, particularly with the rapid
development of AI-driven personalization, marketing automation, generative AI, data analytics,
customer experience management, and digital consumer behavior. The growth pattern also
reflects the increasing relevance of AI technologies in transforming marketing practices and
consumer-brand interactions in digital environments.

Table 3.
Annual Scientific Production.

Year Articles
2020 12
2021 17
2022 21
2023 26
2024 72

Overall, the annual scientific production shows a strong upward trend, especially in 2024. Th is
finding confirms that artificial intelligence and digital marketing represent a rapidly expanding
research domain. The increase in publications also suggests that researchers are increasingly
interested in examining how AI reshapes digital marketing strategies, consumer engagement,
and marketing decision-making.

Most Relevant Sources

The most relevant sources were analyzed to identify the journals and publication outlets that
contributed most frequently to research on artificial intelligence and digita l marketing. As
shown in Table 4, the Journal of Digital and Social Media Marketing was the most productive
source, with 6 articles. This was followed by Applied Marketing Analytics, with 5 articles.
Several sources contributed 3 articles each, including Financial and Credit Activity: Problems of
Theory and Practice, IAES International Journal of Artificial Intelligence, Information
(Switzerland), International Journal of Data and Network Science, Journal of Retailing and
Consumer Services, and Sustainability (Switzerland).

Kahfi; Mapping the Evolution of Artificial Intelligence in Digital Marketing …|161

These findings indicate that research on artificial intelligence and digital marketing is published
across diverse interdisciplinary outlets. The presence of marketing -oriented sources such as the
Journal of Digital and Social Media Marketing, Applied Marketing Analytics, and Journal of
Retailing and Consumer Services suggests that AI has become an important topic in marketing
and consumer behavior research. At the same time, the inclusion of journals related to artificial
intelligence, in formation systems, sustainability, and data science indicates that the field is
multidisciplinary and involves contributions from both business and technology perspectives.

Table 4.
Most Relevant Sources.

Sources Articles
Journal Of Digital And Social Media Marketing 6
Applied Marketing Analytics 5
Financial And Credit Activity: Problems Of Theory And Practice 3
Iaes International Journal Of Artificial Intelligence 3
Information (Switzerland) 3
International Journal Of Data And Network Science 3
Journal Of Retailing And Consumer Services 3
Sustainability (Switzerland) 3
Applied Sciences (Switzerland) 2
Business Ethics And Leadership 2

Overall, the distribution of sources shows that artificial intelligence in digital marketing is not
confined to a single publication domain. Instead, the topic is discussed across marketing,
retailing, data science, artificial intelligence, sustainability, and business ethics journals. This
reflects the broad relevance of AI in digital marketing as both a technolo gical and managerial
research area.

Most Relevant Authors

The most relevant authors were analyzed to identify researchers who contributed most
frequently to the field of artificial intelligence and digital marketing. As shown in Table 5, the
most productive authors each contributed 2 articles. These authors include Allahham Mahmoud,
Cutler Kelly, Dwivedi Yogesh K., Giannakopoulos Nikolaos T., Kanellos Nikos, Li Chia -Ying,
Migkos Stavros P., Sakas Damianos P., Saura Jose Ramon, and Wang Yichuan.
The results indicate that no single author strongly dominated the research field during the
2020–2024 period. Instead, the publication output was distributed across many researchers. This
pattern suggests that artificial intelligence in digital marketing is an emerging and
interdisciplinary research area, attracting scholars from different academic backgrounds,
including marketing, information systems, artificial intelligence, data analytics, consumer
behavior, and business management.

162    International Journal of Educational Administration, Management, and Leadership
   Volume 6, Number 2,  November 2025,  Page 154-175

Table 5.
Most Relevant Authors.

Author Articles Articles Fractionalized
Allahham Mahmoud 2 0.33
Cutler Kelly 2 2.00
Dwivedi Yogesh K 2 0.22
Giannakopoulos Nikolaos T 2 0.42
Kanellos Nikos 2 0.42
Li Chia-Ying 2 0.83
Migkos Stavros P 2 0.42
Sakas Damianos P 2 0.42
Saura Jose Ramon 2 0.67
Wang Yichuan 2 0.22

The fractionalized article score provides additional insight into the authors’ relative contribution
by considering co-authorship patterns. Cutler Kelly had the highest fractionalized score of 2.00,
indicating full authorship contribution across the documents included in the dataset. In contrast,
authors such as Dwivedi Yogesh K. and Wang Yichuan had lower fractionalized scores,
suggesting that their publications involved larger co-author teams. Overall, the results show that
the field is characterized by collaborative and distributed authorship rather than concentration
around a small group of dominant researchers.

Most Globally Cited Documents

The most globally cited documents were analyzed to identify influential publications in the field
of artificial intelligence and digital marketing. As shown in Table 6, the most cited article was
Dwivedi et al. (2021), entitled Setting the future of digital and social media marketing research:
Perspectives and research propositions, with 1,744 citations. This article represents a
foundational contribution because it discusses future research directions in digital and social
media marketing, including the growing role of emerging technologies such as artificial
intelligence.
The second most cited document was Liye and Sun (2020), entitled Machine learning and AI
in marketing: Connecting computing power to human insights, with 487 citations. This article
highlights the role of machine learning and AI in transforming marketing insights and decision -
making. The third most cited document was Chintalapati and Pandey (2022), entitled Artificial
intelligence in marketing: A systematic literature review, with 375 citations, indicating the
importance of review -based studies in consolidating knowledge about AI applications in
marketing.
Other highly cited documents focus on AI-based customer relationship management, chatbot
communication, trust in chatbot interactions, virtual influencers, and AI -powered influencer
marketing. For example, Saura et al. (2021) examined B2B digital marketing in AI -based
customer relationship management, while Kull et al. (2021) and Toader et al. (2020) focused on
chatbot-related engagement and trust. More recent highly cited articles, such as Allal -Chérif et

Kahfi; Mapping the Evolution of Artificial Intelligence in Digital Marketing …|163

al. (2024) and Kim and Park (2024), indicate that virtual influencers and AI -powered influencer
marketing are becoming important emerging themes in the field.

Table 6.
Most Globally Cited Documents.

Author Paper Total Citations
(Dwivedi et al., 2021) Setting the future of digital and social media marketing research: Perspectives and research propositions 1744
(Liye & Sun, 2020) Machine learning and AI in marketing Connecting computing power to human insights 487
(Chintalapati &
Pandey, 2022)
Artificial intelligence in marketing: A systematic
literature review 375
(Saura et al., 2021)
Setting B2B digital marketing in artificial intelligence-
based CRMs: A review and directions for future
research
247
(Kull et al., 2021) How may I help you? Driving brand engagement through the warmth of an initial chatbot message 216
(Toader et al., 2020) The effect of social presence and chatbot errors on trust 203
(Van Esch & Black,
2021)
Artificial Intelligence (AI): Revolutionizing Digital
Marketing 178
(da Silva Oliveira &
Chimenti, 2021)
“Humanized Robots”: A Proposition of Categories to
Understand Virtual Influencers 166
(Allal-Chérif et al.,
2024)
Intelligent influencer marketing: how AI-powered
virtual influencers outperform human influencers 154
(Kim & Park, 2024)
When digital celebrity talks to you: How human-like
virtual influencers satisfy consumer's experience
through social presence on social media endorsements
140

Overall, the most globally cited documents show that the intellectual foundation of this field is
shaped by several major themes: digital and social media marketing transformati on, machine
learning in marketing, AI -based customer relationship management, chatbot interaction,
consumer trust, and virtual influencer marketing. The presence of both older and recent highly
cited articles indicates that the field is rapidly evolving from general AI adoption in marketing
toward more specific applications such as AI -powered personalization, chatbots, and virtual
influencers.

Most Relevant Affiliations

The most relevant affiliations were analyzed to identify institutions that contributed  most
frequently to research on artificial intelligence and digital marketing. As shown in Table 7, the
State University of Trade and Economics was the most productive affiliation, with 5 articles.
This was followed by Swansea University, Universitat Politècnica de València, and Universiti
Teknologi MARA, each contributing 4 articles.
Several institutions contributed 3 articles each, including Instituto Universitário de Lisboa,
Manchester Metropolitan University, State University of Information and Communic ation

164    International Journal of Educational Administration, Management, and Leadership
   Volume 6, Number 2,  November 2025,  Page 154-175

Technologies, and University of Southern California. Meanwhile, Agricultural University of
Athens and Al-Ahliyya Amman University contributed 2 articles each.

Table 7.
Most Relevant Affiliations.
Affiliation Articles
State University Of Trade And Economics 5
Swansea University 4
Universitat Politècnica De València 4
Universiti Teknologi Mara 4
Instituto Universitário De Lisboa 3
Manchester Metropolitan University 3
State University Of Information And Communication Technologies 3
University Of Southern California 3
Agricultural University Of Athens 2
Al-Ahliyya Amman University 2

The findings indicate that research on artificial intelligence and digital marketing is contributed
by institutions from different geographical and academic contexts. The presence of universities
from Europe, Asia, and North America suggests that this research field has attracted global
scholarly attention. However, the relatively small number of articles contributed by each
institution indicates that the field is still emerging and institutionally dispersed, rather than
being dominated by a limited number of research centers.

Country Scientific Production
Country scientific production was analyzed to identify the countries that contributed most
actively to research on artificial intelligence and digital marketing. As shown in Table 8, the
United States was the most productive country, with 53 publications. This indicates that the
United States has played a leading role in developing research on AI applications in d igital
marketing. India ranked second with 43 publications, followed by Ukraine with 36 publications
and the United Kingdom with 24 publications.
Other countries also contributed to the development of the field, including Jordan with 20
publications, China with 18 publications, Spain with 16 publications, Portugal with 12
publications, Indonesia with 11 publications, and France with 10 publications. The presence of
countries from North America, Europe, Asia, and the Middle East indicates that artificial
intelligence in digital marketing has become a globally relevant research topic.
Overall, the results show that research on artificial intelligence and digital marketing is
geographically diverse, although publication output is still concentrated in several leading
countries. The dominance of the United States and India suggests strong scholarly interest in
AI-driven marketing transformation, digital platforms, consumer analytics, and marketing
automation. Meanwhile, the inclusion of Indonesia among the top te n contributing countries
indicates that emerging economies are also beginning to participate in this research domain.

Kahfi; Mapping the Evolution of Artificial Intelligence in Digital Marketing …|165

Table 8.
Country Scientific Production.
Country Freq Country Freq
USA 53 China 18
India 43 Spain 16
Ukraine 36 Portugal 12
Uk 24 Indonesia 11
Jordan 20 France 10

Most Frequent Words
The most frequent words were analyzed to identify the dominant concepts in the literature on
artificial intelligence and digital marketing. As shown in Table 9, the most frequently occurring
term was artificial intelligence, with 80 occurrences, followed by digital marketing, with 78
occurrences. These two terms represent the core focus of the dataset and confirm that the
retrieved documents are closely aligned with the research topic.
The term marketing appeared 35 times, indicating that AI -related research is strongly
connected to broader marketing studies. Meanwhile, machine learning appeared 20 times,
suggesting that machine learning is one of the most frequently discussed AI techniques in digital
marketing research. Other important terms include commerce with 17 occurrences, social media
with 15 occurrences, and big data with 12 occurrences. These terms indicate that AI in digital
marketing is closely associated with digital commerce, social media platforms, and data -driven
marketing practices.
The presence of terms such as social media marketing, marketing strategy, and deep learning
further shows that the field is developing around both managerial and technological themes. On
the managerial side, researchers focus on marketing strategy and social media marketing. On the
technological side, researchers examine machine learning, big data, and deep learning as tools
for improving digital marketing effectiveness.

Table 9.
Most Frequent Words.
Words Occurrences
artificial intelligence 80
digital marketing 78
marketing 35
machine learning 20
commerce 17
social media 15
big data 12
social media marketing 9
marketing strategy 8
deep learning 7

166    International Journal of Educational Administration, Management, and Leadership
   Volume 6, Number 2,  November 2025,  Page 154-175

Overall, the most frequent words indicate that ar tificial intelligence and digital marketing
research is centered on the integration of AI technologies with marketing practices. The frequent
appearance of machine learning, big data, and deep learning suggests that the technological
foundation of the field is strongly data -driven. At the same time, terms such as social media,
commerce, and marketing strategy show that the application of AI is closely related to digital
platforms, consumer interaction, and strategic marketing decision-making.

Thematic Map

The thematic map was used to identify the conceptual structure of research on artificial
intelligence and digital marketing. The map classifies themes based on two dimensions:
centrality and density. Centrality indicates the relevance of a theme to the overall research field,
while density indicates the level of internal development within the theme. Based on these
dimensions, themes can be classified into four quadrants: motor themes, basic themes, niche
themes, and emerging or declining themes.
As shown in Figure 1, the cluster consisting of artificial intelligence, digital marketing, and
marketing appears as one of the most central themes in the field. This indicates that these terms
represent the core intellectual foundation of the research domain. The position of this cluster
suggests that AI and digital marketing are strongly connected to other themes and serve as the
central focus of the literature.
The thematic map also shows several basic themes, including machine learning, commerce,
and marketing strategy. These themes have high centrality but relatively lower density, meaning
that they are important and widely connected to the field but still have room for further
theoretical and methodological development. The presence of machine learning and commerce
indicates that AI in digital marketing is closely associated with data -driven decision-making,
digital commerce, and strategic marketing applications.
Another basic theme includes AI, digital transformation, and learning algorithms. This
cluster sugge sts that digital transformation and algorithmic technologies are important
foundations for understanding the role of AI in marketing. However, its lower density indicates
that these themes are still developing and may become more mature as future studies further
examine AI-enabled transformation in marketing practices.
In the niche themes quadrant, terms such as SEO, ChatGPT, and search engine optimization
appear as specialized but relatively isolated topics. These themes show higher internal
development but lower centrality, indicating that they are well -defined within specific research
areas but not yet fully integrated into the broader artificial intelligence and digital marketing
literature. The presence of ChatGPT as a niche theme reflects the growing interest in generative
AI, although this topic may still be emerging as a more specialized research stream during the
selected period.
The cluster consisting of consumer behavior, mobile marketing, and content marketing
appears closer to the emerging or dec lining themes area. This suggests that these themes may
represent either developing topics or areas that require stronger integration with the central AI
and digital marketing literature. Since consumer behavior and content marketing are highly
relevant to digital marketing, their position may indicate that future research needs to connect
these themes more explicitly with AI -based personalization, predictive analytics, generative
content, and customer experience.

Kahfi; Mapping the Evolution of Artificial Intelligence in Digital Marketing …|167

Figure 1. Thematic Map of Artificial Intelligence and Digital Marketing Research.

Overall, the thematic map indicates that artificial intelligence and digital marketing form the
central structure of the field, while machine learning, commerce, marketing strategy, digital
transformation, SEO, ChatGPT, and content marketing represent important supporting or
emerging themes. These findings suggest that the field is evolving from general discussions of
AI in marketing toward more specific applications involving machine learning, generative AI,
search optimization, digital transformation, and consumer-oriented marketing strategies.

Trend Topics

Trend topic analysis was conducted to identify the temporal development of important
keywords in artificial intelligence and digital marketing research. As shown in Table 10, the
earliest terms appearing in the trend analysis include human and article, with median years
around 2021 and 2022. These terms are likely related to database indexing and should be
interpreted cautiously. More substantive terms such a s big data, artificial intelligence, digital
marketing, marketing, commerce, artificial intelligence (AI), and deep learning provide clearer
insight into the thematic evolution of the field.
The term big data appeared with a frequency of 12 and had a median year of 2022, indicating
that early research in the selected period strongly emphasized the role of large -scale data in
digital marketing. This reflects the importance of data -driven marketing practices, customer

168    International Journal of Educational Administration, Management, and Leadership
   Volume 6, Number 2,  November 2025,  Page 154-175

analytics, and consumer behavior predicti on. The terms artificial intelligence and digital
marketing had the highest frequencies, with 80 and 78 occurrences respectively, and both had a
median year of 2023. This suggests that AI and digital marketing became increasingly central
topics during the middle of the 2020–2024 period.
In more recent years, terms such as commerce, artificial intelligence (AI), and deep learning
show median years of 2024. This indicates that recent studies have shifted toward more specific
AI applications in digital commerce and advanced computational techniques. The emergence of
deep learning suggests that researchers are increasingly paying attention to more advanced AI
methods, while the appearance of commerce reflects the growing connection between AI, e -
commerce, social commerce, and digital business models.

Table 10.
Trend Topics
Term Frequency Year (Q1) Year (Median) Year (Q3)
human 6 2020 2021 2023
big data 12 2022 2022 2024
article 5 2020 2022 2023
artificial intelligence 80 2022 2023 2024
digital marketing 78 2022 2023 2024
marketing 35 2022 2023 2024
commerce 17 2022 2024 2024
artificial intelligence (ai) 8 2022 2024 2024
deep learning 7 2023 2024 2024

Overall, the trend topic analysis shows that research on artificial intelligence and digital
marketing has developed from broader discussions of big data and marketing toward more
specific topics such as AI -driven commerce and deep learning. The dominance of artificial
intelligence and digital marketing confirms that these two concepts form the central res earch
focus, while the emergence of commerce and deep learning indicates future opportunities for
research on AI -enabled digital commerce, predictive marketing, automated decision -making,
and advanced analytics.

Keyword Co-occurrence Network

A keyword co -occurrence network was generated to visualize the conceptual relationships
among the most frequently occurring terms in the field of artificial intelligence and digital
marketing. In this network, node size represents the frequency of keyword occurrence, while the
links between nodes represent co -occurrence relationships. Different colors indicate thematic
clusters, showing how keywords are grouped into related research streams.
As shown in Figure 2, the term artificial intelligence appears as the largest and most central
node in the network. This indicates that it is the dominant concept connecting multiple research
themes within the field. Its central position suggests that artificial intelligence serves as the
intellectual core of the literature and is s trongly linked to other topics in digital marketing
research.
The network reveals several thematic clusters. The red cluster is centered on artificial
intelligence and appears to represent the broad conceptual foundation of the field. This cluster

Kahfi; Mapping the Evolution of Artificial Intelligence in Digital Marketing …|169

reflects the core discussion of AI as a technological driver in digital marketing research. The
blue cluster is highly interconnected and seems to capture application -oriented themes,
particularly those related to digital marketing practices, commerce, and strateg ic applications.
The strong connectivity within this cluster indicates that research has increasingly focused on
how AI is implemented in commercial and marketing contexts.
The green cluster appears to represent themes associated with marketing processes and
consumer-oriented applications. Its relatively dense internal connections suggest that this stream
involves closely related discussions surrounding marketing activities, consumer interaction, and
the use of AI for enhancing marketing performance. Meanwh ile, the purple cluster is smaller
and more peripheral, which may indicate a more specialized or emerging set of topics that has
not yet become fully integrated into the broader field.
Overall, the co -occurrence network confirms that research on artificial intelligence and
digital marketing is conceptually interconnected, with artificial intelligence acting as the main
hub linking multiple application domains. The network also suggests that the field is evolving
beyond general discussions of AI toward more specialized themes involving digital marketing
strategy, commerce, consumer-oriented marketing, and emerging AI applications.

Figure 2. Keyword Co-occurrence Network of Artificial Intelligence and Digital Marketing
Research.

Implications
Theoretical Implications
This study provides several theoretical implications for artificial intelligence and digital
marketing literature. First, the findings show that AI in digital marketing is a rapidly expanding
research domain. The sharp increase in publications, p articularly in 2024, indicates that AI has
become a central topic in marketing research. This supports the view that AI is not merely a
technological tool, but an important theoretical domain that reshapes digital marketing,
consumer behavior, and marketing strategy.
Second, this study contributes to the literature by mapping the intellectual structure of AI and
digital marketing research. The most cited documents indicate that the field is influenced by
research on digital marketing transformation, machine  learning, AI -based CRM, chatbot
communication, trust, and virtual influencers. This shows that the theoretical foundation of the
field is multidisciplinary, combining marketing, information systems, consumer psychology,
data analytics, and digital business.

170    International Journal of Educational Administration, Management, and Leadership
   Volume 6, Number 2,  November 2025,  Page 154-175

Third, the thematic map and keyword co-occurrence network show that the field is structured
around several major themes, including artificial intelligence, digital marketing, machine
learning, commerce, marketing strategy, big data, and deep learning. T hese findings indicate
that future theoretical development should not treat AI as a single broad concept, but should
distinguish between specific AI applications, such as personalization, recommendation systems,
chatbots, generative AI, predictive analytics, and virtual influencers.
Fourth, the presence of emerging themes such as ChatGPT, deep learning, and digital
transformation suggests that the field is moving toward more advanced and specialized research
streams. This provides an opportunity for future researchers to develop new theoretical models
explaining how generative AI and advanced analytics influence consumer engagement, brand
trust, customer experience, and digital marketing performance.
Finally, this study contributes methodologically by demonstrating the value of bibliometric
analysis for mapping the development of AI in digital marketing. By using Biblioshiny, this
study provides a systematic overview of publication trends, influential contributors, thematic
clusters, and emerging research dir ections. This can help future researchers identify research
gaps and position their studies within the broader intellectual structure of the field.

Practical Implications

The findings also provide practical implications for marketers, managers, digital strategists, and
technology developers. First, the rapid growth of AI and digital marketing research indicates
that firms should pay greater attention to AI -based marketing capabilities. AI can support
marketers in customer segmentation, personalization, ca mpaign optimization, content creation,
predictive analytics, and customer relationship management.
Second, the frequent appearance of keywords such as machine learning, big data, commerce,
social media, and marketing strategy suggests that AI should be integrated into broader digital
marketing strategies. Firms should not use AI only for automation, but also for generating
customer insights, improving decision -making, and creating more personalized consumer
experiences.
Third, the emergence of topics such a s ChatGPT, virtual influencers, and deep learning
indicates that marketers need to prepare for new forms of AI -driven consumer interaction.
Generative AI can support content creation, chatbot communication, search optimization, and
personalized recommendations. However, firms must also consider ethical issues, transparency,
consumer trust, and privacy concerns when implementing these technologies.
Fourth, the results suggest that AI in digital marketing requires collaboration between
marketing professionals, data scientists, IT specialists, and strategic decision -makers. Since the
field is multidisciplinary, organizations need cross -functional capabilities to effectively use AI
in marketing. This includes not only technological skills, but also consumer understanding,
ethical awareness, and strategic marketing knowledge.
Finally, the findings can help practitioners identify future areas of investment. Themes such
as AI -driven commerce, deep learning, predictive marketing, social media analytics, and
generative AI are likely to become increasingly important. Firms that understand these trends
may be better prepared to adapt to changing digital marketing environments and consumer
expectations.

Kahfi; Mapping the Evolution of Artificial Intelligence in Digital Marketing …|171

Limitations and Future Research

This study has several limitations that should be acknowledged. First, the bibliometric data were
collected only from the Scopus database. Although Scopus is a comprehensive and widely
recognized academic database, it may not include all relevant publications on artificial
intelligence a nd digital marketing. Future studies may combine data from Scopus, Web of
Science, Dimensions, or Google Scholar to obtain a broader dataset.
Second, this study only included journal articles written in English and published between
2020 and 2024. While this period is relevant because AI -related research in digital marketing
has grown rapidly in recent years, the exclusion of conference papers, book chapters, reviews,
and non-English publications may limit the scope of the analysis. Future research may incl ude
other document types and languages to capture a wider range of scholarly contributions.
Third, the search strategy used the terms “artificial intelligence” and “digital marketing.”
Although these keywords directly represent the focus of the study, some relevant studies may
use different terms, such as “machine learning,” “marketing analytics,” “AI -powered
personalization,” “generative AI,” “chatbots,” or “algorithmic marketing.” Future studies may
expand the search string to include these related terms and compare the results.
Fourth, this study relied on bibliometric indicators such as publication counts, citations,
keywords, thematic maps, and co-occurrence networks. These indicators are useful for mapping
the structure of the field, but they do not provide a detailed qualitative evaluation of the
theoretical arguments, methods, or findings of each article. Future research may combine
bibliometric analysis with systematic literature review or content analysis to provide deeper
insights.
Fifth, the thematic map and keyword co-occurrence network depend on the quality of author
keywords, index keywords, and metadata exported from Scopus. Some keywords may be too
general or generated by indexing systems, such as “human” or “article,” and therefore require
careful interpretation. Future studies may apply keyword cleaning and standardization
procedures to improve the precision of conceptual mapping.
Future research can explore several promising directions. First, researchers can examine the
role of generative A I in digital marketing, including ChatGPT, AI -generated content, virtual
influencers, and automated copywriting. Second, future studies can investigate how AI-powered
personalization affects consumer trust, privacy concerns, perceived intrusiveness, and purchase
intention. Third, researchers can examine ethical issues in AI -driven marketing, such as
algorithmic transparency, data privacy, bias, and consumer manipulation. Fourth, future studies
can focus on AI applications in social commerce, influencer mark eting, customer relationship
management, and omnichannel marketing. Finally, future research can develop empirical
models that test the impact of AI adoption on marketing performance, customer engagement,
and brand loyalty.

Conclusion

This study conducted a bibliometric analysis of artificial intelligence and digital marketing
research using 148 Scopus indexed journal articles published between 2020 and 2024. The
analysis was conducted using Biblioshiny, the web -based interface of the bibliometrix package
in RStudio. The findings show that research on artificial intelligence and digital marketing has
grown rapidly, with a strong increase in publication output, particularly in 2024. This indicates
that AI has become a highly relevant and expanding research topic in the digital marketing
domain.

172    International Journal of Educational Administration, Management, and Leadership
   Volume 6, Number 2,  November 2025,  Page 154-175

The results show that the field is interdisciplinary and globally distributed. Publications
appeared across diverse sources, including marketing, data science, artificial intelligence,
information systems, sustainabil ity, and retailing journals. The most relevant authors and
affiliations indicate that the field is still emerging and not yet dominated by a small group of
scholars or institutions. Country production analysis shows that the United States, India,
Ukraine, the United Kingdom, Jordan, and China were among the leading contributors, while
Indonesia also appeared among the top ten contributing countries.
The keyword and thematic analyses reveal that artificial intelligence, digital marketing,
machine learning, commerce, big data, social media, marketing strategy, and deep learning are
key themes in the field. The thematic map indicates that artificial intelligence and digital
marketing form the central structure of the literature, while topics such as ChatGPT, SEO,
digital transformation, and deep learning represent specialized or emerging areas. The co -
occurrence network further confirms that artificial intelligence acts as the main conceptual hub
connecting multiple research streams.
Overall, this study conclude s that artificial intelligence in digital marketing is a rapidly
growing and conceptually diverse research field. The literature has evolved from broad
discussions of AI and big data toward more specific applications involving machine learning,
digital commerce, generative AI, virtual influencers, customer engagement, and marketing
strategy. Future research should further explore the theoretical, ethical, and practical
implications of AI -driven marketing, particularly in relation to consumer trust, privacy,
personalization, and marketing performance.

Kahfi; Mapping the Evolution of Artificial Intelligence in Digital Marketing …|173

REFERENCES

Allal-Chérif, O., Puertas, R., & Carracedo, P. (2024). Intelligent Influencer Marketing: How AI -
Powered Virtual Influencers Outperform Human Influencers. Technological Forecasting And
Social Change, 200. Https://Doi.Org/10.1016/J.Techfore.2023.123113
Aria, M., & Cuccurullo, C. (2017). Bibliometrix: An R -Tool For Comprehensive Science Mapping
Analysis. Journal Of Informetrics, 11(4), 959–975. Https://Doi.Org/10.1016/J.Joi.2017.08.007
Baas, J., Schotten, M., Plume, A., Côté, G., & Karimi, R. (2020). Scopus As A Curated, High -Quality
Bibliometric Data Source For Academic Research In Quantitative Science Studies. Quantitative
Science Studies, 1(1), 377–386. Https://Doi.Org/10.1162/Qss_A_00019
Babadoğan, B. (2024). Unveiling The Power Of AI -Driven Personalization: Transforming Consumer
Behavior In The Age Of Digital Marketing. Next Frontier For Life Sciences And AI .
Https://Doi.Org/10.62802/Fj43xy18
Bormane, S., & Blaus, E. (2024). Artificial Intellig ence In The Context Of Digital Marketing
Communication. Frontiers In Communication. Https://Doi.Org/10.3389/Fcomm.2024.1411226
Chintalapati, S., & Pandey, S. K. (2022). Artificial Intelligence In Marketing: A Systematic Literature
Review. International Jou rnal Of Market Research , 64(1), 38 –68.
Https://Doi.Org/10.1177/14707853211018428
Da Silva Oliveira, A. B., & Chimenti, P. (2021). “Humanized Robots”: A Proposition Of Categories
To Understand Virtual Influencers. Australasian Journal Of Information Systems , 25, 1 –27.
Https://Doi.Org/10.3127/Ajis.V25i0.3223
Davenport, T., Guha, A., Grewal, D., & Bressgott, T. (2020). How Artificial Intelligence Will Change
The Future Of Marketing. Journal Of The Academy Of Marketing Science , 48(1), 24 –42.
Https://Doi.Org/10.1007/S11747-019-00696-0
De Mauro, A., Sestino, A., & Bacconi, A. (2022). Machine Learning And Artificial Intelligence Use
In Marketing: A General Taxonomy. Italian Journal Of Marketing , 2022, 439 –457.
Https://Doi.Org/10.1007/S43039-022-00057-W
Dwivedi, Y. K., Ismagilova, E., Hughes, D. L., Carlson, J., Filieri, R., Jacobson, J., Jain, V.,
Karjaluoto, H., Kefi, H., Krishen, A. S., Kumar, V., Rahman, M. M., Raman, R., Rauschnabel, P.
A., Rowley, J., Salo, J., Tran, G. A., & Wang, Y. (2021). Setting The Future  Of Digital And Social
Media Marketing Research: Perspectives And Research Propositions. International Journal Of
Information Management , 59, 102168.
Https://Doi.Org/Https://Doi.Org/10.1016/J.Ijinfomgt.2020.102168
Gupta, S., & Chhabria, S. (2023). The Use Of Artificial Intelligence And Machine Learning In Digital
Marketing In 2023: Trends And Insights. International Journal Of Computer Applications .
Https://Doi.Org/10.5120/Ijca2023922635
Gutiérrez-Salcedo, M., Martínez, M. Á., Moral -Munoz, J., Herrera -Viedma, E., & Cobo, M. (2017).
Some Bibliometric Procedures For Analyzing And Evaluating Research Fields. Applied
Intelligence, 48, 1275–1287. Https://Doi.Org/10.1007/S10489-017-1105-Y
Islam, M. A., Fakir, S. I., Masud, S. Bin, Hossen, M. D., Islam, M. T., & Siddiky, M. R. (2024).
Artificial Intelligence In Digital Marketing Automation: Enhancing Personalization, Predictive
Analytics, And Ethical Integration. Edelweiss Applied Science And Technology .
Https://Doi.Org/10.55214/25768484.V8i6.3404
Kim, H., & Park, M . (2024). When Digital Celebrity Talks To You: How Human -Like Virtual
Influencers Satisfy Consumer’s Experience Through Social Presence On Social Media
Endorsements. Journal Of Retailing And Consumer Services , 76.
Https://Doi.Org/10.1016/J.Jretconser.2023.103581
Kull, A. J., Romero, M., & Monahan, L. (2021). How May I Help You? Driving Brand Engagement
Through The Warmth Of An Initial Chatbot Message. Journal Of Business Research , 135, 840–
850. Https://Doi.Org/10.1016/J.Jbusres.2021.03.005
Kumar,  V., Rajan ,  Bharath, Venkatesan,  Rajkumar, & Lecinski,  Jim. (2019). Understanding The
Role Of Artificial Intelligence In Personalized Engagement Marketing. California Management
Review, 61(4), 135–155. Https://Doi.Org/10.1177/0008125619859317
Kumar, S., Lim, W. M., Sivarajah, U., & Kaur, J. (2022). Artificial Intelligence And Blockchain

174    International Journal of Educational Administration, Management, and Leadership
   Volume 6, Number 2,  November 2025,  Page 154-175

Integration In Business: Trends From A Bibliometric -Content Analysis. Information Systems
Frontiers, 25, 871–896. Https://Doi.Org/10.1007/S10796-022-10279-0
Kumpulainen, M., & Sepp änen, M. (2022). Combining Web Of Science And Scopus Datasets In
Citation-Based Literature Study. Scientometrics, 127, 5613 –5631.
Https://Doi.Org/10.1007/S11192-022-04475-7
Liye, & Sun, B. (2020). Machine Learning And AI In Marketing – Connecting Computing Power To
Human Insights. International Journal Of Research In Marketing .
Https://Doi.Org/10.1016/J.Ijresmar.2020.04.005
Mariani, M., Perez‐Vega, R., & Wirtz, J. (2021). AI In Marketing, Consumer Research And
Psychology: A Systematic Literature Review And Research Agenda. Psychology & Marketing .
Https://Doi.Org/10.1002/Mar.21619
Oliveira, O., Da Silva, F. F., Juliani, F., Barbosa, L., & Nunhes, T. (2019). Bibliometric Method For
Mapping The State -Of-The-Art And Identifying Research Gaps And Trends In Literature: An
Essential Instrument To Support The Development Of Scientific Projects. Scientometrics Recent
Advances. Https://Doi.Org/10.5772/Intechopen.85856
Potwora, M., Vdovichena, O., Semchuk, D., Lipych, L., & Saienko, V. (2024). The Use Of Artificial
Intelligence In Marketing Strategies: Automation, Personalization And Forecasting. Journal Of
Management World. Https://Doi.Org/10.53935/Jomw.V2024i2.275
Sakalauskas, V., & Kriksciuniene, D. (2024). Personalized Advertising In E -Commerce: Using
Clickstream Data To Target High -Value Customers. Algorithms, 17, 27.
Https://Doi.Org/10.3390/A17010027
Saura, J. R., Ribeiro -Soriano, D., & Palacios -Marqués, D. (2021). Setting B2B Digital Marketing In
Artificial Intelligence -Based Crms: A Review And Directions For Futur e Research. Industrial
Marketing Management, 98, 161–178. Https://Doi.Org/10.1016/J.Indmarman.2021.08.006
Şenyapar, H. N. D. (2024). Artificial Intelligence In Marketing Communication: A Comprehensive
Exploration Of The Integration And Impact Of AI. Technium Social Sciences Journal .
Https://Doi.Org/10.47577/Tssj.V55i1.10651
Thakur, J., & Kushwaha, B. (2023). Artificial Intelligence In Marketing Research And Future
Research Directions: Science Mapping And Research Clustering Using Bibliometric Analysis.
Global Business And Organizational Excellence. Https://Doi.Org/10.1002/Joe.22233
Theodorakopoulos, L., & Theodoropoulou, A. (2024). Leveraging Big Data Analytics For
Understanding Consumer Behavior In Digital Marketing: A Systematic Review. Human Behavior
And Emerging Technologies. Https://Doi.Org/10.1155/2024/3641502
Toader, D.-C., Boca, G., Toader, R., Măcelaru, M., Toader, C., Ighian, D., & Rădulescu, A. T. (2020).
The Effect Of Social Presence And Chatbot Errors On Trust. Sustainability (Switzerland) , 12(1).
Https://Doi.Org/10.3390/SU12010256
Van Esch, P., & Black, S. (2021). Artificial Intelligence (AI): Revolutionizing Digital Marketing.
Australasian Marketing Journal, 29, 199–203. Https://Doi.Org/10.1177/18393349211037684
Verma, S., Sharma, R., Deb, S., & Maitra, D. (2021). Artificial Intelligence In Marketing: Systematic
Review And Future Research Direction. Int. J. Inf. Manag. Data Insights , 1, 100002.
Https://Doi.Org/10.1016/J.Jjimei.2020.100002
Vlačić, B., Corbo, L., Silva, S., & Dabić, M. (2021). The Evolving Role Of Artificial Intelligence In
Marketing: A Review And Research Agenda. Journal Of Business Research , 128, 187 –203.
Https://Doi.Org/10.1016/J.Jbusres.2021.01.055
Ziakis, C., & Vlachopoulou , M. (2023). Artificial Intelligence In Digital Marketing: Insights From A
Comprehensive Review. Inf., 14, 664. Https://Doi.Org/10.3390/Info14120664

Kahfi; Mapping the Evolution of Artificial Intelligence in Digital Marketing …|175
