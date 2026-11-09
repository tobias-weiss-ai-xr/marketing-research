---
title: 'Machine learning applications in digital advertising performance optimization: A systematic literature
  review'
url: https://doi.org/10.5267/j.ijdns.2025.9.020
category: privacy-data
subcategory: review
date: 2025-11
venue: International Journal of Data and Network Science
authors:
- Jesus Alfredo Apaza-Caceres
- Liz Alessandra Vilca Paja
- Andre Pillihuaman Huachaca
source: openalex-oa
pdf_url: https://doi.org/10.5267/j.ijdns.2025.9.020
pages: 18
chars: 85409
fetched_at: '2026-11-08T17:07:48+00:00'
kb_version: 1
---

# Machine learning applications in digital advertising performance optimization: A systematic literature review

* Corresponding author
E-mail address: jesus.apaza@autonoma.pe (J. A. Apaza-Caceres)

ISSN 2561-8156 (Online) - ISSN 2561-8148 (Print)
© 2026 by the authors; licensee Growing Science, Canada.
doi: 10.5267/j.ijdns.2025.9.020

International Journal of Data and Network Science 10 (2026) 273–290

Contents lists available at GrowingScience

International Journal of Data and Network Science

homepage: www.GrowingScience.com/ijds

Machine learning applications in digital advertising performance optimization: A systematic literature review

Jesus Alfredo Apaza-Caceresa*, Liz Alessandra Vilca Pajaa, Andre Pillihuaman Huachacaa and Diego Alonso
Pedraza Choquea

aUniversidad Autónoma del Perú, Peru
    C H R O N I C L E                          A B S T R A C T
Received May 10, 2025
Received in revised format June
26, 2025
Accepted September 26 2025
Available online
September 26 2025
 The explosion of growth in digital advertising, reaching $798.7 billion by 2025 with 72% of
companies adopting artificial intelligence, warrants a systematic understanding of how machine
learning is transforming this sector. The objective was to systematically analyze the application of
machine learning in web advertising campaigns through a comprehensive review of scientific
literature (2010-2025). The PRISMA methodology was implemented with five-dimensional quality
criteria (0-3 points), selecting 42 excellent articles (13 -15 points). The results reveal a dominance
of deep learning (66.6%), with Deep Neural Networks (35.7%) and attention models (19.0%)
predominating; convergence toward CTR as a universal metric (95.2%); concentration in e -
commerce (61.9%), led by Alibaba (14.3%); and data sparsity as a fundamental limitation (59.5%).
Significant algorithmic consolidation is found, but critical gaps in fairness (0%), sustainability
(0%), and robustness (0%). Implications include the need for methodological diversification, the
development of equity-aware frameworks, and expansion into sectors regulated by privacy -
preserving techniques.

by the authors; licensee Growing Science, Canada. 6© 202
Keywords:
Machine learning
Digital advertising
e-commerce

1. Introduction

Over the past decade, digital advertising has experienced unprecedented growth, cementing itself as the dominant advertising
medium globally. Global digital ad spends reached $798.7 billion in 2025, with growth projected to reach $965.6 billion by
2028, accounting for 73% of total global advertising revenue (Statista, 2024) . This exponential growth has led businesses to
seek more effective ways to maximize the return on their advertising campaign investments, with 72% of global companies
having adopted artificial intelligence technologies in some aspect of their business operations (McKinsey & Company, 2024).
Machine learning (ML) remains a powerful tool for analyzing large amounts of data, personalizing content, predicting
consumer behavior, and optimizing strategic decisions in real time (Chaffey Dave & Ellis -Chadwick y Fiona, 2022; Guo et
al., 2019; Lian et al., 2018) . The myriads of AI- powered audiences  targeting techniques have shown a 30% increase in
advertising performance and a 25% decrease in costs (Ten26Media, 2025), proving the transformative impact these
technologies have on advertising efficiency.
One of the biggest challenges facing today's marketers is properly evaluating the performance of their advertising campaigns,
particularly about critical metrics such as Return on Ad Spend (ROAS), Cost per Acquisition (CPA), Click- through Rate
(CTR), and Conversion Rate (Kumar & Reinartz, 2016) . By 2024, 83% of sales teams that used AI experienced revenue
growth, compared to 66% of those that did not. Faced with this growing need in digital marketing, machine (Salesforce.,
2024)learning algorithms offer significant advantages, enabling the creation of predictive models capable of identifying highly
sophisticated consumer behavior patterns, accurately segmenting audiences, and automating campaign budgets (Lian et al.,
2018).

 274
The programmatic advertising market is undergoing a significant transformation, projected to expand from $23.50 billion in
2024 to $235.71 billion by 2033, at a compound annual growth rate (CAGR) of 29.20% (ResearchAndMarkets, 2025) . This
growth is being driven by advances in artificial intelligence and machine learning, which are enabling advertisers to optimize
ad placement in real-time, improving targeting accuracy and campaign results.
Several studies have investigated the application of advanced algorithmic models such as Random Forest, Gradient Boosting,
Deep Neural Networks, and attention architectures to predict the performance of digital ads on dominant platforms such as
Google Ads and Meta Ads (Facebook/Instagram), as well as in e- commerce marketplaces (Cheng et al., 2016; Guo et al.,
2019). A recent study by Total Economic Forrester's TEI (Term Impact) study found that companies that implement AI -
powered marketing automation achieve a 251% ROI and $2.3 million in cost savings in the corresponding year (Gartner,
2025; Shah, 2025). However, academic research is scattered across diverse methodologies, evaluation metrics, and application
areas, making it difficult to obtain a holistic understanding of the knowledge on this subject.
Augmented analytics, powered by AI and machine learning algorithms, empowers marketers by extracting actionable insights
from vast amounts of data, enabling them to make data-driven decisions and increase ROI (Gartner, 2025).
In a context of rapid technological advances and an increasingly complex digital advertising ecosystem, a systematic literature
review is necessary and timely. The study described below covers research published since 2010 that uses machine learning
techniques to predict, measure, or improve the performance of digital advertising. The main objective of this research is to
identify the most frequently applied algorithms, the most frequently optimized performance metrics, the preferred operating
contexts, and the methodological specifics of studies conducted by researchers competent in both the field of machine learning
and in advertising-specific knowledge.
The research question is: How has machine learning been used to predict, optimize, or measure the performance of online
advertising campaigns in the scientific literature between 2010 and 2025? Therefore, the general objective has been set to
carry out a s ystematic analysis of the application of machine learning to predict, optimize, or measure the performance of
web-based advertising campaigns through a systematic review of the scientific literature published between 2010 and 2025,
with the aim of identifying methodological trends, knowledge gaps, and future lines of research.
This review seeks to contribute to the academic body in digital marketing and data science by providing a systematic
framework to guide future research and data-driven decisions in the field of advertising.
2. Theoretical Framework

2.1 Learning Applications in Digital Marketing
The development of digitalization in marketing has produced a vast amount of data on consumer behavior; this has increased
the need to use machine learning tools to interpret or even leverage this data. A revolution has taken place in the field of digital
marketing thanks to the introduction of machine learning in a long list of applications ranging from process optimization to
the creation of personalized customer experiences and real -time decision-making. All of these aspects help to enhance the
effectiveness and impact of marketing practices, some examples are (Gao et al., 2023):

Campaign Optimization:
Campaign Automation: ML-powered digital marketing platforms allow you to automate and aggregate marketing operations,
helping to make operations accurate and efficient (Berlilana, 2025; Henriques & Oliveira e Sá, 2022) . Ad Optimization: ML
is used to optimize the frequency and type of ads presented to increase open rates and click -through rates (Berlilana, 2025;
Pereira et al., 2024).
Personalization and Recommendations
Personalized product recommendations using machine learning, which is based on user actions and tastes to suggest products
(Duarte et al., 2022; Pereira et al., 2024) . Personalized pricing: ML helps establish dynamic and personalized pricing, which
increases both revenue and customer satisfaction (Murthy et al., 2023; Proserpio et al., 2020) .
Prediction and Analysis
Forecasting: ML is used to predict future trends and aid in strategic decision-making (Nirmal et al., 2022; Rathi et al., 2024).
Predictive analytics: ML allows specialists to anticipate how users will behave and adjust their strategies to more easily meet
consumer needs and preferences (Gkikas & Theodoridis, 2024; Rathi et al., 2024) .
Sentiment Analysis

Using natural language processing (NLP) techniques, artificial intelligence can be used to evaluate consumer opinions and
feelings regarding products or services, resulting in valuable information for future strategies (Loukili et al., 2023) .

J. A. Apaza-Caceres et al.  /International Journal of Data and Network Science 10 (2026)

275
Consumer Behavior Analysis

