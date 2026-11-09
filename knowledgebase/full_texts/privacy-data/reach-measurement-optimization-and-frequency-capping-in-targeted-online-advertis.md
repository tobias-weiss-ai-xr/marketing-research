---
title: Reach Measurement, Optimization and Frequency Capping In Targeted Online Advertising Under k-Anonymity
url: https://arxiv.org/abs/2501.04882
category: privacy-data
subcategory: measurement
date: 2025-01
venue: arXiv (Cornell University)
authors:
- Yuan Gao
- Mu Qiao
source: arxiv
pdf_url: https://arxiv.org/pdf/2501.04882
pages: 17
chars: 47677
fetched_at: '2026-11-08T12:57:59+00:00'
kb_version: 1
---

# Reach Measurement, Optimization and Frequency Capping In Targeted Online Advertising Under k-Anonymity

Reach Measurement, Optimization and Frequency Capping In
Targeted Online Advertising Under k-Anonymity
Yuan Gao
LinkedIn Corporation
Sunnyvale, CA, USA
yugao@linkedin.com
Mu Qiao
LinkedIn Corporation
Sunnyvale, CA, USA
mqiao@linkedin.com
Abstract
The growth in the use of online advertising to foster brand awareness over recent
years is largely attributable to the ubiquity of social media. One pivotal technology
contributing to the success of online brand advertising is frequency capping, a
mechanism that enables marketers to control the number of times an ad is shown to
a specific user. However, the very foundation of this technology is being scrutinized
as the industry gravitates towards advertising solutions that prioritize user privacy.
This paper delves into the issue of reach measurement and optimization within
the context of k-anonymity, a privacy-preserving model gaining traction across
major online advertising platforms. We outline how to report reach within this new
privacy landscape and demonstrate how probabilistic discounting, a probabilistic
adaptation of traditional frequency capping, can be employed to optimize cam-
paign performance. Experiments are performed to assess the trade-off between
user privacy and the efficacy of online brand advertising. Notably, we discern a
significant dip in performance as long as privacy is introduced, yet this comes with
a limited additional cost for advertising platforms to offer their users more privacy.
1 Introduction
Digital advertising now represents a significant proportion of the global ad expenditure (Statista,
2023). Thanks to its innate capacity for targeted and personalized ad delivery, digital advertising has
become an effective platform for performance-based marketing. The key to effectiveness lies largely
in relevancy. Initially, marketers identify potential customers by delineating their audience according
to user geolocation and interests. This process is further refined as digital advertising platforms match
users and ads based on real-time relevance, preventing advertisers’ budgets from being squandered
on less-engaged audiences. Furthermore, major online publishers now offer automated tools to aid
advertisers in optimizing for their desired outcomes, such as purchases or app downloads. The
capacity to measure and drive immediate impact via automated systems forms the backbone of the
swift growth of online advertising.
Conversely, traditional marketing places substantial emphasis on brand advertising. The objective of
brand advertising, unlike performance-based marketing, is to nurture long-term relationships with
customers. This aim is pursued through consistent ad exposure to audiences who demonstrate potential
interest in the brand. However, unlike performance-based advertising where more conversions
translate to better outcomes, increased impression volume does not always yield desirable results in
brand ads. Studies indicate that ad over-exposure negatively impacts the brand (Broussard, 2000; Ma
et al., 2016). In response to this issue, the industry often employs frequency capping. Specifically,
in a brand advertising campaign, a frequency cap of c ensures an ad from the campaign is shown a
maximum of c times to the same user. In brand marketing, it’s typical to define the campaign objective
as maximizing impressions, subject to a frequency cap constraint. The objective is commonly referred
to as reach when c = 1, as it represents the number of unique targeted users served. However, for
Preprint.
arXiv:2501.04882v1  [cs.GT]  8 Jan 2025

