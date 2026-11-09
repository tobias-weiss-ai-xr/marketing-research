---
title: 'LambdaRankIC: Directly Optimizing Rank IC for Financial Prediction'
url: https://arxiv.org/abs/2605.00501
category: ai-marketing
subcategory: measurement
date: 2026-05
venue: ''
authors:
- Yan Lin
- Yihong Su
- Yi Yang
source: arxiv
pdf_url: https://arxiv.org/pdf/2605.00501
pages: 36
chars: 67562
fetched_at: '2026-11-08T13:28:56+00:00'
kb_version: 1
---

# LambdaRankIC: Directly Optimizing Rank IC for Financial Prediction

LambdaRankIC: Directly Optimizing Rank IC for
Financial Prediction
Yan LIN
University of Macau
yanlin@um.edu.mo
Yihong SU
University of Macau
yc47017@um.edu.mo
Yi YANG
Hong Kong University of Science and Technology
imyiyang@ust.hk
May 4, 2026
1
arXiv:2605.00501v1  [cs.LG]  1 May 2026

Abstract
In financial predictions, the performance of machine learning models is often assessed
by Rank IC, which is the Spearman rank correlation between the model predictions and
the realized asset returns. Despite its wide adoption, most existing models are trained
using regression losses or ranking objectives that may not align with Rank IC. We
proposeLambdaRankIC, a novel learning-to-rank approach that directly optimizes
Rank IC. We circumvent the non-differentiability of the ranking operator by deriving
the closed-form expression for the lambda gradients induced by the pairwise rank swaps,
which enables efficient gradient-based optimization within the LambdaRank framework.
We implement LambdaRankIC as a custom objective in XGBoost. Theoretically, we
show that our approach optimizes an upper bound on Rank IC. We evaluate the
proposed approach on both simulated and real-world financial data. In simulation
studies, LambdaRankIC accurately recovers the true ranking structure in noiseless
settings and consistently outperforms regression-based and NDCG-oriented ranking
methods under low signal-to-noise ratios and heavy-tailed noise regimes. In empirical
experiments using real market data, LambdaRankIC achieves the best out-of-sample
performance on evaluation metrics commonly used in finance, including Rank IC, ICIR,
monthly return, and Sharpe ratio. These results show that directly optimizing Rank IC
can yield substantial improvements over conventional learning objectives in financial
predictions when the full-order ranking quality is the primary goal.
Keywords:Rank IC; learning to rank; gradient boosted trees; Spearman rank correlation;
return prediction;
1 Introduction
Quantitative approaches to investment constitute a cornerstone of modern finance. Early
foundational contributions include Markowitz [1952]’s mean-variance framework for portfolio
selection and the multi-factor asset pricing models of Fama and French [1993]. More recently,
advances in machine learning have prompted both researchers and practitioners to incorporate
these data-driven methods into the design of investment strategies [Gu et al., 2020]. The
standard paradigm proceeds in two stages. First, a predictive model is trained to forecast
future stock returns. The model can be a linear model or a more complex machine learning
model (or the return model). Then in the second stage, the resulting forecast scores are used
as signals in downstream tasks such as portfolio construction, factor combination, or risk
model estimation [Grinold and Kahn, 2000].
2

However, given the extremely low signal-to-noise ratio in financial markets, the predictive
performance of the return model remains limited, even with the most advanced machine
learning algorithms. Gu et al. [2020] report monthly out-of-sample R2 values on the order
of 0.5% for their best-performing models such as gradient-boosted decision trees and neural
networks, underscoring the difficulty of predicting returns in levels. Given this low predictive
power in absolute terms, practitioners and researchers have long recognized that the relative
ranking of predicted returns carries far greater economic value than the point forecasts
themselves [Grinold and Kahn, 2000]. For example, in cross-sectional applications, factors are
commonly implemented through sorting stocks into decile portfolios based on the factor score
and forming a top-minus-bottom long–short portfolio. The standard metric for evaluating
model performance is the Rank Information Coefficient (Rank IC), defined as the Spearman
rank correlation ( ρ) between predicted and actual returns. Unlike R2, which measures the
accuracy of level predictions, Rank IC captures the model’s ability to correctly order stocks,
which is operationally relevant for most investment applications. A model that reliably places
outperformers above underperformers is valuable for portfolio construction, even if its point
estimates of return magnitudes are imprecise.
Hence, there is a misalignment between the training objective and the actual objective
that investors wish to optimize for when implementing investment strategies. The prevailing
approach in the machine learning for asset pricing literature is to train models by minimizing
mean squared error (MSE) of return predictions, yet evaluate them using Rank IC (or related,
ranking-based metrics, such as decile spread returns). This train–evaluation mismatch raises
a natural question: Can we instead train models to directly optimize Rank IC?
Directly optimizing Rank IC poses a significant challenge because Spearman’s rank
correlation is a non-differentiable function of model scores. The ranking operator that maps
continuous scores to discrete ranks has zero gradients almost everywhere. This rules out
standard gradient-based optimization, including backpropagation in neural networks. One
might hope that existing learning-to-rank methods for information retrieval could serve as
suitable surrogates for Rank IC optimization. However, a careful examination reveals that
none of the established ranking metrics and objectives align with Rank IC. Pairwise methods
such as RankNet [Burges et al., 2005] optimize a loss closely related to Kendall’s τ , which
treats all pairwise misordering errors as equally costly regardless of the magnitude of rank
displacement. This uniform pairwise weighting is misaligned with Spearman’s ρ, which
penalizes larger rank displacements more heavily. Listwise methods that optimize Normalized
Discounted Cumulative Gain (NDCG) [Burges et al., 2006, Burges, 2010] employ a position
discount that forces the model to concentrate learning effort on the top of the ranking. While
this approach might be well-suited for long-short portfolio construction [Poh et al., 2021,
3

Lin et al., 2026], it is insensitive to the quality of ordering in the middle. Other information
retrieval metrics such as MAP and ERR are designed for binary relevance ranking and
top-heavy ranking scenarios, making them fundamentally incompatible with the continuous,
symmetric, full-ranking nature of Rank IC.
In this paper, we proposeLambdaRankIC, a novel learning-to-rank objective specifically
designed to optimize Rank IC. The core of our approach is the derivation of a simple closed-
form expression for the lambda gradient of Rank IC within the LambdaRank framework.
This expression quantifies the exact change in Rank IC induced by swapping the predicted
ranks of any two arbitrary assets. These lambda gradients can then dynamically guide the
optimization process toward the true Rank IC objective, thereby effectively bypassing the
zero-gradient limitation. Theoretically, we show that our LambdaRankIC approach optimizes
an upper bound on the true Rank IC.
We implementLambdaRankICas a custom objective natively integrated into the
XGBoost library [Wu et al., 2010]. 1 We conduct extensive evaluations and benchmarks of
the proposed approach on both simulated and real-world data. Using simulated data, we
first show that, in the noise-free setting, our approach can effectively recover the ranking
structure of the underlying data-generating process. In noisy settings, we demonstrate that,
compared with both regression-based approaches and existing learning-to-rank objectives
designed to optimize NDCG, our proposed approach achieves higher Rank IC on the test set
and is more robust to overfitting. Using monthly stock data, we benchmark our approach
against two broad classes of existing methods: (1) approaches that first predict returns and
then construct portfolios, and (2) approaches that directly optimize ranking metrics for stock
returns using existing learning-to-rank objectives. We show that our approach achieves the
highest out-of-sample Rank IC and ICIR among all competing models. In terms of portfolio
performance, our approach delivers significantly higher returns and a higher Sharpe ratio.
The remainder of this paper is organized as follows. Section 2 reviews related work on
machine learning for asset pricing and learning-to-rank methods. Section 3 formulates the
problem and Section 4 presents the derivation of LambdaRankIC objective, its implementation,
as well as the theoretical justification. Section 5 reports the results from our simulations.
Section 6 reports the benchmark results using real financial data. Section 7 concludes and
outlines directions for future research.
1Although this paper focuses on tree-based models, the proposed objective can also be extended to neural
networks.We focus on tree-based models because they are the workhorse of modern financial applications and
remain among the best-performing approaches for tabular data, achieving performance comparable to that of
neural networks and transformer-based models [Gorishniy et al., 2021, Bryzgalova et al., 2025, Cong et al.,
2025].
4

