---
title: Machine Learning–Driven Brand Loyalty Analytics Framework for Predicting Customer Retention and
  Enhancing Personalized Engagement in the Culinary Industry
url: https://doi.org/10.71086/iajse/v13i3/iajse13116
category: brand
subcategory: framework
date: 2026-09
venue: International Academic Journal of Science and Engineering
authors:
- Andrea Varghese
- Dr. A. Shanthi
- Dr.Umesh U
source: openalex-oa
pdf_url: https://iaiest.com/iaj/index.php/IAJSE/article/download/IAJSE13116/3020
pages: 13
chars: 49999
fetched_at: '2026-11-08T18:56:55+00:00'
kb_version: 1
---

# Machine Learning–Driven Brand Loyalty Analytics Framework for Predicting Customer Retention and Enhancing Personalized Engagement in the Culinary Industry

300
DOI: 10.71086/IAJSE/V13I3/IAJSE13116
Received: 13 June, 2026/Revised: 15 July 2026/Accepted: 21 August 2026/Published: 15 September 2026

Machine Learning–Driven Brand Loyalty Analytics Framework for
Predicting Customer Retention and Enhancing Personalized
Engagement in the Culinary Industry

Andrea Varghese a*, Dr.A. Shanthi b, Dr.U. Umesh c, V. Vijayaganth d,
Dontamsetti Nageswarrao  e, K. Babu f

a* Ph.D Scholar, Department  of Commerce, KPR College of Arts Science and Research, Coimbatore , Tamil Nadu,
India. E-mail: andreavarghese@kprcas.ac.in , Orcid: https://orcid.org/0009 -0004-9907-7979
b Associate Professor and Head, Department  of Commerce, KPR  College of Arts Science and Research,
Coimbatore , Tamil Nadu, India . E-mail: shanthi.a@kprcas.ac.in , Orcid: https://orcid.org/0000 -0003-0275-6656
c Professor, Department of Commerce, Amal College of Advanced Studies (Autonomous), Aided by Gov ernment of
Kerala & affiliated with Uty.  of Calicut, Nilambur, Kerala , India. E-mail: umesh.tripunithura@gmail.com,
Orcid: https://orcid.org/0000 -0002-5380-4833
d Assistant Professor, Department of Artificial Intelligence and Data Science,  KPR Institute of Engineering and
Technology, Coimbatore , Tamil Nadu, India. E-mail: kv.vijayaganth@gmail.com ,
Orcid: https://orcid.org/ 0000-0003-1096-6354
e Assistant Professor, Department of CSE, CMR Technical Campus, Hyderabad, Telangana, India .
E-mail: nageswarraodontamsetti@gmail.com , Orcid: https://orcid.org/ 0009-0006-5850-4828
f Department of Computational Intelligence, School of Computing, Faculty of Engineering and Technology, SRM
Institute of Science and Technology, Kattankulathur , Tamil Nadu, India .
E-mail: babukumarit@gmail.com , Orcid: https://orcid.org/0000 -0003-2574-5052

Abstract
Due to the fast adoption of various practices including digital ordering, loyalty programs, mobile apps, and social
media in the culinary industry, there is an abundance of customer data available to marketers but at the same time,
there are difficulties in detecting customers' risks of retention and providing efficient personalized engagement. In this
regard, the current research presents a Machine Learning-Driven Brand Loyalty Analytics Framework, which involves
the analysis of transactional behavior, loy alty program engagement, digital engagement, customer sentiment, and
customer profile for the prediction of retention and provision of relevant engagement approaches. For this purpose,
the current research uses the dataset, which includes 5,000 customer re cords gathered within one year. Data
preprocessing includes the removal of duplicates, dealing with missing values, detecting outliers, data normalization,
and feature transformation, followed by the development of five machine learning models: Random Forest, XGBoost,
LightGBM, CatBoost, and Deep Neural Network. XGBoost outperformed other algorithms by achieving an accuracy
of 94.3%, precision of 93.7%, recall of 92.8%, F1 score of 93.2%, and AUC of 0.96. Customer segmentation revealed
1,250 loyal customers with 96.5% retention probabili ty, whereas 750 customers at risk had just 38.4% retention
probability. Personalized engagement was linked to enhancements in retention rate from 72.4% to 87.8%, repeat
purchase rate from 58.3% to 79.5%, customer satisfaction from 74.6% to 90.3%, and custo mer lifetime value from
$420 to $615. These results highlight that the use of predictive analytics in combination with personalization can
enhance customer retention and loyalty management. This framework serves as an effective base for culinary
marketing using data analytics, while further research is needed on multi -restaurant data, real -time analytics,
multimodal customer data, AI agents, and privacy-preserving learning.
International Academic Institute
for Science and Technology

International Academic Journal of Science and Engineering
Vol. 13, No. 3, 2026, pp. 300-312.
ISSN 2454-3896

International
Academic
Journal of
Science and Engineering

www.i aiest.com