simplicity, we refer to the general objective as reach in this paper, reserving the term unique reach for
the case when c = 1.
A key competitive advantage of online advertising platforms over traditional media is their ability to
enforce frequency capping at the individual user level. Yet, as privacy concerns escalate, tracking
individual users may no longer be a viable option in the future (Iwa ´nczak and Rumi ´nski, 2022).
Privacy protecting protocols are being implemented by leading online advertising platforms to protect
the privacy of their user data (LinkedIn, 2023; Google, 2023). These measures leverage generalization
techniques to ensure k-anonymity (Samarati and Sweeney, 1998), a feature that makes an individual
user indistinguishable from a group of otherk −1 users. This paper delves into the reach measurement
and optimization issue within this privacy paradigm.
1.1 Related Work
Traditional reach optimization research often operates under the assumption of known user identities,
with a focus on challenges such as frequency capping and constrained ad matching problems (Mehta
et al., 2007; Feldman et al ., 2009; Buchbinder et al ., 2014; Hojjat et al ., 2017). More practically,
modern online advertising platforms often run under popular auction formats such as first and second
price auctions, and campaign optimization under these auction formats are usually studied under
optimal bidding (Balseiro and Gur, 2019; Gao et al., 2022; Maehara et al., 2018; Zhang et al., 2014).
However, these methodologies are met with significant hurdles when applied in scenarios where
privacy protection protocols obscure full knowledge of user identities.
The preservation of privacy in digital advertising has attracted considerable research interest, with a
significant focus on the issue of cross-publisher reach measurement in environments lacking third-
party cookies. Influential studies propose the establishment of common identifiers across publishers
used exclusively for aggregate measurement (World Federation of Advertisers, 2023). Notably,
(Skvortsov and Koehler, 2019) suggests a method for assigning virtual identifiers across various
domains. With these unified identifiers in place, it becomes possible to amalgamate measurement
statistics from different publishers using differentially-private solutions, which rely on either global
(Kreuter et al., 2020) or local (Wright et al., 2021) summarization algorithms.
Additional research avenues include exploring the intermediary stage where partial cross-publisher
activity data is available from users who have given their consent to be tracked (Sang et al., 2022). In
such instances, machine learning algorithms have been proposed as a means of learning from this
data to infer and optimize non-trackable requests.
Distinguished from the existing body of work, this paper anticipates future scenarios where user
privacy is stringently maintained, even within the context of first-party domains. The aim of this
work is to evaluate the efficacy of measurement and optimization strategies under a specific privacy
protocol, namely the k-anonymous privacy protocol.
1.2 The k-anonymous Privacy Protocol
In the realm of online advertising, the concept of k-anonymity plays a pivotal role in balancing
the effectiveness of targeted advertising with the imperative need for user privacy. This protocol is
adeptly implemented by publisher platforms, such as social media sites, search engines, or content
providers, which meticulously form user groups (Epasto et al ., 2021). Each group comprises k
members, safeguarding individual user actions by making them indistinguishable from k − 1 others
within the same cohort. These groups are thoughtfully created based on common user attributes like
geolocation and interests. When a user visits the publisher and triggers an ad request, their information
is forwarded to a separate identification system, which returns one of the groups containing the user.
This group identity is then utilized by the downstream advertising system to make decisions on ad
displays, ensuring that only group-level information is used, in order to maintain user anonymity
(Figure 1).
While the optimal computation of k-anonymity is recognized as an NP-hard challenge(Meyerson and
Williams, 2004), pragmatic algorithms have emerged (Pascale et al., 2023; Bonizzoni et al., 2013),
facilitating its application in diverse real-world settings. Furthermore, the concept of k-anonymity
seamlessly extends to certain advertising contexts, such as television ads targeted at households. Here,
the ad is directed at a family unit, inherently forming a k-anonymous group, where the television
2

User Publisher
1 2
3 4
5 6
7 8
9 10
11 12
1
User-group identification system
User id
Group id
Ads ranking system
1
2
3
4
AD
Figure 1: Illustration of the k-anonymous Privacy Protocol, highlighting the process from user visit
to ad display within the framework of k-anonymity.
network, by default, ensures a level of k-anonymity by targeting the household collectively rather
than its individual members.
It’s important to delineate the distinct roles of the publisher platform and its advertising system
within this privacy-centric framework. The publisher platform is entrusted with the development
and management of the k-anonymity algorithm and the formation of user groups, underscoring its
commitment to privacy. Conversely, the advertising system operates under the privacy constraints
established by these groups, aiming to deliver personalized advertising content in a manner that
respects user anonymity.
From the vantage point of the advertising system, our objective is to navigate the intricacies of
k-anonymity to optimize ad delivery while upholding the privacy standards set forth by the publisher
platform. This involves devising strategies that maximize advertising effectiveness within the bounds
of k-anonymous groups, ensuring that ads are relevant and impactful, yet privacy-compliant. By
embracing this challenge, we contribute to the sustainable evolution of online advertising, where the
personalization will coexist with privacy.
2 Notations
We use i to index individual users, j to indicate user groups, and t to signify ad requests originating
from a user group. As the primary focus of this research is the measurement and optimization of
reach for a single ad campaign, there’s no need to introduce additional indices for multiple campaigns.
For the campaign in question, we assume its frequency cap is c and it targets a total of N users. For
simplicity, we presume that the targeted user indices range from 1 to N. These targeted users are
assigned to M distinct user groups, which collectively generate a total of T ad requests.
Each ad request t is generated by an unidentified user. However, the system has access to jt, the
index of the user group generating ad request t. We use pt to denote the probability that ad request t
comes from a user who has previously been served fewer than c times.
We define Uj as the set of targeted user indices in group j. Formally,
Uj :=

i

 user i is in user group j ∧ user i is targeted  ,
We also define Gi as the set of group indices containing user i:
Gi := {j | user i is in user group j } .
We use the random variable Xi to denote the number of times user i has viewed the ad.
3

For any given set S, we denote its cardinality as |S|. We represent the probability density function
(p.d.f.) and cumulative density function (c.d.f.) of a Binomial distribution B(n, p) using f (·; n, p)
and F (·; n, p) respectively, i.e., for all x ≤ n,
f (x; n, p) :=
n
x

px(1 − p)n−x,
and
F (x; n, p) :=
xX
i=0
n
i

pi(1 − p)n−i.
Here we extend the domain of f and F to x > nby defining
f (x; n, p) := 0, and F (x; n, p) := 1, ∀x > n.
Finally, ϕ and Φ denote the p.d.f. and c.d.f. for the standard normal distribution, respectively.
3 Reach Measurement
Under k-anonymity, the ability to track users at an individual level is compromised, making accurate
reach measurement challenging. In this section, we focus on estimating reach when only the user
group impressions are accessible. It’s essential to keep in mind that these impressions result from
auction-based bidding. The specifics of the reach optimization problem are outlined in Section 4.
As discussed in the introduction, typically, an ad campaign operates under a pre-determined frequency
cap c, where reach is defined as the total number of impressions served within this cap. However,
advertisers often require the reach metric for a variety of frequency caps. For instance, an advertiser
may set the frequency cap at c = 2 to ensure that targeted users don’t see the ad more than twice.
Still, it would be beneficial for the publisher to report the unique number of users served by the ad.
Time is another important factor. Advertisers frequently assess campaign reach during the campaign
flight, necessitating real-time updates of reach metrics. Additionally, reach metrics should accommo-
date range-based queries to enable advertisers to access reports for any given time frame, such as
reach within the past week or month.
Formally, a time window identifies a subset of indices from the set 1, . . . , T. Let nj be the number of
impressions for the ad campaign from user group j within this window. The theorem below details
the expected reach under a given frequency cap.
Theorem 1 (Reach in Expectation) The expected reach under a given frequency capc ≥ 1 is given
by
NX
i=1


