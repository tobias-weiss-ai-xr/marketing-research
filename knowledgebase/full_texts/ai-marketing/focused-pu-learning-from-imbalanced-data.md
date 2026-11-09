---
title: Focused PU learning from imbalanced data
url: https://arxiv.org/abs/2605.14467
category: ai-marketing
subcategory: measurement
date: 2026-05
venue: ''
authors:
- Elias Zavitsanos
- Georgios Paliouras
source: arxiv
pdf_url: https://arxiv.org/pdf/2605.14467
pages: 31
chars: 81239
fetched_at: '2026-11-08T13:26:44+00:00'
kb_version: 1
---

# Focused PU learning from imbalanced data

Focused PU learning from imbalanced data
Elias Zavitsanos1* and Georgios Paliouras1
1*Institute of Informatics and Telecommunications, NCSR
“Demokritos”, Patriarhou Gregoriou E and 27 Neapoleos St., Agia
Paraskevi, 15310, Attica, Greece.
*Corresponding author(s). E-mail(s): izavits@iit.demokritos.gr;
Contributing authors: paliourg@iit.demokritos.gr;
Abstract
We propose a new method of learning from positive and unlabeled (PU) examples
in highly imbalanced datasets. Many real-world problems, such as disease gene
identification, targeted marketing, fraud detection, and recommender systems,
are hard to address with machine learning methods, due to limited labeled data.
Often, training data comprises positive and unlabeled instances, the latter typi-
cally being dominated by negative, but including also several positive instances.
While PU learning is well-studied, few methods address imbalanced settings or
hard-to-detect positive examples that resemble negative ones. Our approach uses
a focused empirical risk estimator, incorporating both positive and unlabeled
examples to train binary classifiers. Empirical evaluations demonstrate state-of-
the-art performance on imbalanced datasets under two labeling mechanisms -
selecting positives completely at random (SCAR) and selecting at random (SAR).
Beyond these controlled experiments, we demonstrate the value of the proposed
method in the real-world application of financial misstatement detection.
Keywords:PU learning, Imbalanced classification, Weakly supervised learning,
Learning with noisy labels
1 Introduction
In machine learning, classification tasks involve identifying instances that belong to
one or more distinct classes. Binary classification, in particular, aims at a classifier that
separates positive and negative instances, also known as positive-negative (PN) classi-
fication. This task is among the most widely studied problems in machine learning. A
1
arXiv:2605.14467v2  [cs.LG]  21 Sep 2026

PN machine learning algorithm typically has access to a fully labeled training dataset
that consists of representative positive and negative examples. However, there are cases
where the training data contain labeled examples of only the positive class, accompa-
nied by a large pool of unlabeled examples. This is known as the positive-unlabeled
(PU) learning setting. The assumption is that unlabeled data contain examples from
both the positive and the negative class, and the task is the same as binary classifica-
tion; namely, the algorithm needs to learn to separate positive from negative examples.
This setting poses significant hurdles for traditional supervised learning algorithms,
which rely heavily on labeled data to establish a clear distinction between classes.
PU learning has gained much attention in various practical scenarios since positive
and unlabeled data arise naturally for several reasons [1–3]. For instance, in medical
diagnosis, it may be impractical to label all patients as either healthy or diseased [4, 5].
Moreover, in fraud detection, the labels are usually sparse, since the corresponding
authority may delay the investigation of all possible cases, due to time and resource
limitations [6–9]. The above are illustrative examples where PU learning is required.
However, many more real-world applications require learning from PU data, such as
under-reporting (e.g., survey data), recommender systems, disease gene identification,
targeted advertising, and more [10–14].
Although PU learning has been widely studied in the literature [3], most of the work
assumes that the labeled examples are selected completely at random from the positive
examples and that the underlying distribution of positive and negative examples is
mostly balanced. Such assumptions simplify the problem and allow PU learning to
be addressed as a binary classification task with slight modifications. However, the
simplifying assumptions do not hold in many practical applications. In particular,
class imbalance naturally arises for several reasons, resulting in a biased subset of
labeled examples that are not selected completely at random. Class imbalance can be
an intrinsic property of the data or result from limitations to obtain labeled data, such
as cost, privacy, and significant human effort. There is evidence that if both classes
are well represented and come from non-overlapping distributions, it is possible to
obtain good results regardless of class disproportion [15, 16]. If, on the other hand, the
positive class is under-represented and overlaps with the negative one, class imbalance
becomes more of a challenge in the PU learning setting.
This paper proposes a new PU learning method, relaxing the traditional assump-
tions as much as possible. We derive a new risk estimator that incorporates both
the positive and the unlabeled examples in the learning process, focusing on the few
positive examples that are hard to separate from the negative ones. This approach
elegantly supports end-to-end training of binary classifiers without manipulating the
original data. We compare the proposed approach with other state-of-the-art methods
using 14 publicly available datasets and we also experiment with the real-world task
of financial misstatement detection where PU data naturally arises. The experiments
provide evidence that the proposed method achieves state-of-the-art results.
The rest of the paper is structured as follows. Section 2 provides an overview of the
background in PU learning and the related work. Section 3 presents the steps for deriv-
ing the new risk estimator. In section 4, we describe the experimental setup and the
datasets, while section 5 presents the empirical results. In Section 6, we demonstrate
2

the performance of the method in the real-world application of financial misstatement
detection, and finally, in Section 7, we conclude the paper and suggest future research
directions.
2 Background and related work
This section provides preliminary information regarding PU learning and its relation
to other types of learning. Then, we present an overview of PU learning approaches,
based on a commonly used categorization schema.
2.1 Preliminaries
Being a specialization of binary classification, PU learning inherits the assumptions
usually made to enable machine learning, such as that the samples are identically
and independently distributed and constitute a representative sample of the real pop-
ulation. Moreover, being a variant of weak supervision, but a distinct setting from
semi-supervision, it may also inherit related assumptions, such as the smoothness
assumption, the cluster assumption, and the manifold assumption. The first assumes
that examples close to each other in the feature space are more likely to share the
same label. The cluster assumption is a specialization of the smoothness assumption
and hypothesizes that the data tend to form discrete clusters. Therefore, data points
in the same cluster are more likely to share the same label. The manifold assumption
states that the data lie on a manifold of a lower dimension than that of the original fea-
ture space and enables the application of distance-based and density-based methods
defined on that manifold for learning classifiers.
Additional assumptions can be made regarding the observation of the labeled exam-
ples and the underlying labeling mechanism. Most PU learning methods are based
on the Selected Completely At Random (SCAR) assumption, which assumes that the
(positive) labeled examples constitute a randomly selected subset of the pool of pos-
itives, and each positive example has the same probability of being selected to be
labeled [17]. This is a strong assumption and is usually not realistic in practice. A more
realistic assumption is the Selected At Random (SAR) [18] one. In SAR, we assume
that the labeled examples are a biased sample from the positive distribution, where
the selection bias depends on the feature vector representation of the data points. SAR
is a loose assumption for most PU learning applications and can be specialized in the
case of the Probabilistic Gap (PG) assumption, which states that positive examples
that resemble negative ones are less likely to be labeled. In this work, we evaluate the
proposed method using both the SCAR and SAR assumptions.
2.2 PU learning
The majority of related work in PU learning can be categorized into three main
approaches: two-step methods, biased learning techniques, and class-prior-based
methods [3].
Two-step methods: Methods in this category usually rely on the smoothness and
clustering assumptions [3], i.e., they assume that data points of different classes ideally
3

occupy different regions in the feature space. Two-step methods typically identify the
most reliable negatives in the unlabeled data at the first step, and then they train an
algorithm from the newly labeled data. During this step, additional positive examples
may also be identified and labeled [19]. Then, by usually considering only the labeled
examples, a classifier can be trained in a supervised way.
Early attempts in the field used “spy” techniques [20] by turning some labeled
examples into spies and placing them into the unlabeled set. Then, a simple classifier,
usually Naive Bayes (NB) or Support Vector Machine (SVM), is trained by treating
the unlabeled examples as negative and assuming that the reliable negatives are those
whose posterior probability is lower than that of the spies. Then, the Expectation-
Maximization algorithm is used for the final classification. Other similar methods that
perform identification of negative examples or even augmentation of the positive set
and then supervised classifier training have been presented in [21–23]. In addition,
there are methods that iteratively try to learn a classifier from PU data. The first such
approach was the 1-DNF method [24, 25] that aimed to identify positive examples
based on “strong” positive features in the corresponding vector representation. Then
an incremental SVM was used to learn the classifier. Improvements of this approach
include the work proposed in [26], while other variations use an iterative SVM and
Rocchio classification to build prototype vectors for the labeled and the unlabeled
examples [27, 28]. Other two-step methods exploit clustering to identify negatives in
the unlabeled set [11, 13, 14]. The idea here is that reliable negative examples are
selected from the clusters that are further away from the positive clusters [29].
A common limitation of these approaches is their dependence on a sufficient set of
labeled examples, in order to perform the first step, i.e., to select a good set of spies,
to choose strong positive features, to successfully apply the Rocchio principles [30],
or to properly form separable clusters in the feature space. This limitation makes it
difficult for these techniques to be used in settings with class imbalance, where the
labeled set comprises very few positive examples.
To deal with the above limitation, the first step can be viewed as an anomaly
detection step, and related techniques can be used to identify reliable negatives or
positives from the unlabeled set. An initial approach [22] focused on cases where
very few negative examples were expected in the unlabeled data. Unfortunately, that
setting does not align well with the common class imbalance situation, where the class
of interest is the positive one. A more interesting recent approach proposes a method
that relies on a modification of the Isolation Forest outlier detection method to find
unreliable negatives and either label them as positive or ignore them and transform
the problem into a supervised learning setting [31].
Biased learning: Techniques in this category rely on the negativity assumption,
meaning that they treat unlabeled data as negative with label noise. In this category,
work based on a biased SVM has been proposed to penalize misclassified examples
differently, depending on whether they are truly positive or negative [32]. A direct
extension relies on multiple iterations of the biased SVM, in order for misclassified
examples to receive extra penalty [33]. Another modification assigns a weight to each
example in the unlabeled set, on top of the misclassification penalty, indicating the
likelihood of this example being negative [34]. Similarly, the weighted logistic regression
4

