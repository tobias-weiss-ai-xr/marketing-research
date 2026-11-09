---
title: 'Modeling the Telemarketing Process using Genetic Algorithms and Extreme Boosting: Feature Selection
  and Cost-Sensitive Analytical Approach'
url: https://arxiv.org/abs/2310.19843
category: ai-marketing
subcategory: empirical
date: 2023-10
venue: ''
authors:
- Nazeeh Ghatasheh
- Ismail Altaharwa
- Khaled Aldebei
source: arxiv
pdf_url: https://arxiv.org/pdf/2310.19843
pages: 19
chars: 95170
fetched_at: '2026-11-08T13:11:37+00:00'
kb_version: 1
---

# Modeling the Telemarketing Process using Genetic Algorithms and Extreme Boosting: Feature Selection and Cost-Sensitive Analytical Approach

Received 12 May 2023, accepted 27 June 2023, date of publication 6 July 2023, (this is a pre-print version of the published article).
Digital Object Identifier 10.1109/ACCESS.2023.3292840
Modeling the Telemarketing Process
using Genetic Algorithms and Extreme
Boosting: Feature Selection and
Cost-Sensitive Analytical Approach
NAZEEH GHATASHEH1, ISMAIL ALTAHARWA 2, AND KHALED ALDEBEI. 1
1Department of Information Technology, The University of Jordan, Aqaba, Jordan (e-mail: n.ghatasheh, k.debei@ju.edu.jo)
2Department of Computer Information Systems, The University of Jordan, Aqaba, Jordan (e-mail: i_taharwa@ju.edu.jo)
Corresponding author: Nazeeh Ghatasheh (e-mail: n.ghatasheh@ju.edu.jo).
ABSTRACT Currently, almost all direct marketing activities take place virtually rather than in person,
weakening interpersonal skills at an alarming pace. Furthermore, businesses have been striving to sense and
foster the tendency of their clients to accept a marketing offer. The digital transformation and the increased
virtual presence forced firms to seek novel marketing research approaches. This research aims at leveraging
the power of telemarketing data in modeling the willingness of clients to make a term deposit and finding the
most significant characteristics of the clients. Real-world data from a Portuguese bank and national socio-
economic metrics are used to model the telemarketing decision-making process. This research makes two
key contributions. First, propose a novel genetic algorithm-based classifier to select the best discriminating
features and tune classifier parameters simultaneously. Second, build an explainable prediction model. The
best-generated classification models were intensively validated using 50 times repeated 10-fold stratified
cross-validation and the selected features have been analyzed. The models significantly outperform the
related works in terms of class of interest accuracy, they attained an average of 89.07% and 0.059 in terms
of geometric mean and type I error respectively. The model is expected to maximize the potential profit
margin at the least possible cost and provide more insights to support marketing decision-making.
INDEX TERMS Business Analytics, Cost-Sensitive Analysis, Marketing Research, Electronic Business,
Evolutionary Algorithms, Telemarketing
I. INTRODUCTION
T
ELEMARKETING has been the norm in social com-
merce activities since the revolution of social customers.
Marketing teams utilize different communication mediums
such as phone calls, emails, social media platforms, etc.
However, it is not a switch on shift and it is challenging to
predict and understand the client’s behavior. Nowadays the
“social customers” are informed and influenced by various
stimuli which make the business survival more dependent
on intelligent approaches. Businesses have to capture and
extract the needed knowledge nuggets in understanding the
market needs and make critical responses. The sought novel
approaches aim far away beyond conventional market analy-
sis practices [1], [2].
Knowledge is an emergent asset for building and sustain-
ing the business ecosystem in the short and long runs. Such
knowledge represents various aspects of business success
factors, such as behavior, organization, culture, economic,
social, and others. Benefiting from and aligning the advance-
ments in computer intelligence to the advances in business
refers to Business Analytics (BA). BA has been used by many
researchers in different areas to support business creativity.
For example, the behavioral analysis of service company
clients to enhance customer relationship management, mar-
ket segmentation for appropriate delivery of services, and
enhanced customer satisfaction for a higher return on invest-
ment [3].
BA of the banks’ telemarketing process is challenging [4]–
[6] due to the nature of the available data and the percep-
tional factors of the clients. Typically, historical data about
the clients are imbalanced (i.e., the ratio between clients
accepting an offer and those not interested is relatively very
low), missing data usually is a concern, clients’ intentions
VOLUME 11, 2023 1
arXiv:2310.19843v1  [cs.LG]  30 Oct 2023

Ghatasheh et al.: Modeling the Telemarketing Process using Genetic Algorithms and Extreme Boosting
and attitudes may be affected by external factors (e.g., market
dynamics, economic stability, etc), and the decision-makers
are interested in understanding the factors affecting the inten-
tions of the clients [5], [7]. It is infeasible to contact all the
clients in direct marketing campaigns, therefore selecting a
potentially profitable sample of target clients is crucial. The
cost of missing an opportunity is considerable as during the
campaign either there is a possibility to exclude a potential
target or contact an uninterested one.
In practice, researchers aim at leveraging the marketing
process success rate either by implementing highly demand-
ing and complex algorithms [5], [6], [8] (e.g., Deep Learning
and Artificial Neural Networks) or employing approaches in
which the original data are manipulated [4], [9]–[12] (e.g.,
resampling). Complex algorithms may generate competitive
models but hinder the interpretation of the outcomes by
decision-makers, and data manipulation may impose compu-
tational overhead or a distorted real-world representation of
the problem. Either direction will make it harder to generalize
the generated models and may produce analytical reports
specific to the analyzed set of data; which makes predicting
other clients’ intentions harder to achieve.
This research adopts a novel GA-based approach to pre-
dicting the intent of bank clients for two main purposes. First,
tuning the hyperparameters of a cost-sensitive classification
algorithm. Second, finding the best subset of discriminat-
ing features. This approach is used to overcome various
challenges of which some were imposed by the nature of
the telemarketing data. The adapted cost-sensitive classifi-
cation algorithm (i.e., XGBoost) managed to mitigate the
effects of class imbalance without distorting the original
data. Furthermore, minimizing the overall complexity of
the prediction model and enabling an explainable decision-
making process. The approach illustrates that simultaneous
feature selection and parameter optimization is highly recom-
mended and resulted in an outperforming prediction model,
compared to various related works. The selected subset of
features and optimized parameters improved significantly the
performance of the prediction model such that 30% and
10% of the features attained 88.84% and 89.07% of GMean
value respectively. It is worth mentioning that the approach
managed to attain 0.059 as the lowest misclassification error
of the positive class.
The main contributions of this research are:
– An explainable prediction model of the clients “willing
to accept a marketing offer”.
– The significance of the dataset features.
– Maximized potential profit margin at the least possible
cost.
– Insights to support the telemarketing decision-making
process.
– Comparison of most recent research related to bank
telemarketing.
The rest of the paper is organized as follows: Section II
is a summary of the literature related to the use of computer
intelligence in telemarketing, Section III describes in detail
the dataset used in this research and the methodology, the
results and findings are discussed in Section IV, and the main
conclusions are summarized in Section V.
II. LITERATURE REVIEW
Vast and powerful AI advancements [13] opened promising
utilization avenues in the business domain [3], [14]. The last
decades witnessed an accelerated pace of reliance on AI-
based solutions in making knowledge-based decisions [14],
[15]. Marketing research [16], [17] and attempts to model
credit scoring [18] surveys are examples on the importance
and potential of AI-based solutions in business domain.
Telemarketing in particular is still one of the business do-
mains that require more domain-specific solutions [14]; the
clients usually tend to be interested more in human-based
interactions over computer-generated communications [2].
Automated bots or computer-generated marketing content
is still behind expectations and indirect marketing may fail
to convince the clients to value the marketing offers [2].
Consequently, understanding the clients’ behaviors and how
to predict their intentions would significantly improve the
process of direct marketing (e.g., telemarketing through one-
to-one phone calls). In bank telemarketing particularly, BA
is an opportunity to understand the willingness of a client to
accept an offer from past marketing-related data.
Moro et al. made available a rich real-world dataset
containing telemarketing campaign data from a Portuguese
bank [7], which they enriched later with further national
socio-economic metrics [5]. Since the release of the initial
dataset various researchers have been attempting to generate
prediction models and descriptive analytics; to assess the
marketing decision-making process. However, due to the im-
balance distribution of the data and other characteristics, non
of the related works was able to provide solutions that handle
all the challenges faced in modeling this business issue [5],
[7], [19]. Interestingly, most of the researchers agree that
not all the dataset features have the same importance in
understanding the intentions of the clients [4], [5], [7], [9],
[10], [20]. Table 1 describes, in brief, some of the related
works and the best-attained prediction performance in terms
of Geometric Mean (GMean) and Type I Error. Some of the
works listed in Table 1 reported the modeling performance
of different approaches and Machine Learning (ML) algo-
rithms [4], [6], [21] and some attempted to understand the
significance of the specific dataset features in predicting the
willingness of the client to accept an offer [5], [9], [10].
As shown in Table 1, recent studies of bank telemarketing,
approach the problem of predicting clients’ willingness to
enroll in term deposits from two angles, Feature selection,
and imbalanced data handling. Feature selection reduces the
complexity of a prediction model. Proper handling of im-
balanced data allows for better generalization of the predic-
tion model to handle real-world scenarios without exhibiting
any bias towards any of the target classes. Xie et al. [4]
proposed normalization to select features most effectively
influencing a client’s response to a telemarketing offer made
2 VOLUME 11, 2023