International Academic Journal of Science and Engineering,
Vol. 13, No. 3, pp. 300-312.
301
Keywords: Machine Learning, Brand Loyalty Analytics, Customer Retention Prediction, Personalized
Engagement, Culinary Industry, Explainable Artificial Intelligence (XAI).
Introduction
The digitization of the culinary industry has changed the way customer relationships are managed via POS systems,
online ordering, mobile apps, loyalty programs, review platforms, and social media. This digitization creates many
touchpoints that produce lots of data on purchasing behavior, engagement, customer satisfaction, and customer loyalty
(El Guermai & Abdelfattah, 2025 ; Venkateswaran et al., 2024) . Traditional methods of customer relationship
management face challenges in integrating various sources of data and creating effective retention and engagement
strategies based on this data. Thus, machine learning (ML) holds great promise when it comes to  finding behavioral
patterns, predicting customer retention and churn, and implementing personalized marketing efforts  (Akter, 2025). It
is especially important for the competitive culinary industry because retaining customers and encouraging repeat
purchases may directly lead to customer lifetime value and improved performance.
In spite of growing interest in AI-driven personalization, analytics, loyalty programs, and customer churn forecasting,
these techniques have often been studied independently from one another as distinct forms of analysis. As a result,
there is a clear requirement for an overarching approach that can tie together customer behavioral insights, sentiment
data, retention forecasting, explainable analytics, and personalization in a single setting specific to the culinary
industry.
The unique aspect of this study lies in developing the Machine Learning -Based Brand Loyalty Analytics Framework
through which the integration of transactional history, loyalty program membership, digital engagement, customer
sentiments, and behavioral trai ts will be used for predicting loyalty and personalized engagement. This framework
compares Random Forest, XGBoost, LightGBM, CatBoost, and Deep Neural Networks models, and uses explainable
AI in order to find the important factors responsible for retention.
The rest of this paper is structured in the following way. Section 2 introduces the literature background along with the
research gap. Section 3 illustrates the suggested framework and its main elements. Section 4 provides information on
data acquisition, preprocessing, feature generation, and model training. Section 5 demonstrates the experimental
results and comparative analysis. Section 6 provides discussion, implications, and limitations. Finally, conclusions
and directions for further research are provided in Section 7.
Literature Review
A number of recent studies show how AI, ML, and predictive analytics have become increasingly important in
customer engagement, personalization, loyalty, and retention. The application of AI personalization is linked to
increased consumer engagement due to personalized marketing communications based on characteristics of particular
customers (AL-Ghaswyneh, 2025 ; Shwetha & Afza, 2026) . In the culinary industry and ghost kitchens, ML
personalization can be used for highly personalized marketing and promotion decisions (Solar, 2025). The earlier
hospitality studies showed how ML could help engage customers dynamically and co -create value through loyalty
schemes (Aluri et al., 2019) . There are additional recent studies proving that ML marketing analytics increase
personalization and the quality of customer experience (Ganeshkumar et al., 2024; Cherenkov et al., 2024).
Customer retention is another significant field of application. There have been several studies that have revealed that
machine learning algorithms may be used in the determination of whether restaurant customers will continue to be
loyal or not. Moreover, retention predictive models are able to include the process of customer churn prediction and
personalized quality of service methods (Hemajothi et al., 2025; Ibitoye et al., 2026). More sophisticated approaches
consist of churn prediction, customer segmentation, and recommendations for customer retention (Jahan & Sanam,
2026). Service companies use predictive analytics to increase customer loyalty (Dahake et al., 2025) . It appears that
predicting customer retention works better with the help of behavioral and transactional data (Uddin, 2026 ;
Dele-Rotimi, 2026).
Personalization through AI is increasingly being associated with loyalty and relationship management as well. Studies
discuss how AI and ML contribute to customer experience, value generation, engagement, and loyalty in the context
of CRM, while omnichanne l personalization has the potential to improve engagement and loyalty  (Balcıoğlu, 2025;
Biswas et al., 2026) . AI-driven market basket prediction has been used to illustrate how ML can help improve
engagement with loyalty programs (Meftah et al., 2024) . Other research points to the strategic role of CRM in

International Academic Journal of Science and Engineering,
Vol. 13, No. 3, pp. 300-312.
302
managing customer relationships and retaining customers (Emon & Khan, 2026). AI-driven agents can also shape the
future of customer loyalty (Bilgihan et al., 2025).
The literature as a whole suggests that ML can be used for performing customer segmentation, customer retention
prediction, engagement using sentiments, personalization, and loyalty management. Nonetheless, the bulk of studies
in this area have investigated these functionalities separately or have considered these functionalities from the broader
perspective of digital marketing, e -commerce, CRM, and services. Few studies have attempted to develop a holistic
framework related to these functionalities using behavioral analysis, sentiment analysis, customer retention prediction,
Explainable AI, and personalized engagement in the context of the culinary industry. The current research thus fills
this gap.
Proposed Brand Loyalty Analytics Framework
Framework Architecture
The proposed Machine Learning–Driven Brand Loyalty Analytics Framework aims to design an integrated intelligent
framework to predict customer retention and improve engagement by adapting it to the specific context of the culinary
field. The framework comprises four layers: Data Acquisition Layer, Customer Behavioral Intelligence Layer,
Retention Prediction Layer, and Personalized Engagement Layer. All these layers wo rk together to convert raw
customer data into valuable business insights that can be utilized for customer retention and customer loyalty
management. Fig. 1 illustrates the Machine Learning– Driven Brand Loyalty Analytics Framework.
Data sources used by the Data Acquisition Layer include point-of-sale (PoS) transactions, online food ordering apps,
loyalty programs, mobile apps, customer surveys, social media interactions, and more. Once collected, the data is
preprocessed, normalized, and features are extracted in order to ensure its quality and consistency . The Customer
Behavioral Intelligence Layer collects and analyses information on customer purchasing patterns, visit frequency,
spending habits, sentiment scores, and engagement activities to create detailed customer profiles.
The Retention Prediction Layer is powered by state -of-the-art algorithms like XGBoost, Random Forest, and Deep
Neural Networks for calculating the probability of customer retention and predicting at-risk customers. Last but not
least, the Personalized Engagement Layer creates personalized recommendations, customizable rewards, targeted
promotions, and loyalty incentives that are tailored to customers' preferences and behavioral traits. The model
incorporates explainable artificial intelligence to increase predictability, thus allowing culinary businesses to foster
customer loyalty and value. Fig. 1 shows the machine learning-driven brand loyalty analytics framework.

