---
title: Learning from Double Positive and Unlabeled Data for Potential-Customer Identification
url: https://arxiv.org/abs/2506.00436
category: ai-marketing
subcategory: empirical
date: 2025-05
venue: ''
authors:
- Masahiro Kato
- Yuki Ikeda
- Kentaro Baba
- Takashi Imai
- Ryo Inokuchi
source: arxiv
pdf_url: https://arxiv.org/pdf/2506.00436
pages: 6
chars: 24387
fetched_at: '2026-11-08T13:11:31+00:00'
kb_version: 1
---

# Learning from Double Positive and Unlabeled Data for Potential-Customer Identification

arXiv:2506.00436v2  [cs.LG]  9 Jun 2025
Learning from Double Positive and Unlabeled Data
for Potential-Customer Identification
Masahiro Kato
Mizuho-DL Financial Technology
Tokyo, Japan
masahiro-kato@fintec.co.jp
Yuki Ikeda
Mizuho-DL Financial Technology
Tokyo, Japan
yuki-ikeda@fintec.co.jp
Kentaro Baba
Mizuho-DL Financial Technology
Tokyo, Japan
kentaro-baba@fintec.co.jp
Takashi Imai
Mizuho-DL Financial Technology
Tokyo, Japan
takashi-imai@fintec.co.jp
Ryo Inokuchi
Mizuho-DL Financial Technology
Tokyo, Japan
ryo-inokuchi@fintec.co.jp
Abstract—In this study, we propose a method for identifying
potential customers in targeted marketing by applying learning
from positive and unlabeled data (PU learning). We consider a
scenario in which a company sells a product and can observe
only the customers who purchased it. Decision-makers seek to
market products effectively based on whether people have loyalty
to the company. Individuals with loyalty are those who are likely
to remain interested in the company even without additional
advertising. Consequently, those loyal customers would likely
purchase from the company if they are interested in the product.
In contrast, people with lower loyalty may overlook the product
or buy similar products from other companies unless they receive
marketing attention. Therefore, by focusing marketing efforts
on individuals who are interested in the product but do not
have strong loyalty, we can achieve more efficient marketing. To
achieve this goal, we consider how to learn, from limited data, a
classifier that identifies potential customers who (i) have interest
in the product and (ii) do not have loyalty to the company.
Although our algorithm comprises a single-stage optimization,
its objective function implicitly contains two losses derived from
standard PU learning settings. For this reason, we refer to our
approach as double PU learning . We verify the validity of the
proposed algorithm through numerical experiments, confirming
that it functions appropriately for the problem at hand.
I. I NTRODUCTION
Data-driven, effective target marketing has attracted signifi-
cant attention in business. To promote product sales, we focus
on the set of potential customers defined as:
(i) people who might be interested in the product, but
(ii) do not have strong loyalty to the company.
This idea is based on the premise that loyal customers, who
already feel an attachment to the company, are likely to
purchase new products without additional advertising. On the
other hand, those lacking strong company loyalty may fail to
notice the product or choose similar products from competi-
tors, even if they are interested. By identifying and targeting
such potential customers, we aim to conduct marketing more
efficiently.
In this work, we propose a framework for classifying
individuals in a broader population to find those who meet
the above definition of potential customers. Let each person
be characterized by a feature vector X, and suppose they have
two binary labels:
Y ∈ {−1, +1} and Z ∈ {−1, +1}.
Here, Y = +1indicates the person is interested in the product,
while Z = +1indicates the person has loyalty to the company.
Conversely, Y = −1 and Z = −1 each signify the opposite of
those attributes. We define a new binary label W ∈ {−1, +1}
such that
W =
(
+1 if Y = +1and Z = −1,
−1 otherwise.
Thus, W = +1identifies people who are potential customers
(interested in the product but lacking loyalty to the company),
whereas W = −1 indicates they do not meet those conditions.
Our goal is to learn a classifier that predicts W using only
positive data and unlabeled data. More concretely, we assume
availability of three datasets:
• Positive interest data (X ∼ p(x | y = +1)): A set
of people who have shown interest in the product, for
instance by purchasing it or a similar item.
• Unlabeled data (X ∼ p(x)): A dataset of individuals for
whom the interest and loyalty labels are unknown. Only
X is observed.
• Positive loyalty data (X ∼ p(x | y = +1, z= +1)): A
set of people who have shown both interest in the product
and loyalty to the company, for instance by repeatedly
purchasing the company’s products or registering for its
services.
These datasets need not be strictly separate; some overlap
among them is permissible. Figure 1 illustrates how the interest
label Y , the loyalty label Z, and the newly defined label W
for potential customers correspond.
In many real-world scenarios, it is difficult or expensive to
obtain reliable negative labels: a lack of purchase does not
necessarily prove no interest in the product, and the absence

Fig. 1. Diagram illustrating how the interest label Y , loyalty label Z, and
potential-customer label W relate.
of a subscription or account does not directly show no loyalty
to the company. Consequently, we lack explicit negative labels.
However, standard supervised learning algorithms typically
require both positive and negative examples. Learning from
positive and unlabeled data (PU learning) is a form of weak
supervision that addresses this issue and has been employed
in domains such as information retrieval, anomaly detection,
and beyond [2, 4, 10, 12, 15, 17].
Existing PU learning algorithms enable binary classification
when only positive and unlabeled data are available. However,
our setting involves two sorts of positive labels—one indicat-
ing product interest ( Y = +1) and another indicating both
product interest and company loyalty ( Y = +1, Z= +1)—
and we aim to distinguish W = +1(potential customers) from
W = −1. Hence, a direct application of standard PU learning
methods is not sufficient.
We resolve this by extending existing PU learning tech-
niques to incorporate the positive loyalty data. Concretely, we
first define a loss function for classifying Y = +1 versus
Y = −1. Since W = +1 corresponds to Y = +1 and
Z = −1, we then adjust this loss function accordingly to
construct a single objective function for predicting W = +1
versus W = −1. Despite being optimized in one stage, our
approach effectively contains two PU learning losses: one for
identifying those with Y = +1 and another for adjusting
loyalty status ( Z = +1 versus Z = −1). Hence, we refer to
our approach as double PU learning . Details of the proposed
method are presented in Section III.
In Section IV, we report simulation results to verify the
validity of our algorithm. In Section V, we conduct an ex-
periment using real-world marketing data. These experiments
show that the proposed double PU learning classifier works as
intended for the outlined task.
II. P ROBLEM SETTING
Let X ∈ X ⊂ Rd be a feature random variable that
characterizes an individual. Each individual with X potentially
has two labels Y ∈ {−1, +1} and Z ∈ {−1, +1}. In
our setting, we can only observe labeled individuals with
Y = +1 or Z = +1 or unlabeled individuals. Given the
positive and unlabeled data, our interest lies in classifying
{Y = +1} ∧ {Z = −1} or not given X. We introduce more
detailed setting below.
A. Potential Outcomes
To deal with missing random variables, we introduce po-
tential outcomes, which are used in the literature of missing
outcomes [16] and causal inference [11, 14].
Let Y, Z∈ {−1, +1} be binary labels, and X ∈ X ⊂Rd
be a d-dimensional feature vector with a feature space X . We
suppose that the triple (Y, Z, X) is generated as follows:
(Y, Z, X) ∼ p(y, z, x).
In this study, we consider a situation where there are two
different labels Y and Z in each object whose feature is
represented by X. Specifically, in our application, we consider
the following situation.
a) Example:: Each object is a customer whose feature
is summarized as X, such as its age. For the customer, Y
corresponds to an actual outcome of advertisement; that is,
the customer bought a product or not after an advertisement
is treated. Here, Z corresponds to a loyalty of the customer,
which represents that the customer likes the brand or not. If
the labels are Y = +1 and Z = +1, the customer likes the
brand and bought its product as a result of advertisement. If
the labels are Y = +1 and Z = −1, the customer is not
interested in the brand but bought its product.
B. Observed Data
This study assumes that we can observe the following three
datasets, which are generated from p

