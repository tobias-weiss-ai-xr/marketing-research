---
title: 'FLAM: Evaluating Model Performance with Aggregatable Measures in Federated Learning'
url: https://arxiv.org/abs/2605.07962
category: ai-marketing
subcategory: measurement
date: 2026-05
venue: ''
authors:
- Fabian Stricker
- Jose A. Peregrina
- David Bermbach
- Christian Zirpins
source: arxiv
pdf_url: https://arxiv.org/pdf/2605.07962
pages: 10
chars: 46879
fetched_at: '2026-11-08T13:28:10+00:00'
kb_version: 1
---

# FLAM: Evaluating Model Performance with Aggregatable Measures in Federated Learning

FLAM: Evaluating Model Performance with
Aggregatable Measures in Federated Learning
Fabian Stricker
Institute of Data-Centric
Software Systems (IDSS),
Hochschule Karlsruhe,
Karlsruhe, Germany
fabian.stricker@h-ka.de
Jose A. Peregrina
Institute of Data-Centric
Software Systems (IDSS),
Hochschule Karlsruhe,
Karlsruhe, Germany
joseantonio.peregrinaperez@h-ka.de
David Bermbach
Scalable Software Systems
Research Group
TU Berlin
Berlin, Germany
db@3s.tu-berlin.de
Christian Zirpins
Institute of Data-Centric
Software Systems (IDSS),
Hochschule Karlsruhe,
Karlsruhe, Germany
christian.zirpins@h-ka.de
Abstract—Performance evaluation is essential for assessing the
quality of machine learning (ML) models and guiding deployment
decisions. In federated learning (FL), assessing the performance
is challenging because data are distributed across participants.
Consequently, the coordinator must rely on locally computed
evaluation metrics and aggregate them to assess the global model.
A key challenge is that common aggregation strategies, such as
weighted averaging based on the local samples per participant,
do not always produce the same results as centralized evaluation.
Existing definitions of performance evaluation are largely tailored
to accuracy and do not generalize to other metrics, leading
to inconsistencies between participant-based and centralized
evaluation. However, such discrepancies are inconsistent with the
FL objective and lead to a wrong calculation of the metric.
To address this issue, we examine the underlying reasons
for these discrepancies and propose FLAM, a performance
evaluation method based on aggregatable measures that yields
the same results as centralized evaluation without the need for
a global test dataset.
Index Terms—Federated Learning, Model Performance, Fed-
erated Evaluation, Data Heterogeneity
I. INTRODUCTION
Federated learning (FL) is an emerging paradigm for en-
abling the training of a machine learning (ML) model in a
federated way across multiple participants. Each participant
trains a ML model locally on their own private dataset and
sends the resulting model to a coordinator. The coordinator
then aggregates the models into a global model, which aims to
contain all the knowledge of all participants in order to create a
model that generalizes well [1], [2]. In many applications, such
as healthcare and the energy sector, the data are not publicly
available because they contain sensitive information about
patients or customers, which cannot be collected centrally due
to privacy regulations (e.g., GDPR 1). Using FL, the data can
stay at each participant’s site because the local model acts as
a substitute, which improves both communication efficiency
This work was co-funded by the Federal Ministry of Research, Technology
and Space (BMFTR) under Grant 13FH587KX1 (FederatedForecasts)
© 2026 IEEE. Personal use of this material is permitted. Permission from
IEEE must be obtained for all other uses, in any current or future media,
including reprinting/republishing this material for advertising or promotional
purposes, creating new collective works, for resale or redistribution to servers
or lists, or reuse of any copyrighted component of this work in other works.
1https://gdpr.eu/
and privacy [1]. When institutions collaborate, it is important
to accurately assess the model’s performance in order to make
correct decisions about deployment, retraining, or changing the
model architecture. Especially in FL, where participants need
to coordinate, a wrong decision can lead to increased costs for
all parties. Since the coordinator does not have data, it needs
to leverage the participant’s data to assess the performance of
the model.
Today, there is no standardized approach on how to perform
the evaluation across different kinds of metrics and how to
interpret the evaluation results despite the existence of a
benchmarking framework [3]. Furthermore, for the participant-
based evaluation, it is necessary to define how to aggregate the
evaluation results. Here, different weights can yield different
results, which makes a comparison not meaningful. In studies,
weights based on the number of samples per participant [4] or
uniform weights are used [5], [6]. In some cases, the metrics
are calculated on a coordinator-side dataset [7], [8] without
the need for an aggregation.
Besides the selection of weights, we observed a significant
difference between participant-based evaluation and sending
local datasets to the coordinator for centralized evaluation.
This issue particularly affects the aggregation of performance
metrics that follow the implementation of frameworks [3], [9]
or definitions of evaluations [10], [11] that use the number
of samples as weights. However, this issue should not occur
because the evaluation follows the FL objective [1] where each
sample has the same importance [11], which is also the case
for centralized evaluation. Furthermore, with an increasing
non-independent and identically distributed (IID) skew, the
differences get more severe. Resolving these differences is
important because they lead to a wrong assessment of the
performance. Furthermore, a solution needs to be generic in
order to be usable in combination with many performance
metrics.
In order to address this problem, we analyze the discrepancy
by running experiments with a set of commonly used metrics
for classification and regression tasks while considering few
participants. In addition, we discuss the evaluation in FL in or-
der to clarify comparison issues and identify important aspects
that need to be considered when evaluating the performance
arXiv:2605.07962v1  [cs.LG]  8 May 2026

