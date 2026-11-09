---
title: Efficient and Effective Algorithms for A Family of Influence Maximization Problems with A Matroid
  Constraint
url: https://arxiv.org/abs/2410.16603
category: social-media
subcategory: empirical
date: 2024-10
venue: ''
authors:
- Yiqian Huang
- Shiqi Zhang
- Laks V. S. Lakshmanan
- Wenqing Lin
- Xiaokui Xiao
source: arxiv
pdf_url: https://arxiv.org/pdf/2410.16603
pages: 22
chars: 105408
fetched_at: '2026-11-08T13:03:19+00:00'
kb_version: 1
---

# Efficient and Effective Algorithms for A Family of Influence Maximization Problems with A Matroid Constraint

Efficient and Effective Algorithms for A Family of Influence
Maximization Problems with A Matroid Constraint
[Technical Report]
Yiqian Huang
National University of Singapore
yiqian@comp.nus.edu.sg
Shiqi Zhang
National University of Singapore
PyroWis AI
shiqi@pyrowis.ai
Laks V.S. Lakshmanan
University of British Columbia
laks@cs.ubc.ca
Wenqing Lin
Tencent
edwlin@tencent.com
Xiaokui Xiao
National University of Singapore
xkxiao@nus.edu.sg
Bo Tang
Southern University of Science and
Technology
tangb3@sustech.edu.cn
ABSTRACT
Influence maximization (IM) is a classic problem that aims to iden-
tify a small group of critical individuals, known as seeds, who can
influence the largest number of users in a social network through
word-of-mouth. This problem finds important applications includ-
ing viral marketing, infection detection, and misinformation con-
tainment. The conventional IM problem is typically studied with
the oversimplified goal of selecting a single seed set. Many real-
world scenarios call for multiple sets of seeds, particularly on social
media platforms where various viral marketing campaigns need
different sets of seeds to propagate effectively. To this end, previous
works have formulated various IM variants, central to which is the
requirement of multiple seed sets, naturally modeled as a matroid
constraint. However, the current best-known solutions for these
variants either offer a weak (1/2−𝜖)-approximation, or offer a
(1− 1/𝑒−𝜖)-approximation algorithm that is very expensive. We
propose an efficient seed selection method called AMP, an algo-
rithm with a(1− 1/𝑒−𝜖)-approximation guarantee for this family
of IM variants. To further improve efficiency, we also devise a fast
implementation, called RAMP. We extensively evaluate the perfor-
mance of our proposal against 6 competitors across 4 IM variants
and on 7 real-world networks, demonstrating that our proposal
outperforms all competitors in terms of result quality, running time,
and memory usage. We have also deployedRAMP in a real industry
strength application involving online gaming, where we show that
our deployed solution significantly improves upon the baselines.
PVLDB Reference Format:
Yiqian Huang, Shiqi Zhang, Laks V.S. Lakshmanan, Wenqing Lin, Xiaokui
Xiao, and Bo Tang. Efficient and Effective Algorithms for A Family of
Influence Maximization Problems with A Matroid Constraint. PVLDB,
18(2): XXX-XXX, 2025.
doi:XX.XX/XXX.XX
This work is licensed under the Creative Commons BY-NC-ND 4.0 International
License. Visit https://creativecommons.org/licenses/by-nc-nd/4.0/ to view a copy of
this license. For any use beyond those covered by this license, obtain permission by
emailing info@vldb.org. Copyright is held by the owner/author(s). Publication rights
licensed to the VLDB Endowment.
Proceedings of the VLDB Endowment, Vol. 18, No. 2 ISSN 2150-8097.
doi:XX.XX/XXX.XX
PVLDB Artifact Availability:
The source code, data, and/or other artifacts have been made available at
https://github.com/waetr/IM_GM.
1 INTRODUCTION
Given a social network, the problem of influence maximization
(IM) seeks to find a small group of users who can (directly or
indirectly) influence as many users in the network as possible.
It has been applied in various domains, including viral market-
ing [17, 35], efficient infection detection [37], and misinformation
containment [10, 45, 53], among others. Viral marketing, for in-
stance, typically involves a company setting up a campaign to
promote a product by incentivizing a set of influential users (called
“seeds”), aiming to maximize the number of influenced users (re-
ferred to as “spread”) by triggering a cascade of adoptions through
word-of-mouth. Existing work on IM has mostly focused on this
setting of single seed set.
Real-world scenarios of viral marketing are often more com-
plex, requiring multiple sets of seeds, to optimize the overall spread
produced by these sets. This complexity is clearly evident in the
rise of influencer marketing platforms, including the official cre-
ator marketplaces of social media platforms such as Instagram [33],
TikTok [52], and Douyin [23], as well as over 80 third-party plat-
forms [32]. These platforms act as intermediaries, aligning adver-
tisers with key influencers for social advertising campaigns and
aiding influencers in monetizing their online presence. E.g., the
Douyin Xingtu platform reported a substantial user base of over 1.9
million advertisers and 3.2 million creators as of June 2022 [22]. A
critical task for them is coordinating diverse advertiser campaigns
and determining optimal seed sets such that the content created by
the seeds can reach a broader audience through word-of-mouth.
The above viral marketing scenarios that seek multiple seed
sets can be modeled as an IM problem subject to a general matroid
constraint (IM-GM). A general matroid (formal definition in § 2.2)
represents constraints that an IM solution must adhere to. It is
defined as a pair(𝑈,I), where𝑈 is a ground set of elements from
which seeds are selected, andI is a collection of subsets of𝑈 (called
independent sets), representing feasible solutions to the problem.
For example, we show an instance ofIM-GM in the context ofrevenue
maximization.
arXiv:2410.16603v1  [cs.SI]  22 Oct 2024

Example 1.1 (Revenue Maximization). Consider the scenario of
incentivized social advertising [2, 30] where we need to coordinate
𝑇 viral marketing campaigns, such that seed sets𝑆𝑖,𝑆𝑗 selected for
different campaigns𝑖 ≠ 𝑗 do not overlap, and the sum of spread
produced by all campaigns is maximized. This scenario cannot be
trivially treated as independently running IM𝑇 times, as a seed can
contribute to more than one campaign, motivating the introduction
of a matroid. In this case, the ground set𝑈 comprises all possible
combinations of users and campaigns, whileI corresponds to all
feasible solutions(𝑆1,...,𝑆 𝑇) which satisfy𝑆𝑖∩𝑆𝑗 =∅,𝑖 ≠ 𝑗. □
The IM-GM formulation also captures numerous other real-world
applications [16, 41, 46, 47, 57]. We illustrate two such applications:
multi-round IM and adversarial attacks on IM.
Example 1.2 (Multi-Round IM). In the recruitment-based cam-
paign of the Xingtu mobile app [11], service providers select seeds
from a candidate pool in multiple rounds, such that each round’s
seed set has a size≤𝑘 and the spread across all rounds is maximized;
this cardinality constraint can be captured using a matroid. □
Example 1.3 (Adversarial Attacks on IM). In combating the spread
of illicit activities such as pyramid scheme scams [24], money laun-
dering [34], and phishing scams [56], authorities identify not only
malicious users but also suspicious relationships for blocking in order
to control further spread of such activities. Owing to the sensitivity
of blocking, in practice there are limits on the number of users and
relationships that can be blocked. This problem can be modeled as
an instance of IM-GM, with a matroid constraining the maximum
number of identified users and relationships for blocking. □
There exist a number of solutions to IM-GM [2, 13, 16, 18, 20,
30, 41, 46, 47, 49, 57], most of which utilize the greedy approach
introduced by Fisher et al. [25]. The greedy approach iteratively
selects the element with the largest improvement of the objective
function under the matroid constraint, resulting in a (1/2−𝜖)-
approximation for any given𝜖 > 0. Subsequent work [12] improves
upon this result and presents a(1− 1/𝑒−𝜖)-approximation algo-
rithm for submodular maximization under a matroid constraint.
Unlike the greedy approach, it first iteratively searches for a frac-
tional solution which contains a fraction for each element in 𝑈 ,
with each fraction representing the probability that the element
is selected. It then converts the fractional solution into a discrete
one, by randomly rounding each fraction to either 0 or 1. However,
this algorithm incurs significant computational cost and fails to
handle even datasets with a few hundred users (see § 4.1), because
it requires sampling a large number of random subsets of𝑈 in the
evaluation of candidate fractional solutions.
To address this issue, we propose AMP, an algorithm that en-
sures(1− 1/𝑒−𝜖)-approximation for IM-GM while offering superior
efficiency. AMP shares a similar framework as mentioned above
but performs the search and rounding steps deterministically. The
linchpin lies in the fact that AMP avoids expensive random sam-
pling in the assessment of fractional solutions by utilizing a new
estimation method, which reduces computation costs by exploiting
the characteristics of fractional solutions inIM-GM. We also present
RAMP, an algorithm that further improves AMP’s efficiency by
adapting the doubling strategy from Tang et al. [48], but with care-
ful redesign to ensure the correctness forIM-GM. We experimentally
evaluate the performance of AMP and RAMP against 6 competitors
across 4 IM-GM instances, on 7 real-world networks ranging in size
from thousands of nodes and edges to millions of nodes and billions
of edges. Notably, AMP outperforms all competitors by up to 871%
in terms of result quality. Besides, RAMP surpasses the state-of-
the-art by up to 1, 000× in running time and 10× in memory usage,
respectively. In addition, we have deployed our solution RAMP on
a Tencent online gaming platform, and observed that it attracted
160,000 more user engagements compared to the control group
using the current state-of-the-art solution.
To summarize, we make the following contributions in this work:
• We propose an efficient(1− 1/𝑒−𝜖)-approximation solution
AMP for IM-GM (§ 4).
• We provide a scalable implementationRAMP for further improv-
ing the efficiency of AMP (§ 5).
• Our extensive experiments show that AMP and RAMP can effi-
ciently scale to datasets with billions of edges (§ 6).
• We deploy our solution to a Tencent online game and signifi-
cantly improve on the state of the art in user engagement (§ 7).
2 PRELIMINARIES
We provide basic terminology and notations in § 2.1, followed by
formulating influence maximization subject to a general matroid
constraint (IM-GM) in § 2.2. We review typical instances of IM-GM
and their solutions in § 2.3 and § 2.4, respectively.
2.1 Terminology and Notations
Social networks. A social network is a directed graph G =(𝑉,𝐸),
where𝑉 is a set of nodes representing users and𝐸 is a set of edges
representing relationships. Each directed edge𝑒𝑖,𝑗 ∈𝐸 is associated
with𝑝𝑖,𝑗 ∈ [0, 1], and indicates that 𝑣𝑗 can be influenced by 𝑣𝑖
with probability𝑝𝑖,𝑗 . We say𝑣𝑖 (resp.𝑣𝑗 ) the in-neighbor (resp. out-
neighbor) of𝑣𝑗 (resp.𝑣𝑖), and denote the set of in-neighbors (resp.
out-neighbors) of𝑣𝑖 as𝑁𝑖𝑛 𝑖 (resp.𝑁𝑜𝑢𝑡 𝑖 ).
Monotone and submodular functions. Given a set 𝑈 , a non-
negative set function𝑓 is monotone if∀𝑋⊆𝑌⊆𝑈,𝑓 (𝑋)≤ 𝑓(𝑌).
𝑓 is submodular if∀𝑋⊆𝑌⊆𝑈 and𝑢𝑖∈𝑈\𝑌,𝑓 (𝑢𝑖|𝑋)≥ 𝑓(𝑢𝑖|𝑌),
where 𝑓(𝑢𝑖|𝑋) = 𝑓(𝑋∪{𝑢𝑖})− 𝑓(𝑋) denotes the marginal gain
of𝑓 after adding𝑢𝑖 to𝑋. As an example, given a collectionR of
subsets of𝑈 , the coverage function of a set𝑆⊆𝑈 , defined as
ΛR(𝑆) = ˝ 𝑅∈R I(𝑆∩𝑅 ≠∅), (1)
where I(·) is the indicator function, is monotone and submodular.
Notations. Throughout this paper, an upper-case letter𝐴 (resp. a
calligraphic upper-case letterA) denotes a set (resp. a collection of
sets). For a ground set𝑈 , a boldface lower-case letter x∈[ 0, 1]𝑈
represents a vector corresponding to𝑛 elements of𝑈 , where x[𝑖]
denotes the value associated with the element𝑢𝑖∈𝑈 . As a special
case, 1𝑖 (resp. 1𝑆) signifies the indicator vector with value 1 for𝑢𝑖
(resp. for each element𝑢𝑖∈𝑆) and value 0 otherwise. Table 1 lists
the frequently used notations.
2.2 Problem Formulation
Given a graph G =(𝑉,𝐸) and a set𝑆⊆𝑉 of chosen nodes (called
seeds), a diffusion model describes the process by which information
spreads from𝑆 to other nodes via social connections in G. In this

Table 1: Frequently used notations.
Notation Description
G =(𝑉,𝐸) A graph G with node set𝑉 and edge set𝐸.
M =(𝑈,I) A matroid M with ground set𝑈 and collectionI of independent sets.
𝑛 The number of elements in𝑈 .
𝑟,B The rank of M and the collection of all bases in M.
ℎ,𝑘𝑖 The number of partitions, and the capacity of the𝑖-th partition in M.
𝑅,R A random RR set and a collection of random RR sets.
ΛR,𝜎 The coverage function in Eq.(1) and the objective in Definition 2.2.
x The fractional solution of element selection in § 4.
work, we consider the well-known Independent Cascade (IC) [26]
and Linear Threshold (LT) [27] models, where a diffusion instance
captures the stochastic diffusion process from 𝑆 and unfolds in
discrete steps. At the beginning of a diffusion instance L of IC
or LT, all seeds in 𝑆 are set to be active at step 0, leaving other
nodes inactive. In IC, at step𝑡 > 0, each node𝑣𝑖 activated at step
𝑡− 1 has one chance to independently activate its inactive out-
neighbor𝑣𝑗 with probability𝑝𝑖,𝑗 . LT requires that for each node
𝑣𝑗 , (i) ˝ 𝑣𝑖∈𝑁𝑖𝑛 𝑗 𝑝𝑖,𝑗 ≤ 1, and (ii) a threshold𝜆𝑗∈[ 0, 1] is sampled
uniformly at step 0. At step𝑡 > 0, an inactive node𝑣𝑗 is activated
iff the sum of𝑝𝑖,𝑗 w.r.t.𝑣𝑗 ’s activated in-neighbors𝑣𝑖 exceeds𝜆𝑗 .
During a diffusion instance L of IC or LT, once a node is activated,
it remains active in all subsequent steps. L terminates if no more
nodes can be activated, and the set of eventually activated nodes is
denoted as ΓL(G,𝑆). Accordingly, the spread of𝑆 in𝐺 is defined as
𝜌G(𝑆) = E[| ΓL(G,𝑆)|]. (2)
Based on these concepts, Kempe et al. [36] define the influence
maximization (IM) problem as follows.
Definition 2.1 ( IM). Given a graph G, a diffusion model and a
cardinality𝑘, the IM problem is to select a seed set 𝑆 ⊆ 𝑉 with
|𝑆|≤ 𝑘 such that the spread𝜌G(𝑆) defined in Eq.(2) is maximized.
We next review concepts of matroids and then propose a gener-
alized IM problem, viz., IM subject to a general matroid (IM-GM).
Matroids. A general matroid is a pair M =(𝑈,I), where𝑈 is a
finite set (called the ground set) with|𝑈| =𝑛 andI is a collection
of subsets of𝑈 (called independent sets) satisfying the following
axioms: (i)I ≠∅; (ii) if𝐼∈I and𝐽⊆𝐼, then𝐽∈I ; (iii) if𝐼,𝐽 ∈I
and|𝐼| <|𝐽|, then there exists 𝑢𝑖 ∈ 𝐽\𝐼 such that 𝐼∪{𝑢𝑖}∈I .
Of special interest is the partition matroid, whose ground set𝑈 is
divided intoℎ≥ 1 disjoint partitions𝑈1,...,𝑈 ℎ, each𝑈𝑖 associated
with a positive integer 𝑘𝑖. The set of independent sets I in the
partition matroid is defined asI ={𝑆⊆𝑈 :|𝑆∩𝑈𝑖|≤ 𝑘𝑖,∀𝑖∈[ ℎ]}.
In the special case whereℎ = 1, the partition matroid reduces to a
uniform matroid, characterized byI ={𝑆⊆𝑈 :|𝑆|≤ 𝑘}.
Given a matroid M =(𝑈,I), any independent set𝐵∈I with
the largest cardinality, i.e.,|𝐵| = max{|𝐼| : 𝐼 ∈I} , is a base and
its cardinality𝑟 is the rank of M. E.g.,𝑟 = ˝ℎ 𝑖=1𝑘𝑖 in the partition
matroid and 𝑟 = 𝑘 in the uniform matroid. A matroid can have
multiple bases. We denote the collection of all bases of M asB.
Definition 2.2 ( IM-GM). Given a graph G, a diffusion model, and
a matroid M =(𝑈,I) where𝑈 is built on G, IM-GM aims to find a
set𝑆∈I that maximizes a given objective function𝜎 : 2𝑈→ R+,
which is associated with the spread function in Eq.(2).
Observe in Definitions 2.1-2.2 that IM is an instance of IM-GM,
where M is a uniform matroid and 𝜎(𝑆) = 𝜌G(𝑆). Besides IM, a
plethora of IM variants [2, 13, 16, 18, 30, 41, 46, 47, 57] can also be
modeled using IM-GM. The next section will discuss three instances,
obtained from different instantiations of M and𝜎.
2.3 Representative IM-GM Instances
Revenue maximization (RM) [2, 18, 30]. Given a graph𝐺 =(𝑉,𝐸),
a diffusion model, and𝑇 campaigns associated with𝑇 unit revenues
𝛼1,...,𝛼 𝑇 , the RM problem aims to select seed sets𝑆1,𝑆 2,...,𝑆 𝑇⊆𝑉
for the𝑇 campaigns such that the total revenue𝜎(𝑆1,𝑆 2,...,𝑆 𝑇) =˝𝑇
𝑡 =1𝛼𝑡·𝜌𝐺(𝑆𝑡) is maximized. This problem is subject to a user
constraint that each node 𝑣𝑖 ∈ 𝑉 can be included in at most 𝑘𝑖
seed sets, where𝑘𝑖≤𝑇 is a number associated with node𝑣𝑖. This
constraint corresponds to a partition matroidM =(𝑈,I), where the
ground set𝑈 =𝑉×[𝑇] contains all pairs of nodes and campaigns.
𝑈 is partitioned into |𝑉| disjoint subsets 𝑈1,𝑈 2,...,𝑈 |𝑉|, where
𝑈𝑖 ={(𝑣𝑖,𝑡) :𝑡∈[ 𝑇]}. Accordingly,I ={𝑆⊆𝑈 :∀𝑣𝑖∈𝑉,|𝑆∩
𝑈𝑖|≤ 𝑘𝑖}. As a special case, we have 𝑘𝑖 = 1 for all𝑣𝑖∈𝑉 in the
scenario of incentivized social advertising [2, 30].
Non-adaptive multi-round IM (MRIM) [46]. Given a graph𝐺 =
(𝑉,𝐸), a diffusion model, a cardinality𝑘 and the number of cam-
paign rounds 𝑇 , the non-adaptive MRIM problem aims to select
seed set𝑆𝑡 ⊆ 𝑉 in each round𝑡, with|𝑆𝑡|≤ 𝑘, such that the ex-
pected number of activated nodes over all rounds𝜎(𝑆1,𝑆 2,...,𝑆 𝑇)
= E


—𝑇 𝑡 =1 ΓL𝑡(𝐺,𝑆𝑡)

 is maximized, where each diffusion instance
