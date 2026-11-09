---
title: Generative AI for Personalized Marketing and Customer Experience in E-Commerce
url: https://doi.org/10.63282/3050-922x.ijeret-v7i1p103
category: ai-marketing
subcategory: empirical
date: 2026-01
venue: International Journal of Emerging Research in Engineering and Technology
authors:
- Chetankumar Patel
source: openalex-oa
pdf_url: https://ijeret.org/index.php/ijeret/article/download/406/387
pages: 8
chars: 35221
fetched_at: '2026-11-08T13:42:09+00:00'
kb_version: 1
---

# Generative AI for Personalized Marketing and Customer Experience in E-Commerce

International Journal of Emerging Research in Engineering and Technology
Pearl Blue Research Group| Volume 7 Issue 1 PP 12-19, 2026
ISSN: 3050-922X | https://doi.org/10.63282/3050-922X.IJERET-V7I1P103

Original Article

Generative AI for Personalized Marketing and Customer
Experience in E-Commerce

Chetankumar Patel
Independent Researcher.

Received On: 18/11/2025            Revised On: 22/12/2025             Accepted On: 29/12/2025             Published On: 06/01/2026

Abstract - E-commerce has fast become one of the major
components of the worldwide online economy. It has
positively affected the relationship between the business and
the customer through the application of data and AI. At the
same time, changing customer needs have  turned
understanding their preferences and offering them
customized service into a major barrier to competitiveness.
The study is focused on building an effective brand loyalty
model that is able to not only support but also facilitate
personalized marketing and customer service. The procedure
is implemented using the E -Commerce Customer Dataset
from Kaggle and involves a series of steps that include data
cleaning, feature selection, and exploratory visualization
through correlation and distribution analys es. Among the
evaluated features, Satisfaction Score is found to be a crucial
determinant of customer engagement and loyalty. The
suggested Generative Adversarial Networks (GANs) model
was trained, tested, and compared to several baseline
machine learning (ML) methods such as Logistic Regression
(LR), Random Forest (RF), and Naïve Bayes (NB).  The GAN
demonstrated its effectiveness in discovering sequential
patterns and long -term relationships in behavioral data with
95.79% accuracy (ACC), 93.8% precision (PRE), 92% recall
(REC), and 92% F1-score (F1) attained, surpassing all other
models.  The results show that GAN and other deep learning
techniques outperform the standard models, making them
useful tools for e -commerce platforms' predictive analytics,
tailored marketing, and customer retention tactics.

Keywords - E-commerce, Customer Behavior Prediction,
Personalized Marketing, Generative Adversarial Networks
(GANs), Machine Learning, Customer Experience, Data
Analytics, Predictive Modeling.

1. Introduction
The e-commerce industry has grown at a very fast pace
during the recent past, and this was mainly because of
technology breakthroughs, changing consumer tastes, and
more customers using online payment options [1][2]. On the
other hand, as rivalry grows, firms have to come up with new
ideas all the time to keep customers, improve their processe s,
and extract the most profit from their investments. Generative
AI is one of the industry's most revolutionary technologies,
allowing firms to turn huge data sets into information with
ease, perform even the most intricate tasks, and give
customers the m ost personalized shopping experience ever
[3][4]. E -commerce has these challenges to analyze raging
purchasing intent and to create the relevant and customized e-
commerce solutions that are delivered through the right
channels [5][6]. Buyer in tent modelling and mapping are the
foundations of the establishment of stronger e -commerce
platforms and marketing campaigns  [7]. The operators of
electronic commerce sites are aware that the customer
experience plays a vital role in the time consumed, the
percentage of purchases made, loyalty/reward programs, and
the overall income of the business.

The most efficient method for maintaining an e -
commerce platform that works is to be very acquainted with
the customers’ behaviour, needs, preferences, and demands as
they interact with the platform [8]. The whole customer
experience is made up of a business’s every asp ect. The
quality of customer service is one significant factor but it is
also crucial to pay attention to the product’s promotion,
packaging, features, dependability, and user -friendliness [9].
By offering remarkably pleasant experiences throughout the
customer journey so that they are better than the competitors’,
customer loyalty can be built and the likelihood of customers
telling their acquaintances about the platform can be
increased [10][11]. Personalized marketing and ML, two
branches of AI, have been growing in popularity at the same
time. ML allows computers to adapt and learn from data. Out
with the traditional marketing strategies that relied on wide
campaigns and general appeal through the modern,
customized approaches.

