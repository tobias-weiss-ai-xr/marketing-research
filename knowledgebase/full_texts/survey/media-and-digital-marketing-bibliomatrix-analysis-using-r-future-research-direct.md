---
title: 'Media and Digital Marketing: Bibliomatrix Analysis using R (Future Research Directions)'
url: https://doi.org/10.57178/paradoks.v9i2.2375
category: survey
subcategory: review
date: 2026-03
venue: PARADOKS Jurnal Ilmu Ekonomi
authors:
- Minawati Wening
- Tinik Sugiati
- Erick Karunia
source: openalex-oa
pdf_url: https://jurnal.feb-umi.id/index.php/PARADOKS/article/download/2375/1753
pages: 17
chars: 52808
fetched_at: '2026-11-08T18:53:31+00:00'
kb_version: 1
---

# Media and Digital Marketing: Bibliomatrix Analysis using R (Future Research Directions)

PARADOKS Jurnal Ilmu Ekonomi Vol. 9 No. 2, 2026
e-ISSN : 2622-6383

Paradoks: Jurnal Ilmu Ekonomi 9(2) (2026) | 186
Media and Digital Marketing: Bibliomatrix Analysis using R
(Future Research Directions)

Minawati Wening 1*, Tinik Sugiati 2 , Erick Karunia3, Shalahuddin 4
minawening.id01@gmail.com 1*
Program Studi Magister Ilmu Manajemen, Universitas Borneo Tarakan, Indonesia 1*,2,3,4

Abstract

This study aims to analyze the development of research trends on social media and digital marketing
in scientific articles indexed in the Scopus database during 2020–2025. The research uses a descriptive
quantitative approach with bibliometric methods to map patterns  of scientific publications,
researcher collaboration, and the development of research topics in the field. Research data were
obtained from the Scopus database using the PRISMA approach, yielding 544 articles that met the
inclusion criteria. Data analysis was carried out in RStudio using the Bibliometrix package and the
BiblioShiny interface to identify annual publication trends, author productivity, country contributions,
citation analysis, and research topic mapping. The results showed that publications on social media
marketing increased significantly each  year during the study period. In addition, it was found that
several countries make a dominant contribution to publications, and that there has been an increase
in international collaboration in digital marketing research. Thematic analysis also shows that topics
such as social media marketing, consumer engagement, and digital strategy are the main focus in
the scientific literature. This research contributes to understanding the direction of development in
social media-based digital marketing research. It provides a reference for academics, practitioners,
and policymakers to develop more effective digital marketing strategies in the era of digital
transformation.

Keywords: Bibliometric analysis; social media; digital marketing; Scopus; RStudio; Bibliometrix
  This work is licensed under a Creative Commons Attribution 4.0 International License.
Introduction
The development of information technology has brought significant changes to
communication patterns, social interactions, and global economic activities, especially
through social media as a strategic platform for digital marketing . Social media no longer
functions only as a means of social communication but also as an important instrument for
organizations to build brand awareness, strengthen relationships with consumers, and
increase engagement through interactive and creative content strategies. This
phenomenon is in line with rising internet penetration and changes in consume r behavior
that increasingly rely on digital technology to obtain information and conduct  economic
interactions. (Zehra & Kesharwani, 2024).  This condition shows that social media has
contributed to the shift in the conventional marketing paradigm towards more dynamic,
participatory, and technology-based digital marketing (Low et al., 2020; Rooney et al., 2021)
Several studies have highlighted the importance of digital technology in
transforming modern marketing practices. Musa et al. (2024)  show that the Technology
Acceptance Model  (TAM) remains the dominant theoretical framework in technology -
based marketing research and has experienced a significant increase in publications,
especially after 2020. Another study by Gözden et al. (2025) through a bibliometric analysis
of the Scopus article found that the core constructs of TAM , such as perceived usefulness,
perceived ease of use, and behavioral intention, remain central to the conceptual structure
of the research, despite the thematic shift towards the integration of more complex digital
technologies such as artificial intelligence and other digital platforms. In addition, Ajakaiye

Paradoks: Jurnal Ilmu Ekonomi 9(2) (2026) | 187
et al. (2025) and Akerele et al. found that the perception of technological benefits
(perceived usefulness) is the primary factor influencing users' intentions to adopt  digital
marketing technology.
Although various studies have addressed the adoption of digital technologies in
marketing and the use of TAM as an analytical framework, most studies still focus on testing
the relationships between variables in specific contexts, such as consumer behavior  or the
adoption of technology by organizations (Bhardwaj, 2021; Fain & Roberts, 1997) . The
research has not provided a comprehensive overview of the development of knowledge
structures, trends in research topics, and patterns of scientific collaboration in the field of
social media  and digital marketing  globally(Amiri et al., 2023; Ghorbani et al., 2022;
Lamberton & Stephen, 2016) . In addition, bibliometric studies that specifically map the
development of research in this field in the latest period are still relatively limited, so research
that can provide a systematic mapping of the development of scientific literature in the
field of social media and digital marketing is needed(Lamberton & Stephen, 2016; Wani,
2024).
Based on the research gaps described in the previous section, this study aims to
provide a comprehensive understanding of the development of scientific research  on
social media and digital marketing in the international academic literature. In particular,
this study asks several research questions, namely:
1. How to develop the trend of annual scientific document production in social media
and digital marketing research  during the 2020–2025 period;
2. any author who has the highest level of productivity in publishing scientific articles in the
field;
3. Which scientific articles or documents obtained the highest number of citations in the
research domains of social media and digital marketing?
4. What scientific journals show the highest level of productivity in publishing articles
related to the topic?
5. What is the proportion of article publications involving international collaboration in
social media and digital marketing research?
6. Which country had the highest level of publication productivity in the study?
7.  What are the main trends in social media and digital marketing research during the
2020–2025 period?
 By answering these questions, this study aims to systematically map the dynamics of