used in [35] favors correct positive classification over correct negative classification by
using different weights.
Bagging techniques have also been proposed in this direction, mainly to deal with
the bias towards the negative class and to address the fictitious higher importance
that may be given to noisy negative examples. The work in [36], for instance, uses
bagging SVM to learn multiple classifiers trained on labeled examples and subsets of
the unlabeled examples, and an extension is presented in [4]. Other work that is also
based on SVMs incorporates additional regularization terms and favors examples that
are close to each other and have the same label [37–39].
A parallel line of research develops foundation models for tabular data, such as
those used most often in the PU learning literature. Most prominently, TabPFN [40]
is a transformer that performs in-context learning over a labeled support set and
approximates the Bayesian posterior-predictive distribution in a single forward pass.
Such models target the fully supervised positive–negative setting and expose no notion
of unlabeled data. Therefore, applying them to PU problems requires treating the
unlabeled pool as negative.
Incorporation of class prior: Methods that rely on the class prior to either
modify the risk estimators or the prediction of the learned model assume that the
class prior is known or it can be estimated from data [41–44]. Early work in this
direction has proposed duplicating all the unlabeled examples in the training set to
count them as partially positive and negative based on the class prior probabilities
[17]. More recent approaches propose modifications to the learning algorithm, using
risk minimizers that estimate the misclassification cost for both the positive and the
unlabeled examples. Such modifications of the loss function of the algorithm have
led to the direct adaptation of several learning algorithms such as logistic regression
[41, 45, 46] and neural networks [47] for learning with PU data. These methods are
considered state-of-the-art solutions to PU learning. However, they typically cannot
handle cases with significant class imbalance and the challenges that it poses. One
exception to this norm is the work in [48], where a non-negative risk estimation for PU
learning (nnPU) was proposed, building on the work in [46] and [47], and assuming
that oversampling of positive examples is helpful in imbalanced scenarios.
The incorporation of the class prior has also been exploited in recent work [49]
that introduces the PU Hellinger Decision Tree (PUHDT) and the PU Hellinger Ran-
dom Forest (PUHRF). PUHDT is specifically designed for learning from imbalanced
PU datasets under the SCAR assumption, without requiring resampling or misclassi-
fication costs. It adapts the traditional Hellinger distance-based splitting criterion to
handle PU settings, which provides robustness to class imbalance. PUHRF extends
PUHDT, by incorporating it as a base learner in an ensemble framework, using a
stratified bootstrap sampling to ensure that all labeled positive examples are included
in the training data. The above methods rely on SCAR to estimate the number of
positive examples in unlabeled data nodes. Under the SAR or PG assumption, this
estimation becomes biased and unreliable, leading to inaccurate splits and decisions
in the tree. Therefore, PUHDT and PUHRF are tailored to model PU data under the
SCAR assumption only.
5

The family of the nnPU risk estimators provides elegant PU learning methods
that do not rely on data manipulation and preprocessing. Moreover, it offers a way
to experiment with appropriate loss functions that can help with class imbalance and
deal with hard-to-classify examples. In this work, we adopt this approach to derive a
risk estimator, based on imbalanced PU data. The new estimator focuses on the few
positive examples that are difficult to distinguish because of the Probabilistic Gap
assumption. Such methods provide flexibility because they can be incorporated into
neural networks and can be easily extended to semi-supervised settings beyond PU.
3 Method
3.1 Background and notation
The work of du Plessis et al. [43, 45, 46] and the related theoretical analysis [50]
proposed unbiased risk estimators for PU classification (uPU), by utilizing unlabeled
data for risk evaluation. The implication is that label information can be extracted
from unlabeled data, without regularization or other restrictive assumptions. Together
with the extension to non-negative risk estimators (nnPU) in [47], and the work in
[48], they revolutionized the field of PU learning.
The above work has shown that in a PU setting, where negative examples are
not available, the corresponding empirical risk can be approximated indirectly. The
derivation of the PU risk estimator is briefly described as follows. Letx∈R d andy=
{+1,−1}, wheredis a positive integer, be the input and output variables respectively
with probability densityp(x, y). In a PN classification setting fromxtoy, let us
consider two sets of samples, namely the positive (P) and the negative (N):
XP :={x P i }nP i=1 iid ∼p P (x) :=p(x|y= +1),
XN :={x N i }nN i=1 iid ∼p N (x) :=p(x|y=−1)
Also,π P :=p(y= +1) andπ N :=p(y=−1) are the class prior probabilities for
the positive and negative classes such thatπ P +π N = 1.
Letg:R d →Rbe a decision function for PN classification. Ifℓ:R× {±1} →R
is a continuous surrogate loss function, then the partial risks of the classifiergunder
lossℓare:
R+ P (g) :=E P [ℓ(g(x),+1)] =E P [ℓ(g(x))],
R− N (g) :=E N [ℓ(g(x),−1)] =E N [ℓ(−g(x))]
whereE P andE N denote the expectations overp P (x) andp N (x) respectively.
In standard PN classification, where fully labeled training data are available, the
goal is to minimize the risk ofgwith respect toℓunderp(x, y), which is defined as:
R(g) :=E (x,y)[ℓ(g(x), y)] (1)
6

and can be approximated directly from data by:
˜RP N(g) =π P ˜R+ P (g) +π N ˜R− N (g)
=π P ˜R+ P (g) + (1−π P ) ˜R− N (g), (2)
where:
˜R+ P (g) = 1 nP
nPX
i=1
ℓ(g(xP i )),
˜R− N (g) = 1 nN
nNX
i=1
ℓ(−g(xN i ))
By minimizing ˜RP N(g) we obtain the ordinary empirical risk minimizer ˜gP N.
On the other hand, in PU learningX N is not available, thusR − N (g) cannot be
directly estimated. Instead ofX N , we have access to an unlabeled set (U):
XU :={x U i }nU i=1 iid ∼p(x) :=π P ×p P (x) +π N ×p N (x)
However, it has been shown [46] that we can estimateR(g) without any bias by
replacing the second term of Eq. 2. This can be done by exploiting the fact that
p(x) =π P ×p P (x) + (1−π P )×p N (x)
and therefore use the following equality:
(1−π P )R− N (g) =R − U (g)−π P R− P (g) (3)
where:
R− U (g) :=E U [ℓ(g(x),−1)],
R− P (g) :=E P [ℓ(g(x),−1)]
are the empirical risks of the unlabeled samples and the positive samples in the
unlabeled set, respectively. As a result, the classification risk can be approximated by:
˜RP U(g) :=π P ˜R+ P (g)−π P ˜R− P (g) + ˜R− U (g),(4)
where:
˜R− P (g) = 1 nP
nPX
i=1
ℓ(−g(xP i )),
˜R− U (g) = 1 nU
nUX
i=1
ℓ(−g(xU i ))
7

By minimizing ˜RP U(g) we obtain the empirical minimizer ˜gP U. The authors note that
if a symmetric loss function is chosen, such as the sigmoid loss that was used in [46],
the PU risk becomes a cost-sensitive classification ofPandUdata with weight 2π P :
˜RP U:= 2πP ˜R+ P (g) + ˜R− U (g)−π P .
In practice, it was found that when using neural networks, the second term of
Eq. 4 can go much lower than zero, although theoretically it should always be non-
negative, because it is used to estimate (1−πP )EP [ℓ(g(x),−1)]. Therefore, the authors
in [43, 47] observed that:
R− U (g)−π P R− P (g) = (1−π P )R− N (g)≥0
and proposed the following non-negative PU risk estimator:
˜RnnP U(g) :=π P ˜R+ P (g) + max{0, ˜R− U (g)−π P ˜R− P (g)}(5)
In the following section, we aim to derive a non-negative risk estimator using an
appropriate loss function that addresses the challenges of the underlying imbalanced
class distribution in the data and the existence of positive examples in the unlabeled
set that are hard to separate from negative ones.
3.2 Focused risk estimator
In imbalanced data classification, we assume that the positive class is under-
represented while the negative class dominates the data. In PU data, this translates
to having few labeled positive examples and, at the same time, expecting a few pos-
itive examples to be hidden in the unlabeled set. Consequently, the first term of Eq.
5 becomes close to zero and the classification cost is dominated by the unlabeled
data. In many real-world domain applications, we also expect to have among the unla-
beled examples some positive ones that are hard to classify, since they may be close
to negative ones (PG assumption). These two phenomena make the learned model
weak in identifying positive examples. Therefore, the proposed risk estimators must
be equipped with appropriate loss functions to deal with this situation. In this work,
we derive a non-negative risk estimator for PU data that relies on Focal Loss [51],
which divides samples into hard-to-classify and easy-to-classify.
The focal loss is based on the cross-entropy loss function, appropriately modified to
address the class imbalance problem in classification tasks, by down-weighting the loss
for correctly classified examples and up-weighting the loss for misclassified examples.
The focal loss is defined in Eq. 6, where the exponential termγcontrols the weight of
easy and hard examples and the shape of the loss curve. When the probability for the
target class (p t) tends to 1 and the true class is the positive one, the example is an
easily classifiable example and the contribution to the loss is small. Whenp t tends to
0 but still the true class is the positive one for the particular example, the contribution
to the loss is larger.
F L(pt) =−(1−p t)γlog(pt) (6)
To incorporate the focal loss in the empirical risk estimator for PU classification,
we rewrite it as a composite loss, considering the ground truthyand the prediction
p. Letp t of Eq. 6 be:
8

