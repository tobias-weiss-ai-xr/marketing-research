---
title: 'Underquoting and the Dual Role of Price Guides: Evidence from Housing Sales'
url: https://doi.org/10.21203/rs.3.rs-10519536/v1
category: ai-marketing
subcategory: empirical
date: 2026-08
venue: Research Square
authors:
- Adeleh Farzadfar
- Peyman Khezr
- Armin Pourkhanali
source: openalex-oa
pdf_url: https://www.researchsquare.com/article/rs-10519536/latest.pdf
pages: 54
chars: 115769
fetched_at: '2026-11-08T20:03:03+00:00'
kb_version: 1
---

# Underquoting and the Dual Role of Price Guides: Evidence from Housing Sales

Underquoting and the Dual Role of Price Guides:
Evidence from Housing Sales
Adeleh Farzadfar 
RMIT University
Peyman Khezr 
RMIT University
Armin Pourkhanali 
RMIT University
Research Article
Keywords: Underquoting, Housing market
Posted Date: August 6th, 2026
DOI: https://doi.org/10.21203/rs.3.rs-10519536/v1
License:   This work is licensed under a Creative Commons Attribution 4.0 International License.  
Read Full License
Additional Declarations: No competing interests reported.

Underquoting and the Dual Role of Price Guides: Evidence from
Housing Sales
Abstract
This paper studies underquoting as a price-guidance problem in residential property markets. We
argue that advertised guides perform diﬀerent roles across sales mechanisms: in auctions, they can attract
bidders and intensify competition, while in private-treaty sales they more directly signal the seller’s
asking position and shape bargaining. The model predicts that auction guides should be more downward
distorted, less informative about ﬁnal prices, and more likely to be associated with underquoting. Using
Melbourne detached-house listings and transactions, we show that only around one-quarter of auction
prices fall within the advertised guide, compared with more than half of private-treaty prices, and that
around two-thirds of auction properties sell above the upper guide. We then construct guide-independent
valuation benchmarks using global hedonic and geographically weighted regression models estimated on
prior transactions and applied out of sample. The GWR benchmark produces locally adaptive valuation
ranges that are more balanced around realised auction prices than agent-provided auction guides and
provides a scalable benchmark for assessing advertised price guidance. Under a conservative GWR-based
measure, around 44% of auction transactions and 14% of private-treaty transactions are classiﬁed as
underquoted. The ﬁndings support the dual-role interpretation of price guides and provide a scalable
framework for measuring underquoting and improving price-guidance governance.
Keywords: Underquoting; Housing market
JEL Classiﬁcation: R31, D44, L85, C21, C51
1

1 Introduction
Housing is the largest component of household wealth and an important channel linking household
balance sheets, credit conditions, and the broader macroeconomy (Anari and Kolari, 2002; D’Lima and
Schultz, 2021). Fair and transparent price discovery in residential property markets is therefore important for
both household welfare and market eﬃciency. Buyers rely on advertised price guides to assess aﬀordability,
allocate search eﬀort, and decide whether to inspect a property or participate in its sale. When these guides
systematically diverge from plausible market values, buyers may incur unnecessary search and participation
costs, while the competitive conditions surrounding the sale may also be altered.
Underquoting refers broadly to the practice of advertising a property at a price below its plausible
market value or expected transaction range. The practice has attracted particular attention in Australian
housing markets, especially in Victoria and New South Wales, where regulators have introduced disclosure
requirements governing the preparation and revision of price guides and the use of comparable sales. 1
These reforms were intended to improve transparency and reduce misleading price guidance. Nevertheless,
underquoting remains a persistent source of consumer complaints, enforcement activity, and public concern.
One main issue is that the economic role of a price guide may diﬀer across sales mechanisms. In an
auction campaign, the guide is announced before the competitive bidding process begins. It may therefore be
used strategically to attract inspections, increase auction attendance, and expand the pool of active bidders.
The seller can beneﬁt from additional participation while relying on a reserve price to protect against an
undesirably low outcome. In a private-treaty sale, by contrast, the guide is more closely connected to
the seller’s asking position and the subsequent bargaining process. Buyers formulate oﬀers relative to the
advertised range, and a guide that is substantially below the seller’s expectations may attract buyers with
insuﬃcient budgets, generate unsuitable oﬀers, and increase negotiation or delay costs.
This distinction suggests that price guides perform two related but diﬀerent functions. They act as
participation devices by inﬂuencing buyer attention and entry, but they also act as information signals by
communicating a plausible transaction range. The relative importance of these functions depends on the
sales mechanism. In auctions, the participation role may dominate, making guides more susceptible to
strategic downward distortion. In private-treaty sales, the information and bargaining role may impose greater
1See, for example, the Property, Stock and Business Agents Amendment (Underquoting Prohibition) Act 2016 (NSW) and the
Estate Agents Amendment Act 2016 (Vic), discussed in Castle (2017).
2

discipline on the guide and produce a closer relationship between advertised and realised prices.
This paper develops a theoretical and empirical framework for examining this dual role. The theoretical
model allows a seller to lower the guide below a market-consistent valuation benchmark in order to increase
buyer participation. The beneﬁt of doing so is assumed to be greater in auctions, where additional bidders
directly intensify competition. The cost of distorting the guide is assumed to be greater in private-treaty sales,
where misleading guidance can generate buyer mismatch, low oﬀers, and bargaining frictions. The model
consequently predicts that auction guides will be more strongly distorted downwards, underquoting will be
more prevalent in auction campaigns, and ﬁnal auction prices will be less likely to fall within the advertised
range.
Testing these predictions requires a benchmark for plausible property value that does not rely exclusively
on the ﬁnal sale price or on a small set of agent-selected comparable transactions. Existing measures of
underquoting frequently use listing-to-sale price gaps, listing-to-sale ratios, or comparisons with nearby sales
(Stevenson et al., 2010; Österling, 2016; Pardasani, 2020; Gargano and Giacoletti, 2021). These measures
provide useful descriptive information, but they can conﬂate the original listing decision with subsequent
auction competition, bargaining, and changes in market conditions. A large gap between the guide and the
ﬁnal price does not, by itself, establish that the property was deliberately underquoted when listed.
We address this measurement problem by constructing model-implied valuation benchmarks for detached
houses in metropolitan Melbourne. T wo complementary approaches are used. The ﬁrst is a ﬁxed-eﬀects
hedonic pricing model that relates transaction prices to structural, locational, and local-market characteristics.
The second is a geographically weighted regression model that allows the marginal values of housing
characteristics to vary across space. The models are estimated separately for auction and private-treaty
transactions, reﬂecting the possibility that properties sold through the two mechanisms follow diﬀerent pricing
relationships.
The valuation models are estimated using 65,768 detached-house transactions from 2023–2024 and
applied out of sample to 3,991 matched listings and transactions from 2025. The evaluation sample contains
1,336 auction sales and 2,655 private-treaty sales. Advertised price guides are not used to estimate the
valuation models. Instead, the resulting model-implied values are compared with the advertised lower and
upper guide bounds and with realised transaction prices.
The descriptive evidence reveals a sharp diﬀerence between the two sales mechanisms. Only 26.27% of
3

auction prices fall within the advertised range, while 65.72% exceed the upper guide and only 8.01% fall below
the lower guide. In private-treaty sales, 56.05% of prices fall within the advertised range, 19.62% exceed the
upper guide, and 24.33% fall below the lower guide. Auction guides are therefore not merely less accurate;
their errors are strongly asymmetric and concentrated below realised transaction prices. Private-treaty guides
exhibit a considerably more balanced relationship with ﬁnal prices.
To distinguish likely underquoting from ordinary prediction error or unexpected competition, we adopt a
conservative classiﬁcation rule. A transaction is classiﬁed as underquoted only when its realised sale price
exceeds both the upper bound of the advertised range and the lower bound of the model-implied valuation
interval. Under the preferred GWR benchmark, 44.09% of auction transactions satisfy this criterion, compared
with 14.05% of private-treaty transactions. The results are consistent with the theoretical prediction that
auction guides are more strongly used as participation devices, whereas private-treaty guides convey more
information about plausible transaction values.
The spatial valuation model also materially improves typical out-of-sample prediction accuracy relative
to the global hedonic benchmark. This improvement is important because Melbourne contains highly
diﬀerentiated local housing markets in which the value of land, accessibility, dwelling attributes, and
neighbourhood conditions can vary substantially across space. The resulting GWR benchmarks provide
a locally adaptive basis for assessing whether advertised guidance is low relative to the values implied by
observable property and neighbourhood characteristics.
The paper makes three contributions. First, it develops a uniﬁed framework for understanding the dual role
of housing price guides across auction and private-treaty sales. While existing explanations of underquoting
commonly emphasise bidder entry and auction competition, our framework incorporates this participation
channel while showing why price guides may perform a stronger information and bargaining function in
negotiated sales.
Second, the paper provides new comparative evidence on the informativeness of advertised price guides
across sales mechanisms. The substantially lower within-guide rate and strongly asymmetric guide errors
observed for auctions are consistent with auction guides being less closely related to expected transaction
values than private-treaty guides.
Third, the paper develops a scalable model-based approach to measuring underquoting. By combining
advertised guide ranges, realised sale prices, and out-of-sample valuation intervals estimated without using
4

advertised guides, the measure reduces reliance on ex post price gaps or a small number of potentially
unrepresentative comparable sales. The use of a spatially adaptive GWR benchmark further allows valuation
relationships to vary across local housing submarkets and improves typical out-of-sample prediction accuracy
relative to the global hedonic benchmark.
The analysis does not estimate the causal eﬀect of the Victorian disclosure regime, nor does it observe
bidder numbers, inspections, reserve prices, bargaining histories, or agents’ subjective valuations. The
theoretical mechanisms should therefore be interpreted as providing an economic explanation for the empirical
patterns rather than as being structurally identiﬁed. Similarly, the empirical underquoting measure identiﬁes
transactions that satisfy a conservative valuation-based criterion; it does not establish the legal intent required
for a regulatory ﬁnding in an individual case.
Melbourne provides a useful setting for the analysis. It is a large and spatially heterogeneous housing
market with substantial activity under both auction and private-treaty mechanisms. It also operates under an
established disclosure regime, making it possible to study the relationship between advertised guidance and
transaction prices under current institutional conditions.
The remainder of the paper proceeds as follows. Section 2 reviews the literature on strategic price
guidance, bidder participation, asking-price signals, regulation, and housing valuation. Section 3 develops the
dual-role theory of price guides. Section 4 describes the institutional setting and the data. Section 5 presents
the valuation models, constructs the underquoting measure, and reports the empirical results. Section 6
concludes.
2 Literature review
Price guidance plays an important role in housing markets because buyers must decide where to direct
their search before the value of a property is fully revealed through bidding or negotiation. Advertised
guides can convey information about plausible transaction values, but they can also be used strategically to
inﬂuence buyer attention and participation. Underquoting arises when an advertised guide is set below a
market-consistent valuation or expected transaction range. Related studies use terms such as underpricing, bait
pricing, and strategic listing, but the present paper uses underquoting to describe the listing-stage behaviour
most closely associated with the Australian regulatory setting.
5

One strand of the literature examines price guidance as a participation device in housing auctions. A
deliberately low guide can reduce perceived aﬀordability barriers, attract inspections, and increase the number
of buyers who attend or participate in the auction. Additional bidders may then raise the ﬁnal price by
increasing competitive pressure. Evidence from Ireland indicates that properties sold by auction can command
a premium relative to comparable private-treaty sales, particularly in buoyant market conditions, which is
consistent with the strategic use of low initial guidance to stimulate competition (Stevenson et al., 2010).
Evidence from Sweden also shows that lower guides can attract buyer attention, although increased attention
does not necessarily translate into more bidders or higher prices in every market (Hungria-Gunnelin, 2018).
Similarly, Österling (2016) ﬁnds that requiring advertised guides to more closely reﬂect market values reduced
buyer engagement at several stages of the sale process and increased the probability of an unsuccessful sale.
These ﬁndings illustrate the central trade-oﬀ associated with auction guidance: more accurate guides may
improve transparency, but they may also reduce participation and weaken competition.
The eﬀect of low auction guides may be reinforced by behavioural responses during the sale process.
Initial guides can provide salient reference points, while observable participation and bidding can generate
informational herding, competitive arousal, and auction fever (Banerjee, 1992; Bikhchandani et al., 1992;
Simonsohn and Ariely, 2008; Malmendier and Lee, 2011). In the housing-market context, Han and Strange
(2014) examine bidding wars and show how strategically low listing prices can stimulate competition among
multiple buyers, increasing the likelihood that the transaction price exceeds the advertised price. 2 Buyers
may also update their valuations in response to the actions of other participants or become increasingly
committed after investing time and eﬀort in inspections and bidding. These mechanisms can amplify the
diﬀerence between the initial guide and the ﬁnal transaction price. They also imply that the listing-to-sale
price gap reﬂects both the seller’s initial pricing strategy and the subsequent competitive process. A large gap
is therefore consistent with underquoting, but does not by itself establish that the guide was below a plausible
market value when it was announced.
A second strand of the literature studies the role of asking prices in negotiated housing markets. In
private-treaty sales, the advertised price is not merely an instrument for attracting buyers; it also conveys
information and establishes a starting point for negotiation. Horowitz (1992) models the list price as a signal
2The prospect of a bidding war must be weighed against the uncertainty associated with the auction outcome. Khezr (2018)
shows that, when sellers are risk averse, they may prefer to accept a pre-auction oﬀer rather than face the uncertainty associated with
the auction. This may provide an additional rationale for using a low guide to attract a suﬃciently large pool of potential bidders.
6

