---
title: The Estimation of Continual Causal Effect for Dataset Shifting Streams
url: https://arxiv.org/abs/2504.20471
category: ai-marketing
subcategory: empirical
date: 2025-04
venue: ''
authors:
- Baining Chen
- Yiming Zhang
- Yuqiao Han
- Ruyue Zhang
- Ruihuan Du
source: arxiv
pdf_url: https://arxiv.org/pdf/2504.20471
pages: 17
chars: 68839
fetched_at: '2026-11-08T13:14:05+00:00'
kb_version: 1
---

# The Estimation of Continual Causal Effect for Dataset Shifting Streams

THE ESTIMATION OF CONTINUAL CAUSAL EFFECT FOR DATASET
SHIFTING STREAMS ∗
A PREPRINT
Baining Chen
Didi Chuxing
chenbaining_i@didiglobal.com
Yiming Zhang
Didi Chuxing
eddiezhang@didiglobal.com
Yuqiao Han
Didi Chuxing
hanyuqiao@didiglobal.com
Ruyue Zhang
Didi Chuxing
zhangruyue@didiglobal.com
Ruihuan Du†
Didi Chuxing
duruihuan@gmail.com
Zhishuo Zhou
Didi Chuxing
zhouzhishuo@didiglobal.com
Zhengdan Zhu
Didi Chuxing
zhuzhengdan@didiglobal.com
Xun Liu
Didi Chuxing
wubusi@didiglobal.com
Jiecheng Guo
Didi Chuxing
jasonguo@didiglobal.com
April 30, 2025
ABSTRACT
Causal effect estimation has been widely used in marketing optimization. The framework of an uplift
model followed by a constrained optimization algorithm is popular in practice. To enhance perfor-
mance in the online environment, the framework needs to be improved to address the complexities
caused by temporal dataset shift. This paper focuses on capturing the dataset shift from user behavior
and domain distribution changing over time. We propose an Incremental Causal Effect with Proxy
Knowledge Distillation (ICE-PKD) framework to tackle this challenge. The ICE-PKD framework
includes two components: (i) a multi-treatment uplift network that eliminates confounding bias using
counterfactual regression; (ii) an incremental training strategy that adapts to the temporal dataset shift
by updating with the latest data and protects generalization via replay-based knowledge distillation.
We also revisit the uplift modeling metrics and introduce a novel metric for more precise online
evaluation in multiple treatment scenarios. Extensive experiments on both simulated and online
datasets show that the proposed framework achieves better performance. The ICE-PKD framework
has been deployed in the marketing system of Huaxiaozhu, a ride-hailing platform in China.
Keywords Causal Inference · Dataset Shift · Multiple Treatments · Uplift Modeling Evaluation · Incremental Learning
1 Introduction
Causal effect estimation is critical in marketing optimization [He et al., 2024, Sun et al., 2015, Liu et al., 2023] and is
applicable in various other domains, including healthcare [Smit et al., 2023, Sato et al., 2024] and finance transactions
[Kristjanpoller et al., 2025, Kumar et al., 2023]. Previous works have made considerable progress in causal effect
estimation using observational data, as randomized controlled trial (RCT) data is often costly and difficult to obtain.
To address the challenges posed by missing counterfactual outcomes and selection bias [Vemuri, 2015], several ap-
proaches have been proposed, including re-weighting [Austin, 2011, Bottou et al., 2013, Zubizarreta, 2015, Hassanpour
and Greiner, 2019a], balanced representation [Bengio et al., 2013, Shalit et al., 2017] and disentangled representation
[Hassanpour and Greiner, 2019a, Wu et al., 2022].
∗We thank Jianting Guo and Xuegang Kong for their support, collegiality and collaboration during the project.
†Corresponding author
arXiv:2504.20471v1  [cs.LG]  29 Apr 2025

The Estimation of Continual Causal Effect for Dataset Shifting Streams
The training framework must be updated when the distribution of online source data changes over time. However, above
approaches do not adequately address this issue. As a result, the model’s performance decreases very quickly over time
[Chu et al., 2023]. In online marketing, data sources are influenced by several factors, including news, holidays and
weather conditions. These temporal changes in data are referred to as dataset shift. In practice, two kinds of dataset
shift are commonly considered, which are covariate shift [Nair et al., 2019] and concept drift [Kull and Flach, 2014].
Covariate shift is the temporal changes of the covariates’ distribution.
Concept drift is the temporal changes in the relationship between the covariates and the responses (or outcomes) for
each treatment group.
Taking Huaxiaozhu (a popular ride-hailing platform in China) as an example: the temporal changes in user profile
distribution can be viewed as covariate shift, and the temporal changes in how user profiles influence the orders can be
interpreted as concept drift.
Continual Causal Effect Representation Learning method (CERL) is proposed [Chu et al., 2023] to address the problem
of continual lifelong causal effect estimation. The CERL focuses on covariate shift in binary treatment scenarios.
However, our business needs to face the challenges of both covariate shift and concept drift in multiple treatment
settings.
In this paper, we propose the Incremental Causal Effect with Proxy Knowledge Distillation (ICE-PKD), a framework
designed to handle multiple treatments and effectively address the complexities associated with concept drift. ICE-PKD
provides a more robust and adaptable approach for causal effect estimation in dynamic marketing settings. Specifically,
ICE-PKD extends the Disentangled Representations for CounterFactual Regression (DR-CFR) framework [Hassanpour
and Greiner, 2019b] into multiple treatments and draws inspiration from class-incremental methods in computer vision
[Van de Ven et al., 2022, Belouadah et al., 2021], such as functional regularization [Li and Hoiem, 2017] and relay-based
techniques [Rebuffi et al., 2017]. Additionally, we introduce a customized modification to the knowledge distillation
process by incorporating insights from the alternative method of PTLoss [Zhang et al., 2024], addressing concept drift
more effectively. As a result, ICE-PKD is able to learn the continual causal effect for dataset shifting streams. The
effectiveness of ICE-PKD has been validated via extensive experiments.
The main contributions of this paper are as follows: (1) an extended DR-CFR framework for handling multiple
treatments; (2) a novel training strategy for continual causal effect estimation, considering both covariate shift and
concept drift; (3) a new metric RAS-AUCC which evaluates the uplift model in multiple treatments.
2 Related Work
In this section, we present a brief overview of relevant works, including uplift modeling, evaluation metrics for uplift
modeling, incremental learning, knowledge distillation with auxiliary loss terms and continual causal effect estimation.
2.1 Uplift Modeling
Uplift modeling focuses on estimating the Individual Treatment Effect (ITE) and has undergone significant advancements
over time. Existing methods can be broadly classified into three main types: meta-learner-based methods, tree-based
methods and neural network-based methods.
Meta-learner-based methods. These methods use machine learning estimators as base learners to estimate treatment
effects by comparing predicted responses. The S-learner [Lo, 2002] trains a single model on the combined dataset of
treated and control samples, incorporating the treatment indicator as an additive input feature. In contrast, T-learner
[Künzel et al., 2019] constructs two distinct models: one for the treated group and one for the control group.
Tree-based methods. These methods leverage specialized tree or forest structures with treatment-effect-optimized
splitting criteria. Bayesian Additive Regression Trees (BART) [Chipman et al., 2010] merge the interpretability of
decision trees with a Bayesian framework, capturing complex relationships and uncertainty within the data. Causal
Forest [Wager and Athey, 2018] is specifically designed to estimate heterogeneous treatment effects by employing
random forests within a causal inference framework.
Neural network-based methods. These methods fully leverage the approximation capability and structural flexibility
of neural networks. Balancing Neural Network (BNN) [Johansson et al., 2016] minimizes the discrepancy between
the distribution of control and treatment samples using the Integral Probability Metric (IPM). Treatment-Agnostic
Representation Network (TarNet) and Counterfactual Regression (CFR) [Shalit et al., 2017] adopt a multi-task network
2

