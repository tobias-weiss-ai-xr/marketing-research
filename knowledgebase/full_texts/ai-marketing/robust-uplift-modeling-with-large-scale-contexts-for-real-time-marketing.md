---
title: Robust Uplift Modeling with Large-Scale Contexts for Real-time Marketing
url: https://arxiv.org/abs/2502.15697
category: ai-marketing
subcategory: empirical
date: 2025-01
venue: ''
authors:
- Zexu Sun
- Qiyu Han
- Minqin Zhu
- Hao Gong
- Dugang Liu
source: arxiv
pdf_url: https://arxiv.org/pdf/2502.15697
pages: 15
chars: 71473
fetched_at: '2026-11-08T13:13:06+00:00'
kb_version: 1
---

# Robust Uplift Modeling with Large-Scale Contexts for Real-time Marketing

Robust Uplift Modeling with Large-Scale Contexts for
Real-time Marketing
Zexu Sun
Gaoling School of Artificial
Intelligence, Renmin University of
China
Beijing, China
sunzexu21@ruc.edu.cn
Qiyu Han
School of Statistics, Renmin
University of China
Beijing, China
hanqiyu@ruc.edu.cn
Minqin Zhu
Department of Computer Science and
Technology, Zhejiang University
Hangzhou, China
minqinzhu@zju.edu.cn
Hao Gong
Kuaishou Technology
Beijing, China
gong_h@mail.nwpu.edu.cn
Dugang Liu∗
College of Computer Science and
Software Engineering, Shenzhen
University
Shenzhen, China
dugang.ldg@gmail.com
Chen Ma∗
Department of Computer Science,
City University of Hong Kong
Hong Kong SAR
chenma@cityu.edu.hk
ABSTRACT
Improving user engagement and platform revenue is crucial for
online marketing platforms. Uplift modeling is proposed to solve
this problem, which applies different treatments (e.g., discounts,
bonus) to satisfy corresponding users. Despite progress in this field,
limitations persist. Firstly, most of them focus on scenarios where
only user features exist. However, in real-world scenarios, there
are rich contexts available in the online platform (e.g., short videos,
news), and the uplift model needs to infer an incentive for each
user on the specific item, which is called real-time marketing. Thus,
only considering the user features will lead to biased prediction
of the responses, which may cause the cumulative error for uplift
prediction. Moreover, due to the large-scale contexts, directly con-
catenating the context features with the user features will cause
a severe distribution shift in the treatment and control groups.
Secondly, capturing the interaction relationship between the user
features and context features can better predict the user response.
To solve the above limitations, we propose a novel model-agnostic
Robust Uplift Modeling with Large-Scale Contexts (UMLC) frame-
work for Real-time Marketing. Our UMLC includes two customized
modules. 1) A response-guided context grouping module for ex-
tracting context features information and condensing value space
through clusters. 2) A feature interaction module for obtaining bet-
ter uplift prediction. Specifically, this module contains two parts:
a user-context interaction component for better modeling the re-
sponse; a treatment-feature interaction component for discovering
∗Corresponding Authors
Permission to make digital or hard copies of all or part of this work for personal or
classroom use is granted without fee provided that copies are not made or distributed
for profit or commercial advantage and that copies bear this notice and the full citation
on the first page. Copyrights for components of this work owned by others than the
author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or
republish, to post on servers or to redistribute to lists, requires prior specific permission
and/or a fee. Request permissions from permissions@acm.org.
KDD ’25, August 3–7, 2025, Toronto, ON, Canada
© 2025 Copyright held by the owner/author(s). Publication rights licensed to ACM.
ACM ISBN 979-8-4007-1245-6/25/08. . . $15.00
https://doi.org/10.1145/3690624.3709293
the treatment assignment sensitive feature of each instance to bet-
ter predict the uplift. Moreover, we conduct extensive experiments
on a synthetic dataset and a real-world product dataset to verify
the effectiveness and compatibility of our UMLC.
CCS CONCEPTS
• Information systems; • Online marketing;
KEYWORDS
Uplift modeling, Large-scale contexts, Real-time marketing
ACM Reference Format:
Zexu Sun, Qiyu Han, Minqin Zhu, Hao Gong, Dugang Liu, and Chen Ma.
2025. Robust Uplift Modeling with Large-Scale Contexts for Real-time Mar-
keting. In Proceedings of the 31st ACM SIGKDD Conference on Knowledge Dis-
covery and Data Mining V.1 (KDD ’25), August 3–7, 2025, Toronto, ON, Canada.
ACM, New York, NY, USA, 15 pages. https://doi.org/10.1145/3690624.3709293
1 INTRODUCTION
With the development of online platforms, assigning specific incen-
tives to increase user engagement and platform revenue is a crucial
task in online marketing [18, 34]. Since these incentives (e.g., bonus,
discount) are usually related to the cost, different users may have
different responses to these incentives. Then, a successful strategy
is needed to discover the incentive-sensitive user group and only
deliver the incentive to the user that tends to be converted, which
is important in online platforms. In recent years, uplift modeling,
where various treatments are applied for different target users, has
been proposed to achieve this purpose. In practice, we can observe
only one type of user response, which may be for a certain incentive
(i.e., treatment group) or no incentive (i.e., control group) [10]. Up-
lift modeling aims to capture the differences between the treatment
and control groups, which is known as the individual treatment
effect (ITE) or uplift. Many uplift models have been proposed to
facilitate online marketing of online platforms [39].
The existing works can be divided into two directions. 1)Machine-
learning based methods . In detail, these works can be further di-
vided into meta-learner-based and tree-based. S-Learner [17] and
1
arXiv:2502.15697v1  [cs.IR]  4 Jan 2025

KDD ’25, August 3–7, 2025, Toronto, ON, Canada Zexu Sun, et al.
T-Learner [17] are the representative meta-learner methods, which
design a global base learner or two base learners for the samples
in treatment and control groups, respectively. Uplift Tree [ 30]
and Causal Forest [ 2] are two commonly used tree-based meth-
ods. Specifically, the hierarchical tree is used to separate user pop-
ulations into subgroups that exhibit sensitivity to specific treat-
ments [27]. 2) Representation-learning based methods. With the de-
velopment of deep learning, the representation learning becomes
the main research direction for uplift prediction [25]. TARNet [31]
and CFRNet [31] leverage a feature representation network to ex-
tract the feature information into the latent space, then to predict
the responses in different user groups ( i.e., treatment group and
control group) and achieve representation balancing by using the
Integral Probability Metrics (IPM). StableCFR [ 37] smooths the
population distribution and upsample the underrepresented sub-
populations, while balancing distributions between treatment and
control groups. [21] designs a unified framework for both one-side
and two-side online marketing. We focus on the representation-
learning based methods because they can be more flexibly adapted
to modeling the complex scenarios in many industrial systems.
Although existing methods of uplift modeling have shown promis-
ing results and achieved success in many practical problems, they
generally only consider the existence of user features and do not
model the rich context features. In some real-world scenarios, to
better find the users that tend to convert in online platforms, we
need to assign different treatments to users with different contexts.
For example, on short video platforms, the users may receive dif-
ferent coin incentives with different recommended short videos.
We define this problem as real-time marketing. There are some
challenges for solving the uplift problem in real-time marketing:
1) Distribution shift: Random Control Trials (RCTs) are commonly
used to collect data from the online platform for training the uplift
models, which aim to ensure uniform distribution of user features
between treatment and control groups. However, as shown in Fig-
ure 1, when considering the large-scale context features, directly
concatenating the uncontrollable context features (e.g., short videos)
will cause a significant distribution shift between the treatment
and control groups. 2) Feature interaction: Modeling the feature
interaction [33, 36] can improve the prediction accuracy of the
model. However, it is not sufficiently explored in previous uplift
modeling works [2, 3]. With rich context features, discovering the
relationships between the user features and context features, or
the treatment assignment and the features, is essential for better
predicting the uplift.
In this paper, to solve the aforementioned challenges, we pro-
pose a novel model-agnostic Robust Uplift Modeling with Large-
Scale Contexts (UMLC) framework for Real-time Marketing. In
particular, our framework consists of two customized modules. 1)
A response-guided context grouping module aims to extract con-
text features information through a response-guided regression
network, and narrow the value space of context features by the
cluster; 2) A feature interaction module contains a user-context and
a treatment-feature interaction parts can better capture the rela-
tionship between the user features and context features, which may
obtain more reliable user response prediction; a treatment-feature
interaction module aims to discover the treatment assignment sen-
sitive features (i.e., the features have a potential relationship with
treatment sample
(a) standard RCT (b) with contexts
control sample
Figure 1: An example of distributions of standard RCTs and
the RCTs considering the contexts. When considering the
uncontrollable contexts in standard RCTs, there may be the
significant distribution shift between the treatment and con-
trol groups.
treatment assignment) of each instance to target the users that
tend to convert with the specific context features. Moreover, our
contributions can be summarized as follows:
• We propose a novel model-agnostic UMLC framework for
solving the uplift problem in real-time marketing.
• We design a response-guided context grouping module, which
handles the large-scale context with a distribution shift be-
tween the treatment and control groups.
• We also design a feature interaction module, which builds
the relationships between the user and context or treatment
assignment and features for better uplift prediction.
• We conduct extensive experiments on a synthetic dataset and
a product dataset to verify the effectiveness and compatibility
of our UMLC.
2 RELATED WORK
2.1 Real-time Marketing
Real-time marketing appears as a result of consumers’ expectation
for real-time connection with product or service providers [6]. Real-
time service has taken personalization of service beyond merely
providing relevant content to targeted consumers. For example,
consumers’ personal preferences combined with external factors
such as weather, traffic or season could inform context information
needed to co-create value in real-time [5]. With the development of
online marketing, more and more platforms need to design effective
strategy for incentivize sensitive users, including E-commerce com-
panies like Taobao, rental service like Airbnb, short video recom-
mendation like Kuaishou. The above mentioned platforms involve
both user and rich contexts. To further better utilize the incentives,
a possible marketing strategy is to assign different incentives for
each user with different contexts, which is defined as the real-time
online marketing. Recent works [15, 19, 22] in real-time marketing
2

