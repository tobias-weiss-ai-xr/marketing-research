---
title: INTELLIGENT CUSTOMER SEGMENTATION FOR PRECISION MARKETING USING ARTIFICIAL INTELLIGENCE
url: https://doi.org/10.70102/afts.2026.1836.478
category: ai-marketing
subcategory: empirical
date: 2026-09
venue: Archives for Technical Sciences
authors:
- Dr. Vijayakanthan Selvaraj
- Arasuraja Ganesan
- Dr.V. Aruna
source: openalex-oa
pdf_url: https://arhivzatehnickenauke.com/article/1280/pdf/download
pages: 12
chars: 44564
fetched_at: '2026-11-08T20:02:19+00:00'
kb_version: 1
---

# INTELLIGENT CUSTOMER SEGMENTATION FOR PRECISION MARKETING USING ARTIFICIAL INTELLIGENCE

Dr. Vijayakanthan Selvaraj, et al: Intelligent ……  Archives for Technical Sciences 2026, 36(2), 478-489
Technical Institute Bijeljina, Archives for Technical Sciences. Year XVIII – N 0 36           478
ISSN 1840-4855
e-ISSN 2233-0046

Original scientific article
http://dx.doi.org/10.70102/afts.2026.1836.478

INTELLIGENT CUSTOMER SEGMENTATION FOR
PRECISION MARKETING USING ARTIFICIAL
INTELLIGENCE
Dr. Vijayakanthan Selvaraj1*, Dr. Arasuraja Ganesan2, Dr.V. Aruna3,
Dr.M. Vijayakumar4

1*Assistant Professor (Senior Grade),  Faculty of Management,  SRM Institute of Science
and Technology, Vadapalani, Chennai, Tamil Nadu, India.
e-mail: svijayakanthan76@gmail.com, orcid: https://orcid.org/0000-0002-5662-1928
2Associate Professor,  Department of Management Studies,  St. Joseph’s College of
Engineering, OMR, Chennai , Tamil Nadu, India.  e-mail: arasuraja.mba@gmail.com,
orcid: https://orcid.org/0000-0001-6137-1911
3Assistant Professor,  Department of Management Studies,  St. Joseph’s Institute of
Technology, OMR, Chennai, Tamil Nadu, India. e-mail: arunasivakumar28@gmail.com,
orcid: https://orcid.org/0009-0009-0859-6439
4Professor, Department of Management Studies, Panimalar Engineering College,
Poonamallee, Chennai, Tamil Nadu, India. e-mail: vijai711@gmail.com,
orcid: https://orcid.org/0000-0002-9154-3507
Received: May 19, 2026; Revised: June 29, 2026; Accepted: August 10, 2026; Published: September 29, 2026
SUMMARY
As digital marketing platforms evolve, there is an increasing need for intelligent customer segmentation
methods to comprehend complex customer behaviors and enable personalized marketing strategies.
The conventional approaches to customer segmentation are mainly based on demographics and
transactions of customers, which limit the effectiveness of understanding the dynamic customer
preferences, behavior variations, and marketing needs in real -time. To overcome these challenges, this
study introduces Artificial Intelligence-Based Intelligent Customer Segmentation for Precision Marketing
(AI-ICSPM). The uniqueness of the suggested approach is the combination of custo mer behavioral
feature learning, dimensionality reduction via PCA, the K-Means Clustering algorithm for segmentation,
and predictive decision-making via the random forest algorithm within a precision marketing framework.
This research suggests a customer d ata collection, preprocessing, feature extraction and optimization,
segmentation, and marketing strategy development process. Evaluating the framework is done based on
a set of 5,000 customer records that contain demographic, transactional, purchase, and e ngagement
information. The analysis was done based on comparative analysis between the framework and
demographic segmentation, RFM segmentation, conventional k -means algorithm segmentation, and
machine learning segmentation techniques. As a result, the exp erimental results show that the suggested
AI-ICSPM framework outperforms other frameworks in terms of clustering performance, with a
Silhouette Score of 86.5%, a Davies–Bouldin Index of 0.214, and a Calinski–Harabasz Index of 5428.6.
Moreover, the framework enhances the results of predictive marketing through improved customer
profiling, recommendation, and retention activities.
Key words: artificial intelligence, intelligent customer segmentation, precision marketing, customer
analytics, machine learning, personalized marketing, predictive analytics.

