---
title: 'PLSP (Pre-hoc Liminal Space Profiling): OOD Prediction over Detection -- An Anticipatory Approach
  for Machine Learning Model Reliability'
url: https://arxiv.org/abs/2609.12225
category: ai-marketing
subcategory: measurement
date: 2026-09
venue: ''
authors:
- Vipul Bansal
- Himanshu Buckchash
- Balasubramanian Raman
- Deepak Dhungana
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.12225
pages: 10
chars: 28550
fetched_at: '2026-11-08T13:27:51+00:00'
kb_version: 1
---

# PLSP (Pre-hoc Liminal Space Profiling): OOD Prediction over Detection -- An Anticipatory Approach for Machine Learning Model Reliability

PLSP (PRE-HOCLIMINALSPACEPROFILING): OOD
PREDICTION OVERDETECTION– ANANTICIPATORYAPPROACH
FORMACHINELEARNINGMODELRELIABILITY
Vipul Bansal
Indian Institute of Technology Roorkee
Roorkee, India
Himanshu Buckchash∗
IMC University of Applied Sciences
Krems, Austria
Balasubramanian Raman
Indian Institute of Technology Roorkee
Roorkee, India
Deepak Dhungana
IMC University of Applied Sciences
Krems, Austria
ABSTRACT
Out-of-Distribution (OOD) data poses a significant threat to machine learning models, often leading
to model failure during deployment. All existing OOD detection methods are post-hoc, relying
on evaluation metrics such as accuracy and AUC-ROC during inference to indirectly assess the
model’s response to OOD data by measuring deviations. In contrast to existing approaches, the
proposed work shifts the paradigm fromOOD detection to OOD predictionby proposing a pre-hoc
anticipatory framework called PLSP for OOD prediction. We make several key contributions: (a) a
dataset-independent metric called the CREDibility Score (CREDS) is proposed for OOD prediction;
(b) credibility curves are introduced to study the maximum credibility a model can attain; and (c)
credibility heat maps (and volume under surface) are introduced to characterize pre-hoc model
behavior across different datasets. This work provides a novel perspective on signal processing under
distributional shifts. Experiments across multiple datasets demonstrate that the proposed metric
serves as a valuable measure for improving the robustness of machine learning models toward OOD
prediction.
Keywordsout-of-distribution detection · OOD prediction · model robustness · distribution shift · machine learning
reliability·credibility metrics
1 Introduction
Many real world critical applications of machine learning such as medical image analysis or anomaly detection, share the
common challenge of (inference-time) distribution shift in various degrees [1]. This problem arises due to the presence
of OOD data during inference due to regional or environmental changes [ 2, 3]. This leads to reduced performance,
increased safety risk, reduced customer satisfaction, and revenue and trust loss to the service provider [4].
Main reason behind this challenge is the inability of machine learning methods to exhaustively model the underlying data
distribution [5, 6, 7]. Supervised models are often trained by minimizing the generalization error with the assumption
that the train and test samples are drawn from an i.i.d. distribution [8]. This assumption however, does not hold on the
real world data due to the presence of out-of-distribution (OOD) samples [4, 7, 9, 10, 11].
In the existing literature, the generalization performance is measured either using metrics like average or worst-
case accuracy over multiple OOD datasets [12, 13, 14, 15], or through a distance metric over a single OOD dataset
∗© 2026 EURASIP. Accepted for publication in the Proceedings of the 34th European Signal Processing Conference (EUSIPCO
2026), published by EURASIP. This work was supported in part by MeitY , Govt. of India, and IMC University of Applied
Sciences Krems, Austria. Vipul Bansal’s contributions were made at IIT Roorkee, India. Correspondence can be made to:
himanshu.buckchash@imc.ac.at.
arXiv:2609.12225v2  [cs.LG]  15 Oct 2026