Robust Uplift Modeling with Large-Scale Contexts for
Real-time Marketing KDD ’25, August 3–7, 2025, Toronto, ON, Canada
focus on the pricing for different contexts, the product management
or the optimization procedure for bidding. However, for the online
platforms, the aim of real-time online marketing is to delivery dif-
ferent incentives for each user with different contexts, which is not
investigated in the previous works.
2.2 Uplift Modeling
The uplift modeling methods mainly focus on two research direc-
tions: 1) Machine-learning based methods . The machine-learning
based methods can be divided into two more detailed research
categories, i.e., meta-learner based and tree-based. Meta-learner
based methods aim to use any off-the-shelf estimator as the base
learner for the uplift prediction. S-Learner [17] and T-Learner [17]
leverage one global or two base learners for treatment and con-
trol groups, respectively. Tree-based methods aim to design the
splitting criteria or use the ensemble methods to predict the uplift.
Causal Forest [2] uses the ensemble of uplift trees, and returns the
average uplift prediction of them. 2) Representation-learning based
methods. Representation-learning based methods are more flexible
than machine-learning based methods. CFRNet [31] use a shared
bottom to extract features into latent space, and obtain the balanced
representation through IPM. SITE [38] preserves local similarity
and balances data distributions simultaneously, by focusing on
several hard samples in each mini-batch. StableCFR [37] smooths
the population distribution and upsample the underrepresented
subpopulations. There are also some works focus on the specific sce-
nario or the generalization ability of the uplift models. UniTE [21]
proposes a uniform framework for one-side and two-side online
marketing. RUAD [34] defines a robustness case of uplift modeling
and uses the adversarial training to solve it. However, these works
only model the uplift of the users, without considering the effect of
contexts.
3 PRELIMINARIES
To formulate the problem, we follow the Neyman-Rubin potential
outcome framework [28], to define the uplift modeling problem. Let
the observed sample set beD ={𝒙𝑢 𝑖, 𝒙𝑐 𝑖,𝑡𝑖,𝑦𝑖}𝑛 𝑖=1 with𝑛 samples.
Without loss of generality, for each sample, assuming𝑦𝑖∈Y⊂ R
is a continuous response variable, 𝒙𝑢 𝑖 ∈X 𝑢 ⊂ R𝑝 is a vector of
user features with𝑝 elements, 𝒙𝑐 𝑖∈X 𝑐⊂ R𝑞 is a vector of context
features with 𝑞 elements, and 𝑡𝑖 ∈ {0, 1} denotes the treatment
indicator variable, i.e., whether to get an incentive delivery. Note
that the proposed framework can be easily extended to other types
of uplift modeling problems. For user𝑖, the change in user response
caused by an incentive𝑡𝑖, i.e., individual treatment effect or uplift,
denoted as𝜏𝑖, is defined as the difference between the treatment
response and the control response:
𝜏𝑖 =𝑦𝑖(1)− 𝑦𝑖(0), (1)
where𝑦𝑖(0) and𝑦𝑖(1) are the user responses of the control and
treatment groups, respectively.
In the ideal world, i.e., obtaining the responses of a user in both
groups simultaneously, we can easily determine the uplift𝜏𝑖 based
on Eq. (1). However, in the real world, only one of the two responses
is observed for any one user. For example, if we have observed the
response of a customer who receives the discount, it is impossible
to observe the response of the same customer when they do not
receive a discount, where such responses are often referred to as
counterfactual responses. Therefore, the observed response can be
described as:
𝑦𝑖 =𝑡𝑖𝑦𝑖(1)+( 1−𝑡𝑖)𝑦𝑖(0). (2)
For the brevity of notation, we will omit the subscript 𝑖 in the
following if no ambiguity arises.
As mentioned above, the uplift 𝜏 is not identifiable since the
observed response𝑦 is only one of the two necessary terms (i.e.,𝑦(1)
and𝑦(0)). Fortunately, with some appropriate assumptions [ 18],
we can use the conditional average treatment effect (CATE) as an
estimator for the uplift, where CATE is defined as:
𝜏(𝒙) = E(𝑌(1)| 𝑿 = 𝒙)− E(𝑌(0)| 𝑿 = 𝒙)
= E(𝑌|𝑇 = 1, 𝑿 = 𝒙)
|                   {z                   }
𝜇1(𝒙)
− E(𝑌|𝑇 = 0, 𝑿 = 𝒙)
|                   {z                   }
𝜇0(𝒙)
. (3)
where 𝒙 =[𝒙𝑢, 𝒙𝑐] is the features of an instance,[·,·] represents the
concatenation. Intuitively, the desired objective can be described as
the difference between two conditional means𝜏(𝒙) =𝜇1(𝒙)−𝜇0(𝒙).
4 METHODOLOGY
Our UMLC consists of two customized modules: the response-
guided context grouping module and a feature interaction module.
The whole structure of our UMLC is shown in Figure 2, and we
introduce the two modules as follows.
4.1 Response-guided Context Grouping
4.1.1 Motivation. As mentioned in Section 1, when considering the
large-scale contexts, there is a distribution shift between treatment
and control groups, which may introduce bias for uplift prediction.
In recent years, there have been works focusing on solving the
treatment assignment bias between the user groups to obtain the
unbiased treatment effect [31, 37, 38]. The core ideas of these works
are to learn a balanced representation in the latent space from a
distribution perspective [31], or match the samples in the treatment
and control groups from a sample perspective [38].
However, in our problem setting, the above-mentioned methods
that ignore the specific influence of the contexts may be unreliable.
For example, in real-world scenarios, each user can be associated
with many contexts, such as a user may view many short videos a
day, resulting in numerous instances. Therefore, directly concate-
nating the context features with user features may encounter the
issue of variance inflation: similar context features may preserve
many different labels, leading to unreliable predictions.
To address the issue, we propose to consolidate contexts into
discrete groups, and then use these groups as proxy contexts to
enhance uplift prediction. Employing this strategy has the poten-
tial to reduce variance, but if the contexts in the same group are
completely different, it may also introduce additional bias into the
prediction of uplift [26]. Fortunately, if the merged contexts within
the same group have a similar impact on the response, the resulting
bias can be effectively mitigated.
4.1.2 Analysis. For each context 𝒙𝑐∈X 𝑐, we define a correspond-
ing group variable 𝒈∈{ 0, 1, 2,...,𝐾 − 1} denoting the group that
3

KDD ’25, August 3–7, 2025, Toronto, ON, Canada Zexu Sun, et al.
Cluster
Relabel
Lipschtiz
Count
Co-Attention
0.3
0.5
0.2
Embedding
Control
Response
Uplift
Prediction
Aggregation
User-Context Interaction
Treatment-Feature Interaction
 1    1
Response-guided Context Grouping
Cross Attention
 0     0
Cross Attention
Softmax
Feature Interaction
Base Uplift Model
Figure 2: The overall structure of our UMLC framework. The left is the response-guided context grouping module, the right is
the feature interaction module.
the contexts are clustered into. Therefore, regarding the group vari-
able 𝒈 as a one-hot vector, we can define the conditional distribution
on the group variable given context as𝑝(𝒈| 𝒙𝑐). To support our
method, we have the following assumptions.
Assumption 1. We assume the response generation is of the form
𝑦 =ℎ(𝒙𝑢, 𝒙𝑐,𝑡)+ 𝜖 [14], where|ℎ(𝒙𝑢, 𝒙𝑐,𝑡)|≤ 𝐵ℎ and𝜖 is a noise
term with zero mean. We also assume the contexts merged into one
group have a similar effect on the response. It means that for arbitrary
context pair(𝒙𝑐 𝑖, 𝒙𝑐 𝑗) satisfying P  𝒈|𝒙𝑐 𝑖  = P  𝒈|𝒙𝑐 𝑗  , we have

E  𝑦|𝒙𝑢, 𝒙𝑐 𝑖,𝑡  − E h 𝑦|𝒙𝑢, 𝒙𝑐 𝑗,𝑡 i

≤𝛿,∀𝒙𝑢,𝑡,𝑖 ≠ 𝑗, (4)
where|·| denotes absolute value operation,𝐵ℎ and𝛿 are two constants,
and𝛿 is less than 𝐵ℎ.
With the above assumption, we attempt to depict the distance
of functionℎ between different contexts and merge the contexts
with small distances into groups. Given that the function spaceℎ
is of infinite dimension, it is impractical to compute the distance
within the original function space. Then, we propose a method
that involves transforming the resultant function ℎ into a finite-
dimensional embedding, allowing for distance calculations within
the projected space. To realize this strategy, we first give the fol-
lowing assumption.
Assumption 2. There exists a transformation function𝜉 which sat-
isfies∀𝒙𝑢,𝑡,𝑖 ≠ 𝑗

ℎ  𝒙𝑢, 𝒙𝑐 𝑖,𝑡  −ℎ  𝒙𝑢, 𝒙𝑐 𝑗,𝑡 

≤𝜁· 𝜉  𝒙𝑐 𝑖  −𝜉  𝒙𝑐 𝑗 2
+𝜂,𝜁,𝜂 are two constants,∥·∥ 2 denotes the Euclidean distances [9].
If a transformation𝜉 is found to meet Assumption 2 with a small
value𝜂, then it is possible to perform clustering on the context
embedding𝜉(𝒙𝑐) using the Euclidean distance. Through this pro-
cess, the maximum distance between embeddings within a cluster
can be effectively controlled to a small constant𝜅. Regarding the
clusters as the context groups, the distance of regression function
𝛿≤𝜁·𝜅+𝜂 is also small. Then we have the following proposition
to find such a transformation function.
Proposition 1. If we can find a predictive function 𝑓 and trans-
formation function𝜉 with Lipschitz constraints on contexts such that
|ℎ(𝒙𝑢, 𝒙𝑐,𝑡)−𝑓(𝒙𝑢,𝜉(𝒙𝑐),𝑡)|≤ 𝜇,∀𝒙𝑢, 𝒙𝑐,𝑡 and

𝑓  𝒙𝑢,𝜉(𝒙𝑐 𝑖),𝑡 
−𝑓

𝒙𝑢,𝜉(𝒙𝑐 𝑗),𝑡 

