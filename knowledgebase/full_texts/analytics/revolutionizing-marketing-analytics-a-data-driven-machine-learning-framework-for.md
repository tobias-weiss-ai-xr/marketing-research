---
title: 'REVOLUTIONIZING MARKETING ANALYTICS: A DATA-DRIVEN MACHINE LEARNING FRAMEWORK FOR CHURN PREDICTION'
url: https://doi.org/10.63665/ijierm.v09i01.01
category: analytics
subcategory: framework
date: 2025-01
venue: International Journal Of Innovation In Engineering Research & Management
authors:
- Bhumeka Narra
- Navya Vattikonda
- Anuj Gupta
source: openalex-oa
pdf_url: https://journal.ijierm.co.in/index.php/ijierm/article/download/2755/2087
pages: 8
chars: 31517
fetched_at: '2026-11-08T17:31:39+00:00'
kb_version: 1
---

# REVOLUTIONIZING MARKETING ANALYTICS: A DATA-DRIVEN MACHINE LEARNING FRAMEWORK FOR CHURN PREDICTION

150

INTERNATIONAL JOURNAL OF INNOVATION IN ENGINEERING RESEARCH & MANAGEMENT ISSN: 2348-4918
Peer Reviewed and Refereed Journal

   VOLUME: 09, Issue 01, Paper id-IJIERM-IX-I, February 2022
REVOLUTIONIZING MARKETING ANALYTICS: A DATA-DRIVEN MACHINE LEARNING
FRAMEWORK FOR CHURN PREDICTION

Bhumeka Narra
Sr Software Developer, Statefarm
Navya Vattikonda
Business Intelligence Engineer, International Medical Group Inc
Anuj Kumar Gupta
Oracle ERP Senior Business Analyst, Genesis Alkali
Dheeraj Varun Kumar Reddy Buddula
Software Engineer, Anthem Inc
Hari Hara Sudheer Patchipulusu
Software Engineer, Iheartmedia
Achuthananda Reddy Polu
SDE3, Microsoft

Abstract - One of the biggest problems for big bu sinesses is customer attrition. Since
consumers are the primary source of income for businesses in the rental industry, they are
specifically searching for strategies to keep them as clients. This study presents the data -
driven machine learning technique f or telecom sector churn prediction, addressing
challenges of noisy, imbalanced, and high -dimensional data through a comprehensive
preprocessing pipeline that includes noise removal, SMOTE -based balancing, feature
selection, and outlier detection. In order to create predictive models using Decision Trees
and Random Forest classifiers, the preprocessed data —which consists of 3,333 customer
records with attributes ranging from call metrics to charge information —is separated into
training and testing sets. When  measured using measures like accuracy, precision, recall,
F1-score, and ROC analysis, the Decision Tree model performed better than other models
like ANN and SVM, achieving 88% accuracy, 83% precision, 93% recall, and 88% F1 -score.
These outcomes show how  the approach may produce useful insights for improving
customer retention and marketing strategy optimization in changing telecom contexts.
Keywords: Customer Churn Prediction, Customer Retention, Marketing Analytics,
Predictive Analytics, Telco-Customer-Churn dataset, Machine Learning.

1 INTRODUCTION
Today's business environment makes
customer satisfaction and retention the
keys to success, thus making the analysis
of customer behavior a fundamental
source of market advantage. The
telecommunication indus try, which
operates within an environment of swift
expansion and aggressive market
competition, maintains customer churn as
its constant business challenge because
customers sever relationships with
provider services [1]. The act of customer
turnover results in both revenue decrease
and the waste of expenses spent on
customer acquisition through advertising
and concession programs alongside
operational expenses.
The analysis of massive customer
interaction data provides patterns and
meaningful insights busi nesses can use
for engaging with clients who show signs
of disengagement. The acquired insights
guide companies to deliver customized
offers and enhanced service delivery,