Digital marketing has evolved with the help of machine learning (ML), which creates a field where consumer actions can be
anticipated and marketers can adjust their strategies instantly (Gkikas & Theodoridis, 2024; Khan et al., 2025; Silva et al.,
2020). One of the main applications of ML is market segmentation: algorithms can identify groups of consumers who exhibit
similar traits, thus being more efficient with their message (Duarte et al., 2022; Khan et al., 2025) . Among the most common
are deep neural networks (Deep Learning), which allow the analysis of information without a (declarative) structure (images,
text) in order to personalize advertising messages; logistic regression, used to calculate the probability of  a specific action
(e.g., clicking on an advertisement); and decision trees and Random Forests , which are used to extract audiences and also
create predictions about consumer behavior. These tools have improved the presentation of online advertising, delivering more
effective and personalized ads to end consumers. They also increase the efficiency of digital marketing campaigns by
providing content more tailored to the needs of the target audience.
2.2 Advertising Performance Metrics
Evaluating the performance of digital advertising campaigns is based on several key metrics that measure the effectiveness
and efficiency of the strategies implemented. Some of the most commonly used metrics include:
Common metrics
• Cost per Thousand Impressions (CPM): This measures the cost of one thousand ad impressions. It is used to evaluate the
effectiveness of purchasing advertising space in terms of viewability (Silva et al., 2020) .
• Cost per Click (CPC): This measures the cost of each click on an ad. Used for campaigns that aim to drive traffic to a
website (Silva et al., 2020).
• Click-Through Click-through rate (CTR): This measures the proportion of users who click on an ad relative to the total
number of impressions. It is used as a key indicator of the ad's effectiveness in capturing the user's attention (Ramya et al.,
2024a; Silva et al., 2020).
• Cost per Acquisition (CPA): Measures the average cost incurred to acquire a customer through an advertising campaign.
• Return on Ad Spend (ROAS): Measures the revenue generated for each dollar invested in advertising. It's used to help
compare the effectiveness of different advertising channels (Qin, 2023; Qin & Pauwels, 2023) .
• Conversion Rate: Measures the percentage of users who complete a desired action (such as a purchase) after clicking on
an ad. It's used to measure the success of conversion-oriented campaigns (Deng et al., 2021).

Advanced Metrics and Models
• ROA Elasticity: This is a diagnostic tool that helps you choose more profitable advertising levels by showing the
relationship between advertising spending and profits.
• Deep learning models for CTR prediction: Combines deep neural networks (DNNs) with other models to improve the
accuracy of CTR predictions (Ramya et al., 2024b).
• Seasonal Autoregressive Integrated Moving Average with Exogenous Variables (SARIMAX): Considers seasonality and
past performance to provide a more accurate measure of ad effectiveness(Qin & Pauwels, 2023)
• Vector autoregressive moving average with exogenous variables (V ARMAX): Allows flexibility in the length of the
advertising measurement window, capturing the long-term effects of ads (Qin, 2023).

Practical applications
• Mobile advertising: allows you to evaluate the user's propagation capacity and helps identify influential users who can
amplify the campaign's impact (Weng & Long, 2025).
• Google Ads Campaigns: Small and medium-sized businesses (SMBs) often use metrics such as CTR, CPC, and conversion
rates to measure the success of their Google Ads campaigns. (Barbosa et al., 2021).

Understanding and utilizing various advertising performance metrics is crucial for optimizing advertising campaigns and
achieving a better return on investment (ROI). Advanced models and accurate attribution methods can provide more detailed
insights and more reliable evaluations, helping advertisers make informed decisions (Qin, 2023; Qin & Pauwels, 2023; Ramya
et al., 2024a; Shah & Technology Solutions, 2021; Silva et al., 2020).
2.3 Featured Studies in the Application of ML in Digital Advertising

Learning (ML) technology has had an impactful effect on improving the efficiency of digital advertising strategies. Several
studies have employed methods such as Ensemble Methods (e.g., Random Forest and Gradient Boosting) to analyze large
amounts of data and uncover the factors that affect the success of an advertising campaign. These models have demonstrated
remarkable predictive capabilities, achieving 92% accuracy and an F1 score of 89% (Berlilana, 2025) . Furthermore, the
implementation of distributed models has helped improve revenue prediction, enabling more effective resource utilization and

 276
better-informed strategic decisions (Murugan et al., 2023) . Regarding content personalization and segmentation, ML can be
used to create campaigns based on user characteristics and preferences through collaborative and content -based filtering
(Bhaskaraputra et al., 2022; Thirumagal et al., 2024) . Audience segmentation through behavioral and preference analysis
along with demographic data has also been widely used in sectors such as e -commerce and social media to tailor advertising
messages and maximize their effectiveness (Thirumagal et al., 2024).
Finally, prediction and performance analysis have been improved using machine learning techniques. Models based on
algorithms such as Naive Bayes and decision trees have been used to calculate click -through rates (CTR) and conversion
rates, providing important information for improving campaigns (Verma et al., 2024). Furthermore, the challenge of ad click
fraud has begun to be addressed through machine learning, offering solutions that will ensure integrity and continuity in digital
advertising (Choi & Lim, 2020).
3. Methodology

Planning the review
The review planning process involves identifying and defining various aspects to lay the groundwork for its execution, such
as formulating the questions to be answered, detailing the protocol followed,  and any other information relevant to the
review's traceability. These aspects are described in this section.
a. Research Questions
First, a series of research questions have been posed.
• RQ1. What types of machine learning algorithms have been applied in digital advertising?
• RQ2. Which performance metrics are most frequently optimized?
• RQ3. In which sectors, contexts, or digital platforms is the application of machine learning in advertising concentrated?
• RQ4. What are the main knowledge gaps, methodological limitations, or technical challenges identified in the reviewed
literature?
Given the previous research questions, the PICOC method was followed to define the scope of the review.
• Population (P): Academic publications and empirical studies that address digital advertising practices from the perspective
of advertising performance and/or effectiveness.
• Intervention (I): Application of Machine Learning (ML) techniques, including supervised, unsupervised, and reinforcement
learning algorithms, to optimize key metrics such as ROI, CTR, CPA, conversion rate, among others.
• Comparison (C): Although a formal comparison is not required, studies that contrast traditional approaches with ML -based
approaches, or that compare different algorithms or metrics with each other, will be considered.
• Results (O): Results related to improving advertising performance: campaign personalization, automated segmentation,
efficient budget allocation, and consumer behavior prediction.
• Context (C): Digital advertising environments (social networks, search engines, content platforms, e - commerce,
programmatic) advertising) in the period 2010–2025, without geographical restriction.
b. Inclusion and Exclusion Criteria
Once the scope of the review has been established, a series of inclusion (IC) and exclusion (EC) criteria are defined to select
relevant papers that address the identified research questions. If a paper does not meet all the inclusion criteria or meets any
of the exclusion criteria, it will be excluded from the review.
• IC1. Research that explicitly addresses the application of machine learning (ML) or artificial intelligence (AI) techniques in
the context of digital advertising, online marketing, or paid digital media.
• IC2. Studies that evaluate the impact of ML algorithms on advertising performance through metrics such as ROI, CTR, CPA,
conversion rate, budget efficiency, automated segmentation, etc.
• IC3. Publications between 2010 and 2025, according to the temporal scope of this review
• IC4. Peer-reviewed empirical research articles, literature reviews, case studies, and conference papers.
• IC5. Studies published in English or Spanish.
• IC6. Documents available in their entirety for reading and analysis.
Exclusion criteria are derived from inclusion criteria as their opposite.

J. A. Apaza-Caceres et al.  /International Journal of Data and Network Science 10 (2026)

277
• EC1. Research focused exclusively on other fields such as health, finance, or education, unrelated to digital advertising
strategies.
• EC2. Works that deal with digital marketing but without the incorporation or analysis of machine learning or AI algorithms.
• EC3. Studies that are limited to theoretical aspects without evaluating performance or impact metrics in advertising
campaigns.
• EC4. Undergraduate theses, blog posts, extended abstracts, opinion pieces, or presentations without peer review.
• EC5. Studies published more than once under slightly different titles or versions.
• EC6. Publications in languages other than English or Spanish, with no translation available.
c. Search Strategy
It is necessary to identify the most important databases in the research context where the queries will be conducted to obtai n
relevant search results. In this case, three electronic databases were selected: Scopus, Web of Science (WoS) and IEEE Xplore.
These databases were selected based on the following criteria:
• It is a reference database in the field of research.
• It is a relevant database in the research context of this bibliographic review
• Allows you to use search strings like  those in the other selected databases, as well as using Boolean operators to improve
the results of the retrieval process.
d. Query Strings
Specific query strings were specified for each chosen database using its query syntax.
1) SCOPUS

(“machine learning” OR “deep learning” OR “artificial intelligence”)
AND (“digital advertising” OR “online advertising” OR “programmatic advertising” OR “digital marketing”)
AND (“performance” OR “optimization” OR “ROI” OR “return on investment ” OR “conversion rate” OR “click-through
rate” OR “CPA”)
AND (LIMIT-TO (PUBYEAR, 2010–2025))
2) WEB OF SCIENCE

(“machine learning” OR “deep learning” OR “artificial intelligence”)
AND (“digital advertising” OR “online advertising” OR “programmatic advertising” OR “digital marketing”)
AND (“performance” OR “optimization” OR “ROI” OR “return on investment ” OR “conversion rate” OR “click-through
rate” OR “CPA”)
AND (LIMIT-TO (PUBYEAR, 2010–2025))
3) IEEE XPLORE

(“machine learning” OR “deep learning” OR “artificial intelligence”)
AND (“digital advertising” OR “online advertising” OR “programmatic advertising”)
AND (“performance optimization” OR “return on investment” OR “click-through rate” OR “conversion rate”)
e. Quality criteria
To ensure the inclusion of studies of high methodological quality, a quantitative evaluation system was implemented based
on five fundamental criteria, each evaluated on a scale of 0 to 3 points (maximum score: 15 points).
Evaluation Criteria
1. Methodological Quality (0 -3 points): Clear and well- defined objective, comprehensively described methodology and
comparison with baseline or state-of-the-art methods

 278
