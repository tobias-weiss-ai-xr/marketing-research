---
title: 'ChurnNet: A Optimized Modern AI for Churn Prediction'
url: https://arxiv.org/abs/2606.00169
category: ai-marketing
subcategory: empirical
date: 2026-05
venue: ''
authors:
- Syed Saad Saif
- Giulio Maggiore
- Paolo Russo
- Damiano Distante
source: arxiv
pdf_url: https://arxiv.org/pdf/2606.00169
pages: 15
chars: 61061
fetched_at: '2026-11-08T13:02:51+00:00'
kb_version: 1
---

# ChurnNet: A Optimized Modern AI for Churn Prediction

ChurnNet: A Optimized Modern AI for Churn Prediction
Syed Saad Saif1,2[0009−0003−4267−7060], Giulio Maggiore3[0000−0002−4657−0362], Paolo
Russo4[0000−0002−1886−3491], and Damiano Distante3[0000−0002−8467−535X]
1 Department of Computer, Control, and Management Engineering, Sapienza University of Rome,
Rome, Italy
2 Department of Law and Economics, UnitelmaSapienza University of Rome, Rome, Italy
3 R&D Center, Token Financial Technologies, Istanbul, Turkey
4 Department of Civil, Computer Science and Aeronautical Technologies Engineering,
Roma Tre University, Rome, Italy
Abstract.Increased competition and the growing similarity of products and services
offered by retailers have lowered the barriers for customers to switch to competitors. Ac-
curate churn prediction can be a valuable tool for driving effective personalized marketing
campaigns and helping to reduce customer attrition. This study evaluates the performance
of traditional machine learning techniques, namely, Random Forests, XGBoost, and Sup-
port Vector Machines, and compares them with the Unified Multi-Task Time Series Model
for churn prediction, a binary time-series classification task. Despite the strong capacity
of the latter to model complex temporal dynamics and inter-variable relationships, our
results indicate that for churn prediction, conventional methods can still outperform it in
terms of predictive performance, data efficiency, and computational resource requirements
for training and deployment. These findings are consistent across multiple datasets and
various churn labeling techniques.
Keywords:Artificialintelligence·customerchurnprediction·retailsector·non-contractual
environment·Unified Multi-Task Time Series Model·UniTS·Random Forest·XGBoost
·Support Vector Machine·SVM
1 Introduction
In recent years, the retail industry has undergone a profound transformation. The adoption of
online as well as omni-channel sales has allowed customers to have convenient access to multiple
retailers through digital platforms, unlike traditional retail, which relied primarily on physical
touch-points and local customer bases. This evolution has intensified competition and dramati-
cally lowered switching barriers [28,4] making customer retention a strategic priority for retailers
of all sizes.
Customerchurn,theprocessbywhichconsumersreduceorceasetheirpurchasingactivity,has
emerged as a critical challenge in this context. In non-contractual settings, such as e-commerce
and grocery retail, churn does not occur through formal cancellations but through behavioral
changes, such as decreased purchase frequency or volume [8]. Detecting these gradual forms of
defection is particularly challenging yet crucial, as subtle declines in customer engagement often
precede full attrition [33,17].
At the same time, the increasing availability of customer data, particularly through loyalty
programs, digital receipts, browsing histories, and CRM systems has enabled more sophisticated
approaches to customer analytics [37,18]. This abundance of data has catalyzed the application
of machine learning (ML) and artificial intelligence (AI) methods for churn prediction, which
in turn can help businesses to identify early warning signals and implement targeted retention
strategies [17,20].
AI-based churn prediction has been extensively explored incontractual industries, such as
telecommunications, banking, and insurance, with several recent surveys reviewing both tradi-
tional ML and deep learning approaches (e.g., [16,22,3]). However, thenon-contractual retail
sectorremains relatively under investigated. Differently from contractual contexts where churn
is defined by discrete events such as service cancellations, in non-contractual retail the absence
of explicit termination complicates both model design and the operationalization of churn labels
[9,29].
arXiv:2606.00169v1  [cs.LG]  29 May 2026

2 S. Saad Saif et al.
In order to develop a churn prediction system, the question regarding the most suitable ma-
chine learning approach naturally arises. On one hand, recent techniques, such as UniTS [15],
TimesNet [35], and FlowFormer [36], show impressive performance for binary time-series classifi-
cation tasks on datasets of varying domains and levels of difficulty. To achieve this performance,
these models adopt a deep and complex architecture and, therefore, are computationally expen-
sive and prone to overfitting [5]. To mitigate this issue, they are required to be trained on large
datasets. In contrast, conventional techniques have also been successfully applied to achieve good
performance in churn prediction. These models, thanks to their relatively simple architectures,
are more computationally and data-efficient. In this paper, we examine whether the compara-
tively simple nature of churn prediction as a time-series binary classification task necessitates the
use of deep, modern, but complex architectures, or if traditional, simpler models are sufficient
to deliver strong predictive performance.
For this analysis, we compared traditional machine learning models, namely, Random Forests,
XGBoost and Support Vector Machines (SVM), with the Unified Multi-Task Time Series Model
(UniTS) [15], a transformer-based model specifically designed to handle temporal data. We chose
the UniTS model to represent modern deep learning architectures, as it delivers top perfor-
mance on the time-series binary classification task [15]. The study spans multiple real-world
retail datasets and employs a family of churn labeling definitions based on relative drops in
average weekly spending over time windows. Our goal is to assess not only the raw predictive
performance (precision, recall, F1-score) but also to analyze it across datasets with varying char-
acteristics, including size and levels of imbalance. Such an analysis is important when considering
systems intended for real-world deployment. In fact, the results of this study will inform the de-
velopment of a commercial churn prediction system by Infocube5, a digital marketing solutions
provider, which supplied us with two of the datasets included in the evaluation suite of this
research.
The remainder of this paper is structured as follows. Section 2 reviews relevant studies on
AI-based churn prediction in e-commerce and retail, with a focus on applied models, recent
innovations, and the use of advanced AI techniques. Section 3 provides an overview of customer
churn predictive models used in this study, discussing their theoretical suitability for the churn
prediction task. Section 4 details our methodology, including the preparation of the datasets
and the churn labeling strategy. Section 5 describes the implementation of the models. Section 6
presents the empirical results, offering a discussion on the performance and interpretation of the
results, as well as comments on the implications of each method in practical churn prediction
scenarios. Section 7 discusses the limitations and threats to the validity of this study. Finally,
Section 8 concludes the paper and outlines potential directions for future research.
2 Related Works
Although research on churn prediction has predominantly focused on contractual environments,
a number of studies have also examined this task in non-contractual settings. These studies
employ a wide range of AI techniques. While the literature is largely centered on traditional
methods, such as Decision Trees (DT), Random Forests (RF), XGBoost (XGB), SVM, K-Nearest
Neighbors (KNN), and Logistic Regression (LR), more recent approaches, including Artificial
Neural Networks (ANN), Convolutional Neural Networks (CNN), and Long Short-Term Memory
(LSTM) networks, have been applied with varying degrees of success [32,22,11].
Rahib et al. [27] applied several traditional machine learning methods such as SVM, RF and
DT. Sunarya et al. [34] implemented LR and RF. Agbemadon et al. [1] applied both conven-
tional AI techniques, like LR and XGB, as well as modern approaches such as ANN and LSTM.
Boukrouh et al. [6] conducted a comprehensive analysis of a broad suite of AI techniques that
included DT, RF, SVM, LR, NB, KNN, and ANN. In addition to evaluating predictive per-
formance this study also and utilized explainable artificial intelligence (XAI) methods such as
Shapley Additive Explanations (SHAP) and Local Interpretable Model-agnostic Explanations
(LIME) to develop interpretations of these models.
5 https://www.infocube.it

