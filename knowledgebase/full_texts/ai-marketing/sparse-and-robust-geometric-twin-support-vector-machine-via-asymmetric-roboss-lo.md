---
title: Sparse and robust geometric twin support vector machine via asymmetric RoBoSS loss function
url: https://arxiv.org/abs/2608.11567
category: ai-marketing
subcategory: measurement
date: 2026-08
venue: ''
authors:
- Kai Qi
- Xinji Huang
- Hongchun Wang
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.11567
pages: 35
chars: 69526
fetched_at: '2026-11-08T13:28:04+00:00'
kb_version: 1
---

# Sparse and robust geometric twin support vector machine via asymmetric RoBoSS loss function

Sparse and robust geometric twin support vector machine
via asymmetric RoBoSS loss function
Kai Qia, Xinji Huang b, Hongchun Wangb,∗
aNational Center for Applied Mathematics in Chongqing, Chongqing Normal University, Chongqing,
401331, China.
bSchool of Mathematical Sciences, Chongqing Normal University, Chongqing, 401331, China.
Abstract
In real-world scenarios, the training data usually contains redundant features, label
noise and feature noise, which provide severe challenges for the e ﬃciency of machine
learning methods. Since standard support vector machine (SVM) adopts l2-norm
penalty and hinge loss function, it lacks the ability of selecting signiﬁcant features
and is sensitive to noise. To address these issues, this paper proposes a novel asym-
metric, robust, bounded, sparse and smooth (aR) loss function for l1-norm penalized
geometric twin SVM (aRSGTSVM) to handle classiﬁcation and regression tasks. The
l1-norm penalty can achieve the feature selection. The proposed aR loss function can
not only e ﬀectively mitigate the impact of label noise, but also signiﬁcantly enhance
the stability to resampling noise, i.e., the zero-mean feature noise around the boundary
hyperplanes. Furthermore, a statistical analysis of the robustness of aRSGTSVM was
also conducted using the inﬂuence function. Since aRSGTSVM involves nonconvex
and nonsmooth optimization, we develop a fast and stable proximal gradient descent
based solving algorithm. Compared with related state-of-the-art methods, experimen-
tal results demonstrate the superiority of the proposed aRSGTSVM on both synthetic
and UCI datasets. Furthermore, we apply aRSGTSVM to index tracking tasks, where
results for tracking the di ﬀerent indices in the China stock market show that it can
achieve satisfactory performance.
∗Corresponding author. Email: wanghc@cqnu.edu.cn
Email addresses: qikai@cqnu.edu.cn (Kai Qi), 2024110510040@stu.cqnu.edu.cn (Xinji
Huang)
arXiv:2608.11567v1  [cs.LG]  12 Aug 2026

Keywords: Feature selection, robustness, geometric twin classiﬁcation and regression,
asymmetric RoBoSS loss function, nonconvex and nonsmooth optimization
1. Introduction
Twin support vector machine (TSVM) [ 1] is one of the well-known variants of the
support vector machine, which has experienced prosperous developments in the past
decade and has been widely applied into di ﬀerent ﬁelds, such as digit recognition [ 2],
medical diagnosis [ 3, 4] and bioanalysis [ 5]. From a geometric perspective, TSVM
aims to ﬁnd a pair of nonparallel separating hyperplanes, where each hyperplane is
required to be close to the samples of one class while being far from those of the other
class. This makes TSVM more ﬂexible and e ﬃcient than standard SVM. Moreover,
similar to SVM, the standard TSVM can also be explained from a statistical point of
view, i.e., it ﬁts the “loss + penalty” regularization framework [ 3, 6]. Speciﬁcally,
most of the existing TSVM adopt hinge loss and l2-norm penalty. However, hinge loss
is proved to be sensitive to label noise [ 7, 8] and resampling noise (zero-mean feature
noise around the boundary hyperplanes) [ 9]. The l2-norm penalty lacks the ability
to perform feature selection [ 10, 11]. Therefore, there remains signiﬁcant room for
improving the eﬃciency of TSVM in handling complex real-world problems.
The label noise sensitivity of SVMs and TSVMs stems mainly from the upper-
unbounded nature of the hinge loss. Speciﬁcally, label noise usually lies near or even
on the wrong side of the separating hyperplane. For such samples, the losses can be
quite large due to the unboundedness of hinge loss function. Consequently, the ﬁnal
obtained separating hyperplane tends to be deviated by label noise by the minimiza-
tion of the optimization objective. To address this issue, researchers have turned to
nonconvex loss functions to enhance robustness against label noise. By considering
the diﬀerence between the logistic loss and its shifted version, Krause and Singer [ 12]
proposed logistic di ﬀerence (LD) loss for SVM to reduce the inﬂuence of label noise.
Wu and Liu [ 7] integrated a truncated hinge loss, so-called ramp loss, with SVM to
enhance the robustness. Later, Liu et al. [ 13] combined the ramp loss with TSVM to
propose robust nonparallel SVM (RNPSVM). Wang et al. [ 14] constructed a capped
2

l1-norm loss for robust TSVM. Wang et al. [ 8] designed a new truncated squared loss
to obtain a robust SVM ( Ltsl-SVM). In addition to truncation, correntropy is also an ef-
fective approach of designing robust losses [ 15, 16]. Xu et al. [ 17] developed the idea
of correntropy to SVM and proposed rescaled hinge loss SVM, which can alleviate the
disturbance of outliers. Xu et al. [ 18] studied the correntropy based loss (C-loss) for
least squares SVM. Ma et al. [ 19] constructed a novel adaptive capped loss derived
from correntropy to enhance TSVM’s resistance to label noise. Recently, Akhtar et al.
[20] introduced a novel robust, bounded, sparse and smooth (RoBoSS) loss function
for SVM, to mitigate the impact of label noise. However, RoBoSS loss ignores the
perturbation of resampling noise and the performance needs further improving.
Regarding resampling noise, Huang et al. [ 9] ﬁrst demonstrated that hinge loss-
based separating hyperplanes are sensitive to zero-mean feature noise near the bound-
ary. Consequently, solutions derived from resampling procedures, such as K-fold
cross-validation lack stability. Inspired by statistical quantiles, they introduced the
pinball loss to SVM (PinSVM) to enhance its resampling stability. The authors [ 21]
further extended this idea to squared loss, developing an asymmetric least squares SVM
with a smooth, easily optimized objective function. A key limitation of PinSVM is the
loss of sample sparsity. Speciﬁcally, all training samples become support vectors. This
drawback can increase the training burden [ 9]. To encourage the sparsity, Shen et al.
[22] proposed a truncated pinball loss, which can provide a ﬂexible trade-o ﬀ between
sparsity and feature noise insensitivity. Motivated by quantiles and correntropy, Y ang
and Dong [ 23] proposed a generalized quantile loss. Based on the least squares SVM,
He et al. [ 24] established an asymmetric kernel-based learning classiﬁer.
For redundant features, they often provide irrelevant or even misleading informa-
tion for the modelling process. As a result, the predicting performance may degrade.
Zhu et al. [ 10] replaced l2-norm penalty by l1-norm penalty to propose 1-norm SVM,
which can select signiﬁcant features and remove redundant features, simultaneously.
Ikeda and Murata [ 25] investigated the geometrical properties of lp-norm penalized ν-
SVM, where 1 ≤ p ≤ ∞ . Zhu et al. [ 11] integrated elastic net with SVM to construct
doubly regularized SVM (DrSVM). In many real-world scenarios, input features ex-
hibit a grouped structure. Consequently, there is greater interest in performing feature
3

selection or elimination at the group level rather than on an individual basis. To achieve
group selection, Zou and Y uan [26] applied the inﬁnity norm for each group of features
to propose F∞-nrom SVM. Gao et al. [ 27] employed l1-norm penalty for least squares
TSVM to automatically select input features. Moosaei and Hladík [ 28] proposed lp-
norm (0 < p < 1) least squares twin multi-class SVM. With p ≥ 1, Xie et al. [ 29]
designed Laplacian lp-norm least squares TSVM.
Despite advances in robust SVM methods, existing approaches su ﬀer critical lim-
itations that hinder practical use. Label-noise-robust losses such as ramp loss, capped
loss, and RoBoSS typically ignore resampling noise, while resampling-stable variants
like pinball loss remain sensitive to label noise. Most robust losses either sacriﬁce
sparsity or introduce nonconvexity with hyperparameters lacking theoretical tuning
guidance. Moreover, few prior methods address label noise, resampling instability,
and redundant feature interference simultaneously within a uniﬁed framework. No-
tably, RoBoSS lacks resampling-noise resistance and its feature-selection performance
remains unexplored. In this paper, to address the aforementioned issues, we propose
a novel asymmetric RoBoSS loss-based sparse geometric TSVM (aRSGTSVM). The
proposed asymmetric RoBoSS loss is smooth and bounded, which can mitigate the
impact of label noise and resampling noise, simultaneously. Moreover, aRSGTSVM
incorporates an l1-norm penalty to enable feature selection.
In short, the main contributions are summarized as follows:
1) We propose a new asymmetric and robust (aR) loss function. Especially, com-
pared with RoBoSS loss function, the proposed aR loss function can not only e ﬀec-
tively mitigate the impact of label noise, but also enhance the stability to the zero-mean
noise near the boundary hyperplanes (so-called resampling noise).
2) We employ inﬂuence function to demonstrate the robustness of aR loss function.
Although there is extensive literature on enhancing SVM robustness by constructing
non-convex functions, few studies theoretically elucidate the robustness of the con-
structed functions. From a statistical perspective, we further proved that the inﬂuence
function of aR loss is bounded, thereby providing a theoretical guarantee of its robust-
ness.
3) Based on the aR loss and l1-norm penalty, the aRSGTSVM models are proposed
4

for robust classiﬁcation and regression learning problems (In the following content,
we refer to the regression model as aRSGTSVR to avoid confusion). In addition to
robustness, the proposed aRSGTSVM and aRSGTSVR can also reduce the inﬂuence
of noise features.
4) To optimize the nonconvex and nonsmooth aRSGTSVM and aRSGTSVR op-
timization problems, we design an e ﬃcient algorithm based on the proximal gradient
descent algorithm, termed as iPiano algorithm. The implemented algorithm is demon-
strated to be fast and stable, and is applicable to high-dimensional learning problems.
5) A lot of numerical studies on synthetic and benchmark datasets demonstrate
that the proposed aRSGTSVM and aRSGTSVR are robust against label noise and
resampling noise, while maintaining excellent feature selection capability in high-
dimensional settings.
6) To further validate the generalization capability, we apply the model into index
tracking task. The results show that aRSGTSVR delivers consistently superior perfor-
mance across di ﬀerent underlying indices.
The rest of paper is organized as follows: Section 2 introduces the related work of
this paper. Section 3 proposes the aR loss function and applies it to both classiﬁcation
and regression problems. Section 4 presents a lot of experimental results of the pro-
posed models on artiﬁcial datasets, UCI datasets and real-world stock datasets. Finally,
in Section 5, we revisit the main contributions of this paper and provide a concluding
remark.
2. Preliminaries and related work
First, we deﬁne some necessary notation. Consider a supervised learning data
{(xT i , yi)T }n i=1 with n samples and p features, where xi = (xi1, xi2, · · · , xip )T ∈ Rp is
the i-th sample. Note that yi ∈ {± 1} means a binary classiﬁcation problem, while
yi ∈ R means a regression problem. Furthermore, let Y = (y1, y2, · · ·yn)T ∈ Rn and
X = (x1, x2, · · · xn)T ∈ Rn×p. The positive and the negative samples are reorganized as
X+ and X−, respectively. Unless otherwise speciﬁed, all the vectors mentioned below
are in column-form and the norm defaults to the l2-norm.
5