Fig. 1: Machine Learning – Driven Brand Loyalty Analytics Framework
1. Data Sources
 2. Data Processing
• Data Collection
• Data Cleaning
• Feature Engineering
• Data Integration
3. Machine Learning
Engine
• Model Development
• Model Training
• Model Evaluation
• Best Model Selection
• Retention Prediction
• Customer Segmentation
• Retention Analysis
• Feature Importance
• Insights Dashboard
4. Analytics & Insights
• Personalized Recommendations
• Targeted Campaigns
• Loyalty & Rewards
• Retention Actions
5. Personalized
Engagement & Action
6. Feedback & Continuous Learning
Collect Feedback
 Update Data
 Monitor Performance
 Refine & Improve
• Improved Customer Retention
• Higher Customer Satisfaction
• Increased Loyalty Participation
• Greater Customer Lifetime Value
• Data-Driven Decision Making

International Academic Journal of Science and Engineering,
Vol. 13, No. 3, pp. 300-312.
303
Customer Behavioral Intelligence Module
The Customer Behavioral Intelligence Module acts as the foundation of the suggested framework since it analyzes the
customer interaction data to get meaningful insights. This module focuses on understanding the preferences,
purchasing behavior, engagement, and sentiment of customers in order to determine what drives brand loyalty in the
culinary industry. The module analyzes both structured and unstructured data gathered from transactions, loyalty
programs, apps, online reviews, and social media. The behavi oral insights obtained through analyzing important
behavioral metrics such as purchase frequency, Average Order Value (AOV), menu preferences, revisit frequency,
promotion responsiveness, satisfaction, and sentiment are used to recognize behavioral pattern s. Customers are
segmented using machine learning -based clustering into various categories like loyal customers, sporadic visitors,
high-value customers, and churners. The Brand Attachment Index (BAI) is also developed for measuring the strength
of customer-brand relationship using behavioral and attitudinal factors.
Retention Prediction Engine
The Retention Prediction Engine determines the outcome of customer retention and finds those customers who are
vulnerable to leaving the culinary brand. This module applies state -of-the-art machine learning techniques to review
past customer information and make precise forecasts about the likelihood of retention. The goal is to allow businesses
to take action before the customer gives up and decrease churn.
Processed behavioural features of the engine from the Customer Behavioural Intelligence Module are used to include
purchase frequency, Customer Lifetime Value, Sentiment, Loyalty Participation, Digital Engagement Measures, and
Brand Attachment Measures. These features are leveraged for predictive modeling like Random Forest, Gra dient
Boosting, XGBoost, and Deep Neural Networks. The algorithms are able to discover sophisticated patterns between
the customer attributes and calculate the chances of retaining each customer.
A Retention Risk Score (RRS) is determined , and customers  are sorted into low -risk, medium -risk, and high -risk
groups. High-risk customers are flagged to be engaged in real time in accordance with their assignment. The high-risk
customers are automatically assigned to be engaged in real time. The Explainable AI methods include SHAP and
LIME to provide insights into the most important variables for each prediction, improving transparency and trust in
the model's performance. This visibility allows managers to grasp the reasons behind customer attrition and formulate
the necessary measures to keep customers. It can therefore be considered a predictive model that can influence
decisions, create loyalty among customers, and improve business performance in the future.
Personalized Engagement Module
The Personalized Engagement Module takes predictive insight and turns it into actionable strategies for retaining
customers. This is achieved by taking predictive insights from machine learning algorithms, behavioral analytics, and
preferences and using th at information to provide personalized suggestions for the menu, rewards program,
promotions, and communications. Potential churners will be sent retention campaigns using customized incentives
and re-engagement messages. The recommendations and performanc e of the campaigns will be continually analysed
based on customer behaviour changes, and the success of the campaigns will be measured by response rate, customer
satisfaction, engagement, and repeat purchases.
Data Collection and Feature Engineering
Dataset Description
The customer retention forecast model is influenced by the quality and variety of the training data set. A real -time
customer analytics dataset was created by combining culinary service transactions, loyalty program history, reviews,
and social media interactions for culinary services. The data set contains about 5,000 customers within one year and
encompasses Average Order Value, purchase frequency, recency of orders, sentiment scores, review scores, digital
interaction, rewards redeemed, loyalty membership, and customer identity data.
The intensity of customer activity is determined by means of equation (1):
𝐶𝐴𝐼𝑖 = 𝑃𝐹𝑖 + 𝐴𝑂𝑉𝑖 + 𝐷𝐸𝑖 3     (1)
The framework applies CIᵢ, PFᵢ, AOV , and DE as key factors for measuring the customers’ behavior. For the purposes
of reliable model evaluation and customer retention prediction, the dataset is split into training (70%), validation
(15%), and test (15%) datasets.

