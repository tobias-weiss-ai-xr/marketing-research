---
title: Bayesian Regression for Predicting Subscription to Bank Term Deposits in Direct Marketing Campaigns
url: https://arxiv.org/abs/2410.21539
category: ai-marketing
subcategory: empirical
date: 2024-10
venue: ''
authors:
- Muhammad Farhan Tanvir
- Md Maruf Hossain
- Md Asifuzzaman Jishan
source: arxiv
pdf_url: https://arxiv.org/pdf/2410.21539
pages: 6
chars: 26961
fetched_at: '2026-11-08T13:12:07+00:00'
kb_version: 1
---

# Bayesian Regression for Predicting Subscription to Bank Term Deposits in Direct Marketing Campaigns

arXiv:2410.21539v1  [cs.LG]  28 Oct 2024
Bayesian Regression for Predicting Subscription to
Bank Term Deposits in Direct Marketing Campaigns
Muhammad Farhan Tanvir ∗, Md Maruf Hossain †, Md Asifuzzaman Jishan ∗
∗Institute of Computer Science and Computational Science, U niversität Potsdam, Germany
†Faculty of Statistics, Technische Universität Dortmund, G ermany
Email: farhan.tanvir@uni-potsdam.de ∗, mdmaruf.hossain@tu-dortmund.de †, md.jishan@uni-potsdam.de ∗
Abstract—In the highly competitive environment of the bank-
ing industry, it is essential to precisely forecast the beha vior of
customers in order to maximize the effectiveness of marketi ng
initiatives and improve ﬁnancial consequences. The purpos e of
this research is to examine the efﬁcacy of logit and probit mo dels
in predicting term deposit subscriptions using a Portugues e
bank's direct marketing data. There are several demographi c,
economic, and behavioral characteristics in the dataset th at affect
the probability of subscribing. To increase model performa nce
and provide an unbiased evaluation, the target variable was
balanced, considering the inherent imbalance in the datase t. The
two model's prediction abilities were evaluated using Baye sian
techniques and Leave-One-Out Cross-Validation (LOO-CV). The
logit model performed better than the probit model in handli ng
this classiﬁcation problem. The results highlight the rele vance of
model selection when dealing with complicated decision-ma king
processes in the ﬁnancial services industry and imbalanced
datasets. Findings from this study shed light on how banks ca n
optimize their decision-making processes, improve their c lient
segmentation, and boost their marketing campaigns by utili zing
machine learning models.
Index Terms—Applied Bayesian Binary Model, Term Deposits
Subscription, Bayesian Logit Regression, Bayesian Probit Regres-
sion, Predictive Modeling.
I. I NTRODUCTION
The banking sector, particularly in the ﬁeld of marketing
and customer engagement, faces the ongoing challenge of
predicting customer behavior, such as term deposit subscri p-
tions. In addition, accurate forecasting of such behavior i s
very crucial for improving marketing efﬁciency, enhancing
customer segmentation, and optimizing decision-making. T his
research investigates whether Bayesian Data Analysis can
enhance the predictive precision of term deposit subscript ions
in direct marketing campaigns.
Previous studies have shown various machine learning and
statistical techniques implemented to predict customer be hav-
ior in the banking industry [1]. While these approaches have
shown promise, they cannot often account for data imbalance s
and cannot incorporate prior knowledge into the modeling
process [2]. For instance, traditional logistic regressio n treats
data as stationary and has limited efﬁcacy in reﬂecting the u n-
certainty inherent in ﬁnancial data even if it offers reason able
predictive ability [3]. On the other hand, machine learning
models may have problems with being hard to understand and
not being able to incorporate expert knowledge or adapt to
real-time data dynamically [4]. Bayesian methods are very
good for ﬁnancial applications [5] because they are ﬂexible
and can use previous information to make constantly updated
predictions based on new data. Even though they have beneﬁts ,
Bayesian methods for predicting customer term deposit sub-
scriptions have not been studied much [6]. The study aims to
ﬁll that gap by using Bayesian models to make more accurate
and easy-to-understand predictions.
The comparison of two Bayesian models, Bayesian Logis-
tic Regression and Bayesian Probit Regression, which were
applied to a real-world direct marketing dataset from a Por-
tuguese bank, is the primary contribution that this researc h
study makes. With a total of 41,188 observations and 21
variables, the dataset was used to select a balanced subset o f
10,000 records for the purpose of developing a model. Both
models were able to achieve convergence successfully, and
their predictive accuracy was thoroughly evaluated by em-
ploying techniques such as Leave-One-Out Cross-V alidatio n
(LOO-CV) and Out-of-Sample Prediction.
The structure of this research paper is as follows: Section 2
presents the literature review, Section 3 covers the datase t and
data quality, Section 4 describes the methodology, and Sect ion
5 presents the results and discussion. The conclusion outli nes
the main conclusions and makes recommendations for further
study.
II. L ITERATURE REVIEW
Several studies have explored predictive techniques to en-
hance customer behavior forecasting in bank marketing cam-
paigns. One study [7] analyzed customer patterns to improve
a Portuguese bank’s direct marketing strategy using logist ic
regression and decision tree models, ﬁnding logistic regre ssion
to be more accurate. Another study [8] applied oversam-
pling techniques like SMOTE, ADASYN, ROS, and others
to predict term deposit subscriptions, with the Naive Bayes
classiﬁer performing best, while AHC outperformed other
methods. Similarly, [9] identiﬁed "duration" as the key fac tor
inﬂuencing term deposit decisions, with Logistic Regressi on
and Bayesian Logistic Regression achieving 89% and 90%
accuracy, respectively. In [10], XGBoost delivered the hig hest
accuracy (91.73%), followed by logistic regression (88.79 %)
and decision trees (91.2%).
In this study [11], clustering methods like K-Means, K-
Medoids, and DBSCAN were combined with classiﬁcation
algorithms such as Decision Tree, Naïve Bayes, and Random