The Estimation of Continual Causal Effect for Dataset Shifting Streams
architecture, learning separate networks based on a shared balanced representation across the treated and control groups.
DragonNet [Shi et al., 2019] is designed to predict propensity scores and conditional outcomes through an end-to-
end procedure. Disentangled Representations for CounterFactual Regression (DR-CFR) [Hassanpour and Greiner,
2019b] employs representation learning to design a model architecture that explicitly identifies underlying factors
in observational datasets. Deep Entire Space Cross Networks for Individual Treatment Effect Estimation (DESCN)
[Zhong et al., 2022] addresses treatment bias and sample imbalance by jointly learning treatment and response functions
across the entire sample space and utilizing a cross network to model hidden treatment effects. Explicit Feature
Interaction-aware Uplift Network (EFIN) [Liu et al., 2023] enhances online marketing by explicitly modeling treatment
features and their interactions to accurately estimate individual treatment effects.
2.2 Evaluation Metrics for Uplift Modeling
A significant challenge in uplift modeling is the accurate evaluation of model performance, primarily due to the
unobservable nature of counterfactual outcomes in online datasets. The Precision in Estimating Heterogeneous Effects
(PEHE) [Hill, 2011] is commonly employed in semi-synthetic or simulated datasets. It quantifies the discrepancy
between ground truth and predicted treatment effects at the individual level. However, it necessitates knowledge of both
counterfactual and factual outcomes, making it unsuitable for direct evaluation on online data. The Average Treatment
Effect Error (ATE Error) measures the average difference in outcomes between treated and control groups. The Area
Under the Uplift Curve (AUUC) [Devriendt et al., 2020] assesses a model’s ability to rank individuals based on predicted
uplift. The QINI Coefficient [Devriendt et al., 2020] introduces a scaling correction to the AUUC calculation, ensuring a
more accurate assessment when the treatment and control groups are misaligned. The Area Under Cost Curve (AUCC)
[Du et al., 2019] is similar to AUUC but specifically evaluates performance in marketing contexts based on Return On
Investment (ROI). Furthermore, the Area Under Cost Curve for Multiple Treatments (MT-AUCC) [Zhou et al., 2023]
extends AUCC to scenarios involving multiple treatments.
These existing metrics primarily focus on the performance of uplift modeling. However, our main concern is online
revenue. Therefore, we propose the Area Under Cost Curve for Resource Allocation Simulation (RAS-AUCC), a metric
that more accurately reflects the overall effectiveness of online strategies.
2.3 Incremental Learning
Incremental learning [De Lange et al., 2019, Van de Ven et al., 2022, Belouadah et al., 2021] focuses on enabling models
to learn from non-stationary data streams, a concept widely applied in computer vision. A significant challenge in
incremental learning is catastrophic forgetting, where previously acquired knowledge is overwritten as new information
is introduced. To mitigate this issue, incremental learning methods can be categorized into three primary families
[De Lange et al., 2019]: parameter isolation methods, regularization-based methods and replay methods.
Parameter isolation methods. These methods allocate specific model parameters to different tasks, thereby preventing
interference between them. Context-dependent Gating (XdG) [Masse et al., 2018] employs separate gates to control
which parts of the model are used for each task. Hard Attention to the Task (HAT) [Serra et al., 2018] incorporates
task-specific embeddings to apply attention masking, facilitating selective knowledge sharing between tasks.
Regularization-based methods. These methods aim to retain previous knowledge while incrementally updating the
model through regularization. Elastic Weight Consolidation (EWC) [Kirkpatrick et al., 2017] introduces a penalty to
the loss function to restrict significant changes to important weights. Synaptic Intelligence (SI) [Zenke et al., 2017] is
akin to EWC but focuses on estimating weight importance based on their contribution to task performance. Learning
without Forgetting (LwF) [Li and Hoiem, 2017] utilizes knowledge distillation to preserve knowledge from previous
tasks while accommodating new ones.
Reply methods. These methods involve storing and revisiting previous data or representations to help the model
retain previous knowledge while learning new tasks. Averaged Gradient Episodic Memory (A-GEM) [Chaudhry et al.,
2018] employs a memory buffer to store and replay a subset of past data. Incremental Classifier and Representation
Learning (iCaRL) [Rebuffi et al., 2017] selects and retains samples closest to the representation mean of each class,
minimizing the loss on new classes while performing distillation on the replayed samples.
2.4 Knowledge Distillation Enhanced by Auxiliary Loss Techniques
Knowledge Distillation (KD) [Gou et al., 2021] is a technique in which a student model is trained to replicate the
output or intermediate representations of a teacher model. It enables the student to achieve improved performance
3

The Estimation of Continual Causal Effect for Dataset Shifting Streams
while maintaining computational efficiency. However, Zhang et al. [2024] highlights that this learning objective can be
sub-optimal due to discrepancies between the teacher’s output distribution and the ground truth distribution. To address
this issue, PTLoss [Zhang et al., 2024] transforms the vanilla teacher model into a proxy teacher model by perturbing
the leading-order terms in the Maclaurin series of the logarithmic term. PTLoss provides a generalized framework that
incorporates various techniques, including label smoothing [Szegedy et al., 2016], temperature scaling [Hinton, 2015]
and focal loss [Lin, 2017], through the manipulation of perturbation coefficients. Both theoretical and experimental
results demonstrate the effectiveness of PTLoss. Furthermore, Zhang et al. [2024] proposes an alternative solution that
offers valuable insights for enhancing the knowledge distillation process, making it more adaptable to the scenarios
discussed in this paper.
2.5 Continue Causal Effect Estimation
Continual causal effect estimation involves estimating the causal effects of treatments in dynamic settings, where data
evolves over time. The challenges associated with this estimation include not only counterfactual inference in the
presence of selection bias but also the need to adapt to changes in the dynamic environment. Continual Causal Effect
Representation Learning (CERL) [Chu et al., 2023] is the first attempt to address these issues. It builds upon the CFR
framework [Shalit et al., 2017], incorporating an elastic net regularization term and feature representation distillation.
Extensive experiments demonstrate its effectiveness in handling covariate shift within observational data streams with
binary treatment. However, real-world situations are often more complex. The scenarios involving multiple treatments
and concept drift are common in marketing. CERL does not account for these complexities, and this paper aims to
address these challenges.
3 Problem Statement
Let X denote the set of covariates (variables influencing the outcomes), Y denote the set of binary outcomes, T
denote the set of treatments, which consists of 0, 1, · · ·, |T |, and K denote the set of time periods, which consists of
0, 1, · · ·, |K|. In continual causal effects estimation, observational data are collected across different time periods. The
k-th dataset comprises the data {(x, y, t) | x ∈ X, y∈ Y, t∈ T } collected during the k-th time period, which contains
Nk units. Due to covariate shift and concept drift, the datasets {Dk}|K| k=0 exhibit different distributions with respect to X and varying relationships between X and Y .
Covariate shift can be expressed as:
P (x | k) ̸= P (x | k − 1) for k = 1, · · ·, |K|
Concept drift can be expressed as:
P (y | x, t, k) ̸= P (y | x, t, k− 1) for k = 1, · · ·, |K|
Let ti denote the treatment assignment for unit i. For multiple treatments, ti = 0 corresponds to the control group,
while ti = 1, ,· · ·, |T | corresponds to the treatment groups. The outcome for unit i is denoted by yt i when treatment
t is applied to unit i. In observational data, only one of the potential outcomes is observed, referred to as the factual
outcome, while all the remaining unobserved potential outcomes are termed counterfactual outcomes. For each time
period (except 0), the responses ˆyi of treatments t = 0, 1, . . . ,|T | applied to the unit i are predicted to estimate the
expected Individual Treatment Effect (ITE) τ t i under the treatments t = 1, 2, . . . ,|T |. Specifically, under three standard
assumptions [Rosenbaum and Rubin, 1983, Zhong et al., 2022], the estimate of τ t i can be expressed as follows:
τ t i = E(yt i − y0 i |xi) = E(yt i |t, xi) − E(y0 i |t, xi) (1)
Here, E[yt|t, x] represents the expected predicted response ˆyt i of individual xi under treatment t, for t = 0, 1, . . . ,|T |.
In scenarios such as marketing campaigns, the outcome yt i ∈ {0, 1} typically indicates whether the individual made a
purchase, while the predicted response ˆyt i ∈ [0, 1] represents the probability of purchase for that individual.
Our objective is to develop a novel continual causal effect inference framework that accurately estimates causal effects
from incrementally available data Dk in the presence of covariate shift and concept drift.
4 Methodology
As discussed in Section 2.1, most existing methods inadequately capture the dynamics prevalent in many industrial
applications. To address this challenge, we propose the Incremental Causal Effect with Proxy Knowledge Distillation
4