L𝑡 is obtained independently. This constraint can also be viewed
as a partition matroid with the ground set𝑈 =𝑉×[𝑇]. However,
in contrast with RM, this ground set is partitioned w.r.t. rounds, i.e.,
𝑈𝑡 ={(𝑣𝑖,𝑡) :𝑣𝑖∈𝑉}, andI ={𝑆⊆𝑈 :∀𝑡∈[𝑇],|𝑆𝑡|≤ 𝑘}.
Adversarial attacks on IM (AdvIM) [47]. Given a graph𝐺 =(𝑉,𝐸),
a diffusion model, a set of contagious seeds𝐴⊂𝑉 and two cardi-
nalities𝑘𝑣,𝑘𝑒, the AdvIM problem aims to select a blocking set 𝑆
consisting of a blocking node set 𝑆𝑣⊆𝑉\𝐴 with|𝑆𝑣|≤ 𝑘𝑣 and a
blocking edge set𝑆𝑒⊆𝐸 with|𝑆𝑒|≤ 𝑘𝑒, i.e.,𝑆 =𝑆𝑣∪𝑆𝑒, such that
the influence reduction𝜎(𝑆𝑣,𝑆𝑒) =𝜌𝐺(𝐴)− 𝜌𝐺\𝑆(𝐴) is maximized,
where𝐺\𝑆 =(𝑉\𝑆𝑣,𝐸\𝑆𝑒). The constraint in this problem corre-
sponds to a partition matroid with ground set𝑈 =(𝑉\𝐴)∪ 𝐸 and
independent setsI ={𝑆⊆𝑈 :|𝑆𝑣|≤ 𝑘𝑣,|𝑆𝑒|≤ 𝑘𝑒}.
2.4 Approximation Solutions for IM-GMs
Due to the NP-hardness of eachIM-GM problem and the inefficiency
of Monte-Carlo simulations, most previous works borrow the idea
of reverse reachable (RR) set sampling [7], originally designed for
vanilla IM. Specifically, an RR set consists of nodes identified by
simulating a reverse diffusion process of a given diffusion model
from a node 𝑣𝑖 selected uniformly at random. For example, the
reverse diffusion process of the IC model is a stochastic breadth-
first search starting from𝑣𝑖. For each visited 𝑣𝑎, it explores each
in-neighbor𝑣𝑏∈ 𝑁𝑖𝑛𝑎 with probability𝑝𝑏,𝑎. Borgs et al. [7] show
that for any seed set𝑆⊆𝑉 , the probability that an RR set overlaps
𝑆 equals 𝜌G(𝑆) |𝑉| . That is, if we have a collection R of RR sets, we
can use |𝑉| |R| · ΛR(𝑆) as an unbiased estimator of 𝜌G(𝑆). Accord-
ingly, Borgs et al. [7] propose an approximation solution for IM,
which runs in two main steps: (i) RR set generation : sample a set
R of RR sets, with the size |R| sufficient to achieve the desired

approximation; (ii) element selection: use a greedy algorithm for
solving maximum coverage which returns a set𝑆 that maximizes
the coverage ΛR(𝑆). Borgs et al. ’s framework is also leveraged in
various IM-GM instances [2, 16, 30, 41, 46, 47, 57]. A central role in
determining the approximation is played by various greedy element
selection algorithms used in these works, briefly reviewed below.
Greedy [25]. This algorithm greedily selects elements with the
maximum marginal gain subject to the matroid constraint. Specifi-
cally, it starts with a set𝑆 =∅, and then iteratively adds𝑟 elements
to𝑆. In each iteration, it adds𝑢𝑖 to𝑆 if ΛR(𝑢𝑖|𝑆) is the largest among
the elements of𝑈\𝑆 and the inclusion maintains the matroid con-
straint. This algorithm achieves a 1/2-approximation subject to a
general matroid constraint [25] and is the most commonly adopted
algorithm in prior works for IM-GM problems [2, 16, 30, 46, 47, 57].
Local-Greedy [46]. Designed for the partition matroid constraint,
Local-Greedy selects elements partition by partition. Specifically,
it greedily selects elements in the first partition with capacity𝑘1.
Once𝑘1 elements are selected, it proceeds to the second partition,
and so on. This improves the efficiency by pruning the search space
from𝑈 to each partition. Sun et al. [46] prove that Local-Greedy
achieves a 1−𝑒−( 1− 1 𝑒)≈ 0.46 approximation.
Threshold-Greedy [9]. Unlike Greedy, Threshold-Greedy adds
an element𝑢𝑖 to𝑆 if ΛR(𝑢𝑖|𝑆) exceeds a threshold, which starts
at a predefined value and decreases by (1−𝜉) in each iteration.
Compared to Greedy, this algorithm boosts efficiency by reducing
the number of iterations from𝑟 to𝑂 𝜉−1· ln(𝑟/𝜉), while incurring
a loss term𝜉, resulting in an approximation ratio of 1/2−𝜉 [9].
Due to the variety of diffusion models and objectives, IM-GM
solutions require two additional steps before RR set generation:
(i) select a strategy of RR set construction for an IM-GM instance,
where an RR set𝑅 consists of elements in𝑈 instead of nodes in𝑉 ;
(ii) rewire the coverage ΛR and the objective𝜎 such that the scaled
ΛR(𝑆) is an unbiased estimator of𝜎(𝑆), i.e.,𝜎(𝑆) = 𝜅 |R| · E[ΛR(𝑆)],
where the value of constant𝜅 depends on the given IM-GM instance.
E.g., MRIM [46] first selects a random node𝑣𝑖∈𝑉 uniformly, then
independently simulates𝑇 reverse diffusion processes starting from
𝑣𝑖. Denoting the set of examined nodes in each process𝑖 as𝑅′ 𝑖 , the
RR set in MRIM is𝑅′ 1×{ 1}∪···∪ 𝑅′ 𝑇×{𝑇}, and we have𝜅 =|𝑉|. For
the remaining instances, we refer interested readers to Appendix D.
To improve the efficiency of Borgs et al. ’s framework for the
vanilla IM, subsequent solutions, e.g.,TIM [51], IMM [50], DSSA [43],
and OPIM-C [48], focus on reducing the number of sampled RR sets
while ensuring the same approximation ratio. As of now, OPIM-C
is the state of the art and it has been applied to subsequent solu-
tions [6, 28–30, 57]. Most scalable solutions of otherIM-GM instances
also extend the aforementioned ones used inIM. E.g., in RM, [30] uti-
lizes a greedy variant by mixingGreedy and Threshold-Greedy, and
then follows OPIM-C to achieve an approximation not exceeding
1/2−𝜖. Additionally, [46] and [47] offer a(1/2−𝜖)-approximation
for MRIM and AdvIM, respectively, by employing Greedy and IMM.
3 RELATED WORK
Since its introduction in [36], the IM problem has been extensively
researched – see [40] for a comprehensive survey. Here, we mainly
focus on IM under a matroid constraint. Various kinds of matroids
have been considered in previous IM studies. Besides the three
IM-GM instances introduced in § 2.3, partition matroids are also em-
ployed in several IM-GM instances, including capacity constrained
IM [57], IM with fairness constraint [ 20], the lattice IM with par-
titioned budgets [ 16], and so forth [ 13, 49]. Furthermore, other
general matroids are used in previous IM-GM studies to accommo-
date more sophisticated scenarios. For instance, the popularity ratio
maximization problem [41] follows the multiple round setting in
MRIM but aims to significantly surpass competitors’ outreach in
popularity by initiating influence cascades. This paper studies the
intersection of a uniform matroid that restricts the overall car-
dinality with a partition matroid, resulting in a general matroid 1
constraint. As another example, the general version of IM for multi-
ple products [18] requires a laminar matroid constraint that models
capacity limits within hierarchical community structures, such as
the maximum number of selected customers in different states and
the cities they contain. While developing different approaches, the
core ideas of these solutions lie in either Greedy, Local-Greedy, or
Threshold-Greedy, all limited to at most a(1/2−𝜖)-approximation.
In theoretical computer science, another line of previous works
aims to maximize a general submodular function under a matroid
constraint. [12] proposed continuous greedy, the first polynomial-
time algorithm with a(1− 1/𝑒−𝜖) approximation guarantee. [4]
later refined it, achieving state-of-the-art results for general ma-
troids. However, adopting these algorithms in IM-GM is highly in-
efficient, as detailed in § 4.1. Subsequent research has focused on
specific categories of matroids [9, 21, 31]. [9] introduce some spe-
cific optimizations for partition matroids, resulting in an𝑂(𝑛3/2)-
time algorithm. Prior works [ 21, 31] further develop algorithms
with𝑂(𝑛· poly(1/𝜖, log𝑛)) time complexity for partition, graphic,
transversal, and laminar matroids. The above approaches cannot
be directly adopted for IM-GM instances, as they do not apply for
general matroids outside the above matroid classes.
In the next two sections, we present our approach for solving
IM-GM. Given that our overall approach is based on generating
a collection of RR sets and then selecting a set that maximizes
coverage, we divide the presentation along the same theme.
4 ELEMENT SELECTION
Given a set of RR sets R, this section proposes an element-wise
Ascent algorithm over Matroid Polytopes for element selection
(AMP), providing a(1− 1/𝑒−𝜖)-approximation for maximizing the
coverage ΛR subject to the matroid constraint. We first discuss the
challenges in adopting prior(1− 1/𝑒−𝜖)-approximate solutions
and the main idea of AMP (§ 4.1), followed by detailed descriptions
of two core subroutines AMPSearch/AMPSearch-PM (§ 4.2) and
AMPRound (§ 4.3). At last, we provide an analysis of correctness
and time complexity (§ 4.4).
4.1 Overview
Main idea of existing solutions. Several continuous greedy algo-
rithms [4, 12] have been proposed to find(1− 1/𝑒−𝜖)-approximate
solutions for maximizing any monotone submodular function 𝑓
(e.g., ΛR) subject to a general matroid constraint. First, these solu-
tions expand the original function𝑓 to its corresponding multilinear
extension, defined as follows.
1It is not a partition matroid, unlike what is claimed in [41]. See Appendix A for details.

𝑢1
𝑢2
𝑢3
0
[0, 1, 1]
[1, 0, 1]
[1, 1, 0]
(a) Polytopes
𝑢1
𝑢2
𝑢3
0
1
3
2
3
1
1
3 2
3 1
(b) Previous solution
𝑢1
𝑢2
𝑢3
(c) Searching
max
min
𝐹(x)
(d) Rounding
Figure 1: Illustration of continuous greedy solutions andAMP subject to the matroid with𝑈 ={𝑢1,𝑢 2,𝑢 3} andI ={𝐼⊆𝑈 :|𝐼|≤ 2}.
Definition 4.1 (Multilinear Extension). For a set function 𝑓 :
2𝑈 → R+, its multilinear extension 𝐹 :[0, 1]𝑈 → R+ is defined
as𝐹(x) = E[𝑓(Ω(x))], where Ω(x) is a random set that indepen-
dently includes each element𝑢𝑖∈𝑈 from the fractional result x
with probability x[𝑖].
Second, these solutions aim to solve the multilinear optimization
problem maxx∈𝑃I{𝐹(x)}, where𝑃I is the matroid polytope defined
as the convex hull (i.e., all convex combinations of elements) of
{1𝐼 :𝐼∈I}. Notice that, due to the monotonicity of𝑓 , the fractional
solution x that maximizes𝐹(x) is in the base polytope𝑃B =  x∈
𝑃I : ˝ 𝑖∈[𝑛] x[𝑖] =𝑟 	 [19]. To find such a solution x∈𝑃B, given
a parameter 𝜖, these approaches start from x = 0 and update x
by an iterative hill-climbing search process: at each step 𝑡, this
process examines basic solution 𝐵𝑡 ∈ Band the corresponding
fractional solution 𝜖· 1𝐵𝑡 such that 𝐹(x) can be improved after
adding this fractional solution to x. After 1/𝜖 steps, this process
returns a fractional solution x = ˝1/𝜖 𝑡 =1𝜖· 1𝐵𝑡, which is in 𝑃B by
definition. Finally, upon obtainingx∈𝑃B, these solutions employ a
randomized rounding process that eventually convertsx to a discrete
solution𝑆∈B , thus solving the original problem max𝑆∈I{𝑓(𝑆)}.
Example 4.2 (Illustrative Example). Consider a matroid with𝑈 =
{𝑢1,𝑢 2,𝑢 3} andI ={𝐼⊆𝑈 :|𝐼|≤ 2}. As depicted in Figure 1(a),
the origin representsx = 0, and the vertices[1, 1, 0],[1, 0, 1],[0, 1, 1]
indicate all bases. Additionally, the polyhedron and the shaded face
correspond to the matroid polytope and base polytope, respectively.
Assuming𝜖 = 1/3, the three shaded faces shown in Figure 1(b)
represent the feasible spaces for each search step. The solid and
dashed blue lines illustrate the search and rounding process of
previous solutions, respectively. Starting from x = 0, the search
process of Calinescu et al. [12] selects the direction of𝐵1 (i.e., 1𝐵1 =
[1, 1, 0]) and moves x to x+𝜖· 1𝐵1 =
 1
3, 1 3, 0  at the first step,
reaching the smallest shaded face. Subsequently, it selects 1𝐵2 =
[1, 0, 1] and moves x to x+𝜖· 1𝐵2 =
 2
3, 1 3, 1 3  , located in the medium
shaded face. At last, it updates x along the direction of𝐵3, bringing
x to

1, 2 3, 1 3  in the base polytope. Upon completing the search, to
round the fractional solution x, the algorithm [14] moves x on the
base polytope in random directions until it reaches a vertex, e.g.,
[1, 1, 0], indicating the final solution𝑆 ={𝑢1,𝑢 2}. □
Limitations of existing solutions. Existing algorithms suffer
from severe efficiency issues in the hill-climbing search stage, since
computing the multilinear extension𝐹 of a general monotone sub-
modular function𝑓 is expensive. Specifically, the multilinear exten-
sion of a set function𝑓 is
𝐹(x) =
∑︁
𝑆⊆𝑈
 Ö
𝑢𝑖∈𝑆
x[𝑖]
Ö
𝑢𝑖∈𝑈\𝑆
(1− x[𝑖])
!
·𝑓(𝑆). (3)
Computing𝐹(x) exactly involves enumerating all 2𝑛 subsets of𝑈 .
Previous works leverage random subset sampling to estimate𝐹(x),
however they still have a prohibitively expensive time complexity.
E.g., the approach of [12] which selects the𝑡-th basic solution𝐵𝑡
that yields an improvement in𝐹 along the direction of the base𝐵𝑡 ,
requires𝑂 𝑛7 log(𝑛) samples. The improved algorithm [4] selects
each basic solution 𝐵𝑡 using Threshold-Greedy, which includes
an element𝑢𝑖 into𝐵𝑡 if the partial derivative𝜕𝐹(x)/𝜕x[𝑖] exceeds
a pre-defined threshold. This compromises the result quality (see
§ 2.4) yet generates𝑂(𝑛𝑟𝜖−4· log2(𝑛/𝜖)) samples in total.
Additionally, in the rounding stage, existing randomized tech-
niques [1, 14] focus on the efficiency of maintaining x∈𝑃B rather
than the quality of the rounded result. To elaborate, the state-of-
the-art swap rounding [14] iteratively eliminates each distinct item
𝑢𝑖 from the difference between the current basic solution𝐵𝑡 and
the previous merged one𝐵𝑡−1 until all basic solutions are identical.
This is done by accepting 𝑢𝑖 w.p. 1/𝑡 if𝑢𝑖 ∈ 𝐵𝑡\𝐵𝑡−1 and with
the remaining probability if𝑢𝑖∈𝐵𝑡−1\𝐵𝑡 . As proved by [14], swap
rounding returns a discrete set𝑆∈B satisfying𝑓(𝑆)≥( 1−𝜓)𝐹(x)
w.p. at least 1−𝑒−𝐹(x)𝜓 2 8𝐹∗ , where𝐹∗ = maxx𝐹(x). Due to the ad-
ditional error term𝜓, more iterations in the search step or more
RR sets are required to ensure the desired total error𝜖, resulting in
significant computational overhead. Furthermore, the failure prob-
ability is𝑒−𝐹(x)𝜓 2 8𝐹∗ ≥𝑒−𝜓 2 8 > 0.88, which can severely compromise
the quality of the rounded result.
Our proposal. To address the above issues, we consider the mul-
tilinear extension of the coverage function ΛR(·) and show that
it can be evaluated efficiently and deterministically . Specifically, by
plugging ΛR(·) defined in Eq.(1) into Eq.(3), we have
𝐹(x) =
∑︁
𝑅∈R
∑︁
𝑆⊆𝑈
'›
«
Ö
𝑢𝑖∈𝑆
x[𝑖]
Ö
𝑢𝑗∈𝑈\𝑆
(1− x[𝑗])“ﬁ
‹
· I(𝑅∩𝑆 ≠∅),
which can be converted to𝐹(x) = ˝ 𝑅∈R E[I(𝑅∩ Ω(x) ≠∅)]. Since
E[I(𝑅∩ Ω(x) ≠∅)] = 1−˛ 𝑢𝑖∈𝑅(1− x[𝑖]) for a given𝑅⊆𝑈 ,𝐹(x)
can be further rewritten as
𝐹(x) =
∑︁
𝑅∈R
'›
«
1−
Ö
𝑢𝑖∈𝑅
(1− x[𝑖])“ﬁ
‹
. (4)

Algorithm 1: AMP(M,R,𝜖)
Input: The matroid M, an RR collectionR, 0 <𝜖≤ 1
Output: A discrete set𝑆∈B maximizing the coverage
1 QR←{ 𝑞𝑅 :𝑅∈R} ;∀𝑅∈R ,𝑞𝑅← 1;
2 ∀𝑡 = 1, 2,..., 1/𝜖,𝐵𝑡←∅ ; x← 0;
3 for𝑡 = 1, 2,..., 1/𝜖 do
4 if M is a partition matroid then
5 𝐵𝑡,QR← AMPSearch-PM(R, x,𝜖,QR);
6 else
7 𝐵𝑡,QR← AMPSearch(R, x,𝜖,QR)
8 x← x+𝜖· 1𝐵𝑡 ;
9 𝑆← AMPRound(R,𝜖,QR,𝐵 1,𝐵 2,...,𝐵 1/𝜖);
10 return𝑆;
Based on this, we can efficiently calculate the exact value of𝐹(x)
by maintaining a collectionQR, consisting of the variable
𝑞𝑅 = ˛ 𝑢𝑖∈𝑅(1− x[𝑖]) (5)
for each𝑅∈R from the first iteration. This enables us to develop
new search and rounding algorithms capable of achieving the de-
sired(1− 1/𝑒−𝜖)-approximation efficiently. It is noteworthy that,
besides instances of IM-GM, Eq.(4) has the potential to improve IM
scenarios that are solved by leveraging the multilinear extension in
Eq.(3). This includes IM variants constrained by user groups [55]
and group fairness [54].
As outlined in Algorithm 1, our proposed AMP shares a similar
framework with existing continuous greedy methods but intro-
duces two new search strategies, AMPSearch (Algorithm 2) for the
general matroid and AMPSearch-PM (Algorithm 3) for the partition
matroid, and a deterministic rounding algorithm,AMPRound (Algo-
rithm 4). For ease of presentation, we assume w.l.o.g. that 1/𝜖 is an
integer, since for any given𝜖′, we can use 1 ⌈1/𝜖′⌉ as𝜖. During each
search iteration𝑡, AMPSearch and AMPSearch-PM adopt a more
refined approach compared to the coarse-grained search of previous
works [4, 12]. Specifically, they aim for the steepest improvement
in𝐹 and include the element𝑢𝑖 with the largest𝜕𝐹(x)/𝜕x[𝑖] into
𝐵𝑡 , resulting in quicker convergence and fewer search iterations.
AMPSearch-PM improves the efficiency of AMPSearch further by
pruning the search space 𝑈 to one partition, reducing the num-
ber of evaluations of partial derivatives by a factor of𝑟/𝑘∗, where
𝑘∗ = max{𝑘1,𝑘 2,...𝑘 ℎ}. As for the rounding phase, unlike the
randomized methods, our proposed AMPRound deterministically
decides the elimination of a distinct element𝑢𝑖 based on the par-
tial derivative w.r.t. x𝑖. This ensures that 𝐹(x) does not decrease
throughout rounding untilx becomes integral, yielding the rounded
result𝑆 satisfying ΛR(𝑆)≥ 𝐹(x) without failure probability.
For the illustrative example in Figure 1, the red arrowed lines
in Figures 1(c) and (d) trace the movement of x in the search and
rounding process of AMP, respectively. Initially, when x = 0 and
AMP starts to search for𝐵1,𝑢2 is first included as𝜕𝐹(x)/𝜕x[2] is the
largest, updating x to x =

0, 1 3, 0  . Next, as𝜕𝐹(x)/𝜕x[1] becomes
the largest w.r.t. the current x,𝑢1 is included in𝐵1, leading to an
update of x to
 1