International Academic Journal of Science and Engineering,
Vol. 13, No. 3, pp. 300-312.
304
Customer Transaction Data Collection
The data obtained from customer transactions will be the main behavioral data source that will be captured on
real-time basis from POS systems, restaurant management systems, mobile ordering systems, and food delivery
systems. These factors can offer a lot of information about the customer's purchase habits and their spending patterns.
The Purchase Frequency Score (PFS) is obtained by the following equation (2):
𝑃𝐹𝑆𝑖 = 𝑁𝑖 𝑇                      (2)
Where 𝑁𝑖 represents the total number of purchases by the customer that occurred during the observation period T. The
higher the frequency of purchase, the more loyal customers are likely to be and the higher the likelihood of retaining
them, as shown in equation (2).
Additionally, Average Order V alue (AOV) is computed using equation (3):
𝐴𝑂𝑉𝑖 =
∑ 𝑂𝑛 𝑗=1 𝑉𝑗
𝑛        (3)
Where  𝑂𝑉𝑗 is the order value of the transaction 𝑗 and 𝑛 is the number of transactions. Equation (3) serves as an aid to
identify high-value customers that can play a key role in the organization's revenues. The transactional data is
continually synced and synchronized to a centralized customer analytics store to allow real -time monitoring of
customer behavior and to assist with predictive modeling of customer retention.
Loyalty Program Data Extraction
Loyalty schemes are a great source of customer engagement data, and can offer a direct measure of brand attachment.
Customer data is obtained from digital loyalty management systems which track customer enrollment information,
reward point accumulation, re ward redemptions, membership tiers, promotions and referral information. The
combination of these variables gives insights into the commitment and level of interaction that customers have towards
the brand.
The Loyalty Participation Index (LPI) is calculated as in equation (4):
𝐿𝑃𝐼𝑖 = 𝑅𝑃𝑖 + 𝑅𝑅𝑖 + 𝑃𝑃𝑖 3 (4)
Reward Points earned 𝑅𝑃𝑖 denotes the number of Reward Points earned, and Reward Redemption rate 𝑅𝑅𝑖 represents
the rate of redemption of Reward Points, while Promotional Participation rate 𝑃𝑃𝑖 represents the rate of participation
in the promotion. As shown in equation (4), customers with a higher loyalty participation value will have higher
engagement value and are more likely to remain loyal.
A Customer Loyalty Strength Score (CLSS) is further estimated using equation (5):
𝐶𝐿𝑆𝑆𝑖 = 𝛼𝑃𝐹𝑆𝑖 + 𝛽𝐿𝑃𝐼𝑖 (5)
Where α and β are weighting coefficients, and the purchasing behavior and loyalty engagement are merged into a
single measure of loyalty, as done in equation (5). The customer loyalty data extracted are combined with the
transactional and behavioral data to create detailed customer profiles. The integration will allow the proposed
framework to identify valuable customer segments, assess levels of risk for dropping off, and help to develop tailored
strategies that engage customers.
Social Media and Review Data Collection
The sentiments of customers shared through social media and online review sites can be invaluable to understanding
customer satisfaction and how they feel about culinary brands. The information is gathered from Instagram, Facebook,
Google Reviews, Yelp, Zo mato, food delivery apps, etc. The data collected comprises sentiment indicators, likes,
comments, shares, review text, and review ratings. Sentiment scores are assessed using Natural Language Processing
(NLP) algorithms and methods to convert textual feedback into quantitative scores. The Sentiment Score (SS) can be
computed as follows in equation (6):
𝑆𝑆𝑖 = 𝑃𝑖 − 𝑁𝑖 𝑃𝑖 + 𝑁𝑖                   (6)

International Academic Journal of Science and Engineering,
Vol. 13, No. 3, pp. 300-312.
305
𝑃𝑖 represents the number of times positive sentiment appeared, and  𝑁𝑖 represents the number of times negative
sentiment appeared. As reflected in equation (6), the sentiment scores are between −1 and +1, which reflects the
customer perception of the brand.
The Review Influence Score (RIS) can be estimated by the following equation (7):
𝑅𝐼𝑆𝑖 = 𝑆𝑆𝑖 × 𝐸𝑅𝑖             (7)
Where 𝐸𝑅𝑖denotes Engagement Rate. Equation (7) indicates the impact of customer reviews on brand perception and
engagement. These social media and review metrics help build customer behavioral profiles with emotional and
experiential metrics that may be lacking from traditional transaction-based retention programs.
Data Cleaning and Preprocessing
Customer data can come from various sources and may be inconsistent, have duplicate records, missing data, and
noisy information that can impact model performance. Hence, data cleansing and data preprocessing are carried out
to ensure data quality and reli ability of the data analysis. The workflow of the preprocessing involves duplicate
removal, imputation of missing values, outlier detection, normalization, and feature transformation.
Mean substitution (As shown in equation (8)) is used to address missing values:
Missing values are handled using mean substitution as expressed in equation (8):
𝑀𝑉 =
∑ 𝑋𝑖 𝑛 𝑖=1
𝑛         (8)
Where 𝑋𝑖 represents available observations and 𝑛 denotes the number of valid records. equation (8) replaces missing
numerical values with the mean of observed values.
Feature normalization is conducted using Min-Max normalization as shown in equation (9):
𝑋′ = 𝑋 − 𝑋𝑚𝑖𝑛
𝑋𝑚𝑎𝑥 − 𝑋𝑚𝑖𝑛
(9)
In the above, X represents the value of the original feature and X' represents the normalized value of the feature. From
equation (9), all the variables are transformed to be in the range 0 -1, which enhances machine learning performance.
The preprocessed data is later converted into well -defined feature vectors that help segment customers, predict
attrition, and analyze engagement personalized to each customer. At this stage, the proposed framework is ensured to
run on reliable, consistent, and high-quality customer data.
As shown in table 1, the Sample real-time customer analytics data was captured from restaurant point-of-sale systems,
loyalty database systems, mobile ordering apps , and online restaurant review sites. This dataset comprises attributes
of customer behavior, transactional data, customer loyalty, and customer sentiment,  which are used for customer
retention prediction and engagement modeling for personalized interactions.
Table 1: Real-Time Culinary Customer Analytics Dataset Sample
Customer
ID
Purchase
Frequency (PF)
Average Order
Value (USD)
Loyalty
Points (LP)
Sentiment Score
(SS)
Retention
Status
C001 12 45.80 320 0.85 Retained
C002 8 32.50 180 0.62 Retained
C003 3 18.40 45 -0.25 Churned
C004 15 56.70 410 0.91 Retained
C005 5 24.60 90 0.12 Churned
C006 10 39.20 275 0.74 Retained
C007 2 15.30 25 -0.48 Churned
C008 14 52.80 390 0.88 Retained
C009 6 28.90 130 0.35 Retained
C010 4 21.50 60 -0.18 Churned
Dataset Characteristics
The experimental dataset includes customer communication gathered across various food service communication
channels such as Point of Sale (POS) systems in restaurants, food ordering applications online, loyalty management,
and customer review platforms. There are about 5000 customer records in the complete dataset, which was gathered

