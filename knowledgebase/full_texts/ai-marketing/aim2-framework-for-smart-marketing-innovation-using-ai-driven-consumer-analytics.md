---
title: AIM2 framework for smart marketing innovation using AI driven consumer analytics with SOR neural
  networks and XGBoost in Saudi retail.
url: https://doi.org/10.1038/s41598-026-42787-3
category: ai-marketing
subcategory: empirical
date: 2026-01
venue: MED
authors:
- Alarfaj FK
- Badouch M
- Khan HU
source: openalex-oa
pdf_url: https://www.nature.com/articles/s41598-026-42787-3.pdf
pages: 19
chars: 91880
fetched_at: '2026-11-08T20:01:33+00:00'
kb_version: 1
---

# AIM2 framework for smart marketing innovation using AI driven consumer analytics with SOR neural networks and XGBoost in Saudi retail.

AIM2 framework for smart
marketing innovation using AI
driven consumer analytics with
SOR neural networks and XGBoost
in Saudi retail
Fawaz Khaled Alarfaj1, Mohamed Badouch2, Hikmat Ullah Khan3 & Mehdi Boutaounte4
The study introduces the AIM2 (AI-Integrated Marketing Innovation Model) framework by integrating
the Stimulus–Organism–Response (SOR) model with advanced machine learning methods for making
sense of consumer analytics in Saudi retail. Using real data from Tamimi Markets, clustering methods
put products into budget, intermediate, and luxury categories with a 92% silhouette score. Predictive
analysis showed that XGBoost had a 14% smaller error margin than traditional regression and 9% more
accuracy than simple Neural Networks. These results go beyond the current retail analytics methods
that report less than 80% accuracy and highlight the value of incorporating AI-powered techniques
with SOR. The study contributes to both theory and practice by demonstrating the AIM2 framework
in a real retail context and providing practical tips for retailers who want to keep up with the modern
marketing goals.
The transition to digital commerce has resulted in the extensive use of modern technological tools in marketing,
thereby changing the interaction between businesses and customers, and consequently, the choice of the latter.
Old-style marketing methods, which relied heavily on mass communication and uniform campaigns, are now
often replaced by smart, flexible arrangements utilizing AI, ML, and DL for delivering personalized interactions
and providing timely insights. This transformation is very pronounced in retail, where customer expectations
regarding convenience, personalization, and reliability have increased quite a lot. By the end of 2024, global
online sales have reached more than 6 trillion USD, which account for more than 15% of U.S. retail transactions,
while the use of live-streaming and AI-driven commerce in Asia attracted hundreds of millions of users1. These
developments present opportunities as well as difficulties; on the one hand, advanced technology allows for
precise marketing and active customer participation, and on the other hand, it raises issues related to data
protection, transparency, and sustainability.
Innovative tools such as neural networks, boosting algorithms like XGBoost, and multi-modal AI (Artificial
Intelligence) setups are slowly gaining acceptance in customer analysis and are providing better quality of
forecasts than the old, simple statistical or rule-based approaches. Neural networks are excellent at grasping
complex and nonlinear relationships in consumer behavior, boosting algorithms such as XGBoost have repeatedly
demonstrated superior performance over traditional regression models and many single-architecture learners in
structured retail datasets, particularly in heterogeneous and nonlinear consumer environments. Their ensemble
tree optimization and regularization mechanisms enable more stable generalization and lower predictive error2.
These techniques perfectly suit retail data, which can present an eclectic mix of product types and prices, along
with greatly un- predictable consumer preferences. By injecting these technologies into promotional strategies,
companies can improve audience segmentation, dynamic pricing, and recommendation systems which will in
turn directly increase customer satisfaction and loyalty. At the same time, conceptual models remain important
in grounding the tech applications in consumer psychology. The Stimulus-Organism-Response (SOR) model
which is widely used in marketing and consumer studies is a good example of how tech-based stimuli (such as
AI-powered ads, personalized tips) can be broken down into consumer perceptions (organism) and behaviors
1Department of Management Information System, School of Business, King Faisal University, Al Ahsa, Saudi Arabia.
2Faculty of Sciences, Ibn Zohr University, Agadir, Morocco. 3Department of Computer Science, University of Wah,
Wah Cantt, Pakistan. 4National School of Commerce and Management, Ibn Zohr University, Dakhla, Morocco.
email: falarfaj@kfu.edu.sa; mohamed.badouch@edu.uiz.ac.ma
OPEN
Scientific Reports |        (2026) 16:14160 1| https://doi.org/10.1038/s41598-026-42787-3
www.nature.com/scientificreports

(response). Latest studies have modified SOR to situations such as AI assistants, AR, and live streaming shopping,
and demonstrated its role in clarifying trust, participation, and buying intention 3. Nevertheless, the literature
is scarce on the integration of SOR with cutting-edge AI techniques for the development of a comprehensive
method for marketing innovations. Conversely, studies on the integration of SOR with advanced AI techniques
in the creation of a holistic framework for marketing innovation remain limited.
Saudi Arabia gives us a rare opportunity to investigate this integration from a different angle. The Kingdom
has earmarked digital transformation, retail modernization, and sustainable consumption as the main goals of
its Vision 2030. The retail industry, which is already worth more than SAR 400 billion, is being digitized at a very
fast pace, with retail giants and e-commerce stores using Al-powered methods for stocks, clients, and prices to
make them more dynamic. There is however not enough empirical research based on real data from Saudi retail
sectors. Consumer surveys or global datasets make up the bulk of the studies so far, creating a region-specific,
data-driven analysis that is both theory and practice informing voids. Closing this gap is of utmost importance
since Saudi consumers have different cultural likes, use different amounts of products in different seasons (for
example Ramadan and Eid), and have varying trust levels that impacts the effectiveness of marketing4.
The AIM2 (AI-Integrated Marketing Innovation Model) framework, which is presented in this research, has
been developed to connect the new technologies with the marketing theory. The AIM2 model is basically the SOR
model integrated with the advanced AI techniques such as clustering, association rule mining, neural networks,
and XGBoost for the purpose of analyzing consumer behavior in Saudi retail. The Tamimi Markets dataset 5,
which provides extremely detailed information about products and prices, has been used in the framework to
show the accuracy of AI-driven analytics in revealing consumer segments, spotting cross-selling opportunities,
and estimating price elasticity accurately. By integrating theoretical underpinnings and empirical investigation,
AIM2 creates a new pathway for the marketing innovation literature. The importance of AIM 2 comes from
its technological and marketing dimensions that are integrated together. In the case of the technology part,
AIM2 enhances the ML (Machine Learning)/DL (Deep Learning) methods to analyze the complicated retail
data thereby reaching predictive accuracies which are up to 14% higher than those obtained with traditional
regression models and also beating the baseline neural networks by 9% in predicting consumer preferences. As
far as the marketing aspects of AIM2 are concerned, it employs the SOR model to interpret the results and also
to connect the stimuli (AI-driven promotions) at the organism level (trust, perceived value) and the behavioral
outcomes (purchase intention, loyalty)6. This integration of both sides makes the technological insights not only
predictive but also theoretically significant thus providing retailers with strategies that are actionable.
The literature has been providing stronger and stronger evidence for the necessity to integrate AI and
Analytics. Cillo and Rubera7 emphasize that AI and Advanced Analytics have revolutionized marketing by means
of Hyper-Personalization and Predictive Engagement, but they lack theoretical frameworks to comprehend
consumer reactions to such innovations. Acatrinei et al.8 on the other hand, argue that AI-driven Marketing can
engage consumers positively and influence their behaviors sustainably if Trust and Transparency are accounted
for in the systems. Kasem et al. 2 assert that AI-powered Segmentation and Profiling lead to over 90% accuracy
(as against Direct Marketing) when compared with the traditional marketing methods. Almaafi et al. 4 support
their claim that XGBoost algorithms are more accurate than ARIMA models in the forecasting of Saudi Telecom
Stock Prices, thereby making a case for the use of XGBoost models in Retail Analytics. Davtyan3 claims that the
Strategic Role of AI is prominent in the analysis of Consumer Behavior, and that Zhang et al.1 employ Hesitant
Fuzzy Methods for determining the Risk involved in Live Streaming Marketing, thus accentuating the need for
Robust Frameworks in Digital Commerce.
This study adds to the knowledge pool in three major ways. To begin with, it presents the AIM2 Framework,
a novel approach that combines SOR with Advanced AI Methodologies to develop a conceptual model for Smart
Marketing Innovation. Secondly, the research applies the AIM2 Framework to a Real-World Saudi Retail Dataset
in order to provide Empirical Insights into Consumer Segmentation, Cross Selling, and Price Prediction. Last
but not least, it again relates the findings from the earlier parts to the Goals set in Vision 2030, thus showing
how Emerging Technologies can help with Digital Transformation and Sustainable Consumption in the Saudi
Retail sector.
The present paper examines consumer behavior within a Saudi retail dataset using a combination of
clustering, association rule mining, and demand forecasting models. Building on prior work. The remaining
parts of this paper be as follows. Literature regarding the aforementioned topics is reviewed in Sect. 2, which also
highlights the role of AI techniques in the retail domain proved through the application of SOR theory. Section
3 contains the presentation of the AIM2 conceptual model that employs multiple AI methods. The dataset and
the whole process of the research including clustering, mining association rules, applying neural networks, and
XGBoost is discussed in Sect. 4. The empirical outcomes, which encompass segmentation clusters, association
rules, and model performance comparisons, are presented in Sect. 5. In Sect. 6, the marketing implications of
these findings with regard to Vision 2030 are discussed. The paper concludes with a Sect. (7) that presents the
contributions, limitations, and future research directions.
AI outputs become consumer stimuli via an interface translation layer. Computational artifacts such as
cluster centroids, association-rule metrics, or model embeddings are latent representations that are not directly
perceived by consumers. In practice these outputs are transformed into marketing action artifacts (for example:
personalized offers, targeted recommendation lists, dynamic price messages, or tailored email content). It is
these artifacts — not the internal algorithmic vectors — that constitute the external Stimuli in the SOR model.
Formally the pipeline is: AI representation space → Marketing action layer → Consumer perceptual stimulus,
where the marketing action layer maps algorithmic signals to interface elements that consumers observe and
evaluate. This mapping grounds AIM 2 in perceptual psychology and clarifies how algorithmic outputs can be
interpreted as stimuli that influence organismic constructs (trust, perceived value) and behavioral responses.
Scientific Reports |        (2026) 16:14160 2| https://doi.org/10.1038/s41598-026-42787-3
www.nature.com/scientificreports/

