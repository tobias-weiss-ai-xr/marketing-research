---
title: Restoring Incentive Compatibility in Two-Stage Energy Markets with Prosumers
url: https://arxiv.org/abs/2606.25910
category: consumer-behavior
subcategory: empirical
date: 2026-06
venue: ''
authors:
- Nikolas Koumpis
- Koushik Kar
- Leandros Tassiulas
- Manolis Zampetakis
source: arxiv
pdf_url: https://arxiv.org/pdf/2606.25910
pages: 57
chars: 163434
fetched_at: '2026-11-08T13:01:46+00:00'
kb_version: 1
---

# Restoring Incentive Compatibility in Two-Stage Energy Markets with Prosumers

Restoring Incentive Compatibility in Two-Stage Energy
Markets with Prosumers
Nikolas Koumpis Koushik Kar Leandros Tassiulas Manolis Zampetakis
Yale University RPI Yale University Yale University
nikolaos.koumpis@yale.edu kark@rpi.edu leandros.tassiulas@yale.edu manolis.zampetakis@yale.edu
Abstract
A central challenge in modern energy market design is the formulation of a strategy-proof
imbalance settlement layer that secures both the economic efficiency of the institution and
the stability of the power grid. Public data reveals that the day-ahead market is strategi-
cally biased below actual consumer demand. Such empirical observations are explained by
active prosumerswhich provide implementable incentives for demand under-reporting. Ac-
tive prosumers buy energy in theday-ahead marketand sell energy in thereal-time marketfor
balancing real-time energy deviations. By under-reporting their demand for the day ahead
they inflate real-time imbalances and, under uniform pricing, they dispatch their gener-
ation assets more profitably. We model thetwo-stageinstitution under linear preferences
and benchmark it against its associated competitive equilibria. We show that although con-
sumers’ incentives for demand under-reporting vanish when the day-ahead market scales,
prosumers incentives remain lower bounded by a positive gain which depends only on the
real-time market generation stack and their shares over it. To restore incentive compati-
bility under the existing informational constraints, we design a leave-one-out contrastive
scoring rule-based penalty that is implemented by the day-ahead market operator, incen-
tivizes prosumers to report their demand truthfully and ensures small charges when par-
ticipating honestly. We illustrate these results with numerical simulations on synthetic data
and evaluate our mechanism on real-market data by first rationalizing demand reports as
subjective equilibria of the induced game. Our mechanism demonstrates strong incentive
alignment while retaining a low cost for honest participation.
1
arXiv:2606.25910v1  [cs.GT]  24 Jun 2026

Contents
1 Introduction 3
1.1 Our Contributions. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.2 Related Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
2 Institutional Background and Model 8
2.1 Key Actors and Terms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
2.2 Institutional Sequence: From Schedules to Imbalances . . . . . . . . . . . . . . . . 9
2.3 Energy Mechanisms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
2.3.1 The Day-Ahead Mechanism . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
2.3.1.1 Day-Ahead Allocation Rule. . . . . . . . . . . . . . . . . . . . . . 11
2.3.1.2 Day-Ahead Market Pricing Rule . . . . . . . . . . . . . . . . . . . 14
2.3.1.3 Day-Ahead Payment Rule . . . . . . . . . . . . . . . . . . . . . . 14
2.3.2 The Real-Time Mechanism . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
2.3.2.1 Real-Time Market Allocation Rule. . . . . . . . . . . . . . . . . . 15
2.3.2.2 Real-Time Market Pricing Rule. . . . . . . . . . . . . . . . . . . . 17
2.3.2.3 Real-Time Market Payment Rule. . . . . . . . . . . . . . . . . . . 17
3 Incentives 19
3.1 Social Choice . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
3.2 Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
3.3 Consumers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
3.3.1 Anti-Concentration of Aggregate Demand. . . . . . . . . . . . . . . . . . . 24
3.3.2 Empirical Evidence for Small Cost Gaps at Market Clearing. . . . . . . . . 26
3.4 Cross-Market Ownership & Prosumers . . . . . . . . . . . . . . . . . . . . . . . . 27
4 Mechanism Design 32
4.1 Information Constraints . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
4.2 Scoring Rule-Based Mechanisms . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
4.2.1 Contrastive Scoring Rule-Based Payment . . . . . . . . . . . . . . . . . . . 34
4.3 Objectives . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
4.3.1 Approximate Bayessian Incentive Compatibility . . . . . . . . . . . . . . . 36
4.3.2 Approximate Penalty Guarantee for Honest Participants . . . . . . . . . . 38
4.3.3 Budget Balance. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
5 Numerical Results 41
5.1 Simulation Setup and Synthetic Results . . . . . . . . . . . . . . . . . . . . . . . . 41
5.1.1 Simulation Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
5.1.2 Synthetic Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
5.2 Empirical Evaluation on Real-Market Data . . . . . . . . . . . . . . . . . . . . . . 45
5.2.1 Time Resolution, Units, and Sample Period . . . . . . . . . . . . . . . . . . 45
5.2.2 Data and Pre-Processing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
5.2.3 Inverse Best-Response Model . . . . . . . . . . . . . . . . . . . . . . . . . . 46
5.2.3.1 Inner Level: Finite Deviations and Linear Inequalities. . . . . . . 47
5.2.3.2 Inner Regularized Convex Program. . . . . . . . . . . . . . . . . 48
5.2.3.3 Outer Level: Calibration of Real-Time Capacities. . . . . . . . . . 48
5.2.4 Results and Discussion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
6 Conclusion 51
2

1 Introduction
Every day, aday-ahead marketoperator decides how much energy has to be delivered for each
of the twenty-four hours of the next day. The amount that will be needed depends on what
households, factories, hospitals and shops will eventually draw from the grid, and nobody
knows these numbers exactly in advance; for each hour tomorrow the actual total demand is
random. The operator asks the consumers of the day-ahead market to report their demand,
andschedulesproducers for tomorrow to match the total of all reports [Stoft, 2002, Euphemia,
2025]. The next day, because at any given time the energy supplied to the grid should balance
the energy demanded, areal-time (balancing) marketcorrects, at delivery time, any deviation
between the scheduled generation and the realized demand. In the context of this work, we
use the termenergy marketto refer specifically to the sequential coupling of the day-ahead and
real-time markets.
Although scheduling generation to match demand is the most sensible thing to do subject
to the grid balance constraint, this arrangement relies on the assumption that the day-ahead
market participants report their demands truthfully. The operator cannot independently mea-
sure how much each consumer believes to need and has to trust their reports. The same trust
shows up in many other institutions. Online advertising exchanges ask advertisers what an
impression is worth to them, and then allocate it accordingly [Edelman et al., 2007]. Multi-tier
supply chains ask each tier to forecast demand so that the next tier can plan [Lee et al., 1997].
Insurance underwriters ask applicants for risk information and use it to price the premium
[Rothschild and Stiglitz, 1976].
Our work was motivated by striking empirical observations. Figure 1 is based on public
market data fetched from [ENTSO-E, 2026] and reports a persistent gap between the aggre-
gate demand reported by participants in the day-ahead market and the total demand actually
realised the next day for three European countries on three different years.
0 4 8 12 16 20
hour of day
0
50
100under-reporting (%)
0 4 8 12 16 20
hour of day
0
200
400
600avg shortfall (MW) 0
5
10
(% of mean demand)
(a) Hungary, 2023
0 4 8 12 16 20
hour of day
0
50
100under-reporting (%)
0 4 8 12 16 20
hour of day
0
200
400
600avg shortfall (MW)
0
5
10
(% of mean demand) (b) Romania, 2024
0 4 8 12 16 20
hour of day
0
50
100under-reporting (%)
0 4 8 12 16 20
hour of day
100
0
100
200
avg shortfall (MW)
5
0
5
(% of mean demand) (c) Slovakia, 2025
Figure 1: Day-ahead market under-reporting across three European countries.
For each country we pick a recent year and show two views. The top chart in each column
gives, hour by hour, how often the volume sold in the day-ahead market fell 10% below the
electricity people actually used that hour. The bottom chart shows, again hour by hour, how
large that shortfall was on average – in megawatts on the left axis and as a share of the mean
(actual) demand on the right axis. Blue bars mark hours where the market scheduled less than
what was needed; dark-green bars mark hours where it scheduled more. The same pattern
3

shows up everywhere: the gap is largest overnight and in the evening, and almost disappears
around midday.
This gap cannot be attributed to prediction error: it is one-sided, it persists across long
observation windows, and survives changes in market conditions and weather patterns. We
argue that this gap reflects a strategic bias in the demand reports — there exist energy market
participants that systematically under-report their demand whenever is profitable under the
existingsettlement rules.
The economic consequence is direct. The day-ahead market collects reports from many
self-interested players to recover the latent true distribution of next-day demand and shapes
the very data it is trying to learn from. If participants do not report their demand honestly, the
biased day-ahead market drives the real-time market towards a non-zero expected imbalance,
and the real-time market clears more than just the irreducible random fluctuations in actual
consumption, causing the market outcome to drift away from its competitive equilibrium,
thus reducing social welfare.
That said, and given that in both the U.S. and the European energy markets, the settlement
rules are anevolving design objective(see Section 1.2), the central question of this paper – taking
the demand reports as the strategic component – is the following:
Can one design a settlement layer so that the institution estimates the latent demand belief
and hence recovers the competitive equilibrium of the underlying economy?
1.1 Our Contributions.
To answer this question, we start in Section 2 by first providing a unified institutional and
formal model for the two-stage energy markets. This model is the common ground where all
the subsequent results rest. Then, in Section 3 we identify and study the implementable incen-
tives that explain the empirically observed strategic bias. While respecting institutional and
informational constraints, we design in Section 4, a contrastive scoring-rule-based mechanism
implemented by the day-ahead market operator and added to all consumer’s bill. Section 5
demonstrates our findings and evaluates our mechanism design via numerical simulations on
synthetic and on real market data.
Our theoretical and empirical contributions are as follows:
Theoretical Contributions
(1)Vanishing incentives to underreport for consumers(Theorem 1). For any consumer
who does not own real-time generation, the maximum benefit from under-reporting her
demand shrinks toward a non-positive value as the size|I|of demand side of the day-
ahead market grows, at a rate proportional to 1/
p
|I|. Honesty is therefore an approxi-
mate best response for consumers in large day-ahead markets.
(2)Non-vanishing incentives to underreport for prosumers(Theorem 2). For any pro-
sumer — a consumer who owns a strictly positive share of real-time generation assets
— the benefit from under-reporting is bounded below by a strictly positive constant that
depends only on the size of her portfolio and the shape of the real-time supply stack. This
constant does not depend on|I|. Therefore, under the standard institution not everyone
can be made approximately honest simultaneously, no matter how large the day-ahead
market grows.
(3)Scoring-rule restoration of incentive compatibility(Theorem 3, Corollary 1 and Propo-
sition 5). While respecting the existing institutional constraints, we modify the imbalance
4

settlement by designing a contrastive scoring-rule-based payment that the day-ahead op-
erator can compute from observable quantities (the reports, the realised total consump-
tion, and historical data) and add to each participant’s bill. The extra payment is built
from a strictly proper scoring rule and has a single tuning knob, the strong convexity pa-
rameterµof the associated strongly convex function. We prove that, by choosingµlarge
enough, the prosumer’s benefit from lying can be driven strictly below the persistent
constant of (2). Honesty is therefore restored for everyone.
Turningµup deters lying more strongly, but it also charges honest participation more
heavily when their true demand happens to differ from the population average. Proposi-
tion 5 in Section 4.3.2 characterises this trade-off by providing the valueµ ⋆ that balances
the two effects and prove that, in a large market, both the residual incentive to lie and
the residual cost paid by honest participants vanish at the same rate.
Empirical Contributions
(1)Simulations on synthetic market data(Section 5.1). We illustrate the three qualitative
phenomena presented by our theoretical results in a constructed synthetic market that
focuses only on the incentive question. The day-ahead and real-time supply stacks are
fixed and every player holds a uniform belief over private demand. We focus on a single
player with fixed true demand across market sizes so that the comparisons have a com-
mon baseline. In every experiment we evaluate the expected gain from under-reporting,
with the expectation taken by Monte Carlo. The four experiments differ only in which
mechanism is in force and which structural parameters are varied.
(2)Evaluation on real market data(Section 5.2) We demonstrate the performance of our
mechanism by applying it to the strategic component that we infer from real market
data. We work with hourly time series of low, medium and high voltage reported loads
together with the corresponding realized demand. We rationalize the day-ahead mar-
ket reports as subjective equilibria by means of the prosumers parameters and real-time
generation capacity bounds that make the observed day-ahead reports approximately
optimal. Having inferred the model’s parameters, we evaluate our scoring rule-based
mechanism and demonstrate its effects.
1.2 Related Work
This paper contributes to several literature domains. We organize our discussion of the related
work around three themes(i)the design of wholesale electricity markets and the institutional
treatment of imbalance settlement,(ii)mechanism design, subjective beliefs and scoring rules,
(iii)strategic machine learning.
Wholesale Electricity Market Design and Imbalance Settlement.The design of competi-
tive wholesale electricity markets has been a subject of study since deregulation in the 1990s.
[Stoft, 2002] is the first textbook treatment of the two-stage structure — day-ahead scheduling
followed by real-time balancing (what we previously called the energy market)— that is the
institutional setting of the present paper.
In Europe, the Third Energy Package (TEP) [European Commission, 2009] and the most re-
cent Clean Energy Package (CEP) [European Commission, 2019] are each, a set of laws passed
in 2009 and 2019, respectively. The former established the framework for the internal electric-
ity market and the most recent one changed the rules for two things: balancing (the real-time
process ensuring that supply equals demand) and imbalance settlement (the rule for charging
participants’ deviations from schedule). In particular, Directive 2019/944 [EU, 2019] from the
5

CEP officially recognized two kinds of players that hadn’t really existed in EU electricity law
before – active customers and aggregators.
(i)Anactive customeris an energy market participant that isn’t just passively buying elec-
tricity from the grid. They can produce and sell their own electricity. Directive 2019/944
defines them in Article 2(8) and gives them concrete rights in Article 15 (e.g. the right to
sell their excess electricity).
(ii)Anaggregatoris an energy market participant that bundles together lots of small players
and offers their combined flexibility to the electricity market as if it were one big power
plant. The Directive 2019/944 defines aggregators in Article 2(18) and (19) and sets the
rules for how they operate in Article 17.
Article 5(1) of Regulation (EU) 2019/943 [EU2, 2019] establishes that all market participants
are responsible for the imbalances they cause in the system. Since aggregators and active
customers qualify as market participants under Article 2(25) of the same Regulation, they are
subject to this obligation.
Although both active customers and aggregators qualify as market participants under Reg-
ulation (EU) 2019/943, only aggregators are realistically positioned to engage in cross-market
exchange (e.g., buying energy in the day-ahead market and selling it closer to real time, via the
balancing market – see Regulation (EU) 2019/943 [EU2, 2019, Article 2(25)]). Active customers
may benefit indirectly from such strategies by participating through an aggregator (Directive
(EU) 2019/944, Article 15(2)(a)).
That said, a central energy market entity of study in this paper is themarket-active pro-
sumer, or simplyprosumer: an entity that both consumes and produces electricity, qualifies as
a market participant under Article 2(25) of Regulation (EU) 2019/943, and engages in cross-
market exchange between the day-ahead and balancing markets. The prosumer thus sits at
the intersection of the active customer (Directive (EU) 2019/944) and the aggregator function
described in the same Directive, and is subject to the balance responsibility imposed by Article
5(1) of Regulation (EU) 2019/943. The formal definition we adopt for the player’s economic
role in our model is given in Section 2.1.
The EU regulatory framework signals thatimbalance settlement is an active design objective.
Regulation (EU) 2019/943 establishes the general principle of balance responsibility. On top of
that, recital 12 explicitly characterizes imbalance pricing as a behavioral incentive mechanism,
stating that the pricing method for balancing energy ”should create positive incentives for
market participants in keeping their own balance or helping to restore the system balance [...],
thereby reducing system imbalances and costs to society,” and that such pricing approaches
”should strive for the economically efficient use of demand response and other balancing re-
sources.” This framing is reinforced by the Electricity Balancing Guideline [European Commis-
sion, 2017a], to which recital 12 directly refers (Articles 18, 30 and 32). Taken together, these
provisions reveal that the EU treats the design of imbalance settlement as an open, behav-
iorally consequential lever for integrating new market actors such as prosumers, rather than
as a fixed technical detail. This paper contributes directly to this open design problem.
Mechanism Design, Subjective Beliefs and Scoring Rules.Mechanism design in its central
insight, going back to Vickrey [Vickrey, 1961], Myerson [Myerson, 1981], and a long line since,
holds that honesty cannot be assumed – it has to beengineered. For mechanisms with money
like energy markets, this often means designing a payment rule so that, for every participant,
telling the truth is the most profitable thing to do. If lying is unprofitable, self-interest does the
rest.
In our setting, participants report their demand for the next day. These reports can, in
principle, be aggregated to reflect each player’ssubjective beliefabout their consumption needs
6

the following day. De Finetti [de Finetti, 1937] was the first who defined subjective belief
axiomatically through betting: a person’s subjective belief about an event is the price at which
this person would be indifferent to sell or buy a $1-contract written on that event. De Finetti’s
coherence argument shows that consistent beliefs are precisely those that admit no sure-loss
bet. However, the question of how toelicita person’s belief is not answered in his work.
[Brier, 1950] independently, working in meteorology, likely without thinking about subjec-
tive probability foundations but rather about how to verify weather forecasters, was the first
who proposed the quadratic scoring rule as an empirical tool. Two years later [Good, 1952]
introduced the logarithmic scoring rule. De Finetti [Good et al., 1964, p. 357-364] observed
that Brier’s and Good’s scores had the strict propriety property ofmeasuring– in the sense of
eliciting – (true) subjective beliefs. This was a completely different insight from the question
of forecasting skill: a strictly proper scoring rule controls the belief that a person communi-
cates given what they know, and not the quality of what they know, which depends on their
ability in information acquisition. Essentially, according to de Finetti, the scoring rule acts
as an information-elicitation tool that filters out non-rational instincts that usually distort hu-
man judgment. By tying real-world consequences, the score aligns a person’s self-interest with
honesty.
This insight was formalized into a general theory. [McCarthy, 1956] and [Savage, 1971]
characterized the class of strictly proper scoring rules and established their equivalence to
strongly convex functions defined over distributions, while [Gneiting and Raftery, 2007b] and
[Gneiting and Raftery, 2007a] extended the framework to continuous and multivariate fore-
casts and provided the modern synthesis on which most applications rely.
Although in principle individual demand reports can be mapped to the player’s subjec-
tive belief about their consumption needs, scoring these beliefs requires knowing their actual
consumption levels. Such information can be obtained only via metering which introduces
measurement errors and it is often of questionable reliability. That said, any settlement mod-
ification is intended to be implemented by the day-ahead market operator. Accordingly, the
design should be subject to the information available to the day-ahead market stage (see Sec-
tion 4) which does not include the individual consumed energy levels.
For each player, our mechanism builds on twopopulation-level subjective beliefs– one con-
structed from all reports including that player’s and one constructed without it, thus charging
based on their marginal contribution to the day-ahead market’s forecasting ability. The first
work where scoring-rule theory is applied to collective beliefs constructed from many players’
inputs is [Hanson, 2003, 2007] where amarket scoring ruleaggregates individual reports into a
single distribution, and each player’s payoff depends on how their action moves that collective
belief.
Our mechanism aggregates past demand reports and past actual consumption realizations,
forms two market-level subjective beliefs for the real-time imbalance and scores each player
based on their marginal contribution to the market’s forecasting ability of the imbalance. Our
mechanism can be viewed as a scoring-rule formulation of ideas previously developed in [Cai
et al., 2015] on truthful elicitation from strategic data sources, and [Ghorbani and Zou, 2019]
on marginal-contribution valuation. Casting these ideas in scoring-rule language allows us
to establish approximate Bayesian strategy-proofness under the information constraints (see
Section 4).
Strategic Machine Learning.The problem we study is, at its core, a strategic statistical es-
timation problem: an estimator – here, the day-ahead market – is fitted to data submitted
by self-interested players whose reports depend on how the estimator will use them. This
places our work within the growing literature on strategic machine learning, which examines
learning and estimation problems in which data are produced by strategic players rather than
7