Forest. Random Forest achieved the highest predictive accu -
racy, while K-Medoids outperformed K-Means and DBSCAN
in clustering performance by 3.47% and 0.3%, respectively.
Another study [12] introduced an ensemble classiﬁcation
approach with Random Forest, achieving 94.02% accuracy,
and a voting classiﬁer that improved prediction by 1.6%,
handling class imbalance to reach 95.6% overall accuracy. I n
[13], a predictive framework using Support V ector Machines
(SVM) for a Portuguese retail bank achieved 76.48% accuracy
after hyperparameter tuning, with a speciﬁcity of 82.5% and
sensitivity of 72.4%. Another study [14] compared Multi-
layer Perceptron Neural Networks (MLPNN), TAN, Logistic
Regression, and C5.0 decision trees, ﬁnding C5.0 slightly
outperformed the others, with "Duration" and "Age" identiﬁ ed
as key features.
In study [15], techniques like SVM, Random Forest, XG-
Boost, Light GBM, and Gaussian Naïve Bayes were compared
for predicting client behavior, with Light GBM delivering
superior accuracy and faster processing. Similarly, anoth er
study [16] analyzed models such as SVM, Gaussian Naïve
Bayes, Decision Tree, Bagging, XGBoost, and Light GBM on
Portuguese bank data, ﬁnding that Bagging algorithms had
the highest accuracy. In contrast, [17] introduced a hybrid
deep learning model for banking, combining Self Adaptive-
Sea Lion Optimization (SA-SLnO) and Deep Belief Networks
(DBN) with Recurrent Neural Networks (RNN). The SA-
SLnO-RB model outperformed traditional methods, improvin g
accuracy by 0.81%. Lastly, [18] evaluated statistical, res am-
pling, and distance-based methods for unbalanced term depo sit
datasets, showing that cluster-based resampling signiﬁca ntly
improved positive predictions from 37% to 80%, with the
cluster-based undersampling K-Nearest Neighbor algorith m
proving most effective.
III. D ATASET
The dataset contains detailed direct marketing campaign
data carried out by a Portuguese banking institution, consi sting
of 41,188 samples and 21 variables [19]. The dataset is com-
plete without any missing values, ensuring a comprehensive
and reliable source for analysis. It includes a combination
of categorical and integer input variables representing va rious
elements of marketing campaigns and client demographics.
The factors consist of characteristics such as age, occupa-
tion, marital status, educational attainment, housing sit uation,
and contact information, among others. The target variable
represents customer subscription behavior to a term deposi t,
indicating whether a client subscribed yes or not . A signif-
icant imbalance exists in the dataset, with a majority of 'no '
responses. To address this issue, a balanced subsample was
created using oversampling techniques, where the minority
class 'yes' was oversampled to match the majority class. By
increasing minority representation, oversampling correc ts class
inequality. Replicating or synthesizing minority class sa mples
until equitable representation is achieved. Oversampling min-
imizes model bias toward the majority class, improving its
ability to anticipate both classes. From the original 41,18 8
samples, 10,000 samples were randomly chosen, and the
subsample was further balanced using oversampling approac h
which included 5,000 positive responses and 5,000 negative
responses. Bayesian models are computationally intensive ,
especially for large datasets. Hence, a subsample of the mai n
data was chosen for modeling. Complex models and lots
of data make Bayesian inference computationally costly. It
compensates with computational resources by picking a repr e-
sentative subsample, allowing rapid model evaluation with out
compromising analysis integrity. This balancing techniqu e en-
ables a more robust evaluation of model performance, ensuri ng
that class imbalance does not skew the analysis or lead to
biased predictions.
IV. M ETHODOLOGY
In this section, the study brieﬂy looks at the setup of the
model and the criteria selected for the model.
A. Logit model
Logistic regression, also known as the logit model, is
used to explain the probability of a binary outcome with a
dichotomous dependent variable (0 or 1). It transforms the
linear combination of predictor variables into a probabili ty
using the logistic (sigmoid) function. The formula of the
logistic function can be deﬁned as follows [20]:
π = h(η) = exp(η) 1 + exp(η)
or (equivalently) the logit link function
g(π) = log
( π
1 − π
)
= η = β0 + β1x1 + . . . + βkxk
where π is the probability of success, β0 is the intercept
term and β1, β2, ..., βk are the coefﬁcients associated with the
predictor variables x1, x2, ..., xk respectively.
B. Probit model
Probit regression is an alternative technique for estimati ng
the probability of a binary outcome. It uses the probit funct ion,
a cumulative distribution function (CDF) of the standard no r-
mal distribution, to link predictor variables with the prob ability
of a binary outcome. The formulation of the probit model is
as mentioned below [20]:
π = Φ(η) = Φ( x′β)
According to the conventional normal distribution, the CDF
is denoted by Φ. One can determine the chance that a standard
normal random variable is either less than or equal to a
given value by calculating the CDF of the standard normal
distribution Φ.