of a model. To resolve the discrepancy, we propose FLAM, a
method to evaluate models in FL with aggregatable measures
that leverages the data of participants while achieving the
same results as a centralized evaluation. The method eases
the comparison with centralized approaches and supports
mechanisms that usually require a centralized test dataset to
calculate the performance. In summary, we make the following
contributions:
1) We discuss performance evaluation in FL and the aspects
that need to be considered (Section III).
2) We analyze whether commonly used metrics in regres-
sion and classification tasks can be aggregated using
weighted averaging to produce the same results as cen-
tralized evaluation. Furthermore, we analyze the aspects
that influence the differences (Section IV).
3) We propose an evaluation method based on aggregatable
measures that leverages the participants to achieve the
same result as centralized evaluation (Section V).
4) We discuss privacy and applicability aspects of the eval-
uation method for real-world FL systems (Section V).
II. RELATEDWORK
In this section, we discuss the related work on performance
evaluation in FL. Throughout this paper, we use the term
evaluation to denote performance evaluation.
In FL, there are a few evaluation frameworks that do not
solely focus on evaluating the performance of the model but
rather on the FL system with a variety of properties such
as communication costs, data heterogeneity, and convergence
time [3], [10], [12]–[14]. In this regard, the frameworks only
consider different types of the accuracy metric, which is often
insufficient because it does not consider the data distribution.
Consequently, additional metrics should be considered to pro-
vide more insights into the quality of the model.
Chai et al. [11] provide a definition for the evaluation of
variety of FL system properties including the model per-
formance, which they refer to as utility. They mention that
the model trained with FL should ideally achieve the same
performance as a centralized trained one. Furthermore, they
provide a definition for participant-based evaluation with focus
on the accuracy metric. Although this paper provides insights
into the evaluation, they are only addressing the accuracy
metric without considering alternatives. Furthermore, a de-
tailed discussion about which aspects have to be considered is
missing.
Besides the definition of the evaluation, some studies men-
tion how to select the weights for the aggregation. Here,
commonly mentioned weights are either distributed uniformly
in order to provide more fairness or weighted by the number
of samples to prevent a participant with few samples from
having a high influence on the final score [3], [11].
Flach [15] discusses good and bad practices for evaluation
in ML to provide an important foundation for a measurement
theory. In detail, he shows how to aggregate performance
metrics for binary classification based on the confusion ma-
trix considering cross-validation. Furthermore, he mentions
that the F1-score should not be aggregated using arithmetic
averages because it can lead to incoherent results. This is
interesting because we can identify more severe issues in
FL. In contrast, FL is subject to heterogeneous data, where
participants can have a vastly different label distribution and
quantity. Besides data, privacy is an important aspect that
needs to be considered when designing an approach.
Our paper differs from the related work because we focus on
the evaluation of FL trained models to achieve the same result
as centralized evaluation. Furthermore, we focus on aspects
unique to FL, while discussing the goal of the evaluation.
In addition, we do not solely focus on classification tasks
but aim for a generalizable approach. To the best of our
knowledge, there is no paper that addresses the identical issue
for heterogeneous FL settings.
III. PERFORMANCEEVALUATION INFEDERATED
LEARNING
In this section, we provide an overview of evaluation in
FL and clarify which aspects need to be considered when
evaluating the model performance.
In prominent frameworks such as Flower and NVIDIA
Flare [9], [16] multiple evaluation methods are mentioned,
from coordinator-side evaluation with a test set on the coordi-
nator and participant-based evaluation to cross-site evaluation,
where all global and local models are evaluated on all partic-
ipants. Here, we only consider the centralized evaluation and
the participant-based evaluation because they do not reveal
the participant model to other participants. Furthermore, we
consider supervised ML tasks and the evaluation of the global
model. We first define the coordinator-side evaluation based
on the Flower implementation [9] which can be denoted as
Eq. 1 that partially aligns with the definition of centralized
effectiveness of Chai et al. [11] excluding the centralized
training:
U tility(P redict(wg, Dx), Dy)(1)
In the equation,U tility()denotes a function that calculates
a performance metric and the functionP redict()depicts the
prediction made by the global modelw g based on all samples,
whereD x are the features andD y the assigned labels per
sample.
Next, we look at the definition of participant-based eval-
uation. For the definition, we follow the Flower [9] imple-
mentation and the definition of Chai et al. [11]. Although
the implementation is generic for any metric, the definition
describes only the accuracy metric. We combine both aspects
and get the following definition:
PX
i=1
λi ∗U tility(P redict(wg, Dix ), Diy )(2)
This definition describes that the evaluation result is calculated
following the weighted average of a utility function for a set
of participants, wherePrefers to the number of participants.
Here,λ i refers to the weight assigned to the participanti,