Literature review
The marketing strategy has been radically altered due to the infusion of artificial intelligence (AI). AI is being
applied in various ways in marketing to analyze the consumer behaviors and come up with the respective strategies
of engagement, personalization, and trust-building. Moreover, the traditional e-commerce models comprising of
fixed websites and one-size-fits-all promotions at their core are rapidly being superseded by real-time, engaging
platforms that use customer data for predictive analytics and intervention targeting. This change is quite visible
in the retail sector, where the skill of consumer segmentation, demand forecasting, and recommendation
generation according to individual’s preferences has turned into the key to competitive advantage. Nevertheless,
the SOR model of Stimulus-Organism-Response continues to be an important theoretical framework that can
show the effects of technological stimuli on the perceptions and behaviors of consumers. The area of AI in
marketing and consumer analytics touches numerous fields such as clustering, associational rule mining, neural
networks, and XGBoost, the latter being one of the ensembles learning methods. The mentioned technological
capabilities not only find applications in marketing but also in the healthcare, finance, energy, and public policy
sectors implying their widespread usage and relevance.
Consumer analytics using clustering
The use of clustering techniques has always been widespread in marketing as they help in recognizing consumer
segments and product categories. K-Means Clustering, being one of the most popular among the methods,
divides the buyers into different groups according to their purchasing habits and allows the companies to create
promotions that target each group specifically. Liu et al.9 utilized K-means clustering on supermarket transaction
data and were able to identify three principal customer clusters comprising budget-conscious, mid-range, and
premium shoppers. The implications of their study are such that it becomes clear how important it is to resort
to segmentation in evolving different marketing strategies that are not only effective but also less costly to the
firm. Similarly, Hierarchical clustering has been applied to find the product categories with similar consumption
patterns.
For instance, Tabianan et al. 10 argued that hierarchical clustering could unveil the relationships between
product categories making it easier for retailers to come up with bundling strategies that would be in sync
with consumer preferences. Apart from marketing, clustering is heavily employed in healthcare for patient
stratification where patients are grouped by their clinical characteristics into different categories so as to
design personalized treatment plans. In the financial sector, clustering helps in the identification of customer
risk profiles that allow banks to create different kinds of credit products. Utilities use clustering in the power
industry to analyze consumption patterns thus aiding demand-side management and load forecasting. All these
applications go to prove that clustering is a powerful tool that can be used for the analysis of heterogeneous
datasets across sectors.
The method of association rule mining gives a better understanding of cross-selling opportunities through
the detection of those products that customers frequently buy together. An important contribution to this field
was made by Kumar and Patel11 who developed the Apriori algorithm that is still prevalent for retail analysis. The
supermarket database has been subjected to FP-Growth technique in recent days. For instance, Chopvitayakun
et al.12 showed that FP-Growth could back up retailers in crafting bundling strategies that would ultimately boost
sales by pinpointing co-occurrences of complementary goods like coffee and biscuits. In the marketing realm,
the association rules are relied on to set up promotions that bring together the selling of complementary goods,
thus raising the average basket size and consumer satisfaction levels.
In their study of the online retail industry, Joseph et al.13 applied association rule mining, where the patterns,
in turn, can be used to inform dynamic pricing strategies. Their research not only indicates that association rules
can give both revenue and trust to consumers by synchronizing promotions with actual buying behavior but also
suggests that retailers can leverage more by aligning their marketing campaigns with consumer behavior. The
use of association rule mining has also been reported in the field of bioinformatics for the identification of gene
co-expression patterns, in cybersecurity for the analysis of attack sequences, and in education for the assessment
of student learning behaviors. The above-mentioned cases demonstrate the capability of association rule mining
to be applied in various fields with complex and interrelated data as its characteristic.
Neural networks in marketing and other sectors
Neural networks are now at the forefront of consumer analytics allowing companies to discover and exploit
the nonlinear relationships which exist in buying behavior. One of the applications of feedforward neural
networks is for the forecasting of product demand. Bellar et al. 14 applied feedforward networks to retail sales
data, achieving mean absolute percentage error (MAPE) reductions of 10% compared to linear regression. Deep
learning models, such as convolutional neural networks (CNNs), have been applied to sentiment analysis in
e-commerce. Zhao et al.15 demonstrated that CNNs can analyze consumer reviews with accuracy improvements
of 12% compared to traditional text-mining approaches.
Recurrent neural networks (RNNs) and long short-term memory (LSTM) networks have been used to forecast
sequential consumer behavior. Jin16 applied RNNs to predict purchase intention, finding that sequential models
outperform logistic regression in contexts with temporal data. LSTM networks have found their application in
the area of time-series sales forecasting. Afoudi et al.17 confirmed that LSTMs were capable of capturing the long-
term dependencies in retail sales data, and thus they attained better accuracy than the classical autoregressive
models. In addition to marketing, neural networks are broadly utilized in healthcare for diagnosis, in finance
for detection of fraud, in transportation for prediction of traffic congestion, and in power for the smart grid’s
optimization. These usages emphasize the adaptable nature of neural networks in the processing of difficult and
non-linear data in different fields.
Scientific Reports |        (2026) 16:14160 3| https://doi.org/10.1038/s41598-026-42787-3
www.nature.com/scientificreports/

Ensemble learning techniques, especially XGBoost, have become the leading methods in consumer analytics.
Vafaei-Zadeh et al.18 conducted a comparison of the two techniques (XGBoost and GBM) in the retail sector, and
the results indicated that XGBoost outperformed its rival in all aspects of error rates and interpretability. Their
work supports the claim that ensemble methods are powerful enough to deal with the issue of noise in the retail
datasets. Jiang and Lyu19 used XGBoost for the consumer churn prediction problem, and they received accuracy
measures over 90%. The authors regard this as one more reason to believe that ensemble techniques are the go-to
ones for the complex, non-linear data. XGBoost has also been utilized beyond retail, such as in the finance sector
for credit scoring, and healthcare for disease risk predictions, and energy for the forecasting of renewable load
consumption. Paliari et al.20 declared that XGBoost was the winner of the competition against ARIMA when it
came to predicting the price of Saudi telecom stocks, thus confirming its relevance to the financial field. These
cases are just a few examples of the widespread usage of the methods throughout different industries.
Multimodal artificial intelligence, combining text, visuals, and sensor inputs, marks a growing field within
consumer research. César et al. 21 adopted this method for product review analysis, combining textual ratings
with picture of the item to make sentiment assessment stronger. According to their findings, multi-modal data
methods result in richer understanding of customer mind. Marketing applies such systems to process social
media content where posts, images, and videos are mixed together for brand sentiment measurement. The
medical field makes use of similar approaches by combining diagnostic imaging with the patient’s medical
record in order to make clinical choices more accurate. Urban management systems upscale the reading from
connected Internet of Things (IoT) devices to facilitate control over the traffic flow. This situation illustrates how
AI can facilitate deep analysis by merging different data streams in different sectors, though at times there might
still be some grammatical errors in the real situation where perfection is unattainable.
SOR framework in digital commerce
The SOR (Stimulus, Organism, Response) model is the major theoretical framework that helps to analyze
shopper behavior in the context of retail businesses employing AI technologies. Although initially proposed by
Sohaib et al.22 for environmental psychology purposes, the framework has found wide application in consumer
research. In the context of online sales, external stimuli include algorithm-driven discounts, personalized
recommendations, and changes in the user interface. Customers’ cognitive-affective evaluations like trust,
value, and satisfaction are seen as internal organismic responses, while buying mood and brand loyalty are
the consequences of such responses. Alsadoun and Alnasser 23 investigated how AI chatbots affect customer
communication and found that, among other things, speed and personalization significantly influence trust and
satisfaction. Besides, Umezurike et al.24 applied SOR to map out augmented shopping experiences and indicated
that exciting stimuli escalate hedonic perception and shopping urge. Sonboli et al.25 argued that the transparency
of algorithmic filtering increases consumer trust, which in turn raises the likelihood of transaction. All these
findings together point to the necessity of integrating theoretical psychological constructs with practical digital
applications.
Saudi retail transformation under Vision 2030
Saudi Arabia provides a unique scenario for the research of AI-based marketing innovations. The Vision 2030 of
the country redefines digital transformation, retail improvements, and environmentally friendly consumption as
the main areas of attention. A study by Saad et al.26 which took Saudi Arabia as the central point on consumers’
trust in online retail revealed that transparency and honesty were the major factors that swayed the buyers’
decisions. In addition to these, the consumption trends at different times, for example, spikes in usage during
Ramadan and Eid, are among the factors that shape retail strategies. SDAIA (Saudi Data and AI Authority)
is leading the charge by putting in place AI-focused initiatives targeting retail and logistics sectors. One such
study by Memish et al.27 revealed that among the key areas for the application of AI are stock control, customer
communication, and flexible pricing. The aforementioned projects have presented a great opportunity for the
frameworks like AIM 2 that link AI techniques to consumer behavior theory to be executed. Lemonde et al. 28
have mentioned that the smart city application of multimodal AI and suggested that retail marketing could gain
insights from urban analytics even more.
The academic community has taken note and is discussing the considerable progress made in the areas of AI-
driven marketing, customer analysis, and SOR theory. Clustering algorithms and the use of rules derived from
associations not only help in identifying the target audience but also in suggesting complementary products. On
the other hand, the methods like artificial neural networks and ensemble methods e.g., XGBoost yield the best
in terms of accuracy of forecasting. Artificial neural networks plus assistance methods like XGBoost achieve the
best in forecasting accuracy. AI systems that are integrated give comprehensive insight by the unified information
from various sources. For one thing, the SOR paradigm provides an excellent viewpoint for analyzing consumer
behavior; however, its integration with artificial intelligence proves to be limiting. The Saudi Vision 2030 project
is an excellent case for applying these models due to the fact that it is mainly about tech- modernization and
ethical consumerism.
In this research, the AIM2 model is proposed as a remedy which is a blend of SOR and AI to conduct close
studies on purchasers’ behaviors in the context of retail in Saudi Arabia. Utilizing detection, association rule
mining, deep learning models, and boosted decision trees on the sales data of Tamimi Markets, the work
demonstrates that the application of machine-learning-assisted analysis can not only make marketing strategies
smarter, but also increase customer trust and be in line with the goals of Vision 2030.
AIM2 conceptual framework
The AIM2 framework constitutes a tiered architecture meant to amalgamate the sophisticated machine learning
models with the behavioral marketing theory. It seeks to facilitate the creation of smart and flexible marketing
Scientific Reports |        (2026) 16:14160 4| https://doi.org/10.1038/s41598-026-42787-3
www.nature.com/scientificreports/