3, 1 3, 0  . Analogously,𝑢3 and𝑢2 (resp.𝑢1 and𝑢3) are
selected and the corresponding basic solution is𝐵2 ={𝑢2,𝑢 3} (resp.
𝐵3 ={𝑢1,𝑢 3}), eventually yielding a fractional result x =
 2
3, 2 3, 2 3 
Algorithm 2: AMPSearch(R, x,𝜖,QR)
Input: An RR collectionR, a fractional solution x∈[ 0, 1]𝑈 ,
0 <𝜖≤ 1,QR defined in Algorithm 1
Output: A basic solution𝐵∈B , an updated collectionQR
1 𝐵←∅ ; y← x;
2 for𝑖 = 1, 2,...,𝑟 do
3 𝑢𝑗← arg max
𝑢𝑗 :𝑢𝑗∈𝑈\𝐵,𝐵∪{𝑢𝑗}∈I
(
˝
𝑅∈R :𝑢𝑗∈𝑅
𝑞𝑅
1−y[𝑗]
)
;
4 y[𝑗]← y[𝑗]+ 𝜖;𝐵←𝐵∪{𝑢𝑗};
5 ∀𝑅∈R :𝑢𝑗∈𝑅, 𝑞𝑅←𝑞𝑅· 1−y[𝑗] 1−y[𝑗]+𝜖 ;
6 return𝐵,QR ;
in the base polytope, as shown in Figure 1(c). After completing
the search, as illustrated in Figure 1(d), AMP moves x to a vertex
by ensuring the directions are towards maximizing𝐹(x) (i.e., the
brighter area), thereby guaranteeing𝐹(x) is non-decreasing. □
4.2 Element-wise Ascent Search
We first present our element selection algorithm AMPSearch for
the general matroid constraint (pseudocode in Algorithm 2). Specifi-
cally, Line 1 initializes by setting𝐵 =∅ and the vector y = x. It then
proceeds to iteratively populate𝐵 through𝑟 iterations, each time
adding an element to construct a basic solution. In Line 3, during
each iteration𝑖, AMPSearch examines all elements in the remain-
ing set𝑈\𝐵 and selects the element𝑢𝑗 that maximizes the value of˝
𝑅∈R :𝑢𝑗∈𝑅𝑞𝑅/(1− y[𝑗]), while adhering to the matroid constraint.
This value corresponds to the partial derivative 𝜕𝐹(y)/𝜕y[𝑗] as
shown below. All proofs are available in Appendix B.
Lemma 4.3. ∀y∈[ 0, 1]𝑈 and𝑢𝑖∈𝑈, 𝜕𝐹(y) 𝜕y[𝑖] = ˝ 𝑅∈R :𝑢𝑖∈𝑅 𝑞𝑅 1−y[𝑖].
In Lines 4 - 5,AMPSearch updates y[𝑗] to y[𝑗]+𝜖 and includes𝑢𝑗
in𝐵, followed by maintaining the correctness of each𝑞𝑅 value as per
Eq.(5). In particular, for each RR set𝑅 containing𝑢𝑗 , AMPSearch
updates the corresponding 𝑞𝑅 by scaling it with 1−y[𝑗] 1−y[𝑗]+𝜖 . This
process removes the outdated factor 1− y[𝑗]+ 𝜖 and includes the
latest value of 1− y[𝑗].
We next introduce the algorithm AMPSearch-PM tailored for
the partition matroid constraint. In contrast to AMPSearch which
selects the next element from𝑈\𝐵, Algorithm 3 selects an arbitrary
partition𝑈𝑙 of𝑈 satisfying|𝐵∩𝑈𝑙| <𝑘𝑙 , and chooses the element
𝑢𝑗 from𝑈𝑙\𝐵 during each iteration, thus reducing the search space
and running time of AMPSearch by a factor of𝑟/𝑘∗, where𝑘∗ =
max{𝑘1,𝑘 2,...𝑘 ℎ}. The following lemma offers a guarantee of both
algorithms, bounding how much𝐹(x) increases as it approaches the
optimal result𝑆𝑜 for maximizing ΛR(·) s.t. the matroid constraint.
Lemma 4.4. For any input fractional result x, the output 𝐵 of both
AMPSearch and AMPSearch-PM satisfies ΛR(𝑆𝑜)− 𝐹(x+𝜖· 1𝐵)≤
ΛR(𝑆𝑜)−𝐹(x)
1+𝜖 , where𝑆𝑜 = arg max 𝑆∈I ΛR(𝑆).
4.3 Element-wise Ascent Rounding
We introduce the rounding algorithm AMPRound, outlined in Al-
gorithm 4. Given the basic solutions𝐵1,𝐵 2,...,𝐵 1/𝜖, AMPRound

Algorithm 3: AMPSearch-PM(R, x,𝜖,QR)
Input: An RR collectionR, a fractional solution x∈[ 0, 1]𝑈 ,
0 <𝜖≤ 1,QR defined in Algorithm 1
Output: A basic solution𝐵∈B , an updated collectionQR
1 𝐵←∅ ; y← x;
2 for𝑖 = 1, 2,...,𝑟 do
3 𝑈𝑙← an arbitrary partition such that|𝐵∩𝑈𝑙| <𝑘𝑙 ;
4 𝑢𝑗← arg max
𝑢𝑗 :𝑢𝑗∈𝑈𝑙\𝐵
(
˝
𝑅∈R :𝑢𝑗∈𝑅
𝑞𝑅
1−y[𝑗]
)
;
5 y[𝑗]← y[𝑗]+ 𝜖;𝐵←𝐵∪{𝑢𝑗};
6 ∀𝑅∈R :𝑢𝑗∈𝑅, 𝑞𝑅←𝑞𝑅· 1−y[𝑗] 1−y[𝑗]+𝜖 ;
7 return𝐵,QR ;
maintains a vector
y = ˝1/𝜖 𝑙=𝑡+1𝜖· 1𝐵𝑙+𝑡·𝜖· 1𝐵𝑡, (6)
which represents the value of the fractional solution (i.e., x) af-
ter merging the first𝑡 fractional solutions𝜖1𝐵1,𝜖 1𝐵2,...,𝜖 1𝐵𝑡 cor-
responding to the basic solutions 𝐵1,𝐵 2,...,𝐵 𝑡 . It is initialized to
y = ˝1/𝜖 𝑙=1𝜖1𝐵𝑙 . AMPRound then scans each pair of successive basic
solutions from(𝐵1,𝐵 2) to(𝐵1/𝜖−1,𝐵 1/𝜖). For each pair(𝐵𝑡,𝐵𝑡+1),
it iteratively eliminates distinct elements between the two basic
solutions until 𝐵𝑡+1 is identical to 𝐵𝑡 , and thereby merged with
all preceding basic solutions 𝐵𝑡−1,...,𝐵 1. More precisely, AM-
PRound picks an arbitrary element𝑢𝑖 from𝐵𝑡\𝐵𝑡+1, then identifies
an element𝑢𝑗 ∈ 𝐵𝑡+1\𝐵𝑡 such that swapping 𝑢𝑖 and𝑢𝑗 leads to
𝐵𝑡\{𝑢𝑖}∪{ 𝑢𝑗} and𝐵𝑡+1\{𝑢𝑗}∪{ 𝑢𝑖} being bases of the matroid, as
outlined in Lines 4-5. Notably, the existence of such an element𝑢𝑗
is assured by the following matroid exchange property.
Lemma 4.5 (Matroid Exchange property [ 14]). Let𝐵1,𝐵 2 be
two bases of M. For any 𝑢𝑖∈ 𝐵1\𝐵2, there exists 𝑢𝑗 ∈ 𝐵2\𝐵1 such
that𝐵1\{𝑢𝑖}∪{ 𝑢𝑗} and𝐵2\{𝑢𝑗}∪{ 𝑢𝑖} are also bases.
Upon identifying a conflicting element pair (𝑢𝑖,𝑢𝑗), Lines 6-
13 retain the one with the larger partial derivative. If the partial
derivative w.r.t.𝑢𝑖 is not less than that w.r.t.𝑢𝑗 , AMPRound includes
𝑢𝑖∈𝐵𝑡\𝐵𝑡+1 into𝐵𝑡+1 while removing𝑢𝑗 from it. Correspondingly,
it updates the fractional result y by adding𝜖(1𝑖− 1𝑗) as per Eq.(6),
and modifies the values of𝑞𝑅 for all𝑅 that include𝑢𝑖 or𝑢𝑗 based on
Eq.(5). Conversely, if𝑢𝑗 is to be preserved, AMPRound updates𝐵𝑡
by replacing𝑢𝑖 with𝑢𝑗 , and adds𝑡𝜖· 1𝑗− 1𝑖  to y since the𝑡𝜖 1𝐵𝑡
term in Eq. (6) is outdated. Finally, it updates the corresponding
𝑞𝑅 values. In each iteration,𝐹(y) remains non-decreasing and the
quality of the rounded result is guaranteed by the following lemma.
Lemma 4.6. For any 1/𝜖 basic solutions 𝐵1,...,𝐵 1/𝜖 with x =
𝜖· ˝1/𝜖 𝑡 =1 1𝐵𝑡 , AMPRound returns an𝑆∈B satisfying ΛR(𝑆)≥ 𝐹(x).
In the example shown in Figure 1(d), AMPRound takes the basic
solutions𝐵1 ={𝑢1,𝑢 2},𝐵2 ={𝑢2,𝑢 3}, and𝐵3 ={𝑢1,𝑢 3} as inputs.
Initially, AMPRound sets y to 1 3· 1𝐵1+ 1𝐵2+ 1𝐵3  =  2 3, 2 3, 2 3  . In
the first iteration,(𝑢1,𝑢 3) is the only conflicting pair for merging
𝐵1 and𝐵2. AMPRound accepts𝑢3 but removes𝑢1 from𝐵1 based
on their partial derivatives, yielding the merged𝐵1 =𝐵2 ={𝑢2,𝑢 3}.
AMPRound then updates y = y+ 1 3·(13− 11) =  1 3, 2 3, 1  . In the
second iteration,(𝑢2,𝑢 1) is the only conflicting pair for merging (the
Algorithm 4: AMPRound(R,𝜖,QR,𝐵 1,𝐵 2,...,𝐵 1/𝜖)
Input: An RR collectionR, 0 <𝜖≤ 1,QR defined in Algorithm 1,
basic solutions𝐵1,𝐵 2,...,𝐵 1/𝜖
Output: A discrete set𝑆∈B
1 y←𝜖· ˝1/𝜖 𝑙 =1 1𝐵𝑙 ;
2 for𝑡 = 1, 2,..., 1/𝜖− 1 do
3 while𝐵𝑡 ≠𝐵𝑡+1 do
4 𝑢𝑖← an arbitrary element in𝐵𝑡\𝐵𝑡+1;
5 𝑢𝑗← an element in𝐵𝑡+1\𝐵𝑡 s.t.𝐵𝑡\{𝑢𝑖}∪{ 𝑢𝑗}∈B and
𝐵𝑡+1\{𝑢𝑗}∪{ 𝑢𝑖}∈B ;
6 if ˝
𝑅∈R :𝑢𝑖∈𝑅
𝑞𝑅
1−y[𝑖] ≥ ˝ 𝑅∈R :𝑢𝑗∈𝑅 𝑞𝑅 1−y[𝑗] then
7 𝐵𝑡+1←𝐵𝑡+1\{𝑢𝑗}∪{ 𝑢𝑖}; y← y+𝜖 1𝑖− 1𝑗 ;
8 ∀𝑅∈R :𝑢𝑖∈𝑅, 𝑞𝑅←𝑞𝑅· 1−y[𝑖] 1−y[𝑖]+𝜖 ;
9 ∀𝑅∈R :𝑢𝑗∈𝑅, 𝑞𝑅←𝑞𝑅· 1−y[𝑗] 1−y[𝑗]−𝜖 ;
10 else
11 𝐵𝑡←𝐵𝑡\{𝑢𝑖}∪{ 𝑢𝑗}; y← y+𝑡𝜖 1𝑗− 1𝑖 ;
12 ∀𝑅∈R :𝑢𝑗∈𝑅, 𝑞𝑅←𝑞𝑅· 1−y[𝑗] 1−y[𝑗]+𝑡𝜖 ;
13 ∀𝑅∈R :𝑢𝑖∈𝑅, 𝑞𝑅←𝑞𝑅· 1−y[𝑖] 1−y[𝑖]−𝑡𝜖 ;
14 return𝐵1/𝜖 ;
updated)𝐵2 and𝐵3. Following similar operations as in the previous
iteration, the merged𝐵2 =𝐵3 ={𝑢2,𝑢 3} and the fractional result
becomes y = y+ 1 3·(12− 11) =[0, 1, 1]. Hence, the final discrete
result after rounding is𝑆 ={𝑢2,𝑢 3}. □
4.4 Putting It Together
Correctness. Recall in Algorithm 1 that AMP iteratively invokes
AMPSearch or AMPSearch-PM in each iteration𝑡. We denote the
fractional result at the end of iteration𝑡 as x𝑡 =𝜖· ˝𝑡 𝑖=1 1𝐵𝑖 , with
x0← 0. We can then rewrite the improvement of𝐹(x𝑡) compared to
𝐹(x𝑡−1) (see Lemma 4.4) as ΛR(𝑆𝑜)− 𝐹(x𝑡)≤ ΛR(𝑆𝑜)−𝐹(x𝑡−1) 1+𝜖 . By
induction, this leads toΛR(𝑆𝑜)−𝐹(x𝑡)≤ ΛR(𝑆𝑜) (1+𝜖)𝑡 . Upon completion
of 1/𝜖 search iterations, this inequation becomes 𝐹(x1/𝜖)≥ 1−
(1+𝜖)−1/𝜖· ΛR(𝑆𝑜). Given this inequation and Lemma 4.6, the
result𝑆 returned by AMP satisfies the following theorem.
Theorem 4.7. The result𝑆 of the AMP algorithm satisfies
ΛR(𝑆)≥

1− 1
(1+𝜖)
1𝜖

ΛR(𝑆𝑜).
As per Theorem 4.7, by taking as input 𝜖𝑠 = max

𝜖𝑠 : 1 𝜖𝑠 ∈
N, 1−( 1+𝜖𝑠)− 1 𝜖𝑠 ≥ 1− 1 𝑒−𝜖 	 where N ={0, 1, 2,... }, the AMP
algorithm achieves a(1−1/𝑒−𝜖)-approximation for maximizing the
coverage ΛR(𝑆). This input𝜖𝑠 can be obtained by binary search.
Running time for the partition matroid. In each iteration,
AMPSearch-PM computes the partial derivative w.r.t. each𝑢𝑗 from a
given partition𝑈𝑙 , incurring a cost of𝑂
˝
𝑢𝑗∈𝑈𝑙
˝
𝑅∈R I(𝑢𝑗∈𝑅)

.
Upon completion, AMPSearch-PM selects𝑘𝑙 elements from each𝑈𝑙 ,
leading to a total cost of𝑂
˝ℎ
𝑙=1

𝑘𝑙· ˝ 𝑢𝑗∈𝑈𝑙 ˝ 𝑅∈R I(𝑢𝑗∈𝑅)  =
𝑂 𝑘∗· ˝ 𝑅∈R|𝑅|, where𝑘∗ =𝑚𝑎𝑥{𝑘1,𝑘 2,...𝑘 ℎ}. AMPRound op-
erates over 1/𝜖− 1 iterations. In each iteration𝑡, it computes partial

derivatives for every conflicting pair (𝑢𝑖,𝑢𝑗), with𝑢𝑖 ∈ 𝐵𝑡\𝐵𝑡+1
and𝑢𝑗∈𝐵𝑡+1\𝐵𝑡 . Hence, the total running time of AMPRound is
𝑂
˝1/𝜖−1
𝑡 =1
˝
𝑅∈R
˝
𝑢𝑖∈(𝐵𝑡\𝐵𝑡+1)∪(𝐵𝑡+1\𝐵𝑡) I(𝑢𝑖∈𝑅)

, which equals
𝑂 𝜖−1 ˝ 𝑅∈R|𝑅|. As shown in Algorithm 1,AMP runs AMPSearch-
PM for 1/𝜖 iterations and invokes AMPRound once. Therefore, the
running time of AMP subject to the partition matroid is
𝑂

𝑘∗·𝜖−1· ∑︁
𝑅∈R
|𝑅|
!
.
As discussed in § 5.2, ˝ 𝑅∈R|𝑅| is nearly linear to the size of the
graph and seed sets. For instance, ˝ 𝑅∈R|𝑅| =𝑂(𝑘𝜖−2|𝑉| ln|𝑉|) in
vanilla IM, and this running time becomes𝑂 𝑘2𝜖−3|𝑉| ln|𝑉|.
Running time for general matroid. Unlike the partition matroid
case, the general matroid scenario incurs additional cost to con-
firm if𝐵∈I . Specifically, Line 3 of Algorithm 2 checks whether
𝐵∪{𝑢𝑖}∈I given that𝐵∈I , and we assume that this operation
can be finished by an incremental independence call in𝜙𝑖 time. Ad-
ditionally, Line 5 of Algorithm 4 identifies an element𝑢𝑗∈𝐵𝑡+1\𝐵𝑡
satisfying the matroid exchange property for given𝐵𝑡,𝐵𝑡+1∈B .
We assume that each identification can be completed by an ex-
change call in𝜙𝑒 time. Following [31], we implement AMPSearch
(see Algorithm 2) by examining the elements in 𝑈 in decreasing
order of their partial derivatives and selecting the first 𝑢𝑗 with
𝐵∪{𝑢𝑗}∈I . Whenever an element is found to be incompatible,
i.e., adding it breaks independence, we can prune it from the candi-
date list for further iterations. With the above process, AMPSearch
incurs𝑂(𝑛) independence calls across all iterations. Notice that
AMPSearch runs in 𝑟 iterations, and each examines the deriva-
tives of all𝑛 elements. Hence, the time complexity of AMPSearch
is𝑂 𝑛𝜙𝑖+𝑟 ˝ 𝑢𝑖∈𝑈 ˝ 𝑅∈R I(𝑢𝑖∈𝑅) = 𝑂 𝑛𝜙𝑖+𝑟· ˝ 𝑅∈R|𝑅|.
Regarding AMPRound, as|𝐵𝑡+1\𝐵𝑡|≤ 𝑟,𝑂(𝑟) exchange calls are
required for finding a feasible𝑢𝑗 for each of the elements in𝐵𝑡+1\𝐵𝑡 .
Hence, the entire algorithm requires𝑂(𝑟/𝜖) exchange calls. Com-
bining this with the cost analyzed above,AMPRound costs a time of
𝑂 𝜖−1 𝑟𝜙𝑒+ ˝ 𝑅∈R|𝑅| . Therefore, the running time ofAMP sub-
ject to the general matroid is𝑂 𝜖−1 𝑟· ˝ 𝑅∈R|𝑅|+ 𝑛𝜙𝑖+𝑟𝜙𝑒  .
As an example, in the general version of IM for multiple prod-
ucts [18] subject to the laminar matroid constraint, the cost of
each incremental independence call and exchange call is 𝜙𝑖 =
𝑂(log𝑛) and𝜙𝑒 =𝑂(log𝑛) [31]. Here, the running time of AMP is
𝑂 𝜖−1 𝑟 ˝ 𝑅∈R|𝑅|+( 𝑛+𝑟) log𝑛 .
5 RR SET GENERATION SCHEME
Recall in Theorem 4.7 that the proposed AMP offers the desired
approximation guarantee w.r.t. the coverage functionΛR(·). In this
section we present a Rapid version of AMP, called RAMP, which
helps AMP to rapidly determine the required number of RR sets, en-
suring the approximation guarantee for the original objective func-
tion𝜎(·). RAMP follows the state-of-the-art OPIM-C approach [48]
but is generalized to IM-GM. In what follows, we briefly introduce
the RAMP algorithm in § 5.1 and its time complexity in § 5.2.
5.1 RAMP
Main idea. RAMP runs iteratively to mitigate the generation of
excessive RR sets. Initially, it generates two distinct collections of
Algorithm 5: RAMP(G,𝜅, M,𝜖,𝛿)
Input: The graphR, the constant𝜅, the matroid M, an error
tolerance𝜖, a failure probability𝛿
Output: An IM-GM solution𝑆∈I that provides a 1− 1/𝑒−𝜖
approximation w.p. at least 1−𝛿
1 𝜖𝑠← Eq.(7);
2 𝜃𝑚𝑎𝑥← Eq.(8);𝑖𝑚𝑎𝑥← ln𝜅;𝜃1←
l
𝜃𝑚𝑎𝑥
2𝑖max
m
;
3 GenerateR1 andR2 with|R 1| =|R 2| =𝜃1;
4 for𝑖 = 1, 2,...,𝑖 𝑚𝑎𝑥 do
5 𝑆← AMP(R 1, M,𝜖𝑠);
6 Compute𝜎𝑢(S∗) by Eq.(9) onR1 with𝑝𝑓 = 𝛿 3·𝑖𝑚𝑎𝑥 ;
7 Compute𝜎𝑙(S) by Eq.(10) onR2 with𝑝𝑓 = 𝛿 3·𝑖𝑚𝑎𝑥 ;
8 if 𝜎𝑙(𝑆) 𝜎𝑢(𝑆∗) ≥ 1− 1/𝑒−𝜖 or𝑖 =𝑖𝑚𝑎𝑥 then return𝑆;
9 𝜃𝑖+1← 2·𝜃𝑖;
10 Increase the sizes ofR1,R2 such that|R 1| =|R 2| =𝜃𝑖+1;
RR sets, denoted as R1 andR2, each with a size of 𝜃1. At each
iteration𝑖, the element selection algorithm AMP is performed on
R1. Upon selecting a set 𝑆,R2 is leveraged to verify whether 𝑆
satisfies𝜎(𝑆)≥( 1− 1/𝑒−𝜖)· 𝜎(𝑆∗), where𝑆∗ = arg max𝑆∈I𝜎(𝑆).
If it does,𝑆 is returned as the solution. If not, RAMP first increases
the sizes ofR1 andR2 for the next iteration𝑖+ 1 by including new
RR sets, such that each size is equal to𝜃𝑖+1 = 2·𝜃𝑖, and then repeats
the above process. RAMP runs in at most𝑖𝑚𝑎𝑥 iterations, and the
result𝑆 in iteration𝑖𝑚𝑎𝑥 is obtained based onR1 with|R 1| =𝜃𝑚𝑎𝑥 ,
where𝜃𝑚𝑎𝑥 is a carefully-designed constant and ensures that𝑆 still
provide the desired approximation in this worst case.
Detailed implementation. As illustrated in Algorithm 5, RAMP
takes as input a graph G, an IM-GM instance associated with the
matroid M and the constant𝜅, an error tolerance𝜖, and a failure
probability𝛿. Recall in § 2.4 that the constant 𝜅 is the factor to
ensure that ΛR(·) is an unbiased estimator of𝜎(·) for given IM-GM
instance. As shown in Table 2, 𝜅 = |𝑉| in vanilla IM and MRIM,
𝜅 = ˝𝑇 𝑡 =1𝛼𝑡·|𝑉| in RM, and𝜅 =𝜌𝐺(𝐴)−| 𝐴| in AdvIM. Akin to the
input𝜖𝑠 discussed in § 4.4, Line 1 of Algorithm 5 introduces
𝜖𝑠 = max
n
𝜖𝑠 : 1 𝜖𝑠 ∈ N, 1−( 1+𝜖𝑠)− 1 𝜖𝑠 ≥ 1− 1 𝑒− 𝜖 2 o (7)
for the AMP algorithm, such that its result 𝑆 satisfies ΛR1(𝑆)≥
(1− 1/𝑒−𝜖/2)· ΛR1(𝑆𝑜 1), where𝑆𝑜 1 = arg max𝑆∈I ΛR1(𝑆). In Line
2, RAMP initializes three constants: (i) the maximum number𝜃𝑚𝑎𝑥
of required RR sets, (ii) the maximum number of iterations𝑖𝑚𝑎𝑥 , and
(iii) the number of RR sets𝜃1 in the first iteration. To ensure that the
result𝑆 returned in iteration𝑖𝑚𝑎𝑥 achieves𝜎(𝑆)≥ (1− 1/𝑒−𝜖)·
𝜎(𝑆∗) w.p. at least 1−𝛿/3, where𝑆∗ = arg max𝑆∈I𝜎(𝑆), we set
𝜃𝑚𝑎𝑥 to
𝜃𝑚𝑎𝑥 =
8𝜅