Figure 1: Direct correlation between CREDS and accuracy across increasing noise levels (0-50%) for different datasets,
demonstrating CREDS as an effective competitor to post-hoc metrics.
[4, 9, 11, 16, 10, 17, 18]. However, these approaches, do not directly perceive the importance of features during OOD
data evaluation. Due to this, they are not able to assess the impact of changes on the model for any given OOD data
sample [19, 20, 21, 22]. These approaches also lack the ability to measure generalization of the model for any potential
change in OOD input. However, the proposedCREDSmetric perceives bothfeature level understandingof a model
anddistributional changes. It enables the assessment of the maximum possible credibility in case of variation in the
form of a given OOD dataset and also in absence of an OOD dataset.
In this work,Credibilityis defined as the measure of generalizability of a model. High credibility implies higher
generalization ability of the model, similarly, low credibility implies low generalization capacity of the model.
Our findings reveal that the proposed pre-hoc CREDS metric provides estimates comparable to the post-hoc accuracy
metric, as evidenced by the monotonous decline in both measures with increasing noise across all datasets (Fig. 1).
This correlation demonstrates that CREDS serves as a valid measure of model trustworthiness and generalizability.
Critically, unlike existing post-hoc metrics, CREDS can be evaluatedin the absence of any OOD dataset(s), offering
the distinct advantage that model behavior under distributional shifts can be studied and adjusted during the development
environment before deployment, thereby preventing catastrophic failures in production settings.
CREDS operatesby first measuring how much the statistical distribution of each input feature in new data deviates from
its training-data counterpart, for each specific class. This deviation is converted into a foundational credibility score for
the feature and class, subsequently weighted by the model’s reliance on that feature. Finally, these model-aware feature
credibilities are aggregated across all features and then averaged over all classes to produce the overall CREDS score.
The main contributions of this work are:
• To the best of our knowledge, we are the first to propose a direct measure (CREDS) of a machine learning
model’s generalization ability and show its application. It is an approximate formulation, under assumptions,
since a closed form solution is not possilbe.
• We also propose a method to assess possible changes in the credibility of a model upon distributional changes
due to OOD data during inference. The proposed AUC metric for change in credibility, helps us understand
generalization of a model for a particular OOD dataset. We also propose a new V olume Under Surface (VUS)
metric to measure the extent of model generalization for changes in input distribution, given we don’t have any
OOD data to evaluate our model.
• We conduct experiments on multiple datasets to show the usage of credibility scores and associated methods to
evaluate models. We also study the impact of noise on credibility and generalization of a model.
2

2 Credibility Based OOD Evaluation
In Section 2.1, we mathematically introduce CREDS that helps us to evaluate how the model sees an input distribution.
It is an approximate formulation (under stated assumptions) which is empirically validated to work. In Section 2.2,
we then introduce credibility curves to understand the change in credibility score with changing mean and deviation.
From these curves, we find the maximum possible credibility score, a model can achieve, given changes in an input data
stream. Lastly, In Section 2.3, we evaluate the overall vulnerability of the model for OOD data.
2.1 Credibility Score (CREDS)
The way a model is affected by OOD data depends mainly on two factors. Firstly,how does the distribution of OOD
data vary w.r.t. the training data?Secondly,how the changes in feature distribution are perceived by the model?To
understand this, we mathematically define credibility (CREDS),C k,j for thek th feature, given a class labeljas:
Ck,j =e −DKL (p(X v k |Y=j)||q(X t k|Y=j))
=e
−Ep(Xv k |Y=j)
h
log
 p(Xt k |Y=j)
q(X v k |Y=j))
i (1)
Where X t k and X v k are kth feature for training and OOD dataset respectively, and q and p are the respective probability
distributions. Here,D KL represents the KL divergence between the two distributions [23, 24]. If we considerpandq
as multivariate normal distributions with mean µv,k and µt,k and covariance matrix Σv,k and Σt,k respectively with
dimensionsλ, then we can compute:
DKL (p||q) = 1 2 n tr{Σ−1 t,k Σv,k}
+ (µt,k −µ v,k)T Σ−1 t,k (µt,k −µ v,k)
−λ+ ln |Σt,k| |Σv,k| o
(2)
For simplicity of calculation (for tractability and feasibility) we can estimate deviation σv,k for the dataset instead of
covarianceΣ v,k. Assuming a normal distribution, we can rewriteD KL as:
DKL =
h
ln
 σt,k
σv,k