Traditional ML Methods vs UniTS for Retail Churn Prediction 3
Beyond the application of standard techniques, some studies have focused on methodological
innovations aimed at enhancing AI model performance. Gan et al. [14] integrated social behavior
and influence dynamics into the XGBoost framework to capture the impact of customers on their
social networks. Pondel et al. [24] focused on e-commerce data, incorporating non-time-series
departmental information exprimenting with variations of ANN and Recurrent Neural Networks
(RNN) to identify the best-performing option. Miguéis et al. [23] explored the implementation
of Multivariate Adaptive Regression Splines (MARS) and benchmarked its performance against
LR. Notably, Seema et al. [31] introduced a novel approach involving a fading channel patch-
based heat map for training CNN, aiming to improve deep learning model effectiveness in the
churn prediction context.
While previous studies have explored a range of AI techniques for churn prediction, most
focus on either traditional or complex models in isolation. Our work stands out by comparing
traditional machine learning models, such as Decision Trees, Random Forests, and XGBoost,
with UniTS, a transformer-based model specifically designed for time-series data. This unique
comparison highlights the effectiveness of simpler models versus those tailored for temporal tasks,
filling a gap in the existing literature.
3 Background
3.1 Definition of Churn
In the retail sector, customer churn refers to the phenomenon in which a previously active cus-
tomer ceases or substantially reduces engagement in purchasing behavior over a defined period.
Unlike contractual settings, where churn is explicitly observed through contract terminations,
churn in retail is typically inferred from behavioral inactivity, which makes its detection more
challenging.
Labeling customers as churners in retail typically involves defining a period of inactivity or
significant drop in engagement, known as the churn window or churn horizon, beyond which a
customer is considered lost. Common approaches include fixed thresholds, such as no purchases
within 3, 6, or 12 months [19,2], or dynamic thresholds based on individual purchase patterns,
such as multiples of the customer’s average inter-purchase time or spend [26,25,30]. Some stud-
ies also apply customer segmentation and clustering approaches, probability-based scoring, or
survival analysis to estimate churn probabilities [21,12].
Accurate churn labeling is critical, as it influences both model training and the business
interpretation of churn risk. However, definitions vary widely across studies and industries.
3.2 Utilized AI Techniques
As highlighted by several literature reviews [32,22] and our previous study [11], the tradi-
tional machine learning models selected in this work are among the most widely used and well-
established AI techniques in the churn prediction literature. In contrast, UniTS represents a
modern deep learning model specifically designed for time-series data that has been successfully
applied to a variety of domains [15].
Below, we briefly describe the AI techniques used in this study, including both traditional
machine learning methods and UniTS, highlighting their key characteristics and relevance to
churn prediction.
Random ForestsRF, introduced by Breiman in 2001, addresses overfitting in decision trees by
aggregating predictions from multiple trees built on bootstrapped samples and random subsets
of features [7]. Each tree in the forest votes on the outcome, and the majority vote determines
the final prediction. This ensemble approach enhances stability and accuracy compared to a
single tree. Random Forests are particularly effective in handling high-dimensional, nonlinear
data and offer valuable insights into feature importance. In churn prediction, Random Forests
can capture complex patterns in customer behavior; however, it may be less effective at modeling
time dependencies compared to sequential models.

4 S. Saad Saif et al.
XGBoostXGBoost, released by Chen in 2016, is an efficient gradient boosting framework
designed to improve speed and performance through parallelization and regularization [10]. It
builds additive decision trees sequentially, where each new tree corrects the errors made by the
previousensembleusinggradientinformationfromalossfunction.XGBoostintegratestechniques
such as shrinkage, column subsampling, and tree pruning to prevent overfitting and enhance
performance.Itachieveshighaccuracyontabulardata,handlesmissingvalues,andmanagesclass
imbalance effectively. However, to extract its best performance, careful fine-tuning is required. In
churn prediction, XGBoost has proven to be particularly effective in capturing complex patterns
in customer behavior and handling imbalanced datasets.
Support Vector MachinesSVM, introduced in the early 1990s, aim to identify optimal sepa-
rating hyperplanes for classification tasks, using kernel functions to model nonlinear relationships
[13]. The core idea is to find the hyperplane that maximizes the margin between different classes,
while support vectors (data points closest to the boundary) define this separation. Kernel tricks
transform data into higher-dimensional spaces to make it linearly separable when needed. SVMs
are powerful in high-dimensional spaces but may encounter scalability issues with large datasets
and are particularly sensitive to class imbalance, a common challenge in churn prediction.
UniTSUniTS, introduced in 2024 by Gao et al. [15], is a unified multi-task time-series model
designed to handle forecasting, classification, anomaly detection, and imputation within a single
architecture.InspiredbyfoundationmodelsinNaturalLanguageProcessing(NLP)andcomputer
vision, it incorporates task-tokenization, attention mechanisms, and dynamic linear operators to
enable parameter sharing and adaptation across tasks. UniTS processes input sequences through
transformers equipped with specialized tokens that signal different tasks, allowing the same
network to adapt flexibly to diverse objectives. UniTS shows strong performance across diverse
datasetsbutrequiressignificantcomputationalresourcesandlarge-scalepre-training.Itscapacity
to capture complex temporal patterns makes it theoretically well-suited for modeling customer
behavior over time, such as in churn prediction.
4 Methodology
Our methodology follows a structured pipeline designed to prepare transactional data, generate
churn labels, and evaluate multiple machine learning models. An overview of the entire training
and evaluation process is presented in Figure 1.
The process begins with dataset pre-processing and filtering, where raw transactional data is
cleaned and transformed into time series for each customer. Next, customers are labeled based on
different churn definitions. For model training, temporal windows are selected. Various balancing
and sub-sampling strategies are subsequently applied. This produces multiple representative
training datasets, which are then used to train machine learning models and evaluate their
performance. The following subsections provide a detailed explanation each step.
4.1 Dataset Pre-processing
The goal of this step is to clean the data, remove anomalies, and establish a standardized and
consistent starting point for analysis. During pre-processing, transactional data is aggregated by
customer ID and filtered to exclude non-positive values. Additionally, transaction amounts are
aggregated on a weekly basis to ensure temporal consistency across the dataset. The dataset is
also converted into time series data by zero-padding the weeks where no transactions occurred
for a customer.
4.2 Dataset Filtering
To ensure the reliability of predictions, we focus on customers with a sufficient transactional
history. Customers with limited activity provide insufficient behavioral patterns for meaningful
analysis and are typically of lower commercial interest. Therefore, in our study, we exclude

Traditional ML Methods vs UniTS for Retail Churn Prediction 5
customers with fewer than 20 transactional weeks i.e., weeks during which the customer made
at least one transaction.
IC1 IC2 CJ LGSR
Dataset
Pre-processing
Dataset
Filtering
Churn Def. A
Feature
Windowing
Datasets
Churn Labeling
UniTS XGBoost RF SVM
Model Training
Model
Evaluation
Churn Def. A Churn Def. A
1:1 1:4 B-SS
Balancing and Subsampling
Fig. 1.Data processing, training and evaluation pipeline of
the proposed methodology.
T able 1.Churn Labeling Definitions.
Churn Definition α β
A 0.3 0.3
B 0.4 0.4
C 0.5 0.5
Labeling Condition Churner
Label: 1
Non-churner
Label: 0
Yes
No
Weekly Spending - Sample Time Series
Fig. 2.Churn labeling strategy.
Week Number
Spending
Selected Window
Weekly Spending - Churned Customer
(a) Churn customer.
Week Number
Spending
Selected Window
Weekly Spending - Non-Churned Customer
(b) Non-churn customer.
Fig. 3.Feature windowing strategies.
4.3 Churn Labeling
As discussed in the background section 3, churn labeling in non-contractual settings is a non-
trivial task, with various approaches available depending on the use case and data characteristics.
In this work, we adopt a dynamic churn definition, formulated in collaboration with Infocube
and tailored to the needs of their retail clients. This approach aims to provide a more accurate
and individualized churn label by accounting for each customer’s historical shopping behavior.
We define two key timeframes: anobservation windowof lengthA= 40weeks and a subse-
quentlabeling windowof lengthB= 20weeks. The two windows are contiguous and are aligned
with the end date of their respective dataset. The observation window is used to calculate per-
sonalized thresholds which are then applied to the labeling window to determine each customer’s
churn status.
The labeling logic is based on two behavioral parameters, which are elaborated below:

6 S. Saad Saif et al.
– Monetary value: The average weekly spending in the observation window is denoted by
µA, and in the labeling window byµB.
– Frequency of activity: The average number of transactions per week in the observation
window is denoted byfA, and byfB in the labeling window.
A customer is labeled as achurner(1) if both of the following conditions are met:
α·µ A > µB andβ·f A > fB (1)
Otherwise, the customer is labeled as anon-churner(0). Here,αandβare configurable
threshold parameters, which control the sensitivity of the churn detection logic. By evaluating
changes relative to each customer’s historical behavior, this method reduces noise and provides
a more robust and personalized definition of churn.
A visual illustration of this labeling method, showing the positioning of the observation and
labeling windows, is provided in Figure 2.
We employed three different churn labeling definitions by adjusting the sensitivity parameters
αandβ, as summarized in Table 1. These variants enable us to evaluate the robustness of our
models under different churn detection thresholds.
4.4 Feature Windowing
The feature window refers to the time period over which input features (X) are passed to our
models for training. In our study, this window is set to a fixed length of 20 weeks. The selection
of the feature window depends on the churn label assigned to the customer:
– For churners, the feature window ends immediately before the customer’s final period of
sustained inactivity.
– For non-churners, a random valid segment of 20 weeks is selected from the customer’s
available transaction history.
This strategy is motivated by the assumption that, for churners, churn-related behavioral
patterns are likely to be more pronounced in the period leading up to the churn event. Therefore,
capturing this window enables the model to learn relevant dynamics associated with customer
disengagement. In contrast, for non-churners, there is no a priori knowledge about when, or if,
such patterns might occur, so a random 20-week segment is selected to provide a representative
sample of normal activity.
An illustrative example of the feature windowing process for both churners and non-churners
is provided in Figure 3.
4.5 Balancing and Subsampling
To assess the impact of dataset size and class imbalance on model performance, we employed the
following dataset balancing and sub-sampling strategies:
– Balanced Dataset (1:1): These datasets include all churners remaining after filtering. An
equal number of non-churners are then randomly sampled to create a balanced dataset.
This setting is designed to neutralize the impact of class imbalance on model performance.
Although this reduces the total amount of data used for training, it is less of a concern for
large-scale datasets.
– Limited Unbalanced Dataset (1:4): In this setting, all filtered churners are retained, and
four times as many non-churners are randomly sampled. This controlled imbalance allows us
to evaluate model performance under moderately imbalanced conditions while still utilizing
more training data. It provides insight into how well models handle class imbalance in a
realistic yet constrained scenario.
– Balanced Subsampled Dataset (B-SS): To investigate the data efficiency of differ-
ent models, especially on smaller datasets, we created downsampled versions of the larger
datasets. Forsingle-star (*)datasets, we randomly select 2,500 customers after filtering; all
churners are included, and an equal number of non-churners are sampled. Fordouble-star
(**)datasets, the same process is applied with 5,000 customers. This setting allows us to
isolate the impact of dataset size on performance while maintaining balance.

Traditional ML Methods vs UniTS for Retail Churn Prediction 7
T able 2.Dataset Characteristics.
Normalized
T enure Ratio Number of Customer Before Balancing After Balancing
Churn
Def. Cat. Data T otalCH N-CH CH CH N-CH CH N-CH
A
1:1
IC1 0.92 0.69 0.94 0.08 12,425 143,454 12,425 12,425
IC2 0.89 0.71 0.90 0.09 35,309 360,585 35,309 35,309
CJ 0.90 0.75 0.90 0.03 72 2,060 72 72
LGSR 0.94 0.76 0.94 0.01 1,500 283,880 1,500 1,500
1:4
IC1 0.92 0.69 0.94 0.08 12,425 143,454 12,425 49,700
IC2 0.89 0.71 0.90 0.09 35,309 360,585 35,309 141,236
CJ 0.90 0.75 0.90 0.03 72 2,060 72 288
LGSR 0.94 0.76 0.94 0.01 1,500 283,880 1,500 6,000
B-SS
IC1* 0.92 0.69 0.94 0.08 12,425 143,454 390 390
IC2* 0.89 0.71 0.90 0.09 35,309 360,585 416 416
IC1** 0.92 0.69 0.94 0.08 12,425 143,454 200 200
IC2** 0.89 0.71 0.90 0.09 35,309 360,585 220 220
B
1:1
IC1 0.92 0.74 0.94 0.11 16,808 139,071 16,808 16,808
IC2 0.89 0.74 0.90 0.11 43,291 352,603 43,291 43,291
CJ 0.90 0.79 0.90 0.06 124 2,008 124 124
LGSR 0.94 0.78 0.94 0.01 3,338 282,042 3,338 3,338
1:4
IC1 0.92 0.74 0.94 0.11 16,808 139,071 16,808 67,232
IC2 0.89 0.74 0.90 0.11 43,291 352,603 43,291 173,164
CJ 0.90 0.79 0.90 0.06 124 2,008 124 496
LGSR 0.94 0.78 0.94 0.01 3,338 282,042 3,338 13,352
B-SS
IC1* 0.92 0.74 0.94 0.11 16,808 139,071 540 540
IC2* 0.89 0.74 0.90 0.11 43,291 352,603 509 509
IC1** 0.92 0.74 0.94 0.11 16,808 139,071 275 275
IC2** 0.89 0.74 0.90 0.11 43,291 352,603 270 270
C
1:1
IC1 0.91 0.78 0.94 0.14 21,858 134,021 21,858 21,858
IC2 0.89 0.76 0.90 0.13 52,989 342,905 52,989 52,989
CJ 0.89 0.80 0.90 0.07 158 1,974 158 158
LGSR 0.93 0.79 0.94 0.02 6,537 278,843 6,537 6,537
1:4
IC1 0.91 0.78 0.94 0.14 21,858 134,021 21,858 87,432
IC2 0.89 0.76 0.90 0.13 52,989 342,905 52,989 211,956
CJ 0.89 0.80 0.90 0.07 158 1,974 158 632
LGSR 0.93 0.79 0.94 0.02 6,537 278,843 6,537 26,148
B-SS
IC1* 0.91 0.78 0.94 0.14 21,858 134,021 690 690
IC2* 0.89 0.76 0.90 0.13 52,989 342,905 636 636
IC1** 0.91 0.78 0.94 0.14 21,858 134,021 356 356
IC2** 0.89 0.76 0.90 0.13 52,989 342,905 326 326
T able 3.Dataset statistics.
Data
Name
Total
Weeks
Transactional
Weeks
Number
of
Customers
Average
Transactional
Weeks
per Customer
Normalized
Average
Transactional
Weeks
per Customer
IC1 78 8,484,586 490,138 17.31 0.22
IC2 115 25,097,111 937,507 26.77 0.23
CJ 102 123,888 2,500 49.56 0.49
LGSR 117 20,527,165 494,880 41.48 0.35
(a) Before filtering.
Data
Name
Total
Weeks
Transactional
Weeks
Number
of
Customers
Average
Transactional
Weeks
per Customer
Normalized
Average
Transactional
Weeks
per Customer
IC1 78 6,507,930 155,879 41.75 0.54
IC2 115 21,642,961 395,894 54.67 0.48
CJ 102 119,642 2,132 56.12 0.55
LGSR 117 19,318,828 285,380 67.70 0.58
(b) After filtering.
4.6 Model Training and Evaluation
In this step, we train multiple machine-learning models on the prepared datasets and evaluate
their performance using the selected classification metrics. Section 5 provides implementation
details, covering model architectures, hyperparameters, the experimental setup, libraries, and
computational environment.
Dataset Information
In total, four dataset sources were used: two proprietary datasets provided by Infocube (denoted
as IC1 and IC2), and two publicly available datasets,The Complete JourneyandLet’s Get Sort
of Real(denoted as CJ and LGSR, respectively)6. The main characteristics of these sources are
summarized in Table 4a for the unfiltered datasets and in Table 4b after filtering was applied. In
these tables, theTransactional Weeksfield for each dataset source is calculated by counting, for
each customer, the weeks in which they made at least one transaction, and then summing these
countsacrossallcustomers.Average Transactional Weeks per Customergivestheaveragenumber
of transactional weeks per customer.Normalized Average Transactional Weeks per Customer
scales this value by the total period, showing the average transaction frequency per week per
customer.
6 https://www.dunnhumby.com/source-files/