x | y = +1

, p

x

, and
p

x | (y, z) = (+1, +1)

, respectively:
Dy=+1 :=  Xj 	J j=1 i.i.d ∼ p  x | y = +1  ,
DU :=  Xk 	K k=1 i.i.d ∼ p  x  ,
D(y,z)=(+1,+1) :=  Xl 	L l=1 i.i.d ∼ p  x | (y, z) = (+1, +1)  .
Here, we defined D(y,z)=(+1,+1) as a dataset independent of
Dy=+1. However, D(y,z)=(+1,+1) can be observed as a subset
of Dy=+1; that is, D(y,z)=(+1,+1) ⊂ Dy=+1.
This setting is a variant of case-control PU learning [13],
which has been adopted by [3], [8], and [6]. Another frame-
work, known as censoring PU learning, has been used in
earlier studies such as [4] and [1]. Although case-control PU
learning accommodates a more general setting than censoring
PU learning, it requires additional information to train a
classifier.
C. Classification Risk and Optimal Classifiers
Our interest lies in classifying (Y, Z) = (+1 , −1) and
not (Y, Z) = (+1 , −1) given X (Figure 2); that is, we
define positive label W = +1 as (Y, Z) = (+1, −1) and
negative label W = −1 as

(Y, Z) = (+1, +1)