drawn from a fixed distribution of nature. Foundational contributions established the basics
of strategy-proof regression and classification [Dekel et al., 2010, Meir et al., 2012], followed
by the strategic classification framework of [Hardt et al., 2016] and the performative predic-
tion framework of [Perdomo et al., 2020]. Closest to our setting are the strategic-data-source
framework of [Cai et al., 2015], which designs payments so that the resulting statistical esti-
mate is optimal in expectation under truthful reporting, and the data valuation framework of
[Ghorbani and Zou, 2019], which uses leave-one-out marginal contributions as a fair measure
of each data point’s value. We continue in this line, but apply its ideas to a domain not pre-
viously studied from this perspective – electricity imbalance settlement – in which the events
being scored are endogenously defined by the real-time supply stack, a feature absent from
both prior works.
2 Institutional Background and Model
Our analysis uses the simple timeline that is common in energy markets: (i) energy is sched-
uled ahead of delivery, and any real-time deviations between scheduled and actual consump-
tion are corrected by the system operator and settled financially afterwards.
2.1 Key Actors and Terms
Terminology differs across regions. Therefore, before describing the institutional sequence,
we briefly list the actors and terms that appear in it. We map EU terms (NEMO, TSO, BRP ,
ENTSO-E) to their closest U.S. counterparts (ISO/RTO, Balancing Authority, NERC).
ACTIVE PROSUMERS.Aprosumeris an entity that (a) both consumes and produces electric-
ity, (b) qualifies as a market participant under Article 2(25) of Regulation (EU) 2019/943
[EU2, 2019], and (c) engages in cross-market exchange, in particular between the day-
ahead and balancing markets. The prosumer thus sits at the intersection of the active
customer defined in Directive (EU) 2019/944 [EU, 2019] and the aggregator function de-
scribed in the same Directive, and is subject to the balance responsibility imposed by
Article 5(1) of Regulation (EU) 2019/943.
NEMO (EU) / ISO–RTO (US).In the EU, aNominated Electricity Market Operator (NEMO)is
the entity designated to perform tasks related to single day-ahead or single intraday
coupling [European Commission, 2015, Art. 2(23)].
In the U.S., the closest counterpart is theIndependent System Operator (ISO)orRegional
Transmission Organization (RTO), which operates the system and runs day-ahead and
real-time wholesale markets [Federal Energy Regulatory Commission, 2025b, U.S. De-
partment of Energy, 2022].
TSO (EU) / system operator and Balancing Authority (US).ATransmission System Operator
(TSO)is responsible for operating, maintaining, and (if needed) developing the transmis-
sion system in a given area [European Parliament and Council of the European Union,
2019a, Art. 2(35)].
In the U.S., the operational responsibility to keep supply and demand balanced in real
time belongs to aBalancing Authority (BA)(often an ISO/RTO in organized-market re-
gions) [North American Electric Reliability Corporation (NERC), 2025b, U.S. Department
of Energy, 2022].
ENTSO-E (EU) / NERC (US).ENTSO-E is the European network that brings together TSOs
to support secure and coordinated operation of Europe’s interconnected grid [ENTSO-E,
a].
8

In North America, bulk power system reliability standards are developed and overseen
through the North American Electric Reliability Corporation (NERC) under FERC over-
sight [Federal Energy Regulatory Commission, 2023].
LSE:Load Serving Entity.The retail-facing entity that is responsible for serving electricity to
end-use consumers. An LSE forecasts consumption, purchases energy in wholesale mar-
kets (e.g., day-ahead), and is responsible for deviations between scheduled and actual
consumption through imbalance settlement [North American Electric Reliability Corpo-
ration (NERC), 2025a, p. 24 (definition of “Load-Serving Entity”)].
BSP:Balancing Service Provider. In the EU, a market participant with reserve-providing units
(or groups) able to provide balancing services to TSOs [European Commission, 2017b,
Reg. (EU) 2017/2195, Art. 2(6) (definition of “balancing service provider”), OJ L 312/9].
In U.S. ISO/RTO markets, the closest counterpart is aresource/market participantthat of-
fersancillary services(e.g., regulation and operating reserves) to the ISO/RTO and is com-
pensated according to the ancillary-service market rules when providing these reliability
services [ISO New England Inc., n.d., PJM Interconnection, 2025].
BRP (EU) / responsible market participant (US).ABalance Responsible Party (BRP)is a mar-
ket participant (or its representative) responsible for its imbalances in the electricity mar-
ket [European Parliament and Council of the European Union, 2019b, Art. 2(14)].
In U.S. ISO/RTO markets, the ISO/RTO financially settles real-time deviations through
its real-time market and settlement rules; the responsible party is the market partici-
pant (or scheduling entity) behind the schedule [Federal Energy Regulatory Commis-
sion, 2025b].
Buy/sell orders:Instructions submitted to the market operator for a given delivery period. In
EU terminology these are orders that state how much energy a participant wants to buy
or sell for a given delivery period, and at what monetary rate (price) limit. [European
Commission, 2015, Reg. (EU) 2015/1222, Art. 2(21) (definition of “order”)]. A buy order
specifies a quantity the participant is willing to purchase up to a maximum price; a sell
order specifies a quantity the participant is willing to supply above a minimum price.
The market clearing process aggregates these orders to determine the accepted schedules
and the market price.
In U.S. ISO/RTO terminology they are typically calledbids(to buy) andoffers(to sell).
A buy order/bid specifies a quantity and usually a maximum price; a sell order/offer
specifies a quantity and usually a minimum price. The market clearing process matches
bids and offers to determine the accepted schedules and the market price(s) [Federal
Energy Regulatory Commission, 2025a, PJM Interconnection, 2023].
2.2 Institutional Sequence: From Schedules to Imbalances
We describe the institutional sequence at a level sufficient for incentive analysis. While the
precise design differs across markets, the institutional functioning of energy markets can often
be represented as the following sequence:
Day-Ahead Scheduling (DAM).Ahead of delivery, market participants submit buy/sell or-
ders to the Day-Ahead Market (DAM) operated by the NEMO. Market operator selects ac-
cepted demand and generation schedules and computes uniform prices.
9

Intraday Adjustments (IDM).After DAM, participants may adjust schedules closer to de-
livery in the Intraday Market. For clarity we skip intraday adjustments and treat the DAM
schedule as the final schedule for the day ahead.
Balancing and Activation (TSO layer).In real time, the TSO activates balancing resources to
maintain system balance (generation equals demand). Balancing resources can be integrated
cross-border through certain platforms (e.g. ENTSO-E).
Imbalance settlement (financial layer).After delivery, BRPs are charged/credited for devia-
tions between scheduled and realized positions using an imbalance price derived from balanc-
ing actions (design-specific details).
2.3 Energy Mechanisms
Fix one delivery slot. An outcome of an energy market for this slot consists of: (i) an electric-
ity allocationxand (ii) monetary transferst. A participant of an energy market has a private
type that encodes their preference over the market outcomes. In energy markets, participants
communicate their type directly to the mechanism and derive utility based on the market out-
comes.
Definition 1(Mechanism with money).A direct mechanism with money is a pair of maps
(x(·),t(·)),
where x(·)selects allocations and t(·)selects transfers as functions of the communicated types.
Energy markets are direct mechanisms with money and in this section, we define the sequen-
tial coupling of the day-ahead and real-time institutions explicitly as such.
2.3.1 The Day-Ahead Mechanism
The day-ahead mechanism is a direct mechanism with money executed by the NEMO.
Consumers.Individual households and businesses do not participate in the energy market
themselves. Instead, an LSE bundles their total demand and buys the electricity for them.
Therefore, within the day-ahead market, LSEs function as actual consumers.
Producers.Power plants act as the market’s producers. Rather than selling directly to the
end-consumers, they submit supply orders to the day-ahead market based on their nominal
generation capacity. Therefore, within this market, power plants function as the primary pro-
ducers.
Each participant has a private type that encodes their preference over the mechanism’s
outcomes, the latter consisting of allocations and transfers (see Definition 1). The day-ahead
market operates as a double auction, where both LSEs and producers simultaneously submit
price-quantity orders (bids/offers) to the NEMO (ISO). Within the framework of mechanism
design, these orders constitute thereportedtypes of the participants.
Simple Orders.In this study, we focus on simple orders. Simple orders consist of straight-
forward price-quantity pairs thus yielding quasi-linear preferences (for more details about the
different orders submitted in energy markets, see e.g. [Euphemia, 2025]).
LetIbe the set of consumers andJthe set of producers. Each buyeri∈Ihas a type
θi ≡(v i, di)∈R >0 ×R ≥0,
10

wherev i is their marginal value, i.e. willingness to pay, measured in $/MWh and d i isi’strue
demand (MWh) for the particular time slot. Given an allocationx i ∈[0, d i]and transfert i ∈R,
buyerihas quasi-linear utility
Ui(xi,t i;θ i) =vixi +t i.
Each producerj∈Jis characterized by a type
ϕj ≡(c j,g j)∈R >0 ×R ≥0,
wherec j is constant marginal cost ($/MWh) andg j is the nominal generation capacity (MWh)
for the hour. Given dispatchy j ∈[0,g j]and transfert j, producerjhas quasi-linear utility
Uj(yj,t j;ϕ j) =tj −c jyj.
Participants communicate their types to the mechanism by reporting their types to the NEMO.
On the basis of these reports then, the NEMO determines allocations by solving a social welfare
maximization program. On top of that, given these allocations, the NEMO assigns payments
to the participants.
In what follows we define the allocation and payment rules for the day-ahead mechanism
under the assumption of simple orders (linear utilities).
2.3.1.1 Day-Ahead Allocation Rule.For a given reported profile(θ,ϕ), whereθ= (v, d)∈
R2|I| collects buyers’ values and demands andϕ= (c,g)∈R 2|J| collects sellers’ costs and
nominal generation capacities, the NEMO’s role is to find the allocation of energy that creates
the most value for society. The NEMO solves
(xDA,y DA )∈arg max
(x,y)∈R |I| + ×R|J| +
(
v⊤x−c ⊤y:x≤d,y≤g, ∑
i∈I
xi = ∑
j∈J
yj
)
, (1)
where the inequalities are component-wise and the equality constraint ensures that delivered
energy matches demanded energy.
Market Restriction.The welfare maximization program (Equation 1) can be solved greedily
by matching the highest-value consumers with the lowest-cost producers while maintaining
the power balance constraint.
Program (Equation 1) has non-empty and bounded feasible region and hence a primal
optimal(x ⋆,y ⋆)exists and the optimal value is finite. The equality constraint can be relaxed
and because strong duality holds it guarantees the existence of a dual optimalp ⋆. The convex
and piece-wise linear dual function reads:
g(p) =∑
i∈I
max
xi∈[0,di]
(vi −p ) xi + ∑
j∈J
max
yj∈[0,g j]

p−c j

yj, (2)
the best-responses to some feasiblep ⋆ are
x⋆ i (p ⋆)∈arg max x∈[0,di] (vi −p ⋆)x,y ⋆ j (p ⋆)∈arg max y∈[0,g j] (p ⋆ −c j)y, (3)
11

andp ⋆ is dual optimal if
0∈∂g (p⋆) =
(
∑
i∈I
xi = ∑
j∈J
yj :y j ∈y ⋆ j (p⋆) ,x i ∈x ⋆ i (p⋆)
)
. (4)
Then,(x ⋆,y ⋆,p ⋆), wherex ⋆ =x ⋆(p ⋆)andy ⋆ =y ⋆(p ⋆), is primal-dual optimal. According to
(Equation 3), for some fixed dual optimalp ⋆ the set of maximizers of (Equation 1) is not a sin-
gleton and therefore, the allocations determined are in general multi-valued correspondences.
Because of this non-uniqueness, even small variations in reported types could shift market
outcomes in an unknown manner. Then, a participant is not able to determine the consequence
of their reports and subsequently the mechanism designer cannot understand incentives and
hence establish desired incentive properties. To this end, we impose the following rather non-
restrictive assumption over reported types.
Assumption 1(Sufficient conditions for uniqueness of DA-allocation).We restrict to order pro-
files such that∀i,i ′ ∈I,∀j,j ′ ∈J:v i ̸=v i′,c j ̸=c j′,v i ̸=c j
We adopt Assumption 1 to ensure the uniqueness of the market-clearing outcome. While
this excludes exact ties between orders, such cases are negligible (of measure zero). This restric-
tion allows us to treat the allocation rule as a well-defined function rather than a multi-valued
correspondence, providing the necessary foundation for our incentive analysis and mechanism
design in Section 3 and Section 4, respectively.
Proposition 1(Uniqueness of the DA allocation).Under Assumption 1, the DA allocation problem
(Equation 1) has a unique minimizer.
Proof.Fix some given dual optimalp ⋆. Then, under Assumption 1, a consumer and a producer
cannot be marginal simultaneously sincev i ̸=c j for alli∈Iandj∈J. As a result, one of the
summations in (Equation 4) is constant and uniquely determines the allocation of the marginal
participant. In the case where a producer is marginal, the existence of another producer with
cost equal to the marginal cost would place both in the same merit order and can therefore be
exchanged, while being assigned one another’s allocation. The same argument holds in the
case where consumer is marginal.
Each maximization problem in (Equation 2) is solved independently by the participants
with the dual variablep ⋆ driving their individual incentives so that the market clears, i.e. (Equa-
tion 4) holds. The dual optimal that allows players to act based only on their private informa-
tion while still trading with one another, is called market-clearing price.
The allocations obtained by the market and the allocations assigned by the mechanism are
in general different since the latter depend on the reported than the private types. However,
if day-ahead mechanism market participants report their true types, then the two allocations
coincide.
Definition 2(Day-Ahead Market).A day-ahead market is a primal-dual optimal under private types.
Fairness of Competitive Allocations.We refer to market allocations as competitive alloca-
tions. A well-known fact from microeconomics is that competitive allocations are fair in the
sense of Pareto: everyone is allocated what they deserve (according to their private type).
That being said, it makes sense to benchmark our mechanism against the corresponding com-
petitive allocation. This of course translates to incentivizing truthful reporting of the market
participants.
12

In what follows, we define the day-ahead payments. Because energy markets clear through
uniform pricing1, we need first to define the pricing rule – how the reported types determine
the day-ahead price. If we wish our mechanism to be able to recover competitive allocations
(and hence be Pareto fair), we have to make sure that the pricing rule spans market clearing
prices. First, we introduce some notation
Merit-Order Notation.Let(c 1,g 1), . . . ,(c|J| ,g |J| )denote producers ordered by increasing cost:
c1 <· · ·<c|J| . Define cumulative capacities
G0 ≡0,G j ≡ ∑
l≤j
gl (j=1, . . . ,|J|).
LetG |J| be the total generation capacity available in the day-ahead market and assume that it
always suffices for covering the total scheduleq ⋆ ≡ ∑i x⋆ i ∈[0,G |J| ]. The marginal producer
index is defined as the cheapest marginal cost that covers that total (see also Figure 2)
m(q⋆)≡min{l:q ⋆ ≤G l}.
Then, the cost of the marginal producer isc(q ⋆)where we slightly abuse the notation by iden-
tifying the cost of them−th producer (which is the marginal)c m(q⋆), with the cost funtion at
that quantityc(q ⋆). In a similar way, we define the marginal consumer.
Let(v 1,d 1), . . . ,(v|J| ,d |J| )denote consumers ordered by decreasing willingness to pay :
v1 >· · ·>v|I| . Define cumulative demands
D0 ≡0,D l ≡ ∑
i≤l
di (l=1, . . . ,|I|).
Then, the marginal consumer is defined asn(q ⋆)≡max  l:q ⋆ ≤D l 	 and the valuation of the
marginal consumer isv(q ⋆), where once again, byv(q ⋆)we meanv n(q⋆).
Proposition 2(Competitive prices form a closed interval).Let(x ⋆,y ⋆)be a competitive allocation
and q⋆ ≡ ∑i x⋆ i the total quantity exchanged. Then,
p⋆ = h max{c(q ⋆),v(q ⋆ +1)}, min{v(q ⋆),c(q ⋆ +1)} i .
Proof.Because the pair(x ⋆,y ⋆)is the projection of the competitive equilibrium into its first
two coordinates, it automatically satisfies market clearing and therefore, its pre-image under
the best responses (3) gives the competitive prices that are compatible with this allocation 2.
We have
p⋆ ∈

\
i∈I
{p≥0 :x i =x ⋆ i (p)}
!
∩

\
j∈J
{p≥0 :y j =y ⋆ j (p)}

 . (5)
By splitting consumers into those who are at least partially allocated and those who are allo-
cated zeroI=I 1 ∪I 0,I 1 ={i∈I:x i ∈(0, d i]},I 0 ={i∈I:x i =0}we obtain
∩i∈I {p≥0 :x i =x ⋆ i (p)}=  ∩i∈I 1{p≥0 :x i =x ⋆ i (p)}  ∩  ∩i∈I 0{p≥0 :x i =x ⋆ i (p)}  .
1Uniform price means that each participant is charged/payed a constant per unit of energy.
2We can take the best responses over all positive reals (prices). This gives us a set of onlyoptimalallocations.
From that set of optimal allocations, only a subset corresponds to allocations (pairs) that satisfy clearing (non-
empty), and we take the pre-image of that subset under the best responses.
13

Withx i ∈(0, d i], we have{p≥0 :x i =x ⋆ i (p)} ⇐ ⇒p≤vi and hence, the prices supporting
those that are at least partially allocated are
∩i∈I 1{p≤v i}= [0,v(q)].
Forx i =0, we obtain{p≥0 :x ⋆ i (p) =0} ⇐ ⇒p≥vi, and
∩i∈I 0{p≥v i}= [v(q+1),+∞).
Therefore, the set to the left of the intersection in (Equation 5) reads[v(q+1),v(q) ]. By split-
ting producers into those that are at least partially allocated and non-allocated and subse-
quently working in a similar way as we did for the consumers, the set to the right of the
intersection in (Equation 5) reads[c(q),c(q+1) ], and the result follows.
2.3.1.2 Day-Ahead Market Pricing RuleLet
q(θ,ϕ)≡ ∑
i
xDA i (θ,ϕ)∈[0,G |J| ], (6)
be the total quantity demanded for tomorrow. We follow the uniform-pricing convention and
select the day-ahead price as the marginal cost of the marginal producer (in merit order) sup-
plying the cleared quantity:
pDA (θ,ϕ)≡c(q(θ,ϕ)). (7)
According to Proposition 2, under Assumption 1 the marginal cost of the marginal producer
can be realized as a competitive price only if strictly
c(q⋆)>v(q ⋆ +1). (8)
This condition is rather qualitative. It implies that the decline in surplus is driven by a reduc-
tion in valuations rather than an increase in costs. In particular, this is the case in Figure 2
where the market clears with the inverse demand curve “cutting” the inverse supply curve
(see Figure 2). In addition, (Equation 8) implies that non-zero allocated consumers are fully
allocated their demand. This fact will simplify our incentive analysis later on in Section 3.
Assumption 2.We assume that the NEMO is always able to adjust market curves so that (Equation 8)
holds.
Under Assumption 2 the pricing rule (Equation 7) supports competitive allocations and hence
renders possible benchmarking the day-ahead mechanism against competitive equilibria. As
a result, it establishes a formal baseline for evaluating and achieving fairness. Having estab-
lished the pricing rule, we are ready to define the day-ahead payment rule.
2.3.1.3 Day-Ahead Payment RuleEnergy markets clear through a uniform price. The pay-
ments are
tDA i (θ,ϕ)≡ −p DA (θ,ϕ)x DA i (θ,ϕ) (i∈I),
tDA j (θ,ϕ)≡+p DA (θ,ϕ)y DA j (θ,ϕ) (j∈J). (9)
14

Letx≡(x i)|I| i=1,y≡(y j)|J| j=1, andt=  (ti)|I| i=1,(t j)|J| j=1  witht i =p x i andt j =p y j, denote the
outcomes of the day-ahead mechanism.
Definition 3(Day-ahead mechanism).Under Assumption 1 and Assumption 2, the day-ahead
mechanism with money is defined as
MDA (·)≡  xDA (·),y DA (·),t DA (·)  :(θ,ϕ)7→(x,y,t),
where

