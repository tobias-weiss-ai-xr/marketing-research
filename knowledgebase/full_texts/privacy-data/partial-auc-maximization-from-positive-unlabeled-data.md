---
title: Partial AUC Maximization from Positive-unlabeled Data
url: https://arxiv.org/abs/2610.00284
category: privacy-data
subcategory: empirical
date: 2026-09
venue: arXiv (Cornell University)
authors:
- Atsutoshi Kumagai
- Tomoharu Iwata
- Taishi Nishiyama
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.00284
pages: 26
chars: 75360
fetched_at: '2026-11-08T13:00:49+00:00'
kb_version: 1
---

# Partial AUC Maximization from Positive-unlabeled Data

Preprint
PARTIALAUC MAXIMIZATION FROM
POSITIVE-UNLABELEDDATA
Atsutoshi Kumagai, Tomoharu Iwata, Taishi Nishiyama, Hiroshi Takahashi,
Kazuki Adachi,Yasuhiro Fujiwara
NTT, Inc.
atsutoshi.kumagai@ntt.com
ABSTRACT
The partial area under the receiver operating characteristic curve (pAUC) is an im-
portant performance metric for binary classification that summarizes true positive
rates within a specific range of false positive rates (FPRs). Classifiers that achieve
high pAUC need to be obtained in many real-world applications such as cyberse-
curity, medical care, and advertising. Although many methods for maximizing the
pAUC have been proposed, they typically require both labeled positive and nega-
tive data for training. However, in practice, labeled negative data are often difficult
to collect due to privacy concerns or the need for high expertise to annotate them.
In this paper, we propose a method for maximizing the pAUC from positive and
unlabeled (PU) data without negative data. Within an empirical risk minimiza-
tion framework, we show that the pAUC, including its FPR-dependent thresholds,
can be represented using only the positive and marginal densities, and derive an
empirical estimator from PU data. A classifier is then trained by maximizing the
derived smoothed empirical pAUC estimator. We experimentally demonstrate the
effectiveness of the proposed method with ten real-world datasets.
1 INTRODUCTION
The area under the receiver operating characteristic (ROC) curve (AUC) is a widely used evaluation
metric for binary classification, especially in class-imbalanced scenarios where positive data are
much smaller than negative data (Bradley, 1997; Cortes & Mohri, 2003). The ROC curve is obtained
by plotting the true positive rate (TPR) against the false positive rate (FPR) at various threshold
settings. By maximizing the AUC, we can obtain classifiers that achieve high average TPRs over all
FPR values from zero to one (Yang & Ying, 2022).
False Positive Rate False Positive Rate
0 0 1 1
1 1True Positive Rate
True Positive Rate
(a) AUC (b) pAUC
Figure 1: The comparison between the
AUC and pAUC: (a) AUC. (b) pAUC
within FPR range[α, β].
In many real-world applications, we are interested in
achieving high TPRs within a specific range of FPRs.
For example, in cybersecurity, detection systems often
need a low FPR since falsely detecting benign soft-
ware or communications as malicious intensely hin-
ders the work of end users and operators, but they still
require high TPRs to reliably detect truly malicious ac-
tivities (Nishiyama et al., 2024). In medical care, a
low FPR needs to be maintained to avoid unnecessary
biopsies, which are invasive and impose physical and
psychological burdens on patients as well as financial
costs (Baker & Pinsky, 2001; Iwata et al., 2020). In ad-
vertising, a low FPR is also important since irrelevant
advertisements substantially degrade the user experi-
ence. In such applications, a partial AUC (pAUC), which is the partial area under the ROC curve
within a specific FPR range, is a more appropriate metric than the AUC (Yang & Ying, 2022).
Figure 1 illustrates the difference between the AUC and pAUC.
Although many methods for maximizing the pAUC have been proposed (Narasimhan & Agarwal,
2013a; Ueda & Fujino, 2018; Iwata et al., 2020; Yao et al., 2022; Zhu et al., 2022), they require both
1
arXiv:2610.00284v1  [cs.LG]  25 Sep 2026

Preprint
labeled positive and negative (PN) data for training. However, in practice, labeled negative data
are often difficult to collect. For example, in cybersecurity, although some malicious data (positive
data) can be obtained from public blocklists, benign data (negative data) are often unavailable due to
privacy reasons, and identifying benign data within unlabeled data requires a high level of expertise
(Mirsky et al., 2018; Kumagai et al., 2024; 2025). In medical care and advertising, although positive
data can be obtained from biopsy-confirmed cases or clicked ads, data that are not biopsy-confirmed
cases or clicked ads cannot be regarded as negative because they may contain false negatives, such as
early-stage patients incorrectly classified as healthy or advertisements that users are interested in but
happened not to click (Bekker & Davis, 2020). Therefore, such data are better treated as unlabeled
data. In this setting, most existing pAUC maximization methods cannot be applied.
The only exception is the work by Iwata et al. (2020), which proposed a semi-supervised learning
method for maximizing the pAUC and presented an approximation of the pAUC from positive and
unlabeled (PU) data. This method sorts the unlabeled instances by their current classifier scores
and heuristically treats all instances within a specified rank range as negatives, assuming that the
selected instances are indeed negative. However, the resulting objective generally does not coincide
with the pAUC. Moreover, when this heuristic assumption is violated, its performance can degrade.
In this paper, we propose an approach for maximizing the pAUC from PU data by directly reformu-
lating the pAUC without relying on this heuristic assumption. Our approach builds on the empirical
risk minimization (ERM) framework of PU learning, which allows us to rewrite the risk (i.e., the
objective for classifier training) using only the positive and marginal densities (Sugiyama et al.,
2022; Du Plessis et al., 2015). However, unlike standard classification and AUC objectives used in
prior PU learning work (Kiryo et al., 2017; Sakai et al., 2018; Xie & Li, 2018), simply applying this
risk rewriting to the pAUC is insufficient because the pAUC additionally depends on FPR-dependent
score thresholds, which are determined by the unknown negative density. We show that the FPR, and
consequently the FPR-dependent thresholds required for the pAUC, can also be represented using
only the positive and marginal densities, thereby enabling a direct reformulation of the pAUC. Based
on this reformulation, we derive an empirical estimator of the pAUC from PU data. By maximizing
the derived smoothed empirical pAUC estimator, we can train classifiers that achieve high pAUC
even without negative data. The proposed method can use any differentiable classifiers such as lin-
ear classifiers, kernel-based classifiers, and neural network-based classifiers, which is preferable in
practical use.
Our main contributions are summarized as follows: (1) We show that the pAUC, including its FPR-
dependent thresholds, can be reformulated using only the positive and marginal densities, and derive
an empirical estimator of the pAUC from PU data. (2) We propose a method for learning classifiers
that achieve high pAUC by maximizing the derived smoothed empirical pAUC estimator with PU
data. (3) We experimentally demonstrate the effectiveness of the proposed method against existing
PU learning, AUC maximization, and pAUC maximization methods with ten real-world datasets.
2 RELATEDWORK
Many methods for maximizing the AUC have been proposed (Yang & Ying, 2022; Ying et al.,
2016; Yuan et al., 2021b; Zhang et al., 2023; Yuan et al., 2021a). Although these methods perform
well, particularly on class-imbalanced data (Yuan et al., 2021a;b), they require labeled PN data for
training and are not designed for maximizing the pAUC. Since classifiers achieving high AUC are
not necessarily optimal with respect to the pAUC (Narasimhan & Agarwal, 2013a;b), pAUC needs
to be directly maximized.
PU learning methods have been proposed for training binary classifiers from only PU data (Bekker
& Davis, 2020; Elkan & Noto, 2008). A representative approach is the ERM, which rewrites the
risk using only PU data (Sugiyama et al., 2022; Du Plessis et al., 2015). Some methods use this
approach to maximize the AUC with PU data (Sakai et al., 2018; Xie et al., 2024; Xie & Li, 2018).
However, extending this approach to the pAUC is nontrivial because, unlike the AUC, the pAUC
depends on FPR-dependent score thresholds determined by the negative density. Thus, rewriting the
pairwise terms alone is insufficient. We show that these thresholds can also be represented using the
positive and marginal densities, enabling the pAUC to be reformulated from PU data.
2

Preprint
Many pAUC maximization methods have been proposed (Narasimhan & Agarwal, 2013a;b; Iwata
et al., 2020; Yao et al., 2022; Zhu et al., 2022; Ueda & Fujino, 2018; Zhou et al., 2025). Although
these methods are promising, they require labeled PN data for training. Iwata et al. (2020) presented
an approximation of the pAUC from PU data by heuristically treating all unlabeled instances whose
ranks fall within a specified range as negative. However, the resulting objective generally does not
coincide with the pAUC. In contrast, the proposed method reformulates the pAUC from PU data
without relying on this heuristic. Although Xie et al. (2024) also use score-based instance selection,
their method targets the full AUC rather than the pAUC.
3 PRELIMINARIES
In this section, we briefly explain AUC and pAUC. Let input instancex∈ Xand its class label
y∈ {−1,+1}be associated with probability densityp(x, y), where+1and−1correspond to PN
classes, respectively. The conditional probability densities for PN classes are denoted asp p(x) :=
p(x|y= +1)andp n(x) :=p(x|y=−1). Lets:X →Rbe a score function that represents the
relative tendency of an instance to be positive. The classifier is obtained by the score function with
thresholdt:y= sign(s(x)−t), wheresigndenotes a sign function.
The TPR with thresholdtis defined as the probability that the score of positive data is higher than
thresholdt:
TPR(t) :=E x∼pp [I(s(x)> t)],(1)
whereE x∼p [·]is the expectation over densityp, andI(·)is the indicator function;I(Z) = 1ifZis
true andI(Z) = 0otherwise. Similarly, the FPR with thresholdtis defined as the probability that
the score of negative data is higher than thresholdt:
FPR(t) :=E x∼pn [I(s(x)> t)].(2)
The AUC is defined as the area under the ROC curve plotted byTPR(t)againstFPR(t)with
varying thresholdt. Assuming there are no ties, it can be calculated by
AUC :=
Z 1
0
TPR(FPR−1(u))du=E xp∼ppExn∼pn [I(s(x p)> s(xn))],(3)
where
FPR−1(u) = inf{t∈R: FPR(t)≤u}(4)
(Yang & Ying, 2022).FPR −1(u)returns the lower threshold at which the FPR is no greater than
u. The AUC can be regarded as the probability that the score of positive data is higher than that of
negative data.
The pAUC betweenαandβ, where0≤α < β≤1, is defined as the normalized area under the
ROC curve plotted byTPR(t)againstFPR(t)whereFPR(t)is betweenαandβas follows:
pAUC(α, β) := 1 β−α Z β α TPR(FPR−1(u))du
= 1 β−α Exp∼pp Exn∼pn [I(s(x p)> s(xn))I(s(x n)∈[t β, tα])],(5)
wheret α := FPR −1(α)andt β := FPR −1(β)(Yang & Ying, 2022). The pAUC betweenαand
βis the probability that positive data have higher scores than negative data whose score is between
tβ = FPR−1(β)andt α = FPR−1(α). Due to the normalization factor1/(β−α), the pAUC takes
values between zero and one.
GivenN p positive instances{x p 1, . . . ,xp N p }drawn fromp p(x)andN n negative instances
{xn 1, . . . ,xn N n }drawn fromp n(x), the empirical estimator of the pAUC is calculated as
\pAUC(α, β) = 1 (β−α)N pN n
N p X
n=1
jβX
m=jα+1
I(s(x p n)> s(xn (m))),(6)
3