∪

(Y, Z) =
(−1, +1)

∪

(Y, Z) = (−1, −1)

:
positive :W = +1 if (Y, Z) = (+1, −1),
negative :W = −1 otherwise.
Here, we note that because we cannot observe which obser-
vations are labeled Y = −1 or Z = −1. Figure 2 shows

the quadrants divided by these labels. The upper left quadrant
represents W = +1, and the other quadrants are W = −1.
Fig. 2. Quadrants divided by Y and Z. The upper left quadrant represents
W = +1, and the other quadrants are W = −1.
a) Classification risk.: Let g : X →R be a classifier and
G be some set of g. Let EW =+1 and EW =−1 be expectations
over p

x | w = +1

= p

x | (y, z) = (+1, −1)

(density
of X conditioned on a positive label) and p

x | w = −1

=
p

x | (y, z) = (+1, +1)∨(−1, +1)∨(−1, −1)

(density of X
conditioned on a negative label). Then, we define an optimal
classifier as
g∗ = arg min
g∈G
R0-1(g),
where R0-1(g) is the expected misclassification rate when
the classifier g(X) is applied to marginal (unlabeled) feature
distribution p(x), defined as
R0-1(g) =αEW =+1

ℓ0-1(g(X))

+ (1− α)EW =−1

ℓ0-1(−g(X))

,
where ℓ0-1(z) = 1 2 sgn(−z) +1 2 is the zero-one loss and α =
p(w = +1) =p

y = +1, z= −1

is called the class-prior.
We also define β = p(y = +1) and γ = p(y = +1, z= +1)
and assume that β and γ are known.
III. D OUBLE PU L EARNING
This section provides our algorithm. First, we discuss an
unbiased risk for R0-1(g) in Section III-B. Next, we define
empirical risk minimization in Section III-C.
A. Identification
If we have data sampled from p(x | w = +1) and
p(x | w = −1), we can directly construct R0-1(g) =
αEW =+1

ℓ0-1(g(X))

+ (1− α)EW =−1

ℓ0-1(−g(X))

