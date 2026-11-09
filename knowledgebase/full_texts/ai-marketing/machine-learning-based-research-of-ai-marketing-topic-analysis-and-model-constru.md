---
title: 'Machine learning-based research of AI marketing: topic analysis and model construction'
url: https://doi.org/10.1186/s43093-025-00686-5
category: ai-marketing
subcategory: framework
date: 2025-11
venue: Future Business Journal
authors:
- Haofen Xie
- Yuankun Nie
- Li Liu
source: openalex-oa
pdf_url: https://fbj.springeropen.com/counter/pdf/10.1186/s43093-025-00686-5
pages: 23
chars: 104297
fetched_at: '2026-11-08T19:04:47+00:00'
kb_version: 1
---

# Machine learning-based research of AI marketing: topic analysis and model construction

Xie et al. Future Business Journal          (2025) 11:272
https://doi.org/10.1186/s43093-025-00686-5
RESEARCH Open Access
© The Author(s) 2025. Open Access  This article is licensed under a Creative Commons Attribution 4.0 International License, which
permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the
original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or
other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line
to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory
regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this
licence, visit http:// creat iveco mmons. org/ licen ses/ by/4. 0/.
Future Business Journal
Machine learning-based research
of AI marketing: topic analysis and model
construction
Haofen Xie1, Yuankun Nie1*, Li Liu2 and Yang Chen1
Abstract
Artificial intelligence (AI) has emerged as a transformative force in the marketing landscape, significantly altering
consumer engagement, decision-making processes, and strategic management practices. However, despite the sub-
stantial expansion of research on AI in marketing, a comprehensive and systematic understanding of its underlying
knowledge structure and the evolution of its thematic domains remains insufficient. Therefore, we synthesize qualita-
tive insights with bibliometric science mapping by applying CiteSpace and latent Dirichlet allocation (LDA) topic
modeling to 564 Web of Science Core Collection articles (2019–May 2025). The analysis yields three core findings.
First, China and the USA anchor the field’s knowledge production, with the UK, Australia, and India as secondary hubs.
Second, LDA reveals five topics: (1) Digitalization Transformation and Marketing Strategy, which explores the impact
of digital technologies on reshaping traditional marketing approaches; (2) Consumer Behavior and Experience, focus-
ing on how AI influences consumer decision-making and engagement; (3) Business Value and Innovation Research,
examining how AI contributes to business value creation and the development of innovative marketing practices;
(4) Machine Learning Algorithms and Technological Applications, addressing the technical foundations and practi-
cal implementations of AI in marketing; and (5) Generative AI Content and Applications, highlighting the emerging
role of generative AI in content creation and personalization. Third, we develop an integrative value chain framework
that explicates how AI permeates and transforms distinct stages of the marketing process, offering a holistic perspec-
tive on AI’s role in modern marketing practices. Building on these results, we advance a dual co-evolutionary frame-
work—Consumer–Technology–Market and Technology–Economy–Society—that consolidates dispersed streams,
clarifies the field’s intellectual structure. For managers, we map the AI–marketing technology landscape, identify high-
yield opportunities in customer experience and service automation, and delineate risks involving data privacy, bias,
and ethical guardrails, thereby informing effective and responsible adoption of AI in marketing strategy.
Keywords Artificial intelligence marketing, Scientometric techniques, Latent Dirichlet allocation (LDA), Topic
modeling, Big data, AI
Introduction
The “ Artificial Intelligence Index Report 2025” released
by Stanford University indicates that the number of pat -
ent applications related to artificial intelligence (AI) has
shown an explosive growth trend. From 2010 to 2023,
the number of these patents rose sharply from 3833 to
122,511, achieving continuous growth. In 2024 alone, the
growth rate of AI patents reached 29.6%. The data reveal
that as of 2023, China’s share of the total number of AI
*Correspondence:
Yuankun Nie
zz0734@ynufe.edu.cn
1 Yunnan University of Finance And Economics, Kunming, China
2 China University of Mining and Technology, Xuzhou, China

Page 2 of 23Xie et al. Future Business Journal          (2025) 11:272
patent authorizations was as high as 69.7%, ranking first
in the world. At present, scientific research on AI is in a
stage of rapid development, and its commercial applica -
tions also demonstrate strong growth potential. Recent
years, the penetration rate of AI technology in the busi -
ness sector has increased significantly. According to
“The state of AI: How organizations are rewiring to cap -
ture value” released by McKinsey and Company in 2025,
the investment of the AI sector in the USA has reached
$109.1 billion in 2024, with generative AI investments
amounting to $33.9 billion, reflecting a year-on-year
increase of 18.7%.
In terms of practical application, enterprises like Nike
use AI technology in their Training Club app to offer
personalized training suggestions and product recom -
mendations, effectively boosting customer engagement
and sales. Amazon employs AI to analyze data such as
user browsing and purchase history to build a personal -
ized shopping experience. Its intelligent recommendation
system can optimize product recommendations in real
time based on user behavior data, significantly improving
conversion rates and average order value. The “ Auto Ads”
tool developed by Google helps advertisers optimize ad
placement and improve ad effectiveness through contin -
uous machine learning.
Simultaneously, AI technology has garnered significant
attention within the academic community, particularly
for its innovative applications in marketing. One notable
area is the integration of AI and human–machine inter -
action to enhance service delivery [40]. Research has
explored how AI-driven chatbots influence consumer–
brand relationships by offering personalized interac -
tions, enhancing information accessibility, entertainment
value, and customization [13]. Additionally, the degree of
anthropomorphism in AI robot assistants’ appearances
has been shown to significantly affect consumers’ will -
ingness to purchase products [68]. Consumers’ aversion
to AI applications, however, varies across product cat -
egories, reflecting the complex nature of AI acceptance
to consumers [83]. Moreover, AI’s ability to optimize
processes, enhance automation, and improve organiza -
tional transformations—including predictive analytics
and human interaction—has proven effective in reduc -
ing operational costs [17, 81]. These advancements also
facilitate the development of data-driven marketing strat-
egies [48]. For both businesses and researchers, an objec -
tive and critical analysis of existing knowledge is crucial
for identifying gaps and enhancing productivity [65]. As
AI’s role in marketing deepens, academic research in this
domain has expanded, offering more sophisticated and
intelligent solutions for marketing functions [14, 79].
Although applications of artificial intelligence (AI) in
marketing are expanding at pace, the field faces several
binding constraints that limit cumulative knowledge and
responsible practice. Model performance remains tightly
coupled to data availability, representativeness, and gov -
ernance; errors in accuracy and labeling, as well as drift
and bias, undermine reliability and portability across
contexts [35]. At the same time, large-scale collection and
linkage of consumer data heighten privacy risk and ethi -
cal exposure, eroding trust and prompting resistance to
AI-enabled initiatives [80]. A further concern is organi -
zational: Growing dependence on algorithmic decision
support can narrow marketers’ exploration sets and inad-
vertently crowd out strategic creativity and judgment,
particularly when incentives anchor on short-horizon,
optimization-based metrics [50]. Furthermore, current
research in the field of AI marketing is primarily focused
on qualitative studies. Much of the evidence base relies
on manual, qualitative coding schemes that are difficult
to replicate and scale across rapidly proliferating subdo -
mains [40]. Objective, reflective analyses are crucial to
evaluate any extant knowledge base, identify knowledge
gaps, and evaluate research effectiveness and productiv -
ity. For both researchers and publication outlets, such as
journals, where and how scholars choose to publish are
critical components of the marketing discipline’s identity.
These decisions reflect the field’s value systems, aspira -
tions, paradigms, reward structures, cultural norms,
and political hierarchies [40]. As a result, the field lacks
a comprehensive, quantitative analysis of its intellectual
structure, evolutionary pathways, and emergent frontiers
[63].
To address these gaps, we undertake a data-driven
synthesis of the AI-in-marketing literature over the past
5  years, integrating scientometric network analysis with
probabilistic topic modeling. Specifically, we employ Cit -
eSpace to map co-citation and keyword co-occurrence
structures and use Latent Dirichlet Allocation (LDA) to
surface coherent thematic clusters and their temporal
dynamics. This design mitigates subjectivity inherent in
purely qualitative reviews, yields a reproducible portrait
of the field’s knowledge base and trajectories, and ena -
bles early identification of underexplored questions at the
intersection of value creation, boundary conditions, and
ethical governance.
We use two complementary methods to analyze the
research progress and research directions in this field.
First, in order to identify the dominant and prominent
topics, we use machine learning and natural language
processing algorithms to analyze the information about
the identified relevant literature in the field, including
topic modeling techniques that have gained popularity in
recent years, and then perform topic modeling. Then, we
use scientometric techniques to sort out the research on
artificial intelligence marketing in the past 5 years, trying

Page 3 of 23
Xie et al. Future Business Journal          (2025) 11:272

to explore: (1) What is the current status of research in
the field of artificial intelligence marketing? (2) What are
the research hotspots in artificial intelligence marketing
in recent years and what are the future research trends?
(3) Which countries and journals have greater influence
in the field of artificial intelligence marketing?
This study has three major contributions. First, we inte-
grate narrative synthesis with science mapping and topic
modeling to provide a transparent and replicable por -
trait of AI in marketing. By measuring co-citation and
co-occurrence networks with probabilistic topic mod -
els, our approach moves beyond frequency counts and
mitigates the selection and coding subjectivity that often
accompanies purely narrative or manual bibliometric
reviews. Second, the topic modeling results reveal five
robust thematic domains that structure the field’s current
discourse on AI and marketing. These domains delineate
where knowledge has accumulated, where boundaries
and contingencies remain unsettled, and where promis -
ing research frontiers are emerging. Third, leveraging sci-
entometric techniques, we map the intellectual base and
trajectory of the literature—covering journal and article
co-citation structures, keyword co-occurrence network
and burst dynamics, and the conceptual anchors that
have scaffolded theorizing to date. This evidence clarifies
the field’s mechanisms of value creation, boundary con -
ditions, and governance concerns, thereby sharpening
directions for cumulative theory building. Collectively,
these contributions advance theory by synthesizing
fragmented streams into a coherent structure and by
specifying targeted avenues for mechanism-focused,
contingency-aware, and governance-relevant research.
For practice, our science-based map of the AI marketing
landscape informs managerial choices about capability
investment, customer-experience design, and responsible
deployment under data privacy and ethical constraints.
In the second part, we organize the literature review, in
the third part, we explain the specific research methods,
in the fourth part, we review the main research topics in
the field of artificial intelligence marketing, and in the
fifth part, we explain the results of scientometric tech -
niques. Finally, we put forward specific suggestions for
the problems found in the research.
Literature review
Artificial intelligence marketing
The concept of artificial intelligence (AI) was first for -
mally introduced by John McCarthy at the Dartmouth
Conference in 1956 [5]. This technology aims to simu -
late human thinking patterns and cognitive functions
through computer systems and produce human-like
intelligence [54]. With the development of technology,
AI is increasingly applied across various industries, and
its empowering tools are widely favored by professionals
[78]. In the field of marketing, AI also shows significant
application value. As an emerging research field, AI mar -
keting is still in the exploratory stage, and there is no con-
sensus on its definition [27]. Researchers like Rekha et al.
(2016) define it as “a form of direct marketing that opti -
mizes marketing activities using databases and machine
learning technologies” [71], while Overgoor et al. (2019)
describe it as an intelligent process where “ AI agents pro-
pose marketing suggestions or actions based on real-time
database information to achieve optimal marketing out -
comes” [66].
By synthesizing the extant academic literature, we con -
ceptualize AI marketing as a strategic capability derived
from the integration of core computational technolo -
gies (e.g., big data analytics and machine learning) with
a suite of enabling technological infrastructures, includ -
ing the Internet of Things (IoT), virtual reality (VR), and
advanced robotics. The primary objective of this capa -
bility is to augment corporate marketing efficiency and
performance, with the ultimate goal of facilitating value
co-creation between the firm and its consumers [32].
Accordingly, the dyadic relationship between the firm
and the consumer remains the central focus of the major-
ity of scholarly inquiry within this domain.
Artificial intelligence marketing subjects: enterprises
Technological innovation often leads to fundamental
transformations in business models, and AI’s empower -
ment of marketing capabilities is no exception [52]. In
an increasingly data-driven marketing environment, the
continuous improvement of AI technology has become
a key factor for enterprises to maintain their competitive
advantage [73]. Moradi and Dass (2022) pointed out that
businesses in the marketing industry widely agree the
significant value of AI in improving performance [60].
AI’s advanced computational capabilities significantly
enhance efficiency by streamlining operations and ena -
bling data-driven decision-making. As highlighted by
Yang et  al. (2021), AI’s ability to analyze and mine con -
sumer data—such as accurately identifying target audi -
ences, optimizing information delivery, selecting the
most effective channels, and timing engagement—can
greatly enhance consumer experiences [84], such as accu-
rate identification of target audiences, optimization of
information delivery, selection of optimal channels, and
grasping the best timing, can greatly improve consumer
experiences.
Additionally, the diversified functions generated by
the combination of AI systems with machine learning
can effectively reduce the impact of negative brand fac -
tors [4], accurately predict key events [25], optimize
cost-effectiveness ratios [18], and enhance the quality

