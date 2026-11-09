---
title: 'Leveraging AI and NLP for Bank Marketing: A Systematic Review and Gap Analysis'
url: https://arxiv.org/abs/2411.14463
category: cx-retail
subcategory: framework
date: 2024-11
venue: 'RePEc: Research Papers in Economics'
authors:
- Christopher Gerling
- Stefan Lessmann
source: arxiv
pdf_url: https://arxiv.org/pdf/2411.14463
pages: 32
chars: 128748
fetched_at: '2026-11-08T12:57:12+00:00'
kb_version: 1
---

# Leveraging AI and NLP for Bank Marketing: A Systematic Review and Gap Analysis

LEVERAGING AI AND NLP FOR BANK MARKETING :
A S YSTEMATIC REVIEW AND GAP ANALYSIS
Christopher Gerling
Chair of Information Systems
Humboldt University of Berlin
Berlin, Germany
gerlingc@hu-berlin.de
Stefan Lessmann
Chair of Information Systems
Humboldt University of Berlin
Berlin, Germany
ABSTRACT
This paper explores the growing impact of AI and NLP in bank marketing, highlighting their evolv-
ing roles in enhancing marketing strategies, improving customer engagement, and creating value
within this sector. While AI and NLP have been widely studied in general marketing, there is a no-
table gap in understanding their specific applications and potential within the banking sector. This
research addresses this specific gap by providing a systematic review and strategic analysis of AI
and NLP applications in bank marketing, focusing on their integration across the customer journey
and operational excellence.
Employing the PRISMA methodology, this study systematically reviews existing literature to assess
the current landscape of AI and NLP in bank marketing. Additionally, it incorporates semantic map-
ping using Sentence Transformers and UMAP for strategic gap analysis to identify underexplored
areas and opportunities for future research.
The systematic review reveals limited research specifically focused on NLP applications in bank
marketing. The strategic gap analysis identifies key areas where NLP can further enhance market-
ing strategies, including customer-centric applications like acquisition, retention, and personalized
engagement, offering valuable insights for both academic research and practical implementation.
This research contributes to the field of bank marketing by mapping the current state of AI and NLP
applications and identifying strategic gaps. The findings provide actionable insights for developing
NLP-driven growth and innovation frameworks and highlight the role of NLP in improving oper-
ational efficiency and regulatory compliance. This work has broader implications for enhancing
customer experience, profitability, and innovation in the banking industry.
Keywords Bank Marketing · NLP · Sales Analytics · Artificial Intelligence · Systematic Review · Gap Analysis
1 Introduction
The integration of Artificial Intelligence (AI) is rapidly reshaping bank marketing strategies, marking a new era in
how financial institutions engage clients. This builds upon foundational digital marketing principles in customer re-
lationship management (CRM) and personalization, as highlighted by Kannan and Li [2017], who emphasized the
transformative role of digital technologies in enhancing the marketing mix (Product, Price, Place, Promotion). AI rep-
resents a substantial technological shift and offers new opportunities in data processing and predictive analytics. In the
banking sector, AI’s role is particularly significant due to the industry’s unique challenges, including the intangibility
of products, higher security requirements, and the need for complex computations within strict regulatory frameworks,
necessitating distinct AI-driven marketing approaches.
AI can process unstructured data in order to enhance value and revenue in bank marketing. This potential for deeper
insights into consumer behavior, highlighted by Wedel and Kannan [2016], remains underexplored, partly due to
confidentiality issues in customer data. The use of Natural Language Processing (NLP) as a marketing tool has not
been fully leveraged, indicating a gap between AI’s potential and its current use in bank marketing. This motivates a
arXiv:2411.14463v1  [cs.CL]  17 Nov 2024

Leveraging AI and NLP for Bank Marketing
two-step approach: first, conducting a systematic review to synthesize existing knowledge, and second, performing a
strategic gap analysis using advanced semantic mapping techniques to identify opportunities for NLP-enhanced bank
marketing strategies.
This research aims to systematically review and synthesize the literature on AI in bank marketing, with a particular
focus on uncovering the potential and opportunities of NLP within this field. Specifically, the goal is to examine how
NLP can enhance customer engagement, streamline operations, and improve decision-making. The aim is to identify
applications and opportunities for value creation and provide strategic recommendations for effective NLP utilization
by bank marketers.
Previous studies have reviewed NLP applications in general marketing (e.g., Berger et al. [2020], Mustak et al. [2021],
Shankar and Parsana [2022]), examining how automated textual analysis, topic modeling, and sentiment analysis can
generate strategic insights. Within finance, NLP reviews primarily address operational efficiency and consumer be-
havior (e.g., Kumar and Ravi [2016], Aziz et al. [2022]). However, few studies focus on the application of NLP
specifically in bank marketing, where unique challenges related to regulatory constraints and complex customer inter-
actions persist. This gap underscores the need for targeted research to explore how NLP can be adapted to the distinct
requirements of bank marketing.
This study contributes to the literature on AI in bank marketing as follows: First, using the PRISMA methodology
[Moher et al., 2009], it systematically reviews (1) AI and advanced analytics applications in bank marketing and (2)
NLP-specific implementations in general marketing, identifying current trends. Second, it combines both PRISMA
results in an AI-enhanced gap analysis to highlight underexplored areas and opportunities for NLP-based bank mar-
keting strategies. The gap analysis employs semantic mapping techniques, specifically Sentence Transformers with
UMAP, to uncover new research avenues and visualize the landscape of existing studies. Finally, the analysis shows
how NLP can transform customer engagement, marketing strategy, and operational excellence to drive growth and
innovation in banking.
2 Prisma Methodology and Data Collection
This section outlines the methodology for the first step of this study: the systematic review of AI applications in bank
marketing, focusing specifically on the potential of NLP.
2.1 PRISMA Methodology
This review follows the PRISMA (Preferred Reporting Items for Systematic Reviews and Meta-Analyses) framework
to thoroughly explore AI and NLP applications in bank marketing [Moher et al., 2009]. A detailed search strategy
is implemented using Scopus as the primary database for identifying the relevant literature. Scopus was selected
because of its extensive coverage of peer-reviewed journals in various disciplines, including finance, technology, and
marketing. The search strategy aimed to capture a broad spectrum of AI applications, particularly through digital
CRM and personalized marketing.
Marketing Banking
NLP
Query 1
Marketing Banking
NLP
Query 2
Marketing Banking
NLP
Query 3
Figure 1: Areas of interest for PRISMA.
The search strategy is illustrated in Figure 1, using Venn diagrams to depict three primary areas of exploration and
their intersections:
2

Leveraging AI and NLP for Bank Marketing
1. Query 1: Focuses on analytical marketing in the banking sector ( MarketingBanking), providing insights
into digital marketing strategies.
2. Query 2: Examines marketing and NLP ( MarketingNLP), aiming to reveal applications of text processing
and generation across industries.
3. Query 3: Targets the intersection of marketing, banking, and NLP (AllIntersect), crucial for identifying
gaps and opportunities in the literature.
This scheme provides a conceptual roadmap for identifying and analyzing studies within each intersection. The search
was operationalized through specific Boolean search queries detailed in Table 1. Although tailored to the areas and
intersections identified, these queries are kept deliberately broad to capture the maximum range of relevant literature.
Table 1: PRISMA Search Queries for AI Applications in Bank Marketing.
Identifier Search Query Description
MarketingQuery "marketing" OR "market analy*" OR "consumer be-
hav*" OR "sales analy*" OR "product recommend*"
OR "customer relation*" OR "CRM" OR "pricing"
OR "promotion" OR "personali*" OR "churn"
Encompasses broad aspects of analyti-
cal marketing, including customer rela-
tionships.
BankingQuery "bank*" OR "financ*" OR "loan" OR "credit" OR
"money"
Covers various facets of banking and fi-
nancial services.
NLPQuery "NLP" OR "natural language processing" OR "text
analy*" OR "sentiment analy*" OR "language
model*" OR "speech recog*" OR "chatbot*" OR
"LLM"
Focuses on different elements of NLP
and its applications.
MarketingBanking* MarketingQuery AND BankingQuery Involves the overlap of analytical mar-
keting in banking.
MarketingNLP* MarketingQuery AND NLPQuery Highlights the use of NLP in the realm
of marketing.
BankingNLP BankingQuery AND NLPQuery Explores the application of NLP in the
banking sector.
AllIntersect** MarketingQuery AND BankingQuery AND
NLPQuery
Represents the target of NLP-based
bank marketing.
*Key queries in the PRISMA framework for this study.
**Derived from combining individual query outcomes, eliminating a separate search.
The selection criteria were designed to ensure high-quality studies. Only peer-reviewed articles published between
2014 and 2024 were included, to reflect advancements in NLP after the introduction of Word2Vec [Mikolov et al.,
2013]. The criteria included journals ranked C or higher, according to the ABDC Journal Quality List, and conference
papers were excluded to maintain consistency and quality.
2.1.1 Data Extraction and Analysis
Data extraction and analysis were conducted in several iterations to ensure thorough coverage and understanding:
1. Identification: Initial database searches using the pre-defined Boolean queries yielded a preliminary pool of
records.
2. Screening: Records were screened based on titles and keywords, filtering out irrelevant studies and removing
duplicates.
3. Eligibility: Abstracts were reviewed for eligibility, focusing on analytical bank marketing and NLP-based
marketing. Only peer-reviewed journal articles were included.
4. Inclusion: The final selection of studies was based on their direct relevance to the research objectives.
5. Additional Sources: Additional studies relevant to the research field were included if not identified in the
initial search.
The iterative process led to a thematic synthesis that identified key themes in this first part of the study. Research gaps
will be identified at a later stage.
3

Leveraging AI and NLP for Bank Marketing
3 Findings from PRISMA Analysis
3.1 Bibliometric and Publication Analysis
The PRISMA flowchart, shown in Figure 2, visualizes the progression of records through the different phases of the
systematic review, specifically for Queries 1 and 2 ( MarketingBanking and MarketingNLP). These two queries
represent the key areas of focus for this initial step, exploring AI applications in bank marketing and NLP-based
marketing, respectively. The third query, AllIntersect, which represents the intersection of marketing, banking,
and NLP, yielded a limited number of studies. Therefore, this intersection will be analyzed in a later stage to identify
research gaps and potential opportunities as part of the gap analysis.
Identification
Screening
Eligibility
Included
Database records
identified (n=7940)
Title and
Keywords
screened (n=428)
Articles assessed
for eligibil-
ity (n=84)
Studies included
in review (n=35)
Records ex-
cluded (n=344)
(41 duplicate)
Articles ex-
cluded, with
reasons (n=52)
Additionally
included (n=3)
Database records
identified (n=5283)
Title and
Keywords
screened (n=680)
Articles assessed
for eligibil-
ity (n=106)
Studies included
in review (n=82)
Records ex-
cluded (n=574)
(56 duplicate)
Articles ex-
cluded, with
reasons (n=26)
Additionally
included (n=2)
Query 1: MarketingBanking Query 2: MarketingNLP
Figure 2: PRISMA Flowchart of Literature Selection.
The publication trend from 2014 to 2023 is illustrated in Figure 3, which highlights the yearly frequency of included
studies. The data reveals a consistent increase in publications for both MarketingBanking and MarketingNLP, with
notable growth in the last years. This trend indicates growing scholarly interest, possibly driven by methodologi-
cal innovations such as transformer-based language models and evolving industry demands for NLP technologies in
marketing.
4

Leveraging AI and NLP for Bank Marketing
2014 2015 2016 2017 2018 2019 2020 2021 2022 2023
Publication Year
0
2
5
7
10
12
15
17
20Number of Publications
Q1: Marketing & Banking
Q2: Marketing & NLP
Figure 3: Number of Publications per Year.
Table 2 aggregates the journals that currently prevail in the fields of analytical bank marketing and NLP-based general
marketing. The publication landscape is more concentrated in specialized journals than in broad multidisciplinary
journals.
Table 2: Publication Count in Marketing Research by Journal.
Query Journal Count
MarketingBanking
Expert Systems with Applications 5
Decision Support Systems 2
Knowledge-Based Systems 2
Journal of Business Research 2
MarketingNLP
Journal of Business Research 7
Journal of Retailing and Consumer Services 7
Technological Forecasting and Social Change 4
Journal of Marketing Analytics 4
Expert Systems with Applications 3
Knowledge-Based Systems 3
Electronic Commerce Research 3
Journal of Marketing 3
3.2 Thematic Classification
An exploratory analysis of the reviewed literature allowed us to group the two queries into three main dimensions:
CRM, marketing mix, and strategic insights. These dimensions are also supported by Kannan and Li [2017] and
Shankar and Parsana [2022]. This classification provides a structured approach to understanding how AI and NLP
enhance different aspects of bank marketing and lays the foundation for a deeper exploration of these themes in the
following sections. Table 3 presents the thematic distribution of the reviewed studies.
The CRM dimension highlights a stronger focus on retention over acquisition, underscoring banks’ emphasis on long-
term relationships. In the Marketing Mix, AI and NLP are primarily applied to product innovation and promotion,
while pricing and placement receive less focus. The Strategic Insights dimension captures AI and NLP’s role in
competitor and feedback analysis, which supports data-driven decision-making.
In the next subsection, we will classify the selected MarketingBanking papers and analyze them in detail to better
understand how each dimension shapes the application of AI and NLP in bank marketing.
5

Leveraging AI and NLP for Bank Marketing
Table 3: Thematic Distribution and Count of Empirical AI/NLP Studies in Marketing.
Area Category Main Focus MarketingBanking MarketingNLP
Actions CRM Customer Acquisition 2 1
CRM Customer Retention 12 4
Marketing Mix Product 1 10
Marketing Mix Price 2 3
Marketing Mix Place 1 0
Marketing Mix Promotion 10 20
Insights Strategic Insights Competitor Analysis 1 11
Strategic Insights Feedback Analysis 2 49
Strategic Insights Other Insights 10 14
3.3 Analytical Marketing in Banking (Prisma Query 1)
Building on the thematic classification, this section provides an in-depth analysis of the current research on the appli-
cation of AI and advanced analytics in bank marketing. It focuses on the three key areas previously identified: CRM,
marketing mix, and strategic insights. Within these areas, various research streams are aggregated according to the
predefined dimensions, allowing for a detailed exploration of how AI and NLP are being utilized. A detailed summary
of these research studies and their key focus areas is depicted in Table 4.
6