The Estimation of Continual Causal Effect for Dataset Shifting Streams
DR-CFR
k-1
𝑹𝒌−𝟏
Time period 𝒌 − 𝟏
𝑳𝑰𝑪𝑬−𝑷𝑲𝑫
DR-CFR
K
DR-CFR
k-1
DR-CFR
K
𝑫𝒌
𝑹𝒌
Corre
ctor
𝑳𝑩𝒂𝒔𝒆
𝑳𝑷𝑻+ KD
+
RM
Stop
Gradient
× 𝝁
Time period 𝒌 Time period 𝒌 + 𝟏
Figure 1: Architecture of the ICE-PKD framework. The blue trapezoids denote the base model, orange bars represent
the data, pink circles indicate the operators, yellow-gray rectangles correspond to the loss function. The black dashed
lines illustrate the processing of thereplayed dataset, while the black solid lines represent the processing of the latest
available dataset.
(ICE-PKD), an efficient framework for performing uplift modeling on incrementally available data. The architecture
of ICE-PKD is illustrated in Figure 1. Specifically, DR-CFR serves as the base model of ICE-PKD, providing robust
causal inference capabilities in multi-treatment observational data scenarios. The initial model selection ensures reliable
generalization before incremental training, while the knowledge distillation process preserves this generalization during
adaptation to new changes. To mitigate the influence of covariate shift, we use the replay mechanism to maintain
the accuracy and stability of the knowledge distillation process by optimizing the distillation process on the replayed
dataset. To mitigate the influence of concept drift, we transform the original teacher model into a proxy teacher to
improve the accuracy and reliability of the knowledge distillation by mitigating the discrepancy between the teacher
model’s output distribution and ground truth distribution.
4.1 The Base Causal Effect learning Model
In this section, we describe the base model for causal effect estimation in observational datasets. A key challenge in
estimating causal effects from observational data is selection bias, where the distribution of data varies across treatment
groups. This issue is obvious when there are few sample instances within a given domain for each treatment group,
complicating precise inferences about counterfactual outcomes.
To address this challenge, we employ the DR-CFR framework [Hassanpour and Greiner, 2019b]. This framework
disentangles covariates into underlying factors and balances the representation of confounders between control and
treatment groups. This method is effective in enhancing the accuracy of causal effect estimation. In this paper, we
extend it to accommodate multiple treatment scenarios while satisfying the monotonicity condition.
Learning Disentangled Representations. We assume that all covariates influencing the effect of the model are
generated by three underlying factors {Γ, ∆, Υ} [Hassanpour and Greiner, 2019b]. The instrumental factor Γ affects
only the treatment assignment, the confounding factor ∆ influences both the treatment and the outcome, and the
adjustment factor Υ determines only the outcome. While the presence of instrumental and confounding factors
introduces selection bias, confounding factors can still provide useful information for accurately estimating the response.
To model these factors, we employ three representation learning networks Γ(x), ∆(x) and Υ(x), which learn the
respective factors from data.
Re-Weighting Function. To address the selection bias in estimating Individual Treatment Effects, [Hassanpour and
Greiner, 2019b] employs context-aware importance sampling, where the weights are derived exclusively from ∆(x). In
this work, we extend this approach to accommodate the multi-treatment scenario:
w(ti, ∆(xi)) = 1 +
X
j̸=i
p(ti)
p(tj) · π(tj | ∆(xi)) π(ti | ∆(xi)) (2)
5

The Estimation of Continual Causal Effect for Dataset Shifting Streams
Imbalance Loss. Based on the definition of the adjustment factor Υ, the distribution of learned adjustment factors
Υ(x) should be similar across treatment groups [Hassanpour and Greiner, 2019b]. To quantify the distributional
differences of Υ(x), Hassanpour and Greiner [2019b] utilize the Wasserstein distance, incorporating it as a penalty
term in the loss function. We now extend this formulation to the multi-treatment case:
LIm =
|T |X
t=1
disc({Υ(xi)}i:ti=0 , {Υ(xi)}i:ti=t) (3)
Cross Entropy Loss. The combined representations of instrument factors and confounding factors contain sufficient
information to reconstruct the decision rules for the treatment assignment [Hassanpour and Greiner, 2019b]. Therefore,
Hassanpour and Greiner [2019b] leverage the learned representations Γ(x) and ∆(x) to predict the assigned treatments,
minimizing the loss function to ensure that all relevant information pertaining to treatment assignments is captured in
these two representations. The following formula defines the loss function in the multi-treatment case:
π(t|Γ(x), ∆(x)) = eφ(Γ(x),∆(x)) t P|T |
t=0 eφ(Γ(x),∆(x)) t (4)
LCE = 1 N
NX
i=1
− log [π (ti|Γ(xi), ∆(xi))] (5)
Multi-task Learning Architecture for Estimating Factual Loss. The combination of the learned representations
∆(x) and Υ(x) retains sufficient information for accurate factual estimation. In scenarios with a finite number of
treatments, drawing inspiration from the TarNet framework [Shalit et al., 2017], we employ a multi-task learning
structure for factual estimation using ∆(x) and Υ(x). Specifically, each treatment t corresponds to a separate task
network ht(·). We first obtain a shared representation for all tasks by passing the union of ∆(x) and Υ(x) through a
network. Subsequently, each task network ht(·) is trained independently, allowing the model to learn treatment-specific
responses while sharing common features across tasks. This multi-task approach enhances learning efficiency by
leveraging shared information across treatments while capturing the nuances of each treatment assignment. When the
outcome Y is binary, the factual loss function is calculated as follows:
LF ac(x, y, t) = −

y log

gt(∆(x), Υ(x))  + (1 − y) log  1 − gt(∆(x), Υ(x))  (6)
ATE Loss. In practical contexts, such as optimizing the ROI for marketing campaigns, the accuracy of the average
treatment effects is as crucial as the ranking of treatment effects. To enhance the estimate of average treatment effects,
we employ the ATE loss, which is as follows:
LAT E= 1 |T |
|T |X
t=1
| ˆATEt − ATEt| = 1 N · |T |
|T |X
t=1
|(
NX
i=1
ˆyi:ti=t −
NX
i=1
ˆyi:ti=0) − (
NX
i=1
yi:ti=t −
NX
i=1
yi:ti=0)| (7)
Monotonicity Penalty Loss. In online scenarios, such as modeling user purchase propensity at varying discount levels,
the monotonicity assumption is often regarded as prior knowledge. As the treatment level increases, the individual
response is expected to increase. To incorporate this knowledge into our model, we define the concept of monotonicity
penalty loss, which penalizes any violation of this monotonicity assumption. The loss function is as follows:
LM ono= 1 N
NX
i=1
|T |X
t=1
ReLU(ˆyt−1 i − ˆyt i ) (8)
Here, ReLU denotes the rectified linear unit function, which ensures that the penalty is applied only when the predicted
response at the higher treatment level is less than the smaller.
Overall Loss Function of DR-CFR Here, we review the above loss functions and present the overall loss function
for the base causal effect learning model, defined as:
LBase = 1 N
NX
i=1
w(ti, ∆(xi)) · LF ac(xi, yi, ti)
+ α · LCE + β · LIm + γ · LAT E+ δ · LM ono+ λ · LReg
(9)
where LReg is the regularization term, α, β, γ, δ and λ are hyperparameters that control the scale of each component.
6