. How-
ever, since we do not assume the access to the data, we
consider another approach.
Here, we discuss how we identify R0-1(g) from observa-
tions. For a function h : X →R, we define the expected value
of h(X) over p(x | y = +1), p(x), and p(x | y = +1, z=
+1) as Ey=+1[h(X)], EU [h(X)], and Ey=+1,z=+1[h(X)],
respectively. Then, we write R0-1(g) using Ey=+1[h(X)],
EU [h(X)], and Ey=+1,z=+1[h(X)] as follows:
Lemma 1. We have
R0-1(g) =βEY =+1

ℓ0-1(g(X))

− γE(Y,Z )=(+1,+1)

ℓ0-1(g(X))

+ EU

ℓ0-1(−g(X))

− βEY =+1

ℓ0-1(−g(X))

+ γE(Y,Z )=(+1,+1)

ℓ0-1(−g(X))

,
where β := p(y = +1)and γ := p(y = +1, z= +1).
Proof. We have
R0-1(g) =αEW =+1

ℓ0-1(g(X))

+ (1− α)EW =−1

ℓ0-1(−g(X))

= αEW =+1

ℓ0-1(g(X))

+ EU

ℓ0-1(−g(X))

− αEW =+1

ℓ0-1(−g(X))

= βEY =+1

ℓ0-1(g(X))

− γE(Y,Z )=(+1,+1)

ℓ0-1(g(X))

+ EU

ℓ0-1(−g(X))

− βEY =+1

ℓ0-1(−g(X))

+ γE(Y,Z )=(+1,+1)

ℓ0-1(−g(X))

.
Here, we used
αp(x | w = +1) =p(x, w= +1) =p(x, y= +1, z= −1)
= p(x, y= +1)− p(x, y= +1, z= +1)
= βp(x | y = +1)− γp(x | y = +1, z= +1).
B. Unbiased Risk
Thus, we obtain an equivalent formulation of R0-1(g) using
EY =+1[h(X)], EU [h(X)], and E(Y,Z )=(+1,+1)[h(X)]. This
section presents an unbiased risk for R0-1(g) with replacing
its zero-one loss with a surrogate loss.
a) Sample approximation: For h : X → R, we de-
fine sample approximations of EY =+1[h(X)], EU [h(X)], and
E(Y,Z )=(+1,+1)[h(X)] as
bEY =+1[h(X)] = 1 J
JX
j=1
h(Xj),
bEU [g(X)] = 1 K
KX
k=1
h(Xk),
bE(Y,Z )=(+1,+1)[h(X)] = 1 L
LX
l=1
h(Xl).
b) Unbiased empirical risk.: Then, an unbiased risk is
given as
bR0-1(g) := β bEY =+1
h
ℓ0-1

g(X)
i
− γ bE(Y,Z )=(+1,+1)
h
ℓ0-1

g(X)
i
+ bEU
h
ℓ0-1

− g(X)
i
− β bEY =+1
h
ℓ0-1

− g(X)
i
+ γ bE(Y,Z )=(+1,+1)
h
ℓ0-1

− g(X)
i
.
Here, it holds that E
 bR0-1(g)  = R0-1(g).

TABLE I
SURROGATE LOSS ℓ : Z →R+.
Loss name ℓ(z) Z
Squared loss (z − 1)2 R
Log loss − log(z) (0, 1)
Logistic loss log

1 + exp(−z)

R
Hinge loss max

0, 1 − z

R
C. Empirical Risk Minimization
We replace the zero-one loss ℓ0-1(z) with a surrogate loss
ℓ : R →R.
a) Surrogate loss.: Since it is not easy to optimize the
zero-one loss ℓ0-1 directly, we replace it with a surrogate loss,
including the log-loss and hinge loss. Let us denote a surrogate
loss by ℓ : R →R. We raise candidates of a surrogate loss
in Table I. From the computational perspective, the use of
surrogate losses with convexity is preferable. However, there
are applications where non-convex surrogate losses perform
well. Using a surrogate loss ℓ, we define the population risk
as
R(g) =αEW =+1

ℓ(g(X))