The term "e-commerce personalization" is the practice of
making a customer's online purchasing experience unique by
taking into account their demographics, interests, and
activities.  Actually, this idea has come a long way in the last
several years, mostl y because of the widespread application
of AI and ML [12][13]. The application of AI, indeed, has
opened up new avenues of operation in the online store
domain such that the very strong technology of generative AI
has been the one that has really reversed the whole
relationship between firms and consumers. Generative AI has
been the most significant technology among others and is
altering the customer experience at every point in the process
from bespoke recommendations and chatting support to smart
reviews' usage [14][15]. Generative AI is a combination of
ML techniques that provide the capability of creating
completely new content, making accu rate predictions

Chetankumar Patel / IJERET, 7(1), 6-13, 2026

13
regarding future trends, and automating the decision -making
process. Generative AI is causing a sea change in the way
online retailers connect with their customers and make
money. This technology has several applications, including
chatbots driven by AI, automated content production,
dynamic pricing, and personalized product recommendations
[16][17]. In e-commerce, this paper discusses how generative
AI transforms traditional personalized marketing strategies
and improves customer experience through the adoption of
intelligent automation, predictive modelling, and content
generation.

1.1. Motivation and Contribution
The paper's motivation is caused by the increasing
requirement for e -commerce firms to provide very
personalized and engaging customer interactions in an already
crowded, data -driven market. The traditional marketin g
tactics based on wide segmentation have become out -of-date
and thus cannot provide the modern consumers with the
relevance and personalization that they expect. Generative AI
proposes a very drastic change through content creation,
predicting customer behaviour, and personalizing on a larger
scale. By adopting smart auto and machine learning, e -
commerce companies can raise customer satisfaction levels,
fine-tune and increase the efficiency of their marketing
strategies, and thus have a higher conversion r ate. It is the
redefining of personalized marketing and customer
experience through generative AI in the fashion of the ever -
changing digital commerce landscape that this paper seeks to
study. The research contributes the following major points
which are outlined below:
 Developed a structured machine learning framework
for predicting customer behaviour and applying
personalized marketing to e -commerce using real -
world data.
 An optimized pre -processing pipeline has been
implemented, which includes various ta sks such as
handling missing values, removing outliers,
encoding, normalizing, and selecting features, all
aimed at improving the performance of the model.
 A team working on optimizing customer experience
has proposed and rigorously tested a Gen AI based
Generative Adversarial Networks (GANs) model
which, by capturing sequential dependencies, could
enhance the customer churn prediction ACC.
 An extensive model evaluation using main
performance measures like ACC, PRE, REC, and F1
was conducted to confirm the efficacy and
credibility of the suggested strategy.

1.2. Organization of the Paper
The paper is structured in a way to guide the reader
through the different sections easily: related work on
personalized marketing and customer experience prediction is
reviewed in Section II, the dataset, pre -processing steps, and
model implementation are described in Section III, Section IV
contains the experimental results and a comparative analysis;
the study is concluded in Section V by highlighting the key
conclusions and making recommendations for further study.

2. Literature Review
To provide a solid theoretical framework and direction
for the current investigation, a thorough analysis of previous
studies on personalized marketing and customer experience
prediction was carried out.  Manoharan et al. (2025) The
study's main goal is to discover how ML techniques might be
applied to forecast annual spending, customer attrition, and
the timely delivery of online purchases. The research study
has reached a decision that ML techniques are very useful for
predicting the attrition and retention of e -commerce
customers. The main model, gradient boosting, managed to
reach a remarkable 90.67% ACC in forecasting the departure
of customers and 73.75% in forecasting the delivery of a
product on time [18].

Xu (2025) basically focuses on consid ering K -means
clustering as a PRE marketing strategy applied to online
marketplaces. The experiment results showed a huge increase
in ACC by 98.2%, F1 grew to 97.7%, and quality of
segmentation was also improved. Comparative evaluation
shows that K-means is much better than the old models in the
aspects of PRE and REC. The model's outstanding
performance is credited to its unsupervised learning feature
that enables it to automatically reveal hidden patterns that can
be scaled and are data -driven, thus easy to use in improving
e-commerce marketing performance [19].

