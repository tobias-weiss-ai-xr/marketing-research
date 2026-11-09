---
title: Pricing Strategies for Different Accuracy Models from the Same Dataset Based on Generalized Hotelling's
  Law
url: https://arxiv.org/abs/2404.05272
category: ai-marketing
subcategory: empirical
date: 2024-04
venue: ''
authors:
- Jie Liu
- Tao Feng
- Yan Jiang
- Peizheng Wang
- Chao Wu
source: arxiv
pdf_url: https://arxiv.org/pdf/2404.05272
pages: 24
chars: 46972
fetched_at: '2026-11-08T13:18:42+00:00'
kb_version: 1
---

# Pricing Strategies for Different Accuracy Models from the Same Dataset Based on Generalized Hotelling's Law

Pricing Strategies for Different Accuracy Models
from the Same Dataset Based on Generalized
Hotelling’s Law
Jie Liu∗1, Tao Feng†2, Peizheng Wang2, and Chao Wu‡2
1Zhejiang Shuren University
2Zhejiang University
Abstract
We consider a scenario where a seller possesses a dataset D and trains
it into models of varying accuracies for sale in the market. Due to the
reproducibility of data, the dataset can be reused to train models with dif-
ferent accuracies, and the training cost is independent of the sales volume.
These two characteristics lead to fundamental differences between the
data trading market and traditional trading markets. The introduction
of different models into the market inevitably gives rise to competition.
However, due to the varying accuracies of these models, traditional multi-
oligopoly games are not applicable. We consider a generalized Hotelling’s
law, where the accuracy of the models is abstracted as distance. Buy-
ers choose to purchase models based on a trade-off between accuracy and
price, while sellers determine their pricing strategies based on the mar-
ket’s demand. We present two pricing strategies: static pricing strategy
and dynamic pricing strategy, and we focus on the static pricing strategy.
We propose static pricing mechanisms based on various market condi-
tions and provide an example. Finally, we demonstrate that our pricing
strategy remains robust in the context of incomplete information games.
∗Equal contribution
†Equal contribution
‡Corresponding author
1
arXiv:2404.05272v2  [cs.AI]  29 Mar 2025

Contents
1 Introduction 1
2 Preliminary: Data chain structure and utility functions 2
3 Static pricing strategy: generalized Hotelling’s law 4
3.1 Two nodes example . . . . . . . . . . . . . . . . . . . . . . . . . 5
3.2 General situation . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
3.3 Continuity of the revenue function . . . . . . . . . . . . . . . . . 9
4 Dual and quasi-dual situation 10
4.1 Dual situation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
4.2 Quasi-dual situation . . . . . . . . . . . . . . . . . . . . . . . . . 10
4.3 Discussion on the data chains among four dimensions . . . . . . . 12
5 Dynamic pricing strategy: chain-like Nash equilibrium 12
5.1 Two nodes example . . . . . . . . . . . . . . . . . . . . . . . . . 13
5.2 General situation . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
6 Applications: separable utility function 15
6.1 Uniform distribution . . . . . . . . . . . . . . . . . . . . . . . . . 15
6.2 Continuous distribution . . . . . . . . . . . . . . . . . . . . . . . 17
7 Incomplete information game 18
8 Conclusions 20
2

1 Introduction
Data training and trading are receiving increasing attention[Agarwal et al.(2019),
Pei(2020), Zhang et al.(2023)]. Industries across the board have focused their
attention on how to maximize the extraction of information inherent in data
through model training. The value of this information is precisely the manifes-
tation of the value of data as a production factor itself.
We focuses on considering trained models as products in this paper. Trad-
ing models rather than data itself inherently reduces the risk of data pri-
vacy breaches. Unlike physical materials, data possesses reproducibility. In
[Agarwal et al.(2019), Chen et al.(2022)], the reproducibility of data is identi-
fied as a detrimental factor, and strategies are explored to address the challenge
of diminished data value arising from this reproducibility. However, when data
is utilized solely as raw material for training models rather than being directly
sold in the market, we observe that due to this characteristic, we can retrain
the data to generate different models and sell them. Also, from the market’s
perspective, different models can be trained using the same data set, thereby
satisfying varying market demands. This results in traditional economic prin-
ciples, such as opportunity cost, acquiring different connotations in the context
of data transactions.
Despite this, there are still many similarities between data trading and tradi-
tional market transactions. For instance, when different model products are sold
in the market, competition will inevitably arise. There has been lots of research
regarding game theory in data valuation and data market transactions, such as
[Jia et al.(2019), Karlaˇ s et al.(2022), Huang et al.(2023), Yu et al.(2023)]. We
focus on considering the application of generalized Hotelling’s law in the data
trading market.
The traditional Hotelling’s law is a spatial competition strategy, and it
describes a scenario where two firms compete by setting prices and choosing
locations along a linear product space[Brown(1989)]. Based on Hotelling’s
law, there have been numerous studies on location selection and pricing, see
[Guo et al.(2015), Liu and Pelechrinis(2019)]. Essentially , Hotelling’s law
reflects a trade-off between two independent variables of buyers based
on their needs and preferences in order to make an optimal choice. In
this paper, we quantify model accuracy as the distance between multiple buyers
and sellers. Buyers weigh the unit price and accuracy of different models based
on their own utility functions and then choose the model that maximizes their
utility.
We consider a scenario where a single buyer chooses between these two mod-
els at first. In Figure 1, the buyer naturally prefers a model with 100% accuracy,
meaning the buyer’s location corresponds to the location of the 100% accurate
model. However, such accuracy is impossible to achieve. Therefore, the sellers
can only strive to maximize the model’s accuracy, i.e., to be “closer” to the
buyer in terms of “location”. On the other hand, the buyer compares the utility
value between T1 and T2 and chooses the model with higher utility.
Besides replicability, data itself also has privacy protection features, which
1

