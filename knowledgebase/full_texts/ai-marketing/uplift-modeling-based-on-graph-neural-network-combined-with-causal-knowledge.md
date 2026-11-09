---
title: Uplift Modeling based on Graph Neural Network Combined with Causal Knowledge
url: https://arxiv.org/abs/2311.08434
category: ai-marketing
subcategory: empirical
date: 2023-11
venue: ''
authors:
- Haowen Wang
- Xinyan Ye
- Yangze Zhou
- Zhiyi Zhang
- Longhan Zhang
source: arxiv
pdf_url: https://arxiv.org/pdf/2311.08434
pages: 6
chars: 28579
fetched_at: '2026-11-08T13:13:45+00:00'
kb_version: 1
---

# Uplift Modeling based on Graph Neural Network Combined with Causal Knowledge

Uplift Modeling based on Graph Neural Network Combined with
Causal Knowledge
Haowen Wang
Alipay, AntGroup
China
wanghaowen@antgroup.com
Xinyan Ye
Imperial College London
UK
xy2119@ic.ac.uk
Yikang Wang
University College London
UK
yikang.wang.21@ucl.ac.uk
Yangze Zhou
Zhejiang University
China
yangze.zhou@zju.edu.cn
Zhiyi Zhang
Peking University
emma0302@pku.edu.cn
Longhan Zhang
Zhejiang Lab
China
longhanz@zhejianglab.com
emma0302@pku.edu.cn
Jing Jiang∗
Zhejiang Lab
China
jiangj@zhejianglab.com
ABSTRACT
Uplift modeling is a fundamental component of marketing effect
modeling, which is commonly employed to evaluate the effects of
treatments on outcomes. Through uplift modeling, we can iden-
tify the treatment with the greatest benefit. On the other side, we
can identify clients who are likely to make favorable decisions
in response to a certain treatment. In the past, uplift modeling
approaches relied heavily on the difference-in-difference (DID) ar-
chitecture, paired with a machine learning model as the estimation
learner, while neglecting the link and confidential information be-
tween features. We proposed a framework based on graph neural
networks that combine causal knowledge with an estimate of uplift
value. Firstly, we presented a causal representation technique based
on CATE (conditional average treatment effect) estimation and ad-
jacency matrix structure learning. Secondly, we suggested a more
scalable uplift modeling framework based on graph convolution
networks for combining causal knowledge. Our findings demon-
strate that this method works effectively for predicting uplift values,
with small errors in typical simulated data, and its effectiveness has
been verified in actual industry marketing data.
CCS CONCEPTS
• Information systems→ Information systems applications; •
Computing methodologies→ Artificial intelligence; Machine
learning.
∗Corresponding Author.
Permission to make digital or hard copies of all or part of this work for personal or
classroom use is granted without fee provided that copies are not made or distributed
for profit or commercial advantage and that copies bear this notice and the full citation
on the first page. Copyrights for components of this work owned by others than ACM
must be honored. Abstracting with credit is permitted. To copy otherwise, or republish,
to post on servers or to redistribute to lists, requires prior specific permission and/or a
fee. Request permissions from permissions@acm.org.
Conference acronym ’XX, June 03–05, 2018, Woodstock, NY
© 2018 Association for Computing Machinery.
ACM ISBN 978-1-4503-XXXX-X/18/06. . . $15.00
https://doi.org/XXXXXXX.XXXXXXX
KEYWORDS
Uplift Modeling, Graph Neural Network, Causal Inference
ACM Reference Format:
Haowen Wang, Xinyan Ye, Yikang Wang, Yangze Zhou, Zhiyi Zhang, Long-
han Zhang, and Jing Jiang. 2018. Uplift Modeling based on Graph Neural
Network Combined with Causal Knowledge. In Proceedings of Make sure
to enter the correct conference title from your rights confirmation emai (Con-
ference acronym ’XX). ACM, New York, NY, USA, 6 pages. https://doi.org/
XXXXXXX.XXXXXXX
1 INTRODUCTION
Uplift modeling [8] has traditionally relied on randomized experi-
ments, such as randomized controlled trials (RCTs) [19], in which
customers are randomly allocated to either receive or not receive
the intervention. In such instances, obtaining an accurate and inter-
pretable estimate from observational data becomes critical. How-
ever, carrying out such an experiment in a business context fre-
quently results in several challenges, including high costs in terms
of time and money, uneven intervention distribution, and selection
bias in the specific population.
Response modeling or outcome prediction uses supervised learn-
ing models to model the relation between features and target vari-
ables to predict response variation. Although response modeling
is typically preferable to random targets, distinguishing between
treatment-induced be- behavioral changes is often challenging. The
population that should be targeted is the one most likely to respond
positively to the intervention. As a result, a thorough knowledge of
the behavioral changes that occur after the intervention is essential.
Uplift modeling simulates the causal effect between the intervention
and the outcomes based on response modeling. Causal inference
frameworks and machine learning models are corporated to provide
accurate forecasts and optimized performance on intuitive metrics.
The counterfactual nature of intervention data is central to causal
inference in Rubin’s Potential Outcome Framework (POF) [15]. This
characteristic pertains to a person’s inability to both receive and
arXiv:2311.08434v1  [cs.LG]  14 Nov 2023

