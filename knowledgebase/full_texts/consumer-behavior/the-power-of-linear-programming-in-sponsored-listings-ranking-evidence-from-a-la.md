---
title: 'The Power of Linear Programming in Sponsored Listings Ranking: Evidence from a Large-Scale Field
  Experiment'
url: https://arxiv.org/abs/2403.14862
category: consumer-behavior
subcategory: empirical
date: 2024-03
venue: ''
authors:
- Haihao Lu
- Luyang Zhang
- Yuting Zhu
source: arxiv
pdf_url: https://arxiv.org/pdf/2403.14862
pages: 53
chars: 130743
fetched_at: '2026-11-08T13:14:55+00:00'
kb_version: 1
---

# The Power of Linear Programming in Sponsored Listings Ranking: Evidence from a Large-Scale Field Experiment

The Power of Linear Programming in Sponsored Listings
Ranking: Evidence from a Large-Scale Field Experiment
Haihao Lu ∗ Luyang Zhang † Yuting Zhu ‡
November 13, 2025
Abstract
Sponsored product advertisements constitute a major revenue source for online marketplaces
such as Amazon, Walmart, and Alibaba. A key operational challenge in these systems lies in
the Sponsored Listings Ranking (SLR) problem, that is, determining which items to include and
how to rank them to balance short-term revenue with long-term relevance and user experience.
Industry practice predominantly relies on score-based algorithms, which construct heuristic
composite scores to rank items efficiently within strict real-time latency constraints. However,
such methods offer limited control over objective trade-offs and cannot readily accommodate
additional operational constraints. We propose and evaluate a Linear Programming (LP)-based
algorithm as a principled alternative to score-based approaches. We first formulate the SLR
problem as a constrained mixed integer programming (MIP) model and develop a dual-based
algorithm that approximately solves its LP relaxation within 0.1 second, satisfying production-
level latency requirements. In collaboration with a leading online marketplace, we conduct a
19-day field experiment encompassing approximately 329 million impressions. The LP-based al-
gorithm significantly outperforms the industry-standard benchmark in key marketplace metrics,
demonstrating both higher revenue and maintained relevance. Mechanism analyses reveal that
the performance gains are most pronounced when the revenue–relevance tradeoff is stronger.
Our framework also generalizes to settings with inventory, sales, or fairness constraints, offering
a flexible and deployable optimization paradigm. The LP-based algorithm was deployed in pro-
duction at our partner marketplace in January 2023, marking a rare large-scale implementation
of a mathematically grounded ranking algorithm in real-world online advertising.
Keywords: onlineadvertising, sponsoredlistingsrankings, linearprogramming, latency, revenue-
relevance tradeoff, field experiment
1The authors are listed alphabetically and contributed equally to this work. For confidentiality reasons, the
company’s identity remains anonymous throughout the paper. The authors thank the company for providing the
empirical setting and data. The views expressed in this paper are solely those of the authors and do not necessarily
reflect the views of any affiliated organization. All remaining errors are the authors’ own.
∗MIT, Sloan School of Management (haihao@mit.edu)
†Carnegie Mellon University, Heinz College (luyangz@andrew.cmu.edu)
‡National University of Singapore, NUS Business School (y.zhu@nus.edu.sg)
1
arXiv:2403.14862v4  [econ.GN]  12 Nov 2025

1 Introduction
Sponsored product advertisements constitute a primary revenue stream for most major online mar-
ketplaces, including Amazon, Walmart, and Alibaba. For instance, Amazon and Google reported
$37.7 billion and $224.47 billion in sponsored advertising revenues in 2022, respectively.1 In such
advertising systems, third-party sellers pay additional commission fees to online marketplaces to
increase the visibility of their products, thereby enhancing the likelihood that their items are promi-
nently displayed to consumers.
A particularly prevalent format of sponsored product advertising is the sponsored product listing,
which is typically displayed under aseed product. In this format, promoted items are interleaved
with organically ranked products and may appear in sections such as “Sponsored Related Items,”
“Products Related to This Item,” or “You May Also Like,” with platform-specific variations in ter-
minology. Figure 1 provides an illustrative example from Amazon. Within these listings, both
sponsored and non-sponsored products coexist without predetermined slots reserved for sponsor-
ships. This intermixing introduces substantial complexity to determining which items to include
in the listings and how to optimally rank them, a problem we refer to as theSponsored Listings
Ranking(SLR) problem, which is the primary focus of this study.
Figure 1: Sponsored Product Listings Example
The primary challenge in SLR design lies in managing the trade-off between revenue generation and
relevance. Whiledisplayingmoresponsoredproductscanincreaseshort-termplatformrevenue, such
placements may not align with consumer preferences and could degrade user experience. Hence,
the platform must balance two competing objectives: maximizing revenue while maintaining the
1https://ir.aboutamazon.com/annual- reports- proxies- and- shareholder- letters/default.aspx;
https://abc.xyz/investor/ue
2

relevance and quality of displayed items to sustain long-term consumer engagement. Achieving this
balance requires a principled approach to ranking.
Beyondthisfundamentaltrade-off, thepracticaldesignofSLRalgorithmsinvolvesseveraladditional
considerations. First, in terms of computational efficiency, the algorithm must satisfy stringent la-
tency requirements, typically producing a ranked list within 0.1 seconds to meet real-time display
constraints. Second, with respect to interpretability and tractability, the ranking framework should
embody clear objectives and explicit constraints, allowing the decision-making process to remain
transparent and auditable. Third, the algorithm must be flexible and adaptable, enabling adjust-
ments in objectives, constraints, or weighting schemes to accommodate platform-specific business
goals and varying marketplace contexts.
To address practical considerations, particularly the stringent latency requirement, most industry
solutions to the SLR problem adopt a “predict-then-optimize” paradigm comprising two stages. In
the prediction stage, platforms estimate user action rates, such as click-through rate (CTR) or
purchase-through rate (PTR), which correspond to the prevailing Cost-Per-Click (CPC) and Cost-
Per-Acquisition (CPA) business models. In the optimization stage, the system determines which
sponsored items to display and how to rank them. Our proposed algorithmic solution intervenes at
this optimization stage while keeping the prediction stage identical to that used in industry.
A widely adopted approach for the optimization stage in practice is the score-based ranking al-
gorithm, which assigns each item a composite score based on predefined criteria and ranks items
according to these scores. These algorithms are favored for their computational efficiency, typically
producing rankings within 0.1 seconds to satisfy real-time latency requirements. The scoring criteria
generally integrate multiple objectives, such as predicted consumer action rate, item relevance, and
potential revenue generation. In most implementations, platforms employ a linear combination of
these objectives to construct the score function that best aligns with their business priorities (Liu
et al., 2015; Cheng et al., 2016; Covington et al., 2016; Okura et al., 2017; Zhou et al., 2018).
However, score-based algorithms face several inherent limitations. First, the final ranking quality
depends critically on how the score function is specified, making it difficult for marketplaces to se-
lect an appropriate formulation. Rankings may vary substantially across different scoring functions,
and when the chosen function does not directly represent the underlying economic objectives, the
results can be suboptimal and fail to achieve Pareto efficiency. Moreover, aggregating multiple ob-
jectives into a single composite score provides no explicit control over the performance of individual
objectives. In particular, this approach cannot readily accommodate operational constraints that
marketplaces may wish to impose, such as inventory limits, sales targets, or fairness considerations.
To address these challenges, we propose and examine an alternative approach, referred to as the
Linear Programming (LP)-based algorithm, in this paper. Specifically, we formulate the ranking
problem as a constrained mixed integer programming (MIP) model. Because solving the MIP
exactly is NP-hard, we relax it to a tractable LP formulation. However, even with state-of-the-art
3

solvers, directly solving the LP remains too computationally intensive to satisfy the stringent latency
requirements of online marketplaces. Motivated by these constraints, we develop a dual-based
algorithm that approximately solves the original MIP formulation of the SLR problem within 0.1
second, thereby meeting the platform’s real-time demands. We then validate the proposed approach
through a large-scale field experiment conducted in collaboration with a leading online marketplace
(referred to as Marketplace A for confidentiality). The 19-day experiment, run in April 2022 and
encompassing approximately 329 million impressions, demonstrates that the LP-based algorithm
substantially outperforms the highly tuned industry-standard score-based algorithm, leading to
significant improvements in key marketplace performance metrics.
We further examine the underlying mechanism through which our LP-based algorithm outperforms
the score-based benchmark. The key difference lies in how the revenue–relevance tradeoff is modeled.
Inthescore-basedalgorithm, theindustryconventionistoframethistradeoffasonebetweenorganic
revenueandad revenue(see Section 2 for details on the revenue structure). In contrast, our LP-
based algorithm adopts a more disciplined formulation of the revenue–relevance tradeoff: rather
than separating revenue by source, it maximizes total marketplace revenue subject to a minimum
relevanceconstraint. Empirically, weprovideevidencesupportingthismechanism. Theperformance
gains of the LP-based algorithm are more pronounced precisely when the revenue–relevance tradeoff
is stronger. Furthermore, the algorithm demonstrates advantages in both theitem selectionand
conditional rankingstages, consistently identifying items with higher expected revenue.
Our key contribution lies in developing a new ranking algorithm, the LP-based algorithm, for the
SLR problem, which can simultaneously achieve higher revenue and satisfy the stringent latency
requirements of production environments. We further provide empirical evidence from a large-
scale field experiment demonstrating the superior performance of the proposed approach. To the
best of our knowledge, this paper represents the first empirical study to both document large-scale
experiment evidence and uncover the mechanisms underlying the LP-based algorithm’s advantage
over score-based algorithms. In addition, our LP-based framework has strong modeling flexibility,
enabling it to incorporate additional operational constraints, such as inventory limits, sales targets,
or fairness considerations, within an online optimization setting.
Our proposed algorithm was deployed in production at Marketplace A in January 2023, where it
helps the platform deliver high-value sponsored items to consumers in real time. Notably, score-
based algorithms have long served as the industry standard for sponsored listing and other ranking
problems. Our work, by contrast, introduces a principled and practically viable alternative that
has been successfully implemented in production, demonstrating both theoretical soundness and
real-world effectiveness.
1.1 Literature reivew
This section presents related literature on sponsored listing ranking problems.
4

Ranking in recommendation systemOur work provides an approach for the ranking step
in the recommendation system. In a recommendation system, the first step is to estimate the
conversion rate of displaying the impression by machine learning algorithms, which has been quite
mature and provide reasonable estimations in the online advertising industry (Liu et al., 2015;
Cheng et al., 2016; Covington et al., 2016; Okura et al., 2017; Zhou et al., 2018). After estimating
the conversion rates, online platforms are tasked with developing a ranking model that displays
candidate items to consumers in a designated order, which is the focus of this paper. A majority of
previous studies focus on the score-based ranking model (Zehlike et al., 2022; Renda and Straccia,
2003; Montague and Aslam, 2001; Manmatha et al., 2001), that is, calculating a score for each item
through a customized scoring function, and then selecting the displayed items by ranking the scores.
Whiletherankingalgorithmsaresimilaramongvariousstudies, thescoringfunction, however, might
vary, depending on the objectives of each online platform. For instance, Covington et al. (2016)
deployed a deep neural network model and used logistic regressions to generate scores for each
video content on YouTube. Google Play (Cheng et al., 2016), instead, used only the estimated
conversion rate as the score for each item, therefore, aiming to recommend the most relevant items
to consumers. Netflix (Amatriain, 2013) adopted a score function that linearly combines popularity
and predicted rating for each video. Yang et al. (2019) proposes a linear programming based
algorithm for online advertisement bid, without considering the ranking. As we will introduce
more details in section 2, Marketplace A also utilizes a score-based ranking method whose objective
combines different sources of revenue (Ge et al., 2021). In the case of “cold start”, i.e., the launch
of a new advertisement/item, where the data for conversation rate estimation is limited, Ye et al.
(2023) proposed a bandit algorithm that significantly increased the success rate of cold start in field
experiments.
An inevitable drawback of the score-based method is that even though online platforms aim to
achieve Pareto efficiency over multi-objective (Lin et al., 2019), it is hard to guarantee the perfor-
mance of individual objectives. An alternative approach is to formulate the problem as a mathemat-
ical programming problem, that is, maximizing an objective function while setting constraints on
some other metrics and resources. Such a problem can be formulated as a mixed integer program-
ming (MIP) problem (Celis et al., 2017), and sometimes referred to as an advertisement allocation
problem (Mehta et al., 2013). We can also associate this problem with some well-studied literature
on assignment problem (Ross and Soland, 1975) and knapsack problem (Salkin and De Kluyver,
1975). However, as the number of constraints increases, the MIP also becomes increasingly harder
to solve, requiring various approximation techniques. A more comprehensive review can be referred
to (Cattrysse and Van Wassenhove, 1992; Pentico, 2007; Karp et al., 1990). Particularly, Celis et al.
(2017) considered the ranking problem with fairness constraints. Based on LP relaxation, they re-
covered integral solutions with small constraint violations. Asadpour et al. (2023) studied a ranking
model that aims to maximize consumer engagement for online retail, proposing an algorithm by
LP relaxation and randomized rounding. Further, through LP-relaxation and primal-dual pairs,
Google (Bhalgat et al., 2012) addressed an advertisement allocation problem with nested packing
5

constraints, and then approximated it with an LP-based primal-dual algorithm; Microsoft (Chen
et al., 2011) proposed a bidding algorithm for advertisement allocation with budget constraints.
Inspired by (Chen et al., 2011), Alibaba (Zhang et al., 2018)) developed a similar algorithm for a
global advertisement allocation problem that optimized over accumulated search queries.
It is worth noting that although standard algorithms for advertisement allocation problems are well
established in the existing literature, newly formulated problems with distinct objectives or con-
straints often require tailored adaptations of these paradigms. Our proposed algorithm falls into
this category. Specifically, we develop an efficient approximate algorithm to solve the underlying
mixed integer programming (MIP) formulation, with direct application to the SLR problem. Fur-
thermore, we present the first field study that empirically compares the performance of score-based
and LP-based algorithms.
In the context of recommender systems, the primary design objective is to ensure low latency, that
is, the ability to generate rankings within a strictly limited response time. Consequently, unlike
assortment optimization problems (which we will discuss shortly), ranking problems typically do
not treat item interactions as a central concern. Most studies therefore assume that position weights
(often referred to as “position bias”) are independent of the item assortment (Chen et al., 2023;
Agarwal et al., 2019; Hofmann et al., 2013) and develop methods such as propensity-score-based
estimation to correct for this bias (Chen et al., 2023; Hofmann et al., 2013; Joachims et al., 2017).
Multi-objectives selections and trade-offOur paper also relates closely to the literature that
studies the selection of objectives and trade-offs between muti-objectives. As mentioned earlier,
given the variety of objectives, different online platforms may prioritize them differently. Other
than maximizing revenue, online marketplaces might also need to consider extra objectives such
as consumer utility, ranking relevance (Ghose et al., 2014), algorithm fairness (Geyik et al., 2019),
and content diversity (Chen et al., 2024). For instance, online video platforms such as YouTube or
Netflix emphasized more on ranking relevance (Covington et al., 2016; Amatriain, 2013), while on-
line marketplaces such as Tabao cared more about revenue (Hu et al., 2018). Naturally, each online
marketplace has multiple objectives incorporated into the optimization framework. Agarwal et al.
(2011) jointly optimized for initial clicks and post-click downstream. Xiao et al. (2017) considered
the fairness conflict between individuals and the entire group. Chen et al. (2024) recommended
that social media platforms should focus on increasing content diversification specifically for active
consumers. Contrary to industry assumptions, their research revealed that diversified recommen-
dations would enhance content consumption diversity only among active consumers. Adomavicius
and Kwon (2014) optimized for the aggregated diversity of a group of recommendations. Sumida
et al. (2021) characterized the trade-off between revenue and utility under MNL, by constructing
the objective function as a weighted sum of revenue and utility. Louca et al. (2019) proposed a
similar MNL model optimization framework, weighting the sum of revenue and relevance. Li et al.
(2025) considered a fairness metric evaluated by the click-throughs of different Ads and customer
types. They proposed a two-stage allocation method for online advertisement, which balanced rev-
6