International Academic Journal of Science and Engineering,
Vol. 13, No. 3, pp. 300-312.
306
over 12 months. Each record is a unique customer profile that is differentiated by their purchasing behavior, spending
pattern, loyalty participation, customer sentiment, and the outcome of retention.
Table 2: Customer Analytics Dataset Features and Data Types
Variable Description Data Type
Customer ID Unique customer identifier Categorical
Purchase Frequency (PF) Number of purchases during observation period Numerical
Average Order Value (AOV) Average spending per transaction Numerical
Loyalty Points (LP) Total accumulated reward points Numerical
Sentiment Score (SS) Customer opinion score (-1 to +1) Numerical
Retention Status Customer retention outcome Binary
The dataset is subsequently divided into:
• Training Set: 3,500 records (70%)
• Validation Set: 750 records (15%)
• Testing Set: 750 records (15%)
The retention ratio is computed using equation (10):
𝑅𝑅 = 𝑁𝑅
𝑁𝑇
× 100               (10)
Where 𝑅𝑅represents the retention ratio , 𝑁𝑅denotes the number of retained customers, and 𝑁𝑇represents the total
number of customers.
The churn ratio is calculated using equation (11):
𝐶𝑅 = 𝑁𝐶
𝑁𝑇
× 100                 (11)
Where 𝐶𝑅represents Customer Churn Rate and 𝑁𝐶denotes the number of churned customers.
The data in table 2 is the input for the Customer Behavioral Intelligence Module, Retention Prediction Engine, and
Personalized Engagement Module of the proposed Brand Loyalty Analytics Framework. It provides a
multidimensional data set that can be used to analyze customer be haviour, the formation of customer loyalty, and
prediction of customer retention in the culinary industry
Machine Learning Model Development
The Machine Learning Model Development phase is crucial for the proposed Brand Loyalty Analytics Framework, as
it allows for the effective prediction of customer retention rates and facilitates individual engagement for better
customer retention in the cul inary sector. The main goal of this stage is to create intelligent predictive models to
uncover patterns in customer loyalty, to predict the probability of retaining customers, and also to identify potential
customer churn even before it happens.
Machine Learning allows for data analysis of customer behavior through the use of transactional history, involvement
in loyalty programs, sentiments, digital engagement, and demographics. Some of the models that can be used to
analyze customer behaviors in clude random forests, XGBoost, LightGBM, CatBoost, and Deep Neural Networks.
XGBoost is good at detecting non-linear patterns, while the dataset is split into training, validation, and testing subsets.
The various methods of hyperparameter optimization are used to enhance the accuracy of the models and to avoid
overfitting. Several evaluation measures are used for the assessment of the model performance , such as accuracy,
precision, recall, F1 score, and Area Under the Receiver Operating Characteristic Curve (AUC-ROC). The comparison
analysis is performed to identify the best one to use for predicting customer retention.
The Retention Prediction Engine is based on the developed machine learning models. These outputs contribute to the
Personalized Engagement Module, allowing the use of data analytics for enhancing customer retention, satisfaction,
and customer lifetime value.

International Academic Journal of Science and Engineering,
Vol. 13, No. 3, pp. 300-312.
307
Results and Discussion
Experimental Results
The proposed Machine Learning –Driven Brand Loyalty Analytics Framework was tested with a real -time customer
analytics dataset of 5,000 customer records that were derived from restaurant Point-of-Sale (POS), loyalty programs,
mobile restaurant ordering applications, and online customer review sites. The data was split into training, validation,
and testing sets to guarantee the trustworthiness of the model development and unbiased estimation of model
performance. Five machine learning algorithms were used, namely Random Forest, XGBoost, LightGBM, CatBoost,
and Deep Neural Network (DNN), where each was tested to see how well it was able to predict customer retention
and help with customer personalization. The experimental analysis in this study was conducted to compare the
predictive performance, to determine which customer attributes are influential with regard to customer retention, and
to analyze the customers' retention behavior in different segments.
The predictive performance of the machine learning models evaluated is shown in table 3, and the overall comparison
across the various metrics is shown in the heat map in fig. 2. Generally, the findings show that all five machine learning
models successfully predicted the customer retention rate despite having varying performances among the algorithms.
Overall, XGBoost has the best performance with an Accuracy of 94.3%, Precision of 93.7%, Recall of 92.8%,
F1 score of 93.2%, and an AUC of 0.96. CatBoost was the second best, followed by Random Forest, LightGBM, and
Deep Neural Network. The ability of XGBoost to model the nonlinear behavior of customers and learn complex
relationships between loyalty measures, buying patterns, and customer engagement measu res is a key reason why it
is superior.
Table 3: Performance Comparison of Machine Learning Models
Model Accuracy (%) Precision (%) Recall (%) F1-Score (%) AUC-ROC
Random Forest 91.6 90.8 89.9 90.3 0.92
XGBoost 94.3 93.7 92.8 93.2 0.96
LightGBM 90.9 89.5 88.7 89.1 0.91
CatBoost 92.8 92.1 91.3 91.7 0.94
Deep Neural Network 89.7 88.8 87.6 88.2 0.89
Fig. 2 is a complete picture of the performance comparison of all of the models that were tested. A darker intensity
corresponds to a higher score on the performance measures, which helps to determine the best algorithm on a number
of metrics at once. The results are clearly shown, where XGBoost is clearly the leader, and CatBoost is competitive in
the classification task. Random Forest, LightGBM, and Deep Neural Network had marginally lower performance, but
were still capable of consistently predicting the accuracy needed for customer retention analysis. Table 3 and fig. 2
show the performance of the two types of machine learning methods in the proposed framework: ensemble learning
techniques are superior to conventional machine learning methods for loyalty prediction.