≤𝑐· 𝜉(𝒙𝑐 𝑖)− 𝜉(𝒙𝑐 𝑗) 2 ,∀𝒙𝑢, 𝒙𝑐 𝑖, 𝒙𝑐 𝑗,𝑡,𝑖 ≠ 𝑗. Then
the function𝜉 satisfies the Assumption 2 with 𝜁 =𝑐,𝜂 = 2𝜇.
We provide the proof in Appendix A.
Inspired by the Proposition 1, to train the context embedding to
be clustered, we aim to learn the transformation𝜉 and a Lipschitz
regularized regressor𝑓 with small predictive error (i.e., small𝜇).
4.1.3 Procedure. We use the categorical and numerical embed-
dings [13] for the context features, and we construct the regression
model as𝑓 in Proposition 1 which predicts the response based on
the user features, context features, and treatment with Lipschitz
regularization.
Response Prediction. We denote𝜉𝜃(𝒙𝑐) as the concatenation of
the categorical and numerical embeddings [13] for context feature
embeddings,𝜃 is the learnable parameters. To ensure that the ac-
quired embeddings𝜉𝜃(𝑥𝑐) accurately capture the context effects
on the responses and the distance between them, we concatenate
the representation𝜉𝜃(𝑥𝑐) with the user features and the treatment.
This concatenation is then fed into the regression model𝑓 to make
predictions of the response. The prediction loss for the response-
guided regression is defined as:
Lpred =L 𝑓 𝒙𝑢,𝜉𝜃(𝒙𝑐),𝑡 ,𝑦, (5)
whereL(·,·) is the mean square error loss.
Lipschitz Regularization. To ensure a consistent representation
of the relationship of the contexts in the embedding space, we em-
ploy Lipschitz regularization. This regularization guarantees that
the function𝑓 is Lipschitz continuous, meaning that the distance in
4

Robust Uplift Modeling with Large-Scale Contexts for
Real-time Marketing KDD ’25, August 3–7, 2025, Toronto, ON, Canada
the embedding space accurately reflects the context effects. To sat-
isfy Lipschitz continuity, there must exist a non-negative constant
𝑐 for∀𝑖,𝑗,𝑖 ≠ 𝑗 such that:

𝑓(𝒛𝑖)−𝑓 𝒛𝑗 

≤𝑐 𝒛𝑖− 𝒛𝑗 2, (6)
where 𝒛𝑖 =

𝒙𝑢 𝑖,𝜉(𝒙𝑐 𝑖),𝑡𝑖

is the concatenation of the user fea-
tures, the context embedding and the treatment, and intuitively,
the change of response is bounded by constant𝑐 for smoothness. It
is evident that if the function𝑓 is𝑐-Lipschitz on the input 𝒛, then
it is also𝑐-Lipschitz on the context embedding𝜉(𝒙𝑐).
We utilize Lipschitz Regularization [20], a technique that relies
solely on the weight matrices of each network layer, with an esti-
mated per-layer Lipschitz upper bound denoted as𝑐𝑖. The purpose
of this regularization is to constrain the discrepancies between con-
text effects and responses. The corresponding loss function can be
defined as follows:
LLip =
𝑙Ö
𝑖=1
softplus(𝑐𝑖), (7)
where softplus(𝑐𝑖) = ln(1+𝑒𝑐𝑖) is a reparameterization strategy
to avoid invalid negative estimation on Lipschitz constant,𝑐𝑖 and𝑙
is the number of network layers.
Then we can obtain the final loss function for training the
response-guided context embedding:
Lreg =Lpred+𝛼Llip. (8)
where𝛼 is the hyper-parameter to control the trade-off of aligning
the difference between the context embedding and the response.
Following the previous work [ 20], the value of 𝛼 is stated to be
minimal, thus, we set it to be 10−4 in all experiments.
Grouping and Aggregation. After we get the trained context
embedding, grouping it is important for the data dimensionality
reduction and volatility minimization. We determine the number
of groups by setting a hyperparameter 𝐾, and utilize clustering
algorithms like K-means to allocate each context embedding𝜉𝜃(𝒙𝑐)
to a specific group 𝒈. The clustering mappingF , which assigns
embeddings to groups, is formalized as:F :𝜉𝜃(𝒙𝑐)↦→ 𝒈.
Moreover, to enhance the stability and accuracy of uplift model
training and prediction aggregating data with the same features is
necessary. Specially, for any two samples(𝒙𝑢 𝑖, 𝒈𝑖,𝑡𝑖,𝑦𝑖) and(𝒙𝑢 𝑗, 𝒈𝑗,
𝑡𝑗,𝑦𝑗),𝑖 ≠ 𝑗, if they have the same treatment, user features and
context group, we aggregate them into a new sample as:
𝑦 = 𝑦𝑖+𝑦𝑗
2 , ∀𝒙𝑢 𝑖 = 𝒙𝑢 𝑗, 𝒈𝑖 = 𝒈𝑗,𝑡𝑖 =𝑡𝑗. (9)
Then, we can get the relabeled datasetD𝑟 ={𝒙𝑢 𝑖, 𝒈𝑖,𝑡𝑖,𝑦}𝑚 𝑖=1 with
𝑚 samples for subsequent uplift prediction.
4.2 Feature Interaction
The second problem we need to solve is the feature interaction in
uplift prediction. Feature interaction is designed to model combi-
nations between different features and have been shown to signifi-
cantly improve the performance of a response model [7]. To obtain
better uplift prediction, we mainly focus on the user-context in-
teraction and treatment-feature interaction, we detailed introduce
them in the following.
4.2.1 User-Context Interaction. In real time marketing, when con-
sidering the context (i.e., short videos), the context information can
influence the user behavior. Recent state-of-the-art methods [12, 18]
represent the relationships between users and contexts using a ten-
sor. However, utilizing a tensor makes it challenging to differentiate
the effects of various context factors and to model the non-linear
interactions between users and contexts. In this part, we use the
user feature embedding 𝒆𝑢 and the grouped context embedding 𝒆𝑐
to model the user response. We adapt a parallel co-attention net-
work [23] for the user-context interaction to get better prediction
results, the first step is to compute the affinity matrix:
𝑳 = tanh

𝒆𝑇 𝑢· 𝑾𝐿· 𝒆𝑐

, (10)
where 𝑾𝐿 is the weight parameters. After computing this affinity
matrix, the parallel co-attention network considers this affinity
matrix as a feature and learns to predict user and context attention
maps via the following:
𝑯𝑢 =tanh(𝑾𝑢· 𝒆𝑢+(𝑾𝑐· 𝒆𝑐)· 𝑳),
𝑯𝑐 =tanh

𝑾𝑐· 𝒆𝑐+(𝑾𝑢· 𝒆𝑢)· 𝑳𝑇

. (11)
where 𝑾𝑢 and 𝑾𝑐 are the weight parameters. The affinity ma-
trix 𝑳 transform the context attention space to the user attention
space (vice versa for 𝑳𝑇 ). Next, we can get the normalized attention
weights for the user and context embeddings:
𝒂𝑢 = softmax

𝑾𝑇 ℎ𝑢· 𝑯𝑢

, 𝒂𝑐 = softmax

𝑾𝑇 ℎ𝑐· 𝑯𝑐

, (12)
where 𝑾ℎ𝑢 and 𝑾ℎ𝑐 are the weight parameters, 𝒂𝑢 and 𝒂𝑐 are the
attention parameters for the user and context, respectively. Based
on the above attention weights, the user and context attention
vectors are calculated in the following:
ˆ𝒆𝑢 = 𝒂𝑢∗ 𝒆𝑢, ˆ𝒆𝑐 = 𝒂𝑐∗ 𝒆𝑐, (13)
where∗ denotes the sum of the product for each element in the
embedding with the attention vector. Then, we use a multilayer
perceptron (MLP) to predict control responses:
𝜇0 = MLP(ˆ𝒆𝑢, ˆ𝒆𝑐). (14)
4.2.2 Treatment-Feature Interaction. Considering the treatment
assignment sensitive features in the concatenation of the user fea-
tures and context features, we introduce a cross attention based
treatment-feature interaction part to discover the information gain [35]
introduced by the treatment assignment.
Specially, we denote the concatenation of ˆ𝒆𝑢 and ˆ𝒆𝑐 as ˆ𝒆𝑓 , the
embedding of treatment as 𝒆𝑡 . The we can get the attention weights
of the feature embedding as follows:
𝒂𝑡 = softmax
'››
«
(𝑾𝑡· 𝒆𝑡)·

𝑾𝑓· ˆ𝒆𝑓
𝑇
√︁
𝐾𝑑
“ﬁﬁ
‹
, (15)
where 𝑾𝑡 and 𝑾𝑓 are the weight parameters,𝐾𝑑 is the dimension
of the output embedding. Then, to simulate the treatment variation,
we can obtain the 𝒂0 𝑡 and 𝒂1 𝑡 with different treatment embeddings
𝒆0 𝑡 (i.e.,𝑡 = 0) and 𝒆1 𝑡 (i.e.,𝑡 = 1), respectively. The information gain
on the feature embedding introduced by the treatment assignment
can be formulated as:
ˆ𝒆Δ = 𝒂1 𝑡∗ ˆ𝒆𝑓− 𝒂0 𝑡∗ ˆ𝒆𝑓, (16)
5

