---
title: 'Online AutoML: Evaluating Poisoning Attacks on Adversarial Training Defense Strategy in IoT Networks'
url: https://arxiv.org/abs/2610.05810
category: ai-marketing
subcategory: measurement
date: 2026-10
venue: ''
authors:
- Chukwunonso Henry Nwokoye
- Khalil El-Khatib
- Li Yang
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.05810
pages: 7
chars: 36152
fetched_at: '2026-11-08T13:25:51+00:00'
kb_version: 1
---

# Online AutoML: Evaluating Poisoning Attacks on Adversarial Training Defense Strategy in IoT Networks

Online AutoML: Evaluating Poisoning Attacks on
Cost-Utility Adversarial Training Defence Strategy
for IoT Networks
∗†Chukwunonso Henry Nwokoye, ∗Khalil El-Khatib, and ∗Li Yang
∗Faculty of Business and Information Technology, Ontario Tech University,Oshawa, Ontario, Canada
†Department of Computer Science, Alex Ekwueme Federal University,Nigeria
Emails:{henrychukwunonso.nwokoye, khalil.el-khatib, li.yang}@ontariotechu.ca
Abstract—Machine learning (ML)-powered poisoning attack
vectors are adversarial maneuvers whereby an attacker inten-
tionally inserts, corrupts, or alters training data to distort an
ML model’s learning process. The objective is to diminish model
efficacy, instill biases, induce misclassifications, or include con-
cealed backdoors that may be attacked during implementation. In
streaming contexts, poisoning attacks pose significant risks since
models perpetually update based on incoming streams of data. An
assailant may incrementally introduce harmful samples into this
data stream, leading the model to assimilate erroneous features
over time without timely identification. Therefore, this study
is aimed at evaluating the efficacy of the adversarial training
(AT) defense approach against poisoning attacks (label flip and
noise injection) using an online AutoML pipeline for Internet
of Things (IoT) networks. Specifically, poisoning attacks (label
flip and noise injection) were applied to streaming-capable Au-
toML learners (Hoeffding Tree (HT), Leveraging Bagging (LB),
Adaptive Random Forest (ARF), Hoeffding Adaptive Tree (HAT),
and Streaming Random Patches (SRP)). Under the strongest
poisoning rate (PR = 1.0), AT-SRP achieved the highest F1-score
against label flip poisoning (0.904), while AT-LB achieved the
highest F1-score against noise-injection poisoning (0.933). Finally,
several drift detection methods were used for rolling accuracy
and prequential evaluation.
Index Terms—Internet of Things (IoT), Security, Online Au-
toML, Data Streams, Automated Data Analytics, Concept Drift,
Online Machine Learning
I. INTRODUCTION
Online machine learning refers to a family of algorithms that
learn incrementally from data arriving as a continuous stream,
updating their models with each new instance rather than re-
training on static datasets [1]. This paradigm is fundamentally
suited to environments where data volumes are unbounded and
computational resources are constrained, requiring models to
process each instance within bounded time and memory [2].
Data streams are characterised by high velocity, potentially
infinite length, and non-stationarity, a property known as con-
cept drift, in which the underlying data distribution shifts over
time [3]. Stream classifiers must therefore adapt continuously,
remaining responsive to distributional changes without storing
or revisiting prior instances [1].
The practical relevance of online learning extends across
several security-critical domains. In cybersecurity, the volume
and velocity of network traffic make batch retraining impracti-
cal, necessitating adaptive models that classify data in real time
[4]. Intrusion Detection Systems (IDS) deployed in IoT net-
works face compounded challenges: the heterogeneous nature
of IoT devices, their resource constraints, and the diversity of
attack vectors demand classifiers that learn continuously from
evolving traffic [5]. Online AutoML frameworks, such as the
River library formed through the merger of creme and scikit-
multiflow, automate the selection and configuration of the best-
performing stream learner within a unified pipeline, making
them particularly attractive for IoT deployments [3]. Beyond
IoT security, online learners are central to financial fraud
detection, where transaction streams must be classified within
milliseconds against continuously shifting fraud patterns [6].
Despite the growing adoption of online AutoML systems
in security-sensitive applications, their resilience to training-
time adversarial manipulation remains poorly understood [4].
Poisoning attacks in which an adversary introduces corrupted
instances into the training stream to degrade model perfor-
mance pose a direct and realistic threat to continuously learn-
ing systems [7]. Unlike static batch models, stream classifiers
update with every incoming instance, meaning each poisoned
data point immediately distorts the learned decision boundary
[8]. Label-flipping attacks, a widespread form of poisoning,
deliberately invert the ground-truth labels of selected training
instances to steer the classifier toward systematic misclassifi-
cation of targeted classes [9]. This vulnerability is further am-
plified by drift detection mechanisms embedded within online
pipelines: a detector influenced by adversarially induced error
patterns may trigger spurious drift alarms, causing premature
model resets and destabilising the learning process [10].
Building on the above studies, this paper makes three
primary contributions. First, we develop a poisoning attack
framework targeting the training stream of an online AutoML
pipeline, implementing label flip and noise injection [11] on
the whole feature space at varying poisoning rates 1.
Second, we evaluate the degradation in accuracy, precision,
recall, and F1-score across five stream classifiers: Hoeffding
Tree (HT), LeveragingBagging (LB), Adaptive Random For-
est (ARF), Hoeffding Adaptive Tree (HAT), and Streaming
Random Patches (SRP). Third, we analyze the behavioral
1Code and supplementary results are available at: https://github.com/
ChiNonsoHenry16/Label-Flip-NoiseInjection OnAutoML
To appear in the Proceedings of IEEE CASCON 2026.
© 2026 IEEE. Personal use of this material is permitted. Permission from IEEE must be obtained for all other uses, in any current or future media, including
reprinting/republishing this material for advertising or promotional purposes, creating new collective works, for resale or redistribution to servers or lists, or reuse of any
copyrighted component of this work in other works.
arXiv:2610.05810v2  [cs.CR]  11 Oct 2026