(1− 1 𝑒− 𝜖 2) √︃ ln 6 𝛿+ √︃ (1− 1 𝑒− 𝜖 2)( ln|B|+ ln 6 𝛿) 2
𝜖2·𝜎𝑙(𝑆∗) .
(8)
In Eq.(8),𝜎𝑙(𝑆∗) is a lower bound of 𝜎(𝑆∗). For IM, RM, and MRIM,
𝜎𝑙(𝑆∗) can be set as𝑘, max
𝑖≤𝑖≤𝑛
{𝛼𝑖}·|𝑉|, and𝑇𝑘 , respectively. InAdvIM,
𝜎(𝑆∗) can be arbitrarily close to 0 on degenerate instances. Since
we are only interested in problem instances where the influence
reduction is at least 1, i.e.,𝜎(𝑆∗)≥ 1, w.l.o.g. we can set𝜎𝑙(𝑆∗)← 1.

At each iteration𝑖, upon obtainingR1 andR2 with|R 1| =|R 2| =
𝜃𝑖, RAMP employs AMP to select a set𝑆 to maximize the coverage
onR1 (Lines 4-5). To verify whether current𝑆 achieves the desired
approximation ratio (Lines 6-8), RAMP next computes an upper
bound of the optimal solution 𝜎𝑢(𝑆∗), and a lower bound of the
current solution𝜎𝑙(𝑆) by leveragingR1 andR2, respectively. The
intuition behind this verification is that if 𝜎𝑙(𝑆) 𝜎𝑢(𝑆∗) reaches 1− 1/𝑒−𝜖,
then 𝜎(𝑆) 𝜎(𝑆∗)≥ 𝜎𝑙(𝑆) 𝜎𝑢(𝑆∗) also satisfies this approximation. By setting
𝜎𝑢(𝑆∗) =
 √︂
Λ𝑢 R1 (𝑆∗)− ln𝑝𝑓 2 + √︃ − ln𝑝𝑓 2 !2 · 𝜅 |R 1|, and (9)
𝜎𝑙(𝑆) =
 √︃
ΛR2(𝑆)− 2 ln𝑝𝑓 9 − √︃ − ln𝑝𝑓 2 2 + ln𝑝𝑓 18 ! · 𝜅 |R 2| (10)
with𝑝𝑓 = 𝛿 3·𝑖𝑚𝑎𝑥 , we can obtain that𝜎𝑢(𝑆∗) is an upper bound of
𝜎(𝑆∗) w.p. at least1− 𝛿 3·𝑖𝑚𝑎𝑥 and𝜎𝑙(𝑆) is a lower bound of𝜎(𝑆) w.p.
at least 1− 𝛿 3·𝑖𝑚𝑎𝑥 . In Eq.(9), Λ𝑢 R1 (𝑆∗) is an upper bound of ΛR1(𝑆∗),
which can be set to ΛR1(𝑆) 1− 1 𝑒−𝜖 2 . To tighten Λ𝑢 R1 (𝑆∗), we follow the idea
of [48] that computes it based on the current fractional solution
x during the iterations of AMP. See Appendix C for a detailed
explanation.
To summarize, based on the above settings of𝜃𝑚𝑎𝑥 ,𝜎𝑢(𝑆∗), and
𝜎𝑙(𝑆), by the union bound, the correctness of RAMP follows.
Theorem 5.1. Given a graph G, an IM-GM instance associated with
the matroid M and the constant𝜅, an error tolerance 𝜖, and a failure
probability𝛿, RAMP returns a set𝑆 satisfying𝜎(𝑆)≥( 1− 1/𝑒−𝜖)·
𝜎(𝑆∗) with probability at least 1−𝛿, where𝑆∗ = arg max
𝑆∈I
𝜎(𝑆).
5.2 Time Complexity Analysis
Denote the expected time of generating an RR set as𝐸𝑃𝑇 , and the ex-
pected size of an RR set as𝐸𝑃𝑆 . In each iteration𝑖, the computational
overhead of RAMP comes from (i) generating RR sets in𝑂(E[𝜃𝑖·
𝐸𝑃𝑇]), and (ii) an invocation of AMP in𝑂 𝑘∗·𝜖−1𝑠 · ˝ 𝑅∈R 1|𝑅| =
𝑂 𝑘∗·𝜖−1𝑠 · E[𝜃𝑖·𝐸𝑃𝑆] for the partition matroid, as analyzed in
§ 4.4. Let𝑖′ be the iteration where RAMP stops. As proved in [50],
E[𝜃𝑖′· 𝐸𝑃𝑇] = E[𝜃𝑖′]· 𝐸𝑃𝑇 and E[𝜃𝑖′· 𝐸𝑃𝑆] = E[𝜃𝑖′]· 𝐸𝑃𝑆 .
Thus, the time complexity of RAMP for the partition matroid
is𝑂

E
h˝𝑖′
𝑖=1𝜃𝑖
i 
𝐸𝑃𝑇+ 𝑘∗ 𝜖𝑠·𝐸𝑃𝑆  , where𝑘∗ = max{𝑘1,...𝑘 ℎ},
and E
h˝𝑖′
𝑖=1𝜃𝑖
i
is bounded as follows.
Lemma 5.2. When𝛿≤ 1/2, RAMP totally generates𝑂(( ln|B|+
ln(1/𝛿))𝜅𝜖−2/𝜎(𝑆∗)) RR sets in expectation.
Given this lemma and𝜖𝑠 =𝑂(𝜖), when𝛿≤ 1/2, the expected
time complexity of RAMP subject to the partition matroid is
𝑂
(ln|B|+ ln(1/𝛿))𝜅𝜖−2
𝜎(𝑆∗) · 𝐸𝑃𝑇+𝜖−1·𝑘∗·𝐸𝑃𝑆  .
Akin to the above analysis, when𝛿≤ 1/2, the time complexity of
RAMP for the general matroid is
𝑂

(ln|B|+ ln(1/𝛿))𝜅𝜖−2
𝜎(𝑆∗) · 𝐸𝑃𝑇+𝜖−1𝑟·𝐸𝑃𝑆 + (𝑟·𝜙𝑒+𝑛·𝜙𝑖)·ln𝜅 𝜖

.
Table 2:𝜅,𝐸𝑃𝑇 , and𝐸𝑃𝑆 in instances (𝜌∗ = max
𝑣𝑖∈𝑉
𝜌G({𝑣𝑖})).
Name 𝜅 𝐸𝑃𝑇 𝐸𝑃𝑆
Vanilla IM |𝑉| 𝑂

|𝐸|
|𝑉|𝜌∗

𝑂(𝜌∗)
RM ˝𝑇 𝑡 =1𝛼𝑡·|𝑉| 𝑂  |𝐸| |𝑉|𝜌∗  𝑂(𝜌∗)
MRIM |𝑉| 𝑂

𝑇·|𝐸|
|𝑉| 𝜌∗

𝑂(𝑇·𝜌∗)
AdvIM 𝜌𝐺(𝐴)−| 𝐴| 𝑂

|𝑉\𝐴|
𝜌G(𝐴)−|𝐴|· |𝐸| |𝑉|𝜌∗

𝑂(𝜌∗)
Table 3: Dataset statistics (𝐾 = 103,𝑀 = 106,𝐵 = 109).
Name #nodes #edges Type Avg. degree
Facebook 4.0𝐾 176.4𝐾 friendship 43.6
Wiki 7.1𝐾 103.6𝐾 who-votes-on-whom 14.5
Twitter 81.3𝐾 1.7𝑀 who-follows-whom 21.7
Google+ 107.6𝐾 13.7𝑀 who-follows-whom 283.3
Pokec 1.6𝑀 30.6𝑀 friendship 18.7
LiveJournal 4.8𝑀 69.0𝑀 friendship 14.2
Twitter-large 41.7𝑀 1.5𝐵 who-follows-whom 35.2
For IM, [50] shows that𝐸𝑃𝑇 =𝑂
|𝐸|
|𝑉|𝜌∗

and𝐸𝑃𝑆 =𝑂(𝜌∗) under
IC and LT models, where𝜌∗ = max𝑣𝑖∈𝑉 𝜌G({𝑣𝑖}). Besides IM, the
original works of RM, MRIM, and AdvIM [30, 46, 47] also provide
analyses for𝐸𝑃𝑇 and𝐸𝑃𝑆 , which are summarized in Table 2. Since
they are related to𝜌∗ and𝜌∗≤𝜎(𝑆∗), the above complexities can be
further simplified. E.g., for MRIM with𝜅 =|𝑉| and|B| = |𝑉| 𝑘 𝑇 , the
time complexity is𝑂 𝑇 2𝑘𝜖−2 𝑡 (ln|𝑉|+ ln(1/𝛿))·(| 𝐸|+ 𝑘𝜖−1|𝑉|).
6 EXPERIMENTS
We first introduce the experimental settings in § 6.1, and then evalu-
ate the performance of our proposal in § 6.2. All experiments are con-
ducted on a Linux machine with Intel Xeon(R) Gold 6240@2.60GHz
CPU and 377GB RAM in single-thread mode.
6.1 Experimental Setup
Datasets. We experiment with 7 real-world datasets that are widely
adopted in previous works and publicly available at SNAP [38]: Face-
book [5, 39, 58], Wiki [39], Twitter [5], Google+ [58], Pokec [48],
LiveJournal [48, 58], and Twitter-large [48]. The Twitter-large dataset
is the largest dataset ever used in instances RM, MRIM, and AdvIM.
The dataset statistics are listed in Table 3.
IM-GM instances and configurations. We focus on the instances
IM, RM, MRIM, and AdvIM, as illustrated in § 2.2-2.3. Following the
default configurations in related works [ 28, 30, 46, 47], we use
the IC model in RM, MRIM, IM and the LT model in AdvIM. We set
𝑝𝑖,𝑗 = 1/|𝑁𝑖𝑛 𝑗 | for all𝑒𝑖,𝑗 ∈ 𝐸. We configure𝑇 = 10,𝛼𝑖 = 1,𝑘𝑗 = 1
for all 𝑖∈ [𝑇],𝑣𝑗 ∈ 𝑉 for RM, set𝑇 = 20,𝑘 = 100 for MRIM, and
𝑘 = 2000 for IM. In the absence of a ground-truth set𝐴 for AdvIM,
where|𝐴| represents the number of contagious seeds as detected by
the authority, we generate a synthetic set𝐴. This is accomplished
by initially adding the node𝑣𝑖 with the largest out-degree to set𝐴.
Following this, each out-neighbor𝑣𝑗 of𝑣𝑖 is independently added
to𝐴 with a probability of𝑝𝑖,𝑗 . Furthermore, we set𝑘𝑣 = 500 and
𝑘𝑒 = 1000, which are comparable in magnitude to|𝐴|.

AMP,𝜖 = 1 2 AMP,𝜖 = 1 8 AMP-PM,𝜖 = 1 2 AMP-PM,𝜖 = 1 8 Greedy Local-Greedy Threshold-Greedy
25 29 213 217 221
4
8
16
#RR sets
total revenue (×103)
(a) Facebook
25 29 213 217 221
6
12
#RR sets
total revenue (×103)
(b) Wiki
25 29 213 217 221
1
2
4
#RR sets
total revenue (×105)
(c) Twitter
25 29 213 217 221
1
2
4
#RR sets
total revenue (×105)
(d) Google+
25 29 213 217 221
1.5
3
6
#RR sets
total revenue (×106)
(e) Pokec
25 29 213 217 221
4
8
16
#RR sets
total revenue (×106)
(f) LiveJournal
25 29 213 217 221
4
8
16
#RR sets
total revenue (×107)
(g) Twitter-large
Figure 2: Total revenue in RM on various graphs.
21 25 29 213 217
.5
1
2
4
#RR sets
total spread (×102)
(a) Facebook
21 25 29 213 217
1
4
16
64
#RR sets
total spread (×102)
(b) Wiki
21 25 29 213 217
1
2
4
8
#RR sets
total spread (×104)
(c) Twitter
21 25 29 213 217
.6
1.2
#RR sets
total spread (×105)
(d) Google+
21 25 29 213 217
1
10
#RR sets
total spread (×105)
(e) Pokec
21 25 29 213 217
1
10
#RR sets
total spread (×105)
(f) LiveJournal
21 25 29 213 217
8
16
32
#RR sets
total spread (×106)
(g) Twitter-large
Figure 3: Total spread in MRIM on various graphs.
21 25 29 213 217
1
2
4
8
#RR sets
reduction (×102)
(a) Facebook
21 25 29 213 217
8
16
32
64
#RR sets
reduction
(b) Wiki
21 25 29 213 217
.5
1
2
4
#RR sets
reduction (×102)
(c) Twitter
21 25 29 213 217
4
8
#RR sets
reduction (×103)
(d) Google+
21 25 29 213 217
1
10
#RR sets
reduction (×103)
(e) Pokec
21 25 29 213 217
1
5
25
#RR sets
reduction (×103)
(f) LiveJournal
21 25 29 213 217
1
5
25
#RR sets
reduction (×105)
(g) Twitter-large
Figure 4: Influence reduction in AdvIM on various graphs.
Algorithms and constant settings. We evaluate the performance
of 9 algorithms in total, which are divided into two parts: 5 algo-
rithms for element selection, and 4 algorithms for their scalable
implementation. These algorithms are as follows.
• Element selection: Greedy, Local-Greedy, and Threshold-Greedy
(baselines in § 2.4); AMP and AMP-PM for the general matroid
and partition matroid, respectively (Algorithm 1).
• Scalable solutions: RM-A for RM [30], CR-NAIMM for MRIM [46],
and AAIMM for AdvIM [47] (baselines); RAMP (Algorithm 5).
For all element selection algorithms, we apply the lazy evaluation
technique in [37, 42] to improve their empirical efficiency. ForAMP
and AMP-PM,𝜖 is set to 1/2 and 1/8. Based on Theorem 4.7, these
settings provide an approximation of 0.56 and 0.61 for maximizing
ΛR, respectively, indicating a focus on efficiency but at the cost
of result quality, and vice versa. For Threshold-Greedy,𝜉 is set to
the default value 0.05 [6]. For all scalable implementations, we set
𝛿 = 1/|𝑉| by default and vary𝜖 from 0.5 to 0.1 [48, 50]. For a fair
comparison, we have also made other necessary modifications to
scalable competitors and refer interested readers to Appendix D for
details. In addition, for each algorithm, we estimate the objective
function value𝜎 by averaging over 10, 000 Monte Carlo simulations.
We repeat each algorithm 5 times and report the average when
evaluating the running time and the objective function value. All
algorithms are implemented in C++ with -O3 optimization.
6.2 Performance Evaluations
Performance of element selection inRM, MRIM, and AdvIM. In the
first set of experiments, we evaluate the result quality and running
time of element selection algorithms on the IM-GM instances RM,
MRIM, and AdvIM. For a fair comparison, we provide all algorithms
with the same collection of RR setsR. Furthermore, we vary|R|
from 25 to 221 in RM; and from 21 to 217 in MRIM and AdvIM. The
choices of the smallest and largest values for|R| roughly correspond
to𝜃1 and𝜃𝑚𝑎𝑥 in Algorithm 5 when𝜖 = 0.1.
Result quality. As shown in Figures 2-4, both AMP and AMP-PM
return better solutions compared to their competitors in terms of
related objective functions across all datasets. For instance, AMP or
AMP-PM outperforms all competitors by up to 86% on Pokec in RM,
708% on Wiki in MRIM, and 205.8% on Twitter-large in AdvIM. To
explain, AMPSearch and AMPSearch-PM select each element based
on the largest partial derivative and subsequently update the value
of𝑞𝑅 for each𝑅 containing the selected element. In contrast to the
competitors Greedy, Local-Greedy, and Threshold-Greedy, our up-
date strategy circumvents the direct exclusion of each related𝑅 and
offers a more fine-grained marginal coverage for each element. As
a result, it allows for a more refined and potentially more effective
selection process. Furthermore, we observe that the result quality
of Threshold-Greedy is much worse than other approaches when
the number of RR sets is small. This is because it disregards all ele-
ments whose marginal coverage is below the minimum threshold,
rendering the number of selected elements fewer than expected.