enue and algorithm fairness. However, since the objectives might not always align, Rodriguez et al.
(2012) addressed this issue using constraint optimization. On the other hand, as multi-objective
optimization often resulted in many nondominated solutions and low pressure towards the Pareto
front, Li et al. (2016) developed a stochastic ranking algorithm to tackle this problem.
Assortment problemThe work is also related to the literature studying assortment optimization
problems, whichreferto thechallengeofselectingasubsetof productstoofferfroma largerset, inan
online setting, where the goal is often to maximize revenue or customer satisfaction (Kök et al., 2009;
Caro and Gallien, 2007; Gallego et al., 2020). Differing from ranking problems, assortment problems
focus on studying the interaction among listed items and do not usually study the effect of orders.
In assortment literature, many previous works adopt parametric models to model the purchase
probability of items given a certain set of items, such as theindependent demand model(IDM) and
basic attrition model(BAM) (Gallego et al., 2019). Particularly, IDM assumes that the probability
ofsaleforeachitemisindependentofothers, thustheoptimalassortmentwouldbetheoneincluding
all items with positive revenue. However, IDM might be pessimistic in a way that when items are
running out of stock, recapturing any of those sales to alternate products would be infeasible since
the demands are treated as independent (Gallego et al., 2015). Under BAM, on the other hand, for
a given assortment, the choice probability of each item is normalized by the summation of the utility
of all items in that assortment. The often-usedmultinomial choice model(MNL) is a special case of
BAM (McFadden et al., 1973; Luce, 2005). Under the MNL model with no constraint, Talluri and
Van Ryzin (2004); Gallego et al. (2004) characterized the revenue-ordered property of the optimal
assortment. Further, for the robust assortment optimization under MNL, the optimal assortment is
still revenue-ordered (Rusmevichientong and Topaloglu, 2012). However, in contrast to IDM, BAM
might be optimistic about recapturing the sale of alternative items due to the self-normalization
procedure (Gallego et al., 2015). Feldman et al. (2022) also emperically showed that the MNL model
performed worse during multi-purchase events. Recently, there has been some research studying
the ranking of the assortment of products for online retailing. Ferreira et al. (2022) studied the
ranking of the selected assortment display to consumers. The proposed online learning algorithms
also for maximum consumer engagement, which balanced between learning speed and optimality
gap. As classic choice models for online retailing only gave limited consideration to substitution
patterns, Jiang et al. (2025) proposed a high-dimensional choice as an alternative. Asadpour et al.
(2023) focused on ranking assortment in the form of a submodular maximization problem. They
developed offline approximation algorithms that give the maximum probability of purchases. Most
of the previous works in the assortment literature focused on developing theory guarantees. The
only empirical study we found on online assortment problems is Feldman et al. (2022). They novelly
implemented the algorithm proposed in Rusmevichientong et al. (2010) and presented an empirical
study at Alibaba comparing the multinomial logit model versus industry-level machine learning
models for assortment.
7

2 Institutional Context and Score-Based Ranking
We begin this section by outlining the relevant institutional details of our partner marketplace,
including how sponsored listings rankings and the advertising system operate in Marketplace A. We
then describe the current score-based ranking algorithm employed by Marketplace A.
2.1 Sponsored Listings Rankings (SLR)
Sponsored product advertisements are a major source of revenue for most online marketplaces,
including Amazon, Alibaba, and our partner marketplace. These sponsored products typically
appear in two key locations where they are relevant as aranking problem, which we define as
generating a carefully ordered list that includes both sponsored and non-sponsored products.
The first location is the keyword search results page, where the ranking process is referred as
Keyword Ranking(KR) in our partner marketplace. KR addresses the challenge of displaying and
ranking items based on consumer-entered search queries. For example, when a consumer searches
for a keyword on Marketplace A, a ranked list of relevant items is presented, as illustrated in Figure
2a. The task of determining the order of these listings constitutes the KR problem.
The second common location for sponsored products is the product detail page, which consumers
reach after clicking on a specific product. In this context, sponsored products may appear in sections
such as "Sponsored Related Items," "Products Related to This Item," or "You May Also Like," with
specific terminology varying across platforms. The corresponding display format in Marketplace A
is shown in Figure 2b. The ranking of items in this section, which includes both sponsored and non-
sponsored products, is referred to asSponsored Listings Ranking(SLR) in our partner marketplace
and is the primary focus of our study. The main product featured on the page is typically referred
to as theseed item. As with other marketplaces, Marketplace A notifies users that the listings may
include sponsored items, but does not disclose which specific items are sponsored.
In Marketplace A, as in many similar online marketplaces, the goal of SLR is twofold: to display
relevant items to consumers and to generate substantial revenue. Achieving this dual objective is
a central challenge not only for Marketplace A but also for many of its industry peers. On the
one hand, Marketplace A aims to maximize revenue, with the revenue structure detailed in Section
2.2. On the other hand, the platform places high importance on maintaining a positive consumer
shopping experience, which is crucial for its long-term growth. To support this, more relevant items,
defined as those closely related to theseed item, should be ranked higher in the sponsored listings. A
detailed explanation of how relevance is measured is provided in Section 2.3. Balancing this revenue-
relevance tradeoff is the core task of the ranking phase, particularly under the predict-then-optimize
framework adopted by Marketplace A and widely used across the industry.
Beyond practical constraints, especially the stringent latency requirement, three inherent character-
istics of the SLR problem make ranking a particularly critical and challenging task, similar to those
encountered in recommender systems. First, the number of sponsored items displayed is not fixed.
8

(a) Keyword Ranking
 (b) Sponsored Listings Ranking
Figure 2: Example of Two Ranking Problems in Marketplace A
As discussed in Section 2.3, it can range from zero to the total number of available slots, entirely
determined by the ranking algorithm. Second, there are no fixed display positions reserved for
sponsored items; their placement is dynamically assigned based on the ranking algorithm’s output.
Third, from the consumer’s perspective, sponsored items are not marked with any prominent label,
making them indistinguishable from organic listings. These features contrast sharply with tradi-
tional sponsored ads in keyword search engines like Google. In those systems, ranking is relatively
less central: a small number of fixed, clearly labeled ad slots are shown, and platforms can rely on
simple boosting mechanisms for selected sponsored items without needing to rank all results across
pages. As we will discuss in Section 6, our KR setup also differs from that of Google, which allows
our proposed ranking algorithm to be extended to the KR setting in our context.
In Marketplace A, KR and SLR are managed by separate teams within distinct organizational
units that operate independently, a common practice in large-scale marketplaces. As a result, a
product that appeared in the KR results but was not clicked by consumers may still appear in the
SLR section. There is currently no mechanism in place to prevent this duplication, highlighting a
broader challenge faced by large organizations that rely on algorithmic optimization across siloed
teams. All empirical results reported in Section 5 are based on the SLR. In addition, we provide
empirical evidence on how changes to the SLR can influence outcomes in the KR in Section 5.3.
2.2 Revenue Structure and Advertising System
Revenue from sponsored listings comprises two components: (1) thetake fee(also referred to as
organic revenue) and (2) thesponsorship fee(also referred to asad revenue). For every item sold on
9

the platform, Marketplace A collects a commission, called thetake fee, which is a fixed percentage
of the item’s final sale price. This percentage, known as thetake rate, is tiered and ranges from 3%
to 15%, depending on the item’s category and price.
In addition, sellers may choose to voluntarily sponsor their items by paying an additional fee to
boost visibility. This fee is calculated as a percentage of the final sale price and is referred to as the
ad rate. Marketplace A employs a bidding system for setting thead rate: sellers specify a bid as a
percentage of the sale price when setting up a sponsored product, with allowable bids ranging from
1% to 100%. While sellers have the flexibility to choose any bid within the allowable range, the
effectiveness of their sponsored product (i.e., its visibility and ranking) depends on how competitive
their bid is relative to the trending rate.
Importantly, Marketplace A adopts a cost-per-acquisition (CPA) model, in which thesponsorship
feeis charged only when a product is purchased through a sponsored listing. While our discussion
focuses on the SLR setting, it is worth noting that the same revenue structure, including thetake
rateandad rate, also applies to the KR setting.
We make two clarifying notes. First, the revenue structure, comprising bothorganic revenueand
advertising revenue, is widely adopted by major marketplaces such as Amazon and Alibaba. Accord-
ingly, the fundamental revenue–relevance tension inherent in the SLR problem is broadly applicable.
Second, under this revenue structure, consumers are not constrained to purchase only one item from
the sponsored listing. The final goal is to maximize revenue while maintaining relevance and quality
of displayed items to sustain long-term consumer engagement.
2.3 Score-Based Ranking
Score-based ranking refers to ordering listed items according to the monotonic sequence of a certain
score defined by the marketplace. Owing to its simplicity and computational efficiency, score-based
ranking is one of the most widely adopted ranking algorithms in both recommender systems and
sponsored listings operating under the predict-then-optimize paradigm. The core of this approach
lies in how the score is defined. At Marketplace A, score-based ranking is the production model
used for sponsored listings, and the engineering team has conducted extensive research to refine
the score definition for improved performance. In this section, we present the high-level concept
of the score-based ranking algorithm implemented at Marketplace A, which serves as the baseline
for comparison with our proposed LP-based algorithm in the field study. Along the way, we also
outline the predict-then-optimize process employed by Marketplace A and identify the specific step
at which our LP-based algorithm intervenes.
When a consumer opens a webpage with aseed item, Marketplace A first selects a collection of
qualified candidate items. From now on, we use the setN={1,2, ..., n}to denote this collection.
The number of candidate itemsnranges from 1 to 500, as some categories in Marketplace A are
well-stocked with many similar items, while others in the long tail have far fewer. Meanwhile, to
10

avoid the overwhelming number of candidate items, Marketplace A restricts the cardinality ofN
during the selection phase. Then, Marketplace A is tasked to (1) choose a subset ofNaccording
to the slot numberm(m≤n)and then (2) display this subset of items in ranked order. The slot
numbermtypically ranges from 1 to 50. Consistent with the problem setup and the stringent
latency requirements, Marketplace A implemented its SLR procedure through three main stages:
(1) candidate selection, (2) purchase-through rate estimation, and (3) ranking, as detailed below.
Step 1: candidate selection.Among all the items listed on Marketplace A, there is only a small
number of items that are related to theseed itemand thus are potential candidates for the SLR. The
first step is to identify candidate setN. Here, Marketplace A takes two separate approaches. One is
based on the categories ofseed item, and the other is developed from consumers’ history. Each listed
item has been pre-labeled with various categories and sub-categories, spanning multiple layers. The
first group of candidate items is determined by their categorical similarity to theseed item. For
the second group, Marketplace A trains thek-nearest neighbors(KNN) algorithm featured on each
consumer’s browsing and purchase history to select the related items. Eventually, the union of the
first and the second group will formulate the candidate set. As observed in the candidate selection
stage, the sponsored items can be either complements to theseed item(selected based on the user’s
browsing history) or substitutes for theseed item(selected from the same product category).
Step 2: purchase-through rate (PTR) and position weights estimation.Aligned with
common practice in recommender systems, Marketplace A separates the estimation of the conversion
rate, namely, thepurchase-throughrate(PTR),denotedasr j ∈R, andthepositionweights, denoted
ash i ∈R, from the ranking problem due to latency considerations. In other words, Marketplace
A follows the predict-then-optimize paradigm. For the same practical reasons, and consistent with
many online marketplaces, a key underlying assumption in solving the SLR problem is that the
probability that a consumer clicks on itemjat positionican be decomposed asr jhi, thereby
treating the position weights as independent of the assortment of items. In our study, we take all
these estimates as given and intervene only at the ranking stage, which we introduce shortly.
Because Marketplace A adopts a cost-per-acquisition (CPA) model, the key performance metric is
the PTRrj. Specifically, Marketplace A first generates an offline PTR estimate for each itemj∈N,
which is then refined using a fine-tuned XGBoost model. This adjustment leverages consumers’
browsing and purchase histories, as well as characteristics of theseed itemand other candidate
items inN, including category, price, and sales history. Importantly,rj may vary across impressions
for the same itemj, depending on the specific consumer, theseed item, and the other items in the
candidate set. An impression refers to an instance in which a user visits a webpage displaying a
designatedseed itemalong with a sponsored listing. If the user clicks on a product within the
sponsored listing and then returns to the originalseed itempage, the sponsored listing remains
unchanged, and all such activities are considered part of the same impression. In our partner
marketplace, PTR also serves as a proxy for the relevance of a sponsored item to theseed item,
11

as it captures the organic purchase likelihood conditional on theseed item2. The PTR estimation
process also accounts for both the relationship with theseed itemand potential cannibalization
among items within the sponsored listing. This design reflects a deliberate balance between the
latency constraints of real-time operations and the underlying economic relationships among items.
Another important estimation component is the position weightshi, which capture the slot-specific
probability that a purchase originates from positioni, independent of the item displayed. These
weights are empirically estimated through randomized shuffling and A/B testing. In our empirical
analysis, we focus on the desktop website channel, where position weights are fixed across impres-
sions. As expected, the top slots exhibit higher weights than lower ones, and the weights drop
sharply once the slot moves to the next page.
Step 3: score-based ranking.In the final step, Marketplace A computes a score for each
item, ranks the items based on these scores, and selects those with the highest scores for display.
Consequently, not all items in the candidate set appear in the sponsored listing. The number of
displayed items is not fixed but determined by Marketplace A’s internal rules. As a result, some
sponsored listings may contain no sponsored products, while others may include many.
More specifically, the scoresj for thej-th item is defined as a weighted sum of the expectedorganic
revenue(PTR×take rate×price) and the expectedad revenue(PTR×ad rate×price) with the
following form:
sj =r j ×t j ×p j +w×r j ×ad j ×p j,(1)
wherep j denotes the price of the item. The termt j denotes thetake rateof the item, which is
the commission levied by Marketplace A upon the sale of the item, with a predetermined rate for
each item category within the marketplace. Theorganic revenuereflects the mandatory platform
fee paid by the marketplace for each transaction. The termadj ∈R >0 denotes thead ratefor the
j-th item, namely, the amount a vendor is willing to pay for increased item visibility. The process
for determiningad j is detailed in Section 2.2. Thead revenue, in contrast toorganic revenue, is a
discretionary vendor expense aimed at boosting product prominence.
The parameterw∈R + governs the relative importance oforganic revenueversusad revenue. It is
optimized at the impression level based on factors including the predicted PTR, position weights,
ad rates, and item prices. The method for optimizingwis detailed in Ge et al. (2021). Notably,
the selection of the scoring function and the calibration ofwhas gone through extreme tuning at
Marketplace over an extended period, and we believe their production model optimally harnesses
the power of the score-based algorithm.
2This relevance measure is widely used by our partner marketplace and closely resembles the quality score in
Google Ads, which assesses the relevance of an ad and its landing page to a user’s search query:https://support.
google.com/google-ads/answer/6167118?hl=en. Decomposing the purchase path in a sponsored listing, the final
PTR reflects three main components: the expected click-through rate (CTR), the relevance of the item to the user’s
latent purchase intent, and the quality of the landing product page. A key assumption in using PTR as a relevance
score is that a click on theseed itemreflects the user’s latent purchase intention.
12