cX
l=1
lf

l; X
j∈Gi
nj, 1 k

 + c − cF

c; X
j∈Gi
nj, 1 k



 . (1)
In the special case where c = 1, the following Corollary applies:
Corollary 1 Let nj be the number of impressions of the ad campaign from user group j, then the
expected number of unique reach is
NX
i=1

1 −

1 − 1 k P j∈Gi nj ! . (2)
For the other extreme, as c → ∞, equation (1) simply becomes 1 k P i P j∈Gi nj, the expected total
impressions. This number is bounded above by P j nj, the total group impressions. This upper limit
is reached when all users within the groups are targeted.
It’s also worth noting that in the degenerate case where k = 1 and each user belongs to a distinct
group, Theorem 1 and Corollary 1 provide deterministic reach counts.
Theorem 1 allows the publisher to compute reach metrics for any given time window. In addition,
the following alternative formulation of (1) also facilitates a streaming algorithm that updates the
expected reach as new impressions are observed, with a time complexity of O(kc2) and a space
complexity is O(cT ).
4

Corollary 2 The following is an alternative form of the expected number of reach under a frequency
cap c. In other words, (1) can be written as
NX
i=1

c −
c−1X
l=0
(c − l)f

l; X
j∈Gi
nj, 1 k



 .
3.1 Bounds on the Estimate
Apart from consistently reporting the correct reach metric in expectation, it is also crucial to under-
stand the extent to which the actual reach can diverge from the expectation. For instance, when the
groups do not overlap, the reach’s lower bound R(c) is simply PM j=1 min(nj, c), achievable when
requests from each group originate consistently from the same user. Conversely, the upper bound of
R(c) is PM j=1 min(nj, c|Uj|), realizable when, for example, targeted users in a group are catered to
in a round-robin manner. The upper and lower bounds for the general case involving overlap can be
complex to represent mathematically, but they can be computed using greedy algorithms.
When it comes to concentration bounds on the reach metric R(c), it is significant to acknowledge that
although R(c) = P i Ri(c) is a sum of random variables, Hoeffding’s inequality does not apply in this context since Ri(c) are typically negatively correlated for users within the same group. Instead,
we can calculate the variance ofR(c) and apply Chebyshev’s inequality to derive probabilistic bounds
on the deviation. However, the analytical form of the variance for generalc is of combinatorial nature.
Consequently, we present an explicit bound on R(1). It hinges on the following lemma. For notation
simplicity, we denote R := R(1) as the reach when c = 1.
Lemma 1 (Covariance) Let Ri = min(Xi, 1), where Xi represents the number of impressions from
user i. For two users i, i′, let G∩ := Gi ∩ Gi′ represent their intersecting groups andG∪ := Gi ∪ Gi′
their union. If nj denotes the number of impressions of the ad campaign from user group j, then the
covariance Cov[Ri, Ri′] is given by 
1 − 2 k P j∈G∩ nj −  1 − 1 k 2 P j∈G∩ nj ! ×

1 − 1 k P j∈G∪ −G∩ nj . (3)
Together with the observation that in this scenario Var[Ri] = E[Ri](1 − E[Ri]), which equates to
1 −

1 − 1 k P j∈Gi nj !  1 − 1 k P j∈Gi nj , (4)
we obtain the following theorem.
Theorem 2 (Concentration Bounds) The probability that R deviates its expectation E[R] (given in
Theorem 1) by ϵσ is bounded by
P (|R − E[R]| ≥ϵσ) ≤ 1 ϵ2 ,
where
σ2 = X
i
Var[Ri] +
X
i̸=i′
Cov[Ri, Ri′], (5)
where Var[Ri] is given by (4) and Cov[Ri, Ri′] is given by (3).
For general c >1, we can compute the variance of R(c) using Monte Carlo methods. For more
information, refer to Section 5. Finally, the subsequent theorem offers estimates on over-exposure,
crucial for advertisers concerned about its negative impact.
Theorem 3 (Over-exposed Users) If nj denotes the number of impressions of the ad campaign from
user group j, then the expected count of over-exposed users (served more than c times) is
N −
NX
i=1
F

c; X
j∈Gi
nj, 1 k

 .
5

3.2 Relaxing the Uniformity Assumption
The prior sections rely on a key assumption that each user within a group has an equal probability of
generating a group request. While this simplification is essential for privacy protection, it doesn’t
accurately capture real-world scenarios. However, under specific conditions, specifically when user
groups do not overlap and advertisers define their target audience at a level less granular than these
groups, we can improve ad performance without compromising k-anonymity.
Let’s consider a scenario in which the ad platform can estimate each individual user’s visit frequency.
In such a case, we could associate each group j with a property vector (qj1, qj2, . . . , qjk ), where
qj1 ≤ qj2 ≤ . . .≤ qjk and P l qjl = 1. This vector represents the user visit probabilities within group j. To maintain k-anonymity, the ad system is only permitted to access these probabilities
without linking them to specific users. For instance, a group with a property vector of (0, 0, ...,0, 1)
would signal to the ad system that there is a single active user in the group, while the rest are inactive;
however, the system would not be able to identify the active user. The following theorem provides
the expected reach for a user group in this setup.
Theorem 4 Given nj as the number of impressions of the ad campaign from user group j with
property vector (qj1, qj2, . . . , qjk ), the expected reach generated from user groupj under frequency
cap c can be expressed as:
kX
i=1
 cX