8 S. Saad Saif et al.
From the four dataset sources, we constructed 36 distinct datasets by applying the three
churn-labeling definitions introduced in Subsection 4.3, together with the three balancing and
subsampling strategies described in Subsection 4.5. Table 2 summarizes the resulting dataset
families and their characteristics: theCat.column indicates whether a dataset is subsampled
or balanced/imbalanced; N-CH and CH denote non-churners and churners, respectively. The
Normalized Tenurerepresents each customer’s active span divided by the total number of weeks.
The churn ratio, along with the number of customers both before and after the balancing step,
is also reported.
5 Implementation
This section outlines the implementation details, experimental environment, and model-specific
hyperparameters used in the study. All experiments were conducted using Python 3.10.9, with
core data processing handled using pandas 1.5.3 and numpy 1.24.4.
Sktime 0.16.1 was used for handling and converting time series data structures. Scikit-learn
1.7.0 was employed for evaluating model performance using metrics such asaccuracy,precision,
recall,F1-score, andROC-AUC, and also for implementing models such as Support Vector Ma-
chines and Random Forests. The implementation details and hyperparameter configurations for
each model are described below.
5.1 UniTS
The UniTS models were implemented using the official UniTS framework, publicly available
on GitHub7. All experiments were conducted using PyTorch 2.0.0, with GPU acceleration to
enhance training efficiency.
The UniTS framework supports a variety of training paradigms, including prompt learning,
few-shot learning, zero-shot inference, and supervised learning.
– Prompt learningenables the model to adapt to new tasks using learned task-specific
prompt tokens, without modifying the underlying model weights.
– Few-shot learningallows the model to generalize to new tasks using only a small number
of labeled examples.
– Zero-shot inferenceleverages the pre-trained model’s representations to perform tasks for
which it has not been explicitly trained.
– Supervised learningrefers to traditional fine-tuning using fully labeled datasets for a
specific downstream task.
In the original UniTS paper, the supervised learning approach yielded the best overall perfor-
mance. Consequently, we adopt this approach in our study to showcase the full potential of the
model. Rather than training from randomly initialized weights, we leveraged transfer learning by
initializingthemodelwiththepubliclyavailablecheckpointunits_x64_supervised_checkpoint.pth 8,
obtained from the official UniTS release repository.
It is worth noting that we did not perform extensive hyperparameter tuning for UniTS. This
decision aligns with the framework’s design philosophy, which emphasizes plug-and-play usability
over complex configuration.
The key hyperparameters and training settings used in our experiments are summarized in
Table 5a. As discussed in Section 7, more targeted tuning of UniTS-specific hyperparameters or
the use of different transformer-based architectures may yield different outcomes and insights.
Therefore, the performance results presented here for UniTS should be taken as reflective of the
potential performance of transformer-based architectures in general.
7 https://github.com/mims-harvard/UniTS
8 https://github.com/mims-harvard/UniTS/releases/tag/ckpt

Traditional ML Methods vs UniTS for Retail Churn Prediction 9
5.2 XGBoost
Experiments with XGBoost were conducted using theXGBClassifierinterface from version
3.0.2. The model was trained using the binary logistic objective for churn classification. Feature
values were used in their raw form without normalization, as the model is robust to unscaled
input. The hyperparameters used are summarized in Table 5c.
5.3 Support Vector Machine
Support Vector Machine models were implemented using theSVCclass from the scikit-learn
library, version1.7.0. Before training, the input features were standardized usingStandard-
Scaler, which centers each feature around a zero mean and unit variance. This scaling step is
essential for distance-based models like SVM to function properly.
The classifier was trained using a radial basis function (RBF) kernel. Table 5d lists the
hyperparameters used.
5.4 Random Forest
Random Forest models were implemented using theRandomForestClassifierclass from scikit-
learn version 1.7.0. No feature scaling was applied prior to training, as tree-based models are
invariant to the scale of input features.
Table 5b shows the configuration used for the Random Forest model.
T able 4.Model Hyperparameters.
Parameter V alue Description
prompt_num 10 Number of prompts used in the model
patch_len 16 Patch length for input sequences
stride 16 Stride for patching
e_layers 3 Number of encoder layers
d_model 64 Embedding dimension
learning_rate 1e-4 Fine-tuning learning rate
weight_decay5e-6 L2 regularization
train_epochs 10 Number of training epochs
batch_size 32 Mini-batch size
acc_it 32 Gradient accumulation steps
clip_grad 100 Gradient clipping threshold
fix_seed 42 For reproducibility
is_training 1 Enables training mode
lradj supervised Learning rate scheduler type
task_type classification Only classification task used
(a) UniTS.
Parameter V alueDescription
n_estimators 100 Number of trees in the ensemble
random_state 42 For reproducibility
(b) Random Forest.
Parameter V alue Description
objective binary:logistic For binary classification
n_estimators 100 Number of boosting rounds
max_depth 4 Limits tree complexity to reduce overfitting
learning_rate 0.1 Moderate rate for stable convergence
subsample 0.8 Random subset of data per tree
colsample_bytree 0.8 Subset of features per tree
random_state 42 For reproducibility
eval_metric logloss Log-loss used during training
(c) XGBoost.
Parameter V alueDescription
kernel rbf Radial basis function kernel
C 1.0 Regularization parameter
gamma scale Kernel coefficient based on number of features
probability True Enables probability estimates (used for ROC-AUC)
random_state 42 For reproducibility
(d) SVM.
All experiments were conducted on a system with an AMD Ryzen 9 7950X CPU, 64 GB
DDR5 RAM, two NVIDIA RTX 4090 GPUs, a 2 TB NVME SSD, running Ubuntu LTS 22.04.
6 Results
In this section, we evaluate the models using standard performance metrics: Accuracy, Precision,
Recall, F1-score, and AUC-ROC. These metrics are particularly relevant for churn prediction,
where datasets are often imbalanced. In such cases, AUC-ROC provides a more reliable basis for
performance comparison across models. Moreover, both false positives and false negatives carry
significant business implications: excessive false positives may lead to unnecessary spending on
customer retention, while false negatives can result in missed opportunities to intervene with