Fig. 2: Machine Learning Model Performance Comparison

International Academic Journal of Science and Engineering,
Vol. 13, No. 3, pp. 300-312.
308
The proposed framework also analysed customer retention behaviour, dividing customers into four groups of behavior
according to the purchase pattern, participation in loyalty and engagement activities. The segmentation results are
presented in table 4 and the corresponding probabilities of retention in a lollipop chart as shown in fig 3. This analysis
gives businesses a better sense of the difference in customer loyalty among customer segments, and the ability to focus
on customer engagement programs based on customer retention risk.
Table 4: Customer Retention Analysis by Customer Segment
Customer Segment Number of Customers Average Retention Probability (%) Average Loyalty Score
Highly Loyal Customers 1,250 96.5 92
Regular Customers 1,850 84.2 78
Occasional Customers 1,150 63.7 55
At-Risk Customers 750 38.4 31
This customer segmentation analysis shows that there are significant differences in terms of retention probability
across various customer segments. Customers who scored the highest average on retention probability (96.5%) also
had the highest scores on loyalty (92), meaning that they were most likely to be loyal and purchase from the culinary
brand in the long term,  as they were more consistent in their purchases. The retention behavior among Regular
Customers was also positive, with an average of 84.2% retention probability, suggesting that their relationships with
customers are solid and based on regular interactions. Occasional Customers had a moderate retention rate of 63.7% ,
which indicated less regular customer behavior and less brand emotional attachment. The At -Risk Customer group
had the lowest retention probability (38.4%) and loyalty score (31), indicating that these customers are in need of
urgent attention, such as through customization of promotional content and measures to increase their loyalty.
Fig. 3 shows how each customer segment is ranked in terms of the likelihood of retaining a customer. It's evident that
behavioral segmentation is significant in CRM, as the difference between the two groups of customers (Highly Loyal
and At-Risk) is considerable. Customers who had engaged in the survey multiple times and were actively in the loyalty
program had a positive attitude and a frequent buying history and als o performed better in terms of retention. This
visualization further reinforces that customer segmentation offers vital insights for the highest-value customers and
deciding on the best customer engagement strategies.

Fig. 3: Customer Retention Probability by Customer Segment
The experimental evaluation also revealed the features of the customers that were the most important in predicting
customer retention. Purchase Frequency, Loyalty Points, Sentiment Score, and Digital Engagement were the top four
behavioral metrics, as always, in predicting customer loyalty among all the behavioral variables. Those who interacted
with the brand more often, actively participated in loyalty programs, gave a positive response to the brand through
online feedback, and had a high interaction level i n the digital sphere had significantly higher retention probabilities
than those who had lower levels of interaction. Moreover, the Personalized Engagement Module has successfully
determined the customers likely to have a high churn risk and come up with p ersonalized retention recommendations

International Academic Journal of Science and Engineering,
Vol. 13, No. 3, pp. 300-312.
309
based on the customer's behavior. The results show that a combination of transactional behavior, customer loyalty
involvement, customer sentiment, and machine learning analytics is an ideal basis for accurate customer retention
forecasting as well as intelligent and proactive customer relationship management in the culinary industry.
Discussion
The experimental assessment shows that the proposed Machine Learning–Driven Brand Loyalty Analytics Framework
is able to solve the issue of predicting customer retention in the culinary sector effectively and practically, while also
improving the level of personalization of customer engagement. The strong results obtained by the machine learning
models analyzed validate the ability to successfully forecast customer retention by using all of these elements of
transactional behavior, customer participation in loyalty programs, digital engagement, and customer sentiment in a
single analytical model. XGBoost algorithm performed best in predictive performance - meaning that it had the highest
ability to find complex nonlinear relationships between customer attributes and to provide the best possible prediction
of customer retention. The results show that sophisticated ensemble learning methods are appropriate for customer
loyalty analysis, thus enabling organizations to make reliable decisions based on data.
The suggested framework not only provides predictive information about customer loyalty but also provides valuable
information about behavioral characteristics that affect customer loyalty. Purchase Frequency, Loyalty Points,
Sentiment Score and Digital Engagement were found to be the most significant factors in the experimental analysis
of the factors that drive customer retention. Consistent with this, customer who were e ngaging with the brand on a
regular basis and had redeemed their loyalty rewards  had been expressing positive sentiments online, had interacted
with the brand regularly on digital channels, and  had higher probabilities of retention than customers with sparse
engagement. These results suggest that there are several factors other than transactions that contribute to customer
loyalty. By combining the data from various customer intelligence sources, businesses can gain a more comprehensive
view of customer behavior and use this insight to create effective strategies for customer retention.
The Explainable Artificial Intelligence (SHAP) feature importance analysis is shown in fig. 4 and represents the
contribution of each behavioral variable to the prediction process. The horizontal feature importance chart shows that
the most important features for the customer retention prediction are Purchase Frequency, Loyalty Points, Sentiment
Score, Digital Engagement and Average Order Value. Predictor factors include Review Rating, Recency, Discount
Usage, Tenure of the Customer, and Demographic Factors as well. Explainable AI provides a more transparent
framework through which predictions can be explained, enabling better decision-making.