The Estimation of Continual Causal Effect for Dataset Shifting Streams
4.2 The Continual Incremental Causal Effect Learning
Building on the base causal effect learning model, we propose the ICE-PKD framework. This framework effectively
addresses both covariate shift and concept drift by first training a well-generalized initial model on the initially available
data and then updating it with incrementally available data.
Initial Model Selection and Parameter Initialization. Given the complexity of the uplift model, random initialization
of the parameters can lead to significant performance perturbations. To mitigate this, we train the model multiple
times on the initially available data and select the optimal model gt θ0 (x). Furthermore, similar to the incremental learning approaches in computer vision [Li and Hoiem, 2017, Rebuffi et al., 2017], we initialize the parameters of the
incremental model based on those of the previously trained model. Specifically, during the k-th incremental training of
the model, we initialize the model parameters θk using θk−1, which are the parameters obtained after the (k − 1)-th
incremental training.
Loss Function Regularization via Knowledge Distillation. To ensure model generalization during incremental
training, we draw inspiration from the class-incremental method LwF [Li and Hoiem, 2017] and adapt it to the uplift
model scenario. Under the assumption of concept drift, our focus is the difference in predicted distributions between
the model before and after incremental training. Specifically, we examine the discrepancy between the model gθk (x)
and the model gθk−1 (x). To quantify this difference, we employ the Kullback-Leibler (KL) Divergence. In the context
of a binary outcome problem, the KL Divergence is computed as:
DKL(y ∥ ˆy) = y log y ˆy + (1 − y) log 1 − y 1 − ˆy (10)
where y represents the ground truth label and ˆy represents the predicted probability.
Thus, the knowledge distillation loss function LKD during the k-th incremental training is calculated as:
LKD = 1 N
NX
i=1
|T |X
t=0
DKL(gt θk−1 (xi) ∥ gt θk (xi)) (11)
where the superscript t indicates the model’s response under the treatment t, θk−1 are the model parameters after the
(k − 1)-th incremental training (which remain fixed during this process), and θk are the model parameters updated
during the current incremental training.
By penalizing the difference in predictive distributions between the model before and after incremental training, we aim
to preserve previous knowledge and mitigate catastrophic forgetting.
Replay Mechanism. Due to covariate shift, relying solely on new data to calculate distributional differences for
preserving previous knowledge becomes unfeasible, as neural networks often perform poorly when predicting out-of-
distribution data. Drawing inspiration from the class-incremental method iCaRL [Rebuffi et al., 2017] in computer
vision, we apply knowledge distillation to a replayed subset of the previous dataset. However, unlike image classification
tasks, sample or feature centers do not play a significant role in our scenario. Therefore, we adopt a uniform sampling
approach, preserving approximately one percent of the initial available sample size from the previous dataset as a
representation of previous training data. Specifically, we set:
Nsave =
j
0.01 · ˜N0
k
(12)
where ˜N0 is the sample size used for training the base model, and Nsave represents the integer part of 0.01 · ˜N0.
After the (k − 1)-th incremental training, we have not only model parameters θk−1 but also the replayed dataset
Rk−1, which consists of Nsave samples, along with the sample size ˜Nk−1 used for previous training. During the k-th
incremental training, the latest available dataset Dk with Nk samples is utilized. The sample size used for previous
training is then updated as follows:
˜Nk = ˜Nk−1 + Nk (13)
To determine the size of the replayed dataset Rk from Rk−1 and Dk, we calculate:
N R save, ND save =
$
Nsave · ˜Nk−1
˜Nk
%
,
 Nsave · Nk
˜Nk

(14)
7

The Estimation of Continual Causal Effect for Dataset Shifting Streams
For uniform sampling, we generate sequences of random numbers:
r1, r2, . . . , rNsave, d1, d2, . . . , dNk ∼ U (0, 1) (15)
where {ri}Nsave i=1 and {di}Nk i=1 are sequences of random numbers corresponding to the indices of the datasets Rk−1 and
Dk, respectively. These random sequences are sorted, and we select the first N R save samples from Rk−1 and N D save
samples from Dk to form the replayed dataset Rk for the (k + 1)-th incremental training.
This sampling procedure can be expressed as:
Rk ← UniformSample(Rk−1, NR save) ∪ UniformSample(Dk, ND save)
Proxy Teacher for Knowledge Distillation. Concept drift introduces a natural discrepancy in the output distributions
of the teacher model used for knowledge distillation, even without considering training bias. Consequently, the teacher
model can produce a biased estimate of the label distribution. Requiring the student to blindly imitate the teacher
model gθk−1 (x) can lead to the student inheriting biases, resulting in suboptimal predictions during the k-th incremental
training. To mitigate this issue, we transform the original teacher into a proxy teacher by incorporating a corrector
hθc (x) in the calculation of KL divergence, drawing inspiration from the alternative solution of PTLoss [Zhang et al.,
2024]. The loss function for knowledge distillation is then calculated as follows:
LP T= 1 N
NX
i=1
|T |X
t=0
DKL(gt θk−1 (xi) + ht θc (xi) ∥ gt θk (xi, t)) (16)
This formulation is similar to Eq. 11. The difference is the addition of the corrector hθc, which is a neural network
sharing the same input covariates and output dimensions as gθk−1 (x).
Additionally, we configure the activation function of the hidden layers to ReLU and the output layer to Tanh, while
employing the Xavier initialization method to ensure that the output values of the hθc remain small before training.
This mitigates large perturbations to the teacher model at the onset of training, facilitating more rapid convergence,
which aligns well with incremental learning approaches that employ a smaller learning rate and fewer training epochs.
With this modification, not only are the updates to the model’s parameters θk influenced by the previous knowledge (i.e.
teacher model gθk−1 (x)), but also the teacher model is guided and corrected by the new data during thek-th incremental
training.
Overall Loss Function of ICE-PKD. The overall loss function of ICE-PKD during the k-th incremental training is
calculated as follows:
LICE −P KD= LBase|Dk + µ · LP T|Rk−1 (17)
where µ is a weighting coefficient, LBase|Dk denotes LBase computed on the latest available dataset Dk, and
LP T|Rk−1 represents LP Tcalculated on the replayed dataset Rk−1.
Finally, we summarize the procedures of ICE-PKD. The pseudo code of ICE-PKD can be found at Algorithm 1.
5 Experiments and Evaluations
5.1 Description of the datasets
To accurately assess the model performance, we conduct experiments on both synthetic datasets and online datasets.
The synthetic datasets [Berrevoets and Verbeke, 2019] align with our assumptions and provide access to ground truth
(i.e., counterfactual outcomes). The online dataset further demonstrates the practical applicability and significance of
the proposed method. The datasets are described as follows:
5.1.1 Synthetic Dataset
We first consider a 2-dimensional synthetic dataset [Berrevoets and Verbeke, 2019] with three treatments, facilitating
both analysis and visualization. For each time period k, the exact responses under different treatments are given by the
following equations:
pk,0(x1, x2) = σ

0.6x2 1 + x1x2 2 − (0.5 − d0(k)) · x1 − (0.6 − 0.5d0(k)) · x2 + 0.2d0(k) + ϵ  (18)
pk,1(x1, x2) = σ

0.7x2 1 + 0.1x2 2 + x1x2 2 − (0.5 − d1(k)) · x1 − (0.5 − 0.5d1(k)) · x2 + 0.2d1(k) + ϵ  (19)
pk,2(x1, x2) = σ

0.9x2 1 + 0.15x2 2 + x1x2 2 − (0.5 − d2(k)) · x1 − (0.5 − 0.5d2(k)) · x2 + 0.2d2(k) + ϵ  (20)
8

The Estimation of Continual Causal Effect for Dataset Shifting Streams
Algorithm 1 Incremental Causal Effect with Proxy Knowledge Distillation (ICE-PKD)
Require: Initial dataset D0, incremental data sequence {Dk}|K| k=1
Ensure: Trained model θk for k = 1, · · ·, |K|
1: Initialize:
2: Train base model: θ0 ← arg minθ LBase|D0
3: Initialize replay buffer: R0 ← UniformSample(D0, Nsave)
4: Set total sample count: ˜N0 ← N0
5: for k = 1 to |K| do
6: θk ← θk−1 {Inherit previous parameters}
7: Initialize corrector network hθc using Xavier initialization
8: Build proxy teacher: gt θk−1 (x) + ht θc (x)
9: Merge train datasets: Dk ∪ Rk−1
10: for epoch = 1 to epochs do
11: Update parameters: θk ← θk − η∇θk (LBase|Dk + µ · LP T|Rk−1)
12: Update corrector: θc ← θc − η∇θc (LP T|Rk−1)
13: end for
14: Update total sample count: ˜Nk ← ˜Nk−1 + Nk
15: Compute sample sizes:
16: N R save ← ⌊Nsave · ˜Nk−1/ ˜Nk⌋
17: N D save ← ⌈Nsave · Nk/ ˜Nk⌉
18: Rk ← UniformSample(Rk−1, NR save) ∪ UniformSample(Dk, ND save)
19: end for
20: return θk for k = 1, · · ·, |K|
Figure 2: Response Function Visualization for k = 0. The blue surface corresponds to t = 0, the red surface to t = 1,
and the green surface to t = 2.
where x1, x2 ∈ [0, 1], and σ(·) represent the logistic sigmoid function, which maps the polynomial expressions to
the range [0, 1]. The term ϵ ∼ N(0, 0.0001) represents Gaussian noise, and x = ( x1, x2) is a covariate with two
components. The treatments t = 0, 1, 2 correspond to different coupon amounts, while d0(k), d1(k), d2(k) represent
concept drift that varies over time, indexed by the time period k. The specific relationship between di(k) and k is
defined as follows:
di(k) =
0.1ik + 0.2k if 0 ≤ k ≤ 3
−0.1ik + 0.65i − 0.2k + 1.3 if 4 ≤ k ≤ 6 for i = 0, 1, 2 (21)
Figure 2 presents the visualization of the response function for the time period k = 0 . As shown, the generated
functional relationships adhere to the monotonicity assumption, aligning with online expectations. Specifically, a user’s
willingness to purchase increases as the discount rises.
9

