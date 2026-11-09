---
title: 'ACQ: A Unified Framework for Automated Programmatic Creativity in Online Advertising'
url: https://arxiv.org/abs/2412.06167
category: digital-marketing
subcategory: empirical
date: 2024-12
venue: arXiv (Cornell University)
authors:
- Ruizhi Wang
- Kai Liu
- Bingjie Li
source: arxiv
pdf_url: https://arxiv.org/pdf/2412.06167
pages: 16
chars: 38204
fetched_at: '2026-11-08T12:57:25+00:00'
kb_version: 1
---

# ACQ: A Unified Framework for Automated Programmatic Creativity in Online Advertising

ACQ: A Deployed Two-Stage Framework for
Automated Creative Quota Allocation in
Large-Scale Online Advertising
Ruizhi Wang, Yu Rong, Kai Liu, Bingjie Li, Qingpeng Cai⋆, Fei Pan, and Peng
Jiang
1 Huazhong University of Science and Technology, China
wangruizhi@hust.edu.cn
2 Kuaishou Technology, China
rongyu03@kuaishou.com,liukai10@kuaishou.com,libingjie03@kuaishou.com,
caiqingpeng@kuaishou.com,panfei05@kuaishou.com,jiangpeng@kuaishou.com
Abstract.In digital advertising, demand-side platforms (DSPs) allow
advertisers to create multiple ad creatives from a single photo for real-
time bidding. While increasing the number of creatives can improve bid-
ding opportunities, it cannot scale indefinitely, and the incremental ad-
vertising revenue typically exhibits diminishing returns as more creatives
are generated. This raises a practical problem for DSPs: how to automat-
ically determine an appropriate creative quota for each photo at scale. To
address this problem, we propose Automated Creatives Quota (ACQ), a
deployed two-stage framework for creative quota allocation in large-scale
online advertising. In the first stage, ACQ predicts quota-conditioned ex-
pected revenue using a multi-task model built on an unbalanced binary
tree, which is designed to handle the highly skewed revenue distribution
across quota levels. In the second stage, ACQ formulates quota allocation
under global capacity constraints as a multiple-choice knapsack problem
(MCKP) and solves it with an efficient dual-based algorithm. Extensive
offline experiments and online experiments on Kuaishou’s advertising de-
livery platform demonstrate the effectiveness of ACQ, achieving a 6.20%
increase in platform advertising revenue.
Keywords:Online advertising·Creative quota allocation·Structured
revenue prediction·Large-scale allocation.
1 Introduction
Online advertising is a major revenue source for Internet companies [9]. To im-
prove campaign effectiveness and reduce manual operations, major platforms
such as Google, Amazon, Tencent, ByteDance and Kuaishou have developed
sophisticated demand-side platforms (DSPs) for strategy automation, ad de-
livery optimization, and real-time bidding [7,12]. In modern advertising sys-
tems, advertisers typically manage three hierarchical levels within an account—
campaigns, units, and creatives—and must decide how many creatives should be
⋆ Corresponding author.
arXiv:2412.06167v2  [cs.AI]  21 Aug 2026

2 R. Wang et al.
campaigns
creatives
units
photo
account
advertiser
Fig.1: Hierarchical structure in an advertising system. From top to bottom,
the hierarchy includes advertiser, account, campaign, unit, and creative. Each
creative is generated from a single photo, while one photo can be expanded into
multiple creatives by combining different titles or themes.
generated for each photo. As illustrated in Figure 1, a single photo can be used to
generate multiple creatives by combining different titles, themes, or templates.
Generating multiple creatives from the same photo can improve bidding op-
portunities because different creatives may appeal to different audiences [4].
However, assigning more creatives to a photo does not lead to unlimited gains.
From the DSP perspective, two practical issues must be considered. First, the
number of creatives cannot grow indefinitely because platform resources are fi-
nite, and creating too many creatives may aggravate data sparsity, since many
newly generated creatives receive little or no traffic. Second, the incremental
advertising revenue brought by additional creatives usually diminishes as the
creative quota increases, due to audience overlap and competition among sim-
ilar creatives. Therefore, an important practical problem is to automatically
determine an appropriate creative quota for each photo.
In this paper, we study thecreative quota allocation problem, which aims to
optimize the number of creatives generated from each photo so as to maximize
total advertising revenue under platform constraints. This problem is challeng-
ing for three reasons. First, the target variable is extremely imbalanced: on any
given day, more than 90% of photos receive zero ad revenue, which makes di-
rect prediction difficult. Second, standard regression models do not explicitly
capture the structured relationship between ad revenue and creative quota. In
practice, this relationship is expected to satisfy several intuitive properties, in-
cludingmonotonicity,submodularity,andlocalsmoothness.Third,theallocation
problem must be solved at very large scale, involving on the order of ten million