+ (1− α)EW =−1

ℓ(−g(X))

.
b) Empirical risk minimization.: We train g as
bg = arg min
g∈G
bR(g), (1)
where
bR(g) := β bEY =+1
h
ℓ

g(X)
i
+ bEU
h
ℓ

− g(X)
i
− β bEY =+1
h
ℓ

− g(X)
i
− γ bE(Y,Z )=(+1,+1)
h
ℓ

g(X)
i
+ γ bE(Y,Z )=(+1,+1)
h
ℓ

− g(X)
i
.
We refer to an algorithm that trains a binary classifier by (1)
as double PU learning, since this objective function essentially
consists of two PU learning risks as explained in the following
section.
D. Intuition behind our Algorithm
We can decompose bR(g) as
bR(g) = bRPU(g) − γ bE(Y,Z )=(+1,+1)
h
ℓ

g(X)
i
+ γ bE(Y,Z )=(+1,+1)
h
ℓ

− g(X)
i
,
where bRPU(g) is the standard PU learning risk defined as
bRPU(g) := β bEY =+1
h
ℓ

g(X)
i
+ bEU
h
ℓ

− g(X)
i
− β bEY =+1
h
ℓ

− g(X)
i
.
a) Unbiased PU risk.: The part bRPU(g) corresponds to
an unbiased PU risk for classifying Y = +1 and Y = −1.
By minimizing bRPU(g), we can train a classifier that classifies
individuals into Y = +1and Y = −1. Figure 3 illustrates this
classification, where the blue part corresponds to Y = +1and
the remaining part corresponds to Y = −1.
Fig. 3. The standard PU classification.
b) Unbiased double PU risk.: The blue region in Fig-
ure 3 includes (Y, Z) = (+1, +1) in addition to (Y, Z) =
(+1, −1) (W = +1). We aim to remove this region. This
step can be interpreted as the second PU classification, since
we minimize another empirical risk by regarding Y = +1as
unlabeled data and (Y, Z) = (+1, +1) as labeled data. As
a result, we obtain a classifier that classifies individuals into
W = +1and W = −1. In Figure 4, the blue part corresponds
to W = +1and the remaining part corresponds to W = −1.
Fig. 4. The double PU classification.
Thus, our double PU learning algorithm trains a classifier
for identifying potential customers by minimizing the unbiased
empirical risk. This unbiasedness is important because it guar-
antees finite-sample stability of the learning process. In our
setting, obtaining an unbiased risk estimator is not obvious, as
the sampling scheme is non-standard in binary classification.
E. Non-negative risk correction.
When the hypothesis class G is highly complex—such as
when it includes neural networks—empirical risk minimiza-
tion in PU learning often breaks down [8]. The problem
stems from the negative term in the risk expression, which
can diverge to negative infinity during training, a phenomenon
referred to as train-loss hacking in [5]. To address this issue,
[8] introduced the non-negative risk correction, and the same
correction can be applied to double PU learning . This adjust-
ment has been shown to enhance training stability. One way

of the correction is
bR(g) := β bEY =+1
h
ℓ

g(X)
i
+ max
n
0, bEU
h
ℓ

− g(X)
i
− β bEY =+1
h
ℓ

− g(X)
io
− γ bE(Y,Z )=(+1,+1)
h
ℓ

g(X)
i
+ γ bE(Y,Z )=(+1,+1)
h
ℓ

− g(X)
i
.
F . Cost-sensitive learning.
In many real applications, dataset is imbalanced in terms
of class distribution, and cost-sensitive learning is one way
to cope with this problem. Double-PU learning can be trans-
formed to cost-sensitive setting. Slightly modifying the deriva-
tion of Lemma 1, we suggest
bR(g) := cF N

β bEY =+1
h
ℓ

g(X)
i
− γ bE(Y,Z )=(+1,+1)
h
ℓ

g(X)
i
+ cF P

bEU
h
ℓ