Fig. 4: Explainable Artificial Intelligence (SHAP) Feature Importance Analysis
The PEM uses the predictive analysis results to generate relevant strategies for retaining customers. According to the
level of risk and their behaviour, it provides personalized offers, loyalty incentives, recommendations for the menu
and ways of communicating. Rather than a one -size-fits-all approach, companies can engage customers more
effectively through personalised engagement tactics that target customer preferences and behaviours in order to boost
satisfaction and customer loyalty.

International Academic Journal of Science and Engineering,
Vol. 13, No. 3, pp. 300-312.
310
These personal engagement strategies, which are summarized in table 5, are compared to organizational performance
before and after implementing personalization. Significant changes were seen in all the business indicators that were
measured. Customer Retention Rate rose from 72.4% to 87.8% , which is an improvement of 21.27%. Likewise, the
Repeat Purchase Rate went from 58.3% to 79.5% , and Loyalty Program Participation rose from 61.8% to 84.2%.
Additionally, the Customer Satisfaction Score significantly increased, from 74.6% to 90.3%, after customer
personalization. In addition, the adoption of an intelligent customer engagement strategy resulted in a Customer
Lifetime Value rise from $420 to $615 – highlighting the economic value of implementing the strategy. All these
enhancements suggest that the proposed framework's personalized recommendations have a positive impact on both
customer actions and the performance of the organization.
Table 5: Impact of Personalized Engagement Strategies
Performance Indicator Before Personalization After Personalization Improvement (%)
Customer Retention Rate 72.4 87.8 21.27
Repeat Purchase Rate 58.3 79.5 36.36
Loyalty Program Participation 61.8 84.2 36.25
Customer Satisfaction Score 74.6 90.3 21.05
Customer Lifetime Value $420 $615 46.43
The effect of all these improvements is shown in fig. 5, which provides an overview of all the factors contributing to
business performance, including personalized engagement. The figure clearly illustrates the evolution of the proposed
framework in terms of the progressive increase in the value of customer retention , repeat purchases, participation in
the loyalty program, customer satisfaction and customer lifetime value. The “sequential improvement” in the
visualization highlights that an improvement strategy tailored to the customer brings benefits beyond one performance
indicator, and not just in one dimension. It is clear that customer personalisation can be a viable cross -enterprise
approach that can drive customer loyalty, enhance engagement, and boost profits.

Fig. 5: The Impact of Personalized Engagement Strategies
In terms of managing a restaurant, the proposed Brand Loyalty Analytics Framework serves as a holistic decision
support system that helps restaurant managers and the marketing team recognize the important customer segments,
identify customers at high risk of churning and target better resource allocation for retention. All these elements,
brought together in a single platform, give organisations the opportunity to change the way they use marketing
methods, replacing them with a fact-based approach to customer retention strategies based on personal characteristics.
This is more effective marketing, builds strong customer relationship, and enhances the lifetime value of customers.

International Academic Journal of Science and Engineering,
Vol. 13, No. 3, pp. 300-312.
311
In general, combining machine learning with customer behaviour, customer loyalty, digital interaction, and sentiment
analysis helps create a smart solution for customer retention in the food and beverages industry.
The framework proposed not only has high predictive accuracy, but it is also interpretable and provides actionable
recommendations that can facilitate proactive decision -making. The framework fosters brand loyalty, customer
satisfaction, maximizes customer lifetime value, and ultimately helps modern food and beverage enterprises establish
sustainable competitive advantage, all while effectively leveraging predictive modelling and customizing interactions
with customers.
Conclusion
This paper proposed a Machine Learning -Driven Brand Loyalty Analytics Framework which can forecast customer
retention and personalization. This framework involves transaction behavior, participation in loyalty program, digital
interaction, customer sentime nt analysis, and behavioral features in order to provide an integrative approach in
analyzing customer loyalty and retention. With the help of a sample of 5,000 customer data, five machine learning
models were comparatively analyzed. The analysis showed th at XGBoost performed better than others with an
accuracy rate of 94.3%, precision of 93.7%, recall of 92.8%, F1 -score of 93.2%, and AUC of 0.96. It was able to
outperform other models such as Random Forest, LightGBM, CatBoost, and Deep Neural Network.  Further customer
segmentation also showed significant behavioral differences where 1,250 loyal customers showed an average retention
probability of 96.5%, compared to 750 at risk customers whose retention probability was only 38.4%. Some of the
main variables found to be relevant to retention were purchase frequency, loyalty program membership, sentiment
score, digital engagement, and average order value. The other variable of personalized engagement also saw a
significant improvement where retention went up from 72.4% to 87.8%, repeat purchase from 58.3% to 79.5%, loyalty
program membership from 61.8% to 84.2%, customer satisfaction from 74.6% to 90.3%, and customer lifetime value
from 420 to 615. Further studies would help validate this framework with more diverse data collected from larger and
multiple restaurants, as well as customer streams in real-time. Future studies might involve multimodal data, chatbots
powered by artificial intelligence, e nhanced recommendation systems, and federated learning that would further
personalize the process while protecting privacy.
References
AL-Ghaswyneh, O. F. M. (2025). Exploring the impact of AI -driven personalization on consumer engagement in
digital marketing. Management, 29(1). https://doi.org/10.58691/man/200968
Solar, T. S. (2025). Using machine learning algorithms to personalize customer experience in ghost kitchens:
hyper-personalized marketing and promotion. In  Impact of AI and the evolution of future ghost kitchens
(pp. 311-358). IGI Global Scientific Publishing. https://doi.org/10.4018/979-8-3373-0432-8.ch016
Aluri, A., Price, B. S., & McIntyre, N. H. (2019). Using machine learning to cocreate value through dynamic customer
engagement in a brand loyalty program.  Journal of Hospitality & Tourism Research , 43(1), 78 -100.
https://doi.org/10.1177/1096348017753521
Ganeshkumar, M., Karunakaran, S., Muzhumathi, R., & Suguna, R. (2024, October). Ai -driven marketing insights:
Harnessing machine learning for enhanced consumer engagement and personalization. In  2024 First
International Conference on Software, Systems and Information Technology (SSITCON)  (pp. 1 -6). IEEE.
https://doi.org/10.1109/SSITCON62437.2024.10796558
Cherenkov, E., Benga, V ., Lee, M., Nandwani, N., Raguin, K., Sueur, M. C., & Sun, G. (2024). From machine learning
algorithms to superior customer experience: Business implications of machine learning-driven data analytics
in the hospitality industry. Journal of Smart Tourism, 4(2), 5-14.
https://doi.org/10.52255/smarttourism.2024.4.2.2
Uddin, H. M. (2026). A systematic review of artificial intelligence -based customer analytics in personalized digital
marketing (2019 –2026). American Journal of Data Science and Analytics , 7(03), 295 -339.
https://doi.org/10.63125/x3e0dx27
Hemajothi, S., Stella, K., Mahesh, P., & NS, H. (2025, August). Enhancing Customer Retention in Restaurants using
Machine Learning Algorithm. In  2025 5th International Conference on Soft Computing for Security
Applications (ICSCSA) (pp. 1497-1503). IEEE. https://doi.org/10.1109/ICSCSA66339.2025.11170715
Dele-Rotimi, A. O. (2026). Enhancing customer value through artificial intelligence and machine learning:
Personalization, big data analytics, and customer experience management.  International Journal of Applied
Resilience and Sustainability, 2(2), 1290-1321. https://doi.org/10.70593/deepsci.0202052