Next, we will propose an alternative ranking approach based onlinear programming(LP) to solve
the SLR. Note that the first two steps, candidate selection and PTR and position weights estimation,
remain unchanged. Our contribution lies in introducing a new method for the final ranking stage.
3 Linear Programming (LP)-Based Ranking Algorithm
In this section, we first formulate the SLR problem as amixed integer programming(MIP) model.
However, solving this MIP exactly is computationally infeasible under the platform’s latency con-
straints. We therefore propose a primal–dual algorithm to solve its LP relaxation, which produces a
feasible and near-optimal solution to the original MIP. We then describe the production algorithm
implemented by Marketplace A, a practical variant of our primal–dual algorithm, that enforces
the relevance constraints in expectation rather than at each impression, and present its associated
theoretical guarantee. Finally, we provide a theoretical explanation for why our LP-based approach
can outperform the conventional score-based algorithm.
3.1 Mixed-Integer Programming (MIP) Formulation for the SLR Problem
Suppose we havencandidate items designated to be assigned tomslots(m≤n). For each sloti,
we have the knowledge of its estimated position weighthi, which represents the importance of the
i-th slot. In general, the customer is more likely to buy the items at the first few slots than the latter
ones, and such differences among slots are measured byhi. Additionally, for each itemj, we take the
estimates: (1) the relevance to theseed item,rj, measured by the PTR, and (2) expected revenue
vj as the sum of expectedorganic revenueandad revenueas we defined previously from equation
(1), i.e.,v j :=r jpj(tj +ad j). Denote the vectors asv:= (v 1,· · ·, vn),r:= (r 1,· · ·, rn),h:=
(h1,· · ·, hm).
Without loss of generality, we assume that position weightsh i are sorted in descending order;
namely, the item at the slot with a smaller index is more likely to be purchased than the same item
at a slot with a larger index.
Assumption 1(Monotonically decreasing position weights).The position weightsh i is sorted in
descending order, i.e.,hi ≥h i+1.
In the MIP formulation, we aim to maximize the expected total revenue while posing a lower bound
on the overall relevance level. The binary decision variableX⊆ {0,1}m×n represents a ranking
plan, namely, an itemjis assigned to slotiwhenX ij takes the value1, or0if not. As a feasible
ranking plan satisfies Pm i=1 X ij ≤1(i.e., each slot can only have one candidate), Pn j=1 X ij ≤1
(i.e., each candidate can only be shown at most once), andXij ∈ {0,1}(i.e., the decision variable
is binary). For notational convenience, we denote
P=


X:
mX
i=1
X ij ≤1∀j,
nX
j=1
X ij ≤1∀i,X ij ∈ {0,1}


 ,(2)
13

as the feasible region of a ranking. Furthermore, we can compute the maximal overall relevance as
a= max
X∈P



mX
i=1
nX
j=1
hirjX ij


 .(3)
ais the maximal possible relevance a ranking can achieve. That is, when the ranking is based
solely on the relevance (PTR) of an item to theseed item, without accounting for revenue from
sponsored products, the maximum achievable relevance score corresponds to the highest possible
ranking outcome. In the MIP formulation, we aim to find a ranking that maximizes the revenue
while making sure that the overall relevance is at leastλtimes the maximal overall relevance with
a pre-determined parameterλ∈[0,1]:
(P0) max X
mX
i=1
nX
j=1
hivjX ij (4)
s.t.
mX
i=1
nX
j=1
hirjX ij −λa≥0(5)
X∈P.(6)
Notice that the MIP formulation is always feasible, because the ranking that gives the maximal
overall relevance store is a feasible solution. Additionally, withλdecreases, the feasible region ofP0
is monotonically enlarged. Since a smallerλwill induce a possibly lower relevance value but higher
revenue, the trade-off between revenue and relevance is fulfilled by the parameterλ.
We highlight several key assumptions in our model setup. First, we assume that the position
weighth i is independent of the PTR. While this independence may not hold universally across all
sponsored listings, the assumption is motivated by the need for low-latency response times. This
simplification is commonly adopted in industry practice (Chen et al., 2023). Second, while our
ranking stage does not explicitly account for interactions among items in a sponsored listing due
to latency considerations, we address potential dependencies through PTR estimation. That is,
the estimated PTR for each item can depend on the overall assortment of items in the sponsored
listing. However, the position weighthi remains fixed and is not influenced by the assortment. This
setup reflects a deliberate design choice: we aim to capture item interactions during prediction stage
rather than the optimization stage. Third, our model allows for the possibility that a consumer
purchases multiple items from a single sponsored listing. This flexibility is consistent with platform
objectives, as multiple purchases do not negatively impact the platform, sellers, or consumers. In
practice, our partner marketplace data show that, among sponsored listings that led to purchases,
most involved only one item, and the maximum number of items purchased from a single listing
was four.
14

3.2 Linear Programming (LP) Relaxation and an Efficient Algorithm
A challenge of the real-time SLR problem is the latency requirement, which needs to be finished
within 0.1 second in general. This poses a strict limitation for obtaining a ranking policy, preventing
us from exactly solving MIP. Indeed, the traditional Branch-and-Bound/Branch-and-Cut method
for solving MIP costs excessively long and unstable time that the marketplace cannot afford. In
such cases, a typical approach is to look at and solve its LP relaxation. Unfortunately, the state-of-
the-art commercial LP solvers can still not solve the LP relaxation within the latency requirement
(see Appendix A.1 for a computational study). Here, we present a linear time dual-based bisection
algorithm that finds a feasible and approximately optimal MIP solution.
We start with presenting the LP relaxed version of MIP, by relaxing the binary variable constraint
X ij ∈ {0,1}toX ij ∈[0,1]:
(P1) max X
mX
i=1
nX
j=1
hivjX ij (7)
s.t.
mX
i=1
nX
j=1
hirjX ij −λa≥0(8)
X∈F,(9)
where
F=


X:
mX
i=1
X ij ≤1∀j,
nX
j=1
X ij ≤1∀i,X ij ∈[0,1]


 .(10)
Algorithm 2 presents our major algorithm. The basic idea of the algorithm is to do a bisection
search for the optimal dual variable to the constraint (8), and then obtain the corresponding primal
response that gives an approximate solution to the LP formulation. More specifically, the algorithm
has the following three steps:
Algorithm 1:PrimalResponse(δ, m)
Input:δ, m.
Output:X∈F⊆R m×n.
Sort the value ofδin the descending order, i.e.,δj1 ≥ · · · ≥δjn. 3
ComputeX, such thatX 1j1 =X 2j2 =· · ·=Xmjm = 1, andX ij = 0elsewhere.
ReturnX
Step 1: Check if the relevance constraint is redundant
Givenh,v,r, we could first easily verify whether the relevance constraint (5) is redundant. Re-
moving (5), the optimal value ofP0 would bemax X∈F {Pm i=1 Pn j=1 hivjX ij}. Similar to the way
3In the case of a tie, we can break the tie by lexicographical order. This ensures a unique output of the function
PrimalResponse for any given input.
15

of obtaininga, due to the unimodularity property, we can obtain the optimal solution by (1) first
sorting the vectorvin descending order, i.e.,v j1 ≥ · · · ≥vjn, and (2) setXiji =· · ·=Xmjm = 1
andX ij = 0elsewhere. Also, we can see thatX∈P.
If Pm i=1 Pn j=1 hirjX ij ≥λa, it means that the ranking that generates the maximum revenue is also
feasible toP0, indicating that the relevance constraint (8) is redundant andXis an optimal solution
toP 0. Then, the algorithm ends, and an optimal solution to the LP and MIP formulation is found.
Step 2: Obtain a range of the optimal dual variable
Let us consider the following primal-dual form ofP1, denoted asD1:
(D1) min µ≥0 D(µ) := max X∈F
mX
i=1
nX
j=1
hiX ij(vj +µr j)−µλa .(11)
Denoteδ:= (δ 1,· · ·, δn), whereδ j =v j +µr j. We denote the optimal value ofD1 as OPTD, and
an optimal dual variable isµ∗.
Suppose that constraint (8) is not redundant, then it follows from complementary slackness that
µ∗ >0. The second step of Algorithm 2 is to find an upper and lower bound onµ∗.
Notice that for any givenµ, one can solve the inner maximization problem overXin (11) by a
simple ranking-based algorithm (see Algorithm 1), and we denote the solutionX(µ). Furthermore,
we know thatX(µ)gives a sub-gradient ofD(µ)by
mX
i=1
nX
j=1
hirjX ij(µ)−λa∈∂D(µ).(12)
Notice thatD(µ)is a convex function and0∈∂D(µ ∗). Furthermore, due to the feasibility of the
constraint (8), we know there exists a large enough finiteµ, such that its sub-gradient is strictly
positive. Thus, we can obtain an upper-boundµ+ ≥µ ∗ by iteratively doubling the value ofµ+ and
checking its corresponding sub-gradient. We can also obtain a lower boundµ− ≤µ ∗ during this
process.
Step 3: Obtain a near-optimal dual solution and a feasible rankingWhen a lower bound
µ− and an upper boundµ + ofµ ∗, we can do a bisection search forµ∗ tillµ + −µ − ≤ϵ, whereϵ
is the target accuracy. Then it is easy to check that the primal response ofµ+ is a feasible and
near-optimal solution toP0. Eventually, Algorithm 2 outputs the primal response ofµ+.
The only parameter in our LP-based algorithm is the relevance parameterλ. We provide guidance
on how to fine-tune this parameter in Appendix A.2.
16

Algorithm 2:LP-based method
Input:h,r,v, λ, a, ϵ,m.
▷Step 1: check if the relevance constraint (5) is redundant.
ComputeX=PrimalResponse(v, m).
if Pm i=1 Pn j=1 hirjX ij −λa≥0then
returnX
else
▷Step 2: find the range containingµ∗.
µ− = 0, µ+ = 1
Computeδ=v+µ +r.
ComputeX=PrimalResponse(δ, m).
while Pm i=1 Pn j=1 hirjX ij −λa <0do µ− =µ +,µ + = 2µ+
Computeδ=v+µ +r.
Computex=PrimalResponse(δ, m).
end
▷Step 3: findµ ∗.
whileµ + −µ − > ϵdo
µ= µ++µ− 2
Computeδ=v+µr.
ComputeX=PrimalResponse(δ, m).
if Pm i=1 Pn j=1 hirjX ij −λa≥0then µ+ =µ
else
µ− =µ.
end
end
Computeδ=v+µ +r.
ComputeX=PrimalResponse(δ, m).
returnX
end
17

3.3 Production Variant of the LP-Based Algorithm and Theoretical Guarantee
The original algorithm described in Algorithm 2 guarantees strictly feasible ranked listings, that is,
every impression satisfies the relevance constraint. In practice, however, Marketplace A does not
require each individual impression to strictly meet the relevance constraint. Instead, it is acceptable
for the constraint to hold in expectation, allowing for higher overall revenue.
To address this production need, we introduce a variant of Algorithm 2, presented as Algorithm 3,
which is used in our field experiment. This new algorithm retains the same primal-dual structure
but modifies how the ranked listing is constructed. Specifically, in addition to the feasible solution
from Algorithm 2, we compute an infeasible (with a minor gap) but revenue-optimal solution using
a relaxed dual variableµ− (withX=PrimalResponse(v+µ −r, m)), where the relevance score of
this listing may fall slightly below the required thresholdλa.
Finally, Algorithm 3returns a randomized solution sampled from the feasible and infeasible solutions
such that the expected relevance constraint is satisfied, while achieving higher expected revenue.
This randomized strategy is provably both feasible in expectation and optimal under the relaxed
constraint. Before we prove this, we first introduce some assumptions.
First, we assume that in SLR setting, there exists no degeneracy:
Assumption2(Nondegeneracy).For an index setI:={(j, k) :j∈[m]ork∈[m], j̸=k, r k ̸=r j},
we defineµ jk := vj −vk rk−rj for all pairs(j, k)∈I. Then for any given vectorv,rin our SLR problem
P0, and a pair of indicies(j, k)∈I, we define the pairwise indifference value
µjk := vj −v k rk −r j ,(13)
and its collection as{µ jk }(j,k)∈I. Then for any two distinct unordered pairs(j, k)̸= (p, q)with
(j, k),(p, q)∈I, we assume thatµjk ̸=µ pq. It is noted thatµjk is a value such that there might be
some “ties” in the vector ofv+µ jk r, i.e.,v j +µ jk rj =v k +µ jk rk.
Notice that both valuesvand relevancerare learned from a machine learning model, thus one can
view they come from a continuous distribution. As a direct consequence, it is with probability 1
that nondegeneracy holds.
Theorem1(OptimalityoftheapproximatedsolutionofAlgorithm3).Under Assumptions 1 and 2,
we define the smallest distance between all pairs of indifference values as
∆min(r,v) := min (j,k),(p,q)∈I,(j,k)̸=(p,q) |µjk −µ pq|.(14)
Let ˜Xbe the randomized solution returned by Algorithm 3 with the bisection toleranceϵ <∆min(r,v),
andX LP be the optimal solution to the relaxed primal problemP1. Then, in expectation, ˜Xequals
18

Algorithm 3:A variant of LP-based algorithm in production
Input:h,r,v, λ, a, ϵ,m.
▷Step 1: check if the relevance constraint (5) is redundant.
ComputeX=PrimalResponse(v, m).
if Pm i=1 Pn j=1 hirjX ij −λa≥0then
returnX
else
▷Step 2: find the range containingµ∗.
µ− = 0, µ+ = 1
Computeδ=v+µ +r.
ComputeX=PrimalResponse(δ, m).
while Pm i=1 Pn j=1 hirjX ij −λa <0do µ− =µ +,µ + = 2µ+
Computeδ=v+µ +r.
Computex=PrimalResponse(δ, m).
end
▷Step 3: findµ ∗.
whileµ + −µ − > ϵdo
µ= µ++µ− 2
Computeδ=v+µr.
ComputeX=PrimalResponse(δ, m).
if Pm i=1 Pn j=1 hirjX ij −λa≥0then µ+ =µ
else
µ− =µ.
end
end
Computeδ + =v+µ +r.
Computeδ − =v+µ −r.
ComputeX + =PrimalResponse(δ +, m).
ComputeX − =PrimalResponse(δ −, m).
▷Step 4: randomized return.
U=Uniform(0,1).
α= ( Pm i=1 Pn j=1 hirjX +,ij −λa)/( Pm i=1 Pn j=1 hirjX +,ij − Pm i=1 Pn j=1 hirjX −,ij).
ifU > αthen
returnX +
else
returnX −
end
end
19