2 Background and Related Work
2.1 Machine Learning in Finance
Machine learning in Finance builds on the broader evidence that asset returns are predictable
from characteristics [Fama and French, 1993, Harvey et al., 2016]. Empirical evidence docu-
ments that nonlinear models can improve model performance relative to linear benchmarks.
For example, in a large-scale comparison, Gu et al. [2020] show that tree-based and neural
network-based models are consistently competitive for cross-sectional return prediction. Leip-
pold et al. [2022] report similar results in international markets. Feng et al. [2024] and Gu et al.
[2021] demonstrate performance gains from nonlinear representation learning. Researchers
have also explored the applications of more advanced approaches, such as Transformer-based
models [Kelly et al., 2025], graph neural networks [Tian et al., 2022], generative adversarial
networks [Chen et al., 2024], and deep reinforcement learning [Cong et al., 2021]. Among
these models, tree models have gained much attention due to their vast success in tabular
datasets [Gorishniy et al., 2021] and efficiency in model training. For example, Cong et al.
[2025] adapt the tree split criterion using financial metrics, while Bryzgalova et al. [2025] use
trees to group a series of stocks to span SDF.
Machine learning models have also been used for risk management in finance, particularly
for predicting stock price volatility. For example, Yang et al. [2022] propose a knowledge-driven
approach leveraging textual data in financial reports for volatility prediction. Zhang et al.
[2024] design a neural network with a long- and short-term memory retrieval architecture
to model market volatility. He et al. [2025] leverage the unique structure in earnings
conference call transcripts and propose a novel divide-and-contrast machine learning method
for predicting firm risks.
In the literature, the standard empirical workflow for modeling and investing remains
largely decoupled. Models are typically trained to minimize a generic prediction loss (for
example, Mean Squared Error of the stock return). Then, the resulting forecasts are
subsequently mapped into portfolio rankings or allocation rules. Recent studies suggest
that such a predict–then–rank design can be suboptimal when the ultimate objective is
cross-sectional ordering rather than point prediction. In this spirit, Butler and Kwon [2023],
Cong et al. [2021], and Costa and Iyengar [2023] propose end-to-end frameworks that more
tightly couple prediction and portfolio choice. Our paper echoes their call for a better
alignment between the training objective and investment by directly optimizing Rank IC, a
metric that is directly related to asset ranking.
5

2.2 Learning to Rank and Its Applications to Finance
Learning-to-Rank algorithms (LTR), originally developed for information retrieval and recom-
mender systems, have been increasingly recognized for their potential in financial applications.
LTR algorithms are generally categorized into three paradigms [Liu, 2009]: pointwise, pairwise,
and listwise. Pointwise approaches treat each item independently, making the ranking task
to standard regression or classification. Pairwise methods instead model relative preferences
between item pairs, optimizing the ordering of pairwise comparisons [Burges et al., 2005,
Freund et al., 2003]. Listwise approaches directly optimize a list-level objective that evaluates
the entire ranked list at once [Cao et al., 2007, Xia et al., 2008].
These algorithms are typically evaluated using ranking-specific metrics. The most widely
adopted include Normalized Discounted Cumulative Gain (NDCG), Mean Average Precision
(MAP), and Expected Reciprocal Rank (ERR). Among these, NDCG at position k is defined
as:
NDCG@k= DCG@k IDCG@k ,DCG@k=
kX
r=1
g(yr)
log2(1 +r) ,(1)
whereg(y) is the gain function (typically 2 y −1) and IDCG is the ideal (maximum) DCG.
Several studies have applied learning-to-rank methods to the finance domain, arguing that
traditional “regress-then-rank” approach is sub-optimal because they minimize pointwise
prediction error rather than explicitly learning the relative ordering of asset returns. For
example, Poh et al. [2021] enhanced cross-sectional momentum strategies by applying various
LTR algorithms to rank assets directly. They demonstrate that LTR algorithms improve the
trading performance measured in terms of Sharpe Ratio compared to traditional predict-then-
rank approaches. Song et al. [2017] combined LTR algorithms with news sentiment indicators
for stock portfolio selection, showing that RankNet and ListNet produce robust rankings
under different market conditions. Feng et al. [2019] proposed a Temporal Relational Ranking
framework that incorporates inter-stock relations through temporal graph convolutions,
formulating stock prediction as a ranking task to capture time-sensitive dependencies across
assets. Ma and Tan [2022] proposed a deep multi-task learning framework (MTSR) that
stabilizes and guides the training of complex listwise stock ranking models by leveraging
auxiliary tasks to address the training difficulties inherent in small-sample, high-dimensional
financial data. Zhang et al. [2022] developed the ListFold algorithm, a listwise loss function
that simultaneously emphasizes both the top and bottom of the ranked list to better align
with the needs of long-short portfolio construction. Saha et al. [2021] adopted a listwise
approach using top-k probability distributions. More recently, Lin et al. [2026] provides the
first systematic investigation of the performance of all three learning -to-rank methods based
6

on an extensive set of firm characteristics spanning three decades. The authors compare
these methods with traditional regression and probabilistic models and develop a dual -ranker
framework to mitigate the algorithms’ heavy emphasis on top-ranked items.
Despite these advances, all existing LTR applications in finance inherit ranking metrics
from information retrieval as their optimization targets, such as NDCG. However, NDCG is
a position-discounted, top-heavy metric that concentrates signal on items near the top of the
list, which is misaligned with the needs of cross-sectional asset pricing, where ranking quality
across all positions in the cross-section matters. None of the aforementioned studies consider
optimizing Rank IC, which is the standard evaluation metric used by quantitative portfolio
managers and factor investors. This gap motivates our development of LambdaRankIC.
3 Problem Formulation
3.1 Setup and Notation
We formulate our problem as ranking stocks in the cross-section (e.g., monthly), similar to
[Gu et al., 2020]. In practice, this is analogous to predicting the next-period stock returns
(or the ranking of stock returns). Periodically, investors build a model to generate investment
signals. This signal is then used in the downstream task to form investment strategies. One
naive strategy would be going long (buying) assets with the highest scores and shorting
(selling) assets with the lowest scores, subject to some constraints [Coqueret and Guida,
2020]. While we formulate the problem as a cross-sectional prediction problem, it can be
easily extended to incorporate time-series information or time-series prediction, as long as
the problem involves ranking a group of assets.
Let G = {G1, . . . , Gm, . . . , GM } denote M groups (e.g., months), where group Gm contains
nm items (e.g., the universe of stocks in a month). 2 Each item i∈G m is associated with a
feature vectorx im ∈R d and a real-valued label yim ∈R representing its future return. 3 A
parameterized modelf θ :R d →Rassigns a scores im =f θ(xim) to each item.
Learning to RankCollecting the scores sim in month m into a vectors m and the
corresponding labels yim intoy m, and defining a loss function l that takes the labels and
2In the learning to rank literature, this is called a query.
3This corresponds to the relevance score in the learning to rank literature. In the factor synthesis literature,
f is sometimes called thecomposite signaloralpha score[Tulchinsky, 2019]; here we treat it as a generic
scoring function learned by the model.
7

scores and outputs a real value, the total loss is:
L= 1 M X m l(ym,s m) (2)
A learning-to-rank algorithm finds the optimalfthat minimizes the total loss:
ˆf= arg min
θ
L(3)
3.2 Rank IC (Spearman Rank Correlation)
Definition 1(Predicted rank and label rank).Within groupG m of sizen: 4
• Thepredicted rank ˆri ∈ {1, . . . , n}is the position of item i when items are sorted by
scores i in descending order (rank 1 = highest score).
• Theactual rank ˜yi ∈ {1, . . . , n}is the position of item i when items are sorted by label
yi in descending order (rank 1 = highest label). We assume no ties. Ties are broken by
the original data index.
Definition 2(Rank IC).For a group of n assets with predicted ranks ˆr= (ˆr1, . . . ,ˆrn) and
label ranks ˜y= (˜y1, . . . ,˜yn), the Spearman rank correlation [Spearman, 1904] is:
ρ= Cov(ˆr,˜y) σˆrσ˜y (4)
Equation (4) is a shorthand for the Pearson correlation between the two rank vectors when
there are no ties in either ranking. In the finance literature, ρ computed cross-sectionally
each period and averaged over time is called theRank Information Coefficient(Rank IC).
4 The LambdaRankIC Objective and Its Implementa-
tions
4.1 LambdaRank Framework and LambdaMART
Before deriving the LambdaRankIC objective, we first describe the LambdaRank framework
and LambdaMART algorithm, which form the basis of our approach. The LambdaRank
framework follows a probabilistic pairwise setup [Burges, 2010, Burges et al., 2006]. For a
4We drop the subscriptmfor brevity.
8