response of the Early Drift Detection Method (EDDM),
Adaptive Windowing (ADWIN), and Drift Detection Method
(DDM) drift detectors under poisoned conditions and evaluate
the adversarial training defense. Together, these contributions
address an identified gap in the security of online AutoML
systems for IoT environments [4], [12].
II. RELATED WORK
Poisoning attacks constitute a class of training-time ad-
versarial threats in which an attacker manipulates the data
used to build a machine learning model either to degrade
overall accuracy (availability attacks) or to induce targeted
misclassifications (integrity attacks) [8]. Foundational work by
Biggio et al. [13] established that support vector machines
are susceptible to gradient-based poisoning, providing the
theoretical basis for subsequent research in this area. Label-
flipping attacks corrupt training labels without modifying
feature values, making them particularly difficult to detect
through conventional input validation [14]. These attacks are
notoriously hard to detect at scale. Training datasets are often
too large for per-instance inspection, and adversarial label flips
can be subtle, especially in continuously updating systems
[15].
Recent empirical evidence confirms that even modest poi-
soning rates as low as two to five percent of the training
distribution are sufficient to cause significant classification
degradation [9]. In IoT contexts, Tian et al. [7] conducted
a comprehensive survey of poisoning strategies and coun-
termeasures, observing that edge-deployed systems relying
on live data streams are particularly vulnerable due to the
absence of offline validation checkpoints. The attack surface
widens considerably in federated and distributed IoT learning
scenarios, where model updates from multiple heterogeneous
devices are aggregated at a central server [16]. Nguyen et
al. [17] demonstrated that federated IDS systems can be
severely compromised by even a small number of malicious
participants injecting poisoned local updates into the aggrega-
tion process. Yang et al. [18] examined clean-label poisoning
in federated IoT environments, showing that adversaries can
embed malicious behaviour within feature-plausible samples,
effectively evading statistical anomaly detectors. In a clean
label attack, the attacker introduces alterations to the features
while maintaining the labels in an ostensibly ”clean” state.
This is extensively researched and particularly relevant in
situations when an assailant is unable to alter labels (for
instance, automated or crowdsourced data management). Noise
injection can be classified as clean-label and was also specifi-
cally characterized as a data poisoning strategy [11], whereby
hostile noise injected into training data distorts deep learning
frameworks in a visually undetectable way. Collectively, these
findings confirm that poisoning represents an operationally
viable threat to deployed IoT machine learning pipelines, not
merely a theoretical concern [7].
Despite substantial progress in adversarial robustness for
batch machine learning, the security of online AutoML
pipelines against poisoning remains sparsely studied [4].
Fig. 1. The overview of the proposed framework
AT offers a more practical defense posture for resource-
constrained online learners; however, its systematic evaluation
against stream classifiers in IoT security settings has not
been conducted [12]. Likewise, while adversarial concept drift
detection has been explored in isolation [10], its behavior
within a full online AutoML pipeline comprising multiple
learner options has not been studied. This paper directly
addresses these gaps by providing the first joint evaluation of
poisoning attack impact and adversarial defense across HT,
LB, ARF, HAT, and SRP in a unified streaming AutoML
setting.
AT has been named among defense strategies against poi-
soning attacks [19]. Therefore, the AT approach was adapted
along with the dirty (label flip) and clean label [18] (noise
injection) [11] poisoning attacks. Considering the papers re-
viewed herein, we aim to extend the online AutoML pipeline
proposed by Yang & Shami [20] by applying the AT [21].
Furthermore, the impact of poisoning attacks on the improved
pipeline was evaluated using popular metrics. Also, we imple-
mented live learning to manage concept/model drift in real-
time traffic under poisoning attacks.
III. METHODOLOGY
We implement an automated machine learning (AutoML)
pipeline, subsequently applying data poisoning assaults in
both label and feature domains, and using AT as a defensive
strategy, assessed by streaming tree-based classifiers with live
concept drift detection. The study employed the IoTID20
dataset [22], and performance was measured using accuracy,
precision, recall, and F1-score. The proposed methodology is
shown in Fig. 1.
Initially, data undergoes automated preprocessing by the
identification and encoding of categorical variables via label
encoding, then addressing infinite and missing values by sub-
stituting them with zeros. Feature normalization was dynami-
cally determined using a Shapiro-Wilk normality assessment:
if features exhibit statistical Gaussianity, z-score normalization
is applied; if not, min-max scaling transforms features to