l=1
lf (l; nj, qji) + c − cF (c; nj, qji)
!
.
The total reach of the campaign can then be derived by summing up the reach from each group, as
we are assuming the groups do not overlap. In the case of unique reach ( c = 1), we can state the
following:
Corollary 3 Given nj as the number of impressions of the ad campaign from user group j with
property vector (qj1, qj2, . . . , qjk), the expected number of unique reach from user groupj can be
defined as:
k −
kX
i=1
(1 − qji)nj .
4 Reach Optimization
Measurement and optimization play pivotal roles in online advertising platforms, as they are essential
tools that help marketers achieve a solid return on investment. Reach measurement is typically
displayed on an ad reporting page within the publisher platform, allowing marketers to identify gaps
in audience coverage and evaluate the effectiveness of their marketing strategies. Meanwhile, reach
optimization is often offered by the platform through an automated bidding service, which places
bids on behalf of advertisers in each auction to optimize results. As the outcome is reported by the
measurement component, it is crucial that these two elements maintain consistency with one another.
In this section, we focus on the reach maximization problem with regard to an ad campaign, which
comprises an ad, a budget, and a targeted user set. In traditional scenarios where user identity is
readily available, the advertising platform tracks the frequency of ad impressions per user. It halts
the campaign for a given user once the frequency cap c is reached. Here, we expand the reach
optimization problem to account for ad requests originating from user groups.
Let T denote the total number of ad impressions initiated by the targeted users’ viewing or search
sessions. Each impression is generally auctioned either via a first-price or second-price auction, with
the winning bid claiming the impression. The objective of an ad campaign is to secure as many
impressions as possible while ensuring that each targeted user receives the ad at most c times. For
instance, when c = 1, the goal is to reach as many unique targeted users as possible.
Consider the t-th impression and define Wt(b) as the winning probability given a bid price of b
and Ht(b) as the expected cost. Let their respective derivatives be wt and ht. Let B denotes the
6

campaign’s budget. We solve the following optimization problem to optimize reach:
max
bt
TX
t=1
ptWt(bt), s.t.
TX
t=1
Ht(bt) ≤ B, (6)
where pt is the likelihood that the t-th impression originates from a targeted user who has seen
the campaign’s ad fewer than c times. In a deterministic environment, if the user generating the
impression is known, pt is binary, thus recovering the traditional frequency capping mechanism.
Section 4.1 explains how to calculate pt in a stochastic scenario where only the user’s group is
identifiable. The term ptWt(bt) specifies the marginal contribution of the t-th impression, so this
natural probabilistic frequency capping extension directly relates to the campaign’s optimization
objective.
Let λ be the Lagrangian multiplier for the budget constraint, then the optimal bid b∗ t given λ is
b∗ t (λ) =
 ht
wt
−1  pt
λ

, (7)
where (·)−1 signifies function inverse. The optimal Lagrangian multiplier λ∗ satisfies the KKT
condition
TX
t=1
Ht(b∗ t (λ∗)) = B.
In practical terms, λ∗ can be obtained via an online solver (Gao et al., 2022).
4.1 Estimating Reach Probability
As discussed in the previous section, the crucial quantity in Equation 7 is pt. This is the probability
that the request comes from a user who has viewed the ad fewer than c times.
Consider a campaign focused on maximizing unique reach (c = 1), within a user group composed of
two targeted users: A and B. Suppose the group generates two ad requests indexed by 1 and 2. For
the first request, p1 = 1 since it is the initial time we encounter this group. If the campaign secures
this impression, the next time this group visits the publisher, we know that either A or B has seen the
ad. Hence, there is only a 50% chance that we can reach a unique user, and therefore, p2 = 0.5.
Formally, let ntj denote the number of impressions of the ad campaign from user group j up until the
t-th ad request. Let jt represent the index of the user group that generates the t-th ad request. We
then have the following formula for pt.
Theorem 5 (Probability of Additional Reach) Assume that user group jt generates ad request t.
The probability pt that ad request t comes from a user who has viewed the ad fewer than c times is
given by
pt = 1 k X i∈Ujt F

c − 1; X
j∈Gi
ntj, 1 k

 . (8)
As a remark, as c → ∞, we find that pt → 1, in which case, the optimization problem in(6) simplifies
to an impression volume optimization. For the specific case where c = 1, we have the following
corollary.
Corollary 4 For a campaign optimizing for unique reach, we have
pt = 1 k X i∈Ujt

1 − 1 k P j∈Gi ntj .
It’s noteworthy that the probability pt decreases exponentially with ntj for a specific group j. To
see how the winning probability diminishes as the group impression count increases, consider
pt = exp(−αntj), where α >0 is a parameter that depends on the group size. At the extremes, for a
group of size k = 1, we have α → +∞, and α → 0 as the group size k → ∞.
7