2. Data Quality (0-3 points): Detailed description of the dataset and problem, relevant variables and metrics documented.
3. Quality of Analysis (0-3 points): Use of multiple evaluation metrics, evidenced model validation procedures, and detailed
justification of algorithms used.
4. Quality of Results (0 -3 points): Clear and systematic presentation of results, contextualized interpretation of findings and
explicit identification of limitations.
5. Practical Relevance (0-3 points): Applicability to real industrial contexts, use of metrics oriented to commercial results and
demonstrable commercial impact
Of the studies evaluated, 42 articles (43.3%) reached the Excellent category with scores between 13 and 15 points, 55 articles
(56.7%) were classified in the good category with scores between 10 and 12 points, no study was classified in the Fair (7- 9
points) or Poor (<7 points) categories, indicating that all articles included in the review met minimum standards of scientif ic
quality. This quality distribution provided a solid basis for the selection of the 42 excellent articles as the main corpus for the
subsequent analyses of the systematic review.
The data collection process for conducting the systematic review was divided into different phases, during which various
activities were carried out. The PRISMA flowchart was used to detail the actions performed during data extraction (Fig. 1).

Fig. 1. PRISMA diagram of the research selection procedure
4. Results
Types of machine learning algorithms that have been applied in digital advertising
The analysis of the 42 high -quality articles reveals a clear dominance of deep learning approaches in the application of
machine learning to digital advertising. Deep neural networks represent the most prevalent category with 15 studies (35.7%),
followed by attention-based models with 8 studies (19.0%), and recurrent neural networks with 5 studies (11.9%). Together,
these three deep learning categories comprise 66.6% of the total literature analyzed, demonstrating an academic consensus on
the superiority of these techniques for the challenges inherent to digital advertising.
The temporal evolution of algorithmic techniques shows a clear transition from classical methods to more sophisticated
approaches. Support vector methods (4.8%) and traditional factorization methods (7.1%) represent the historical foundations
of the field, established mainly between 2013 and 2016. The era of specialization (2017 and 2019) was characterized by the
explosion of specialized neural network architectures, particularly the development of hybrid models such as DeepFM that
combine the memorization of linear methods with the generalization capabilities of deep learning (9.5% of studies).
Hybrid deep learning methods (9.5%) have emerged as a notable strategy, illustrated by methods such as Wide & Deep
Learning, DeepFM, and xDeepFM, which address the individual weaknesses of each algorithmic paradigm. At the same time,
ensemble methods (7.1%) have also demonstrated value in reducing overfitting and improving predictive robustness, which
is especially important in advertising environments where data is highly variable. Probabilistic models account for only 2.4%
of the work, yet are a possibili ty worth considering, as they are gaining increasing prominence in quantifying uncertainty in
advertising decision- making. This lack of representativeness presents a significant opportunity for the development of
Bayesian methods—for example, to provide confidence intervals for CTR predictions and for bid optimization.

J. A. Apaza-Caceres et al.  /International Journal of Data and Network Science 10 (2026)

279
Reinforcement learning appears in only 2.4% of the literature, which in practice represents a considerable methodological gap
given its natural application in dynamic optimization problems, such as programmatic bidding or ad selection. This limited
use could be due to its complicated implementation or the simulation conditions required for training.
Graph neural networks (4.8%) are an area with significant potential, but very low adoption. These models are very good at
capturing complex relationships between users, ads, and contexts, and are therefore especially useful in recommendation
problems in advertising or knowledge modeling. The limited representation suggests that the field has not yet been able to
fully exploit the possibilities offered by relational data in digital advertising.
The concentration of 66.6% of studies on deep learning techniques reveals a possible methodological saturation. The literature
shows a trend toward technical sophistication ( federated learning , distributed systems ) rather than paradigmatic
diversification. This suggests the need to explore alternative methodological approaches that can address domain- specific
challenges, such as cold start problem, model interpretability, and continuous adaptation to changes in user behavior.
The dominance of deep learning techniques is relevant to industrial practice. While these methods appear to be the most
predictive, they are also the most problematic in terms of interpretability, computational resource consumption, and the
number of data points required. The significant presence of hybrid models (9.5%) suggests that the industry has found a
common ground that pragmatically balances performance and operational efficiency, combining the simplicity of linear
methods with the expressiveness of deep learning (See Table 1).
Table 1
Machine Learning Algorithms Applied in Digital Advertising
Algorithmic Category Specific Techniques Characteristics Main Contributions n %
Deep Neural Networks ESMM, Deep & Cross
Network, Product-based NN,
Deep Crossing, FNN, ONN,
Neural Feature Selection,
Deep CNN, Task-oriented
NN, Distributed DNN,
YouTube DNN, Monotonic
NN, Vertical Federated NN,
Convolutional Generative,
Feature Generation CNN
Multi-task, Feature Crossing,
Web- scale, Local
Neighborhood, AutoML, IoT
Data, End-to-End,
Distributed, Large-scale,
Real-time, Federated,
Generative
Solution to selection bias CVR, Automatic interaction
modeling, Embedding operations, Featureless
modeling Engineering, Automatic feature selection,
Big data processing, GPU distributed systems,
Scalable recommendations, DSP auction optimization,
Vertical federated learning
15 35.70%
Attention-based
Models
Hierarchical Bayesian + Self-
Attention, RAS-DTAAN,
DIN, AutoInt, FiBiNET,
Hierarchical Attention, BST,
Neural Attentional Rating,
AFM
Uncertainty + Attention,
Real-time, Interest Modeling,
Automatic, Feature
Importance, Interpretable,
Sequential, Review-based,
Attention Weight
Uncertainty quantification, Adversarial sampling +
temporal attention, Dynamic interest modeling,
Machine learning interactions, Importance + bilinear
interaction, Interpretable CTR, Behavior sequence
modeling, Explanatory regression, FM attention
weights
8 19.00%
Recurrent Neural
Networks
LSTM, GRU, Gaussian
Functions, DSIN, SLI-REC,
Latent Cross, Bi-LSTM +
Parrot Optimizer
Multi-method, Session-
based, Long Sequential,
Context-aware, Temporal
E-commerce campaign optimization, session-based
interest modeling, long-term sequential behavior,
contextual recommendations, temporal interest
modeling
5 11.90%
Hybrid Deep Learning FM + Neural Networks,
DeepFM, Wide & Deep
Learning, xDeepFM
Hybrid, Standard, Linear +
DNN, Enhanced
Optimal combination FM-NN, Classical reference FM
+ DNN, Memorization + generalization, Explicit +
implicit interactions
4 9.50%
Ensemble Methods ML-CBIAM + TOPSIS,
Random Forest + Gradient
Boosting, Random Forest +
XGBoost + SVM, XGBoost
Multi-method, Ensemble,
Multi-method, Standard
Purchase intent analysis, Digital marketing strategies,
Comparative CTR prediction, Scalable boosting
system
3 7.10%
Factorization Methods Field- aware FM, Field-
weighted FM, Neural FM
Field- aware, Display Ads,
Sparse Analytics
FM conscious fields, FM weighted display, FM neural
sparse data
3 7.10%
Graph Neural
Networks
Knowledge Graph CNN,
Neural Graph Collaborative
Filtering
Knowledge Graph, Graph-
based
CNN on knowledge graphs, Collaborative graph
filtering
2 4.80%
Support Vector
Methods
FTRL, Logistic Regression +
SVM
Large-scale, Simple/ Scalable click prediction, Simple and scalable prediction 2 4.80%
Probabilistic Models Bayesian Networks + MDN Uncertainty Bayesian approach to uncertainty quantification 1 2.40%
Reinforcement
Learning
Multi- Armed Bandit +
Thompson Sampling
Real-time Framework bandits two stages 1 2.40%
TOTAL - - - 42 100%

Performance metrics that are most frequently optimized
Analysis of the performance metrics used in the 42 high- quality studies reveals a notable convergence toward a consolidated
set of assessment indicators. Click -Through CTR (Cell Rate) emerges as the virtually universal metric, present in 95.2% of
the studies analyzed, with reported values ranging from 3.3% to 19.4%. This near -absolute prevalence of CTR underscores
its role as a fundamental indicator for evaluating user engagement and advertising effectiveness, providing a comparable
baseline across different platforms, algorithms, and application contexts.
The Conversion Rate (CVR), although present in a smaller percentage of studies (19.0%), represents a metric of high
commercial value that captures effectiveness beyond simple initial engagement.
We clearly observe the consolidation of two metrics such as: the AUC ( Area Under Curve) and Logloss . The AUC (83.3%)
was prominent in our literature review and has established itself as the standard for evaluating binary classification models

 280