which can be, for instance, computed based on the proportion
of data samples for a participant|D i|relative to the samples
of the global dataset|D all|, which is the concatenation of
all participant datasets. If we select these weights, then the
definition aligns with the FL objective [1]. Furthermore,D ix
denotes the features for the samples of the participanti. The
resulting definition faces two issues. First, it is not defined how
the weights should be selected, as some studies use the number
of samples as weights [4] and others use uniform weights [5],
[6]. Second, different weights can lead to divergent interpre-
tations, which, in turn, can result in incoherent metrics if it is
not described how they were calculated. To this end, we want
to discuss which aspects are important for evaluation as well
as how to handle different computations of metrics.
Which aspects are important for evaluation?In order to
discuss this question, we start with evaluation in centralized
ML. The evaluation metrics are selected based on the prop-
erties of the available dataset (e.g., class imbalance) as well
as the learning task (e.g., regression, classification) and the
loss function, which can be modified to match the learning
task (e.g., the cost of different predictions or regularization).
In comparison, FL introduces various new properties and
changes in the learning goal that lead to new aspects that
have to be considered during evaluation. First, the selection
of the weights for the aggregation of the participant metrics is
important because the weights modify the resulting metric.
Chai et al. [11] recommend using the number of samples
per participant as weight because they follow the loss of the
optimization goal defined by McMahan et al. [1] which defines
that each sample gets assigned the same importance. However,
in research there are aggregation methods that modify the FL
objective [17], [18]. Therefore, the weight selection depends
on the objective. If they do not align with the objective, it
could lead to a model that achieved the optimal minimum,
but the metric does not represent it. Consequently, one could
make wrong assumptions about the quality of the model.
Second, when selecting metrics for evaluating the perfor-
mance, it is unknown whether the dataset has class imbalance
because the data are private and distributed across the partici-
pants. In this case, plain accuracy can be misleading because
the model can optimize on a class that occurs often. Hence,
it would be better to use multiple metrics or metrics that can
handle both cases to prevent a wrong assessment.
Third, in FL the data can change at any time due to new data
collected by the participants or changes in the federation. For
example, participants can join, leave, or encounter failures,
which leads to a permanent or temporary change in data
distribution that can lead to a different quality assessment [19].
Hence, considering the generalization over the quality for a
fixed dataset can be more important.
Fourth, the model is not created for a single entity but
rather for a federation of participants. For example, if a
low number of market competitors collaborate, the evaluation
needs to consider fairness so that all participants benefit from
participation; otherwise, they may not participate at all [20].
Last, in FL we do not have one resulting model but rather
multiple models, such as the local models, the global model, or
multiple personalized versions of the global model [17]. Here,
it is important to define what should be evaluated and which
goals the evaluation should follow. It would be reasonable
to evaluate the final model that is used as a service and the
global model, which can be considered an intermediate result.
Consequently, the calculation and selection of the metrics need
to align with the goal of the FL task and need to consider
unique FL aspects.
How can we differentiate and compare interpretations?
If we consider the important aspects for evaluation, then the
calculation of metrics is complex, and denoting the name of
the metric is insufficient, because the aggregation changes
the measurement, which can lead to wrong conclusions and
comparisons. Consequently, it is necessary that studies men-
tion how the metrics are aggregated and what they measure.
Although a comparison between different measurements is
not meaningful, they could be used as extensions to provide
supporting insights about the quality of the model. For exam-
ple, assigning uniform weights to each participant can yield
more information about the fairness of the process [18]. If
we want to compare the participant-based evaluation with the
centralized ML evaluation, then it is necessary to understand
how the weights should be selected. In centralized evaluation,
every sample counts equally, which is also the case for the
FL optimization objective [1]. Consequently, a comparison
of these two metrics should lead to a meaningful evaluation
because they refer to the same measurement. Contrary to the
expectations, some metrics lead to different results between
centralized evaluation and aggregating them based on the
weighted average. This can lead to wrong conclusions when
comparing centralized training against federated training and
evaluation.
IV. AGGREGATIONDEVIATIONS OFMETRICS
In this section, we show that computing the metric using the
number of samples per participant as weights in a weighted
averaging aggregation can yield different results compared
to coordinator-side evaluation. Furthermore, we identify for
which metrics the deviations occur and what factors lead to
large deviations. We first define the experiment setup and then
analyze the experiments.
A. Experiment Setup
To demonstrate the severity of the effect and underscore
the relevance in federated settings, we conducted experiments
across multiple datasets and learning tasks. In Table I, we sum-
marize the configuration of the experiments. For the datasets,
we selected the CIFAR-10 [21] and CIFAR-100 [21] for image
classification because they are balanced and feature different
complexities with a high number of classes. In the case of the
tabular datasets, we select the Covertype [22] dataset because
it contains many features and class imbalance. Last, the
time-series datasets PVOD [23] and GermanSolarFarm [24]
are selected because they feature a different learning task