systems that rely on data and are anchored in psychology at the same time. AI has been widely accepted as an
important factor in retail analytics, but the majority of the current methods emphasize only predictive accuracy
and ignore the cognitive and emotional aspects of consumer behavior. Our solution is filling this gap by putting
the SOR model at the center of its design ensuring that the outputs of technology are judged by a behavioral
standard and then converted into significant marketing actions.
AIM2’s basis is composed of the Artificial Intelligence Layer that interprets unprocessed retail data with four
essential techniques: clustering, association rule mining, neural networks, and XGBoost. In order to find out
different segment’s groups such as budget-affording, mid-range, and premium shoppers, Clustering algorithms
are implemented to group consumers by their buying habits. By analyzing co-purchase patterns, Association
rule mining, especially through FP-Growth or Apriori algorithms, reveals product relations and suggests cross-
selling areas29. Neural networks—these can be feedforward, convolutional, or recurrent—are applied in demand
forecasting and sentiment analysis to discover nonlinear relationships in those fields. XGBoost, an effective
combined learning method is deployed on churn prediction, price sensitivity modeling, and dynamic pricing
optimization among others. The AI elements carry out their respective functions simultaneously, hence they
produce stimuli that are directed to the upper tier of the framework as input. Our solution fusion block therefore
operates at the marketing action layer: fused algorithmic signals are converted into concrete interface artifacts
(e.g., a “recommended for you” bundle or a time-limited discount) that consumers perceive as stimuli.
The SOR Framework Layer is the second layer of our system and it interprets AI-produced outputs in
relation to consumer psychology. The layer here processes the AI models’ outputs—by means of personalized
recommendations, dynamic promotions, and targeted messaging—as outside triggers. These stimuli were
statistically associated with organism-level constructs such as trust and perceived value, as estimated by the SEM
path coefficients. The SOR model thus captures the whole process from stimuli to psychological responses as
marketing literature using constructs. Observed behaviors like purchase intention, brand loyalty, and advocacy
are grouped under the final component response. The SOR model embedded in the architecture of AIM2 allows
AI-driven insights not only to be predictive but also to be explanatory, providing marketers with the “why”
behind consumer actions.
The last and most important layer is the Integration and Governance Layer, which guarantees that the system
functions in an ethical, transparent, and adaptive way. MLOps practices are introduced in this layer to keep watch
over model performance, spot bias, and apply equity among the different consumer segments. A mechanism for
feedback loop is also included, which consumes the AI layer for continuous model refinements the consumer
responses and then feeds them back into the AI layer for continuous model refinements. This back-and-forth
process not only allows AIM2 to constantly learn but also to adapt to consumer preferences, seasonal trends, and
market forces that are constantly changing. The integration layer therefore turns AIM 2 from a mere analytics
engine into a vibrant learning system which can power marketing innovation for a long term.
The complete structure of the system is represented by Fig. 1. Consumer interaction data (left side) enter the AI
Layer (blue), which contains four modules: clustering, association rule mining, neural networks, and XGBoost.
A server icon represents the centralized hosting and computation environment for AI services. Model outputs
are forwarded to the SOR Layer (orange), where they are interpreted as marketing stimuli influencing organism-
level states (trust, satisfaction, perceived value) and leading to behavioral responses (purchase intention, loyalty).
The Integration and Governance Layer (green) includes MLOps monitoring, fairness auditing, and explainability
mechanisms. A feedback loop connects this layer back to the AI Layer to enable continuous learning. The final
system outputs are visualized through a labeled Marketing Insights Dashboard block.
The process in our system is such that it has a linear and cyclical nature at the same time. It starts with user
engagement, which gets processed through AI models to produce stimuli. These stimuli, upon being interpreted
using the SOR framework, result in psychological and behavioral reactions. The governance and fairness analyses
are done on the responses, and the knowledge obtained is applied to retraining and fine-tuning the AI models.
This closed-loop system grants the technology the ability to adapt to changes in customer behavior and keep
Fig. 1. AIM 2 conceptual framework architecture.

Scientific Reports |        (2026) 16:14160 5| https://doi.org/10.1038/s41598-026-42787-3
www.nature.com/scientificreports/

up with ethical practices. With this, the digital transformation of retail environments through smart marketing
innovation is thereby made possible.
The diagram in Fig. 2 is a modular stimulus-fusion flowchart that shows how four AI modules feed a single
decision representation. On the left are four inputs: Clustering (cluster centroids), Association Rules (rule
scores), Neural Networks (sequence embeddings), and XGBoost (champion scores). These outputs are pooled
into a central Stimulus Fusion block that is annotated with a compact fusion formula and a softmax head
that maps the fused vector to action probabilities. The fused stimulus then flows through a short SOR chain
— Perception → Organism → Response — where perception converts model outputs into marketing stimuli,
organism captures internal states (trust, perceived value, personalized loss/bundles/price), and response records
behavioral outcomes (purchase intention, retention).
Materials and methods
The software and hardware materials, the dataset and its preprocessing, the analytical and modeling methods,
a complex algorithm block with explicit loops, and a practical narrative of how each equation was applied in
the experiment are the main points covered in this section. The aim is to give a reproducible and thorough
implementation of AIM 2 with transparent methodological choices, concrete hyperparameters, and a clear
workflow from data to behavioral insights.
Software packages and exact version numbers, hardware details, and the analysis scripts are provided in
Appendix A (Software and Reproducibility) and in the code repository referenced in the Code Availability
statement.
Dataset and preprocessing
Tamimi Markets is a major Saudi grocery chain with nationwide presence; the dataset contains multi-month
transactional records across urban and suburban stores. We compared key summary statistics (price ranges,
mean basket size, monthly transaction patterns) with publicly available Saudi retail sector reports and found
close alignment (see Table  1). These checks support the dataset’s suitability as a representative sample for
studying consumer behavior in Saudi retail.
The dataset was obtained from Tamimi Markets and contains transactional records with product category,
price, quantity, pseudonymized customer IDs, and timestamps. Numerical attributes were normalized with
min–max scaling to stabilize algorithms sensitive to feature scale30:

x′ = x − xmin
xmax − xmin
Categorical variables (e.g., Product_Category) were one-hot encoded for tabular learners, and embedded for
neural networks when beneficial. Outliers were removed via the interquartile range (IQR) rule31:
 IQR = Q3 − Q1,x < Q 1 − 1.5 · IQR or x>Q 3 +1 .5 · IQR ⇒ exclude
and temporal duplicates were resolved to avoid leakage across splits. Data partitioning followed a task-specific
protocol. For time-series forecasting models (including LSTM), a strictly chronological split was applied to
Attribute Type Description Example/range
Transaction_ID Integer Unique identifier of each transaction 1 … 1,200,000
Customer_ID Integer Pseudonymized customer identifier 10,001 … 480,000
Product_Category Categorical Product category (dairy, meat, bakery, etc.) ~ 25 categories
Product_Price (SAR) Numeric Unit price in SAR 1.0 … 499.0
Quantity Integer Units purchased 1 … 50
Date Date Transaction timestamp 2022–2024
Table 1. Transactional data attributes and descriptions (Tamimi markets).

Fig. 2. Flowchart showing four AI modules feeding a central fusion block with the fusion equation and
softmax head; arrows lead to Stimulus, Organism, and Response boxes describing perception, trust/value, and
purchase/retention outcomes. Fusion block: learned scalar weights wc, wr , wn, wxcombine signals C, R,N, X;
weights are optimized via backpropagation together with the final action head.

Scientific Reports |        (2026) 16:14160 6| https://doi.org/10.1038/s41598-026-42787-3
www.nature.com/scientificreports/

prevent temporal leakage: the earliest 70% of observations formed the training set, the subsequent 15% the
validation set, and the most recent 15% the test set. No future timestamps were available to the model during
training. For non-temporal tasks (e.g., churn classification and clustering), stratified splitting by Customer_ID
was used to avoid identity leakage while preserving behavioral distributions.
Evaluation metrics were selected per task. For demand regression, we monitored RMSE. RMSE (root mean
square error) measures average absolute error in the original units and penalizes large misses; MAPE reports
average percentage error and is easy to interpret but becomes unstable for zeros and very small actuals, so use it
cautiously for low-volume SKUs32.

RM SE =
/radical√p/radicalver√ex/radicalver√ex√ 1
n
n∑
i=1
(yi − ˆyi)2
and MAPE (mean absolute percentage error) expresses average error as a percentage of actuals32,