AMP,𝜖 = 1/2 AMP,𝜖 = 1/8 AMP-PM,𝜖 = 1/2 AMP-PM,𝜖 = 1/8
Greedy Local-Greedy Threshold-Greedy RR set generation
25 29 213 217 221
0.1
101
103
#RR sets
running time (s)
(a) Facebook
25 29 213 217 2210.01
100
102
#RR sets
running time (s)
(b) Wiki
25 29 213 217 2210.1
101
103
#RR sets
running time (s)
(c) Twitter
25 29 213 217 2210.1
101
103
105
#RR sets
running time (s)
(d) Google+
25 29 213 217 221100
101
102
103
#RR sets
running time (s)
(e) Pokec
25 29 213 217 221
101
102
103
#RR sets
running time (s)
(f) LiveJournal
25 29 213 217 221
102
103
104
105
#RR sets
running time (s)
(g) Twitter-large
Figure 5: Running time of element selection in RM.
AMP,𝜖 = 1 2 AMP,𝜖 = 1 8 Greedy Threshold-Greedy
21 25 29 213 217
2
4
#RR sets
spread (×103)
(a) Facebook
21 25 29 213 217
2
4
#RR sets
spread (×103)
(b) Wiki
21 25 29 213 217
2
4
#RR sets
spread (×104)
(c) Twitter
21 25 29 213 217
3
6
#RR sets
spread (×104)
(d) Google+
21 25 29 213 217
4
8
16
#RR sets
spread (×104)
(e) Pokec
21 25 29 213 217
.3
3
30
#RR sets
spread (×104)
(f) LiveJournal
21 25 29 213 217
2
4
8
16
#RR sets
spread (×106)
(g) Twitter-large
Figure 6: The spread in IM on various graphs.
RAMP RM-A CR-NAIMM AAIMM
0 0.2 0.4 0.6102
103
104
105
approx. guarantee
running time (s)
(a) RM (Twitter-large)
0 0.2 0.4 0.6100
102
104
approx. guarantee
running time (s)
(b) MRIM (Wiki)
0 0.2 0.4 0.6100
102
104
approx. guarantee
running time (s)
(c) AdvIM (Wiki)
Figure 7: Total running time of scalable algorithms.
Running time. In the second set of experiments, we use RM as the in-
stance and report the running times of element selection algorithms
in Figure 5. Similar trends were observed in the running time results
for other instances. Specifically, Local-Greedy and AMP-PM (with
𝜖 = 1/2) are the fastest and second-fastest algorithms respectively,
across all datasets, each being 4− 10× faster than Greedy. Recall
from the first set of experiments that Local-Greedy, despite being
the fastest, is the second least effective algorithm, quality wise. Fur-
thermore, we compare AMP and AMP-PM with the same𝜖 values
across these problems using partition matroids. In particular, AMP-
PM improves the running time by an order of magnitude. These
observations demonstrate the efficiency of AMP-PM, as proved in
§ 4.4. Note that, in Figure 5(e), the running time of AMP decreases
when|R| ≥ 215, due to the lazy evaluation technique. We also
report the time taken to generateR. RR set generation becomes
more expensive than all methods as the size of R increases. For
instance, when|R| > 29 on Google+, the time taken to generateR
exceeds that of AMP-PM by more than an order of magnitude. This
motivates the design of an efficient scheme for RR set generation,
as proposed in § 5.
Performance of element selection in IM. In the third set of ex-
periments, we evaluate the performance of the proposed element
selection methods on the conventional IM problem. Here, we only
compare AMP with Greedy and Threshold-Greedy as AMP and
AMP-PM (resp. Greedy and Local-Greedy) are essentially equiva-
lent. Figure 6 reports the spread of each method on different datasets
as|R| is varied from 21 to 217. Notably, AMP outperforms competi-
tors by up to 871% on LiveJournal. This is attributed to the more
fine-grained marginal coverage, as discussed earlier.
Effect of 𝜖 in AMP. Next, we examine the impact of the 𝜖 pa-
rameter in the proposed AMP algorithm. Here, we focus on the
result qualities of AMP and Greedy, as shown in Figures 2-6. Note
that AMP is equivalent to Greedy when𝜖 = 1. Based on observa-
tions in the first and third sets of experiments, the result quality
of AMP improves significantly by decreasing𝜖 from 1 to 1/2 (i.e.,
increasing the number of iterations in Line 4 of Algorithm 1 from
1 to 2). This improvement becomes less pronounced with further
increases in the number of iterations. For example, in MRIM, the
solution quality of AMP improves by 84% on Pokec when|R| = 29
as𝜖 decreases from 1 to 1/2. In contrast, the improvement is only
7% when comparing𝜖 = 1/2 with𝜖 = 1/8.
Performance of scalable implementations. Finally, we evaluate
the running times of RAMP and all scalable competitors by vary-
ing𝜖 from 0.5 to 0.1. In Figure 7, the approximation ratio of each
solution is used as the x-axis, with RAMP having 1− 1/𝑒−𝜖 and all
competitors having 1/2−𝜖; in Figure 7(a), we exclude approaches
that run more than 72 hours. Due to space constraints, we only re-
port results for the largest dataset on which the baseline algorithm
with𝜖 = 0.5 can terminate within 72 hours. These datasets are
Twitter-large in RM and Wiki in MRIM and AdvIM. Interested readers
can find more experimental results, including the memory usage of
scalable algorithms, in Appendix E.
Specifically, RAMP consistently outperforms the baseline regard-
ing running time while ensuring the same approximation guarantee
across all cases. Notably, RAMP is at least 1, 000× faster than CR-
NAIMM in MRIM and at least 100× faster than AAIMM in AdvIM.
In addition, RAMP completes within 66 hours for RM on Twitter-
large when𝜖 = 0.3, whereas RM-A only returns results for𝜖≥ 0.4

and fails to terminate even after 7 days when 𝜖 = 0.3. The rea-
son for the efficiency of RAMP is twofold. First, RAMP introduces
the early termination and the tightened bound Λ𝑢 R1 (𝑆∗), which allows us to generate an appropriate number of RR sets as soon as a
(1− 1/𝑒−𝜖)-approximation is reached. Furthermore,AMP provides
superior result qualities during iterations, enabling RAMP to reach
the desired approximation faster. In contrast, RM-A, CR-NAIMM,
and AAIMM generate a large number of RR sets and rely onGreedy
or Local-Greedy for element selection, leading to inferior result
qualities. To summarize, the proposed RAMP is significantly faster
than all competitors while providing the same result quality.
7 DEPLOYMENT
We have deployed our proposed RAMP in a real industry setting
for GameX of Tencent. The details are described below.
Application scenario. GameX is a Tencent multiplayer online
game with hundreds of millions of users and a massive number
of user-generated maps. A map in the game is a vibrant and dy-
namic environment featuring several obstacles and puzzle-solving
settings, allowing multiple users to compete with each other simul-
taneously. Besides, the social network in GameX can be constructed
based on friendships formed in the game, with an average of∼16
friends per user, making it sufficiently dense [3]. As such, users can
interact with their friends on the social network, such as playing
or inviting to play the game in some maps, which contributes to
cascades of maps in the game. In other words, a user might play the
game in a map if their friends have played or shared it. To further
promote the maps, the game environment can generate 𝑘 maps
as recommendations for each user, who can receive them during
the game and click the maps they are interested in playing in. The
performance of GameX is measured by the number of engaged user-
map pairs, each of which denotes that a user plays a user-generated
map, reflecting the engagement of users in the game.
Control and treatment groups. We have deployed three ap-
proaches: (i) Most-Click, (ii) RM-A, and (iii) RAMP. Specifically, for
the control group, we have deployed Most-Click, the state-of-the-
art solution for this scenario. It operates by first ranking maps for
each user𝑣𝑖 based on the descending order of probability𝑤𝑖,𝑡 that
𝑣𝑖 will click map𝑡 and then selecting the top-𝑘 maps with the high-
est click probabilities for each user. We learn the probability𝑤𝑖,𝑡
using XGBoost [15], a machine learning model to predict whether
a given user would play the game in a given map.
We have deployed RM-A and RAMP for two different treatment
groups. For treatment groups, we focus on addressing the RM prob-
lem and returning𝑘 user-map pairs for each user. Notably, we set
each unit revenue to 1 and employ the IC model as the diffusion
model. In this model, the influence probability𝑝𝑖,𝑗 for each𝑒𝑖,𝑗 ∈𝐸
is calculated as 𝑐𝑖,𝑗˝
𝑣𝑖∈𝑁𝑖𝑛 𝑗 𝑐𝑖,𝑗 , where𝑐𝑖,𝑗 denotes the number of histor-
ical interactions on𝑒𝑖,𝑗 , such as co-playing, gifting, etc. To address
RM in this context, we first leverage the competing solution RM-
A [30], as mentioned in § 6, the core of which is selecting𝑘 seeds for
each map using Greedy. Next, we implement the proposed RAMP
by targeting an enhanced objective function𝜎𝑊(𝑆) based on𝜎(𝑆).
Table 4: Numbers of engaged pairs in GameX ( 𝑀 = 106).
Algorithm Most-Click RM-A RAMP
#engaged pairs 7.34M 7.36M 7.50M
This function is defined as
𝜎𝑊(𝑆) = ∑︁
𝑆′⊆𝑆
Ö
(𝑣𝑖,𝑡)∈𝑆′
𝑤𝑖,𝑡
Ö
(𝑣𝑖,𝑡)∈𝑆\𝑆′
(1−𝑤𝑖,𝑡)· 𝜎(𝑆′),
where𝑊 is a given (or learned) set of click probabilities that con-
tains𝑤𝑖,𝑡 for every user-map pair(𝑣𝑖,𝑡). By adjusting the scale of
𝑞𝑅 in AMP, RAMP can be adapted to this new objective while main-
taining the same approximation guarantee and time complexity.
For further details, readers are referred to Appendix F.
Deployment setups. This deployment is conducted on an in-house
cluster in Tencent consisting of hundreds of machines, each of
which has 16GB memory and 12 Intel Xeon Processor E5-2670 CPU
cores. To mitigate the network effect, the phenomenon whereby
user behaviors are influenced by others within the same network,
we follow [44] and conduct cluster-level experimentation. Specifi-
cally, we first partition all users into several communities of almost
the same size with high edge connectivity and node feature similar-
ity, and then randomly assign the live traffic in the same community
to the treatment or control groups. Furthermore, we set the number
of recommended maps𝑘 to 2. As a result, each approach is assigned
to 0.7 million sampled users with 400 randomly selected maps to
recommend, leading to 277.5 million user-map pairs for observation.
In this scenario, the constraint is a partition matroid M =(𝑈,I),
where𝑈 comprises all pairs of users and maps (277.5 million) and
I consists of all solutions, each containing𝑘 = 2 maps per user.
Online performance. Table 4 reports the number of engaged pairs
for each algorithm. Notably, the treatment groups achieve more
engaged pairs compared to the control group Most-Click – 20,000
(0.27%) for RM-A and 160,000 (2.17%) for RAMP, demonstrating the
usefulness of involving the word-of-mouth effect in this scenario.
In addition, RAMP yields 140,000 (1.9%) more engaged pairs than
RM-A. To explain, unlike Most-Click which solely focuses on the
probability of a seed adopting the promoted map, RAMP takes into
account not only this inclination but also the subsequent word-
of-mouth effect, as captured by the IC model with its associated
influence probability. The improvement of RAMP over RM-A can
be attributed to two factors. First, RAMP achieves a(1− 1/𝑒−𝜖)-
approximation, while the result of RM-A is(1/2−𝜖)-approximate.
Second, the enhanced objective𝜎𝑊(𝑆) comprehensively considers
the adoption inclination of any subset of𝑆. In contrast, even if the
revenue unit𝛼𝑡 is leveraged, RM-A can only involve the average
inclination for each map𝑡. While the percentage improvement may
appear modest, the improved numbers of engaged pairs lead to
substantial additional revenue for the industry.
8 CONCLUSIONS
In this paper, we focus on applications requiring multiple seed sets
for IM, which are formulated as instances of IM subject to a matroid
constraint. For effectiveness, we propose AMP, which achieves a
(1− 1/𝑒−𝜖)-approximation guarantee for this problem. For en-
hanced efficiency, we also propose a fast implementation called

RAMP. Our comprehensive experiments demonstrate that our pro-
posal outperforms state-of-the-art methods in both effectiveness
and efficiency. Moreover, we have successfully deployed RAMP in
an online gaming propagation scenario in a real industry setting,
yielding considerable improvements. In the future, to exploit the
infrastructure in the industry further, we will consider solutions in
the distributed setting. It is also interesting to explore real-world
applications of IM under other types of matroid constraints and
develop scalable and effective solutions for them.
REFERENCES
[1] Alexander A Ageev and Maxim I Sviridenko. 2004. Pipage rounding: A new
method of constructing algorithms with proven performance guarantee. Journal
of Combinatorial Optimization 8 (2004), 307–328.
[2] Cigdem Aslay, Francesco Bonchi, Laks VS Lakshmanan, and Wei Lu. 2017. Rev-
enue maximization in incentivized social advertising. Proc. VLDB Endowment 10,
11 (2017), 1238–1249.
[3] Lars Backstrom, Paolo Boldi, Marco Rosa, Johan Ugander, and Sebastiano Vigna.
2012. Four degrees of separation. In Web Science. 33–42.
[4] Ashwinkumar Badanidiyuru and Jan Vondrák. 2014. Fast algorithms for maxi-
mizing submodular functions. In SODA. 1497–1514.
[5] Ruben Becker, Gianlorenzo d’Angelo, and Hugo Gilbert. 2021. Influence Maxi-
mization With Co-Existing Seeds. In CIKM. 100–109.
[6] Song Bian, Qintian Guo, Sibo Wang, and Jeffrey Xu Yu. 2020. Efficient algorithms
for budgeted influence maximization on massive social networks. Proc. VLDB
Endowment 13, 9 (2020), 1498–1510.
[7] Christian Borgs, Michael Brautbar, Jennifer Chayes, and Brendan Lucier. 2014.
Maximizing social influence in nearly optimal time. In SODA. 946–957.
[8] Richard A Brualdi. 1969. Comments on bases in dependence structures. Bulletin
of the Australian Mathematical Society 1, 2 (1969), 161–167.
[9] Niv Buchbinder, Moran Feldman, and Roy Schwartz. 2017. Comparing apples
and oranges: Query trade-off in submodular maximization. Mathematics of
Operations Research 42, 2 (2017), 308–329.
[10] Ceren Budak, Divyakant Agrawal, and Amr El Abbadi. 2011. Limiting the spread
of misinformation in social networks. In WWW. 665–674.
[11] ByteDance. 2023. Recruitment-based Campaign in the Document of Douyin
Xingtu Platform. https://www.xingtu.cn/help-center/demander/126583.
[12] Gruia Calinescu, Chandra Chekuri, Martin Pal, and Jan Vondrák. 2011. Maximiz-
ing a monotone submodular function subject to a matroid constraint. SIAM J.
Comput. 40, 6 (2011), 1740–1766.
[13] T-H Hubert Chan, Li Ning, and Yong Zhang. 2020. Influence maximization
under the non-progressive linear threshold model. In International Workshop on
Frontiers in Algorithmics. 37–48.
[14] Chandra Chekuri, Jan Vondrák, and Rico Zenklusen. 2010. Dependent random-
ized rounding via exchange properties of combinatorial structures. In FOCS.
575–584.
[15] Tianqi Chen and Carlos Guestrin. 2016. XGBoost: A Scalable Tree Boosting
System. In SIGKDD. 785–794.
[16] Wei Chen, Ruihan Wu, and Zheng Yu. 2020. Scalable lattice influence maximiza-
tion. IEEE Transactions on Computational Social Systems 7, 4 (2020), 956–970.
[17] Pedro Domingos and Matt Richardson. 2001. Mining the network value of
customers. In SIGKDD. 57–66.
[18] Nan Du, Yingyu Liang, Maria-Florina Balcan, Manuel Gomez-Rodriguez,
Hongyuan Zha, and Le Song. 2017. Scalable Influence Maximization for Multiple
Products in Continuous-Time Diffusion Networks. J. Mach. Learn. Res. 18, 2
(2017), 1–45.
[19] Jack Edmonds. 1971. Matroids and the Greedy Algorithm. Math. Program. 1, 1
(1971), 127–136.
[20] Marwa El Halabi, Slobodan Mitrović, Ashkan Norouzi-Fard, Jakab Tardos, and
Jakub M Tarnawski. 2020. Fairness in Streaming Submodular Maximization:
Algorithms and Hardness. In NeurIPS. 13609–13622.
[21] Alina Ene and Huy L. Nguyen. 2019. Towards Nearly-Linear Time Algorithms
for Submodular Maximization with a Matroid Constraint. In ICALP. 54:1–54:14.
[22] Ocean Engine. 2022. ByteDance Xingtu Creator Ecosystem Report. https://
trendinsight.oceanengine.com/arithmetic-report/detail/773.
[23] Ocean Engine. 2023. China Influencer Marketing with Douyin and
Xingtu. https://www.oceanengine.io/resource/china-influencer-marketing-
douyin-xingtu-tips-strategies.
[24] Pihu Feng, Xin Lu, Zaiwu Gong, and Duoyong Sun. 2021. A case study of
the pyramid scheme in China based on communication network. Physica A:
Statistical Mechanics and its Applications 565 (2021), 125548.
[25] Marshall L Fisher, George L Nemhauser, and Laurence A Wolsey. 1978. An
analysis of approximations for maximizing submodular set functions—II. In
Polyhedral combinatorics. 73–87.
[26] Jacob Goldenberg, Barak Libai, and Eitan Muller. 2001. Talk of the network: A
complex systems look at the underlying process of word-of-mouth. Marketing
letters 12, 3 (2001), 211–223.
[27] Mark Granovetter. 1978. Threshold models of collective behavior. American
journal of sociology 83, 6 (1978), 1420–1443.
[28] Qintian Guo, Sibo Wang, Zhewei Wei, and Ming Chen. 2020. Influence maximiza-
tion revisited: Efficient reverse reachable set generation with bound tightened.
In SIGMOD. 2167–2181.
[29] Qintian Guo, Sibo Wang, Zhewei Wei, Wenqing Lin, and Jing Tang. 2022. Influ-
ence Maximization Revisited: Efficient Sampling with Bound Tightened. ACM
Transactions on Database Systems 47, 3 (2022).
[30] Kai Han, Benwei Wu, Jing Tang, Shuang Cui, Cigdem Aslay, and Laks VS Lak-
shmanan. 2021. Efficient and effective algorithms for revenue maximization in
social advertising. In SIGMOD. 671–684.
[31] Monika Henzinger, Paul Liu, Jan Vondrák, and Da Wei Zheng. 2023. Faster
Submodular Maximization for Several Classes of Matroids. InICALP. 74:1–74:18.
[32] Influencer Marketing Hub. 2024. Top Influencer Marketing Platforms for April
2024. https://influencermarketinghub.com/influencer-marketing-platforms.
[33] Instagram. 2022. Introducing Creator Marketplace, Where Brands Can Dis-
cover Creators to Collaborate With. https://business.instagram.com/blog/creator-
marketplace-discover-partnerships.
[34] Emilia A Isolauri and Irfan Ameer. 2023. Money laundering as a transnational
business phenomenon: a systematic review and future agenda. Critical Perspec-
tives on International Business 19, 3 (2023), 426–468.
[35] Raghuram Iyengar, Christophe Van den Bulte, and Thomas W Valente. 2011.
Opinion leadership and social contagion in new product diffusion. Marketing
science 30, 2 (2011), 195–212.
[36] David Kempe, Jon Kleinberg, and Éva Tardos. 2003. Maximizing the spread of
influence through a social network. In SIGKDD. 137–146.
[37] Jure Leskovec, Andreas Krause, Carlos Guestrin, Christos Faloutsos, Jeanne
VanBriesen, and Natalie Glance. 2007. Cost-effective outbreak detection in
networks. In SIGKDD. 420–429.
[38] Jure Leskovec and Andrej Krevl. 2014. SNAP Datasets: Stanford Large Network
Dataset Collection. http://snap.stanford.edu/data.
[39] Weihua Li, Quan Bai, Minjie Zhang, and Tung Doan Nguyen. 2018. Automated
influence maintenance in social networks: an agent-based approach. IEEE Trans-
actions on Knowledge and Data Engineering 31, 10 (2018), 1884–1897.
[40] Yuchen Li, Ju Fan, Yanhao Wang, and Kian-Lee Tan. 2018. Influence maximization
on social graphs: A survey.IEEE Transactions on Knowledge and Data Engineering
30, 10 (2018), 1852–1872.
[41] Hao Liao, Sheng Bi, Jiao Wu, Wei Zhang, Mingyang Zhou, Rui Mao, and Wei
Chen. 2023. Popularity Ratio Maximization: Surpassing Competitors through
Influence Propagation. Proc. ACM Manag. Data 1, 2 (2023).
[42] Michel Minoux. 1978. Accelerated greedy algorithms for maximizing submodular
set functions. Optimization Techniques (1978), 234–243.
[43] Hung T Nguyen, My T Thai, and Thang N Dinh. 2016. Stop-and-stare: Optimal
sampling algorithms for viral marketing in billion-scale networks. In SIGMOD.
695–710.
[44] Martin Saveski, Jean Pouget-Abadie, Guillaume Saint-Jacques, Weitao Duan,
Souvik Ghosh, Ya Xu, and Edoardo M Airoldi. 2017. Detecting network effects:
Randomizing over randomized experiments. In SIGKDD. 1027–1035.
[45] Michael Simpson, Farnoosh Hashemi, and Laks VS Lakshmanan. 2022. Misinfor-
mation mitigation under differential propagation rates and temporal penalties.
Proc. VLDB Endowment 15, 10 (2022), 2216–2229.
[46] Lichao Sun, Weiran Huang, Philip S Yu, and Wei Chen. 2018. Multi-round
influence maximization. In SIGKDD. 2249–2258.
[47] Lichao Sun, Xiaobin Rui, and Wei Chen. 2023. Scalable Adversarial Attack
Algorithms on Influence Maximization. In WSDM. 760–768.
[48] Jing Tang, Xueyan Tang, Xiaokui Xiao, and Junsong Yuan. 2018. Online process-
ing algorithms for influence maximization. In SIGMOD. 991–1005.
[49] Shaojie Tang. 2018. When social advertising meets viral marketing: Sequencing
social advertisements for influence maximization. In AAAI, Vol. 32.
[50] Youze Tang, Yanchen Shi, and Xiaokui Xiao. 2015. Influence maximization in
near-linear time: A martingale approach. In SIGMOD. 1539–1554.
[51] Youze Tang, Xiaokui Xiao, and Yanchen Shi. 2014. Influence maximization:
Near-optimal time complexity meets practical efficiency. In SIGMOD. 75–86.
[52] Tiktok. 2023. 5 ways TikTok Creator Marketplace makes creator marketing
easy. https://www.tiktok.com/business/en-US/blog/making-creator-marketing-
easy/.
[53] Amo Tong, Ding-Zhu Du, and Weili Wu. 2018. On Misinformation Containment
in Online Social Networks. In NeurIPS, Vol. 31.
[54] Alan Tsang, Bryan Wilder, Eric Rice, Milind Tambe, and Yair Zick. 2019. Group-
Fairness in Influence Maximization. In IJCAI. 5997–6005.
[55] Rajan Udwani. 2018. Multi-Objective Maximization of Monotone Submodular
Functions with Cardinality Constraint. In NeurIPS. 9513–9524.
[56] Arun Vishwanath. 2015. Diffusion of deception in social media: Social contagion
effects and its antecedents. Information Systems Frontiers 17 (2015), 1353–1367.