+
σ2 v,k + (µv,k −µ t,k)2
2σ2 t,k − 1 2 i (3)
Even if the true distributions aren’t perfectly Gaussian, changes in their central tendency (mean) and dispersion
(variance) are often the most significant and impactful types of shifts for many ML models. The GaussianDKL formula
is sensitive to exactly these. Moreover, by calculatingC k,j for each feature and class, CREDS can pinpoint where the
distributional shift is occurring at a granular level.
The credibility Ck,j just accounts for distribution difference in between OOD data and training data. To incorporate
how model perceives the distributional changes, we take feature importancefk into account to calculate class credibility
Cj as: Cj = P k fkCk,j. To estimate a feature’s overall effects on the results, we can also estimate Ck for a given
feature as: Ck = P j njP j nj Ck,j. Where nj are the number of samples in class j of training dataset. We can further
compute the overall credibility scoreCof the model as:
C=
X
j
X
k
njP
j nj
fkCk,j (4)
Overall, credibility C is a collective measure of: “How model observes input distribution weighted over all the classes
and features".
The credibility score (CREDS) isnot a performance scorelike Accuracy or AUC-ROC. Instead it tells us about
feasibility to utilize our model to predict on given test data. The metric helps to understand tendency to generalize under
unknown distributions. This includes both data and model’s perspective on perceiving the data.
2.2 Credibility Curves
To evaluate the changes observed in credibility score with mean and deviation of input data stream we propose utilization
of credibility curves. These curves show changes inC j for a classjby fixing eitherµ v,k orσ v,k for allkfeatures.
3

To assess generalization of credibility for a class j with given set of σv,k, we vary the value of µv,k for each feature in a
range −ϵ to +ϵ given ϵ >0. We calculate Area Under the Cj vs µv curve for a given class k to estimate the potential of
network as:
AU Cµv ϵ j =
Z ϵ
−ϵ
X
k
fkCk,j (µt,k, µv, σt,k, σv,k)dµv (5)
AU Cµv ϵ = X
j
njP
j nj
AU Cµv ϵ j (6)
where Ck,j (.) function gives estimate of Ck,j for a set of parameters. Similarly, we calculate Area Under the Cj vs σv
curve for a given classkto estimate the potential of network as:
AU Cσv ϵ j =
Z ϵ
0
X
k
fkCk,j (µt,k, µv,k, σt,k, σv)dσv (7)
AU Cσv ϵ = X
j
njP
j nj
AU Cσv ϵ j (8)
Higher the value of AU Cµv ϵ j or AU Cσv ϵ j, more credibility one model can sustain for each class j on potential changes
in µv or σv. We also estimate the maximum credibility C µ j,max and C σ j,max for variation of µv and σv respectively. For
that we estimate∂C k,j /∂µv and∂C k,j /∂σv as:
∂Cj
∂µv
=
X
k
fk
∂Ck,j
∂µv
=−
X
k
fk
(µv −µ t,k)
σ2 t,k Ck,j (9)
∂Cj
∂σv
=
X
k
fk
∂Ck,j
∂σv
=
X
k
fk
h 1
σv
− σv
σ2 t,k
i
Ck,j (10)
For a maxima we estimate Cj such that ∂Cj/∂µv = 0 and ∂2Cj/∂2µv <0 and ∂Cj/∂σv = 0 and ∂2Cj/∂2σv <0 .
For the case, given µt,k =µ t∀k, one possible solution for same is µv =µ t. Other possible way to find a maxima, is to
generate samples for range of values for µv and σv and estimate C µ j,max and C σ j,max. These curves help to see how
change in current distribution affects the credibility score of the potential data.
2.3 Model Vulnerability Analysis
If we don’t have an available OOD dataset, we would still like to see how our model behave to potential OOD
distributions. To do so we plot a heatmap of Cj with variation in both µv,k and σv,k such that µv,k =µ v∀k and
σv,k =σ v∀k. These plots help us to understand variation of credibility for a class with distribution of data.
Similar to AU Cϵ µvj and AU Cϵ σvj we can compute the V olume Under the Surface (VUS) of these plots betweenCj, µv
and σv to see how well the model performs for a class when there is a change in distribution. Mathematically we can
define it as:
V U Sα,β j =
Z α
0
Z β
−β
X
k
fkCk,j (µt,k, µv, σt,k, σv)dµvdσv (11)
V U Sα,β = X
j
njP
j nj
V U Sα,β j (12)
Where V U Sα,β gives an overall metrics for a model. Higher the value of V U Sα,β j , more chances for a class to achieve
better credibility for potential OOD data. If all the features of the dataset have a µt,k = 0 and σt,k = 1, then there is
atleast one point for whichC j is exactly equal to 1.
3 Experiments
This section demonstrates how these methods can be utilized for evaluating various cases. We evaluate on five benchmark
datasets spanning handwritten digits (MNIST [25], SVHN [26]) and natural images (CIFAR-10 [27], CINIC-10 [28],
STL10 [29]), with training samples ranging from 500 to 90K. All images are preprocessed into feature vectors of size
49 (digit datasets) or 64 (natural image datasets) through dimensionality reduction. This diverse collection enables
comprehensive evaluation across different data distributions and complexities. Additionally,Noisy Datasetsare created
to see how increasing noise impacts the model credibility. Four noise levels are used:10%,20%,30%,and40%.
4