Leveraging AI and NLP for Bank MarketingTable 4: Chronology of Analytical Bank Marketing.
Study Aim Methods Data
Acquisition
Retention
Product
Price
Place
Promotion
Competition
Feedback
Other Insights
Gür Ali and Ar-
itürk [2014]
To improve customer churn prediction with horizon-
specific classifiers
Logistic Regression, Survival
Analysis, Cox Regression
Private Banking customer records
from a European bank
- ✓ - - - - - - -
Abdolvand et al.
[2015]
To integrate performance management and customer
management for strategic decision-making, measur-
ing the Customer Lifetime Value
Genetic K-means, Analytic Hier-
archical Processes, Data Envelop-
ment Analysis
Data from an Iranian commercial
retail bank
- - - - - - - - ✓
Musto et al.
[2015]
Improve advisory process in wealth management
with individualized asset allocation recommendation
framework
Case-based reasoning Financial Data from an experimen-
tal session with 1172 real users
- - ✓ - - ✓ - - -
Estrella-Ramón
et al. [2016]
Calculate a multi-product model of Customer Poten-
tial Value
Probit method 24 months of behavioral panel data
for 2,187 customers of a Spanish
bank
- - - - - - - - ✓
Quijano-Sanchez
and Liberatore
[2017]
To develop a decision support system (DSS) for client
acquisition applied to financial networks
Reliability Graph, Probability
Function, Projected Gradient
Descent, Maximum Reliability
Path Algorithm
Client and operations data from
Banco Santander, including rela-
tionship types, intensity, and expert
evaluations
✓ - - - - ( ✓) - - -
Schwartz et al.
[2017]
To develop a DSS for optimizing online display ad
impressions to maximize customer acquisition
Multi-Armed Bandit (Reinforce-
ment Learning), Hierarchical
Models, Thompson Sampling
Over 750 million ad impressions
data from a large retail bank’s on-
line display ad campaign
✓ - - - ✓ (✓) - - -
Michel et al.
[2017]
To improve the effectiveness and efficiency of cus-
tomer selection for direct marketing campaigns using
net scoring to forecast campaign-related uplifts
Decision Trees, χ2-statistic Empirical data from the financial
sector involving a dataset with
107,259 customers in the target
group
- ✓ - - - ✓ - - ✓
Afolabi et al.
[2017]
To help the banking industry in Nigeria perform so-
cial media competitive analysis and transform social
media data into actionable insights
Text mining, Sentiment analysis,
K-means clustering
Data from Facebook and Twitter
accounts of the five largest banks
in Nigeria
- - - - ( ✓) - ✓ - ( ✓)
Mosavi and Afsar
[2018]
To systematically integrate several data mining tech-
niques and management issues to analyze customer
value in Tejarat Bank branches in Iran
Fuzzy Analytic Hierarchy Process
(FAHP), K-means clustering, De-
cision tree, Support Vector Ma-
chine (SVM), Random forest
Demographic, frequency, money,
and trust attributes of customers
from Tejarat Bank branches in Iran
- - - - - - - - ✓
Chakrabarti et al.
[2018]
Analyzing user reviews to better understand the cor-
relation between RATER dimension sentiment scores
and user overall rating (customer satisfaction)
Logistic Regression, Sentiment
Analysis
Online reviews from
BankBazaar.com for three largest
private banks in India
- - - - - - - ✓ (✓)
Shirazi and Mo-
hammadi [2019]
Constructing a predictive churn model using big data
and analyze various aspects of customer behavior af-
fecting churn in the Canadian banking industry
Classification and Regression
Trees (CRT)
Structured archival data and un-
structured data (online web pages,
website visits, phone conversation
logs) from over 3 million customer
records
- ✓ - - - - - - -
Continued on next page
7

Leveraging AI and NLP for Bank Marketing
Study Aim Methods Data
Acquisition
Retention
Product
Price
Place
Promotion
Competition
Feedback
Other Insights
Bogaert et al.
[2019]
Evaluate multi-label classification techniques and rec-
ommender systems for cross-sell purposes in the fi-
nancial services sector
Multi-label classification tech-
niques (binary relevance, classifier
chains with base classifiers such
as Adaboost, random forest,
neural networks), Recommender
systems (user-based collaborative
filtering, item-based collaborative
filtering, association rules, popular
recommender method, random
recommender method)
Customer data from an interna-
tional financial services provider,
including 2,923,989 unique cus-
tomers and 6808 unique products
- - - - - ✓ - - -
Łady˙zy´nski et al.
[2019]
To develop a system for predicting customers’ will-
ingness to take a personal loan using deep learning
and random forests.
Random forests, Deep belief net-
works
Transactional and historical data
from a large retail bank in Poland
- - - - - ✓ - - -
Co¸ ser et al. [2020] Identifying key characteristics and predicting the like-
lihood of customer churn in banking
Logistic Regression, Random For-
est (with Grid Search optimization)
Bank customer data from Kaggle - ✓ - - - - - - -
De Caigny et al.
[2020]
Improve customer churn prediction by incorporating
textual data from customer communications
Logistic Regression, CNN Financial services provider data,
text messages
- ✓ - - - - - - -
Vélez et al. [2020] Forecasting customer churn and Net Promoter Score
(NPS) to improve decision-making and customer re-
tention
Logistic Regression, Stepwise Se-
lection, WOE Variables, Gradient
Boosting
Client survey data from a global
bank, client database records
- ✓ - - - - - - -
Hernández-Nieves
et al. [2020]
Developing a fog computing-based architecture to im-
prove personalized customer service through predic-
tive systems for recommending banking products
Fog computing architecture, Hy-
brid recommendation system,
CBR
Data from mobile devices, appli-
cations, and local bank equipment
processed through fog nodes with
intelligent agents
- - - - - ✓ - - -
Mancisidor et al.
[2021]
Improve marketing campaigns, customer relation-
ship management, data and process management, and
credit risk assessment by using V AE to learn latent
representations that reflect customers’ creditworthi-
ness
Variational Autoencoder (V AE),
AEVB algorithm, Weight of Evi-
dence (WoE) transformation
Norwegian and Finnish car loan
data, Kaggle "Give Me Some
Credit" dataset
- - - - - - - - ✓
V o et al. [2021] Develop a customer churn prediction model leverag-
ing unstructured data from customer call logs to en-
hance churn risk prediction accuracy and provide re-
tention insights
Text Mining with TF-IDF, Multi-
stacking ensemble (XGBoost, Lo-
gistic Regression, Random Forest,
Gaussian Naive Bayes)
Two million call logs from over
two hundred thousand customers,
provided by an Australian financial
services company
- ✓ - - - - - - ( ✓)
Piris and Gay
[2021]
To analyze customer feedback and identify key fac-
tors influencing customer satisfaction
Latent Dirichlet Allocation
(LDA), Data pre-processing,
Bag-of-Words (BoW), Term
Frequency-Inverse Document
Frequency (TF-IDF)
12,000 Customer Feedback An-
swers from a Bank Survey
- - - - - - - ✓ -
Ho et al. [2021] Examine the longitudinal relationships between cus-
tomer loyalty behaviors and firm financial outcomes
in the context of credit card usage
Sequence Analysis, Optimal
Matching, Cluster Analysis,
Activity-Based Costing (ABC)
Longitudinal dataset from a na-
tional bank in Taiwan, including
87,667 credit card customers
- ✓ - - - - - - -
Ban and Keskin
[2021]
Develop a personalized dynamic pricing model using
high-dimensional customer features to optimize pric-
ing and maximize revenue
Personalized demand model,
Semi-clairvoyant policy design,
Near-optimal pricing policy,
Lasso regularization, Maximum
quasi-likelihood regression
Simulated data, Real-life data from
an online auto loan company in the
United States
- - - ✓ - - - - ( ✓)
Continued on next page
8

Leveraging AI and NLP for Bank Marketing
Study Aim Methods Data
Acquisition
Retention
Product
Price
Place
Promotion
Competition
Feedback
Other Insights
Shumanov et al.
[2022]
Using AI predicted personality to enhance advertising
effectiveness
Mixed-method approach, AI algo-
rithms (GloVe, machine learning)
Retail banking customer data, sur-
vey responses, voice-to-text cus-
tomer interaction data
- - - - - ✓ - - ✓
AL-Najjar et al.
[2022]
Develop credit card customer churn prediction mod-
els using ML to generate early alerts for banks, en-
abling proactive customer retention strategies
Bayesian network, C5 tree,
CHAID tree, CR tree, neural
network, k-nearest neighbor
clustering
Credit card customer data from
Analyttica, 10,127 customers, 20
variables
- ✓ - - - - - - -
Kim et al. [2022] Validate stochastic customer base models in noncon-
tract settings for financial services
Pareto/NBD, Pareto/GGG,
BG/CNBD-k, MBG/CNBD-k
Transaction data from a nation-
wide financial services company in
Korea (2015-2018)
- ✓ - - - - - - ( ✓)
Valluri et al.
[2022]
Evaluate the effectiveness of ML techniques in pre-
dicting used auto loan churn among subprime borrow-
ers
Logistic Regression, Linear Dis-
criminant Analysis, Decision
Trees, Random Forests
Dataset from a Midwestern credit
union (2014-2016)
- ✓ - - - - - - ( ✓)
Feng et al. [2022] Proposing a dynamic ensemble selection method for
predicting bank telemarketing sales
META-DES-AAP (Dynamic En-
semble Selection, Multi-objective
Optimization)
Telemarketing dataset from a retail
bank in Portugal
- - - - - ✓ - - ✓
Tékouabou et al.
[2022]
Proposing a machine learning framework using the
CMB approach to predict the success of bank tele-
marketing campaigns by addressing data heterogene-
ity and feature preprocessing
Class Membership-Based (CMB)
Classifier
UCI Portuguese bank telemarket-
ing dataset (45,000 customers con-
tacted between 2008 and 2012)
- - - - ( ✓) ✓ - - ✓
Rouhani and Mo-
hammadi [2023]
Developing a hybrid model to predict customer churn
in the banking industry
Decision Tree (DT), Multinomial
Regression (MR), Hybrid DT-MR
Bank dataset (6507 customers, 10
months)
- ✓ - - - - - - -
Radovanovi´c et al.
[2023]
Proposing a fair classifier chain model for multi-label
classification in bank marketing strategies to address
fairness issues in predictive modeling
Fair Classifier Chain using Logis-
tic Regression
Historical data from bank market-
ing campaigns (2240 customers)
- - - - - ✓ - - ✓
Simsek and Tas
[2023]
Classifying and predicting customer churn in the
banking sector, with a focus on addressing data im-
balance for improved prediction accuracy.
Logistic Regression, K-Nearest
Neighbor, Support Vector Ma-
chine, Decision Tree, Random
Forest, Gradient Boosting Ma-
chines, LightGBM, XGBoost,
ROS-V oting (RF-LGBM)
Kaggle dataset of churning bank
customers
- ✓ - - - - - - ✓
Natesan et al.
[2023]
Formulating dynamic and static pricing models for
home loans to optimize net present value over 15
years using various demand functions and default
probability relationships
AMPL with MINOS solver,
quadratic programming, sensitiv-
ity analysis
Data from a nationalized bank in
India (demand for home loans over
different interest rates)
- - - ✓ - - - - -
Boustani et al.
[2023]
Improving the predictive accuracy of cross-selling
consumer loans in retail banking by utilizing deep
learning networks and account transaction data.
Deep Learning (Auto-encoder,
Neural Networks, Decision Trees,
SVM, Random Forest, Gradient
Boosting Machine, Heterogeneous
Ensemble)
Transaction data of 6127 individ-
ual customers from a Middle East-
ern bank, including demographics,
product ownership, and credit card
transactions
- - - - - ✓ - - -
9

Leveraging AI and NLP for Bank Marketing
3.3.1 Customer Relationship in AI-driven Bank Marketing
The enhancement of customer relationships through AI technologies exemplifies a multi-dimensional approach.
Specifically, AI has been instrumental in transforming how banks acquire and retain customers.
Customer Acquisition. AI-driven customer acquisition strategies have demonstrated significant potential for opti-
mizing marketing efforts. For instance, Quijano-Sanchez and Liberatore [2017] developed a decision support system
for Banco Santander, which utilized client and operational data to identify the most reliable sequences for client acqui-
sition and cross-selling. This decision support system employed state-of-the-art models, including a reliability graph
and a probability function, to optimize the client acquisition process. Similarly, Schwartz et al. [2017] optimized on-
line display ad impressions using multi-armed bandit methods and hierarchical models, achieving an 8% improvement
in customer acquisition without additional costs. Adaptive learning and real-time data optimization are thus effective
methods to enhance customer acquisition strategies in banks.
Customer Retention. Predictive models for customer retention have been instrumental in reducing churn rates, en-
abling banks to maintain a stable customer base and mitigate revenue losses. Various studies have employed advanced
AI and ML techniques to enhance these predictive models and develop effective retention strategies.
Gür Ali and Aritürk [2014] introduced a dynamic churn prediction framework using horizon-specific binary classifiers.
Their Multiple Period Training Data (MPTD) approach increased the size of the training data set and reduced the rarity
of churn events, thereby enhancing prediction accuracy. The study makes use of logistic regression, survival analysis,
and Cox regression on customer records from a European bank and specifically deals with rate churn events.
Leveraging big data analytics, Shirazi and Mohammadi [2019] developed a model to identify churn patterns among
retirees in the Canadian banking industry. By analyzing unstructured data from online web pages, website visits, and
phone conversation logs, the study provided a view of customer behavior, enabling targeted retention strategies. The
integration of diverse data sources has been a subject of investigation in the field of churn prediction modeling. Co¸ ser
et al. [2020] used a dataset from Kaggle consisting of 10,000 bank customer records with variables such as socio-
demographic characteristics, balance, estimated salary, and tenure. They forecast customer attrition using logistic
regression and random forest. The random forest classifier demonstrated superior predictive accuracy, enabling banks
to implement preemptive measures to retain valuable customers. De Caigny et al. [2020] enhanced churn prediction by
incorporating textual data from customer communications with advisors. The study improved the accuracy of churn
prediction models by using logistic regression and convolutional neural networks (CNNs), which provided deeper
insights into customer behavior and communication patterns.
Vélez et al. [2020] combined logistic regression, stepwise selection, and Weight of Evidence (WOE) variables to
forecast customer churn and Net Promoter Score (NPS). The study identified strong predictors, such as customer age
and the number of insurance contracts, which enabled targeted actions to retain customers. Similarly, V o et al. [2021]
leveraged unstructured call log data and text mining techniques, integrating features into a multi-stacking ensemble
model. This approach provided deeper insights into customer behavior and risk factors, enabling more effective and
personalized retention strategies.
Studies such as that of Ho et al. [2021] have focused on segmenting customers based on their loyalty behaviors to
develop targeted retention strategies. Employing sequence analysis, the research segments customers into six distinct
groups: Loyalist, Switching Loyalist, Switching Defector, Defector, Dormant Loyalist, and Dormant Defector. These
groups show varying profitability, allowing banks to allocate marketing resources more effectively. Tree-based models,
exemplified in the work of AL-Najjar et al. [2022] utilizing the C5 decision tree algorithm, are robust predictors of
customer churn. Their model identifies key predictors, such as total transaction count and revolving balance, which
can be used to inform proactive measures to retain customers and enhance stability.
Moreover, the efficacy of stochastic models in forecasting customer activity and retention in noncontractual settings
was validated by Kim et al. [2022] through the use of transaction data to classify active customers with high accuracy.
Valluri et al. [2022] evaluated the effectiveness of various ML techniques in predicting used auto loan churn among
subprime borrowers, identifying significant variables such as loan-to-value ratio and FICO credit score to inform the
development of targeted interventions.
Finally, hybrid models have demonstrated considerable potential for enhancing the accuracy of churn prediction.
Rouhani and Mohammadi [2023] combined decision trees and multinomial regression to categorize customers into
three distinct classes: non-churn, prone to churn, and churn. This approach yielded an average accuracy of 87.66%. In
addressing data imbalance in churn prediction, Simsek and Tas [2023] employed a hybrid model combining random
oversampling (ROS) and voting (RF-LGBM), achieving high accuracy (95%) and F1-score (0.95) and effectively
identifying at-risk customers.
10