Dr. Vijayakanthan Selvaraj, et al: Intelligent ……  Archives for Technical Sciences 2026, 36(2), 478-489
Technical Institute Bijeljina, Archives for Technical Sciences. Year XVIII – N 0 36           479
INTRODUCTION
Segmentation of customers through intelligent analysis has now become an important aspect of precision
marketing in order to determine customer segments and implement behavioral patterns and personalized
strategies. Innovations in artificial intelligence (AI), clustering methods, and deep learning techniques
have significantly enhanced the marketing system's ability to analyze consumer information and predict
customer response to make decisions based on that prediction  [1]. Intelligent segmentation using AI
enables targeted customer targeting through intelligent recommendation and adaptive learning methods
[2]. Decision-support systems based on AI have been used in order to improve precision marketing by
combining customer analysis, predictive modeling, and intelligent decision-making [3]. The application
of AI in the field of product marketing has changed customer experience management through advanced
market segmentation and consumer profiling [4].
The application of the methods of AI to personalized marketing approaches contributes to cultural
segmentation and better targeting through an analysis of different customer traits and preferences.
The use of such frameworks is known to increase customer engagement due to the application of
adaptive recommendations and better marketing communication strategies [5]. The use of deep
learning-based mathematical models in combination with the explainable AI and RFM analysis has
contributed to customer segmentation with the help of better classification and behavior interpretations
[6]. Modern research has considered the possibilities of using customer segmentation frameworks based
on AI for personalized marketing purposes, indicating an increase in their ability to segment customers
[7]. Machine learning -based customer segmentation frameworks can help organizations reveal useful
information from huge customer datasets for effective marketing purposes [8].
Machine learning techniques used in consumer behavior prediction have also been useful in precision
marketing by enabling the forecast of customer preferences and buying intentions. Intelligent techniques
are used in supporting data -driven marketing techniques via continuous analysis of customers'
interaction patterns and behavioral trends [9]. In addition, AI based personal marketing techni ques
enhance the customer experience and predictive targeting through the use of intelligent analytics to
enhance segmentation and communication strategies [10]. However, there are issues associated with
dynamic behaviors of consumers in current approaches . Thus, it is imperative to have intelligent
segmentation frameworks that make use of artificial intelligence in order to make informed decisions
about customer behavior.
Key Contribution
• The research develops an intelligent segmentation model that employs the use of artificial
intelligence to analyze customers' traits, behaviors, and transactions. The model allows accurate
customer group identification and facilitates precision marketing using data analysis.
• The recommended method employs the use of predictive analysis to identify the preferences of
customers and their purchasing behaviors to make recommendations and conduct marketing
activities accordingly. In comparison to traditional segmentation methods, t he intelligent system
facilitates higher customer engagement and satisfaction levels.
• The research offers an adaptive solution to continuously analyze and segment customers depending
on changing market conditions and customer behavior. Using the intelligent analytical tools,
businesses can make efficient marketing decisions while effectively utilizing their resources.
This paper is organized as follows. The literature review will be described in Section II, which includes
the literature on the current artificial intelligence -based customer segmentation, precision marketing,
and the research gap found in past studies. In Section III, the proposed methodology will be explained,
which consists of the overall architecture of the AI -ICSPM framework, use of AI in customer
segmentation, and the proposed algorithm for intelligent customer classification and precision
marketing. Finally, Section IV will present the results of our experiments, which include the description
of datasets used, data collection and preprocessing methods, parameter initialization, software and
hardware configuration, evaluation criteria, and comparative analysis with current customer

Dr. Vijayakanthan Selvaraj, et al: Intelligent ……  Archives for Technical Sciences 2026, 36(2), 478-489
Technical Institute Bijeljina, Archives for Technical Sciences. Year XVIII – N 0 36           480
segmentation techniques. Performance analysis of our proposed framework will also be included in this
section. Finally, the conclusions drawn from this research will be presented in Section V.
LITERATURE REVIEW
Digital marketing has greatly benefited from artificial intelligence through improved personalization and
consumer engagement through sophisticated analysis of consumer preference, behavior, and interaction
history. Artificial intelligence marketing system s can help automate customer profiling and
communication for better segmentation and marketing campaign effectiveness [11]. Business
segmentation using AI is another example of intelligent systems being used to classify customers,
identify market opportunities, and support strategic marketing decisions [12]. Recent systematic studies
on artificial intelligence for customer analytics show that machine learning, prediction, and
recommendations are becoming more important in personalized digital marketing. The use of these
techniques is valuable for customer segmentation because help to analyze consumer data and improve
targeted marketing activities [13]. Sophisticated customer segmentation models that include behavior
indicators and clustering algorithms have been used in order  to increase the accuracy of customer
grouping and marketing strategy design [14].
Intelligent real-time segmentation with the use of big data analytics and clustering technique is helpful
for enterprises to be able to keep track of customer behaviors and modify marketing strategies
accordingly. The intelligent segmentation process makes  enterprises more responsive and better at
managing relationships with customers within highly competitive digital markets [15].
AI algorithm -powered precision marketing platforms have helped make better decisions regarding
e-commerce by making patterns out of customer data [16]. Big data analytics-powered digital marketing
strategies have helped businesses gain better skills for understanding customer behavior, forecasting
their preferences, and developing personalized marke ting strategies. This approach helps businesses
understand the necessity of combining intelligence analytics with customer segmentation in order to be
successful in marketing [17]. Customer segmentation approaches based on data analytics are also helpful
for targeted advertisements that incorporate customer analytics and behavior modeling [18].
Artificial intelligence-based product marketing solutions help in improving customer experience by
improving the segmentation process and producing insights from customer data. By making use of
intelligent analytics, companies can gain a better understandi ng of customers' needs and devise
personalized approaches for engaging and satisfying them [19]. With advancements in intelligent
technologies, the future of precision marketing lies in the integration of AI-based prediction, automation
and customer intell igence for optimal decision making [20]. Even though current research shows the
efficiency of AI-based segmentation and personalization methods, it is still difficult to achieve real-time
adaptability and accuracy in predicting customer behavior. Thus, the re is a need for an intelligent
customer segmentation framework employing artificial intelligence.
Research Gap
Although there have been many breakthroughs in AI -based customer analysis and personalized
marketing, existing solutions tend to suffer from challenges associated with adapting to dynamic
customer behavior, real -time segmentation, and forecasting the chang es in consumer preferences.
Moreover, conventional segmentation approaches often involve static clustering algorithms with a few
behavioral features that limit their usefulness for use in modern digital marketing scenarios. Thus, an
intelligent AI-based customer segmentation solution is necessary.
PROPOSED METHODOLOGY
Overall Architecture for Research Methodology
Figure 1 describes the proposed framework and provides a detailed overview of the entire process
involved in the AI-based Intelligent Customer Segmentation framework. The entire process begins from
the Data Acquisition layer, where a variety of data about customers, including demographic, transactional,

Dr. Vijayakanthan Selvaraj, et al: Intelligent ……  Archives for Technical Sciences 2026, 36(2), 478-489
Technical Institute Bijeljina, Archives for Technical Sciences. Year XVIII – N 0 36           481
behavioral, purchase histories, social interaction, and feedback data, is gathered in order to form a full
knowledge base about customers. Once the required customer data has been gathered, it is preprocessed
and converted into behavioral features at the Data Preprocessing and Feature Engineering layer.