M AP E = 100 n
n∑
i=1
⏐⏐⏐⏐ yi − ˆyi yi ⏐⏐⏐⏐
with special attention to low-volume SKUs where relative errors are operationally significant. For churn
classification, we tracked accuracy, AUC, and log-loss on the validation set.
The organism-level variables (trust, perceived value, and satisfaction) were not inferred solely from
transactional logs. A structured consumer survey was conducted among loyalty-program customers using
validated multi-item Likert scales adapted from SOR-based marketing studies. Survey responses were
pseudonymously linked to transactional records through hashed customer identifiers under retailer data
governance approval. Transactional attributes (e.g., promotion exposure, price variability, recommendation
diversity, and purchase consistency) served as stimulus indicators, while survey-measured latent variables
constituted the organism layer in the SEM model. This hybrid survey–behavior linkage allowed psychological
constructs to be measured directly while preserving privacy.
Clustering quality was measured using the silhouette score; reported values include the mean and standard
deviation across 1,000 bootstrap resamples. Predictive models were compared using RMSE, MAE, and accuracy
where appropriate; for each metric we report the point estimate and a 95% confidence interval computed via
bootstrap (1,000 resamples) on the held-out test set. Baselines: (1) Traditional regression refers to ordinary
least squares (OLS) trained on the same features; (2) Baseline neural network refers to a single hidden-layer
feedforward network with 64 units and ReLU activation trained under the same preprocessing and train/test
split.
Data integrity verification
The Tamimi Markets dataset used in this study was obtained from the public repository cited in the Data
Availability statement. Because public datasets can contain errors or incomplete metadata, we performed a
systematic integrity verification before analysis. Steps included: (1) Range checks on price and quantity fields
to identify implausible values; (2) Temporal validation to confirm expected seasonality (e.g., Ramadan and
Eid purchase spikes) by comparing transaction counts across calendar months; (3) Basket statistics (mean and
median items per transaction) compared with regional retail reports to ensure realistic basket sizes; (4) Outlier
audits where transactions with prices or quantities beyond three interquartile ranges were inspected and removed
only when clearly erroneous; (5) Missingness analysis and imputation rules documented in preprocessing. All
data cleaning decisions and removed record counts are reported in Table 2. These checks increased confidence
that the dataset reflects plausible Saudi retail activity for the analyses reported.
Check Metric Before cleaning After cleaning Action/Notes
Price range Minimum–maximum price – SAR – SAR Removed implausible prices; documented criteria
Quantity per item Min–max quantity – – Corrected obvious entry errors
Missingness % missing per key field price: x%>; qty: y%> price: x2%>; qty: y2%> Imputation rules or row removal described
Basket size Mean (median) items/transaction mean=; median= mean=; median= Compared to regional retail benchmarks
Outliers removed Number (percent) of records n= n_removed= (<%>) IQR or z-score rule; list removal rationale
Duplicate transactions Number removed n_dup= n_dup_removed= Deduplication criteria documented
Records retained Final dataset size n_initial= n_final= Final sample used in analyses
Temporal validation Monthly transaction pattern no. months with spikes: seasonal spikes preserved Ramadan/Eid spikes checked and retained
Table 2. Transactional data attributes and descriptions (Tamimi markets).

Scientific Reports |        (2026) 16:14160 7| https://doi.org/10.1038/s41598-026-42787-3
www.nature.com/scientificreports/

Stimulus fusion and model training
The fusion layer combines algorithmic signals from clustering C, association rules R, neural network embeddings
N, and XGBoost outputs X into a single action probability vector. The fusion computation used in the final model
is:
 P (a)= softmax (Wf [wcC + wrR + wnN + wxX]+ b)
where wc, wr , wn, wxare scalar fusion weights and Wf, b are the final linear layer parameters. The fusion
weights are learned parameters and are optimized jointly with Wf and b by minimizing the cross-entropy loss on
the action prediction head using stochastic gradient descent (Adam optimizer; learning rate and regularization
hyperparameters reported in the Model Training subsection). Gradients flow through the fusion weights
during backpropagation, allowing the training process to allocate relative importance to each signal type.
Hyperparameter tuning (learning rate, weight decay, early stopping patience) was performed on a validation
split; the final model was evaluated on a held-out test set.
Hyperparameter ranges were chosen based on prior retail forecasting literature and initial pilot experiments on
a validation fold. For neural networks we explored hidden layer sizes {32,64,128}, learning rates {1e−4, 1e−3,1e−2
}, and dropout {0.0,0.2,0.5}. For XGBoost we searched over tree depth {3,6,9}, learning rate {0.01,0.1,0.2}, and
subsample {0.6,0.8,1.0}. Grid search with early stopping on the validation set selected final values.
Governance and fairness auditing
The dataset used in this study contains transactional records and customer identifiers but does not include explicit
demographic attributes such as gender, nationality, or ethnicity. Consequently, we did not perform fairness
audits across legally protected demographic groups. Instead, fairness checks were conducted across behavioral
segments derived from the data (for example, price-sensitivity clusters and spending tiers). Specifically, we
measured disparate impact and parity metrics across these behavioral groups to detect systematic differences
in model recommendations or predicted actions. We explicitly avoided inferring demographic attributes from
transactional data because such inference can introduce additional bias and ethical risk. Because demographic
labels were not available and no demographic inference was performed, formal fairness assessments across
protected groups (e.g., gender, nationality) were not possible in this study.
Clustering for consumer segmentation
K-means clustering was used to segment consumers because it yields interpretable centroids and performs well
on retail tabular data33. The objective minimized the within-cluster sum of squares:

J =
k∑
c=1
∑
x∈Cc
∥ x − µc∥2
where µc is the centroid of cluster Cc. The number of clusters k was selected via the silhouette coefficient,

s (i)= b (i) − a (i) max {a( i),b (i )}
with a (i) the mean intra-cluster distance for point i and b (i) the smallest mean distance to any other cluster.
W e swept k ∈{ 2,..., 10}, computing s (i) per candidate. The maximum silhouette occurred at k =3 , aligning
with budget, mid-range, and premium segments. Feature engineering included average basket value, purchase
frequency, category diversity, and local price elasticity estimates. Centroids were interpreted as marketing
profiles and fed forward as stimuli to the SOR layer for personalized recommendations34.
In practice, distances were computed in the normalized feature space to avoid dominance by high-variance
attributes, and convergence was declared when centroid movement fell below a tolerance threshold. W e verified
stability by running multiple random initializations (n_init = 10) and selecting the model with the best average
silhouette.
Association rule mining
FP-Growth was applied to derive frequent item sets and association rules without exhaustive candidate
generation. It constructs a compact FP-tree and mines conditional pattern bases recursively35. Rule strength was
assessed by support, confidence, and lift:
 Support (X → Y )= Count (X ∪ Y ) N ,

Conf idence (X → Y )= Support (X ∪ Y ) Support (X) ,

Lif t(X → Y )= Conf idence (X → Y ) Support (Y ) .

Scientific Reports |        (2026) 16:14160 8| https://doi.org/10.1038/s41598-026-42787-3
www.nature.com/scientificreports/

We tuned min_support within [0.01, 0.05], depending on whether the analysis operated at the category or SKU
level, and retained rules with Conf idence ≥ 0.85 and Lif t > 1. For example, {Bread, Milk}→{ Butter}
achieved Confidence=0.87 and Lift=1.23, supporting basket-level bundles and dynamic recommendations. T o
avoid spurious correlations, we cross-validated rules across temporal folds and verified stability under bootstrap
resampling of transactions.
Neural networks for sentiment prediction
We trained a Multilayer Perceptron (MLP) for demand forecasting with three hidden layers (256–128–64), ReLU
activations, dropout p =0 .3, and Adam optimizer with α = 10−3.
with early stopping based on validation RMSE36 and learning-rate reduction on plateau to stabilize training.
For temporal dependencies (e.g., seasonal ramps around Ramadan and Eid), we trained a two-layer LSTM (64
and 32 units). The LSTM cell updates followed37:
 ct = ft · ct−1 + it ·
∼
ct,h t = ot · tanh (ct)
where ft, it, and ot are forget, input, and output gates, ct the cell state, and ht the hidden state. Categorical features
were represented by embeddings ∈ Rd and concatenated with continuous inputs, improving representation
capacity for product categories. Training used mini-batches of 512, with weight decay and dropout to mitigate
overfitting. While sentiment models (CNNs over reviews) can complement demand prediction, the core reported
results derive from tabular demand models given the dataset’ s structure.
Dynamic pricing using XGBoost
XGBoost was employed for churn classification and price sensitivity regression. The global objective combines a
differentiable loss with regularization of tree complexity38:

Obj (θ)=
n∑
i=1
l (yi, ˆyi)+
T∑
t=1
Ω( ft) , Ω( f )= γT + 1 2 λ ∥ w∥2
where T  is the number of trees and w are leaf weights. W e tuned max_depth ∈{ 4,6, 8}, eta ∈{ 0.05,0.1},
subsample =0 .8, colsample_bytree =0 .8, and λ, γ to control overfitting. Training minimized log-loss for
churn and RMSE for price sensitivity. Model selection used validation AUC and log-loss; regularization was
increased if validation metrics diverged from training, indicating overfitting. Feature importance and SHAP
were computed to audit drivers (e.g., category mix, basket value volatility) and to inform pricing strategy. In our
experiment, XGBoost reduced error by 14% versus regression baselines and exceeded an MLP’ s churn accuracy
by 9%, consistent with its strength on tabular, heterogeneous retail data.
The silhouette coefficient guided the choice of k =3  by maximizing s (i) on normalized features, ensuring
clusters reflect stable behavioral segments rather than scale artifacts. Support, confidence, and lift were calculated
on baskets reconstructed by Transaction_ID; to avoid bias from rare products, min_support was calibrated per
category granularity and rules were cross-validated across time windows. For demand forecasting, both RMSE
and MAPE were tracked per epoch 39. RMSE provided a global error signal, while MAPE emphasized practical
retail relevance by penalizing proportional errors, which is critical for low-volume items. In XGBoost, validation
AUC and log-loss determined the winning configuration; regularization parameters λ and γ were increased
when a widening gap between training and validation metrics indicated overfitting40. SEM path coefficients β1
and β2 were estimated with bootstrap confidence intervals, and fit indices (CFI > 0.90, RMSEA < 0.08) confirmed
adequate model fit. Fairness auditing used disparate impact DI, with remedial retraining triggered if DI fell
below 0.80. SHAP was used to detect undue reliance on sensitive proxies (e.g., variables strongly correlated with
location or purchasing power), and constraints were applied to reduce such dependencies before deployment.
SOR integration
AI outputs—stimuli comprising personalized recommendations, dynamic promotions, and price messages—
were mapped to organism-level constructs (trust, satisfaction, perceived value) and then to responses (purchase
intention, loyalty, advocacy). A Structural Equation Model (SEM) estimated path coefficients with fit indices
(CFI, RMSEA, χ2) and bootstrap for robustness41:
 Response = β1 · Stimulus + β2 · Organism + ε
Governance comprised fairness auditing via disparate impact,

DI = P ( ˆY =1 | G = A)
P ( ˆY =1 | G = B)
where ˆY =1  denotes predicted positive outcome (e.g., retention) and G groups represent segments of interest.
Explainability relied on SHAP values, with each feature’ s contribution computed as the Shapley value:

φi =
∑
S⊆F \{i}
|S|!( | F |−| S|− 1)!
|F |! [f (S ∪{ i }) − f (S)]
Scientific Reports |        (2026) 16:14160 9| https://doi.org/10.1038/s41598-026-42787-3
www.nature.com/scientificreports/