The Estimation of Continual Causal Effect for Dataset Shifting Streams
To satisfy the assumption of covariate shift, we generate a training covariate dataset of size 10,000 and a test covariate
dataset of size 50,000, utilizing four truncated normal distributions and one uniform distribution for each time period k.
The means of the truncated normal distributions are randomly selected from the range [0.2, 0.8], while their standard
deviations are chosen from [0.01, 0.1], with covariance set to zero. According to the properties of normal distributions,
most points lie within the domain [0, 1] × [0, 1], and any points outside this domain are truncated to fall within the
domain boundaries. The uniform distribution is denoted as U [0, 1].
According to Eqs. 18, 19 and 20, we can derive the exact response probabilities for the three treatments, which are
subsequently used to evaluate the Precision in Estimation of Heterogeneous Effect (PEHE). Additionally, these response
probabilities serve as parameters in Bernoulli experiments to generate the corresponding labels.
In the test dataset, each covariate is randomly assigned a treatment, ensuring the absence of selection bias. In the
training dataset, treatments are applied according to predefined rules. Specifically, when x1 + x2 < 0.8, neither the
uplift from t = 0 to t = 1 nor from t = 1 to t = 2 is significant. In this case, we prefer to apply treatment t = 0 to
covariates in this region, while the probabilities of applying t = 1 or t = 2 are both relatively low. Practically, we
perform a Bernoulli test with a probability of 0.6 and applyt = 0 if successful; otherwise, we conduct another Bernoulli
test with a probability of 0.5 and apply t = 1 if successful. If neither test is successful, we apply t = 2. Conversely,
when x1 + x2 > 1.2, treatment t = 1 is preferred, while for 0.8 ≤ x1 + x2 ≤ 1.2, treatment t = 2 is preferred.
For the 10-dimensional synthetic dataset, we replicate the process used for the 2-dimensional dataset. The primary
distinction is the increased dimensionality, which results in a larger dataset for both training and testing.
5.1.2 Online Dataset
In Huaxiaozhu’s new passenger acquisition campaign, we have access to substantial data that exhibits both covariate shift
and conceptual drift. To capture these dynamics, we partition the data over time, following the model updating strategy
employed in previous online work. Specifically, the non-incremental model updating strategy utilizes approximately 1
million records from the past 9 weeks each week, balancing resource constraints with model effectiveness. For each
time period k, the records from the subsequent week are considered as the test dataset. We use around 120,000 new
passenger records each week as an incremental training set Dk for time period k = 1, 2, · · ·, 6, while the initially
available dataset comprises approximately 1 million records from the 9 weeks preceding the start of the experiment.
For modeling, we utilize a 53-dimensional feature space that includes covariates such as city-specific characteristics and
historical statistics. The campaign involves eight treatment levels, corresponding to coupon amounts 3, 4, . . . ,10, with
treatments indexed as t = 0, 1, . . . ,7. The control group is represented by t = 0, which corresponds to a minimum
coupon amount of 3. The outcome label y ∈ {0, 1} indicates whether an order is completed (y = 0) or not (y = 1).
5.2 Experimental Setting
For the synthetic dataset, we sequentially split the 10% of each training dataset for the time period k as the available
dataset Dk. This criterion is motivated by the observed decline in online performance during this period. To predict
the test dataset for each time period k, where k = 1 , 2, · · ·, 6, we apply our model, ICE-PKD, along with three
comparison strategies. In the incremental updating of ICE-PKD, we first select an initial model gt θ0 (x) that achieves optimal performance on the initially available data (i.e. the entire training dataset at the time period k = 0) and then
incrementally update the model with Dk for each k = 1, 2, · · ·, 6. To further demonstrate the effectiveness of ICE-PKD,
we compare it with three alternative strategies: DR-CFR A trains the DR-CFR using the entire training dataset from the
previous time period k − 1, serving as the baseline; DR-CFR B trains the DR-CFR using only the latest available dataset
Dk, which limits generalization; DR-CFR C does not update the model gt θ0 (x), sacrificing real-time adaptability.
For the online dataset, we simulate a scenario where the exact time of drift occurrence is unknown, assuming that drift
emerges gradually over time. To predict the test dataset for each time period k, where k = 1, 2, · · ·, 6, we again apply
ICE-PKD and three comparison strategies. In the incremental updating of ICE-PKD, we select an initial model gt θ0 (x) that performs best on the initially available records and then update the model incrementally with Dk. DR-CFR A
trains the DR-CFR using the records from the past 9 weeks (including Dk), serving as the baseline. DR-CFR B trains
the DR-CFR using only the latest available dataset Dk. DR-CFR C does not update the model gt θ0 (x). Table 1 presents a comparative analysis of various strategies, focusing on key aspects such as the use of the latest data, data volume, and
the application of incremental updates.
Throughout the experiment, all settings remain consistent, except for the configuration of ICE-PKD, which introduces
an additional corrector and utilizes a smaller learning rate along with fewer training epochs. Specifically, for the
2-dimensional synthetic dataset, ICE-PKD has 8,952 parameters, while the other non-incremental models have 8,409
parameters. The learning rate is set to 1 × 10−4 for ICE-PKD and 1 × 10−3 for the others. Training epochs are set
10

The Estimation of Continual Causal Effect for Dataset Shifting Streams
Table 1: Comparative Analysis of Various Strategies
Strategy Use of Latest Data Data volume Incremental Updates
DR-CFR A Yes 100, 000 No
DR-CFR B Yes 14, 000 No
DR-CFR C No 100, 000 No
ICE-PKD Yes 100, 000 + k × 14, 000 Yes
to 10 for ICE-PKD and 20 for the others. For the 10-dimensional synthetic dataset, ICE-PKD has 50,372 parameters,
while the others have 48,169. For the online dataset, ICE-PKD has 463,612 parameters, while the others have 456,204.
5.3 Evaluation Metrics
In this study, we adopt three commonly used evaluation metrics: Average Treatment Effect Error (ATE Error), Precision
in Estimation of Heterogeneous Effect (PEHE) [Hill, 2011] and QINI Coefficient [Devriendt et al., 2020]. These metrics
are essential for assessing the performance of model predictions. However, a gap (constrained optimization method)
exists between model predictions and online decision-making. Therefore, improved predictions do not necessarily
translate to increased online revenues. To address this, we introduce a novel simulation metric, Area Under Cost Curve
for Resource Allocation Simulation (RAS-AUCC), which provides a more accurate reflection of the overall performance
of online strategies using randomized controlled trial(RCT) data. The specific formulas and principles are as follows:
ATE Error . ATE Error quantifies the difference between the estimated and true average treatment effects for the
treatment group. It helps evaluate the accuracy in predicting the overall treatment effect. In scenarios with multiple
treatments, the ATE Error is calculated as the average across all treatment groups. The formula is given by:
ϵAT E= 1 |T |
|T |X
t=1
| ˆATEt − ATEt| (22)
where ˆATEt is the estimated ATE for the treatment group t and ATEt is the true ATE for the treatment group t.
PEHE. PEHE evaluates the model’s accuracy in predicting heterogeneous treatment effects across the entire pop-
ulation, specifically applied to synthetic datasets. This metric is computed as the square root of the average squared
differences between the predicted and ground truth treatment effects, weighted by the population size. The formula of
PEHE is:
ϵP EHE= 1 N · |T |
NX
i=1
|T |X
t=1
(ˆτ t i − τ t i ) 2 (23)
where ˆτ t i is the predicted treatment effect for individual i in treatment group t, τ t i is the true treatment effect for
individual i in treatment group t and N is the total number of individuals.
QINI. The QINI Coefficient is a metric designed to evaluate the ranking performance of uplift estimation. It quantifies
the difference in rewards between treatment and control groups on a per-segment basis, following the sorting of samples
by their estimated uplift. To enhance its applicability in multi-treatment scenarios, we employ the average QINI
Coefficient as a performance measure. The QINI Coefficient is calculated as the area under the QINI Curve. Sort all the
quintuples from the treatment ˜t and control groups in descending order of estimated individual treatment effect. Let m
represent a percentage (e.g. 10%, 20%) and define Sm as the set of samples corresponding to the top m percent. For
treatment ˜t, the values for the QINI Curve are computed as follows:
V (m) =
X
i∈Sm
I(yi = 1, ti = ˜t) −
P
i∈Sm I(yi = 1, ti = 0) P i∈Sm I(t = ˜t)P
i∈Sm I(ti = 0) (24)
where I(·) denotes the indicator function, such that I(ti = 0) equals 1 when ti = 0 and 0 otherwise.
11

