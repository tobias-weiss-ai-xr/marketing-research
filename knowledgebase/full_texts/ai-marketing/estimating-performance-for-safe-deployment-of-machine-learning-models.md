---
title: Estimating Performance for Safe Deployment of Machine Learning Models
url: https://arxiv.org/abs/2610.29262
category: ai-marketing
subcategory: measurement
date: 2026-10
venue: ''
authors:
- Zeju Li
- Konstantinos Kamnitsas
- Mobarakol Islam
- Melanie Roschewitz
- Cheng Ouyang
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.29262
pages: 78
chars: 167182
fetched_at: '2026-11-08T13:39:01+00:00'
kb_version: 1
---

# Estimating Performance for Safe Deployment of Machine Learning Models

Estimating Performance for Safe Deployment of
Machine Learning Models
Zeju Lia,b, Konstantinos Kamnitsasc, Mobarak I. Hoqued, Mélanie
Roschewitze, Cheng Ouyangc,e,g, Chen Chenf,e, Ben Glockere
aCollege of Biomedical Engineering, Fudan University, Shanghai, China
bOxford Centre for Integrative Neuroimaging, University of Oxford, Oxford, UK
cDepartment of Engineering Science, University of Oxford, Oxford, UK
dDivision of Informatics, Imaging and Data Science, University of
Manchester, Manchester, UK
eDepartment of Computing, Imperial College London, London, UK
fSchool of Computer Science, University of Sheffield, Sheffield, UK
gInstitute of Clinical Sciences, Imperial College London, London, UK
Abstract
The main challenge in applying deep neural networks to real-world scenarios
lies in distributional discrepancies between training and test datasets, often
caused by variations in data acquisition conditions. Assessing the perfor-
mance of pre-trained models without labels is crucial for safety, but this is
complicated by deep models’ overly optimistic probabilistic outputs, often
exacerbated by class imbalances, leading to unreliable predictions. To ad-
dress these issues, we introduce MOVAL, a novel MOdel eVALuation tool
that estimates performance using unlabeled test data. MOVAL incorporates
class-wise confidence calibration to adjust model outputs, allowing for the es-
timation of metrics beyond accuracy and mitigating the detrimental effects
of class imbalance on confidence calibration. Additionally, we propose an
ensemble approach that combines multiple calibrated confidence scores for a
more robust solution. We validate MOVAL on natural and medical image
datasets with various acquisition shifts, covering tasks from classification to
segmentation. It achieves state-of-the-art results across evaluation metrics
such as accuracy, F1-Score, AUC, and more. Furthermore, we demonstrate
that MOVAL provides accurate performance estimations at the class, in-
stance, and pixel levels, ensuring the transparent and safe deployment of
machine learning models. We provide MOVAL as a deployment tool for
monitoring and estimating performance under a range of domain shifts.
arXiv:2610.29262v2  [cs.LG]  29 Oct 2026

Keywords:Trustworthy Machine Learning, Interpretability, Quality
Control, Deep Learning
1. Introduction
The witnessed success of machine learning is built upon the independently
and identically distributed (IID) assumption. However, this assumption does
not always hold in real-world applications due to domain shifts, where the
training and test data come from different distributions. There are multiple
kinds of domain shifts, but we primarily consider acquisition shifts, as they
have the most direct and significant impact on model performance, causing
modelstofailsilently. Therefore, trustworthysafeguardsareneededtoensure
model performance with minimal assumptions and to provide prompt feed-
back without access to ground truth (Eche et al., 2021). Existing algorithms
for model evaluation are either task-specific or rely on globally calibrated
probabilities, which do not provide a comprehensive evaluation beyond accu-
racy or Dice similarity coefficient (DSC) (Zenk et al., 2025). In this work, we
combinerecentadvancesinmodelcalibrationandconfidencescoreestimation
to develop a new model evaluation method that can be applied to various
types of tasks, informing model failure with multiple estimated metrics and
meaningful indicators at different levels.
Developing reliable, real-time performance assessment systems is crucial
for the safe deployment of machine learning in clinical practice. Such systems
help identify the limits of model applicability and support practitioners in
iteratively refining their training strategies. For instance, when a skin-lesion
classification model is trained on data from a source domain, deployment
decisions in a new target domain can be guided by the model’s predicted
accuracy on all unlabeled test images. Additionally, because magnetic reso-
nanceimaging(MRI)istypicallynon-quantitative, itisoftenunclearwhether
a model remains valid when applied in a local hospital where acquisition pro-
tocols differ and expert annotations may be unavailable. This approach helps
prevent overfitting when optimizing results using a small number of labeled
test images by using predicted accuracy as a surrogate to validation loss.
1.1. Related Works
Many methods have been proposed for this scenario, but they often lack
robustness or have limited applicability. For example, distance metric be-
2

tween the training and test datasets can be a good indicator for model per-
formance, but requires the access to validation data every time of estimat-
ing (Horvitz and Thompson, 1952; Chen et al., 2021) and/or need another
regression model (Deng and Zheng, 2021; Robinson et al., 2018). Reference-
based methods (Fan and Davidson, 2006; Wang et al., 2020b; Valindria et al.,
2017; Li et al., 2022a) estimate model performance by comparing the predic-
tion results to a predefined reference (i.e. shape template for segmentation),
but lack the ability to leverage the probability of the model output, and are
mostly limited to segmentation tasks with strong shape priors. As a sepa-
rate but related line of work, conformal prediction methods (Barber et al.,
2023) provide prediction sets with formal coverage guarantees, which can
increase confidence at deployment but do not directly reflect the underlying
model’s performance. These are related but distinct goals: conformal pre-
diction provides set-valued uncertainty guarantees for individual predictions
under specific assumptions (e.g., exchangeability or its relaxations), whereas
MOVAL estimates aggregate, class-, instance-, and pixel-wise performance
metrics (accuracy, F1-Score, sensitivity, precision, AUC) without providing
per-prediction coverage guarantees.
Confidence-score-basedmethods, whichestimatetheaccuracyofatrained
model using the mean value of the maximum class probability (MCP), are
more efficient and are believed to be accurate for model evaluation (Elsahar
and Gallé, 2019; Mehrtash et al., 2020; Garg et al., 2022; Islam et al., 2021;
Baek et al., 2022; Ouyang et al., 2022b; Roschewitz and Glocker, 2023; Lu
et al., 2023; Press et al., 2024). However, this approach is largely limited
to accuracy estimation, which can be a misleading metric for imbalanced
datasets, a common occurrence in real-world classification tasks, particularly
in segmentation. For example, accuracy can approach 100%in imbalanced
datasets, even if all samples are classified as belonging to the majority class.
In medical applications, it is often preferable to track clinically relevant met-
rics such as sensitivity or specificity, or metrics that take into account class
imbalance, such as area under the curve (AUC) or F1-Score.
Model calibration, also known as confidence calibration, is the process of
adjusting the probability outputs of a trained model to better reflect the true
likelihoodofitspredictions. Thisadjustmentistypicallyperformedusingval-
idation data, aiming to ensure that the calibrated model’s confidence scores
align with the observed accuracy on unseen test data. A model is said to be
well-calibrated when the predicted confidence aligns with the true probability
that the associated model prediction is correct. However, most methods as-
3

sume that every class performs equally well (Guo et al., 2017; Guillory et al.,
2021; Garg et al., 2022; Kivimäki et al., 2024; Mehrtash et al., 2020), thus
calibrating the probabilities of all classes in the same way. In practice, this
is not true, especially in the presence of class imbalance, where predictions
for majority classes tend to be overconfident, while predictions for minority
classes are often underconfident (Li et al., 2020). Consequently, after cal-
ibration, although global metrics may be aligned, the discrepancy between
different classes becomes even larger. This not only increases the estima-
tion error on test data but also leads to misleading results when examining
class-wise or instance-wise performance (Li et al., 2022b).
Severalmethodstargetmulti-classcalibrationwithclass-dependenttrans-
formations, including Dirichlet calibration (Kull et al., 2019), matrix scaling
anditsregularizedvariants, andrelatedapproaches (Zongetal.,2024; Le Coz
et al., 2024; Zhao et al., 2021; Valk and Kull, 2023). These methods can, in
principle, apply different corrections across classes via a fullc×ctransfor-
mation. However, they are fit by minimizing an aggregate calibration loss
(e.g., negative log-likelihood or expected calibration error) over the whole
validation set rather than a class-specific objective, so they do not explic-
itly enforce that each class’s calibrated confidence matches that class’s true
performance; correcting class imbalance is not their stated goal.
1.2. Contributions
We address these open challenges with MOVAL, a new MOdel eVALu-
ation framework, benchmark, and deployable tool for assessing robust and
comprehensive model performance under domain shifts without the need for
manual labels. Specifically, we propose to enhance confidence score-based
approaches through class-wise calibration, which aligns confidence estimates
with performance metrics using class-specific parameters. This not only im-
proves accuracy estimation by reducing bias between classes but also nat-
urally extends confidence-based methods to the estimation of other met-
rics, including F1-Score, sensitivity, precision, and AUC. To our knowledge,
MOVAL is the first benchmark to evaluate how well confidence scores esti-
matemetricsbeyondaccuracy. Ratherthanintroducingafundamentallynew
calibration algorithm, our contribution lies in systematically unifying and
extending existing calibration, confidence-score, and ensemble ideas across a
broader range of metrics and tasks than prior work.
MOVAL is the first unified confidence score-based estimation framework
applicable to tasks beyond classification—including 2D and 3D segmenta-
4

tion; existing works are primarily limited to classification. We systemically
extend various confidence scores—beyond MCP—to the problem of perfor-
mance estimation. This includes scores like Entropy (Steinhardt and Liang,
2016), Doctor (Granese et al., 2021), and Energy (Liu et al., 2020b), which
were designed for identifying model failure but have not been extensively
discussed in the context of performance estimation. Importantly, we find
that an ensemble of multiple confidence scores provides the most robust and
accurate performance estimation. We provide this as a ready-to-use tool and
anticipate that practitioners will integrate it into their existing deployment
pipelines as a standard procedure 1. MOVAL does not require validation
data at the inference stage, impose assumptions on the tasks, or rely on ad-
ditional regression models, making it lightweight, flexible, and reproducible.
Through experiments on six tasks across 6,572 test settings, MOVAL out-
performs state-of-the-art methods in several areas, reducing estimation error
by 43% in real-world classification tasks and by over 50% in segmentation
tasks. Additionally, it provides detailed indicator results at the class-wise,
instance-wise, and pixel-wise levels.
We presented our preliminary results at MICCAI 2022 (Li et al., 2022b),
which mainly focused on the discussion of class-wise calibration for perfor-
mance estimation, where it was shown to outperform class-wise calibration
baselines such as vector scaling. Building on that, this paper further dis-
cusses: 1) the estimation of metrics other than accuracy, 2) estimation for
2D and 3D segmentation tasks, 3) estimation with different confidence scores
and their ensemble with additional evidence, and most importantly, 4) the
development of an open-source tool for the community to enable the safe
deployment of machine learning models.
2. Preliminaries: Confidence-Based Model Evaluation
2.1. Problem Setup
Inthecontextofc-classimageclassification, ourgoalistoestablishamap-
ping between the image spaceX ⊂Rd and the label spaceY={1,2, . . . , c}.
This framework can be extended to segmentation tasks by assuming that an
image patchx i is sampled fromX, withy i ∈ Yrepresenting the label of the
central pixels.
1https://pypi.org/project/moval/
5

We assume that two labeled image sets,DT r={(x i, yi)}I i=1 andD V =
{(xi, yi)}N i=1, drawn from the same source domain, are available for model
training and validation. Once trained, the model is applied to a target do-
mainD T e, where the distribution differs from the source domain, a com-
mon scenario in real-world applications. Our goal is to estimate its perfor-
mance, including accuracy, F1-Score, sensitivity, precision, and AUC, on the
target domain to support decision-making when only a set of test images
DT e={x T e i }M i=1 is available without any ground truth.
We propose MOVAL, a framework for estimating model performance
under domain shifts without requiring ground truth labels, specifically for
modern machine learning models like convolutional neural networks (CNNs).
MOVAL leverages logits (pre-softmax outputs) to estimate metrics across the
dataset. To ensure these probabilities are useful for performance estimation
under domain shifts, they are adjusted to match real metrics on a labeled
validation set from the source domain.
After training a neural networkfon the training datasetD T r, we aim
to develop a calibration model based on its performance on the validation
datasetD V ={(x i, yi)}N i=1. Specifically, given an input samplexi from the
validation set, the network outputf(xi)(i.e., logits) is obtained. Our ob-
jective is to minimize the following equation based on the validation dataset
with respect to the parameters in the MOVAL frameworkM:

M  {f(x i)}N i=1  − C  {(f(x i), yi)}N i=1 

,(1)
whereCrefers to the calculation of a metric that evaluates the model’s perfor-
mance across the entire labeled validation dataset. In contrast,Mestimates
these metrics based solely on the network outputs and

 ·

 refers to a desired
measurement of the gap, such as L1 distance. After optimization,Mcan be
applied directly to any test dataset, and we expect the estimated metrics to
offer more accurate insights into performance, particularly in the presence of
domain shifts.
MOVAL maps a set of logits to the final metrics through three key pro-
cedures: confidence score computation, model calibration, and metric calcu-
lation (Fig. 2b). To enable the calibration process, a tunable parameter is
typically added to the confidence score computation. Different calibration
techniques, such as Temperature Scaling (TS) (Guo et al., 2017), Differences
of Confidences (DoC) (Guillory et al., 2021), and Average Thresholded Con-
fidence (ATC) (Garg et al., 2022), define this parameter in distinct ways.
6

MOVAL extends these methods by altering the optimization objectives on a
per-class basis—CandMcalculate the metric for each class individually, ap-
plying class-specific parameters. This not only enhances accuracy estimation
under class imbalance but is also a key step in expanding the MOVAL frame-
work to metrics beyond accuracy and tasks beyond classification—areas that
have been largely unexplored.
MOVAL’s flexibility makes it more effective for supporting deployment
decisions for machine learning models, by making the trade-offs among differ-
ent performance metrics explicit. For example, in brain lesion segmentation
from MRI data, accuracy alone is insufficient. To properly evaluate segmen-
tation performance, tracking the F1-Score and focusing on pixel-level insights
is critical. If minimizing missed lesions is a priority, sensitivity estimation is
essential. Alternatively, when assessing post-processing techniques aimed at
reducing false positives without significantly affecting overall performance,
precision becomes the most appropriate metric to track.
2.2. Accuracy Estimation
The confidence score indicates the likelihood that the predicted label is
correct and can estimate accuracy for a specific dataset. We first describe
a general accuracy estimation framework based on MCP, which aligns well
with existing confidence-based methods.
Given an inputx i, the trained modelfgenerates the output logitz i =
f(x i)∈R c. The predicted probability vectorpi is then computed by apply-
ing the softmax function toz i, wherep ij =σ(z i)j = ezij Pc
j=1 ezij for thej’th
class. The predicted class labely ′ i corresponds to the class with the high-
est probability, given byy′ i = argmaxj(pij). The confidence scoreq i for this
sample, modeled by MCP, can be calculated asqi = maxj(pij).
The confidence score is a number ranging from 0 to 1; the higher the num-
ber, the more likely the sample is correctly classified. Ideally, we want the
confidence to have quantitative meaning that informs the decision-making
process. Specifically, for the entire validation datasetDV, we calculate the
average confidence withα′ = 1 N PN i=1 qi, and expect it to reflect the real accu-
racy. In practice, we can apply a similar procedure to the test dataset under
domain shiftsD T eand obtain the estimated accuracy asα′(T e)= 1 M PM i=1 qT e i
(Fig. 1).
However, directly computing confidenceqi over the softmax function for
estimation can be problematic as the predicted probability cannot reflect
7