Page 4 of 23Xie et al. Future Business Journal          (2025) 11:272
of strategic decisions [77]. Artificial intelligence (AI)
accelerates digital transformation by automating stra -
tegic tasks, enhancing decision-making, and improving
organizational agility. By optimizing data-driven work -
flows, AI enables faster and more accurate decisions,
thereby boosting competitive advantage. It reshapes
organizational routines by automating routine tasks,
allowing managers to concentrate on higher-value activi -
ties. Moreover, AI fosters innovation, helping companies
quickly adapt to market changes, which, in turn, influ -
ences their competitive positioning and facilitates the
creation of personalized business models. Additionally,
enterprises can leverage big data and AI technologies to
actively drive digital transformation, exploring new gov -
ernance mechanisms for inter-enterprise cooperation
and value creation. This dynamic process model of digital
transformation is structured around the cognitive—strat-
egy positioning—strategy implementation framework.
However, existing research has the following limitations:
First, there is an excessive focus on AI’s role in assisting
corporate marketing decisions, especially the impact on
cost-effectiveness and brand development. Second, there
is a lack of exploration into the application differences
among various types of businesses and industries. Third,
there is a lack of in-depth analysis of AI marketing strate-
gies in specific contexts. Finally, there is a lack of system -
atic research on the long-term impacts of AI technology
on marketing, such as changes in workforce structure
and changes in corporate innovation capabilities.
Artificial intelligence marketing subjects: consumers
In promotional activities, AI technology provides crucial
support for marketers. Studies have shown that AI can
significantly enhance marketing efficiency, deepen cus -
tomer feature insights, and achieve highly personalized
marketing experiences [23]. Existing academic research
has confirmed that both the design of physical robots
[53] and the shaping of virtual robot personas [28] can
effectively increase consumers’ shopping affinity, thereby
influencing their purchasing decisions.
From the perspective of human–computer interac -
tion, scholars have focused on how two primary modes
(text interaction mode and voice interaction mode) affect
consumers. Hoy (2018) pointed out that voice assistants
can significantly facilitate the formation of purchase deci-
sions by meeting consumers’ information retrieval and
shopping needs [36]. Many studies indicate that emo -
tional factors in AI play a critical role in the consumer
decision-making process. Consumers tend to choose AI
technologies with a higher degree of humanization, and
their purchasing decisions are often based on brand pref -
erence and user experience [3]. However, the concept
of “uncanny valley” proposed by Mori (1970) deserves
attention: When consumers face highly human-like but
not completely human robots, they may feel repulsive
[62]. This psychological reaction can cause consumer
attitudes to suddenly change from approval to disgust,
which has a negative impact on purchasing decisions.
Recent research by Chaturvedi et  al. (2024) suggested
that this problem can be effectively alleviated by design -
ing comprehensive AI companions with functionality,
emotionality, and conversational abilities [10].
The Technology Acceptance Model (TAM), as a classic
theoretical framework for explaining technology accept -
ance behavior, has been widely applied in the field of
AI marketing. Studies have shown that TAM effectively
explains consumers’ willingness to accept AI-powered
products through its core constructs of perceived useful -
ness and perceived ease of use [75]. In the context of B2B
marketing, TAM has been instrumental in identifying
the cognitive foundations of marketers’ adoption of AI,
revealing how businesses perceive the commercial value
brought by AI technology [60]. Notably, researchers
have found that TAM needs to be combined with other
theories to better explain the complex consumer behav -
ior in AI marketing environments. For instance, some
studies have integrated TAM with the AIDA (Attention-
Interest-Desire-Action) model, finding that market -
ing communications, as an external factor, significantly
influence consumers’ perceptions of AI applications in
terms of both perceived usefulness and ease of use [76].
The Unified Theory of Acceptance and Use of Technol -
ogy (UTAUT) and its extended model, UTAUT, demon -
strate even stronger explanatory power in AI marketing
research. Research indicates that UTAUT outperforms
traditional models in explaining the acceptance of AI
applications [75]. By expanding the UTAUT model to
include new variables such as technology anxiety and
consumer trust, researchers have captured a more com -
prehensive picture of consumers’ behavioral motiva -
tions for using AI applications [7]. Empirical studies in
the domains of mobility, home, and health have shown
that, aside from security factors, all additional UTAUT
extension factors play a significant role in explaining con-
sumers’ behavioral intentions and usage behaviors [26].
These extensions, including hedonic motivation, price
value, and habit, reflect the diverse characteristics of AI
technology applications. Dual-process cognitive theory
provides an important perspective for understanding
consumer decision-making in AI marketing. Research
indicates that consumer acceptance of AI devices fol -
lows a three-stage acceptance generation process: pri -
mary evaluation, secondary evaluation, and outcome
stages [34]. During this process, consumers engage in
both rational performance evaluations and are influenced
by emotional factors. Specifically, social influence and

Page 5 of 23
Xie et al. Future Business Journal          (2025) 11:272

hedonic motivation positively affect performance expec -
tations, while anthropomorphic features influence effort
expectations. These two types of expectations jointly
determine consumers’ emotional responses, ultimately
influencing their acceptance of AI device usage.
Current research in AI marketing reveals several sig -
nificant limitations that warrant further investigation.
First, there is a notable gap in understanding the intrinsic
mechanisms that connect consumer attitudes, behavio -
ral intentions, and actual consumption behavior. While
much of the existing literature focuses on surface-level
correlations, there is a lack of comprehensive models that
explain how these factors dynamically interact to influ -
ence consumer decision-making. Second, comparative
studies across different cultural contexts are scarce. As AI
marketing strategies increasingly transcend geographi -
cal boundaries, understanding how cultural differences
shape consumer responses to AI-driven marketing prac -
tices is essential. Third, existing research often addresses
isolated topics, without establishing a cohesive theoreti -
cal framework. A systematic literature review is needed
to consolidate these fragmented studies, offering a more
integrated perspective on AI marketing and helping
scholars better grasp the evolving research direction in
this field.
Analysis methodology
Methodology
Based on the research methods of predecessors [63], this
study intends to analyze the main research topics of arti -
ficial intelligence in the field of marketing through topic
modeling and scientometric techniques, and to reveal
the research hotspots and key issues in the discipline by
quantitatively analyzing the characteristics of publica -
tions on specific topics, and to track the evolution trend
of research topics. In topic modeling, Latent Dirichlet
Allocation (LDA) is used, which is an unsupervised topic
modeling technology based on Bayesian statistics. Its
core function is to mine potential topic structures from
text data [ 41]. LDA can not only solve the high-dimen -
sional sparsity problem in traditional vector space mod -
els, but also solve the problem of multiple words with the
same meaning by assigning synonyms to the same topic
[57]. The scientometric techniques of this article are pro -
vided by CiteSpace’s systematic analysis of data such as
the distribution of publications, citation patterns, and
keyword co-occurrence provides a scientific basis for
the visualization and regularity summary of discipline
development dynamics [19]. CiteSpace is a multivariate,
time-sharing, and dynamic citation visualization analysis
software that focuses on analyzing the potential knowl -
edge contained in scientific literature and was developed
in the context of scientometrics, data, and information
visualization [43].
Data source
The data for this study are sourced from the Web of Sci -
ence database, which includes influential academic jour -
nals and conference papers globally. To systematically
examine the latest research advancements in the field of
AI marketing, a literature search was conducted based on
the WOS core database.
The Web of Science (WoS) Core Collection was
selected as the sole database for the literature retrieval
in this study. This decision was made based on both the
database’s academic rigor and its suitability for interdis -
ciplinary topics such as artificial intelligence (AI) and
marketing. WoS is widely recognized for its selective
inclusion of peer-reviewed journals and its standardized
bibliographic information, which ensure the reliability
and replicability of bibliometric analyses. In contrast,
while Scopus also provides broad coverage, previous
comparative studies have shown a high degree of overlap
between WoS and Scopus in the fields of business, man -
agement, and computer science, suggesting that WoS
alone can sufficiently represent the core literature base
[59]. Furthermore, WoS offers more consistent citation
data and advanced analytical tools, which are essential for
mapping knowledge structures and identifying emerging
trends in AI marketing research. Therefore, restricting
the data source to WoS enhances both data consistency
and analytical robustness while minimizing duplication
and noise from non-peer-reviewed materials that are
often found in other databases such as Google Scholar.
In this research, we primarily focused on the element of
marketing about AI [29]. Then, we based on the method
of constructing search formulas proposed by Professor
Chen Chaomei [11], the search formula was determined
as follows: TS = (“ AI marketing” OR “ AI in marketing” OR
“ AI and marketing” OR “ AI for marketing” OR “market -
ing and AI” OR “marketing with AI” OR “ AI for market -
ing” OR “marketing with AI” OR “ AI marketing” OR “ AI
in marketing” OR “ AI and marketing” OR “ AI for mar -
keting” OR “marketing and AI” OR “marketing with AI”
OR “ AI for marketing” OR “marketing with AI”) AND
DT = (Article) AND LA = (English).
A search was conducted within the Web of Science
Core Collection for publications related to AI market -
ing from January 1, 2019, to early May 2025. As data
collection ended in early May 2025, the number of docu -
ments for that year may be fewer than in previous years.
An initial set of 4129 relevant documents was obtained.
After manual screening, the literature in non-marketing
fields, such as finance, investment, and human resources
(including terms such as “labor market” and “capital

Page 6 of 23Xie et al. Future Business Journal          (2025) 11:272
market”), were excluded. We only retained articles rel -
evant to the theme of marketing (Fig.  1). The focus was
narrowed to English articles. Finally, 2056 qualified litera-
ture were selected as research samples [42].
We delimit the time boundary to January 2019–May
2025. The lower bound (2019) is chosen to capture the
modern phase of AI diffusion into marketing, marked by
national policy initiatives and a step-change in industry
expansion. In the USA, Executive Order 13859 launched
the American AI Initiative, and the 2019 update to the
National AI R&D Strategic Plan articulated federal prior -
ities. In China, official statistics report a ¥510 billion core
AI industry with more than 2600 enterprises by year-end
2019 and ¥770 billion by the first half of 2020, indicating
a clear post-2019 acceleration. The upper bound (May
2025) reflects our data-retrieval cutoff to ensuring timeli-
ness, transparency, and reproducibility.
In order to increase the specificity of the search, we
systematically organized the dataset and chose articles in
peer-reviewed international journals (564 out of 2056).
These journals represent the latest and most influential
journals in the field (Table  1). Finally, we downloaded
metadata for these 564 articles, which include print fea -
tures, authors’ names, corresponding authors’ countries,
total number of publications, citation counts with total
citations, average article citations, number of citing arti -
cles with and without self-citations, journal sources, key -
words, countries and regions, and author-level metrics
(e.g., h-, m-, and g-indices).
Research subjects analysis
Table 1 presents the results of the visualization analysis
of the national cooperation network. The analysis param-
eters are set as follows: time slice length of 1 year, g-index
(k = 25), LRF = 2.5, L/N = 10, LBY = 5, and e = 1.0. The
g-index is a metric used to assess the academic impact
of scholars or publications. It is defined as follows: If
a scholar has ’g’ papers, and each of these ’g’ papers has
been cited at least ’g’ times, then the scholar’s G-index is
’g. ’ The Link Retaining Factor (LRF) controls the density
Recordsi dentifiedf rom:
Webo fS cience (n =4132)
Recordsr emoved before screening:
Duplicater ecords removed( n
=2)
Recordss creened by thet itle and
abstract (n =4129)
Recordse xcludedN on-marketing
relateda rticles( finance, investment,
humanr esources)(n =2,073)
Reports assessedf or eligibility( n
=2056)
Reportse xcluded:
Articlesi n non-peer-reviewed
journals (n= 1492)
Studies included in article( n= 564)
IdentificationScreeningIncluded
Fig. 1 Literature screening process based on the PRISMA process