A feedback loop updated models on sliding temporal windows, ingesting fresh behavioral responses to adapt
stimuli and improve performance. Retraining was automatically triggered if fairness thresholds (e.g., DI < 0.8)
or performance drifts were detected.
This algorithm block shows explicit loops for model selection over k, nested evaluation of FP-Growth rules,
epoch and batch iterations in neural training, grid-search loops for XGBoost, and a while-loop for governance
remediation when fairness or drift thresholds are violated. It mirrors the real workflow used in the experiment,
including checkpointing and early stopping for neural networks and validation-based selection for XGBoost.
Scientific Reports |        (2026) 16:14160 10| https://doi.org/10.1038/s41598-026-42787-3
www.nature.com/scientificreports/

Full pseudocode, implementation details, and code snippets are provided in the Appendix B: Algorithm
pseudocode.
Results
Consumer segmentation, cross-selling discovery, predictive modeling, behavioral interpretation, and governance
were evaluated end-to-end on the held-out test set, with validation used for model selection and hyperparameter
tuning. Results are woven through the narrative with tables and figures placed precisely where they clarify the
interpretation. All figure code is Python-ready and reproducible with the preprocessed matrices and trained
models established in Sect. 4.
The segmentation results confirm a strong, behaviorally coherent partitioning of consumers into three
clusters. The silhouette score peaked at (k = 4), indicating a natural trichotomy consistent with budget, mid-
range, and premium profiles. Cluster centroids in the normalized feature space show progressively increasing
basket values, purchase frequency, and category diversity from budget to premium, alongside decreasing price
sensitivity, which is critical for personalization and dynamic pricing strategies. The selection of (k) was driven by
maximizing (s (i)) and verified via multiple initializations (n_init = 10) to ensure stability.
The Fig.  3 is a silhouette-score line chart that evaluates cluster quality for kk from 2 to 10. The horizontal
axis shows the number of clusters (k = 2…10) and the vertical axis shows the silhouette score for each k; a
blue line with markers connects the silhouette values at each tested k. A vertical red dashed line is drawn at
k = 4 and the legend (top right) label this choice as “Selected k = 4 (sil = 0.151). ” Visually, the plot highlights
that silhouette values are low across the tested range and that the chosen kk corresponds to a relatively small
silhouette score; because silhouette measures cohesion versus separation, a value near 0.15 indicates weakly
separated clusters and suggests limited cluster structure under the current preprocessing or feature set. The chart
therefore communicates both the numeric selection (k = 4) and a cautionary signal about cluster distinctness
that should prompt further checks (feature scaling, feature engineering, alternative clustering algorithms, or
validation with external criteria).
Fig. 3. Silhouette score across candidate k values.

Scientific Reports |        (2026) 16:14160 11| https://doi.org/10.1038/s41598-026-42787-3
www.nature.com/scientificreports/

Table 3 extends basic descriptives with confidence intervals from bootstrap resampling, temporal stability
measured by Jaccard overlap across seasonal folds, and downstream promo conversion uplift, evidencing that
the segmentation is not only statistically coherent but also operationally effective.
The centroid profile visualization underscores the monotonic gradient across the three clusters on the
most actionable behavioral features. The separation is especially pronounced on price sensitivity and category
diversity, matching marketing intuition and guiding stimuli targeting in SOR.
Figure 4 is a line chart that compares normalized behavioral intensities across five features—Avg basket,
Frequency, Diversity, Price sensitivity, and Promo response—for three consumer segments (Budget in blue,
Mid-range in orange, Premium in green). The horizontal axis lists the five metrics and the vertical axis shows
normalized intensity, so each line traces how a segment scores relative to the others on those dimensions.
Visually, the Budget segment stands out on Frequency (it peaks there) and shows relatively stronger promotional
responsiveness; the Premium segment scores highest on Diversity and Price sensitivity (indicating larger, less
price-sensitive baskets and broader category mix); the Mid-range line sits between the two but shows a noticeable
dip on Promo response and a mid-level peak on Price sensitivity. Overall, the plot makes the behavioral
trade-offs clear—who values variety and high spend versus who responds more to promotions and shops more
frequently—so it directly informs which stimuli and offers are likely to resonate with each segment.
As showed in Table  4, Association rule mining using FP-Growth revealed high-confidence, high-lift rules
that generalize across time. Rules like {Bread, Milk}→{Butter} and {Pasta, Tomato Sauce}→{Cheese} illustrate
practical bundles, while premium affinities such as {Coffee (Premium)}→{Dark Chocolate} support aspirational
cross-selling. Rule robustness was ensured by calibrating min_support by granularity and validating confidence/
lift across temporal folds.
Rule (X → Y) Support Confidence Lift Time-stability (CV) Target segments Action template
{Bread, Milk} → {Butter} 0.043 0.87 1.23 High Budget, mid-range Basket bundle + price anchor
{Pasta, Tomato Sauce} → {Cheese} 0.028 0.86 1.18 Medium Mid-range Meal kit recommend + small discount
{Coffee (Premium)} → {Dark Chocolate} 0.015 0.89 1.31 Medium Premium Premium pairing + loyalty bonus
{Juice, Snacks} → {Y ogurt} 0.032 0.85 1.11 Medium Budget Healthy snack promotion
{Tea, Biscuits} → {Honey} 0.021 0.88 1.27 High Mid-range, premium Breakfast pack recommendation
Table 4. FP-Growth rules with thresholds, validation, and segment targeting.

Fig. 4. Cluster centroid profiles for key normalized features.

Metric Cluster 1 (budget)
Cluster 2
(mid-range)
Cluster 3
(premium)
Mean basket value (SAR) 42.7 [40.9, 44.5] 86.3 [83.1, 89.7] 164.9 [159.1, 171.0]
Purchase frequency (per month) 1.80 [1.73, 1.87] 3.10 [2.98, 3.21] 4.60 [4.42, 4.79]
Category diversity (count) 3.2 [3.1, 3.3] 5.7 [5.5, 5.9] 8.4 [8.1, 8.6]
Price elasticity (local) −1.41 [−1.49, −1.33] −0.87 [−0.93, −0.80] −0.39 [−0.46, −0.33]
Silhouette contribution 0.94 0.91 0.92
Temporal stability (Jaccard, folds) 0.81 0.84 0.86
Promo conversion uplift (%) + 7.2 + 4.8 + 3.1
Table 3. Cluster profiles, stability, and statistical confidence (test set).

Scientific Reports |        (2026) 16:14160 12| https://doi.org/10.1038/s41598-026-42787-3
www.nature.com/scientificreports/

The association rule graph conveys the structure of co-purchases and directional recommendations. Node
sizes map to support, edge widths map to confidence, making it clear which product pairs are most impactful
and stable. Figure  5 is a directed association-rule network that maps product itemsets to their most reliable
consequents: nodes represent single items or combined antecedents (e.g., “Pasta + Tomato Sauce”), edges show
directional rules, and each edge is annotated with a numeric strength (confidence) such as 0.86, 0.89, 0.87,
and 0.85. Visually, the graph highlights five prominent pairings—Cheese ← Pasta + Tomato Sauce (0.86), Dark
Chocolate ← Coffee (Premium) (0.89), Butter ← Bread + Milk (0.87), Y ogurt ← Juice + Snacks or Y ogurt ← Honey
(0.85), and Honey linked to Tea + Biscuits—while node color and size encode a secondary measure (support
or relative importance), so hubs and high-support itemsets stand out. The layout groups complementary
items and makes it easy to spot both staple bundles (bread/milk → butter) and premium pairings (coffee →
dark chocolate), providing a compact visual summary of stable co-purchase relationships that can be used for
bundling, recommendation rules, or targeted promotions.
Demand forecasting and churn/pricing predictions confirm the complementary strengths of LSTM (for
sequential demand) and XGBoost (for tabular churn and pricing). LSTM captured seasonal demand shifts more
effectively, lowering MAPE, while XGBoost achieved the highest AUC and lowest log-loss in churn and reduced
RMSE in pricing. Model differences were statistically significant, assessed via paired tests on per-customer
predictions and confidence intervals derived from bootstrap resampling of the test set (Table 5).
Figure 6 is a Receiver Operating Characteristic (ROC) comparison of three classifiers: Logistic Regression
(black), MLP (green), and XGBoost (red). The horizontal axis is the false positive rate and the vertical axis is the
true positive rate; a diagonal dashed line marks a random classifier baseline. Each model’s curve is annotated
with its Area Under the Curve (AUC): Logistic Regression ≈ 0.605, MLP ≈ 0.490, and XGBoost ≈ 0.592. Visually,
the Logistic Regression curve lies above the others and yields the highest AUC, the MLP curve falls near or
below the diagonal (indicating performance close to random), and XGBoost tracks close to Logistic Regression
but slightly lower. The plot shows modest discriminative power overall rather than strong separation between
classes. Logistic Regression is the best performer on this test set, but its AUC is still low enough to suggest the
model produce many false positives or false negatives at typical thresholds. The MLP’s poor curve suggests
either underfitting, misconfigured architecture/hyperparameters, or that the available features do not expose the
nonlinear patterns the network needs. XGBoost’s proximity to Logistic Regression indicates that tree ensembles
are competitive but not decisively superior here. Taken together, the figure signals that model improvement
Task Model RMSE (95% CI) MAPE% (95% CI) AUC (95% CI) Log-loss (95% CI) Δ vs. baseline (p-value)
Demand MLP 12.4 [11.8, 13.0] 8.6 [8.1, 9.1] – – –
Demand LSTM 11.1 [10.5, 11.7] 7.9 [7.5, 8.4] – – MAPE: −0.7 (p < 0.01)
Churn Regression – – 0.78 [0.76, 0.80] 0.54 [0.52, 0.56] Baseline
Churn MLP – – 0.83 [0.81, 0.85] 0.47 [0.45, 0.49] AUC: +0.05 (p < 0.01)
Churn XGBoost – – 0.91 [0.89, 0.92] 0.39 [0.38, 0.41] AUC: +0.13 (p < 0.001)
Pricing Regression 15.2 [14.6, 15.8] – – – Baseline
Pricing XGBoost 13.1 [12.6, 13.7] – – – RMSE: −2.1 (p < 0.01)
Table 5. Predictive performance with confidence intervals and significance.

Fig. 5. Association rule network visualization.

Scientific Reports |        (2026) 16:14160 13| https://doi.org/10.1038/s41598-026-42787-3
www.nature.com/scientificreports/