that aﬀects buyers’ beliefs about the property’s value and the seller’s willingness to accept an oﬀer. Y avas and
Y ang (1995) similarly show that the seller’s listing-price decision balances competing objectives. A lower
asking price can increase buyer arrival and shorten the search process, whereas a higher asking price may
strengthen the seller’s bargaining position and raise the transaction price conditional on sale. The optimal
asking price therefore reﬂects both search and bargaining considerations. Announced prices can also inﬂuence
seller commitment in auction settings. Khezr and Menezes (2018) characterise the asking price as a partial
commitment device and show that, under certain conditions, it yields a higher expected payoﬀ for the seller
than a fully committed reserve price.
Empirical evidence also shows that asking-price strategies evolve during the marketing process. Knight
(2002) documents the relationship between listing-price revisions, time on market, and eventual selling prices,
indicating that the asking price responds to information revealed through buyer interest and unsuccessful
search. Recent evidence from South Australia also links strategic underpricing to housing-market liquidity
and time on market (Pilat and Leishman, 2025). Using detailed records of oﬀers and counteroﬀers, Merlo and
Ortalo-Magné (2004) show that the timing and sequence of oﬀers reveal information about valuations and
bargaining positions. These studies imply that private-treaty guides should not necessarily be interpreted as
truthful point forecasts. Nevertheless, because the guide frames subsequent oﬀers and negotiations, setting it
substantially below the seller’s expected value can attract poorly matched buyers, generate unsuitable oﬀers,
and increase delay or bargaining costs.
The auction and private-treaty literature therefore assign diﬀerent roles to the same observable object. In
auctions, the guide can primarily operate as an entry device because the ﬁnal price is determined through
competitive bidding and the seller can use a reserve price to protect against an unacceptably low outcome. In
private-treaty sales, the guide has a stronger signalling and bargaining function because oﬀers are formulated
and negotiated relative to the advertised range. Existing studies generally analyse these mechanisms separately.
There is comparatively little work providing a uniﬁed explanation for why the informativeness and strategic
use of price guides should diﬀer across sales mechanisms. The theoretical framework developed in this paper
addresses this gap by allowing the participation beneﬁt and the information or bargaining cost of low guidance
to vary between auctions and private-treaty sales.
A related literature examines the regulation of underquoting. Australian reforms have strengthened
disclosure obligations, restricted the language agents may use in advertising, and imposed requirements
7

concerning comparable sales and the revision of price estimates. Empirical studies of Sydney and Melbourne
document a narrowing of listing-to-sale price gaps following stricter regulation (Pardasani, 2020; Gargano
and Giacoletti, 2021). These ﬁndings suggest that disclosure rules can constrain the most extreme forms of
low guidance. At the same time, continued complaints and enforcement activity indicate that regulation has
not removed the underlying incentives to attract buyers through advertised prices. The eﬀect of regulation is
therefore likely to depend on whether it transforms the guide into a binding constraint or merely increases the
expected cost of setting it below a market-consistent value.
The empirical measurement of underquoting remains diﬃcult. Most existing studies rely on listing-to-sale
price diﬀerences, listing-to-sale ratios, or comparisons with a limited set of nearby transactions (Stevenson
et al., 2010; Österling, 2016; Hungria-Gunnelin, 2018; Pardasani, 2020; Gargano and Giacoletti, 2021). These
approaches provide informative descriptive measures, but they face two important limitations. First, realised
prices are determined after the guide has been set and may reﬂect bidder competition, bargaining, market news,
or changes in local demand. Second, comparable-sales approaches may depend on a small set of properties
that diﬀer in quality or location and may be selected strategically by the selling agent. Consequently, these
measures can conﬂate deliberate low guidance with legitimate valuation uncertainty and subsequent price
discovery.
This measurement problem connects the underquoting literature to the broader housing-valuation literature.
Hedonic pricing models provide a conventional method for estimating the market value of heterogeneous
properties by relating transaction prices to structural, locational, and neighbourhood characteristics (Rosen,
1974; Blomquist and Worley, 1981; Sheppard, 1999). Their principal advantage is transparency: they provide
an independently estimated benchmark that does not rely on the advertised guide itself. A standard hedonic
speciﬁcation, however, imposes common marginal eﬀects across a metropolitan market, even though the
value of land, accessibility, dwelling characteristics, and local amenities may vary substantially across space.
Geographically weighted regression addresses this limitation by allowing coeﬃcients to vary with location
(Brunsdon et al., 1996; Fotheringham et al., 2002, 2009). This ﬂexibility is particularly relevant in a spatially
heterogeneous housing market such as Melbourne, where otherwise similar property characteristics can be
valued diﬀerently across local submarkets. Combining a global hedonic model with a spatially adaptive
GWR benchmark provides a useful way to assess whether estimated underquoting is robust to alternative
assumptions about the geographic structure of housing prices.
8

This paper contributes to these literatures in three ways. First, it develops a uniﬁed theory in which
price guides serve as both participation devices and information signals, with the relative importance of
these functions depending on the sales mechanism. The framework predicts that auction guides will be
more strongly distorted downwards and less closely related to ﬁnal prices than private-treaty guides. Second,
the paper develops a conservative model-based measure of underquoting that combines advertised guide
ranges, independently estimated valuation intervals, and realised transaction prices. This reduces reliance on
listing-to-sale price gaps alone. Third, by estimating separate hedonic and GWR benchmarks for auction and
private-treaty transactions, the paper provides new evidence on how the informativeness and strategic use of
advertised price guides diﬀer across housing sales mechanisms.
3 The Dual Role of Price Guides in Housing Sales
Price guides can serve two distinct economic functions in housing markets. First, they can act as
participation devices by shaping buyer attention, inspection decisions, and entry into the sale process. Second,
they can act as information signals by communicating the seller’s expectations about plausible transaction
values. The relative importance of these two functions depends on the sales mechanism. In auction campaigns,
the participation role is likely to dominate because additional bidders directly increase competitive pressure
and the seller can rely on a reserve price for downside protection. In private-treaty sales, the information
role is likely to be more important because oﬀers are negotiated relative to the guide, and misleadingly low
guidance can attract mismatched buyers, generate low oﬀers, and increase bargaining frictions.
This section develops a simple model that captures this dual role. The model shows that underquoting can
occur under both auction and private-treaty sales, but it should be more severe in auctions. It also implies that
ﬁnal prices should be less likely to fall within the quoted price range in auctions than in private-treaty sales.
3.1 Environment
There is one seller and a set of potential buyers. The seller observes a signal 𝑠 about the likely market
value of the property. Let
𝜇(𝑠) = E[𝑃𝑐 | 𝑠]
9

denote the seller’s posterior expectation of the competitive transaction price under market-consistent price
guidance, where 𝑃𝑐 is the benchmark transaction price that would arise absent strategic distortion in the
guide.
The seller publicly announces a price guide range
[𝑞 𝐿,𝑞 𝐻], 𝑞 𝐿 ≤𝑞𝐻.
For the theory, we focus on the upper bound of the guide, 𝑞𝐻, because it is the most conservative advertised
benchmark for underquoting. To simplify notation, suppose 𝑞 =𝑞𝐻. The lower guide is captured by the width
of the quoted range, 𝑤 =𝑞𝐻 −𝑞 𝐿, so that the advertised range can be written as [𝑞 −𝑤,𝑞 ].
Deﬁne the downward deviation of the upper guide from the seller’s market-consistent benchmark as
𝑑 = 𝜇(𝑠) − 𝑞. A larger value of 𝑑 means that the upper guide is set further below the seller’s posterior
benchmark. The case 𝑑 >0 corresponds to underquoting.
Deﬁnition 3.1. A property is underquoted if the upper bound of the advertised price guide is below the
seller’s market-consistent benchmark: 𝑞 < 𝜇(𝑠), or equivalently,𝑑 >0.
The seller chooses the guide before the transaction price is determined. The sales mechanism is denoted
by
𝑀 ∈ {𝐴,𝑃𝑇 },
where𝐴 denotes auction and 𝑃𝑇 denotes private-treaty sales.
3.2 The two roles of the price guide
The price guide aﬀects the seller’s expected payoﬀ through two channels. The ﬁrst is a participation
channel. Let 𝑚 𝑀 (𝑑) denote the expected number of participating buyers under mechanism 𝑀. In auctions,
this is the expected number of bidders who attend and bid. In private-treaty sales, it is the expected number
of serious buyers, inspections, or oﬀers generated by the campaign. We assume that lower guides increase
participation:
𝑑𝑚 𝑀 (𝑑)
𝑑𝑑 > 0.
Since𝑑 =𝜇(𝑠) −𝑞, increasing𝑑 is equivalent to lowering the advertised guide.
10

The second channel is an information and bargaining channel. The guide communicates information
about the seller’s expected price and shapes buyer beliefs. This role is especially important in private-treaty
sales, where oﬀers are negotiated relative to the guide. If the guide is set too far below the seller’s expected
transaction value, the seller may attract buyers whose budgets are too low, receive oﬀers far below the seller’s
acceptable price, or incur delay and bargaining costs.
We capture these two channels using a reduced-form payoﬀ representation. Let 𝐵𝑀 (𝑑;𝑠) denote the gross
beneﬁt from setting the guide 𝑑 below the market-consistent benchmark. This beneﬁt reﬂects the participation
eﬀect of a lower guide. We assume
𝐵𝑀 (0;𝑠) = 0, 𝐵 𝑀 𝑑 (𝑑;𝑠) > 0, 𝐵 𝑀 𝑑𝑑 (𝑑;𝑠) < 0.
Thus, a lower guide increases expected beneﬁt through participation, but the marginal beneﬁt is diminishing.
Let𝐾 𝑀 (𝑑;𝑠) denote the cost of setting the guide below the market-consistent benchmark. This cost
includes regulatory exposure, reputational cost, mismatch costs from attracting poorly matched buyers, and
bargaining or delay costs. We assume
𝐾 𝑀 (0;𝑠) = 0, 𝐾 𝑀 𝑑 (𝑑;𝑠) ≥ 0, 𝐾 𝑀 𝑑𝑑 (𝑑;𝑠) > 0.
Thus, the marginal cost of underquoting is non-negative and increasing in the degree of distortion.
The seller’s payoﬀ under mechanism 𝑀 is
Π 𝑀 (𝑑;𝑠) = Π 𝑀 0 (𝑠) +𝐵𝑀 (𝑑;𝑠) −𝐾 𝑀 (𝑑;𝑠),
where Π 𝑀 0 (𝑠) is the seller’s expected payoﬀ under market-consistent price guidance. The seller chooses
𝑑 ∈ [ 0, ¯𝑑],
where ¯𝑑 is the largest feasible downward deviation of the guide.
For later use, deﬁne the marginal net gain from increasing the degree of underquoting as
𝐺 𝑀 (𝑑;𝑠) =𝐵𝑀 𝑑 (𝑑;𝑠) −𝐾 𝑀 𝑑 (𝑑;𝑠).
11

Given the assumptions above,
𝐺 𝑀 𝑑 (𝑑;𝑠) =𝐵𝑀 𝑑𝑑 (𝑑;𝑠) −𝐾 𝑀 𝑑𝑑 (𝑑;𝑠) < 0.
Thus, the marginal net gain from underquoting is strictly decreasing in the degree of underquoting.
3.3 Auction and Private-treaty sales as diﬀerent Mechanisms
The key diﬀerence between auctions and private-treaty sales lies in the relative strength of the participation
beneﬁt and the information or bargaining cost.
In auction campaigns, additional bidders directly increase competitive pressure. A lower guide can
therefore have a high marginal beneﬁt. In addition, the seller can rely on a reserve price, which reduces the
risk of being forced to accept a low price. This weakens the cost of quoting low.
In private-treaty sales, a lower guide can still attract attention and generate oﬀers, but the ﬁnal price is
determined through negotiation rather than open ascending bidding. The seller cannot rely on the same public
competitive process to convert extra attention into ﬁnal-price pressure. Moreover, because oﬀers are made
relative to the advertised guide, a misleadingly low guide can generate low oﬀers, attract unsuitable buyers,
and create bargaining frictions.
We summarise this distinction with the following assumption.
Assumption 1. For all relevant𝑑 and𝑠,
𝐵 𝐴 𝑑 (𝑑;𝑠) ≥ 𝐵𝑃𝑇 𝑑 (𝑑;𝑠)
and
𝐾 𝐴 𝑑 (𝑑;𝑠) ≤ 𝐾 𝑃𝑇 𝑑 (𝑑;𝑠).
At least one of these inequalities is strict on a non-empty interval.
This assumption formalises the dual-role interpretation. The participation beneﬁt of lowering the guide is
larger in auctions, while the information, mismatch, and bargaining costs of lowering the guide are larger in
private-treaty sales.
12

Let
𝑑∗ 𝑀 (𝑠) ∈ arg max 𝑑 ∈ [0, ¯𝑑 ] Π 𝑀 (𝑑;𝑠)
denote the seller’s optimal degree of underquoting under mechanism 𝑀.
Proposition 1. Underquoting is optimal under mechanism𝑀 if the marginal participation beneﬁt of lowering
the guide at the market-consistent benchmark exceeds the marginal cost.
Proof. At the market-consistent benchmark, 𝑑 = 0 and the upper guide equals 𝜇(𝑠). The derivative of the
seller’s payoﬀ with respect to 𝑑 is
𝜕Π 𝑀 (𝑑;𝑠)
𝜕𝑑 =𝐵𝑀 𝑑 (𝑑;𝑠) −𝐾 𝑀 𝑑 (𝑑;𝑠) =𝐺 𝑀 (𝑑;𝑠).
Suppose
𝐺 𝑀 (0;𝑠) > 0.
Then, for a small increase Δ> 0 in the degree of underquoting, a ﬁrst-order Taylor expansion gives
Π 𝑀 (Δ;𝑠) − Π 𝑀 (0;𝑠) = Δ𝐺 𝑀 (0;𝑠) +𝑜(Δ).
Since𝐺 𝑀 (0;𝑠) > 0, this expression is positive for suﬃciently small Δ. Therefore 𝑑 = 0 cannot be optimal.
The seller strictly prefers a positive degree of underquoting, so 𝑑∗ 𝑀 (𝑠) > 0. Equivalently,𝑞∗ 𝑀 (𝑠) < 𝜇(𝑠).
Thus, underquoting is optimal whenever the marginal participation beneﬁt at the market-consistent benchmark
exceeds the marginal cost. □
This proposition shows why underquoting may occur even when price disclosure rules exist. Regulation
and reputational concerns enter through 𝐾 𝑀 (𝑑;𝑠), but they do not eliminate underquoting if the participation
value of a lower guide remains suﬃciently large.
Proposition 2. Auction guides are more strongly distorted downward than private-treaty guides.
Proof. By the mechanism-ordering assumption,
𝐵 𝐴 𝑑 (𝑑;𝑠) ≥ 𝐵𝑃𝑇 𝑑 (𝑑;𝑠)
13

