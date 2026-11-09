---
title: Designing Ad Auctions with Targeting Information
url: https://arxiv.org/abs/2601.09541
category: consumer-behavior
subcategory: empirical
date: 2026-01
venue: ''
authors:
- Srinivas Tunuguntla
- Carl F. Mela
- Jason Pratt
source: arxiv
pdf_url: https://arxiv.org/pdf/2601.09541
pages: 85
chars: 155978
fetched_at: '2026-11-08T13:06:09+00:00'
kb_version: 1
---

# Designing Ad Auctions with Targeting Information

Designing Ad Auctions with Targeting Information
Srinivas Tunuguntla∗ Carl F. Mela † Jason Pratt ‡
August 14, 2026
Abstract
Digital advertising publishers sell ad inventory that conveys targeting information,
such as demographic, contextual, or behavioral audience segments, to advertisers. While
revealing this information improves ad relevance, it can reduce competition and lower
auction revenues. To address this trade-off, we develop the Information-Bundling Posi-
tion Auction (IBPA), a general auction mechanism for search and display advertising that
leverages targeting information while preserving competition. The mechanism treats the
realized audience segment as the publisher’s private information. For a given advertiser,
IBPA implements information bundling through mixed-bundle pricing over segments;
across advertisers, it applies the marginal-revenue framework to allocate impressions and
determine payments.
We show that IBPA is Bayesian incentive compatible and individually rational: truth-
fulbiddingformsaBayes–Nashequilibriumandadvertisersreceivenon-negativeexpected
utility from participation. Moreover, IBPA achieves at least 63% of the revenue of the
optimal feasible mechanism and weakly dominates all scalar-bid disclosure mechanisms,
including generalized second-price (GSP) auctions. The mechanism also resolves the
trade-off between targeting precision and market thickness: publisher revenue is increas-
ing in information granularity and decreasing in disclosure granularity.
Using auction-level data from a large retail media platform, we estimate advertiser
valuation distributions and simulate counterfactual outcomes. Relative to GSP, IBPA
increases publisher revenue by 91%, allocation rate by 26pp, advertiser welfare by 62%,
and total welfare by 79%.
Keywords: Display Advertising, Pricing, Auctions, Reserve Prices, Optimization, Real-
Time Bidding (RTB), Programmatic Buying, Mechanism Design
∗Assistant Professor of Marketing at the Fuqua School of Business, Duke University (email: srini-
vas.tunuguntla@duke.edu)
†The T. Austin Finch Foundation Professor Emeritus of Business Administration and Scholar in Residence
at the Fuqua School of Business, Duke University (email: mela@duke.edu, phone: 919-660-7767).
‡General Manager and Senior Research Officer, Koddi (email:jason.pratt@koddi.com)
arXiv:2601.09541v2  [econ.GN]  13 Aug 2026

1 Introduction
Digital advertising is increasingly transacted through real-time auctions, with global spend
expected to reach nearly$1trillion by 2032, with a 17% CAGR.1 Digital advertising contexts
include search advertising on retail media and search engines—typically sold using a gener-
alized second price auction or GSP (Varian 2007)—and display ads—typically sold in open
exchanges via a first price auction and walled gardens via a second price auction (Choi et al.
2020). Across these environments, impression opportunities differ in terms of the consumer
viewing the ad—such as demographics, prior purchases, and browsing histories—and the con-
text in which the ad is delivered, including the publisher’s page (e.g., surrounding content)
and the ad format (e.g., banner, tower). Advertisers’ valuations depend on such targeting
information, as both audience and context directly affect the expected value of an impression.
This paper considers how a publisher should sell impressions when it has private access to
such targeting information. We model impressions as belonging to different segments defined
by their audience and contextual attributes. For each arriving impression opportunity, the
publisher privately observes the realized segment, while advertisers do not. Our central contri-
bution is to design an auction mechanism for such settings, where the value of an impression
is segment-dependent and the impression’s segment is privately observed by the publisher.
A key challenge is that advertiser valuations are multidimensional, with each advertiser
assigning different values to different segments. Designing optimal auctions in such environ-
ments is well known to be difficult (Kolesnikov et al. 2022). In practice, publishers address
this challenge by restricting advertisers to submit a scalar bid, thereby reducing the auction
to a single dimension. The most common implementation of such a scalar-bid auction is
to disclose the realized segment and elicit a bid conditional on that information. This “full
disclosure” regime improves match quality by allowing advertisers to avoid irrelevant impres-
sions. Conventional wisdom holds that such disclosure should improve revenues by raising
advertisers’ effective bids. However, a growing body of work finds that disclosing granular
1https://www.themarketintelligence.com/market-reports/programmatic-advertising-market-4734
1

targeting information can reduce publisher revenue by thinning competition within each auc-
tion (Ada, Abou Nabout, and Feit 2022; Levin and Milgrom 2010; Lu and Yang 2015; Yao
and Mela 2011).2 Publishers therefore face a trade-off between targeting precision and market
thickness—more granular targeting information improves relevance and advertiser willingness-
to-pay, but more granular disclosure fragments demand and reduces auction competitiveness.
Rafieian and Yoganarasimhan (2021); Bergemann et al. (2022) address this trade-off by
optimizing the disclosure policy while holding the scalar-bid auction fixed. In particular, the
publisher partitions segments into groups and reveals only group membership, so that bids
reflect expected values over segments within each group. In contrast, we take a mechanism-
design perspective. Rather than restricting attention to scalar-bid auctions and optimizing
disclosure within that class, we redesign the auction itself to directly accommodate multidi-
mensional valuations.
We introduce a new auction mechanism—which we refer to as the Information-Bundling
Position Auction (IBPA)—that integrates insights from mixed bundling in pricing with the
marginal-revenue approach to mechanism design. Rather than disclosing the realized seg-
ment and soliciting a scalar-bid, the publisher keeps this information private and solicits a
multidimensional bid—one bid for each possible segment. In the single-advertiser case, the
optimal mechanism reduces to the publisher offering the advertisers a mixed bundling menu
of segments and prices, a form of second-degree price discrimination. We extend this logic to
multiple advertisers using the marginal-revenue framework (Bulow and Roberts 1989; Alaei
et al. 2013). For each advertiser, we construct a revenue curve, map the advertiser’s multidi-
mensional bid to a position on that curve, and compute the corresponding marginal revenue.
The impression is then allocated to the advertiser with the highest marginal revenue, and
payments follow a critical-quantile logic analogous to second price auctions.
We establish four theoretical properties of IBPA. First, we show that the mechanism is
Bayesian incentive compatible and individually rational: truthful bidding forms a Bayes–
2Most empirical studies find that richer targeting information increases ad prices and publisher revenue. The non-
monotonic effects emphasized here arise in settings where finer targeting substantially reduces competition by thinning
the set of bidders.
2

Nash equilibrium and advertisers receive non-negative expected utility from participation.
Second, while exact revenue maximization is generally intractable in multidimensional envi-
ronments, we show that IBPA achieves at least a(1−1/e)≈63%fraction of the revenue
of the optimal feasible mechanism. Third, IBPA weakly dominates the class of scalar-bid
disclosure mechanisms, including generalized second-price auctions, irrespective of the distri-
bution of advertiser valuations or whether advertisers are symmetric. Finally, IBPA resolves
the targeting-precision versus market-thickness trade-off identified in prior work: publisher
revenue is always increasing in the granularity of the information available to the publisher.
We empirically evaluate our mechanism using auction-level bidding data from a major on-
line retailer and its ad-tech partner. Using the estimated distribution of advertiser valuations,
segments, and click-through rate parameters, we simulate counterfactual outcomes under al-
ternative mechanisms. We find that IBPA increases publisher revenue by 91%, allocation rate
by 26pp, advertiser welfare by 62%, and total welfare by 79%, relative to GSP.
In the remainder of the paper, we first review how our research builds on the existing
literature. We then present a numerical example that illustrates the intuition behind the
proposed mechanism and its relationship to standard scalar-bid auctions. Next, we describe
the auction environment, formalize the publisher’s optimization problem, and introduce the
proposed IBPA mechanism. We then establish the theoretical properties of the proposed
mechanism. Finally, we present an empirical application using auction-level data from a
large retail media platform to estimate advertiser valuation distributions and evaluate the
counterfactual performance of IBPA relative to existing auction mechanisms. We conclude by
summarizing the contributions of the paper and discussing directions for future research.
2 Background and Related Literature
2.1 Digital Advertising
A large and growing literature examines real-time bidding in display advertising. Much of
this work focuses on advertiser-side objectives, including the response or return to advertising
(Gordon, Moakler, and Zettelmeyer 2023; Johnson 2023; Tunuguntla 2026), the design of
3

advertising content (Lee, Hosanagar, and Nair 2018), and optimal ad targeting and bidding
strategies (Rafieian and Yoganarasimhan 2021; Sayedi 2018; Tunuguntla and Hoban 2020).
A complementary stream examines the publisher side, focusing on the design of auction
mechanisms used to allocate advertising inventory. This includes comparisons of first- and
second-price auctions (Despotakis, Ravi, and Sayedi 2021), the optimization of reserve prices
(Choi and Mela 2023), and the allocation of inventory across channels such as direct sales and
exchanges (Balocco et al. 2025).
We contribute to the publisher-side literature by studying auction design when impressions
are heterogeneous, advertiser valuations are multidimensional, and impression characteristics
are privately observed by the publisher.
2.2 Information Asymmetries in Auctions
A large literature studies how sellers should design auctions when they possess private in-
formation about the objects being sold. Much of this literature studies vertical quality
information—where uncertainty concerns the overall quality of the item and bidders share
a common ranking of outcomes—focusing on optimal information disclosure and information
acquisition (Milgrom and Weber 1982; Bergemann and Pesendorfer 2007; Li, Srinivasan, and
Sun 2009; Shi 2012; Kim and Koh 2022; Chen and Yang 2023). In contrast, digital adver-
tising markets are characterized by horizontal (match) information asymmetries, where the
value of an impression depends on how well it matches the preferences of different advertisers.
Audience and contextual information determine the relevance of an impression, and different
advertisers may value the same impression differently.
Within this setting, the literature largely focuses on information disclosure while holding
the auction format fixed, typically as a generalized second-price auction. Advertisers sub-
mit scalar bids, and heterogeneity in valuations is accommodated through the information
disclosed prior to bidding.
A central insight from this literature is that disclosure can create a trade-off between tar-
geting precision and market thickness (Levin and Milgrom 2010). More granular information
4

improves match quality and increases advertisers’ willingness to pay. While most empiri-
cal studies find that greater targeting granularity increases publisher revenue, more granular
disclosure can also reduce competition by narrowing the set of relevant bidders. In settings
where this reduction in market thickness is sufficiently severe, publisher revenue may become
non-monotonic in the level of information disclosed, a pattern documented in both theoretical
and empirical work (Yao and Mela 2011; Ada, Abou Nabout, and Feit 2022; Lu and Yang
2015; Sousa 2025; Wu, Huang, and Li 2025; Rafieian and Yoganarasimhan 2021).
This paper takes a different perspective. We show that this trade-off is not inherent to the
environment, but arises from the restriction to scalar-bid auction formats. By allowing adver-
tisers to submit multidimensional bids and by keeping impression-level information private to
the publisher, the auction can simultaneously exploit fine-grained targeting information and
preserve competition across advertisers.
2.3 Mixed-Bundle Pricing
A key insight underlying our mechanism is that the multi-advertiser auction can be decom-
posed into a collection of single-advertiser problems. Each such single-advertiser problem
parallels the classic multi-product pricing problem, where a seller offers multiple goods to a
buyer with heterogeneous preferences.
The multi-product pricing literature shows that revenue-maximizing mechanisms in such
environments take the form of second-degree price discrimination implemented through mixed-
bundle pricing (Adams and Yellen 1976; Rochet 1985; McAfee, McMillan, and Whinston 1989;
Armstrong 2016). In our setting, the “goods” correspond to impression segments, and mixed
bundling becomes a menu of segment bundles and prices. Rather than screening advertisers
using a single scalar bid, the publisher screens them based on their full valuation vector across
segments. Thus, mixed bundling generalizes the role of reserve prices in standard auctions by
replacing a single screening threshold with a multidimensional pricing menu.
This perspective highlights a key limitation of standard advertising auctions. Restricting
advertisers to scalar bids limits the publisher to coarse forms of price discrimination mediated
5

through information disclosure. By eliciting multidimensional bids instead, the publisher
can screen across valuation vectors, expanding the set of feasible mechanisms beyond those
achievable through disclosure alone.
2.4 The Marginal Revenue Framework
We extend the bundling-based pricing logic from the single-advertiser setting to the multi-
advertiser environment through the marginal-revenue approach. In the classical single-item
auctionwithsingle-dimensionalprivatevalues, Myerson(1981)showsthattherevenue-maximizing
mechanism allocates the item to the bidder with the highest virtual value. Bulow and Roberts
(1989) provide an equivalent interpretation in terms of marginal revenue maximization: each
bidder is associated with a revenue curve, and the optimal allocation assigns the item to
the bidder with the highest marginal revenue, defined as the derivative of this curve evalu-
ated at the point implied by the bidder’s bid. This equivalence provides both an economic
interpretation and a tractable method for implementation. Building on this insight, Alaei
et al. (2013) show that marginal-revenue maximization is revenue-optimal for any setting
with single-dimensional agent types and quasi-linear preferences.
Beyond single-dimensional settings, Alaei et al. (2013) extend the marginal-revenue frame-
work to certain multidimensional environments in which the seller allocates a single resource
subject to an ex ante allocation constraint. Their examples include settings such as selling
an insurance contract with multiple deductible levels, where buyers have different valuations
for different contract terms. Although only one contract is allocated, bidder types are mul-
tidimensional because valuations vary with the choice of deductible. In such environments,
marginal-revenue mechanisms are generally not revenue-optimal unless the type distribution
satisfies “revenue linearity” (Alaei et al. 2013), but the framework continues to provide a
tractable approach to mechanism design and delivers strong approximation guarantees even
when exact optimality fails.
Our setting differs in a key aspect. An impression belongs to a realized segment drawn
by nature (as opposed to chosen by the seller), and that segment is privately observed by the
6

publisher (seller). Whether an advertiser receives the impression therefore depends on the re-
alized segment. Thus, although our setting also involves allocating a single resource subject to
an ex ante feasibility constraint, an advertiser’s allocation cannot be summarized by a single
unconditional allocation variable. Instead, the allocation is inherently state-contingent, vary-
ing with the realized segment observed only by the publisher. The mechanism must therefore
specify a segment-contingent allocation rule that depends on the publisher’s private informa-
tion. We thus extend the marginal-revenue framework to a distinct class of multidimensional
environments in which allocation is contingent on anexogenousstate (segment).
As in the multidimensional environments studied by Alaei et al. (2013), marginal-revenue
mechanisms in our setting are not generally revenue-optimal absent additional structure such
as revenue linearity. Nevertheless, the approach continues to yield tractable mechanisms with
strong approximation guarantees. Moreover, the mechanism we propose dominates the class
of scalar-bid, disclosure-based mechanisms.
3 Numerical Example and Intuition
Before introducing the formal model and mechanism, we begin with a numerical example that
illustrates the key economic forces and the intuition underlying our approach. Throughout
this section, we assume that bids equal valuations; Section 4 shows that this assumption can
be supported by an incentive-compatible mechanism.
We proceed in two steps. We begin with a single advertiser, a single ad slot, and two
segments to illustrate price bundling. We then extend to two advertisers to introduce the
marginal-revenue approach.
3.1 Single Advertiser: Price Bundling
Consider a publisher selling a single impression to one advertiser. The impression can belong
to one of two segments,AorB, each occurring with probability1/2. The publisher observes
the realized segment, while the advertiser knows only this prior distribution. The advertiser’s
valuation depends on the segment, with(vA, vB)independently distributed uniformly on[0,1].
We focus on a single ad slot and normalize the click-through rate to one, so that valuations
7

can be interpreted as per-click values.
Scalar-bid mechanisms.In practice, most ad auctions restrict advertisers to submit a
scalar bid. Within this class, the publisher can vary the information disclosed prior to bidding.
Under full disclosure, the publisher reveals the segment before the auction. Conditional
on segmentA, the problem reduces to a single-item auction with valuevA ∼Unif[0,1]. The
optimal mechanism is a second-price auction with reserve pricerA = 0.5yielding expected
revenue0.25. The same logic applies for segmentB, so total expected revenue is0.25.
Under null disclosure, the publisher does not reveal the segment and the advertiser bids
based on the expected valuevAB = 1 2 (vA +vB). The optimal mechanism is again a second-price
auction, but with a reserve pricerAB ≈0.41, yielding expected revenue≈0.27.
When there are more than two segments, the publisher may also adopt partial disclosure
by grouping segments into coarser categories and revealing only the group containing the
realized segment.
A pricing interpretation.Because there is a single advertiser, these scalar-bid mechanisms
can be equivalently viewed as posted-price schemes. Under full disclosure, the publisher posts
segment-specific prices(rA = 0.5, rB = 0.5). Under null disclosure, the publisher instead posts
a single pricer AB ≈0.41for the bundled impression. In each case, the advertiser purchases
if its expected utility is non-negative. Thus, scalar-bid mechanisms restrict the publisher to
either segment-specific pricing or pricing a pooled bundle of segments.
Mixed bundling via multidimensional bids.This observation suggests a natural exten-
sion. In pricing theory, both separate pricing and pure bundling are special cases of mixed
bundling, which allows the seller to offer both individual segments and bundles simultaneously.
Mixed bundling weakly dominates either extreme.
Consider the following mixed-bundle menu of options: (i) Buy segmentAonly: receive
the impression and payρA = 0.66if the realized segment isA, and receive nothing and pay
zero otherwise, (ii) Buy segmentBonly: receive the impression and payρ B = 0.66if the
realized segment isB, and receive nothing and pay zero otherwise, and (iii) Buy the bundle:
8