TABLE I: Experiment Configurations
Property Value
Datasets (Classification) Covertype, CIFAR-10, CIFAR-100
Metrics (Classification) Accuracy, Precision, Recall, F1-score, MCC
Datasets (Regression) PVOD, GermanSolarFarm
Metrics (Regression) R2-score
Aggregation Algorithm FedAvg [1]
Number of participants 4
Local Training Rounds 5
Communication Rounds 20
Optimizer Adam
TABLE II: Alpha Parameters used for Data Partitioning
Property Value
QS Alpha Values 2.0
LS Alpha Values 0.6, 7.0
LQS Alpha Values (QS, LS) (10.0, 1.0), (3.0, 0.7)
and contain heterogeneity through the different photovoltaic
stations.
For the partitioning of the classification datasets, we use the
Dirichlet distribution to generate different data distributions, as
it is commonly used in FL [25], [26]. In order to artificially
create quantity skews (QS), label skews (LS) or a combination
of quantity and label skews (LQS), we use the alpha values in
Table II. In addition to the Dirichlet-based skews, we create
a manual skew (MS). Here, participants share few classes but
also are the sole owner of a specific class, which simulates
a scenario where organizations have partially overlapping dis-
tributions but also maintain unique edge cases. In the case of
the time-series dataset, we select two forecasting datasets that
consist of multiple stations. For the PVOD dataset, we choose
4 stations that differ in the number of observations. In the case
of the GermanSolarFarm, we group the stations together and
assign each participant one group to simulate energy providers
with different stations located across Germany.
Next, we explain the model types used for each dataset.
For both CIFAR-10 and CIFAR-100, we use convolutional
neural networks (CNNs) in combination with dense layers
for the output to achieve reasonable performance with ac-
ceptable computational overhead. In case of the Covertype
dataset, we use a TabTransformer [27] because they achieve
good performance in few training rounds. For the time series
datasets, we use a one-dimensional CNN in combination with
gated recurrent units (GRU) for the PVOD dataset, as these
provide high quality with low computational resources. For the
GermanSolarFarm dataset, we use a long short-term memory
(LSTM) model. For all implementations, we use Tensorflow 2
and calculate the metrics using Scikit-learn 3.
Based on these configurations, we run experiments for each
dataset that results from the partitioning. Here, the goal is
to identify if there are classification or regression metrics
that show deviations between the coordinator-based evaluation
on the concatenated participant datasets and participant-based
evaluation. As metrics, we selected commonly used metrics
2https://www.tensorflow.org/
3https://scikit-learn.org/stable/
0 5 10 15 200
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
Agg R2
Srv R2
Rounds
Metrics
Fig. 1: PVOD: Comparison of aggregated metrics against
coordinator-side calculated metrics.
in multiclass classification, such as accuracy and the macro
and weighted versions of precision, recall, and F1-score.
Furthermore, we added the Matthews Correlation Coefficient
(MCC) [28] as a balanced measure even if the datasets have
class imbalance [29]. For the regression tasks, we selected the
R2-score, which measures the proportion of the variance of a
target that can be explained by the model.
B. Findings
Following the experiment setup, we conduct multiple ex-
periments and summarize the following observations:
Finding 1: The aggregation of metrics such as the R2-score,
Macro F1-score, Macro Precision, Macro Recall, Weighted
F1-score, MCC and Weighted Precision showed differences
compared to a centralized calculation –In Fig. 1, the R2-
score shows a difference of up to 0.26 between aggregating the
participant metrics and calculating the results on a coordinator-
side dataset. For the CIFAR-10 dataset in Fig. 2, we can also
observe differences across the metrics. Here, the weighted
precision shows the highest differences, with up to 0.39.
In comparison, the weighted recall and accuracy show no
differences and have the same results as centralized evaluation.
In addition, we can observe differences for the Covertype
dataset across the different metrics in Fig. 3a and 3b. Although
in Fig. 3c the MCC indicates larger differences than for the
CIFAR10 dataset. Here, the accuracy and weighted recall
both show no differences and are similar to coordinator-
side evaluation. The highest absolute difference was for the
weighted precision, with up to 0.19. Based on the experiments,
we showed that there can be differences between aggregating
the metrics and calculating them based on a coordinator-side
dataset. Upon analyzing the different skews of the experi-
ments, we could observe that the differences are higher the
larger the deviation between the participants’ metrics are.
Finding 2: The aggregation of metrics such as the accuracy
and the weighted recall showed no deviations –In the pre-
vious finding, we could observe differences for most metrics
except accuracy and weighted recall. Rather than showing
a difference between the evaluations, we want to show that
there is no difference. We assume that the coordinator-side
dataset is a concatenation of the participant datasets and use

0 5 10 15 200
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
Agg macro precision
Srv macro precision
Agg macro recall
Srv macro recall
Agg macro f1
Srv macro f1
Rounds
Metrics
(a) Macro Metrics
0 5 10 15 200
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
Agg weighted precision
Srv weighted precision
Agg weighted recall
Srv weighted recall
Agg weighted f1
Srv weighted f1
Rounds
Metrics
(b) Weighted Metrics
0 5 10 15 200
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
Agg mcc
Srv mcc
Agg accuracy
Srv accuracy
Rounds
Metrics
(c) MCC and Accuracy
Fig. 2: CIFAR-10 MS: Comparison of aggregated metrics
against coordinator-side calculated metrics.
Eq. 2, where the weights for a participant are the number
of samples. We start by analyzing the accuracy metric for
multiclass classification and set the centralized calculation
equal to the aggregation. In the Eq. 3, the variableCdenotes
the number of classes andT Pij refers to the true positives for
the classjacross the dataset for participanti.
PC
j=1 T Pallj
|Dall| =
PX
i=1
|Di|
|Dall| ∗
PC
j=1 T Pij
|Di|
= 1 |Dall|
PX
i=1
CX
j=1
T Pij
=
PC
j=1 T Pallj
|Dall| (3)
0 5 10 15 200
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
Agg macro precision
Srv macro precision
Agg macro recall
Srv macro recall
Agg macro f1
Srv macro f1
Rounds
Metrics
(a) Macro Metrics
0 5 10 15 200
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
Agg weighted precision
Srv weighted precision
Agg weighted recall
Srv weighted recall
Agg weighted f1
Srv weighted f1
Rounds
Metrics
(b) Weighted Metrics
0 5 10 15 200
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
Agg mcc
Srv mcc
Agg accuracy
Srv accuracy
Rounds
Metrics
(c) MCC and Accuracy
Fig. 3: Covertype LS withα= 0.6: Comparison of aggregated
metrics against coordinator-side calculated metrics.
Furthermore, through simplification, we show that the cen-
tralized calculation of accuracy is equal to the aggregation.
Following the same approach, we can show the same behavior
for the weighted recall in Eq. 4. Here, we use the formula
from Scikit-learn [30] that uses the number of samples for a
class as weights. The left-hand side represents the centralized
evaluation and is already simplified for clarity. We show
equivalency by simplifying the right-hand side which describes

