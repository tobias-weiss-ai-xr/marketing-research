---
title: Backward Compatibility in Tree-Based Explanations and Enhanced CART Algorithm
url: https://arxiv.org/abs/2608.08674
category: ai-marketing
subcategory: measurement
date: 2026-08
venue: ''
authors:
- Hirofumi Suzuki
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.08674
pages: 18
chars: 62475
fetched_at: '2026-11-08T13:28:55+00:00'
kb_version: 1
---

# Backward Compatibility in Tree-Based Explanations and Enhanced CART Algorithm

Backward Compatibility in Tree-Based Explanations and
Enhanced CART Algorithm
Hirofumi Suzuki
suzuki-hirofumi@fujitsu.com
Fujitsu Limited
Kawasaki, Kanagawa, Japan
Figure 1: Solid and dashed lines denote the decision boundaries of the corresponding decision tree and the old decision tree,
respectively. When a naive decision tree update is performed using CART on a new dataset, the explanations (i.e., the feature
subspaces associated with predictions) change substantially for many samples belonging to the blue square and green triangle
classes. In contrast, updates performed using our CART-BCTX result in only minor changes in explanations for most samples.
Abstract
In the operation of machine learning models,model updateis a fun-
damental process that requires careful consideration of its impact on
downstream decision-making. Particularly when operating explain-
able models, changes in explanations resulting from model updates
can lead to detrimental outcomes for users.Decision trees, due to
their high transparency, are frequently employed in risk-sensitive
decision-making and serve as a prominent example in which the
aforementioned issue is evident. However, existing research address-
ing similar issues has focused on explanations based on feature
contributions, and thus cannot handle explanations derived from
tree structures. Therefore, this paper proposes theBackward Com-
patibility Loss in Tree-based eXplanations (BCLTX), a loss metric
that suppresses changes in decision tree explanations before and
after updates. Furthermore, we designCART with Backward Com-
patibility in Tree-based eXplanations (CART-BCTX), a lightweight
algorithm that improves upon CART for the decision tree update
problem under BCLTX. Experimental results using 10 real-world
datasets, including both classification and regression tasks, show
that CART-BCTX achieves favorable trade-offs between prediction
performances and BCLTX values, with comparable computation
times to CART, regardless of the task.
CCS Concepts
•Computing methodologies → Classification and regression
trees.
This work is licensed under a Creative Commons Attribution 4.0 International License.
KDD 2026, Jeju Island, Republic of Korea.
©2026 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-2259-2/2026/08
https://doi.org/10.1145/3770855.3817736
Keywords
Decision Tree, Backward Compatibility, Explainable AI, CART
ACM Reference Format:
Hirofumi Suzuki. 2026. Backward Compatibility in Tree-Based Explanations
and Enhanced CART Algorithm. InProceedings of the 32nd ACM SIGKDD
Conference on Knowledge Discovery and Data Mining V.2 (KDD 2026), August
9–13, 2026, Jeju Island, Republic of Korea.ACM, New York, NY, USA, 18 pages.
https://doi.org/10.1145/3770855.3817736
Resource Availability:
The source code of this paper has been made publicly available at https:
//doi.org/10.6084/m9.figshare.32521632.
1 Introduction
In the operation of systems based on machine learning models, it
is necessary to continuously monitor model performance and con-
ductmodel updatesas needed in order to maintain or improve their
performance [16, 24, 27]. Model updates replace models trained
on older datasets with those trained on more recent and/or larger
datasets accumulated during system operation. However, such up-
dates inevitably change model behavior and can have a substantial
impact on downstream decision-making, potentially leading to
unexpected or undesirable outcomes. Indeed, a user study has re-
ported that naive model updates reduce the productivity of decision-
making supported by machine learning models [4]. To address this
issue, prior studies have investigatedbackward compatibility, a
metric that quantifies differences in model behavior before and
after updates, as well as model update methods based on this con-
cept [4, 20, 21, 25, 26, 29].
Explainable models [2, 8] are widely deployed in risk-sensitive
decision-making domains such as healthcare, finance, and manufac-
turing, where model updates can lead to detrimental outcomes for
users. In addition, even when an updated model achieves superior
arXiv:2608.08674v1  [cs.LG]  9 Aug 2026

KDD 2026, August 9–13, 2026, Jeju Island, Republic of Korea. Hirofumi Suzuki
predictive performance, users may not fully trust it if its explana-
tions differ substantially from those of the previously deployed
model [28], highlighting the importance of backward compatibility
in explanations. A representative example of explainable models is
decision trees[ 6], which provide explanations through if–then–else
rules derived from tree structures and are frequently used in risk-
sensitive applications due to their high transparency [9, 13, 23, 30].
However, existing studies on backward compatibility [20, 29] pri-
marily focus on SHAP-based feature contribution explanations [19],
and thus cannot handle tree-based explanations.
To overcome this limitation, we propose theBackward Compati-
bility Loss in Tree-based eXplanations (BCLTX), a loss metric that
captures changes in tree-based explanations before and after model
updates. Unlike existing backward compatibility metrics [20], the
core idea of BCLTX does not rely on the conventional notion of
disagreement measures [17], but is instead specifically designed
to directly reflect the properties of tree-based explanations. Fur-
thermore, we formulate a decision tree update problem induced
by BCLTX, and proposeCART with Backward Compatibility in
Tree-based eXplanations (CART-BCTX)to solve this problem. CART-
BCTX is a lightweight algorithm that extends CART [6], a standard
decision tree learning algorithm, allowing backward compatible
updates to be performed efficiently without sacrificing scalability.
The main concept of this paper is shown in Figure 1.
Our contributions are summarized as follows:
• We focus on the fact that decision tree explanations can be
represented as a conjunction of intervals defined by split
points for individual features, and propose a backward com-
patibility loss metric that captures explanation differences
before and after updates. The proposed metric includes for-
mulations based on the Jaccard coefficient, which captures
differences in contributing feature sets, as well as formula-
tions based on absolute and squared errors, which capture
differences in feature-wise intervals.
• Based on the proposed backward compatibility loss metrics,
we formulate a decision tree update problem and design an
efficient algorithm to solve it. The proposed algorithm ex-
tends the standard decision tree learning algorithm CART;
compared with CART, it has equivalent computational com-
plexity when using Jaccard- or squared-error–based loss
metrics, and incurs at most a log𝑛 factor increase in the
worst case when using absolute-error–based loss metrics,
where𝑛denotes the number of samples.
• We conducted experiments on 10 real-world datasets, in-
cluding both classification and regression tasks. The results
demonstrate that our update algorithm achieves excellent
trade-offs between predictive performances and the pro-
posed loss metrics, with computation times comparable to
those of CART. In addition, the results suggest that the pro-
posed loss metrics based on absolute error and squared error
contribute to improving backward compatibility with respect
to predictions.
• Although our framework assumes a batch learning environ-
ment, backward compatibility can also be evaluated in a
batch-wise manner under incremental learning with data
streams. Based on this perspective, we conduct comparative
experiments with incremental decision trees. The results
suggest that backward compatibility in tree-based explana-
tions is not necessarily preserved over medium- to long-term
periods by incremental decision trees.
2 Related Work
Bansal et al. pointed out that changes in model behavior caused by
model updates can reduce the productivity of human–AI collabora-
tive decision-making, and introducedbackward compatibilityas a
metric to capture this issue [4]. Backward compatibility is defined
as the proportion of samples that are correctly predicted by the
new model among those that were correctly predicted by the old
model. By training new models to improve backward compatibility,
user trust in predictions can be preserved across model updates.
Srivastava et al. empirically analyzed how naive model updates de-
grade backward compatibility and proposed an alternative metric
that focuses on incorrect predictions rather than correct ones [26].
In addition, generalized backward compatibility metrics have been
proposed from the perspectives of true positives and false nega-
tives [25], as well as robustness-enhanced metrics that take local
data distributions into account [21].
While the aforementioned studies define backward compatibility
from the perspective of changes in prediction results, Matsuno et
al. focused on SHAP-based explanations [19] and definedBackward
Compatibility in eXplanation (BCX)from the perspective of changes
in explanations [20]. This definition takes into account the concept
of disagreement measures proposed in prior literature [17]. Further-
more, since Matsuno et al. applied BCX to differentiable machine
learning models, an extended method has also been proposed to
handle gradient boosting tree ensembles [ 29]. However, BCX is
currently the only existing backward compatibility metric defined
from the perspective of changes in explanations. This indicates a
clear need for dedicated backward compatibility metrics suitable for
explainable models that primarily rely on non-SHAP explanations,
such as decision trees [6].
Another line of related work is incremental decision trees such
as Hoeffding Trees (HT) [ 11], also known as Very Fast Decision
Trees (VFDT) [7], and Hoeffding Adaptive Trees (HAT) [5]. Incre-
mental decision trees achieve practical performance on streaming
environments by sequentially determining and updating branching
conditions based on statistical guarantees such as the Hoeffding
bound. While there is a significant difference between update sce-
narios of ours and incremental decision trees in terms of whether
data is processed in batch or stream format, we can expect that
incremental decision trees exhibit relatively high backward compat-
ibility with recently observed data, as they are updated sequentially
in response to incoming data streams. However, our experiments
suggest that this property does not necessarily extend to batch-wise
evaluation over medium- to long-term periods.
3 Proposed Loss Metrics
We consider updating a decision tree trained on an old dataset to
a new decision tree using a new dataset, and proposeBackward
Compatibility Loss in Tree-based eXplanations (BCLTX)as a loss
metric. Each sample consists of an𝑚-dimensional feature vector
𝒙=(𝑥 𝑗)𝑚 𝑗=1∈R 𝑚 and a target variable𝑦, where𝑦∈{ 1,...,𝑐} for