[57] Shiqi Zhang, Yiqian Huang, Jiachen Sun, Wenqing Lin, Xiaokui Xiao, and Bo
Tang. 2023. Capacity Constrained Influence Maximization in Social Networks.
In SIGKDD. 3376–3385.
[58] Yuqing Zhu, Jing Tang, and Xueyan Tang. 2020. Pricing influential nodes in
online social networks. Proc. VLDB Endowment 13, 10 (2020), 1614–1627.

(v1,1)
(v1,2)
(v2,1)
(v2,2)
(v3,1)
(v3,2)
Figure 8: The illustration of 𝑈 in the counterexample. The
squares represent the elements in 𝑈 and the blue boxes rep-
resent the partitions in M𝑝 .
A CORRECTION ON LIAO ET AL. ’S ASSERTION
Popularity ratio maximization ( PRM) [41]. Given a graph𝐺 =
(𝑉,𝐸), the number of campaigns𝑇 , an overall capacity𝑘, and three
parameters𝑑𝑛 0,𝑑𝑝 0,𝑧 which define the objective function𝜎𝑃𝑅𝑀 , PRM
aims to find
𝑆1,...,𝑆 𝑇 = arg max
𝑆1,...,𝑆𝑇⊆𝑉,˝𝑇 𝑡 =1|𝑆𝑡|≤𝑘,𝑆𝑖∩𝑆𝑗 =∅∀𝑖≠𝑗 𝜎𝑃𝑅𝑀(𝑆1,...,𝑆 𝑇).
Similar to RM, we denote 𝑈 = 𝑉×[𝑇] and divide 𝑈 into|𝑉|
disjoint paritions𝑈1,𝑈 2,...,𝑈 |𝑉|, where𝑈𝑖 ={(𝑣𝑖,𝑡) :𝑡∈[𝑇]}. In
addition, we define a uniform matroidM𝑢 =(𝑈,I𝑢) and a partition
matroid M𝑝 =(𝑈,I𝑝), whereI𝑢 ={𝑆⊆ 𝑈 :|𝑆|≤ 𝑘} andI𝑝 =
{𝑆⊆𝑈 :∀𝑣𝑖∈𝑉,|𝑆∩𝑈𝑖|≤ 1}. Accordingly, the constraint of PRM
is M𝑃𝑅𝑀 =(𝑈,I𝑃𝑅𝑀), whereI𝑃𝑅𝑀 ={𝑆 :𝑆 is feasible} =I𝑢∩I𝑝.
Liao et al. ’s Assertion.Liao et al. [41] claim that M𝑃𝑅𝑀 is a parti-
tion matroid. We review its definition below.
Definition A.1 (Partition Matroid). A matroid M =(𝑈,I) is a
partition matroid iff there existℎ≥ 1 sets𝑈1,...,𝑈 ℎ, andℎ positive
integers𝑘1,...,𝑘 ℎ, such thatI ={𝑆⊆𝑈 :|𝑆∩𝑈𝑖|≤ 𝑘𝑖,∀𝑖∈[ ℎ]}.
However, this claim is incorrect, as we demonstrate in the fol-
lowing theorem.
Theorem A.2. M𝑃𝑅𝑀 is not a partition matroid.
Proof. We prove it by constructing a counterexample ofM𝑃𝑅𝑀
that is not a partition matroid. Before introducing the counterex-
ample, we first present Lemmas A.3-A.5 which will be frequently
utilized for showing that a matroid is not a partition matroid. It is
easy to verify their correctness.
Lemma A.3. A matroid M =(𝑈,I) is not a partition matroid iff
M is not identical to any possible partition matroid with ground set
𝑈 , i.e., the set of their independent sets are different.
Lemma A.4. For two matroids M and M′, if their ranks are not
equal, then M and M′ are not identical.
Lemma A.5. For two matroids M and M′, denote the set of all bases
of them asB andB′, respectively. If|B| ≠|B′|, then M and M′ are
not identical.
The counterexample. Consider a special case of M𝑢, M𝑝, and M𝑃𝑅𝑀
where𝑉 ={𝑣1,𝑣 2,𝑣 3},𝑇 = 2,𝑘 = 2. Figure 8 illustrates the ground
set𝑈 in this case, where M𝑝 constrains that at most 1 square can
be selected per column (the blue boxes), M𝑢 constrains that a maxi-
mum of𝑘 = 2 squares can be selected in total, and M𝑃𝑅𝑀 incorpo-
rates these constraints. Notably, M𝑃𝑅𝑀 is a general matroid with
the rank = 2, and it has 𝐶3 2× 22 = 12 different bases2. In light
of Lemma A.3, we next show that M𝑃𝑅𝑀 is not identical to any
partition matroid.
Given an integer𝑥, denote a partition matroid with ground set
𝑈 and the number of partitions ℎ = 𝑥 as Mℎ=𝑥 . For any Mℎ=3,
since each𝑘𝑖 (the cardinality constraint in partition𝑈𝑖) of Mℎ=3
is at least 1 (see Definition A.1), the rank of Mℎ=3 must exceed
2. By lemma A.4, M𝑃𝑅𝑀 is not identical to any possible Mℎ=3.
Anagolously, M𝑃𝑅𝑀 is not identical to any possible Mℎ=4, Mℎ=5, or
Mℎ=6. Among all Mℎ=1, there is only one with the rank equal to
M𝑃𝑅𝑀 , which is(𝑈,{𝑆⊆𝑈 :|𝑆|≤ 2}) = M𝑢 ≠ M𝑃𝑅𝑀. Therefore,
M𝑃𝑅𝑀 is also not identical to any possible Mℎ=1.
Regarding the case ofℎ = 2, if𝑘1 > 1 or𝑘2 > 1 in one Mℎ=2, the
rank of Mℎ=2 will also exceed 2, hence M𝑃𝑅𝑀 is not identical to
Mℎ=2 due to Lemma A.4. Therefore, we only consider any Mℎ=2
with𝑘1 =𝑘2 = 1, denoted as M∗ ℎ=2. We further divide all possible
M∗ ℎ=2 into three categories based on the size of their partitions|𝑈1|,
|𝑈2|, and denote the number of bases in each M∗ ℎ=2 as|B∗ ℎ=2|: (i) if
|𝑈1| = 1,|𝑈2| = 5, then|B∗ ℎ=2| = 1× 5 = 5; (ii) if|𝑈1| = 2,|𝑈2| = 4,
then|B∗ ℎ=2| = 2× 4 = 8; (iii) if|𝑈1| = 3,|𝑈2| = 3, then|B∗ ℎ=2| =
3× 3 = 9. As per Lemma A.5, none of them is identical to M𝑃𝑅𝑀 as
M𝑃𝑅𝑀 has 12 different bases.
Consequently, M𝑃𝑅𝑀 is not identical to any Mℎ=1,..., Mℎ=6.
Given that Mℎ=1,..., Mℎ=6 contains all possible partition matroids
on𝑈 , by Lemma A.3, M𝑃𝑅𝑀 is not a partition matroid. □
B PROOFS
B.1 Proofs for Results in Section 4
This section provides the proofs for Lemma 4.3, Lemma 4.4, and
Lemma 4.6. We first introduce some basic properties of the multi-
linear extension, which will be frequently utilized in the following
proofs. Specifically, given the multilinear extension𝐹, we have the
following properties.
proposition 1. For any 𝑖 ∈ [𝑛] and 𝜖 ≥ 0 (assuming that
x[𝑖]+ 𝜖≤ 1),𝐹(x+𝜖· 1𝑖) =𝐹(x)+ 𝜖𝜕𝐹(x) 𝜕x[𝑖] .
proposition 2. If𝑓 is non-decreasing, then 𝜕𝐹(x) 𝜕x[𝑖] ≥ 0 for any
𝑖. If 𝑓 is submodular, then 𝜕2𝐹(x) 𝜕𝑥[𝑖]𝜕𝑥[𝑗]≤ 0 for any𝑖,𝑗 , which implies
that 𝜕𝐹(x) 𝜕x[𝑖] is non-increasing.
Proof of Lemma 4.3. As per Proposition 1 and the definition of𝐹
in Eq.(3), we can derive that
𝜕𝐹(y)
𝜕y[𝑖] = 1 𝜖(𝐹(y+𝜖· 1𝑖)− 𝐹(y))
=
∑︁
𝑆⊆𝑈\{𝑢𝑖}
'›
«
Ö
𝑢𝑗∈𝑆
y[𝑗]
Ö
𝑢𝑗∈𝑈\{𝑢𝑖}\𝑆
(1− y[𝑗])“ﬁ
‹
· ΛR(𝑢𝑖|𝑆).
2We can obtain a base in Figure 8 by first selecting 2 columns out of 3 ( 𝐶3 2), then
selecting 1 square out of 2 in each column (22).

On the other hand,
∑︁
𝑆⊆𝑈
'›
«
Ö
𝑢𝑗∈𝑆
y[𝑗]
Ö
𝑢𝑗∈𝑈\𝑆
(1− y[𝑗])“ﬁ
‹
· ΛR(𝑢𝑖|𝑆)
=
∑︁
𝑆⊆𝑈 :𝑢𝑖 ∉𝑆
'›
«
(1− y[𝑖])
Ö
𝑢𝑗∈𝑆
y[𝑗]
Ö
𝑢𝑗∈𝑈\{𝑢𝑖}\𝑆
(1− y[𝑗])“ﬁ
‹
ΛR(𝑢𝑖|𝑆)
+
∑︁
𝑆⊆𝑈 :𝑢𝑖∈𝑆
'›
«
Ö
𝑢𝑗∈𝑆
y[𝑗]
Ö
𝑢𝑗∈𝑈\𝑆
(1− y[𝑗])“ﬁ
‹
· 0
=
∑︁
𝑆⊆𝑈\{𝑢𝑖}
'›
«
(1− y[𝑖])
Ö
𝑢𝑗∈𝑆
y[𝑗]
Ö
𝑢𝑗∈𝑈\{𝑢𝑖}\𝑆
(1− y[𝑗])“ﬁ
‹
ΛR(𝑢𝑖|𝑆).
Hence, the above-said partial derivative turns to
1
1− y[𝑖]
'›
«
∑︁
𝑆⊆𝑈
'›
«
Ö
𝑢𝑗∈𝑆
y[𝑗]
Ö
𝑢𝑗∈𝑈\𝑆
(1− y[𝑗])“ﬁ
‹
· ΛR(𝑢𝑖|𝑆)“ﬁ
‹
= 1 1− y[𝑖] E[ΛR(𝑢𝑖|Ω(y))] (11)
= 1 1− y[𝑖] ∑︁ 𝑅∈R :𝑢𝑖∈𝑅 E[I(𝑅∩ Ω(y) =∅)].
In addition, for any𝑅∈R , E[I(𝑅∩ Ω(y) =∅)] = ˛ 𝑢𝑖∈𝑅(1− y[𝑖]).
By the definition of𝑞𝑅 in Eq.(5), we can derive that
𝜕𝐹(y)
𝜕y[𝑖] =
∑︁
𝑅∈R :𝑢𝑖∈𝑅
˛
𝑢𝑗∈𝑅(1− y[𝑗])
1− y[𝑖] =
∑︁
𝑅∈R :𝑢𝑖∈𝑅
𝑞𝑅
1− y[𝑖].
□
Proof of Lemma 4.4. We denote𝐵(𝑖) ={𝑢𝑏(1),...,𝑢 𝑏(𝑖)} as the
independent set after selecting element 𝑢𝑏(𝑖) in iteration 𝑖 with
𝐵 =𝐵(𝑟), and𝑆𝑜 ={𝑢𝑠(1),...,𝑢 𝑠(𝑟)} as the optimal result on ΛR.
To complete this proof, we provide the following lemma.
Lemma B.1. In AMPSearch, a permutation of 𝑆𝑜 exists such that
∀𝑖∈[ 𝑟],𝑢𝑠(𝑖)∈𝑈\𝐵(𝑖−1) and𝐵(𝑖−1)∪{𝑢𝑠(𝑖)}∈I . In AMPSearch-
PM, a permutation of 𝑆𝑜 exists such that∀𝑖∈[ 𝑟],𝑢𝑠(𝑖)∈𝑈𝑙\𝐵(𝑖−1) ,
where𝑈𝑙 is the selected partition in Line 3 of Algorithm 3.
Lemma B.1 guarantees that there exists a permutation of𝑆𝑜 such
that𝑢𝑠(𝑖) is among the candidates when choosing 𝑢𝑏(𝑖) in both
algorithms. This implies that the selection of𝑢𝑏(𝑖), which has the
largest partial derivative, ensures
𝜕𝐹(x+𝜖· 1𝐵(𝑖−1))
𝜕x[𝑏(𝑖)] ≥ 𝜕𝐹(x+𝜖· 1𝐵(𝑖−1)) 𝜕x[𝑠(𝑖)] . (12)
For brevity, below we let x′ = x+𝜖· 1𝐵. Therefore, we have
𝐹(x′)− 𝐹(x)
=
𝑟∑︁
𝑖=1
𝐹(x+𝜖· 1𝐵(𝑖))− 𝐹(x+𝜖· 1𝐵(𝑖−1))
=𝜖·
𝑟∑︁
𝑖=1
𝜕𝐹(x+𝜖· 1𝐵(𝑖−1))
𝜕x[𝑏(𝑖)] (Proposition 1)
≥𝜖·
𝑟∑︁
𝑖=1
𝜕𝐹(x+𝜖· 1𝐵(𝑖−1))
𝜕x[𝑠(𝑖)] (Eq.(12))
≥𝜖·
𝑟∑︁
𝑖=1
𝜕𝐹(x′)
𝜕x[𝑠(𝑖)] (Proposition 2)
≥𝜖·
𝑟∑︁
𝑖=1
E

ΛR(𝑢𝑠(𝑖)|Ω(x′))  (Eq.(11))
≥𝜖· E

ΛR(𝑆𝑜∪ Ω(x′))− ΛR(Ω(x′))  (submodularity)
≥𝜖· ΛR(𝑆𝑜)− 𝐹(x′). (monotonicity)
□
Proof of Lemma B.1. We mainly utilize the following lemma.
Lemma B.2 ([ 8]). Given two bases 𝐵1,𝐵 2 of M, there is a bijection
𝜙 :𝐵1→𝐵2 such that∀𝑢𝑖∈𝐵1,𝐵1\{𝑢𝑖}∪{ 𝜙(𝑢𝑖)} is also a base.
We let𝑢𝑠(𝑖) = 𝜙

𝑢𝑏(𝑖)

and denote 𝐵′ = 𝐵\{𝑢𝑏(𝑖)}∪{ 𝑢𝑠(𝑖)},
which is also a base in I by Lemma B.2. For AMPSearch in Al-
gorithm 2, we prove∀𝑖 ∈ [𝑟],𝐵(𝑖−1)∪{𝑢𝑠(𝑖)}∈I and𝑢𝑠(𝑖) ∈
𝑈\𝐵(𝑖−1) by contradiction. Specifically, if 𝐵(𝑖−1)∪{𝑢𝑠(𝑖)} ∉I,
then𝐵′ = 𝐵(𝑖−1)∪{𝑢𝑠(𝑖),𝑢𝑏(𝑖+1),...,𝑢 𝑏(𝑟)} ∉I, which contra-
dicts the fact that 𝐵′ ∈ I. If 𝑢𝑠(𝑖) ∉ 𝑈\𝐵(𝑖−1), it implies that
∃𝑗∈[ 𝑖− 1],𝑢𝑠(𝑖) =𝑢𝑏(𝑗) and𝐵′ =𝐵\{𝑢𝑏(𝑖)}, which is not a base
since|𝐵\{𝑢𝑏(𝑖)}| <|𝐵| =𝑟 and leads to a contradiction.
For AMPSearch-PM in Algorithm 3, we prove∀𝑖∈[ 𝑟],𝑢𝑠(𝑖)∈
𝑈𝑙\𝐵(𝑖−1) in a similar way. In particular, if𝑢𝑠(𝑖)∈𝑈𝑞,𝑞 ≠𝑙, then
|𝐵′∩𝑈𝑙| =𝑘𝑙− 1 and|𝐵′∩𝑈𝑞| =𝑘𝑞+ 1, contradicting the definition
of base. Akin to the second case mentioned above, if𝑢𝑠(𝑖)∈𝐵(𝑖−1),
then𝐵′ =𝐵\{𝑢𝑏(𝑖)} and𝐵′ <𝑟, resulting in a contradiction. □
Proof of Lemma 4.6. To complete the proof, we provide the fol-
lowing corollary.
Corollary 1 ([ 12]). Given𝐹 be the multilinear extension of a
monotone and submodular function 𝑓 . For any y ∈ [0, 1]𝑈 and
𝑖,𝑗 ∈[ 𝑛], the function 𝐹 y 𝑖,𝑗(𝑡) =𝐹(y+𝑡(1𝑖− 1𝑗)) is convex.
In other words, the derivative
d𝐹 y 𝑖,𝑗(𝑡)
d𝑡 is non-decreasing as 𝑡
increases. Based on this, we focus on each unit step in AMPRound,
where it selects a conflicting element pair(𝑢𝑖,𝑢𝑗) between𝐵𝑡 and
𝐵𝑡+1, and decides on a swap direction. In Line 6 of Algorithm 4,
AMPRound computes the derivative at𝑡 = 0,
d𝐹 y 𝑖,𝑗(0)
d𝑡 = 𝜕𝐹(y) 𝜕y[𝑖] − 𝜕𝐹(y) 𝜕y[𝑗]. (13)
As per Corollary 1, if Eq.(13) is non-negative, then∀𝑡 > 0,
d𝐹 y 𝑖,𝑗(𝑡)
d𝑡 ≥
0. This indicates that updating y to y+𝜖(1𝑖− 1𝑗) results in an non-
decreasing update in 𝐹(y) from𝐹 y 𝑖,𝑗(0) to𝐹 y 𝑖,𝑗(𝜖). Conversely, if
Eq.(13) is negative, an analogous deduction shows that 𝐹 y 𝑖,𝑗(𝑡) is
non-increasing for𝑡 < 0. Accordingly, AMPRound updates𝐹(y) to
𝐹 y 𝑖,𝑗(−𝑡𝜖), ensuring it is non-decreasing. □

