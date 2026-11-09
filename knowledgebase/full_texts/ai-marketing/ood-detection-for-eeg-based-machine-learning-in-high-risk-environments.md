---
title: OOD Detection for EEG-based Machine Learning in High-Risk Environments
url: https://arxiv.org/abs/2608.17620
category: ai-marketing
subcategory: measurement
date: 2026-08
venue: ''
authors:
- Philipp Bomatter
- Henry Gouk
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.17620
pages: 37
chars: 82970
fetched_at: '2026-11-08T13:27:27+00:00'
kb_version: 1
---

# OOD Detection for EEG-based Machine Learning in High-Risk Environments

OOD Detection for EEG-based Machine Learning
in High-Risk Environments
Philipp Bomatter1* and Henry Gouk1
1 School of Informatics, University of Edinburgh, United Kingdom.
*Corresponding author(s). E-mail(s): philipp.bomatter@ed.ac.uk;
Contributing authors: henry.gouk@ed.ac.uk;
Abstract
Machine learning models for electroencephalography (EEG) analysis show great
promise across a wide range of applications, but their deployment in high-risk
domains is hindered by their vulnerability to distribution shifts. Encountering
out-of-distribution (OOD) data can lead to catastrophic, overconfident predic-
tive failures. While OOD detection methods can mitigate these risks, they remain
heavily under-explored for EEG. Moreover, evaluations in the broader literature
typically evaluate OOD detection performance in isolation, ignoring their prac-
tical impact on downstream applications. To bridge this gap, we introduce a
benchmark for EEG OOD detection, evaluate a broad range of methods, and
furthermore evaluate their value in two clinical downstream prediction task. Our
results disentangle OOD detection and model uncertainty estimation capabilities,
which are frequently conflated in the literature, provide actionable insights about
the current state of the art for EEG OOD detection and model uncertainty esti-
mation, and demonstrate how complementary methods for both aspects can be
combined to form a robust safety net for the deployment of EEG-based machine
learning models in real-world applications.
Keywords:EEG, OOD Detection, AI Safety, Robustness, Reliability
1 Introduction
Machine learning (ML) provides a promising avenue for supporting and enhancing
the analysis of electroencephalography (EEG). However, especially in high-risk con-
texts like clinical applications, the use of machine learning-based EEG biomarkers is
hindered by their vulnerability to distribution shifts. Machine learning models can
1
arXiv:2608.17620v1  [cs.LG]  18 Aug 2026

fail catastrophically (and with high confidence) when they are presented with data
that differs substantially from the data they were trained on, i.e. out-of-distribution
(OOD) data [1]. Particularly for EEG, there are ample ways in which such shifts can
be introduced, including different recording hardware, (accidental) mismatches in the
preprocessing (e.g. filter settings or re-referencing), or differences in the patient pop-
ulation. While specific quality controls for some of these can be designed, part of the
problem is that there can be unknown shifts that one does not expect. Furthermore,
while for example individual differences between patients can be the cause of distri-
bution shifts [2], only deploying a model for patients that the model has seen during
training is often not an option. In such cases, it may not be clear a priori whether the
EEG data from a new patient is similar enough to the data seen during training.
OOD detection can mitigate these risks by enabling a system to abstain from mak-
ing a prediction or defer to a human expert when a case is likely out of distribution.
Current OOD detection methods can broadly be categorized into two paradigms: dis-
criminative and generative. Approaches such as Maximum Softmax Probability (MSP)
[3], Energy scores [4], Out-of-Distribution Detector for Neural Networks (ODIN) [5],
and Activation Shaping (ASH) [6] directly operate on the activations or outputs of
a (discriminative) classification model. Conversely, methods based on a generative
model—including likelihood estimates, Typicality [7], Density of State Estimation
(DoSE) [8], and Signal in the Noise (SITN) [9]—attempt to explicitly model the
underlying distribution of the training data. While these methods have seen exten-
sive development and benchmarking in domains like computer vision, their application
to EEG data remains heavily under-explored. Furthermore, the standard evaluation
paradigm in the broader OOD detection literature suffers from a significant discon-
nect from clinical utility. The vast majority of existing work evaluates OOD detection
methods strictly in isolation, assessing only how well a method can separate an
in-distribution dataset from a distinctly different out-of-distribution dataset (e.g. sepa-
rating CIF AR-10 images from SVHN images). Crucially, such evaluations fail to reflect
the downstream impact of OOD detection: when deploying a system for clinical diag-
nosis, the ultimate goal is not to merely detect OOD samples, but to understand how
flagging such samples improves the reliability of the diagnosis.
To bridge this gap, this work presents a systematic evaluation of OOD detection for
EEG, explicitly linking detection capabilities to downstream performance in clinical
prediction tasks. We design a suite of practically relevant perturbations with different
levels of severity and use them to benchmark a broad set of OOD detection methods
spanning the aforementioned approaches based on both discriminative and generative
models. In line with a recent theoretical critique and position paper [10, 11], our
results disentangle two fundamentally distinct concepts that are frequently conflated
in the literature: true OOD detection vs model uncertainty. Across perturbations,
methods based on discriminative models were largely incapable of OOD detection,
while methods based on generative models achieved considerably better results, with
increasing performance for higher perturbation severities. However, in downstream
clinical evaluations—where model errors stem from both OOD data and difficult in-
distribution (ID) cases—we find that methods from both paradigms effectively predict
model performance. While generative models recognise unfamiliar data, discriminative
2

methods can serve as a valuable proxy for model uncertainty. Ultimately, we show that
these complementary signals can be combined to form a more robust safety net for
the deployment of EEG-based machine learning models in clinical and other high-risk
applications.
In summary, our main contributions are as follows:
• We present an OOD detection evaluation framework for EEG that closes several
gaps in the field. The framework comprises a suite of perturbations for the
controlled creation of OOD EEG data, as well as investigations of downstream
impacts in two clinically relevant prediction tasks.
• We benchmark a broad range of OOD detection methods, including both dis-
criminative and generative approaches, the latter of which have not previously
been probed in an EEG context, but achieved substantially better performance.
• We present strong empirical evidence that clearly disentangles the often conflated
concepts of OOD detection and model uncertainty, a finding and experimental
setup that is of broader interest to the OOD detection community beyond EEG.
• Our results provide actionable guidance on the current state of the art for EEG
OOD detection and show how it can be combined with uncertainty estimation for
the safer deployment of machine learning models in high-risk EEG applications.
2 Related Work
OOD Detection for EEG-based Machine LearningThe EEG-specific litera-
ture on OOD detection is limited. In a recent preprint, Mulder et al. benchmarked
several discriminative OOD detection methods in a motor imagery setting and found
them to be largely ineffective [12]. Liu et al. proposed a temporal OOD detection
method for EEG-based brain-computer interfaces (BCIs) and compared it against a
range of standard discriminative OOD detection methods [13]. Our study investigates
a more general setting than the latter and is focused on a clinical context rather than
BCIs. Furthermore, while our results largely concur with their findings on discrimi-
native methods, our experiments also include methods based on generative models,
an important addition given that they displayed much better OOD detection capa-
bilities. Concurrent work by Tveter et al. also introduced a range of perturbations
to create EEG data with controlled distribution shifts [14]. However, their work is
focused on the comparison of different ensemble learning methods and their robustness
to distribution shifts rather than OOD detection.
OOD Detection Benchmarks in Other DomainsOutside of EEG, the OOD
detection literature is particularly advanced in computer vision. Notable works that
have focused on the evaluation of different OOD detection methods are the OpenOOD
benchmarks [15, 16], although many methods papers also include comprehensive com-
parisons against other methods [3–6, 8, 9]. Less mature, but more closely related to
EEG, is the field of OOD detection for (more general) time series data. Within this
3

Data
OOD Perturbations
OOD Detection MethodsModels
MSP Energy
ODIN ASH
Likelihood T ypicality
DoSE SITN
OOD Detection
Evaluation
Downstream Performance
train
EEG Labels
abnormal
normal
... ...
abnormal
... ...
test
TUAB
Discriminative Model
TCN
(supervised training)
Generative Model
UNet
(ﬂow matching)
Resampling Channel Shuﬄe Re-referencing
High-pass ﬁlter Low-pass ﬁlter
Fig. 1 OOD Detection Evaluation Concept.Starting from an EEG dataset with annota-
tions for a prediction task (here TUAB with EEG normality labels), the data is first partitioned
into training and test splits. The training data is then used to train two models: a generative model
trained using only the EEG without labels (here a UNet trained via flow-matching), and a discrimi-
native model trained through supervised learning (here a TCN model). The test data then serves as
in-distribution test data, for which corresponding out-of-distribution data is generated through con-
trolled perturbations. Finally, we evaluate a range of OOD detection methods based on either the
generative or discriminative model. In addition to OOD detection performance, we also evaluate its
impact on downstream performance, quantifying how the prediction accuracy of the discriminative
model varies across samples with different OOD scores of the different methods.
field, the OOD detection benchmark for time series data by Gungor et al. is most rel-
evant to our work [17]. However, like EEG-specific prior work, their benchmarks are
limited to discriminative approaches, for which they reported relatively poor perfor-
mance overall. Furthermore, a common thread across all these works is their primary
reliance on semantic shifts to define OOD data, such as reserving a subset of classes
as OOD or evaluating models across disjoint datasets. Guille-Escuret et al. recently
criticised these approaches, arguing that an exclusive focus on semantic shifts neglects
relevant (covariate) distribution shifts encountered by real-world systems [18]. Moti-
vated by a practical perspective, we see the value of OOD detection in protecting
against model failure, irrespective of the nature of the shift. Our work is therefore
closely aligned with this view. Our work is also different in that we go beyond stan-
dard OOD detection evaluations to study impacts on downstream clinical applications
and disentangle the concepts of true OOD detection and model uncertainty.
3 Methods
Figure 1 provides an overview of the components that enable our EEG OOD detection
evaluations. Starting from an EEG dataset with corresponding annotations for a (clin-
ical) prediction task, samples are first partitioned into a training and test split. The
training data is used to train two models: a generative model trained using only the
EEG without labels (i.e. unsupervised), and a discriminative model trained through
supervised learning. The test set then serves as in-distribution test data, for which
we generate corresponding out-of-distribution data through controlled perturbations.
Finally, we evaluate a range of OOD detection methods based on either the generative
4