KDD ’25, August 3–7, 2025, Toronto, ON, Canada Zexu Sun, et al.
to better optimize the cross attention structure to find treatment
the sensitive features, we aim to maximize the information gain ˆ𝒆Δ
in the final loss function.
Similar to the control response prediction, we can also use a
multilayer perceptron to predict the uplift of each sample with and
without the information gain, respectively, as defined below:
ˆ𝜏 =𝑀𝐿𝑃(ˆ𝒆𝑓), ˜𝜏 =𝑀𝐿𝑃(ˆ𝒆Δ+ ˆ𝒆𝑓). (17)
Thus, we can get the information gain coefficient through a
difference function, which acts as the importance of the sample in
the uplift prediction loss function, and is defined as follows:
𝑤𝑏𝑎𝑡𝑐ℎ = exp( ˜𝜏− ˆ𝜏)˝
𝑏𝑎𝑡𝑐ℎ exp( ˜𝜏− ˆ𝜏),
Luplift =𝑤𝑏𝑎𝑡𝑐ℎ·(( 1−𝑡)·L( 𝜇0,𝑦)
+𝑡·(L(𝜇1,𝑦)+ 𝛽·L( ˜𝜇1,𝑦)))−𝛾·∥ ˆ𝒆Δ∥2 𝐹.
(18)
where𝜇1 =𝜇0+ ˆ𝜏 is the predicted treatment response, ˜𝜇1 =𝜇0+ ˜𝜏
is the predicted treatment response with treatment-feature interac-
tion,𝑤𝑏𝑎𝑡𝑐ℎ is the sample weight calculated in the batch,𝛽 and𝛾
are the hyperparmeters to control the trade-off.
5 EXPERIMENTS
In this section, we conduct extensive experiments on a synthetic
dataset and a product dataset to answer the following research
questions:
• RQ1: Can our UMLC outperform different baselines on vari-
ous commonly used uplift modeling metrics?
• RQ2: How does each proposed module contributes to the
performance of our UMLC?
• RQ3: How does the choice of group number influences the
performance of our UMLC?
And we also conduct more detailed experiments and analysis in
Appendix C.
5.1 Experimental Setups
5.1.1 Datasets. Synthetic dataset. To simulate complex real-world
scenarios, the synthetic dataset used in our incorporates several
key factors. 1) the generation of user features and context features
is independent of the treatment to simulate the real-world RCTs. 2)
For each user, a random selection of 60-130 contexts is made from
the context pool, and these are combined to generate the samples,
which ensures that each user is connected with multiple contexts
in a random manner. 3) The distributions of user responses in both
the treatment and control groups exhibit long-tailed behavior. In
light of Assumption 1, we divide the contexts into six groups based
on their influence on the response. 4) Similar to the real-world
data, the features include three types of distribution features: bi-
nary, categorical, and numerical. For each type, we use Bernoulli,
Multinomial, and Gaussian distributions, respectively. Moreover,
we present the detailed generation process of the Synthetic dataset
in Appendix C.1.
Production dataset. This dataset comes from an industrial pro-
duction environment, one of the largest short-video platforms in
China. For such short video platforms, clarity is an important user
experience indicator. A decrease in clarity may lead to a decrease
in users’ playback time. Therefore, through random experiments
Figure 3: The visualization of the Production dataset. As 𝑡
increases, the clarity of the video correspondingly enhances.
within a week, we provided high-clarity videos (𝑡 = 1) to the treat-
ment group and low-clarity videos (𝑡 = 0) to the control group. We
count the total viewing time of users’ short videos in a week and
quantify the impact of definition degradation on user experience.
The visualization of this dataset is shown in Figure 3. For the online
random experiments, we control the distributions of the users in
two groups to be similar and collect the data that each user with all
the short videos played. Moreover, the statistics of the two datasets
are presented in Appendix C.1.
5.1.2 Baselines and Metrics. Baselines. We compare our UMLC
with S-Learner [17], T-Learner [17], TARNet [31], CFRNet [31],
DragonNet [32], EUEN [16] and UniTE [21]. All of them are the
representative methods in uplift modeling.
Metrics. Following the setup of previous work [ 3], we employ
three evaluation metrics commonly used in uplift modeling, i.e.,
AUUC (Area under Uplift Curve) , QINI (Qini Coefficient) and
KENDALL (Kendall’s Rank Correlation).
5.1.3 Implementation Details. We implement all baselines and our
UMLC based on Pytorch 1.10, with Adam as the optimizer and a
maximum iteration count of 50. We use the QINI as a reference
to search for the best hyper-parameters for all baselines and our
model. We also adopt an early stopping mechanism with a patience
of 5 to avoid over-fitting to the training set. Furthermore, we utilize
the hyper-parameter search library Optuna [ 1] to accelerate the
tuning process, all experiments are implemented on NVIDIA A40
and Intel(R) Xeon(R) 5318Y Gold CPU @ 2.10GHz. The code of
our UMLC framework is provided in https://github.com/ZexuSun/
UMLC.
5.2 Overall Performance (RQ1)
To evaluate the effectiveness and compatibility of our UMLC, we
conduct experiments on a synthetic dataset and a production dataset.
The results are presented in Table 1, and we have the following
observations. 1) S-Learner and T-Learner get competitive results
on the two datasets among all the baseline methods. This indicates
that the complex design of model structure ( e.g., representation
balancing, target regularization) may not be beneficial for the uplift
prediction in real-time marketing. In particular, the massive data of
this scenario suffers from the significant distribution shift among
the two groups; without the specific model structure design, the
uplift models may get even worse uplift prediction results than
the S-Learner and T-Learner. 2) CFRNet performs competitively
among all the representation learning-based methods, but due to
6

Robust Uplift Modeling with Large-Scale Contexts for
Real-time Marketing KDD ’25, August 3–7, 2025, Toronto, ON, Canada
Table 1: Overall comparison between our UMLC and the baselines on Synthetic and Production datasets. We report the results
over five random seeds. The best results and second best results are bold and underlined , respectively.
Method Synthetic Dataset Production Dataset AUUC QINI KENDALL AUUC QINI KENDALL
S-Learner 0.2104± 0.0292 0.2502 ± 0.0116 0.1186 ± 0.0118 1.7907 ± 0.0529 2.3156 ± 0.0493 0.2631 ± 0.0252
T-Learner 0.2250± 0.0201 0.2697 ± 0.0178 0.1185 ± 0.0110 1.8007 ± 0.0634 2.3426 ± 0.0504 0.3152 ± 0.0209
TARNet 0.2131± 0.0136 0.2379 ± 0.0224 0.1368 ± 0.0122 1.7754 ± 0.0575 2.2764 ± 0.0473 0.3263 ± 0.0286
CFRNet-mmd 0.2077± 0.0237 0.2120 ± 0.0257 0.1689 ± 0.0134 1.6569 ± 0.0594 2.1614 ± 0.0528 0.3368 ± 0.0227
CFRNet-wass 0.2139± 0.0298 0.2234 ± 0.0309 0.1594 ± 0.0166 1.7286 ± 0.0646 2.1093 ± 0.0602 0.3536 ± 0.0346
DragonNet 0.2574± 0.0365 0.2153 ± 0.0279 0.1754 ± 0.0138 1.3581 ± 0.0613 1.8750 ± 0.0522 0.3894± 0.0258
EUEN 0.2158± 0.0202 0.2170 ± 0.0195 0.1126 ± 0.0087 1.2506 ± 0.0505 1.7092 ± 0.0513 0.3157 ± 0.0220
UniTE 0.2091± 0.0226 0.2071 ± 0.0234 0.1284 ± 0.0126 1.3092 ± 0.0499 1.8075 ± 0.0534 0.3684 ± 0.0275
UMLC (CFRNet-mmd) 0.3149± 0.0209 0.2558± 0.0191 0.1647± 0.0152 2.2106± 0.0595 2.6105± 0.0545 0.3473± 0.0246
UMLC (CFRNet-wass) 0.2871± 0.0235 0.2499± 0.0204 0.1584± 0.0112 2.0329± 0.0565 2.5201± 0.0453 0.3210± 0.0277
UMLC (DragonNet) 0.2549± 0.0208 0.2961± 0.0216 0.1894± 0.0165 1.9019± 0.0556 1.8514± 0.0463 0.3368± 0.0265
UMLC (EUEN) 0.2406± 0.0245 0.2594± 0.0268 0.1473± 0.0124 1.9539± 0.0555 2.3680± 0.0469 0.2631± 0.0251
UMLC (UniTE) 0.2533± 0.0269 0.2467± 0.0221 0.1594± 0.0166 2.0505± 0.0594 2.4416± 0.0569 0.2947± 0.0271
Table 2: Ablation study of our UMLC with four base uplift models on Synthetic and Production datasets. We report the results
over five random seeds. The best results and second best results are bold and underlined , respectively.
Method Synthetic Dataset Production Dataset AUUC QINI KENDALL AUUC QINI KENDALL
UMLC (CFRNet-mmd) 0.3149± 0.0209 0.2558± 0.0191 0.1647± 0.0152 2.2106± 0.0595 2.6105± 0.0545 0.3473± 0.0246
w/o RCG 0.2321± 0.0201 0.2230 ± 0.0208 0.1694± 0.0162 1.9073 ± 0.0549 2.4665 ± 0.0435 0.3578± 0.0249
w/o UCI 0.2395± 0.0221 0.2268 ± 0.0164 0.1547 ± 0.0149 1.8578 ± 0.0584 1.8255 ± 0.0470 0.3084 ± 0.0251
w/o TFI 0.2144± 0.0213 0.2482 ± 0.0144 0.1315 ± 0.0159 2.1349 ± 0.0557 2.4983 ± 0.0539 0.3263 ± 0.0248
UMLC (CFRNet-wass) 0.2871± 0.0235 0.2499± 0.0204 0.1584± 0.0112 2.0329± 0.0565 2.5201± 0.0453 0.3210± 0.0277
w/o RCG 0.2221± 0.0209 0.2279 ± 0.0196 0.1601± 0.0123 1.9214 ± 0.0568 2.3612 ± 0.0519 0.3597± 0.0244
w/o UCI 0.2355± 0.0213 0.2026 ± 0.0219 0.1328 ± 0.0179 1.9307 ± 0.0583 1.9992 ± 0.0478 0.3122 ± 0.0257
w/o TFI 0.2062± 0.0204 0.2368 ± 0.0205 0.1473 ± 0.0119 2.0519± 0.0549 2.4805 ± 0.0543 0.3137 ± 0.0248
UMLC (DragonNet) 0.2549± 0.0208 0.2961± 0.0216 0.1894± 0.0165 1.9019± 0.0556 1.8514± 0.0463 0.3368± 0.0265
w/o RCG 0.3094± 0.0239 0.2019 ± 0.0222 0.1484 ± 0.0117 1.7542 ± 0.0574 1.8481 ± 0.0552 0.4210± 0.0252
w/o UCI 0.2634± 0.0212 0.2064 ± 0.0258 0.1557 ± 0.0174 1.8401 ± 0.0572 1.8370 ± 0.0487 0.3398 ± 0.0251
w/o TFI 0.2639± 0.0244 0.2365 ± 0.0205 0.1778 ± 0.0149 1.9050± 0.0583 1.8405 ± 0.0538 0.2778 ± 0.0277
UMLC (EUEN) 0.2406± 0.0245 0.2594± 0.0268 0.1473± 0.0124 1.9539± 0.0555 2.3680± 0.0469 0.2631± 0.0251
w/o RCG 0.2295± 0.0251 0.2404 ± 0.0226 0.1263 ± 0.0121 1.5694 ± 0.0586 2.0819 ± 0.0555 0.3789 ± 0.0257
w/o UCI 0.2170± 0.0215 0.1783 ± 0.0251 0.1491± 0.0143 1.3145 ± 0.0568 1.8223 ± 0.0538 0.3992± 0.0265
w/o TFI 0.2119± 0.0235 0.2121 ± 0.0223 0.1157 ± 0.0135 1.4179 ± 0.0579 2.2572 ± 0.0492 0.2315 ± 0.0266
UMLC (UniTE) 0.2533± 0.0269 0.2467± 0.0221 0.1594± 0.0166 2.0505± 0.0594 2.4416± 0.0569 0.2947± 0.0271
w/o RCG 0.2118± 0.0217 0.2083 ± 0.0244 0.1401 ± 0.0135 1.6776 ± 0.0576 2.1548 ± 0.0526 0.3421 ± 0.0277
w/o UCI 0.2087± 0.0295 0.2204 ± 0.0226 0.1389 ± 0.0164 1.7011 ± 0.0574 2.4001 ± 0.0554 0.3052 ± 0.0289
w/o TFI 0.2422± 0.0263 0.2078 ± 0.0204 0.1631± 0.0173 1.8688 ± 0.0586 2.3730 ± 0.0542 0.3947± 0.0255
the representation balancing of Integral Probability Metrics (e.g.,
Maximum Mean Discrepancy, Wasserstein), the training time cost
is high, especially the Wasserstein, which is optimized by the line
search. The results of DragonNet, EUEN, and UniTE may be worse
than the meta-learner methods; this may be because complex model
structure design may not be useful for the uplift task. 3) We combine
our UMLC with four commonly used uplift modeling methods (i.e.,
CFRNet, DragonNet, EUEN, UniTE). We can find that integrating
our UMLC on different uplift models can consistently achieve per-
formance improvement, especially on QINI. This may be because
we tune the model hyperparameters by using the QINI as the ob-
jective. This demonstrates the effectiveness of our UMLC, where
the carefully designed two modules can effectively collaboratively
reduce the distribution shift and perform feature interaction to
improve the model’s performance. After combining the four base
uplift models with our UMLC, the performance is improved across
7