10 S. Saad Saif et al.
actual churners. Consequently, Precision and Recall serve as critical complementary measures,
providing deeper insights into these trade-offs.
The evaluation is conducted on 36 datasets derived from four raw data sources, as detailed in
Section 4. To ensure a robust comparison, the datasets were systematically constructed with con-
trolled variations in size, class imbalance, and churn definitions (A, B, and C). The corresponding
results are reported in Table 5.
We observe that the tree-based models,XGBoostandRandom Forest, consistently outper-
form both the transformer-basedUniTSarchitecture and the more conventionalSupport Vector
Machine(SVM) under all the conditions mentioned above.
We first contrast the performance under standard conditions with sufficient dataset size,
namely the datasets generated from the data sourcesIC1,IC2, andLGSRunder balanced (1:1)
and limited unbalanced (1:4) conditions. The datasets generated from theCJdata source and all
datasets under theB-SScategories are considered data-scarce, i.e., due to the limited number of
training examples, model performance is, in some cases, severely limited. We discuss and contrast
model performance under these conditions separately in Subsection 6.2.
When applyingChurn Definition-Ato balanced datasets (1:1),XGBoostachieves the highest
accuracy of0.77onIC1, closely followed byRandom Forestat0.76, whileUniTSandSVM
remain lower at0.72. The superiority of tree-based models holds acrossIC2andLGSRas well.
Accuracy is reported here, as it serves as a sufficient metric to evaluate performance under
balanced conditions.
When shifting to the imbalanced datasets (1:4), we contrast precision and recall metrics to
more effectively highlight performance differences under this imbalance. OnIC1, the precision
ranking is as follows:Random Forest(0.76),XGBoost(0.75),SVM(0.70), andUniTS(0.69). For
recall,XGBoostachieves the highest value of0.47, followed byRandom Forestat0.43,UniTS
at0.35, andSVMat only0.09. Similar patterns are observed onIC2andLGSR, confirming the
superior performance of tree-based methods also under class imbalance.
Comparable trends hold under the alternative churn definitions B and C as well.
Below, we further analyze how model performance varies with class imbalance, dataset size,
and different churn definitions, providing detailed insights into model-specific behavior.
6.1 Performance by Churn Definition
Increasing the churn threshold (moving fromChurn Definition AtoChurn Definition C) gen-
erally improves performance across all models. For example, on the 1:1 balanced IC1 dataset,
UniTS achieves an accuracy of0.72underChurn Definition A, which rises to0.74underChurn
Definition B, and further improves to0.75under the most lenient threshold,Churn Definition C.
This increased performance could be due to an increase in the number of dataset samples
used for training.
Note that since we use sub-sampling to limit dataset imbalance, increasing the size of the
minority class, which is the churn class in this instance, increases the total number of samples
used for training. As can be seen in Table 2, by moving to a more lenient definition, fromChurn
Definition AtoChurn Definition C, the number of customers classified as churners increases. For
example, for theIC2data source, the churn rate increases from 8% underChurn Definition Ato
11% underChurn Definition B, and to 14% underChurn Definition C. This corresponds to an
increase in the total number of customers in the dataset from 24,850 to 43,716 betweenChurn
Definitions AandChurn Definition-C.
Another reason for the improved performance could be that churn prediction under a more le-
nient definition is an easier task, as the classes are more easily separable. ForChurn Definition A,
both the monetary value and frequency of a customer must drop by 70% between the observation
and labeling window. Customers exhibiting such an aggressive drop may represent involuntary
churners, e.g., those who have churned due to relocation or unexpected life events, where the
weeks leading up to the churn event might not show strong behavioral signals indicative of churn.