Leveraging AI and NLP for Bank Marketing
Together, these studies collectively underscore the importance of leveraging advanced analytics and AI techniques to
enhance customer retention strategies in the banking sector. By accurately predicting customer churn and understand-
ing the underlying factors, banks can develop targeted interventions that maintain a stable customer base and improve
profitability.
3.3.2 Marketing Mix in AI-driven Bank Marketing
AI technologies enable banks to optimize the 4 P’s of the marketing mix, enhancing customer engagement, improving
operational efficiency, and driving revenue growth. This section explores how AI-driven approaches have the potential
to transform products, pricing strategies, channel selection, and promotional activities.
Product Innovation. Musto et al. [2015] explored the enhancement of financial advisory services in wealth man-
agement through individualized asset allocation recommendations. To this end, they employed case-based reasoning
and diversification strategies, with the objective of creating personalized investment portfolios. The results of their
investigation demonstrated that these AI-driven portfolios could align with clients’ risk profiles and potentially offer
superior yields compared to traditional human advisor recommendations. Consequently, they concluded that the use
of AI in wealth management could improve the advisory process.
Pricing Strategies. In their respective studies, Ban and Keskin [2021] and Natesan et al. [2023] explored dynamic
pricing models with the objective of optimizing revenue. Ban and Keskin [2021] demonstrated the effectiveness of
personalized dynamic pricing using high-dimensional customer features and heterogeneous price elasticity. The study
employed machine learning (ML) techniques such as lasso regularization and maximum quasi-likelihood regression,
achieving a 47% increase in expected revenue over a six-month period. Natesan et al. [2023] formulated dynamic and
static pricing models for home loans to optimize the net present value (NPV) of cash flows over a 15-year period. The
study used data from a nationalized bank in India, employing quadratic programming. The dynamic pricing model
generally yielded higher expected revenue compared to the static model, particularly for linear demand functions. This
suggested that continuously adjusting loan interest rates in response to market conditions could significantly enhance
a bank’s revenue.
Place Strategies. Schwartz et al. [2017] addressed optimal channel selection by optimizing online display ad im-
pressions to improve customer acquisition rates. Using multi-armed bandit (MAB) methods and hierarchical models,
the study dynamically adjusted ad placements based on real-time data, addressing the "learn-and-earn" trade-off.
Implemented in a live field experiment, the system achieved an 8% improvement in customer acquisition without
additional costs, highlighting its effectiveness in enhancing customer acquisition strategies through adaptive learning
and real-time data optimization.
Promotional Activities. The application of AI has significantly enhanced the efficacy of promotional strategies of
banks. AI-driven marketing efforts are now more personalized and efficient than traditional methods. For instance,
Musto et al. [2015] demonstrated how AI can be leveraged to enhance wealth management. This was achieved by uti-
lizing AI for individualized investment recommendations through case-based reasoning and diversification strategies.
These approaches yielded superior yields and more closely aligned with clients’ risk profiles than traditional methods.
Michel et al. [2017] optimized direct marketing campaigns by using decision trees and a newχ2-statistic to accurately
forecast campaign-related uplifts, identifying customers likely to respond positively. This approach maximized cam-
paign impact and efficiency. Bogaert et al. [2019] compared multi-label classification techniques and recommender
systems. Their findings indicated that user-based collaborative filtering and classifier chains with Adaboost were the
most effective for cross-selling in the financial sector. These methods enhanced the prediction and recommendation of
pertinent products to customers.
In retail banking, Łady˙zy´nski et al. [2019] utilized ML models, including random forests and deep belief networks, to
predict customers’ likelihood of purchasing credit products. This approach allowed for optimal timing and personal-
ized offers, increasing the effectiveness of direct marketing campaigns. Hernández-Nieves et al. [2020] integrated fog
computing and hybrid recommendation methodologies to provide real-time, personalized product suggestions, such
as mortgages and loans. This innovative system enhanced customer satisfaction and conversion rates by ensuring the
delivery of timely and relevant product recommendations.
Shumanov et al. [2022] enhanced advertising effectiveness by predicting consumer personality traits and matching
them with congruent advertising messages. The study employed AI techniques, including Global Vectors for Word
Representation (GloVe) and other ML algorithms, to infer personality traits from voice-to-text customer interaction
data. This approach provides a scalable method for enhancing marketing communications and validating AI for
11

Leveraging AI and NLP for Bank Marketing
accurate personality profiling. The results indicate that extroverted consumers demonstrated a greater responsiveness
to advertisements that evoked excitement and social rewards, whereas neurotic consumers exhibited a preference for
messages that reduced perceived risks and provided social acceptance cues. This tailored advertising approach led to
a notable improvement in click-through and conversion rates.
Feng et al. [2022] aimed to enhance the efficacy of bank telemarketing sales through the implementation of a dynamic
ensemble selection method (META-DES-AAP). This method considered both the accuracy and the average profit of
the telemarketing campaigns. The insights gained from this method enabled more informed and strategic marketing
decisions. Tékouabou et al. [2022] employed a Class Membership-Based (CMB) classifier to improve the prediction
of successful telemarketing campaigns. The CMB approach, which processes heterogeneous data such as age, marital
status, and educational level, achieved high accuracy (97.3%) and an AUC score (95.9%) through precise targeting of
potential customers.
The ethical considerations of promotional activities were addressed by Radovanovi ´c et al. [2023], who introduced a
fair classifier chain approach to avoid gender bias in predictive models. The study highlighted a trade-off between
increased fairness (by 7% to 17%) and a slight decrease in predictive performance (up to 9% in AUC), emphasizing
the importance of ethical considerations in marketing strategies.
Finally, Boustani et al. [2023] demonstrated the value of transaction data in improving cross-selling models using deep
learning networks. By analyzing nearly 800,000 credit card transactions, the study showed that integrating transaction
data with demographic and product ownership data significantly enhanced predictive accuracy. The heterogeneous
ensemble model achieved an AUC of 0.932, highlighting the potential for optimized promotional efforts in retail
banking.
3.3.3 Strategic Insights in AI-driven Bank Marketing
With AI, banks extend marketing beyond traditional metrics, offering insights into competitors and customers. This
knowledge streamlines decision-making for market positioning.
Competitor Analysis. Afolabi et al. [2017] demonstrated the use of social media data for competitive analysis in
Nigeria’s banking industry. By employing text mining, sentiment analysis, and k-means clustering techniques, the
study analyzed unstructured text content from Facebook and X/Twitter accounts of the largest banks. This analy-
sis provided deep insights into customer sentiments and engagement, enabling banks to understand their competitive
positioning and devise strategic marketing initiatives. The study demonstrates the potential for banks to make in-
formed decisions and enhance their competitive edge in the market by transforming social media data into actionable
knowledge.
Feedback Analysis. In order to gain knowledge about the service quality and satisfaction of customers, the study
conducted by Chakrabarti et al. [2018] analyzed online customer reviews. The analysis was conducted using sentiment
analysis, which enabled the researchers to identify the dimensions of service that had the greatest impact on customer
satisfaction. These dimensions included responsiveness and tangibles. Similarly, Piris and Gay [2021] utilized topic
modeling to analyze customer feedback from a bank’s satisfaction survey, identifying key topics that influence satis-
faction levels.
Other Insights. Beyond competitor and feedback analysis, AI-driven analytics generate valuable insights that en-
hance customer relationships and profitability in banking. Abdolvand et al. [2015] proposed integrating performance
management with customer management using Customer Lifetime Value (CLV) as a financial metric. This integrative
approach employed a variety of techniques, including genetic K-means, analytic hierarchical processes, and data en-
velopment analysis, to segment customers into distinct clusters. Estrella-Ramón et al. [2016] calculated a Customer
Potential Value (CPV) through a probit model and panel data of Spanish banks. The researchers identified a number of
key determinants of future profits, including the length of the relationship, product usage, and cross-buying behavior.
Furthermore, Mosavi and Afsar [2018] utilized data mining techniques, including fuzzy analytic hierarchy process
(FAHP) and K-means clustering, to construct a customer value pyramid. This approach yielded valuable insights into
customer behavior and preferences, thereby facilitating the development of more effective customer relationship man-
agement strategies. Additionally, Mancisidor et al. [2021] employed a Variational Autoencoder (V AE) to learn latent
representations of bank customers’ data, specifically to reflect their creditworthiness. By transforming the input data
using Weight of Evidence (WoE), the V AE created meaningful latent spaces that clustered customers based on their
likelihood of default. This clustering allowed banks to better understand customer segments and to enable a more
efficient customer relationship management. These customer insights are frequently linked with subsequent marketing
actions for profit generation.
12

Leveraging AI and NLP for Bank Marketing
3.4 Natural Language Processing in Marketing (Prisma Query 2)
Following the analysis of AI applications in bank marketing, we now turn to the broader landscape of general mar-
keting studies utilizing NLP (MarketingNLP). As a subset of AI, NLP has been widely used to analyze and interpret
human language in various marketing contexts. Inspired by Berger et al. [2020], we begin by examining the Textual
Universe in Marketing, focusing on text producers and receivers, including sources like social media posts, customer
reviews, and call logs. Understanding these data flows is crucial for effective NLP applications. Next, we explore
NLP models and techniques for Decoding Texts in Marketing, such as sentiment analysis and topic modeling, which
are essential for generating insights. After the publication of Berger et al. [2020], transformer-based models have
further revolutionized the field of NLP, adding new capabilities not covered in their analysis. Finally, we categorize
the reviewed studies by industry sectors to identify potential improvements in banking from other sectors. This second
PRISMA review provides the basis for our subsequent gap analysis, which will delve into further applications of NLP
in bank marketing.
3.4.1 Textual Universe in Marketing
To effectively apply NLP in marketing, it is crucial to understand the sources of textual data. Following Berger et al.
[2020], we distinguish between text producers and receivers, focusing primarily on firms and customers as the key
stakeholders.
Table 5 categorizes the types of texts produced and received by firms and customers, based on the textual data used in
the included studies. It illustrates the diversity of textual data available for NLP in analytical marketing. As shown,
a substantial portion of the text generated in marketing originates from customers, such as feedback, reviews, social
media posts, and user-generated content. These sources are heavily researched for understanding customer sentiment
and behavior. Firms, as the primary recipients, derive actionable insights and business value from these data sources,
although other customers may also consume the content.
Firms also produce text, with a more balanced distribution between customers and internal recipients. Direct commu-
nication with customers, such as marketing messages, online ads, chatbot interactions, and content marketing tweets,
has emerged as a significant area of interest. Internally, firms generate reports and operational texts.
13

Leveraging AI and NLP for Bank Marketing
Table 5: Types of Texts Produced and Received by Firms and Customers.
Text Receiver
Text Producer Firm Customer
Firm Reports and Logs :
• Annual Reports and Financial Filings [Cooper et al., 2022, Han et al., 2021]
• Customer Call Notes and Interaction Logs [Ozan, 2021, Shumanov et al., 2022]
Internal Operations:
• Marketing Prompt Templates and Brand Communications [Tafesse and Wood, 2024]
Customer Communications:
• Marketing Messages and Online Ads [Atalay et al., 2023, Wu et al., 2022]
• Chatbot and V oice Agent Interactions [Kushwaha and Kar, 2021, Rhee and Choi, 2020]
• Content Marketing Tweets [Barbosa et al., 2023, Batta et al., 2023, Galiano-Coronil et al.,
2023, Liu et al., 2021, Gruss et al., 2020, Hu et al., 2019]
• Email Campaign and Advertising Materials [Atalay et al., 2023, Wu et al., 2022]
• Newsletters and Social Media Posts
Marketing Content:
• SEO Texts for Website Landing Pages [Reisenbichler et al., 2022]
Customer Feedback and Reviews :
• Customer Reviews from Various Platforms [Marandi et al., 2024, Le et al., 2024, Nicolau
et al., 2024, Liu et al., 2024, Zhai et al., 2024, Park et al., 2023, Karn et al., 2023, Barbosa
et al., 2023, Han et al., 2023, Solairaj et al., 2023, Batta et al., 2023, Khan et al., 2023, Liu
et al., 2023, Yazıcı and Ozansoy Çadırcı, 2023, Loupos et al., 2023, Rahimi et al., 2022,
Sun et al., 2022, Aldunate et al., 2022, Guha Majumder et al., 2022, Kim et al., 2022,
Garner et al., 2022, Alzate et al., 2022, Alantari et al., 2022, Zhang et al., 2022, Farzadnia
and Raeesi Vanani, 2022, Vassilikopoulou et al., 2022, Celuch, 2021, Karthik and Gana-
pathy, 2021, Shambour, 2021, Heidary Dahooie et al., 2021, Zhang et al., 2021, Ghasemi
and Momtazi, 2021, Situmeang et al., 2020, Deng, 2020, Timoshenko and Hauser, 2019,
Lawani et al., 2019, Kim et al., 2019, Zhang et al., 2018, Dubey et al., 2017, Ma et al.,
2017, Lee et al., 2016, Xiang et al., 2015, Li et al., 2015, Yang et al., 2015]
User-Generated Content:
• Social Media Posts and Tweets [Lappeman et al., 2022, Swaminathan et al., 2022,
Agrawal and Mittal, 2022, Lamrhari et al., 2022, Wu et al., 2022, Villarroel Ordenes
and Silipo, 2021, Fresneda et al., 2021, Gozuacik et al., 2021, Kushwaha and Kar, 2021,
Piris and Gay, 2021, Lopez et al., 2020, Missaoui et al., 2019, Cu et al., 2019, Chang
et al., 2019, Hu et al., 2019, Ghosh et al., 2018, Peláez et al., 2018, Afolabi et al., 2017,
Pathak and Pathak-Shelat, 2017, Balusamy et al., 2015]
Direct User Interaction:
• Electronic Messages to Client Advisors [De Caigny et al., 2020]
• Speech and Facial Expressions (video data) [Chen et al., 2022]
Social Media Interactions:
• Forum Posts and Discussions [Sun et al., 2022, Wu and Chang, 2020, Liu et al., 2019,
Homburg et al., 2015]
• Blog Posts
• Social Media Reviews
14