KDD ’25, August 3–7, 2025, Toronto, ON, Canada Zexu Sun, et al.
Figure 4: The context embedding t-SNE visualization of different group number 𝐾 (2-10) and the sample counts on the trained
context embedding of Synthetic dataset. The first is the distribution of the original data.
diverse metrics on the two datasets. This suggests that our UMLC
can serve as a general framework to improve the performance of
uplift models in real-time marketing.
5.3 Ablation Study (RQ2)
In this section, we conduct the ablation studies of our UMLC and
analyze the role played by each module. We sequentially remove the
components of the UMLC, i.e., the Response-guided Context Group-
ing (RCG), the User-Context Interaction (UCI) and the Treatment-
Feature Interaction (TFI). We construct three variants of UMLC,
which are denoted as w/o RCG, w/o UCI, and w/o TFI. We present
the results in Table 2, and we can see that removing any part may
bring performance degradation. This verifies the validity of each
part designed in our UMLC. In particular, the response-guided
context grouping module can narrow the contexts’ feature space,
reducing the distribution shift caused by the large-scale contexts.
The user-context interaction part introduces the relationship be-
tween the user and context features, which can help the uplift model
better predict the user response. The treatment-feature interaction
part can help the model discover the treatment assignment sensi-
tive features, and the designed loss weight term can help the model
adjust the sample importance, which can assign a bigger weight for
the treatment assignment sensitive samples. All the components are
helpful in solving the real-time marketing problem and improving
prediction performance.
5.4 Context Grouping Analysis (RQ3)
In this section, we detailed an analysis of the choice of 𝐾. We
show the cluster results of the trained context embedding on the
Synthetic dataset in Figure 4. In the Synthetic dataset, we design
six groups of contexts through the influence of the response, and
from Figure 4, we can see that the trained context embedding can
2 3 4 5 6 7 8 9 10
Total Groups
0
2
4
6
8
10Groups
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1.0
Alignment
Treatment Control Alignment
(a) Groups matching results
2 3 4 5 6 7 8 9 10
Total Groups
0.150
0.175
0.200
0.225
0.250
0.275
0.300
0.325
0.350Values
AUUC
QINI
KENDALL (b) Performance with different groups
Figure 5: The evaluation of different group number 𝐾 (2-10).
We report the mean over five runs with different seeds.
reflect the groups, even though the original data visualization has
no evidence. The cluster results show that when we select𝐾 as 6, we
can get a good grouping result. To further illustrate the rationality
of the group number choice, we conduct additional experiments in
Figure 5. We define a metric Alignment to evaluate the performance
of grouping, i.e.,
Alignment = 𝐶𝑜𝑢𝑛𝑡 M (𝒙𝑢𝑡, 𝒈𝑡),(𝒙𝑢𝑐, 𝒈𝑐) 𝐶𝑜𝑢𝑛𝑡(𝒙𝑢𝑡) ,
where 𝒙𝑢𝑡, 𝒈𝑡 and 𝒙𝑢𝑐, 𝒈𝑐 are the users and all the context groups in
treatment and control groups, respectively.M(·,·) is to match the
users based on the k-Nearest Neighbors (k-NN) [11], then remain
the users 𝒙𝑢𝑡 where 𝒈𝑡 = 𝒈𝑐, and the 𝐶𝑜𝑢𝑛𝑡(·) represents the
sample counter. Alignment represents the proportion of similar
users in treatment and control groups that match the same context
groups of all the users in the treatment group.
From the results, we can see that although the group number in
treatment and control samples is consistent with the total group
number, the alignment is decreased with𝐾 increases and suffers
a drastic decline between 6 and 7. Specifically, we also show the
8

Robust Uplift Modeling with Large-Scale Contexts for
Real-time Marketing KDD ’25, August 3–7, 2025, Toronto, ON, Canada
model performance (i.e., UMLC (CFRNet-mmd)) across all the met-
rics with different group numbers. The results show that the model
performance increases on most metrics from𝐾 = 2 to 6, and also
decreases on the 𝐾 = 7. This indicates that, although the group
number is a hyperparameter, with a well trained response-guided
context grouping module, we can target its value from the embed-
ding space.
6 CONCLUSION
In this paper, to model the uplift in real-time marketing with
massive data, we propose a novel model-agnostic Robust Uplift
Modeling with Large-Scale Contexts (UMLC) framework. UMLC
consists of two customized modules. 1) The response-guided con-
text grouping module, which trains the context embedding through
the regression model, then clusters the embedding into groups. 2)
The feature interaction module, which contains two parts, i.e., the
user-context interaction and the treatment-feature interaction. We
conduct extensive evaluations to validate the effectiveness of our
UMLC, we also demonstrate the compatibility, which can be used
as a general framework for real-time marketing.
ACKNOWLEDGMENTS
We thank the support of the National Natural Science Foundation
of China (No.62302310).
REFERENCES
[1] Takuya Akiba, Shotaro Sano, Toshihiko Yanase, Takeru Ohta, and Masanori
Koyama. 2019. Optuna: A next-generation hyperparameter optimization frame-
work. In Proceedings of the 25th ACM SIGKDD international conference on knowl-
edge discovery & data mining . 2623–2631.
[2] Susan Athey and Stefan Wager. 2019. Estimating treatment effects with causal
forests: An application. Observational studies 5, 2 (2019), 37–51.
[3] Mouloud Belbahri, Alejandro Murua, Olivier Gandouet, and Vahid Partovi Nia.
2021. Qini-based uplift regression. The Annals of Applied Statistics 15, 3 (2021),
1247–1272.
[4] Ola Bratteli and Derek William Robinson. 2012. Operator algebras and quantum
statistical mechanics: Volume 1: C*-and W*-Algebras. Symmetry Groups. Decom-
position of States. Springer Science & Business Media.
[5] Dimitrios Buhalis and Marie Foerste. 2015. SoCoMo marketing for travel and
tourism: Empowering co-creation of value. Journal of destination marketing &
management 4, 3 (2015), 151–161.
[6] Dimitrios Buhalis and Yeyen Sinarta. 2019. Real-time co-creation and nowness
service: lessons from tourism and hospitality. Journal of Travel & Tourism Mar-
keting 36, 5 (2019), 563–582.
[7] Muffy Calder, Mario Kolberg, Evan H Magill, and Stephan Reiff-Marganiec. 2003.
Feature interaction: a critical review and considered forecast. Computer Networks
41, 1 (2003), 115–141.
[8] Huigang Chen, Totte Harinen, Jeong-Yoon Lee, Mike Yung, and Zhenyu Zhao.
2020. Causalml: Python package for causal machine learning. arXiv preprint
arXiv:2002.11631 (2020).
[9] Per-Erik Danielsson. 1980. Euclidean distance mapping. Computer Graphics and
image processing 14, 3 (1980), 227–248.
[10] Eustache Diemert, Artem Betlei, Christophe Renaudin, and Massih-Reza Amini.
2018. A large scale benchmark for uplift modeling. In KDD.
[11] Markus Frölich. 2004. Finite-sample properties of propensity-score matching
and weighting estimators. Review of Economics and Statistics 86, 1 (2004), 77–90.
[12] Chunjing Gan, Dan Yang, Binbin Hu, Ziqi Liu, Yue Shen, Zhiqiang Zhang, Jinjie
Gu, Jun Zhou, and Guannan Zhang. 2023. Making Large Language Models
Better Knowledge Miners for Online Marketing with Progressive Prompting
Augmentation. arXiv preprint arXiv:2312.05276 (2023).
[13] Yury Gorishniy, Ivan Rubachev, and Artem Babenko. 2022. On embeddings for
numerical features in tabular deep learning. Advances in Neural Information
Processing Systems 35 (2022), 24991–25004.
[14] Patrik Hoyer, Dominik Janzing, Joris M Mooij, Jonas Peters, and Bernhard
Schölkopf. 2008. Nonlinear causal discovery with additive noise models.Advances
in neural information processing systems 21 (2008).
[15] Abdul Jabbar, Pervaiz Akhtar, and Samir Dani. 2020. Real-time big data processing
for instantaneous marketing decisions: A problematization approach. Industrial
Marketing Management 90 (2020), 558–569.
[16] Wenwei Ke, Chuanren Liu, Xiangfu Shi, Yiqiao Dai, S Yu Philip, and Xiaoqiang
Zhu. 2021. Addressing exposure bias in uplift modeling for large-scale online
advertising. In 2021 IEEE International Conference on Data Mining (ICDM) . IEEE,
1156–1161.
[17] Sören R Künzel, Jasjeet S Sekhon, Peter J Bickel, and Bin Yu. 2019. Metalearners for
estimating heterogeneous treatment effects using machine learning. Proceedings
of the national academy of sciences 116, 10 (2019), 4156–4165.
[18] Dugang Liu, Xing Tang, Han Gao, Fuyuan Lyu, and Xiuqiang He. 2023. Explicit
Feature Interaction-aware Uplift Network for Online Marketing. arXiv preprint
arXiv:2306.00315 (2023).
[19] Guodong Liu, Yan Xu, and Kevin Tomsovic. 2015. Bidding strategy for micro-
grid in day-ahead market based on hybrid stochastic/robust optimization. IEEE
Transactions on Smart Grid 7, 1 (2015), 227–237.
[20] Hsueh-Ti Derek Liu, Francis Williams, Alec Jacobson, Sanja Fidler, and Or Litany.
2022. Learning smooth neural functions via lipschitz regularization. In ACM
SIGGRAPH 2022 Conference Proceedings . 1–13.
[21] Runshi Liu and Zhipeng Hou. 2023. UniTE: A Unified Treatment Effect Estimation
Method for One-sided and Two-sided Marketing. In Proceedings of the 32nd ACM
International Conference on Information and Knowledge Management . 1472–1481.
[22] Yun Liu, Yuanzheng Li, Hoay Beng Gooi, Ye Jian, Huanhai Xin, Xichen Jiang, and
Jianfei Pan. 2017. Distributed robust energy management of a multimicrogrid
system in the real-time energy market. IEEE Transactions on Sustainable Energy
10, 1 (2017), 396–406.
[23] Jiasen Lu, Jianwei Yang, Dhruv Batra, and Devi Parikh. 2016. Hierarchical
question-image co-attention for visual question answering. Advances in neural
information processing systems 29 (2016).
[24] Jiaqi Ma, Zhe Zhao, Xinyang Yi, Jilin Chen, Lichan Hong, and Ed H Chi. 2018.
Modeling task relationships in multi-task learning with multi-gate mixture-of-
experts. In Proceedings of the 24th ACM SIGKDD international conference on
knowledge discovery & data mining . 1930–1939.
[25] Belbahri Mouloud, Gandouet Olivier, and Kazma Ghaith. 2020. Adapting neural
networks for uplift models. arXiv preprint arXiv:2011.00041 (2020).
[26] Jie Peng, Hao Zou, Jiashuo Liu, Shaoming Li, Yibao Jiang, Jian Pei, and Peng
Cui. 2023. Offline policy evaluation in large action spaces via outcome-oriented
action grouping. In Proceedings of the ACM Web Conference 2023 . 1220–1230.
[27] Nicholas J Radcliffe and Patrick D Surry. 2011. Real-world uplift modelling with
significance-based uplift trees. White Paper TR-2011-1, Stochastic Solutions (2011),
1–33.
[28] Donald B Rubin. 2005. Causal inference using potential outcomes: Design, mod-
eling, decisions. J. Amer. Statist. Assoc. 100, 469 (2005), 322–331.
[29] Piotr Rzepakowski and Szymon Jaroszewicz. 2010. Decision trees for uplift
modeling. In 2010 IEEE International Conference on Data Mining . IEEE, 441–450.
[30] Piotr Rzepakowski and Szymon Jaroszewicz. 2012. Decision trees for uplift mod-
eling with single and multiple treatments. Knowledge and Information Systems
32 (2012), 303–327.
[31] Uri Shalit, Fredrik D Johansson, and David Sontag. 2017. Estimating individual
treatment effect: generalization bounds and algorithms. InInternational conference
on machine learning. PMLR, 3076–3085.
[32] Claudia Shi, David Blei, and Victor Veitch. 2019. Adapting neural networks for
the estimation of treatment effects. Advances in neural information processing
systems 32 (2019).
[33] Yang Sun, Junwei Pan, Alex Zhang, and Aaron Flores. 2021. FM2: Field-matrixed
factorization machines for recommender systems. In Proceedings of the web
conference 2021. 2828–2837.
[34] Zexu Sun, Bowei He, Ming Ma, Jiakai Tang, Yuchen Wang, Chen Ma, and Dugang
Liu. 2023. Robustness-enhanced Uplift Modeling with Adversarial Feature De-
sensitization. arXiv preprint arXiv:2310.04693 (2023).
[35] Wanjie Tao, Huihui Liu, Xuqi Li, Qun Dai, Hong Wen, and Zulong Chen. 2023.
Event-Aware Adaptive Clustering Uplift Network for Insurance Creative Ranking.
In Proceedings of the 46th International ACM SIGIR Conference on Research and
Development in Information Retrieval . 1966–1970.
[36] Ruoxi Wang, Rakesh Shivanna, Derek Cheng, Sagar Jain, Dong Lin, Lichan Hong,
and Ed Chi. 2021. Dcn v2: Improved deep & cross network and practical lessons
for web-scale learning to rank systems. In Proceedings of the web conference 2021 .
1785–1797.
[37] Anpeng Wu, Kun Kuang, Ruoxuan Xiong, Bo Li, and Fei Wu. 2023. Stable
estimation of heterogeneous treatment effects. In International Conference on
Machine Learning. PMLR, 37496–37510.
[38] Liuyi Yao, Sheng Li, Yaliang Li, Mengdi Huai, Jing Gao, and Aidong Zhang. 2018.
Representation learning for treatment effect estimation from observational data.
Advances in neural information processing systems 31 (2018).
[39] Weijia Zhang, Jiuyong Li, and Lin Liu. 2021. A unified survey of treatment effect
heterogeneity modelling and uplift modelling. ACM Computing Surveys (CSUR)
54, 8 (2021), 1–36.
9