receive the impression regardless of segment, payρAB = 0.43. Given(v A, vB), the advertiser
selects the option that maximizes expected utility. This menu yields expected revenue of
approximately0.275, exceeding both full disclosure and null disclosure.
Two features are worth emphasizing. First, this mechanism cannot be implemented with a
scalar bid: computing allocations and payments requires conditioning on all of the advertiser’s
segment-level valuations, either directly through multidimensional bids or indirectly through
menu selection. Second, the menu generalizes reserve prices by replacing a single screening
threshold with a multidimensional pricing menu.
Figure 1:Allocation regions in advertiser valuation space under full disclosure, null
disclosure, and mixed bundling.
Key insight.Allowing multidimensional bids enables second-degree price discrimination
over valuation vectors rather than a single scalar statistic, expanding the set of feasible mech-
anisms. More generally, withTsegments, the publisher can price up to2T bundles.
Figure 1 illustrates the partitions of the valuation space(vA, vB)under the three mech-
anisms. Under full disclosure, allocation depends only on the realized segment, producing
vertical and horizontal reserve-price boundaries. Under null disclosure, allocation depends
on the advertiser’s expected valuation for the bundled impression, producing a diagonal cut-
off. Mixed bundling creates a richer partition based on the advertiser’s full valuation vector,
allowing finer price discrimination than scalar-bid mechanisms.
9

3.2 Single Advertiser Revenue Curve
Toextendtheprice-bundlinglogictomultipleadvertisers, wesummarizeeachadvertiser’smul-
tidimensional valuation distribution by a revenue curve, which maps the maximum revenue
that can be extracted from an advertiser as a function of the advertiser’s ex-ante probability
of receiving the impression. The revenue curve compresses the multidimensional pricing prob-
lem into a one-dimensional object indexed only by allocation probability, which allows us to
compare advertisers using a scalar marginal revenue.
We illustrate the revenue curve’s construction using the two-segment example from Section
3.1. There, we identified a mixed bundling menu with pricesρA = 0.66, ρB = 0.66, ρAB = 0.43
that maximizes the publisher’s revenue. More generally, consider all possible choices of
(ρA, ρB, ρAB). Each such menu induces (i) an ex-ante probability of allocation—the prob-
ability that the advertiser receives the impression, averaged over the distribution of advertiser
valuations and segment realizations—and (ii) an ex-ante expected revenue for the publisher.
Plotting expected revenue against allocation probability across all such menus, and taking the
(weakly increasing) concave hull, yields the advertiser’s revenue curve.
The revenue curve admits an equivalent and useful characterization. For eachq∈[0,1], let
R(q)denote the maximum expected revenue that the publisher can extract from the advertiser
subject to the constraint that the ex-ante probability of allocation is at mostq. The resulting
functionR(q)coincides with the concave hull described above. Because the revenue curve is
concave, the marginal revenueR′(q)is decreasing inq.
Figure 2a illustrates the revenue curve for the two-segment example. Each point on the
figure corresponds to a different menu of mixed-bundle prices(ρA, ρB, ρAB). Figure 2b com-
pares the mixed bundling revenue curve with those obtained under separate pricing (varying
ρA, ρB withρ AB =∞) and pure bundling (varyingρAB withρ A =ρ B =∞). Since both are
special cases of mixed bundling, their revenue curves lie weakly below that of mixed bundling.
The revenue curve is advertiser-specific and provides a summary of the advertiser’s multi-
dimensional valuation distribution. Advertisers with different valuation distributions therefore
10

(a)Feasible revenue–allocation probability pairs and
the induced revenue curve under mixed-bundle pricing.
Each point corresponds to a pricing menu, and the red
line traces the concave hull.
(b)Revenue curves across mechanism classes
Figure 2:Revenue curves and their construction from single-advertiser mechanisms
induce different revenue curves. These curves are constructed ex ante from the advertisers’
priors and form the key inputs to the marginal-revenue approach described next.
3.3 Multiple Advertisers: Marginal Revenue Approach
We now turn to the multi-advertiser setting. Here, the publisher must determine both how
to allocate impressions across competing advertisers and how to compute the corresponding
payments for the winning advertiser. The marginal revenue approach provides a tractable
way to address both problems.
When an auction occurs, advertisers submit their multidimensional bids (equal to valu-
ations), and the mechanism proceeds as follows. First, for each advertiser, map its realized
valuation vector to a scalar positionq—which we refer to as a quantile—on its revenue curve
and compute marginal revenueR′(q). Second, allocate the impression to the advertiser with
the highest marginal revenue. Third, compute the winning advertiser’s payment. We now
describe each step in turn.
Mapping valuations to quantiles and computing marginal revenue.Fix an adver-
tiser and its revenue curve. Eachq∈[0,1]on the revenue curve corresponds to a single-
11

advertiser mechanismM(q), which can be interpreted as a menu of mixed-bundle prices—e.g.,
(ρA, ρB, ρAB)in the two-segment case. By construction,M(q)induces an ex-ante allocation
probabilityqand expected revenueR(q). The collection of mechanisms{M(q)} q∈[0,1] that
define the revenue curve provides the basis for mapping valuation vectors to quantiles.
Consider our two-segment example with independent uniform valuations, to illustrate this
mapping from advertiser valuations to quantiles. Fix a realized segment. For eachq, the
mechanismM(q)determines whether a given realized valuation vector would result in the
impression being allocated for that segment. We then map an advertiser’s realized valua-
tion vector to the smallestqsuch thatM(q)would allocate the impression conditional on
the realized segment. This mapping is segment-specific and is where the publisher’s private
information about the realized segment enters. The resultingqdetermines the advertiser’s
marginal revenueR′(q). Note that this quantile depends only on the advertiser’s own valuation
vector and revenue curve, and is independent of other advertisers.
(a)Segment A
 (b)Segment B
Figure 3:Mapping valuation vectors to quantiles using single-advertiser mechanisms.
Advertiser 1 with realized valuation(0.7,0.2)is shown as a blue cross and advertiser 2 with
realized valuation(0.58,0.82)as an orange cross; colored lines indicate allocation boundaries
for different values ofq.
Figure 3 illustrates the mapping from realized valuation vectors to quantiles in the two-
segment example. The figure plots the allocation boundaries induced by the single-advertiser
12

mechanismsM(q)for different values ofq, for each realized segment. We also plot two hy-
pothetical advertisers: advertiser 1 with realized valuations(0.7,0.2)and advertiser 2 with
realized valuations(0.58,0.82)for segmentsAandB, respectively. The allocation boundaries
shown in the figure can also be interpreted as iso-quantile curves, with each curve correspond-
ing to valuation vectors that map to the same quantile.
Consider segmentA(Figure 3a). For each advertiser, we identify the smallestqsuch
that the corresponding mechanismM(q)would allocate the impression given the advertiser’s
realized valuation vector. For advertiser 1, this yieldsq 1 = 0.4, while for advertiser 2, it
yieldsq 2 = 0.3. The same procedure applies for segmentB(Figure 3b), yieldingq1 = 0.6and
q2 = 0.2.
Allocation.Once each advertiser’s quantile is determined, its marginal revenueR ′(q)is
obtained from the revenue curve. The impression is then allocated to the advertiser with the
highest marginal revenue, with ties broken arbitrarily.
In our example, both advertisers have the same valuation distribution and therefore have
identical revenue curves. Since marginal revenue is decreasing inq, the advertiser with the
lower quantile has the higher marginal revenue and receives the impression. For segmentA,
we haveq1 = 0.4andq 2 = 0.3, so advertiser 2 wins. The same conclusion holds for segmentB.
In particular, advertiser 2 wins segmentAeven thoughv 2A = 0.58< v1A = 0.7, because the
allocation depends on the advertisers’ full valuation vectors through their induced marginal
revenues, rather than only on valuations for the realized segment.
Payment.For the winning advertiser, we compute the highest quantileq crit at which it
would still win the impression given the other advertisers’ bids. The advertiser is then charged
according to the mechanismM(qcrit)corresponding to this critical quantile.
This payment rule is analogous to a second-price auction: just as the winner in a second-
price auction pays the smallest bid at which it would still win, here the winner pays according
to the highest quantile at which it would still win. In the case of identical revenue curves, this
corresponds to using the second-lowest quantile, directly paralleling the second-price logic.
13

In our example, for segmentA, advertiser 2 wins with quantileq2 = 0.3, and the critical
quantile isq crit =q 1 = 0.4, the quantile of the competing advertiser. Thus, advertiser 2 is
charged according to the mechanismM(0.4). For segment B, advertiser 2 again wins, with
critical quantileq crit =q 1 = 0.6, and is therefore charged according toM(0.6).
Summary.Together, these examples illustrate the main ingredients of IBPA: price bundling,
revenuecurves, quantilemapping, marginal-revenueallocation, andcritical-quantilepayments.
We now formalize these ideas in a general setting with arbitrary valuation distributions, het-
erogeneous advertisers, and multiple ad slots.
4 Problem Setup and Proposed Mechanism
4.1 Model
Consider a publisher sellingSad slots on a page, indexed bys∈[S]. 3 Throughout the
paper, we model both search and display advertising as position auctions. Search advertising
corresponds to the general multi-slot case, whereas display advertising is a special case with
a single slot. Differences in pricing conventions can be accommodated through the click-
through-rate parameters and valuation definitions. For example, CPM pricing is equivalent to
setting click-through rates equal to one and interpreting valuations as values per impression.
Each page belongs to a segmentt∈[T], defined by contextual page attributes (e.g., content
category) and/or consumer characteristics (e.g., demographics, past purchases, and browsing
history). Let
p= (p 1, p2, . . . , pT ),with
TX
t=1
pt = 1,
denote the probability distribution over segments.
There areAadvertisers, indexed bya∈[A]. Advertiserahas a per-click valuationv at ≥0
for an impression of segmentt; impressions that do not receive a click generate no value.
Differences inv at across segments can be interpreted as arising from differences in expected
post-click outcomes, such as conversion probabilities or purchase values, or other downstream
3We use the notation[K] ={1,2, . . . , K}.
14

advertiser objectives. Letv a = (va1, . . . , vaT )denote the advertiser’s type (valuation vector).
At the time of each impression, the publisher observes the realized segmentt, whereas the
advertisers only know the distributionp. Each advertiser privately observes its own valuation
vectorv a, while the publisher knows only a prior distributionFa overR T + for each advertiser
a. We allow for heterogeneous priors{F a}A a=1, and we assume that advertisers draw their
types—valuation vectors—independently of each other.
One interpretation ofFa has the standard Bayesian interpretation as uncertainty over ad-
vertiser valuations. In repeated-auction environments such as digital advertising, it can be
equivalently interpreted as the distribution of advertiser valuations across impression opportu-
nities. Such variation may arise because advertisers possess information beyond the targeting
information observed by the publisher, including first-party customer data, information de-
rived from activity on the advertiser’s website, or third-party data sources. Throughout the
paper, we adopt the standard Bayesian formulation while recognizing that repeated digital
advertising auctions provide a natural empirical interpretation of the prior.
This formulation follows the standard Bayesian mechanism design framework (Myerson
1981). The timing is as follows: the publisher first commits to a mechanism; then the publisher
observes the realized segment while each advertiser privately observes its valuation vector;
finally, the mechanism determines allocations of slots and payments. Within this framework,
ex-ante refers to the stage before the segment and advertiser valuations are realized. Interim
refers to the perspective of a single player—advertiser or publisher—after observing its private
information but before knowing the realizations of others, when expectations are taken over
the types of the remaining players. Ex-post refers to the stage after both the segment and all
advertisers’ valuations are realized. We assume all agents are risk-neutral.
Without loss of generality, we focus on direct mechanisms (Myerson 1981), in which each
advertiserasubmits a bid vectorb a = (ba1, . . . , baT ), corresponding to bids for each segment.
The mechanism then determines outcomes as a function of all submitted bids, denoted by
B= (b 1, . . . ,bA).
15

A direct mechanism is characterized by allocation functionsxast(B)and an expected pay-
mentm a(B)for each advertiser.x ast ∈[0,1]denotes the probability that advertiserareceives
slotsfor segmentt, whilem a denotes the expected payment of advertisera, where the ex-
pectation is taken over the mechanism’s randomization, segment, and click realizations.4
Feasibility requires that each advertiser is assigned at most one slot for each segment, i.e.,
X
s
xast ≤1∀a, t
and that each slot is assigned to at most one advertiser, i.e.,
X
a
xast ≤1∀s, t
4.2 Advertiser Incentive Constraints
Given a mechanism—allocation and payment functions—advertisers submit bids that maxi-
mize their expected utility. Because valuations are specified per-click, advertiser utility de-
pends on the click-through rate (CTR). It is standard practice in the literature to model the
CTR of an advertiserain slotsas a product of the advertiser’s qualityγa and the slot effect
αs (Athey and Nekipelov 2011). We further allow the CTR to vary with segmenttthrough
segment effectsβ t. Thus, the CTR of advertiserain slotsfor segmenttis given by
¯cast =α s βt γa
We assume that slots are numbered so thatα1 ≥α 2 ≥ · · · ≥αS. Throughout the paper, we
refer to slot1as the highest slot and slotSas the lowest slot. Furthermore, to normalize the
scale, we set the effect of the top slot toα1 = 1and the effect of the first segment toβ1 = 1
without loss of generality.
4Only expected payments are needed to compute the publisher’s revenue. The mechanism does not depend on how
payments are disaggregated at the slot or segment level. Thus, specific per-slot paymentsmast can be implemented in
any convenient form as long as they aggregate to the expected paymentma.
16

The expected utility of advertisera, when biddingb a with true valuation vectorv a, is
then
ua(ba,v a) =E
"X
t,s
pt αsβtγavat xast(ba,b −a)−m a(ba,b −a)
#
,
where the expectation is taken over the bids of all other advertisersb−a. Each advertiser
chooses bids to maximize this expected utility.
By the revelation principle (Myerson 1981), we can restrict our attention to mechanisms
that are incentive compatible without loss of generality. A mechanism is Bayesian incentive
compatible (BIC) if truthful bidding constitutes a Bayes-Nash equilibrium, that is,
ua(va,v a)≥u a(ba,v a)∀b a,∀v a,∀a.
We impose this constraint in our publisher optimization problem to ensure that bids equal
true valuations, i.e.,V= (v 1, . . . ,vA) =B= (b 1, . . . ,bA).
In addition, mechanisms must satisfy a participation, or Bayesian individual rationality
(BIR), constraint: each advertiser’s expected utility—in equilibrium—must be non-negative,
ua(va,v a)≥0∀v a,∀a.
4.3 Publisher Optimization Problem
Given these incentive constraints, the publisher chooses a mechanism to maximize expected
revenue, defined as the sum of expected payments across all advertisers5. The publisher’s prob-
lem can thus be summarized as choosing allocation and payment rules to maximize expected
5More generally, the publisher’s objective could involve a combination of revenue and advertiser utilities (e.g., to
reflect competitive pressures across publishers), but the structure of the analysis remains unchanged.
17

revenue subject to feasibility, incentive compatibility, and individual rationality constraints:
max
{xast(·), ma(·)}
EV
"X
a
ma(V)
#
s.t.
X
s
xast(V)≤1,∀a, t,∀V(Feasibility: one slot per advertiser)
X
a
xast(V)≤1,∀s, t,∀V(Feasibility: one advertiser per slot)
ua(va,v a)≥u a(ba,v a),∀b a,∀v a,∀a(BIC)
ua(va,v a)≥0,∀v a,∀a(BIR).
(1)
4.4 Information-Bundling Position Auction (IBPA)
To address the publisher’s problem, we develop the Information-Bundling Position Auction
(IBPA), which applies the marginal-revenue approach to this environment with multidimen-
sional advertiser valuations, multiple slots, and publisher-private segment information. The
mechanismreducesthejointadvertiser-slot-segmentproblemtoatractablecollectionofsingle-
advertiser, single-slot components.
Implementing the marginal-revenue approach in our setting raises two challenges. First,
unlike standard single-resource environments, the publisher allocates multiple slots for each
possible segment. At first glance, this suggests that the single-advertiser problem is multidi-
mensional across both slots and segments, so that no one-dimensional revenue curve exists.
We show, however, that the single-advertiser problem depends only on the highest available
slot. Since revenue curves are constructed ex ante, before the realization of segments or adver-
tiser valuations, we can integrate over segments and obtain a one-dimensional revenue curve
for each advertiser.
Second, the marginal-revenue approach requires mapping each advertiser’s valuation vec-
tor to a scalar quantile on its revenue curve. In standard single-dimensional settings, this
mapping follows from the natural ordering of scalar values. Here, advertiser types are mul-
18

tidimensional valuation vectors and therefore have no natural ordering. We resolve this by
using the publisher’s private information: for any slot and realized segment, we order adver-
tiser types according to their probability of receiving the slot under the prior distribution of
valuations, yielding a segment-specific quantile mapping.
Using these revenue curves and quantile mappings, IBPA computes advertisers’ marginal
revenues, assigns slots in decreasing order of slot effect, and determines payments consistent
with incentive compatibility. The remainder of this section formalizes the single-advertiser
mechanisms, constructs their revenue curves, and develops the resulting marginal-revenue
allocation and payment rules.
4.4.1 SingleAdvertiserMechanisms.Webeginwiththesingle-advertiserproblem, which
forms the building block of IBPA. As illustrated in Section 3.1, the mechanism reduces to a
menu of (possibly randomized) bundles of segments and associated prices. The marginal-
revenue approach extends this single-advertiser mechanism to multiple advertisers.
Fix advertisera 0 with quality effectγ a0 on the click-through rate (CTR). Let ˜S⊆[S]
denote the set of available slots, and lets0 be the slot with the highest slot effectαs0.
With a single advertiser, the publisher’s problem in Equation 1 reduces to choosing alloca-
tion functionsxa0st(va0)∀s∈ ˜S,∀tand an expected payment functionm a0(va0), to maximize
expected revenue, subject to incentive compatibility (IC), individual rationality (IR), and the
feasibility constraint that the advertiser cannot be assigned more than one slot.
By the taxation principle (Rochet 1985), any single-agent IC and IR mechanism can be
represented as a menu of options from which the advertiser self-selects. Each menu optionk
specifies probabilistic allocations across slots and segments,χ(k) st ∀s∈ ˜S,∀t, together with a
paymentα s0γa0µ(k).6
Given its realized valuation vectorva0, the advertiser chooses the menu option that max-
imizes its utility. If the advertiser chooses optionk, thenx a0st =χ (k) st ∀s, t, andma0 =
6We express the payment in this scaled form for convenience; multiplying byαs0 γa0 is without loss of generality.
19