Page 7 of 23
Xie et al. Future Business Journal          (2025) 11:272

of links within a network. When constructing a co-cita -
tion network in CiteSpace, the LRF determines the pro -
portion of links to be retained when calculating the
co-citation strength between nodes. A higher LRF value
results in more retained links and a denser network. L/N
(Links per Node) represents the average number of links
per node. This parameter is used to control the connec -
tivity of the network. Similar to LRF, it more directly lim-
its the number of links from the perspective of each node.
LBY (Look Back Years) is the look-back period, which
controls the time window for detecting burst terms. In
CiteSpace, ’e’ typically refers to a parameter within the
calculation of network centrality, particularly related to
Betweenness Centrality [43].
Figure  2 displays 84 nodes and 233 connecting lines,
with each node representing a country. The depth of the
node color reflects the closeness of cooperation between
countries in recent years, while the size of the node is
proportional to the number of papers published by that
country. It can be observed that a total of 84 countries
or regions have published research papers related to AI
marketing. The USA ranks first with 154 publications,
followed by China with 153.
In terms of publication patterns, a research network
has formed primarily led by the USA and China, with
active participation from the UK, Australia, India,
France, Germany, Spain, and Italy. The research output
of China and the USA in this field is similar, ranking
Table 1 Conceptualization of artificial intelligence marketing in this paper
Key Details
Retrieval time May 8, 2025
Data source Web of Science core database—SCI,SSCI
Retrieval Topic TS = (artificial intelligence marketing OR artificial intelligence in marketing
OR artificial intelligence and marketing OR artificial intelligence for marketing
OR marketing and artificial intelligence OR marketing with artificial intel-
ligence OR artificial intelligence for marketing OR marketing with artificial
intelligence OR AI marketing OR AI in marketing OR AI and marketing OR AI
for marketing OR marketing and AI OR marketing with AI OR AI for market-
ing OR marketing with AI OR artificial intelligence purchase OR AI purchase
OR artificial intelligence consumption OR AI consumption)
Time Zone January 2019–May 2025
Screening 1.Reasearch direction is limited and related to artificial intelligence marketing
2.Publishing journal related to marketing
3.CiteSpace weight removal function
Search Results 564 valid reference, including 12,952 citations
Fig. 2 Countries’ co-occurring network

Page 8 of 23Xie et al. Future Business Journal          (2025) 11:272
first and second in the world, respectively. A deeper
analysis reveals that the research advantages of the
USA mainly come from some aspects. Firstly, the fed -
eral government continues to regard scientific and
technological innovation as a national strategic priority,
creating a favorable policy environment for AI market -
ing research and ensuring long-term and stable capital
investment.
Secondly, the USA possesses a world-leading reser -
voir of AI talent, providing solid intellectual support and
technical assurance for related research. China’s rapid
development in recent years has benefited from multi -
ple factors. On the one hand, the central government has
established AI as a national strategic priority through
policy documents such as the “New Generation Artificial
Intelligence Development Plan, ” formulated a clear devel-
opment roadmap, and guided the industry, academia, and
research to increase R&D investment. On the other hand,
the rapid growth in domestic market demand for intel -
ligent and personalized services provides strong mar -
ket-driven momentum for AI marketing research。The
immense domestic market size and unparalleled access
to vast user datasets in both countries provide a critical
advantage for developing and validating sophisticated
AI marketing models, thereby fostering the continuous
emergence of relevant academic achievements.
In contrast, countries such as the UK, Australia, and
India, while being significant contributors, form a dis -
tinct second tier. The UK and Australia, with their strong
traditions in academic research, produce high-quality
studies but may be constrained by a smaller scale of
industrial application and market size compared to the
U.S. and China. India, with its rapidly growing IT sec -
tor and talent pool, shows significant potential. However,
its research output in this specific domain may reflect a
developmental stage that is still in not maturing in terms
of foundational AI research investment and industry-aca-
demia collaboration on the same scale as the two leading
nations. This geopolitical and techno-economic context
provides a deeper explanation for the observed distribu -
tion of scholarly output in AI marketing.
The dominance of the USA and China in AI marketing
research can be better understood through the lens of
national innovation systems (NIS) theory, which empha -
sizes the interaction between government, industry, and
academia in driving innovation. In the USA, federal poli -
cies prioritize scientific and technological innovation,
creating a favorable environment for AI research. Sig -
nificant R&D investments, tax incentives, and a business-
friendly regulatory framework support the development
and commercialization of AI technologies, fostering close
collaboration between industry giants such as Google
and leading academic institutions.
Similarly, China’s rapid progress in AI marketing is
largely driven by the government’s strategic focus on
AI, as outlined in the "New Generation Artificial Intelli -
gence Development Plan." This policy-driven ecosystem,
coupled with the country’s vast consumer market and
extensive data access, propels China’s leadership in AI
marketing. NIS theory highlights the role of government
policy in shaping innovation, particularly in emerging
sectors like AI. Differences in intellectual property (IP)
regimes and regulatory approaches further differentiate
the research focus in the U.S. and China. The U.S. has a
robust IP system that incentivizes private sector innova -
tion, although it may limit access to AI models and data.
In contrast, China’s more flexible IP regime and gov -
ernment support for open-source initiatives foster col -
laboration and innovation in AI marketing. Additionally,
while the U.S. regulatory environment promotes rapid AI
development, China’s more centralized approach ensures
that AI applications align with national priorities, par -
ticularly in the consumer data space.
In conclusion, integrating NIS theory and examining
the role of IP and regulatory frameworks provides deeper
insight into how national policies shape the direction of
AI marketing research, with the U.S. and China main -
taining competitive advantages in this field.
Topic modeling
Since the massive amount of information exceeds human
processing capabilities, using LDA for topic modeling has
many significant advantages. First, as an unsupervised
learning algorithm, LDA does not require labeled data
and can automatically mine potential topic structures in
large-scale text data, reducing manual intervention and
annotation costs.
To determine the optimal number of topics, we cal -
culate the coherence score. As illustrated in Fig.  3, the
coherence score reaches its peak when the number of
topics is set to 5, indicating that the model achieves the
highest interpretability and the best fit. Therefore, gener -
ating five topics is considered the most ideal configura -
tion for this model [32].
Through topic modeling, we found that existing
research on artificial intelligence marketing mainly
focuses on several key domains (Table  2). Based on the
analysis of keywords and existing literature, five topics
were classified as follows: (1) Digitalization Transfor -
mation and Marketing Strategy. (2) Consumer Behav -
ior and Experience. (3) Business Value and Innovation
Research. (4) Machine Learning Algorithms and Tech -
nological Applications. (5) Generative AI Content and
Applications.
Topic 1 focuses on how digital technology innova -
tion reshapes marketing research and practice and how

Page 9 of 23
Xie et al. Future Business Journal          (2025) 11:272

companies can use effective marketing strategies to influ-
ence consumers’ purchasing decisions. Artificial intelli -
gence is the core driving force in digital transformation,
and it has profoundly changed the way companies inter -
act with consumers. AI often collaborates with other
technologies in digital transformation, mainly supporting
Fig. 3 Consistency scores under different number of topics
Table 2 Dominant topics in research on artificial intelligence in marketing
Topic
number
Label of the topic Main keywords Exemplary studies
1 Digitalization Transformation and Marketing Strategy Digital, data, technology, market, business, strategy,
decision
Brock and Von, 2019
Dwivedi et al., 2023
Paschen., 2019
Huang and Rust, 2021
Al-Surmi, 2022
2 Consumer Behavior and Experience Consumer, effect, product, customer, perceived, inten-
tion, relationship
Hoyer et al.,2020
Kumar et al., 2019
Puntoni et al., 2021
3 Business Value and Innovation Research Service, firm, value, future, capability, innovation, busi-
ness, social
Enholm et al., 2022
Canhoto and Clear, 2020
4 Machine Learning Algorithms and Technological
Applications
Learning, model, algorithm, data, network, user, predic-
tion, method
Huang and Rust, 2022
Kopalle et al., 2022
Bag et al., 2021
Yu and Liu, 2024
5 Generative AI Content and Applications Content, advertising, generated, tourism, ChatGPT,
generative, brand, information
Cao et al., 2025
Meyer et al., 2023
Zhang et al., 2024
Wang et al., 2024
Grewal et al., 2024