2.1. ENNHSVM
For the standard TSVM, its training process does not fully consider the core re-
quirement of comparing distances to each separating hyperplane in the prediction stage,
leading to an inconsistency between the training and prediction processes. As [ 30]
pointed out, this inconsistency can possibly reduce the prediction performance, espe-
cially in the datasets with heteroscedastic noise.
Recently, Qi and Y ang [ 3] proposed a novel consistent ENNHSVM, which per-
forms better than the standard TSVM. Speciﬁcally, ENNHSVM pursues two nonparal-
lel hyperplanes by optimizing the following problems:
min c1
2

∥X+w+ + e+b+∥2 + ∥X−w− + e−b−∥2
+ 1 2  ∥w+∥2 + b2 + + ∥w−∥2 + b2 − 
+ c2
2

∥ξ+∥2 + ∥ξ−∥2 + c3  eT +ξ+ + eT −ξ− 
s.t.
8>>>><>>>>: X+w+ + e+b+ + X+w− + e+b− ≥ e+ − ξ+, ξ+ ≥ 0, X−w− + e−b− + X−w+ + e−b+ ≤ ξ− − e−, ξ− ≥ 0,
(1)
where w± and b± are the normal vectors and intercepts of the positive and negative
hyperplanes. ci (i = 1, 2, 3) are positive tuning parameters, ξ± are slack variables and
e± are two vectors with all elements equaling to one.
After obtaining w± and b±, for a given new sample xnew, its label can be classiﬁed
via the following decision function:
fxnew  = sign  xT new w+ + w−  + b+ + b−  , (2)
where sign(·) denotes the sign function.
Although ENNHSVM is consistent and demonstrated to be e ﬃcient, it cannot per-
form feature selection and exhibits poor performance in the presence of redundant vari-
ables. Moreover, its application in regression has not yet been explored in depth.
6

2.2. RoBoSS loss for SVM
To reduce the impact of label noise, recently, Akhtar et al. [ 20] proposed a robust,
bounded, sparse and smooth loss (RoBoSS). They incorporated the RoBoSS loss into
the SVM framework, resulting in a novel robust RoBoSS-SVM.
In detail, RoBoSS loss is deﬁned as
LRoBoS S (u) =
8>>>>><>>>>>: λ1 − (au + 1) exp(−au), u > 0, 0, u ≤ 0, (3)
where a is the shape parameter and λ is the boundary parameter. The primal problem
of RoBoSS-SVM can be formulated as
min
w,b
1
2 ∥w∥2 + C n nX i=1 LRoBoSS  1 − yi  wT xi + b  . (4)
where w and b are the normal vector and intercept of the separating hyperplane. C > 0
is the tuning parameter.
3. The proposed aRSGTSVM(R)
As discussed earlier, although the RoBoSS loss is robust to noise, it exhibits in-
stability to resampling. In this chapter, an asymmetric version of the RoBoSS loss,
termed aR loss, is proposed to address more complex noise in high-dimensional learn-
ing. Speciﬁcally, Section 3.1 introduces the aR loss and investigates its theoretical
properties. Section 3.2 presents the aRSGTSVM method for classiﬁcation problems,
while Section 3.3 proposes the aRSGTSVR model for regression scenarios. Finally,
Section 3.4 provides the corresponding optimization algorithm.
3.1. asymmetric RoBoSS loss
Although the RoBoSS loss demonstrates considerable robustness to label noise,
Huang et al. [ 31] point out that in many practical problems, beyond outliers, high-
dimensional complex data may also be a ﬀected by other types of noise, such as re-
sampling noise or zero-mean noise near the bounding hyperplane. However, one-sided
7

loss functions like the hinge loss and RoBoSS loss struggle to e ﬀectively mitigate the
impact of such noise, leading to unstable model performance and leaving room for im-
provement. Therefore, to further enhance the capability of the RoBoSS loss in handling
complex data, we propose a new loss function named aR, which is deﬁned as follows:
LaR(u) =
8>>>>><>>>>>: λ1 − (au + 1) exp(−au), u > 0, τλ1 − (au2 + 1) exp(−au2), u ≤ 0, (5)
where the shape parameter a > 0, the margin parameter λ > 0, and the parameter
τ ∈ [0, 1] control the asymmetry of the loss function, thereby enhancing the model’s
robustness to resampling noise.
Next, we elaborate on the properties of the proposed aR loss function.
Property 1. The aR loss function is C1-smooth.
Proof. First, by (5), it follows that
∇LaR(u) =
8>>>>><>>>>>: λa2u exp(−au), u > 0, 2τλa2u3 exp(−au2), u ≤ 0, (6)
Thus, we can deduce that ∇LaR(0+) = 0 and ∇LaR(0−) = 0. According to ( 5), we have
limu→0+ LaR(u) = limu→0− LaR(u) = LaR(0) = 0, which implies that LaR(u) is continuous
at u = 0. Consequently, the aR loss is a C1-smooth function. □
Property 2. The aR loss function is bounded.
Proof. For u > 0, we have ∇LaR(u) = λa2u exp(−au) > 0, which implies
that LaR(u) is strictly monotonically increasing on (0 , +∞). For u < 0, we have
∇LaR(u) = 2τλa2u3 exp(−au2) < 0, which implies that LaR(u) is strictly monotonically
decreasing on ( −∞, 0). According to the monotonicity above, the function reaches its
global minimum at u = 0, and LaR(0) = 0, which means that the loss function is lower
bounded by 0.
Next, we analyze the upper bound of the function by calculating the limits at inﬁn-
ity:
lim
u→+∞
LaR(u) = λ, lim u→−∞ LaR(u) = τλ. (7)
8

Since 0 < τ ≤ 1, we have τλ ≤ λ. Combined with monotonicity on both intervals,
all function values satisfy
0 ≤ LaR(u) ≤ λ, ∀u ∈ R. (8)
Therefore, the aR loss function is both lower bounded and upper bounded, namely,
it is bounded on R. □
Property 3. The aR loss is robust to label noise (outliers), which can be theoreti-
cally guaranteed by inﬂuence function.
Proof. Hampel introduced the inﬂuence function [ 32], which is mainly used to
measure the stability of an estimator when subjected to inﬁnitesimal contamination.
For an ideal roust loss function, the inﬂuence function of the induced estimator is
bounded.
Following [33] and by ( 6), we have that ∇laR achieves its maximum at u = 1 a for
u > 0, while it achieves its maximum at u = −
q
3
2a for u ≤ 0. Therefore, it follows that
|IF(u)| ≤ max
0BBBB@ λa e , 3τλ √ 6a 2e3/2 1CCCCA < ∞, ∀u ∈ R. (9)
Therefore, according to the inﬂuence function theory, for the SVM model designed
based on the aR loss, even if the loss u caused by label noise is extremely large, their
impact on the model is still limited. This theoretically guarantees the robustness of the
aR loss.
Figure 1 illustrates the various forms of the aR loss function under di ﬀerent param-
eters. Combined with the preceding propositions, the asymmetric RoBoSS (aR) loss
function is a bounded, asymmetric, smooth, and non-convex function. Consequently,
compared to the original RoBoSS loss, our proposed loss function is not only robust
to outliers but also resilient to zero-mean feature noise, enabling it to handle more
complex problems.
9

0.0
0.5
1.0
1.5
−4 −2 0 2 4
u
loss
type
a=1
a=2
a=3
a=4
(a) Di ﬀerent a values
0.0
0.5
1.0
1.5
−4 −2 0 2 4
u
loss
type
λ=0.5
λ=1
λ=1.5
λ=2 (b) Di ﬀerent λ values
0.0
0.5
1.0
−4 −2 0 2 4
u
loss
type
τ=0.2
τ=0.4
τ=0.6
τ=0.8 (c) Di ﬀerent τ values
Figure 1: Illustrations of di ﬀerent parameter values of the proposed aR loss function
3.2. aR loss-based sparse geometric TSVM
In this section, we mainly study the classiﬁcation problems. Since the proposed
aR loss can e ﬀectively mitigate the impact of outliers and strengthen the stability to
resampling noise, simultaneously. We propose a novel sparse and robust geometric
twin support vector machine(aRSGTSVM), which integrates the aR loss function with
ENNHSVM, thereby inheriting the consistency properties of ENNHSVM. The result-
ing expression is as follows:
min c1
2

∥X+w+ + e+b+∥2 + ∥X−w− + e−b−∥2
+ λ (∥w+∥1 + |b+| + ∥w−∥1 + |b−|)
+ c2
0BBBBBB@ X
i∈N+
LaR ((ξ+)i) +
X
i∈N−
LaR ((ξ−)i)
1CCCCCCA
s.t.
8>>>>>>>>><>>>>>>>>>: X+w+ + e+b+ + X+w− + e+b− ≥ e+ − ξ+, X−w− + e−b− + X−w+ + e−b+ ≤ ξ− − e−, ξ+ ≥ 0, ξ− ≥ 0, (10)
where N± denotes by the index sets of positive and negative samples. ( ξ±)i means the
i-th element of the slack variables. Other notations are similar to ENNHSVM.
In contrast to ENNHSVM, our proposed classiﬁer replaces the loss function in the
original model with the aR loss and incorporates an l1-norm penalty to equip the model
with feature selection capability. The core idea of the proposed aRSGTSVM is outlined
as follows:
10