or discriminative model in two ways. First, we assess their OOD detection perfor-
mance, i.e. how well their assigned OOD scores discriminate between the unperturbed
ID test samples and their corresponding perturbed OOD versions. Second, we also
evaluate the impact of OOD detection on downstream performance in the (clinical)
prediction task, quantifying how the prediction accuracy of the discriminative model
varies across samples with different OOD scores of the different methods.
Detailed descriptions for the different components are given in the following
sections. We start with the EEG perturbation suite that forms the backbone of our
benchmarks in Section 3.1. Section 3.2 then outlines the different OOD detection meth-
ods included in our benchmarks along with architecture and training details for the
underlying models. Information about the datasets, prediction tasks, data splitting,
and preprocessing is provided in Section 3.3.
3.1 OOD Perturbation Suite for EEG
We introduce a suite of controlled perturbations to create OOD samples from in-
distribution test data. These transformations were designed to simulate plausible
distribution shifts that may be encountered in real-world EEG data, though they are
fundamentally intended to serve as a structured, reproducible, and well-controlled
testbed rather than an exhaustive modelling of reality. Furthermore, the perturbations
were designed to be parametrisable, which (with the exception of the re-referencing
perturbation) enables fine-grained control of the severity of the distribution shift.
Finally, by applying these transformations directly to the ID test set, the resulting
OOD data is perfectly paired with the unperturbed baseline, providing the method-
ological capacity to isolate the exact effect of a shift on model performance. The
perturbations are illustrated in Figure 2 and described in the following paragraphs.
Sampling RateThe signal is resampled to a higher sampling rate (using bandlim-
ited sinc interpolation via the torchaudio library) and then cropped to maintain the
same number of samples. From the perspective of a model that expects data to be at
a lower sampling rate, perturbed samples will appear smoothed. Sampling rate mis-
matches are surprisingly common in practice; for instance, a common issue in the
evaluation of EEG foundation models is that they are applied to data with a different
sampling rate than the model was pre-trained on. We control the severity of this per-
turbation by varying the amount by which the sampling rate is increased compared to
the 100 Hz that the model was trained on, ranging from 125 Hz over 150 Hz to 200 Hz.
Channel OrderThe ordering of a subset of EEG channels is permuted. From the
perspective of a model that was trained with a fixed given channel order, the pertur-
bation will lead to strange topographies with, for example, eye blinks appearing in
presumed occipital channels. In practice, perturbations like this could be introduced
by accident with some recording devices where electrodes are plugged into the ampli-
fier individually. We control the severity of this perturbation by varying the size of the
subset of randomly selected channels which are permuted. We increase the subset from
10%, i.e. swapping just two channels in the 19-channel layout, to 50% and then 100%.
Reference SchemeThe EEG channels are re-referenced to a different scheme.
Starting from average-referenced data that is used to train the model, we re-reference
5

0.0 0.5 1.0 1.5
Time (s)
Fp1
Fp2
F3
F4
Cz
O1
O2
Original
(unperturbed)
0.0 0.5 1.0 1.5
Time (s)
Resampling
(150 Hz)
0.0 0.5 1.0 1.5
Time (s)
Channel Shuffle
(50%)
0.0 0.5 1.0 1.5
Time (s)
Fp1
Fp2
F3
F4
Cz
O1
O2
Re-reference
(Cz)
0.0 0.5 1.0 1.5
Time (s)
High-pass Filter
(8 Hz)
0.0 0.5 1.0 1.5
Time (s)
Low-pass Filter
(15 Hz)
Fig. 2 Illustration of EEG OOD Perturbations.An unperturbed (ID) EEG segment is shown
(top left panel) along with corresponding OOD samples obtained through the different perturbations.
For visualisation purposes, only a subset of channels are shown.
to three different schemes: a monopolar vertex reference with Cz as the reference chan-
nel, a linked-temporal reference with the average of T7 and T8 as the reference, and
a longitudinal double-banana bipolar montage with an additional transverse channel
(T7-T8) to maintain the same channel count. Unlike the different levels for other per-
turbations, these three options do not have a clear ordering in terms of perturbation
severity.
High-pass FilterThe signal is filtered with an additional zero-phase Butterworth
high-pass filter, attenuating low-frequency content. Starting from the unperturbed
data (high-pass filtered at 1 Hz), we vary the severity of this perturbation by increasing
the cutoff frequency starting from 2 Hz to 4 Hz and 8 Hz, progressively removing more
low-frequency activity.
Low-pass FilterAnalogous to the high-pass filter perturbation described above,
the signal is filtered with a low-pass filter. Starting from the unperturbed data (low-
pass filtered at 50 Hz), we vary the severity of this perturbation by lowering the
cutoff frequency starting from 45 Hz to 30 Hz and 15 Hz, progressively removing more
high-frequency activity.
3.2 OOD Detection Methods
Our benchmarks include popular OOD detection methods grouped into two
paradigms: methods based directly on discriminative classification models and meth-
ods based on generative models.
6

3.2.1 Discriminative-model-based Methods
In the following, we outline the OOD detection methods included in our benchmarks
that are directly based on the discriminative model used for the given classification
task. As the underlying discriminative model for all methods, we use the TCN archi-
tecture originally proposed by Bai et al. [19], which has since been adapted and widely
used for EEG data [20] (see Appendix E for hyperparameters and training details).
Maximum Softmax Probability (MSP)MSP uses the maximum probability
from the network’s final softmax layer as a confidence score [3]. This is based on the
assumption that the model will output lower maximum probabilities (reflecting higher
uncertainty) when presented with OOD data compared to ID data.
Energy ScoreInstead of operating on the softmax outputs, which are normalised
to sum to one, Liu et al. proposed computing an energy score directly from the model’s
unnormalised logits [4]. OOD samples are expected to produce higher energy scores.
Out-of-Distribution Detector for Neural Networks (ODIN)ODIN builds
upon the standard MSP approach through two key modifications: applying temper-
ature scaling to the model’s logits prior to the softmax computation, and adding
gradient-based perturbations to the input data that are expected to have a stronger
impact on ID than OOD data [5]. Together, these modifications aim to improve
the separability of ID and OOD samples with the resulting score. We adopt the
hyperparamters reported in the original publication for the main results (T=1000,
ϵ=0.0014). We did not perform hyperparameter tuning because we do not assume
access to OOD data in our experiments. Furthermore, the original publication suggests
relatively good hyperparameter transferability.
Activation Shaping (ASH)Djurisic et al. introduced an activation shaping (ASH)
method that intervenes in the forward pass of a model by pruning and transforming
activations before they reach the final classification head, after which the energy score
is computed on the resulting logits [6]. We specifically use the ASH-S version with a
pruning percentage of 65%. While tuning of this hyperparameter would require access
to OOD data, which we do not assume in our benchmarks, the authors report relatively
stable performance across different parameter values in the original publication.
3.2.2 Generative-model-based Methods
In the following, we outline the OOD detection methods included in our benchmarks
that are based on a generative model. As the underlying generative model for all meth-
ods, we use the UNet architecture following Ho et al. [21], as implemented by Dhariwal
and Nichol [22], and train it using the flow matching objective by Lipman et al. [23]
(see Appendix E for details). We use Euler’s method (with 100 timesteps), imple-
mented in the library by Lipman et al. [24], as ODE solver to obtain the likelihoods
and noise samples required by the different methods.
Log-likelihoodThe log-likelihood is evaluated via the instantaneous change of vari-
ables formula, calculated as the sum of the log-probability of the latent representation
7

and the negative integral of the vector field’s divergence over the flow trajectory. Sam-
ples with low likelihood under the generative model are flagged as OOD, reflecting the
assumption that the model assigns higher probability densities to ID data.
TypicalityTypicality was introduced by Nalisnick et al. to correct for a failure
mode of likelihoods in high dimensions where regions of high probabilitydensitycan
lie outside of the so-called typical set that contains almost all probabilitymass[7].
It is defined as the absolute difference between the negative log-likelihood and an
estimate of the entropy. We estimate the entropy as the average negative log-likelihood
over the (in-distribution) validation data, following experiments in [9] that showed
negligible differences to estimation on the training data as in the original publication.
Furthermore, we use the single-sample version as in [8].
Density of State Estimation (DoSE)DoSE measures the empirical density of
multiple statistics computed on in-distribution data (as for Typicality, we use (in-
distribution) validation data following experiments in [9]) [8]. We specifically use the
DoSEKDE version for flow-based models, which is based on three statistics: the log-
likelihood, the log-probability of the latent representation, and the log-determinant
of the Jacobian (corresponding to the integral of the vector field’s divergence for the
continuous-time flow matching model used in our experiments). A 1D Kernel Density
Estimator (KDE) is fit to each statistic and the final OOD score is computed by sum-
ming the log-probabilities from the individual KDEs. As in the original publication,
the default SciPy KDE implementation with a Gaussian kernel and automatic deter-
mination of the bandwidth parameter through Scott’s rule is used, and following [9],
the KDEs are fit on a random subset of 10,000 samples for computational efficiency.
Signal in the Noise (SITN)SITN uses the diffeomorphic properties of continuous
normalising flows to detect OOD samples by checking if their corresponding noise
samples (obtained through backwards integration along the probability flow ODE) are
consistent with the Gaussian prior used during training [9].
3.3 Data
Experiments were conducted on two large datasets (TUAB, CAUEEG) with anno-
tations for clinical prediction tasks. With more than 1,000 participants each, these
datasets are among the largest EEG datasets available for research purposes, provid-
ing us with the necessary sample size for robust training and benchmarking of machine
learning methods.
TUABThe Temple University Hospital Abnormal (TUAB) EEG Corpus [25, 26]
comprises a demographically balanced and curated subset of more than 2,300 par-
ticipants from the TUH EEG Corpus [27]. The data was collected in a hospital
environment and recordings were annotated by board certified neurologists for the
normality of the EEG according to standardised criteria [28]. We specifically used ver-
sion 3.0.1 of the dataset and followed the data curation and splitting in [2], which
respects the official train-test split and additionally defines a validation split with 10%
of the training data. All splitting is performed on the participant level, i.e. all samples
of a given participant are assigned to the same split. Data access requests should be
directed to the dataset authors.
8