Page 10 of 23Xie et al. Future Business Journal          (2025) 11:272
existing businesses rather than disruptive innovation
[6]. It integrates a variety of digital technologies, pro -
vides brands with an immersive experience, expands
the dimension of data collection, and helps with preci -
sion marketing decisions [22]. AI systems can be divided
into six basic building blocks for information processing,
including structured data, unstructured data, preproc -
essing, core processes, knowledge bases, and informa -
tion output. In particular, AI’s ability to convert data into
market knowledge should be noted [67]. AI technology
can influence consumers’ decision-making process at
three different stages: marketing research, marketing
strategy (STP), and marketing action. For example, it can
enhance consumers’ purchasing intention and brand loy -
alty through personalized recommendations and senti -
ment analysis [39]. In addition, the synergy of marketing
and IT strategies will play an important role in improv -
ing corporate performance. Effective marketing strate -
gies can not only influence consumer decisions, but also
improve the overall operational efficiency of enterprises
through synergy with IT strategies [2].
Topic 2 focuses on how artificial intelligence technol -
ogy affects consumers’ decision-making process, interac -
tive experience, and relationship. With the support of AI
technology, companies can accurately predict and meet
consumer needs [37], as well as the positive and poten -
tial negative impacts of personalized experiences driven
by AI technology on consumer behavior [52]. How to
successfully shape consumers’ cognitive and emotional
responses through AI technology is what marketers
need to focus on. In addition, existing research has also
focused on the psychological and social challenges that
consumers may experience when interacting with AI,
such as privacy concerns, algorithmic bias, and distrust
of automated decision-making [69].
Topic 3 delves into the pivotal role of artificial intelli -
gence in creating business value and fostering innovation.
The value derived from the application of AI technolo -
gies within an enterprise is multidimensional. It enhances
business value not only by optimizing internal business
processes (e.g., improving operational efficiency and
automating repetitive tasks) to refine internal functions,
but also by adjusting products and services that directly
engage with customers (e.g., personalized recommen -
dations, intelligent customer service, and customized
product development) to augment external capabilities
[24]. The breadth and depth of this value creation make
AI a critical driver for enterprises to gain and sustain a
competitive advantage in an increasingly fierce mar -
ket. However, in the process of leveraging AI to achieve
value creation, enterprises must maintain a high degree
of prudence and rational judgment. As emphasized by
[8], if data-related risks—such as issues with data quality,
bias, privacy breaches, or algorithmic opacity—are not
properly managed, the application of AI can, conversely,
lead to significant value destruction. This includes not
only economic losses but also potential damage to cor -
porate reputation and consumer trust. Therefore, when
deploying AI solutions, it is imperative for firms to estab -
lish a robust data governance framework that ensures
the accuracy, integrity, and security of data. They must
also meticulously evaluate the fairness and transparency
of algorithms to mitigate potential adverse impacts and
ensure that AI investments are sustainably and effectively
translated into positive business value. Furthermore, the
continuous monitoring and iterative optimization of AI
systems, coupled with the intervention of human experts
in critical decision-making junctures, are paramount to
maximizing the commercial potential of AI while hedg -
ing its inherent risks.
Research related to Topic 4 focuses on the develop -
ment and application of artificial intelligence technology.
By enhancing data processing capabilities, a collabora -
tive framework between artificial intelligence and con -
sumers is established to make better consumer decisions
[38]. Existing research mainly studies the application of
AI technology in the field of marketing from two dimen -
sions: (1) human–machine interaction and (2) automated
analysis of text, audio, images, and video [48]. Artificial
intelligence technology will enhance the impact on cus -
tomer knowledge creation, user knowledge creation, and
external market knowledge creation, and better serve
enterprises and consumers [4]. This approach empha -
sizes deep learning models to analyze customer data,
identify consumer needs, and provide consumers with
highly personalized service experiences [85].
The five key topics in AI marketing research are intri -
cately interconnected, each influencing and reinforcing
the others. Digitalization Transformation and Market -
ing Strategy (Topic 1) provides the foundational frame -
work, enabling the AI technologies discussed in Machine
Learning Algorithms and Technological Applications
(Topic 4) to enhance data processing capabilities and
guide marketing strategies. This synergy, in turn, drives
Business Value and Innovation (Topic 3), as AI-powered
innovations improve operational efficiency and foster
deeper customer engagement. Additionally, insights from
Consumer Behavior and Experience (Topic 2) reveal how
AI’s impact on personalization directly influences con -
sumer decision-making, while also underscoring poten -
tial challenges such as privacy concerns and algorithmic
bias.
Furthermore, Generative AI Content and Applications
(Topic 5) builds upon the digital transformation dis -
cussed in Topic 1, allowing businesses to scale the crea -
tion of personalized, engaging content. The integration of

Page 11 of 23
Xie et al. Future Business Journal          (2025) 11:272

generative AI into marketing communications is shaped
by the technological and strategic advancements across
the other topics, ultimately influencing both business
performance and consumer experiences. These interde -
pendencies underscore the necessity for a comprehensive
understanding of how AI technologies converge across
various domains to drive innovation, optimize opera -
tions, and enhance customer relationships in the market-
ing ecosystem.
The core of Topic 5 is to explore the wide application
of generative AI technology in content creation and
marketing communication and its far-reaching impact.
The research content of this topic covers several key
dimensions. First, the evaluation of AI-generated con -
tent is an important part of it, which includes quantita -
tive and qualitative analysis of the quality, originality,
relevance, emotional expression, and user acceptance of
text, images, audio or video content created by AI [9].
For example, the related research evaluates the applica -
tion effect of large language models such as ChatGPT in
advertising copy, social media posts or product descrip -
tions, and examine its potential in improving efficiency,
reducing costs, and achieving personalized communi -
cation [56]. Secondly, the application of generative AI
in marketing in specific industries, such as AI content
generation in tourism marketing, has demonstrated its
strong adaptability to scenarios [87]. Tourist analysis can
be conducted by analyzing the photos or commentary
content generated by tourists to explore the image com -
position, visual esthetic quality, and uniqueness of tour -
ist destinations [82]. Finally, and most importantly, it is
exploring new models of human–machine collaborative
content creation. Generative AI is not intended to com -
pletely replace human creators, but rather to empower
marketers as a powerful auxiliary tool [31]. This new
model emphasizes the combination of human creativity,
strategic insights, and ethical judgment with AI’s effi -
cient generation and data analysis capabilities. Future
research will further explore how to build an efficient
human–machine collaborative process, optimize the
prompt engineering of AI tools, and how to balance AI’s
automation capabilities with human’s unique creativity to
achieve higher quality, more influential, and more brand-
value-oriented marketing content. This requires not only
technological progress, but also marketing profession -
als to play a leading role in strategy formulation, content
review, and ethical norms to ensure that the application
of AI can truly serve marketing goals rather than just
pursue efficiency.
Connections and relative importance between topics
As shown in Fig.  4, the distance between the cent -
ers of the circles represents the connectedness and
correspondence about topics. And, inter-topic distance
map by applying Python latent Dirichlet allocation visu -
alization (pyLDAvis), the distance between the centers of
the circles represents the connectedness and correspond-
ence between topics, and the size of each circle rep -
resents the importance of each topic in the document
collection. The pyLDAvis inter-topic distance map pro -
vides a sophisticated visual representation for interpret -
ing the thematic landscape derived from Latent Dirichlet
Allocation (LDA) models. The size of each circle is pro -
portional to the prevalence or overall importance of that
topic within the document collection, reflecting its fre -
quency and contribution to the corpus. This comprehen -
sive visual tool thus facilitates a nuanced understanding
of the relationships among topics, aiding researchers in
discerning dominant research areas, identifying potential
gaps, and constructing coherent narratives from complex
textual data [21]. In addition, the bar chart lists the Top-
30 Most Salient Term.
The Inter-topic Distance Map, generated via multi -
dimensional scaling, visually represents the thematic
landscape of AI in marketing research by illustrating the
relationships and distances between identified topics.
Each circle denotes a distinct research theme, with the
proximity between circles indicating thematic similar -
ity and overlap, while greater distances suggest thematic
divergence. Notably, Topic 1 (Digitalization Transforma -
tion and Marketing Strategy) and Topic 3 (Business Value
and Innovation Research) exhibit significant overlap and
close proximity, suggesting a strong conceptual connec -
tion. This alignment underscores the pervasive influence
of digital transformation on contemporary marketing
strategies, which are increasingly intertwined with the
pursuit of business value and innovation. Digital trans -
formation, as explored in Topic 1, is often intertwined
with the pursuit of business value, which encompasses
operational efficiency, customer engagement, and inno -
vation. However, this overlap may also lead to conceptual
ambiguity, as the two topics seem to conflate AI’s role
in strategic marketing decisions with its broader impact
on organizational value creation. This potential confu -
sion underscores the need for clearer theoretical differ -
entiation between AI’s applications in marketing and its
contributions to business innovation. While both topics
are interconnected, they should be defined separately to
avoid blending the strategic aspects of marketing with
broader operational impacts.
Furthermore, Topic 4 (Machine Learning Algorithms
and Technological Applications) is positioned distinctly
apart from Topics 1, 2, and 3, yet its isolated nature
highlights its foundational role. This separation implies
that while the core technological advancements in
machine learning are critical enablers, the research on

Page 12 of 23Xie et al. Future Business Journal          (2025) 11:272
these algorithms often remains in a more technical, less
directly applied domain compared to the strategic, con -
sumer, or business-oriented discussions.
Conversely, Topic 2 (Consumer Behavior and Experi -
ence) is situated at a considerable distance from all other
topics, particularly from the technology-focused Topic
4 and the emerging Topic 5 (Generative AI Content and
Applications). This spatial separation suggests a potential
research gap or a less integrated approach between the
technological development of AI and its direct impact
on consumer psychology and experience. Based on the
Stimulus–Organism–Response (S–O–R) model, where
AI-driven marketing stimuli (e.g., personalized ads and
chatbots) are expected to influence consumer internal
states (organism) and subsequent behaviors (response).
The current thematic distance implies that while AI tech-
nologies are being developed, their direct and nuanced
effects on consumer behavior and experience may not
yet be fully integrated into the mainstream technological
research.
Lastly, Topic 5 (Generative AI Content and Applica -
tions), positioned somewhat independently but closer
to the main cluster than Topic 4, signifies its nascent but
rapidly growing importance. Its distinctiveness reflects
its cutting-edge nature, while its relative proximity to the
core cluster suggests its potential to bridge technological
advancements with strategic and consumer-centric appli-
cations, potentially reshaping future research on digital
transformation and consumer engagement. The map thus
not only delineates current research foci but also implic -
itly highlights areas ripe for interdisciplinary integration
and future scholarly exploration.
To address the interconnectedness of the identified
themes and provide a coherent narrative of AI’s role in
the marketing process, we propose an integrative frame -
work that illustrates how AI permeates and transforms
various stages of the marketing value chain. As depicted
in Fig. 5, this framework elucidates the dynamic interplay
among the five themes, from foundational technological
advancements to their ultimate impact on business per -
formance and consumer engagement.
This framework is underpinned by machine learn -
ing algorithms and enabling technologies. This theme
represents the core technological infrastructure and
methodological advancements that underpin all AI-
driven marketing initiatives. As our analysis indicates,
research in this area often resides in a more technical
domain, focusing on the development and refinement of
algorithms, data processing capabilities, and collabora -
tive frameworks for enhanced decision-making. While
Fig. 4 Inter-topic distance map of the modeled topics