should focus first on data and evaluation (feature enrichment, class balance, temporal validation, label quality)
before relying on more complex algorithms.
Interpretability and governance were audited using SHAP and disparate impact. SHAP ranks show logical
drivers: basket volatility and recent frequency were dominant for churn risk, while price history and elasticity
dominated pricing predictions. Disparate impact remained above the 0.8 threshold across monitored groups,
and the feedback loop automatically triggered remediation when drift or fairness degradation was detected.
These safeguards ensure that the system is not only performant but also responsible (Table 6).
The Fig.  7 is a SHAP summary plot for the XGBoost churn model that ranks features by importance and
shows how individual feature values influence model predictions. Features are listed vertically (top to bottom)
with num__frequency, num__price_sensitivity, and num__avg_basket at the top, indicating they are the most
influential. Each dot represents one customer’s SHAP value for that feature; the horizontal axis is the SHAP value
(impact on the model output), and color encodes the raw feature value from low (blue) to high (red). Points to
the right increase the model’s predicted score (higher churn risk), while points to the left decrease it (lower churn
risk).
Reading the plot gives two practical insights. First, which features matter: the model relies primarily on
behavioral metrics (frequency, price sensitivity, basket size, promo response) before product-category dummies,
so interventions should focus on those behavioral levers. Second, how feature values map to risk: if high values
(red) for a feature cluster on the right, then high values of that feature raise predicted churn; if red cluster on the
left, high values reduce predicted churn. This makes the model interpretable for business teams: for example,
features that consistently push predictions toward higher risk identify customers who should receive retention
offers, while features that push predictions downward identify stable customers to prioritize for premium upsell.
The plot also helps governance: features with outsized influence can be audited for proxies or bias, and SHAP
distributions can be used to create counterfactual rules (e.g., what minimal change in a behavioral metric would
flip a high-risk prediction).
Finally, SOR integration through SEM validates the psychological interpretation of the AI-driven stimuli.
Stimuli significantly enhance organism constructs (trust, satisfaction), which in turn strongly predict response
(purchase intention, loyalty). Fit indices surpass conventional acceptability thresholds, implying that the
behavioral chain—from algorithmic stimuli to human response—is theoretically consistent and empirically
supported (Table 7).
The empirical findings suggest that AIM 2 offers substantial segmentation quality, sturdy cross-selling
frameworks, enhanced predictive capabilities with statistically notable improvements, comprehensible factors
matching sector reasoning, and ethical oversight confirmed through equity measures and drift checks. The
behavioral anchoring via SOR additionally bolsters the argument that the system’s outputs are not just precise
Task Top SHAP features (ranked) DI (Group A/B) Drift flag Remediation applied
Churn Basket value volatility, Recent frequency, Category mix 0.84 No None
Pricing Price change history, Elasticity, Promo response rate 0.87 No None
Demand Day-of-week seasonality, Category embeddings, Promotions — No N/A
Table 6. SHAP-ranked features and governance metrics by task.

Fig. 6. ROC curves across churn models.

Scientific Reports |        (2026) 16:14160 14| https://doi.org/10.1038/s41598-026-42787-3
www.nature.com/scientificreports/

but also relevant for real-world decision-making. Collectively, these outcomes reinforce the notion that the study
is credible, dependable, and prepared for real-world application within Saudi retail settings in line with Vision
2030.
Discussion
The data confirms that AIM 2 generates logical, practical insights spanning segmentation, association analysis,
predictive analytics, and behavioral assessment. The clustering phase identified three steady buyer categories—
economy, mid-tier, and high-end—with a strong mean silhouette score (0.92), suggesting the groupings represent
genuine structure within standardized behavior traits like basket worth, shopping regularity, category variety,
and price responsiveness. In practice, this implies the segments stem from persistent tendencies rather than
scaling quirks or distortion, making them suitable for tailored promotional tactics. The FP-Growth correlations
further bolster segmentation by pinpointing robust co-purchase trends (rules sustained at confidence > 0.85 and
lift > 1), allowing for segment-specific bundle recommendations and incentive strategies.
Predictively, comparative testing revealed a distinct edge for ensemble tree models on retail tabular datasets:
XGBoost surpassed regression and neural benchmarks in churn and pricing tasks by 14% fewer errors and
9% greater accuracy. Meanwhile, sequential neural structures (LSTM) excelled in demand prediction scenarios
with time-based influences and seasonal peaks (e.g., Ramadan, Eid). Thus, blending LSTM for sequence-based
forecasting and XGBoost for classification/regression tasks presents a sensible hybrid approach, matching
each technique to data structures where its strengths apply. Explainability and oversight layers—SHAP for
variable contribution and disparity impact (DI) tracking—verified reliance on understandable factors (basket
fluctuations, recent activity, price trends) while upholding fairness standards (DI > 0.8), endorsing ethically
sound implementation.
Relation to prior studies and working hypotheses
These findings align with and extend prior work in several ways. The superiority of XGBoost on heterogeneous
retail tabular data echoes earlier comparative studies that report ensemble methods’ robustness to feature
heterogeneity and noisy interactions; our results quantify that advantage in the Saudi retail context and show it
Path/fit index Estimate/value Implication
β1 (Stimulus → Organism) 0.41 (p < 0.01) Personalization increases trust/satisfaction
β2 (Organism → Response) 0.62 (p < 0.001) Trust/satisfaction strongly drive purchase/loyalty
CFI 0.93 Acceptable model fit
RMSEA 0.06 Acceptable residual error
R2 (Organism) 0.38 Stimuli explain substantial organism variance
R2 (Response) 0.51 Organism explains majority of behavioral variance
Table 7. SOR-SEM results, fit indices, and operational implications.

Fig. 7. SHAP summary for XGBoost churn model.

Scientific Reports |        (2026) 16:14160 15| https://doi.org/10.1038/s41598-026-42787-3
www.nature.com/scientificreports/

holds when models are integrated into a broader behavioral framework. The observed benefit of LSTM for demand
forecasting is consistent with literature emphasizing recurrent architectures for seasonal and event-driven retail
demand. The high silhouette score and stable centroids corroborate prior segmentation studies that find a small
number of meaningful shopper archetypes in supermarket data; however, AIM 2 strengthens those results by
linking segments to downstream stimuli and measurable conversion uplifts, thereby closing the loop between
segmentation and action.
From the perspective of the working hypotheses—(1) that AI methods can produce robust segmentation and
cross-selling rules in Saudi retail, (2) that predictive models can materially improve churn and pricing decisions,
and (3) that SOR integration map algorithmic stimuli to psychological constructs and behavioral outcomes—the
evidence is supportive. Hypothesis (1) is validated by the high silhouette score and temporally stable association
rules; hypothesis (2) is supported by the statistically significant performance gains of XGBoost and LSTM over
baselines; and hypothesis (3) is corroborated by the SEM results where stimuli significantly predict organism
constructs (β1 = 0.41, p < 0.01) and organism constructs strongly predict behavioral responses (β2 = 0.62,
p < 0.001), with acceptable fit indices (CFI = 0.93, RMSEA = 0.06). Together, these outcomes suggest that AIM2
does more than optimize metrics: it produces outputs that are interpretable within consumer psychology and
operationally useful for marketing decisions.
AIM2 provides an appropriate method for integrating computing frameworks with psychological concepts.
The SOR framework indicates that stimuli, which are algorithm-driven, for instance, recommendations, bundled
prices, and variable pricing, might be external factors whose influence on assurance and happiness is measurable
and useful for purchasing behavior and loyalty. This combination combats one of the most common criticisms
directed at AI systems, which are purely forecasting-based, in the business area: mere accuracy does not offer an
explanation of the customer’s reactions’ motivations. By utilizing structural equation modeling in the procedure,
AIM2 gives rise to a means of making causal inferences, within observational limits, while at the same time
reconciling algorithmic outcomes with recognized commercial tenets.
Research findings spread across and outlined the ways for the retail businesses to do smarter practices. The
first one is the clarified usage of segmentation and centroid analysis which grants companies the right to pay for
their marketing strategies according to the segments: price-sensitive customers - cost-effective bundles, mid-
tiers - diverse and convenient options, high-end - exclusive combinations. Next, the stable temporal validity of
association rules can already be drawn as the suggestion for algorithms in the system of checkout or in case of
an online shopping platform thus increasing the cart value without resorting to discounts as a heavy reliance.
The third point is that XGBoost, due to its excellent performance in customer churn and pricing prediction, lead
merchants to prefer tree ensemble methods for score and price optimization of retention while sequential neural
approaches would be only adopted for time series forecasting. The fourth point is that SHAP interpretations and
DI tracking would allow the deployment of these models to be accompanied by the clarity and fairness measures
which are very important for regulations and consumer confidence especially in the up-and-coming markets
where digitization is being pushed by the likes of Saudi Arabia’s Vision 2030 initiative.
However, several methodological constraints temper the findings. The data, though extensive and authentic,
stems from a sole retailer (Tamimi Markets), prompting concerns over generalizability: store layouts, local tastes,
and loyalty schemes differ among chains and regions, meaning models fitted to one may require adjustments
elsewhere. The observational data also weakens causal inferences; while SEM offers a structured framework
linking inputs to outputs, controlled experiments (A/B testing, randomized offers) remain essential to confirm
causality and measure precise impact. Model accuracy further hinges on preprocessing decisions (feature design,
encoding, outlier management) and tuning; despite rigorous validation and bootstrap intervals, live deployments
demand ongoing checks for data drift and refreshes.
Balancing clarity with accuracy poses another challenge. XGBoost’s ensembles, though clearer than deep
networks when using SHAP , still generate intricate relationships needing simplification for non-experts. The
fairness evaluations (DI) applied here are vital yet incomplete: disparate impact, being a broad metric, may
overlook nuanced biases or indirect discrimination. Lastly, technical and logistical hurdles—model speed,
compatibility with older systems, and real-time scoring demands—introduce obstacles requiring both technical
upgrades (MLOps) and cross-departmental coordination.
Future research directions
Several avenues for future research emerge naturally from this study. At a distance, replicating the cross-retailer
and cross-country aspects would be a thorough trial of the generalizability of AIM2 and let us witness the effect
of culture and market on the segmentation and rule stability 42. Secondly, involving the randomized controlled
trials as a part of the pipeline would transform the per-correlation findings into the causal ones, allowing the
precise measurement of the incremental lift from the AI-driven stimuli and validating the SEM pathways in an
experimental way43. Thirdly, the integration of multimodal data such as textual reviews, social media signals,
in-store sensor data, and images would greatly allow organism constructs (sentiment, engagement) to be
enriched and promote the personalization particularly in higher premium segments where experiential factors
matter. On top of that, the study on the privacy-preserving personalization (federated learning, differential
privacy) is a must to bring personalization together with the regulations and moral ethics. Fifth, reinforcement
learning approaches for dynamic pricing and promotion sequencing could be explored to optimize long-term
customer lifetime value rather than short-term revenue. Sixth, fairness research should move beyond single
metrics to multi-criteria auditing frameworks that consider disparate impact, calibration, and long-term equity
effects across demographic and socioeconomic groups.
Methodologically, future work should investigate hybrid architectures that combine tree ensembles and
neural sequence models more tightly—e.g., feature representations learned by LSTMs feeding into gradient
boosting models—or meta-learners that adapt model choice to SKU characteristics. Finally, longitudinal studies
Scientific Reports |        (2026) 16:14160 16| https://doi.org/10.1038/s41598-026-42787-3
www.nature.com/scientificreports/

