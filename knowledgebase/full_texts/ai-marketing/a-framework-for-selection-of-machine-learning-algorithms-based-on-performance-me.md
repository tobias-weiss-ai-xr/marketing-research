---
title: A Framework for Selection of Machine Learning Algorithms Based on Performance Metrices and Akaike
  Information Criteria in Healthcare, Telecommunication, and Marketing Sector
url: https://arxiv.org/abs/2510.00321
category: ai-marketing
subcategory: empirical
date: 2025-09
venue: ''
authors:
- "A. K. Hamisu</name>\n      <arxiv:affiliation>Abubakar Hamisu Kamagata</arxiv:affiliation>\n    </author>\n\
  \    <author>\n      <name>K. Jasleen"
source: arxiv
pdf_url: https://arxiv.org/pdf/2510.00321
pages: 17
chars: 41394
fetched_at: '2026-11-08T13:13:39+00:00'
kb_version: 1
---

# A Framework for Selection of Machine Learning Algorithms Based on Performance Metrices and Akaike Information Criteria in Healthcare, Telecommunication, and Marketing Sector

113DOI: 10.1201/9781003226147-6
A Framework for Selection
of Machine Learning
Algorithms Based on
Performance Metrices
and Akaike Information
Criteria in Healthcare,
Telecommunication,
and Marketing Sector
A. K. Hamisu and K. Jasleen
CONTENTS
6.1 Introduction .................................................................................................. 114
6.2 Machine Learning Applications ................................................................... 114
6.3 Design and Implementation of Framework for Model Selection .................. 117
6.3.1 Phase 1: Input Analysis Phase .......................................................... 117
6.3.1.1 Input Attributes .................................................................. 117
6.3.1.2 Attribute Analysis .............................................................. 117
6.3.2 Phase 2: Model Building Phase ........................................................ 118
6.3.2.1 Data collection ................................................................... 118
6.3.2.2 Data Pre-Processing ...........................................................118
6.3.2.3 Features Extraction ............................................................ 118
6.3.2.4 Model Building ..................................................................119
6.3.3 Phase 3: Model Evaluation Phase .....................................................120
6.3.3.1 Model Analysis Module .....................................................120
6.3.4 Phase 4: Model Recommendation Phase ..........................................120
6.4 Result and Analysis ......................................................................................120
6.4.1 Selection of Model based on Accuracy, Precision, Recall,
and F-Measure ..................................................................................121
6.4.2 Selection of Model Based on Akaike Information Criteria ..............124
6.5 Conclusion  ....................................................................................................124
References ..............................................................................................................126
6
BK-TandF-JENA_9781032126876-211334-Chp06.indd   113 13/11/21   4:16 PM

114 Machine Learning and Deep Learning in Medical Data Analytics
6.1 INTRODUCTION
Machine intelligence is the last invention that humanity will ever need to make.
Nick Bostrom
The growth of the internet has seen a profusion of data and a surge in technology for
extracting information from big data for marketing strategy, adding value to prod-
ucts and services, and personalizing the consumer experience. Recently, there has
been a remarkable increase in interest in the era of artificial intelligence (AI), ML,
and deep learning (DL), as more individuals become aware of the breadth of new
applications enabled by ML and DL methodologies. The applications of ML and
DL range from home to hospital, domestic to enterprise, agriculture to military, and
include all aspects of life. The main focus of this chapter is on applications of ML
methodologies in three separate sub-domains: healthcare, marketing, and telecom -
munications. In the healthcare sector, two significant problems are considered for
this research work. One is cardiovascular disease and another one is fetal health. The
reason for choosing both these diseases is the rate at which they affect the people.
Cardiovascular disease, also known as coronary ailment, is one of the most serious
ailments in India and around the world. Heart disease is estimated to be the cause of
28.1% of deaths. It is also the leading cause of death, accounting for more than 17.6
million fatalities in 2016 across the world (Shan et al. 2017). As a result, accurate
and early diagnosis and treatment of such diseases necessitates a system that can
forecast with pinpoint accuracy and consistency. The second problem that is consid-
ered for this work is fetal health classification which includes classification of fetal as
healthy or unhealthy. A total of three datasets (two cardiovascular datasets and one
fetal health dataset) were used under healthcare sector. In this chapter, a framework
for the selection of ML algorithm has been proposed. ML algorithm was selected
based on dataset attributes, performance metrics, and AIC score. For experimenta-
tion purposes, ML algorithms were divided into eager, lazy, and hybrid learners.
For the evaluation of the proposed framework, a total of eight datasets from three
sectors (healthcare, telecommunication, and marketing) were selected for experi -
mentation. This paper contributes in context of framework for recommendation of
the best ML algorithm/model according to the input attributes. Model recommen -
dation was based on performance evaluation parameters (accuracy, precision, and
recall) as well as on model selection parameters (AIC).
The rest of the chapter is organized as follows. Section 6.2 presents related work
carried out in proposed direction. Complete methodology followed for implementa-
tion of this work is presented in Section 6.3. Detailed results and analysis are pre -
sented in section 6.4 followed by concluding remarks in section 6.5.
6.2 MACHINE LEARNING APPLICATIONS
ML has potential applications in various domains and sectors. This section provides
a brief glimpse of applications of ML in healthcare, telecommunication, marketing,
and other sectors.
BK-TandF-JENA_9781032126876-211334-Chp06.indd   114 13/11/21   4:16 PM