KDD ’25, August 3–7, 2025, Toronto, ON, Canada Zexu Sun, et al.
A PROOF OF PROPOSITION 1
Proposition 1. (Restatement) If we can find a good predictive
function𝑓 and transformation function𝜉 with Lipschitz constraints on
contexts such that|ℎ(𝒙𝑢, 𝒙𝑐,𝑡)−𝑓(𝒙𝑢,𝜉(𝒙𝑐),𝑡)|≤ 𝜇,∀𝒙𝑢, 𝒙𝑐,𝑡 and

𝑓  𝒙𝑢,𝜉(𝒙𝑐 𝑖),𝑡  −𝑓  𝒙𝑢,𝜉(𝒙𝑐 𝑗),𝑡 

≤𝑐· 𝜉(𝒙𝑐 𝑖)− 𝜉(𝒙𝑐 𝑗) 𝑗 ,∀𝒙𝑢, 𝒙𝑐 𝑖,
𝒙𝑐 𝑗,𝑡 . Then the function𝜉 satisfies the Assumption 2 with𝜁 =𝑐,𝜂 = 2𝜇.
Proof.

ℎ 𝒙𝑢, 𝒙𝑐 𝑖,𝑡 −ℎ  𝒙𝑢, 𝒙𝑐 𝑗,𝑡 

≤

𝑓 𝒙𝑢,𝜉(𝒙𝑐 𝑖),𝑡 −𝑓  𝒙𝑢,𝜉(𝒙𝑐 𝑗),𝑡 

+

𝑓 𝒙𝑢,𝜉(𝒙𝑐 𝑖),𝑡 −ℎ 𝒙𝑢, 𝒙𝑐 𝑖,𝑡 

+

𝑓  𝒙𝑢,𝜉(𝒙𝑐 𝑗)  −ℎ  𝒙𝑢, 𝒙𝑐 𝑗,𝑡 

≤𝑐·
𝜉(𝒙𝑐 𝑖)− 𝜉(𝒙𝑐 𝑗) 2 + 2𝜇
□
B COMPUTATIONAL COMPLEXITY
In this section, we analyze the computational complexity of our
UMLC. The total computational complexity of the 𝑘-means, co-
attention and cross-attention is𝑂(𝑛𝐾𝑙𝐾𝑐)+𝑂

𝑛𝐾 2 𝑑

+𝑂((𝑛+𝐾𝑐)𝑛𝐾𝑢)+
𝑂 (𝐾𝑐+𝑛)𝐾 2𝑢 +𝑂 (𝐾𝑢+𝑛)𝐾 2𝑐 , where𝑛 is the number of sam-
ples,𝐾 is the number of clusters, 𝑙 is the iterations number of 𝐾
means,𝐾𝑐 is the dimension of the context embedding, 𝐾𝑢 is the
dimension of the user embedding,𝐾𝑑 is the dimension of the con-
catenation of context and user embedding.
C DETAILED EXPERIMENTS
C.1 Synthetic Dataset Generation.
In our problem setting, the synthetic data consists of user features
𝒙𝑢; context features 𝒙𝑐, treatment𝑡, and response𝑦, we describe
the generation process in the following.
• User Features Generation. We assume that the user features
is a𝑝 dimensional vector𝑥𝑢 1,...,𝑥 𝑢𝑝 . Specially, we generate them
with the binary features𝑥𝑢 1,...,𝑥 𝑢𝑝𝑏∼ Bernoulli(0.5), and the con-
tinuous features𝑥𝑢 𝑝𝑏+1,...,𝑥 𝑢𝑛𝑏+𝑛𝑐∼N( 0, 1), where𝑝𝑏 and𝑝𝑐 are
the dimensions of binary features and the continuous features,
respectively, and𝑝 =𝑝𝑏+𝑝𝑐. We set𝑝𝑏 = 34 and𝑝𝑐 = 66.
Context features Generation. To simulate the real-word data, we
use𝑞 as the length of the context features, and there are three types
of features in the context features 𝒙𝑐, i.e., binary features, contin-
uous features and categorical features. Specially, the binary features
𝑥𝑐 1,...,𝑥 𝑐𝑞𝑏∼ Bernoulli(0.5), the continuous features𝑥𝑐 𝑞𝑏+1,...,𝑥 𝑐𝑞𝑏+𝑞𝑐
∼N( 0, 1) and the categorical features𝑥𝑐 𝑞𝑏+𝑞𝑐+1,...,𝑥 𝑐𝑞𝑏+𝑞𝑐+𝑞𝑚∼
Multinomial(4, 0.25, 0.25, 0.25, 0.25), We denote the dimensions
as𝑞𝑏,𝑞𝑐, and 𝑞𝑚 for them. And we set 𝑞𝑏 = 34,𝑞𝑐 = 66 and
𝑞𝑚 = 3. Referring to the Assumption 1, the influence of the con-
text features should be divided into 𝐾 groups. In the Synthetic
dataset, we set𝐾 = 6, and we generate another categorical feature
𝑥𝑐𝑞∼ Multinomial(6, 0.2, 0.16, 0.16, 0.16, 0.16, 0.16), whose influence
for the response is separately modeled in the response generation.
User-Context Features Combination. Our goal is to replicate
the real-world, real-time marketing scenario, where a relatively
small number of users engage with a significantly larger number
of contexts. After we generate the user features and the context
0 5 10 15 20 25 30
Feature Value
0.00
0.01
0.02
0.03
0.04
0.05Proportion
(a) Continuous feature 1
0 500 1000 1500 2000 2500
Feature Value
0.000
0.002
0.004
0.006
0.008
0.010
0.012
0.014
0.016Proportion (b) Continuous feature 2
0 5 10 15 20 25 30
Feature Value
0.00
0.01
0.02
0.03
0.04
0.05
0.06Proportion
(c) Continuous feature 3
0 5 10 15 20 25 30 35
Feature Value
0.0
0.1
0.2
0.3
0.4
0.5Proportion (d) Categorical feature
Figure 6: The feature visualization of the Production dataset.
features, we need to design the combination of the user and the con-
texts. Specifically, we generate a large context pool (i.e., 100 times
larger than the user number), and each user is associated with a
uniquely and randomly chosen subset (i.e., 60-130 contexts) of these
contexts, highlighting the one-to-many relationship fundamental
to user-context interactions.
Treatment Generation. In the randomized control trials, the
treatment is randomly assigned to each user. Thus, we generate
𝑡∼ Bernoulli(0.5) for each user, and the samples belonging to each
user are assigned with the same𝑡.
Response Generation. For each sample, we generate the two
potential responses𝑦0 and𝑦1 as follows:
𝑦0 =0.5
𝑝∑︁
𝑖=1
𝑥𝑢 𝑖 + 0.5
𝑞𝑐+𝑞𝑏∑︁
𝑗=1
𝑥𝑐 𝑗+ 0.5
𝑞𝑏+𝑞𝑐∑︁
𝑗=1
(
𝑝∑︁
𝑖=1
𝑥𝑢 𝑖)𝑥𝑐 𝑗
+ 0.5
𝑞𝑏+𝑞𝑐+𝑞𝑚∑︁
𝑣=𝑞𝑏+𝑞𝑐+1
𝑥𝑐 𝑣+𝑧0+𝜖0,
where the distribution of𝑧0, i.e.,P(𝑧0)∈{N( 0, 1),N( 2, 0.5),N(− 1, 2),
N( 3, 1.5),N(− 2, 0.8),N( 1, 2)} for the corresponding group (i.e.,𝑥𝑐 𝑑)
of the context,𝜖0∼N( 0, 1) is the noise term.
Expanding upon𝑦0, the user response𝑦1 incorporates the effect
of the treatment and is formulated as:
𝑦1 =𝑦0+ 0.2
𝑝∑︁
𝑖=1
𝑥𝑢 𝑖 + 0.2
𝑞𝑐+𝑞𝑏∑︁
𝑗=1
𝑥𝑐 𝑗+ 0.2
𝑞𝑏+𝑞𝑐∑︁
𝑗=1
(
𝑝∑︁
𝑖=1
𝑥𝑢 𝑖)𝑥𝑐 𝑗
+ 0.2
𝑞𝑏+𝑞𝑐+𝑞𝑚∑︁
𝑣=𝑞𝑏+𝑞𝑐+1
𝑥𝑐 𝑣+𝑧1+𝜖1.
where𝑧1 is similar to𝑧0, and𝜖1∼N( 0, 1) is the noise term.
Moreover, to better understand the two datasets that we used,
we present the statistics of the two datasets in Table 3.
10