Kumar et al. (2025) This study was focused on customer
behaviour and the internet buying pro cess. Among the major
advantages of using AI in e -commerce, the capability to
customize user experiences on e -commerce platforms stands
out as the most important one. The AI model surpassed
LSTM and CNN in terms of performance, being trained with
CNN and Convolutional LSTM according to the key criteria.
It dispenses personalized insights and recommendations with
a mean ACC of 92.03%. AI -driven personalization has
changed the whole e -commerce landscape by giving
personalized experiences and product recommendations [20].

Arul Mary Rexy  et al. (2024) investigate Predictive
analytics' potential effects on e-commerce customers' privacy.
Specifically, it considers the combination of K -Means
clustering and a single BERT -CNN-A-BiGRU model to
improve the prediction ACC. The suggested solution exceeds
the best -performing methods and reaches the ACC level of
98.30%. The increase in ACC indicates how the suggested
method can be very helpful in dealing with privacy issues
related to the use of e-commerce predictive analytics [21].

Zulfadli, Ilham and Indrabayu (2023) The primary
objective is to develop a sentiment analy sis algorithm that
evaluates consumer opinions in online product evaluations.
The dataset used for evaluation is that of Tokopedia's product
reviews. The findings demonstrate that the SV model is better
than the SS approach.  A 69% ACC rate, 70% PRE rate, 69%
REC rate, and 69% f1 are all achieved by the suggested SV
model [22].

Masroor et al. (2023) forecast customer churn for a ride -
sharing application by training appropriate supervised

Chetankumar Patel / IJERET, 7(1), 6-13, 2026

14
ensemble-based machine learning models on customer
attributes as well as their loyalty to the application. Gradient
Boost and Cat Boost algorithms perf ormed the best in
identifying potential churning customers, with AUC -ROC
scores of 0.85 and computation times of 58 seconds and 80
seconds, respectively, while XG Boost was not far behind
with an AUC-ROC score of 0.84 and the fastest computation
time of 45 seconds among all models assessed [23].
Table I gives a summary of the latest studies regarding
the application of AI in personalized marketing and customer
experience prediction, and it indicates the models that were
proposed, the dataset used, the main conclusions drawn by the
researchers, and the difficulties met.

Table 1: Recent Studies on Personalized Marketing and Customer Experience Prediction Using Artificial Intelligence
Author(s)
& Year
Proposed Work Techniques Dataset Results Key Findings Limitations &
Future Work
Manoharan
et al. (2025)
Investigated the
use of ML
methods to predict
e-commerce
product on-time
delivery, annual
spending, and
customer attrition
KNN, Naive
Bayes,
Gradient
Boosting
E-commerce
transaction
dataset
Gradient
Boosting
achieved
90.67%
accuracy for
customer
attrition and
73.75% for
on-time
delivery
ML techniques
are effective for
forecasting
attrition and
delivery outcomes
in e-commerce
Future work may
explore hybrid
models and larger
datasets for
improved
prediction
accuracy
Xu (2025) Utilized K-Means
clustering to
enhance e-
commerce client
segmentation and
optimize precision
marketing
K-Means
Clustering
Customer
behavioral
dataset from
e-commerce
platform
Accuracy:
98.2%, F1-
score: 97.7%
K-Means
effectively
segments
customers,
enabling targeted
marketing
campaigns
Integration with
dynamic behaviour
analysis and other
unsupervised
learning methods
can be explored
Kumar et al.
(2025)
Developed CNN
and Convolutional
LSTM-based AI-
driven
customization to
comprehend online
purchasing
patterns
CNN,
ConvLSTM
Online
customer
behaviour
dataset
Average
accuracy:
92.03%
AI personalization
enhances user
experience and
provides deeper
behavioural
insights
Future research
can include multi-
modal data and
real-time
personalization
techniques
Arul Mary
Rexy et al.
(2024)
Investigated
predictive
analytics with K-
Means and unified
BERT-CNN-A-
BiGRU model
focusing on
consumer privacy
K-Means,
BERT-CNN-
A-BiGRU
Hybrid
Model
E-commerce
systems'
predictive
analytics
dataset
Accuracy:
98.3%
Achieved high
accuracy while
addressing
privacy concerns
in predictive
analytics
Future studies may
emphasize
privacy-preserving
techniques and
ethical AI
frameworks
Zulfadli,
Ilham &
Indrabayu
(2023)
Developed an
ensemble learning-
based sentiment
analysis model for
online product
reviews.
Soft Voting
(SVM, RF,
NB)
Tokopedia
Product
Review
Dataset
Accuracy:
69%,
Precision:
70%, Recall:
69%, F1-
score: 69%
Soft Voting
ensemble
outperformed the
Sentiment
Selector model
Model
performance could
be enhanced using
deep NLP models
and larger review
datasets
Masroor et
al. (2023)
Forecasted
customer churn in
ride-sharing
applications using
ensemble ML
models
Gradient
Boost,
CatBoost,
XGBoost
Ride-sharing
customer
dataset
Gradient
Boost AUC-
ROC: 0.85,
CatBoost:
0.85,
XGBoost:
0.84
Ensemble models
effectively
identify potential
churners in
imbalanced
datasets
Incorporating
temporal features
and real-time
churn prediction
can improve
applicability