given pair of items ( i, j) with feature vectorsx i, xj ∈R d, a learning-to-rank function f maps
their features into scores si = f (xi) and sj = f (xj). The score difference is then mapped to a
probability via a sigmoid function:
Pij ≡P(s i > sj) = 1 1 +e −σ(si−sj ) ,(5)
where σ is a shape parameter controlling the steepness of the sigmoid, and Pij denotes the
modeled probability that item i should be ranked above item j. The cost function is then
written as the cross-entropy betweenP ij and the target probability:
C=− ¯Pij logP ij −(1− ¯Pij) log(1−P ij),(6)
where ¯Pij is the target (ground-truth) probability that item i ranks above item j (e.g., ¯Pij = 1
if i is ranked higher than j, ¯Pij = 0 if j is ranked higher, or ¯Pij = 0.5 if tied). The gradient
with respect tos i is:
∂C
∂si
=σ( ¯Pij −P ij) =− ∂C ∂sj ≡λ ij (7)
Equation 7 is the original RankNet gradient [Burges et al., 2005], which can be directly
optimized via gradient descent. The challenge is that there is a disconnect between the
loss function in Eq. (6) and the evaluation metrics, such as the Normalized Discounted
Cumulative Gain (NDCG). Typically, these evaluation metrics are based on the sorted ranking
of items, which are generally non-differentiable with respect to model parameters. Burges
et al. [2006] show that scaling λij by the change in the target metric when swapping items
i and j provides a good approximation to the gradient of the target metric. For example,
when the target metric is NDCG, the scaled lambda is:
λ′ ij =λ ij ·∆NDCG ij (8)
where ∆NDCGij is the absolute change in NDCG when items i and j are swapped. This
is the LambdaRank algorithm. Although originally developed for NDCG, Donmez et al.
[2009] empirically show that the approach extends to other non-differentiable rank metrics
such as Mean Average Precision (MAP) and Mean Reciprocal Rank (MRR). The original
LambdaRank algorithm was developed for neural networks. Its tree-based counterpart,
LambdaMART [Friedman, 2001], has a standard implementation in XGBoost [Chen and
Guestrin, 2016]. However, none of the standard implementations support Rank IC as the
target metric, which motivates our work. In the following section, we derive ∆RankIC for
use in the LambdaRank framework.
9

4.2 Derivation of∆RankIC
We now derive the closed-form expression for the change in Rank IC when two items are
swapped.
Lemma 1(Variance of uniform ranks).Fornconsecutive integers{1,2, . . . , n},
Var(1, . . . , n) =n2 −1 12 .(9)
Using Lemma 1, the Spearman rank correlation can be rewritten as the Pearson correlation
between predicted ranks ˆrand true ranks ˜y:
ρ= Cov(ˆr,˜y) σˆrσ˜y = Cov(ˆr,˜y) Var(1, . . . , n)= 1 n Pn i=1 ˆri ˜yi −¯r¯˜y (n2 −1)/12 = 12(Pn i=1 ˆri ˜yi −n¯r¯˜y) n(n2 −1) ,(10)
where ¯r= ¯˜y= (n+ 1)/2, since both rank vectors are permutations of{1, . . . , n}.
Proposition 1(∆RankIC).Let item i have predicted rank ˆri and actual rank ˜yi, and let item
j have predicted rank ˆrj and actual rank ˜yj. After swapping items i and j in the predicted
ranking (soimoves toˆr j andjmoves toˆr i), the change in Rank IC is:
∆RankIC= 12|ˆrj −ˆri||˜yi −˜yj| n(n 2 −1) . (11)
Proof. From Eq. (10), the numerator of ρ depends only on D = Pn i=1 ˆri ˜yi, given a fixed
group. Expanding:
D= ˆr1 ˜y1 +· · ·+ ˆri ˜yi +· · ·+ ˆrj ˜yj +· · ·+ ˆrn ˜yn.
After swappingiandj:
D′ = ˆr1 ˜y1 +· · ·+ ˆrj ˜yi +· · ·+ ˆri ˜yj +· · ·+ ˆrn ˜yn.
Hence:
∆D=D ′ −D= (ˆrj −ˆri)˜yi + (ˆri −ˆrj)˜yj = (ˆrj −ˆri)(˜yi −˜yj).(12)
Since the denominator n(n2 − 1)/12 and the term n¯r¯˜yare invariant to any permutation of
the predicted ranking, we have:
∆RankIC =|∆ρ|=| 12D ′
n(n2 −1) − 12D n(n2 −1) |= 12|∆D| n(n2 −1) = 12|ˆrj −ˆri| |˜yi −˜yj| n(n 2 −1) .(13)
10

Equation (11) has an intuitive interpretation. The magnitude of improvement on Rank IC
from swapping i and j is determined by how far apart the two items are in the predicted
ranking (ˆrj −ˆri) and their actual rank separation (˜yi −˜yj).
Comparison with LambdaRank with NDCG objective (LambdaRank-NDCG)In
LambdaRank with NDCG as the objective, the scaling factor is:
∆NDCGij =| 2yi −2 yj
IDCG || 1 log2(1 + ˆri) − 1 log2(1 + ˆrj) |.(14)
Since the NDCG discount function 1 /log 2(1 + r) is convex and monotonically decreasing in
r, the difference

1
log2(1+ˆri) − 1 log2(1+ˆrj )

is substantially larger for swaps near the top of the
ranked list than for swaps at lower positions. Consequently, the resulting λ gradients are
concentrated on top-ranked items, making LambdaRank-NDCG inherently top-heavy.
Table 1 compares the scaling factor ∆ for the two existing LambdaRank objectives in
XGBoost and our proposed objective. ∆RankIC can be computed in O(1) time and is easily
integrated as an extension of existing objectives. Algorithm 1 shows the gradient computation
loop implemented in XGBoost.
Table 1: Comparison of LambdaRankIC and Existing Approaches
Objective ∆ (Scaling Factor) Pair Weighting Portfolio Alignment
rank:pairwise1 Uniform equal weight for all misordered pairs
rank:ndcg |2yi −2 yj | IDCG | 1 log2(1 + ˆri) − 1 log2(1 + ˆrj) |Concentrated at top ranks Optimizes head of ranking
rank:ic(ours) 12|ˆrj −ˆri||˜yi −˜yj| n(n2 −1) Proportional to rank separation Directly optimize for Rank IC
4.3 Theoretical Justification of LambdaRankIC
One of the limitations of LambdaRank is that, although it works empirically well [Donmez
et al., 2009], there is no guarantee that weighting λ with the change of ranking metric (e.g.,
∆RankIC) from a pairwise swap can optimize the global ranking metrics. In this section, we
provide some theoretical justification of LambdaRankIC based on the LambdaLoss framework
[Wang et al., 2018]. The paper establishes that LambdaRank is a special configuration of the
LambdaLoss framework. More importantly, LambdaRank with ∆ NDCG weighting optimizes
a coarse upper bound on global NDCG. In what follows, we show that, by weighting λ
with ∆RankIC, the LambdaRankIC algorithm optimizes an upper bound on 1 −ρ , so that
minimizing the LambdaRankIC loss indirectly maximizes Rank IC. We first introduce the
11

Algorithm 1LambdaRank with RankIC
Require:Predictionss, labelsy, learning rateη, featuresx
▷Pre-processing
1:foreach groupgin parallel do
2:Stable-sort elements in groupgby label in descending order
3:Assign ranks 1,2, . . .in sorted order as label ranks ˜y
4:end for
▷Boosting loop
5:foriteration = 1toMaxIterdo
6:foreach groupgin parallel do
7:n←number of elements in groupg
8:Sort elements in groupgby prediction scoresin descending order
9:Obtain predicted ranks ˆrfrom the sorted order
10:Initializeλ i ←0, h i ←0 for alliin groupg
11:foreach pair (i, j) sampled fromgdo
12:if˜y i <˜yj then
13:swap(i, j)▷Ensure ˜y i ≥˜yj
14:end if
15:∆← 12 (ˆrj −ˆri) (˜yi −˜yj) n(n2 −1)
16:p←σ(s i −s j)
17:λ ij ←(p−1)· |∆|
18:h ij ←2p(1−p)· |∆|
19:λ i +=λ ij;λ j −=λ ij
20:h i +=h ij;h j +=h ij
21:end for
22:end for
23:Fit treeTusing{(x i, λi, hi)}for alli ▷Tree fitting and score update
24:s i ←s i +η·T(x i) for alli
25:end for
LambdaLoss framework and establish how LambdaRankIC relates to it. We then show that
the LambdaRankIC loss is an upper bound on 1−ρ.
4.3.1 The LambdaLoss Framework
Following Wang et al. [2018], in Eq. (2),l(y m,s m) can be written as
l(y,s) =−log 2 P(y|s) =−log 2
X
π∈Π
P(y|s, π)P(π|s) (15)
where π is a (latent) ranked list and P (π|s) is the distribution conditional ons. We drop the
subscript m and useyandsfor brevity. Eq. (15) is the loss function in the LambdaLoss
12