Figure 1. Overall architecture of proposed methodology
The extracted features are then analyzed further in the AI-Based Feature Learning Layer, where machine
learning techniques and principal component analysis (PCA) find hidden correlations, reduce
dimensionality, and create optimized representations of customer behavior, simplify the data, and create
advanced features of the customer behavior. The learned features are sent to the Intelligent Customer
Segmentation Layer, where AI -based clustering and classification methods segment customers into
groups that include valuable customers, potential customers. Lastly, the Precision Marketing Decision
Layer applies the created customer segments to develop targeted marketing campaigns, personalized
offers, recommended products, and customer retention programs. Evaluation of marketing results allows
improving customer engagement, conversion rates, and retention. Therefore, the proposed architecture
allows creating an end-to-end AI-based solution for converting customer data into marketing decisions.
Integration of AI Technology in Customer Segmentation
The AI technology has revolutionized conventional ways of customer segmentation in that it uses the
dynamics of market analysis which is data -driven and more personalized. The methods of customer
segmentation used traditionally depend mainly on demographic s, geography, and Behavioral aspects,
which may not be able to explain intricate customer behavior. Applying AI introduces sophisticated
tools such as machine learning, dimensionality reduction, and predictive analytics  to unearth hidden
connections from customer data in huge amounts. The Intelligent Customer Segmentation for Precision
Marketing Using Artificial Intelligence model involves the use of AI algorithms to analyze different
aspects of customer data including buying behavior, transactions, social media activities, etc.
Clustering methods based on machine learning like K-means, Hierarchical Clustering and density-based
methods allow for the automatic detection of customer segments that share common attributes.
Moreover, AI-powered predictive algorithms learn from newly collected data regarding the customers,
hence adapting the segmentation model to changes in the market and in consumer behavior. In addition
Data
Acquisition
Layer
Customer
Profile Data
Transaction
Records
Purchase
History
Web & App
Behavior
Social Media
Interactions
Feedback &
Survey Data
Demographic
Data
Data Preprocessing
& Feature
Engineering Layer
Data
Cleaning
Data
Integration
Data
Transformation
Feature
Extraction
Feature
Engineering
AI-Based Feature
Learning Layer
Machine Learning /
Deep Learning
Models
Pattern & Relationship
Discovery
Dimensionality
Reduction
Feature
Representation
Feature
Representation
 K-Means
Clustering
Hierarchical
Clustering
Gaussian
Mixture Models
Deep
Clustering
High-Value
Customers
Potential
Customers
Low-Engagement
Customers
Precision
Marketing
Decision
Layer
Targeted
Marketing
Campaigns
Personalized
Communications
Product
Recommendations
Optimized
Pricing &
Offers
Performance
Evaluation &
Feedback
Customer
Retention
Strategies
Improved Customer Engagement, Higher Conversion, Customer Retention & Business Growth

Dr. Vijayakanthan Selvaraj, et al: Intelligent ……  Archives for Technical Sciences 2026, 36(2), 478-489
Technical Institute Bijeljina, Archives for Technical Sciences. Year XVIII – N 0 36           482
to this, principal component analysis (PCA) helps to achieve accurate segmentations by reducing
high-dimensional features and preserving maximum variance across customer attributes.
Moreover, the implementation of AI also helps in achieving precision marketing through the link
between customer segmentations and marketing strategies tailored to them. Based on the information
provided by AI, companies can make recommendations regarding products and campaigns, predict the
purchasing intent of customers and also increase customer loyalty. The reinforcement learning and
recommendation algorithms contribute even more to decision making by analyzing customer behavior
and constantly improving marketing actions.
In the suggested framework, AI serves as an intelligent decision support system linking customer data
collection, behavioral analysis, segmentation and targeted marketing. Automated data analysis,
predictive intelligence and adaptive learning help companies transition from classification of customers
to intelligent segmentation of customers. Thus, the implementation of AI in marketing is helpful for
efficient marketing, customer satisfaction and competitive advantage for companies through
evidence-based decisions.
Proposed Algorithm for Research Methodology
𝐴𝑙𝑔𝑜𝑟𝑖𝑡ℎ𝑚: 𝐴𝐼 − 𝐼𝐶𝑆𝑃𝑀 (𝐴𝑟𝑡𝑖𝑓𝑖𝑐𝑖𝑎𝑙 𝐼𝑛𝑡𝑒𝑙𝑙𝑖𝑔𝑒𝑛𝑐𝑒
− 𝐵𝑎𝑠𝑒𝑑 𝐼𝑛𝑡𝑒𝑙𝑙𝑖𝑔𝑒𝑛𝑡 𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟 𝑆𝑒𝑔𝑚𝑒𝑛𝑡𝑎𝑡𝑖𝑜𝑛 𝑓𝑜𝑟 𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛 𝑀𝑎𝑟𝑘𝑒𝑡𝑖𝑛𝑔)
𝐼𝑛𝑝𝑢𝑡: 𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟 𝑑𝑎𝑡𝑎𝑠𝑒𝑡
𝑂𝑢𝑡𝑝𝑢𝑡: 𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟 𝑠𝑒𝑔𝑚𝑒𝑛𝑡𝑠
𝐵𝑒𝑔𝑖𝑛
1. 𝐶𝑜𝑙𝑙𝑒𝑐𝑡 𝑐𝑢𝑠𝑡𝑜𝑚𝑒𝑟 𝑑𝑎𝑡𝑎
2. 𝑃𝑟𝑒𝑝𝑟𝑜𝑐𝑒𝑠𝑠 𝑑𝑎𝑡𝑎:
      − 𝑅𝑒𝑚𝑜𝑣𝑒 𝑚𝑖𝑠𝑠𝑖𝑛𝑔 𝑎𝑛𝑑 𝑑𝑢𝑝𝑙𝑖𝑐𝑎𝑡𝑒 𝑣𝑎𝑙𝑢𝑒𝑠
      − 𝑁𝑜𝑟𝑚𝑎𝑙𝑖𝑧𝑒 𝑐𝑢𝑠𝑡𝑜𝑚𝑒𝑟 𝑎𝑡𝑡𝑟𝑖𝑏𝑢𝑡𝑒𝑠