Leveraging AI and NLP for Bank Marketing
3.4.2 Decoding Texts in Marketing with NLP
NLP has revolutionized marketing by providing tools to analyze and interpret vast amounts of textual data. This
enables marketers to gain valuable insights into customer behavior, preferences, and sentiments. In this section, we
explore advanced NLP methodologies and their applications in marketing, as summarized in Table 6.
Sentiment and Emotion Analysis. A predominant area of interest within NLP studies in marketing is the investi-
gation of customer sentiment and emotions. Sentiment analysis is a technique that identifies and categorizes opinions
expressed in texts to determine the overall attitude of an individual or a group towards a particular product or brand.
This attitude can be represented numerically or classified into opinion polarity classes, which include positive, neutral,
and negative [Barbosa et al., 2023, Solairaj et al., 2023, Zhang et al., 2022, Lappeman et al., 2022, Guha Majumder
et al., 2022, Afolabi et al., 2017]. Such analysis is beneficial for providing timely feedback, managing brand reputation,
shaping marketing strategies, and gaining more profound insights into brand perception.
Aspect-Based Sentiment Analysis (ABSA) provides a more granular perspective compared to general sentiment anal-
ysis, allowing firms to identify specific features or aspects of products and services that drive customer satisfaction
[Liu et al., 2024, Lappeman et al., 2022, Vassilikopoulou et al., 2022]. This technique differentiates between different
aspects of products mentioned within the text, providing a targeted understanding of customer feedback.
An even more complex method for analyzing customer sentiments is Multimodal Emotion Recognition [Chen et al.,
2022]. This method interprets emotions through multiple data types, including speech-to-text and image data. This
represents the cutting-edge of sentiment analysis, offering deeper insights that can be used to tailor marketing strategies
effectively.
Sentiment Analysis is often integrated with other NLP methods, such as topic modeling, to enhance the understanding
of customer feedback [Barbosa et al., 2023].
Topic Modeling. Topic modeling is a set of techniques that can be used to identify hidden topics or trends within
textual datasets. In the field of marketing, topic modeling is employed to derive valuable insights about customers,
including customer preferences and market trends.
The majority of studies in this field employ Latent Dirichlet Allocation (LDA) with a fixed number k of latent topics
to be identified in a text corpus. LDA, for instance, has been effectively used by Le et al. [2024] and Barbosa et al.
[2023] to aid in market segmentation and trend analysis. For example, LDA has been applied to customer reviews and
social media posts to uncover underlying themes, enabling businesses to tailor their marketing strategies accordingly
[Nicolau et al., 2024].
Closely related to this is Correlated Topic Modeling (CTM), which allows for correlations between topics, providing
a nuanced understanding of thematic relationships within a dataset [Garner et al., 2022]. This approach is particularly
valuable for datasets where topics are likely to be interrelated, such as customer reviews spanning multiple product
categories.
Newer methods, such as transformer-based language models like BERT (Bidirectional Encoder Representations
from Transformers), are gaining popularity in the field of topic modeling and sentiment analysis [Yazıcı and Ozan-
soy Çadırcı, 2023]. By leveraging pre-trained embeddings, these models facilitate more accurate topic identification,
thereby improving the semantic understanding of text.
Natural Language Generation. The fields of Natural Language Generation (NLG), Conversational AI, and Gener-
ative AI (GenAI) have recently attracted significant interest from researchers and practitioners alike, with new appli-
cations in marketing emerging.
The rise of Large Language Models (LLMs) such as GPT has facilitated the creation of marketing content through
user prompts, offering a new level of versatility in text generation [Tafesse and Wood, 2024]. In marketing practice,
the underlying data and the desired outcome shape the complexity of the prompt engineering process. LLMs enable
marketers to create highly personalized content, enhancing customer engagement.
A related development is the integration of LLMs into customer-facing interactions, such as chatbots [Jin and Eastin,
2023, Kushwaha and Kar, 2021] or voice systems [Rhee and Choi, 2020]. LLMs can provide the textual basis and
analytics tools out of the box to handle customer queries and automate sales processes. These chatbots can simulate
human-like interactions, thereby improving customer satisfaction and engagement.
In addition to customer interactions, NLG can also generate high-quality SEO content, which is essential for im-
proving search engine rankings and attracting more visitors to websites. The use of transfer learning in this context
15

Leveraging AI and NLP for Bank Marketing
can further fine-tune models for specific domains, ensuring the generated content closely mirrors human-written text
[Reisenbichler et al., 2022].
Table 6: NLP Methods in Marketing Research.
Tools/Methods Description Studies
Sentiment and Emotion Analysis
General Sentiment
Analysis
Identifying and categorizing opinions expressed in a piece
of text to determine the author’s attitude. Widely used for
understanding customer feedback and overall sentiment to-
wards brands or products.
Nicolau et al. [2024], Park et al. [2023], Karn et al. [2023], Barbosa et al.
[2023], Han et al. [2023], Solairaj et al. [2023], Khan et al. [2023], Liu
et al. [2023], Galiano-Coronil et al. [2023], Rahimi et al. [2022], Sun et al.
[2022], Agrawal and Mittal [2022], Guha Majumder et al. [2022], Garner
et al. [2022], Lamrhari et al. [2022], Alzate et al. [2022], Alantari et al.
[2022], Wu et al. [2022], Zhang et al. [2022], Farzadnia and Raeesi Vanani
[2022], Celuch [2021], Karthik and Ganapathy [2021], Villarroel Ordenes
and Silipo [2021], Heidary Dahooie et al. [2021], Zhang et al. [2021], Lopez
et al. [2020], Wu and Chang [2020], Deng [2020], Lawani et al. [2019],
Kim et al. [2019], Cu et al. [2019], Ghosh et al. [2018], Peláez et al. [2018],
Afolabi et al. [2017], Dubey et al. [2017], Xiang et al. [2015], Balusamy
et al. [2015], Homburg et al. [2015], Yang et al. [2015]
Aspect-Based Senti-
ment Analysis (ABSA)
Analyzing sentiment with respect to specific aspects or fea-
tures of a product or service, providing a more granular
view of customer opinions.
Liu et al. [2024], Zhai et al. [2024], Aldunate et al. [2022], Lappeman et al.
[2022], Vassilikopoulou et al. [2022], Gozuacik et al. [2021], Liu et al.
[2019], Chang et al. [2019], Zhang et al. [2018], Ma et al. [2017], Lee et al.
[2016]
Multimodal Emotion
Recognition
Recognizing and categorizing emotions from multiple data
modalities.
Chen et al. [2022]
Topic Modeling
Latent Dirichlet Allo-
cation (LDA)
A generative statistical model allowing sets of observations
to be explained by unobserved groups, aiding in discover-
ing hidden topics within text data.
Le et al. [2024], Barbosa et al. [2023], Yazıcı and Ozansoy Çadırcı [2023],
Sun et al. [2022], Swaminathan et al. [2022], Lamrhari et al. [2022], Alzate
et al. [2022], Alantari et al. [2022], Wu et al. [2022], Zhang et al. [2022],
Farzadnia and Raeesi Vanani [2022], Celuch [2021], Piris and Gay [2021],
Situmeang et al. [2020], Wu and Chang [2020], Hu et al. [2019], Lee et al.
[2016]
Correlated Topic Mod-
eling (CTM)
Analyzing the latent topical structure in text data to capture
correlations among topics.
Garner et al. [2022]
BERT-Based Models Using BERT embeddings for improved semantic under-
standing.
Yazıcı and Ozansoy Çadırcı [2023]
Top2Vec Identifying topics using topic/word vectors. Yazıcı and Ozansoy Çadırcı [2023]
Structural Topic Mod-
elling (STM)
Incorporating metadata to improve topic discovery and seg-
ment characterization.
Fresneda et al. [2021]
Natural Language Generation
Large Language Mod-
els (LLMs)
Using LLMs for generating marketing content and au-
tomating customer interactions.
Tafesse and Wood [2024]
Chatbot Integration Developing chatbots to handle customer queries and auto-
mate responses.
Jin and Eastin [2023], Kushwaha and Kar [2021], Chiu and Chuang [2021],
Rhee and Choi [2020]
SEO Content Creation Creating website content optimized for search engines to
improve visibility and traffic.
Reisenbichler et al. [2022]
Other Text Mining Analyses
Text Classification Categorizing text into predefined categories for different in-
dividualized marketing tasks.
Marandi et al. [2024], Batta et al. [2023], Loupos et al. [2023], Liu et al.
[2021], Han et al. [2021], Ozan [2021], Gruss et al. [2020], De Caigny et al.
[2020], Hu et al. [2019]
Clustering Grouping texts based on similarities. Marandi et al. [2024], Alzate et al. [2022]
Syntactic Surprise
Analysis
Evaluating the unexpectedness of the syntactic structure
within a text.
Atalay et al. [2023]
Word Embedding
(Word2Vec)
Representing words in vector space based on their mean-
ings and context.
Ozan [2021], Timoshenko and Hauser [2019]
Word Frequency Anal-
ysis
Comparing the frequency of words in different datasets. Cooper et al. [2022]
Text Similarity Analy-
sis
Measuring the similarity between texts. Ghasemi and Momtazi [2021], Missaoui et al. [2019]
Emerging Pattern Min-
ing
Identifying patterns that show significant changes between
datasets or over time.
Li et al. [2015]
Semantic Entity Ex-
traction
Identifying and categorizing entities within text. Liu et al. [2023]
Text Parsing Detect and parse attributes/entities in texts. Cooper et al. [2022]
Visualizations
Word Clouds Creating word clouds based on textual data to visualize fre-
quently occurring terms.
Kim et al. [2022]
Perceptual Maps Using dimensionality reduction to plot data in 2D. Alzate et al. [2022], Lee et al. [2016]
Other Text Mining Analyses. A wide array of custom text mining techniques extends beyond the already presented
methods. Marketers can use advanced text classification techniques for categorizing customer feedback, detecting
emerging trends, and enhancing recommender systems. This extends beyond the capabilities of conventional sentiment
16

Leveraging AI and NLP for Bank Marketing
analysis or topic modeling. For instance, it becomes possible to create highly customized features and models to
predict customers’ intentions, such as the likelihood of a return visit to a hotel [Marandi et al., 2024]. In the context of
unstructured data, the architectures of these models are often complex. To capture non-trivial, nonlinear, and hidden
relationships within text data, deep neural networks are employed De Caigny et al. [2020]. These models are capable
of performing tasks such as sales forecasting or the construction of efficient recommender systems, as evidenced by
prior research [Shambour, 2021, Loupos et al., 2023, Missaoui et al., 2019].
Identifying similarities between customers, products, or brands can be performed by vector-based text similarity anal-
ysis. In order to achieve this, the respective text objects (words, sentences, collections of texts) are transformed into
embeddings. There are a number of different approaches that can be employed in this regard, including the use of word
embeddings with Word2Vec, document embeddings with Doc2Vec/Paragraph2Vec, and traditional lexical matching
techniques such as TF-IDF [Ghasemi and Momtazi, 2021]. In vectorized form, these objects can be compared and the
degree of similarity quantified. Word embeddings, for instance, can effectively capture semantic similarities between
customer interactions [Ozan, 2021, Han et al., 2021]. Additionally, using word embeddings enhances the understand-
ing of customer needs from reviews [Timoshenko and Hauser, 2019]. Clustering algorithms can then group similar
objects based on shared characteristics or behaviors, thus facilitating text-based customer and market segmentation.
This enables the categorization of customers into groups based on their reviews and feedback, as well as the segmen-
tation of brands into distinct markets [Marandi et al., 2024, Alzate et al., 2022]. Furthermore, text-based similarities
can be leveraged to build recommender systems based on collaborative filtering [Ghasemi and Momtazi, 2021].
Text parsing and entity extraction are also frequently used in NLP to structure information from unstructured text.
This is particularly relevant for corporate reports and documents, enabling firms to automate and streamline marketing
processes effectively [Cooper et al., 2022, Liu et al., 2023].
In addition to these techniques, syntactic surprise analysis and emerging pattern mining provide further capabilities
for custom marketing analyses. The application of syntactic surprise analysis allows for the evaluation of unexpected
syntactic structures within text. This can be used to improve the effectiveness of marketing messages through moderate
surprise [Atalay et al., 2023]. Emerging pattern mining focuses on significant changes in data patterns over time. With
this information, marketing strategies can be proactively adapted based on shifting customer behaviors and market
trends [Li et al., 2015].
Visualizations. Visualizations give marketers further guidance to effectively analyze unstructured textual data and
generate actionable insights. Techniques such as word clouds and perceptual maps help visualize frequently occurring
terms and relationships within data. Word clouds are a visual representation of the most frequently occurring terms in
text data and can provide an intuitive overview of customer feedback and reviews [Kim et al., 2022].
Perceptual Maps use dimensionality reduction to plot high-dimensional textual vector representations in a manner that
is comprehensible to humans, typically in two dimensions. Clusters and relationships in the data can then be identified
via the data points in the plot. In marketing, perceptional maps are used to illustrate customer preferences or brand
positioning in a competitive market [Alzate et al., 2022, Lee et al., 2016]. These maps reveal the relative positioning
of products or brands, thereby highlighting areas for potential improvement or differentiation.
3.4.3 NLP Studies by Industries
Table 7 summarizes NLP marketing studies by sector, highlighting the distribution of research efforts and sector-
specific trends. Examining these studies reveals that the majority of research is not focused on banking and finance.
By analyzing the approaches and findings from other sectors, we can identify valuable insights and methods that may
be applicable to improving NLP-based marketing in the banking sector.
Automotive. The automotive sector has effectively utilizedNLP to unveil consumer preferences and analyze product
defects through online reviews. Studies such as Liu et al. [2024], Sun et al. [2022], and Liu et al. [2019] emphasize the
importance of fine-grained sentiment analysis and consumer segmentation. These methodologies allow automotive
companies to improve product design, enhance customer relationship management, and develop targeted marketing
strategies. For instance, Liu et al. [2024] introduced a framework using graph neural networks for opinion pair gener-
ation to improve sentiment analysis accuracy. Sun et al. [2022] applied LDA, sentiment analysis, and cluster analysis
to segment consumers and identify key factors influencing purchasing behavior. Similarly, Liu et al. [2019] used
supervised learning and domain-specific sentiment analysis to analyze competitive advantages from user-generated
content.
E-commerce. E-commerce is the most extensively studied sector with 25 papers, demonstrating the versatile appli-
cations of NLP in this domain. The primary focus is onsentiment analysis, recommendation systems, and the impact of
17