1) Minimizing the ﬁrst term of the objective of ( 10) forces each hyperplane to be
closer to its corresponding class samples and farther from the other class, en-
hancing inter-class discrimination.
2) The second term ∥cdot∥1 induces sparsity in the model solution, enabling e ﬀec-
tive variable selection and handling of high-dimensional complex problems.
3) The third term employs the aR loss function, whose inherent properties pro-
vide robustness against label noise and resampling noise, thereby improving the
model’s generalization performance.
To simplify subsequent derivations, deﬁne the following notations: ˜X+ = (X+, e+),
˜X− = (X−, e−), ˜w± = (wT ±, b±)T and ˜w = ( ˜w+, ˜w−). Furthermore, let
A =
0BBBBBBBB@ ˜XT + ˜X+ 0 0 ˜XT − ˜X− 1CCCCCCCCA , B = 0BBBBBBBB@ ˜X+ ˜X+ − ˜X− − ˜X− 1CCCCCCCCA , e = 0BBBBBBBB@ e+ e− 1CCCCCCCCA , ξ = 0BBBBBBBB@ ξ+ ξ− 1CCCCCCCCA . (11)
Then, the aRSGTSVM problem ( 10) can be rewritten as:
min c1
2 ˜wT A ˜w + λ∥ ˜w∥1 + c2 2 ∥ξ∥2
s.t.
8>>>><>>>>: B ˜w ≥ e − ξ, ξ ≥ 0. (12)
which is equivalent to the following "loss + penalty" form, i.e.,
min
˜w
c1
2 ˜wT A ˜w + c2
nX
i=1
LaR(1 − bT i ˜w) + λ∥ ˜w∥1. (13)
where bi represents the i-th row vector of matrix B.
3.3. aR loss-based sparse geometric TSVR
To extend the application scope from discrete classiﬁcation to continuous predic-
tion, we apply aRSGTSVM to regression problems and propose aR loss-based sparse
geometric TSVR (aRSGTSVR).
11

Using the idea of TSVR [ 34], let X+ = (X+, Y + ε1e+) , X− = (X−, Y − ε2e−), w+ = 
wT +, η+
T
, w− =

wT −, η−
T
, where ε1, ε2 > 0 are tuning parameters. We ﬁrst transform
(10) into the following regression problem:
min c1
2

∥X+w+ + η+(Y + ε1e+) + e+b+∥2 + ∥X−w− + η−(Y − ε2e−) + e−b−∥2
+ λ (∥w+∥1 + |η+| + |b+| + ∥w−∥1 + |η−| + |b−|)
+ c2
0BBBBBB@ X
i∈N+
LaR ((ξ+)i) +
X
i∈N−
LaR ((ξ−)i)
1CCCCCCA
s.t.
8>>>>>>>>><>>>>>>>>>: X+w+ + η+(Y + ε1e+) + e+b+ + X+w− + η−(Y + ε1e+) + e+b− ≥ e+ − ξ+, X−w− + η−(Y − ε2e−) + e−b− + X−w+ + η+(Y − ε2e−) + e−b+ ≤ ξ− − e− < 0, ξ+ ≥ 0, ξ − ≥ 0.
(14)
Analogously to the classiﬁcation problem, we further deﬁne the following vari-
ables: ˜X+ = (X+, Y + ε1e+, 1) , ˜X− = (X−, Y − ε2e−, 1) , ˜w+ =  wT +, η+, b+ T , ˜w− = 
wT −, η−, b−
T
, ˜w =

˜wT +, ˜wT −
T
, as well as the corresponding matrices and vectors:
A =
0BBBBBBBB@ ˜XT + ˜X+ O O ˜XT − ˜X− 1CCCCCCCCA , B = 0BBBBBBBB@ ˜X+ ˜X+ − ˜X− − ˜X− 1CCCCCCCCA , e = 0BBBBBBBB@ e+ e− 1CCCCCCCCA , ξ = 0BBBBBBBB@ ξ+ ξ− 1CCCCCCCCA .
We rewrite (14) as:
min c1
2 ˜wT A ˜w + λ∥ ˜w∥1 + c2 2 ∥ξ∥2
s.t.
8>>>><>>>>: B ˜w ≥ e − ξ, ξ ≥ 0. (15)
Similar to the previous steps, we obtain the linear case of the aRSGTSVR model:
min c1
2 ˜wT A ˜w + c2
nX
i=1
LaR

1 − bT i ˜w  + λ∥ ˜w∥1. (16)
By utilizing the feature mapping Φ(·) that maps raw input space into a high dimen-
sional Reproducing Kernel Hilbert Space, the proposed aRSGTSVM(R) model can be
extended to the sparse kernel case. In fact, by only replacing X with Φ(X), we derive
12

the aRSGTSVM(R) model for the sparse kernel scenario. Note that feature selection is
one of the key focuses of this study, so we primarily consider the linear case
3.4. iPiano algorithm
Due to the non-convex aR loss function and non-smooth penalty term, Problem (10)
constitutes a non-convex optimization problem. Conventional solution approaches typ-
ically employ the di ﬀerence of convex functions (DC) algorithm or the half-quadratic
(HQ) algorithm, which require iteratively solving a series of subproblems and incur
substantial computational costs. Therefore, we opt to utilize the iPiano (Inertial Prox-
imal Algorithm for Nonconvex Optimization) algorithm [ 35] for optimization, which
oﬀers advantages of rapid convergence and numerical stability, particularly suited for
high-dimensional complex problems. The following derivation will be presented using
the classiﬁcation problem as an illustrative example.
3.4.1. iPiano for aRSGTSVM
The iPiano algorithm can solve optimization problems of the form:
min
x∈Rn
h(x) = f (x) + g(x), (17)
where g is convex (possibly nonsmooth), f is C1-smooth (possibly nonconvex).
Thus, (10) can also be interpreted as having the form " f + g" :
min
˜w
c1
2 ˜wT A ˜w + c2
nX
i=1
LaR

1 − bT i ˜w 
|                                    {z                                    }
f
+ λ∥ ˜w∥1|{z}
g
.
(18)
Let ui = 1 − bT i ˜w, then the objective function f is given by:
f ( ˜w) =
8>>>>>><>>>>>>: c1 2 ˜wT A ˜w + c2 nP i=1 λ1 − (aui + 1) exp (−aui) , ui > 0, c1 2 ˜wT A ˜w + c2 nP i=1 τλ  1 −  au2 i + 1  exp  −au2 i  , ui ≤ 0. (19)
13

Then ∇ f is obtained:
∇ f ( ˜w) =
8>>>>>><>>>>>>: c1A ˜w − c2 nP i=1 a2λbiui exp(−aui), ui > 0, c1A ˜w − c2 nP
i=1
2a2τλbiu3 i exp(−au2 i ), ui ≤ 0.
(20)
Here, L > 0 denotes an upper bound constant for the Lipschitz continuity of ∇ f ,
which satisﬁes the inequality
|∇ f ( ˜w1) − ∇ f ( ˜w2)| ≤ L∥ ˜w1 − ˜w2∥, ∀ ˜w1, ˜w2. (21)
Because
∇2 f ( ˜w) =
8>>>>><>>>>>: c1A − c2 Pn i=1 a2λbibT i (−1 + aui) exp(−aui), ui > 0, c1A − c2 Pn i=1 2a2τλbibT i  −3u2 i + 2au4 i  exp(−au2 i ), ui ≤ 0, (22)
we can get
L = c1∥A∥ + c2λa2 max

1, 2 |τ| a √e ! nX i=1 ∥bi∥2. (23)
The general framework of the iPiano algorithm for the problem ( 17) is presented in
the algorithm 1. In this work, we empirically set the maximum iteration number niter
to 500 and the error threshold ε to 10−6.
The proximal map is deﬁned by
(I + α∂g)−1( ˆx) := arg min
x∈Rn
(
αg(x) + 1 2 ∥x − ˆx∥2 2
)
, (24)
where I is the identity map, α > 0 is a given step size parameter, and g is a proper
lower semicontinuous convex function whose speciﬁc deﬁnition is given in ( 18).
3.4.2. iPiano for aRSGTSVR
According to (16) and (13), the aRSGTSVR model can be reformulated into a form
consistent with that of the aRSGTSVM. Thus, similarly to algorithm 1, the overall
procedure for solving the aRSGTSVR algorithm is shown in algorithm 2.
14

Algorithm 1 iPiano for aRSGTSVM
1: Input: Set step size parameters β = 0.5, α = 1 − β L , where L is the Lipschitz
constant of ∇ f , choose ˜w0 ∈ dom, h, ˜w−1 = ˜w0. The maximal iteration number
niter, and the convergent error ε.
2: Output: Optimal solution ˜w∗ of (10)
3: Initialize iteration counter n = 0
4: while n < niter do
5: ˜wn+1 = (I + αn∂g)−1 ˜wn − αn∇ f ( ˜wn) + βn( ˜wn − ˜wn−1)
6: if ∥ ˜wn+1 − ˜wn∥2 < ε then
7: break
8: end if
9: n = n + 1
10: end while
11: return ˜wn+1
Algorithm 2 iPiano for aRSGTSVR
1: Input: Set step size parameters β = 0.5, α = 1 − β L , where L is the Lipschitz
constant of ∇ f , choose ˜w0 ∈ dom, h, ˜w−1 = ˜w0. The maximal iteration number
niter, and the convergent error ε.
2: Output: Optimal solution ˜w∗ of (16)
3: Initialize iteration counter n = 0
4: while n < niter do
5: ˜wn+1 = (I + αn∂g)−1 ˜wn − αn∇ f ( ˜wn) + βn( ˜wn − ˜wn−1)
6: if ∥ ˜wn+1 − ˜wn∥2 < ε then
7: break
8: end if
9: n = n + 1
10: end while
11: return ˜wn+1
It is worth noting that the convergence of the proposed iPiano-based algorithm is
guaranteed by Theorem 4.8 in the iPiano framework established by Ochs et al. [ 35].
Speciﬁcally, for nonconvex and possibly nonsmooth objective functions, under the con-
dition that the objective satisﬁes the KurdykaLojasiewicz property and appropriate step
size parameters are adopted, it can be veriﬁed that the iterative sequence of the iPiano
algorithm converges to critical points. Consequently, the algorithm developed has a
solid theoretical convergence guaranty.
15