Backward Compatibility in Tree-Based Explanations and Enhanced CART Algorithm KDD 2026, August 9–13, 2026, Jeju Island, Republic of Korea.
Algorithm 1PredictAndExplanation(𝑇,𝒙)
1:𝑙←(−∞) 𝑚 𝑗=1,𝑢←(∞) 𝑚 𝑗=1
2:Let𝑡be the root node of𝑇
3:while𝑡is not a leaf nodedo
4:if𝑥 𝑗𝑡≤𝑣 𝑡 then
5:𝑢 𝑗𝑡←𝑣 𝑡
6:𝑡←The left child node of𝑡
7:else
8:𝑙 𝑗𝑡←𝑣 𝑡
9:𝑡←The right child node of𝑡
10:return(𝑦 𝑡 ,𝑙,𝑢)
classification tasks with𝑐 classes, and𝑦∈R for regression tasks. Let
the old dataset be denoted as𝐷1 ={(𝒙 𝑖,𝑦𝑖)}𝑛1 𝑖=1 and the additional
dataset as 𝐷Δ ={(𝒙 𝑖,𝑦𝑖)}𝑛2 𝑖=𝑛1+1, and define the new dataset as 𝐷2 =𝐷 1∪𝐷 Δ. Let𝑇1 denote the old decision tree trained on the old
dataset𝐷1, and let𝑇2 denote the new decision tree updated using
the new dataset𝐷2. BCLTX is designed to capture the differences
between the explanations produced by𝑇 1 and𝑇 2.
3.1 Tree-Based Explanations
A decision tree𝑇 is a binary tree that, given an input 𝒙, produces
both a prediction of the target value and an explanation supporting
the prediction. For each node 𝑡 in𝑇 , if𝑡 is an internal node, it is
associated with a feature index𝑗𝑡 and a split point𝑣𝑡 ; if𝑡 is a leaf
node, it is associated with a predicted value𝑦𝑡 . Given an input 𝒙,
inference in𝑇 starts from the root node. At each internal node𝑡,
the condition𝑥𝑗𝑡≤𝑣 𝑡 determines whether the inference proceeds
to the left or right child, and the predicted value associated with the
reached leaf node is output. Each leaf node corresponds to a feature
subspace that does not overlap with those of other leaf nodes, and
the decision tree can output this subspace as an explanation for
the prediction. Algorithm 1 describes how to compute both the
prediction and the explanation of a decision tree𝑇 for a given input
𝒙. The procedure runs in𝑂(𝑚+𝑑) time, where𝑑 is the depth of
𝑇 . Here, an explanation is represented by a lower bound vector
𝑙=(𝑙 𝑗(𝑇,𝒙)) 𝑚 𝑗=1 and an upper bound vector𝑢=(𝑢 𝑗(𝑇,𝒙)) 𝑚 𝑗=1.
We formally interpret the explanation𝑙,𝑢 produced by a decision
tree𝑇 for an input 𝒙. First, a feature is considered to essentially
contribute to the explanation if at least one of its lower or upper
bounds is finite. The set of such features can be expressed as
𝐹(𝑇,𝒙):={𝑗∈{1,...,𝑚}|𝑙 𝑗(𝑇,𝒙)>−∞∨𝑢 𝑗(𝑇,𝒙)<∞}.(1)
This set can be decomposed into the feature sets that contribute to
the lower bounds and to the upper bounds, respectively:
𝐹𝑙(𝑇,𝒙):={𝑗∈{1,...,𝑚}|𝑙 𝑗(𝑇,𝒙)>−∞},
𝐹𝑢(𝑇,𝒙):={𝑗∈{1,...,𝑚}|𝑢 𝑗(𝑇,𝒙)<∞}. (2)
The explanation 𝑙,𝑢 can be represented as the following logical
expression over the feature set𝐹(𝑇,𝒙) : a conjunction of intervals
defined by the lower and upper bounds of each contributing feature.
𝐸(𝑇,𝒙):=
Û
𝑗∈𝐹(𝑇,𝒙)
𝑙𝑗(𝑇,𝒙)<𝑗-th feature≤𝑢 𝑗(𝑇,𝒙) .(3)
3.2 Definitions of BCLTX
Motivated by the tree-based explanations described above, we pro-
pose four variants of BCLTX. Two of them are based on Eqs. (1)
and (2), and the remaining two are based on Eq. (3). These defini-
tions are formulated as basic measures derived from commonly
used dissimilarity metrics.
First, based on Eq. (1), we define BCLTX by measuring the dif-
ference between𝐹(𝑇 1,𝒙) and𝐹(𝑇 2,𝒙) using the Jaccard coefficient.
𝛿JAC(𝑇1,𝑇2,𝒙):= 1 𝑚|𝐹(𝑇 1,𝒙)△𝐹(𝑇 2,𝒙)|
Here,△ denotes the symmetric difference operator between sets.
This definition of BCLTX reflects the extent to which the features
contributing to the explanations differ. Next, this Jaccard-based
definition can be extended to a formulation using Eq. (2):
𝛿JLU(𝑇1,𝑇2,𝒙):=
1
2𝑚(|𝐹𝑙(𝑇1,𝒙)△𝐹 𝑙(𝑇2,𝒙)|+|𝐹 𝑢(𝑇1,𝒙)△𝐹 𝑢(𝑇2,𝒙)|).
This captures the differences in the features contributing to the
explanations with respect to the lower and upper bounds separately.
The definitions of BCLTX based on Eq. (3) quantify differences
between the feature-wise intervals of 𝐸(𝑇1,𝒙) and𝐸(𝑇2,𝒙) using
the mean absolute error (MAE) or the mean squared error (MSE).
To this end, two preprocessing steps are applied. First, to ensure
finite evaluation of interval differences, we use adjusted bounds
𝑙′ 𝑗(𝑇,𝒙) :=max{𝑙 𝑗(𝑇,𝒙),𝑥 min 𝑗 } and𝑢′ 𝑗(𝑇,𝒙) :=min{𝑢 𝑗(𝑇,𝒙),𝑥 max 𝑗 },
where𝑥min 𝑗 :=min{𝑥 𝑖,𝑗}𝑛2 𝑖=1 and𝑥max 𝑗 :=max{𝑥 𝑖,𝑗}𝑛2 𝑖=1. Second, to
achieve scale-invariant evaluation across features, we introduce
the standard deviation𝜎𝑗 of{𝑥𝑖,𝑗}𝑛2 𝑖=1. Under these preprocessing
steps, BCLTX based on MAE and MSE are defined as follows.
𝛿MAE(𝑇1,𝑇2,𝒙):=
1
2𝑚
𝑚∑︁
𝑗=1
|𝑙′ 𝑗(𝑇1,𝒙)−𝑙 ′ 𝑗(𝑇2,𝒙)|+|𝑢 ′ 𝑗(𝑇1,𝒙)−𝑢 ′ 𝑗(𝑇2,𝒙)|
𝜎𝑗
𝛿MSE(𝑇1,𝑇2,𝒙):=
1
2𝑚
𝑚∑︁
𝑗=1
(𝑙′ 𝑗(𝑇1,𝒙)−𝑙 ′ 𝑗(𝑇2,𝒙)) 2+(𝑢′ 𝑗(𝑇1,𝒙)−𝑢 ′ 𝑗(𝑇2,𝒙)) 2
𝜎2 𝑗
4 Decision Tree Update under BCLTX
We formulate the problem of updating an old decision tree 𝑇1 to
a new decision tree 𝑇2 on the new training dataset 𝐷2 so as to
suppress BCLTX. Furthermore, we propose an efficient algorithm
to address the problem,CART with Backward Compatibility in Tree-
based eXplanations (CART-BCTX), which enhances CART [ 6], a
standard algorithm for constructing decision trees.
4.1 Formulation
Our decision tree update problem aims to minimize the following
objective function using a hyperparameter𝜆∈R ≥0 that controls
the strength of BCLTX.
𝑓(𝑇 1,𝑇2,𝐷 2,𝜆):=
1
|𝐷2|
∑︁
(𝒙,𝑦)∈𝐷 2
ℓ(𝑇2(𝒙),𝑦)+ 𝜆 |𝐷𝑠| ∑︁ (𝒙,𝑦)∈𝐷 𝑠 𝛿(𝑇1,𝑇2,𝒙) (4)