Ghatasheh et al.: Modeling the Telemarketing Process using Genetic Algorithms and Extreme Boosting
by a bank. Further, they utilized “SMOTE”, oversampling, to
extend the minority class to overcome issues related to data
imbalances. Besides losing the generality of the prediction
model due to the oversampling, we argue that our approach
outperforms [4] by digging deep to identify feature-level
characteristics that help in predicting client intent. Moro,
Cortez, and Rita proposed a feature selection approach based
on sensitivity analysis and expert analysis [5]. The need for
human expertise remains a raised question. Compared to
the literature and our proposed solution, [5] make modest
progress in terms of type I error. The only justification is
overlooking the imbalanced nature of the data. Although
features selection improved model accuracy (i.e., GMean
values for the last two rows in Table 1), this improvement
was at the expense of missing clients interested in long-term
deposit offers.
Safarkhani, and Moro [9] proposed a combinatory ap-
proach that does feature selection and handles imbalanced
data. They utilize wrapped subset evaluation to select the
best discriminating features. While the proposed solution
performs well in terms of GMean, it made quite poor perfor-
mance in terms of type I error. In addition to this performance
flaw, the way [9] handles imbalanced data is questionable,
as both oversampling and under-sampling are maintained
simultaneously. such that correctly classified instances were
increased and wrongly classified instances were reduced.
Yan, Li, and Liu used “S_Kohonen network” to predict the
success rates of a fixed deposit by a telemarketing offer [10].
Their key purpose is to identify the best features to improve
prediction rates of clients who are interested in long-term
deposits through a telemarketing offer. By studying statistical
metrics, they were able to reduce the feature space to 13 fea-
tures. Results were reported in terms of cross-check accuracy,
which does not leave a window to investigate performance in
terms of the different errors. Additionally, they resort to a
method of bottom sampling to reduce the majority class to
mitigate the issue of imbalanced data. Neglecting over 75%
of the publicly released data.
In [6], Ghatasheh et al. proposed using cost-sensitive anal-
ysis to handle imbalanced data issues in the bank telemar-
keting domain. They achieved a pronounced improvement
in terms of prediction model accuracy. They improved pre-
diction rates of the minority class, i.e., clients intended to
positively respond to the telemarketing offer, compared to the
approaches of data re-sampling. In their work [6], Ghatasheh
et al. overlooked feature selection as a robust mean to reduce
the complexity of prediction models. Also, they focused on
the improvements to the prediction model with less discus-
sion of the associated reflections on the economic factors.
Wong, Song, and Wong investigated cost-sensitive analysis
as a mean to handle imbalanced data in business applica-
tions [8], They considered six business domains including
churn prediction, default payment, firm fraud detection, in
addition to the bank deposit telemarketing. Their proposed
idea, namely CSDE, is an ensemble learning version of a
cost-sensitive deep neural network. Prediction models per-
form well in most domains except for churn prediction, and
clients’ response to bank telemarketing offers. In these two
domains variance between “TPR” and “TNR” exceeds 30%.
We argue our proposed approach outperforms [8] in terms
of modeling a client response to a telemarketing offer of a
bank due to the utilization of the Genetic Algorithm (GA) as
a mean for optimizing prediction model parameters.
Gupta, Raghav, and Srivastava compared a set of boosting
algorithms to the conventional machine learning techniques
in the context of bank telemarketing [19]. They found that
Light GBM outperforms all investigated classifiers in terms
of accuracy, AUC score, Precision, Recall, and F1 score
when considering overall data. But, by looking deep into
the reported results, a key observation arises, XGBoost made
very close results in most cases. It outperforms Light GBM
when considering the recall rate of the positive class and
the precision rate of the negative class. This observation
complies with our argument that XGBoost minimizes the
expected bias of the prediction model to the majority class.
Besides reporting results of the investigated classifiers, [19]
do not explicitly mention applying any means to mitigate the
issue of imbalanced data or to select the best discriminating
features. Feng et al. proposed a dynamic ensemble method to
predict the success of a bank term deposit contract through
telemarketing offer [21]. They consider average profit in
addition to the accuracy of the prediction model. They treated
errors differently according to the type of misclassification.
Also, they reported the important factors that impact the
success of a telemarketing offer. Compared to the approach
we propose here, re-weighting miss-classification resembles
cost-sensitive analysis. But, here, we employ machine learn-
ing formal methods to do re-weighting. Additionally, we
ignore correctly classified instances from the re-weighting
process to avoid falling into over-fitting models. Besides
extreme amplifying of errors, [21], perform under-sampling
to avoid complexities brought by imbalanced data. But, they
retain less than 05% of the real data. In our experiments, we
utilize cost-sensitive analysis to handle the issue of imbal-
anced data and to consider economic performance factors si-
multaneously. This allows us to use the whole dataset without
ignoring any instance, which allows for better generalization
of the prediction model.
III. DATA AND METHODOLOGY
This study attempts to model the process of identifying the
profitable telemarketing target clients and identify the possi-
ble decision-making criteria. Starting from the approaches in
the research works [6] and [22] towards a cost-sensitive fea-
ture selection approach. In telemarketing, the positive class
label “yes” represents “a case where a client has subscribed
for a term deposit” and the negative class label “no” repre-
sents the cases in which the client “is not interested”. Various
research works highlighted the advantages of cost-sensitive
approaches in modeling different behaviors or decision-
making processes [6], [8], [23]–[26]. However, predicting the
attitudes of the clients based on the past telemarketing data
VOLUME 11, 2023 3

Ghatasheh et al.: Modeling the Telemarketing Process using Genetic Algorithms and Extreme Boosting
TABLE 1. Summary of bank telemarketing related works.
Ref. Year Imbalance Handling Features Approach GMean Type I Err.
[4] 2022 Oversampling (SMOTE) Normalization Random subspace-multi-
boosting (Decision Trees C4.5)
94.73 0.073
[21] 2022 filter outliers and undersam-
pling, Training dataset normal-
ization
one-hot encoding Dynamic ensemble selection
(several base classifiers)
89.39 0.074
[19] 2021 NA All features used Tuned machine learning classi-
fiers
78.11 0.337
[9] 2021 Resampling Wrapped Subset Evaluation,
Feature selection (12)
Decision Trees (J48) 87.14 0.211
[10] 2020 Subsampling Feature significance (13 fea-
tures)
Optimize S_Kohonen network NA NA
[6] 2020 Cost-Sensitive Classification All features used Cost-Sensitive Multilayer Per-
ceptron
78.93 0.192
[8] 2020 Cost-Sensitive Classification All features used Cost-Sensitive Deep Neural
Network Ensemble
66.2 0.295
[5] 2018 Subsampling and Feature Se-
lection
feature relevance and expert
evaluation
Neural Network Ensemble 81.79 0.182
[7] 2014 NA Relative importance, semi-
automatic approach for feature
selection
Artificial Neural Network 72.95 0.347
is challenging. It is inferred according to the investigated
literature that an unbiased outperforming prediction model
of both user classes is missing. A trade-off could be taken
into consideration to favor the prediction of one of the class
labels over the other without losing the overall prediction
power. The cost of target misclassification depends on the
incorrectly predicted class label; which is usually unequal in
practice [27]. Therefore, directing the classifier to favor more
the class of interest by increasing the weight of the positive
class during the training process would reduce the potential
costs. Cost-sensitive classification is expected to reduce the
positive class misclassification errors while preserving an
acceptable overall prediction accuracy in unbalanced datasets
[6], [23]. Section III-A describes the used dataset in this
research and Section III-B describes the proposed approach.
A. TELEMARKETING DATASET DESCRIPTION
This study considers an updated version of the real-world
Portuguese bank, “Banco de Portugal”, a benchmark market-
ing dataset that is available online [7]. The dataset is enriched
by five socio-economic national-wide indicators and it covers
the period from May 2008 till November 2010. The dataset
has 41188 records of which 36548 records have a negative
label and 4640 have a positive label, i.e., there are only 11%
records of the class of interest. The dataset consists of 20
features. Half of these features (i.e., 10 features) are numeric
and the other half are categorical.
Table 2 contains descriptive statistics of the numerical
features. However, Table 3 describes the distribution of the
categorical features. Furthermore, Table 2 presents a descrip-
tive statistic of the class label (i.e., “yes” and “no”), which
is named “y” in this paper. Each numerical and categorical
feature is given an index for reference.
TABLE 2. Descriptive statistics of numerical features. (Adapted from [7])
Feature Index Avg SD Min. Max.
age 0 40.02 10.42 17 98
duration 1 258.29 259.28 0 4918
campaign 2 2.57 2.77 1 56
pdays 3 962.48 186.91 0 999
previous 4 0.17 0.49 0 7
emp.var.rate* 5 0.08 1.57 -3.4 1.4
cons.price.idx* 6 93.58 0.58 92.201 94.767
cons.conf.idx* 7 -40.50 4.63 -50.8 -26.9
euribor3m* 8 3.62 1.73 0.634 5.045
nr.employed* 9 5167.04 72.25 4963.6 5228.1
* Social and economic context features
B. THE PROPOSED APPROACH
Direct marketing (e.g., phone calls and targeted emails) is one
of the business opportunities that is used by many industries.
However, past direct marketing data do not explicitly reveal
the characteristics of potentially profitable client segments.
Business-oriented organizations strive to understand the basis
of the decision-making process such as in defining and con-
tacting clients who are willing to accept an offer. Black-box
solutions may offer acceptable prediction accuracy. However,
they are still unable to explicitly and clearly explain the
basis of a judgment. Genetic Algorithms (GA) have recently
been used in simultaneous dimensionality reduction and hy-
perparameter optimization to tackle challenges imposed by
commonly used approaches [22].
Marketing is still way behind the complete reliance on au-
tonomous AI systems, human intervention is highly required
at the moment [2]. Therefore, one role of AI-based solutions
is to assist in understanding the clients and justifying the
marketing decisions [12]. There are many types of recent
and advanced ML methods that are proven to attain a high
level of prediction accuracy. Nonetheless, in classification
problems tree-based algorithms were the most used, and
4 VOLUME 11, 2023

Ghatasheh et al.: Modeling the Telemarketing Process using Genetic Algorithms and Extreme Boosting
TABLE 3. Distribution of Categorical features and Descriptive Statistics of the
class label. (Adapted from [7])
Feature Index Category Count Perc.
job
10 admin. 10422 25.30%
11 blue-collar 9254 22.47%
12 entrepreneur 1456 03.54%
13 housemaid 1060 02.57%
14 management 2924 07.10%
15 retired 1720 04.18%
16 self-employed 1421 03.45%
17 services 3969 09.64%
18 student 875 02.12%
19 technician 6743 16.37%
20 unemployed 1014 02.46%
21 unknown 330 00.80%
marital
22 divorced 4612 11.20%
23 married 24928 60.52%
24 single 11568 28.09%
25 unknown 80 00.19%
education
26 basic.4y 4176 10.14%
27 basic.6y 2292 05.56%
28 basic.9y 6045 14.68%
29 high.school 9515 23.10%
30 illiterate 18 00.04%
31 professional.course 5243 12.73%
32 university.degree 12168 29.54%
33 unknown 1731 04.20%
default
credit in default.
34 no 32588 79.12%
35 unknown 8597 20.87%
36 yes 3 00.01%
housing
housing loan.
37 no 18622 45.21%
38 unknown 990 02.40%
39 yes 21576 52.38%
loan
personal loan
40 no 33950 82.43%
41 unknown 990 02.40%
42 yes 6248 15.17%
contact
communication type
43 cellular 26144 63.47%
44 telephone 15044 36.53%
month
45 apr 2632 06.39%
46 aug 6178 15.00%
47 dec 182 00.44%
48 jul 7174 17.42%
49 jun 5318 12.91%
50 mar 546 01.33%
51 may 13769 33.43%
52 nov 4101 09.96%
53 oct 718 01.74%
54 sep 570 01.38%
day_of_week
55 fri 7827 19.00%
56 mon 8514 20.67%
57 thu 8623 20.94%
58 tue 8090 19.64%
59 wed 8134 19.75%
poutcome
previous marketing
campaign outcome.
60 failure 4252 10.32%
61 nonexistent 35563 86.34%
62 success 1373 3.33%
class label.y - no 36548 88.73% - yes 4640 11.27%
* Total number of records: 41188.
gradient boosting and extreme gradient boosting (e.g., XG-
Boost) were the most efficient methods [16]. In general,
XGboost performs well in various domains due to its dis-
tinguished abilities in handling outliers, missing values, high
dimensional data, sparse-aware processing, linear and non-
linear relationships, and parallel processing. Accordingly,
XGBoost is known for its scalability and ability to handle
large datasets.
Marketing research, in particular, seeks an understanding
of the relation between the input variables and the target
class, and the level of influence on the prediction results [4]–
[6]. In addition, many classical ML methods seem to attract
attention recently due to the vast advancement in computa-
tional resources, their ability to produce explainable models,
and their simplicity [12], [16]. GA are able to compete with
advanced ML methods in optimization problems where the
problem space is relatively small and complex. It is apparent
that most advanced methods (e.g., deep learning) are less
likely to easily replace the classical ML methods in the mean-
time. The aforementioned characteristics would nominate a
combination of a robust classification method (i.e., XGboost)
and a potentially effective optimization algorithm (e.g., GA)
to model the telemarketing problem.
This research attempts to (1) develop an outperforming
prediction model of a client willing to accept a term deposit,
(2) find the most significant characteristics of the clients
“willing to accept an offer”, (3) maximize the potential
profit margin at the least possible cost, and (4) provide more
insights to support the marketing decision-making process.
Figure 1 is an abstract illustration of the proposed methodol-
ogy and the phases of the work are summarized as follows:
– Dataset preprocessing (Section III-B1)
– GA feature selection and hyperparameter optimization
(Section III-B2)
– Analysis of the selected features (Section IV-B)
– Repeated cross-validation of the best-selected models
(Section III-B3)
0
0
λ
μ
Cost
Telemarketing
Dataset
Features
Genetic AlgorithmXGBoost
Feature Selection and Optimization
Parameters Selected Features
Best
Cross
Validation
Pre-Processing
Clients
Data
Socio-Ec
onomic
Data
Campaign
Data
Features
Param
FIGURE 1. Abstract Architecture of the Proposed Methodology.
1) Dataset Preprocessing
The class label “y” is encoded to satisfy the requirements of
some classifiers (e.g, XGBoost), i.e., the classes “yes” and
“no” are replaced by “1” and “0”, respectively. The class of
interest is set to be “1” in all of the related performance met-
rics. The marketing dataset, which is used in this research, is
VOLUME 11, 2023 5