ACQ: A Deployed Two-Stage Framework for Creative Allocation 3
photos, which places substantial demands on memory usage and computational
efficiency.
To address these challenges, we propose a two-stage framework calledAu-
tomated Creatives Quota (ACQ). The first stage learns the expected ad
revenue of each photo under different creative quotas from historical data. To
handle the severe target imbalance while preserving the structured relationship
across quota levels, we develop a multi-task prediction model based on an un-
balanced binary tree. The second stage allocates creative quotas under business
constraints based on the predicted ad revenue. We formulate this allocation
stage as a large-scale optimization problem and design an efficient solver based
on Lagrangian optimization and bisection, making ACQ practical for industrial
deployment.
Our main contributions are summarized as follows:
–We formulate a practical and commercially importantcreative quota al-
location problemfor automated ad creative creation and deactivation in
DSP systems.
–We propose ACQ, a two-stage “prediction + allocation” framework that
jointly models quota-dependent expected ad revenue and large-scale quota
allocation.
–We develop a multi-task prediction model based on an unbalanced binary
tree to address severe target imbalance while encoding desirable structural
properties, including monotonicity, submodularity, and smoothness.
–We design an efficient large-scale allocation solver based on Lagrangian op-
timization with bisection, enabling deployment on Kuaishou for problems
involving tens of millions of candidate photos.
–We validate ACQ through extensive offline experiments on real-world data
and online A/B testing in production on Kuaishou’s advertising delivery
platform, where it consistently outperforms strong baselines.
The rest of this paper is organized as follows. Section 2 reviews related work.
Section 3 formulates the creative quota allocation problem. Section 4 presents
the proposed ACQ framework. Section 5 reports the datasets and experimental
results. Section 6 concludes the paper.
2 Related Work
Creative Automation in Digital Advertising.Digital advertising is a major appli-
cation of machine learning, and creative production is a key factor in campaign
performance [6,10]. Existing AI applications in the creative pipeline mainly in-
clude dynamic creative optimization (DCO) and programmatic advertising cre-
ation (PAC). DCO focuses on adapting or selecting creative content according
to user behavior and contextual signals [5,16], while PAC emphasizes the au-
tomated generation of ad creatives from large material libraries [13]. However,
these studies mainly address creative generation or selection quality, rather than
deciding how many creatives should be generated from a single photo under
platform constraints. Our work instead studies creative quota allocation.

4 R. Wang et al.
Input
Account-Photo
Pairs
Feature X
Sparse Features
• product name
• first industry
• second industry
• ...
Dense Features
Hist, revenue, conv.,
impressions over
multiple windows
Candidate Quotas
1 2 ••• 200
(a) Target Decomposition
Root
(All S)
S = 0
( >90%) S > 0
•••
•••
•••
••• •••
（ b ） UBTM Prediction Module
X q
Embedding Layer
Hidden MLP Layers
Multi-Head Outputs
  Cumulative Sum Head
  (Monotonicity)
  Reverse Cumsum Head
  (Submodularity)
  Lipschitz Regularizer
  (Smoothness)
Output:                                     (Revenue + Exploration)
（ c ） DBSSolver Allocation Module
MCKP Formulation
Photo 1 Photo 2 ••• Photo n
Dual Decomposition
Per-Photo Optimization
Capacity Residual
Bisection Search
Output
Quota
Allocation
Fig.2: Overview of ACQ. The framework consists of a prediction module
(UBTM) for quota-conditioned ad-revenue estimation and an allocation mod-
ule (DBSSolver) for large-scale creative quota allocation.
Imbalanced and Structured Prediction.Learning from highly imbalanced tar-
gets remains challenging for deep models [26,2]. Existing approaches include
resampling, reweighting, multi-stage training, and target transformation [28,27,
20]. Tree-structured decomposition has also shown promise for handling ordered
or imbalanced prediction targets [18]. In many practical decision systems, pre-
dictive functions are further expected to satisfy structural properties such as
monotonicity, smoothness, and submodularity [23,21]. Prior work has incorpo-
rated such properties through parametric function design, order-based losses, or
constrained architectures [19,30,7,8,25]. Our setting combines both challenges:
the target is highly imbalanced, while the quota-conditioned ad-revenue function
should also satisfy meaningful structural constraints.
Large-Scale Constrained Allocation.Thesecondstageofourframeworkisrelated
to large-scale constrained decision-making, especially multiple-choice knapsack
optimization and its Lagrangian relaxation [14]. Prior work has applied this for-
mulation to industrial allocation tasks such as budget allocation and constrained
decision systems [17,1,30,23]. Efficient dual optimization methods, including
gradient-based updates and bisection-based solvers, have made such approaches
practical at scale [30,23]. Our work builds on this line of research but focuses
on a different application: allocating creative quotas for millions of photos based
on predicted quota-dependent ad revenue.
3 Problem Formulation
We formulate thecreative quota allocation problemas a multiple-choice knapsack
problem (MCKP). For each account-photo pair, the platform must choose one