KDD 2026, August 9–13, 2026, Jeju Island, Republic of Korea. Hirofumi Suzuki
Here,𝑇(𝒙) denotes the predicted value on the decision tree𝑇 for
the input 𝒙,ℓ denotes a task-specific loss function, such as the 0-1
loss for classification tasks or the squared error for regression tasks,
𝛿∈{𝛿 JAC,𝛿 JLU,𝛿 MAE,𝛿 MSE}, and𝐷𝑠 denotes the set of samples that
are correctly predicted by𝑇 1. Specifically,𝐷𝑠 is defined as
𝐷𝑠 :={(𝒙,𝑦)∈𝐷 2|𝑠(𝑇 1(𝒙),𝑦)=1}
where𝑠is an indicator function defined as
𝑠( ˆ𝑦,𝑦):=
(
1[ ˆ𝑦=𝑦] (classification),
1[| ˆ𝑦−𝑦|≤𝜖] (regression).
Here, for regression tasks, a prediction is regarded as correct if the
absolute error is less than or equal to a given threshold𝜖∈R ≥0.
The above definition incorporates backward compatibility into
the loss function by weighting only samples for which the old
model made correct predictions. In practice, however, the definition
of𝐷𝑠 is flexible and can be adjusted to meet user requirements.
For example,𝐷𝑠 can be defined as the set of samples that satisfy a
decision rule in which the user has sufficient confidence, enabling
model updates that better reflect the user’s intentions. Furthermore,
it is also possible to assign more fine-grained real-valued weights
to individual samples.
We need to develop an efficient algorithm to address the above
problem. However, this problem is computationally challenging
even when𝜆= 0[ 12]. Therefore, we enhance CART [6], a greedy
algorithm for constructing decision trees, so that it can handle
BCLTX. In addition, although decision trees employ a post-pruning
method known as cost complexity pruning [6], this pruning method
can be readily extended to handle BCLTX.
4.2 CART-BCTX
In this subsection, we describe CART-BCTX in detail. CART-BCTX
is a greedy decision tree update algorithm that enhances CART
to heuristically optimize Eq. (4). CART starts from a minimal de-
cision tree consisting of only a root node and grows the tree by
recursively selecting greedy splits that improve the objective, as
long as given constraints on the maximum depth and the mini-
mum sample size are satisfied. CART-BCTX incorporates operations
that account for BCLTX into the greedy split selection procedure
of CART. Specifically, CART-BCTX maintains, for each node in
the growing decision tree, a lower bound vector ˆ𝑙 and an upper
bound vector ˆ𝑢 that represent the feature subspace correspond-
ing to that node. The most greedy split is then searched using ˆ𝑙
and ˆ𝑢. Pseudo-code corresponding to the recursive procedure for
growing a decision tree in CART-BCTX is shown in Algorithm 2
(initially call CART-BCTX(𝐷2,(𝑥 min 𝑗 )𝑚 𝑗=1,(𝑥 max 𝑗 )𝑚 𝑗=1, 0) where𝑇1,𝐷𝑠,
and𝜆 are globally stored). In the following, we describe in detail
the procedure searching greedy splits (Algorithm 3) and present
the resulting computational complexity of CART-BCTX.
Let𝐷 denote the dataset associated with the node currently being
considered for splitting. For each feature𝑗, the set of candidate split
points𝑉 is defined as the midpoints between consecutive values
when the samples in𝐷 are sorted in ascending order with respect to
𝑥𝑗 . For each split point𝑣∈𝑉 , which is scanned in ascending order,
we compute the gain with respect to the task-specific loss, denoted
by Gainℓ, and the gain with respect to BCLTX, denoted by Gain𝛿.
Among all combinations of features and split points, we select the
Algorithm 2CART-BCTX(𝐷, ˆ𝑙, ˆ𝑢,𝑑)
1:Generate a node𝑡
2:𝑦 𝑡←Generate a prediction result on𝐷
3:if𝑑=max_depththen
4:returnThe tree with only the root node𝑡
5:(𝑗 𝑡,𝑣𝑡)←FindBestSplit-BCTX(𝐷, ˆ𝑙, ˆ𝑢)
6:if𝑗 𝑡 =NULLthen
7:returnThe tree with only the root node𝑡
8:𝐷 𝐿←{(𝒙,𝑦)∈𝐷|𝑥 𝑗𝑡≤𝑣 𝑡}
9:𝐷 𝑅←{(𝒙,𝑦)∈𝐷|𝑥 𝑗𝑡 >𝑣 𝑡}
10: ˇ𝑙← ˆ𝑙, ˇ𝑢← ˆ𝑢
11: ˇ𝑙𝑗𝑡←𝑣 𝑗𝑡 , ˇ𝑢𝑗𝑡←𝑣 𝑗𝑡 ,
12:𝑇 𝐿←CART-BCTX(𝐷 𝐿, ˆ𝑙, ˇ𝑢,𝑑+1)
13:𝑇 𝑅←CART-BCTX(𝐷 𝑅, ˇ𝑙, ˆ𝑢,𝑑+1)
14: returnThe tree rooted at 𝑡 with the left subtree𝑇𝐿 and the
right subtree𝑇𝑅
Algorithm 3FindBestSplit-BCTX(𝐷, ˆ𝑙, ˆ𝑢)
1:𝑗 ∗←NULL,𝑣 ∗←NULL,Gain ∗←0
2:for𝑗=1,...,𝑚do
3:Compute threshold candidates𝑉of𝑗-th feature over𝐷
4:𝐷 𝐿←∅,𝐷 𝑅←𝐷
5:for𝑣∈𝑉in ascending orderdo
6:𝐷 diff←{(𝒙,𝑦)∈𝐷 𝑅|𝑥 𝑗≤𝑣}
7:𝐷 𝐿←𝐷 𝐿∪𝐷 diff,𝐷 𝑅←𝐷 𝑅\𝐷 diff
8:ComputeGain ℓ andGain𝛿 of(𝐷 𝐿,𝐷𝑅)
9:if|𝐷 𝐿|<min_samples_leafthen continue
10:if|𝐷 𝑅|<min_samples_leafthen continue
11:ifGain ∗ < 1 |𝐷 2| Gainℓ+ 𝜆 |𝐷𝑠| Gain𝛿 then
12:𝑗 ∗←𝑗,𝑣 ∗←𝑣,Gain ∗← 1 |𝐷 2| Gainℓ+ 𝜆 |𝐷𝑠| Gain𝛿
13:return(𝑗 ∗,𝑣∗)
split that maximizes the total gain 1 |𝐷 2| Gainℓ+ 𝜆 |𝐷𝑠| Gain𝛿. If the
total gain does not exceed zero for any split, no split is performed.
SinceGainℓ can be computed in the same manner as in CART, we
omit its description and focus only on how to efficiently compute
Gain𝛿. The computation of Gain𝛿 depends on the variant of the
BCLTX definition being used. Here, when the dataset𝐷 is split by a
point𝑣 on feature𝑗, we denote by𝐷𝐿 and𝐷𝑅 the sets of samples in
𝐷 satisfying𝑥𝑗≤𝑣 and𝑥𝑗 >𝑣 , respectively. In addition, we denote
by𝐷diff the set of samples that lie between the split point 𝑣 and
the immediately preceding split point. A key observation is that
the effect of a split using 𝑗 and𝑣 on the explanations is solely that,
for samples in𝐷𝐿, the upper bound ˆ𝑢𝑗 changes to𝑣, whereas for
samples in𝐷 𝑅, the lower bound ˆ𝑙𝑗 changes to𝑣.
For𝛿JAC.We need to check whether the feature𝑗 currently under
consideration has already been used. Let ¯𝑙𝑗 := 1[ˆ𝑙𝑗 =𝑥 min 𝑗 ] and
¯𝑢𝑗 := 1[ ˆ𝑢𝑗 =𝑥 max 𝑗 ] for convenience to represent𝑗 is not used for ˆ𝑙
and ˆ𝑢, respectively. We can compute the gain
Gain𝛿JAC = 1 𝑚 ∑︁ (𝒙,𝑦)∈𝐷∩𝐷 𝑠 ¯𝑙𝑗 ¯𝑢𝑗(1[𝑗∈𝐹(𝑇 1,𝒙)]−1[𝑗∉𝐹(𝑇 1,𝒙)]).

Backward Compatibility in Tree-Based Explanations and Enhanced CART Algorithm KDD 2026, August 9–13, 2026, Jeju Island, Republic of Korea.
This gain depends only on the feature𝑗 and is therefore constant
with respect to the choice of split point𝑣.
For𝛿JLU.Similarly to 𝛿JAC, we need to check whether the feature
𝑗 currently under consideration has already been used for the upper
and lower bounds, respectively. We can compute the gain
Gain𝛿JLU = 1 2𝑚 ∑︁ (𝒙,𝑦)∈𝐷 𝐿∩𝐷𝑠 ¯𝑢𝑗(1[𝑗∈𝐹 𝑢(𝑇1,𝒙)]−1[𝑗∉𝐹 𝑢(𝑇1,𝒙)])
+ 1 2𝑚 ∑︁ (𝒙,𝑦)∈𝐷 𝑅∩𝐷𝑠 ¯𝑙𝑗(1[𝑗∈𝐹 𝑙(𝑇1,𝒙)]−1[𝑗∉𝐹 𝑙(𝑇1,𝒙)]).
In addition, the gain change with respect to 𝐷diff can be com-
puted in𝑂(|𝐷 diff|) time by adding and subtracting constants1[𝑗∈
𝐹𝑢(𝑇1,𝒙)]− 1[𝑗∉𝐹 𝑢(𝑇1,𝒙)] and1[𝑗∈𝐹 𝑙(𝑇1,𝒙)]− 1[𝑗∉𝐹 𝑙(𝑇1,𝒙)]
for all(𝒙,𝑦)∈𝐷 diff∩𝐷𝑠.
For𝛿MAE.According to the definition, we can compute the gain
Gain𝛿MAE = 1 2𝑚𝜎𝑗 ∑︁ (𝒙,𝑦)∈𝐷 𝐿∩𝐷𝑠 (|𝑢′ 𝑗(𝑇1,𝒙)− ˆ𝑢𝑗|−|𝑢 ′ 𝑗(𝑇1,𝒙)−𝑣|)
+ 1 2𝑚𝜎𝑗 ∑︁ (𝒙,𝑦)∈𝐷 𝑅∩𝐷𝑠 (|𝑙′ 𝑗(𝑇1,𝒙)− ˆ𝑙𝑗|−|𝑙 ′ 𝑗(𝑇1,𝒙)−𝑣|).
For efficient gain computation, we maintain the set U of𝑢′ 𝑗 for
samples in𝐷𝐿∩𝐷𝑠 and the setL of𝑙′ 𝑗 for samples in𝐷𝑅∩𝐷𝑠. Then,
it suffices to compute˝ 𝑢′ 𝑗∈U|𝑢′ 𝑗−𝑤| and ˝ 𝑙′ 𝑗∈L|𝑙′ 𝑗−𝑤| for a given
𝑤. By partitioningU into two subsetsU≤ andU> according to
the conditions𝑢′ 𝑗≤𝑤 and𝑢′ 𝑗 >𝑤 , respectively, we can rewrite˝
𝑢′ 𝑗∈U|𝑢′ 𝑗−𝑤|=𝑤|U ≤|− ˝ 𝑢′ 𝑗∈U≤𝑢′ 𝑗+ ˝ 𝑢′ 𝑗∈U >𝑢′ 𝑗−𝑤|U >|. The
same transformation applies toL. Such computations are achieved
by maintainingUandLusing self-balancing binary search trees,
enabling the gain to be computed in𝑂(|𝐷 diff|log|𝐷|)time.
For𝛿MSE.According to the definition, we can compute the gain
Gain𝛿MSE = 1 2𝑚𝜎2 𝑗 ∑︁ (𝒙,𝑦)∈𝐷 𝐿∩𝐷𝑠 ((𝑢′ 𝑗(𝑇1,𝒙)− ˆ𝑢𝑗)2−(𝑢′ 𝑗(𝑇1,𝒙)−𝑣) 2)
+ 1 2𝑚𝜎2 𝑗 ∑︁ (𝒙,𝑦)∈𝐷 𝑅∩𝐷𝑠 ((𝑙′ 𝑗(𝑇1,𝒙)− ˆ𝑙𝑗)2−(𝑙′ 𝑗(𝑇1,𝒙)−𝑣) 2).
Here, for a given set of values W and a value 𝑤, we can write˝
𝑤′∈W(𝑤′−𝑤) 2 = ˝ 𝑤′∈W𝑤′2+ 2𝑤 ˝ 𝑤′∈W𝑤′+|W|𝑤 2. There-
fore, the computation of Gain𝛿MSE with respect to𝐷𝐿 can be com-
pleted in𝑂(|𝐷 diff|) time by updating ˝ 𝑢′ 𝑗∈U𝑢′2 𝑗 and ˝ 𝑢′ 𝑗∈U𝑢′ 𝑗 for
the setU according to𝐷diff∩𝐷𝑠. The same procedure applies to
𝐷𝑅 and the corresponding setL.
In general, CART preprocesses the dataset by sorting it in as-
cending order with respect to each feature, and this sorted order
can be maintained even after the dataset is recursively partitioned.
Moreover, the computation ofGainℓ can be performed in𝑂(|𝐷 diff|)
time following the standard CART procedure. Note that, for classi-
fication tasks, it is common practice to use the Gini impurity as a
surrogate rather than directly using the 0–1 loss. Considering these
facts together with the discussion on the computation of Gain𝛿,
and noting that for each feature 𝑗 the total sum of|𝐷diff| over all
split points is|𝐷| , the following proposition holds regarding the
computational complexity of CART-BCTX.
Proposition 1.Let 𝑛=|𝐷 2|, 𝑑1 be the depth of 𝑇1, and 𝑑2
be the depth of the updated tree. We preprocess to sort the dataset
and compute the explanation 𝑙,𝑢 for each sample in 𝑂(𝑛𝑚log𝑛+
𝑛(𝑚+𝑑 1)) time. Then, CART-BCTX takes𝑂(𝑛𝑚𝑑 2) time for 𝛿∈
{𝛿JAC,𝛿 JLU,𝛿 MSE}, same as CART, and𝑂(𝑛𝑚𝑑 2 log𝑛)time for𝛿 MAE.
4.3 Cost Complexity Pruning under BCLTX
Cost complexity pruning (CCP) is a post-pruning method that re-
duces the size of a decision tree in order to prevent overfitting [6].
However, when CCP is naively applied to a decision tree constructed
by CART-BCTX, aggressive pruning may severely degrade back-
ward compatibility in explanations. Therefore, we introduce a sim-
ple extension of CCP that enables it to be executed under BCLTX.
Our CCP removes subtrees of𝑇2 deemed unnecessary by mini-
mizing the following objective function.
𝑔(𝑇1,𝑇 ccp 2 ,𝐷 2,𝜆,𝛼):=𝑓(𝑇 1,𝑇 ccp 2 ,𝐷 2,𝜆)+𝛼#Leaves(𝑇 ccp 2 )
Here,𝑇 ccp 2 is the pruned decision tree,# Leaves(𝑇 ccp 2 ) denotes the
number of its leaves, and𝛼∈ R≥0 is a regularization parameter. Our
CCP differs from the standard CCP only in replacing the loss func-
tion𝑓 with our formulation of Eq. (4), and introduces no changes
from an algorithmic perspective. That is, as in the standard CCP [6],
it is possible to efficiently search for candidate values of𝛼, compute
𝑇 ccp 2 for each𝛼, and select a better𝛼via cross-validation on𝐷 2.
5 Experiments
To evaluate the performance of CART-BCTX, we investigated its
behavior on real-world datasets by comparing it with a naive model
update using CART as well as incremental decision trees. CART-
BCTX was implemented using C++20 and modularized in Python
3.13 via Cython 3.2. Note that CART can be executed within CART-
BCTX without any additional overhead by explicitly skipping the
computation of Gain𝛿 when𝜆= 0. In addition, we used the River
library [22] for incremental decision trees. The experimental envi-
ronment consisted of Ubuntu 24.04 LTS on WSL2, 13th Gen Intel(R)
Core(TM) i7-13700H CPU, and 16GB of memory.
Our experiments are designed to address the following four
research questions:
(i) Can CART-BCTX achieve a well-balanced trade-off between
predictive performance and BCLTX values?
(ii) Does improving BCLTX values affect backward compatibility
in predictions?
(iii) Can CART-BCTX operate with computation times compara-
ble to those of CART?
(iv) How does the behavior of CART-BCTX differ from that of
incremental decision trees?
Datasets.We used a total of 10 datasets obtained from the UCI
Machine Learning Repository [14] and the KEEL Dataset Reposi-
tory [1]. The datasets consist of five classification tasks and five
regression tasks; the dataset names, numbers of samples, and num-
bers of features are summarized in Table 1. Categorical features
were preprocessed using one-hot encoding, and the reported num-
bers of features correspond to those after preprocessing.
Settings.For both CART and CART-BCTX, no depth limit was
imposed, the minimum sample size was set to 1% of the number

KDD 2026, August 9–13, 2026, Jeju Island, Republic of Korea. Hirofumi Suzuki
Task Dataset #Samples #Features Source
adult 45222 104 UCI
magic 19020 10 UCI
Classification shoppers 12330 28 UCI
spambase 4601 57 UCI
thyroid 7200 21 KEEL
abalone 4177 10 UCI
ailerons 13750 40 KEEL
Regression power-plant 9568 4 UCI
puma32h 8192 32 KEEL
wine-quality 6497 13 UCI
Table 1: Summary of datasets used in our experiments.
of samples in the training dataset, and the post-pruning process
by CCP was performed using 5-fold cross-validation. For CART-
BCTX, the parameter𝜆 was varied over nine values:0.0001,0.0005,
0.001,0.005,0.01,0.05,0.1,0.5, and1.0. All variants of BCLTX were
tested, namely 𝛿JAC,𝛿JLU,𝛿MAE, and 𝛿MSE. We set the number of
samples in the old training dataset𝐷1 to 500 and that in the new
training dataset𝐷2 to 1,000, using the remaining samples as the
test dataset. The old decision tree was trained by CART on𝐷1. For
each dataset, a total of 100 trials were conducted using random
splits of the dataset. In regression tasks, the parameter 𝜖 used to
define correct predictions by the old model was set to the root mean
squared error (RMSE) of the old decision tree evaluated on𝐷 2.
5.1 Prediction–BCLTX Trade-off Analysis
Figure 2 (for classification tasks) and Figure 3 (for regression tasks)
present the predictive performance and BCLTX values of the up-
dated decision trees obtained by CART and CART-BCTX. In these
figures, the values obtained by CART serve as the starting point,
and the trajectories illustrate changes in the evaluation metrics
as𝜆 increases in CART-BCTX, where each point represents the
average over 100 trials. As reference lines, the predictive perfor-
mance of the old decision tree and that of the new decision tree
obtained by CART, as well as the BCLTX values obtained by CART,
are shown. As measures of predictive performance, we used the
error rate (i.e., misclassification rate) for classification datasets and
the RMSE for regression datasets. For all datasets, we evaluated the
sample-averaged values of𝛿JAC,𝛿JLU,𝛿MAE, and𝛿MSE over samples
that were correctly predicted by the old decision tree.
From both Figure 2 and Figure 3, we observe that CART-BCTX
achieves improvements in predictive performance comparable to
those of CART for small𝜆, and that the magnitude of performance
improvement decreases as𝜆 increases. In addition, compared with
CART, CART-BCTX consistently improves BCLTX values, while the
improvement in BCLTX becomes more gradual as𝜆 increases. These
results indicate that CART-BCTX exhibits a reasonable trade-off be-
tween improvements in predictive performance and improvements
in BCLTX as𝜆 varies. Although the behavior of CART-BCTX varies
depending on the variant of BCLTX used during execution, employ-
ing𝛿MAE and𝛿MSE leads to notably improved values of the other
loss metrics,𝛿JAC and𝛿JLU, across all datasets. That is, using𝛿MAE
or𝛿MSE is sufficient when executing CART-BCTX. In summary,
CART-BCTX is capable of balancing the trade-off between predictive
performance and BCLTX values, and execution with 𝛿MAE or𝛿MSE is
recommended in most cases.
5.2 Effect on Compatible Predictions
Although CART-BCTX focuses on backward compatibility in expla-
nations, it is also desirable in practice that it maintains Backward
Compatibility in Predictions (BCP) [ 4]. Figure 4 shows the BCP
baseline obtained by CART and the changes in BCP achieved by
CART-BCTX with varying𝜆. Here, BCP is defined as the proportion
of samples that are correctly predicted by the new decision tree
among those that are correctly predicted by the old decision tree:
BCP(𝑇1,𝑇2,𝐷 test):=
˝
(𝒙,𝑦)∈𝐷 test𝑠(𝑇1(𝒙),𝑦)𝑠(𝑇 2(𝒙),𝑦) ˝
(𝒙,𝑦)∈𝐷 test𝑠(𝑇1(𝒙),𝑦) .
From Figure 4, we observe that when CART-BCTX is executed
using𝛿MAE or𝛿MSE, BCP improves substantially as𝜆 increases. In
contrast, when𝛿JAC or𝛿JLU is used, cases in which BCP improves
are relatively limited. Note that for the ‘thyroid‘ dataset, the BCP
achieved by CART is already sufficiently high, and therefore little
improvement is obtained by CART-BCTX. Intuitively, this behavior
can be attributed to the fact that improving𝛿MAE or𝛿MSE reduces
changes in how samples are partitioned by the decision tree, making
the predictions of the new decision tree more likely to be equivalent
to those of the old decision tree. In summary,CART-BCTX is also
effective in improving backward compatibility in predictions, and
execution with𝛿 MAE or𝛿 MSE is recommended in most cases.
5.3 Computation Times
Theoretically, the computational complexity of CART-BCTX is com-
parable to that of CART. However, in practice, additional compu-
tations related to BCLTX introduce a certain amount of overhead.
Therefore, to evaluate the extent of this overhead, we compared
the computation times of CART and CART-BCTX.
Figure 5 shows the results. CART-BCTX using 𝛿JAC, 𝛿JLU, or
𝛿MSE achieves computation times comparable to those of CART,
and at worst less than twice. In addition, although CART-BCTX
using MAE theoretically incurs a worst-case overhead of log𝑛 , the
empirical results show that, for𝑛= 1000, the computation times are
at most approximately twice those of CART. For regression tasks,
cases were observed in which CART-BCTX is faster than CART for
large𝜆. This can be attributed to the fact that the computational
complexity depends on the depth of the constructed decision tree,
and that incorporating BCLTX naturally suppresses unnecessary
splits. In summary,CART-BCTX operates with computation times
that are practically comparable to those of CART.
5.4 Comparison with Incremental Trees
We investigated the differences in behavior between CART-BCTX
and the incremental decision trees VFDT [7] and HAT [5] using the
same dataset as in the above experiments. Since VFDT and HAT
are designed to assume a sufficient number of samples, we changed
the sample sizes to|𝐷1|= 1000and |𝐷2|= 2000. Furthermore, we
used the implementations in the River library [22] 1 for VFDT and
HAT, setting the parameters to “grace_period=50” and “tau=0.15”,
and for HAT, “drift_window_threshold = 100”. For CART-BCTX,
1https://riverml.xyz/latest/

Backward Compatibility in Tree-Based Explanations and Enhanced CART Algorithm KDD 2026, August 9–13, 2026, Jeju Island, Republic of Korea.
Figure 2: Trade-offs for classification tasks. BCTX-tmpdenotes CART-BCTX using 𝛿tmp. The horizontal and vertical axes
represent the error rate and the sample-averaged BCLTX, respectively (lower is better for both). The gray dashed lines indicate
the error rates of the old models. The gray dotted lines represent the error rates and BCLTX values achieved by CART. All
plotted values are averaged over 100 trials. Overall, CART-BCTX achieves a reasonable trade-off between error rate and BCLTX.
we used the settings 𝜆= 0.005and 𝛿=𝛿 MSE, which achieved a
good prediction-BCLTX trade-off in many cases in the previous
experiments. Under these settings, we measured the prediction loss
and the BCP for CART, CART-BCTX, VFDT, and HAT, as well as
the sample-averaged BCLTX (𝛿MSE) for samples correctly predicted
by the old decision trees. In addition, Appendix C provides specific
examples of old and new decision trees obtained using each method
on the spambase dataset.
Note that incremental decision trees are not explicitly designed
to enforce backward compatibility in both predictions and explana-
tions. Our comparison aims to highlight differences in their behav-
ior under batch-wise evaluation of backward compatibility, while
also comparing prediction performance.
Figure 6 shows the results. Regarding the BCLTX values based
on𝛿MSE, CART-BCTX clearly achieved the best results in many
datasets except for abalone and ailerons. For abalone and ailerons
datasets, CART-BCTX, VFDT, and HAT all achieved comparable
results. Regarding BCP values, CART-BCTX consistently achieved
good results in all cases for the classification tasks, whereas VFDT
and HAT consistently showed good results for the regression tasks.
However, with the exception of the puma32h dataset, CART-BCTX
also achieved relatively good BCP values on the regression tasks.
Based on these findings, when observing performance on a batch-
wise basis, incremental decision trees maintained a certain level of
backward compatibility in predictions, but were inferior in terms
of backward compatibility in tree-based explanations compared to
CART-BCTX. Regarding prediction loss, the CART variants clearly
exhibited lower values than incremental decision trees, reflecting
the superior fit of batch learning on non-large datasets. In sum-
mary,CART-BCTX is superior to incremental decision trees in both of
predictive performance and BCLTX values, and has a comparable per-
formance in BCP values, when measuring batch-wise performances.
6 Conclusion
In this paper, we proposed Backward Compatibility Loss in Tree-
based eXplanations (BCLTX), a loss metric that captures backward
compatibility with respect to explanations in decision tree updates.
We also proposed CART with Backward Compatibility in Tree-
based eXplanations (CART-BCTX), an efficient greedy algorithm
for the decision tree update problem under BCLTX. CART-BCTX

KDD 2026, August 9–13, 2026, Jeju Island, Republic of Korea. Hirofumi Suzuki
Figure 3: Trade-offs for regression tasks. BCTX-tmpdenotes CART-BCTX using 𝛿tmp. The horizontal and vertical axes represent
the RMSE and the sample-averaged BCLTX, respectively (lower is better for both). The gray dashed lines indicate the RMSEs
of the old models. The gray dotted lines represent the RMSEs and BCLTX values achieved by CART. All plotted values are
averaged over 100 trials. Overall, CART-BCTX achieves a reasonable trade-off between RMSE and BCLTX.
Figure 4: Resulting BCP values (higher is better). BCTX-tmpdenotes CART-BCTX using 𝛿tmp. The plotted values represent the
mean over 100 trials with the standard deviation. CART-BCTX with𝛿 MAE or𝛿 MSE achieves higher BCP as𝜆increases.

Backward Compatibility in Tree-Based Explanations and Enhanced CART Algorithm KDD 2026, August 9–13, 2026, Jeju Island, Republic of Korea.
Figure 5: Resulting computation times. BCTX-tmpdenotes CART-BCTX using 𝛿tmp. The plotted values represent the mean over
100 trials with the standard deviation. The computation time of CART-BCTX is comparable to that of CART.
Figure 6: sample-averaged BCLTX (𝛿MSE), BCP, and loss values for CART, CART-BCTX (𝜆= 0.005,𝛿=𝛿 MSE), VFDT, and HAT.
The plotted values represent the mean over 100 trials with the standard deviation. The hatched areas mean the improvement
degrees of the losses. CART-BCTX offered a better balance of backward compatibility and accuracy than others in many cases.
has computational complexity comparable to that of the standard
decision tree construction algorithm CART. Experimental results on
10 real-world datasets covering both classification and regression
tasks demonstrated that CART-BCTX achieves favorable trade-offs
between predictive performance and BCLTX, with computation
times comparable to those of CART. In addition, we confirmed
that strengthening backward compatibility in explanations through
BCLTX also leads to improved backward compatibility in predic-
tions. Furthermore, we confirmed that CART-BCTX achieves supe-
rior performance in both predictive accuracy and BCLTX compared
with incremental decision trees under batch-wise evaluation. We
believe that our work supports the trustworthy deployment of de-
cision trees in risk-sensitive decision-making tasks, where trust in
model predictions is critically important.
Limitations and Future Work.There are three main future di-
rections. First, since constructing an optimal decision tree is com-
putationally intractable in general [ 12] (i.e., even in 𝜆= 0cases
for our situation), CART-BCTX is designed as a greedy algorithm.
From a practical perspective, it would be important to extend recent
efficient algorithms for learning near-optimal decision trees [3, 15]
so that they can handle BCLTX. Second, BCLTX does not explicitly
consider model updates under concept drift [ 18]. Under concept
drift, it is necessary to discuss for which samples backward compat-
ibility in explanations can or should be preserved. We report pre-
liminary experimental results of CART-BCTX under concept drift
scenarios in Appendix D. Finally, it remains to be investigated to
what extent strengthening backward compatibility in explanations
through BCLTX is meaningful in practice. To this end, conducting
user studies in realistic deployment settings, including synthetic
environments such as those considered by Bansal et al. [4], would
be an important direction for future work.
Acknowledgments
This work was supported by Japan Science and Technology Agency
(JST), ACT-X Grant Number JPMJAX24CE.
References
[1] J. Alcalá-Fdez, A. Fernández, J. Luengo, J. Derrac, S. García, L. Sánchez, and F.
Herrera. 2011. KEEL data-mining software tool: Data set repository, integration
of algorithms and experimental analysis framework.Journal of Multiple-Valued
Logic and Soft Computing17 (2011), 255–287. Issue 2-3.

KDD 2026, August 9–13, 2026, Jeju Island, Republic of Korea. Hirofumi Suzuki
[2] Alejandro Barredo Arrieta, Natalia Díaz-Rodríguez, Javier Del Ser, Adrien Ben-
netot, Siham Tabik, Alberto Barbado, Salvador Garcia, Sergio Gil-Lopez, Daniel
Molina, Richard Benjamins, Raja Chatila, and Francisco Herrera. 2020. Ex-
plainable Artificial Intelligence (XAI): Concepts, taxonomies, opportunities
and challenges toward responsible AI.Information Fusion58 (2020), 82–115.
doi:10.1016/j.inffus.2019.12.012
[3] Varun Babbar, Hayden McTavish, Cynthia Rudin, and Margo I Seltzer. 2025. Near
Optimal Decision Trees in a SPLIT Second. InProceedings of the 42nd International
Conference on Machine Learning. 2114–2175.
[4] Gagan Bansal, Besmira Nushi, Ece Kamar, Daniel S. Weld, Walter S. Lasecki, and
Eric Horvitz. 2019. Updates in human-ai teams: Understanding and addressing
the performance/compatibility tradeoff. In33rd AAAI Conference on Artificial
Intelligence (AAAI 2019). AAAI Press, Washington, DC, 2429–2437. doi:10.1609/
aaai.v33i01.33012429
[5] Albert Bifet and Ricard Gavaldà. 2009. Adaptive learning from evolving data
streams. InAdvances in Intelligent Data Analysis VIII. IDA 2009. Lecture Notes in
Computer Science, vol 5772., Vol. 5772 LCNS. Springer. doi:10.1007/978-3-642-
03915-7_22
[6] Leo Breiman, Jerome H. Friedman, Richard A. Olshen, and Charles J. Stone.
1984.Classification And Regression Trees. Routledge, New York. doi:10.1201/
9781315139470
[7] Pedro Domingos and Geoff Hulten. 2000. Mining high-speed data streams. In
Proceeding of the Sixth ACM SIGKDD International Conference on Knowledge
Discovery and Data Mining. 71–80. doi:10.1145/347090.347107
[8] Filip Karlo Dosilovic, Mario Brcic, and Nikica Hlupic. 2018. Explainable artifi-
cial intelligence: A survey. In2018 41st International Convention on Information
and Communication Technology, Electronics and Microelectronics, MIPRO 2018 -
Proceedings. IEEE, 210–215. doi:10.23919/MIPRO.2018.8400040
[9] Mohammad M. Ghiasi, Sohrab Zendehboudi, and Ali Asghar Mohsenipour. 2020.
Decision tree-based diagnosis of coronary artery disease: CART model.Computer
Methods and Programs in Biomedicine192 (2020), 105400. doi:10.1016/j.cmpb.
2020.105400
[10] Michael Bonnell Harries. 1999.SPLICE-2 Comparative Evaluation: Electricity
Pricing. Technical Report. The University of South Wales.
[11] Geoff Hulten, Laurie Spencer, and Pedro Domingos. 2001. Mining time-changing
data streams. InProceedings of the Seventh ACM SIGKDD International Conference
on Knowledge Discovery and Data Mining. ACM Press. doi:10.1145/502512.502529
[12] Laurent Hyafil and Ronald L. Rivest. 1976. Constructing optimal binary decision
trees is NP-complete.Inform. Process. Lett.5 (1976), 15–17. Issue 1. doi:10.1016/
0020-0190(76)90095-8
[13] Shashidhar Kaparthi and Daniel Bumblauskas. 2020. Designing predictive main-
tenance systems using decision tree-based machine learning techniques.Interna-
tional Journal of Quality and Reliability Management37 (2020), 659–686. Issue 4.
doi:10.1108/IJQRM-04-2019-0131
[14] Markelle Kelly, Rachel Longjohn, and Kolby Nottingham. [n. d.]. The UCI Machine
Learning Repository. https://archive.ics.uci.edu.
[15] Hector Kohler, Riad Akrour, and Philippe Preux. 2025. Breiman meets Bellman:
Non-Greedy Decision Trees with MDPs. InProceedings of the ACM SIGKDD
International Conference on Knowledge Discovery and Data Mining, Vol. 2. As-
sociation for Computing Machinery, New York, NY, United States, 1207–1218.
doi:10.1145/3711896.3736868
[16] Dominik Kreuzberger, Niklas Kuhl, and Sebastian Hirschl. 2023. Machine Learn-
ing Operations (MLOps): Overview, Definition, and Architecture.IEEE Access11
(2023), 31866–31879. doi:10.1109/ACCESS.2023.3262138
[17] Satyapriya Krishna, Tessa Han, Alex Gu, Steven Wu, Shahin Jabbari, and
Himabindu Lakkaraju. 2024. The Disagreement Problem in Explainable Ma-
chine Learning: A Practitioner’s Perspective.Transactions on Machine Learning
Research2024 (2024).
[18] Jie Lu, Anjin Liu, Fan Dong, Feng Gu, Joao Gama, and Guangquan Zhang. 2019.
Learning under Concept Drift: A Review.IEEE Transactions on Knowledge and
Data Engineering31 (2019). Issue 12. doi:10.1109/TKDE.2018.2876857
[19] Scott M. Lundberg and Su In Lee. 2017. A unified approach to interpreting
model predictions. InProceedings of the 31st International Conference on Neural
Information Processing Systems, Vol. 2017-December. Curran Associates Inc., Red
Hook, NY, United States, 4768–4777.
[20] Ryuta Matsuno. 2024. Backward Compatibility in Attributive Explanation and
Enhanced Model Training Method. In27th European Conference on Artificial
Intelligence (ECAI 2024), Vol. 392. 1011–1018. doi:10.3233/FAIA240591
[21] Ryuta Matsuno and Keita Sakuma. 2023. A Robust Backward Compatibility Metric
for Model Retraining. InProceedings of the 32nd ACM International Conference on
Informationand Knowledge Management (CIKM 2023). Association for Computing
Machinery, New York, NY, United States, 4190–4194. doi:10.1145/3583780.3615213
[22] Jacob Montiel, Max Halford, Saulo Martiello Mastelini, Geoffrey Bolmier, Raphael
Sourty, Robin Vaysse, Adil Zouitine, Heitor Murilo Gomes, Jesse Read, Talel
Abdessalem, and Albert Bifet. 2021. River: machine learning for streaming data
in Python.Journal of Machine Learning Research22 (2021), 1–8.
[23] Nurcan Ocal, Metin Kamil Ercan, and Eyup Kadioglu. 2015. Predicting Financial
Failure Using Decision Tree Algorithms: An Empirical Test on the Manufacturing
Industry at Borsa Istanbul.International Journal of Economics and Finance7
(2015), 189–206. Issue 7. doi:10.5539/ijef.v7n7p189
[24] Andrei Paleyes, Raoul Gabriel Urma, and Neil D. Lawrence. 2023. Challenges
in Deploying Machine Learning: A Survey of Case Studies.Comput. Surveys55
(2023), 1–29. Issue 6. doi:10.1145/3533378
[25] Tomoya Sakai. 2022. A Generalized Backward Compatibility Metric. InProceed-
ings of the ACM SIGKDD International Conference on Knowledge Discovery and
Data Mining. Association for Computing Machinery, New York, NY, United States,
1525–1535. doi:10.1145/3534678.3539465
[26] Megha Srivastava, Besmira Nushi, Ece Kamar, Shital Shah, and Eric Horvitz. 2020.
An Empirical Analysis of Backward Compatibility in Machine Learning Systems.
InProceedings of the ACM SIGKDD International Conference on Knowledge Dis-
covery and Data Mining. Association for Computing Machinery, New York, NY,
United States, 3272–3280. doi:10.1145/3394486.3403379
[27] Georgios Symeonidis, Evangelos Nerantzis, Apostolos Kazakis, and George A.
Papakostas. 2022. MLOps - Definitions, Tools and Challenges. In2022 IEEE 12th
Annual Computing and Communication Workshop and Conference, CCWC 2022.
IEEE, 453–460. doi:10.1109/CCWC54503.2022.9720902
[28] Xinru Wang and Ming Yin. 2023. Watch Out for Updates: Understanding the
Effects of Model Explanation Updates in AI-Assisted Decision Making. InProceed-
ings of the 2023 CHI Conference on Human Factors in Computing Systems(New York,
NY, USA). Association for Computing Machinery. doi:10.1145/3544548.3581366
[29] Tsukasa Yamakura, Yoichi Sasaki, Yuzuru Okajima, and Thiem Van Chu. 2025.
Retraining Gradient Boosting Decision Trees with Backward Compatibility of
Explanations. In29th Pacific-Asia Conference on Knowledge Discovery and Data
Mining (PAKDD 2025). Springer-Verlag, Berlin, Heidelberg, 68–79. doi:10.1007/
978-981-96-8173-0_6
[30] Ye Zhao, Ling Yang, Brad Lehman, Jean François De Palma, Jerry Mosesian, and
Robert Lyons. 2012. Decision tree-based fault detection and classification in solar
photovoltaic arrays. InConference Proceedings - IEEE Applied Power Electronics
Conference and Exposition - APEC. IEEE, 93–99. doi:10.1109/APEC.2012.6165803
A Details of Our Cost Complexity Prunig
Here, we describe CCP under BCLTX in detail. Our CCP minimizes
the following objective function.
𝑔(𝑇1,𝑇 ccp 2 ,𝐷 2,𝜆,𝛼):=𝑓(𝑇 1,𝑇 ccp 2 ,𝐷 2,𝜆)+𝛼#Leaves(𝑇 ccp 2 )(5)
In CCP, for each node𝑡 in𝑇2, we can compute the cost𝛼𝑡 required
to remove the subtree rooted at𝑡 and make𝑡 a new leaf node. Let
the set of samples associated with node𝑡be denoted as
𝐷𝑡 :={(𝒙,𝑦)∈𝐷 2|𝒙reaches the node𝑡}
Then, the value of the loss function 𝑓 restricted to the subtree
rooted at𝑡can be computed as follows.
𝑓𝑡(𝑇1,𝑇2,𝐷 2,𝜆):=
1
|𝐷2|
∑︁
(𝒙,𝑦)∈𝐷 𝑡
ℓ(𝑇2(𝒙),𝑦)+ 𝜆 |𝐷𝑠| ∑︁ (𝒙,𝑦)∈𝐷 𝑠∩𝐷𝑡 𝛿(𝑇1,𝑇2,𝒙)
Let ¯𝑇2,𝑡 denote the decision tree obtained by removing the subtree
rooted at𝑡 from𝑇2. Then, the value of the loss function𝑓 restricted
to the new leaf node𝑡in𝑇 2 can be computed as follows.
¯𝑓𝑡(𝑇1,𝑇2,𝐷 2,𝜆):=
1
|𝐷2|
∑︁
(𝒙,𝑦)∈𝐷 𝑡
ℓ( ¯𝑇2,𝑡(𝒙),𝑦)+ 𝜆 |𝐷𝑠| ∑︁ (𝒙,𝑦)∈𝐷 𝑠∩𝐷𝑡 𝛿(𝑇1, ¯𝑇2,𝑡,𝒙)
Then, the cost𝛼𝑡 can be computed as follows.
𝛼𝑡 =
¯𝑓𝑡(𝑇1,𝑇2,𝐷 2,𝜆)−𝑓 𝑡(𝑇1,𝑇2,𝐷 2,𝜆)
#DescendantLeaves(𝑡)−1 (6)
Here,# DescendantLeaves(𝑡) is the number of leaves in the subtree
rooted at𝑡on𝑇 2.
CCP iteratively removes the subtree rooted at the node𝑡 with
the minimum cost and then recomputes the costs on the resulting
decision tree. It is known that the costs of the removed nodes are
guaranteed to be monotonically non-decreasing, and these costs

Backward Compatibility in Tree-Based Explanations and Enhanced CART Algorithm KDD 2026, August 9–13, 2026, Jeju Island, Republic of Korea.
Algorithm 7UpdateTree-CV(𝑇 1,𝐷 2,𝜆,𝐾)
1:𝑇 2←CART-BCTX(𝐷 2,(𝑥 min 𝑗 )𝑚 𝑗=1,(𝑥 max 𝑗 )𝑚 𝑗=1,0)
2:A←Compute-𝛼-Path(𝑇 2,𝐷 2)
3:𝑓 𝛼←0for all𝛼∈A
4:for𝑘=1,...,𝐾do
5:𝐷 trn 2 ←Get training set of𝑘-th fold over𝐷 2
6:𝐷 val 2 ←Get validation set of𝑘-th fold over𝐷 2
7:𝑇 𝑘 2 ←CART-BCTX(𝐷 trn 2 ,(𝑥 min 𝑗 )𝑚 𝑗=1,(𝑥 max 𝑗 )𝑚 𝑗=1,0)
8:for𝛼∈Ain ascending orderdo
9:𝑇 𝑘 2 ←CostComplexityPruning(𝑇 𝑘 2,𝐷 trn 2 ,𝛼)
10:𝑇 𝑘,𝛼 2 ←PruneEquivalentSiblings(𝑇 𝑘 2)
11:𝑓 𝛼←𝑓 𝛼+𝑓(𝑇 1,𝑇𝑘,𝛼 2 ,𝐷 val 2 ,𝜆)
12:𝛼 ∗←argmin 𝛼{𝑓𝛼}
13:𝑇 ccp 2 ←CostComplexityPruning(𝑇 2,𝐷 2,𝛼∗)
14:𝑇 ccp 2 ←PruneEquivalentSiblings(𝑇 ccp 2 )
15:return𝑇 ccp 2
Algorithm 4Compute-𝛼-Path(𝑇 2,𝐷 2)
1:A←{0}
2:whileThe root node of𝑇 2 is not a leaf nodedo
3: Compute𝛼𝑡 for all the internal nodes of𝑇2 according to𝐷2
4:𝑡 ∗←argmin 𝑡{𝛼𝑡}
5:A←A∪{𝛼 𝑡∗}
6:𝑇 2← ¯𝑇2,𝑡∗
7:returnA
Algorithm 5CostComplexityPruning(𝑇 2,𝐷,𝛼)
1:whileThe root node of𝑇 2 is not a leaf nodedo
2: Compute𝛼𝑡 for all the internal nodes of𝑇2 treating𝐷 as𝐷2
3:𝑡 ∗←argmin 𝑡{𝛼𝑡}
4:if𝛼 𝑡∗ >𝛼then break
5:𝑇 2← ¯𝑇2,𝑡∗
6:return𝑇 2
Algorithm 6PruneEquivalentSiblings(𝑇)
1:Let𝑡be the root node of𝑇
2:if𝑡is a leaf nodethen
3:returnThe tree with only the node𝑡
4:Let𝑇 𝐿 and𝑇𝑅 be the left and right subtrees of𝑇, respectively
5:𝑇 𝐿←PruneEquivalentSiblings(𝑇 𝐿)
6:𝑇 𝑅←PruneEquivalentSiblings(𝑇𝑅)
7:Let𝑡 𝐿 and𝑡𝑅 be the left and right children of𝑡, respectively
8:if𝑡 𝐿 and𝑡𝑅 are leaf nodesthen
9:if
(
𝑦𝑡𝐿 =𝑦𝑡𝑅 (classification)
|𝑦𝑡𝐿−𝑦𝑡𝑅|≤𝜏(regression) then
10:returnThe tree with only the node𝑡
11: returnThe tree rooted at 𝑡 with the left subtree𝑇𝐿 and the
right subtree𝑇𝑅
serve as candidate values of 𝛼 (Algorithm 4). When performing
pruning for a given value of 𝛼, it suffices to continue removing
subtrees as long as the cost of the candidate node does not exceed
𝛼 (Algorithm 5). Notably, the behavior of CCP based on Eq. (5)
differs slightly from that of the standard CCP, in that it may pro-
duce sibling nodes with identical prediction values. While this can
be regarded as a consequence of preserving backward compatibil-
ity in explanations as much as possible, we recommend removing
such sibling nodes from the perspective of reducing redundancy in
the decision tree (Algorithm 6). In our experiments on regression
tasks, prediction equivalence is defined as having an absolute dif-
ference no greater than0.1%of the observed range of target values.
Taken together, the complete decision tree update algorithm, which
combines CART-BCTX with CCP using𝐾-fold cross-validation, is
summarized in Algorithm 7.
B Additional Experiments under Alternative
Update Settings
In the main body, we assumed that the old dataset𝐷1 is contained
in the new dataset𝐷2. However, depending on data retention poli-
cies in practical settings, two additional update scenarios can be
considered. One scenario is where𝐷1 and𝐷2 partially overlap, and
the other is where 𝐷1 and𝐷2 are disjoint. In the following, we
present additional experimental results under these two settings.
The datasets and the configurations of all algorithms are the same
as those used in the main experiments.
B.1 Partially Overlapping Old and New Datasets
We set the number of samples in the old dataset𝐷1 to1, 000and
that in the new dataset 𝐷2 to1, 000. In addition, we assume the
number of common samples in𝐷 1∩𝐷 2 to500. We conducted100
random trials for each dataset. Figure 7 (for classification tasks) and
Figure 8 (for regression tasks) present the predictive performance
and BCLTX values of the updated decision trees. Figure 9 shows the
BCP baseline obtained by CART and the BCP changes achieved by
CART-BCTX with varying𝜆. Figure 10 presents the computation
times of CART and CART-BCTX.
Although the trajectories with varying𝜆 are somewhat complex,
CART-BCTX generally exhibits a favorable trade-offs between pre-
dictive performances and BCLTX values. In terms of predictive per-
formance, naive updates using CART may in some cases degrade
performance relative to the old decision tree, whereas CART-BCTX
achieves substantial improvements in most cases. This behavior can
be attributed to the fact that CART-BCTX learns a new decision tree
while explicitly referencing the old decision tree. For both the trade-
off analysis and BCP changes, improvements obtained using𝛿MAE
or𝛿MSE are particularly effective, and execution of CART-BCTX
with𝛿MAE or𝛿MSE is recommended under this update setting as
well. In addition, the computation times of CART and CART-BCTX
remain comparable.
B.2 Disjoint Old and New Datasets
We set the number of samples in the old dataset𝐷1 to1, 000and that
in the new dataset𝐷2 to1, 000. In addition, we assume𝐷1∩𝐷 2 =∅ .
We conducted100random trials for each dataset. Figure 11 (for
classification tasks) and Figure 12 (for regression tasks) present the
predictive performance and BCLTX values of the updated decision
trees. Figure 13 shows the BCP baseline obtained by CART and the
BCP changes achieved by CART-BCTX with varying𝜆. Figure 14
presents the computation times of CART and CART-BCTX.

KDD 2026, August 9–13, 2026, Jeju Island, Republic of Korea. Hirofumi Suzuki
Except for the ‘adult‘ and ‘thyroid‘ datasets, CART-BCTX gener-
ally exhibits favorable trade-offs between predictive performances
and BCLTX values. For the ‘adult‘ dataset, substantial improve-
ments are observed with𝛿MSE for large𝜆. For the ‘thyroid‘ dataset,
moderate improvements are observed with 𝛿MAE for large𝜆. For
both the trade-off analysis and BCP changes, improvements ob-
tained using 𝛿MAE or𝛿MSE are again effective, and execution of
CART-BCTX with𝛿MAE or𝛿MSE is recommended under this update
setting as well. In addition, the computation times of CART and
CART-BCTX remain comparable.
C Visualized Tree Comparison
In this section, we compare specific examples of old/new deci-
sion trees, on the spambase dataset, obtained using each method
(CART, CART-BCTX, VFDT, and HAT) in Section 5.4. The trees are
illustrated in Figure 15. The task of spambase dataset is to deter-
mine whether a given email is spam (class 1) or not (class 0) via
word/character frequencies and capital run lengthes. In the tree
illustrations, we use the abbreviations “wf” for “word_freq”, “cf”
for “char_freq”, and “crl” for “capital_run_length”.
First, we compare the new decision trees (b) and (c) of CART and
CART-BCTX with the old decision tree (a) of CART. Although there
was only a little difference in the features added or removed by
the updates (a)→(b) and (a)→(c), the update (a)→(c) made smaller
changes in the thresholds of the shared features than the update
(a)→(b). As a result, the changes in the decision boundaries were
smaller for the update (a)→(c). In fact, 𝛿MSE was4 .17and2 .35
for the updates (a)→(b) and (a)→(c), respectively. Thus,we could
visually confirm the effectiveness of CART-BCTX for the backward
compatibility in tree-based explanations.
Next, we focus on the results of incremental decision trees VFDT
and HAT. The new decision trees (e) and (g) are generated by adding
some new branches to the old ones (d) and (f). Furthermore, most
of these new branches are based on features that are not used in
the old trees. As a result, both the updates (d) →(e) and (f)→(g)
significantly changed the decision boundaries. In fact, the values
of𝛿MSE were13.23for (d)→(e) and18.83for (f)→(g), respectively.
Thus,HAT may not necessarily maintain backward compatibility in
tree-based explanations.
D A Preliminary Analysis of CART-BCTX
under Concept Drift Settings
In this section, we present a preliminary analysis of how well CART-
BCTX preserves predictive performance and backward compatibil-
ity when a decision tree is repeatedly updated in a streaming envi-
ronment with concept drift. We update and evaluate the tree using
a "test-then-train" approach for sequentially arriving batches, and
quantify the prediction loss, backward compatibility in tree-based
explanations, and backward compatibility in predictions before and
after each update.
D.1 Setup
Dataset.We used the elec2 dataset [ 10] (45,312 samples in total),
which consists of real-world data and is available in the River li-
brary [22]. The task is a binary classification regarding electricity
supply and demand (whether the price is UP or DOWN). The fea-
tures included the continuous variables “nswprice”, “nswdemand”,
“vicprice”, “vicdemand”, and “transfer”, as well as the “day” of the
week (one-hot encoded as 7 categories) and the time period, which
was transformed usingsin and cos functions to preserve periodicity:
“period_sin” and “period_cos”. The stream was processed in batch-
wise manner by dividing the chronologically ordered samples into
batches at fixed intervals. Taking advantage of the fact that there
are 48 observations per day (at 30-minute intervals), we configured
three conditions with different update frequencies by setting the
batch length to 1-week, 2-week, and 4-week (48× 7samples per
week). The first batch was used for initial training, and evaluation
and updates were performed on each subsequent batch.
Competitors.We compared CART-BCTX, CART, HAT, and a
decision tree without update (the CART baseline for prediction loss).
For HAT, we used the implementation from the River library and set
“grace_period=48”, “delta=1e-5”, and “tau=0.01” for accommodating
the periodicity of the elec2 dataset. For CART-BCTX, we set 𝜆=
0.005and 𝛿=𝛿 MSE. For both CART and CART-BCTX, no depth
limit was imposed, the minimum sample size was set to 1% of the
number of samples in the training batch, and the post-pruning
process by CCP was performed using 5-fold cross-validation.
D.2 Results
Figure 16 summarizes the error rates, sample-averaged BCLTX
(𝛿MSE), and BCP values of CART, CART-BCTX, and HAT. We evalu-
ate these metrics across sequential batches with different update
intervals (1-week, 2-week, and 4-week settings), reporting only the
error rate for the no-update baseline.
First, in terms of predictive performance, CART and CART-BCTX
consistently achieved stable and superior error rates across all set-
tings. In contrast, HAT occasionally showed noticeable degradation,
sometimes performing worse than the no-update baseline. This in-
dicates that batch-wise retraining remains robust under repeated
updates, whereas HAT may exhibit instability.
Second, regarding BCLTX, HAT consistently achieved low values
in the 1-week and 2-week settings, indicating strong consistency
with recently observed data (336 and 672 samples). However, in
the 4-week setting (1,334 samples), HAT occasionally showed clear
increases in BCLTX, suggesting degradation from a medium- to
long-term periods. In contrast, CART exhibited large fluctuations,
while CART-BCTX reduced these fluctuations and maintained more
stable values for all settings.
Third, in terms of BCP, HAT occasionally exhibited notable drops
in several batches, indicating instability in preserving previously
correct predictions. In contrast, CART and CART-BCTX showed
stable BCP trends with comparable performance across all settings.
This suggests that enforcing backward compatibility in tree-based
explanations does not harm prediction consistency.
In summary,CART-BCTX achieves a balanced trade-off between
predictive performance and backward compatibility, with more sta-
ble behavior than CART and more consistent medium- to long-term
periods than HAT.

Backward Compatibility in Tree-Based Explanations and Enhanced CART Algorithm KDD 2026, August 9–13, 2026, Jeju Island, Republic of Korea.
Figure 7: Trade-offs for classification tasks under partially overlapping old and new datasets.

KDD 2026, August 9–13, 2026, Jeju Island, Republic of Korea. Hirofumi Suzuki
Figure 8: Trade-offs for regression tasks under partially overlapping old and new datasets.
Figure 9: BCP values (higher is better) for CART and CART-BCTX under partially overlapping old and new datasets.

Backward Compatibility in Tree-Based Explanations and Enhanced CART Algorithm KDD 2026, August 9–13, 2026, Jeju Island, Republic of Korea.
Figure 10: Computation times for CART and CART-BCTX under partially overlapping old and new datasets.
Figure 11: Trade-offs for classification tasks under disjoint old and new datasets.

KDD 2026, August 9–13, 2026, Jeju Island, Republic of Korea. Hirofumi Suzuki
Figure 12: Trade-offs for regression tasks under disjoint old and new datasets.
Figure 13: BCP values (higher is better) for CART and CART-BCTX under disjoint old and new datasets.

Backward Compatibility in Tree-Based Explanations and Enhanced CART Algorithm KDD 2026, August 9–13, 2026, Jeju Island, Republic of Korea.
Figure 14: Computation times for CART and CART-BCTX under disjoint old and new datasets.
(a) CART (Old)
 (b) CART (New, Naive)
 (c) CART (New, BCTX)
(d) VFDT (Old)
 (e) VFDT (New)
 (f) HAT (Old)
 (g) HAT (New)
Figure 15: Specific examples of old/new decision trees on the spambase dataset.

KDD 2026, August 9–13, 2026, Jeju Island, Republic of Korea. Hirofumi Suzuki
Figure 16: Performance under concept drift situation using elec2 dataset.