4. Numerical studies
In this section, to further investigate the performance of our proposed algorithm,
we design a series of numerical studies to compare aRSGTSVM and aRSGTSVR with
some well-known and recent robust methods to verify the performance of our proposed
aRSGTSVM and aRSGTSVR.
For the classiﬁcation problem, we compared the classical 1-SVM [ 36], TPMSVM
[37], Pin-TSVM [ 31], rhingeSVM [ 17], and RoBoSS-SVM [ 20]. The regularization
parameter λ in 1-SVM is selected from the candidate set Λ = {0.01, 0.02, 0.03, . . . ,0.99}.
For TPMSVM, we select the values of ν from the set {0.1, 0.2, . . . ,0.8, 0.9}. For
Pin-TSVM, the parameter ν from set {2i | i = −8, −7, . . . ,7, 8} and τ is tuned in
{0.1, 0.3, 0.5, 0.7, 0.9}. In the rhingeSVM, the η is assumed to be 1. For RoBoSS-
SVM, the parameters a and λ are selected from the set {1, 2, 3, 4, 5} and {0.5, 1, 1.5, 2}
, respectively. For the aRSGTSVM, the parameters a and λ are the same as those of
RoBoSS-SVM, and we take τ in the range {0.2, 0.5, 0.8}.
For the regression problem, we compared aRSGTSVR with SVR, LASSO, Elastic
Net, TSVR [ 38] and Res-TSVR [ 39]. In the SVR, the parameter ε is optimized in the
range {2i | i = −8, −7, . . . ,7, 8}. For TSVR, we set C1 = C2 and ε1 = ε2. For Res-
TSVR, the regularization parameters C1 = C2 and η in the range of {1, 3, . . . ,16}. For
the aRSGTSVR, the hyperparameters a, λ, and τ are optimized through a grid search
over the discrete sets {1, 2, 3, 4, 5}, {0.5, 1, 1.5, 2}, and {0.2, 0.5, 0.8}, respectively.
For all of the methods mentioned above, we have chosen the values of C and ε
from the following sets: {2i | i = −8, −7, . . . ,7, 8}. In the nonlinear case, we consider
the Gaussian kernel function, i.e. K(x1, x2) = exp(−γ∥x1 − x2∥2 2). The parameters γ
of the Gaussian kernel function take values in the range {2i | i = −8, −7, . . . ,7, 8}.
No training-test partition was performed in this study. All models were trained on
the entire dataset, and the reported accuracy values are averaged results from ﬁve-fold
cross-validation, with each fold acting as the validation set sequentially.
For classiﬁcation problems, using acc (accuracy) as our evaluation metric. For re-
gression problems, we evaluated the performance of the model using RMSE. MAE was
used during the simulations to select the optimal parameters. Their speciﬁc deﬁnitions
16

0
2
4
6
0 2 4
x1
x2
(a) 1-SVM
0
2
4
6
0 2 4
x1
x2 (b) TPMSVM
0
2
4
6
0 2 4
x1
x2 (c) Pin-TSVM
0
2
4
6
0 2 4
x1
x2
(d) rhingeSVM
0
2
4
6
0 2 4
x1
x2 (e) RoBoSS-SVM
0
2
4
6
0 2 4
x1
x2 (f) aRSGTSVM
Figure 2: The red solid lines represent the separating hyperplanes obtained by 1-SVM, TPMSVM, Pin-
TSVM, rhingeSVM, RoBoSS-SVM and aRSGTSVM. The Bayes classiﬁer is shown as a black dotted line.
Table 1: The accuracy(acc) and standard deviation (sd) with linear kernel. The bold is the best one.
label noise 1-SVM TPMSVM Pin-TSVM rhingeSVM RoBoSS-SVM aRSGTSVM
acc ± sd acc ± sd acc ± sd acc ± sd acc ± sd acc ± sd
no noise 0.950 ± 0.035 0.950 ± 0.055 0.950 ± 0.035 0.960 ± 0.055 0.950 ± 0.035 0.960 ± 0.022
5% 0.910 ± 0.082 0.910 ± 0.004 0.920 ± 0.057 0.910 ± 0.042 0.910 ± 0.065 0.920 ± 0.027
10% 0.850 ± 0.087 0.850 ± 0.004 0.850 ± 0.061 0.850 ± 0.061 0.850 ± 0.094 0.870 ± 0.057
20% 0.780 ± 0.104 0.770 ± 0.004 0.770 ± 0.130 0.770 ± 0.168 0.770 ± 0.076 0.790 ± 0.065
35% 0.620 ± 0.076 0.630 ± 0.004 0.630 ± 0.091 0.630 ± 0.076 0.630 ± 0.065 0.660 ± 0.074
are as follows:
RMSE =
vt
1
n
nX
i=1
(yi − ˆyi)2, MAE = 1 n nX i=1 |yi − ˆyi|, (25)
where n represents the number of samples used for testing.
4.1. Artiﬁcial datasets for classiﬁcation
Example 1. To evidence the robustness of aRSGTSVM to label noise, we con-
ducted an experiment using a two-dimensional synthetic dataset containing 100 sam-
ples. In this example, the samples were generated from two Gaussian distributions
with equal probability: xi, i ∈ { 1, 2, . . . ,50} ∼ N(u1, Σ1), xi, i ∈ { 51, 52, . . . ,100} ∼
N(u2, Σ2), where u1 = [2, 5]T , u2 = [4, 2]T and Σ1 = Σ 2 = diag(1, 2). In this case, the
17

−1
0
1
−2 −1 0 1 2
x1
x2
(a) 1-SVM
−1
0
1
−2 −1 0 1 2
x1
x2 (b) TPMSVM
−1
0
1
−2 −1 0 1 2
x1
x2 (c) Pin-TSVM
−1
0
1
−2 −1 0 1 2
x1
x2
(d) rhingeSVM
−1
0
1
−2 −1 0 1 2
x1
x2 (e) RoBoSS-SVM
−1
0
1
−2 −1 0 1 2
x1
x2 (f) aRSGTSVM
Figure 3: The black solid lines represent the separating hyperplanes obtained by 1-SVM, TPMSVM, Pin-
TSVM, rhingeSVM, RoBoSS-SVM and aRSGTSVM.
Bayes classiﬁer is fC(x) = 4x1 − 3x2 − 3 2 . To systematically investigate the impact of
label noise on model performance, experiments were conducted under varying noise
ratios.
In Figure 2 presents a noise-free condition, in which the black dotted line represents
the Bayesian optimal decision boundary and the red solid line represents the decision
boundary obtained from each model. Among the six models evaluated, our proposed
aRSGTSVM demonstrates the most satisfactory performance, with its decision bound-
ary showing the closest alignment to that of the Bayesian classiﬁer. The complete
experimental results are presented in Table 1, which demonstrate the remarkable ro-
bustness and noise insensitivity of our proposed aRSGTSVM.
Example 2. To exemplify the stability of SVM under resampling, a total of 160
samples were generated based on Example 1, with the parameters set tou1 = [0.8, −0.5]T ,
u2 = [−0.8, 0.5]T , and Σ1 = Σ 2 = diag(0.2, 0.2). The experiment was repeated 30 times.
As visualized in Figure 3, the proposed aRSGTSVM demonstrates exceptional
robustness and stability in constructing decision hyperplanes. Speciﬁcally, the hy-
perplanes of aRSGTSVM form a remarkably narrow and highly concentrated clus-
ter, with almost no variation across di ﬀerent resampling runs, highlighting its strong
18

Table 2: The accuracy (acc) and standard deviation (sd) in di ﬀerent (n, p). The bold is the best one.
(a) 0% label noise
1-SVM TPMSVM Pin-TSVM rhingeSVM RoBoSS-SVM aRSGTSVM
n = 50, p = 100 0.900 ± 0.071 0.920 ± 0.130 0.940 ± 0.055 0.900 ± 0.071 0.920 ± 0.110 0.940 ± 0.089
n = 50, p = 150 0.940 ± 0.055 0.920 ± 0.084 0.940 ± 0.055 0.920 ± 0.084 0.920 ± 0.084 0.960 ± 0.055
n = 100, p = 150 0.920 ± 0.027 0.930 ± 0.027 0.930 ± 0.076 0.920 ± 0.067 0.930 ± 0.057 0.970 ± 0.045
n = 100, p = 200 0.920 ± 0.076 0.910 ± 0.055 0.920 ± 0.084 0.910 ± 0.074 0.930 ± 0.045 0.960 ± 0.042
(b) 5% label noise
n = 50, p = 100 0.860 ± 0.114 0.880 ± 0.084 0.900 ± 0.122 0.860 ± 0.134 0.880 ± 0.045 0.920 ± 0.084
n = 50, p = 150 0.940 ± 0.055 0.900 ± 0.071 0.940 ± 0.055 0.920 ± 0.045 0.940 ± 0.089 0.960 ± 0.055
n = 100, p = 150 0.900 ± 0.035 0.880 ± 0.057 0.890 ± 0.108 0.880 ± 0.084 0.900 ± 0.100 0.940 ± 0.042
n = 100, p = 200 0.930 ± 0.084 0.920 ± 0.076 0.920 ± 0.057 0.910 ± 0.042 0.930 ± 0.045 0.950 ± 0.035
(c) 10% label noise
n = 50, p = 100 0.840 ± 0.134 0.840 ± 0.152 0.860 ± 0.114 0.840 ± 0.114 0.860 ± 0.055 0.880 ± 0.130
n = 50, p = 150 0.900 ± 0.100 0.880 ± 0.084 0.880 ± 0.084 0.880 ± 0.164 0.900 ± 0.071 0.920 ± 0.084
n = 100, p = 150 0.830 ± 0.104 0.840 ± 0.114 0.830 ± 0.076 0.810 ± 0.108 0.850 ± 0.087 0.870 ± 0.097
n = 100, p = 200 0.830 ± 0.097 0.800 ± 0.079 0.810 ± 0.082 0.810 ± 0.124 0.830 ± 0.144 0.870 ± 0.027
(d) 20% label noise
n = 50, p = 100 0.720 ± 0.228 0.700 ± 0.122 0.740 ± 0.207 0.720 ± 0.130 0.720 ± 0.179 0.780 ± 0.110
n = 50, p = 150 0.800 ± 0.071 0.840 ± 0.089 0.780 ± 0.110 0.780 ± 0.110 0.780 ± 0.084 0.840 ± 0.195
n = 100, p = 150 0.770 ± 0.130 0.770 ± 0.057 0.750 ± 0.112 0.770 ± 0.115 0.770 ± 0.084 0.800 ± 0.087
n = 100, p = 200 0.770 ± 0.115 0.760 ± 0.134 0.760 ± 0.055 0.740 ± 0.089 0.770 ± 0.104 0.790 ± 0.089
(e) 35% label noise
n = 50, p = 100 0.600 ± 0.100 0.600 ± 0.141 0.620 ± 0.084 0.560 ± 0.182 0.660 ± 0.195 0.680 ± 0.130
n = 50, p = 150 0.700 ± 0.071 0.660 ± 0.167 0.740 ± 0.089 0.660 ± 0.152 0.720 ± 0.148 0.780 ± 0.205
n = 100, p = 150 0.620 ± 0.057 0.610 ± 0.108 0.630 ± 0.097 0.600 ± 0.127 0.640 ± 0.089 0.660 ± 0.082
n = 100, p = 200 0.620 ± 0.115 0.600 ± 0.035 0.640 ± 0.055 0.590 ± 0.152 0.620 ± 0.104 0.670 ± 0.067
resistance to sample perturbations. While RoBoSS-SVM exhibits improved stability
relative to traditional SVM variants, its hyperplanes still show non-negligible disper-
sion. In sharp contrast, the baseline models, including 1-SVM, TPMSVM, Pin-TSVM
and rhingeSVM, generate widely scattered hyperplanes with substantial ﬂuctuations,
particularly in the boundary regions between classes. This dispersion reveals their sen-
sitivity to minor changes in the training data, resulting in unstable decision boundaries.
Beyond its robustness advantage, aRSGTSVM also achieves the most accurate separa-
tion between the two classes (red and blue points), e ﬀectively distinguishing between
the samples and delivering the best overall classiﬁcation performance among all eval-
uated models.
Example 3. In this example, the samples were generated from two multivariate
Gaussian distributions with equal probability: xi, i ∈ { 1, 2, . . . , n 2 } ∼ N(u1, Σ1), xi, i ∈
{ n 2 + 1, n 2 + 2, . . . ,n} ∼ N(u2, Σ2), where u1 = (0.1, 0.2, 0.3, 0.4, 0.5, 0, . . . ,0)T ∈ Rn,
u2 = −u1 and Σ1 = Σ 2 = (σi j) is deﬁned with non-zero elements: σii = 1, for i =
19