ACQ: A Deployed Two-Stage Framework for Creative Allocation 5
creative quota, i.e., the number of creatives to be generated from that photo.
The goal is to maximize the total expected advertising revenue under a global
capacity constraint on the total number of creatives.
Let(i, j)denote an account-photo pair, wherei∈ {1, . . . , I}indexes adver-
tiser accounts andj∈ {1, . . . , Ji}indexes photos under accounti. For each pair
(i, j), we consider a set of candidate creative quota levelsQ={q1, q2, . . . , qK},
whereq k is the number of creatives assigned under optionk. In our production
system, the maximum quota is 200, soQ={1,2, . . . ,200}.
For each account-photo pair(i, j)and quota optionqk, letx ijk ∈ {0,1}be
a binary decision variable, wherex ijk = 1indicates that quotaq k is selected
for pair(i, j), andx ijk = 0otherwise. Letv ijk denote the allocation value of
assigning quotaq k to pair(i, j). The optimization problem is formulated as
max
IX
i=1
JiX
j=1
KX
k=1
vijk xijk
s.t.
IX
i=1
JiX
j=1
KX
k=1
qkxijk ≤B,
KX
k=1
xijk = 1,∀i, j,
xijk ∈ {0,1},∀i, j, k,
(1)
whereBis the global capacity budget for the total number of creatives. The
first constraint limits the total number of allocated creatives, while the second
ensures that exactly one quota level is selected for each account-photo pair.
The allocation valuevijk is defined as
vijk = ˆSijk +λ eijk ,(2)
where ˆSijk is the predicted expected ad revenue for pair(i, j)under quotaqk,
produced by the first-stage prediction model, andeijk is an exploration score.
Theexplorationscoreisconstructedbasedontheupperconfidencebound(UCB)
principle [3] to balance exploitation and exploration in deployment. The coeffi-
cientλ≥0controls the strength of the exploration term.
4 Methodology
In this section, we present the details of ACQ, as illustrated in Figure 2. In the
prediction module, we address the challenge of unbalanced target variables and
examine network properties to ensure monotonicity, submodularity, and smooth-
ness. In the allocation module, we tackle the large-scale allocation problem using
a Lagrangian dual optimization method with bisection.

6 R. Wang et al.
4.1 Prediction Module
ModelingwithanunbalancedbinarytreeThepredictionmoduleestimates
the expected ad revenue of an account-photo pair under different creative quotas.
Let the training set beD={(X t, qt, St)}m t=1, wheremdenotes the total number
of samples in the dataset,Xt denotes the input features,qt the creative quota,
andS t the observed ad revenue. The goal of the first stage is to learn a quota-
conditioned predictor ˆS(X, q). A major challenge is that the target distribution
is highly imbalanced: many samples have zero ad revenue, while the positive
values are heavy-tailed, making standard regression unstable on low-frequency
but high-value regions [26].
To address this issue, we propose anUnbalanced Binary Tree Model
(UBTM). The key idea is to decompose the ad-revenue target space into a
hierarchy of binary classification tasks, which serves as auxiliary supervision in
a multi-task framework. This design is inspired by tree-based neural models such
as TDM [31] and TPM [18], which are effective for skewed data distributions.
Specifically, we construct an unbalanced binary treeTover the target vari-
ableS. The root node covers the full support of ad revenue values. Its left child
is a singleton node corresponding to zero ad revenue, while the right subtree
recursively partitions the positive target region. To better fit the long-tail dis-
tribution, the leaf nodes in the positive subtree are built by equal-frequency
partitioning over samples withS >0. Thus, each node corresponds to either a
singleton set or an interval of ad revenue values.
Suppose the tree hasNnodes andN f leaf nodes. Each internal node is
associated with a binary classifier, resulting inN−N f auxiliary classification
tasks. For any nodeNk, letp k ={N (0) k ,N (1) k , . . . ,N(d(k)) k }denote the path from
the root toN k, whered(k)is its depth. Then the probability that the target
falls into nodeNk can be factorized as
P(S∈ Nk |X, q, T) =
d(k)Y
t=1
P