The Estimation of Continual Causal Effect for Dataset Shifting Streams
∆𝐶𝑜𝑠𝑡(𝑏) ∆𝐶𝑜𝑠𝑡
∆𝑅𝑒𝑤𝑎𝑟𝑑(𝑏)
∆𝑅𝑒𝑤𝑎𝑟𝑑
𝐴𝑠
𝐴𝐿
Model
Straight
Figure 3: RAS-AUCC. The red line represents the model’s predicted curve, while the green line represents the straight-
line benchmark. ∆Cost and ∆Reward indicate the maximum cost and the maximum reward when the largest treatment
is applied to each individual.
RAS-AUCC. We assume the availability of a RCT dataset consisting ofN samples. Given a specific budget b, we
can determine the decision-making allocation tb i based on the model predictions for each individual i. The allocation
method commonly employed is a constrained optimization algorithm in marketing, such as 0-1 integer programming
and greedy algorithms. In the RCT dataset, we can obtain the ground truth cost and reward associated with a treatment
value for each individual i, denoted as ci for cost and ri for reward. This allows us to estimate the incremental cost
∆Cost(b) and the incremental reward ∆Reward(b).The specific formulas are as follows:
∆Cost(b) = N ·
 P
i I(ti > 0, ti = tb i )ciP
i I(ti > 0, ti = tb i ) −
P
i I(ti = 0)ciP
i I(ti = 0)

(25)
∆Reward(b) = N ·
 P
i I(ti > 0, ti = tb i )riP
i I(ti > 0, ti = tb i ) −
P
i I(ti = 0)riP
i I(ti = 0)

(26)
Our objective is to maximize the ratio of the incremental rewards to the incremental costs, i.e. ROI. Similar to the
QINI curve, we can derive a curve based on the ∆Cost(b) and ∆Reward(b). As illustrated in Figure 3, the area under
this curve is AS, while the area under the straight line is AL, which is used for normalization. Consequently, the
RAS-AUCC is calculated as (AS − AL)/AL.
5.4 Evaluation Framework for Continual Causal Effects Estimation
Estimating continual causal effects involves various evaluation metrics across multiple time periods, complicating the
assessment of model performance. Therefore, establishing a comprehensive and robust assessment framework is crucial.
A common approach is to compare the average differences of each metric across time periods. However, this method is
highly sensitive to extreme values. Specifically, a significant increase or decrease in one time period can distort the
observed effects in others. To address this challenge, we propose the use of two stability indicators to jointly evaluate
the model’s performance.
PRIO-10. The Percentage of Relative Improvement Over 10% (PRIO-10) measures the proportion of cases where
the model’s improvement exceeds 10%. This indicator assesses the overall performance gain relative to the baseline.
Specifically, given the Baseline Mbaseline, for any model A, and for any evaluation metric E that benefits from larger
values (such as QINI and RAS-AUCC), the improvement [Zhong et al., 2022] is calculated as:
Impr k(A) = Ek(A) − Ek(Mbaseline) |Ek(Mbaseline)| × 100%, k = 1, 2, · · ·, |K| (27)
where k represents the different time periods. The PRIO-10 for method A is then calculated as:
PRIO-10(A) = 1 |K|
|K|X
k=1
I(Impr k(A) > 10%) × 100% (28)
12

The Estimation of Continual Causal Effect for Dataset Shifting Streams
In contrast, for any evaluation metric that improves with smaller values, such as ATE Error and PEHE, the improvement
is calculated by multiplying the result by −1.
PRDU-5. The Percentage of Relative Deterioration Under 5% (PRDU-5) measures the proportion of cases in which
the model’s performance deteriorates under 5%. This metric evaluates the model’s ability to avoid significant declines
in performance, providing insight into its stability across different time periods.
AD. The Average Difference (AD) assesses the model’s overall performance by calculating the average difference in
evaluation metrics between the model and the baseline across all time periods. This indicator offers a straightforward
measure of how well the model performs relative to the baseline.
6 Experiment Results
This section presents the results of our experiments, providing a comparative analysis of various strategies,and
conducting an ablation experiment to explain the contribution of each module.
6.1 Performance Comparison
We assess the effectiveness of ICE-PKD by comparing it against other strategies on both synthetic and online datasets,
as detailed in Table 2. The experimental setup is described in Section 5.2. Key insights from the results are summarized
below.
Compared to other strategies, ICE-PKD consistently demonstrates superior performance on both synthetic and online
datasets. Specifically, ICE-PKD achieves the largest reductions in the error metrics ϵAT Eand ϵP EHE, as well as almost
the most significant improvements in the order metrics QINI and RAS-AUCC. Notably, it is the only strategy that
surpasses the baseline (DR-CFR A) across all indicators. Emphasize here, the robustness of the AD is evidenced by the
performance of all other indicators, while the confidence of RAS-AUCC is reflected in other metrics.
In contrast, DR-CFR B, which is trained solely on the most recent dataset Dk, demonstrates lower performance in
order metrics. On the 2-dimensional synthetic dataset, it is outperformed by both DR-CFR C and ICE-PKD in terms of
ϵP EHE. Although DR-CFR B performs better than DR-CFR C in AD for RAS-AUCC, it significantly underperforms in
PRIO-10 and PRDU-5, which is undesirable. On the 10-dimensional synthetic dataset, it performs worse than DR-CFR
C in AD for RAS-AUCC, further underscoring its unreliability. On the online dataset, DR-CFR B’s performance is
even worse, significantly trailing the baseline in both QINI and RAS-AUCC. These results suggest that DR-CFR B
lacks generalization and may overfit when trained on smaller datasets.
DR-CFR C, which does not update the initial model gt θ0 (x), exhibits poorer performance across the error metrics. Notably, it performs the worst in ϵAT E, being the only strategy significantly below the baseline for both the 2-
dimensional synthetic dataset and the online dataset. Although DR-CFR C performs well on some AD indicators, its
stability indicators (PRIO-10 and PRDU-5) are generally the worst, indicating it is not a reliable choice. This poor
performance can be attributed to the model’s lack of real-time adaptability in the presence of covariate shift and concept
drift.
To further illustrate these findings, we visualize the comparison results for the 2-dimensional synthetic dataset in Figure
4. The vertical axis represents the difference between each strategy’s metrics and the baseline’s across different time
periods k. ICE-PKD (represented by the purple line with circular marker points) consistently performs best, positioned
at the bottom of the subplots for ϵAT Eand ϵP EHE, and at the top of the subplots for QINI and RAS-AUCC. In contrast,
DR-CFR B (yellow line with triangle markers) exhibits significant fluctuations due to the smaller training set. DR-CFR
C (green line with square markers) performs poorly, particularly in ϵAT Eand ϵP EHE, due to its lack of real-time
adaptability. These visual observations closely align with the analytical results discussed above.
In conclusion, ICE-PKD outperforms all other strategies across both synthetic and online datasets, demonstrating its
robustness, adaptability and effectiveness in addressing covariate shift and concept drift.
6.2 Ablation Experiment
To evaluate the contribution of each component in ICE-PKD, we conducted an ablation experiment on the 2-dimensional
synthetic dataset. In this experiment, we systematically removed key components of the model to assess their impact on
performance. The results are presented in Table 3.
We define three variants of ICE-PKD by removing the following components:
13