Traditional ML Methods vs UniTS for Retail Churn Prediction 11
T able 5.Model results.
Cat. Data Metrics UniTS XGB RF SVM
1:1
IC1
Accuracy 0.72 0.77 0.76 0.72
Precision 0.72 0.77 0.75 0.74
Recall 0.74 0.78 0.78 0.67
F1-score 0.73 0.77 0.76 0.70
ROC-AUC 0.80 0.87 0.87 0.77
IC2
Accuracy 0.78 0.81 0.81 0.77
Precision 0.78 0.81 0.81 0.82
Recall 0.77 0.82 0.80 0.69
F1-score 0.77 0.82 0.81 0.75
ROC-AUC 0.87 0.91 0.91 0.83
CJ
Accuracy 0.52 0.72 0.72 0.62
Precision 0.57 0.85 0.85 0.69
Recall 0.76 0.65 0.65 0.65
F1-score 0.65 0.73 0.73 0.67
ROC-AUC 0.50 0.76 0.76 0.65
LGSR
Accuracy 0.80 0.94 0.93 0.83
Precision 0.80 0.93 0.93 0.82
Recall 0.84 0.95 0.95 0.90
F1-score 0.82 0.94 0.94 0.86
ROC-AUC 0.88 0.98 0.98 0.92
1:4
IC1
Accuracy 0.84 0.86 0.86 0.81
Precision 0.69 0.75 0.76 0.70
Recall 0.35 0.47 0.43 0.09
F1-score 0.46 0.57 0.55 0.17
ROC-AUC 0.81 0.86 0.86 0.78
IC2
Accuracy 0.87 0.87 0.87 0.83
Precision 0.73 0.74 0.76 0.71
Recall 0.52 0.57 0.51 0.24
F1-score 0.60 0.64 0.61 0.35
ROC-AUC 0.88 0.90 0.90 0.81
CJ
Accuracy 0.28 0.94 0.96 0.86
Precision 0.11 0.80 0.89 0.00
Recall 0.60 0.80 0.80 0.00
F1-score 0.19 0.80 0.84 0.00
ROC-AUC 0.45 0.91 0.93 0.86
LGSR
Accuracy 0.85 0.94 0.94 0.85
Precision 0.68 0.86 0.88 0.83
Recall 0.52 0.86 0.81 0.39
F1-score 0.59 0.86 0.85 0.53
ROC-AUC 0.86 0.97 0.98 0.90
B-SS
IC1*
Accuracy 0.49 0.73 0.72 0.67
Precision 0.52 0.75 0.76 0.75
Recall 0.67 0.75 0.72 0.59
F1-score 0.59 0.75 0.74 0.66
ROC-AUC 0.47 0.84 0.84 0.72
IC2*
Accuracy 0.47 0.78 0.78 0.68
Precision 0.51 0.78 0.78 0.70
Recall 0.64 0.83 0.83 0.69
F1-score 0.57 0.81 0.81 0.70
ROC-AUC 0.48 0.87 0.87 0.74
IC1**
Accuracy 0.49 0.80 0.78 0.57
Precision 0.51 0.77 0.76 0.62
Recall 0.74 0.88 0.83 0.50
F1-score 0.60 0.82 0.80 0.55
ROC-AUC 0.50 0.85 0.86 0.69
IC2**
Accuracy 0.49 0.75 0.77 0.73
Precision 0.54 0.80 0.86 0.82
Recall 0.76 0.74 0.72 0.66
F1-score 0.63 0.77 0.78 0.73
ROC-AUC 0.46 0.82 0.85 0.72
(a) A (α= 0.3,β= 0.3)
Cat. Data Metrics UniTS XGB RF SVM
1:1
IC1
Accuracy 0.74 0.79 0.78 0.73
Precision 0.74 0.80 0.81 0.76
Recall 0.74 0.77 0.75 0.68
F1-score 0.74 0.78 0.78 0.72
ROC-AUC 0.82 0.89 0.88 0.79
IC2
Accuracy 0.80 0.83 0.82 0.74
Precision 0.81 0.82 0.82 0.76
Recall 0.78 0.83 0.82 0.71
F1-score 0.79 0.83 0.82 0.73
ROC-AUC 0.88 0.91 0.91 0.82
CJ
Accuracy 0.54 0.92 0.92 0.70
Precision 0.49 0.91 0.88 0.65
Recall 0.77 0.91 0.95 0.68
F1-score 0.60 0.91 0.91 0.67
ROC-AUC 0.62 0.96 0.97 0.77
LGSR
Accuracy 0.80 0.95 0.94 0.84
Precision 0.80 0.92 0.92 0.79
Recall 0.79 0.97 0.97 0.91
F1-score 0.79 0.95 0.95 0.85
ROC-AUC 0.88 0.98 0.98 0.92
1:4
IC1
Accuracy 0.85 0.87 0.87 0.83
Precision 0.71 0.76 0.77 0.75
Recall 0.46 0.53 0.49 0.22
F1-score 0.56 0.62 0.60 0.34
ROC-AUC 0.84 0.88 0.88 0.81
IC2
Accuracy 0.87 0.88 0.87 0.83
Precision 0.73 0.73 0.75 0.71
Recall 0.56 0.61 0.55 0.23
F1-score 0.64 0.66 0.64 0.35
ROC-AUC 0.89 0.91 0.91 0.83
CJ
Accuracy 0.35 0.93 0.92 0.85
Precision 0.17 0.93 1.00 1.00
Recall 0.71 0.62 0.52 0.14
F1-score 0.27 0.74 0.69 0.25
ROC-AUC 0.51 0.98 0.97 0.85
LGSR
Accuracy 0.87 0.94 0.94 0.86
Precision 0.71 0.84 0.85 0.81
Recall 0.59 0.87 0.84 0.42
F1-score 0.65 0.86 0.85 0.56
ROC-AUC 0.90 0.98 0.98 0.92
B-SS
IC1*
Accuracy 0.47 0.77 0.75 0.69
Precision 0.46 0.73 0.73 0.65
Recall 0.73 0.80 0.76 0.72
F1-score 0.56 0.76 0.74 0.69
ROC-AUC 0.55 0.86 0.86 0.75
IC2*
Accuracy 0.49 0.77 0.78 0.73
Precision 0.50 0.75 0.76 0.75
Recall 0.74 0.82 0.83 0.70
F1-score 0.60 0.79 0.79 0.73
ROC-AUC 0.49 0.86 0.87 0.77
IC1**
Accuracy 0.55 0.78 0.85 0.76
Precision 0.58 0.82 0.87 0.80
Recall 0.78 0.79 0.87 0.78
F1-score 0.66 0.81 0.87 0.79
ROC-AUC 0.50 0.88 0.90 0.83
IC2**
Accuracy 0.54 0.81 0.81 0.66
Precision 0.57 0.84 0.88 0.71
Recall 0.72 0.84 0.75 0.66
F1-score 0.64 0.84 0.81 0.68
ROC-AUC 0.61 0.91 0.91 0.78
(b) B (α= 0.4,β= 0.45)
Cat. Data Metrics UniTS XGB RF SVM
1:1
IC1
Accuracy 0.75 0.80 0.80 0.75
Precision 0.74 0.81 0.81 0.77
Recall 0.77 0.79 0.78 0.71
F1-score 0.76 0.80 0.80 0.74
ROC-AUC 0.82 0.89 0.89 0.81
IC2
Accuracy 0.80 0.84 0.83 0.79
Precision 0.80 0.83 0.83 0.83
Recall 0.80 0.85 0.83 0.72
F1-score 0.80 0.84 0.83 0.77
ROC-AUC 0.89 0.92 0.92 0.85
CJ
Accuracy 0.56 0.81 0.81 0.75
Precision 0.54 0.81 0.81 0.70
Recall 0.84 0.81 0.81 0.88
F1-score 0.66 0.81 0.81 0.78
ROC-AUC 0.61 0.85 0.86 0.79
LGSR
Accuracy 0.79 0.93 0.93 0.83
Precision 0.76 0.91 0.91 0.78
Recall 0.87 0.96 0.96 0.92
F1-score 0.81 0.94 0.93 0.84
ROC-AUC 0.89 0.97 0.97 0.91
1:4
IC1
Accuracy 0.86 0.88 0.87 0.84
Precision 0.70 0.74 0.76 0.73
Recall 0.49 0.57 0.53 0.27
F1-score 0.58 0.65 0.63 0.40
ROC-AUC 0.86 0.89 0.90 0.82
IC2
Accuracy 0.87 0.88 0.88 0.83
Precision 0.72 0.74 0.75 0.70
Recall 0.59 0.64 0.59 0.30
F1-score 0.65 0.69 0.66 0.42
ROC-AUC 0.90 0.92 0.92 0.84
CJ
Accuracy 0.39 0.90 0.85 0.80
Precision 0.24 0.88 0.83 0.80
Recall 0.80 0.63 0.43 0.11
F1-score 0.37 0.73 0.57 0.20
ROC-AUC 0.61 0.94 0.94 0.83
LGSR
Accuracy 0.87 0.94 0.93 0.86
Precision 0.71 0.82 0.83 0.76
Recall 0.54 0.87 0.82 0.43
F1-score 0.61 0.84 0.83 0.55
ROC-AUC 0.90 0.97 0.97 0.92
B-SS
IC1*
Accuracy 0.73 0.76 0.78 0.71
Precision 0.79 0.77 0.80 0.71
Recall 0.63 0.76 0.76 0.74
F1-score 0.70 0.76 0.78 0.72
ROC-AUC 0.79 0.88 0.88 0.78
IC2*
Accuracy 0.73 0.85 0.85 0.75
Precision 0.78 0.87 0.86 0.73
Recall 0.64 0.84 0.83 0.81
F1-score 0.70 0.85 0.85 0.77
ROC-AUC 0.80 0.93 0.93 0.84
IC1**
Accuracy 0.47 0.75 0.71 0.66
Precision 0.47 0.77 0.72 0.63
Recall 0.72 0.68 0.67 0.71
F1-score 0.57 0.72 0.69 0.67
ROC-AUC 0.49 0.82 0.83 0.71
IC2**
Accuracy 0.50 0.82 0.83 0.69
Precision 0.53 0.83 0.84 0.72
Recall 0.68 0.83 0.86 0.74
F1-score 0.60 0.83 0.85 0.73
ROC-AUC 0.54 0.86 0.86 0.78
(c) C (α= 0.5,β= 0.5)
6.2 Impact of Class Imbalance
In imbalanced classification settings, accuracy becomes a misleading metric, as any apparent gain
is largely driven by the dominance of the non-churner class. To properly capture the models’
ability to detect churners, we instead evaluate performance using precision and recall. Precision
measures how many of the predicted churners are truly churners, while recall measures how many
of the actual churners the model successfully identifies. These metrics are more informative under
imbalance, as they directly reflect performance on the minority class, which is the primary focus
in churn prediction for real-world scenarios.
When transitioning from balanced (1:1) to imbalanced (1:4) datasets, model performance
generally decreases as the class ratio becomes more skewed. The observed trend shows that
this decline is most pronounced for models that are highly sensitive to class distribution, such
as SVM, while tree-based methods (XGB, RF) and the transformer-based UniTS demonstrate
greater robustness.
For example, under the IC2 dataset withChurn Definition A, the following results are ob-
served when moving from a balanced to an imbalanced setting. For UniTS, precision decreases
from0.78to0.73and recall drops from0.77to0.52. For XGB, precision declines from0.81to