Chetankumar Patel / IJERET, 7(1), 6-13, 2026

15
3. Research Methodology

Fig 1: Proposed Flowchart for Personalized Marketing
and Customer Experience Prediction

An accurate model for forecasting E -commerce client
behaviour shall be established as the purpose of the study. It
focuses on enhancing personalized marketing strategies and
improving customer experience through data -driven insights.
The methodology for implementing the GAN model on the e-
commerce customer dataset follows a structured machine
learning pipeline, beginning with data pre -processing, as
discussed below in Figure 1.

In the section that follows, and lay out the recommended
methodology step by step:
3.1. Data Gathering and Analysis
The "E-commerce Customer" dataset has been analyzed
as a key factor in this study. The dataset has been obtained
from Kaggle. This study uses a dataset of e -commerce
behaviour data from a multi -category business from October
2019 to Apri l 2020. The dataset consists of 4 numeric
variables which are Event -time, Product-id, Category-id, and
Price. Below are given data visualizations such as bar plots
and heatmaps that were used for examining attack
distribution, feature correlations, etc.:

Fig 2: Correlation Analysis

The Figure 2 illustrates a heatmap Correlation Analysis,
revealing the pairwise relationships among the major
variables in the dataset. The colour scale from dark red to
dark blue denotes strong positive to strong negative
correlations, respectively. It is important to mention that
price_1 and actprice1 present a very high positive correlation,
while Rating is positively correlated with high star ratings and
negatively with low ones. This heatmap offers an easy -to-
understand picture of feature interdependencies, thus helping
in pinpointing the main predictors and directing the feature
selection process for model development

Fig 3: Distribution Plots

In Figure 3, there are 16 bar charts that depict the
distribution of important variables concerning customers,
such as demographics and behavioural characteristics. The
different charts present the number of occurrences for
features like tenure, city tier,  satisfaction score, app usage,
and order activity. Customer Satisfaction Score is one of the
most powerful features, illuminating customer engagement
and loyalty. The charts prove to be a compact and clear
representation of the different customer types an d their
changes which can be applied for the purpose of exploratory
data analysis.

3.2. Data Pre-processing
The dataset of e -commerce customers was used for the data
preparation process which included merging of data, cleaning,
Data preprocessing
Remove
Duplicates
Remove outliers
Normalization
(StandardScaler)
One-Hot Encoding
Data splitting
Training
 Testing
E-Commerce
Customer Dataset
from Kaggle
Feature Selection
Results
Implementation
using Generative
Adversarial
Networks
(GANs)Model
Model evaluation
accuracy, precision,
recall, f1 score

Handle missing
value

Chetankumar Patel / IJERET, 7(1), 6-13, 2026

16
and feature extraction. Th e pre-processing activities included
making the missing values, ending duplicate and outlier
records, and performing label encoding and normalization on
the data. The main methods of pre-processing are enumerated
below:
 Handle missing value:  The handling o f missing
values involves the utilization of various methods to
tackle the problem of data points that are not present
in a dataset, which could be in the form of empty
cells, null entries, or indicators like "NA," thereby
securing the PRE and trustworthin ess of data
evaluation and machine learning models [24].
 Remove Duplicate:  "Remove duplicates" refers to