CAUEEGThe Chung-Ang University Hospital EEG (CAUEEG) dataset [29]
includes a subset of 1,122 participants to which diagnostic labels for the categories
normal, mild cognitive impairment (MCI), or dementia were assigned by neurologists
based on a neuropsychological examination. We used the official train-validation-test
split without overlapping participants. Data access for academic and research purposes
can be requested from the dataset authors.
PreprocessingThe data preprocessing comprised the following steps: selection of
a fixed channel subset (the 19 channels in the 10-20 system), band-pass filtering to
1-50 Hz, resampling to 100 Hz, and re-referencing to average reference. Finally, non-
overlapping epochs with 2s duration were used.
4 Results
4.1 OOD Detection Performance
Table 1 shows the Area Under the Receiver Operating Characteristic (AUROC) curve
for the OOD detection performance across the different perturbations and severity lev-
els for all methods on the TUAB dataset. Models for the discriminative and generative
methods were trained on the train split of the (unperturbed) dataset and OOD detec-
tion methods were then evaluated by using the unperturbed test split of the dataset
as ID samples and the perturbed test data as OOD samples.
T able 1 OOD detection performance on TUAB.Performance is reported in terms of
AUROC and bold values highlight the best result for each perturbation and severity level.
Discriminative-model-based methods (MSP, Energy, ODIN, ASH) perform largely at chance level,
whereas generative-model-based methods achieve considerably better OOD detection with
increasing performance for higher severity levels. SITN consistently achieves the best performance.
Perturbation Severity MSP Energy ODIN ASH LL Typ. DoSE SITN
Resampling
125 Hz 0.517 0.500 0.514 0.533 0.369 0.559 0.5560.947
150 Hz 0.457 0.479 0.453 0.534 0.275 0.646 0.6470.981
200 Hz 0.383 0.451 0.377 0.522 0.143 0.816 0.8260.989
Channel Shuffle
10% 0.549 0.494 0.549 0.513 0.607 0.521 0.5430.754
50% 0.553 0.431 0.555 0.494 0.793 0.682 0.7110.924
100% 0.526 0.391 0.529 0.460 0.823 0.726 0.7480.942
Re-referencing
Cz 0.517 0.435 0.520 0.597 0.950 0.937 0.9870.998
T7, T8 0.587 0.513 0.591 0.568 0.927 0.896 0.9730.997
bipolar 0.752 0.621 0.757 0.719 0.940 0.919 0.9620.996
High-pass Filter
2 Hz 0.514 0.558 0.511 0.506 0.475 0.504 0.5030.604
4 Hz 0.531 0.603 0.526 0.550 0.445 0.510 0.5100.749
8 Hz 0.446 0.684 0.439 0.637 0.367 0.546 0.5440.872
Low-pass Filter
45 Hz 0.499 0.502 0.499 0.503 0.461 0.507 0.5050.822
30 Hz 0.500 0.511 0.498 0.515 0.246 0.649 0.6440.986
15 Hz 0.511 0.536 0.506 0.560 0.016 0.975 0.9740.990
9

OOD detection methods operating on discriminative models that were trained in
a supervised way on the normality prediction task (MSP, Energy, ODIN, ASH) were
largely ineffective for differentiating between in- and out-of-distribution data. These
methods performed close to chance level (AUROC of 0.5) for most conditions and
showed inconsistent trends with perturbation severity. Energy scores, for instance,
showed increasingly better OOD detection performance with higher severities of the
high-pass filter perturbation, but decreasing performance for increasing severities of
the resampling perturbation.
Generative models (in particular Typicality, DoSE, and SITN), on the other hand,
achieved much better OOD detection overall with consistent severity-dependent per-
formance improvements. SITN clearly emerged as the most effective OOD detection
method with strong performance even at the lowest severity level and for pertur-
bations where other methods performed close to chance level (see for example the
channel shuffle perturbation at the lowest severity level where only two channels are
flipped). Raw log-likelihoods worked well for certain perturbations (Channel Shuffle,
Re-referencing), but not others, exhibiting a behaviour previously observed in the
computer vision literature, which we discuss in more detail in Appendix D.
Evaluations on CAUEEG corroborate these results, except that DoSE narrowly
outperformed SITN for the Re-referencing perturbation and the highest severity Low-
pass Filter setting (see Appendix A). Additional results for Mahalanobis distances can
be found in Appendix B.
4.2 Downstream Performance Impact
Panel A in Figure 3 shows the impact of OOD detection on the clinical downstream
EEG normality prediction task on the TUAB dataset (see Section 3.3). The figure
shows one method from each paradigm (MSP as a discriminative method and SITN as
a generative method) where the resampling perturbation (severity 200 Hz) was used
for the OOD data. For each method, the pooled in- and out-of-distribution samples
were sorted according to the assigned OOD scores. Then we report the (downstream)
classification accuracy of the discriminative model across different percentile bins of
the OOD score (e.g. the performance across the samples with the lowest 0.1% MSP
scores, the 0.1-1% lowest MSP scores, etc.). The arrows in the top left/right corners
of the plots indicate the OOD direction for each method: for MSP, OOD samples
are expected to have lower scores, whereas SITN should assign higher scores to OOD
samples. Finally, the histograms show the sample counts in each percentile bin with
the different colours indicating the proportion of ID and OOD samples.
For MSP, the proportion of ID and OOD samples is relatively similar across the
bins, consistent with the poor OOD detection AUROC values reported in Section 4.1.
MSP does not separate ID and OOD samples well. Despite this fact, MSP values are
still predictive of model performance, except for a failure mode at very high confidence
values. SITN, on the other hand, separates ID and OOD samples extremely well. It
can be seen that the model performance is substantially lower on OOD data, dropping
almost to chance level, such that OOD detection provides a very valuable safety net
to prevent misclassifications.
10

0.1
1
5
10
25
50
75
90
95
99
99.9
100
MSP Percentile Bin Upper Edge
0
25k
50k
75kSample Count
371 401
OOD
0.1
1
5
10
25
50
75
90
95
99
99.9
100
SITN Percentile Bin Upper Edge
370 372
OOD
53 50 51 53 57
66 71 74 81 85 85
47
0
50
100
Accuracy (%)
80 82 81 80 81 80
57 52 51 55 55 56
A ID OOD Accuracy Average Accuracy (67.5%)
0.1
1
5
10
25
50
75
90
95
99
99.9
100
MSP Percentile Bin Upper Edge
0
20k
40kSample Count
186 196
0.1
1
5
10
25
50
75
90
95
99
99.9
100
SITN Percentile Bin Upper Edge
186 186
49 49 53 57
65
78
87 94 98 99 96
48
0
50
100
Accuracy (%)
83 81 80 81 81 81 81 80 82 79
55 58
B Count Accuracy Average Accuracy (80.5%)
Fig. 3 Model performance for pathology prediction on the TUAB dataset. AID samples
and corresponding OOD samples obtained with the resampling perturbation (severity 200 Hz). Per-
formance is shown in terms of accuracy across percentile bins, where the x ticks indicate the upper
edge of the corresponding bin (i.e. the first bin contains samples from the 0-0.1 percentile, the sec-
ond one 0.1-1, etc.). The histograms indicate the number of ID and OOD samples in each bin. The
arrows in the top left/right of each plot indicate the OOD direction for the corresponding metric.
See Appendix H for full downstream performance results across all perturbations and OOD detection
methods.BThe same visualisations restricted to only in-distribution data. MSP is a good indicator
of model performance across in-distribution samples except for a failure mode at the highest MSP
scores, whereas SITN provides little information about model performance between ID samples.
In Panel B, we present the same visualisations on ID data (i.e. the unperturbed
test data) alone. It can be seen that MSP scores are much more predictive of model
performance than SITN scores within ID samples. Generative approaches like SITN,
which do not have access to the discriminative model used for the classification task,
provide little indication for model performance within the majority of in-distribution
samples, but they do not have the aforementioned failure mode of discriminative meth-
ods at very high confidence levels. A performance drop can be observed for ID samples
with the most extreme (top 1%) SITN scores. These samples likely represent rare
in-distribution samples to which the model had very low exposure during training.
Full results for all perturbations and OOD detection methods as well as evaluations
on the dementia diagnosis task on CAUEEG can be found in Appendix H. While the
11

Sample OOD Detector
OOD
ID
abstain / defer to human
Model
Uncertainty
high uncertainty
predict
low uncertainty
Fig. 4 Decision Diagram for Combined OOD and Uncertainty Detection.Samples are
jointly probed by an OOD detector and a model uncertainty estimator, each of which can trigger the
system to abstain from prediction or defer to a human expert to prevent misclassifications.
effect on downstream performance was smaller for certain conditions (e.g. Low-pass
Filter on CAUEEG; Figure H17), the general patterns are highly consistent.
Overall, these results clearly disentangle two aspects that influence downstream
performance. Generative methods like SITN excel at true OOD detection, identifying
samples outside the training distribution, for which model predictions should not be
trusted because the model was not exposed to comparable data during training. Dis-
criminative methods like MSP, on the other hand, are not suitable for OOD detection,
but reflect model uncertainty. Even with ample exposure to similar samples during
training, certain cases can be ambiguous and difficult for the model to classify. Model
uncertainty can capture such cases and provide valuable information about how well
the model is likely to perform across different in-distribution samples.
4.3 Combination of OOD Detection and Model Uncertainty
The results in Section 4.2 suggest that it could be extremely useful to combine
OOD detection and model uncertainty methods. OOD detection methods can provide
protection against highly confident mispredictions when the model encounters out-of-
distribution samples, while model uncertainty methods function well for in-distribution
data, where they provide valuable estimates of the model performance.
We evaluated a system following the decision diagram in Figure 4, where sam-
ples are assessed by both an OOD detector and a model uncertainty estimator. The
classifier then only provides predictions for samples that pass both tests and abstains
from prediction otherwise. We used SITN for OOD detection, following the calibration
procedure detailed in the original publication [9], which allows one to pick a thresh-
old with access to only an in-distribution validation set based on an acceptable false
positive rate (FPR). A target FPR of 1% was chosen for this example. To control
model uncertainty, we first used isotonic regression (fitted on the in-distribution val-
idation set) to map raw MSP values to calibrated probabilities. We then thresholded
samples as too uncertain if the calibrated probability of the prediction being correct
was below 60%. The choice of this threshold will in practice depend on the costs of
misclassifications vs abstaining from prediction or deferring to a human expert.
Results on TUAB are shown in Table 2. Focusing on the baseline performance
without any rejections (coverage 100%) first, it can be seen that the accuracy dropped
12

from 80.5% on ID data to 67.5% when corresponding OOD samples (resampling per-
turbation at 200 Hz) were included in the evaluation. When SITN was used to reject
OOD samples, performance remained stable across both conditions. Note also that,
as expected, the coverage on ID data is close to the desired 1% FPR. Using MSP to
reject high uncertainty samples improved performance on ID data (at the cost of a
lower coverage). When OOD samples were included in the evaluation, MSP did not
protect well against the drop in performance, with only marginally better accuracy
than the baseline despite rejecting more than 10% of the samples. Combining the two
methods resulted in the best accuracy across both conditions.
T able 2 Selective Classification Performance for OOD Detection and
Model Uncertainty Estimation.OOD Detection (using SITN), Model
Uncertainty (using MSP), and their combination (SITN+MSP) are compared on
ID-only data and ID+OOD data. OOD data was generated with the resampling
perturbation at 200 Hz. MSP provides an accuracy improvement on
in-distribution data, but only SITN provides effective protection against OOD
data. Combining both methods enables the highest accuracy across both in- and
out-of-distribution data.
ID Only ID and OOD
Rejection Method Coverage Accuracy Coverage Accuracy
Baseline (No Rejection) 100.0% 80.5% 100.0% 67.5%
SITN (OOD Detection) 98.5% 80.8% 49.5% 80.7%
MSP (Model Uncertainty) 88.1% 83.8% 89.2% 69.3%
Combined (SITN + MSP) 86.9% 84.1% 43.7% 84.1%
5 Discussion and Conclusions
In this study, we introduced an OOD detection benchmark for EEG-based machine
learning and systematically evaluated a broad spectrum of both discriminative and
generative methods. Our results clearly demonstrate that standard discriminative
methods are incapable of reliably detecting OOD EEG data under realistic covariate
shifts, a finding that aligns with limited prior work in the EEG BCI literature [12, 13].
However, generative approaches—which to the best of our knowledge have not been
previously benchmarked for EEG or general time-series OOD detection—yield sub-
stantially better performance. In particular, Signal in the Noise (SITN) establishes a
new state of the art for EEG OOD detection.
Follow-up evaluations to assess the utility of OOD detection in two clinical
downstream prediction tasks demonstrated two things. First, performance dropped
substantially on out-of-distribution samples, emphasising the value of OOD detec-
tion to prevent mispredictions in high-risk applications. Second, both discriminative
and generative methods were predictive of downstream performance, but for differ-
ent reasons. Only generative methods protect against model failure by flagging OOD
samples. Discriminative methods prevent mispredictions by highlighting samples with
high model uncertainty, even if they are in-distribution. These results provide strong
13