research development using a bibliometric approach. The novelty of this research lies in the
comprehensive mapping of social media and digital marketing research trends  in Scopus-
indexed articles in the current period 2020 –2025 using bibliometric analysis based on
Bibliometrix/BiblioShyny software, to provide a more up -to-date picture of scientific
publication patterns, research collaboration networks, and the development of research
themes in Social Media  and Digital Marketing (Bala & Verma, 2018; Krishen et al., 2021;
Lamberton & Stephen, 2016).
This study uses the Technology Acceptance Model (TAM)  as a theoretical
foundation to explain how technology is increasingly accepted and utilized in digital
marketing activities (Buvár & Gáti, 2023; Ritz et al., 2019) . TAM explained that the
acceptance of technology is influenced by two main constructs, namely perceived
usefulness and perceived ease of use , which further affect the behavioral intentions and
actual use of technology by individuals and organizations (Davis, 2014).  This framework
describes the process of how individuals or organizations accept and adopt new
technologies when they are deemed useful and easy to use. In the context of digital
marketing development, the growing use of social media as a marketing tool indicates that
digital technology is increasingly accepted and integrated into business activities. Therefore,
TAM is used in this study to provide a conceptual basis for understanding the relationship
between technology acceptance and the development of social media  studies and
digital marketing(Carlos Martins Rodrigues Pinho & Soares, 2011; Wirtz & Göttel, 2016).

Paradoks: Jurnal Ilmu Ekonomi 9(2) (2026) | 188
Analysis Method
Research Design
This study uses a descriptive quantitative approach, employing bibliometric analysis
to map the development of research on social media and digital marketing. Bibliometric
analysis is used to identify patterns of scientific publications, research trends, author
productivity, state contributions, and the development of research topics in a field of study.
This method is widely used in scientific research to sys tematically analyze the structure of
knowledge and the development of literature in a discipline (Aria & Cuccurullo, 2017;
Donthu et al., 2021).

Population and sample
This study uses purposive sampling, a non -probabilistic method that deliberately
selects units of analysis based on their relevance and suitability to  the research criteria.
According to Guarte & Barrios (2006),  Purposive sampling  is beneficial when researchers
believe that certain elements in a population can provide the most accurate and relevant
information to the research focus(Ames et al., 2019; Campbell et al., 2020). In this study, the
technique was used to select articles from the Scopus database containing the keywords
"social media" and "digital marketing" . The initial search yielded 6,187 documents, which
were then filtered gradually based on the research inclusion criteria, namely the limitation
of the 2020–2025 publication period (4,617 documents), the limitation of the subject area of
Business, Management and Accounting (2,114 documents), the type of article document
(1,245 documents), the publication stage of the final publication stage (1,143 documents),
the suitability of the main keywords of social media and digital marketing (562 documents),
journal source type (556 documents), and language restriction of English publications until
544 documents were obtained as the final sample of the research. Thus, the sample of this
study consists of 544 scientific articles that were purposively selected to ensure the analyzed
data is relevant and representative of the research objectives in examining trends in
scientific publications related to social media and digital marketing.

Data Types and Sources
The data used in this study is secondary data obtained from the Scopus database,
one of the reputable international scientific databases , which collects publications from
various academic journals around the world  (Azis et al., 2025; Chavez et al., 2022) . Data
from Scopus were chosen because it undergoes rigorous peer review and selection ,
thereby ensuring the quality, reliability, and credibility of the information used in the research.
Using this secondary data, researchers can analyze the dynamics of scientific knowledge
development without collecting primary data directly, since the information needed is
already available in publication metadata. In the context of this research, secondary data
enables researchers to objectively and quantitatively identify research trends, collaboration
patterns, and the development of research themes in the field of social media and digital
marketing, while improving research efficiency by allowing analysis of a broad,
standardized dataset.

Data collection methods
The data collection process in this study refers to the PRISMA ( Preferred Reporting
Items for Systematic Reviews and Meta-Analyses) framework developed by (Id et al., 2021).
This approach is used to ensure that the identification, screening, and selection of literature
are carried out systematically and transparently. The flow of the article selection process in
this study is presented in the following figure:
The PRISMA framework is used to explain the stages of data collection and filtering in
a structured manner , starting from identification, screening, eligibility, and  inclusion. The
initial search was conducted in the Scopus database using the keywords "social media"
AND "digital marketing," yielding  6,187 documents. Furthermore, a screening process was

Paradoks: Jurnal Ilmu Ekonomi 9(2) (2026) | 189
carried out with several screening criteria, namely restrictions on the 2020 -2025 publication
year so that there were 4,617 documents left, then screening based on the subject area of
Business, Management, and Accounting so that it became 2,114 documents, as well as
restrictions on the type of article documents , which resulted in 1,245 documents. The next
stage is a restriction on the status of the final publication, bringing the total to 1,143 articles.
At the eligibility stage, the selection process was carried out by reviewing keyword
relevance, resulting in 562 articles. Furthermore, there was a restriction  on the source type
of scientific journals, leaving 556 articles, and a restriction on the language of English
publications, which resulted in 544 articles as the final dataset of the research. All articles
that pass the inclusion stage are then deemed worthy of further analysis using bibliometric
analysis in BiblioShiny within  the RStudio environment . Methodologically, this PRISMA flow
shows that the data reduction process is carried out systematically  and transparently, and
is replicable, so that the final dataset used truly represents research on social media and
digital marketing in the 2020–2025 period in accordance with the research study's focus.