Assuming a winning probability model in which the bids of competing campaigns follow a log-
normal distribution for thet-th request from group j, i.e., Wt(b) = Φ((ln b−µt)/σt), the relationship
between the winning probability and the number of impressions for group j can be expressed as
Wt(pt/λ) = Φ((−αntj − ln λ − µt)/σt). Generally, when the groups overlap, impressions from
other groups should also be taken into account, but the decay is of the same order.
Finally, pt can be computed in a streaming fashion with time complexityO(kc) and space complexity
O(cT ).
4.2 Non-uniform Setting
For completeness, we also present the reach probabilities pt in the non-uniform arrival setting
described in Section 3.2.
Theorem 6 Let ntj be the number of impressions of the ad campaign from user groupj with property
vector (qj1, qj2, . . . , qjk ), up until ad request t happens. Now suppose user group j generates the
t-th request, then the probability pt that ad request t is from a user that has been served less than c
times previously is
pt =
kX
i=1
qjiF (c − 1; ntj, qji) . (9)
In particular, for unique reach, pt = P i qji(1 − qji)ntj .
5 Experiments
This section outlines the experiments conducted to address a range of significant questions. Firstly,
we deploy Monte Carlo simulations on the reach distribution, demonstrating the accuracy of the
reach estimate and its variance progression throughout a campaign’s lifespan. Secondly, we show the
increase in measurement uncertainty as stricter user privacy is implemented. Next, we run tests on
campaign reach optimization under varying privacy levels, resulting in an efficiency versus privacy
tradeoff curve. This quantifies the influence of privacy on digital brand advertising performance.
Lastly, we also compare the performance of different methods on real-world datasets where user
arrival within a group is non-uniform.
5.1 Monte Carlo Simulations on Reach
The expected reach for a given set of group impressions is detailed in Theorem 1. In this initial
experiment, Monte Carlo simulations are conducted to derive the complete reach distribution. We
model a campaign with 120 targeted users and a frequency cap, c = 3. These targeted users are
divided into 20 groups, each containing k = 6 members. We randomly draw 250 impressions from
these groups and sample the potential user trajectories that generated these impressions. This data is
used to plot the reach distribution (Figure 2A), with the empirical mean from this distribution closely
aligning with the expected reach from Theorem 1.
Further analysis of the reach distribution evolution as impressions increase is illustrated in Figure
2B. When impressions are scarce, it is likely that most fall under the frequency cap and are counted
as reach, resulting in a small distribution variance. As impressions accrue, the variance initially
increases, but decreases as impressions become plentiful. This is due to the reach becoming saturated
as a result of the frequency cap amidst a high number of impressions.
Lastly, the variances across various group sizes are plotted in Figure 2C. This illustrates the effect
of heightened user privacy on the reach measurement’s uncertainty. At k = 1, the measurement
is deterministic. As user privacy is introduced ( k = 2), a substantial increase in variance occurs.
However, as we provide more user privacy, the growth in measurement uncertainty is minimal.
5.2 Privacy vs. Efficiency Tradeoff
Digital privacy is ushering in substantial changes within the advertising industry. There is a prevailing
consensus that the efficacy of online marketing risks being compromised as stronger privacy protection
8

A B C
Figure 2: Experiments on reach measurement. Reach is defined as the number of impressions under
the frequency cap. A: Distribution of reach with 250 impressions and a frequency cap of 3. The black
dashed vertical line indicates the mean of the sampled distribution. The red solid line depicts the
expected reach calculated from Theorem 1. B: Distributions of reach under different numbers of
impressions. C: Variance of reach with different group sizes.
is enacted. In this section we quantify the decline in brand advertising performance under different
privacy levels.
In this experiment, we construct a campaign that targets 120 users who generate a total of 2000 ad
impressions. These impressions are sold via second-price auctions hosted by the advertising platform.
The winning price (second price) of each request is drawn from a log-normal distribution with µ = 0
and σ2 = 0.5. The advertising platform maps these targeted users into groups of size k, and only the
group id is made available for each ad request. A bidding agent places bids on behalf of the advertiser,
adhering to the bidding formula (7). The λt is then updated based on the following online algorithm,
as suggested in (Balseiro and Gur, 2019; Gao et al., 2022):
λt+1 = λt − ε(1 − rt),
where rt signifies the ratio of the spend in request t and the average budget per request B/T . The
learning rate ε is set to 0.1. To imitate real-world scenarios in online production systems, lower and
upper bounds on bid prices are also established at 0.1 and 10, respectively. The starting bid λ1 is
fixed at 10.
The return on ad spend (ROAS), here defined as the ratio of total reach over total spend, is plotted
against varying group sizes (Figure 3). When no user privacy is in place (k = 1), the best possible
ROAS is achieved. ROAS for other scenarios is normalized against this optimal upper limit, facil-
itating easier comprehension of the performance decline percentage. As anticipated, performance
deteriorates monotonically as k increases. Notably, a 33% drop in ROAS is observed as user privacy
is introduced (shifting from k = 1 to k = 2). However, there isn’t a significant additional cost for
enhanced privacy. In the extreme case when all users form a single group, the situation mirrors
advertising on traditional media, where frequency capping is only applicable to the entire audience
population. Here, the efficiency is merely 62% of fully personalized online advertising.
5.3 Evaluation on Real-world Dataset
In practice the number of user impressions within a group can vary a lot. To bridge this gap, further
experiments were conducted using auction and impression data from a real-world advertising platform.
Users on the platform were randomly assigned to non-overlapping groups of size 20. Frequency
counts of each member within a group revealed a variation in their distribution across different groups,
as demonstrated in Figure 4.
In this experiment, we focus specifically on unique reach (c = 1). We evaluated four unique reach
measurement and optimization approaches on a total of 10 ad campaigns. These approaches include:
• A. Unique impressions: Each impression from a user group is considered a reach, leading
to an overestimation.
• B. Unique groups: Reach is defined as the number of unique group impressions, resulting
in an underestimation.
• C. Uniform reach: Reach is estimated using Theorem 1 and reach probability is calculated
via Theorem 4, which assumes a uniform distribution of user frequencies within a group.
9