αs0γa0µ(k). The resulting utility is
ua0(va0) =
X
t,s
pt αsβtγa0va0t χ(k) st −α s0γa0µ(k).(2)
This representation of the single-advertiser mechanism as a menu of options allows for a
further simplification: any allocation that assigns positive probability to lower slots can be
replaced by an equivalent allocation that assigns probability only to the highest available slot
s0, with probabilities appropriately rescaled. This transformation preserves the advertiser’s
expected utility for every valuation vector, and therefore leaves publisher revenue unchanged.
The following proposition formalizes this result.
Proposition 1.For any mechanismMthat includes a menu optionkwithχ (k) ˜s˜t >0for some
˜s̸=s 0, ˜t, there exists another mechanismM ′ in whichχ (k) st = 0∀s̸=s 0 ∀tsuch that the
publisher’s expected revenue underM′ is equal to that underM.
Proof.See Web Appendix A.
Hence, without loss of generality, we can restrict attention to menus in which each option
specifies allocations only for slots 0 across segmentsχ t ∀tand a corresponding payment
αs0γa0µ(k). This representation reduces the single-advertiser mechanism to a menu of (possibly
randomized) bundles of segments and associated prices, which generalizes the mixed-bundle
pricing in Section 3.1. Thus, the single-advertiser mechanism is precisely a multidimensional
pricing problem over segments
4.4.2 SingleAdvertiserRevenueCurve.Wenowformalizetherevenuecurveintroduced
in Section 3.2. For a given slot, each single-advertiser mechanism—a menu of randomized bun-
dles of segments and associated prices—induces (i) an ex-ante probability that the advertiser
receives the slot, averaged over the distribution of advertiser valuations and segment realiza-
tions, and (ii) an ex-ante expected revenue for the publisher. The revenue curve is obtained
by solving for the single-advertiser mechanism that maximizes expected revenue subject to
the constraint that the ex-ante probability of allocation is at mostq, for eachq∈[0,1].
20

Fixadvertiseraandletsdenotethehighestavailableslot. Consideramenu{χ (k), µ(k)}k∈[K],
whereχ (k) specifies a randomized bundle of segments andµ(k) the associated payment. Given
such a menu, the advertiser draws a valuation vectorva ∼F a and selects the option that max-
imizes its utility as defined in Equation 2. Letξk denote the probability that the advertiser
selects optionk.
Conditional on selecting optionk, the advertiser receives slotswith probabilityP t ptχ(k) t
and the publisher receives revenueαsγaµ(k). The ex-ante constrained single-advertiser problem
is therefore
max
K,{χ(k),µ(k)}
αsγa
KX
k=1
ξkµ(k) subject to
KX
k=1
ξk
 X
t
ptχ(k) t
!
≤q.(3)
We denote the optimal value of this problem as a function ofqbyRas(q), which defines
the advertiser’s revenue curve for slots.7 Intuitively, the revenue curve describes how the
advertiser’s contribution to publisher revenue changes as the advertiser’s allocation probability
for the slot increases. When constructed for all advertisers, these curves capture the trade-off
inherent in increasing one advertiser’s allocation probability relative to others.8
The following proposition establishes that the revenue curve is non-decreasing and con-
cave. This result is consistent with standard economic intuition: as the allocation probability
increases, the mechanism exhibits diminishing returns, so marginal revenues decline withq.
To establish the result, letMdenote the class of mechanisms over which the constrained
single-advertiser problem is optimized, and assume thatMis closed under convex combina-
tions.9
Proposition 2.When the class of mechanismsMis closed under convex combinations, the
7 For expositional convenience, we represent the mechanism as a menu of lengthK. More generally, the taxation
principle permits menu representations with infinitely many or even a continuum of menu options. Our use of finite
menus should therefore be interpreted as a notational simplification rather than a restriction on the underlying class
of incentive-compatible and individually rational mechanisms.
8Because revenue curves are constructed ex-ante, the allocation constraint averages not only over the advertiser’s
valuation distribution but also over segment realizations.
9A convex combination of mechanismsM1, . . . , Mn is defined as selecting mechanismMi with probabilityλi, where
λi ≥0for alliand Pn i=1 λi = 1.
21

revenue curveR as(q)is non-decreasing and concave inq. Consequently, the marginal revenue
R′ as(q)is non-negative and weakly decreasing inq.
Proof.See Web Appendix A.
The revenue curve also exhibits additional structure that further simplifies the marginal-
revenue approach.
Proposition 3.For any mechanism classM, the revenue curve factorizes as
Ras(q) =α sγa Φa(q),
whereΦ a(q)depends only on advertisera’s valuation distribution and not on slots.
Proof.See Web Appendix A.
The functionΦ a(q) is obtained by solving the slot-normalized version of the single adver-
tiser problem in Equation 3, given by
Φa(q) = max
K,{χ(k),µ(k)}
KX
k=1
ξk µ(k) s.t.
KX
k=1
ξk
 X
t
pt χ(k) t
!
≤q.(4)
We therefore refer toΦa(q)as the advertiser’s normalized revenue curve henceforth.
The factorization of the revenue curve into slot and advertiser components has two impor-
tant implications. First, revenue curves for a given advertiser across slots are simply scaled
versions of one another, with slot effects entering only multiplicatively. As a consequence,
when computing marginal revenues from advertiser valuations, the mapping to a quantileq
on the revenue curve depends only onΦa(q), which is independent of the slot. Hence the
quantile mapping is itself slot-independent.
Second, marginal revenues take the formR ′ as(q) =α sγaΦ′ a(q). For a given advertiser,
this expression implies that marginal revenue is higher for higher slots. Thus, to maximize
marginal revenue, it is natural to allocate in order of slots from highest to lowest. At the same
time, for a fixed slot, advertisers’ marginal revenues are ranked byγaΦ′ a(q). This parallels the
22

generalized second-price auction, where advertisers are ordered by the product of a quality
score and a bid. In our formulation,γa plays the role of the quality score, whileΦ′ a(q)can be
interpreted as a virtual value—the derivative of the scaled revenue curve—similar to Myerson’s
optimal auction for a single item (Myerson 1981; Bulow and Roberts 1989). We refer toΦ′ a(q)
as the advertiser’s normalized marginal revenue or virtual value henceforth.
4.4.3 Marginal Revenue Approach.The slot-normalized revenue curves are computed
offline for each advertiser, prior to any auction. During an auction, advertisers draw valuation
vectors from their respective priors and submit corresponding bid vectors. For now, we assume
truthful bidding, so that bids equal valuations; later, we show that the resulting mechanism is
Bayesian incentive compatible and individually rational (see Section 5.1), thereby justifying
this assumption.
Given the submitted valuation vectors and the realized segment observed by the publisher,
the mechanism proceeds in three steps, as illustrated in 3.3. First, for each advertiser, the pub-
lisher maps the valuation vector to a position on the advertiser’s revenue curve, referred to as
a quantile. Second, the publisher computes each advertiser’s marginal revenue as the deriva-
tive of the revenue curve at the corresponding quantile and allocates slots using the resulting
marginal revenues. Third, the publisher computes payments for the winning advertisers.
To build intuition, we begin with a special case in which the collection of mechanisms
{Ma(q)}q∈[0,1]—whereM a(q)denotes the mechanism for advertiserathat solves the slot-
normalizedsingle-advertiserprobleminEquation4underallocationconstraintq, achievingthe
normalized revenueΦ a(q)—exhibits three additional structural properties. First, allocations
are deterministic: for every menu optionk, the allocation vectorχ(k) ∈ {0,1}T is binary across
segments. Second, for each segmentt, letΩat(q)denote the set of valuation vectors allocated
underM a(q)when the realized segment ist. These allocation regions satisfy nestedness: if
q1 ≤q 2, thenΩ at(q1)⊆Ω at(q2)for every segmentt. Intuitively, as the allocation constraint is
relaxed, the allocation region expands to include lower valuations while continuing to allocate
higher valuations. Third, the allocation regions are probability-matched under the prior, so
23

thatF a(Ωat(q)) =qfor every segmenttand everyq∈[0,1].
These properties are restrictive: in general, the mechanisms{M a(q)}q∈[0,1] may involve
randomization and need not generate nested allocation regions. Nevertheless, this special case
captures the core mechanics of the marginal-revenue approach, allows the quantile mapping
to be described geometrically, and mirrors the numerical example in Section 3. The more
general construction is presented in Web Appendix B. We now describe the three steps of the
marginal-revenue approach in turn.
Mapping valuations to quantiles.We begin by constructing a mapping from an adver-
tiser’s valuation vector to a position on its revenue curve. When the mechanisms{Ma(q)}q∈[0,1]
satisfy the nestedness property above, the allocation regionsΩat(q)expand monotonically asq
increases. Moreover, because these regions satisfyFa(Ωat(q)) =q, each value ofqindexes the
probability mass of the corresponding allocation region. Relaxing the allocation constraint
fromqtoq+dqtherefore adds the valuation vectorsΩ at(q+dq)\Ω at(q), whose contribution
to publisher revenue is the marginal revenueΦa(q+dq)−Φ a(q) = Φ ′ a(q)dq. These newly
admitted valuation vectors can thus be interpreted as the marginal types at quantileq.
This yields a natural quantile mapping. For realized segmentt, define the advertiser’s
quantile as the smallest allocation constraint under which its valuation vector is allocated:
qat =Q at(va) = inf{q∈[0,1] :v a ∈Ω at(q)}.
withq at = 1if the advertiser is never allocated for anyq <1. Lower quantiles correspond
to valuation vectors admitted under tighter allocation constraints and therefore have higher
marginal revenues, exactly as illustrated in Figure 3.
Finally, Proposition 3 showed thatR as(q) =α sγaΦa(q). Since slot effects enter only
multiplicatively, the underlying mechanismsMa(q)are identical across slots, implying that
the quantile mapping is slot-independent.
24

SlotAllocations.Withthevaluation-to-quantilemappingsinplace, thepublishercomputes
each advertiser’s marginal revenue for the realized segment. For advertisera, letqat =Q at(va)
denote the advertiser’s quantile for segmentt. The marginal revenue of advertiserafor slots
is thenR ′ as(qat) =α sγaΦ′ a(qat).
Proposition 3 established that marginal revenues across slots differ only through the slot
multiplierα s. Consequently, maximizing total marginal revenue reduces to processing slots
in decreasing order ofαs and assigning each slot to the advertiser with the highest marginal
revenue.
Within each slots, advertisers are ranked byγaΦ′ a(qat). Slots are assigned in this order
until either all slots or all advertisers are exhausted, excluding advertisers with non-positive
marginal revenues.
This allocation rule parallels standard scalar-bid position auctions, in which advertisers
are ranked by the product of a quality score and a scalar bid. In our mechanism, however, the
scalar bid is replaced by the advertiser’s normalized marginal revenueΦ′ a(qat), which depends
on the advertiser’s full valuation vector and the realized segment. Consequently, allocations
depend on richer information about advertiser preferences across segments, rather than on a
single scalar statistic.
Payments.We now generalize the critical-quantile payment logic introduced in Section 3.3.
In the single-slot setting considered there, an advertiser faces a single critical quantile below
which it receives the slot. The single-advertiser mechanism associated with this threshold
determines its payment. With multiple slots, each slot has a corresponding critical quantile,
and an advertiser’s payment depends on the critical quantiles for its assigned slot and all lower
slots.
To formalize this idea, setαS+1 = 0and decompose each slot effect into incremental click-
through-rate layers∆ j =α j −α j+1, j∈[S]. Receiving slotsis equivalent to receiving layers
j=s, . . . , S, sinceαs = PS j=s ∆j.
Consider advertisera, with quantileq at, assigned slots. For each layerj≥s, holding the
25

other advertisers’ quantiles fixed, define the layer-jcritical quantile as
bqj at = sup{q∈[0,1] :awould continue to receive layerjif its quantile wereq}.
Becauseγ aΦ′ a(q)is weakly decreasing inq, advertiserareceives layerjfor all quantiles below
this cutoff. Moreover, the cutoff depends only on the other advertisers’ quantiles.
Leteaj denote the advertiser rankedj+ 1, when one exists. Thenbqj at is the largest quantile
satisfyingγ aΦ′ a  bqj at  ≥γ eaj Φ′ eaj  qeaj t  . If no advertiser below rankjhas a positive score, the
critical quantile is instead determined byγaΦ′ a  bqj at  >0. Thus,bq j at identifies the boundary at
which advertiseraloses layerjand falls below slotj.
The single-advertiser mechanismMa(bqj at)determines the payment for layerj. Given adver-
tisera’s valuation vector, letχj aτ andµ j a denote the allocation vector and normalized expected
payment of the selected menu option underMa(bqj at), and defineλ j a = PT τ=1 pτ χ j aτ .
By Proposition 3, layerjscales the normalized single-advertiser mechanism by∆jγa. Its
expected incremental payment is therefore∆jγaµ j a. To collect this payment only when the
advertiser receives the layer, one convenient implementation charges∆jγa µ j a λ j a conditional on
allocation. Averaging over segment realizations and the mechanism’s randomization then
yields the required expected incremental payment∆jγaµ j a.
Summing across the layers, the advertiser’s per-impression payment is
mimp ast =γ a
SX
j=s
(αj −α j+1) µ j a
λ j a .
If payments are collected per click, as is common in practice, the per-click payment is obtained
by dividing by the realized click-through rate:
mclick ast = mimp ast αsβtγa = 1 αsβt SX j=s (αj −α j+1) µ j a λ j a .
This construction is the position-auction analogue of the Myerson payment identity (My-
26

erson 1981). Allocation of each incremental click-through-rate layer is monotone in the ad-
vertiser’s quantile, and the corresponding critical-quantile payment implements the incentive-
compatible payment associated with that allocation rule. Equivalently, just as a winner in
a second-price auction pays according to the weakest bid at which it would continue to win,
an advertiser here pays for each layer according to the weakest quantile at which it would
continue to receive that layer. With a single slot, there is only one layer, and the formula
reduces to the critical-quantile payment rule in Section 3.3.
4.4.4 IBPA Summary.
Economic Logic of Pricing and Allocation.In sum, IBPA combines several linked com-
ponents. First, it converts each advertiser’s multidimensional valuation problem into a one-
dimensional revenue-ranking problem, making the publisher’s allocation problem tractable.
For advertisera, the normalized revenue curveΦ a(q)gives the maximum expected revenue
that the publisher can obtain when the advertiser’s ex-ante probability of receiving an im-
pression is at mostq. Each pointqon this curve corresponds to a single-advertiser pricing
menu that implements the associated allocation probability.
Second, the revenue curve summarizes the trade-off underlying the choice of pricing menu.
Under a tight allocation constraint, the mechanism allocates to only valuation vectors that
support relatively selective pricing menus and generate high revenue as a result. Relaxing the
allocation constraint increases the probability that the impression is allocated, but does so by
extending allocation toward weaker valuation vectors with lower incremental revenue. Thus,
Φa(q)captures the trade-off between allocating more frequently and extracting revenue from
the marginal allocation.
Third, at auction time, the publisher uses the realized impression segment to map each
advertiser’s valuation vector to a quantileqat on the advertiser’s revenue curve. In the nested
deterministic case,q at is the smallest allocation probability at which the corresponding single-
advertiser mechanism would allocate the impression to that valuation vector. A lower quantile
therefore identifies a valuation vector that is profitable to serve even under a tighter allocation
27

constraint and consequently carries a higher marginal revenue. Importantly, this is a revenue-
based index of the advertiser’s full valuation vector, rather than simply its valuation for the
realized segment.
Fourth, IBPA allocates slots according to the resulting marginal-revenue scores,γaΦ′ a(q),
assigning higher slots to advertisers with larger scores. In this way, the mechanism balances
the increased likelihood of allocating the impression against the declining revenue contribution
of expanding allocation. Payments are determined by the critical-quantile rule in the nested
deterministic case and by the corresponding interim payment rule in the general construction.
Offline and Online Implementation.IBPA naturally separates into an offline stage and
an online auction stage. In the offline stage, the publisher solves the constrained single-
advertiserproblemstoconstructtheadvertiser-specificnormalizedrevenuecurvesandsegment-
specific valuation-to-quantile mappings. These objects depend only on advertisers’ valuation
distributions and can therefore be computed before auctions occur.
Intheonlinestage, afterobservingtherealizedsegmentandreceivingadvertisers’valuation
vectors, the publisher maps each valuation vector to a quantile, computes its marginal-revenue
score, allocates slots greedily in decreasing order of these scores, and computes the associated
payments. Algorithm 1 in Web Appendix C summarizes these steps, and Table 3 provides a
summary of the notation.
This separation is important for scalability. The computationally intensive construction of
revenue curves and quantile mappings is performed offline, while the online auction requires
onlyquantileevaluation, marginal-revenuecomputation, allocation, andpaymentcalculation.
5 Theoretical Analysis
This section establishes four theoretical properties of IBPA. First, the mechanism is a feasible
Bayesian incentive compatible and individually rational mechanism. Second, although multi-
dimensional mechanism design environments generally do not admit tractable exact solutions,
IBPA inherits strong approximation guarantees from the marginal-revenue framework. Third,
IBPA weakly dominates the class of scalar-bid disclosure mechanisms, including generalized
28

second-price auctions. Finally, IBPA resolves the targeting-precision versus market-thickness
trade-off identified in prior work.
5.1 Incentive Compatibility and Feasibility of IBPA
We first establish that IBPA satisfies the feasibility, Bayesian incentive compatibility (BIC),
and Bayesian individual rationality (BIR) constraints in Equation 1. The result follows from
the fact that the interim mechanism induced by the marginal-revenue allocation rule can
be represented as a convex combination of single-advertiser mechanisms that are themselves
incentive compatible and individually rational. Here, the interim mechanism refers to the
mechanism faced by a given advertiser after integrating over the valuations of the other ad-
vertisers and the mechanism’s randomization. Consequently, truthful reporting constitutes a
Bayes–Nash equilibrium, allowing the subsequent analysis to treat submitted bid vectors as
valuation vectors. Feasibility follows directly from the slot allocation rule, which assigns each
slot to at most one advertiser and each advertiser to at most one slot.
Proposition 4.The IBPA mechanism satisfies feasibility, BIC, and BIR.
Proof.See Web Appendix D.
5.2 Revenue Approximation
Having established that IBPA is a feasible BIC and BIR mechanism, we next compare its
revenue to that of the optimal feasible BIC and BIR mechanism. Because our setting is
multidimensional—advertisers possess valuation vectors over segments, and the publisher’s
allocation rule is segment-contingent—exact characterization of the revenue-maximizing BIC
and BIR mechanism is intractable absent additional structural assumptions on the valuation
distributions (Kolesnikov et al. 2022; Alaei et al. 2013). Nevertheless, the marginal-revenue
structure of IBPA yields a strong approximation guarantee relative to the optimal mechanism.
LetRev OPT denote the maximum expected revenue attainable by any feasible BIC and BIR
mechanism for the publisher’s problem in Equation 1, and letRevIBPA denote the expected
revenue generated by IBPA.
29