the process of pinpointing and getting rid of data that
are either identical or nearly identical, with the aim
of attaining the quality and productivity of the data
used.
 Remove outliers:  Outlier removal is the act of
spotting and then either getting rid of or  altering the
data points that are highly dissimilar to the largest
part of the data in a dataset.

3.3. One-Hot Encoding For Data Encoding
The process of data encoding refers to turning
information into a designated format for various purposes,
such as t ransmission, storage, or analysis, making sure that
the corresponding data is easily and effectively handled by
computers and algorithms. To convert categorical input into a
numerical representation that ML models can comprehend,
one-hot encoding is a ML technique.

3.4. Normalization (Standard Scaler)
The dataset was normalized employing the
StandardAero() method to adjust the data such that the mean
of the resulting distribution is 0 and the standard deviation is
1 [25]. The method described in Equation (1) is used to
perform this transformation, where each observation's mean
value is deducted and the standard deviation is used to divide:

  (1)

The attribute's changed value (z), the attribute's initial
value (x) for each descriptor, the average (μ) , and the
attribute's standard deviation (σ) from the dataset.

3.5. Feature Selection
Feature selection is the technique of identifying and
picking the most important input variables (features) from the
data set to improve the result, reduce the complexit y, and
make the ML model more interpretable. In data pre -
processing, feature selection is the choice of a subset of
relevant features (variables, predictors) from a data set to be
applied in the model -building process. This process aims to
increase model p erformance by reducing dimensionality,
enhancing interpretability, and also dealing with issues like
overfitting.

3.6. Data Splitting
The same data set is used to construct a training set and a
testing set, which are then used to train the models and assess
their performance, respectively. The division ratio is such that
70% of data is assigned for training and 30% for testing.

3.7. Proposed Generative Adversarial Networks (GANs)
Model
In machine learning modeling, Generative Adversarial
Networks (GANs) have advanced. In order to distinguish
between artificial and genuine data, this machine learning
technique uses discriminating networks. GANs behave in a
way that allows them to learn th e joint distribution of the
entire dataset, in contrast to traditional machine learning
techniques. The Generator (G) and Discriminator (D) neural
networks are the two neural networks used by GANs. In order
to create synthetic data that closely resembles t he real data,
the G is used to input a random noise vector. Simultaneously,
the D's goal is to take actual samples and function as a teacher
who can assess the output's performance and determine if the
data are authentic or fraudulent. The Min –Max game is used
to teach both G and D such that G's losses are kept to a
minimum and D's losses are maximized. The function of
GAN is given below in Equation (2):
         (   )        ( )        ( )        (
 ( ( )))    ( )     (2)

The noise " z" is created at random, and "G(z)" shows
how "G" tries to learn a distribution PG from the distribution
of noise "Pz," bringing "PG" closer to the distribution of real-
world data, represented by "P" data. Furthermore, the
Discriminator tries to verify if the sample is authentic or
fraudulent.

3.8. Evaluation Metrics
PRE, REC, ACC, and F1 were among the measures used to
assess the models' performance and the test set's product
suggestion prediction. For a classification task, a confusion
matrix summarizes the results of the predictions. The
predictions are categorized according to whether they were
correct or erroneous. Two possible outcomes are represented
by the symbols TP and FP, respectively, for TP and FN, and
by the symbols FN and TN, for true negativ es.  Where, as
described below:
Accuracy: The percentage of instances in the dataset (input
samples) that the trained model correctly predicted as a
function of the total number of instances. It is given as
Equation (3)-

            (3)

Precision: A model's predictive ACC is the proportion of true
positives in relation to all TP. the ACC of the classifier's
positive class predictions is given by Equation (4)-

      (4)

Recall: This metric depicts the proportion o f positive
occurrences that were correctly predicted to all positive
occurrences. The formula for it in mathematics is Equation
(5)-

      (5)

Chetankumar Patel / IJERET, 7(1), 6-13, 2026

17
F1 score: The combination of REC and PRE strikes a balance
between the two, making it a harmonic mean. Between zero
and one is its range. According to Equation (6)-

                  (6)

The key evaluation metrics used and applied in the following
results are ACC, PRE, REC, and F1 below:

4. Results and Discussion
The experimental setup is shown in this section and the
performance analysis of the proposed GAN model utilizing
the E-Commerce Customer Da taset. Table II shows that the
model was tested with crucial metrics including F1, REC,
ACC, and PRE.  The implementation made use of Scikit -
learn.  A 95.79% ACC rate, 93.8% PRE rate, 92% REC rate,
and 92% F1 for the GAN model demonstrate its reliability
and the well -balanced Ness of its predictions for consumer
behaviour in relation to targeted marketing and improved
customer experience.

Table 2: Classification Results of the Proposed Model
Using E-Commerce Customer Dataset
Matrix GAN Model
Accuracy 95.79
Precision 93.8
Recall 92
F1-score 92

Fig 4: GAN  Model Accuracy Graph

The training and validation ACC curves of the GAN
model over 20 epochs are shown in Figure 4. ACC curves for
both training and validation have been steadily increasing,
suggesting that the model is getting better at learning with
each cycle.  Starting at a round 0.75 and gradually increasing
to around 0.96 is the training ACC, whereas starting at around
0.72 and ending at around 0.94 is the validation ACC. The
closeness of both curves in the last epochs is an indication
that the model can apply the patterns it has learnt from the
training data to fresh data, thereby exhibiting minimal
overfitting and stable learning behaviour.

Fig 5: GAN Model Loss Graph

Figure 5 illustrates the loss curves for both training and
validation of the GAN model throughout the 20 epochs. The
model error is shown to consistently decrease throughout the
training process, as both curves have a downward trend. The
training loss (blu e line) has a rapid drop in the beginning
epochs, and then it continues to fall smoothly, reaching a
point close to 0.1, where it is somewhat stabilized. On the
other side, the validation loss (red line) has a remarkable
decrease, ending at around 0.18, wi th very little change in
between epochs, by the last epoch. The neighbouring position
of the two curves is indicative of good model generalization
and effective learning without any hint of overfitting.

4.1. Comparative Analysis
Table III shows the result s of a performance comparison
that was conducted to evaluate the suggested GAN model.
The goal was to find out how effective the model was.
Performance-wise, the best among the assessed models was

Chetankumar Patel / IJERET, 7(1), 6-13, 2026

18
MLP, which got 70.3% ACC, LR, which got 90% and KNN,
which got 81.9%. With its highest ACC of 95.79%, the
proposed Generative Adversarial Networks (GANs) model
beat all and came next with 93.8% PRE, 92% REC, and 92%
F1, thus, proving its excellent ability for predicting
personalized marketing outcomes and improvin g customer
experience.

Table 3: Comparison of Different Machine and DEEP
Learning Based on Customer Experience Prediction
Model Accuracy Precision Recall F1-
score
MLP[26] 70.30 78.10 76 77
LR[27] 90 82 50 62
KNN[28] 81.9 67.2 51.1 47.7
GAN 95.79 93.8 92 92

GAN is a powerful method that practically dominates all
the others regarding its capability of learning, handling of
sequential data, and generalization, due to its very good
performance. The very feature of learning temporal
dependencies makes it possible for the customers' behavior
patterns to be ascertained more accurately and thus, using the
obtained data for predicting marketing outcomes personalized
for customers to be more effective. The model, moreover, is
not just predictably good across the major metrics but also, in
fact, less erroneous and, thus, absolutely dependable and
stable in terms of the results produced for the improvement of
customer engagement and experience.

5. Conclusion and Future Study
E-commerce, owing to the digital transformation,
changes in customer behaviour, and the rising use of smart
systems, has become the fastest -growing and most dynamic
industry. The companies that decide to win the customer
engagement battle by offering personalization will find it
inevitable to detect and predic t customer preferences. The
study is one such project and intends to make a contribution
by using ML and DL techniques for predicting customer
behaviour via the E -Commerce Customer Dataset. The GAN
model has achieved a stunning ACC of 95.79%, thus
outdoing simpler models such as LR, KNN, and MLP. Its
exceptional performance across PRE, REC, and F1 metrics
attests to the fact that it is capable of not only discovering and
giving birth to novel marketing strategies based on customer
behaviour patterns but also encouraging them. Expanding this
study to incorporate real -time consumer data is one potential
avenue for future research, the addition of other behavioural
and contextual variables, and the exploration of more
sophisticated architectures such as transfo rmer-based or
hybrid models. Also, the integration of the model into
recommendation systems and customer segmentation
strategies could result in improved scalability and flexibility,
thus enabling companies to provide more accurate and
engaging customer ex periences in a digital marketplace that
gets more and more competitive every day.