and
𝐾 𝐴 𝑑 (𝑑;𝑠) ≤ 𝐾 𝑃𝑇 𝑑 (𝑑;𝑠)
for all relevant𝑑 and𝑠. Therefore,
𝐺 𝐴(𝑑;𝑠) =𝐵 𝐴 𝑑 (𝑑;𝑠) −𝐾 𝐴 𝑑 (𝑑;𝑠) ≥ 𝐵𝑃𝑇 𝑑 (𝑑;𝑠) −𝐾 𝑃𝑇 𝑑 (𝑑;𝑠) =𝐺 𝑃𝑇 (𝑑;𝑠).
Thus, at any given degree of underquoting, the marginal net gain from lowering the guide is weakly larger in
auctions than in private-treaty sales.
Since𝐺 𝑀 (𝑑;𝑠) is strictly decreasing in 𝑑, an interior optimum satisﬁes
𝐺 𝑀 (𝑑∗ 𝑀 (𝑠);𝑠) = 0.
Consider ﬁrst the case in which both optima are interior. Since
𝐺 𝑃𝑇 (𝑑∗ 𝑃𝑇 (𝑠);𝑠) = 0,
and since𝐺 𝐴(𝑑;𝑠) ≥ 𝐺 𝑃𝑇 (𝑑;𝑠) for all𝑑, it follows that 𝐺 𝐴(𝑑∗ 𝑃𝑇 (𝑠);𝑠) ≥ 0. Because 𝐺 𝐴(𝑑;𝑠) is strictly
decreasing in𝑑, the point at which 𝐺 𝐴(𝑑;𝑠) reaches zero must be weakly greater than 𝑑∗ 𝑃𝑇 (𝑠). Hence
𝑑∗ 𝐴(𝑠) ≥ 𝑑∗ 𝑃𝑇 (𝑠).
The same ordering also holds when one or both optima are at the boundary. If 𝑑∗ 𝑃𝑇 (𝑠) = 0, the result is
immediate because 𝑑∗ 𝐴(𝑠) ≥ 0. If 𝑑∗ 𝐴(𝑠) = ¯𝑑, the result is immediate because 𝑑∗ 𝑃𝑇 (𝑠) ≤ ¯𝑑. If 𝑑∗ 𝑃𝑇 (𝑠) = ¯𝑑,
then𝐺 𝑃𝑇 (𝑑;𝑠) ≥ 0 throughout the feasible interval, and therefore𝐺 𝐴(𝑑;𝑠) ≥ 0 throughout the same interval.
Hence𝑑∗ 𝐴(𝑠) = ¯𝑑 as well. Therefore, 𝑑∗ 𝐴(𝑠) ≥ 𝑑∗ 𝑃𝑇 (𝑠). Since𝑞∗ 𝑀 (𝑠) = 𝜇(𝑠) − 𝑑∗ 𝑀 (𝑠), this is equivalent to
𝑞∗ 𝐴(𝑠) ≤ 𝑞∗ 𝑃𝑇 (𝑠). Thus, auction guides are predicted to be lower relative to market-consistent value than
private-treaty guides. □
This proposition captures the main theoretical distinction. In auctions, the guide is primarily an entry
device. In private-treaty sales, the guide is more strongly disciplined by its information and bargaining role.
The theory therefore predicts more severe underquoting in auctions, but it does not predict that private-treaty
14

guides must be perfectly truthful.
3.4 Price guides and ﬁnal transaction prices
The preceding result compares optimal guides across sales mechanisms. We now derive an implication
for the probability that the ﬁnal transaction price falls within the quoted range.
Let the ﬁnal transaction price under mechanism 𝑀 be written as
𝑃𝑀 =𝑞∗ 𝑀 +𝑧 𝑀 +𝜀 𝑀,
where𝑞∗ 𝑀 is the optimal upper guide, 𝑧 𝑀 ≥ 0 is the expected gap between the ﬁnal price and the upper guide,
and𝜀 𝑀 is a mean-zero pricing shock. The term 𝑧 𝑀 captures the extent to which the ﬁnal price is expected to
exceed the guide.
Assume
𝑧 𝑀 =𝑎 𝑀𝑑∗ 𝑀 (𝑠), 𝑎 𝑀 > 0.
Thus, the expected ﬁnal-price gap is increasing in the degree of downward guide distortion. The parameter 𝑎 𝑀
captures how strongly guide distortion translates into a ﬁnal price above the guide. In auctions, this parameter
is likely to be larger because low guides attract bidders but the ﬁnal price is determined by competitive
bidding. In private-treaty sales, it may be smaller because the guide also anchors negotiation.
The quoted range is [𝑞∗ 𝑀 −𝑤,𝑞 ∗ 𝑀 ]. Conditional on guide width 𝑤, the ﬁnal price lies within the quoted
range if
𝑞∗ 𝑀 −𝑤 ≤ 𝑃𝑀 ≤𝑞∗ 𝑀.
Using the expression for 𝑃𝑀 , this event is equivalent to
−𝑤 ≤𝑧 𝑀 +𝜀 𝑀 ≤ 0.
Assumption 2. The shock 𝜀 𝑀 has a continuous distribution with density 𝑓 , symmetric around zero and
weakly decreasing in |𝑥| for𝑥 ≥ 0. Conditional on observed property characteristics and guide width, the
distribution of the shock is comparable across mechanisms.
Proposition 3. Final prices are less likely to fall within the quoted range in auctions than in private-treaty
15

sales when auction guides are more strongly distorted downward.
Proof. For a given guide width 𝑤, deﬁne
𝜙(𝑧;𝑤) = Pr(−𝑤 ≤𝑧 +𝜀 ≤ 0).
This is the probability that the ﬁnal price falls within the quoted range when the expected ﬁnal-price gap
above the guide is 𝑧. Using the distribution function 𝐹 of𝜀,
𝜙(𝑧;𝑤) =𝐹 (−𝑧) −𝐹 (−𝑤 −𝑧).
Diﬀerentiating with respect to 𝑧 gives
𝜕𝜙 (𝑧;𝑤)
𝜕𝑧 = −𝑓 (−𝑧) + 𝑓 (−𝑤 −𝑧).
By symmetry of 𝑓 ,
𝑓 (−𝑧) = 𝑓 (𝑧), 𝑓 (−𝑤 −𝑧) = 𝑓 (𝑤 +𝑧).
Since𝑤 ≥ 0 and𝑧 ≥ 0, we have𝑤 +𝑧 ≥𝑧. Because 𝑓 (𝑥) is weakly decreasing in 𝑥 for𝑥 ≥ 0,
𝑓 (𝑤 +𝑧) ≤ 𝑓 (𝑧).
Therefore,
𝜕𝜙 (𝑧;𝑤)
𝜕𝑧 = −𝑓 (𝑧) + 𝑓 (𝑤 +𝑧) ≤ 0.
Thus, the probability that the ﬁnal price falls within the quoted range is weakly decreasing in the expected gap
between the ﬁnal price and the upper guide.
From the previous proposition,
𝑑∗ 𝐴(𝑠) ≥ 𝑑∗ 𝑃𝑇 (𝑠).
If, in addition,
𝑎 𝐴𝑑∗ 𝐴(𝑠) ≥ 𝑎 𝑃𝑇𝑑∗ 𝑃𝑇 (𝑠),
16

then𝑧 𝐴 ≥𝑧 𝑃𝑇. Since𝜙(𝑧;𝑤) is weakly decreasing in 𝑧,
Pr(𝑃 𝐴 ∈ [𝑞∗ 𝐴 −𝑤,𝑞 ∗ 𝐴]) ≤ Pr(𝑃𝑃𝑇 ∈ [𝑞∗ 𝑃𝑇 −𝑤,𝑞 ∗ 𝑃𝑇 ]).
Therefore, conditional on comparable guide widths and observed property characteristics, ﬁnal prices are less
likely to fall within the quoted range in auction campaigns than in private-treaty campaigns. □
This proposition connects the theory directly to the empirical pattern that ﬁnal prices are substantially
less likely to fall within advertised guides in auctions than in private-treaty sales. In auctions, the guide is
more strongly used to attract participation, so ﬁnal prices often exceed the guide. In private-treaty sales, the
guide is more informative and more closely tied to the negotiation process, so transaction prices are more
likely to remain within the advertised range.
3.5 Underquoting incidence across mechanisms
The theory also delivers a prediction about underquoting incidence. Suppose properties diﬀer in the
strength of the participation incentive and in the cost of guide distortion. Let 𝜔 denote a property-speciﬁc or
local-market state, such as buyer demand, market tightness, or valuation uncertainty. The optimal degree of
underquoting is then
𝑑∗ 𝑀 (𝑠,𝜔 ).
A property is empirically classiﬁed as underquoted when the guide is suﬃciently below the market-consistent
benchmark and the ﬁnal transaction price conﬁrms that the guide was low relative to realised market value.
Let𝜏 >0 denote the minimum economically meaningful downward distortion required for a property to
be classiﬁed as underquoted. The probability of underquoting under mechanism 𝑀 can be written as
Pr(Underquoted | 𝑀) = Pr(𝑑∗ 𝑀 (𝑠,𝜔 ) >𝜏 ).
Proposition 4. Underquoting is more prevalent in auction campaigns than in private-treaty campaigns.
Proof. From the previous ordering result,
𝑑∗ 𝐴(𝑠,𝜔 ) ≥ 𝑑∗ 𝑃𝑇 (𝑠,𝜔 )
17

for each state (𝑠,𝜔 ). Therefore, for any threshold 𝜏 >0,
{𝑑∗ 𝑃𝑇 (𝑠,𝜔 ) >𝜏 } ⊆ {𝑑∗ 𝐴(𝑠,𝜔 ) >𝜏 }.
Taking probabilities over the distribution of (𝑠,𝜔 ) gives
Pr(𝑑∗ 𝑃𝑇 (𝑠,𝜔 ) >𝜏 ) ≤ Pr(𝑑∗ 𝐴(𝑠,𝜔 ) >𝜏 ).
Hence,
Pr(Underquoted | 𝑃𝑇) ≤ Pr(Underquoted | 𝐴).
Thus, underquoting is predicted to be more prevalent in auction campaigns than in private-treaty campaigns. □
This result does not imply that underquoting is absent in private-treaty sales. Lower guides can still attract
buyer attention and generate more oﬀers. The prediction is comparative: because the participation beneﬁt is
larger and the information cost is lower in auctions, underquoting should be more common and more severe
in auction campaigns.
3.6 Discussion and empirical implications
The model highlights the dual role of price guides in housing markets. The guide is both a participation
device and an information signal. The participation role is strongest in auctions, where additional bidders
directly increase competitive pressure and the seller can rely on a reserve price for downside protection. The
information role is strongest in private-treaty sales, where oﬀers are negotiated relative to the advertised guide
and misleadingly low guidance can create mismatch, delay, and bargaining costs.
The theoretical model is written in terms of the seller’s market-consistent benchmark, 𝜇(𝑠), and the
downward deviation of the upper guide, 𝑑 =𝜇(𝑠) −𝑞. These objects are not directly observed in the data. We
therefore use model-implied valuation intervals as empirical counterparts to the unobserved market-consistent
benchmark. The advertised upper guide corresponds to the observable guide chosen by the seller or agent,
while the hedonic and GWR valuation intervals provide guide-independent benchmarks based on observed
property characteristics and local market conditions.
The theory yields three empirical implications. First, Proposition 2 predicts that auction guides should be
18

positioned lower relative to market-consistent values than private-treaty guides. Empirically, this corresponds
to testing whether model-implied valuation bounds exceed advertised guide bounds more frequently in
auctions. Second, Proposition 3 predicts that ﬁnal transaction prices should be less likely to fall within
advertised guide ranges in auctions than in private-treaty sales. Empirically, this corresponds to comparing the
distribution of realised prices relative to advertised guide ranges across sale mechanisms. Third, Proposition
4 predicts that underquoting should be more prevalent in auction campaigns. Empirically, this corresponds to
comparing the conservative GWR-based underquoting indicator across auction and private-treaty sales, both
descriptively and after controlling for observable property and locational characteristics.
These empirical tests should be interpreted as reduced-form tests of the model’s observable implications
rather than as a structural estimation of the seller’s optimal guide choice. The data do not contain bidder
numbers, inspections, reserve prices or bargaining histories, so the participation channel itself is not directly
observed. Instead, the empirical analysis examines whether the observable patterns are consistent with that
channel: whether auction guides are more often below guide-independent valuation benchmarks, whether
auction prices are more likely to exceed the advertised range, and whether the resulting underquoting signal is
more prevalent in auction campaigns.
4 Institutional Setting and Data
Melbourne provides a particularly suitable setting for studying underquoting because it has substantial
activity under both auction and private-treaty sales, together with a strong auction tradition in which listing
guides may shape bidder expectations and participation. This section describes Melbourne’s housing market,
its institutional setting, and the data used in the empirical analysis. High transaction volumes, spatially
heterogeneous property values, and active disclosure regulation make Melbourne a useful setting for comparing
advertised guides with model-implied valuations. We ﬁrst outline the institutional context before describing
the datasets used to construct property-level valuation benchmarks.
4.1 Melbourne Housing Market
The empirical analysis focuses on Melbourne, one of Australia’s largest and most active housing markets.
Together with Sydney, Melbourne accounts for roughly 55% of the nation’s total residential property value,
19

making it a natural laboratory for studying price discovery, market frictions, and regulatory eﬀectiveness in
housing (CoreLogic, 2018). The combination of deep auction activity, high household leverage, and strong
spatial price gradients means that even modest distortions in listing behaviour can have systemically relevant
consequences for wealth distribution and market eﬃciency.
Underquoting is a particularly salient concern in Victoria’s auction -driven institutional environment.
Complaints to Consumer Aﬀairs Victoria (CA V) about misleading price guides rose sharply in the mid -2010s,
prompting strengthened disclosure rules and expanded enforcement (Österling, 2016). Despite these
interventions, underquoting remains a prominent feature of the regulatory docket. The dedicated Underquoting
Taskforce received more than 2,800 complaints between 2023 and 2024, an increase of roughly 70%, with a
growing share lodged by industry professionals rather than buyers (Victorian Government, 2024; Consumer
Aﬀairs Victoria, 2024). This pattern suggests that even compliant agents perceive strategic underquoting as a
source of competitive pressure.
Experience in New South Wales provides a useful external benchmark. Following the 2016 reform, NSW
Fair Trading continues to record high complaint volumes and to issue regular infringement notices (ABC
News, 2024; Trading, 2024). In both Victoria and New South Wales, complaints have grown more rapidly
than formal enforcement actions, indicating that underquoting remains diﬃcult to detect and substantiate ex
ante. From an economic perspective, this enforcement gap reﬂects a more fundamental measurement problem:
regulators largely observe listing ranges, realised prices, and a small set of agent -selected comparables, but
lack a systematic benchmark for the market-consistent value of individual properties.
This study frames underquoting in Melbourne as a problem of identifying systematic deviations of listing
guides from model -implied market values in a regulated housing market. By combining transaction-level
data with econometric valuation benchmarks, we provide evidence on the prevalence and spatial distribution
of patterns consistent with underquoting under the current Victorian disclosure regime.
4.2 Data
This study uses two linked datasets for detached house transactions in metropolitan Melbourne. The raw
2023–2024 sales ﬁle contains a larger set of completed house transactions. After restricting the sample to
detached houses and retaining observations with valid structural characteristics, land size, suburb-level rent,
contract prices and method-of-sale information, the ﬁnal training sample used in the pricing analysis contains
20