xDA (·),y DA (·)  is given by (Equation 1), t DA (·)≡  (tDA i )i∈I ,(t DA j )j∈J  is given by (Equa-
tion 9), and the clearing price p DA (·)entering t DA is given by (Equation 7).
2.3.2 The Real-Time Mechanism
The day-ahead producers that are dispatched to cover the actual consumption in the day-
ahead commit to supplyybased on the scheduled demandxreported in the day-ahead mar-
ket. However, the actual consumptionD(MWh), demanded in real-time is uncertain. The
difference between the total scheduled demandq(θ,ϕ)from the day-ahead market and the
actual consumption places the grid in imbalance
ρ(D,(θ,ϕ))≡D−q(θ,ϕ), (10)
and must be balanced with an appropriate real-time supply adjustment. The role of the real-
time (balancing) market is therefore to provide this required quantity.
To safeguard operational security around the day-ahead plan, the TSO procures reserve
capacity in advance (FCR/FRR/RR) [European Commission, 2017d, Chapter 1, Article 14] for
maintaining physical balance between generation and demand. Operationally, it does so by
activating balancing resources (BSPs), the latter being the actors of the real-time market. A
BSP can be either a producer, or market actor with assets capable of rapidly adjusting electricity
production.
Each BSPj∈ Jis characterized by a type θj ≡( cj, gj)∈R >0 ×R ≥0, where ck >0 is
the marginal cost and gk ≥0 the awarded capacity. For simplicity, we assume that the set of
balancing resources awarded upward activation in the hour is the same with the BSPs.
2.3.2.1 Real-Time Market Allocation Rule.Given required balancing energyρ≥0 and
reported profile θ= (c, g)∈R |J| ≥0 ×R |J| ≥0 collecting BSPs’ costs and reserved capacities, the role
of the TSO is to dispatch BSPs for balancing real-time imbalance at minimum cost.
yRT ∈arg min
y∈R|J| +


 c⊤y: y≤ g, ∑ j∈J yj =ρ


 , (11)
where the inequality is component-wise and ∑ yj =ρis the balancing constraint ensuring
that dispatched reserves clear the system imbalance. Let G≡ ∑ gj denote the total reserved
capacity. For a consumption realizationD, the LP (11) has a solution only if Gsuffices for
supplying the emerged system imbalance.
Assumption 3(RT feasibility).We assume that the TSO reserves enough capacity for supplying the
real-time imbalances.
Assumption 4 ensures that the RT allocation rule (Equation 11) remains well-defined. Failure
to satisfy this condition poses a significant risk of grid instability; consequently, the TSO is
15

Energy
Price
Day-Ahead Market
Energy
Price
Real-Time Market
Figure 2: (Left) Day-ahead market schedule for a particular time slot. Costs and valuations
are placed in increasing and decreasing order, respectively. Each step corresponds to the best
response of the participant (see also equation (Equation 3)). The height of a step corresponds
to marginal values whereas the width to quantities. The marginal consumer and producer cor-
respond to those steps where the market curves “meet”. The vertical gap at clearing encodes
the range of market clearing prices. (Right) Real-time market curves. The dark-blue curve
represents the TSO’s demand for balancing energy, while the dark-green curve represents the
awarded capacities.
required to secure real-time reserves to account for tail events. This approach trades grid safety
with increased system costs, as the TSO must procure reserve capacity that may ultimately
remain idle with high probability. Therefore, accurate consumption forecasting is vital for
ensuring both grid reliability and market cost-effectiveness.
We can easily link the structure of the real-time allocation to the day-ahead allocation by
modeling the TSO’s commitment to balancing the grid as a fictitious consumer with finite
willingness to pay greater than any real-time cost,v o > cj for allj∈ J, and demand equal to
the imbalance, do ≡ρ
yRT ∈arg max
(xo,y)∈R+×R|J| +


 vo xo − c⊤y:x o ≤d o, y≤ g, ∑ j∈J yj =x o


 . (12)
Similarly to the discussion in paragraph 2.3.1.1, we impose the following assumption for en-
suring uniqueness of the real-time allocation.
Assumption 4(RT strict merit order).We assume cj′ ̸= cj for j′ ̸=j.
Proposition 3(Uniqueness of real-time allocation).Under Assumption 3 and Assumption 4, and
for any realized consumption, the real-time problem (Equation 11) has a unique minimizer.
Proof.Given that the TSO’s valuation is always greater than any real-time cost, under distinct
marginal costs, no more than one real-time producers can be marginal and hence, for eachD,
allocation is pinned down by market clearing (see also proof of Proposition 1)
Given that for each consumption realization the real-time allocation rule is structurally the
same with the day-ahead allocation rule, the definition of real-time competitive equilibria, and
pricing rules are also follow directly from the discussion of paragraph 2.3.1.1. Accordingly,
under Assumption 3, for each realized consumptionD, strong duality holds for (Equation 11)
and there exists dual optimal p⋆(D), that we call real-time market clearing price, that regulates
real-time producers’ incentives so that the real-time system imbalance is supplied
y⋆ j ∈argmax
y∈[0,gj]
p⋆(D) y− cjy(13)
16

and
ρ= ∑ y⋆ j . (14)
Since the TSO commits to delivering the day-ahead schedule,v o > p⋆(D)and hence, there
exists large enough budgetw o >0 such that for eachD, TSO is allocated the grid imbalance
ρ(D,x ⋆),
x⋆ o (D) =ρ(D,x ⋆),w o ≥ p⋆(D)ρ(x ⋆,D),Q−a.e. (15)
Definition 4(Real-time market).Given day-ahead consumers’ allocations(x ⋆ i )|I| i=1, a real-time market
is a price p⋆(D)and allocations  x⋆ o (D),( y⋆ j (D)) |J| j=1  such that (Equation 13), (Equation 14), and
(Equation 15) hold.
Once again, (x⋆ o (D), y⋆(D), p⋆(D) ) are primal-dual optimal for (Equation 11). Moving for-
ward, fairness for the real-time mechanism is feasible only if the real-time pricing rule spans
real-time market clearing prices.
2.3.2.2 Real-Time Market Pricing Rule.Order balancing units by increasing costs, with
cumulative capacities Gr = ∑ℓ≤r g(ℓ), and define m(ρ)≡min{r:ρ≤ Gr}. The real-time
uniform pricing policy is defined as the marginal cost of the marginal unit:
pRT(θ,ϕ, θ,D)≡ c(ρ), (16)
where again, we slightly abuse notation by writing c(ρ)instead of c(m(ρ)) . Similarly to (Equa-
tion 8) the marginal cost of marginal producer supports real-time competitive allocation only
if
c(ρ)>v(ρ+1). (17)
This condition can be easily satisfied assuming the existence of a second real-time consumer
with zero valuation.
Assumption 5.We assume that the TSO is always able to adjust market curves so that (Equation 17)
holds.
2.3.2.3 Real-Time Market Payment Rule.On top of their operational role, TSO’s are granted
financial role to act as a real-time settlement counterparty: they pay BSPs for the balancing en-
ergy they deliver and charge (or credit) Balance Responsible Parties (BRPs) for their deviations
from schedule.
Leto i(θ,ϕ)≡d i −x DA i (θ,ϕ)be BRPi’s deviation. With one-price settlement at the real-time
pricep RT(D,θ,ϕ), BRPs pay their imbalance
tRT i (D,θ,ϕ)≡ −p RT(θ,ϕ, θ,D)o i(θ,ϕ)1 h xDA i (θ,ϕ)̸=0 i , (18)
and BSPs receive
tRT k (D,θ,ϕ)≡+p RT(θ,ϕ, θ,D)y RT k (D,θ,ϕ). (19)
The real-time settlement process requires knowledge of di in order to allocate imbalance charges
to each BRP , and this information is typically provided via metering. A BRP can either be the
17

participant itself or an appointed representative that takes on the financial responsibility for
imbalances. Conceptually, BRPs serve as the TSO’s financial counterparties in the same way
that buyers serve as the NEMO’s counterparties in the day-ahead market.
Letx o(D), y(D)≡( yj(D)) |J| j=1, and t≡  to(D),( tj(D)) |J| j=1  denote the real-time outcomes,
where to(D) = p(D)x o(D)and tj(D) = p(D) yj(D).
Definition 5(Real-time mechanism).Under Assumption 4, the real-time mechanism with money is
defined as
MRT(·,θ,ϕ,D)≡  yRT(·,θ,ϕ, θ,D),t RT(·,θ,ϕ, θ,D)  : θ7− →  xo, y(D), t(D) 
with y RT(·)given by (Equation 11), t RT(·)≡  tRT i (·),t RT k (·)  given by (Equation 18) and (Equa-
tion 19), and p RT(·)given by (Equation 16).
The day-ahead market operator (NEMO) implements only the day-ahead allocation and uni-
form payments as a function of submitted bids. The imbalance settlement is implemented by
the BRP/TSO layer, which observes metered consumption and applies an exogenous settle-
ment rule. Incentives must therefore be analyzed in the composed mechanism that we now
define:
Definition 6(Energy mechanism).Under Assumption 1–Assumption 4, the energy mechanism is a
direct mechanism with money defined as
ME(D)≡  xE(·),t E(·,D)  :(θ,ϕ, θ)7− →  x,y,t, xo, y(D), t(D)  ,
where xE(·)≡  xDA (·),x RT(·)  and tE(·,D)≡  tDA (·),t RT(·,D)  .
Observe that the day-ahead and real-time markets form two sequential equilibria, where the
real-time equilibrium is driven by the day-ahead schedule. Moving forward, it is important to
characterize the defined institutions w.r.t. whether they preserve money.
Definition 7(Ex-post budget balance).A mechanism isex-post budget balancedif
∑ tk(·,D) =0 for all type profiles.
Neither the day-ahead nor the real-time mechanism is ex-post budget balanced in isolation
due to imbalance settlement. Nevertheless, the energy mechanismM E(D)is ex-post budget
balanced by construction since
∑
i∈I
tDA i (θ,ϕ) +∑
j∈J
tDA j (θ,ϕ) +∑
i∈I
tRT i (θ,ϕ, θ,D)
=p RT(θ,ϕ, θ,D)

 ∑
j∈| J|
yRT j (θ,ϕ, θ,D)− ∑
i∈I
δi(D,θ,ϕ)


+p DA (θ,ϕ)

∑
j∈J
yDA j (θ,ϕ)− ∑
i∈I
xDA i (θ,ϕ)
!
=0.
(20)
18

3 Incentives
Market participants have preferences over the market outcomes, typically expressed as utility
functions derived from their private types. On the basis of their private information, the pub-
licly available institutional framework and their knowledge about the world and the others,
they best respond to the induced game so as to influence the social choice for their own benefit.
As we already saw in Section 2, the response of the real-time mechanism, driven by the
day-ahead schedule, determines energy costs to the final consumers and affects grid stability.
In particular, any bias of the day-ahead schedule from the actual consumption increases im-
balances which later on are bought by the end consumers via the imbalance settlement (Equa-
tion 18). Beyond financial damage, large biases threaten operational security by destabilizing
the power grid.
3.1 Social Choice
As we saw in Section 1, empirical observations in European energy markets—and, in particu-
lar, inspection of consumption data from [ENTSO-E, 2026] reveal a systematic underestimation
of realized demand in the day-ahead stage. While forecast errors are always present in practice,
the severity and persistence of this underestimation motivates the hypothesis that day-ahead
market consumers are strategically misreporting their demands.
To investigate this hypothesis, we assume that valuations, costs and nominal capacities are
publicly available or at least, they can be inferred, and focus on the demands. Let d≡(d i)i∈I
denote the vector of true (private) demands. Building on the discussion in paragraph 2.3.1.1, if
day-ahead players were acting in isolation, the resulting day-ahead allocation would be Pareto
fair relative to the private types and in the absence of strategic bias, the TSO would have to
safeguard only for the inherent uncertainty of the actual consumption.
Consequently, Pareto fairness in the Day-Ahead stage is a prerequisite for minimizing real-
time costs and preventing grid failures. Given that all types except demands are public, truth-
ful reporting of demands in the day-ahead mechanism becomes the necessary and sufficient
condition for Pareto fairness.
Given that the day-ahead and real-time institutions are linked, incentives for demand
under-reporting in the day-ahead stage might be induced by preferences that extend beyond
the day-ahead outcomes. Therefore, we benchmark the entire energy institution (see Defini-
tion 6) against the corresponding market equilibria
ME : d7− →  (x⋆,y ⋆,t ⋆),  x⋆ o (D), y⋆(D), t⋆(D)   . (21)
Intuitively, when the day-ahead allocation is truthful, the real-time imbalance varies around
zero, thus minimizing risk of grid instability, the real-time price and the overall energy costs. A
nonzero average deviation means that the day-ahead plan inherits some strategic component
(strategic bias). That said, observe that under public values, costs, and generation capacities, if
MDA : d7→ (x⋆,y ⋆,t ⋆) , (22)
is truthfully implemented, then so is M RT and hence M E. Crucially, because existence and
uniqueness conditions are independent of the demands(d), we can analyze incentives with-
out concern that varying the demand reports will compromize the well-definedness of (Equa-
tion 21).
19

3.2 Setup
Consumers in the day-ahead-mechanism privately observe demands from some distribution.
They also maintain a belief about the others types d −i and actual consumptionD, usually
formed by aggregating past profiles and states of the world.
Let(d −i,D)∼P i be such a belief maintained playeriand letP −i denote the associated
marginal w.r.t. d−i. Then, for a given sampled private type, they decide based on that sub-
jective belief and play a subjective equilibrium (see [Sorin, 1992, Aumann, 1992, Kalai and
Lehrer, 1995]).
Unlike Bayes-Nash, subjective equilibria are inefficient since there is no guarantee that hon-
est forecasting will ever emerge. If, however, under the energy mechanism, all consumers were
required to report their demands truthfully, and this requirement were common knowledge,
then the induced game would admit a well-defined common prior.
In order the mechanism participants to report truthfully on the basis of their knowledge,
mechanism should be such that they rationalize truth-telling –approximately– as their best
response.
Definition 8(ε-Bayesian Strategy-Proofness).If bidders draw their types from some distribution
P=× m i=1Pi, then a direct mechanismMisε-Bayesian strategy-proofness, or (ε-Bayesian Incentive
Compatible (ε-BIC)) with respect to P if for each bidder i∈I
Eθ−i∼P−i
h
Ui (θi, M(θi,θ −i))
i
≥E θ−i∼P−i
h
Ui

θi, M

θ′ i,θ −i  i −ε,
for all potential misreportsθ ′ i, in expectation over all other bidders bidθ −i. A mechanism is Bayesian
strategy-proof if it is 0-Bayesian strategy-proof (resp. 0-BIC).
The implementable preferences over the mechanism’s outcomes span positive combinations
of consumers in the day-ahead market, producers in the day-ahead market and producers in
the real-time market. However, under the defined institutions (see Assumption 1 and As-
sumption 4), day-ahead producers’ components would constrain the demand under-reporting
incentives and hence act against what we empirically observe in the European electricity mar-
kets. For that reason, we rule them out of the incentive study.
The incentive question studied in this section is whether, under only cross-market owner-
ship (prosumers), the rational behavior under the defined institutions is compatible with the
market equilibria (see Section 2).
3.3 Consumers
We now study the incentives of consumers in the energy institution. Typically, preferences
over the day-ahead consumption outcomes are implemented by (LSEs), the latter being asso-
ciated with their own clientele. Thus naturally, such entities are modeled as a single consumer.
Consumeri’s preferences over outcomes(x,t)of the energy mechanism are given by
Ui(x,t) =v i xi +t i.
Being aware of the institutional framework, each consumer affects the social choice by acting
rationally and reporting their demand d i ∈R ≥0 to the day-ahead institution so that their
preferences are maximized in expectation. Let(d ′ i, d−i)∈R |I| ≥0 be the reported demand profile
in the day-ahead mechanism. At that profile, under mechanism M E, consumeri∈Iderives
net utility
Ui

di, M E(d′ i, d−i)  =v idi +t DA i (d′ i, d−i) +tRT i (D, d′ i, di, d−i), (23)
20

where, according to (Equation 9)
tDA i (d′ i, d−i) =−p DA (d′ i, d −i)x DA i (d′ i, d −i),
and according to (Equation 18)
tRT i (D, d′ i, di, d−i) =−p RT ρ(D,x DA (d′ i, d−i))  di −x DA i (d′ i, d −i)  1  xDA i ̸=0  .
The first term in (Equation 23) is consumeri’s utility from both the day-ahead and the real-
time stage. The second term is the payment charged to the consumer in the day-ahead stage.
If consume more than bought in the day-ahead stage, consumers have to buy the remainder at
the real-time price. The third term in (Equation 23) expresses the payment for these imbalances
as being defined by the real-time settlement (Equation 19). Wheni∈Iis zero day-ahead-
allocated the real-time settlement is not applied (see (Equation 18)) and the net utility vanishes.
To set the stage for our incentive analysis, given report d′ i ∈[0, d i]let
Ai ≡
n
d−i ∈R |I|−1 ≥0

 vi >p DA (d′ i, d−i) o , (24)
be the event within whichiis allocated when reporting d ′ i. LetA i =A(d i)be the event where
iis allocated when reporting truthfully, andA ′ i =A(d ′ i)the event whereiis allocated when
under-reporting.
Under Assumption 2 a consumer that is allocated in the day-ahead market is (fully) allo-
cated their report. Therefore,
xDA i (d′ i, d−i) =d ′ i 1 A′ i (d−i). (25)
If consumeriis allocated when reporting truthfully, so is when under-reports
1 Ai (d−i) =1=⇒1 A′ i (d−i) =1, (26)
since due to merit order, under-reporting in the day-ahead mechanism can only drop the day-
ahead price. In addition, observe that for some report d′ i
1
h
xDA i (d′ i, d−i)̸=0 i =1 A′ i (d−i). (27)
The point-wise gain obtained by under-reporting d′ i =d i −δ i is defined as
Gi

di, M E(di −δ i, d−i)  ≡U i  di, M E(di −δ i, d−i)  −U i  di, M E(di, d−i)  . (28)
Given their true (private) demand, consumers decide about their report by maximizing their
utility in expectation over all other reports and actual consumption. By plugging (Equation 25),
(Equation 26), (Equation 27) into (Equation 28) we obtain:
Gi

di, M E(di −δ i, d−i)  =  pDA (di, d−i)1 Ai −p DA (di −δ i, d−i)1 A′ i  di
+

pDA (di −δ i, d−i)−p RT(ρ)  δi1 A′ i ,
whereρ=ρ(δ i) =D− ∑l xDA l  di −δ i, d−i  . At this point we assume that consumeribelieves
21

that she is certainly allocated.
Assumption 6(Certain allocation).When reporting truthfully, total demand does not exceed total
supply capacity:d i + ∑j̸=i dj ≤G |J| almost surely, so thatPr(A i) =1.
Under Assumption 6, Pr(A ′ i) =1. By taking expectations (Equation 29) reads
E(D,d−i)∼Pi Gi

di, M E(di −δ i, d−i)  =E h pDA (di, d−i)−p DA (di −δ i, d−i) i di
+E
h
pDA (di −δ i, d−i)−p RT(δi, d−i) i δi
≤E
h
−p DA (di −δ i, d−i) +pDA (di, d−i) i di
+E
h
pDA (di, d−i)−p RT(0, d−i) i δi, (29)
whereE

pRT ρ(δi) 

 d−i  =p RT(δi, d−i), and the inequality follows because the day-ahead
price increases with the demand report ofiand the real-time price is increasing with imbalance
ρ. According to the first term of (Equation 29), by requesting less energy, consumeripulls the
day-ahead price down. For handling the second term of (Equation 29) we state the following
Assumption 7(Real-time market is more expensive than the day-ahead market).When con-
sumer i reports truthfully, in expectation over all others bidd −i
E
h
pDA (di, d−i)−p RT(0, d−i) i ≤0. (30)
Moving forward, because the inverse supply curve is piece-wise constant, if the reduction stays
within the same step, the same producer remains marginal and the price does not change at
all. Further, the price drops only if the reduced demand crosses a step boundary in the supply
curve.
The following Lemma extends Lipschitz continuity to piece-wise constant inverse supply.
Lemma 1(Extending Lipschitz continuity to the piecewise constant inverse supply curve).For
alld −i in the support of P−i, all feasible demandsd i, and all under-reportsδ i ∈[0, d i],

pDA (di, d−i)−p DA (di −δ i, d−i)

 ≤L|δ i|+2H, (31)
where
L=max
0≤j≤|J|−1
cj+1 −c j
Gj+1 −G j
, 2H=2 max
0≤j≤|J|−1
|cj+1 −c j|.
Proof.LetD=d i + ∑j̸=i dj denote the total demand under truthful reporting andD ′ = (di −
δi) +∑j̸=i dj the total demand under the under-report, so thatD−D ′ =δ i. From (Equation 6)
and (Equation 7), within the eventA i the day-ahead market clearing price equals the inverse
supply functionc:[G 0,G |J| ]→R ≥0 evaluated at total demand:
pDA (di, d−i) =c(D),p DA (di −δ i, d−i) =c(D ′),
so the price difference we seek to bound is|c(D)−c(D ′)|.
22