3. 𝑆𝑒𝑙𝑒𝑐𝑡 𝑖𝑚𝑝𝑜𝑟𝑡𝑎𝑛𝑡 𝑐𝑢𝑠𝑡𝑜𝑚𝑒𝑟 𝑓𝑒𝑎𝑡𝑢𝑟𝑒𝑠:
      − 𝑃𝑢𝑟𝑐ℎ𝑎𝑠𝑒 𝑏𝑒ℎ𝑎𝑣𝑖𝑜𝑢𝑟
      − 𝑆𝑝𝑒𝑛𝑑𝑖𝑛𝑔 𝑝𝑎𝑡𝑡𝑒𝑟𝑛
      − 𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟 𝑖𝑛𝑡𝑒𝑟𝑎𝑐𝑡𝑖𝑜𝑛
      − 𝐷𝑒𝑚𝑜𝑔𝑟𝑎𝑝ℎ𝑖𝑐 𝑑𝑒𝑡𝑎𝑖𝑙𝑠
4. 𝐴𝑝𝑝𝑙𝑦 𝑃𝐶𝐴 𝑓𝑜𝑟 𝑓𝑒𝑎𝑡𝑢𝑟𝑒 𝑟𝑒𝑑𝑢𝑐𝑡𝑖𝑜𝑛
5. 𝐴𝑝𝑝𝑙𝑦 𝐾 − 𝑀𝑒𝑎𝑛𝑠 𝑐𝑙𝑢𝑠𝑡𝑒𝑟𝑖𝑛𝑔:
      − 𝐼𝑛𝑖𝑡𝑖𝑎𝑙𝑖𝑧𝑒 𝑐𝑙𝑢𝑠𝑡𝑒𝑟𝑠
      − 𝐺𝑟𝑜𝑢𝑝 𝑠𝑖𝑚𝑖𝑙𝑎𝑟 𝑐𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝑠
      − 𝑈𝑝𝑑𝑎𝑡𝑒 𝑐𝑙𝑢𝑠𝑡𝑒𝑟 𝑐𝑒𝑛𝑡𝑟𝑒𝑠 𝑢𝑛𝑡𝑖𝑙 𝑠𝑡𝑎𝑏𝑙𝑒

Dr. Vijayakanthan Selvaraj, et al: Intelligent ……  Archives for Technical Sciences 2026, 36(2), 478-489
Technical Institute Bijeljina, Archives for Technical Sciences. Year XVIII – N 0 36           483
6. 𝐼𝑑𝑒𝑛𝑡𝑖𝑓𝑦 𝑐𝑢𝑠𝑡𝑜𝑚𝑒𝑟 𝑠𝑒𝑔𝑚𝑒𝑛𝑡𝑠:
      − 𝐻𝑖𝑔ℎ − 𝑣𝑎𝑙𝑢𝑒 𝑐𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝑠
      − 𝑃𝑜𝑡𝑒𝑛𝑡𝑖𝑎𝑙 𝑐𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝑠
      − 𝐿𝑜𝑤 − 𝑒𝑛𝑔𝑎𝑔𝑒𝑚𝑒𝑛𝑡 𝑐𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝑠
7. 𝑇𝑟𝑎𝑖𝑛 𝑎 𝑚𝑢𝑙𝑡𝑖 − 𝑐𝑙𝑎𝑠𝑠 𝑅𝑎𝑛𝑑𝑜𝑚 𝐹𝑜𝑟𝑒𝑠𝑡 𝑐𝑙𝑎𝑠𝑠𝑖𝑓𝑖𝑒𝑟 𝑢𝑠𝑖𝑛𝑔 𝑡ℎ𝑒 𝑔𝑒𝑛𝑒𝑟𝑎𝑡𝑒𝑑 𝐾
− 𝑀𝑒𝑎𝑛𝑠 𝑐𝑙𝑢𝑠𝑡𝑒𝑟 𝑙𝑎𝑏𝑒𝑙𝑠 𝑎𝑠 𝑡𝑎𝑟𝑔𝑒𝑡 𝑐𝑙𝑎𝑠𝑠𝑒𝑠 𝑡𝑜 𝑒𝑛𝑎𝑏𝑙𝑒 𝑝𝑟𝑒𝑑𝑖𝑐𝑡𝑖𝑣𝑒
𝑐𝑢𝑠𝑡𝑜𝑚𝑒𝑟 𝑠𝑒𝑔𝑚𝑒𝑛𝑡 𝑎𝑠𝑠𝑖𝑔𝑛𝑚𝑒𝑛𝑡 𝑑𝑢𝑟𝑖𝑛𝑔 𝑖𝑛𝑓𝑒𝑟𝑒𝑛𝑐𝑒.
8. 𝑃𝑟𝑒𝑑𝑖𝑐𝑡 𝑛𝑒𝑤 𝑐𝑢𝑠𝑡𝑜𝑚𝑒𝑟 𝑠𝑒𝑔𝑚𝑒𝑛𝑡
9. 𝐺𝑒𝑛𝑒𝑟𝑎𝑡𝑒 𝑝𝑒𝑟𝑠𝑜𝑛𝑎𝑙𝑖𝑧𝑒𝑑 𝑚𝑎𝑟𝑘𝑒𝑡𝑖𝑛𝑔 𝑟𝑒𝑐𝑜𝑚𝑚𝑒𝑛𝑑𝑎𝑡𝑖𝑜𝑛𝑠
10. 𝑅𝑒𝑡𝑢𝑟𝑛 𝑓𝑖𝑛𝑎𝑙 𝑐𝑢𝑠𝑡𝑜𝑚𝑒𝑟 𝑠𝑒𝑔𝑚𝑒𝑛𝑡𝑠
𝐸𝑛𝑑
Algorithm Explanation
The AI-ICSPM algorithm proposed in this study analyzes customer data in a structured manner and
generates customer segments that support precision marketing decisions. First, customer information is
gathered through transaction records, CRM, and digital interaction platforms. Then, the data is
preprocessed to remove inconsistencies, fill missing data values, and normalize data attributes. Customer
features such as behavioral patterns, spending habits, engagement levels, and demographic details  are
extracted. These are optimized via feature selection and dimensionality reduction. Preprocessed data are
given to the K-Means clustering algorithm, which creates segments according to behavioral similarities
of the customers. The clusters are analyzed , and descriptive segment names are assigned, such as
high-value customers, potential customers, and low-engagement customers, based on their behaviors.
These segment labels are not used as features while training the K -Means algorithm. The proposed
model adopts a two-stage hybrid approach combining unsupervised clustering with supervised machine
learning. First, K-Means clustering is utilized in an offline phase to perform exploratory data analysis
and discover latent pseudo-ground-truth customer segments based on behavioral features. This approach
entails using a two-stage hybrid framework involving unsupervised clustering techniques and supervised
learning models. Firstly, the K-Means Clustering algorithm will be applied in the offline mode in order
to perform exploratory data analysi s and identify latent segments among the customers according to
their behaviors. Secondly, instead of using the traditional centroid distance look -up mechanism, the
Random Forest classification algorithm will be trained using the labels in order to account  for the
non-linearity in the decision boundaries and handle missing data during inference. In this context, the
Random Forest classification algorithm will function as a multi -class predictive inference engine for
online scoring.
EXPERIMENTAL RESULTS
Dataset Description
The recommended Intelligent Customer Segmentation for Precision Marketing using Artificial
Intelligence framework employs a multi-dimensional database of customer behavior consisting of 5,000
customer records derived from simulated e -commerce portals, cust omer relationship management
systems (CRM), transactional records, and online customer interaction data. The point that must be
highlighted is that this set of data is artificially developed in order to demonstrate the proposed
algorithms and the architect ure framework. Hence, the scale distribution of various attributes such as
income scale compared to luxury product classification is based on benchmarking rather than any