115Framework for Selection of ML Algorithms
Goyal et al. (2021) introduced the concept of Internet of Health Things and dis-
cusses about potential challenges, advancement and benefits for IoT based healthcare
and healthcare aided living. Pattnayak and Jena (2021) discussed and explained the
need of ML for healthcare systems. Potential application of ML in healthcare and
healthcare aided areas which includes from patient to doctor, from diagnosis to treat-
ment, from surgery to decision support system were well elaborated. Panigrahi et al.
(2021) developed an expert system-based clinical decision support system (CDSS) for
prediction and diagnosis of hepatitis-B. This system comprises 59 rules and imple -
mentation is done using web-based Expert System Shell. Paramesha et al. (2021)
discussed ML-based approach for sentiment analysis of narrated drug reviews and
engineering in food technology which are indirectly related to the healthcare sec-
tor. Mohapatra et al. (2021) experimented with convolutional neural network (CNN)
for early detection of skin cancer. They have also performed comparative analysis
of MobileNet and ResNet50 CNN architectures for skin cancer classification task.
Ramakrishnudu et al. (2021) proposed a system that predicts the overall health status
of a person using ML techniques. Various parameters such as person’s sleeping pat-
tern, his/her physical activity, and his/her eating habits were used for predicting the
overall health of the person. Panicker et al. (2021) proposed lightweight CNN model
for classifying tuberculosis bacilli from non-bacilli objects. The performance of the
proposed model in terms of accuracy is close to the existing ML models Panicker
et al. 2021). Islam et al. discussed the use of DL techniques for autonomous disease
diagnosis from symptoms. They proposed a graph convolution network (GCN) as
a disease–symptom network to link the disease and symptoms. GCN-based deep
neural network determines the most probable diseases associated with the given
symptoms with 98% accuracy (Islam et al. 2021). Khamparia et al. (2020) proposed
transfer learning based novel DL internet of health and things driven method for
skin cancer classification. The proposed method performed well as compared to ear-
lier reported techniques. Güldo ğan et al. (2021) proposed a transfer learning-based
technique for the detection and classification of breast cancer (benign or malignant)
based on the ultrasound images. Performance metrics such as accuracy, sensitivity, and
specificity with 95% confidence intervals were 0.974 (0.923–1.0), 0.957 (0.781–0.999),
and 1 (0.782–1.0), respectively (Güldoğan et al. 2021). Said et al. (2021) proposed a
new transfer learning-based approach for the classification of breast cancer in histo-
pathological images. Block wise fine tuning strategy has been employed to handle
CNN RESNET-18 (Said et al. 2021). Yang et al. (2021) explored the potential of DL
models in the identification of lung cancer subtypes and cancer mimics from whole
slide images. Irene et al. (2021) elaborated the ethics of ML in healthcare through
the lens of social justice. Recent developments, challenges, and solutions to address
those challenges were discussed in detail. Danton et al. (2020) proposed a system -
atic approach to identify the ethics in ML-based healthcare applications. Elements
such as conceptual model, development, implementation, and evaluation were con -
sidered while framing the approach (Danton et al. 2020). Muhammad et al. (2020)
discussed the challenges, requirements, and opportunities in the area of fairness in
healthcare AI and the various nuances associated with it. Liu et al. (2020) proposed
DL approaches for automatic diagnosis of Alzheimer’s disease (AD) and its prodro-
mal stage, that is, mild cognitive impairment (MCI). Baskaret al. (2020) proposed
BK-TandF-JENA_9781032126876-211334-Chp06.indd   115 13/11/21   4:16 PM

116 Machine Learning and Deep Learning in Medical Data Analytics
a framework for wearable sensors (WS) so that it can be applicable as a part of
smart healthcare tracking applications. Andre et al. (2019) discussed the application
of computer vision, natural language processing in the context of medical domain.
Siddique and Chow (2021) discussed the application of ML/AI in healthcare com -
munication. This work includes chatbots for the COVID-19 health education, cancer
therapy, and medical imaging. The challenges, issues, and problems for the imple -
mentation of ML- and DL-based applications in healthcare and healthcare-aided
sector have been discussed (Riccardo et al. 2018). Mateen et al. (2020) presented a
framework for improving the accuracy of ML algorithms in healthcare by incorpo -
rating reporting guidelines such as SPIRIT-AI and CONSORT-AI in clinical and
health science in ML approaches. Ferdous et al. (2020) presented a review on ML
when applied to prediction of different diseases. The contribution of ML in health-
care is discussed with aim to provide the best suitable ML algorithm (Ferdous et al.
2020). Utsav et al. (2019) presented a technique to use ML algorithms for predict -
ing the probability of cardiac arrest based on various attributes. Zoabi et al. (2021)
proposed an ML-based technique to predict whether an individual is infected with
SARS-CoV-2 or not. The model takes different parameters such as age, gender, and
presence of various COVID symptoms. Faizal and Sultan (2020) explored the appli-
cation of AI and data analytics techniques for mobile health. These techniques can
be used for providing valuable insights to users and accordingly resources can be
planned for mobile health. AI-based models have been proposed for mobile health.
Futoma et al. (2020) emphasized for clinical utility and generalizability of ML algo-
rithms and answers the various questions (when, how, and why) on ML applicabil -
ity for both clinicians and for patients. Wang et al. (2020) proposed an alternative
COVID-19 diagnosis methodology based on COVID-19 radio graphical changes in
computerized tomography (CT) images. They experimented with DL methods to
extract the hidden features from CT scans and provide the diagnosis for COVID-19
(Wang et al. 2020). Song et al. (2020) proposed DeepPneumonia technique (as DL
based COVID detection from CT scans) to identify patients with COVID-19. Punn
et al. (2020) proposed ML- and DL-based model to analyze predictive behavior of
COVID-19 using a dataset published on the Johns Hopkins dashboard.
Authors proposed a technique to predict the customer churn rate (who are likely
to cancel the subscription). Various ML algorithms such as DT, Random Forest,
and XGBoost have been experimented (Kavitha et al. 2020). Researchers presented
analysis to leverage ML methods in marketing research. Comparison between ML
methods with statistical methods was also presented. A unified conceptual frame -
work for ML methods have been proposed in this work (Liye and Baohong 2020).
Dev et al. (2016) used ML to predict heart disease.
In Galván et al.’s (2009) study, a lazy learning strategy was proposed for building
classification learning models. In this work, authors compared the accuracy of SVM
and KNN algorithms on student performance data sets. SVM performed well as com-
pared to KNN with accuracy of 91.07% (Nuranisah et al. 2020). Thanh and Kappas
(2017) examined and compared the performance of ML algorithm for land use/cover
classification. The classification results showed a high overall accuracy of all the algo-
rithms In this paper, authors experimented with ML algorithms on healthcare datasets
(Raj and Sonia 2017). Zhenlong et al. (2017) explored the usefulness of ML algorithms
BK-TandF-JENA_9781032126876-211334-Chp06.indd   116 13/11/21   4:16 PM