C. Priors and Posterior Inference
The Bayesian method uses priors based on previous research
or expertise, which inﬂuence posterior distributions afte r data
is observed. In Bayesian logit and probit models, weakly inf or-
mative normal priors centered around zero were implemented
to allow ﬂexibility in predictor variable effects. Using Ma rkov
Chain Monte Carlo (MCMC), posterior distributions were
estimated, which provide probabilistic support for parame ter
values and predictions, unlike point estimates in frequent ist
methods [21].
D. Priors Assumptions
1) Prior Selection for Logit Model: The logit model im-
plemented more informative priors to reﬂect problem-speci ﬁc
knowledge. The intercept had a normal prior with a mean
of 3.5 and a standard deviation of 1, indicating a strong
belief about the event's baseline probability with moderat e
ﬂuctuation. The regression coefﬁcients had a normal prior w ith
a mean of 0 and a standard deviation of 0.5, suggesting modest
but meaningful predictor effects, making the model conserv a-
tive for scenarios where predictors have limited inﬂuence [ 22].
2) Prior Selection for Probit Model: The intercept had a
normal prior with a mean of 0 and a standard deviation of
5, allowing for signiﬁcant ﬂuctuations in the baseline even t
probability. The regression coefﬁcients had normal priors with
a mean of 0 and a standard deviation of 2, suggesting a
potentially greater but uncertain inﬂuence on the outcome.
This approach is suitable when predictor effects are less kn own
or expected to deviate more from zero [22].
V. R ESULT AND DISCUSSION
This section represents the research's outcomes. This stud y
selected 10,000 observations from the entire dataset for th e
ﬁnal model implementation.
A. Bayesian Logit Regression Model Implementation
The results of implementing the Bayesian logit regression
model, taking into account twenty-one features, are presen ted
for consideration.
1) Summary of the model: Table 1 shows the estimated
coefﬁcients and diagnostic measures for the Bayesian Logit
Regression model, highlighting predictor-outcome relati on-
ships. Positive effects are observed for the "intercept" (2 .34),
"marital" (0.19), and "education" (0.08), while negative e ffects
are seen for "default" (-0.44) and "contact" (-0.45). Credi ble
intervals reﬂect the uncertainty of these estimates, with n ar-
rower intervals indicating greater precision.
The Rhat values of 1.00 for all variables indicate that
the Bayesian model has effectively converged. This shows
that the MCMC algorithm has mixed well and the posterior
distributions have stabilized. Additionally, high ESS Bul k and
ESS Tail values, such as for "education" and "campaign,"
conﬁrm adequate sampling and reliable posterior estimates ,
ensuring credible and well-converged results for the model .
B. Bayesian Probit Regression Model Implementation
The results of implementing the Bayesian probit regression
model, taking into account twenty-one features, are presen ted
for consideration.
1) Summary of the model: Table 2 presents the estimated
coefﬁcients and diagnostics for the Bayesian Probit Regres sion
model, showing the effects of predictor variables on the
outcome. The "intercept" has a strong negative estimate (-
3.62) with a narrow credible interval (-3.79 to -3.46). Smal l
negative effects are seen for "default" (-0.04), "housing" (-
0.00), and "contact" (-0.05), while "education" (0.01) and
"marital" (0.01) show small positive impacts. The estimate s,
along with standard errors and credible intervals, provide
insights into the direction, magnitude, and uncertainty of these
effects. The Rhat values of 1.00 for all variables conﬁrm
successful convergence, indicating that the MCMC simulati ons
have mixed well and the posterior distributions are stable,
ensuring reliable parameter estimates.
The table reports high ESS Bulk values, such as for "age"
(3528), "job" (4797), and "education" (5327), indicating p re-
cise central tendency estimates from the posterior distrib ution.
ESS Tail values, robust for variables like "housing" (2799) and
"euribor3m" (2832), conﬁrm well-sampled extreme values.
These large ESS values indicate minimal autocorrelation in
the MCMC chains, ensuring the reliability of the posterior
estimates.
The diagnostic metrics in Table 2 conﬁrm the robustness and
stability of the Bayesian Probit Regression model. Credibl e
intervals reﬂect the uncertainty of each estimate. In contr ast,
the coefﬁcient estimates, Rhat, and ESS values together hig h-
light the reliability of the Bayesian estimation process an d the
effects of the predictor variables.
C. Model Comparison
Table 3 summarizes the results of a Leave-One-Out Cross-
V alidation (LOO-CV) comparison between the Bayesian Logit
Regression model logit_model and the Bayesian Pro-
bit Regression model probit_model. The table presents
the Expected Log Pointwise Predictive Density Difference
elpd_diff and its associated standard error of the difference
se_diff, allowing for an evaluation of these models pre-
dictive performance. In this comparison, the logit_model
serves as the reference model with an elpd_diff of
0.0 and no associated uncertainty ( se_diff = 0.0). The
probit_model, however, exhibits a signiﬁcantly negative
elpd_diff value of -1860.9, indicating that its predictive
performance is substantially worse than the logit_model.
The se_diff for the probit_model is 49.7, indicating a
degree of uncertainty in this performance difference. Desp ite
this uncertainty, the large negative elpd_diff suggests
that the logit_model outperforms the probit_model in
terms of predictive accuracy based on LOO-CV results.
The comparison highlights that the logit_model is
better suited for predicting the outcome in this context, as
evidenced by its higher expected log pointwise predictive
density. Although the probit_model shows some degree