Ghatasheh et al.: Modeling the Telemarketing Process using Genetic Algorithms and Extreme Boosting
imbalanced and contains a mix of categorical and numerical
features. Furthermore, some of the data are missed, which are
denoted as “unknown”. Such dataset characteristics impose
many challenges that make the quality and fairness of a
classification method more questionable. One-Hot Encoding
is one of the possible solutions to alleviate these challenges
[28], [29]. One-Hot Encoding transforms each categorical
data into a new feature and assigns a binary value of “1”
or “0” to those features, i.e., a categorical feature with “m”
categories is transformed to “m” binary features. Each feature
is assigned to “1” if a given data falls within the category,
and zero otherwise, as illustrated in Table 4. In the bank
marketing dataset, the 10 categorical features are transformed
to 52 One-Hot Encoded features. Therefore, the total number
of the dataset features becomes 62 features. Table 3 contains
all the encoded features and their corresponding index in the
dataset.
TABLE 4. Three data instances under the categorical feature named “default”
after being One-Hot-Encoded (i.e., A=no, B=yes, C=unknown).
Instance default_no default_yes default_unknown
A 1 0 0
B 0 1 0
C 0 0 1
The encoded features (i.e., 52 features) make an opportu-
nity to study the effect of each specific category on the pre-
diction performance. Furthermore, feature selection may give
insights into the most and least significant features. Detailed
feature analysis and possibly an outperforming classification
are facilitated by the methods described in Section III-B2.
2) GA Feature Selection and Hyperparameter Optimization
In this research, further modifications are made to the GA
presented in [22] (mainly the sensitivity to the class weight
and features encoding) to select a feature subset of the mar-
keting dataset and tune the classifier hyperparameters. Cost-
Sensitive classification [8], [30] aims at giving more weight
to the class of interest (i.e., usually the minority class) and
hence minimizing the misclassification cost. The weights are
adjusted according to the “Cost Matrix” shown in Equation
1. The “Cost Matrix” represents the cost of re-weighting
the classes in which µ and λ represent the corresponding
misclassification cost (i.e., False Positive and False Negative
cost respectively) [6], [8], [30].
Cost =
 0 λ
µ 0

(1)
Confusion matrix [31] represents visually the classification
performance. It is considered the main base for comparison
and deriving several performance metrics. It consists of a
two-dimensional table that holds the counts of the prediction
assessment (i.e., the count of correctly classified instances
“True” and incorrectly classified instances “False”). The
class of interest in this study, i.e., Positive class (y=yes),
represents “Clients willing to take a term deposit” and the
Negative Class (y=no) represents “Clients not interested in
the offer”. Therefore the counts are interpreted as follows:
True Positive (TP) is the “Clients willing to take a term
deposit” correctly classified by the algorithm as y=yes, False
Positive (FP) is the “Clients willing to take a term deposit”
incorrectly classified by the algorithm as y=no, True Negative
(TN) is the “Clients not interested in the offer” correctly
classified as y=no, and False Negative (FN) is the “Clients
not interested in the offer” incorrectly classified as y=yes.
The goodness of the prediction model is represented by TN
and TP, and the confusion of the model (misclassification) is
represented by FP and FN. The developed confusion matrix
is illustrated in Table 5.
TABLE 5. Confusion Matrix (Adapted from [6] ).
Predicted
take a term deposit ?
Willing to Not interested
Actual
take a term deposit ?
Willing to TP FN
Not interested FP TN
Usually, correct classification has no incurred cost [32],
i.e., C TP = C TN = 0, where C represents the cost. Machine
learning algorithms consider an equal misclassification cost.
However, many business cases agree with that, i.e., classi-
fying a fraud activity as legitimate has more drastic conse-
quences than classifying a legitimate activity as fraud. The
same considerations apply to many other fields. For example,
the cost of diagnosing a cancer patient as healthy has more
“deadly” consequences than diagnosing a healthy individual
as a possible cancer patient [32]. Furthermore, in telemar-
keting, it is expected that the cost of CFN is higher than the
cost of CFP due to missing a potential opportunity to profit.
Accordingly, Table 6 represents the desired adaptation of the
misclassification cost to the confusion matrix. Equation 2 is
used to quantify the total misclassification cost.
TABLE 6. Applied Cost Matrix (Adapted from [6], [32] ).
Predicted
take a term deposit ?
Willing to Not interested
Actual
take a term deposit ?
Willing to CTP=0 CFN=λ
Not interested CFP=µ C TN=0
Total_Cost =λ
X
FN +µ
X
FP (2)
In theory, it is advised to set the cost value to the “Inverse
of the class distribution” [32]. however, in imbalanced dis-
tributions, the improper cost value may cause an extreme
amplification of the positive class weight. Therefore, it is
recommended to examine different cost values [30], [32]
(e.g., different λ values). However,µ is always set to 1. Using
6 VOLUME 11, 2023

Ghatasheh et al.: Modeling the Telemarketing Process using Genetic Algorithms and Extreme Boosting
equation 3, the inverse of the telemarketing dataset class
distribution is computed and found to equal 7.877 ( ≈ 8).
Consequently, the inverse class distribution and different
arbitrary cost values were employed in this research to find a
possibly suitable cost value.
ClassDistributionInverse =
P y = “yes′′
P y = “no′′ (3)
The work of [22] presented a modified GA that tries to
find an optimal subset of dataset features as well as an eX-
treme Gradient Boosting (XGBoost) [33] hyperparameters
that maximize the fitness function. The utilized fitness func-
tion is the Geometric Mean (GMean), which is commonly
used in evaluating the prediction performance in imbalanced
class distributions. Equation 4 shows the GMean, which is
the square root of the multiplication of the positive class
recall, i.e., True Positive Rate (TPR), and negative class
recall, i.e., True Negative Rate (TNR) [22], [34]–[36]. The
TPR and TNR are computed as shown in Equations 6) and 7
respectively.
GMean =
√
TPR × TNR (4)
The GMean metric considers both classes (i.e., “Positive”
and “Negative” classes) to avoid class bias in describing
the model performance. The higher GMean indicates a bet-
ter overall classification performance in predicting the two
classes.
Chen and Guestrin [33] proposed a tree boosting algo-
rithm XGBoost. XGBoost is scalable, and it considers data
compression and sharding, cache-aware access, and sparsity-
aware. The XGBoost trains each tree on the residual error
of the previous tree. Consequently, this results in improved
performance, which is represented by the sum of the trees’
predictions. The XGBoost is recommended by many re-
searchers, such as [22], [32], [33], [37]–[40]. They illustrate
its outperforming behavior in many classification and regres-
sion problems if tuned properly.
The GA initializes some parents (a.k.a. chromosomes) that
consist of randomly selected classifier hyperparameters and a
subset of the dataset features (i.e., chromosome genes). A set
of new children (offspring) is generated through selection,
uniform crossover, and mutation over various generations.
GA aims at maximizing the GMean by a stochastic search for
the best hyperparameters and features subset. The first part
of the chromosomes is used to set XGBoost parameters and
the rest are for the selected dataset features. Consequently,
the best XGBoost model, which is selected based on the
GMean, is employed to define the best hyperparameter values
and the optimal features subset. The misclassification cost in
XGBoost is set by the “scale_pos_weight” parameter.
3) Repeated Cross-Validation
The GA search method is examined under different configu-
rations (i.e., different GA setups and cost values). The best
chromosomes are validated using 10-fold stratified cross-
validation [20], [22]. To assert the reliability of the 10-fold
cross-validation, our experiments are repeated 50 times (i.e.,
50×10 CV). The performance metrics and the selected fea-
tures are reported and analyzed further to better understand
the telemarketing process. The specific performance metrics
used in the assessment are described in the next subsection
(i.e., Subsection III-B4).
4) Performance Metrics
The learning capability of the model development process
is an essential aspect of the assessment. There are various
performance metrics, derived from the confusion matrix,
that describe the prediction model’s ability to detect the
willingness of clients to accept a marketing offer. Missing
a potentially profitable client or contacting an uninterested
client results in an incurred cost that should be minimized
to gain the overall advantage. Therefore, it is recommended
to give more attention to the metrics that illustrate an overall
prediction accuracy (i.e., performance metrics based on both
“Negative” and “Positive” classes). Some of these perfor-
mance metrics are briefly described as follows:
1) Total Accuracy (Accuracy). It is the count of correctly
classified instances to the total number of instances.
Alternatively, accuracy is referred to as success rate.
Accuracy is calculated according to Equation 5.
Accuracy = TP + TN TP + TN + FP + FN (5)
2) True Positive Rate (TPR). It is the count of correctly
classified clients willing to accept an offer (i.e., Actual
“willing to” predicted as “willing to”) [31]. Alterna-
tively, TPR is named “Recall” or “Sensitivity”. TPR is
calculated according to Equation 6.
TPR = TP TP + FN (6)
3) True Negative Rate (TNR). It is the count of correctly
classified clients not interested in an offer (i.e., Actual
“not interested” predicted as “not interested”) [31].
Alternatively, TNR is named “Specificity”. TNR is
calculated according to Equation 7.
TNR = TN FP + TN (7)
4) Type I Error. It is the False Negative Rate (FNR) as α
(FNR = 1 - TPR) [41]. FNR is calculated according to
Equation 8.
Type_I_Error = FN TP + FN= FNR (8)
5) Type II Error. It is the False Positive Rate (FPR) as
β (FPR = 1- TNR) [41]. Alternatively, named the
probability of “False Alarm” or “Fall-Out”. FPR is
calculated according to Equation 9.
VOLUME 11, 2023 7

Ghatasheh et al.: Modeling the Telemarketing Process using Genetic Algorithms and Extreme Boosting
Type_II_Error = FP FP + TN= FPR (9)
The Total accuracy is sometimes a misleading perfor-
mance metric and particularly in imbalanced class distribu-
tions [6], [22], [23], [42]. Due to the high number of negative
class counts compared to the positive class counts in real-
life scenarios, it is recommended to support the analysis with
other performance metrics. The classification algorithms usu-
ally have more tendency towards the negative class (i.e.,
bias caused by dominance) and thus less prediction accuracy
of the positive class. In imbalanced class distribution, it is
usual to report the GMean and Area Under the Curve (AUC)
as classification performance metrics. GMean and AUC are
class-independent metrics and they consider the minority
class in evaluating the prediction model accuracy. Therefore,
the AUC as a metric is a representation of the diagnostic
ability of the prediction model [43]. A smaller AUC (i.e.,
AUC < 0.5) indicates randomness of the classification and
a higher AUC indicates better diagnosability. Receiver Oper-
ating Characteristic Curve (ROC) confronts the probabilities
(i.e., TPR and FPR) with different threshold values. The area
under ROC generates the AUC.
In marketing research, it is common to report the Lift
Curve [44] of the classification model. Lift analysis shows the
usefulness of the model against a random selection. Equation
10 shows how lift is calculated at a certain sample size.
Lift = TPR Sample_Size (10)
Relatively high lift values mean an increased probability
(lift) of selecting a positive sub-sample using the prediction
model, compared to random selection.
IV . RESULTS AND DISCUSSION
The behavior of the recently used boosting algorithms XG-
Boost, CatBoost, and LightGBM depends on the experiment
configurations. The boosting algorithms in terms of testing
time are examined under different configurations. Mainly
the testing time of models trained over 1000, 5000, and
10000 instances. To ensure the fairness of the comparison the
same samples were used in building all the models from the
Portuguese marketing dataset. For each input size, the depth
of the model tree is set to 2, 4, 6, 8, and 10. Figure 2 illustrates
the testing time in seconds of the three boosting algorithms
running over a CPU-based environment. It is apparent that
LightGBM testing time increases significantly in relation to
the depth of the model and the sample size. At the first glance,
the LightGBM appears to suit the small size of telemarketing
datasets and shallow tree depth.
As the depth of the model increases as the performance
varies significantly among the three boosting algorithms.
Figure 3 illustrates the sample test size in relation to the
testing time at the maximum examined depth (i,e., 10). The
analysis of the testing time shows that XGBoost outperforms
the confronted algorithms in larger datasets or deeper models.
(1000, 2)(1000, 4)(1000, 6)(1000, 8)(1000, 10)(5000, 2)(5000, 4)(5000, 6)(5000, 8)(5000, 10)(10000, 2)(10000, 4)(10000, 6)(10000, 8)(10000, 10)
Test_Size, Depth
0
500
1000
1500
2000Time in Seconds
boosting
catboost
lightgbm
xgboost
FIGURE 2. Testing time comparison of XGBoost, CatBoost, and LightGBM.
1000 5000 10000
test_size
0
50
100
150
200
250time in seconds
catboost xgboost
FIGURE 3. Testing time comparison of XGBoost and CatBoost at model
depth = 10.
A. SENSITIVITY ANAL YSIS
Sensitivity analysis [45] is an important step in building
a machine learning-based model. It aims at studying the
behavior of the used methods when applied to a specific case
and defining the proper setup parameters. In this study, it
is important to analyze the effect of the GA configurations
[22] and different cost values ( λ) on the fitness function.
Therefore, several GA parameters andλ values are examined
as listed in Table 7. Wherever there is a random number
generation method the “seed” is fixed (i.e., randomness seed
= 723) to ensure consistent behavior in the comparisons and
reproducible experiments.
Specifically for XGBoost, the recommended ranges of the
hyperparameters to be optimized are listed in Table 8 with
a brief description of each parameter. The GA algorithm
considers these specified ranges in optimizing the hyperpa-
8 VOLUME 11, 2023