References
[1] M. S. Raisinghani, “E -Pricing for Intelligent
Enterprises,” in Intelligent Enterprises of the 21st
Century, 2011. doi: 10.4018/978-1-59140-160-5.ch015.
[2] A. Parupalli and H. Kali, “Leveraging ML for Business
Forecasting in ERP -Enabled E -commerce
Environments,” ESP J. Eng. Technol. Adv. , vol. 4, no. 3,
2024, doi: 10.56472/25832646/JETA-V4I3P120.
[3] L. Yang and S. Hamori, “S ystemic risk and economic
policy uncertainty: International evidence from the
crude oil market,” Econ. Anal. Policy , vol. 69, pp. 142 –
158, 2021, doi: 10.1016/j.eap.2020.12.001.
[4] P. Mehrotra et al., “Price Investment using Prescriptive
Analytics and Optimization in Retail,” in Proceedings of
the ACM SIGKDD International Conference on
Knowledge Discovery and Data Mining , 2020. doi:
10.1145/3394486.3403365.
[5] C. Patel, “Integration of AI in Customer Relationship
Management (CRM) for Improved Sales Outcomes,”
Int. J. Emerg. Res. Eng. Technol. , vol. 6, no. 4, pp. 137 –
145, 2025, doi: 10.63282/3050 -922X.IJERET-
V6I4P117.
[6] V. Varma, “Data Analytics for Predictive Maintenance
for Business Intelligence for Operational Efficiency,”
Asian J. Comput. Sci. Eng., vol. 7, no. 4, 2022.
[7] S. B. V. Naga, S. Thangavel, S. K. Kuchoor, N.
Narukulla, and L. K. Yenduri, “Optimizing Online
Marketing Strategies With Machine Learning and Deep
Learning Innovations,” in Impact of Digital
Transformation on Business Growth and Performance ,
2025, pp. 483 –512. doi: 10.4018/979 -8-3693-9783-
1.ch018.
[8] T. Kumar and V. Shah, “Leadership in digital
transformation: Enhancing customer value through AI -
driven innovation in financial services marketing,” Int.
J. Sci. Res. Arch., vol. 15, no. 3, pp. 618–627, Jun. 2025,
doi: 10.30574/ijsra.2025.15.3.1767.
[9] M. Zhou et al., “Understanding consumers’ behavior to
adopt self-service parcel services for last -mile delivery,”
J. Retail. Consum. Serv. , 2020, doi:
10.1016/j.jretconser.2019.101911.
[10] C. Meyer and A. Schwager, “Understanding customer
exprience,” 2007.
[11] S. Jain, M. Sundström, and J. Peterson, “Mass
Customized Fashion : Importance of Data Sharing in the
Supply,” Nord. Retail Wholes. Conf. Reykjavík, 2018.
[12] B. R. R. Reddy and R. L. Kumar, “A Fusion Model for
Personalized Adaptive Multi -Product Recommendation
System Using Transfer Learning and Bi-GRU,” Comput.
Mater. Contin., vol. 81, no. 3, pp. 4081–4107, 2024, doi:
https://doi.org/10.32604/cmc.2024.057071.
[13] H. P. Kapadia and K. C. Chittoor, “AI Chatbots for
Financial Customer Service: Challenges & Solutions,” J.
Adv. Futur. Res., vol. 2, no. 2, p. 7, 2024.
[14] R. Arora, “Leveraging Generative AI in E -commerce:
Enhancing Customer Experience from Conversation to
Reviews,” Int. J. Multidiscip. Res., vol. 6, no. 5, pp. 1–8,
2024, doi: 10.36948/ijfmr.2024.v06i05.25833.
[15] S. P. Kalava, “Revolutionizing Customer Experience:
How CRM Digital Transformation Shapes Business,”
Eur. J. Adv. Eng. Technol., p. 4, 2024.
[16] M. Mussi, G. Genalti, A. Nuara, F. Trovó, M. Restelli,
and N. Gatti, “Dy namic Pricing with Volume Discounts

Chetankumar Patel / IJERET, 7(1), 6-13, 2026