the weighted recall with aggregation.
PC
j=1 T Pallj
|Dall| =
PX
i=1
|Di|
|Dall|
1
|Di|
PC
j=1
T Pij +F Nij
1
T Pij
T Pij +F Nij
= 1 |Dall|
PX
i=1
CX
j=1
T Pij
=
PC
j=1 T Pallj
|Dall| (4)
Upon simplification, we observe that in the context of multi-
class classification, the weighted recall with samples per class
as weights leads to the same measurement as the accuracy.
The selection of the weights is crucial because they modify
the equation to measure the number of all TPs against all
samples, which is equivalent to accuracy.
Following both equations, we demonstrated that it is possi-
ble to achieve the same results as coordinator-side evaluation
in a distributed way, leveraging the participants. As a conse-
quence, the predictions are not the cause of the difference;
otherwise, all metrics have to be affected. However, we
showed that only a subset of metrics are affected. Leading
to the conclusion that there is no difference between making
predictions with a fixed global model in a centralized location
versus making the predictions with the same model in a
distributed manner. Hence, there is no dependency between
input samples. This conclusion is only true if we consider our
assumptions; hence, the global model on each participant is
fixed and deterministic. Therefore, the prediction for the same
sample will yield the same result because the prediction does
not modify the model weights. Consequently, the distributed
evaluation process can be interpreted as parallelization of the
evaluation. To resolve the problem of the different values, a
solution needs to modify the calculation of the metrics, which
we propose in the next section.
V. ACHIEVINGCENTRALIZEDEVALUATION WITH
DISTRIBUTED DATASETS
In this section, we propose FLAM, a method that calculates
performance metrics based on aggregatable measures (AM).
We first define the requirements that the AMs must satisfy.
Next, we demonstrate, given a set of AMs, the calculation is
valid. We then derive the AMs for the R2-score and the F1-
scores and show their correctness. Furthermore, we discuss the
applicability and privacy of the proposed method.
A. FLAM: Metric Calculation based on Aggregatable Mea-
sures
Rather than calculating the metrics on the participants side
and aggregating them on the coordinator’s, we move the
calculation of the metrics towards the coordinator. Thus, we
can avoid the aggregation of the performance metrics. Instead,
we identify AMs of the metric calculation and send them to
the server to calculate the performance metric. In this context,
AMs are decomposed components of a specific metric, which
can be recombined to achieve the same calculation process.
Hence, they do not modify the calculation of the metric. We
define an AM as a measure that can be calculated on different
local datasets and achieves the same results as if they were
calculated centrally. Consequently, an AM needs to satisfy
Eq. 5.
AMall =
PX
i=1
AMi (5)
Here, we assume that the global dataset is a concatenation of
the test datasets used for evaluation. Some metrics, such as the
R2-score require statistical information such as the mean over
the labels. To fulfill the requirement, the statistical information
needs to be calculated across the participant datasets and then
aggregated into a global statistical metric. Otherwise, this
would lead to dependencies on the local datasets. If the metric
calculation can be decomposed into a set of AMs, we can
evaluate the performance of a model with the following steps:
1) The participants calculate the measures on their local
dataset.
2) The local AMs are sent to the coordinator.
3) The coordinator aggregates the measures.
4) The coordinator uses the aggregated measures to calcu-
late the metric.
Our method modifies the participant-based evaluation (see
Eq. 2) by moving the aggregation of the participant results
into the calculation of the metric and removing the weights,
because the AMs are calculated based on the samples for
a participant. This results in Eq. 6. In the equation, the
functioncalc AM si()denotes the calculation of the AMs
for a participantibased on the predicted value and the
ground truth over the participant datasetD i. For readability,
we shorten the function to the calculated AMs for a participant,
assuming that a valid set of AMs is found.
U tility(
PX
i=1
calc AM si(P redict(wg, Dix ), Diy ))
=U tility(
PX
i=1
AMi)
(6)
Now that we have defined the method, we can prove that
our method achieves the same performance as centralized
evaluation by showing that it is equal to centralized evaluation
(see Eq. 1). In Eq. 7, we simplify both methods to show
that they refer to the same calculation. To achieve the equiva-
lency, we perform two steps. First, we rewrite the centralized
evaluation to calculate the AMs centrally, which is possible
because the AMs are decomposed measures that do not modify
the calculation. Hence, AMs are intermediate results of the
original metric calculation. Second, the AMs need to satisfy
Eq. 5. Therefore, we can rewrite the sum of the values as the