often lead to incomplete information on both the buyer’s and seller’s sides. In
[Shokri et al.(2012)], the authors explore how to ensure the robustness of the
results with incomplete information. In Section 7, we also demonstrate that
under incomplete information game, the algorithm we provide remains robust
and the error bound can be calculated.
Related works
In [Agarwal et al.(2019)], the authors introduce an effective data trading
mechanism, which gives the strategies for matching buyers and sellers as well
as how the market interacts. Additionally, the authors present a robust-to-
replication algorithm, ensuring that even if the traded data is replicated, it will
not affect its market pricing. In [Chen et al.(2022)], the authors introduce an-
other data trading mechanism to prevent the devaluation of the seller’s data
after replication. This method involves the seller initially presenting a por-
tion of the data to the buyer as sample data along with a selling price. Then
the buyer conducts Bayesian inference to predict the accuracy and quality of
the data via the corresponding prior knowledge, thus determining whether to
purchase the data at the offered price or not. In terms of privacy protection,
[Amiri et al.(2023)] presents a trading mechanism that not only protects data
privacy but also allows the seller to demonstrate the quality of the data to the
buyer. In this paper, the quality of the data depends on the relevance of the
sold data to the buyer’s needs. In [Ravindranath et al.(2023)], a deep learning-
based approach for designing data market mechanisms is presented, targeting
more complex transaction scenarios. It seeks to identify optimal market mech-
anism designs by examining two settings: one involving a single buyer and
another involving multiple buyers. In [Sun et al.(2024)], a data market pricing
scheme based on the combination of machine learning and the Stackelberg game
is also proposed, and the optimization objective of this pricing scheme is to max-
imize the buyers’ benefits. In [Egan and Oren(2024)], a scenario of repeatedly
selling data in an auction setting is given, and the corresponding winner deter-
mination problem is investigated. Regarding research on direct model pricing,
[Chen et al.(2019)] studies a machine learning-based model pricing mechanism,
with a particular focus on strategies to avoid arbitrage.
2 Preliminary: Data chain structure and utility
functions
In this paper, we consider a scenario where sellers train models with different
accuracies using the dataset D and sell them in the market. We arrange these
models as a data chain, see Figure 2, based on their accuracies, from lowest to
highest (or vice versa). We assume in this paper that accuracy Ai of the model
Ti is a strictly monotonically increasing known function of training cost ci. We
aim to maximize the profit of models across the entire data chain by arranging
the training costs and unit prices pi. Note that the cost of model training is
independent of sales volume, and there exists competition among models of
2

accuracyA1 A2
T1(with price p1) T2(with price p2)
1
buyer
Figure 1: Generalized Hotelling’s law
different accuracies. Let S : s1 → s2 → · · · →sn be a data chain and Ti’s are
the corresponding trained models, the goal is to maximize
nP
i=1
max{ri − ci, 0}
under the constraints of ci’s where ri is the revenue from sales of Ti.
Figure 2: Data Chain (Dataset D cannot be directly sold to the market)
An obvious issue in solving this optimization problem is how to determine
the unit price and sales volume for each model. Generally, the seller’s sales
volume is related to market demand, expressed as utility functions once the
unit price is set.
We denote a class of continuous functions B = ( b1, b2, · · ·, bn) as utility
functions for all buyers, where each index corresponds to the model Ti with
cost ci and the precision Ai determined by ci. The independent variables of
bi’s include the model price p and the buyers’ minimum accuracy requirement
a. The buyer will choose the model only if the utility function value is positive
and the model’s accuracy exceeds their own accuracy requirements. If multiple
models have positive utility function values, the buyer will choose the model
with the highest function value. We denote P as the price cap and we define A
and A as the lower and upper bounds of the model’s accuracy, respectively. We
assume that bi’s have the following properties:
• For any two models Ti and Tj with i < jand fixed p and a, then bi(p, a) <
bj(p, a).
• All bi’s are strictly monotonically decreasing of p.
• The function bi is strictly monotonically increasing of a ∈ [A, Ai].
3

The first property implies that, for buyers with a fixed accuracy requirement,
a model with higher accuracy corresponds to higher utility at the same price
point. The third property indicates that, when a model is priced fixedly, buyers
with higher accuracy needs will derive higher utilities from the model.
We define Di,p = {a ∈ [A, Ai]|bi(p, a) ≥ 0} and we have
Definition 2.1. We name the class of functions B = (b1, b2, · · ·, bn) are accuracy-
compatible if for any i < jand fixed p, p′, we denote Bij(a) = bi(p, a) − bj(p′, a)
and we have
• Bij(a) > 0 or Bij(a) < 0 for a ∈ Di,p
T Dj,p′.
• If there exists a ∈ Di,p
T Dj,p′ such that Bij(a) = 0, then Bij(a+) < 0 for
Di,p
T Dj,p′ ∋ a+ > aand Bij(a−) > 0 for Di,p T Dj,p′ ∋ a− < a.
Remark 2.2. The motivation behind defining the accuracy-compatibility of util-
ity functions stems from the observation that, when the prices of two models fall
within a reasonable range, i.e., the corresponding utility function values are non-
negative, and then these two models are in competition. In this case, the outcome
of this competition consistently sees buyers with high accuracy demands opting
for the model that offers high accuracy at a higher price. In contrast, buyers
with low accuracy demands make the opposite choice. This definition aligns with
realistic scenarios.
3 Static pricing strategy: generalized Hotelling’s
law
We reiterate that in this paper, we consider a seller possesses a dataset D and
makes a profit by training this dataset into multiple models of different accura-
cies and selling them. We assume that, for the seller, the relationship between
the training cost and the corresponding model accuracy is a known, strictly
monotonically increasing function. Also, for the buyers, the distribution of
their minimum required accuracies is known, which we denote as λ(a), and con-
tinuous. Moreover, for any buyer with a known minimum required accuracy, the
utility function for models of a specified accuracy and price is also known, and
the utility functions corresponding to all accuracies are accuracy-compatible.
We give the algorithm steps to maximize the seller’s profit,
1. The seller lists all the possible cost allocations c1, c2, · · ·, cn where ci <
ci+1.
2. The seller optimizes the corresponding pricing strategy to maximize the
profit based on the fixed cost allocations.
3. The seller compares all the profits and chooses the cost allocation corre-
sponding to the highest profit.
4

We focus primarily on the second step in this section. We consider a static
pricing strategy, where upstream nodes set prices first, and downstream nodes
set prices based on the distribution of minimum accuracy requirements and the
upstream nodes’ pricing strategies to maximize the profit of this model and the
models of the upstream nodes. Once downstream nodes have completed their
pricing, upstream nodes do not adjust their prices further. We use generalized
Hotelling’s law to describe the market competition between adjacent nodes.
Specifically, we have
1. We calculate p1 to maximize the profit of T1.
2. Fixed p1 and we calculate p2 to maximize the profit of T1 and T2.
3. We iterate to calculate pi, while keeping p1, p2, · · ·, pi−1 invariant, until
i = n.
3.1 Two nodes example
When only model T1 is sold in the market, the optimal pricing strategy which
is based on the buyers’ utility function and minimum accuracy requirements is
p1 = argmax
p
p
Z A1
a′ 1
λ(a)da. (1)
where b1(p, a′ 1) = 0. Note that A1 is the function of c1 and utility function b1
is denoted by A1. We rename the market allocation of T1 as (a1,−, a1,+].
We consider the situation in which both T1 and T2 are sold in the market,
and the corresponding utility functions b1 and b2 are accuracy-compatible. Note
that due to differences in model accuracy and price, their utility function values
vary, leading to differing competitive environments when these models are sold
into the market. Consequently, we categorize and discuss all possible competi-
tive environments and present corresponding optimization plans along with the
constraints on accuracy and price for models associated with these strategies.
We denote b2(p, a′ 2) = 0 and b1(p1, a∗ 2) = b2(p, a∗ 2) ≥ 0 if a∗ 2 is attainable. We
classify and discuss three possible market allocation scenarios:
• If the T2’s market completely covers the T1’s market, then we have
p2 = argmax
p
p
Z A2
a′ 2
λ(a)da, a ′ 2 < a1,−. (2)
Note that B12 < 0 in ( a1,−, a1,+] because of accuracy-compatible of bi’s.
It leads to a∗ 2 not attainable.
• If there is market competition between T2 and T1, then we have
p2 = argmax
p
p1
Z a∗ 2
a1,−
λ(a)da+p
Z A2
a∗ 2
λ(a)da, a ′ 2 ≥ a1,− a1,− ≤ a∗ 2 ≤ a1,+.
(3)
5