p = 300
p = 200
p = 100
0 0.1 0.2 0.3 0.4
0.00
0.25
0.50
0.75
1.00
0.00
0.25
0.50
0.75
1.00
0.00
0.25
0.50
0.75
1.00
Label Noise Ratio
Prediction Accuracy
Method aRSGTSVM SGTSVM (ablation)
Figure 4: The results of the ablation experiments under di ﬀerent ratios of label noise and number of features.
1, 2, . . . ,n and σi j = −0.2, for 1 ≤ i , j ≤ 5.
As shown in Table 2, we systematically compared the classiﬁcation performance
of the proposed aRSGTSVM with several state-of-the-art SVM-based methods across
diﬀerent combinations of sample size n, feature dimension p, and varying label noise
levels ranging from 0% to 35%. The results, measured by mean classiﬁcation accu-
racy and standard deviation, consistently demonstrate that aRSGTSVM achieves the
highest or tied-for-highest accuracy in nearly all experimental settings, including high-
dimensional scenarios where p > n, while maintaining stable performance across re-
peated trials. As label noise increases, aRSGTSVM consistently outperforms com-
peting methods, showing its superiority in both clean high-dimensional environments
and noisy conditions. This comprehensive comparison conﬁrms that the proposed aR-
SGTSVM exhibits stronger robustness against label noise and better adaptability to
high-dimensional data compared with baseline models, validating the e ﬀectiveness of
its asymmetric regularized twin SVM framework.
Example 4. To further verify the e ﬀectiveness of the proposed asymmetric Ro-
BoSS loss function, we conduct ablation experiments. Based on the setting of Exam-
ple 3, we ﬁx the sample size at n = 200, set the feature dimension p ∈ { 100, 200, 300}
20

10−2
10−1
100
101
102
103
50 60 70 8090100 200 400 600 800 1000 2000 3000 40005000600070008000900010000
log10(Sample Size)
Runing Time (s)
Classifier
1−SVM
TPMSVM
Pin−TSVM
rhingeSVM
RoBoSS−SVM
aRSGTSVM
Figure 5: The one-run CPU time cost of 1-SVM, TPMSVM, Pin-TSVM, rhingeSVM, RoBoSS-SVM and
aRSGTSVM under di ﬀerent sample sizes.
and the label noise ratio to {0%, 10%, 20%, 30%, 40%}. The experimental results are
presented in Figure 4.
As shown in Figure 4, under di ﬀerent feature dimensions ( p = 100, 200, 300)
and varying label noise ratios (0% to 40%), the proposed aRSGTSVM consistently
achieves higher prediction accuracy than the ablation method SGTSVM, which re-
moves the asymmetric robust loss. As the noise ratio increases from 0% to 40%, the
prediction accuracy of both methods decreases. However, aRSGTSVM exhibits a much
smaller decline, demonstrating superior robustness to label noise. Moreover, as the fea-
ture dimension increases from 100 to 300, aRSGTSVM maintains stable performance,
whereas SGTSVM shows a more pronounced drop in accuracy. These results validate
the eﬀectiveness and robustness of the proposed asymmetric RoBoSS loss function in
scenarios with label noise and high-dimensional features.
Example 5. In this example, we investigate the CPU time cost of our proposed
algorithm (Algorithm 1) with varying numbers of samples and features, respectively.
Based on the setting of Example 1, we ﬁx the feature dimension at p = 2, set the sample
size n ranging from 50 to 10000 with a label noise ratio of 15%, and set all parameters
to 1 except for τ = 0.5. The results are presented in Figure 5. Based on the setting
of Example 3, We further conduct experiments with a ﬁxed sample size n = 100 and
feature dimension p ranging from 50 to 5000, under the same noise ratio and parameter
21

10−2
10−1
100
101
102
103
50 100 200 400 600 800 1000 2000 3000 4000 5000
log10(Feature Number)
Runing Time (s)
Classifier
1−SVM
TPMSVM
Pin−TSVM
rhingeSVM
RoBoSS−SVM
aRSGTSVM
Figure 6: The one-run CPU time cost of 1-SVM, TPMSVM, Pin-TSVM, rhingeSVM, RoBoSS-SVM and
aRSGTSVM under di ﬀerent feature numbers.
settings, as shown in Figure 6.
Figure 5 presents the CPU running time of various classiﬁers under diﬀerent sample
sizes. As the sample size increases from 50 to 10000, the running time of most com-
pared algorithms increases signiﬁcantly. Among them, rhingeSVM and Pin-TSVM
show the fastest growth in time complexity, with their time consumption far exceeding
other models in large-sample scenarios. In contrast, the proposed aRSGTSVM main-
tains an extremely low running time throughout. Even when the sample size reaches
10000, its time consumption remains at a low level, only slightly higher than 1-SVM
and much lower than other compared models, demonstrating excellent scalability to
large sample sizes.
Figure 6 illustrates the single-run CPU time (log scale) of di ﬀerent algorithms as
the feature dimension increases from 50 to 5,000, with a ﬁxed sample size of n = 100.
For the proposed aRSGTSVM, the running time grows slowly when the number of
features is below 200, but increases sharply thereafter, becoming the highest among
all compared methods at 5,000 dimensions. In contrast, Pin-TSVM and TPMSVM
maintain consistently low running times, while 1-SVM and RoBoSS-SVM exhibit an
approximately linear increase with a much lower growth rate than aRSGTSVM. In
summary, aRSGTSVM is sensitive to feature dimensionality, incurring high computa-
tional costs in high-dimensional scenarios, though its running time remains acceptable
22

−0.5
0.0
0.5
1.0
1.5
−10 −5 0 5 10
x
y
Actual
aRSGTSVR
Elastic Net
LASSO
Res−TSVR
SVR
TSVR
(a) No noise
−0.5
0.0
0.5
1.0
1.5
−10 −5 0 5 10
x
y
Actual
aRSGTSVR
Elastic Net
LASSO
Res−TSVR
SVR
TSVR (b) Uniform noise
−0.5
0.0
0.5
1.0
1.5
−10 −5 0 5 10
x
y
Actual
aRSGTSVR
Elastic Net
LASSO
Res−TSVR
SVR
TSVR (c) Gaussian noise
Figure 7: Predictions of SVR, TSVR, Res-TSVR and aRSGTSVR on Sinc function with di ﬀerent noises.
in low-to-medium dimensions.
4.2. Artiﬁcial datasets for regression
Example 1. In this example, we designed a two-dimensional case to demonstrate
that aRSGTSVR is robust under di ﬀerent types of noise, namely uniform noise and
Gaussian noise. We generate 160 samples as follows:
y = sinc(xi) = sin xi xi + ei, xi ∼ U[−3π, 3π]. (26)
Noise is added based on ( 26), which is deﬁned as follows:
Type A: ei ∼ U[−0.4, 0.4], Type B: ei ∼ N(0, 0.22).
We plotted the ﬁtting curve of each model in Figure 7. Since it is not intuitively
obvious which model ﬁts the true curve better, we present the corresponding root mean
square error and standard deviation obtained with the nonlinear kernel setting in Table
3. The results consistently show that the proposed aRSGTSVR achieves the best over-
all performance in terms of RMSE across di ﬀerent noise conditions, including noise-
less, uniform noise, and Gaussian noise scenarios, while maintaining a relatively low
standard deviation. Compared with competing methods such as SVR, LASSO, Elastic
Net, TSVR, and Res-TSVR, aRSGTSVR exhibits more stable and superior regression
performance, which conﬁrms that our method is more robust than other comparative
models under di ﬀerent types of noise when handling nonlinear regression tasks.
23

Table 3: The RMSE and standard deviation (sd) with nonlinear kernel. The bold is the best one.
SVR LASSO Elastic Net TSVR Res-TSVR aRSGTSVR
No noise 0.080 ± 0.013 0.074 ± 0.012 0.075 ± 0.011 0.075 ± 0.030 0.126 ± 0.115 0.071 ± 0.010
Uniform noise 0.128 ± 0.026 0.129 ± 0.014 0.130 ± 0.015 0.129 ± 0.021 0.128 ± 0.022 0.118 ± 0.017
Gaussian noise 0.267 ± 0.059 0.270 ± 0.062 0.265 ± 0.060 0.265 ± 0.055 0.264 ± 0.057 0.260 ± 0.073
Table 4: The RMSE and standard deviation (sd) in di ﬀerent (n, p). The bold is the best one.
(a) 0% label noise
SVR LASSO Elastic Net TSVR Res-TSVR aRSGTSVR
n = 50, p = 30 1.570 ± 1.342 1.968 ± 1.988 1.819 ± 1.838 1.949 ± 1.254 1.861 ± 0.892 1.438 ± 0.675
n = 50, p = 50 1.712 ± 1.902 2.331 ± 2.354 2.331 ± 2.354 2.105 ± 1.998 1.976 ± 0.907 1.481 ± 1.041
n = 50, p = 100 1.811 ± 1.900 2.331 ± 2.354 2.331 ± 2.354 2.140 ± 0.884 2.041 ± 2.532 1.501 ± 1.135
(b) 5% label noise
n = 50, p = 30 1.574 ± 1.341 1.958 ± 1.977 1.958 ± 1.977 1.942 ± 1.469 1.862 ± 0.770 1.406 ± 1.101
n = 50, p = 50 1.802 ± 1.607 2.325 ± 2.349 2.325 ± 2.349 2.097 ± 1.618 1.904 ± 1.142 1.461 ± 1.543
n = 50, p = 100 1.773 ± 1.478 2.325 ± 2.349 2.325 ± 2.349 2.157 ± 2.204 1.986 ± 1.350 1.480 ± 1.438
(c) 10% label noise
n = 50, p = 30 1.632 ± 0.574 1.990 ± 2.010 1.990 ± 2.010 1.978 ± 1.155 1.892 ± 0.922 1.444 ± 0.717
n = 50, p = 50 1.835 ± 0.774 2.334 ± 2.358 2.334 ± 2.358 2.178 ± 2.055 2.091 ± 0.784 1.487 ± 1.290
n = 50, p = 100 1.878 ± 1.115 2.334 ± 2.358 2.334 ± 2.358 2.165 ± 1.645 2.120 ± 1.348 1.483 ± 1.279
(d) 20% label noise
n = 50, p = 30 1.590 ± 0.477 1.962 ± 1.982 1.825 ± 1.843 1.946 ± 1.596 1.709 ± 1.477 1.435 ± 0.994
n = 50, p = 50 1.815 ± 1.876 2.336 ± 2.360 2.336 ± 2.360 2.150 ± 1.257 1.941 ± 1.999 1.485 ± 1.315
n = 50, p = 100 1.832 ± 2.459 2.336 ± 2.360 2.336 ± 2.360 2.162 ± 1.702 1.924 ± 1.491 1.535 ± 1.984
(e) 35% label noise
n = 50, p = 30 1.590 ± 0.360 1.972 ± 1.992 1.823 ± 1.841 1.896 ± 1.044 1.858 ± 1.041 1.400 ± 0.959
n = 50, p = 50 1.767 ± 1.566 2.352 ± 2.376 2.352 ± 2.376 2.169 ± 1.798 1.939 ± 1.758 1.528 ± 1.302
n = 50, p = 100 1.787 ± 1.583 2.352 ± 2.376 2.352 ± 2.376 2.157 ± 2.144 2.002 ± 1.248 1.519 ± 1.682
Example 2. To illustrate that aRSGTSVR exhibits excellent variable selection ca-
pability under di ﬀerent noise ratios for high-dimensional data, in this example, the
samples are generated from the following multivariate Gaussian distribution: xi, i ∈
{1, 2, . . . ,n} ∼ N(u, Σ), where u = (0.1, 0.2, 0.3, 0.4, 0.5, 0, . . . ,0)T ∈ Rn and Σ = (σi j)
is deﬁned with non-zero elements: σii = 1, for i = 1, 2, . . . ,n and σi j = −0.2, for 1 ≤
i , j ≤ 5.
The response variable y for each sample is constructed via the function:
y = sin(3x1) + x2 2 + exp(−|x3|) + log(|x4| + 1) + x1x5. (27)
Table 4 presents the RMSE and standard deviation results of all compared meth-
ods across di ﬀerent combinations of sample size n, feature dimension p, and label
noise levels ranging from 0% to 35%, while Figure 8 further visualizes the perfor-
24