no user privacy
full privacy, traditional media
Figure 3: Privacy vs. efficiency in online brand advertising. The relative ROAS is plotted against
different group sizes k representing different levels of user privacy.
Figure 4: Relative frequency of each user within a group. Distributions of six groups are shown.
Users are ranked based on their frequency.
• D. Non-uniform reach: Reach is estimated based on Theorem 5, and reach probability is
calculated via Theorem 6. For each group, the property vector is derived from actual user
visit frequencies in the dataset.
Using Rtrue as the ground truth reach and R as the measured reach, we calculated the relative error of
reach measurement for all methods using the formula |R − Rtrue|/Rtrue. As illustrated in Figure 5,
approach D provides the most accurate measurement among the four methods. It’s worth noting that
for D, we did not account for estimation errors in the property vectors. However, these can usually be
forecasted with a reasonable level of accuracy using historical user visit data. Importantly, approach
C (which assumes a uniform distribution within the group) consistently overestimates the actual
reach. This is because maximizing (9) in the probability simplex reaches its maximum with uniform
distribution.
To evaluate the reach optimization performance of these four approaches, we used the same bidding
algorithm described in Section 5.2, discounting the bids at each request level using the reach
10

Figure 5: Reach measurement performance comparison. The error metric of each campaign is plotted
as a dot. Error bars represent standard deviation. A, B, C, D represents the four approaches listed in
section 5.3.
A B C D
Mean 85.99% 88.42% 86.95% 94.12%
Variance 0.023 0.018 0.023 0.005
Table 1: Mean and variance of relative ROAS of the different approaches across the 10 campaigns. A,
B, C, D represents the four approaches listed in Section 5.3.
probabilities calculated from the different approaches. For each campaign, its bids in the auctions
were replaced by the output of the bidding algorithm, while other competing bids remained unchanged.
For all methods, we measured the relative ROAS compared to existing performance where no privacy
is enforced. The results are summarized in Table 1.
It’s evident that relaxing the uniformity assumption within user groups results in improved measure-
ment accuracy and advertising performance, primarily because this model better corresponds with
real-world user visit patterns. However, this approach necessitates that user groups do not overlap
and all calculations are conducted at the group level.
6 Final Remarks
To the best of our knowledge, this paper is the first to investigate reach measurement, optimization,
and frequency capping under the k-anonymous privacy protocol. We outline how to report reach
in this new privacy context and demonstrate how probabilistic discounting, a probabilistic variant
of traditional frequency capping, can be leveraged to optimize campaign performance. For ease of
presentation, we have assumed that all user groups are of equal size k. However, the findings are
adaptable to scenarios where user groups vary in size.
11

The privacy landscape is fast-evolving and it has profound implications on the future of digital
advertising. This study evaluates one of the many possible privacy protocols. Comparing the
advertising efficiency vs. user privacy tradeoffs of different privacy frameworks is an important future
research direction.
Finally, the comparative analysis of various methodologies for optimizing reach in real-world datasets
underscores the enhanced performance achieved by relaxing the uniform assumption. This finding
points to an encouraging path forward: incorporating realistic models of user behavior into the design
of reach optimization strategies, especially within the context ofk-anonymous environments, presents
a promising avenue for advancing the efficacy and precision of targeted online advertising while
upholding user privacy.
References
Santiago R Balseiro and Yonatan Gur. 2019. Learning in repeated auctions with budgets: Regret
minimization and equilibrium. Management Science 65, 9 (2019), 3952–3968.
Paola Bonizzoni, Gianluca Della Vedova, Riccardo Dondi, Yuri Pirola, and Raffaella Rizzi. 2013.
Parameterized complexity of k-anonymity: hardness and tractability. Journal of Combinatorial
Optimization 26, 1 (2013), 19–43. https://doi.org/10.1007/s10878-011-9413-7
Gerard Broussard. 2000. How advertising frequency can work to build online advertising effectiveness.
International Journal of Market Research 42, 4 (2000), 1–13.
Niv Buchbinder, Moran Feldman, Arpita Ghosh, and Joseph Naor. 2014. Frequency capping in online
advertising. Journal of Scheduling 17, 4 (2014), 385–398.
Alessandro Epasto, Andrés Muñoz Medina, Steven Avery, Yijian Bai, Robert Busa-Fekete, CJ Carey,
Ya Gao, David Guthrie, Subham Ghosh, James Ioannidis, et al . 2021. Clustering for private
interest-based advertising. In Proceedings of the 27th ACM SIGKDD Conference on Knowledge
Discovery & Data Mining. 2802–2810.
Jon Feldman, Aranyak Mehta, Vahab Mirrokni, and Shan Muthukrishnan. 2009. Online stochastic
matching: Beating 1-1/e. In 2009 50th Annual IEEE Symposium on Foundations of Computer
Science. IEEE, 117–126.
Yuan Gao, Kaiyu Yang, Yuanlong Chen, Min Liu, and Noureddine El Karoui. 2022. Bidding Agent
Design in the LinkedIn Ad Marketplace. arXiv preprint arXiv:2202.12472 (2022).
Google. 2023. How Google Anonymizes Data. Available at https://policies.google.com/
technologies/anonymization?hl=en-US. Last Accessed: 2023-08-07.
Ali Hojjat, John Turner, Suleyman Cetintas, and Jian Yang. 2017. A unified framework for the
scheduling of guaranteed targeted display advertising under reach and frequency requirements.
Operations Research 65, 2 (2017), 289–313.
Przemysław Iwa´nczak and Mateusz Rumi´nski. 2022. The future of frequency capping in privacy-
centric digital advertising. Available at SSRN 3985974 (2022).
Benjamin Kreuter, Craig William Wright, Evgeny Sergeevich Skvortsov, Raimundo Mirisola, and
Yao Wang. 2020. Privacy-Preserving Secure Cardinality and Frequency Estimation. Technical
Report. Google, LLC.
LinkedIn. 2023. Group Identity for LinkedIn Ads . Available at https://www.linkedin.com/
help/lms/answer/a543144. Last Accessed: 2023-08-07.
Hao Ma, Xueqing Liu, and Zhihong Shen. 2016. User fatigue in online news recommendation. In
Proceedings of the 25th International Conference on World Wide Web. 1363–1372.
Takanori Maehara, Atsuhiro Narita, Jun Baba, and Takayuki Kawabata. 2018. Optimal Bidding
Strategy for Brand Advertising.. In IJCAI. 424–432.
Aranyak Mehta, Amin Saberi, Umesh Vazirani, and Vijay Vazirani. 2007. Adwords and generalized
online matching. Journal of the ACM (JACM)54, 5 (2007), 22–es.
12