for two key reasons: it is independent of the decision boundary and it allows direct comparisons between the different
algorithms tested. Logloss (78.6%) also features prominently in model evaluation because it provides an accurate assessment
of the probabilistic calibration of models, which is particularly critical in advertising systems, where predicted probabilities
are the basis for bid optimization (real-time bidding).
Table 2
Machine Learning-Optimized Performance Metrics for Digital Advertising
Metric Category Specific Metrics Reported Values Main Applications Characteristics n %
Engagement Metrics
CTR (Click-Through)
Rate) 3.3% - 19.4% Click prediction, campaign optimization, creative evaluation Universal metric, easy to interpret, comparable across platforms 40 95.20%
Conversion Rate (CVR) 3.3% - Post-click CVR E-commerce, funnel optimization, effectiveness measurement Action metric, high commercial value, problem selection bias 8 19.00%
Impressions Volume metrics Reach measurement, media planning, awareness campaigns Exposure metric, basis for CTR calculation 6 14.30%
Clicks (absolute) Volume-based Evaluation of interaction volume, traffic generation Raw engagement metric, traffic dependent 5 11.90%
Technical ML
Metrics
AUC (Area Under Curve) Standard benchmarking Evaluation of binary models, algorithm comparison, technical validation Threshold-independent, technical standard, interpretable 35 83.30%
Logloss (Cross- entropy) Probabilistic calibration Evaluating probabilities, calibrating models, programmatic systems Penalizes erroneous predictions, critical calibration 32 76.20%
Accuracy 28.6% - 98% Balanced problems, general evaluation, simple baselines Simple metric, problematic with class imbalance 12 28.60%
F1-Score 89% (Berlilana et al.) Unbalanced problems, robust evaluation, precision- recall balances Harmonic mean, robust to imbalance, complete evaluation 8 19.00%
Precision / Recall Various Cases with differentiated costs, specific optimization, detailed analysis Complementary metrics, false positives/negatives control 7 16.70%
RMSE/MSE R² up to 98% Problems of regression, continuous optimization, probabilistic models Regression metrics, sensitive to outliers 3 7.10%
Business Metrics
Revenue Primary business objective Final objective of all studies, ROI calculation, business impact Latest success metric, variable by industry 38 90.50%
ROAS (Return on Ad
Spend) 19.4% (Shi et al.) Budget optimization, campaign efficiency, modern advertising trending metrics upward 5 11.90%
ROI (Return on
Investment) Up to 19.4% General investment evaluation, business cases, strategic decisions Classic business metrics, broader than ROAS 3 7.10%
CPC (Cost Per Click) Variable by platform Cost control, bid optimization, budget management Direct cost metric, auction- dependent 3 7.10%
Cost Efficiency Various optimization Budget optimization, resources allocation, performance marketing Operational metrics, platform-specific 4 9.50%
Specialized Metrics
ACOS (Amazon) Amazon -specific E- commerce optimization, marketplace advertising, platform-specific Specific to the Amazon ecosystem 2 4.80%
Bid Performance Auction optimization Real-time bidding, DSP optimization, programmatic advertising Real-time metrics, auction- specific 2 4.80%
Creative Performance Creative optimization Ad creative testing, A/B testing, content optimization Qualitative assessment, creative- specific 2 4.80%
User Interaction Engagement depth User behavior analysis, recommendation systems, engagement quality Beyond clicks, behavioral depth 2 4.80%
Temporal Prediction Time- aware metrics Session-based optimization, temporal modeling, dynamic systems Time- dependent, sequential optimization 2 4.80%
NLL/KLD (Uncertainty) Bayesian evaluation Uncertainty quantification, probabilistic models, risk assessment Advanced probabilistic, uncertainty-aware 2 4.80%

The observed transition from Accuracy (28.6%) to F1-Score (19.0%) reflects a methodological maturation of the field, which
recognizes the limitations of Accuracy as an evaluation metric in contexts of imbalanced data, characteristic of click prediction
problems where conversion rates are typically low. This evolution suggests greater sophistication in understanding the specific
challenges of the advertising domain.
The economic result remains the priority commercial objective in 90.5% of the research projects. The Return on Ad Spend
(ROAS), present in only 11.9% of research papers and showing a moderate increase in recent publications (2024 -2025) with
a value reaching 19.4%, represents a logical evolution of ROI toward more concrete indicators of the advertising ecosystem,
given that it provides a direct measure of the effectiveness of advertising value. The progressive introduction of ROAS
demonstrates the maturation of the advertising field toward the use of concrete metrics for real-time campaign optimization.

J. A. Apaza-Caceres et al.  /International Journal of Data and Network Science 10 (2026)

281
Cost per click (CPC) , present in 7.1% of studies, remains a valid metric for direct cost control, especially in programmatic
auction environments where budget control is essential to ensure the commercial viability of the campaigns involved.
The evaluation of empirical material reveals the emergence of specialized metrics that reflect the growing diversification and
complexity of the field; uncertainty metrics such as Negative Log Likelihood (NLL) and Kullback-Leibler. Divergence (KLD),
although present in only 4.8% of studies, represents a significant methodological limitation for the development of risk-aware
advertising systems capable of measuring confidence in their forecasts.
The temporal and bid performance metrics, which appear in 4.8% of studies, demonstrate a shift toward analyzing more
sophisticated aspects of advertising ecology, such as real -time optimization or modeling temporal patterns of user behavior.
In short, specialized metrics seem to reflect the field's approach to addressing more complex challenges beyond simple CTR
forecasting.
Platform metrics such as ACOS (Amazon Cost of Sales) denote the need to adapt to particular ecosystems, where the specific
characteristics of the platforms require specialized indicators. The analysis reveals significant gaps in the evaluation of aspects
relevant to the responsible development of machine learning in advertising. The complete lack of fairness metrics in the
literature analyzed is a significant limitation, especially in situations where advertising algorithms perpetuate or amplify social
or demographic biases.  The lack of long- term impact metrics demonstrates a focus consistently on short -term optimization,
which can neglect the effects of ad fatigue and the long- term impact o n user experience. Similarly, the absence of
environmental sustainability metrics reflects a gap in considering the energy and environmental impact of large-scale machine
learning systems.  On the other hand, the observed convergence around standard metrics (CTR, AUC, Logloss , Revenue)
facilitates comparability between studies and reproducibility of results, key aspects for scientific advancement in the field .
However, this same standardization entails the danger of over-optimization toward specific metrics, possibly neglecting more
important, though less measured, aspects of system performance.
The emergence of specific metrics such as ROAS and uncertainty metrics demonstrates a shift toward more modulated, more
situated assessments. This trend also highlights the need to create more comprehensive evaluation frameworks that balance
technical, commercial, and ethical metrics (See Table 2).
Sectors, contexts or digital platforms where the application of machine learning in advertising is concentrated
The analysis of the sector distribution reveals a significant concentration in the e -commerce ecosystem, which represents
61.9% of all studies analyzed when combining general e-commerce applications (42.9%) with specific e-commerce platforms
(19.0%). This dominance reflects inherent characteristics of the sector that make it particularly suitable for the application of
machine learning techniques : the availability of comprehensive transactional data, the high density of value per transaction
that justifies investments in algorithmic optimization, and the wealth of user behavioral data that facilitates large -scale
personalization. Within the e -commerce ecosystem, a clear geographic and platform bifurcation is observed. The Alibaba/
Taobao ecosystem dominates with six studies (14.3%), reflecting the hegemonic position of these platforms in the Chinese
market and the unique integration of social commerce, digital payments, and logistics services that characterizes the " super -
app " model. In contrast, Amazon represents 4.8% of the studies, highlighting the more fragmented approach of the Western
ecosystem, where different aspects of e-commerce are handled by specialized platforms (See Table 3).
Table 3
Machine Learning Sectors for Digital Advertising
Category Specific Platforms/Sectors Application Contexts Main Features Use Cases n %
E- commerce
Platforms
Amazon (2 studies), Alibaba/
Taobao (6 studies)
Sponsored Products,
Sponsored Brands,
Marketplace advertising,
Product recommendations
High- value
transactions, complete
funnel tracking, rich
user data, conversion
optimization
CTR prediction, CVR
optimization, product
recommendation, bid
optimization, ACOS
management
8 19.00%
Social Media
Platforms
Meta/Facebook (1 study), YouTube
(2 studies), Reddit (1 study),
WeChat/Weibo/ Douyin (1 study)
Social advertising, video
advertising, feed
optimization, creative
performance
User engagement focus,
viral potential, social
signals, content-driven
Creative optimization,
feed ranking, video
recommendations, social
targeting
5 11.90%
Search & Display
Advertising
Google (3 studies), General display
networks
Search advertising, display
advertising, programmatic
buying, contextual targeting
Intent-based, keyword-
driven, contextual
relevance, auction
mechanisms
Search ads, display
banners, contextual
targeting, bid management
8 19.00%
General E-commerce Generic e- commerce applications (18 studies)
Online retail, digital
commerce, conversion
optimization, customer
journey
Transaction-focused,
customer lifetime
value, retention,
personalization
Product recommendations,
customer segmentation,
price optimization,
inventory management
18 42.90%
Entertainment &
Media
Netflix, Spotify, General streaming
(3 studios)
Content recommendation,
subscription optimization,
engagement maximization
Content consumption,
user preferences,
engagement metrics,
retention
Content recommendations,
playlist generation,
subscription management,
engagement optimization
3 7.10%
Mobile Applications App stores, mobile advertising (1 study) App recommendations, mobile advertising, in-app purchases Mobile- specific, app ecosystem, user behavior patterns App recommendations, mobile ad optimization, in-app engagement 1 2.40%

 282
Analysis of technical contexts indicates that CTR prediction accounts for 35.7% of applications and is emerging as a common
issue across multiple advertising contexts.
Recommendation systems account for 19.0% of applications, being the primary focus of e -commerce and entertainment
platforms. This fact highlights that advertising and content recommendation are converging, and that the lines between
marketing and user experience blur, especially in contexts where product recommendations are presented simultaneously as
a useful feature for the user and as a monetization channel for the platform.
Real-time bidding (RTB) is a specific technical context that presents specific challenges such as latency (response
requirements in milliseconds), lack of knowledge about auction dynamics, and budget overruns. The relatively limited
representation of RTB in the literature may reflect the technical and data access barriers that characterize this highly targeted
advertising ecosystem (See Table 4).
Table 4
Analysis by Technical Contexts
Technical Context Description Main Platforms Technical Characteristics Specific Challenges n %
CTR Prediction Click Probability Prediction Universal application
Binary classification,
large-scale data, real-time
inference
Data sparsity, cold start,
scalability 15 35.70%
Recommendation Systems Product/content recommendation systems Alibaba, Amazon, Netflix, Spotify Collaborative filtering, content-based, hybrid approaches Cold start, diversity vs accuracy, scalability 8 19.00%
Real-time Bidding (RTB) Real-time bid optimization Google, Amazon, DSPs Millisecond latency, auction dynamics, budget constraints Latency requirements, uncertainty, competition 6 14.30%
Display Advertising Graphic advertising and banners General networks, Google Display Visual content, contextual targeting, placement optimization Ad blindness, viewability, brand safety 5 11.90%
Programmatic Advertising Automated purchase of advertising space DSPs, SSPs, Ad Exchanges Automated buying, audience targeting, optimization Transparency, fraud detection, attribution 3 7.10%
Social Media Advertising Social media advertising Facebook, Instagram, TikTok Social signals, viral mechanics, user-generated content Privacy concerns, content moderation, engagement quality 3 7.10%
Mobile Advertising Mobile-specific advertising Mobile apps, mobile web Location data, device capabilities, user context Battery consumption, data usage, user experience 2 4.80%

