---
title: Algorithmic Collusion of Pricing and Advertising on E-commerce Platforms
url: https://arxiv.org/abs/2508.08325
category: consumer-behavior
subcategory: empirical
date: 2025-08
venue: ''
authors:
- Hangcheng Zhao
- Ron Berman
source: arxiv
pdf_url: https://arxiv.org/pdf/2508.08325
pages: 52
chars: 105295
fetched_at: '2026-11-08T13:05:33+00:00'
kb_version: 1
---

# Algorithmic Collusion of Pricing and Advertising on E-commerce Platforms

Algorithmic Collusion of Pricing and Advertising on E-commerce
Platforms∗
Hangcheng Zhao† Ron Berman‡
October 2025
∗We thank Eric Bradlow, Pinar Yildirim, Raju Jagmohan Singh, Raghu Iyengar, Leon Musolff, Christophe Van
den Bulte, Soheil Ghili, Sylvia Hristakeva, Omid Rafieian, Tianxin Zou, Kanishka Misra, Sridhar Moorthy, Tat
Chan, Yufeng Huang, Ilya Morozov, and participants at the 4th Annual AI in Management Conference, 14th Annual
Theory and Practice of Marketing Conference, 2nd FTC Conference on Marketing and Public Policy, 2025 Workshop
on Platform Analytics, 35th Annual POMS Conference, 2025 ASA Marketing Section Doctoral Dissertation Research
Award Session, and Conference on Frontiers in Machine Learning and Economics for their helpful comments. All
errors are our own.
†Rutgers Business School. hangcheng.zhao@rutgers.edu
‡The Wharton School of the University of Pennsylvania. ronber@wharton.upenn.edu
arXiv:2508.08325v2  [econ.GN]  31 Oct 2025