Conference acronym ’XX, June 03–05, 2018, Woodstock, NY Wang and Ye, et al.
refuse intervention. This means that the effects of many therapies
cannot be seen in the same person. Two frameworks that have been
extensively examined for causal impact estimations based on this
counterfactual characteristic are the meta-learner framework [17]
and the customised machine learning model-based framework [4].
The ultimate goal is to increase the accuracy of causal impact es-
timation through the use of feature engineering and validation
approaches such as PS matching [3], weighting [11], feature repre-
sentation [13], and so on.
In the past, researchers in uplift modeling were largely concerned
with how to employ unbiased data and models in the estimation
framework. We increased the amount of data information by defin-
ing causal knowledge and implementing structured representation,
then used a graph convolution neural network [21] to efficiently and
directionally integrate feature neighborhood information, achiev-
ing excellent performance in uplift modeling and prediction tasks.
The following is a description of our paper’s contribution to method-
ological and empirical evaluation perspectives:
• First, we propose to use conditional average treatment effect
(CATE) as the attribute representing the causal information of the
feature and as part of uplift modeling and propose a causal network
model framework to effectively calculate it based on knowledge
distilling and double machine learning.
• Second, we propose to learn the causal diagram structure of
the data before uplift modeling and reconstruct the data according
to the learned adjacency matrix.
• Third, we propose an uplift modeling estimator based on graph
convolution neural networks, which can integrate and characterize
neighborhood feature attributes according to the cause and effect
diagram structure and improve the performance of downstream
tasks.
2 RELATED WORK
The estimation of the uplift value in uplift modeling is often based
on the Potential Outcome Framework(POF) [ 15]. The individual
treatment effect(ITE) can be expressed as:
𝐼𝑇𝐸 :𝜏(𝑖) =𝑌𝑖(1)− 𝑌𝑖(0) (1)
Shere𝑌𝑖(1) and𝑌𝑖(0) represents the result of the outcome variable
under the treatment condition and control condition, respectively,
for individual𝑖,𝜏(𝑖) is the ITE value.
Considering that the individual effect of treatment will vary
from individual and the high cost of marketing experiments in
the industry, the conditional average treatment effect(CATE) is
proposed as the effect of treatment on subgroups evaluated by the
conditional average treatment effect (CATE), which is calculated
by:
𝐶𝐴𝑇𝐸 :𝜏𝑖 =𝐸[𝑌𝑖(1)| 𝑋𝑖]−𝐸[𝑌𝑖(0)| 𝑋𝑖] (2)
where𝑋𝑖 is the feature vector for individual𝑖.
For the estimation of CATE and ITE, the most direct method is
to make an unbiased adjustment to the regression model. Series
of meta learners represented by s-learner are designed based on
the concept, that is, train one or more models with y as the output
training target, input T and X, and get the change of Y by changing
the value of T to estimate ITE and CATE.
𝜏(𝑥) =𝐸[𝑌𝑖(1)− 𝑌𝑖(0)|𝑋] =𝐸[𝜏𝑖|𝑋] (3)
Another series of methods for uplift modeling prediction is the
probability score matching (PSM) [3] method based on randomized
controlled trials (RCT) [19]. By calculating the probability score
𝑃(𝑡|𝑥), each sample is given a different treatment object according
to its similarity, so for sample𝑖, we find sample 𝑗:
argmin𝑗 dist(𝑖,𝑗) =