Table 1: Overall CREDS results (with mean and deviation) for MNIST and SVHN. Credibility is estimated for all the
permutations of SVHN and MNIST dataset. Additionally, noise was varied in each dataset from 0% to 50 % to note the
change in CREDS.
Train Dataset Test Dataset Credibility
MNIST
SVHN 0.458±0.085
MNIST 0.971±0.021
MNIST(10% Noise) 0.853±0.059
MNIST(20% Noise) 0.745±0.072
MNIST(30% Noise) 0.646±0.077
MNIST(40% Noise) 0.550±0.072
SVHN
MNIST 0.444±0.083
SVHN 0.986±0.003
SVHN(10% Noise) 0.943±0.007
SVHN(20% Noise) 0.847±0.012
SVHN(30% Noise) 0.730±0.015
SVHN(40% Noise) 0.617±0.017
3.0.1 Training Details
We run experiments by pairing MNIST with SVHN and CIFAR-10 with CINIC-10 and STL-10. The dataset MNIST
and SVHN form a pair of dataset which are out of distribution for each other. CIFAR-10, CINIC-10 and STL-10 forms
a group datasets which is partially different from each other. We train a random forest [ 30] model on features and
utilize the feature importance received from the model to calculate credibility scores (CREDS), C. We further estimate
credibility curves by changing µv and σv and estimate C µ max and C σ max for the dataset and also estimate AU C5 µv and
AU C5 σv. For these datasets we also estimateV U S5,5.
3.0.2 Credibility on MNIST & SVHN
We train our model on MNIST and test on SVHN and vice versa and observe the credibility score as given in Table 1.
Intra-dataset training and testing on MNIST & SVHN give high CREDS values of 0.971 & 0.986 respectively. Higher
CREDS on intra-dataset evaluation, show that the test data acts like an In-Distribution for the model. This is because
µv,k →µ t,k and σv,k →σ t,k. This brings DKL(refer (Equation 3)) tend to 0, in turn bringing Ck,j(refer (Equation 1))
close to 1. When training on MNIST and testing on SVHN, CREDS is 0.4581, indicating significant dataset differences.
The reverse configuration yields 0.4446, slightly lower due to differences in prior distributions p(X t k/Y=j) , feature
importances fk, and class distributions nj/ P j nj. Note that Ck,j, being exponential in DKL, captures larger variations
at higherD KL values despite small changes in credibility.
3.0.3 Credibility on CIFAR-10, CINIC-10 & STL-10
Intra-dataset CREDSs (Table 2) are high: 0.998, 0.999, and 0.997 for CIFAR-10, CINIC-10, and STL-10 respectively.
CIFAR-10/CINIC-10 cross-evaluation yields∼0.94, as CINIC-10 contains CIFAR-10 images, making prior probabilities
p(X t k/Y=j) similar. However, CIFAR-10/STL-10 cross-evaluation drops to ≈ 0.89, indicating dissimilar feature
distributions despite visual similarity.
3.0.4 Impact of Noise on Credibility
Addition of Gaussian noise N(0,1) deviates the posterior probability p(X v k |Y=j) from the prior p(X t k|Y=j) ,
decreasing credibility Ck,j (Tables 1 and 2). MNIST exhibits larger credibility drops than SVHN due to simpler learned
features being more susceptible to noise.
3.0.5 Credibility Curves
Fig. 2 shows credibility curves for µv and σv variations. MNIST-trained models show lower C µ j,max and C σ j,max than
SVHN-trained models, indicating higher susceptibility to distributional changes. CIFAR-10 and CINIC-10 exhibit
similar credibility patterns, reflecting their dataset similarity.
5