support for the position recently put forward by Li et al., which argues that discrimi-
native methods “answer the wrong question for OOD detection”[10]. We furthermore
demonstrated how the complementary capabilities of discriminative and generative
methods can be combined to protect against both failure modes.
The present study has some limitations that highlight valuable directions for future
work. While the creation of OOD data through the perturbations presented in this
work has several advantages (unambiguous ground truth, perfect pairing with ID
samples, large sample size, control of severity levels), the field would benefit from addi-
tional benchmarks and curated datasets to study a wider variety of distribution shifts.
Designing such OOD detection setups is more challenging than in computer vision.
While images from different datasets (e.g. CIF AR-10 vs SVHN) or different object
categories (e.g. cats vs cars) are clearly distinct, comparing EEG segments across dif-
ferent datasets is more nuanced. Besides clear differences in recording hardware or
preprocessing, aspects of which are already reflected in our perturbation experiments,
the degree to which differences in patient populations manifest in EEG distribution
shifts is hard to quantify. Even for comparatively well-studied variables like sex or
age with known population-level differences [30–32], a lot of the variance is driven by
individual differences. Moreover, cross-dataset label definitions are often not mutually
exclusive. EEG segments in the TUAB dataset could in principle also be assigned a
simultaneous label for the dementia diagnosis task in CAUEEG, such that CAUEEG
segments need not necessarily be OOD for a TUAB-trained model (see exploratory
analysis in Appendix F). Where possible, we recommend grounding OOD detection
through simultaneous assessments of performance in a relevant downstream task as
in our experiments. This ensures that progress in OOD detection will translate to
superior safeguards in practical applications.
Our results also raise questions about benchmarking practices in the broader OOD
detection literature. How can the poor performance of discriminative methods in our
evaluations be reconciled with their success on widely used computer vision bench-
marks like OpenOOD? We hypothesise that this discrepancy stems from fundamental
differences in how OOD evaluation is framed. For one, established leaderboards fre-
quently permit the use of auxiliary OOD data during training. Our setup, by contrast,
strictly assumes no prior access to OOD data, reflecting a more realistic scenario
where models encounter completely unanticipated shifts. Furthermore, OOD detec-
tion benchmarks are dominated by semantic shifts [18]. An influential survey paper by
Yang et al. even frames this exclusive focus as part of the general definition of OOD
detection, although it is acknowledged that other shifts may be considered OOD from a
generalisation perspective or when considering high-risk applications [33]. We encour-
age future applied work to place practical utility at its centre. In clinical domains, the
primary objective of OOD detection is to prevent model failure caused by unantic-
ipated distribution shifts. Crucially, achieving this requires benchmarks designed to
prevent the entanglement of true OOD detection and model uncertainty. As our results
suggest, these are fundamentally distinct capabilities and conflating the two obscures
what a given method actually achieves. By designing benchmarks that explicitly sep-
arate OOD detection from model uncertainty estimation, the field can make targeted
progress on both fronts.
14

Acknowledgements.This project was supported by the Royal Academy of Engi-
neering under the Research Fellowship programme.
References
[1] Nguyen, A.M., Yosinski, J., Clune, J.: Deep neural networks are easily fooled:
High confidence predictions for unrecognizable images. In: IEEE Conference on
Computer Vision and Pattern Recognition, CVPR 2015, Boston, MA, USA, June
7-12, 2015, pp. 427–436 (2015). https://doi.org/10.1109/CVPR.2015.7298640
[2] Bomatter, P., Gouk, H.: Is Limited Participant Diversity Impeding EEG-based
Machine Learning? In: Proc. of NeurIPS, vol. 38, pp. 117447–117474 (2025)
[3] Hendrycks, D., Gimpel, K.: A baseline for detecting misclassified and out-of-
distribution examples in neural networks. In: Proc. of ICLR (2017)
[4] Liu, W., Wang, X., Owens, J.D., Li, Y.: Energy-based out-of-distribution
detection. In: Proc. of NeurIPS (2020)
[5] Liang, S., Li, Y., Srikant, R.: Enhancing the reliability of out-of-distribution image
detection in neural networks. In: Proc. of ICLR (2018)
[6] Djurisic, A., Bozanic, N., Ashok, A., Liu, R.: Extremely simple activation shaping
for out-of-distribution detection. In: Proc. of ICLR (2023)
[7] Nalisnick, E., Matsukawa, A., Teh, Y.W., Lakshminarayanan, B.: Detecting
Out-of-Distribution Inputs to Deep Generative Models Using Typicality. ArXiv
preprint abs/1906.02994 (2019)
[8] Morningstar, W.R., Ham, C., Gallagher, A.G., Lakshminarayanan, B., Alemi,
A.A., Dillon, J.V.: Density of states estimation for out of distribution detection.
In: The 24th International Conference on Artificial Intelligence and Statis-
tics, AISTATS 2021, April 13-15, 2021, Virtual Event. Proceedings of Machine
Learning Research, vol. 130, pp. 3232–3240 (2021)
[9] Bomatter, P., Geary, J., Gouk, H.: The Signal in the Noise: OOD Detection
Through Goodness-of-Fit Testing in Factorised Latent Spaces. ArXiv preprint
abs/2605.22496 (2026)
[10] Li, Y.L., Lu, D., Kirichenko, P., Qiu, S., Rudner, T.G.J., Bruss, C.B., Wilson,
A.G.: Position: Supervised Classifiers Answer the Wrong Questions for OOD
Detection. In: Proceedings of the 42nd International Conference on Machine
Learning, pp. 81689–81713 (2025)
[11] Li, Y.L., Lu, D., Kirichenko, P., Qiu, S., Rudner, T.G.J., Bruss, C.B., Wil-
son, A.G.: Out-of-Distribution Detection Methods Answer the Wrong Questions.
ArXiv preprint abs/2507.01831 (2025)
15

[12] Mulder, M.Q., Valdenegro-Toro, M., Sburlea, A.I., Jong, I.P.d.: The Chal-
lenge of Out-Of-Distribution Detection in Motor Imagery BCIs. ArXiv preprint
abs/2603.13324 (2026)
[13] Liu, C., Li, S., Tan, L., Wu, D.: Temporal Out-of-Distribution Detection
for Asynchronous Motor Imagery Brain-Computer Interfaces. ArXiv preprint
abs/2605.01014 (2026)
[14] Tveter, M., Tveitstøl, T., Hatlestad-Hall, C., Hammer, H.L., Haraldsen, I.R.J.H.:
Uncertainty in deep learning for EEG under dataset shifts. Artificial Intelligence
in Medicine174, 103374 (2026) https://doi.org/10.1016/j.artmed.2026.103374
[15] Yang, J., Wang, P., Zou, D., Zhou, Z., Ding, K., Peng, W., Wang, H., Chen, G.,
Li, B., Sun, Y., Du, X., Zhou, K., Zhang, W., Hendrycks, D., Li, Y., Liu, Z.:
Openood: Benchmarking generalized out-of-distribution detection. In: Proc. of
NeurIPS (2022)
[16] Zhang, J., Yang, J., Wang, P., Wang, H., Lin, Y., Zhang, H., Sun, Y., Du, X., Li,
Y., Liu, Z., Chen, Y., Li, H.: OpenOOD v1.5: Enhanced Benchmark for Out-of-
Distribution Detection. ArXiv preprint abs/2306.09301 (2023)
[17] Gungor, O., Rios, A.S., Ahuja, N., Rosing, T.: TS-OOD: Evaluating Time-Series
Out-of-Distribution Detection and Prospective Directions for Progress. ArXiv
preprint abs/2502.15901 (2025)
[18] Guille-Escuret, C., No¨ el, P., Mitliagkas, I., V´ azquez, D., Monteiro, J.: Expecting
the unexpected: Towards broad out-of-distribution detection. In: Proc. of NeurIPS
(2024)
[19] Bai, S., Kolter, J.Z., Koltun, V.: An Empirical Evaluation of Generic Con-
volutional and Recurrent Networks for Sequence Modeling. ArXiv preprint
abs/1803.01271 (2018)
[20] Gemein, L.A.W., Schirrmeister, R.T., Chrabaszcz, P., Wilson, D., Boedecker, J.,
Schulze-Bonhage, A., Hutter, F., Ball, T.: Machine-learning-based diagnostics
of EEG pathology. NeuroImage220, 117021 (2020) https://doi.org/10.1016/j.
neuroimage.2020.117021
[21] Ho, J., Jain, A., Abbeel, P.: Denoising diffusion probabilistic models. In: Proc. of
NeurIPS (2020)
[22] Dhariwal, P., Nichol, A.Q.: Diffusion models beat gans on image synthesis. In:
Proc. of NeurIPS, pp. 8780–8794 (2021)
[23] Lipman, Y., Chen, R.T.Q., Ben-Hamu, H., Nickel, M., Le, M.: Flow matching for
generative modeling. In: Proc. of ICLR (2023)
16