Theorem 5.Suppose advertisers’ valuation vectors are drawn independently across advertis-
ers, while allowing arbitrary dependence across segments within an advertiser. Then
RevIBPA ≥

1− 1 e  RevOPT
Proof.See Web Appendix D.
Theproofproceedsintwosteps. First, weconstructanex-anterelaxationofthepublisher’s
problem in Equation 1. Rather than requiring the feasibility constraints on allocation to hold
for every realization of advertiser valuations and segments, we require them to hold only ex-
ante, i.e., in expectation. This relaxation enlarges the feasible set of mechanisms, since every
ex-post feasible BIC and BIR mechanism is also feasible for the ex-ante relaxed problem.
The optimal value of the relaxed problem therefore provides an upper bound on the revenue
attainable by any feasible mechanism. Second, we compare IBPA to this ex-ante benchmark.
Results from the marginal-revenue literature imply that the ex-post feasible marginal-revenue
mechanism achieves at least a(1−1/e)fraction of the corresponding ex-ante relaxation.
Applying this result to IBPA yields the approximation guarantee.
Theorem 5 implies that IBPA obtains at least(1−1/e)≈0.632fraction of the revenue of
the optimal feasible BIC and BIR mechanism, regardless of the valuation distributions or the
complexity of the environment. Thus, although exact multidimensional revenue maximiza-
tion is generally intractable, IBPA provides a tractable mechanism with a strong worst-case
performance guarantee.
The next subsection provides a complementary benchmark by comparing IBPA with the
class of scalar-bid disclosure mechanisms, including generalized second-price auctions.
5.3 Dominance over Scalar-Bid Disclosure Mechanisms
Standard advertising auctions address multidimensional valuations by restricting advertisers
to submit scalar bids while varying the information disclosed before bidding. A disclosure
policy partitions the segment space into groups and reveals only the group containing the
30

realized segment, so advertisers bid based on their expected value for the disclosed group.
Following Rafieian and Yoganarasimhan (2021), we formalize disclosure through partitions
of the segment space. LetP disc be a partition of the set of segments[T]intoDdisjoint
disclosure blocks, and letgdisc : [T]→[D]denote the associated block membership function.
When an impression of segmenttarrives, the publisher observestbut discloses only the block
gdisc(t)to advertisers. Because advertisers submit scalar bids, advertisera’s bid for a disclosed
blockd∈[D]reflects its expected valuation over the segments contained in that block.
We refer to any mechanism that operates in this way as a scalar-bid disclosure mechanism.
Formally, for a disclosure partitionPdisc, letM SB(Pdisc)denote any feasible scalar-bid (SB)
mechanism in which, after disclosure blockdis revealed, advertisers submit a scalar bid for
that block, and allocations and payments depend only on the disclosed block and the sub-
mitted scalar bids, not on distinctions among segments within the block. This class includes
generalized second-price auctions, first-price auctions, and other disclosure-based auction for-
mats that restrict advertisers to scalar bids conditional on the disclosed information. Let
RevMSB(Pdisc)denote the expected publisher revenue generated by such a mechanism.
The following theorem shows that IBPA weakly dominates the class of scalar-bid disclosure
mechanisms, for any disclosure partition.
Theorem 6.For any disclosure partitionP disc and any scalar-bid disclosure mechanism
MSB(Pdisc),
RevIBPA ≥Rev MSB(Pdisc).
Proof.See Web Appendix D.
The proof proceeds in two steps. First, for any disclosure partition, a scalar-bid disclosure
mechanism reduces the environment to a single-parameter position auction, where each adver-
tiser is characterized by its expected value for the disclosed block. By the marginal-revenue
characterization of optimal auctions in single-parameter environments, the optimal scalar-bid
mechanism is therefore a marginal-revenue mechanism (Bulow and Roberts 1989). Second,
31

every single-advertiser mechanism feasible under a scalar-bid disclosure policy can also be im-
plemented within IBPA by restricting allocations and payments to depend only on disclosure
blocks. IBPA therefore optimizes over a strictly larger set of mechanisms and therefore weakly
dominates every scalar-bid disclosure mechanism.
AnimmediateimplicationofTheorem6isthatIBPAweaklydominatesgeneralizedsecond-
price (GSP) auctions under any disclosure regime, since GSP is a scalar-bid disclosure mecha-
nism. More broadly, the dominance result highlights the fundamental limitation of scalar-bid
mechanisms. By requiring advertisers to compress segment-level valuations into a single bid
before allocation and pricing occur, scalar-bid mechanisms discard information about hetero-
geneity in advertiser preferences across segments. In contrast, IBPA elicits the advertiser’s
full valuation vector and applies the marginal-revenue framework directly to this richer infor-
mation while preserving incentive compatibility. As a result, IBPA can implement a strictly
larger set of allocation and pricing rules, allowing the publisher to better exploit differences
in advertiser valuations and thereby generate weakly higher revenue.
5.4 Monotonicity in Information and Disclosure Granularity
The previous subsections compared IBPA against two revenue benchmarks: the optimal feasi-
ble BIC and BIR mechanism, and the class of scalar-bid disclosure mechanisms. We now turn
to a complementary question: how does publisher revenue under IBPA vary with the gran-
ularity of the information available to the publisher and the granularity of the information
disclosed to advertisers?
The question has two dimensions. The first is information granularity: how finely should
the publisher distinguish segments internally? The second is disclosure granularity: how
much of this information should be revealed to advertisers before bidding? Under IBPA,
these decisions are distinct because advertisers submit multidimensional bids.
We formalize the publisher’s internal information using a partitionPinfo of the segment
space[T]intoIblocks, with block-membership functiong info : [T]→[I]. Under information
partitionP info, thepublisherobservesonlytheinformationblockg info(t)containingtherealized
32

segmentt, and therefore cannot condition allocations or payments on distinctions finer than
the blocks inP info. Disclosure is represented by a partitionP disc, with block-membership
functiong disc.
We compare the granularity of two partitions using set refinement (Rafieian and Yoga-
narasimhan 2021). LetP 1 andP 2 be two partitions of[T]. We say thatP 1 is at least as
granular asP 2—denotedP 1 ⪰ P2—if for every blockB∈ P1, there exists a blockC∈ P2
such thatB⊆C. That is,P 1 is more granular thanP2 whenever it splits the segment space
more finely.
A pair(P info,P disc)is feasible ifP info ⪰ Pdisc, so every disclosure block is a union of
information blocks. Advertisers then submit bids for the information blocks contained within
the disclosed block. The following theorem shows that the publisher revenue under IBPA is
monotonically increasing in the information granularity and monotonically decreasing in the
disclosure granularity.
Theorem 7.For anyP (1) info ⪰ P(2) info and for allP disc such that both pairs(P (1) info,P disc)and
(P (2) info,P disc)are feasible,
RevIBPA(P (1) info,P disc)≥Rev IBPA(P (2) info,P disc).
Similarly, for anyP(1) disc ⪰ P(2) disc and for allPinfo such that both pairs(Pinfo,P (1) disc)and(P info,P (2) disc)
are feasible,
RevIBPA(Pinfo,P (1) disc)≤Rev IBPA(Pinfo,P (2) disc).
Proof.See Web Appendix D.
Taken together, the two monotonicity results imply that publisher revenue is maximized
under the full-information/null-disclosure regime. That is, the publisher benefits from observ-
ing the most refined segment information available while revealing no information about the
realized segment prior to bidding. The mechanism described in Section 4 corresponds exactly
to this regime.
33

The key insight is that finer information and coarser disclosure enlarge the set of feasible
single-advertiser mechanisms. A mechanism feasible under a coarser information partition can
always be replicated under a finer one, while a mechanism feasible under finer disclosure can
always be replicated under coarser disclosure. The monotonicity results follow immediately
from these nested feasible sets.
Theorem 7 stands in contrast to prior work (Levin and Milgrom 2010; Yao and Mela 2011;
Ada, Abou Nabout, and Feit 2022; Rafieian and Yoganarasimhan 2021) showing that publisher
revenue under scalar-bid mechanisms such as GSP need not be monotone in the granularity
of targeting information. Under such mechanisms, advertisers must compress their segment-
level valuations into a single bid, causing information granularity and disclosure granularity
to become coupled. As a result, increasing the amount of information available to advertisers
improves targeting precision but may simultaneously reduce competition, generating the non-
monotonic trade-offs documented in the literature.
Under IBPA, information granularity and disclosure granularity can be varied indepen-
dently because advertisers submit multidimensional bids. Finer information expands the set
of feasible mechanisms, while greater disclosure restricts it. Revenue therefore moves mono-
tonically in the direction predicted by second-degree price discrimination: it increases with
information granularity and decreases with disclosure granularity.
5.5 Computational Complexity and Approximation
IBPA is defined through a collection of constrained single-advertiser problems that determine
advertisers’ normalized revenue curves. Solving these problems exactly may require optimiza-
tion over a rich class of multidimensional pricing mechanisms and can become computationally
challenging as the number of segments increases.
To address this issue, in Web Appendix E, we develop two computationally tractable ap-
proximation classes. The first restricts attention to deterministic segment bundles, yielding
a finite menu representation closely related to mixed-bundling mechanisms. The second im-
poses an additive pricing structure across segments that can be optimized in time polynomial
34

in the number of segments. Building on approximation results from the multidimensional
pricing literature, we show that these approximation classes retain strong worst-case revenue
guarantees relative to the unrestricted single-advertiser problem.
6 Empirical Application
The theoretical results establish that IBPA outperforms scalar-bid disclosure mechanisms,
including GSP. This section quantifies the magnitude of those gains in a realistic empirical
setting. Using auction-level data from a large retail media platform, we estimate the primitives
required to implement the mechanism, including the prior distribution of advertiser valuations,
the distribution of segments, and slot effects on click-through rates. With these primitives in
hand, we compute publisher revenue under IBPA and compare it against optimal scalar-bid
mechanisms under alternative disclosure regimes, as well as GSP benchmarks.
6.1 Data
Our analysis draws on auction-level data from a large retail media platform collected during
the period May 17, 2025 to July 14, 2025. The dataset contains all position auctions conducted
on the platform during this interval for one product category. For each auction, we observe
the realized segment, the number of ad slots available, and participating advertisers’ bids and
quality scores (γa).
The platform classifies impressions into segments that combine audience and device infor-
mation. Segments combine consumer behavior (three categories), demographics (eight cate-
gories), and device type (three categories), yielding3×8×3 = 72distinct segments. 10
The platform employs the generalized second-price (GSP) auction format under the full
disclosure. Advertisers therefore observe the realized segment before bidding and submit a
bid specific to that segment. Auction outcomes follow the standard GSP rule: advertisers are
ranked by the product of their bid and quality score, slots are assigned in that order, and each
advertiser pays the minimum bid needed to retain its assigned slot.
10Although additional audience attributes are available, we focus on these dimensions because the platform considers
them the most relevant for advertiser targeting.
35

Statistic Value
Auctions 9.6M
Advertisers 1,207
Segments 72
Slot distribution 1 slot (14%), 3 slots (11%),
8 slots (42%), 20 slots (24%),
other (9%)
Submitted bids 44.4M
Average bid $5.31
Average quality score 0.0096
Table 1:Data summary statistics
To estimate click-through rate (CTR) parameters, we use a separate dataset covering
the same time period as the auction data. This dataset contains daily-level observations for
each advertiser, reporting the number of impressions and clicks received at each slot position.
These daily aggregates identify the slot multipliersαs using variation in advertisers’ realized
positions over time, following Athey and Nekipelov (2011).
The auctions are sealed bid. Advertisers combine the targeting information disclosed by
thepublisherwithprivateinformation—suchasfirst-partycustomerdata, conversionhistories,
website activity, or third-party data—when determining bids. Consequently, valuations may
vary across impression opportunities even within the same segment, motivating the private-
information framework used in the paper.
Data Summary.Table 1 summarizes the data. The sample contains 9.6 million auctions,
72 segments, and 1,207 advertisers. Most auctions (≈66%) contain either 8 or 20 slots.
Figure 4 shows substantial variation in segment frequency; the most common segment
accounts for approximately 12% of auctions. These empirical frequencies define the segment
probabilitiesp t. Advertiser bids and quality scores also exhibit substantial heterogeneity. The
average bid is$5.31per-click, and the average quality score (γ) is 0.0096. Figure 5 illustrates
this heterogeneity by plotting average bids and quality scores by advertiser and by segment.
The CTR dataset contains 11.4M impressions and 198,609 clicks during the sample period,
yielding an average click-through rate of 0.0174. Figure 6 plots the empirical CTR by slot
36

Figure 4:Distribution of segments
position. Observed CTR need not decline monotonically with slot position because it reflects
both slot effects and the quality of advertisers assigned to each slot; we estimate the underlying
slot effects separately.
6.2 Estimating Primitives
To evaluate the performance of the marginal-revenue mechanism and the benchmark mech-
anisms, we require several primitives: (i) the distribution of advertiser valuations{Fa}a∈[A],
(ii) the distribution of advertiser quality scores{γa}, (iii) slot effects on click-through rates
{αs}, and (iv) the distribution of segments{pt}. The distribution of segments follows directly
from the empirical frequencies computed in Section 6.1. Similarly, the empirical distribution
of advertiser quality scores is used directly. The remaining primitives—slot effects and valua-
tion distributions—are identified from the data using the framework of Athey and Nekipelov
(2011) and the equilibrium structure of generalized second-price auctions. We describe their
estimation in Web Appendix F.
6.3 Comparison of Mechanisms
Using the primitives estimated in Section 6.2, we compute publisher revenue under IBPA and
compare it against two classes of benchmarks. First, we consider optimal scalar-bid mech-
37

(a)Advertiser-level
 (b)Segment-level
Figure 5:Distribution of average bid vs. quality score
anisms under alternative disclosure regimes, which correspond to the theoretical benchmark
in Theorem 6. Second, we compare IBPA to generalized second-price (GSP) auctions un-
der the same disclosure regimes, as GSP remains the dominant auction format in search and
retail media advertising. We first describe the mechanisms considered and then outline our
counterfactual simulation procedure.
6.3.1 IBPA.Our primary mechanism is IBPA under the full-information/null-disclosure
regime

P full info,P null disc  , which Theorem 7 identifies as the revenue-maximizing information and
disclosure regime.11 The constrained single-advertiser problems (Equation 4) are solved nu-
merically using a genetic algorithm.12
For each advertiser, we solve the constrained problem on a grid of allocation probabilities
q∈[0,1]. The normalized revenue curveΦ a(q)is then approximated by a piecewise-linear
interpolation across this grid. This yields a conservative approximation, as the true revenue
curve is concave and therefore weakly above the piecewise-linear fit. Quantile mappings and
auction outcomes—allocations and payments—are computed as described in Section 4.4.3.
11We implement the additive-pricing approximationIBPAadd described in Web Appendix E. SinceIBPAadd restricts
the class of feasible single-advertiser mechanisms, the resulting revenue estimates provide a conservative lower bound
on the performance of the unrestricted IBPA mechanism.
12We use a genetic algorithm to account for the possibility of multiple local optima. Results are robust to algorithmic
tuning parameters; we use: population size 100, 50 parents per generation (tournament selection), 5 elites, crossover
probability 0.8 (blending), and mutation probability 0.2 (random mutation).
38

Figure 6:Variation of click-through rate by slot
6.3.2 Optimal Scalar-Bid Mechanisms.Theorem 6 establishes that IBPA weakly domi-
nates the class of scalar-bid disclosure mechanisms. To quantify the magnitude of this advan-
tage, we first construct optimal scalar-bid benchmarks under alternative disclosure regimes.
As discussed in Section 5.3, for a given disclosure partitionP, the corresponding revenue-
maximizing scalar-bid mechanism is the marginal-revenue mechanism in the induced single-
parameter environment. These mechanisms are Bayesian incentive compatible, so advertisers
bid truthfully and allocations and payments follow the corresponding marginal-revenue rules.
Ideally, one might evaluate all possible partitions of the 72 segments, but this is com-
putationally infeasible. Instead, we exploit the five underlying segment attributes: consumer
behavior (1 attribute), demographics (3 attributes), and device type (1 attribute). By toggling
each attribute on or off, we generate25 = 32meaningful disclosure regimes.
In our empirical setting, the null-disclosure partitionP=Pnull disc yields the highest revenue.
We therefore report results for both the null-disclosure and full-disclosure regimes, denoted
OPT-SB-ND and OPT-SB-FD, respectively.
39

6.3.3 GSPBenchmarks.WeadditionallycompareIBPAtogeneralizedsecond-price(GSP)
auctions, which remain the dominant auction format in search and retail media advertising.
We report GSP under the same full-disclosure and null-disclosure regimes considered above,
denoted GSP-FD and GSP-ND, respectively.
Unlike IBPA and the optimal scalar-bid mechanisms, GSP is not incentive compatible.
Consequently, advertiser behavior depends on the equilibrium concept employed. In principle,
the appropriate comparison would use a Bayes-Nash equilibrium under private information.
However, Bayes-Nash equilibria for GSP position auctions with advertiser quality scores are
generally not tractable and may fail to exist (Gomes and Sweeney 2009).13 We therefore follow
Edelman, Ostrovsky, and Schwarz (2007); Varian (2007) and compute an envy-free equilib-
rium. Because such equilibria are not unique, we report the envy-free upper bound—the
equilibrium yielding the highest publisher revenue—thereby providing a conservative bench-
mark for comparison with IBPA.
For each GSP benchmark, reserve prices are optimized to maximize publisher revenue..
Specifically, we evaluate publisher revenue over a grid of reserve prices, where the grid gran-
ularity matches the minimum bid increment observed in the data, and select the revenue-
maximizing reserve. Following the standard treatment in the sponsored-search literature
(e.g., Athey and Nekipelov 2011), the reserve price is implemented as an additional bid-
der with quality score equal to one. All reported GSP results therefore correspond to the
revenue-maximizing reserve price within the considered grid.
6.3.4 CounterfactualPerformanceComparison.Tocomparemechanismsinacommon
environment, we simulate 10 million auctions using the primitives from Section 6.2. For each
simulated auction, we (1) set the number of slots to8and use the estimated slot effects{αs},
(2) draw the number of advertisers and their quality scoresγa from the empirical distributions,
(3) draw a valuation vectorva for each advertiser from the estimated distributions{Fat}, and
(4) draw the realized segmenttfrom the empirical distribution{pt}.
13Bayes-Nash equilibria have been characterized for certain GSP environments without quality scores. To our
knowledge, no analogous characterization exists for the quality-score environment considered here.
40