result over the full dataset.
U tility(P redict(wg, Dallx ), Dy) =U tility(
PX
i=1
AMi)
U tility(AMall) =U tility(
PX
i=1
AMi)
=U tility(AMall)
(7)
Thus, we can use the method if we decompose a specific
metric into measures that are aggregatable. We showed that
some metrics lead to wrong results; therefore, we analyze
these metrics and decompose them in AMs. Since each metric
is calculated differently, it is not feasible to show the AMs
for all identified metrics. Therefore, we exemplarily show the
method for the R2-score and the F1-scores because they are
widely used. We make the implementations and selection of
AMs for all identified metrics including the MCC, weighted
precision, macro recall, and macro precision publicly available
as a GitHub repository 4.
Although deriving a general method that identifies a set
of AMs is challenging, we propose a structured approach to
identify AMs. First, we analyze the formal definition of the
metric and identify dependencies on dataset-specific statistics.
For example, quantities such as the mean of a local data
partition or other participant-specific scaling factors that can
influence the computation. Second, once a set of AMs has been
identified, we validate the correctness by analyzing whether
the requirement (see Eq. 5) is satisfied.
We start with finding AMs for the R2-score. Here, we first
analyze the R2-score [31]:
R2 = 1−
PDall
k=1 (y truek −y predk)2 PDall
k=1 (y truek −mean(y trueDall ))2
(8)
Based on the equation, we can derive the AMs in Eq. 9 and
the calculation of the metric on the coordinator, including the
placeholders for the AMs in Eq. 10. In both equations,y true
refers to the ground truth andy predto the predicted value
for a sample.
rs Ai =
DiX
k=1
(y truek −y predk)2,
rs Bi =
DiX
k=1
(y truek −mean(y trueDall ))2
(9)
R2 = 1−
PP
i=1 rs Ai PP
i=1 rs Bi
(10)
Furthermore, in order to make the calculation identical across
all participants, it is necessary to calculate the mean of the
concatenated global datasetD all. Otherwise, this would lead
to different results per participant. To validate the AMs, we
start withrs Ai in Eq. 11 and verify that the requirement
is satisfied. We can rewrite the double summations as a
4https://github.com/HKA-IDSS/Supplement-FLAM-Evaluation
single one over all samples in the global dataset. This is
possible because we assume the same deterministic global
model across the participants, and the coordinator dataset is
the concatenation of the participant datasets. Therefore, we
have the same prediction per participant for a given sample.
Furthermore, there are no scaling factors connected to the local
data part; hence, the requirement is satisfied.
DallX
k=1
(y truek −y predk)2 =
PX
i=1
DiX
k=1
(y truek −y predk)2
=
DallX
k=1
(y truek −y predk)2
(11)
We can show the same for the second AM because they have
a similar structure. Here, the difference is the mean, which
needs to be calculated on the full datasets to prevent local
dependencies.
Next, we analyze the equation for macro F1-score [32]:
F1 M acro= 1 C
CX
j=1
2∗T Pj
2∗T Pj +F Pj +F Nj
(12)
We can identify the two AMs in 13, which are the TP for each
class as well as the sum of the FP and FN per class.
f1 Aji =F Pij +F Nij ,
f1 Bji =T Pij
(13)
Following the AMs, we can rewrite the macro F1 and sum up
the AMs across the participants to get Eq. 14.
f1 m= 1 C
CX
j=1
2∗ PP i=1 f1 Bji
2∗ PP i=1 f1 Bji + PP i=1 f1 Aji (14)
Next, we repeat the same steps for the weighted F1 [32]. Here,
the equation is modified by using weights based on the number
of samples per class instead of uniform weights. In order to get
the weights per class, it is necessary to define another AM that
describes the number of samples for a specific class denoted
in Eq. 15.
wji =T Pij +F Nij (15)
Based on this measure, we can modify the weighted F1 to
achieve Eq. 16.
f1 w= 1 Dall
CX
j=1
(
PX
i=1
wji ) 2∗ PP i=1 f1 Bji
2∗ PP i=1 f1 Bji + PP i=1 f1 Aji
(16)
To validate that the AMs for the different F1-scores are correct,
we analyze if the requirement is fulfilled. Since all AMs
consist of absolute counts and sums, there is no statistical
information or other scaling factor that depends on the local
dataset. Consequently, we can perform the same simplification
as for the first AM of the R2-score and follow the same
reasoning.

0 5 10 15 200
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
Agg R2
FLAM R2
Srv R2
Rounds
Metrics
Fig. 4: PVOD: Comparison of FLAM, coordinator-side calcu-
lated metrics, and the aggregated metrics.
0 5 10 15 200
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
FLAM macro precision
Srv macro precision
FLAM macro recall
Srv macro recall
FLAM macro f1
Srv macro f1
Rounds
Metrics
(a) Macro Metrics
0 5 10 15 200
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
FLAM weighted precision
Srv weighted precision
FLAM weighted f1
Srv weighted f1
FLAM mcc
Srv mcc
Rounds
Metrics
(b) Weighted Metrics and MCC
Fig. 5: CIFAR-10 MS: Comparison of FLAM against
coordinator-side calculated metrics.
B. Results
We further show the correctness of the AMs selection by
running experiments with the same setup as described in
Section IV and including the evaluation results of FLAM.
Here, we show the results for the experiments that had the
highest deviation for the different dataset types. We start with
the regression task in Fig. 4 that shows that the FLAM achieves
the same R2-score as coordinator-based evaluation. In case of
the CIFAR-10 dataset, Fig. 5a indicates the same overlapping
results for the macro metrics. The same applies to the weighted
metrics and the MCC in Fig. 5b. For the Covertype dataset
with labels skew and unbalanced classes, the experiments in
0 5 10 15 200
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
FLAM macro precision
Srv macro precision
FLAM macro recall
Srv macro recall
FLAM macro f1
Srv macro f1
Rounds
Metrics
(a) Macro Metrics
0 5 10 15 200
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
FLAM weighted precision
Srv weighted precision
FLAM weighted f1
Srv weighted f1
FLAM mcc
Srv mcc
Rounds
Metrics
(b) Weighted Metrics and MCC
Fig. 6: Covertype LS withα= 0.6: Comparison of FLAM
against coordinator-side calculated metrics.
Fig. 6a and Fig. 6b depict, for all metrics, that they achieved
the same results as the centralized evaluation. Following these
results, we showed that our method can achieve the same
results as centralized evaluation based on a coordinator-side
test dataset for commonly used metrics as long as a suitable set
of AMs is identified. Due to the large number of experiments,
showing all experiments would be excessive. We make the
experiment results for all metrics publicly available as a
GitHub repository.
C. Discussion
So far, we have shown that our method can achieve the
same quality as centralized evaluation for a set of metrics
without a centralized test dataset using the participant datasets.
Besides the correctness in FL, the applicability and privacy are
important aspects.
In FL there are various metrics and learning tasks that
we did not include in the evaluation, leading to the question
of whether the method can be used with other metrics. In
general, all metrics are composed of single terms that form
the calculation, and the lowest level of AMs in the case of
supervised learning would be true and predicted values. These
can be used as AMs because these values are counts. Thus, it
would also be possible for any metric in supervised learning
that builds upon these values.
Besides the use of different metrics, the method needs
to scale with more participants. In general, all participants