toX LP, namely, the output solution in expectation is the optimal solution to the LP:
E[ ˜X] =X LP,E[Rel( ˜X)] =λa,E[Rev( ˜X)] =OPT LP.(15)
Proof of Theorem 1 is provided in Appendix A.3.
Remark3.1 (Runtime Complexity of Algorithms 2 and 3).Defineµ max := max(j,k)∈I{µjk }. Then
the runtime complexity of Algorithms 2 and 3 are the same and both depends on three domi-
nant components: (1) sorting and selection from Algorithm 1 withO(nlogm)per each step, (2)
step 2 (finding the range containingµ ∗) withO(log(1 +µ max)), and (3) step 3 (findµ ∗) with
O(log(µmax/ϵ)). Thus the overall runtime complexity isO((log(1 +µmax) + log(µmax/ϵ))·nlogm) =
O(nlog(µ max/ϵ) logm), which is a nearly-linear-time algorithm inn.
3.4 Why the LP-Based Algorithm Outperforms the Score-Based Algorithm
The central challenge in our setting is the revenue–relevance tradeoff. If advertising revenue were
absent, the marketplace’s objective would be straightforward: promote items consumers are most
likely to purchase, thereby maximizingorganic revenue. However, because advertising contributes
substantially to marketplace revenue, prioritizing sponsored items does not necessarily align with
consumer preferences. The tradeoff, therefore, reflects a fundamental tension: displaying more
sponsored items increases marketplace revenue but may reduce relevance if those items are less
likely to be purchased.
In the score-based algorithm, the industry convention is to treat this as a tradeoff betweenor-
ganic revenueandad revenue. As expressed in Equation 1, the balancing is achieved through the
parameterw, which adjusts the weight assigned to ad-related factors. In contrast, our LP-based al-
gorithm adopts a different perspective and modeling approach. Rather than distinguishing revenue
sources, we treat the marketplace’s objective as maximizing total revenue (Equation 4), regardless of
whether it arises from organic purchases or advertisements. We incorporate the relevance dimension
explicitly by imposing a minimum requirement, controlled by parameterλ. This framing captures
the idea that marketplaces often set hard constraints on consumer experience, ensuring a minimum
relevance threshold, while still aiming to maximize overall revenue. Crucially, our approach also de-
livers an LP solution that satisfies latency requirements, enabling practical deployment. Section 5.2
will provide empirical evidence on why this approach can outperform the score-based algorithm and
illustrate how the revenue–relevance tradeoff plays out in practice.
Several clarifications are in order. First, both our proposed algorithm and the score-based algorithm
incorporate slot-specific weightshi. As described in Section 2.3, the parameterwin the score-based
method is optimized at the impression level, accounting for predicted PTR, position weights, ad
rates, and item prices (see Ge et al. 2021 for details)4. Second, in designing our field experiment, we
4Our modeling idea could, in principle, be expressed in a score-based framework asδj =r j ×t j ×p j +r j ×
adj ×p j +µ×r j, whereµis the dual variable associated with the relevance constraint. We nonetheless prefer the
20

deliberately adopted a conservative test strategy. Specifically, whilewin the score-based algorithm
is optimized at the impression level, ourλis applied globally across all impressions. To ensure a fair
and conservative benchmark, we setλabove the average relevance level achieved by the score-based
algorithm in pre-experiment data. This design allows us to test whether our LP-based approach
can improve both revenue and relevance through a more principled formulation of the tradeoff.
4 Field Experiment Design and Data
To showcase the effectiveness of the LP-based algorithm, we conduct a randomized field experiment
in Marketplace A to evaluate its empirical performance. This section first outlines the experiment
design, followed by a description of the data used in our analysis.
4.1 Experiment design
We conducted a 19-day randomized field experiment from April 27 to May 16, 2022, to evaluate the
empirical performance of the proposed LP-based algorithm on Marketplace A’s platform across four
major countries. Marketplace A operates four primary consumer access channels: desktop website,
iOS app, Android app, and mobile website. The experiment was implemented on the desktop
website channel ("dWeb"), which generates the highest consumer traffic among all channels. As
discussed in Section 2.3, because our experiment focuses on a single channel, the slot-specific weights
hi keep the same across all impressions in both the treatment and control groups. The benchmark
was the score-based algorithm described in Section 2.3, which served as Marketplace A’s production
model during the study period. Introduced in 2020, the score-based algorithm had undergone
extensive experimentation and hyperparameter tuning, and the version deployed in our experiment
is considered to have reached its full optimization potential.
We considered two treatment groups for the proposed LP-based algorithm, differing in the relevance
parameterλ. Following the parameter tuning approach described in Section A.2, we selectedλ∈
{0.9,0.95}for the field study. Both values exceed the average relevance scores achieved by the
score-based algorithm in the pre-experiment data. This choice reflects a conservative test design
aimed at examining whether the LP-based algorithm can deliver revenue gains while simultaneously
improving the relevance of sponsored listings. Specifically, we implemented the following three
experiment conditions:
1.LP90 (Treatment 1):For consumers assigned to this group, the displayed listings will be
generated by the LP-based algorithm with hyperparameterλ= 0.90.
2.LP95 (Treatment 2):For consumers assigned to this group, the displayed listings will be
generated by the LP-based algorithm with hyperparameterλ= 0.95.
LP-based formulation because it naturally accommodates hard constraints on relevance, consistent with marketplace
goals of safeguarding consumer experience and long-term performance, while still maximizing revenue subject to
those constraints. Moreover, the LP-based formulation possesses the modeling flexibility to accommodate additional
constraints and can be effectively applied in an online setting.
21

3.Benchmark (Control):For consumers assigned to this group, the displayed listings will be
generated by the score-based algorithm.
During the 19-day experiment, each consumer visiting the sponsored listings page was randomly
assigned to one of the three groups, with listings generated according to the assigned method.
Assignment was based on unique consumer IDs, ensuring that each consumer consistently received
the same treatment throughout the experiment, regardless of the number of visits.
4.2 Data
During the 19-day period, our field experiment involved in total 32,058,321 consumers, of which
10,686,419 consumers were assigned toLP90 (Treatment 1), 10,689,158 consumers were assigned
toLP95 (Treatment 2), and 10,682,744 were assigned toBenchmark (Control). During the
experiment period, it is likely that each consumer pays multiple visits, generating many impressions.
As a result, in total, 329 million impressions were generated. Specifically, 109,868,303 impressions
were assigned toLP90 (Treatment 1), 109,843,211 impressions were assigned toLP95 (Treat-
ment 2), and 109,567,246 impressions were assigned toBenchmark (Control).
The randomization check results are presented in Table 1. We examine three key variables, calcu-
lated using data from the three months preceding the experiment launch: (1) the average number of
purchases per consumer (Purchases); (2) the total expenditure (USD) per consumer (GMV); and
(3) the total revenue generated for the partner marketplace (USD) per consumer (Revenue). Due to
confidentiality agreement, exact values cannot be disclosed; instead, we normalize the benchmark to
one and report all other values relative to this benchmark. We also provide the minimum pairwise
p-value across all group comparisons. The results confirm that the randomization was successful.
Table 1:Randomization Check.
LP90 LP95 Benchmark Mininum Pairwise P-value
(Treatment 1) (Treatment 2) (Control)
Purchases 1.00 1.00 1.00 0.99
GMV 1.01 1.02 1.00 0.22
Revenue 1.00 0.98 1.00 0.94
Observations 10,686,419 10,689,158 10,682,744 -
The dataset provided to us consists of three components. The first comprises aggregated results
from the full-scale experiment, including: (1) the average number of purchases per consumer for
each group (Purchases); (2) the total expenditure (USD) per consumer for each group (GMV);
(3) the total revenue generated for the partner marketplace (USD) per consumer for each group
(Revenue); and (4) the average transaction price per consumer among those who made at least
one purchase during the experiment for each group (Transaction Price). All of these measures only
document the activities from the SLR. We use this data to evaluate the effectiveness of our proposed
LP-based algorithm in Section 5.1.
22

Because of the vast scale of the full dataset and practical restrictions related to data privacy, the
partner marketplace was unable to provide us with impression-level data for the entire experiment.
Instead, we were given a randomly sampled subset of the full-scale experiment, comprising 690,611
impressions per experiment group and 2,071,833 impressions in total. Recall that an impression
refers to an instance in which a user visits a webpage displaying a designatedseed itemalong
with a sponsored listing. For each impression, we observe several variables: the average product
price in the sponsored listing, the average normalized PTR weighted by position weights, the total
number of clicks, the number of purchases, the corresponding revenue generated for the partner
marketplace, the date of the impression, and the experiment group assignment. Summary statistics
for this sample are reported in Appendix A.4. Notice that the consumer ID of each impression was
not provided to us for this sample. Although the data are randomly sampled, there remain some
performance differences between the sampled dataset and the full dataset, which we will further
discuss in Section 5. We primarily use this dataset to analyze the mechanisms through which our
proposed LP-based algorithm achieves superior performance. As we will show, the core advantage
of our modeling approach in balancing the revenue–relevance tradeoff remains robust.
To complement our mechanism analysis, the third dataset consists of a random sample drawn
from the 17 days preceding the launch of the field experiments, containing 266,003 impressions and
13,370,159 unique items. Unlike the random sample obtained during the experiments, this dataset
provides richer detail at the item level. For each impression, we can observe the price, thetake rate,
thead rate, the normalized PTR, and the ranking for each item in the candidate set. In addition,
the data documents whether an item appeared in the final sponsored listing, whether a consumer
clicked on or purchased a specific item in the listing, as well as the price and revenue of theseed item,
the seller ID, and the consumer ID. A distinction is that, whereas the field experiment data only
covers registered users with user IDs (which enable randomization), this pre-experiment sample may
include impressions without user IDs. Specifically, 164,737 impressions are from 160,694 registered
users, while the remaining 101,266 impressions are from unregistered users. Summary statistics for
this dataset are provided in Appendix A.4.
5 Field Experiment Analysis and Results
This section reports our empirical analysis and principal findings. We first assess the effectiveness
of the proposed LP-based algorithm using the key outcome variables defined by the partner market-
place (Section 5.1). We then examine the mechanisms underlying its superior performance relative
to the score-based algorithm (Section 5.2). Finally, we consider additional factors pertinent to the
generalizability and limitations of the experiment results (Section 5.3).
5.1 Does LP-Based Algorithm OutPerform the Score-Based Algorithm?
We evaluate algorithmic effectiveness in the partner marketplace using three outcome variables, as
defined in Section 4.2: (1) the average number of purchases per consumer (Purchases); (2) total
23

expenditure per consumer (GMV); and (3) total revenue generated for the partner marketplace per
consumer (Revenue). The main results are reported in Table 2. Due to confidentiality agreement,
we report only the relative changes of the two treatment groups (LP90andLP95) under the
proposed LP-based algorithm compared with the control group (Benchmark), i.e., the score-based
algorithm. All monetary values are calculated in USD. We also present the corresponding p-values
from pairwise t-tests.
Table 2: LP-Based Algorithm vs Score-Based Algorithm.
LP90 LP95
(Treatment 1) (Treatment 2)
Purchases1.55%*** (<0.001) 3.22%*** (<0.001)
GMV1.39% (0.11) 2.96%*** (<0.001)
Revenue1.80%** (0.03) 0.81% (0.32)
Notes. We report the relative changes of the two treatment groups
(LP90andLP95) compared with control group (Benchmark),
i.e., the score-based algorithm. Associatedp-values from pairwise
t-tests are reported in parentheses. The sample size in Treatment
1 isN treatment1 = 10,686,419, in Treatment 2 isN treatment2 =
10,689,158, and in the Control group isNcontrol = 10,682,744. ***
p <0.01, **p <0.05, *p <0.1.
First, intermsofconsumerpurchases, theLP95treatmentleadstoastatisticallysignificantincrease
of 3.22% (p <0.001), while theLP90treatment yields a smaller but still significant increase of
1.55% (p <0.001). This suggests that the LP-based algorithm is more effective at stimulating
demand and generating additional consumer transactions than the score-based algorithm.
Second, with respect to GMV, theLP95treatment yields a statistically significant increase of
2.96% (p <0.001), whereas theLP90treatment shows only a modest increase of 1.55%, which is
statistically insignificant. Recall that the relevance parameterλis higher inLP95. The stronger
performance ofLP95relative toLP90highlights the importance of a sufficiently stringent relevance
threshold in driving consumer spending compared with the score-based algorithm. Importantly, the
improvements in GMV are not attributable to changes in transaction prices: the relative changes
in average transaction price are small and statistically insignificant for both treatments (LP95:
–0.23%;LP90: –0.20%). This pattern suggests that the gains in GMV arise primarily from higher
purchase volumes rather than higher prices, and that such volume-driven growth materializes only
when the relevance threshold is sufficiently high.
Finally, with respect to marketplace revenue,LP95produces only a modest and statistically in-
significant gain of 0.81% (p= 0.32), whereasLP90generates a statistically significant increase
of 1.80% (p= 0.03). Taken together with the GMV results, this suggests that higher consumer
spending does not necessarily translate into higher marketplace revenue, in part because revenue
also depends on advertising income. These patterns point to a relevance–revenue tradeoff: while a
higher relevance threshold (LP95) enhances consumer spending, it does not substantially increase
marketplace revenue, whereas a lower relevance threshold (LP90) has limited impact on GMV but
24

raises revenue through greater advertising returns. It is important to note that in our experiment
design, both treatment groups have higher average relevance scores than the benchmark score-based
algorithm (see Section 4.1). Thus, theLP90results demonstrate the superiority of the LP-based
algorithm in improving marketplace revenue while simultaneously enhancing the relevance of spon-
sored listings.
5.2 Why the LP-Based Algorithm Outperforms: Empirical Insights
In this section, we present empirical evidence to explain why the LP-based algorithm outperforms
the score-based benchmark. We begin with a heterogeneity analysis, showing that listings facing a
stronger revenue–relevance tradeoff benefit more from our method relative to the score-based algo-
rithm. We then analyze the characteristics of items prioritized by the LP-based algorithm, offering
deeper insight into the mechanisms underlying its superior performance. Because this analysis
requires fine-grained item-level information, we rely on the richer impression-level data collected
before the experiment’s launch, and we complement it with aggregated listing-level evidence from
the sampled impression-level data in the field experiment. Finally, drawing on these results to-
gether with the theoretical arguments in Section 3.4, we synthesize the evidence to highlight why
the LP-based algorithm outperforms the score-based benchmark.
5.2.1 Sponsored Listings that Benefit More
In this section, we conduct a heterogeneous treatment effect analysis to provide empirical evidence
for why our LP-based algorithm outperforms. Using the sampled impression-level data from the
full experiment, we focus on how the algorithm addresses the core revenue–relevance tradeoff. The
strength of this tradeoff varies across contexts, and our framework should perform particularly well
when it is more pronounced. One natural dimension along which this occurs is the displayed price
of sponsored listings. For higher-priced sponsored listings, the forces shaping conversion probability
and revenue potential diverge more sharply: on the one hand, expensive products typically face
lower baseline purchase probabilities, a pattern we also confirm in our data; on the other hand, each
successful conversion yields disproportionately higher revenue for the platform. Thus, effectively
managing the revenue–relevance tradeoff becomes especially critical for higher-priced listings, and it
is precisely in such cases where our LP-based approach is expected to deliver the greater gains. It is
worth noting that theLP90group is the one that can illustrate this argument, since it is the group
that achieves higher revenue than the benchmark based on Table 2. As discussed in Section 4.2, our
sampled dataset exhibits performance differences compared to the full dataset. The key observation
is that while theLP90group did not show a significantly higher number of purchases than the
score-based benchmark, it still achieved higher overall revenue. Detailed results are provided in
Appendix A.6.
To evaluate our hypothesis, we estimate the following empirical specification:
Yi =β 0 +β 1 ×Algo90 i +β 2 ×LogAvgPricei +β 3 ×WeightedPTR i +β 4 ×Algo90 i ×LogAvgPricei +η t +ϵ i,
25