Google is present in three studies (7.1%), Meta/Facebook in one (2.4%), and YouTube in two (4.8%), representing the
advertising ecosystem in the West. This concentration not only reveals, on the one hand, the level of market dominance of
these platforms, but also demonstrates that these platforms have the capacity to provide access to data and research resources
that make academic studies possible. On the other hand, the representation of Chinese platforms (WeChat, Weibo, Douyin) in
one study (2.4%) represe nts the integrated ecosystem model that characterizes the Chinese digital market, where the
boundaries separating social media, e- commerce, and financial services are more blurred than in the Western market. The
analysis reveals representative gaps in sectors that, despite being commercially relevant, are located on the margins of
academic literature. Financial services, healthcare, and education are virtually absent, which can be attributed to heavy
regulation, compliance requirements, and higher privacy sensitivities in the sectors analyzed. This absence may be due to the
differences that characterize B2B decision -making processes, which include longer cycles, multiple people involved, and
more complex evaluation criteria than CTR prediction models tailored to individual consumer decisions. The study notes a
significant geographic bias toward developed markets, with 35.7% of research studies focused on the Western market and
16.7% on the Chinese market, while emerging markets only contributed 4.8% of research studies despite representing a
significant and growing share of global internet usage and digital commerce (See Table 5).
Table 5
Geographic and Market Distribution
Market/Region Dominant Platforms Market Characteristics Specific Regulations Unique Trends n %
Chinese Market
Alibaba, Taobao,
WeChat, Weibo,
Douyin
Integrated ecosystem,
super-apps, mobile-first
Local data regulations,
great firewall
Social commerce, live
streaming, integrated
payments
7 16.70%
Western Market Amazon, Google, Facebook, YouTube Separate ecosystems, privacy regulations GDPR, CCPA, privacy by design Privacy-focused, consent management, data portability 15 35.70%
Emerging Markets General applications Mobile- first, limited infrastructure Varying regulatory maturity Offline- to -online, mobile payments, local languages 2 4.80%
Global Market/Agnostic Platform-independent solutions Cross- platform compatibility Multiple regulatory compliance Standardization, interoperability, scalability 18 42.90%

This lower contribution can be attributed to data access barriers, differences in the history of research infrastructure, and  the
concentration of academic resources in research centers in developed markets. However, it also represents a significant
opportunity for future research, especially considering the characteristics of emerging markets, parallel payment systems, and
intermittent connectivity patterns.

J. A. Apaza-Caceres et al.  /International Journal of Data and Network Science 10 (2026)

283
The concentration of studies on e-commerce and specific platforms has important implications for the transferability of results.
While techniques developed for CTR prediction in e -commerce have demonstrated applicability in other contexts, platform -
specific optimizations may have limited transferability. This concentration also suggests the need to develop more diverse
benchmarks and datasets that facilitate the evaluation of techniques in broader industry contexts (See Table 6).
Table 6
Analysis by Type of Data Used
Data Type Main Sources Characteristics Processing Challenges Opportunities Prevalence
Behavioral Data Click streams, navigation patterns, interaction logs High volume, sequential, sparse Real-time processing, privacy, storage Personalization, prediction accuracy High
Transactional Data Purchase history, conversion events, revenue High value, structured, temporary Attribution modeling, lifetime value Business optimization, ROI measurement High
Contextual Data Time, location, device, content Dynamic, multi-dimensional Feature engineering, relevance Targeting precision, context awareness Average
Social Data Social graphs, sharing behavior, engagement Network effects, viral patterns Graph processing, influence modeling Viral marketing, social proof Average
Content Data Ad creatives, product descriptions, multimedia Unstructured, multimodal NLP, computer vision, feature extraction Creative optimization, content generation Low
Demographic Data Age, gender, location, interests Structured, sensitive Privacy compliance, bias mitigation Audience segmentation, targeting Low

The absence of regulated sectors such as healthcare and financial services indicates the need to develop techniques that can
operate under stricter compliance and privacy constraints, a particularly relevant area of research in the context of emergin g
regulations such as GDPR and state privacy laws in the United States.
Main knowledge gaps, methodological limitations or technical challenges
The analysis of methodological limitations reveals that data issues constitute the most prevalent and persistent category of
challenges in machine learning for digital advertising. Data sparsity emerges as the fundamental challenge, present in 59.5%
of the studies analyzed, manifesting consistently across different algorithms, platforms, and time periods. This prevalence
reflects an inherent characteristic of advertising data: the extremely sparse nature of user- item matrices, where most users do
not interact with most available content, creating a problem that significantly impairs the models' generalization capacity.
The cold starts This problem —although it only appears in 4.8% of the reviewed papers— is one of the most serious limitations
to the commercial viability of advertising systems: the inability to make predictions for new users or products implies the loss
of direct monetization opportunities. The low representation of this problem in the reviewed literature may be indicative of
the gap between the theoretical problems discussed in academic research and the types of problems faced in industrial
implementations.
Technical problems are the second most common limitations encountered (28.6%), with the scalability category standing out
above the rest. issues (representing 14.3% of all papers reviewed), justified because it reflects the tension that arises bet ween
the increase in algorithmic sophistication and the operational requirements that must be met by advertising systems that must
process billions of events daily with millisecond latencies. This increase in complexity towards deep models Learning has
increased the technical challenges, introducing a paradox that the most effective algorithms from a performance perspective
may be impractical from an operational perspective.
Computational cost (7.1% of studies) emerges as a growing constraint that transcends strictly technical considerations and
expands into the realm of environmental sustainability and economic viability. This trend clearly conflicts with the evolving
approach in the machine learning community , which calls for developing algorithms that are effective and efficient in terms
of energy and computational resources.
Model interpretability accounts for 7.1% of the studies, which is a rather low representation given the self-imposed difficulty
of the growing regulatory environment and stakeholder demands for greater algorithmic transparency.
The lack of interpretability considerations in the literature suggests a reluctance on the part of academic research to align itself
with the progress made in terms of operational and regulatory demands illustrated by industry, as these are often more focused
on the results of technical performance metrics.
The analysis reveals complete absences (0.0% of studies) in critical areas that have gained prominence in other applications
of machine learning . The complete absence of equity considerations represents an alarming methodological gap, particularly
considering the potential for advertising algorithms to perpetuate or amplify socioeconomic, racial, or gender discrimination
in access to economic opportunities and information.
The lack of environmental sustainability considerations (0.0% of studies) reflects a significant omission at a time when the
energy impact of large -scale machine learning systems is receiving increasing attention from both regulators and corporate
stakeholders committed to carbon neutrality goals.

 284