Preprint
wherej α :=αN n,j β :=βN n, andx n (m) is the negative instance ranked in them-th position among
negative data in a descending order of scoress(x) 1 (Dodd & Pepe, 2003). The empirical pAUC is
the empirical probability that positive data have higher scores than negative data that are ranked
betweenj α andj β.
4 PROPOSEDMETHOD
We first explain our problem setting in Section 4.1. Then, we derive the empirical estimator of the
pAUC with PU data in Section 4.2. Lastly, we describe the pAUC maximization method with the
derived pAUC estimator in Section 4.3.
4.1 PROBLEMSETTING
Suppose that we are given a set of positive instancesX p and a set of unlabeled instancesX:
X p :={x p n}N p n=1 i.i.d. ∼p p(x), X:={x n}N n=1 i.i.d. ∼p(x) =πp p(x) + (1−π)p n(x),(7)
wherep(x)is the marginal density, andπ:=p(y= +1)is the positive class-prior. We assume that
πis known as in the previous PU learning studies (Du Plessis et al., 2015; Kiryo et al., 2017; Iwata
et al., 2020). Whenπis unknown, it can be estimated from PU data (Scott, 2015; Ramaswamy et al.,
2016; Yao et al., 2021), as also illustrated in our experiments. Our goal is to learn score functions
that can maximize the pAUC betweenαandβfrom given PU dataX p ∪X.
4.2PAUC ESTIMATOR WITHPU DATA
We derive the empirical estimator of the pAUC with PU data. First, from the definition of marginal
densityp(x) =πp p(x) + (1−π)p n(x)in Eq. (7), the negative density can be represented as
pn(x) = 1 1−π [p(x)−πp p(x)].(8)
By substituting Eq. (8) into Eq. (5), we obtain
pAUC(α, β) = 1 (β−α)(1−π) [Exp∼ppEx∼p [I(s(x p)> s(x))I(s(x)∈[t β, tα])]
−πExp∼ppE¯xp∼pp [I(s(x p)> s(¯xp))I(s( ¯xp)∈[t β, tα])]].(9)
In Eq. (9), each expectation depends on positive or marginal densities; they can be approximated
with PU dataX p ∪X. However, thresholdst α = FPR −1(α)andt β = FPR −1(β)still depend
on negative densityp n(x). Therefore, we next represent thresholdst α = FPR −1(α)andt β =
FPR−1(β)using only the positive and marginal densities.
From Eq. (8), the FPR in Eq. (2) can be also rewritten as
FPR(t) =E x∼pn [I(s(x)> t)] = 1 1−π [Ex∼p [I(s(x)> t)]−πE xp∼pp [I(s(x p)> t)]].(10)
Sincet α = FPR −1(α)andt β = FPR −1(β), Eq. (10) implies that these population thresholds
are determined only by the positive and marginal densities. Thus, Eqs. (9) and (10) show that the
pAUC, including its thresholds, can be represented using only the positive and marginal densities.
From Eq. (10), the empirical estimator of the FPR with thresholdtis represented as
[FPR(t) = 1 1−π
"
1
N
NX
n=1
I(s(x n)> t)− π N p
N p X
n=1
I(s(x p n)> t)
#
.(11)
Sincet α = FPR−1(α) = inf{t∈R: FPR(t)≤α}, we want to estimate the lower threshold at
which Eq. (11) is no greater thanα. Since the value of Eq. (11) changes discretely when thresholdt
1For simplicity, we assumed thatj α andj β are both integers following the previous studies (Yao et al.,
2022; Narasimhan & Agarwal, 2013b).
4

Preprint
FPR(t)
ts(1) s(2) s(3) s(4)
1
s(5) s(6) s(7)
…
…
s(k) : score of positive instance
s(k) : score of unlabeled instance
The value of s(6) can be
used for threshold t

Figure 2: A visual explanation of determining threshold ˆtα: The vertical and horizontal axes rep-
resent [FPR(t)and thresholdt, respectively.s (k) denotes thek-th smallest score within the scores
of all training data{s(x)}, wherex∈X p ∪X. From Eq. (11), [FPR(t) = 1for anytsmaller
thans (1) and [FPR(t) = 0for anytgreater than or equal tos (N p+N) . [FPR(t)is a discrete function
where its value changes only whentcrosses one of the scores (k). When thresholdtexceeds the
score of the unlabeled (positive) instance, [FPR(t)decreases (increases). By checkings (1), s(2),· · ·
in ascending order and identifying the first (minimum) score at which [FPR(t)≤α, we can take the
score (s(6) in the figure) as the threshold ˆtα.
crosses the score of training instance, we can determine thresholdˆtα by simply examining the scores
of training PU dataX p ∪X, as shown in Figure 2. Specifically, threshold ˆtα can be determined as
ˆtα = min{s(x) : [FPR(s(x))≤α,x∈X p ∪X}.(12)
Similarly, threshold ˆtβ can be determined as
ˆtβ = min{s(x) : [FPR(s(x))≤β,x∈X p ∪X}.(13)
Note that when the value of Eq. (11) was less than zero or greater than one, we clipped the value to
zero and one, respectively.
By substituting estimated thresholds ˆtα and ˆtβ into Eq. (9), the empirical estimator of the pAUC can
be represented as
\pAUC(α, β) = 1 (β−α)(1−π)
" N p X
n=1
NX
m=1
 I(s(x p n)> s(xm))I(s(x m)∈[ ˆtβ, ˆtα])
N Np

−π
N p,N p X
n̸=m
 I(s(x p n)> s(xp m))I(s(x p m)∈[ ˆtβ, ˆtα])
N p(N p −1)

 ,(14)
where we omitted the case ofn=min the second term to avoid biases following the study (Sakai
et al., 2018). The finite-sample properties of this estimator are analyzed in Section A.
4.3PAUC MAXIMIZATION WITHPU DATA
We explain the pAUC maximization method using Eq. (14). Since the gradient of the indicator
functionI(·)is zero almost everywhere, the empirical pAUC in Eq. (14) cannot be maximized by
using gradient descent-based methods. To make the empirical pAUC differentiable, following the
previous studies (Iwata et al., 2020; Kumagai et al., 2024; 2025), we used the sigmoid function
σ(s(x)−s(x ′)) = 1/(1 + exp(−s(x) +s(x ′)))instead ofI(s(x)> s(x ′))in Eq. (14):
^pAUC(α, β) = 1 (β−α)(1−π)
" N p X
n=1
NX
m=1
 σ(s(xp n)−s(x m))I(s(x m)∈[ ˆtβ, ˆtα])
N Np

−π
N p,N p X
n̸=m
 σ(s(xp n)−s(x p m))I(s(x p m)∈[ ˆtβ, ˆtα])
N p(N p −1)

 .(15)
5

Preprint
Algorithm 1Training procedure of the proposed method
Require:PU dataX p ∪X, positive class-priorπ, FPR range valuesαandβ, positive mini-batch
sizeP, and unlabeled mini-batch sizeU
Ensure:Model parameters of score functions
1:repeat
2:Sample unlabeled data with sizeUfromX
3:Sample positive data with sizePfromX p
4:Calculate thresholds ˆtα and ˆtβ in Eqs. (12) and (13) with the sampled data
5:Calculate the loss in Eq. (16) on the sampled data
6:Update parameters ofswith the gradient of the loss
7:untilEnd condition is satisfied;
Here, we do not replace the indicator function term for instance selectionI(s(x)∈[ ˆtβ, ˆtα])with
the sigmoid function for simplicity and stability. This treatment is standard in previous pAUC max-
imization studies (Ueda & Fujino, 2018; Iwata et al., 2020; Yao et al., 2022). Thus, gradients are
only propagated through the sigmoid function terms during training. Note that we can use any sur-
rogate functions such as logistic and ramp functions instead of the sigmoid function (Sakai et al.,
2018). Maximizing ^pAUC(α, β)is equivalent to minimizing1− ^pAUC(α, β). Therefore, our loss
function for learningsis given as
L(s;α, β) = 1− ^pAUC(α, β).(16)
Algorithm 1 shows the training procedure of the proposed method with stochastic gradient descent
methods. We first sample PU data fromX p ∪X(Lines 2–3). Then, we calculate thresholds ˆtα
and ˆtβ by using Eqs. (12) and (13), respectively (Line 4). By using the estimated thresholds, we
calculate the loss in Eq. (16) for learning score functions(Line 5). Here, estimating the thresholds
and evaluating the loss on the same mini-batch is natural, because the thresholds themselves are part
of the empirical pAUC objective. Lastly, we update parameters of score functionsby using the
gradient of the loss (Line 6).
5 EXPERIMENTS
5.1 DATA
We used eight real-world datasets in the main paper: MNIST (LeCun et al., 1998), Fashion MNIST
(FMNIST) (Xiao et al., 2017), SVHN (Netzer et al., 2011), CIFAR10 (Krizhevsky et al., 2009),
SUSY (Baldi et al., 2014), CODRNA (Uzilov et al., 2006), IJCNN (Prokhorov, 2001), and EP-
SILON (Tsoumakas et al., 2008). These datasets have been commonly used in PU learning studies
(Kumagai et al., 2024; 2025; Xie et al., 2024; Kiryo et al., 2017; Jiang et al., 2023; Sakai & Shimizu,
2019; Hammoudeh & Lowd, 2020). In Section C.6, we used Mammography (Vanschoren et al.,
2014) and Online-shoppers (Sakar et al., 2019), which are medical- and advertising-related datasets.
MNIST comprises handwritten images of 10 digit classes, and FMNIST comprises images belong-
ing to 10 fashion categories. Each image in MNIST and FMNIST is represented as a28×28
grayscale image. SVHN consists of images of 10 printed digits cropped from photographs of house
number plates, while CIFAR-10 consists of images of 10 animal and vehicle categories. Each image
in SVHN and CIFAR-10 is represented as a32×32RGB image. SUSY , CODRNA, IJCNN, and
EPSILON are binary tabular datasets taken from the site of LIBSVM (Chang & Lin, 2011). The
numbers of features of SUSY , CODRNA, IJCNN, and EPSILON are 18, 8, 22, and 2,000, respec-
tively. For image datasets, we created binary classification tasks from each dataset following the data
creation procedure of previous studies (Kumagai et al., 2024; 2025; Xie et al., 2024). Specifically,
for MNIST and SVHN, we used odd digits as positive and even digits as negative. For FMNIST,
we used non-upper garment classes (1, 5, 7, 8, and 9) as positive and the others as negative. For
CIFAR10, we used the vehicle classes (0, 1, 8, and 9) as positive and the animal classes as negative.
For training in each dataset, we used 5,000 unlabeled data and changed the numbers of positive data
within{30,50,100}. Additionally, we used 50 positive and 1,000 unlabeled data for validation. For
6

Preprint
Table 1: Test average pAUCs and their standard deviations withα= 0,β= 0.1over different
labeled positive data sizesN p = 30,50, and100. Values in bold are not statistically different at
the5%level from the best performing method in each row according to a paired t-test. ‘# Best’ row
represents the number of results of each method that are the best or comparable to it.
DataπOurs NNPU PUAUC PAUC PUpAUCh 2step
MNIST 0.10.683±0.0740.522±0.131 0.627±0.056 0.597±0.070 0.675±0.073 0.633±0.058
0.20.633±0.0710.577±0.068 0.592±0.054 0.473±0.058 0.624±0.064 0.592±0.054
FMNIST 0.10.924±0.0250.756±0.022 0.895±0.037 0.824±0.0640.925±0.0280.907±0.037
0.20.914±0.0280.770±0.035 0.867±0.047 0.649±0.1190.912±0.0360.873±0.047
SVHN 0.10.247±0.0810.055±0.004 0.208±0.070 0.201±0.053 0.233±0.078 0.202±0.075
0.20.191±0.0730.054±0.004 0.171±0.053 0.161±0.032 0.152±0.065 0.157±0.053
CIFAR10 0.10.478±0.0780.050±0.039 0.459±0.078 0.362±0.075 0.466±0.0760.469±0.079
0.20.433±0.0750.070±0.0690.420±0.0780.256±0.0430.426±0.075 0.423±0.079
SUSY 0.10.454±0.0340.357±0.078 0.414±0.051 0.366±0.055 0.437±0.032 0.415±0.052
0.20.424±0.0450.370±0.058 0.389±0.054 0.245±0.052 0.389±0.047 0.385±0.054
CODRNA 0.1 0.741±0.047 0.317±0.266 0.749±0.057 0.630±0.071 0.744±0.0500.754±0.054
0.20.716±0.0560.691±0.064 0.719±0.062 0.495±0.0850.720±0.060 0.726±0.060
IJCNN 0.10.620±0.0940.264±0.118 0.563±0.087 0.525±0.071 0.600±0.100 0.572±0.090
0.20.565±0.0960.449±0.088 0.525±0.083 0.393±0.062 0.440±0.194 0.524±0.085
EPSILON 0.10.193±0.0410.078±0.0060.191±0.0430.175±0.0340.193±0.044 0.190±0.046
0.20.163±0.0450.081±0.0100.170±0.0390.139±0.0260.162±0.039 0.172±0.043
# Best 15 0 3 0 6 6
unlabeled data in training and validation, we changed class-priorπwithin{0.1,0.2}. We used 2,500
positive and 2,500 negative data as test data for evaluation. Training, validation, and test data did not
overlap. We conducted 10 different experiments for each positive class-prior and labeled positive
data size changing the random seeds and evaluated mean test pAUC.
5.2 COMPARISONMETHODS
We compared the proposed method (Ours) with five methods: non-negative PU learning method
(NNPU) (Kiryo et al., 2017), AUC maximization method with PU data (PUAUC) (Xie & Li, 2018;
Xie et al., 2024), pAUC maximization method (PAUC) (Ueda & Fujino, 2018), pAUC maximization
method with PU data based on the heuristic scoring assumption (PUpAUCh) (Iwata et al., 2020),
and two-step pAUC maximization method with PU data (2step). All methods including the proposed
method used neural networks for modeling classifiers (score functions).
NNPU is a widely used PU learning method for balanced binary classification, which trains the
classifier by minimizing the non-negative classification risk rewritten with PU data. PUAUC trains
the classifier by maximizing the AUC rewritten with PU data. PAUC maximizes the pAUC by using
PU data regarding all unlabeled data as negative. PUpAUCh maximizes the pAUC from PU data
by heuristically treating all unlabeled instances within a specified rank range based on their current
scores as negative during training. 2step first trains a classifier by using PUAUC, and then assigns
pseudo PN labels to the unlabeled data by using the trained classifier. Specifically, it selects the
topπNunlabeled instances according to the classifier scores as pseudo-positive, and assigns the
remaining instances as pseudo-negative. Then, it applied PAUC for the positive and pseudo PN data
to train the classifier. The proposed method, NNPU, PUpAUCh, and 2step used class-prior valueπ
for training. The details of settings such as network architectures are described in section B.
5.3 RESULTS
Tables 1 and 2 show the average test pAUCs and their standard deviations for two settingsα= 0,
β= 0.1, andα= 0,β= 0.2, respectively. We used pAUC withα= 0since it is often used in
previous studies and real-world applications (Narasimhan & Agarwal, 2013a; Iwata et al., 2020; Zhu
et al., 2022). The results withα= 0.1andβ= 0.2are also reported in Section C.1. The proposed
method performed the best or comparably to it in almost all cases (31 out of 32). NNPU did not
work well since it is not designed for both class-imbalanced data and pAUC maximization. PUAUC
outperformed NNPU since maximizing the AUC is appropriate for class-imbalanced data. However,
it was often outperformed by the proposed method by a large margin, which indicates the impor-
tance of explicitly maximizing the pAUC. PAUC did not perform well either even though it aims to
maximize the pAUC. This is because it merely treats all unlabeled data as negative, which leads to
7

Preprint
Table 2: Test average pAUCs and their standard deviations withα= 0,β= 0.2over different
labeled positive data sizesN p = 30,50, and100. Values in bold are not statistically different at
the5%level from the best performing method in each row according to a paired t-test. ‘# Best’ row
represents the number of results of each method that are the best or comparable to it.
DataπOurs NNPU PUAUC PAUC PUpAUCh 2step
MNIST 0.10.755±0.0560.610±0.127 0.725±0.048 0.736±0.055 0.749±0.055 0.730±0.050
0.20.723±0.0650.677±0.062 0.696±0.049 0.652±0.0620.717±0.0560.697±0.049
FMNIST 0.10.943±0.0220.775±0.016 0.925±0.028 0.926±0.0320.940±0.0230.934±0.027
0.20.934±0.0230.789±0.033 0.904±0.034 0.853±0.0590.931±0.0260.911±0.033
SVHN 0.10.342±0.0920.105±0.005 0.305±0.0810.334±0.0860.329±0.089 0.313±0.084
0.20.289±0.0900.104±0.005 0.262±0.063 0.264±0.052 0.221±0.067 0.259±0.064
CIFAR10 0.10.610±0.0740.089±0.058 0.595±0.072 0.569±0.0700.600±0.062 0.608±0.070
0.20.578±0.0750.116±0.094 0.559±0.078 0.459±0.0700.569±0.066 0.564±0.077
SUSY 0.10.553±0.0320.457±0.075 0.522±0.041 0.528±0.046 0.540±0.028 0.523±0.042
0.20.528±0.0440.474±0.051 0.499±0.047 0.434±0.056 0.508±0.039 0.500±0.045
CODRNA 0.10.853±0.0340.386±0.292 0.850±0.041 0.830±0.0470.855±0.035 0.856±0.038
0.20.838±0.0390.791±0.059 0.827±0.048 0.705±0.0720.839±0.039 0.833±0.047
IJCNN 0.10.711±0.0790.367±0.111 0.670±0.084 0.687±0.073 0.687±0.101 0.683±0.084
0.20.659±0.1020.543±0.092 0.637±0.087 0.573±0.068 0.599±0.132 0.641±0.089
EPSILON 0.10.305±0.0580.128±0.0070.298±0.0550.290±0.0430.304±0.053 0.299±0.060
0.20.269±0.0460.132±0.0120.260±0.0500.248±0.0370.261±0.053 0.270±0.055
# Best 16 0 2 1 9 6
40 60 80 100
Np
0.60
0.65
0.70
0.75
0.80T est pAUC
Ours
NNPU
PUAUC
PAUC
PUpAUCh
2step
(a) MNIST
40 60 80 100
Np
0.80
0.85
0.90
0.95T est pAUC (b) FMNIST
40 60 80 100
Np
0.1
0.2
0.3
0.4T est pAUC (c) SVHN
40 60 80 100
Np
0.1
0.2
0.3
0.4
0.5
0.6
0.7T est pAUC (d) CIFAR10
40 60 80 100
Np
0.425
0.450
0.475
0.500
0.525
0.550
0.575T est pAUC
(e) SUSY
40 60 80 100
Np
0.5
0.6
0.7
0.8
0.9T est pAUC (f) CODRNA
40 60 80 100
Np
0.4
0.5
0.6
0.7
0.8T est pAUC (g) IJCNN
40 60 80 100
Np
0.15
0.20
0.25
0.30
0.35T est pAUC (h) EPSILON
Figure 3: The average test pAUCs and their standard errors withα= 0,β= 0.2over different
class-priorsπ∈ {0.1,0.2}when changing the number of labeled positive dataN p.
very biased results. PUpAUCh outperformed these methods (NNPU, PUAUC, and PAUC) since it
is explicitly designed for maximizing the pAUC with PU data. However, it is often outperformed
by the proposed method. Section C.8 shows that its heuristic assumption is frequently violated dur-
ing training. Although 2step performed comparably to PUpAUCh, its performance was limited by
the label noise inherent in the pseudo PN data. Overall, these results show the effectiveness of our
method for maximizing the pAUC from PU data.
As for the results of each class-priorπin Tables 1 and 2, all methods except NNPU tended to
perform worse asπincreased. This is because these (p)AUC maximization-based methods include
a term in their objective functions that encourages the scores of positive data to be higher than those
of unlabeled data (e.g., the first term in Eq. (15) for the proposed method). Whenπis small, the
unlabeled data can be regarded as mostly negative and thus the corresponding objective function
term becomes more suitable for learning accurate score functions that can rank positive data higher
than negative ones. As a result, the performance tends to improve (degrade) asπis decreased
(increased). On the other hand, since increasingπreduces the severity of class-imbalance, NNPU
tended to perform better. Nevertheless, since our focus is on the class-imbalanced problem, these
results support the effectiveness of the proposed method. In Section C.2, we further confirmed the
effectiveness of the proposed method under smaller and larger class-prior values.
8

Preprint
0.10 0.15 0.20 0.25 0.30
Input π
0.69
0.70
0.71
0.72
0.73T est pAUC
Ours
PUAUC
PUpAUCh
2step
(a) MNIST
0.10 0.15 0.20 0.25 0.30
Input π
0.88
0.89
0.90
0.91
0.92
0.93
0.94T est pAUC (b) FMNIST
0.10 0.15 0.20 0.25 0.30
Input π
0.15
0.20
0.25
0.30T est pAUC (c) SVHN
0.10 0.15 0.20 0.25 0.30
Input π
0.52
0.54
0.56
0.58
0.60T est pAUC (d) CIFAR10
0.10 0.15 0.20 0.25 0.30
Input π
0.49
0.50
0.51
0.52
0.53T est pAUC
(e) SUSY
0.10 0.15 0.20 0.25 0.30
Input π
0.78
0.80
0.82
0.84T est pAUC (f) CODRNA
0.10 0.15 0.20 0.25 0.30
Input π
0.50
0.55
0.60
0.65T est pAUC (g) IJCNN
0.10 0.15 0.20 0.25 0.30
Input π
0.18
0.20
0.22
0.24
0.26
0.28T est pAUC (h) EPSILON
Figure 4: The average test pAUCs and their standard errors withα= 0,β= 0.2when true class-
priorπ= 0.2. ‘Inputπ’ means the class-prior value used for training.
Table 3: The results using estimated class-prior when the true class-prior isπ= 0.2: test average
pAUCs and their standard deviations withα= 0,β= 0.2over different labeled positive data sizes
N p = 30,50, and100. Values in bold are not statistically different at the5%level from the best
performing method in each row according to a paired t-test. ‘# Best’ row represents the number of
results of each method that are the best or comparable to it.
DataπOurs NNPU PUAUC PAUC PUpAUCh 2step
MNIST 0.20.721±0.0610.676±0.065 0.696±0.049 0.652±0.0620.716±0.0530.697±0.049
FMNIST 0.20.933±0.0240.808±0.055 0.904±0.034 0.853±0.0590.932±0.0260.910±0.033
SVHN 0.20.301±0.0730.104±0.005 0.262±0.063 0.264±0.0520.292±0.0830.266±0.063
CIFAR10 0.20.571±0.0640.494±0.0780.559±0.0780.459±0.070 0.539±0.0810.556±0.078
SUSY 0.20.523±0.0440.488±0.051 0.499±0.047 0.434±0.056 0.505±0.039 0.498±0.046
CODRNA 0.2 0.821±0.043 0.639±0.167 0.827±0.048 0.705±0.0720.824±0.043 0.829±0.047
IJCNN 0.20.646±0.0430.198±0.043 0.637±0.087 0.573±0.068 0.616±0.1060.650±0.084
EPSILON 0.20.274±0.0490.128±0.0080.269±0.0500.248±0.0370.270±0.046 0.270±0.053
# Best 7 0 2 0 5 4
Figure 3 shows the average test pAUCs with their standard errors when changing the number of la-
beled positive dataN p. The proposed method consistently performed well across different numbers
of labeled positive data. Since labeled positive data are informative for training, the proposed method
tended to perform better asN p increased. In Section C.4, we also evaluated the proposed method
with different unlabeled training data sizesNand found that it performed well across differentN.
pAUC maximization methods with PU data (the proposed method, PUpAUCh, and 2step) need to
know true class-priorπfor training. Although we evaluated these methods with true class-priors in
our experiments following the previous PU learning studies (Iwata et al., 2020; Kiryo et al., 2017;
Du Plessis et al., 2015), there might be some noise in practice. Therefore, we investigated how the
performance of the proposed method changes when using noisy class-priors for training. Figure 4
shows the results. Here, PUAUC is a strong baseline that does not depend onπfor training. The
proposed method performed well in many cases, even when the class-prior used for training (Input
π) differed from true class-priorπ. These results show that the proposed method robustly works
well as long as noise on the class-prior is not so large.
Furthermore, we examined the performance of the proposed method when using the class-priors
estimated from PU data. For this, we used the kernel embedding-based class-prior estimation
method (Ramaswamy et al., 2016). The estimated class-priors of MNIST, FMNIST, SVHN, CI-
FAR10, SUSY , CODRNA, IJCNN, and EPSILON were0.214,0.208,0.096,0.382,0.226,0.159,
0.113, and0.159, respectively. Table 3 shows the average test pAUCs and their standard deviations
when using the estimated class-priors. The proposed method still performed well. These results
suggest that the proposed method remains effective and practically applicable even when the class-
priors are estimated from data.
9

Preprint
6 CONCLUSION
We proposed a method for maximizing the pAUC from PU data by representing the pAUC, includ-
ing its FPR-dependent thresholds, using only the positive and marginal densities. Based on this
reformulation, we derived an empirical estimator whose smoothed version enables classifier train-
ing without negative data. Experiments on ten real-world datasets demonstrated its effectiveness
compared with existing PU learning, AUC maximization, and pAUC maximization methods.
REFERENCES
Stuart G Baker and Paul F Pinsky. A proposed design and analysis for comparing digital and analog
mammography: special receiver operating characteristic methods for cancer screening.Journal
of the American Statistical Association, 96(454):421–428, 2001.
Pierre Baldi, Peter Sadowski, and Daniel Whiteson. Searching for exotic particles in high-energy
physics with deep learning.Nature communications, 5(1):4308, 2014.
Jessa Bekker and Jesse Davis. Learning from positive and unlabeled data: a survey.Machine
Learning, 109(4):719–760, 2020.
Andrew P Bradley. The use of the area under the roc curve in the evaluation of machine learning
algorithms.Pattern recognition, 30(7):1145–1159, 1997.
Chih-Chung Chang and Chih-Jen Lin. Libsvm: a library for support vector machines.ACM trans-
actions on intelligent systems and technology (TIST), 2(3):1–27, 2011.
Corinna Cortes and Mehryar Mohri. Auc optimization vs. error rate minimization.NeurIPS, 2003.
Lori E Dodd and Margaret S Pepe. Partial auc estimation and regression.Biometrics, 59(3):614–623,
2003.
Marthinus Du Plessis, Gang Niu, and Masashi Sugiyama. Convex formulation for learning from
positive and unlabeled data. InICML, 2015.
Charles Elkan and Keith Noto. Learning classifiers from only positive and unlabeled data. In
SIGKDD, 2008.
Zayd Hammoudeh and Daniel Lowd. Learning from positive and unlabeled data with arbitrary
positive shift. InNeurIPS, 2020.
Tomoharu Iwata, Akinori Fujino, and Naonori Ueda. Semi-supervised learning for maximizing the
partial auc. InAAAI, 2020.
Yangbangyan Jiang, Qianqian Xu, Yunrui Zhao, Zhiyong Yang, Peisong Wen, Xiaochun Cao, and
Qingming Huang. Positive-unlabeled learning with label distribution alignment.IEEE Transac-
tions on Pattern Analysis and Machine Intelligence, 2023.
Diederik P Kingma and Jimmy Ba. Adam: a method for stochastic optimization.arXiv preprint
arXiv:1412.6980, 2014.
Ryuichi Kiryo, Gang Niu, Marthinus C Du Plessis, and Masashi Sugiyama. Positive-unlabeled
learning with non-negative risk estimator.NeurIPS, 2017.
Alex Krizhevsky, Geoffrey Hinton, et al. Learning multiple layers of features from tiny images.
2009.
Atsutoshi Kumagai, Tomoharu Iwata, Hiroshi Takahashi, Taishi Nishiyama, and Yasuhiro Fujiwara.
Auc maximization under positive distribution shift. InNeurIPS, 2024.
Atsutoshi Kumagai, Tomoharu Iwata, Hiroshi Takahashi, Taishi Nishiyama, Kazuki Adachi, and
Yasuhiro Fujiwara. Positive-unlabeled auc maximization under covariate shift. InICML, 2025.
Yann LeCun, L´eon Bottou, Yoshua Bengio, and Patrick Haffner. Gradient-based learning applied to
document recognition.Proceedings of the IEEE, 86(11):2278–2324, 1998.
10

Preprint
Pascal Massart. The tight constant in the dvoretzky-kiefer-wolfowitz inequality.The annals of
Probability, pp. 1269–1283, 1990.
Yisroel Mirsky, Tomer Doitshman, Yuval Elovici, and Asaf Shabtai. Kitsune: an ensemble of au-
toencoders for online network intrusion detection. InNDSS, 2018.
Mehryar Mohri, Afshin Rostamizadeh, and Ameet Talwalkar.F oundations of machine learning,
volume 2. MIT press Cambridge, 2012.
Harikrishna Narasimhan and Shivani Agarwal. A structural svm based approach for optimizing
partial auc. InICML, 2013a.
Harikrishna Narasimhan and Shivani Agarwal. Svmpauctight: a new support vector method for
optimizing partial auc based on a tight convex upper bound. InKDD, 2013b.
Yuval Netzer, Tao Wang, Adam Coates, Alessandro Bissacco, Baolin Wu, Andrew Y Ng, et al.
Reading digits in natural images with unsupervised feature learning. InNIPS workshop on deep
learning and unsupervised feature learning, volume 2011, pp. 7. Granada, Spain, 2011.
Taishi Nishiyama, Atsutoshi Kumagai, Akinori Fujino, and Kazunori Kamiya. Partial auc maxi-
mization for security log analysis robust to overfitting and noisy labels. InGLOBECOM, 2024.
Adam Paszke, Sam Gross, Soumith Chintala, Gregory Chanan, Edward Yang, Zachary DeVito,
Zeming Lin, Alban Desmaison, Luca Antiga, and Adam Lerer. Automatic differentiation in
pytorch. 2017.
Danil Prokhorov. Ijcnn 2001 neural network competition.Slide presentation in IJCNN, 1(97):38,
2001.
Harish Ramaswamy, Clayton Scott, and Ambuj Tewari. Mixture proportion estimation via kernel
embeddings of distributions. InICML, 2016.
Tomoya Sakai and Nobuyuki Shimizu. Covariate shift adaptation on learning from positive and
unlabeled data. InAAAI, 2019.
Tomoya Sakai, Gang Niu, and Masashi Sugiyama. Semi-supervised auc optimization based on
positive-unlabeled learning.Machine Learning, 107:767–794, 2018.
C Okan Sakar, S Olcay Polat, Mete Katircioglu, and Yomi Kastro. Real-time prediction of online
shoppers’ purchasing intention using multilayer perceptron and lstm recurrent neural networks.
Neural Computing and Applications, 31(10):6893–6908, 2019.
Clayton Scott. A rate of convergence for mixture proportion estimation, with application to learning
from noisy labels. InAISTATS, 2015.
Masashi Sugiyama, Han Bao, Takashi Ishida, Nan Lu, and Tomoya Sakai.Machine learning from
weak supervision: An empirical risk minimization approach. MIT Press, 2022.
Grigorios Tsoumakas, Ioannis Katakis, and Ioannis Vlahavas. Effective and efficient multilabel
classification in domains with large number of labels. InProc. ECML/PKDD 2008 workshop on
mining multidimensional data, 2008.
Naonori Ueda and Akinori Fujino. Partial auc maximization via nonlinear scoring functions.arXiv
preprint arXiv:1806.04838, 2018.
Andrew V Uzilov, Joshua M Keegan, and David H Mathews. Detection of non-coding rnas on the
basis of predicted secondary structure formation free energy change.BMC bioinformatics, 7(1):
173, 2006.
Joaquin Vanschoren, Jan N Van Rijn, Bernd Bischl, and Luis Torgo. Openml: networked science in
machine learning.ACM SIGKDD Explorations Newsletter, 15(2):49–60, 2014.
Han Xiao, Kashif Rasul, and Roland V ollgraf. Fashion-mnist: a novel image dataset for benchmark-
ing machine learning algorithms.arXiv preprint arXiv:1708.07747, 2017.
11

Preprint
Zheng Xie and Ming Li. Semi-supervised auc optimization without guessing labels of unlabeled
data. InAAAI, 2018.
Zheng Xie, Yu Liu, Hao-Yuan He, Ming Li, and Zhi-Hua Zhou. Weakly supervised auc optimization:
a unified partial auc approach.IEEE Transactions on Pattern Analysis and Machine Intelligence,
2024.
Tianbao Yang and Yiming Ying. Auc maximization in the era of big data and ai: a survey.ACM
computing surveys, 55(8):1–37, 2022.
Yao Yao, Qihang Lin, and Tianbao Yang. Large-scale optimization of partial auc in a range of false
positive rates. InNeurIPS, 2022.
Yu Yao, Tongliang Liu, Bo Han, Mingming Gong, Gang Niu, Masashi Sugiyama, and Dacheng Tao.
Rethinking class-prior estimation for positive-unlabeled learning. InICLR, 2021.
Yiming Ying, Longyin Wen, and Siwei Lyu. Stochastic online auc maximization.NeurIPS, 2016.
Zhuoning Yuan, Zhishuai Guo, Nitesh Chawla, and Tianbao Yang. Compositional training for end-
to-end deep auc maximization. InICLR, 2021a.
Zhuoning Yuan, Yan Yan, Milan Sonka, and Tianbao Yang. Large-scale robust deep auc maximiza-
tion: a new surrogate loss and empirical studies on medical image classification. InProceedings
of the IEEE/CVF International Conference on Computer Vision, pp. 3040–3049, 2021b.
Xinwen Zhang, Yihan Zhang, Tianbao Yang, Richard Souvenir, and Hongchang Gao. Federated
compositional deep auc maximization.NeurIPS, 2023.
Linli Zhou, Bokun Wang, My T. Thai, and Tianbao Yang. Stochastic primal-dual double block-
coordinate for two-way partial auc maximization.Transactions on Machine Learning Research,
2025. ISSN 2835-8856.
Dixian Zhu, Gang Li, Bokun Wang, Xiaodong Wu, and Tianbao Yang. When auc meets dro: opti-
mizing partial auc for deep learning with non-convex convergence guarantee. InICML, 2022.
A THEORETICALANALYSIS
In this section, we analyze the finite-sample properties of the proposed pAUC estimator in Eq. (14).
We first analyze the estimation error of the FPR estimator in Eq. (11) and the FPRs at the estimated
thresholds ˆtα and ˆtβ. Then, we derive a finite-sample error bound for the empirical pAUC estimator
in Eq. (14). Finally, we analyze the effect of class-prior estimation error. Throughout this section,
we assume0≤α < β <1, which covers all settings of interest.
For the analysis, we explicitly write the dependence on score functionswhen necessary. LetSbe a
class of score functions. Fors∈ S, define
F s(t) :=E x∼p [I(s(x)> t)],(17)
F
p
s (t) :=E xp∼pp [I(s(x p)> t)],(18)
and their empirical versions as
bF s(t) := 1 N
NX
n=1
I(s(x n)> t),(19)
bF p s (t) := 1 N p N p X n=1 I(s(x p n)> t).(20)
Then, Eqs. (10) and (11) can be written as
FPRs(t) = F s(t)−π F
p
s (t)
1−π ,(21)
[FPRs(t) =
bF s(t)−π bF p s (t)
1−π .(22)
12

Preprint
We use the following assumption.
Assumption A.1.F or everys∈ Sconsidered in the analysis, the distribution ofs(x n)underp n(x)
has no point masses.
Assumption A.1 serves as a convenient sufficient condition for handling the data-dependent esti-
mated thresholds in the finite-sample analysis, as it ensures thatFPR s(t)is continuous int. We
use this continuity below when relating an estimated threshold to the FPR at that threshold. When
α= 0, it is possible that no finite threshold achievesFPR s(t) = 0. In this case, we sett α,s = +∞,
defineFPR s(+∞) = 0, and interpret[t β,s, tα,s]as[t β,s,∞).
A.1 UNIFORMCONVERGENCE OF THESCORESURVIVALPROBABILITIES
Define the uniform estimation errors of the marginal and positive score survival probabilities as
∆N := sup
s∈S, t∈R

 bF s(t)− F s(t)

 ,(23)
∆N p := sup
s∈S, t∈R

 bF p s (t)− F p s (t)

 .(24)
Thus,∆ N and∆ N p are the largest estimation errors of the marginal and positive score survival
probabilities, respectively, over alls∈ Sandt∈R.
We first consider a finite score-function classSwith|S|=M. For any fixeds∈ S, the Dvoretzky–
Kiefer–Wolfowitz (DKW) inequality (Massart, 1990) gives
P

sup
t∈R

 bF s(t)− F s(t)

 > ϵ  ≤2 exp(−2N ϵ2).(25)
Although the DKW inequality is usually stated for cumulative distribution functions, it can also be
directly applied to the survival probabilities since F s(t) = 1−F s(t)and bF s(t) = 1− bFs(t), where
Fs and bFs are the population and empirical cumulative distribution functions ofs(x), respectively.
Applying the union bound over allMscore functions gives
P(∆ N > ϵ)≤2Mexp(−2N ϵ2).(26)
Setting the right-hand side toδ/2gives
ϵN =
r
log(4M/δ)
2N ,(27)
and therefore
P(∆ N ≤ϵ N )≥1− δ 2 .(28)
Applying the same argument to theN p positive instances gives
ϵN p =
r
log(4M/δ)
2N p ,(29)
such thatP(∆ N p ≤ϵ N p )≥1−δ/2. Thus, by the union bound, with probability at least1−δ,
∆N ≤ϵ N ,∆ N p ≤ϵ N p (30)
hold simultaneously. In particular, for a finite score-function class, the empirical marginal and
positive score survival probabilities converge uniformly to their population values, with errors of
orders
O
 r
log(M/δ)
N
!
andO
 r
log(M/δ)
N p
!
,(31)
respectively.
13

Preprint
The following analysis only requires the uniform bounds in Eq. (30). Therefore, the results are not
restricted to finite score-function classes. For a score functionsand a thresholdt, define
Cs,t :={x∈ X:s(x)> t}.(32)
Consider the collection of these sets over all score functions and thresholds:
C:={C s,t :s∈ S, t∈R}.(33)
Since
F s(t) =P x∼p (x∈C s,t), bF s(t) = 1 N
NX
n=1
I(x n ∈C s,t),(34)
we have
∆N = sup
C∈C

 1 N NX n=1 I(x n ∈C)−P x∼p (x∈C)

 .(35)
Therefore, ifChas finite VC dimensiond, a standard VC uniform-convergence bound (Mohri et al.,
2012) gives
∆N =O
 r
dlog(2N) + log(2/δ)
N
!
(36)
with probability at least1−δ/2. Applying the same argument to the positive distribution using the
same set classCand theN p positive instances gives
∆N p =O
 r
dlog(2N p) + log(2/δ)
N p
!
(37)
with probability at least1−δ/2. Thus, by the union bound, both bounds hold simultaneously with
probability at least1−δ. Therefore, the following results also apply to infinite score-function classes
when the threshold-set classChas finite VC dimension.
A.2 ACCURACY OF THEPU-BASEDFPR ESTIMATOR ANDESTIMATEDTHRESHOLDS
We first analyze the error of the FPR estimator in Eq. (11).
Theorem A.2.Suppose that
∆N ≤ϵ N ,∆ N p ≤ϵ N p.(38)
Then,
sup
s∈S, t∈R

[FPRs(t)−FPR s(t)

 ≤ϵ FPR,(39)
where
ϵFPR := ϵN +πϵ N p
1−π .(40)
The same bound holds when [FPRs(t)is clipped to[0,1]as in the proposed method.
Proof.Using Eqs. (21) and (22), we have

[FPRs(t)−FPR s(t)

= 1 1−π

  bF s(t)− F s(t)  −π  bF p s (t)− F p s (t) 

≤ 1 1−π h

 bF s(t)− F s(t)

 +π

 bF p s (t)− F p s (t)

 i
≤ ∆N +π∆ N p
1−π
≤ ϵN +πϵ N p
1−π =ϵ FPR.(41)
Since this holds for everys∈ Sandt∈R, by taking the supremum, we obtain Eq. (39). Since
FPRs(t)∈[0,1], clipping [FPRs(t)to[0,1]cannot increase the estimation error. Thus, the same
bound also holds for the clipped estimator.
14

Preprint
Forγ∈ {α, β}, letˆtγ,s denote the estimated threshold obtained by Eq. (12) or Eq. (13), respectively,
for score functions. Sinceα < β,
n
t: [FPRs(t)≤α
o
⊆
n
t: [FPRs(t)≤β
o
.(42)
Therefore, ˆtβ,s ≤ ˆtα,s even though [FPRs(t)is not necessarily monotonic int.
Theorem A.3.Suppose that Assumption A.1 holds,0≤α < β <1, and
∆N ≤ϵ N ,∆ N p ≤ϵ N p.(43)
Then, for everys∈ Sandγ∈ {α, β},

FPRs(ˆtγ,s)−γ

 ≤ϵ FPR.(44)
Proof.We fixsand omit its subscript for simplicity. Since0≤γ <1, clipping [FPRs(t)to[0,1]
does not change the set of thresholds satisfying [FPRs(t)≤γ. From the definition of ˆtγ in Eqs. (12)
and (13),
[FPR(ˆtγ)≤γ.(45)
Therefore, Theorem A.2 gives
FPR(ˆtγ)≤γ+ϵ FPR.(46)
For the lower bound, ˆtγ is the smallest score among the PU instances at which the empirical FPR is
no greater thanγ. Suppose first that ˆtγ is not the smallest score among the PU instances, and lett − γ
be the largest distinct score smaller than ˆtγ. By the definition of ˆtγ,
[FPR(t− γ )> γ.(47)
Since there is no PU instance whose score lies in(t − γ , ˆtγ), the empirical FPR is constant on this
interval. Therefore,
[FPR(t)> γ, t∈(t − γ , ˆtγ).(48)
If ˆtγ is the smallest score among the PU instances, then all PU instances have scores greater thant
for anyt < ˆtγ. Hence,
[FPR(t) = 1−π 1−π = 1> γ.(49)
Thus, in either case, there is a left neighborhood of ˆtγ in which [FPR(t)> γ. This argument does
not require [FPR(t)to be monotonic. Fortapproaching ˆtγ from below, Theorem A.2 gives
FPR(t)> γ−ϵ FPR.(50)
Assumption A.1 ensures thatFPR(t)is continuous. Therefore, takingt↑ ˆtγ gives
FPR(ˆtγ)≥γ−ϵ FPR.(51)
Combining Eqs. (46) and (51) gives

FPR(ˆtγ)−γ

 ≤ϵ FPR.(52)
Sinces∈ Sandγ∈ {α, β}were arbitrary, the result holds for everys∈ Sandγ∈ {α, β}.
Theorem A.3 directly bounds the quantity needed for pAUC estimation. The estimated threshold
values themselves do not need to be close to their population values as long as the FPRs at the
estimated thresholds are close to the target valuesαandβ.
15

Preprint
A.3 FINITE-SAMPLEERROR OF THEEMPIRICAL PAUC ESTIMATOR
We next analyze the empirical pAUC estimator in Eq. (14). Forb∈Randa∈R∪ {+∞}with
b≤a, define
As(a, b) :=Exp∼ppEx∼p [I(s(x p)> s(x))I(s(x)∈[b, a])],(53)
Bs(a, b) :=Exp∼ppE¯xp∼pp [I(s(x p)> s(¯xp))I(s( ¯xp)∈[b, a])].(54)
Their empirical versions are
bAs(a, b) := 1 N Np
N p X
n=1
NX
m=1
I(s(x p n)> s(xm))I(s(x m)∈[b, a]),(55)
bBs(a, b) := 1 N p(N p −1)
N p X
n,m=1
n̸=m
I(s(x p n)> s(xp m))I(s(x p m)∈[b, a]).(56)
Define
Qs(a, b) :=As(a, b)−πBs(a, b) (β−α)(1−π) .(57)
Using Eq. (8), we have
Qs(a, b) = 1 β−α Exp∼ppExn∼pn [I(s(x p)> s(xn))I(s(x n)∈[b, a])].(58)
Therefore,
Qs(tα,s, tβ,s) = pAUCs(α, β).(59)
We use the following lemma.
Lemma A.4.LetZ 1, . . . , Zn be i.i.d. copies of a random variableZand suppose that
sup
t∈R

 1 n nX i=1 I(Z i > t)−P(Z > t)

 ≤ϵ.(60)
Then, for any non-increasing functiong:R→[0,1],
sup
b≤a

 1 n nX i=1 g(Zi)I(Z i ∈[b, a])−E[g(Z)I(Z∈[b, a])]

 ≤2ϵ,(61)
where the supremum is taken overa, b∈R.
Proof.Fix a realization ofZ 1, . . . , Zn satisfying Eq. (60). Then,

 1 n nX i=1 I(Z i > t)−P(Z > t)

 ≤ϵfor allt∈R.(62)
The probability of any interval can be expressed using differences and one-sided limits of the tail
probabilities in Eq. (60). Therefore,

 1 n nX i=1 I(Z i ∈J)−P(Z∈J)

 ≤2ϵ(63)
for any intervalJ. For example, for a closed left endpoint, we use
P(Z∈[b,∞)) = lim
t↑b
P(Z > t), 1 n
nX
i=1
I(Z i ∈[b,∞)) = lim t↑b
1
n
nX
i=1
I(Z i > t).(64)
16

Preprint
Next, since0≤g(z)≤1, we use
g(z) =
Z 1
0
I(g(z)> u)du.(65)
Multiplying both sides byI(z∈[b, a])gives
g(z)I(z∈[b, a]) =
Z 1
0
I(z∈[b, a])I(g(z)> u)du
=
Z 1
0
I(z∈J u)du,(66)
where
Ju = [b, a]∩ {z:g(z)> u}.(67)
Sincegis non-increasing,{z:g(z)> u}is a half-line, i.e., a set of the form(−∞, c)or(−∞, c]
(possibly empty or all ofR). Therefore,J u is an interval, possibly empty, for everyu∈[0,1]. By
Eq. (63),

 1 n nX i=1 I(Z i ∈J u)−P(Z∈J u)

 ≤2ϵ.(68)
Applying the above identity to eachZ i and toZ, we have
1
n
nX
i=1
g(Zi)I(Z i ∈[b, a])−E[g(Z)I(Z∈[b, a])]
=
Z 1
0
(
1
n
nX
i=1
I(Z i ∈J u)−P(Z∈J u)
)
du.(69)
Therefore,

 1 n nX i=1 g(Zi)I(Z i ∈[b, a])−E[g(Z)I(Z∈[b, a])]

≤
Z 1
0

 1 n nX i=1 I(Z i ∈J u)−P(Z∈J u)

 du
≤
Z 1
0
2ϵ du= 2ϵ.(70)
Since this holds for everyb≤a, taking the supremum proves Eq. (61).
Lemma A.5.Suppose that∆ N ≤ϵ N and∆ N p ≤ϵ N p. Then, for everys∈ Sanda, b∈Rwith
b≤a,

 bAs(a, b)−As(a, b)

 ≤2ϵ N +ϵ N p ,(71)

 bBs(a, b)−Bs(a, b)

 ≤3 N p N p −1 ϵN p + 1 N p −1 .(72)
Proof.Using Eqs. (18) and (53), we have
As(a, b) =Ex∼p
h
F
p
s (s(x))I(s(x)∈[b, a])
i
.(73)
Similarly, Eq. (55) can be written as
bAs(a, b) = 1 N
NX
m=1
bF p s (s(xm))I(s(x m)∈[b, a]).(74)
17

Preprint
Therefore,

 bAs(a, b)−As(a, b)

≤

 1 N NX m=1 h bF p s (s(xm))− F p s (s(xm)) i I(s(x m)∈[b, a])

+

 1 N NX m=1 F p s (s(xm))I(s(x m)∈[b, a])−A s(a, b)

 .(75)
By the definition of∆ N p, the first term is at mostϵ N p. Since F
p
s (z)is non-increasing inz,
Lemma A.4, applied to the marginal scoresZ m =s(x m)together with∆ N ≤ϵ N , bounds the
second term by2ϵ N . This proves Eq. (71).
For bBs(a, b), we first introduce the corresponding V-statistic so that the pairwise sum can be written
using the empirical positive score survival probability:
bBV s (a, b) := 1 (N p)2
N p X
n=1
N p X
m=1
I(s(x p n)> s(xp m))I(s(x p m)∈[b, a]).(76)
Using Eq. (20), this can be written as
bBV s (a, b) = 1 N p
N p X
m=1
bF p s (s(xp m))I(s(x p m)∈[b, a]).(77)
Also,
Bs(a, b) =Exp∼pp
h
F
p
s (s(xp))I(s(x p)∈[b, a]) i .(78)
As in the case of bAs(a, b), replacingbF p s in Eq. (77) with F p s gives an error of at mostϵN p. Applying
Lemma A.4 to the positive scores gives an additional error of at most2ϵ N p. Therefore,

 bBV s (a, b)−Bs(a, b)

 ≤3ϵ N p.(79)
The diagonal terms in bBV s (a, b)are zero since
I(s(x p n)> s(xp n)) = 0.(80)
Therefore,
bBs(a, b) = N p N p −1 bBV s (a, b).(81)
Using Eq. (79), we have

 bBs(a, b)−Bs(a, b)

 ≤ N p N p −1

 bBV s (a, b)−Bs(a, b)

 + Bs(a, b) N p −1
≤3 N p
N p −1 ϵN p + 1 N p −1 ,(82)
where we used0≤B s(a, b)≤1. This proves Eq. (72).
Theorem A.6.Suppose that Assumption A.1 holds,0≤α < β <1,N p ≥2, and
∆N ≤ϵ N ,∆ N p ≤ϵ N p.(83)
Then, simultaneously for everys∈ S,

 \pAUCs(α, β)−pAUCs(α, β)

 ≤B N,N p ,(84)
where
BN,N p := 1 (β−α)(1−π)  4ϵN +  1 + 2π+ 3π N p N p −1  ϵN p + π N p −1  .(85)
18

Preprint
Proof.We decompose the estimation error as

 \pAUCs(α, β)−pAUCs(α, β)

≤

 \pAUCs(α, β)−Qs(ˆtα,s, ˆtβ,s)

+

Qs(ˆtα,s, ˆtβ,s)−Q s(tα,s, tβ,s)

 .(86)
The estimated thresholds ˆtα,s and ˆtβ,s are selected from the PU instance scores and are therefore
finite. Thus, Lemma A.5 can be applied at these data-dependent thresholds. Using Eqs. (71) and
(72), the first term in Eq. (86) is bounded by

 \pAUCs(α, β)−Qs(ˆtα,s, ˆtβ,s)

≤ 1 (β−α)(1−π)  2ϵN +ϵ N p + 3π N p N p −1 ϵN p + π N p −1  .(87)
The bound in Lemma A.5 is uniform over the finite endpointsaandb. Thus, it also holds when the
estimated thresholds and the empirical pAUC are calculated from the same instances.
For the second term, changing either endpoint of the score interval affects Eq. (58) only through
negative instances whose scores are between the original and changed endpoints. Since the pairwise
indicator is bounded by one,

Qs(ˆtα,s, ˆtβ,s)−Q s(tα,s, tβ,s)

≤ 1 β−α 

FPRs(ˆtα,s)−FPR s(tα,s)

 +

FPRs(ˆtβ,s)−FPR s(tβ,s)

 .(88)
Under Assumption A.1,FPR s(t)is continuous. Thus, for finite population thresholds,
FPRs(tγ,s) =γ.(89)
Together with the conventionFPR s(+∞) = 0whent α,s = +∞, we have
FPRs(tα,s) =α,FPR s(tβ,s) =β.(90)
Then, Theorem A.3 gives

Qs(ˆtα,s, ˆtβ,s)−Q s(tα,s, tβ,s)

≤ 1 β−α 

FPRs(ˆtα,s)−α

 +

FPRs(ˆtβ,s)−β


≤ 2ϵFPR
β−α .(91)
Combining Eqs. (87) and (91), and substituting Eq. (40), proves Eq. (84).
For a finite score-function class with|S|=M, the DKW bounds in Section A.1 and a union
bound show that the conditions of Theorem A.6 hold simultaneously with probability at least1−δ.
Therefore,
sup
s∈S

 \pAUCs(α, β)−pAUCs(α, β)

=O

1
(β−α)(1−π)
"r
log(M/δ)
N +
r
log(M/δ)
N p + 1 N p
#!
(92)
with probability at least1−δ. Thus, the empirical pAUC estimator is uniformly consistent as
N, Np → ∞. The same conclusion applies to infinite score-function classes when the correspond-
ing uniform errors in Eq. (30) converge to zero. Since the bound is uniform overs∈ S, it also
applies to a score function selected fromSusing the training data.
19

Preprint
A.4 EFFECT OFCLASS-PRIORESTIMATIONERROR
We finally analyze the effect of using an inaccurate class-prior at the population level. Leteπ∈[0,1)
be the class-prior value used in the proposed method, whileπis the true class-prior. Replacingπ
witheπin Eq. (10) gives
FPReπ,s(t) := F s(t)−eπF
p
s (t)
1−eπ .(93)
Proposition A.7.F or everys∈ Sandt∈R,
FPReπ,s(t)−FPR s(t)
= π−eπ 1−eπ [TPRs(t)−FPR s(t)].(94)
Consequently,
sup
s∈S, t∈R
|FPReπ,s(t)−FPR s(t)| ≤ϵπ, ϵ π := |eπ−π| 1−eπ .(95)
Proof.From Eq. (7),
F s(t) =πTPR s(t) + (1−π)FPR s(t).(96)
Substituting this into Eq. (93) gives
FPReπ,s(t) = (π−eπ)TPRs(t) + (1−π)FPR s(t) 1−eπ .(97)
SubtractingFPR s(t)gives Eq. (94). SinceTPR s(t),FPR s(t)∈[0,1], Eq. (95) follows.
Forb∈Randa∈R∪ {+∞}withb≤a, define
Qeπ,s(a, b) :=As(a, b)−eπBs(a, b) (β−α)(1−eπ) .(98)
Let
etγ,s := inf{t∈R: FPR eπ,s(t)≤γ}, γ∈ {α, β},(99)
where we setinf∅= +∞. Sinceα < β, every threshold satisfyingFPR eπ,s(t)≤αalso satisfies
FPReπ,s(t)≤β. Therefore,
etβ,s ≤ etα,s.(100)
Theorem A.8.Suppose that Assumption A.1 holds and0≤α < β <1. Then, for everys∈ S,

Qeπ,s(etα,s, etβ,s)−pAUC s(α, β)

≤ 3|eπ−π| (β−α)(1−eπ) .(101)
Proof.We fixs. From Proposition A.7,
sup
t∈R
|FPReπ,s(t)−FPR s(t)| ≤ϵπ.(102)
SinceFPR eπ,s(t)→1ast→ −∞andγ <1, there exists a finiteTsuch thatFPR eπ,s(t)> γ
for allt < T. Therefore, etγ,s =−∞cannot occur. Suppose first that etγ,s is finite. Since the
survival probabilities F s(t)and F
p
s (t)are right-continuous int,FPR eπ,s(t)is also right-continuous.
Therefore, from the definition of etγ,s,
FPReπ,s(etγ,s)≤γ.(103)
20

Preprint
Also, for everyt < etγ,s,
FPReπ,s(t)> γ.(104)
Together with Eq. (102), these inequalities give
FPRs(etγ,s)≤γ+ϵ π,(105)
FPRs(t)> γ−ϵ π fort < etγ,s.(106)
Assumption A.1 ensures thatFPR s(t)is continuous. Therefore, takingt↑ etγ,s in the second
inequality gives
FPRs(etγ,s)≥γ−ϵ π.(107)
Thus,

FPRs(etγ,s)−γ

 ≤ϵ π.(108)
If etγ,s = +∞, then necessarilyγ= 0. With the conventionFPR s(+∞) = 0, Eq. (108) also holds.
Therefore, Eq. (108) holds forγ∈ {α, β}.
As in the proof of Theorem A.6, Eq. (58) and the fact that the pairwise indicator is bounded by one
give

Qs(etα,s, etβ,s)−pAUC s(α, β)

≤ 1 β−α 

FPRs(etα,s)−α

 +

FPRs(etβ,s)−β


≤ 2ϵπ
β−α .(109)
Next, from Eq. (7),
As(a, b) =πBs(a, b) + (1−π)Cs(a, b),(110)
where
Cs(a, b) :=Exp∼ppExn∼pn [I(s(x p)> s(xn))I(s(x n)∈[b, a])].(111)
SubstitutingA s(a, b) =πBs(a, b) + (1−π)Cs(a, b)intoQeπ,sandQ s gives
Qeπ,s(a, b) =(π−eπ)Bs(a, b) + (1−π)Cs(a, b) (β−α)(1−eπ) ,(112)
Qs(a, b) =Cs(a, b) β−α .(113)
Therefore,
Qeπ,s(a, b)−Qs(a, b)
= π−eπ (β−α)(1−eπ) [Bs(a, b)−Cs(a, b)].(114)
SinceB s(a, b), Cs(a, b)∈[0,1],
|Qeπ,s(a, b)−Qs(a, b)| ≤ϵπ β−α .(115)
Applying Eq. (115) at
(a, b) = (etα,s, etβ,s)(116)
and combining it with Eq. (109) gives

Qeπ,s(etα,s, etβ,s)−pAUC s(α, β)

≤ 3ϵπ
β−α = 3|eπ−π| (β−α)(1−eπ) ,(117)
which proves Eq. (101).
Theorem A.8 shows that the population-level error caused by an inaccurate class-prior is controlled
by|eπ−π|/(1−eπ).
21

Preprint
Table 4: Test average pAUCs and their standard deviations withα= 0.1,β= 0.2over different
labeled positive data sizesN p = 30,50, and100. Values in bold are not statistically different at
the5%level from the best performing method in each row according to a paired t-test. ‘# Best’ row
represents the number of results of each method that are the best or comparable to it.
DataπOurs NNPU PUAUC PAUC PUpAUCh 2step
MNIST 0.10.838±0.0430.698±0.126 0.823±0.0410.839±0.048 0.839±0.0420.826±0.036
0.20.821±0.0480.776±0.063 0.800±0.046 0.776±0.0410.818±0.0500.808±0.050
FMNIST 0.1 0.958±0.021 0.795±0.011 0.955±0.0200.964±0.0190.958±0.0210.963±0.018
0.20.954±0.0240.806±0.034 0.943±0.022 0.910±0.037 0.951±0.0250.958±0.018
SVHN 0.1 0.423±0.098 0.154±0.006 0.402±0.0920.451±0.1040.377±0.092 0.410±0.097
0.2 0.360±0.104 0.154±0.007 0.353±0.0740.391±0.0850.258±0.063 0.351±0.081
CIFAR10 0.10.744±0.0630.127±0.077 0.731±0.069 0.721±0.0620.743±0.056 0.752±0.063
0.20.722±0.0710.162±0.118 0.698±0.080 0.623±0.081 0.697±0.0690.712±0.081
SUSY 0.10.647±0.0290.557±0.074 0.629±0.0350.651±0.024 0.642±0.0300.632±0.034
0.20.629±0.0380.578±0.047 0.610±0.043 0.606±0.0440.628±0.0350.617±0.040
CODRNA 0.1 0.959±0.025 0.454±0.319 0.951±0.030 0.949±0.033 0.959±0.0270.965±0.023
0.2 0.946±0.037 0.892±0.056 0.935±0.037 0.853±0.061 0.949±0.0310.959±0.028
IJCNN 0.10.792±0.1000.469±0.108 0.778±0.0860.803±0.0780.760±0.1250.811±0.086
0.2 0.730±0.136 0.636±0.0980.750±0.0940.714±0.086 0.620±0.2170.769±0.101
EPSILON 0.10.411±0.0650.177±0.0080.404±0.067 0.410±0.060 0.406±0.068 0.399±0.079
0.20.360±0.0630.184±0.0150.368±0.062 0.363±0.0480.295±0.0660.368±0.071
# Best 10 0 3 8 6 10
B EXPERIMENTALSETTINGS
For MNIST, FMNIST, SUSY , CODRNA, IJCNN, EPSILON, we used a three-layered feed-forward
neural network with ReLU activations for the classifier (score function), where each hidden layer
consisted of128units. For SVHN and CIFAR10, we used a convolutional neural network composed
of two convolutional blocks followed by a three-layer feed-forward neural network for the classifier
(score function). The first (second) convolutional block comprised a 6 (16) filter5×5convolution,
the ReLU activation, and a2×2max-pooling layer. The numbers of nodes in the two hidden
layers were120and84, and ReLU activations were used. For all comparison methods, the same
neural network architecture was used. The PU mini-batch sizesPandUwere set to50and1,000,
respectively. For all methods, we used the Adam optimizer (Kingma & Ba, 2014) with a learning
rate of10 −3. The maximum number of epochs was200. The loss with validation PU data was used
for early-stopping to mitigate overfitting. All methods were implemented using PyTorch (Paszke
et al., 2017), and all experiments were conducted on a Linux server with an Intel Xeon CPU and
A100 GPU.
C ADDITIONALEXPERIMENTALRESULTS
C.1 RESULTS WITHα= 0.1ANDβ= 0.2
Table 4 shows the test average pAUCs and their standard deviations withα= 0.1,β= 0.2. The
proposed method performed well in many cases. Compared to caseα= 0(Tables 1 and 2), PAUC
and 2step tended to perform well. We describe possible reasons for their good performance below.
These methods treat unlabeled data (or pseudo N data) whose scores fall within a certain range
defined byαandβas negatives for training. In general, unlabeled data with high scores are more
likely to be positive. Therefore, whenα= 0, such high score positive data tend to fall into the
range, making it difficult for these methods to perform strongly. In contrast, whenα >0, these
positive data in the unlabeled data are less likely to be included in the range, which can lead to
better performance. Nevertheless, the proposed method performed comparably to or better than
these methods. Note that the proposed method outperformed these methods by a large margin in the
case ofα= 0as shown in Tables 1 and 2.
C.2 RESULTS WITHπ= 0.01ANDπ= 0.3
In the main paper, we evaluated the proposed method withπ= 0.1andπ= 0.2. Here, we investi-
gated the performance of the proposed method under smaller and larger class-prior values. Table 5
shows the average test pAUCs and their standard deviations withα= 0,β= 0.2. The proposed
22

Preprint
Table 5: The results withπ= 0.01andπ= 0.3: test average pAUCs and their standard deviations
withα= 0,β= 0.2over different labeled positive data sizesN p = 30,50, and100. Values in bold
are not statistically different at the5%level from the best performing method in each row according
to a paired t-test. ‘# Best’ row represents the number of results of each method that are the best or
comparable to it.
DataπOurs NNPU PUAUC PAUC PUpAUCh 2step
MNIST 0.010.799±0.0540.338±0.009 0.768±0.055 0.794±0.0520.799±0.0530.792±0.055
FMNIST 0.01 0.949±0.021 0.731±0.112 0.945±0.021 0.947±0.022 0.949±0.0210.954±0.017
SVHN 0.010.411±0.0890.105±0.005 0.363±0.0890.410±0.089 0.412±0.0830.398±0.087
CIFAR10 0.01 0.661±0.067 0.081±0.053 0.634±0.079 0.662±0.072 0.656±0.0700.679±0.063
SUSY 0.010.571±0.0220.295±0.038 0.528±0.0410.570±0.022 0.569±0.0220.552±0.033
CODRNA 0.010.882±0.0250.124±0.031 0.875±0.0320.883±0.024 0.882±0.024 0.881±0.027
IJCNN 0.010.766±0.0700.188±0.023 0.714±0.0850.765±0.0670.763±0.070 0.753±0.077
EPSILON 0.010.353±0.0550.131±0.005 0.324±0.059 0.350±0.0520.354±0.0540.338±0.064
MNIST 0.30.688±0.0680.665±0.067 0.663±0.051 0.565±0.0610.689±0.0600.664±0.052
FMNIST 0.30.923±0.0290.824±0.070 0.883±0.042 0.747±0.0830.922±0.0290.888±0.042
SVHN 0.30.239±0.0790.105±0.0050.233±0.056 0.237±0.0450.145±0.0320.229±0.056
CIFAR10 0.30.544±0.0790.229±0.148 0.513±0.083 0.373±0.0580.522±0.0800.518±0.085
SUSY 0.30.502±0.0500.465±0.053 0.478±0.051 0.366±0.051 0.483±0.043 0.474±0.049
CODRNA 0.30.824±0.0450.804±0.050 0.802±0.060 0.623±0.0940.819±0.0530.808±0.060
IJCNN 0.30.580±0.1340.518±0.1360.593±0.0870.480±0.066 0.415±0.2260.593±0.134
EPSILON 0.3 0.231±0.054 0.180±0.0570.245±0.0440.213±0.032 0.169±0.0460.245±0.046
# Best 13 0 3 5 9 6
Table 6: The results using the logistic loss: test average pAUCs and their standard deviations with
α= 0,β= 0.2over different labeled positive data sizesN p = 30,50, and100. Values in bold
are not statistically different at the5%level from the best performing method in each row according
to a paired t-test. ‘# Best’ row represents the number of results of each method that are the best or
comparable to it.
DataπOurs PUAUC PAUC PUpAUCh 2step
MNIST 0.10.759±0.0580.727±0.047 0.743±0.057 0.752±0.055 0.732±0.048
0.20.727±0.0660.699±0.050 0.652±0.0600.719±0.0570.700±0.049
FMNIST 0.10.945±0.0230.915±0.034 0.933±0.0270.944±0.0240.929±0.029
0.20.939±0.0240.907±0.036 0.854±0.0570.936±0.0260.915±0.034
SVHN 0.10.346±0.0950.302±0.070 0.328±0.071 0.330±0.096 0.308±0.073
0.20.285±0.0910.262±0.0610.268±0.0500.227±0.069 0.259±0.062
CIFAR10 0.10.613±0.0700.592±0.072 0.552±0.078 0.602±0.0660.606±0.068
0.20.579±0.0720.559±0.079 0.452±0.0690.572±0.065 0.564±0.079
SUSY 0.10.551±0.0330.516±0.042 0.514±0.048 0.541±0.028 0.521±0.040
0.20.525±0.0440.493±0.043 0.427±0.053 0.509±0.042 0.495±0.042
CODRNA 0.10.853±0.0340.849±0.043 0.824±0.0480.854±0.035 0.856±0.038
0.20.837±0.0400.828±0.049 0.707±0.0780.839±0.039 0.834±0.047
IJCNN 0.10.712±0.0810.663±0.089 0.685±0.071 0.688±0.100 0.680±0.085
0.20.652±0.1220.628±0.092 0.572±0.069 0.595±0.1450.633±0.094
EPSILON 0.10.303±0.058 0.297±0.0550.290±0.0470.305±0.0540.295±0.056
0.20.272±0.049 0.269±0.0480.249±0.0400.258±0.054 0.269±0.055
# Best 16 2 1 8 6
method performed well. These results show that the proposed method is effective across a wide
range of class-prior values.
C.3 RESULTS USING THELOGISTICLOSS
In the main paper, we used the sigmoid function as the surrogate function in Eq. (15). Here, we
evaluated the (p)AUC-based methods including the proposed method using the logistic loss as the
surrogate function. Table 6 shows the results. The results are similar to those obtained with the
sigmoid function in Table 2, and the proposed method still outperforms the other methods. These
results suggest that the proposed method is effective with multiple surrogate functions.
C.4 RESULTS WITHDIFFERENTNUMBERS OFUNLABELEDTRAININGDATA
Figure 5 shows the average test pAUCs with their standard errors when changing the number of
unlabeled training dataN. The proposed method tended to perform better asNincreased and
consistently performed well compared to other methods across differentN.
23

Preprint
2000 4000 6000 8000
N
0.55
0.60
0.65
0.70
0.75T est pAUC
Ours
NNPU
PUAUC
PAUC
PUpAUCh
2step
(a) MNIST
2000 4000 6000 8000
N
0.80
0.85
0.90T est pAUC (b) FMNIST
2000 4000 6000 8000
N
0.10
0.15
0.20
0.25
0.30T est pAUC (c) SVHN
2000 4000 6000 8000
N
0.1
0.2
0.3
0.4
0.5
0.6T est pAUC (d) CIFAR10
2000 4000 6000 8000
N
0.44
0.46
0.48
0.50
0.52
0.54T est pAUC
(e) SUSY
2000 4000 6000 8000
N
0.4
0.5
0.6
0.7
0.8T est pAUC (f) CODRNA
2000 4000 6000 8000
N
0.3
0.4
0.5
0.6
0.7T est pAUC (g) IJCNN
2000 4000 6000 8000
N
0.15
0.20
0.25
0.30T est pAUC (h) EPSILON
Figure 5: The average test pAUCs and their standard errors withα= 0,β= 0.2over different
class-priorsπ∈ {0.1,0.2}and positive data sizesN p ∈ {30,50,100}when changing the number
of unlabeled dataN.
Table 7: Training time [sec] of each method on the MNIST and CIFAR10 datasets, where(α, β) =
(0,0.2),π= 0.2,N p = 100.
DataNOurs NNPU PUAUC PAUC PUpAUCh 2step
MNIST 5,000 90.460 90.054 90.036 90.978 89.618 184.040
CIFAR10 9,000 305.871 304.184 302.897 305.471 302.469 608.849
C.5 COMPUTATIONCOSTS
We investigated the training time of the proposed method on the MNIST and CIFAR10 datasets. We
used a Linux server with a 2.20 GHz CPU. Table 7 shows the results. Since 2step additionally learns
the classifier to create pseudo PN data, its training time was long. For the remaining methods, the
training times were all similar. This result indicates that the proposed method is sufficiently practical
in terms of the computation cost.
C.6 EVALUATION ONREAL-WORLDMEDICAL ANDADVERTISINGDATASETS
In Section 1, we presented examples from the medical and advertising domains to motivate our
problem setting. In this section, we evaluated the proposed method on Mammography (Vanschoren
et al., 2014) and Online-shoppers (Sakar et al., 2019), which are real-world medical and advertising-
related datasets, respectively.
Mammography is a dataset for detecting microcalcifications, which are treated as positives, and is
highly class-imbalanced (i.e., the positive class-prior is0.023). Due to the limited (positive) data
size, we used30and20positive data for training and validation, respectively;5,000and1,000
unlabeled data for training and validation, respectively; and3,000test data. The unlabeled and
test data were created to preserve the original class-prior value (i.e.,π= 0.023). Online-shoppers
is a dataset for predicting whether an online browsing session results in a purchase, with purchase
sessions treated as positives. The positive class-prior is0.155. This task is closely related to the
advertising scenario motivating our work: it is important to identify sessions likely to result in
purchases while maintaining a low FPR, since falsely targeting non-purchase sessions can waste
advertising resources and degrade user experience. For this dataset, we changed the positive training
data size within{30,50,100}as in the other datasets and used1,000test data. The sizes of other
datasets were the same as those for Mammography. The unlabeled data were created to preserve the
original class-prior (i.e.,π= 0.155).
Table 8 shows the results. On Mammography, the proposed method performed comparably to the
other pAUC maximization methods (PAUC, PUpAUCh, and 2step). Since this dataset has a very
24

Preprint
Table 8: The results on Mammography and Online-shoppers: test average pAUCs and their standard
deviations withα= 0,β= 0.1andα= 0,β= 0.2. Values in bold are not statistically different at
the5%level from the best performing method in each row according to a paired t-test.
DataβOurs NNPU PUAUC PAUC PUpAUCh 2step
Mammography 0.10.784±0.0410.001±0.001 0.754±0.0410.780±0.045 0.786±0.037 0.784±0.037
Mammography 0.20.821±0.0390.004±0.004 0.810±0.0320.831±0.039 0.827±0.036 0.834±0.029
Online-shoppers 0.10.329±0.0810.222±0.072 0.259±0.069 0.226±0.032 0.308±0.085 0.263±0.071
Online-shoppers 0.20.442±0.0790.331±0.079 0.371±0.073 0.386±0.063 0.425±0.079 0.379±0.073
Table 9: FPRs induced by the estimated thresholds during training.
Dataα β N p FPR Epoch 1 Epoch 10 Epoch 50 Epoch 100
FMNIST 0.0 0.1 30FPR( ˆtα)0.025 0.031 0.031 0.031
0.0 0.1 100FPR( ˆtα)0.017 0.020 0.022 0.023
0.0 0.1 30FPR( ˆtβ)0.118 0.115 0.115 0.116
0.0 0.1 100FPR( ˆtβ)0.107 0.109 0.108 0.109
0.0 0.2 30FPR( ˆtα)0.022 0.030 0.031 0.031
0.0 0.2 100FPR( ˆtα)0.013 0.021 0.021 0.022
0.0 0.2 30FPR( ˆtβ)0.217 0.208 0.208 0.208
0.0 0.2 100FPR( ˆtβ)0.210 0.204 0.200 0.200
CODRNA 0.0 0.1 30FPR( ˆtα)0.061 0.064 0.058 0.058
0.0 0.1 100FPR( ˆtα)0.027 0.033 0.044 0.046
0.0 0.1 30FPR( ˆtβ)0.140 0.138 0.129 0.130
0.0 0.1 100FPR( ˆtβ)0.114 0.115 0.113 0.115
0.0 0.2 30FPR( ˆtα)0.058 0.058 0.056 0.057
0.0 0.2 100FPR( ˆtα)0.027 0.027 0.041 0.041
0.0 0.2 30FPR( ˆtβ)0.223 0.216 0.214 0.215
0.0 0.2 100FPR( ˆtβ)0.208 0.201 0.204 0.204
small positive class-prior, treating unlabeled instances as negative introduces only limited bias, mak-
ing such approaches naturally competitive. In contrast, on Online-shoppers, the proposed method
consistently outperformed the other methods. This dataset has a larger positive class-prior, making
it more important to properly account for positive instances contained in the unlabeled data. Such
non-negligible class-priors can naturally arise when both training and test data are drawn from a can-
didate population enriched through upstream screening, filtering, or retrieval. Overall, these results
show that the proposed method is particularly effective in practically relevant settings where the un-
labeled data contain a non-negligible proportion of positive instances, while remaining competitive
even when the positive class-prior is very small.
C.7 EMPIRICALANALYSIS OFFPRSINDUCED BY THEESTIMATEDTHRESHOLDS
We tracked the FPRs with the estimated thresholds,FPR( ˆtα)andFPR( ˆtβ), during training, and
examined whether they remained close to the target valuesαandβ. 2 In this experiment, ˆtα and ˆtβ
were estimated from training PU mini-batch as described in Algorithm 1, and the FPRs induced by
the estimated thresholds were calculated on different fixed2,500negative instances.
Table 9 shows the average FPRs induced by the estimated thresholds at selected training epochs for
FMNIST and CODRNA, an image dataset and a tabular dataset, respectively. For both datasets,
FPR(ˆtβ)remained close to the target valueβthroughout training. In contrast,FPR( ˆtα)showed
larger deviations from the targetα= 0, indicating that estimating the threshold corresponding to the
extreme FPR (α= 0) is more challenging. Nevertheless, increasing the number of positive training
instances fromN p = 30toN p = 100consistently reduced the deviations from the target FPRs
for both thresholds. These results suggest that the proposed method can appropriately estimate the
target FPR region from PU data during training, and the estimation becomes more accurate as the
number of positive training data increases.
2We did not track the estimated thresholds themselves because they may change substantially when the
scale or offset of the score function changes, even when the resulting pAUC remains unchanged.
25

Preprint
Table 10: Pseudo-negative selection quality of PUpAUCh (Iwata et al., 2020) and the test pAUC gap
between Oracle and PUpAUCh. Largercindicates greater positive contamination in the selected
pseudo-negatives relative to random selection.
DatacOracle−PUpAUCh
MNIST 1.5421 0.08379
FMNIST 0.6666 0.01786
SVHN 1.5432 0.09771
CIFAR10 1.5502 0.09186
SUSY 1.1720 0.04063
CODRNA 2.2437 0.04952
IJCNN 1.6922 0.13128
EPSILON 1.5265 0.03976
C.8 EMPIRICALANALYSIS OF THEHEURISTICSCORINGASSUMPTION
The existing pAUC maximization method, PUpAUCh, trains the score function by heuristically
treating all unlabeled instances whose ranks based on their current scores fall within a specified
range as negatives (Iwata et al., 2020). Here, we evaluate the quality of these pseudo-negatives
to investigate to what extent their heuristic assumption that the selected unlabeled instances are
negative holds during training.
Specifically, we first define
e= |{x∈B:y= +1}| |B| ,(118)
whereBdenotes the set of selected pseudo-negative instances within the mini-batch unlabeled data.
Thus,erepresents the proportion of selected instances that are actually positive. If instances are
selected uniformly at random from the unlabeled data, the expected proportion of positives among
them isπ. Thus, we define
c= e π ,(119)
wherec= 1indicates that the selection is random,c <1indicates that it is better than the random
selection, andc >1indicates that it is worse than the random selection. A largercmeans a greater
violation of the PUpAUCh’s heuristic scoring assumption.
Table 10 reports the averagecduring PUpAUCh training, together with the test pAUC gap from
an oracle method that explicitly uses the true negative instances contained in the unlabeled data,
i.e., Oracle−PUpAUCh. Here, we fixedπ= 0.1,α= 0, andβ= 0.1. We first observe that
c >1for most datasets, indicating that the pseudo-negatives selected by PUpAUCh often contain
more positive instances than expected under random selection. This result empirically shows that
the heuristic scoring assumption of PUpAUCh is frequently violated during training. Moreover, we
observe a positive association betweencand the performance gap between Oracle and PUpAUCh
(Spearman’sρ= 0.714). This suggests that poorer pseudo-negative selection tends to be associated
with a larger performance degradation relative to the oracle.
26