Figure 7 reports publisher revenue across all mechanisms. Consistent with Theorem 6,
IBPA outperforms the optimal scalar-bid benchmarks under both disclosure regimes. More-
over, the optimal scalar-bid mechanisms outperform the corresponding GSP benchmarks. The
ordering of revenues matches our theoretical predictions:
IBPA>OPT−SB−FD>GSP−FD
andIBPA>OPT−SB−ND>GSP−ND.
Figure 7:Revenue comparison
Relative to GSP-FD, IBPA increases publisher revenue by 91%. This improvement can
be decomposed into two components. First, the corresponding optimal scalar-bid mecha-
nism (OPT-SB-FD) increases revenue by 34% relative to GSP-FD, reflecting the value of
revenue-optimal allocation and pricing within the class of scalar-bid mechanisms. Second,
IBPA increases revenue by an additional 42% relative to OPT-SB-FD, reflecting the value of
multidimensional bidding and the richer price-discrimination opportunities enabled by IBPA.
A similar pattern emerges under null disclosure. Relative to GSP-ND, IBPA increases
revenue by 69%. Of this gain, 44% is attributable to moving from GSP-ND to OPT-SB-ND,
41

Metric GSP-FD GSP-ND OPT-SB-FD OPT-SB-ND IBPA
Revenue +0% +14% +34% +63% +91%
Advertiser Welfare +0% -28% +49% +69% +62%
Total Welfare +0% -4% +41% +66% +79%
Allocation Rate +0pp +19pp +2pp +25pp +26pp
Table 2:Performance of mechanisms relative to GSP-FD
while the remaining 17% arises from moving from OPT-SB-ND to IBPA.
While our theoretical guarantees concern revenue, we also measure advertiser welfare (ex-
pected sum of utilities) and total welfare (publisher revenue plus advertiser welfare). Table
2 reports percentage changes in revenue, advertiser welfare, and total welfare, along with
percentage-point changes in allocation rate, relative to the GSP–FD benchmark across alter-
native mechanisms. While welfare improvements are not theoretically guaranteed for arbitrary
primitives, in our empirical setting, both metrics improve under the proposed mechanism
relative to the benchmark—advertiser welfare by 62% and total welfare by 79%. The im-
provements appear to be driven by allocation rate—in our simulations, the probability of an
impression being sold under the proposed mechanism is 47% compared to 21% under the
benchmark. Higher allocation rate indicates that impressions are more frequently matched to
advertisers who value them, improving outcomes for all participants.
The results alsoprovide some insight into the sources of therevenue gains. While allocation
and pricing decisions are jointly determined by the mechanism and therefore do not admit
a clean additive decomposition, the comparison across mechanisms is informative. Moving
from GSP-FD to the optimal scalar-bid mechanism increases revenue by 34% while increasing
allocation rate by only 2 percentage points. In contrast, moving from the optimal scalar-
bid mechanism to IBPA increases revenue by an additional 42% and allocation rate by an
additional 24 percentage points. These patterns suggest that a substantial portion of the
gains from IBPA arises from improved matching between advertisers and impressions, which
increases the probability that impressions are allocated. At the same time, the additional
revenue gain relative to the optimal scalar-bid benchmark indicates that multidimensional
42

bidding and the richer screening opportunities available under IBPA also contribute materially
to performance.
6.3.5 Revenue and Information Granularity.The previous subsection compared mech-
anisms under full publisher information, using each mechanism’s revenue-maximizing disclo-
sureregime. Wenowexaminehowpublisherrevenuechangesaspublisherinformationbecomes
more granular.14 For IBPA, we maintain the revenue-maximizing null-disclosure regime while
varying the information available to the publisher. For scalar-bid mechanisms, information
granularity and disclosure granularity are equivalent, since advertisers can condition their
bids only on disclosed information. We therefore report the scalar-bid mechanisms under full
disclosure throughout this analysis.15
Starting from no publisher information, we sequentially reveal the five segment attributes
(consumer behavior, three demographic attributes, and device type) in a random order. Figure
8 reports publisher revenue as additional attributes become available.
Consistent with Theorem 7, publisher revenue under IBPA increases monotonically with
information granularity. In contrast, neither the optimal scalar-bid mechanism nor GSP ex-
hibits monotonicity. Additional information can reduce revenue because finer segmentation
thins competition while scalar bidding prevents the mechanism from fully exploiting the richer
information.
At null publisher information, IBPA and the optimal scalar-bid mechanism coincide be-
cause both reduce to the same single-parameter environment. As publisher information be-
comes more granular, the revenue gap between the two mechanisms widens in our empirical
setting, illustrating the increasing value of multidimensional bidding. Consistent with the
earlier revenue comparisons, GSP underperforms the corresponding optimal scalar-bid mech-
anism across all information regimes.
14This exercise is relevant for understanding the potential revenue implications of privacy policies that restrict the
information publishers may use for advertising. Such policies can be viewed as coarsening the information available to
the publisher.
15For scalar-bid mechanisms, information and disclosure granularity cannot be varied independently. A fully in-
formed publisher disclosing a coarse partition is equivalent to a less-informed publisher observing only that partition and
fully disclosing it. Thus, when varying publisher information, it is without loss of generality to impose full disclosure.
43

Figure 8:Revenue and information granularity
7 Discussion & Conclusion
This paper develops the Information-Bundling Position Auction (IBPA), a mechanism for
selling digital advertising inventory when advertiser valuations depend on audience and con-
textual information privately observed by the publisher. Unlike standard scalar-bid auctions,
IBPA separates targeting precision from market thickness by allowing advertisers to submit
multidimensional bids while treating the realized impression segment as the publisher’s private
information.
For each advertiser, IBPA constructs a menu of bundle prices that implements second-
degree price discrimination over the advertiser’s valuation vector. Across advertisers, impres-
sions are allocated using the marginal-revenue framework.
The resulting mechanism is feasible, Bayesian incentive compatible, and individually ratio-
nal. Although exact revenue maximization is generally intractable, IBPA achieves a(1−1/e)-
approximation to the optimal feasible mechanism. It also weakly dominates scalar-bid disclo-
sure mechanisms, including GSP, and resolves the targeting-precision versus market-thickness
trade-off. Consequently, publisher revenue is increasing in the granularity of the information
44

available to the publisher.
Using data from a retail media platform, we estimate advertiser valuations and evaluate
the performance of IBPA in counterfactual simulations. Relative to GSP, IBPA increases
publisher revenue by approximately 91%, advertiser welfare by 62%, and total welfare by
79%. The welfare gains arise primarily from improved allocation rates, as impressions are
more frequently matched to advertisers who value them.
Several extensions and considerations merit discussion. First, our analysis abstracts from
advertiser budget constraints, multi-homing, and competition among publishers. Although
IBPA satisfies individual rationality, a budget-constrained advertiser may reallocate spending
across platforms if its marginal return changes. Publishers can accommodate such concerns
by imposing minimum advertiser-utility constraints or incorporating advertiser welfare into
their objectives. Because IBPA is constructed from single-advertiser revenue problems, these
modifications can be incorporated directly into the mechanism.
Relatedly, the counterfactual revenue gains estimated for a single publisher need not scale
proportionally under industry-wide adoption. Aggregate advertiser budgets may be fixed or
slow-moving, and higher allocation rates may increase ad load, potentially affecting consumer
engagement. Publishers therefore choose auction design jointly with ad supply, pacing, and
other policies that balance short-run revenue against advertiser retention and consumer expe-
rience. A full equilibrium analysis of publisher competition, advertiser budget allocation, and
consumer engagement is an important direction for future work.
Second, practical implementation requires addressing both bid complexity and computa-
tional scalability. Although IBPA requires multidimensional bids, these bids can be repre-
sented compactly. Advertising platforms already allow advertisers to combine base bids with
modifiers for device, demographics, behavior, and other targeting attributes. These inputs
naturally generate segment-contingent valuation vectors without requiring advertisers to sub-
mit an independent bid for every segment. Modern machine-learning bidding systems can
also generate segment-contingent valuation vectors in a single model evaluation, mitigating
45

the computational burden on advertisers.
Most of the publisher’s computational burden occurs offline, when constructing revenue
curves and quantile mappings. The online mechanism then uses these mappings to compute
marginal revenues, allocations, and payments.16 Scalability nevertheless remains important
because the number of segments can grow rapidly with the number of targeting attributes.
Practical implementations may therefore require structured bid representations, dimension
reduction, or restricted pricing menus, such as the additive-pricing approximation used in our
empirical analysis.
Finally, practical adoption requires commitment and transparency. Incentive compatibil-
ity ensures that truthful reporting is optimal conditional on the announced mechanism, but
advertisers must also trust the publisher to follow its allocation and payment rules (Akbar-
pour and Li 2020). This concern is not unique to IBPA: GSP similarly requires confidence in
platform-determined quality scores, rankings, and pricing rules. An important direction for
future work therefore concerns the role of commitment, transparency, and verifiability in ad
auction design.
Overall, this paper shows that the tension between targeting precision and competition is
notinherenttodigitaladvertisingmarkets. Bycombininginformationbundlingwithmarginal-
revenue allocation, IBPA provides a tractable alternative to scalar-bid disclosure mechanisms,
provides strong performance guarantees, and opens several directions for research on imple-
mentation, platform competition, commitment, and dynamic advertiser participation.
16In our implementation, an online auction required approximately 400 milliseconds on a standard laptop. Con-
structing a revenue curve required several minutes with a 10-point quantile grid and approximately one hour with a
100-point grid.
46

References
Ada, Sila, Nadia Abou Nabout, and Elea McDonnell Feit (2022), “Context Information Can Increase
Revenue in Online Display Advertising Auctions: Evidence from a Policy Change,”Journal of
Marketing Research, 59 (5), 1040–1058.
Adams, William James and Janet L. Yellen (1976), “Commodity Bundling and the Burden of
Monopoly,”The Quarterly Journal of Economics, 90 (3), 475–498.
Akbarpour, Mohammad and Shengwu Li (2020), “Credible Auctions: A Trilemma,”Econometrica,
88 (2), 425–467.
Alaei, Saeed, Hu Fu, Nima Haghpanah, and Jason Hartline “The Simple Economics of Approximately
Optimal Auctions,” “2013 IEEE 54th Annual Symposium on Foundations of Computer Science,”
pages 628–637 (2013).
Armstrong, Mark (2016), “Nonlinear Pricing,”Annual Review of Economics, 8 (Volume 8, 2016),
583–614.
Athey, Susan and Denis Nekipelov (2011), “A Structural Model of Sponsored Search Advertising
Auctions,”Working Paper, University of California, Berkeley.
Babaioff, Moshe, Nicole Immorlica, Brendan Lucier, and S Matthew Weinberg (2020), “A Simple
and Approximately Optimal Mechanism for an Additive Buyer,”Journal of the ACM (JACM),
67 (4), 1–40.
Balocco, Francesco, Yixin Lu, Ting Li, and Alok Gupta (2025), “Lemon Ads: Adverse Selection in
Multichannel Display Advertising Markets,”Management Science.
Bergemann, Dirk, Tibor Heumann, Stephen Morris, Constantine Sorokin, and Eyal Winter (2022),
“Optimal information disclosure in classic auctions,”American Economic Review: Insights, 4 (3),
371–388.
Bergemann, Dirk and Martin Pesendorfer (2007), “Information Structures in Optimal Auctions,”
Journal of Economic Theory, 137 (1), 580–609.
Bulow, Jeremy and John Roberts (1989), “The Simple Economics of Optimal Auctions,”Journal of
political economy, 97 (5), 1060–1090.
Chawla, Shuchi, Yifeng Teng, and Christos Tzamos (2019), “Buy-many Mechanisms are Not Much
Better than Item Pricing,”Proceedings of the 2019 ACM Conference on Economics and Com-
putation.
Chen, Yi-Chun and Xiangqian Yang (2023), “Information Design in Optimal Auctions,”Journal of
Economic Theory, 212, 105710.
Choi, Hana and Carl F. Mela (2023), “Optimizing Reserve Prices in Display Advertising Auctions,”
SSRN Electronic Journal.
Choi, Hana, Carl F. Mela, Santiago R. Balseiro, and Adam Leary (2020), “Online Display Advertising
Markets: A Literature Review and Future Directions,”Information Systems Research, 31 (2),
556–575.
Despotakis, Stylianos, R. Ravi, and Amin Sayedi (2021), “First-Price Auctions in Online Display
Advertising,”Journal of Marketing Research, 58 (5), 888–907.
Edelman, Benjamin, Michael Ostrovsky, and Michael Schwarz (2007), “Internet Advertising and the
Generalized Second-Price Auction: Selling Billions of Dollars,”American Economic Review,
97 (1), 242–259.
Gomes, Renato D and Kane S Sweeney (2009), “Bayes-Nash Equilibria of the Generalized Second
Price Auction,”Proceedings of the 10th ACM conference on Electronic Commerce.
47

Gordon, Brett R., Robert Moakler, and Florian Zettelmeyer (2023), “Close Enough? A Large-Scale
Exploration of Non-Experimental Approaches to Advertising Measurement,”Marketing Science,
42 (4), 768–793.
Hart, Sergiu and Noam Nisan (2013), “The Menu-size Complexity of Auctions,”Proceedings of the
Fourteenth ACM Conference on Electronic Commerce.
Johnson, Garrett A. (2023), “Inferno: A Guide to Field Experiments in Online Display Advertising,”
Journal of Economics and Management Strategy, 32 (3), 469–490.
Kim, KyungminandYoungwooKoh(2022), “AuctionswithFlexibleInformationAcquisition,”Games
and Economic Behavior, 133, 256–281.
Kolesnikov, Alexander V, Fedor Sandomirskiy, Aleh Tsyvinski, and Alexander P Zimin (2022), “Beck-
mann’s Approach to Multi-Item Multi-Bidder Auctions,”arXiv preprint arXiv:2203.06837.
Lee, Dokyun, Kartik Hosanagar, and Harikesh S. Nair (2018), “Advertising Content and Consumer
Engagement on Social Media: Evidence from Facebook,”Management Science, 64 (11), 5105–
5131.
Lee, Jasper CH and Paul Valiant (2016), “Optimizing Star-Convex Functions,”2016 IEEE 57th
Annual Symposium on Foundations of Computer Science (FOCS).
Levin, Jonathan and Paul Milgrom (2010), “Online Advertising: Heterogeneity and Conflation in
Market Design,”American Economic Review, 100 (2), 603–607.
Li, Shibo, Kannan Srinivasan, and Baohong Sun (2009), “Internet Auction Features as Quality
Signals,”Journal of Marketing, 73 (1), 75–92.
Lu, Shijie and Sha Yang (2015), “A Two-Sided Market Analysis of Behaviorally Targeted Display
Advertising,”SSRN Electronic Journal.
Manelli, Alejandro M and Daniel R Vincent (2007), “Multidimensional Mechanism Design: Revenue
Maximization and the Multiple-good Monopoly,”Journal of Economic Theory, 137 (1), 153–185.
McAfee, R. Preston, John McMillan, and Michael D. Whinston (1989), “Multiproduct Monopoly,
Commodity Bundling, and Correlation of Values,”The Quarterly Journal of Economics, 104 (2),
371–383.
Milgrom, Paul R. and Robert J. Weber (1982), “A Theory of Auctions and Competitive Bidding,”
Econometrica, 50 (5), 1089–1122.
Myerson, Roger B (1981), “Optimal Auction Design,”Mathematics of Operations Research, 6 (1),
58–73.
Rafieian, Omid and Hema Yoganarasimhan (2021), “Targeting and Privacy in Mobile Advertising,”
Marketing Science, 40 (2), 193–218.
Rochet, Jean-Charles (1985), “The Taxation Principle and Multi-time Hamilton-Jacobi Equations,”
Journal of Mathematical Economics, 14 (2), 113–128.
Sayedi, Amin (2018), “Real-Time Bidding in Online Display Advertising,”Marketing Science, 37 (4),
553–568.
Shi, Xianwen (2012), “Optimal Auctions with Information Acquisition,”Games and Economic
Behavior, 74 (2), 666–686.
Sousa, Tulio (2025), “Competition and Targeting in Auctions for Online Ads,”Working Paper, Duke
University.
Tunuguntla, Srinivas (2026), “Display Ad Measurement Using Observational Data,”Working Paper,
Duke University.
Tunuguntla, Srinivas and Paul R. Hoban (2020), “A Near-Optimal Bidding Strategy for Real-Time
Display Advertising Auctions,”Journal of Marketing Research, 58 (1), 1–21.
48

Turnbull, Bruce W (1976), “The Empirical Distribution Function with Arbitrarily Grouped, Censored
and Truncated Data,”Journal of the Royal Statistical Society: Series B (Methodological), 38 (3),
290–295.
Varian, Hal R. (2007), “Position Auctions,”International Journal of Industrial Organization, 25 (6),
1163–1178.
Wu, Ruiqi, Yufeng Huang, and Nan Li (2025), “Platform Information Design and Competitive Price
Targeting,”Available at SSRN 4619584.
Yan, Qiqi “Mechanism Design via Correlation Gap,” “Proceedings of the Twenty-Second Annual
ACM-SIAM Symposium on Discrete Algorithms,” pages 710–719, SIAM (2011).
Yao, Song and Carl F. Mela (2011), “A Dynamic Model of Sponsored Search Advertising,”Marketing
Science, 30 (3), 447–468.
49