Leveraging AI and NLP for Bank Marketing
Table 7: Overview of NLP Marketing Studies by Industry Sectors.
Sector Main Studies Count
Automotive Liu et al. [2024], Sun et al. [2022], Liu et al. [2019] 3
E-commerce Zhai et al. [2024], Karn et al. [2023], Solairaj et al. [2023], Batta et al. [2023], Jin and Eastin [2023], Liu et al.
[2023], Yazıcı and Ozansoy Çadırcı [2023], Sidlauskiene et al. [2023], Agrawal and Mittal [2022], Guha Ma-
jumder et al. [2022], Kim et al. [2022], Alantari et al. [2022], Chen et al. [2022], Karthik and Ganapathy
[2021], Heidary Dahooie et al. [2021], Kushwaha and Kar [2021], Ghasemi and Momtazi [2021], Rhee and
Choi [2020], Wu and Chang [2020], Kim et al. [2019], Timoshenko and Hauser [2019], Zhang et al. [2018],
Dubey et al. [2017], Ma et al. [2017], Yang et al. [2015]
25
Entertainment & Events Loupos et al. [2023], Celuch [2021], Deng [2020] 3
Financial Services * Li et al. [2023], Lappeman et al. [2022], Sajid et al. [2022], Shumanov et al. [2022], De Caigny et al. [2020],
Afolabi et al. [2017]
6
Food & Restaurants Han et al. [2023], Khan et al. [2023], Situmeang et al. [2020], Gruss et al. [2020] 4
Hospitality & Travel Marandi et al. [2024], Le et al. [2024], Nicolau et al. [2024], Rahimi et al. [2022], Garner et al. [2022], Farzadnia
and Raeesi Vanani [2022], Vassilikopoulou et al. [2022], Lawani et al. [2019], Missaoui et al. [2019], Chang
et al. [2019], Xiang et al. [2015], Li et al. [2015]
12
Retail Liu et al. [2021], Chiu and Chuang [2021], Han et al. [2021] 3
Technology & Electronics Park et al. [2023], Zhang et al. [2022], Gozuacik et al. [2021], Lee et al. [2016] 4
* The applications in financial services will be detailed in the gap analysis in section 4.
online reviews on consumer behavior. Studies like Zhai et al. [2024] and Solairaj et al. [2023] highlight how sentiment
analysis can extract consumer opinions from reviews, aiding in data-driven decisions to enhance customer satisfaction.
NLP has advanced recommendation systems, as seen in Karn et al. [2023] and Heidary Dahooie et al. [2021], which
use sentiment analysis to improve recommendation accuracy. AI-driven chatbots are also significant, with studies
like Jin and Eastin [2023] and Sidlauskiene et al. [2023] exploring their role in enhancing customer interaction and
personalizing shopping.
Analyzing customer feedback is crucial for refining marketing strategies. Wu and Chang [2020] and Yazıcı and Ozan-
soy Çadırcı [2023] used text-mining techniques to identify key topics and sentiments in reviews, providing insights
into customer preferences and areas for improvement. Cross-cultural and multilingual aspects are also considered, as
in Le et al. [2024], ensuring a comprehensive understanding of diverse customer bases.
Emerging technologies like voice shopping and multimodal content analysis are explored in studies such as Rhee and
Choi [2020] and Liu et al. [2023]. These innovations highlight the evolving landscape of e-commerce and the need
for continuous adaptation of new technologies. Overall, the extensive research in e-commerce demonstrates NLP’s
significant role in enhancing online shopping by improving customer experience, personalizing marketing efforts, and
driving sales through the effective use of NLP technologies.
Additionally, Timoshenko and Hauser [2019] demonstrates the use of NLP to identify customer needs and improve
product development across various industries. By analyzing user-generated content, companies can better under-
stand customer preferences and enhance their marketing strategies to address specific concerns and improve overall
satisfaction.
Entertainment & Events. NLP techniques are crucial in the Entertainment and Events sectors for analyzing cus-
tomer reviews to enhance service quality and predict performance. Studies like Loupos et al. [2023] and Deng [2020]
demonstrate the impact of pre-release reviews and online word-of-mouth on box office sales. Loupos et al. [2023]
highlights how critic reviews can predict movie success, while Deng [2020] shows the differing impacts of user and
critic reviews. In the events industry, Celuch [2021] uses sentiment analysis to identify key aspects valued by event-
goers, such as technical issues and customer support, aiding event organizers in improving the customer experience.
Food & Restaurant. NLP has been extensively applied in the food and restaurant sector to analyze customer feed-
back and improve service quality. Studies such as Han et al. [2023], Khan et al. [2023], Situmeang et al. [2020], and
Gruss et al. [2020] utilize sentiment analysis and topic modeling to understand customer sentiments and preferences.
For instance, Han et al. [2023] examined the link between social media marketing (SMM) performance indicators
and restaurant sales, finding that increased social media engagement positively correlates with sales revenue. Khan
et al. [2023] used text mining to analyze online reviews from a food delivery portal, identifying key factors such as
hygiene and pricing that influence delivery ratings. Situmeang et al. [2020] applied advanced text mining techniques to
uncover latent dimensions of customer satisfaction from online reviews, providing insights into service improvement.
18

Leveraging AI and NLP for Bank Marketing
Gruss et al. [2020] focused on the impact of social media post attributes on customer engagement, highlighting the
importance of community-building content.
Hospitality & Travel. The travel and hospitality sector leverages NLP to analyze customer reviews and enhance
service quality. Papers like Marandi et al. [2024], Le et al. [2024], and Nicolau et al. [2024] use sentiment analysis,
topic modeling, and other NLP techniques to understand customer preferences, improve service offerings, and increase
customer retention. By analyzing large volumes of textual data, hotels and travel companies can better meet customer
expectations and tailor their marketing strategies to different customer segments.
Studies such as Marandi et al. [2024] highlight the importance of identifying key hotel features that influence customer
revisit intentions. This involves analyzing customer feedback to extract relevant features and segmenting customers
based on their preferences. Similarly, Le et al. [2024] emphasizes the use of thevoice of the customer strategy to align
customer expectations with service delivery, employing business intelligence solutions for detailed analysis.
Furthermore, Nicolau et al. [2024] explores the impact of daily review sentiment on hotel performance metrics, sug-
gesting that sentiment analysis can serve as a real-time indicator of a hotel’s operational effectiveness. This approach
helps in dynamically adjusting pricing strategies to optimize revenue. Other studies, like Rahimi et al. [2022], investi-
gate gender differences in review content, providing insights into tailored marketing strategies.
Retail. The retail sector benefits from NLP through the analysis of customer engagement on social media andomni-
channel marketing strategies. Papers like Liu et al. [2021], Chiu and Chuang [2021], and Han et al. [2021] explore the
impact of social media activities and customer feedback on brand engagement and sales performance. Liu et al. [2021]
investigates the influence of various dimensions of a luxury brand’s social media activities on customer engagement,
emphasizing the importance of entertainment, interaction, and trendiness. Chiu and Chuang [2021] discusses the
development of anomni-channel chatbot using convolutional neural networks (CNNs) to enhance personalized service
and precision marketing. Han et al. [2021] uses textual analysis to measure brand and customer focus, revealing a
positive correlation between customer focus and profitability. These studies highlight the importance of understanding
customer interactions and preferences to refine marketing tactics and improve customer satisfaction, which can inspire
the banking sector to adopt similar approaches for enhancing customer engagement and loyalty.
Technology & Electronics. In the technology and electronics sector, studies such as Park et al. [2023], Zhang et al.
[2022], and Gozuacik et al. [2021] useNLP to analyze online reviews and social media content to understand customer
needs and product performance. Park et al. [2023] proposes a framework involving network analysis, topic modeling,
and sentiment analysis to identify meaningful opinions from smart speaker reviews, helping in product improvement
and brand positioning. Zhang et al. [2022] introduces a customer requirement identification framework using sentiment
polarity to categorize product attributes for better product design strategies. Gozuacik et al. [2021] utilizes sentiment
analysis and opinion retrieval from social media to support product development and innovation, exemplified by the
case of Google Glass. These insights help companies in product development, marketing strategy refinement, and
competitive analysis, ultimately leading to better customer satisfaction and increased market share.
The Banking and Financial Services sector has also conducted a limited number of NLP-related studies with a focus
on marketing. A more in-depth analysis combined with a gap analysis will be presented in the following section.
4 Gap Analysis
While our systematic review provided fruitful insights into the applications of analytical bank marketing and NLP
across a range of industries, our investigation into the intersection of these two areas has revealed notable gaps. The
literature search ( AllIntersect, Query 3) for studies specifically addressing NLP in bank marketing revealed a
lack of in-depth research with practical applications. This gap presents unique opportunities to enhance data-driven
decision-making and personalize customer experiences in banking, though regulatory constraints add challenges for
implementing NLP effectively in this field.
To conceptualize the research field, Figure 4 illustrates the convergence of the domains of marketing, banking, and
NLP.Engagement reflects the integration of marketing strategies to enhance the customer journey in the banking sector
[Kannan and Li, 2017]. Strategy demonstrates how NLP contributes to strategic decision-making by providing insights
from textual analysis [Berger et al., 2020]. Excellence emphasizes the role of NLP in optimizing banking processes,
improving efficiency, and reducing costs [Kumar and Ravi, 2016]. At the core intersection, Growth represents the
combined potential of all three domains to drive value and foster innovation in banking. These components form the
basis of our gap analysis, which explores and evaluates opportunities for NLP integration in bank marketing.
19

Leveraging AI and NLP for Bank Marketing
Customer Relationship
Marketing Insights
Marketing Mix
Banking Services
Financial Advisory
Risk ManagementEngagement
Sentiment Analysis
Text Generation
Topic Modeling
Strategy Excellence
Growth
Marketing Banking
NLP
Figure 4: The intersection of Marketing, Banking, and NLP.
4.1 Growth with NLP-Driven Marketing Strategies
Integrating NLP in bank marketing stimulates growth by enhancing data-driven decision-making and personalized
customer interactions. To gain a deeper insight into the potential applications of NLP within bank marketing, we
conducted an AI-based mapping and visualization of the existing MarketingBanking and MarketingNLP litera-
ture. A Sentence Transformer ( all-mpnet-base-v2) was employed to process each abstract from the included studies,
transforming them into high-dimensional vectors that capture semantic meanings. These vectors were then projected
into a two-dimensional space using the Uniform Manifold Approximation and Projection (UMAP) technique, which
preserves semantic relationships and allows for a visual representation of the research landscape.
The resulting visualization, presented in Figure 5, reveals both densely covered areas, indicating well-researched
topics, and sparsely populated areas that signify potential research gaps in NLP applications for bank marketing. To
identify prevalent themes and research interests, we performed manual labeling on the resulting clusters. We analyzed
the studies within the plot to determine relevant dimensions that best characterize the clustering patterns. Based on
these analyses, key dimensions and gaps were identified to guide future studies in NLP applications for bank marketing.
The map visually positions the identified marketing categories along two strategic axes. The first axis reflects the
Customer Focus vs. Strategic Focus dimension, as supported by prior research [Mustak et al., 2021]. A second axis,
Internal Focus vs. External Focus, emerges upon further analysis. The combination of these two dimensions provides
a detailed understanding of the positioning of the marketing landscape, offering deeper insights into the strategic
application of NLP within the banking sector.
The plot reveals clustering patterns corresponding to different marketing categories. TheAnalytical Marketing & NLP
category (MarketingNLP) is broadly distributed across the UMAP space, showing that NLP applications in marketing
are diverse and applied across a wide range of tasks. This distribution exhibits a skew towards the External Focus and
Strategic Focus quadrants, indicating that NLP techniques are frequently utilized to analyze external data sources with
strategic objectives in mind.
In contrast, the Analytical Marketing & Banking category (MarketingBanking) demonstrates a more concentrated
clustering within the Customer Focus and Internal Focus quadrants. This reflects the traditional focus of bank mar-
20

Leveraging AI and NLP for Bank Marketing
Acquisition
Competitor
Insights
Retention
Feedback
Product
Price
Promotion
Strategic Focus
Customer Focus
External
Focus
Internal
Focus
Q1: Marketing & Banking
Q2: Marketing & NLP
Q3: Marketing & Banking & NLP
Figure 5: Semantic Mapping of AI-driven Marketing Applications in Banking.
keting strategies, which are centered on customer needs and reliant on internal data sources. The overlapping studies
in the Analytical Marketing & Banking & NLP category (AllIntersect) highlight the suitability of integrating NLP
into bank marketing processes, spanning both Customer Focus and Strategic Focus areas.
In a more detailed examination, the UMAP projection reveals distinct patterns across multiple marketing categories,
as shown in Figure 6, which provides a category-wise comparison.
To illustrate, the Retention category is prominently positioned in the upper-middle section of the plot, close to the
axes of Customer Focus and Internal Focus. The concentration of research and applications in this area underscores
its pivotal role in banking. The Acquisition and Insights categories are located in close proximity to one another at
the center of the plot, which suggests that these categories are distributed across the two dimensions in a multifaceted
manner. This distribution encompasses both internal and external data, as well as a combination of direct customer
engagement and strategic focus. Similarly, the Price and Promotion categories are located at the center of the plot,
reflecting different research directions and data sources. The Product, Feedback, and Competitor categories are
more closely aligned with the strategic and external focus axis. This relationship can be attributed to the nature of
feedback as an external data source, which is often used to enhance product quality. Similarly, competitor analysis
requires access to external data, which is essential for informing strategic decisions. The Place category has been
excluded from the plot due to the assignment of only a single study to this category.
Some categories exhibit a considerable degree of variance within the plot, with studies from the same category being
distributed across different quadrants. This scatter variance is also displayed in Figure 6. It illustrates that, for instance,
the Insights category, which has a high variance score, is not concentrated in any particular dimension. In contrast, the
Product category demonstrates less scatter.
The UMAP plot illustrates the integration of NLP techniques in a multitude of applications in the analytical marketing
landscape. However, it also reveals several gaps where further NLP adoption could enhance bank marketing. Notably,
the underutilization of NLP in customer-centric applications, such as retention, acquisition, and customer insights,
suggests that banks may not be fully leveraging NLP to personalize and optimize customer interactions. Addressing
these gaps can enhance customer engagement and foster growth in banking, which we explore further in the following
subsection.
21

Leveraging AI and NLP for Bank Marketing
Acquisition
Scatter Variance: 7.69
Q1: Marketing & Banking
Q2: Marketing & NLP
Q3: Marketing & Banking & NLP
Competitor
Scatter Variance: 1.34
Q1: Marketing & Banking
Q2: Marketing & NLP
Q3: Marketing & Banking & NLP
Insights
Scatter Variance: 8.62
Q1: Marketing & Banking
Q2: Marketing & NLP
Q3: Marketing & Banking & NLP Retention
Scatter Variance: 4.29
Q1: Marketing & Banking
Q2: Marketing & NLP
Q3: Marketing & Banking & NLP
Feedback
Scatter Variance: 2.46
Q1: Marketing & Banking
Q2: Marketing & NLP
Q3: Marketing & Banking & NLP
Product
Scatter Variance: 2.21
Q1: Marketing & Banking
Q2: Marketing & NLP
Q3: Marketing & Banking & NLP
Price
Scatter Variance: 8.25
Q1: Marketing & Banking
Q2: Marketing & NLP
Q3: Marketing & Banking & NLP
Promotion
Scatter Variance: 5.05
Q1: Marketing & Banking
Q2: Marketing & NLP
Q3: Marketing & Banking & NLP
Figure 6: Multi-Category Comparison of Semantic UMAP Embeddings.
4.2 Growth with NLP-Driven Customer Engagement
To address the identified gaps in customer engagement, we now focus on theEngagement component of our conceptual
framework (Figure 4), analyzing how NLP can enhance customer interactions across the banking customer journey.
Adapting the customer journey framework by Kannan and Li [2017] to a financial setting, we consider the stages
of awareness, consideration, conversion, and retention. By mapping NLP applications onto these stages, we aim to
provide actionable recommendations for banks to enhance engagement throughout the customer lifecycle, ultimately
fostering stronger customer relationships and driving growth.
Figure 7 illustrates how NLP-driven marketing actions and strategic insights can enhance customer engagement at
each stage of the journey.
In the awareness stage, banks seek to attract potential customers and establish brand recognition. Our analysis in-
dicates that banks underutilize NLP in customer acquisition and competitor analysis. Traditionally, banks rely on
structured data, overlooking rich insights from unstructured data sources such as social media interactions and cus-
tomer reviews. This represents a missed opportunity to understand public perception and market trends.
22