S∈ N(t) k |S∈ N(t−1) k , X, q, T  .(3)
For a leaf node, this probability represents the likelihood that the target ad
revenue falls into the corresponding interval.
Multi-task learningWe train UBTM in a multi-task manner [29], where the
main task is quota-conditioned ad-revenue regression and the auxiliary tasks are
derived from the internal nodes of the unbalanced binary tree. This design allows
the model to exploit hierarchical supervision over the highly imbalanced target
space and improves generalization across different regions of the ad-revenue dis-
tribution.
For the training setD={(X t, qt, St)}m t=1, the target valueSt of each sample
tis assigned to a leaf node, which uniquely determines a root-to-leaf path. Each
internal node on this path defines a binary auxiliary classification label. Suppose
the tree containsN−N f internal nodes. For an auxiliary taska∈ {1, . . . , N−

ACQ: A Deployed Two-Stage Framework for Creative Allocation 7
Nf }, letz t,a ∈ {0,1}be the binary label for samplet,ˆp t,a be the predicted
conditional probability, andmt,a ∈ {0,1}be an indicator of whether nodealies
on the path of samplet. The auxiliary classification loss is defined as:
Ltree = 1 m
mX
t=1
N−N fX
a=1
mt,a [−zt,a log ˆpt,a −(1−z t,a) log(1−ˆpt,a)].(4)
In addition to hierarchical classification, we use a regression head to predict
the observed ad revenue. LetˆSt denote the predicted ad revenue for samplet.
The main regression loss is
Lreg = 1 m
mX
t=1
(St − ˆSt)2.(5)
We further introduce an auxiliary uncertainty term following prior work on
tree-based prediction [18]. Specifically, we define
σt =
p
E(S 2 |X t, qt, T)−E(S|X t, qt, T)2,(6)
which estimates the conditional standard deviation induced by the tree-based
output distribution. The average uncertainty loss is then defined as:
Lunc = 1 m
mX
t=1
σt.(7)
This term provides a measure of predictive uncertainty and serves as an auxiliary
regularizer during training.
The final training objective is
L=α 1Ltree +α 2Lunc +α 3Lreg,(8)
whereL tree andL reg denote the tree-based loss and regularization term, respec-
tively. In our experiments, we setα 1 = 1,α 2 = 1, andα 3 = 0.2. Although
adaptive weighting methods are available [15], we found the model to be rela-
tively stable under moderate variations of these coefficients in offline tuning.
Modeling Structured PropertiesIn this section, we model the functional
relationship between the creative quota of a photo and its corresponding ad
revenue. For each sample(X, q, S),Xcontains both sparse and dense features,q
denotes the creative quota, andSis the observed ad revenue. Our goal is to learn
a quota-conditioned response functionf(X, q)≈E[S|X, q], while enforcing
several structural properties that are consistent with domain knowledge.
For a given photoP, letfP (q)denote its expected ad revenue under creative
quotaq. We define the photo-level ad revenue under quotaqas the total revenue
accumulated over the creatives generated from that photo. Based on the serving
mechanism of advertising systems, where bidding and delivery are performed at
the creative level, this aggregated quantity provides a natural target for quota
allocation.