International Academic Journal of Science and Engineering,
Vol. 13, No. 3, pp. 300-312.
312
Ibitoye, A. O., Kolade, O., & Onifade, O. F. (2026). Customer retention model using machine learning for improved
user-centric quality of experience through personalised quality of service.  Journal of Business Analytics ,
9(3), 177-195. https://doi.org/10.1080/2573234X.2025.2551950
Balcıoğlu, Y . S. (2025). AI-driven personalization in omnichannel marketing: enhancing customer engagement and
loyalty. In Leveraging AI for effective digital relationship marketing  (pp. 97 -130). IGI Global Scientific
Publishing. https://doi.org/10.4018/979-8-3693-5340-0.ch004
Biswas, S., Rane, N. L., & Rane, J. (2026). Enhancing customer experience, engagement, value creation, and loyalty
through artificial intelligence and machine learning in CRM. International Journal of Applied Resilience and
Sustainability, 2(2), 473-502. https://doi.org/10.70593/deepsci.0202019
Dahake, P. S., Gajghate, A., Dahake, P., Mohare, R., & Bhadade, P. (2025, November). Customer Loyalty in the Age
of Personalization: A Predictive Analytics Approach for Service -Based Business Models. In  2025 3rd
DMIHER International Conference on Artificial Intelligence in Healthcare, Education and Industry
(IDICAIHEI) (pp. 1-6). IEEE. https://doi.org/10.1109/IDICAIHEI65991.2025.11378814
Shwetha, S., & Afza, N. (2026). Role of AI-Driven Personalized Marketing in Enhancing Customer Engagement and
Fostering Brand Loyalty on Online Platforms. In  Harnessing AI and Predictive Analytics for
Decision-Making and Competitive Advantage  (pp. 247 -282). IGI Global Scientific Publishing.
https://doi.org/10.4018/979-8-3373-3648-0.ch009
El Guermai, R., & Abdelfattah, J. (2025, April). Enhancing Customer Loyalty Through Artificial Intelligence and Big
Data: A Narrative Literature Review. In International Conference on Digital Technologies and Applications
(pp. 91-102). Cham: Springer Nature Switzerland. https://doi.org/10.1007/978-3-032-07915-2_8
Meftah, M., Ounacer, S., & Azzouazi, M. (2024). Enhancing customer engagement in loyalty programs through
AI-powered market basket prediction using machine learning algorithms. In  Engineering applications of
artificial intelligence (pp. 319-338). Cham: Springer Nature Switzerland.
https://doi.org/10.1007/978-3-031-50300-9_18
Emon, M. M. H., & Khan, T. (2026). Strengthening Bonds: The Strategic Role of Customer Relationship Management
in Loyalty and Retention. In Strategic Innovation and Sustainable Customer-Centric Growth (pp. 27-56). IGI
Global Scientific Publishing. https://doi.org/10.4018/979-8-3373-6955-6.ch002
Akter, M. (2025). Impact of predictive machine learning models on operational efficiency and consumer satisfaction
in university dining services.  ASRC Procedia: Global Perspectives in Science and Scholarship , 1(01),
376-403. https://doi.org/10.63125/5tjkae44
Venkateswaran, P. S., Dominic, M. L., Agarwal, S., Oberai, H., Anand, I., & Rajest, S. S. (2024). The role of artificial
intelligence (AI) in enhancing marketing and customer loyalty. In  Data-driven intelligent business
sustainability (pp. 32-47). IGI Global Scientific Publishing.
https://doi.org/10.4018/979-8-3693-0049-7.ch003
Bilgihan, A., Ostinelli, M., Zhang, Y ., & Lorenz, M. (2025). Artificial intelligence (AI) agents and the future of
customer loyalty.  International Journal of Contemporary Hospitality Management , 37(9), 3240 -3262.
https://doi.org/10.1108/IJCHM-03-2025-0373
Jahan, I., & Sanam, T. F. (2026). A comprehensive framework for customer retention in E -commerce using machine
learning based on churn prediction, customer segmentation, and recommendation.  Electronic Commerce
Research, 26(1), 1-44. https://doi.org/10.1007/s10660-024-09936-0