(a) (b) (c) (d)
Figure 2: Credibility Curves for variation in µv and σv for (a) model trained on MNIST and tested on SVHN (b) model
trained on SVHN and tested on MNIST (c) model trained on CINIC-10 and tested on CIFAR-10 (d) model trained on
CIFAR-10 and tested on CINIC-10.
Table 2: Credibility results (with mean and std.) for experiments on CIFAR-10, STL-10, and CINIC-10. Credibility is
estimated for all the permutations of all datasets. Noise was varied in each dataset from 0% to 50 % to note the change
in CREDS.
Train Dataset Test Dataset Credibility
CIFAR 10
CINIC-10 0.940±0.059
STL-10 0.892±0.080
CIFAR-10 0.998±0.000
CIFAR-10(10% Noise) 0.964±0.005
CIFAR-10(20% Noise) 0.881±0.013
CIFAR-10(30% Noise) 0.774±0.020
CIFAR-10(40% Noise) 0.667±0.026
CINIC-10
STL-10 0.940±0.047
CIFAR-10 0.942±0.055
CINIC-10 0.999±0.000
CINIC-10(10% Noise) 0.967±0.003
CINIC-10(20% Noise) 0.884±0.011
CINIC-10(30% Noise) 0.776±0.017
CINIC-10(40% Noise) 0.667±0.022
STL-10
CIFAR-10 0.894±0.094
CINIC-10 0.939±0.061
STL-10 0.997±0.000
STL-10(10% Noise) 0.965±0.009
STL-10(20% Noise) 0.880±0.021
STL-10(30% Noise) 0.770±0.030
STL-10(40% Noise) 0.660±0.035
3.0.6 Maximum Credibility Potential of a Model
Tables 3 and 4 demonstrate models can achieve maximum potential credibilities (C µ max, C σ max) exceeding their baseline
C on OOD data (e.g., MNIST → SVHN baseline C= 0.4581 , but C µ max = 0.6323). Adding Gaussian noise minimally
impacts C µ max but significantly degrades C σ max, showing that noise limits model robustness primarily through variance
shifts rather than mean shifts.
6