Web Appendix
Web Appendix A: Proofs from Section 4
Proof of Proposition 1.Consider any single-advertiser IC/IR mechanismM, represented
(by the taxation principle) as a menu of lottery pricings{(χ(k), µ(k))}k, where each lottery
kspecifies allocation probabilitiesχ (k) st ∈[0,1]for slotss∈ ˜Sand segmentst∈[T], and an
expected paymentm (k) =α s0γa0µ(k). Fix a lottery pricingk.
Define, for each segmentt, the CTR-weighted (slot-collapsed) allocation probability
¯χ(k) t ≡ X
s∈ ˜S
αs
αs0
χ(k) st .
Now construct a modified lottery pricing(χ(k)′, µ(k)′)that allocates only the highest available
slots 0 as follows:
χ(k)′ s0t = ¯χ(k) t ∀t, χ (k)′ st = 0∀s̸=s 0,∀t, µ (k)′ =µ (k).
For eacht, sinceα s ≤α s0 for alls∈ ˜S,
¯χ(k) t = X
s∈ ˜S
αs
αs0
χ(k) st ≤ X
s∈ ˜S
χ(k) st ≤1,
where the last inequality follows from the feasibility constraint that the advertiser receives at
most one slot for any given segment. Hence the modified lottery pricing is also feasible.
For any valuation vectorva0 = (va01, . . . , va0T ), the expected utility from lotterykunder
Mis
U (k)(va0) = X
t
X
s
pt αsβtγa0va0tχ(k) st −α s0γa0µ(k).
Under the modified lottery pricing,
U (k)′(va0) = X
t
pt αs0βtγa0va0tχ(k)′ s0t −α s0γa0µ(k)′.
1

By construction,α s0χ(k)′ s0t =α s0 ¯χ(k) t = P s αsχ(k) st for everyt, andµ (k)′ =µ (k). Therefore
U (k)′(va0) =U (k)(va0)for all valuation vectorsv a0.
Thus replacing lottery pricingkby(χ (k)′, µ(k)′)leaves the utility of that menu item un-
changed pointwise inva0, so the advertiser’s menu choice behavior is unchanged. Because the
payment parameter is unchanged, publisher revenue from this modified lottery pricing is also
unchanged. Repeating this argument for every lottery pricing in the mechanism establishes
the result.
Proof of Proposition 2.For notational convenience, we drop the advertiser and slot sub-
scripts and writeR(q)for the optimal expected revenue of the ex-ante single-advertiser prob-
lem with allocation constraintq. LetM(q)denote an optimal mechanism that achievesR(q),
and letΛ(q)be its ex-ante allocation probability. By feasibility,Λ(q)≤q.
To prove monotonicity, take anyq1, q2 ∈[0,1]. Any mechanism feasible under constraint
q1—in particularM(q 1)—satisfiesΛ(q 1)≤q 1 ≤q 2 and is therefore feasible at constraintq2.
SinceR(q 2)is the maximum revenue over all mechanisms feasible at constraintq2, we obtain
R(q2)≥R(q 1). Thus,R(q)is non-decreasing inq, and consequently,R ′(q)≥0∀q.
Take anyq1, q2 ∈[0,1]withq 1 < q2 and anyν∈[0,1]. Letq=νq 1 + (1−ν)q 2. Consider
the convex combination of mechanisms
fM≡ν M(q 1) + (1−ν)M(q 2).
The ex-ante allocation probability underfMis
eΛ =νΛ(q 1) + (1−ν) Λ(q 2)≤νq 1 + (1−ν)q 2 ≡q,
so fMis feasible for the problem with allocation constraintq.
2

Moreover, the expected revenue offMis
Revenue(fM) =ν R(q 1) + (1−ν)R(q 2).
SinceR(q)is defined as the maximum expected revenue among all mechanisms feasible at
constraintq, it follows that
R(q)≥Revenue( fM) =ν R(q 1) + (1−ν)R(q 2).
This inequality holds for everyq1, q2 ∈[0,1]and everyν∈[0,1]withq=νq 1 + (1−ν)q 2.
HenceR(·)is concave on[0,1]. Concavity immediately implies that the (right) derivative
R′(q)exists almost everywhere and is weakly decreasing wherever it exists.
Proof of Proposition 3.Fix an advertiseraand a slots. Recall that the ex-ante single-
advertiser problem with allocation constraintqchooses a menu of lotteries{(χ (k), µ(k))}k to
maximize
Ras(q) = max
K,{χ(k),µ(k)}
αsγa
KX
k=1
ξk µ(k) s.t.
KX
k=1
ξk
 X
t
pt χ(k) t
!
≤q,
whereξ k is the probability that lotterykis chosen ex-ante under the prior.
DefineΦ a(q)to be the optimal value of theslot-normalizedproblem that keeps the same
feasible menus and allocation constraint but omits the multiplicative factorαsγa from the
objective:
Φa(q) = max
K,{χ(k),µ(k)}
KX
k=1
ξk µ(k) s.t.
KX
k=1
ξk
 X
t
pt χ(k) t
!
≤q,
To prove the claim, it is sufficient to show thatΦa(q)is independent of the slots.
Consider any fixed menu{(χ (k), µ(k))}k. Take two optionsk 1, k2 from this menu. The
advertiser’s expected utility difference betweenk1 andk 2 when the highest remaining slot is
3

sis
X
t
pt αsβtγa vat

χ(k1) t −χ (k2) t

−α sγa

µ(k1) −µ (k2)

.
Factoring outα sγa >0, the sign of this difference—and thus the choice betweenk1 and
k2—is determined by
X
t
pt βt vat

χ(k1) t −χ (k2) t

−

µ(k1) −µ (k2)

,
which is independent ofs. Therefore, for any menu, the induced choice probabilities do not
depend ons. The allocation constraint P k ξk  P t ptχ(k) t  ≤qis also independent ofs.
Consequently, the feasible set of menus for the normalized problem is the same for every
s, and the only appearance of(αs, γa)in the original objective is as a multiplicative factor. It
follows that the optimal value satisfies
Ras(q) =α sγa Φa(q),
whereΦ a(q)is independent of the slots. This proves the claim.
4

Web Appendix B: General Quantile Mapping and Payments
In Section 4.4.3, we described the valuation-to-quantile mapping and payment rule under a
transparent special case in which the single-advertiser mechanisms{Ma(q)}q∈[0,1] have nested
deterministic allocations. In that case, a valuation vector can be mapped to the smallest
allocation constraintqunder which the corresponding single-advertiser mechanism allocates
the impression, and payments admit a critical-quantile interpretation.
This appendix describes the general construction, which does not require nestedness or
deterministic allocations. The key difference from the special case in the main text is that
the quantile mapping may be randomized, and payments are not generally computed using
critical quantiles. Instead, we first construct the interim mechanism induced by marginal-
revenue maximization and then implement the corresponding allocation and payment rules
through a randomized quantile mapping.
Because Proposition 3 implies that an advertiser’s normalized marginal-revenue score
γaΦ′ a(q)is common across slots, we construct a single quantile for each advertiser and re-
alized segment. The construction therefore does not treat exact slot assignments separately.
Instead, it summarizes the advertiser’s position allocation in top-slot-equivalent units.
B.1 Preliminaries
The marginal revenue approach requires a mapping from advertiser valuation vectors to quan-
tiles. We begin with the observation that the induced quantiles must be uniformly distributed
under the advertiser’s prior (Alaei et al. 2013). That is, for each advertiseraand realized
segmentt, the final mappingQ at should satisfy
Qat(va)∼Unif[0,1]whenv a ∼F a.
Suppose first that such a quantile mapping has been constructed. Given a vector of
quantilesq= (q 1, . . . , qA), the marginal-revenue allocation rule assigns slots in decreasing
order of the scoresγ aΦ′ a(qa), excluding advertisers with non-positive marginal revenue and
5

breaking ties arbitrarily.
LetI M R as (q,Q −a)∈ {0,1}indicate that advertiserais assigned slotsby the marginal-
revenue allocation rule when its own quantile isq. Define advertisera’s quantile-space, top-
slot-equivalent allocation curve as
ωM R a (q) =E Q−a
" SX
s=1
αsI M R as (q,Q −a)
#
,
where the expectation is taken over the independently drawn quantiles of the other advertisers
and over any tie-breaking randomization.
Equivalently, settingαS+1 = 0and∆ j =α j −α j+1,
ωM R a (q) =
SX
j=1
∆j Pr{ais among the topjeligible advertisers|q a =q}.
SinceΦ a is concave,Φ ′ a(q)is weakly decreasing inq. Consequently, each probability in the
equation above, and thereforeωM R a (q), is weakly decreasing inq.
The use of the top-slot-equivalent allocation curve is important in the multi-slot environ-
ment. The probability that an advertiser receives a particular slot need not be monotone in
its quantile, because weakening its score may move it from a higher slot to a lower slot. In
contrast, its click-through-rate-weighted allocation is weakly decreasing in its quantile.
B.2 Interim Mechanism as a Convex Combination of{Ma(q)}
The functionω M R a (q)determines the interim mechanism faced by advertisera. In particular,
the interim mechanism is a convex combination of the optimal single-advertiser mechanisms
{Ma(q)}q∈[0,1], with weights determined by the decrease inωM R a (q)(Alaei et al. 2013). Thus,
the interim mechanismM a can be expressed as17
M a =
Z 1
0
Ma(eq)

−dωM R a (eq)  .
17Formally, the integral is interpreted with respect to the Lebesgue--Stieltjes measure induced byωM R a , including
the appropriate boundary mass atq= 1. Any residual probability mass1−ωM R a (0)is assigned to the null mechanism
Ma(0).
6

Operationally, M a draws an allocation constraint˜qaccording to the distribution induced
byω M R a above and then offers advertiserathe single-advertiser mechanismMa(˜q).
Let χat(va)denote the probability thatM a allocates the top-slot-equivalent impression in
segmentt, when its valuation vector isv a and µa(va)denote the corresponding normalized
expected payment. The objective of the quantile mapping and payment construction is to
implement this target interim allocation and payment rule in the multi-advertiser auction.
Since everyM a(q)is incentive compatible and individually rational and their convex com-
bination induced byω M R a to construct M a does not depend on advertisera’s valuation, M a
is also incentive compatible and individually rational.
B.3 Constructing the Quantile Mapping
For a fixed advertiseraand segmentt, the target allocation ruleχat(va)induces an ordering
over valuation vectors. Higher values ofχat correspond to stronger types: under the target
interim mechanism, they receive a greater top-slot-equivalent allocation.
The rank of a valuation vectorva induced by such an ordering is given by
ρat(va) = Pr v′a∼Fa {χat(v′ a)> χat(va)}.
This ranking in turn induces a ranked interim allocation curve
gat(r) = sup

y∈[0,1] : Pr
va∼Fa
(χat(va)≥y)≥r

.
Thus,g at(r)is the allocation probability of a valuation vector at rankrwhen valuation
vectors are sorted in decreasing order of their target allocation probabilities. This curve is
weakly decreasing inrby construction.
The rankingρ at satisfies the propertyρ at(va)∼Unif[0,1]whenv a ∼F a18. However,
18ρat(va)∼Unif[0,1]assuming that the distribution ofx at(va)whenv a ∼F a is atomless. When the target
allocation rule has atoms, ties can be broken by an independent uniform random variable. In particular, one may
replaceρ at(va)byPr{x at(V′ a)> xat(va)}+U 0 at Pr{xat(V′ a) =xat(va)},whereU 0 at ∼Unif[0,1]. This randomized rank
is uniform without the atomlessness assumption.
7

ρat(va)cannot generally be used directly as the final quantile. If the mechanism usedqat =
ρat(va), then the advertiser’s resulting ranked allocation curve would beωM R a (ρat(va)), which
implements the quantile-space winning curveωM R a , not the ranked interim allocation curvegat.
In general,ω M R a (r)̸=g at(r). Thus, the rank mapping has the correct distributional property,
but it need not implement the correct ranked allocation curve.
To obtain the correct implementation, we modify the rank mappingρ at(va)using the
interval-resampling construction of Alaei et al. (2013). The goal is to construct a randomized
transformation
Ψat : [0,1]→[0,1]
such that, forR∼Unif[0,1],
Ψat(R)∼Unif[0,1],
and, for each rankr,
E

ωM R a  Ψat(r)  =g at(r),
where the expectation is taken over the randomization inΨat.
The first condition preserves the uniform distribution of quantiles. The second condition
ensures that the marginal-revenue allocation rule implements the target allocation probability
prescribed by the interim mechanismM a.
The transformationΨat is constructed by interval resampling. In a discrete approximation,
order valuation vectors by the rankρat. Whenever the quantile-space allocation curveωM R a
differs from the ranked target allocation curvegat, identify an interval of ranks over which
averagingω M R a produces the desired level ofgat. Types whose preliminary ranks fall in this
interval are then resampled uniformly within the interval. Repeating this procedure over
the ordered type space yields a sequence of resampling intervals. This procedure preserves
the uniform distribution of final quantiles while ensuring that the allocation probabilities
induced by the marginal-revenue allocation rule coincide with the target interim allocation
probabilities.
8

The final segment-specific quantile mapping is
Qat(va) = Ψat

ρat(va)

.
By construction,Q at(va)∼Unif[0,1]whenv a ∼F a, and the marginal-revenue allocation rule
implements the target segment-contingent allocation probabilityχat(va). This construction
nests the deterministic mapping in Section 4.4.3.
B.4 Payments
In the nested deterministic case described in the main text, payments can be represented
using critical quantiles. In the general case, such a representation need not exist. Payments
are instead inherited from the target interim mechanismM a.
Let µa(va)denote the normalized expected payment underM a, and define
λa(va) =
TX
t=1
ptχat(va).
Thus, λa(va)is advertisera’s ex-ante allocation in top-slot-equivalent units under the target
interim mechanism. Sinceα1 = 1, the corresponding expected payment in the position auction
isγ aµa(va). To collect this payment only when the advertiser receives a slot, one convenient
implementation charges
mimp ast (va) =α sγa µa(va) λa(va) .
If payments are collected per click, the impression payment is divided by the realized click-
through rateα sβtγa. The resulting per-click payment is
mclick ast (va) = µa(va) βtλa(va) .
In the nested deterministic case, the layer-specific critical-quantile payments described in
Section 4.4.3 provide an alternative disaggregation of the same expected payment.
9

Web Appendix C: Notation and Algorithm Summary
Notation Definition
a∈[A], s∈[S], t∈[T]Advertiser, slot, and segment indices.
pt Probability of segmentt.
va = (va1, . . . , vaT )Advertisera’s valuation vector, wherev at is
the per-click valuation for segmentt.
Fa Distribution of advertisera’s valuation
vector.
ba = (ba1, . . . , baT )Advertisera’s bid vector, whereb at is the
bid for segmentt.
αs, βt, γa Slot, segment, and advertiser effects in the
click-through rate¯cast =α sβtγa.
xast(V), ma(V)Allocation rule and expected payment rule.
Ras(q) =α sγaΦa(q),Φ a(q),Φ ′ a(q)Revenue curve, slot-normalized revenue
curve, and normalized marginal revenue.
Ma(q)Optimal single-advertiser mechanism
attainingΦ a(q)under allocation constraint
q.
Ωat(q)Allocation region induced by a deterministic
mechanismM a(q)for segmentt.
qat =Q at(va)Quantile associated with advertisera’s
valuation vector for segmentt.
χ(k) t , µ(k) Allocation probability and payment
parameter associated with menu optionk.
Table 3:Summary of notation
10

Algorithm 1Information-Bundling Position Auction (IBPA)
1:Inputs:
2:Segment probabilitiesp t
3:Advertiser priorsF a
4:Quality scoresγ a
5:Slot effectsα s
6:
7:Outputs:
8:Allocationsx ast
9:Paymentsm a
10:
Offline Stage: Construct Revenue Curves
11:foreach advertiserado
12:Solve the slot-normalized constrained single-advertiser problem for allq∈[0,1](Equa-
tion 4)
13:Construct the normalized revenue curveΦ a(q)(Section 4.4.2)
14:Construct the segment-specific valuation-to-quantile mappingsQ at(va)for all segments
t(Section 4.4.3 and Web Appendix B)
15:end for
Online Stage: Marginal-Revenue Auction
16:foreach arriving impressiondo
17:Publisher observes realized segmentt
18:Advertisers submit bid vectorsv a (truthful bidding in equilibrium)
19:foreach advertiserado
20:Compute quantile from valuation vector:
qat =Q at(va)
21:Compute marginal revenue from quantile for each slot (Proposition 3):
R′ as(qat) =α sγaΦ′ a(qat)
22:end for
23:Allocate slots greedily in decreasing order ofα s, assigning each slot to the unassigned
advertiser with the highest positive marginal revenue (Section 4.4.3)
24:Compute payment for each winning advertiser (Section 4.4.3 and Web Appendix B)
25:end for
11

Web Appendix D: Proofs from Section 5
Proof of Proposition 4.Weverifyfeasibility, Bayesianincentivecompatibility, andBayesian
individual rationality in turn.
Feasibility follows directly from the allocation rule. For each realized segment, IBPA
processes slots in decreasing order of slot effect and assigns each slot to at most one advertiser.
Once an advertiser is assigned a slot, that advertiser is removed from consideration for lower
slots. Hence, for every valuation profileV, segmentt, and slots,
X
a
xast(V)≤1and
X
s
xast(V)≤1,
so the feasibility constraints in Equation (1) are satisfied.
We next establish incentive compatibility. Fix an advertisera. Conditional on advertiser
a’s reported valuation vector, the marginal-revenue allocation rule and the quantile construc-
tion induce an interim mechanism for advertisera, where the expectation is taken over the
valuations of the remaining advertisers and over any randomization in the mechanism. By
construction (see Web Appendix B), this interim mechanism can be represented as a con-
vex combination of the single-advertiser mechanisms{M a(q)}q∈[0,1], with weights induced
by the marginal-revenue allocation rule. Each single-advertiser mechanismM a(q)is incen-
tive compatible by construction, since it solves the single-agent constrained problem over
incentive-compatible mechanisms. A convex combination of incentive-compatible mechanisms
is incentive compatible: for any true valuation vectorva and any reportba, truthful reporting
yields weakly higher expected utility in each component mechanism, and therefore also in their
expectation. Hence truthful reporting maximizes advertisera’s interim expected utility. Since
this argument applies to every advertisera, truthful multidimensional reporting constitutes a
Bayes–Nash equilibrium, and the IBPA mechanism is BIC.
Finally, individual rationality follows from the same convex-combination argument. Each
single-advertiser mechanismMa(q)is individually rational by construction, so truthful partici-
12