65,768 observations: 20,250 auction sales and 45,518 private-treaty sales. The second dataset is the 2025
evaluation sample, which contains properties for which advertised listing-price bounds and subsequent realised
transaction prices are both observed. 3 After applying the same validity requirements, the 2025 evaluation
sample contains 3,991 observations: 1,336 auction transactions and 2,655 private-treaty transactions. This
distinction is central because price guides serve diﬀerent functions in auction and private-treaty sales. In
private-treaty sales, the quoted range is more closely connected to the seller’s asking position and the
subsequent negotiation between buyer and seller. In auctions, however, the guide is set before the competitive
bidding process begins and can inﬂuence which buyers inspect the property, attend the auction and decide
to bid. Combining the two sale mechanisms would therefore blur two quite diﬀerent pricing environments.
For this reason, the valuation models and underquoting measures are estimated separately for auction and
private-treaty transactions.
The analysis is restricted to detached houses. This restriction reduces heterogeneity arising from
apartments, townhouses and other dwelling types, whose pricing may reﬂect diﬀerent ownership structures,
land components and buyer segments. Each property record contains core structural characteristics, including
the number of bedrooms, bathrooms and parking, land size, and realised contract price. The 2025 evaluation
sample additionally contains advertised lower and upper listing-price bounds. The data also include locational
information, including distances to the Melbourne CBD, public transport and education facilities, together with
suburb-level median rent. Median rent is used as a local-market indicator because it captures neighbourhood
demand conditions that are not fully summarised by physical housing attributes alone.
Geographic coordinates are used in the spatial modelling stage. For the 2023–2024 training sample, each
property is assigned the centroid coordinates of its corresponding Mesh Block 4. For the 2025 evaluation
sample, geocoded property-level coordinates derived from the property address are used. These coordinates
allow the GWR model to estimate locally varying pricing relationships across Melbourne rather than imposing
a common set of marginal eﬀects across all locations.
3The advertised guide variables refer to the most recent recorded lower and upper price bounds available before the recorded sale
outcome. The data do not contain the full sequence of guide revisions during the marketing campaign.
4Mesh Blocks are the smallest geographic areas deﬁned by the Australian Bureau of Statistics (ABS) within the Australian
Statistical Geography Standard (ASGS). Most residential Mesh Blocks contain approximately 30–60 dwellings. In this study, each
property in the training sample is assigned the centroid coordinates of its corresponding Mesh Block, providing spatial precision
while preserving conﬁdentiality and consistency with the ABS geographic hierarchy; see the ABS Census Geography Glossary.
21

Table 1: Summary statistics for Melbourne house sales in the 2023–2024 training sample, reported separately by
sale segment. Panel A reports auction transactions and Panel B reports private-treaty transactions. The table presents
the minimum, median, mean, maximum and standard deviation for key property characteristics, contract prices and
suburb-level median rent. Auction sales are properties recorded as sold at auction, while private-treaty sales are
negotiated non-auction transactions. Statistics are calculated after applying the validity ﬁlters used in the pricing
analysis.
Variable Min Median Mean Max SD
Panel A: Auction (𝑁 = 20, 250)
Property characteristics
Bedrooms 1 3 3.35 8 0.83
Bathrooms 1 2 1.77 6 0.67
Parking 0 2 1.69 6 0.93
Land size (m 2) 31 576 555.07 2,999 247.04
Prices (AUD)
Contract price (AUD) 285,000 1,090,000 1,191,584 2,800,000 507,057
Suburb-level indicator
Median rent (AUD per week) 251.14 530.00 539.51 1,375.00 85.58
Panel B: Private-treaty sales (𝑁 = 45, 518)
Property characteristics
Bedrooms 1 3 3.40 8 0.79
Bathrooms 1 2 1.85 6 0.61
Parking 0 2 1.77 6 0.89
Land size (m 2) 33 553 588.84 2,996 338.04
Prices (AUD)
Contract price (AUD) 200,000 762,000 902,680 2,800,000 421,027
Suburb-level indicator
Median rent (AUD per week) 317.62 490.00 506.11 1,375.00 84.56
Table 1 reports summary statistics for the 2023–2024 training sample. Auction properties are more
expensive than private-treaty properties in the training period. The median auction contract price is AUD1.09
million, compared with AUD762,000 for private-treaty sales, and the mean auction price is also substantially
higher at AUD1.19 million. The physical characteristics are broadly similar across segments, but auction
dwellings are slightly smaller on average in bathrooms and land size. Auction properties have a mean of 3.35
bedrooms, 1.77 bathrooms and 555 m 2 of land, while private-treaty properties have 3.40 bedrooms, 1.85
bathrooms and 589 m 2 of land. The auction sample is also located in somewhat higher-rent suburbs, with a
median suburb-level rent of AUD530 per week compared with AUD490 for private-treaty sales. This suggests
22

that auctions are more concentrated in higher-value local markets. 5
Table 2 summarises the 2025 evaluation sample. The auction segment again has higher prices than private-
treaty sales. The median realised auction price is AUD1.012 million, compared with AUD820,000 for
private-treaty sales. The advertised price ranges also diﬀer sharply across segments. In auctions, the median
lower and upper listing bounds are AUD900,000 and AUD990,000, while the median realised sale price is
AUD1.012 million.
Figure 1: Spatial distribution of the 2023–2024 training sample ( 𝑁 = 65,768, left) and the 2025 evaluation
sample (𝑁 = 3,991, right) across Greater Melbourne. Training-sample locations are represented by Mesh
Block centroids, while evaluation-sample locations are based on geocoded property addresses.
5Note that the analysis focuses on completed transactions with matched advertised guides and realised sale prices. Consequently,
withdrawn, unsold, or unmatched passed-in properties are outside the evaluation sample. The ﬁndings therefore relate to successfully
completed sales.
23

Table 2: Summary statistics for Melbourne house listings and sales in the 2025 evaluation sample. Panel A reports
auction transactions and Panel B reports private-treaty transactions. The table presents property characteristics,
advertised price bounds, realised contract prices and suburb-level median rent. One private-treaty observation with
reversed bounds was corrected before calculation.
Variable Min Median Mean Max SD
Panel A: Auction (𝑁 = 1, 336)
Property characteristics
Bedrooms 1 3 3.55 7 0.76
Bathrooms 1 2 1.76 4 0.62
Parking 1 2 2.26 6 0.96
Land size (m 2) 127 604 610.05 2,000 194.57
Prices (AUD)
Listing price (min quoted) 320,000 900,000 998,103 2,980,000 401,369
Listing price (max quoted) 350,000 990,000 1,074,020 2,980,000 428,411
Contract price (AUD) 370,000 1,012,500 1,110,517 2,860,000 438,677
Suburb-level indicator
Median rent (AUD per week) 390.00 540.00 552.73 980.00 71.67
Panel B: Private-treaty sales (𝑁 = 2, 655)
Property characteristics
Bedrooms 1 4 3.59 8 0.72
Bathrooms 1 2 1.84 4 0.57
Parking 1 2 2.26 6 0.97
Land size (m 2) 38 608 653.38 2,590 313.89
Prices (AUD)
Listing price (min quoted) 202,500 790,000 899,393 3,000,000 355,456
Listing price (max quoted) 250,000 850,000 959,393 3,200,000 378,603
Contract price (AUD) 235,000 820,000 925,960 2,800,000 357,715
Suburb-level indicator
Median rent (AUD per week) 390.00 525.00 537.30 1,250.00 75.23
This gap is consistent with the later evidence that auction properties frequently sell above the advertised
maximum. In private-treaty sales, the median lower and upper listing bounds are AUD790,000 and
AUD850,000, compared with a median realised price of AUD820,000, indicating a more balanced relationship
between listed and realised prices. The 2025 auction and private-treaty samples are similar in bedrooms,
bathrooms and parking, but private-treaty properties have larger median land size, at 608 m 2 compared with
604 m2 for auctions.
24

Extreme observations are removed using the same trimming approach applied in the pricing analysis.
Observations with extreme log contract prices or extreme log land sizes are excluded to reduce the inﬂuence
of outliers on the hedonic and GWR estimates. In addition to this log-price and log-land-size trimming, the
sample is restricted to transactions with contract prices and land sizes lying within the support used for model
estimation. This removes extremely high-value transactions and unusually large land parcels that are unlikely
to be comparable with the suburban detached-house market analysed in this paper. 6 For both datasets,
suburb-level median rent sourced from CoreLogic is merged to proxy local housing market conditions. As
shown in Figure 1, the spatial concentration of observations varies across Melbourne.
5 Empirical analysis
This section takes the theoretical predictions to the data in three steps. First, we construct independent
valuation benchmarks for each sale mechanism using completed 2023–2024 transactions and apply them out
of sample to the 2025 evaluation sample. The purpose is to obtain model-implied valuation ranges that do not
depend on the advertised guide. Second, we compare advertised guide bounds with model-implied valuation
bounds and realised transaction prices. This allows us to examine whether auction guides are positioned
lower relative to estimated market values and whether auction outcomes are less likely to remain within the
quoted range. Third, we use a conservative GWR-based classiﬁcation rule to identify likely underquoted
properties and compare incidence across auction and private-treaty sales. The empirical analysis therefore
links directly to the propositions: auction guides should be more downward distorted, auction prices should
less often fall within the quoted range, and underquoting should be more prevalent in auction campaigns.
5.1 Fixed-eﬀects hedonic benchmark
As a ﬁrst valuation benchmark, we estimate a ﬁxed-eﬀects hedonic pricing model in the spirit of Rosen
(1974). Hedonic models are widely used in housing economics to relate transaction prices to observed
structural and locational characteristics, such as dwelling size, land size and neighbourhood attributes (see,
e.g., Blomquist and Worley (1981); Sheppard (1999); Diao and Ferreira (2010); Diao et al. (2016)). In this
6Observations are trimmed symmetrically at ﬁve standard deviations from the sample mean of log contract price and log land size.
Trimming is conducted after log transformation to reduce the inﬂuence of scale and skewness. Additional support restrictions are
applied to ensure that the estimation and evaluation samples remain within the suburban detached-house market considered in the
analysis.
25

study, the hedonic model provides a transparent benchmark against which the more ﬂexible spatial model can
be compared.
The model is estimated on completed transactions from the 2023–2024 training sample and then used to
predict prices for the 2025 evaluation sample. Estimation is conducted separately by sale mechanism. The
auction benchmark is estimated using only auction sales, while the private-treaty benchmark is estimated
using only private-treaty sales. This avoids imposing a common pricing relationship on two diﬀerent sale
environments and means that method of sale is used to deﬁne the estimation sample rather than entering the
regression as an explanatory variable.
Let the transaction price of property 𝑖 depend on observed structural attributes A𝑖, locational and
neighbourhood characteristics N𝑖, and an idiosyncratic error term:
Price𝑖 = 𝑓 (A𝑖, N𝑖) +𝑣𝑖. (1)
We operationalise this relationship using a log-linear ordinary least squares speciﬁcation. The dependent
variable is the logarithm of the realised contract price. The main explanatory variables are the number of
bedrooms, bathrooms and parking, log land size, distance to public transport and distance to the Melbourne
CBD. Suburb ﬁxed eﬀects absorb persistent neighbourhood-level diﬀerences, while seasonal indicators
capture common within-year variation in market conditions. The baseline hedonic benchmark is estimated in
log-linear form as
ln(SalePrice𝑖) =𝛽0 +𝛽1Bedrooms𝑖 +𝛽2Bathrooms𝑖 +𝛽3Parking𝑖
+𝛽4 ln(LandSize𝑖) + 𝛽5 ln(MedianRent𝑠 (𝑖) )
+𝛽6DistTransport𝑖 +𝛽7DistCBD𝑖 +𝜆𝑞 (𝑖) +𝛿ℓ (𝑖) +𝑣𝑖. (2)
Here,𝜆𝑞 (𝑖) denotes seasonal ﬁxed eﬀects and𝛿ℓ (𝑖) denotes suburb ﬁxed eﬀects. The term MedianRent𝑠 (𝑖)
is measured at the suburb level and varies across both suburbs and years. The model is estimated separately
within each sale segment: the auction model is estimated using only auction transactions, while the private-
treaty model is estimated using only private-treaty transactions. The method-of-sale variable is therefore used
to deﬁne the estimation sample rather than being included as an explanatory variable.
The revised speciﬁcation uses the same core structural and locational covariates as the preferred GWR
26

benchmark, while retaining suburb ﬁxed eﬀects in the global hedonic model. The structural controls are
bedrooms, bathrooms, parking and land size, with land size entering in logarithmic form. Suburb-level
median rent controls for local rental-market conditions and broader neighbourhood desirability. The locational
controls include distance to public transport and distance to the Melbourne CBD. Seasonal indicators account
for within-year variation in market conditions, while suburb ﬁxed eﬀects capture broad spatial diﬀerences.
The ﬁtted values from Equation (2) provide model-implied expected property values for the 2025
evaluation sample. For each 2025 property, the estimated log price is exponentiated to obtain the predicted
price level. These predictions are then used to construct model-implied valuation intervals, which are
compared with advertised listing ranges and realised transaction prices. Advertised guide prices are not used
as explanatory variables in the hedonic speciﬁcation; they enter only at the comparison stage when assessing
whether public price guidance is low relative to model-implied market values.
For the real-time adjustment exercise, geographic coordinates are retained in the dataset but are not
included directly in the hedonic regression equations. 7 Instead, latitude and longitude are used after prediction
to identify nearby prior transactions and construct local prediction-error adjustments. This adjustment is
applied to the model prediction rather than entering the OLS estimation equation itself.
For private-treaty transactions, Table 3 shows that the global hedonic benchmark captures several standard
price gradients. Bedrooms, bathrooms and parking are all positively associated with sale prices, indicating
that larger and better-equipped dwellings command higher transaction prices. Land size also enters positively
and signiﬁcantly, suggesting that additional land area is capitalised into private-treaty prices once other
structural and locational characteristics are controlled for. Suburb-level median rent is strongly positive,
consistent with higher-sale-price properties being located in stronger local rental markets and more desirable
neighbourhoods.
7Geographic coordinates are measured using Mesh Block centroids for the training sample and property-level geocoded coordinates
for the evaluation sample.
27