𝑃(𝑡|𝑥𝑖)−𝑃 𝑡|𝑥𝑗 

 (4)
Then CATE could be calculated by:
ˆ𝜏 = 1 𝑛
" ∑︁
𝑖:𝑡𝑖 =1
𝑦𝑖−𝑦𝑗 + ∑︁
𝑖:𝑡𝑖 =0
𝑦𝑗−𝑦𝑖 
#
(5)
In addition, the industry’s research on lift modeling also includes
methods based on the Covariate Balancing Method and Modeling
Unobserved Confounder. Typical methods of the first category
include Inverse Probability of Treatment Weighting (IPTW) [ 7],
Entropy Balancing (EB) [10], and Approximate Residual Balancing
(ARB) [1], in which core is how to re-assign weights to samples. The
core of the second type of method is to model the confounder. One
way is to model the instrumental variable, which is represented by
the two-stage least square (2SLS) method [2]. The first stage is to
fit the impact of the change of I on T, and the second stage is to fit
the impact of the change of T on y caused by the change of I. The
other way is to use deep learning to represent the confounder, such
as SITE [20], Dragonnet [18], and CEVAE [12].
The past research mainly focused on adjusting and optimizing
the uplift value estimation model in a structured or unstructured
way. Estimation methods based on the foundation model have
shown us the importance of embedding causal structure knowledge
into the estimation process. This paper will try to conduct data
mining on features. On the one hand, it expands the amount of
information by defining and applying causal information; on the
other hand, it reconstructs structured origin data through causal
diagram structural information and uses GCN to learn neighbor-
hood information from unstructured reconstructed data to improve
the performance of uplift modeling using the framework of meta
learner [17].
The structure of the paper is as follows. Section II reviews the
critical concepts of uplift modeling and frameworks of the learning
approach. In Section III, we introduce the methodology of our causal
knowledge framework. Section IV evaluates these methods with
both synthetic and real-world data. Finally, Section V summarizes
the findings and recommends future research for uplift modeling
applications.
3 METHODOLOGY
This section will introduce the calculation method and architec-
ture of graph neural networks embedded with causal knowledge.
We propose an interpretable causal graph network representation
learning framework with features as nodes. It can expand the rep-
resentation of features by node embedding, mapping the originally
scalar features into a high-dimension space, and then integrating
the causal information and structural information into the graph