Adam Meyerson and Ryan Williams. 2004. On the Complexity of Optimal K-Anonymity. In
Proceedings of the Twenty-third ACM SIGMOD-SIGACT-SIGART Symposium on Principles of
Database Systems (PODS ’04). ACM, New York, NY , USA, 223–228.https://doi.org/10.
1145/1055558.1055591
Daniel De Pascale, Giuseppe Cascavilla, Damian A. Tamburri, and Willem-Jan Van Den Heuvel.
2023. Real-world K-Anonymity applications: The KGen approach and its evaluation in fraudulent
transactions. Information Systems 115 (May 2023), 102193. https://doi.org/10.1016/j.
is.2023.102193
P. Samarati and L. Sweeney. 1998. Protecting Privacy when Disclosing Information: k-Anonymity
and its Enforcement through Generalization and Suppression. Technical Report. Computer Science
Laboratory, SRI International. http://www.csl.sri.com/papers/sritr-98-04/
Qian Sang, Ravi Kant, and Niklas Karlsson. 2022. Feedback Control of In-Target Rate for Probabilis-
tic Frequency Cap in Online Advertising. In 2022 American Control Conference (ACC). IEEE,
5354–5359.
Evgeny Skvortsov and Jim Koehler. 2019. Virtual people: Actionable reach modeling. Technical
Report.
Statista. 2023. Share of digital in advertising revenue worldwide from 2019
to 2027 . Available at https://www.statista.com/statistics/375008/
share-digital-ad-spend-worldwide/ . Last Accessed: 2023-08-07.
World Federation of Advertisers. 2023. Cross-Media Measurement. Available at https://wfanet.
org/leadership/cross-media-measurement . Last Accessed: 2023-08-07.
Craig William Wright, Evgeny Sergeevich Skvortsov, Jason Frye, Jiayu Peng, Jim Koehler,
Joseph Goodknight Knightbrook, Laura Book, Michael Daub, Scott Schneider, Sheng Ma, Xichen
Huang, Ying Liu, Yunwen Yang, and Preston Lee. 2021.Privacy-centric Cross-publisher Reach
and Frequency Estimation Via Vector of Counts. Technical Report. Google, LLC.
Weinan Zhang, Shuai Yuan, and Jun Wang. 2014. Optimal real-time bidding for display advertising.
In Proceedings of the 20th ACM SIGKDD international conference on Knowledge discovery and
data mining. 1077–1086.
A Supplement Materials
A.1 Proofs
A.1.1 Proof of Theorem 1
Let Xi be the random variable for the number of times user i has seen the ad. For any impression
generated from a user group that contains user i, there is a 1/k probability that the ad request is from
user i. This corresponds to a Bernoulli trial with a success probability 1/k. Therefore within the
given time window, Xi ∼ B
P
j∈Gi nj, 1/k

, a Binomial distribution with the number of trials as
the sum of impressions generated from any user group that contains user i.
Denote R(c) as the random variable for the number of impressions under frequency cap c, and
Ri(c) := min(Xi, c) the number of impressions under frequency cap c for user i. Then E[R(c)] =P
i E[Ri(c)] := P i E[min(Xi, c)]. The result is then obtained by direct calculation, i.e.,
E[R(c)] =
NX
i=1
E[min(Xi, c)]
=
NX
i=1
E[Xi|Xi ≤ c] + cP (Xi > c)
=
NX
i=1
 cX
l=1
lf

l; X
j∈Gi
nj, 1 k

 + c − cF

c; X
j∈Gi
nj, 1 k


!
.
13

A.1.2 Proof of Corollary 1
This naturally comes as a special case of Theorem 1, but here we provide an alternative proof that
is more intuitive. Define Yi = min(Xi, 1), then E[Yi] = P (Yi = 1), the probability that user i is
reached at least once. With this probabilistic interpretation the conclusion is obvious.
A.1.3 Proof of Theorem 2
We first prove Lemma 1. The expectation of Ri is given in (2), i.e.,
E[Ri] =

1 −

1 − 1 k P j∈Gi nj ! .
With inclusion–exclusion principle, we have
P (RiRi′ = 0) = P (Ri = 0) + P (Ri′ = 0) − P (Ri = 0, Ri′ = 0)
=

1 − 1 k P j∈Gi nj +  1 − 1 k P j∈Gi′ nj
−

1 − 1 k P j∈G∪ −G∩ nj  1 − 2 k P j∈G∩ nj
Note that E[RiRi′] = P (RiRi′ = 1) = 1 − P (RiRi′ = 0), Therefore
Cov[Ri, Ri′] = E[RiRi′] − E[Ri]E[Ri′]
=

1 − 1 k P j∈G∪ −G∩ nj
×
 