1.00
1.25
1.50
1.75
2.00
0.0 0.1 0.2 0.3
SVR Lasso ElasticNet
TSVR Res−TSVR aRSGTSVR
(a) n = 50, p = 30
1.0
1.5
2.0
2.5
0.0 0.1 0.2 0.3
SVR Lasso ElasticNet
TSVR Res−TSVR aRSGTSVR (b) n = 50, p = 50
1.0
1.5
2.0
2.5
0.0 0.1 0.2 0.3
SVR Lasso ElasticNet
TSVR Res−TSVR aRSGTSVR (c) n = 50, p = 100
Figure 8: Predictions of SVR, LASSO, Elastic Net, TSVR, Res-TSVR and aRSGTSVR on Sinc function
with diﬀerent types of noises.
mance trends of each method under varying noise conditions for di ﬀerent dimensional
settings. As shown in both the table and ﬁgure, the proposed aRSGTSVR consis-
tently achieves the lowest RMSE values across all experimental scenarios, including
low-dimensional, boundary high-dimensional, and classical high-dimensional cases,
while maintaining stable performance with relatively small standard deviations. Com-
pared with baseline models such as SVR, LASSO, Elastic Net, TSVR, and Res-TSVR,
aRSGTSVR exhibits superior regression accuracy and stronger robustness against in-
creasing label noise, conﬁrming its combined advantages in prediction accuracy and
stability for both low- and high-dimensional nonlinear regression tasks.
4.3. UCI datasets for classiﬁcation
4.3.1. Experimental results
To assess the generalization performance of the models, we conducted tests on a
lot of UCI datasets (see Table 5). Furthermore, to examine the robustness of the SVMs
to outliers, we introduced artiﬁcial noise by randomly selecting 15% and 35% of the
training samples and swapping their labels.
Table 6 presents the performance comparison of various SVM models using the ini-
tial data. In terms of average prediction accuracy, our proposed aRSGTSVM achieves
the most optimal results, followed by RoBoSS-SVM, while rhingeSVM also demon-
strates strong competitiveness. Although 1-SVM performs well only on certain datasets,
all models can e ﬀectively predict data labels. TPMSVM and Pin-TSVM show the
25

Table 5: The information of seleced UCI datasets.
Dataset #Samples #Features
acoustic 400 50
amphibians 189 21
autism 702 15
bads 1372 4
dccc 30000 23
diabetes 520 16
gait 47 321
garments 1197 7
heartfailure 299 12
lsvt 126 310
messidor 1151 19
raisin 900 7
shillbidding 6321 9
tripadvisor 980 9
vertebral 310 6
waveform 5000 40
wp 4746 15
relatively poorest performance. Overall, the vast majority of models are capable of
eﬀectively classifying the data.
As shown in Table 7, the aRSGTSVM model still achieves the optimal perfor-
mance. In comparison, the competitive advantages of rhingeSVM, RoBoSS-SVM, and
1-SVM models gradually diminish, while TPMSVM shows an improving trend. Pin-
TSVM consistently demonstrates relatively poor performance. From Table 8, it can be
observed that aRSGTSVM performs best on all UCI datasets, and as the noise ratio
increases, the superiority of aRSGTSVM becomes more pronounced, indicating that
our model exhibits strong robustness to label noise.
4.3.2. Comparisons by statistical test
To further validate the e ﬀectiveness of our proposed aRSGTSVM model, we com-
pare it with other SVM models on multiple datasets using the Friedman test and the
corresponding Nemenyi post-hoc test[ 40]. The null hypothesis of the Friedman test
is that there is no signiﬁcant di ﬀerence among all models. If the null hypothesis is
rejected, the Nemenyi test is conducted. The Friedman statistic is deﬁned as:
FF = (Dn − 1)χ2 F
Dn(Ck − 1) − χ2 F ,
26

Table 6: The results of UCI datasets with 0% label noise. The bold is the best one.
1-SVM TPMSVM Pin-TSVM rhingeSVM RoBoSS-SVM aRSGTSVM
acoustic 0.755 ±0.084 0.825 ±0.062 0.767 ±0.059 0.868 ±0.044 0.853 ±0.046 0.8730.8730.873±0.0220.0220.022
amphibians 0.704 ±0.080 0.746 ±0.090 0.714 ±0.115 0.793 ±0.062 0.809 ±0.075 0.814 ±0.0830.814±0.0830.814±0.083
autism 1.000±0.0001.000±0.0001.000±0.000 0.967 ±0.030 0.970 ±0.038 1.000 ±0.0001.000±0.0001.000±0.000 1.000 ±0.0001.000±0.0001.000±0.000 1.000 ±0.0001.000±0.0001.000±0.000
bads 0.981±0.017 0.985 ±0.012 0.961 ±0.026 0.987 ±0.009 0.984 ±0.013 0.988 ±0.0130.988±0.0130.988±0.013
dccc 0.753±0.064 0.821 ±0.053 0.812 ±0.049 0.803 ±0.054 0.832 ±0.059 0.836 ±0.0310.836±0.0310.836±0.031
diabetes 0.917 ±0.036 0.904 ±0.037 0.892 ±0.030 0.937 ±0.041 0.940 ±0.0390.940±0.0390.940±0.039 0.910 ±0.026
gait 0.980±0.063 0.915 ±0.145 0.915 ±0.145 0.980 ±0.063 0.940 ±0.135 1.000 ±0.0001.000±0.0001.000±0.000
garments 0.999 ±0.003 0.998 ±0.004 0.993 ±0.008 1.000 ±0.0001.000±0.0001.000±0.000 1.000 ±0.0001.000±0.0001.000±0.000 0.999 ±0.003
heartfailure 0.762 ±0.071 0.836 ±0.058 0.843 ±0.052 0.833 ±0.079 0.836 ±0.060 0.859 ±0.0630.859±0.0630.859±0.063
lsvt 0.985±0.0320.985±0.0320.985±0.032 0.760 ±0.123 0.824 ±0.094 0.953 ±0.075 0.904 ±0.123 0.912 ±0.090
messidor 0.600 ±0.051 0.699 ±0.042 0.601 ±0.071 0.751 ±0.0360.751±0.0360.751±0.036 0.673 ±0.060 0.751 ±0.0340.751±0.0340.751±0.034
raisin 0.788±0.034 0.865 ±0.028 0.862 ±0.031 0.871 ±0.032 0.875 ±0.0270.875±0.0270.875±0.027 0.869 ±0.027
shillbidding 0.982 ±0.012 0.984 ±0.008 0.979 ±0.010 0.984 ±0.011 0.982 ±0.006 0.988 ±0.0090.988±0.0090.988±0.009
tripadvisor 0.644 ±0.027 0.747 ±0.020 0.753 ±0.019 0.733 ±0.026 0.759 ±0.033 0.761 ±0.0340.761±0.0340.761±0.034
vertebral 0.813 ±0.052 0.803 ±0.051 0.806 ±0.059 0.855 ±0.061 0.858 ±0.0460.858±0.0460.858±0.046 0.839 ±0.061
waveform 0.832 ±0.047 0.866 ±0.034 0.836 ±0.028 0.877 ±0.021 0.881 ±0.031 0.887 ±0.0250.887±0.0250.887±0.025
wp 0.809±0.044 0.853 ±0.030 0.853 ±0.028 0.856 ±0.031 0.857 ±0.029 0.861 ±0.0320.861±0.0320.861±0.032
Table 7: The results of UCI datasets with 15% label noise. The bold is the best one.
1-SVM TPMSVM Pin-TSVM rhingeSVM RoBoSS-SVM aRSGTSVM
acoustic 0.670 ±0.079 0.760 ±0.079 0.755 ±0.077 0.767 ±0.060 0.780 ±0.088 0.8500.8500.850±0.0570.0570.057
amphibians 0.688 ±0.075 0.730 ±0.067 0.730 ±0.114 0.778 ±0.077 0.740 ±0.078 0.784 ±0.1060.784±0.1060.784±0.106
autism 0.829±0.127 0.959 ±0.025 0.953 ±0.025 0.949 ±0.024 0.963 ±0.026 0.992 ±0.0150.992±0.0150.992±0.015
bads 0.817±0.032 0.970 ±0.027 0.955 ±0.025 0.973 ±0.024 0.977 ±0.016 0.978 ±0.0200.978±0.0200.978±0.020
dccc 0.628±0.063 0.820 ±0.0410.820±0.0410.820±0.041 0.807 ±0.040 0.814 ±0.039 0.817 ±0.041 0.810 ±0.041
diabetes 0.691 ±0.084 0.908 ±0.031 0.902 ±0.044 0.869 ±0.039 0.917 ±0.0160.917±0.0160.917±0.016 0.904 ±0.035
gait 0.850±0.141 0.875 ±0.144 0.855 ±0.138 0.875 ±0.144 0.855 ±0.138 0.960 ±0.0840.960±0.0840.960±0.084
garments 0.818 ±0.074 0.994 ±0.008 0.992 ±0.009 0.980 ±0.011 0.999 ±0.0030.999±0.0030.999±0.003 0.998 ±0.004
heartfailure 0.659 ±0.076 0.826 ±0.075 0.826 ±0.075 0.823 ±0.059 0.830 ±0.069 0.856 ±0.0740.856±0.0740.856±0.074
lsvt 0.849±0.060 0.754 ±0.136 0.693 ±0.120 0.848 ±0.063 0.819 ±0.120 0.921 ±0.0740.921±0.0740.921±0.074
messidor 0.561 ±0.042 0.698 ±0.045 0.642 ±0.035 0.699 ±0.040 0.646 ±0.053 0.731 ±0.0510.731±0.0510.731±0.051
raisin 0.735±0.183 0.859 ±0.035 0.854 ±0.032 0.859 ±0.041 0.863 ±0.035 0.871 ±0.0330.871±0.0330.871±0.033
shillbidding 0.903 ±0.058 0.973 ±0.012 0.968 ±0.022 0.978 ±0.0110.978±0.0110.978±0.011 0.978 ±0.0100.978±0.0100.978±0.010 0.978 ±0.0130.978±0.0130.978±0.013
tripadvisor 0.601 ±0.035 0.752 ±0.0350.752±0.0350.752±0.035 0.747 ±0.035 0.731 ±0.041 0.750 ±0.042 0.739 ±0.044
vertebral 0.687 ±0.087 0.806 ±0.086 0.742 ±0.083 0.826 ±0.072 0.858 ±0.0590.858±0.0590.858±0.059 0.858 ±0.0550.858±0.0550.858±0.055
waveform 0.707 ±0.050 0.815 ±0.028 0.828 ±0.032 0.843 ±0.030 0.831 ±0.034 0.860 ±0.0320.860±0.0320.860±0.032
wp 0.669±0.043 0.827 ±0.031 0.818 ±0.026 0.824 ±0.030 0.827 ±0.026 0.831 ±0.0330.831±0.0330.831±0.033
where Dn is the number of datasets, and Ck is the number of models,
χ2 F = 12Dn Ck(Ck + 1)
0BBBBBB@ CkX
i=1
R2 i − Ck(Ck + 1)2 4 1CCCCCCA ,
where Ri is the average rank of the i-th model (calculated from the results in Table 6-8).
Given Dn = 17 and Ck = 6, then for a noise ratio of 0%, FF = 14.507. For 15%,
FF = 27.788. For 35%, FF = 25.107. In our experiment, FF follows an F(5, 80)
distribution. At a signiﬁcance level of 0.05, the critical value is F0.05(5, 80) = 3.329.
27