Robust Uplift Modeling with Large-Scale Contexts for
Real-time Marketing KDD ’25, August 3–7, 2025, Toronto, ON, Canada
Table 3: Statistics of the Synthetic dataset and Produc-
tion Dataset. We randomly split the two datasets for
train/validation/test split proportion of 70%/20%/10%.
Dataset Feature number User number User Context Treated Control
Synthetic 100 103 236421 236116
Production 66 109 397943 397852
C.2 Production Dataset Visualization
In this section, we make some visualization for the Production
dataset, the results are shown in Figure 6, which can help the readers
make decisions to implement our UMLC on their own scenario.
C.3 Experimental Setups
We present the detailed description of the baselines we used in the
following:
• S-Learner [17]: S-Learner is a kind of meta-learner method
that uses a single estimator to estimate the outcome without
giving the treatment a special role.
• T-Learner [17]: T-Learner is similar to S-Learner, which
uses two estimators for the treatment and control groups,
respectively.
• TARNet [31]: TARNet is a commonly used neural network-
based uplift model. It uses the shared bottom network to
extract feature information.
• CFRNet [31]: CFRNet (i.e., CFRNet-wass, CFRNet-mmd) ap-
plies an additional loss to TARNet, which forces the learned
treated and control feature distributions to be closer.
• DragonNet [32]: DragonNet exploits the sufficiency of the
propensity score for estimation adjustment, and uses a regu-
larization procedure based on the non-parametric estimation
theory.
• EUEN [16]: EUEN is an explicit uplift modeling approach,
which can correct the exposure bias.
• UniTE [21]: UniTE adopts the Robinson Decomposition [4]
framework, and design a MMoE [ 24] based structure for
uplift prediction.
We present the detailed description of the metrics we used in
the following:
• AUUC (Area under Uplift Curve) : A common metric to
evaluate the area under the uplift curve [ 29]. We use the
CausalML package [8] to implement the metric.
• QINI (Qini Coefficient) [25]: A common metric to evaluate
the area under the qini curve, different from AUUC, it scale
the responses in control group.
• KENDALL (Kendall’s Rank Correlation) [25]: A metric
to evaluate the average predicted uplift and the predicted
uplift in each bin, we report the result of 20 bins.
Additionally, we also evaluate the results of the ground truth uplift
prediction on the Synthetic dataset, we use the following metrics:
Top s% CFRNet (User) CFRNet UMLC (CFRNet) ↑(CFRNet (User)) ↑(CFRNet)
5% 0.099% 0.101% 0.104% 0.0045% 0.0032%
10% 0.217% 0.219% 0.220% 0.0031% 0.0006%
15% 0.320% 0.329% 0.332% 0.0117% 0.0026%
20% 0.430% 0.435% 0.439% 0.0093% 0.0039%
25% 0.516% 0.514% 0.517% 0.0008% 0.0028%
30% 0.583% 0.581% 0.590% 0.0071% 0.0088%
35% 0.662% 0.677% 0.680% 0.0188% 0.0032%
40% 0.746% 0.775% 0.787% 0.0419% 0.0120%
45% 0.828% 0.873% 0.885% 0.0566% 0.0120%
50% 0.924% 0.962% 0.998% 0.0733% 0.0357%
Figure 7: The results of uplift gains ( i.e., only user, user +
context, our UMLC with user + context), we use 5% as the
step size.
Table 4: The results of ground truth uplift evaluation on
Synthetic Dataset. We report the results over five random
seeds. The best results and second best results are bold and
underlined, respectively.
Method 𝜖𝐴𝑇𝐸 𝜖𝑃𝐸𝐻𝐸
S-Learner 0.6093± 0.1592 3.1983 ± 0.1921
T-Learner 0.5727± 0.1628 2.9817 ± 0.1729
TARNet 0.5139± 0.1529 2.7789 ± 0.1948
CFRNet-mmd 0.5133± 0.1190 2.3743 ± 0.1829
CFRNet-wass 0.5017± 0.1739 2.4283 ± 0.1638
DragonNet 0.5129± 0.1294 2.7891 ± 0.1384
EUEN 0.4938± 0.1599 2.3802 ± 0.2193
UniTE 0.5213± 0.1074 2.8345 ± 0.1739
UMLC (CFRNet-mmd) 0.4932± 0.1439 2.3482± 0.1274
UMLC (CFRNet-wass) 0.4721± 0.1548 2.3793± 0.1539
UMLC (DragonNet) 0.4083± 0.1283 2.4930± 0.1983
UMLC (EUEN) 0.4193± 0.1492 2.3237± 0.1385
UMLC (UniTE) 0.4892± 0.1947 2.6941± 0.1928
• 𝜖𝐴𝑇𝐸 : The absolute error on the average treatment effect,
which is defined as:
𝜖𝐴𝑇𝐸 =

 1 𝑛 𝑛∑︁ 𝑖=1  𝑦1−𝑦0 − 1 𝑛 𝑛∑︁ 𝑖=1  ˆ𝑦1− ˆ𝑦0

• 𝜖𝑃𝐸𝐻𝐸 : In order to measure the accuracy of the uplift predic-
tion, we use the Precision in Estimation of Heterogeneous
Effect (PEHE), which is defined as:
𝜖𝑃𝐸𝐻𝐸 = 1 𝑛 𝑛∑︁ 𝑖=1 h 𝑦1−𝑦0  −  ˆ𝑦1− ˆ𝑦0 i 2
C.4 Ground Truth Uplift Evaluation
We present the evaluation of the ground truth uplift in Table 4.
From the table, it can be observed that for𝜖𝐴𝑇𝐸 , UMLC (DragonNet)
achieves the best performance with a mean value of 0.4083 , closely
followed by UMLC (EUEN) with a mean of 0.4193 . For 𝜖𝑃𝐸𝐻𝐸 ,
UMLC (EUEN) performed the best with a mean value of 2.3237 ,
while UMLC (CFRNet-mmd) ranked second with a mean of 2.3482.
Our UMLC consistent superiors performance across two metrics,
which demonstrates UMLC’s advantages and reliability in uplift
prediction.
11