The inverse supply function is piecewise constant over the partitionG 0 <G 1 <· · ·<G|J| :
c(x) =c j forx∈[G j,G j+1),j=0, 1, . . . ,|J| −1.
It has|J|jump discontinuities at the partition points, with jump sizes|c j+1 −c j|.
Step 1: Piecewise linear interpolant.We construct a continuous approximation ofcby connecting
the corners
(G0,c 0),(G 1,c 1), . . . ,(G |J| ,c |J| )
with straight line segments. This defines the piecewise linear interpolantg:[G 0,G |J| ]→R ≥0,
given on each subinterval[G j,G j+1]by
g(x) =c j + cj+1 −c j Gj+1 −G j (x−G j).
By construction,gis continuous on[G 0,G |J| ], linear on each subinterval[G j,G j+1], and agrees
withcat every partition point:g(G j) =c(Gj) =cj for eachj=0, 1, . . . ,|J|.
Step 2: Lipschitz constant of the interpolant.Sincegis piecewise linear and continuous, it is
Lipschitz continuous with global Lipschitz constant
L=max
0≤j≤|J|−1
|cj+1 −c j|
Gj+1 −G j
.
That is, for allx,y∈[G 0,G |J| ],
|g(x)−g(y)| ≤L|x−y|.
Step 3: Pointwise approximation error.Fixx∈[G j,G j+1). On this interval,c(x) =c j, while the
interpolant satisfiesg(x)∈[min(c j,c j+1), max(c j,c j+1)]. Thus
|c(x)−g(x)|=|c j −g(x)| ≤ |cj+1 −c j|.
Taking the supremum over allxand all subintervals,
H≡ ∥c−g∥ ∞ ≤max
0≤j≤|J|−1
|cj+1 −c j|.
The quantityHis bounded by the largest jump in the inverse supply function.
Step 4: Combining.Applying the triangle inequality to the decompositionc= (c−g) +g,
|c(D)−c(D ′)|=|c(D)−g(D) +g(D)−g(D ′) +g(D′)−c(D ′)|
≤ |c(D)−g(D)|+|g(D)−g(D ′)|+|g(D ′)−c(D ′)|
≤ ∥c−g∥∞ +L|D−D ′|+∥c−g∥ ∞
=L|δ i|+2H,
where the last line uses|D−D ′|=|δ i|and∥c−g∥ ∞ ≤H.
Empirical evidence suggest that the day-ahead market clears within a sub-range of costs where
23

the Lipschitz part and the price gap are both very small.
3.3.1 Anti-Concentration of Aggregate Demand.
While Lemma Lemma 1 alone yields a deterministic bound on the gain from the day-ahead
price drop, this bound can be further tightened by accounting for the fact that the price change
occurs only when the deviation causes total demand to cross a supply step boundary. Whether
or not this crossing occurs depends on where the aggregate demand of other players ∑j̸=i dj,
happens to fall relative to the step boundaries of the supply curve. If playeri’s beliefsP −i are
sufficiently spread out —that is, if no small interval of possible demand values is assigned too
much probability—then the chance of such a crossing is small, and the expected gain shrinks
accordingly.
As mentioned earlier in Section 3.2, players form their beliefs about others’ total demand
from historical market data. The condition we require is that these beliefs do not concentrate
excessively in any narrow interval. This is a rather mild requirement: it holds whenever the
historical demand data is not pathologically concentrated at a single point and it is directly
verifiable from past data.
The appropriate tool for formalizing this condition is theL´ evy concentration function, a classi-
cal object in probability theory introduced by L´evy [L´evy, 1937] and developed systematically
by Petrov [Petrov, 1975, Chapter 3].
For a random variableXand a widthδ≥0, the L ´evy concentration function is defined as
Q(X,δ)≡sup
x∈R
Pr

X∈[x,x+δ]

. (32)
It measures the maximum probability thatXplaces on any interval of widthδ. A small value of
Q(X,δ)means that the distribution ofXis spread out and does not concentrate too much mass
in any narrow region. As we show below, the L ´evy concentration function of the aggregate
demand ∑j̸=i dj is small whenever enough individual players exhibit variability in their bids.
This follows from the Kolmogorov–Rogozin inequality, which we now recall.
Proposition 4(Kolmogorov–Rogozin inequality [Rogozin, 1961]; see also [Petrov, 1975, Chap-
ter 3, §2]).Letξ 1, . . . ,ξn be independent random variables. For any l>0, define
Qk(l) =sup
x∈R
Pr

ξk ∈[x,x+l]

,s=
n
∑
k=1

1−Q k(l)

. (33)
Then for any F≥l,
sup
x∈R
Pr

n
∑
k=1
ξk ∈[x,x+F]
!
≤ C F l √s, (34)
where C>0is a universal constant.
ANTI-CONCENTRATION OF AGGREGATE DEMAND
When many independent random quantities are summed, the resulting distribution can-
not concentrate too much on any narrow interval: the probability it assigns to a window
of fixed width decays at rate 1/ √nin the number of summands. In our setting, the ag-
gregate demand reported by all players other thaniplays the role of this sum. As the
market grows, that aggregate spreads out, and it becomes increasingly unlikely to fall
24

within a neighbourhood of a supply-curve breakpoint — the only region in which a uni-
lateral underreport can alter the clearing price. Smoothness of the collective is therefore
what limits individual manipulation in every result that follows.
In our setting,ξ j =d j for eachj̸=i, and the sum ∑j̸=i dj is the aggregate demand of all
players other thani. The quantityQ j(l) =supx Pr(dj ∈[x,x+l])measures how concentrated
playerj’s bid is: it equals one if and only if playerjalways bids within the same interval
of widthl, and is strictly less than one whenever playerj’s bid varies beyond that width.
The quantity 1−Q j(l)captures how much variability playerjcontributes, and the sums=
∑j̸=i (1−Q j(l))aggregates this variability across all other players. Proposition 4 then says that
the more players exhibit variable bidding behavior, the more spread out the aggregate demand
is, and the smaller the L´evy concentration function becomes.
This motivates the following assumption, which is a primitive condition on individual con-
sumers’ reporting behavior.
Assumption 8(Non-degenerate demand report variability).There exist constants l>0and
κ∈(0, 1]such that for at least m players j∈I\ {i},
Qj(l)≡sup
x∈R
Pr

dj ∈[x,x+l]

≤1−κ. (35)
Assumption 8 says that there exist at leastmconsumers that do not always report within
the same narrow interval of widthl: each such consumer’s report varies by more thanlacross
market realizations. The constantκquantifies the minimum variability each of these players
exhibits. This is a weak and empirically verifiable condition: it fails only if nearly all players
report the exact same quantity in every market period, which would mean there is essentially
no demand uncertainty. In any realistic energy market variability in weather, and individual
consumption ensures that many consumers’ demands fluctuate, so bothmandκare bounded
away from zero.
Assumption 9(Proportional demand variability).There exists r∈(0, 1]such that the number of
players m satisfying Assumption 8 is at least a fixed fraction of the total number of consumers|I|:
m≥r|I|. (36)
Assumption 9 says that the share of players with variable demand does not vanish as the
market grows. It holds whenever the sources of demand variability — weather, economic
activity, individual consumption patterns — affect a stable fraction of the population.
We are now ready to state the first result of this section.
Theorem 1(Vanishing incentive to misreport for consumers).Under Assumption 7, Assump-
tion 8, and Assumption 9, for allε>0there exists N∈Nsuch that for all|I|>N, for any consumer
i∈I
E d−i∼P−i
h
Ui

di, M E(di, d −i) i ≥E d−i∼P−i h Ui  di, M E(d′ i, d −i) i −ε, (37)
for all potential misreportsd ′ i ∈[0, d i], in expectation over all other bidders bidd −i. Specifically, the
gain from misreporting is bounded by
ε(|I|) = C(L d
3
+2H d
2
)
l
p
r|I|κ
|I|→∞
− − − →0. (38)
25

VANISHING INCENTIVE TO MISREPORT FOR CONSUMERS
A consumer can profit from under-reporting her demand only when the deviation shifts
the day-ahead clearing price. Such a shift requires the aggregate report of the other play-
ers to fall within her deviation of a supply-curve breakpoint. By the anti-concentration
inequality, this event occurs with probability of order 1/
p
|I|, and the maximal attain-
able gain decays at the same rate. Consequently, for any prescribed toleranceε>0 there
exists a market size beyond which no consumer can gain more thanεfrom any misre-
port. Truthful reporting on the consumer side is thus an approximate equilibrium of the
standard mechanism ME, with a slack that vanishes as the market grows.
Proof.Our goal is to upper bound the expected gain (Equation 29). Under Assumption 7
E(D,d−i)∼Pi Gi

di, M E(di −δ i, d−i)  =E d−i∼P−i h ∆p DA (di,δ i, d−i)d i i . (39)
Using the identity|∆p DA |=|∆p DA | ·1{∆pDA ̸=0}and Lemma Lemma 1,
E(D,d−i)∼Pi Gi

di, M E(di −δ i, d−i)  ≤(Ld 2 i +2Hd i)E d−i∼P−i h 1  ∆p DA ̸=0 	 i . (40)
The event{∆p DA (di,δ i, d−i)̸=0}occurs only if ∑j̸=i dj falls in an interval of widthδ i. Under
Assumption 8, at leastmplayers satisfyQ j(l)≤1−κ, givings= ∑j̸=i (1−Q j(l))≥mκ.
Applying Proposition 4,
Pr

∆p DA (di,δ i, d−i)̸=0

 Ai  ≤sup
x∈R
Pr

∑
j̸=i
dj ∈[x,x+δ i]
!
≤ Cδ i
l √mκ . (41)
Substituting (Equation 41) into (Equation 40),
E(D,d−i)∼Pi Gi

di, M E(di −δ i, d−i)  ≤(Ld 2 i +2Hd i)· Cδ i l √mκ . (42)
Taking the supremum over all feasible under-reportsδ i ∈[0, d i]and usingδ i ≤d i ≤ d,
sup
δi∈[0,di]
(Ld2 i +2Hd i)· Cδ i l √mκ ≤ C(L d
3
+2H d
2
)
l √mκ . (43)
Declaring
ε= C(L d
3
+2H d
2
)
l √mκ ,
and subsequently adopting Assumption 9 completes the proof.
3.3.2 Empirical Evidence for Small Cost Gaps at Market Clearing.
Recall from Section 2.3.1 that in day-ahead electricity markets, the clearing price is set by the
marginal producer—the most expensive unit needed to meet total demand. Empirical studies
show that, for a large percent of operating hours, this marginal producer is a natural gas-fired
26

power plant. In European day-ahead auctions, Zakeri et al. [Zakeri et al., 2023, p. 2778] find
that gas-fired plants set the wholesale price approximately 80% of the time [Zakeri et al., 2023,
p. 2785, Fig. 5] and a European Commission study confirms similar findings [Gasparella et al.,
2023].
In the US, the PJM day-ahead market clears using cost-based offers from the same power
plants [PJM Interconnection, 2024a, Section 5, p. 63–80], and the Monitoring Analytics State of
the Market Report shows that fuel costs—mainly gas—constitute the dominant component of
day-ahead clearing prices [Monitoring Analytics, 2024, p. 143–148].
When gas is the marginal fuel, the cost gaps between consecutive producers in the merit
order are small, because all gas-fired units share the same fuel price and differ only in their
heat rates—a measure of how efficiently they convert fuel to electricity [Kirschen and Strbac,
2018, Chapter 3].
In a large market such as PJM, the combined-cycle gas power plants contain a large number
of units spanning a narrow range of heat rates [U.S. Energy Information Administration, 2021,
2023] across tens of thousands of megawatts of capacity [PJM Interconnection, 2024b]. Be-
cause these units share the same fuel and differ only slightly in efficiency, their marginal costs
are tightly grouped, and the cost gap between any twoconsecutiveunits in the merit order is
negligibly small relative to the price level.
Remark 1(Magnitude ofε).Theε-BIC boundε=C(L d
3
+2H d
2
)/(l √mκ)is small when: (i)
H is small, which holds when the market clears within the gas bundle (Section 3.3.2); (ii) dis small
relative to total demand, which holds when individual consumers are small relative to the market; and
(iii) m·κis large, which holds when many players exhibit uncertain demand behavior. In a market with
|I|comparable players where m is proportional to|I|(see Assumption 9), we obtainε∼O(1/
p
|I|),
which vanishes rapidly as the market grows.
According to Remark 1, consumers have no incentive to under-report in a large market.
Next, we study a subset of day-ahead market consumers — namely, consumers who own
generation assets in the balancing market and can produce energy in real time. We call these
consumers prosumers (see also Section Section 2.1). As we will see, under the same market
parameters and conditions stated in Theorem 1 (and Remark 1), prosumers’ gain from under-
reporting is lower-bounded by a strictly positive constant. That is, there exists a subset of
players inIwhose gain from under-reporting does not go to zero as the market grows (see
Theorem 2).
3.4 Cross-Market Ownership & Prosumers
Consumers might also own one or more generation assets in the real-time market. We refer
to such actors that buy energy in the day-ahead market while owning shares on production
(generation) units in the real-time market as prosumers (see Section 2.1).
Let(α i,1, . . . ,αi,|J| )be the convex combination of shares for prosumeri∈Iover generation
assets. Then, prosumers’ preferences over the energy mechanism’s outcomes(x,t, y, t)read:
Uα i (x,t, y, t) =Ui(x,t) +∑
l∈ J
αil

tl − cl yl

. (44)
Each prosumer then, influences the social choice by acting rationally and reporting their de-
mand d i ∈R ≥0 to the day-ahead institution so that her preferences are maximized. Let
(d′ i, d−i)∈R |I| ≥0 be the reported demand cap profile in the day-ahead mechanism. At that
profile, under mechanism ME, prosumeri∈Iderives utility
Uα i  di, M E(d′ i, d −i)  ≡U i  di, M E(d′ i, d −i)  +C i  D; d ′ i, d −i  , (45)
27

where
Ci

D; d ′ i, d −i  ≡1 h xDA (d′ i, d−i)̸=0 i ∑
l∈ J
αil