Table 3: C µ max, C σ max, AU C5 µv and AU C5 σv on MNIST and SVHN (with mean and std. on multiple runs). C µ max,
C σ max, AU C5 µv and AU C5 σv are estimated for all the permutations of SVHN and MNIST. Noise was varied from 0% to
50 % to observe how noise effectsC µ max,C σ max,AU C5 µv andAU C5 σv.
Train Dataset Test Dataset C µ max C σ max AU C5 µv AU C5 σv
MNIST
SVHN 0.632±0.091 0.536±0.093 1.715±0.202 1.678±0.274
MNIST 0.756±0.103 0.869±0.071 1.885±0.339 2.314±0.259
MNIST(10% Noise) 0.762±0.091 0.805±0.074 1.953±0.329 2.199±0.261
MNIST(20% Noise) 0.749±0.096 0.716±0.069 2.031±0.332 2.041±0.248
MNIST(30% Noise) 0.747±0.094 0.637±0.068 2.119±0.337 1.890±0.239
MNIST(40% Noise) 0.735±0.096 0.557±0.064 2.199±0.350 1.723±0.226
SVHN
MNIST 0.687±0.068 0.565±0.039 2.067±0.244 1.963±0.115
SVHN 0.987±0.003 0.996±0.001 2.705±0.083 2.750±0.023
SVHN(10% Noise) 0.986±0.003 0.948±0.007 2.728±0.081 2.671±0.030
SVHN(20% Noise) 0.980±0.003 0.851±0.011 2.801±0.078 2.498±0.036
SVHN(30% Noise) 0.968±0.003 0.743±0.012 2.904±0.072 2.283±0.039
SVHN(40% Noise) 0.947±0.003 0.645±0.012 3.026±0.067 2.062±0.039
Table 4: C µ max, C σ max, AU C5 µv and AU C5 σv for various experiments on CIFAR-10, STL-10 and CINIC-10 datasets.
Results are reported in the form of mean and deviation across multiple runs. C µ max, C σ max, AU C5 µv and AU C5 σv are estimated for all the permutations of CIFAR-10, STL-10 and CINIC-10 dataset. Additionally, we increase noise level in
each dataset from 0% to 50 % to observe how noise effectsC µ max,C σ max,AU C5 µv andAU C5 σv.
Train Dataset Test Dataset C µ max C σ max AU C5 µv AU C5 σv
CIFAR 10
CINIC-10 0.963±0.023 0.956±0.046 2.305±0.110 2.643±0.096
STL-10 0.953±0.022 0.922±0.067 2.250±0.140 2.590±0.131
CIFAR-10 0.976±0.019 0.995±0.002 2.387±0.175 2.705±0.080
CIFAR-10(10% Noise) 0.976±0.019 0.962±0.007 2.412±0.172 2.654±0.080
CIFAR-10(20% Noise) 0.976±0.018 0.885±0.012 2.483±0.166 2.526±0.085
CIFAR-10(30% Noise) 0.973±0.017 0.791±0.017 2.585±0.161 2.354±0.088
CIFAR-10(40% Noise) 0.964±0.015 0.700±0.021 2.707±0.156 2.169±0.091
CINIC-10
STL-10 0.971±0.011 0.949±0.050 2.365±0.161 2.643±0.101
CIFAR-10 0.971±0.017 0.954±0.046 2.433±0.178 2.650±0.069
CINIC-10 0.984±0.011 0.997±0.002 2.423±0.123 2.718±0.061
CINIC-10(10% Noise) 0.984±0.011 0.965±0.003 2.449±0.121 2.668±0.064
CINIC-10(20% Noise) 0.983±0.010 0.887±0.010 2.522±0.120 2.537±0.070
CINIC-10(30% Noise) 0.978±0.008 0.791±0.016 2.629±0.116 2.360±0.073
CINIC-10(40% Noise) 0.967±0.007 0.697±0.019 2.754±0.114 2.169±0.075
STL-10
CIFAR-10 0.950±0.035 0.915±0.075 2.409±0.170 2.558±0.099
CINIC-10 0.958±0.030 0.951±0.048 2.378±0.128 2.619±0.074
STL-10 0.966±0.029 0.993±0.002 2.356±0.151 2.686±0.080
STL-10(10% Noise) 0.967±0.028 0.962±0.009 2.382±0.149 2.638±0.087
STL-10(20% Noise) 0.967±0.027 0.884±0.018 2.454±0.148 2.509±0.096
STL-10(30% Noise) 0.964±0.025 0.787±0.026 2.559±0.144 2.333±0.104
STL-10(40% Noise) 0.954±0.023 0.693±0.029 2.685±0.142 2.144±0.105
3.0.7 Model Generalization on Varying OOD Dataset
We compute AU C5 µv and AU C5 σv (Tables 3, 4) to quantify generalization under parameter variations. As expected, AUC
values are higher for structurally similar test sets. With increasing noise, AU C5 µv rises while AU C5 σv falls, suggesting model credibility remains more consistent under mean shifts than under deviation shifts in noisy environments.
3.0.8 Overall Model Generalization Estimates
Credibility heatmaps (Fig. 3) reveal class-specific patterns in Cj for simultaneous µv and σv variations. V U S5,5 results
(Table 5) show SVHN models generalize better than MNIST, while CINIC-10 slightly outperforms CIFAR-10 and
STL-10 due to ImageNet augmentation and larger sample size.
7