Figure 1. PRISMA Method Flowchart
Data Analysis Methods
This study uses a bibliometric approach, focusing on quantitative data analysis to
uncover patterns and trends in the scientific literature on social media as a digital marketing
medium. This approach allows researchers to assess various indicators, such as the number
of publications, author collaborations, thematic trends, and journal distribution. To support

Paradoks: Jurnal Ilmu Ekonomi 9(2) (2026) | 190
this process, RStudio software is used with the Bibliometrix package, which is an open-source
tool specifically designed for bibliometric analysis and comprehensive knowledge mapping
(Aria & Cuccurullo, 2017)

Bibliometric Analysis Procedure Using RStudio
This study uses a bibliometric approach, drawing on data from the Scopus database,
which offers broad  coverage of international indexes and complete metadata for
performance analysis and scientific mapping. The data collection process began with a
search using the keywords "social media" AND "digital marketing ," which resulted in 6,187
documents. Furthermore, a screening process was carried out based on inclusion criteria by
limiting the publication period to 2020 –2025, selecting the subject area of Business,
Management and Accounting, the artic le type, the final publication stage, the journal
source, and the English  language. After all stages of selection were implemented, 544
articles were obtained that met the research criteria and were declared worthy of further
analysis. All article metadata is then exported from Scopus as a CSV file for analysis in
RStudio.
Bibliometric analysis was conducted in RStudio using the Bibliometrix package and
the BiblioShiny graphical interface, enabling systematic analysis . Data is imported through
the Import Raw File  menu by selecting Scopus as the database source and setting the
author name format to Full Name  to maintain consistency of author identification.
Furthermore, various analyses were carried out to answer the research questions, including
Annual Scientific Production to analyze annual publication trends, Most Relevant Authors to
identify the most productive authors, Most Global Cited Documents to find out the articles
with the highest citations, and Most Relevant Sources to determine the most productive
journals. In addition, the Author Productivity (Lotka's Law) analysis was used to examine the
distribution of author productivity; Corresponding Authors' Countries and Country
Productivity were used to analyze contributions and collaborations between countries; and
the Thematic Map and Trending Topics were used to map the  development of research
themes. The results of the analysis, presented as tables, graphs, and network maps, are then
interpreted to systematically and transparently explain the dynamics of the development
of social media and digital marketing research in the 2020–2025 period.
Results and Discussion
Results
Annual Publication Growth Trends Analysis of growth rates.
Analysis of publication growth trends indicates that scientific productivity in social
media and digital marketing has fluctuated throughout the 2020–2025 period. Based on the
annual scientific production graph, the number of publications increased from 70 articles in
2020 to 75 in 2021, indicating  an initial growth of 7.14%. However, in 2022 , there was a
decrease to 67 articles, a 10.67% decline from  the previous year. This decline reflects
fluctuations in scientific productivity, although it generally does not change the direction of
research development in the medium term.
The growth trend will continue in 2023, with the number of publications reaching 90
articles, an increase of 34.33%, then rising to 104 articles in 2024,  a growth of 15.56%. By the
end of the study period, the number of publications reached an all -time high in 2025 with
138 articles, an increase of 32.69% compared to the previous year. Overall, this pattern
suggests that research on social media and digital marketing shifted from a relatively slow
initial growth phase to a stronger and more sustainable expa nsion phase during the study
period.

Paradoks: Jurnal Ilmu Ekonomi 9(2) (2026) | 191

Figure 2. Publication Growth Trends

Number of Publications per Year (2020–2025)
The quantitative presentation of the distribution of articles published each year
during the research period provides an overview of scientific productivity, based on
metadata extracted from the Scopus database and filtered through the previous selection
process.

Table 1. Number of Publications as of Year 2020–2025
Year Articles
2020 70
2021 75
2022 67
2023 90
2024 104
2025 138
   Source: RStudio data processing (2026)

The number of research publications related to social media and digital marketing
during 2020–2025 is as follows: 70 articles in 2020, 75 in 2021, 67 in 2022, 90 in 2023, 104 in 2024,
and 138 in 2025. The data illustrate the dynamics of research development in this field over
the years. In the initial observation period, namely 2020 –2021, the number of publications
increased moderately from 70 to 75 articles, indicating greater  academic attention to the
use of social media as a digital marketing instrument. However, in 2022 , the number of
publications decreased to 67 articles, suggesting a period of fluctuation in research activity.
Entering 2023, the number of publications increased significantly to 90, then rose to 104 in
2024, indicating stability and consistency in research growth in this field.
The peak in the number of publications occurs in 2025, with 138 articles, representing
a fairly sharp increase compared to the previous year. The growth rate of this study can also
be analyzed using the Compound Annual Growth Rate (CAGR) to determine the average
annual growth during the study period. Based on the number of publications , from 70
articles in 2020 to 138 in 2025, a CAGR of approximately  18.4% per year is obtained. These
results show that , on average, research on social media and digital market ing grows
significantly each year, which, in turn, confirms the increasing academic attention to these
topics, as well as  the development of digital technology and the transformation of social
media-based marketing practices (Brealey et al., 2019).

Author Productivity & Impact
The author's productivity analysis aims to identify individual contributions to the

Paradoks: Jurnal Ilmu Ekonomi 9(2) (2026) | 192
development of the literature on social media and digital marketing. In bibliometric analysis,
productivity is measured not only by the number of articles but also by the fractional
counting approach, which calculates authors' contributions by accounting for the number
of collaborators per  publication. This approach provides a more proportionate picture of
each author's level of involvement in scientific publications. Based on Table 4.2, the authors
with the highest number of articles are Carlson, Jamie L.; Krishen, Anjala S.; and Kunkel, Thilo,
each of whom produced 4 articles. However, when viewed in terms of fractionalized article
values, Kunkel, Thilo had a higher individual contribution (1.33). In contrast,  Carlson, Jamie
L., and Krishen, Anjala S. had a value of 0.76, indicating that their publications involved more
collaboration with a larger number of authors.
In the group of authors with 3 articles, the variation in fractional contributions looked
more diverse. Hodson, Jaigris, had the highest contribution score of 1.58, followed by Fusté-
Forné, Francesc (1.50), and Abell, Annika, and Kar, Arpan Kumar, each with a score of 1.33,
indicating relatively high individual involvement in their publications. In contrast, some
authors, such as Dias, Álvaro Lopes (0.78), Jacobson, Jenna (0.72), and Rahman,
Mohammad M. (0.51),  had lower fractional values, which indicates t hat the articles they
produced involved collaborations with a larger number of authors. Overall, these results
show that the productivity of authors in social media and digital marketing research is not
only determined by the number of articles produced, b ut also by the magnitude of
individual contributions in collaborative publications, thus providing a more comprehensive
picture of the role of authors in the development of literature in these fields.

Table 2. Highest Productivity Writer
No Authors Articles Articles Fractionalized
1 Carlson, Jamie L. 4 0,76
2 Krishen, Anjala S. 4 0,76
3 Kunkel, Thilo 4 1,33
4 Abell, Annika 3 1,33
5 Dias, Álvaro Lopes 3 0,78
6 Fusté-Forné, Francesc 3 1,50
7 Hodson, Jaigris 3 1,58
8 Jacobson, Jenna 3 0,72
9 Kar, Arpan Kumar 3 1,33
10 Rahman, Mohammad M. 3 0,51
   Source:Hasil olahan data Rstudio (2026)

Global Citation Analysis and Most Influential Documents
The citation analysis aims to identify the articles that make the most significant
contributions to research on social media and digital marketing. The two main indicators
used are Total Citations (TC) and Normalized Total Citations (NTC). TC shows the number of
citations an article receives. At the same time, NTC measures an article's relative impact by
accounting for citations per year and publication age . TC/Y (Total Citations per Year) is
used to assess the impact of articles each year, providing a more accurate picture of their
relevance in the current literature. Based on this analysis, the article by Dwivedi et al. (2021),
"Setting The Future of Digital and Social Media Marketing Research: Perspectives  And
Research Propositions", leads with 1,526 total citations , 254.33 citations per year , and
Normalized TC 23.49 , signaling a major impact in shaping digital marketing and social
media research frameworks.

Paradoks: Jurnal Ilmu Ekonomi 9(2) (2026) | 193
Table 3. Journal with the Highest Citation
Source: RStudio data processing (2026)

 The second position is occupied by Appel et al. (2020) with the article "The Future of
Social Media in Marketing ," which has 1,187 total citations and 169.57 citations per year,
indicating the growing relevance of social media -based marketing research. Quach
Thaichon's (2022) article, titled "Digital Technologies: Tensions in Privacy and Data", records
No Authors Title Journal Yop Total Citations Tc/Y Normalized Tc
1. Dwivedi
Setting The Future Of Digital
And Social Media Marketing
Research: Perspectives And
Research Propositions
International
Journal Of
Information
Management
2021 1526 254.33 23.49
2. Appel,  The Future of Social Media in Marketing
Journal Of The
Academy Of
Marketing
Science
2020 1187 169.57 18.43
3. Quach Thaichon Digital Technologies: Tensions In Privacy And Data
Journal Of The
Academy Of
Marketing
Science
2022 385 77.00 14.01
4. Chatterjee
Why Do Small And Medium
Enterprises Use Social Media
Marketing And What Is The
Impact: Empirical Insights From
India
International
Journal Of
Information
Management
2020 338 48.29 5.25
5. Lin
Happiness Begets Money:
Emotion And Engagement In
Live Streaming
Journal Of
Marketing
Research
2021 318 53.00 4.89
6. Sokolova
You Follow Fitness Influencers
On Youtube. However, Do You
Actually Exercise? How
Parasocial Relationships, And
Watching Fitness Influencers,
Relate To Intentions To Exercise
Journal Of
Retailing And
Consumer
Services
2021 262 43.67 4.03
7.  Jun,
What Makes Followers Loyal?
The Role Of Influencer
Interactivity In Building
Influencer Brand Equity
Journal Of
Product & Brand
Management
2020 260 37.14 4.04
8. Herhausen The Digital Marketing Capabilities Gap Industrial Marketing Management 2020 214 30.57 3.32
9. Cruz- Cárdenas
COVID-19, Consumer Behavior,
Technology, And Society: A
Literature Review And
Bibliometric Analysis
Technological
Forecasting And
Social Change
2021 205 34.17 3.16
10. Pittman
More Trust In Fewer Followers:
Diverging Effects Of Popularity
Metrics And Green Orientation
Social Media Influencers
Journal Of
Interactive
Marketing
2021 202 33.67 3.11
`11. Saima
The Effect of Social Media
Influencer Marketing on
Consumers’ Purchase Intention
And The Mediating Role of
Credibility
Journal Of
Promotion
Management
2020 193 27.57 3.00
12 Jacobson Social Media Marketing: Who Is Watching The Watchers?
Journal Of
Retailing And
Consumer
Services
2020 184 26.29 2.86
13. Harrigan Identifying Influencers on Social Media
International
Journal Of
Information
Management
2021 177 29.50 2.72
14. Dolega
Going Digital? The Impact of
Social Media Marketing on
Retail Website Traffic, Orders,
and Sales
Journal Of
Retailing And
Consumer
Services
2021 170 28.33 2.62
15 Gössling
Tourism, Technology, and ICT:
A Critical Review Of
Affordances And Concessions
Journal Of
Sustainable
Tourism
2021 170 28.33 2.62

Paradoks: Jurnal Ilmu Ekonomi 9(2) (2026) | 194
385 total citations and 77.00 citations per year , highlighting the challenges in privacy and
data in digital marketing. Chatterjee's (2020)  article, titled "Why Do Small and Medium
Enterprises Use Social Media Marketing and What Is the Impact", obtained 338 total citations
and 48.29 citations per year , providing important insights into the application of social
media in MSME marketing in India. Overall, these articles demonstrate a deeper
understanding of the role of social media in marketing and make signi ficant contributions
to digital marketing theory and practice, particularly in digital influencer marketing , data-
driven strategies, and consumer behavior.

Publications by Journal
An analysis of the journals that publish the most articles on social media and digital
marketing provides important insights into the major publication outlets in this field. The Most
Relevant Sources graph displays the top 10 journals by the number of documents indexed
in the research dataset. This visualization illustrates the author's tendency to choose
publication channels and shows how digital marketing topics are evolving across different
scientific domains. The horizontal axis shows the number of documents published, while the
vertical axis shows the name of the journal as the source of the pub lication. This graph
identifies the journals that play the most active role in disseminating research results,
providing an overview of the major publication centers in the international literature.

Figure 3. Publication Growth Trends

Based on the graph, the Journal of Retailing and Consumer Services  takes the top
spot with 22 articles, making it the most prolific source of publications in the dataset. The
dominance of this journal indicates that research on social media and digital marketing is
closely linked to consumer behavior, retail services, and the relationship between
consumers and digital platforms. Productivity was further occupied by Cogent Business and
Management and the Journal of Digital and Social Media Marketing, each with 17 articles,
both showing a strong focus on managerial, strategic, and applied aspects of  digital
marketing. This is followed by Emerald Emerging Markets Case Studies, with 14 articles, and
Technological Forecasting and Social Change, with 12 articles, which reflect perspectives
on emerging markets and the impact of technology on socio-economic systems. In addition,
Innovative Marketing and the Journal of Theoretical and Applied Electronic Commerce
Research, each with 11 articles, highlight the linkage between marketing innovation and e-
commerce. Groups with fewer publications, such as the Journal of Business Research (10
articles) and Psychology and Marketing (8 articles), demonstrated a cross-disciplinary focus
on consumer behavior and the psychological and business implications of digital marketing.
Overall, the distribution of these publications shows that social media and digital marketing
research is spread across a wide range of journals, with a diverse but concentrated focus
on the main journals that form the basis of the literature in this field.

Paradoks: Jurnal Ilmu Ekonomi 9(2) (2026) | 195
Author Productivity (Lotka’s Law Analysis)
The analysis of collaboration and author productivity in social media and digital
marketing research for the period 2020–2025 was conducted by integrating the Lotka Law
approach with collaboration analysis based on the country of origin of the corresponding
author, using the SCP (Single Country Publications) and MCP (Multiple Country Publications)
indicators. Lotka's law describes the distribution of author productivity, assuming an inverse
relationship between the number of articles published and the numbe r of authors who
produce them.
Tabel 4.  Author Productivity Distribution Table
No Documents Written N. Of Authors Proportion Of Authors Theoretical
1 1 1453 0,950294 0,70243902
2 2 64 0,041857 0,17560976
3 3 9 0,005886 0,07804878
4 4 3 0,001962 0,04390244
Figure 4. Author Productivity Through Lotka’s Law
Source: Rstudio data processing results (2026)

Based on the results of the analysis displayed in the table and graph of the
distribution of author productivity, it can be seen that the category of one publication
dominates significantly: as many as 1,453 authors, or around 95.03%, produced only one
article during the research period. This proportion is much higher than Lotka's theoretical
value of 70.24%, suggesting that the productivity structure in this field is highly concentrated
among authors with a single contribution.
In category two of publications, the number of authors decreased drastically to 64
people or around 4.19%, far below the theoretical estimate of 17.56%. A sharper decline
was observed in the categories of three publications with 9 authors (0.59%) and four
publications with 3 authors (0.20%), both well below the theoretical expectations of 7.80%
and 4.39%, respectively. The stark difference between the actual and theoretical
distributions of Lotka's data shows that the concentration of authors' productivity in this field
is even more extreme than the general pattern predicted by the theory. This indicates that
only a small percentage of authors maintained consistency in their scientific contributions
during the observation period.
The steeper slope of the actual distribution curve compared with Lotka's theoretical
curve indicates that the structure of the scientific community in the field of social media
and digital marketing has not been fully dominated by a stable,  sustainably productive
group of core authors. Most authors serve as  sporadic contributors engaged in project -
based research or temporary collaborations. These findings reflect the characteristics of the
field of social media and digital marketing, which are dynamic, interdisciplinary, and highly

Paradoks: Jurnal Ilmu Ekonomi 9(2) (2026) | 196
influenced by developments in digital technology, thus attracting broad participation from
various disciplines such as management, communication, information systems, and
entrepreneurship. Although the rate of author participation is relatively high, the consistency
and sustainability  of scientific productivity remain limited, suggesting that the research
community is still growing.

International Research Collaboration (SCP/MCP Analysis)
In addition to showing the structure of individual productivity , which is highly
concentrated among authors with one publication, the dynamics of the scientific
community in the field of social media and digital marketing can also be understood
through patterns  of international collaboration based on the country of origin of the
corresponding author. This analysis distinguishes between Single Country Publications (SCP)
and Multiple Country Publications (MCP) to assess the degree of global integration within
research networks.
 The visualisation results show that India ranks first in the number of publications, but
most of its articles fall into the SCP category, indicating  the dominance of domestic
research activities. The United States is next in terms of the number of publications, but has
a relatively higher proportion of MCPs than India, reflecting more active involvement in
international collaboration. Other countries, such as China, the United Kingdom, Australia,
and Spain, show a similar pattern : a dominance of domestic p ublications, accompanied
by moderate international collaboration.
Indonesia is in the middle group in publication productivity , with SCP dominance,
indicating that research is still developing at the national level with relatively limited
international collaboration. In contrast, some European countries , such as France,  show a
more balanced proportion of MCPs despite having fewer absolute publications, indicating
a relatively higher level of global integration. Overall, the structure of research collaboration
in the field of social media and digital marketing remains domi nated by domestic
publications, so a country's high productivity does not always align  with the intensity of its
international collaboration. These findings show that strengthening cross -border
cooperation is an important factor for improving the quality of research, enriching scientific
perspectives, and expanding the global impact of the development of literature in this field.

Publications by Country
Mapping the contributions of publications by country shows that research on social
media and digital marketing is widely distributed across regions.
Based on the data, India ranks first with 56 articles, followed by the United States
with 44 and China with 31. These three countries can be categorized as major productivity
centers in this field of study, reflecting their strong research capacity and significant
academic attention to digital transformation in marketing. Other countries , such as the
United Kingdom (24 articles), Australia (22 articles), and Spain (21 articles), have also made
significant contributions to the development of the literature in this field.
When analyzed geographically, the Asian region shows a fairly strong dominance,
with countries such as India, China, Indonesia (16 articles), Korea (12 articles), Malaysia (8
articles), and Ukraine (10 articles). This dominance is related to the rapid growth of the digital
economy, increasing internet penetration, and the development of a technology -based
business ecosystem in the region. Meanwhile, European countries such as the United
Kingdom, Spain, Portugal (16 articles), France (15 articles), and Italy  (12 articles) showed
relatively consistent contributions, reflecting a strong focus on technology-based marketing
innovation and digital transformation. In North America, the United States and Canada (11
articles) also make important contributions, with the United States not only showing high
productivity but also often having  a significant citation impact. Overall, the distribution of
this publication confirms that research on social media  and digital marketing  is growing

Paradoks: Jurnal Ilmu Ekonomi 9(2) (2026) | 197
globally, with productivity concentrated in countries with advanced digital ecosystems and
strong academic infrastructure.

Table 5.  Top Ten Most Productive Countries in Publishing

No Country Articles
1 India 56
2 Usa 44
3 China 31
4 United Kingdom 24
5 Australia 22
6 Spain 21
7 Indonesia 16
8 Portugal 16
9 France 15
10 Italy 12
11 Korea 12
12 Canada 11
13 Ukraine 10
14 Malaysia 8
Source: RStudio data processing (2026)

Thematic Map Analysis
Thematic map analysis was conducted to identify the conceptual structure and the
level of theme development in social media and digital marketing research, based on two
main dimensions: centrality and density. Centrality describes the relevance of a theme to
the overall field of study, while density indicates the maturity and strength of internal linkages
between concepts within a theme. Thus, centrality reflects the extent to which a theme is
an important part of the research network, while density indicates the theme's level of
development and conceptual structure. Based on these two dimensions, the thematic map
is divided into four quadrants, namely motor themes , basic themes , niche themes , and
emerging or declining themes.

Figure 6. Thematic Map Analysis

The results of the analysis showed that the quadrant of motor themes (centrality and
high density) was dominated by clusters themed on social networking (online), commerce,
and sales. This position indicates that research linking online social networks to commercial
activities and sales performance is a highly relevant and conceptually evolving theme.
These themes have strong connections to other topics in social media and digital marketing

Paradoks: Jurnal Ilmu Ekonomi 9(2) (2026) | 198
and demonstrate theoretical maturity and consistency in  research. Therefore, this cluster
plays a key role in research and development, particularly in leveraging digital platforms to
drive transaction and sales growth.
In the basic themes quadrant (high centrality and low density), there is a large cluster
that includes the themes of social media, marketing, and influencer marketing, which shows
a high level of relevance to the entire field of study and  can be categorized as the main
foundation of research. However, the relatively low density indicates that,  although these
themes are often the focus of research, their conceptual structure is still evolving and not
yet fully integrated. Other clusters in the same quadrant,  namely digital marketing, social
media marketing, and purchase intent, also have a fairly high level of centrality, indicating
that the relationship between digital marketing and purchase intent is a fundamental topic
often used to measure the effectiveness of digital marketing strategies. Meanwhile, in the
quadrant of niche themes  (low centrality and high density) , themes such as marketing
communications, consumer behavior, and marketing management exhibit good
conceptual maturity. However, their relevance to the overall research network is relatively
low, so they develop into more specific, in -depth studies . In the emerging or declining
themes quadrant (centrality and low density), there is a consumer decision-making theme,
indicating that these topics lack  a strong relationship or significant conceptual
development in the analyzed dataset. Overall, the thematic map shows that research in
social media and digital marketing currently tends to focus on integrating social networks
with commercial activities, with sales as the main driver  of research development . In
contrast, basic themes such as social media marketing and influencer marketing still require
a deeper strengthening of concepts and theories, to reflect the dynamics of the research
field that continues to develop with a combination of established core themes, basic
themes that are still developing, and new themes that have the potential to become the
focus of research in the future.

Trend Topic
Topic trend analysis was conducted to identify the direction of development and
dynamics of studies in the fields of social media and digital marketing , based on keyword
frequency from 2020 to 2025.

Figure 7. Trend Topic

The development of topic trends in the field of social media and digital marketing
until 2024, given that the publication data used comes from Scopus, and that  consistently
indexed articles are only available until that year. Visualization of trending topics is
generated using the Bibliometrix software with the BiblioShyny interface, where topics are
displayed based on the frequency of keyword appearances each year. If, in a given year,
the number of keyword appearances does not meet the set threshold, that year does not

Paradoks: Jurnal Ilmu Ekonomi 9(2) (2026) | 199
appear in the chart. Although the study period extends to 2025, the trend map only shows
developments up to 2024, as the following year's data is not significant enough or has not
yet been fully indexed in the database.
The theme of social media marketing shows significant dominance, with its
frequency increasing  every year. A sharp increase in 2024 indicates that this theme is
receiving more attention, as well as the growing importance of social media as a key tool
in digital marketing. Other themes, such as digital marketing, social media, and marketing,
also showed steady growth, with digital marketing in particular experiencing rapid
development, reflecting the shift of the marketing industry towards the digital era.
Consumer behavior  also appears with a fairly high frequency, indicating an increase in
research on digital marketing-related consumer behavior, especially regarding  consumer
engagement and online shopping behavior. On the other hand, the themes of tourist
behavior, tourism development, and tourist destinations appear less frequently, indicating
that, although relevant, these topics have not been the main focus of research on  social
media and digital marketing . In the 2024 to 2025 period, themes such as influencer
marketing, social media strategy, and consumer decision-making saw a significant increase
in attention, reflecting a shift toward more detailed research on how influencers and social
media strategies influence  consumer decisions. Overall, this graph shows that the field of
social media  and digital marketing  is increasingly focused on strategic , behavior -based
approaches, with social media as the primary tool for shaping consumer decisions and
enhancing digital marketing effectiveness.

Discussion
Based on an analysis of topic trends in social media and digital marketing research
from 2020 to 2025, social media marketing emerged as the dominant theme, with a
significant increase in publication frequency, especially in 2024. This reflects the increasingly
important role of social media in digital marketing strategies and strengthening consumer
engagement. In addition, the theme of digital marketing and social media also continues
to grow rapidly, signalin g a shift from traditional marketing to technol ogy-based
approaches and digital platforms. This increase in frequency suggests that research is
shifting toward a deeper understanding of social media -based marketing strategies and
consumer behavior within digital marketing.
Meanwhile, themes such as influencer marketing and social media strategy receive
greater attention in the 2024–2025 period, illustrating a shift toward more detailed research
on social media strategies and the influence of influencers on consumer behavior. On the
other hand, topics such as tourist behavior and tourism development appear less frequently,
indicating that while these topics remain  relevant, they are no longer the main focus in
digital marketing research. Overall, this trend suggests that resea rch in social media and
digital marketing is increasingly focused on a more strategic,  behavior-based approach,
with social media playing a central role in shaping purchasing decisions and the
effectiveness of digital marketing.
Conclusions and Suggestions
This study identifies a consistent increasing trend in the number of publications in the
field of social media and digital marketing during the period 2020–2025. Despite fluctuations
in 2022, overall  publications increased sharply, particularly after 2023, indicating  an
acceleration of research in this field. Findings on author productivity indicate that most
publications are single -authored, while some major authors, such as Dwivedi (2021) and
Appel (2020), make significant contributions. Mapping publication sources shows that the
Journal of Retailing and Consumer Services  is the most productive in publishing articles on
this theme. The dominant research themes are social media marketing, digital marketing,
and consumer decision -making, with international collaborations still limited to certain

Paradoks: Jurnal Ilmu Ekonomi 9(2) (2026) | 200
countries, such as the United States, India, and China.
This research makes a significant contribution to understanding the development
trends in research on  social media and digital marketing. Using a bibliometric approach,
this study mapped the growth pattern of publications, the distribution of author productivity,
and the influence of citations in the literature. These findings provide a clear picture of the
main direction and focus of research in this area  and offer insights for academics,
researchers, and practitioners to identify opportunities for further  research and
development. In addition, the results of this study can be used to formulate more
appropriate strategies in utilizing social media and digital marketing as part of broader
research in the marketing discipline.
While this study provides useful insights, there are some limitations to be aware of.
This study uses only data available in the Scopus database and covers the period 2020 –
2025, thereby limiting the analysis to publications from that period . In addition, this study
focuses more on quantitative analysis and has not examined in depth the theoretical
context or substance of each study. Therefore, further research is recommended to expand
data sources across various databases and extend the analysis period to o btain a more
comprehensive picture of long -term developments in this field. A combination of
quantitative and qualitative approaches will also provide a more holistic understanding of
the emerging topic.
Acknowledgments
The author expressed his gratitude to the Faculty of Economics, University of Borneo
Tarakan, for support in the form of academic facilities and a conducive research
environment during the preparation of this research. This support also helps the smooth
running of various stages of research, from data collection and analysis to the preparation
of this scientific article. The author also appreciates the contributions of various parties within
the faculty who have provided academic and administrative support , enabling this
research to be completed properly.
Reference
Ajakaiye, O. P. O., Ojeka-John, R., Akerele-Popoola, O. E., & Apalowo, J. T. (2025). Evaluation
of the Nigerian Media’s Development Communication Agenda in the Post -covid Era.
In Media and Communication Systems for Sustainability in Nigeria  (pp. 249 –270).
Springer.
Akerele, O. E., Azeez, A. L., Adeniyi, A., Ajakaiye, O. O. P., Ejem, A., & Ojeka -John, R. O.
(2025). Analysis of Self -Reports of Domestic Violence on Social Media by Nigerian
Women: Spiral of Silence or Spiral of Revolt. Howard Journal of Communications, 1–21.
Ames, H., Glenton, C., & Lewin, S. (2019). Purposive sampling in a qualitative evidence
synthesis: A worked example from a synthesis on parental perceptions of vaccination
communication. BMC Medical Research Methodology, 19(1), 26.
Amiri, A. M., Kushwaha, B. P., & Singh, R. (2023). Visualisation of global research trends and
future research directions of digital marketing in small and medium enterprises using
bibliometric analysis. Journal of Small Business and Enterprise Development, 30(3), 621–
641.
Aria, M., & Cuccurullo, C. (2017). bibliometrix: An R -tool for comprehensive science
mapping analysis. Journal of Informetrics , 11(4), 959 –975.
https://doi.org/https://doi.org/10.1016/j.joi.2017.08.007

Paradoks: Jurnal Ilmu Ekonomi 9(2) (2026) | 201
Azis, M. I., Karunia, E., & Loong, A. H. (2025). Mapping the intersection of financial technology
and sustainability: A bibliometric analysis using R programming language. Jurnal Ilmiah
Manajemen Kesatuan, 13(6), 5127–5140.
Bala, M., & Verma, D. (2018). A critical review of digital marketing. M. Bala, D. Verma (2018).
A Critical Review of Digital Marketing. International Journal of Management, IT &
Engineering, 8(10), 321–339.
Bhardwaj, B. R. (2021). Adoption, diffusion and consumer behavior in technopreneurship.
International Journal of Emerging Markets, 16(2), 179–220.
Buvár, Á., & Gáti, M. (2023). Digital marketing adoption of microenterprises in a technology
acceptance approach. Management and Marketing, 18(2), 127–144.
Campbell, S., Greenwood, M., Prior, S., Shearer, T., Walkem, K., Young, S., Bywaters, D., &
Walker, K. (2020). Purposive sampling: complex or simple? Research case examples.
Journal of Research in Nursing, 25(8), 652–661.
Carlos Martins Rodrigues Pinho, J., & Soares, A. M. (2011). Examining the technology
acceptance model in the adoption of social networks. Journal of Research in
Interactive Marketing, 5(2–3), 116–129.
Chavez, H., Albornoz, M. B., & Martín, F. (2022). Big data Research: A Bibliometric Analysis of
the Scopus Database, 2009–2019. Journal of Scientometric Research, 11(1), 64–78.
Davis, F. D. (2014). Information Technology Introduction. 13(3), 319–340.
Donthu, N., Kumar, S., Mukherjee, D., Pandey, N., & Lim, W. M. (2021). How to conduct a
bibliometric analysis: An overview and guidelines. Journal of Business Research , 133,
285–296.
Fain, D., & Roberts, M. Lou. (1997). Technology vs. consumer behavior: the battle for the
financial services customer. Journal of Direct Marketing, 11(1), 44–54.
Ghorbani, Z., Kargaran, S., Saberi, A., Haghighinasab, M., Jamali, S. M., & Ale Ebrahim, N.
(2022). Trends and patterns in digital marketing research: bibliometric analysis. Journal
of Marketing Analytics, 10(2), 158–172.
Gözden, Y. D. E. N., Ri, G., Şletme, L. I., Pazarlama, V. E., Teratüründe, L. I., In, T. A. M., Bli, B.
I., & Anali, Y. K. (2025). REVISITING THE TECHNOLOGY ACCEPTANCE MODEL IN THE AGE
OF ARTIFICIAL INTELLIGENCE  : A BIBLIOMETRIC ANALYSIS OF TAM IN BUSINESS AND
MARKETING LITERATURE. 10(2), 497–517. https://doi.org/10.54452/jrb.1615746
Guarte, J. M., & Barrios, E. B. (2006). Estimation under purposive sampling. Communications
in Statistics-Simulation and Computation, 35(2), 277–284.
Krishen, A. S., Dwivedi, Y. K., Bindu, N., & Kumar, K. S. (2021). A broad overview of interactive
digital marketing: A bibliometric network analysis. Journal of Business Research , 131,
183–195.
Lamberton, C., & Stephen, A. T. (2016). A thematic exploration of digital, social media, and
mobile marketing: Research evolution from 2000 to 2015 and an agenda for future
inquiry. Journal of Marketing, 80(6), 146–172.
Low, S., Ullah, F., Shirowzhan, S., Sepasgozar, S. M. E., & Lin Lee, C. (2020). Smart digital

Paradoks: Jurnal Ilmu Ekonomi 9(2) (2026) | 202
marketing capabilities for sustainable property development: A case of Malaysia.
Sustainability, 12(13), 5402.
Musa, H. G., Fatmawati, I., Nuryakin, N., & Suyanto, M. (2024). Marketing research trends
using technology acceptance model ( TAM ): a comprehensive review of researches
( 2002 – 2022 ). Cogent Business & Management , 11(1).
https://doi.org/10.1080/23311975.2024.2329375
Ritz, W., Wolf, M., & McQuitty, S. (2019). Digital marketing adoption and success for small
businesses: The application of the do -it-yourself and technology acceptance models.
Journal of Research in Interactive Marketing, 13(2), 179–203.
Rooney, T., Krolikowska, E., & Bruce, H. L. (2021). Rethinking relationship marketing as
consumer led and technology driven: propositions for research and practice. Journal
of Relationship Marketing, 20(1), 42–61.
Wani, J. A. (2024). The current research landscape in digital marketing scientific literature in
libraries: exploration through performance and science mapping. Digital Library
Perspectives, 40(1), 35–52.
Wirtz, B. W., & Göttel, V. (2016). Technology acceptance in social media: Review, synthesis
and directions for future empirical research. Journal of Electronic Commerce Research,
17(2), 97.
Zehra, S., & Kesharwani, S. (2024). Social Media Marketing: A Bibliometric Analysis. Global
Journal of Enterprise Information System. https://doi.org/10.1186/s43093-025-00465-2