Ghatasheh et al.: Modeling the Telemarketing Process using Genetic Algorithms and Extreme Boosting
TABLE 7. GA Parameters configurations.
Parameter Value
Percent of features to select (F) [10,20,30,40] %
Parents (P) [10, 20, 100]
Crossover ratio (C) [10, 20, . . . ,90] %
Generations (G) [100, 50, 30]
Cost (λ) [1,2, . . . , 12, 15, 20, 50, 100, 150, 200]
rameters of XGBoost.
TABLE 8. The hyperparameters of XGBoost to be optimized by GA [22].
XGB Parameter Value
Range
Description
learning_rate 0.01 - 1 Algorithm learning rate; the lower
the better but requires more itera-
tions to find an optimal solution.
n_estimators 10 - 1500 Maximum number of estimators
max_depth 1 - 10 Maximum tree depth, to control
overfitting. (e.g., high depth will
bias the algorithm toward a specific
sample)
min_child_weight 0.01 - 10.0 Minimum sum of observations in a
child
gamma 0.01 - 10 Minimum reduction of loss when
splitting
subsample 0.01 - 1.0 Random subset of observations for
each tree
colsample_bytree 0.01 - 1.0 Subset of columns to be sampled in
the trees
Different cost value “ λ” is used to re-weight the mis-
classification cost in different experiments. The other GA
configuration parameters are fixed; the percentage of features
to be selected (F) is 10, the initial population size (P) is
10, the crossover ratio (C) is 5%, and iterated over 100
generations (G). The effect of the different cost values on the
GMean is illustrated in Figure 4(a) ( λ = 1, . . . ,5 ), Figure
4(b) (λ = 6, . . . ,10 ), Figure 4(c) ( λ = 11, 12, 15, 20), and
Figure 4(d) (λ = 50, 100, 150, 200).
It is noticeable that cost values around the inverse of the
class distribution ( 7.877 ≈ 8), Figure 4(b), results in the
best GMean values. It leads to better convergence of the
fitness function too. The value “ λ = 6” is the most suitable
cost value for the bank telemarketing case, it is less likely
to cause an amplification of the positive class weight, and
it is expected to avoid overfitting in the generated models.
Therefore, a cost value = 6 is fixed in the following experi-
ments to study the effect of the crossover ratio in modeling
the telemarketing process. The other GA parameters are fixed
to focus on the effect of the crossover. The effect of the
crossover ratio between 10% and 50% is illustrated in Figure
5(a), and Figure 5(b) shows the effect of the crossover ratio
between 50% and 90%.
50% Crossover ratio represents a borderline between two
sets of results, (i.e., High and Low fitness). A crossover
ratio below 50% results in a higher GMean compared to a
crossover over 50%. The nature of the GA and the relatively
small number of features to be selected require a small
crossover proportion. In addition, the randomness of the GA
in initializing the population seems to be sufficient and hence
requires a low rate of crossover. The analysis of the crossover
effect as illustrated in Figure 5 and the cost value effect
shown in Figure 4 makes it apparent that fast convergence
occurs usually before 20 generations, and in general, there is
no significant increase in GMean value after 30 generations.
The initial sensitivity analysis results suggest that the
near-optimal configuration values are 6 as cost value, 20%
crossover rate, and 20 generations. Based on these findings
a number of consequent optimization and feature selection
experiments were conducted, of which some were repeated
roughly with configurations according to Table 7. The con-
figurations and the results of the top ten experiments (based
on GMean) are listed in Table 9. The experiments are named
by letters from “A” to “J” and “A-J” refers to the best
10 GA feature selection and hyperparameter optimizations
experiments.
B. ANAL YSIS OF THE SELECTED FEATURES
The GA achieved a maximum GMean value of 90.21%
with 19 selected features and the best GMean was 89.83%
with seven selected features. In general, the most dominant
features are “1: duration” and “8: euribor3m” followed by “6:
cons.price.idx” then “56: day_of_week_mon”. “duration” in
seconds represents the duration of the last contact with the
client, “euribor3m” and “cons.price.idx” are socio-economic
metrics representing a daily indicator of 3-month “Euribor”
rate and a monthly indicator of consumer price index respec-
tively, and “day_of_week_mon” is the last day of contact
with the client. Spearman rank correlation matrix illustrated
in Figure 6 highlights the correlation of the features based
on all the conducted experiments, Table 10 lists the GMean
correlation coefficients, and Table 11 lists the frequency of
the features in all the experiments. The correlation matrix and
the frequency of the features give insights into prioritizing
the characteristics to be considered in deciding which client
to contact in the next marketing campaign.
An interesting observation regarding the significance of
the features can be drawn from the correlation matrix. The
features are divided into three main groups according to their
positive, negative, and neutral influence on the GMean value.
The diverging relationships are explained in Table 10 in terms
of Spearman rank correlation coefficient r. The Spearman
r values suggest that the Negative and Neutral groups of
features are an extra burden in understanding the intentions
of the clients. This could be a direction towards studying
the significance of telemarketing features and how to re-
construct a telemarketing database.
C. ABLATION TEST
Further analysis of the proposed approach highlights the
effect of FS, Parameter Optimization “PO”, and the selected
cost value “ λ” on the overall performance (i.e., represented
by the GMean). A set of combinations eliminating one or
more of the main parts of the proposed approach (i.e., FS,
VOLUME 11, 2023 9

Ghatasheh et al.: Modeling the Telemarketing Process using Genetic Algorithms and Extreme Boosting
0 20 40 60 80 100
Generation
0.60
0.65
0.70
0.75
0.80
0.85
0.90
0.95Fitness (GMean)
Cost = 1
Cost = 2
Cost = 3
Cost = 4
Cost = 5
(a) λ ∈ [1,. . . ,5]
0 20 40 60 80 100
Generation
0.60
0.65
0.70
0.75
0.80
0.85
0.90
0.95Fitness (GMean)
Cost = 6
Cost = 7
Cost = 8
Cost = 9
Cost = 10 (b) λ ∈ [6,. . . ,10]
0 20 40 60 80 100
Generation
0.60
0.65
0.70
0.75
0.80
0.85
0.90
0.95Fitness (GMean)
Cost = 11
Cost = 12
Cost = 15
Cost = 20
(c) λ ∈ [11, 12, 15, 20]
0 20 40 60 80 100
Generation
0.60
0.65
0.70
0.75
0.80
0.85
0.90
0.95Fitness (GMean)
Cost = 50
Cost = 100
Cost = 150
Cost = 200 (d) λ ∈ [50, 100, 150, 200]
FIGURE 4. The effect of different cost values on the GMean; F=10, P=10, C=5%, G=100.
0 20 40 60 80 100
Generation
0.76
0.78
0.80
0.82
0.84
0.86
0.88
0.90Fitness (GMean)
Crossover = 10%
Crossover = 20%
Crossover = 30%
Crossover = 40%
Crossover = 50%
(a) Crossover ∈ [10%,20%. . . ,50%]
0 20 40 60 80 100
Generation
0.76
0.78
0.80
0.82
0.84
0.86
0.88
0.90Fitness (GMean)
Crossover = 50%
Crossover = 60%
Crossover = 70%
Crossover = 80%
Crossover = 90% (b) Crossover ∈ [50%,60%. . . ,90%]
FIGURE 5. The effect of different crossover ratios on the GMean; F=10, P=10, G=100, and λ=6.
PO, and cost sensitivity “C1 or C6”) are confronted with
experiment “A”. “C1” means eliminating cost sensitivity
(i.e., equal cost of misclassification where “ λ”=1) and “C6”
represents considering cost-sensitive classification using the
best-selected cost value that was determined by the sensi-
tivity analysis. The baseline for the benchmark judgment is
experiment “A” having a GMeamn value of 90.21% (which
considers FS, PO, and C6). Table 12 describes the GA setup,
optimized XGBoost parameters, and the attained perfor-
mance using each of the configurations. The naming conven-
tion of the experiments illustrates the eliminated or included
parts of the approach (e.g., “PO-C6” means eliminating FS
10 VOLUME 11, 2023

Ghatasheh et al.: Modeling the Telemarketing Process using Genetic Algorithms and Extreme Boosting
TABLE 9. Performance summary of the top 10 GA optimization and feature selection experiments (Experiments with IDs “A-J”).
Experiment: A B C D E F G H I J
GA Setup
Perc. to Sel. 30% 30% 10% 30% 10% 10% 20% 40% 10% 10%
Parents 100 100 20 100 10 10 50 20 10 10
Crossover 20% 80% 70% 70% 20% 50% 80% 20% 50% 50%
Generations 30 50 100 30 100 100 30 30 100 100
λ 6 8 6 6 6 6 8 6 8 10
Performance
GA Time in sec. 6163.667 9807.685 1171.609 3713.541 937.327 722.467 2306.898 1021.876 1028.308 711.473
Fitness (GMean) 90.21% 89.97% 89.83% 89.81% 89.75% 89.70% 89.68% 89.65% 89.60% 89.52%
Optimized Hyperparameters
learning_rate 0.18 0.18 0.36 0.18 0.15 0.27 0.15 0.39 0.37 0.27
n_estimators 163 10 114 294 320 444 10 280 80 51
max_depth 6 6 3 6 5 3 4 2 3 5
min_child_weight 10 10 5.8 10 10 10 7.31 10 10 8.65
gamma 6.76 10 4.34 9.35 10 2.97 8.23 6.84 10 3.99
subsample 0.97 0.97 1 0.97 0.51 0.95 0.53 0.61 0.65 1
colsample_bytree 0.5 0.5 0.61 0.5 0.8 0.78 0.82 0.94 0.5 0.9
Best Selected Features
Count 19 17 7 19 7 7 13 25 7 7
Features Indices 1, 5, 6, 7,
8, 15, 21,
22, 24,
25, 26,
36, 40,
49, 53,
55, 56,
58, 60
1, 3, 5,
6, 7, 8,
13, 21,
23, 28,
29, 31,
39, 48,
53, 55,
56
0, 1, 6,
8, 21,
41, 46
1, 2, 6,
7, 8,
15, 21,
22, 24,
25, 28,
31, 32,
39, 40,
51, 56,
59, 60
0, 1, 2,
5, 8,
14, 56
0, 1, 6,
8, 9,
47, 56
0, 1, 2,
6, 7, 8,
14, 21,
25, 53,
54, 55,
56
1, 5, 6,
7, 8, 9,
12, 13,
15, 16,
22, 27,
28, 29,
31, 36,
37, 44,
46, 50,
51, 52,
56, 59,
60
0, 1, 6,
8, 20,
29, 59
0, 1, 6,
7, 8,
24, 60
step, utilizing GA to optimize XGBoost parameters, and
considering cost sensitivity where “λ” =6). Apparently, none
of the combinations was able to outperform the baseline
experiment “A”, and neglecting all the approach components
in experiment “C1” did not outperform any of the other
experiments.
A closer look at Table 12 indicates that the GMean value in
experiment “PO-C6” is 0.71% less than in “A”. However, the
computational complexity of “PO-C6” is significantly higher
as it considers all the features. Further insights on the effect
of the proposed approach steps on the convergence of the
GA fitness function are illustrated in Figure 7. Across the
different generations, the bahaviour of the approach indicates
that “FS”, “PO”, and cost sensitivity together affect positively
the performance.
Based on the ablation test, it is essential to consider all the
proposed approach components. Noticeably, “PO” and cost
sensitivity significantly affect the performance. The inclusion
of “FS” facilitates outperforming and remarkably reduces
the complexity of the generated model. “FS” and “PO” to-
gether outperformed having the cost sensitivity disregarded;
experiments “FS-PO-C1” outperform all non cost-sensitive
ones, and “FS-PO-C6” outperforms all. Understanding the
prediction model is better facilitated by less complex models
(i.e., smaller optimized trees where the feature subset is rela-
tively small). Human comprehension of less complex models
would benefit the marketing decision-making process.
D. MODEL VALIDATION
A set of 10-fold validation experiments are initialized using
the recommended cost values λ, the optimized XGBoost
hyperparameters, and the selected features (i.e., according
to the best ten experiments “A-J” which are listed in Table
9). Each 10-fold validation experiment based on “A-J” is
repeated 50 times (50 ×10CV) to generate 500 models per
configuration. Figure 8 illustrates the performance of the
models of each configuration in terms of GMean (Figure
8(a)), Accuracy (Figure 8(b)), TPR (Figure 8(c)), and FPR
(Figure 8(d)). The GMean value in the validation experiments
is relatively close to the GMean value in the corresponding
GA optimization experiments; this indicates the ability of the
GA algorithm to find relatively stable models.
VOLUME 11, 2023 11