pRT(D, d′ i, d−i)− cl  yRT l (D, d′ i, d−i  . (46)
Under the day-ahead and real-time institutions described in Section 2, by under-reporting
their day-ahead demand, a prosumer lowers the net day-ahead schedule thus increasing both
the likelihood and the magnitude of upward real-time imbalances in such a way so that pro-
sumer’s generation asset gets activated and offers real-time revenues.
Due to the piecewise-constant structure of the real-time inverse supply curve (see Figure 2),
the resulting real-time payoff is a discrete random variable. Its realized value is determined by
the specific capacity bin
Bj ≡[ Gj, Gj+1),
into which the aggregate system imbalance materializes.
Formally, Lemma Lemma 2 expresses the second term in (Equation 45) as a state-contingent
balancing-energy payoff whose availability and size are supported by maintaining shares over
the reserved generation capacity in real time.
Lemma 2.Let
wij ≡ ∑
l∈ J:l≤j−1

cj − cl

αil gl,j∈ J.
and fix reportd ′ i. Then, the second term of (Equation 45) can be expressed as
Ci

D; d ′ i, d −i  =1 h xDA (d′ i, d−i)̸=0 i ∑
j∈J
wij 1

ρ(di, d−i)∈B j

. (47)
Proof.Fix some report d ′ i and letρ=D− ∑i xDA i (d′ i, d−i), be the corresponding imbalance
for that report. Ifρ∈B l, the market clears at producerl(i.e. producerlis marginal), hence
pRT(D, d′ i, d−i) =cl which implies Cl(D, d′ i, d−i) =0. Moreover, if
cl >p RT(di, d−i)⇐ ⇒ρ< Gl,
then producerlis not dispatched, soy RT l (D, d′ i, d−i) =0 and again Cl(D, d′ i, d−i) =0. Thus,
producerlyields positive profit only when the induced imbalance exceeds Gl+1. Whenever
the reporting cap di allows the imbalance to reach values above Gl+1,
Cl(D, d′ i, d−i) =∑
j∈J

cj − cl

gl 1

ρ∈[ Gj, Gj+1)

1 [l≥j ] . (48)
By aggregating acrossl,
Ci(D, d′ i, d−i) =∑
l∈ J
αil Cl(di, d−i) = ∑
j∈J

∑
l≥j
(cj − cl)α il gl
!
1

ρ∈[ Gj, Gj+1)

. (49)
Setting the term inside the parenthesis equal tow ij ≥0 for all(i,j)∈I× Jcompletes the
proof.
28

Prosumers are a subset of consumers. Our goal then is to identify an interpretable and feasible
(w.r.t. Assumption 1, Assumption 4, and Assumption 8) market instance such that prosumers
have incentives to under-report. This would then prove that ME is notε−BIC.
To begin with, according to (Equation 49), the energy mechanism partitions the real-time
capacity axis into mutually exclusive imbalance states (bins). Each prosumer then is provided
for free by the energy mechanism a portfolio of Arrow–Debreu-style contracts: the contract for
state Bj paysw i,j ifρlands in B j and zero otherwise. This is a flaw of the energy mechanism.
Recall Assumption 6 and define the probabilities
Pj(δi)≡E h Pr(Bj −δ i |d −i) i ,P j(0)≡E h Pr(Bj |d −i) i ,
and the probability shift∆P(δ i)≡P j(δi)−P j(0). Under Assumption 6, prosumer’s expected
gain from under-reporting d′ i =d i −δ i reads
E d−i∼P−i Gα i  di, M E(di −δ i, d−i)  =E d−i∼P−i Gi  di, M E(di −δ i, d−i)  +
wi,∆P(δ i)

.
Let βi ≡max δi∈[0,di] Ep RT(δi, d−i)be the the maximum expected real-time price that playeri
can influence by fully under-reporting, and let βidi the corresponding cost. Given the fact that
the day-ahead price is increasing w.r.t. the demand report, equation (Equation 29) yields
E d−i∼P−i Gi

di, M E(di −δ i, d−i)  ≥ −βidi (50)
Boundary-crossing decomposition.Letρ 0 ≥0 be the real-time imbalance when prosumeri
reports truthfully (δi =0), with continuous CMFF(x)≡Pr(ρ 0 ≤x), whereF(x) =0 forx≤0.
Then
Pj(δi) =F(G j+1 −δ i)−F(G j −δ i), (51)
and the mass crossing (from the left) boundary Gj when under-reporting byδ i is
Tj(δi)≡Pr

Gj −δ i ≤ρ 0 < Gk

=F( Gk)−F( Gk −δ i). (52)
Dropping the indexifromw i and writing∆w j ≡w j −w j−1, and using the boundary conditions
T1(δi) =T |J| (δi) =0 (no mass crosses 0 from the left, and no mass crossesG |J|), equations
(Equation 51)–(Equation 52) yield thegap-weighted inflowformula:

w,∆P(δ i)

=
J−1
∑
j=2
∆wj Tj(δi). (53)
Unimodal profits.Suppose the profit vector is unimodal across bins, i.e. there existsj p such
that
w1 ≤ · · · ≤wjp ≥ · · · ≥wJ−1. (54)
29

Then∆w j ≥0 forj≤j p and∆w j ≤0 forj≥j p +1, and (Equation 53) splits into

w,∆P(δ i)

=
jp
∑
j=2
∆wj Tj(δi)
| {z }
uphill crossings
−
|J|−1
∑
j=j p+1
|∆w j|T j(δi)
| {z }
downhill crossings
.
Under-reporting is therefore profitable atδi when the mass crossingprofit-increasingboundaries
dominates both the mass crossingprofit-decreasingboundaries and the baseline costβ iδi.
Unimodal mass function.We assume that the probability mass function is unimodal. Under
this assumption the boundary-crossing massesj7→T j(δi)are themselves unimodal injfor
every fixedδ i ∈(0, d i]: as Gj moves toward the high-probability region ofρ 0, the width-δ i
window massT j(δi) =Pr([Gj −δ i, Gj))first increases and then decreases.
Combined with unimodal profits (Equation 54), this gives clear intuition: profitable under-
reporting requires choosingδ i so that the (typically localised) boundary crossings with the
largestT j(δi)fall on the uphill sidej≤j p, while crossings on the downhill sidej≥j p +1
remain small.
Single-asset special case.Suppose prosumeriholds exactly one real-time generation asset on
binj 0, with payoffw≡w j0. Then
E d−i∼P−i Gα i  di, M E(di −δ i, d−i)  ≥w  Tj0(δi)−T j0+1(δi)  .
If moreoverj 0 =| J| −1 (the previous from rightmost bin), thenT|J| (δi) =0 and
E d−i∼P−i Gα i  di, M E(di −δ i, d−i)  ≥w T |J|−1 (δi). (55)
Theorem 2(Persistent incentive to misreport for prosumers).For all|I| ∈Nand under the same
assumptions as Theorem 1, there exists a prosumer i∈I, with true demandd i, and under-report
d′ i ∈[0, d i]such that,
E d−i∼P−i
h
Uα i  di, M E(d′ i, d −i) i −E d−i∼P−i h Uα i  di, M E(di, d −i) i ≥ε α i , (56)
in expectation over all other bidders bidd −i, whereε α i =d i(w qi − βi)is independent of
(|I|,r,C,H,m,κ).
The term di(w qi − βi)is the prosumer’s net gain from under-reporting, scaled by their de-
mand. The quantityw q i is the real-time profit rate: the revenue the prosumer earns per unit
of demand by pushing the imbalance across the boundary of their generation bin, wherew
is the cost gap between consecutive bins times the nominal capacity of the prosumer’s asset
andq i is the rate at which boundary-crossing scenarios are activated. The quantity βi is the
real-time price cost: the most the prosumer pays per unit of demand for the energy that spills
into real-time due to the under-report. The differencew q i − βi is the net rate: what the pro-
sumer earns from the real-time dispatch manipulation minus what they pay for the spilled
energy. The lower boundε α i is positive whenw q i > βi, meaning the prosumer earns more
from manipulating the real-time dispatch than they pay for the resulting real-time energy cost.
NON-VANISHING INCENTIVES TO UNDERREPORT FOR PROSUMERS
A prosumer is a market participant who, in addition to buying in the day-ahead market,
30

holds an ownership share in one or more real-time producers. By under-reporting her
day-ahead demand, she induces a positive imbalance to be covered in real time. When
that imbalance crosses the next generation capacity threshold of the real-time merit or-
der, her own asset remains dispatched and earns the cost gap between it and the next
producer. The resulting profit is determined by the real-time supply curve, the nominal
generation capacities and her ownership vector alone. Thus it is bounded below by a
strictly positive constant that does not depend on the market size. Cross-market own-
ership thus introduces a structural incentive to underreport that the standard settlement
cannot eliminate, however large the number of consumers becomes. That is, there is no
single toleranceεthat can serve all players simultaneously, and the standard mechanism
fails to be approximately incentive compatible.
Theorem 1 and Theorem 2 are contradictory in the following sense. Theorem 1 states that
for any toleranceε>0, the gain from misreporting for every consumer falls belowεonce
the market is large enough. Theorem 2 states that a prosumer — who is a player inI— has
gain at leastε α i >0 regardless of how large the market is. In particular, choosingε=ε α i /2 in
Theorem 1: for|I|large enough, every consumer’s gain is belowε α i /2, yet the prosumer’s gain
remains at leastε α i >ε α i /2. Therefore, the mechanism ME cannot beε-BIC with vanishingεfor
all players inI.
Below is the proof of Theorem 2:
Proof.Consider a prosumeriwho owns a single real-time generation asset in binj 0, where
j0 <| J| −1.
Step 1: Setup.The real-time supply curve is such that the cost gap between binj 0 and binj 0 +1
isw>0. This is the difference in cost between the prosumer’s asset and the next producer
on the real-time supply curve, which depends on their respective fuels and technologies. Cru-
cially,wis a property of the real-time supply curve and the prosumer and it is independent of
the day-ahead parameters(H,l,m,κ)that control the consumer boundεof Theorem 1.
Step 2: Imbanace distribution.Under truthful reporting (δ i =0), the real-time imbalanceρ 0 falls
within binj 0 with high probability and concentrates near the right boundary Gj0+1 of that bin,
The prosumer’s asset is the marginal real-time producer and earns zero profit.
Step 3: The prosumer under-reports.The prosumer sets d ′ i =0, i.e.,δ i =d i. This pushes d i units
of demand into real-time. In scenarios where the truthful imbalanceρ 0 was within di units to
the left of the boundaryGj0+1, the increased imbalance crosses into binj0 +1, a more expensive
producer is dispatched, and the prosumer’s asset becomes infra-marginal thus earningw.
Step4: Lower bound on the gain.From the single-asset special case, the prosumer’s expected gain
is (Equation 55)
E d−i∼P−i Gα i  di, M E(di −δ i, d−i)  ≥ −βidi +w T j0+1(di), (57)
Sinceρ 0 concentrates near the boundary Gj0+1, the CMFFplaces large mass just to the left of
this boundary, and the crossing probability satisfiesT j0+1(di)≥q i di for someq i >0. There-
fore,
E d−i∼P−i Gα i  di, M E(di −δ i, d−i)  ≥d i(w q i − βi). (58)
Step 5:If,wq i > βi, the right-hand side of (Equation 58) is strictly positive. Thus, declaring
εα i ≡d i(w q i − βi)>0, (59)
31

we observe thatε α i depends only on real-time parameters (w,q i, βi), the prosumer’s true de-
mand d i the maximum real-time cost βi, the real-time profitw, and not on the day-ahead
supply curve parameters(H,l,m,κ)that driveε→0 in Theorem 1. Therefore,ε α i remains
bounded away from zero under the same conditions that makeεvanish, which completes the
proof.
4 Mechanism Design
We design a mechanism for the two-stage energy institution (see Definition 6) consisting of a
day-ahead scheduling stage and a real-time balancing stage. The allocation rules in both stages
are fixed and reflect the existing regulatory framework. Uniform pricing is also taken as given.
In Section 3.1 we saw that under public costs, values and nominal capacities, if the day-ahead
institution is truthfully implemented, then so is the energy mechanism. Our design problem
then concerns the settlement rule faced by demand-side participants at the day-ahead stage.
The strategic component of the day-ahead schedule can destabilize the grid but also in-
crease the energy costs for consumers. In Section 3 we saw that under certain conditions, the
current imbalance settlement is unable to incentivize prosumers in reporting their demand
truthfully.
Moreover, we identify an additional major concern with the existing imbalance settlement
framework. Its reliance on metering introduces vulnerabilities to manipulation and measure-
ment errors, raising questions about its trustworthiness.
To this end, we propose an extended imbalance settlement mechanism
tDA,S i (·)≡t DA i (·) +Πi(·),i∈I, (60)
implemented by the day-ahead market, whereΠi(·)is chosen from an appropriate classCof mech-
anisms characterized by properties we define in Section 4.3. We have the following definition.
Definition 9(Extended Energy Mechanism).Under Assumption 1 – Assumption 4, the extended
energy mechanism is a direct mechanism with money defined as
MS(D)≡  xE(·),t S(·,D)  :(θ,ϕ, θ)7− →  x,y,t, xo, y(D), t(D) 
where x E(·)≡  xDA (·),x RT(·)  , t S(·,D)≡  tDA,S (·),t RT(·,D)  , and t DA,S (·)≡t DA (·) +
Π(·).
On the basis of Definition 9, our mechanism is obtained as the solution to the following opti-
mization problem
MS⋆(·)∈arg min
MS(·)∈C
(
E

ρ  d′ 1, . . . , d′ |I| 

 2 : d ′ i ∈arg max
x∈[0,di]
E∼P−i Uα i

di, MS(x, d−i)  ,∀i∈I ) .
In what follows, we characterize the setCby defining the specific properties this mechanism
must satisfy.
4.1 Information Constraints
The proposed settlement modification is intended to be implemented by the day-ahead market
operator (NEMO). Accordingly, we explicitly restrict the information available to the designer
to what is institutionally observable at the day-ahead stage and after delivery.
32

At the time settlement is computed, the designer observes:
(i) the full profile of day-ahead reports d= (d i)i∈I ;
(ii) the day-ahead clearing outcomex DA (d)and the cleared total ∑i∈I xDA i (d);
(iii) realizedsystem totalconsumptionDfor the delivery hour;
(iv) public historical data consisting of past day-ahead reports and realized system consump-
tions.
The designer doesnotobserve realized consumption at the level of individual day-ahead par-
ticipants or Balance Responsible Party (BRP) portfolios, nor any settlement allocation of real-
ized consumption to individual participants.
While individual BRP-level allocated volumes are calculated and used for imbalance set-
tlement by the TSO (or a nationally assigned settlement entity), they are outside the defined
scope of NEMO tasks (which concerns day-ahead/intraday coupling and clearing/settlement
of the resulting trades) and are subject to professional secrecy where they are treated as con-
fidential information under network codes: [European Commission, 2017b, EBGL Art. 2(15),
OJ L 312/10; Art. 52(1), OJ L 312/44; Art. 54(1), OJ L 312/45; Art. 11(3)–(4), OJ L 312/16]
[European Commission, 2015, CACM Art. 7(1), OJ L 197/33; Art. 13(3)–(4), OJ L 197/39].
4.2 Scoring Rule-Based Mechanisms
The inputs to the designer’s problem are the information available to the NEMO, the structure
of prosumer’s incentives and the publicly available market parameters. The market partici-
pants should be aware of the incentive changes applied by the NEMO.
Recalling our earlier notation, B j refers to thejth interval formed by the cumulative real-
time generation capacities,[ Gj, Gj+1). With d ′ i we denote the report of theiprosumer in the
day-ahead mechanism and with d −i the demands of the rest of the players. The real-time
imbalance is given byρ=D− ∑i xDA i (d′ i, d−i), whereDis the random (true) total consumption
andw i = (wij )j∈J is the real-time profit vector of prosumeri∈I.
Let1(d ′ i, d−i,D)denote the vector with components the indicator functions1(ρ∈B j),j∈
J. Then, on the basis of Lemma 2, at reported profile(d i, d−i), prosumer’s utility reads
Uα i  di, M E(d′ i, d −i)  =U i  di, M E(d′ i, d −i)  +
wi,1(d ′ i, d−i,D)  1 Ai (d−i). (61)
The term1 Ai (d−i)encodes the allocation event ofi∈Iwhen reporting d i (see (Equation 24)),
though, under Assumption 6 it can be omitted and hence its precise mechanics are not impor-
tant to the following discussion.
Information used by the designer.Prosumeri∈Ireports d ′ i so as to maximize their expected
utility. The designer observes others’ reports too. Thus, when conditioned on the others’
reports, prosumerisubmits d ′ i ∈[0, d i]and shares their belief
P(d′ i, d−i)≡E  1(d ′ i, d−i,D)

 d−i  ∈∆ |J|, (62)
about the imbalance with the mechanism. In expectation over the true total consumption given
the others submissions, prosumerireports d i so as to maximize
E∼D|d −iUα i (di, d−i,D)≡E ∼D|d −iUi(d′ i, d−i,D) +
wi,P(d ′ i, d−i)  . (63)
According to (Equation 63), prosumer’s incentives are forced by their profit vector and there
is no reason to expect them to report their belief truthfully.
33

Definition 10(Scoring rule, proper scoring rule, strictly-proper scoring rule).LetΩbe an out-
come space and∆the set of probability distributions onΩ. A scoring rule is a function
S:∆×Ω→R.
S is proper if, for every true distribution P∈∆,
Eω∼P [S(P,ω)]≥E ω∼P [S(Q,ω)]for all Q∈∆,
and strictly proper if equality holds only when Q=P.
The work of [McCarthy, 1956] is one of the earliest that formally links the value of information
to the convexity of a function, laying the groundwork for Bregman divergences. Then, [Savage,
1971] shows that every strictly proper scoring rule is expressed via the supporting hyperplanes
of a strongly convex function.
Lemma 3(Savage Representation for Scoring Loss Rules, [Savage, 1971, Gneiting and Raftery,
2007b]).For any strictly proper scoring rule S there exists a strictly convex functionϕ:∆ n →R,
n∈N, called the generating potential, such that:
S(P,Q) =−ϕ(Q) +D ϕ(Q∥P),
where the Bregman divergence induced byϕis:
Dϕ(Q∥P)≡ϕ(Q)−ϕ(P)−

∇ϕ(P),Q−P

≥0,
with equality if and only if Q=P, by strong convexity ofϕ.
That said, on the basis of the available information, the designer would like to penalize pro-
sumers’ incentives via a mechanism constructed from a familyϕ(·,γ):∆ |J| →Rof smooth,
µ(γ)-strongly convex (with respect to∥ · ∥p for somep≥1) real-valued functions parameter-
ized byγ∈Γ ϕ.
LetS ϕ(γ) be the corresponding scoring rule. The vectorγcontrols the modulus of strong
convexity of the function. Following Definition 10, a scoring rule is maximized if and only if
the player submits their subjective belief truthfully and hence it can be deployed as a properly
γ−tuned penalty to incentivize the player to report truthfully.
Although the NEMO has access to the player’s past reports, which could potentially be
used to form a probabilistic forecast the player, this is not the case for their true reports, as
indicated by the observability constraints (see Section 4.1). Hence, a scoring-rule penalty that
evaluates a player’s report solely on the basis of their forecast cannot be constructed.
What can be done instead is to score (Equation 62) against a distribution at zero that ex-
presses the true (competitive) imbalance (see Section 3.1). However, by doing so, even if player
ireport truthfully, (Equation 62) could be still far from zero because of the others−i.
We overcome this difficulty be designing a contrastive scoring rule penalty as follows:
4.2.1 Contrastive Scoring Rule-Based Payment
Given the past reports of playeri, d i, the past reports of the others (available information
see Section 4.1) d −i, and the past consumption realizationsD, letλ= |I|−1 |I| andD −i ≡λD
be an approximation of the actual consumption associated with all players except playeri.
This approximation becomes more accurate whenever players’ true demands are close to each
34

other. Letρ −i ≡D −i − ∑j̸=i dj be the imbalance associated with players−ionly and1 −i(d−i)
the vector with components the indicator functions1(ρ −i ∈B j),j∈ J.
On the basis ofρ −i the NEMO can form the probability mass function (PMF) about how
the rest of the players,−i∈I, predict their corresponding imbalance. Let
P−i(d−i)≡E

1 −i(d−i;λ)

d−i  (64)
be this PMF which is either communicated to or can be easily obtained by playeriagain, based
on past total consumption realizations, past reports and the coefficientλwhich is communi-
cated from the mechanism to the player.
Then, both forecasts are evaluated against a PMF centered at zero or more precisely, against
a PMF for which all the mass is concentrated, in the first bin (one-hot vector with the first
entry being the non-zero entry). LetQbe this PMF. The designer scores both (Equation 62)
and (Equation 64) againstQand forms the contrastive loss
Dγi

d′ i, d −i  ≡S ϕ(γi)  P−i(d−i),Q  −S ϕ(γi)  P(d′ i, d−i),Q  . (65)
Although the actual total consumption is observable, it is not needed to forming the above
difference. The mechanism announces to all consumers (including prosumers) of the day-
ahead market the following scoring-rule-based payment
Πγi

d′ i, d −i  ≡  Dγi  d′ i, d −i  + +ζ i, (66)
that acts as a penalty charged to playeri∈Iwhen reporting d ′ i while others report d−i. Here,
ζi is a real number and by[·] + we mean positive part.
According to (Equation 66), whenever the forecast constructed from all players performs
poorly relative toQ, while the forecast based on all players exceptiaccurately predicts their
share of the imbalance (demand), the discrepancy (Equation 65) is positive and is attributed to
playeri’s report. In this case, playeriis deemed responsible for the degradation in predictive
accuracy and should therefore be heavily penalized. In the case where the player contributes
more to forecast accuracy than the rest of the players, expression (Equation 65) is negative, and
the player receives payment equal toζ i.
Prosumer’s utility at profile(d ′ i, d−i)under mechanism M S reads
Uα i  di, MS(d′ i, d −i)  ≡U α i  di, ME(d′ i, d −i)  −Π γi (d′ i, d−i),
whereα≥0.
Bregman Divergence Properties.We recall two standard properties of Bregman divergences
that will be used latter when we prove the Theorem of this work (see Theorem 3).
Lemma 4(Three-Point Identity, [Chen and Teboulle, 1993]).For any P,P ′,Q∈∆ n, with n∈N:
Dϕ(Q∥P) =D ϕ(Q∥P ′) +Dϕ(P′∥P) +
∇ϕ(P ′)− ∇ϕ(P),Q−P ′ .
Lemma 5(Strong Convexity, [Nesterov et al., 2018]).Ifϕisµ-strongly convex, for all P∈∆ n,
then for all P,P ′ ∈∆ n, with n∈N:
Dϕ(P∥P ′)≥ µ 2 ∥P−P ′∥2 p.
At this point, we assume thatP i(di, d−i)lies betweenQandP i(d′ i, d−i)in the sense that the
35

player’s more honest report is closer to the truthQthan the manipulated report.
Assumption 10.The true report P(d i, d−i)lies between Q and P(d ′ i, d−i)in the Bregman sense:
Dϕ(Q∥P(d ′ i, d−i))≥D ϕ(Q∥P(d i, d−i)) +Dϕ(P(di, d−i)∥P(d ′ i, d−i)),P −i a.e.
This says that the direct divergence fromQtoP(d ′ i, d−i))is at least as large as the two-step path
Q→P(d i, d−i)→P(d ′ i, d−i)). In particular, it impliesDϕ(Q∥P(d ′ i, d−i)))≥D ϕ(Q∥P(d i, d−i)):
the manipulated reportP(d ′ i, d−i))incurs a strictly larger penalty than the more honest report
P(di, d−i).
Observe that Assumption 10 is equivalent, via the three-point identity (see Lemma 4), to:

∇ϕ(P(d i, d−i))− ∇ϕ(P(d′ i, d−i)),Q−P(d i, d−i)  ≥0,
which says that the direction fromP(d i, d−i)toP(d ′ i, d−i)in gradient space is opposed to the
direction fromP(d i, d−i)toward truthQ.
4.3 Objectives
Having designed the class our mechanism M S we are now in a position to state the objectives
we want it to satisfy.
4.3.1 Approximate Bayessian Incentive Compatibility
As we already mentioned in Section 3.1, (Equation 21) is truthfully implemented if, under
public valuations, costs and nominal capacities, the day-ahead mechanism is truthfully imple-
mented. Therefore, our focus is to truthfully implement (Equation 22). Our implementation is
such that, given everyone’s beliefs about uncertainty, the players’ play leads the mechanism to
the competitive benchmark. Hence, our objective isε-BIC: a singleεthat bounds the gain from
misreporting foreveryplayer in the (demand side of the) market.
As established by Theorem 1 and Theorem 2, the standard mechanism ME achievesε−BIC
for consumers with vanishingεas the market grows, but fails for prosumers whose gain is
bounded below byε α i >0, which as we saw, is independent of the day-ahead market size.
The following Theorem shows that the scoring rule mechanism MS reduces the prosumer’s
gain to at mostε(|I|) +ε S whereε(|I|)vanishes with market size andε S is a design constant
controlled by the strong convexity parameterµ(γ)and can be set less than the lower boundε α i .
Theorem 3(Scoring-Rule Energy Mechanism M S isε-BIC).Let S be a strictly proper scoring rule
associated with a generating potentialϕ γi that isµ-strongly convex. Then, under Assumption 10, for
allε>0there exists N∈Nsuch that for all|I|>N, for every player i∈I (consumer or prosumer),
and any misreportd ′ i ∈[0, d i),
Ed−i∼P−i
h
Ui

di, MS(di, d −i)  i ≥E d−i∼P−i h Ui  di, MS(d′ i, d −i)  i −ε− ∥wi∥2 2 2µ , (67)
in expectation over all other bidders bidd −i. For consumers (w i =0), the bound reduces to that of
Theorem 1.
SCORING-RULE RESTORATION OF INCENTIVE COMPATIBILITY
The day-ahead settlement is augmented with a contrastive payment built from a strictly
proper scoring rule. Each reported demand is mapped to a probabilistic forecast of the
36

real-time imbalance. A report whose implied forecast is substantially worse than the
one collectively implied by the remaining players incurs a fee. The level of that fee is
controlled by a single design parameterµ, the strong-convexity parameter of the under-
lying potential. Under the resulting mechanism, every player’s gain from misreporting
is bounded above by the consumer decay termε(|I|)plus a prosumer-specific residual
of magnitude∥w i∥2 q/(2µ). This residual is not a feature of the institution: it is a tunable
parameter that the designer can drive arbitrarily close to zero by increasingµ, thereby
restoring approximate incentive compatibility.
Theorem 3 provides a uniform bound on the gain from misreporting for all players under
the penalized mechanism MS. For consumers, the bound isε(|I|), which vanishes with market
size — the same as under M E. For prosumers, the bound has an additional term∥w i∥2 q/(2µ)
that reflects the real-time profit. This term does not vanish with market size, but the designer
controls it through the strong convexity parameterµ. A natural question is whetherµcan be
chosen large enough to make this term smaller than the prosumer’s gain under the original
mechanism ME. We first prove Theorem 3 and then state a Corollary (see Corollary 1), which
confirms that such a choice is always possible.
Proof.To simplify the notation, letP=P(d i, d−i)andP ′ =P(d ′ i, d−i)denote the PMFs over
real-time bins under truthful reporting and under the under-report, respectively, and letQ
denote the true PMF. We treat consumers and prosumers separately.
Case 1: Consumers (w i =0).The consumer’s gain under M S equals their gain under M E
minus the penalty difference. Then, from Lemma Lemma 3, and under Assumption 6, the gain
from under-reporting under mechanism MS reads
Ed−i∼P−i Gi