Leveraging AI and NLP for Bank Marketing
ChurnPreventionRetention
Customer AcquisitionAwareness
Product Place PromotionConsideration
PriceConversion
Feedback Analysis
CompetitorAnalysis
Marketing InsightsMarketing Actions
Figure 7: NLP-Based Marketing Actions and Insights Across the Banking Customer Journey.
We recommend that banks employ NLP techniques like sentiment analysis and topic modeling on social media data
to gain real-time insights into customer sentiments and preferences [Afolabi et al., 2017, Lappeman et al., 2022]. By
identifying potential customers based on online behavior and sentiments, banks can enhance theircustomer acquisition
efforts. Additionally, leveraging NLP for dynamic adjustment of ad content and placement can improve engagement
and acquisition rates [Lamrhari et al., 2022]. For effective competitor analysis, banks should analyze competitors’
customer reviews using NLP to understand market positioning and identify areas for differentiation [Schwartz et al.,
2017, Quijano-Sanchez and Liberatore, 2017].
During the consideration stage, potential customers evaluate banking options. Personalization and relevant informa-
tion are crucial, yet banks often underutilize NLP for understanding customer needs in product development, person-
alizing promotions, and optimizing channels (place) for delivering marketing messages.
To bridge this gap, banks should analyze unstructured customer feedback, such as online reviews and surveys, using
NLP to inform product development [Zhang et al., 2022, Timoshenko and Hauser, 2019]. Techniques like sentiment
analysis and topic modeling can reveal customer preferences and areas for improvement, leading to products that
better align with customer expectations [Heidary Dahooie et al., 2021, Sun et al., 2022]. Furthermore, integrating
NLP-driven recommender systems allows banks to offer tailored financial products and personalize promotions, en-
hancing customer engagement [Shumanov et al., 2022, Tafesse and Wood, 2024]. Optimizing place involves using
NLP to analyze customer interactions across different platforms, enabling banks to deliver promotions through the
most effective channels [Schwartz et al., 2017].
At the conversion stage, customers decide to engage with a banking service. Here, price is often the primary deter-
mining factor due to the commoditized nature of banking products. However, banks rarely employ NLP to analyze
customer perceptions of pricing. Hence, they are missing opportunities to adjust pricing strategies based on customer
feedback.
We suggest that banks apply NLP to analyze customer feedback on pricing to gain insights into perceptions of price
fairness [Lawani et al., 2019, Zhai et al., 2024]. By examining sentiments related to pricing, banks can adapt their
price models to align with customer expectations, thereby optimizing conversion rates. Additionally, NLP can support
personalized pricing by analyzing customer interactions and behaviors, enabling a more responsive and customer-
centric approach [Chen et al., 2022].
The retention stage is concerned with the maintenance of long-term customer relationships. Banks often use ML to
detect churn signals such as reduced account activity [AL-Najjar et al., 2022], changes in spending [Co¸ ser et al., 2020],
and shifts in product usage [Shirazi and Mohammadi, 2019]. However, they often overlook insights from unstructured
data, such as emotional cues and context.
23

Leveraging AI and NLP for Bank Marketing
To enhance churn prevention and feedback analysis, banks should integrate NLP techniques to analyze unstructured
data sources like customer feedback, call center transcripts, and social media interactions. Recent studies have demon-
strated improved predictive accuracy and a deeper understanding of customer behavior when textual data is integrated
into the analytical process [De Caigny et al., 2020]. For instance, sentiment analysis of social media posts can reveal
early signs of dissatisfaction, enabling proactive interventions [Lappeman et al., 2022]. Analyzing call center logs
with NLP helps identify customer concerns and allows timely corrective actions [Rouhani and Mohammadi, 2023].
By combining NLP with structured data models, banks can develop more advanced churn prediction systems that cap-
ture both behavioral patterns and emotional indicators [V o et al., 2021, Lamrhari et al., 2022], ultimately enhancing
customer loyalty and satisfaction.
4.3 Growth with NLP-Driven Operational Excellence
Operational excellence is essential for banks seeking sustainable growth and competitive advantage. By optimizing
processes, reducing costs, and enhancing service quality, banks can improve financial profitability and build stronger
customer relationships. While pursuing these goals, banks must also consider regulatory compliance and ethical
standards as crucial preconditions, ensuring that NLP implementations are trustworthy and legally sound.
To structure our analysis, we draw on a value creation framework inspired by Kannan and Li [2017], focusing on three
dimensions: customer equity, value for the bank, and value for customers. Through our PRISMA-based literature
review, we systematically identified key components within this framework, categorizing insights related to NLP
applications in bank marketing. These insights align with elements of the marketing mix and highlight substantial
opportunities for NLP to drive operational excellence in banking.
Product Price Place Promotion
NLP
Brand Position Profitability Efficient Channels Customer Lifetime Customer Equity
Product
Innovation
Revenue
Optimization
Cost
Reduction
ROI
Improvement
Value for
the Bank
Personalized
Experience Fair Pricing Accessibility Relevant Content Value for Customers
Marketing Mix
Outcomes
Figure 8: Growth and Innovation Framework for NLP in Bank Marketing.
Figure 8 illustrates how NLP can be integrated into the marketing mix to create value across the three dimensions. The
concept of Customer Equity, as defined by Kannan and Li [2017], refers to the broader, long-term financial value
derived from customers through effective acquisition, retention, and profitability strategies. These strategies contribute
to sustained customer loyalty and higher margins over time. Value for the Bank refers to the economic benefits for
the bank, including metrics such as sales, profits, and growth rates. Value for Customers is defined as the perceived
benefit to the customer, encompassing improvements in financial value, brand trust, customer relationships, and overall
satisfaction. This value is directly experienced through the enhanced quality of products and services offered.
Enhancing Customer Equity with NLP. We recommend that banks leverage NLP to strategically position their
brand and tailor customer interactions, thereby improving marketing actions. By utilizing NLP-driven insights, banks
can enhance CLV , leading to higher profitability and stronger customer relationships over time. For instance, Ab-
dolvand et al. [2015] suggest integrating CLV as a key financial metric within CRM systems, using advanced cluster-
24

Leveraging AI and NLP for Bank Marketing
ing techniques to identify and retain high-value customers. Similarly, Mosavi and Afsar [2018] propose employing
data mining techniques to create a customer value pyramid, helping banks classify and optimize the value derived from
different customer segments, thereby maximizing CLV .
Moreover, banks should utilize NLP-driven insights to refine dynamic pricing strategies [Ban and Keskin, 2021]. By
predicting customer behavior and aligning pricing strategies with customer expectations, banks can boost individual
customer profitability and strengthen the overall equity of the customer base.
Driving Value for the Bank with NLP. To enhance financial success, banks should employ NLP to facilitate product
innovation, revenue optimization, and cost reduction. By analyzing customer feedback using NLP, banks can inform
product design strategies and ensure that new offerings are closely aligned with customer needs [Zhang et al., 2022,
Timoshenko and Hauser, 2019]. This approach is not only crucial for successful product launches but also contributes
to sustained revenue growth.
We recommend that banks adopt dynamic pricing models supported by NLP to adjust pricing in response to market
conditions and customer demand, optimizing revenue streams over time [Natesan et al., 2023]. Additionally, NLP
offers significant cost-reduction potential, particularly through digital channels and improved customer service systems
that streamline operations and reduce the need for manual intervention [Hernández-Nieves et al., 2020].
Furthermore, utilizing NLP in targeted marketing campaigns can significantly increase Return on Investment (ROI).
For example, Feng et al. [2022] propose a dynamic ensemble selection method that focuses on maximizing both
accuracy and profit in bank telemarketing campaigns, ensuring that marketing efforts are cost-effective and yield high
returns. By optimizing resource allocation and enhancing the precision of marketing strategies, banks can achieve
better financial outcomes.
Creating Value for Customers with NLP. Banks should leverage NLP to enhance the accessibility, inclusivity,
and quality of banking services by providing personalized experiences tailored to individual needs. Personalized
investment recommendations, driven by NLP, help customers make informed financial decisions that align with their
risk profiles and financial goals [Musto et al., 2015]. Additionally, integrating sentiment analysis with multi-criteria
decision-making ensures that product recommendations are relevant and valuable to each customer [Heidary Dahooie
et al., 2021].
Implementing fair pricing strategies is another critical area where NLP adds value for customers. By analyzing cus-
tomer reviews and quality metrics, banks can ensure that pricing is transparent and aligned with customer expectations
[Lawani et al., 2019], which is essential for maintaining trust and satisfaction in the banking sector.
Finally, delivering relevant content through NLP-driven strategies is crucial for customer engagement and satisfaction.
Banks should use NLG to create SEO-optimized content that improves search rankings and reduces costs [Reisen-
bichler et al., 2022]. Moreover, crafting marketing messages with an optimal level of syntactic surprise can effectively
drive customer engagement [Atalay et al., 2023]. Aligning chatbot personalities with user traits can further improve
customer satisfaction by delivering personalized, engaging content [Jin and Eastin, 2023]. By focusing on ethical con-
siderations, such as transparency in communication and data usage, banks can foster trust and ensure that interactions
uphold high standards of fairness and integrity.
5 Discussion and Conclusion
AI and NLP are reshaping marketing practices across various industries. However, the banking sector has yet to fully
capitalize on these technological advancements, particularly in marketing, due to unique challenges such as regulatory
constraints. This study addresses a notable gap in existing research by exploring the underutilized potential of NLP in
bank marketing, aiming to enhance customer engagement, boost operational efficiency, and support strategic decision-
making.
Through a PRISMA-based systematic review of existing literature on AI applications in bank marketing and NLP-
based marketing studies, we uncovered a noticeable scarcity of research at the intersection of these domains. Utilizing
advanced semantic mapping techniques, specifically Sentence Transformers with UMAP, we identified underexplored
areas where NLP can drive additional value creation in banking.
Our findings contribute to both theory and practice. Theoretically, we extend the current knowledge by connecting
general marketing frameworks with banking’s unique needs. We introduced a novel growth and innovation framework
for NLP integration in bank marketing, providing a conceptual model for future academic research. This framework
aligns NLP applications with the marketing mix and customer journey stages, offering a structured perspective on
how NLP can create value in banking. Practically, we offer actionable insights for banking professionals. By map-
25

Leveraging AI and NLP for Bank Marketing
ping NLP applications onto the banking customer journey (awareness, consideration, conversion, and retention) we
provide strategic recommendations for enhancing customer engagement and personalization. For instance, leveraging
sentiment analysis and topic modeling on social media data can improve customer acquisition efforts by identifying po-
tential customers and understanding their preferences in real-time. Additionally, integrating NLP-driven recommender
systems and personalized pricing strategies can optimize conversion rates and foster stronger customer relationships.
Our analysis also highlights the potential of NLP in driving operational excellence. By optimizing processes, reduc-
ing costs, and improving service quality, NLP has the potential to enhance both profitability and customer loyalty.
The proposed framework serves as a roadmap for banks to integrate NLP into their operational processes, aiming for
cost reduction and revenue optimization. In implementing these NLP-driven strategies, banks must ensure regula-
tory compliance and uphold ethical standards as prerequisites for maintaining customer trust and achieving long-term
success.
Despite the contributions, our study has limitations that open avenues for future research. The focus on peer-reviewed
articles may have excluded recent industry practices and insights presented in reports and conferences, potentially
limiting the comprehensiveness of our review. Moreover, the rapid evolution of AI and NLP calls for ongoing research
to keep pace with new advancements. Future studies should explore the application of NLP in personalized marketing
within the stringent regulatory constraints of the banking industry. Addressing ethical considerations, privacy issues,
and compliance requirements associated with NLP-driven marketing will be essential for sustainable implementation
in the industry.
References
Neda Abdolvand, Amir Albadvi, and Mohammad Aghdasi. Performance management using a value-based customer-
centered model. International Journal of Production Research, 53.0:5472.0–5483.0, 2015. doi: 10.1080/00207543.
2015.1026613.
Ibukun Tolulope Afolabi, Azubuike Ansalem Ezenwoke, and Charles K. Ayo. Competitive analysis of social media
data in the banking industry. International Journal of Internet Marketing and Advertising, 11.0:183.0–201.0, 2017.
doi: 10.1504/IJIMA.2017.085644.
Shiv Ratan Agrawal and Divya Mittal. Optimizing customer engagement content strategy in retail and e-tail: Available
on online product review videos.Journal of Retailing and Consumer Services, 67.0, 2022. doi: 10.1016/j.jretconser.
2022.102966.
Dana AL-Najjar, Nadia Al-Rousan, and Hazem AL-Najjar. Machine learning to develop credit card customer churn
prediction. Journal of Theoretical and Applied Electronic Commerce Research , 17.0:1529.0–1542.0, 2022. doi:
10.3390/jtaer17040077.
Huwail J. Alantari, Imran S. Currim, Yiting Deng, and Sameer Singh. An empirical comparison of machine learn-
ing methods for text-based sentiment analysis of online consumer reviews. International Journal of Research in
Marketing, 39.0:1.0–19.0, 2022. doi: 10.1016/j.ijresmar.2021.10.011.
Ángeles Aldunate, Sebastián Maldonado, Carla Vairetti, and Guillermo Armelini. Understanding customer satisfaction
via deep learning and natural language processing. Expert Systems with Applications, 209.0, 2022. doi: 10.1016/j.
eswa.2022.118309.
Miriam Alzate, Marta Arce-Urriza, and Javier Cebollada. Mining the text of online consumer reviews to analyze brand
image and brand positioning. Journal of Retailing and Consumer Services , 67.0, 2022. doi: 10.1016/j.jretconser.
2022.102989.
A. Selin Atalay, Siham El Kihal, and Florian Ellsaesser. Creating effective marketing messages through moderately
surprising syntax. Journal of Marketing, 87.0:755.0–775.0, 2023. doi: 10.1177/00222429231153582.
Saqib Aziz, Michael Dowling, Helmi Hammami, and Anke Piepenbrink. Machine learning in finance: A topic mod-
eling approach. European Financial Management, 28.0:744.0–770.0, 2022. doi: 10.1111/eufm.12326.
Balamurugan Balusamy, Thusitha Murali, Aishwarya Thangavelu, and P. Venkata Krishna. A multi-level text classifier
for feedback analysis using tweets to enhance product performance. International Journal of Electronic Marketing
and Retailing, 6.0:315.0–338.0, 2015. doi: 10.1504/IJEMR.2015.073455.
Gah-Yi Ban and N. Bora Keskin. Personalized dynamic pricing with machine learning: High-dimensional features
and heterogeneous elasticity. Management Science, 67.0:5549.0–5568.0, 2021. doi: 10.1287/mnsc.2020.3680.
Belém Barbosa, José Ramón Saura, Senka Borovac Zekan, and Domingo Ribeiro-Soriano. Defining content market-
ing and its influence on online user behavior: a data-driven prescriptive analytics method. Annals of Operations
Research, 2023. doi: 10.1007/s10479-023-05261-1.
26