the range of ([0, 1]). Dimensionality reduction was achieved
by prioritizing features based on their relevance derived by
LightGBM regression and progressively eliminating those that
contribute less than 10% to the total importance. Superfluous
characteristics exhibiting a strong pairwise Pearson correlation
(r >0.9)are then eliminated, retaining just a single feature
from each associated cluster.
To assess the resilience to poisoning, two offensive tech-
niques are examined. Label flip (LF) poisoning arbitrarily
substitutes the labels of chosen training data with a different
class, determined evenly at random. This traditional ”dirty-
label” assault [13], [23] instills potentially significant confu-
sion into model training. Noise injection (NI) poisoning, seen
as a feature-space and ”clean-label” assault [11], introduces
random uniform (adversarial) noise into each feature of chosen
samples while preserving the labels. Each feature value is
altered by a stochastic value inside±10%of its range and
constrained to its domain, emulating feature-space pollution
of the input distribution.
AT is used as a defensive strategy for the ensemble and
streaming classifiers within River. For each training batch,
subsequent to possible contamination, we generate an extra
AT sample using the same assault methodology and include
both in the model update batch. This resembles the AT
framework proposed by Goodfellow et al. [24], although it
operates in a streaming, online context. Subsequent to train-
ing, we calculate the typical classification metrics—accuracy,
recall, precision, and F1 score—for both the Naive and AT
variants at several poisoning rates (PR). Furthermore, we
implement 3 drift detectors (EDDM, DDM, and ADWIN) on
the classifier output streams, documenting drift occurrences
and examining the relationship between drift instances and the
locations of injected anomalies. For all experiments, we used
predetermined random seeds that guarantee reproducibility and
facilitate direct scenario comparisons.
The streaming classifiers considered for this study include
LB, HAT, ARF, SRP, and HT [20]. We primarily selected them
to ensure architectural variety among streaming classifiers,
including a foundational incremental and drift-responsive tree
(HT and HAT) and 3 ensemble techniques (LB, ARF, and
SRP). In the experimental setup, we developed naive and
adversarially trained (AT) models for each of the online
learners (HT, LB, ARF, SRP, and HAT). The resulting models
are Naive-HT, AT-HT, Naive-LB, AT-LB, Naive-SRP, AT-SRP,
Naive-ARF, AT-ARF, Naive-HAT, and AT-HAT. Implementing
both naive and AT model variants is important for assessing
robustness against poisoning attacks [25].
Poisoning attacks affect the data during the training phase.
In this scenario, the assailant introduces harmful or adver-
sarial instances into the training dataset to distort or skew
the model throughout its training period (in some cases, a
portion of the labels may be altered (label flipping), attributes
modified, etc.). Besides label flip, we executed a feature-space
data contamination assault by including adversarial noise into
training samples [11], whereby noise-infused data is used to
intentionally corrupt the learning process.
TABLE I
NAIVEMODELPERFORMANCEUNDERLABEL-FLIPPOISONING
Classifier Rate Accuracy F1 Precision Recall
Hoeffding Tree 0.0 0.942 0.914 0.888 0.942
Hoeffding Tree 0.4 0.942 0.914 0.888 0.942
Hoeffding Tree 1.0 0.058 0.006 0.003 0.058
Leveraging Bagging 0.0 0.898 0.911 0.928 0.898
Leveraging Bagging 0.4 0.191 0.259 0.857 0.191
Leveraging Bagging 1.0 0.058 0.006 0.003 0.058
SRPClassifier 0.0 0.936 0.911 0.888 0.936
SRPClassifier 0.4 0.286 0.391 0.880 0.286
SRPClassifier 1.0 0.055 0.049 0.452 0.055
Hoeffding Adaptive Tree 0.0 0.942 0.914 0.888 0.942
Hoeffding Adaptive Tree 0.4 0.942 0.914 0.888 0.942
Hoeffding Adaptive Tree 1.0 0.058 0.006 0.003 0.058
Adaptive Random Forest 0.0 0.942 0.914 0.888 0.942
Adaptive Random Forest 0.4 0.839 0.860 0.882 0.839
Adaptive Random Forest 1.0 0.058 0.006 0.003 0.058
IV. RESULTS
In the evaluation of the proposed methodology for ad-
versarial ML threats and control, it is essential to report
metrics for naive and AT model variants. This is usually
referred to as adversarial robustness research [26], and it
allows security managers to understand the extent to which
a particular defense strategy impacts both adversarial attacks
and the metrics.
Here, we present poisoning rate (PR) as well as the Naive
and AT variants of metrics such as accuracy, precision, recall
and F1 score. The PR represents the proportion (%) of the
training dataset that is subjected to manipulation (modifi-
cation). It indicates the quantity of contaminated training
instances. Note that PR ranges from 0.00 to 1.00. To succinctly
illustrate the effects of the poisoning attacks (label flip and
noise injection) at different intensities, we present findings
for three illustrative conditions, namely (a) No attack/baseline
(PR = 0.00), (b) mild attack (PR = 0.40), and (c) strong attack
(PR = 1.00). These represent the baseline, a plausible adver-
sarial situation, as well as an upper-bound worst-case circum-
stance, respectively. For every online classifier, we compared
performances under these conditions to distinctly demonstrate
the susceptibility of the na¨ıve model and the resilience afforded
by the AT approach. The comprehensive results are avail-
able at the following GitHub repository: https://github.com/
ChiNonsoHenry16/Label-Flip-NoiseInjection OnAutoML.
A. Impact of Poisoning Attacks
The label-flip outcomes reveal a significant disparity be-
tween the na ¨ıve and AT setups (Tables I and II). In the
naive setup, raising the PR often results in significant deterio-
ration, with several classifiers attaining F1-scores around zero
at a PR of 1.0. Conversely, AT offers significantly enhanced
robustness for some models. Significantly, SRPClassifier at-
tains an F1-score of 0.904, an accuracy of 0.906, and a recall
of 0.906 at the 1.0 label-flip rate, while HAT records an F1-
score of 0.778. Utilizing LB maintains an F1 score of 0.661
at the maximum PR of 1.00.
Tables III and IV provide the relevant findings for the noise
injection poisoning attack. In contrast to label flipping, noise