Page 13 of 23
Xie et al. Future Business Journal          (2025) 11:272

seemingly distinct, these foundational technologies are
the indispensable enablers that empower the subsequent
stages of AI integration into marketing. Without robust
machine learning models and efficient data processing,
the sophisticated applications discussed in other themes
would not be feasible. This foundational layer emphasizes
the continuous need for technological innovation and
expertise to push the boundaries of what AI can achieve
in marketing.
Building upon the technological foundations, Topic 1,
Digitalization Transformation and Marketing Strategy,
represents the strategic integration of AI into broader
organizational and marketing contexts. This theme high -
lights how digital technologies, with AI as a core driving
force, reshape marketing research and practice, influenc -
ing consumer purchasing decisions, and enhancing over -
all operational efficiency. The close proximity of Topic to
Topic in our inter-topic distance map underscores the
pervasive influence of digital transformation on contem -
porary marketing strategies, which are increasingly inter-
twined with the pursuit of business value and innovation.
AI’s ability to convert data into actionable market knowl -
edge is crucial here, enabling precision marketing deci -
sions and influencing consumer decision-making across
various stages, from marketing research to strategy for -
mulation and action.
Closely linked with strategic integration, Topic 3, Busi -
ness Value and Innovation Research, focuses on the
tangible outcomes and benefits derived from AI adop -
tion. This theme explores how AI contributes to multidi -
mensional value creation, both through internal process
optimization and external customer-facing enhance -
ments. This value creation is a direct consequence of
effectively leveraging the technological foundations
(Topic 4) and strategically integrating them into market -
ing operations (Topic 1). However, this theme also criti -
cally highlights the imperative for rational judgment and
robust data governance to mitigate risks such as data
quality issues, bias, privacy breaches, and algorithmic
opacity, which could otherwise lead to significant value
destruction. Thus, the realization of business value is
contingent upon responsible and ethical AI deployment.
Positioned somewhat distinctly in our thematic map,
Topic 2, Consumer Behavior and Experience, represents
the direct impact of AI on the end-user. This theme
explores how AI technologies influence consumers’
decision-making processes, interactive experiences, and
relationships with brands. It encompasses the predic -
tion and fulfillment of consumer needs, as well as the
positive and potential negative impacts of personal -
ized AI-driven experiences. The ethical considerations,
such as privacy concerns, algorithmic bias, and distrust
of automated decision-making, are particularly salient
here, as they directly affect consumer trust and accept -
ance. While this topic appears distant from the purely
technological (Topic 4), it is the ultimate recipient and
validator of AI’s application in marketing. Bridging this
gap requires a deeper understanding of consumer psy -
chology and a human-centric approach to AI design and
implementation.
Finally, Topic 5, Generative AI Content and Applica -
tions, represents a rapidly emerging and transformative
Fig. 5 Integrative framework of the modeled topics

Page 14 of 23Xie et al. Future Business Journal          (2025) 11:272
aspect of AI in marketing. This theme focuses on the
creation of content—text, images, audio, and video—
through generative AI models and its application in
various marketing communications, from advertising
creative to personalized tourism content. While drawing
upon the foundational algorithms (Topic 4), its distinc -
tiveness reflects its cutting-edge nature and its potential
to reshape content creation paradigms. Crucially, this
theme emphasizes the evolving paradigm of human–
machine collaborative content creation, where human
creativity, strategic insights, and ethical judgment are
combined with AI’s efficient generation and data analysis
capabilities. This collaboration is vital for producing high
quality, impactful, and brand-aligned marketing content,
ensuring that AI serves as an empowering tool rather
than a mere automation engine.
The integrative framework presented in this study effec-
tively synthesizes existing research on AI in marketing,
organizing key themes into a cohesive narrative. Rather
than introducing entirely new predictions, it primarily
restructures and refines the current body of knowledge.
By linking foundational technologies, such as Machine
Learning Algorithms (Topic 4), with practical applica -
tions such as Digitalization Transformation and Market -
ing Strategy (Topic 1) and Business Value and Innovation
(Topic 3), the framework illustrates how AI seamlessly
integrates into various stages of the marketing value
chain. While this connection does not offer groundbreak-
ing predictive insights, it provides a more comprehensive
and systematic understanding of AI’s multifaceted role in
marketing, highlighting the interdependencies between
technological advancements, strategic decision-making,
and consumer engagement. By structuring these themes
within a unified framework, it underscores how techno -
logical innovations, such as machine learning, serve as
critical enablers of both strategic marketing efforts and
business value creation. For example, it effectively links
AI’s ability to enhance consumer personalization (Topic
2) with strategic decisions in Topic 1, ultimately driving
tangible business outcomes as discussed in Topic 3. This
approach reveals the strategic interplay between tech -
nology and marketing—an aspect that has not been as
clearly articulated in the previous literature. In this way,
the framework offers a more cohesive, holistic perspec -
tive on how AI technologies drive marketing innovation,
optimize operational efficiency, and impact both business
performance and consumer behavior.
Scientometric analysis
Scientometric analysis can provide a macroscopic per -
spective on the research field, revealing the relationship
between the literature, the evolution of research topics,
and the intersection of disciplines through quantitative
analysis, thereby helping researchers quickly grasp the
overall structure and development trend of the research
field [44]. By using Scientometric analysis, we can reduce
the possibility of bias due to personal subjective percep -
tion and obtain results from more objective surveys.
Journal co‑citation analysis
This study uses the following parameter settings for co-
citation network analysis: a time slice of 1 year, a thresh -
old for each period using the g-index (k = 25), and path
optimization parameters LRF = 2.5, network trimming
parameter L/N = 10, time span LBY = 5, and network
density e = 1.0. The Pathfinder algorithm was applied for
network pruning. In the generated co-citation network
graph, node size is positively correlated with citation
frequency. The larger the node, the higher the number
of citations of the journal. Moreover, the width of con -
necting lines reflects the strength of co-citation between
journals [43]. Authoritative journals such as the Jour-
nal of Business Research, Technological Forecasting and
Social Change, Journal of the Academy of Marketing Sci -
ence, and Journal of Marketing each have co-citation fre -
quencies exceeding 100 times (Table  3). These journals
cover a wide range of research topics in the field of AI
marketing. The high frequency of co-citations not only
reflects the authoritative status and important influence
of these journals, but also confirms the high quality and
wide recognition of their published research findings. As
core journals in the AI marketing research field, they pro-
vide scholars with an important platform for publishing
results and continuously advance the development of this
research area by fostering the exchange and integration
of academic ideas.
However, we must also approach the citation count
metric with caution due to its time-dependent nature.
Given the cumulative effect of citations, the highly cited
journals identified in this study tend to be those that
have been established in the field for a longer period and
have accumulated a substantial body of literature. In con-
trast, journals that have only recently started publish -
ing a significant amount of research on AI marketing, or
those that are rapidly emerging in nascent subfields but
have not yet had sufficient time to accumulate citations,
Table 3 Journal co-citation sorted by count
Cited journals Count Centrality
JOURNAL OF BUSINESS RESEARCH 126 0.35
TECHNOLOGICAL FORECASTING AND SOCIAL
CHANGE
122 0.25
JOURNAL OF THE ACADEMY OF MARKETING SCI-
ENCE
105 0.31
JOURNAL OF MARKETING 104 0.20

Page 15 of 23
Xie et al. Future Business Journal          (2025) 11:272

may not have their full impact reflected in co-citation
frequency alone. Future research could incorporate
real-time impact indicators for journals, such as journal
impact factors or recent citation growth rates, or employ
citation analysis of the latest literature to more compre -
hensively capture the influence of leading and emerging
journals in the AI marketing domain.
Keywords co‑occurrence analysis and burst
analysis
Keyword co-occurrence analysis is an effective method
to reveal research hotspots and temporal characteristics
(Li and Chen, 2016). The keyword co-occurrence func -
tion of CiteSpace can identify core terms in research
literature and reveal emerging trends and development
patterns [11]. To delve into the research dynamics of AI
marketing, this study employs keyword co-occurrence
network analysis with the following parameters: a time
slice of 1  year, g-index (k = 15), LRF = 2.5, L/N = 10,
LBY = 5, e = 1.0, MAX WORDS = 5, and the Pathfinder
algorithm for network optimization. The analysis results
(Fig. 6) show that the generated keyword co-occurrence
network contains N = 252 and E = 396, with a network
density of 0.0125. Modularity value (Q-value) and aver -
age silhouette value (S-value) are important indicators for
evaluating clustering quality. When Q > 0.3, it indicates a
significant clustering structure. When S > 0.5, it indicates
that the clustering result is reasonable. When S > 0.7, it
is highly reliable [12]. This study achieved a Q-value of
0.7088 and an S-value as high as 0.8719 (Fig.  6), which
fully verified the effectiveness of cluster analysis. The net-
work analysis reveals the diverse and interdisciplinary
nature of AI marketing research.
The CiteSpace keyword co-occurrence network
reveals the knowledge structure and evolutionary char -
acteristics of the artificial intelligence marketing field,
wherein "artificial intelligence" as the absolute core
node (largest volume, red hot zone) forms a multi-lay -
ered network structure: The first layer consists of high-
centrality nodes such as "technology," "model," and
"information"; the second layer includes strategic nodes
such as "machine learning," "adoption," and "trust";
while the periphery comprises specialized nodes such
as "customer engagement" and "service robot." The
Fig. 6 Keywords co-occurring network