The Estimation of Continual Causal Effect for Dataset Shifting Streams
Table 2: Performance comparison of different strategies on synthetic and online datasets
ϵAT E ϵP EHE QINI RAS-AUCC
strategy PRIO-10 PRDU-5 AD PRIO-10 PRDU-5 AD PRIO-10 PRDU-5 AD PRIO-10 PRDU-5 AD
synthetic
dataset
2d
DR-CFR A - - 0 - - 0 - - 0 - - 0
DR-CFR B 83.3% 83.3% -0.0065 50% 66.7% 0.0028 83.3% 83.3% 0.0286 66.7% 66.7% 0.0566
DR-CFR C 33.3% 50% 0.0032 50% 66.7% -0.0017 66.7% 66.7% 0.0233 100% 100% 0.0457
ICE-PKD 100% 100% -0.0313 100% 100% -0.0195 100% 100% 0.0418 100% 100% 0.0669
synthetic
dataset
10d
DR-CFR A - - 0 - - 0 - - 0 - - 0
DR-CFR B 16.7% 33.3% 0.0073 33.3% 66.7% -0.0164 16.7% 33.3% -0.0019 66.7% 66.7% 0.0161
DR-CFR C 0% 0% 0.0154 33.3% 33.3% -0.0104 16.7% 16.7% -0.0155 66.7% 66.7% 0.0540
ICE-PKD 83.3% 100% -0.0177 100% 100% -0.0276 100% 100% 0.0112 66.7% 100% 0.0699
online
dataset
DR-CFR A - - 0 - - - - - 0 - - 0
DR-CFR B 50% 50% -0.0002 - - - 33.3% 33.3% -0.0289 50% 50% -0.0097
DR-CFR C 33.3% 33.3% 0.0039 - - - 66.7% 83.3% 0.0213 83.3% 100% 0.0789
ICE-PKD 66.7% 100% -0.0023 - - - 83.3% 83.3% 0.0273 83.3% 100% 0.0495
1 2 3 4 5 6
time period k
0.06
0.04
0.02
0.00
0.02
0.04
0.06
0.08
difference
ATE
Strategy A
Strategy B
Strategy C
ICE-PKD
1 2 3 4 5 6
time period k
0.04
0.02
0.00
0.02
0.04
0.06
difference
PEHE
Strategy A
Strategy B
Strategy C
ICE-PKD
1 2 3 4 5 6
time period k
0.02
0.00
0.02
0.04
0.06
0.08
difference
QINI
Strategy A
Strategy B
Strategy C
ICE-PKD
1 2 3 4 5 6
time period k
0.04
0.02
0.00
0.02
0.04
0.06
0.08
0.10
0.12
difference
RAS-AUCC
Strategy A
Strategy B
Strategy C
ICE-PKD
Figure 4: Comparison of performance metrics across different strategies. Each subfigure illustrates a specific metric,
with the horizontal axis representing different time periods k and the vertical axis depicting the difference in metric
values between the various strategies and the baseline (DR-CFR A).
w/o PT: ICE-PKD without the proxy teacher for knowledge distillation.
w/o RM: ICE-PKD without the replay mechanism.
w/o KD: ICE-PKD without the knowledge distillation process.
For each variant, the experimental setup is consistent with ICE-PKD. The results in Table 3 yield the following key
insights:
Impact of Proxy Teacher (PT): The removal of the proxy teacher for knowledge distillation (w/o PT) results in a
significant decline in overall performance across all metrics. Specifically, ϵAT Eand ϵP EHEexhibit increased error
values, with the AD for these metrics worsening from -0.0313 to -0.0270 and from -0.0195 to -0.0171, respectively.
Additionally, both QINI and RAS-AUCC show decreased values, with the AD dropping from 0.0418 to 0.0397 and from
0.0669 to 0.0634, respectively. These results underscore the critical role of the proxy teacher in knowledge distillation,
as it enhances the overall performance of ICE-PKD by preventing the model from blindly mimicking the teacher in the
presence of concept drift.
Impact of Replay Mechanism (RM): The exclusion of the replay mechanism (w/o RM) leads to the most pronounced
decrease in performance, especially for RAS-AUCC. Specifically, the PRIO-10 drops from 100% to 83.3%, and the AD
decreases from 0.0669 to 0.0434. These findings highlight the importance of preserving previous knowledge through
the replayed dataset. Given that neural network models often struggle with out-of-distribution data, relying solely on
knowledge distillation with the latest available data can misguide the model when faced with covariate shift.
Impact of Knowledge Distillation (KD): The absence of the knowledge distillation process (w/o KD) significantly
undermines stability indicators. Specifically, PRIO-10 forϵAT Eand ϵP EHEdecreases to 83.3% and 66.7%, respectively,
while PRDU-5 for ϵAT Ealso drops to 83.3%. These results illustrate the essential role of knowledge distillation in
maintaining stable and accurate predictions over time.
ICE-PKD: The ICE-PKD framework consistently outperforms its ablated variants across all metrics, achieving the
lowest average error metrics, the highest average order metrics, and the highest stability indicators. For instance,
ICE-PKD achieves 100% in both PRIO-10 and PRDU-5 for ϵP EHEand RAS-AUCC, along with the lowest AD values
for ϵP EHEand the highest for RAS-AUCC. These results confirm the effectiveness of integrating all components in the
proposed method.
14

The Estimation of Continual Causal Effect for Dataset Shifting Streams
Table 3: Ablation study on synthetic dataset
ϵAT E ϵP EHE QINI RAS-AUCC
strategy PRIO-10 PRDU-5 AD PRIO-10 PRDU-5 AD PRIO-10 PRDU-5 AD PRIO-10 PRDU-5 AD
synthetic
dataset
ICE-PKD 100% 100% -0.0313 100% 100% -0.0195 100% 100% 0.0418 100% 100% 0.0669
w/o PT 83.3% 100% -0.0270 83.3% 100% -0.0171 100% 100% 0.0397 100% 100% 0.0634
w/o RM 100% 100% -0.0257 83.3% 100% -000169 100% 100% 0.0421 83.3% 100% 0.0434
w/o KD 83.3% 83.3% -0.0271 66.7% 100% -0.0170 100% 100% 0.0407 100% 100% 0.0637
In conclusion, the ablation experiment validates the design of ICE-PKD, highlighting the critical contributions of proxy
teacher, replay mechanism and knowledge distillation to the overall performance. Collectively, these components
enhance the model’s robustness, stability and accuracy.
6.3 Online Performance
We have conducted an online A/B test experiment in Huaxiaozhu’s new passenger acquisition campaign. By deploying
the proposed incremental updating strategy, we have achieved a 0.14% improvement in the average weekly completion
rate compared to non-incremental strategies. This result further demonstrates the effectiveness of the ICE-PKD
framework.
7 Conclusion
In this paper, we introduce the ICE-PKD framework to address the challenges of continual causal effect estimation in
marketing, where covariate shift and concept drift frequently occur. Our approach extends the DR-CFR framework to
accommodate multiple treatments and presents a novel incremental method for uplift modeling.
The experimental results demonstrate that ICE-PKD consistently outperforms alternative strategies across both synthetic
and online datasets. In the presence of covariate shift and concept drift, ICE-PKD can effectively ensure stable
and superior performance over time. Additionally, ablation experiments highlight the crucial roles of the integrated
components in enhancing the model’s performance and robustness.
Overall, ICE-PKD represents a significant advancement in continual causal effect estimation, providing a more
effective and robust approach for dynamic marketing environments. Several promising avenues for future research
include exploring uplift models better suited for estimating continuous causal effects and investigating advanced
incremental learning methods, such as enhanced knowledge distillation techniques, improved replay mechanisms and
other specialized structures.
References
Bowei He, Yunpeng Weng, Xing Tang, Ziqiang Cui, Zexu Sun, Liang Chen, Xiuqiang He, and Chen Ma. Rankability-
enhanced revenue uplift modeling framework for online marketing. In Proceedings of the 30th ACM SIGKDD
Conference on Knowledge Discovery and Data Mining, pages 5093–5104, 2024.
Wei Sun, Pengyuan Wang, Dawei Yin, Jian Yang, and Yi Chang. Causal inference via sparse additive models with
application to online advertising. In Proceedings of the AAAI conference on artificial intelligence, volume 29, 2015.
Dugang Liu, Xing Tang, Han Gao, Fuyuan Lyu, and Xiuqiang He. Explicit feature interaction-aware uplift network for
online marketing. In Proceedings of the 29th ACM SIGKDD Conference on Knowledge Discovery and Data Mining,
pages 4507–4515, 2023.
JM Smit, Jesse H Krijthe, WMR Kant, JA Labrecque, M Komorowski, DAMPJ Gommers, Jasper van Bommel,
Marcel JT Reinders, and Michel E van Genderen. Causal inference using observational intensive care unit data: a
scoping review and recommendations for future practice. npj Digital Medicine, 6(1):221, 2023.
Taiki Sato, Yohei Sotomi, Shungo Hikoso, Tetsuhisa Kitamura, Daisaku Nakatani, Katsuki Okada, Tomoharu Dohi,
Akihiro Sunaga, Hirota Kida, Yuki Matsuoka, et al. Uplift modeling to identify patients who require extensive
catheter ablation procedures among patients with persistent atrial fibrillation. Scientific Reports, 14(1):2634, 2024.
Werner Kristjanpoller, Kevin Michell, Cristian Llanos, and Marcel C Minutolo. Incorporating causal notions to
forecasting time series: a case study. Financial Innovation, 11(1):15, 2025.
Satyam Kumar, Yelleti Vivek, Vadlamani Ravi, and Indranil Bose. Causal inference for banking finance and insurance a
survey. arXiv preprint arXiv:2307.16427, 2023.
15