TABLE II
AT MODELPERFORMANCEUNDERLABEL-FLIPPOISONING
Classifier Rate Accuracy F1 Precision Recall
Hoeffding Tree 0.0 0.058 0.006 0.003 0.058
Hoeffding Tree 0.4 0.058 0.006 0.003 0.058
Hoeffding Tree 1.0 0.058 0.006 0.003 0.058
Leveraging Bagging 0.0 0.429 0.550 0.905 0.429
Leveraging Bagging 0.4 0.296 0.409 0.860 0.296
Leveraging Bagging 1.0 0.543 0.661 0.871 0.543
SRPClassifier 0.0 0.112 0.124 0.830 0.112
SRPClassifier 0.4 0.153 0.191 0.880 0.153
SRPClassifier 1.00.906 0.9040.9020.906
Hoeffding Adaptive Tree 0.0 0.942 0.914 0.888 0.942
Hoeffding Adaptive Tree 0.4 0.058 0.006 0.003 0.058
Hoeffding Adaptive Tree 1.0 0.703 0.778 0.873 0.703
Adaptive Random Forest 0.0 0.123 0.133 0.909 0.123
Adaptive Random Forest 0.4 0.076 0.064 0.673 0.076
Adaptive Random Forest 1.0 0.058 0.006 0.003 0.058
TABLE III
NAIVEMODELPERFORMANCEUNDERNOISE-INJECTIONPOISONING
Classifier Rate Accuracy F1 Precision Recall
Hoeffding Tree 0.0 0.942 0.914 0.888 0.942
Hoeffding Tree 0.4 0.905 0.922 0.951 0.905
Hoeffding Tree 1.0 0.942 0.914 0.888 0.942
Leveraging Bagging 0.0 0.894 0.909 0.930 0.894
Leveraging Bagging 0.4 0.607 0.709 0.936 0.607
Leveraging Bagging 1.0 0.942 0.937 0.934 0.942
SRPClassifier 0.0 0.942 0.914 0.888 0.942
SRPClassifier 0.4 0.892 0.913 0.949 0.892
SRPClassifier 1.0 0.934 0.937 0.940 0.934
Hoeffding Adaptive Tree 0.0 0.942 0.914 0.888 0.942
Hoeffding Adaptive Tree 0.4 0.942 0.914 0.888 0.942
Hoeffding Adaptive Tree 1.0 0.942 0.915 0.888 0.942
Adaptive Random Forest 0.0 0.942 0.914 0.888 0.942
Adaptive Random Forest 0.40.981 0.980 0.980 0.981
Adaptive Random Forest 1.0 0.942 0.915 0.905 0.942
TABLE IV
ADVERSARIALLYTRAINEDMODELPERFORMANCEUNDER
NOISE-INJECTIONPOISONING
Classifier Rate Accuracy F1 Precision Recall
Hoeffding Tree 0.0 0.686 0.769 0.907 0.686
Hoeffding Tree 0.4 0.718 0.791 0.905 0.718
Hoeffding Tree 1.0 0.721 0.793 0.905 0.721
Leveraging Bagging 0.00.948 0.9520.9580.948
Leveraging Bagging 0.4 0.904 0.921 0.952 0.904
Leveraging Bagging 1.0 0.936 0.933 0.930 0.936
SRPClassifier 0.0 0.923 0.917 0.912 0.923
SRPClassifier 0.4 0.933 0.932 0.932 0.933
SRPClassifier 1.0 0.943 0.925 0.923 0.943
Hoeffding Adaptive Tree 0.0 0.855 0.884 0.929 0.855
Hoeffding Adaptive Tree 0.4 0.891 0.904 0.922 0.891
Hoeffding Adaptive Tree 1.0 0.803 0.848 0.910 0.803
Adaptive Random Forest 0.00.946 0.952 0.962 0.946
Adaptive Random Forest 0.4 0.942 0.914 0.888 0.942
Adaptive Random Forest 1.0 0.942 0.914 0.888 0.942
injection results in a less consistent deterioration across the
na¨ıve models, with some classifiers maintaining comparatively
good efficacy despite elevated poisoning rates. The AT-based
models also have varied reactions. At the peak noise-injection
rate, LB attains an F1 score of 0.933, whilst SRPClassifier
secures 0.925 and HAT reaches 0.848. Consequently, the
findings suggest that AT does not provide consistent enhance-
ments across all classifiers; its efficacy fluctuates based on
the poisoning method and the foundational online-learning
classifier/framework.
Fig. 2. Accuracies and Poisoning Rates
TABLE V
BESTAT MODELSUNDERPOISONINGATTACKS
Poisoning Attack Best AT Model Rate Accuracy Precision Recall F1
Label FlipSRPClassifier 1.0 0.906 0.902 0.906 0.904
Noise InjectionLeveraging Bagging 1.0 0.936 0.930 0.936 0.933
The AT findings reveal that SRP classifier is the most robust
configuration against label-flip poisoning, whereas the LB is
the most effective against noise-injection poisoning, evaluated
at the peak non-zero poisoning rate (1.0) using the F1 score
(Table V). In addition, the accuracies and across poisoning
rates are depicted in Fig. 2. Graphical illustrations of other
metrics available in the GitHub repository provided above.
B. Drift Detection using EDDM
In this study, we employed several drift detection tech-
niques, including ADWIN and DDM; nevertheless, EDDM
revealed a greater number of drift instances for the mod-
els. With EDDM, drift occurrences were rigorously ana-
lyzed compared to the others that exhibited lesser sensitivity
characteristics for both na ¨ıve and AT models under poisoning
attacks (label flip and noise injection). Besides highlighting
discrepancies in drift detection rates, EDDM’s results showed
overlap between drift events and the consistency of model
classification, at least for noise injection attacks.
Table VI contains the EDDM detections acquired for the
Naive and AT models subjected to LF and NI assaults at
poisoning rates of 0.0, 0.4, and 1.0. The findings indicate
significant discrepancies in the quantity of identified drifts
across different classifiers and kinds of attacks. The Naive-
LB model documented 15, 10, and 0 EDDM detections at
LF rates of 0.4, 1.0, and 0.0, respectively, but its NI setup
yielded 24 detections at a PR of 0.4. The associated AT-LB
model yielded 9 and 0 detections at LF rates of 0.4 and 1.0,
respectively, and 2 detections with NI at 0.4.
Other classifiers demonstrated varying patterns of
EDDM detection. The HT yielded 13 detections for the