1 − 2 k P j∈G∩ nj −  1 − 1 k 2 P j∈G∩ nj ! .
This concludes the proof of Lemma 1. Finally, the covariance formula allows us to calculate the
variance of reach, i.e.,
Var[
X
i
Ri] =
X
i
Var[Ri] +
X
i̸=i′
Cov[Ri, Ri′],
and Theorem 2 is derived by applying Chebyshev’s inequality.
A.1.4 Proof of Theorem 3
The number of users who are over-exposed is simplyPN i=1 P (Xi > c), so the result is straightforward given the distribution of Xi.
A.1.5 Proof of Theorem 4
Let Zi represent the random variable for the number of times the user with visit probability qji has
viewed the ad. In this case, Zi ∼ B(n, p). The proof follows a similar line of reasoning to that of
Theorem 1.
A.1.6 Proof of Theorem 5
Let Xi denote the random variable for the number of times user i has seen this ad. Then pt, the
probability that ad request t originates from a user who has viewed the ad fewer than c times, is
simply
pt = 1 k X i∈Ujt P (Xi < c),
which is an average of the probabilities for each user in group jt. As shown in the proof of Theorem
1, Xi follows a Binomial distribution with parameters P j∈Gi ntj and 1/k, leading us to (8).
14

ALGORITHM 1: Streaming Algorithm For Reach Measurement
Set n[i] = 0 for i = 1, . . . , N;
Set f [l, t] = 0, for l = 0, . . . , c; t = 0, . . . , T;
Set f [l, l] =
 1
k
l
for l = 0, . . . , c;
Set R[m] = 0, for m = 1, . . . , c;
for t = 1, . . . , Tdo
if the campaign wins request t from group jt then
for i in Ujt do
Increment n[i] by 1;
for l = 0, . . . , cdo
if n[i] > lthen
if f [l, n[i]] = 0 then
Set f [l, n[i]] = f [l,n[i]−1]n[i] n[i]−l  1 − 1 k  ;
end
end
for m = l + 1, . . . , cdo
Increment R[m] by (m − l)(f [l, n[i] − 1] − f [l, n[i]]);
end
end
end
end
for m = 1, . . . , cdo
Output R[m], the reach at frequency cap m;
end
end
A.1.7 Proof of Theorem 6
Let Zi represent the random variable for the number of times the user with visit probability qji has
viewed the ad. In this case, Zi ∼ B(n, p). The proof then follows a similar line of reasoning to that
of Theorem 5.
A.2 Algorithms
A.2.1 Streaming Algorithm for Reach Measurement
Theorem 1 allows the publisher to compute reach metrics given any time window. We give a streaming
algorithm (Algorithm 1) that outputs the expected number of reach as new impressions are getting
observed in real time. The algorithm is based on Corollary 2.
The time complexity of Algorithm 1 for each new impression is O(kc2), and the overall space com-
plexity is O(cT ). It uses dynamic programming to avoid duplicate computation of f (l; n, 1/k), ∀l ∈
{1, . . . , c}, n∈ {1, . . . , T}. For the particular case when the groups are non-overlapping, the time
complexity goes down to O(c2) as the computation can be conducted on the group level instead.
A.2.2 Streaming Algorithm for Reach Optimization
Similar to the measurement algorithm, a streaming algorithm that computespt is given in Algorithm 2.
The quantity pt shows up in the bidding formula 7, which is used to optimize campaign performance.
The time complexity for each request is O(kc), and the overall space complexity is O(cT ).
B Additional Experiment on the Impact of Targeted User Coverage
In our experiments, we operated under the assumption that all users within a group are targeted.
However, in actual advertising scenarios, advertisers target users based on various attributes such as
geolocation, age, and gender. The alignment of these targeting attributes to a set of groups may not
15

ALGORITHM 2: Streaming Algorithm for reach probability pt
Set n[i] = 0 for i = 1, . . . , N;
Set f [l, t] = 0, for l = 0, . . . , c; t = 0, . . . , T;
Set f [l, l] =
 1
k
l
for l = 0, . . . , c;
for t = 1, . . . , Tdo
Set pt = 0;
for i in Ujt do
Increment pt by 1 k Pc−1 m=0 f [m, n[i]];
end
Output pt;
if the campaign wins request t from group jt then
for i in Ujt do
Increment n[i] by 1;
for l = 0, . . . , cdo
if n[i] > lthen
if f [l, n[i]] = 0 then
Set f [l, n[i]] = f [l,n[i]−1]n[i] n[i]−l  1 − 1 k  ;
end
end
end
end
end
end
always be perfect, depending on how the user group mapping is structured. This can lead to situations
where only a subset of users within a group is targeted.
In this additional experiment, we evaluate the influence of the extent of targeted user coverage within
groups. We setup a campaign that targets only 12 users within a population of 144 users. These
144 users are divided into 12 user groups. We manipulate how the 12 targeted users are distributed
within these 12 groups. In one extreme, all of them are housed within a single group. Conversely, in
the other extreme, each of them belongs to a unique user group. We define coverage as the average
proportion of targeted users within a group, considering only groups that contain at least one targeted
user. In the extreme cases, the coverage levels are 100% and 8.33%, respectively.
A plot of ROAS (return on ad spend) versus coverage demonstrates an almost linear increase in
efficiency with coverage, underlining the significance of creating groups that align with advertisers’
targeting segments (Figure 6).
Combining the observation from other experiments, we emphasize that the erosion of ROAS under
k-anonymity is attributed to several factors. Firstly, the enforcement of frequency capping in user
groups now can only be probabilistic, leading to potential wastage of advertising budget on over-
exposed users. Secondly, the reach probability pt for a user group can be significantly reduced by
a few active users within the group, preventing the campaign from reaching the other users in the
group. Lastly, when a group contains a mix of targeted and untargeted users, there’s a risk of ads
being served to users outside the target range, resulting in further wastage of advertising spend.
16

Figure 6: Impact of the coverage of targeted users in groups. Coverage is defined as the average
percentage of the targeted users in a group. A coverage of 1.0 implies that all the users in the group
are within the target.
17