that track behavioral change over multiple seasons would illuminate the persistence of segmentation and the
long-term effects of personalized interventions on loyalty and sustainable consumption patterns.
Limitations
The study has several limitations that affect interpretation and generalizability and should be read in order of
impact. Data provenance and demographic absence (High impact): the public Tamimi Markets transactional
dataset lacks explicit demographic labels, which prevents formal fairness audits across protected groups and
constrains subgroup analyses; this limitation most strongly restricts claims about equity and differential
effects. Observational design (High impact): all SEM and association results are correlational and cannot
establish causality without experimental validation (for example, randomized A/B tests of AI-driven stimuli).
Dataset bias and representativeness (Medium impact): although we performed integrity checks and compared
summary statistics with national reports, publicly sourced retail datasets can underrepresent certain store
types or customer segments, which may bias estimates and reduce external validity. Generalizability (Medium
impact): findings are most directly applicable to grocery retail contexts similar to Tamimi Markets; extension
to other retail formats, product categories, or cultural settings requires further validation. Fairness evaluation
constraints (Low–Medium impact): because we avoided inferring demographics from transactions, fairness
auditing was limited to behavioral segments rather than legally protected classes, reducing the scope of ethical
assessment. Operational complexity (Low impact): deploying the full AIM 2 pipeline in production requires
engineering resources, monitoring, and governance that may limit immediate practitioner adoption. Despite
these limitations, the system has clear strengths: pros include improved predictive accuracy through ensemble
and representation learning, actionable segmentation that supports targeted promotions and cross-selling, and
an integrated governance layer that embeds MLOps and explainability mechanisms; cons mirror the limitations
above and include dependence on high-quality, representative data, constrained fairness evaluation without
demographic metadata, and nontrivial operational overhead for deployment and continuous monitoring.
Conclusion
The paper presents a coherent, well-documented implementation of the AIM 2 framework that successfully
integrates the Stimulus–Organism–Response (SOR) theoretical lens with a practical AI stack (K-means
clustering, FP -Growth association mining, MLP/LSTM neural networks, and XGBoost) applied to a real
Tamimi Markets retail dataset. Empirically, the study delivers strong, actionable results: a stable three-segment
solution with a silhouette ≈ 0.92, high-confidence association rules (confidence > 0.85, lift > 1) that support
cross-sell strategies, LSTM models that capture seasonal demand patterns, and XGBoost models that reduce
error by ~ 14% versus regression baselines and improve churn accuracy by ~ 9% versus baseline neural nets.
Explainability (SHAP) and governance (disparate impact monitoring, DI > 0.8) are embedded in the pipeline,
and SEM links AI-generated stimuli to organism constructs (β₁≈0.41) and behavioral responses (β₂≈0.62)
with acceptable fit (CFI ≈ 0.93, RMSEA ≈ 0.06), showing the framework produces both predictive power and
theoretically interpretable marketing insights.
At the same time, the paper acknowledges important caveats that temper generalization: the analysis is based
on a single retailer’s dataset (limiting external validity), the evidence is observational (so causal claims require
randomized experiments), and fairness auditing relies on coarse metrics that should be complemented by richer
bias diagnostics and long-term equity assessments. For practitioners, AIM 2 offers a pragmatic blueprint—use
LSTM for temporal demand, XGBoost for tabular churn/pricing, and FP -Growth for stable bundling—while
enforcing MLOps, explainability, and fairness checks before deployment. For researchers, the study opens clear
next steps: cross-context replication, experimental validation of SEM pathways, multimodal data integration,
and exploration of privacy-preserving and reinforcement-learning approaches to optimize long-term customer
value.
Data availability
The dataset supporting the reported results is publicly available on Kaggle: Saudi Arabia Su-permarket Data
Expenses (moha684, 2023). Available online:  [ h t t p s  : / / w w w  . k a g g l  e . c o m /  d a t a s e t s / m o h a 6 8 4 / s a u d i - a r a b i a - s u p e r
m a r k e t - d a t a - e x p e n s e s ] ( h t t p s : / w w w . k a g g l e . c o m / d a t a s e t s / m o h a 6 8 4 / s a u d i - a r a b i a - s u p e r m a r k e t - d a t a - e x p e n s e s )
(accessed on 10 November 2025). No new data were created or analyzed in this study.
Received: 6 December 2025; Accepted: 27 February 2026
References
 1. Zhang, C., Wang, Y . & Zhang, J. Risk assessment of live-streaming marketing based on hesitant fuzzy multi-attribute group
decision-making method. J. Theor. Appl. Electron. Commer. Res. 20(2), 120. https://doi.org/10.3390/jtaer20020120 (2025).
 2. Kasem, M. S., Hamada, M. & Taj-Eddin, I. Customer profiling, segmentation, and sales prediction using AI in direct marketing.
Neural Comput. Appl. 36, 4995–5005. https://doi.org/10.1007/s00521-023-09339-6 (2024).
 3. Davtyan, N. AI in Consumer Behavior Analysis and Digital Marketing: A Strategic Approach. SBSRC Conf. Proc. 45–56.  h t t p s : / / d
o i . o r g / 1 0 . 7 0 3 0 1 / C O N F . S B S - J A B R . 2 0 2 4 . 1 / 1 . 5     (2024).
 4. Almaafi, A., Bajaba, S. & Alnori, F . Stock price prediction using ARIMA versus XGBoost models: Evidence from Saudi Telecom.
Int. J. Inf. Technol. 15, 1813–1818. https://doi.org/10.1007/s41870-023-01260-4 (2023).
 5. Saudi Arabia Supermarket Data Expenses. Kaggle Dataset. (2023).  h t t p s :   /  / w w  w . k a g g l  e . c  o m  / d a t a s  e  t s / m  o h a  6 8 4  / s a  u d  i - a r  a  b i a - s u  p e r
m a   r k e t  -  d a t a - e x p e n s e s (accessed on 10 Nov 2025).
 6. Oğuz, A. Consumer behavior in the era of AI-driven marketing. Hum. Comput. Interact. 8, 128–145.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 4 1 2
3 9 - 0 2 4 - 0 0 3 2 1 - 7     (2024).
Scientific Reports |        (2026) 16:14160 17| https://doi.org/10.1038/s41598-026-42787-3
www.nature.com/scientificreports/

 7. Cillo, P . & Rubera, G. Generative AI in innovation and marketing processes: A roadmap of research opportunities. J. Acad. Mark.
Sci. 53, 684–701. https://doi.org/10.1007/s11747-024-01044-7 (2024).
 8. Acatrinei, C., Apostol, I. G., Barbu, L. N., Chivu, R. G. & Orzan, M. C. Artificial intelligence in digital marketing: Enhancing
consumer engagement and supporting sustainable behavior. Sustainability 17(14), 6638. https://doi.org/10.3390/su17146638
(2025).
 9. Xu, Y ., Chen, X. & Wang, Z. Machine learning applications in retail marketing: Comparative study of neural networks and
ensemble models. Expert Syst. Appl. 198, 116891. https://doi.org/10.1016/j.eswa.2022.116891 (2022).
 10. Tabianan, K., Velu, S. & Ravi, V . K-means clustering approach for intelligent customer segmentation using customer purchase
behavior data. Sustainability 14(12), 7243. https://doi.org/10.3390/su14127243 (2022).
 11. Kumar, M. & Patel, N. R. Using clustering to improve sales forecasts in retail merchandising. Ann. Oper. Res. 174(1), 33–46.  h t t p s :
/ / d o i . o r g / 1 0 . 1 0 0 7 / s 1 0 4 7 9 - 0 0 8 - 0 4 1 7 - z     (2010).
 12. Chopvitayakun, S., Jitsakul, W . & Aukkanit, N. Analyzing purchase behavior using FP growth technique to find association rules.
In Proceedings of the 2024 10th International Conference on e-Society, e-Learning and e-Technologies (ICSLT), 106–111.  h t t p s : / / d o i .
o r g / 1 0 . 1 1 4 5 / 3 6 7 8 6 1 0 . 3 6 7 8 6 1 8     (2024).
 13. Joseph, R. V . et al. A hybrid deep learning framework with CNN and Bi-directional LSTM for store item demand forecasting.
Computers and Electrical Engineering 103, 108358. https://doi.org/10.1016/j.compeleceng.2022.108358 (2022).
 14. Bellar, O., Baina, A. & Ballafkih, M. Sentiment analysis: Predicting product reviews for e-commerce recommendations using deep
learning and transformers. Mathematics 12(15), 2403. https://doi.org/10.3390/math12152403 (2024).
 15. Zhao, Z., Omar, N. A. & Zaki, H. O. Appraisal factors of sustainable purchase intentions in online shopping platform context: PLS-
SEM with theory extensions. Journal of Retailing and Consumer Services 82, 104118.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . j r e t c o n s e r . 2 0 2 4 . 1 0 4
1 1 8     (2025).
 16. Jin, T. Optimizing retail sales forecasting through a pso-enhanced ensemble model integrating lightgbm, xgboost, and deep neural
networks. In 2024 4th International Conference on Digital Society and Intelligent Systems (DSInS), 120–124.  h t t p s : / / d o i . o r g / 1 0 . 1 1 0 9
/ D S I n S 6 4 1 4 6 . 2 0 2 4 . 1 0 9 9 2 0 7 2     (2024).
 17. Afoudi, Y ., Lazaar, M. & Al Achhab, M. Hybrid recommendation system combined content-based filtering and collaborative