Table 3: Private-treaty sales: OLS coeﬃcient estimates from the model ﬁtted to the 2023–2024 training sample. The
dependent variable is log sale price. The table reports coeﬃcient estimates, conventional standard errors, 𝑡-statistics and
estimation-sample diagnostics for the unadjusted global OLS benchmark. *, ** and *** denote signiﬁcance at the 10%,
5% and 1% levels, respectively. Locally adjusted 2025 out-of-sample prediction performance is reported separately in
Table 5.
Variable Estimate Std. Error 𝑡-stat. 𝑝-value
Intercept 4.6200*** 0.0547 84.534 0.0000
Bedrooms 0.0652*** 0.0020 33.278 0.0000
Bathrooms 0.1358*** 0.0025 53.985 0.0000
Parking 0.0154*** 0.0016 9.844 0.0000
ln(Land size) 0.1692*** 0.0027 63.332 0.0000
ln(Median rent) 1.2145*** 0.0087 139.654 0.0000
Distance to transport -0.0033*** 0.0002 -16.670 0.0000
Distance to CBD -0.0021*** 0.0000 -47.863 0.0000
Autumn 0.0014 0.0036 0.399 0.6903
Winter -0.0007 0.0037 -0.200 0.8416
Summer -0.0095** 0.0038 -2.531 0.0114
Season indicators Y es
Suburb ﬁxed eﬀects Y es
Adjusted𝑅2 0.4906
Akaike information criterion (AIC) 13,950.66
Bayesian information criterion (BIC) 14,055.37
The locational coeﬃcients have the expected signs: distance to public transport and distance to the
Melbourne CBD are both negative and highly signiﬁcant, indicating that prices decline as properties become
less accessible to transport amenities and farther from central Melbourne. The seasonal indicators are
generally weak, although summer transactions are associated with slightly lower prices. The adjusted 𝑅2
of 0.491 indicates that the global OLS model captures broad price variation in the training sample, but the
model remains a single global benchmark and cannot fully capture local variation in Melbourne housing
prices. This motivates the spatially adaptive GWR benchmark, which allows pricing relationships to vary
locally across Melbourne rather than imposing one common set of coeﬃcients. 8
For auction transactions, Table 4 shows a broadly similar hedonic structure, although the estimated
gradients diﬀer from the private-treaty segment. Bedrooms and bathrooms are positively and highly
signiﬁcantly associated with sale prices, while parking is weakly negative and only marginally signiﬁcant.
8Median rent is measured at the suburb level and matched to each transaction by suburb and year. Because the preferred
speciﬁcation does not include suburb ﬁxed eﬀects, median rent is used as an observable local-market control rather than being
separately identiﬁed from within-suburb variation after ﬁxed eﬀects.
28

Land size enters positively and signiﬁcantly, indicating that larger lots are capitalised into auction prices after
controlling for other property and location characteristics.
Table 4: Auction sales: OLS coeﬃcient estimates from the model ﬁtted to the 2023–2024 training sample. The
dependent variable is log sale price. The table reports coeﬃcient estimates, conventional standard errors, 𝑡-statistics and
estimation-sample diagnostics for the unadjusted global OLS benchmark. *, ** and *** denote signiﬁcance at the 10%,
5% and 1% levels, respectively. Locally adjusted 2025 out-of-sample prediction performance is reported separately in
Table 5.
Variable Estimate Std. Error 𝑡-stat. 𝑝-value
Intercept 4.1155*** 0.0931 44.193 0.0000
Bedrooms 0.0590*** 0.0030 19.434 0.0000
Bathrooms 0.1215*** 0.0036 33.643 0.0000
Parking -0.0040* 0.0024 -1.684 0.0922
ln(Land size) 0.1550*** 0.0047 33.316 0.0000
ln(Median rent) 1.3740*** 0.0140 98.400 0.0000
Distance to transport -0.0037*** 0.0006 -6.177 0.0000
Distance to CBD -0.0101*** 0.0002 -50.036 0.0000
Autumn -0.0053 0.0054 -0.978 0.3280
Winter -0.0056 0.0055 -1.014 0.3107
Summer -0.0135** 0.0060 -2.243 0.0249
Season indicators Y es
Suburb ﬁxed eﬀects Y es
Adjusted𝑅2 0.5008
Akaike information criterion (AIC) 7,745.53
Bayesian information criterion (BIC) 7,840.52
Suburb-level median rent is also strongly positive, suggesting that auction prices are higher in stronger
local rental markets and more desirable neighbourhoods. The locational gradients have the expected signs:
distance to public transport and distance to the Melbourne CBD are both negative and statistically signiﬁcant,
implying that auction prices decline as properties become less accessible to transport amenities and farther
from central Melbourne. Seasonal eﬀects are limited, although summer transactions are associated with
slightly lower prices. The adjusted 𝑅2 of 0.501 indicates that the global OLS benchmark captures broad
price variation in the auction training sample, but the model remains deliberately transparent and global. The
remaining spatial heterogeneity in housing prices motivates the use of the GWR benchmark.
29

5.1.1 Locally adjusted OLS predictions
The 2025 prediction metrics in Table 5 are based on locally adjusted OLS predictions, not the unadjusted
ﬁtted values summarised in Tables 3 and 4. For each 2025 property 𝑖 in sale segment 𝑚, the global OLS
model ﬁrst produces an unadjusted log-price prediction ˆ𝑦𝑂𝐿𝑆 𝑖𝑚 . We then apply a real-time comparable-sales
correction based on prior completed 2025 transactions from the same sale segment. For each prior comparable
transaction 𝑗, the log prediction error is
𝑒 𝑗 = log(𝑃 𝑗) − ˆ𝑦𝑂𝐿𝑆 𝑗𝑚 ,
where ˆ𝑦𝑂𝐿𝑆 𝑗𝑚 is generated using the segment-speciﬁc OLS model estimated only on the 2023–2024 training
sample.
For private-treaty properties, the comparable set ﬁrst searches for prior sales in the same suburb and with
the same bedroom count within the previous 60 days, with a 3 km spatial fallback. For auction properties, the
comparable set ﬁrst searches for prior sales in the same suburb and with the same bedroom count within the
previous 90 days, with a 5 km spatial fallback. Only transactions with sale dates preceding the sale date of
property𝑖 are used. The local adjustment is the median prediction error among the selected comparables:
~𝑒𝑂𝐿𝑆 𝑖 = median{𝑒 𝑗 : 𝑗 ∈ C 𝑂𝐿𝑆 𝑖 }.
If no qualifying prior comparable is available, the adjustment is set to zero. The adjusted OLS prediction is
then
ˆ𝑦𝑎𝑑 𝑗,𝑂𝐿𝑆 𝑖𝑚 = ˆ𝑦𝑂𝐿𝑆 𝑖𝑚 + ~𝑒𝑂𝐿𝑆 𝑖 , ˆ𝑃𝑎𝑑 𝑗,𝑂𝐿𝑆 𝑖𝑚 = exp ( ˆ𝑦𝑎𝑑 𝑗,𝑂𝐿𝑆 𝑖𝑚 ) .
Thus, Table 5 evaluates the out-of-sample accuracy of the locally adjusted OLS predictions used in the
guide-classiﬁcation exercise.
30

Table 5: Out-of-sample prediction accuracy for the 2025 test dataset based on the locally adjusted global OLS hedonic
pricing model. The table reports standard forecast evaluation metrics measuring prediction errors in both absolute dollar
terms and relative percentage terms. Prediction accuracy is reported separately for auction and private-treaty transactions
in the 2025 evaluation sample. Absolute error P50 is the median absolute diﬀerence between realised and predicted
transaction prices. MAPE is the median absolute percentage error. Log error is deﬁned as log(𝑃actual) − log(𝑃predicted).
Metric Value
Panel A: Auction
Absolute error P50 (median absolute error, AUD) 138,599.47
Median Absolute Percentage Error (%) 13.60
Median log error -0.0256
Median absolute log error 0.1348
Panel B: Private-treaty sales
Absolute error P50 (median absolute error, AUD) 90,245.51
Median Absolute Percentage Error (%) 10.98
Median log error -0.0095
Median absolute log error 0.1086
Table 5 reports the 2025 out-of-sample accuracy of the locally adjusted global OLS benchmark. These
metrics should be distinguished from the estimation-sample diagnostics reported in Tables 3 and 4. 9
The private-treaty model performs somewhat better in typical error terms. The median absolute error
is AUD 90,246 and the median absolute percentage error is 10.98%, both below the corresponding auction
errors. Overall, the locally adjusted OLS model provides a useful transparent benchmark, but its prediction
errors remain large enough to motivate the spatially adaptive GWR benchmark.
Table 6 compares realised 2025 sale prices with two alternative price ranges: the advertised agent range
and the OLS-implied valuation range. The OLS range is not intended to be a formal statistical prediction
interval. It is a model-implied guide range with the same 10% upper-to-lower width used in the classiﬁcation
exercise. The table therefore provides a transparent comparison between the public guide supplied to buyers
and a benchmark guide constructed from observed housing characteristics and local-market information. 10
For private-treaty sales, 56.05% of realised prices fall within the advertised agent range, while 19.62%
are above the advertised maximum and 24.33% are below the advertised minimum. This relatively balanced
9Log error is deﬁned as log(𝑃actual) − log(𝑃predicted).
10The 10% upper-to-lower valuation width is chosen to align the model-implied valuation interval with the institutional logic of
advertised price guides. Victorian underquoting regulation requires agents to justify price guidance using comparable sales and local
market information, and policy discussion of underquoting commonly treats a 10% guide range or a sale price more than 10% above
the guide as an economically meaningful threshold. The purpose of the 10% interval in this paper is therefore not to deﬁne legal
underquoting, but to place the model-implied benchmark on a comparable scale to the advertised guide range observed by buyers.
This also ensures that the OLS and GWR benchmarks are evaluated using the same proportional interval width.
31

pattern is consistent with the role of the private-treaty guide as a bargaining range. In contrast, the OLS-implied
range shows greater dispersion, with 24.86% of sales falling within the predicted range, 34.65% above it, and
40.49% below it. This pattern reﬂects both the limitations of a global hedonic benchmark and the deliberately
narrow 10% range imposed around the predicted price.
The auction segment shows a much sharper asymmetry in the advertised guide comparison. Around
65.72% of auction sales sell above the advertised maximum, while only 8.01% sell below the advertised
minimum. This pattern is consistent with the idea that auction guides often sit below eventual transaction
prices and may help attract bidder participation before the auction. By contrast, the OLS-implied auction
range classiﬁes 19.01% of sales inside the predicted range, 36.08% above it and 44.91% below it. The OLS
benchmark therefore does not reproduce the strong upward asymmetry observed in advertised auction guides.
However, the listing-to-sale gap alone is not suﬃcient to identify underquoting, since ﬁnal auction prices
also reﬂect competition among bidders and market conditions at the time of sale. The OLS-implied range
provides a useful transparent benchmark comparison, but its global structure and remaining prediction errors
motivate the use of GWR as the main local valuation benchmark.
Table 6: The table classiﬁes realised 2025 sale prices relative to advertised agent guides and OLS-implied guide ranges.
The OLS-implied range is constructed around the predicted price ˆ𝑃. The lower and upper bounds are ˆ𝑃/ √ 1.10 and
ˆ𝑃 √ 1.10, so the ratio of the upper bound to the lower bound is 1.10. Percentages are calculated within each sale segment.
Benchmark Category Count Percent (%)
Panel A: Private-treaty sales
Agent guide Price between listing minimum and maximum 1,488 56.05
Agent guide Price above listing maximum 521 19.62
Agent guide Price below listing minimum 646 24.33
OLS Price between predicted minimum and maximum 660 24.86
OLS Price above predicted maximum 920 34.65
OLS Price below predicted minimum 1,075 40.49
Panel B: Auction
Agent guide Price between listing minimum and maximum 351 26.27
Agent guide Price above listing maximum 878 65.72
Agent guide Price below listing minimum 107 8.01
OLS Price between predicted minimum and maximum 254 19.01
OLS Price above predicted maximum 482 36.08
OLS Price below predicted minimum 600 44.91
32

5.2 Geographically weighted regression (GWR)
To allow for spatial heterogeneity in housing price determinants, we next estimate a geographically
weighted regression (GWR) model, which extends the hedonic framework by allowing the marginal eﬀects of
housing attributes to vary across space (Brunsdon et al., 1996; Fotheringham et al., 2002, 2009). Unlike the
ﬁxed-eﬀects hedonic model, which imposes common marginal eﬀects across all suburbs, the GWR framework
permits the pricing of structural and locational characteristics to diﬀer across local housing submarkets. This
ﬂexibility is particularly relevant in Melbourne, where the value of housing attributes may vary substantially
across locations. The model is estimated on completed 2023–2024 transactions and then applied out of
sample to the 2025 evaluation sample. As in the ﬁxed-eﬀects hedonic analysis, the estimation is conducted
separately within each sale segment. The auction model is estimated using auction transactions only, while
the private-treaty model is estimated using private-treaty transactions only. The method-of-sale variable is
therefore used to deﬁne the estimation sample rather than being included as a regressor.
The GWR speciﬁcation is
ln(SalePrice𝑖) =𝛽0(𝑥𝑖,𝑦 𝑖) + X′ 𝑖 𝜷(𝑥𝑖,𝑦 𝑖) +𝑣𝑖, (3)
where (𝑥𝑖,𝑦 𝑖) denotes the geographic coordinates of property 𝑖, and 𝜷(𝑥𝑖,𝑦 𝑖) is a vector of location-speciﬁc
coeﬃcients. Unlike the ﬁxed-eﬀects hedonic model, which imposes a common set of marginal eﬀects across
all locations, the GWR model allows the relationship between property attributes and sale prices to vary
spatially.
The covariate vector X𝑖 contains the same parsimonious core variables used in the revised hedonic
benchmark. These include structural characteristics, local market conditions, accessibility measures, seasonal
indicators and land-use controls. Speciﬁcally, the structural and locational variables are bedrooms, bathrooms,
parking, log land size, log suburb-level median rent, distance to public transport and distance to the Melbourne
CBD. Seasonal indicators are included for autumn, winter and summer, with spring as the omitted category.
Land-use indicators are included where available, with rare categories grouped into an “Other” category to
improve estimation stability. The ﬁtted log prices are exponentiated to obtain model-implied expected property
values for the 2025 evaluation sample. These predicted values are then used to construct model-implied
valuation intervals, which are compared with advertised listing ranges and realised transaction prices in the
33