B.2 Proofs for Results in Section 5
This section provides the proofs for Theorem 5.1 and Lemma 5.2.
We mainly utilize two martingale-based concentration bounds as
shown in the following lemma, which can be derived from Corollary
1 and Corollary 2 of [50].
Lemma B.3. Given a setR of random RR sets with|R| =𝜃 and a
set𝑆⊆𝑈 independent ofR, for any 𝜆 > 0,
Pr

ΛR(𝑆)− 𝜃 𝜅·𝜎(𝑆)≥ 𝜆  ≤ exp  − 𝜆2 2𝜃 𝜅𝜎(𝑆)+ 2 3𝜆 ! , (14)
Pr

ΛR(𝑆)− 𝜃 𝜅·𝜎(𝑆)≤− 𝜆  ≤ exp  − 𝜆2 2𝜃 𝜅𝜎(𝑆) ! . (15)
Proof of Theorem 5.1. To complete the proof, we first establish
the following lemma to ensure the correctness of𝜃𝑚𝑎𝑥 .
Lemma B.4. Given constants𝜖 > 0,𝛽 > 0,𝛿 > 0 and a set 𝑆⊆𝑈
satisfying ΛR(𝑆)≥ 𝛽· ΛR(𝑆𝑜), if
|R|≥
2𝜅

𝛽
√︃
ln 2 𝛿+ √︃ 𝛽(ln|B|+ ln 2 𝛿) 2
𝜖2𝜎(𝑆∗) ,
then Pr[𝜎(𝑆) <(𝛽−𝜖)𝜎(𝑆∗)]≤ 𝛿.
By replacing𝜖 with 𝜖 2 ,𝛽 with 1− 1 𝑒−𝜖 2 , and𝛿 with 𝛿 3 , we obtain
the value of𝜃𝑚𝑎𝑥 in Eq.(8). Regarding𝜎𝑢(𝑆∗) and𝜎𝑙(𝑆), we utilize
the following lemma.
Lemma B.5. Given a constant 𝑝𝑓 > 0, by setting
𝜎𝑢(𝑆∗) = '›
«
√︄
Λ𝑢 R1 (𝑆∗)− ln𝑝𝑓 2 +
√︄
− ln𝑝𝑓
2
“ﬁ
‹
2
· 𝜅 |R 1|, (16)
𝜎𝑙(𝑆) = '››
«
'›
«
√︄
ΛR2(𝑆)−
2 ln𝑝𝑓
9 −
√︄
− ln𝑝𝑓
2
“ﬁ
‹
2
+
ln𝑝𝑓
18
“ﬁﬁ
‹
· 𝜅 |R 2|,
(17)
we have Pr[𝜎(𝑆∗) >𝜎𝑢(𝑆∗)]≤ 𝑝𝑓 and Pr[𝜎(𝑆) <𝜎𝑙(𝑆)]≤ 𝑝𝑓 .
Based on Lemma B.5,𝜎𝑢(𝑆∗) in Eq.(9) and𝜎𝑙(𝑆) in Eq.(10) are
obtained using Eq.(16) and Eq.(17), respectively, with𝑝𝑓 =𝛿/(3·
𝑖𝑚𝑎𝑥).
As guaranteed above, each computation of 𝜎𝑢(𝑆∗) or𝜎𝑙(𝑆) is
correct w.p. at least 1−𝛿/(3·𝑖𝑚𝑎𝑥). In addition, when |R 1| =
|R 2| =𝜃𝑚𝑎𝑥 , RAMP achieves a(1− 1/𝑒−𝜖) approximation w.p. at
least 1−𝛿/3. By the union bound, RAMP achieves a 1− 1/𝑒−𝜖
approximation w.p. at least 1−𝛿. □
Proof of Lemma B.4. To complete the proof, we first establish the
following lemma, which illustrates that when the size|R| =𝜃 is
sufficiently large, 𝜅 𝜃 ΛR(𝑆∗) is close to𝜎(𝑆∗).
Lemma B.6. Given constants 𝜖1 > 0 and𝛿1 > 0, if 𝜃 ≥ 𝜃′ 1 =
2𝜅 ln(1/𝛿1)
𝜎(𝑆∗)·𝜖 2 1 , then
Pr

ΛR(𝑆∗)≥( 1−𝜖1)𝜃 𝜅·𝜎(𝑆∗)  ≥ 1−𝛿1.
Combining it with the fact that ΛR(𝑆)≥ 𝛽· ΛR(𝑆𝑜), we can
derive that Eq.(18) holds w.p. at least 1−𝛿1 if𝜃≥𝜃′ 1:
ΛR(𝑆)≥ 𝛽· ΛR(𝑆𝑜)≥ 𝛽· ΛR(𝑆∗)≥ 𝛽·( 1−𝜖1)𝜃 𝜅𝜎(𝑆∗). (18)
We now use the following lemma to connect𝜎(𝑆) with𝜎(𝑆∗).
Lemma B.7. Given constants𝜖2 =𝜖−𝛽·𝜖1≥ 0 and𝛿2 > 0, if
Eq.(18) holds and
𝜃≥𝜃′ 2 = 2𝛽𝜅·

ln|B|+ ln 1 𝛿2

𝜎(𝑆∗)· 𝜖2 2 ,
then
Pr

𝜎(𝑆)≥( 𝛽−𝜖)· 𝜎(𝑆∗)  ≥ 1−𝛿2.
Combining Lemmas B.6-B.7 and the union bound, we derive that
if𝜃≥ max(𝜃′ 1,𝜃′ 2), we have𝜎(𝑆)≥( 𝛽−𝜖)· 𝜎(𝑆∗) w.p. of at least
1−𝛿1−𝛿2. By setting𝛿1 =𝛿2 =𝛿/2 and
𝜖1 = 𝜖
𝛽+
√︄
ln|B|+ ln 1 𝛿2
1
𝛽 ln 1 𝛿1
!,
we have
𝜃′ 1 =𝜃′ 2 = 2𝜅

𝛽
√︃
ln 2 𝛿+ √︃ 𝛽(ln|B|+ ln 2 𝛿) 2
𝜖2𝜎(𝑆∗) .
□
Proof of Lemma B.6. As per Eq.(15), we have
Pr

ΛR(𝑆∗)≤( 1−𝜖1)𝜃 𝜅·𝜎(𝑆∗) 
≤ Pr

ΛR(𝑆∗)− 𝜃 𝜅·𝜎(𝑆∗)≤− 𝜖1 𝜃 𝜅·𝜎(𝑆∗) 
≤ exp

−
𝜖2 1𝜎(𝑆∗)𝜃
2𝜅
!
≤ exp

−
𝜖2 1𝜎(𝑆∗)𝜃′ 1
2𝜅
!
≤𝛿1.
□
Proof of Lemma B.7. For a set𝑆′∈B , we say𝑆′ is bad if𝜎(𝑆′) <
(𝛽−𝜖)𝜎(𝑆∗). Based on Eq.(14), for a bad𝑆′, we have
Pr
h𝜅
𝜃· ΛR(𝑆′)− 𝜎(𝑆′)≥ 𝜖2·𝜎(𝑆∗) i
≤ exp

−
𝜖2 2·𝜎(𝑆∗)2
2𝜎(𝑆′)+ 2 3𝜖2𝜎(𝑆∗) · 𝜃 𝜅
!
≤ exp

−
𝜖2 2·𝜎(𝑆∗)
2·( 𝛽−𝜖)+ 2 3·𝜖2 · 𝜃 𝜅
!
≤ exp

−
𝜖2 2·𝜎(𝑆∗)𝜃′ 2
2𝛽·𝜅
!
≤𝛿2
|B|.
Since there exist at most|B| possible𝑆′, by the union bound, we
obtain that for a𝑆 that satisfies Eq.(18),
𝜎(𝑆)≤ 𝜅 𝜃· ΛR(𝑆′)− 𝜖2·𝜎(𝑆∗)≤( 𝛽−𝜖)· 𝜎(𝑆∗)
w.p. at most𝛿2. □

Proof of Lemma B.5. We denote𝜃(1) =|R 1| and𝜃(2) =|R 2|.
Regarding the upper bound𝜎𝑢(𝑆∗), based on Eq.(15) in Lemma B.3,
we have
Pr
 𝜎(𝑆∗) > '› « √︄ Λ𝑢 R1 (𝑆∗)− ln𝑝𝑓 2 + √︄ − ln𝑝𝑓 2 “ﬁ ‹ 2 · 𝜅 𝜃(1) 
≤ Pr
 𝜎(𝑆∗) > '› « √︄ ΛR1(𝑆∗)− ln𝑝𝑓 2 + √︄ − ln𝑝𝑓 2 “ﬁ ‹ 2 · 𝜅 𝜃(1) 
≤ Pr
 '› « √︄ 𝜃(1)·𝜎(𝑆∗) 𝜅 − √︄ − ln𝑝𝑓 2 “ﬁ ‹ 2 > ΛR1(𝑆∗)− ln𝑝𝑓 2 
= Pr
 − √︄ −2· ln𝑝𝑓· 𝜃(1)·𝜎(𝑆∗) 𝜅 > ΛR1(𝑆∗)− 𝜃(1)·𝜎(𝑆∗) 𝜅 
≤ exp'›
«
2· ln𝑝𝑓· 𝜃(1)·𝜎(𝑆∗) 𝜅
2· 𝜃(1)·𝜎(𝑆∗) 𝜅
“ﬁ
‹
=𝑝𝑓.
Regarding the lower bound 𝜎𝑙(𝑆), by Eq. (14) in Lemma B.3, we
have
Pr
"
𝜎(𝑆) <
 √︃
ΛR2(𝑆)− 2 ln𝑝𝑓 9 − √︃ − ln𝑝𝑓 2 2 + ln𝑝𝑓 18 ! · 𝜅 𝜃(2) #
= Pr
√︃
𝜎(𝑆)·𝜃(2)
𝜅 − ln𝑝𝑓 18 < √︃ ΛR2(𝑆)− 2 ln𝑝𝑓 9 − √︃ − ln𝑝𝑓 2 
= Pr
√︃
− 2 ln𝑝𝑓·𝜎(𝑆)𝜃(2) 𝜅 + ln2𝑝𝑓 9 − ln𝑝𝑓 3 < ΛR2(𝑆)− 𝜎(𝑆)𝜃(2) 𝜅 
≤ exp
'››››
«
−
√︃
− 2 ln𝑝𝑓·𝜎(𝑆)𝜃(2) 𝜅 + ln2𝑝𝑓 9 − ln𝑝𝑓 3 2
2· 𝜎(𝑆)𝜃(2) 𝜅 + 2 3· √︃ − 2 ln𝑝𝑓·𝜎(𝑆)𝜃(2) 𝜅 + ln2𝑝𝑓 9 − ln𝑝𝑓 3 
“ﬁﬁﬁﬁ
‹
=𝑝𝑓.
This completes the proof. □
Proof of Lemma 5.2. We denote
𝜃(1) =|R 1|,𝜃(2) =|R 2|,
𝛽 = 1− 1 𝑒− 𝜖 2, 𝜖1 =𝜖/2, e𝜖1 =(1−𝛽)𝜖1, b𝜖1 =
√︄
2𝑎𝜅
𝜎(𝑆∗)𝜃(1),
𝜖2 =
√︄
2𝑎𝜅
𝜎(𝑆)𝜃(2), e𝜖2 =

√︄
2𝑎𝜎(𝑆)𝜃(2)
𝜅 + 𝑎2 9 + 𝑎 3  · 𝜅 𝜎(𝑆)𝜃(2),
where𝑎 =𝑐 ln 3𝑖𝑚𝑎𝑥 𝛿 for any𝑐≥ 1. Furthermore, we denote𝜃′ =
max{𝜃′ 1,𝜃′ 2}, where
𝜃′ 1 = (2+ 2e𝜖1/3)𝜅 ln 6|B| 𝛿 e𝜖2 1𝜎(𝑆∗) , 𝜃′ 2 = 27𝜅 ln 3𝑖𝑚𝑎𝑥 𝛿 (𝛽−𝜖1)𝜖2 1𝜎(𝑆∗).
One can verify that𝜃′ =𝑂(( ln|B|+ ln(1/𝛿))𝜅𝜖−2 𝑡 /𝜎(𝑆∗)). Accord-
ing to Lemma B.3, for any𝑐≥ 1, if𝜃(1) =𝜃(2) =𝑐𝜃′, we can derive
the following results.
Pr
 𝜅
𝜃(1)· ΛR1(𝑆∗) <(1−𝜖1)𝜎(𝑆∗)

≤
𝛿
6
𝑐
, (19)
Pr
 𝜅
𝜃(1)· ΛR1(𝑆) >𝜎(𝑆)+ e𝜖1·𝜎(𝑆∗)

≤
 𝛿
6|B|
𝑐
, (20)
Pr
 𝜅
𝜃(1)· ΛR1(𝑆∗) <(1− b𝜖1)𝜎(𝑆∗)

≤
 𝛿
3𝑖𝑚𝑎𝑥
𝑐
, (21)
Pr
 𝜅
𝜃(2)· ΛR2(𝑆) <(1−𝜖2)𝜎(𝑆)

≤
 𝛿
3𝑖𝑚𝑎𝑥
𝑐
, (22)
Pr
 𝜅
𝜃(2)· ΛR2(𝑆) >(1+ e𝜖2)𝜎(𝑆)

≤
 𝛿
3𝑖𝑚𝑎𝑥
𝑐
. (23)
Note that by definition, e𝜖2 =
√︂
𝑎(2+2e𝜖2/3)𝜅
𝜎(𝑆)𝜃(2) , so Eq.(23) is obatined
by
𝑙.ℎ.𝑠. ≤ exp
'››
«
−
𝑎(2+2e𝜖2/3)𝜅
𝜎(𝑆)𝜃(2) 𝜎(𝑆)
2+ 2e𝜖2/3 · 𝜃(2) 𝜅 “ﬁﬁ
‹
=
 𝛿
3𝑖𝑚𝑎𝑥
𝑐
.
Recall in RAMP that𝑆 is derived fromR1. To satisfy the requirement
of Lemma B.3, we consider any of the|B| possible values of𝑆 in
Eq.(20). By the union bound, the probability that at least one of the
events in Eq.(19)-Eq.(23) happens is at most
𝛿
6
𝑐
+
 𝛿
6|B|
𝑐
·|B|+ 3·
 𝛿
3𝑖𝑚𝑎𝑥
𝑐
≤𝛿𝑐.
In the following, we elaborate on the connections implied by
these events. If the events in Eq.(19) and Eq.(20) do not happen, we
have
𝜎(𝑆)≥ ΛR1(𝑆)− e𝜖1𝜎(𝑆∗)
≥𝛽· ΛR1(𝑆∗)− e𝜖1𝜎(𝑆∗)
≥𝛽·( 1−𝜖1)𝜎(𝑆∗)− e𝜖1𝜎(𝑆∗)
=(𝛽−𝜖1)𝜎(𝑆∗).
Therefore, by the definition ofb𝜖1,𝜖 2,e𝜖2 and the fact that𝑐𝜃′≥𝜃′ 2,
we have
b𝜖1≤
√︄
2(𝛽−𝜖1)𝜖2 1
27 <𝜖1/3,
𝜖2≤
√︄
2(𝛽−𝜖)𝜎(𝑆∗)𝜖2 1
27𝜎(𝑆) <𝜖1/3,
e𝜖2 =
√︄
𝑎(2+ 2e𝜖2/3)𝜅
𝜎(𝑆)𝜃(2) ≤
√︄
(2+ 2e𝜖2/3)𝜖2 1
27 <𝜖1/3.

In addition, if the event in Eq.(21) does not happen, we have
𝜅
𝜃(1) ΛR1(𝑆∗)≥

1−
√︄
2𝑎𝜅
𝜎(𝑆∗)𝜃(1)
!
𝜎(𝑆∗)
⇔ 𝜅
𝜃(1)𝜎(𝑆∗) ≥
1−
√︃ 2𝑎𝜅
𝜎(𝑆∗)𝜃(1)
ΛR1(𝑆∗)
⇔ 𝜅
𝜃(1)𝜎(𝑆∗) ≥
'››
«
1√︃
ΛR1(𝑆∗)+ 𝑎 2+ √︃ 𝑎 2
“ﬁﬁ
‹
2
⇔
√︂
ΛR1(𝑆∗)+ 𝑎 2+ √︂𝑎 2 2 · 𝜅 𝜃(1) ≥𝜎(𝑆∗).
Therefore, we can infer that
1− b𝜖1 = 1−
√︄
2𝑎𝜅
𝜎(𝑆∗)𝜃(1)
≤ 1−
√
2𝑎√︃
ΛR1(𝑆∗)+ 𝑎 2+ √︃ 𝑎 2
≤
Λ𝑢 R1 (𝑆∗) √︃
Λ𝑢 R1 (𝑆∗)+ 𝑎 2+ √︃ 𝑎 2 2.
By setting𝑝𝑓 = 𝛿 3𝑖𝑚𝑎𝑥 in Eq.(16) such that ln 1 𝑝𝑓 ≤𝑎, we have
𝜎𝑢(𝑆∗)≤
√︂
Λ𝑢 R1 (𝑆∗)+ 𝑎 2+ √︂𝑎 2 2 · 𝜅 𝜃(1) ≤ Λ𝑢 R1 (𝑆∗) 1− b𝜖1 · 𝜅 𝜃(1). (24)
Similarly, when the event in Eq.(23) does not happen, we have
 √︂
ΛR2(𝑆)+ 2𝑎 9 − √︂𝑎 2 !2 − 𝑎 18≥𝜎(𝑆)· 𝜃(2) 𝜅 .
Therefore, we can infer that
ΛR2(𝑆)− e𝜖2𝜎(𝑆)· 𝜃(2) 𝜅
= ΛR2(𝑆)−

√︄
2𝑎𝜎(𝑆)𝜃(2)
𝜅 + 𝑎2 9 + 𝑎 3 
≤ ΛR2(𝑆)−
√︂
2𝑎ΛR2(𝑆)+ 4𝑎2 9 −𝑎+ 𝑎 3 
=
 √︂
ΛR2(𝑆)+ 2𝑎 9 − √︂𝑎 2 !2 − 𝑎 18
By setting𝑝𝑓 = 𝛿 3𝑖𝑚𝑎𝑥 in Eq.(17) such that ln 1 𝑝𝑓 ≤𝑎, we have
𝜎𝑙(𝑆)≥ ΛR2(𝑆)· 𝜅 𝜃(2)− e𝜖2𝜎(𝑆) = ΛR2(𝑆)− e𝜖2𝜎(𝑆). (25)
Putting (24) and (25) together, when none of the events in Eq.(19)-
Eq.(23) happen, we have
𝜎𝑙(𝑆)
𝜎𝑢(𝑆∗)≥
ΛR2(𝑆)− e𝜖2𝜎(𝑆)· 𝜃(2) 𝜅
Λ𝑢 R1 (𝑆∗)/( 1− b𝜖1)
≥
(1− b𝜖1)( 1−𝜖2− e𝜖2)𝜎(𝑆)· 𝜃(2) 𝜅
Λ𝑢 R1 (𝑆∗)
>(1− b𝜖1−𝜖2− e𝜖2)
𝜎(𝑆)· 𝜃(2) 𝜅
ΛR1(𝑆)
ΛR1(𝑆)
Λ𝑢 R1 (𝑆∗)
>(1−𝜖1)
ΛR1(𝑆)− e𝜖1·𝜎(𝑆∗)· 𝜃(2) 𝜅
ΛR1(𝑆) ·𝛽
≥( 1−𝜖1) ΛR1(𝑆)− e𝜖1ΛR1(𝑆∗)/( 1−𝜖1) ΛR1(𝑆) ·𝛽
≥( 1−𝜖1)

