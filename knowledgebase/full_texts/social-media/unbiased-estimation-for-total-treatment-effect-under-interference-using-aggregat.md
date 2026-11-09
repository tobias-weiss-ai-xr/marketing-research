---
title: Unbiased Estimation for Total Treatment Effect Under Interference Using Aggregated Dyadic Data
url: https://arxiv.org/abs/2402.12653
category: social-media
subcategory: empirical
date: 2024-02
venue: ''
authors:
- Lu Deng
- Yilin Li
- JingJing Zhang
- Yong Wang
- Chuan Chen
source: arxiv
pdf_url: https://arxiv.org/pdf/2402.12653
pages: 11
chars: 49752
fetched_at: '2026-11-08T13:11:43+00:00'
kb_version: 1
---

# Unbiased Estimation for Total Treatment Effect Under Interference Using Aggregated Dyadic Data

Unbiased Estimation for Total Treatment Effect Under
Interference Using Aggregated Dyadic Data
Lu Deng
Tencent, Inc.
Shenzhen, Guangdong, China
adamdeng@tencent.com
Yilin Li
Peking University
Beijing, China
yilinli@pku.edu.cn
JingJing Zhang
Tencent, Inc.
Shenzhen, Guangdong, China
broccozhang@tencent.com
Yong Wang
Tencent, Inc.
Shenzhen, Guangdong, China
darwinwang@tencent.com
Chuan Chen
Tencent, Inc.
Shenzhen, Guangdong, China
chuanchen@tencent.com
ABSTRACT
In social media platforms, user behavior is often influenced by in-
teractions with other users, complicating the accurate estimation
of causal effects in traditional A/B experiments. This study inves-
tigates situations where an individual’s outcome can be broken
down into the sum of multiple pairwise outcomes, a reflection of
user interactions. These outcomes, referred to as dyadic data, are
prevalent in many social network contexts. Utilizing a Bernoulli
randomized design, we introduce a novel unbiased estimator for
the total treatment effect (TTE), which quantifies the difference in
population mean when all individuals are assigned to treatment
versus control groups. We further explore the bias of our estimator
in scenarios where it is impractical to include all individuals in the
experiment, a common constraint in online control experiments.
Our numerical results reveal that our proposed estimator consis-
tently outperforms some commonly used estimators, underscoring
its potential for more precise causal effect estimation in social media
environments.
CCS CONCEPTS
• Probability and Statistics→ Experimental design; • Mathe-
matics of computing→ Exploratory data analysis.
KEYWORDS
causal inference, interference, network effects, total treatment effect,
online control experiment, dyadic data
ACM Reference Format:
Lu Deng, Yilin Li, JingJing Zhang, Yong Wang, and Chuan Chen. 2024.
Unbiased Estimation for Total Treatment Effect Under Interference Using
Aggregated Dyadic Data . In Proceedings of the ACM SIGKDD Conference
on Knowledge Discovery and Data Mining 2024 (KDD’24). ACM, Barcelona,
Spain, 11 pages. https://doi.org/XXXXXXX.XXXXXXX
Permission to make digital or hard copies of all or part of this work for personal or
classroom use is granted without fee provided that copies are not made or distributed
for profit or commercial advantage and that copies bear this notice and the full citation
on the first page. Copyrights for components of this work owned by others than ACM
must be honored. Abstracting with credit is permitted. To copy otherwise, or republish,
to post on servers or to redistribute to lists, requires prior specific permission and/or a
fee. Request permissions from permissions@acm.org.
KDD’24, August 25–29, 2024, Barcelona, Spain
© 2024 Association for Computing Machinery.
ACM ISBN 978-1-4503-XXXX-X/18/06. . . $15.00
https://doi.org/XXXXXXX.XXXXXXX
1 INTRODUCTION
Online control experiments provide robust methodologies for tech
companies to assess the impact of innovative product strategies
[18, 19]. In such experiments, the population is randomly divided
into a treatment group, which receives the treatment under in-
vestigation, and a control group, which maintains the status quo.
The treatment effect is then estimated by comparing the difference
in outcomes between these two groups post-treatment. Classical
causal inference techniques for estimating these effects rely on the
Stable Unit Treatment Value Assumption (SUTVA). SUTVA posits
that an individual’s outcome is independent of the treatment as-
signments of others, ensuring that there is no interference between
units. In scenarios where SUTVA is valid, the difference-in-means
estimator or Horvitz-Thompson estimator provides an unbiased
estimate of the treatment effect [16].
However, social network settings commonly violate the SUTVA,
as an individual’s behavior can be influenced by their social con-
nections [10, 13, 17, 26, 35]. This violation may introduce bias into
estimates from traditional randomized experiments. For instance,
consider a social media platform testing a feature to promote user
messaging. This feature could inadvertently stimulate friends in the
control group to increase their messaging activity. Consequently,
both the treatment and control groups exhibit increased activity,
potentially leading to an underestimation of the treatment’s actual
effect. This phenomenon, known as network effects, is also referred
to as interference, spillover, or peer influence effects. Our primary
focus is to estimate the difference in population mean outcomes
when all individuals are assigned to either the treatment or control
group.
Causal inference amidst interference has attracted increasing in-
terest from academia and industry in recent decades. There are two
primary methods to address this: the design-based approach and
the model-assisted approach. The design-based approach aims to re-
duce bias in effect estimation by strategically assigning treatments.
One such method is graph cluster randomization [ 13, 14, 35, 36],
which groups a network into clusters and treats each cluster as a
whole. While this can reduce bias, it may also decrease the precision
of results and is not suitable for highly interconnected networks.
Another method is LinkedIn’s ego-cluster experiment [28], which
focuses on individuals and their direct connections. However, this
method has low power and may still introduce bias. The model-
assisted approach involves constructing mathematical models of
arXiv:2402.12653v1  [cs.SI]  20 Feb 2024