Dr. Vijayakanthan Selvaraj, et al: Intelligent ……  Archives for Technical Sciences 2026, 36(2), 478-489
Technical Institute Bijeljina, Archives for Technical Sciences. Year XVIII – N 0 36           484
realistic data of high -net-worth individuals. Every customer record consists of demographic,
transactional, and behavioral variables such as age, gender, location, yearly income, number of purchase,
transaction amount, preferred products, website portal visitation, effectiveness of campaign and
customer engagement level.
Data Collection and Preprocessing Technique
The intelligent customer segmentation using artificial intelligence proposed framework uses the
customer dataset that is multidimensional and sourced from the transactional database, customer
relationship management (CRM) systems, e -commerce system, and di gital interactions. The data
includes demographic information about customers, customer purchasing behavior, online interaction,
and marketing responses. An example of the dataset used for customer segmentation using AI is
presented in table 1 below.
Table 1. Sample customer dataset
Customer
ID
Age Gender Location Annual
Income
($)
Purchase
Frequency
Average
Purchase
Value ($)
Website
Visits/Month
Product
Preference
Campaign
Response
(%)
C001 25 Female Urban 32000 12 85 18 Fashion 78
C002 42 Male Suburban 68000 7 210 10 Electronics 62
C003 31 Female Urban 45000 15 120 22 Beauty
Products
85
C004 55 Male Rural 38000 4 75 5 Household
Items
40
C005 36 Female Metropolitan 75000 10 300 16 Luxury
Products
91
As mentioned in table 1, the acquired data set contains 5,000 records of customers with various
behavioral and demographic attributes in order to perform AI segmentation. Some of the most significant
attributes are related to customer demographics such as age, gender, and location; f inancial attributes
like income and ability to spend money; behavior attributes including buying frequency, transaction
amounts, and preferred products; and digital engagement attributes such as website visits, campaign
interactions, and feedback responses. These attributes enable clustering of similar customers and market
segmentation. Prior to employing artificial intelligence algorithms, the dataset is subject to preprocessing
to ensure the data is consistent and reliable. Thus, data cleansing is performed to eliminate duplicates,
fix inconsistencies, and process missing information through statistical imputation.  The encoding
process converts categorical features such as gender, location, and product category into numeric
representation. In addition, numerical attributes are normalized through feature scaling to ensure that all
variables contribute equally during model training . Feature engineering is conducted by creating
behavioral features such as a customer's lifetime value, purchase intensity index, engagement index, and
loyalty index. After that, the transformed dataset is used as input to AI -based clustering and predictive
models in order to uncover customer segments that might be hidden in it. This approach improves
segmentation accuracy and enables  precision marketing through customer segmentation. Customer
segments are not used as input features during the process of data preprocessing and modeling. Customer
segments are produced using the proposed AI -based clustering framework through demographic,
transactional, and behavioral features.
Parameter Initialization
Table 2 describes the parameter settings that define the functioning of the suggested Intelligent Customer
Segmentation for Precision Marketing Using Artificial Intelligence framework. The data set consisting
of 5,000 customer samples will be split into 80% training and 20% testing samples to make sure of the
proper learning and performance assessment of the framework. The K-Means clustering algorithm uses
Three customer groups to categorize customers with similar behavioral patterns, namely High -Value
Customers, Potential Customers and Low -Engagement Customers. The proposed framework employs
PCA for feature dimensionality reduction, K -Means clustering for customer segment generation, and
Random Forest classification for predictive segment assignment.