which both boost customer fulfillment
levels and marketing cost-effectiveness.
The s trategic requirement for
organizations to predict customer churn
extends beyond technical challenges,
especially when operating with
subscription-based business models[2].
Through accurate customer attrition
identification, companies can create
proactive s trategies that lower customer
turnover rates and bring substantial
profits over extended periods. Error
prediction capabilities of machine learning
allow data analysis to proceed
autonomously, which constitutes the
analytical transformation that leads
marketers to produce predictive models
for decision -making. Machine learning
describes the method of teaching digital
computers to perform tasks that qualify as
learning through animal or human
behavior and cognitive processes [3]. An
ML system gathers observa tions of its
working environment to improve
performance in the future [4].

151

INTERNATIONAL JOURNAL OF INNOVATION IN ENGINEERING RESEARCH & MANAGEMENT ISSN: 2348-4918
Peer Reviewed and Refereed Journal

   VOLUME: 09, Issue 01, Paper id-IJIERM-IX-I, February 2022
1.1 Contribution of study
The research analyzes a data -based
machine learning system that aims to
transform marketing analysis through
customer churn forecasting. The research
establishes advancements within its field
through improved model efficiency and
data-based customer retention decisions.
The key contributions are as follows:
 Utilizing the Telco Customer Churn
dataset to provide a comprehensive
view of churned and non -churned
customers to efficiently train and
assess models.
 Preprocessing the dataset and
identifying the most relevant features
is done through feature selection,
along with outlier detection techniques
to improve data quality and model
reliability.
 The dataset is divided into sections for
testing and training, while applying
cross-validation to ensure robust
evaluation and generalizability of the
framework.
 To evaluate machine learning,
performance indicators such as
accuracy, precision, recall, and F1 -
score are utilized, models like DT and
Random Tree, in order to provide a
balanced approach to handling false
positives and false negatives.

1.2 Structure of paper
The structure of the paper is as follows: A
thorough literature review that highlights
current methods is presented in Section II.
The suggested framework and model
development are explained in Section III.
Results of the Section IV experiment and
visualization of important metrics. Finally,
Section V concludes with key findings,
practical implications, and
recommendations for future
advancements in marketing analytics.

2 LITERATURE REVIEW
The literature review examines approaches
to anticipating customer loss through ML
and DL models with the purpose of
enhancing retention efforts and guiding
strategic choices.
Idris, Iftikhar and Rehman (2019) the
combination of AdaBoost classification
features with genetic programming
searching tools allow the development of
an advanced churn prediction system that
effectively identifies churn behavior
improvements. The telecom dataset
imbalance problem receives solution
through PSO-based undersampling, which
allocates training data fairly to GP -
AdaBoost prediction systems. The
combination of GP -AdaBoost with particle
swarm optimization based undersampling
develops ChP -GPAB as a prediction
system generating better results for
consumer churn detection along with
identifying key drivers of customer
behavior. Two widely known telecom data
sets are utilized to test and assess the
proposed ChP-GPAB system. The findings
reveal t hat ChP -GPAB identifies the
causes of customer turnover while
achieving assessment results of 0.91 AUC
and 0.86 AUC based on data from the
Cell2Cell and Orange datasets [5].
Saghir et al. (2019) analysis
evaluates solitary and ensemble neural
networks as c lassifiers before introducing
a combined ensemble model that uses
bagging with neural networks for better
performance metrics and heightened
churn prediction precision. The research
uses two benchmark datasets obtained
from GitHub for assessing and compari ng
the proposed model. On average, the
proposed model reaches an accuracy rate
of 81% [6].
Ebrah and Elnasir (2019) analysis
includes implementing Naïve Bayes
alongside SVM and decision tree
algorithms on both cell2cell and IBM
Watson datasets. The cell2ce ll data
contains 71,047 observations alongside 57
attributes whereas the IBM Watson data
contains 7033 observations distributed
across 21 attributes. The IBM dataset
yielded scores of 0.82, 0.87, and 0.77
according to the AUC performance
evaluation, wherea s the cell2cell dataset
yielded scores of 0.98, 0.99, and 0.98.
When compared to earlier studies that
used matching datasets, the suggested
models demonstrated higher accuracy
levels [7].
Agrawal et al. (2018) this study
uses a DL approach to show how to d o
churn predictions on a Telco dataset.
Experts decided to develop a non -linear
classification model through multilayered
neural networks. All four elements
including contextual, use, customer data
and support features, contribute to the
churn prediction m odel assessment. The
system determines both the probability of
customer churn as well as the influential