TABLE VI
EDDM DRIFTDETECTIONUNDERPOISONINGATTACKS
Classifier Attack Naive-EDDM AT-EDDM
HoeffdingTree label flip 13/13/10 10/10/10
HoeffdingTree noise injection 13/0/13 6/0/0
LeveragingBagging label flip 0/15/10 1/9/0
LeveragingBagging noise injection 0/24/0 3/2/0
SRPClassifier label flip 2/5/7 0/0/2
SRPClassifier noise injection 13/1/0 0/0/0
HoeffdingAdaptiveTree label flip 13/13/10 13/10/6
HoeffdingAdaptiveTree noise injection 13/13/13 0/0/11
AdaptiveRandomForest label flip 13/3/10 16/0/10
AdaptiveRandomForest noise injection 13/0/4 3/13/13
Note:Each triplet represents the number of EDDM detections at poisoning rates 0.0,
0.4, and 1.0, respectively.
TABLE VII
POISONINGATTACKRESULTS ANDDRIFTDETECTION
Model PR Attack Total Drift (EDDM) Overlap
Leveraging Bagging Classifier
Na¨ıve-LB 0.4 NI 24 1
AT-LB 0.4 NI 2 1
AT-LB 0.6 NI 1 1
SRP Classifier
AT-SRP 0.2 NI 1 1
AT-SRP 0.8 NI 1 1
Adaptive Random Forest
AT-ARF 0.8 NI 3 1
Naive-HT model at both 0.0 and 0.4 LF rates, whereas AT-
HT generated 10 detections across all three LF rates.
For HAT, the Naive-HAT reliably yielded 13 detections
amidst NI at all three rates (0.0, 0.4 and 1.0), while the
AT-HAT model recorded 0, 0, and 11 detections, respec-
tively. The ARF exhibited a divergent trend with NI: the
Naive-ARF yielded 13, 0, and 4 detections, whereas the AT-
ARF model resulted in 3, 13, and 13 detections at rates of 0.0,
0.4, and 1.0, respectively. The findings indicate that EDDM
responses fluctuate significantly based on the classifier, the
poisoning mechanism and the PR.
C. Drift-Poison Overlap
To measure the correlation between our proposed poisoning
attack models and identified concept drifts, we investigated
whether EDDM drift occurrences aligned with samples altered
by the poisoning attack, termed drift-poison overlap. Table VII
encapsulates the aggregate count of EDDM-identified drifts
with the tally of drifts that matched with contaminated samples
for chosen noise-injection trials.
No overlap between drift and poison was seen for the label-
flip assaults; hence, these findings are omitted from the table.
Throughout the label-flip trials, the identified drift occurrences
did not align with any contaminated samples. Conversely, little
overlap was seen for some NI attacks. For instance, in the case
of the LB classifier with a poisoning rate of 0.4, one of the 24
EDDM-identified drifts in the Naive-LB model and one of the
two identified drifts in the AT model aligned with a poisoned
sample. An overlap of 1 was similarly seen for the AT-SRP
and AT-ARF models at the specified NI rates.
TABLE VIII
MODELPERFORMANCE FORNOISE-INJECTIONCASESWITH
DRIFT-POISONOVERLAP
Model PR Acc F1 Prec Rec Overlap
Leveraging Bagging
Na¨ıve-LB 0.4 0.607 0.709 0.936 0.607 1
AT-LB 0.4 0.904 0.921 0.952 0.904 1
AT-LB 0.6 0.903 0.921 0.952 0.903 1
SRP Classifier
AT-SRP 0.2 0.950 0.950 0.950 0.950 1
AT-SRP 0.8 0.884 0.908 0.955 0.884 1
Adaptive Random Forest
AT-ARF 0.8 0.938 0.936 0.934 0.938 1
To conduct a more thorough examination of the identified
drift-poison overlap, we assessed the model predictions under
the NI setups where an EDDM-detected drift aligned with
a contaminated sample. Table VIII presents the PR, accuracy,
F1-score, precision, recall, and overlap for these instances. For
LB, at a PR of 0.4, the Na ¨ıve-LB model achieved an accuracy
and recall of 0.607, an F1-score of 0.709, and a precision of
0.936. At the same PR, AT-LB achieved significantly superior
accuracy (0.904), recall (0.904), and F1-score (0.921), while
preserving a precision of 0.952. At a heightened PR of 0.6,
AT-LB demonstrated comparable efficacy, with an accuracy of
0.903 and an F1-score of 0.921.
For the remaining classifiers, AT-SRP attained accuracy,
precision, recall, and F1-score metrics of 0.950 with a PR of
0.2. With a PR of 0.8, the accuracy and recall dropped to
0.884, although precision stayed elevated at 0.955 and the F1-
score remained at 0.908. The AT-ARF, assessed at a PR of 0.8,
attained an accuracy and recall of 0.938, a precision of 0.934,
and an F1-score of 0.936. Significantly, every configuration
shown in the table exhibits a singular overlap count.
Also, whereas these findings delineate model efficacy, par-
ticularly for the noise-injection settings when drift-poison
overlap was seen, they do not inherently confirm that the coin-
ciding poisoning incident caused the associated performance
alterations. Figs. 3 and 4 show the rolling and prequential
accuracies, EDDM drift overlap of the Naive-LB and AT-LB
models for noise injection poison attack at poisoning rate 0.4.
V. DISCUSSION
At the peak PR of 1.0, resilience differed across various
poisoning methods and AT classifiers (Tables IX and X). In
the context of label-flip poisoning, SRP attained the superior
F1-score of 0.904, whereas Leveraging Bagging recorded the
greatest F1-score of 0.933 in scenarios including noise injec-
tion. While SRP had marginally superior accuracy compared to
Leveraging Bagging during noise injection (0.943 vs 0.936),
its F1-score was worse (0.925 versus 0.933). Consequently,
with the F1-score as the principal metric, the findings reveal
variations in AT model efficacy contingent upon the kind of
poisoning attack.
Concept drift denotes the evolving data distribution as time
progresses. Identifying this drift is essential for ML models to
adjust and sustain optimal performance. Various approaches