di, M S(d′ i, d−i)  ≤E d−i∼P−i Gi  di, M E(d′ i, d−i)  −

Dϕ(Q||P ′)−D ϕ(Q||P)

≤ε(|I|), (68)
where the last inequality follows from Theorem 1 — the penalty does not worsen the con-
sumer’s bound.
Case 2: Prosumers (wi ̸=0).The prosumer’s gain under M S is
Ed−i∼P−i Gα i  di, M S(d′ i, d−i)  ≤ε(|I|) +⟨w i,P ′ −P⟩ −

Dϕ(Q∥P ′)−D ϕ(Q∥P)

 , (69)
where the first term is the consumer component bounded by Theorem 1, the second is the
real-time profit, and the third is the penalty difference.
Step 1: Apply Assumption 10.
Ed−i∼P−i Gα i  di, M S(di, d−i)  ≤ε(|I|) +⟨w i,P ′ −P⟩ −D ϕ(P∥P ′). (70)
Step 2: Apply Lemma Lemma 5.
Ed−i∼P−i Gα i  di, M S(di, d−i)  ≤ε(|I|) +⟨w i,P ′ −P⟩ − µ 2 ∥P−P ′∥2 (71)
Step 3: Conjugate duality.
37

Ed−i∼P−i Gα i  di, M S(di, d−i)  ≤ε(|I|) +⟨w i,P ′ −P⟩ − µ 2 ∥P−P ′∥2 p
≤ε(|I|) +sup
∆∈R|J|
h
⟨wi,∆ ⟩ − µ 2 ∥∆∥2 p i
≤ε(|I|) +
∥wi∥2 q
2µ . (72)
Note that forw i =0 the bound reduces to that of Theorem 1.
Theorem 3 establishes that the prosumer’s gain under M S is at mostε(|I|) +∥w i∥2 q/(2µ).
Theorem 2 established that prosumer’s gain under M E can be at leastε α i >0. The penalty is
effective if the upper bound under the new mechanism is strictly below the lower bound under
the old mechanism. We now state that the designer can always achieve this.
Corollary 1(The penalty eliminates the prosumer’s advantage).Consider the prosumer from
Theorem 2 with lower boundε α i >0. For all|I|large enough thatε(|I|)<ε α i , anyµsatisfying
µ>
∥wi∥2 q
2

εα i −ε(|I|)  (73)
ensures that the prosumer’s gain underM S is strictly less thanε α i :
ε(|I|) +
∥wi∥2 q
2µ <ε α i . (74)
Such aµalways exists, since the designer controlsµthroughγ i (see also Table Table 1)
Of course,µcan be increased further to infinity but as we are going to see in the next section,
µposes a trade-off between eliminating prosumer’s incentives to under-reporting and a large
penalty when the same prosumer happens to report truthfully.
4.3.2 Approximate Penalty Guarantee for Honest Participants
Ideally, we would like the mechanism to impose zero expected penalty on any player who
reports truthfully:
Ed−i∼P−i Πγi

di, d −i

=0, (75)
for all true demands di and alli∈I. That is, an honest participant should expect zero penalty
in expectation over the others bid. To achieve (Equation 75) exactly, the designer would set
ζi =−E d−i

Dγi (di, d−i)

+, which offsets the expected penalty at the truthful report. However,
this requires knowledge of the true demand d i, which is private information. If the designer
knew d i, the contrastive penalty structure would be unnecessary — one could simply score
each player’s report against a belief constructed from the true demands. The entire motivation
for the contrastive nature of the penalty mechanism is precisely that d i is not observed (see
Section 4.1).
We resolve this issue with a simple approximation. The designer does not observe individ-
ual true demands, but does observe the total realized demandD= ∑i∈I di ex post. In a large
market with comparable consumers, the average demandD/|I|is a reasonable proxy for each
38

player’s true demand. Then, the designer sets the offset as
ζi =−E d−i∼P−i

Dγi (D/|I|, d −i)

+, (76)
which is computable only from observable quantities. Under this choice, the expected penalty
at the truthful report di is no longer exactly zero, but approximately zero:
Ed−i∼P−i Πγi

di, d −i

=E d−i

Dγi (di, d−i)

+ −E d−i

Dγi (D/|I|, d −i)

+. (77)
Proposition 5(Approximate tax-free guarantee).Set the offset as in (Equation 76) where D=
∑i∈I di is the total realized demand. Then, for any consumer i reporting truthfully,
Ed−i∼P−i Πγi

di, d −i

≤κ ϕ ·µ·E d−i∼P−i
P(di, d−i)−P(D/|I|, d −i)  1, (78)
whereκ ϕ ≡
supt∈[0,1] |ϕ′′ 0 (t)|
inft∈[0,1] |ϕ′′ 0 (t)| .depends only on the designer’s choice of base potential.
Proof.Under the offsetζ i =−E d−i [Dγi (D/|I|, d −i)]+, the expected penalty at the truthful re-
port di is
Ed−i Πγi (di, d−i) =E d−i

Dγi (di, d−i)

+ −E d−i

Dγi (D/|I|, d −i)

+
≤E d−i

Dγi (di, d−i)−D γi (D/|I|, d −i)

. (79)
Recall that the first term ofD γi (d′ i, d−i)does not depend on the first argument. Therefore,

Dγi (di, d−i)−D γi (D/|I|, d −i)

=

Sϕ(γi)(P(di, d−i),Q)−S ϕ(γi)(P(D/|I|, d −i),Q)

. (80)
For the separable potentialϕ γi (P), the Savage representation gives
Sϕ(γi)(P,Q) = ∑
l
γi,l

ϕ0(Pl) +ϕ′ 0(Pl)(Ql −P l)  . (81)
Fix d −i and declareP l =P l(di, d−i)and ˜Pl =P l(D/|I|, d −i). Then, for each componentl,
the functionp7→ϕ 0(p) +ϕ′ 0(p)(Q l −p)has derivativeϕ ′′ 0 (p)(Q l −p), which is bounded in
absolute value by sup t∈[0,1] |ϕ′′ 0 (t)| · |Ql −p| ≤M ϕ0 sinceQ l,p∈[0, 1]. By the mean value
theorem applied to each component,

Sϕ(γi)(P,Q)−S ϕ(γi)( ˜P,Q)

 ≤ ∑
l
γi,l Mϕ0 |Pl − ˜Pl| ≤ ∥γi∥∞ Mϕ0 ∥P− ˜P∥1, (82)
Substituting (Equation 80) and (Equation 82) into (Equation 79),
Ed−i Πγi (di, d−i)≤ ∥γi∥∞ Mϕ0 ·E d−i
P(di, d−i)−P(D/|I|, d −i)  1. (83)
For uniform weightsγ i,l =γ i for alll, we have∥γ i∥∞ =γ i and the strong convexity parameter
readsµ=γ i ·inf t∈[0,1] |ϕ′′ 0 (t)|. Substitutingγ i =µ/ inf t |ϕ′′ 0 (t)|into (Equation 83),
Ed−i∼P−i Πγi

di, d −i

≤
supt∈[0,1] |ϕ′′ 0 (t)|
inft∈[0,1] |ϕ′′ 0 (t)| ·µ·E
P(di, d−i)−P(D/|I|, d −i)  1
=κ ϕ ·µ·E
P(di, d−i)−P(D/|I|, d −i)  1. (84)
39

The penalty trade-off for honest participants.From Theorem 3, the prosumer’s gain from
misreporting is at mostε(|I|) +∥w i∥2 q/(2µ), which decreases asµgrows. From Proposition 5,
the penalty at truthful reporting is at mostκ ϕ ·µ·E∥P− ˜P∥1, which increases asµgrows. The
two bounds move in opposite directions: a largeµeliminates the prosumer’s incentives, but
when the same prosumer happens to report truthfully, the largeµamplifies the penalty they
pay for honest participation. We now study this tradeoff and characterize the value ofµthat
best balances the two.
Consider a fixed prosumeriwith profit vectorw i and a fixed penalty parameterµ. The sameµ
governs the mechanism regardless of whether the prosumer underreports or reports truthfully.
The tradeoff.Define the following shorthands:
R(µ)≡
∥wi∥2 q
2µ ,T(µ)≡κ ϕ ·µ·E
P− ˜P  1, (85)
where ˜P=P(D/|I|, d −i). HereR(µ)is the residual gain from under-reporting (excluding
ε(|I|)) andT(µ)is the penalty at truthful reporting. The functionRis decreasing inµandT
is increasing inµ. The designer faces a tradeoff: increasingµtightens the bound on under-
reporting but loosens the bound on truthful reporting. The value ofµthat balances the two
objectives is obtained by settingR(µ) =T(µ). Solving forµ ⋆ yields
µ⋆ = ∥wi∥qq
2κ ϕ ·E
P− ˜P  1 . (86)
At this value, the residual gain from misreporting and the penalty at truthful reporting are
both equal to
R(µ⋆) =T(µ ⋆) =∥w i∥q
s
κϕ ·E
P− ˜P  1
2 . (87)
In summary, no fixedµcan achieve both objectives perfectly: deterring under-reporting re-
quires largeµ, protecting truthful reporting requires smallµ. The optimalµ ⋆ balances the two,
and the resulting common bound vanishes in large markets.
Large market regime.The common value (Equation 87) is the product of two factors: the
prosumer’s profit norm∥w i∥q and
q
κϕ ·E∥P− ˜P∥1/2. The first is a fixed property of the
prosumer. The second vanishes in the large market regime where players are comparable in
size, becauseD/|I| →d i impliesE∥P− ˜P∥1 →0. Therefore, at the optimalµ ⋆, both the gain
from under-reporting and the penalty at truthful reporting vanish as the day-ahead market
grows.
4.3.3 Budget Balance.
Baseline day-ahead and real-time energy settlement are jointly budget balanced by construc-
tion under uniform pricing and physical balance constraints (see (Equation 20)). The introduc-
tion of the settlement adjustmentΠ i generally generates additional revenue that needs to be
balanced.
40

Potentialϕ(P;γ) Score name ScoreS(P,i) Ej∼Q [S(P,j)] Normp Strong convexityµ(γ)
∑i γiP2 i
Quadratic
(Brier) 2γiPi − ∑k γkP2 k 2 ∑i γiQiPi − ∑i γiP2 i 2 2γmin
∑i γiPi lnP i
Logarithmic
(Log score) γi(lnP i +1)− ∑k γkPk ∑i γiQi (lnP i +1 ) − ∑i γiPi 1 γmin
∑i γi
Pα i
α ,α>1
Power / Tsallis
(α-score) γiPα−1 i − α−1 α ∑k γkPα k ∑i γiQiPα−1 i − α−1 α ∑i γiPα i α µα =



(α−1)γ min α≤2
(α−1)γ min δα−2 α>2
∑i γiePi
Exponential
score γiePi + ∑k γkePk (1−P k) ∑i γiQiePi + ∑i γiePi (1−P i) 1 γmin
Table 1: Strictly proper scoring rules with generating potentials and strong convexity param-
etersµ(γ)with respect to∥ · ∥p. For the power potential withα>2, the simplex is truncated
toP i ≥δ>0 to ensure strong convexity, sinceP α−2 i →0 asP i →0. The logarithmic and
exponential potentials achieveµ 1 =γ min. For the log score this is becauseγ i/Pi ≥γ i with
the infimum achieved atP i =1; for the exponential score becausee Pi ≥1 with the infimum
achieved atP i =0.
The TSOs are allowed to develop an additional settlement mechanism separate from im-
balance settlement to recover procurement costs of balancing capacity, administraitive costs,
and other balancing-related costs (subject to RNA approval) [European Commission, 2017c].
On top of that, any net financial outcome must be passed on to network users (so extra revenue
must ultimately be returned / offset somewhere) [European Commission, 2017c].
Thus, to preserve feasibility of the overall institution, we impose budget balance through a
neutrality account. Specifically, we introduce an account 0 with transfer
t0 ≡ ∑
i∈I
Πi
and require the accounting identity
∑
i∈I
tDA,new i (d) +∑
j∈J
tRT k (D, d) +t0(d) =0 (88)
to hold for every realization-type profile(D, d).
5 Numerical Results
5.1 Simulation Setup and Synthetic Results
We isolate the three qualitative phenomena presented in Sections Section 3-Section 4 in a con-
structed synthetic market that focuses only on the incentive question.
5.1.1 Simulation Setup
The day-ahead and real-time merit-order supply curves are fixed. Every player holds a uni-
form belief over private demand of common widthl. We focus on playeri∈Iwith true
demand di, fixed across market sizes. This allows the comparisons to be made at a common
baseline.
In every experiment we evaluate, on a grid of candidate reports d ′ i ∈[0, d i], the expected
gain from under-reporting,E d−i∼P−i [Gi(di, M(d ′ i, d−i))] , with the expectation taken by Monte
Carlo. The four experiments differ only in which mechanism M is in force and which structural
41

parameters are varied. Each subsequent experiment adds one ingredient on top of the previous
one, so that the figures read progressively.
Units.Throughout, energy quantities (d i, d′ i,D, gj) are in MWh delivered over the one-hour
delivery period, and prices (p DA,p RT,v i,c j, cj) are in $/MWh. Each term of the per-period
utility is therefore a product $/MWh×MWh=$, which we read as a per-hour dollar amount,
i.e. $/h. Thus the gain and expected gain inherits the same units. That said, all payoff and gain
axes in the figures below are reported in $/h.
5.1.2 Synthetic Results
Theorem 1 — vanishing consumer gain.We consider a family of energy markets indexed by
the number of consumers|I|. All players are consumers withα j =0 for allj∈ J. The demand
of playeri∈I, d i is held fixed and the day-ahead nominal generation capacities are rescaled
across market sizes so that the truthful clearing always lands on a common merit-order supply
point. Recall (Equation 29) under Assumption 6. The intuition is as follows: For an under-
report to be profitable, it must shift the day-ahead clearing price which requires ∑j̸=i dj to fall
within a strip of width di −d ′ i around a supply-curve step. Theorem 1 bounds the probability
of that event byO(1/
p
|I|), so the expected gain inherits the same rate.
0.85 0.88 0.91 0.94 0.97 1.00
normalized report
20
10
0
10
20
30
40
50
Consumer gain under  ME  ($/h)
Consumer i's gain curves across market sizes
market size |I|
|I| = 5
|I| = 10
|I| = 50
|I| = 100
|I| = 150
|I| = 200
0 25 50 75 100 125 150 175 200
market size  |I|
10
5
0
5
10
15
20
25
upper bound on consumer gain  ($/h)
Decay of the gain bound  ε(|I|) = O(1/
√
|I| )
numerical upper bound
theoretical upper bound
Figure 3:Vanishing consumer gain.Left: expected gain of the consumeriunder mechanism
ME as a function of the normalised report d ′ i/di, one curve per market size|I|. Each curve
passes through zero at truthful reporting and decreaases toward negative values as the under-
report grows. Right: maximum of the gain over d′ i as a function of|I|, together with a reference
of the theoretical bound. The numerical envelope starts at a small positive level, decays at the
predicted rate, and crosses below zero once|I|is large enough that the day-ahead-real-time
residual strictly dominates the day-ahead price gap term.
Figure 3 confirms the predicted decay. The left panel shows that the sign of the gain is
driven by the under-report cost: every curve rises toward zero from below as d ′ i tends to d i
(d′ i/di →1), and the family shifts upward as|I|grows. The right panel removes the report
dimension by taking for each|I|, the maximum of the gain over non-truthful reports and com-
paring it against the theoretical bound reference. For small markets the maximum is positive
but small: a narrow interior band of under-reports still yields profit because the probability of
shifting the clearing price is high enough to beat the residual. As|I|grows, that band shrinks
at rate 1/
p
|I|and eventually disappears for|I|=50; the curve crosses below the reference
and into the negative region. Intuitively, a single consumer’s ability to move the market price
decreases with scale, and once it has decreased enough, the residual forces every misreport
into strict loss.
42

Theorem 2 — persistence of the prosumer gain.We repeat the previous experiment, but now
playeriis endowed with an ownership vectorα i on the simplex of real-time producers and
with nominal capacities g. The remaining players stay consumers withα j =0. The gain under
ME conists of the previous consumer term and an real-time-share term (see (Equation 46)). The
explanation is that, by under-reporting, the prosumer pushes a positive imbalance into real
time. Once that imbalance crosses the next capacity threshold of the real-time merit order, her
own asset is activated and collects the cost gap between it and the preceding unit. This profit
depends only on the real-time supply curve. The convex combinationα i, and the nominal
generation capacities does not vanish with|I|. In every market size, one therefore expects
a band of interior under-reports in which the real-time-share channel dominates the under-
report cost and yields a strictly positive gain.
0.70 0.78 0.85 0.92 1.00
normalized report
0
50
100
150prosumer gain  ($/h)
Prosumer's gain curves across market sizes
market size |I|
|I| = 5
|I| = 10
|I| = 50
|I| = 100
|I| = 150
|I| = 200
0 50 100 150 200
market size  |I|
20
0
20
40
60
upper bound on gain  ($/h)
Prosumer gain persists; consumer gain vanishes
prosumer (total)
consumer part only (Thm 2)
Figure 4:Persistent prosumer gain.Left: expected gain under M E across the same market
family of market sizes|I|=5, 10, 50, 100, 150, 200 as Figure 3. At the full display scale the
faimily again looks dominated by the under-report cost, so the structural feature of interest,
a positive interior humb around the reports that activate the real-time-share, is shown in the
zoomed sub-plot. Right: maximum prosumer gain over reports d ′ i ∈[0, d i)as a function of|I|
mapped onto the consumer bound of Figure 3. The consumer bound decays to zero and below
while the prosumer bound stabilizes at a strictly positive level (around 50 $/h;see also the
level of the humb in the left panel) determined by the real-time supply structure, the nominal
generation capacities andα i.
Figure 4 reproduces Theorem 2 visually. The right panel contrasts the two maxima: the
consumer curve drops as before, while the prosumer curve stabilizes at a strictly positive level.
The left panel explains why: even for large|I|there is a band of under-reports, located close
to truthful (in a neighborhood of d ′ i/di =0.89), on which the prosumer’s real-time-share rev-
enue increases the under-report cost and produces a strictly positive gain. The height of that
hump depends on the real-time supply curve, generation capacities andα i, and hence, it does
not shrink with the market size. No single toleranceεcan serve consumers and prosumers
simultaneouly once|I|is large enough, and M E therefore fails to beε−BIC with vanishingε
over the whole player set.
Theorem 3 — scoring rule restoration.We reuse the market of the previous experiments and
augment the day-ahead settlement with the contrastive scoring-rule paymentΠ γi of Section 4.
The payment is parameterized by the strong convexity parameterµof the underlying potential
function. We sweepµover a set of values while holding all other primitives constant. The
prosumer’s gain under the extended mechanism M S equals her gain under M E minus the
scoring-rule payment (Equation 66).
43