152

INTERNATIONAL JOURNAL OF INNOVATION IN ENGINEERING RESEARCH & MANAGEMENT ISSN: 2348-4918
Peer Reviewed and Refereed Journal

   VOLUME: 09, Issue 01, Paper id-IJIERM-IX-I, February 2022
factors behind such behavior. The trained
model applies its weighted values to
features in order to predict customer
attrition likelihood. An 80.03% ac curacy
rate was attained. The methodology also
gives businesses the capacity to pinpoint
the underlying causes of churn issues and
take action to resolve them [8].
Idris and Khan (2017) used Orange
and Cell2Cell to assess the effectiveness of
the suggested FW-ECP system, two openly
available standard telecom datasets. FW -
ECP produces superior prediction
performances relative to the most
advanced techniques currently in use,
taking into consideration both the huge
dimensionality and unbalanced nature of
the training sets. The Orange and
Cell2Cell datasets have feature spaces
that are 24D and 18D, respectively,
instead of 260D and 76D. The Orange and
Cell2Cell datasets had respective AUCs of
0.85 and 0.82 based on FW-ECP [3].
Mishra and Reddy (2018) Divide
the client base into churners and non -
churners. In this regard, deep learning is
superior to typical machine learning
techniques because it can handle ever -
increasing data quantities, reveal hidden
patterns, identify patterns and underlying
hazards, and dete ct consumer behavior
with more accuracy. This paper's
implementation of DL using CNNs for
churn prediction shows high accuracy
performance. The results of the
experiments show that the churn
prediction out predictive model achieves a
performance level of 8 6.85% accuracy,
91.08 accuracy, 93.08% recall, and
92.06% F-score. The rate of error is 13.15
percent [9].
Table I provides a comprehensive
summary of key studies on customer
churn prediction, highlighting
methodologies, datasets, performance
metrics limit ations, and suggested future
work.

I) Summary of Literature Review on Customer Churn Prediction using machine learning
References Methodology Dataset Performance Limitations & Future Work
Idris, Iftikhar,
and Rehman
(2019)
GP-AdaBoost
integration; PSO-based
undersampling for
dataset balancing.
Cell2Cell, Orange
telecom datasets
AUC: 0.91 (Cell2Cell),
0.86 (Orange)
Limited to telecom datasets; focuses
mainly on churners without extensive
generalization for non -telecom
datasets.
Saghir et al.
(2019)
Ensemble Neural
Network classifier using
Bagging.
Two benchmark
datasets from GitHub
Accuracy: 81% Focused on accuracy; lacks
exploration of interpretability and
reasons for churn.
Ebrah and
Elnasir (2019)
SVMs, Decision Trees,
and Naïve Bayes.
IBM Watson (7033 obs,
21 attrs), Cell2Cell
AUC: 0.82, 0.87, 0.77
(IBM); 0.98, 0.99, 0.98
(Cell2Cell)
Limited analysis of class imbalance;
limited focus on scalability for large
datasets.
Agrawal et al.
(2018)
Multilayer Neural
Network for nonlinear
classification.
Telco dataset Accuracy: 80.03% Performance limited to a single
dataset; lacks exploration of real-world
constraints.
Idris and Khan
(2017)
FW-ECP system for
dimensionality reduction
and handling
imbalanced datasets.
Orange, Cell2Cell AUC: 0.85 (Orange), 0.82
(Cell2Cell)
Focused on dimensionality reduction,
lacks interpretability for real -world
decision-making.
Mishra and
Reddy (2018)
CNN-based Deep
Learning for churn
prediction.
Telecom Industry
dataset
Accuracy: 86.85%;
Precision: 91.08%;
Recall: 93.08%; F1:
92.06%
Limited exploration of alternative deep
learning architectures and broader
applications.