pation gives advertiseraweakly non-negative expected utility in every component mechanism.
Any convex combination of these mechanisms therefore also gives weakly non-negative interim
expected utility. Thus the IBPA mechanism satisfies BIR.
Combining feasibility, BIC, and BIR establishes the result.
Proof of Theorem 5.We prove the result in two steps. First, we upper-bound the revenue
of the optimal feasible BIC and BIR mechanism by an ex-ante relaxation. Second, we show
that IBPA obtains at least a(1−1/e)fraction of this ex-ante relaxation.
Throughout the proof, we useα1 = 1and letα S+1 = 0. For notational simplicity, we write
Φ′ a(q)for the marginal revenue of advertisera. At points whereΦa is not differentiable, take
any subgradient; the argument is unchanged by the usual ironing or tie-breaking conventions.
Consider any feasible BIC and BIR mechanismMfor the publisher’s problem in Equation
1, with allocation rulexM ast(V)and payment rulem M a (V). For advertisera, define the interim
allocation and payment rules induced byM, obtained by integrating over the valuation vectors
of the other advertisers:
X M ast(va) =E V−a  xM ast(va,V −a)  ,¯m M a (va) =E V−a  mM a (va,V −a)  .
BecauseMis BIC and BIR, this interim single-advertiser mechanism is IC and IR for adver-
tisera.
Now collapse advertisera’s interim slot allocation into top-slot-equivalent impression units.
Define
˜xM at (va) =
SX
s=1
αsX M ast(va).
as the probability of receiving the top slot that would generate the same click-through-rate-
weighted allocation as the original slot assignment. Thus˜xM at (va)converts the original slot
allocation into an equivalent top-slot allocation measured in click-through-rate units. Since
the original mechanism assigns advertiserato at most one slot for each realized segment and
13

αs ≤1, we have
0≤˜x M at (va)≤1for alla, t,v a.
Moreover, the collapsed allocation preserves advertisera’s interim utility:
TX
t=1
ptβtγavat ˜xM at (va)−¯mM a (va) =E V−a
" TX
t=1
SX
s=1
ptαsβtγavatxM ast(va,V −a)−m M a (va,V −a)
#
.
Thus the collapsed rule(˜xM a ,¯mM a )is a feasible IC and IR single-advertiser mechanism for the
top slot.
Let
zM a =E va
" TX
t=1
pt ˜xM at (va)
#
=E V,t
" SX
s=1
αsxM ast(V)
#
(5)
denote advertisera’s ex-ante top-slot-equivalent allocation probability underM. By the def-
inition of the normalized single-advertiser revenue curveΦa, no IC and IR single-advertiser
mechanism that allocates top-slot-equivalent impression with ex-ante probability at mostzM a
can extract more thanγaΦa(zM a )from advertisera. Therefore,
EV

mM a (V)  ≤γ aΦa(zM a ).
Summing over advertisers gives
RevM =
AX
a=1
EV

mM a (V)  ≤ AX
a=1
γaΦa(zM a ),(6)
whereRev M is the expected revenue of the mechanismM.
We next characterize the ex-ante feasibility of the vectorzM = (z M 1 , . . . , zM A ). For any
subset of advertisersB⊆[A], ex-post feasibility ofMimplies that, for every valuation profile
Vand segmentt,
X
a∈B
SX
s=1
αsxM ast(V)≤
min{|B|,S}X
j=1
αj.
The right-hand side is the largest total slot effect that can be assigned to advertisers inB:
14

assign up to|B|advertisers to the highest available slots. Taking expectations overVandt
and using 5, we obtain
X
a∈B
zM a ≤
min{|B|,S}X
j=1
αj ∀B⊆[A].
Define the ex-ante impression-allocation polytope
Pα =


z∈R A + : X a∈B za ≤ min{|B|,S}X j=1 αj ∀B⊆[A]    .
The preceding argument shows that every ex-post feasible mechanism induces an ex-ante
vectorz M ∈ Pα. Hence every feasible BIC and BIR mechanismMsatisfies
RevM ≤
AX
a=1
γaΦa(zM a )≤max z∈Pα
AX
a=1
γaΦa(za),
where the first inequality follows from equation 6. Define the ex-ante relaxation value as
RevEA ≡max
z∈Pα
AX
a=1
γaΦa(za).
Taking the supremum over all feasible BIC and BIR mechanismsMyields a bound on the
optimal revenue
RevOPT ≤Rev EA.
It remains to compare IBPA to the ex-ante relaxation. Consider the following single-
dimensional analog of the publisher’s multidimensional problem, where each advertisera’s
type is represented by a scalar quantileqa ∼Unif[0,1], advertisera’s revenue curve isG a(q) =
γaΦa(q), and the feasibility constraint is the same ex-ante service polytopePα. The ex-ante
relaxation of this analog is exactlyRevEA.
By construction of the segment-specific quantile mappings in IBPA, for every advertisera
and segmentt,Q at(va)∼Unif[0,1], whenv a ∼F a. Since advertisers’ valuation vectors are
independent across advertisers, the quantiles(Q1t(v1), . . . , QAt(vA))are independent across
15

advertisers for every realized segmentt. This argument does not require independence across
segments within an advertiser’s valuation vector; arbitrary within-advertiser dependence is
already incorporated into the single-advertiser revenue curveΦa and the quantile mappings
Qat.
Conditional on the realized segmentt, IBPA assigns slots to maximize total marginal
revenue:
max
x
AX
a=1
SX
s=1
αsγaΦ′ a(Qat(va))x as
subject to the assignment constraints that each advertiser receives at most one slot and each
slot is assigned to at most one advertiser. This is precisely the marginal-revenue mechanism for
the single-dimensional analog, with revenue curvesGa(q) =γ aΦa(q)and feasibility constraint
Pα. The payment rule of IBPA implements the interim mechanism corresponding to this
marginal-revenue allocation rule, so the revenue of IBPA in the original environment equals
the revenue of the marginal-revenue mechanism in the analog.
We now apply the feasibility-based approximation result. To do so, it suffices to verify
that the weighted rank functions induced by the position-auction feasibility constraint are
monotone and submodular. Fix any nonnegative weight vectorw= (w1, . . . , wA). For a set
of available advertisersD⊆[A], define the weighted rank function induced by the position
auction as
fw(D) = max xas∈{0,1}P
s xas≤1, P a xas≤1
X
a∈D
SX
s=1
αswaxas.
Equivalently,f w(D)assigns the largest weight inDto the highest slot, the second-largest
weight to the second-highest slot, and so on. Letrw k (D)denote the weighted rank function of
thek-unit uniform matroid, i.e., the sum of theklargest weights inD. Then
fw(D) =
SX
k=1
(αk −α k+1)r w k (D).
Eachr w k (·)is monotone and submodular, and the coefficientsα k −α k+1 are nonnegative.
16

Thereforef w(·)is monotone and submodular.
By the correlation-gap bound of Yan (2011), as used in the feasibility-based approximation
framework of Alaei et al. (2013), the ex-post feasible marginal-revenue mechanism for any
environment whose weighted rank functions are monotone submodular obtains at least a
(1−1/e)fraction of the ex-ante relaxation. Applying this result to the single-dimensional
analog gives
RevIBPA ≥

1− 1 e  RevEA.
Combining this lower bound withRevOPT ≤Rev EA, we obtain
RevIBPA ≥

1− 1 e  RevOPT.
This proves the theorem.
Proof of Theorem 6.Fix an arbitrary disclosure partitionP disc ={B 1, . . . , BD}. Let
pd =
X
t∈Bd
pt
denote the probability that the realized segment belongs to disclosure blockd. For each
advertisera, define the block-level value
¯vad =
X
t∈Bd
pt
pd
βtvat.
Equivalently, if the segment effectβt is absorbed into the valuation, then¯vad is simply adver-
tisera’s expected valuation over the segments in blockd. Conditional on disclosure blockd,
receiving slotstherefore gives advertiseraexpected gross valueα sγa¯vad.
Consider any scalar-bid disclosure mechanismMSB(Pdisc). Because the mechanism elicits
only a scalar bid for the disclosed block, and allocations and payments depend only on this
17

scalar bid and the disclosed block, the mechanism treats all segments inBd as a single object
from the advertiser’s perspective. Thus, conditional on disclosure blockd,MSB(Pdisc)induces
a single-parameter position-auction environment in which advertisera’s type is¯vad.
IfM SB(Pdisc)is not itself a direct truthful mechanism, fix any Bayes–Nash equilibrium of
the mechanism. By the revelation principle, the allocation and payment rules induced by this
equilibrium can be implemented by a direct BIC and BIR mechanism in the corresponding
single-parameter environment, with the same expected publisher revenue. Hence the revenue
of any scalar-bid disclosure mechanism is bounded above by the revenue of the optimal BIC
and BIR mechanism in the block-level single-parameter environment induced byPdisc.
LetRev IBPA(Pdisc)denote the revenue of the marginal-revenue mechanism in this auxiliary
block-level environment, where the objects being sold are the disclosure blocksB1, . . . , BD
and the realized block is fully disclosed. Since this is a standard single-parameter environment
with quasi-linear preferences and position-auction feasibility constraints, the marginal-revenue
mechanism is revenue-maximizing among all feasible BIC and BIR mechanisms. Therefore,
RevMSB(Pdisc)≤Rev IBPA(Pdisc).
It remains to compare this auxiliary block-level IBPA benchmark with the proposed IBPA
mechanism, which operates on the full segment space and does not disclose the realized seg-
ment. We do this by comparing the underlying single-advertiser revenue curves.
Fix advertisera, slots, and allocation constraintq∈[0,1]. Let ¯ΦPdisc a (q)denote the
normalized single-advertiser revenue curve in the auxiliary block-level environment, and let
Φa(q)denote the normalized single-advertiser revenue curve under the full segment space with
no disclosure.
We claim that
Φa(q)≥ ¯ΦPdisc a (q)for alla, q.
To see this, take any single-advertiser mechanism feasible in the auxiliary block-level envi-
18

ronment under allocation constraintq. Under that mechanism, after blockdis disclosed, the
advertiser faces a menu of lotteries over that block. Let a generic option in the menu for block
dbe denoted byℓ d, with allocation probability¯χd(ℓd)and normalized payment¯µd(ℓd), both
conditional on blockd.
We now construct a no-disclosure single-advertiser mechanism on the original segment
space that replicates this block-level mechanism. The no-disclosure menu contains one option
for every tuple
ℓ= (ℓ 1, . . . , ℓD),
whereℓ d is an option from the block-dmenu. For such a tuple, define the segment-level
allocation rule and normalized payment by
χt(ℓ) = ¯χd(ℓd)for everyt∈B d,
and
µ(ℓ) =
DX
d=1
pd ¯µd(ℓd).
For any valuation vectorva, the advertiser’s utility from tupleℓin the constructed no-
disclosure mechanism is
DX
d=1
X
t∈Bd
ptβtvat ¯χd(ℓd)−
DX
d=1
pd ¯µd(ℓd) =
DX
d=1
pd [¯vad ¯χd(ℓd)−¯µd(ℓd)].
Because the menu contains all tuples of block-level options, maximizing this expression over
ℓis equivalent to choosing, for each blockd, the option that the advertiser would have chosen
after observingdin the auxiliary block-level mechanism. Thus, the constructed no-disclosure
mechanism replicates the same ex-ante allocation probability, the same expected payment,
and the same utility for every valuation vector. In particular, it satisfies the same ex-ante
allocation constraintqand generates the same expected revenue.
Therefore, every single-advertiser mechanism feasible in the auxiliary block-level envi-
19

ronment is also feasible under the full segment space with no disclosure. This proves that
Φa(q)≥ ¯ΦPdisc a (q)for alla, q. Since the slot-specific revenue curve factorizes as
Ras(q) =α sγaΦa(q),
this implies that the full-segment/no-disclosure revenue curves weakly dominate the auxiliary
block-level revenue curves for every advertiser and slot:
Ras(q)≥ ¯RPdisc as (q)for alla, s, q.
The marginal-revenue mechanism preserves this pointwise ordering of single-advertiser rev-
enue curves: if one environment yields weakly higher single-advertiser revenue curves for every
advertiser, slot, and allocation probability, then the corresponding multi-advertiser marginal-
revenue mechanism yields weakly higher expected revenue. Applying this monotonicity prop-
erty gives
RevIBPA ≥Rev IBPA(Pdisc).
Combining the above inequality withRevMSB(Pdisc)≤Rev IBPA(Pdisc), we obtain
RevIBPA ≥Rev IBPA(Pdisc)≥Rev MSB(Pdisc).
Since the disclosure partitionPdisc and the scalar-bid disclosure mechanismMSB(Pdisc)were
arbitrary, the result follows.
Proof of Theorem 7.We prove the two monotonicity statements by comparing the single-
advertiser revenue curves induced by the relevant information and disclosure regimes. The
argument parallels the proof of Theorem 6.
For any information partitionPinfo and disclosure partitionP disc such thatP info ⪰ Pdisc,
20

let
RPinfo,Pdisc as (q)
denote advertisera’s slot-srevenue curve under the pair(Pinfo,P disc). By Proposition 3, this
curve factorizes as
RPinfo,Pdisc as (q) =α sγaΦPinfo,Pdisc a (q),
whereΦ Pinfo,Pdisc a (q)is the corresponding normalized single-advertiser revenue curve.
We first establish monotonicity in information granularity. Fix a disclosure partitionPdisc,
and letP (1) info ⪰ P(2) info, with both pairs(P(1) info,P disc)and(P (2) info,P disc)feasible. Fix an advertiser
a, a slots, and an allocation constraintq∈[0,1].
Consider any single-advertiser mechanism feasible under the coarser information partition
P (2) info. Under this mechanism, after disclosure blockd∈ Pdisc is revealed, the advertiser faces
a menu whose options specify allocation probabilities over the information blocks contained
ind. Let a generic menu option be denoted byℓd, and let¯χC(ℓd)be the allocation probability
assigned to coarse information blockC∈ P(2) info withC⊆d. Let¯µ(ℓ d)denote the associated
normalized payment.
We now construct a mechanism under the finer information partitionP(1) info that replicates
this coarser mechanism. For every fine information blocki∈ P(1) info, letC(i)be the unique
block inP (2) info such thati⊆C(i). Define the allocation rule under the finer partition by
χi(ℓd) = ¯χC(i)(ℓd)for everyi⊆d,
and keep the same normalized payment,
µ(ℓd) = ¯µ(ℓd).
This construction preserves utilities pointwise. To see this, letpi = P t∈i pt and define
21

advertisera’s expected value for information blockias
¯vai = 1 pi X t∈i ptβtvat.
For any coarse information blockC, the corresponding coarse-block value is
¯vaC = 1 pC X i⊆C pi¯vai.
Therefore, the utility from optionℓd under the finer-information mechanism is
X
i⊆d
pi
pd
¯vaiχi(ℓd)−µ(ℓ d) =
X
C⊆d
pC
pd
¯vaC ¯χC(ℓd)−¯µ(ℓd),
which is exactly the utility from the corresponding option under the coarser-information mech-
anism. Hence the advertiser makes the same menu choice, the publisher obtains the same
expected payment, and the ex-ante allocation probability is unchanged. In particular, the
constructed mechanism satisfies the same allocation constraintqand generates the same ex-
pected revenue.
Thus every single-advertiser mechanism feasible under(P(2) info,P disc)is also feasible under
(P (1) info,P disc). It follows that, for every advertisera, slots, and allocation constraintq,
R
P (1) info,Pdisc
as (q)≥R
P (2) info,Pdisc
as (q).
That is, finer information weakly raises the single-advertiser revenue curves.
We next establish monotonicity in disclosure granularity. Fix an information partition
Pinfo, and letP (1) disc ⪰ P(2) disc, with both pairs(Pinfo,P (1) disc)and(P info,P (2) disc)feasible. Thus, each
blockD∈ P(2) disc is a union of blocksd∈ P(1) disc.
Fix advertisera, slots, and allocation constraintq. Consider any single-advertiser mech-
anism feasible under the finer disclosure partitionP(1) disc. Under this mechanism, after a fine
disclosure blockd∈ P (1) disc is revealed, the advertiser faces a menu of options. Letℓd denote
22

an option from the menu associated with fine disclosure blockd, with allocation probabilities
¯χi(ℓd)for information blocksi∈ Pinfo satisfyingi⊆d, and normalized payment¯µ(ℓ d).
We construct a mechanism under the coarser disclosure partitionP(2) disc that replicates the
finer-disclosure mechanism. Fix a coarse disclosure blockD∈ P(2) disc, and let
D(D) ={d∈ P(1) disc :d⊆D}
be the set of fine disclosure blocks contained inD. The menu offered afterDis disclosed
contains one option for every tuple
ℓD = (ℓd)d∈D(D),
whereℓ d is an option from the fine-disclosure menu associated with blockd.
For such a tuple, define the allocation probability for each information blocki⊆dby
χi(ℓD) = ¯χi(ℓd),
and define the normalized payment by
µ(ℓD) =
X
d∈D(D)
pd
pD
¯µ(ℓd),
wherep d = P t∈d pt andp D = P d∈D(D) pd.
For any valuation vectorva, the advertiser’s utility from tupleℓD conditional on coarse
disclosure blockDis
X
i⊆D
pi
pD
¯vaiχi(ℓD)−µ(ℓ D).
Using the construction above, this can be written as
X
d∈D(D)
pd
pD
"X
i⊆d
pi
pd
¯vai ¯χi(ℓd)−¯µ(ℓd)
#
.
23

Because the menu under the coarse disclosure blockDcontains all tuples of fine-block menu
options, maximizing this expression overℓD is equivalent to choosing, separately for each fine
disclosure blockd⊆D, the option that the advertiser would have chosen whendwas directly
disclosed under the finer-disclosure mechanism. Therefore, the coarser-disclosure mechanism
replicates the same ex-ante allocation probabilities and the same expected payments as the
finer-disclosure mechanism. In particular, it satisfies the same allocation constraintqand
generates the same expected revenue.
Thus every single-advertiser mechanism feasible under(Pinfo,P (1) disc)is also feasible under
(Pinfo,P (2) disc). Hence, for every advertisera, slots, and allocation constraintq,
R
Pinfo,P (1) disc
as (q)≤R
Pinfo,P (2) disc
as (q).
That is, coarser disclosure weakly raises the single-advertiser revenue curves.
Finally, as in the proof of Theorem 6, the marginal-revenue mechanism preserves pointwise
dominance of the single-advertiser revenue curves: if one regime yields weakly higher revenue
curvesR as(q)for every advertisera, slots, and allocationprobabilityq, then thecorresponding
multi-advertiser IBPA mechanism yields weakly higher expected publisher revenue. Applying
this monotonicity property to the revenue-curve dominance derived above proves the theorem.
24