underquoting analysis.
5.2.1 Construction of the GWR valuation interval.
Because the underquoting classiﬁcation depends on the model-implied valuation bounds, we construct the
GWR interval explicitly in ﬁve steps. Let 𝑖 denote a 2025 evaluation property in sale segment 𝑚 ∈ {𝐴,𝑃𝑇 },
where𝐴 denotes auction and 𝑃𝑇 denotes private-treaty sales. Let ˆ𝑦𝐺𝑊 𝑅 𝑖𝑚 be the GWR prediction for log sale
price, obtained from the segment-speciﬁc GWR model estimated on 2023–2024 completed transactions. The
corresponding price-level prediction is
ˆ𝑃𝐺𝑊 𝑅 𝑖𝑚 = exp ( ˆ𝑦𝐺𝑊 𝑅 𝑖𝑚 ) .
First, we construct a raw model-implied guide interval around the GWR prediction using the same 10%
upper-to-lower width used for the hedonic benchmark. Deﬁne
ℎ = 1 2 log(1.10).
The initial GWR bounds are
ˆ𝑃 0,𝐺𝑊 𝑅 𝑖𝑚 = exp ( ˆ𝑦𝐺𝑊 𝑅 𝑖𝑚 −ℎ ) , ˆ𝑃 0,𝐺𝑊 𝑅 𝑖𝑚 = exp ( ˆ𝑦𝐺𝑊 𝑅 𝑖𝑚 +ℎ ) .
Equivalently,
ˆ𝑃 0,𝐺𝑊 𝑅 𝑖𝑚 = ˆ𝑃𝐺𝑊 𝑅 𝑖𝑚√ 1.10 , ˆ𝑃 0,𝐺𝑊 𝑅 𝑖𝑚 = ˆ𝑃𝐺𝑊 𝑅 𝑖𝑚 √ 1.10,
so that
ˆ𝑃
0,𝐺𝑊 𝑅
𝑖𝑚
ˆ𝑃 0,𝐺𝑊 𝑅 𝑖𝑚 = 1.10.
Second, we construct a local real-time prediction-error adjustment using only prior completed sales. 11
For each 2025 property 𝑖 with sale date 𝑡𝑖, we ﬁrst search for comparable transactions 𝑗 from the same sale
11The comparable pool consists only of completed 2025 evaluation-sample transactions whose sale dates precede 𝑡𝑖. For each
comparable transaction 𝑗, the associated prediction is generated out of sample using the segment-speciﬁc GWR model estimated only
on the 2023–2024 training data. The realised price of comparable transaction 𝑗 is therefore not used in estimating its own GWR
prediction. This ensures that the local prediction-error adjustment uses only information that would have been available before the
sale of property 𝑖 and avoids in-sample residuals from the GWR training period.
34

segment, same suburb and same bedroom count, with sale dates satisfying
0<𝑡 𝑖 −𝑡 𝑗 ≤ 90 days.
For each comparable sale 𝑗, deﬁne the log prediction error
𝑒 𝑗 = log(𝑃 𝑗) − log( ˆ𝑃𝐺𝑊 𝑅 𝑗𝑚 ),
where𝑃 𝑗 is the realised sale price and ˆ𝑃𝐺𝑊 𝑅 𝑗𝑚 is the GWR prediction for that prior transaction. Thus, only
information that would have been available before the 2025 sale of property 𝑖 is used.
Third, if no same-suburb and same-bedroom prior comparable is available within the 90-day window, we
use a spatial fallback rule. 12 The comparable set is expanded to prior transactions from the same sale segment
and same bedroom count located within 3 km of property 𝑖, again requiring
0<𝑡 𝑖 −𝑡 𝑗 ≤ 90 days.
The adjustment is based on all prior transactions satisfying the relevant rule; the number of comparable sales
is therefore allowed to vary by property. If no prior comparable is available even after the 3 km fallback, no
local adjustment is applied and the adjustment term is set to zero.
Fourth, the local adjustment for property 𝑖 is the median prior log prediction error:
~𝑒𝑖 = median{𝑒 𝑗 : 𝑗 ∈ C𝑖 },
where C𝑖 denotes the selected comparable set. If C𝑖 is empty, ~𝑒𝑖 = 0. The adjusted GWR prediction is then
ˆ𝑦𝑎𝑑 𝑗,𝐺𝑊 𝑅 𝑖𝑚 = ˆ𝑦𝐺𝑊 𝑅 𝑖𝑚 + ~𝑒𝑖,
or, equivalently in price levels,
ˆ𝑃𝑎𝑑 𝑗,𝐺𝑊 𝑅 𝑖𝑚 = ˆ𝑃𝐺𝑊 𝑅 𝑖𝑚 exp(~𝑒𝑖).
12The 90-day window and 3-km fallback radius are chosen to approximate the type of recent and local comparable-sales information
available to agents and buyers at the time of listing, while preserving enough observations for a property-level real-time adjustment.
As a robustness check, we re-estimate the main underquoting classiﬁcation using alternative interval widths and comparable-sales
windows. The auction–private-treaty ranking remains unchanged.
35

Thus, the comparable-sales correction shifts the GWR midpoint upward or downward according to recent
local forecast errors.
Fifth, the ﬁnal GWR valuation interval is constructed around the adjusted GWR prediction using the same
10% upper-to-lower width:
ˆ𝑃 𝐺𝑊 𝑅 𝑖𝑚 = exp ( ˆ𝑦𝑎𝑑 𝑗,𝐺𝑊 𝑅 𝑖𝑚 −ℎ ) , ˆ𝑃 𝐺𝑊 𝑅 𝑖𝑚 = exp ( ˆ𝑦𝑎𝑑 𝑗,𝐺𝑊 𝑅 𝑖𝑚 +ℎ ) .
Equivalently,
ˆ𝑃 𝐺𝑊 𝑅 𝑖𝑚 = ˆ𝑃𝑎𝑑 𝑗,𝐺𝑊 𝑅 𝑖𝑚√ 1.10 , ˆ𝑃 𝐺𝑊 𝑅 𝑖𝑚 = ˆ𝑃𝑎𝑑 𝑗,𝐺𝑊 𝑅 𝑖𝑚 √ 1.10.
The proportional width of the GWR interval is therefore ﬁxed at 10% for every property, while the dollar
width varies with the adjusted predicted price. Advertised guide prices are not used in estimating the GWR
model, constructing the local error adjustment, or forming the GWR valuation interval. 13 The GWR-based
underquoting indicator is then deﬁned as
𝑈𝐺𝑊 𝑅 𝑖 = 1 { 𝑃𝑖 > 𝐿𝑖 and𝑃𝑖 > ˆ𝑃 𝐺𝑊 𝑅 𝑖𝑚 } ,
where𝑃𝑖 is the realised sale price, 𝐿𝑖 is the advertised upper guide, and ˆ𝑃 𝐺𝑊 𝑅 𝑖𝑚 is the comparable-adjusted
lower bound of the GWR valuation interval. This screened classiﬁcation does not identify a property as
underquoted solely because its realised sale price exceeds the advertised range. It additionally requires the
realised price to exceed the lower bound of the guide-independent model-implied valuation interval, thereby
reducing reliance on the guide-to-sale price gap alone. Table 7 shows substantial spatial variation in the
auction pricing equation. The GWR coeﬃcients should not be interpreted as average marginal eﬀects because
they vary locally across Melbourne. The table is therefore best interpreted as evidence on the distribution of
local pricing relationships rather than as a direct comparison of individual coeﬃcients.
For bedrooms, the median local coeﬃcient is 0.0498, with an interquartile range from -0.0030 to 0.1112.
For bathrooms, the median is 0.1195, with an interquartile range from 0.0521 to 0.1944. These estimates
indicate that the price gradients associated with dwelling characteristics are generally positive but vary
across local housing submarkets. Land size also displays a positive local gradient. The median coeﬃcient
13The adjustment is based on all prior transactions satisfying the relevant rule; the number of comparable sales is therefore allowed
to vary by property.
36

on ln(Land size) is 0.2614, with an interquartile range from 0.1179 to 0.3997, suggesting that land area
is capitalised into auction prices, but with diﬀerent intensity across locations. Local market conditions,
measured by ln(Median rent), also vary across space, with a median coeﬃcient of 0.0626 and an interquartile
range from -0.4807 to 0.5997.
Distance-related eﬀects also vary across locations. The median coeﬃcient on distance to transport is
0.0076, with an interquartile range from -0.2246 to 0.2316, while the median coeﬃcient on distance to the
CBD is -0.0202, with an interquartile range from -0.2248 to 0.1968. These patterns show that accessibility
gradients are not constant across Melbourne, which is precisely the type of spatial heterogeneity that a global
OLS model cannot capture. Overall, the table supports the use of a spatially adaptive benchmark, but the
wide coeﬃcient ranges mean that the GWR model should be judged mainly by its out-of-sample prediction
performance and its role as a local valuation benchmark.
Table 7: AUCTION: Distribution of local coeﬃcient estimates from the manual GWR model estimated on the
2023–2024 training sample. The table reports the cross-sectional distribution of location-speciﬁc parameter estimates
and global diagnostic statistics for the spatially varying coeﬃcient speciﬁcation. AIC, and BIC are computed from the
manual GWR Gaussian likelihood using the eﬀective number of parameters.
Variable Min 1st Qu. Median Mean 3rd Qu. Max
Intercept -143.6859 5.4767 11.4816 11.5588 17.3866 150.5031
Bedrooms -0.6233 -0.0030 0.0498 0.0617 0.1112 4.4280
Bathrooms -3.4001 0.0521 0.1195 0.1690 0.1944 13.5481
Parking -2.6667 -0.0245 0.0148 0.0385 0.0597 11.3312
ln(Land size) -2.9039 0.1179 0.2614 0.2549 0.3997 3.8010
ln(Median rent) -20.9810 -0.4807 0.0626 0.0425 0.5997 11.4836
Distance to transport -7.9318 -0.2246 0.0076 -0.0080 0.2316 5.6806
Distance to CBD -5.3529 -0.2248 -0.0202 -0.0056 0.1968 7.8289
Autumn -5.5000 -0.0820 -0.0035 -0.0034 0.0748 5.9738
Winter -5.4481 -0.0819 0.0012 -0.0010 0.0827 4.1038
Summer -1.8180 -0.0948 -0.0069 -0.0083 0.0798 4.1006
Season indicators Y es
Suburb ﬁxed eﬀects Y es
Adjusted𝑅2 0.9255
Akaike information criterion (AIC) -27,561.23
Bayesian information criterion (BIC) 88,600.89
Median absolute error (AUD) 30,240.27
Table 8 reports a similarly strong degree of local heterogeneity for private-treaty transactions. The median
37

bedroom coeﬃcient is positive at 0.0461, while the median bathroom coeﬃcient is larger at 0.1133, again
indicating that bathroom capacity is more strongly priced than bedrooms across many local markets. The
land-size coeﬃcient has a positive median of 0.2491, but the ﬁrst and third quartiles are 0.1133 and 0.3888,
showing that the value of land size is not uniform across Melbourne. In some locations larger land parcels are
rewarded more strongly, while in others the estimated premium is weaker once local market conditions and
other dwelling characteristics are controlled for. The median-rent coeﬃcient is positive at 0.1404, suggesting
that local rental-market strength remains informative for private-treaty prices, although the wide range of
estimates points to substantial neighbourhood variation. Distance to the CBD has a small positive median
coeﬃcient of 0.0193, with an interquartile range from -0.2588 to 0.3164, reinforcing that the accessibility
gradient is spatially uneven rather than constant across Melbourne.
Table 8: Private-treaty sALES: Distribution of local coeﬃcient estimates from the manual GWR model estimated
on the 2023–2024 training sample. The table reports the cross-sectional distribution of location-speciﬁc parameter
estimates and global diagnostic statistics for the spatially varying coeﬃcient speciﬁcation. AIC and BIC are computed
from the manual GWR Gaussian likelihood using the eﬀective number of parameters.
Variable Min 1st Qu. Median Mean 3rd Qu. Max
Intercept -158.0759 0.0466 7.8053 8.9038 16.6105 302.9506
Bedrooms -5.2716 0.0013 0.0461 0.0636 0.1043 14.0843
Bathrooms -105.7962 0.0390 0.1133 0.2749 0.1989 43.2256
Parking -20.0371 -0.0178 0.0169 0.0685 0.0561 37.4105
ln(Land size) -3.2855 0.1133 0.2491 0.2492 0.3888 15.3800
ln(Median rent) -73.2336 -0.2634 0.1404 0.2266 0.6621 44.1714
Distance to transport -17.3489 -0.2860 0.0160 -0.0040 0.2881 16.1177
Distance to CBD -16.1698 -0.2588 0.0193 0.0338 0.3164 15.8689
Autumn -4.5488 -0.0675 -0.0025 -0.0022 0.0564 9.0875
Winter -9.5567 -0.0642 0.0000 0.0005 0.0657 7.7584
Summer -9.0641 -0.0742 -0.0049 -0.0049 0.0605 9.0167
Season indicators Y es
Suburb ﬁxed eﬀects Y es
Adjusted𝑅2 0.9173
Akaike information criterion (AIC) -59,558.70
Bayesian information criterion (BIC) 216,141.63
Median absolute error (AUD) 19,769.13
The model diagnostics show a strong in-sample ﬁt, with an adjusted 𝑅2 of 0.9173 and median absolute
percentage error of 2.52%. However, as with the auction model, the very large coeﬃcient ranges imply
38