3 METHODOLOGY
This study aims to produce an accurate
marketing analytics churn forecast. By
leveraging historical customer data, the
framework aims to identify p atterns and
key predictors of churn, enabling
businesses to take proactive measures.
The methodology study shown in the
flowchart presents a systematic machine -
learning approach for telecom customer
churn analysis. It begins with a dataset of
telecom custo mer data which undergoes
data preprocessing to clean and prepare
the information. The process then
branches into two parallel steps: feature
selection to identify relevant variables and
outlier detection to remove anomalous
data points. After the preparati on steps
converge, the data is divided into a 75:25
ratio between training and test sets. The
subsequently train machine learning
models, specifically Random Forests and
Decision Trees, using the training data. In
a comprehensive evaluation that follows
model construction, Recall, accuracy,
precision, and F1 score are evaluated. The
findings are obtained in the last stage,
which completes a structured pipeline

153

INTERNATIONAL JOURNAL OF INNOVATION IN ENGINEERING RESEARCH & MANAGEMENT ISSN: 2348-4918
Peer Reviewed and Refereed Journal

   VOLUME: 09, Issue 01, Paper id-IJIERM-IX-I, February 2022
from raw data to useful insights for
forecasting customer attrition in the
telecom industry. Figur e 1 shows this
process in a flowchart that highlights the
important steps.
 Churn prediction using machine
learning can be represented as a
flowchart.

A flowchart's subsequent phases are
briefly described below:
Data Collection
Our dataset  has  been  coll ected  from
two  large  enterprise  systems, named
ESX-1 and ESX -2. The security raw
events were collected over 5  months  for
ESX-1,  over  30  days  for ESX -2,
respectively, in which the detecting threat
information was  separately  recorded  by
the  S OC security  analysts whenever  a
network intrusion  occurred.  The  list  of
threat detection information contains
threat occurrence time, related attacks,
category of attack, respond contents,
attack IPaddress,  and victim network
information.
In our d atasets, we investigated
798 detecting cyber threats in  ESX -1,
which  are dispersed  across  the  entire
collection period. Looking  at  the type of
occurred  attacks  in  recorded cyber
threats, there are 240 scanning, 547
system hacking, and 11 worm a ttacks.
Similarly, in ESX -2 there are 941
scanning, 3,077 system hacking, and 51
worm attacks. This categorizing of attack
type was manually performed by SOC
analysts. By category, the system hacking
attack includes a cross site script, DDoS,
brute force attack, and injection  attack. A
trojan and backdoor  attack  belongs  to
scanning  attack.  Overall the number of
attacks were found 4,079 cyber -threats.
Our dataset  has  been  collected  from
two  large  enterprise systems, named
ESX-1 and ESX -2. The security raw
events were collected over 5  months  for
ESX-1,  over  30  days  for ESX -2,
respectively, in which the detecting threat
information was  separately  recorded  by
the  SOC security  analysts whenever  a
network  intrusion  occurred.  The  li st  of
threat detection information contains
threat occurrence time, related attacks,
category of attack, respond contents,
attack IPaddress,and victim network
information.
The telecom industry's churn
prediction model design uses a customer's
historical conduct over a certain time
period to forecast how they will behave in
the near future. As a result, it is standard
procedure to collect as much information
as possible on every customer. These
attributes—Churn as class label, area,
Here are the details o f each of the 3333
records in the dataset: service calls,
evening calls, evening charges, evening
minutes, day calls, international calls,
international minutes, and lastly, night
calls, night charges, and nightly minutes.
Figure 2 below shows the correlat ion
matrix for churn prediction:

 Heatmap of Correlation Matrix
The correlation matrix in Figure 2 shows
the heatmap displaying relationships
between financial and demographic
variables like age, dependents, referrals,
tenure, and various charge categorie s. It
uses a blue -to-green color gradient with
numerical values in each cell to indicate
correlation strength, where diagonal cells
show perfect correlation (1) and off -
diagonal cells show varying positive and
negative relationships between different
variable pairs.
 Data Processing