19
in Online Settings,” in Proceedings of the 37th AAAI
Conference on Artificial Intelligence, AAAI 2023 , 2023.
doi: 10.1609/aaai.v37i13.26845.
[17] T. Shah, “The Role of Customer Data Platforms (CDPs)
in Driving Hyper -Personalization in FinTech,” Int. Res.
J. Eng. Technol., vol. 12, no. 04, p. 10, 2025.
[18] G. Manoharan, R. Gupta, B. B, V. V. Darunkar, S. K.
Mishra, and M. Soni, “The impact of Artificial
Intelligence on E -commerce Customer Experience and
Personalization,” in 2025 6t h International Conference
for Emerging Technology (INCET) , 2025, pp. 1 –5. doi:
10.1109/INCET64471.2025.11140097.
[19] M. Xu, “Data -Driven Customer Segmentation in E -
Commerce using K -Means Clustering for Personalized
Marketing Strategies,” in 2025 3rd Internati onal
Conference on Data Science and Information System
(ICDSIS), 2025, pp. 1 –8. doi:
10.1109/ICDSIS65355.2025.11071130.
[20] G. Kumar, G. Devayani, C. Saraswathi, R. Melba Kani,
S. Dongre, and M. S. M. Mallick, “Exploring Consumer
Behavior in E -Commerce with AI  Personalization and
Market Trends Analysis Models,” in 2025 3rd
International Conference on Integrated Circuits and
Communication Systems (ICICACS) , 2025, pp. 1 –6. doi:
10.1109/ICICACS65178.2025.10967904.
[21] V. A. M. Rexy, S. Venkatesan, P. Ravisankar, and N .
Kalaivani, “BERT -CNN-A-BiGRU Approach for
Predictive Analytics in E -commerce,” in 2024 2nd
International Conference on Self Sustainable Artificial
Intelligence Systems (ICSSAS) , 2024, pp. 114 –119. doi:
10.1109/ICSSAS64001.2024.10760980.
[22] Zulfadli, A. A. I lham, and Indrabayu, “Sentiment
Analysis with Soft -Voting Method on Customer
Reviews for Purchasing Transactions of E -Commerce,”
in 2023 IEEE International Conference on Industry 4.0,
Artificial Intelligence, and Communications Technology
(IAICT), IEEE, Ju l. 2023, pp. 295 –299. doi:
10.1109/IAICT59002.2023.10205954.
[23] M. I. Masroor, K. M. Sadman Sakib, M. Hasan, M. A.
Al Arman, P. Dey, and T. F. Sanam, “Ensemble based
Machine Learning Approach for Predicting Customer
Churn in E -Commerce,” in 2023 26th International
Conference on Computer and Information Technology,
ICCIT 2023 , 2023. doi:
10.1109/ICCIT60459.2023.10441468.
[24] K. M. R. Seetharaman, “Digital Transformation in Retail
Sales: Analyzing the Impact of Omni-Channel Strategies
on Customer Engagement, ” J. Glob. Res. Math. Arch. ,
vol. 10, no. 12, 2023, doi: 10.5281/zenodo.15280578.
[25] V. Verma, “LSTM -based to Predicting Stock Market
Trends Using Machine Learning and Sentiment
Analysis,” vol. 8, no. 3, pp. 102–111, 2021.
[26] R. Akshara, S. K. Reddy, and A. Jain, “Leveraging Deep
Learning to Forecast E -Commerce Product Fulfillment,”
SSRG Int. J. Electron. Commun. Eng. , vol. 12, no. 5, pp.
118–125, 2025, doi: 10.14445/23488549/IJECE -
V12I5P110.
[27] P. A. Sunarya, U. Rahardja, S. C. Chen, Y. M. Li, and
M. Hardini, “Deci phering Digital Social Dynamics: A
Comparative Study of Logistic Regression and Random
Forest in Predicting E -Commerce Customer Behavior,”
J. Appl. Data Sci. , vol. 5, no. 1, pp. 100 –113, 2024, doi:
10.47738/jads.v5i1.155.
[28] M. Loukili, F. Messaoudi, and M. E l Ghazi, “Sentiment
Analysis of Product Reviews for E -Commerce
Recommendation based on Machine Learning,” Int. J.
Adv. Soft Comput. its Appl. , vol. 15, no. 1, pp. 1 –13,
2023, doi: 10.15849/IJASCA.230320.01.