12 S. Saad Saif et al.
0.74and recall decreases from0.82to0.57. For RF, precision goes from0.81to0.76and recall
falls from0.80to0.51. Finally, for SVM, precision decreases from0.82to0.71, but recall collapses
dramatically from0.69to0.24.
These results reveal a clear pattern: while precision remains relatively stable across all mod-
els, recall suffers a substantial decline under imbalance. This indicates that models become less
effective at identifying churners as the minority class becomes underrepresented. Among the eval-
uated methods, tree-based models (XGB and RF) and the transformer-based UniTS demonstrate
better resilience, maintaining moderate recall values even when the class distribution is skewed.
SVM experiences the most severe performance degradation under imbalance because, in the
soft-margin setting, the separating hyperplane becomes skewed toward the minority class. As
imbalance grows, the ratio of positive to negative support vectors becomes more imbalanced
and samples near the margin are more likely to be classified as negative. While its precision
decreases moderately (0.82→0.71), recall collapses to0.24because the model fails to predict
churners effectively. This consistent trend demonstrates SVM’s sensitivity to class imbalance and
it’s worse performance compared to XGB, RF, and UniTS, which handle skewed distributions
more robustly.
6.3 Small Dataset and Data Efficiency Analysis
Since the datasets considered in this section are balanced (1:1), the accuracy metric is sufficient
for comparing performance. As the dataset size decreases, the performance of all models generally
declines,althoughthedegreeofdegradationunderdatascarcityvariessignificantlyacrossmodels.
As a representative example, we examine the IC2 dataset underChurn Definition C(see
Table 2), where IC2 represents the full dataset, IC2* is a considerably smaller subset, and IC2**
is approximately half the size of IC2*. Under these settings, UniTS achieves an accuracy of
0.80on the full IC2 dataset but drops to0.73under IC2*, and further collapses to0.50on
IC2**. XGB achieves0.84accuracy on IC2 and maintains a strong0.85on IC2*, before slightly
decreasing to0.82under IC2**. Similarly, RF obtains0.83accuracy on IC2, remains stable at
0.85on IC2*, and retains0.83on IC2**. In contrast, SVM performs reasonably well on the full
IC2 dataset with0.79accuracy and drops slightly to0.75under IC2*, but declines further to
0.69on IC2**. While these numbers are reported for IC2 as an example, similar patterns are
consistently observed across other datasets.
These results reveal a clear and consistent pattern: tree-based models (XGB and RF) exhibit
strong robustness under limited data availability, retaining high accuracy even when datasets are
significantly reduced. SVM shows moderate resilience but suffers more noticeable degradation
in extremely low-resource scenarios. UniTS, on the other hand, demonstrates a consistent trend
of severe performance deterioration when data becomes scarce, confirming that it struggles to
generalize effectively without sufficient training samples.
Transformer-based models like UniTS require larger datasets due to their higher complex-
ity and large parameter count. Unlike tree-based methods, which generalize well with limited
samples, transformers need abundant data to effectively capture temporal patterns and learn
stable representations. In scarce-resource scenarios, the limited number of examples reduces the
diversity of behavioral signals, making it harder for the model to distinguish churners from non-
churners.
7 Threats to Validity
This section discusses potential limitations and factors that may affect the validity and general-
izability of the findings presented in this study.
Limitations of Dataset, Applied Churn Definition, and Filtering Techniques
Although the experiments were conducted on multiple datasets and under different churn defini-
tions, the scope of this study remains limited, and the results may not fully generalize to all churn
prediction tasks in retail contexts. In domains where consumer behavior is more complex, the

Traditional ML Methods vs UniTS for Retail Churn Prediction 13
UniTS model could have greater opportunities to capture intricate interdependencies, potentially
leading to improved performance.
Moreover, while several churn labeling strategies were explored based on Infocube’s require-
ments, the study does not cover the full spectrum of possible churn definitions. Alternative
labeling schemes may substantially change the framing of the classification task and, in turn,
affect model performance.
Finally, the dataset filtering procedure also introduces limitations to the applicability of our
results, as customers with fewer than 20 transactional weeks were excluded. While this threshold
was justified in our case, ensuring that the analysis focused on customers with sufficient transac-
tional history to produce more reliable predictions, it can restrict the transferability of findings
to other domains. For instance, in e-commerce or other retail environments where shorter cus-
tomer life-cycles are common and business objectives may differ, models could produce different
outcomes when applied to customers with limited histories.
Considerations Regarding Transformer-Based Methods
This work does not attempt to exhaustively optimize transformer-based models for churn pre-
diction. Since UniTS is designed as a user-friendly, plug-and-play platform without the need for
extensive model tuning, the reported results are valid for performance comparisons under default
configurations. However, it remains possible that transformer-based approaches with architec-
ture, optimizers, and hyperparameters specifically fine-tuned for churn prediction tasks could
achieve superior results.
8 Conclusion
This study presents a comprehensive comparison between conventional machine learning models
and the transformer-based UniTS model for the task of churn prediction in non-contractual retail
environments. By conducting a rigorous evaluation of the models across 36 datasets with varying
levels of imbalance, size, and churn definitions, we shed light on the performance trade-offs
between classical and modern AI techniques in real-world retail applications.
Our findings demonstrate that tree-based models, particularly XGBoost and Random Forest,
consistently outperform UniTS and SVM in most experimental settings. These models offer high
predictive accuracy, robustness to class imbalance, and remarkable data efficiency, achieving
strong performance even with as few as 200–600 churners. In contrast, the UniTS model, while
theoretically well-suited for modeling temporal dynamics, underperforms on small to medium-
sized tabular datasets, likely due to its high data requirements.
From a practical perspective, the results suggest that traditional ensemble methods remain
a reliable and efficient choice for churn prediction in typical retail environments where data is
structured and often limited. Although transformer-based models may hold promise, particularly
in scenarios involving large-scale behavioral data and rich temporal histories, their advantages
are not fully realized under constrained data settings.
Looking ahead, future research could explore how UniTS and similar architectures perform
when additional behavioral and contextual features (e.g., browsing activity, promotions, season-
ality) are included. Additionally, a systematic analysis of training time, energy efficiency, and
deployment constraints would help assess the suitability of different model types for modern
AI-accelerated infrastructures. By advancing our understanding of the conditions under which
advanced architectures can provide tangible benefits, we hope to guide more effective and scalable
applications of AI in customer retention strategies.
Acknowledgments.This work was carried out while Syed Saad Saif was enrolled in the Italian Na-
tional Doctorate on Artificial Intelligence run by Sapienza University of Rome in collaboration with
UnitelmaSapienza University of Rome, with his doctoral fellowship co-funded by Infocube SRL.
Disclosure of Interests.The authors declare that they have no competing interests.