Uplift Modeling based on Graph Neural Network Combined with Causal Knowledge Conference acronym ’XX, June 03–05, 2018, Woodstock, NY
features through graph convolution to achieve a more accurate
estimation of uplift value.
3.1 Causal Knowledge Representation
We propose a framework for computing causal knowledge rep-
resentation. We transfer knowledge through the concept of the
soft target in knowledge distillation as the estimation target of the
causal estimator. We estimate each feature’s causal average treat-
ment effect(CATE) and take it as the weight of the feature based
on the causal effect. This work has been proven to obtain more
information.
Figure 1: Causal Weighting Calculation Framework
Figure 2: Causal Graph for Feature X1
Figure 1 shows the architecture of the causal average treatment
effect(CATE) calculation. Firstly, in the module of knowledge distil-
lation and representation, We will build a knowledge distillation
task for label Y(0/1), using the teacher model(XGBoost [5], etc. as
base regressor) to get the probability ˆ𝑌 as the soft label to replace
Y as the target label. Secondly, in the multi-head causal weight
calculation module, we establish a causal graph for each feature
as shown in Figure 2, use the soft label ˆ𝑌 got in Module 1 as a
knowledge label, and estimate CATE in the framework of double
machine learning (DML) [6]. Since the CATE estimation of each
feature is independent, we designed a multi-head mechanism to
make the calculation more efficient. Double machine learning is
a classic estimator to estimate (heterogeneous) treatment effects
when treatment is classified and all potential confounders/controls.
DML makes the following structural equation assumptions for the
data generation process:
𝑌 =𝜃(𝑋)· 𝑇+𝑔(𝑋,𝑊)+ 𝜖 E[𝜖|𝑋,𝑊] = 0 (6)
𝑇 = 𝑓(𝑋,𝑊)+ 𝜂 E[𝜂|𝑋,𝑊] = 0 (7)
E[𝜂·𝜖|𝑋,𝑊] = 0 (8)
After modeling Y and T, respectively, the estimated CATE value
𝜃(𝑋) satisfies the equation:
˜𝑌 =𝜃(𝑋)· ˜𝑇+𝜖 (9)
Here ˜𝑌 is the residual of Y, ˜𝑇 is the residual of T.
Considering E[𝜖·𝜂| 𝑋] = 0, the problem of estimating 𝜃(𝑋)
can be transformed into the following regression problem.
ˆ𝜃 = arg min
𝜃∈Θ
E𝑛

( ˜𝑌−𝜃(𝑋)· ˜𝑇)2 (10)
3.2 Causal Graph Structure Learning
The graph network structure contains the dataset’s prior infor-
mation. The connection relationship indicates the direction and
distance of information transmission and determines the direction
and degree of information sharing and transmission of nodes in
the subsequent graph network characterization operation.
Here, we use the classical Bayesian network structure as the
structure of the causal feature representation graph. Scoring search
is a standard method to solve the problem of Bayesian network
structure to evaluate the degree of fit between the Bayesian network
and training data and then find the optimal Bayesian network based
on the scoring function. The goal is now to solve the following task:
argmax
𝐺∈𝐺
score(𝐺,D). (11)
The scoring function introduces the inductive preference of what
kind of Bayesian network you want to obtain. Here we use the
Bayesian Information Criterion(BIC) [ 14] as the score function,
which approximates the Bayes Dirichlet equivalent uniform(BDeu),
sharing the critical property of decomposability.
score(𝐺,D) =
∑︁
𝑋𝑖
score(𝑋𝑖, Π𝑖,D) (12)
Score𝑏𝑖𝑐(𝑔 :𝐷) =𝑙(( ˆ𝜃,𝑔) :𝐷)− log𝑀 2 Dim[𝑔] (13)
D is the given data, M is the number of training samples, g is the
given structure, Dim[g] is the number of independent parameters
of model g, ˆ𝜃 is the maximum likelihood estimate of the parameter
given the structure g and the data D.
After determining the scoring function, here we use the hill-
climbing [16] algorithm as the optimization algorithm for the struc-
tural learning problem. The Hill-climbing algorithm is a classical
algorithm for local search based on a greedy algorithm, starting
with a candidate solution and continuing to search in its neighbor-
hood until there is no better solution. The steps of the local search
algorithm are described as follows: Firstly, initialize a feasible solu-
tion X. Secondly, select a moved solution s (x) in the neighborhood
of the current solution so that f (s (x)) < f (x), s (x) in S (x). If there
is no such solution, X is the optimal solution, and the algorithm
stops. Thirdly, make x = s (x) and repeat the second step.
3.3 GNN based uplift modeling
After Causal Knowledge Representation and Causal Graph Struc-
ture Learning, we obtained more information about the dataset
and a specific relationship between features. Considering the excel-
lent representation ability of graph neural networks, we propose a
graph neural network representation framework based on causal