8 R. Wang et al.
Monotonicity.A larger creative quota should not reduce the expected ad
revenue of the same photo. Therefore, for anyq 1 < q2, we expectf P (q1)≤
fP (q2).
To enforce this property, we adopt a multi-head architecture. The first output
head predicts the base ad revenue under quota1, while each subsequent head
predicts a non-negative increment relative to the previous quota level. Formally,
letg 1(X)be the output of the first head and letgk(X),k≥2, be the raw outputs
of the increment heads. We define the prediction under quotakas
ˆS(X, k) =
(
g1(X), k= 1,
g1(X) +Pk t=2 ϕ  gt(X)  , k >1, (9)
whereϕ(·)is a non-negative activation function. In our implementation, we use
ϕ(z) =z 2, so that every increment is non-negative by construction. As a result,
ˆS(X, k)is monotone non-decreasing with respect to the quota levelk.
Submodularity.In practice, adding more creatives to the same photo usu-
ally yields smaller and smaller gains because different creatives often compete
for overlapping audiences. Therefore, besides monotonicity, we also expect the
quota-response function to exhibit diminishing marginal returns. Formally, for
a given photoP, define the marginal gain at quota levelkas
∆P (k) =fP (k)−f P (k−1), k≥2.
We expect
∆P (k+ 1)≤∆ P (k),∀k≥2.
To enforce this structure, we parameterize the quota-dependent increments
in reverse order. Letdk(X)denote the increment from quotak−1to quotak.
We require
d2(X)≥d 3(X)≥ · · · ≥dK(X)≥0.
Specifically, lethk(X)be the raw output of thek-th decrement head and letψ(·)
be a non-negative activation function. We define
dK(X) =ψ(h K(X)),(10)
and for2≤k < K,
dk(X) =d k+1(X) +ψ(hk(X)).(11)
Sinceψ(h k(X))≥0, the resulting increments are non-increasing as the quota
level grows. The final prediction is then
ˆS(X, k) =ˆS(X,1) +
kX
t=2
dt(X), k≥2,(12)
which guarantees both monotonicity and submodularity by construction.

ACQ: A Deployed Two-Stage Framework for Creative Allocation 9
Smoothness.Wealsoencouragethelearnedresponsefunctiontovarysmoothly.
This is desirable in practice because abrupt changes across neighboring quota
levels often indicate overfitting or unstable extrapolation. Instead of imposing
a hard smoothness constraint on the discrete quota-response curve, we regu-
larize the Lipschitz constant of the network following prior work on Lipschitz-
constrained neural models [22,11].
Letz j denote the spectral norm of the weight matrix in thej-th fully con-
nected layer, and letLbase denote the original training objective. We define the
Lipschitz regularization term as
Llip =
JY
j=1
softplus(zj),(13)
whereJis the number of fully connected layers andsoftplus(z) = log(1 +e z)
ensures non-negativity. The final smoothness-regularized objective is
Lsmoo =L+λ lipLlip,(14)
whereλ lip controls the strength of the regularization. This regularizer does not
strictly enforce smoothness across quota levels, but it improves the stability of
the learned mapping and empirically leads to smoother quota-response predic-
tions.
4.2 Allocation Module
The creative quota allocation problem defined in Eq. 1 is a multiple-choice knap-
sack problem (MCKP), which is combinatorial and difficult to solve directly at
very large scale. To obtain an efficient industrial solver, we first relax the binary
decision variables to the continuous interval[0,1]. The relaxed problem is
max
IX
i=1
JiX
j=1
KX
k=1
vijk xijk
s.t.
IX
i=1
JiX
j=1
KX
k=1
qkxijk ≤B,
KX
k=1
xijk = 1,∀i, j,
0≤x ijk ≤1,∀i, j, k.
(15)
Since Eq. 15 is a feasible linear program, strong duality holds, and the KKT
conditions are necessary and sufficient for optimality. Introducing a nonnegative
dual variableµ≥0for the global capacity constraint, we obtain the Lagrangian
L(X, µ) =
IX
i=1
JiX
j=1
KX
k=1
vijk xijk +µ

B−
IX
i=1
JiX
j=1
KX
k=1
qkxijk

 .(16)

10 R. Wang et al.
The corresponding dual function is
ϕ(µ) = max
X
L(X, µ),(17)
and the dual problem isminµ≥0 ϕ(µ).
For a fixedµ, the optimization overXdecomposes across account-photo
pairs. Specifically, for each pair(i, j), we solve
max
{xijk }K k=1
KX
k=1
(vijk −µq k)xijk s.t.
KX
k=1
xijk = 1,0≤x ijk ≤1.
Therefore, the optimal quota choice for pair(i, j)is
k∗(i, j;µ) = arg max
k

vijk −µq k

,(18)
and the corresponding solution is one-hot:
xijk ∗ = 1, x ijk = 0fork̸=k ∗.
Hence, although the problem is relaxed, the optimal solution to each Lagrangian
subproblem remains integral.
Define the capacity residual function
g(µ) =
IX
i=1
JiX
j=1
KX
k=1
qkxijk (µ)−B,(19)
wherex ijk (µ)is the optimal solution induced by Eq. 18. The following proposi-
tion shows thatg(µ)is monotone.
Proposition 1.g(µ)is monotone non-increasing with respect toµ.
Proof.Fix any account-photo pair(i, j)and omit the indices(i, j)for brevity.
Letk 1 andk 2 be the optimal quota indices under dual variables0< µ1 < µ2,
respectively. By optimality,
vk1 −µ 1qk1 ≥v k2 −µ 1qk2 ,
and
vk2 −µ 2qk2 ≥v k1 −µ 2qk1 .
Adding the two inequalities yields
(µ2 −µ 1)(qk1 −q k2 )≥0.
Sinceµ 2 > µ1, we obtainqk1 ≥q k2. Therefore, the selected quota for each pair
is non-increasing inµ. Summing over all pairs givesg(µ1)≥g(µ 2).
which proves thatg(µ)is monotone non-increasing.
By complementary slackness, the optimal dual variableµ∗ satisfies
µ∗ g(µ∗) = 0.(20)
Becauseg(µ)is monotone non-increasing, we can efficiently search forµ ∗ via
bisection. Following this idea, we adopt a dual-based binary search solver (DB-
SSolver) [30] to obtain a near-optimal large-scale allocation solution.

ACQ: A Deployed Two-Stage Framework for Creative Allocation 11
5 Experiments
5.1 Dataset
We evaluate ACQ on a real-world dataset collected from Kuaishou’s large-scale
intelligent advertising delivery platform. Each sample corresponds to an account-
photo pair under a given creative quota, with the target defined as the observed
ad revenue over the evaluation window. The dataset contains approximately 60
million samples. As shown in Table 1, the target distribution is highly skewed,
with a median of 0 and a long positive tail, which is consistent with the zero-
heavy ad-revenue prediction setting studied in this paper.
Table 1: Dataset statistics.
Data Size Mean Median Std. Min Max
60M 0.81 0.00 40.10 0.00 20000.00
Sparse features product name, first industry name, second industry name
Dense features historical ad revenue, target ad revenue, conversion, and
impression statistics over multiple time windows
5.2 Offline Experiments
We conduct offline evaluation of ACQ for both the prediction and allocation
modules using production logs, where training and validation are performed on
temporally consecutive data slices.
Baselines.
– UBTM: Our proposed model based on an unbalanced binary tree.
– DNN: A standard deep regression model trained with mean squared error.
– ZILN[24]: A deep model trained with the zero-inflated log-normal loss,
which is widely used for zero-heavy value prediction.
– CREAD[20]: A discretization-based method that transforms continuous
labels into multiple intervals, trains multiple binary classifiers, and recon-
structs the final prediction.
Evaluation metrics.
– MSE: Measures the average squared error between predicted and observed
ad revenue.
– AUC: Evaluates the model’s ability to separate zero-ad-revenue samples
from positive-ad-revenue samples.
– PAUC: Measures ranking quality within the positive-ad-revenue subset,
which is more sensitive to the ordering of valuable samples.
– GAUC: A grouped AUC weighted by account-level ad revenue, which em-
phasizes performance on high-value accounts.

12 R. Wang et al.
Table 2: Offline prediction results on the real-world dataset.
Main Method Variant AUC↑MSE↓PAUC↑GAUC↑
ZILN [24] - 0.927180 NaN* 0.240395 0.653189
CREAD [20] - 0.806779 980.21 0.573294 0.623219
DNN
control 0.884369 820.91 0.740429 0.689695
mon 0.904987 777.41 0.741367 0.678157
sub 0.905742 885.67 0.741194 0.682286
smo 0.906678 821.62 0.740722 0.682286
UBTM (ours)
control 0.926627 812.98 0.745376 0.682656
mon 0.930778 852.23 0.736744 0.675737
sub0.933521783.630.745545 0.689926
smo 0.924065749.760.725943 0.663382
* Extremely large predictions lead to numerical overflow when computing squared errors.
(1.00, 0.20, 1.00) (1.00, 0.50, 1.00) (1.00, 0.80, 1.00) (1.00, 1.00, 1.00)
Parameter setting (α1, α2, α3)
0.88
0.90
0.92
0.94
0.96AUC
Max AUC fluctuation ≤ 0.016
Nleaf = 9 Nleaf = 17 Nleaf = 33
(1.00,0.20,1.00) (1.00,0.50,1.00) (1.00,0.80,1.00) (1.00,1.00,1.00)
Parameter setting (α1, α2, α3)
0.0
0.2
0.4
0.6
0.8
1.0GAUC / PAUC
GAUC Δ=0.010 | PAUC Δ=0.016 | MSE Δ=165
GAUC PAUC MSE
500
600
700
800
900
1000
MSE
Fig.3: Sensitivity analysis of ACQ under different loss weights and tree sizes.
Experimental conclusions.Table 2 reports the offline performance of the predic-
tion module. Here, “mon”, “sub”, and “smo” denote the incorporation of mono-
tonicity, submodularity, and smoothness, respectively, while “control” denotes
the base model without these structural designs.
Several observations can be drawn. First, UBTM consistently outperforms
the non-tree baselines on most ranking-oriented metrics, which validates the ad-
vantage of hierarchical target modeling for highly skewed ad-revenue prediction.
In particular,UBTM-subachieves the best AUC, PAUC, and GAUC, suggest-
ing that modeling monotonicity together with diminishing marginal returns is
beneficial for identifying high-value samples. Second, compared with the DNN
variants, UBTM generally provides a better balance between regression accuracy
andrankingquality,indicatingthattheunbalancedbinarytreeoffersamoresuit-
able inductive bias for zero-heavy and long-tailed ad-revenue data. Third, the
smoothness constraint improves MSE for UBTM but degrades ranking-oriented

ACQ: A Deployed Two-Stage Framework for Creative Allocation 13
Table 3: Solver efficiency comparison between GLPK and the DBSSolver.
Dataset Size GLPK DBSSolver(ours)
Dual (×10−4) Time (min) Dual (×10 −4) Time (min)
100k 6.3316 69.6 6.3324 1.83
200k 6.3312 312.0 6.3324 1.84
500k 6.3305 2174.4 6.3324 1.94
Table 4: Offline allocation results.
Date Ad revenue uplift Creatives uplift ACQ ad revenue Rule-based ad revenue ACQ creatives Rule-based creatives
Day122.72%0.04%27,92722,75659,06159,039
Day216.80%0.20%33,44928,63858,35558,242
Day318.64%-0.25%20,35517,15758,92359,073
Day427.23%0.04%25,68720,19062,67162,645
Day526.51%-0.13%30,89324,42064,42264,506
Day610.61%0.30%18,87917,06464,89164,698
Day711.96%0.02%21,95719,61169,33269,319
Day816.30%-0.40%29,12325,04174,51174,809
Note:All ad revenue and creative counts are reported in thousands (k).
metrics, suggesting that smoothness regularization may improve numerical fit
while being less aligned with the downstream allocation objective.
Table 3 compares the proposed DBSSolver with GLPK. DBSSolver achieves
nearly identical dual values while reducing runtime by more than an order of
magnitude, and its advantage becomes more pronounced as the problem size
increases. These results confirm that the proposed solver is suitable for large-
scale deployment.
Table 4 presents the offline allocation results. Under an almost identical total
number of allocated creatives, ACQ consistently yields higher ad revenue than
the rule-based strategy across all evaluation days. This shows that the gain
mainly comes from better quota allocation rather than simply assigning more
creatives. The ad-revenue uplift ranges from 10.61% to 27.23%, with an average
improvement of 18.08%.
Parameter sensitivity.Figure 3 shows that UBTM is relatively robust to the
number of leaf nodes in the unbalanced binary tree and to the choice of multi-
task loss weights. The performance varies only moderately across a reasonable
range of hyperparameter settings.
5.3 Online Experiments

14 R. Wang et al.
advertiser Users
provide
all photos
ACQ Service Retrieval Ranking Mix Ranking
all photos
model decision
UBTM
DBSSolver
candidate creatives candidate creatives
candidate creatives
mapping quota to hierarchical structure
campaign quota
unit quota
creative quota
display
Fig.4: Offline-to-online serving workflow of ACQ.
Online FrameworkFigure 4 shows the online serving workflow of ACQ. Of-
fline, UBTM and the DBSSolver determine creative quotas for account-photo
pairs, which are then mapped to the hierarchical campaign–unit–creative struc-
ture and stored in Redis. Online, the advertising system retrieves these allocation
results to support retrieval, ranking, and mix-ranking for candidate creative gen-
eration and delivery.
A/B Test ResultsThe ACQ framework was deployed on Kuaishou’s advertis-
ing platform, where a 30-day A/B test was conducted to evaluate its effective-
ness.. The A/B test results show a 6.20% increase in actual ad revenue, a 4.46%
reduction in the total number of creatives, a 14.86% increase in active creatives,
a 0.15% decrease in the total number of photos, and a 6.24% increase in ac-
tive photos. These results indicate that the ACQ framework optimizes resource
allocation, improving cost efficiency by reducing redundant creatives while en-
hancing the proportion of active creatives and photos.
6 Conclusion
In this paper, we proposed ACQ, a two-stage framework for the creative quota
allocation problem in digital advertising. ACQ aims to determine how many cre-
atives should be generated from each photo so as to improve total ad revenue
under platform capacity constraints. In the first stage, we developed UBTM, a
multi-task prediction model based on an unbalanced binary tree, to address the
highly skewed ad-revenue distribution while incorporating desirable structural
properties such as monotonicity and submodularity. In the second stage, we for-
mulated quota allocation as a large-scale optimization problem and designed an
efficient dual-based solver, DBSSolver, to obtain practical solutions for industrial
deployment. Extensive offline experiments and online A/B tests on Kuaishou’s
advertising delivery platform demonstrated the effectiveness of ACQ, showing
that it improves ad revenue while enabling more efficient creative allocation at
scale.

ACQ: A Deployed Two-Stage Framework for Creative Allocation 15
References
1. Ai, M., Li, B., Gong, H., Yu, Q., Xue, S., Zhang, Y., Zhang, Y., Jiang, P.: Lbcf:
A large-scale budget-constrained causal forest algorithm. In: Proceedings of the
ACM Web Conference 2022. pp. 2310–2319 (2022)
2. Alvis, C.D., Seneviratne, S.: A survey of deep long-tail classification advancements.
ACM Comput. Surv.1(1), 35 (April 2024)
3. Auer, P.: Finite-time analysis of the multiarmed bandit problem (2002)
4. Azimi, J., Zhang, R., Zhou, Y., Navalpakkam, V., Mao, J., Fern, X.: The impact of
visual appearance on user response in online display advertising. In: proceedings
of the 21st international conference on World Wide Web. pp. 457–458 (2012)
5. Baardman, L., Fata, E., Pani, A., Perakis, G.: Dynamic creative optimization in
online display advertising. Available at SSRN 3863663 (2021)
6. Chen, G., Xie, P., Dong, J., Wang, T.: Understanding programmatic creative: The
role of ai. Journal of Advertising48(4), 347–355 (2019)
7. Chen, X., Liu, Z., Yu, L., Li, S., Gu, L., Zeng, X., Tan, Y., Gu, J.: Adversarial
learningforincentiveoptimizationinmobilepaymentmarketing.In:Proceedingsof
the 30th ACM international conference on information & knowledge management.
pp. 2940–2944 (2021)
8. Chin, R., Manzie, C., Ira, A., Nesic, D., Shames, I.: Gaussian processes with mono-
tonicity constraints for preference learning from pairwise comparisons. In: 2018
IEEE Conference on Decision and Control (CDC). pp. 1150–1155. IEEE (2018)
9. Choi, H., Mela, C.F., Balseiro, S.R., Leary, A.: Online display advertising markets:
A literature review and future directions. Information Systems Research31(2),
556–575 (2020)
10. Ford, J., Jain, V., Wadhwani, K., Gupta, D.G.: Ai advertising: An overview and
guidelines. Journal of Business Research166, 114124 (2023)
11. Gouk, H., Frank, E., Pfahringer, B., Cree, M.J.: Regularisation of neural networks
by enforcing lipschitz continuity. Machine Learning110, 393–416 (2021)
12. Guo, L., Jin, J., Zhang, H., Zheng, Z., Yang, Z., Xing, Z., Pan, F., Niu, L., Wu, F.,
Xu, H., et al.: We know what you want: An advertising strategy recommender sys-
tem for online advertising. In: Proceedings of the 27th ACM SIGKDD Conference
on Knowledge Discovery & Data Mining. pp. 2919–2927 (2021)
13. Guo, S., Jin, Z., Sun, F., Li, J., Li, Z., Shi, Y., Cao, N.: Vinci: an intelligent graphic
design system for generating advertising posters. In: Proceedings of the 2021 CHI
conference on human factors in computing systems. pp. 1–17 (2021)
14. Kellerer, H., Pferschy, U., Pisinger, D., Kellerer, H., Pferschy, U., Pisinger, D.: The
multiple-choice knapsack problem. Knapsack problems pp. 317–347 (2004)
15. Kendall, A., Gal, Y., Cipolla, R.: Multi-task learning using uncertainty to weigh
losses for scene geometry and semantics. In: Proceedings of the IEEE conference
on computer vision and pattern recognition. pp. 7482–7491 (2018)
16. Koren, Y., Somekh, O., Shahar, A., Itzhaki, A., Cohen, T., Krasteva, M., Shadi, T.:
Dynamic creative optimization in verizon media native advertising. In: 2020 IEEE
International Conference on Big Data (Big Data). pp. 1654–1662. IEEE (2020)
17. Li, L., Sun, L., Weng, C., Huo, C., Ren, W.: Spending money wisely: Online elec-
tronic coupon allocation based on real-time user intent detection. In: Proceedings
of the 29th ACM International Conference on Information & Knowledge Manage-
ment. pp. 2597–2604 (2020)

16 R. Wang et al.
18. Lin, X., Chen, X., Song, L., Liu, J., Li, B., Jiang, P.: Tree based progressive re-
gression model for watch-time prediction in short-video recommendation. In: Pro-
ceedings of the 29th ACM SIGKDD Conference on Knowledge Discovery and Data
Mining. pp. 4497–4506 (2023)
19. Liu, Z., Wang, D., Yu, Q., Zhang, Z., Shen, Y., Ma, J., Zhong, W., Gu, J., Zhou, J.,
Yang, S., et al.: Graph representation learning for merchant incentive optimization
in mobile payment marketing. In: Proceedings of the 28th ACM International
Conference on Information and Knowledge Management. pp. 2577–2584 (2019)
20. Sun, J., Ding, Z., Chen, X., Chen, Q., Wang, Y., Zhan, K., Wang, B.: Cread: A
classification-restoration framework with error adaptive discretization for watch
time prediction in video recommender systems. In: Proceedings of the AAAI Con-
ference on Artificial Intelligence. vol. 38, pp. 9027–9034 (2024)
21. Sun, Z., Yang, H., Liu, D., Weng, Y., Tang, X., He, X.: End-to-end cost-effective
incentive recommendation under budget constraint with uplift modeling. In: Pro-
ceedings of the 18th ACM Conference on Recommender Systems (RecSys ’24).
p. 10. ACM, Bari, Italy (October 14–18 2024)
22. Szegedy, C., Zaremba, W., Sutskever, I., Bruna, J., Erhan, D., Goodfellow, I.,
Fergus, R.: Intriguing properties of neural networks. In: International Conference
on Learning Representations (2014)
23. Wang, C., Shi, X., Xu, S., Wang, Z., Fan, Z., Feng, Y., You, A., Chen, Y.: A
multi-stage framework for online bonus allocation based on constrained user intent
detection. In: Proceedings of the 29th ACM SIGKDD Conference on Knowledge
Discovery and Data Mining. pp. 5028–5038 (2023)
24. Wang, X., Liu, T., Miao, J.: A deep probabilistic model for customer lifetime value
prediction. arXiv preprint arXiv:1912.07753 (2019)
25. Wu, Y., Zhu, Z., Ma, C., Qian, H., Lu, X., Zhang, Y., Qin, X., Fei, B., Zhou,
J., Zhou, A.: Cost-efficient fraud risk optimization with submodularity in insur-
ance claim. In: Proceedings of the 30th ACM SIGKDD Conference on Knowledge
Discovery and Data Mining. pp. 3448–3459 (2024)
26. Yang, Y., Zha, K., Chen, Y., Wang, H., Katabi, D.: Delving into deep imbal-
anced regression. In: International conference on machine learning. pp. 11842–
11851. PMLR (2021)
27. Zhan, R., Pei, C., Su, Q., Wen, J., Wang, X., Mu, G., Zheng, D., Jiang, P., Gai, K.:
Deconfounding duration bias in watch-time prediction for video recommendation.
In: Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery
and Data Mining. pp. 4472–4481 (2022)
28. Zhang, S., Li, Z., Yan, S., He, X., Sun, J.: Distribution alignment: A unified frame-
work for long-tail visual recognition. In: CVPR (2021)
29. Zhang, Y., Yang, Q.: An overview of multi-task learning. National Science Review
5(1), 30–43 (2018)
30. Zhao, K., Hua, J., Yan, L., Zhang, Q., Xu, H., Yang, C.: A unified framework
for marketing budget allocation. In: Proceedings of the 25th ACM SIGKDD In-
ternational Conference on Knowledge Discovery & Data Mining. pp. 1820–1830
(2019)
31. Zhu, H., Li, X., Zhang, P., Li, G., He, J., Li, H., Gai, K.: Learning tree-based
deep model for recommender systems. In: Proceedings of the 24th ACM SIGKDD
international conference on knowledge discovery & data mining. pp. 1079–1088
(2018)