• If there is no market competition between T1 and T2, then we have
p2 = argmax
p
p
Z A2
A1
λ(a)da, a 1,− < a′ 2 ≤ A1, (4)
or
p2 = argmax
p
p
Z A2
a′ 2
λ(a)da, A 1 < a′ 2 < A2. (5)
It is clear that the market allocation of each model is connected, and we
rename the new market allocation of T1 and T2 as (a1,−, a1,+] and ( a2,−, a2,+].
Let
b2(a) =
(
bj(pj, a) if a ∈ (aj,−, aj,+], j = 1, 2,
0 otherwise, (6)
we show the market allocation that corresponds to these situations, see Figure
3.
a
b2(a)
a2,− a2,+
(a) Allocation of
(2)
a
b2(a)
a1,−a1,+(a2,−) a2,+
(b) Allocation of
(3)
a
b2(a)
a1,−a1,+(a2,−) a2,+
(c) Allocation of (4)
a
b2(a)
a1,− a1,+a2,− a2,+
(d) Allocation of
(5)
Figure 3: Market allocations(red is for T1 and blue is for T2)
3.2 General situation
In this subsection, we prove the main result by induction. For a data chain
length of 2, we have the following observations
• The market allocation of each model is connected and b2 is continuous
almost everywhere. Moreover, we have a1,− < a1,+ ≤ a2,− < a2,+.
6

• If b2 is not continuous in a, then lim a→a− b2(a) > lim a→a+ b2(a).
• If there exists market allocation ( aj,−, aj,+] corresponds to Tj and aj,− /∈
supp{b2}, then lim a→(aj,−)+ bj(a) = 0.
• If bi is discontinuous at point ak,+, then ak,+ = Ak.
We then assume that it also holds when the length of the data chain is i, and
we introduce a definition
Definition 3.1. We define i-th enveloping utility function of the data chain
s1 → s2 → · · · →si as
bi(a) =
(
bj(pj, a) if a ∈ (aj,−, aj,+], j = 1, 2, . . . , i,
0 otherwise. (7)
When the length of data chain is i + 1, we have
Lemma 3.2. Fixed p, bi+1(p, a) and bi(a) in supp{bi} have at most one point
where their function values are equal.
Proof. We prove this lemma by contradiction. We assume there are two adjacent
points where bj(pj, α1) = bi+1(p, α1) and bk(pk, α2) = bi+1(p, α2). It is clear
that j ̸= k due to the accuracy-compatibility. Without losing generality, we
assume j < k, and then α1 < α2 by definition.
We havebi+1(p, aj,+) ≥ bi(aj,+) = bj(pj, aj,+), and bi+1(p, ak,−) < lim a→(ak,−)+ bi(ak,−) =
bk(pk, ak,−) respectively, due to the accuracy-compatibility of bi+1, bj and bk.
Also, we have bi+1(p, aj,+) ≤ bi+1(p, ak,−) due to monotonicity. Note that
bi+1(p, aj,+) = bi+1(p, ak,−) if and only if j + 1 = k, i.e., aj,+ = ak,−, but in
this case, we have bi+1(p, aj,+) ≥ bj(pj, aj,+) ≥ bk(pk, ak,−) > bi+1(p, ak,−),
it leads to a contradiction. So we claim that bi+1(p, aj,+) < bi+1(p, ak,−) and
aj,+ ̸= ak,−.
We have
• If (aj,+, ak,−] ⊆ supp{bi}, then we denote the market allocations ofTj+1, Tj+2, · · ·, Tk−1
are (as,−, as,+](s = j + 1, j+ 2, . . . , k− 1). Due to compatibility and the
fact that bi+1(p, aj,+) ≥ bj(pj, aj,+), we have, note that as,+ = as+1,−,
bi+1(p, a)−bs(ps, a) > 0, a ∈ (as,−, as,+], s = j+1, j+2, . . . , k−1. (8)
It leads to bi+1(p, ak,−) ≥ lim a→(ak,−)+ bk(pk, ak,−) > bi+1(p, ak,−), which is
a contradiction.
• If ( aj,+, ak,−] ⊈ supp{bi}, then there exists ( au,−, ak,−] ⊆ supp{bi} and
by assumption, we have lim
a→(au,−)+
bi(a) = 0. So
bi+1(p, a) − bs(ps, a) > 0, a ∈ (as,−, as,+], s = u + 1, u+ 2, . . . , k− 1,
(9)
which is also a contradiction.
7

We assume that for the data chain s1 → s2 → · · · →si, the corresponding
market allocation for each model is connected. Then, for the model Ti+1 and
let bi+1(p, a′ i+1) = 0 and bi+1(p, a∗ i+1) = bi(a∗ i+1) ≥ 0 if a∗ i+1 is attainable, we
consider the following possible market allocation scenarios:
• If a′ i+1 ∈ (aj−1,+, aj,−], then bi+1(p, a) ≥ bi(a) where a ∈ (a′ i+1, ai,+] due
to accuracy-compatibility. We have
pi+1 = argmax
p
p
Z Ai+1
a′ i+1
λ(a)da, a j−1,+ < a′ i+1 ≤ aj,−. (10)
Also, if a′ i+1 ∈ (ak,−, ak,+] where bi+1(p, a) < bi(a) for a ∈ (a′ i+1, aj,+]
and bi+1(p, a) > bi(a) for a ∈ (aj+1,−, Ai], then we have
pi+1 = argmax
p
p
Z Ai+1
aj,+
λ(a)da, a k,− < a′ i+1 ≤ ak,+ (11)
and aj,+ = Aj. In these two cases, Ti+1 completely covers Tj, Tj+1, · · ·Ti’s
markets and has no competition with the previous j − 1 models.
• If a′ i+1 ∈ (ak,−, ak,+] and exists a∗ i+1 ∈ (aj,−, aj,+] such thatbi+1(p, a∗ i+1) =
bi(a∗ i+1) ≥ 0, then we have
pi+1 = argmax
p
pj
Z a∗ i+1
aj,−
λ(a)da+p
Z Ai+1
a∗ i+1
λ(a)da, a k,− < a′ i+1 ≤ ak,+, a j,− < a∗ i+1 ≤ aj,+.
(12)
In this case, Ti+1 completely covers the Tj+1, Tj+2, · · ·, Ti’s markets but
competes with the j-th model.
• If a′ i+1 ∈ (Ai, Ai+1], then we have
pi = argmax
p
p
Z Ai+1
a′ i+1
λ(a)da, A i < a′ i+1 ≤ Ai+1. (13)
In this case, Ti has no market competition with all previous models.
It is clear that all classifications related to the allocation of Ti+1 are con-
nected. We select the optimal strategy with the highest profit and update the
enveloping utility function accordingly.
We have
Theorem 3.3. For any given cost allocation, the market allocations for all
models are connected if the utility functions are accuracy-compatible.
Based on observations, we present the following corollaries without proof.
Corollary 3.4. In the case of bi(p, a′ i) = 0 , a′ i is a strictly monotonically in-
creasing function of p.
Corollary 3.5. For the case of (11), we have bi+1(pi+1, Aj) = 0.
8

3.3 Continuity of the revenue function
The goal of this subsection is to prove that ri+1(p) is a continuous function of
p under certain conditions. We have ( aq.−, aq,+](q = 1, 2, . . . , i) as the optimal
market allocation for T1, T2, · · ·, Ti. We then introduce the model Ti+1 to the
market. If there exists ( ak,−, aj,+] ∈ supp{bi} where ak,− /∈ supp{bi} and bi is
discontinuous at point aj,+ = Aj, then we denote ( ak,−, Aj] as a block. The
market allocation consists of a few blocks.
Lemma 3.6. We let bi+1(ρ, α) = 0 where bi+1(ρ, Aj) = bj(pj, Aj). For a price
p′ > 0, the equation bi+1(p′, a) = bi(a) > 0 can hold if a′ ∈ (ak,−, α] where
bi+1(p′, a′) = 0 and bi+1(p′, a) = bi(a) cannot hold if a′ ∈ (α, Aj].
Proof. For a′ ∈ (ak,−, α] we denote 0 = bi+1(p′, a′) < bi(a′). Note that p′ < ρ
by Corollary 3.4 and we have
bi+1(p′, Aj) > bi+1(ρ, Aj) = bj(pj, Aj) = bi(Aj). (14)
Since bi+1(p′, a) and bi(a) are both continuous in (ak,−, Aj], it leads tobi+1(p′, a) =
bi(a) > 0 is attainable. The situation of a′ ∈ (α, Aj] is similar and we omit the
details.
Theorem 3.7. For a block (ak,−, Aj], if a∗ i+1 is a continuous function of price
p and lim
a′ i+1→(ak,−)+
bi(p, a∗ i+1) = 0 where bi+1(p, a′ i+1) = 0, then revenue function
ri+1 of Ti+1 is a continuous function of a′ i+1 in this block. Moreover, if it
holds for all blocks, then ri+1 is continuous in [A, Ai+1] and it leads to ri is a
continuous function of the price.
Proof. We list all the endpoints in Subsection 3.2 and show that all of them are
continuous.
• For a′ i+1 = α, we haveri+1(α) = p R Ai+1 Aj λ(a)da and ri+1(a′ i+1) → p R Ai+1 Aj λ(a)da
for a′ i+1 → (α)−. For a′ i+1 → (α)+, we have, note that bi+1(p, a) < bi(a)
where a ∈ (a′ i+1, Aj], it also leads to ri+1(a′ i+1) = p R Ai+1 Aj λ(a)da.
• For a′ i+1 = ak,−, we have ri+1(a′ i+1) = p R Ai+1 a′ i+1 λ(a)da and ri+1(a′ i+1) →
p
R Ai+1
a′ i+1 λ(a)da if a′ i+1 → (ak,−)−. For a′ i+1 → (ak,−)+, if a∗ i+1 is at-
tainable, then by assumption, we have a∗ i+1 → a′ i+1 and ri+1(a′ i+1) →
p
R Ai+1
a′ i+1 λ(a)da. The conclusion is consistent in the case of a∗ i+1 not at-
tainable.
• For a′ i+1 = aj,+ ̸= aj+1,−, we have ri+1(a′ i+1) = p R Ai+1 a′ i+1 λ(a)da. For
a′ i+1 → (aj,+)+, it leads to ri+1(a′ i+1) → p R Ai+1 a′ i+1 λ(a)da by (10). For
a′ i+1 → (aj,+)−, if a∗ i+1 is attainable, then a′ i+1 ≤ a∗ i+1 < aj,+ and
ri+1(a′ i+1) → p R Ai+1 a′ i+1 λ(a)da. The conclusion is consistent in the case
of a∗ i+1 not attainable.
9

• For a′ i+1 = Ai, note that it is an endpoint of a block and ai,+ = Ai.
The left-continuity follows. For a′ i+1 → (Ai)+, we have ri+1(a′ i+1) =
p
R Ai+1
a′ i+1 λ(a)da → p
R Ai+1
Ai λ(a)da.
4 Dual and quasi-dual situation
We consider the dual and quasi-dual situation in this section, where the max-
imum permissible price for each buyer in the market is known, and our goal
is also to maximize the seller’s profit. We assume that the maximum permis-
sible price for buyers in the market follows a continuous distribution denoted
as µ(p). In this scenario, we continue to use dual generalized Hotelling’s law.
However, in this part, we abstract the unit price of the model as distance and
mark the precision of the model as characteristics on points, see Figure 4. We
aim to find a static pricing strategy and the corresponding market allocation
that maximizes the seller’s profit. Note that with a slight abuse of notation, we
use B = (b1, b2, · · ·, bn) in all situations.
4.1 Dual situation
We denote a class of functions B = ( b1, b2, · · ·, bn) as dual utility functions,
where each index corresponds to the price Pi allocated to model Ti. Similarly,
the independent variables of bi’s include the model accuracy a and the buyers’
maximum permissible price p. Properties are similar to the primal situation.
We denote Di,a = {p ∈ [0, P]|bi(a, p) ≥ 0} and denote P1 < P2 < · · ·< Pn.
Definition 4.1. We name the class of functions B = (b1, b2, · · ·, bn) are price-
compatible if for any i < jand fixed a, a′ ∈ [A, A], we denote Bij(p) = bi(a, p) −
bj(a′, p) and we have
• Bij(p) > 0 or Bij(p) < 0 in Di,a
T Dj,a′.
• If there exits p such that Bij(p) = 0, then Bij(p−) < 0 for Di,a
T Dj,a′ ∋
p− > pand Bij(p+) > 0 for Di,a
T Dj,a′ ∋ p+ < p.
Note that in Section 3, we have presented an algorithm for pricing strategy.
In this section, we interchange two variables from the previous section and,
therefore, omit the detailed algorithm for brevity.
4.2 Quasi-dual situation
We observe that due to duality, the assumption in the dual scenario also shifts
to the seller listing the pricing menu of all the models, rather than the cost
allocations. However, when we continue to employ the assumption from Section
3, namely that the seller can select a reasonable cost allocation to maximize
profit, the optimization mechanism in the dual scenario becomes inapplicable.
10

Therefore, we consider the quasi-dual scenario, where we reiterate the premises
and assumptions within this context.
We assume a class of functions B = (b1, b2, · · ·, bn) called quasi-dual utility
functions, where each index corresponds to the accuracy Ai allocated to the
model Ti. Similarly, the independent variables of bi’s include the model price
p and the buyers’ maximum permissible price ¯p, and p ≤ ¯p. We define Di,p =
{¯p ∈ [0, P]|bi(p, ¯p) ≥ 0}. We assume c1 < c2 < · · ·< cn.
Definition 4.2. We name the class of functions B = (b1, b2, · · ·, bn) are second-
type accuracy-compatible if for any i < j and fixed p, p′ ∈ [0, P], we denote
Bij(¯p) = bi(p, ¯p) − bj(p′, ¯p) and we have
• Bij(¯p) > 0 or Bij(¯p) < 0 in Di,pi
T Dj,pj .
• If there exits ¯p such that Bij(¯p) = 0, then Bij(¯p−) < 0 for Di,pi
T Dj,pj ∋
¯p− > ¯p and Bij(¯p+) > 0 for Di,pi
T Dj,pj ∋ ¯p+ < ¯p.
If there is one model sold in the market with price p, the corresponding cost
c1 and b1(p, ¯p1) = 0, we have
p1 = argmax
p
p
Z ¯p1
p
µ(¯p)d¯p. (15)
We rename the market allocation of T1 as [¯p1,−, ¯p1,+).
We assume two models T1 and T2 are sold in the market, and the corre-
sponding utility functions b1 and b2 are second-type accuracy-compatible. Let
b2(p, ¯p2) = 0 and b2(p, ¯p∗ 2) = b1(p1, ¯p∗ 2) > 0 if ¯p∗ 2 is attainable, we have
• If the T2’s market completely covers the T1’s, then we have
p2 = argmax
p
p
Z ¯p2
p
µ(¯p)d¯p, ¯p2 ≥ ¯p1,+, p ≤ ¯p1,−. (16)
• If there is market competition between T2 and T1, then we have
p2 = argmax
p
p1
Z ¯p∗ 2
¯p1,−
µ(¯p)d¯p + p
Z ¯p2
¯p∗ 2
µ(¯p)d¯p, ¯p1,+ ≥ ¯p∗ 2 ≥ ¯p1,−. (17)
• If there is no market competition between T1 and T2, meaning that the
buyers choosing these two models do not overlap, then we have
p2 = argmax
p
p
Z ¯p2
p
µ(¯p)d¯p, p > ¯p1,+. (18)
or
p2 = argmax
p
p
Z ¯p2
¯p1,+
µ(¯p)d¯p, ¯p1,− < p≤ ¯p1,+. (19)
We rename the market allocation of T1 and T2 as [¯p1,−, ¯p1,+) and [¯p2,−, ¯p2,+).
11

pricep2 p1
T2(with Accuracy A2) T1(with Accuracy A1)
0
buyer
Figure 4: Dual generalized Hotelling’s law
Remark 4.3. We give a brief explanation to show that the other situations are
impossible. We have
• If ¯p2,− < ¯p2,+ ≤ ¯p1,− < ¯p1,+, then we have b2(p2, ¯p1,−) > b1(p1, ¯p1,−)
which contradicts the fact that ¯p1,− is in the market allocation of T1.
• If the market allocation of T1 is not connected, then there exists p′ 1, p′ 2 and
p′′ 1 where 0 < b1(p1, p′ 1) < b2(p2, p′ 2) and b2(p2, p′ 2) < b1(p1, p′′ 1 ). It leads to
a contradiction that b1 and b2 are second-type accuracy-compatible. The
situation of T2 is similar.
Definition 4.4. We define i-th enveloping quasi-dual utility function of the
data chain s1 → s2 → · · · →si as
bi(¯p) =
(
bj(pj, ¯p) if ¯p ∈ [¯pj,−, ¯pj,+),
0 otherwise. (20)
The situation with arbitrary chain lengths can be generalized from the primal
situation and the quasi-dual situation with chain length of 2 combined. We omit
the details of this part.
4.3 Discussion on the data chains among four dimensions
In this section, we have conducted various forms of duality transformations
on the primal situation, specifically by interchanging the constraint conditions
associated with the two variables of accuracy and price to different extents. This
includes fully swapping all constraint conditions between these two variables,
as well as partially swapping some conditions while keeping others unchanged,
thereby deriving several distinct ’dual’ forms, see Table 1. Note that the fourth
scenario is not described in this paper. However, its properties and the method
for constructing its data chain can be derived analogously.
5 Dynamic pricing strategy: chain-like Nash equi-
librium
In the previous sections, we consider the static strategy where
• The goal of pricing Ti is to maximize the overall profit of T1, T2, · · ·, Ti.
• Once Ti has completed the pricing, T1, T2, · · ·, Ti−1 do not adjust their
prices further.
12

Table 1: Situation among four dimensions
Situations Optimized object Known market distribution Index of utility functions Variables of utility functions
Primal Accuracy Accuracy Accuracy (Price,Accuracy)
Dual Price Price Price (Accuracy,Price)
Quasi-dual Accuracy Price Accuracy (Price,Price)
Ultra-dual Price Accuracy Price (Accuracy,Accuracy)
In this section, we consider a different scenario named dynamic pricing strategy
and
• The goal of pricing Ti is to maximize the profit of Ti.
• The pricing strategy for Ti is based on its adjacent models, Ti−1 and Ti+1.
When the chain length is 1, the scenario is equivalent to a static pricing strat-
egy. For the case where the chain length is 2, we use the idea of bilateral game
theory in data markets from [D’acquisto et al.(2012)], which states that a Nash
equilibrium exists when the maximum points of the corresponding best response
functions for both players coincide. We consider the scenario where the chain
length is 2 and subsequently generalize it. Note that we incorporate an ad-
ditional assumption, namely, that each model will always be trained and sold
regardless of whether the profit is positive.
5.1 Two nodes example
When considering the scenario with two modelsT1 and T2, we note that whether
competition arises between the two models depends on the choice of T2. We
have
• In T1’s perspective If T2 competes with T1, i.e. b2(p2, A1) > 0, then
the optimal pricing strategy for T1 is, let b2(p2, a∗,+ 1 ) = b1(p, a∗,+ 1 ) and
b1(p, a′ 1) = 0,
p1 = argmax
p
p
Z a∗,+ 1
a′ 1
λ(a)da. (21)
If there is no competition between the two models, then the scenario for
T1 is the same as (1).
• In T2’s perspective For T2, it makes choice to compete with T1 or not.
Therefore, we calculate the maximum values in two different scenarios
separately to derive the optimal pricing strategy for T2. If T2 competes
13

with T1, we have, let b1(p1, a∗,− 2 ) = b2(p, a∗,− 2 ),
p2 = argmax
p
p
Z A2
a∗,− 2
λ(a)da. (22)
If T2 does not compete with T1, i.e. b2(p, A1) ≤ 0, we have
p2 = argmax
p
p
Z A2
a′ 2
λ(a)da. (23)
If there exist p1 and p2 such that they are respectively the optimal pricing
strategies for T1 and T2, then a Nash equilibrium exists.
5.2 General situation
We are now considering the pricing strategy for a data chain of length n. The
pricing strategy for T1 is given, and the pricing strategy of Tn is similar. For Ti,
we consider the left and right endpoints of its market allocation interval, noting
that the values of these endpoints essentially stem from the competitive game
between Ti and its neighboring models Ti−1 and Ti+1. We have
• The competitive game between Ti−1 and Ti In this case, Ti makes
choice to compete with Ti−1 or not. Therefore, we calculate the maximum
values in two different scenarios separately. If Ti competes with Ti−1, we
have, let bi−1(pi−1, a∗,− i ) = bi(p, a∗,− i ),
pi = argmax
p
p
Z ∗
a∗,− i
λ(a)da (24)
If Ti does not compete with Ti−1, i.e. b2(p2, A1) ≤ 0, we have
pi = argmax
p
p
Z ∗
a′ i
λ(a)da (25)
• The competitive game between Ti and Ti+1 If Ti+1 competes with
Ti, then the optimal pricing strategy for Ti is, let bi+1(pi+1, a∗,+ i ) =
bi(p, a∗,+ i ),
pi = argmax
p
p
Z a∗,+ i
∗
λ(a)da (26)
If there is no competition between the two models, then we have
pi = argmax
p
p
Z Ai
∗
λ(a)da (27)
14

If there exist p1, p2, · · ·, pn such that they are respectively the optimal pric-
ing strategies for Ti’s, then a Nash equilibrium exists.
We observe that, regardless of adopting dynamic pricing strategies or static
pricing strategies, we only consider the competitive game between adjacent mod-
els. This simplified form of the game problem aligns with real-world scenarios.
Remark 5.1. In this section, we omit the proof of the connectivity of the market
allocation for brevity. It is evident from the proof details of Theorem 3.3 that we
did not utilize the condition that pi is the optimal price under a static strategy.
This implies that, regardless of the prices arbitrarily assigned, the final market
allocation is always connected. Consequently, the connectivity of the market
allocation also holds in this section.
6 Applications: separable utility function
In this section, we discuss a special type of utility function, namely the separable
utility function, and present the possible values for pi’s in such a scenario. We
have
Definition 6.1. [Chen et al.(2022)]If bi(p, a) = fi(p)hi(a) or bi(p, a) = fi(p) +
hi(a) respectively, then bi is multiplicatively separable, or additively separable
respectively where fi is a function of p and hi is a function of a.
Note that in our paper, the additive separable utility function and the mul-
tiplicative separable utility function can be transformed into each other through
exponential or logarithmic transformations. Without loss of generality, we only
consider the additive separable scenario. We assume bi(p, a) = fi(p) + hi(a)
where fi and hi are differentiable.
Note that the revenue function ri(p) is continuous almost everywhere, im-
plying that the maximum value is attained only when the price p takes values
at the endpoints or stationary points. The computation of revenue correspond-
ing to the endpoints is straightforward. Moreover, the conclusion drawn in this
section is that, under the utility functions being separable, the expression for
the stationary points can be solved using differential equations. The goal of this
section is to calculate all the expressions of the stationary points,
6.1 Uniform distribution
There is one model sold in the market, then we have
p1 = argmax
p
p
Z A1
a′ 1
da = argmax
p
p(A1 − a′ 1). (28)
Now we calculate the stationary point and we have b1(p, a′ 1) = f1(p) +h1(a′ 1) =
0. It leads to a′ 1 = h−1 1 (−f1(p)), for which a′ 1 is a function of price p and we
denote a′ 1(η1) = ξ1. We have
(A1 − a′ 1(p)) − p da′ 1(p) dp = 0, (29)
15

and then p is the solution of the following equations
a′ 1 = h−1 1 (−f1(p)),
a′ 1 = A1 + η1(ξ1 − A1) p . (30)
In this case, the stationary point of r1 is the maximum point.
In the general case, i.e. i ≥ 2, we have
• For a′ i ∈ (ak−1,+, ak,−] where a′ i = h−1 i (−fi(p)), we havebi(f −1 i (−hi(a′ i)), a) >
bi−1(a) for a ∈ (a′ i, Ai−1]. We denote a′ i(ηi) = ξi and we have
pi = argmax
p
p(Ai − a′ i), a k−1,+ < a′ i ≤ ak,−. (31)
We calculate the stationary point and solve
(Ai − a′ i) − p da′ i(p) dp = 0. (32)
So the stationary point p is the solution of the following equations
a′ i = Ai + ηi(ξi − Ai) p ,
a′ i = h−1 i (−fi(p)).
(33)
Also, in the case of (11), we have pi = f −1 i (hi(Aj)).
• Let a′ i ∈ (ak,−, ak,+] and bi(p, a∗ i ) = bi−1(a∗ i ) = bj(pj, a∗ i ) where a∗ i ∈
(aj,−, aj,+]. In this case, we have
pi = argmax
p
p(Ai−a∗ i )+pj(a∗ i −aj,−), a k,− < a′ i ≤ ak,+, a j,− < a∗ i ≤ aj,+
(34)
where
a∗ i = (hi − hj)−1(fj(pj) − fi(p)). (35)
We solve, denote a∗ i (ψi) = ϕi,
Ai − a∗ i − (p − pj) da∗ i dp = 0. (36)
The stationary point p is the solution of the following equations
a∗ i = Ai + ϕi − Ai (ψi − pj)(p − pj) ,
a∗ i = (hi − hj)−1(fj(pj) − fi(p)).
(37)
• If a′ i ∈ (Ai−1, Ai], then we have
pi = argmax
p
p(Ai − a′ i)da, A i−1 < a′ i ≤ Ai, (38)
16

and
(Ai − a′ i(p)) − p da′ i(p) dp = 0. (39)
It leads to p is the solution of the following equations
a′ i = h−1 i (−fi(p)),
a′ i = Ai + ηi(ξi − Ai) p . (40)
6.2 Continuous distribution
We define the cumulative distribution function (CDF) of λ(a) as F (a). There
is one model sold in the market, then we have
p1 = argmax
p
p
Z A1
a′ 1
λ(a)da = argmax
p
p(F (A1) − F (a′ 1)) (41)
Now we calculate the stationary point, where it is also the maximum point. We
have
(F (A1) − F (a′ 1)) − p dF (a′ 1) dp = 0. (42)
then p is the solution of the following equations
a′ 1 = h−1 1 (−f1(p)),
a′ 1 = F −1(F (A1) + η1(ξ1 − A1) p ). (43)
In the general case, i.e. i ≥ 2, we have
• If a′ i ∈ (ak−1,+, ak,−] and bi(f −1 i (−hi(a′ i)), a) > bi−1(a) in (a′ i, Ai−1], then,
similarly, we calculate the stationary point of (10) and solve
(F (Ai) − F (a′ i)) − p dF (a′ i) dp = 0. (44)
It leads to
a′ i = h−1 i (−fi(p)),
a′ i = F −1(F (Ai) + ηi(ξi − Ai) p ). (45)
Also, in the case of (11), we have pi = f −1 i (hi(Aj)).
• If a′ i ∈ (ak,−, ak,+] and bi(p, a∗ i ) = bi−1(a∗ i ) where a∗ i ∈ (aj,−, aj,+], then
we have
a∗ i = (hi − hj)−1(fj(pj) − fi(p)). (46)
We calculate the stationary point of (12), and
a∗ i = F −1(F (Ai) + ϕi − Ai (ψi − pj)(p − pj) ),
a∗ i = (hi − hj)−1(fj(pj) − fi(p)).
(47)
17

• If a′ i ∈ (Ai−1, Ai], then we calculate the stationary point of (13) and
a′ i = h−1 i (−fi(p)),
a′ i = F −1(F (Ai) + ηi(ξi − Ai) p ). (48)
7 Incomplete information game
We consider incomplete information games, where a discrepancy exists between
the seller’s known utility functions and the true utility functions of the buyers.
The goal of this section is to demonstrate that our method remains robust under
such errors and provide an error analysis for the revenue of a single model. We
recall the notation in Section 3, and bi’s are the utility functions known to the
seller. We denote bi’s are the true utility functions in the market corresponding
to the cost ci, and Λ = sup λ(a). We present the following assumptions:
• For the utility functions known to the seller, we assume
αi,p|a − a′| ≤ |bi(p, a) − bi(p, a′)| ≤βi,p|a − a′| (49)
where 0 < α1 < β1 < α2 < β2 < · · ·< αn < βn. We use a slight abuse
of notation and denote αi,p = αi and βi,p = βi if it does not introduce
ambiguity.
• The true utility function bi are also continuous and accuracy-compatible.
For the errors between the utility functions known to the seller and the
true functions, we assume
|bi(p, a) − bi(p, a)| < ϵi(p). (50)
• We assume, for i < jand p < p′,
0 > lim
a→A
bi(p, a) > lim a→A bj(p′, a), 0 > lim a→A bi(p, a) > lim a→A bi(p′, a), (51)
We recall Section 3 and the corresponding optimal revenue of Ti is
ri = pi
Z ai,+
ai,−
λ(a)da (52)
where ri − ci > 0. Note that in this case, we have ai,− ∈ {a′ i, a∗ i } and ai,+ ∈
{Ai, a∗ i+1} if a∗ i and a∗ i+1 are attainable.
Now we calculate the true revenue. We denotebi(pi, a′ i) = 0 and bj(pj, a∗ j ) =
bi(pi, a∗ j ) > 0 if a∗ j is attainable, then
ri = max{pi
Z ai,+
ai,−
λ(a)da, 0} (53)
18

where
ai,− = max{a′ i, a∗ j , j= 1, 2, . . . , i−1}, ai,+ = min{Ai, a∗ j , j= i+1, i+2, . . . , n}.
(54)
It leads to
|ri − ri| ≤piΛ(|ai,− − ai,−| + |ai,+ − ai,+|). (55)
We calculate the error bound through classified discussion.
• If ai,− = a′ i and ai,− = a′ i, then we have
|a′ i − a′ i| ≤1 αi |bi(pi, a′ i) − bi(pi, a′ i)| = 1 αi |bi(pi, a′ i) − bi(pi, a′ i)| < ϵi(pi) αi .
(56)
• If ai,− = a∗ i and ai,− = a∗ i−1, then we recall Bi,i−1(a) = bi(pi, a) −
bi−1(pi−1, a) and let Bi,i−1(a) = bi(pi, a) − bi−1(pi−1, a). So Bi,i−1(a∗ i ) =
Bi,i−1(a∗ i−1) = 0. We have
|Bi,i−1(a∗ i )−Bi,i−1(a∗ i )| ≤ |bi(pi, a∗ i )−bi(pi, a∗ i )|+|bj(pj, a∗ i )−bj(pj, a∗ i )| < ϵi(pi)+ϵj(pj)
(57)
and
|Bi,i−1(a∗ i−1) − Bi,i−1(a∗ i−1)| = |Bi,i−1(a∗ i−1) − Bi,i−1(a∗ i )|
= |bi(pi, a∗ i ) − bi−1(pi−1, a∗ i ) − bi(pi, a∗ i ) + bi−1(pi−1, a∗ i )|
≥ ||bi(pi, a∗ i )−bi(pi, a∗ i )|−|bi−1(pi−1, a∗ i )−bi−1(pi−1, a∗ i )|| ≥(αi−βi−1)|a∗ i−1−a∗ i−1|
(58)
It leads to
|a∗ i − a∗ i−1| < ϵi(pi) + ϵj(pj) αi − βi−1 (59)
• If ai,− = a′ i and ai,− = a∗ j where j ̸= i − 1, then a′ i ≥ Aj ≥ a∗ j and a∗ j ≥ a′ i
due to the the monotonicity of bj. So |a′ i − a∗ j | ≤ |a′ i − a′ i| < ϵi(pi) αi .
• If ai,− = a∗ i , ai,− = a∗ j where j ̸= i − 1 and bi(pi, a∗ j ) = bj(pj, a∗ j ) is
attainable, then we have a∗ i > a∗ j and a∗ j ≥ a∗ i−1. It leads to
|a∗ i −a∗ j | ≤max{|a∗ i −a∗ i−1|, |a∗ j −a∗ j |} ≤max{ ϵi(pi) + ϵi−1(pi−1) αi − βi−1 , ϵi(pi) + ϵj(pj) αi − βj }.
(60)
If a∗ j is not attainable, then a∗ i > Aj > a∗ j ≥ a∗ i−1. It leads to
|a∗ i − a∗ j | < |a∗ i − a∗ i−1| < ϵi(pi) + ϵi−1(pi−1) αi − βi−1 (61)
• If ai,− = a∗ i and a = a′ i, then we have, if a′ i ≥ Ai−1, then a′ i ≥ Ai−1 ≥
a∗ i > a′ i and
|a∗ i − a′ i| < |a′ i − a′ i| < ϵi(pi) αi . (62)
19

If a′ i < Ai−1, then a∗ i is attainable due to bi−1(pi−1, Ai−1) ≤ bi(pi, Ai−1).
It leads to
|a′ i − a∗ i | ≤max{|a∗ i − a∗ i−1|, |a′ i − a′ i|} ≤max{ ϵi(pi) + ϵi−1(pi−1) αi − βi−1 , ϵi(pi) αi }.
(63)
• If ai,+ = a∗ i+1 and ai,+ = a∗ i+1, then we have, similar to (59),
|a∗ i − a∗ i+1| < ϵi(pi) + ϵi+1(pi+1) βi+1 − αi (64)
• If ai,+ = a∗ i+1 and ai,+ = a∗ j where j ̸= i + 1, then similar to (60), we have
|a∗ i −a∗ j | ≤max{|a∗ i −a∗ i+1|, |a∗ j −a∗ j |} ≤max{ ϵi(pi) + ϵi+1(pi+1) βi+1 − αi , ϵi(pi) + ϵj(pj) βj − αi }
(65)
if a∗ j is attainable, and
|a∗ i − a∗ j | < |a∗ i − a∗ i−1| < ϵi(pi) + ϵi+1(pi+1) βi+1 − αi (66)
if a∗ j is not attainable.
• If ai,+ = Ai and ai,+ = a∗ j , then we have, note that Bi,j(Ai) > 0,
Bi,j(Ai) ≤ 0, and Bi,j(a∗ j ) > 0,
|Bi,j(Ai) − Bi,j(Ai)| ≥ |Bi,j(Ai) − Bi,j(a∗ i )| ≥(βj − αi)|Ai − a∗ i | (67)
It leads to
|Ai − a∗ i | ≤ϵi(pi) + ϵi+1(pj) βj − αi . (68)
• If a = a∗ i and a = Ai, then we have, note thatBi.i+1(Ai) < 0, Bi,i+1(Ai) >
0, and Bi,i+1(a∗ i ) = 0,
|Bi,i+1(Ai) − Bi,i+1(Ai)| ≥ |Bi,i+1(Ai) − Bi,i+1(a∗ i )| ≥(βi+1 − αi)|Ai − a∗ i |
(69)
It leads to
|Ai − a∗ i | ≤ϵi(pi) + ϵi+1(pi+1) βi+1 − αi . (70)
8 Conclusions
We study to trade models instead of datasets themselves in this paper, and we
have introduced a novel transaction mechanism in the data market. Given the
reproducibility of data, we train the data multiple times to produce models of
varying accuracy levels, catering to diverse market demands. We employ the
generalized Hotelling’s law to describe the market preferences for these mod-
els and the competitive scenario. Based on this scenario, we select the most
appropriate cost allocation strategy to ensure maximum profit maximization.
20

References
[Agarwal et al.(2019)] Anish Agarwal, Munther Dahleh, and Tuhin Sarkar.
2019. A marketplace for data: An algorithmic solution. In Proceedings
of the 2019 ACM Conference on Economics and Computation . 701–726.
[Amiri et al.(2023)] Mohammad Mohammadi Amiri, Frederic Berdoz, and
Ramesh Raskar. 2023. Fundamentals of task-agnostic data valuation. In
Proceedings of the AAAI Conference on Artificial Intelligence , Vol. 37.
9226–9234.
[Brown(1989)] Stephen Brown. 1989. Retail location theory: The legacy of
Harold Hotelling .
[Chen et al.(2022)] Junjie Chen, Minming Li, and Haifeng Xu. 2022. Selling
data to a machine learner: Pricing via costly signaling. In International
Conference on Machine Learning . PMLR, 3336–3359.
[Chen et al.(2019)] Lingjiao Chen, Paraschos Koutris, and Arun Kumar. 2019.
Towards Model-based Pricing for Machine Learning in a Data Market-
place. In Proceedings of the 2019 International Conference on Manage-
ment of Data (Amsterdam, Netherlands) (SIGMOD ’19) . Association
for Computing Machinery, New York, NY, USA, 1535–1552. https:
//doi.org/10.1145/3299869.3300078
[D’acquisto et al.(2012)] Giuseppe D’acquisto, Marta Flamini, and Maurizio
Naldi. 2012. A game-theoretic formulation of security investment decisions
under ex-ante regulation. In Information Security and Privacy Research:
27th IFIP TC 11 Information Security and Privacy Conference, SEC 2012,
Heraklion, Crete, Greece, June 4-6, 2012. Proceedings 27 . Springer, 412–
423.
[Egan and Oren(2024)] Malcolm Egan and Nir Oren. 2024. Package Exchange
Mechanisms with Quality Constraints for Data Markets. (2024).
[Guo et al.(2015)] Wen-Chung Guo, Fu-Chuan Lai, and Dao-Zhi Zeng. 2015. A
Hotelling model with production. Mathematical Social Sciences 73 (2015),
40–49.
[Huang et al.(2023)] Baihe Huang, Sai Praneeth Karimireddy, and Michael I
Jordan. 2023. Evaluating and Incentivizing Diverse Data Contributions in
Collaborative Learning. arXiv preprint arXiv:2306.05592 (2023).
[Jia et al.(2019)] Ruoxi Jia, David Dao, Boxin Wang, Frances Ann Hubis, Nick
Hynes, Nezihe Merve G¨ urel, Bo Li, Ce Zhang, Dawn Song, and Costas J
Spanos. 2019. Towards efficient data valuation based on the shapley value.
In The 22nd International Conference on Artificial Intelligence and Statis-
tics. PMLR, 1167–1176.
21

[Karlaˇ s et al.(2022)] Bojan Karlaˇ s, David Dao, Matteo Interlandi, Bo Li, Sebas-
tian Schelter, Wentao Wu, and Ce Zhang. 2022. Data debugging with shap-
ley importance over end-to-end machine learning pipelines. arXiv preprint
arXiv:2204.11131 (2022).
[Liu and Pelechrinis(2019)] Xin Liu and Konstantinos Pelechrinis. 2019. A
Data-Driven Examination of Hotelling’s Linear City Model. In Proceed-
ings of the 10th ACM Conference on Web Science (Boston, Massachusetts,
USA) (WebSci ’19). Association for Computing Machinery, New York, NY,
USA, 165–169. https://doi.org/10.1145/3292522.3326020
[Pei(2020)] Jian Pei. 2020. A survey on data pricing: from economics to data
science. IEEE Transactions on knowledge and Data Engineering 34, 10
(2020), 4586–4608.
[Ravindranath et al.(2023)] Sai Srivatsa Ravindranath, Yanchen Jiang, and
David C Parkes. 2023. Data market design through deep learning. Ad-
vances in Neural Information Processing Systems 36 (2023), 6662–6689.
[Shokri et al.(2012)] Reza Shokri, George Theodorakopoulos, Carmela Tron-
coso, Jean-Pierre Hubaux, and Jean-Yves Le Boudec. 2012. Protecting
location privacy: optimal strategy against localization attacks. In Pro-
ceedings of the 2012 ACM conference on Computer and communications
security. 617–627.
[Sun et al.(2024)] Peng Sun, Liantao Wu, Zhibo Wang, Jinfei Liu, Juan Luo,
and Wenqiang Jin. 2024. A Profit-Maximizing Data Marketplace with Dif-
ferentially Private Federated Learning under Price Competition. Proc.
ACM Manag. Data 2, 4, Article 191 (Sept. 2024), 27 pages. https:
//doi.org/10.1145/3677127
[Yu et al.(2023)] Yi Yu, Shengyue Yao, Juanjuan Li, Fei-Yue Wang, and Yilun
Lin. 2023. SWDPM: A social welfare-optimized data pricing mechanism.
In 2023 IEEE International Conference on Systems, Man, and Cybernetics
(SMC). IEEE, 2900–2906.
[Zhang et al.(2023)] Mengxiao Zhang, Fernando Beltr´ an, and Jiamou Liu. 2023.
A Survey of Data Pricing for Data Marketplaces. IEEE Transactions on
Big Data (2023).
22