Transforming data, or processing it, is
known as data processing. When
presented correctly, data may be both
educational and useful. It can be highly
beneficial. Data processing systems are
also known as information systems. Data
processing may also be described as the
process of converting information into
data. The following steps of pre-processing
are listed below:
 Noise Removal
It is necessary to ensure that the data is
significant since noisy data might provide
subpar outcomes. There are many missing
entries, erroneous values such as "Null,"

154

INTERNATIONAL JOURNAL OF INNOVATION IN ENGINEERING RESEARCH & MANAGEMENT ISSN: 2348-4918
Peer Reviewed and Refereed Journal

   VOLUME: 09, Issue 01, Paper id-IJIERM-IX-I, February 2022
and imbalanced characteristics in the
telecom dataset.
 Data Balancing
Balancing, an essential aspect of accurate
classification, significantly influences the
model's ability to effective ly represent the
classification performance. To address this
imbalance, the SMOTE was employed.
This technique oversamples the minority
class ("Yes‖) to achieve a more balanced
distribution, as illustrated in Figure 3.

 Before and After Applying SMOTE
Figure 3 shows two bar plots illustrating
the distribution of a binary "Churn"
variable before and after applying the
SMOTE balancing method. In the left plot
labeled "Distribution of Churn," there is a
clear class imbalance where the "No"
category (shown in red) has approximately
5,000 counts while the "Yes" category
(shown in blue) has only about 1,800
counts. The right plot, labeled "Balanced
Distribution of Churn," demonstrates the
effect of SMOTE application, where both
categories have been balanced to
approximately 5,000 counts each,
effectively addressing the initial class
imbalance problem that could potentially
bias a machine learning model's
performance.
 Feature Selection
For dimensionality reduction, feature
selection is one method that is employed
[10]; repetitive and unnecessary
characteristics are eliminated while
pertinent features are chosen. Reducing
input dimensionality can enhance
performance by either boosting
generalization ability and classification
accuracy or lowering learning pace and
model complexity.
 Outlier Detection
There are two main categories for outlier
detection: distance -based techniques and
density-based techniques. An observation
is identified as an outlier according to QC
if its value falls outside the specified non -
outlier range.
 Data Splitting
The data was divided into two categories:
25% for testing and 75% for training. The
model is fitted during the training phase,
and evaluating the model's performance
prior to field deployment helps guard
against unforeseen problems tha t may
result from overfitting.
 Proposed Decision Tree (DT)
A hierarchical structure called a decision
tree makes predictions by doing a number
of feature checks [11]. Let's write X for the
input characteristics, Y for the goal
variable, and 𝐷𝑇 for the d ecision tree.
Based on feature tests, the decision tree
iteratively divides the dataset with the goal
of maximizing class separation or
minimizing impurity [12]. The forecast
from the decision tree might be shown as
follows: (1):(1)
Here,  is the class label assigned to
the i-th leaf node, and L is the number of
decision tree leaf nodes, and  is the region
or subset of instances that the i -th leaf
node was assigned to the feature testing.
The indicator function  returns 1 if the
input instance X is in the r egion  and 0
otherwise. Based on the feature checks,
the decision tree moves from the root to a
leaf node and gives the leaf node where
the instance is located the appropriate
class label, .
 Performance metrics
A number of measures, characteristics
like F1 -score, recall, accuracy, and
precision are used to evaluate the
effectiveness of the implemented model.
These metrics help determine how
successful the model is overall. The terms
listed below are explained in their model:
 Customer churning (positive) is
referred to as a "TP" and is classified
as such.
 The term "TN" refers to a consumer
who is not churning (negative) and is
labelled as such [13].
 A "false positive (FP)" is a consumer
who is categorized as churn (positive)
even if they are not churning
(negative).
 A "false negative (FN)" is a customer
who is churning (positive) but is said
to be not churning (negative).
Accuracy: Accuracy measures the precise
number of all made forecasts that turned

155

INTERNATIONAL JOURNAL OF INNOVATION IN ENGINEERING RESEARCH & MANAGEMENT ISSN: 2348-4918
Peer Reviewed and Refereed Journal

   VOLUME: 09, Issue 01, Paper id-IJIERM-IX-I, February 2022
out to be accurate, and Equation (2) is
used to calculate it:
(2)
Precision: The precision of the equation is
the percentage of the projected positive
situations that were accurate (3):
(3)
Recall: The equation is used to compute
recall, which is the percentage of
affirmative cases that were properly
detected (4):
(4)
F1-score: The combination finds extensive
usage as a solitary measurement tool to
evaluate [14] performance of the classifier.
The harmonic combination of accuracy
rate and recall measurement produces the
F-measure assessment metric (5).
(5)
ROC: A graphic depiction of model
performance overall thresholds is the ROC
curve. Through data charting, an
evaluation of the TPR and FPR at
particular thresholds yields a ROC curve.

4 RESULTS & DISCUSSIONS
The churn prediction system is built on a
Windows platform with an Intel i7
processor, 16GB RAM, and SSD storage,
utilizing Python -based libraries such as
scikit-learn and Pandas
This section discusses the
simulated results for machine learning -
based churn prediction utilizing customer-
churn datasets and provides the results of
decision tree model in Table II:
I) Findings of Decision Tree Model on
Telco-Customer-Churn dataset for churn
Prediction
Measures Decision Tree
Accuracy 88%
Precision 83%
Recall 93%
F1-score 88%

 Bar Graph for Decision Tree