The lack of research on robustness against adversarial attacks is particularly worrying given the economic context of digital
advertising, where click fraud and bot traffic represent economic losses estimated at billions of dollars annually. This gap
suggests a disconnect between academic research and the real security threats faced by the industry.
The distribution of reported limitations suggests a potential disparity between the challenges addressed in academic research
and those faced in industrial implementations. The high prevalence of data scarcity (59.5%) and the relatively low attention
paid to issues such as implementation challenges (0.0%) or systems integration (0.0%) suggest that academic research may
be biased toward fundamental algorithmic problems while underestimating operational and integration challenges.
This disparity may reflect academic incentives that favor theoretical contributions over practical solutions, but it may also
indicate barriers to accessing information about real -world implementation challenges due to the proprietary nature of many
industrial advertising systems. Evaluation challenges and validation issues (4.8% each) represent fundamental methodological
limitations that affect the transferability of research results to practical applications. The gap between offline metrics us ed in
academic research and online performance in real-world systems represents a persistent challenge that limits the field's ability
to develop truly effective solutions.  The identified gaps suggest several critical directions for future research. Regulatory
urgency surrounding equity and explainability demands the development of equity- aware advertising frameworks that can
balance technical performance with social equity objectives. Sustainability pressures require research in green computing
specifically tailored to high-volume advertising systems.
The need for robustness against adversarial attacks represents an opportunity for the development of adversarial training
techniques specifically designed for contexts where economic incentives create strong motivations for system manipulation.
Finally, the gap in human- AI interaction suggests the need for research in advertising design that prioritizes user autonomy
and well-being over purely commercial optimization (See table 7).
Table 7
Knowledge gaps, methodological limitations or technical challenges
Category of Limitation Specific Problems Technical Manifestations Impact on the Field Proposed Solutions n %
Data Problems
Data Sparsity Sparse, missing matrices values, cold users / items Performance degradation, difficulty generalization Feature engineering, embedding techniques, transfer learning 25 59.50%
Cold Start Problem New users/products with no history Impossibility of initial prediction, loss of opportunities Content- based methods, demographic features, exploration strategies 2 4.80%
Class Imbalance Imbalance clicks vs non- clicks Bias towards majority class, inflated metrics Sampling techniques, cost - sensitive learning, focal loss 1 2.40%
Limited Dataset Size Small samples for validation Overfitting, lack of statistical robustness Data augmentation, synthetic data, transfer learning 2 4.80%
Privacy Concerns Restrictions on access to sensitive data Limitations features, compliance overhead Federated learning, differential privacy, on- device processing 1 2.40%
Model Problems
Model Interpretability Black box" models, lack of explainability Stakeholder distrust, compliance regulation SHAP, LIME, attention mechanisms, explainable AI 3 7.10%
Model Complexity Overcomplexity of architectures Overfitting, difficulty in maintenance Regularization, early stopping, model selection 1 2.40%
Overfitting Memorization vs. generalization Degraded performance on new data Cross- validation, regularization, ensemble methods 1 2.40%
Generalization Issues Lack of transferability between contexts cross-domain applicability Domain adaptation, meta- learning, robust features 0 0.00%
Algorithmic Bias Systematic biases in predictions Demographic discrimination, inequality Fairness constraints, bias detection, diverse training data 0 0.00%
Technical Challenges
Scalability Issues Large-scale processing limitations Latency, insufficient throughput Distributed computing, model compression, efficient architectures 6 14.30%
Computational Cost High consumption of computing resources Operational costs, sustainability concerns Model pruning, quantization, efficient inference 3 7.10%
Real-time Processing Ultra-low latency requirements Impossibility of real-time optimization Edge computing, model optimization, caching strategies 2 4.80%
Infrastructure Limitations Dependence on specialized hardware Barriers to adoption, vendor lock -in Cloud solutions, containerization, standardization 1 2.40%
Business Challenges
Evaluation Challenges Difficulty metrics offline vs online Gap between research and production A/B testing, online learning, multi-armed bandits 2 4.80%
Validation Issues Cross -temporal validation problems Obsolete models, concept drift Continuous learning, model monitoring, adaptive systems 2 4.80%
Deployment Challenges Research-production gap Time -to - market, integration complexity MLOps, automated pipelines, model serving platforms 0 0.00%
System Integration legacy systems Technological fragmentation API standardization, microservices, gradual migration 0 0.00%

J. A. Apaza-Caceres et al.  /International Journal of Data and Network Science 10 (2026)

285
5. Discussion

The results of this systematic review confirm the established dominance of deep learning techniques in machine learning
applications for digital advertising, with 66.6% of high- quality studies adopting neural network- based approaches (Deep
Neural Networks 35.7%, Attention- based Models 19.0%, and Recurrent Neural Networks 11.9%). This algorithmic
concentration is consistent with the observations of (Cheng et al., 2016; Lian et al., 2018) , who demonstrated the superiority
of specialized architectures such as Deep Interest Network (DIN) for modeling user behavior in advertising contexts.
The prevalence of hybrid models (9.5%), particularly DeepFM and Wide & Deep Learning,  reflects the recognition that
combining linear memoization and nonlinear generalization provides significant operational advantages (Cheng et al., 2016;
Guo et al., 2017) . This trend towards algorithmic hybridization suggests a maturing of the field where pure technical
performance optimization is balanced with considerations of computational efficiency and interpretability, aligning with
findings on (Lian et al., 2018) the effectiveness of architectures that explicitly combine explicit and implicit feature
interactions.
However, excessive concentration on deep Learning also presents methodological risks. As they point out (McMahan et al.,
2013)in their seminal analysis of large -scale click prediction , algorithmic sophistication must be balanced with practical
considerations of implementation, maintenance, and explainability. The underrepresentation of reinforcement techniques
learning (2.4%) and probabilistic methods (2.4%) indicate significant opportunities for methodological diversification,
particularly considering recent advances in contextual bandits for real-time bidding optimization (L. Li et al., 2010).
The approximate convergence toward CTR as the primary evaluation metric (95.2% of papers) produces an unparalleled
methodological state-of-the-art, even superior to the adoption of standard metrics in other areas of machine learning. Such
standardization undoubtedly facilitates comparison across papers; however, it also poses significant limitations. As argued,
(Bottou et al., 2007) strict CTR optimization can lead to suboptimal solutions from a long -term business value perspective,
especially when downstream metrics such as conversion and customer lifetime value are not taken into account.
The emergence of ROAS (11.9% of recent studies) as an alternative metric reflects an evolution towards indicators more
aligned with direct commercial objectives, consistent with the trends observed by (Kumar & Reinartz, 2016) In marketing
analytics, the technical consolidation around the AUC - Logloss pairing (83.3% and 76.2% respectively) provides a robust
basis for model evaluation, although as (Provost & Fawcett, 2001)these metrics point out, they may not fully capture practical
utility in contexts where the costs of different types of errors are asymmetrically distributed.
The complete absence of fairness metrics in the reviewed literature contrasts sharply with developments in other fields of
applied ML. This gap is particularly concerning considering the findings of (Lambrecht & Tucker, 2019) gender bias in
advertising algorithms, and suggests an urgent need to incorporate fairness -aware machine learning frameworks like those
proposed by (Dwork et al., 2012; Hardt et al., 2016).
The dominance of e-commerce (61.9% of studies) reflects structural characteristics that make this sector particularly suitable
for ML applications: availability of comprehensive transactional data, high value density per interaction, and relatively short
feedback loops (Adomavicius & Tuzhilin, 2005; Linden et al., 2003) . However, this concentration also limits the
transferability of results and can create methodological blind spots.
The strong dominance of the Alibaba ecosystem (14.3% of studies) compared to the limited representation of Western
platforms exposes profound differences in digital ecosystem architectures. As documented (Parker et al., 2016) , the " super-
apps " integrated into the Chinese market create unique opportunities for holistic user behavior modeling that are unavailable
in more fragmented ecosystems. This disparity suggests limitations in the cross -cultural transferability of techniq ues
developed for specific contexts.
The underrepresentation of regulated sectors (healthcare 0%, financial services 0%, education 0%) reflects systemic barriers,
but also represents significant opportunities. Advances in privacy preservation with machine learning , particularly federated
learning (Kairouz et al., 2021; T. Li et al., 2020), suggest that these limitations may be addressable, opening up new application
domains that are currently unexplored.
The persistent dominance of data sparsity as a fundamental limitation (59.5% of studies) across multiple algorithmic
generations indicates that this problem exceeds the existence of concrete technical solutions and is a challenge. This
persistence is consi stent with theoretical analyses of fundamental limitations in (Bell & Koren, 2007) sparse recommender
systems and suggests an opening for more fundamental research such as transfer learning and meta - learning. (Pan & Yang,
2010).
The emergence of scalability issues (14.3%) as a major limitation indicates the tension between algorithmic sophistication
and operational requirements; this trend is alarming since advertising data must grow exponentially (Chen & Guestrin, 2016).
Solutions that have been proposed in the literature, such as modeling compression (Han et al., 2016)and distributed computing
(Dean & Ghemawat, 2008), require specific research for advertising contexts where ultra-low latencies are highly relevant.

 286
Critical gaps in fairness (0%), sustainability (0%), and adversarial robustness (0%) highlight alarming methodological
shortcomings that urgently need to be addressed. The failure to consider fairness issues contrasts significantly with
developments in other areas of applied machine (Mehrabi et al., 2022) learning, while the failure to consider environmental
sustainability ignores the significant energy impact of large-scale machine (Schwartz et al., 2020; Strubell et al., 2019)learning
systems . The emergence of privacy-preserving techniques such as federated Learning reflects a reaction to regulations such
as the GDPR and the CCPA, but also points to opportunities for innovation that go beyond mere regulatory compliance and
move toward value creation (Kairouz et al., 2021) . The trend toward probabilistic models with uncertainty quantification
indicates an increase in methodological sophistication that can overcome the robustness limitations that have been highlighted
in deterministic systems (Kendall & Gal, 2017).
This systematic review, although comprehensive in its temporal and methodological coverage, has inherent limitations that
must be considered when interpreting its results. The focus on academic literature may underestimate industrial innovations
that go unpublished due to intellectual property considerations. Furthermore, the bias toward English- language publications
may limit the representation of developments in non-Western markets.
Quality assessment based on specific methodological criteria, although systematic, may have favored certain types of
contributions over others. In particular, studies focused on practical applications may have been undervalued relative to
fundamental algorithmic contributions, potentially distorting the representation of practical versus theoretical limitations.
6. Conclusions