where for each impressioni, the dependent variableYi ∈ {Purchases,Revenue}.Purchasesmeasures
the number of purchases per impression, andRevenuedenotes the revenue generated for the partner
marketplace per impression. Algo90i is the treatment indicator capturing assignment to theLP90
with the omitted category being theBenchmark.LogAvgPrice i is the logarithm of the average
product price of all items in the sponsored listing within impressioni; the log transformation reduces
the influence of extreme price values.WeightedPTRi denotes the average normalized PTR, weighted
bypositionweightsforthesponsoredlistinginimpressioni. Weincludedayfixedeffectsη t tocontrol
for time-varying heterogeneity. Our main parameter of interest isβ4, which captures the interaction
between algorithm assignment and displayed product price, and is expected to be positive.
Table 3: Sponsored Listings that Benefit More.
Purchases Revenue
(1) (2)
LP90 -0.019*** -0.091**
(0.002) (0.044)
LogAvgPrice -0.076*** -0.054***
(0.000) (0.015)
WeightedPTR 0.002*** 0.212***
(0.000) (0.006)
LP90×LogAvgPrice 0.004*** 0.034**
(0.000) (0.015)
Notes. Observation numbers areN= 1,381,222.
Robust standard errors are reported in parentheses.
***p <0.01, **p <0.05, *p <0.1.
Table 3 reports the results of the heterogeneity analysis. First, consistent with intuition, sponsored
listings with a higher average displayed price tend to receive fewer purchases and generate lower
platform revenue, whereas listings with a higher predicted transaction rate (PTR) attract more pur-
chases and contribute to higher revenue. Second, the negative coefficient onLP90arises because
the random sample does not show a significantly higher number of purchases for theLP90group,
suggesting that for lower-priced product listings, our algorithm delivers limited incremental value.
Third, the positive and significant coefficient on the interaction termLP90×log(AvgP rice)sup-
ports our prediction. Specifically, for sponsored listings with higher average product prices, where
the revenue–relevance tradeoff is more pronounced, the LP-based algorithm demonstrates greater
improvement relative to the score-based benchmark.
5.2.2 Item Characteristics Favored by the LP-based Algorithm
To further understand why the LP-based algorithm can outperform the score-based algorithm, we
next examine what types of items it tends to favor.
Given the data limitations, our sampled impression-level data from the experiment only includes
the aggregated characteristics of sponsored listings, but our exercise needs item-level information.
To achieve this, we leverage the impression-level data collected prior to the experiment’s launch,
26

which provides richer item-level details. For all data details, please refer to Section 4.2.
This dataset enables us to disentangle the two key stages of ranking algorithms (LP-based versus
score-based):item selection, which determines the set of products included in the sponsored listing,
andconditional ranking, which specifies their ordering once selected. Distinguishing between these
stages is important, as it allows us to assess not only whether the LP-based algorithm selects
a different set of items compared to the score-based benchmark, but also whether it employs a
distinct logic in ranking them.
To achieve our goal, we simulate both the score-based algorithm and the LP-based algorithm (with
λ∈ {0.90,0.95}) on the same candidate set for each impression, producing three distinct ranked
lists with an equal number of displayed items, set to the partner marketplace’s average display size.
The simulation reveals substantial divergence initem selection. Out of 13,370,159 candidate items
across 266,003 impressions, the score-based algorithm selects 2,579,511 unique items, while the LP-
based algorithm selects 2,530,810 items (λ= 0.90) and 2,535,457 items (λ= 0.95). The overlap
between the score-based and LP-based selections is only 1,395,573 items (λ= 0.90) and 1,419,438
items (λ= 0.95), corresponding to overlap ratios of just37.6%and38.4%of the combined unique
item sets. These statistics provide early evidence that the two ranking algorithms employ markedly
different logics in selecting items for sponsored listings.
Weimplementthefollowingempiricalstrategytoevaluatehowthealgorithmsdifferinitem selection.
The analysis is conducted separately for theLP90andLP95algorithms at the item level. For each
comparison (LP90vs. score-based algorithm orLP95vs. score-based algorithm), we construct a
universe consisting of all unique items shown by either algorithm across the dataset. The following
logistic regression specifications are estimated:
P(Selected LPk j = 1) = Λ(β01 +β 11ExpectedRevenuej +β 21Popularityj),
P(Selected LPk j = 1) = Λ(β02 +β 12OrganicRevenuej +β 22AdRevenuej +β 32Popularityj).
whereΛ(·)denotes the logistic function. For each unique itemj, the dependent variable SelectedLPk j
equals 1 if the item is selected by the LP algorithm with constraintλ=k(k∈ {0.90,0.95}), and 0
otherwise. ExpectedRevenuej denotes the expected revenue of itemj, computed using Equation 1
withw= 1andt j set to the averagetake rateof our partner marketplace, since the item-leveltake
rateis not observed. Because thetake rateexhibits little variation in our setting, this approximation
suffices to illustrate the mechanism of our method. Popularityj is defined as the total number of
timesitemjappearsinthecandidatesetandservesasaproxyforitempopularity. OrganicRevenue j
corresponds to theorganic revenuecomponent, given byrj ×tj ×pj in Equation 1, while AdRevenuej
corresponds to thead revenuecomponent, given byr j ×ad j ×p j.
Results on item characteristics favored by the LP-based algorithm in the selection stage are reported
in Table 4. Two patterns are noteworthy. First, by more effectively capturing the revenue–relevance
27

Table 4: Item Characteristics Favored by the LP-Based Algorithm: Item Selection.
LP90 LP95
(1) (2) (3) (4)
ExpectedRevenue 0.764*** 0.207***
(0.006) (0.003)
OrganicRevenue 0.148*** 0.072***
(0.004) (0.002)
AdRevenue 3.163*** 0.817***
(0.019) (0.010)
Popularity 0.118*** 0.114*** 0.135*** 0.133***
(0.001) (0.001) (0.001) (0.001)
Observations 3,793,666 3,793,666 3,793,666 3,793,666
Notes. Robust standard errors are reported in parentheses. ***p <0.01, **p <0.05, *p <
0.1.
tradeoff, bothLP90andLP95identify items with higher expected revenue, encompassing both
organic and advertising revenue, relative to the score-based benchmark in theitem selectionstage.
Second, our LP-based algorithms favor more popular items. A potential concern is that such selec-
tion may exacerbate inequities in online marketplaces, as niche products face reduced opportunities
for promotion. An advantage of our LP-based framework, however, is its flexibility: fairness con-
straints can be readily incorporated (e.g., Lu et al. 2025), and we provide additional extensions
along these lines in Appendix A.5.
Next, we move to the evaluation of differences inconditional ranking. We adopt a similar strategy
with the following specification:
P(Promoted k ij = 1) = Λ(β01 +β 11ExpectedRevenuej +β 21Popularityj),
P(Promoted k ij = 1) = Λ(β02 +β 12OrganicRevenuej +β 22AdRevenuej +β 32Popularityj).
This impression–item–level analysis is restricted to the subset of items appearing in both algorithms’
lists for a given impressioni. For each such itemj, the dependent variable Promotedk ij equals 1 if
RankLP ij <Rank score ij (i.e., the item is ranked higher by the LP algorithm) and 0 otherwise. The
evaluation is again conducted separately forLP90andLP95.
Results on the item characteristics favored by the LP-based algorithm during the ranking stage are
reported in Table 5. Consistent with the selection stage, the algorithm continues to favor items
with higher expected revenue, indicating that the LP-based approach can effectively capture the
revenue–relevancetradeoffnotonlywhendecidingwhichitemstoinclude, butalsowhendetermining
how to rank them relative to each other. A key difference emerges, however, in how the algorithm
weights the components of revenue. In the ranking stage, the algorithm tends to promote items
with higher organic revenue but down-weight items with higher ad revenue. This suggests that
once the set of sponsored listings is determined, the algorithm emphasizes consumer-driven revenue
28

Table 5: Item Characteristics Favored by the LP-based Algorithm: Conditional Ranking.
LP90 LP95
(1) (2) (3) (4)
ExpectedRevenue 0.001*** 0.001***
(0.000) (0.000)
OrganicRevenue 0.004*** 0.004***
(0.001) (0.001)
AdRevenue -0.002*** -0.002***
(0.000) (0.000)
Popularity -0.001*** -0.001*** -0.001*** -0.001***
(0.000) (0.000) (0.000) (0.000)
Observations 1,574,818 1,574,818 1,602,775 1,602,775
Notes. Robust standard errors are reported in parentheses. ***p <0.01, **p <0.05, *p <0.1.
rather than ad-driven revenue when refining the ranking. Another noteworthy finding is that the
LP-based algorithm systematically de-emphasizes more popular items in the ranking stage. By
less aggressively promoting popular items, the LP-based approach helps mitigate concerns about
fairness and concentration of exposure across items in the selection stage.
Similar patterns can also be seen in the aggregated sponsored-listing-level evidence from the sampled
impression-level data in the field experiment. We report the results in Appendix A.7.
5.2.3 Summarization of Why the LP-Based Algorithm Outperforms
The LP-based algorithm outperforms the score-based benchmark because it tackles the core chal-
lenge of balancing the revenue–relevance tradeoff in a more principled and flexible manner. Whereas
the score-based approach frames this tradeoff as a weighted tension betweenorganic revenueand
ad revenue, the LP-based framework directly maximizes total revenue while imposing a minimum
relevance constraint, thereby reflecting the practical requirement that marketplaces must safeguard
consumer experience even as they pursue revenue growth. Empirically, we show that the perfor-
mance gains of the LP-based algorithm are larger precisely when the revenue–relevance tradeoff is
more pronounced. Moreover, the algorithm proves advantageous in both theitem selectionand
conditional rankingstages, consistently identifying items with higher expected revenue. Finally, in
Appendix A.8, we document additional evidence that illustrates how the revenue–relevance tradeoff
operates in practice.
5.3 Generalizability and Limitations of the Experiment Results
Although our field experiment provides empirical evidence for the superiority of the LP-based algo-
rithm, we acknowledge two concerns regarding the generalizability and limitations of our findings.
First, all outcome variables in our main analysis capture only activities within the SLR. A possible
concern is that while purchases and revenues from the SLR increase, they could partly cannibalize
29

the purchases and revenues of theseed item. To assess this possibility, we analyze the sampled data
collected prior to the launch of the field experiment, which includes revenue information for theseed
item(Appendix A.9). Our results suggest that such cannibalization is unlikely to be substantial.
Second, our experiment focuses on short-run effects, raising the question of whether the observed
treatment effects persist in the long term. On the one hand, the main advantage of the LP-based
framework lies in its ability to capture the revenue–relevance trade-off, a mechanism that we believe
can be sustained in ranking scenarios. Indeed, our empirical evidence in Section 5.2 supports this
mechanism. On the other hand, we attempt to provide additional evidence on the potential for
long-term persistence using the available data (Appendix A.10). While these analyses are limited,
they offer suggestive insights that our experiment results are likely to hold in the long run.
6 Conclusion
In this paper, we propose a novel approach to ranking items in sponsored listings that not only
improves performance but also satisfies industry latency requirements. Specifically, we develop
a LP–based algorithm for sponsored listings. Beyond establishing its theoretical properties, we
conduct a large-scale field experiment on a major U.S. online marketplace. The results validate
both the superiority of our LP-based algorithm over the industry’s score-based benchmark and its
applicability in real-time settings. Complementary empirical analyses further shed light on the
mechanisms driving its effectiveness. The key advantage of our framework lies in its principled
treatment of the revenue–relevance tradeoff: rather than framing it as a weighted balance between
organic revenueandad revenue, as in the score-based approach, our algorithm directly maximizes
total revenue subject to a minimum relevance constraint. We further highlight the flexibility of
LP-based methods in incorporating broader planning constraints.
Several important avenues remain for future research. First, while our empirical evidence focuses on
sponsored listings, the framework could be extended to KR settings where ranking plays a critical
role, such as in our partner marketplace. A key distinction is that sponsored items are typically
specified to consumers in KR, a challenge that would need to be addressed in such extensions.
Second, following industry practice, we estimated position weights (hi) and PTR separately and
treated them as given when optimizing the ranking process. Developing efficient methods to jointly
estimateh i andPTRrepresentsaninterestingandimportantnextstep. Finally, althoughweprovide
preliminary evidence on the long-term effects of our LP-based algorithm, richer field experiments
specifically designed to capture sustained outcomes would yield deeper insights into its long-run
impact (Zhang et al. 2020). In particular, future investigations could examine how the estimation of
PTR should be adapted to capture consumers’ behavioral changes under the new ranking algorithm,
as well as how advertisers adjust their bidding and advertising strategies in response.
30

References
Adomavicius, G. and Kwon, Y. (2014). Optimization-based approaches for maximizing aggregate
recommendation diversity.INFORMS Journal on Computing, 26(2):351–369.
Agarwal, A., Takatsu, K., Zaitsev, I., and Joachims, T. (2019). A general framework for counter-
factual learning-to-rank. InProceedings of the 42nd International ACM SIGIR Conference on
Research and Development in Information Retrieval, pages 5–14.
Agarwal, D., Chen, B.-C., Elango, P., and Wang, X. (2011). Click shaping to optimize multiple
objectives. InProceedings of the 17th ACM SIGKDD international conference on Knowledge
discovery and data mining, pages 132–140.
Amatriain, X. (2013). Big & personal: data and models behind netflix recommendations. In
Proceedings of the 2nd international workshop on big data, streams and heterogeneous source
Mining: Algorithms, systems, programming models and applications, pages 1–6.
Applegate, D., Díaz, M., Hinder, O., Lu, H., Lubin, M., O’Donoghue, B., and Schudy, W. (2021).
Practical large-scale linear programming using primal-dual hybrid gradient.Advances in Neural
Information Processing Systems, 34:20243–20257.
Applegate, D., Díaz, M., Lu, H., and Lubin, M. (2024). Infeasibility detection with primal-dual
hybrid gradient for large-scale linear programming.SIAM Journal on Optimization, 34(1):459–
484.
Applegate, D., Hinder, O., Lu, H., and Lubin, M. (2023). Faster first-order primal-dual methods for
linear programming using restarts and sharpness.Mathematical Programming, 201(1):133–184.
Asadpour, A., Niazadeh, R., Saberi, A., and Shameli, A. (2023). Sequential submodular maximiza-
tionandapplicationstorankinganassortmentofproducts.Operations Research, 71(4):1154–1170.
Bhalgat, A., Feldman, J., and Mirrokni, V. (2012). Online allocation of display ads with smooth de-
livery. InProceedings of the 18th ACM SIGKDD international conference on Knowledge discovery
and data mining, pages 1213–1221.
Caro, F. and Gallien, J. (2007). Dynamic assortment with demand learning for seasonal consumer
goods.Management science, 53(2):276–292.
Cattrysse, D. G. and Van Wassenhove, L. N. (1992). A survey of algorithms for the generalized
assignment problem.European journal of operational research, 60(3):260–272.
Celis, L. E., Straszak, D., and Vishnoi, N. K. (2017). Ranking with fairness constraints.arXiv
preprint arXiv:1704.06840.
Chen, G., Chan, T., Zhang, D., Liu, S., and Wu, Y. (2024). The effects of diversity in algorith-
mic recommendations on digital content consumption: A field experiment.Available at SSRN
4365121.
31