Performance
Figure 4 displays the performance of a DT
model for churn prediction. The chart
highlights four key metrics: F1 -score,
recall, accuracy, and precision. The
model's precision is 83%, and its accuracy
is 88%. Recall achieves the highest value
at 93%, and the F1-score is also 88%. The
chart provides a clear representation of
how the decision tree model fares across
different evaluation metrics in predicting
churn.

 ROC curve for DT model
A classification model's performance
appears in Figure 5 at various cutoff
points. The TPR against FPR is shown by
the blue curve, while the random guess
classifier's performance is shown by the
diagonal grey line. The classifier can
efficiently discriminate between positive
and negative classes, as evidenced by th e
outstanding model performance indicated
by the AUC value of 0.97. A further
indication of the curve's high prediction
accuracy and low sensitivity/specificity
trade-offs is its closeness to the top -left
corner.

 Confusion matrix for DT Model
In this Figure 6 shows a confusion matrix
for a binary classification model. It
displays the relationship between true and
predicted labels. There are 847 true
negatives (model correctly predicted "No"),
174 FP (model predicted "Yes" when the
true label was "No"), 45  FN (model
predicted "No" when the true label was
"Yes"), and 1004 TP (model correctly
predicted "Yes"). The model demonstrates
exceptional classification performance
because it achieves high accurate
classification of true positives and true
negatives, according to this matrix.

156

INTERNATIONAL JOURNAL OF INNOVATION IN ENGINEERING RESEARCH & MANAGEMENT ISSN: 2348-4918
Peer Reviewed and Refereed Journal

   VOLUME: 09, Issue 01, Paper id-IJIERM-IX-I, February 2022
 Churn classification performance
Figure 7 visualizes the predicted
probabilities for a churn classification
model. It features a red dashed decision
boundary at 0.5, blue bars for sample
distributions, and orange bars for
predicted positive probabilities. The model
appears to provide accurate predictions
with little uncertainty around the
boundary, as indicated by the bimodal
distribution with peaks close to 0 and 1.
I) Comparison between DT and Existing
Models Performance on Telco -Customer-
Churn dataset
Model Accuracy
Decision Tree (DT) 88%
Artificial Neural Network (ANN)[15] 55.61%
Support Vector Machine (SVM) [16] 69.95%
Random Forest[17] 84.4%

 Bar Graph for Accuracy Comparison