(a) (b)
Figure 3: Credibility heatmaps for model trained on (a) MNIST and (b) SVHN for class labels 0 (top) and 1 (bottom).
Table 5: V U S5,5 calculated for models trained on MNIST, SVHN, CIFAR-10, STL-10 and CINIC-10, with mean and
deviation across multiple runs.
Train Dataset V U S5,5
MNIST 10.99±1.62
SVHN 13.93±0.19
CIFAR-10 13.55±0.66
STL-10 13.39±0.65
CINIC-10 13.64±0.50
4 Conclusion
This work introduces PLSP, a paradigm shift from post-hoc OOD detection to pre-hoc OOD prediction through the
CREDibility Score (CREDS) metric. Unlike existing approaches requiring OOD datasets during inference, CREDS
enables anticipatory assessment of model behavior under distributional shifts during development. Experiments across
MNIST, SVHN, CIFAR-10, CINIC-10, and STL-10 demonstrate that CREDS provides estimates comparable to
post-hoc accuracy metrics while offering evaluation in the absence of OOD data. The introduced credibility curves,
heatmaps, and VUS metrics provide comprehensive tools for analyzing model vulnerability, revealing differential
sensitivity to mean versus variance shifts. The strong correlation between CREDS and accuracy validates its utility as
a pre-deployment robustness indicator, enabling proactive adjustments to prevent catastrophic failures in production
environments.
References
[1] Jingkang Yang, Kaiyang Zhou, Yixuan Li, and Ziwei Liu. Generalized out-of-distribution detection: A survey.
arXiv preprint arXiv:2110.11334, 2021. 1
8