Fig. 3. Drift Detection for Naive-LB Model
Fig. 4. Drift Detection for AT-LB Model
TABLE IX
AT PERFORMANCEUNDERLABEL-FLIPPOISONING ATRATE1.0
Classifier Acc. F1
Hoeffding Tree 0.058 0.006
Leveraging Bagging 0.543 0.661
SRPClassifier 0.906 0.904
Hoeffding Adaptive Tree 0.703 0.778
Adaptive Random Forest 0.058 0.006
TABLE X
AT PERFORMANCEUNDERNOISEINJECTION ATRATE1.0
Classifier Acc. F1
Hoeffding Tree 0.721 0.793
Leveraging Bagging 0.936 0.933
SRPClassifier 0.943 0.925
Hoeffding Adaptive Tree 0.803 0.848
Adaptive Random Forest 0.942 0.914
have been formulated for drift detection; however, EDDM has
proved very efficient even for our study herein.
Essentially, an observed drift should not be construed as
conclusive proof of a poisoning assault; instead, these findings
delineate the behavior of EDDM in relation to the changing
prediction stream amongst the assessed attack circumstances.
Our findings suggest that EDDM sometimes generates drift
detections that align with some poisoning occurrences; yet, the
frequency of such overlapping events is minimal compared to
the overall count of detected drifts.
In the examined experiments, no clear overlap between drift
and poison was seen for label-flip assaults, indicating that the
identified drift occurrences were not directly associated with
the specific samples whose labels were altered. Since the AT
defense did not consistently mitigate label-flip poisoning, a
more effective AT strategy should be investigated.
VI. CONCLUSION& FUTUREWORK
This study examined the impact of poisoning attacks on
a streaming AutoML pipeline equipped with an AT defense
strategy. It is noteworthy that experiments were conducted
at poisoning rates (PR) of 0.0, 0.2, 0.4, 0.6, 0.8, and 1.0.
However, for compact presentation, we reported the baseline
(0.0), intermediate (0.4), and maximum (1.0) PR. The AT
results reveal that SRP classifier is the most robust config-
uration against label flip poisoning, whereas the LB is the
most effective against noise-injection poisoning, evaluated at
the peak non-zero poisoning rate (1.0) using the F1 score.
While concept drift detection was done using several methods,
EDDM produced more drift detections than the other evaluated
detectors. The findings affirm the effectiveness of adversarial