− g(X)
i
− β bEY =+1
h
ℓ

− g(X)
i
+ γ bE(Y,Z )=(+1,+1)
h
ℓ

− g(X)
i
,
where cF Nand cF P are the costs of false negative and false
positive respectively.
IV. S IMULATION STUDIES
To verify the proposed algorithm we generated 500 positive
samples with label (Y, Z) = (+1 , −1) and 1000 negative
samples with labels (Y, Z) = (+1 , +1) and (Y, Z) =
(−1, −1), respectively, from bivariate Gaussian distributions
(Figure 5). Using 70% of the positive samples as labeled
data, we randomized 30% of both (Y, Z) = (+1, −1) and
(Y, Z) = (+1, +1) to unlabeled for Y , and further randomized
50% of (Y, Z) = (+1, +1) to unlabeled for Z. Samples with
Y = −1 were fully unlabeled for both Y and Z. With (x1, x2)
as features we trained a logistic-loss classifier. The learned
decision boundary p(w = +1| x) = 0.5 is shown in Figure 5,
demonstrating that double PU learning successfully separates
potential customers despite partial labeling.
V. A PPLICATION TO MARKETING
We applied our method to bank marketing dataset 1 origi-
nally from UCI machine learning repository. There are 11,162
samples total with 15 features. We want to predict customers
who are likely to accept a marketing offer but not likely to
default. In order to do so, we defined Y = +1 if a customer
accepted a marketing offer and Z = +1 if the customer is
in default. We want to find customers of W = +1 (Y = +1
but Z = −1). Note that this situation is different from the
main motivation of this paper (finding a customer who have
shown interest and low loyalty), but this setting also aligns
with double-PU learning, because a bank often does not know
a customer defaults unless the bank itself offers a loan to the
1https://www.kaggle.com/datasets/janiobachmann/bank-marketing-
dataset/data
Fig. 5. Results of the numerical experiment.
customer. We first divided the original dataset into training
and test dataset by 80% and 20%. Next, we further divided
the training dataset into three datasets where the first one (10%
of total) used only samples with Y = +1 (corresponding
to Dy=+1), the second one (10% of total) used all samples
(corresponding to DU ) and the third one (80% of total) used
only samples with Y = +1 and Z = +1 (corresponding to
D(y,z)=(+1,+1)). We applied double-PU learning to these three
datasets. We set β = 0.4738 and γ = 0.0046 and employed a
linear classifier for g. Also, since a customer default can result
in a significant cost, we assigned a cost to false positives that is
100 times higher than the cost of false negatives for predicting
W using the cost-sensitive learning explained above. As a
result of the experiment, ROC-AUC of the learned classifier
on the test dataset is 0.6013, implying that it can predict better
than the random classifier.
VI. R ELATED WORK
PU learning has also been investigated in statistics and
economics [9]. In the machine-learning literature, [4] proposed
a practical algorithm for PU learning, and [3] later introduced
another practical approach, known as unbiased PU learning.
We assumed the class priors β and γ are known, but this is
often not the case in real applications. While the class prior can
be estimated under certain conditions [7], doing so introduces
extra assumptions.
Two main data-generation mechanisms are considered in PU
learning: censoring PU learning and case-control PU learning
(see Section II-B). The setting analyzed by [4] falls under
censoring PU learning, whereas those in [9] and [3] correspond
to case-control PU learning. In case-control PU learning,
positive instances are gathered independently of the unlabeled
sample. In contrast, in censoring PU learning, a single sample
is drawn first, after which only a subset of its positive instances