have the same number of measures that they need to cal-
culate, which depends on the metrics and how the equation
is decomposed into AMs. With more participants, only the
number of results sent to the coordinator increases, which is
more problematic for the aggregation of the model weights,
which can be a large matrix. Here, hierarchical aggregation
can be a solution. Since our method sums up the measures, a
hierarchical approach with intermediate aggregators could be
a possible solution as long as the metric is calculated on the
highest level of the hierarchy of aggregators. Following the
same approach, the computational overhead of summing up
the AM of each participant would be distributed alongside the
hierarchy of aggregators.
Another aspect is the heterogeneity of participants’ data
pipelines, which can lead to different data structures and
properties. Hence, influencing the training and evaluation. To
achieve a consistent structure, data harmonization is essential
for real-world deployment [20]. Accordingly, future work
should focus on privacy-preserving data harmonization.
Considering privacy, one of the goals of FL is to improve
the privacy of the participants and prevent the leakage of
sensitive information. In this regard, sending the true labels
and true predictions can lead to privacy issues in real-world
FL. Although they do not contain the features, in contrast
to sending the data to the coordinator, statistical information
about the participants’ data is revealed. Therefore, the goal
should be to find AMs that consist of multiple aspects in
order to reduce information about the data; however, this is
strongly dependent on the metric. While we do not propose
privacy solutions, there are methods such as secure multi-party
computation (SMPC) to calculate the global mean without
revealing individual information of the participants, hence,
improving the privacy [33], [34].
VI. CONCLUSION
Evaluating model performance metrics is a common step
in ML. However, in FL, computing the metrics following
strategies such as weighted averaging based on the samples
per participant can yield different results than centralized
evaluation. These differences can result in incorrect model
comparisons and misguided deployment decisions, posing a
high risk for the collaboration.
To address this issue, we analyzed the underlying causes
of these deviations and showed that the metric calculation
is leading to differences. We proposed FLAM, a general
evaluation method that decomposes the calculation into AMs.
These AMs are calculated by the participants and sent to
the coordinator to compute the metric. We showed that this
approach achieves the same results as centralized evaluation
without the need for a global test dataset. In addition, we
discussed key considerations for reliable model evaluation in
FL settings.
REFERENCES
[1] B. McMahan, E. Moore, D. Ramage, S. Hampson, and Blaise Aguera y
Arcas, “Communication-Efficient Learning of Deep Networks from De-
centralized Data,” inProceedings of the 20th International Conference
on Artificial Intelligence and Statistics. PMLR, 2017.
[2] A. Hard, K. Rao, R. Mathews, S. Ramaswamy, F. Beaufays, S. Augen-
stein, H. Eichner, C. Kiddon, and D. Ramage, “Federated Learning for
Mobile Keyboard Prediction,” 2019.
[3] S. Caldas, S. M. K. Duddu, P. Wu, T. Li, J. Kone ˇcn´y, H. B. McMahan,
V . Smith, and A. Talwalkar, “LEAF: A Benchmark for Federated
Settings,” 2019.
[4] F. Lai, X. Zhu, H. V . Madhyastha, and M. Chowdhury, “Oort: Ef-
ficient Federated Learning via Guided Participant Selection,” in15th
{USENIX}Symposium on Operating Systems Design and Implementa-
tion ({OSDI}21), 2021.
[5] H. Cho, A. Mathur, and F. Kawsar, “FLAME: Federated Learning Across
Multi-device Environments,”Proceedings of the ACM on Interactive,
Mobile, Wearable and Ubiquitous Technologies, 2022.
[6] Y . Yu, A. Wei, S. P. Karimireddy, Y . Ma, and M. Jordan, “TCT: Con-
vexifying federated learning using bootstrapped neural tangent kernels,”
inAdvances in Neural Information Processing Systems, S. Koyejo,
S. Mohamed, A. Agarwal, D. Belgrave, K. Cho, and A. Oh, Eds. Curran
Associates, Inc., 2022.
[7] D. Garg, D. Sanyal, M. Lee, A. Tumanov, and A. Gavrilovska, “Client
Availability in Federated Learning: It Matters!” inProc. of the 5th
Workshop on Machine Learning and Systems, ser. EuroMLSys ’25.
ACM, 2025.
[8] Y . Sun, Y . Mao, and J. Zhang, “MimiC: Combating Client Dropouts
in Federated Learning by Mimicking Central Updates,”IEEE Trans. on
Mobile Computing, 2024.
[9] D. J. Beutel, T. Topal, A. Mathur, X. Qiu, J. Fernandez-Marques, Y . Gao,
L. Sani, K. H. Li, T. Parcollet, P. P. B. de Gusm ˜ao, and N. D. Lane,
“Flower: A Friendly Federated Learning Research Framework,” 2022.
[10] D. Chai, L. Wang, L. Yang, J. Zhang, K. Chen, and Q. Yang, “FedEval:
A Holistic Evaluation Framework for Federated Learning,” 2022.
[11] ——, “A Survey for Federated Learning Evaluations: Goals and Mea-
sures,”IEEE Transactions on Knowledge and Data Engineering, 2024.
[12] S. Hu, Y . Li, X. Liu, Q. Li, Z. Wu, and B. He, “The OARF Bench-
mark Suite: Characterization and Implications for Federated Learning
Systems,”ACM Trans. Intell. Syst. Technol., 2022.
[13] A. Nilsson, S. Smith, G. Ulm, E. Gustavsson, and M. Jirstrand, “A
Performance Evaluation of Federated Learning Algorithms,” inProceed-
ings of the Second Workshop on Distributed Infrastructures for Deep
Learning, ser. DIDL ’18. ACM, 2018.
[14] L. Liu, F. Zhang, J. Xiao, and C. Wu, “Evaluation Framework For Large-
scale Federated Learning,” 2020.
[15] P. Flach, “Performance evaluation in machine learning: The good, the
bad, the ugly, and the way forward,” inProceedings of the AAAI
Conference on Artificial Intelligence, no. 01, 2019.
[16] H. R. Roth, Y . Cheng, Y . Wen, I. Yang, Z. Xu, Y .-T. Hsieh, K. Kersten,
A. Harouni, C. Zhao, K. Lu, Z. Zhang, W. Li, A. Myronenko, D. Yang,
S. Yang, N. Rieke, A. Quraini, C. Chen, D. Xu, N. Ma, P. Dogra,
M. Flores, and A. Feng, “NVIDIA FLARE: Federated Learning from
Simulation to Real-World,” 2022.
[17] T. Li, S. Hu, A. Beirami, and V . Smith, “Ditto: Fair and Robust
Federated Learning Through Personalization,” inProceedings of the 38th
International Conference on Machine Learning. PMLR, 2021.
[18] T. Li, M. Sanjabi, A. Beirami, and V . Smith, “Fair Resource Allocation
in Federated Learning,” 2020.
[19] F. Stricker, D. Bermbach, and C. Zirpins, “Analyzing the Impact of
Participant Failures in Cross-Silo Federated Learning,” 2025.
[20] K. Kuo, C. Yadav, and Virginia Smith, “Research in Collaborative
Learning Does Not Serve Cross-Silo Federated Learning in Practice,”
2025.
[21] A. Krizhevsky, “Learning Multiple Layers of Features from Tiny Im-
ages,” University of Toronto, Tech. Rep., 2009.
[22] J. Blackard, “Covertype,” 1998.
[23] T. Yao, J. Wang, H. Wu, P. Zhang, S. Li, Y . Wang, X. Chi, and M. Shi,
“PVOD v1.0 : A photovoltaic power output dataset,” 2021.
[24] A. Gensler, J. Henze, N. Raabe, and V . Pankraz, “GermanSolar-
Farm data set,” https://www.uni-kassel.de/eecs/en/sections/intelligent-
embedded-systems/downloads.html, 2016.
[25] J. Wang, Q. Liu, H. Liang, G. Joshi, and H. V . Poor, “Tackling the
Objective Inconsistency Problem in Heterogeneous Federated Optimiza-
tion,” inAdvances in Neural Information Processing Systems. Curran
Associates, Inc., 2020.