Conference acronym ’XX, June 03–05, 2018, Woodstock, NY Wang and Ye, et al.
graph representation, which can integrate this information more
efficiently.
GCN [21] is a multi-layer neural network that can operate di-
rectly on the graph and induce nodes to obtain information on
neighborhood vectors based on the neighborhood attributes of
nodes. Consider a graph G = (V, e), where V (| V | = n) and E are the
sets of nodes and edges, respectively. It is assumed that each node
is connected to itself, that is, (v, v)∈𝐸 for any v. Let x∈ R𝑛×𝑚 be
a matrix containing all N nodes and their vector features, where
m is the dimension of the vector, and each row 𝑥𝑣∈ R𝑚 are the
vectors of V. We introduce the adjacency matrix A and its degree
matrix D of G, where 𝑑𝑖𝑖 = ˝ 𝑗𝐴𝑖𝑗 . Due to the characteristics of
the self-circulation hypothesis, the diagonal element of a is set to 1.
In general, GCN can only capture information about its neighbors
through one layer of convolution. We can integrate information
about a wider range of neighbors by stacking multiple GCN layers:
𝐻(𝑙+1) =𝜎  ˆ𝐷− 1 2 ˆ𝐴 ˆ𝐷− 1 2𝐻(𝑙)𝑊(𝑙)  (14)
Here𝐻(𝑙+1) and𝐻(𝑙) are the output and input matrices. ˆ𝐴 =𝐴+𝐼,
where A is the adjacency matrix, and I is the identity matrix. ˆ𝐷 is
the degree matrix of ˆ𝐴, ˆ𝐷− 1 2 ˆ𝐴 ˆ𝐷− 1 2 is the normalized symmetric
adjacency matrix, and𝑊(𝑙) ∈ R𝑚×𝑘 is a weight matrix. 𝜎 is an
activation function, e.g., a LeakyReLU.
Here we use GCN to extract and integrate features based on the
causal neighborhood structure we learned in the previous step. We
take advantage of the feature that GCN can efficiently fuse features
according to the neighborhood structure to get graph embedding of
each sample and then perform prediction tasks based on it. Figure 3
shows that we have expanded the information on each feature. In
addition to the value of each feature itself, we have also expanded
the information of structural features and causal weights.
Figure 3: GNN-based uplift modeling architecture.
For the estimation of uplift value, we refer to the design method
of S-learner in meta learner and use our GNN-based model as the
base learner.
𝜇0(𝑥) = E[𝑌(𝑇 = 0)| 𝑋 =𝑥] (15)
𝜇1(𝑥) = E[𝑌(𝑇 = 1)| 𝑋 =𝑥] (16)
After𝜇0 and𝜇1 are calculated, respectively, the uplift value for
each sample can be calculated:
˜𝐷1 𝑖 :=𝑌 1 𝑖 − ˆ𝜇0

𝑋 1 𝑖

(17)
˜𝐷0 𝑖 := ˆ𝜇1

𝑋 0 𝑖