framework. While Eq. (15) is not convex in general, it can be minimized by the expectation
maximization algorithm [Dempster et al., 1977]. Essentially, the procedure starts with a
random guess of the model parameter θ and iterates over the E-step and M-step: at the
E-step, the distribution of the latent variable π is estimated based on the current model f (t);
at the M-step, the model parameters are updated by minimizing the expected loss. Wang
et al. [2018] shows that LambdaRank is a special case under the LambdaLoss framework
with two choices forP(y|s, π) andP(π|s):
Hard assignmentLambdaRank adopts hard assignment distribution H(π|s) to replace
P (π|s). H(π|s) assigns probability one to the ranked list ˆπobtained by sorting items by
decreasing scoress, and zero to all other permutations. In this case,
l(y,s) =−log 2 P(y|s,ˆπ) (16)
Generalized Bradley–Terry LikelihoodFor items (assets) i and j, with respective
labels (i.e., returns)y i andy j, and ranks ˆπi and ˆπj, we define
P(y|s,ˆπ) =
Y
yi>yj
P(y i > yj |s i, sj,ˆπi,ˆπj) (17)
where
P(y i > yj |s i, sj,ˆπi,ˆπj) =
 1
1 +e −σ(si−sj )
ωij (ˆπi,ˆπj ,yi,yj ,si,sj )
(18)
and the exponentω ij(·) is the scaling factor (∆) given in Table 1.
For example, whenω ij(·) = 1,
l(y,s) =
X
yi>yj
log2

1 +e −σ(si−sj ) .
This is the pairwise LambdaRank loss. When ωij(·) = ∆NDCG, as defined in Eq. (14), the
resulting loss is the one used in LambdaRank with the NDCG objective.
Definition 3(LambdaRankIC Loss).Under the LambdaLoss framework, letting ωij(·) =
∆ RankIC gives us the loss optimized in our LambdaRankIC algorithm. Formally, let ˜y
represent the true ranks presorted by the true label valuesy, as defined in Eq. (10) and let ˜yi
and ˜yj denote the true ranks of items i and j, respectively, where rank 1 is the most relevant
and larger rank values indicate lower relevance. Replacing ˆπi, ˆπj with ˆri and ˆrj for notation
13

consistency with Eq. (10), as they represent predicted ranks based on model scores, we have
ωij(.) = ∆RankIC= 12|ˆrj −ˆri| |˜yi −˜yj| n(n2 −1) (19)
Hence,
lC(y,s) =
X
yi>yj
12|ˆrj −ˆri| |˜yi −˜yj|
n(n2 −1) log2

1 +e −σ(si−sj ) (20)
Eq. (20) is the loss function we are optimizing under the LambdaLoss framework. We call it
theLambdaRankIC Loss.
4.3.2 LambdaRankIC Loss as an Upper Bound
We now examine to what extent the LambdaRankIC loss is related to the true RankIC. As
we shall see, the LambdaRankIC loss is an upper bound on 1−ρ.
Proposition 2(RankIC loss).Let the rank of item i be written as ˆri = 1 + P j̸=i Isi<sj ,
where Isi<sj is the indicator function equal to 1 when si < sj and zero otherwise. Defining
the RankIC loss as1−ρ, we have:
1−ρ= 12 n(n2 −1) X ˜yi<˜yj (˜yj −˜yi)I si<sj (21)
The proof of Proposition 2 can be found in the appendix. Proposition 2 expresses 1 −ρ
as a sum over discordant pairs weighted by the true rank separation ( ˜yj −˜yi). Hence swaps
between items far apart in true relevance contribute more to the cost than swaps between
similarly ranked items. Isi<sj can also be viewed as the zero–one loss, which is bounded above
by the logistic loss [Wang et al., 2018]:
Isi<sj ≤log 2

1 +e −σ(si−sj ) (22)
Hence, we have:
1−ρ≤ 12 n(n2 −1) X ˜yi<˜yj (˜yj −˜yi) log 2  1 +e −σ(si−sj ) =l sg (23)
Eq. (23) establishes that lsg is the logistic surrogate of the RankIC loss 1 −ρ . Assuming no
14

ties in scores, it directly follows that
1−ρ≤l sg = 12 n(n2 −1) X ˜yi<˜yj 1|{z} |ˆrj −ˆri|≥1 ·(˜yj −˜yi) log 2  1 +e −σ(si−sj )
≤ 12 n(n2 −1) X ˜yi<˜yj |ˆrj −ˆri| |˜yj −˜yi|log 2  1 +e −σ(si−sj ) =l C,(24)
given that |ˆrj −ˆri| ≥1 for all pairs when there are no ties in scores. Eq. (24) establishes
that the LambdaRankIC lossl C is an upper bound on 1−ρ.
5 Simulations
Noiseless Convergence CheckWe first evaluate LambdaRankIC on simulated data with
a known ground-truth signal. This allows us to study convergence behavior and sensitivity to
distributional assumptions in a controlled setting. We generate a panel of T = 120 monthly
cross-sections (i.e., groups), each containing N = 500 stocks. The target return for stock i in
the next periodt+ 1 is given by
yi,t+1 =f(x i,t) +ε i,t+1,(25)
where f is a deterministic signal function,x i,t is a 10-dimensional feature vector, and εi,t+1 is
the noise term. Both the features and the noise term are drawn i.i.d. from N (0, 1). Further,
we let f (xi,j) = β⊤xi,j, where β∈R p is a fixed unit-norm coefficient vector drawn once from
N (0, I). The first 80 periods serve as the training set and the remaining 40 periods as the
test set.
We first verify that our custom LambdaRankIC implementation can recover the ranking
structure implied by the data-generating process (DGP) by conducting a noiseless convergence
check. Specifically, we remove the noise term and set the learning target to yi,t+1 = f (xi,t).
We then train the model for 1,000 boosting rounds and repeat the experiment across 10
random seeds.
15

Figure 1: Convergence without Noise
25 50 75 100 125 150 175 200
Boosting Round
0.725
0.750
0.775
0.800
0.825
0.850
0.875
0.900
0.925Rank IC
Convergence Curve
Test IC
Train IC
25 50 75 100 125 150 175 200
Boosting Round
0.000
0.005
0.010
0.015
0.020Train IC - Test IC
Training-Test Gap
Train-Test Gap
Noiseless Validation
Notes.For readability, we plot only the first 200 boosting rounds. Learning rate = 0 .01, maximum depth = 6.
Figure 1 reports the convergence curves in the noiseless setting. In the left panel, the
model learns the noiseless ranking structure steadily and consistently. Averaged across seeds,
the test Rank IC increases from 0 .772 at boosting round 1 to 0 .949 at round 1000, while
the corresponding training Rank IC increases from 0 .780 to 0 .953 over the same period.
Importantly, the train–test gap shown in the right panel remains small throughout training,
rising modestly early on before narrowing steadily, from about 0.008 at round 1 to about 0.004
by round 1000. Overall, these dynamics suggest that the remaining gap to perfect ranking is
unlikely to be driven by severe overfitting. Taken together, these results provide a strong
implementation sanity check. In the absence of noise, the objective steadily recovers the true
ranking structure and achieves a mean best test Rank IC of 0 .949 (standard deviation 0 .004).
Moreover, the best performance is attained essentially at the final boosting round across all
seeds.
Convergence under Different Signal-to-Noise RegimesNext, we evaluate the model’s
convergence performance with more realistic noisy data across different signal-to-noise regimes.
We increase the dimensionality ofx i,t to p = 100 features. We calibrate the noise variance so
that the signal-to-noise ratio SNR≡Var (f )/Var(ε) takes one of three target values: High
(SNR = 2.0), Medium ( SNR = 0.5), or Low ( SNR = 0.1). The Low regime aims to simulate
realistic equity return prediction, where monthly out-of-sample R2 values are typically below
1% [Gu et al., 2020].
We train the model with different learning rates ( η∈ {0.001, 0.01, 0.1}), boosted for 200
rounds, with all other hyperparameters held fixed. Each configuration is repeated across
10 random seeds. The evaluation metric is the cross-sectional Rank IC (Spearman rank
16

correlation between predicted and realized returns), averaged across all test-set periods.
Figure 2 reports convergence curves for the p = 10 DGP (Panel (a)) and the more challenging
p = 100 DGP (Panel (b)). Across both panels, the learning dynamics are consistent: larger
learning rates produce faster improvement and higher test Rank IC within the fixed budget
of 200 boosting rounds. For p = 10, the pattern is clear under all SNR regimes: η = 0.1
consistently achieves the highest end-of-training test Rank IC, followed by η = 0.01, while
η = 0.001 remains undertrained. Across SNR regimes, end-of-training test Rank IC declines
as the problem becomes harder (lower SNR). For example, in the high-SNR setting, the end
Rank IC is close to 0.9, whereas in the low-SNR setting it falls below 0.3.
Panel (b) shows the same qualitative pattern but at a lower performance level, reflecting
the increased difficulty of the p = 100 setting. When p = 100, all curves shift downward and
the performance gap across learning rates widens substantially. In particular, the smaller
learning rates ( η = 0.001 and η = 0.01) remain far from the best-performing trajectory even
at round 200, indicating undertraining under the fixed boosting budget. The largest learning
rate, η = 0.1, remains the strongest choice in all three SNR regimes, although its curve is
still rising at the final round, suggesting that convergence is not yet fully saturated.
In Panel (c), we report the train–test gap for the hardest setting ( p = 100, low SNR)
under various learning rate settings ( η∈ {0.001, 0.01, 0.1}). Even in this regime, the model
still learns meaningful ranking structure, as both training and test Rank IC increase over
boosting rounds across all three learning rates. For larger learning rates ( η = 0 .01 and
η = 0.1), improvement in test Rank IC eventually plateaus while the train–test gap widens,
indicating progressive overfitting.
17