This systematic review of the literature on machine learning in digital advertising, based on the analysis of 42 quality articles,
unfolds in a field characterized by significant algorithmic consolidation, notable metric convergence, but also by urgent and
relevant methodological gaps. First, the prevalence of deep learning techniques Learning (66.6% of articles) establishes a
certain technical consensus in favor of the superiority of these techniques for specific problems in the advertising domain.
The use  of hybrid methods (9.5%) suggests a progression in maturity toward approaches that can balance technical
performance and operational aspects. However, the very low representation of dominant techniques such as reinforcement
learning (2.4%) and probabilist ic methods (2.4%) suggests that there are significant opportunities for methodological
diversification. Second, the near-universal convergence toward CTR as the dominant metric (95.2%) aids comparability across
studies, but the pitfalls associated with the pursuit of local optimization may be present. The meteoric rise of ROAS (11.9%)
as an alternative metric and the widespread algorithmic reliance on AUC- Logloss establish a good technical basis, but a poor
technical basis, for evaluating publications. The  complete absence of equity metrics represents a critical gap that requires
urgent attention.
Finally, sectoral concentration in e -commerce (representing 61.9%) shows positive structural implications, although it also
limits the transferability of results. Dependence on specific platforms (Alibaba 14.3%, Amazon 4.8%) represents differences
in digital ecosystem architectures, as well as a geographic bias that cannot be ignored. The lack of regulation in specific sectors
is seen as both current limitations and future opportunities.
Furthermore, data scarcity remains one of the limitations of e -commerce, which has been preserved through several
algorithmic generations (59.5%). The emergence of scalability problems (14.3%) and computational costs (7.1%) suggests a
growing conflict between algorithmic sophistication and the viability of operational use.
This paper contributes to the existing body of knowledge in multiple dimensions. Methodologically, it presents, in a systematic
and quantitative manner, the first characterization of the algorithmic landscape in the context of ML for digital advertising ,
establishing the basis for future comparison. Empirically, it describes, highlighting the parallels between the study of
optimizations in academic settings and that of industry, the patterns of convergence and divergence that help establish research
priorities or decisions regarding industrial implementation, etc. Structurally, the identification of significant gaps detected in
the context of equity, sustainability, and robustness concludes with the development of a research agenda in which technical
optimization is replaced or complemented by the search for algorithmic adaptation to aspects related to responsibility and
social impact. Finally, the identification of persistent and emerging limitations helps influence the prioritization of resea rch
and development resource allocations.
The findings have significant implications for various stakeholders. For researchers, the existence of significant
methodological gaps reveals promising future paths in less -explored domains. The predominance of well -established
techniques points to the need for disruption rather than optimization. For industrial professionals, the focus on well-established
techniques and metrics simplifies decision -making, but at the same time, the pursuit of a pseudo- optimum is also inherently
risky. The emergence of scalability and computational cost limitations demands investments in more efficient infrastructure
or digital structures.
The findings suggest several avenues for future research. In the short term, there is a need to redevelop equity -focused
frameworks specific to advertising, given the potential for social impact and looming regulatory pressure. In the medium term,
research into green computing and sustainable artificial intelligence for advertising applications can address environmental
challenges and, at the same time, build certain competitive advantages.

J. A. Apaza-Caceres et al.  /International Journal of Data and Network Science 10 (2026)

287
At the methodological level, exploring under-researched techniques such as reinforcement learning and various probabilistic
methods can open up the possibilities for new capabilities. At the industry level, expanding into regulated domains through
privacy-preserving techniques can offer opportunities that have significant implications for both research impact and
commercial value.
In essence, developing solutions to persistent problems like data scarcity may require a paradigm shift toward transfer
learning, meta-learning, or entirely new methods that address emerging data sources and new computing paradigms.
Machine learning in digital advertising has evolved from an experimental field of application to a mature technical field with
significant commercial impact. However, the mature nature of this field also highlights the need to evolve toward greater
methodological diversity, ethical consideration, and sustainability awareness.
The field is at a crossroads where technical sophistication needs to be balanced with social responsibility and environmental
governance. The results of this review suggest that, although some technical progress has been made, the next stage of
development should focus on inclusive, sustainable, and ethically informed approaches to serve not only commercial purposes
but also broader societal goals. Future research must embrace this challenge, developing methodologies that are not only
technically excellent but also socially responsible, environmentally sustainable, and ethically sound.
References
Adomavicius, G., & Tuzhilin, A. (2005). Toward the next generation of recommender systems: a survey of the state -of-the-
art and possible extensions. IEEE Transactions on Knowledge and Data Engineering, 17(6), 734 –749.
https://doi.org/10.1109/TKDE.2005.99
Barbosa, B., Oliveira, Z., Teixeira, S. F., & Gomes, V . P. (2021). Understanding Google Ads metrics for SME. In Advanced
Digital Marketing Strategies in a Data-Driven Era. https://doi.org/10.4018/978-1-7998-8003-5.ch007
Bell, R. M., & Koren, Y . (2007). Lessons from the Netflix prize challenge. ACM SIGKDD Explorations Newsletter, 9(2), 75–
79. https://doi.org/10.1145/1345448.1345465
Berlilana, B. (2025). Enhancing Digital Marketing Strategies with Machine Learning for Analyzing Key Drivers of Online
Advertising Performance. Journal of Applied Data Sciences, 6(2), 817–827. https://doi.org/10.47738/jads.v6i2.658
Bhaskaraputra, A., Sutojo, F., Ramadhan, A. N., Agung Santoso Gunawan, A., & Anderies. (2022). Systematic Literature
Review on Solving Personalization Problem in Digital Marketing using Machine Learning and Its Impact. 2022
International Seminar on Application for Technology of Information and Communication (ISemantic) , 178 –182.
https://doi.org/10.1109/iSemantic55962.2022.9920387
Bottou, L., Chapelle, O., DeCoste, D., & Weston, J. (2007). Large-Scale Kernel Machines (Neural Information Processing) .
The MIT Press.
Chaffey Dave, & Ellis-Chadwick y Fiona. (2022). Digital Marketing (8th ed.). Pearson.
Chen, T., & Guestrin, C. (2016). XGBoost: A Scalable Tree Boosting System. Proceedings of the 22nd ACM SIGKDD
International Conference on Knowledge Discovery and Data Mining, 785–794. https://doi.org/10.1145/2939672.2939785
Cheng, H.-T., Koc, L., Harmsen, J., Shaked, T., Chandra, T., Aradhye, H., Anderson, G., Corrado, G., Chai, W., Ispir, M., Anil,
R., Haque, Z., Hong, L., Jain, V ., Liu, X., & Shah, H. (2016). Wide &amp; Deep Learning for Recommender Systems.
Proceedings of the 1st Workshop on Deep Learning for Recommender Systems , 7 –10.
https://doi.org/10.1145/2988450.2988454
Choi, J.-A., & Lim, K. (2020). Identifying machine learning techniques for classification of target advertising. ICT Express ,
6(3), 175–180. https://doi.org/10.1016/j.icte.2020.04.012
Dean, J., & Ghemawat, S. (2008). MapReduce: simplified data processing on large clusters. Communications of the ACM ,
51(1), 107–113. https://doi.org/10.1145/1327452.1327492
Deng, C., Wang, H., Tan, Q., Xu, J., & Gai, K. (2021). Calibrating User Response Predictions in Online Advertising (pp. 208–
223). https://doi.org/10.1007/978-3-030-67667-4_13
Duarte, V ., Zuniga-Jara, S., & Contreras, S. (2022). Machine Learning and Marketing: A Systematic Literature Review. IEEE
Access, 10, 93273–93288. https://doi.org/10.1109/ACCESS.2022.3202896
Dwork, C., Hardt, M., Pitassi, T., Reingold, O., & Zemel, R. (2012). Fairness through awareness. Proceedings of the 3rd
Innovations in Theoretical Computer Science Conference, 214–226. https://doi.org/10.1145/2090236.2090255
Gao, B., Wang, Y ., Xie, H., Hu, Y ., & Hu, Y . (2023). Artificial Intelligence in Advertising: Advancements, Challenges, and
Ethical Considerations in Targeting, Personalization, Content Creation, and Ad Optimization. Sage Open, 13(4).
https://doi.org/10.1177/21582440231210759
Gartner. (2025). Augmented Analytics Market Size and Share Outlook -  Forecast Trends and Growth Analysis Report (2025-
2034).
Gkikas, D. C., & Theodoridis, P. K. (2024). Predicting Online Shopping Behavior: Using Machine Learning and Google
Analytics to Classify User Engagement. Applied Sciences, 14(23), 11403. https://doi.org/10.3390/app142311403
Guo, H., Tang, R., Ye, Y ., Li, Z., & He, X. (2017). DeepFM: A Factorization -Machine based Neural Network for CTR
Prediction.
Guo, H., Yu, J., Liu, Q., Tang, R., & Zhang, Y . (2019). PAL:  a position-bias aware learning framework for CTR prediction in
live recommender systems. Proceedings of the 13th ACM Conference on Recommender Systems , 452– 456.
https://doi.org/10.1145/3298689.3347033

 288