−𝑌 0 𝑖 (18)
Here ˜𝐷1 𝑖 and ˜𝐷0 𝑖 are the uplift values for samples in the interven-
tion group and control group.
4 EXPERIMENTS
4.1 Dataset
4.1.1 Synthetic dataset. We used a method to simulate the gener-
ation of a dataset containing individual treatment effects, which
is available in causalml. In Chen et al. [4] research, it is used as a
method to provide simulated data, which is available in Causalml.
This synthetic method in the study provides the test groundings for
estimating individual treatment effects and facilitating validation.
The following is the generating mechanism: for different choices
of X-distribution𝑃𝑑, there is dimension𝑑, noise level𝜎, propensity
function𝑒∗(·), baseline primary effect𝑏∗(·), and treatment effect
function𝜏∗(·). The distributions and relations are mathematically
expressed in terms:
𝑋𝑖∼𝑃𝑑 (19)
𝜀𝑖|𝑋𝑖∼𝑁(0, 1) (20)
𝑊𝑖|𝑋𝑖∼ Bernoulli 𝑒∗(𝑋𝑖) (21)
𝑌𝑖 =𝑏∗(𝑋𝑖)+(𝑊𝑖− 0.5)𝜏∗(𝑋𝑖)+𝜎𝜀𝑖 (22)
The generation mechanism is featured by nuisance components
and an easy treatment effect function. The initial distribution is
constructed from 𝑋𝑖1∼ 𝑈𝑛𝑖𝑓(0, 1)𝑑 is constructed, followed by
𝑒∗(𝑋𝑖 =𝑡𝑟𝑖𝑚 0.1{𝑠𝑖𝑛(𝜋𝑋𝑖1𝑋𝑖2)} and𝜏∗(𝑋𝑖) =(𝑋𝑖1+𝑋𝑖2)/2 to com-
pute propensity scores and treatment effects, respectively. The
treatment𝑊 is generated as a binary distribution. Eventually, in-
terval trimming of the distribution is performed via 𝑡𝑟𝑖𝑚(𝑥) =
𝑚𝑎𝑥{𝜂,𝑚𝑖𝑛(𝑥, 1−𝜂)}. This simulation method is adpoted as a scaled
version of the Friedman [9] function, where a baseline main effect
is computed through𝑏∗(𝑋𝑖) =𝑠𝑖𝑛(𝜋𝑋𝑖1𝑋𝑖2)+ 2(𝑋𝑖1− 0.5)2+𝑋𝑖4+
0.5𝑋𝑖5.
4.1.2 Real-world dataset. We use the criteo uplift dataset [ 8] as
the evaluation of the real-world dataset, which is constructed by
collecting data from the incremental test. It randomly divides the
people into two categories, whether it is advertised or not. The
criteo uplift dataset has 25 million rows, each representing a user
with 11 characteristics, a treatment indicator, and two tags (click
and conversion). Here we use conversion as the tag we focus on
in uplift estimation. Figure 4 shows the results after learning the
Bayesian network structure of the dataset.

Uplift Modeling based on Graph Neural Network Combined with Causal Knowledge Conference acronym ’XX, June 03–05, 2018, Woodstock, NY
Figure 4: Correlation network between confounders, treat-
ment, and outcome from the real-world dataset, CRITEO
4.2 Result
4.2.1 synthetic dataset. In this case, the actual causal effect of
features can be calculated easily because the datasets are produced
with a certain mechanism The absolute loss ( Abs) is adopted to
measure the deviation between the actual causal effect and the
estimated causal effect. As for the prediction accuracy, the mean
squared error (MSE) is adopted. The proposed method has been
compared to traditional models like linear regression (LR), SVR,
and XGBoost.
Figure 5: Mean squared error for y-prediction accuracy of
base methods and ours with the numbers of confounders are
5, 9, and 20, respectively.
Figure 6: Absolute error of ITE of base methods and ours with
the numbers of confounders are 5, 9 and 20, respectively.
Figure 5 shows that the origin GNN-based model performs simi-
larly to traditional models in the traditional regression task, while
Table 1: AUUC for uplifting evaluation and MSE for y-
prediction of baseline methods and proposed method
Model AUUC MSE
LR 0.4980 0.0026
SVR 0.5475 0.0037
XGBoost 0.8756 0.0025
GCN 0.5443 0.0028
GCN (Causal Weighting) 0.8807 5e-06
the GNN-based model performs much better when combined with
the causal weighting. As for uplift modeling estimation, as shown
in Figure 6, causal weighting combined architecture has a much
more apparent effect. Before combining causal weighting informa-
tion, GNN based model is slightly better than LR and SVR in the
estimation of uplift value but worse than xgboost while achieving
a very accurate result when adopting the causal weighting com-
bined architecture. Another result is that GNN based model can
have a much more stable performance when the number of con-
founders increases, which means that it can have a much more
robust performance when facing more complex situations.
4.2.2 Real-world dataset. In a real-world dataset, the actual causal
effect of treatment remains unknown, leading to the abovemen-
tioned indicators being inapplicable. As a result, Area Under Uplift
Curve (AUUC) is adopted to measure the performance of an uplift-
ing model on the real-world dataset. AUUC can be calculated as
follows:
𝐴𝑈𝑈𝐶(𝑓) =
∫ 1
0
𝑉(𝑓,𝑥)𝑑𝑥≈
𝑛∑︁
𝑘=1
𝑉(𝑓,𝑘) (23)
𝑤ℎ𝑒𝑟𝑒𝑉(𝑓,𝑘) = 1 |𝑇| ∑︁ 𝑖∈𝑓(D,𝑘) 𝑦1 𝑖[𝑡𝑖 =1]− 1 |𝐶| ∑︁ 𝑗∈𝑓(D,𝑘) 𝑦1 𝑗[𝑡 𝑗 =0]
(24)
Here𝑓(D,𝑘) can be the k first samples of the dataset when or-
dered by the prediction of the model𝑓 ,|𝑇| is the number of samples
in the treatment group(t=1), and|𝐶| is the number of samples in
the control group(t=0).
For certain causal relationships, the higher the AUUC is, the
better the uplifting model performs. The AUUC of the baseline
models and ours are listed in Table 1.
Table 1 shows that when estimating the uplift value in the real-
world dataset, although origin GNN has a similar performance with
LR and SVR, it has a better performance than XGBoost when with
the causal weighting combined architecture.
5 CONCLUSION AND FUTURE WORK
In this work, we investigated how to describe causal information in
uplift modeling (add conditional average treatment effect (CATE)
and build an adjacency matrix using Bayesian network structure
learning). In addition, we addressed how to incorporate this causal
information into uplift estimations by proposing a framework for
uplift modeling that is based on graph neural networks.

Conference acronym ’XX, June 03–05, 2018, Woodstock, NY Wang and Ye, et al.
Experiments on simulated and real-world datasets reveal that
while the origin graph convolutional neural network performs
comparably to conventional approaches when directly predicting
uplift values, when paired with causal neighbourhood features
and causal representation information, it demonstrates exceptional
performance in both the prediction job and the uplift estimation
task of the target, owing to the GCN’s excellent neighbourhood
learning features.
It is worthwhile to investigate more methods of characterising
causal knowledge in the future. Weighted adjacent matrices might
be seen as a means of guiding graph convolutional neural networks
to provide accurate data. Alternatively, it is equally intriguing to
investigate the size of the receptive domain of neighbourhood fea-
tures. A wider receptive domain denotes more information, which
might aid us in enhancing the performance of this job in down-
stream prediction.
REFERENCES
[1] Susan Athey, Guido W Imbens, and Stefan Wager. 2018. Approximate residual
balancing. Journal of the Royal Statistical Society. Series B (Statistical Methodology)
80, 4 (2018), 597–623.
[2] Kenneth A Bollen. 1996. An alternative two stage least squares (2SLS) estimator
for latent variable equations. Psychometrika 61, 1 (1996), 109–121.
[3] Marco Caliendo and Sabine Kopeinig. 2008. Some practical guidance for the
implementation of propensity score matching. Journal of economic surveys 22, 1
(2008), 31–72.
[4] Huigang Chen, Totte Harinen, Jeong-Yoon Lee, Mike Yung, and Zhenyu Zhao.
2020. Causalml: Python package for causal machine learning. arXiv preprint
arXiv:2002.11631 (2020).
[5] Tianqi Chen, Tong He, Michael Benesty, Vadim Khotilovich, Yuan Tang, Hyunsu
Cho, Kailong Chen, Rory Mitchell, Ignacio Cano, Tianyi Zhou, et al. 2015. Xgboost:
extreme gradient boosting. R package version 0.4-2 1, 4 (2015), 1–4.
[6] Victor Chernozhukov, Denis Chetverikov, Mert Demirer, Esther Duflo, Christian
Hansen, and Whitney Newey. 2017. Double/debiased/neyman machine learning
of treatment effects. American Economic Review 107, 5 (2017), 261–265.
[7] Nicholas C Chesnaye, Vianda S Stel, Giovanni Tripepi, Friedo W Dekker,
Edouard L Fu, Carmine Zoccali, and Kitty J Jager. 2022. An introduction to
inverse probability of treatment weighting in observational research. Clinical
Kidney Journal 15, 1 (2022), 14–20.
[8] Eustache Diemert, Artem Betlei, Christophe Renaudin, and Massih-Reza Amini.
2018. A large scale benchmark for uplift modeling. In KDD.
[9] Jerome H Friedman, Eric Grosse, and Werner Stuetzle. 1983. Multidimensional
additive spline approximation. SIAM J. Sci. Statist. Comput. 4, 2 (1983), 291–301.
[10] Hainmueller J. 2012. Entropy balancing for causal effects: A multivariate reweight-
ing method to produce balanced samples in observational studies. In Political
analysis. 20(1): 25–46.
[11] Fan Li, Kari Lock Morgan, and Alan M Zaslavsky. 2018. Balancing covariates via
propensity score weighting. J. Amer. Statist. Assoc. 113, 521 (2018), 390–400.
[12] Christos Louizos, Uri Shalit, Joris M Mooij, David Sontag, Richard Zemel, and
Max Welling. 2017. Causal effect inference with deep latent-variable models.
Advances in neural information processing systems 30 (2017).
[13] Krikamol Muandet, David Balduzzi, and Bernhard Schölkopf. 2013. Domain
generalization via invariant feature representation. In International conference on
machine learning. PMLR, 10–18.
[14] Andrew A Neath and Joseph E Cavanaugh. 2012. The Bayesian information cri-
terion: background, derivation, and applications. Wiley Interdisciplinary Reviews:
Computational Statistics 4, 2 (2012), 199–203.
[15] Donald B Rubin. 2005. Causal inference using potential outcomes: Design, mod-
eling, decisions. J. Amer. Statist. Assoc. 100, 469 (2005), 322–331.
[16] Bart Selman and Carla P Gomes. 2006. Hill-climbing search. Encyclopedia of
cognitive science 81 (2006), 82.
[17] Jean-François Ton, Dino Sejdinovic, and Kenji Fukumizu. 2021. Meta learning for
causal direction. In Proceedings of the AAAI Conference on Artificial Intelligence ,
Vol. 35. 9897–9905.
[18] Fung Po Tso, Lin Cui, Lizhuo Zhang, Weijia Jia, Di Yao, Jin Teng, and Dong Xuan.
2013. DragonNet: a robust mobile internet service system for long-distance trains.
IEEE transactions on mobile computing 12, 11 (2013), 2206–2218.
[19] Maureen L Whittal, Sheila R Woody, Peter D McLean, SJ Rachman, and Melisa Ro-
bichaud. 2010. Treatment of obsessions: A randomized controlled trial. Behaviour
research and therapy 48, 4 (2010), 295–303.
[20] Liuyi Yao, Sheng Li, Yaliang Li, Mengdi Huai, Jing Gao, and Aidong Zhang. 2018.
Representation learning for treatment effect estimation from observational data.
Advances in neural information processing systems 31 (2018).
[21] Si Zhang, Hanghang Tong, Jiejun Xu, and Ross Maciejewski. 2019. Graph convo-
lutional networks: a comprehensive review. Computational Social Networks 6, 1
(2019), 1–23.
A APPENDIX
A.1 Code Availability
The code that supports the findings of this study will be available
on GitHub.