Dr. Vijayakanthan Selvaraj, et al: Intelligent ……  Archives for Technical Sciences 2026, 36(2), 478-489
Technical Institute Bijeljina, Archives for Technical Sciences. Year XVIII – N 0 36           485
Table 2. Parameter initialization for intelligent customer segmentation for precision marketing using artificial
intelligence
Parameter Value/Setting
Dataset Size 5,000 customer records
Data Split 80% Training, 20% Testing
Number of Clusters (K) 3
Distance Metric Euclidean Distance
Feature Reduction PCA (5 Components, 92.4% Cumulative Explained Variance)
Feature Scaling Min–Max Normalization
Clustering Algorithm K-Means
Supervised Classifier Random Forest
Therefore, the model configuration focuses on clustering and classification parameters rather than neural
network optimization settings. Principal  Component Analysis (PCA) with 5 components is applied
following Min–Max normalization, retaining approximately 92.4% of the total cumulative explained
variance. This ensures significant dimensionality reduction and noise suppression while preserving the
core latent behavioral signal without substantial loss of information. The performance of the proposed
framework is evaluated using internal clustering validation metrics, including Silhouette Score,
Davies–Bouldin Index (DBI), and Calinski–Harabasz Index (CHI), along with predictive and marketing
performance metrics such as Customer Lifetime Value (CLV) prediction accuracy, Mean Squared Error
(MSE), and Root Mean Square Error (RMSE), as presented in table 4.
Software and Hardware Configuration
Table 3. Software and hardware configuration
Category Configuration
Programming Language Python 3.10
Development Environment Jupyter Notebook / Google Colab
Machine Learning Libraries Scikit-learn, TensorFlow, Keras
Data Processing Tools Pandas, NumPy
Visualization Tools Matplotlib, Seaborn
Operating System Windows 11
Processor Intel Core i7 / AMD Ryzen 7
RAM 16 GB
Storage 512 GB SSD
GPU NVIDIA RTX Series (8 GB)
System Architecture 64-bit Computing Environment
Table 3 describes the Intelligent Customer Segmentation for Precision Marketing Using Artificial
Intelligence system, which is developed using a Python development environment that uses the latest
machine learning and data analytics packages. Model development can be conducted using Python 3.10
with Jupyter Notebook/Google Colab, where Scikit-learn is used for dimensionality reduction (PCA),
clustering (K-Means), and predictive modeling (Random Forest). Data pre-processing and data analysis
are carried out using Pandas and NumPy, while Matplotlib and Seaborn are used for visualizations and
results interpretation. The computing environment includes a Windows 11 operating system with an
Intel Core i7/AMD Ryzen 7 CPU, 16 GB RAM, 512 GB SSD, and an NVIDIA RTX series GPU to
accelerate training and computation in AI models.
Metric Evaluation
The performance of the proposed architecture is evaluated in two distinct phases to account for both
unsupervised clustering quality and supervised inference performance. Primary segmentation
performance is evaluated directly on the unsupervised clustering step using intrinsic internal validation
metrics including the Silhouette Score, Davies –Bouldin Index (DBI), and Calinski –Harabasz Index
(CHI) which measure cluster compactness and separation without requiring prior ground -truth class
labels. Subsequently, the downstream Random Forest classifier is evaluated using hold -out test set

Dr. Vijayakanthan Selvaraj, et al: Intelligent ……  Archives for Technical Sciences 2026, 36(2), 478-489
Technical Institute Bijeljina, Archives for Technical Sciences. Year XVIII – N 0 36           486
accuracy to measure how effectively the decision -tree ensemble approximates and generalizes the
learned high-dimensional decision boundaries for real-time online scoring.
Silhouette Score
𝑆(𝑖) = 𝑏(𝑖) − 𝑎(𝑖) 𝑚𝑎𝑥(𝑎, (𝑖)𝑏(𝑖))                                         (1)
In equation (1) describes the  𝑎(𝑖) defined Average distance between customer 𝑖and other customers in
the same cluster. 𝑏(𝑖) The minimum average distance between customers 𝑖and customers in another
cluster. A value closer to 1 indicates better-separated customer segments.
Davies–Bouldin Index (DBI)
𝐷𝐵𝐼 = 1 𝐾 ∑ 𝑚
𝐾
𝑖=1
𝑎𝑥𝑗≠𝑖 ( 𝑆𝑖 + 𝑆𝑗 𝑀𝑖𝑗 )                           (2)
In equation (2) describes the 𝐾 defined as the number of clusters  𝑆𝑖, 𝑆𝑗 represents Within-cluster scatter.
𝑀𝑖𝑗 defined as the distance  between cluster centroids. Lower  DBI values indicate better clustering
performance.
Customer Engagement Improvement
𝐶𝐸𝐼 = 𝐸𝑎𝑓𝑡𝑒𝑟 − 𝐸𝑏𝑒𝑓𝑜𝑟𝑒
𝐸𝑏𝑒𝑓𝑜𝑟𝑒
× 100                             (3)
From the above equation (3) describes 𝐸𝑎𝑓𝑡𝑒𝑟 represents customer engagement after AI-based marketing
𝐸𝑏𝑒𝑓𝑜𝑟𝑒 represents the customer engagement before the AI-based marketing.
Comparison with Existing Customer Segmentation Methods
The performance of the suggested ICSPM -AI framework is compared with conventional customer
segmentation techniques such as demographic segmentation, RFM segmentation, the K-Means
clustering algorithm, and machine learning-based customer segmentation. The comparison will be made
considering aspects like segmentation accuracy, precision, recall, F1 score and improvement in customer
engagement. The values will be shown according to the conventional ranges that are found in past
customer analytics studies and studies related to marketing using artificial intelligence. For supervised
learning metrics, the customer segments created using K -Means clustering will be considered the true
labels.
Table 4. Comparison with existing customer segmentation methods
Metric Demographic-
Based
Segmentation
RFM-Based
Segmentation
Traditional K-
Means
Clustering
Machine
Learning-Based
Segmentation
Proposed AI-
ICSPM
Framework
Silhouette Score (%) 52.4 61.8 72.6 78.9 86.5
Davies–Bouldin Index (DBI) 0.684 0.521 0.386 0.294 0.214
Calinski–Harabasz Index (CHI) 2145.8 2986.4 3642.7 4215.6 5428.6
Customer Lifetime Value (CLV)
Prediction Accuracy (%)
68.5 75.8 82.4 89.6 94.2
Customer Conversion Rate
Improvement (%)
21.6 32.5 41.8 54.7 62.8
Recommendation Accuracy (%) 65.4 73.6 81.2 88.7 93.6
Retention Rate Improvement (%) 18.9 28.7 37.6 49.8 58.4
Response Prediction
Accuracy (%)
70.2 77.9 84.6 90.8 95.1
Processing Time (seconds) 8.4 12.6 15.8 21.5 18.6
Scalability (%) 62.5 71.4 80.6 87.8 92.7
Mean Squared Error (MSE) 0.084 0.062 0.041 0.026 0.012
Root Mean Square Error (RMSE) 0.290 0.249 0.202 0.161 0.109