Page 16 of 23Xie et al. Future Business Journal          (2025) 11:272
network’s color evolution (from blue–green to red)
demonstrates the temporal development of research
hotspots from foundational concepts to the latest
frontiers, particularly with red nodes such as "genera -
tive AI" and "capability" representing the most recent
research directions. Through analysis of connection
patterns and density distribution, structural holes can
be identified, including the technology-consumer expe -
rience bridging area and the gap between generative
AI and traditional marketing nodes, revealing poten -
tial research opportunities. This network also exhibits
a technology-business dual-core structure, multidis -
ciplinary knowledge flow, and diversified application
scenarios, reflecting the highly interdisciplinary nature
of artificial intelligence marketing research, providing
researchers with a clear knowledge map that guides
future research directions.
Table 4 shows that in the field of artificial intelligence
marketing, there are 15 keywords that appear more
than 30 times, and the top 20 high-frequency words
include: artificial intelligence, impact, technology, big
data, machine learning, model, trust, social media,
management, etc. The higher the centrality, the more
it can explain its importance in current research. Sort -
ing the data in descending order, there are 42 keywords
with a centrality of more than 0.1. High-centrality key -
words such as b2b marketing, adoption, consequences,
classification, deep learning, experience, behavior, and
management indicate the core themes of related research.
These terms represent more than mere popularity;
they constitute the structural pillars upon which the
most influential research in the field is constructed. The
preeminent centrality of "b2b marketing" highlights its
pivotal function as a central nexus integrating diverse
research streams. Research within this thematic domain
typically bridges technical AI advancements with organi -
zational theory, examining how AI tools fundamentally
reshape processes such as lead generation, customer rela-
tionship management (CRM), and value chain optimiza -
tion in B2B environments. Adoption and consequences
form a powerful conceptual pair, representing the entire
lifecycle of technological integration. The prominence of
these technical terms (classification and deep learning)
highlights the methodological engine of the field. "Classi -
fication" is a foundational machine learning task essential
for core marketing functions such as customer segmen -
tation and churn prediction. The high centrality of "deep
learning" signifies a move toward more sophisticated,
nonlinear models capable of capturing complex patterns
in large datasets. Their role as central nodes, rather than
peripheral terms, demonstrates that advanced computa -
tional methods are not just tools but are integral to the
theoretical and conceptual development of the field.
By comparison, it is found that performance, big data,
social media, and knowledge are both high-frequency
Table 4 Artificial intelligence marketing research keywords sorted by centrality and count
Number Keywords Count Year Keywords Centrality Year
1 Artificial intelligence 347 2019 b2b marketing 0.36 2019
2 Impact 82 2019 Adoption 0.26 2019
3 Technology 76 2019 Consequences 0.24 2021
4 Big data 51 2019 Classification 0.21 2022
5 Machine learning 51 2020 Deep learning 0.20 2022
6 Model 50 2019 Experience 0.20 2019
7 Trust 40 2019 Behavior 0.19 2019
8 Knowledge 39 2020 Management 0.17 2019
9 Social media 38 2019 Intentions 0.16 2021
10 Management 38 2019 Satisfaction 0.15 2021
11 Acceptance 38 2019 Information technology 0.14 2021
12 Information 37 2020 Strategy 0.13 2019
13 Artificial intelligence 37 2019 Acceptance 0.13 2019
14 Framework 33 2021 Cross-section 0.12 2025
15 Decision-making 33 2021 Emotions 0.12 2024
16 Innovation 30 2020 Customer satisfaction 0.12 2021
17 Ai 29 2021 Innovation 0.12 2020
18 Adoption 28 2019 Knowledge 0.12 2020
19 Future 28 2022 Technology 0.12 2019
20 Performance 26 2020 b2b marketing 0.36 2019

Page 17 of 23
Xie et al. Future Business Journal          (2025) 11:272

keywords and high-centrality keywords, which to a cer -
tain extent reflect the hot spots and themes of current
research in the field. The results in Table  4 are also con -
sistent with the general direction of this study. At this
stage, artificial intelligence technology is based on big
data and machine learning, and is continuously iterated
and updated. It relies on algorithms to process massive
amounts of information and mainly interacts with con -
sumers through social media and various software to
help companies make marketing strategy decisions. At
the same time, it pays close attention to consumers’ expe-
rience, acceptance, and trust, thereby promoting con -
sumers to make purchasing decisions.
This study utilizes the burst detection algorithm pro -
posed by Kleinberg (2002) for analysis. In the visualiza -
tion results, the blue time period represents the data
collection period over the past 5 years [46], while the red
time period indicates the citation burst period of the key-
word [72], Fig.  7. The top 23 keywords with the strong -
est burst of citations are extracted according to their
strength. As can be seen from the figure, performance has
received the most attention in the field of artificial intel -
ligence marketing (burst strength = 4.21, 2020–2022),
followed by decision-making (burst strength = 3.44,
2021–2022) and future (burst strength = 2.8, 2022–2023).
The strong burst strength observed for “performance”
reflects the early and sustained emphasis on demonstrat -
ing the tangible benefits and return on investment (ROI)
of AI applications in marketing. This surge likely coin -
cided with the initial widespread adoption of AI tools
by businesses, necessitating empirical evidence to justify
their implementation and scale.
Similarly, the burst of “decision making” highlights a
growing scholarly interest in how AI influences and opti -
mizes strategic and tactical choices within marketing.
This trend was likely spurred by the increasing sophistica-
tion of AI algorithms capable of processing vast datasets
and providing predictive insights, thereby transforming
traditional human-centric decision processes. The burst
suggests a shift in focus from merely applying AI to inte -
grating AI into the core cognitive functions of marketing
management, exploring human–AI collaboration mod -
els and the implications for managerial autonomy and
accountability. This also aligns with the broader academic
discourse on explainable AI, as understanding AI’s con -
tribution to decision-making becomes paramount.
The emergence of “future” as a burst term indicates
a collective forward-looking perspective within the
research community. This recent surge can be attributed
to the rapid advancements in generative AI and large
language models, which have opened unprecedented
possibilities for content creation, personalization, and
customer interaction. This burst reflects a proactive
academic response to these disruptive technologies,
prompting researchers to explore their long-term impli -
cations, ethical considerations, and potential to redefine
marketing paradigms. Collectively, these burst keywords
not only delineate the historical trajectory of research
interests but also implicitly forecast future directions.
Conclusions
General discussion
With the rapid development of technology, AI is promot-
ing the transformation across multiple fields. Its applica -
tion in the field of marketing has become a key research
direction of common concern in academia and industry.
As an emerging interdisciplinary field, AI marketing inte-
grates cutting-edge AI technologies with modern mar -
keting theories. Through machine learning algorithms,
natural language processing technology, and big data
analysis methods [61], it enables deep insights into con -
sumer behavior, intelligent optimization of marketing
decision processes, and significant enhancement of mar -
keting precision and efficiency, thereby creating sustaina-
ble competitive advantages for businesses topic modeling
techniques [70].
This study combines topic modeling and scientomet -
ric techniques to systematically analyze AI marketing
research literature from 2019 to May 2025 within the
Web of Science Core Collection database. The goal is to
comprehensively sort out the research evolution path in
this field, identify core research topics, and predict future
development trends, so as to provide theoretical basis
and innovative perspectives for subsequent academic
research and business practice.
First, we performed topic modeling based on the algo -
rithm’s advanced methodology. By reviewing a total of
564 relevant literature on artificial intelligence market -
ing from 2019 to May 2025, we identified five topics: (1)
Digitalization Transformation and Marketing Strategy.
(2) Consumer Behavior and Experience. (3) Business
Value and Innovation Research. (4) Machine Learn -
ing Algorithms and Technological Applications. (5)
Generative AI Content and Applications. The relation -
ships among these interdependent themes underscore
the critical need for a comprehensive understanding of
how AI technologies integrate across various domains
to drive innovation, optimize operations, and enhance
customer relationships within the marketing ecosys -
tem. To clarify the interconnections between the iden -
tified themes and cohesively articulate AI’s role in the
marketing process, we propose an integrative frame -
work. This framework demonstrates how AI perme -
ates and transforms multiple stages of the marketing
value chain, combining foundational technologies,
such as Machine Learning Algorithms (Topic 4), with

Page 18 of 23Xie et al. Future Business Journal          (2025) 11:272
practical applications such as Digitalization Transfor -
mation and Marketing Strategy (Topic 1) and Business
Value and Innovation (Topic 3). It illustrates the seam -
less integration of AI into the marketing value chain,
emphasizing the interdependencies between techno -
logical advancements, strategic decision-making, and
consumer engagement. This approach uncovers the
strategic interplay between technology and market -
ing—an aspect that has been insufficiently addressed in
prior literature. In this manner, the framework offers a
more cohesive and comprehensive perspective on how
AI technologies drive marketing innovation, optimize
Fig. 7 Top 23 keywords with the strongest citation burst

Page 19 of 23
Xie et al. Future Business Journal          (2025) 11:272

operational efficiency, and influence both business per -
formance and consumer behavior.
Then, using scientometric techniques, we found that
artificial intelligence marketing has attracted a lot of
attention from scholars in the marketing. In terms of
country/region distribution, the USA and China lead
global research output in this domain, forming an inter -
national collaborative research framework centered
around these two countries with contributions from mul-
tiple nations. Regarding journal influence, high-impact
journals such as the Journal of Business Research, Tech-
nological Forecasting and Social Change, Journal of the
Academy of Marketing Science, and Journal of Marketing
have not only published numerous AI marketing research
papers but also exhibit high centrality in co-citation net -
works. The academic results published in these authori -
tative journals provide important theoretical references
and methodological insights for future research in the
field.
From the perspective of consumers, the application of
AI technology in the field of marketing has a significant
dual effect. On the one hand, intelligent recommenda -
tion systems enhance the quality of consumers’ pur -
chasing decisions by improving algorithm accuracy [88],
while voice interaction interfaces enhance user experi -
ence through efficient response mechanisms [16]. On
the other hand, technology acceptance displays nonlin -
ear characteristics, which is mainly due to the uncanny
valley effect caused by human-like technology and the
influence of cross-cultural differences [15]. Consumers’
value assessment framework for AI marketing includes
three key dimensions: perception of technology reli -
ability, perceived naturalness of interaction, and trust in
data privacy [1, 51]. Privacy calculus theory suggests that
consumers weigh the benefits of AI, such as personalized
recommendations, against potential privacy risks, includ-
ing data misuse. When AI systems offer strong privacy
protection and transparency, trust increases, leading to
improved decision quality and higher adoption. However,
if privacy concerns outweigh these benefits, particularly
when data protection is perceived as inadequate, AI’s
impact can become negative, eroding trust, and reducing
adoption [74]. Additionally, algorithm aversion theory
highlights that consumers may reject AI recommenda -
tions if they perceive the algorithms as flawed or incon -
sistent, despite their accuracy [49]. Key factors, such
as algorithm transparency and human involvement in
decision-making, influence whether consumers accept or
reject AI-driven outcomes. When AI’s decision-making
process is opaque or detached from human logic, it may
lead to algorithm aversion, undermining trust and deci -
sion quality [20]. When intelligent systems can effectively
simulate human thinking patterns and fully guarantee
data sovereignty, they will significantly enhance con -
sumers’ willingness to continue using them, thereby
promoting the formation of a coordinated development
mechanism of “consumer-technology-market. ” The estab-
lishment of this virtuous cycle depends on the dynamic
balance between technical performance and user trust.
The framework highlights the dynamic interaction
between consumers, AI technologies, and the market,
emphasizing how trust and technological performance
drive consumer adoption and market growth.
At the enterprise level, the profound impact of AI tech-
nology implementation manifests primarily through stra-
tegic empowerment and organizational transformation.
Machine learning-driven demand forecasting models, for
instance, have propelled marketing decisions from being
experience-oriented to data-driven, enabling dynamic
optimization of resource allocation efficiency [58, 64].
Furthermore, AI-optimized supply chain collabora -
tion and intelligent pricing mechanisms empower firms
to establish significant cost advantages, while computer
vision-based advertising creative generation systems sub-
stantially enhance the effectiveness of marketing content.
Beyond operational efficiencies, the deep integration of
AI technology fundamentally reshapes organizational
structures. Intelligent customer service systems are pro -
gressively supplanting traditional manual services, lead -
ing to a breakthrough in efficiency. The convergence of
blockchain and AI technologies, meanwhile, establishes
novel transparent trust mechanisms.
However, the inherent risks of over-reliance on tech -
nology and the challenges posed by algorithmic black
box issues necessitate the establishment of robust ethi -
cal review systems within enterprises [45]. To navigate
this evolving landscape and ensure practical relevance,
firms must strategically leverage AI to inform critical
managerial decision-making. This involves integrating
AI adoption into firm innovation strategies, fostering
agile responses to market shifts, and optimizing mar -
keting resource allocation based on predictive analytics.
AI also drives significant organizational restructuring,
necessitating new skill sets and collaborative human–
AI models. Specifically, in core business functions, AI
profoundly impacts customer engagement through
personalized interactions, enhances Customer Rela -
tionship Management (CRM) by predicting customer
needs and churn, and revolutionizes product personali -
zation by tailoring offerings at scale. These capabilities
translate into more efficient inventory management and
optimized resource allocation. This capability directly
contributes to a firm’s cost leadership advantage, as it
reduces overproduction, stockouts, and waste, enhanc -
ing operational efficiency. Moreover, AI-enabled cus -
tomer relationship management (CRM) systems allow