Ghatasheh et al.: Modeling the Telemarketing Process using Genetic Algorithms and Extreme Boosting
GMean
age
duration
campaign
pdays
previous
emp.var.rate
cons.price.idx
cons.conf.idx
euribor3m
nr.employed
job_admin.
job_blue-collar
job_entrepreneur
job_housemaid
job_management
job_retired
job_self-employed
job_services
job_student
job_technician
job_unemployed
job_unknown
marital_divorced
marital_married
marital_single
marital_unknown
education_basic.4y
education_basic.6y
education_basic.9y
education_high.school
education_illiterate
education_professional.course
education_university.degree
education_unknown
default_no
default_unknown
default_yes
housing_no
housing_unknown
housing_yes
loan_no
loan_unknown
loan_yes
contact_cellular
contact_telephone
month_apr
month_aug
month_dec
month_jul
month_jun
month_mar
month_may
month_nov
month_oct
month_sep
day_of_week_fri
day_of_week_mon
day_of_week_thu
day_of_week_tue
day_of_week_wed
poutcome_failure
poutcome_nonexistent
poutcome_success
GMean
age
duration
campaign
pdays
previous
emp.var.rate
cons.price.idx
cons.conf.idx
euribor3m
nr.employed
job_admin.
job_blue-collar
job_entrepreneur
job_housemaid
job_management
job_retired
job_self-employed
job_services
job_student
job_technician
job_unemployed
job_unknown
marital_divorced
marital_married
marital_single
marital_unknown
education_basic.4y
education_basic.6y
education_basic.9y
education_high.school
education_illiterate
education_professional.course
education_university.degree
education_unknown
default_no
default_unknown
default_yes
housing_no
housing_unknown
housing_yes
loan_no
loan_unknown
loan_yes
contact_cellular
contact_telephone
month_apr
month_aug
month_dec
month_jul
month_jun
month_mar
month_may
month_nov
month_oct
month_sep
day_of_week_fri
day_of_week_mon
day_of_week_thu
day_of_week_tue
day_of_week_wed
poutcome_failure
poutcome_nonexistent
poutcome_success
 0.6
0.4
0.2
0.0
0.2
0.4
0.6
0.8
1.0
FIGURE 6. Spearman rank correlation matrix of all the features, in addition to
the GMean value
0 5 10 15 20 25 30
Generation
74
76
78
80
82
84
86
88
90Fitness (GMean)
FS-PO-C6
PO-C6
FS-PO-C1
FS-C1
FS-C6
PO-C1
FIGURE 7. The effect of the “FS”, “PO” and “λ” on attaining the best GMean
value using GA.
The accuracy metric values reassure the concerns in this
study and the related works regarding the use of accuracy
as the main performance metric in imbalanced data dis-
tributions. Based on the performance metrics, the GMean
gives better insights regarding the goodness of the predic-
tion model. Usually, in imbalanced data distributions, it is
important to boost the accuracy of predicting the minority
class without compromising the significance of the majority
class. In the case of bank telemarketing, the FPR indicates
the ratio of contacts with clients that are less likely to accept
an offer. According to Figure 8(d), the FPR is relatively low
in comparison to the TPR; the average of the highest FPR
was about 17.5% in Experiment “G” whereas most of the
TABLE 10. Spearman rank correlation coefficient r of the features in all
experiments with the GMean value.
Feature GMean
Positive Correlation
GMean 1.000000
day_of_week_mon 0.527395
job_unknown 0.423456
cons.price.idx 0.382481
housing_yes 0.375691
loan_no 0.369523
education_basic.9y 0.326174
month_oct 0.305689
day_of_week_fri 0.303669
poutcome_failure 0.281449
euribor3m 0.281059
day_of_week_tue 0.281059
marital_married 0.265445
pdays 0.265445
month_jul 0.265445
month_jun 0.257546
loan_unknown 0.249830
marital_single 0.248120
education_professional.course 0.237010
education_high.school 0.230655
day_of_week_wed 0.212013
age 0.211448
marital_unknown 0.166648
job_housemaid 0.163087
month_dec 0.162366
job_entrepreneur 0.151168
month_may 0.140823
job_admin. 0.132722
job_self-employed 0.132722
month_sep 0.128773
education_university.degree 0.120592
education_basic.6y 0.111977
job_retired 0.102628
job_unemployed 0.093686
job_student 0.088125
emp.var.rate 0.087515
default_yes 0.073810
job_management 0.053003
marital_divorced 0.048086
month_apr 0.027994
contact_cellular 0.023422
loan_yes 0.011198
education_basic.4y 0.000000
Negative Correlation
housing_unknown -0.007807
nr.employed -0.012232
month_mar -0.013914
month_aug -0.014813
housing_no -0.061587
cons.conf.idx -0.063511
month_nov -0.066659
job_technician -0.073389
contact_telephone -0.074211
poutcome_success -0.093686
default_unknown -0.124915
campaign -0.190675
default_no -0.194803
day_of_week_thu -0.202987
job_services -0.249830
education_unknown -0.302337
Neutral Correlation
duration NaN
previous NaN
job_blue-collar NaN
education_illiterate NaN
poutcome_nonexistent NaN
experiments it was less than 13%. It is highly important to
keep the cost value in mind before interpreting the results of
the classification algorithm. For example in experiment “J”
the average TPR was about 94% but the cost λ equals 10;
such a scenario calls for a bank marketing domain expert
to validate the cost value. If a 10 cost value is justifiable
then the prediction model would be suitable for assessing
the total cost of marketing efforts in practice. Further details
regarding the validation process are presented in Table 13.
12 VOLUME 11, 2023

Ghatasheh et al.: Modeling the Telemarketing Process using Genetic Algorithms and Extreme Boosting
A B C D E F G H I J
0.86
0.87
0.88
0.89
0.90
0.91
(a) Geometric Mean
A B C D E F G H I J
0.82
0.83
0.84
0.85
0.86
0.87
0.88
0.89
 (b) Accuracy
A B C D E F G H I J
0.84
0.86
0.88
0.90
0.92
0.94
0.96
(c) TPR
A B C D E F G H I J
0.12
0.14
0.16
0.18
0.20
 (d) FPR
FIGURE 8. Performance metrics of “50×10CV” using the selected features and optimized parameters in the experiments “A-J”.
The maximum GMean and AUC values were 90.92% and
95.91% respectively. Linking the XGBoost parameters (in
Table 9) with the results in Figure 8 and Table 13 illustrates
that the higher the “max_depth” the better the performance
when λ = 6, except for Experiment “C”.
Telemarketing teams may create a short list of clients, that
are expected to accept a marketing offer, to be contacted. The
ability of the prediction model to increase the probability of
selecting possibly interested clients is represented by the lift
of the classifier, and the diagnostic ability (i.e., the random-
ness in classification) is illustrated by the ROC; maximum
lift and AUC are sought. The selected features (30% of
the 62 encoded features) and optimized hyperparameters in
experiment “A” (i.e., having the highest GMean and listed
in Table 9) were used to generate an XGBoost prediction
model. Another model is generated using all the dataset
features and the optimized hyperparameters in experiment
“A”. The models were validated using 10-fold stratified cross-
validation (10CV). Figure 9 plots the lift curves of both the
model with and without feature selection, and Figure 10
confronts the ROC curves of the models.
The ROC curves of the model with the selected features
are illustrated in Figure 10(a), and the ROC curves of the
second model are plotted in Figure 10(b). It is apparent that
10% 20% 30% 40% 50% 60% 70% 80% 90% 100%
Sample Size (Clients being contacted)
1
2
3
4
5
6Lift
Selected features model
All features model
Baseline (Random)
FIGURE 9. Lift curves of a 10-fold cross-validated XGBoost model, using the
selected features (i.e., 30%) and tuned parameters from experiment “A”.
feature selection reduced the dimensionality of the dataset
and maintained competitive lift and AUC values; which
supports the objectives of this research in overcoming the
challenges imposed by the imbalanced dataset. The lift of
the generated model is higher than random selection and the
AUC shows that the classifier does not make totally random
VOLUME 11, 2023 13