117Framework for Selection of ML Algorithms
for driver drowsiness detection. The results revealed that SVM performed well. In this
paper, authors proposed the application of lazy learning techniques to Bayesian tree
induction and presents the resulting lazy Bayesian rule learning algorithm, called Lbr
(Zheng and Webb 2000). Solomon et al. (2014) presented evaluation of eager and lazy
classification algorithms using UCI Bank Marketing data set. Results revealed that
eager learners outperform the lazy learners with accuracy of 98%.
6.3  DESIGN AND IMPLEMENTATION OF
FRAMEWORK FOR MODEL SELECTION
Proposed architecture is explained in Figure 6.1. Proposed system consists of various
phases: data collection, data pre-processing, feature extraction, model building, and
performance evaluation.
6.3.1 Phase 1: InPut analysIs Phase
6.3.1.1 Input Attributes
In this phase, attributes are input into the system. The selection of attributes entirely
depends upon the problem for which the most suitable algorithm is to be identified.
6.3.1.2 Attribute Analysis
In this sub-phase, input attributes are analyzed. Various kinds of analysis such as
size of input attributes, type of input attributes, and nature of input attributes are
FIGURE 6.1 Architecture of proposed system.
BK-TandF-JENA_9781032126876-211334-Chp06.indd   117 13/11/21   4:16 PM

118 Machine Learning and Deep Learning in Medical Data Analytics
performed for better understanding of data. Visualization technique was used to
identify the relationship between input attributes whether it is linear or non-linear,
based on which set of ML algorithms were selected. For input attributes where a lin-
ear relationship exists among the attributes, algorithms like SVM can be selected for
initial evaluation. If the size of input attributes is small, algorithm like Naïve Bayes
can be preferable for initial evaluation. As nature of data concerns, it depends upon
the output target variable type. In our work, target variable is categorical in nature.
6.3.2 Phase 2: Model BuIldIng Phase
In this phase, various selected ML algorithms were trained and tested for datasets
from each of the sectors. The ML algorithm training and testing process is described
in the following sub-phases.
6.3.2.1 Data collection
For this research work, three sectors (healthcare, telecommunication, and market -
ing) were selected. A total of eight datasets were collected in three sectors. Details
of dataset by sector are presented in Table 6.1. The description includes the number
of records, attributes, and class labels in each dataset.
6.3.2.2 Data Pre-Processing
Raw data need to be pre-processed to organize them into the form which is good for
training the ML algorithm (Han and Kamber 2001). In this work, raw data passes
through various pre-processing stages such as label encoding and handling missing
values with mean of that attribute.
6.3.2.3 Features Extraction
To reduce the computational cost and time for building the model, subsets of fea-
tures/attributes were selected. Multifactor dimensionality reduction methods were
used for reducing the dimensionality of the data. Some attributes were not consid-
ered for model building based upon co-linearity matrices (used for finding relation -
ship with indented class label).
TABLE 6.1
Dataset Description
Sector Dataset Description
Marketing (Avocado 2020) 18,249 records; 13 attributes; 2 class labels
(Bank in Marketing 2020) 11,162 records; 17 attributes; 2 class labels
Telecommunication (Telecom 2020) 4000 records; 12 attributes; 2 class labels
(Cell2cell train 2020) 51047 records; 38 attributes; 2 class labels
(Churn in Telecom 2020) 3333 records; 21 attributes; 2 class labels
Healthcare (Cardio-Vascular 2020) 70,000 records; 13 attributes; 2 class labels
(Fetal_Health 2020) 2126 records; 22 attributes; 2 class labels
(Health_heart 2020) 1025 records; 14 attributes; 2 class labels
BK-TandF-JENA_9781032126876-211334-Chp06.indd   118 13/11/21   4:16 PM