Table III and Figure 8 present a
performance comparison between DT and
existing models, including ANN, SVM, and
RF. The DT model achieves the highest
accuracy of 88%, demonstrating the best
prediction capability for customer churn
research. However, the accuracy of the
ANN model is the lowest (55.61%),
indicating that it is not particularly helpful
in this case. The RF model exhibits
competitive performance with an accuracy
of 84.4%, whilst the SVM model performs
modestly with an accuracy of 69.95%.
This comparison highlights DT's
effectiveness in handli ng the Telco -
Customer-Churn dataset compared to
other popul ar machine -learning
approaches.

5 CONCLUSION & FUTURE WORK
Financial stability and client retention in
telecoms are inextricably linked to
customer churn forecast. Telecom firms
are using machine lea rning (ML) to
forecast customer attrition or the
likelihood that a client would switch to a
rival. The Decision Tree (DT) model
performs successfully in predicting
customer turnover based on its 0.97 AUC
score from ROC curve and accuracy of
88% and precisi on of 83% and recall of
93% and F1 -score of 88%. The confusion
matrix, which displays a high proportion
of genuine positives and true negatives
with few misclassifications, supports these
findings even more. The DT model
demonstrates high effectiveness in
processing the Telco -Customer-Churn
dataset because it achieves better
performance than ANN (55.61%), SVM
(69.95%) and RF (84.4%). The study's
limitations include a reliance on historical
data, which may not fully capture
dynamic market changes or customer
behavior trends. Future work could focus
on improving the generalization of the
churn prediction model by incorporating
real-time data, social media signals, and
other external factors such as economic
trends or competitor actions.

REFERENCES
1 O. Adwan , H. Faris, K. Jaradat, O. Harfoushi,
and N. Ghatasheh, ―Predicting customer churn
in telecom industry using multilayer preceptron
neural networks: Modeling and analysis,‖ Life
Sci. J., vol. 11, no. 3, pp. 75–81, 2014.
2 B. Mishachandar and K. A. Kumar, ―Predicting
customer churn using targeted proactive
retention,‖ Int. J. Eng. \& Technol. , vol. 7, no.
2.27, p. 69, 2018.
3 A. Idris and A. Khan, ―Churn Prediction System
for Telecom using Filter–Wrapper and Ensemble
Classification,‖ Comput. J. , vol. 60, no. 3, pp.
410–430, 2017, doi: 10.1093/comjnl/bxv123.
4 A. Amin et al. , ―Comparing oversampling
techniques to handle the class imbalance
problem: A customer churn prediction case
study,‖ Ieee Access , vol. 4, pp. 7940 –7957,
2016.
5 A. Idris, A. Iftikhar , and Z. U. Rehman,
―Intelligent churn prediction for telecom using
GP-AdaBoost learning and PSO
undersampling,‖ Cluster Comput. , vol. 22, no.
Suppl 3, pp. 7241–7255, 2019.
6 M. Saghir, Z. Bibi, S. Bashir, and F. H. Khan,
―Churn Prediction using Neural N etwork based
Individual and Ensemble Models,‖ in
Proceedings of 2019 16th International Bhurban
Conference on Applied Sciences and Technology,
IBCAST 2019 , 2019. doi:
10.1109/IBCAST.2019.8667113.
7 K. Ebrah and S. Elnasir, ―Churn prediction
using machine  learning and recommendations
plans for telecoms,‖ J. Comput. Commun., vol. 7,
no. 11, pp. 33–53, 2019.
8 S. Agrawal, A. Das, A. Gaikwad, and S. Dhage,
―Customer Churn Prediction Modelling Based
on Behavioural Patterns Analysis using Deep
Learning,‖ in 2018 International Conference on
Smart Computing and Electronic Enterprise,
ICSCEE 2018 , 2018. doi:
10.1109/ICSCEE.2018.8538420.
9 A. Mishra and U. S. Reddy, ―A Novel Approach
for Churn Prediction Using Deep Learning,‖ in
2017 IEEE International Conferenc e on
Computational Intelligence and Computing
Research, ICCIC 2017 , 2018. doi:
10.1109/ICCIC.2017.8524551.
10 V. Umayaparvathi and K. Iyakutti, ―Automated
feature selection and churn prediction using
deep learning models,‖ Int. Res. J. Eng. Technol.,
vol. 4, no. 3, pp. 1846–1854, 2017.
11 H. Sharma, S. Kumar, and others, ―A survey on
decision tree algorithms of classification in data
mining,‖ Int. J. Sci. Res., vol. 5, no. 4, pp. 2094–
2097, 2016.