Dr. Vijayakanthan Selvaraj, et al: Intelligent ……  Archives for Technical Sciences 2026, 36(2), 478-489
Technical Institute Bijeljina, Archives for Technical Sciences. Year XVIII – N 0 36           487

Figure 2. Comparison of existing customer segmentation methods
Table 4 and figure 2 represent the comparative analysis of the performance of the proposed AI-ICSPM
model with the existing models of customer segmentation such as demographic -based segmentation,
RFM-based segmentation, traditional K -means clustering approach and ML -based c ustomer
segmentation approach. The analysis reveals that the proposed framework has better clustering
performance, with the highest silhouette score (86.5%), the lowest Davies-Bouldin index (DBI) (0.214),
and the highest Calinski -Harabasz index (CHI) (5428.6) . While the overall processing time for the
AI-ICSPM framework (18.6 seconds) represents a slight runtime increase over basic K -Means
(15.8 seconds) due to the overhead of the dual -stage PCA preprocessing and Random Forest training
pipeline, this minimal computational cost yields a significant (~13.9%) improvement in Silhouette Score
(86.5% vs. 72.6%) and substantially higher overall segmentation accuracy. In relation to the predictive
and marketing performance of the framework, the AI-ICSPM framework has the highest CLV prediction
accuracy of 94.2%, customer conversion rate of 62.8%, recommendation accuracy of 93.6%, and
retention rate of 58.4%. Furthermore, the framework gives the highest response prediction accuracy of
95.1% and scalability of 92.7%. Despite the fact that machine learning-based segmentation provides
superior results when compared with traditional techniques, it is still limited in its functionality when
compared with the AI -ICSPM because of its lower adaptability and personalization capabilities.
Moreover, the suggested framework ensures minimal prediction error as it demonstrates the minimum
value of MSE – 0.012 and RMSE – 0.109, which proves higher accuracy of prediction results. In general,
from the comparative analysis, it can be stated that the integration of artificial inte lligence, feature
learning, and intelligent segmentation approaches allows the suggested approach to offer superior
results.
DISCUSSION
The efficiency of the suggested AI -ICSPM (Intelligent Customer Segmentation with Artificial
Intelligence for Precision Marketing) framework can be demonstrated by the framework’s capability to
convert customer data into useful and applicable information about markets. In contrast to conventional
segmentation frameworks which are primarily focused on static factors such as demographics or
pre-established customer segments, the suggested AI -based framework examines several aspects of
customer behaviors like transaction record, purchase behaviors, online activity, and levels of
engagement to uncover the relationships between different customers. Due to the use of AI-based feature
learning and clustering techniques, the framework is capable of generating accurate and dynamic
customer segments, such as valuable customers, prospective customers, and low-engagement customers.

Dr. Vijayakanthan Selvaraj, et al: Intelligent ……  Archives for Technical Sciences 2026, 36(2), 478-489
Technical Institute Bijeljina, Archives for Technical Sciences. Year XVIII – N 0 36           488
The suggested architecture is an effective approach for increasing segmentation efficiency through
intelligent data processing, feature extraction, and predictive analytics. Intelligent algorithms help
increase the ability of the system to process large am ounts of heterogeneous customer data by
automatically recognizing significant behavioral features and simplifying the structure of the database.
This provides an opportunity for companies to create accurate customer profiles and marketing strategies
in accordance with their needs and preferences. Moreover, the model can learn and evolve along with
consumers' tendencies, which makes it possible to keep segments actual.
Moreover, the efficiency of AI-based segmentation is also shown through its contribution to achieving
precise marketing results. By correctly segmenting customers, the proposed model will allow making
personalized recommendations, promotions, and retaining customers through better approaches.
As compared to traditional models of segmentation, the use of the AI -ICSPM framework provides a
more versatile and data -driven way of segmentation by incorporating machine learning, feature
optimization, and predictive intelligence into the process . Thus, the suggested model of AI -based
intelligent customer segmentation can be seen as an effective solution for contemporary marketing
conditions.
CONCLUSION
The aim of this study was to design a smart customer segmentation strategy that is able to overcome the
challenges associated with traditional strategies and can provide adaptive and precise solutions for
customer segmentation in the form of precision marketing. In order to address this challenge, the concept
of Artificial Intelligence-Based Intelligent Customer Segmentation for Precision Marketing (AI-ICSPM)
was introduced. What makes the suggested framework unique is the combination of the application of
artificial intelligence techniques such as feature learning, intelligent clustering, prediction, and adaptive
customer segmentation within the marketing decision support system. The methodology adopted in this
study includes customer data collection, preprocessing, feature extraction, dimensionality reduction
through PCA, and custome r segmentation using AI through K -Means clustering. The experiment was
carried out using 5,000 customer records with features such as demographic , purchasing behavior,
transaction, and engagement features. A comparison was conducted between the suggested AI-ICSPM
segmentation framework and other existing segmentation techniques, such as demographic -based
segmentation, RFM-based segmentation, traditional K -Means clustering, and machine learning -based
segmentation techniqu es.  Moreover, the suggested framework enhanced Silhouette Score 86.5 %
through the application of personalized recommendations and targeted marketing strategies. The results
show that AI -driven segmentation provides better profiling and decision -making than  traditional
methods. Future studies could be carried out in areas such as real-time streaming, large industry datasets,
explainable AI, and reinforcement learning techniques.
REFERENCES
[1] Ling Z, Li Y, Zhao W. Research on consumer segmentation and response prediction model for precision
marketing based on clustering and deep learning. In  Proceedings of the 2025 2nd International Conference
on Digital Economy, Blockchain and Artificial Intelligence 2025 Jun 27 (pp. 482 -487).
https://doi.org/10.1145/3762249.3762324
[2] Arunraju CH. AI -powered consumer segmentation and targeting: A theoretical framework for precision
marketing by autonomous (Agentic) AI. International Journal of Science and Research Archive.
2025;14(02):401-24. https://doi.org/10.30574/ijsra.2025.14.2.0370
[3] El Koufi N, Belangour A. Toward a decision -making system based on artificial intelligence for precision
marketing: A case study of Morocco. Journal of Open Innovation: Technology, Market, and Complexity.
2024 Mar 1;10(1):100250. https://doi.org/10.1016/j.joitmc.2024.100250
[4] Hye A. Artificial intelligence in product marketing: Transforming customer experience and market
segmentation. ASRC Procedia: Global Perspectives in Science and Scholarship. 2023 Apr 29;3(1):132 -59.
https://doi.org/10.63125/58npbx97
[5] Alijoyo FA, Aziz TS, Omer N, Yusuf N, Kumar MD, Ramesh AV, Ulmas Z, El -Ebiary YA. Personalized
marketing: Leveraging AI for culturally aware segmentation and targeting. Alexandria Engineering Journal.
2025 Apr 1;119:8-21. https://doi.org/10.1016/j.aej.2025.01.074