Figure 5 shows how the penalty closes the prosumer gap. The interior hump of Figure 4
which was responsible for the persistent prosumer advantage under M E, is pushed into the
negative region onceµis large enough. The right panel gives the quantitative story: the fam-
ily of green curves traces the Theorem 3 boundε(|I|) +∥w i∥2 2/(2µ). The first term decays
with|I|at rate 1/
p
|I|established for consumer, and the second term is a free parameter that
the designer can shrink by increasingµ. For largeµ, the prosumer bound coincides with the
consumer bound, restoring a uniformε−BIC guarantee over the full player set.
0.86 0.90 0.93 0.97 1.00
normalized report
10
0
10
20
30
40
50
prosumer gain under MS   ($/h)
Penalized prosumer gain across market sizes (µ = 150)
market size |I|
|I| = 5
|I| = 10
|I| = 50
|I| = 100
|I| = 150
|I| = 200
0 50 100 150 200
market size  |I|
10
0
10
20
30
40
50
upper bound on gain  ($/h)
Penalty drives prosumer gain toward the consumer bound
prosumer bound
consumer bound
prosumer under M S,  µ = 25
prosumer under M S,  µ = 50
prosumer under M S,  µ = 100
prosumer under M S,  µ = 130
prosumer under M S,  µ = 150
Figure 5:Scoring-rule mechanism drives the prosumer gain toward the consumer bound
Left: prosumer gain under M S across market sizes|I|=5, 10, 50, 100, 150, 200 at a single rep-
resentative penalty strengthµ=150. Every curve still touches zero at truth but exhibits a
sharp downward step at the under-report where the scoring rule fires: after that threshold the
penalty adds a strictly negative contribution that suppress the real-time-share humb of Fig-
ure 4. Right: maximum gain under mechanism M S as a function of|I|for a family of penalty
strengthsµ=50, 100, 130, 150. As before, the dark red solid curve corresponds to the pro-
sumer’s bound and the light green dashed curve to the consumer curve of Figure 4. Between
the two sits a family of prosumer bounds under M S at varying strong-convexity parameterµ
(dark green = smallµ, light green = largeµ). Asµgrows the red family descents from the dark-
red reference toward the dashed green one, in agreement with the boundε(|I|) +∥w i∥2 2/(2µ).
Incentive deterence vs. cost of honest reporting.If under the value ofµsuch that prosumers’
gain drops to the consumer bound (Figure 5), the prosumer plays honestly under mechanism
MS, what does it cost them and how much they give up when under-reporting?
Figure 6 makes this comparison at every penalty strength a designer might consider, on
the same synthetic market that we used in Theorem 1-Theorem 3. The horizontal axis is the
penalty strengthµwhich varies from 0 up to 150 – that is the range that matters for this market.
LetU 0 be the prosumer’s average payoff (measured in $/h) on this market when they report
their true demand under mechanism ME.
It makes sense to useU 0 as a reference since it expresses what the prosumer would have
earned if the penalty had never been introduced. Hence, any cost or gain the penalty creates
is naturally read against it. On top of that,U 0 adapts to the size of the market: if we double
every price, every demand, and every producer capacity,U0 doubles too, and so do the penalty
and the under-reporting gain. The percentage ofU 0 stays the same, so the numbers we report
applies to a market that is either ten times larger or ten times smaller. Lastly,U0 is the quantity
the prosumer actually cares about. The penalty strengthµis also in dollars per hour, but it is a
setting the designer picks. ComparingµtoU 0 via the percentage axis is what makes the figure
say something concrete for the prosumer.
44

0 50 100 150
strong-convexity parameter  µ
0
10
20
30$/h
25.1 $/h  (0.49%)
Deterrence vs. cost of truthful play
cost of truthful play
deterrence
0.0
0.1
0.2
0.3
0.4
0.5
% of U 0
Figure 6: Two curves the designer should look at. One expressed as a percentage of the pro-
sumer’s baseline hourly earningsU 0 ≈5127.95 $/hand the other absolute dollars for the
particular hour slot.Blue: the most the prosumer is expected to earn by under-reporting on
this market, after the penalty activates; it shrinks to zero as the penalty parameterµis turned
up.Green: the most the mechanism is expected to charge the honest prosumer, in this market;
it grows in direct proportion toµ. Atµ≈150 the two plots summarise the calibration we use
for Theorem 1—Theorem 3:under-reporting gain of 0% and a worst-case honest cost of 0.5% of
U0 (respectively 25$/h).
5.2 Empirical Evaluation on Real-Market Data
This section demonstrates the performance of our mechanism by applying it to the strategic
component that we infer from real market data. In particular, we work with hourly time series
of low, medium and high voltage reported loads (interpreted as three players’ day-ahead re-
ports) found in [HENEX] together with the corresponding realized demand, extracted from an
ENTSO-E-based dataset [ENTSO-E, b] and preprocessed to retain only under-estimated hours
in which the aggregate report does not exceed actual total consumption.
On this set we rationalize the day-ahead market reports as subjective equilibria by means
of the prosumers valuations, demands, real-time share vectors and real-time nominal capacity
bounds that make the observed day-ahead reports approximately optimal with respect to a
finite set of breakpoint deviations.
We formulate this inverse problem as a convex feasibility program, relaxed with slacks
and recast it as a regularized convex optimization program (inner level), while the nominal
real-time capacities are treated as outer-level decision variables tuned by a derivative-free co-
variance matrix evolution strategy (CMA-ES) search rather than by a large mixed-integer for-
mulation.
We detail the key modeling and algorithmic parameters (valuation floor, slack penalties,
regularization weights, quantile supports, and solver choices), and finally present numeri-
cal results that compare observed and predicted best-response reports, day-ahead/real-time
prices, imbalances, and player utilities under the calibrated model, with and without the effect
of our mechanism.
5.2.1 Time Resolution, Units, and Sample Period
Day-ahead time unit (MTU) in our sample.In our empirical sample (prior to October 2025),
the coupled EU day-ahead market (SDAC) clears at anhourlyMTU, i.e. a delivery day is par-
titioned into 24 hourly MTUs. SDAC transitioned from hourly to 15-minute MTUs on trading
day 30 September 2025 for delivery day 1 October 2025; this occurs after our sample period.
[European Commission, 2025, SDAC Project Parties, 2025]
Imbalance settlement time unit (ISP).At the EU level, EBGL sets the harmonisation objective
for a 15-minute ISP . [European Commission, 2017e]
45

Model period and units.Because our dataset reports realized load only at the hourly level,
we conduct the theoretical and empirical analysis at thehourlyresolution. We study a single
delivery hour and suppress the hour index whenever no confusion arises. Letτ>0 denote the
duration of one model period in hours; in the baseline specification,τ=1. All quantity vari-
ables areenergyquantities in MWh delivered over that hour. For example, 100 MW sustained
over 15 minutes corresponds to 25 MWh, while 100 MW sustained over an hour corresponds
to 100 MWh.
5.2.2 Data and Pre-Processing
The dataset combines day-ahead reported quantities at three aggregation levels: low-voltage
LV , medium-voltage MV , high-voltage HV , and realized total load (actual total system demand)
D. In the implementation, these quantities are fetched from an annual ENTSO-E [ENTSO-
E, b] ”Total Load” time series and a preprocessed day-ahead market dataset containing the
voltage levels forecasts [HEnEx, 2025]. The data are stored in an array of shape(days, 4, 24)
containing LV , MV , HV , and actual total consumption for each hour of the day, from which
we extract a single hour across all days. For that fixed hour, each selected slottrefers to a
day of the year. We define three ”players” corresponding to the LV , MV , and HV aggregates,
and denote the collection d t i as the observed day-ahead report of playeriat dayt, fori∈
I,|I|=3. The realized total consumption is denotedD t. We restrict attention to under-
estimated days where the reported day-ahead quantities do not exceed the realized average
demand. Specifically, we retain only those tuples

dt 1, dt 2, dt 3,D t that satisfy ∑i dt i ≤D t and
discard all remaining days. This ensures that the implied day-ahead schedule is physically
feasible without upward curtailment and simplifies the real-time modeling: imbalances are
always nonnegative,ρ t ≥0 and therefore, the real-time market always operates in a ”short”
regime that activates positive real-time capacities. After this filtering step, we obtain a dataset
dataset=

dt 1, dt 2, dt 3,D t	 t∈T, whereTindexes the remaining days for the chosen time slot.
5.2.3 Inverse Best-Response Model
Fixing a particular time slot of the day-ahead, we are provided with a sequence of reported pro-
files and total consumptions{(d t 1, . . . , dt |I| ,D t)}T t=1 over different dayst. Such sequences are
publicly available by e.g., the Hellenic Energy Exchange [HENEX] and the ENTSO-E Trans-
parency Platform [ENTSO-E, b]. We assume that each player decides upon the same historical
horizonH>0 and maintains beliefsP t −i, andQ. For eacht>H, these histograms are con-
structed by aggregating previously observed samples over a rolling window of length equal
to the horizonH,(d τ i , . . . , dτ |I| ,D τ),τ=t−H, . . . ,t−1.
Given observed (from the data) profiles{(dt 1, . . . , dt |I| ),D t}T t=H+1 , we want to determine, for
each player and each day, those valuations, demands and incentive strength (convex combi-
nations) that rationalize the players’ reports as subjective equilibria ofG t. Letv t = [vt 1, . . .vt |I| ],
dt = [dt 1, . . . dt |I| ],A t = [αt 1; . . . ;αt |I| ], whereα t i = [αt i,1, . . . ,αt i,|J| ]is the row vector of shares for
playeri∈I. Lastly, gt = [gt 1, . . . ,gt |J| ]is the vector of nominal capacities of the real time market.
46

The problem we are interested in solving is: For eacht=H+1, . . . ,T
Find

dt,v t,A t, gt
subject to :d t i ∈arg max x∈[0,dt i ] Ut i  x, ;v t i,α t i, gt ,
∑
i
dt i =D t,
∑
j∈J
αt i,j =1,
vt i ≥0,
αt ≥0,
gt ≥0,
∀i∈I. (89)
In practice of course, the dominance of the observed report is approximated by enforcing it on
a finite grid of deviationsA i,t around the observation.
The feasibility problem (Equation 89) is infinite-dimensional: the best-response conditions
involve expectations with respect to empirical distributions and an arg max over a continuum
of actionsx∈[0, d t i ], and the real-time capacities gt themselves are additional unknowns. In
order to implement it numerically we proceed in two steps:
(i) for fixed real-time capacities gt we build a finite set of breakpoint deviationsA i,t and
formulate aninnerconvex program that enforces approximate best-response inequalities
and infers(d t,v t,A t);
(ii) treating the capacities gt asoutervariables, we tune them so that the model’s forward best
responses match the observed reports. This outer problem is tackled with a derivative-
free CMA-ES search rather than a large mixed-integer program.
5.2.3.1 Inner Level: Finite Deviations and Linear Inequalities.Fix a finite set of calibration
daysT fit ⊂ {H+1, . . . ,T}and assume that the real-time capacitiesgt fort∈T fit are given. For
each such daytand each playeri∈I, we construct a finite deviation setA i,t ⊂[0,D t]which
contains the endpoints 0 andD t, day-ahead and real-timebreakpoints(values ofxwhere the
day-ahead marginal unit or the real-time marginal genset changes, computed from the day-
ahead/real-time stacks and the empirical supports ofP t −i andQ t), and the observed report d t i
(used to form utility differences but not treated as a deviation).
For each(i,t)and each deviationx∈A i,t, we compare the expected utility of the observed
action dt i and the deviationx, withU t i (·)as in (Equation 45). The approximate best-response
condition is:
Ut i (dt i;v t i,α t i, gt)≥U t i (x;v t i,α t i, gt)−s i,t(x),∀x∈A i,t, (90)
for some slacks i,t(x)≥0 that allows for small violations and model error. By construction,
and for fixed capacities and empirical distributions,U t i (x)is affine in the unknowns(v t i,α t i )
and the real-time term is a weighted sumα t⊤ i (expected RT reward vector atx). Hence there
exist coefficients
Ai,t(x)∈R,B i,t(x)∈R |J|,b i,t(x)∈R,
computed from the data and gt, such that
Ut i (d′t i )−U t i (x) =A i,t(x)v t i +B i,t(x)⊤αt i −b i,t(x).
47

Substituting this into (Equation 90) yields the linear constraint
Ai,t(x)v t i +B i,t(x)⊤αt i ≥b i,t(x)−s i,t(x),∀x∈A i,t,∀i∈I,∀t∈T fit. (91)
We retain the feasibility constraints from (Equation 89) in a slightly strengthened form:
∑
i∈I
dt i =D t, d t i ≥d t i, d t i ≥0,∀t∈T fit, (92)
∑
j∈J
αt i,j =1,α t i,j ≥0,∀i∈I,∀t∈T fit, (93)
vt i ≥v min,∀i∈I,∀t∈T fit, (94)
wherev min is a valuation floor chosen strictly above the largest marginal cost in the day-ahead
stack.
5.2.3.2 Inner Regularized Convex Program.To select a particular solution and keep the
inferred parameters economically reasonable, we minimize the total slack together with small
quadratic regularization terms. Introducing positive weightsγ slack,γ α,γ v >0,γ d >0, we
solve the followinginnerinverse best-response problem:
min
vt i,dt i,αt i
si,t (x)≥0
∑
i∈I

γslack ∑
x∈A i,t
si,t(x) +γα∥αt i ∥2 2 +γ v(vt i )2 +γ d(dt i )2
s.t. BR inequalities (Equation 91) for alli,t,x,
demand constraints (Equation 92), share constraints (Equation 93),
and valuation floor (Equation 94).
(95)
All constraints in (Equation 95) are affine and the objective is a strictly convex quadratic func-
tion. Thus, for fixed capacities gt and empirical distributions(P t −i,Q t), problem (Equation 95)
is a convex quadratic program which we solve with off-the-shelf solvers (OSQP , with ECOS
and SCS as fallbacks), obtaining inferred primitives( bvt i, bdt i, bαt i )for each(i,t)∈I×T fit.
5.2.3.3 Outer Level: Calibration of Real-Time Capacities.In the inner problem, we treated
the real-time capacities gt as fixed parameters. The second step is to adjust these capacities so
that the model’s predicted best-response bids reproduce the observed ones. Given a candidate
collection of real-time capacities g=

gt t∈T fit, we keep the inner primitives( bvt i, bdt i,bαt i )fixed
and simulate the subjective gamesG t forward. For each daytand playeriwe compute a
soft(quantal) best response d t,BR i (gt)by evaluatingU t i (x)on a refined breakpoint grid and
applying a softmax over utilities:
dt,BR i (gt) =∑x∈A sim i,t πt i (x; gt)x,π t i (x; gt) = exp

Ut i (x;v t i,α t i, gt)/τ 
∑ ˜x∈A sim i,t exp

Ut i ( ˜x; bvt i,bαt i, gt)/τ ,
whereA sim i,t is a simulation breakpoint set (constructed in the same spirit asAi,t), andτ>0 is a
temperature parameter. Asτ→0 the soft best response approaches the hard argmax, whereas
largerτyields smoother responses and better numerical robustness.
We then measure the fit between the model and the data by the mean squared deviation
48

between observed and predicted bids:
L(g):= 1 |I| ∑t∈T fit ∑i∈I  dt,BR i (gt)−d t i 2 . (96)
Theouterproblem is then
min
g
L(g)
s.t.g t j ≤ gt j ≤ gt j,max,∀j∈ J,∀t∈T fit, (97)
whereg t j >0 and gt j,max are simple box bounds (in the implementation, they are built from a
heuristic “suggested” real-time capacity based on the empirical distribution of positive imbal-
ances).
The mapping g7→L( g)is evaluated via simulation and is nonconvex and nonsmooth. We
therefore solve (Equation 97) with a covariance-matrix adaptation evolution strategy (CMA-
ES), acting on the flattened vector of capacities. In the numerical experiments we use a two-
stage procedure: a first “cheap” stage with a very short belief horizon (used to warm-start the
capacities), followed by a second stage with a longer horizon and refined CMA-ES search.
5.2.4 Results and Discussion
In this section we answer, slot by slot and player by player, the following question: if we keep
the same fitted primitives and switch from the mechanism M E to mechanism M S, does the
best response move towards truthfulness? If yes, by how much, at what cost, and on which
slots? Under MS each player maximizes the same ME utility minus the contrastive penaltyΠ γi
defined in (Equation 66).
The first thing to look at is what the players actually report. Figure 7 shows that under ME
we see the observed report d t i and the fitted true demand bd t i sitting strictly above it on most
slots. That vertical gap is the empirical evidence of strategic under-reporting: the fitted player
knows their true demand is bd t i , but, given the real-time profit channel, it is cheaper for them to
drop the day-ahead report down to d t i .
20 25
Day slot t
2500
3000
3500
4000Player 1 quantity (MW)
Player 1: reported vs. true demand vs. best response
Reported
True demand
Best response
20 25
Day slot t
1000
1500Player 2 quantity (MW)
Player 2: reported vs. true demand vs. best response
Reported
True demand
Best response
20 25
Day slot t
1000
1250
1500
1750Player 3 quantity (MW)
Player 3: reported vs. true demand vs. best response
Reported
True demand
Best response
Figure 7: Observed report dt i (solid blue), fitted truthful capbd t i (dashed cyan) and best response
under ME (dashed green). The ME best response reproduces the observed report.
Moving forward, we set the strong-convexity modulus per player toµ= (10 5, 105, 106),
mapped toγ i via Table Table 1 under the log potential (logarithmic scoring rule). The spread
is asymmetric: a large penalty for LV and MV , and a strong one for HV . This way a single plot
shows, what “penalty in between”, and “penalty on” look like on the same real data.
Figure 8 shows that under M S, on exactly those gapped slots, the best response lifts off
the observed curve and travels towards the fitted cap. The mechanism makes the profitable
under-report expensive enough that the player prefers to increase their report. On slots where
49

the two ME curves were already close, MS changes nothing, which is the correct behavior of a
mechanism that is supposed to activate only when there is something to correct.
20 25
Day slot t
2500
3000
3500
4000Player 1 quantity (MW)
Player 1: reported vs. true demand vs. best response
Reported
True demand
Best response
20 25
Day slot t
1000
1500Player 2 quantity (MW)
Player 2: reported vs. true demand vs. best response
Reported
True demand
Best response
20 25
Day slot t
1000
1250
1500
1750Player 3 quantity (MW)
Player 3: reported vs. true demand vs. best response
Reported
True demand
Best response
Figure 8: The MS best response (dashed green) moves towards the true demand (dashed cyan)
on exactly the slots where the two ME curves were apart.
Quantity under M E under MS
Day-ahead clearing price ($/MWh) 80 80
Real-time clearing price ($/MWh) 200 20 (min 0, max 40)
Real-time imbalance (MWh) 614 (min 408, max 919) 24 (min 0, max 47)
Total cleared demand (MWh) 4977 5547
Day-ahead marginal producer bin 3 of|J|=4 bin 3 of|J|=4
Real-time marginal producer bin| ¯J|=4 (most expensive) bin 1 (cheapest), or inactive
Table 2: Day-ahead and real-time clearing prices, real-time imbalance, total cleared day-ahead
demand, and the marginal producer on each side under the two mechanisms. Reported quan-
tities are means over the simulated slots, with the per-slot minimum and maximum given in
parentheses where dispersion is non-trivial. Both cleared day-ahead totals fall inside the same
day-ahead capacity bin (bin 3 of|J|=4), so the day-ahead clearing price is unaffected. Under
MS the residual the TSO must cover in real time shrinks by roughly an order of magnitude,
the marginal real-time producer drops from the most expensive bin to the cheapest (or none at
all), and the real-time clearing price collapses correspondingly.
The summary in Table 2 tells the same story. Under both mechanisms the day-ahead market
clears inside the same generation capacity bin, and hence the day-ahead clearing price does not
change: the larger reports under M S consume more but remain inside the same bin without
crossing the upper step of the bin. The real-time market behaves differently. Under M E the
residual that the TSO must cover in real time is large enough to activate the most expensive
producer on the real-time supply stack, while under M S that residual is much smaller and
either the cheapest real-time marginal cost is activated or no real-time producer is dispatched
at all and the real-time clearing price collapses correspondingly. Both effects are consistent
with what the theory predicts.
Figure 9 completes the picture by showing the real-time imbalance, i.e. how much demand
had to be absorbed in the real-time market. Under M E this quantity is positive: that is the
residual real-time profit channel Theorem 2 tells us the mechanism is meant to close. Under
MS the same slots show a substantially smaller residual. Price and imbalance curves show that
the mechanism does what it is supposed to do overall.
Lastly, the purpose of Figure 10 is to illustrate when mechanism M S activates and how
much cost it incurs. In order to ease the comparison the top row of Figure 10 reproduces the
content of Figure 7. The two rows at the bottom of Figure 10 check the property that matters
most for a well-posed mechanism: when a player is honest, the mechanism does not charge
them. For each player we plot the per-slot penalty, and we look at what happens on the slots
50