Table 8: The results of UCI datasets with 35% label noise. The bold is the best one.
1-SVM TPMSVM Pin-TSVM rhingeSVM RoBoSS-SVM aRSGTSVM
acoustic 0.585 ±0.110 0.605 ±0.112 0.595 ±0.112 0.647 ±0.088 0.642 ±0.093 0.853 ±0.0530.853±0.0530.853±0.053
amphibians 0.529 ±0.153 0.546 ±0.152 0.593 ±0.098 0.609 ±0.128 0.556 ±0.113 0.793 ±0.0690.793±0.0690.793±0.069
autism 0.619±0.294 0.882 ±0.050 0.929 ±0.033 0.895 ±0.057 0.900 ±0.056 0.993 ±0.0220.993±0.0220.993±0.022
bads 0.620±0.054 0.972 ±0.014 0.918 ±0.038 0.965 ±0.018 0.969 ±0.014 0.981 ±0.0110.981±0.0110.981±0.011
dccc 0.570±0.113 0.778 ±0.056 0.549 ±0.110 0.787 ±0.047 0.779 ±0.043 0.799 ±0.0500.799±0.0500.799±0.050
diabetes 0.610 ±0.171 0.810 ±0.066 0.835 ±0.052 0.821 ±0.048 0.835 ±0.047 0.902 ±0.0320.902±0.0320.902±0.032
gait 0.755±0.227 0.640 ±0.251 0.685 ±0.221 0.680 ±0.258 0.620 ±0.253 0.980 ±0.0630.980±0.0630.980±0.063
garments 0.705 ±0.348 0.973 ±0.015 0.985 ±0.013 0.969 ±0.023 0.989 ±0.011 0.999 ±0.0030.999±0.0030.999±0.003
heartfailure 0.519 ±0.156 0.736 ±0.139 0.690 ±0.137 0.719 ±0.110 0.733 ±0.108 0.853 ±0.0390.853±0.0390.853±0.039
lsvt 0.666±0.158 0.608 ±0.191 0.586 ±0.193 0.668 ±0.164 0.666 ±0.148 0.912 ±0.0810.912±0.0810.912±0.081
messidor 0.554 ±0.045 0.617 ±0.052 0.557 ±0.063 0.590 ±0.071 0.602 ±0.065 0.717 ±0.0350.717±0.0350.717±0.035
raisin 0.615±0.295 0.848 ±0.038 0.846 ±0.039 0.836 ±0.035 0.851 ±0.040 0.868 ±0.0270.868±0.0270.868±0.027
shillbidding 0.632 ±0.073 0.973 ±0.018 0.975 ±0.016 0.970 ±0.016 0.971 ±0.017 0.981 ±0.0140.981±0.0140.981±0.014
tripadvisor 0.535 ±0.046 0.668 ±0.084 0.602 ±0.179 0.728 ±0.058 0.714 ±0.071 0.742 ±0.0530.742±0.0530.742±0.053
vertebral 0.635 ±0.171 0.716 ±0.087 0.603 ±0.143 0.707 ±0.062 0.687 ±0.063 0.855 ±0.0600.855±0.0600.855±0.060
waveform 0.612 ±0.065 0.802 ±0.051 0.804 ±0.047 0.779 ±0.051 0.793 ±0.060 0.877 ±0.0210.877±0.0210.877±0.021
wp 0.566±0.088 0.798 ±0.033 0.786 ±0.061 0.804 ±0.051 0.816 ±0.034 0.832 ±0.0340.832±0.0340.832±0.034
1 2 3 4 5 6
CD = 1.829
aRSGTSVM
RoBoSS−SVM
rhingeSVM TPMSVM
1−SVM
Pin−TSVM
(a) 0% label noise
1 2 3 4 5 6
CD = 1.829
aRSGTSVM
RoBoSS−SVM
TPMSVM rhingeSVM
Pin−TSVM
1−SVM
(b) 15% label noise
1 2 3 4 5 6
CD = 1.829
aRSGTSVM
RoBoSS−SVM
rhingeSVM TPMSVM
Pin−TSVM
1−SVM
(c) 35% label noise
Figure 9: The average ranks of six classiﬁers on the UCI datasets with di ﬀerent label noise.
Since FF > 3.329, the null hypothesis of the Friedman test should be rejected, and the
Nemenyi test is conducted next.
28

If there is a signiﬁcant di ﬀerence between two models, the di ﬀerence in their aver-
age ranks must be at least the critical di ﬀerence, deﬁned as:
CD = q0.05
r
Ck(Ck + 1)
6Dn
.
Given that Dn = 17, Ck = 6, and q0.05(6) = 2.85, we obtain CD = 1.777.
Figure 9 visualizes the average ranking comparison of six Support V ector Regres-
sion (SVR) models. According to the Critical Di ﬀerence (CD) diagram analysis cri-
terion, when the distance between two models on the horizontal axis exceeds the CD
value (red solid line), it indicates a statistically signiﬁcant di ﬀerence between them.
In the subﬁgure 9(a), aRSGTSVM, rhingeSVM, and RoBoSS-SVM are grouped to-
gether, while Pin-TSVM, 1-SVM, and TPMSVM form another group, with signiﬁcant
performance diﬀerences between these two groups. In the subﬁgure 9(b), the grouping
changes to aRSGTSVM, RoBoSS-SVM, and TPMSVM as one group, and 1-SVM,
Pin-TSVM, and rhingeSVM as the other group, maintaining signiﬁcant inter-group
diﬀerences. In the subﬁgure 9(c), aRSGTSVM stands alone as one group, while the
remaining models (RoBoSS-SVM, rhingeSVM, 1-SVM, Pin-TSVM, and TPMSVM)
form another group, with equally signiﬁcant performance di ﬀerences between groups.
It can be observed that aRSGTSVM signiﬁcantly outperforms other comparative mod-
els, and its advantage becomes more pronounced as the noise ratio increases, fully
demonstrating the model’s performance stability across di ﬀerent label noise scenarios.
4.4. Index tracking for regression
In this section, to assess the models out-of-sample performance, we employ six
index tracking datasets spanning from January 1, 2025, to July 1, 2025, for experi-
mentation. The dataset is partitioned such that the ﬁrst 70% (rounded down if not an
integer) is used as the training set, with the remainder serving as the test set. During
training, the Mean Absolute Error (MAE) is utilized to select the optimal parameters,
while the model’s performance is evaluated based on the annual tracking error. The
annual tracking error is deﬁned as:
29

Table 9: TrackingErrorYear for diﬀerent datasets. The bold is the best one.
Index SVR LASSO Elastic Net TSVR Res-TSVR aRSGTSVR
bz50 0.138 0.126 0.133 0.120 0.135 0.117
cy200 0.059 0.134 0.078 0.045 0.045 0.040
hs300 0.277 0.277 0.380 0.122 0.138 0.117
xf100 0.638 0.328 0.250 0.368 0.925 0.226
ys50 0.191 0.065 0.068 0.128 0.124 0.057
zz500 0.297 0.271 0.185 0.162 0.109 0.105
1000
1100
1200
1300
1400
1500
0 25 50 75 100
Date(2025/01/01−2025/07/01)
Stock Index
Real
Fitted
Predicted
(a) bz50
3000
3500
4000
4500
0 25 50 75 100
Date(2025/01/01−2025/07/01)
Stock Index
Real
Fitted
Predicted (b) cy200
3750
4000
4250
4500
4750
0 30 60 90 120
Date(2025/01/01−2025/07/01)
Stock Index
Real
Fitted
Predicted (c) hs300
8000
9000
10000
0 30 60 90 120
Date(2025/01/01−2025/07/01)
Stock Index
Real
Fitted
Predicted
(d) xf100
6900
7200
7500
7800
8100
0 25 50 75 100
Date(2025/01/01−2025/07/01)
Stock Index
Real
Fitted
Predicted (e) ys50
5500
6000
6500
7000
7500
0 25 50 75 100
Date(2025/01/01−2025/07/01)
Stock Index
Real
Fitted
Predicted (f) zz500
Figure 10: Index tracking plots for Stock Indices. The red solid lines are the true values, the blue solid lines
are the ﬁtted values on the training set, and the blue dashed lines are the predicted values on the test set.
TrackingErroryear =
√
252 ·
sPT
t=1 (errt − err)2
T − 1 ,
where errt = yt − ˆyt for t = 1, 2, · · · , T , yt denotes the return of an index at time t, ˆyt is
the estimated value of yt, and err represents the mean of errt over t = 1, 2, · · · , T .
To mitigate spurious regression and enable the model to focus on replicating rela-
tive price movements, converting raw price data to returns is crucial for index tracking.
For a raw price series Pt, the return at time t is calculated as:
rt = Pt Pt−1 − 1, t = 1, 2, · · · , T.
Similarly, the index value yt at time t is converted to its corresponding return, which
30