KDD’24, August 25–29, 2024, Barcelona, Spain Lu Deng, Yilin Li, Jingjing Zhang, Yong Wang, and Chuan Chen
potential outcomes and estimating parameters to understand effects
[5, 6, 11, 27, 29, 32, 34]. The exposure model [2, 24] is an example
of this approach, simplifying the treatment information into "expo-
sures" to study causal effects. However, this approach assumes that
these exposures fully encapsulate the causal relationships, which
may not always be the case. Recent research has explored the impli-
cations of incorrect models and found that some estimators can still
be reliable under broader interference conditions, but determining
the conditions remains challenging [8, 20, 30, 31].
This work’s primary contribution is the development of novel es-
timators for interference within the context of dyadic data. Dyadic
data, capturing interactions between pairs of users (dyads), enables
the investigation of complex dynamics and relationships among
users. For example, in social network analysis, dyads may refer
to individuals within a network. Utilizing dyadic information al-
lows researchers to gain insights into intricate interactive behavior.
Dyadic data analysis is crucial across various scientific disciplines,
including economics [25], social sciences [1], and biomedical sci-
ences [23]. To our knowledge, we are the first to propose using
aggregated dyadic data to estimate treatment effects amidst inter-
ference. We introduce and analyze several new estimators that
incorporate dyadic structures under different experimental scenar-
ios. The proposed framework is easy to set up and is widely run
at Weixin’s experiment platform. Our simulation results validate
the theorems and demonstrate the performance of the proposed
estimators. In summary, our contributions include:
(1) Formalizing the potential outcome model with dyadic out-
comes and providing an unbiased estimator of the total treat-
ment effect under a simple randomized experiment.
(2) Offering a detailed analysis of our estimator when the ex-
periment includes only a small fraction of the population.
(3) Proposing a novel experimental scheme that uses clustering
to reduce the bias of the estimator in subpopulation experi-
ments.
(4) Conducting systematic simulations on two social networks
and comparing our method with traditional estimators, thereby
providing a credible reference for our method’s effectiveness.
The structure of this paper is as follows: Section 2 provides an
initial discussion on the potential outcome model and network
interference. Section 3 details our proposed estimators. Section 4
presents simulation studies and a real-world example that corrobo-
rates our theoretical findings. Section 5 concludes with a thorough
discussion. Appendix A contains the proofs of some of our theoret-
ical results.
2 PROBLEM SETTING
In this section, we’ll formalize the problem of causal inference
under interference, discuss some commonly used assumptions, and
describe the structure of dyadic data.
2.1 Potential outcome model
Consider a finite population of𝑛 individuals. Let𝑊𝑖∈{ 0, 1} rep-
resent the random binary treatment assignment for individuals
𝑖, where 1 and 0 denote treatment and control, respectively. Let
W =(𝑊1,...,𝑊 𝑛)⊺ ∈ Ω Δ={0, 1}𝑛, a vector of length 𝑛, be the
experiment assignment vector for all individuals. Let𝑌𝑖(W) denote
the potential outcome for individual 𝑖 if the treatment vector W
is implemented. Our goal is to estimate the total treatment effect
(TTE). TTE is defined as the difference in population mean when
all individuals are placed in treatment versus control, which can be
expressed as
𝜏 Δ= 1 𝑛 𝑛∑︁ 𝑖=1 h 𝑌𝑖(W = 1)− 𝑌𝑖(W = 0) i . (1)
where 1 =(1,..., 1)⊺, 0 =(0,..., 0)⊺. In what follows, expectations
E are over the treatment assignment only, potential outcomes are
considered fixed. Under SUTVA,𝑌𝑖(W) = 𝑌𝑖(𝑊𝑖) for all W∈ Ω.
Therefore, TTE can be simplified as
𝜏 = 1 𝑛 𝑛∑︁ 𝑖=1 h 𝑌𝑖(𝑊𝑖 = 1)− 𝑌𝑖(𝑊𝑖 = 0) i . (2)
A commonly used estimator for𝜏 is the difference-in-means esti-
mator, defined by
ˆ𝜏𝑑𝑖𝑚 =
˝𝑛
𝑖=1𝑊𝑖𝑌𝑖˝𝑛
𝑖=1𝑊𝑖
−
˝𝑛
𝑖=1(1−𝑊𝑖)𝑌𝑖˝𝑛
𝑖=1(1−𝑊𝑖) . (3)
Under Bernoulli randomization or complete randomization, ˆ𝜏𝑑𝑖𝑚 is
an unbiased estimator for𝜏 [16]. However, when interference exits,
ˆ𝜏𝑑𝑖𝑚 is biased and fails to provide a valid estimate of𝜏[10, 13].
2.2 Network Graph
In the following sections, we consider that the interference can be
characterized by a directed graph𝐺 =(𝑉,𝐸), where the node set
𝑉 ={1, 2,...,𝑛 } represents the individuals, and𝐸 ={(𝑖,𝑗)} is the
collection of edges that represent interference between individuals.
We use|𝐸| to denote the cardinality of 𝐸, which is the number
of edges in the graph. Each graph is represented by an adjacency
matrix. Let𝐴 be an𝑛×𝑛 matrix with entries(𝐴𝑖𝑗)1≤𝑖,𝑗≤𝑛 where
𝐴𝑖𝑗 ∈{ 0, 1} with𝐴𝑖𝑖 = 0, and for𝑖 ≠ 𝑗,
𝐴𝑖𝑗 Δ=
(
0 no edge between𝑖 and 𝑗
1 direct edge from𝑖 to 𝑗. (4)
We let𝑁𝑢(𝑗) Δ={𝑖 :𝐴𝑖𝑗 = 1} and𝑁𝑑(𝑗) Δ={𝑖 :𝐴𝑗𝑖 = 1} represent
the upstream neighbors and downstream neighbors set of user 𝑗
with respect to the graph, respectively. Throughout the article, we
assume that the network graph𝐺 is fixed and known.
2.3 Neighborhood Interference
The neighborhood interference assumption [9, 12, 22, 36, 39] posits
that an individual’s outcome depends solely on the treatment as-
signments of their direct neighbors within a specified network. This
assumption is frequently utilized when addressing interference, as
it simplifies the problem by focusing on local interactions.
(A1) (Neighborhood Interference) The potential outcomes only
depend on one’s own and neighbors’ treatment assignments:
𝑌𝑖(W) = 𝑌𝑖(W′) if𝑊𝑖 = 𝑊′ 𝑖 and𝑊𝑗 = 𝑊′ 𝑗 for all 𝑗 ∈
𝑁𝑢(𝑖)∪ 𝑁𝑑(𝑖).
Assuming neighborhood interference, the Horvitz-Thompson
estimator combined with exposure mapping can be employed to
estimate the total treatment effect [3]. However, the practical ap-
plication of such estimators is often hindered by their substantial

Unbiased Estimation for Total Treatment Effect Under Interference Using Aggregated Dyadic Data KDD’24, August 25–29, 2024, Barcelona, Spain
variances or their dependence on stringent exposure mapping as-
sumptions.
2.4 Dyadic data setup
To estimate the total treatment effect, we propose an assumption
that is applicable in real-world scenarios and pertains to potential
outcomes. We denote the network graph characterizing the inter-
ference as𝐺 =(𝑉,𝐸), and adopt the neighborhood interference
assumption (A1). In a given scenario, each direct edge (𝑖,𝑗)∈ 𝐸
is associated with an outcome, represented as 𝑧𝑖,𝑗 . The outcome
for unit 𝑗, denoted as 𝑌𝑗 , is defined as the summation of these
associated outcomes from its upstream neighbors.
𝑌𝑗 =
∑︁
𝑖∈𝑁𝑢(𝑗)
𝑧𝑖,𝑗. (5)
Example 2.1. Within the framework of content sharing and for-
warding, consider a scenario where a user𝑖 forwards a video to another
user 𝑗. Upon receiving the video, user 𝑗 clicks on it, leading to the
sharing page, and then watches the video. This action results in a
stay duration, denoted by 𝑧𝑖,𝑗 . The cumulative stay duration on the
sharing page for user 𝑗 over a specific period is calculated by sum-
ming up the stay durations𝑧𝑖,𝑗 , each of which is generated by clicking
on videos forwarded by friends. In the absence of any forwarding
or clicking interaction between user 𝑖 and user 𝑗, we assign 𝑧𝑖,𝑗 a
value of 0, signifying that no stay duration is generated under such
circumstances.
It’s important to note that𝑧𝑖,𝑗 does not necessarily need to be
symmetric for the pair(𝑖,𝑗), which means that𝑧𝑖,𝑗 ≠𝑧𝑗,𝑖 is permissi-
ble. Additionally, we set𝑧𝑖,𝑖 = 0, indicating that we are considering
a graph without a self-loop. The value of 𝑧𝑖,𝑖 will influence the
properties of our estimators, a point that will be illustrated in the
subsequent section. For each unit𝑗, we denote𝐷𝑗 as the summation
of paired outcomes from downstream neighbors:
𝐷𝑗 =
∑︁
𝑖∈𝑁𝑑(𝑗)
𝑧𝑗,𝑖. (6)
We refer to𝐷𝑗 as the diffusion metric, as it characterizes the spillover
effect from individual 𝑗 diffusing to all of his neighbors. Moreover,
we refer to𝑌𝑗 and𝐷𝑗 as aggregated dyadic data. For a more de-
tailed understanding of how𝑌𝑖 and𝐷𝑖 are calculated, please refer
to Figure 1, which provides a visual representation of this process.
The forms of𝑌𝑖 and𝐷𝑖 exhibit a kind of duality: one is a summa-
tion from upstream neighbors, and the other is from downstream
neighbors. In fact, it can be shown that ˝𝑛 𝑗=1𝑌𝑗 = ˝𝑛 𝑗=1𝐷𝑗 . Thus,
the total treatment effect defined by𝑌𝑖 and𝐷𝑖 are identical. If we
denote𝑧𝑖,𝑗(W),𝑌𝑗(W) and𝐷𝑗(W) as the counterfactual outcomes
under treatment vector W, then
𝜏 = 1 𝑛 𝑛∑︁ 𝑖=1 h 𝑌𝑖(W = 1)−𝑌𝑖(W = 0) i = 1 𝑛 𝑛∑︁ 𝑖=1 h 𝐷𝑖(W = 1)−𝐷𝑖(W = 0) i .
In past studies, researchers have only used𝑌𝑖 to estimate the total
treatment effect. Our work demonstrates that we can leverage the
information provided by𝐷𝑗 to construct a more accurate estimate.
Figure 1: An illustration of the calculation of 𝑌𝑖 and𝐷𝑖 . Sup-
pose node 𝑖 has 7 neighbor nodes, where nodes 1,2,3,4 are
upstream neighbors, and nodes 5,6,7 are downstream neigh-
bors. Each direct edge is associated with an outcome. 𝑌𝑗 is
the summation of the paired outcomes from upstream neigh-
bors, which is 𝑧1,𝑗+𝑧2,𝑗+𝑧3,𝑗+𝑧4,𝑗 .𝐷𝑗 is the summation of
the paired outcomes from downstream neighbors, which is
𝑧𝑗,5+𝑧𝑗,6+𝑧𝑗,7.
3 METHODOLOGY
In this section, we will delineate the fundamental assumption that
forms the basis of our approach, introduce the novel estimator we
have developed, and conduct an in-depth analysis of the perfor-
mance of this estimator under a variety of conditions.
3.1 Dyadic Interference
Our overarching framework necessitates an interference assump-
tion on the dyadic outcome𝑧𝑖,𝑗(W).
(A2) For each(𝑖,𝑗), the potential outcomes𝑧𝑖,𝑗(W) only depend
on unit𝑖 and unit𝑗’s treatment assignments: for anyW, W′∈
Ω, if𝑊𝑖 =𝑊′ 𝑖 and𝑊𝑗 =𝑊′ 𝑗 , then𝑧𝑖,𝑗(W) =𝑧𝑖,𝑗(W′).
Assumption (A2) embodies a specific form of the neighbor interfer-
ence assumption, which is plausible considering that most dyadic
data originate from pairwise interactions between units. Under this
assumption, we further propose that 𝑧𝑖,𝑗(W) can be modeled as
follows:
𝑧𝑖,𝑗(W) =𝛼𝑖,𝑗+𝛽𝑖,𝑗𝑊𝑖+𝛾𝑖,𝑗𝑊𝑗+𝜁𝑖,𝑗𝑊𝑖𝑊𝑗. (7)
The parameters𝛽𝑖,𝑗 and𝜁𝑖,𝑗 are intended to capture network inter-
ference, specifically addressing the potential spillover effect. On the
other hand,𝛾𝑖,𝑗 is designed to capture the direct effect of treatment.
Given (7), we can expand𝑌𝑗(W) and𝐷𝑗(W) as
𝑌𝑗(W) =
∑︁
𝑖∈𝑁𝑢(𝑗)

𝛼𝑖,𝑗+𝛽𝑖,𝑗𝑊𝑖+𝛾𝑖,𝑗𝑊𝑗+𝜁𝑖,𝑗𝑊𝑖𝑊𝑗

, (8)
and
𝐷𝑗(W) =
∑︁
𝑖∈𝑁𝑑(𝑗)

𝛼𝑗,𝑖+𝛽𝑗,𝑖𝑊𝑗+𝛾𝑗,𝑖𝑊𝑖+𝜁𝑗,𝑖𝑊𝑖𝑊𝑗

. (9)

KDD’24, August 25–29, 2024, Barcelona, Spain Lu Deng, Yilin Li, Jingjing Zhang, Yong Wang, and Chuan Chen
The total treatment effect estimand𝜏 takes the value
𝜏 = 1 𝑛 𝑛∑︁ 𝑖=1 h 𝑌𝑖(W = 1)− 𝑌𝑖(W = 0) i
= 1 𝑛 𝑛∑︁ 𝑗=1 ∑︁ 𝑖∈𝑁𝑢(𝑗)  𝛽𝑖,𝑗+𝛾𝑖,𝑗+𝜁𝑖,𝑗  .
Estimating these parameters presents a significant challenge due
to the substantial number of model parameters, which scales with
the number of edges in the network𝑂(|𝐸|). Therefore, we do not
estimate these parameters in practice.
We can rewrite (8) as follows:
𝑌𝑗(W) =𝛼𝑗+𝛾𝑗𝑊𝑗+
∑︁
𝑖∈𝑁𝑢(𝑗)

𝛽𝑖,𝑗𝑊𝑖+𝜁𝑖,𝑗𝑊𝑖𝑊𝑗

,
where𝛼𝑗 = ˝ 𝑖∈𝑁𝑢(𝑗)𝛼𝑖,𝑗 and𝛾𝑗 = ˝ 𝑖∈𝑁𝑢(𝑗)𝛾𝑖,𝑗 . By setting the pa-
rameter𝜁𝑖,𝑗 = 0, the model simplifies to the heterogeneous additive
network effects model, as discussed by Yu et al.[38] in their 2022
paper. This demonstrates that our model is a more general form
capable of encompassing the model proposed by Yu and colleagues
when certain conditions are applied.
To simplify the formula, we assume that 𝑧𝑖,𝑗 = 0 if(𝑖,𝑗) ∉ 𝐸.
Then the TTE𝜏 can be expressed as follows:
𝜏 = 1 𝑛 ∑︁ 𝑖≠𝑗  𝛽𝑖,𝑗+𝛾𝑖,𝑗+𝜁𝑖,𝑗  . (10)
3.2 Estimator
Consider a simple Bernoulli randomization experiment, where each
unit in the experiment is randomly assigned to either the treat-
ment group or the control group. Let 𝜋 = P(𝑊𝑖 = 1) represent
the treatment probability. We define two Horvitz-Thompson (HT)
estimators:
ˆ𝜏1(𝜋) = 1 𝑛 𝑛∑︁ 𝑖=1 𝑊𝑖𝑌𝑖 𝜋 − 1 𝑛 𝑛∑︁ 𝑖=1 (1−𝑊𝑖)𝑌𝑖 1−𝜋 , (11)
and
ˆ𝜏2(𝜋) = 1 𝑛 𝑛∑︁ 𝑖=1 𝑊𝑖𝐷𝑖 𝜋 − 1 𝑛 𝑛∑︁ 𝑖=1 (1−𝑊𝑖)𝐷𝑖 1−𝜋 . (12)
The parameter𝜋 in the estimators suggests that the properties of
the estimators are dependent on𝜋. The ˆ𝜏1(𝜋) is a commonly used
estimator in causal inference. It is widely recognized that ˆ𝜏1(𝜋)
is biased for the total treatment effect𝜏 when interference exists
[10, 13].
Finally, we define a new estimator ˆ𝜏(𝜋) as the sum of ˆ𝜏1(𝜋) and
ˆ𝜏1(𝜋). That is,
ˆ𝜏(𝜋)△= ˆ𝜏1(𝜋)+ ˆ𝜏2(𝜋). (13)
We use ˆ𝜏(𝜋) to estimate the total treatment effect𝜏. We will next
demonstrate the properties of these three estimators under various
scenarios. All the proofs can be found in the appendix.
3.3 Full population experiment
We begin by considering the simplest scenario in which the entire
population participates in the experiment. The following result is
provided:
Proposition 3.1. E
 ˆ𝜏1(𝜋)  = 1 𝑛 ˝ 𝑖≠𝑗 𝛾𝑖,𝑗+𝜁𝑖,𝑗𝜋.
The estimator’s bias is given by − 1 𝑛 ˝ 𝑖≠𝑗  𝛽𝑖,𝑗 +𝜁𝑖,𝑗(1−𝜋)  ,
which can scale with the average spillover effect across the edges
between the treated and control groups. In practice, the sign of
𝛽𝑖,𝑗 and𝜁𝑖,𝑗 may not be identical, implying that we do not even
know whether our estimate is an overestimate or an underestimate.
Thankfully, with the assistance ofˆ𝜏2(𝜋), we can unbiasedly estimate
the total treatment effect. This additional information can then be
employed to significantly simplify the estimation of causal effects.
The following result characterize the bias of ˆ𝜏2(𝜋).
Proposition 3.2. E
 ˆ𝜏2(𝜋)  = 1 𝑛 ˝ 𝑖≠𝑗 𝛽𝑖,𝑗+𝜁𝑖,𝑗𝜋.
ˆ𝜏2(𝜋) is also a biased estimator for the total treatment effect.
From Proposition 3.1 and 3.2, we can infer that
E
 ˆ𝜏(𝜋)  = 1 𝑛 ∑︁ 𝑖≠𝑗 𝛽𝑖,𝑗+𝛾𝑖,𝑗+ 2𝜋𝜁𝑖,𝑗 .
Consequently, for𝜋 = 0.5, we derive E
 ˆ𝜏(0.5)  = 1 𝑛 ˝ 𝑖≠𝑗 𝛽𝑖,𝑗+
𝛾𝑖,𝑗+𝜁𝑖,𝑗
 =𝜏. Therefore, when𝜋 = 0.5, ˆ𝜏(0.5) serves as an unbiased
estimator of the total treatment effect. We summarize the analysis
above for the estimator ˆ𝜏 in the following theorem.
Theorem 3.1. Assume (A2) and that the experiment includes all
units, the expectation of ˆ𝜏(𝜋) is
E
 ˆ𝜏(𝜋)  = 1 𝑛 ∑︁ 𝑖≠𝑗 𝛽𝑖,𝑗+𝛾𝑖,𝑗+ 2𝜋𝜁𝑖,𝑗 .
When𝜋 = 0.5, that is, when treatment and control assignments are
equally probable, ˆ𝜏(0.5) is an unbiased estimator of the total treatment
effect𝜏.
There are several important points to note in this subsection.
Firstly, our proposed estimator relies heavily on assumption (A2),
which states that𝑧𝑖,𝑗 depends solely on the treatment assignments
of unit𝑖 and unit 𝑗. This assumption is akin to the neighborhood
interference assumption. While a similar approach to the method
in [4] can be used to test assumption A2, it may not be as efficient.
Secondly, we assume that𝑧𝑖,𝑖 = 0 for all𝑖. This assumption is crucial
for the unbiased property of ˆ𝜏. If we were to allow𝑧𝑖,𝑖 ≠ 0, then it
can be shown that when𝜋 = 0.5, the bias of ˆ𝜏 is 1 𝑛 ˝ 𝑖(𝛽𝑖,𝑖+𝛾𝑖,𝑖+
𝜁𝑖,𝑖). However, even when𝑧𝑖,𝑖 ≠ 0, compared to ˆ𝜏1, our proposed
estimator ˆ𝜏 still shows an improvement in terms of bias, which
further underscores its potential usefulness in practice. We leave
the proof of this statement to the reader.
3.4 Sub-population experiment
Theorem 3.1 provides an unbiased estimator for the total treatment
effect. However, this holds only when we conduct an controlled
experiment with the entire population. In reality, many industry
experimental platforms run thousands of experiments simultane-
ously every day using a layered structure design (see [18, 33, 37] for
more details about the layer and experiment structure). Typically,
an experiment encompasses only a small fraction of users, often
less than 10% according to [18]. This leads us to a natural question:
Does the conclusion of Theorem 3.1 still holds when the experiment
includes only a subset of the population? This is a critical question,
as it directly impacts the applicability and relevance of our findings
in real-world settings.

Unbiased Estimation for Total Treatment Effect Under Interference Using Aggregated Dyadic Data KDD’24, August 25–29, 2024, Barcelona, Spain
Let’s suppose we randomly select a proportion 𝑝(0 < 𝑝≤ 1)
of the population to participate in the experiment. For each user
𝑖, we use𝑉𝑖 ∈{ 0, 1} to denote whether user 𝑖 is included in the
experiment or not. Users who are included in the experiment are
then assigned to either the treatment or control group through a
Bernoulli randomization process. Let’s denote𝜋 = P(𝑊𝑖 = 1|𝑉𝑖 = 1)
as the probability of users in the experiment receiving the treat-
ment. To simplify the problem, we’ll assume that users who are
not included in the experiment receive the control group strategy,
i.e., P(𝑊𝑖 = 0|𝑉𝑖 = 0) = 1. Under these assumptions, the two HT
estimators become functions of𝑝 and𝜋:
ˆ𝜏1(𝑝,𝜋) = 1 𝑛 𝑛∑︁ 𝑖=1 𝑉𝑖𝑊𝑖𝑌𝑖 𝑝𝜋 − 1 𝑛 𝑛∑︁ 𝑖=1 𝑉𝑖(1−𝑊𝑖)𝑌𝑖 𝑝(1−𝜋) , (14)
and
ˆ𝜏2(𝑝,𝜋) = 1 𝑛 𝑛∑︁ 𝑖=1 𝑉𝑖𝑊𝑖𝐷𝑖 𝑝𝜋 − 1 𝑛 𝑛∑︁ 𝑖=1 𝑉𝑖(1−𝑊𝑖)𝐷𝑖 𝑝(1−𝜋) . (15)
This setup allows us to explore how the proportion of the popula-
tion included in the experiment and the probability of receiving
treatment affect the bias of our estimators. The bias property of
these two estimators are presented below.
Proposition 3.3. E
 ˆ𝜏1(𝑝,𝜋)  = 1 𝑛 ˝ 𝑖≠𝑗 𝛾𝑗,𝑖+𝑝𝜋𝜁𝑗,𝑖 .
Proposition 3.4. E
 ˆ𝜏2(𝑝,𝜋)  = 1 𝑛 ˝ 𝑖≠𝑗 𝛽𝑖,𝑗+𝑝𝜋𝜁𝑖,𝑗 .
Note that ˆ𝜏(𝑝,𝜋) = ˆ𝜏1(𝑝,𝜋)+ ˆ𝜏2(𝑝,𝜋), We have the following
theorem about ˆ𝜏(𝑝,𝜋).
Theorem 3.2. Assume (A2). The expectation of ˆ𝜏(𝑝,𝜋) is
E
 ˆ𝜏(𝑝,𝜋)  = 1 𝑛 ∑︁ 𝑖≠𝑗 𝛽𝑖,𝑗+𝛾𝑖,𝑗+ 2𝑝𝜋𝜁𝑖,𝑗 . (16)
and the bias is
E
 ˆ𝜏(𝑝,𝜋)− 𝜏  =− 1− 2𝑝𝜋 𝑛 ∑︁ 𝑖≠𝑗 𝜁𝑖,𝑗. (17)
Theorem 3.1 can be seen as a special case of Theorem 3.2. Specif-
ically, when𝑝 = 1, meaning the entire population is included in
the experiment, Theorem 3.2 simplifies to Theorem 3.1. However,
in general, we have ˝ 𝑖≠𝑗𝜁𝑖,𝑗 ≠ 0. This implies that the estima-
tor ˆ𝜏(𝑝,𝜋) in a sub-population experiment (where 𝑝 < 1) is bi-
ased for the total treatment effect. Furthermore, there are𝑂(|𝐸|)
terms in the summands of ˝ 𝑖≠𝑗𝜁𝑖,𝑗 , which suggests that the bias is
𝑂
|𝐸|
𝑛

. When comparing the biases of the two estimators ˆ𝜏(𝑝,𝜋)
and ˆ𝜏1(𝑝,𝜋), we find that the difference in their expected biases is
given by:
E
 ˆ𝜏1(𝑝,𝜋)− 𝜏  − E  ˆ𝜏(𝑝,𝜋)− 𝜏  = 1 𝑛 ∑︁ 𝑖≠𝑗 (𝛽𝑖,𝑗+𝑝𝜋𝜁𝑖,𝑗).
This result implies that the absolute bias of ˆ𝜏(𝑝,𝜋) is smaller than
the absolute bias of ˆ𝜏1(𝑝,𝜋). In other words, the estimator ˆ𝜏(𝑝,𝜋)
is more accurate in estimating the total treatment effect when only
a subset of the population is included in the experiment.
3.5 Sub-population two-stage experiment
For the remainder of this paper, we will focus on the scenario
where the experiment does not include all users in the population.
Under a simple Bernoulli randomization experiment without full
population coverage, the estimator ˆ𝜏(𝑝,𝜋) is biased for the total
treatment effect. This naturally leads us to question whether it is
possible to find an estimator with a smaller bias. In this subsection,
we provide some positive results by considering a special design
that is similar to two-stage randomized experiments and the cluster
network experiment randomization process [17]. This design aims
to reduce bias and improve the accuracy of our estimates, thereby
providing a more reliable understanding of the treatment effect.
Given a network graph 𝐺, let’s assume we can partition the
graph into disjoint clusters using common clustering algorithm
like Louvain community detection [7]. Our two-stage experiment
scheme consists of two steps:
(1) First, we randomly select𝑝 percent of the clusters to form
the sub-population in the experiment.
(2) Second, we randomly assign the units in the sub-population
to either the treatment group with probability𝜋, or the con-
trol group with probability 1−𝜋.
A visualization of this two-stage experiment process is provided
in Figure 2. Similar to the setting in subsection 3.4, for each user
𝑖, we use𝑉𝑖∈{ 0, 1} to indicate whether they are included in the
experiment, with P(𝑉𝑖 = 1) = 𝑝. Users who are not included in
the experiment are assigned the control strategy. To distinguish
this scenario from the one discussed in subsection 3.4, we denote
the two HT estimators in (14) and (15) as ˆ𝜏1𝑐(𝑝,𝜋) and ˆ𝜏2𝑐(𝑝,𝜋),
respectively. The HT estimator of the total treatment effect is then
given by ˆ𝜏𝑐(𝑝,𝜋) = ˆ𝜏1𝑐(𝑝,𝜋)+ ˆ𝜏2𝑐(𝑝,𝜋). Finally, let ¯𝜎 denote the
proportion of each user’s friends within the same cluster relative
to their total number of friends, i.e.,
¯𝜎 = 1 𝑛 ∑︁ 𝑖 |{𝑗 : 𝑗 and𝑖 are in the same cluster}| 𝑑𝑖
We have the following results.
Proposition 3.5. E
 ˆ𝜏1𝑐(𝑝,𝜋)  = 1 𝑛 ˝ 𝑖≠𝑗  𝛾𝑖,𝑗+ ¯𝜎𝜋+(1−¯𝜎)𝑝𝜋𝜁𝑖,𝑗  .
Proposition 3.6. E
 ˆ𝜏2𝑐(𝑝,𝜋)  = 1 𝑛 ˝ 𝑖≠𝑗  𝛽𝑖,𝑗+ ¯𝜎𝜋+(1−¯𝜎)𝑝𝜋𝜁𝑖,𝑗  .
Theorem 3.3. Assume (A2). Under a two-stage experiment scheme,
the expectation of ˆ𝜏𝑐(𝑝,𝜋) is
E
 ˆ𝜏𝑐(𝑝,𝜋)  = 1 𝑛 ∑︁ 𝑖≠𝑗  𝛽𝑖,𝑗+𝛾𝑖,𝑗+ 2𝜋 ¯𝜎+( 1− ¯𝜎)𝑝𝜁𝑖,𝑗  . (18)
The bias is
E
 ˆ𝜏2 𝑐(𝑝,𝜋)− 𝜏  =−(1− 2𝑝𝜋)( 1− ¯𝜎) 𝑛 ∑︁ 𝑖≠𝑗 𝜁𝑖,𝑗. (19)
From equations (17) and (19), we can observe that the absolute
bias of the estimatorˆ𝜏𝑐(𝑝,𝜋) in the two-stage experiment is reduced
by ¯𝜎(1−2𝑝𝜋) 𝑛 ˝ 𝑖≠𝑗𝜁𝑖,𝑗 compared to the absolute bias of the estimator
ˆ𝜏(𝑝,𝜋) in the simple randomized experiment. This indicates that the
two-stage experiment can further reduce the bias of the estimator
without sacrificing any statistical power. This is a significant finding,
as it suggests that a two-stage experimental design can provide

KDD’24, August 25–29, 2024, Barcelona, Spain Lu Deng, Yilin Li, Jingjing Zhang, Yong Wang, and Chuan Chen
clusters
Experiment 1
Experiment 2
Treatment
Control
Treatment
Control
Experiment 1
Experiment 2
Figure 2: Visualization of the two-stage experiment process.
more accurate estimates of the treatment effect, thereby improving
the reliability of our results. In practical applications, the value of ¯𝜎
typically falls between 30% to 40% [17], meaning that the bias can
be reduced by a minimum of 30%.
4 NUMERICAL EXPERIMENTS
4.1 Simulated data
To compare the performance of the estimators mentioned earlier
under various conditions, we conducted several simulation studies.
These studies were based on two real-world social networks: FB-
Standard3 and FB-Cornell5 1. The FB-Standard3 network comprises
11,586 nodes and 568,309 edges, yielding an average degree of 98.1.
On the other hand, the FB-Cornell5 network consists of 18,660
nodes and 790,777 edges, resulting in an average degree of 84.7. To
initiate our simulations, we first generated the paired outcomes
based on the model defined in equation (7):
𝑧𝑖,𝑗(𝑊𝑖,𝑊𝑗) =𝛼𝑖,𝑗+𝛽𝑖,𝑗𝑊𝑖+𝛾𝑖,𝑗𝑊𝑗+𝜁𝑖,𝑗𝑊𝑖𝑊𝑗.
Next, we aggregated the paired outcomes to obtain𝑌𝑖 and𝐷𝑖. The
parameters𝛼𝑖,𝑗,𝛽𝑖,𝑗,𝛾𝑖,𝑗,𝜁𝑖,𝑗 were generated from either a uniform
or a Bernoulli distribution. Specifically, we considered the following
two cases:
• For uniform distributed coefficients,𝛼𝑖,𝑗 = 1,𝛽𝑖,𝑗 ∼ Uniform
(0, 0.5),𝛾𝑖,𝑗 ∼ Uniform(0, 1),𝜁𝑖,𝑗 ∼ Uniform(0, 0.5) for all
pair(𝑖,𝑗)∈ 𝐸 independently.
• For Bernoulli distributed coefficients,𝛼𝑖,𝑗 = 0,𝛽𝑖,𝑗 ∼ Bernoulli
(0.25),𝛾𝑖,𝑗 ∼ Bernoulli(0.5),𝜁𝑖,𝑗 ∼ Bernoulli(0.25) for all
pair(𝑖,𝑗)∈ 𝐸 independently.
Once the parameters were generated, they remained fixed through-
out the simulation. We considered a total of four different simula-
tion settings. For each setting, we performed 10,000 repetitions to
calculate the bias of the estimators and assess their performance.
1Network topology data can be found in https://networkrepository.com/socfb-
Stanford3.php and https://networkrepository.com/socfb-Cornell5.php
Firstly, we simulated a scenario where the entire population is
included in the experiment. We varied the treatment probability𝜋
across the set{0.1, 0.3, 0.5, 0.7, 0.9}. The results of these simulations
are presented in Figure 3. From the figure, it is evident that both
ˆ𝜏1(𝜋) and ˆ𝜏2(𝜋) exhibit bias under any given treatment probability.
However, ˆ𝜏(𝜋) remains unbiased when𝜋 = 0.5. This observation
aligns perfectly with the conclusion drawn in Theorem 3.1.
Secondly, we simulated a scenario where only a subset of the
population is included in the experiment. In this case, we fixed the
treatment probability at 𝜋 = 0.5, varied the in-experiment prob-
ability𝑝 across the set{0.05, 0.1, 0.25, 0.5, 1}. The results of these
simulations are presented in Figure 4. From the figure, it is evident
that when𝑝 < 1 , all three estimators ˆ𝜏1(𝑝,𝜋), ˆ𝜏2(𝑝,𝜋) and ˆ𝜏(𝑝,𝜋)
exhibit bias. Not surprisingly, the bias of ˆ𝜏(𝑝,𝜋) decreases as 𝑝
approaches 1. This suggests that increasing the traffic ratio of the
experiment can help reduce the bias introduced by interference.
Furthermore, we observe that the absolute bias of ˆ𝜏(𝑝,𝜋) is consis-
tently smaller than the absolute bias of ˆ𝜏1(𝑝,𝜋) under any given
in-experiment probability. This indicates the superiority of ˆ𝜏(𝑝,𝜋)
over ˆ𝜏1(𝑝,𝜋).
Lastly, we simulated a two-stage experiment scenario. We first
applied the Louvain algorithm [7] with a fixed random seed and a
resolution parameter set to 10 to group the units into clusters. This
resulted in 240 clusters for the FB-Cornell5 graph and 192 clusters
for the FB-Stanford3 graph. As in the previous scenario, we fixed
the treatment probability at𝜋 = 0.5, and varied the in-experiment
probability𝑝 across the set{0.05, 0.1, 0.25, 0.5, 1}. The results of
these simulations are presented in Figure 5. From the figure, it is
evident that the two-stage experiment scheme can further reduce
the bias of ˆ𝜏(𝑝,𝜋) compared to the simple Bernoulli randomized
experiment. This suggests that a two-stage experimental design,
where units are first grouped into clusters, can be a more effective
strategy for reducing bias in the presence of interference.

Unbiased Estimation for Total Treatment Effect Under Interference Using Aggregated Dyadic Data KDD’24, August 25–29, 2024, Barcelona, Spain
   
WUHDWPHQWSUREDELOLW\









ELDV
XQLIRUPFRUQHOO
(1)
 (2)
   
WUHDWPHQWSUREDELOLW\









ELDV
ELQRPLDOFRUQHOO
(1)
 (2)
   
WUHDWPHQWSUREDELOLW\





ELDV
XQLIRUPVWDQIRUG
(1)
 (2)
   
WUHDWPHQWSUREDELOLW\





ELDV
ELQRPLDOVWDQIRUG
(1)
 (2)
Figure 3: Visualizations of the performance of three TTE estimators under full population Bernoulli design on FB-Standard3
and FB-Cornell5 networks for both Uniform and Bernoulli potential outcomes models. Each line’s height represents the relative
bias of the estimator.
    
H[SHULPHQWUDWLR







ELDV
XQLIRUPFRUQHOO
(1)
 (2)
    
H[SHULPHQWUDWLR







ELDV
ELQRPLDOFRUQHOO
(1)
 (2)
    
H[SHULPHQWUDWLR








ELDV
XQLIRUPVWDQIRUG
(1)
 (2)
    
H[SHULPHQWUDWLR








ELDV
ELQRPLDOVWDQIRUG
(1)
 (2)
Figure 4: Visualizations of the performance of three TTE estimators under sub-population Bernoulli design on FB-Standard3
and FB-Cornell5 networks for both Uniform and Bernoulli potential outcomes models. Each line’s height represents the relative
bias of the estimator.
    
H[SHULPHQWUDWLR






ELDV
XQLIRUPFRUQHOO
 LQ WZRVWDJH H[SW
  LQ VLPSOH H[SW
    
H[SHULPHQWUDWLR







ELDV
XQLIRUPVWDQIRUG
 LQ WZRVWDJH H[SW
  LQ VLPSOH H[SW
    
H[SHULPHQWUDWLR






ELDV
ELQRPLDOFRUQHOO
 LQ WZRVWDJH H[SW
  LQ VLPSOH H[SW
    
H[SHULPHQWUDWLR







ELDV
ELQRPLDOVWDQIRUG
 LQ WZRVWDJH H[SW
  LQ VLPSOH H[SW
Figure 5: Visualizations of the performance of three TTE estimators under sub-population two-stage experiment design
on FB-Standard3 and FB-Cornell5 networks for both Uniform and Bernoulli potential outcomes models. Each line’s height
represents the relative bias of the estimator.

KDD’24, August 25–29, 2024, Barcelona, Spain Lu Deng, Yilin Li, Jingjing Zhang, Yong Wang, and Chuan Chen
Table 1: Estimates with a re-scaled confidence interval of the metrics in the two-stage experiment.
ˆ𝜏1 ˆ𝜏2 ˆ𝜏
Metric 1 -0.605%± 0.255% 3.498%± 1.198% 0.621%± 0.5%
Metric 2 -0.712%± 0.349% 3.381%± 1.171% 0.678%± 0.5%
4.2 Real Data
We present an empirical experiment conducted on Weixin’s ex-
periment platform, utilizing aggregated dyadic data to estimate
the total treatment effect. Weixin, a popular messaging and calling
application, allows users to interact with their contacts. A built-in
feature of Weixin, known as "Channels", is akin to TikTok, enabling
users to view and discover a plethora of personalized short videos.
Similar to Example 2.1, users typically share intriguing videos with
their friends, who can then access the "Channels" page by clicking
on the shared video, watching it, and exploring other videos.
A two-stage experiment spanning two weeks was executed to
evaluate a novel algorithm. The experiment contains about 4% of
the users. In the treatment group, the algorithm increased the like-
lihood of users sharing videos. The underlying hypothesis was that
promoting video sharing would lead to users exiting the "Channels"
page to engage in conversations with friends, thereby reducing
their consumption but increasing that of their friends. The pri-
mary objective was to ascertain whether this new algorithm could
enhance user activity and consumption when deployed to all users.
The outcomes for two crucial metrics are detailed in Table 1.
All data and attributes are collected after user approvals and data
masking to protect user privacy. Each metric was re-scaled such
that the estimator ˆ𝜏 has a confidence interval (CI) width of one.
The results align with our initial expectations. The ˆ𝜏1 indicates
a significant decrease, while the ˆ𝜏 exhibits a substantial increase,
implying that the total treatment effect of the new algorithm is
positive. Upon deploying the new algorithm to all users, an upward
trend in the consumption of the entire user base was observed,
corroborating the results of ˆ𝜏.
5 DISCUSSION
The estimator ˆ𝜏, as developed in our study, has the potential to
estimate the total treatment effect within a dyadic data structure.
This estimator exhibits no bias when the experiment encompasses
the entire population and the probability of treatment is set at 0.5.
Compared to the conventional estimator ˆ𝜏1, our proposed estimator
ˆ𝜏 demonstrates reduced bias when the experiment includes only
a small subset of the population. Furthermore, we suggest the ap-
plication of ˆ𝜏 within a two-stage experimental scheme, a strategy
that can further mitigate the estimator’s bias.
Several potential avenues exist for extending our current work.
Firstly, we have not yet presented the variance properties of these
estimators. In practical applications, we utilize the sample vari-
ance of𝑌𝑖 and𝐷𝑖 to facilitate statistical inference. Our simulation
findings suggest that the sample variance provides a reasonably
accurate estimate of the true variance. Future work could involve
deriving the expression for the variance of these estimators, demon-
strating the convergence rate, and proposing alternative estimators
for variance within a dyadic data structure.
Secondly, our work relies on an important assumption (A2),
which posits that the potential pair outcomes𝑧𝑖,𝑗(W) depend solely
on the treatment assignments of units 𝑖 and 𝑗. This assumption
could be extended to a more general case, for instance, by assuming
that the potential pair outcomes𝑧𝑖,𝑗(W) depend on the treatment
assignments of units 𝑖,𝑗 , and all their respective neighbors. Al-
though an assumption of this nature significantly increases the
complexity of inferring the total treatment effect, researchers may
be able to leverage dyadic data to construct estimators that exhibit
superior properties compared to commonly used estimators, such
as the difference-in-means estimator and the Horvitz-Thompson
estimator.
Thirdly, this paper considers simple Bernoulli randomization ex-
perimentation. There are other experimental randomization schemes,
such as cluster randomization or ego cluster randomization, which
are useful for dealing with interference. Future research could ex-
plore the integration of our estimators with these alternative ran-
domization schemes, potentially leading to insightful findings for
estimating the total treatment effect.
Fourthly, dyadic data represents a unique type of data structure.
However, in some scenarios, we may not have access to dyadic data,
meaning that the outcome𝑌𝑖 cannot be decomposed into the sum
of edge-level outcomes. Consider, for instance, a user activity level
metric, which is binary, represented by 1 (active) or 0 (inactive). It is
not feasible to express the user activity level metric in a summation
form. For such metrics, researchers could consider integrating our
method with the approaches proposed in [15, 21] to estimate the
total treatment effect.
Exploring these potential extensions could significantly broaden
the applicability of our estimators to more general models, while
also providing the necessary theoretical justifications. These promis-
ing research directions present exciting opportunities for future
work, and we look forward to seeing how they will further advance
our understanding in this field.
Code Availability Statement:https://github.com/adamdenglu/diffusion-
metric-with-aggregated-dyadic-data
REFERENCES
[1] Coren L Apicella, Frank W Marlowe, James H Fowler, and Nicholas A Christakis.
2012. Social networks and cooperation in hunter-gatherers. Nature 481, 7382
(2012), 497–501.
[2] Peter M Aronow and Cyrus Samii. 2012. Estimating average causal effects under
general interference. In Summer Meeting of the Society for Political Methodology,
University of North Carolina, Chapel Hill, July . 19–21.
[3] Peter M Aronow and Cyrus Samii. 2017. Estimating average causal effects under
general interference, with application to a social network experiment. (2017).
[4] Susan Athey, Dean Eckles, and Guido W Imbens. 2018. Exact p-values for network
interference. J. Amer. Statist. Assoc. 113, 521 (2018), 230–240.
[5] Guillaume W Basse and Edoardo M Airoldi. 2015. Optimal model-assisted design
of experiments for network correlated outcomes suggests new notions of network
balance. arXiv preprint arXiv:1507.00803 (2015).

Unbiased Estimation for Total Treatment Effect Under Interference Using Aggregated Dyadic Data KDD’24, August 25–29, 2024, Barcelona, Spain
[6] Guillaume W Basse and Edoardo M Airoldi. 2018. Model-assisted design of
experiments in the presence of network-correlated outcomes. Biometrika 105, 4
(2018), 849–858.
[7] Vincent D Blondel, Jean-Loup Guillaume, Renaud Lambiotte, and Etienne Lefeb-
vre. 2008. Fast unfolding of communities in large networks. Journal of statistical
mechanics: theory and experiment 2008, 10 (2008), P10008.
[8] Alex Chin. 2018. Central limit theorems via Stein’s method for randomized
experiments under interference. arXiv preprint arXiv:1804.03105 (2018).
[9] Mayleen Cortez, Matthew Eichhorn, and Christina Yu. 2022. Staggered rollout
designs enable causal inference under interference without network knowledge.
Advances in Neural Information Processing Systems 35 (2022), 7437–7449.
[10] Dean Eckles, Brian Karrer, and Johan Ugander. 2016. Design and analysis of
experiments in networks: Reducing bias from interference. Journal of Causal
Inference 5, 1 (2016), 20150021.
[11] Laura Forastiere, Edoardo M Airoldi, and Fabrizia Mealli. 2021. Identification
and estimation of treatment and interference effects in observational studies on
networks. J. Amer. Statist. Assoc. 116, 534 (2021), 901–918.
[12] Laura Forastiere, Fabrizia Mealli, Albert Wu, and Edoardo M Airoldi. 2022. Es-
timating causal effects under network interference with Bayesian generalized
propensity scores. The Journal of Machine Learning Research 23, 1 (2022), 13101–
13161.
[13] Huan Gui, Ya Xu, Anmol Bhasin, and Jiawei Han. 2015. Network a/b testing:
From sampling to estimation. In Proceedings of the 24th International Conference
on World Wide Web. 399–409.
[14] Richard J Hayes and Lawrence H Moulton. 2017. Cluster randomised trials. CRC
press.
[15] Yuchen Hu, Shuangning Li, and Stefan Wager. 2022. Average direct and indirect
causal effects under interference. Biometrika 109, 4 (2022), 1165–1172.
[16] Guido W Imbens and Donald B Rubin. 2015. Causal inference in statistics, social,
and biomedical sciences. Cambridge University Press.
[17] Brian Karrer, Liang Shi, Monica Bhole, Matt Goldman, Tyrone Palmer, Charlie
Gelman, Mikael Konutgan, and Feng Sun. 2021. Network experimentation at
scale. In Proceedings of the 27th acm sigkdd conference on knowledge discovery &
data mining. 3106–3116.
[18] Ron Kohavi, Alex Deng, Brian Frasca, Toby Walker, Ya Xu, and Nils Pohlmann.
2013. Online controlled experiments at large scale. In Proceedings of the 19th
ACM SIGKDD international conference on Knowledge discovery and data mining .
1168–1176.
[19] Ron Kohavi, Alex Deng, Roger Longbotham, and Ya Xu. 2014. Seven rules
of thumb for web site experimenters. In Proceedings of the 20th ACM SIGKDD
international conference on Knowledge discovery and data mining . 1857–1866.
[20] Michael P Leung. 2022. Causal inference under approximate neighborhood
interference. Econometrica 90, 1 (2022), 267–293.
[21] Shuangning Li and Stefan Wager. 2022. Random graph asymptotics for treatment
effect estimation under network interference. The Annals of Statistics 50, 4 (2022),
2334–2358.
[22] Yang Liu, Yifan Zhou, Ping Li, and Feifang Hu. 2022. Adaptive A/B Test on Net-
works with Cluster Structures. InInternational Conference on Artificial Intelligence
and Statistics. PMLR, 10836–10851.
[23] Douglas A Luke and Jenine K Harris. 2007. Network analysis in public health:
history, methods, and applications. Annu. Rev. Public Health 28 (2007), 69–93.
[24] Charles F Manski. 2013. Identification of treatment response with social interac-
tions. The Econometrics Journal 16, 1 (2013), S1–S23.
[25] Richard Portes and Helene Rey. 2005. The determinants of cross-border equity
flows. Journal of international Economics 65, 2 (2005), 269–296.
[26] Jean Pouget-Abadie, Guillaume Saint-Jacques, Martin Saveski, Weitao Duan, Sou-
vik Ghosh, Ya Xu, and Edoardo M Airoldi. 2019. Testing for arbitrary interference
on experimentation platforms. Biometrika 106, 4 (2019), 929–940.
[27] Guillaume Saint-Jacques, James Eric Sorenson, Nanyu Chen, and Ya Xu. 2019. A
method for measuring network effects of one-to-one communication features in
online a/b tests. arXiv preprint arXiv:1903.08766 (2019).
[28] Guillaume Saint-Jacques, Maneesh Varshney, Jeremy Simpson, and Ya Xu. 2019.
Using ego-clusters to measure network effects at LinkedIn. arXiv preprint
arXiv:1903.08755 (2019).
[29] Carl-Erik Särndal, Bengt Swensson, and Jan Wretman. 2003.Model assisted survey
sampling. Springer Science & Business Media.
[30] Fredrik Sävje. 2023. Causal inference with misspecified exposure mappings:
separating definitions and assumptions. Biometrika (2023), asad019.
[31] Fredrik Sävje, Peter Aronow, and Michael Hudgens. 2021. Average treatment
effects in the presence of unknown interference. Annals of statistics 49, 2 (2021),
673.
[32] Daniel L Sussman and Edoardo M Airoldi. 2017. Elements of estimation the-
ory for causal effects in the presence of network interference. arXiv preprint
arXiv:1702.03578 (2017).
[33] Diane Tang, Ashish Agarwal, Deirdre O’Brien, and Mike Meyer. 2010. Overlap-
ping experiment infrastructure: More, better, faster experimentation. In Proceed-
ings of the 16th ACM SIGKDD international conference on Knowledge discovery
and data mining. 17–26.
[34] Panos Toulis and Edward Kao. 2013. Estimation of causal peer influence effects.
In International conference on machine learning . PMLR, 1489–1497.
[35] Johan Ugander, Brian Karrer, Lars Backstrom, and Jon Kleinberg. 2013. Graph
cluster randomization: Network exposure to multiple universes. In Proceedings of
the 19th ACM SIGKDD international conference on Knowledge discovery and data
mining. 329–337.
[36] Johan Ugander and Hao Yin. 2023. Randomized graph cluster randomization.
Journal of Causal Inference 11, 1 (2023), 20220014.
[37] Tao Xiong, Yong Wang, and Senlie Zheng. 2020. Orthogonal Traffic Assignment
in Online Overlapping A/B Tests . Technical Report. EasyChair.
[38] Christina Lee Yu, Edoardo M Airoldi, Christian Borgs, and Jennifer T Chayes.
2022. Estimating the total treatment effect in randomized experiments with
unknown network structure. Proceedings of the National Academy of Sciences
119, 44 (2022), e2208975119.
[39] Yuan Yuan and Kristen M Altenburger. 2022. A Two-Part Machine Learning
Approach to Characterizing Network Interference in A/B Testing.
A PROOFS
A.1 Proof of Proposition 3.1
Proof. Let’s rewrite the estimator b𝜏1 as
b𝜏1 = 1 𝑛 𝑛∑︁ 𝑖=1 𝑊𝑖𝑌𝑖 𝜋 − 1 𝑛 𝑛∑︁ 𝑖=1 (1−𝑊𝑖)𝑌𝑖 1−𝜋
= 1 𝑛𝜋 𝑛∑︁ 𝑖=1 𝑊𝑖  𝑛∑︁ 𝑗=1  𝛼𝑗,𝑖+𝛽𝑗,𝑖𝑊𝑗+𝛾𝑗,𝑖𝑊𝑖+𝜁𝑗,𝑖𝑊𝑖𝑊𝑗  −
1
𝑛(1−𝜋)
𝑛∑︁
𝑖=1
(1−𝑊𝑖)
 𝑛∑︁ 𝑗=1  𝛼𝑗,𝑖+𝛽𝑗,𝑖𝑊𝑗+𝛾𝑗,𝑖𝑊𝑖+𝜁𝑗,𝑖𝑊𝑖𝑊𝑗 
= 1 𝑛𝜋 ∑︁ 𝑖≠𝑗 𝑊𝑖  𝛼𝑗,𝑖+𝛽𝑗,𝑖𝑊𝑗+𝛾𝑗,𝑖+𝜁𝑗,𝑖𝑊𝑗  −
1
𝑛(1−𝜋)
∑︁
𝑖≠𝑗
(1−𝑊𝑖)

𝛼𝑗,𝑖+𝛽𝑗,𝑖𝑊𝑗

Note that
(1) E(𝑊𝑖) =𝜋.
(2){𝑊𝑖}𝑛 𝑖=1 are independent, E(𝑊𝑖𝑊𝑗) =𝜋2 for𝑖 ≠ 𝑗.
So we have
E(b𝜏1) = 1 𝑛 ∑︁ 𝑖≠𝑗  𝛼𝑗,𝑖+𝛽𝑗,𝑖𝜋+𝛾𝑗,𝑖+𝜁𝑗,𝑖𝜋  − 1 𝑛 ∑︁ 𝑖≠𝑗  𝛼𝑗,𝑖+𝛽𝑗,𝑖𝜋 
= 1 𝑛 ∑︁ 𝑖≠𝑗  𝛾𝑖,𝑗+𝜁𝑖,𝑗𝜋  .
□

KDD’24, August 25–29, 2024, Barcelona, Spain Lu Deng, Yilin Li, Jingjing Zhang, Yong Wang, and Chuan Chen
A.2 Proof of Proposition 3.2
Proof. Follow the same steps,
b𝜏2 = 1 𝑛 𝑛∑︁ 𝑖=1 𝑊𝑖𝐷𝑖 𝜋 − 1 𝑛 𝑛∑︁ 𝑖=1 (1−𝑊𝑖)𝐷𝑖 1−𝜋
= 1 𝑛𝜋 𝑛∑︁ 𝑖=1 𝑊𝑖  𝑛∑︁ 𝑗=1  𝛼𝑖,𝑗+𝛽𝑖,𝑗𝑊𝑖+𝛾𝑖,𝑗𝑊𝑗+𝜁𝑖,𝑗𝑊𝑖𝑊𝑗  −
1
𝑛(1−𝜋)
𝑛∑︁
𝑖=1
(1−𝑊𝑖)
 𝑛∑︁ 𝑗=1  𝛼𝑖,𝑗+𝛽𝑖,𝑗𝑊𝑖+𝛾𝑖,𝑗𝑊𝑗+𝜁𝑖,𝑗𝑊𝑖𝑊𝑗 
= 1 𝑛𝜋 𝑛∑︁ 𝑖≠𝑗 𝑊𝑖  𝛼𝑖,𝑗+𝛽𝑖,𝑗+𝛾𝑖,𝑗𝑊𝑗+𝜁𝑖,𝑗𝑊𝑗  −
1
𝑛(1−𝜋)
∑︁
𝑖≠𝑗
(1−𝑊𝑖)

𝛼𝑖,𝑗+𝛾𝑖,𝑗𝑊𝑗

.
Again,{𝑊𝑖}𝑛 𝑖=1 are independent. Hence
E(b𝜏2) = 1 𝑛 ∑︁ 𝑖≠𝑗  𝛼𝑖,𝑗+𝛽𝑖,𝑗+𝛾𝑖,𝑗𝜋+𝜁𝑖,𝑗𝜋  − 1 𝑛 ∑︁ 𝑖≠𝑗  𝛼𝑖,𝑗+𝛾𝑖,𝑗𝜋 
= 1 𝑛 ∑︁ 𝑖≠𝑗  𝛽𝑖,𝑗+𝜁𝑖,𝑗𝜋  .
□
A.3 Proof of Proposition 3.3
Proof. Follow the same steps,
b𝜏1 = 1 𝑛 𝑛∑︁ 𝑖=1 𝑉𝑖𝑊𝑖𝑌𝑖 𝑝𝜋 − 1 𝑛 𝑛∑︁ 𝑖=1 𝑉𝑖(1−𝑊𝑖)𝑌𝑖 𝑝(1−𝜋)
= 1 𝑛𝑝𝜋 𝑛∑︁ 𝑖=1 𝑉𝑖𝑊𝑖  𝑛∑︁ 𝑗=1  𝛼𝑗,𝑖+𝛽𝑗,𝑖𝑊𝑗+𝛾𝑗,𝑖𝑊𝑖+𝜁𝑗,𝑖𝑊𝑖𝑊𝑗  −
1
𝑛𝑝(1−𝜋)
𝑛∑︁
𝑖=1
𝑉𝑖(1−𝑊𝑖)
 𝑛∑︁ 𝑗=1  𝛼𝑗,𝑖+𝛽𝑗,𝑖𝑊𝑗+𝛾𝑗,𝑖𝑊𝑖+𝜁𝑗,𝑖𝑊𝑖𝑊𝑗 
= 1 𝑛𝑝𝜋 𝑛∑︁ 𝑖≠𝑗 𝑉𝑖𝑊𝑖  𝛼𝑗,𝑖+𝛽𝑗,𝑖𝑊𝑗+𝛾𝑗,𝑖+𝜁𝑗,𝑖𝑊𝑗  −
1
𝑛𝑝(1−𝜋)
∑︁
𝑖≠𝑗
𝑉𝑖(1−𝑊𝑖)

𝛼𝑗,𝑖+𝛽𝑗,𝑖𝑊𝑗

Note that
(1) E(𝑉𝑖𝑊𝑖) =𝑝𝜋 .
(2) E(𝑉𝑖𝑊𝑖𝑊𝑗) =𝑝2𝜋.
(3) E𝑉𝑖(1−𝑊𝑖) =𝑝(1−𝜋).
(4) E𝑉𝑖(1−𝑊𝑖)𝑊𝑗  =𝑝2𝜋(1−𝜋).
Hence
E(b𝜏1) = 1 𝑛 ∑︁ 𝑖≠𝑗  𝛼𝑗,𝑖+𝛽𝑗,𝑖𝑝𝜋+𝛾𝑗,𝑖+𝜁𝑗,𝑖𝑝𝜋  − 1 𝑛 ∑︁ 𝑖≠𝑗  𝛼𝑗,𝑖+𝛽𝑗,𝑖𝑝𝜋 
= 1 𝑛 ∑︁ 𝑖≠𝑗  𝛾𝑗,𝑖+𝑝𝜋𝜁𝑗,𝑖  .
□
A.4 Proof of Proposition 3.4
Proof. Follow the same steps,
b𝜏2 = 1 𝑛 𝑛∑︁ 𝑖=1 𝑉𝑖𝑊𝑖𝐷𝑖 𝑝𝜋 − 1 𝑛 𝑛∑︁ 𝑖=1 𝑉𝑖(1−𝑊𝑖)𝐷𝑖 𝑝(1−𝜋)
= 1 𝑛𝑝𝜋 𝑛∑︁ 𝑖=1 𝑉𝑖𝑊𝑖  𝑛∑︁ 𝑗=1  𝛼𝑖,𝑗+𝛽𝑖,𝑗𝑊𝑖+𝛾𝑖,𝑗𝑊𝑗+𝜁𝑖,𝑗𝑊𝑖𝑊𝑗  −
1
𝑛𝑝(1−𝜋)
𝑛∑︁
𝑖=1
𝑉𝑖(1−𝑊𝑖)
 𝑛∑︁ 𝑗=1  𝛼𝑖,𝑗+𝛽𝑖,𝑗𝑊𝑖+𝛾𝑖,𝑗𝑊𝑗+𝜁𝑖,𝑗𝑊𝑖𝑊𝑗 
= 1 𝑛𝑝𝜋 ∑︁ 𝑖≠𝑗 𝑉𝑖𝑊𝑖  𝛼𝑖,𝑗+𝛽𝑖,𝑗+𝛾𝑖,𝑗𝑊𝑗+𝜁𝑖,𝑗𝑊𝑗  −
1
𝑛𝑝(1−𝜋)
∑︁
𝑖≠𝑗
𝑉𝑖(1−𝑊𝑗)

𝛼𝑖,𝑗+𝛾𝑖,𝑗𝑊𝑗

Hence
E(b𝜏2) = 1 𝑛 ∑︁ 𝑖≠𝑗  𝛼𝑖,𝑗+𝛽𝑖,𝑗+𝛾𝑖,𝑗𝑝𝜋+𝜁𝑖,𝑗𝑝𝜋  − 1 𝑛 ∑︁ 𝑖≠𝑗  𝛼𝑖,𝑗+𝛾𝑖,𝑗𝑝𝜋 
= 1 𝑛 ∑︁ 𝑖≠𝑗  𝛽𝑖,𝑗+𝑝𝜋𝜁𝑖,𝑗 
□
A.5 Proof of Proposition 3.5
Proof. Follow the same steps,
b𝜏1 = 1 𝑛 𝑛∑︁ 𝑖=1 𝑉𝑖𝑊𝑖𝑌𝑖 𝑝𝜋 − 1 𝑛 𝑛∑︁ 𝑖=1 𝑉𝑖(1−𝑊𝑖)𝑌𝑖 𝑝(1−𝜋)
= 1 𝑛𝑝𝜋 𝑛∑︁ 𝑖=1 𝑉𝑖𝑊𝑖  𝑛∑︁ 𝑗=1  𝛼𝑗,𝑖+𝛽𝑗,𝑖𝑊𝑗+𝛾𝑗,𝑖𝑊𝑖+𝜁𝑗,𝑖𝑊𝑖𝑊𝑗  −
1
𝑛𝑝(1−𝜋)
𝑛∑︁
𝑖=1
𝑉𝑖(1−𝑊𝑖)
 𝑛∑︁ 𝑗=1  𝛼𝑗,𝑖+𝛽𝑗,𝑖𝑊𝑗+𝛾𝑗,𝑖𝑊𝑖+𝜁𝑗,𝑖𝑊𝑖𝑊𝑗 
= 1 𝑛𝑝𝜋 ∑︁ 𝑖≠𝑗 𝑉𝑖𝑊𝑖  𝛼𝑗,𝑖+𝛽𝑗,𝑖𝑊𝑗+𝛾𝑗,𝑖+𝜁𝑗,𝑖𝑊𝑗  −
1
𝑛𝑝(1−𝜋)
∑︁
𝑖≠𝑗
𝑉𝑖(1−𝑊𝑖)

𝛼𝑗,𝑖+𝛽𝑗,𝑖𝑊𝑗

Note that
(1) E(𝑉𝑖𝑊𝑖) =𝑝𝜋, E𝑉𝑖(1−𝑊𝑖) =𝑝(1−𝜋).
(2) E𝑉𝑖𝑊𝑖𝑊𝑗  = E[E𝑉𝑖𝑊𝑖𝑊𝑗

𝑗 and𝑖 are in the same cluster)] =
¯𝜎∗ E𝑉𝑖𝑊𝑖 +( 1− ¯𝜎)∗ E𝑉𝑖𝑊𝑖 E𝑊𝑗  = ¯𝜎𝑝𝜋+( 1− ¯𝜎)𝑝2𝜋2.

Unbiased Estimation for Total Treatment Effect Under Interference Using Aggregated Dyadic Data KDD’24, August 25–29, 2024, Barcelona, Spain
(3) E𝑉𝑖(1−𝑊𝑖)𝑊𝑗  = E[E𝑉𝑖(1−𝑊𝑖)𝑊𝑗

𝑗 and𝑖 are not in the
same cluster)] =(1− ¯𝜎)𝑝2𝜋(1−𝜋).
Hence
E(b𝜏1) = 1 𝑛 ∑︁ 𝑖≠𝑗  𝛼𝑗,𝑖+𝛾𝑗,𝑖+( 𝛽𝑗,𝑖+𝜁𝑗,𝑖)( ¯𝜎+( 1− ¯𝜎)𝑝𝜋)  −
1
𝑛
∑︁
𝑖≠𝑗

𝛼𝑗,𝑖+𝛽𝑗,𝑖(1− ¯𝜎)𝑝𝜋

= 1 𝑛 ∑︁ 𝑖≠𝑗  𝛽𝑖,𝑗 ¯𝜎+𝛾𝑖,𝑗+  ¯𝜎+( 1− ¯𝜎)𝑝𝜋𝜁𝑖,𝑗 
□
A.6 Proof of Proposition 3.6
Proof. Follow the same steps in (A.5),
b𝜏2 = 1 𝑛 𝑛∑︁ 𝑖=1 𝑉𝑖𝑊𝑖𝐷𝑖 𝑝𝜋 − 1 𝑛 𝑛∑︁ 𝑖=1 𝑉𝑖(1−𝑊𝑖)𝐷𝑖 𝑝(1−𝜋)
= 1 𝑛𝑝𝜋 𝑛∑︁ 𝑖=1 𝑉𝑖𝑊𝑖  𝑛∑︁ 𝑗=1  𝛼𝑖,𝑗+𝛽𝑖,𝑗𝑊𝑖+𝛾𝑖,𝑗𝑊𝑗+𝜁𝑖,𝑗𝑊𝑖𝑊𝑗  −
1
𝑛𝑝(1−𝜋)
𝑛∑︁
𝑖=1
𝑉𝑖(1−𝑊𝑖)
 𝑛∑︁ 𝑗=1  𝛼𝑖,𝑗+𝛽𝑖,𝑗𝑊𝑖+𝛾𝑖,𝑗𝑊𝑗+𝜁𝑖,𝑗𝑊𝑖𝑊𝑗 
= 1 𝑛𝑝𝜋 ∑︁ 𝑖≠𝑗 𝑉𝑖𝑊𝑖  𝛼𝑖,𝑗+𝛽𝑖,𝑗+𝛾𝑖,𝑗𝑊𝑗+𝜁𝑖,𝑗𝑊𝑗  −
1
𝑛𝑝(1−𝜋)
∑︁
𝑖≠𝑗
𝑉𝑖(1−𝑊𝑖)

𝛼𝑖,𝑗+𝛾𝑖,𝑗𝑊𝑗

Hence
E(b𝜏2) = 1 𝑛 ∑︁ 𝑖≠𝑗  𝛼𝑖,𝑗+𝛽𝑗,𝑖+(𝛾𝑗,𝑖+𝜁𝑖,𝑗)( ¯𝜎+( 1− ¯𝜎)𝑝𝜋)  −
1
𝑛
∑︁
𝑖≠𝑗

𝛼𝑖,𝑗+𝛾𝑖,𝑗(1− ¯𝜎)𝑝𝜋

= 1 𝑛 ∑︁ 𝑖≠𝑗  𝛽𝑖,𝑗+𝛾𝑖,𝑗 ¯𝜎+  ¯𝜎+( 1− ¯𝜎)𝑝𝜋𝜁𝑖,𝑗 
□