Han, S., Mao, H., & Dally, W. J. (2016). Deep Compression: Compressing Deep Neural Networks with Pruning, Trained
Quantization and Huffman Coding.
Hardt, M., Price, E., & Srebro, N. (2016). Equality of Opportunity in Supervised Learning.
Henriques, P., & Oliveira e Sá, J. (2022). Proposal for a Digital Marketing Platform. Atas Da Conferencia Da Associacao
Portuguesa de Sistemas de Informacao, 19–36. https://doi.org/10.18803/capsi.v22.19-36
Kairouz, P., McMahan, H. B., Avent, B., Bellet, A., Bennis, M., Nitin Bhagoji, A., Bonawitz, K., Charles, Z., Cormode, G.,
Cummings, R., D’Oliveira, R. G. L., Eichner, H., El Rouayheb, S., Evans, D., Gardner, J., Garrett, Z., Gascón, A., Ghazi,
B., Gibbons, P. B., … Zhao, S. (2021). Advances and Open Problems in Federated Learning. Foundations and Trends®
in Machine Learning, 14(1–2), 1–210. https://doi.org/10.1561/2200000083
Kendall, A., & Gal, Y . (2017). What Uncertainties Do We Need in Bayesian Deep Learning for Computer Vision?
Khan, M., Ahmad, M., Alidjonovich, R. D., Bakhritdinovich, K. M., Turobjonovna, K. M., & Odilovich, I. J. (2025). The
impact of cultural factors on digital marketing strategies with Machine learning and honey bee Algorithm (HBA). Cogent
Business & Management, 12(1). https://doi.org/10.1080/23311975.2025.2486590
Kumar, V ., & Reinartz, W. (2016). Creating Enduring Customer Value. Journal of Marketing, 80(6), 36–68.
Lambrecht, A., & Tucker, C. (2019). Algorithmic Bias? An Empirical Study of Apparent Gender-Based Discrimination in the
Display of STEM Career Ads. Management Science, 65(7), 2966–2981. https://doi.org/10.1287/mnsc.2018.3093
Li, L., Chu, W., Langford, J., & Schapire, R. E. (2010). A contextual -bandit approach to personalized news article
recommendation. Proceedings of the 19th International Conference on World Wide Web, 661 –670.
https://doi.org/10.1145/1772690.1772758
Li, T., Sahu, A. K., Talwalkar, A., & Smith, V . (2020). Federated Learning: Challenges, Methods, and Future Directions. IEEE
Signal Processing Magazine, 37(3), 50–60. https://doi.org/10.1109/MSP.2020.2975749
Lian, J., Zhou, X., Zhang, F., Chen, Z., Xie, X., & Sun, G. (2018). xDeepFM: Combining Explicit and Implicit Feature
Interactions for Recommender Systems. Proceedings of the 24th ACM SIGKDD International Conference on Knowledge
Discovery & Data Mining, 1754–1763. https://doi.org/10.1145/3219819.3220023
Linden, G., Smith, B., & York, J. (2003). Amazon.com recommendations: item-to-item collaborative filtering. IEEE Internet
Computing, 7(1), 76–80. https://doi.org/10.1109/MIC.2003.1167344
Loukili, M., Messaoudi, F., & El Ghazi, M. (2023). Sentiment Analysis of Product Reviews for E -Commerce
Recommendation based on Machine Learning. International Journal of Advances in Soft Computing and Its Applications,
15(1), 1–13. https://doi.org/10.15849/IJASCA.230320.01
McKinsey & Company. (2024). The state of AI: How organizations are rewiring to capture value.
McMahan, H. B., Holt, G., Sculley, D., Young, M., Ebner, D., Grady, J., Nie, L., Phillips, T., Davydov, E., Golovin, D.,
Chikkerur, S., Liu, D., Wattenberg, M., Hrafnkelsson, A. M., Boulos, T., & Kubica, J. (2013). Ad click prediction: a view
from the trenches. Proceedings of the 19th ACM SIGKDD International Conference on Knowledge Discovery and Data
Mining, 1222–1230. https://doi.org/10.1145/2487575.2488200
Mehrabi, N., Morstatter, F., Saxena, N., Lerman, K., & Galstyan, A. (2022). A Survey on Bias and Fairness in Machine
Learning.
Murthy, A., Buddhi, D., Averineni, A., Narayana, M. S., Sowjanya, G. D., & Sowmya, Ch. (2023). Machine Learning as A
Predictive Technology and its Impact on Digital Markets. 2023 3rd International Conference on Advance Computing and
Innovative Technologies in Engineering (ICACITE), 672–676. https://doi.org/10.1109/ICACITE57410.2023.10182639
Murugan, P., Esakkiammal, S., Kanagavalli, N., Priya, P. K., Martis, J. E., & Kavitha, P. (2023). Revenue Forecasting Using
Distributed Machine Learning In Online Advertising Systems. 2023 International Conference on Research Methodologies
in Knowledge Management, Artificial Intelligence and Telecommunication Engineering (RMKMATE) , 1 –6.
https://doi.org/10.1109/RMKMATE59243.2023.10369815
Nirmal, E. S., Narang, P., Rajeswari, T. S., Usman, M., Subha, B., & Jadhav, V . S. (2022). The Application of Effective
Machine Learning Tools in Digital Marketing for Enhancing Brand Presence and Image Among the Fast -Moving
Consumer Goods in the Developing Countries. 2022 2nd International Conference on Advance Computing and Innovative
Technologies in Engineering (ICACITE), 2307–2311. https://doi.org/10.1109/ICACITE53722.2022.9823902
Pan, S. J., & Yang, Q. (2010). A Survey on Transfer Learning. IEEE Transactions on Knowledge and Data Engineering ,
22(10), 1345–1359. https://doi.org/10.1109/TKDE.2009.191
Parker, G., Van Alstyne, M. W., & Jiang, X. (2016). Platform Ecosystems: How Developers Invert the Firm. SSRN Electronic
Journal. https://doi.org/10.2139/ssrn.2861574
Pereira, I., Madureira, A., Bettencourt, N., Coelho, D., Rebelo, M. Â., Araújo, C., & de Oliveira, D. A. (2024). A Machine
Learning as a Service (MLaaS) Approach to Improve Marketing Success. Informatics , 11(2), 19.
https://doi.org/10.3390/informatics11020019
Proserpio, D., Hauser, J. R., Liu, X., Amano, T., Burnap, A., Guo, T., Lee, D., Lewis, R., Misra, K., Schwarz, E., Timoshenko,
A., Xu, L., & Yoganarasimhan, H. (2020). Soul and machine (learning). Marketing Letters , 31(4), 393 –404.
https://doi.org/10.1007/s11002-020-09538-4
Provost, F., & Fawcett, T. (2001). Robust Classification for Imprecise Environments. Machine Learning, 42(3), 203–231.
https://doi.org/10.1023/A:1007601015854
Qin, V . (2023). Lengthen your attribution window: Which digital ads have most long -term impact? Applied Marketing
Analytics: The Peer-Reviewed Journal, 9(1), 73. https://doi.org/10.69554/WPUS1821

J. A. Apaza-Caceres et al.  /International Journal of Data and Network Science 10 (2026)

289
Qin, V ., & Pauwels, K. (2023). Upper funnel ad effectiveness and seasonality in consumer durable goods. Applied Marketing
Analytics: The Peer-Reviewed Journal, 8(4), 345. https://doi.org/10.69554/CPYM7682
Ramya, T. E., Balasubramanie, P., Shanmughapriya, P., Ananthi, P., & Sakthiganesan, G. (2024a). Enhancing Click-Through
Rate Prediction: A Composite Approach Integrating DNN with DCN and FM -NN (pp. 391– 403).
https://doi.org/10.1007/978-981-97-7710-5_29
Ramya, T. E., Balasubramanie, P., Shanmughapriya, P., Ananthi, P., & Sakthiganesan, G. (2024b). Enhancing Click-Through
Rate Prediction: A Composite Approach Integrating DNN with DCN and FM -NN. In Lecture Notes in Networks and
Systems: Vol. 23 LNNS. https://doi.org/10.1007/978-981-97-7710-5_29
Rathi, S. R., Jadhav, N., Raut, A., Navhal, A., & Patil, M. (2024). Predictive Analytics Using Machine Learning for Enhanced
Online Advertising (pp. 281–306). https://doi.org/10.4018/979-8-3693-6705-6.ch011
ResearchAndMarkets. (2025). Programmatic advertising market trends and growth forecast report 2025-2033.
Salesforce. (2024). State of Sales Report: AI Impact on Revenue Growth.
Schwartz, R., Dodge, J., Smith, N. A., & Etzioni, O. (2020). Green AI. Communications of the ACM , 63(12), 54– 63.
https://doi.org/10.1145/3381831
Shah, A., & Technology Solutions, iWeb. (2021). The Impacts of User Experience Metrics on Click- Through Rate (CTR) in
Digital Advertising: A Machine Learning Approach Siddhesh Nasnodkar Article history (V ol. 4, Issue 1).
Shah, K. (2025, April 2). ROI for machine learning in ecommerce. Bloomreach.
Silva, J., Vargas, J., Vergara, D. R., Araya, G., Rosado, C., Lezama, O. B. P., & Quintero, B. (2020). CTR Prediction for
Optimizing the Negotiation of Internet Advertising Campaigns  (pp. 149–157). https://doi.org/10.1007/978-981-15-4875-
8_13
Statista. (2024). Digital advertising market outlook worldwide.
Strubell, E., Ganesh, A., & McCallum, A. (2019). Energy and Policy Considerations for Deep Learning in NLP. Proceedings
of the 57th Annual Meeting of the Association for Computational Linguistics , 3645– 3650.
https://doi.org/10.18653/v1/P19-1355
Ten26Media. (2025). The AI-powered advertising era: Your guide to navigating AI in paid media.
Thirumagal, P. G., Kishore Bhattacharjee, Dr., Dorbala, R., Palav, M. R., S, V ., & Mahajan, V . (2024). Application of Machine
Learning Algorithms in Personalized Marketing. 2024 5th International Conference on Recent Trends in Computer Science
and Technology (ICRTCST), 165–170. https://doi.org/10.1109/ICRTCST61793.2024.10578463
Verma, A., Singh, A., Verma, G., Yadav, A., & Sharma, A. (2024). A Performance Study of the Naive Bayes Classifier in
Advertisement Analysis. 2024 International Conference on Communication, Computer Sciences and Engineering
(IC3SE), 618–624. https://doi.org/10.1109/IC3SE62002.2024.10593497
Weng, M., & Long, Y . (2025). Research on Mobile Advertising Users’ Propagation Ability Evaluation based on the
Neutrosophic Cubic Number Multiple -Attribute Decision-Making Neutrosophic Sets and Systems. In Neutrosophic Sets
and Systems (V ol. 79).

 290

© 2026 by the authors; licensee Growing Science, Canada. This is an open access article
distributed under the terms and conditions of the Creative Commons Attribution (CC -BY)
license (http://creativecommons.org/licenses/by/4.0/).