Figure 2: Convergence Curves under Different Signal-to-Noise Ratio (SNR) Conditions
25 50 75 100 125 150 175 200
Boosting Round
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9Test Rank IC
High SNR (SNR = 10)
25 50 75 100 125 150 175 200
Boosting Round
Medium SNR (SNR = 1)
25 50 75 100 125 150 175 200
Boosting Round
Low SNR (SNR = 0.1)
lr=0.001 lr=0.01 lr=0.10
(a) Convergence curves with 10 features
25 50 75 100 125 150 175 200
Boosting Round
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8Test Rank IC
High SNR (SNR = 10)
25 50 75 100 125 150 175 200
Boosting Round
Medium SNR (SNR = 1)
25 50 75 100 125 150 175 200
Boosting Round
Low SNR (SNR = 0.1)
lr=0.001 lr=0.01 lr=0.10
(b) Convergence curves with 100 features
(c) Train–test gap across different learning rate settings (Low SNR, 100 features)
Notes.(1) In all the plots, the y-axis is the test Rank IC, while the x-axis is the boosting runs. (2) In Panel
(a) and Panel (b), columns correspond to High, Medium, and Low SNR. (3) In Panel (C) columns correspond
to different learning rate settings. (4)Shaded regions show±1 standard deviation across 10 seeds.
Comparison with Existing Approaches in Financial PredictionIn the previous two
experiments, we assumed Gaussian noise. In practice, however, asset returns often exhibit
heavy tails and excess kurtosis [Cont, 2001, Harvey et al., 2016]. To better reflect this reality
18

and investigate whether the proposed approach is more robust to heavy-tailed noise, our final
simulation compares the proposed LambdaRankIC objective with two existing approaches
under a heavy-tailed DGP: LambdaRank with NDCG objective and squared-error regression.
Specifically, we consider a linear DGP with p = 100 features. We let εi,t+1 in Eq. (25) follow a
Student-t distribution with 5 degrees of freedom and rescale it to achieve the target SNR level.
We then train the same XGBoost model with different objectives: rank:ic, rank:ndcg, and
reg:squarederror, while keeping the tree structure and boosting hyperparameters constant.
Figure 3: Comparison with Existing Approaches
(a) Convergence curves
200 400 600 800 1000
Boosting Round
0.4
0.5
0.6
0.7
0.8
0.9
1.0Rank IC
LambdaRankIC
T est IC
Train IC
200 400 600 800 1000
Boosting Round
LambdaMART­NDCG
T est IC
Train IC
200 400 600 800 1000
Boosting Round
MSE
T est IC
Train IC
Train vs T est IC (Linear, Medium SNR, Student­t noise)
(b) Train-test Gap: Medium SNR
Notes.(1) Panel (a) shows the convergence curves across different signal-to-noise regimes. (2) Panel (b)
shows train-test gap of the three learning objectives under the medium signal-to-noise regime.
Figure 3 presents the learning curves and train–test gaps of the three models over 1000
boosting rounds, allowing us to examine both convergence dynamics and generalization
behavior. Table 2 reports the corresponding peak test Rank IC values. The results support
two related conclusions. First, the ranking-based objectives are more robust in the heavy-
tailed, low-SNR regime, which is more representative of real-world financial data. As shown
in Figure 3, the model with MSE objective peaks in early training rounds, and its train–test
19

gap is substantially larger than those of the two ranking-based objectives in the low-SNR
setting. Consistently, Table 2 shows that MSE achieves a lower peak Rank IC (0.2480)
than LambdaRankIC (0.2803). This pattern suggests that MSE is more prone to overfitting
and more sensitive to heavy-tailed noise. Second, comparing the two rank-based objectives,
LambdaRankIC substantially outperforms LambdaRank-NDCG in test Rank IC. This is
consistent with the fact that the NDCG objective optimizes a top-heavy ranking criterion,
whereas our target metric is full cross-sectional Rank IC.
One might argue that the higher peak Rank IC achieved by MSE and NDCG in high and
medium SNR regimes suggests that the superiority of LambdaRankIC is confined solely to
low-SNR environments. However, as shown in Table 2, LambdaRankIC reaches its highest
Rank IC at the 999th iteration, which is close to the predefined upper limit (1000) for
boosting rounds. This fixed budget constraint suggests that the model has not yet fully
converged, and that performance may improve further with additional boosting rounds.
Furthermore, even under this constrained training setup, the gap between the highest overall
peak Rank IC and that of LambdaRankIC is marginal (less than 0.05), indicating no significant
underperformance by our proposed method.
In summary, our simulations show that the proposed LambdaRankIC objective offers clear
advantages over existing methods. Compared with the common practice of predicting return
levels using MSE loss, LambdaRankIC is less prone to overfitting and is less sensitive to
noise, especially in challenging low-SNR regimes. Our results also indicate that off-the-shelf
ranking objectives are often top-heavy, emphasizing only the highest-ranked items. This
objective mismatch leads to lower out-of-sample Rank IC.
Table 2: Peak Test Rank IC
LambdaRankIC NDCG MSE
SNR Peak IC Peak Round Peak IC Peak Round Peak IC Peak Round
High 0.8207 999 0.6697 5680.8666235
Medium 0.6344 665 0.5165 964.50.646798.5
Low0.2803171 0.2381 691.5 0.2480 38
6 Benchmarking with Real Financial Data
6.1 Dataset and Experimental Protocol
We evaluate the proposed methods in real financial predictions. We set up the task by
generating investment signals for the next period. The raw signal is calculated from the
20

next-period excess return, defined as
ri,t+1 = pi,t+1 −p i,t
pi,t
−r f t+1 (26)
where pit is the stock price and rf t+1 is the risk-free rate. For regression-based models, this is
the prediction target. For learning-to-rank models, this is the label for ranking.
The dataset is constructed from Green et al. [2017] and contains 94 monthly firm-level
characteristics. Following common practice in the empirical asset pricing literature [Kelly
et al., 2019, Gu et al., 2020], we transform each characteristic into its cross-sectional rank.
After dropping observations with missing values, the data contains 2,746,083 stock-month
observations spanning 21,396 securities from January 1964 to December 2024. All models are
trained and evaluated under the same rolling-window protocol. In each window, we use 120
months for training, 60 months for validation, and 12 months for testing, then advance the
window by 12 months. The validation period is used for hyperparameter tuning.
We compare our method against three regression-based benchmarks: ordinary least-
squares (OLS) regression, XGBoost regression with MSE loss ( reg:squarederror), and
neural-network regression. OLS and neural-network models are implemented with scikit-learn.
For the neural-network baseline, we use a three hidden layer architecture following Gu et al.
[2020], with hidden layer sizes of 32, 16, and 8. We also compare our LambdaRankIC
approach against two off-the-shelf learning-to-rank methods using XGBoost’s LambdaRank
implementation: standard pairwise ranking ( rank:pairwise) and NDCG-optimized ranking
(rank:ndcg). The regression baselines are trained on raw future excess returns. The learning-
to-rank models use the same inputs and training, validation, and test splits, but we treat
each month as one group for ranking (i.e., one query).
We report four ranking metrics: average monthly Rank IC ( IC ), its standard deviation
Std(IC ), ICIR = IC /Std(IC ), and NDCG@100. We also report portfolio-based performance.
Specifically, following the existing literature [Gu et al., 2020], each month we sort assets into
deciles based on model scores and construct a value-weighted long–short portfolio that buys
the top decile and sells the bottom decile, rebalanced monthly. We report the portfolio’s
average monthly return ( Return), volatility ( Vol.), annualized Sharpe ratio ( Sharpe), and
maximum drawdown (MDD). All metrics except the Sharpe ratio are reported as percentages.
6.2 Results
Table 3 reports the consolidated out-of-sample benchmark results. The results support the
conclusion that directly optimizing an IC-aligned objective yields the best cross-sectional
21