Page 20 of 23Xie et al. Future Business Journal          (2025) 11:272
firms to enhance customer engagement through proac -
tive, data-driven interactions, predicting, and address -
ing customer needs before they arise. This ability not
only builds customer intimacy but also fosters a more
resilient market position. Similarly, AI-optimized pric -
ing models, driven by real-time data analysis, enable
businesses to implement dynamic pricing strategies
that respond to market fluctuations, thereby improv -
ing profit margins and capturing additional value. By
constructing sophisticated human–machine collabora -
tion models, enterprises can effectively balance techni -
cal rationality with value rationality, thereby fostering
the coordinated and sustainable development of the
broader “technology-economy-society” system. The
Technology–Economy–Society framework focuses on
the broader societal and economic implications of AI
integration, offering insights into organizational trans -
formation and the balance between technological inno -
vation and ethical considerations.
Future perspective
AI marketing has become a key driver of innovation in
the marketing field. Enterprises use AI technology to
optimize marketing decision processes, enhance con -
sumer experiences, and strengthen customer relation -
ship management [18]. However, due to its relatively
short development history, existing research results are
fragmented and lack systematic theoretical frameworks,
indicating that AI marketing research still holds vast
potential for development [33].
Investigating contextual factors governing AI’s dual impact
on consumer behavior
Future research could delve more profoundly into the
contextual variables that determine whether AI exerts
a predominantly positive or negative influence on
consumer decision-making. While extant literature
acknowledges the dual impact of AI, the boundary con -
ditions—such as privacy concerns, algorithmic trans -
parency, and data security trust—remain underexplored
[47]. Theories such as privacy calculus and algorithm
aversion provide critical frameworks for understanding
how consumers weigh the trade-off between the ben -
efits of AI-driven personalization and the potential risks,
including privacy infringements and algorithmic biases
[86]. Future studies should investigate how individual
consumer characteristics (e.g., technological fluency
and cultural diversity) and macro-environmental factors
(e.g., market maturity and regulatory frameworks) shape
these dynamics. By examining these factors, researchers
can enhance our understanding of the conditions under
which AI’s influence on consumer behavior will be con -
structive or potentially alienating.
Enhancing AI’s integration in business value creation
and strategic decision‑making
A further avenue for future research lies in the inte -
gration of AI with business value creation and strate -
gic decision-making processes. Although this study
highlights the transformative potential of AI in opti -
mizing operations and customer engagement, there
is a need for deeper exploration into how AI capabili -
ties translate into specific and sustainable competitive
advantages across different industries. Future research
could focus on how firms can strategically embed AI-
driven technologies—such as predictive analytics and
advanced machine learning models—within their
innovation frameworks to drive sustained growth [55].
Moreover, exploring the organizational challenges and
ethical implications of AI adoption, especially in rela -
tion to algorithmic decision-making, is essential. Key
areas such as data governance, algorithmic transpar -
ency, and human–AI collaboration require further
examination to ensure that AI applications are both
effective and ethically sound, thereby maximizing busi -
ness value without compromising consumer trust [30].
Research limitations
This study adopts a systematic quantitative analysis
method to effectively avoid the subjective bias prob -
lems common in traditional non-systematic literature
reviews, expert surveys, and opinion studies. However,
there are several limitations. First, due to the selected
keywords and the time range of 2019– May 2025 in
the Web of Science database, it fails to fully present
the development of AI marketing. Second, regard -
ing the methodology for keyword selection.The search
query was constructed based on a predefined set of
keywords derived from foundational literature in the
field. While this approach ensures relevance to core
concepts, it may not have fully captured all emerg -
ing or niche terminologies in this rapidly evolving
domain. Future research could mitigate this limitation
by employing more dynamic or machine-assisted key -
word identification techniques. Finally, another avenue
for future research, building upon the thematic analy -
sis conducted in this study, involves the application of
advanced statistical techniques such as factor analysis.
While Latent Dirichlet Allocation (LDA) effectively
identified key research themes, a subsequent factor
analysis on the generated topic-word distributions or
topic-document assignments could provide a more

Page 21 of 23
Xie et al. Future Business Journal          (2025) 11:272

robust and nuanced interpretation of the underlying
thematic structures.
Author contributions
We attest to the fact that all authors have contributed signifcantly to the work,
have read the manuscript, attest to the validity and legitimacy of the data and
their interpretation, and agree for publication this manuscript in the Future.
Funding
We gratefully acknowledge the financial support from the National Natural
Science Foundation of China (No. 71662036).
Availability of data and materials
The raw data supporting the conclusions of this article will be made available
by the authors on request.
Declarations
Ethics approval and consent to participate
The following declaration were made to the Chief Executive Officers of the
regulatory authorities which participated in the study: “I, XXX, of the XXX, XXX,
XXX, declare that, I will maintain secrecy and confidentiality, and will not use
any data and information obtained from your organization in the course of my
research for any purpose other than for my academic endeavors.” In addition,
the XXX approved my research proposal on the ethics consideration. I should,
therefore, state that: “Ethics consideration in this research was observed in
compliance with the OUT-Research Ethics Guidelines, 2015.” The main issues
considered were avoiding data fabrication in surveys, data falsification in
surveys and plagiarism.
Consent for publication
We attest to the fact that all authors have contributed significantly to the
work, have read the manuscript, attest to the validity and legitimacy of the
data and their interpretation, and agree for publication this manuscript in the
future.
Competing interests
The authors declare no competing interests.
Received: 12 September 2025   Accepted: 2 November 2025
References
 1. Alhitmi HK, Mardiah A, Al-Sulaiti KI et al (2024) Data security and privacy
concerns of AI-driven marketing in the context of economics and busi-
ness field: an exploration into possible solutions. Cogent Bus Manage
11(1):2393743
 2. Al-Surmi A, Bashiri M, Koliousis I (2022) AI based decision making:
combining strategies to improve operational performance. Int J Prod Res
60(14):4464–4486
 3. Armutcu B, Tan A, Ho SPS et al (2024) The effect of bank artificial intel-
ligence on consumer purchase intentions. Kybernetes. https:// doi. org/ 10.
1108/K- 01- 2024- 0145
 4. Bag S, Gupta S, Kumar A et al (2021) An integrated artificial intelligence
framework for knowledge creation and B2B marketing rational decision
making for improving firm performance. Ind Mark Manage 92:178–189
 5. Bini F, Pica A, Azzimonti L et al (2021) Artificial intelligence in thyroid
field—a comprehensive review. Cancers (Basel) 13(19):4740
 6. Brock JKU, Von Wangenheim F (2019) Demystifying AI: what digital trans-
formation leaders can teach you about realistic artificial intelligence. Calif
Manage Rev 61(4):110–134
 7. Cabrera-Sánchez JP , Villarejo-Ramos ÁF, Liébana-Cabanillas F et al (2021)
Identifying relevant segments of AI applications adopters–expanding the
UTAUT2’s variables. Telemat Informatics 58:101529
 8. Canhoto, Clear F (2020) Artificial intelligence and machine learning as
business tools: a framework for diagnosing value destruction potential.
Bus Horiz 63(2):183–193
 9. Cao et al (2025) A survey of AI-generated content (AIGC). ACM Comput
Surv 57(5):1–38
 10. Chaturvedi R, Verma S, Srivastava V (2024) Empowering AI companions
for enhanced relationship marketing. Calif Manage Rev 66(2):65–90
 11. Chen C (2006) CiteSpace II: detecting and visualizing emerging trends
and transient patterns in scientific literature. J Am Soc Inf Sci Technol
57(3):359–377
 12. Chen C (2017) Science mapping: a systematic review of the literature. J
Data Inf Sci. https:// doi. org/ 10. 1515/ jdis- 2017- 0006
 13. Cheng Y, Jiang H (2022) Customer–brand relationship in the era of
artificial intelligence: understanding the role of chatbot marketing efforts.
J Product Brand Manag 31(2):252–264
 14. Chui M, Francisco S (2017) Artificial intelligence the next digital frontier.
McKinsey Company Glob Inst 47(3.6):6–8
 15. Ciechanowski L, Przegalinska A, Magnuski M et al (2019) In the shades of
the uncanny valley: an experimental study of human–chatbot interac-
tion. Future Gener Comput Syst 92:539–548
 16. Corbett E, Weber A (2016) What can I say? Addressing user experience
challenges of a mobile voice user interface for accessibility. In: Proceed-
ings of the 18th international conference on human-computer interac-
tion with mobile devices and services. 72–82
 17. Davenport TH, Ronanki R (2018) Artificial intelligence for the real world.
Harv Bus Rev 96(1):108–116
 18. Davenport T, Guha A, Grewal D et al (2020) How artificial intelligence will
change the future of marketing. J Acad Mark Sci 48:24–42
 19. De Bakker FGA, Groenewegen P , Den Hond F (2005) A bibliometric analy-
sis of 30 years of research and theory on corporate social responsibility
and corporate social performance. Bus Soc 44(3):283–317
 20. De Bruijn H, Warnier M, Janssen M (2022) The perils and pitfalls of explain-
able AI: strategies for explaining algorithmic decision-making. Gov Inf Q
39(2):101666
 21. DePaolo CA, Wilkinson K (2014) Get your head into the clouds: using
word clouds for analyzing qualitative assessment data. TechTrends.
https:// doi. org/ 10. 1007/ s11528- 014- 0750-9
 22. Dwivedi YK, Hughes L, Wang Y et al (2023) Metaverse marketing: how
the metaverse will shape the future of consumer research and practice.
Psychol Mark 40(4):750–776
 23. Elhajjar S (2025) Unveiling the marketer’s lens: exploring experiences and
perspectives on AI integration in marketing strategies. Asia Pac J Mark
Logist 37(2):498–517
 24. Enholm IM, Papagiannidis E, Mikalef P et al (2022) Artificial intelligence
and business value: a literature review. Inf Syst Front 24(5):1709–1734
 25. Farrokhi A, Shirazi F, Hajli N, Tajvidi M (2020) Using artificial intelligence to
detect crisis related to events: decision making in B2B by artificial intel-
ligence. Ind Mark Manag 91:257–273
 26. Gansser OA, Reich CS (2021) A new acceptance model for artificial intel-
ligence with extensions to UTAUT2: an empirical study in three segments
of application. Technol Soc 65:101535
 27. Gao Y, Liu H (2023) Artificial intelligence-enabled personalization in inter-
active marketing: a customer journey perspective. J Res Interact Mark
17(5):663–680
 28. Go E, Sundar SS (2019) Humanizing chatbots: the effects of visual, iden-
tity and conversational cues on humanness perceptions. Comput Human
Behav 97:304–316
 29. Gong X, Yee CL, Lee SY et al (2024) Knowledge mapping of impulsive