Ghatasheh et al.: Modeling the Telemarketing Process using Genetic Algorithms and Extreme Boosting
TABLE 11. Selection frequency of features in the best experiments “A-J” and
in all the experiments.
Feature: Experiments
Index Name A-J All
1 duration 10 37
8 euribor3m 10 36
6 cons.price.idx 9 19
56 day_of_week_mon 7 10
0 age 6 22
7 cons.conf.idx 6 20
21 job_unknown 5 7
5 emp.var.rate 4 13
60 poutcome_failure 4 5
2 campaign 3 8
15 job_retired 3 10
22 marital_divorced 3 6
24 marital_single 3 5
25 marital_unknown 3 5
28 education_basic.9y 3 4
29 education_high.school 3 8
31 education_professional.course 3 5
53 month_oct 3 6
55 day_of_week_fri 3 5
59 day_of_week_wed 3 4
9 nr.employed 2 4
13 job_housemaid 2 4
14 job_management 2 4
36 default_yes 2 8
39 housing_yes 2 3
40 loan_no 2 2
46 month_aug 2 5
51 month_may 2 6
3 pdays 1 1
12 job_entrepreneur 1 2
16 job_self-employed 1 1
20 job_unemployed 1 1
23 marital_married 1 1
26 education_basic.4y 1 2
27 education_basic.6y 1 2
32 education_university.degree 1 3
37 housing_no 1 2
41 loan_unknown 1 1
44 contact_telephone 1 3
47 month_dec 1 2
48 month_jul 1 1
49 month_jun 1 2
50 month_mar 1 3
52 month_nov 1 5
54 month_sep 1 2
58 day_of_week_tue 1 1
4 previous 0 0
10 job_admin. 0 1
11 job_blue-collar 0 0
17 job_services 0 1
18 job_student 0 3
19 job_technician 0 4
30 education_illiterate 0 0
33 education_unknown 0 2
34 default_no 0 3
35 default_unknown 0 1
38 housing_unknown 0 1
42 loan_yes 0 2
43 contact_cellular 0 1
45 month_apr 0 2
57 day_of_week_thu 0 1
61 poutcome_nonexistent 0 0
62 poutcome_success 0 1
predictions.
Based on the lift curve, selecting 10% of the clients to
be contacted using the generated model will make it about
6 times more possible to reach interested clients than by
using a random classifier. From another perspective, the AUC
indicates a higher probability of the model to rank random
interested clients higher than random uninterested more than
95% of the time. In essence, the lift and ROC curves sup-
port the proposed prediction models in terms of leveraging
the possibility of reaching the sought clients and lowering
the possibility of disturbing uninterested clients. Contacting
0.0 0.2 0.4 0.6 0.8 1.0
False Positive Rate
0.0
0.2
0.4
0.6
0.8
1.0True Positive Rate
ROC curve of class 0 (area = 0.95)
ROC curve of class 1 (area = 0.95)
micro-average ROC curve (area = 0.96)
macro-average ROC curve (area = 0.95)
(a) ROC curve using the selected features in exp. “A”.)
0.0 0.2 0.4 0.6 0.8 1.0
False Positive Rate
0.0
0.2
0.4
0.6
0.8
1.0True Positive Rate
ROC curve of class 0 (area = 0.95)
ROC curve of class 1 (area = 0.95)
micro-average ROC curve (area = 0.97)
macro-average ROC curve (area = 0.95)
(b) ROC curve using all the features.
FIGURE 10. ROC curves of a 10-fold cross-validated XGBoost model, using
the selected features (i.e., 30%) and tuned parameters from experiment “A”.
interested clients and not bothering uninterested ones would
be an added value to the bank in terms of its perceived image,
and would reduce the telemarketing direct and indirect costs.
The variations in the performance among the different
experiments are due to the stochastic nature of the GA search
and the randomness of XGBoost model building. Nonethe-
less, the strengths of both GA and XGboost were combined
in this study to select the best subset of features. It is apparent
in the results of different experiments that a relatively small
subset of the total features could be significantly important
in building a competitive prediction model. The outcomes of
this study are compared to different related modeling of bank
telemarketing attempts in Section IV-E.
E. COMP ARISONS
The validated cost-sensitive XGBoost models, tuned by GA,
outperform recent related works [6], [8], [9], [19] in model-
ing the bank telemarketing process. In essence, the compari-
son is based on GMean, Type I Error, Type I Error, and Accu-
racy. Usually, the researchers report part of the performance
metrics and used different validation approaches. However,
Table 14 and Table 15 summarize the performance of several
attempts to model part of the bank telemarketing process
14 VOLUME 11, 2023

Ghatasheh et al.: Modeling the Telemarketing Process using Genetic Algorithms and Extreme Boosting
TABLE 12. The effect of applying feature selection “FS”, parameter optimization “PO” and the cost value “λ” on the model performance.
Experiment: FS-PO-C6
“A”
PO-C6 C6 FS-PO-C1 FS-C1 FS-C6 PO-C1 C1
GA Setup
Perc. to Sel. 30% - - 30% 30% 30% - -
Parents 100 100 - 100 100 100 100 -
Crossover 20% 20% - 20% 20% 20% 20% -
Generations 30 30 - 30 30 30 30 -
λ 6 6 6 1 1 6 1 1
Optimized Hyperparameters
learning_rate 0.18 0.15 ⋆ 0.15 ⋆ ⋆ 0.19 ⋆
n_estimators 163 110 ⋆ 266 ⋆ ⋆ 257 ⋆
max_depth 6 6 ⋆ 9 ⋆ ⋆ 3 ⋆
min_child_weight 10 2.74 ⋆ 10 ⋆ ⋆ 4.62 ⋆
gamma 6.76 9.35 ⋆ 9.54 ⋆ ⋆ 0.01 ⋆
subsample 0.97 0.97 ⋆ 0.63 ⋆ ⋆ 0.51 ⋆
colsample_bytree 0.5 0.96 ⋆ 0.5 ⋆ ⋆ 0.61 ⋆
Performance
Fitness (GMean) 90.21% 89.50% 86.70% 76.76% 76.29% 76.29% 75.66% 74.60%
- Not used.
⋆ Default XGBoost Parameters which are 0.3, 100, 6, 1, 0, 1, 1 respectively.
TABLE 13. Performance and time metrics of the “50×10CV” validation experiments.
Exp GA Fitness Selected Features GMean % AUC % Training Time Testing Time
GMean % Count Min. : Avg. : Max. Min. : Avg. : Max. Avg. sec. Avg. sec.
(SD) (SD) (SD) (SD)
A 90.21 19 86.19 : 88.84 : 90.71
(0.007)
93.51 : 94.81 : 95.91
(0.003)
7.737
(0.512)
0.107
(0.015)
B 89.97 19 86.18 : 88.00 : 90.17
(0.006)
92.86 : 93.90 : 95.47
(0.004)
0.573
(0.072)
0.036
(0.008)
C 89.83 7 86.15 : 88.75 : 90.75
(0.007)
93.38 : 94.54 : 95.46
(0.003)
2.224
(0.298)
0.054
(0.012)
D 89.81 19 86.64 : 88.87 : 90.83
(0.007)
93.65 : 94.78 : 95.57
(0.003)
13.644
(0.643)
0.136
(0.017)
E 89.75 7 86.24 : 88.61 : 90.67
(0.007)
93.47 : 94.57 : 95.67
(0.003)
11.8
(0.873)
0.192
(0.031)
F 89.70 7 86.56 : 88.60 : 90.39
(0.007)
93.46 : 94.52 : 95.42
(0.003)
9.389
(0.493)
0.153
(0.018)
G 89.68 13 85.64 : 87.43 : 89.17
(0.006)
92.30 : 93.61 : 94.82
(0.004)
0.504
(0.054)
0.034
(0.007)
H 89.65 25 86.10 : 88.64 : 90.41
(0.007)
93.48 : 94.61 : 95.57
(0.004)
10.875
(0.516)
0.089
(0.013)
I 89.60 7 86.01 : 88.76 : 90.50
(0.006)
93.46 : 94.42 : 95.27
(0.003)
1.768
(0.201)
0.049
(0.01)
J 89.52 7 87.00 : 89.07 : 90.92
(0.006)
93.61 : 94.71 : 95.58
(0.004)
1.738
(0.183)
0.055
(0.011)
Avg. 89.77 - 88.56 94.45 6.025 0.089
(i.e., decision-making support in defining profitable clients at
the lowest possible financial cost). The total accuracy metric
alone is not necessarily an indication of the goodness of the
prediction model. Financial cost minimization is manifested
by identifying potentially profitable clients who are willing
to accept a marketing offer and minimizing the attempts
to convince possibly uninterested clients. The trade-off is
negotiable as increasing the possibility of identifying a client
willing to accept an offer could justify the possible incurred
costs of contacting unwilling clients to a certain limit. A
domain expert is needed to quantify the exact costs and
benefits in money value according to the cost values that are
recommended in this study.
The GMean of all the experiments in this study is sig-
VOLUME 11, 2023 15

Ghatasheh et al.: Modeling the Telemarketing Process using Genetic Algorithms and Extreme Boosting
TABLE 14. Performance comparison of different classification algorithms.
Algorithm Geometric Mean Type I Error Type II Error Accuracy
Our approach (Selected Features), Avg. of 50 × 10CV:
A (f=19) 88.84 0.096 0.127 87.65
B (f=19) 88.00 0.073 0.165 84.56
C (f=7) 88.75 0.094 0.131 87.35
D (f=19) 88.87 0.098 0.125 87.83
E (f=7) 88.61 0.105 0.123 87.92
F (f=7) 88.60 0.104 0.124 87.81
G (f=13) 87.43 0.073 0.175 83.62
H (f=25) 88.64 0.095 0.132 87.25
I (f=7) 88.76 0.074 0.150 85.91
J (f=7) 89.07 0.059 0.157 85.44
Other cost-sensitive results from related works:
Meta-Cost-Multilayer Perceptron [6] 78.93 0.192 0.229 77.48
CostSensitiveClassifier-Multilayer Perceptron [6] 73.17 0.386 0.128 84.18
Cost-Sensitive Deep Neural Network Ensemble [8] 66.2 0.295 0.378 n.a.
Cost-Sensitive Deep Neural Network [8] 57.9 0.385 0.458 n.a.
AdaCost [8] 44.2 0.11 0.78 n.a.
Meta-Cost [8] 55.1 0.650 0.132 n.a.
Benchmark Machine-learning classifiers:
Multilayer Perceptron [6] 60.87% 0.61 0.05 88.98
Deep Learning for Multilayer Perceptron [6] 57.86% 0.64 0.07 86.24
J48 [6] 58.79% 0.64 0.04 88.9
Lib-LINEAR SVM [6] 62.46% 0.53 0.17 78.61
Decision Table [6] 56.58% 0.67 0.03 89.49
Very Fast Decision Rules [6] 59.13% 0.54 0.24 72.61
Random Forest Trees [6] 51.44% 0.73 0.02 89.82
Tuned benchmark machine-learning classifiers:
XgBoost [19] 78.11 0.337 0.079 90.39
Light GBM [19] 77.83 0.352 0.066 90.92
Support Vector Machines [19] 68.30 0.487 0.091 88.46
Gaussian Naïve Bayes [19] 57.49 0.643 0.074 83.93
Random Forest Trees [19] 77.32 0.354 0.075 90.46
nificantly higher than in the related works, which indicates
achieving a better balance in modeling the negative and
positive classes. For instance in [9] the 12 features, listed in
Table 16, achieved a maximum total accuracy of 94.39% but
had a low prediction accuracy of the class of interest and
relatively high negative class prediction accuracy; 78.94%
in TPR and 96.20% in TNR respectively. Moreover, non
of the models in the related works achieved a competitive
prediction accuracy of the positive class; except in [4] but
with oversampling. The comparison results did not show any
outperforming overall performance, even though some of the
related works did not cross-validate the models nor reported
a repeated validation approach. The neural network-based
models such as in [8] were unable to generate outperforming
models nor provide clear feature analysis. Neural network
models are usually considered as black-box, which makes
them less likely preferred in the decision-aid process; due to
the difficulty in interpreting the model and its dynamics. In
terms of the comparison with benchmark classifiers, tuning
is essential to achieve competitive performance. In [6], [19]
the base classifiers failed to model the positive class properly,
including XGBoost. It is inferred from the comparison that
tuning is essential to initialize the classifiers with proper
parameters and not all the features should be used in bank
telemarketing model building.
The authors in [9] used the “Wrapped Subset Evaluation”
method to select 12 features in building a “J48” trees model.
They attained better total accuracy than resampling and using
the complete original dataset. Their findings support some of
the main results in this study such that a subset of the features
set may improve the overall performance of the prediction
model. Table 16 confronts the top 15 features in [4] and
the selected 12 Features in [9] with the frequency of the
corresponding features chosen in this study. The authors in
[4] managed to achieve very competitive performance results
TABLE 15. Performance of different related classification algorithms.
Algorithm Geometric Mean Type I Error Type II Error Accuracy
J48 on Original Dataset [9] 75.55 0.39 0.064 90.87
J48 and Feature Selection (f=12) [9] 87.14 0.211 0.038 94.39
Naïve Bayes [21] 79.39 0.206 0.206 79.39
Decision Trees [21] 81.83 0.169 0.190 81.82
K Nearest Neighbours [21] 83.43 0.185 0.146 83.48
Logistic Regression [21] 83.17 0.175 0.161 83.18
Support Vector Machine [21] 73.28 0.311 0.221 73.48
Random Forests [21] 85.03 0.185 0.113 85.15
Adaboost [21] 84.52 0.166 0.143 84.55
XGBoost [21] 87.28 0.108 0.146 87.27
Gradient Tree Boosting [21] 87.13 0.114 0.143 87.12
LightGBM [21] 87.13 0.120 0.137 87.12
Artificial Neural Network Ensemble∔ [5] 81.79 0.182 0.182 81.77
META-DES-AAP⋆ [21] 89.39 0.074 0.137 89.39
J48 on Resampled Dataset* [9] 86.12 0.228 0.039 94.1
Random Subspace-Multi-Boosting* [4] 94.73 0.073 0.032 94.7
∔ Feature relevance and expert evaluation.
⋆ Dynamic Ensemble Selection considering Accuracy and Economic Performance (AP) with Meta-Training
* Dataset resampling has been applied.
but with oversampling. There are many concerns about using
oversampling such as the generalization of the generated
models. Imposing a synthetic group of instances to overcome
the imbalance issue may significantly improve the classifier
performance, but it will affect the ability of the model to
predict according to a future set of instances. It is usually
preferred to avoid altering the original dataset significantly
and to validate using a real-world representative sample [6].
In summary, the proposed approach in this research man-
aged to outperform the related research in minimizing the
misclassification cost of the positive class at the best possible
tradeoff. The findings of this research agree with related
works that a subset of the dataset features would give in-
sights into the probability of a client accepting a market-
ing offer. Moreover, one-hot encoding broadens the insights
and decomposes the categorical features into corresponding
detailed features. The empirical results support the claims
regarding the ability of the cost-sensitive model to lower
telemarketing costs and describe the dataset features without
altering the real-world data. The ultimate goal of this research
was to avoid altering the imbalanced real-world data and to
seek a potentially realistic prediction model.
F . LIMITATIONS AND IMPLICATIONS
This research realized some outperforming and competing
models in comparison to the related works on the same
dataset. However, some limitations exist which were handled
or mitigated. This research considered a single benchmark
dataset, which was introduced in [7], in all the experi-
ments. The dataset is challenging due to the relatively high
imbalance ratio and the existence of some missing values
(i.e., missing values provided by the source are denoted as
“unknown”). Stratified and repeated cross-validation of the
models, feature encoding, and making the classification al-
gorithm cost sensitive were employed to mitigate the effects
of imbalance, minimize the bias in generalization, and avoid
any major alterations to the original dataset. The authors
in [7] considered one country and data up to November
2010. In fact, expanding the dataset is not an easy task. This
research relies on the results of the related studies on the same
dataset in assessing the level of performance improvement.
16 VOLUME 11, 2023