Chen, J., Dong, H., Wang, X., Feng, F., Wang, M., and He, X. (2023). Bias and debias in rec-
ommender system: A survey and future directions.ACM Transactions on Information Systems,
41(3):1–39.
Chen, Y., Berkhin, P., Anderson, B., and Devanur, N. R. (2011). Real-time bidding algorithms for
performance-based display ad allocation. InProceedings of the 17th ACM SIGKDD international
conference on Knowledge discovery and data mining, pages 1307–1315.
Cheng, H.-T., Koc, L., Harmsen, J., Shaked, T., Chandra, T., Aradhye, H., Anderson, G., Corrado,
G., Chai, W., Ispir, M., et al. (2016). Wide & deep learning for recommender systems. In
Proceedings of the 1st workshop on deep learning for recommender systems, pages 7–10.
Covington, P., Adams, J., and Sargin, E. (2016). Deep neural networks for youtube recommenda-
tions. InProceedings of the 10th ACM conference on recommender systems, pages 191–198.
Feldman, J., Zhang, D. J., Liu, X., and Zhang, N. (2022). Customer choice models vs. machine
learning: Finding optimal product displays on alibaba.Operations Research, 70(1):309–328.
Ferreira, K. J., Parthasarathy, S., and Sekar, S. (2022). Learning to rank an assortment of products.
Management Science, 68(3):1828–1848.
Gallego, G., Iyengar, G., Phillips, R., and Dubey, A. (2004). Managing flexible products on a
network.Available at SSRN 3567371.
Gallego, G., Li, A., Truong, V.-A., and Wang, X. (2020). Approximation algorithms for product
framing and pricing.Operations Research, 68(1):134–160.
Gallego, G., Ratliff, R., and Shebalov, S. (2015). A general attraction model and sales-based
linear program for network revenue management under customer choice.Operations Research,
63(1):212–232.
Gallego, G., Topaloglu, H., et al. (2019).Revenue management and pricing analytics, volume 209.
Springer.
Ge, Z., Zhou, W., Lute, J., and Ilardi, A. (2021). Relevance constrained re-ranking in sponsored
listing recommendations. InProceedings of the 2021 ACM SIGKDD Workshop on AdKDD. ACM.
Geyik, S. C., Ambler, S., and Kenthapadi, K. (2019). Fairness-aware ranking in search & recom-
mendation systems with application to linkedin talent search. InProceedings of the 25th acm
sigkdd international conference on knowledge discovery & data mining, pages 2221–2231.
Ghose, A., Ipeirotis, P. G., and Li, B. (2014). Examining the impact of ranking on consumer
behavior and search engine revenue.Management Science, 60(7):1632–1654.
Granger, C. W. (1969). Investigating causal relations by econometric models and cross-spectral
methods.Econometrica: journal of the Econometric Society, pages 424–438.
32

Hofmann, K., Schuth, A., Whiteson, S., and De Rijke, M. (2013). Reusing historical interaction data
for faster online learning to rank for ir. InProceedings of the sixth ACM international conference
on Web search and data mining, pages 183–192.
Hu, Y., Da, Q., Zeng, A., Yu, Y., and Xu, Y. (2018). Reinforcement learning to rank in e-commerce
search engine: Formalization, analysis, and application. InProceedings of the 24th ACM SIGKDD
international conference on knowledge discovery & data mining, pages 368–377.
Jiang, Z. Z., Li, J., and Zhang, D. J. (2025). A high-dimensional choice model for online retailing.
Management Science, 71(4):3320–3339.
Joachims, T., Swaminathan, A., and Schnabel, T. (2017). Unbiased learning-to-rank with biased
feedback. InProceedings of the tenth ACM international conference on web search and data
mining, pages 781–789.
Karp, R. M., Vazirani, U. V., and Vazirani, V. V. (1990). An optimal algorithm for on-line bipartite
matching. InProceedings of the twenty-second annual ACM symposium on Theory of computing,
pages 352–358.
Kök, A. G., Fisher, M. L., and Vaidyanathan, R. (2009). Assortment planning: Review of litera-
ture and industry practice.Retail supply chain management: Quantitative models and empirical
studies, pages 99–153.
Li, B., Tang, K., Li, J., and Yao, X. (2016). Stochastic ranking algorithm for many-objective
optimization based on multiple indicators.IEEE Transactions on Evolutionary Computation,
20(6):924–938.
Li, X., Rong, Y., Zhang, R., and Zheng, H. (2025). Online advertisement allocation under customer
choices and algorithmic fairness.Management Science, 71(1):825–843.
Lin, X., Chen, H., Pei, C., Sun, F., Xiao, X., Sun, H., Zhang, Y., Ou, W., and Jiang, P. (2019). A
pareto-efficient algorithm for multiple objective optimization in e-commerce recommendation. In
Proceedings of the 13th ACM Conference on recommender systems, pages 20–28.
Liu, Q., Yu, F., Wu, S., and Wang, L. (2015). A convolutional click prediction model. InProceedings
of the 24th ACM international on conference on information and knowledge management, pages
1743–1746.
Louca, R., Bhattacharya, M., Hu, D., and Hong, L.(2019). Joint optimization of profitand relevance
for recommendation systems in e-commerce. InRMSE@ RecSys.
Lu, H., Simester, D., and Zhu, Y. (2025). Optimizing scalable targeted marketing policies with
constraints.Marketing Science, page forthcoming.
Luce, R. D. (2005).Individual choice behavior: A theoretical analysis. Courier Corporation.
33

Manmatha, R., Rath, T., and Feng, F. (2001). Modeling score distributions for combining the
outputs of search engines. InProceedings of the 24th annual international ACM SIGIR conference
on Research and development in information retrieval, pages 267–275.
McFadden, D. et al. (1973). Conditional logit analysis of qualitative choice behavior.
Mehta, A.etal.(2013). Onlinematchingandadallocation.Foundations and Trends®in Theoretical
Computer Science, 8(4):265–368.
Montague, M.andAslam, J.A.(2001). Relevancescorenormalizationformetasearch. InProceedings
of the tenth international conference on Information and knowledge management, pages 427–433.
Okura, S., Tagami, Y., Ono, S., and Tajima, A. (2017). Embedding-based news recommendation for
millions of users. InProceedings of the 23rd ACM SIGKDD international conference on knowledge
discovery and data mining, pages 1933–1942.
Pentico, D. W. (2007). Assignment problems: A golden anniversary survey.European Journal of
Operational Research, 176(2):774–793.
Renda, M. E. and Straccia, U. (2003). Web metasearch: rank vs. score based rank aggregation
methods. InProceedings of the 2003 ACM symposium on Applied computing, pages 841–846.
Rodriguez, M., Posse, C., and Zhang, E. (2012). Multiple objective optimization in recommender
systems. InProceedings of the sixth ACM conference on Recommender systems, pages 11–18.
Ross, G. T. and Soland, R. M. (1975). A branch and bound algorithm for the generalized assignment
problem.Mathematical programming, 8(1):91–103.
Rusmevichientong, P., Shen, Z.-J. M., and Shmoys, D. B. (2010). Dynamic assortment optimization
with a multinomial logit choice model and capacity constraint.Operations research, 58(6):1666–
1680.
Rusmevichientong, P. and Topaloglu, H. (2012). Robust assortment optimization in revenue man-
agement under the multinomial logit choice model.Operations research, 60(4):865–882.
Salkin, H. M. and De Kluyver, C. A. (1975). The knapsack problem: a survey.Naval Research
Logistics Quarterly, 22(1):127–144.
Sumida, M., Gallego, G., Rusmevichientong, P., Topaloglu, H., and Davis, J. (2021). Revenue-utility
tradeoff in assortment optimization under the multinomial logit model with totally unimodular
constraints.Management Science, 67(5):2845–2869.
Talluri, K. and Van Ryzin, G. (2004). Revenue management under a general discrete choice model
of consumer behavior.Management Science, 50(1):15–33.
34

Xiao, L., Min, Z., Yongfeng, Z., Zhaoquan, G., Yiqun, L., and Shaoping, M. (2017). Fairness-aware
group recommendation with pareto-efficiency. InProceedings of the eleventh ACM conference on
recommender systems, pages 107–115.
Yang, X., Li, Y., Wang, H., Wu, D., Tan, Q., Xu, J., and Gai, K. (2019). Bid optimization by mul-
tivariable control in display advertising. InProceedings of the 25th ACM SIGKDD international
conference on knowledge discovery & data mining, pages 1966–1974.
Ye, Z., Zhang, D. J., Zhang, H., Zhang, R., Chen, X., and Xu, Z. (2023). Cold start to improve
market thickness on online advertising platforms: Data-driven algorithms and field experiments.
Management Science, 69(7):3838–3860.
Zehlike, M., Yang, K., and Stoyanovich, J. (2022). Fairness in ranking, part i: Score-based ranking.
ACM Computing Surveys, 55(6):1–36.
Zhang, D. J., Dai, H., Dong, L., Qi, F., Zhang, N., Liu, X., and Liu, Z. (2020). The long-term and
spillover effects of price promotions on retailing platforms: Evidence from a large randomized
experiment on alibaba.Management Science, 66(6):2291–2799.
Zhang, W., Wei, C., Meng, X., Hu, Y., and Wang, H. (2018). The whole-page optimization via
dynamic ad allocation. InCompanion Proceedings of the The Web Conference 2018, pages 1407–
1411.
Zhou, G., Zhu, X., Song, C., Fan, Y., Zhu, H., Ma, X., Yan, Y., Jin, J., Li, H., and Gai, K. (2018).
Deep interest network for click-through rate prediction. InProceedings of the 24th ACM SIGKDD
international conference on knowledge discovery & data mining, pages 1059–1068.
35

Online Appendix
A.1 Computation Results
In this section, we compare the performance of our proposed LP-based algorithm and Gurobi, a
commercial solver, for solving synthetic instances that mimic the SLR problem in practice. Recall
that our goal is to solve the MIP formulationP0. Unfortunately, no MIP solver can possibly solve
P0 within the latency requirement or even close. To meet the latency requirement, we consider two
approaches: (i) the proposed LP-based Algorithm 2, which outputs a feasible, integral, and nearly
optimal solution toP 0; (ii) commercial LP solver Gurobi to solve the relaxed LP formulation (7),
which often outputs an infeasible and fractional solution toP1, but it serves a good benchmark for
running time comparison.
In all of our experiments, we simulate each instance (a given pair ofm, n, λ) 1000 times and present
the average results. For Gurobi, we used the concurrent method Gurobi 10.0, which runs primal
simplex, dual simplex, and barrier methods simultaneously. We set the dual feasibility tolerance to
be10 −4 (for Gurobi) and theϵto be10 −4 (for LP-based Algorithm 2). The experiments run on the
Dell PowerEdge R640 computing node with20GB of memory. It is noted that the running time for
Gurobi listed below only involves the solving time and does not include the model building time.
In practice, the time latency (0.1seconds) is required for the sum of building and solving time. To
exhibit the efficiency of the LP-based algorithm, we designed two experiments.
First, due to the special structure of the formulated SLR problem,λplays an essential role in
determining the computational cost of solving the problem. With a smallλ, the relevance constraint
(8) might be redundant, thus resulting in the LP-based algorithm solving extremely fast. Therefore,
we would like to compare the LP-based algorithm’s and Gurobi’s performances with a wide range of
λ∈[0,1]. In the first experiment, by fixing the problem size (m= 50slots andn= 500products,
which is typically the largest problem size we might encounter in Marketplace A’s SLR problem)
and independently uniformly generating random variables (h, r, v∼U(0,1)), we set up the test for
multipleλranging from0to1, i.e.,λ∈ {.1, .2, .3, .4, .5, .6, .7, .8, .9, .925, .95, .975}. The optimal gap
is calculated as (Optimal value of MIPP0 - Approximated objective value of LP-based Algorithm
2)/Optimal value of MIPP0. As indicated in Table A1, we see that excluding the cases whereλis
Online Appendix Page 1

too small (λ≤0.5), the proposed LP-based algorithm achieves more than20x time improvement
over Gurobi LP solver. In the meantime, the LP-based algorithm can achieve the optimal gap of
less than0.05%for each instance.
Table A1:Experiment Results for Multipleλ,m= 50, andn= 500
λ .1 .2 .3 .4 .5 .6 .7 .8 .9 .925 .95 .975
Optimality Gap (%) 0.000* 0.000* 0.000* 0.000* 0.000* 0.001 0.003 0.008 0.015 0.019 0.027 0.042
LP-based time (seconds) 0.001 0.001 0.001 0.001 0.004 0.009 0.01 0.01 0.01 0.01 0.011 0.012
Gurobi time (seconds) 0.224 0.205 0.204 0.205 0.212 0.231 0.247 0.264 0.3 0.317 0.337 0.362
Time improvement
(Gurobi time/LP-based time)
289** 269** 262** 252** 48** 24 26 27 30 31 30 30
In the second experiment, we would like to explore the performance of the LP-based algorithm for
various problem sizes, especially when the problem dimension increases. Thus, for the second ex-
periment, by pickingλ= 0.95(which is a reasonable value forλas shown in the field study), we test
with a range ofm∈ {10,20,50,100,200,500}andn∈ {50,100,200,500,1000,2000}(m≤n). As
shown in Table A2, compared to Gurobi, the LP-based algorithm achieves a massive improvement,
especially under large-scale problems. We see that the time improvement grows as the problem size
increases, whereas the optimal gap reduces. Whenm= 500, the LP-based algorithm is more than
100x faster than Gurobi with the optimal gap to be0.004%. Under the0.1seconds latency require-
ment, we see that the LP-based solver can solve a problem with a size of at mostm= 500, n= 500.
Yet, under the same conditions, Gurobi can only solve one with a size ofm= 100, n= 100. Overall,
the optimal gap is usually negligible (<1%) for reasonably sized instances.
The above two experiments demonstrate the efficiency of the proposed algorithm compared to state-
of-the-art commercial solvers. Indeed, the LP commercial solver is not a feasible solution due to
the latency requirement of the marketplace, while our proposed Algorithm 2 enables such an LP
approach for sponsored listing.
Online Appendix Page 2