Table 3: Out-of-sample Benchmark Results
Ranking Metrics Portfolio Returns
Method IC↑Std(IC)↓ICIR↑NDCG@100↑Return (%)↑Vol. (%)↓Sharpe↑MDD (%)↓
Regression-based
OLS Regression 0.0471 0.0706 0.6663 0.5077 0.97 4.56 0.74043.78
XGBoost Regression 0.0418 0.0917 0.4561 0.4924 1.25 6.21 0.696 58.29
MLP Regression 0.04280.05310.8059 0.4967 1.084.520.831 46.28
Learning-to-rank-based
Pairwise 0.0828 0.1153 0.7181 0.5328 1.42 8.68 0.566 81.59
NDCG 0.0863 0.1063 0.8122 0.5312 1.20 8.32 0.501 83.24
RankIC (ours)0.11480.11141.0308 0.5415 2.228.310.92364.29
Notes.(1) ↑ (↓) indicates higher (lower) is better;boldmarks the best value in each column.
(2) Ranking metrics are computed from next-month model predictions. (3) Portfolio metrics
are based on value-weighted top-minus-bottom decile returns formed monthly using model
scores. (4) Return, volatility, and maximum drawdown are reported in monthly percent. (5)
Sharpe ratios are annualized: Sharpe =Return/V ol.×
√
12.
ranking performance. Our approach (RankIC) is the strongest model on three of the four
ranking metrics: it attains the highest average IC, the highest ICIR, and the best NDCG@100.
Compared with the regression-based methods, learning-to-rank methods overall achieve higher
average IC, ICIR, and NDCG@100. Both pairwise and NDCG-based methods achieve an
average Rank IC of about 0.08, while our method attains a substantially higher IC of 0.115,
an increase of over 30% relative to these baselines. As expected, regression-based methods
achieve considerably lower IC values, averaging about 0.044. Turning to portfolio returns,
our method achieves the highest monthly average return at 2.22%. Its annualized Sharpe
ratio is also the highest at approximately 0.92. While the volatility is moderately higher
compared with regression-based methods, the return is substantially higher, leading to a
superior overall Sharpe ratio.
To gain deeper insights into the model predictions and their corresponding portfolio
performance, we stratify the cross-sectional stocks into ten deciles for each method, as
reported in Table 4. Stocks with the highest predicted scores are allocated to Decile 10,
while those with the lowest are placed in Decile 1. Several key observations emerge from
this analysis. First, across all methods, decile returns and Sharpe ratios generally increase
from Decile 1 to Decile 10, while volatilities broadly decrease. This trend validates the
cross-sectional sorting capability of all evaluated models. Second, as shown in Panel A, a
comparison among the learning-to-rank methods reveals that our proposed RankIC more
effectively identifies underperforming stocks than the other two learning-to-rank methods,
producing strongly negative returns in the lowest decile (Decile 1). This stronger short signal
significantly enhances profitability when constructing long–short portfolios when shorting the
bottom decile. Third, compared with traditional regression models, LTR methods successfully
22

generate profitable short signals. The regression methods fail in this regard: the lowest deciles
of all three regression models yield positive returns, which severely degrades their long–short
portfolio performance. Finally, although RankIC incurs a higher maximum drawdown than
the regression baselines, it maintains the lowest drawdown among all LTR models and achieves
the highest Sharpe ratio across all six evaluated methods.
Table 4: Performance Metrics by Decile
Panel A: L TR Methods
LTR: RankIC LTR: Pairwise LTR: NDCG
Decile Ret Vol SR MDD Ret Vol SR MDD Ret Vol SR MDD
1 -1.20 10.08 -0.41 100.00 -0.34 10.27 -0.12 99.70 -0.27 9.95 -0.09 99.44
2 -0.10 8.53 -0.04 97.97 0.03 8.54 0.01 97.27 0.38 8.05 0.16 90.21
3 0.44 7.35 0.21 91.56 0.31 6.76 0.16 91.99 0.54 7.30 0.26 85.47
4 0.42 5.81 0.25 74.57 0.61 6.05 0.35 83.79 0.52 6.32 0.29 84.97
5 0.59 5.36 0.38 71.95 0.75 5.28 0.49 69.69 0.69 5.42 0.44 71.69
6 0.69 4.82 0.49 67.62 0.79 4.84 0.57 63.98 0.82 4.73 0.60 55.84
7 0.86 4.52 0.66 46.44 0.93 4.62 0.70 44.71 0.81 4.79 0.59 47.91
8 0.88 4.34 0.71 41.70 0.85 4.69 0.63 45.21 0.80 4.61 0.60 50.39
9 0.94 4.37 0.75 48.52 0.89 4.84 0.64 49.26 1.02 4.65 0.76 45.23
10 1.01 4.38 0.80 50.26 1.07 5.07 0.73 55.82 0.93 4.86 0.67 55.52
H–L 2.22 8.32 0.92 64.29 1.42 8.69 0.57 81.59 1.20 8.32 0.50 83.24
Panel B: Regression Methods
Regression: OLS Regression: XGBoost Regression: MLP
Decile Ret Vol SR MDD Ret Vol SR MDD Ret Vol SR MDD
1 0.19 5.66 0.12 85.70 0.12 7.90 0.05 97.03 0.16 6.71 0.08 96.75
2 0.47 4.86 0.34 67.56 0.52 6.69 0.27 87.93 0.49 5.05 0.34 77.99
3 0.75 4.59 0.57 52.54 0.59 5.39 0.38 66.29 0.67 4.59 0.50 51.62
4 0.68 4.52 0.52 53.24 0.48 5.30 0.31 65.98 0.70 4.47 0.54 54.29
5 0.78 4.66 0.58 52.64 0.84 5.24 0.56 52.26 0.81 4.38 0.64 44.92
6 0.85 4.65 0.64 42.74 0.82 5.33 0.53 61.22 0.76 4.68 0.56 53.33
7 0.93 4.81 0.67 53.54 0.84 4.86 0.60 54.07 0.88 4.88 0.63 51.08
8 0.87 5.17 0.58 53.44 0.83 5.19 0.55 59.37 0.71 4.79 0.52 59.83
9 1.03 5.38 0.66 61.73 0.95 5.40 0.61 53.63 1.00 5.32 0.65 54.02
10 1.17 5.67 0.71 56.85 1.37 5.89 0.81 47.31 1.25 6.39 0.68 48.56
H–L 0.97 4.56 0.74 43.78 1.25 6.21 0.70 58.29 1.08 4.53 0.83 46.28
Notes.This table reports decile portfolio performance based on model predictions. We report monthly return
(Ret), monthly volatility (Vol), annualized Sharpe ratio (SR), and maximum drawdown (MDD) for each
method. The high-minus-low (H–L) portfolio is constructed by taking a long position in stocks in the highest
decile (Decile 10) and a short position in stocks in the lowest decile (Decile 1). All metrics except the Sharpe
ratio are reported in percent.
We further visualize the cumulative returns of the long–short portfolios over the sample
period in Figure 4. Notably, the portfolio constructed using RankIC begins to consistently
outperform the other portfolios around 1985, and the performance gap between RankIC
and the benchmark methods widens steadily thereafter. This sustained outperformance in
cumulative returns provides further evidence of the effectiveness of our proposed method.
In contrast, the NDCG-based method underperforms all other approaches, particularly
after 2008, highlighting the potential limitations of its top-heavy objective. The Pairwise
23

Figure 4: Cumulative Returns
Note: The shaded periods denote recessions as defined by the National Bureau of Economic Research (NBER).
method performs robustly, maintaining the second-highest cumulative return trajectory,
especially in the later period. Among the regression-based approaches, the OLS (Normal)
Regression model delivers the lowest returns, while the MLP and XGBoost models converge to
similar performance levels by the end of the sample period. Furthermore, the RankIC portfolio
has remained notably resilient during recessionary periods, such as the Great Recession of
2007–2009 and the outbreak of the 2020 pandemic. This strong robustness suggests that our
proposed method is well suited to navigating severe market downturns.
7 Conclusion
Motivated by the need to directly optimize Rank IC in financial applications, we propose
LambdaRankIC, a novel learning-to-rank objective that directly targets the Spearman rank
correlation between model predictions and realized asset returns. We derive a closed-form
expression for the lambda gradients within the LambdaRank framework and analytically show
that the proposed objective optimizes a coarse upper bound of Rank IC. We conduct extensive
experiments using both simulated data and real financial market data. In simulations with
noiseless data, we demonstrate that our approach is able to recover the underlying ranked
24