[2] Abhijit Guha Roy, Jie Ren, Shekoofeh Azizi, Aaron Loh, Vivek Natarajan, Basil Mustafa, Nick Pawlowski, Jan
Freyberg, Yuan Liu, Zach Beaver, et al. Does your dermatology classifier know what it doesn’t know? detecting
the long-tail of unseen conditions.arXiv preprint arXiv:2104.03829, 2021. 1
[3] Ishaan Gulrajani and David Lopez-Paz. In search of lost domain generalization. InInternational Conference on
Learning Representations, 2020. 1
[4] Stanislav Fort, Jie Ren, and Balaji Lakshminarayanan. Exploring the limits of out-of-distribution detection.arXiv
preprint arXiv:2106.03004, 2021. 1, 2
[5] Alex Krizhevsky, Ilya Sutskever, and Geoffrey E Hinton. Imagenet classification with deep convolutional neural
networks.Advances in neural information processing systems, 25:1097–1105, 2012. 1
[6] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. Delving deep into rectifiers: Surpassing human-level
performance on imagenet classification. InProceedings of the IEEE international conference on computer vision,
pages 1026–1034, 2015. 1
[7] Nick Drummond and Rob Shearer. The open world assumption. IneSI Workshop: The Closed World of Databases
meets the Open World of the Semantic Web, volume 15, 2006. 1
[8] Yong Liu. Unbiased estimate of generalization error and model selection in neural network.Neural Networks,
8(2):215–219, 1995. 1
[9] Jim Winkens, Rudy Bunel, Abhijit Guha Roy, Robert Stanforth, Vivek Natarajan, Joseph R Ledsam, Patricia
MacWilliams, Pushmeet Kohli, Alan Karthikesalingam, Simon Kohl, et al. Contrastive training for improved
out-of-distribution detection.arXiv preprint arXiv:2007.05566, 2020. 1, 2
[10] Timo Milbich, Karsten Roth, Samarth Sinha, Ludwig Schmidt, Marzyeh Ghassemi, and Björn Ommer. Character-
izing generalization under out-of-distribution shifts in deep metric learning. InAdvances in Neural Information
Processing Systems, 2021. 1, 2
[11] Hoang Thanh-Tung and Truyen Tran. Toward a generalization metric for deep generative models. In”I Can’t
Believe It’s Not Better!”NeurIPS 2020 workshop, 2020. 1, 2
[12] Charlie Frogner, Sebastian Claici, Edward Chien, and Justin Solomon. Incorporating unlabeled data into
distributionally robust learning.Journal of Machine Learning Research, 22(56):1–46, 2021. 1
[13] Zheyan Shen, Peng Cui, Tong Zhang, and Kun Kunag. Stable learning via sample reweighting. InProceedings of
the AAAI Conference on Artificial Intelligence, volume 34, pages 5692–5699, 2020. 1
[14] Jiashuo Liu, Zheyuan Hu, Peng Cui, Bo Li, and Zheyan Shen. Heterogeneous risk minimization.arXiv preprint
arXiv:2105.03818, 2021. 1
[15] Kaiyang Zhou, Ziwei Liu, Yu Qiao, Tao Xiang, and Chen Change Loy. Domain generalization: A survey.arXiv
preprint arXiv:2103.02503, 2021. 1
[16] Haotian Ye, Chuanlong Xie, Yue Liu, and Zhenguo Li. Out-of-distribution generalization analysis via influence
function.arXiv preprint arXiv:2101.08521, 2021. 2
[17] Nanyang Ye, Kaican Li, Lanqing Hong, Haoyue Bai, Yiting Chen, Fengwei Zhou, and Zhenguo Li. Ood-bench:
Benchmarking and understanding out-of-distribution generalization datasets and algorithms.arXiv preprint
arXiv:2106.03721, 2021. 2
[18] Behnam Neyshabur, Srinadh Bhojanapalli, David Mcallester, and Nati Srebro. Exploring generalization in deep
learning.Advances in Neural Information Processing Systems, 30:5947–5956, 2017. 2
[19] Martin Arjovsky, Léon Bottou, Ishaan Gulrajani, and David Lopez-Paz. Invariant risk minimization.stat, 1050:27,
2020. 2
[20] David Krueger, Ethan Caballero, Joern-Henrik Jacobsen, Amy Zhang, Jonathan Binas, Dinghuai Zhang, Remi
Le Priol, and Aaron Courville. Out-of-distribution generalization via risk extrapolation (rex). InInternational
Conference on Machine Learning, pages 5815–5826. PMLR, 2021. 2
[21] Minghao Xu, Jian Zhang, Bingbing Ni, Teng Li, Chengjie Wang, Qi Tian, and Wenjun Zhang. Adversarial domain
adaptation with domain mixup. InProceedings of the AAAI Conference on Artificial Intelligence, volume 34,
pages 6502–6509, 2020. 2
[22] Shen Yan, Huan Song, Nanxiang Li, Lincan Zou, and Liu Ren. Improve unsupervised domain adaptation with
mixup training.arXiv preprint arXiv:2001.00677, 2020. 2
[23] Solomon Kullback.Information Theory and Statistics. Wiley, New York, 1959. 3
[24] Yufeng Zhang, Wanwei Liu, Zhenbang Chen, Kenli Li, and Ji Wang. On the properties of kullback-leibler
divergence between gaussians.arXiv preprint arXiv:2102.05485, 2021. 3
9

[25] Li Deng. The mnist database of handwritten digit images for machine learning research [best of the web].IEEE
Signal Processing Magazine, 29(6):141–142, 2012. 4
[26] Yuval Netzer, Tao Wang, Adam Coates, Alessandro Bissacco, Bo Wu, and Andrew Y . Ng. Reading digits in
natural images with unsupervised feature learning. InNIPS Workshop on Deep Learning and Unsupervised
Feature Learning 2011, 2011. 4
[27] Benjamin Recht, Rebecca Roelofs, Ludwig Schmidt, and Vaishaal Shankar. Do cifar-10 classifiers generalize to
cifar-10?arXiv preprint arXiv:1806.00451, 2018. 4
[28] Luke N Darlow, Elliot J Crowley, Antreas Antoniou, and Amos J Storkey. Cinic-10 is not imagenet or cifar-10.
arXiv e-prints, pages arXiv–1810, 2018. 4
[29] Adam Coates, Honglak Lee, and Andrew Y . Ng. An analysis of single layer networks in unsupervised feature
learning. 2011. 4
[30] Leo Breiman. Random forests.Machine learning, 45(1):5–32, 2001. 5
10