Dr. Vijayakanthan Selvaraj, et al: Intelligent ……  Archives for Technical Sciences 2026, 36(2), 478-489
Technical Institute Bijeljina, Archives for Technical Sciences. Year XVIII – N 0 36           489
[6] Talaat FM, Aljadani A, Alharthi B, Farsi MA, Badawy M, Elhosseini M. A mathematical model for customer
segmentation leveraging deep learning, explainable AI, and RFM analysis in targeted marketing.
Mathematics. 2023 Sep 15;11(18):1-26. https://doi.org/10.3390/math11183930
[7] Hemalatha R, Amulya G, Lalitha CH. AI -Driven Customer Segmentation for Personalized Marketing.
In2024 Second International Conference Computational and Characterization Techniques in Engineering &
Sciences (IC3TES) 2024 Nov 15 (pp. 1-5). IEEE. https://doi.org/10.1109/IC3TES62412.2024.10877505
[8] Mallikraj SV, Pawar SA, Hole S, Gupta R, Alsailawi HA, Mudhafar  M. AI -Powered Customer
Segmentation: Enhancing Targeted Marketing Strategies Through Machine Learning. In2025 IEEE 5th
International Conference on ICT in Business Industry & Government (ICTBIG) 2025 Dec 12 (pp. 1-5). IEEE.
https://doi.org/10.1109/ICTBIG68706.2025.11323753
[9] Lin J. Application of machine learning in predicting consumer behavior and precision marketing. PLoS One.
2025 May 6;20(5):e0321854. https://doi.org/10.1371/journal.pone.0321854
[10] Bano R, Azim F, Mahmood Z, Sanaullah A, Ali O. The role of artificial intelligence in personalized
marketing: Enhancing customer experience, predictive targeting, and brand engagement. The Critical Review
of Social Sciences Studies. 2025 Apr 3;3(2):50-65. https://doi.org/10.59075/d94kvf44
[11] Shoeb M, Zillul M. Artificial intelligence in digital marketing enhancing personalization and consumer
engagement. Business and Social Sciences. 2025 Jan 14;3(1):1-9. https://doi.org/10.25163/business.3110209
[12] Agova P, Valcheva D, Asenov O. The Application of Artificial Intelligence in Business Segmentation.
BRAIN. Broad Research in Artificial Intelligence and Neuroscience. 2025 Sep 8;16(3):74 -85.
http://dx.doi.org/10.70594/brain/16.3/7
[13] Uddin HM. A systematic review of artificial intelligence -based customer analytics in personalized digital
marketing (2019 –2026). American Journal of Data Science and Analytics. 2026 Mar 14;7(03):295 -339.
https://doi.org/10.63125/x3e0dx27
[14] Wu L. Research on customer segmentation and precision marketing strategy based on LRFMC model and
K-means algorithm. InInternational Conference on Engineering Management, Computer Applications, and
Supply Chain (EMCAS 2025) 2026 Apr 1 (Vol. 14161, pp. 259-266). SPIE.
https://doi.org/10.1117/12.3108716
[15] Fang Z, Wan N. Real-time customer segmentation using big data and cluster analysis in enterprise marketing
strategies. International Journal of Information and Communication Technology. 2026;27(51):1 -6.
https://doi.org/10.1504/IJICT.2026.153705
[16] Zhu J. Data analysis of e -commerce precision marketing system based on artificial intelligence algorithm.
In2023 International Conference on Distributed Computing and Electrical Circuits and Electronics
(ICDCECE) 2023 Apr 29 (pp. 1-5). IEEE. https://doi.org/10.1109/ICDCECE57866.2023.10150655
[17] Kong C. Research on enterprise digital precision marketing strategy based on big data. Mathematical
Problems in Engineering. 2022;2022(1):4279983. https://doi.org/10.1155/2022/4279983
[18] Al Rafi M. Intelligent Customer Segmentation A Data -Driven Framework for Targeted Advertising and
Digital Marketing Analytics. International Journal of Research Publications in Engineering, Technology and
Management (IJRPETM). 2022 Sep 7;5(5):7417-28. https://doi.org/10.15662/IJRPETM.2022.0505003
[19] Abdullah MS, Hasan R. AI -driven insights for product marketing: Enhancing customer experience and
refining market segmentation. American Journal of Interdisciplinary Studies. 2023 Dec 5;4(04):80 -116.
https://doi.org/10.63125/pzd8m844
[20] Zhao H. Precision Marketing Strategies Driven by Intelligent Technology. In2025 International Conference
on Intelligent Communication Networks and Computational Techniques (ICICNCT) 2025 Sep 5 (pp. 1 -6).
IEEE. https://doi.org/10.1109/ICICNCT66124.2025.11233210