Table A2:Experiment Results for Various Problem Sizes
Panel A: LP-based time (seconds)
m
n 50 100 200 500 1000 2000
10 0.001 0.001 0.003 0.006 0.011 0.022
20 0.001 0.002 0.003 0.007 0.013 0.027
50 0.001 0.002 0.005 0.011 0.021 0.041
100 0.003 0.006 0.017 0.034 0.067
200 0.011 0.027 0.061 0.128
500 0.061 0.125 0.283
Panel B: Gurobi time (seconds)
m
n 50 100 200 500 1000 2000
10 0.003 0.006 0.012 0.038 0.102 0.326
20 0.007 0.014 0.027 0.085 0.225 0.671
50 0.017 0.045 0.110 0.343 0.851 2.304
100 0.094 0.205 0.423 0.844 1.832
200 0.639 1.366 2.468 5.170
500 8.158 16.339 28.717
Panel C: Time improvement (Gurobi time/LP time)
m
n 50 100 200 500 1000 2000
10 4.9 4.7 4.8 6.4 9.2 14.6
20 9.2 9.1 8.6 11.9 16.9 25.3
50 16.0 20.1 23.6 31.4 40.8 56.2
100 29.2 31.7 24.7 24.6 27.3
200 58.3 50.0 40.4 40.4
500 133.7 130.3 101.5
Panel D: Optimal Gap (%)
m
n 50 100 200 500 1000 2000
10 0.83 0.573 0.343 0.159 0.078 0.039
20 0.336 0.269 0.182 0.081 0.044 0.020
50 0.062 0.059 0.052 0.027 0.015 0.007
100 0.015 0.015 0.01 0.006 0.004
200 0.004 0.004 0.004 0.004
500 0.004 0.004 0.004
A.2 Guidance for Fine-Tuning the LP-Based Algorithm
This section provides practical guidelines for fine-tuning and implementing the LP-based algorithm.
The algorithm involves only one parameter, the relevance parameterλ. As a first step, we rec-
ommend that readers estimate a suitable range ofλfor subsequent A/B testing using historical
data.
For each historical impressionkgenerated by the current ranking algorithm, assume access tov,
r,h, and the corresponding rankingX k. These inputs allow the computation of a relevance score
(see Equation 5):
Rel(X k) =
Pm
i=1
Pn
j=1 hirjX k ij
a .(1)
The intuition is as follows. Substituting Rel(Xk)into Equation 5 yieldsa(Rel(Xk)−λ)≥0, which
simplifies to Rel(Xk)≥λ. In other words,λspecifies a lower bound on the relevance score for
future impressions.
We suggest that practitioners construct the empirical distribution of Rel(Xk)across historical
impressions and select a summary statistic (e.g., the mean, median, or a chosen quantile) as a
benchmark value, denotedλ 0. Implementing the LP-based algorithm withλ 0 ensures that the
Online Appendix Page 3

resulting relevance scores are, on average, comparable to those under the prior ranking algorithm.
This provides a principled starting point for further tuning via A/B testing.
Building on this benchmark, readers can adjustλaccording to their strategic objectives. For those
aiming to improve ranking quality relative to the current strategy, we recommend starting with
λ0 and testing incremental increases. Specifically, testing groups can be formed with relevance
parametersλ 0, λ0 +δ, λ0 + 2δ, . . .for some user-chosen step sizeδ >0. As shown in our earlier
analysis, higher values ofλtypically yield rankings that are more relevant.
Conversely, practitionersseekingtoprioritizerevenuemayexploredecreasingλfromλ 0, forexample,
λ0, λ0 −δ, λ0 −2δ, . . .. Ultimately, the optimal choice ofλshould be guided by the outcomes of A/B
testing, balancing the trade-off between relevance and revenue in line with organizational objectives.
A.3 Proof of Theorem 1
In order to prove Theorem 1, we first show the following lemma that gives the closed-form solution
of the LP-relaxed primal problemP1:
Lemma 1(Closed-form solution of the LP-relaxed primal problem).Under Assumptions 1 and 2
the optimal solution of the LP-relaxed primal problemP1, denoted byXLP, has the following closed
form:
1.Case A (Nonbinding relevance constraint).Fixµ= 0withδ=v, then if
Rel(PrimalResponse(δ, m))≥λa, then the relevance constraint is nonbinding withµ ∗ = 0,
and the LP optimal solution is integral:XLP =PrimalResponse(δ, m).
2.Case B (Binding relevance constraint).The relevance constraint binds whenµ ∗ >0.
For any dual variableµ, we define its associated integral solution as
X +(µ) := lim t→0PrimalResponse(v+ (µ+t)r, m), then the optimal dual variableµ∗ of the
problemD 1 is characterized as the smallest pairwise indifference value such that its associated
integral solution is feasible, i.e., :
µ∗ = inf{µ∈ {0} ∪ {µjk }(j,k)∈I :Rel(X +(µ))≥λa}.(2)
Online Appendix Page 4

Then for suchµ∗, letδ∗ :=v+µ ∗rand its sorted indices in non-increasing order asj(1),· · ·, j(n).
•B1 (Boundary tie between positionmandm+ 1).Ifδ ∗ j(m) =δ ∗ j(m+1), then the
optimal solution is fractional only in the last row:
X LP i,j(i) = 1∀i < m,XLP m,j(m) =α,X LP m,j(m+1) = 1−α,X LP ij = 0otherwise,(3)
•B2 (Interior tie within the topmpositions).Ifδ ∗ j(s) =δ ∗ j(s+1) for somes < m,
then optimal solution is fractional only in rowsands+ 1:
X LP i,j(i), = 1∀i∈[m]\ {s, s+ 1},X LP s,j(s) =X LP s+1,j(s+1) = 1−α,
X LP s,j(s+1) =X LP s+1,j(s) =α,X LP ij = 0otherwise,(4)
•B3 (No tie within the topmpositions).Ifδ ∗ j(1) >· · ·> δ∗ j(m), i.e., all top-m scores
are strictly ordered, then the optimal LP solution is integral:
X LP i,j(i) = 1∀i∈[m],X LP ij = 0otherwise.(5)
Proof.ForCase A, it is trivial to see that when the relevance constraint ofP1 is nonbinding, then
the optimal dual variableµ∗ = 0. The LP optimal solution is integral and the permutation of the
sorted vectorvin a descending order.
ForCase B, we show that the derived LP solutions in all sub-cases are (1) feasible and (2) optimal.
Feasibility Check.
•B1 (Boundary tie between positionmandm+ 1).
Rel(X LP) =
m−1X
i=1
hirj(i) +αh mrj(m) + (1−α)h mrj(m+1) (6)
=
m−1X
i=1
hirj(i) +λa−
m−1X
i=1
hirj(i) (7)
=λa.(8)
Online Appendix Page 5

•B2 (Interior tie within the topmpositions).
Rel(X LP) =
mX
i=1,i /∈{s,s+1}
hirj(i) + (1−α)(h srj(s) +h s+1rj(s+1)) +α(h s+1rj(s) +h srj(s+1))
(9)
=
mX
i=1,i /∈{s,s+1}
hirj(i) +λa−
mX
i=1,i /∈{s,s+1}
hirj(i) (10)
=λa.(11)
•B3 (No tie within the topmpositions).The proposedX LP is the permutation matrix
that assigns the topmitems to themrows in the order ofh. We will see below that in this
subcase necessarily Rel(XLP) =λa, otherwiseµ ∗ would not be dual-optimal.
Optimality Check.
We show thatX LP in all three subcases ofCase Bare optimal forP 1. We first verify the KKT
conditions for the relaxed LP problem:
1.Dual feasibility:by definition of the dual problem.
2.Primal feasibility:as we have shown in the previous part ofFeasibility check.
3.Stationarity:for all three subcases, we haveX LP ∈arg max X∈F L(µ,X). In case B1 and
B2, every split within the tied block maximizesL(µ∗,·), so ourX LP is one such maximizer;
in case B3, since the order ofδ∗ is strict overj(1),· · ·, j(m), the stated permutation is the
unique maximizer.
4.Complementary slackness:for all three cases, we haveµ ∗(λa−Rel(X LP)) = 0.
Since all KKT conditions are satisfied, therefore,XLP is optimal forP1.
Then we have the following proof for Theorem 1:
Proof.Note that we could re-writeE[ ˜X] = (1−α)X + +αX −. Then we discuss over each case.
Case A (Nonbinding relevance constraint).Withµ∗ = 0, we haveX− =X + =X LP. Thus
E[ ˜X] =X LP, whereX LP is the optimal solution toP1.
Online Appendix Page 6

Case B1 (Boundary tie between positionmandm+ 1).From Algorithm 3, we see that both
X − andX + have the exact same first rowsm−1withX+,i,j(i) =X −,i,j(i) = 1for alli < m. Thus,
E[ ˜X i,j(i)] =X LP i,j(i) = 1for alli < m. In them-th row,X +,m,j(m+1) = 1whileX −,m,j(m) = 1.
Thus, we get them-th row ofE[˜X]as:
E[ ˜X m,j(m)] =α=X LP m,j(m),(12)
and
E[ ˜X mj(m+1)] = 1−α=X LP m,j(m+1).(13)
Thus,E[ ˜X] =X LP.
B2 (Interior tie within the topmpositions).Similarly, we see that bothX − andX + have
the exact same rows except fors- ands+1-th row. Specifically,X−,s,j(s) = 1andX +,s+1,j(s+1) = 1.
Therefore, we haveE[ ˜X s,j(s)] =E[ ˜X s+1,j(s+1)] = 1−αandE[ ˜X s,j(s+1)] =E[ ˜X s+1,j(s)] =α. This
gives:E[ ˜X] =X LP.
B3 (No tie within the topmpositions).Then the Lagrangian maximizer atµ∗ is unique with
X + =X − =X LP. ThusE[ ˜X] =X LP.
A.4 Summary Statistics of the Sampled Data
Panel A in table A3 reports the summary statistics for our second dataset, introduced in Section
4.2, which consists of a random sample from the full-scale experiment. Panel B in table A3 presents
the summary statistics for our third dataset, a random sample drawn prior to the launch of the field
experiment. Both samples are at the impression level and we report summary statistics only for
those variables whose disclosure is permitted by the company. All monetary variables are reported
in USD.
A.5 Extension: Overall Planning
In practice, there may be additional requirements from marketplaces and/or customers. For in-
stance, (1) some marketplaces would like to pose constraints such as inventory limits or targeted
Online Appendix Page 7

Table A3: Summary Statistics.
Variable Mean Median SD Sample Size
Panel A: Random Sample of the Full-Scale Experiment
Average Product Price 2.69 0.31 57.33 2,071,833
Number of Clicks 1.07 1.00 0.53 2,071,833
Panel B: Random Sample Drawn Before the Experiment
Average Product Price 301.31 29.69 11223.03 13,370,159
Total Number of Candidate Items 70.17 60.00 47.90 266,003
Total Number of Items 11.34 12.00 2.35 266,003
Total Number of Sponsored Items 9.43 12.00 4.11 266,003
Number of Clicks 0.32 0.00 0.64 266,003
Seed Item Price 819.38 28.99 53,169.45 266,003
revenue for each seller or product category, and (2) some consumers way prefer the diversity of
items shown to them. These global constraints involve many impressions over a period; thus, we
call it overall planning. Unfortunately, there is no guarantee that a score-based algorithm can sat-
isfy such constraints because a score-based algorithm takes greedy operations for local objectives.
On the other hand, these constraints can be naturally incorporated into an LP-based algorithm, as
described below.
A.5.1 LP-Based Algorithm for Overall Planning
The basic idea is to utilize historical data to obtain corresponding dual variables (i.e., reduced costs)
associated with the overall planning constraints and then utilize these dual variables in the online
LP-based ranking.
Step 1: Obtain dual variables for global constraints.Given a historical dataset that records
the impressions for each day, suppose there areTimpressions,Gunique consumers, and a group
ofKselected sellers who pay additionalAd feesand accordingly pose requirements on inventory
and revenue. For each impressiont, it hasmt slots andn t candidate items. Leth it, vjt, rjt denote
the associated position weight for each slotit, revenue and relevance for each candidate itemjt.
Similar to the previous setting, for each impressiont, we can get the maximum relevance scoreat
that any ranking can obtain, and define any relevance hyperparameterλt ∈[0,1].
For a selected sellerk, there is an inventory limitLk, and a target revenueIk within a time period
(usually a day). We consider the following overall planning constraints: (i) from the perspective of
Online Appendix Page 8

market fairness, the online marketplace does not interfere with the number of items a single sellerk
could display to a single consumerg; (ii) for each consumerg, she would prefer candidate items from
various diverse sellers instead of a few who have paid highAd fees. Therefore, we would set up a
lower bound of the total of sellers whose items are displayed to her, denoted bySg. (iii) After paying
an extra Ad rate, the sellerkwould want to display his items to at leastCk number of consumers.
We would highlight that any combination of these constraints (even some similar constraints) can
be incorporated into this algorithmic framework.
Suppose we haveTimpressions in the historical data, indexed byt,i.e.,t= 1, ..., T. We selectK
unique sellers, indexed byk= 1, ..., K, andGunique consumers, indexed byg= 1, ..., G. Each
consumerghas totalT g impressions. Moreover, among theseT g impressions, the candidate items
are provided byKg sellers.
Using historical data, we can obtain the optimal ranking with overall constraints (i), (ii), (iii) by
solving the following LP:
max
X
TX
t=1
mtX
i=1
ntX
j=1
hitvjtX ijt (14)
s.t.
mtX
i=1
ntX
j=1
hitrjtX ijt ≥λ tat,∀t= 1, ..., T(15)
TX
t=1
mtX
i=1
ntX
j=1
X ijt1{itemjtlisted by sellerk} ≤L k,∀k= 1, ..., K(16)
TX
t=1
mtX
i=1
ntX
j=1
hitX ijtvjtk 1{itemjtlisted by sellerk} ≥I k,∀k= 1, ..., K(17)
GX
g=1
TgX
t=1
mtX
i=1
ntX
j=1
X ijt1{itemjtlisted by sellerk} ≥C k,∀k= 1,· · ·, K(18)
KX
k=1
TgX
t=1
mtX
i=1
ntX
j=1
X ijt1{itemjtlisted by sellerk} ≥S g,∀g= 1,· · ·, G(19)
mtX
i=1
X ijt ≤1,∀t= 1, ..., T,∀jt= 1, ..., nt (20)
ntX
j=1
X ijt ≤1,∀t= 1, ..., T,∀it= 1, ..., mt (21)
0≤X ijt ≤1,∀t= 1, ..., T,∀jt= 1, ..., nt,∀it= 1, ..., mt (22)
Online Appendix Page 9

where (15) associates with the relevance constraint, (16) associates with the inventory limit con-
straint, (17) associates with the revenue constraint, (18) associates with the minimum seller con-
straint, and (19) associates with the minimum consumer constraint.
Notice that the above LP could be large in terms of the size of the decision variable and the number
of constraints, therefore we cannot solve it in real time. Instead, we can collect the data from the last
time period and solve the above offline LP. Then, we obtain the optimal dual variablesξ(inventory
limit constraint (16)),ν(the revenue constraint (17)),η(the minimum seller constraint (18)), and
θ(minimum consumer constraint (19)).
Later, for each incoming impressiontinduced by consumerg, we can modify the previous LP
problem proposed inP 1 by adding extra terms associated withξ, ν, θ, ηto the objective function.
The modified LP problem is illustrated in below:
max
X
mtX
i=1
ntX
j=1
hitvjtX ijt −
KX
k=1
ξk
mtX
i=1
ntX
j=1
X ijt1{itemjtlisted by sellerk}
+
KX
k=1
νk
mtX
i=1
ntX
j=1
hitX ijtvjtk 1{itemjtlisted by sellerk}
+
KX
k=1
ηk
mtX
i=1
ntX
j=1
X ijt1{itemjtlisted by sellerk}
+θ g
KX
k=1
mtX
i=1
ntX
j=1
X ijt1{itemjtlisted by sellerk}
s.t.
mtX
i=1
ntX
j=1
hitrjtX ijt ≥λ tat
mtX
i=1
X ijt ≤1,∀j= 1, ..., nt
ntX
j=1
X ijt ≤1,∀i= 1, ..., mt
0≤X ijt ≤1,∀j= 1, ..., nt,∀i= 1, ..., mt.
Notice that the LP formulation can be huge in practice. We present numerical experiments on
solvingsuch problemswiththe recentdevelopmentofsolversinthe nextsection, which demonstrates
the traceability of this approach.
Online Appendix Page 10