14 S. Saad Saif et al.
References
1. Agbemadon, K.B., Couturier, R., Laiymani, D.: Churn detection using machine learning in the retail
industry. In: 2022 2nd International Conference on Computer, Control and Robotics (ICCCR). pp.
172–178 (March 2022).https://doi.org/10.1109/ICCCR54399.2022.9790213,
2. Baghla, S., Gupta, G.: Performance evaluation of various classification techniques for customer
churn prediction in e-commerce. Microprocessors and Microsystems94, 104680 (2022).https:
//doi.org/https://doi.org/10.1016/j.micpro.2022.104680,https://www.sciencedirect.com/
science/article/pii/S0141933122002101
3. Barsotti, A., Gianini, G., Mio, C., Lin, J., Babbar, H., Singh, A., Taher, F., Damiani, E.: A decade of
churn prediction techniques in the telco domain: A survey. SN Computer Science5(4), 404 (2024).
https://doi.org/10.1007/s42979-024-02722-7
4. Basker, E.: Supersize it: The growth of retail chains and the rise of the big-box store. The Journal
of Economic Perspectives26(2), 177–198 (2012)
5. Benkendorf, D.J., Hawkins, C.P.: Effects of sample size and network depth on a deep learning
approach to species distribution modeling. Ecological Informatics60, 101137 (2020)
6. Boukrouh, I., Azmani, A.: Explainable machine learning models applied to predicting customer
churn for e-commerce. IAES International Journal of Artificial Intelligence (IJ-AI)14(1), 286–
297 (2025).https://doi.org/10.11591/ijai.v14.i1.pp286-297,https://ijai.iaescore.com/
index.php/IJAI/article/view/25293,
7. Breiman, L.: Random forests. Machine learning45(1), 5–32 (2001)
8. Buckinx, W., Van den Poel, D.: Customer retention in the non-contractual retail setting: the role of
purchase behavior. Expert Systems with Applications28(3), 479–486 (2005)
9. Chen, L., Wang, Y.: B2c e-commerce customer churn prediction based on k-means and svm. In:
International Conference on Data Mining (2019)
10. Chen, T., Guestrin, C.: Xgboost: A scalable tree boosting system. In: Proceedings of the 22nd acm
sigkdd international conference on knowledge discovery and data mining. pp. 785–794 (2016)
11. Colli, N.C., Saif, S.S., Maggiore, G., Distante, D.: Artificial intelligence for customer churn prediction
in non-contractual retail environments: A systematic literature review (2025), manuscript under peer
review
12. Coolwijk, S., Ziabari, S.S.M., Angileri, F.: Vision transformer approach to customer churn prediction
radar chart image classification for non-subscription based e-commerce. In: Information Integration
and Web Intelligence: 26th International Conference, IiWAS 2024, Bratislava, Slovak Republic, De-
cember 2–4, 2024, Proceedings, Part II. p. 75–80. Springer-Verlag, Berlin, Heidelberg (2024).https:
//doi.org/10.1007/978-3-031-78093-6_6,https://doi.org/10.1007/978-3-031-78093-6_6
13. Cortes, C., Vapnik, V.: Support-vector networks. Machine learning20(3), 273–297 (1995)
14. Gan, L.: Xgboost-based e-commerce customer loss prediction. Computational Intelligence and Neu-
roscience2022(1), 1858300 (2022).https://doi.org/https://doi.org/10.1155/2022/1858300,
https://onlinelibrary.wiley.com/doi/abs/10.1155/2022/1858300,
15. Gao, S., Koker, T., Queen, O., Hartvigsen, T., Tsiligkaridis, T., Zitnik, M.: Units: A unified multi-
task time series model. In: The Thirty-eighth Annual Conference on Neural Information Processing
Systems (2024),https://openreview.net/forum?id=nBOdYBptWW
16. Geiler, S., Affeldt, S., Nadif, M.: Machine learning techniques for customer churn prediction: A
review. IEEE Access10, 34567–34589 (2022).https://doi.org/10.1109/ACCESS.2022.3141592
17. Gupta,R.,Sharma,N.:Churndetectionusingmachinelearningintheretailindustry.In:Proceedings
of ICMLC (2021)
18. Hagberg, J., Sundstrom, M., Egels-Zandén, N.: The digitalization of retailing: an exploratory frame-
work. International Journal of Retail & Distribution Management44(7), 694–712 (2016)
19. J, S., Gangadhar, C., Arora, R.K., Renjith, P., Bamini, J., Chincholkar, Y.d.: E-commerce customer
churn prevention using machine learning-based business intelligence strategy. Measurement: Sensors
27(2023).https://doi.org/10.1016/j.measen.2023.100728,https://www.sciencedirect.com/
science/article/pii/S2665917423000648
20. Lee, H.J., Cho, S.B.: Machine learning-based customer churn prediction in home appliance rental
business. Expert Systems with Applications150, 113255 (2020)
21. Lee, N.T., Lee, H.C., Hsin, J., Fang, S.H.: Prediction of customer behavior changing via a hybrid
approach. IEEE Open Journal of the Computer Society5, 27–38 (2024).https://doi.org/10.1109/
OJCS.2023.3336904
22. Manzoor, A., Qureshi, M.A., Kidney, E., Longo, L.: A review on machine learning methods for
customer churn prediction and recommendations for business practitioners. IEEE Access12, 70434–
70463 (2024).https://doi.org/10.1109/ACCESS.2024.3402092

Traditional ML Methods vs UniTS for Retail Churn Prediction 15
23. Miguéis, V., Camanho, A., Falcão e Cunha, J.: Customer attrition in retailing: An application of mul-
tivariate adaptive regression splines. Expert Systems with Applications40(16), 6225–6232 (2013).
https://doi.org/https://doi.org/10.1016/j.eswa.2013.05.069,https://www.sciencedirect.
com/science/article/pii/S0957417413003679,
24. Pondel, M., Wuczynski, M., Gryncewicz, W., Łysik, Ł., Hernes, M., Rot, A., Kozina, A.: Deep learn-
ing for customer churn prediction in e-commerce decision support. vol. 1, p. 3 – 12 (2021).https://
doi.org/10.52825/bis.v1i.42,https://www.tib-op.org/ojs/index.php/bis/article/view/42,
; Cited by: 18; All Open Access, Hybrid Gold Open Access
25. Pondel, M., Wuczynski, M., Gryncewicz, W., Łysik, Ł., Hernes, M., Rot, A., Kozina, A.: Deep learn-
ing for customer churn prediction in e-commerce decision support. vol. 1, p. 3 – 12 (2021).https://
doi.org/10.52825/bis.v1i.42,https://www.tib-op.org/ojs/index.php/bis/article/view/42
26. Rachid, A.D., Abdellah, A., Belaid, B., Rachid, L.: Clustering prediction techniques in defining and
predicting customers defection: The case of e-commerce context. International Journal of Electrical
and Computer Engineering (IJECE)8(4), 2367–2383 (2018).https://doi.org/10.11591/ijece.
v8i4.pp2367-2383,https://ijece.iaescore.com/index.php/IJECE/article/view/8531
27. Rahib, M.A.A., Saha, N., Mia, R., Sattar, A.: Customer data prediction and analysis in e-
commerce using machine learning. Bulletin of Electrical Engineering and Informatics13(4),
2624–2633 (2024).https://doi.org/10.11591/eei.v13i4.6420,https://www.beei.org/index.
php/EEI/article/view/6420,
28. Reinartz, W., Kumar, V.: The impact of customer relationship characteristics on profitable lifetime
duration. Journal of Marketing67(1), 77–99 (2003)
29. Rodríguez, M., García, J.: Comparison of deep learning algorithms to predict customer churn within
a local retail industry. Applied Computing and Informatics (2023)
30. Rudd, D.H., Huo, H., Xu, G.: Causal analysis of customer churn using deep learning. In: 2021
International Conference on Digital Society and Intelligent Systems (DSInS). pp. 319–324 (2021).
https://doi.org/10.1109/DSInS54396.2021.9670561
31. Seema, Gupta, G.: Development of fading channel patch based convolutional neural network models
for customer churn prediction. International Journal of System Assurance Engineering and Man-
agement15(1), 391–411 (January 2024).https://doi.org/10.1007/s13198-022-01759-,https:
//ideas.repec.org/a/spr/ijsaem/v15y2024i1d10.1007_s13198-022-01759-2.html,
32. Shahabikargar, M., Beheshti, A., Zhang, X., Foo, J., Jolfaei, A.: A comprehensive survey on customer
churn analysis studies. Journal of Information and Telecommunication0(0), 1–47 (2025).https:
//doi.org/10.1080/24751839.2025.2528440,https://doi.org/10.1080/24751839.2025.2528440
33. Singh, R., Kapoor, M.: Understanding customer attrition at an individual level: a new model in
grocery retail context. Journal of Retailing and Consumer Services58, 102345 (2021)
34. Sunarya, P., Rahardja, U., Chen, S., Lic, Y.M., Hardini, M.: Deciphering digital social dynamics:
A comparative study of logistic regression and random forest in predicting e-commerce customer
behavior. Journal of Applied Data Sciences5(1), 100–113(2024).https://doi.org/10.47738/jads.
v5i1.155,https://bright-journal.org/Journal/index.php/JADS/article/view/155,
35. Wu, H., Hu, T., Liu, Y., Zhou, H., Wang, J., Long, M.: Timesnet: Temporal 2d-variation modeling
for general time series analysis. In: International Conference on Learning Representations (2023)
36. Wu, H., Wu, J., Xu, J., Wang, J., Long, M.: Flowformer: Linearizing transformers with conservation
flows. arXiv preprint arXiv:2202.06258 (2022)
37. Zhang, R., Kim, J.: Customer churn in retail e-commerce business: spatial and machine learning
approach. Journal of Retail Analytics18, 122–135 (2022)