structure of the data-generating process. Across all simulation settings, LambdaRankIC
consistently outperforms existing approaches, including standard regression-based methods
and learning-to-rank models optimized using the NDCG objective. Furthermore, using a
large-scale empirical dataset comprising 94 firm characteristics over a 30-year period, we
show that LambdaRankIC achieves the highest out-of-sample Rank IC and ICIR, as well
as superior portfolio performance in terms of returns and Sharpe ratios, relative to both
regression models with various specifications and existing learning-to-rank methods. Overall,
our results demonstrate that LambdaRankIC represents a meaningful extension of existing
learning-to-rank methodologies and provides a powerful new tool for ranking-based prediction
problems in finance.
7.1 Limitations and Future Directions
Our approach is not without limitations. First, from a methodological perspective, Lamb-
daRankIC inherits the same limitations from the original LambdaRank framework. In
particular, the derived λ values are pseudo-gradients rather than true gradients, since the
Rank IC objective is a non-smooth function of the model scores. Nevertheless, Donmez et al.
[2009] demonstrate that LambdaMART converges to a fixed point of the gradient under mild
conditions, although no global convergence guarantees are available. We explicitly acknowl-
edge this limitation and address it empirically by presenting convergence curves in Section 6.
Moreover, we partially mitigate this concern by showing that the LambdaRankIC algorithm
optimizes a coarse upper bound of 1 −Rank IC , such that minimizing the LambdaRankIC
loss indirectly maximizes Rank IC. Relatedly, tighter upper bounds of Rank IC may exist.
For example, Wang et al. [2018] derive alternative weighting schemes for the ∆ terms in
LambdaRank to more closely approximate target ranking metrics. However, they also caution
that employing tighter surrogate bounds may increase the risk of overfitting. Exploring this
trade-off in the context of Rank IC optimization remains an interesting direction for future
research.
Second, one of the key motivations of our work is the non-differentiability of the ranking
operator. A promising direction is therefore to incorporate differentiable sorting and ranking
operators [Blondel et al., 2020] into gradient boosting, enabling theoretically grounded
gradients for Spearman rank correlation.
Third, our experiments focus on cross-sectional ranking, where each date defines a group
of assets to be ranked. The framework extends naturally to time-series ranking. For example,
we can treat an asset as a query and rank its expected returns across future periods. This
formulation aligns with market-timing applications and time-series IC evaluation, and would
25

allow the same RankIC-optimized objective to be applied to a structurally different prediction
task.
Finally, our current implementation is limited to CPU-based training. Developing a
parallelized or CUDA-enabled implementation to support GPU-accelerated training on
large-scale datasets is a natural next step.
26

References
M. Blondel, O. Teboul, Q. Berthet, and J. Djolonga. Fast differentiable sorting and ranking.
InProceedings of the 37th International Conference on Machine Learning, pages 950–960,
2020.
S. Bryzgalova, M. Pelger, and J. Zhu. Forest through the trees: Building cross-sections of
stock returns.The Journal of Finance, 80(5):2447–2506, 2025.
C. Burges, T. Shaked, E. Renshaw, A. Lazier, M. Deeds, N. Hamilton, and G. Hullender.
Learning to rank using gradient descent. InProceedings of the 22nd International Conference
on Machine Learning, pages 89–96, 2005.
C. J. Burges. From RankNet to LambdaRank to LambdaMART: An overview. Technical
Report MSR-TR-2010-82, 2010.
C. J. Burges, R. Ragno, and Q. Le. Learning to rank with nonsmooth cost functions. In
Advances in Neural Information Processing Systems, volume 19, 2006.
A. Butler and R. H. Kwon. Integrating prediction in mean-variance portfolio optimization.
Quantitative Finance, 23(3):429–452, 2023.
Z. Cao, T. Qin, T.-Y. Liu, M.-F. Tsai, and H. Li. Learning to rank: from pairwise approach
to listwise approach. InProceedings of the 24th International Conference on Machine
Learning, pages 129–136, 2007.
L. Chen, M. Pelger, and J. Zhu. Deep learning in asset pricing.Management Science, 70(2):
714–750, 2024.
T. Chen and C. Guestrin. XGBoost: A scalable tree boosting system. InProceedings of the
22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining,
pages 785–794, 2016.
L. W. Cong, K. Tang, J. Wang, and Y. Zhang. Alphaportfolio: Direct construc-
tion through deep reinforcement learning and interpretable ai.Available at SSRN:
https://ssrn.com/abstract=3554486 or http://dx.doi.org/10.2139/ssrn.3554486, 2021.
L. W. Cong, G. Feng, J. He, and X. He. Growing the efficient frontier on panel trees.Journal
of Financial Economics, 167:104024, 2025.
R. Cont. Empirical properties of asset returns: stylized facts and statistical issues.Quantitative
finance, 1(2):223, 2001.
27

G. Coqueret and T. Guida.Machine learning for factor investing: R version. Chapman and
Hall/CRC, 2020.
G. Costa and G. N. Iyengar. Distributionally robust end-to-end portfolio construction.
Quantitative Finance, 23(10):1465–1482, 2023.
A. P. Dempster, N. M. Laird, and D. B. Rubin. Maximum likelihood from incomplete data
via the em algorithm.Journal of the Royal Statistical Society. Series B (Methodological),
39(1):1–22, 1977.
P. Donmez, K. Svore, and C. J. Burges. On the local optimality of LambdaRank. In
Proceedings of the 32nd International ACM SIGIR Conference on Research and Development
in Information Retrieval, pages 460–467, 2009.
E. F. Fama and K. R. French. Common risk factors in the returns on stocks and bonds.
Journal of Financial Economics, 33(1):3–56, 1993.
F. Feng, X. He, X. Wang, C. Luo, Y. Liu, and T.-S. Chua. Temporal relational ranking for
stock prediction.ACM Transactions on Information Systems, 37(2):1–30, 2019.
G. Feng, J. He, N. G. Polson, and J. Xu. Deep learning in characteristics-sorted factor models.
Journal of Financial and Quantitative Analysis, 59(7):3001–3036, 2024.
Y. Freund, R. Iyer, R. E. Schapire, and Y. Singer. An efficient boosting algorithm for
combining preferences.Journal of Machine Learning Research, 4:933–969, 2003.
J. H. Friedman. Greedy function approximation: A gradient boosting machine.Annals of
Statistics, 29(5):1189–1232, 2001.
Y. Gorishniy, I. Rubachev, V. Khrulkov, and A. Babenko. Revisiting deep learning models
for tabular data.Advances in Neural Information Processing Systems, 34:18932–18943,
2021.
J. Green, J. R. Hand, and X. F. Zhang. The characteristics that provide independent
information about average us monthly stock returns.The Review of Financial Studies, 30
(12):4389–4436, 2017.
R. C. Grinold and R. N. Kahn.Active Portfolio Management: A Quantitative Approach for
Providing Superior Returns and Controlling Risk. McGraw Hill, 2000.
S. Gu, B. Kelly, and D. Xiu. Empirical asset pricing via machine learning.The Review of
Financial Studies, 33(5):2223–2273, 2020.
28

S. Gu, B. Kelly, and D. Xiu. Autoencoder asset pricing models.Journal of Econometrics,
222(1):429–450, 2021.
C. R. Harvey, Y. Liu, and H. Zhu. . . . and the cross-section of expected returns.The Review
of Financial Studies, 29(1):5–68, 2016.
Y. He, Y. Yang, D. Lian, and K. Zhang. Divide and contrast: A text-based method for firm
market risk prediction.INFORMS Journal on Computing, 2025.
B. T. Kelly, S. Pruitt, and Y. Su. Characteristics are covariances: A unified model of risk
and return.Journal of Financial Economics, 134(3):501–524, 2019.
B. T. Kelly, B. Kuznetsov, S. Malamud, and T. A. Xu. Artificial intelligence
asset pricing models.Available at SSRN: https://ssrn.com/abstract=5089371 or
http://dx.doi.org/10.2139/ssrn.5089371, January 2025. doi: 10.2139/ssrn.5089371. URL
https://ssrn.com/abstract=5089371. Swiss Finance Institute Research Paper No. 25-
08.
M. Leippold, Q. Wang, and W. Zhou. Machine learning in the Chinese stock market.Journal
of Financial Economics, 145(2):64–82, 2022.
Y. Lin, Y. Su, and Z. Zhu. Empirical asset pricing via learning-to-rank.Available at SSRN:
https://ssrn.com/abstract=6348379 or http://dx.doi.org/10.2139/ssrn.6348379, 2026.
T.-Y. Liu. Learning to rank for information retrieval.Foundations and Trends®in Informa-
tion Retrieval, 3(3):225–331, 2009.
T. Ma and Y. Tan. Stock ranking with multi-task learning.Expert Systems with Applications,
199:116886, 2022.
H. Markowitz. Portfolio selection.The Journal of Finance, 7(a), 1952.
D. Poh, B. Lim, S. Zohren, and S. Roberts. Building cross-sectional systematic strategies by
learning to rank.The Journal of Financial Data Science, 3(2):70–86, 2021.
S. K. Saha, J. Gao, and R. Gerlach. Stock ranking prediction using list-wise approach and
node embedding technique.IEEE Access, 9:88981–88997, 2021.
Q. Song, A. Liu, and S. Y. Yang. Stock portfolio selection using learning-to-rank algorithms
with news sentiment.Neurocomputing, 264:20–28, 2017.
C. Spearman. The proof and measurement of association between two things.The American
Journal of Psychology, 15(1):72–101, 1904.
29