20 21 22 23 24 25
Day slot t
0
250
500
750Imbalance (MW)
Imbalance: ME vs MS
imbalance under ME
imbalance under MS
Figure 9: Imbalance (day-ahead-cleared demand subtracted from the realized total consump-
tion) under ME (dark green) and under MS (light green).
where the observed report already agrees with the fitted truthful demand (so the player is, in
effect, honest) versus the slots where the fit detected a meaningful under-report (so the player
is not honest). On the honest slots the penalty is flat and near zero across all three players.
On the dishonest slots the penalty activates based on how strong the player’sµis: player 1
(LV ,µ=10 5), player 2 (HV ,µ=10 6), and player 3 (MV ,µ=10 5). The last row shows for
each player, how the realized payoff diminishes under the equilibrium profiles played w.r.t.
mechanism MS for each time slot. In short, the plots show that dishonest play is what turns
the penalty on, and honest play keeps it off and how the payoffs reduce under our mechanism
design.
6 Conclusion
We studied a strategic estimation problem in which an institution—the day-ahead market—
aggregates reports from self-interested players in order to recover a latent population-level
object: the true distribution of next-day demand. Classical statistical estimation treats data
as drawn from nature; in our setting the data are reports chosen by players who respond to
the very rules that will process them, and the estimator is therefore endogenous to its own
data-generating process.
Empirically, this circularity has a visible signature. Using publicly available data from three
European wholesale markets, we documented a persistent, one-sided gap between aggregate
day-ahead reports and realized consumption. The gap survives long observation windows
and changes in conditions, ruling out prediction noise as the explanation. We argued that it
is best understood as the equilibrium response of strategic prosumers to the prevailing settle-
ment rules.
Our theoretical results explain the asymmetry of this response. For players participating
on the demand side only—consumersin our model—the gain from misreporting shrinks at rate
1/
p
|I|in the size|I|of the day-ahead market, so honesty is an approximate best response in
large day-ahead markets. For consumers who also hold real-time generation—prosumers—the
gain is bounded below by a strictly positive constant that depends only on the prosumer’s
portfolio and the real-time supply stack, and does not vanish as the day-ahead market grows.
The two-stage institution therefore cannot be made approximately truthful for everyone si-
multaneously.
To close this gap we introduced an imbalance-settlement mechanism built on a strictly
proper, leave-one-out contrastive scoring rule. The auctioneer constructs two population-level
subjective beliefs about the real-time outcome—one using the player’s report and one omitting
it—and charges each player according to her marginal contribution to the fidelity of the mar-
ket’s belief. The mechanism has a single tuning parameterµ, the strong-convexity parameter of
51

20 25
Day slot t
2500
3000
3500
4000Player 1 quantity (MW)
Player 1: reported vs. true demand vs. best response
Reported
True demand
Best response
20 25
Day slot t
1000
1500Player 2 quantity (MW)
Player 2: reported vs. true demand vs. best response
Reported
True demand
Best response
20 25
Day slot t
1000
1250
1500
1750Player 3 quantity (MW)
Player 3: reported vs. true demand vs. best response
Reported
True demand
Best response
Reproduced from Fig. Figure 7, aligned column-wise with the panels below.
20 25
Day slot t
0
105
Penalty ($/h)
Player 1: when the penalty fires & penalty level
penalty fires
Π1
20 25
Day slot t
0
1
2Payoff ($/h)
1e6
Player 1: utilities under ME vs MS
utility under ME
utility under MS
Player 1 (LV ,µ=10 5)
20 25
Day slot t
0
105
106
107
Penalty ($/h)
Player 2: when the penalty fires & penalty level
penalty fires
Π2
20 25
Day slot t
0
200000
400000
600000Payoff ($/h)
Player 2: utilities under ME vs MS
utility under ME
utility under MS Player 2 (MV ,µ=10 5)
20 25
Day slot t
0
105
Penalty ($/h)
Player 3: when the penalty fires & penalty level
penalty fires
Π3
20 25
Day slot t
0
200000
400000Payoff ($/h)
Player 3: utilities under ME vs MS
utility under ME
utility under MS Player 3 (HV ,µ=10 6)
Figure 10: Mechanism at work, per player. The top row reproduces Figure 7 so the reader can
line up the deterred slots with the penalty and utility rows below. Middle row: penalty under
MS; the light green band is where the penalty activates. Bottom row: realized utility (payoff)
under M E (no penalty) vs. under M S (paid penalty already subtracted); the vertical gap on
deterred slots is the money paid to the mechanism.
the strongly convex function associated with the scoring rule, which the designer can set large
enough to dominate the prosumer’s persistent strategic gain. Increasingµalso charges honest
players whose private demand happens to lie far from the population, and we characterized
the valueµ ⋆ that balances these two effects: in a large market the residual incentive to misre-
port and the residual cost paid by honest participants vanish at the same rate. The mechanism
is informationally light: the auctioneer needs nothing beyond what is already observable in
the day-ahead stage, and the existing allocation and pricing rules are left untouched—only the
settlement transfer is modified.
We then tested the mechanism on real day-ahead and real-time data from a European
wholesale market. Once the penalty is in place, reports rise toward true demand, more en-
ergy clears in the day-ahead stage, and the real-time imbalance shrinks by roughly an order of
magnitude. In our model, the day-ahead clearing price is unaffected because the larger reports
remain within the same step of the supply curve; the real-time clearing price however drops
sharply because the smaller imbalance no longer requires the most expensive producers to be
activated. The empirical picture matches the theory.
52

References
Regulation (EU) 2019/943 of the European Parliament and of the Council of 5 June 2019 on the
internal market for electricity (recast). Official Journal of the European Union, L158, 14 June
2019, pp.54-124, June 2019. Applied from 1 January 2020.
Robert Aumann. Perspectives on bounded rationality. InProceedings of the 4th conference on
Theoretical aspects of reasoning about knowledge, pages 108–117, 1992.
W Glenn Brier. Verification of forecasts expressed in terms of probability.Monthly weather
review, 78(1):1–3, 1950.
Yang Cai, Constantinos Daskalakis, and Christos Papadimitriou. Optimum statistical estima-
tion with strategic data sources. InConference on Learning Theory, pages 280–296. PMLR,
2015.
Gong Chen and Marc Teboulle. Convergence analysis of a proximal-like minimization algo-
rithm using bregman functions.SIAM Journal on Optimization, 3(3):538–543, 1993.
Bruno de Finetti. La pr ´evision: ses lois logiques, ses sources subjectives.Annales de l’Institut
Henri Poincar´ e, 7(1):1–68, 1937. Translated as ’Foresight: Its Logical Laws, Its Subjective
Sources’ in Kyburg and Smokler (1964).
Ofer Dekel, Felix Fischer, and Ariel D. Procaccia. Incentive compatible regression learning.
Journal of Computer and System Sciences, 76(8):759–777, 2010. doi: 10.1016/j.jcss.2010.03.003.
Benjamin Edelman, Michael Ostrovsky, and Michael Schwarz. Internet advertising and the
generalized second-price auction: Selling billions of dollars worth of keywords.Ameri-
can Economic Review, 97(1):242–259, March 2007. doi: 10.1257/aer.97.1.242. URLhttps:
//www.aeaweb.org/articles?id=10.1257/aer.97.1.242.
ENTSO-E. ENTSO-E Mission Statement, a. URLhttps://www.entsoe.eu/about/inside-
entsoe/mission-statement/. About page (mission statement).
ENTSO-E. Total load – greece (25 may 2025), b.https://transparency.entsoe.eu/
load-domain/r2/totalLoadR2/show?name=&defaultValue=false&viewType=
GRAPH&areaType=CTA&atch=false&dateTime.dateTime=25.05.2025+00:00%7CCET%
7CDAY&biddingZone.values=CTY%7C10YGR-HTSO-----Y!CTA%7C10YGR-HTSO-----
Y&dateTime.timezone=CET CEST&dateTime.timezone input=CET+(UTC+1)+/+CEST+
(UTC+2).
ENTSO-E. Entso-e website.https://www.entsoe.eu, 2026.
EU. Directive (eu) 2019/944 of the european parliament and of the council of 5 june
2019 on common rules for the internal market for electricity and amending directive
2012/27/eu (recast). Official Journal of the European Union, 2019. Available athttps:
//eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32019L0944.
Euphemia. Pan-european hybrid electricity market integration algorithm, 2025. URLhttps:
//www.nemo-committee.eu/. Accessed: 2025-01-07.
European Commission. Third energy package. Legislative package, Directives 2009/72/EC
and 2009/73/EC; Regulations (EC) No 713/2009, 714/2009, and 715/2009, 2009. Official
Journal of the European Union, L 211, 14 August 2009.
53

European Commission. Commission regulation (eu) 2015/1222 of 24 july 2015 establish-
ing a guideline on capacity allocation and congestion management, 2015. URLhttps:
//eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32015R1222. OJ L 197,
25.7.2015, pp. 24–72.
European Commission. Commission regulation (eu) 2017/2195 of 23 november 2017 estab-
lishing a guideline on electricity balancing. Official Journal of the European Union, Novem-
ber 2017a. URLhttps://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:
32017R2195.
European Commission. Commission Regulation (EU) 2017/2195 of 23 November 2017 estab-
lishing a guideline on electricity balancing. Official Journal of the European Union, L 312,
pp. 6–53, November 2017b. URLhttps://eur-lex.europa.eu/legal-content/EN/TXT/
HTML/?uri=CELEX%3A32017R2195. Text with EEA relevance.
European Commission. Commission Regulation (EU) 2017/2195 of 23 November 2017 estab-
lishing a guideline on electricity balancing (Text with EEA relevance). Official Journal of the
European Union, L 312, 28 November 2017, pp. 6–53, November 2017c. URLhttps://eur-
lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A32017R2195. Text with EEA
relevance; Regulation (EU) 2017/2195 on electricity balancing guideline.
European Commission. Commission Regulation (EU) 2017/2195 of 23 November 2017 es-
tablishing a guideline on electricity balancing. Commission Regulation / Technical Re-
port 2017/2195, Official Journal of the European Union, 2017d. URLhttps://eur-
lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX%3A32017R2195. Accessed: 2025-
09-09.
European Commission. Commission regulation (eu) 2017/2195 of 23 november 2017 establish-
ing a guideline on electricity balancing (ebgl). Official Journal of the European Union, L 312,
28.11.2017, 2017e. URLhttps://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=
CELEX:32017R2195.
European Commission. Clean energy for all Europeans package. Legislative package, Di-
rectives (EU) 2018/844, 2018/2001, 2018/2002, 2019/944; Regulations (EU) 2018/1999,
2019/941, 2019/942, 2019/943, 2019. Official Journal of the European Union.
European Commission. Eu electricity trading in the day-ahead markets becomes more dy-
namic, 2025. URLhttps://energy.ec.europa.eu/news/eu-electricity-trading-day-
ahead-markets-becomes-more-dynamic-2025-10-01 en. News item, 1 Oct 2025.
European Parliament and Council of the European Union. Directive (eu) 2019/944 of 5
june 2019 on common rules for the internal market for electricity and amending di-
rective 2012/27/eu, 2019a. URLhttps://eur-lex.europa.eu/legal-content/EN/TXT/
PDF/?uri=CELEX:32019L0944. OJ L 158, 14.6.2019, pp. 125–199.
European Parliament and Council of the European Union. Regulation (eu) 2019/943 of 5 june
2019 on the internal market for electricity, 2019b. URLhttps://eur-lex.europa.eu/legal-
content/EN/TXT/PDF/?uri=CELEX:32019R0943. OJ L 158, 14.6.2019, pp. 54–124.
Federal Energy Regulatory Commission. Reliability Explainer, 2023. URLhttps://
www.ferc.gov/reliability-explainer. Webpage last updated August 16, 2023.
Federal Energy Regulatory Commission. An Introductory Guide for Participation in
ISO New England Processes, 2025a. URLhttps://www.ferc.gov/introductory-guide-
participation-iso-new-england-processes. Webpage published April 11, 2025.
54

Federal Energy Regulatory Commission. An Introductory Guide to Electricity Mar-
kets Regulated by the Federal Energy Regulatory Commission, 2025b. URL
https://www.ferc.gov/introductory-guide-electricity-markets-regulated-
federal-energy-regulatory-commission. Webpage last updated April 3, 2025.
Andrea Gasparella, Derck Koolen, and Andreas Zucker. The merit order and price-setting
dynamics in European electricity markets. Technical Report JRC134300, European Commis-
sion, Joint Research Centre, Petten, 2023.
Amirata Ghorbani and James Zou. Data shapley: Equitable valuation of data for machine
learning. InInternational conference on machine learning, pages 2242–2251. PMLR, 2019.
Tilmann Gneiting and Adrian E. Raftery. Strictly proper scoring rules, prediction, and
estimation.Journal of the American Statistical Association, 102(477):359–378, 2007a. doi:
10.1198/016214506000001437.
Tilmann Gneiting and Adrian E. Raftery. Strictly proper scoring rules, prediction, and estima-
tion.Journal of the American Statistical Association, 102(477):359–378, 2007b.
I. J. Good. Rational decisions.Journal of the Royal Statistical Society. Series B (Methodological), 14
(1):107–114, 1952. URLhttps://www.jstor.org/stable/2984087.
Irving John Good, AJ Mayne, JM Smith, and Thornton Page. The scientist speculates: an
anthology of partly-baked ideas.American Journal of Physics, 32(4):322–322, 1964.
Robin Hanson. Combinatorial information market design.Information Systems Frontiers, 5(1):
107–119, 2003.
Robin Hanson. Logarithmic market scoring rules for modular combinatorial information ag-
gregation.Journal of Prediction Markets, 1(1):3–15, 2007. doi: 10.5750/jpm.v1i1.417.
Moritz Hardt, Nimrod Megiddo, Christos Papadimitriou, and Mary Wootters. Strategic clas-
sification. InProceedings of the 2016 ACM Conference on Innovations in Theoretical Computer
Science (ITCS), pages 111–122. ACM, 2016. doi: 10.1145/2840728.2840730.
HENEX. Hellenic energy exchange (henex): Day-ahead market report.https://
www.enexgroup.gr/web/guest/markets-publications-el-day-ahead-market.
HEnEx. Hellenic energy exchange, 2025. URLhttps://www.enexgroup.gr/. Accessed: 2025-
01-07.
ISO New England Inc. Regulation (Settlement item description), n.d. URL
https://www.iso-ne.com/markets-operations/settlements/understand-bill/item-
descriptions/regulation. Webpage describing regulation as an ancillary service provided
based on regulation supply offers.
Ehud Kalai and Ehud Lehrer. Subjective games and equilibria.Games and economic behavior, 8
(1):123–163, 1995.
Daniel Kirschen and Goran Strbac.Fundamentals of Power System Economics. Wiley, 2nd edi-
tion, 2018. See Chapter 3 (generating electricity, marginal cost of generation, merit order
dispatch).
Hau L. Lee, V . Padmanabhan, and Seungjin Whang. Information distortion in a supply chain:
The bullwhip effect.Management Science, 43(4):546–558, 1997. ISSN 00251909, 15265501. URL
http://www.jstor.org/stable/2634565.
55

Paul L´evy.Th´ eorie de l’addition des variables al´ eatoires. Gauthier-Villars, Paris, 1937.
John McCarthy. Measures of the value of information.Proceedings of the National Academy of
Sciences, 42(9):654–655, 1956.
Reshef Meir, Ariel D. Procaccia, and Jeffrey S. Rosenschein. Algorithms for strategyproof clas-
sification.Artificial Intelligence, 186:123–156, 2012. doi: 10.1016/j.artint.2012.03.008.
Monitoring Analytics. 2023 State of the Market Report for PJM, Section 3: Energy Mar-
ket. Technical report, March 2024. URLhttps://www.monitoringanalytics.com/reports/
PJM State of the Market/2023/2023-som-pjm-sec3.pdf. See pp. 130–132, Figs. 3-1 and 3-
2 (day-ahead supply curves); pp. 143–148 (LMP fuel cost component decomposition).
Roger B. Myerson. Optimal auction design.Mathematics of Operations Research, 6(1):58–73, 1981.
ISSN 0364765X, 15265471. URLhttp://www.jstor.org/stable/3689266.
Yurii Nesterov et al.Lectures on convex optimization, volume 137. Springer, 2018.
North American Electric Reliability Corporation (NERC). Glossary of terms used in nerc reli-
ability standards, October 2025a. URLhttps://www.nerc.com/globalassets/standards/
reliability-standards/glossary of terms.pdf. Updated October 1, 2025.
North American Electric Reliability Corporation (NERC).Glossary of Terms Used in NERC Re-
liability Standards. NERC, November 2025b. URLhttps://www.nerc.com/globalassets/
standards/reliability-standards/glossary of terms.pdf. Updated November 5, 2025.
Juan C. Perdomo, Tijana Zrnic, Celestine Mendler-D ¨unner, and Moritz Hardt. Performative
prediction. InProceedings of the 37th International Conference on Machine Learning (ICML),
volume 119 ofProceedings of Machine Learning Research, pages 7599–7609, 2020.
Valentin V . Petrov.Sums of Independent Random Variables, volume 82 ofErgebnisse der Mathematik
und ihrer Grenzgebiete. Springer-Verlag, Berlin, 1975. Translated from the Russian by A. A.
Brown.
PJM Interconnection. Manual 11 revisions (redline): Energy Market Business Rules and
Day-Ahead timeline (committee material), 2023. URLhttps://www.pjm.com/-/media/
DotCom/committees-groups/committees/mic/2023/20230412/20230412-item-02-3---
real-time-values-manual-11-revisions---redline.ashx. Committee document dated
April 12, 2023 (PDF).
PJM Interconnection.Manual 11: Energy & Ancillary Services Market Operations, revision 129 edi-
tion, February 2024a. URLhttps://www.pjm.com/library/manuals. See Section 5, pp. 63–
80 (day-ahead market scheduling and clearing procedure).
PJM Interconnection. PJM publishes annual planning report for 2023. PJM Inside Lines,
2024b. URLhttps://insidelines.pjm.com/pjm-publishes-annual-planning-report-
for-2023/. Documents over 1,400 generators and approximately 65,000 MW of natural gas
capacity interconnection rights in PJM.
PJM Interconnection. Ancillary Services Fact Sheet, January 2025. URLhttps:
//www.pjm.com/-/media/DotCom/about-pjm/newsroom/fact-sheets/ancillary-
services-fact-sheet.pdf. Fact sheet dated Jan. 29, 2025.
B. A. Rogozin. An estimate for concentration functions.Theory of Probability & Its Applications,
6(1):94–97, 1961. doi: 10.1137/1106007.
56

Michael Rothschild and Joseph Stiglitz. Equilibrium in competitive insurance markets: An
essay on the economics of imperfect information.The Quarterly Journal of Economics, 90(4):
629–649, 1976. ISSN 00335533, 15314650. URLhttp://www.jstor.org/stable/1885326.
Leonard J Savage. Elicitation of personal probabilities and expectations. In V . P . Godambe and
D. A. Sprott, editors,Foundations of statistical inference, pages 159–175. Holt, Rinehart and
Winston, 1971.
SDAC Project Parties. 15-minute mtu in sdac was implemented (press release), 2025.
URLhttps://eepublicdownloads.blob.core.windows.net/public-cdn-container/
clean-documents/Network%20codes%20documents/NC%20CACM/SDAC%202025/SDAC 15-
Minute MTU Was Implemented.pdf. Press release dated 01 Oct 2025; go-live on trading day
30 Sep 2025 for delivery day 1 Oct 2025.
Sylvain Sorin. Information and rationality: some comments.Annales d’Economie et de Statis-
tique, pages 315–325, 1992.
Steven Stoft. Power system economics.Journal of Energy Literature, 8:94–99, 2002.
U.S. Department of Energy. How it Works: The Role of a Balancing Author-
ity, 2022. URLhttps://www.energy.gov/sites/default/files/2023-08/Balancing%
20Authority%20Backgrounder 2022-Formatted 041723 508.pdf. Backgrounder (docu-
ment label: 2022; formatted 2023-04-17 per filename).
U.S. Energy Information Administration. Newer-technology natural gas-fired generators
are utilized more than older units in PJM. Today in Energy, April 2021. URLhttps:
//www.eia.gov/todayinenergy/detail.php?id=47556. Documents heat rates by tur-
bine class: B/D/E-class (>8,000 BTU/kWh), F-class (7,000–7,300 BTU/kWh), H/J-class
(6,700 BTU/kWh).
U.S. Energy Information Administration. Natural gas combined-cycle power plants increased
utilization with improved technology. Today in Energy, December 2023. URLhttps://
www.eia.gov/todayinenergy/detail.php?id=60984. Documents fleet-wide average heat
rate of 6,960 BTU/kWh for CCGT plants built 2010–2022.
William Vickrey. Counterspeculation, auctions, and competitive sealed tenders.The Journal of
finance, 16(1):8–37, 1961.
Behnam Zakeri, Iain Staffell, Paul E. Dodds, Michael Grubb, Paul Ekins, Jaakko J ¨a¨askel¨ainen,
Samuel Cross, Kristo Helin, and Giorgio Castagneto Gissey. The role of natural gas in
setting electricity prices in Europe.Energy Reports, 10:2778–2792, 2023. doi: 10.1016/
j.egyr.2023.09.069. See p. 2778 (Abstract: headline results); p. 2780, Section 3 (methodology
based on day-ahead market data); p. 2785, Fig. 5 (country-level marginal shares in 2021).
57