Leveraging AI and NLP for Bank Marketing
Anuj Batta, Arpan Kumar Kar, and Shyamali Satpathy. Cross-platform analysis of seller performance and churn for
ecommerce using artificial intelligence. Journal of Global Information Management , 31.0, 2023. doi: 10.4018/
JGIM.322439.
Jonah Berger, Ashlee Humphreys, Stephan Ludwig, Wendy W. Moe, Oded Netzer, and David A. Schweidel. Unit-
ing the tribes: Using text for marketing insight. Journal of Marketing , 84.0:1.0–25.0, 2020. doi: 10.1177/
0022242919873106.
Matthias Bogaert, Justine Lootens, Dirk Van den Poel, and Michel Ballings. Evaluating multi-label classifiers and
recommender systems in the financial service sector. European Journal of Operational Research , 279.0:620.0–
634.0, 2019. doi: 10.1016/j.ejor.2019.05.037.
Noureddine Boustani, Ali Emrouznejad, Roya Gholami, Ozren Despic, and Athina Ioannou. Improving the predictive
accuracy of the cross-selling of consumer loans using deep learning networks. Annals of Operations Research ,
2023. doi: 10.1007/s10479-023-05209-5.
Krzysztof Celuch. Customers’ experience of purchasing event tickets: mining online reviews based on topic modeling
and sentiment analysis. International Journal of Event and Festival Management , 12.0:36.0–50.0, 2021. doi:
10.1108/IJEFM-06-2020-0034.
Somnath Chakrabarti, Deepak Trehan, and Mayank Makhija. Assessment of service quality using text mining –
evidence from private sector banks in india.International Journal of Bank Marketing, 36.0:594.0–615.0, 2018. doi:
10.1108/IJBM-04-2017-0070.
Yung-Chun Chang, Chih-Hao Ku, and Chun-Hung Chen. Social media analytics: Extracting and visualizing hilton
hotel ratings and reviews from tripadvisor. International Journal of Information Management , 48.0:263.0–279.0,
2019. doi: 10.1016/j.ijinfomgt.2017.11.001.
Jinyu Chen, Ziqi Zhong, Qindi Feng, and Lei Liu. The multimodal emotion information analysis of e-commerce
online pricing in electronic word of mouth. Journal of Global Information Management, 30.0, 2022. doi: 10.4018/
JGIM.315322.
Ming-Chuan Chiu and Kai-Hsiang Chuang. Applying transfer learning to achieve precision marketing in an omni-
channel system–a case study of a sharing kitchen platform. International Journal of Production Research , 59.0:
7594.0–7609.0, 2021. doi: 10.1080/00207543.2020.1868595.
Holly B. Cooper, Michael T. Ewing, and Sagarika Mishra. Text-mining 10-k (annual) reports: A guide for b2b
marketing research. Industrial Marketing Management, 107.0:204.0–211.0, 2022. doi: 10.1016/j.indmarman.2022.
10.001.
Alexandru Co¸ ser, Anamaria Aldea, Monica Mihaela Maer-Matei, and Levida Be¸ sir. Propensity to churn in banking:
What makes customers close the relationship with a bank? Economic Computation and Economic Cybernetics
Studies and Research, 54.0:77.0–94.0, 2020. doi: 10.24818/18423264/54.2.20.05.
Tung Cu, Helmut Schneider, and James Van Scotter. How does sentiment content of product reviews make diffusion
different? Journal of Computer Information Systems , 59.0:127.0–135.0, 2019. doi: 10.1080/08874417.2017.
1312636.
Arno De Caigny, Kristof Coussement, Koen W. De Bock, and Stefan Lessmann. Incorporating textual information in
customer churn prediction models based on a convolutional neural network. International Journal of Forecasting,
36.0:1563.0–1578.0, 2020. doi: 10.1016/j.ijforecast.2019.03.029.
Tianjie Deng. Investigating the effects of textual reviews from consumers and critics on movie sales. Online Informa-
tion Review, 44.0:1245.0–1265.0, 2020. doi: 10.1108/OIR-10-2019-0323.
Gaurav Dubey, Ajay Rana, and Jayanthi Ranjan. Fine-grained opinion mining of product review using sentiment and
semantic orientation. International Journal of Business Information Systems , 25.0:1.0–17.0, 2017. doi: 10.1504/
IJBIS.2017.083274.
Antonia Estrella-Ramón, Manuel Sánchez-Pérez, Gilbert Swinnen, and Koen Vanhoof. Estimating customer potential
value using panel data of a spanish bank. Journal of Business Economics and Management , 17.0:580.0–597.0,
2016. doi: 10.3846/16111699.2014.970571.
Siavash Farzadnia and Iman Raeesi Vanani. Identification of opinion trends using sentiment analysis of airlines pas-
sengers’ reviews. Journal of Air Transport Management, 103.0, 2022. doi: 10.1016/j.jairtraman.2022.102232.
Yi Feng, Yunqiang Yin, Dujuan Wang, and Lalitha Dhamotharan. A dynamic ensemble selection method for bank
telemarketing sales prediction. Journal of Business Research , 139.0:368.0–382.0, 2022. doi: 10.1016/j.jbusres.
2021.09.067.
27

Leveraging AI and NLP for Bank Marketing
Jorge E. Fresneda, Thomas A. Burnham, and Chelsey H. Hill. Structural topic modelling segmentation: a segmentation
method combining latent content and customer context. Journal of Marketing Management , 37.0:792.0–812.0,
2021. doi: 10.1080/0267257X.2021.1880464.
Araceli Galiano-Coronil, Alexander Aguirre Montero, Jose Antonio López Sánchez, and Rosario Díaz Ortega. Ex-
ploring social responsibility, social marketing and happiness using artificial intelligence, automated text analysis
and correspondence analysis. Management Decision, 2023. doi: 10.1108/MD-01-2023-0099.
Benjamin Garner, Corliss Thornton, Anita Luo Pawluk, Roberto Mora Cortez, Wesley Johnston, and Cesar Ayala.
Utilizing text-mining to explore consumer happiness within tourism destinations. Journal of Business Research ,
139.0:1366.0–1377.0, 2022. doi: 10.1016/j.jbusres.2021.08.025.
Negin Ghasemi and Saeedeh Momtazi. Neural text similarity of user reviews for improving collaborative filtering
recommender systems. Electronic Commerce Research and Applications, 45.0, 2021. doi: 10.1016/j.elerap.2020.
101019.
Amit K. Ghosh, Praveen Kotekal, and Goutam Chakraborty. Attribute-based sentiment analysis in marketing: Ap-
plication and strategic implications. Model Assisted Statistics and Applications , 13.0:311.0–318.0, 2018. doi:
10.3233/MAS-180441.
Necip Gozuacik, C. Okan Sakar, and Sercan Ozcan. Social media-based opinion retrieval for product analysis using
multi-task deep neural networks. Expert Systems with Applications, 183.0, 2021. doi: 10.1016/j.eswa.2021.115388.
Richard Gruss, Eojina Kim, and Alan Abrahams. Engaging restaurant customers on facebook: The power of be-
longingness appeals on social media. Journal of Hospitality and Tourism Research, 44.0:201.0–228.0, 2020. doi:
10.1177/1096348019892071.
Madhumita Guha Majumder, Sangita Dutta Gupta, and Justin Paul. Perceived usefulness of online customer reviews:
A review mining approach using machine learning & exploratory data analysis. Journal of Business Research ,
150.0:147.0–164.0, 2022. doi: 10.1016/j.jbusres.2022.06.012.
Özden Gür Ali and Umut Aritürk. Dynamic churn prediction framework with more effective use of rare event data:
The case of private banking. Expert Systems with Applications , 41.0:7889.0–7903.0, 2014. doi: 10.1016/j.eswa.
2014.06.018.
Simeng Han, Werner Reinartz, and Bernd Skiera. Capturing retailers’ brand and customer focus.Journal of Retailing,
97.0:582.0–596.0, 2021. doi: 10.1016/j.jretai.2021.01.001.
Wenjia Han, Ozgur Ozdemir, and Shivam Agarwal. Linking social media marketing to restaurant performance –
the moderating role of advertising expenditure. Journal of Hospitality and Tourism Insights, 2023. doi: 10.1108/
JHTI-03-2023-0217.
Jalil Heidary Dahooie, Romina Raafat, Ali Reza Qorbani, and Tugrul Daim. An intuitionistic fuzzy data-driven
product ranking model using sentiment analysis and multi-criteria decision-making. Technological Forecasting and
Social Change, 173.0, 2021. doi: 10.1016/j.techfore.2021.121158.
E. Hernández-Nieves, Guillermo Hernández, Ana-Belén Gil-González, Sara Rodríguez-González, and Juan M. Cor-
chado. Fog computing architecture for personalized recommendation of banking products. Expert Systems with
Applications, 140.0, 2020. doi: 10.1016/j.eswa.2019.112900.
Hillbun Ho, Keng-Ming Tien, Anne Wu, and Sonika Singh. A sequence analysis approach to segmenting credit card
customers. Journal of Retailing and Consumer Services, 59.0, 2021. doi: 10.1016/j.jretconser.2020.102391.
Christian Homburg, Laura Ehm, and Martin Artz. Measuring and managing consumer sentiment in an online commu-
nity environment. Journal of Marketing Research, 52.0:629.0–641.0, 2015. doi: 10.1509/jmr.11.0448.
Yuheng Hu, Anbang Xu, Yili Hong, David Gal, Vibha Sinha, and Rama Akkiraju. Generating business intelligence
through social media analytics: Measuring brand personality with consumer-, employee-, and firm-generated con-
tent. Journal of Management Information Systems, 36.0:893.0–930.0, 2019. doi: 10.1080/07421222.2019.1628908.
Eunjoo Jin and Matthew S. Eastin. Birds of a feather flock together: matched personality effects of product rec-
ommendation chatbots and users. Journal of Research in Interactive Marketing , 17.0:416.0–433.0, 2023. doi:
10.1108/JRIM-03-2022-0089.
P.K. Kannan and H. Alice Li. Digital marketing: A framework, review and research agenda, 3 2017. URL https://
papers.ssrn.com/abstract=3000712. 4 P’s - Product, Price, Place, Promotion==> Marketing ActionsProduct:
Customize ProductsPlace: Channel (Mobile, geographic, multi-channel)Promotion: Product recommendationValue
Creation = Value for Customers, Customer Equity, Value for the Firm.
28

Leveraging AI and NLP for Bank Marketing
Arodh Lal Karn, Rakshha Kumari Karna, Bhavana Raj Kondamudi, Girish Bagale, Denis A. Pustokhin, Irina V .
Pustokhina, and Sudhakar Sengan. Customer centric hybrid recommendation system for e-commerce applications
by integrating hybrid sentiment analysis. Electronic Commerce Research, 23.0:279.0–314.0, 2023. doi: 10.1007/
s10660-022-09630-z.
R.V . Karthik and Sannasi Ganapathy. A fuzzy recommendation system for predicting the customers interests using
sentiment analysis and ontology in e-commerce. Applied Soft Computing, 108.0, 2021. doi: 10.1016/j.asoc.2021.
107396.
Farheen Mujeeb Khan, Suhail Ahmad Khan, Khalid Shamim, Yuvika Gupta, and Shariq I. Sherwani. Analysing cus-
tomers’ reviews and ratings for online food deliveries: A text mining approach. International Journal of Consumer
Studies, 47.0:953.0–976.0, 2023. doi: 10.1111/ijcs.12877.
Taewook Kim, Dong Sung Kim, Donghyun Kim, and Jong Woo Kim. Multidimensional analysis of consumers’
opinions from online product reviews. Asia Pacific Journal of Information Systems, 29.0:838.0–855.0, 2019. doi:
10.14329/apjis.2019.29.4.838.
Takhun Kim, Dongyeon Kim, and Yongkil Ahn. Instant customer base analysis in the financial services sector.Expert
Systems with Applications, 202.0, 2022. doi: 10.1016/j.eswa.2022.117326.
B. Shravan Kumar and Vadlamani Ravi. A survey of the applications of text mining in financial domain. Knowledge-
Based Systems, 114.0:128.0–147.0, 2016. doi: 10.1016/j.knosys.2016.10.003.
Amit Kumar Kushwaha and Arpan Kumar Kar. Markbot – a language model-driven chatbot for interactive marketing
in post-modern world. Information Systems Frontiers, 2021. doi: 10.1007/s10796-021-10184-y.
Soumaya Lamrhari, Hamid El Ghazi, Mourad Oubrich, and Abdellatif El Faker. A social crm analytic framework for
improving customer retention, acquisition, and conversion. Technological Forecasting and Social Change, 174.0,
2022. doi: 10.1016/j.techfore.2021.121275.
James Lappeman, Michaela Franco, Victoria Warner, and Lara Sierra-Rubia. What social media sentiment tells
us about why customers churn. Journal of Consumer Marketing , 39.0:385.0–403.0, 2022. doi: 10.1108/
JCM-12-2019-3540.
Abdelaziz Lawani, Michael R. Reed, Tyler Mark, and Yuqing Zheng. Reviews and price on online platforms: Evidence
from sentiment analysis of airbnb reviews in boston.Regional Science and Urban Economics, 75.0:22.0–34.0, 2019.
doi: 10.1016/j.regsciurbeco.2018.11.003.
Thien Le, Thanh Ho, Van-Ho Nguyen, and Hoanh-Su Le. How to deeply understand the voice of the customer? a
proposal for a synthesis of techniques for analyzing online reviews in the hospitality industry.Journal of Hospitality
and Tourism Insights, 2024. doi: 10.1108/JHTI-07-2023-0460.
Anthony J.T. Lee, Fu-Chen Yang, Chao-Hung Chen, Chun-Sheng Wang, and Chih-Yuan Sun. Mining perceptual maps
from consumer reviews. Decision Support Systems, 82.0:12.0–25.0, 2016. doi: 10.1016/j.dss.2015.11.002.
Chia-Ying Li, Yu-Hui Fang, and Yu-Hung Chiang. Can ai chatbots help retain customers? an integrative perspective
using affordance theory and service-domain logic. Technological Forecasting and Social Change, 197.0, 2023. doi:
10.1016/j.techfore.2023.122921.
Gang Li, Rob Law, Huy Quan Vu, Jia Rong, and Xinyuan Zhao. Identifying emerging hotel preferences using emerging
pattern mining technique. Tourism Management, 46.0:311.0–321.0, 2015. doi: 10.1016/j.tourman.2014.06.015.
Kang Liu, Feng Xue, Dan Guo, Le Wu, Shujie Li, and Richang Hong. Megcf: Multimodal entity graph collaborative
filtering for personalized recommendation. ACM Transactions on Information Systems, 41.0, 2023. doi: 10.1145/
3544106.
Xia Liu, Hyunju Shin, and Alvin C. Burns. Examining the impact of luxury brand’s social media marketing on
customer engagement: Using big data analytics and natural language processing. Journal of Business Research ,
125.0:815.0–826.0, 2021. doi: 10.1016/j.jbusres.2019.04.042.
Yang Liu, Jiale Shi, Fei Huang, Jingrui Hou, and Chengzhi Zhang. Unveiling consumer preferences in automotive
reviews through aspect-based opinion generation. Journal of Retailing and Consumer Services , 77.0, 2024. doi:
10.1016/j.jretconser.2023.103605.
Yao Liu, Cuiqing Jiang, and Huimin Zhao. Assessing product competitive advantages from the perspective of
customers by mining user-generated content on social media. Decision Support Systems , 123.0, 2019. doi:
10.1016/j.dss.2019.113079.
Alberto Lopez, Eva Guerra, Beatriz Gonzalez, and Sergio Madero. Consumer sentiments toward brands: the interac-
tion effect between brand personality and sentiments on electronic word of mouth. Journal of Marketing Analytics,
8.0:203.0–223.0, 2020. doi: 10.1057/s41270-020-00085-5.
29