Deployment with test set
Performance estimation w/ calibrated confidence scores
𝒟!"=𝒙#!" #$% &
𝒙#!" #$% &
Calibrated Probability$𝒑# !" #$% &
Estimate
𝑓 	#$% & 𝛼′(!") 𝛼!"
Optimization with validation set𝒟)=(𝒙#,𝑦#)#$% *
Pre-calibrated model Calibrated model
𝛼′=1 𝑁0 #$% * max+ (𝑝#+) 𝛼)=1 𝑁0 #$% * 𝟙(argmax + (𝑝#+)=𝑦#)
Accuracy Estimation Real Accuracy
𝛼′=1 𝑁0 #$% * max+ (̂𝑝#+)
Calibrated Accuracy Estimation
𝒙##$% *
Calibrated Probability$𝒑##$% *
Match
𝑓 	#$% * =𝛼)𝛼′𝒙##$% *
Probability𝒑##$% *
Not
match
𝑓 	#$% * 𝛼)𝛼′≠	#$% *
Logits𝒛##$% *
Φ′+= 2∑#$% *𝟙#+̂𝑝#+ ∑#$% *𝟙#++∑#$% * ̂𝑝#+
F1-Score Estimation
𝜌′+=
∑#$% *𝟙#+̂𝑝#+
∑#$% * ̂𝑝#+
Sensitivity Estimation
𝜋′+=
∑#$% *𝟙#+̂𝑝#+
∑#$% *𝟙#+
Precision Estimation
Λ,+=B -
%
𝑇𝑃𝑅′+𝑡𝑑(𝐹𝑃𝑅′+(𝑡))
AUC Estimation
a b
c d
Figure 1: Detailed descriptions of the confidence calibration process. Herep ij denotes
the raw (uncalibrated) softmax probability that unitibelongs to classj, whereiindexes
a sample for classification and a pixel/voxel for segmentation, assuming a single volume
is under consideration; after calibration,pij is replaced by the calibrated probabilityˆpij
used to compute all reported metric estimates.(a): Based on the model probabilities
pi, multiple performance metrics can be estimated. As we illustrate with the example
of accuracy, vanilla model probabilities are well known to be overconfident. Therefore,
the estimation is prone to being too optimistic and not accurate.(b): The calibration
process adjusts the probabilities such that the estimation aligns with the real metrics on
the validation dataset.(c): The same principle can be applied to estimating other group-
wise metrics.(d): The calibrated probabilities are expected to produce more accurate
estimations when exposed to domain shifts.
the real accuracy with modern neural networks (Guo et al., 2017). There-
fore, we need to adjust the confidence to obtain the modified confidence
ˆqi, a process commonly known as model calibration. To achieve this, ad-
ditional parameters are introduced into the confidence calculation process,
enabling fine-tuning. While methods like TS, DoC, and ATC define these
parameters differently, they all share the same optimization function. Specif-
ically, a common approach is to use the validation accuracy, defined as
αV = 1 N PN i=1 1(y ′ i =y i)2, as a surrogate objective forα ′ to find the solu-
21is an indicator function that equals 1 when the underlying criterion is met and 0
otherwise.
8

tion (Elsahar and Gallé, 2019; Guillory et al., 2021; Garg et al., 2022). Sub-
sequently, the same calibration process is applied to the test dataset, with
the expectation that the estimation results using the calibrated confidence
ˆqT e i will be more accurate.
a
Validation
Out-Domain
Test
Predicted Class
Maximum Class
Probability (MCP)
Temperature
Scaling (TS) MCP
Class Specific (CS)
TS MCP
c
Out-Domain TestValidation
Sensitivity TPFN
VanillaTSCS TS
Class
21.415.9 0.0
0
1
2
3
4
5
6
7
8
9
-25025-25025-25025
VanillaTSCS TS
Class
29.016.0 7.5
0
1
2
3
4
5
6
7
8
9
-25025-25025-25 025
Estimation Gap Estimation Gap
AUC
Estimation Gap
0
1
2
3
4
5
6
7
8
9
 Class
-5    0    5-5    0    5-5    0    5
Estimation Gap
2.2 1.4 0.5 2.9 1.4 0.9
0
1
2
3
4
5
6
7
8
9
 Class
-10010-10010-10010
VanillaTSCS TSVanillaTSCS TS
b
Accuracy Mean Confidence Estimation Gap (width ∝ magnitude)
0
1
2
3
4
5
6
7
8
9
0
1
2
3
4
5
6
7
8
9
Predicted Class
Validation
Out-Domain
Test
PrecisionTPFP
Class
20.026.321.3
-50050
0
1
2
3
4
5
6
7
8
9
-50050-50 050
Class
26.928.922.6
0
1
2
3
4
5
6
7
8
9
-50050-50 050-50050
Estimation Gap Estimation Gap
VanillaTSCS TSVanillaTSCS TS
F1-Score TPFPFN
Class
25.312.20.0
0
1
2
3
4
5
6
7
8
9
-25025-25025-25025
Class
34.417.4 5.5
0
1
2
3
4
5
6
7
8
9
-25025-25025-25025
Estimation Gap Estimation Gap
VanillaTSCS TSVanillaTSCS TS
MCP
TS MCP
CS TS MCP
MOV AL
Ensemble
MOV AL
Ensemble
0.2             0.4             0.6             0.8             1.0 0.2             0.4             0.6             0.8             1.0 0.2             0.4             0.6             0.8             1.0 0.2             0.4             0.6             0.8             1.0 0.2                    0.4                    0.6                    0.8                    1.0
Out-Domain TestValidation Out-Domain TestValidation Out-Domain TestValidation
MCP
TS MCP
CS TS MCP
MOV AL
Ensemble
Figure 2: Class-wise calibration and multi-metric estimation with MOVAL. We show an
estimation example on CIFAR10-LT, where sample counts decrease from class 0 to class
9.(a): MOVAL facilitates class-wise calibration with class-specific parameters. Class-
wise calibration allows for the alignment of estimated class-wise metrics and the true
underlying counterparts, which can mitigate model biases caused by class imbalance.(b):
Overall accuracy estimation across different methods. By aggregating multiple confidence
scores, MOVAL Ensemble achieves the most accurate results.(c): In addition to accuracy
estimation, which is provided by existing methods, class-wise alignment enables MOVAL
to estimate class-wise metrics, thus providing a comprehensive evaluation.
We argue that existing confidence-based accuracy estimation methods
struggle to generalize effectively to imbalanced datasets, which are common
in medical image classification and segmentation. Prior studies have demon-
strated that models trained on imbalanced data are prone to misclassifying
minority class samples as belonging to the majority class, but rarely the re-
verse (Li et al., 2020). As a result, these models often achieve high overall
accuracy but are underconfident in predicting minority class samples, while
being overly confident for majority class predictions (Fig. 2c). Existing cali-
bration methods apply a uniform probability-adjustment procedure across all
9

classes. This uniformity leads to higher estimation error for minority-class
samples (e.g., TS MCP exhibits substantial estimation error on minority
classes, as shown in Fig. 2a), which in turn limits their ability to generalize
effectively (Fig. 2b). To address this, we introduce class-specific parameters
into the performance estimation framework using adaptive optimization, re-
ducingtheconfidencebiasofneuralnetworkstowardminorityclasses(Fig.3).
Other group-wise metrics, such as sensitivity, precision, F1-Score and AUC,
can be formulated similarly. The details are provided in the Suppl. Note.
3. Proposed Method: MOVAL
The MOVAL model consists of three key components. 1) Confidence
Score Calculation: Given the network logitsz i, the confidence scoreq i is
computed. 2) Model Calibration: The confidence score is adjusted to align
estimated metrics with target metrics, producing the calibrated confidence
scoreˆqi fromq i. 3) Metrics Computation: Usingˆqi, evaluation metrics for the
entire dataset are computed, including calibrated probabilitiesˆpi for metrics
beyond accuracy.
In following sections, we will present our main contribution, class-wise
model calibration, using MCP for accuracy estimation. Subsequent sections
will explore its extension to various metrics and types of confidence scores.
Original/Class-Specific Temperature Scaling (TS)
!(𝒛!/%∗)#
𝑧’(
𝑧’)
"𝑞’ !(𝒛!/%#∗)#"𝑞’ 𝑧’(
𝑧’)
Global temperature 𝑇∗ Class-Specific temperature 𝑻∗={𝑇" ∗,𝑇# ∗}
Original/Class-Specific Difference of Confidences (DoC)
*+
𝑝’(
𝑝’)
"𝑞’ *+#
𝑝’(
𝑝’)
"𝑞’
Global difference 𝑑 Class-Specific difference 𝒅={𝑑",𝑑𝟐}
Original/Class-Specific AverageThresholdedConfidence (ATC)
𝟙[%!&’#∗]"𝑞’ 𝟙[%!&’∗]"𝑞’
Global threshold 𝑡∗ Class-Specific threshold 𝒕∗={𝑡"∗,𝑡#∗}
Original/Class-Specific Temperature Scaling AverageThresholdedConfidence (TS-ATC)
&𝑞’ 𝟙[%!&’#∗] "𝑞’ 𝟙[)%!&’∗] "𝑞’!(𝒛!/%∗)#
𝑧’(
𝑧’)
!(𝒛!/%#∗)#
𝑧’(
𝑧’)
Global temperature 𝑇∗ Global threshold 𝑡∗ Class-Specific temperature 𝑻∗={𝑇" ∗,𝑇# ∗} Class-Specific threshold 𝒕∗={𝑡"∗,𝑡#∗}
𝑝’)
𝑝’( 𝑝’(
𝑝’)
Expected AccuracyLogit 𝑧’,
Probability 𝑝’, Calibrated Confidence Score "𝑞’
Calibration process
&𝑞’
a
b c
d
Figure 3: We extend existing model calibration methods to class-specific variants by intro-
ducing parameters for different classes. This enables class-wise calibration and improves
estimation accuracy, especially when the model is trained with class-imbalanced data.
10

3.1. Class-Specific Temperature Scaling
The TS method is one of the most widely used calibration methods (Guo
et al., 2017; Hinton et al., 2015). It introduces a temperature parameter to
rescale the logits, withq i = max j(σ(z i/T) j). To find the value ofTthat
makes the estimated accuracy closely approximate the true accuracy, the
optimal temperatureT ∗ is determined using the validation datasetDV as:
T ∗ = argmin
T

 1 N NX i=1 qi −α V

 = argmin T

 1 N NX i=1 max j (σ( zi T )j)−α V

. (2)
To enable class-specific calibration, we extend the temperature parameter
to a vectorTwithcelements, where thej’th elementT j corresponds to
thej’th class. The calibrated confidence score is then computed asq i =
maxj(σ(z i/Ty′ i)j), with the optimalT∗ j determined by:
T ∗ j = argmin
Tj

 1 Nj NX i=1 1 ijqi −α V j

 = argmin Tj

 1 Nj NX i=1 1 ij max k (σ( zi Tj )k)−α V j

,
(3)
whereN j = PN i=1 1 ij andα V j is the accuracy for thej’th class on the vali-
dation set which is calculated asαV j = 1 Nj PN i=1 1 ij1(y ′ i =y i). This approach
ensures that the optimizedT∗ results inˆqi aligning with the class-wise accu-
racy (Fig. 3a).
3.2. Class-Specific Difference of Confidences
The DoC method (Guillory et al., 2021) adjustsq i by subtracting the
differenced=α ′ −α V, which is the gap between the real accuracyαV and
the estimated resultsα′:
ˆqi =q i −d.(4)
A clipping operation between 0 and 1 may be necessary to ensure that the
calibrated confidence is properly normalized. We introduce a class-specific
DoC method, where we define a difference vectordwithcelements, with the
j’th elementd j representing the difference for thej’th class. The class-wise
calibrated confidence scoreˆqi is then computed as follows:
11

ˆqi =q i −d y′ i,(5)
whered j = 1 Nj PN i=1 1 ijqi −α V j is the difference between the average predicted
probability for samples predicted that they belong to classjandα V j . This
approach insulates the probabilities of samples predicted as minority classes
from the influence of majority classes, reducing bias (Fig. 3b).
3.3. Class-Specific Average Thresholded Confidence
The ATC method (Garg et al., 2022) is a heuristic yet effective approach
for estimating model performance, consistently delivering top results across
multiple robustness evaluation benchmarks (Garg et al., 2022; Baek et al.,
2022). It predicts accuracy by calculating the proportion of samples with
qi values exceeding a learned thresholdt. The thresholdtis determined as
follows, and the confidence score is then calculated asˆqi =1(q i > t∗), where:
t∗ = argmin
t

 1 N NX i=1 1(q i > t)−α V

. (6)
In the context of ATC,ˆqi is no longer a standard calibrated confidence
score but instead a discrete value∈ {0,1}. Despite this, it can still be used
foraccuracyestimationaspreviouslydescribed. Forclass-specificcalibration,
we propose learning a set of thresholds represented by the vectort, which
hascelements, one for each class. Thej’th element is determined by:
t∗ j = argmin
tj

 1 Nj NX i=1 1 ij1(q i > tj)−α V j

. (7)
We then calibrate the probabilities asˆqi =1(q i > t∗ y′ i )based on the pre-
dictedclassy ′ i (Fig.3c). Thisapproachdiscretizestheprobabilitiesofsamples
predicted as different classes using distinct thresholdst∗ y′ i , effectively compen- sating for the bias introduced by class imbalance.
3.4. Class-Specific with Average Thresholded Confidence with Temperature
Scaling
Confidence scores can be first calibrated using TS before being applied in
the ATC process, referred to as TS-ATC (Garg et al., 2022). Specifically, the
confidence score is initially calibrated with TS to obtain˜qi, which satisfies
12

Eq. 2, and is then used in the ATC calibration process. By incorporating
our class-specific modifications to both TS and ATC, we similarly derive the
class-specific variant, CS TS-ATC (Fig. 3d).
3.5. Confidence Scores Calculation
In addition to MCP, various other confidence scores can be derived from
logitsz i, such as Entropy (Steinhardt and Liang, 2016), Doctor (Granese
et al., 2021), and Energy (Liu et al., 2020b). While these techniques have
not been extensively explored in the context of model evaluation, they have
demonstrated improved performance in related tasks like anomaly detec-
tion (Chandola et al., 2009) and failure detection (Bernhardt et al., 2022).
Therefore, we believe it would be valuable to extend the discussed model
calibration methods to incorporate these confidence scores. To achieve this,
Entropy and Doctor is calculated with:
qEntropy i = 1 + X
j
pij logc pij, q Doctor i =
P
j p2 ij −1P
j p2 ij .(8)
The calibration of these two confidence scores is straightforward since
they directly involvep ij in their computation. As a result, TS calibration
can be applied by adjustingTin the softmax process, wherepij =σ(z i/T) j.
In contrast, Energy is calculated as follows:
qEnergy i =Tlog X
j
ezij /T .(9)
It is important to note that we adjust the calculation to ensure alignment
with the typical requirements of confidence scores, where a higher value indi-
cates greater confidence. Additionally, we normalize the Doctor and Energy
scores usingmaxi qi andmin i qi3, then clip the values between 0 and 1 to give
them quantitative significance.
3.6. Calibration for Group-Wise Metrics
Aspreviouslydiscussed, calculatinggroup-wisemetricsrequirescalibrated
probabilities ˆpi. Thus, we need to derive ˆpi from the confidence score
3The calibrated confidence scores are normalized based on the range of uncalibrated
confidence scores rather than calibrated scores; otherwise, the calibration process would
not affect the estimation results.
13

ˆqi, which involves filling in the probabilities for non-maximum classes. To
achieve this, we propose two approaches: 1) Generate the probabilities as
if they originated from the TS process. Specifically, we find the parame-
ter that best fits the maximum probabilities (i.e., findT ∗ such thatˆqi =
maxj(σ
 zi
T ∗

j)) on a per-case basis and use it to estimate the non-maximum
probabilities. 2) Equally distribute the remaining probability across the non-
maximum classes, i.e., 1−qi c−1 4. Initial experiments suggest that neither solu-
tion consistently outperforms the other. We adopt the second approach for
all experiments, as it is more efficient.
Since the class-specific parameters may influence the group-wise metrics
estimation of other classes, we optimize each parameter sequentially, starting
with the class that has the highest number of predictions and proceeding in
descending order. This approach helps minimize the overall estimation error
on the validation dataset.
3.7. MOVAL Ensemble
Model ensembles, which average the probabilities from multiple models
before making decisions, can effectively enhance model performance (Kam-
nitsas et al., 2018). We apply this concept to our task, referring to it as
MOVAL Ensemble. In this approach,Ldifferent models are calibrated sep-
arately, each yieldingˆp(l) i . The ensemble probabilities are then computed as
follows:
ˆpEnsemble i = 1 L
LX
l=1
ˆp(l) i ,(10)
which are later used on test data to estimate metrics. We select different
combinations for various tasks, summarized in Extended Table E.19.
3.8. Performance Estimation for Segmentation Tasks
We propose extending confidence-based model evaluation methods to seg-
mentation. Unlike classification, segmentation evaluation emphasizes group-
wise metrics that compare volumes rather than the entire dataset.
To this end, we slightly adjust the notation and denote the validation
dataset as consisting ofZsegmentation cases, represented asDV ={S z}Z z=1,
4For calibrated probabilities under ATC, the non-maximal values are simply set to 0.
14

whereS z contains all the training pairs for casez, with a total ofnpixels.
This is defined asSz ={(x zi, yzi)}n i=1, wherex zi is an image patch sampled
from casezandy zi is the ground truth class of its central pixel. We denote
pzij as the predicted probability of samplex zi for thej’th class, and its
calibrated version asˆpzij (derived from the calibrated confidence scoreˆqzi).
The estimated F1-Score is then computed using the predicted probabilities,
analogous to the common soft DSC loss (Milletari et al., 2016). Specifically,
the real F1-Score ofD V for thej’th class, denoted asΦ V j , is estimated as
follows:
Φ′ j = 1 Z
ZX
z=1
2 Pn i=1 1 zij ˆpzijPn
i=1 1 zij + Pn i=1 ˆpzij ,(11)
where now1 zij =1(argmax k(pzik) =j). Notably, we do not calibrate the
background class, as its performance remains consistently high due to the
relative ease of classifying the majority of background samples. Adjusting
the estimation to match this performance is difficult and can interfere with
the calibration of foreground classes, as optimizing for the background class
was found to destabilize the overall results.
3.9. Group-Wise Calibration
Since our approach performs calibration on a per-class basis, a natural
concern is the requirement for a sufficient number of samples in each class,
especially for minority classes. To address this limitation, we introduce a
group-wise calibration strategy that allows class-wise calibration methods to
operateatthegrouplevel, sharingclass-specificparametersacrossclassesand
aligning metrics across multiple predicted classes. This approach, also used
in (Li et al., 2024) for a different application, reduces reliance on validation
datasets and proves more robust to various advanced training strategies.
As an example, we consider the CS TS of accuracy based on MCP
(i.e., Eq. 3). For group-wise calibration, we assume a unique parameter
eTfor calibrating all the samples belonging to a batch ofBclasses,b=
[b1,· · ·, j,· · ·, bB]⊺. The construction ofbcan be user-defined, but by de-
fault, the classes are grouped based on the number of samples predicted as
classj, i.e.,N j. Recall that the accuracy for thej’th class can be estimated
asα ′ j = 1 Nj PN i=1 1 ij maxk(σ  zi eT  k ). The group-wise calibration of CS TS is optimized with:
15

eT ∗ = argmin
eT

 X
j∈b
Nj(α′ j −α V j )

.(12)
The estimation of other metrics (e.g., replacingα′ j withΦ ′ j for F1-Score
estimation) or the use of alternative estimation methods can be done in very
similar ways. Notably, ifBequals 1, group-wise calibration is equivalent to
the vanilla CS calibration we introduced beforehand; ifBequals the class
numberCwhen estimating accuracy, it is equivalent to the original class-
agnosticcalibration. Allresultsinthispaperarereportedwithoutgroup-wise
calibration unless specified.
3.10. Optimization
WeoptimizetheparametersoftheMOVALmodelsusingbound-constrained
minimization algorithms. By default, we apply the Nelder-Mead simplex al-
gorithm (Gao and Han, 2012) through the SciPy toolbox (Virtanen et al.,
2020). The parameters are initially set to 1.0, and to improve the robustness
of the optimization, we perform 5 additional initializations with different
starting points if the initial optimization results are unsatisfactory. In prac-
tice, we optimize the class-specific parameter for classjonly when there are
both predicted instances of classjand ground truth instances labeled as class
jin the validation dataset. Otherwise, optimization would be meaningless.
4. Experiments
4.1. Experimental Setup
In our experiments, we first train a classifierfwithD T r, then we make
predictions onDV and optimize the calibration model based on model output
and the validation labels. Afterwards, we evaluate our model onDT eand
estimatethequalityofthepredictedresultsbasedonthepre-softmaxnetwork
outputsf(x T e i ).
Wetraintheclassificationandsegmentationmodelsusingawell-established
process based on ResNet (He et al., 2016) and U-Net (Ronneberger et al.,
2015), following previous successful related efforts (Isensee et al., 2021; Rus-
sakovskyetal.,2015;Marrakchietal.,2021). Detailedtrainingconfigurations
are provided in Suppl. Note.
16

4.2. Datasets
CIFAR10-LT.We resample the CIFAR10 training set (Krizhevsky et al.,
2009) using an exponential class ratio to create an imbalanced dataset with
c= 10classes and an imbalance ratio of 100, following (Cao et al., 2019).
The validation and test sets remain unchanged. To introduce domain shifts,
we apply 95 synthetic corruptions from CIFAR10-C (Hendrycks and Diet-
terich, 2019a). Dataset details are provided in Extended Fig. C.12, with
visualizations shown in Extended Fig. C.13.
CIFAR100-LT.We adopt similar strategies to create an imbalanced CI-
FAR100 dataset, which also has an imbalance ratio of 100. This dataset has
c= 100classes.
Skin lesion classification.The skin lesion datasets havec= 7classes.
We randomly select 70%of the data from HAM10000 (Tschandl et al., 2018)
for the training dataset and reserve the rest for validation. We addition-
ally collect 7 publicly available skin lesion datasets which were collected in
different institutions including BCN (Combalia et al., 2019), VIE (Rotem-
berg et al., 2021), MSK (Gutman et al., 2016), UDA (Gutman et al., 2016),
OTH (Rotemberg et al., 2021), D7P (Kawahara et al., 2018) and PH2 (Men-
donça et al., 2013) mainly following (Yoon et al., 2019). The split is per-
formed at the dataset level: training and validation use HAM10000 exclu-
sively, and each of the seven test datasets is an independently collected cohort
from a different institution, with no patient or image overlap with the source
data.
BrainlesionMRIsegmentation.Weevaluatetheproposedmethodswith
brain lesion segmentation based on T1-weighted MR images using data from
Anatomical Tracings of Lesions After Stroke (ATLAS) (Liew et al., 2022).
This dataset is for binary segmentation (c= 2), with highly imbalanced
classes. Images are registered to the MNI152 template (Brett et al., 2002)
with a spacing of1.00mm×1.00mm×1.00mm.
This dataset contains 653 samples collected using 13 different scanners
of different field strengths and manufacturers. The split is performed at
the scanner level: all 88 cases from the chosen scanner are used exclusively
for training and validation, and the remaining 565 cases, acquired on the
other 12 scanners, are used exclusively as target test data, with no patient
or scanner overlap between source and test. We create synthetic domains
shifts by applying 83 distinct transformations, including spatial, appearance
and noise operations to the validation data. We show some visualization
of this dataset in Extended Fig. C.14. The detailed dataset statistics and
17

transformation implementation are summarized in Extended Table E.4 and
Extended Table E.20.
Prostate MRI segmentation.We also evaluate on the task of cross-site
prostate segmentation based on T2-weighted MR images following (Liu et al.,
2020a). This is also a binary segmentation task (c= 2). We resample the
images to a common resolution of0.80mm×0.80mm×1.50mm.
We use 30 cases collected by (Bloch et al.,2015) as the source domain. For
the target domain, we utilize five datasets described in (Lemaître et al., 2015;
Bloch et al., 2015; Litjens et al., 2014), which were collected from various
institutions using scanners of different field strengths and manufacturers.
As with the brain lesion data, the split is at the institution/scanner level.
Synthetic domain shifts are generated using the same 83 transformations
applied to brain lesions.
Cardiac MRI segmentation.We utilize cardiac MR images from the
Multi-Centre, Multi-Vendor, andMulti-DiseaseCardiacSegmentation(M&Ms)
Challenge (Campello et al., 2021). The task is to segment the images into
three classes (c= 3), including the left and right ventricle cavities and the
left ventricle myocardium. The image volume is anisotropic and is therefore
evaluated slice by slice, that is, in 2D. We resample the images to a common
resolution of1.25mm×1.25mm×10.00mm.
This dataset contains short-axis cardiac MR images from 345 samples
across5differentsites. Followingtheclinicalprotocol, wesegmenttwoframes
of the MRI, including the end-diastolic (ED) and end-systolic (ES) phases,
totaling 690 images. We use data from one site (190 images) as the source
domain and validate the trained model on other domains and synthesized
domain shifts. The split is again at the site level. Compared with synthesized
domain shifts in 3D segmentation, we exclude those that operate in the z-axis
due to its anisotropic nature, resulting in 65 test conditions. We report the
average estimation error across all three classes.
4.3. Class-Wise Performance Alignment
We first demonstrate the effectiveness of class-wise calibration by extend-
ing existing methods including TS, DoC, ATC and TS-ATC (which is a
combination of TS and ATC) to the variants where performances are aligned
in class-wise manner with class-specific (CS) parameters. These proposed
variants are denoted as CS TS, CS DoC, CS ATC and CS TS-ATC, respec-
tively.
18

Classification (3 Tasks w/ 197 conditions)a
b
Sensitivity
F1-Score
Accuracy
Precision Estimation
AUC Estimation
Van
Vanilla
Provided by MOV AL
Existing Standards: 4.9
Color: Category
Existing Methods
Size: MAE
MOV AL Best: 3.1
Accuracy Estimation
Van
Vanilla
Provided by MOV AL
Existing Standards: 20.6
Color: Category
Existing Methods
Size: MAE
MOV AL Best: 14.8
Sensitivity Estimation
F1-Score Estimation
Precision
AUC
****㌵-value≤ 10 !"
Provided by MOV AL
Existing Standards: 10.3
Color: Category
Existing Methods
Size: MAE
MOV AL Best: 8.1
Provided by MOV AL
Existing Standards: 27.3
Color: Category
Existing Methods
Size: MAE
MOV AL Best: 24.1
Vanilla
Precision Estimation
b
Vanilla
Vanilla
Figure 4: Class-wise calibration improves the estimation results for all metrics in classi-
fication tasks.(a): The mean absolute error (MAE) between real metrics and estimated
results based on different estimation methods for classification tasks. The size of the cir-
cles represents the MAE, with smaller circles indicating better performance. We report
the average MAE for various tasks here.(b): MAE comparison between the original es-
timation methods and our proposed class-specific variants for classification tasks. Paired
t-tests were used for statistical analysis.
We use CIFAR10-LT to illustrate the calibration process for CS TS, as
shown in Fig. 2b. TS adjusts confidence based on validation performance to
align global accuracy with global confidence. However, this is achieved by
sacrificing class-wise performance, where the majority classes remain over-
confident (i.e., the mean confidence is higher than the actual accuracy), while
the minority classes are underconfident.
We evaluate the estimation results across 3 classification tasks, cover-
ing 197 types of domain shifts, which include both synthetic shifts for CI-
FAR (Krizhevsky et al., 2009) and real-world acquisition shifts for skin lesion
classification where images are gathered from various sites (Tschandl et al.,
2018) (Fig. 7a, Extended Fig. C.17a). To note, we resample the CIFAR
19

training dataset to create a long-tailed distribution, making the evaluation
more realistic, as this reflects the nature of real-world datasets (Liu et al.,
2019; Cao et al., 2019). The models are based on a standardized version
of ResNet (He et al., 2016). In order to evaluate the estimation results, we
calculate the Mean Absolute Error (MAE) between the predicted and the
real accuracy and report the overall results as the mean MAE across three
tasks (Fig. 4a). Our proposed CS variants significantly improve the estima-
tion results, reducing the overall MAE from 6.64 to 5.81 (Fig. 4b, Extended
Fig. C.17b, paired t-test,p= 1.01×10 −48). Specifically, the CS variants
reduce the MAE for TS from 7.33 to 7.06 (p= 0.02), from 10.40 to 9.76 for
DoC (p= 1.71×10 −9), from 4.38 to 3.50 for ATC (p= 6.42×10−15) and from
4.45 to 2.93 for TS-ATC (p= 1.94×10−42). These results clearly highlight
the importance of addressing class imbalance in the design of performance-
prediction methods to mitigate biases introduced by the data.
Another advantage of class-wise alignment is its robustness to label shifts
in test datasets, as it tracks performance separately for each class. This
is especially beneficial when there are more samples from minority classes
at test time. For example, when deploying the model on the CIFAR10-
LT dataset, which includes only the two most minority classes, CS variants
can reduce the MAE from 27.0 to 21.7 (Extended Table E.7, paired t-test,
p= 2.40×10 −120). Additionally, it is clear that the proposed CS variants
provide more accurate performance estimation on the subsets defined by the
model’s predictions (Fig 2b).
4.4. Multi-Metric Estimation
The MOVAL framework allows to estimate other metrics beyond accu-
racy, delivering a thorough assessment based solely on the network outputs.
Those metrics like the F1-Score are typically calculated on a per-class basis.
Consequently, we compute the MAE for each individual class and report the
MAE for a case along with its average MAE across all classes (Extended
Fig. C.16a).
Class-wise performance alignment naturally suits the estimation of group-
wise metrics, as demonstrated with CIFAR10-LT in Fig. 2a. Existing cali-
bration methods focused on accuracy can reduce overconfidence and, in turn,
lower estimation error for group-wise metrics (NannyML), but they do not
achieve optimal results for those metrics. Although our CS variants may
not fully align performance for precision and AUC, they greatly enhance
calibration, thereby reducing estimation errors during testing.
20

Similarly to the accuracy estimation evaluation, we report results across
three classification tasks (Fig. 4a). Our CS variants show clear advantage
than existing metrics (Fig. 4b, Extended Fig. C.17b), reducing the MAE
from 21.25 to 13.95 for F1-Score (paired t-test,T(3151) = 79.16, p≤10−4),
from 20.40 to 14.96 for sensitivity (T(3151) = 46.89, p≤10−4), from 31.23
to 26.99 for precision (T(1575) = 64.76, p≤10−4), and from 9.19 to 6.04 for
AUC (p= 1.25×10 −125).
4.5. MOVAL for Segmentation Tasks
2D Segmentation (1 Task w/ 69 conditions)
DSC (F1-Score) Estimation
a 3D Segmentation (2 Tasks w/ 183 conditions)
DSC (F1-Score) Estimation
c
Sensitivity Estimation
Precision Estimation
Sensitivity Estimation
Precision Estimation
b d 2D Segmentation (1 Task w/ 69 conditions) 3D Segment ation (2 Tasks w/ 183 conditions)
MAE
MAE
****㌵-value≤ 10 !"
F1-Score Sensitivity Precision Accuracy AUC F1-Score Sensitivity Precision Accuracy AUC
Provided by MOVAL
Existing Standards: 7.0
Color: Category
Existing Methods
Size: MAE
MOVAL Best: 3.4
Provided by MOVAL
Existing Standards: 9.1
Color: Category
Existing Methods
Size: MAE
MOVAL Best: 7.7
Provided by MOVAL
Existing Standards: 3.1
Color: Category
Existing Methods
Size: MAE
MOVAL Best: 3.1
Provided by MOVAL
Existing Standards: 16.1
Color: Category
Existing methods
Size: MAE
MOVAL Best: 6.2
Provided by MOVAL
Existing Standards: 9.1
Color: Category
Existing Methods
Size: MAE
MOVAL Best: 5.1
Provided by MOVAL
Existing Standards: 14.8
Color: Category
Existing Methods
Size: MAE
MOVAL Best: 3.1
Vanilla Vanilla
Vanilla
VanillaVanilla
Vanilla
Figure 5: Class-wise calibration is even more crucial for segmentation tasks.(a, c):
MAE between real metrics and estimated results from different methods for 2D and 3D
segmentation tasks.(b, d): MAE comparison between the original estimation methods
and proposed class-specific variants for 2D and 3D segmentation tasks. Statistical tests
are conducted using paired t-tests.
21

b c
 3D F1-Score Estimation 3D Sensitivity Estimation 3D Precision Estimati on
MAE
Samples
MAE
Samples
Predicted Precision
MAE
Samples
Real F1-Score
Real Sensitivity
Predicted F1-Score Predicted Sensitivity
Real Precision
Van Van Van
Van Van Van
Baseline: MCP | Vanilla
Existing Standards: MCP | ATC
MOVAL Ensemble
Prostate Synthetic
Prostate Natural
y = x
Brain Lesion Synthetic
Brain Lesion Natural
Baseline: MCP | Vanilla
Existing Standards: MCP | TS-ATC
MOVAL Ensemble
Prostate Synthetic
Prostate Natural
y = x
Brain Lesion Synthetic
Brain Lesion Natural
Baseline: MCP | Vanilla
Existing Standards: MCP | TS
MOVAL Ensemble
Prostate Synthetic
Prostate Natural
y = x
Brain Lesion Synthetic
Brain Lesion Natural
Baseline: MCP | Vanilla
Existing Standards: MCP | ATC
MOVAL Ensemble
Mean
Baseline: MCP | Vanilla
Existing Standards: MCP | TS-ATC
MOVAL Ensemble
Mean
Baseline: MCP | Vanilla
Existing Standards: MCP | TS
MOVAL Ensemble
Mean
2D F1-Score Estimation 2D Sensitivity Estimation 2D Precision Estimati on
MAE
Samples
MAE
Samples
Predicted Precision
MAE
Samples
Real F1-Score
Predicted F1-Score Predicted Sensitivity
Real Sensitivity
Real Precision
Van Van Van
Baseline: MCP | Vanilla
Existing Standards: MCP | TS-ATC
MOVAL Ensemble
Cardiac Synthetic
Cardiac Natural
y = x
Baseline: MCP | Vanilla
Existing Standards: MCP | ATC
MOVAL Ensemble
Cardiac Synthetic
Cardiac Natural
y = x
Baseline: MCP | Vanilla
Existing Standards: MCP | Vanilla
MOVAL Ensemble
Cardiac Synthetic
Cardiac Natural
y = x
Baseline: MCP | Vanilla
Existing Standards: MCP | TS-ATC
MOVAL Ensemble
Mean
Baseline: MCP | Vanilla
Existing Standards: MCP | ATC
MOVAL Ensemble
Mean
Baseline: MCP | Vanilla
Existing Standards: MCP | Vanilla
MOVAL Ensemble
Mean
a
 Accuracy Estimation Sensitivity Estimation Precision Estimation F1-S core Estimation AUC Estimation
Real Accuracy
Predicted Accuracy
MAE
Real Sensitivity
Predicted Sensitivity
MAE
Real Precision
Predicted Precision
MAE
Real F1-Score
Predicted F1-Score
MAE
Real AUC
Predicted AUC
MAE
Samples
Samples
Samples
Samples
Samples
Van Van Van
Van
|Van
VanVan
Baseline: MCP | Vanilla
Existing Standards: MCP | TS-ATC
MOVAL Ensemble
CIFAR10-LT
CIFAR100-LT
Skin Lesion
y = x
Baseline: MCP | Vanilla
Existing Standards: MCP | ATC
MOVAL Ensemble
CIFAR10-LT
CIFAR100-LT
Skin Lesion
y = x
Baseline: MCP | Vanilla
Existing Standards: MCP | TS
MOVAL Ensemble
CIFAR10-LT
CIFAR100-LT
Skin Lesion
y = x
Baseline: MCP | Vanilla
Existing Standards: MCP | Vanilla
MOVAL Ensemble
CIFAR10-LT
CIFAR100-LT
Skin Lesion
y = x
Baseline: MCP | Vanilla
Existing Standards: MCP | TS-ATC
MOVAL Ensemble
Mean
Baseline: MCP | Vanilla
Existing Standards: MCP | ATC
MOVAL Ensemble
Mean
Baseline: MCP | Vanilla
Existing Standards: MCP | TS
MOVAL Ensemble
Mean
Baseline: MCP | Vanilla
Existing Standards: MCP | TS-ATC
MOVAL Ensemble
Mean
Baseline: MCP | Vanilla
Existing Standards: MCP | Vanilla
MOVAL Ensemble
Mean
Baseline: MCP | Vanilla
Existing Standards: MCP | TS-ATC
MOVAL Ensemble
CIFAR10-LT
CIFAR100-LT
Skin Lesion
y = x
Figure 6: Agreement between predicted and real metrics for different tasks. For each
subfigure: Top: Predicted and real label distribution. We benchmark MOVAL ensemble
(blue) against MCP baselines (light gray) and the best-performing existing method (dark
gray). Middle: Predicted versus real metrics. Each point represents the model’s perfor-
mance on unseen target data under specific conditions. Bottom: Histogram of MAE for
different estimation methods.(a): Classification tasks.(b): 2D segmentation tasks.(c):
3D segmentation tasks.
The MOVAL framework supports the evaluation of both 2D and 3D seg-
mentation tasks. It extends to semantic segmentation by treating it as pixel-
level dense classification. A key distinction between evaluating segmentation
and classification is that segmentation involves comparing 2D slices or 3D
volumes, rather than assessing the entire dataset. With this adjustment, all
the previously mentioned methods can be easily adapted for segmentation
tasks.
Weevaluate2DsegmentationonthetaskofcardiacMRI(Campelloetal.,
2021) segmentation and 3D segmentation on prostate MRI (Liu et al., 2020a)
and brain lesion MRI (Liew et al., 2022) segmentation. For all segmentation
tasks, we apply transformations as synthetic domain shifts (Extended Ta-
ble E.20) and collect images from different scanners to represent real domain
shifts. The models are built upon a standardized version of 3D U-Net (Ron-
22

neberger et al., 2015).
We present the evaluation results of the average MAE between real and
synthesized scenarios (Fig. 5a, Fig. 5c). We omit accuracy and AUC eval-
uations, as these metrics often approach 100%for segmentation tasks (Ex-
tended Fig. C.15c, Extended Fig. C.15d). Our CS variants demonstrate even
greater advantages over existing standards compared to classification results
(Fig. 5b, Fig. 5d). This may be due to previous model calibration methods
being heavily biased toward the background class, a consequence of class
imbalance.
We focus on evaluating the F1-Score (i.e., DSC), the most commonly
used metric for segmentation tasks (Fig 7c, Extended Fig. C.18a, Extended
Fig. C.18b). CS variants greatly enhance confidence-based estimation of
the F1-Score, lowering the MAE from 12.88 to 4.73 for 2D segmentation
(paired t-test,p= 1.03×10 −227) and from 15.41 to 4.69 for 3D segmentation
(T(2927) = 72.55,p≤10 −4). Similar conclusions also apply to sensitivity
and precision (Extended Fig. C.16b, Extended Fig. C.16c). For sensitivity,
CS variants decrease the MAE from 9.55 to 4.31 for 2D segmentation (p=
2.57×10 −145) and from 12.78 to 5.75 for 3D segmentation(p= 1.59×10−320).
For precision, they reduce the MAE from 11.25 to 9.36 for 2D segmentation
(p= 1.94×10 −47) and from 9.38 to 5.76 for 3D segmentation (p= 2.97×
10−29). Note that we exclude energy-based evaluation for precision due to
its consistently poor performance in segmentation tasks.
4.6. Confidence Scores Ensemble
MOVAL enhances existing model calibration methods by integrating con-
fidence scores beyond MCP and utilizing ensemble techniques for improved
results. While traditional model evaluation methods rely on MCP for its sim-
plicity and straightforward quantitative meaning, MOVAL advances this by
integrating other confidence scores, such as Entropy (Steinhardt and Liang,
2016), Doctor (Granese et al., 2021), and Energy (Liu et al., 2020b). These
confidence scores have shown enhanced outlier detection capabilities due to
their improved ability to capture information from non-maximum predictions
(Fig. 2a). Additionally, akin to model ensembles in discriminative models, we
investigate the ensemble of the best methods to deliver robust and effective
solutions.
We begin by investigating the discrepancies between different confidence
scores and estimation algorithms, as model ensembles are effective only when
the methods exhibit substantial diversity (Kamnitsas et al., 2018; Ganaie
23

a Classification (3 Tasks w/ 197 conditions) Accuracy Estimation
2D Segmentation (1 Task w/ 69 conditions) F1-Score Estimation
MAE
Estimation Algorithm
MAE
Estimation Algorithm
Classification (3 Tasks w/ 197 conditions) Performance Estimation
MAE
~
~
~𝑝-value>0.05
*𝑝-value≤0.05
**𝑝-value≤0.01
***𝑝-value≤10!"
****𝑝-value≤10!# Vanilla
Vanilla
c 3D Segmentation (2 Task w/ 183 conditions) F1-Score Estimation
MAE
Estimation Algorithm
Vanilla
b Confidence Score
Confidence Score
MCP
Energy
Entropy
Doctor
MOVAL
Ensemble
MCP
Energy
Entropy
Doctor
MOVAL
Ensemble
Figure 7: MOVAL Ensemble achieves state-of-the-art performance.(a, c): MAE com-
parison between proposed algorithms and existing standards (Best-performing existing
method versus MOVAL Ensemble, paired t-test,p= 1.05×10−7 for accuracy estimation
of classification tasks,p= 3.54×10 −4 for F1-Score estimation of 2D segmentation tasks,
p= 4.28×10 −27 for F1-Score estimation of 3D segmentation tasks, see the results of other
metrics in Extended Fig. C.16 and the results of individual datasets metrics in Extended
Fig. C.17 and Fig. C.18).(b): MAE comparison between estimation algorithms based on
MCP and other confidence scores for classification tasks (see Extended Fig. C.19 for other
tasks).
etal.,2022). WefindthatMCPyieldssignificantlydifferentresultscompared
to other confidence scores in 13 out of 15 conditions for classification tasks
(Fig. 7b), 8 out of 9 conditions for 2D segmentation, and 9 out of 9 conditions
for 3D segmentation (Extended Fig. C.19b). Additionally, we observe that
different existing estimation algorithms also display clear differences under
varying conditions (Extended Fig. C.19a).
Next, we combine three estimation methods into an ensemble, known as
MOVAL Ensemble, and apply it to all the test conditions previously men-
tioned. Notably, we select different combinations for various tasks and met-
rics, with most of the chosen methods being from our proposed CS vari-
ants (Extended Table E.19). The resulting MOVAL Ensemble consistently
ranks among the top performers across all tasks and metrics, achieving the
best results in 7 out of 11 scenarios (Fig. 4a, Fig. 5a, Fig. 5c). Compared
to state-of-the-art methods, the MOVAL Ensemble demonstrates significant
advantages in most cases (Fig. 7a, Fig. 7c, Extended Fig. C.16a, Extended
Fig. C.16b, Extended Fig. C.16c).
For classification tasks, compared to the best-performing existing meth-
ods, MOVAL Ensemble reduces the MAE from 4.86 to 3.09 for accuracy
24

(paired t-test,p= 1.05×10 −7), from 20.63 to 14.81 for F1-Score (p=
6.04×10 −18), from 19.37 to 15.84 for sensitivity (p= 3.54×10 13), from
27.32 to 24.10 for precision (p= 1.43×10 −6), and from 10.33 to 8.08 for
AUC (p= 8.18×10 −7). Specifically, we observe that MOVAL Ensemble
significantly enhances performance especially when there are fewer classes
(e.g., 10 classes, Extended Fig. C.17a). For example, MOVAL Ensemble re-
duces the MAE from 18.85 to 9.45 for sensitivity estimation on CIFAR10-LT
(Extended Table E.5,p= 1.53×10 −93).
For segmentation tasks, MOVAL Ensemble consistently enhances F1-
Scoreestimationaccuracyacrossvarioustasks(ExtendedFig.C.18a). Specif-
ically, compared to the best-performing existing methods, MOVAL Ensemble
reduces the MAE from 7.05 to 3.44 for 2D segmentation (paired t-test,p=
3.54×10 −4) and from 16.13 to 7.74 for 3D segmentation (p= 4.28×10−27).
For precision estimation, MOVAL Ensemble decreases the MAE from 9.06
to 7.68 for 2D segmentation (p= 8.54×10−7) and from 9.09 to 5.12 for 3D
segmentation (p= 1.53×10 −10). MOVAL Ensemble also proves effective for
sensitivity estimation in 3D segmentation, reducing the MAE from 14.76 to
10.43 (p= 1.09×10 −4). Although the improvement in sensitivity for 2D
segmentation is not significant (3.07 versus 3.09,p= 0.80), MOVAL Ensem-
ble demonstrates notably better results for the most minority class (i.e., left
cavities segmentation), reducing the MAE from 2.93 to 2.87 (p= 1.4×10−2).
In summary, MOVAL Ensemble serves as a reliable tool for estimating key
metrics such as F1-Score, sensitivity, and precision in segmentation tasks.
To gain a deeper understanding of the estimation results, we exam-
ine the actual metrics and estimation outcomes of MOVAL Ensemble, the
best-performing existing methods and the MCP baselines (Fig. 6a, Fig. 6b,
Fig. 6c). The predicted performance by the MCP baseline consistently ex-
ceeds the actual performance across all metrics due to the common over-
confidence in neural networks (Guo et al., 2017). Existing standards can mit-
igate the discrepancy between estimated and actual metrics, while MOVAL
Ensemble performs better at estimating the underlying label distribution
(Top Fig. 6a). The estimation results of MOVAL Ensemble are closer to
the”predicted metric=real metric" line over a broad range, indicating that
it produces less estimation error across varying levels of difficulty (Middle
Fig. 6c). The distribution of MAE produced by MOVAL Ensemble is more
concentrated at lower values, indicating that it achieves smaller estimation
errors in a greater number of cases (Bottom Fig. 6c).
25

4.7. Robustness under Training Conditions
a
b
cCIFAR10-LT Classification F1-Score Brain Lesion Segmentation F1-Score
Brain Lesion Segmentation
F1-Score Estimation (MAE)
CIFAR10-LT Classification
F1-Score Estimation (MAE)
|Van |Van
|Van|Van
Cardiac 2D Segmentation
F1-Score Estimation
CIFAR10-LT Classification
F1-Score Estimation
CIFAR10-LT Classification
AUC Estimation
MAE
MAE
MAE
CIFAR10-LT Classification
Accuracy Estimation
CIFAR10-LT Classification
Sensitivity Estimation
CIFAR10-LT Classification
Precision Estimation
MAE
MAE
MAE
Data Used for Estimation Data Used for Estimation Data Used for Estimation
Data Used for Estimation Data Used for Estimation Data Used for Estimation
Brain Lesion 3D Segmentation F1-Score Estimation
MAE
Data Used for Estimation
F1-ScoreF1-Score
Training Strategies
Training Strategies
Balanced
Training I
Balanced
Training II
Robust
Training I
Robust
Training II
Vanilla
Balanced
Training I
Balanced
Training II
Robust
Training I
Robust
Training II
Vanilla
Balanced
Training I
Balanced
Training II
Robust
Training I
Robust
Training II
Vanilla
Balanced
Training I
Balanced
Training II
Robust
Training I
Robust
Training II
Vanilla
Baseline: MCP | Vanilla
Original
Class-Specific
Baseline: MCP | Vanilla
Original
Class-Specific
Baseline: MCP | Vanilla
Existing Standards
MOVAL Ensemble
Baseline: MCP | Vanilla
Existing Standards
MOVAL Ensemble
Existing Standards w/ 100% Data
Existing Standards w/ 100% Data Existing Standards w/ 100% Data Existing Standards w/ 100% Data
Existing Standards w/ 100% Data Existing Standards w/ 100% Data
Figure 8: MOVAL Ensemble maintains stability in realistic settings.(a): Classifica-
tion and segmentation results when models are trained with advanced training strategies
designed for class imbalance or domain generalization (Classification, Balanced Training
I: label-distribution-aware margin (LDAM) loss (Cao et al., 2019), Balanced Training
II: deferred re-weighting (DRW) training schedule (Cao et al., 2019), Robust Training
I: cutout (DeVries and Taylor, 2017), Robust Training II: RandAugment (Cubuk et al.,
2020); Segmentation, Balanced Training I: asymmetric large margin loss (Li et al., 2020),
Balanced Training II: asymmetric focal loss (Li et al., 2020), Robust Training I: global
intensity non-linear augmentation (GIN) technique (Ouyang et al., 2022a), Robust Train-
ing II: mixup (Zhang et al., 2017)).(b): Top: MAE comparison between the original
estimation methods and our proposed class-specific variants with various training strate-
gies. Bottom: MAE comparison between best-performing existing method and MOVAL
Ensemble with various training strategies.(c): MAE achieved by MOVAL Ensemble when
optimized with different amounts of validation data.
We evaluate the compatibility of MOVAL Ensemble with models trained
using advanced strategies, specifically Balanced Training to address class
imbalance (Cao et al., 2019; Li et al., 2020) and Robust Training to improve
model generalization (DeVries and Taylor, 2017; Cubuk et al., 2020; Ouyang
et al., 2022a; Zhang et al., 2017). These strategies are commonly used in
real-world applications (Suppl. Note) and are applied to CIFAR10-LT and
brain lesion segmentation. Most strategies improve model performance on
unseen test data across various domain shifts (Fig. 8a).
26

We then apply the MOVAL framework to these models to evaluate its
effectiveness in these realistic settings (Fig. 8b). Previous conclusions remain
valid for most scenarios involving advanced training strategies. For example,
the proposed CS variants yield better results than the original estimation
algorithms for F1-Score (Top Fig. 8c). Additionally, MOVAL Ensembles
consistently outperform best-performing existing methods by a substantial
margin when models are trained using various strategies (Bottom Fig. 8c).
In practice, certain balanced training strategies can significantly alter the
distribution of predicted probabilities and complicate the confusion matrix.
This creates challenges for performance estimation, particularly accuracy es-
timation, since calibration methods rely on these probabilities and metrics.
To address this, we propose group-wise calibration, which aligns accuracy
across groups of samples from different classes which share similar statistics
instead of focusing on individual classes. This approach can stabilize accu-
racy estimation in advanced training settings (Extended Table E.13, E.14).
4.8. Stability with Varying Amounts of Data
We evaluate MOVAL Ensemble with varying amounts of available valida-
tion data to provide practical application guidelines. We optimize MOVAL
Ensemble for default-trained models on CIFAR10-LT and cardiac segmenta-
tion with different data quantities, and for all advanced training strategies in
brain lesion segmentation. This simulates a realistic setting, and we present
the average results from five runs.
We find that MOVAL Ensemble is not sensitive to the amount of vali-
dation data, performing well even with limited data (Fig. 8c). For classifi-
cation tasks like CIFAR10-LT, it requires as little as 5%of the validation
data to achieve performance comparable to best-performing existing meth-
ods for most metrics. Approximately 60 samples per case are needed to
obtain the most stable results. A similar conclusion applies to segmentation
tasks, where 12 slices are required for 2D segmentation and 6 volumes for
3D segmentation to achieve stable results. MOVAL Ensemble performs best
with Balanced Training II (asymmetric focal loss) (Li et al., 2020), likely due
to reduced variance in predicted probabilities for background samples, min-
imizing probability shifts under domain changes and enhancing estimation
effectiveness.
Additionally, as previously mentioned, we provide group-wise calibration
for classification, which assumes that classes with similar statistics should
share similar optimal calibration parameters, thereby reducing the number
27

of parameters. This approach could further decrease the need for validation
samples (Extended Fig. C.20).
4.9. Informative Indicators at Different Levels
a
b
MCP Grouped by Predicted Class TS Calibrated MCP Grouped by Predicted Class
TS Calibrated Doctor Grouped by Predicted Class MOVAL Ensemble Grouped by Predicted Class
Overall Overall
Overall Overall
Confidence Score Confidence Score
Confidence Score Confidence Score
Predicted Class (From Majority to Minority)
Predicted Class (From Majority to Minority) Predicted Class (From Majority to Minority)
Predicted Class (From Majority to Minority)
DSC (F1-Score) Estimation for 2D Cardiac Segmentation
DSC (F1-Score) Estimation for 3D Brain Lesion Segmentation
Estimating with Average MCP Estimating with TS MCP Estimating with MOVAL Ensemble
Estimating with Average MCP Estimating with TS MCP Estimating with MOVAL Ensemble
1.0
0.7
0.4
0.1
1.0
0.7
0.4
0.1
1.0
0.7
0.4
0.1
1.0
0.7
0.4
0.1
1.0
0.7
0.4
0.1
1.0
0.7
0.4
0.1
Overall
Overall Overall
Overall Overall
Overall
Figure 9: Fine-grained performance indicators at class and instance levels.(a): Alignment
of confidence scores and class-wise correctness for skin lesion classification.(b): Top:
Alignment of instance-wise DSC estimation and real DSC for 2D cardiac segmentation.
Bottom: Alignment for 3D brain lesion segmentation.
Lastly, we test if the calibrated confidence of MOVAL Ensemble can be
informative except the use of estimating global metrics. Specifically, the
confidence score is calibrated to match accuracy for skin lesion classification
and to match the F1-Score for cardiac and brain lesion segmentation.
MOVAL provides more precise feedback at the class-wise level (Fig. 9a).
By evaluating model performance on a per-class basis, the MOVAL Ensem-
ble not only offers an overall estimation advantage but also demonstrates
improved alignment with class-wise performance. This allows for a more
accurate assessment of sample groups and facilitates comparisons between
different groups.
MOVAL also provides more precise feedback at the instance-wise level
for segmentation tasks (Fig. 9b). By optimizing MOVAL parameters using
28

averages from various cases, we can also evaluate performance for individual
cases. While existing accuracy-calibrated methods tend to be overly op-
timistic for segmentation tasks, MOVAL Ensemble offers a more accurate
reflection of segmentation results across different cases.
Differences
Real DSC is [0.785]PredictionGround Truth
MOVAL Ensemble
Estimation [0.841]
TS MCP
Estimation [0.977]
MCP
Estimation [0.991]
MOVAL Ensemble
Estimation [0.909, 0.863, 0.839]
TS MCP
Estimation [0.989, 0.978, 0.970]
MCP
Estimation [0.996, 0.993, 0.988]
Differences
Real DSC is [0.910, 0.843, 0.869] PredictionGround Truth [Green:1, Blue:2, Red: 3]
Segmentation Label
 Segmentation Label
 Segmentation Error
Uncertainty Region
 Uncertainty Region
 Uncertainty Region
Figure 10: Fine-grained performance indicators at pixel level. Left: Visualization of
calibrated confidence scores for 2D cardiac segmentation. Right: 3D scatter plots of
segmentation error and uncertainty regions from calibrated confidence scores.
MOVAL provides prompt performance feedback at the pixel-wise level
(Fig. 10). We can assess model performance using the calibrated confidence
map. For example, MOVAL Ensemble can highlight classes with relatively
poor performance (Left Fig. 10). It also offers quantitative insights into
uncertain regions and emphasizes areas that need closer attention (Right
Fig. 10). This behavior arises because MOVAL Ensemble integrates multiple
confidence scores, whose combined confidence values tend to concentrate near
0 and 1 (see Extended Fig. C.21), potentially making it easier to detect
anomalies without carefully crafting a threshold.
5. Discussion and Conclusion
Reliable deployment is crucial for fully realizing the potential of modern
machine learning models in real-world applications. Efforts to regulate the
development of machine learning models to support safer deployment have
been on the rise (Rivera et al., 2020; Vasey et al., 2022), yet a standard-
ized tool to easily monitor performance without labels is still lacking. To
fill this gap, we introduce MOVAL, a new confidence-based model evalua-
tion tool that estimates model performance without needing ground truth.
By extending confidence-based approaches to a variety of confidence scores,
29

metrics, and tasks, we achieve promising results in diverse scenarios, from
cross-site skin lesion classification to cross-scanner MRI segmentation. We
believe this tool can enhance existing machine learning workflows with its
easy-to-use and transparent design, as a practical post-training monitoring
andperformance-estimationaidthatcaninform, ratherthanbyitselfguaran-
tee, safe deployment of machine learning in real-world settings. For instance,
it can help determine whether a pre-trained model should be deployed by
evaluating if its estimated performance on target data meets the acceptance
criteria for the deployment environment, complementing rather than replac-
ing standard validation and regulatory processes.
The key feature of MOVAL is its ability to track a wide range of com-
plementary and informative metrics, including accuracy, F1-Score, sensitiv-
ity, precision, and AUC, all within a unified framework. Confidence scores
have shown notable accuracy results for balanced benchmark datasets like
CIFAR10, but they do not address class imbalance, a common issue in med-
ical imaging databases. MOVAL’s unique contribution is its extension of
the standard calibration process to incorporate class-wise alignment. This
approach not only reduces calibration bias caused by class imbalance but
also naturally adapts the framework to estimate group-wise metrics beyond
accuracy (Fig. 2). Furthermore, unlike existing methods, class-wise calibra-
tion enables MOVAL to track performance at the class level, making it less
sensitive to variations in label distribution during testing compared to the
training distribution.
MOVAL is highly versatile and can be easily applied to a variety of tasks,
including classification, 2D segmentation, and 3D segmentation. Through
extensive evaluation across six tasks and 6,572 test scenarios (Fig. 4, Fig. 5),
we demonstrate that MOVAL offers significant advantages over existing stan-
dards. Designed with distinct modular components, the framework is flexible
enough to integrate additional confidence scores or other performance esti-
mation methods. In the future, we plan to include more recent successes in
confidence-based accuracy estimation, such as Agreement-on-the-Line (Baek
et al., 2022), ATC-distance (Roschewitz and Glocker, 2023), Confidence Op-
timal Transport (COT) (Lu et al., 2023) and Weighted Flips (WF) (Press
et al., 2024) into our framework.
Building on our successful approaches, we introduce MOVAL Ensemble,
which combines the strengths of various estimation methods by averaging the
calibrated probabilities. This ensemble achieves top performance in most
of the scenarios we tested. Specifically, compared to the best-performing
30

existingmethods, itreducesclassificationaccuracyestimationerrorby36.4%,
2D segmentation F1-Score estimation error by 51.2%, and 3D segmentation
F1-Score estimation error by 52.0%. While we provide MOVAL Ensemble
as a comprehensive solution, users can also customize it by selecting the
confidence scores they wish to combine for their specific tasks.
We illustrate the utility and effectiveness of MOVAL Ensemble in real-
istic settings and use cases. Our findings indicate that MOVAL Ensemble
performs well with various advanced model training strategies designed to
enhance model robustness against class imbalance and domain shifts. De-
spite these strategies significantly altering model behavior, our method con-
sistently produced stable estimation results across most scenarios. We also
demonstrate that MOVAL Ensemble has minimal requirements for the vali-
dationsetandofferpracticalsuggestionsfordesigningexperimentsinrealistic
settings (Fig. 8). Furthermore, we show that calibrated confidence can be
valuable for fine-grained performance analysis (Fig. 9).
MOVAL is primarily designed to estimate model performance under ac-
quisition shifts in medical imaging, where images are typically obtained un-
der varying conditions (Castro et al., 2020). While it can be used in other
domain shift scenarios, users should ensure the following for optimal per-
formance (though not all can be avoided): 1) No annotation shifts between
the validation and test sets, meaning the labeling concept remains consis-
tent across datasets. 2) No population shifts between validation and test
sets, meaning there should be no population-related covariate shifts in the
input features. This requires ensuring that samples are collected from simi-
lar regions and demographics, with comparable disease patterns or evolving
environments. 3) Although MOVAL is not highly sensitive to prevalence
shifts (e.g., differing class ratios between validation and test), performance
is generally optimal when these ratios align because the learned calibration
parameters are closely tied to the confusion matrix, which is more likely to
remain correlated between validation and test with identical prevalence.
The precision estimate is inherently limited as it can only be calibrated
from positive predictions, ignoring the informative but large pool of false neg-
atives. This makes it less reliable than sensitivity or F1-Score, which lever-
age a wider range of prediction data for calibration. Consequently, MOVAL
should not be the sole metric for applications prioritizing precision. This
limitation matters most in clinical use cases where false positives drive un-
necessary interventions or follow-up procedures (e.g., biopsy referral, repeat
scans). Based on our experiments (Fig. 4, Fig. 7), MOVAL’s precision esti-
31

mate is reasonably reliable when validation and target prevalence are similar
and the positive class is not extremely rare; otherwise, we recommend treat-
ing it as indicative only and confirming with a modest labeled sample or the
more robust F1-Score or sensitivity estimates.
MOVAL relies on a calibration parameter learned from the validation
dataset and applied, without adjustment, to unlabeled test data—an as-
sumption, not a guarantee, since the ideal parameters would require test-
domain labels. We therefore describe MOVAL as a practical monitoring and
performance-estimation tool that can support deployment decisions, rather
than one that ensures safe deployment under arbitrary shift. Its validity
depends on the shift type. Under acquisition shifts, where the scanner, pro-
tocol, or site changes but the model’s input-output relationship is largely
preserved, we find empirically that validation-domain calibration remains
informative (Section 4). Under prevalence or class-ratio shifts, MOVAL’s
class-wise design is comparatively robust. Under more severe shifts, where
the confidence-correctness relationship changes qualitatively, calibration may
not transfer, and we recommend a small labeled test sample to check and, if
necessary, recalibrate.
Estimating performance from unlabeled test data is not identifiable in
general without assumptions linking validation-domain calibration to test-
domain correctness, and no distribution-free guarantee should be expected
under arbitrary shift. In the acquisition-shift regime we target, a bounded
divergence between validation and target confidence-score distributions, a
stable class-conditional label distribution, or an identifiable label-shift struc-
ture would let one bound the estimation error; access to multiple labeled
source domains would offer a further, more permissive route to a worst-case
bound. We leave a formal treatment of these assumptions to future work.
Several other directions for future work remain to enhance MOVAL’s appli-
cability and robustness. First, integrating test-time calibration, where the
model is adjusted on-the-fly using target domain data (Wang et al., 2020a;
Hu et al., 2024) or information from multiple domains (Yu et al., 2022), could
improve adaptability, though such methods typically require retraining or ac-
cess to multiple source domains that may not be available at deployment; we
view them as complementary rather than as direct substitutes for MOVAL’s
post-training, single-source setting. Second, more extensive evaluation across
a wider range of applications (e.g., ultrasound), tasks (e.g., 3D classification),
and model architectures is warranted. In particular, broader validation on
modern foundation models, multimodal models, and additional modalities
32

such as CT, ultrasound, and video remains future work.
For practitioners, we summarize the practical guidance that follows from
our ablations (Fig. 8). Calibration set size: as few as 5%of the validation
data (approximately 60 samples per class for classification) is sufficient for
stable estimates; for segmentation, about 12 slices (2D) or 6 volumes (3D)
are typically needed. Class-wise versus group-wise calibration: class-wise
calibration is preferred when each class has enough validation samples (rule
of thumb, tens of samples per class); when some classes are rare, group-
wise calibration, which shares parameters across a small number of groups,
achieves comparable accuracy with substantially fewer validation samples per
group. Interpreting disagreement across confidence scores: when individual
confidence scores (MCP, Entropy, Doctor, Energy) diverge substantially in
their estimates, this itself is a useful diagnostic that the shift may be more
severethananacquisitionshift, andwerecommenddefaultingtotheMOVAL
Ensemble estimate, which is more robust than any single score, in these cases.
Triggering manual review: because MOVAL cannot certify that validation-
domain calibration transfers, we recommend manual review or additional
labeling whenever the estimated performance drops below the acceptance
threshold for the application, when confidence-score disagreement is high, or
when the estimated prevalence distribution departs substantially from the
validation distribution.
MOVAL is parameter-efficient, at most requiring onlyc(the number of
classes)×L(the number of ensemble choices) parameters. This leads to
computationally efficient and reproducible optimization and inference pro-
cesses, especially compared to methods that require references during in-
ference (Valindria et al., 2017) or an additional neural network (Robinson
et al., 2018). We provide a Python API for all the algorithms described
above, designed for use and enhancement with every trained model. Given
the importance of time efficiency in machine learning applications like au-
tonomous driving and surgical image analysis, we believe our approach can
serve as a practical, real-time monitoring aid that supports, but does not by
itself guarantee, safe deployment in safety-critical applications.
Acknowledgments
This project received funding from the ERC under the EU’s Horizon 2020
research and innovation programme (grant No 757173). MR is funded by an
Imperial College President’s PhD scholarship and a Google PhD Fellowship.
33

Author contributions
Conceptualization:ZL, MI, BG.Methodology:ZL, MR, CO.Soft-
ware:ZL.Validation:ZL.Formal analysis:ZL.Data curation:ZL,
CO.Writing – original draft:ZL.Writing – review & editing:ZL,
KK, CC, MR, BG.Supervision:BG.Project administration:BG.
Funding acquisition:BG.
References
Baek, C., Jiang, Y., Raghunathan, A., Kolter, J.Z., 2022. Agreement-on-
the-line: Predicting the performance of neural networks under distribu-
tion shift. Advances in Neural Information Processing Systems 35, 19274–
19289.
Barber, R.F., Candes, E.J., Ramdas, A., Tibshirani, R.J., 2023. Conformal
prediction beyond exchangeability. The Annals of Statistics 51, 816–845.
Bernhardt, M., Ribeiro, F.D.S., Glocker, B., 2022. Failure detection in med-
ical image classification: A reality check and benchmarking testbed. arXiv
preprint arXiv:2205.14094 .
Bloch, N., Madabhushi, A., Huisman, H., Freymann, J., Kirby, J., Grauer,
M., Enquobahrie, A., Jaffe, C., Clarke, L., Farahani, K., 2015. Nci-isbi
2013 challenge: automated segmentation of prostate structures. The Can-
cer Imaging Archive 370.
Brett, M., Johnsrude, I.S., Owen, A.M., 2002. The problem of functional
localization in the human brain. Nature reviews neuroscience 3, 243–249.
Campello, V.M., Gkontra, P., Izquierdo, C., Martin-Isla, C., Sojoudi, A.,
Full, P.M., Maier-Hein, K., Zhang, Y., He, Z., Ma, J., et al., 2021. Multi-
centre, multi-vendor and multi-disease cardiac segmentation: the m&ms
challenge. IEEE Transactions on Medical Imaging 40, 3543–3554.
Cao, K., Wei, C., Gaidon, A., Arechiga, N., Ma, T., 2019. Learning im-
balanced datasets with label-distribution-aware margin loss. Advances in
neural information processing systems 32.
Castro, D.C., Walker, I., Glocker, B., 2020. Causality matters in medical
imaging. Nature Communications 11, 3673.
34

Chandola, V., Banerjee, A., Kumar, V., 2009. Anomaly detection: A survey.
ACM computing surveys (CSUR) 41, 1–58.
Chen, M., Goel, K., Sohoni, N.S., Poms, F., Fatahalian, K., Ré, C., 2021.
Mandoline: Model evaluation under distribution shift. Proceedings of the
International Conference on Machine Learning (ICML) , 1617–1629.
Combalia, M., Codella, N.C., Rotemberg, V., Helba, B., Vilaplana, V.,
Reiter, O., Carrera, C., Barreiro, A., Halpern, A.C., Puig, S., et al.,
2019. Bcn20000: Dermoscopic lesions in the wild. arXiv preprint
arXiv:1908.02288 .
Cubuk, E.D., Zoph, B., Shlens, J., Le, Q.V., 2020. Randaugment: Practical
automated data augmentation with a reduced search space. Proceedings
of the IEEE/CVF conference on computer vision and pattern recognition
workshops , 702–703.
Deng, W., Zheng, L., 2021. Are labels always necessary for classifier accuracy
evaluation? Proceedings of the IEEE/CVF conference on computer vision
and pattern recognition , 15069–15078.
DeVries, T., Taylor, G.W., 2017. Improved regularization of convolutional
neural networks with cutout. arXiv preprint arXiv:1708.04552 .
Eche, T., Schwartz, L.H., Mokrane, F.Z., Dercle, L., 2021. Toward gener-
alizability in the deployment of artificial intelligence in radiology: Role
of computation stress testing to overcome underspecification. Radiology:
Artificial Intelligence 3, e210097.
Elsahar, H., Gallé, M., 2019. To annotate or not? predicting performance
drop under domain shift. Proceedings of the 2019 Conference on Empirical
Methods in Natural Language Processing and the 9th International Joint
Conference on Natural Language Processing (EMNLP-IJCNLP) , 2163–
2173.
Fan, W., Davidson, I., 2006. Reverse testing: an efficient framework to select
amongst classifiers under sample selection bias. Proceedings of the 12th
ACM SIGKDD international conference on Knowledge discovery and data
mining , 147–156.
35

Ganaie, M.A., Hu, M., Malik, A.K., Tanveer, M., Suganthan, P.N., 2022.
Ensemble deep learning: A review. Engineering Applications of Artificial
Intelligence 115, 105151.
Gao, F., Han, L., 2012. Implementing the nelder-mead simplex algorithm
with adaptive parameters. Computational Optimization and Applications
51, 259–277.
Gao, W., Jin, R., Zhu, S., Zhou, Z.H., 2013. One-pass auc optimization, in:
International conference on machine learning, PMLR. pp. 906–914.
Garg, S., Balakrishnan, S., Lipton, Z.C., Neyshabur, B., Sedghi, H., 2022.
Leveraging unlabeled data to predict out-of-distribution performance.
arXiv preprint arXiv:2201.04234 .
Granese, F., Romanelli, M., Gorla, D., Palamidessi, C., Piantanida, P., 2021.
Doctor: A simple method for detecting misclassification errors. Advances
in Neural Information Processing Systems 34, 5669–5681.
Guillory, D., Shankar, V., Ebrahimi, S., Darrell, T., Schmidt, L., 2021.
Predicting with confidence on unseen distributions. Proceedings of the
IEEE/CVF international conference on computer vision , 1134–1144.
Guo, C., Pleiss, G., Sun, Y., Weinberger, K.Q., 2017. On calibration of
modern neural networks. International conference on machine learning ,
1321–1330.
Gutman, D., Codella, N.C., Celebi, E., Helba, B., Marchetti, M., Mishra,
N., Halpern, A., 2016. Skin lesion analysis toward melanoma detection:
A challenge at the international symposium on biomedical imaging (isbi)
2016, hosted by the international skin imaging collaboration (isic). arXiv
preprint arXiv:1605.01397 .
Harris, C.R., Millman, K.J., Van Der Walt, S.J., Gommers, R., Virtanen, P.,
Cournapeau, D., Wieser, E., Taylor, J., Berg, S., Smith, N.J., et al., 2020.
Array programming with numpy. Nature 585, 357–362.
He, K., Zhang, X., Ren, S., Sun, J., 2016. Deep residual learning for image
recognition. Proceedings of the IEEE conference on computer vision and
pattern recognition , 770–778.
36

Hendrycks, D., Dietterich, T., 2019a. Benchmarking neural network robust-
ness to common corruptions and perturbations. Proceedings of the ICLR
.
Hendrycks, D., Dietterich, T., 2019b. Benchmarking neural network ro-
bustness to common corruptions and perturbations. arXiv preprint
arXiv:1903.12261 .
Hinton, G., Vinyals, O., Dean, J., 2015. Distilling the knowledge in a neural
network. arXiv preprint arXiv:1503.02531 .
Horvitz, D.G., Thompson, D.J., 1952. A generalization of sampling without
replacement from a finite universe. Journal of the American statistical
Association 47, 663–685.
Hu, D., Liang, J., Wang, X., Foo, C.S., 2024. Pseudo-calibration: Improv-
ing predictive uncertainty estimation in unsupervised domain adaptation,
in: Forty-first International Conference on Machine Learning, pp. 19304–
19326.
Isensee, F., Jaeger, P.F., Kohl, S.A., Petersen, J., Maier-Hein, K.H., 2021.
nnu-net: a self-configuring method for deep learning-based biomedical im-
age segmentation. Nature methods 18, 203–211.
Islam, M., Seenivasan, L., Ren, H., Glocker, B., 2021. Class-distribution-
aware calibration for long-tailed visual recognition. arXiv preprint
arXiv:2109.05263 .
Kamnitsas, K., Bai, W., Ferrante, E., McDonagh, S., Sinclair, M., Pawlowski,
N., Rajchl, M., Lee, M., Kainz, B., Rueckert, D., et al., 2018. Ensembles of
multiple models and architectures for robust brain tumour segmentation,
in: Brainlesion: Glioma, Multiple Sclerosis, Stroke and Traumatic Brain
Injuries: Third International Workshop, BrainLes 2017, Held in Conjunc-
tion with MICCAI 2017, Quebec City, QC, Canada, September 14, 2017,
Revised Selected Papers 3, Springer. pp. 450–462.
Kawahara, J., Daneshvar, S., Argenziano, G., Hamarneh, G., 2018. Seven-
point checklist and skin lesion classification using multitask multimodal
neural nets. IEEE journal of biomedical and health informatics 23, 538–
546.
37

Kivimäki, J., Białek, J., Nurminen, J.K., Kuberski, W., 2024. Confidence-
based estimators for predictive performance in model monitoring. arXiv
preprint arXiv:2407.08649 .
Krizhevsky, A., Hinton, G., et al., 2009. Learning multiple layers of features
from tiny images. Technical report .
Kull, M., Perello Nieto, M., Kängsepp, M., Silva Filho, T., Song, H., Flach,
P., 2019. Beyond temperature scaling: Obtaining well-calibrated multi-
class probabilities with dirichlet calibration. Advances in neural informa-
tion processing systems 32.
Le Coz, A., Herbin, S., Adjed, F., 2024. Confidence calibration of classifiers
with many classes. Advances in Neural Information Processing Systems
37, 77686–77725.
Lemaître, G., Martí, R., Freixenet, J., Vilanova, J.C., Walker, P.M., Meri-
audeau, F., 2015. Computer-aided detection and diagnosis for prostate
cancer based on mono and multi-parametric mri: a review. Computers in
biology and medicine 60, 8–31.
Li, K., Yu, L., Heng, P.A., 2022a. Towards reliable cardiac image segmen-
tation: Assessing image-level and pixel-level segmentation quality via self-
reflective references. Medical Image Analysis 78, 102426.
Li, Z., Kamnitsas, K., Glocker, B., 2020. Analyzing overfitting under class
imbalance in neural networks for image segmentation. IEEE transactions
on medical imaging 40, 1065–1077.
Li, Z., Kamnitsas, K., Islam, M., Chen, C., Glocker, B., 2022b. Estimat-
ing model performance under domain shifts with class-specific confidence
scores, in: International Conference on Medical Image Computing and
Computer-Assisted Intervention, Springer. pp. 693–703.
Li, Z., Zheng, Y.Q., Chen, C., Jbabdi, S., 2024. Learning label refinement
and threshold adjustment for imbalanced semi-supervised learning. arXiv
preprint arXiv:2407.05370 .
Liew, S.L., Lo, B.P., Donnelly, M.R., Zavaliangos-Petropulu, A., Jeong, J.N.,
Barisano, G., Hutton, A., Simon, J.P., Juliano, J.M., Suri, A., et al., 2022.
38

A large, curated, open-source stroke neuroimaging dataset to improve le-
sion segmentation algorithms. Scientific data 9, 320.
Litjens, G., Toth, R., van de Ven, W., Hoeks, C., Kerkstra, S., van Ginneken,
B., Vincent, G., Guillard, G., Birbeck, N., Zhang, J., et al., 2014. Evalua-
tion of prostate segmentation algorithms for mri: the promise12 challenge.
Medical image analysis 18, 359–373.
Liu, Q., Dou, Q., Heng, P.A., 2020a. Shape-aware meta-learning for gener-
alizing prostate mri segmentation to unseen domains. International con-
ference on medical image computing and computer-assisted intervention ,
475–485.
Liu, W., Wang, X., Owens, J., Li, Y., 2020b. Energy-based out-of-
distribution detection. Advances in neural information processing systems
33, 21464–21475.
Liu, Z., Miao, Z., Zhan, X., Wang, J., Gong, B., Yu, S.X., 2019. Large-scale
long-tailedrecognitioninanopenworld, in: ProceedingsoftheIEEE/CVF
conference on computer vision and pattern recognition, pp. 2537–2546.
Lu, Y., Qin, Y., Zhai, R., Shen, A., Chen, K., Wang, Z., Kolouri, S., Stepput-
tis, S., Campbell, J., Sycara, K., 2023. Characterizing out-of-distribution
error via optimal transport. Advances in Neural Information Processing
Systems 36, 17602–17622.
Marrakchi, Y., Makansi, O., Brox, T., 2021. Fighting class imbalance with
contrastive learning. International conference on medical image computing
and computer-assisted intervention , 466–476.
Mehrtash, A., Wells, W.M., Tempany, C.M., Abolmaesumi, P., Kapur, T.,
2020. Confidence calibration and predictive uncertainty estimation for
deep medical image segmentation. IEEE transactions on medical imaging
39, 3868–3878.
Mendonça, T., Ferreira, P.M., Marques, J.S., Marcal, A.R., Rozeira, J., 2013.
Ph 2-a dermoscopic image database for research and benchmarking. 2013
35th annual international conference of the IEEE engineering in medicine
and biology society (EMBC) , 5437–5440.
39

Milletari, F., Navab, N., Ahmadi, S.A., 2016. V-net: Fully convolutional
neural networks for volumetric medical image segmentation. 2016 fourth
international conference on 3D vision (3DV) , 565–571.
NannyML, 2023. NannyML (release 0.11.0).https://github.com/
NannyML/nannyml. NannyML, Belgium, OHL.
Ouyang, C., Chen, C., Li, S., Li, Z., Qin, C., Bai, W., Rueckert, D., 2022a.
Causality-inspired single-source domain generalization for medical image
segmentation. IEEE Transactions on Medical Imaging 42, 1095–1106.
Ouyang, C., Wang, S., Chen, C., Li, Z., Bai, W., Kainz, B., Rueckert, D.,
2022b. Improved post-hoc probability calibration for out-of-domain mri
segmentation, in: International Workshop on Uncertainty for Safe Utiliza-
tion of Machine Learning in Medical Imaging, Springer. pp. 59–69.
Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel,
O., Blondel, M., Prettenhofer, P., Weiss, R., Dubourg, V., et al., 2011.
Scikit-learn: Machine learning in python. the Journal of machine Learning
research 12, 2825–2830.
Press, O., Shwartz-Ziv, R., LeCun, Y., Bethge, M., 2024. The entropy
enigma: Success and failure of entropy minimization. arXiv preprint
arXiv:2405.05012 .
Rivera, S.C., Liu, X., Chan, A.W., Denniston, A.K., Calvert, M.J.,
Ashrafian, H., Beam, A.L., Collins, G.S., Darzi, A., Deeks, J.J., et al.,
2020. Guidelines for clinical trial protocols for interventions involving ar-
tificial intelligence: the spirit-ai extension. The Lancet Digital Health 2,
e549–e560.
Robinson, R., Oktay, O., Bai, W., Valindria, V.V., Sanghvi, M.M., Aung, N.,
Paiva, J.M., Zemrak, F., Fung, K., Lukaschuk, E., et al., 2018. Real-time
prediction of segmentation quality. International conference on medical
image computing and computer-assisted intervention , 578–585.
Ronneberger, O., Fischer, P., Brox, T., 2015. U-net: Convolutional net-
works for biomedical image segmentation, in: Medical image computing
and computer-assisted intervention–MICCAI 2015: 18th international con-
ference, Munich, Germany, October 5-9, 2015, proceedings, part III 18,
Springer. pp. 234–241.
40

Roschewitz, M., Glocker, B., 2023. Distance matters for improving perfor-
mance estimation under covariate shift, in: 2023 IEEE/CVF International
Conference on Computer Vision Workshops (ICCVW), IEEE. pp. 4551–
4561.
Rotemberg, V., Kurtansky, N., Betz-Stablein, B., Caffery, L., Chousakos,
E., Codella, N., Combalia, M., Dusza, S., Guitera, P., Gutman, D., et al.,
2021. A patient-centric dataset of images and metadata for identifying
melanomas using clinical context. Scientific data 8, 1–8.
Russakovsky, O., Deng, J., Su, H., Krause, J., Satheesh, S., Ma, S., Huang,
Z., Karpathy, A., Khosla, A., Bernstein, M., et al., 2015. Imagenet large
scale visual recognition challenge. International journal of computer vision
115, 211–252.
Schneider, S., Lee, J.H., Mathis, M.W., 2023. Learnable latent embeddings
for joint behavioural and neural analysis. Nature 617, 360–368.
Steinhardt, J., Liang, P.S., 2016. Unsupervised risk estimation using only
conditional independence structure. Advances in Neural Information Pro-
cessing Systems 29.
Tschandl, P., Rosendahl, C., Kittler, H., 2018. The ham10000 dataset, a large
collection of multi-source dermatoscopic images of common pigmented skin
lesions. Scientific data 5, 1–9.
Valindria, V.V., Lavdas, I., Bai, W., Kamnitsas, K., Aboagye, E.O., Rockall,
A.G., Rueckert, D., Glocker, B., 2017. Reverse classification accuracy:
predicting segmentation performance in the absence of ground truth. IEEE
transactions on medical imaging 36, 1597–1606.
Valk, K., Kull, M., 2023. Assuming locally equal calibration errors for non-
parametric multiclass calibration. Transactions on Machine Learning Re-
search .
Vasey, B., Nagendran, M., Campbell, B., Clifton, D.A., Collins, G.S., De-
naxas, S., Denniston, A.K., Faes, L., Geerts, B., Ibrahim, M., et al., 2022.
Reporting guideline for the early stage clinical evaluation of decision sup-
port systems driven by artificial intelligence: Decide-ai. bmj 377.
41

Virtanen, P., Gommers, R., Oliphant, T.E., Haberland, M., Reddy, T., Cour-
napeau, D., Burovski, E., Peterson, P., Weckesser, W., Bright, J., et al.,
2020. Scipy1.0: fundamentalalgorithmsforscientificcomputinginpython.
Nature methods 17, 261–272.
Wang, H., Yu, Z., Yue, Y., Anandkumar, A., Liu, A., Yan, J., 2020a. Learn-
ing calibrated uncertainties for domain shift: A distributionally robust
learning approach. arXiv preprint arXiv:2010.05784 .
Wang, S., Tarroni, G., Qin, C., Mo, Y., Dai, C., Chen, C., Glocker, B., Guo,
Y., Rueckert, D., Bai, W., 2020b. Deep generative model-based quality
control for cardiac mri segmentation, in: Medical Image Computing and
Computer Assisted Intervention–MICCAI 2020: 23rd International Con-
ference, Lima, Peru, October 4–8, 2020, Proceedings, Part IV 23, Springer.
pp. 88–97.
Yoon, C., Hamarneh, G., Garbi, R., 2019. Generalizable feature learning
in the presence of data bias and domain class imbalance with application
to skin lesion classification. International conference on medical image
computing and computer-assisted intervention , 365–373.
Yu, Y., Bates, S., Ma, Y., Jordan, M., 2022. Robust calibration with multi-
domain temperature scaling. Advances in Neural Information Processing
Systems 35, 27510–27523.
Zenk, M., Zimmerer, D., Isensee, F., Traub, J., Norajitra, T.,
Jäger, P.F., Maier-Hein, K., 2025. Comparative benchmark-
ing of failure detection methods in medical image segmentation:
Unveiling the role of confidence aggregation. Medical Image
Analysis 101, 103392. URL:https://www.sciencedirect.com/
science/article/pii/S1361841524003177, doi:https://doi.org/10.
1016/j.media.2024.103392.
Zhang, H., Cisse, M., Dauphin, Y.N., Lopez-Paz, D., 2017. mixup: Beyond
empirical risk minimization. arXiv preprint arXiv:1710.09412 .
Zhao, S., Kim, M., Sahoo, R., Ma, T., Ermon, S., 2021. Calibrating predic-
tions to decisions: A novel approach to multi-class calibration. Advances
in Neural Information Processing Systems 34, 22313–22324.
42

Zong, C.C., Wang, Y.W., Xie, M.K., Huang, S.J., 2024. Dirichlet-based
prediction calibration for learning with noisy labels, in: Proceedings of the
AAAI Conference on Artificial Intelligence, pp. 17254–17262.
Appendix A. Quantitative Results
Dataset
and Training
Strategy
Confidence Score
Estimation
Algorithm
Class-Agnostic Class-Specific MOVAL
EnsembleMCP Energy Entropy Doctor MCP Energy Entropy Doctor
CIFAR10
Synthetic-95
Vanilla
Training
Vanilla 32.6±6.229.4±5.230.5±6.136.3±6.5— — — —
2.8±2.1
TS 6.5±5.013.5±6.75.5±5.04.9±4.07.1±5.412.4±7.65.9±4.94.0±3.7
DoC 11.7±6.28.5±5.310.9±6.112.6±6.510.9±6.58.5±5.910.3±6.111.6±6.7
ATC 4.1±3.76.2±3.74.2±3.74.1±3.73.5±3.53.2±1.83.3±3.23.4±3.4
TS-ATC 5.0±2.66.7±3.75.4±3.15.3±2.92.8±2.73.6±2.22.8±2.43.0 ±2.2
CIFAR100
Synthetic-95
Vanilla
Training
Vanilla 46.7±4.35.4±3.155.6±4.664.8±4.9— — — —
2.5 ±2.3
TS 6.1±3.810.4±4.86.9±4.23.3±2.95.8±3.210.5±3.96.5±3.62.8±2.8
DoC 9.0±4.38.7±4.59.7±4.611.0±4.98.5±3.67.8±3.89.0±3.810.3±4.1
ATC 4.2±3.13.3±2.43.8±3.04.2±3.13.9±2.72.9±2.63.3±2.73.8±2.7
TS-ATC 2.7±4.24.2±3.33.0±2.22.7±1.72.2±2.13.5±3.22.6±2.42.2±1.8
HAM10000
Natural-7
Vanilla
Training
Vanilla 20.8±11.641.8±12.215.9±9.420.1±10.8— — — —
3.9±3.8
TS 11.0±6.620.1±10.29.8±6.38.9±5.411.1±6.719.3±10.49.8±6.38.2±5.5
DoC 15.3±8.314.0±7.812.6±7.314.7±8.115.1±8.513.8±7.812.6±7.414.5±8.2
ATC 8.3±5.04.9±3.07.4±4.28.6±5.06.0±4.35.1±3.55.4±4.06.2±4.3
TS-ATC 6.9±6.37.7±6.35.5±2.86.5±3.24.7±4.07.4±5.84.3 ±3.84.3 ±3.9
Table A.1: Related to Fig. 4. Evaluation of accuracy estimation for different classification
tasks under various types of domain shifts based on MAE. The best and second-best results
within the same category are inboldand underlinedfor each configuration.
43

Dataset
Confidence Score
Estimation
Algorithm
Class-Agnostic Class-Specific MOVAL
EnsembleMCP Energy Entropy Doctor MCP Energy Entropy Doctor
Cardiac-2D
Synthetic-65
Vanilla 17.8±7.752.5±9.016.3±7.217.5±7.5— — — —
4.3±5.0
TS 14.8±7.119.8±8.413.3±6.713.7±6.75.1±5.06.3±7.04.7±4.24.5±3.9
DoC 17.4±7.717.0±8.015.9±7.217.1±7.55.6±6.05.9±6.15.2±5.55.5±5.9
ATC 6.5±4.519.8±8.46.4±4.46.5±4.53.6±4.24.5±7.73.6±4.33.6±4.2
TS-ATC 6.2±6.719.8±8.46.2±4.46.2±4.44.0 ±6.26.2±10.14.0 ±6.24.0 ±6.2
Natural-4
Vanilla 15.9±0.852.3±1.814.8±0.815.7±0.8— — — —
2.6 ±0.4
TS 13.8±0.817.3±0.912.8±0.813.1±0.83.4±0.62.6 ±0.53.8±0.43.8±0.4
DoC 15.5±0.815.4±1.014.5±0.815.3±0.82.4±0.42.9±0.72.4±0.42.4±0.4
ATC 7.8±0.417.3±0.97.8±0.47.8±0.43.6±0.25.5±1.23.6±0.23.6±0.2
TS-ATC 7.9±0.817.3±0.97.9±0.47.9±0.44.5±0.88.1±2.04.5±0.84.5±0.8
Prostate-3D
Synthetic-83
Vanilla 12.7±8.061.4±5.38.6±4.810.7±6.4— — — —
1.7±2.2
TS 10.4±7.013.1±9.06.1±3.47.2±4.22.3±6.54.0±9.01.4 ±1.61.3±1.7
DoC 12.5±8.09.1±7.88.5±4.810.6±6.43.4±7.82.8±7.61.7±4.22.4±6.1
ATC 3.5±1.614.1±9.13.5±1.63.5±1.63.1±5.33.2±5.43.1±5.33.1±5.3
TS-ATC 3.5±3.43.1±3.43.5±1.63.5±1.63.1±5.33.6±5.93.1±5.33.1±5.3
Natural-5
Vanilla 18.9±6.657.2±5.312.9±4.316.0±5.4— — — —
1.6±1.4
TS 16.0±5.920.0±7.49.7±3.511.2±4.07.4±5.811.0±7.42.2±1.82.5±2.1
DoC 18.8±6.615.2±6.612.8±4.315.9±5.39.5±6.48.7±6.55.4±4.07.4±5.1
ATC 5.2±1.921.1±7.45.2±1.95.2±1.92.7±2.12.7±2.12.7±2.12.7±2.1
TS-ATC 5.2±3.52.1 ±0.95.2±1.95.2±1.92.7±2.12.7±2.02.7±2.12.7±2.1
Brain Lesion-3D
Synthetic-83
Vanilla 23.2±7.773.0±8.218.7±5.921.1±6.7— — — —
2.1 ±3.3
TS 20.9±7.224.8±8.417.3±5.618.0±5.84.4±7.25.1±8.32.2±4.12.3±4.2
DoC 23.1±7.724.8±8.418.7±5.921.0±6.74.3±7.35.1±8.32.8±5.43.4±6.2
ATC 15.3±4.624.8±8.415.3±4.615.3±4.62.3±4.02.3±4.02.3±4.02.3±4.0
TS-ATC 15.3±5.624.8±8.415.3±4.615.3±4.62.3±4.01.8±2.62.3±4.02.3±4.0
Natural-12
Vanilla 51.8±15.039.2±16.745.5±12.648.5±13.4— — — —
25.5 ±12.3
TS 49.3±14.854.0±15.944.0±12.444.9±12.634.4±16.235.7±17.128.7±12.728.9±12.8
DoC 51.7±15.054.0±15.945.5±12.648.5±13.433.9±15.835.6±17.130.3±13.331.8±14.1
ATC 40.5±11.054.0±15.940.5±11.040.5±11.028.8±12.428.7±12.328.8±12.428.8±12.4
TS-ATC 40.5±12.454.0±15.940.5±11.040.5±11.028.8±12.416.8±10.728.8±12.428.8±12.4
Table A.2: Related to Fig. 5. Evaluation of DSC (F1-Score) estimation for different
segmentation tasks under various types of domain shifts based on MAE. The best and
second-best results within the same category are inboldand underlinedfor each config-
uration.
44

Appendix B. MOVAL API and Example Usage
We offer a Python implementation of MOVAL that supports input in
the form of NumPy arrays (Harris et al., 2020)5. Themovalpackage (in-
stallable viapip install moval) implements only the MOVAL estimation
algorithms (confidence scores, calibration, metric computation) for use with
any trained model; it does not itself contain the paper’s experiments. The
separatemoval_scriptsrepository, together with the dataset and model
repositories linked above, contains the scripts and configurations needed to
reproduce the main classification and segmentation experiments reported in
this paper. The provided API is compatible with scikit-learn (Pedregosa
et al., 2011), a widely used machine learning library. This compatibility
allows users to leverage scikit-learn tools for downstream processing of the
computed probabilities, such as classification, clustering, and dimensionality
reduction (Schneider et al., 2023).
In a classification task withc= 10classes, the validation set contains 100
samples, while the test dataset consists of 200 samples:
import numpy as np
C = 10
logits = np.random.randn(100, C)
gts = np.random.randint(0, C, (100))
l_test = np.random.randn(200, C)
For example, a MOVAL classification model calibrated for accuracy using
TS with Entropy can be defined as:
import moval
moval_model = moval.MOVAL(
mode = "classification",
confidence_scores = "entropy-conf",
estim_algorithm = "ts-model",
class_specific = False
)
Alternatively, as we suggest, a MOVAL Ensemble model can be con-
structed with:
5Classification datasets and models:https://github.com/ZerojumpLine/
Robust-Skin-Lesion-Classification. Segmentation datasets and models:https:
//github.com/ZerojumpLine/Robust-Medical-Segmentation. Project page:https://
zerojumpline.github.io/moval/. Code:https://github.com/ZerojumpLine/MOVAL.
Documentation:https://moval.readthedocs.io/en/latest/index.html. Code (and
data) to reproduce the figures:https://github.com/ZerojumpLine/moval_scripts.
45

moval_model = moval.MOVAL(
mode = "classification",
estim_algorithm = \
"moval-ensemble-cls-accuracy"
)
For a 3D segmentation task withc= 2classes, the validation set consists
of 5 samples, and the test set includes 1 sample, defined as:
C = 2 ; H = 50 ; W = 50 ; D = 80
logits = [] ; gts = []
for _ in range(5):
logit = np.random.randn(C, H, W, D)
gt = np.random.randint(0, C, (H, W, D))
logits.append(logit)
gts.append(gt)
l_test = [np.random.randn(C, H, W, D)]
Similarly, a MOVAL segmentation model calibrated for F1-Score using
CS ATC with Doctor can be defined as:
moval_model = moval.MOVAL(
mode = "segmentation",
metric = "f1score",
confidence_scores = "doctor-conf",
estim_algorithm = "atc-model",
class_specific = True
)
The fitting and inference processes for the MOVAL model in both tasks
are identical:
moval_model.fit(logits, gts)
estim = moval_model.estimate(l_test)
# estim is of shape (1, ) for accuracy,
# while (c, ) for group-wise metrics
After optimization, we can obtain instance-wise estimation for the vali-
dation data using:
estim_val = moval_model.fitted_perf
# estim_val has N values for classification
# while Z values for segmentation
In addition to the overall estimated metrics, we can also derive the cali-
brated probabilitiesˆpi:
46

prob = moval_model.get_probability(l_tests)
We recommend supplying the MOVAL model with all pre-trained models.
To achieve this, the parameters can be saved and loaded using:
moval_model.save(’./m.pkl’)
loaded_model = moval.MOVAL.load(’./m.pkl’)
Appendix C. Supplementary Figures
Confidence
Score
Testing
Tasks
Estimating
Metrics
Classification
2D Segmentation
3D Segmentation
MCPEnergyEntropyDoctor
MCPEnergyEntropyDoctor
Accuracy
F1-Score
Sensitivity
Precision
AUC
Existing Method Provided by MOV AL Selected for MOV AL Ensemble
Class-Wise Calibration
c Logit {𝑧!}!"# $ ∈ℝ$
MCP=max! 𝑝!
Energy=−log/
!
𝑒%!
Entropy=−/
!
𝑝!log$𝑝!
Doctor=
1−∑!𝑝! &
∑!𝑝! &
Probability𝑝!∈[0,1]
a Calibrated ProbabilityLogit
Classification
2D Segmentation
3D Segmentation
 MOV AL
b
FigureC.11: ComparisonofMOVALwithexistingstandards.(a): Withinaunifiedframe-
work, MOVAL can be readily applied to classification, 2D, and 3D segmentation tasks.
(b): After extending existing methods in many dimensions, we find that an ensemble of
multiple confidence scores leads to more robust and state-of-the-art results.(c): MOVAL
explores performance estimation based on confidence scores rather than maximum class
probability (MCP), which is the basis of all existing methods.
47

CIFAR10-LT
In-Domain
Train: 12406
Validate: 3000
Test: 7000
Synthesized
Domain
Shifts:
7000 x 95
CIFAR100-LT
In-Domain
Train: 10847
Validate: 3000
Test: 7000
Synthesized
Domain
Shifts:
7000 x 95
Skin Lesion Classification
In-Domain
Train: 7010
Validate: 1002
Test: 2003
Out-Domain
Test 1: 12413
Test 2: 4365
Test 3: 3450
Test 4: 613
Test 5: 8201
Test 6: 1923
Test 7: 200
Brain Lesion Segmentation
In-Domain
Train: 61
Validate: 9
Test: 18
Synthesized
Domain
Shifts:
18 x 83
Out-Domain
Test 1: 137
Test 2: 38
Test 3: 29
Test 4: 18
Test 5: 78
Test 6: 49
Test 7: 25
Test 8: 70
Test 9: 19
Test 10: 42
Test 11: 15
Test 12: 45
Prostate Segmentation
In-Domain
Train: 21
Validate: 3
Test: 6
Synthesized
Domain
Shifts:
6 x 83
Out-Domain
Test 1: 12
Test 2: 12
Test 3: 19
Test 4: 30
Test 5: 13
Cardiac Segmentation
In-Domain
Train: 132
Validate: 19
Test: 39
Synthesized
Domain
Shifts:
39 x 65
Out-Domain
Test 1: 148
Test 2: 102
Test 3: 150
Test 4: 100
a
b
c
d
e
f
Figure C.12: Summary of the datasets used in this study.(a): Classification task I, Long-
tailed version of the CIFAR10 dataset.(b): Classification task II, Long-tailed version of
the CIFAR10 dataset.(c): Classification task III, skin lesion classification from 8 sources
of data.(d): 2D segmentation task I, cardiac MRI segmentation from 5 different scanners.
(e): 3D segmentation task I, prostate MRI segmentation from 6 different scanners.(f ):
3D segmentation task II, brain lesion segmentation from 13 different scanners.
48

Training
CIFAR10-LT
Classification
Test
Conditions at
Deployment
Domain #1 Domain #2 Domain #3 Domain #4 Domain #5 Domain #6 Domain #7
…
Training
Skin Lesion
Classification
Test
Conditions at
Deployment
…
Training
Cardiac MRI
Segmentation
Test
Conditions at
Deployment
…
Training
Prostate MRI
Segmentation
Test
Conditions at
Deployment
…
Training Brain
Lesion MRI
Segmentation
Test
Conditions at
Deployment
…
Figure C.13: In real-world scenarios, significant discrepancies often exist between training
and testing environments, affecting the distribution of acquired images. For instance,
in natural images, such discrepancies can be caused by image corruptions like blur or
noise (Hendrycks and Dietterich, 2019b). In medical images, these can arise from scanner
effects or variations in imaging protocols (Castro et al., 2020). For segmentation tasks,
regions of interest are highlighted with different colors.
49

Training
samples
Test settings at
deployment,
including 12
natural (Nat) and
83 synthesized
(Syn) domain
shifts
(Original) Syn#2 Syn#3 Syn#4 Syn#5 Syn#6 Syn#7 Syn#8 Syn#9 Syn#10 Syn#11Syn#1
Syn#12 Syn#14 Syn#15 Syn#16 Syn#17 Syn#18 Syn#19 Syn#20 Syn#21 Syn#22 Syn#23Syn#13
Nat#1 Nat#2 Nat#3 Nat#4 Nat#5 Nat#6 Nat#7 Nat#8 Nat#9 Nat#10 Nat#11 Nat#12
Syn#24 Syn#26 Syn#27 Syn#28 Syn#29 Syn#30 Syn#31 Syn#32 Syn#33 Syn#34 Syn#35Syn#25
Syn#36 Syn#38 Syn#39 Syn#40 Syn#41 Syn#42 Syn#43 Syn#44 Syn#45 Syn#46 Syn#47Syn#37
Syn#48 Syn#50 Syn#51 Syn#52 Syn#53 Syn#54 Syn#55 Syn#56 Syn#57 Syn#58 Syn#59Syn#49
Syn#60 Syn#62 Syn#63 Syn#64 Syn#65 Syn#66 Syn#67 Syn#68 Syn#69 Syn#70 Syn#71Syn#61
Syn#72 Syn#74 Syn#75 Syn#76 Syn#77 Syn#78 Syn#79 Syn#80 Syn#81 Syn#82 Syn#83Syn#73
a
b
Figure C.14: Examples of brain lesion segmentation datasets.(a): Visualization of Brain
MR images of In-Domain and Out-Domain Examples. Top: Brain MR images used for
training. Brain lesion regions are highlighted with red color. Bottom: Brain MR images
with natural and synthesized domain shifts.(b): Intensity histograms of training and test
data for 12 test conditions.
50

2D Segmentation
(1 Task w/
69 conditions)
a
3D Segmentation
(2 Tasks w/
183 conditions)
b
2D Accuracy Estimation 3D Accuracy Estimation2D AUC Estimation 3D AUC Estimation
Real Accuracy
Predicted Accuracy
MAE
Samples
Real Accuracy
Predicted Accuracy
MAE
Samples
Real AUC
Predicted AUC
MAE
Samples
Real AUC
Predicted AUC
MAE
Samples
c d
Accuracy Estimation
Accuracy Estimation
AUC Estimation
AUC Estimation
Vanilla Vanilla
Vanilla Vanilla
Van Van
Van
Van
Van Van
|Van
|Van
Van Van
Provided by MOVAL
Existing Standards: 0.2
Color: Category
Existing Methods
Size: MAE
MOVAL Best: 0.2
Provided by MOVAL
Existing Standards: 0.1
Color: Category
Existing Methods
Size: MAE
MOVAL Best: 0.1
Provided by MOVAL
Existing Standards: 2.6
Color: Category
Existing Methods
Size: MAE
MOVAL Best: 2.2
Provided by MOVAL
Existing Standards: 1.9
Color: Category
Existing Methods
Size: MAE
MOVAL Best: 1.8
Baseline: MCP | Vanilla
Existing Standards: MCP | TS
MOVAL Ensemble
Prostate Synthetic
Prostate Natural
y = x
Brain Lesion Synthetic
Brain Lesion Natural
Baseline: MCP | Vanilla
Existing Standards: MCP | DoC
MOVAL Ensemble
Prostate Synthetic
Prostate Natural
y = x
Brain Lesion Synthetic
Brain Lesion Natural
Baseline: MCP | Vanilla
Existing Standards: MCP | Vanilla
MOVAL Ensemble
Cardiac Synthetic
Cardiac Natural
y = x
Baseline: MCP | Vanilla
Existing Standards: MCP | DoC
MOVAL Ensemble
Cardiac Synthetic
Cardiac Natural
y = x
Baseline: MCP | Vanilla
Existing Standards: MCP | DoC
MOVAL Ensemble
Mean
Baseline: MCP | Vanilla
Existing Standards: MCP | Vanilla
MOVAL Ensemble
Mean
Baseline: MCP | Vanilla
Existing Standards: MCP | TS
MOVAL Ensemble
Mean
Baseline: MCP | Vanilla
Existing Standards: MCP | DoC
MOVAL Ensemble
Mean
Figure C.15: Accuracy and AUC are less useful for segmentation tasks.(a, b): MAE
between real metrics and estimated results based on different estimation methods for 2D
and 3D segmentation tasks. We also report the average MAE for natural and synthetic
domain shifts here. The smaller the MAE, the better.(c, d): Top: Predicted and real
label distribution. We benchmark MOVAL ensemble (blue) against MCP baselines (light
gray) and the best-performing existing method (dark gray). Middle: Predicted versus
real metrics for 2D and 3D segmentation tasks. Bottom: Histogram of MAE for different
estimation methods. As the class ratios are extremely imbalanced for segmentation tasks,
accuracy and AUC are less informative as they are close to 100%.
51

c
a
Vanilla
Vanilla
Vanilla
Vanilla
～
Vanilla
 Vanilla
b
VanillaVanilla
3D Segmentation (2 Tasks w/ 183 conditions) Sensitivity Estimation 3D Segmentation (2 Tasks w/ 183 conditions) Precision Estimation
2D Segmentation (1 Task w/ 69 conditions) Sensitivity Estimation 2D Segmentation (1 Task w/ 69 conditions) Precision Estimation
Classification (3 Tasks w/ 197 conditions) Sensitivity Estimation Classification (3 Tasks w/ 197 conditions) AUC Estimation
Classification (3 Tasks w/ 197 conditions) F1-Score Estimation Classification (3 Tasks w/ 197 conditions) Precision Estimation
MAE MAE MAE MAE
MAE MAE MAE MAE
Estimation Algorithm
Estimation Algorithm
Estimation Algorithm
Estimation Algorithm
Estimation Algorithm
Estimation Algorithm
Estimation Algorithm
Estimation Algorithm
Confidence Score
MCP
Energy
Entropy
Doctor
MOVAL
Ensemble
Confidence Score
Confidence Score
Confidence Score
Confidence Score
Confidence Score
Confidence Score
Confidence Score
MCP
Energy
Entropy
Doctor
MOVAL
Ensemble
MCP
Energy
Entropy
Doctor
MOVAL
Ensemble
MCP
Energy
Entropy
Doctor
MOVAL
Ensemble
MCP
Energy
Entropy
Doctor
MOVAL
Ensemble
MCP
Energy
Entropy
Doctor
MOVAL
Ensemble
MCP
Energy
Entropy
Doctor
MOVAL
Ensemble
MCP
Energy
Entropy
Doctor
MOVAL
Ensemble
Figure C.16: MOVAL Ensemble achieves significant improvements on major evaluation
metrics.(a, b, c): MAE comparison between proposed algorithms and existing methods
(Existing best method versus MOVAL Ensemble, paired t-test,T(196) = 9.54, p= 6.04×
10−18 for F1-Score estimation of classification tasks,T(196) = 4.97, p= 1.43×10−6 for
precision estimation of classification tasks,T(196) = 7.80, p= 3.54×1013 for sensitivity
estimation of classification tasks,T(196) = 5.10, p= 8.18×10−7 for AUC estimation of
classification tasks,T(68) =−0.26, p= 0.80for sensitivity estimation of 2D segmentation
tasks,T(68) = 5.42, p= 8.54×10 −7 for precision estimation of 2D segmentation tasks,
T(182) = 3.96, p= 1.09×10−4 for sensitivity estimation for 3D segmentation tasks and
T(182) = 6.79, p= 1.53×10−10 for precision estimation for 3D segmentation tasks.
52

a bCIFAR10-LT Classification Accuracy Estimation
CIFAR100-LT Classification Accuracy Estimation
Skin Lesion Classification Accuracy Estimation
Estimation Algorithm
MAE
Estimation Algorithm
MAE
Estimation Algorithm
MAE
Vanilla
Vanilla
Vanilla
AUC
F1-Score
Precision
Sensitivity
Accuracy
AUC
F1-Score
Precision
Sensitivity
Accuracy
AUC
F1-Score
Precision
Sensitivity
Accuracy
Confidence Score
Confidence Score
Confidence Score
MCP
Energy
Entropy
Doctor
MOVAL
Ensemble
MCP
Energy
Entropy
Doctor
MOVAL
Ensemble
MCP
Energy
Entropy
Doctor
MOVAL
Ensemble
Figure C.17: MOVAL Ensemble achieves state-of-the-art performance for several classifi-
cation tasks.(a): MAE comparison between proposed algorithms and existing methods
for different classification tasks.(b): MAE comparison between the original estimation
methods and our proposed class-specific variants for different classification tasks.
53

a bCardiac MRI Segmentation (Synthetic Conditions) F1-Score Estimation
Estimation Algorithm
MAE
Cardiac MRI Segmentation (Natural Conditions) F1-Score Estimation
Estimation Algorithm
MAE
Prostate MRI Segmentation (Synthetic Conditions) F1-Score Estimation
Estimation Algorithm
MAE
Prostate MRI Segmentation (Natural Conditions) F1-Score Estimation
MAE
Brain Lesion MRI Segmentation (Synthetic Conditions) F1-Score Estimation
Estimation Algorithm
MAE
Brain Lesion MRI Segmentation (Synthetic Conditions) F1-Score Estimation
Estimation Algorithm
MAE
Estimation Algorithm
Vanilla
Vanilla
Vanilla
Vanilla
Vanilla
Vanilla
F1-Score
Sensitivity
Precision
Accuracy
AUC
F1-Score
Sensitivity
Precision
Accuracy
AUC
F1-Score
Sensitivity
Precision
Accuracy
AUC
F1-Score
Sensitivity
Precision
Accuracy
AUC
F1-Score
Sensitivity
Precision
Accuracy
AUC
F1-Score
Sensitivity
Precision
Accuracy
AUC
F1-Score
Sensitivity
Precision
Accuracy
AUC
Confidence Score
Confidence Score
Confidence Score
Confidence Score
Confidence Score
Confidence Score
MCP
Energy
Entropy
Doctor
MOVAL
Ensemble
MCP
Energy
Entropy
Doctor
MOVAL
Ensemble
MCP
Energy
Entropy
Doctor
MOVAL
Ensemble
MCP
Energy
Entropy
Doctor
MOVAL
Ensemble
MCP
Energy
Entropy
Doctor
MOVAL
Ensemble
MCP
Energy
Entropy
Doctor
MOVAL
Ensemble
Figure C.18: MOVAL Ensemble achieves state-of-the-art performance for several segmen-
tation tasks.(a): MAE comparison between proposed algorithms and existing methods
for different segmentation tasks.(b): MAE comparison between the original estimation
methods and our proposed class-specific variants for different segmentation tasks.
54

2D Segmentation (1 Task w/ 69 conditions) Performance Estimation
MAEMAE
3D Segmentation (2 Task w/ 183 conditions) Performance Estimation
~
~
~!-value>0.05
*!-value≤0.05
**!-value≤0.01
***!-value≤10!"
****!-value≤10!#
~!-value>0.05
*!-value≤0.05
**!-value≤0.01
***!-value≤10!"
****!-value≤10!#
Classification (3 Tasks w/ 197 conditions) Performance Estimation
2D Segmentation (1 Task w/ 69 conditions) Performance Estimation
3D Segmentation (2 Tasks w/ 183 conditions) Performance Estimation
MAEMAEMAE
a b
Accuracy Sensitivity Precision F1-Score AUC
F1-Score Sensitivity Precision Accuracy AUC
F1-Score Sensitivity Precision Accuracy AUC
F1-Score Sensitivity Precision Accuracy AUC
F1-Score Sensitivity Precision Accuracy AUC
Figure C.19: MOVAL Ensemble combines advanced calibration and confidence scores
for better performance.(a): MAE comparison between estimation algorithms based on
different confidence calibration algorithms.(b): MAE comparison between estimation
algorithms based on MCP and other confidence scores for segmentation tasks.
CIFAR10-LT Classification Accuracy Estimation
MAE
Data Used for Estimation
CIFAR10-LT Classification F1-Score Estimation
Data Used for Estimation
MAE
CIFAR10-LT Classification Sensitivity Estimation
Data Used for Estimation
MAE
CIFAR10-LT Classification AUC Estimation
Data Used for Estimation
MAE
CIFAR10-LT Classification Precision Estimation
Data Used for Estimation
MAE
Figure C.20: Group-wise calibration enhances the robustness of the MOVAL Ensemble
against a reduction in validation samples. The proposed group-wise calibration method
generally requires fewer validation samples because it has fewer learnable parameters.
However, it may negatively impact the estimation of false positive predictions, which
require class-specific adjustments. This could potentially affect the estimation of AUC
and precision when data are sufficient. The standard error is shown alongside the bar
plots.
55

Validation
Out-Domain
Test
Accuracy
 Confidence Score Mean Confidence Estimation Gap
Class-Wise Performance
Predicted Class
Class-Wise Performance
Predicted Class
0.0 0.2 0.4.           0.6            0.8            1.0
Predicted Class
Predicted Class
Class-Wise Performance
0.0 0.2 0.4.           0.6            0.8            1.0
Class-Wise Performance
0.0 0.2 0.4.           0.6            0.8            1.0
Predicted Class
Class-Wise Performance
Predicted Class
Class-Wise Performance
MOV AL EnsembleMaximum Class Probability (MCP) Temperature Scaling (TS) MCP Class Specific (CS) TS MCP
Class-Wise Performance
Predicted Class
Class-Wise Performance
Predicted Class
0.0 0.2 0.4           0.6            0.8            1.0
MOV AL EnsembleMCP TS MCP CS TS MCP
Figure C.21: Confidence score distributions of different calibration methods on CIFAR10-
LT. For each class and calibration method, we show the estimated accuracy (gray gradient
bar), the true accuracy (black tick), and the gap between them (red), together with the
underlying confidence-score distribution (blue). Confidence distributions are shown as
kernel density estimates (KDE) of the per-sample confidence values, for visualization only,
to make the shift in confidence across classes easier to see. MOVAL Ensemble, which
combines multiple calibrated confidence scores, shows a distinctly bimodal distribution
concentrated near 0 and 1, providing a more distinct indicator of prediction correctness
than the single-score methods.
56

Appendix D. Supplementary Note
Appendix D.1. Group-Wise and Class-Specific Metrics Estimation
Apart from accuracy, we can also estimate group-wise metrics that mea-
sure model performance from different perspectives based on the predicted
probabilityp i instead of the confidence scoreqi. This is because these met-
rics also incorporate information from non-maximum classes. This approach
is related to efforts that formulate these metrics as loss functions (Gao et al.,
2013; Milletari et al., 2016). However, to enable estimation without ground
truth at test time, we use the predicted labely ′ i as a substitute for the
ground truth in our calculations. This can be viewed as an extension of the
confidence-based accuracy framework, which assumes that all predictions are
correct at some level of confidence. Specifically, the estimated F1-Score is
defined as:
Φ′ j = 2 PN i=1 1 ijpij PN
i=1 1 ij + PN i=1 pij ,(D.1)
where1 ij =1(y ′ i =j)is 1 if the predicted most probable class isjand0
otherwise. In a similar manner, sensitivity and precision can be calculated
as follows:
ρ′ j =
PN
i=1 1 ijpij PN
i=1 pij
, π ′ j =
PN
i=1 1 ijpij PN
i=1 1 ij
.(D.2)
The AUC calculation uses the One-vs-Rest strategy, which involves com-
paring one class against all other classes combined in multi-class problems.
Notably, this is equivalent to the One-vs-One strategy for binary classifi-
cation, which involves comparing every unique pairwise combination. The
estimation is given by:
Λ′ j =
Z 1
0
TPR′ j(t)d(FPR′ j(t)),(D.3)
where the true positive rate (TPR) and false positive rate (FPR) are calcu-
lated as follows:
TPR′ j(t) =
PN
i=1 1(p ij > t)pij PN
i=1 1(p ij > t)
,FPR ′ j(t) =
PN
i=1 1(p ij ≤t) P k̸=j pik
PN
i=1 1(p ij ≤t)
.
(D.4)
57

Throughout,iindexes a sample for classification and a pixel (2D) or voxel
(3D) for segmentation; for segmentation,zadditionally indexes the case (vol-
ume), so the per-pixel probability is writtenpzij. Eqs. D.1-D.4 are written
with the raw softmax output (pij for classification,p zij for segmentation)
to introduce the estimators; as described below, all reported estimates are
computed after MOVAL’s class-wise calibration, i.e., with the raw probabil-
ity replaced by its calibrated counterpart (ˆpij orˆpzij). In this manner, we
can derive all the metrics using only the network outputs. However, like
accuracy estimation, metrics derived from uncalibrated probabilities may be
inaccurate. Although some studies suggest that accuracy-calibrated models
perform better (NannyML), we believe that this approach may be subopti-
mal, as accuracy calibration does not necessarily improve all metrics.
Instead, we offer a novel solution for calibrating confidence to align with
these metrics. For each metric, we optimize a specific model tailored to that
metric. It directly adjusts parameters to ensure that the estimated metrics
align closely with the actual metrics on the validation set. This alignment is
made possible by our unique MOVAL framework, which incorporates class-
wise calibration with class-specific parameters.
After obtaining the calibrated probability ˆpi, the optimization process
closely follows the accuracy calibration procedure, as class-specific param-
eters can naturally be extended to other metrics. Using F1-Score as an
example, we perform separate calibration for thej’th class by adjusting all
pi predicted asjto ˆpi with class-specific parameters, ensuring that the es-
timation from Eq. D.1 usingˆpi aligns with the actual metrics. This process
is carried out for each class individually. All the other group-wise metrics,
including sensitivity, precision, and AUC, can be calibrated similarly using
Eq. D.2 and Eq. D.3, respectively. Regarding AUC, we compute five thresh-
olds at equal intervals based on the range of probabilitiesˆpij for all samples
of classj(denoted astin Eq. D.4). Using these thresholds, we then calculate
the areas under the FPR′ j–TPR′ j curve to estimate the AUC of classj, i.e,
Λ′ j.
Appendix D.2. Network Configurations
Here, we detail the network configurations and training procedures used
to develop the model for classification and segmentation tasks. This includes
specifics on neural network training and advanced strategies commonly em-
ployed to tackle class imbalance and domain generalization. These methods
are established techniques widely adopted as best practices.
58

Appendix D.2.1. Classification
Network architecture.We train a ResNet-32 (He et al., 2016) for CI-
FAR10 and CIFAR100 experiments following (Cao et al., 2019). We train a
ResNet-50 for skin lesion lesion classification following (Russakovsky et al.,
2015; Marrakchi et al., 2021).
Network training.We trained for 200 epochs on the CIFAR experiments
and 20,000 epochs for skin lesion classification. The networks are trained
using stochastic gradient descent (SGD). The learning rate was set to 0.1
and reduced using step decay. The images are normalized based on the
statistics of the training dataset. For the CIFAR baseline experiments, we
employed data augmentation techniques such as random flipping and color
transformations. For the skin lesion classification baseline experiments, we
applied data augmentation strategies including cropping to224×224and
random flipping.
Given a sample with labely∈ {1,2, . . . , c}, the neural network generates
z, which is subsequently transformed into a probability vectorp, where the
jth elementp j represents the probability of thejth class. Unless specified
otherwise, the network is trained using cross-entropy (CE) loss, which is
defined as:
LCE =−logp y =−log ezy P
k ezk .(D.5)
BalancedtrainingI:label-distribution-awaremargin(LDAM)loss(Cao
et al., 2019).LDAM applies unequal margins to the logits of different
classes to enhance the robustness of predictions for minority classes. The
calculation is defined as:
LLDAM CE =−log ezy−∆y
ezy−∆y + P k̸=y ezk ,(D.6)
where the margins for different classes are calculated as:
∆j = C n1/4 j ,(D.7)
whereCis a hyper-parameter andn j is the number of samples for classj.
This encourages the network to focus on minority classes, as they require
larger margins.
59

BalancedtrainingII:deferredre-weighting(DRW)weightingsched-
ule (Cao et al., 2019).DRW adjusts the weight of samples belonging to
different classes. To learn good representations and achieve unbiased per-
formance across classes, it applies uniform weighting at the beginning and
then reweights the samples based on class frequency (i.e., minority classes
receive larger weights) in the later stages of network training. Specifically, it
optimizes with:
LDRW CE =−w y logp y,(D.8)
wherew y is the weight for classy, which starts at 1 and later changes to
1/ny.
Robust training I: cutout (DeVries and Taylor, 2017).Cutout is
a data augmentation strategy that modifies the input sample by randomly
cropping out a square in the image and replacing it with black patches.
This helps networks become robust to local features and improves general-
ization. Cutout is commonly adopted in neural networks to enhance model
generalizability. We found that it significantly improves model accuracy on
in-domain samples but fails to enhance performance on most out-of-domain
samples, possibly because it causes neural networks to rely more on the orig-
inal intensity distributions. We choose to report its performance because it
is a default technique for training neural networks in classification.
Robust training II: RandAugment (Cubuk et al., 2020).RandAug-
ment is a data augmentation strategy that applies multiple stacked transfor-
mations with predefined magnitudes, unlike baseline methods. It introduces
transformations from a larger collection, improving network performance un-
der these conditions.
Appendix D.2.2. Segmentation
Network architecture.We train a 3D U-Net (Ronneberger et al., 2015)
for segmentation using the nnU-Net (Isensee et al., 2021) framework, with a
base feature map size of 30 and 4 downsampling steps at the bottleneck.
Network training.The networks are trained using patches sampled from
whole images, as the images are typically too large to be input into the
network due to memory limitations. For cardiac MRI segmentation, we train
using patches of size128×128×8with a batch size of 30. For prostate MRI
segmentation, we use patches of size64×64×32with a batch size of 32. For
brain lesion segmentation, we train with patches of size128×128×128and
a batch size of 2.
60

We train neural networks for 1000 epochs, in each epoch we train with
patches for 100 iterations. The networks are trained using SGD, with learn-
ing rates linearly decreased from 0.01 to 0. By default, we apply Z-score
normalization to MR images, ensuring that each MRI volume has a mean of
zero and unit variance. Given an image patch, the labelycorresponds to the
center pixel and is represented as a one-hot vector. In this vector,ej equals 1
ifjis the true class, and 0 otherwise. For baseline experiments, the networks
are trained with a balanced sum of cross-entropy (CE) loss and sample-wise
soft DSC loss, which are defined as:
LCE =−
cX
j=1
ej logp j =−
cX
j=1
ej log ezj P
k ezk ,(D.9)
and
LDSC =
cX
j=1
(1−e j)pj +e j(1−p j)
pj +e j
.(D.10)
Balanced training I: asymmetric large margin loss (Li et al., 2020).
Asymmetric large margin loss, similar to LDAM, is better suited for segmen-
tation tasks and has been validated with soft DSC. Specifically, we represent
the rare class with a one-hot vectorr, where thejth elementrj ∈ {0,1}is 1
if classjis rare. For example, for brain lesion segmentation, we set[0,1]to
indicate that the brain lesion class is considered rare. Based on this, the CE
and soft DSC loss are modified to:
LALM CE =−
cX
j=1
ej logh j,(D.11)
and
LALM DSC =
cX
j=1
(1−e j)hj +e j(1−h j)
hj +e j
,(D.12)
whereh j is the modified probability:
hj = ezj −e j∆jP
k ezk−ej ∆j ,(D.13)
where
61

∆j =r jC ′,(D.14)
whereC ′ is a hyper-parameter. The neural network is then optimized using
the equal sum of the CE and soft DSC losses, and the same applies to the
later asymmetric focal loss.
Balanced training II: asymmetric focal loss (Li et al., 2020).Asym-
metric focal loss builds upon the concept of focal loss but is better suited for
long-tail learning, as it removes the attenuation term for rare classes. This
adjustment helps prevent the network from under-fitting minority classes.
Specifically, the CE and soft DSC losses are modified as follows:
LAF CE =−
cX
j=1
rjej logp j −
cX
j=1
(1−r j)(1−p j)γej logp j,(D.15)
and
LAF DSC =
cX
j=1
(1−e j)pj +r jej(1−p j)
pj +e j
+
cX
j=1
(1−e j)pj + (1−r j)(1−p j)γej(1−p j)
pj +e j
.
(D.16)
Robust training I: global intensity non-linear augmentation (GIN)
technique (Ouyang et al., 2022a).GIN is a random kernel-based domain
generalization method that transforms images into random styles. Given an
image patchx, it transforms it into˜xusing:
˜x= βg(x+ (1−β)x) ∥βg(x+ (1−β)x)∥ F ∥x∥F ,(D.17)
where∥ · ∥F denotes the Frobenius norm,g(·)represents a shadow CNN with
randomly initialized parameters, andβis a parameter sampled from a uni-
form distribution. In this way, the network can be robust to various kinds
of intensity transformations. We find that GIN helps neural networks gen-
eralize better across different appearances but performs worse with spatial
transformations. Therefore, to ensure a fair comparison, we exclude all spa-
tial transformation-based synthetic domain shifts when evaluating advanced
training strategies, including GIN.
Robust training II: mixup (Zhang et al., 2017).Mixup extends the
distributions of the training dataset by combining two individual samples. In
62

addition to{x,e}, it requires another pair{x′,e ′}and creates a new sample
with:
˜x=λx+ (1−λ)x ′, ˜e=λe+ (1−λ)e ′,(D.18)
whereλis a parameter sampled from a beta distribution.
Appendix D.3. Fine-Grained Performance Analysis
To evaluate the proposed algorithms, we compare the estimated results
with the actual metrics and compute the MAE. For class-wise metrics beyond
accuracy, we report the average MAE across different classes. To assess
the significance between methods, we perform a paired t-test on the MAE
values obtained under different conditions using each method. We exclude
the evaluation of classes that are absent during testing, particularly in the
task of skin lesion classification, where some classes may be missing at test
time. For segmentation, we exclude the background class when evaluating
the model’s performance.
For a comprehensive analysis of the estimation results, we provide exam-
ples at the class, instance, and pixel levels. For class-wise performance, we
group the confidence scores by the predicted class, calculate their averages,
and compare these averages to the corresponding accuracy of the samples.
In instance-wise analysis for segmentation tasks, we evaluate performance on
a case-by-case basis rather than as a whole. For pixel-wise analysis, we visu-
alize the calibrated confidence scores adjusted by the F1-Score, highlighting
uncertain regions as1−ˆqi. For 3D confidence score visualization, we display
pixels with uncertainty greater than 0.1 and set the cluster transparency to
0.005.
63

Appendix E. Supplementary Tables
Accuracy F1-Score Sensitivity Precision AUC Advanced Training Reduced Data Total
Classification 197 197 197 197 197 380 2375 3740
2D Segmentation 69 69 69 69 69 0 276 621
3D Segmentation 183 183 183 183 183 216 1080 2211
Total 449 449 449 449 449 596 3731 6572
Table E.3: Summary of experimental results covered in the main body.
nv (%) mel (%) bcc (%) df (%) bkl (%) vasc (%) akiec (%) Total
HAM 6705 (67) 1113 (11) 514 (5) 115 (1) 1099 (11) 142 (1) 327 (3) 10015
BCN 4206 (34) 2857 (23) 2809 (23) 124 (1) 1138 (9) 111 (1) 1168 (9) 12413
VIE 4331 (99) 34 (1) 0 0 0 0 0 4365
MSK 2202 (62) 826 (23) 30 (1) 5 (<1) 470 (13) 0 7 (<1) 3540
UDA 408 (67) 193 (31) 3 (<1) 2 (<1) 7 (1) 0 0 613
OTH 4523 (55) 1669 (20) 513 (6) 124 (2) 889 (11) 95 (1) 388 (5) 8201
D7P 1150 (60) 501 (26) 84 (4) 40 (2) 90 (5) 58 (3) 0 1923
PH2 160 (80) 40 (20) 0 0 0 0 0 200
Table E.4: Dataset statistics of skin lesion classification datasets used in this study. nv:
Melanocytic nevi, mel: Melanoma, bcc: Basal cell carcinoma, df: Dermatofibroma, bkl:
Benign keratosis, vasc: Vascular skin lesions, akiec: Actinic Keratoses (Solar Keratoses)
and Intraepithelial Carcinoma (Bowen’s disease).
64

Evaluation
Metric and
Dataset
Confidence Score
Estimation
Algorithm
Class-Agnostic Class-Specific MOVAL
EnsembleMCP Energy Entropy Doctor MCP Energy Entropy Doctor
Sensitivity
CIFAR10
Synthetic-95
Vanilla 32.3±5.231.4±3.230.6±5.135.9±5.7— — — —
9.5 ±3.6
TS 20.8±3.724.6±5.521.3±3.721.6±3.512.2±5.515.4±6.911.8±5.110.9±4.4
DoC 21.9±4.222.9±4.621.7±4.222.6±4.513.8±6.113.1±5.813.3±5.814.5±6.3
ATC 18.9±3.025.0±3.919.1±3.118.9±3.09.5 ±3.810.8±4.29.4±3.79.4±3.7
TS-ATC 21.2±3.727.7±4.922.9±3.422.6±3.410.2±4.412.0±4.810.2±3.810.0±3.6
CIFAR100
Synthetic-95
Vanilla 41.6±4.615.1±4.052.5±4.761.9±4.9— — — —
15.1±4.0
TS 17.0±2.223.4±2.319.6±2.115.9±2.017.1±4.623.4±5.618.1±4.719.0±3.9
DoC 16.8±2.421.3±2.219.1±2.420.9±2.518.4±4.616.8±5.219.2±4.820.3±5.0
ATC14.3±2.318.0±2.014.4 ±2.214.3±2.215.6±4.116.1±4.215.4±4.015.7±4.2
TS-ATC 15.4±2.120.3±2.117.5±2.016.4±2.015.6±4.016.6±4.716.0±3.915.8±3.8
HAM10000
Natural-7
Vanilla 44.4±11.634.6±22.539.5±11.141.9±10.9— — — —
23.0 ±15.1
TS 37.1±11.653.2±12.535.3±11.531.0±11.828.1±14.934.9±15.225.7±15.423.9±15.3
DoC 41.2±11.545.3±11.637.8±11.439.0±11.329.8±14.530.5±15.227.7±14.728.8±14.4
ATC 24.9±13.024.5±12.824.5±13.124.8±13.124.0±15.323.2±14.723.2±14.823.8±15.0
TS-ATC 23.6±11.532.1±11.323.7±12.923.8±13.023.6±15.523.6±13.824.2±14.622.5±14.8
Precision
CIFAR10
Synthetic-95
Vanilla 32.7±6.749.2±3.833.2±6.931.5 ±6.2— — — —
31.6±7.0
TS 37.1±7.236.3±7.137.0±7.137.7±6.832.4±7.332.5±6.931.8±7.034.9±6.2
DoC 36.6±7.136.6±7.236.6±7.136.5±7.131.3±7.132.2±6.931.3±7.131.7±7.0
ATC — — — — — — — —
TS-ATC — — — — — — — —
CIFAR100
Synthetic-95
Vanilla 34.6±1.426.3±2.438.8±1.645.3±1.8— — — —
22.0±3.5
TS 26.3±2.226.8±2.326.2±2.326.0±2.122.0±3.623.3±3.122.1±3.622.7±3.1
DoC 26.7±2.226.4±2.326.7±2.227.0±2.221.8±3.422.1±3.421.9 ±3.422.1±3.4
ATC — — — — — — — —
TS-ATC — — — — — — — —
HAM10000
Natural-7
Vanilla 24.1±12.521.2±11.120.9±12.023.6±12.2— — — —
18.7±9.4
TS 18.6±11.722.5±13.618.3 ±11.518.2±10.818.8±9.420.2±10.618.6±9.322.5±9.9
DoC 20.0±12.419.7±12.419.1±11.919.9±12.019.3±9.520.0±10.319.8±9.819.2±9.4
ATC — — — — — — — —
TS-ATC — — — — — — — —
Table E.5: Evaluation of sensitivity and precision estimation for different classification
tasks under various types of domain shifts based on MAE. The best and second-best
results within the same category are inboldand underlinedfor each configuration.
65

Evaluation
Metric and
Dataset
Confidence Score
Estimation
Algorithm
Class-Agnostic Class-Specific MOVAL
EnsembleMCP Energy Entropy Doctor MCP Energy Entropy Doctor
F1-Score
CIFAR10
Synthetic-95
Vanilla 40.2±7.416.0±2.938.9±7.342.4±7.7— — — —
8.5±3.1
TS 22.3±6.028.7±8.121.6±6.019.4±5.911.8±5.515.1±6.811.3±5.010.2±4.1
DoC 26.4±7.124.9±6.825.9±6.927.3±7.514.0±6.413.1±5.813.5±6.214.9±6.9
ATC 17.1±4.417.2±6.117.3±4.517.1±4.48.5±3.111.6±4.88.7 ±3.28.5±3.1
TS-ATC 16.4±6.019.4±6.816.3±5.416.3±5.49.8±3.813.2±5.810.7±4.410.0±3.7
CIFAR100
Synthetic-95
Vanilla 56.6±4.215.9±3.164.6±4.370.4±4.4— — — —
12.7 ±2.6
TS 21.5±3.931.7±4.625.1±4.215.5±3.114.6±3.422.7±4.515.9±3.617.2±2.5
DoC 22.8±4.228.4±4.526.4±4.529.2±4.616.7±3.514.5±4.017.1±3.818.2±4.1
ATC 14.7±3.116.5±2.914.3±3.014.7±3.112.8±2.614.1±2.912.6±2.512.9±2.6
TS-ATC 13.9±4.219.8±3.415.9±2.714.4±2.613.3±2.614.3±3.014.2±2.813.4±2.6
HAM10000
Natural-7
Vanilla 52.6±15.129.9±20.248.3±14.050.8±14.1— — — —
23.2 ±15.1
TS 44.6±14.356.5±17.243.0±13.639.2±12.533.5±15.638.0±17.329.7±15.525.6±15.3
DoC 48.6±15.050.6±15.645.6±14.146.9±14.234.2±16.534.3±16.131.7±16.233.5±16.3
ATC 33.2±12.729.9±11.232.7±12.733.5±12.723.7±15.525.5±13.323.1±14.423.5±15.1
TS-ATC 31.6±13.637.6±12.230.6±12.131.3±12.123.5±14.528.3±13.925.4±13.622.9±14.9
AUC
CIFAR10
Synthetic-95
Vanilla 6.8±2.89.4±1.96.5±2.87.2±2.9— — — —
3.0±1.1
TS 3.6 ±1.83.6±0.83.7±1.94.0±2.13.8±2.35.1±2.63.7±2.33.8±2.3
DoC 6.3±1.73.9±1.75.9±1.67.3±1.94.6±2.83.7±1.64.4±2.74.8±2.9
ATC — — — — — — — —
TS-ATC — — — — — — — —
CIFAR100
Synthetic-95
Vanilla 9.2±2.217.4±1.68.9±2.510.3±2.8— — — —
6.5±0.7
TS 10.3±0.614.0±1.79.9±0.710.3±1.57.9±1.77.1±2.56.8±1.77.0±1.9
DoC 13.7±1.811.6±1.316.2±2.218.4±2.57.2±2.37.3±1.46.6 ±2.46.8±2.6
ATC — — — — — — — —
TS-ATC — — — — — — — —
HAM10000
Natural-7
Vanilla 20.2±6.913.7±5.919.1±6.620.3±6.9— — — —
14.7 ±3.4
TS 17.0±6.615.6±8.517.6±6.418.6±6.216.0±2.615.8±7.117.0±1.517.9±2.4
DoC 16.1±6.716.1±7.516.6±6.616.4±6.716.8±7.015.7±2.416.6±6.816.9±7.1
ATC — — — — — — — —
TS-ATC — — — — — — — —
Table E.6: Evaluation of F1-Score and AUC estimation for different classification tasks
under various types of domain shifts based on MAE. The best and second-best results
within the same category are inboldand underlinedfor each configuration.
Dataset
and Training
Strategy
Confidence Score
Estimation
Algorithm
Class-Agnostic Class-Specific MOVAL
EnsembleMCP Energy Entropy Doctor MCP Energy Entropy Doctor
CIFAR10
Synthetic-95
Vanilla
Training
Vanilla 57.0±10.48.6±5.354.5±10.461.1±10.5— — — —
—
TS 28.8±9.639.4±9.527.2±9.924.2±11.127.4±4.435.9±6.124.3±3.718.9±3.4
DoC 36.1±10.432.4±8.535.0±10.437.4±10.534.1±5.528.9±4.532.9±5.335.2±5.6
ATC 23.1±11.320.2±10.122.9±11.423.2±11.315.7±4.111.2 ±5.214.7±4.215.2±4.1
TS-ATC 21.5±9.918.1±9.121.4±11.321.4±11.414.3±3.410.5±6.414.0±3.413.7±3.5
Table E.7: Evaluation of accuracy estimation for different classification tasks under various
types of domain shifts based on MAE. The test datasets include only samples from the 2
most minority classes. The best and second-best results within the same category are in
boldand underlined for each configuration.
66

Evaluation
Metric and
Dataset
Confidence Score
Estimation
Algorithm
Class-Agnostic Class-Specific MOVAL
EnsembleMCP Energy Entropy Doctor MCP Energy Entropy Doctor
Sensitivity
Cardiac-2D
Synthetic-65
Vanilla 15.1±6.562.3±9.212.4±5.914.5±6.3— — — —
3.3±2.5
TS 9.8±5.818.8±7.87.4±5.38.1±5.34.4±3.76.0±6.34.2±3.24.1±3.1
DoC 14.4±6.513.5±7.011.8±5.913.8±6.35.1±5.15.5±5.14.6±4.54.9±4.9
ATC 3.2 ±2.418.8±7.83.3±2.53.2 ±2.43.1±2.54.5±5.93.1±2.53.1±2.5
TS-ATC 3.5±5.318.8±7.83.5±2.73.5±2.83.4±3.46.4±9.13.4±3.43.4±3.5
Natural-4
Vanilla 11.1±1.566.2±2.69.1±1.510.7±1.5— — — —
2.9±0.2
TS 7.1±1.613.7±1.75.6±1.46.1±1.64.3±0.44.2±0.94.3±0.34.3±0.3
DoC 10.3±1.510.1±1.88.5±1.59.9±1.54.0±0.84.5±0.63.8±0.73.9±0.8
ATC 2.9±0.113.7±1.72.9±0.12.9±0.13.6±0.14.0±0.13.6±0.13.6±0.1
TS-ATC 2.8 ±1.413.7±1.72.8 ±0.32.7±0.33.7±0.15.5±0.43.7±0.13.7±0.1
Prostate-3D
Synthetic-83
Vanilla 11.9±8.671.2±8.35.2±4.38.4±6.4— — — —
4.1±5.0
TS 7.7±7.112.8±10.33.0±2.93.7±3.54.7±6.67.2±10.33.8±3.23.8±3.5
DoC 11.7±8.65.3±8.35.1±4.38.2±6.46.1±8.65.4±8.34.1±4.14.8±6.2
ATC 3.7±4.714.7±10.53.7±4.73.7±4.73.5 ±2.33.5 ±2.33.5 ±2.33.5 ±2.3
TS-ATC 3.7±2.98.3±6.43.7±4.73.7±4.73.5 ±2.33.7±2.63.5 ±2.33.5 ±2.3
Natural-5
Vanilla 11.6±3.871.9±4.26.6±1.76.8±4.5— — — —
5.6±0.7
TS 6.3±4.713.8±3.36.4±5.96.4±3.65.4±1.88.2±3.36.5±3.86.4±3.3
DoC 11.4±3.85.2±3.56.5±1.76.7±4.45.8±3.85.3 ±3.56.2±2.55.6±1.5
ATC 10.4±10.015.8±3.210.4±10.010.4±10.07.1±6.47.1±6.47.1±6.47.1±6.4
TS-ATC 10.4±5.915.4±10.310.4±10.010.4±10.07.1±6.46.6±6.17.1±6.47.1±6.4
Brain Lesion-3D
Synthetic-83
Vanilla 20.2±6.575.6±6.912.6±5.916.3±6.4— — — —
2.8±4.8
TS 15.9±6.323.3±7.010.7±5.411.5±5.72.9 ±5.63.1±6.93.7±6.13.6±6.0
DoC 20.1±6.523.3±7.012.6±5.916.3±6.42.8±6.13.0±6.93.2±5.73.0±5.7
ATC 9.4±4.823.3±7.09.4±4.89.4±4.84.4±7.34.4±7.34.4±7.34.4±7.3
TS-ATC 9.4±5.423.3±7.09.4±4.89.4±4.84.4±7.34.1±6.84.4±7.34.4±7.3
Natural-12
Vanilla 52.4±14.837.8±17.042.4±12.447.2±13.0— — — —
29.3±14.3
TS 47.9±14.556.5±16.240.0±12.341.4±12.434.8±15.537.8±17.429.3±12.729.6±12.8
DoC 52.3±14.856.5±16.242.4±12.447.1±13.035.5±15.937.6±17.331.1±13.432.8±14.2
ATC 35.6±11.356.5±16.235.6±11.335.6±11.327.4±11.927.2 ±11.927.4±11.927.4±11.9
TS-ATC 35.6±12.356.5±16.235.6±11.335.6±11.327.4±11.915.6±11.027.4±11.927.4±11.9
Table E.8: Evaluation of sensitivity estimation for different segmentation tasks under
various types of domain shifts based on MAE. The best and second-best results within
the same category are inboldand underlinedfor each configuration.
67

Evaluation
Metric and
Dataset
Confidence Score
Estimation
Algorithm
Class-Agnostic Class-Specific MOVAL
EnsembleMCP Energy Entropy Doctor MCP Energy Entropy Doctor
Precision
Cardiac-2D
Synthetic-65
Vanilla 9.5±1.555.0±3.78.2±0.99.3±1.3— — — —
8.4 ±0.8
TS 10.8±1.517.7±7.711.0±2.011.0±1.910.1±0.652.1±3.610.1±1.99.3±1.9
DoC 10.8±1.610.3±1.411.0±1.310.9±1.59.2±0.652.1±3.69.2±1.09.0±0.7
ATC — — — — — — — —
TS-ATC — — — — — — — —
Natural-4
Vanilla 8.6±0.556.4±2.07.5 ±0.58.4±0.3— — — —
7.0±0.9
TS 17.8±1.517.9±0.716.6±1.516.8±1.57.9±0.654.8±2.07.8±2.07.0±1.6
DoC 16.7±1.624.0±1.615.7±1.516.5±1.67.5 ±0.454.8±2.07.8±2.17.5 ±0.4
ATC — — — — — — — —
TS-ATC — — — — — — — —
Prostate-3D
Synthetic-83
Vanilla 9.3±3.411.9±5.86.5±2.88.8±3.2— — — —
3.1±4.5
TS 6.3±3.46.3±2.12.6±3.12.7 ±3.27.7±8.411.2±5.86.5±5.46.6±6.1
DoC 6.3±2.59.1±7.43.3±2.64.6±2.67.4±9.011.4±5.85.8±4.86.0±5.6
ATC — — — — — — — —
TS-ATC — — — — — — — —
Natural-5
Vanilla 17.4±9.322.3±11.711.9±7.316.1±8.8— — — —
3.7±2.7
TS 6.4±2.69.1±7.44.6 ±5.75.1±5.38.3±3.021.4±11.66.6±1.06.1±1.5
DoC 9.2±8.18.3±4.66.7±7.98.6±8.77.4±3.021.6±11.66.4±1.65.9±1.4
ATC — — — — — — — —
TS-ATC — — — — — — — —
Brain Lesion-3D
Synthetic-83
Vanilla 16.9±8.420.6±9.913.7±7.416.3±8.2— — — —
5.7±7.3
TS 11.3±5.020.6±9.99.9±7.65.8±8.63.2±5.920.4±9.94.6 ±7.55.1±7.8
DoC 22.5±7.620.6±9.912.9±6.119.4±6.83.2±5.720.4±9.94.6 ±7.34.7±7.1
ATC — — — — — — — —
TS-ATC — — — — — — — —
Natural-12
Vanilla 23.6±8.438.5±17.320.1±8.623.0±8.6— — — —
7.9±5.3
TS 12.4±9.538.5±17.313.1±8.27.9±5.96.5±4.938.3±17.412.2±8.712.4±8.5
DoC 26.1±13.838.5±17.315.2±12.623.0±13.76.8 ±4.938.3±17.410.8±8.19.9±7.4
ATC — — — — — — — —
TS-ATC — — — — — — — —
Table E.9: Evaluation of precision estimation for different segmentation tasks under var-
ious types of domain shifts based on MAE. The best and second-best results within the
same category are inboldand underlined for each configuration.
68

Evaluation
Metric and
Dataset
Confidence Score
Estimation
Algorithm
Class-Agnostic Class-Specific MOVAL
EnsembleMCP Energy Entropy Doctor MCP Energy Entropy Doctor
Accuracy
Cardiac-2D
Synthetic-65
Vanilla 0.8±0.380.9±0.20.7±0.30.8±0.3— — — —
0.3±0.5
TS 0.2 ±0.41.2±0.50.3±0.60.3±0.60.2 ±0.40.7±0.50.3±0.60.3±0.6
DoC 0.2 ±0.30.1±0.20.3±0.50.3±0.50.2 ±0.30.2 ±0.20.3±0.50.3±0.5
ATC 0.4±0.71.0±0.30.4±0.80.4±0.70.4±0.80.6±0.60.4±0.80.4±0.8
TS-ATC 0.4±0.61.2±0.50.4±0.80.4±0.80.5±0.80.9±0.40.5±0.80.5±0.8
Natural-4
Vanilla 0.5±0.081.9±0.10.4±0.00.5±0.0— — — —
0.1 ±0.0
TS 0.4±0.00.6±0.00.4±0.00.4±0.00.3±0.00.3±0.00.3±0.00.2±0.0
DoC 0.3±0.00.8±0.00.3±0.00.3±0.00.2±0.00.6±0.00.2±0.00.2±0.0
ATC0.0±0.00.6±0.00.0±0.00.0±0.00.1 ±0.00.4±0.00.1 ±0.00.1 ±0.0
TS-ATC0.0±0.00.6±0.00.0±0.00.0±0.00.1 ±0.00.5±0.00.1 ±0.00.1 ±0.0
Prostate-3D
Synthetic-83
Vanilla 0.3±0.273.9±0.30.3±0.60.4±0.5— — — —
0.2 ±0.4
TS 0.2 ±0.30.1±0.20.4±0.60.3±0.60.2 ±0.30.1±0.20.4±0.60.3±0.6
DoC 0.2 ±0.30.2 ±0.20.3±0.60.3±0.60.2 ±0.30.2 ±0.20.3±0.60.3±0.6
ATC 0.4±0.70.4±0.20.4±0.70.4±0.70.4±0.70.1±0.10.4±0.70.4±0.7
TS-ATC 0.4±0.60.4±0.60.4±0.70.4±0.70.4±0.70.4±0.60.4±0.70.4±0.7
Natural-5
Vanilla 0.5±0.274.1±0.20.1 ±0.00.3±0.1— — — —
0.0±0.0
TS0.0±0.00.3±0.20.4±0.30.3±0.20.1 ±0.00.3±0.20.4±0.30.3±0.2
DoC 0.3±0.20.3±0.20.1 ±0.10.1 ±0.10.3±0.10.2±0.10.2±0.10.1 ±0.0
ATC 0.6±0.40.7±0.30.6±0.40.6±0.40.6±0.40.2±0.10.6±0.40.6±0.4
TS-ATC 0.6±0.30.4±0.30.6±0.40.6±0.40.6±0.40.6±0.40.6±0.40.6±0.4
Brain Lesion-3D
Synthetic-83
Vanilla0.1±0.296.8±0.30.1±0.40.2 ±0.4— — — —
0.1±0.3
TS0.1±0.20.1±0.00.1±0.50.1±0.40.1±0.20.1±0.00.1±0.50.1±0.4
DoC0.1±0.20.1±0.00.1±0.40.1±0.40.1±0.20.1±0.00.1±0.40.1±0.4
ATC0.1±0.50.1±0.00.1±0.50.1±0.50.1±0.50.1±0.00.1±0.50.1±0.5
TS-ATC0.1±0.50.1±0.00.1±0.50.1±0.50.1±0.50.1±0.00.1±0.50.1±0.5
Natural-12
Vanilla 0.2 ±0.196.5±0.20.1±0.10.2 ±0.1— — — —
0.1±0.1
TS0.1±0.10.2 ±0.10.1±0.10.1±0.10.1±0.10.2 ±0.10.1±0.10.1±0.1
DoC0.1±0.10.2 ±0.10.1±0.10.1±0.10.1±0.10.2 ±0.10.1±0.10.1±0.1
ATC0.1±0.10.2 ±0.10.1±0.10.1±0.10.1±0.10.2 ±0.10.1±0.10.1±0.1
TS-ATC0.1±0.10.2 ±0.10.1±0.10.1±0.10.1±0.10.2 ±0.10.1±0.10.1±0.1
Table E.10: Evaluation of accuracy estimation for different segmentation tasks under
various types of domain shifts based on MAE. The best and second-best results within
the same category are inboldand underlinedfor each configuration.
69

Evaluation
Metric and
Dataset
Confidence Score
Estimation
Algorithm
Class-Agnostic Class-Specific MOVAL
EnsembleMCP Energy Entropy Doctor MCP Energy Entropy Doctor
AUC
Cardiac-2D
Synthetic-65
Vanilla 2.9±0.645.6±0.83.0±0.72.7±0.6— — — —
2.3±0.4
TS 4.3±1.03.1±0.84.3±1.14.1±1.02.5±0.533.1±0.62.4 ±0.42.3±0.4
DoC 3.4±0.65.0±1.33.5±0.73.2±0.62.5±0.519.2±0.32.4 ±0.42.3±0.4
ATC — — — — — — — —
TS-ATC — — — — — — — —
Natural-4
Vanilla 2.3±0.545.3±0.22.3±0.52.2 ±0.4— — — —
2.1±0.5
TS 2.8±0.32.6±0.52.7±0.32.6±0.32.2 ±0.532.5±0.22.2 ±0.52.2 ±0.5
DoC 2.5±0.43.2±0.32.5±0.42.4±0.42.2 ±0.519.1±0.32.2 ±0.52.1±0.5
ATC — — — — — — — —
TS-ATC — — — — — — — —
Prostate-3D
Synthetic-83
Vanilla 0.4 ±1.318.1±1.60.4 ±1.30.4 ±1.3— — — —
0.4 ±1.1
TS 0.6±1.00.9±1.10.5±1.20.5±1.20.4 ±1.317.5±1.50.4 ±1.30.4 ±1.3
DoC0.3±1.31.0±0.60.3±1.30.3±1.30.4 ±1.317.0±1.50.4 ±1.30.4 ±1.3
ATC — — — — — — — —
TS-ATC — — — — — — — —
Natural-5
Vanilla 1.3±0.916.6±0.71.1±0.91.3±0.9— — — —
0.9±0.9
TS 0.8 ±0.70.7±0.60.8 ±0.90.8 ±0.81.3±0.916.0±0.71.2±0.91.3±0.9
DoC 1.1±0.90.8 ±0.61.0±0.91.1±0.91.3±0.915.5±0.61.2±0.91.3±0.9
ATC — — — — — — — —
TS-ATC — — — — — — — —
Brain Lesion-3D
Synthetic-83
Vanilla 0.9±1.52.6±0.50.7±1.50.9±1.5— — — —
0.5±1.4
TS 0.6 ±1.31.1±1.50.6 ±1.50.5±1.50.5±1.42.2±0.70.5±1.50.5±1.5
DoC 0.8±1.51.1±1.50.6 ±1.50.8±1.50.5±1.52.1±0.70.5±1.50.5±1.5
ATC — — — — — — — —
TS-ATC — — — — — — — —
Natural-12
Vanilla 6.0±4.46.0±5.06.7±4.96.5±4.7— — — —
5.4±4.4
TS5.4±4.46.2±4.56.7±5.06.6±4.95.4±4.36.2±5.16.5±4.96.1±4.7
DoC 5.9±4.46.2±4.56.6±4.96.4±4.75.5 ±4.46.3±5.16.5±4.96.1±4.7
ATC — — — — — — — —
TS-ATC — — — — — — — —
Table E.11: Evaluation of AUC estimation for different segmentation tasks under various
types of domain shifts based on MAE. The best and second-best results within the same
category are inboldand underlined for each configuration.
70

Dataset
and Training
Strategy
Confidence Score
Estimation
Algorithm
Class-Agnostic Class-Specific MOVAL
EnsembleMCP Energy Entropy Doctor MCP Energy Entropy Doctor
CIFAR10
Synthetic-95
Balanced
Training I
Vanilla 25.2±8.221.8±8.549.8±10.313.0±2.7— — — —
11.5±6.4
TS 27.9±8.032.9±11.027.3±7.827.7±8.215.7±7.723.5±11.914.3±6.914.4±7.4
DoC 31.5±10.232.8±11.031.9±10.329.6±9.119.9±9.923.5±11.920.4±10.216.0±7.8
ATC 22.0±5.636.5±10.328.3±8.826.7±8.19.4 ±6.229.0±14.313.3±7.112.0±6.6
TS-ATC 22.3±7.836.5±10.322.2±5.125.5±7.48.8±5.029.1±14.38.8±5.211.6±6.7
Balanced
Training II
Vanilla 36.6±8.217.3±4.735.3±7.939.0±8.5— — — —
8.0±3.2
TS 21.9±6.327.6±9.021.3±6.019.6±5.211.1±5.215.7±8.110.4±4.59.3±3.8
DoC 25.5±7.924.2±7.425.0±7.626.4±8.313.9±7.012.8±6.113.4±6.615.0±7.7
ATC 18.5±4.716.3±4.818.3±4.618.5±4.78.1 ±3.29.8±3.28.0±3.28.1 ±3.2
TS-ATC 16.9±6.017.2±5.716.1±4.216.2±4.38.4±3.212.6±4.99.1±3.38.8±3.3
Robust
Training I
Vanilla 39.7±9.117.3±4.738.2±8.944.4±10.1— — — —
10.5 ±5.8
TS 25.1±7.432.5±10.824.6±7.223.4±6.714.2±6.620.0±10.113.6±6.312.8±6.0
DoC 28.9±8.728.7±9.128.3±8.431.2±9.816.9±8.016.8±8.016.3±7.619.3±9.3
ATC 20.8±5.318.0±5.320.2±5.320.7±5.310.8±6.212.9±5.910.6±6.310.3±5.7
TS-ATC 18.7±7.221.5±6.217.8±5.817.4±6.311.5±7.015.2±6.311.7±6.512.2±6.7
Robust
Training II
Vanilla 33.1±6.021.5±4.531.6±5.836.2±6.4— — — —
7.4±3.8
TS 20.2±4.926.1±7.119.6±5.017.7±5.310.3±4.614.9±6.49.9±4.49.5±4.1
DoC 23.2±5.822.9±5.922.5±5.624.3±6.212.2±5.112.4±5.411.6±4.913.3±5.7
ATC 17.5±4.317.4±5.516.4±4.517.4±4.37.4±3.912.5±6.47.4±3.87.4±3.9
TS-ATC 15.5±5.019.4±6.315.9±4.616.0±4.79.2 ±5.014.9±6.910.6±6.210.5±6.2
Table E.12: Evaluation of F1-Score estimation for CIFAR10 classification under different
training strategies based on MAE. The best and second-best results within the same
category are inboldand underlined for each configuration.
71

Dataset
and Training
Strategy
Confidence Score
Estimation
Algorithm
Class-Agnostic Class-Specific MOVAL
EnsembleMCP Energy Entropy Doctor MCP Energy Entropy Doctor
CIFAR10
Synthetic-95
Balanced
Training I
Vanilla 37.3±9.38.3±7.252.4±9.420.2±8.9— — — —
12.4±11.7
TS 12.4±7.722.5±10.911.2±7.710.5±9.413.6±10.320.2±13.612.7±10.311.1±10.7
DoC 18.4±9.322.4±10.919.0±9.414.0±9.318.2±11.920.2±13.618.8±12.214.3±11.0
ATC4.5±6.026.4±12.98.1±9.88.0±8.76.4±8.823.1±17.18.3±9.88.2±9.5
TS-ATC 5.8±7.726.5±12.95.3 ±5.47.6±8.07.5±8.923.1±17.17.3±9.18.0±9.1
Balanced
Training II
Vanilla 30.5±7.931.9±6.628.3±7.634.6±8.2— — — —
5.5±6.9
TS 8.1±6.215.0±8.47.4±5.65.9±4.69.7±9.315.5±10.78.8±9.07.4±8.5
DoC 13.0±7.910.3±6.812.3±7.614.1±8.213.6±9.911.5±9.312.9±9.614.6±10.3
ATC 5.9±5.44.3 ±2.65.7±5.25.9±5.46.7±8.65.2±5.76.3±7.86.6±8.4
TS-ATC 4.4±5.64.8±3.33.9±2.93.9±3.05.8±8.05.1±4.65.5±7.25.6±7.3
Robust
Training I
Vanilla 30.8±7.130.4±7.028.3±6.838.8±8.3— — — —
4.0±3.1
TS 9.2±5.418.6±9.28.4±5.36.9±5.110.1±7.117.8±10.69.1±6.97.7±6.4
DoC 14.4±7.113.0±7.113.5±6.817.3±8.314.2±8.113.1±8.713.4±7.816.5±9.2
ATC 5.4±4.44.8±3.44.6±4.45.2±4.44.7±4.15.0±2.94.4±3.74.3±3.7
TS-ATC 3.9 ±5.34.3±4.24.4±2.64.8±2.94.0±3.66.0±3.63.5±2.93.5±2.4
Robust
Training II
Vanilla 24.9±4.836.8±4.522.2±4.729.9±5.1— — — —
5.5±4.2
TS 5.6±4.312.8±5.94.9±4.35.1±4.04.4±2.610.5±5.23.5±2.33.0±2.8
DoC 9.6±4.88.0±4.68.5±4.710.7±5.17.8±3.76.6±3.66.9±3.48.7±4.0
ATC 4.6±3.78.8±6.84.2±3.54.5±3.62.4±2.17.8±6.03.2±2.52.5 ±2.2
TS-ATC 5.1±4.310.8±8.26.3±4.76.4±4.83.9±3.08.3±6.34.9±3.74.7±3.5
Table E.13: Evaluation of accuracy estimation for CIFAR10 classification under different
training strategies based on MAE. The proposed CS variants underperform in accuracy
estimation compared to their counterparts when models are trained using advanced bal-
anced training strategies. We observe that balanced training strategies largely affect the
model’s predicted probabilities, resulting in a more significant difference in the confusion
matrix when exposed to domain shifts. These changes, in particular, create difficulties
for CS variants, as they rely on predictions to choose class parameters. In such cases, we
recommend performing class-wise calibration with group-wise parameters (c.f. Table E.14)
or alternatively tracking the F1-Score. The best and second-best results within the same
category are inboldand underlined for each configuration.
72

Dataset
and Training
Strategy
Confidence Score
Estimation
Algorithm
Class-Agnostic Class-Specific MOVAL
EnsembleMCP Energy Entropy Doctor MCP Energy Entropy Doctor
CIFAR10
Synthetic-95
Balanced
Training I
Vanilla 37.3±9.38.3±7.252.4±9.420.2±8.9— — — —
11.5±6.9
TS 12.4±7.722.5±10.911.2±7.710.5±9.412.2±7.420.7±9.811.1±7.510.6±9.3
DoC 18.4±9.322.4±10.919.0±9.414.0±9.317.6±8.720.7±9.818.2±8.913.8±9.1
ATC4.5±6.026.4±12.98.1±9.88.0±8.74.7 ±6.024.2±11.28.3±10.28.1±9.1
TS-ATC 5.8±7.726.5±12.95.3±5.47.6±8.05.4±5.224.2±11.25.3±5.47.8±8.4
Balanced
Training II
Vanilla 30.5±7.931.9±6.628.3±7.634.6±8.2— — — —
3.7 ±3.0
TS 8.1±6.215.0±8.47.4±5.65.9±4.68.0±5.814.5±8.07.1±5.45.5±4.6
DoC 13.0±7.910.3±6.812.3±7.614.1±8.212.8±7.510.0±6.412.0±7.213.7±7.8
ATC 5.9±5.44.3±2.65.7±5.25.9±5.45.7±5.53.9±2.35.1±5.15.6±5.4
TS-ATC 4.4±5.64.8±3.33.9±2.93.9±3.04.2±3.94.6±3.03.6±3.03.6±3.0
Robust
Training I
Vanilla 30.8±7.130.4±7.028.3±6.838.8±8.3— — — —
3.7±3.0
TS 9.2±5.418.6±9.28.4±5.36.9±5.18.6±4.817.7±8.77.7±4.76.3±4.5
DoC 14.4±7.113.0±7.113.5±6.817.3±8.313.8±6.612.4±6.712.9±6.216.5±7.7
ATC 5.4±4.44.8±3.44.6±4.45.2±4.44.0±3.54.3±3.33.5 ±3.43.9±3.5
TS-ATC 3.9±5.34.3±4.24.4±2.64.8±2.93.3±2.84.4±4.13.9±2.44.0±2.5
Robust
Training II
Vanilla 24.9±4.836.8±4.522.2±4.729.9±5.1— — — —
6.4±5.1
TS 5.6±4.312.8±5.94.9±4.35.1±4.05.1±3.812.0±5.44.6±3.95.0±3.6
DoC 9.6±4.88.0±4.68.5±4.710.7±5.18.8±4.47.6±4.37.8±4.39.9±4.7
ATC 4.6±3.78.8±6.84.2±3.54.5±3.63.7±3.08.6±6.74.0±3.13.8 ±3.0
TS-ATC 5.1±4.310.8±8.26.3±4.76.4±4.85.0±3.710.7±8.26.0±4.86.1±4.9
Table E.14: Related to Extended Table E.13. Evaluation of accuracy estimation for CI-
FAR10 classification under different training strategies based on MAE. To achieve stable
estimation in complex scenarios, we employ a group-wise optimization strategy. Specifi-
cally, we estimate two parameters for the CS variants: one shared by the 8 classes with
the highest number of predicted samples, and another shared by the remaining 2 classes.
Compared to CS variants applied to individual classes, this technique reduces the number
of required validation samples and mitigates the complexity of the confusion matrix (e.g.,
misclassifications within a group have less impact on the estimation results). In this ways,
the CS variants can effectively generalize with advanced balanced training strategies. The
best and second-best results within the same category are inboldand underlinedfor each
configuration.
73

Dataset
and Training
Strategy
Confidence Score
Estimation
Algorithm
Class-Agnostic Class-Specific MOVAL
EnsembleMCP Energy Entropy Doctor MCP Energy Entropy Doctor
Brain Lesion-3D
Synthetic-42
Balanced
Training I
Vanilla 24.8±9.770.2±10.021.6±7.523.3±8.5— — — —
2.6 ±4.2
TS 22.5±8.925.9±10.519.6±6.820.2±7.15.8±9.06.6±10.42.8±4.72.9±4.8
DoC 24.8±9.725.9±10.521.5±7.523.2±8.55.8±9.26.5±10.24.0±6.84.8±7.9
ATC 17.1±5.225.9±10.517.1±5.217.1±5.22.7±4.02.7±4.02.7±4.02.7±4.0
TS-ATC 17.1±6.825.9±10.517.1±5.217.1±5.22.7±4.02.5±3.42.7±4.02.7±4.0
Balanced
Training II
Vanilla 26.4±14.652.4±12.220.5±10.023.4±12.1— — — —
2.5 ±3.8
TS 24.0±13.428.6±16.318.7±9.019.7±9.78.9±13.710.3±16.13.3±5.13.6±5.5
DoC 26.4±14.624.7±15.120.5±10.023.4±12.18.9±13.99.4±14.55.6±8.97.1±11.2
ATC 15.9±6.528.5±16.315.9±6.515.9±6.51.6±2.41.6±2.31.6±2.41.6±2.4
TS-ATC 15.9±9.028.6±16.315.9±6.515.9±6.51.6±2.41.6±2.11.6±2.41.6±2.4
Robust
Training I
Vanilla 27.6±15.467.6±18.415.2±6.821.7±9.8— — — —
2.8 ±4.5
TS 26.7±15.031.3±18.720.9±9.022.1±10.010.0±15.811.9±18.62.7±4.82.9±5.2
DoC 27.5±15.331.3±18.719.6±8.221.8±9.88.9±14.011.8±18.53.0±5.65.0±8.3
ATC 13.6±6.231.3±18.713.6±6.213.6±6.23.1±4.83.1±4.83.1±4.83.1±4.8
TS-ATC 13.6±9.031.3±18.713.6±6.213.6±6.23.1±4.83.7±5.83.1±4.83.1±4.8
Robust
Training II
Vanilla 30.5±17.963.3±19.321.2±11.326.0±14.3— — — —
3.5±5.5
TS 27.5±16.833.6±20.321.8±11.622.7±12.411.7±17.613.5±20.24.5±7.14.9±7.6
DoC 30.4±17.932.1±20.021.5±11.426.0±14.311.3±17.013.2±19.96.5±9.98.7±13.0
ATC 17.7±7.733.6±20.317.7±7.717.7±7.72.4±4.32.4±4.32.4±4.32.4±4.3
TS-ATC 17.7±11.633.6±20.317.7±7.717.7±7.72.4±4.32.7 ±3.72.4±4.32.4±4.3
Natural-12
Balanced
Training I
Vanilla 52.5±15.338.3±18.748.7±13.350.7±14.2— — — —
29.6 ±11.5
TS 50.2±14.853.8±15.946.6±12.747.3±13.034.5±15.635.1±16.630.3±12.230.5±12.3
DoC 52.5±15.353.8±15.948.7±13.350.6±14.233.9±15.735.0±16.531.4±13.432.5±14.3
ATC 43.6±11.153.8±15.943.6±11.143.6±11.129.7±11.929.5±11.829.7±11.929.7±11.9
TS-ATC 43.6±12.753.8±15.943.6±11.143.6±11.129.7±11.927.4±10.329.7±11.929.7±11.9
Balanced
Training II
Vanilla 51.6±15.427.5±13.544.2±12.447.7±13.7— — — —
22.7±9.7
TS 48.7±14.854.2±16.542.1±11.843.2±12.333.9±15.636.6±16.924.5±10.425.1±10.6
DoC 51.5±15.449.8±15.944.2±12.447.6±13.734.5±15.434.8±16.029.7±12.131.8±13.5
ATC 39.0±10.054.2±16.539.0±10.039.0±10.018.1 ±8.318.0±8.318.1 ±8.318.1 ±8.3
TS-ATC 39.0±11.854.2±16.539.0±10.039.0±10.018.1 ±8.318.0±8.318.1 ±8.318.1 ±8.3
Robust
Training I
Vanilla 47.7±14.545.1±18.938.1±12.643.1±12.8— — — —
28.6±15.0
TS 47.0±14.450.8±15.342.5±12.643.3±12.831.6±15.932.0±16.527.6±13.627.7±13.6
DoC 47.7±14.550.8±15.341.5±12.843.1±12.830.0±15.132.0±16.526.6 ±13.327.5±13.5
ATC 37.4±11.650.7±15.337.4±11.637.4±11.625.5±15.325.5±15.325.5±15.325.5±15.3
TS-ATC 37.4±12.650.8±15.337.4±11.637.4±11.625.5±15.328.9±18.225.5±15.325.5±15.3
Robust
Training II
Vanilla 50.5±14.341.8±14.241.9±13.045.9±13.4— — — —
26.9±13.2
TS 47.7±14.253.4±14.842.4±13.043.1±13.232.7±15.134.0±15.726.7±13.127.0±13.1
DoC 50.4±14.352.0±14.842.2±13.045.9±13.432.0±14.933.8±15.628.1±13.529.6±14.0
ATC 39.6±12.253.4±14.839.6±12.239.6±12.225.6±13.125.6±13.125.6±13.125.6±13.1
TS-ATC 39.6±13.053.4±14.839.6±12.239.6±12.225.6±13.126.3 ±14.225.6±13.125.6±13.1
TableE.15: EvaluationofF1-Scoreestimationforbrainlesionsegmentationunderdifferent
training strategies based on MAE. The best and second-best results within the same
category are inboldand underlined for each configuration.
74

Estimating
Metric
Group-Wise
Calibration
Samples Used for Estimating
3000 (100%) 1500 (50%) 600 (20%) 300 (10%) 150 (5%) 90 (3%)
Accuracy No 2.8±2.12.8±2.32.9±2.33.4±2.13.9±3.04.6±3.6
Sensitivity No 9.5±3.69.7±3.511.0±3.612.2±4.016.4±4.425.2±8.1
Precision No 31.6±7.032.0±7.231.7±6.832.0±7.031.9±6.832.8±7.2
F1-Score No 8.5±3.18.7±3.010.5±3.811.4±4.215.4±4.420.4±6.2
AUC No 3.0±1.13.0±1.13.3±1.43.6±1.63.8±1.84.0±2.0
Accuracy 5 Groups 2.9±2.12.9±2.23.0±2.43.2±2.43.1±2.23.9±3.0
Sensitivity 5 Groups 10.8±4.310.8±4.411.5±4.112.4±4.414.5±4.415.6±4.6
Precision 5 Groups 32.7±7.132.7±7.132.8±7.232.8±7.232.9±7.232.9±7.3
F1-Score 5 Groups 8.4±3.48.6±3.49.3±3.69.7±3.713.4±4.414.2±4.7
AUC 5 Groups 3.2±1.23.2±1.33.4±1.53.7±1.83.7±1.84.0±2.0
Table E.16: MAE of estimation results for CIFAR10 classification when MOVAL Ensemble
is optimized with different amounts of validation data. For group-wise calibration, we split
the 10 cases into 5 groups, with each group containing 2 classes.
Dataset Samples Used for Estimating 19 (100%) 12 (63%) 6 (32%) 3 (16%) 2 (11%) 1 (5%)
Synthetic-65 4.3±5.04.6±4.44.7±4.65.4±4.26.2±3.38.3±2.4
Natural-4 2.6±0.42.6±0.33.3±0.33.6±0.34.2±0.26.5±0.4
Average 3.5 3.6 4.0 4.5 5.2 7.4
Table E.17: MAE of F1-Score estimation results for cardiac segmentation when MOVAL
Ensemble is optimized with different amounts of validation data.
75

Dataset Training Strategy Samples Used for Estimating 9 (100%) 6 (66%) 3 (33%) 2 (22%) 1 (11%)
Synthetic-42
Vanilla 0.5±0.62.9±0.34.0±0.45.8±0.113.5±0.3
Balanced Training I 0.5±0.53.4±0.13.8±0.16.5±0.214.3±0.4
Balanced Training II 0.2±0.31.5±0.13.5±0.45.4±0.28.4±0.2
Robust Training I 0.9±0.74.4±0.34.3±0.38.8±0.421.0±0.8
Robust Training II 0.6±0.63.8±0.43.6±0.26.8±0.115.0±0.2
Natural-12
Vanilla 25.5±12.325.1±12.529.2±12.029.3±12.426.3±12.1
Balanced Training I 29.6±11.529.1±11.631.3±11.629.5±11.927.2±11.3
Balanced Training II 22.7±9.722.0±9.826.9±9.626.6±9.824.3±10.2
Robust Training I 28.6±15.029.4±14.531.0±14.428.5±14.326.5±11.4
Robust Training II 26.9±13.226.9±13.028.1±13.227.3±13.025.8±12.1
Average
Vanilla 13.0 14.0 16.6 17.6 19.9
Balanced Training I 15.0 16.2 17.5 18.0 20.8
Balanced Training II 11.5 11.8 15.2 16.0 16.4
Robust Training I 14.8 16.9 17.6 18.7 23.7
Robust Training II 13.8 15.4 15.9 17.0 20.4
Table E.18: MAE of F1-Score estimation results for brain lesion segmentation under dif-
ferent training strategies when MOVAL Ensemble is optimized with different amounts of
validation data.
76

Estimating
Metric
Classification
Choice 1 Choice 2 Choice 3
Accuracy MCP|CS TS-ATC ENT|CS TS-ATC ENE|CS ATC
Sensitivity DOC|CS TS-ATC ENT|CS ATC MCP|CS ATC
Precision DOC|CS TS MCP|CS DoC DOC|CS DoC
F1-Score DOC|CS ATC ENT|CS ATC MCP|CS ATC
AUC ENT|CS TS DOC|CS TS DOC|CS DoC
Estimating
Metric
Segmentation-2D
Choice 1 Choice 2 Choice 3
F1-Score ENT|CS DoC DOC|CS DoC MCP|CS ATC
Sensitivity MCP|ATC MCP|TS-ATC DOC|ATC
Precision ENT|CS TS MCP|CS DoC ENT|CS DoC
Accuracy MCP|ATC ENT|CS DoC MCP|CS TS
AUC ENE|TS MCP|CS TS ENE|CS DoC
Estimating
Metric
Segmentation-3D
Choice 1 Choice 2 Choice 3
F1-Score DOC|CS TS ENT|CS TS ENE|CS TS-ATC
Sensitivity ENE|CS DoC MCP|CS TS ENE|CS TS-ATC
Precision MCP|CS TS MCP|CS DoC DOC|TS
Accuracy MCP|TS MCP|CS TS DOC|CS DoC
AUC MCP|CS TS MCP|TS MCP|CS DoC
Table E.19: The confidence scores chosen for creating MOVAL Ensemble.
77

Category Operation ID Operation Name Description Range of magnitudes
Spatial
transformations
1,2,3,4,5 Scaling down Scale down the image by factor 1 +M [0.05, 0.15, 0.25, 0.35, 0.45]
6,7,8,9,10 Scaling up Scale up the image by factor 1 +M [0.05, 0.15, 0.25, 0.35, 0.45]
11,12,13,14,15 RotateFrontal ACW Rotate the image along frontal axis anticlockwise [5°, 15°, 25°, 90°, 180°]
16,17,18,19 RotateFrontal CCW Rotate the image along frontal axis clockwise [5°, 15°, 25°, 90°]
20,21,22,23,24 RotateSagittal ACW Rotate the image along sagittal axis anticlockwise [5°, 15°, 25°, 90°, 180°]
25,26,27,28 RotateSagittal CCW Rotate the image along sagittal axis clockwise [5°, 15°, 25°, 90°]
29,30,31,32,33 RotateLongitudinal ACW Rotate the image along longitudinal axis anticlockwise [5°, 15°, 25°, 90°, 180°]
34,35,36,37 RotateLongitudinal CCW Rotate the image along longitudinal axis clockwise [5°, 15°, 25°, 90°]
38,39,40,41 Mirroring Flip the sample in different planes [Sagittal, Frontal, Axial, All]
Intensity
transformations
42,43,44 Gamma expansion Scalexto [0,1], thenO(x) =x 1+γ, and scale it back [0.1, 0.3, 0.5]
45,46,47 Gamma compression Scalexto [0,1], thenO(x) =x 1/(1+γ), and scale it back [0.1, 0.3, 0.5]
48,49,50 Inverted gamma expansion Do the gamma compression with the inverted image [0.1, 0.3, 0.5]
51,52,53 Inverted gamma compression Do the gamma expansion with the inverted image [0.1, 0.3, 0.5]
54,55,56 Adding intensityO(x) =x+ shift [0.05, 0.15, 0.25]
57,58,59 Subtracting intensityO(x) =x- shift [0.05, 0.15, 0.25]
60,61,62 Scaling up intensity histogram O(x) =x* (1 + scale) [0.05, 0.15, 0.25]
63,64,65 Scaling down intensity histogram O(x) =x/ (1 + scale) [0.05, 0.15, 0.25]
66,67,68 Increasing contrast Reduce the image mean, thenO(x) =x* (1 + scale), and add the mean value back [0.05, 0.15, 0.25]
69,70,71 Decreasing contrast Reduce the image mean, thenO(x) =x/ (1 + scale), and add the mean value back [0.05, 0.15, 0.25]
Noise
transformations
72,73,74 Blurring Blur the image using Gaussian filter with different standard deviations [0.5, 0.7, 0.9]
75,76,77 Sharpening
Sharpen the image using Laplacian of
Gaussian filter with different standard
deviations
[0.9, 0.7, 0.5]
78,79,80 Adding Gaussian noise Add Gaussian noise with different standard deviations [0.025, 0.075, 0.125]
81,82,83 Simulating low resolution Scale down the image, and scale it back [0.9, 0.7, 0.5]
Table E.20: List of all transformations that we use to generate synthetic domain shifts
for segmentation. There are 24 types of operations with a total of 83 choices. For 2D
segmentation, we exclude spatial transformations in the frontal and sagittal axes. For 3D
segmentation with advanced training strategies, we exclude all spatial transformations as
some algorithms impose strong spatial priors.
78