Ghatasheh et al.: Modeling the Telemarketing Process using Genetic Algorithms and Extreme Boosting
TABLE 16. The top 15 features in [4] and the selected 12 Features in [9]
confronted with the frequency of the corresponding selected features in the
experiments “A-J”.
Selected Features:
in [4] (rank:importance) in [9] in “A-J” (freq.)
age(15:0.65) age 0:age(6)
education(4:45.98) Education 31:education_professional.course(3)
29:education_high.school(3)
28:education_basic.9y(3)
32:education_university.degree(1)
33:education_unknown(0)
30:education_illiterate(0)
27:education_basic.6y(1)
26:education_basic.4y(1)
contact(11:8.31) contact 44:contact_telephone(1)
43:contact_cellular(0)
duration(5:40.25) duration 1:duration(10)
pdays(14:6.71) pdays 3:pdays(1)
previous(9:12.34) previous 4:previous(0)
poutcome(10:10.78) poutcome 60:poutcome_failure(4)
NA emp.var.rate 5:emp.var.rate(4)
NA cons.price.idx 6:cons.price.idx(9)
NA cons.conf.idx 7:cons.conf.idx(6)
euribor3m(7:24.88) euribor3m 8:euribor3m(10)
NA nr.employed 9:nr.employed(2)
day_of_week(3:52.32) NA 56:day_of_week_mon(7)
job(1:70.77) NA 21:job_unknown(5)
15:job_retired(3)
14:job_management(2)
13:job_housemaid(2)
20:job_unemployed(1)
12:job_entrepreneur(1)
16:job_self-employed(1)
19:job_technician(0)
18:job_student(0)
17:job_services(0)
11:job_blue-collar(0)
10:job_admin.(0)
month (2:60) NA 53:month_oct(3)
51:month_may(2)
46:month_aug(2)
54:month_sep(1)
52:month_nov(1)
50:month_mar(1)
49:month_jun(1)
48:month_jul(1)
47:month_dec(1)
45:month_apr(0)
campaign(6:39.87) NA 2:campaign(3)
marital(8:17) NA 2:marital_divorced(3)
24:marital_single(3)
25:marital_unknown(3)
23:marital_married(1)
housing(12:7.16) NA 39:housing_yes(2)
37:housing_no(1)
38:housing_unknown(0)
loan(13:6.97) NA 40:loan_no(2)
41:loan_unknown(1)
42:loan_yes(0)
Considering different datasets, building a new dataset, or
expanding the dataset would be considered in future works
due to time and resource limitations. It is worth mentioning,
that socio-economic features are usually specific to a certain
community and time which make expanding a dataset even
more challenging. The employed classifier (XGBoost) is
proven to perform well for the use of imbalanced datasets
and outperforms the related research on the same dataset as
well. Due to time and resource limitations, this research did
not utilize deep learning or highly resource-demanding al-
gorithms but instead, intensive validation and comprehensive
reporting of the employed approach results were presented
to make it easier to compare with future works. Despite the
limitations and challenges, the implications of this research
would benefit the business analytics research area, the bank
marketing process, and knowledge-based decision-making in
general. Specifically for bank marketing, telemarketers will
be equipped with updated knowledge in their communication
with the clients which in its turn would improve the customer
experience; contacting a wider range of possibly interested
clients based on better marketing techniques would stimulate
more clients to make a long term deposit, which on its
turn will increase the revenues and most probably higher
commission for the telemarketers. Less stress on the telemar-
keters as they would be more confident in their selection of
target clients to be contacted and enhances their persuasion
abilities. From the telemarketers’ point of view, the updated
knowledge would make them more engaged and feel satisfied
with their achievements; high morale would be another in-
direct implication. Increased trust between the client and the
bank is one of the potential implications that are hard to attain
in a short time usually. As a result, positive implications
would be on the behaviors of both clients and telemarketers
which in its turn will propagate to benefit the organization at
the higher levels (e.g., The middle and top management of
the bank). The outcomes of this research create optimistic
expectations of more considerations and improvements in
future research in the field of bank telemarketing or other
domains as well; both in the technical or managerial aspects
of the employed approach.
V . CONCLUSIONS AND FUTURE DIRECTIONS
In light of what is revealed in this study, it is clear that the
proposed approach was able to outperform in terms of model-
ing the telemarketing process. Simultaneous feature selection
and hyperparameter optimization using genetic algorithms
managed to realize a promising cost-sensitive prediction
model. The extensive validation of the prediction model
illustrates its ability to mitigate a number of challenges in
the analytics of telemarketing data. In essence, selecting the
proper feature subset may significantly improve the perfor-
mance of the classification model (i.e.,88.84% and 89.07%
of GMean using 30% and 10% of the features respectively.
Furthermore, it is found that it is highly recommended to
analyze the effect of the features on the performance as some
may negatively correlate with the class labels. From a socio-
psychological perspective, revealing aspects of clients would
result in a better customer experience, a higher probability to
accept an offer, tightened trust, and possibly less job-based
stress. However, business domain experts are still needed to
quantify the exact financial cost of the marketing campaigns
based on the generated models. This research built on the
results of previous research work to provide better market-
ing insights and directs future work toward several related
research areas. Such future directions include applying the
proposed approach to different telemarketing datasets and
applying the same approach to different business domains.
VOLUME 11, 2023 17

Ghatasheh et al.: Modeling the Telemarketing Process using Genetic Algorithms and Extreme Boosting
REFERENCES
[1] A. Van Looy, “Social customer relationship management,” in Social
Media Management: Using Social Media as a Business Instrument .
Cham: Springer International Publishing|, 2022, pp. 97–123, doi:
10.1007/978-3-030-99094-7_5.
[2] S. Li, A. M. Peluso, and J. Duan, “Why do we prefer humans to
artificial intelligence in telemarketing? a mind perception explanation,”
J. Retail. Consum. Serv. , vol. 70, Art. no. 103139, 2023, doi:
10.1016/j.jretconser.2022.103139.
[3] A. Sestino and A. D. Mauro, “Leveraging artificial intelligence in business:
Implications, applications and methods,” Tech. Anal. Strat. Manag. ,
vol. 34, no. 1, pp. 16–29, 2022, doi: 10.1080/09537325.2021.1883583.
[4] C. Xie, J.-L. Zhang, Y . Zhu, B. Xiong, and G.-J. Wang, “How to improve
the success of bank telemarketing? prediction and interpretability analysis
based on machine learning,”Comput. Ind. Eng., vol. 175, Art. no. 108874,
2023, doi: 10.1016/j.cie.2022.108874.
[5] S. Moro, P. Cortez, and P. Rita, “A divide-and-conquer strategy using
feature relevance and expert knowledge for enhancing a data mining
approach to bank telemarketing,” Expert Syst. , vol. 35, no. 3, Art. no.
e12253, 2018, e12253 EXSY-Sep-16-212.R2, doi: 10.1111/exsy.12253.
[6] N. Ghatasheh, H. Faris, I. Altaharwa, Y . Harb, and A. Harb, “Business
analytics in telemarketing: Cost-sensitive analysis of bank campaigns
using artificial neural networks,” Appl. Sci., vol. 10, no. 7, Art. no. 2581,
Apr 2020, doi: 10.3390/app10072581.
[7] S. Moro, P. Cortez, and P. Rita, “A data-driven approach to predict the
success of bank telemarketing,” Decis. Support Syst., vol. 62, pp. 22–31,
2014, doi: 10.1016/j.dss.2014.03.001.
[8] M. L. Wong, K. Seng, and P. K. Wong, “Cost-sensitive ensemble of
stacked denoising autoencoders for class imbalance problems in business
domain,” Expert Syst. Appl. , vol. 141, Art. no. 112918, 2020, doi:
10.1016/j.eswa.2019.112918.
[9] F. Safarkhani and S. Moro, “Improving the accuracy of predicting bank
depositor’s behavior using a decision tree,”Appl. Sci., vol. 11, no. 19, Art.
no. 9016, Sep 2021, doi: 10.3390/app11199016.
[10] C. Yan, M. Li, and W. Liu, “Prediction of bank telephone marketing
results based on improved whale algorithms optimizing s_kohonen
network,” Appl. Soft Comput. , vol. 92, Art. no. 106259, 2020, doi:
10.1016/j.asoc.2020.106259.
[11] Y . Li and Z. Wu, “Prediction of customers’ subscription to time
deposits based on smoteenn-xgboost model,” in Proc. Wuhan Int. Conf.
e-Bus., 2022, pp. 632–642, [Online]. Available: https://aisel.aisnet.org/
whiceb2022/61.
[12] S. C. K. Tékouabou, S. C. Gherghina, H. Toulni, P. N. Mata, and J. M.
Martins, “Towards explainable machine learning for bank churn prediction
using data balancing and ensemble-based methods,”Mathematics, vol. 10,
no. 14, Art. no. 2379, Jul 2022, doi: 10.3390/math10142379.
[13] S. Chintalapati and S. K. Pandey, “Artificial intelligence in marketing: A
systematic literature review,” Int. J. Mark. Res., vol. 64, no. 1, pp. 38–68,
2022, doi: 10.1177/14707853211018428.
[14] A. L. Echeberria, “The impact of ai on business, economics and
innovation,” in Artificial Intelligence for Business: Innovation, Tools and
Practices, A. Landeta Echeberria, Ed. Cham: Springer Int. Publishing,
2022, pp. 67–96, doi: 10.1007/978-3-030-88241-9_3.
[15] S. C. Cooper, V . Pereira, D. Vrontis, and Y . Liu, “Extending the
resource and knowledge based view: Insights from new contexts
of analysis,” J. Bus. Res. , vol. 156, Art. no. 113523, 2023, doi:
10.1016/j.jbusres.2022.113523.
[16] V . Duarte, S. Zuniga-Jara, and S. Contreras, “Machine learning and mar-
keting: A systematic literature review,” IEEE Access, vol. 10, pp. 93 273–
93 288, 2022, doi: 10.1109/ACCESS.2022.3202896.
[17] E. W. Ngai and Y . Wu, “Machine learning in marketing: A literature
review, conceptual framework, and research agenda,” J. Bus. Res. , vol.
145, pp. 35–48, 2022, doi: 10.1016/j.jbusres.2022.02.049.
[18] D. Tripathi, A. K. Shukla, B. R. Reddy, G. S. Bopche, and D. Chandramo-
han, “Credit scoring models using ensemble learning and classification
approaches: a comprehensive survey,” Wireless Pers. Commun., vol. 123,
pp. 785–812, 2022, doi: 10.1007/s11277-021-09158-9.
[19] A. Gupta, A. Raghav, and S. Srivastava, “Comparative study of ma-
chine learning algorithms for portuguese bank data,” in I. Conf. Comput.
Commun. Intell. Syst. , Greater Noida, India, 2021, pp. 401–406, doi:
10.1109/ICCCIS51004.2021.9397083.
[20] N. Barraza, S. Moro, M. Ferreyra, and A. de la Peña, “Mutual information
and sensitivity analysis for feature selection in customer targeting: A
comparative study,” J. Inf. Sci. , vol. 45, no. 1, pp. 53–67, feb 2019, doi:
10.1177/0165551518770967.
[21] Y . Feng, Y . Yin, D. Wang, and L. Dhamotharan, “A dynamic ensemble
selection method for bank telemarketing sales prediction,” J. Bus. Res. ,
vol. 139, pp. 368–382, 2022, doi: 10.1016/j.jbusres.2021.09.067.
[22] N. Ghatasheh, I. Altaharwa, and K. Aldebei, “Modified genetic algorithm
for feature selection and hyper parameter optimization: Case of xgboost
in spam prediction,” IEEE Access, vol. 10, pp. 84 365–84 383, 2022, doi:
10.1109/ACCESS.2022.3196905.
[23] N. Ghatasheh, H. Faris, R. Abukhurma, P. A. Castillo, N. Al-Madi, A. M.
Mora, A. Al-Zoubi, and A. Hassanat, “Cost-sensitive ensemble methods
for bankruptcy prediction in a highly imbalanced data distribution: a real
case from the spanish market,” Prog. Artif. Intell., vol. 9, no. 4, pp. 361–
375, 2020, doi: 10.1007/s13748-020-00219-x.
[24] X. Jiang, S. Pan, G. Long, J. Chang, J. Jiang, and C. Zhang, “Cost-
sensitive hybrid neural networks for heterogeneous and imbalanced
data,” in Int. Joint Conf. Neural Netw. IEEE, 2018. doi:
10.1109/IJCNN.2018.8489420.
[25] C. X. Ling and V . S. Sheng, “Cost-sensitive learning,” in Encyclopedia
of Machine Learning , C. Sammut and G. I. Webb, Eds. Boston, MA:
Springer US, 2010, pp. 231–235, doi: 10.1007/978-0-387-30164-8_181.
[26] S. Höppner, B. Baesens, W. Verbeke, and T. Verdonck, “Instance-
dependent cost-sensitive learning for detecting transfer fraud,”
Eur. J. Oper. Res. , vol. 297, no. 1, pp. 291–300, 2022, doi:
10.1016/j.ejor.2021.05.028.
[27] X. Han, R. Cui, Y . Lan, Y . Kang, J. Deng, and N. Jia, “A gaussian
mixture model based combined resampling algorithm for classification of
imbalanced credit data sets,” Int. J. Mach. Learn. Cybern. , vol. 10, pp.
3687–3699, May 2019, doi: 10.1007/s13042-019-00953-2.
[28] L. Yu, R. Zhou, R. Chen, and K. K. Lai, “Missing data preprocessing
in credit classification: One-hot encoding or imputation?” Emerg.
Mark. Finance Trade , vol. 58, no. 2, pp. 472–482, 2022, doi:
10.1080/1540496X.2020.1825935.
[29] C. Seger, “An investigation of categorical variable encoding techniques
in machine learning: binary versus one-hot and feature hashing,”
Ph.D. dissertation, Elect. Eng. Comput Sci., 2018. [Online]. Available:
http://urn.kb.se/resolve?urn=urn:nbn:se:kth:diva-237426
[30] S. He, B. Li, H. Peng, J. Xin, and E. Zhang, “An effective cost-
sensitive xgboost method for malicious urls detection in imbalanced
dataset,” IEEE Access, vol. 9, pp. 93 089–93 096, 2021, doi: 10.1109/AC-
CESS.2021.3093094.
[31] C. Sammut and G. I. Webb, Encyclopedia of Machine Learning and Data
Mining, 2nd ed. New York: Springer, 2017. doi: 10.1007/978-1-4899-
7687-1.
[32] I. D. Mienye and Y . Sun, “Performance analysis of cost-sensitive
learning methods with application to imbalanced medical data,”
Informatics Medicine Unlocked , vol. 25, Art. no. 100690, 2021, doi:
10.1016/j.imu.2021.100690.
[33] T. Chen and C. Guestrin, “XGBoost: A scalable tree boosting system,” in
Proc. 22nd ACM SIGKDD Int. Conf. Knowledge Discovery Data Mining,
ser. KDD ’16. New York, NY , USA: ACM, 2016, pp. 785–794, doi:
10.1145/2939672.2939785.
[34] D. Tao, X. Li, X. Wu, and S. J. Maybank, “Geometric mean for subspace
selection,” IEEE Trans. Pattern Anal. Mach. Intell., vol. 31, no. 2, pp. 260–
274, 2009, doi: 10.1109/TPAMI.2008.70.
[35] M.-J. Kim, D.-K. Kang, and H. B. Kim, “Geometric mean based boosting
algorithm with over-sampling to resolve data imbalance problem for
bankruptcy prediction,” Expert Syst. Appl., vol. 42, no. 3, pp. 1074–1082,
2015, doi: 10.1016/j.eswa.2014.08.025.
[36] J. Akosa, “Predictive accuracy: A misleading performance measure
for highly imbalanced data,” in Proc. SAS Global Forum 2017
Conf. Cary, NC: SAS Inst. Inc., 2017. [Online]. Available: https:
//support.sas.com/resources/papers/proceedings17/0942-2017.pdf.
[37] A. Occhipinti, L. Rogers, and C. Angione, “A pipeline and comparative
study of 12 machine learning models for text classification,” Expert Syst.
Appl., vol. 201, Art. no. 117193, 2022, doi: 10.1016/j.eswa.2022.117193.
[38] S. Pafka, “benchm-ml,” https://github.com/szilard/benchm-ml, 2019.
[Online]. Available: https://github.com/szilard/benchm-ml
[39] V . Morde and V . A. Setty, “Xgboost algorithm: Long may she
reign!” Apr 2019. [Online]. Available: https://towardsdatascience.com/
vishalmorde-xgboost-algorithm-long-she-may-rein-edd9f99be63d
[40] D. Nielsen, “Tree boosting with xgboost-why does xgboost win "every"
machine learning competition?” Master’s thesis, NTNU, Trondheim,
Norway, 2016. [Online]. Available: http://hdl.handle.net/11250/2433761
18 VOLUME 11, 2023

Ghatasheh et al.: Modeling the Telemarketing Process using Genetic Algorithms and Extreme Boosting
[41] D. M. W. Powers, “Evaluation: From precision, recall and f-factor
to roc, informedness, markedness & correlation,” School Informatics
Eng., Flinders University, Adelaide, Australia, Tech. Rep. SIE-07-001,
2007. [Online]. Available: http://david.wardpowers.info/BM/Evaluation_
SIETR_2up.pdf
[42] N. V . Chawla, “Data mining for imbalanced datasets: An overview,”
in Data Mining Knowledge Discovery Handbook , O. Maimon and
L. Rokach, Eds. Boston, MA: Springer US, 2005, pp. 853–867, doi:
10.1007/0-387-25465-X_40.
[43] J. A. Hanley and B. J. McNeil, “The meaning and use of the area under a
receiver operating characteristic (roc) curve,” Radiology, vol. 143, no. 1,
pp. 29–36, 1982, doi: 10.1148/radiology.143.1.7063747.
[44] M. J. Berry and G. Linoff, Data Mining Techniques: For Marketing, Sales,
and Customer Support. New York, NY , USA: John Wiley & Sons, Inc.,
1997. [Online]. Available: https://dl.acm.org/doi/10.5555/560675.
[45] A. Saltelli, “Sensitivity analysis for importance assessment,” Risk Anal.,
vol. 22, no. 3, pp. 579–590, 2002, doi: 10.1111/0272-4332.00040.
NAZEEH GHATASHEH is an Associate Profes-
sor at the Information Technology Department of
the University of Jordan in Jordan. He holds a
B.Sc. degree in computer information systems,
which he obtained from The University of Jor-
dan in Amman, Jordan, in 2004. With a strong
commitment to academic excellence, he earned
merit-based scholarships to pursue his M.Sc. in e-
business management and his Ph.D. degree in e-
business from the University of Salento in Italy,
which he obtained in 2008 and 2011 respectively.
Throughout his academic career, he has held various leadership positions,
including Chairperson of the Information Technology and Computer Infor-
mation Systems Departments, University Liaison Officer for Quality and
Development, Dean’s Assistant for Quality and Development, Faculty Board
Member, and Director of the Computer Center at The University of Jordan
in Aqaba, Jordan.
Dr. Ghatasheh has a keen interest in applied scientific research that in-
cludes e-Business, Business Analytics, Applied Computational Intelligence,
and Data Mining. He is a team member of the funded Erasmus+ KA02
CBHE project named Edu4ALL; which aims at fair inclusion of students
with disability in higher education and establishing a technology-based
and modern accessibility unit. He is the manager of a funded project by
the University of Jordan aimed at realizing an AI-based pronunciation
assessment of spoken foreign languages.
ISMAIL ALTAHARWAreceived the B.Sc. degree
in computer science and its applications from The
Hashemite University, Jordan, in 2005, the M.Sc.
degree in computer science (emphasis in AI tech-
niques especially computational intelligence and
evolutionary computations) from Al-Balqa Ap-
plied University, Jordan, in 2008, and the Ph.D.
degree in computer science and information en-
gineering (emphasized in machine learning tech-
niques and information security) from the National
Taiwan University of Science and Technology, Taiwan, in 2014.
He is currently an Associate Professor with the Department of Computer
Information Systems, The University of Jordan, Aqaba Campus. Altaharwa’s
research interests include information security, machine learning, informa-
tion retrieval, and software engineering.
Altaharwa is the manager of Edu4ALL project at the University of Jordan.
Edu4ALL is an Erasmus+ KA02 CBHE project that aims to encourage the
inclusion of students with disability in higher education by modernizing the
legalizations and the services provided to them in the HEIs in Palestine and
Jordan. And, by establishing an accessibility unit, equipped with the latest
tools of assistive technology.
KHALED ALDEBEI is an Assistant Professor at
the Information Technology Department of the
University of Jordan in Jordan. He received a B.Sc.
degree in Software Engineering from Al-Balqa
Applied University, Jordan, in 2006, an M.Sc de-
gree in Computer Science from from Al-Balqa
Applied University, Jordan, in 2009, and a Ph.D.
degree in Computer Science from the University
of Technology, Sydney, Australia, in 2018.
Throughout his academic career, he has held
various leadership positions, including Chairperson of the Information Tech-
nology and Computer Information Systems Departments at The University
of Jordan in Aqaba, Jordan.
Dr. Aldebei has a keen interest in applied scientific research that includes
machine learning, data mining, and natural language processing. He is a team
member of the funded Erasmus+ KA02 CBHE project named Edu4ALL;
which aims at fair inclusion of students with disability in higher education
and establishing a technology-based and modern accessibility unit. He is
also a team member of a funded project by the University of Jordan
aimed at realizing an AI-based pronunciation assessment of spoken foreign
languages.
VOLUME 11, 2023 19