119Framework for Selection of ML Algorithms
6.3.2.4 Model Building
In this research work, 13 machine algorithms were experimented. These ML algo -
rithms were divided into the following categories: eager or lazy depending upon the
learning procedure and third category is hybrid (Huang et al. 2014; Dev et al. 2016).
1. Eager learning: This category of ML algorithms includes DT, SVM, and
Neural Network (NN).
A DT is built using recursive partitioning-based approach. A tree-like
structure is generated using input attributes and leaf nodes of those gener -
ated trees represent the class labels. In this research work, C4.5 version of
DT was built using the gain ratio of attribute.
 () ()= ,      (,  )  (Gain Rtio XD InformationG ainX D Entropy PDi i Xi  (6.1)
Where () ,  Gain Ratio XDi  is ratio of attribute Xi with regard to Dataset D
(Han and Kamber 2001).
SVM is statistical ML algorithm which is based on the structural risk
minimization principle (Han and Kamber 2001). Linear SVM tries to find
maximal marginal hyperplane using the following equation:
 

=
+≥
−+ ≤−



()
1i fw ·x b1
1i fw ·x b1f x  (6.2)
Where  andwb  parameters are identified from training data.
NN is supervised ML algorithm which is based on backprogation where
weights in hidden layer and output layer are updated according to error in
estimation. For weights updation, the following equation is utilized.
 λ=+ −+ (  ) 1ww yy xj k j k ii k ij  (6.3)
Where k is iteration, xij is input attribute value, wj k  is weight assigned in
kth iteration, and λ learning rate (Han and Kamber 2001).
2. Lazy learning: This category includes KNN algorithm and LNB algorithm.
KNN algorithm is a distance-based ML algorithm which has application
in classification as well as regression problems. In this research work, dis-
tance is calculated based on Euclidean distance measure. Distance between
test point (x) and existing training point (y) is given by,
 ∑()=−
=
 
1
2
Eucideand istancex y
i
n
ii  (6.4)
For each dataset, hyper-parameter for KNN, that is, k, is tuned using
elbow method.
BK-TandF-JENA_9781032126876-211334-Chp06.indd   119 13/11/21   4:16 PM

120 Machine Learning and Deep Learning in Medical Data Analytics
3. Hybrid Learning: This category of ML algorithms was formed by combin -
ing different ML algorithms. Algorithms in this category are generated by
stacking up the different ML algorithms from the eager and lazy categories.
Count in eager, lazy, and hybrid ML categories is 3, 2, and 8 respectively.
Table 6.2 provides the details about the categories of ML algorithms.
6.3.3 Phase 3: Model evaluatIon Phase
6.3.3.1 Model Analysis Module
In this phase, analysis of each ML model is carried out in terms of performance
evaluation parameters and model selection parameters. Accuracy, precision, recall,
F-measure, receiver operating characteristic (ROC) curve, and ROC area under
curve (AUC) are used as performance metrices for evaluation. For model selection
purposes, the AIC score was calculated for each algorithm (Akaike 1973).
6.3.4 Phase 4: Model RecoMMendatIon Phase
Based on the attributes passed on in phase 1, this phase identifies the most suitable ML
algorithm based on performance metrices and AIC score. Recommendation of ML
algorithm is based on the weighted average of performance parameters and AIC score.
6.4 RESULT AND ANALYSIS
The purpose of this research is to find the best performing ML algorithm in each sec-
tor (telecommunication, health, and marketing). For this purpose, a total 104 experi-
ments were performed where every dataset (8 in total) is experimented with 13 ML
TABLE 6.2
Category-Wise Machine Learning Algorithms
S. No. Category Algorithm
1 Eager Decision Tree (DT)
Support Vector Machine (SVM)
Neural Network (NN)
2 Lazy K-nearest Neighbhour (KNN)
Lazy Naïve Bayes (LNB)
3 Hybrid KNN+LNB
SVM+DT+NN
SVM+KNN
DT+KNN
NN+KNN
SVM+LNB
DT+LNB
NN+LNB
BK-TandF-JENA_9781032126876-211334-Chp06.indd   120 13/11/21   4:16 PM

121Framework for Selection of ML Algorithms
algorithms (as listed in the previous section). Selection of ML algorithm is carried
out on the basis of performance parameters as well as AIC score. Implementation of
this work has been carried out in Python.
6.4.1  s electIon of Model Based on accuRacy,
PRecIsIon, Recall, and f-MeasuRe
Tables 6.3–6.5 show the results of ML algorithms in each sector. For interpretation
purposes, the average of each metric (accuracy, precision, recall, and f-measure) is
obtained.
From Tables 6.3–6.5, it can be observed that the eager learner category of ML
algorithms performed well as compared to lazy and hybrid learner. Overall average
TABLE 6.3
Result Obtained with Marketing Sector
Learning
Methods
Average
Accuracy
Average
Precision
Average
Recall
Average
F-measure
Eager learner 94 0.92 0.99 0.95
Lazy learner 91 0.86 0.74 0.78
Hybrid learner 92 0.88 0.93 0.93
TABLE 6.4
Result Obtained with Healthcare Sector
Learning
Methods
Average
Accuracy
Average
Precision
Average
Recall
Average
F-measure
Eager learner 90 0.88 0.83 0.88
Lazy learner 85 0.86 0.88 0.87
Hybrid learner 76 0.78 0.77 0.79
TABLE 6.5
Result Obtained with Telecommunication Sector
Learning
Methods
Average
Accuracy
Average
Precision
Average
Recall
Average
F-measure
Eager learner 90 0.89 0.99 0.92
Lazy learner 86 0.90 0.84 0.86
Hybrid learner 85 0.78 0.87 0.88
BK-TandF-JENA_9781032126876-211334-Chp06.indd   121 13/11/21   4:16 PM

122 Machine Learning and Deep Learning in Medical Data Analytics
accuracy of eager learners ranges from 90% to 94%. Accuracy- and precision-based
comparative analysis is presented in Tables 6.6 and 6.7.
From Figures 6.2 and 6.3, it can be observed that the eager learner category of
algorithms performed well for the healthcare sector based on accuracy and precision.
For identification of the best ML algorithm in each sector, performance analysis of
ML algorithms in the eager learner category is carried out. From Figures 6.2 and 6.3,
TABLE 6.6
Average Accuracy-Based Comparison of Machine Learning Algorithms
Learning Methods
Marketing
Dataset Average
Accuracy
Telecommunication
Dataset Average
Accuracy
Healthcare
Dataset Average
Accuracy
Eager learner 94 90 90
Lazy learner 91 86 85
Hybrid learner 92 85 76
TABLE 6.7
Average Precision-Based Comparison of Machine Learning Algorithms
Learning Methods
Marketing
Dataset Average
Precision
Telecommunication
Dataset Average
Precision
Healthcare
Dataset Average
Precision
Eager learner 0.92 0.89 0.88
Lazy learner 0.86 0.90 0.86
Hybrid learner 0.88 0.78 0.78
FIGURE 6.2 Comparison of algorithms based on accuracy.
BK-TandF-JENA_9781032126876-211334-Chp06.indd   122 13/11/21   4:16 PM

123Framework for Selection of ML Algorithms
it can be observed that the eager learner category of algorithms performed well for
the healthcare sector based on accuracy and precision. For identification of the best
ML algorithm in each sector, performance analysis of ML algorithms in the eager
learner category is carried out. In the case of the healthcare dataset, SVM is proven to
be the best ML algorithm, whereas in the case of the telecommunication and market-
ing dataset, DT comes out as the top performing one. NN was the worst performing
algorithm in each sector. Furthermore, ROC curve (refer to Figures 6.4–6.6) and ROC-
AUC score was analyzed for top performing algorithms. ROC-AUC score comes out to
be 1.0 for all top performing ones.
FIGURE 6.3 Comparison of algorithms based on precision.
FIGURE 6.4 ROC curve for DT algorithm in the marketing sector.
BK-TandF-JENA_9781032126876-211334-Chp06.indd   123 13/11/21   4:16 PM

124 Machine Learning and Deep Learning in Medical Data Analytics
As performance of all the ML algorithms is on the same scale, further analyses
is carried out using AIC.
6.4.2 s electIon of Model Based on akaIke InfoRMatIon cRIteRIa
In this section, algorithm performance is measured in terms of AIC. The best model
is chosen with the help of probability framework of log-likelihood under maximum
likelihood estimation. The AIC score can be calculated using:
 ()=∗ −22  logAICk L  (6.5)
FIGURE 6.5 ROC curve for SVM algorithm in the healthcare sector.
FIGURE 6.6 ROC curve for DT algorithm in the telecommunication sector.
BK-TandF-JENA_9781032126876-211334-Chp06.indd   124 13/11/21   4:16 PM

125Framework for Selection of ML Algorithms
where k indicates the number of independent variables used to build the model
and L indicates maximum likelihood estimate of model (Akaike 1973). The best
model is one which minimizes the information loss and has the minimum score
for AIC.
From Table 6.8 it can be observed that in the marketing dataset, the lowest AIC
score of 15.41 is reported by the eager learner category of ML algorithms, whereas
for the telecommunication and healthcare datasets, the lowest AIC score is reported
by the lazy learner category of ML algorithms with a score of 19.91 and 21.76,
respectively.
From Figure 6.7 it can be observed that for the marketing sector, the lowest
AIC score is reported by eager learners, whereas in the case of telecommunica-
tion and healthcare sectors, the lazy learner category reported the lowest AIC.
To find the best suitable algorithm for each sector, comparative analysis has been
TABLE 6.8
Results Based on Average AIC Score
Learning Methods
Marketing Dataset
Average AIC
Telecommunication
Dataset Average AIC
Healthcare Dataset
Average AIC
Eager learner 15.41 21.92 24.07
Lazy learner 16.35 19.91 21.76
Hybrid learner 17.38 22.19 24.96
FIGURE 6.7 Comparison of algorithms based on AIC score.
BK-TandF-JENA_9781032126876-211334-Chp06.indd   125 13/11/21   4:16 PM

126 Machine Learning and Deep Learning in Medical Data Analytics
carried out. Comparative analysis of algorithms based on accuracy and AIC
score is presented in Table 6.9.
FIGURE 6.7 Three different ML model categories (lazy, eager, hybrid) for three
different sectors are compared using AIC for model selection.
From Table 6.9 it can be observed that for the marketing dataset, the eager learner
category is the better option as compared to lazy learners. Based on accuracy and
AIC score, the most suitable ML algorithms are DT and SVM. On the basis of accu-
racy, eager learner is the best performing category of ML algorithms. DT and SVM
are the most suitable algorithms for the telecommunication as well as healthcare
sectors. On the basis of AIC score, lazy learner category of ML algorithms is the
best option for the telecommunication and healthcare sectors. Out of all lazy learn -
ers, KNN performed well on telecommunication as well as on the healthcare sector.
6.5 CONCLUSION
In this research work, a framework for recommendation of ML algorithm has been
formulated. The purpose was to find the most suitable ML algorithm for three differ-
ent sectors. For experimentation purpose, ML algorithm were divided into three cat-
egories: eager, lazy, and hybrid learner. KNN, LNB, SVM, DT, NN, and the hybrid
classifier using stacking were used on eight different datasets (from three different
sectors: marketing, healthcare, and telecommunication). On the basis of accuracy,
results revealed that eager learner ML algorithms are the best performing ones in
all three sectors. Among eager learners, SVM is proven to be the top performing in
healthcare with precision of 0.98. DT is the best suited for the telecommunication
and marketing datasets with precision of 0.99 and 0.94, respectively. Whereas, on the
basis of AIC score, SVM is the best suited for the marketing dataset, whereas KNN
is the best suited for telecommunication and healthcare dataset.
REFERENCES
Akaike, H 1973. Information theory and an extension of the maximum likelihood principle.
In: Petrov, B. N. and Csáki, F. (eds.), 2nd International Symposium on Information
Theory, Tsahkadsor, Armenia, USSR, September 2–8, 1971 . Budapest: Akadémiai
Kiadó, pp. 267–81.
Andre, E., Alexandre, R., Bharath, R., Volodymyr, K., Mark, D., Katherine, C., Claire, C.,
Greg, C., Sebastian, T., Jeff, D. 2019. A guide to deep learning in healthcare. Nature
Medicine, 25: 24–29. https://doi.org/10.1038/s41591-018-0316-z
TABLE 6.9
Accuracy- v/s AIC Score-Based Comparative Analysis of Algorithms
Accuracy-Based Analysis AIC-Based Analysis
Category Algorithm Category Algorithm
Marketing Eager DT Eager SVM
Telecommunication Eager DT Lazy KNN
Healthcare Eager SVM Lazy KNN
BK-TandF-JENA_9781032126876-211334-Chp06.indd   126 13/11/21   4:16 PM

127Framework for Selection of ML Algorithms
Avocado dataset accessed from https://www.kaggle.com/neuromusic/avocado-prices in
Dec 2020.
Bank in Marketing dataset accessed from https://www.kaggle.com in Dec 2020.
Baskar, S., Mohamed, S. P., Kumar, R., Burhanuddin, M. A., Sampath, R. 2020. A dynamic
and interoperable communication framework for controlling the operations of wear -
able sensors in smart healthcare applications. Computer Communications ,149: 17–26.
https://doi.org/10.1016/j.comcom.2019.10.004
Cardio_Vascular dataset accessed from https://www.kaggle.com in Dec 2020.
Cell2celltrain dataset accessed from https://www.kaggle.com in Dec 2020.
Churn in Telecom dataset accessed from https://www.kaggle.com in Dec 2020.
Danton, S. C., Michael, D. A., Chris, F. 2020. Identifying ethical considerations for machine
learning healthcare applications. The American Journal of Bioethics , 20(11): 7–17.
https://doi.org/10.1080/15265161.2020.1819469
Dev, S. K., Krishnapriya, S., Kalita, D. 2016. Prediction of heart disease using data mining
techniques. Indian Journal of Science and Technology , 9(39): 1–5.
Faizal, K. Z., Sultan, R. A. 2020. Applications of artificial intelligence and big data analyt -
ics in m-health: A healthcare system perspective. Journal of Healthcare Engineering ,
2020: 1–15. https://doi.org/10.1155/2020/8894694
Ferdous, M., Debnath, J., Chakraborty, N. R. 2020. Machine Learning Algorithms in Healthcare:
A Literature Survey. 11th International Conference on Computing, Communication
and Networking Technologies (ICCCNT), Kharagpur, India, 2020, pp. 1–6, https://doi.
org/10.1109/ICCCNT49239.2020.9225642
Fetal_Health dataset accessed from https://www.kaggle.com in Dec 2020.
Futoma, J., Simons, M., Panch, T., Doshi-Velez, F., Celi, L. A. 2020. The myth of generalis -
ability in clinical research and machine learning in health care. The Lancet. Digital
health, 2(9): e489–e492. https://doi.org/10.1016/S2589-7500(20)30186-2
Galván, I. M., Valls, J. M., Lecomte, N., Isasi, P. 2009. A Lazy Approach for Machine
Learning Algorithms. Artificial Intelligence Applications and Innovations III. AIAI
2009. IFIP International Federation for Information Processing , vol 296. Boston,
MA: Springer. https://doi.org/10.1007/978-1-4419-0221-4_60
Goyal, S., Sharma, N., Bhushan, B., Shankar, A., Sagayam, M. 2021. IoT Enabled Technology
in Secured Healthcare: Applications, Challenges and Future Directions . In Hassanien
A.E., Khamparia A., Gupta D., Shankar K., Slowik A. (eds) Cognitive Internet of
Medical Things for Smart Healthcare. Studies in Systems, Decision and Control , 311:
25–48. https://doi.org/10.1007/978-3-030-55833-8_2
Güldoğan, E., Ucuzal, H., Küçükakçalı, Z., Çolak, C. 2021. Transfer learning-based classifi -
cation of breast cancer using ultrasound images. Middle Black Sea Journal of Health
Science, 7(1): 74–80. https://doi.org/10.19127/mbsjohs.876667
Han, J., Kamber, M. 2001. Data Mining: Concepts and Techniques. San Diego, USA: Morgan
Kaufmann.
Health_heart dataset accessed from https://www.kaggle.com in Dec 2020.
Huang, G., Song, S., Gupta, J. N. D., Wu, C. 2014. Semi-supervised and unsupervised extreme
learning machines. IEEE Transactions on Cybernetics , 44(1): 2405–17. https://doi.
org/10.1109/TCYB.2014.2307349
Irene, Y. C., Emma, P., Sherri, R., Shalmali, J., Kadija, F., Marzyeh, G. 2021. Ethical machine
learning in healthcare. Annual Review of Biomedical Data Science , 4(1): 1–24. https://
doi.org/10.1146/annurev-biodatasci-092820-114757
Islam, S. R., Sinha, R., Maity, S. P., Ray, A. K. 2021. Deep Learning on Symptoms in Disease
Prediction. In: Mohanty, S. N., Nalinipriya, G., Jena, O. P. and Sarkar, A. (eds), Machine
Learning for Healthcare Applications, Wiley Online Library, pp. 77–87. https://doi.
org/10.1002/9781119792611.ch5
BK-TandF-JENA_9781032126876-211334-Chp06.indd   127 13/11/21   4:16 PM

128 Machine Learning and Deep Learning in Medical Data Analytics
Kavitha, V., Hemanth, K. G., Mohan, K. S. V., Harish, M. 2020. Churn prediction of customer in
telecom industry using machine learning algorithms. International Journal of Engineering
Research & Technology, 09(05). http://dx.doi.org/10.17577/IJERTV9IS050022
Khamparia, A., Singh, P. K., Rani, P., Samanta, D., Khanna, A., Bhushan, B. 2020. An inter-
net of health things-driven deep learning framework for detection and classification
of skin cancer using transfer learning. Transactions on Emerging Telecommunication
Technologies: 32, e3963. https://doi.org/10.1002/ett.3963
Liu, M., Lian, C., Shen, D. 2020. Anatomical-Landmark-Based Deep Learning for Alzheimer’s
Disease Diagnosis with Structural Magnetic Resonance Imaging. In: Chen, Y. W. and
Jain, L. (eds), Deep Learning in Healthcare. Intelligent Systems. Reference Library, vol
171. Cham: Springer. https://doi.org/10.1007/978-3-030-32606-7_8
Liye, M., Baohong, S. 2020. Machine learning and AI in marketing – Connecting comput -
ing power to human insight. International Journal of Research in Marketing , 37(3):
481–504. https://doi.org/10.1016/j.ijresmar.2020.04.005
Mateen, B. A., Liley, J., Denniston, A. K. 2020. Improving the quality of machine learning
in health applications and clinical research. Nature Machine Intelligence , 2: 554–6.
https://doi.org/10.1038/s42256-020-00239-1
Mohapatra, S., Abhishek, N., Bardhan, D., Ghosh, A. A., Mohanty, S. 2021. Comparison of
MobileNet and ResNet CNN Architectures in the CNN-Based Skin Cancer Classifier
Model. In: Mohanty, S. N., Nalinipriya, G., Jena, O. P. and Sarkar, A. (eds), Machine
Learning for Healthcare Applications , Wiley Online Library, 169–86. https://doi.
org/10.1002/9781119792611.ch11
Muhammad, A. A., Arpit, P., Carly, E., Vikas, K., Ankur, T. 2020. Fairness in Machine Learning
for Healthcare. In Proceedings of the 26th ACM SIGKDD International Conference
on Knowledge Discovery & Data Mining (KDD ‘20) . New York, NY: Association for
Computing Machinery, 3529–3530. https://doi.org/10.1145/3394486.3406461
Nuranisah, Syahril E., Poltak, S. 2020. Analysis of algorithm support vector machine learn -
ing and k-nearest neighbor in data accuracy. IOP Conf. Series: Materials Science and
Engineering, 725: 1–7.
Panicker, R. O., Pawan, S., Rajan, J., Sabu, M. 2021. A Lightweight Convolutional Neural
Network Model for Tuberculosis Bacilli Detection From Microscopic Sputum Smear
Images. In: Mohanty, S. N., Nalinipriya, G., Jena, O. P. and Sarkar, A. (eds), Machine
Learning for Healthcare Applications , Wiley Online Library,343–51. https://doi.
org/10.1002/9781119792611.ch22
Panigrahi, N., Ayus, I., Jena, O. P. 2021. An Expert System-Based Clinical Decision Support
System for Hepatitis-B Prediction & Diagnosis. In: Mohanty, S. N., Nalinipriya, G.,
Jena, O. P. and Sarkar, A. (eds), Machine Learning for Healthcare Applications, Wiley
Online Library,57–75. https://doi.org/10.1002/9781119792611.ch4
Paramesha, K., Gururaj, H., Jena, O. P. 2021. Applications of Machine Learning in Biomedical
Text Processing and Food Industry. In: Mohanty, S. N., Nalinipriya, G., Jena, O. P.
and Sarkar, A. (eds), Machine Learning for Healthcare Applications :, Wiley Online
Library, 151–67. https://doi.org/10.1002/9781119792611.ch10
Pattnayak, P., Jena, O. P. 2021. Innovation on Machine Learning in Healthcare Services–
An Introduction. In: Mohanty, S. N., Nalinipriya, G., Jena, O. P. and Sarkar, A. (eds),
Machine Learning for Healthcare Applications , Wiley Online Library,1–15. https://
doi.org/10.1002/9781119792611.ch1
Punn, N. S., Sonbhadra, S. K., Agarwal, S. 2020. COVID-19 epidemic analysis using
machine learning and deep learning algorithms. medRxiv . https://doi.org/10.1101/
2020.04.08.20057679
Raj, K., Sonia. 2017. SVM & KNN based classification of healthcare data sets using weka.
IJCSC, 8(1): 50–54. https://doi.org/10.031206/IJCSC.2016.012
BK-TandF-JENA_9781032126876-211334-Chp06.indd   128 13/11/21   4:16 PM

129Framework for Selection of ML Algorithms
Ramakrishnudu, T., Prasen, T. S., Chakravarthy, V. T. 2021. A Framework for Health Status
Estimation Based on Daily Life Activities Data Using Machine Learning Techniques.
In: Mohanty, S. N., Nalinipriya, G., Jena, O. P. and Sarkar, A. (eds), Machine
Learning for Healthcare Applications , Wiley Online Library, 17–32. https://doi.
org/10.1002/9781119792611.ch2
Riccardo, M., Fei, W., Shuang, W., Xiaoqian, J., Joel, T. D. 2018. Deep learning for health -
care: review, opportunities and challenges. Briefings in Bioinformatics, 19(6): 1236–46,
https://doi.org/10.1093/bib/bbx044
Said, B., Xiabi, L., Zhongshu, Z., Xiaohong, M., Chokri, F. 2021. A new transfer learning
based approach to magnification dependent and independent classification of breast
cancer in histopathological images. Biomedical Signal Processing and Control , 63.
https://doi.org/10.1016/j.bspc.2020.102192
Shan, X., Tiangang, Z., Zhen, Z., Daoxian, W., Junfeng, H., Xiaohui, D. 2017. Cardiovascular
Risk Prediction Method Based on CFS Subset Evaluation and Random Forest
Classification Framework. 2017 IEEE 2nd International Conference on Big Data
Analysis (ICBDA), 228–32. https://doi.org/10.1109/ICBDA.2017.8078813
Siddique, S, Chow, J. C. L. 2021. Machine learning in healthcare communication.
Encyclopedia , 1(1): 220–39. https://doi.org/10.3390/encyclopedia1010021
Solomon, G. F., Abebe, D. A., Bhabani, S. D. M. 2014. A comparative study on performance
evaluation of eager versus lazy learning methods. International Journal of Computer
Science and Mobile Computing , 3(3): 562–8.
Song, Y., Shuangjia, Z., Liang, L., et al. 2020. Deep learning Enables Accurate
Diagnosis of Novel Coronavirus (COVID-19) with CT images. IEEE/ACM
Transactions on Computational Biology and Bioinformatics https://doi.org/10.1101/
2020.02.23.20026930
Telecom dataset accessed from https://www.kaggle.com/blastchar/telco-customer-churn in
Dec 2020.
Thanh, N. P., Kappas, M. 2017. Comparison of Random Forest, k-Nearest Neighbor, and
support vector machine classifiers for land cover classification using Sentinel-2
imagery. Sensors (Basel) . 18(1). doi: 10.3390/s18010018. PMID: 29271909; PMCID:
PMC5796274.
Utsav, C., Vikas, K., Vipul, C., Sumit, T., Amit, K. 2019. Cardiac arrest prediction using
machine learning algorithms. 2019 2nd International Conference on Intelligent
Computing Instrumentation and Control Technologies (ICICICT) , 1, 886–90. https://
doi.org/10.1109/ICICICT46008.2019.8993296
Wang, S., Kang, B., Ma, J., Zeng, X., Xiao, M., Guo, J., Cai, M., Yang, J., Li, Y., Meng, X., Xu,
B. 2020. A deep learning algorithm using CT images to screen for Corona Virus Disease
(COVID-19). European Radiology. https://doi.org/10.1007/s00330-021-07715-1
Yang, H., Chen, L., Cheng, Z., Yang, M., Wang, J., Lin, C., Wang, Y., Huang, L., Chen, Y.,
Peng, S., Ke, Z., Li.,W. 2021. Deep learning-based six-type classifier for lung cancer
and mimics from histopathological whole slide images: a retrospective study. BMC
Medicine. 19(80). https://doi.org/10.1186/s12916-021-01953-2
Zheng, Z., Webb, G. I. 2000. Lazy learning of Bayesian rules. Machine Learning , 41: 53–84.
https://doi.org/10.1023/A:1007613203719
Zhenlong, L., Qingzhou, Z., Xiaohua, Z. 2017. Performance analysis of K-Nearest neighbor,
support vector machine, and artificial neural network classifiers for driver drowsiness
detection with different road geometries. International Journal of Distributed Sensor
Systems, 13(9): 1–12. https://doi.org/10.1177/1550147717733391
Zoabi, Y., Deri-Rozov, S., Shomron, N. 2021. Machine learning-based prediction of
COVID-19 diagnosis based on symptoms. npj Digital Medicine , 4(3): 1–5. https://doi.
org/10.1038/s41746-020-00372-6
BK-TandF-JENA_9781032126876-211334-Chp06.indd   129 13/11/21   4:16 PM