157

INTERNATIONAL JOURNAL OF INNOVATION IN ENGINEERING RESEARCH & MANAGEMENT ISSN: 2348-4918
Peer Reviewed and Refereed Journal

   VOLUME: 09, Issue 01, Paper id-IJIERM-IX-I, February 2022
12 P. Jayaswal, B. R. Prasad, D. Tomar, and S.
Agarwal, ―An ensemble approach for efficient
churn prediction in telecom industry,‖ Int. J.
Database Theory Appl. , vol. 9, no. 8, pp. 211 –
232, 2016.
13 A. Alamsyah and N. Salma, ―A comparative
study of employee churn prediction model,‖ in
2018 4th international conference on science and
technology (ICST), 2018, pp. 1–4.
14 A. Amin, F. Al -Obeidat, B. Shah, A. Adnan, J.
Loo, and S. Anwar, ―Customer churn prediction
in telecommunication industry using data
certainty,‖ J. Bus. Res. , 2019, doi:
10.1016/j.jbusres.2018.03.003.
15 A. Mishra and U. S. Reddy, ―A comparative
study of customer churn prediction in telecom
industry using ensemble based classifiers,‖ in
Proceedings of the International Conference on
Inventive Computing and Informatics, ICICI
2017, 2018. doi: 10.1109/ICICI.2017.8365230.
16 G. E. Xia, H. Wang, and Y. Jiang, ―Application
of customer churn prediction based on weighted
selective ensembles,‖ in 2016 3rd International
Conference on Systems and Informatics, ICSAI
2016, 2017. doi: 10.1109/ICSAI.2016.7811009.
17 I. Ullah, B. Raza, A. K. Malik, M. Imran, S. U.
Islam, and S. W. Kim, ―A Churn Prediction
Model Using Random Forest: Analysis of
Machine Learning Techniques for Churn
Prediction and Factor Identification in Telecom
Sector,‖ IEEE Access , 2019 , doi:
10.1109/ACCESS.2019.2914999.
18 Routhu, K., Bodepudi, V., Jha, K. M., & Chinta,
P. C. R. (2020). A Deep Learning Architectures
for Enhancing Cyber Security Protocols in Big
Data Integrated ERP Systems.  Available at
SSRN 5102662.
19 Chinta, P. C. R., & Katnapally, N. (2021). Neural
Network-Based Risk Assessment for
Cybersecurity in Big Data -Oriented ERP
Infrastructures. Neural Network -Based Risk
Assessment for Cybersecurity in Big Data -
Oriented ERP Infrastructures.
20 Katnapally, N., Chinta, P. C. R., Routhu, K. K.,
Velaga, V., Bodepudi, V., & Karaka, L. M. (2021).
Leveraging Big Data Analytics and Machine
Learning Techniques for Sentiment Analysis of
Amazon Product Reviews in Business
Insights. American Journal of Computing and
Engineering, 4(2), 35-51.
21 Karaka, L. M. (2021). Optimising Product
Enhancements Strategic Approaches to
Managing Complexity.  Available at SSRN
5147875.
22 Chinta, P. C. R., & Karaka, L. M. Agentic AI and
Reinforcement Learning: Towards More
Autonomous and Adaptive Ai Systems.
23 Boppana, S. B., Moore, C. S., Bodepudi, V.,
Jha, K. M., Maka, S. R., & Sadaram, G. AI and
ML Applications In Big Data Analytics:
Transforming ERP Security Models For Modern
Enterprises.