The Estimation of Continual Causal Effect for Dataset Shifting Streams
Vijay K Vemuri. Causal inference for statistics, social, and biomedical sciences: an introduction by guido w. imbens and
donald b. rubin: New york, ny: Cambridge university press, 2015, isbn 978-0521885881, 644 pages, 60(hardcover),
48 (ebook), 33.49(kindleedition), 2015.
Peter C Austin. An introduction to propensity score methods for reducing the effects of confounding in observational
studies. Multivariate behavioral research, 46(3):399–424, 2011.
Léon Bottou, Jonas Peters, Joaquin Quiñonero-Candela, Denis X Charles, D Max Chickering, Elon Portugaly, Dipankar
Ray, Patrice Simard, and Ed Snelson. Counterfactual reasoning and learning systems: The example of computational
advertising. Journal of Machine Learning Research, 14(11), 2013.
José R Zubizarreta. Stable weights that balance covariates for estimation with incomplete outcome data. Journal of the
American Statistical Association, 110(511):910–922, 2015.
Negar Hassanpour and Russell Greiner. Counterfactual regression with importance sampling weights. In IJCAI, pages
5880–5887. Macao, 2019a.
Yoshua Bengio, Aaron Courville, and Pascal Vincent. Representation learning: A review and new perspectives. IEEE
transactions on pattern analysis and machine intelligence, 35(8):1798–1828, 2013.
Uri Shalit, Fredrik D Johansson, and David Sontag. Estimating individual treatment effect: generalization bounds and
algorithms. In International conference on machine learning, pages 3076–3085. PMLR, 2017.
Anpeng Wu, Junkun Yuan, Kun Kuang, Bo Li, Runze Wu, Qiang Zhu, Yueting Zhuang, and Fei Wu. Learning
decomposed representations for treatment effect estimation. IEEE Transactions on Knowledge and Data Engineering,
35(5):4989–5001, 2022.
Zhixuan Chu, Ruopeng Li, Stephen Rathbun, and Sheng Li. Continual causal inference with incremental observational
data. In 2023 IEEE 39th International Conference on Data Engineering (ICDE), pages 3430–3439. IEEE, 2023.
Nimisha G Nair, Pallavi Satpathy, Jabez Christopher, et al. Covariate shift: A review and analysis on classifiers. In
2019 Global Conference for Advancement in Technology (GCAT), pages 1–6. IEEE, 2019.
Meelis Kull and Peter Flach. Patterns of dataset shift. In First international workshop on learning over multiple contexts
(LMCE) at ECML-PKDD, volume 5, 2014.
Negar Hassanpour and Russell Greiner. Learning disentangled representations for counterfactual regression. In
International Conference on Learning Representations, 2019b.
Gido M Van de Ven, Tinne Tuytelaars, and Andreas S Tolias. Three types of incremental learning.Nature Machine
Intelligence, 4(12):1185–1197, 2022.
Eden Belouadah, Adrian Popescu, and Ioannis Kanellos. A comprehensive study of class incremental learning
algorithms for visual tasks. Neural Networks, 135:38–54, 2021.
Zhizhong Li and Derek Hoiem. Learning without forgetting. IEEE transactions on pattern analysis and machine
intelligence, 40(12):2935–2947, 2017.
Sylvestre-Alvise Rebuffi, Alexander Kolesnikov, Georg Sperl, and Christoph H Lampert. icarl: Incremental classifier
and representation learning. In Proceedings of the IEEE conference on Computer Vision and Pattern Recognition,
pages 2001–2010, 2017.
Rongzhi Zhang, Jiaming Shen, Tianqi Liu, Jialu Liu, Michael Bendersky, Marc Najork, and Chao Zhang. Knowledge
distillation with perturbed loss: From a vanilla teacher to a proxy teacher. In Proceedings of the 30th ACM SIGKDD
Conference on Knowledge Discovery and Data Mining, pages 4278–4289, 2024.
Victor SY Lo. The true lift model: a novel data mining approach to response modeling in database marketing. ACM
SIGKDD Explorations Newsletter, 4(2):78–86, 2002.
Sören R Künzel, Jasjeet S Sekhon, Peter J Bickel, and Bin Yu. Metalearners for estimating heterogeneous treatment
effects using machine learning. Proceedings of the national academy of sciences, 116(10):4156–4165, 2019.
Hugh A Chipman, Edward I George, and Robert E McCulloch. Bart: Bayesian additive regression trees. The Annals of
Applied Statistics, 4(1):266–298, 2010.
Stefan Wager and Susan Athey. Estimation and inference of heterogeneous treatment effects using random forests.
Journal of the American Statistical Association, 113(523):1228–1242, 2018.
Fredrik Johansson, Uri Shalit, and David Sontag. Learning representations for counterfactual inference. In International
conference on machine learning, pages 3020–3029. PMLR, 2016.
Claudia Shi, David Blei, and Victor Veitch. Adapting neural networks for the estimation of treatment effects. Advances
in neural information processing systems, 32, 2019.
16

The Estimation of Continual Causal Effect for Dataset Shifting Streams
Kailiang Zhong, Fengtong Xiao, Yan Ren, Yaorong Liang, Wenqing Yao, Xiaofeng Yang, and Ling Cen. Descn: Deep
entire space cross networks for individual treatment effect estimation. In Proceedings of the 28th ACM SIGKDD
Conference on Knowledge Discovery and Data Mining, pages 4612–4620, 2022.
Jennifer L Hill. Bayesian nonparametric modeling for causal inference. Journal of Computational and Graphical
Statistics, 20(1):217–240, 2011.
Floris Devriendt, Jente Van Belle, Tias Guns, and Wouter Verbeke. Learning to rank for uplift modeling. IEEE
Transactions on Knowledge and Data Engineering, 34(10):4888–4904, 2020.
Shuyang Du, James Lee, and Farzin Ghaffarizadeh. Improve user retention with causal learning. In The 2019 ACM
SIGKDD Workshop on Causal Discovery, pages 34–49. PMLR, 2019.
Hao Zhou, Shaoming Li, Guibin Jiang, Jiaqi Zheng, and Dong Wang. Direct heterogeneous causal learning for resource
allocation problems in marketing. In Proceedings of the AAAI Conference on Artificial Intelligence , volume 37,
pages 5446–5454, 2023.
Matthias De Lange, Rahaf Aljundi, Marc Masana, Sarah Parisot, Xu Jia, Ales Leonardis, Gregory Slabaugh, and Tinne
Tuytelaars. Continual learning: A comparative study on how to defy forgetting in classification tasks. arXiv preprint
arXiv:1909.08383, 2(6):2, 2019.
Nicolas Y Masse, Gregory D Grant, and David J Freedman. Alleviating catastrophic forgetting using context-dependent
gating and synaptic stabilization. Proceedings of the National Academy of Sciences, 115(44):E10467–E10475, 2018.
Joan Serra, Didac Suris, Marius Miron, and Alexandros Karatzoglou. Overcoming catastrophic forgetting with hard
attention to the task. In International conference on machine learning, pages 4548–4557. PMLR, 2018.
James Kirkpatrick, Razvan Pascanu, Neil Rabinowitz, Joel Veness, Guillaume Desjardins, Andrei A Rusu, Kieran
Milan, John Quan, Tiago Ramalho, Agnieszka Grabska-Barwinska, et al. Overcoming catastrophic forgetting in
neural networks. Proceedings of the national academy of sciences, 114(13):3521–3526, 2017.
Friedemann Zenke, Ben Poole, and Surya Ganguli. Continual learning through synaptic intelligence. In International
conference on machine learning, pages 3987–3995. PMLR, 2017.
Arslan Chaudhry, Marc’Aurelio Ranzato, Marcus Rohrbach, and Mohamed Elhoseiny. Efficient lifelong learning with
a-gem. arXiv preprint arXiv:1812.00420, 2018.
Jianping Gou, Baosheng Yu, Stephen J Maybank, and Dacheng Tao. Knowledge distillation: A survey. International
Journal of Computer Vision, 129(6):1789–1819, 2021.
Christian Szegedy, Vincent Vanhoucke, Sergey Ioffe, Jon Shlens, and Zbigniew Wojna. Rethinking the inception
architecture for computer vision. In Proceedings of the IEEE conference on computer vision and pattern recognition,
pages 2818–2826, 2016.
Geoffrey Hinton. Distilling the knowledge in a neural network. arXiv preprint arXiv:1503.02531, 2015.
T Lin. Focal loss for dense object detection. arXiv preprint arXiv:1708.02002, 2017.
Paul R Rosenbaum and Donald B Rubin. The central role of the propensity score in observational studies for causal
effects. Biometrika, 70(1):41–55, 1983.
Jeroen Berrevoets and Wouter Verbeke. Causal simulations for uplift modeling. arXiv preprint arXiv:1902.00287,
2019.
17