Fig. 5. EDDM Detections
training and underscore the need for ongoing model monitor-
ing with adaptive drift detection. Finally, drift detectors were
used to detect drift in the naive-LB and AT-LB models. Future
work will include statistical significance testing, comparisons
across repeated runs, and evaluation on additional IoT datasets.
ACKNOWLEDGMENT
This project was made possible in part through the support
of the National Cybersecurity Consortium and the Government
of Canada (CSIN).
REFERENCES
[1] Heitor Murilo Gomes, Jesse Read, Albert Bifet, Jean Paul Barddal,
and Jo ˜ao Gama. Machine learning for streaming data: state of the art,
challenges, and opportunities.ACM SIGKDD Explorations Newsletter,
21(2):6–22, 2019.
[2] Giacomo Ziffer, Alessio Bernardo, Emanuele Della Valle, Vitor
Cerqueira, and Albert Bifet. Towards time-evolving analytics: Online
learning for time-dependent evolving data streams.Data Science, 6(1-
2):1–16, 2023.
[3] Jacob Montiel, Max Halford, Saulo Martiello Mastelini, Geoffrey
Bolmier, Raphael Sourty, Robin Vaysse, Adil Zouitine, Heitor Murilo
Gomes, Jesse Read, Talel Abdessalem, et al. River: machine learning
for streaming data in python.Journal of Machine Learning Research,
22(110):1–8, 2021.
[4] Fabr ´ıcio Ceschin, Marcus Botacin, Albert Bifet, Bernhard Pfahringer,
Luiz S Oliveira, Heitor Murilo Gomes, and Andr ´e Gr ´egio. Machine
learning (in) security: A stream of problems.Digital Threats: Research
and Practice, 5(1):1–32, 2024.
[5] Vanlalruata Hnamte and Jamal Hussain. Dcnnbilstm: An efficient
hybrid deep learning-based intrusion detection system.Telematics and
Informatics Reports, 10:100053, 2023.
[6] Fabrizio Carcillo, Andrea Dal Pozzolo, Yann-A ¨el Le Borgne, Olivier
Caelen, Yannis Mazzer, and Gianluca Bontempi. Scarff : a scalable
framework for streaming credit card fraud detection with spark.Infor-
mation Fusion, 41, 09 2017.
[7] Zhiyi Tian, Lei Cui, Jie Liang, and Shui Yu. A comprehensive survey
on poisoning attacks and countermeasures in machine learning.ACM
Computing Surveys, 55(8):1–35, 2022.
[8] Battista Biggio and Fabio Roli. Wild patterns: Ten years after the rise
of adversarial machine learning. InProceedings of the 2018 ACM
SIGSAC conference on computer and communications security, pages
2154–2156, 2018.
[9] Kshitiz Aryal, Maanak Gupta, and Mahmoud Abdelsalam. Analysis of
label-flip poisoning attack on machine learning based malware detector.
In2022 IEEE International conference on big data (big data), pages
4236–4245. IEEE, 2022.
[10] Tegjyot Singh Sethi and Mehmed Kantardzic. On the reliable detection
of concept drift from streaming unlabeled data.Expert Systems with
Applications, 82:77–99, 2017.
[11] Adrien Chan-Hon-Tong. An algorithm for generating invisible data
poisoning using adversarial noise that breaks image classification deep
learning.Machine Learning and Knowledge Extraction, 1(1):192–204,
2018.
[12] Ehsan Hallaji, Roozbeh Razavi-Far, Mehrdad Saif, and Enrique Herrera-
Viedma. Label noise analysis meets adversarial training: A defense
against label poisoning in federated learning.Knowledge-based systems,
266:110384, 2023.
[13] Battista Biggio, Blaine Nelson, and Pavel Laskov. Poisoning attacks
against support vector machines.arXiv preprint arXiv:1206.6389, 2012.
[14] Rahim Taheri, Reza Javidan, Mohammad Shojafar, Zahra Pooranian,
Ali Miri, and Mauro Conti. On defending against label flipping attacks
on malware detection systems.Neural Computing and Applications,
32(18):14781–14800, 2020.
[15] Fahri Anıl Yerlikaya and S ¸erif Bahtiyar. Data poisoning attacks
against machine learning algorithms.Expert Systems with Applications,
208:118101, 2022.
[16] Gan Sun, Yang Cong, Jiahua Dong, Qiang Wang, Lingjuan Lyu, and
Ji Liu. Data poisoning attacks on federated machine learning.IEEE
Internet of Things Journal, 9(13):11365–11375, 2021.
[17] Thien Duc Nguyen, Phillip Rieger, Markus Miettinen, Ahmad-Reza
Sadeghi, et al. Poisoning attacks on federated learning-based iot
intrusion detection system. InProc. workshop decentralized IoT syst.
secur.(DISS), volume 79, pages 1–7, 2020.
[18] Jie Yang, Jun Zheng, Thar Baker, Shuai Tang, Yu-an Tan, and Quanxin
Zhang. Clean-label poisoning attacks on federated learning for iot.
Expert Systems, 40(5):e13161, 2023.
[19] Nasser Allheeib. Securing machine learning against data poisoning
attacks.International Journal of Data Warehousing and Mining, 20(1),
2024.
[20] Li Yang and Abdallah Shami. Iot data analytics in dynamic environ-
ments: From an automated machine learning perspective.Engineering
Applications of Artificial Intelligence, 116:105366, 2022.
[21] Klim Kireev, Bogdan Kulynych, and Carmela Troncoso. Adversarial
robustness for tabular data through cost and utility awareness.arXiv
preprint arXiv:2208.13058, 2022.
[22] Imtiaz Ullah and Qusay H. Mahmoud. A scheme for generating a dataset
for anomalous activity detection in iot networks. In Cyril Goutte and
Xiaodan Zhu, editors,Advances in Artificial Intelligence, pages 508–
520, Cham, 2020. Springer International Publishing.
[23] Elan Rosenfeld, Ezra Winston, Pradeep Ravikumar, and Zico Kolter.
Certified robustness to label-flipping attacks via randomized smoothing.
InInternational Conference on Machine Learning, pages 8230–8241.
PMLR, 2020.
[24] Ian J Goodfellow, Jonathon Shlens, and Christian Szegedy. Explaining
and harnessing adversarial examples.arXiv preprint arXiv:1412.6572,
2014.
[25] Li Yang, Mirna El Rajab, Abdallah Shami, and Sami Muhaidat. Enabling
automl for zero-touch network security: Use-case driven analysis.IEEE
Transactions on Network and Service Management, 21(3):3555–3582,
2024.
[26] Aleksander Madry, Aleksandar Makelov, Ludwig Schmidt, Dimitris
Tsipras, and Adrian Vladu. Towards deep learning models resistant
to adversarial attacks.arXiv preprint arXiv:1706.06083, 2017.