1− e𝜖1/(1−𝜖1) 𝛽  ·𝛽
=𝛽−𝜖1 = 1− 1/𝑒−𝜖.
This implies that when we generate 𝜃(1) = 𝜃(2) = 𝑐𝜃′ RR sets,
RAMP does not terminate only if at least one of the events in
Eq.(19)-Eq.(23) happens, whose probability is at most𝛿𝑐 𝑡 . Let 𝑗 be
the first iteration that 𝜃(1) = 𝜃(2) ≥ 𝜃′. From this iteration, the
expected number of RR sets generated thereafter is at most
2·
𝑖𝑚𝑎𝑥∑︁
𝑧=𝑗
𝜃1· 2𝑧·𝛿 2𝑧−𝑗
= 2· 2𝑗·𝜃1
𝑖𝑚𝑎𝑥−𝑗∑︁
𝑧=0
2𝑧·𝛿 2𝑧
≤ 4𝜃′
𝑖𝑚𝑎𝑥−𝑗∑︁
𝑧=0
2−2𝑧+𝑧 (2𝑗−1𝜃1 <𝜃′ and𝛿≤ 1/2)
≤ 4𝜃′
𝑖𝑚𝑎𝑥−𝑗∑︁
𝑧=0
2−𝑧 (−2𝑧+𝑧≤−𝑧)
≤ 8𝜃′.
Therefore, the expected number of RR sets generated is less than
10𝜃′, which is also𝑂(( ln|B|+ ln(1/𝛿))𝜅𝜖−2/𝜎(𝑆∗)). □
C TIGHTENED UPPER BOUND
In Section 5.1, we set the tightened upper bound Λ𝑢 R1 (𝑆∗) to
Λ𝑢 R1 (𝑆∗) = min
 
 min 0≤𝑡≤1\𝜖𝑠
n
bΛR1(x𝑡)
o
, 𝐹(x1/𝜖𝑠) 1− 1
(1+𝜖𝑠)
1𝜖𝑠
,|R 1|
 
 , (26)
where x0 = 0, x𝑡 = ˝𝑡 𝑙=1𝜖𝑠· 1𝐵𝑙 , and
bΛR(x) =𝐹(x)+ max 𝑆∈I
 

∑︁
𝑢𝑖∈𝑆
∑︁
𝑅∈R :𝑢𝑖∈𝑅
𝑞𝑅
 
 .
In particular, 𝐹(x1/𝜖𝑠) 1− 1
(1+𝜖𝑠)
1𝜖𝑠
≥ ΛR1(𝑆∗) is derived from Theorem 4.7,
and|R 1|≥ ΛR1(𝑆∗) holds clearly. The following lemma ensures
that min
0≤𝑡≤1\𝜖𝑠
n
bΛR1(x𝑡)
o
≥ ΛR1(𝑆∗).
Lemma C.1. For any x∈[ 0, 1]𝑛 and a collectionR of RR sets, we
have bΛR(x)≥ ΛR(𝑆𝑜)≥ ΛR(𝑆∗).

Algorithm 7: RM-A-Simplified(G,𝜅, M,𝜖,𝛿)
1 𝜃𝑚𝑎𝑥← 2|𝑉| 𝜖 2

1
2
√︃
ln 16 𝛿 + √︃ 1 2(𝑇·|𝑉|+ ln 16 𝛿) 2 ;
2 𝑖𝑚𝑎𝑥← log2𝜃𝑚𝑎𝑥 ;
3 GenerateR1 andR2 with|R 1| =|R 2| = 1;
4 for𝑖 = 1, 2,...,𝑖 𝑚𝑎𝑥 do
5 𝑆← Greedy(R 1, M);
6 Compute𝜎𝑢(S∗) by Eq.(16) onR1 with
𝑝𝑓 = 𝛿 4(𝑇+2)𝑖𝑚𝑎𝑥 and Λ𝑢 R1 (𝑆∗) = 2· ΛR1(𝑆);
7 Compute𝜎𝑙(S) by Eq.(17) onR2 with𝑝𝑓 = 𝛿 4(𝑇+2)𝑖𝑚𝑎𝑥 ;
8 if 𝜎𝑙(𝑆) 𝜎𝑢(𝑆∗)≥ 1/2−𝜖 or𝑖 =𝑖𝑚𝑎𝑥 then return𝑆;
9 Double the sizes ofR1 andR2 with new random RR sets;
Algorithm 6: Maximum-Weight-Greedy(R, x,𝑞𝑅)
1∀𝑢𝑖∈𝑈,𝑤 𝑖 = ˝ 𝑅∈R :𝑢𝑖∈𝑅𝑞𝑅;
2 𝑆←∅ ;
3 for𝑖 = 1, 2,...,𝑛 do
4 𝑢𝑗← the element with the𝑖-th largest𝑤𝑗 ;
5 if𝑆∪{𝑢𝑗}∈I then𝑆←𝑆∪{𝑢𝑗};
6 return ˝ 𝑢𝑗∈𝑆𝑤𝑗 ;
Proof. By the monotonicity and submodularity of ΛR(·), we
have
ΛR(𝑆𝑜)≤ E[ΛR(𝑆𝑜∪ Ω(x))]
≤𝐹(x)+
∑︁
𝑢𝑖∈𝑆𝑜
E[ΛR(𝑢𝑖|Ω(x))]
≤𝐹(x)+ max
𝑆∈I
 

∑︁
𝑢𝑖∈𝑆
E[ΛR(𝑢𝑖|Ω(x)]
 
 .
Derived from Eq. (11), we have E[ΛR(𝑢𝑖|Ω(x)] = ˝
𝑅∈R :𝑢𝑖∈𝑅
𝑞𝑅.
Therefore, the above fromula is equal to
𝐹(x)+ max
𝑆∈I
 

∑︁
𝑢𝑖∈𝑆
'›
«
∑︁
𝑅∈R :𝑢𝑖∈𝑅
𝑞𝑅 “ﬁ
‹
 
 ,
which completes the proof. □
To compute Eq.(26), we utilize a greedy algorithm [19] to obtain
the term max𝑆∈I{ ˝
𝑢𝑖∈𝑆
˝
𝑅∈R :𝑢𝑖∈𝑅
𝑞𝑅}. Its pseudocode is shown in
Algorithm 6. We invoke Maximum-Weight-Greedy after each exe-
cution of AMPSearch or AMPSearch-PM in Line 9 of Algorithm 1.
In addition, 𝐹(x𝑡) can be obtained by accumulating the partial
derivatives of the selected𝑢𝑗 at all𝑟 iterations in Line 3 (resp. Line
4) of AMPSearch (resp. AMPSearch-PM).
D IMPLEMENTATION DETAILS
In each IM-GM instance, we adopt the same approach that constructs
one RR set𝑅 as in its original work. Apart from MRIM, the details
for other IM-GM instances are described below.
• IM: We first select a node𝑣𝑖∈𝑉 uniformly at random, and then
simulate a reverse diffusion process in𝐺 starting from𝑣𝑖. We
let𝑅 be the set of all examined nodes.
• RM: We first randomly select a node 𝑣𝑖 ∈ 𝑉 uniformly, and a
campaign index 𝑗∈[ 𝑇] w.p. 𝛼𝑗˝
𝑗∈[𝑇]𝛼𝑗 . We simulate a reverse
diffusion process starting from𝑣𝑖, denoting the set of examined
nodes as𝑅′. Then, we let𝑅←𝑅′×{ 𝑗}.
• AdvIM: We first select a node𝑣𝑖∈𝑉\𝐴 uniformly at random, and
then simulate the reverse diffusion process from𝑣𝑖 and include
the examined nodes into𝑅. If𝑅∩𝐴 =∅, we clear𝑅 and repeat
the process until𝑅∩𝐴 ≠∅.
In AdvIM, we compute 𝜃max in Eq.(8) setting𝜅 ← |𝑉|−| 𝐴|.
Note that this may slightly increase 𝜃max but does not affect the
correctness and overall time complexity of RAMP.
Regarding the lazy evaluation technique on AMP and AMP-PM,
this process can be efficiently executed using a max-heap and im-
proves the practical runtime performance. Specifically, we maintain
an upper bound of𝜕𝐹(y) 𝜕y[𝑖] for each𝑢𝑖∈𝑈 , denoted as𝐹𝑢 𝑖 , initially set
to+∞. During each iteration, when selecting𝑢𝑗 , we avoid travers-
ing all elements. Instead, we repeatedly choose the element𝑢𝑗 with
the largest𝐹𝑢 𝑗 , updating𝐹𝑢 𝑗 to 𝜕𝐹(y) 𝜕y[𝑗] = ˝ 𝑅∈R :𝑢𝑗∈𝑅𝑞𝑅/(1− y[𝑗]).
If𝐹𝑢 𝑗 continues to be the largest one among the candidates after
this update, it confirms that𝑢𝑗 has the largest partial derivative.
It is worth noting that the original version ofRM-A [30] includes
two additional sets of input:𝑐𝑖,𝑗 , the cost of selecting the node𝑣𝑖
for campaign 𝑗, and𝑏𝑗 , the maximum tolerable cost for campaign
𝑗. By setting 𝑐𝑖,𝑗 = 1,∀𝑣𝑖 ∈ 𝑉,𝑗 ∈ [𝑇] and𝑏𝑗 =+∞,∀𝑗 ∈ [𝑇],
its simplified pseudocode is presented in Algorithm 7, with the
notations aligned to our paper. Algorithm 7 is similar toRAMP, but
it differs in (i) the parameterization of𝜃𝑚𝑎𝑥 ,𝑖𝑚𝑎𝑥 , and𝑝𝑓 , and (ii)
the utilization Greedy3 to yield the set𝑆.
E MORE EXPERIMENTAL RESULTS
Memory usage. We report the memory usage of each scalable
implementation for RM, MRIM, or AdvIM at its peak memory con-
sumption in Figure 11. Similar to Figure 7, we report results for the
largest dataset on which the baseline algorithm with𝜖 = 0.5 can
terminate within 72 hours. As shown, the memory usage of each
algorithm is roughly proportional to its running time reported in
Figure 7. Most notably, the memory occupancy of RAMP is consis-
tently lower than that of RM-A, CR-NAIMM and AAIMM due to
the smaller number of sampled RR sets. Specifically, the memory
footprint of RAMP in AdvIM is up to 10× lower than AAIMM on
Wiki. Regarding RM, RAMP or RM-A has a memory footprint of
102GB on Twitter-large when𝜖≥ 0.4. Of this, 62GB is allocated
for storing the dataset (with half for the original graph and half for
the reversed graph, on which the RR sets are generated), while the
remaining 40 GB (∼39%) is used for storing the sampled RR sets.
In conclusion, the resource utilization of the proposed RAMP is
superior to all competitors.
More experiments for RM. Figures 9-10 report the running times
and memory footprints of scalable algorithms for RM on smaller
3By our settings of𝑐𝑖,𝑗 and𝑏𝑗 , the element selection algorithm RM_with_Oracle(𝜏)
in [30] is essentially equivalent to Greedy, for any given𝜏.

RAMP RM-A
0 0.2 0.4 0.60.1
101
103
approx. guarantee
running time (s)
(a) Facebook
0 0.2 0.4 0.60.1
101
103
approx. guarantee
running time (s)
(b) Wiki
0 0.2 0.4 0.6100
102
104
approx. guarantee
running time (s)
(c) Twitter
0 0.2 0.4 0.6101
103
105
approx. guarantee
running time (s)
(d) Google+
0 0.2 0.4 0.6101
103
105
approx. guarantee
running time (s)
(e) Pokec
0 0.2 0.4 0.6101
103
105
approx. guarantee
running time (s)
(f) LiveJournal
Figure 9: Total running time in RM.
0 0.2 0.4 0.6101
102
approx. guarantee
memory usage (MB)
(a) Facebook
0 0.2 0.4 0.6101
102
103
approx. guarantee
memory usage (MB)
(b) Wiki
0 0.2 0.4 0.6102
103
approx. guarantee
memory usage (MB)
(c) Twitter
0 0.2 0.4 0.6103
104
approx. guarantee
memory usage (MB)
(d) Google+
0 0.2 0.4 0.6103
104
105
approx. guarantee
memory usage (MB)
(e) Pokec
0 0.2 0.4 0.6
104
105
approx. guarantee
memory usage (MB)
(f) LiveJournal
Figure 10: Memory usage in RM.
RAMP RM-A CR-NAIMM AAIMM
0 0.2 0.4 0.6100
120
approx. guarantee
memory usage (GB)
(a) RM (Twitter-large)
0 0.2 0.4 0.6
103
104
105
approx. guarantee
memory usage (MB)
(b) MRIM (Wiki)
0 0.2 0.4 0.6101
102
103
approx. guarantee
memory usage (MB)
(c) AdvIM (Wiki)
Figure 11: Memory usage of scalable algorithms.
RAMP CR-NAIMM
0 0.2 0.4 0.6100
102
104
approx. guarantee
running time (s)
(a) Running time
0 0.2 0.4 0.6102
103
104
105
approx. guarantee
memory usage (MB)
(b) Memory usage
Figure 12: Running time and memory usage in MRIM on Wiki.
datasets, respectively. As shown in Figure 9, RAMP is more effi-
cient than RM-A while ensuring the same approximation guarantee
across all cases. In particular,RAMP is an order of magnitude faster
than RM-A on Google+, Pokec, and LiveJournal. Additionally, Fig-
ure 10 shows that RAMP occupies significantly lower memory than
RM-A. For example, the memory usage of RAMP is 8.7× lower than
RM-A on Wiki when ensuring a 0.4-approximation.
More experiments for MRIM. Figure 12 reports the running time
and memory usage of each algorithm for MRIM on Wiki. Note that
we exclude results on other datasets as CR-NAIMM and AAIMM
fail to terminate within 72 hours even when𝜖 = 0.5. Here, RAMP
outperforms CR-NAIMM at least three orders of magnitude in
terms of running time and at least an order of magnitude in terms
of memory usage, respectively. To summarize, Figures 9-12 present
similar outcomes to those in Figures 7-11, where RAMP is more
efficient regarding running time and resource utilization.
F ADJUSTED ALGORITHM FOR DEPLOYMENT
Note that the enhanced objective function𝜎𝑊(𝑆) is also monotone
and submodular. Towards the new objective 𝜎𝑊(𝑆), we modify
AMP for maximizing the following function:
Λ𝑊 R(𝑆) = ∑︁
𝑆′⊆𝑆
Ö
𝑢𝑗∈𝑆′
𝑤𝑗
Ö
𝑢𝑗∈𝑆\𝑆′
(1−𝑤𝑗)ΛR(𝑆′),
which is an unbiased estimate of𝜎𝑊(𝑆) satisfying𝜎𝑊(𝑆) = 𝜅 |R| ·
Λ𝑊 R(𝑆). Specifically, at the beginning of AMP (Algorithm 1), we
maintain a variable
𝑞′ 𝑅 = Ö
𝑢𝑖∈𝑅
(1− x[𝑖]· 𝑤𝑖)
instead of𝑞𝑅 for each𝑅∈R inQ. It is also initialized to1. Through-
out Algorithms 1-4, when calculating the partial derivative 𝜕𝐹(y) 𝜕y[𝑖]
w.r.t.𝑢𝑖, we replace ˝
𝑅∈R :𝑢𝑖∈𝑅
𝑞𝑅
1−y[𝑖] with 𝑤𝑖 1−y[𝑖]𝑤𝑖 ˝ 𝑅∈R :𝑢𝑖∈𝑅 𝑞′ 𝑅.
Furthermore, when updating each𝑞𝑅, we replace𝑞𝑅←𝑞𝑅· 1−y[𝑗] 1−y[𝑗]+𝑧
with𝑞′ 𝑅←𝑞′ 𝑅· 1−𝑤𝑗 y[𝑗] 1−𝑤𝑗(y[𝑗]+𝑧) , where𝑧∈{ 𝜖,−𝜖,𝑡𝜖,−𝑡𝜖}. The cor-
rectness of these adjustments is assured by the following lemma.
Lemma F.1. Let𝐹𝑊 denote the multilinear extension of Λ𝑊 R(𝑆).
For any x∈[ 0, 1]𝑈 we have
𝜕𝐹𝑊(x)
𝜕x[𝑖] = 𝑤𝑖 1− x[𝑖]· 𝑤𝑖 ∑︁ 𝑅∈R :𝑢𝑖∈𝑅 Ö 𝑢𝑗∈𝑅 (1− x[𝑗]· 𝑤𝑗).
Proof. Similar to Eq.(11), we have
𝜕𝐹𝑊(x)
𝜕x[𝑖] = 1 1− x[𝑖] E h Λ𝑊 R(𝑢𝑖|Ω(x)) i . (27)

In addition, for any𝑆⊆𝑈 and𝑢𝑖∈𝑈\𝑆, we have
Λ𝑊 R(𝑢𝑖|𝑆) = ∑︁
𝑆′⊆𝑆∪{𝑢𝑖}
Ö
𝑢𝑗∈𝑆′
𝑤𝑗
Ö
𝑢𝑗∈𝑆\𝑆′
(1−𝑤𝑗)ΛR(𝑆′)
−
∑︁
𝑆′⊆𝑆
Ö
𝑢𝑗∈𝑆′
𝑤𝑗
Ö
𝑢𝑗∈𝑆\𝑆′
(1−𝑤𝑗)ΛR(𝑆′)
=

𝑤𝑖·
∑︁
𝑆′⊆𝑆
Ö
𝑢𝑗∈𝑆′
𝑤𝑗
Ö
𝑢𝑗∈𝑆\𝑆′
(1−𝑤𝑗)ΛR(𝑆′∪{𝑢𝑖})
+( 1−𝑤𝑖)·
∑︁
𝑆′⊆𝑆
Ö
𝑢𝑗∈𝑆′
𝑤𝑗
Ö
𝑢𝑗∈𝑆\𝑆′
(1−𝑤𝑗)ΛR(𝑆′)
!
−
∑︁
𝑆′⊆𝑆
Ö
𝑢𝑗∈𝑆′
𝑤𝑗
Ö
𝑢𝑗∈𝑆\𝑆′
(1−𝑤𝑗)ΛR(𝑆′)
=𝑤𝑖·
∑︁
𝑆′⊆𝑆
Ö
𝑢𝑗∈𝑆′
𝑤𝑗
Ö
𝑢𝑗∈𝑆\𝑆′
(1−𝑤𝑗)ΛR(𝑢𝑖|𝑆′).
Let Φ𝑆 denote a random set that independently includes each ele-
ment𝑢𝑗∈𝑆 w.p.𝑤𝑗 . Hence, for any𝑆⊆𝑈 and𝑢𝑖∈𝑈 , Λ𝑊 R(𝑢𝑖|𝑆)
can be rewritten to
𝑤𝑖·
∑︁
𝑅∈R :𝑢𝑖∈𝑅
E[I(Φ𝑆∩𝑅 =∅)]· I(𝑢𝑖 ∉𝑆).
By plugging the above result into Eq.(27), we have
𝜕𝐹𝑊(x)
𝜕x[𝑖] = 𝑤𝑖 1− x[𝑖] ∑︁ 𝑅∈R :𝑢𝑖∈𝑅 E  I(ΦΩ(x)∩𝑅 =∅)· I(𝑢𝑖 ∉ Ω(x)) 
=𝑤𝑖·
∑︁
𝑅∈R :𝑢𝑖∈𝑅
E

I(ΦΩ(x)\{𝑢𝑖}∩𝑅 =∅)

Equivalently, ΦΩ(x)\{𝑢𝑖} is a random set that independently in-
cludes each𝑢𝑗∈𝑈\{𝑢𝑖} with probability x[𝑗]· 𝑤𝑗 . Hence, we can
further derive that
𝜕𝐹𝑊(x)
𝜕x[𝑖] =𝑤𝑖·
∑︁
𝑅∈R :𝑢𝑖∈𝑅
Ö
𝑢𝑗∈𝑅\{𝑢𝑖}
(1− x[𝑗]· 𝑤𝑗)
= 𝑤𝑖
1− x[𝑖]· 𝑤𝑖
∑︁
𝑅∈R :𝑢𝑖∈𝑅
Ö
𝑢𝑗∈𝑅
(1− x[𝑗]· 𝑤𝑗).
This completes the proof. □