pt =
(
p,ify= 1
1−p,ify=−1 (7)
Then, the focal loss is written as:
F L=
(
−(1−p) γlog(p),ify= 1
−pγlog(1−p),ify=−1 (8)
We can now work from Eq. 4 for the expected risk, by expandingR + P (g),R − P (g),
andR − U (g), in order to approximate the true risk. We call the derived risk estimator
iFPU:
RiF P U(g) :=π P R+ P (g)−π P R− P (g) +R − U (g) (9)
and by expanding, we have:
˜RiF P U(g) = 1 nP
nPX
i=1
−πP (1−g(x i))γlog(g(x i))
+ 1 nU
nUX
i=1
−(g(xi))γlog(1−g(x i))
− 1 nP
nPX
i=1
−πP (g(xi))γlog(1−g(x i))
(10)
and the corresponding non-negative PU risk is, therefore:
˜RiF P U(g) = 1 nP
nPX
i=1
−πP (1−g(x i))γlog(g(x i))
+ max{0, 1 nU
nUX
i=1
−(g(xi))γlog(1−g(x i))
− 1 nP
nPX
i=1
−πP (g(xi))γlog(1−g(x i))}
(11)
In terms of training, stochastic optimization is used. When ˜R− U (g)−π P ˜R− P (g)
becomes smaller than zero for a mini-batch, we perform a step of gradient ascent along
∇( ˜R− U (g)−π ˜R− P (g) to make the mini-batch less overfitted. The training process of
the non-negative focused risk estimator is performed according to Algorithm 1.
On a theoretical note, an important motivation for employing unbiased risk esti-
mators in weakly supervised settings is that they enable estimation error bounds to
guarantee statistical consistency. In [46], for example, the authors prove that their risk
estimator is both unbiased and consistent. On the other hand, proving consistency
in the asymptotic cases is not informative for the behavior of the estimator in the
9

Algorithm 1Imbalanced Focused PU (iFPU)
1:Input:training data (X P ,X U )
2:Parameters:class priorπ, max epochs, learning rate
3:Output:classifier ˜g P U(x;θ)
4:LetAbe an external SGD-like stochastic optimization method
5:whileno stopping criterion is metdo
6:Shuffle (X P ,X U ) intoNmini-batches
7:fori= 1 toNdo
8:if ˜RU (g;X i U )−π P ˜RP (g;X i P )≥0then
9:UpdateθbyAwith∇ θ ˜RP U(X i P ,X i U )
10:else
11:UpdateθbyAwith∇ θ( ˜RU (g;X i U )−π ˜RP (g;X i P ))
12:end if
13:end for
14:end while
15:Return:˜g P U(x;θ)
finite-sample cases, especially when using complex models and deep learning methods
[47, 52]. In combination with deep networks, unbiased risk estimators suffer from neg-
ative empirical risks during training, which is a sign of overfitting. Thus, biased risk
estimators are often employed to control overfitting. The iFPU risk estimator pro-
posed in this work relies on focal loss. Hence, the expected loss is not equal to the
actual loss of the model, as focal loss is designed to assign different weights to different
types of errors. This weighting can lead to an overestimate of the model’s actual risk.
Moreover, in the case of focal loss, it is not possible to guarantee that the expected
loss will converge to the true risk.
However, it is important to note that such a biased risk estimator can prove particu-
larly useful in practical applications, where there is a need to improve the performance
of the models on imbalanced datasets. In our case, the focal loss has been shown to be
classification-calibrated [53]. Although it may give under-confident or over-confident
classifiers, it can still yield the Bayes optimal classifier, which maximizes the expected
accuracy in classification, i.e., it makes the most probable prediction for each new
example. Finally, in terms of complexity, although the focal loss is more expensive than
the logistic loss, since it requires logs and powers, in practice the overall asymptotic
complexity remains the same.
3.3 Theoretical analysis
This section provides finite-sample guarantees and makes explicit which labeling
assumptions are required. Proofs can be found in Appendix A.
LetGbe the score class,p=σ(g(x)), and write the focal loss of Eq.6 asℓ +(z) =
−(1−σ(z)) γ logσ(z) andℓ −(z) =ℓ +(−z). With partial risksR + P =E pP [ℓ+],R − P =
EpP [ℓ−],R − U =E U [ℓ−], the iFPU estimator is bRiFPU =π P bR+ P −π P bR− P + bR− U , and the
target is the focal riskR FL(g) =π P EpP [ℓ+] +π N EN [ℓ−], under full positive-negative
supervision.
10

To model labeling, lete(x) = Pr(s=1|y=1, x) be the propensity,c=E pP [e(x)],
andp l = (e/c)p P the labeled-positive density from which the labeled positives are
drawn. In SCAR, we havee(x)≡c(hencep l =p P ), while SAR allowse(·) to depend
onx.
The mixture identityp=π P pP +π N pN used in Eqs. (3)–(5) is apopulation
identity that holds for any loss and any labeling mechanism. The labeling assumption
enters at the empirical positive average in Eqs. (10)–(11), which estimatesE pl [·]
rather thanE pP [·]. Proposition 1 makes this precise.
Proposition 1(Population identity and SCAR validity versus SAR bias).For any
loss and any labeling,R iFPU(g) =R FL(g)(population). The empirical estimator
satisfies
E
 bRiFPU(g)  =R FL(g) +b(g), b(g) =π P CovpP  e(x) c , ℓ+(g(x))−ℓ −(g(x))  .
Hence bRiFPU is unbiased forR FL under SCAR (b≡0), whereas under SAR, the bias
b(g)lives in the sampling mechanism of the labeled positives and is therefore orthogonal
to the choice of loss.
For the SAR case, estimatinge(x) under PU data needs extra identifiability
assumptions, as in the SAREM [18] and LBE [54] approaches. Therefore, the SAR
results of Section 5 are reported asempirical robustnessof the uncorrected estimator.
This robustness is plausibly aided by the focal term up-weighting precisely the hard
positives that SAR labeling down-weights inb(g).
Estimation error under SCAR.
The guarantees below targetR FL and therefore hold under SCAR.
Lemma 1(Focal loss is Lipschitz and bounded).For allγ≥0,ℓ ± areL γ-Lipschitz
in the score withL γ = 1 +γ/e, and0≤ℓ ± ≤C B =−σ(B) γ logσ(−B)whenever
|g(x)| ≤B.
The lemma records two elementary properties of the focal loss. First, it is never too
steep, since its slope is capped byL γ = 1+γ/eand, second, on a bounded score range,
it is never too tall, since it stays belowC B. The boundedness requires|g(x)| ≤B
because the focal loss diverges for confidently wrong predictions (p→0).
Theorem 1(SCAR estimation-error and excess-risk bound).Under SCAR and
|g(x)| ≤B, with probability at least1−δthe following bound holds:
sup
g∈G

 bRiFPU(g)−RFL(g)

 ≤2L γ  2πP RnP (G)+RnU (G)  +3CB q log(6/δ) 2nmin =O  1√nP + 1√nU  ,
whereR n is the Rademacher complexity andn min = min{nP , nU }. Consequently the
iFPU minimiserbghas excess focal riskR FL(bg)−ming∈G RFL(g)of the same order.
The theorem certifies that the empirical PU risk iFPU actually minimizes is a faith-
ful proxy for the population focal risk it cannot observe. Under SCAR the estimator
is centered on that risk (Proposition 1), and the gap between the two vanishes at the
standard rateO(1/ √nP + 1/√nU ), so more labeled positives or more unlabeled data
11

both tighten the guarantee. Since the bound holds for everygat once, it transfers to
the classifier iFPU returns, whose excess focal risk is of the same order. Because focal
loss is classification-calibrated [53], this excesssurrogaterisk transfers to excess 0–1
risk up to an approximation term, so the bound reaches the classification risk only
through calibration. Recall that the biased focal estimator need not converge to the
true risk as mentioned in Section 3.2.
4 Experimental setup
In this section, we evaluate the effect of the proposed risk minimizer (iFPU) on the
learning algorithm, comparing it with related PU learning methods under a common
experimental setup. Rather than optimizing classifiers or hyperparameters, our focus is
on assessing the impact of replacing other risk minimizers with iFPU. We also include
comparisons with state-of-the-art PU methods that employ different approaches.
Since we focus on learning with PU data under class imbalance, without making
explicit assumptions regarding the labeling mechanism, we experiment with both the
SCAR and the SAR assumptions. In the experiments, we model the single training
set scenario [3] and we use public datasets for imbalanced binary classification. In
particular, we replicate the experimental setup of [31] to facilitate direct comparison
against those methods. Since the datasets in their original form are not PU data, they
are processed to (a) treat the negative examples as unlabeled data and (b) “hide” part
of the positive examples in the unlabeled data.
The main contributions of the experimental setup are that it includes compar-
isons with multiple established PU methods and results under both SCAR and SAR
assumptions, with SAR modeled to reflect the more challenging probabilistic gap
scenario.
4.1 Datasets
As mentioned above, we use the same 14 datasets used in [31], that cover different
domains and are widely used in the imbalanced classification literature. We focus
especially on such datasets since they provide a varying imbalance, spanning positive
rates from about 1% to 14%. Table 1 summarizes the details of the datasets.
In Table 1, the columnPrefers to the percentage of positive examples in the
dataset, reflecting the different imbalance ratios in different datasets. As mentioned
above, we treat negative examples as unlabeled and “hide” positive examples in the
unlabeled set. Thus, the columnsP 25%toP 75%indicate the proportion of the posi-
tive examples that remain labeled in different experiments. This further demonstrates
the effect of class imbalance, since the inherent imbalance between the positive and
negative examples is gradually amplified by having fewer and fewer known positive
ones during training at different settings.
In addition, the labeling mechanism decides which of the positive examples will
become unlabeled. To simulate the SCAR assumption, each positive example has the
same probability of becoming unlabeled. On the other hand, the SAR assumption
introduces a bias to the selected positive examples that depends on the features. We
use the average Euclidean distance between positive and negative examples to bias the
12

T able 1Details of the 14 imbalanced classification datasets in terms of
number of samples, features, imbalance ratio, and percentages of positive
examples that become unlabeled to simulate PU data.
Dataset Obs. Feats Pos. ratio P75% P50% P25%
Cardio 1831 21 9.60% 7.20% 4.80% 2.40%
Thyroid 3772 7 2.50% 1.87% 1.25% 0.63%
Climate 540 20 8.52% 6.39% 4.26% 2.13%
Forest cover 5000 10 1.00% 0.75% 0.50% 0.25%
Seismic 2584 11 6.57% 4.93% 3.29% 1.64%
Mammography 5000 6 2.58% 1.93% 1.29% 0.65%
Shuttle 5000 9 6.40% 4.80% 3.20% 1.60%
Letter 1600 32 6.25% 4.69% 3.13% 1.56%
Yeast 1004 8 9.86% 7.40% 4.93% 2.47%
Poker 8-9vs5 2075 10 1.20% 0.90% 0.60% 0.30%
Pie chart 745 36 2.15% 0.61% 1.08% 0.54%
Pizza cutter 661 37 7.87% 5.90% 3.94% 1.97%
Satellite 5000 36 1.48% 1.11% 0.74% 0.37%
Segment 2308 18 14.0% 10.5% 7.0% 3.50%
labeling mechanism, as proposed in [31]. In particular, positive examples that are closer
to negative ones in the original feature space are more likely to become unlabeled.
The experiments are organized as follows. For each dataset, we perform 20 repe-
titions by splitting the data randomly into training (70%) and test (30%) sets. This
is performed for both assumptions regarding the labeled positive examples (SCAR
and SAR) and for all three ratios of positive examples that become unlabeled (25%,
50%, 75%). The above combinations create a total of (14datasets×10repetitions×
2labeling assumptions×3ratios) = 840 different runs of the methods.
4.2 Methods and parameters
We compare the proposed method 1 (iFPU) against three other methods that rely on
empirical risk minimization, namely the unbiased PU (uPU) [46], the non-negative PU
(nnPU) [47] and the imbalanced non-negative PU (i-NNPU) [48], as neural instanti-
ations commonly used in the literature, to assess the effect of the different empirical
risks. We also include an XGBoost classifier for fairer comparison with the other
approaches. Additionally, we compare iFPU against the two-step method (NNIF) pro-
posed in [31], which uses an anomaly detection step to create pseudo labels for the
data and then learns an XGBoost classifier with default hyperparameters. For the lat-
ter comparison, we also implement an XGBoost classifier, equipped with the iFPU
empirical risk estimator.
Moreover, we compare our method against PU Hellinger Decision Trees (PUHDT)
and PU Hellinger Random Forests (PUHRF) [49], both known to achieve state-of-
the-art performance in positive-unlabeled learning. Lastly, we also compare against
the instance-dependent PU deep learning method with labeling bias estimation (LBE)
[54], which specializes in hard settings with label bias, as in SAR, as well as with
1Code and data will be published on GitHub.
13

SAREM [18], which is an Expectation-Maximization (EM) framework for PU learn-
ing and was one of the first approaches to explicitly tackle SAR. Additionally, we
include results obtained from an XGBoost classifier treating the unlabeled instances
as negatives (negativity assumption) as well as results from fully supervised train-
ing of the XGBoost classifier, serving as an upper bound for achievable classification
performance. In this supervised scenario, we evaluate XGBoost using both the stan-
dard loss and the focal loss to further validate the suitability of focal loss under
our class-imbalanced conditions. Table 2 summarizes all methods evaluated in our
experiments.
T able 2Methods used in empirical evaluation.
Method Setting Configuration
uPU Positive-Unlabeled MLP, 5 layers, sigmoid loss
nnPU Positive-Unlabeled MLP, 5 layers, sigmoid loss
i-NNPU Positive-Unlabeled MLP, 5 layers, sigmoid loss
iFPUM LP Positive-Unlabeled MLP, 5 layers, PU focal loss
uPUXGB Positive-Unlabeled XGBoost, default hyper-parameters
nnPUXGB Positive-Unlabeled XGBoost, default hyper-parameters
NNIF Positive-Unlabeled XGBoost, default hyper-parameters
PUHDT Positive-Unlabeled PU Hellinger Decision Tree, default hyper-parameters
PUHRF Positive-Unlabeled PU Hellinger Random forest, default hyper-parameters
LBE Positive-Unlabeled MLP, default hyper-parameters
SAREM Positive-Unlabeled Expectation-Maximization, default parameters
iFPUXGB Positive-Unlabeled XGBoost, PU focal loss, default hyper-parameters
XGBoost Positive-Unlabeled Negativity assumption, standard loss, default hyper-parameters
XGBoost Positive-Negative XGBoost supervised, standard loss, default hyper-parameters
XGBoostF L Positive-Negative XGBoost supervised, focal loss, default hyper-parameters
The focal loss introduces an additional parameter,γ. Specifically, the gradient of
the focal loss is a weighted variant of the cross-entropy gradient, where the weighting
depends onγthrough the termp t. The latter is based on the model’s predictions
and also appears in standard cross-entropy. The parameterγeffectively controls the
threshold probability at which the gradient flowing backward becomes small (or zero),
indicating regions where the model is confident in its predictions. Hence, adjustingγ
allows the selection of a probability threshold below which predictions are considered
non-confident and thus receive larger gradient updates. However, in this work we avoid
hyper-parameter tuning, as it necessitates additional assumptions, especially under the
SAR scenario, due to the absence of negatively labeled validation data [55]. Therefore,
we adopt the recommended default setting ofγ= 3.
5 Empirical results
We evaluate the performance of the methods on 14 heavily imbalanced datasets,
with varying ratios of labeled positives under both SCAR and SAR labeling assump-
tions. Specifically, we investigate how our proposed risk estimator compares to related
14

approaches based on similar risk-minimization frameworks, as well as to state-of-the-
art methods. Although we experiment with two classifiers (MLP and XGBoost), our
analysis primarily focuses on the impact of the risk minimizer rather than on the
choice of classifier.
T able 3Evaluation results under the SCAR assumption across different proportions of labeled
positive examples. As shown in Table 2, the first four models use an MLP classifier, while the next
eight use state-of-the-art tree-based methods. In the final three rows, the first model operates under
the negativity assumption, treating unlabeled examples as negative, and the other two are fully
supervised and included for comparison purposes. Results are expressed in terms of ROC-AUC and
PR-AUC for the positive class, macro-averaged over the 14 datasets. The best performing method is
shown in bold and the runner up is underlined.
ROC-AUC PR-AUC
Labeled proportion: 25% 50% 75% 25% 50% 75%
uPU 0.53±0.06 0.55±0.05 0.56±0.04 0.12±0.04 0.13±0.03 0.13±0.02
nnPU 0.54±0.06 0.55±0.05 0.56±0.04 0.12±0.04 0.13±0.02 0.13±0.02
i-NNPU 0.54±0.05 0.56±0.05 0.56±0.03 0.12±0.03 0.13±0.02 0.13±0.02
iFPUM LP 0.58±0.03 0.60±0.03 0.62±0.03 0.13±0.03 0.14±0.02 0.14±0.01
uPUXGB 0.77±0.05 0.82±0.05 0.85±0.03 0.37±0.06 0.44±0.06 0.50±0.06
nnPUXGB 0.81±0.05 0.84±0.04 0.86±0.03 0.43±0.06 0.49±0.06 0.52±0.05
NNIF 0.81±0.05 0.85±0.03 0.87±0.03 0.46±0.06 0.50±0.06 0.53±0.05
PUHDT 0.72±0.09 0.77±0.07 0.79±0.07 0.40±0.07 0.43±0.06 0.46±0.05
PUHRF0.83±0.07 0.87±0.06 0.89±0.06 0.52±0.09 0.59±0.07 0.63±0.06
LBE 0.80±0.06 0.84±0.05 0.86±0.04 0.49±0.08 0.53±0.06 0.53±0.06
SAREM 0.81±0.05 0.84±0.04 0.85±0.04 0.51±0.06 0.55±0.06 0.56±0.06
iFPUXGB 0.80±0.04 0.85±0.03 0.87±0.03 0.52±0.050.57±0.04 0.60±0.05
XGBoostneg. 0.59±0.03 0.60±0.03 0.63±0.03 0.22±0.05 0.31±0.05 0.42±0.05
XGBoost 0.90±0.03 0.90±0.03 0.90±0.03 0.65±0.05 0.65±0.05 0.65±0.05
XGBoostF L 0.92±0.03 0.92±0.03 0.92±0.03 0.67±0.05 0.67±0.05 0.67±0.05
Table 3 presents the results under the SCAR assumption. In this setting, we include
the methods of uPU [46], nnPU [47], i-NNPU [48], and our iFPU, using a 5-layer MLP
classifier, as shown in the first four rows of the table. These methods demonstrate
relatively low performance in terms of ROC-AUC and PR-AUC. The results of uPU,
nnPU, and i-NNPU are comparable, with nnPU and i-NNPU offering little improve-
ment over uPU, despite attempts to address overfitting [47] or class imbalance [48].
iFPU outperforms the other three methods, albeit with a small margin.
The next eight rows of Table 3 present a comparison between our proposed method,
the two extensions of uPU and nnPU to an XGBoost classifier, and five state-of-
the-art approaches: the two-step NNIF technique [31], the PU Hellinger decision tree
(PUHDT), and its ensemble variant (PUHRF) [49], the instance-dependent PU with
label bias (LBE) [54], and the SAREM approach [18]. For consistency, we employ the
XGBoost classifier in our method, since NNIF utilizes XGBoost, and the Hellinger-
based methods also rely on tree-based classifiers. The final three rows show the
performance of the XGBoost classifier under a biased setting treating all unlabeled as
negatives and under two fully supervised settings. The latter serves as an upper bound
for PU classifiers. We report results using both the standard loss and the focal loss,
15

clearly demonstrating the superior performance of the focal loss in this scenario and
supporting our decision to minimize a risk estimator based on focal loss. It should be
noted that the NNIF method includes an anomaly detection step designed to remove
“noisy” negative examples from the unlabeled set prior to training XGBoost with
the remaining examples treated as negatives. In contrast, our iFPU method directly
incorporates the proposed risk estimator into the XGBoost training process without
requiring any pre-processing. Similarly, PUHDT, PUHRF, LBE, and SAREM inte-
grate unlabeled examples directly during training without pre-processing steps. All
tree-based methods use the same XGBoost and tree-based parameters to ensure a fair
comparison.
The results confirm, as expected, that the number of labeled positive examples
significantly influences both ROC-AUC and PR-AUC across all evaluated methods.
Although ROC-AUC is reported, it should be noted that it is less reliable in scenarios
of extreme class imbalance. This is because the false positive rate becomes insensitive
to changes in the number of false positives, due to its denominator being dominated by
a large number of true negatives. In contrast, PR-AUC is more sensitive to false posi-
tives and is unaffected by the number of true negatives, thus providing a more reliable
metric in highly imbalanced contexts. Considering PR-AUC as the most suitable met-
ric, our proposed iFPU method outperforms the uPU and nnPU extensions, as well as
NNIF, PUHDT, LBE, and SAREM though it remains slightly below PUHRF. Addi-
tionally, aiming to measure significant performance differences among all methods of
Table 3, the Iman-Davenport statistical test indeed reveals significant differences, rank-
ing PUHRF first and iFPU second. However, to examine whether there are statistical
differences between PUHRF and iFPU that achieve comparable performance, a sub-
sequent Wilcoxon paired test indicates no statistically significant difference between
these two across all three proportions of labeled positive examples (p-value>0.05).
Under the more realistic SAR assumption (Table 4), the results differ notably.
Again, the first four rows compare our proposed method with methods employing
similar risk minimizers. Importantly, iFPU maintains performance comparable to that
observed under the SCAR assumption (Table 3), whereas the performance of the
other methods declines. This highlights the robustness of iFPU in scenarios where
positive examples resembling negatives are less likely to be labeled. As anticipated,
performance improves with an increasing percentage of labeled positive examples.
Examining the next eight rows of Table 4 and again focusing on PR-AUC, we
observe that all methods experience some performance degradation under the SAR
assumption. However, NNIF, PUHRF, LBE, SAREM, and iFPU XGB exhibit greater
resilience, with a smaller decrease in performance compared to PUHDT. Notably,
iFPU outperforms all methods, except for PUHRF, across all three proportions of
labeled positive examples. Specifically, iFPU achieves comparable results to PUHRF
in the scenarios with 50% and 75% labeled positive examples. Importantly, in the
most challenging scenario—where only 25% of positive examples are labeled, iFPU
surpasses PUHRF by 5 percentage points and LBE and SAREM by 3 and 2 percent
points respectively. This supports the applicability of our proposed method in more
realistic and challenging scenarios that frequently arise in real-world applications. In
16

T able 4Evaluation results under the SAR assumption across different proportions of labeled
positive examples. As shown in Table 2, the first four models use an MLP classifier, while the next
eight use state-of-the-art tree-based methods. In the final three rows, the first model operates under
the negativity assumption, treating unlabeled examples as negative, and the other two are fully
supervised and included for comparison purposes. Results are expressed in terms of ROC-AUC and
PR-AUC for the positive class, macro-averaged over the 14 datasets. The best performing method is
shown in bold and the runner up is underlined.
ROC-AUC PR-AUC
Labeled proportion: 25% 50% 75% 25% 50% 75%
uPU 0.52±0.05 0.52±0.04 0.53±0.03 0.11±0.02 0.11±0.02 0.12±0.02
nnPU 0.53±0.05 0.53±0.04 0.54±0.03 0.11±0.02 0.11±0.02 0.12±0.02
i-NNPU 0.54±0.05 0.53±0.03 0.54±0.02 0.12±0.02 0.12±0.02 0.12±0.02
iFPUM LP 0.58±0.04 0.60±0.02 0.61±0.01 0.13±0.02 0.14±0.02 0.14±0.01
uPUXGB 0.75±0.06 0.82±0.04 0.85±0.03 0.33±0.06 0.44±0.06 0.49±0.06
nnPUXGB 0.79±0.05 0.84±0.04 0.86±0.03 0.40±0.06 0.47±0.06 0.52±0.05
NNIF0.80±0.050.85±0.03 0.87±0.03 0.43±0.06 0.50±0.06 0.53±0.05
PUHDT 0.69±0.06 0.76±0.06 0.78±0.06 0.33±0.06 0.41±0.05 0.45±0.05
PUHRF0.80±0.060.86±0.06 0.89±0.050.45±0.060.57±0.06 0.62±0.06
LBE 0.79±0.05 0.84±0.04 0.85±0.04 0.47±0.07 0.53±0.06 0.53±0.06
SAREM0.80±0.050.84±0.04 0.85±0.04 0.48±0.07 0.53±0.07 0.55±0.06
iFPUXGB 0.80±0.050.84±0.03 0.87±0.05 0.50±0.050.55±0.05 0.60±0.05
XGBoostneg. 0.58±0.03 0.60±0.03 0.63±0.03 0.18±0.05 0.28±0.05 0.40±0.05
XGBoost 0.90±0.03 0.90±0.03 0.90±0.03 0.65±0.05 0.65±0.05 0.65±0.05
XGBoostF L 0.92±0.03 0.92±0.03 0.92±0.03 0.67±0.05 0.67±0.05 0.67±0.05
all settings, the biased XGBoost classifier under the negativity assumption is pre-
sented as an ablation of replacing the “focused” risk estimator with the standard loss,
highlighting the positive effect of using iFPU in an imbalanced PU setting.
In terms of statistical significance across all methods, the Iman-Davenport statis-
tical test reveals significant differences when considering all methods under the SAR
assumption. Specifically, PUHRF ranks first, followed by iFPU, when 50% or 75% of
the positive examples are labeled. In contrast, in the most challenging scenario with
only 25% labeled positives, iFPU ranks first. Furthermore, the Wilcoxon paired test
indicates that iFPU is statistically indistinguishable from PUHRF at 50% or 75%
labeled positive examples. However, in the most challenging setting with only 25%
labeled examples, iFPU significantly outperforms all the other methods (p-value<
0.05).
Analyzing the performance of the two best methods (PUHRF and iFPU) further,
Figure 1 illustrates their performance on the three most heavily imbalanced datasets,
considering the most challenging scenario - that is, when only 25% of the positive
examples are labeled - under both labeling assumptions. The box plots summarize
results from ten independent runs of each method per dataset. In the relatively eas-
ier SCAR case, iFPU appears to achieve a slightly higher performance on the Cover
dataset, exhibiting a higher mean and median PR-AUC values, whereas the two meth-
ods perform similarly on the other two datasets. Under the more challenging SAR
assumption, iFPU clearly outperforms PUHRF in the Cover and Satellite datasets, as
17

Fig. 1Comparison of the iFPU XGB and PUHRF methods on the three most imbalanced datasets
(Cover, Poker, Satellite) under (a) the SCAR assumption and (b) the SAR assumption, with only 25%
of positive examples labeled. Box plots summarize the PR-AUC performance across 10 independent
runs for each method and dataset. The median is shown with a solid and the mean with a dotted
line in each box.
indicated by higher mean and median PR-AUC values, while the two methods achieve
similar performance in the Poker dataset.
It is important to emphasize that no hyperparameter tuning was conducted in this
study. While this was intentional, optimizing parameters for the XGBoost classifier
and focal loss could potentially yield even stronger results. However, unbiased hyperpa-
rameter tuning in positive-unlabeled scenarios is challenging, as it requires additional
assumptions due to the lack of negatively labeled validation data [55]. Therefore,
addressing this challenge remains open for future research. It is also important to note
that the focus of the controlled experiments was to show the effect of iFPU, keeping as
much as possible similar classifiers with same hyper-parameters. Considering that the
empirical evaluation was performed on tabular data, a natural consideration would be
the use of TabPFN [40]. Tabular foundation models are shown to perform remarkably
well in a fully supervised positive-negative setting. Although iFPU is agnostic to the
base classifier, a proper integration that minimises the iFPU risk over a pre-trained
tabular representation is non-trivial because a frozen pre-trained model exposes no
per-task empirical risk, and we flag it as future work at this point.
5.1 Sensitivity analysis on class prior
Accurate estimation of the class prior is essential for methods relying on prior prob-
abilities, such as the approach proposed in this work. Although the priorπ p can be
effectively estimated from (P), (N), and (U) data [56, 57], prior misspecification per-
formance is crucial in such methods. In this section, we perform a sensitivity analysis
to explore the impact of incorrect prior estimates on the performance of iFPU.
18

Fig. 2Sensitivity analysis of the iFPU XGB method with respect to incorrect class prior estimates,
averaged across all datasets. Performance is measured by macro-average PR-AUC of the positive class,
under (a) the SCAR assumption and (b) the SAR assumption, with only 25% of positive examples
labeled. Error bars indicate standard deviations.
We use the same 14 datasets under the SCAR and SAR assumptions, focus-
ing specifically on the most challenging scenario—when only 25% of the pos-
itive examples are labeled. For this analysis, we evaluate the method using
various prior estimates based on multiples of the ground-truth prior:π P ∈
{0.25πP ,0.5π P , πP ,1.5π P ,2.0π P ,4.0π P }.
Figure 2 presents the results measured by PR-AUC under (a) the SCAR assump-
tion and (b) the SAR assumption. We observe that iFPU generally exhibits robust
performance across the entire range of incorrect prior estimates. The best results are
achieved, as expected, when the correct prior is selected, whereas the largest per-
formance degradations occur with significantly underestimated priors. Notably, the
robustness of the method remains consistent regardless of the labeling assumption.
6 Real-world application
Beyond the controlled experiments across benchmark datasets, we wanted to assess
the value of the method in a real-world problem. For this purpose, we used it to detect
financial misstatements in annual reports, a task where PU data naturally arise. Finan-
cial misstatements, which severely impact firms and stakeholders, demand accurate
detection to ensure reports are error-free. This task is labor-intensive, involving the
calculation of risk indicators and financial variables [7–9]. Thus, the literature relies on
historical data to train ML models to predict the likelihood of future misstatements.
The domain faces two major challenges: extreme class imbalance, as misstatements
constitute a small fraction of the reports, and sparsely labeled positives, due to delayed
identification of misstatements [7, 9]. Misstatements often remain undetected for years,
affecting multiple reports. While historical data used for ML training are fully anno-
tated, realistic modeling must account for the limited labeled positives and abundant
unlabeled examples during training, reflecting real-world delays in detection.
Misstatements, whether intentional or due to accounting errors, are challenging
to identify. Intentional misstatements are often deliberately concealed, while errors
closely resemble normal cases, making detection difficult. This aligns with the prob-
abilistic gap (PG) assumption, where unlabeled positives resemble negatives due to
the labeling mechanism’s effort constraints. Thus, financial misstatement detection
exemplifies learning from imbalanced PU data, under the PG assumption.
19

6.1 Data and experimental setting
We used the data and experimental setup from [9, 58], based on financial informa-
tion from [7], which includes publicly traded US companies and consolidated financial
statements. Each record represents a financial report for a specific year, with 28 finan-
cial indices, such as assets, debt, receivables, liabilities, and 14 derived features from
the work in [59], such as soft assets, earning before interest, and market data which
have proven effective in misstatement detection [7, 8]. Additional categorical features,
such as industry and state of incorporation, are also included. For details on the finan-
cial variables, the reader is referred to [7, 60] and Appendix B. The data spans the
period 2000–2014, aligned with the test years of [7, 9, 58, 61].
The dataset is structured with test years from 2003–2014, and for each test year,
the preceding three years are used for training (e.g., 2000–2002 for 2003). In total, there
are 47,086 firm-year instances in the data. Each instance in the dataset is labeled as
positive (misstatement) or negative, with positives constituting only 1% of the dataset.
While all labels are available, this does not reflect reality: misstatements are often
discovered years after filing, and may retroactively affect multiple prior reports [62].
Empirical evidence suggests that overlooking this delay can significantly bias model
performance [9].
To simulate the delayed detection of financial misstatements, labels in the training
set are flipped for “unknown positives” if their restatement date falls after the test
year, based on the Audit Analytics (AA) database2. This ensures a realistic setup with
hidden positives in the training data. Following this approach, as shown in Figure 3,
approximately 40% of positive training labels are missing at the time of training, with
higher percentages for years closer to the test year. For example, when testing on 2003,
only 50% of positives are retained for 2002 (Y-1year), 70% for 2001 (Y-2year), and
80% for 2000 (Y-3year), resulting in about 40% of positives hidden in the unlabeled
pool (blue bar).
We adopt the model architecture from [58], modifying it to incorporate the
proposed empirical risk. The model features a TabTransformer [63] for contextual
embeddings of categorical attributes, which enhances predictive accuracy by capturing
interactions between categorical variables. These embeddings are concatenated with
continuous attributes to form a final feature vector, which is processed by a gated
MLP (gMLP) module [64]. The gMLP encodes cross-feature interactions using a gat-
ing mechanism similar to attention. To address class imbalance and detect overlapping
positives and negatives, a calibrated focal loss is minimized. We adapt this by incor-
porating the proposed iFPU method, which uses the same calibration mechanism for
focal loss as [58]. Specifically, the focal loss parameterγis set to 3 or 5, based on
model confidence, andαis set to the inverse class frequency. To compare the PU set-
ting against prior work, we use the same hyperparameters as [58] without additional
tuning. Moreover, we include the iFPU XGB method described in this work, i.e., the
proposed iFPU risk estimator with the XGBoost classifier, as well as the PUHRF
method, which was also included in our controlled experiments of Section 5.
2https://www.auditanalytics.com/
20

Test year
Percentage of known positives
0
25
50
75
100
2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014
Total in training Y-1 Y-2 Y-3
Fig. 3The percentage of the positive examples (misstatements) that are known per training year.
Y-1,Y-2, andY-3correspond to the three years before the test year.
6.2 Empirical results
In the setting described in section 6.1, we evaluate the classification models as rankers,
similar to previous work [7, 9, 58, 61], since the task requires associating every report
with a score, i.e., the classifier’s confidence. In addition, it has been argued [7, 8] that
the time capacity of human auditors is limited, and, in practice, auditors can choose
to see as many high-risk reports as possible. Thus, we report results on R-precision,
which is a ranking evaluation measure for direct comparison with the previous work.
We compare the method that incorporates the calibrated-iFPU and the pro-
posed iFPU XGB , as well as the PUHRF [49], against the work in [9], which
uses the TabTransformer with the gMLP and the calibrated focal loss (TabTrans-
former gMLP Cal FL) and we also include the methods in [9] (Fin-SVM and Fin-LR),
the RUSBoost from [7, 8], and the methodology proposed in [7], where there is a tem-
poral gap of two years between training and testing (SVM-2y gap and LR-2y gap).
The assumption behind this two-year gap is that most misstatements will have been
detected meanwhile, and thus, a PU setting may not be required. Our exploratory
analysis confirmed that these two years contain the majority of unknown positives
(see Fig. 3). However, unknown positives exist also beyond the two-year period.
In terms of empirical results in the context of this task, it has been argued [7–9]
that it is common for suggested models to perform poorly since the challenges of the
task and the peculiarities of the financial domain do not allow much space for general-
ization. However, as shown in Table 5, the TabTransformer model with the calibrated
focal loss managed to achieve an R-precision score three times higher than the RUS-
Boost model. An important note to make here is that all the methods presented in
Table 5, except the ones using iFPU or PUHRF, do not assume a PU setting. This
means that although they are all evaluated on the same data, using the same number of
positive examples in the training sets, they rely on the negativity assumption, treating
all unlabeled examples as negative. On the other hand, when we model the problem
21

T able 5Performance of different methods in terms of
R-precision, averaged over the period 2003-2014.
Method R-precision
LR-2y gap from [7] 2.40%
SVM-2y gap from [7] 2.00%
RUSBoost from [7, 8] 5.73%
Fin-SVM from [9] 3.40%
Fin-LR from [9] 4.70%
TabTransformer gMLP Cal FL from [58] 17.63%
PUHRF 18.22%
Calibrated-iFPU 19.10%
iFPUXGB 19.95%
as a PU learning task, we achieve higher performance, as shown in the last two rows
of the table, which, to the best of our knowledge, constitutes the state-of-the-art in
misstatement detection. Notably, in this realistic PU setting, the methods incorporat-
ing iFPU perform better than PUHRF, indicating that the proposed method is more
suitable for handling real-world cases where PU data resembling the probabilistic gap
assumption arises.
7 Conclusions
While PU learning has been widely studied, its application to imbalanced PU data
remains underexplored. We address this gap by proposing a PU learning method
based on the risk minimization framework, incorporating focal loss as a surrogate
loss function. This approach uses both positive and unlabeled examples for training,
leveraging the focal loss to emphasize hard-to-identify positive examples. Unlike two-
step PU learning methods, the proposed approach integrates seamlessly with any
classification algorithm based on cost minimization.
We extensively evaluated the method on 14 benchmark datasets and a real-
world application, simulating various labeling mechanisms to reflect natural PU data
emergence. The method’s performance highlights the potential of risk minimization
techniques for PU learning. At the same time, extensions to semi-supervised and
multi-class settings are natural directions for future research.
Other future directions include testing on additional datasets, including more real-
world scenarios, and extending the method to multi-positive and unlabeled settings.
Additionally, temperature scaling could be explored to calibrate model outputs toward
true class posteriors, though optimizing the required temperature parameter in PU
data presents a non-trivial challenge that is also worth exploring.
Appendix A Proofs
Throughout,R n(G) =E

supg∈G 1 n Pn i=1 εi g(xi)  denotes the Rademacher complexity
ofG, withε i i.i.d. Rademacher signs. We useℓ±,R ± P ,R − U ,R FL,e(·),c, andp l = (e/c)pP
as defined in Section 3.3.
22

A.1 Proof of Proposition 1
Proof of Proposition 1. Population identity.The mixture identityp(x) =π P pP (x) +
πN pN (x) gives, for any fixedh,E U [h] =π P EpP [h] +π N EN [h]. Takingh=ℓ −(g(·))
yieldsπ N R− N (g) =R − U (g)−π P R− P (g), i.e. Eq. (3). Substituting intoR FL(g) =
πP R+ P (g) +πN R− N (g) givesR FL(g) =π P R+ P (g)−π P R− P (g) +R− U (g) =R iFPU(g), using
only the mixture identity, hence for any loss and any labeling mechanism.
Bias of the empirical estimator.The labeled positives are drawn fromp l, so the
positive averages have meanE pl [·] while the unlabeled average has meanE U [·]. By
linearity and the population identity,
E
 bRiFPU(g)  −R FL(g) =π P  Epl −E pP   ℓ+ −ℓ −  ,
since the unlabeled term is unchanged. Fromp l = (e/c)pP ,

Epl −E pP

[h] =E pP
h e(x)
c −1

h
i
, h=ℓ + −ℓ −.
BecauseE pP [e(x)/c] = 1, the multipliere(x)/c−1 is mean-zero underp P , so this expec-
tation equals Cov pP

e(x)/c, h

. This proves the stated form ofb(g). Under SCAR,
e(x)≡c, soe(x)/cis constant and the covariance vanishes for everyg; under SAR it
is generally nonzero. The multiplier depends only on the labeling mechanism and not
onℓ, establishing that the bias is orthogonal to the choice of loss.
A.2 Proof of Lemma 1
Proof of Lemma 1.Sinceℓ −(z) =ℓ +(−z), it suffices to bound|ℓ ′ +(z)|. We writep=
σ(z), and use sigmoid’s derivative dp/dz=p(1−p). Differentiatingℓ + =−(1−
p)γ logp,
dℓ+
dp =γ(1−p) γ−1 logp− (1−p) γ p ,
hence, by the chain rule,
ℓ′ +(z) = dℓ+ dp p(1−p) =γ p(1−p) γ logp−(1−p) γ+1.(A1)
Both terms in (A1) are non-positive on (0,1), so|ℓ ′ +(z)|=γ p|logp|(1−p) γ + (1−
p)γ+1. The mapp7→ −plogpon (0,1) is maximised atp= 1/ewith value 1/e;
with (1−p) γ ≤1 this bounds the first term byγ/e, and the second by 1. Thus
|ℓ′ +(z)| ≤1 +γ/e=L γ.
For boundedness, (A1) showsℓ ′ +(z)≤0, soℓ + is non-increasing and attains
its maximum on [−B, B] atz=−B, wherep=σ(−B) and 1−p=σ(B), giv-
ingℓ +(−B) =−σ(B) γ logσ(−B) =C B; non-negativity follows from−logp≥0.
Symmetry gives the same bounds forℓ −.
23

A.3 Proof of Theorem 1
Proof of Theorem 1.Under SCAR,p l =p P , so by Proposition 1 the empirical positive
averages are unbiased forR ± P andE[ bRiFPU] =R FL. The triangle inequality gives
sup
g

 bRiFPU −R FL

 ≤π P sup
g

 bR+ P −R + P

 +π P sup g

 bR− P −R − P

 + sup g

 bR− U −R − U

.
Fix one term, an average ofni.i.d. terms of the formℓ(g(x)) bounded byC B
(Lemma 1). Changing one sample shifts the supremum by at mostC B/n, so
McDiarmid’s inequality gives, with probability at least 1−δ/3,
sup
g

 bR−R

 ≤Esup
g

 bR−R

 +C B q log(6/δ) 2n .
Standard symmetrisation bounds the expectation by 2R n(ℓ◦ G), and the Ledoux-
Talagrand contraction inequality [65, 66], applicable sinceℓisL γ-Lipschitz (Lemma 1),
givesR n(ℓ◦G)≤L γRn(G). Hence each term is at most 2LγRn(G)+C B
p
log(6/δ)/(2n)
withn=n P for the two positive terms andn=n U for the unlabeled term. A union
bound over the three events, together withπ P ≤1, 2π P + 1≤3, andn≥n min, yields
the displayed bound. The order statement follows whenR n(G) =O(1/ √n), as for
norm-bounded linear or neural classes.
Excess risk.Let ∆ = sup g | bRiFPU(g)−R FL(g)|,bg∈arg min g bRiFPU(g) andg ⋆ ∈
arg ming RFL(g). ThenR FL(bg)−RFL(g⋆)≤( bRiFPU(bg) + ∆)−(bRiFPU(g⋆)−∆)≤2∆,
since bRiFPU(bg)≤ bRiFPU(g⋆). Thus the excess focal risk is of the same order as the
bound above.
Appendix B Financial features for misstatement
detection
This section provides the list of financial features used for the real-world modeling of
misstatement detection.
References
[1] Frenay, B., Verleysen, M.: Classification in the presence of label noise: A survey.
IEEE Transactions on Neural Networks and Learning Systems25(5), 845–869
(2014) https://doi.org/10.1109/TNNLS.2013.2292894
[2] Zhou, Z.-H.: A brief introduction to weakly supervised learning. National Science
Review5(1), 44–53 (2017) https://doi.org/10.1093/nsr/nwx106
[3] Bekker, J., Davis, J.: Learning from positive and unlabeled data: a
survey. Machine Learning109(4), 719–760 (2020) https://doi.org/10.1007/
s10994-020-05877-5
24

T able B1Financial feature set from [9], based on [7] and [59].
Current assets, total (act) Account payable (ap)
Assets, total (at) Common/ordinary equity, total (ceq)
Cash & short investments (che) Cost of goods sold (cogs)
Common shares outstanding (csho) Debt in current liabilities, total (dlc)
Inventories, total (invt) Long-term debt issuance (dltis)
Long-term debt, total (dltt) Net income (ni)
Depreciation & amortization (dp) Receivables, total (rect)
Income bf extraordinary items (ib) Investment and advances, other (ivao)
Retained earnings (re) Short-term inv/ments, total (ivst)
Current liabilities, total (lct) Liabilities, total (lt)
Preferred stock (capital), total (pstk) Sales/turnover (sale)
Sale of common/preferred stock (sstk) Income taxes payable (txp)
Income taxes, total (txt) Interest and expense, total (xint)
Price close, annual, fiscal (prcc f) WC accruals (dch wc)
RSST accruals (ch rsst) Change in receivables (dch rec)
Change in inventory (dch inv) Change in cash sales (ch cs)
Soft assets percentage (soft assets) Change in cash margin (ch cm)
Change in return on assets (ch roa) actual issuance (issue)
Book to market (bm) Depreciation index (dpi)
Retained earnings over assets (reoa) Earnings before interest (EBIT)
Cash Flow Earnings Difference (ch fcf) Property & equipment, total (ppegt)
[4] Claesen, M., De Smet, F., Suykens, J., De Moor, B.: A robust ensemble approach
to learn from positive and unlabeled data using svm base models. Neurocomput-
ing160, 73–84 (2015) https://doi.org/10.1016/j.neucom.2014.10.081
[5] Claesen, M., De Smet, F., Gillard, P., Mathieu, C., De Moor, B.: Building classi-
fiers to predict the start of glucose-lowering pharmacotherapy using belgian health
expenditure data. ArXivabs/1504.07389(2015)
[6] Stripling, E., Baesens, B., Chizi, B., vanden Broucke, S.: Isolation-based condi-
tional anomaly detection on mixed-attribute data to uncover workers’ compen-
sation fraud. Decision Support Systems111, 13–26 (2018) https://doi.org/10.
1016/j.dss.2018.04.001
[7] Bao, Y., Ke, B., Li, B., Yu, Y.J., Zhang, J.: Detecting accounting fraud in pub-
licly traded us firms using a machine learning approach. Journal of Accounting
Research58(1), 199–235 (2020)
[8] Bertomeu, J., Cheynel, E., Floyd, E., W., P.: Using machine learning to detect
misstatements. Review of Accounting Studies26, 468–519 (2021)
[9] Zavitsanos, E., Mavroeidis, D., Bougiatiotis, K., Spyropoulou, E., Loukas, L.,
Paliouras, G.: Financial misstatement detection: A realistic evaluation. In: Pro-
ceedings of the Second ACM International Conference on AI in Finance. ACM,
Virtual event (2021). https://doi.org/10.1145/3490354.3494453
25

[10] Gal´ arraga, L., Teflioudi, C., Hose, K., Suchanek, F.M.: Fast rule mining in onto-
logical knowledge bases with amie+. The VLDB Journal24(6), 707–730 (2015)
https://doi.org/10.1007/s00778-015-0394-1
[11] Vasighizaker, A., Jalili, S.: C-pugp: A cluster-based positive unlabeled learning
method for disease gene prediction and prioritization. Computational Biology
and Chemistry76, 23–31 (2018) https://doi.org/10.1016/j.compbiolchem.2018.
05.022
[12] Zupanc, K., Davis, J.: Estimating rule quality for knowledge base completion
with the relationship between coverage assumption. In: Proceedings of the 2018
World Wide Web Conference, pp. 1073–1081. International World Wide Web
Conferences Steering Committee, Lyon, France (2018). https://doi.org/10.1145/
3178876.3186006
[13] Mignone, P., Pio, G., Dˇ zeroski, S., Ceci, M.: Multi-task learning for the simulta-
neous reconstruction of the human and mouse gene regulatory networks. Scientific
Reports10(1), 22295 (2020) https://doi.org/10.1038/s41598-020-78033-7
[14] Mignone, P., Pio, G., D’Elia, D., Ceci, M.: Exploiting transfer learning for the
reconstruction of the human gene regulatory network. Bioinformatics36(5), 1553–
1561 (2019) https://doi.org/10.1093/bioinformatics/btz781
[15] Japkowicz, N.: The class imbalance problem: Significance and strategies. In: Pro-
ceedings of the 2000 International Conference on Artificial Intelligence ICAI.
Computer Science Research, Education and Applications Press, Athens, Georgia,
USA (2000)
[16] Krawczyk, B.: Learning from imbalanced data: open challenges and future direc-
tions. Progress in Artificial Intelligence5(4), 221–232 (2016) https://doi.org/10.
1007/s13748-016-0094-0
[17] Elkan, C., Noto, K.: Learning classifiers from only positive and unlabeled data. In:
Proceedings of the 14th ACM SIGKDD International Conference on Knowledge
Discovery and Data Mining, pp. 213–220. ACM, Las Vegas, Nevada, USA (2008).
https://doi.org/10.1145/1401890.1401920
[18] Bekker, J., Robberechts, P., Davis, J.: Beyond the selected completely
at random assumption for learning from positive and unlabeled data. In:
Machine Learning and Knowledge Discovery in Databases: European Conference,
ECML PKDD. Springer, Wurzburg, Germany (2019). https://doi.org/10.1007/
978-3-030-46147-8 5
[19] Fung, G.P.C., Yu, J.X., Lu, H., Yu, P.S.: Text classification without negative
examples revisit. IEEE Transactions on Knowledge and Data Engineering18(1),
6–20 (2006) https://doi.org/10.1109/TKDE.2006.16
26

[20] Liu, B., Yu, P., Li, X.: Partially supervised classification of text documents.
In: International Conference on Machine Learning (ICML), p. 8. AAAI press,
Washington, DC USA (2003). https://doi.org/10.1385/1-59259-358-5:387
[21] Li, X.-L., Liu, B.: Learning from positive and unlabeled examples with different
data distributions. In: Machine Learning: ECML 2005, pp. 218–229. Springer,
Porto, Portugal (2005)
[22] Li, X., Liu, B., Ng, S.-K.: Learning to identify unexpected instances in the
test set. In: International Joint Conference on Artificial Intelligence, pp. 2802–
2807. Morgan Kaufmann Publishers Inc., Hyderabad India (2007). https://api.
semanticscholar.org/CorpusID:14296672
[23] Yu, S., Li, C.: Pe-puc: A graph based pu-learning approach for text classification.
In: Machine Learning and Data Mining in Pattern Recognition, pp. 574–584.
Springer, Leipzig, Germany (2007)
[24] Yu, H., Han, J., Chang, K.C.-C.: Pebl: Positive example based learning for web
page classification using svm. In: 8th ACM SIGKDD International Conference on
Knowledge Discovery and Data Mining, pp. 239–248. ACM, Edmonton Alberta
Canada (2002). https://doi.org/10.1145/775047.775083
[25] Yu, H., Han, J., Chang, K.: Pebl: Web page classification without negative
examples. IEEE Transactions on Knowledge and Data Engineering16(2003)
https://doi.org/10.1109/TKDE.2004.1264823
[26] Peng, T., Zuo, W., He, F.: Svm based adaptive learning method for text clas-
sification from positive and unlabeled documents. Knowledge and Information
Systems16(3), 281–301 (2008) https://doi.org/10.1007/s10115-007-0107-1
[27] Li, X., Liu, B.: Learning to classify texts using positive and unlabeled data.
In: 18th International Joint Conference on Artificial Intelligence, pp. 587–594.
Morgan Kaufmann Publishers Inc, Acapulco, Mexico (2003)
[28] Li, X.-L., Liu, B., Ng, S.-K.: Negative training data can be harmful to text
classification. In: Li, H., M` arquez, L. (eds.) Empirical Methods in Natural Lan-
guage Processing, pp. 218–228. ACM, Cambridge Massachusetts (2010). https:
//aclanthology.org/D10-1022
[29] Chaudhari, S., Shevade, S.: Learning from positive and unlabelled examples using
maximum margin clustering. In: 19th International Conference on Neural Infor-
mation Processing, pp. 465–473. ACM, Doha Qatar (2012). https://doi.org/10.
1007/978-3-642-34487-9 56
[30] Uden, M.A.: Rocchio : Relevance Feedback in Learning Classification Algorithms
(2007). https://api.semanticscholar.org/CorpusID:14424311
27

[31] Ortega V´ azquez, C., Broucke, S., De Weerdt, J.: A two-step anomaly detec-
tion based method for pu classification in imbalanced data sets. Data Mining
and Knowledge Discovery37(3), 1301–1325 (2023) https://doi.org/10.1007/
s10618-023-00925-9
[32] Liu, B., Dai, Y., Li, X., Lee, W.S., Yu, P.S.: Building text classifiers using posi-
tive and unlabeled examples. In: Third IEEE International Conference on Data
Mining, pp. 179–186. IEEE, Melbourne, Florida (2003). https://doi.org/10.1109/
ICDM.2003.1250918
[33] Ke, T., Yang, B., Zhen, L., Tan, J., Li, Y., Jing, L.: Building high-performance
classifiers using positive and unlabeled examples for text classification. In: Wang,
J., Yen, G.G., Polycarpou, M.M. (eds.) Advances in Neural Networks – ISNN
2012, pp. 187–195. Springer, Shenyang, China (2012)
[34] Liu, Z., Shi, W., Li, D., Qin, Q.: Partially supervised classification – based on
weighted unlabeled samples support vector machine. In: Advanced Data Mining
and Applications, pp. 118–129. Springer, Wuhan, China (2005)
[35] Lee, W.S., Liu, B.: Learning with positive and unlabeled examples using weighted
logistic regression. In: 20th International Conference on International Conference
on Machine Learning, pp. 448–455. AAAI Press, Washington, DC USA (2003)
[36] Mordelet, F., Vert, J.-P.: Supervised inference of gene regulatory networks from
positive and unlabeled examples. Methods in molecular biology939, 47–58
(2013)
[37] Suykens, J.A.K., Vandewalle, J.: Least squares support vector machine classi-
fiers. Neural Processing Letters9(3), 293–300 (1999) https://doi.org/10.1023/A:
1018628609742
[38] Ke, T., Jing, L., Lv, H., Zhang, L., Hu, Y.: Global and local learning from positive
and unlabeled examples. Applied Intelligence48(8), 2373–2392 (2018) https://
doi.org/10.1007/s10489-017-1076-z
[39] Ke, T., Lv, H., Sun, M., Zhang, L.: A biased least squares support vector machine
based on mahalanobis distance for pu learning. Physica A: Statistical Mechanics
and its Applications509, 422–438 (2018) https://doi.org/10.1016/j.physa.2018.
05.128
[40] Hollmann, N., M¨ uller, S., Purucker, L., Krishnakumar, A., K¨ orfer, M., Hoo, S.B.,
Schirrmeister, R.T., Hutter, F.: Accurate predictions on small data with a tabular
foundation model. Nature (2025) https://doi.org/10.1038/s41586-024-08328-6
[41] Bekker, J., Davis, J.: Estimating the class prior in positive and unlabeled data
through decision tree induction. Proceedings of the AAAI Conference on Artificial
Intelligence32(1), 2712–2719 (2018) https://doi.org/10.1609/aaai.v32i1.11715
28

[42] Ramaswamy, H., Scott, C., Tewari, A.: Mixture proportion estimation via kernel
embeddings of distributions. In: Proceedings of The 33rd International Conference
on Machine Learning. Proceedings of Machine Learning Research, vol. 48, pp.
2052–2060. JMLR, New York, New York, USA (2016). https://proceedings.mlr.
press/v48/ramaswamy16.html
[43] Plessis, M.C., Niu, G., Sugiyama, M.: Class-prior estimation for learning from
positive and unlabeled data. Machine Learning106(4), 463–492 (2017) https:
//doi.org/10.1007/s10994-016-5604-6
[44] Zeiberg, D., Jain, S., Radivojac, P.: Fast nonparametric estimation of class pro-
portions in the positive-unlabeled classification setting. Proceedings of the AAAI
Conference on Artificial Intelligence34(04), 6729–6736 (2020) https://doi.org/
10.1609/aaai.v34i04.6151
[45] Plessis, M.C., Niu, G., Sugiyama, M.: Analysis of learning from positive and
unlabeled data. In: Advances in Neural Information Processing Systems, vol. 27,
p. 9. Curran Associates, Inc, Montreal, Canada (2014)
[46] Plessis, M.D., Niu, G., Sugiyama, M.: Convex formulation for learning from posi-
tive and unlabeled data. In: 32nd International Conference on Machine Learning.
Proceedings of Machine Learning Research, vol. 37, pp. 1386–1394. JMLR, Lille
France (2015)
[47] Kiryo, R., Niu, G., Plessis, M., Sugiyama, M.: Positive-unlabeled learning with
non-negative risk estimator. In: Advances in Neural Information Processing
Systems. Curran Associates Inc., Long Beach, CA, USA (2017)
[48] Su, G., Chen, W., Xu, M.: Positive-unlabeled learning from imbalanced data.
In: 13th International Joint Conference on Artificial Intelligence, IJCAI-21, pp.
2995–3001. Curran Associates, Inc, Virtual conference (2021). https://doi.org/
10.24963/ijcai.2021/412
[49] Ortega V´ azquez, C., Broucke, S., De Weerdt, J.: Hellinger distance decision trees
for pu learning in imbalanced data sets. Machine Learning113(7), 4547–4578
(2024) https://doi.org/10.1007/s10994-023-06323-y
[50] Niu, G., Plessis, M.c., Sakai, T., Ma, Y., M., S.: Theoretical comparisons of
positive-unlabeled learning against positive-negative learning. In: NIPS, p. 9.
Curran Associates Inc., Barcelona Spain (2016)
[51] Lin, T.-Y., Goyal, P., Girshick, R., He, K., Doll´ ar, P.: Focal loss for dense object
detection. IEEE Transactions on Pattern Analysis and Machine Intelligence
42(2), 318–327 (2020) https://doi.org/10.1109/TPAMI.2018.2858826
[52] Chou, Y.-T., Niu, G., Lin, H.-T., Sugiyama, M.: Unbiased risk estimators can
mislead: a case study of learning with complementary labels. In: Proceedings of
29

the 37th International Conference on Machine Learning, p. 10. JMLR, Virtual
conference (2020)
[53] Charoenphakdee, N., Vongkulbhisal, J., Chairatanakul, N., Sugiyama, M.: On
focal loss for class-posterior probability estimation: A theoretical perspective. In:
IEEE Conference on Computer Vision and Pattern Recognition. IEEE, Nashville,
TN, USA (2020)
[54] Gong, C., Wang, Q., Liu, T., Han, B., You, J., Yang, J., Tao, D.: Instance-
Dependent Positive and Unlabeled Learning With Labeling Bias Estimation .
IEEE Transactions on Pattern Analysis & Machine Intelligence44(08), 4163–4177
(2022) https://doi.org/10.1109/TPAMI.2021.3061456
[55] Yoo, J., Kim, J., Yoon, H., Kim, G., Jang, C., Kang, U.: Accurate graph-based
pu learning without class prior. In: 2021 IEEE International Conference on Data
Mining (ICDM), pp. 827–836. IEEE, Virtual conference (2021). https://doi.org/
10.1109/ICDM51629.2021.00094
[56] Saerens, M., Latinne, P., Decaestecker, C.: Adjusting the Outputs of a Classifier
to New a Priori Probabilities: A Simple Procedure. Neural Computation14(1),
21–41 (2002)
[57] du Plessis, M.C., Sugiyama, M.: Semi-supervised learning of class balance under
class-prior change by distribution matching. Neural Networks50, 110–119 (2014)
https://doi.org/10.1016/j.neunet.2013.11.010
[58] Zavitsanos, E., Kelesis, D., Paliouras, G.: Calibrating tabtransformer for financial
misstatement detection. Applied Intelligence55(1), 15 (2025)
[59] Dechow, P.M., Ge, W., Larson, C.R., Sloan, R.G.: Predicting material accounting
misstatements. Contemporary accounting research28(1), 17–82 (2011)
[60] Cecchini, M., Aytug, H., Koehler, G.J., Pathak, P.: Detecting management fraud
in public companies. Management Science56(7), 1146–1160 (2010)
[61] Zavitsanos, E., Bougiatiotis, K., Sideras, A., Paliouras, G.: Positive-unlabeled
learning for financial misstatement detection under realistic constraints. In: Pro-
ceedings of the 6th ACM International Conference on AI in Finance. ICAIF
’25, pp. 864–872. ACM, New York, NY, USA (2025). https://doi.org/10.1145/
3768292.3770366
[62] Dyck, A., Morse, A., Zingales, L.: Who blows the whistle on corporate fraud?
The journal of finance65(6), 2213–2253 (2010)
[63] Huang, X., Khetan, A., Cvitkovic, M., Karnin, Z.: TabTransformer: Tabular
Data Modeling Using Contextual Embeddings. arXiv (2020). https://doi.org/10.
48550/ARXIV.2012.06678
30

[64] Liu, H., Dai, Z., So, D., Le, Q.V.: Pay attention to mlps. In: Advances in Neural
Information Processing Systems, vol. 34, pp. 9204–9215. Curran Associates, Inc.,
Virtual conference (2021)
[65] Foster, D.J., Rakhlin, A.:ℓ ∞ Vector Contraction for Rademacher Complexity
(2019). https://arxiv.org/abs/1911.06468
[66] Bartlett, P.L., Mendelson, S.: Rademacher and gaussian complexities: risk bounds
and structural results. J. Mach. Learn. Res.3(null), 463–482 (2003)
31