H. Tian, X. Zheng, K. Zhao, M. W. Liu, and D. D. Zeng. Inductive representation learning on
dynamic stock co-movement graphs for stock predictions.INFORMS Journal on Computing,
34(4):1940–1957, 2022.
I. Tulchinsky.Finding Alphas: A quantitative approach to building trading strategies. John
Wiley & Sons, 2019.
X. Wang, C. Li, N. Golbandi, M. Bendersky, and M. Najork. The lambdaloss framework for
ranking metric optimization. InProceedings of the 27th ACM International Conference on
Information and Knowledge Management, pages 1313–1322, 2018.
Q. Wu, C. J. Burges, K. M. Svore, and J. Gao. Adapting boosting for information retrieval
measures.Information Retrieval, 13(3):254–270, 2010.
F. Xia, T.-Y. Liu, J. Wang, W. Zhang, and H. Li. Listwise approach to learning to rank:
theory and algorithm. InProceedings of the 25th International Conference on Machine
learning, pages 1192–1199, 2008.
Y. Yang, K. Zhang, and Y. Fan. Analyzing firm reports for volatility prediction: A knowledge-
driven text-embedding approach.INFORMS Journal on Computing, 34(1):522–540, 2022.
X. Zhang, L. Wu, and Z. Chen. Constructing long-short stock portfolio with a new listwise
learn-to-rank algorithm.Quantitative Finance, 22(2):321–331, 2022.
Z. Zhang, J. Yuan, and A. Gupta. Let the laser beam connect the dots: Forecasting and
narrating stock market volatility.INFORMS Journal on Computing, 36(6):1400–1416,
2024.
A Proof of Proposition 2
Proof.By the definition ofρin Eq. (9) and the fact that
¯ˆr= ¯˜y= n+ 1 2 ,
we have
ρ= 12 n(n2 −1)
 nX
i=1
ˆri ˜yi −n (n+ 1) 2
4
!
.
Using
ˆri = 1 +
X
j̸=i
I si<sj ,
30

we obtain nX
i=1
ˆri ˜yi =
nX
i=1
˜yi +
nX
i=1
X
j̸=i
˜yi I si<sj .
Now consider the double sum nX
i=1
X
j̸=i
˜yi I si<sj .
Each ordered pair ( i, j) with i̸ = j appears exactly once in this sum. To rewrite the sum in
terms of unordered pairs, group together the two ordered pairs ( i, j) and ( j, i) associated
with the same unordered pair{i, j}. For each unordered pair, relabel the indices so that
˜yi <˜yj.
Then the contribution of the ordered pair (i, j) is
˜yi I si<sj ,
while the contribution of the ordered pair (j, i) is
˜yj I sj <si.
Therefore, for each unordered pair{i, j}such that ˜yi <˜yj, the total contribution is
˜yi I si<sj + ˜yj I sj <si.
Assuming that there are no ties in the scores, we have
I sj <si = 1−I si<sj ,
and hence
˜yi I si<sj + ˜yj I sj <si = ˜yi I si<sj + ˜yj

1−I si<sj

= ˜yj −(˜yj −˜yi)I si<sj .
Therefore,
nX
i=1
X
j̸=i
˜yi I si<sj =
X
˜yi<˜yj

˜yj −(˜yj −˜yi)I si<sj

,
where P ˜yi<˜yj denotes summation over all unordered pairs{i, j}, indexed so that ˜yi <˜yj.
31

Substituting this into the previous display gives
nX
i=1
ˆri ˜yi =
nX
i=1
˜yi +
X
˜yi<˜yj

˜yj −(˜yj −˜yi)I si<sj

=
nX
i=1
˜yi +
X
˜yi<˜yj
˜yj −
X
˜yi<˜yj
(˜yj −˜yi)I si<sj .
Since ˜yis a permutation of{1, . . . , n},
nX
i=1
˜yi =
nX
k=1
k= n(n+ 1) 2 .
Moreover, to evaluate X
˜yi<˜yj
˜yj,
fix a valuek∈ {1, . . . , n}and consider the unique indexjsuch that
˜yj =k.
Here, ˜yj is the true rank of sample j. In the sum above, the term ˜yj is counted once for every
indexisatisfying
˜yi <˜yj =k.
Since ˜yis a permutation of{1, . . . , n}, the ranks smaller thankare exactly
1,2, . . . , k−1,
and each of these ranks appears exactly once. Therefore, there are exactly k− 1 indices i
such that ˜yi < k. Hence, the value k = ˜yj is added exactly k− 1 times in the sum, so its
total contribution is
(k−1)k.
Summing over all possible rank valuesk= 1, . . . , n, we obtain
X
˜yi<˜yj
˜yj =
nX
k=1
(k−1)k.
32

Therefore,
X
˜yi<˜yj
˜yj =
nX
k=1
(k−1)k= n(n+ 1)(2n+ 1) 6 − n(n+ 1) 2 .
Hence,
nX
i=1
ˆri ˜yi = n(n+ 1)(2n+ 1) 6 − X ˜yi<˜yj (˜yj −˜yi)I si<sj .
Substituting this into the expression forρyields
ρ= 12 n(n2 −1)

 n(n+ 1)(2n+ 1)
6 −n (n+ 1) 2 4 − X ˜yi<˜yj (˜yj −˜yi)I si<sj

 .
Since
n(n+ 1)(2n+ 1)
6 −n (n+ 1) 2 4 = n(n2 −1) 12 ,
it follows that
ρ= 1− 12 n(n2 −1) X ˜yi<˜yj (˜yj −˜yi)I si<sj ,
and therefore
1−ρ= 12 n(n2 −1) X ˜yi<˜yj (˜yj −˜yi)I si<sj .
B Hyperparameters Used in Simulation
Hyperparameter Value
max depth 8
learning rate{0.001, 0.01, 0.1}
subsample 1.0
colsample bytree 1.0
min child weight 1
tree method hist
C Characteristics used in Return Prediction
33

Variable Description
absacc Absolute value ofacc
acc Working capital accruals
aeavol Abnormal earnings announcement volume
age # of years since first Compustat coverage
agr Asset growth rate
baspread Bid-ask spread
beta Beta
betasq Market beta squared
bm Book-to-market ratio
bm ia Industry-adjusted book-to-market ratio
cash Cash holdings
cashdebt Cash flow to debt
cashpr Cash productivity
cfp Cash flow to price ratio
cfp ia Industry-adjusted cash flow to price ratio
chatoia Industry-adjusted change in asset turnover
chcsho % Change in shares outstanding
chempia Industry-adjusted change in # of employees
chinv Change in inventory
chmom Change in 6-month momentum
chpmia Industry-adjusted change in profit margin
chtx % Change in tax expense
cinvest Corporate investment
convind Convertible debt indicator
currat Current ratio
depr Depreciation / PP&E
divi Dividend initiation
divo Dividend omission
dolvol Dollar trading volume
dy Dividend to price
ear Earnings announcement return
egr Growth in common shareholder equity
ep Earnings to price
Continued on next page
34

Variable Description
gma Gross profitability
grCAPX % change in capital expenditures
grltnoa Growth in long term net operating assets
herf Industry sales concentration
hire Employee growth rate
idiovol Idiosyncratic return volatility
ill Illiquidity
indmom Industry momentum
invest Capital expenditures and inventory
lev Leverage
lgr Change in total liabilities
maxret Maximum daily return
mom12m 12-month momentum
mom1m 1-month momentum
mom36m 36-month momentum
mom6m 6-month momentum
ms Financial statement score
mve Size
mve ia Industry-adjusted size
nincr Number of earnings increases
operprof Operating profitability
orgcap Organizational capital
pchcapx ia Industry adjusted % change in capital expenses
pchcurrat % change in current ratio
pchdepr % change in depreciation
pchgm pchsale % change in gross margin - % change in sales
pchquick % change in quick ratio
pchsale pchinvt % change in sales - % change in inventory
pchsale pchrect % change in sales - % change in A/R
pchsale pchxsga % change in sales - % change in SG&A
pchsaleinv % change in sales-to-inventory
pctacc Percent accruals
pricedelay Price delay
Continued on next page
35

Variable Description
ps Financial statements score
quick Quick ratio
rd R&D increase
rd mve R&D to market capitalization
rd sale R&D to sales
realestate Real estate holdings
retvol Return volatility
roaq Return on assets
roavol Earnings volatility
roeq Return on equity
roic Return on invested capital
rsup Revenue surprise
salecash Sales to cash
saleinv Sales to inventory
salerec Sales to receivables
secured Secured debt
securedind Secured debt indicator
sgr Sales growth
sin Sin stocks
sp Sales to price
std dolvol Volatility of liquidity (dollar trading volume)
std turn Volatility of liquidity (share turnover)
stdacc Accrual volatility
stdcf Cash flow volatility
tang Debt capacity/firm tangibility
tb Tax income to book income
turn Share turnover
zerotrade Zero trading days
36