buying behavior research: a visual analysis using CiteSpace. Hum Social
Sci Commun 11(1):1–18
 30. Grewal D, Hulland J, Kopalle PK et al (2020) The future of technology and
marketing: a multidisciplinary perspective. J Acad Mark Sci 48:1–8
 31. Grewal D, Satornino CB, Davenport T et al (2024) How generative AI is
shaping the future of marketing. J Acad Mark Sci. https:// doi. org/ 10. 1007/
s11747- 024- 01064-3
 32. Yanqing G, Jiayi Z (2025) Research on the sustainable development of
scientist-run enterprises driven by entrepreneurship: taking hard tech-
nology enterprises as an example. Forum Sci Technol China 02:84–94.
https:// doi. org/ 10. 13580/j. cnki. fstc. 2025. 02. 015
 33. Guowei Z, Wenli G, Jiahui L et al (2021) Artificial intelligence marketing: a
research review and prospects. For Econ Manag 43(07):86–96

Page 22 of 23Xie et al. Future Business Journal          (2025) 11:272
 34. Gursoy D, Chi OH, Lu L et al (2019) Consumers acceptance of artificially
intelligent (AI) device use in service delivery. Int J Inf Manage 49:157–169
 35. Haleem A, Javaid M, Qadri MA et al (2022) Artificial intelligence (AI) appli-
cations for marketing: a literature-based study. Int J Intell Netw 3:119–132
 36. Hoy MB (2018) Alexa, Siri, Cortana, and more: an introduction to voice
assistants. Med Ref Serv Q 37(1):81–88
 37. Hoyer WD, Kroschke M, Schmitt B et al (2020) Transforming the customer
experience through new technologies. J Interact Mark 51(1):57–71
 38. Huang MH, Rust RT (2022) A framework for collaborative artificial intel-
ligence in marketing. J Retail 98(2):209–223
 39. Huang MH, Rust RT (2021) A strategic framework for artificial intelligence
in marketing. J Acad Mark Sci 49:30–50
 40. Huang MH, Rust RT (2018) Artificial intelligence in service. J Serv Res
21(2):155–172
 41. Jelodar H, Wang Y, Yuan C et al (2019) Latent Dirichlet allocation (LDA)
and topic modeling: models, applications, a survey. Multimedia Tools
Appl 78:15169–15211
 42. Jiang Y, Yang G, Li H et al (2023) Knowledge driven approach for smart
bridge maintenance using big data mining. Autom Constr 146:104673
 43. Jie L, Chaomei C (2022) CiteSpace: text mining and visualization in scien-
tific literature. Capital University of Economics and Business Press, Beijing
 44. Kastrin A, Hristovski D (2021) Scientometric analysis and knowledge
mapping of literature-based discovery (1986–2020). Scientometrics
126(2):1415–1451
 45. Keegan BJ, Iredale S, Naudé P (2023) Examining the dark force con-
sequences of AI as a new actor in B2B relationships. Ind Mark Manag
115:228–239
 46. Kleinberg J (2002) Bursty and hierarchical structure in streams. In:
Proceedings of the eighth ACM SIGKDD international conference on
Knowledge discovery and data mining. 91–101
 47. Kolbjørnsrud V, Amico R, Thomas RJ (2016) How artificial intelligence will
redefine management. Harv Bus Rev 2(1):3–10
 48. Kopalle PK, Gangwar M, Kaplan A et al (2022) Examining artificial intel-
ligence (AI) technologies in marketing via a global lens: current trends
and future research opportunities. Int J Res Mark 39(2):522–540
 49. Kordzadeh N, Ghasemaghaei M (2022) Algorithmic bias: review, synthesis,
and future research directions. Eur J Inf Syst 31(3):388–409
 50. Kshetri N, Dwivedi YK, Davenport TH et al (2024) Generative artificial
intelligence in marketing: applications, opportunities, challenges, and
research agenda. Int J Inf Manage 75:102716
 51. Kumar D, Suthar N (2024) Ethical and legal challenges of AI in marketing:
an exploration of solutions. J Inf Commun Ethics Soc 22(1):124–144
 52. Kumar V, Rajan B, Venkatesan R et al (2019) Understanding the role of arti-
ficial intelligence in personalized engagement marketing. Calif Manage
Rev 61(4):135–155
 53. Lee S, Lau IY, Hong Y (2011) Effects of appearance and functions on lik-
ability and perceived occupational suitability of robots. J Cogn Eng Decis
Mak 5(2):232–250
 54. Liang XW, Cai YY, Yu JS et al (2019) Update on thyroid ultrasound: a nar-
rative review from diagnostic criteria to artificial intelligence techniques.
Chin Med J 132(16):1974–1982
 55. Madhani PM (2010) Resource based view (RBV) of competitive advan-
tage: an overview. Resource based view: concepts and practices, Pankaj
Madhani. 3–22
 56. Meyer JG, Urbanowicz RJ, Martin PCN et al (2023) ChatGPT and large
language models in academia: opportunities and challenges. Biodata
Min 16(1):20
 57. Mo Y, Kontonatsios G, Ananiadou S (2015) Supporting systematic reviews
using LDA-based document representations. Syst Rev 4:1–12
 58. Mogaji E, Nguyen NP (2022) Managers’ understanding of artificial intel-
ligence in relation to marketing financial services: insights from a cross-
country study. Int J Bank Mark 40(6):1272–1298
 59. Mongeon P , Paul-Hus A (2016) The journal coverage of Web of Science
and Scopus: a comparative analysis. Scientometrics 106(1):213–228
 60. Moradi M, Dass M (2022) Applications of artificial intelligence in B2B mar-
keting: challenges and future directions. Ind Mark Manag 107:300–314
 61. Moreno A, Redondo T (2016) Text analytics: the convergence of big data
and artificial intelligence. IJIMAI. 3(6):57–64. (Carlos RC, Kahn CE, Halabi S
(2018) Data science: big data, machine learning, and artificial intelligence.
J Am Coll Radiol. 15(3):497–498
 62. Mori M (1970) The uncanny valley: the original essay by Masahiro Mori.
IEEE Spectr 6(1):6
 63. Mustak M, Salminen J, Plé L et al (2021) Artificial intelligence in marketing:
topic modeling, scientometric analysis, and research agenda. J Bus Res
124:389–404
 64. Noranee S, bin Othman AK (2023) Understanding consumer sentiments:
exploring the role of artificial intelligence in marketing. JMM17: Jurnal
Ilmu ekonomi dan manajemen 10(1):15–23
 65. Olan F, Arakpogun EO, Suklan J et al (2022) Artificial intelligence and
knowledge sharing: contributing factors to organizational performance. J
Bus Res 145:605–615
 66. Overgoor G, Chica M, Rand W et al (2019) Letting the computers
take over: using AI to solve marketing problems. Calif Manage Rev
61(4):156–185
 67. Paschen J, Kietzmann J, Kietzmann TC (2019) Artificial intelligence (AI)
and its implications for market knowledge in B2B marketing. J Bus Ind
Mark 34(7):1410–1419
 68. Pizzi G, Scarpi D, Pantano E (2021) Artificial intelligence and the new
forms of interaction: who has the control when interacting with a chat-
bot? J Bus Res 129:878–890
 69. Puntoni S, Reczek RW, Giesler M et al (2021) Consumers and artificial
intelligence: an experiential perspective. J Market 85(1):131–151
 70. Radanliev P , De Roure D, Nicolescu R et al (2021) Artificial intelligence and
the internet of things in industry 40. CCF Trans Pervas Comput Interact
3:329–338
 71. Rekha AG, Abdulla MS, Asharaf S (2016) Artificial intelligence marketing:
an application of a novel lightly trained support vector data description. J
Inf Optim Sci 37(5):681–691
 72. Saleem F, Khattak A, Ur Rehman S et al (2021) Bibliometric analysis of
green marketing research from 1977 to 2020. Publications 9(1):1
 73. Salminen J, Yoganathan V, Corporan J et al (2019) Machine learning
approach to auto-tagging online content for content marketing effi-
ciency: a comparative analysis between methods and content type. J Bus
Res 101:203–217
 74. Schomakers EM, Lidynia C, Ziefle M (2022) The role of privacy in the
acceptance of smart technologies: applying the privacy calculus to
technology acceptance. Int J Human-Comput Interact 38(13):1276–1289
 75. Sohn K, Kwon O (2020) Technology acceptance theories and factors
influencing artificial Intelligence-based intelligent products. Telemat Inf
47:101324
 76. Song HJ, Ruan WJ, Jeon YJJ (2021) An integrated approach to the pur-
chase decision making process of food-delivery apps: focusing on the
TAM and AIDA models. Int J Hosp Manage 95:102943
 77. Stone M, Aravopoulou E, Ekinci Y et al (2020) Artificial intelligence (AI) in
strategic marketing decision-making: a research agenda. Bottom Line
33(2):183–200
 78. Syam N, Sharma A (2018) Waiting for a sales renaissance in the fourth
industrial revolution: machine learning and artificial intelligence in sales
research and practice. Ind Mark Manage 69:135–146
 79. Verma S, Sharma R, Deb S et al (2021) Artificial intelligence in marketing:
systematic review and future research direction. Int J Inf Manag Data
Insights 1(1):100002
 80. Vlačić B, Corbo L, e Silva SC et al (2021) The evolving role of artificial
intelligence in marketing: a review and research agenda. J Bus Res
128:187–203
 81. Wamba-Taguimdje SL, Fosso Wamba S, Kala Kamdjoug JR et al (2020)
Influence of artificial intelligence (AI) on firm performance: the busi-
ness value of AI-based transformation projects. Bus Process Manag J
26(7):1893–1924
 82. Wang X, Mou N, Zhu S et al (2024) How to perceive tourism destination
image? A visual content analysis based on inbound tourists’ photos. J
Destin Mark Manage 33:100923
 83. Xie Z, Yu Y, Zhang J et al (2022) The searching artificial intelligence: con-
sumers show less aversion to algorithm-recommended search product.
Psychol Mark 39(10):1902–1919
 84. Yang X, Li H, Ni L et al (2021) Application of artificial intelligence in preci-
sion marketing. J Org End User Comput 33(4):209–219
 85. Yu BTW, Liu STX (2024) Deep learning application for marketing engage-
ment–its thematic evolution. J Res Interact Mark. https:// doi. org/ 10. 1108/
JRIM- 08- 2024- 0371

Page 23 of 23
Xie et al. Future Business Journal          (2025) 11:272

 86. Zhang C, Lu Y (2021) Study on artificial intelligence: the state of the art
and future prospects. J Ind Inf Integr 23:100224
 87. Zhang JJ, Wang YW, Ruan Q et al (2024) Digital tourism interpretation
content quality: a comparison between AI-generated content and
professional-generated content. Tour Manage Perspect 53:101279
 88. Zimmermann R, Mora D, Cirqueira D et al (2023) Enhancing brick-and-
mortar store shopping experience with an augmented reality shopping
assistant application using personalized recommendations and explain-
able artificial intelligence. J Res Interact Mark 17(2):273–298
Publisher’s Note
Springer Nature remains neutral with regard to jurisdictional claims in pub-
lished maps and institutional affiliations.