KDD ’25, August 3–7, 2025, Toronto, ON, Canada Zexu Sun, et al.
128 256 512 1024 2048
Batch Size b
0.16
0.18
0.20
0.22
0.24
0.26
0.28
0.30
0.32Values
AUUC
QINI
KENDALL
(a) Batch size 𝑏 on Synthenic dataset
0.1 0.3 0.5 0.7 0.9
Loss Weight
0.16
0.18
0.20
0.22
0.24
0.26
0.28
0.30
0.32Values
AUUC
QINI
KENDALL (b) Loss weight 𝛽 on Synthenic dataset
0.1 0.3 0.5 0.7 0.9
Loss Weight
0.16
0.18
0.20
0.22
0.24
0.26
0.28
0.30
0.32Values
AUUC
QINI
KENDALL (c) Loss weight𝛾 on Synthenic dataset
128 256 512 1024 2048
Batch Size b
0.25
0.3
0.35
1.5
2
2.5
3
Values
AUUC
QINI
KENDALL
(d) Batch size𝑏 on Production dataset
0.1 0.3 0.5 0.7 0.9
Loss Weight
0.25
0.3
0.35
1.5
2
2.5
3
Values
AUUC
QINI
KENDALL (e) Loss weight 𝛽 on Production dataset
0.1 0.3 0.5 0.7 0.9
Loss Weight
0.25
0.3
0.35
1.5
2
2.5
3
Values
AUUC
QINI
KENDALL (f) Loss weight 𝛾 on Production dataset
Figure 8: The results of the hyperparameter analysis on the two datasets ( i.e., batch size𝑏, loss weight 𝛽 and loss weight𝛾). We
report the results of the mean over five runs with different seeds.
C.5 Algorithm Pseudocode
In this section, to easily understand our proposed framework, we
provide the pseudocode of our UMLC in Algorithm 1.
Algorithm 1 The training procedure of our UMLC.
Input: User features 𝒙𝑢, context features𝒙𝑐, treatment𝑡, response
𝑦, regression model parameters 𝝋, uplift model parameters 𝝎,
hyperparameters𝛼,𝛽,𝛾.
Output: The regression model parameters 𝝋 and uplift model
parameters 𝝎.
Response-guided Context Grouping
1: Calculate the prediction loss according to Eq. (5).
2: Calculate the Lipschitz Regularization according to Eq. (7).
3: Update the regression model parameters 𝝋 according to Eq. (8).
4: Group and aggregate the training data according to Eq. (9).
Feature Interaction
5: Get the user and context attention matrix according to Eq. (11).
6: Calculate the user and context attention vectors according to
Eq. (13).
7: Predict the control response according to Eq. (14).
8: Calculate the information gain by treatment assignment ac-
cording to Eq. (16).
9: Predict the uplift according to Eq. (17).
10: Update the uplift model parameters 𝝎 according to Eq. (18).
C.6 Uplift Gain Experiments
To further evaluate the performance of our UMLC, we conduct the
uplift gain experiments on the Synthetic dataset, which has two
potential responses for each sample. After we have the learned
uplift models, we sort the samples by the uplifts that the model
predicted. And then, we assign the top 𝑠% of the samples with
treatment𝑡 = 1 and the rest with𝑡 = 0. Comparing to the strategy
that all the samples are assigned with𝑡 = 0, we can calculate the
uplift gain (i.e., Gain) by the sum of corresponding user responses,
i.e.,
Gain =
˝
𝑠%𝑦1+ ˝ rest𝑦0− ˝𝑦0 ˝𝑦0 × 100%
where𝑠% and rest represent the top𝑠% of the samples and the rest
of the samples, respectively.
We present the results in Figure 7, we use 5% as the step size. From
the results, we have the following observations. 1) From the results
of CFRNet (User) and CFRNet, we can see that the CFRNet performs
better than CFRNet (User). This indicates that only considering the
user to assign treatments for each sample may introduce bias for
the model learning. 2) Our UMLC consistently outperforms CFRNet
(User) and CFRNet across all the top𝑠% of the samples. With the
percentage of the sample increase, the improvement of our UMLC
becomes larger. This may be because when the𝑠% increases, the
context groups of our UMLC can mitigate the prediction variance
of the large-scale contexts, which can help the model get a better
ranking of the samples to achieve higher uplift gain.
C.7 Hyperparameter Sensitivity analysis
In this section, we conduct experiments on the two datasets to
evaluate the influence of the important hyperparameters, i.e., batch
size𝑏, loss weight𝛽, and loss weight𝛾. In particular, we use the
UMLC (CFRNet-mmd) as the model to handle the experiments; we
present the results in Figure 8.
From the results, we have the following observations. 1) Our
UMLC is pretty robust to the batch size𝑏, even though we adjust
the sample weights on the batch level. This shows that the infor-
mation gain we used by the treatment feature interaction is a soft
12

Robust Uplift Modeling with Large-Scale Contexts for
Real-time Marketing KDD ’25, August 3–7, 2025, Toronto, ON, Canada
5 10 15 20 25 30 35 40 45
Total Groups
0
10
20
30
40Groups
0.2
0.3
0.4
0.5
0.6
0.7
Alignment
Treatment Control Alignment
(a) Groups matching results
5 10 15 20 25 30 35 40 45
Total Groups
0.25
0.3
0.35
1.5
2
2.5
3
Values
AUUC
QINI
KENDALL (b) Performance with different groups
Figure 9: The evaluation of different group number 𝐾 (5-45).
We report the mean over five runs with different seeds.
approach for the model optimization, based on the trained user-
context embedding, the loss weight may be rational for the model
optimization, which does not influence the model performance
much. 2) For the loss weight𝛽 and𝛾, the model performance first
increases across various metrics, but it suffers from the decrease
when the weights are bigger than the specific values. This may be
because the two components of the loss function can be regarded
as the regularizations of the model; the big weights may cause the
model to lose the power of prediction. Thus, the readers need to
carefully adjust their values on the different datasets.
C.8 Context Grouping Analysis
To further validate the effectiveness of the response-guided con-
text grouping module, we also conducted experiments to show the
visualization, the alignment, and the performance of our UMLC on
the Production dataset. The alignment and the performance of the
learned model (i.e., UMLC (CFRNet-mmd)) are shown in Figure 10,
the visualization is shown in Figure 10. Due to the complexity of
the context data in the Production dataset, the true group number
of the learned context embedding is unknown, we show the clus-
ter visualization and sample counter from 5 to 45 (5 per step). To
reflect the context grouping performance more clearly, instead of
bar charts, we use pie charts for the sample counter of each group
number𝐾 on the Production dataset. The sample counter, which
is bigger than 5% of the total samples, is indicated; with bigger𝐾,
the sample counters of most groups are less than 5%. We combine
the results in Figure 9 with the visualization to further analyze the
performance. From Figure 9(a), the context groups in the treatment
and control groups become imbalanced with big total groups 𝐾
(i.e., 25, 35, 40, 45). This may be because the Production dataset is
collected from a real-world scenario, which is more complex than
the Synthetic dataset. However, considering the alignment results
and the model performance, they suffer from a big decline after the
group number𝐾 is bigger than 20. This indicates that, even with
more complex data, we can target the number of context groups
without training the whole model.
C.9 Additional Ablation Study
In the main contents, we conduct the experiments with four base
uplift models. Due to the space limitation of the main contents, we
present the experimental results with three another uplift models in
Table 5. From the results, we can see that, with our UMLC, we can
consistently improve the model performance on most metrics. And
the ablation study shows that removing each part of our UMLC
will hurt the model performance.
C.10 Additional Evaluations
In the main contents of our paper, we focus on comparing each base
model with and without UMLC. To better evaluate the performance
of our UMLC, in this section, we conduct the variant by three
aspects, (1) without context grouping, (2) grouped with Kmeans, and
(3) grouped with other cluster methods. The results are presented
in Figure 11. From the results, we can see that our UMLC performs
better than only using user features, using the category feature
for grouping or applying Kmeans on the context samples. For the
variants of UMLC ( i.e., UMLC-Hierarchical, UMLC-Spectral and
UMLC-DBSCAN), they perform similar with the original UMLC,
which verifies the robustness of our UMLC for different cluster
methods.
13

KDD ’25, August 3–7, 2025, Toronto, ON, Canada Zexu Sun, et al.
Figure 10: The context embedding t-SNE visualization of different group number 𝐾 (5-45, 5 per step) and the sample counts on
the trained context embedding of Production dataset. The first is the distribution of the normalized original context data.
Table 5: Additional Ablation study of our UMLC with another three uplift models on Synthetic and Production datasets. We
report the results over five random seeds. The best results and second best results are bold and underlined , respectively.
Method Synthetic Dataset Production Dataset AUUC QINI KENDALL AUUC QINI KENDALL
UMLC (S-Learner) 0.2346± 0.0226 0.2597± 0.0283 0.1304± 0.0126 1.9038± 0.0583 2.4983± 0.0518 0.2792± 0.0237
w/o RCG 0.2145± 0.0264 0.2512 ± 0.0233 0.1207 ± 0.0135 1.8263 ± 0.0536 2.3252 ± 0.0483 0.2613 ± 0.0236
w/o UCI 0.2259± 0.0225 0.2519 ± 0.0214 0.1240 ± 0.0137 1.8342 ± 0.0547 2.4552 ± 0.0462 0.2641 ± 0.0263
w/o TFI 0.2343± 0.0204 0.2585 ± 0.0195 0.1296 ± 0.0147 1.8591 ± 0.0556 2.4205 ± 0.0483 0.2763 ± 0.0247
UMLC (T-Learner) 0.2734± 0.0284 0.2783± 0.0223 0.1279± 0.0148 2.0321± 0.0525 2.4983± 0.0527 0.3174± 0.0237
w/o RCG 0.2291± 0.0282 0.2230 ± 0.0226 0.1143 ± 0.0184 1.8133 ± 0.0522 2.3531 ± 0.0438 0.2729 ± 0.0274
w/o UCI 0.2465± 0.0235 0.2483 ± 0.0194 0.1171 ± 0.0136 1.8781 ± 0.0573 2.1255 ± 0.0462 0.2982 ± 0.0224
w/o TFI 0.2657± 0.0228 0.2598 ± 0.0122 0.1215 ± 0.0137 2.0201 ± 0.0583 2.4218 ± 0.0542 0.2947 ± 0.0295
UMLC (TARNet) 0.2913± 0.0294 0.2472± 0.0228 0.1219± 0.0162 2.1349± 0.0552 2.3842± 0.0454 0.3306± 0.0273
w/o RCG 0.2296± 0.0235 0.2230 ± 0.0223 0.1194 ± 0.0146 1.9073 ± 0.0584 2.3983± 0.0525 0.3278 ± 0.0235
w/o UCI 0.2567± 0.0292 0.2268 ± 0.0235 0.1187 ± 0.0184 1.8578 ± 0.0587 2.3255 ± 0.0484 0.3284 ± 0.0271
w/o TFI 0.2783± 0.0223 0.2445 ± 0.0209 0.1175 ± 0.0142 2.0422 ± 0.0554 2.3365 ± 0.0427 0.3263 ± 0.0235
14

Robust Uplift Modeling with Large-Scale Contexts for
Real-time Marketing KDD ’25, August 3–7, 2025, Toronto, ON, Canada
User
 Category
 Context Kmeans
 UMLC
UMLC-Hierarchical
 UMLC-Spectral UMLC-DBSCAN
(a) Synthetic dataset
User Category Context Kmeans UMLC
UMLC-Hierarchical UMLC-Spectral UMLC-DBSCAN
(b) Production dataset
Figure 11: Performance of the variations of our UMLC. User represents the results with only the user features. Category
represents we use the ground truth category in the context features for learning the context embedding. Context K-means
represents that we apply K-means on the context samples rather than embedding. UMLC-Hierarchical, UMLC-Spectral and
UMLC-DBSCAN are the variants of our UMLC with different cluster methods on the context embedding.
15