[26] T. Lin, L. Kong, S. U. Stich, and M. Jaggi, “Ensemble Distillation for
Robust Model Fusion in Federated Learning,” inAdvances in Neural
Information Processing Systems. Curran Associates, Inc., 2020.
[27] X. Huang, A. Khetan, M. Cvitkovic, and Z. Karnin, “TabTransformer:
Tabular Data Modeling Using Contextual Embeddings,” 2020.
[28] J. Gorodkin, “Comparing two K-category assignments by a K-category
correlation coefficient,”Computational Biology and Chemistry, 2004.
[29] G. Jurman, S. Riccadonna, and C. Furlanello, “A Comparison of MCC
and CEN Error Measures in Multi-Class Prediction,”PLOS ONE, 2012.
[30] “3.4. Metrics and scoring: Quantifying the quality of predictions,”
https://scikit-learn.org/stable/modules/model evaluation.html.
[31] M. H. Kutner and J. Neter,Applied Linear Regression Models,
ser. Irwin/McGraw-hill Series in Operations and Decision Sciences.
McGraw-Hill/Irwin, 2004.
[32] M. C. Hinojosa Lee, J. Braet, and J. Springael, “Performance Metrics
for Multilabel Emotion Classification: Comparing Micro, Macro, and
Weighted F1-Scores,”Applied Sciences, 2024.
[33] K. Bonawitz, V . Ivanov, B. Kreuter, A. Marcedone, H. B. McMahan,
S. Patel, D. Ramage, A. Segal, and K. Seth, “Practical secure aggregation
for privacy-preserving machine learning.” Association for Computing
Machinery, 2017.
[34] J. So, C. He, C.-S. Yang, S. Li, Q. Yu, R. E. Ali, B. Guler, and
S. Avestimehr, “LightSecAgg: A Lightweight and Versatile Design for
Secure Aggregation in Federated Learning,”Proceedings of Machine
Learning and Systems, 2022.