A.5.2 Computational results for overall planning
In this section, we present the experiment results for the overall planning problem from Section
A.5. The overall planning is formalized as a large-scale problem using the data from a certain
period; therefore, it can only be solved offline. Therefore, in this experiment, we formulate the
optimization problem using the historical data of an entire day. Specifically speaking, we would set
up the restrictions on the existing inventoryLand the targeted revenueIfor the selected top sellers
who have the most listed items. In total, we filter out 5,408 sellers and formulate an optimization
problem with 265,646,022 variables, 26,423,572 constraints, and 962,620,739 non-zeros. We use two
solvers, which are Gurobi (version 9.0) and OR-Tools1, and compare their performances in terms
of the solving time, number of iterations, and minimum memory spaces required.
Currently, Gurobi adopts three widely-used methods to solve the LP problem, which are respectively
primal simplex, dual simplex, and barrier. For OR-Tools, we choose the method of Practical Large-
Scale Linear Programming using Primal-Dual Hybrid Gradient (PDLP) (Applegate et al., 2021,
2023,2024), whichspecializesinsolvinglarge-scaleLPproblemsefficiently. Thus, inthisexperiment,
we incorporate four groups (Primal Simplex, Dual Simplex, Barrier, and PDLP) in total, and
compare the performance of PDLP to all other groups. For these experiment groups, under different
coresandthreads, weevaluatetheirperformanceintermsofthesolvingtime. Similartotheprevious
section, we implement this experiment with the Dell PowerEdge R640 computing node. It is noted
that in our case, due to the restricted computing resources, the upper limit of the running time is
set to be 48 hours (172,800seconds).
Out of four groups, we first find that Gurobi Dual simplex method fails to deliver the correct solution
due to the numerical sensitivity caused by the excessively large number of variable coefficients, and
Gurobi Primal simplex reach the time limit for four out of the five runs. Both PDLP and Gurobi
Barrier can solve the problem, while PDLP is averagingly twice as fast as Gurobi Barrier. This
demonstrates that solving the huge-scale overall planning problem with the LP-based method is
tractable with modern computing architectures and optimization solvers.
1https://developers.google.com/optimization/lp/lp_advanced
Online Appendix Page 11

Table A4: Experiment Results for Overall Planning
Solving MethodPDLP Barrier Primal Sim-
plex
Dual Sim-
plex
Number of Threads 4 4 1* 1*
Able to Solve the Problem Correctly? Yes Yes Yes No
Average Solving Time (Sec) 27,458 56,236 171,396 **
Number of Iterations 3,328 208 206 **
Ratio of Cases Reaching the Time Limit 0 0 80%*** **
Notes. In total, the problem contains 265,646,022 variables, 26,423,572 constraints, and 962,620,739 non-zeros. We
run each experiment with the same settings 5 times and take the average of each metric to report. In cases where the
solving time limit is reached before the solution is given, we use the time limit(172,800 seconds) as its solving time
in terms of calculating the average solving time. * For Primal and Dual simplex methods, Gurobi only allows 1
thread to solve the problem, which cannot be altered. ** Dual simplex fails to give the correct solution, of which
the metrics will not be reported. *** Only 1 out of 5 instances finished solving within the time limit.
A.6 Representation of the Random Sample from the Full-Scale Experiment
We report a corresponding table to Table 2 in the main draft, constructed using the random sample
from the full-scale experiment. As observed, the primary difference lies in the fact that theLP90
group does not demonstrate a statistically significant improvement in number of purchases relative
to the score-based benchmark.
Table A5: Representation of the Random Sample
LP90 LP95
(Treatment 1) (Treatment 2)
Purchases0.23% (0.51) 7.77%*** (<0.001)
GMV2.16% (0.11) 6.09%*** (<0.001)
Revenue3.07%*** (<0.01) 6.63%** (0.01)
Notes. We report the relative changes of the two treatment groups
(LP90andLP95) compared with control group (Benchmark),
i.e., the score-based algorithm for the random sample of the full-
scale experiment. Associatedp-values from pairwiset-tests are
reported in parentheses. The sample size in Treatment 1 is
Ntreatment1 = 126,713, in Treatment 2 isN treatment2 = 136,759,
and in the Control group isNcontrol = 126,875. ***p <0.01, **
p <0.05, *p <0.1.
A.7 Supplementary Evidence on Items Favored by the LP-Based Algorithm
In this section, we provide supplementary evidence on items favored by the LP-based algorithm
using the sampled impression-level data from the field experiment. This dataset contains only ag-
gregated features of sponsored listings. We focus on two key features. The first isLog Average Price,
which captures the logarithm of the average product price across all items in a sponsored listing.
Online Appendix Page 12

The logarithmic transformation mitigates the influence of extreme values. The second feature is
Weighted PTR, a measure of the predicted likelihood of purchase. Formally, it is defined as the
inner product of the position weight vectorhand the relevance score vectorr.
We implement the following empirical strategy setup:
Yi =β 0 +β 1 ×Algo90 i +β 2 ×Algo95 i +η t +ϵ i,(23)
where for a given impression indexed byi,Y i is the dependent variable, andYi ∈ {Log Average
Price,Weighted PTR}. Algo90i,Algo95 i are indicators representing which algorithms the current
impression has been assigned to (i.e.,LP90orLP95; if both are zero, then it is assigned to
Benchmark).β 1 andβ 2 are the parameters of interest, capturing the effects ofLP90andLP95
on the dependent variable of interest relative to the score-based algorithm. We include day fixed
effectsη t to account for any time-related heterogeneity.ϵi is the error term.
Table A6: Sponsored Listing Characteristics Fa-
vored by the LP-based Algorithm.
Log Average Price Weighted PTR
LP90 -0.064*** 0.117
(0.002) (0.091)
LP95 -0.109*** 0.483***
(0.002) (0.074)
Notes. Observation numbers areN= 2,071,833. Ro-
bust standard errors are reported in parentheses. ***
p <0.01, **p <0.05, *p <0.1.
Table A6 reports how the LP-based algorithms (LP90andLP95) alter the characteristics of spon-
sored listings relative to the score-based benchmark. BothLP90andLP95significantly reduce
theLog Average Priceof displayed items, withLP90lowering it by 0.064 andLP95by an even
larger 0.109. This contrasts with the results in Section 5.2.2. Specifically, the average product
price in our random sample from the full-scale experiment is 2.69 USD, compared to 301.31 USD
in the pre-experiment sample, indicating that the two samples differ substantially in product cate-
gories. This suggests that the LP-based algorithms prioritize items with higher expected revenue,
consistent with our main findings in Section 5.2.2, rather than systematically favoring either more
expensive or cheaper products. For lower-priced categories, demand effects dominate, leading to the
Online Appendix Page 13

observed price decreases in Table A6. Conversely, for higher-priced categories, price effects domi-
nate, resulting in price increases among displayed items in Section 5.2.2. Importantly, the observed
improvements of the LP-based algorithms cannot be attributed to changes in transaction prices,
as shown in Section 5.1. The relative changes in average transaction price are small and statisti-
cally insignificant for both treatments (LP95: –0.23%;LP90: –0.20%). RegardingWeighted PTR,
LP90shows no statistically significant change, whereasLP95yields a sizable and highly significant
increase of 0.483, consistent with the findings in Section 5.2.2.
A.8 The Revenue-Relevance Trade-Off
In this section, we provide some empirical evidence for the revenue-relevance trade-off. Through our
LP model, we can identify the trade-off between revenue and relevance. When the hyperparameter
λin problemP 1 increases, the relevance increases while the optimal revenue decreases.
From September 13th, 2022 to September, 27th, 2022, we conducted a second A/B test on the same
marketplace (dWeb), in which we mainly focused on exploring the comparison of performances for
various values ofλ. In total, we have set up four experiment groups, which are named respectively
LP90,LP85,LP80, andLP75, taking the associatedλto be 0.90, 0.85, 0.80, and 0.75. In
total, we count 17,931,775 unique consumers and 199,681,466 impressions. Specifically,LP90was
assigned 4,483,091 consumers, generating 49,916,423 impressions;LP85was assigned 4,487,531
consumers, generating 49,983,811 impressions;LP80was assigned 4,479,883 consumers, generating
49,883,948 impressions;LP75was assigned 4,481,270 consumers, generating 49,897,284 impressions.
We concentrate on two metrics:Revenue per consumerandPurchases per consumersince these are
the most essential evaluation metrics for revenue and relevance, as we explained before.
We setLP75to be the benchmark, of which we compute the relative change of metrics for other
groups over. Figure 1 shows the apparent trade-off over these two metrics. ForRevenue per con-
sumer, compared toLP75, the relative changes ofLP90,LP85,LP80are 1.24%, 0.60%, and
0.30%. For thePurchases per consumer, compared toLP75, the relative changes ofLP90,LP85,
LP80are -1.19%, -0.89%, and 0.11%. Asλ, the hyperparameter controlling the overall relevance,
decreases,Purchases per consumerdrops as well whileRevenue per consumerincreases.
Online Appendix Page 14

(a) Relative change of number of purchases
 (b) Relative change of revenue
Figure 1:Plots with the error bar showing the comparison of the relative change of (a) the
Purchases per consumer and (b) Revenue per consumer forLP90,LP85,LP80, andLP75.
A.9 Empirical Evidence on Revenue Independence between SLR and KR
In this section, we examine whether the observed increases in SLR revenues may partly cannibalize
the purchases and revenues of theseed item. To investigate this possibility, we draw on the sampled
data collected prior to the launch of the field experiment, which includes revenue information for the
seed item. For each impression, we define KR revenue as the revenue that Marketplace A generates
from sales of theseed item. Using three empirical tests, we find no evidence that increases in SLR
revenue may reduce KR revenue.
Test 1: Pearson correlation.For each impressioni, we denote KR revenue asRevenueKR i
and SLR revenue asRevenueSLRi. Then we compute the Pearson correlation coefficient between
RevenueKRi andRevenueSLR i across all impressionsi= 1,· · ·,266,003. The resulting correlation
coefficient is0.001with p-value of0.901, indicating no significant correlation betweenRevenueKRi
andRevenueSLR i.
Test 2: Granger causality test.We conduct a Granger causality test (Granger 1969) to examine
whether the sequence ofRevenueSLRihelps forecastRevenueKRiat various lags, which would
indicate a potential dependency. Since our sampled impressions include timestamps, we are able to
order them chronologically and construct the required lag structures. As reported in table A7, the
results reveal no evidence of a significant causal relationship. Across all tested lag lengths (1, 2, 10,
Online Appendix Page 15

and 20), the p-values remain non-significant, suggesting that SLR revenue does not Granger-cause
KR revenue.
Table A7: Granger Causality Test Results
Lag=1 Lag=2 Lag=10 Lag=20
SSR F-test 0.0230 (0.8795) 0.0221 (0.9781) 0.0131 (1.0000) 0.9239 (0.5560)
SSR Chi2-test 0.0230 (0.8795) 0.0442 (0.9781) 0.1311 (1.0000) 18.5267 (0.5528)
Likelihood Ratio 0.0230 (0.8795) 0.0442 (0.9781) 0.1311 (1.0000) 18.5157 (0.5535)
Parameter F-test 0.0230 (0.8795) 0.0221 (0.9781) 0.0131 (1.0000) 0.9239 (0.5560)
Notes. The table presents Granger causality test statistics with corresponding p-values in parentheses for
different lags (1,2,10,20).
Test 3: Pooled OLS.We further conduct an analysis restricted to sessions with identifiable user
IDs. Leveraging our panel of 157,154 impressions from 153,275 unique users, we examine how KR
revenue relates to the characteristics of SLR and SLR revenue. To estimate this relationship, we
employ a pooled Ordinary Least Squares (OLS) regression, clustering standard errors at the user
level.
We set up the following specification:
RevenueKRi =α+βRevenueSLR i +γ 1LogSeedPricei
+γ 2LogSponsoredListingPricei +γ 3AdRatei +δ d +τ h +ϵ i.(24)
LogSeedPricei denotesthelogarithmofthepriceoftheseediteminimpressioni,LogSponsoredListingPrice i
refers to the average logarithm of the prices of the SLR items in impressioni, andAdRateicaptures
the average ad rate of the SLR items in impressioni. In addition, we control for day fixed effects
(δd) and hour fixed effects (τh). Standard errors are clustered at the user level. Table A8 shows
that the relationship is not statistically significant, consistent with the results of the previous two
empirical tests. Overall, the evidence suggests that in our setting, improvements in SLR revenue
do not materially cannibalize the revenue of theseed item.
A.10 Stability of Experimental Results: Implication for Long-Term Effects
A key concern in interpreting short-term experiment results is whether the observed treatment
effects persist beyond the experimental window or merely reflect transient responses. Since our goal
Online Appendix Page 16

Table A8: KR Revenue and SLR Revenue.
KR Revenue
SLR Revenue -0.0003
(0.000)
LogSeedPrice 0.1186
(1.650)
LogSponsoredListingPrice -1.8418
(2.196)
Ad Rate 2.0584**
(0.889)
Observations 157,154
Notes. Standard errors clustered at the user level are
reported in parentheses. ***p <0.01, **p <0.05, *
p <0.1.
is to infer long-term impacts from a 17-day online A/B test, it is crucial to evaluate whether the
treatment effects of the LP-based ranking algorithms (LP90andLP95) remain stable across the
duration of exposure. To this end, we conduct empirical tests of the temporal stability of treatment
effects.
We begin by dividing the chronologically ordered impression stream intoB∈10,20,40equal-
sized exposure bins, indexed from early to late impressions. Within each bin, we compute average
outcomes for each algorithm, including the number of purchases and revenue generated for the
marketplace. Formally, letNdenote the total number of chronologically ordered impressions in the
dataset. For a chosen number of binsB, we partition the stream as follows:
Bb ={t:⌊ tN B ⌋=b}, b= 0,· · ·, B−1.(25)
so that each exposure bin contains approximatelyN/Bsequential impressions.
Our impression-level dataset consists of randomized assignments to one of three ranking algorithms:
the benchmark score-based algorithm and the two LP-based alternatives (LP90andLP95). From
these, we compute bin-level average treatment effects (ATEs) by comparing outcomes in each LP-
based group against the benchmark. Specifically, let¯Yg,b denote the mean of an outcome variable
(either Revenue per Impression or Number of Purchases) for algorithmgin binb. Then the bin-level
Online Appendix Page 17

ATEs are defined as:
ATE90,b = ¯YLP90,b − ¯YBenchmark,b,ATE 95,b = ¯YLP95,b − ¯YBenchmark,b.(26)
Finally, to test for temporal trends in treatment effects, we regress the bin-level ATEs on bin indices:
ATEg,b =β 0,g +β 1,gb+ϵ g,b, b= 0,· · ·, B−1.(27)
This specification allows us to assess whether treatment effects are stable over time (β1,g = 0) or
exhibit systematic upward or downward trends.
Table A9: Stability of Experimental Results.
LP90 LP95
Bin Number Purchases Revenue Purchases Revenue
B = 10 0.012 -0.0002 0.008 0.000
(0.007) (0.001) (0.011) (0.000)
B = 20 0.009* 0.000 0.006 0.000
(0.006) (0.000) (0.006) ( 0.000)
B = 40 0.008 0.0004 -0.008 -0.0002
(0.006) (0.001) (0.008) (0.000)
Notes. Robust standard errors are reported in parentheses. ***p <
0.01, **p <0.05, *p <0.1.
Table A9 shows that, across all bin numbers and outcome variables, there is no statistically signif-
icant evidence of any systematic trend in the experimental data, suggesting that our experimental
results are likely to hold in the long run.
Online Appendix Page 18