Web Appendix E: Computational Complexity and Approximation
Wenowdiscussthecomputationalchallengesofsolvingtheex-anteconstrainedsingle-advertiser
problem. Solving the ex-ante constrained single-advertiser problem in Section 4 requires op-
timizing over the full classMof arbitrary menu of randomized bundle pricings, where each
menu option specifies a allocation-probability vectorχ∈[0,1] T and an associated expected
paymentµ. While the problem is conceptually straightforward, the optimal menu can have
arbitrary length; consequently, computation can become expensive when the number of seg-
mentsTis large (Manelli and Vincent 2007; Hart and Nisan 2013).
To address this complexity, we consider two structured families of mechanisms that approx-
imateMwhile retaining strong revenue guarantees. The first restricts allocation-probability
vectors to be binary, reducing the menu to a collection of deterministic bundles. The sec-
ond further restricts payments to follow a simple additive form. Both classes retain strong
performance guarantees by preserving the core price-discrimination structure of the full mech-
anism while also simplifying computation. We also discuss how the main theoretical results
in Section 5 extend to these approximations.
E.1 Binary-Allocation Menus
Our first approximation solves the single-advertiser problem by restricting attention to menus
of bundle pricings with binary allocation-probability vectors. Formally, define
M0 bin ={(χ, µ)∈ M:χt ∈ {0,1} ∀t}.
A menu option inM0 bin therefore corresponds to offering the advertiser a subset of segments
together with an associated payment: the advertiser receives exactly those segments for which
χt = 1. To ensure individual rationality, we normalize the payment for the zero-allocation
vector to beµ(0) = 0.
Since there are at most2 T binary allocation-probability vectors and the zero vector is
normalized, solving the optimal single-advertiser mechanism for any ex-ante allocation con-
25

straintqrequires computing at most2 T −1payments, one for each non-zero allocation vector.
Although this growth is exponential inT, it is far more tractable than optimizing over the
full mechanism classM, whose optimal menus may require infinitely many (non-binary) ran-
domized bundles.
Mechanisms inM 0 bin are closely related to the classic mixed bundling approach in multi-
product monopoly pricing. Each binary allocation vector corresponds to a bundle of segments,
and the mechanism offers a menu of such bundles with associated prices to implement second-
degree price discrimination.
LetM bin be the convex closure ofM0 bin. That is,M bin includes all convex combinations
of mechanisms inM 0 bin. We denote the marginal-revenue extension of this restricted single-
advertiser class byIBPAbin.
Despiteitssimplicity,M bin enjoysstrongapproximationguaranteesforthesingle-advertiser
problem: when valuations across segments are drawn independently (i.e., from a product dis-
tribution), the optimal mechanism inMbin achieves a constant-factor approximation to the
optimal revenue inM, and under arbitrary correlations, it achieves anO(logT)approximation
(see Proposition 10).
The following propositions show that the theoretical results from Section 5 continue to
hold forIBPA bin.
Proposition 8.For every disclosure partitionPdisc and any scalar-bid disclosure mechanism
MSB(Pdisc),
RevIBPAbin ≥Rev MSB(Pdisc).
The proof follows Theorem 6 withMbin replacingM. For any disclosure partitionP disc,
a scalar-bid disclosure mechanism induces a block-level single-parameter position auction,
whose revenue is bounded by the corresponding marginal-revenue mechanism. The single-
agent mechanisms in this auxiliary problem are threshold rules, or convex combinations of
threshold rules after ironing, and hence belong toMbin. The tuple construction from The-
orem 6 embeds these block-level binary mechanisms into the full-information/null-disclosure
26

environment without changing utilities, allocation probabilities, or payments. Thus theMbin
revenue curves weakly dominate the scalar-bid block-level curves, implying the result.
Proposition 9.For anyP (1) info ⪰ P(2) info and for allP disc such that both pairs(P(1) info,P disc)and
(P (2) info,P disc)are feasible,
RevIBPAbin(P (1) info,P disc)≥Rev IBPAbin(P (2) info,P disc).
Similarly, for anyP(1) disc ⪰ P(2) disc and for allPinfo such that both pairs(Pinfo,P (1) disc)and(P info,P (2) disc)
are feasible,
RevIBPAbin(Pinfo,P (1) disc)≤Rev IBPAbin(Pinfo,P (2) disc).
The proof is the restricted version of Theorem 7. Finer information weakly enlarges the
feasible set because any binary menu defined on a coarser information partition can be repli-
cated by assigning each finer block the allocation and payment of its containing coarse block.
Coarser disclosure also weakly enlarges the feasible set because any binary menu under finer
disclosure can be replicated by offering tuples of fine-block menu options, with payments ag-
gregated by their probability weights. Both constructions preserve utilities, payments, and
ex-ante allocation probabilities, and both remain withinM bin. Hence the corresponding
binary-menu revenue curves move monotonically in the stated directions, and the marginal-
revenue extension gives the result.
E.2 Additive-Pricing Menus
Our second approximation restricts payments to follow an additive structure:
µ(χ) =ρ 0 +
X
t∈[T]
ptχtρt,
whereρ t is a fixed price for targeting segmenttandρ 0 can be interpreted as an entry fee
for participating in the mechanism. The resulting class,M0 add ⊂ M0 bin, retains the binary-
allocationstructurewhileimposingasimple, linearpricingrule. Asbefore, toensureindividual
27

rationality, we normalize the payment for the zero-allocation vector to beµ(0) = 0.
Thisstructureiscomputationallyconvenient: menusneedonlyspecifyavector(ρ 0, ρ1, . . . , ρT ),
and the resulting mechanism is implementable in time polynomial inT(Proposition 11).
LetM add be the convex closure ofM0 add. We denote the marginal-revenue extension of
this restricted single-advertiser class byIBPAadd.
Despite its simplicity,Madd achieves the same revenue-approximation guarantees asMbin
under both independent and correlated valuations (Proposition 10). In practice,Madd pro-
vides a highly scalable approximation that preserves the essential mixed-bundling logic of the
full IBPA mechanism.
Proposition 10.For the ex-ante constrained single-advertiser problem, the mechanism class
Mbin of binary-allocation menus and its subclassMadd of additive-pricing menus each achieve
a constant-factor approximation to the optimal revenue inMwhen valuations across segments
are drawn independently (i.e., from a product distribution). More generally, when valuations
may be arbitrarily correlated across segments, both classes achieve anO(logT)approximation
to the optimal revenue.
Proof.See Section E.3.
Proposition 11.For the ex-ante constrained single-advertiser problem, optimization over the
classM add can be carried out, for any approximation toleranceϵ >0, in time polynomial in
both dimensionsTand tolerance1/ϵ. In particular, each step of an optimization routine can
be implemented inO(T)operations.
Proof.See Section E.3.
E.3 Proofs
Proof of Proposition 10.Fix a single advertisera 0 and the highest available slots0. Be-
cause the multiplicative factorαs0γa0 is irrelevant for approximation ratios, we work with the
slot-normalized problem in Equation (4). A single-advertiser mechanism is a menu of options
{(χ(k), µ(k))}K k=1, whereχ (k) ∈[0,1] T specifies, for each segmentt, the probabilityχ (k) t that
28

the advertiser is served when segmenttrealizes, andµ (k) is the corresponding normalized
expected payment. Letξ k denote the ex-ante probability (under the advertiser’s prior) that
optionkis chosen. For any such menuM, define its normalized expected revenue and its
ex-ante allocation probability:
Rev(M)≡
KX
k=1
ξk µ(k),Alloc(M)≡
KX
k=1
ξk
 TX
t=1
pt χ(k) t

.
For a mechanism classC ⊆ M, let
OPTC(q)≡sup

Rev(M) :M∈ C,Alloc(M)≤q

denote the optimal value at ex-ante capq. Our goal is to show that for everyq∈[0,1],
OPTMbin(q)andOPT Madd(q)approximateOPT M(q)within a constant factor under indepen-
dent values and withinO(logT)under arbitrary correlations.
For any mechanism classC ⊆ Mand any multiplierλ≥0, define the Lagrangian value
ΠC(λ)≡sup
M∈C

Rev(M)−λAlloc(M)

.
For anyλ≥0and any mechanismMfeasible at capq(i.e.,Alloc(M)≤q),
Rev(M)≤Rev(M)−λAlloc(M) +λq≤Π M(λ) +λq.
Taking the supremum over allM∈ Mfeasible atqyields the weak-duality bound
OPTM(q)≤Π M(λ) +λq∀λ≥0.(7)
We now show that the single-advertiser problem is isomorphic to a seller offering multiple
items (one per segmentt) to a single buyer with additive per-item values. For a realized
valuation vectorv= (v 1, . . . , vT ), the (normalized) expected utility of optionkisU (k)(v) =
29

PT
t=1 pt βt vt χ(k) t −µ (k).Define the transformed “item values”v ′ t ≡p tβtvt fort∈[T]. Then
U (k)(v) = P t v′ tχ(k) t −µ (k), which is exactly the utility of anadditivebuyer in a multi-item
problem who receives (possibly randomized) quantitiesχ(k) t of each itemtand paysµ (k). In
particular: allowingχ (k) ∈[0,1] T corresponds to allowing randomized bundles (the full class
M), restrictingχ (k) ∈ {0,1}T corresponds to deterministic bundles (the classM bin), and
imposing additive pricingµ(χ) =ρ 0 + P t ptχtρt corresponds to item pricing (with an entry
fee) for an additive buyer (the classMadd).
Fixλ≥0. For any menu option(χ, µ), the Lagrangian objective contributes
µ−λ
TX
t=1
ptχt =µ−
TX
t=1
ct χt,wherec t ≡λp t.
ThusΠ M(λ)is exactly the optimal expected profit in the additive multi-item problem in
which serving “item”tincurs (expected) costc t per unit ofχ t. Equivalently, define a shifted
payment˜µ≡µ− P t ctχt and shifted item values˜vt ≡v ′ t −c t. Then buyer utility is unchanged:
X
t
v′ tχt −µ= X
t
˜vtχt −˜µ,
and seller profit becomes exactly the shifted revenue˜µ. Hence maximizing profit with costs
{ct}is isomorphic to revenue maximization for an additive buyer with (shifted) values{˜vt};
shifting by constants preserves independence/correlation structure across items.
Known approximation results for additive single-buyer multi-item mechanism design there-
fore apply: Babaioff et al. (2020) show that when valuations for items are drawn independently
(from a product distribution), the better of selling items separately (per-item pricing) and sell-
ing the grand bundle achieves a universal constant-factor approximation to optimal revenue.
In particular, the optimal revenue is at most six times the revenue from the better of these two
mechanisms. When valuations are arbitrarily correlated, Chawla, Teng, and Tzamos (2019)
show that selling items separately guarantees anO(logT)approximation.
Inoursetting, bothitempricingandgrand-bundlepricingarecontainedinM add (asspecial
30

cases of additive pricing menus). Separate good pricing corresponds to settingρ0 = 0in the
class of mechanisms with binary allocations and additive pricings, and grand-bundle pricing
corresponds to settingρ t = 0∀t. Thus, the revenue achievable under binary allocations and
additive pricings inherits the same constant-factor andO(logT)approximation guarantees.
In particular, there exists a factorcsuch that, for everyλ≥0,
ΠM(λ)≤cΠ Madd(λ).(8)
BecauseM add (andM bin)isclosedunderconvexcombinations, thecurveq7→OPT Madd(q)
is concave by the same argument as Proposition (2). Fix anyq∈(0,1)and choose any
subgradientλ q ∈∂OPT Madd(q). Concavity implies thatqmaximizes the functionq ′ 7→
OPTMadd(q′)−λ qq′, and consequently
ΠMadd(λq) = OPT Madd(q)−λ qq.(9)
Combining (7) (withλ=λ q), (8), and (9) gives
OPTM(q)≤Π M(λq) +λ qq≤cΠ Madd(λq) +λ qq≤c

ΠMadd(λq) +λ qq

=cOPT Madd(q),
where the penultimate inequality usesc≥1. Thus, for everyq∈[0,1],M add achieves ac-
approximationto theex-ante constrainedoptimum inM(constantcunderindependent values
andc=O(logT)under arbitrary correlations). SinceM add ⊆ Mbin, the same guarantee holds
forM bin as well.
Proof of Proposition 11.Results such as Lee and Valiant (2016) show that polynomial-
time global optimization is possible for broad classes of non-convex objectives in both the
number of dimensionsTand the tolerance parameter1/ϵ. To establish the stated result,
it therefore suffices to show that a single step of such an optimization routine—namely, the
31

evaluation of the objective and the constraint—can be carried out inO(T)operations.
Because the objective and the constraint are expectations over the advertiser’s valuation
distribution, we approximate them using sample averages. Replacing exact expectations with
sample averages increases the number of iterations required to reach a given tolerance level,
but does not affect the complexity of each step with respect toT. Thus, it remains to show
that, for any given sample of the advertiser’s valuation vector, the optimal bundle can be
identified inO(T)time.
Letσbe a binary vector (excluding the all-zero vector) representing a bundle of segments,
whereσ t = 1indicates inclusion of segmentt. The advertiser’s utility from bundleσis
U(σ) =−ρ 0 + P t ptσt(vt −ρ t). We determine the optimal bundle by examining each segment
tas follows:
Segments with large surplus.Ifv t > ρt + ρ0 pt for some segmentt, i.e.,−ρ 0 +p t(vt −ρ t)>0,
then the bundle containing only segmenttyields positive utility. In addition, addingtto any
other bundle strictly increases utility, so the optimal bundle must includet.
Segments with negative surplus.Ifv t < ρt, then addingtdecreases utility in any bundle.
Therefore, the optimal bundle does not contain such segments.
Intermediate segments.Ifρ t < vt < ρt + ρ0 pt , then segmenttis not profitable on its own,
but if another segment with large surplus is already included, addingtincreases utility. In
this case, the optimal bundle must include both the large-surplus segment andt.
Residual case.If no segment satisfies the large-surplus condition, the only candidate
optimal bundle is the set of all segment withvt > ρt. Denote this bundle byσ. If−ρ 0 +
P
t ptσt(vt −ρ t)>0, thenσis optimal; otherwise, the null bundle is optimal.
This procedure requires only a single pass through theTsegments, and thus runs inO(T)
time. Combined with the guarantees of derivative-free optimization, this establishes that the
single-advertiser problem with binary allocations and additive pricings can be solved in time
polynomial inTand1/ϵ.
32

Web Appendix F: Estimating Primitives
F.1 Slot Effects
Click-through rate (CTR) in the model is multiplicatively separable into slot, segment, and
advertiser effects:
CTRast =α sβtγa.
Following Athey and Nekipelov (2011), the slot effects{αs}and advertiser effects{γ a}are
identified from variation in realized positions across advertisers over time. Because our CTR
data do not break out clicks by segment, we setβt = 1for allt. This normalization ap-
plies uniformly across all counterfactual mechanisms and therefore preserves the fairness of
comparisons.
Lety asd denote the observed CTR for advertiserain slotson dayd, and letn asd denote
the corresponding number of impressions. We estimate the multiplicative CTR model using
Poisson quasi-maximum likelihood, specifying the conditional mean as
E[yasd] =α sγa = exp(logα s + logγ a).
Becausey asd is a rate estimated fromnasd impressions, we weight observations bynasd in
thePoissonQMLE.Weestimatethemodelusingslotandadvertiserfixedeffects, with{logα s}
treated as slot fixed effects and{logγa}treated as advertiser fixed effects. Consistent with
the structure of the mechanism, we impose the monotonicity constraintα1 ≥α 2 ≥ · · · ≥αS
during estimation.
The specification achieves a McFadden pseudo-R2 of0.864, indicating that the assumptions
of multiplicative separability and monotonicity of slot effects provide a good approximation to
the CTR data. The resulting slot effects{αs}are used both in the estimation of distribution
of advertiser valuations below and in counterfactual mechanism comparisons.
33

F.2 Distribution of Advertiser Valuations
Because GSP is not truth-telling, advertiser bids do not equal valuations. Nevertheless, Edel-
man, Ostrovsky, and Schwarz (2007) and Varian (2007) show that equilibrium bidding behav-
ior in GSP, which they refer to as envy-free equilibria, imposes sharp inequality constraints
that bound advertiser valuations. Let advertisers be ordered by bid-rank (ba ×γ a) so that
advertisera s occupies slots. The envy-free conditions require:
γasvas ≥ γas+1bas+1αs −γ as+2bas+2αs+1 αs −α s+1 ≥γ as+1vas+1.
The middle term defines theincremental cost per click(ICC) of moving from slots+ 1to slot
s:
ICC s,s+1 = γas+1bas+1αs −γ as+2bas+2αs+1
αs −α s+1
.
In equilibrium these ICCs must satisfy the monotonicity condition
ICC s,s+1 ≥ICC s+1,s+2.
Becauseobservedbidsmayviolatemonotonicity, wefollowVarian(2007)andcomputeweighted
ICCs{ICC d∗ s,s+1}that minimize the weighted deviation from monotonicity:
ICC d s,s+1 = γas+1bas+1αsds −γ as+2bas+2αs+1ds+1 αsds −α s+1ds+1 ,
with weightsdchosen to minimize P s(1−d 2 s)subject to the ICCs being monotone. The
optimal weightsd ∗ yield a monotone sequence of ICCs.
These monotone ICCs deliver valuation bounds:
γasvas ∈

ICC d∗ s,s+1, ICCd∗ s−1,s  , s= 2, . . . , S−1.
For slot1, the lower bound is identified; for the upper bound we setv= 2b max, whereb max
34

is the largest bid observed. For slotS, the upper bound is identified; the lower bound requires
the highest losing bid, which we do not observe, so we conservatively set it to zero.
Thus each advertiser in each auction contributes an interval(L, U]containing the true
valuationv at. To estimate the valuation distributionFat, we pool the intervals across auctions
and compute the non-parametric maximum likelihood estimator using the Turnbull estimator
(Turnbull 1976). Because all auctions in our sample belong to a single product category, we
assume that advertisers are ex ante symmetric within an segment, and that valuations are
independent and identically distributed draws from a common distributionFt. This symmetry
assumption permits pooling interval observations across advertisers and auctions to recover
a single valuation distribution for each segment. We implement the estimator using the EM
algorithm, which yields a piecewise-uniform CDF with data-driven support.
Figure 9 plots estimated valuation densities for three randomly sampled segments, illus-
trating substantial heterogeneity in valuation levels and dispersion. These estimated valuation
distributions, together with the CTR primitives above, are used in the counterfactual mech-
anism comparisons in Section 6.3.
Figure 9:Distribution of valuations for randomly sampled segments
35