that the GWR results should be evaluated mainly through out-of-sample prediction and guide-classiﬁcation
performance. Table 9 shows that the GWR model materially improves the typical prediction error relative to
the global OLS benchmark. For auction transactions, the median absolute error is AUD 72,305, meaning
that for the typical auction property the GWR-predicted value is within about AUD 72,000 of the realised
sale price. This is a substantial reduction compared with the OLS auction median absolute error reported
earlier. The median absolute percentage error is also low at 7.05%, indicating that the model provides a
reasonably tight valuation benchmark for the median auction transaction. The median log error is close to
zero at −0.0110, suggesting little systematic median overprediction or underprediction.
For private-treaty transactions, the typical prediction error is similarly favourable. The median absolute error
is AUD 60,346 and the median absolute percentage error is 7.03%. These values indicate that the GWR
model gives a practically useful estimate of market value for the central part of the private-treaty distribution.
The median log error of −0.0075 is very small, again suggesting that the model is not materially biased at the
median. Therefore, the GWR model is strongest as a median-based local valuation benchmark, rather than as
a model that eliminates all extreme forecast errors.
Table 9: Out-of-sample prediction accuracy for the 2025 test dataset based on the GWR model. The table reports
forecast evaluation metrics measuring prediction errors in both absolute dollar terms and relative percentage terms.
Absolute error P50 denotes the median absolute prediction error and reﬂects the typical deviation between predicted and
realised transaction prices.
Metric Value
Panel A: Auction
Absolute error P50 (median absolute error, AUD) 72,305.36
Median Absolute Percentage Error (%) 7.05
Median log error -0.0110
Median absolute log error 0.0713
Panel B: Private-treaty sales
Absolute error P50 (median absolute error, AUD) 60,346.11
Median Absolute Percentage Error (%) 7.03
Median log error -0.0075
Median absolute log error 0.0701
Table 10 compares realised 2025 sale prices with two ranges: the advertised agent guide and the
GWR-implied valuation range. The table is central to the price-guidance analysis because the GWR range
is constructed from observed property characteristics and local pricing relationships, rather than from the
39

selling agent’s advertised guide.
The sharpest contrast appears in the auction panel. Under the advertised agent guide, only 26.27% of
auction prices fall within the quoted range, while 65.72% sell above the listed maximum and only 8.01% fall
below the listed minimum. This is not simply evidence of greater dispersion around the guide; the errors
are strongly asymmetric and concentrated above the advertised maximum. The GWR-implied range gives a
more balanced comparison: 42.44% of auction prices fall inside the predicted range, 22.38% are above the
predicted maximum, and 35.18% are below the predicted minimum. Although the GWR model does not
eliminate prediction error, its classiﬁcations are not systematically concentrated below realised auction prices
in the same way as the advertised agent guides.
For private-treaty sales, the advertised guide is much more closely aligned with realised transaction prices.
In this segment, 56.05% of prices fall inside the advertised range, 19.62% are above the listed maximum, and
24.33% are below the listed minimum. This pattern is consistent with the interpretation that private-treaty
guides operate partly as bargaining ranges: they anchor buyer oﬀers and seller expectations, and therefore
remain more closely connected to the eventual transaction price. The GWR classiﬁcation is more dispersed,
with 41.28% inside the predicted range, 29.30% above, and 29.42% below, but it does not display the same
strong upward asymmetry observed for auction agent guides. The evidence is consistent with the comparative
predictions of the framework in Proposition 3, which predicts that ﬁnal transaction prices should be less likely
to fall within the quoted range in auction campaigns than in private-treaty sales. The relevant comparison
is the advertised agent guide. Auction prices are far less likely to remain inside the quoted range than
private-treaty prices, and they are much more likely to exceed the advertised maximum. This is precisely the
pattern implied by the participation-role mechanism: in auctions, a lower guide can attract bidder interest
before the competitive process begins, while the ﬁnal price is subsequently determined through bidding. In
private-treaty sales, by contrast, the guide is more disciplined by its bargaining and information role.
40

Table 10: Classiﬁcation of realised transaction prices relative to GWR-implied valuation bounds and advertised listing
price ranges for the 2025 test dataset.
Benchmark Category Count Percent (%)
Panel A: Private-treaty sales
Agent guide Price between listing minimum and maximum 1,488 56.05
Agent guide Price above listing maximum 521 19.62
Agent guide Price below listing minimum 646 24.33
GWR Price between predicted minimum and maximum 1,096 41.28
GWR Price above predicted maximum 778 29.30
GWR Price below predicted minimum 781 29.42
Panel B: Auction
Agent guide Price between listing minimum and maximum 351 26.27
Agent guide Price above listing maximum 878 65.72
Agent guide Price below listing minimum 107 8.01
GWR Price between predicted minimum and maximum 567 42.44
GWR Price above predicted maximum 299 22.38
GWR Price below predicted minimum 470 35.18
This subsection examines the type of properties classiﬁed as underquoted under the conservative GWR-
based rule. The aim is to see whether underquoting is concentrated in particular dwelling types rather than
being evenly distributed across all properties. The analysis focuses on bedrooms, bathrooms and parking,
which are the most visible housing attributes in buyer search and price expectations.
Table 11: Log-based diagnostics for advertised guide distortion. The table reports how often model-implied valuation
bounds exceed advertised listing bounds under the ﬁxed-eﬀects hedonic and GWR models, separately for private-treaty
and auction transactions. Percentages are calculated within each panel using observations with valid advertised and
model-implied bounds. The private-treaty and auction panels contain 2,655 and 1,336 observations, respectively.
Condition Hedonic model GWR model
Count Percent (%) Count Percent (%)
Panel A: Private-treaty sales (𝑁 = 2, 655)
log( ˆ𝑃max) > log(Listmax) 1,524 57.40 1,512 56.95
log( ˆ𝑃min) > log(Listmin) 1,293 48.70 1,173 44.18
Panel B: Auction (𝑁 = 1, 336)
log( ˆ𝑃max) > log(Listmax) 932 69.76 1,038 77.69
log( ˆ𝑃min) > log(Listmin) 888 66.47 983 73.58
Table 11 compares advertised guide bounds with model-implied valuation bounds. The results show
that advertised prices are frequently below the values implied by both valuation models, but the pattern is
41

considerably stronger for auctions. Under the hedonic benchmark, the model-implied upper bound exceeds the
advertised upper guide in 69.76% of auction cases, compared with 57.40% for private-treaty sales. The GWR
comparison is even sharper: 77.69% for auctions versus 56.95% for private-treaty sales. The lower-bound
comparison gives the same conclusion. Under the hedonic benchmark, the model-implied lower bound
exceeds the advertised lower guide in 66.47% of auction cases, compared with 48.70% for private-treaty sales.
Under GWR, the corresponding ﬁgures are 73.58% and 44.18%, respectively. Thus, auction guides are more
frequently positioned below model-implied valuation bounds across both valuation benchmarks.
These results are consistent with the proposed mechanism for Proposition 2, which predicts that auction
guides are more strongly distorted downward than private-treaty guides. The important feature of Table 11 is
that the comparison is made against independently estimated valuation intervals rather than realised prices
alone. This matters because realised auction prices can be aﬀected by bidder competition after the guide is
announced. By contrast, the model-implied bounds are constructed from observed property characteristics,
local market conditions and spatial information, without using the advertised guide as an explanatory variable.
The fact that model-implied bounds exceed advertised bounds much more often in auctions indicates that
auction guides are systematically positioned lower relative to market-consistent values. This pattern is
consistent with the economic mechanism in Proposition 2: in auctions, the guide has a stronger participation
role, so lowering it can attract more potential bidders and intensify competition. In private-treaty sales,
by contrast, the guide is more disciplined by its bargaining and information role. Before using the GWR
predictions in the guide-classiﬁcation analysis, we examine the local estimation diagnostics to assess spatial
coverage, local collinearity and out-of-sample stability. The preferred manual GWR speciﬁcation uses an
adaptive nearest-neighbour bandwidth with 𝑘 = 25 and an adaptive bisquare kernel. Thus, the bandwidth is
not a ﬁxed kilometre radius; it is the realised spatial radius required to include the local neighbours around
each prediction point.
The realised bandwidths remain local in scale. For private-treaty predictions, the median bandwidth
is 0.51 km, with 90th and 95th percentiles of 0.91 km and 1.03 km, respectively. For auction predictions,
the corresponding values are 0.69 km, 1.27 km and 1.64 km. Local condition numbers are generally
moderate, with medians of 8.26 for private-treaty sales and 7.16 for auctions. Condition numbers exceed 30
in 11.19% and 5.69% of local regressions, respectively. The maximum-VIF diagnostics indicate that some
local collinearity remains, especially for distance-to-transport and distance-to-CBD variables, so the local
42

coeﬃcients are not interpreted as structural marginal eﬀects. Instead, the GWR is used as a local valuation
benchmark.
Out-of-sample performance is strong at the median. The auction GWR produces a median absolute log
error of 0.0713, while the private-treaty GWR has a median absolute log error of 0.0701. The empirical
analysis emphasises median prediction accuracy, valuation-bound comparisons and guide-classiﬁcation rates,
rather than mean predictions or individual local coeﬃcients. Overall, these diagnostics indicate that the
preferred GWR speciﬁcation provides a predominantly local and reasonably well-conditioned valuation
benchmark for the subsequent classiﬁcation analysis.
5.3 Dwelling characteristics of GWR-identiﬁed underquoted properties
This subsection examines whether properties identiﬁed as underquoted under the conservative GWR-based
rule share common observable dwelling characteristics. The purpose is not to estimate the causal eﬀects
of bedrooms, bathrooms or parking on underquoting, but to describe the housing segment in which the
model-based underquoting signal occurs most frequently. A high share of three- or four-bedroom properties
among the identiﬁed cases does not necessarily imply that these dwellings have a higher probability of
underquoting, as it may partly reﬂect their prevalence in Melbourne’s detached-house market. The results
should therefore be interpreted as compositional evidence about the properties identiﬁed by the classiﬁcation
rule. Table 12 reports the dwelling characteristics of auction properties classiﬁed as underquoted. Most
identiﬁed cases are conventional family-sized houses. Three-bedroom properties account for 44.99% of the
underquoted auction sample, while four-bedroom properties account for 40.07%. Together, these groups
represent 85.06% of the identiﬁed auction cases. The bathroom and parking distributions exhibit a similar
pattern: 58.91% of the properties have two bathrooms and 61.97% have two parking spaces. Thus, the auction
underquoting signal is not concentrated primarily among very small dwellings or unusually large luxury
properties. Instead, most identiﬁed cases occur among standard suburban houses likely to attract a broad pool
of family-home buyers. This composition is consistent with the proposed participation mechanism, although
it should not be interpreted as evidence that these dwelling types have higher conditional underquoting rates.
43

Table 12: Distribution of dwelling characteristics for auction properties classiﬁed as underquoted under the conservative
GWR-based identiﬁcation rule. Percentages are calculated within the underquoted auction sample.
Category Value Count Percent (%)
Bedrooms
Beds 3 265 44.99
Beds 4 236 40.07
Beds 5 59 10.02
Beds 2 23 3.90
Beds 6 5 0.85
Beds 7 1 0.17
Bathrooms
Baths 2 347 58.91
Baths 1 192 32.60
Baths 3 47 7.98
Baths 4 3 0.51
Parking
Parking 2 365 61.97
Parking 1 85 14.43
Parking 4 63 10.70
Parking 3 59 10.02
Parking 5 9 1.53
Parking 6 8 1.36
Method of Sale
Method of sale Sold at auction 589 100.00
Table 13 reports the corresponding distribution for private-treaty properties. The composition is broadly
similar to that of the auction sample. Three-bedroom dwellings account for 49.06% of the identiﬁed
private-treaty cases, while four-bedroom dwellings account for 40.75%. Together, these categories represent
89.81% of the private-treaty cases. T wo-bathroom properties account for 64.34% of the sample, and properties
with two parking spaces account for 66.76%. These results similarly indicate that the identiﬁed private-treaty
cases are predominantly standard suburban family homes rather than atypical properties. As with the auction
results, however, the percentages describe the composition of the identiﬁed sample and do not establish that
these property types have higher underquoting rates relative to their representation in the full private-treaty
sample.
44

Table 13: Distribution of dwelling characteristics for private-treaty properties classiﬁed as underquoted under the
conservative GWR-based identiﬁcation rule. Percentages are calculated within the underquoted private-treaty sample.
Category Value Count Percent (%)
Bedrooms
Beds 3 183 49.06
Beds 4 152 40.75
Beds 5 19 5.09
Beds 2 13 3.49
Beds 6 5 1.34
Beds 1 1 0.27
Bathrooms
Baths 2 240 64.34
Baths 1 109 29.22
Baths 3 22 5.90
Baths 4 2 0.54
Parking Spaces
Parking 2 249 66.76
Parking 1 47 12.60
Parking 3 35 9.38
Parking 4 32 8.58
Parking 5 5 1.34
Parking 6 5 1.34
Method of Sale
Method of sale Private-treaty sales 373 100.00
The incidence estimates are consistent with Proposition 4, which predicts that underquoting is more
prevalent in auction campaigns than in private-treaty sales. Under the conservative GWR-based rule, 589
of the 1,336 auction transactions are classiﬁed as underquoted, corresponding to 44.09% of the auction
evaluation sample. The corresponding ﬁgure for private-treaty sales is 373 of 2,655 transactions, or 14.05%.
The estimated incidence is therefore more than three times higher for auctions. Tables 12 and 13 complement
this comparison by describing the characteristics of the identiﬁed properties within each mechanism. Because
classiﬁcation requires the realised price to exceed both the advertised upper guide and the lower bound of the
GWR-implied valuation interval, the measure reduces reliance on the guide-to-sale price gap alone. The
substantially higher auction incidence is consistent with the proposed participation mechanism, under which
lower guides may attract additional bidders and intensify competition, while private-treaty guides remain
45