[24] Lipman, Y., Havasi, M., Holderrieth, P., Shaul, N., Le, M., Karrer, B., Chen,
R.T.Q., Lopez-Paz, D., Ben-Hamu, H., Gat, I.: Flow Matching Guide and Code.
ArXiv preprint abs/2412.06264 (2024)
[25] L´ opez, S., Suarez, G., Jungreis, D., Obeid, I., Picone, J.: Automated Identifica-
tion of Abnormal Adult EEGs. IEEE Signal Processing in Medicine and Biology
Symposium (SPMB)2015(2015) https://doi.org/10.1109/SPMB.2015.7405423
[26] Diego, L.d., Isabel, S.: Automated Interpretation of Abnormal Adult Electroen-
cephalograms (2017)
[27] Obeid, I., Picone, J.: The Temple University Hospital EEG Data Corpus.
Frontiers in Neuroscience10(2016) https://doi.org/10.3389/fnins.2016.00196
[28] Rubin, D.I.: Clinical Neurophysiology, 5th ed edn. Contemporary Neurology Ser,
(2021)
[29] Kim, M.-j., Youn, Y.C., Paik, J.: Deep learning-based EEG analysis to classify
normal, mild cognitive impairment, and dementia: Algorithms and dataset. Neu-
roImage272, 120054 (2023) https://doi.org/10.1016/j.neuroimage.2023.120054
[30] Aurlien, H., Gjerde, I.O., Aarseth, J.H., Eldøen, G., Karlsen, B., Skeidsvoll,
H., Gilhus, N.E.: EEG background activity described by a large computerized
database. Clinical Neurophysiology115(3), 665–673 (2004) https://doi.org/10.
1016/j.clinph.2003.10.019
[31] Chiang, A.K.I., Rennie, C.J., Robinson, P.A., Albada, S.J., Kerr, C.C.: Age trends
and sex differences of alpha rhythms including split alpha peaks. Clinical Neu-
rophysiology122(8), 1505–1517 (2011) https://doi.org/10.1016/j.clinph.2011.01.
040
[32] Cellier, D., Riddle, J., Petersen, I., Hwang, K.: The development of theta and
alpha neural oscillations from ages 3 to 24 years. Developmental Cognitive
Neuroscience50, 100969 (2021) https://doi.org/10.1016/j.dcn.2021.100969
[33] Yang, J., Zhou, K., Li, Y., Liu, Z.: Generalized Out-of-Distribution Detection:
A Survey. International Journal of Computer Vision132(12), 5635–5662 (2024)
https://doi.org/10.1007/s11263-024-02117-4
[34] Lee, K., Lee, K., Lee, H., Shin, J.: A simple unified framework for detecting out-of-
distribution samples and adversarial attacks. In: Proc. of NeurIPS, pp. 7167–7177
(2018)
[35] Nalisnick, E.T., Matsukawa, A., Teh, Y.W., G¨ or¨ ur, D., Lakshminarayanan, B.:
Do deep generative models know what they don’t know? In: Proc. of ICLR (2019)
[36] Serr` a, J.,´Alvarez, D., G´ omez, V., Slizovskaia, O., N´ u˜ nez, J.F., Luque, J.: Input
17

complexity and out-of-distribution detection with likelihood-based generative
models. In: Proc. of ICLR (2020)
[37] Schirrmeister, R., Zhou, Y., Ball, T., Zhang, D.: Understanding anomaly detection
with deep invertible networks through hierarchies of distributions and features.
In: Proc. of NeurIPS (2020)
[38] Kirichenko, P., Izmailov, P., Wilson, A.G.: Why normalizing flows fail to detect
out-of-distribution data. In: Proc. of NeurIPS (2020)
[39] Havtorn, J.D., Frellsen, J., Hauberg, S., Maaløe, L.: Hierarchical vaes know what
they don’t know. In: Proc. of ICML. Proceedings of Machine Learning Research,
vol. 139, pp. 4117–4128 (2021)
[40] Kamkari, H., Ross, B.L., Cresswell, J.C., Caterini, A.L., Krishnan, R.G., Loaiza-
Ganem, G.: A geometric explanation of the likelihood OOD detection paradox.
In: Proc. of ICML (2024)
[41] Tangermann, M., M¨ uller, K.-R., Aertsen, A., Birbaumer, N., Braun, C., Brunner,
C., Leeb, R., Mehring, C., Miller, K.J., Mueller-Putz, G., Nolte, G., Pfurtscheller,
G., Preissl, H., Schalk, G., Schl¨ ogl, A., Vidaurre, C., Waldert, S., Blankertz, B.:
Review of the BCI Competition IV. Frontiers in Neuroscience6(2012) https:
//doi.org/10.3389/fnins.2012.00055
18

Appendix A OOD Detection Results on CAUEEG
T able A1 OOD detection performance in terms of AUROC across different
perturbations and severity levels on CAUEEG.Bold values indicate the best performing
metric for a given perturbation and severity. Discriminative-model-based methods (MSP, Energy,
ODIN, ASH) perform largely at chance level, whereas generative-model-based methods achieve
considerably better OOD detection with increasing performance for higher severity levels.
Perturbation Severity MSP Energy ODIN ASH LL Typ. DoSE SITN
Resampling
125 Hz 0.531 0.517 0.540 0.540 0.286 0.587 0.7600.956
150 Hz 0.497 0.520 0.514 0.590 0.166 0.732 0.8860.984
200 Hz 0.470 0.531 0.495 0.658 0.056 0.906 0.9650.992
Channel Shuffle
10% 0.496 0.502 0.505 0.518 0.622 0.552 0.7110.759
50% 0.443 0.490 0.470 0.570 0.841 0.766 0.9680.956
100% 0.408 0.483 0.436 0.583 0.879 0.819 0.9820.968
Re-referencing
Cz 0.281 0.230 0.305 0.366 0.992 0.9911.0000.997
T7, T8 0.305 0.361 0.339 0.471 0.982 0.9761.0000.997
bipolar 0.426 0.439 0.454 0.562 0.990 0.9891.0000.997
High-pass Filter
2 Hz 0.520 0.640 0.512 0.532 0.455 0.507 0.5660.606
4 Hz 0.507 0.685 0.494 0.578 0.408 0.518 0.5940.756
8 Hz 0.518 0.792 0.494 0.721 0.291 0.589 0.6260.899
Low-pass Filter
45 Hz 0.496 0.501 0.496 0.502 0.446 0.505 0.5440.822
30 Hz 0.495 0.510 0.492 0.515 0.186 0.700 0.9430.987
15 Hz 0.557 0.564 0.556 0.563 0.007 0.9890.9980.994
Appendix B Mahalanobis Distance
We also evaluated the Mahalanobis distance [34], an OOD detection approach that falls
into the discriminative category but differs from the methods detailed in Section 3.2
by modelling the density of the latent embedding space, rather than deriving a score
based on the network’s predictions.
Specifically, we first extracted the penultimate-layer feature representations from
the pre-trained discriminative model, taking the activations immediately following the
global average pooling layer. Using the in-distribution validation set, we estimated the
class-conditional mean feature vectors alongside a single, shared covariance matrix tied
across all classes. To ensure numerical stability, a small regularisation term (ϵ= 10 −5)
was added to the diagonal of the shared covariance matrix prior to computing its
inverse (the shared precision matrix). During evaluation, the Mahalanobis distance was
calculated between each test sample’s feature vector and each of the class-conditional
means using this shared precision matrix. A sample’s final score was then defined
as its minimum Mahalanobis distance across all available classes. OOD samples are
expected to have higher scores indicating that their embeddings are situated further
from the known in-distribution classes.
19

OOD detection results are shown in Table B2. In contrast to other discrimina-
tive methods, the Mahalanobis distance yielded superior OOD detection performance
under the Resampling, Channel Shuffle, and Re-referencing perturbations. However,
it exhibited a severe vulnerability to the High-pass Filter perturbation, where it
performed worse than random chance.
T able B2 Mahalanobis distance OOD detection performance in terms of AUROC
across different perturbations and severity levels.Compared to other discriminative
approaches, Mahalanobis distances show better performance for the Resampling, Channel Shuffle,
and Re-referencing perturbations, but also a strong failure for the High-pass Filter perturbation,
where they consistently underperform even random guessing.
Perturbation Severity TUAB CAUEEG
Resampling
125 Hz 0.548 0.544
150 Hz 0.594 0.586
200 Hz 0.654 0.640
Channel Shuffle
10% 0.583 0.604
50% 0.741 0.763
100% 0.775 0.799
Re-referencing
Cz 0.851 0.925
T7, T8 0.794 0.845
bipolar 0.786 0.861
High-pass Filter
2 Hz 0.348 0.263
4 Hz 0.321 0.252
8 Hz 0.285 0.153
Low-pass Filter
45 Hz 0.500 0.501
30 Hz 0.506 0.505
15 Hz 0.541 0.519
Appendix C Sample Size Dependence
A potential limitation of generative methods could be a larger sample size require-
ment. To investigate this possibility, we performed a data scaling analysis where the
amount of training data was varied while the validation and test data was kept the
same. Starting from a subset of just 25 participants and 5 segments per participant, we
increased the sample size in two different ways: either increasing the number of partic-
ipants or the number of segments per participant. These experiments were conducted
on the TUAB dataset and subsampling of participants was stratified by the normality
label. We used the resampling perturbation at 200 Hz for OOD detection evaluations.
As shown in Figure C1, OOD detection performance generally increased with the
amount of training data, where a larger number of participants (solid lines) was more
impactful than an equal number of segments from a smaller participant cohort (dashed
lines). Generative methods (SITN in particular) performed surprisingly well even with
very limited data and dominated discriminative methods across all evaluated sample
20

sizes. The failure mode for log-likelihoods where performance decreased with more
training data is discussed in Appendix D.
125 500 2000 8000
Total Sample Size (Participants × Segments)
0.2
0.4
0.6
0.8
1.0AUROC
MSP
Energy
ODIN
ASH
Log-likelihood
Typicality
DoSE
SITN

Increasing Participants
Increasing Segments
Fig. C1 Sample Size Dependence of OOD Detection Performance.Starting from a baseline
of just 25 participants and 5 segments per participant (= 125 samples in total), the training data
was gradually increased by either increasing the number of participants (solid lines) or segments per
participant (dashed lines). The sampling rate perturbation at 200 Hz was used to generate OOD
samples. OOD detection performance generally increased with the amount of training data (see
Appendix D for a discussion of the likelihood). Even in the smallest data regimes, generative methods
dominated discriminative approaches. Note that MSP is occluded by ODIN, which showed almost
identical performance across sample sizes.
Appendix D Limitations of Likelihoods for OOD
Detection
Several works in the computer vision literature have identified critical limitations of
likelihoods for OOD detection [35–40], which motivated the development of methods
like Typicality, DoSE, and SITN. In widely replicated experiments, it was shown that
generative models trained on CIF AR-10 consistently assign higher likelihoods to sam-
ples from other datasets like MNIST or SVHN [35–38]. Investigating this issue, Serr` a
et al. further observed a strong correlation between likelihood and sample complexity
(measured by PNG compression size), showing that “simpler” samples like constant-
colour images were consistently assigned higher likelihoods than more “complex”
ones.
We investigated and were able to replicate the same behaviour for EEG data. Panel
A in Figure D2 shows the log-likelihood distribution across ID test samples (100 Hz)
compared to the distributions for the corresponding OOD samples obtained through
the resampling perturbation at different severities. It can be seen that OOD samples
were consistently assigned higher likelihoods, with the highest likelihoods assigned
to samples perturbed at the highest severity level. As mentioned in Section 3.1 and
21