we continue to denote as yt for consistency.
The experimental results are presented in Table 9. As evidenced by the annual
tracking errors, the proposed aRSGTSVR achieves the best performance across all six
index tracking datasets, demonstrating strong generalization capability of the model.
As illustrated in Figure 10, the ﬁtted and predicted values of the aRSGTSVR model
closely align with the true values. This visually conﬁrms the model’s superior ﬁtting
performance and robust generalization ability.
5. Conclusion
This paper designs a novel asymmetric loss function LaR based on the RoBoSS
loss, which is integrated with ENNHSVM to establish aRSGTSVM for classiﬁcation
and aRSGTSVR for regression tasks. To tackle the challenging optimization issue
arising from the combination of a nonconvex loss LaR and a sparse penalty l1 in the
objective function, the iPiano algorithm is adopted to achieve e ﬃcient and stable op-
timization. Experimental results in synthetic datasets demonstrate that aRSGTSVM
maintains strong robustness against label noise, delivers stable performance under re-
sampling, achieves satisfactory results in high-dimensional scenarios, and presents
competitive computational eﬃciency. Meanwhile, aRSGTSVR also exhibits prominent
noise resistance and e ﬀective high-dimensional variable selection capability. In real-
world datasets, both proposed models acquire favorable generalization performance.
The core contribution of this study lies in that the designed asymmetric loss naturally
balances model robustness and sparsity, which provides a reliable and superior alter-
native to conventional symmetric loss functions for practical scenarios su ﬀering from
label noise, high-dimensional features, and resampling instability.
It is noteworthy that although this study employs a cross-validation strategy for
model parameter optimization, this method can only detect the presence or absence of
overﬁtting rather than alleviate it. Alleviating overﬁtting requires strategies such as reg-
ularization. Furthermore, cross-validation necessitates repeated data partitioning and
model retraining, resulting in substantial computational overhead. This issue becomes
particularly pronounced in high-dimensional data or complex model scenarios. Given
31

that information criteria (e.g., AIC, BIC) can construct objective functions by integrat-
ing model goodness of ﬁt and complexity without requiring repeated data partitioning
and retraining, they signiﬁcantly enhance parameter tuning e ﬃciency while balancing
model generalization performance. Therefore, exploring the optimal information crite-
rion tailored to the characteristics of our model represents a highly valuable direction
for future research. Additionally, distributed or parallel algorithms can be employed to
further improve the computational e ﬃciency of the model.
Acknowledgments
This research is supported by the National Natural Science Foundation of China
(Grant No. 12401664), the Natural Science Foundation of Chongqing Municipality
(Grant No. CSTB2024NSCQ-MSX0855), and the Science and Technology Research
Program of Chongqing Municipal Education Commission (Grant No. KJQN202400514).
References
[1] Jayadeva, R. Khemchandani, S. Chandra, Twin support vector machines for pat-
tern classiﬁcation, IEEE Transactions on Pattern Analysis and Machine Intelli-
gence 29 (2007) 905–910.
[2] X. Chen, J. Y ang, Q. Y e, J. Liang, Recursive projection twin support vector
machine via within-class variance minimization, Pattern Recognition 44 (2011)
2643–2655.
[3] K. Qi, H. Y ang, Elastic net nonparallel hyperplane support vector machine and
its geometrical rationality, IEEE Transactions on Neural Networks & Learning
Systems 33 (2022) 7199–7209.
[4] Z. Liang, S. Ding, Fuzzy twin support vector machines with distribution inputs,
IEEE Transactions on Fuzzy Systems 32 (2024) 240–254.
[5] A. Quadir, M. Sajid, M. Tanveer, Granular ball twin support vector machine,
IEEE Transactions on Neural Networks & Learning Systems 36 (2025) 12444–
12453.
32

[6] Y . Shao, C. Zhang, X. Wang, N. Deng, Improvements on twin support vector
machines, IEEE Transactions on Neural Networks 22 (2011) 962–968.
[7] Y . Wu, Y . Liu, Robust truncated hinge loss support vector machines, Journal of
the American Statistical Association 102 (2007) 974–983.
[8] H. Wang, Z. Zhu, Y . Shao, Fast support vector machine with low-computational
complexity for large-scale classiﬁcation, IEEE Transactions on Systems, Man, &
Cybernetics: Systems 54 (2024) 4151–4163.
[9] X. Huang, L. Shi, J. Suykens, Support vector machine classiﬁer with pinball
loss, IEEE Transactions on Pattern Analysis & Machine Intelligence 36 (2014)
984–997.
[10] J. Zhu, S. Rosset, T. Hastie, R. Tibshirani, 1-norm support vector machines, in:
Advances in Neural Information Processing Systems, 2004, pp. 1–8.
[11] L. Wang, J. Zhu, H. Zou, The doubly regularized support vector machine, Statis-
tica Sinica (2006) 589–615.
[12] N. Krause, Y . Singer, Leveraging the margin more carefully, in: Proceedings of
the Twenty-First International Conference on Machine Learning, 2004, p. 63.
[13] D. Liu, Y . Shi, Y . Tian, Ramp loss nonparallel support vector machine for pattern
classiﬁcation, Knowledge-Based Systems 85 (2015) 224–233.
[14] C. Wang, Q. Y e, P . Luo, N. Y e, L. Fu, Robust capped l1-norm twin support vector
machine, Neural Networks 114 (2019) 47–59.
[15] W. Liu, P . Pokharel, J. Principe, Correntropy: Properties and applications in non-
gaussian signal processing, IEEE Transactions on Signal Processing 55 (2007)
5286–5298.
[16] A. Singh, R. Pokharel, J. Principe, The c-loss function for pattern classiﬁcation,
Pattern Recognition 47 (2014) 441–453.
33

[17] G. Xu, Z. Cao, B. Hu, J. Principe, Robust support vector machines based on the
rescaled hinge loss function, Pattern Recognition 63 (2017) 139–148.
[18] G. Xu, B. Hu, J. Principe, Robust c-loss kernel classiﬁers, IEEE Transactions on
Neural Networks & Learning Systems 29 (2018) 510–529.
[19] J. Ma, L. Y ang, Q. Sun, Adaptive robust learning framework for twin support
vector machine classiﬁcation, Knowledge-Based Systems 211 (2021) 106536.
[20] M. Akhtar, M. Tanveer, M. Arshad, Roboss: A robust, bounded, sparse, and
smooth loss function for supervised learning, IEEE Transactions on Pattern Anal-
ysis & Machine Intelligence 47 (2025) 149–160.
[21] X. Huang, L. Shi, J. Suykens, Asymmetric least squares support vector machine
classiﬁers, Computational Statistics & Data Analysis 70 (2014) 395–405.
[22] X. Shen, L. Niu, Z. Qi, Y . Tian, Support vector machine classiﬁer with truncated
pinball loss, Pattern Recognition 68 (2017) 199–210.
[23] L. Y ang, H. Dong, Robust support vector machine with generalized quantile loss
for classiﬁcation and regression, Applied Soft Computing 81 (2019) 105483.
[24] M. He, F. He, L. Shi, X. Huang, J. Suykens, Learning with asymmetric kernels:
Least squares and feature interpretation, IEEE Transactions on Pattern Analysis
& Machine Intelligence 45 (2023) 10044–10054.
[25] K. Ikeda, N. Murata, Geometrical properties of nu support vector machines with
diﬀerent norms, Neural Computation 17 (2005) 2508–2529.
[26] H. Zou, M. Y uan, The F∞-norm support vector machine, Statistica Sinica (2008)
379–398.
[27] S. Gao, Q. Y e, N. Y e, 1-norm least squares twin support vector machines, Neu-
rocomputing 74 (2011) 3590–3597.
[28] H. Moosaei, M. Hladík, Sparse solution of least-squares twin multi-class sup-
port vector machine using ℓ0 and ℓp-norm for classiﬁcation and feature selection,
Neural Networks 166 (2023) 471–486.
34

[29] X. Xie, F. Sun, J. Qian, L. Guo, R. Zhang, X. Y e, Z. Wang, Laplacianlp norm least
squares twin support vector machine, Pattern Recognition 136 (2023) 109192.
[30] Y .-H. Shao, W.-J. Chen, N.-Y . Deng, Nonparallel hyperplane support vector ma-
chine for binary classiﬁcation problems, Information Sciences 263 (2014) 22–35.
[31] Y . Xu, Z. Y ang, X. Pan, A novel twin support-vector machine with pinball loss,
IEEE Transactions on Neural Networks & Learning Systems 28 (2017) 359–370.
[32] F. R. Hampel, Contributions to the theory of robust estimation, University of Cal-
ifornia, Berkeley, 1968.
[33] M. Akhtar, M. Tanveer, M. Arshad, Robots: A robust bounded twin svm based
on roboss loss function, Pattern Recognition (2026) 113653.
[34] R. Khemchandani, K. Goyal, S. Chandra, Twsvr: regression via twin support
vector machine, Neural Networks 74 (2016) 14–21.
[35] P . Ochs, Y . Chen, T. Brox, T. Pock, ipiano: Inertial proximal algorithm for non-
convex optimization, SIAM Journal on Imaging Sciences 7 (2014) 1388–1419.
[36] P . S. Bradley, O. L. Mangasarian, Feature selection via concave minimization and
support vector machines., in: ICML, volume 98, 1998, pp. 82–90.
[37] X. Peng, Tpmsvm: a novel twin parametric-margin support vector machine for
pattern recognition, Pattern recognition 44 (2011) 2678–2692.
[38] X. Peng, Tsvr: an e ﬃcient twin support vector machine for regression, Neural
Networks 23 (2010) 365–372.
[39] M. Singla, D. Ghosh, K. Shukla, W. Pedrycz, Robust twin support vector regres-
sion based on rescaled hinge loss, Pattern Recognition 105 (2020) 107395.
[40] J. Demšar, Statistical comparisons of classiﬁers over multiple data sets, Journal
of Machine learning research 7 (2006) 1–30.
35