more closely connected to bargaining and negotiation.
5.3.1 Formal comparison across sales mechanisms.
To assess whether the auction–private-treaty diﬀerences are statistically meaningful rather than reﬂecting
descriptive variation in sample proportions, we complement the classiﬁcation evidence with formal binary-
outcome tests. Let𝑌𝑖 denote a binary guide outcome for property𝑖. For the principal test,𝑌𝑖 is the conservative
GWR-based underquoting indicator, deﬁned as
𝑌 𝐺𝑊 𝑅 𝑖 = 1 { 𝑃𝑖 > 𝐿𝑖 and𝑃𝑖 > ˆ𝑃 𝐺𝑊 𝑅 𝑖 } ,
where𝑃𝑖 is the realised sale price, 𝐿𝑖 is the advertised upper guide, and ˆ𝑃 𝐺𝑊 𝑅 𝑖 is the lower bound of the
GWR-implied valuation interval. We also construct indicators for whether the sale price falls inside, above
or below the advertised guide and whether the GWR-implied valuation bounds exceed the corresponding
advertised bounds. For each outcome, we estimate the linear probability model
𝑌𝑖 =𝛼 +𝛽𝐴𝑢𝑐𝑡𝑖𝑜𝑛 𝑖 +𝑋 ′ 𝑖𝛾 +𝜀𝑖,
where𝐴𝑢𝑐𝑡𝑖𝑜𝑛 𝑖 equals one for auction transactions and zero for private-treaty transactions. The vector 𝑋𝑖
contains property, location, season and land-use controls, and standard errors are clustered at the suburb level.
The coeﬃcient 𝛽 measures the regression-adjusted conditional diﬀerence between auction and private-treaty
transactions; it should not be interpreted as a causal eﬀect of selecting the auction mechanism. Table 14
reports the results. The conservative GWR-based underquoting incidence is 44.09% for auctions and 14.05%
for private-treaty sales, producing a raw diﬀerence of 30.04 percentage points. The diﬀerence is highly
statistically signiﬁcant, with a 95% conﬁdence interval of [27.07, 33.01] and a two-sample proportion-test
𝑝-value below 0.001. After controlling for observable property, location, season and land-use characteristics,
the estimated auction–private-treaty diﬀerence remains 28.74 percentage points and is statistically signiﬁcant
at the 1% level using suburb-clustered standard errors. Thus, the substantially higher auction incidence cannot
be explained solely by diﬀerences in the observable composition of the two samples. The advertised-guide
outcomes reinforce this conclusion. After controlling for observable characteristics, auction sale prices are
25.43 percentage points less likely to fall within the advertised guide and 42.40 percentage points more likely
46

to exceed its upper bound.
Table 14: Formal tests of auction–private-treaty diﬀerences in binary guide outcomes. Raw percentages are calculated
using 1,336 auction transactions and 2,655 private-treaty transactions. The conservative GWR-based underquoting
indicator equals one when the realised sale price exceeds both the advertised upper guide and the lower bound of the
GWR-implied valuation interval. Adjusted diﬀerences are percentage-point coeﬃcients from linear probability models
containing property, location, season and land-use controls. Standard errors are clustered at the suburb level.
Outcome Private (%) Auction (%) Raw diﬀ. 95% CI Prop. 𝒑 Adj. diﬀ. Clust. SE Adj. 𝒑
Conservative GWR-based
underquoted indicator 14.05 44.09 30.04 [27.07, 33.01] < 0.001 28.74 1.85 < 0.001
Sale price inside
advertised agent guide 56.05 26.27 -29.77 [-32.80, -26.75] < 0.001 -25.43 2.27 < 0.001
Sale price above
advertised agent maximum 19.62 65.72 46.10 [43.14, 49.06] < 0.001 42.40 2.19 < 0.001
Sale price below
advertised agent minimum 24.33 8.01 -16.32 [-18.51, -14.14] < 0.001 -16.98 1.64 < 0.001
GWR upper bound exceeds
advertised upper bound 56.95 77.69 20.75 [17.82, 23.67] < 0.001 22.00 1.99 < 0.001
GWR lower bound exceeds
advertised lower bound 44.18 73.58 29.40 [26.37, 32.42] < 0.001 30.04 1.90 < 0.001
The GWR-bound comparisons produce a similar pattern. The GWR-implied upper valuation bound
exceeds the advertised upper guide for 77.69% of auction properties, compared with 56.95% of private-treaty
properties. The corresponding lower-bound percentages are 73.58% and 44.18%, respectively. Overall, the
results show economically large and statistically precise diﬀerences across sales mechanisms that remain
after regression adjustment and are consistent with the comparative predictions of the theoretical framework.
Figure 2 provides a suburb-level visual summary of the GWR-based price guidance for the auction market.
Panel (a) shows that the median GWR-implied midpoint is close to the median realised suburb-level sale
price, while the median agent midpoint lies lower. This pattern is consistent with the earlier classiﬁcation
results, where advertised auction guides were frequently below realised prices. Panel (b) gives a more
detailed suburb-by-suburb comparison. For many high-activity auction suburbs, the GWR-implied interval is
positioned closer to the realised median price than the advertised agent interval. The diﬀerence is especially
visible in suburbs where the black point lies above, or near the top of, the agent guide range but is more
aligned with the GWR-implied range. This is useful because the GWR guide is constructed from observed
property characteristics and local spatial information, not from the selling agent’s advertised range. It therefore
provides a more systematic benchmark for assessing whether auction price guidance is low relative to local
market valuations.
47

0.0e+00
5.0e−07
1.0e−06
1.5e−06
$  500k $1m $1.5m $2m
Suburb−level median realised transaction price
Density
Median actual sale price Median agent midpoint Median GWR midpoint
Each observation is one suburb with at least 5 auction transactions.
Auction sales: distribution of suburb−level median realised prices
(a) Distribution of suburb-level median realised auction prices.
Wyndham Vale
Werribee
Tarneit
Hoppers Crossing
Mickleham
Craigieburn
Greenvale
Epping
Mernda
Frankston
Reservoir
Noble Park
Mill Park
Point Cook
Bundoora
South Morang
Keysborough
Mulgrave
Coburg
Dingley Village
Ringwood
Mitcham
Templestowe Lower
Forest Hill
Cheltenham
Vermont
Preston
Doncaster
Bulleen
Doncaster East
$  500k $  750k $1m $1.25m $1.5m $1.75m
Price
Suburb
Agent listing interval GWR−implied interval
Top 30 suburbs by number of auction transactions. Black points are suburb−level median realised prices.
Auction sales: suburb−level median guide comparison
(b) Suburb-level comparison of agent and GWR-implied intervals.
Figure 2: GWR-implied price guidance for auction transactions in the 2025 evaluation sample. Panel (a) shows the
distribution of suburb-level median realised auction prices for suburbs with at least ﬁve auction transactions. The
vertical reference lines report the median realised sale price, the median midpoint of the advertised agent range, and the
median midpoint of the GWR-implied valuation range. Panel (b) compares advertised agent intervals with GWR-implied
valuation intervals for the 30 suburbs with the largest number of auction transactions. Each row represents one suburb;
the black point denotes the suburb-level median realised sale price.
48

6 Conclusions
This paper studies underquoting as a problem of price guidance rather than simply as a gap between the
advertised price and the ﬁnal sale price. The central argument is that advertised guides perform diﬀerent
economic roles across sales mechanisms. In auctions, the guide can be used to attract attention, increase
inspections and expand the potential bidder pool, while the reserve price protects the seller from a low outcome.
In private-treaty sales, the guide is more closely tied to the seller’s asking position and the negotiation process,
making misleadingly low guidance more costly.
The theoretical framework formalises this distinction by treating the guide as both a participation device
and an information signal. It predicts that auction guides should be more strongly distorted downward, auction
sale prices should be less likely to fall within the quoted range, and underquoting should be more prevalent in
auction campaigns. The empirical evidence from Melbourne detached-house transactions is consistent with
these predictions. Only 26.27% of auction prices fall within the advertised range, compared with 56.05% of
private-treaty prices, while 65.72% of auction properties sell above the advertised upper guide.
The model-based evidence reinforces this interpretation. The GWR-implied valuation range produces a
more balanced distribution of realised prices than the advertised auction guide, suggesting that the strong
upward asymmetry in auction outcomes is speciﬁc to agent guidance rather than valuation uncertainty
alone. Under the conservative GWR-based rule, 44.09% of auction transactions and 14.05% of private-treaty
transactions are classiﬁed as underquoted, indicating that the underquoting signal is substantially stronger in
auctions.
These ﬁndings have practical implications for price-guidance governance. Model-implied valuation
benchmarks can help regulators, agencies and listing platforms identify campaigns where advertised guides
appear materially low relative to local market values. Such tools would not replace legal judgment, but
they can support earlier monitoring, compliance review and more targeted enforcement. Overall, the paper
provides a theoretical interpretation and empirical measurement framework for understanding underquoting
in regulated housing markets.
References
ABC News (2024) “Melbourne, Sydney Property Real Estate Underquoting Status,” https://www.abc.net.
49

au/news/2024-08-24/melbourne-sydney-property-real-estate-underquoting-status/
104252630.
Anari, Ali and James Kolari (2002) “House prices and inﬂation,” Real Estate Economics, 30 (1), 67–84.
Banerjee, Abhijit V . (1992) “A Simple Model of Herd Behavior,” Quarterly Journal of Economics , 107 (3),
797–817.
Bikhchandani, Sushil, David Hirshleifer, and Ivo Welch (1992) “A Theory of Fads, Fashion, Custom, and
Cultural Change as Informational Cascades,” Journal of Political Economy, 100 (5), 992–1026.
Blomquist, Glenn and Lawrence Worley (1981) “Hedonic prices, demands for urban housing amenities, and
beneﬁt estimates,” Journal of Urban Economics , 9 (2), 212–221, 10.1016/0094-1190(81)90041-3.
Brunsdon, Chris, A. Stewart Fotheringham, and Martin E. Charlton (1996) “Geographically Weighted
Regression: A Method for Exploring Spatial Nonstationarity,” Geographical Analysis, 28 (4), 281–298,
10.1111/j.1538-4632.1996.tb00936.x.
Castle, James (2017) “Real Estate Price Underquoting,”https://www.choice.com.au/money/property/
buying/articles/real-estate-price-underquoting .
Consumer Aﬀairs Victoria (2024) “Underquoting Taskforce Becomes Permanent,” Published: 31
August 2024, Accessed: 26 January 2026, https://www.consumer.vic.gov.au/latest-news/
underquoting-taskforce-becomes-permanent .
CoreLogic (2018) “CoreLogic Hedonic Home Value Index, November 2018 Results,” https:
//www.corelogic.com.au/sites/default/files/2018-12/CoreLogic%20home%20value%
20index%20Dec%201%20FINAL.pdf, Accessed: 2019-03-14.
Diao, Mi and Jr. Ferreira, Joseph (2010) “Residential property values and the built environment: Empirical
study in the Boston, Massachusetts, metropolitan area,” Transportation Research Record: Journal of the
Transportation Research Board, 2174, 138–147, 10.3141/2174-18.
Diao, Mi, Yuqing Qin, and Tien Foo Sing (2016) “Negative externalities of rail noise and housing values:
Evidence from the cessation of railway operations in Singapore,” Real Estate Economics, 44 (4), 878–917,
10.1111/1540-6229.12123.
50

D’Lima, Walter and Paul Schultz (2021) “Residential real estate investments and investor characteristics,”
The Journal of Real Estate Finance and Economics , 63 (3), 354–393.
Fotheringham, A. Stewart, Chris Brunsdon, and Martin Charlton (2002) Geographically Weighted Regression:
The Analysis of Spatially Varying Relationships , Chichester: Wiley.
(2009) “Geographically Weighted Regression,” in Fischer, Manfred M. and Arthur Getis eds. The
SAGE Handbook of Spatial Analysis , 243–254, Thousand Oaks, CA: SAGE Publications.
Gargano, Andrea and Matteo Giacoletti (2021) “Cooling Auction Fever: Underquoting Laws in the Housing
Market,” University of Melbourne Working Paper Series, 21 (3).
Han, Lu and William C. Strange (2014) “Bidding Wars for Houses,” Real Estate Economics, 42 (1), 1–32.
Horowitz, Joel L. (1992) “The Role of the List Price in Housing Markets: Theory and an Econometric Model,”
Journal of Applied Econometrics , 7 (2), 115–129.
Hungria-Gunnelin, Rosane (2018) “The Impact of Underpricing on Real Estate Auction Outcomes: A
Behavioral Perspective,” International Journal of Housing Markets and Analysis , 11 (3), 412–429.
Khezr, Peyman (2018) “Why Sellers Avoid Auctions: Theory and Evidence,” The Journal of Real Estate
Finance and Economics, 56 (2), 163–182.
Khezr, Peyman and Flavio Menezes (2018) “Auctions with an asking price,” International Journal of Game
Theory, 47 (4), 1329–1350.
Knight, John R. (2002) “Listing Price, Time on Market, and Ultimate Selling Price: Causes and Eﬀects of
Listing Price Changes,” Real Estate Economics, 30 (2), 213–237.
Malmendier, Ulrike and Y oung Han Lee (2011) “The bidder’s curse,” American Economic Review, 101 (2),
749–787.
Merlo, Antonio and François Ortalo-Magné (2004) “Bargaining over Residential Real Estate: Evidence from
England,” Journal of Urban Economics , 56 (2), 192–216.
Österling, Anders Eskil (2016) “Underpricing regimes in housing markets,” Available at SSRN 2795031.
51

Pardasani, Haresh G (2020) Three essays on the performance of housing markets in Australia , Ph.D.
dissertation, Macquarie University.
Pilat, Clayton and Chris Leishman (2025) “Strategic underpricing and time-on-market: evidence from South
Australia’s housing market,” International Journal of Housing Markets and Analysis , 18 (7), 66–86.
Rosen, Sherwin (1974) “Hedonic prices and implicit markets: Product diﬀerentiation in pure competition,”
Journal of Political Economy, 82 (1), 34–55, 10.1086/260169.
Sheppard, Stephen (1999) “Hedonic analysis of housing markets,” in Handbook of Regional and Urban
Economics, 3, 1595–1635, 10.1016/S1574-0080(99)80010-8.
Simonsohn, Uri and Dan Ariely (2008) “When rational sellers face nonrational buyers: evidence from herding
on eBay,” Management science, 54 (9), 1624–1637.
Stevenson, Simon, Jack Y oung, and Constantin Gurdgiev (2010) “A Comparison of Alternative Methods
for the Valuation of Residential Property in Ireland,” Journal of European Real Estate Research , 3 (2),
147–168.
Trading, NSW Fair (2024) “Underquoting Enforcement Report,” Issued March 2024.
Victorian Government (2024) “Underquoting Taskforce Here to Stay,” Published: 2024-08-31, https:
//www.premier.vic.gov.au/underquoting-taskforce-here-stay .
Y avas, Abdullah and Shiawee Y ang (1995) “The Strategic Role of Listing Price in Marketing Real Estate:
Theory and Evidence,” Real Estate Economics, 23 (3), 347–368.
52

Supplementary Files
This is a list of supplementary ﬁles associated with this preprint. Click to download.
UnderquotingJRFEV2.tex
references.bib
underquotingmapsuburbCONTINUOUS.png
underquotingmapsuburbCONTINUOUSselectedsuburbs.png