Leveraging AI and NLP for Bank Marketing
Pantelis Loupos, Yvette Peng, Sute Li, and Hao Hao. What reviews foretell about opening weekend box office
revenue: the harbinger of failure effect in the movie industry. Marketing Letters, 34.0:513.0–534.0, 2023. doi:
10.1007/s11002-023-09665-8.
Yue Ma, Guoqing Chen, and Qiang Wei. Finding users preferences from large-scale online reviews for personalized
recommendation. Electronic Commerce Research, 17.0:3.0–29.0, 2017. doi: 10.1007/s10660-016-9240-9.
Rogelio A. Mancisidor, Michael Kampffmeyer, Kjersti Aas, and Robert Jenssen. Learning latent representations of
bank customers with the variational autoencoder. Expert Systems with Applications , 164.0, 2021. doi: 10.1016/j.
eswa.2020.114020.
Aliakbar Marandi, Misagh Tasavori, and Manoochehr Najmi. New insights into hotel customer’s revisiting intentions,
based on big data. International Journal of Contemporary Hospitality Management, 36.0:292.0–311.0, 2024. doi:
10.1108/IJCHM-06-2022-0719.
René Michel, Igor Schnakenburg, and Tobias von Martens. Effective customer selection for marketing cam-
paigns based on net scores. Journal of Research in Interactive Marketing , 11.0:2.0–15.0, 2017. doi: 10.1108/
JRIM-10-2015-0080.
Tomas Mikolov, Kai Chen, Greg Corrado, and Jeffrey Dean. Efficient estimation of word representations in vector
space, 2013. URL https://arxiv.org/abs/1301.3781.
Sondess Missaoui, Faten Kassem, Marco Viviani, Alessandra Agostini, Rim Faiz, and Gabriella Pasi. Looker: a
mobile, personalized recommender system in the tourism domain based on social media user-generated content.
Personal and Ubiquitous Computing, 23.0:181.0–197.0, 2019. doi: 10.1007/s00779-018-01194-w.
David Moher, Alessandro Liberati, Jennifer Tetzlaff, Douglas G. Altman, Gerd Antes, David Atkins, Virginia Bar-
bour, Nick Barrowman, Jesse A. Berlin, Jocalyn Clark, Mike Clarke, Deborah Cook, Roberto D’Amico, Jonathan J.
Deeks, P. J. Devereaux, Kay Dickersin, Matthias Egger, Edzard Ernst, Peter C. Gøtzsche, Jeremy Grimshaw,
Gordon Guyatt, Julian Higgins, John P.A. Ioannidis, Jos Kleijnen, Tom Lang, Nicola Magrini, David McNamee,
Lorenzo Moja, Cynthia Mulrow, Maryann Napoli, Andy Oxman, Bá Pham, Drummond Rennie, Margaret Samp-
son, Kenneth F. Schulz, Paul G. Shekelle, David Tovey, and Peter Tugwell. Preferred reporting items for sys-
tematic reviews and meta-analyses: the prisma statement. PLoS medicine , 6, 7 2009. ISSN 1549-1676. doi:
10.1371/JOURNAL.PMED.1000097. URL https://pubmed.ncbi.nlm.nih.gov/19621072/.
A.B. Mosavi and A. Afsar. Customer value analysis in banks using data mining and fuzzy analytic hierarchy
processes. International Journal of Information Technology and Decision Making , 17:819–840, 2018. doi:
10.1142/S0219622018500104.
Mekhail Mustak, Joni Salminen, Loïc Plé, and Jochen Wirtz. Artificial intelligence in marketing: Topic modeling,
scientometric analysis, and research agenda. Journal of Business Research, 124.0:389.0–404.0, 2021. doi: 10.1016/
j.jbusres.2020.10.044.
Cataldo Musto, Giovanni Semeraro, Pasquale Lops, Marco De Gemmis, and Georgios Lekkas. Personalized finance
advisory through case-based recommender systems and diversification strategies. Decision Support Systems, 77.0:
100.0–111.0, 2015. doi: 10.1016/j.dss.2015.06.001.
Sumeetha Natesan, Deepika Thakur, Goutam Dutta, and Manoj Kumar Tiwari. Pricing and revenue manage-
ment for bank home loans: a mathematical approach. OPSEARCH, 60.0:656.0–687.0, 2023. doi: 10.1007/
s12597-023-00624-5.
Juan Luis Nicolau, Zheng Xiang, and Dan Wang. Daily online review sentiment and hotel performance.International
Journal of Contemporary Hospitality Management, 36.0:790.0–811.0, 2024. doi: 10.1108/IJCHM-05-2022-0594.
¸ Sükrü Ozan. Case studies on using natural language processing techniques in customer relationship management
software. Journal of Intelligent Information Systems, 56.0:233.0–253.0, 2021. doi: 10.1007/s10844-020-00619-4.
Jeongeun Park, Donguk Yang, and Ha Young Kim. Text mining-based four-step framework for smart speaker product
improvement and sales planning.Journal of Retailing and Consumer Services, 71.0, 2023. doi: 10.1016/j.jretconser.
2022.103186.
Xema Pathak and Manisha Pathak-Shelat. Sentiment analysis of virtual brand communities for effective tribal mar-
keting. Journal of Research in Interactive Marketing, 11.0:16.0–38.0, 2017. doi: 10.1108/JRIM-09-2015-0069.
Jose Ignacio Peláez, Francisco E. Cabrera, and L.G. Vargas. Estimating the importance of consumer purchasing criteria
in digital ecosystems. Knowledge-Based Systems, 162.0:252.0–264.0, 2018. doi: 10.1016/j.knosys.2018.07.023.
Yolande Piris and Anne-Cécile Gay. Customer satisfaction and natural language processing. Journal of Business
Research, 124.0:264.0–271.0, 2021. doi: 10.1016/j.jbusres.2020.11.065.
30

Leveraging AI and NLP for Bank Marketing
Lara Quijano-Sanchez and Federico Liberatore. The big chase: A decision support system for client acquisition
applied to financial networks. Decision Support Systems, 98.0:49.0–58.0, 2017. doi: 10.1016/j.dss.2017.04.007.
Sandro Radovanovi´c, Andrija Petrovi ´c, Boris Delibaši ´c, and Milija Suknovi ´c. A fair classifier chain for multi-label
bank marketing strategy classification. International Transactions in Operational Research, 30.0:1320.0–1339.0,
2023. doi: 10.1111/itor.13059.
Roya Rahimi, Mike Thelwall, Fevzi Okumus, and Anil Bilgihan. Know your guests’ preferences before they arrive at
your hotel: evidence from tripadvisor. Consumer Behavior in Tourism and Hospitality, 17.0:89.0–106.0, 2022. doi:
10.1108/CBTH-06-2021-0148.
Martin Reisenbichler, Thomas Reutterer, David A. Schweidel, and Daniel Dan. Frontiers: Supporting content market-
ing with natural language generation. Marketing Science, 41.0:441.0–452.0, 2022. doi: 10.1287/mksc.2022.1354.
Chong Eun Rhee and Junho Choi. Effects of personalization and social role in voice shopping: An experimental study
on product recommendation by a conversational voice agent. Computers in Human Behavior , 109.0, 2020. doi:
10.1016/j.chb.2020.106359.
Saeed Rouhani and Ali Mohammadi. A novel hybrid forecasting approach for customers churn in banking industry.
Journal of Information and Knowledge Management, 22.0, 2023. doi: 10.1142/S0219649222500897.
Soman Sajid, Natalia V olkova, Joseph Ato Wilson, and Emmanuel Opoku-Asante. Using text mining and crowdsourc-
ing platforms to build employer brand in the us banking industry. Global Business and Organizational Excellence,
41.0:6.0–27.0, 2022. doi: 10.1002/joe.22153.
Eric M. Schwartz, Eric T. Bradlow, and Peter S. Fader. Customer acquisition via display advertising using multi-armed
bandit experiments. Marketing Science, 36.0:500.0–522.0, 2017. doi: 10.1287/mksc.2016.1023.
Qusai Shambour. A deep learning based algorithm for multi-criteria recommender systems. Knowledge-Based Sys-
tems, 211.0, 2021. doi: 10.1016/j.knosys.2020.106545.
Venkatesh Shankar and Sohil Parsana. An overview and empirical comparison of natural language processing (nlp)
models and an introduction to and empirical application of autoencoder models in marketing. Journal of the
Academy of Marketing Science, 50.0:1324.0–1350.0, 2022. doi: 10.1007/s11747-022-00840-3.
F. Shirazi and Mahbobeh Mohammadi. A big data analytics model for customer churn prediction in the retiree segment.
International Journal of Information Management, 48.0:238.0–253.0, 2019. doi: 10.1016/j.ijinfomgt.2018.10.005.
Michael Shumanov, Holly Cooper, and Mike Ewing. Using ai predicted personality to enhance advertising effective-
ness. European Journal of Marketing, 56.0:1590.0–1609.0, 2022. doi: 10.1108/EJM-12-2019-0941.
Justina Sidlauskiene, Yannick Joye, and Vilte Auruskeviciene. Ai-based chatbots in conversational commerce and
their effects on product and price perceptions. Electronic Markets, 33.0, 2023. doi: 10.1007/s12525-023-00633-8.
Murat Simsek and Iclal Cetin Tas. A classification application for using learning methods in bank costumer’s portfolio
churn. Journal of Forecasting, 2023. doi: 10.1002/for.3038.
Frederik Situmeang, Nelleke de Boer, and Austin Zhang. Looking beyond the stars: A description of text mining
technique to extract latent dimensions from online product reviews. International Journal of Market Research ,
62.0:195.0–215.0, 2020. doi: 10.1177/1470785319863619.
A. Solairaj, G. Sugitha, and G. Kavitha. Enhanced elman spike neural network based sentiment analysis of online
product recommendation. Applied Soft Computing, 132.0, 2023. doi: 10.1016/j.asoc.2022.109789.
Bing Sun, Hongying Mao, and Chengshun Yin. How to identify product defects and segment consumer groups on an
online auto forum. International Journal of Consumer Studies, 46.0:2270.0–2287.0, 2022. doi: 10.1111/ijcs.12784.
Vanitha Swaminathan, H. Andrew Schwartz, Rowan Menezes, and Shawndra Hill. The language of brands in so-
cial media: Using topic modeling on social media conversations to drive brand strategy. Journal of Interactive
Marketing, 57.0:255.0–277.0, 2022. doi: 10.1177/10949968221088275.
Wondwesen Tafesse and Bronwyn Wood. Hey chatgpt: an examination of chatgpt prompts in marketing. Journal of
Marketing Analytics, 2024. doi: 10.1057/s41270-023-00284-w.
Artem Timoshenko and John R. Hauser. Identifying customer needs from user-generated content. Marketing Science,
38.0:1.0–20.0, 2019. doi: 10.1287/mksc.2018.1123.
Stéphane Cédric Koumétio Tékouabou, ¸ Stefan Cristian Gherghina, Hamza Toulni, Pedro Neves Mata, Mário Nuno
Mata, and José Moleiro Martins. A machine learning framework towards bank telemarketing prediction. Journal of
Risk and Financial Management, 15.0, 2022. doi: 10.3390/jrfm15060269.
31

Leveraging AI and NLP for Bank Marketing
Chandrasekhar Valluri, Sudhakar Raju, and Vivek H. Patil. Customer determinants of used auto loan churn: comparing
predictive performance using machine learning techniques. Journal of Marketing Analytics , 10.0:279.0–296.0,
2022. doi: 10.1057/s41270-021-00135-6.
Aikaterini Vassilikopoulou, Irene Kamenidou, and Constantinos-Vasilios Priporas. Negative airbnb reviews: an aspect-
based sentiment analysis approach. EuroMed Journal of Business, 2022. doi: 10.1108/EMJB-03-2022-0052.
Francisco Villarroel Ordenes and Rosaria Silipo. Machine learning for marketing on the knime hub: The development
of a live repository for marketing applications. Journal of Business Research , 137.0:393.0–410.0, 2021. doi:
10.1016/j.jbusres.2021.08.036.
Nhi N.Y . V o, Shaowu Liu, Xitong Li, and Guandong Xu. Leveraging unstructured call log data for customer churn
prediction. Knowledge-Based Systems, 212.0, 2021. doi: 10.1016/j.knosys.2020.106586.
D. Vélez, A. Ayuso, C. Perales-González, and J. Tinguaro Rodríguez. Churn and net promoter score forecasting for
business decision-making through a new stepwise regression methodology.Knowledge-Based Systems, 196.0, 2020.
doi: 10.1016/j.knosys.2020.105762.
Michel Wedel and P. K. Kannan. Marketing analytics for data-rich environments.https://doi.org/10.1509/jm.15.0413,
80:97–121, 11 2016. ISSN 15477185. doi: 10.1509/JM.15.0413. URL https://journals.sagepub.com/doi/
10.1509/jm.15.0413.
Jia-Jhou Wu and Sue-Ting Chang. Exploring customer sentiment regarding online retail services: A topic-based
approach. Journal of Retailing and Consumer Services, 55.0, 2020. doi: 10.1016/j.jretconser.2020.102145.
Linwan Wu, Naa Amponsah Dodoo, Taylor Jing Wen, and Li Ke. Understanding twitter conversations about artificial
intelligence in advertising based on natural language processing. International Journal of Advertising, 41.0:685.0–
702.0, 2022. doi: 10.1080/02650487.2021.1920218.
Zheng Xiang, Zvi Schwartz, John H. Gerdes, and Muzaffer Uysal. What can big data and text analytics tell us about
hotel guest experience and satisfaction? International Journal of Hospitality Management, 44.0:120.0–130.0, 2015.
doi: 10.1016/j.ijhm.2014.10.013.
Chin-Sheng Yang, Cheng-Hsiung Chen, and Pei-Chann Chang. Harnessing consumer reviews for marketing intel-
ligence: a domain-adapted sentiment classification approach. Information Systems and e-Business Management ,
13.0:403.0–419.0, 2015. doi: 10.1007/s10257-014-0266-z.
Gül Yazıcı and Tu ˘gçe Ozansoy Çadırcı. Creating meaningful insights from customer reviews: a methodological
comparison of topic modeling algorithms and their use in marketing research. Journal of Marketing Analytics ,
2023. doi: 10.1057/s41270-023-00256-0.
Mengfan Zhai, Xinyue Wang, and Xijie Zhao. The importance of online customer reviews characteristics on re-
manufactured product sales: Evidence from the mobile phone market on amazon.com. Journal of Retailing and
Consumer Services, 77.0, 2024. doi: 10.1016/j.jretconser.2023.103677.
Hui Zhang, Huguang Rao, and Junzheng Feng. Product innovation based on online review data mining: a case study
of huawei phones. Electronic Commerce Research, 18.0:3.0–22.0, 2018. doi: 10.1007/s10660-017-9279-2.
Min Zhang, Lin Sun, G. Alan Wang, Yuzhuo Li, and Shuguang He. Using neutral sentiment reviews to improve
customer requirement identification and product design strategies. International Journal of Production Economics,
254.0, 2022. doi: 10.1016/j.ijpe.2022.108641.
You Zhang, Jin Wang, and Xuejie Zhang. Personalized sentiment classification of customer reviews via an interactive
attributes attention model. Knowledge-Based Systems, 226.0, 2021. doi: 10.1016/j.knosys.2021.107135.
Piotr Łady˙zy´nski, Kamil ˙Zbikowski, and Piotr Gawrysiak. Direct marketing campaigns in retail banking with the use
of deep learning and random forests. Expert Systems with Applications , 134.0:28.0–35.0, 2019. doi: 10.1016/j.
eswa.2019.05.020.
32