Algorithmic Collusion of Pricing and Advertising on E-commerce Platforms
Abstract
When online sellers use AI learning algorithms to automatically compete on e-commerce
platforms, there is concern that they will learn to coordinate on higher than competitive prices.
However, this concern was primarily raised in single-dimension price competition. We investigate
whether this prediction holds when sellers make pricing and advertising decisions together,
i.e., two-dimensional decisions. We analyze competition in multi-agent reinforcement learning,
and use a large-scale dataset from Amazon.com to provide empirical evidence. We show that
when consumers have high search costs, learning algorithms can coordinate on prices lower
than competitive prices, facilitating a win-win-win for consumers, sellers, and platforms. This
occurs because algorithms learn to coordinate on lower advertising bids, which lower advertising
costs, leading to lower prices and enlarging demand on the platform. We also show that our
results generalize to any learning algorithm that uses exploration of price and advertising bids.
Consistent with our predictions, an empirical analysis shows that price levels exhibit a negative
interaction between estimated consumer search costs and algorithm usage index. We analyze the
platform’s strategic response and find that reserve price adjustments will not increase platform
profits, but commission adjustments will, while maintaining the beneficial outcomes for both
sellers and consumers.
Keywords: Artificial Intelligence, Algorithmic Collusion, Platforms, Advertising, Sponsored
Product Ads, Reinforcement Learning, Q-learning, Consumer Search.
1 Introduction
Reinforcement learning (RL) algorithms have been successfully applied to marketing applications
including automated advertising bidding (Cai et al. 2017, Wu et al. 2018), pricing (Dub´ e and Misra
2023, Misra et al. 2019, Smith et al. 2023), personalized recommendations and more (Schwartz
et al. 2017, Liu 2023, Rafieian 2023). These algorithms are very suitable for learning in dynamic
environments without much prior information, because they can be model-free and learn the reward
structure as they explore the outcomes from their actions. The RL algorithms do not have to know
how ad auctions operate or how demand responds to prices, or any other a-priori details about
the economic environment in order to learn. In practice, multiple firms publicize that they use
reinforcement learning to optimize pricing and advertising strategies in real time simultaneously. 1
1For example, Alibaba implemented deep reinforcement learning for large-scale dynamic pricing (Liu et al.
2019). Feedvisor promotes their “continuous real-time optimizations for both pricing and advertising allowing
to drive profitable growth”(https://feedvisor.com/feedvisors-integrated-solution/, accessed Oct 20, 2025),
while Profasee’s “Price and Ad Optimizers work together to revolutionize the profit potential of your Amazon
store.”(https://profasee.com/all-in-optimizer/, accessed Oct 20, 2025).
1

In recent research that used simulations to analyze competitive pricing using reinforcement-
learning, Calvano et al. (2020), Hansen et al. (2021) and Johnson et al. (2023) find that these
algorithms can learn to tacitly collude on setting prices that are higher than competitive prices
(even without direct communication), which is harmful to consumers. The issue became a major
policy worry, and the FTC even stated that “Price fixing by algorithm is still price fixing.” 2
In this paper, we ask whether algorithmic decision making by competing firms is necessarily
detrimental to consumers, or whether there are cases when consumers, as well as firms and an
intermediating platform, might benefit from them. One reason for asking this question is that
most of the analyses of algorithmic decision making often focused on one-dimensional learning such
as learning to price, or to advertise, but in reality, firms often need to make multi-dimensional
decisions. Another reason we focus on this question is that for online platforms (but also for
other settings such as grocery chains and media markets), their revenue streams combine sales
commissions or another profit margin on sales, as well as ad revenue, and as a result the platform
has some flexibility in which stream to emphasize more, which in turn affects what algorithms learn.
Of course, there are also many other cases where algorithmic decision making can help consumers. 3
However, we are interested in exactly those cases that were previously identified as harmful to
consumers.
Our analysis combines two approaches—we use an analytical model to analyze a benchmark
case of pure competition (with complete information where algorithmic pricing and bidding are
not needed) to show the effect of ad bids and search costs. We then use an extensive empirical
simulation to analyze algorithmic pricing and bidding using RL to show that prices and bids could
be lower when algorithms learn to coordinate in a setting with high consumer search cost. We also
estimate search costs and algorithmic pricing adoption using a large-scale dataset from Amazon.com
and provide evidence consistent with prices being lower in markets with higher consumer search
cost and higher algorithm usage. To make our results comparable to previous research, we analyze
a specific, yet common, RL algorithm called Q-learning (described in Section 4). We later discuss
the generalizability of our findings to other types of learning algorithms.
2Recently, the Federal Trade Commission and Department of Justice are taking different actions
to fight algorithmic collusion. See detail athttps://www.ftc.gov/business-guidance/blog/2024/03/
price-fixing-algorithm-still-price-fixing.
3Well-known examples are recommendation systems and other algorithms that help match consumers and products
(or consumers with other consumers) (Mullainathan and Spiess 2017, Mikl´ os-Thal and Tucker 2019).
2

In Section 3, we motivate our model through providing details of an online platform (such as
Amazon.com) where consumers come to search for products to buy, and sellers come to sell their
products. The platform displays ordered links to consumers, with the prominent sponsored links
sold through an ad auction, while the other (organic) links are ranked based on product features
(price, rating and other features). This setting is quite common in e-commerce and includes large
companies such as eBay and Expedia. The sellers on the platform set prices for their products and
also decide how much to bid for displaying their product in the sponsored position. When consumers
search for a keyword, they see an ordered list of links, and traverse it until they find a product to
buy or stop searching. We assume that the purchase decisions follow a standard choice model, with
consumers having heterogeneous consideration set sizes, which are a result of heterogeneous search
costs. We later show evidence that search costs are indeed high and heterogeneous on Amazon.com,
lending credibility to this assumption.
In Section 4, we compare two sellers who use reinforcement-learning algorithms to price and bid
to the case of pure competition without learning. Under pure competition (without RL), search
costs increase prices in equilibrium, because the sponsored positions become more valuable. This
in turn increases equilibrium bids on ads, leading to increased marginal costs and higher prices
(Armstrong and Zhou 2011). Our first novel finding in Section 4, where we analyze multi-agent
reinforcement learning, is that the algorithms converge on prices lower than competitive prices. In
other words, Q-learning can result in coordinated pricing, but the algorithms coordinate on lower
prices that help consumers. This is in stark contrast to findings from previous research (Calvano
et al. 2020, Johnson et al. 2023), where it was shown that pricing algorithms learn to collude on
higher prices.
Our insight comes from the role of advertising. If the algorithms could exchange information
and coordinate on the best outcome for them, they would have decided to bid zero on the ads and
evenly split the market. Because the ads are a cost for the sellers, it is best for them to agree to
lower these costs. This is in contrast to prices, where it is beneficial for both sellers to increase
prices. When search costs are high, the benefit from coordinating on lower bids outweighs the
benefit from coordinating on higher prices, and the equilibrium outcome is better for consumers.
Unlike the case of competing over prices only, when competing on prices and ad bids together, lower
equilibrium prices result in higher seller profit, because total demand on the platform increases, as
3

well as advertising costs decrease.
Tacit coordination by algorithms can also benefit the platform (Section 5) when search costs
are high, because the increase in sales generates more commissions that dominate the decrease in
revenue from advertising. We find that adjusting the ad reserve prices might not be as effective
compared to changing commission rates. This is because increasing the reserve price shifts the
algorithms even further towards coordinating on lower bids, further reducing the advertising rev-
enue. However, by increasing their commission rates, the platforms can recoup some of the lost
advertising revenue due to lower bids.
In Section 6, we analyze data from more than 2,000 product search keywords on Amazon.com,
yielding more than 1 million observations per day for 2 million products. Our goal is to see if there
is evidence that indeed prices decrease for markets with higher search costs and higher adoption of
algorithmic pricing. We estimate the consumer search costs using the variation in observed product
rankings and their sales over time. 4 We estimate an algorithm usage index for different product
categories using the correlation patterns in prices set by sellers over time (Chen et al. 2016). We
find a negative interaction on price levels between estimated search costs and algorithmic pricing
adoption, consistent with our model’s prediction that prices are lower in markets with higher
adoption of algorithmic pricing and higher consumer search costs.
To summarize, unlike much of the past research, we find that consumers as well as the platform
might benefit from tacit coordination by algorithms. These findings can be useful for sellers who
are concerned about adopting algorithmic pricing with multi-dimensional decision-making. They
can also help platforms decide if they should encourage sellers to use algorithmic pricing and
bidding, and even whether they should offer these algorithms themselves. Finally, our results
provide good news for consumers because lower prices by algorithms increase consumer welfare.
From a regulatory perspective, this area of inquiry is currently of high relevance for modern digital
platforms, making our findings extremely relevant.
4We use moment conditions (Lam 2021, Yu 2024) to address the simultaneity issue between the ranking of a
product on a page and its sales. If a product is ranked higher it will likely have more sales, but in turn, having more
sales might rank it higher.
4

2 Contribution and Related Work
Our research contributes to a growing stream of literature that examines how algorithms affect
competition through pricing. In this stream, a central concern is that reinforcement learning or
related heuristics may lead to tacit collusion and supra-competitive prices. For example, Calvano
et al. (2020) and Hansen et al. (2021) demonstrate for oligopolies that algorithms such as Q-learning
and multi-armed bandits can lead to equilibrium prices above competitive levels. Johnson et al.
(2023) investigate platforms’ ability to steer demand towards lower-priced sellers and find that
algorithms result in supra-competitive prices in the absence of non-neutral platform intervention.
The phenomenon of algorithmic collusion is also documented in scenarios where algorithms make
sequential decisions (Klein 2021) and where Q-learning algorithms compete with simple heuristic
algorithms (Wang et al. 2023). By contrast, despite concerns expressed by policymakers, Mikl´ os-
Thal and Tucker (2019) find that better forecasting algorithms can lead to lower prices and higher
consumer surplus. To uncover the mechanism behind such algorithmic collusion, Asker et al. (2022)
study the effect of algorithm design on collusion. Similarly, Banchio and Skrzypacz (2022) find that
synchronous algorithms are less likely to converge on collusive outcomes. Banchio and Mantegazza
(2022) reveal that spontaneous coupling can sustain collusion in prices and market shares. Our
research adds to these prior work by considering multi-dimensional decisions, and by analyzing the
cost aspect of the decision making. We show that collusion does not always lead to predictable
outcomes in one direction for consumers, but can actually benefit (or harm) consumers depending
on which force (cost or revenue) is stronger given consumer search heterogeneity.
On the empirical side, Musolff (2022) documents that repricing algorithms follow Edgeworth
cycles to effectively coax competitors into raising their prices, which decreases competition. Brown
and MacKay (2021) find that algorithms allow for more frequent price changes, generate price
dispersion, and increase price levels. Assad et al. (2024) find that algorithmic-pricing software
significantly increased the margin in Germany’s retail gasoline market. Calder-Wang and Kim
(2023) find that algorithms set more responsive prices, leading to higher rents and lower occupancy
in the U.S. multifamily rental housing market. Our research adds further evidence by considering
the effects of consumer heterogeneity in search costs which affects how valuable sponsored ads are.
We find empirical evidence that prices might be lower when algorithms are used to price and bid
5

and consumer search costs are high, compared to a case of full-information competition. This
finding provides a more nuanced view of the potential impact of algorithmic pricing when other
forces are at play.
Substantively, our paper builds upon research in search advertising and sponsored ads (Edelman
et al. 2007, Varian 2007, Sayedi et al. 2018, Choi and Mela 2019, Long et al. 2022). These works
typically assume that the value of winning an ad auction is exogenously given. Athey and Ellison
(2011) introduced consumer search, which endogenizes advertisers’ valuation. Chen and He (2011),
Kang (2021) incorporated the pricing decision into the sponsored ads auction. Armstrong and
Zhou (2011) demonstrated how higher search costs raise bids, ad expenditures, and ultimately
prices — an effect closely related to the mechanisms we examine. Our research builds on these
(mostly theoretical) insights by considering the impact of learning algorithms in these settings,
and by providing empirical evidence for these predictions. In these settings, platform algorithms
that rank products by price, rating, or advertising bids influence both seller profits and consumer
surplus (Lam 2021, Lee and Musolff 2021, Farronato et al. 2023). In these works, classic models of
consumer search (Weitzman 1979, Ursu 2018, Honka and Chintagunta 2017, Morozov et al. 2021)
are often used and emphasize heterogeneity in search costs, which we find have a substantial impact
on the findings in our work.
3 Institutional Background and Model Setup
3.1 Institutional Setting
We analyze platforms similar to Amazon.com that list and sell products from third-party sellers. In
our main analysis, if the platform directly sells a product to consumers, we assume that consumers
will treat it as another seller. We discuss self-preferencing (where Amazon might promote its own
products more) in the Conclusion.
We consider consumers who start by typing a keyword into the search box. The platform
then lists relevant products with both organic and sponsored listings. We focus on the default
“Featured” ranking, where the platform ranks organic products based on multiple factors like sales
performance, customer ratings, and conversion histories. 5 We assume consumers consider products
5Consumers can also choose other sorting options, including “Price: Low to High”, “Price: High to Low”, “Avg.
6

sequentially in the order displayed to them. They have heterogeneous search costs and might stop
their search without considering later products on the search results page. Consumers who have
high search costs (e.g., impatient), generally visit only the top links (i.e., mostly sponsored) and
only consider buying the products that appear there. 6 By contrast, consumers with low search
costs or frictions (e.g., patient), will consider also organic products which appear lower on the list.
Sponsored products are distinguished from organic by the label “Sponsored,” and a product
can appear in both sponsored and organic positions. Figure 1 and Web Appendix Figure W A2
present examples.
Figure 1: Example of First Two Rows of an Amazon Search Result Page with 60 Products
First two rows of the search results for “humidifiers for bedroom.” Orange rectangles emphasize
sponsored listings that link to products by sellers who won the ad position in an auction.
We focus on Sponsored Product Ads format because they account for about 78% of total seller
ad spend on Amazon.com. 7 and appear prominently on the search result page.
Customer Review”, “Newest Arrivals”, and “Best Sellers”.
6For example, Farronato et al. (2025) find that a median consumer had a consideration set of 15 products and
only 23.3% of consumers considered a product located in the middle of the results page.
7Statistic fromJungle Scout. Seehttps://www.junglescout.com/blog/amazon-sponsored-product-ads/, Ac-
7

Amazon uses real-time ad auctions to determine which ads to display and their order. The
ranking is based on a combination of the advertisers’ bids and the ads’ relevance. 8 Sellers are
motivated to bid for sponsored positions to attract more consumer attention earlier in their search.
Sellers bid for each keyword based on their willingness to pay per click (CPC) and pay only when
a consumer clicks their ad. 9
Sellers also pay the platform a share of the revenue from units sold as commission. 10 Other fees
that Amazon can collect from sellers (e.g., shipping and return administration), are included in the
manufacturing (marginal), as they do not alter search result rankings nor consumer search.
Sellers need to pick product prices and if, and how much, to bid for sponsored ads to maximize
profits. They face two trade-offs regarding prices. First, they want to avoid strong price competition
with other sellers and prefer higher equilibrium prices. Second, they also want the prices not to
be too high, because otherwise consumers might choose to buy from another website (an outside
option good). Regarding ad bids, the more sellers bid, the higher their chances are of winning the
sponsored link and reaching consumers who only consider the top positions. However, they will
want to avoid competing too aggressively on bids as they incur costs that lower profits.
In our main analysis we do not consider the platform’s incentives to change commission fees or
ad auction reserve prices, and discuss these in Section 5.
Because of these two-dimensional tradeoffs for bids and prices, when sellers use profit-maximizing
algorithms to guide pricing and bidding decisions, it is unclear whether equilibrium prices and bids
will be high or low. On the one hand, sellers want higher price to increase profits, which increase
the valuation of winning the sponsored positions leading to higher bids. On the other hand, they
would like to bid lower to reduce their marginal costs, leading to lower prices. These two opposing
forces are the main factor that impacts the results in our analysis using the model we introduce.
A-priori it isn’t obvious which force will prevail.
cessed June 8, 2024.
8Amazon Ads, How does bidding work for Sponsored Products?https://advertising.amazon.com/library/
videos/campaign-bidding-sponsored-products.
9Amazon uses generalized second-price auctions, where for each consumer click on an ad in ther-th sponsored
position, the seller pays Amazon an amount equal to the “realized” bid of the (r+ 1)-th highest bidder, which is a
relevance adjusted bid.
10Amazon discloses that commission rates differ for various product categories, typically being 15%. Seehttps:
//sell.amazon.com/pricing#referral-fees, accessed June 8, 2024.
8

3.2 Model Setup
Our model has three player types:n≥2sellers, who sell one differentiated product on a retail
platform, and a unit mass ofconsumerswho choose between purchasing from either one of these
sellers on the platform, or an outside good. We analyze this model analytically and also use it for
empirical simulation and estimation on data.
PlatformThe platform determines listing rankings on the search results page. Sponsored po-
sitions are determined by ad auctions; organic positions are determined using a recommendation
algorithm. We first consider a simplified case where two sellers compete and there is one sponsored
position followed by two organic listings. The sponsored listing is the first product consumers see
and is awarded to the winning ad-auction bidder. Figure W A1 in the Web Appendix provides an
illustration of the results page for the simplified model.
We assume each search keyword is its own independent market, hence we can focus on one
representative keyword only. Each seller has a constant marginal production costc i >0, and pays
the platform a commission rateτ∈(0,1) of revenues. Sellers interact repeatedly over time and in
each periodt= 0,1, . . ., they simultaneously decide on the bidbt i ≥0 to submit in the auction and
the pricep t i ≥0 to set for its product.
The platform shows the seller with the highestrealized bid ˜bt i in the sponsored position, when
the bids submitted by sellers areb t i. We approximate the impact of the ads’ relevance score and
the uncertainty sellers face when deciding their bids, by assuming that the realized bid ˜bt i follows a
log-normal distribution: log( ˜bt i)∼ N(log(bt i), σi). We use a first-price auction for tractability and
to avoid scenarios with multiple equilibria. While this differs from the generalized second price
auction that Amazon.com uses, we do not expect this difference to be crucial for the main insights
from our analysis. 11 We provide more details in Section 3.3.
ConsumersIn periodta unit mass of consumers who wish to buy at most one product perform
a search. They spend one period in the market and then exit and are replaced by a new cohort.
11Generalized second-price auctions and first-price auctions have similar theoretical strategic incentives and al-
gorithm performance. Both are non-truthful, and algorithms behave similarly and learn to collude on lower bids
(Rovigatti et al. 2023, Banchio and Skrzypacz 2022), unlike in non-generalized second-price auctions. Our assump-
tions are similar to those imposed in Yu (2024).
9

A representative consumer who buys productiin periodtobtains utilityu t i =a i −p t i +ϵ i, where
ai capture vertical differentiation andp t i is the product’s price. The outside good is indexed by 0,
with utilityu t 0 =ϵ 0. We assume thatϵ 0 and eachϵ i are i.i.d. type-I extreme value with common
scale parameterµ >0. 12 If productiis in the consideration setN t in timet, its demand is:
si

pt = exp
 ai−pt i
µ

P
j∈N t exp
 aj −pt j
µ

+ 1
(1)
wherep t is the vector of prices of products in the consumer’s consideration set.
Consumers search for products in the order displayed to them, and have heterogeneous search
costs. High search costs can lead them to stop their search early and consider only a subset of all
products on the page. For the simplified model we follow Armstrong and Zhou (2011) and assume
that there are two segments of consumers. A fractionθof consumers has high search costs and
considers only the product in the sponsored position. The remaining 1−θfraction of consumers
considers the products in all positions. For example, if productsiandjare presented in order
{j, i}on the search results page, then the high search cost segment considers onlyj, and the other
segment has a consideration set of{j, i}. If a product appears in both the sponsored and an organic
position, we assume that consumers consider it as one product from the organic link. 13 The search
process represented by the two segments can be viewed as the outcome of consumers who perform
sequential optimal search and decide to stop when the expected value from continuing is below their
search cost, with a heterogeneous distribution of search costs (Weitzman 1979). Appendix W A.3
provides details about the relationship between the simplified model and an optimal search process.
Endogenizingθwould not change our main insights. We also consider a specification where the
ranking affects consumer utility directly in Web Appendix W A.3.3 and find similar results.
We denote bys i

pt i  the market share of productiamong consumers who only consider the
top position when productiappears in the top position, and denote the market share of product
iamong consumers considering both sponsored and organic positions bys i

pt i, pt j

. Taking the
12The parameterµis also an index of horizontal differentiation, and the case of substitutes is obtained in the limit
whenµ→0.
13Web Appendix W A.3.2 describes a sensitivity analysis where a fraction of consumers who consider all products
also click the sponsored link.
10

outside option into account, the market shares of productiare:
si

pt i  = exp
 ai−pt i
µ

exp
 ai−pt i
µ

+ 1
si

pt i, pt j  = exp
 ai−pt i
µ

exp
 ai−pt i
µ

+ exp
 aj −pt j
µ

+ 1
SellersIn the simplified model, we assume that the two sellers are ex-ante symmetric in their
quality and production costs (a t i =a t j andc t i =c t j). Hence, the platform will treat the sellers
identically for organic rankings and randomize the order of display in the two organic positions.
Asymmetric sellers are analyzed in Appendix A.5.2. Our empirical analysis allows for multiple
sellers who can be differentiated and asymmetric. The sellers have a common discount factor
δ∈(0,1), and maximize the cumulative discounted profit:
∞X
t=0
δtπt i(pt,b t) (2)
The one-period profit for selleriin periodt, denoted asπ t i(pt,b t), is given by:
πt i(pt,b t) =θ·Pr( ˜bt i > ˜bt j)·s i  pt i  ·  (1−τ)·p t i −c i  −γ i ·E h ˜bt i | ˜bt i > ˜bt j i
+ (1−θ)·s i

pt i, pt j  ·  (1−τ)·p t i −c i  (3)
whereb t is the vector of bids submitted by all sellers in periodt. The first term represents the profit
from the sponsored position and is affected by the share of “impatient” consumersθ, the chance of
winning the ad auction Pr( ˜bt i > ˜bt j), the market share of the product (vs. the outside good)s i  pt i 
and the profit per sale, which depends on the profit margin and cost of ads. The inverse conversion
rate,γ i, indicates the number of clicks needed for a sale and is assumed common knowledge. The
commission rate charged by the platform is denoted asτ. Appendix A.1 derives the expressions for
the chance of winning the ad auction Pr( ˜bt i > ˜bt j) and the expected ad cost conditional on winning
the auction and the competitor’s bidE
h ˜bt i | ˜bt i > ˜bt j i . The second term is the profit from consumers
who consider more than just the sponsored product.
11

3.3 Full Competition Benchmark
We first analyze a full competition version of the model where the sellers have complete information
and do not need to learn about their environment. This setting forms the benchmark which we use
to compare to the algorithmic case in repeated games.
We consider two scenarios:
1.Full competition with pricing and bidding: Both sellers have complete information about
model parameters and consumer behavior. They compete by setting prices and bids simulta-
neously. The equilibrium price and bid are denotedp N andb N , respectively.
2.Pricing without bidding: In this scenario sellers compete only on prices without advertising.
Consumer preferences remain the same, withθrepresenting the fraction of consumers who
focus only on the first position. Each seller’s probability of being displayed in the first position
is 1 2 without an auction. We denote the equilibrium price asp oN ,14 and each seller solves:
max
pi
πi(p) =

θ· 1 2 ·s i (pi) + (1−θ)·s i (pi, pj)  ·((1−τ)·p i −c i) (4)
We present the equilibrium prices in Figure 2a and the bids in Figure 2b. The case without
advertising has zero bids.
The following lemma, proven in Appendix A.2, shows that when sellers bid on advertising,
equilibrium prices are higher:
Lemma 1.The equilibrium price in competition with advertising bids is always greater than or equal
to the equilibrium price without advertising:pN ≥p oN . The equilibrium price without advertising
is also increasing inθ.
The intuition is that ads increase the marginal cost and drive up prices. Whenθ= 0 and there
are no costly ads, the prices in both models coincide. Equilibrium prices increase with the fraction
of consumers who only consider the first positionθ. A higherθimplies the seller competes more
often only with the outside option (and not with another seller), which allows them to charge a
14Here,Nstands for the Nash-Bertrand equilibrium, andoindicates the scenario with pricing competition only,
but without advertising.
12

Figure 2: Equilibrium Prices and Bids in One-Shot Game
(a) Prices
 (b) Bids
Panels (a) and (b) show the equilibrium prices and bids as a function ofθunder different scenarios,
respectively. The dashed gray line, and black solid line represent the benchmark equilibrium price
poN (or bidb oN ), and the Nash-Bertrand equilibrium pricep N (or bidb N ), respectively. For this
example, we set the parameters asa i =a j = 2,c i =c j = 1, andµ= 1 4 for comparison with the
results in Calvano et al. (2020). For ads-related parameters, we setσ i =σ j = 0.5 andγ i =γ j = 2.
higher price. Armstrong and Zhou (2011) also similarly show that increased bids to win sponsored
positions increase the sellers’ advertising expenses and, consequently, their total costs. 15
Figure 2(b) shows that equilibrium bidsb N increase withθ. A largerθmeans higher potential
profits from winning the sponsored position, thereby incentivizing sellers to bid more aggressively,
which leads to pricing with advertising to be higher than pricing without.
4 Algorithmic Pricing and Bidding: A Multi-Agent Reinforce-
ment Learning Approach
Turning to our main analysis, we analyze sellers who use reinforcement learning algorithms (specif-
ically, tabular Q-learning) to make pricing and bidding decisions repeatedly. We use numerical
simulations to analyze algorithms that interact in a Multi-Agent setting. First, we introduce the
notation for Q-learning in a stationary single-player environment. Then, we extend from single to
multiple agents.
Single-agent Q-LearningAn algorithm facing an unknown stationary Markov Decision Envi-
ronment with a finite set of statess t ∈ S, a finite set of actionsat ∈ A, wheret= 1,2, . . .denotes
the time periods. Choosinga t in states t yields rewardπ t, and the environment moves to state
15Our proof in Appendix A.2 also explains why the result only requires that bids are non-zero in equilibrium, and
does not depend on the specific auction format.
13

st+1 with probabilityF(π t, st+1 |s t, at). The objective of the algorithm is maximize the expected
present value of the stream of rewardsE
P∞
t=0 δtπ(s t, a(st))  . Q-learning tries to maximize this
objective by iteratively estimating an “action-value function”Q ∗(s, a) whereQ∗(s, a) gives the ex-
pected discounted payoffs of taking actionaat statestoday and then using the optimal policy
functiona ∗(s) in future periods. Thus,
Q∗(s, a) =E[π(s, a)] +δE  V  s′ |s, a 
whereV(s ′ |s, a) is the future optimal value. The optimal policya∗(s) isa ∗(s) = arg maxa∈A Q∗(s, a).
Learning and ExperimentationSinceQ ∗(s, a) is unknown, the Q-Learning algorithm esti-
mates is as follows: Starting with an initial matrixQ 0, at timetand in states, the algorithm
determines the action to take. With a probability 1−ϵ t, the algorithm operates inexploitation
mode, choosing the optimal action according to the current period Q-matrix and states. With
probabilityϵ t, it entersexploration mode, and uniformly randomizes over all available actions. After
choosing the actiona t ins t, the realized payoffπ t and new states ′ are observed. The element of
the Q-matrix corresponding to (s, a) is updated to
Qt+1(s, a) = (1−α)Qt(s, a) +α

πt(s, a) +δmax ˜a∈A Qt

s′,˜a  (5)
whereQ t(s, a) is the previous “un-updated” element of the Q-matrix, andα∈(0,1) is a learning
rate parameter, which captures the extent to which old information is replaced by new information.
The probability of experimentationϵ t isϵ t =e −βt, whereβ >0 is the experimentation parameter. 16
Q-learning has theoretical convergence guarantees only in stationary single-player settings. In
our multi-agent setting, convergence is not guaranteed because each agent continually changes its
strategy by updating its Q-matrix, rendering the environment non-stationary from the other agents’
perspectives. Despite this, in our empirical simulations we always observe convergence.
Extending to Multiple-seller Pricing and Bidding in E-CommerceWe extend prior work
such as Calvano et al. (2020) and Johnson et al. (2023) by incorporating sponsored ads and consumer
16This means that initially the algorithms choose purely random actions, as whent= 0,ϵ t =e 0 = 1. As time
passes, the algorithms take greedy actions more frequently.
14

search to an implementation of Multi-Agent Reinforcement Learning (MARL) as follows:
We first consider a symmetric duopoly (n= 2) with discount factorδ= 0.95. Each agent has
a marginal costc= 1. True demand (unknown a-priori to the algorithms) is given by Equation
(1) with each firm having the same quality componenta i =a j = 2 and scale parameterµ= 1 4 .
We normalize the quality component of the outside option to bea 0 = 0. The one-period profit
is defined as in (3), under the assumption that the demand function remains stationary, and the
agent maximizes the sum of future expected discounted profits. In Section 4.3 we also investigate
the cases of heterogeneous product quality and more than two sellers.
Action SpaceIn each periodt, the action space for each agent is a product of the set of possible
prices and bids, that isa it = (pit, bit). The set of prices is discretized into 15 equally spaced values
within the range [p min −ξ(p max −p min),p max +ξ(p max −p min)].17 The bid set contains 10 equally
spaced elements in the range [0,(1 +ξ)·b max], with the upper bound slightly above the maximum
bid.18
State SpaceIn our primary analysis we assume that sellers observe competitor prices but
only know their own bid. This is consistent with real-world practice: prices on e-commerce plat-
forms are public, and sellers can use automated repricing tools that scrape competitor prices to
adjust their own. However, bid information in sponsored-ad auctions is usually private and not
observable by other sellers. 19 We assume that each agent has a one-period memory, which means
that only the price and bid from the previous period enter the state space. The state space
sit = (pit−1, pjt−1, bit−1), consists of the previous period’s prices set by all agents and the bids set
by the agent itself, resulting in 15 n ×10 elements. In Section 4.3, we also examine an alternative
state spaces it = (pit−1, pjt−1, bit−1, bjt−1) in which sellers observe competitor bids.
Each seller’s algorithm independently maintains and updates its own Q-matrix over time, and
17Here,p min andp max represent the minimum and maximum prices across all scenarios, respectively, for all values
ofθ. The parameterξ >0, set to 0.1, allows prices to extend slightly beyond the maximum and minimum values
to include all possible price ranges in every scenario. In our baseline model, the minimum and maximum values are
1.47 and 2.1, respectively.
18The maximum bidb max is the Nash-Bertrand bidb N , as the monopoly bidb M is zero. In our default parameter
specifications, the maximum possible bid equals 0.24.
19For example, Amazon’s Marketplace allows sellers to publicly observe competing prices through various au-
tomated repricing tools, yet ad auction bids remain private. The FTC has investigated whether Amazon’s ad-
auction system adequately discloses its reserve pricing and auction structure, highlighting concerns about the
opacity of auctions on major e-commerce platforms (seehttps://www.reuters.com/business/retail-consumer/
us-ftc-probes-google-amazon-over-search-advertising-practices-source-says-2025-09-12/, accessed Oct
12, 2025).
15

makes its pricing and bidding decisions at timetconditional on the state space. To initializeQ 0,
and following the fact that at first choices are purely random, each cell is set to the discounted
payoff that would accrue to playeriif opponents randomized their prices and bids uniformly:
Qi,0 (s, ai) =
P
a−i∈An−1 πi (ai, a−i)
(1−δ)|A| n−1 .
The default parameters are set toα= 0.15 andβ= 10 −5 unless specified otherwise.
ConvergenceWe count the simulation round as converged if the induced strategy of each agent
remains unchanged for 100,000 periods. For every period’s Q-matrixQ i,t and possible states, we
identify the action that corresponds to the highest Q-matrix payoff, inducing a policy function in
every period,a i,t(s) = argmax a [Qi,t(s, a)]. We stop the simulation if the policy function remains
constant for each agent for 100,000 periods, or after one billion periods elapsed. Subsequently, we
calculate payoffs and other relevant metrics by averaging over the last 100,000-period horizon. We
repeat the procedure 1000 times for every set of parameters, and report the average across these
1000 iterations for all statistics.
4.1 Reinforcement Learning Simulation Results
Our analysis uses a grid of values ofθfrom zero to one in increments of 0.01. Figure 3 displays
the Q-learning equilibrium prices as a function ofθ, and compares them to the benchmark full
competition results.
The case ofθ= 0 when every consumer considers the products in all positions corresponds
to the case considered in the past literature (Calvano et al. 2020). The market-share weighted
Q-learning equilibrium price is 1.7, which is higher than the Nash-Bertrand price of approximately
1.47, consistent with past results that algorithms learn to set prices higher than competitive when
there is no consumer search cost.
Whenθincreases, for lower values ofθ, Q-learning prices remain above the competitive prices.
However, for higher values ofθ, Q-learning prices can fall below competitive levels. Whether
algorithmic prices fall above or below fully competitive prices depends on the level of search cost
heterogeneity in the market. The higher search costs are, the higher the chances that the algorithms
will converge to lower than competitive prices.
16

Figure 3: Q-learning Prices vs Competition Prices as a Function of Search Costs
The figure shows the Q-learning simulation prices (blue solid) and full competition prices (with
advertising - black solid, without - dashed) as a function of search costsθ.
This finding is one of the major contributions of our paper and is important because it counters
the intuition developed by past research. We show that sponsored ads and consumer search costs
may cause algorithms to converge to prices that are lower than competitive prices. Unlike other
cases of algorithmic collusion, in our case lower prices are beneficial and not harmful to consumers.
We will further illustrate the implications for consumer surplus later in section 4.2.
Intuition: Bid CoordinationFigure 4 presents the average equilibrium bids. The bids affect
the cost of the sellers. At higher values ofθ, average Q-learning bids are significantly lower than
those observed with full competition, suggesting that the algorithms learn to coordinate on lower
bids. This bid coordination reduces the sellers’ advertising expenses, and consequently their overall
costs. Such a reduction in costs leads to lower market prices and higher sellers’ profit.
Past research also identified that Q-learning may result in coordination on lower bids in ad
auctions (Banchio and Mantegazza 2022, Banchio and Skrzypacz 2022, Rovigatti et al. 2023).
However, we observe that this force is in opposite to the force that encourages algorithms to increase
prices. Because these bids may interact with prices, and the level of this interaction depends on
the consumer’s search costs and frictions, whether bids decrease or increase in equilibrium depends
also on pricing and consumer search costs.
17

Figure 4: Q-learning Results: Bids
The figure shows the Q-learning bids (solid blue) and full competition bids (solid black) as a function
ofθ. Without advertising the bid is always zero (dashed).
4.1.1 Generalizability: W ould prices always be lower with multi-agent Q-Learning?
The results we uncovered depended on specific simulation parameter values. We generalize them
and prove that we expect lower than competitive prices for any values of the learning algorithm
parameters. Our analysis also allows us to explain why we expect these results.
In our second primary contribution, we derive a theoretical bound for the fully collusive values
that RL algorithms can potentially reach. We consider two sellers who actively collude on both
prices and bids with complete information. In this scenario, the two sellers maximize their joint
profits by jointly setting prices and bids, acting as if they are a single monopolist. The reason to
perform this analysis (although the scenario is both unrealistic and likely illegal from an anti-trust
perspective) is that it provides an upper bound on the profits of the sellers, and hence we can
predict that the learning agent equilibria will be between the fully competitive and fully collusive
ones. Therefore, if we can prove that for a set of parameter values the collusive prices are lower
than the competitive prices, then we would expect this outcome to also generalize to most cases of
competing RL algorithms.
The equilibrium collusive pricep M and bidb M are defined as: 20
(pM ,b M ) = arg max
(pi,bi)
πi(p,b) +π j(p,b), s.t. p j =p i, bj =b i
20Mstands for monopoly.
18

In equilibrium the two sellers would agree to set their bids to the minimum,bi =b j →0, because
this strategy minimizes advertising costs while maintains the same probability of capturing the
demand from consumers who consider only the first position. Then, the two sellers would decide
on the collusive prices to maximize their aggregate profits given they would both bid as low as
possible.
The algorithmic prices are expected to be between the theoretical collusive and fully competitive
prices. We will show that these prices have a cross-over point for an intermediate value ofθallowing
us to conclude that algorithmic prices will be higher than competitive for low values ofθ, but lower
than competitive prices for high values ofθ.
Figure 5 illustrates these results where we add the collusive outcome to the previous results.
We observe a crossing of the competitive and collusive prices. Comparing the full competition price
pN with the fully collusive pricep M , we find that for low values ofθ,p M >p N , while for high
values ofθ,p M <p N . There is a crossover value of ˜θ, such thatp M (˜θ) =p N (˜θ).
Figure 5: Q-learning and Theoretical Collusion
(a) Prices
 (b) Bids
Panels (a) and (b) show the Q-learning (solid blue) vs competitive (solid black) and collusive (red)
prices and bids as a function ofθ.
These results are summarized in the following lemmas:
Lemma 2.The monopoly pricesp M decrease withθ.
Appendix A.3 provides the detailed proof. Unlike the case of full competition, collusive prices
decrease withθ. Whenθ= 0, all consumers consider both products, and because of the consumer’s
idiosyncratic preferences, the monopolist has two chances to compete with the outside option.
However, whenθ= 1, the monopolist only has one product to sell (because every consumer only
19

considers one product from the first link). In this sense, the outside option becomes stronger when
θ= 1, forcing the monopolist to decrease the price and obtain a lower profit margin.
In the limit whenθ= 1, we prove the following:
Lemma 3.Limiting caseWhenθ= 1, the monopoly pricep M is equal to the competitive price
without advertisingp oN , i.e.,p M =p oN .
This holds because whenθ= 1, consumers in both cases consider only one product, giving both
the competitive seller and monopolist the same objective with zero ad costs.
We combine Lemmas 1, 2 and 3 to arrive at our main result:
Proposition 1.There exists ˜θ∈(0,1)such that forθ < ˜θ,p M >p N , while forθ >˜θ,p M <p N .
We present detailed proof in Section A.4. The proposition guarantees that there is a level of
search cost where the fully collusive prices become lower than the fully competitive one, because
the savings in ad costs dominate the incentive to raise prices. Since algorithmic pricing and bidding
are expected to always be between these two equilibria, we expect our results to generalize to any
dynamic pricing algorithm that also buys advertising.
4.2 Impact on Sellers and Consumers
Figure 6 presents the Q-learning simulation results for sellers’ profit and consumer surplus.21 Figure
6(a) shows that although algorithmic pricing yields lower profit than full collusion, sellers still
benefit compared to full competition.
Consumer surplus decreases with prices. Indeed, Figure 6(b) shows that for highθconsumer
surplus can be higher when using learning algorithms compared to full competition, because the
Q-learning prices are lower than the full competition prices.
The Folk theorem (Fudenberg and Maskin 1986), says that in an infinitely repeated game, any
outcome between cooperative (our full collusion) and competitive (our full competition) in the one-
21Consumer surplus in periodtis
CS

pt =θ· X
j
1{j∈ J1(Γt)} ·µlog

exp
 a−p t j
µ

+ 1

+ (1−θ)·µlog
"X
j
exp
 a−p t j
µ

+ 1
#
=−θ·
X
j
1{j∈ J1(Γt)} ·µlog  1−s j  pt j  −(1−θ)·µlog

1−
X
j
sj

pt
!
(6)
20

Figure 6: Q-learning Results: Sellers’ Profit and Consumer Surplus
(a) Sellers’ Profit
 (b) Consumer Surplus
The left and right figure show the sellers’ profit and consumer surplus, respectively. Solid blue
denotes Q-learning simulation, solid black denotes full competition and solid red full collusion.
Dashed indicates competition without advertising.
shot game can be sustained as a subgame-perfect Nash equilibrium (SPE) when the discount factor
δis high enough. Consequently, we cannot predict whether the algorithmic prices and profits will
be closer to fully collusive or fully competitive, and we again use simulation for the analysis. We
plot the ratios of the difference between the algorithmic and competitive prices and profits, divided
by the difference between the collusive and competitive prices and profits, respectively. That is, we
compute pQ−pN pM −pN and πQ−πN πM −πN . A ratio smaller than 0.5 indicates that the algorithmic outcomes are
closer to competition; otherwise, they are closer to collusion.
Figure 7 shows that whenθ= 0, the algorithms can achieve roughly 60% of the price increase
from the competitive price to the collusive price, and 80% of the profit increase from the com-
petitive profit to the collusive profit. For low values ofθ, we see that the ratios for both price
and profit are higher than 0.5, implying that the algorithms generate outcomes closer to monopoly
(collusion), which is consistent with previous findings about algorithmic collusion (Calvano et al.
2020). However, for high values ofθ, in the range where the algorithms benefit both consumers
and sellers, the algorithms can only achieve profit increases that are roughly between 30% and
40% of the increase from the competitive profit to the collusive profit. This suggests that when
algorithms compete in more than just one dimension of pricing, the algorithmic outcomes are closer
to competition. This is the opposite of cases ofθ= 0, where there are no consumer search costs.
4.3 Additional bidding information, differentiated products, multiple sellers,
and separate algorithms for pricing and bidding
We performed robustness analyses for four scenarios.
21

Figure 7: Q-learning Results: Price and Profit Ratios
(a) Price Ratio
 (b) Sellers’ Profit Ratio
The left and right figure show the ratio statistics for prices and sellers’ profit, respectively. The
parameter specifications are the same as in Figure 2.
In Appendix A.5.1, each seller is allowed to also observe the bids of their competitors. The
motivation is that the platform might experiment with the auction design and disclose winning
bids,22 or that sellers could subscribe to a third-party service that provides bidding information.
The additional information will change the sellers’ bids, and we are interested in how this will affect
the platform’s revenue and the sellers’ profits. Our results show that the additional information
does not impact the platform’s revenue and the sellers’ profits much. The algorithms converge to
almost the same equilibrium but at a slightly higher level of collusion. Hence information-based
methods might not be an effective tool for the platform, and it might want to consider more direct
incentive-based tools to strategically respond to sellers who use algorithmic pricing (Section 5).
Appendices A.5.2 and A.5.3 show robustness for multiple sellers and differentiated sellers. In
these scenarios with multiple heterogeneous sellers, the market’s average prices can still be lower
when algorithm usage is high. Appendix A.5.4 also shows that our results remain robust to allowing
the sellers to run two separate RL algorithms (one for pricing and one for bidding).
5 Strategic Response by the Platform
An important aspect not considered in previous work is that the platform can respond strategically
to equilibrium prices and bids to maximize its own profits. Since the platform’s revenue come
22For example, Google has been experimenting with providing additional information to ad auction participants and
has recently introduced the “minimum bid to win” field for bidders, which provides insight into the bid price needed to
win an individual auction (https://support.google.com/authorizedbuyers/answer/2696468?hl=en&utm_source=
chatgpt.com, accessed Oct 20, 2025)
22

from sale commissions and ad auctions, we consider two incentive-based mechanisms: adjusting
the commission rate and adjusting the ad-auction reserve bids.
Unlike most of the research on ad auctions where adjusting auction reserve prices has a clear
direction of impact, in our setting, due to interactions with pricing competition and demand, the
best direction for the platform’s strategic response are unclear. It depends on market parameters
and the platform’s objectives.
Appendices A.6.1 and A.6.2 consider the scenario where the platform’s objective is to maximize
its own single-period profit which is the sum of sales commissions and ad auction revenue. We also
consider a scenario where the platform’s objective is long-term growth by maximizing a weighted
average of its own profit, sellers’ profit, and consumer surplus in Web Appendix W A.4.3.
We find that increasing the reserve price may not be an effective response for the platform,
whereas adjusting the commission fee is. When the platform does make adjustments, sellers and
consumers can still continue to benefit (compared to the case of full competition), and this is also
the case when the platform’s objective does not only maximizing its own short-term profit.
6 Empirical Evidence from Amazon.com
Our analysis predicts that when search costs are high on the platform, algorithmic pricing and
bidding can benefit consumers and sellers through lowered prices. We collected and analyzed
a large-scale dataset from Amazon.com to look for evidence consistent with this prediction. Our
analysis is correlational and cross sectional, and hence we cannot fully interpret it as causal evidence.
6.1 Data
We collected data from Amazon.com from April 2024 to April 2025. The data includes 2,382 highly
searched keywords across all product categories. Our software submitted a search keyword and then
navigated to the first search result page mimicking normal user behavior. We recorded the ranking
of each product (both sponsored and organic) within the first page. We also recorded other product
information, including its price, product ratings, the number of reviews, whether it is an Amazon
Prime product, and delivery information. To obtain a representative distribution of the sponsored
product listings which vary over time and depending on who wins the ad auctions, we repeated the
23

search for each keyword once every three hours, generating more than 19,000 requests per day.
We obtained additional data fromJungle Scout 23 that included information on the monthly
search volume, suggested pay-per-click bid, and related keywords for each keyword. We also used
Keepa.comwhich provided product information, ratings, reviews, and time listed.
Table W A1 in the Web Appendix presents summary statistics. Figures W A8 and W A9 shows
that most sponsored listings appear near the top search results, consistent with our assumptions.
6.2 Estimation of Search Costs
To test for evidence of decreasing prices when algorithms are used and search costs increase, we
need to estimate consumer search costs in each keyword market. For that we use the variations
in organic and sponsored product positions and daily sales. We first introduce the notations and
assumptions, then describe the identification strategy, and present our estimation results.
Market DefinitionWe assume that each keywordk, is an independent market, and the market
size is its search volume. Using the daily bestseller rank information from Amazon 24 and the Rank
to Sales estimation tool fromJungle Scout, we calculated the imputed daily sales,q jt, for a product
j. The market share of productjin marketkat timet(day) iss jkt = qjt Vk/30 , whereV k is the
monthly search volume of keywordk.
Estimating Consumer Consideration Size DistributionWhen our scraper searches a key-
wordk, it seeNproducts in the first page of the search results. 25 For each keyword, we conduct
a search once every three hours, resulting in a total ofS= 8 searches each day, with each search
indexed bys. LetR st k be the ordered ranking of products in searchsof keywordkin daytand
Jn(Rst k ) is the set of products in the firstnpositions. 26 Consumers face search costs and might
stop at a certain position without continuing to the next position on the search results page. We
assume that there is a unit mass of consumers and that the mass of consumers who stops at the
23One of the largest e-commerce data intelligence companies.
24The daily best sales rank is generally considered a reliable proxy for sales quantity in the literature (Chevalier
and Goolsbee 2003).
25For most of the product categoriesN= 60 andN= 22 for the category ‘Electronics.’
26Among theNdifferent positions, there are both sponsored and organic positions. The number of sponsored
positions is 12 whenN= 60, and 6 whenN= 22.
24

n-th position follows an exponential distribution, i.e.,λ·e −λ·n, whereλis the rate parameter. 27
Consumer Choice ModelConsumeri’s utility of purchasing productjat timetis:
uijt =X ′ jt ·β−α·p jt +γSponsored jt +ξ jt | {z }
δjt
+ϵijt (7)
whereX jt are product characteristics,p jt is the price of productjat timet, andξ jt is an unobserved
demand shock. The idiosyncratic preference shockϵ ijt follows a Type I extreme value distribution.
The mean utility of the outside option, or not buying any product on the first page of the search
results, is normalized to zero. We denote the deterministic part of the utility asδ jt.
As a product may appear in different positions within each search result, each potentially leading
to different sales outcomes, we compute the average choice probability across searches. The market
share of productjin keywordkin daytis
sharejkt = 1 |S| SX s=1 NX n=1 1{j∈J n(Rs kt)} ·(F(λ, n)−F(λ, n−1))· eδjt 1 + P j′∈Jn(Rs kt) eδj′t (8)
Here,F(λ, n)−F(λ, n−1) is the mass of consumers with consideration sizen. The last term is
the standard logit choice probability of productj, conditional on it appearing among the topn
products in a given search resultR s kt.
Estimation and IdentificationWe use the method of moments similar to Lam (2021) and Yu
(2024) with an instrument to account for the endogeneity between the rank of a product and it
sales. The previous period’s organic rank is used as an instrument for the current period’s rank. We
assume that the unobserved quality of a product follows an AR(1) process, i.e.,ξ jt =η jt +ρ·ξ jt−1,
whereξ jt−1 is the lagged unobserved quality andη jt is an uncorrelated contemporaneous shock.
Additionally, we assume that the previous period’s organic rank,r jt−1, is uncorrelated with the
contemporaneous shockη jt. The rationale is that the platform cannot predict the next period’s
shock in the unobserved quality, and even if it could, the platform does not have any incentive
to incorporate that into the current period’s organic ranking. Both of these yield the moment
27Hence, the mass of consumers who stop at positionnor before is given by the cumulative distribution function
of the exponential distribution,F(λ, n) = 1−e −λ·n. And the mass of consumers with consideration set of sizenis
F(λ, n)−F(λ, n−1) =e −λ·(n−1) −e −λ·n.
25

condition:
E

 ηjt ·ξ jt−1
ηjt ·r jt−1

 = 0 (9)
Estimation proceeds as follows:
1. Start with a guess forλ. Invert (8), and find solutions ˜δjt.
2. Regress ˜δjt onX jt,p jt andSponsored jt. Obtain the residual ˜ξjt.
3. Given a guess ofρ, construct ˜η jt = ˜ξjt −ρ· ˜ξjt−1.
4. Construct the moment condition according to (9), wherer jt−1 is the rank of productjat
timet−1. Search forλandρthat minimize this condition.
Estimation ResultsFigure 8 plots the distribution of estimated search costs within each cate-
gory. There is substantial variation in consumer search costs across categories. For the categories
‘Clothing, Shoes & Jewelry,’ ‘Pet Supplies,’ and ‘Beauty & Personal Care,’ consumers tend to stop
their product search later in the search results pages. By contrast, for ‘Office Products,’ ‘Sports
& Outdoors,’ and ‘Tools & Home Improvement,’ consumers search fewer products before making
a purchase decision. These findings are consistent with consumers searching less when the benefit
of continuing their search is low because there is little new differentiation to be found. Since the
search frictions are quite high for some categories, we expect to see beneficial outcomes from using
pricing algorithms in these categories.
6.3 Evidence of Negative Interaction between Search Costs and Algorithm Us-
age
As we do not know whether a seller is using algorithms or not we need to infer it from the data. We
construct an algorithm usage index derived from the correlation in pricing patterns, following Chen
et al. (2016). The intuition is that sellers using algorithmic pricing are likely to base their prices,
at least partially, on prices set by other sellers. Our data contains prices at quite high frequency,
and if a seller shows high correlation with competitor prices, it suggests that they likely use pricing
algorithms to respond to competitors at fast pace. We compute the correlation of the price vector
26

Figure 8: Estimation of Consumer Search Costs
Fraction of consumers who stop at or before a quarter of the listings in the search results page.
The estimate is by keyword/market, and we then obtain the mean and standard deviation for all
keywords within each product category in our sample.
of a product, − →pj , with the market average price, − →pj′. If the correlation is greater than a threshold
ρ, we infer that the seller of productjis using algorithms to adjust prices. We then average the
algorithm usage indicator for all products in a market as the market’s algorithm usage index:
algok = 1 |Jk| X j∈Jk 1  corr − →pj , − →pj′  ≥¯ρ 	 (10)
Figure 9 shows the fraction of sellers using algorithms in each product-keyword category. When
we set the thresholdρ= 0.3, the mean ratio of sellers using algorithms across all keywords is
31.1%, with a standard deviation of 12%. The empirical findings we provide is robust to different
thresholds we test.
Figure 10 compares the mean product prices when we split the data into low vs high consumer
search costs and algorithm usage. With low consumer search costs, higher algorithm usage correlates
with higher prices, while with higher consumer search costs, it correlates with lower prices. This
negative interaction is consistent with the prediction from our model about pricing and advertising
collusion.
We also conducted a regression analysis to control for category fixed effects and rule out al-
27

Figure 9: Algorithm Usage Index
Fraction of sellers using algorithms in each product keyword market. The mean and standard
deviation within each product category are computed over all product-keywords in that category.
ternative explanations such as that products with higher search costs may also tend to be more
expensive or have higher production costs. Table W A2 in the web appendix shows that the results
remain similar even after controlling for these effects.
Figure 10: Interaction of Consumer Search Costs on Prices
The figure shows the mean prices in markets with low versus high consumer search costs and
algorithm usage.
28

7 Discussion and Conclusion
Our paper analyzes competing sellers who need to decide on product prices and ad-auction bids
in an e-commerce setting. Many of these sellers opt to using algorithms to make these decisions,
and past research raised concerns that the outcome might be harmful for consumers because of
collusion on higher prices. Our findings show that when consumers have heterogeneous search
costs, and enough of them have high costs, then employing reinforcement learning algorithms can
surprisingly result in prices that are lower than competitive prices, because the algorithms learn
to collude on lower advertising bids, which lower the marginal cost for pricing. Lower prices are
beneficial to consumers, but can also be beneficial to the e-commerce platform because they increase
the demand from consumers which compensates for lower advertising revenues. The sellers also
benefit, but mostly from saving on advertising costs. Our analysis of a large-scale dataset of over
2 million products on Amazon.com showed that consumer search costs are high and heterogeneous
for many categories and products. We found a negative interaction between consumer search costs
and algorithm usage on pricing, which is consistent with our theory.
Platforms have multiple ways to strategically respond to sellers using such algorithms. Our
analysis of incentive based strategies shows that adjusting sales commission rates is better for
recoup some of the revenues the platform loses from lower advertising bids compared to changing
reserve prices or disclosing bid information. Increased commissions do erode some of the benefits
for sellers and consumers from lower prices achieved by algorithms, but these prices still remain
lower than without these algorithms.
Our analysis also has a few limitations. First, we focused on two specific decisions: pricing
and advertising, while in reality, sellers might need to learn to make others decisions. However,
the principles that we uncovered regarding advertising should operate for most decisions that are
realized as costs to the sellers, because sellers are better off by coordinating on lower costs if they do
not affect demand. Second, we analyzed a specific reinforcement learning algorithm (Q-learning),
and the results might not generalize to any learning algorithm. However, we can provide some
insight in this direction. Even when initializing an algorithm at the competitive equilibrium prices
and providing it with the true state-action value function (Q matrix), the algorithm will gradually
shift to non-competitive equilibrium because of its exploration feature. We believe that in other
29

cases where exploration is an inherent property of the algorithm, it will learn to converge on non-
competitive outcomes.
Our paper also opens the door to a few additional research questions. For example, platforms
might also act as a seller, selling their own private label products. This self-preferencing (Farronato
et al. 2023, Lam 2021) incentive will add another layer of complexity which is promising for analysis
in future work. Another interesting direction is to consider targeting of keywords and allowing
algorithms to learn who to target, and then coordinate to “split the market” creating inefficient
bidding and matching. In this case, it might be possible that welfare is lowered for consumers.
One implication of our findings is to emphasize the impact of consumer search and heterogeneous
search costs on learning algorithms. These costs create a unique interaction between pricing and
advertising, that cause competition and collusion to yield unexpected outcomes. We believe that
this finding makes a unique contribution to the growing literature on algorithmic collusion.
Another implication of our findings affects mostly platforms and consumers. There is currently
an ongoing debate about the role of algorithmic decision making on platforms, and whether they
are harmful or beneficial to consumers (Zhang et al. 2021, Fu et al. 2022, Zhong 2023). Our
findings provide a nuanced view on this question. Algorithms indeed create tacit collusion when
they compete, but some level of collusion is not necessarily harmful for consumers (or platforms).
Funding and Competing Interests
Partial financial support was received from (removed for blind review). All authors certify that they
have no affiliations with or involvement in any organization or entity with any financial interest or
non-financial interest in the subject matter or materials discussed in this manuscript.
References
Mark Armstrong and Jidong Zhou. Paying for prominence.The Economic Journal, 121(556):F368–F395,
2011.
John Asker, Chaim Fershtman, and Ariel Pakes. Artificial intelligence, algorithm design, and pricing. In
AEA Papers and Proceedings, volume 112, pages 452–56, 2022.
Stephanie Assad, Robert Clark, Daniel Ershov, and Lei Xu. Algorithmic pricing and competition: Empirical
evidence from the german retail gasoline market.Journal of Political Economy, 132(3):000–000, 2024.
Susan Athey and Glenn Ellison. Position auctions with consumer search.The Quarterly Journal of Eco-
nomics, 126(3):1213–1270, 2011.
30

Martino Banchio and Giacomo Mantegazza. Artificial intelligence and spontaneous collusion. Available at
SSRN, 2022.
Martino Banchio and Andrzej Skrzypacz. Artificial intelligence and auction design. InProceedings of the
23rd ACM Conference on Economics and Computation, pages 30–31, 2022.
Zach Y Brown and Alexander MacKay. Competition in pricing algorithms. Technical report, National
Bureau of Economic Research, 2021.
Han Cai, Kan Ren, Weinan Zhang, Kleanthis Malialis, Jun Wang, Yong Yu, and Defeng Guo. Real-time
bidding by reinforcement learning in display advertising. InProceedings of the tenth ACM international
conference on web search and data mining, pages 661–670, 2017.
Sophie Calder-Wang and Gi Heung Kim. Coordinated vs efficient prices: The impact of algorithmic pricing
on multifamily rental markets. Available at SSRN, 2023.
Emilio Calvano, Giacomo Calzolari, Vincenzo Denicolo, and Sergio Pastorello. Artificial intelligence, algo-
rithmic pricing, and collusion.American Economic Review, 110(10):3267–3297, 2020.
Le Chen, Alan Mislove, and Christo Wilson. An empirical analysis of algorithmic pricing on amazon mar-
ketplace. InProceedings of the 25th international conference on World Wide Web, pages 1339–1349,
2016.
Yongmin Chen and Chuan He. Paid placement: Advertising and search on the internet.The Economic
Journal, 121(556):F309–F328, 2011.
Judith Chevalier and Austan Goolsbee. Measuring prices and price competition online: Amazon. com and
barnesandnoble. com.Quantitative marketing and Economics, 1:203–222, 2003.
Hana Choi and Carl F Mela. Monetizing online marketplaces.Marketing Science, 38(6):948–972, 2019.
Jean-Pierre Dub´ e and Sanjog Misra. Personalized pricing and consumer welfare.Journal of Political Econ-
omy, 131(1):131–189, 2023.
Benjamin Edelman, Michael Ostrovsky, and Michael Schwarz. Internet advertising and the generalized
second-price auction: Selling billions of dollars worth of keywords.American Economic Review, 97(1):
242–259, 2007.
Chiara Farronato, Andrey Fradkin, and Alexander MacKay. Self-preferencing at amazon: Evidence from
search rankings. InAEA Papers and Proceedings, volume 113, pages 239–43, 2023.
Chiara Farronato, Andrey Fradkin, and Alexander MacKay. Vertical integration and consumer choice:
Evidence from a field experiment. Technical report, National Bureau of Economic Research, 2025.
Runshan Fu, Ginger Zhe Jin, and Meng Liu.Human-Algorithm Interactions: Evidence from Zillow. com.
National Bureau of Economic Research, 2022.
Drew Fudenberg and Eric Maskin. The folk theorem in repeated games with discouting or with incomplete
information.Econometrica, 54(3):533–554, 1986.
Karsten T Hansen, Kanishka Misra, and Mallesh M Pai. Frontiers: Algorithmic collusion: Supra-competitive
prices via independent algorithms.Marketing Science, 40(1):1–12, 2021.
Sherry He, Brett Hollenbeck, and Davide Proserpio. The market for fake reviews.Marketing Science, 41(5):
896–921, 2022.
Elisabeth Honka and Pradeep Chintagunta. Simultaneous or sequential? search strategies in the us auto
insurance industry.Marketing Science, 36(1):21–42, 2017.
Justin P Johnson, Andrew Rhodes, and Matthijs Wildenbeest. Platform design when sellers use pricing
algorithms.Econometrica, 91(5):1841–1879, 2023.
Mingshi Kang. Sponsored link auctions with consumer search. Technical report, working paper, 2021.
Timo Klein. Autonomous algorithmic collusion: Q-learning under sequential pricing.The RAND Journal
of Economics, 52(3):538–558, 2021.
31

H Tai Lam. Platform search design and market power. Job Market Paper, Northwestern University, 2021.
Kwok Hao Lee and Leon Musolff. Entry into two-sided markets shaped by platform-guided search. Job
Market Paper, Princeton University, 2021.
Jiaxi Liu, Yidong Zhang, Xiaoqing Wang, Yuming Deng, and Xingyu Wu. Dynamic pricing on e-commerce
platform with deep reinforcement learning: A field experiment.arXiv preprint arXiv:1912.02572, 2019.
Xiao Liu. Dynamic coupon targeting using batch deep reinforcement learning: An application to livestream
shopping.Marketing Science, 42(4):637–658, 2023.
Fei Long, Kinshuk Jerath, and Miklos Sarvary. Designing an online retail marketplace: Leveraging informa-
tion from sponsored advertising.Marketing Science, 41(1):115–138, 2022.
Jeanine Mikl´ os-Thal and Catherine Tucker. Collusion by algorithm: Does better demand prediction facilitate
coordination between sellers?Management Science, 65(4):1552–1561, 2019.
Kanishka Misra, Eric M Schwartz, and Jacob Abernethy. Dynamic online pricing with incomplete information
using multiarmed bandit experiments.Marketing Science, 38(2):226–252, 2019.
Ilya Morozov, Stephan Seiler, Xiaojing Dong, and Liwen Hou. Estimation of preference heterogeneity in
markets with costly search.Marketing Science, 40(5):871–899, 2021.
Sendhil Mullainathan and Jann Spiess. Machine learning: an applied econometric approach.Journal of
Economic Perspectives, 31(2):87–106, 2017.
Leon Musolff. Algorithmic pricing facilitates tacit collusion: Evidence from e-commerce. InProceedings of
the 23rd ACM Conference on Economics and Computation, pages 32–33, 2022.
Omid Rafieian. Optimizing user engagement through adaptive ad sequencing.Marketing Science, 42(5):
910–933, 2023.
Imke Reimers and Joel Waldfogel. A framework for detection, measurement, and welfare analysis of platform
bias. Technical report, National Bureau of Economic Research, 2023.
Gabriele Rovigatti, Michele Rovigatti, and Ksenia Shakhgildyan. Artificial intelligence & data obfuscation:
Algorithmic competition in digital ad auctions. Technical report, CEPR Discussion Papers, 2023.
Amin Sayedi, Kinshuk Jerath, and Marjan Baghaie. Exclusive placement in online advertising.Marketing
Science, 37(6):970–986, 2018.
Eric M Schwartz, Eric T Bradlow, and Peter S Fader. Customer acquisition via display advertising using
multi-armed bandit experiments.Marketing Science, 36(4):500–522, 2017.
Adam N Smith, Stephan Seiler, and Ishant Aggarwal. Optimal price targeting.Marketing Science, 42(3):
476–499, 2023.
Raluca M Ursu. The power of rankings: Quantifying the effect of rankings on online consumer search and
purchase decisions.Marketing Science, 37(4):530–552, 2018.
Hal R Varian. Position auctions.International Journal of Industrial Organization, 25(6):1163–1178, 2007.
Qiaochu Wang, Yan Huang, Param Vir Singh, and Kannan Srinivasan. Algorithms, artificial intelligence
and simple rule based pricing. Available at SSRN 4144905, 2023.
Martin L Weitzman. Optimal search for the best alternative.Econometrica (pre-1986), 47(3):641, 1979.
Di Wu, Xiujun Chen, Xun Yang, Hao Wang, Qing Tan, Xiaoxun Zhang, Jian Xu, and Kun Gai. Budget
constrained bidding by model-free reinforcement learning in display advertising. InProceedings of the 27th
ACM International Conference on Information and Knowledge Management, pages 1443–1451, 2018.
Chuan Yu. The welfare effects of sponsored product advertising.Available at SSRN 4817542, 2024.
Shunyuan Zhang, Nitin Mehta, Param Vir Singh, and Kannan Srinivasan. Frontiers: Can an artificial
intelligence algorithm mitigate racial economic inequality? an analysis in the context of airbnb.Marketing
Science, 40(5):813–820, 2021.
32

Zemin Zhong. Platform search design: The roles of precision and price.Marketing Science, 42(2):293–313,
2023.
Appendix
Appendix A.1. Details of Pricing and Bidding Model
For simplicity, we drop the time superscript in the one-shot game. The expected demand for seller
iis:D i(p,b) =θ·Pr{ ˜bi > ˜bj} ·si(pi) + (1−θ)·s i(pi, pj).
To model the uncertainty in auction outcomes, we assume that when a seller submits a bid
bi, the realized bid ˜bi is stochastic ˜bi =ω ibi, and follows a log-normal distribution: log

˜bi
 i.i.d.∼
N

log (bi), σ2 . Hence, when sellersiandjsubmit bidsb i andb j, respectively, the realized bid of
selleri, ˜bi, is higher than that of sellerjwith probability Pr{ ˜bi > ˜bj}= Pr{log(b i)>log(b j)}=
Φ


log

bi
bj

√
2σ

.
Next, we derive the expected Cost Per Click (CPC) that sellerineeds to pay, given that he
wins the auction, E[ ˜bi| ˜bi > ˜bj]. Letu= log(ωi) σ ∼ N(0,1) andv= log(ωj ) σ ∼ N(0,1).
E
h
˜bi| ˜bi > ˜bj
i
= 1
Pr{ ˜bi > ˜bj}
Z
log(bi)
σ +u>
log(bj)
σ +v
biωiϕ(u)ϕ(v)dudv
= 1
Pr{ ˜bi > ˜bj}
Z
log(bi)
σ +u>
log(bj)
σ +v
bi exp(σu)ϕ(u)ϕ(v)dudv
= bi
Pr{ ˜bi > ˜bj}
Z +∞
−∞
exp(σu)ϕ(u)du
Z log(bi)
σ +u−
log(bj)
σ
−∞
ϕ(v)dv
= bi
Pr{ ˜bi > ˜bj}
Z +∞
−∞
Φ


log

bi
bj

σ +u

 exp(σu)ϕ(u)du(11)
Resulting in the expected seller profit:
πi(p,b) =θ·Φ


log

bi
bj

√
2σ

 ·s i(pi) ((1−τ)·p i −c i −˜ci) + (1−θ)·((1−τ)·p i −c i)·s i(pi, pj)
where ˜ci =γ i · bi
Φ


log
 bi
bj

√
2σ


R +∞
−∞ Φ


log

bi
bj

σ +u

 exp(σu)ϕ(u)du.
33

Appendix A.2. Proof of Lemma 1: Monotonicity and Comparison of Competitive
Price and Benchmark Price
A.2.1. Monotonicity of Equilibrium Price Under Price Only Competition
We show that equilibrium prices under price only competitionpoN increase withθusing the implicit
function theorem. The sellers’ profit is:
πi(pi, pj;θ) =

θ
2 si(pi) + (1−θ)s i(pi, pj)
 
(1−τ)p i −c

≡q(θ)m,
where we denotem= (1−τ)p i −c, ands i(pi) =
exp
 ai−pi
µ

1+exp
 ai−pi
µ
 , si(pi, pj) =
exp
 ai−pi
µ

1+exp
 ai−pi
µ

+exp
 aj −pj
µ
 ,
q(θ) = θ 2 si(pi) + (1−θ)s i(pi, pj).
We first compute the first order condition. Assumea i =a j =a,c i =c j =c, we havep i =p j =p
in a symmetric equilibrium. Define exp≡exp

a−p
µ

>0, a1 := 1 + exp, b 1 := 1 + 2 exp.Then
si(pi) = exp a1 , si(pi, pj) = exp b1 .
The derivatives of these expressions with respect top i are d si(pi) dpi = d dp

exp
1+exp

=− exp µ(1+exp)2 =
− exp µa2 1 , ∂si(pi,pj ) ∂pi |pi=pj =p =− expa 1 µb2 1 ,q p(θ) = θ 2 dsi(pi) dp + (1−θ) dsi(pi,pj ) dp (<0).
First–order condition (FOC)Combining the above expressions yields:
G(p, θ) :=∂πi
∂pi
=q p(θ)m+q(θ)(1−τ) = 0.
Providing the equilibrium equation:
m=− q(θ) qp(θ) (1−τ).(12)
Comparative static with respect toθ:G θ =

1
2 s′ i(p)−s ′ i(p, p)  m+  1 2 si(p)−s i(p, p)  (1−τ).
Plugging in (12), we get Gθ 1−τ =  1 2 si(p)−s i(p, p)  −  1 2 s′ i(p)−s ′ i(p, p)  q(θ) qp(θ) .We then simplify:
Gθ = (1−τ) exp 3 θ(1 + 2 exp)2 + 2(1−θ)(1 + exp) 3 = (1−τ) exp 3 2(1 + exp)3 −θ(2 exp 3 + 2 exp2 + 2 exp + 1) >0
For all exp>0 andθ∈[0,1], the denominator is strictly positive (e.g. it is minimized atθ= 1 and
equals 4exp2 + 4exp + 1>0). HenceG θ >0.
By the Implicit Function Theorem dp∗ dθ =− Gθ Gp . SinceG θ >0 we only focus on the sign of
Gp =∂ 2πi/∂p2 i at the interior optimum.
Second–order condition (SOC):G p at the optimum
π′ i(p) =q p m+q(1−τ), π ′′ i (p) =q pp m+ 2(1−τ)q p.
34

At the interior optimum the FOC holds:q p m+q(1−τ) = 0, and we can eliminateminπ ′′ i ,
π′′ i (p) = (1−τ)  2qp − q qpp qp  = (1−τ) 2q2 p −q qpp qp .(†)
We compute 2q2 p −q qpp = exp 2 4µ 2 a3 1 b3 1 h (4exp4 + 2exp3 + 2exp2 + 2exp + 1)θ2 −(8exp 4 + 10exp3 +
14exp2 + 12exp + 4)θ+ 4(1 + exp) 4
i
>0 for allp(all exp>0) andθ∈[0,1],
Together withq p <0 this implies by (†) thatG p <0 atp ∗, therefore, dp∗ dθ =− Gθ Gp >0.
A.2.2. Price with pricing and bidding are higher than price only competition
We show thatp N i ≥p oN i . In a symmetric equilibriumb i =b j, yielding the sellers’ profit:
πi(pi, pj;b i, bj)|bi=bj = θ 2 si(pi)  (1−τ)p i −c−˜c i  + (1−θ)s i(pi, pj)  (1−τ)p i −c 
where ˜ci =γ i · bi
Φ


log
 bi
bj

√
2σ


R +∞
−∞ Φ


log

bi
bj

σ +u

 exp(σu)ϕ(u)du≥0. Definec H =c+ ˜ci.
Whenc H =c, the setting is equivalent to the price only competition case. Thus, it suffices to
show that the equilibrium prices increase withc H .
We compute the first order condition (FOC):
G(p;θ, cH ) = ∂πi ∂pi = θ 2 s′ i(p)  (1−τ)p−c H  + (1−τ) θ 2 si(p) + (1−θ)s ′ i(pi, pj)m+ (1−τ)(1−θ)s i(pi, pj) = 0.
(FOC)
The Implicit Function Theorem implies dp∗ dcH =− GcH Gp . WithG cH = ∂G ∂cH =− θ 2 s′ i(p)>0 and
with
Gp = θ 2 s′′ i (pi)  (1−τ)p−c H  +(1−θ)s ′′ i (pi, pj)  (1−τ)p−c  +2(1−τ)  θ 2 s′ i(pi)+(1−θ)s ′ i(pi, pj)  <0.
we can combine the signs to receive: dp∗ dcH =− GcH Gp =− (+) (−) >0.
Appendix A.3. Proof of Lemma 2: Monotonicity of Collusive Prices
We show that the equilibrium collusive prices decrease withθ. The approach is similar to that
of Lemma 1 and we relegate the details to Web Appendix W A.2. The analysis using the implicit
function theorem shows that becauseG θ <0 for allθ∈[0,1], and becauseG p <0 at the interior
optimum, then dp∗ dθ =− Gθ Gp <0 .
35

Appendix A.4. Proof of Proposition 1
Whenθ= 1, by Lemma 1,p oN is lower thanp N because ad costs increase pricesp N ≥p oN , and
by Lemma 3,p oN =p M . Hence,p N >p oN =p M .
Whenθ= 0, the collusive pricesp M are higher than the full competition pricesp N because
competition leads to lower prices. The ads do not affect demand and cost asθ= 0,p oN =p N . So,
pM >p oN =p N .
By Lemma 2,p M decreases withθ. Therefore, there always exists a point at which the collusive
pricep M and the competitive pricep N intersect.
Appendix A.5. Robustness to additional bidding information, differentiated prod-
ucts and multiple sellers
A.5.1. Alternative Bid Information in State Space
We consider thecomplete statescenario where the state space iss it = (p it−1, pjt−1, bit−1, bjt−1)
and sellers know competitor bids. Figure A1 compares thecomplete statescenario to our previous
scenario. Thecomplete statecondition yields outcomes closer to the fully collusive case, but still
similar to what we found before.
Figure A1: Complete State vs Partial Bid Information
(a) Sellers’ Profit
 (b) Price
 (c) Bid
Panels (a), (b), and (c) show the sellers’ profit, price, and bid, respectively. The blue solid lines
represent the benchmark scenario, while the green lines represent thecomplete statescenario.
Solid red indicates the fully collusive case, solid black the fully competitive, and dashed is fully
competitive without advertising.
A.5.2. Asymmetric Sellers
We present an analysis of full competition and algorithmic pricing for sellers with differentiated
quality. The sponsored ranking is determined by the bids of the two sellers using the same auction
as before. Organic listings are ranked by the platform’s recommendation system, and the order
depends probabilistically on their quality. For consumers , we assume that a fractionθof them
consider only the first listing, while the remaining consumers consider all listings. Their choice of
products depends on the differentiated qualities. The seller’s profit is:
πi(p,b) = Pr{ ˜bi > ˜bj} ·
h
θ·s i(pi, ai)

(1−τ)p i −c i −γ iE
h
˜bi| ˜bi > ˜bj
ii
+ (1−θ)·s i(pi, pj, ai, aj)((1−τ)p i −c i)
36

Figure A2 shows the sellers’ profit and consumer surplus. Similar to our previous results, algo-
rithms benefit both sellers. When consumer search costs are high, algorithmic pricing can benefit
consumers, generating a higher consumer surplus.
Figure A2: Heterogeneous Sellers With Differentiated Quality
(a) Sellers’ Profit
 (b) Consumer Surplus
Panels (a) and (b) show the Q-learning and full competition sellers’ profits and consumer surplus
as functions ofθ. We seta i = 3 anda j = 2, and keep other parameters the same as in Figure 2.
In panel (a), the black line and the blue line represent seller 1’s profits in the full competition and
Q-learning cases, respectively; the dashed black line and the green line represent seller 2’s profits in
the full competition and Q-learning cases, respectively. In panel (b), the solid black line represents
the consumer surplus in the full competition case, while the solid blue line denotes the Q-learning
consumer surplus from our simulation experiments.
A.5.3. Multiple Sellers
We now consider the scenario where theren >2 sellers competing for the sponsored position. In
the price and ads competition case, when sellers are homogeneous, a sellers’ profit is:
πi(p,b)
=θ·Pr{ ˜bi >max j̸=i { ˜bj}} ·si(pi)

(1−τ)p i −c i −γ iE

˜bi| ˜bi >max j̸=i ˜bj

+ (1−θ)·s i(pi,p j)((1−τ)p i −c i)
And in the price only competition case, the sellers’ profit is
πi(p) = θ n ·s i(pi) ((1−τ)p i −c i) + (1−θ)·s i(pi,p j)((1−τ)p i −c i)
Figure A3 shows the equilibrium prices under full competition, price-only competition, and
monopoly for the cases where there are more than two sellers. In the multiple-seller case, the
following results still hold:Lemma 1 (ads increase the equilibrium prices), Lemma 2 (collusive prices
decrease withθ), Lemma 3 (limiting case, whenθ= 1, the collusive prices and the equilibrium
prices under price-only competition are the same across different numbers of sellers, since consumers
only consider the top product whenθ= 1), and Proposition 1. Thus, even with more than two
sellers, the collusive price can still be lower than the competitive prices, and we can also expect the
algorithmic prices to fall below the competitive prices.
37

Figure A3: Multiple sellers
Equilibrium prices as a function ofθwhen there are multiple sellers. The dashed gray, black solid
and red solid line represent the benchmark equilibrium price, the Nash-Bertrand equilibrium price
and collusive price, respectively. Seller-related and ad-related parameters are set the same as in
our default specifications, as in Figure 2.
A.5.4. Separate learning algorithms for pricing and bidding
We consider the scenario where sellers use two Q-learning algorithms separately for pricing and bid-
ding. The pricing algorithm for sellerilearns to set the pricep it with a state space of (pit−1, pjt−1),
while the bidding algorithm learns to setb it with a state space of (b it−1). The single-period profit
remains the same as before, defined in Equation (3). The learning and updating procedures are the
same as before, with the main idea outlined in Equation (5). Figure A4 presents the equilibrium
pricing and bidding results and shows that algorithmic prices still yield lower prices.
Figure A4: Separate learning algorithms for pricing and bidding
(a) Price
 (b) Bid
Panels (a) and (b) show the Q-learning and full competition prices and bids as functions ofθ.
The black, blue, green, and red solid lines represent the equilibrium prices in the full competition,
single Q-learning (for both pricing and bidding), separate Q-learning (for pricing and bidding), and
collusive cases, respectively.
38

Appendix A.6. Platform Strategic Response
A.6.1. Adjusting Commission Rate
Figure A5 presents results for adjusting the commission rate with high consumer search costs. In-
creasing the commission rate can increase the platform’s profit when sellers use algorithms. Decom-
posing the platform’s profit, A5(b) shows that most of the increase is due to increased commissions
revenue from increased commission rates. However, advertising revenues generally decrease as the
bid coordination effect becomes more dominant (Figure W A5(c) in the web appendix).
Figure A5: Platform Strategic Response: Commission Rate
(a) Platform’s Profit
 (b) Commission Revenue
Panels (a) and (b) show the platform’ profit and commission fees as a function ofτwhenθ= 0.8.
The platform’s Q-learning simulation profits and fees are in solid blue. Solid red are fully collusive,
and solid black are fully competitive. Dashed are from pricing without advertising.
The platform might benefit from sellers using algorithmic pricing, thus not requiring any ad-
justment of commission rates. If the platform increases the commission rate, algorithms can still
generate higher consumer surplus and seller profits than under full competition at the adjusted
commission rate.28
A.6.2. Adjusting Ad Auction Reserve Price
We also conduct simulation analyses where we allow the platform to gradually increase the reserve
price from 0. We assume that if the bids submitted by all sellers are lower than the reserve price, the
platform will need to randomly display one of the products in the top position without advertising
costs for the sellers. 29 Figure A6 shows that interestingly, the reserve price might not be effective,
as the platform raises the reserve price above the Q-learning equilibrium bid level, there is a large
28This is because the same consumer search cost will still fall within the region where algorithms yield beneficial
outcomes for both sellers and consumers at a higher commission rate.
29The sellers’ profit function becomes
πt i (pt,b t) =θ·1  ˜bt i ≥r  ·Pr(( ˜bt i > ˜bt j))·s i  pt i  ·  (1−τ)·p t i −c i  −γ i ·E h ˜bt i | ˜bt i > ˜bt j i
+
 1
2 ·θ·1
 ˜bt i < r  ∧  ˜bt j < r  ·s i  pt i  + (1−θ)·s i  pt i, pt j  ·  (1−τ)·p t i −c i  (13)
whererdenotes the platform’s reserve price.
39

discontinuity point in the platform’s revenue. When the reserve price is below the Q-learning
equilibrium bid, increasing the reserve price has very little effect. When it reaches the equilibrium
bid, the algorithms need to coordinate on a new equilibrium bid, and they learn to coordinate on
lower bids below the new reserve price, implying that they will pay even lower advertising costs
(figure A6(b)).
Figure A6: Platform Strategic Response: Reserve Price
(a) Platform’s Profit
 (b) Bids
Panels (a) and (b) show the platform’s profit and sellers’ bids as functions of the reserve price when
θ= 0.8 andτ= 0.15, respectively. The blue solid line denotes the Q-learning platform profits from
our simulation experiments. The representation of other lines and the parameter specifications are
the same as in Figure 2. The dashed vertical lines represent the Q-learning bids in the algorithmic
pricing scenario.
40

Web appendix
Web Appendix W A.1. Sponsored Ads Examples
Figure W A1 below provides an illustration of the results page for the simplified model. Figure W A2
shows an example of an Amazon search results page with 22 products as viewed on a desktop or
laptop browser, which contains a mix of both sponsored and organic products. Key information
presented on the search results page includes the product’s image, price, sales, customer ratings,
and delivery options. The mobile app experience is similar, displaying a mix of sponsored and
organic products vertically that consumers can scroll down or click on for more details.
Figure W A1: Graphical Representation of the Theoretical Model
Sponsored Position
Organic Position
This figure provides a graphical representation of the search result page layout. There is a sponsored
position on the top, followed by organic positions.
Web Appendix W A.2. Details of Proof of Lemma 2
As before, we show this result using the Implicit Function Theorem.
The monopolist’s objective function is
max
pi,pj ,bi,bj
πM (p,b) =π i(p,b) +π j(p,b) (14)
The two sellers would agree to set their bids to the minimum,b i =b j →0, because it minimizes
advertising costs while maintaining the same probability of capturing the demand from consumers
who consider only the first position. The monopolist objective becomes:
max
pi,pj =pi
πM (p,0) = pj =pi (θ·s i (pi) + 2(1−θ)·s i (pi, pi))·((1−τ)·p i −c i)
We first compute the first order condition. Assume exp := exp

a−p
µ

>0, a1 := 1+exp, b1 := 1+
2 exp, pi =p j =p. Then,s i(p) = exp a1 , si(p, p) =exp b1 , d si(p) dp =− exp µ a2 1 , d si(p,p) dp = d dp

exp
1+2 exp

=− exp µ b2 1 ,
W A-1

Figure W A2: Example of Amazon Search Result Page With 22 Products
First five rows of the search results for “air fryer.” Orange rectangles emphasize sponsored listings
that link to products by sellers who won the ad position in an auction.
q(θ) =θ si(p) + 2(1−θ)s i(p, p).
FOC.Combining the above expressions yields:
G(p, θ) :=∂πM
∂p =q p(θ)m+q(θ) (1−τ) = 0 =⇒m=− q(θ) qp(θ) (1−τ).(FOC)
W A-2

Comparative static with respect toθ.Differentiate the FOC inθ:
Gθ =

s′ i(p)−2 d si(p,p) dp

m+

si(p)−2s i(p, p)

(1−τ).
We then simplify:
Gθ =−(1−τ) 2 exp2 θ(1 + 2 exp)2 + 2(1−θ)(1 + exp) 2 <0
(Every denominator term is strictly positive for all exp>0 andθ∈[0,1].)
Second–order condition (SOC):G p at the optimum
We also need to know the sign ofG p =∂ 2πM /∂p2 at the interior optimum. Note
π′ M (p) =q p m+q(1−τ), π ′′ M (p) =q pp m+2(1−τ)q p = (1−τ)  2qp− q qpp qp  = (1−τ) 2q2 p −q qpp qp .
(⋆)
Plugging in d2si(p) dp2 = exp µ2  1 a2 1 − 2exp a3 1  , d2si(p,p) dp2 = exp µ2  1 b2 1 − 4exp b3 1  , and simplifying, we get
2q2 p −q qpp = exp 2 µ2 a3 1 b3 1 h (2−θ) 2 + 6 exp (2−θ) + 2 exp2 (6−θ+θ 2) + 4 exp3 (1 +θ) i >0.
All denominators are positive; each bracketed term is non-negative for exp>0 andθ∈[0,1]
(indeed strictly positive). Sinceq p <0, (⋆) givesG p <0.
Web Appendix W A.3. Discussion of the modeling choice ofθ
W A.3.1. Endogenizingθ
At each positionn, consumers will form an expectation of the incremental utility of continu-
ing their search to the next position, which is log

1 +e δ1 +e δ2 +· · ·+E h ˆeδn+1|δ1, δ2,· · ·, δn i −
log

1 +e δ1 +e δ2 +· · ·+eδn

, and compare with the coststo search one more product. If the
cost is lower than the expected incremental utility, they will continue to search for the product in
positionn+ 1; otherwise, they will stop at positionn.
For the two-product example, suppose that the cumulative distribution function of the cost
isF s. Suppose that every consumer search at least one product, then log

1 +e δ1

−0> s
would always hold. For consumers to search the first position but not the second, we have
log

1 +e δ1

−0> s >log

1 +e δ1 +e δ2

−log

1 +e δ1

. For consumers to search the sec-
ond, we have log

1 +e δ1 +e δ2

−log

1 +e δ1

> s. Therefore,θand 1−θcan be expressed
asθ=
Fs(log(1+eδ1))−Fs(log(1+eδ1 +eδ2)−log(1+eδ1))
Fs(log(1+eδ1)) and 1−θ=
Fs(log(1+eδ1 +eδ2)−log(1+eδ1))
Fs(log(1+eδ1)) .
If we endogenizeθ, the crossing results in Proposition 1 still hold, since the limiting behavior
and the fact that ads increase prices remain the same, although the exact point at which the
W A-3

competitive and collusive prices intersect would change slightly.
W A.3.2. Sensitivity check: A fraction of consumers who consider all products would
also click the sponsored links
We consider a sensitivity check in which a fractionκof consumers who consider all products also
click the sponsored links. The seller’s profit becomes:
πt i(pt,b t) =θ·Pr( ˜bt i > ˜bt j)·s i  pt i  ·  (1−τ)·p t i −c i  −γ i1 ·E h ˜bt i | ˜bt i > ˜bt j i
+ (1−θ)·κ·s i

pt i, pt j  ·  (1−τ)·p t i −c i  −γ i2 ·E h ˜bt i | ˜bt i > ˜bt j i
+ (1−θ)·(1−κ)·s i

pt i, pt j  ·  (1−τ)·p t i −c i 
Figure W A3 presents the equilibrium prices for different values ofκ. Whenκ= 0, it corresponds
to our baseline model. The crossing results of competition prices and collusive prices still hold.
Figure W A3: Sensitivity check: fraction of consumers who consider all products also click ads
The figure shows the full competition prices (with advertising - black, dark blue and blue solid) as
a function of search costsθand under different values ofκ.
W A.3.3. Alternative Characterization of Consumer Search Costs
We consider an alternative way of modeling consumer search costs and show that the details of
modeling consumer search costs do not change our main findings that collusive prices can fall
below competitive prices. Following Reimers and Waldfogel (2023), we consider a reduced-form
characterization of consumer search costs. Specifically, consumer’s utility for productjwhen ranked
atr j is given by:
uij =X ′ jβ−αp j +ζr j +ζ ′r0 j +ξ j +ϵ ij
where the outside good has utility 0,ξ j represents unobserved product quality,r 0 j is the initial rank
of productj, andϵ ij is an extreme value error. Here,ζis the causal effect of rank on sales, while
W A-4

ζ ′ reflects the systematic product quality variation across ranks that is not accounted for byx j.
The mean expected utility of productjwhen ranked atrisδ j(r) =X ′ jβ−αp j +ζ ′r0 j +ζr. Even
if productjwere moved to a different rankr j, the part of utility reflected byζ ′r0 j would remain,
while the part reflected byζrwould change. The “rank-independent expected mean utility” is
δ0 j ≡X ′ jβ−αp j +ζ ′r0 j =δ j(r)−ζr.
Productj’s market share when rankedr th is given bys j(r) = eδj (r) 1+P eδj (r) . The way in which
the products are ranked affects both consumer well-being and the propensity for consumers to
purchase.
Then assume that the ad auction part is the same as the one we consider in our benchmark
model, while the consumer choice is from this model. In the full competition scenario, where sellers
compete on both prices and bids, the profit function becomes:
πt i(pt,b t) = Pr(˜bt i > ˜bt j)· e
ai−pt i
µ
e
ai−pt i
µ +e
aj −pt j −ζ
µ + 1
·

(1−τ)·p t i −c i  −γ i ·E h ˜bt i | ˜bt i > ˜bt j i
+ Pr(˜bt i < ˜bt j)· e
ai−pt i −ζ
µ
e
ai−pt i −ζ
µ +e
aj −pt j
µ + 1
·

(1−τ)·p t i −c i  (15)
In the scenario where there are no sponsored ads and the platform randomly displays one of
the products in the top position, the sellers’ profit function is:
πt i(pt,b t) = 1 2 ·

 e
ai−pt i
µ
e
ai−pt i
µ +e
aj −pt j −ζ
µ + 1
+ e
ai−pt i −ζ
µ
e
ai−pt i −ζ
µ +e
aj −pt j
µ + 1

 ·  (1−τ)·p t i −c i 
Figure W A4 presents the equilibrium results. The results are robust and similar to those in
Figure 2. 30 The main intuitions from Lemma 1 (advertising increases prices), from Lemma 2
(monopoly prices decrease with the rank effect), as well as the limiting behavior as the rank effect
approaches infinity, remain robust, and collusive prices can still be lower than competitive prices
when consumer search costs are high.
Web Appendix W A.4. Platform Strategic Response Additional Results
W A.4.1. Platform Strategic Response: Commission Rate Additional Results
Figure W A5 presents additional results when the platform adjusts the commission rate.
30In the limiting case, when the causal effect of rank on sales, denoted byζ, approaches infinity (ζ→ ∞) or zero
(ζ→0), it is equivalent to the case where the fraction of consumers who only care about the first position approaches
one (θ→1) or zero (θ→0), respectively.
W A-5

Figure W A4: Casual Effect of Rank Model
(a) Prices
 (b) Bids
Panels (a) and (b) show the equilibrium prices and bids as functions of the casual effect on sales
parameterζ, respectively. The representation of other lines and the parameter specifications are
the same as in Figure 2.
Figure W A5: Platform Strategic Response: Commission Rate Additional Results
(a) Ad Revenue
 (b) Sellers’ Profit
(c) Prices
 (d) Consumer Surplus
Panels (a) to (d) show the platform’ ads revenue, sellers’ profit, market price and consumer surplus
as a function ofτwhenθ= 0.8, respectively. The blue solid line denotes the Q-learning platform
profits from our simulation experiments. The representation of other lines and the parameter
specifications are the same as in Figure 2.
W A.4.2. Platform Strategic Response: Reserve Price Additional Results
Figure W A6 presents additional results when the platform adjusts the reserve price.
W A-6

Figure W A6: Platform Strategic Response: Reserve Price
(a) Commission
 (b) Ads Revenue
(c) Seller Profit
 (d) Consumer Surplus
Panels (a) - (d) show the platform’s commission revenue, ads revenue, sellers’ profit, and consumer
surplus as functions of the reserve price whenθ= 0.8 andτ= 0.15, respectively. The blue solid
line denotes the Q-learning platform profits from our simulation experiments. The representation
of other lines and the parameter specifications are the same as in Figure 2. The dashed vertical
lines represent the Q-learning bids in the algorithmic pricing scenario.
W A.4.3. Platform’s Alternative Objective: W eighted Average of T otal Surplus
Given competition between platforms, a platform might also consider consumer surplus and seller
profits to encourage entry for long-term business growth. Hence, we consider a scenario where the
platform is maximizing a weighted average of its own profit, sellers’ profit, and consumer surplus,
with weightsωand 1−ω, respectively. The platform’s objective can be written as follows:
ω·π p(p,b)+(1−ω)·

X
j
πj(p,b) +CS(p)

 =ω·  πAd p (p,b) +π Com p (p,b)  +(1−ω)·

X
j
πj(p,b) +CS(p)


whereπ p(p,b) is the platform’s own-profit,π j(p,b) is sellerj’s profit as defined in (3), andCS(p)
is the consumer surplus as defined in (6).
Whenω= 1 2 , i.e., the platform puts equal weight on its own profit versus the sum of sellers’
profits and consumer surplus, then its objective is equivalent to maximizing the total surplus. 31
31Since the commission fee and advertising costs are transfers between sellers and consumers, they cancel out when
ω= 1 2 . Therefore, the total surplus in this scenario is also equivalent to the duopoly case where there is no platform,
no commission fee, and no advertising costs.
W A-7

The platform’s objective becomes P j  θ·Pr( ˜bj > ˜b−j)·s j (pj) + (1−θ)·s j (pj, p−j)  ·(p j −c j)−
θ· P j 1{j∈ J1(Γ)} ·µ·log (1−s j (pj))−(1−θ)·µ·log  1− P j sj (p)  .
Figure W A7a shows the total surplus as function ofθwhen commission rate is 15%, i.e.,τ=
0.15.32 When consumer search costs are high, compared with the full competition case, using
learning algorithms always increase the total surplus. Because compared to the outside option,
products on the platform become cheaper and hence more attractive. Figure W A7b plots the total
surplus when the platform adjusts its commission rate, given a high value ofθ. Algorithmic pricing
consistently yields a higher total surplus than the full competition case, even when the platform is
adjusting the commission rate.
Figure W A7: Platform Strategic Response: Total Surplus
(a) Total Surplus vsθ
 (b) Total Surplus vsτ
Panel (a) shows the total surplus as a function of consumer search friction whenτ= 0.15, and (b)
shows the total surplus as a function of the reserve price whenθ= 0.8. The blue solid line denotes
the Q-learning platform profits from our simulation experiments. The representation of other lines
and the parameter specifications are the same as in Figure 2.
Thus, even if the platform’s own single-period profit is lower, considering the sellers’ profit and
consumer surplus, the platform will not make any adjustments, and the beneficial outcomes for
sellers and consumers will remain.
Web Appendix W A.5. Additional Empirical Results
W A.5.1. Distribution of Sponsored Product Ads
The positions that are most likely to be sponsored positions in our data are 1-4, 11-14, and 19-22 for
a product page with 60 products, and 1, 2, 7, 12, 17, and 22 for a product page with 22 products.
Figure W A9 present the corresponding heatmaps of the density of sponsored products within a
product result page.
32This is the rate for most product categories on Amazon.com
W A-8

Figure W A8: Distribution of Sponsored Product Ads by Position for Different Page Layouts
(a) Page Layout with 60 products
 (b) Page Layout with 22 products
This figure shows the ratios of sponsored products by position for product result pages with 60 and
22 products.
Figure W A9: Distribution of Sponsored Product Ads by Page Layout
(a) Page layout with 60 products.
 (b) Page layout with 22 products.
This figure shows the heatmap plots of the ratios of sponsored products by position for product
result pages containing 60 and 22 products.
W A-9

W A.5.2. Summary Statistics at Keyword Level
Table W A1 presents the summary statistics at keyword level.
Table W A1: Summary Statistics at Keyword Level
Mean SD Min Max
Price 56.83 86.24 6.576 1,073
CPC 1.393 0.896 0.420 7.390
Monthly Sales 5,041 3,903 207.2 28,097
Monthly search volume 284,196 396,570 50,008 4,167,001
N = 2,382
W A.5.3. Comparing Sponsored and Organic Products
We plot the average prices, number of ratings, ratings, and number bought last month for a given
position in Figure W A10. Compared with their organic counterparts in the same positions, spon-
sored products have lower number of reviews and number of products bought last month, indicating
that they are more likely to be less established products and might be buying ads to gain awareness
from consumers. The average ratings decrease with position, with sponsored products having lower
average ratings than organic products in the same position. However, ratings might be a noisy
indicator of quality, and sellers might be buying fake reviews (He et al. 2022). We are cautious
about drawing the conclusion that sponsored products have lower mean quality.
Figure W A10: Position vs Observables
(a) Price
 (b) Number Bought Last Month
(c) Number of Reviews
 (d) Ratings
The panels (a)–(d) show the mean product prices, number of products bought last month, number of reviews,
and ratings by each position for sponsored and organic products. The blue circle represents the organic
products, while yellow squares denote the sponsored products.
W A-10

W A.5.4. Regression: Negative Interaction
We run the following equivalent regressions, controlling for category fixed effects.
pricek =β 0 +β 1 ·search cost highk +β 2 ·algo highk +β 3 ·search cost highk ·algo highk +ϵ k (16)
Table W A2 presents the results. The interaction of algorithm usage and consumer search costs
on prices is significantly negative when controlling for category fixed effects.
Table W A2: Search Cost and Algorithm Usage Interaction
Price
Search cost high 63.36*** 42.55***
(5.942) (5.809)
Algo high 2.502 1.797
(5.942) (5.727)
Algo high·search cost high -22.41*** -26.83***
(8.404) (7.819)
constant 30.45*** 42.31***
(4.077) (3.900)
Category FE No Yes
Standard errors in parentheses *** p<0.01, ** p<0.05, * p<0.1
W A-11