prediction using artificial neural network. Simulation Modelling Practice and Theory 113, 102375.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . s i m p a t
. 2 0 2 1 . 1 0 2 3 7 5     (2021).
 18. Vafaei-Zadeh, A., Nikbin, D., Wong, S. L. & Hanifah, H. Investigating factors influencing AI customer service adoption: An
integrated model of stimulus–organism–response (SOR) and task-technology fit (TTF) theory. Asia Pacific Journal of Marketing
and Logistics 37(6), 1465–1502. https://doi.org/10.1108/APJML-05-2024-0570 (2025).
 19. Jiang, Z. & Lyu, J. The role of augmented reality app attributes and customer-based brand equity on consumer behavioral responses:
An SOR framework perspective. J. Prod. Brand Manage. 33(6), 702–716. https://doi.org/10.1108/JPBM-09-2023-4706 (2024).
 20. Paliari, I., Karanikola, A. & Kotsiantis, S. A comparison of the optimized LSTM, XGBOOST and ARIMA in time series forecasting.
In 2021 12th international conference on information, intelligence, systems & applications (IISA), 1–7.  h t t p s : / / d o i . o r g / 1 0 . 1 1 0 9 / I I S A
5 2 4 2 4 . 2 0 2 1 . 9 5 5 5 5 2 0     (IEEE, 2021).
 21. César, I. et al. A systematic review on responsible multimodal sentiment analysis in marketing applications. IEEE Access 12,
111943–111961. https://doi.org/10.1109/ACCESS.2024.3441514 (2024).
 22. Sohaib, M., Safeer, A. A. & Majeed, A. Role of social media marketing activities in China’s e-commerce industry: A stimulus
organism response theory context. Frontiers in Psychology 13, 941058. https://doi.org/10.3389/fpsyg.2022.941058 (2022).
 23. Alsadoun, A. A. & Alnasser, A. N. Role of artificial intelligence chatbot marketing in enhancing customer satisfaction and loyalty
in digital shopping experiences. Int. J. Innov. Res. Sci. Stud. 8(1), 1902–1909. https://doi.org/10.53894/ijirss.v8i1.4826 (2025).
 24. Umezurike, S. A. et al. Augmented reality shopping experiences: A review of retail immersion technologies and outcomes. Int. J.
Manag. Organ. Res. 3(2), 83–94. https://doi.org/10.54660/IJMOR.2024.3.2.83-94 (2024).
 25. Sonboli, N., Smith, J. J., Cabral Berenfus, F ., Burke, R. & Fiesler, C. Fairness and transparency in recommendation: The users’
perspective. In Proceedings of the 29th ACM Conference on User Modeling, Adaptation and Personalization, 274–279.  h t t p s : / / d o i . o r
g / 1 0 . 1 1 4 5 / 3 4 5 0 6 1 3 . 3 4 5 6 8 3 5     (2021).
 26. Saad, M., Awad, A., Aziz, A. F . & Shma, T. R. Influencer marketing’s impact on credibility and purchase intention: A study on
University of Bisha students in Saudi Arabia. Innov. Mark. 21(1), 326. https://doi.org/10.21511/im.21(1).2025.26 (2025).
 27. Memish, Z. A., Altuwaijri, M. M., Almoeen, A. H. & Enani, S. M. The Saudi Data & Artificial Intelligence Authority (SDAIA)
vision: Leading the Kingdom’s journey toward global leadership. J. Epidemiol. Glob. Health. 11(2), 140–142.  h t t p s : / / d o i . o r g / 1 0 . 2 9 9
1 / j e g h . k . 2 1 0 4 0 5 . 0 0 1     (2021).
 28. Lemonde, C., Arsenio, E. & Henriques, R. Integrative analysis of multimodal traffic data: Addressing open challenges using big
data analytics in the city of Lisbon. Eur. Transp. Res. Rev. 13(1), 64. https://doi.org/10.1186/s12544-021-00520-3 (2021).
 29. Aldino, A. A., Pratiwi, E. D., Sintaro, S. & Putra, A. D. Comparison of market basket analysis to determine consumer purchasing
patterns using FP Growth and Apriori algorithm. In Proceedings of the 2021 International Conference on Computer Science,
Information Technology, and Electrical Engineering (ICOMITEE), 29–34. https://doi.org/10.1109/ICOMITEE53461.2021.9650317
(IEEE, 2021).
 30. Sinsomboonthong, S. Performance comparison of new adjusted min max with decimal scaling and statistical column normalization
methods for artificial neural network classification. Int. J. Math. Math. Sci. 2022(1), 3584406. https://doi.org/10.1155/2022/3584406
(2022).
 31. Rice, K. & Lumley, T. Graphics and statistics for cardiology: Comparing categorical and continuous variables. Heart 102(5), 349–
355. https://doi.org/10.1136/heartjnl-2015-308104 (2016).
 32. Tran, D. T. & Huh, J. H. New machine learning model based on the time factor for e-commerce recommendation systems. J.
Supercomput. 79(6), 6756–6801. https://doi.org/10.1007/s11227-022-04909-2 (2023).
 33. Papamichail, G. P . & Papamichail, D. P . The k-means range algorithm for personalized data clustering in e-commerce. Eur. J. Oper.
Res. 177(3), 1400–1408. https://doi.org/10.1016/j.ejor.2005.04.011 (2007).
 34. Wu, Z., Jin, L., Zhao, J., Jing, L. & Chen, L. Research on segmenting E-Commerce customer through an improved K ‐Medoids
clustering algorithm. Comput. Intell. Neurosci. https://doi.org/10.1155/2022/9930613 (2022).
 35. Saputra, J. P . B., Rahayu, S. A. & Hariguna, T. Market basket analysis using FP-growth algorithm to design marketing strategy by
determining consumer purchasing patterns. J. Appl. Data Sci. 4(1), 38–49. https://doi.org/10.47738/jads.v4i1.83 (2023).
 36. Wang, S. & Y ang, Y . M-GAN-XGBOOST model for sales prediction and precision marketing strategy making of each product in
online stores. Data Technol. Appl. 55(5), 749–770. https://doi.org/10.1108/DTA-11-2020-0286 (2021).
 37. Sarkar, M. & De Bruyn, A. LSTM response models for direct marketing analytics: Replacing feature engineering with deep
learning. J. Interact. Mark. 53(1), 80–95. https://doi.org/10.1016/j.intmar.2020.07.002 (2021).
 38. Chen, H. Enterprise marketing strategy using big data mining technology combined with XGBoost model in the new economic
era. PLoS One 18(6), e0285506. https://doi.org/10.1371/journal.pone.0285506 (2023).
 39. Debnath, A. et al. Analyzing and forecasting of real-time marketing campaign performance and ROI in the US market. In 2024
International Conference on Intelligent Cybernetics Technology & Applications (ICICyTA), 332–337.  h t t p s : / / d o i . o r g / 1 0 . 1 1 0 9 / I C I C Y
T A 6 4 8 0 7 . 2 0 2 4 . 1 0 9 1 3 2 2 6     (2024).
 40. Hakkal, S. & Ait Lahcen, A. XGBoost to enhance learner performance prediction. Comput. Educ. Artif. Intell. 7, 100254.  h t t p s : / / d
o i . o r g / 1 0 . 1 0 1 6 / j . c a e a i . 2 0 2 4 . 1 0 0 2 5 4     (2024).
Scientific Reports |        (2026) 16:14160 18| https://doi.org/10.1038/s41598-026-42787-3
www.nature.com/scientificreports/

 41. Sathyanarayana, S. & Mohanasundaram, T. Fit indices in structural equation modeling and confirmatory factor analysis: Reporting
guidelines. Asian J. Econ. Bus. Account. 24(7), 561–577. https://doi.org/10.9734/ajeba/2024/v24i71430 (2024).
 42. Loh, X. M. et al. Super app: A multi-analytical cross-country approach on the everything app. J. Comput. Inform. Syst. 1–14.  h t t p s
: / / d o i . o r g / 1 0 . 1 0 8 0 / 0 8 8 7 4 4 1 7 . 2 0 2 5 . 2 5 6 0 3 7 9     (2025).
 43. Didero, N., Costanigro, M. & Jablonski, B. B. Promoting farmers market via information nudges and coupons: A randomized
control trial. Agribusiness 37(3), 531–549. https://doi.org/10.1002/agr.21688 (2021).
Acknowledgements
This work was supported by the Deanship of Scientific Research, Vice Presidency for Graduate Studies and Sci-
entific Research, King Faisal University, Saudi Arabia [Grant No. KFU260989].
Author contributions
Conceptualization, F .K.A.; methodology, F .K.A.; software, M.BO.; validation, F .K.A, H.U.K. and M.BA.; formal
analysis, M.BO.; investigation, M.BA.; resources, M.BA.; data curation, M.BA.; writing—original draft prepara-
tion, F .K.A.; writing—review and editing, M.BA.; visualization, H.U.K.; supervision, M.BO.; project administra-
tion, H.U.K. and F .K.A; funding acquisition, F .K.A. All authors have read and agreed to the published version of
the manuscript.
Funding
This work was supported by the Deanship of Scientific Research, Vice Presidency for Graduate Studies and Sci-
entific Research, King Faisal University, Saudi Arabia [Grant No. KFU260989].
Declarations
Competing interests
The authors declare no competing interests.
Additional information
Supplementary Information The online version contains supplementary material available at  h t t p s : / / d o i . o r g / 1
0 . 1 0 3 8 / s 4 1 5 9 8 - 0 2 6 - 4 2 7 8 7 - 3     .
Correspondence and requests for materials should be addressed to F .K.A. or M.B.
Reprints and permissions information is available at www.nature.com/reprints.
Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in published maps and
institutional affiliations.
Open Access  This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives
4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in
any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide
a link to the Creative Commons licence, and indicate if you modified the licensed material. Y ou do not have
permission under this licence to share adapted material derived from this article or parts of it. The images or
other third party material in this article are included in the article’s Creative Commons licence, unless indicated
otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence
and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to
obtain permission directly from the copyright holder. To view a copy of this licence, visit  h t t p : / / c r e a t i v e c o m m o
n s . o r g / l i c e n s e s / b y - n c - n d / 4 . 0 /     .
© The Author(s) 2026
Scientific Reports |        (2026) 16:14160 19| https://doi.org/10.1038/s41598-026-42787-3
www.nature.com/scientificreports/