is revealed. Due to this property, censoring PU learning is also
called the one-sample scenario, while case-control PU learning
is also called the two-sample scenario.
Our problem setting is a variant of case-control PU learning,
but it can also be formulated within the censoring PU learning
framework. Although the case-control setting is slightly more
general, it requires knowledge of the class prior to train the
classifier. As a result, censoring PU learning algorithms are
sometimes viewed as more practical. Note that our algorithm
is directly applicable to the censoring PU setting 2.
VII. C ONCLUSION
In this study, we proposed the double PU learning approach
for targeted marketing. Our focus was on identifying potential
customers who are interested in a product but do not have
loyalty to the company. We proposed an algorithm for training
a binary classifier in this task, despite limited data availability,
referred to as the double PU learning. We confirmed the
soundness of the proposed algorithm via simulated studies.
REFERENCES
[1] Jessa Bekker and Jesse Davis. Learning from positive and
unlabeled data under the selected at random assumption.
In Proceedings of the Second International Workshop
on Learning with Imbalanced Domains: Theory and
Applications, volume 94, pages 8–22, 2018.
[2] Gilles Blanchard, Gyemin Lee, and Clayton Scott. Semi-
supervised novelty detection. Journal of Machine Learn-
ing Research, 11(Nov):2973–3009, 2010.
[3] Marthinus Christoffel du Plessis, Gang. Niu, and Masashi
Sugiyama. Convex formulation for learning from positive
and unlabeled data. In ICML, pages 1386–1394, 2015.
[4] Charles Elkan and Keith Noto. Learning classifiers from
only positive and unlabeled data. In KDD, pages 213–
220, 2008.
[5] Masahiro Kato and Takeshi Teshima. Non-negative
bregman divergence minimization for deep direct density
ratio estimation. In ICLR, volume 139, pages 5320–5333,
2021.
[6] Masahiro Kato, Takeshi Teshima, and Junya Honda.
Learning from positive and unlabeled data with a selec-
tion bias. In ICLR, 2019.
[7] Masahiro Kato, Liyuan Xu, Gang Niu, and Masashi
Sugiyama. Alternate estimation of a classifier and the
class-prior from positive and unlabeled data, 2018. arXiv:
1809.05710.
[8] Ryuichi Kiryo, Gang Niu, Marthinus Christoffel
du Plessis, and Masashi Sugiyama. Positive-unlabeled
learning with non-negative risk estimator. In NeurIPS,
pages 1675–1685, 2017.
[9] Tony Lancaster and Guido Imbens. Case-control studies
with contaminated controls. Journal of Econometrics ,
71(1):145–160, 1996.
2As [13] discusses, most case-control PU algorithm can be applied to
censoring PU learning setting when the class prior is known
[10] Xiao-Li Li, Philip S Yu, Bing Liu, and See-Kiong Ng.
Positive unlabeled learning for data stream classification.
In SDM, pages 259–270, 2009.
[11] Jerzy Neyman. Sur les applications de la theorie
des probabilites aux experiences agricoles: Essai des
principes. Statistical Science, 5:463–472, 1923.
[12] Minh Nhut Nguyen, Xiaoli-Li Li, and See-Kiong Ng.
Positive unlabeled leaning for time series classification.
In IJCAI, pages 1421–1426, 2011.
[13] Gang Niu, Marthinus Christoffel du Plessis, Tomoya
Sakai, Yao Ma, and Masashi Sugiyama. Theoretical com-
parisons of positive-unlabeled learning against positive-
negative learning. In NeurIPS, volume 29, 2016.
[14] D.B. Rubin. Estimating causal effects of treatments
in randomized and nonrandomized studies. Journal of
Educational Psychology, 66(5):688–701, 1974.
[15] Clayton Scott and Gilles Blanchard. Novelty detection:
Unlabeled data definitely help. In AISTATS, pages 464–
471, 2009.
[16] A.W. van der Vaart. Asymptotic Statistics . Cambridge
Series in Statistical and Probabilistic Mathematics. Cam-
bridge University Press, 1998.
[17] Gill Ward, Trevor Hastie, Simon Barry, Jane Elith, and
John R Leathwick. Presence-only data and the em
algorithm. Biometrics, 65(2):554–563, 2009.