illustrated in Figure 2, samples perturbed with this perturbation appear increasingly
smoothed with higher severities. Furthermore, Panel B in the same figure shows the
(ID) EEG segments with the lowest and highest likelihood in the dataset. Consis-
tent with the complexity observations by Serr` a et al., the highest likelihoods are
assigned to completely flat EEG segments, whereas high-amplitude artefacts resulted
in particularly low likelihoods.
0.0 0.5 1.0
Log-likelihood 1e4
0
1
2Density
1e 4
A SFreq [Hz]
100
125
150
200
0 1
Time (s)
Channels
B Low Likelihood
0 1
Time (s)
High Likelihood
Fig. D2 Likelihood Limitations. ADistribution of log-likelihoods across ID samples (100 Hz)
and OOD samples obtained with the resampling perturbation at increasing severities of 125, 150,
and 200 Hz. As previously observed in the context of computer vision datasets, OOD samples are
consistently assigned higher likelihoods than the in-distribution data.BEEG segments that were
assigned the lowest and highest likelihoods, respectively. As in computer vision, where “simpler”
images like constant-colour images are assigned high likelihoods, EEG segments with completely flat
channels also result in high likelihoods. High-amplitude artefacts result in the opposite extreme and
are assigned very small likelihoods.
Appendix E Training Details
For the generative model, the UNet architecture following Ho et al. [21], as imple-
mented in Dhariwal and Nichol [22] was used with the hyperparameters detailed in
Table E3. Following the flow matching objective of Lipman et al. [23], we constructed
a linear interpolant between a Gaussian noise sampleZ∼ N(0, I) and a data sample
X∼P data:X t = (1−t)Z+tX, t∼ U[0,1] and minimised the mean-squared error
between the network output and the target vector fieldX−Z.
For the discriminative model, a Temporal Convolutional Network (TCN) [19] was
used with the hyperparameters detailed in Table E4. This model was trained using a
supervised cross-entropy loss for the respective prediction task.
Both models were optimised with AdamW (learning rate 10 −4, weight decay 0.01,
β1 = 0.9,β 2 = 0.999,ϵ= 10 −8) and global gradient norm clipping (max norm
1.0). The generative and discriminative models were trained for 1,000,000 and 50,000
gradient steps, respectively, at a batch size of 128 and with weights restored to the
checkpoint of lowest validation loss. It was empirically verified that the validation loss
had converged within the maximum number of gradient steps for both models.
22

T able E3UNet hyperparameters.
Hyperparameter Value
Channels 64
Depth 2
Channel multipliers 1, 2, 2, 2
Heads 1
Attention resolution 8
Dropout 0.0
T able E4TCN hyperparameters.
Hyperparameter Value
Blocks 4
Filters 64
Kernel size 5
Dilations 1, 2, 4, 8
Dropout 0.0
Appendix F Exploratory Cross-dataset Experiments
We conducted a number of cross-dataset experiments where we evaluated the TUAB-
trained methods on CAUEEG and conversely the CAUEEG-trained methods on
TUAB. We consider this analysis exploratory as it is unclear to what degree samples
from one of these datasets should be considered OOD for a model trained on the other
dataset. Aside from potential (unquantified) hardware differences, participants in the
TUAB dataset could in principle also be assigned a label from the dementia diagnosis
task on CAUEEG, such that EEG recordings from one dataset should not necessarily
be considered OOD for a model trained on the other one. Rather than treating this
setup as a benchmarking task to evaluate OOD detection performance, we are inter-
ested to what degree cross-dataset samples result in high OOD scores and if there are
differences across participant subgroups.
Table F5 shows AUROC values analogous to those reported for OOD detection
performance. Overall, the different methods show moderate discrimination between
the two datasets. Scores from DoSE and SITN, the two strongest OOD detection
methods according to the results in Section 4.1, do not separate samples from the
two datasets when trained on TUAB (AUROC<0.55), but achieve AUROC values
of 0.703 and 0.740 respectively when trained on CAUEEG. This would be consistent
with CAUEEG forming a subset of the TUAB data distribution.
T able F5 Cross-dataset Discrimination Across OOD Detection Methods.Models were
trained on one dataset and then evaluated using the test split of the training dataset as ID and the
test split of the other dataset as OOD data (e.g. TUAB→CAUEEG denotes trained on TUAB and
using CAUEEG as OOD). The degree to which OOD scores discriminate between samples from the
two datasets is reported in terms of AUROC. Note that ID and OOD should be interpreted with a
grain of salt in this setup as it is unclear to what degree cross-dataset samples are OOD.
Condition MSP Energy ODIN ASH LL Typ. DoSE SITN
TUAB→CAUEEG 0.594 0.478 0.598 0.5170.6690.432 0.462 0.544
CAUEEG→TUAB 0.489 0.558 0.477 0.514 0.398 0.643 0.7030.740
In the following figures, we compare OOD scores across different subgroups within
the target dataset. To do so, we aggregated OOD scores on the participant level
by averaging across samples, resulting in an average OOD score per participant.
23

Furthermore, to facilitate comparisons, we normalised OOD scores by applying min-
max scaling to map the raw outputs of each OOD detection method to a standard
[0,1] range. Additionally, scores were inverted where necessary, such that a higher
normalised OOD score always indicates “more OOD”.
Figure F3 shows normalised OOD scores across the different diagnosis labels on
CAUEEG (normal, mild cognitive impairment, dementia) for the TUAB-trained mod-
els. Trends across diagnosis groups are inconsistent across methods and scores are
strongly overlapping. Figure F4 shows the same scores across age, with the colours
corresponding to the same diagnosis groups (normal in green, mci in orange, dementia
in blue). No clear trends are discernable, which might be expected given that the age
range of the TUAB training data spans the full age range of the CAUEEG dataset.
Figure F5 shows normalised scores for the CAUEEG-trained models on TUAB, strat-
ified by the EEG normality label. Although scores are strongly overlapping for all
methods, abnormal EEGs tended to be assigned somewhat higher OOD scores by
SITN. Finally, Figure F6 shows the same OOD scores across age on TUAB. As for
CAUEEG, no clear trend is discernable, although in this case one might have expected
younger participants to look more OOD given that only 14 out of 950 participants in
the CAUEEG training data (less than 2%) are aged younger than 50.
0.00
0.25
0.50
0.75
1.00Normalised OOD Score
MSP
 Energy
 ODIN
 ASH
normal mci dementia
Dementia Label
0.00
0.25
0.50
0.75
1.00Normalised OOD Score
Log Likelihood
normal mci dementia
Dementia Label
Typicality
normal mci dementia
Dementia Label
DoSE
normal mci dementia
Dementia Label
SITN
Fig. F3 Cross-dataset Subgroup Analysis of OOD Scores Across Diagnosis Labels on
CAUEEG.The results show normalised participant-level OOD scores for samples from the CAUEEG
dataset assigned by methods trained on TUAB. Scores are largely overlapping without a consistent
trend across diagnosis groups.
24

0.00
0.25
0.50
0.75
1.00Normalized OOD Score
MSP
 Energy
 ODIN
 ASH
40 60 80
Age
0.00
0.25
0.50
0.75
1.00Normalized OOD Score
Log Likelihood
40 60 80
Age
Typicality
40 60 80
Age
DoSE
40 60 80
Age
SITN
Fig. F4 Cross-dataset Subgroup Analysis of OOD Scores Across Age on CAUEEG.
The results show normalised participant-level OOD scores for samples from the CAUEEG dataset
assigned by methods trained on TUAB. No clear trend is observable.
0.00
0.25
0.50
0.75
1.00Normalized OOD Score
MSP
 Energy
 ODIN
 ASH
normal abnormal
Normality Label
0.00
0.25
0.50
0.75
1.00Normalized OOD Score
Log Likelihood
normal abnormal
Normality Label
Typicality
normal abnormal
Normality Label
DoSE
normal abnormal
Normality Label
SITN
Fig. F5 Cross-dataset Subgroup Analysis of OOD Scores Across EEG Normality Labels
on TUAB.The results show normalised participant-level OOD scores for samples from the TUAB
dataset assigned by methods trained on CAUEEG. Scores are largely overlapping, although SITN
assigned somewhat higher OOD scores to abnormal EEG recordings.
25

0.00
0.25
0.50
0.75
1.00Normalized OOD Score
MSP
 Energy
 ODIN
 ASH
25 50 75
Age
0.00
0.25
0.50
0.75
1.00Normalized OOD Score
Log Likelihood
25 50 75
Age
Typicality
25 50 75
Age
DoSE
25 50 75
Age
SITN
Fig. F6 Cross-dataset Subgroup Analysis of OOD Scores Across Age on TUAB.The
results show normalised participant-level OOD scores for samples from the TUAB dataset assigned
by methods trained on CAUEEG. No clear trends are discernable.
Appendix G Cross-participant BCI Experiment
We evaluated the different OOD detection methods in a cross-participant setup on
the BNCI 2014-001 Motor Imagery dataset [41]. This dataset contains EEG data for a
motor imagery task from nine participants. Two sessions (recorded on different days)
are available for each participant, each of which in turn consists of six runs with 12
trials per class. In our setup, we only used trials for the left hand and right hand
classes, resulting in 144 trials per session and participant. We used the official train-
test split, which assigns the first session of each participant to train and the second to
test. Additionally, we used the last run in the training session as validation data. For
our cross-participant experiment, we trained the classification model and the OOD
detection methods only on the training data of the first participant. We then evaluated
the methods on the test data of the training participant as well as on the test data of
all other participants.
Figure G7 shows the results with prediction accuracy for the motor imagery task
and OOD scores aggregated to the participant level through averaging. For better
visualisation, we flipped scores where necessary, such that higher scores on the x-
axis always correspond to higher OOD scores. SITN is the only method to clearly
separate the (ID) training participant from all (OOD) participants. On six out of eight
of the unseen participants prediction accuracy for the motor imagery task dropped
considerably below the within-participant test performance. MSP assigned the lowest
OOD scores to the two participants where model performance was higher than for
the training participant, however, it also assigned the third lowest OOD score to a
26

participant where performance dropped below chance level and which was flagged as
highly OOD by all generative methods as well as the Energy score and ASH.
0.975
 0.950
Score (  more OOD)
0.5
0.7
0.9
Accuracy
1
2
3
4
5
6
7
8
9
MSP
150 200
Score (  more OOD)
1
2
3
4
5
6
7
8
9
Energy
0.505
 0.503
Score (  more OOD)
1
2
3
4
5
6
7
8
9
ODIN
200 250
Score (  more OOD)
1
2
3
4
5
6
7
8
9
ASH
0 10000
Score (  more OOD)
0.5
0.7
0.9
Accuracy
1
2
3
4
5
6
7
8
9
Log-Likelihood
5000 10000
Score (  more OOD)
1
2
3
4
5
6
7
8
9
Typicality
30 40 50
Score (  more OOD)
1
2
3
4
5
6
7
8
9
DoSE
0.6 0.8
Score (  more OOD)
1
2
3
4
5
6
7
8
9
SITN
Fig. G7 Cross-participant Experiments on the BNCI 2014-001 Motor Imagery Dataset.
Numbers next to the points indicate participant id. Methods were trained on the training data from
participant 1 and evaluated on the test data from all participants. OOD scores were aggregated on the
participant-level through averaging and aligned such that higher scores always indicate more OOD.
Only SITN clearly separates test data from the training participant (ID) from the other participants
(OOD). MSP assigns the lowest OOD scores to two participants where model performance was even
higher than for the training participant, but also the 3rd lowest score to the participant where model
performance was lowest and which was flagged as highly OOD by most other methods.
Appendix H Full Downstream Performance Results
The following pages show the full results for the downstream performance evaluations
across both tasks and datasets (normality prediction on TUAB (binary classification,
chance level 50%); dementia diagnosis on CAUEEG (3-way classification into normal,
MCI, dementia, chance level≈33%)) for all perturbations and OOD detection meth-
ods. Performance is shown in terms of accuracy across percentile bins of the OOD
score, where the x ticks indicate the upper edge of the corresponding bin (i.e. the first
bin contains samples from the 0-0.1 percentile, the second one 0.1-1, etc.). The his-
tograms indicate the number of ID and OOD samples in each bin. The arrows in the
top left/right of each plot indicate the OOD direction for the corresponding metric.
The captions for each figure indicate the task and dataset as well as the perturbation
used to generate the OOD data.
27

0.1
1
5
10
25
50
75
90
95
99
99.9
100
MSP Percentile Bin Upper Edge
0
25k
50k
75kSample Count
371 401
OOD
MSP
0.1
1
5
10
25
50
75
90
95
99
99.9
100
Energy Percentile Bin Upper Edge
371 371
OOD
Energy
0.1
1
5
10
25
50
75
90
95
99
99.9
100
ODIN Percentile Bin Upper Edge
0
25k
50k
75kSample Count
371 371
OOD
ODIN
0.1
1
5
10
25
50
75
90
95
99
99.9
100
ASH Percentile Bin Upper Edge
371 371
OOD
ASH
0.1
1
5
10
25
50
75
90
95
99
99.9
100
Log Likelihood Percentile Bin Upper Edge
0
25k
50k
75kSample Count
371 371
OOD
Log Likelihood
0.1
1
5
10
25
50
75
90
95
99
99.9
100
Typicality Percentile Bin Upper Edge
371 371
OOD
Typicality
0.1
1
5
10
25
50
75
90
95
99
99.9
100
DoSE Percentile Bin Upper Edge
0
25k
50k
75kSample Count
371 371
OOD
DoSE
0.1
1
5
10
25
50
75
90
95
99
99.9
100
SITN Percentile Bin Upper Edge
370 372
OOD
SITN
53 50 51 53 57
66 71 74 81 85 85
47
0
50
100
Accuracy (%)
46
64
82 81 74
66 66 65 62 56 57 51
50 50 52 53 58
66 71 74 81 85 85
47
0
50
100
Accuracy (%)
45
69
80 78 73 70 66 61 58 53 57 55
47
61
79 76 76 73
59 56
67
79
94
71
0
50
100
Accuracy (%)
77 78 77 77 75 69
61 59 68
78
88
47
49
85
64 64 64 61 68 74 78 80 80 78
0
50
100
Accuracy (%)
80 82 81 80 81 80
57 52 51 55 55 56
ID OOD Accuracy Average Accuracy (67.5%)
Fig. H8 Normality Prediction on TUAB — Resampling Perturbation (200 Hz)
28

0.1
1
5
10
25
50
75
90
95
99
99.9
100
MSP Percentile Bin Upper Edge
0
25k
50k
75kSample Count
371 387
OOD
MSP
0.1
1
5
10
25
50
75
90
95
99
99.9
100
Energy Percentile Bin Upper Edge
371 371
OOD
Energy
0.1
1
5
10
25
50
75
90
95
99
99.9
100
ODIN Percentile Bin Upper Edge
0
25k
50k
75kSample Count
369 371
OOD
ODIN
0.1
1
5
10
25
50
75
90
95
99
99.9
100
ASH Percentile Bin Upper Edge
371 371
OOD
ASH
0.1
1
5
10
25
50
75
90
95
99
99.9
100
Log Likelihood Percentile Bin Upper Edge
0
25k
50k
75kSample Count
371 371
OOD
Log Likelihood
0.1
1
5
10
25
50
75
90
95
99
99.9
100
Typicality Percentile Bin Upper Edge
371 371
OOD
Typicality
0.1
1
5
10
25
50
75
90
95
99
99.9
100
DoSE Percentile Bin Upper Edge
0
25k
50k
75kSample Count
371 371
OOD
DoSE
0.1
1
5
10
25
50
75
90
95
99
99.9
100
SITN Percentile Bin Upper Edge
371 376
OOD
SITN
49 51 51 54 56 63 70 69 70
79 85
50
0
50
100
Accuracy (%)
48 54
70 72 68 62 64 65 65 65 60 59
49 51 52 53 56 63 70 69 70
79 85
50
0
50
100
Accuracy (%)
49
58
73 72 67 64 64 63 62 60 59 61
50 56 58 51 50 56
70 77 80
89 93
41
0
50
100
Accuracy (%)
74 74 73 73 73 68
60 53 58
73
55 49
48
55
72
58 53 60
68 72 76 80 80 78
0
50
100
Accuracy (%)
80 81 81 80 81 74
59
50
39 32 39
54
ID OOD Accuracy Average Accuracy (64.7%)
Fig. H9 Normality Prediction on TUAB — Channel Shuffle Perturbation (100%)
29

0.1
1
5
10
25
50
75
90
95
99
99.9
100
MSP Percentile Bin Upper Edge
0
25k
50k
75kSample Count
371 485
OOD
MSP
0.1
1
5
10
25
50
75
90
95
99
99.9
100
Energy Percentile Bin Upper Edge
371 371
OOD
Energy
0.1
1
5
10
25
50
75
90
95
99
99.9
100
ODIN Percentile Bin Upper Edge
0
25k
50k
75kSample Count
364 371
OOD
ODIN
0.1
1
5
10
25
50
75
90
95
99
99.9
100
ASH Percentile Bin Upper Edge
371 371
OOD
ASH
0.1
1
5
10
25
50
75
90
95
99
99.9
100
Log Likelihood Percentile Bin Upper Edge
0
25k
50k
75kSample Count
371 371
OOD
Log Likelihood
0.1
1
5
10
25
50
75
90
95
99
99.9
100
Typicality Percentile Bin Upper Edge
371 371
OOD
Typicality
0.1
1
5
10
25
50
75
90
95
99
99.9
100
DoSE Percentile Bin Upper Edge
0
25k
50k
75kSample Count
371 371
OOD
DoSE
0.1
1
5
10
25
50
75
90
95
99
99.9
100
SITN Percentile Bin Upper Edge
370
OOD
SITN
48 49 51 53 55 61
72
84
93 96 92
50
0
50
100
Accuracy (%)
49 49
71 76 74 69 67 65 67 67 60 57
50 48 51 52 54 61
72
85
93 97 91
47
0
50
100
Accuracy (%)
50 52
75 77 76 72 66 63 60 58 57 54
47 49 51 57 55 62
76 80 80
89 94
48
0
50
100
Accuracy (%)
79 82 80 81 79 74
65 58 57 51 49 47
44 50 53 57 54
64
75 81 81 82 81 79
0
50
100
Accuracy (%)
80 82 81 80 81 80
60 55 52 50 51
ID OOD Accuracy Average Accuracy (68.7%)
Fig. H10 Normality Prediction on TUAB — Re-referencing Perturbation (bipolar)
Note: The irregular bin sizes at the upper percentiles of the SITN plot are due to metric saturation,
where a large number of tied maximum scores are grouped into the final bin.
30

0.1
1
5
10
25
50
75
90
95
99
99.9
100
MSP Percentile Bin Upper Edge
0
25k
50k
75kSample Count
371 371
OOD
MSP
0.1
1
5
10
25
50
75
90
95
99
99.9
100
Energy Percentile Bin Upper Edge
371 371
OOD
Energy
0.1
1
5
10
25
50
75
90
95
99
99.9
100
ODIN Percentile Bin Upper Edge
0
25k
50k
75kSample Count
370 371
OOD
ODIN
0.1
1
5
10
25
50
75
90
95
99
99.9
100
ASH Percentile Bin Upper Edge
371 371
OOD
ASH
0.1
1
5
10
25
50
75
90
95
99
99.9
100
Log Likelihood Percentile Bin Upper Edge
0
25k
50k
75kSample Count
371 371
OOD
Log Likelihood
0.1
1
5
10
25
50
75
90
95
99
99.9
100
Typicality Percentile Bin Upper Edge
371 371
OOD
Typicality
0.1
1
5
10
25
50
75
90
95
99
99.9
100
DoSE Percentile Bin Upper Edge
0
25k
50k
75kSample Count
371 371
OOD
DoSE
0.1
1
5
10
25
50
75
90
95
99
99.9
100
SITN Percentile Bin Upper Edge
370 372
OOD
SITN
45 50 52 55 57
66
77
85 90
98 98
53
0
50
100
Accuracy (%)
49
76
88 89 83 77
69
58 53 56
68 65
48 49 52 54 58
66
77
85 90
98 98
53
0
50
100
Accuracy (%)
46
81
88 86 80 74
67 63 62
75
67 72
44
59
78 76 74 73 72 68
60
77
85
41
0
50
100
Accuracy (%)
72 74 73 73 73 74 71 67 67
84
64
44
41
70
81
68 68 71 74 73 74 72 71 74
0
50
100
Accuracy (%)
80 82 81 80 81 75
66 65 69 71
50 55
ID OOD Accuracy Average Accuracy (72.0%)
Fig. H11 Normality Prediction on TUAB — High-pass Filter Perturbation (8 Hz)
31

0.1
1
5
10
25
50
75
90
95
99
99.9
100
MSP Percentile Bin Upper Edge
0
25k
50k
75kSample Count
371 377
OOD
MSP
0.1
1
5
10
25
50
75
90
95
99
99.9
100
Energy Percentile Bin Upper Edge
371 371
OOD
Energy
0.1
1
5
10
25
50
75
90
95
99
99.9
100
ODIN Percentile Bin Upper Edge
0
25k
50k
75kSample Count
365 371
OOD
ODIN
0.1
1
5
10
25
50
75
90
95
99
99.9
100
ASH Percentile Bin Upper Edge
371 371
OOD
ASH
0.1
1
5
10
25
50
75
90
95
99
99.9
100
Log Likelihood Percentile Bin Upper Edge
0
25k
50k
75kSample Count
371 371
OOD
Log Likelihood
0.1
1
5
10
25
50
75
90
95
99
99.9
100
Typicality Percentile Bin Upper Edge
371 371
OOD
Typicality
0.1
1
5
10
25
50
75
90
95
99
99.9
100
DoSE Percentile Bin Upper Edge
0
25k
50k
75kSample Count
371 371
OOD
DoSE
0.1
1
5
10
25
50
75
90
95
99
99.9
100
SITN Percentile Bin Upper Edge
370 371
OOD
SITN
48 50 52 55 62
74
85
92 97 99 96
49
0
50
100
Accuracy (%)
45
73
89 91 87
79 76 72 68 65 64 64
47 50 53 55 62
75
84
92 97 99 96
48
0
50
100
Accuracy (%)
47
79
91 89 86 81 77 70 65 61 66 64
49
70
79 76 80 80 79 74 73 74
98
47
0
50
100
Accuracy (%)
80 83 80 81 80 80 78 74 73 74
93
45
78
98
72 72 78 76 79 80 81 82 81 79
0
50
100
Accuracy (%)
80 82 81 80 81 81 79 73 72 72 67
55
ID OOD Accuracy Average Accuracy (78.0%)
Fig. H12 Normality Prediction on TUAB — Low-pass Filter Perturbation (15 Hz)
32

1
5
10
25
50
75
90
95
99
100
MSP Percentile Bin Upper Edge
0
5k
10k
15kSample Count
694 694
OOD
MSP
1
5
10
25
50
75
90
95
99
100
Energy Percentile Bin Upper Edge
694 694
OOD
Energy
1
5
10
25
50
75
90
95
99
100
ODIN Percentile Bin Upper Edge
0
5k
10k
15kSample Count
694 694
OOD
ODIN
1
5
10
25
50
75
90
95
99
100
ASH Percentile Bin Upper Edge
694 694
OOD
ASH
1
5
10
25
50
75
90
95
99
100
Log Likelihood Percentile Bin Upper Edge
0
5k
10k
15kSample Count
694 694
OOD
Log Likelihood
1
5
10
25
50
75
90
95
99
100
Typicality Percentile Bin Upper Edge
694 694
OOD
Typicality
1
5
10
25
50
75
90
95
99
100
DoSE Percentile Bin Upper Edge
0
5k
10k
15kSample Count
694 694
OOD
DoSE
1
5
10
25
50
75
90
95
99
100
SITN Percentile Bin Upper Edge
694
OOD
SITN
34 37 37 38 40 44 48 49 50 43
0
25
50
75
100
Accuracy (%)
35
42 47 46 43 42 41 40 38 37
37 37 37 38 39 44 49 51 52 46
0
25
50
75
100
Accuracy (%)
43 46 44 45 44 42 41 36 36 35
36 38
48 53 48
40
32 32 35
44
0
25
50
75
100
Accuracy (%)
52 54 53 52 47
38 31 33 36 41
49
28 34 33 34
51 52 53 49 51
0
25
50
75
100
Accuracy (%)
48 51 51 53 51
30 35 37 39 38
ID OOD Accuracy Average Accuracy (42.6%)
Fig. H13 Dementia Diagnosis on CAUEEG — Resampling Perturbation (200 Hz)
33

1
5
10
25
50
75
90
95
99
100
MSP Percentile Bin Upper Edge
0
5k
10k
15kSample Count
694 694
OOD
MSP
1
5
10
25
50
75
90
95
99
100
Energy Percentile Bin Upper Edge
694 694
OOD
Energy
1
5
10
25
50
75
90
95
99
100
ODIN Percentile Bin Upper Edge
0
5k
10k
15kSample Count
694 694
OOD
ODIN
1
5
10
25
50
75
90
95
99
100
ASH Percentile Bin Upper Edge
694 694
OOD
ASH
1
5
10
25
50
75
90
95
99
100
Log Likelihood Percentile Bin Upper Edge
0
5k
10k
15kSample Count
694 694
OOD
Log Likelihood
1
5
10
25
50
75
90
95
99
100
Typicality Percentile Bin Upper Edge
694 694
OOD
Typicality
1
5
10
25
50
75
90
95
99
100
DoSE Percentile Bin Upper Edge
0
5k
10k
15kSample Count
694 694
OOD
DoSE
1
5
10
25
50
75
90
95
99
100
SITN Percentile Bin Upper Edge
694 708
OOD
SITN
31 37 36 39 42 45 48 43 42 33
0
25
50
75
100
Accuracy (%)
32 38 45 44 44 43 41 39 41 34
34 37 36 38 41 45 49 47 44 34
0
25
50
75
100
Accuracy (%)
39 44 42 43 44 43 42 39 35 33
43
27 32 33 38
48 50 47
64 63
0
25
50
75
100
Accuracy (%)
50 52 50 49 46 42
33 32 27 40
42
27 29 31 36
52 53 53 50 51
0
25
50
75
100
Accuracy (%)
48 51 51 53 49
34 35 36 31 35
ID OOD Accuracy Average Accuracy (42.6%)
Fig. H14 Dementia Diagnosis on CAUEEG — Channel Shuffle Perturbation (100%)
34

1
5
10
25
50
75
90
95
99
100
MSP Percentile Bin Upper Edge
0
5k
10k
15kSample Count
694 694
OOD
MSP
1
5
10
25
50
75
90
95
99
100
Energy Percentile Bin Upper Edge
694 694
OOD
Energy
1
5
10
25
50
75
90
95
99
100
ODIN Percentile Bin Upper Edge
0
5k
10k
15kSample Count
692 694
OOD
ODIN
1
5
10
25
50
75
90
95
99
100
ASH Percentile Bin Upper Edge
694 694
OOD
ASH
1
5
10
25
50
75
90
95
99
100
Log Likelihood Percentile Bin Upper Edge
0
5k
10k
15kSample Count
694 694
OOD
Log Likelihood
1
5
10
25
50
75
90
95
99
100
Typicality Percentile Bin Upper Edge
694 694
OOD
Typicality
1
5
10
25
50
75
90
95
99
100
DoSE Percentile Bin Upper Edge
0
5k
10k
15kSample Count
694 694
OOD
DoSE
1
5
10
25
50
75
90
95
99
100
SITN Percentile Bin Upper Edge
694
OOD
SITN
34 36 36 39 42 46 50 47 41 28
0
25
50
75
100
Accuracy (%)
29 33
41 43 43 44 44 44 45 40
36 37 36 38 41 46 51 48 40 30
0
25
50
75
100
Accuracy (%)
39 43 41 42 44 44 45 43 38 37
31 31 34 34 35
51 52 47
64 64
0
25
50
75
100
Accuracy (%)
52 56 53 53 51
35 34 34 31 31
31 30 35 35 35
51 53 53 50 51
0
25
50
75
100
Accuracy (%)
48 51 51 53 52
34 36 35 32
ID OOD Accuracy Average Accuracy (43.1%)
Fig. H15 Dementia Diagnosis on CAUEEG — Re-referencing Perturbation (bipolar)
Note: The irregular bin sizes at the upper percentiles of the SITN plot are due to metric saturation,
where a large number of tied maximum scores are grouped into the final bin.
35

1
5
10
25
50
75
90
95
99
100
MSP Percentile Bin Upper Edge
0
5k
10k
15kSample Count
694 694
OOD
MSP
1
5
10
25
50
75
90
95
99
100
Energy Percentile Bin Upper Edge
694 694
OOD
Energy
1
5
10
25
50
75
90
95
99
100
ODIN Percentile Bin Upper Edge
0
5k
10k
15kSample Count
693 694
OOD
ODIN
1
5
10
25
50
75
90
95
99
100
ASH Percentile Bin Upper Edge
694 694
OOD
ASH
1
5
10
25
50
75
90
95
99
100
Log Likelihood Percentile Bin Upper Edge
0
5k
10k
15kSample Count
694 694
OOD
Log Likelihood
1
5
10
25
50
75
90
95
99
100
Typicality Percentile Bin Upper Edge
694 694
OOD
Typicality
1
5
10
25
50
75
90
95
99
100
DoSE Percentile Bin Upper Edge
0
5k
10k
15kSample Count
694 694
OOD
DoSE
1
5
10
25
50
75
90
95
99
100
SITN Percentile Bin Upper Edge
694 700
OOD
SITN
36 39 38 42 45 50
59
69 74
56
0
25
50
75
100
Accuracy (%)
39
49 51 52 52 51 46 45 48
32
37 39 40 42 44 50
61
69 67
60
0
25
50
75
100
Accuracy (%)
46 47 45 47 50 51 54 49 43 45
32 34 41
50 53 49 48 53
65
43
0
25
50
75
100
Accuracy (%)
52 52 54 53 51 48 46 52 52
32
36
51 48 47 50 51 52 50 48 49
0
25
50
75
100
Accuracy (%)
48 51 51 53 50 49 50 49 41 38
ID OOD Accuracy Average Accuracy (49.7%)
Fig. H16 Dementia Diagnosis on CAUEEG — High-pass Filter Perturbation (8 Hz)
36

1
5
10
25
50
75
90
95
99
100
MSP Percentile Bin Upper Edge
0
5k
10k
15kSample Count
694 694
OOD
MSP
1
5
10
25
50
75
90
95
99
100
Energy Percentile Bin Upper Edge
694 694
OOD
Energy
1
5
10
25
50
75
90
95
99
100
ODIN Percentile Bin Upper Edge
0
5k
10k
15kSample Count
693 694
OOD
ODIN
1
5
10
25
50
75
90
95
99
100
ASH Percentile Bin Upper Edge
694 694
OOD
ASH
1
5
10
25
50
75
90
95
99
100
Log Likelihood Percentile Bin Upper Edge
0
5k
10k
15kSample Count
694 694
OOD
Log Likelihood
1
5
10
25
50
75
90
95
99
100
Typicality Percentile Bin Upper Edge
694 694
OOD
Typicality
1
5
10
25
50
75
90
95
99
100
DoSE Percentile Bin Upper Edge
0
5k
10k
15kSample Count
694 694
OOD
DoSE
1
5
10
25
50
75
90
95
99
100
SITN Percentile Bin Upper Edge
694
OOD
SITN
37 40 40 42 45 50
59
68 67
57
0
25
50
75
100
Accuracy (%)
37
46 51 51 51 51 47 44 47 41
39 40 39 42 44 51
60 67 64 62
0
25
50
75
100
Accuracy (%)
45 51 46 47 51 51 50 48 45 43
39 38
49 54 53 48 46 45 56 48
0
25
50
75
100
Accuracy (%)
52 56 53 53 51 47 45 46 56 50
55 55
46 46 47 52 53 53 50 51
0
25
50
75
100
Accuracy (%)
48 51 51 53 52 48 47 47 47 43
ID OOD Accuracy Average Accuracy (49.6%)
Fig. H17 Dementia Diagnosis on CAUEEG — Low-pass Filter Perturbation (15 Hz)
37