TABLE I
ESTIMATED COEFFICIENTS AND DIAGNOSTICS FOR THE BAYESIAN LOGIT REGRESSION MODEL
Variable Estimate Est.Error 95% CI Lower 95% CI Upper Rhat ES S Bulk ESS Tail
Intercept 2.34 0.81 0.77 3.94 1.00 567 576
age 0.02 0.00 0.01 0.03 1.00 1299 938
job 0.01 0.01 -0.01 0.03 1.01 2273 584
marital 0.19 0.08 0.03 0.35 1.01 1164 620
education 0.08 0.02 0.04 0.12 1.01 1708 818
default -0.44 0.13 -0.68 -0.19 1.00 1510 756
housing 0.05 0.04 -0.03 0.14 1.00 1346 798
loan -0.02 0.06 -0.14 0.09 1.01 1891 838
contact -0.45 0.14 -0.71 -0.16 1.01 424 613
month -0.12 0.02 -0.16 -0.08 1.00 1344 637
day_of_week 0.04 0.03 -0.02 0.11 1.00 1381 815
duration 0.01 0.00 0.01 0.01 1.01 1159 893
campaign -0.05 0.03 -0.10 -0.00 1.00 1407 644
pdays -0.08 0.02 -0.12 -0.04 1.00 526 499
previous -0.25 0.13 -0.48 0.00 1.00 577 662
poutcome 0.25 0.18 -0.08 0.61 1.00 590 535
emp.var.rate -0.14 0.07 -0.28 -0.00 1.01 355 469
cons.price.idx -0.01 0.02 -0.06 0.04 1.01 334 424
cons.conf.idx 0.01 0.01 -0.01 0.03 1.01 517 691
euribor3m -0.00 0.00 -0.00 0.00 1.00 2366 823
nr.employed -0.33 0.06 -0.45 -0.21 1.00 472 631
TABLE II
ESTIMATED COEFFICIENTS AND DIAGNOSTICS FOR THE BAYESIAN PROBIT REGRESSION MODEL
Variable Estimate Est.Error 95% CI Lower 95% CI Upper Rhat ES S Bulk ESS Tail
Intercept -3.62 0.08 -3.79 -3.46 1.00 1594 2029
age 0.00 0.00 0.00 0.00 1.00 3528 2531
job 0.00 0.00 -0.00 0.00 1.00 4797 2675
marital 0.01 0.01 -0.01 0.03 1.00 3316 2786
education 0.01 0.00 0.00 0.01 1.00 5327 2282
default -0.04 0.02 -0.07 -0.00 1.00 2038 2161
housing 0.00 0.01 -0.01 0.01 1.00 4360 2799
loan -0.00 0.01 -0.02 0.01 1.00 4425 2576
contact -0.05 0.02 -0.09 -0.02 1.00 1548 2059
month -0.01 0.00 -0.01 -0.00 1.00 4835 2970
day_of_week 0.00 0.00 -0.00 0.01 1.00 4417 2338
duration 0.00 0.00 0.00 0.00 1.00 3936 3016
campaign -0.01 0.00 -0.01 0.00 1.00 4624 2308
pdays -0.00 0.00 -0.01 0.00 1.00 1445 2041
previous -0.01 0.01 -0.03 0.02 1.00 1716 2506
poutcome 0.02 0.02 -0.01 0.06 1.00 1393 1836
emp.var.rate -0.01 0.01 -0.03 0.01 1.00 2081 2135
cons.price.idx -0.00 0.00 -0.01 0.00 1.00 1896 2111
cons.conf.idx 0.00 0.00 -0.00 0.00 1.00 2250 2929
euribor3m -0.00 0.00 -0.00 0.00 1.00 4447 2832
nr.employed -0.03 0.01 -0.04 -0.01 1.00 2214 2647
TABLE III
LOO-CV M ODEL COMPARISON RESULTS .
Model elpd_diff se_diff
logit_model 0.0 0.0
probit_model -1860.9 49.7
of uncertainty, the results strongly favor the logit_model,
indicating its superior predictive capacity in this analys is.
D. Out of Sample Prediction
Table 4 presents prediction results for the Bayesian Logit
Model, summarizing key statistics for three instances. The ﬁrst
instance has an estimated prediction of 0.257 with a standar d
error of 0.437 and a 95% CI ranging from 0 to 1, indicating
TABLE IV
PREDICTION RESULTS FOR LOGIT MODEL
Estimate Est. Error Q2.5 Q97.5
1 0.257 0.437 0 1
2 0.159 0.365 0 1
3 0.111 0.314 0 1
substantial uncertainty. Similarly, the second instance h as an
estimate of 0.159 (SE 0.365) and the third 0.111 (SE 0.314),
both with wide CI from 0 to 1, reﬂecting variability and
uncertainty in the predictions.
Table 5 provides the prediction results for the Bayesian
Probit Model, detailing the estimated values (Estimate), t heir
associated standard errors (Est. Error), and the 95% CI (Q2. 5

TABLE V
PREDICTION RESULTS FOR PROBIT MODEL
Estimate Est. Error Q2.5 Q97.5
1 0.638 0.725 0.5 0.977
2 0.636 0.720 0.5 0.977
3 0.542 0.629 0.5 0.841
and Q97.5) for three predicted instances. The ﬁrst instance
shows an estimate of 0.638 with a standard error of 0.725,
and a 95% CI ranging from 0.5 to 0.977. This suggests a
relatively high predicted value with moderate uncertainty , as
reﬂected in the large standard error and the CI, which covers a
wide range. Similarly, the second instance has an estimate o f
0.636, also with a standard error of 0.720 and a CI from 0.5 to
0.977. The third instance presents a slightly lower estimat e of
0.542 with a standard error of 0.629, and a narrower CI (0.5 to
0.841), indicating a bit more precision in this case compare d
to the others.
E. Discussion
The research ﬁndings demonstrate that both the Bayesian
Logit and Probit regression models applied to 10,000 ob-
servations provide reliable estimates for predicting outc omes,
though their predictive performance varies. In both models ,
predictors like "marital status", "education", and "conta ct"
show signiﬁcant effects. As shown in Table 1, the Bayesian
Logit Regression model converges effectively with Rhat val ues
of 1.00 and sufﬁciently large ESS values, ensuring reliable
parameter estimation. The Probit model on Table 2 also
converged with similar stability. Moreover, Table 3 compar es
the two models using Leave-One-Out Cross-V alidation (LOO-
CV). The Logit model outperforms the Probit model, with
an elpd_diff of 0.0 and -1860.9 for the Probit model,
indicating better predictive accuracy for the Logit model
despite some uncertainty se_diff. On the other hand, Out-
of-sample predictions in Tables 4 and 5 reﬂect similar patte rns
of uncertainty in both models, though the Logit model con-
sistently provides better predictive performance. Overal l, the
Bayesian Logit Regression model proves to be more accurate
and reliable in forecasting outcomes.
VI. C ONCLUSION
This study used a dataset from a Portuguese bank's direct
marketing campaign to assess the performance of logit and
probit models in predicting client subscriptions to bank te rm
deposits. To ensure fair and thorough testing of the models,
this research employed Bayesian modeling techniques and
balanced the dataset. Using Leave-One-Out Cross-V alidati on
(LOO-CV) as a measure of prediction accuracy, this research
results showed that the logit model routinely beat the probi t
model. Based on these results, it seems like the logit model
might work better here for classifying customer subscripti on
behavior into two categories. In complicated ﬁelds like ﬁna n-
cial marketing, the study shows how important it is to choose
the right models for imbalanced datasets. Financial instit utions
can improve their decision-making processes, ﬁne-tune the ir
marketing tactics, and better target their customers with t he
knowledge gathered from this research. To further enhance
prediction accuracy in comparable applications, future st udies
could investigate other modeling techniques, such as ensem ble
methods or non-linear classiﬁers.
REFERENCES
[1] E. Jiang, Z. Wang, and J. Zhao, “Prediction of Term Deposi t in Bank:
Using Logistic Model”, BCP Business & Management , vol. 34, pp. 607–
614, 2022.
[2] Z. K. Mundargi, A. Bodhankar, A. Mahajan, D. Prasad, S. Ma hajan,
and R. Dhakalkar, “Bank Fixed Term Deposit Analysis Using Ba yesian
Logistic Regression”, ICONAT, Goa, India, pp. 1–4, 2023.
[3] L. Setiyani, A. Indahsari, A. Rosalina, and T. Wansen, “F inding the
Best Techniques for Predicting Term Deposit Subscriptions (Case Study
UCI Machine Learning Dataset)”, Proceedings of the International
Conference, pp. 100–104, 2022.
[4] J. Alexandra and K. P . Sinaga, “Machine Learning Approac hes for Mar-
keting Campaign in Portuguese Banks”, ICORIS, Makasar, Indonesia,
pp. 1–6, 2021.
[5] H. Elsalamony, “Bank Direct Marketing Analysis of Data M ining
Techniques”, International Journal of Computer Applications , vol. 85,
pp. 1–8, 2013.
[6] A. Gupta, A. Raghav, and S. Srivastava, “Comparative Stu dy of Machine
Learning Algorithms for Portuguese Bank Data”, ICCCIS, Greater
Noida, India, pp. 401–406, 2021.
[7] Jiang, Enjing and Wang, Zihao and Zhao, Jiaying. Predict ion of Term
Deposit in Bank: Using Logistic Model. BCP Business & Management ,
34. 607-614, 2022.
[8] Alaa Abu-Srhan, Bara’a Alhammad, Sanaa Al zghoul and Riz ik Al-
Sayyed, “Visualization and Analysis in Bank Direct Marketi ng Predic-
tion” IJACSA, 10(7), 2019.
[9] Z. K. Mundargi, A. Bodhankar, A. Mahajan, D. Prasad, S. Ma hajan
and R. Dhakalkar, "Bank Fixed Term Deposit analysis using Ba yesian
Logistic Regression," ICONAT, Goa, India, 2023, pp. 1-4, 2023.
[10] Setiyani, Lila and Indahsari, Ayu and Rosalina, and Wan sen, Tjong.
Finding the Best Techniques for Predicting Term Deposit Sub scriptions
(Case Study UCI Machine Learning Dataset) . 100-104, 2022.
[11] J. Alexandra and K. P . Sinaga, "Machine Learning Approa ches for Mar-
keting Campaign in Portuguese Banks," ICORIS, Makasar, Indonesia,
pp. 1-6, 2021.
[12] S. E. Saeed, M. Hammad and A. Alqaddoumi, "Predicting Cu stomer’s
Subscription Response to Bank Telemarketing Campaign Base d on
Machine learning Algorithms," International Conference on Decision
Aid Sciences and Applications (DASA) , Chiangrai, Thailand, pp. 1474-
1478, 2022.
[13] Sagala, Noviyanti and Permai, Syarifah. Predictive Mo del using SVM
to Improve the Effectiveness of Direct Marketing. 1-6, 2021 .
[14] Elsalamony, Hany. Bank Direct Marketing Analysis of Da ta Mining
Techniques. International Journal of Computer Applications , 85, 2013.
[15] A. Gupta, A. Raghav and S. Srivastava, "Comparative Stu dy of Machine
Learning Algorithms for Portuguese Bank Data," International Confer-
ence on Computing, Communication, and Intelligent Systems (ICCCIS),
Greater Noida, India, pp. 401-406, 2021.
[16] N. Sonkar, R. K. Chaurasiya, M. Choubey, R. Prasad and R. K. Baghel,
"Prediction of Potential Customers for Term Deposit: Analy sis Using
Bagging with Bank Marketing Data," SCEECS, Bhopal, India, pp. 1-6,
2024.
[17] Reddy, N.S. Optimal feature selection and hybrid deep l earning for
direct marketing campaigns in banking applications. Evol. Intel , 15,
1969–1990, 2022.
[18] Marinakos, G., Daskalaki, S. Imbalanced customer clas siﬁcation for
bank direct marketing, J Market Anal , 5, 14–30, 2017.
[19] Rita P . Moro, S. and P . Cortez. Bank Marketing. UCI Machine Learning
Repository, 2012.
[20] Fahrmeir Ludwig, Thomas Kneib, Stefan Lang, and Brian M arx. Regres-
sion: Models, Methods and Applications. Springer Berlin Heidelberg ,
ISBN 9783642343339, 2013.
[21] B. Lambert, A Student’s Guide to Bayesian Statistics. 1 st ed. Sage
Publications Ltd , 2018.
[22] J. M. Hilbe, Practical Guide to Logistic Regression. Chapman and
Hall/CRC, 2015.

This figure "fig1.png" is available in "png"
 format from:
http://arxiv.org/ps/2410.21539v1
