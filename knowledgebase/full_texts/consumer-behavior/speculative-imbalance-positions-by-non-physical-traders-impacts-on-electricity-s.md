---
title: 'Speculative Imbalance Positions by Non-Physical Traders: Impacts on Electricity System Balancing
  in Great Britain'
url: https://arxiv.org/abs/2610.28075
category: consumer-behavior
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Joseph Cary
- Thomas Morstyn
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.28075
pages: 36
chars: 71010
fetched_at: '2026-11-08T13:18:09+00:00'
kb_version: 1
---

# Speculative Imbalance Positions by Non-Physical Traders: Impacts on Electricity System Balancing in Great Britain

Highlights
Speculative Imbalance Positions by Non-Physical Traders: Impacts
on Electricity System Balancing in Great Britain
Joseph Cary, Thomas Morstyn
•Non-physical traders’ speculative imbalance positions reduce GB sys-
tem imbalances
•Total absolute imbalance volume was 16–20% lower than without spec-
ulative positions
•Balancing costs were £347–396m lower and supplier imbalance charges
65–75% lower
arXiv:2610.28075v1  [eess.SY]  20 Oct 2026

Speculative Imbalance Positions by Non-Physical
Traders: Impacts on Electricity System Balancing in
Great Britain
Joseph Carya,∗, Thomas Morstyna
aDepartment of Engineering Science, University of Oxford, Parks Road, Oxford, OX1
3PJ, Oxfordshire, United Kingdom
Abstract
The electricity system in Great Britain (GB) allows participants to deliber-
ately produce or consume a different volume to their traded position and has
incentivised this practice with a single imbalance price since 2015. In partic-
ular, non-physical traders (NPTs) often take an open position to imbalance
without any intention to produce or consume power. However, new gov-
ernment proposals could restrict this practice due to concerns over supply–
demand balancing feasibility and costs. This article presents the first em-
pirical analysis of speculative imbalance positioning (SIP) by NPTs in the
GB electricity system through its effects on imbalance volumes, balancing
costs, the imbalance price, and associated settlement costs over the period
2021–2024. Our research uses party-level imbalance data in each settlement
period to run counterfactual simulations of the electricity balancing mecha-
nism without the aggregate NPT imbalance. Our results indicate that SIP
by NPTs reduced the total net balancing volume required by 3.1–3.9 TWh
(16–20%), reduced system imbalance standard deviation by 48–65 MWh
(13–17%), reduced balancing costs by £347–396m (5.9–6.7%), and reduced
supplier imbalance costs by £193–325m (65–75%) over the analysis period.
These results suggest that consumer bills would have been higher without
SIP by NPTs, since the extra costs would likely have been passed on to
consumers through levies, although the potential for effects in the wholesale
(primarily late-stage intraday) markets complicates this picture.
Keywords:Electricity market design, Electricity system balancing,
∗Corresponding author. Email address: joseph.cary@wolfson.ox.ac.uk

Speculative trading, Electricity imbalance pricing
1. Introduction
Electricity system balancing in GB takes place primarily through the
balancing mechanism (BM), in which NESO (the GB transmission system
operator) simultaneously instructs both congestion and other transmission
constraint management actions, as well as refining units’ schedules to main-
tain aggregate supply and demand balance. Over the period 2021–2024,
NESO spent £1.4 billion per year on average to manage supply and demand
imbalances through the BM alone1. The average absolute imbalance over the
same period in each half-hour window was 233 MWh, or around 4 TWh per
year — equivalent to 1.5% of total energy delivered through the transmission
network in 2024 (NESO, 2025b). NESO has a licence condition to minimise
consumer costs which highlights the need for efficient market mechanisms.
Trading parties in the GB electricity system are financially accountable
for differences between their contracted and physical positions. In GB, along
with other markets such as the Irish Single Electricity Market, the Nether-
lands, Denmark, and France, parties are allowed to take speculative positions
on the imbalance price. This research assesses whether speculative imbalance
positioning (SIP) by non-physical traders (NPTs) benefits the GB electricity
system.
OnekeyreasontopermitSIPistoincentivise‘helpful’imbalances(Ofgem,
2015), as explained in the following example. Suppose an NPT buys energy
ahead of time, consumes no energy, but the system has a net upward bal-
ancing energy requirement anyway. This energy purchase likely induced an
increase in generation, which reduces the net balancing energy requirement
compared with the counterfactual of no purchase. The trade is profitable if
the price at which the NPT’s imbalance is settled (i.e. at which they sell
their excess energy) exceeds the purchase cost. If the imbalance price is
tied to the marginal cost of energy balancing, profitable imbalance arbitrage
will also reduce the system imbalance (Bunn and Kermer, 2021). However,
whether this idealised scenario plays out in practice is an empirical matter.
For example, if the settlement price (SP) does not reflect the marginal cost of
buying balancing power, NPTs may be incentivised to take positions which
1Calculated from settlement stack data, based on flagged vs unflagged actions
2

exacerbate the system imbalance. Despite this trading strategy being com-
mon in GB (Elexon, 2019a), no study has quantified its effects on the GB
system.
This research is timely for three main reasons. First, the UK govern-
ment’s review of electricity market arrangements (REMA) led to a decision
to address the challenges through reformed national pricing (RNP). Among
the latest set of proposals are measures that deliberately curb opportunistic
imbalancing by small physical assets in real time (which we term passive bal-
ancing – see Section 2.2), which they associate with adverse effects on grid
stability and consumer costs (NESO, 2026). These same measures would in-
hibit SIP, but (as the document acknowledges) there is no existing research
on how these reforms would affect balancing volumes. Second, REMA states:
“Non-physical traders improve market liquidity and are an im-
portant component of a healthy market, therefore we want to
encourage their participation” (DESNZ, 2024)
yet provides no evidence in the technical assessments supporting this posi-
tion. Third, in 2020 ACER decided on single imbalance pricing as the stan-
dard methodology for the harmonisation of the imbalance settlement across
member system operators (SOs) (ACER, 2020). Since this could create an
incentivefor opportunisticimbalancing acrossnew markets, itis importantto
understand how single pricing has already played out in a market with signif-
icant structural similarities. This paper focuses on the GB system, due to the
abundance of publicly available GB data on balancing. However, the analy-
sis and methodology are also relevant to other energy systems, particularly
those with liquid intraday markets, transparent imbalance price mechanisms,
and a growing share of variable renewable energy sources in the generation
mix, such as in Europe and Japan.
This paper provides two main novel contributions. First, as far as the au-
thors are aware this research represents the first significant published analysis
on the role of NPTs in the GB system. Second, this research provides the first
empirical quantification of the impacts of SIP on GB electricity balancing,
ten years after the introduction of single imbalance pricing.
In this research, we focus on the effects of SIP (by NPTs only) on balanc-
ing and imbalance settlement volumes and costs. Reducing these is one of
the key aims of permitting SIP (see Section 2), and of significant public in-
terest given the recent rise in balancing costs. Combining extensive publicly
3

available data in new ways, we run counterfactual simulations of the GB bal-
ancing mechanism as the basis of our analysis. Over the period 2021–2024,
our modelling suggests that SIP reduced the total volume of energy balanc-
ing actions required by 3.1–3.9 TWh (16–20%), and reduced consumer bills
through lower balancing costs to NESO (between £347–396m, or 5.9–6.7%)
and a reduction in imbalance charges to suppliers (between £193–£325m, or
65–75%). While SIP also plays an important role in changing overall system
emissions and short-term market price formation, estimating these effects ei-
ther requires non-public information or ex-ante market modelling, which is
outside the scope of this paper.
The remainder of the paper is structured as follows. Section 2 covers
GB trading arrangements and provides a literature review. Section 3 covers
the data sources and methodology of the analysis. Section 4 reports the
results on system imbalance volumes and financial effects. Finally, Section 5
discusses the implications of the results for ongoing policy discussions.
2. Literature Review
This section provides an overview of GB electricity trading arrangements,
and related academic literature on opportunistic imbalancing.
2.1. GB Market Arrangements
Figure 1 provides an overview of domestic power trading arrangements in
GB, via sequential ex-ante markets from years ahead until just before deliv-
ery. One hour before delivery (known as gate closure) large generators and
demand units which participate in the BM submit their expected schedules
and costs to deviate from their schedule. From gate closure until the end
of a settlement period (the 30-minute blocks into which GB power days are
divided), NESO balances the grid primarily through the BM. Some actions
maintain exact supply/demand balance (known as energy balancing), while
others manage transmission constraints such as line capacity limits (known
as system balancing). In the 45-minute window between gate and intra-
day market closure, all trading parties can change their contracted positions
through trading on the continuous intraday market, and non-BM units (such
as smaller batteries and flexible plants) can change their output accordingly.
The difference between a party’s contracted and metered volume over
the course of a settlement period is their imbalance volume. If they have
oversupplied or under-consumed, their excess is sold back to the system at
4

Long Term
Hourly
Day
Ahead
Auctions
Half Hour
Day
Ahead
Auction
Intraday
Auctions Balancing Mechanism Imbalance Settlement
Intraday Continuous
00:00 D-1
Settlement
Period - 60 Mins
Settlement
Period - 15 Mins
Settlement
Period Start
Settlement
Period End
Figure 1: Timeline of trading arrangements in the GB electricity market. NESO manages
supply and demand imbalances and system network constraints primarily within the BM,
which starts 60 minutes before delivery. Parties may trade up to 15 minutes before delivery
on the continuous intraday market, overlapping with the BM.
SP, and vice versa. The net volumetric sum of the actions taken by NESO
in a settlement period is the NIV (net imbalance volume, see Equation 2).
SP is, generally, the price of the most expensive action taken by NESO in
the direction of NIV, after netting off balancing actions taken in the opposite
direction. For example, if NESO accepts 100 MWh of upward regulation and
20 MWh downward regulation in a settlement period, SP is set by the price
of the 80th MWh2. Changes to the total volume of balancing actions taken
could affect SP, and hence cashflows to imbalanced parties.
In November 2015, the GB imbalance settlement switched from dual to
single pricing. Among other reasons, Ofgem (the GB power market regula-
tor) wanted to reward parties for taking ‘helpful’ imbalances (Ofgem, 2015).
The following example clarifies this rationale. Consider a part-loaded gas
generator, who (correctly) identifies that the system will be short by 150
MWh of generation. Their marginal cost isC£/MWh. Under a single im-
balance price regime, SP is set by the marginal cost of upward regulation. If
C < SP, the generator has an incentive of(SP−C)£/MWh to generate
more than their contracted quantity, since they receive SP for any excess
power generated. If they do so, this reduces the system imbalance and saves
the SO (and hence the consumer) at least(SP−C)£/MWh compared to
2There are various complications to this procedure, which are clearly detailed in
(Elexon, 2025b).
5

activating more costly upward balancing power. However, under a dual im-
balance price regime, the price the generator receives for spilling into the
system is often set by thedownwardregulation marginal price. Since this
generally falls below the marginal cost of gas generation, the part-loaded gen-
erator has little to no incentive to spill, and chooses not to do so. Instead, the
SO has to activate (more costly) upward balancing power, increasing costs
to the consumer. Effectively, this reform partly outsources energy balancing
responsibility away from the BM, and encourages parties to anticipate and
counteract the overall system imbalance.
2.2. Academic Literature
Existing research falls into three main categories: imbalance price theory,
modelling agent behaviour under different systems, and empirical analysis of
the effects of changes to imbalance price regimes. This paper falls into the
final category, filling a gap in the literature on exploring the effects of SIP in
the GB system. In this review, it will be useful to distinguish between two
different types of opportunistic imbalance positions:
Passive Balancing:Asset-backed traders voluntarily change their output
from their contracted position to access a more favourable price at
imbalance than available in ex-ante markets. For example, a small
battery changes its output in response to the latest publications of
balancing actions taken by the SO.
Speculative Imbalance Positioning:NPTs speculating on price spreads
between short-term market prices and the SP. For example, in anticipa-
tion of the SP exceeding the current intraday price, an NPT might pur-
chase power at intraday, without any intention to consume the power
purchased.
Both strategies aim to profit from predicting SP. From a system perspec-
tive, these strategies can coincide in terms of their physical effects. For ex-
ample, an NPT may contract with a small asset post-gate closure, effectively
transferring the SP risk from the asset to the NPT, but with the same net
effect as the small asset spilling into the system. However, some SIP occurs
pre-gate closure, which can provide visibility to the SO if the counterparty
submits their generation schedule in advance.
Combining single imbalance pricing with allowing opportunistic imbal-
ancing has theoretical support. Suppose the forward markets settle to some
6

equilibrium price, but forecast errors mean the system is short. Here, the
SO is buying marginal power. In GB, where SP is generally reflective of the
marginal costs of buying power (Chen et al., 2024), a long position from the
forward markets displaces a higher priced balancing action, thus reducing
balancing costs and SP (albeit at a loss of producer surplus at the margin)
(Bunn and Kermer, 2021; Bunn et al., 2021). Other research proposes alter-
nativeimbalancepriceandsettlementschemes, suchasin(Ghiassi-Farrokhfal
et al., 2023; Lago et al., 2021). However, these alternatives are beyond the
scope of this research.
There exists significant simulated evidence that opportunistic imbalanc-
ing can be a profitable strategy in single price regimes. For example, a risk-
averse opportunistic imbalance strategy backtested on the Belgian market
would have been profitable (Bruneel et al., 2025), while a passive balancing
strategy in the same market yields similar outcomes for a BESS operator
(Karimi Madahi et al., 2024). Density forecasts are incorporated in a pas-
sive balancing strategy for a gas-fired unit in the Austrian market in (Bunn
et al., 2018), which offers improvements over techniques based on traditional
expected value forecasts. Even simple trading strategies based on predicting
only the sign of the imbalance, such as those in (Lisi and Edoli, 2018; Pozzetti
and Cartlidge, 2020), can generate profits through opportunistic imbalanc-
ing in the Italian and GB markets respectively. However, a risk-constrained
strategy in GB outperformed a similar simple benchmark (Browell, 2018).
While incentives for opportunistic imbalancing under dual pricing are
generallylowerthanundersinglepricing, onesimulationinDenmarksuggests
that even under dual pricing, an asset-backed player (a wind farm in this
case) is incentivised to take a passive balancing position (Chaves-Ávila et al.,
2014). However, different price-setting rules in the Netherlands (historically)
suggest that arbitrage profits were negative on average under dual pricing
(Boogert and Dupont, 2005).
Only a few papers move beyond the benefits for the individual to consider
the effects on overall system balancing in a European-style market (namely
with day-ahead, continuous intraday, balancing, and imbalance settlement
stages), which is one of the key contributions of our research. One study
on a generic European-style market finds that overall imbalance costs are
lowest under single price incentives (van der Veen et al., 2012). In the
Austrian market, NPTs are simulated to take system-supportive and prof-
itable imbalance positions, provided information relevant to forecasting is
published sufficiently promptly (Bunn and Kermer, 2021). A simulation
7

on the Japanese market shows that despite the dual pricing disincentive
against opportunistic imbalancing, profitable and system-supportive arbi-
trage opportunities remain (Matsumoto et al., 2022). However, a trading
algorithm which takes speculative intraday positions based on expected im-
balance prices, backtested on German data between 2017 and 2019, finds that
a profitable trading strategy would not have been system supportive due to
biased imbalance price incentives (Koch, 2022). A more efficient intraday
price constraint would make this strategy more system supportive by tying
the imbalance price to the true marginal cost of procuring balancing energy.
In practice, the following studies provide strong evidence that balancing
parties respond to imbalance price incentives, regardless of whether oppor-
tunistic imbalancing is permitted. Following a switch from a single to a hy-
brid single/dual imbalance pricing regime in Italy, imbalances from demand-
side balance responsible parties fell drastically (Clò and Fumagalli, 2019).
An analysis of the German grid suggests that taking a systematically short
position through passive balancing would have been highly profitable. How-
ever, in 2016–17 there was no systematic arbitrage opportunity left, as mar-
ket players systematically repositioned their traded volumes in response to
asymmetric penalties for being short when the system is short vs. long when
the system is long (Koch and Hirth, 2019). Later research finds a significant
association between the demand for imbalance energy (i.e. aggregate imbal-
ance) and the imbalance price in Germany. An increase in the imbalance
price is associated with adecreasein demand for imbalance energy (Eicke
et al., 2021), despite the prohibition of strategic imbalances in this market.
Another study investigates whether parties take opportunistic imbalance
positions, and what the effect on system balancing is. The analysis suggests
traded volumes react to the publication of the latest system balance. These
changes to traded positions are found to reduce system balancing volumes as
well as the 95th percentile of system imbalances (Koch and Maskos, 2020). A
different approach reaches a similar conclusion, finding significant evidence
of statistical arbitrage through the correlations between DA and imbalance
price spreads. There is no evidence that this practice threatened system
stability compared with other systems (Möller et al., 2011).
Other research casts doubt on the benefits of passive balancing. Over the
period 2009–2011 in Germany, imbalance prices were relatively predictable,
but not strongly correlated with spot (day-ahead and intraday) prices due to
the market design (Just and Weber, 2015). The mechanism allowed for dom-
inant strategies by generators which threatened system stability. In practice,
8

some players exploited this system which destabilised the grid by exacerbat-
ing imbalances, and cost consumers through raised spot prices and higher
reserve capacity requirements.
Finally, Elexon (the balancing and settlement administrator in GB) in-
vestigate increases in imbalance volumes by individual parties following the
switch to single imbalance pricing (Elexon, 2019a). While imbalances by
generators and suppliers remained broadly flat over the period 2014–2019,
imbalances by NPTs grew significantly. They find that most imbalances by
NPTsareinthesamedirectionasthemarketimbalance, i.e. whenthesystem
is long, NPTs are also long. However, the growth in NPT imbalances has not
led to an increase in balancing energy volumes, nor the most extreme NIVs.
We return to this counter-intuitive finding in Section 4.1, arguing that this
is the wrong metric to understand the effect of SIP on system imbalances.
Further investigation in (Elexon, 2019b) finds evidence that NPTs likely take
speculative imbalances in the GB market, but does not estimate the system
effect of this strategy.
Beyond the European/Japanese context, there exists an extensive litera-
ture on the role of speculators in arbitraging day-ahead and real-time price
spreads in US markets. Many researchers find that speculation has bene-
fited US power systems by curbing generator market power, promoting price
convergence, and reducing system operating costs and carbon emissions (see,
e.g., (Jha and Wolak, 2019, 2023; Mercadal, 2022; Saravia, 2003)). How-
ever, others find that speculation can increase system operational complexity
(Parsons et al., 2015), or increase spreads to gain higher revenues from power
derivatives (Birge et al., 2018). We do not discuss this literature in detail,
because US markets differ significantly from European-style markets (and
hence from our setting) for two key reasons. First, the clearing mechanism
in the US is based on central dispatch and nodal pricing, whereas most Eu-
ropean markets rely on self-dispatch (to some extent) and zonal or national
pricing. Second, US markets do not have a continuous intraday market,
meaning speculation occurs at day-ahead. The ability to speculate closer to
delivery with better information and the salient differences in market clearing
mean that our institutional setting is sufficiently distant from the US that
conclusions do not necessarily carry over.
In light of the mixed findings from other markets on the benefits of oppor-
tunistic imbalancing, this subject merits closer analysis. This research aims
to fill the gap in the literature in the GB context, and extend the analysis of
system balancing implications using counterfactual simulations incorporating
9

real data to generate estimated cost effects.
3. Data, Assumptions, and Methodology
The overall aim of this research is to estimate the effects of SIP on BM
volumes and costs by setting up a counterfactual scenario without SIP, and
to use this analysis to infer the effects on balancing costs and imbalance
settlement. This section discusses the data required, key assumptions in the
analysis, and finally highlights our novel methodology.
3.1. Data
Elexon categorises balancing parties under different but not mutually
exclusive labels. In this analysis, we define NPTs, generators, suppliers, and
mixed-role parties as in Table 1. These categories allow us to understand
how SIP affects the imbalance cashflows of different system participants.
Category TN (NPT) TS (Supplier) TG (Generator)
NPT✓ ✗ ✗
Generator✗ ✗ ✓
Supplier✗ ✓ ✗
Mixed Role More than one of TN, TS, and TG
Table 1: The definitions of the four main types of trading parties in our analysis, according
to their registration status with Elexon.
These definitions exclude opportunistic imbalances by asset-backed firms
who trade beyond their physical volumes (essentially non-physical trading).
However, it is difficult to distinguish the effects of these actions from passive
balancing or unintentional mismatches between traded position and metered
volume (e.g. wind forecast errors or outages). This is a significant caveat
of our analysis — the total effect of opportunistic imbalances may be larger
than quantified in this research. However, we aim to investigate purely SIP
by NPTs, whose trading model is primarily arbitrage rather than managing
a physical portfolio, and as such are likely to represent the majority of pure
speculative imbalance volumes.
We analyse the following two counterfactuals:
10

Any Metered Volume (AMV):All NPT imbalances are considered de-
liberate speculative volumes regardless of the party’s metered volume.
An NPT’s physical volume may be non-zero if, for example, they trade
over interconnectors, or optimise an asset on behalf of another party.
This represents an upper bound on total SIP volumes, discussed below.
Zero Metered Volume (ZMV):Only NPTs for whom their period me-
tered volume is 0 are included. In any given period, these NPTs are
a subset of all NPTs included in the AMV scenario. As such, this
counterfactual represents a lower bound on total SIP volumes.
The study covers 2021–2024. There are 48 settlement periods in a day
(except clock change days, in which there are 46 in short days and 50 in
long days), which gives a maximum of 70,128 data points. We remove
settlement periods in which data was partially or fully missing from the
analysis, losing 1,305 settlement periods (roughly 27 days’ worth of data).
Most of these points are due to market index price data missing, predom-
inantly in 2021, and physical BM data missing in September 2022, leaving
68,823 data points. The sources for all datasets used in this analysis can
be found in the replication guide in the online GitHub repository (https:
//github.com/PSALOxford/niv-chasing-bm-analysis/tree/main).
3.2. Assumptions
Underlying this research is the assumption that SIP does not affect the
imbalances of other parties. In other words, this implies that a supplier would
have found another counterparty with whom to trade in the counterfactual,
such that their overall imbalance (difference between traded and physical
positions) is unchanged, or in the case of a generator, there is simply less
generation on the system. Anecdotally, generators aim to match their ex-
pected output with their traded positions, unless they themselves are passive
balancing (such as smaller batteries). This assumption is one of the main
limitations of our work for two key reasons. First, without SIP, we would ex-
pect lower liquidity post-gate closure. This is a crucial period of the intraday
market for renewable generators looking to cover an imbalance implied by
forecast updates. However, this conservative assumption is in keeping with
underestimating the true benefits of SIP throughout this paper. Second, it is
unlikely that these assets would take the same passive imbalance positions in
the counterfactual, since the real time state of the system would be different.
11

However, it is impossible to know what these passive balancing volumes are,
so we do not attempt to account for this. On the supplier side, it is unlikely
they would be able to purchase the same volumes in the different scenar-
ios, since one of the key functions of NPTs is to provide liquidity. However,
this assumption should affect only the supplier imbalance benefit part of our
analysis, and not the overall picture on balancing volumes and costs.
Figure 2 is an example of this assumption. Suppose a supplier over-
forecasts their demand, and purchases power at intraday. In the factual
scenario (where NPT is allowed), an NPT might sell this contract, but with-
out backing the contract with physical output. In the counterfactual scenario
(where NPT is disallowed), the supplier might purchase the same amount of
energy from an asset-backed generator, thus increasing scheduled physical
system supply. Suppose the system has excess power. In the counterfactual
case, the SO would have to accept another bid to decrease supply, compared
to the factual case in which the NPT simply buys their shortage from the
settlement administrator.
Supplier
NPT
Buys
power
from
Supplier
Power
Plant
Buys
power
from
Factual
Counterfactual
Intraday
No
action
taken,
since
supplier
purchase
did
not
increase
net
supply
Balancing
Mechanism
Power
Plant
NESO
Sells
power
to
Supplier
Elexon
Sells
excess
to
NPT
Elexon
Buys
shortage
from
Supplier
Elexon
Sells
excess
to
Imbalance
Settlement
Figure 2: Stages of SIP for a scenario in which the system ends up with excess power due
to suppliers over-forecasting demand, demonstrating the differences in generation, system
balancing, andimbalancesettlementbetweenthefactual(withSIP)andthecounterfactual
(without).
For our analysis, we make three further key assumptions.
First, we assume that the stack of available actions in the BM is un-
changed between the factual and counterfactual scenarios. This does not
provide a perfect simulation of the counterfactual: clearly, if NPTs cannot
12

take speculative positions, and suppliers instead purchase the same energy
directly from generators, then the same generator will not submit the same
prices in the BM as they would in the factual case. However, we do not
expect that this assumption will alter our conclusions significantly. Anecdo-
tally, most speculative trades occur after gate closure, i.e. when BM units
have already submitted their physical positions, bids, and offers to the SO.
Hence most physical effects of SIP occur due to interactions with smaller
plants anyway, which do not interact with the BM significantly.
Second, our simulation assumes the SO takes balancing actions through
the BM (rather than ancillary services) in merit order. This means the results
in this paperunderestimatethe effects of SIP on balancing costs and hence
the settlement price, since the SO does not always accept balancing actions
in merit order, often because doing so would violate an existing transmission
constraint.
Third, we assume all balancing actions are flagged correctly (we discuss
the importance of ‘flagging’ further in Section 3.3.2). The SO flags actions
which address a system management constraint (e.g. thermal line capacity),
rather than energy balancing, since the BM handles both balancing responsi-
bilities. In our simulation, all SO-flagged actions are assumed to be taken in
the counterfactual, since we assume NESO would have taken the same sys-
tem management actions in the counterfactual (i.e. the level of SO-flagged
actions required is unchanged). The accuracy of this flagging procedure was
≥99.5% in FY2024–25 (NESO, 2025a), so we anticipate this assumption will
have a very limited impact on the results.
3.3. Methods
In this section, we discuss the methods used to calculate NIV, BM costs,
SP, and imbalance settlement costs in the counterfactual scenario without
SIP. A detailed guide on workflow replication can be found in the accompa-
nying GitHub repository. Table 2 provides a key for the symbols used in this
section.
3.3.1. Counterfactual Imbalance Volumes
We investigate the effects on imbalance volumes by calculating NIV in
each settlement period without NPTs. First, we calculate an aggregate im-
balance by NPTs from reports available upon request from Elexon which
provide the traded volume, metered volume, and energy imbalance volume
for each trading party in each settlement period.
13

Symbol Description
NGB trading parties classified as NPTs according to Table 1, a subset of all
GB trading parties
SGB trading parties classified as suppliers according to Table 1
GGB trading parties classified as generators according to Table 1
MGB trading parties classified as mixed role according to Table 1
Ip Imbalance (MWh) of partyp
qi Volume (MWh) of accepted balancing actioniin a given settlement period
(positive is offer; negative is bid)
pi Price (£/MWh) associated with accepted balancing actioni
Cp Imbalance cashflow (£) for partyp
BMTotal BM costs (£) in a given settlement period
Table 2: Definitions of symbols used in the methodology
Imb=
X
n∈N
In (1)
N IVis the net volume of balancing actions taken:
N IV=
X
i
qi (2)
However, a positive party imbalance implies the party is oversupplied.
Hence, the counterfactualN IV(N IV′) is calculated as:
N IV′ =N IV+Imb(3)
3.3.2. Balancing Mechanism Simulation
In our counterfactual BM simulation, we aim to model the balancing
actions the SO would have taken if the overall system imbalance wereN IV′,
i.e. without SIP. Figure 3 shows two examples of the simulation we run. In
both cases,N IV= 100MWh. In counterfactuals 1 and 2,Imb= 200and
−150MWh respectively, soN IV′ = 300and−50MWh.
Incounterfactual1, weaccept200MWhofupwardregulation. Weassume
the SO accepts offers starting with the marginal unflagged offer, in this case
from CCGT 1. If this plant has headroom, the SO accepts the remaining
volume at this price, before moving to the next cheapest offer (CCGT 2)
to fulfil the next portion of volume requirement. This merit-order process
repeats until the total accepted volume meets theN IV′ requirement. We do
14

Wind 1
-20 MWh @ £10/MWh
Battery 1
-30 MWh @ £5/MWh
Battery 2
25 MWh @ £40/MWh
Pumped Storage 1
50 MWh @ £55/MWh
CCGT 1
55 MWh @ £60/MWh
OCGT 1
20 MWh @ £90/MWh
Offers
Bids
Wind 1
-20 MWh @ £10/MWh
Battery 1
-30 MWh @ £5/MWh
Battery 2
25 MWh @ £40/MWh
Pumped Storage 1
50 MWh @ £55/MWh
CCGT 1
55 MWh @ £60/MWh
OCGT 1
20 MWh @ £90/MWh
CCGT 1
65 MWh @ £60/MWh
CCGT 2
90 MWh @ £70/MWh
OCGT 1
45 MWh @ £90/MWh
SO-Flagged Action
New Balancing Action
Factual
NIV = 100 MWh
Counterfactual 1
NIV' = 300 MWh
Wind 1
-20 MWh @ £10/MWh
Battery 1
-30 MWh @ £5/MWh
Battery 2
25 MWh @ £40/MWh
Pumped Storage 1
5 MWh @ £55/MWh
OCGT 1
20 MWh @ £90/MWh
Counterfactual 2
NIV' = -50 MWh
Battery 3
-50 MWh @ £2/MWh
Figure 3: Schematic of merit order simulation for two counterfactual imbalances: one in
which the SO requires extra upward regulation, and another in which accepted volume
must be removed and further bids accepted.
not remove accepted bids in this instance, on the assumption that these bids
were required to manage short-term fluctuations in supply and demand.
In counterfactual 2, we reduce the imbalance volume by150MWh. To
do so, the most expensive unflagged offers are removed, until the volume
of offers matches the volume of bids. Then, the SO accepts the highest
priced bids, starting with the current marginal downward regulation plant
(in this case Battery 1). In this example, we suppose Battery 1 has no
footroom, and as such the SO accepts a bid from the next highest priced
unit, Battery 3. As before, SO-flagged actions are unchanged between the
factual and counterfactual. Pseudocode for our simulation engine is available
in Appendix A.
3.3.3. Financial Effects
The counterfactual BM costs to the SO are calculated directly from the
new settlement stack as:
15

BM=
X
i
qipi (4)
From the counterfactual stack of balancing actions (e.g. Counterfactuals
1 and 2 in Figure 3), we use Elexon’s procedures to calculateSP′ (Elexon,
2025a,b). Elexon aims to calculate a price which reflects the cost of managing
supply-demand imbalances over the 30-minute settlement period. As such,
notallbalancingactionscontributetoSP—forexample, actionswhichman-
age transmission constraints, or short duration/very small volume actions do
not set the imbalance price. The full calculation is not detailed here since it
is not an original part of our methodology, but the algorithm is implemented
in the supporting GitHub repository and replicated in pseudocode in Ap-
pendix A. The algorithm written to calculateSPfrom balancing actions was
backtested on 2024 data to ensure accuracy.
UsingSP (′) we calculate the imbalance settlement charges/payments to
each party, which are just signed net cashflows through the imbalance settle-
ment mechanism:
C (′) p =I p ·SP (′) (5)
where positive is a payment to the party. In calculating aggregate cashflows
for each of the types of trading parties in Table 1 (supplier, generator, or
mixed role), we sum the cashflows for each trading party in that type. For
example, supplier cashflows are defined as:
CS =
X
p∈S
Cp (6)
4. Results
Our study covers each half-hour period from 2021 to 2024, excluding
periods in which relevant data was missing. A summary of the key results
can be found in Table 3, discussed in greater detail in the subsections to
follow.
4.1. Imbalance Volumes
We run the two scenarios AMV (any metered volume) and ZMV (zero
metered volume) explained in Section 3.1 in our analysis. These aim to
16

Metric (unit) F actual AMV ZMV AMV - F actual ZMV - F actual
Average NIV (MWh) 1.9 -26.0 -16.0 -27.9 -17.9
Average absolute NIV (MWh) 233 278 291 44.3 57.3
Total absolute NIV (TWh) 16.1 19.1 20.0 3.1 3.9
NIV standard deviation
(MWh)
312 361 378 48.1 65.3
Max NIV (MWh) 1737 1792 2281 54.5 544
Min NIV (MWh) -1869 -1925 -1936 -55.5 -66.7
% |imbalances|>1GWh 0.71 1.21 1.44 0.50 0.73
Total BM costs (£bn) 9.00 9.40 9.35 0.40 0.35
Average system price
(£/MWh)
119.8 121.3 119.2 1.47 -0.62
Total SO imbalance
settlement cashflow (£m)
853 959 1032 106 179
Simbalance cashflow (£m) -106 -431 -299 -325 -193
Gimbalance cashflow (£m) -221 -280 -263 -60 -42
Mimbalance cashflow (£m) 93 -69 -0.9 -163 -94
Table 3: Comparison of factual and modelled system imbalance metrics. A positive NIV
implies the system was short. All financial results are in nominal terms.
bound our estimate of the true effects of SIP through the net effect of all
NPTs (AMV) and pure SIP (ZMV). Our results indicate that SIP reduced
the total volume and volatility of required balancing actions, as shown in
Figures 4 and 5 which we discuss now.
Figure 4(a) demonstrates the effect of shifting otherwise required bal-
ancing volumes into the wholesale markets on the total absolute volume of
balancing actions required over 2021–2024. Notably, in each year, the total
volume of balancing actions NESO would have had to take would have been
higher without SIP in both the AMV and ZMV cases. Figure 4(b) shows
the effect of SIP on the average imbalance volume in each settlement period.
This highlights that SIP can significantly alter both the sign and magnitude
of the average raw imbalance. The financial implications of these results are
explored in Section 4.2.
Figure 5 demonstrates the effect of SIP on the volatility and tails of
the imbalance distribution through a quantile difference plot for the AMV
(Figure 5(a)) and ZMV (Figure 5(b)) scenarios. These results indicate that
thetailsoftheimbalancedistribution(below/abovethe10 th/90th percentiles)
are more extreme in the counterfactuals. This suggests SIP reduces the
17

2021 2022 2023 2024
Year
0.0
0.2
0.4
0.6
0.8
1.0
1.2
Difference in T otal Absolute
Imbalance Volume (TWh)
(a)
AMV  Factual
ZMV  Factual
2021 2022 2023 2024
Year
60
40
20
0
20
40
60
Average Period Imbalance Volume (MWh)
(b)
Factual
AMV
ZMV
Figure 4: (a) Bar chart showing the difference in the total absolute volume of balancing
actions required by year between the counterfactual without SIP (AMV/ZMV cases) vs
the factual, with NPTs. (b) Bar chart showing the effect of SIP on the average period
imbalance by year, comparing the factual and counterfactual scenarios.
frequency of extreme events, which is important for balancing reserve sizing.
Both plots reveal a clear positive slope, which (in our case) indicates a more
volatile imbalance volume in the counterfactual.
Beyond the summaries above, we present a high-level summary of the
effect of SIP on balancing volumes in Table 4. In this table, we present the
proportion of periods in which the aggregate NPT imbalance interacted with
the overall system imbalance under our different scenarios. The average NPT
position indicates that in both scenarios, NPTs are net sellers in the intra-
day market and hence take an average short position through to imbalance.
The averageabsoluteposition is of a comparable magnitude to the average
absolute factual NIV (see Table 3). A naive comparison of NPT imbalances
would find that these do not oppose the outturn NIV in the AMV case on av-
erage, and only do so 56.5% of the time in the ZMV case. This could indicate
that SIP fails to anticipate NIV correctly, and as such does not contribute
to system balancing. However, this would be an inappropriate reading of
the results. In both cases, NPTs correctly anticipate the sign of the system
imbalancewithout their interventionaround 70% of the time. The difference
betweenthesetworesults liesinmultiple NPTsattempting todefeatthesame
18

0 20 40 60 80 100
Quantile (%)
125
100
75
50
25
0
25
50
AMV  Factual Quantile Difference (MWh)
(a)
0 20 40 60 80 100
Quantile (%)
150
100
50
0
50
100
ZMV  Factual Quantile Difference (MWh)
(b)
Figure 5: Quantile difference between counterfactual (without NPTs) and factual (with
NPTs) net imbalance volumes 2021–2024. Only the 1st–99th percentiles are displayed for
clarity of representation.
imbalance. Most importantly, even with competition among NPTs flipping
the sign of the imbalance, the absolute counterfactual NIV would have been
larger without NPTs more often than not in both cases. This explains the
observed reduction in absolute imbalance volumes observed in Table 3.
4.2. Financial Effects
By reducing the balancing volumes required, SIP affects the costs NESO
incurs through the BM, and imbalance settlement costs for other parties
through changes to SP. While there will also be financial consequences in the
ex-ante markets, we do not provide estimates for this within this research.
Doing so would shift the focus from using publicly available data to support
precise calculations towards estimating impacts on day-ahead and intraday
markets, which would be useful future research. We find that SIP brings
significant overall financial benefits in the BM and at imbalance settlement.
Figure 6 plots the simulated difference in BM costs across the scenar-
ios. Overall, SIP reduces balancing costs by between £396m (AMV) and
£347m (ZMV), a significant (5.9–6.7%) reduction in the overall spend on
SO-unflagged actions in the BM over the period 2021–2024 (£5.54bn). How-
ever, the plot reveals significant differences by year. Most notably, the AMV
19

Metric (unit) AMV ZMV
Average NPT position (MWh) -27.9 -17.9
Average absolute net NPT position (MWh) 198 123
NPT position standard deviation (MWh) 254 163
Max aggregate imbalance position (MWh) 1477 1946
NPT imbalance opposed tofactualsystem imbalance (%) 43.1 56.5
NPT imbalance opposed tocounterfactualsystem imbalance (%) 68.0 71.0
Absolute counterfactual imbalance > absolute factual imbalance (%) 57.4 65.0
Sign of counterfactual imbalance̸=sign of factual imbalance (%) 25.0 14.4
Table 4: Summary of the interaction between NPT imbalance volumes and fac-
tual/counterfactual imbalance volumes.
case appears to represent a net cost to the SO in 2022, while the benefits
in 2024 are significantly smaller than other years. To understand this het-
erogeneity, we return to Figure 4(b). In 2022, the average imbalance in the
AMV case was -49.5 MWh, compared with 15.0 MWh in the factual case. Al-
though SIP reduced the total imbalance volume in 2022-AMV (Figure 4(a)),
the average imbalance flipped from long (AMV) to short (factual). As such,
the SO went from receiving payments to reduce generation, to paying to in-
crease generation. 2024 is a similar story: average imbalance in AMV and
ZMV cases was significantly longer, meaning the SO received lower revenues
for reducing output. This motivates the need to look at imbalance costs as
well as balancing costs to understand the true effect of SIP: although the
SO (and hence consumers) might appear to benefit from lower balancing
costs, oversupplied retailers would have received lower imbalance settlement
revenue.
Suppliers pay back to the SO on aggregate at imbalance in both scenarios.
However, SIP reduced this liability by £325m (75% reduction) for AMV, and
£193m (65% reduction) for ZMV due to changes in SP. Similarly, generators
pay back to the SO on aggregate at imbalance, but notably this liability is
also higher (by £60m/£42m; SIP reduced this liability by 21%/16%) in the
AMV/ZMV cases. SIP has two main effects on the system imbalance (and
hence SP) which explain imbalance costs for both suppliers and generators
being lower in the factual case. First, suppliers’ and generators’ imbalances
are less strongly (positively) correlated with the overall system imbalance
in the factual case. This means there are more occasions in which the sup-
plier/generator has a ‘helpful’ imbalance, settled at a favourable price. For
example, SIP means suppliers are long when the system is short more often,
20

2021 2022 2023 2024
Year
100
0
100
200
300
Difference in BM Costs
(£m, nominal)
AMV  Factual
ZMV  Factual
Figure 6: Bar chart plotting the differences in BM costs between AMV and ZMV scenarios
and the factual (with SIP) by year.
and suppliers benefit from high imbalance payments. Second, when suppli-
ers’/generators’ imbalances are in the same direction as the overall system
imbalance, SIP tends to reduce the overall system imbalance, meaning these
imbalances are settled at a less extreme price. Table 5 summarises these
differences.
Overall imbalance cashflows to Elexon, the settlement administrator, in
the counterfactual are £106m/£179m higher, a 12%/21% increase, driven
by higher imbalance costs to suppliers and generators. The change in total
cashflow does not match the sum of the change in cashflows for suppliers and
generatorssincetheoverallchangeincashflowincludescashflowchangesfrom
otherpartytypes(suchasNPTsoraggregators)whichwedonotincludehere.
Changes to the imbalance cashflows of these other parties due to changes to
the imbalance price explain the difference.
The financial effects on generators are likely asymmetric depending on
the technology type. Smaller renewable generators, who are more prone
to forecast errors and may be unable to self-balance their production, are
more exposed to imbalance prices than larger firms with bigger portfolios
and more conventional, controllable assets. To demonstrate this, Figure 7
plots the quantiles ofSP AM V /ZM V−P ID againstSP−P ID.P ID is an in-
21

Supplier Generator
Metric (unit) F actual AMV ZMV F actual AMV ZMV
S/Gimbalance correlation
with system imbalance
0.40 0.66 0.54 0.38 0.51 0.44
S/Gimbalance in same di-
rection as system imbalance
(%)
64.1 75.1 69.8 63.4 68.7 65.9
SP when system andS/G
short (£/MWh)
168.89 189.23 180.74 164.21 173.21 172.04
SP when system andS/G
long (£/MWh)
69.75 62.69 62.37 68.64 61.58 61.87
Table 5: Summary of the interaction between supplier and generator imbalance volumes
and factual/counterfactual imbalance volumes and settlement prices.
traday reference price of the volume-weighted average price of all half-hourly
contract trades on EPEX Spot in GB in the hour before gate closure. These
plots aim to represent that SIP compresses real time scarcity margins in the
BM. SIP in this time period will have some effect on the intraday price,
generally in the opposite direction to the difference between the outturn
SP and intraday price. As such, these plotsunderestimatethe extent to
which SIP compresses scarcity margins. However, the plots reveal that the
real time scarcity/oversupply premium is significantly larger without SIP.
This indicates that this trading strategy closes arbitrage opportunities, and
contributes to a more efficient intraday and balancing market. This suggests
that SIP reduces imbalance price risk for other system users, with the largest
benefits accruing to those parties most exposed to imbalance prices through
forecast errors (namely suppliers and small renewable generators). Larger
generating firms also lose out through reduced balancing revenues.
5. Discussion and Policy Implications
Ten years after the switch to single imbalance pricing, this paper marks
the first research on how SIP affects the electricity system. Given the toler-
ance of the GB system towards opportunistic imbalancing and NPT market
participation, this is an area of interest to electricity policymakers beyond
GB considering the effects of switching to single imbalance pricing and al-
lowing opportunistic imbalancing. Such relaxations could significantly alter
22

150
 100
 50
 0 50 100 150
Quantiles of Factual System Price
- Intraday Price (£/MWh)
200
100
0
100
200
Quantiles of AMV System Price
- Intraday Price (£/MWh)
150
 100
 50
 0 50 100 150
Quantiles of Factual System Price
- Intraday Price (£/MWh)
200
150
100
50
0
50
100
150
200
Quantiles of ZMV System Price
- Intraday Price (£/MWh)
Figure 7: Q–Q plots displaying the quantiles of the difference between the counterfactual
system price and the intraday price, and the factual system price and the intraday price
in both AMV and ZMV scenarios. 1st–99th percentiles displayed.
market dynamics in, for example, Belgium and Germany. This research also
provides the first major analysis of the role of NPTs in the GB system.
Our modelling indicates that SIP reduces consumer bills through a re-
duction in the pass-through of imbalance settlement costs to suppliers and
BM costs incurred by NESO to consumers. Although we do not model the
benefits of intraday trading with NPTs to suppliers, NPTs are net sellers
in the intraday markets, which exerts downward pressure on prices. We
would expect additional competition to encourage generators to offer closer
to the competitive equilibrium price, likely contributing to lower wholesale
costs, further reducing bills. We conclude that the incentives for SIP in the
GB system align with the aims of the imbalance pricing modification, in re-
flecting the value of helpful imbalances to participants – NPTs, NESO, and
consumers benefit from this practice.
While generators benefit from lower imbalance settlement costs, and re-
newable generators (who are most exposed to the imbalance price through
forecast errors) in particular benefit from a less volatile imbalance price, the
effects of SIP on generators on the whole are less clear-cut. First, reduced
balancing volumes reduce generator BM revenues. Second, NPTs are net
23

sellers in the intraday markets. Throughout, we assume the imbalances of
all other parties are the same in the factual and the counterfactual scenarios.
This does not entail that each NPT intraday sale displaces a generator sale:
participants may otherwise self-balance their portfolios rather than using in-
traday trading, or the trade might not have been executed at all. However,
further competition at intraday does reduce revenues to generators at the
margin, at a benefit to purchasers who pay lower prices. In this sense, SIP
represents a transfer from generators to NPTs, the SO and suppliers.
Through changing the scheduled operations of units via ex-ante trad-
ing and the balancing volume requirement, SIP will affect carbon emissions.
However, the effect of SIP on system emissions requires estimating which
units respond to price movements in ex-ante markets, together with the
trades corresponding to open positions for SIP. Neither of these inputs can
be precisely calculated from publicly available data. As in Section 4.2, future
research could extend the methodology of this paper to estimate the effects of
SIP on ex-ante market prices and emissions. However, we now provide both
quantitative and qualitative arguments to suggest that SIP reduces power
system emissions. We note that the GB power system is subject to the UK
emissions trading scheme, and as such a reduction in power system emis-
sions may be offset by an increase elsewhere as out-of-merit producers sell
on their allowances. However, reducing power system emissions is one of the
key priorities for the UK government.
First, the UK government’s preferred approach to calculating emissions
changestotheGBpowersystem, long-runmarginalemissionsfactors(DESNZ,
2023), does not apply to this investigation, since we do not investigate a sus-
tained change in demand. Instead, we calculate the balancing mechanism
marginal emissions factor (MEF), as in (LCP & EnAppSys, 2014). Essen-
tially, this short-run statistic measures the short-run carbon cost of flexibility,
and indicates how often NESO requires carbon intensive units to balance the
system. A higher MEF implies a greater requirement to maintain carbon
intensive units on hand for system balancing. In the factual case, the aver-
age MEF was 239 kgCO2e/MWh, compared to 279 and 272 kgCO2e/MWh
in the AMV and ZMV cases. Lower balancing volumes reduce reliance on
carbon intensive units for energy balancing.
Second, the further ahead of time the system is balanced, the larger the
stack of plants which are able to change their output to help system balanc-
ing. This allows more efficient CCGTs (for example) to step in and increase
their output, rather than relying on less efficient but more flexible peakers to
24

respond to shortages. Similarly, running fewer plants closer to their full out-
put improves emissions due to efficiency gains and a lower number of plant
start-ups, and flatter output schedules reduce operational costs.
Third, although not a direct short-run carbon impact, SIP seems to both
reducethevolatilityofthesettlementprice(seeSection4.2)andallowsmaller
renewable generators to trade away their imbalances close to real time. This
provides a long-run benefit to those most exposed to imbalance settlement
prices, particularly variable renewable generators and suppliers. Reducing
SP tail risk can help the business case for further renewable investment, as
wellasreducinghedging/overcautioncostsfromsuppliersseekingtominimise
their downside risk.
Our research relies on key assumptions and simplifications to the com-
plexities of system balancing. Notably, we have neglected the interactions of
SIP with transmission constraints, which is one of the key concerns raised
regarding this trading strategy (NESO, 2026). This simplification does not
affect the conclusions of our results on the benefits of SIP for supply and
demand balancing. In practice, energy balancing must account for trans-
mission constraints, and as such our merit order model is a conservative
estimate of the reduction in balancing costs due to SIP, in keeping with our
approach throughout. However, it is possible that changes to other units’
schedules due to trades with NPTs could either help to resolve or aggravate
a transmission constraint. For example, an NPT buying at intraday might
induce a unit in an export constrained region to turn up, requiring the SO
to reduce further generation in this region, while increasing generation else-
where. Alternatively, an intraday trade in the other direction may alleviate
the constraint, serving a dual purpose. Data currently available makes fur-
ther analysis of this interaction challenging: counterparties of intraday trades
are not available, constraint data in GB is scarce, and the correspondence
between an executed trade and the change to a given unit’s schedule is com-
plicated by portfolio-level optimisation. Further research in this area, subject
to improved data availability, would add to the research we present here.
Our analysis demonstrates the empirical benefits of SIP in a mature mar-
ket with significant and growing renewables penetration for the first time.
The proposal to realign the market closure deadline with gate closure (one
hour in advance of delivery) (DESNZ, 2025) risks reducing SIP by NPTs.
Given NPTs tend to open their positions within the final hour, reacting to
updated forecasts and real time bid/offer acceptances by NESO, restricting
SIP in this way would likely lead to lower activity, moving wholesale volumes
25

into the BM, running counter to broader aims for the power market. Ulti-
mately, a drop in SIP would harm consumers, suppliers, smaller generators,
and NESO, with a likely gain for larger established generating firms.
The results of this analysis cannot be applied directly to other European
markets with similar structures, due to differences in information availabil-
ity in particular. However, this research should provide a starting point for
similar analyses in other systems, and demonstrates the possibility of overall
system benefits to other countries considering permitting speculative imbal-
ance positions.
Acknowledgements
The authors thank David Mlynski, Nicholas Wood, Andrew Richards,
and the wider team at Outlook Energy for helpful discussions and feedback
on drafts of this manuscript. The authors would like to acknowledge that the
DPhil studentship which made this research possible is funded by Outlook
Energy through the University of Oxford.
Declaration of generative AI and AI-assisted technologies in the
manuscript preparation process
During the preparation of this work, the authors used Claude and Chat-
GPT in the implementation of the simulation code, and reviewing drafts of
the manuscript. The authors reviewed and edited the output as needed and
take full responsibility for the content of the published article.
References
ACER, 2020. Harmonisation of imbalance settlement.https:
//www.acer.europa.eu/electricity/market-rules/electricity-
balancing/harmonisation-of-imbalance-settlement. Accessed: 28
July 2025.
Birge, J.R., Hortaçsu, A., Mercadal, I., Pavlin, J.M., 2018. Limits to arbi-
trage in electricity markets: A case study of MISO. Energy Economics 75,
518–533.
Boogert, A., Dupont, D., 2005. On the effectiveness of the anti-gaming policy
betweentheday-aheadandreal-timeelectricitymarketsinthenetherlands.
Energy Economics 27, 752–770.
26

Browell, J., 2018. Risk constrained trading strategies for stochastic genera-
tion with a single-price balancing market. Energies (Basel) 11, 1345–.
Bruneel, R., Schuurmans, M., Patrinos, P., 2025. Optimal intraday power
trading for single-price balancing markets: An adaptive risk-averse strat-
egy using mixture models. Applied Energy 389, 125754–.
Bunn, D.W., Gianfreda, A., Kermer, S., 2018. A trading-based evaluation
of density forecasts in a real-time electricity market. Energies (Basel) 11,
2658–.
Bunn, D.W., Inekwe, J.N., MacGeehan, D., 2021. Analysis of the fundamen-
tal predictability of prices in the british balancing market. IEEE Transac-
tions on Power Systems 36, 1309–1316.
Bunn, D.W., Kermer, S.O., 2021. Statistical arbitrage and information flow
inanelectricitybalancingmarket. TheEnergyJournal(Cambridge, Mass.)
42, 19–40.
Chaves-Ávila, J., Hakvoort, R., Ramos, A., 2014. The impact of european
balancing rules on wind power economics and on short-term bidding strate-
gies. Energy Policy 68, 383–393.
Chen, H., Li, J., O’Leary, N., Shao, J., 2024. Examining the drivers of
the imbalance price: Insights from the balancing mechanism in the united
kingdom. Journal of Environmental Management 371, 123239.
Clò, S., Fumagalli, E., 2019. The effect of price regulation on energy imbal-
ances: A difference in differences design. Energy Economics 81, 754–764.
DESNZ, 2023. Guidance on Valuation of Energy Use and Greenhouse
Gas (GHG) Emissions: Background Documentation. Technical Report.
DESNZ. URL:https://assets.publishing.service.gov.uk/media/
66c85e891f215d9f0a913536/guidance-on-valuation-of-energy-
use-ghg-emissions-background-documentation.pdf. accessed: 4
December 2025.
DESNZ, 2024. Review of electricity market arrangements (rema) second
consultation document.https://assets.publishing.service.gov.
uk/media/65ef6694133c220011cd37cd/review-electricity-market-
27

arrangements-second-consultation-document.pdf. Accessed: 28 July
2025.
DESNZ, 2025. Review of Electricity Market Arrangements (REMA) REMA
Summer Update.https://assets.publishing.service.gov.uk/
media/686f71412557debd867cbeff/review-of-electricity-market-
arrangements-rema-summer-update-2025.pdf. Accessed: 28 July 2025.
Eicke, A., Ruhnau, O., Hirth, L., 2021. Electricity balancing as a market
equilibrium: An instrument-based estimation of supply and demand for
imbalance energy. Energy Economics 102, 105455–.
Elexon, 2019a. BSC Insights: What is Driving Increases in Electricity
Imbalance Volumes?https://www.elexon.co.uk/bsc/operational/
balancing-and-settlement/elexon-insights-what-is-driving-
increases-in-electricity-imbalance-volumes-july-2019/. Ac-
cessed: 28 July 2025.
Elexon, 2019b. Investigations into NIV-chasing in GB electricity market
– 294 September 2019 panel meeting.https://www.elexon.co.uk/
bsc/documents/groups/panel/2019-meetings/294-september/294-
09-investigations-into-niv-chasing-in-gb-electricity-market-
shadrack-nyarko/. Accessed: 8 December 2025.
Elexon, 2025a. BSC Section T: Settlement and Trading Charges – Annex T-
1. Elexon. URL:https://bscdocs.elexon.co.uk/bsc/bsc-section-t-
settlement-and-trading-charges#annex-t-1. effective from 16 April
2025; Online document.
Elexon, 2025b. Imbalance pricing guidance.https://bscdocs.elexon.co.
uk/guidance-notes/imbalance-pricing-guidance. Effective From 14
July 2025. Accessed: 17 February 2026.
Ghiassi-Farrokhfal, Y., Belo, R., Hesamzadeh, M.R., Bunn, D., 2023. Opti-
mal electricity imbalance pricing for the emerging penetration of renewable
and low-cost generators. Manufacturing & Service Operations Manage-
ment 25, 1966–1983.
Jha, A., Wolak, F.A., 2019. Can Financial Participants Improve Price Dis-
covery and Efficiency in Multi-Settlement Markets with Trading Costs?
28

NBER working paper series no. w25851, National Bureau of Economic
Research, Cambridge, Mass.
Jha, A., Wolak, F.A., 2023. Can forward commodity markets improve spot
market performance? evidence from wholesale electricity. American eco-
nomic journal. Economic policy 15, 292–330.
Just, S., Weber, C., 2015. Strategic behavior in the german balancing energy
mechanism: incentives, evidence, costs and solutions. Journal of Regula-
tory Economics 48, 218–243.
Karimi Madahi, S.S., Claessens, B., Develder, C., 2024. Distributional rein-
forcement learning-based energy arbitrage strategies in imbalance settle-
ment mechanism. Journal of Energy Storage 104, 114377–.
Koch, C., 2022. Intraday imbalance optimization: incentives and impact of
strategic intraday bidding behavior. Energy Systems (Berlin. Periodical)
13, 409–435.
Koch, C., Hirth, L., 2019. Short-termelectricitytradingforsystembalancing:
An empirical analysis of the role of intraday trading in balancing germany’s
electricity system. Renewable & Sustainable Energy Reviews 113, 109275–.
Koch, C., Maskos, P., 2020. Passive balancing through intraday trading:
Whether interactions between short-term trading and balancing stabilize
germany’s electricity system. International Journal of Energy Economics
and Policy 10, 101–112.
Lago, J., Poplavskaya, K., Suryanarayana, G., De Schutter, B., 2021. A
market framework for grid balancing support through imbalances trading.
Renewable and Sustainable Energy Reviews 137, 110467.
LCP & EnAppSys, 2014. Analysis of the marginal emission
factor (mef).https://assets.publishing.service.gov.uk/media/
5a7dacfde5274a5eaea65a89/MEF_Analysis_-_Report_FINAL.pdf. Ac-
cessed: 29 July 2025.
Lisi, F., Edoli, E., 2018. Analyzing and forecasting zonal imbalance signs in
the italian electricity market. The Energy Journal 39, 1–20.
29

Matsumoto, T., Bunn, D., Yamada, Y., 2022. Mitigation of the inefficiency in
imbalance settlement designs using day-ahead prices. IEEE Transactions
on Power Systems 37, 3333–3345.
Mercadal, I., 2022. Dynamic Competition and Arbitrage in Electricity Mar-
kets: The Role of Financial Players. MIT Center for Energy and Environ-
mental Policy Research.
Möller, C., Rachev, S.T., Fabozzi, F.J., 2011. Balancing energy strategies in
electricity portfolio management. Energy Economics 33, 2–11.
NESO, 2025a. Accuracy of System Management Action Flagging (P217A):
May 2024 – April 2025. Technical Report. NESO. URL:https://www.
neso.energy/document/366271/download. accessed: 28 July 2025.
NESO, 2025b. Britain’s electricity explained: 2024 review.https://www.
neso.energy/news/britains-electricity-explained-2024-review.
Accessed: 28 July 2025.
NESO, 2026. Reformed National Pricing: Balancing, Settlement and Dis-
patch — Call for Input. Technical Report. National Energy System
Operator (NESO). URL:https://www.neso.energy/document/376966/
download. accessed 11 February 2026.
Ofgem, 2015. Balancing and Settlement Code (BSC) P305: Electric-
ity Balancing Significant Code Review Developments. Technical Re-
port. Ofgem. URL:https://www.ofgem.gov.uk/sites/default/files/
docs/2015/04/p305d_1.pdf. accessed 28 July 2025.
Parsons, J.E., Colbert, C., Larrieu, J., Martin, T., Mastrangelo, E., 2015. Fi-
nancial Arbitrage and Efficient Dispatch in Wholesale Electricity Markets.
Technical Report 15-002. MIT Center for Energy and Environmental Pol-
icy Research. Available at SSRN:https://ssrn.com/abstract=2574397
orhttp://dx.doi.org/10.2139/ssrn.2574397.
Pozzetti, L., Cartlidge, J., 2020. Trading electricity markets using neural
networks, in: Affenzeller, M., Bruzzone, A., Longo, F., Petrillo, A. (Eds.),
Proceedings of the 32nd European Modeling & Simulation Symposium
(EMSS 2020), European Modeling & Simulation Symposium. pp. 311–318.
30

Saravia, C., 2003. Speculative Trading and Market Performance: The Effect
ofArbitrageursonEfficiencyandMarketPowerintheNewYorkElectricity
Market.
van der Veen, R.A., Abbasy, A., Hakvoort, R.A., 2012. Agent-based analysis
of the impact of the imbalance pricing mechanism on market behavior in
electricity balancing markets. Energy Economics 34, 874–881.
Appendix A. Pseudocode for the counterfactual simulation
This appendix sets out the counterfactual simulation described in Sec-
tion 3.3.2. The purpose is to provide a conceptual overview of the algorithms
used in the simulation, and should be read in conjunction with the replication
guide for the accompanying repository:https://github.com/PSALOxford/
niv-chasing-bm-analysis/tree/main.
Notation.Each settlement period is indexed byt.N IV t is the factual Net
Imbalance Volume (NIV), in MWh, withN IVt >0meaning the system
is short. The factual settlement stackS t is the set of accepted balancing
actionsa. Each action has a BM Unit (BMU)u a, a bid–offer pair number
ka (ka >0for offers,k a <0for bids), a pricep a, a volumeq a (qa >0for
offers,q a <0for bids) and a System Operator (SO) flagf a.B t is the set
of bid–offer pairs submitted fort. Each pair has a levelLu,k in MW, which
contributes 1 2 Lu,k MWh over the half-hour SP.PNu,MELS u andMILS u are
the Physical Notification, Maximum Export Limit and Maximum Import
Limit, each integrated over the SP to give MWh.Pis the set of BSC parties
andN⊆ Pis the subset classified as non-physical traders (NPTs). For party
i,I i,t is its energy imbalance volume andCi,t its imbalance charge, both from
MR1B. Primes (e.g.N ′ t,S ′ t,P ′ t) denote counterfactual quantities.
31

Algorithm 1Re-dispatch of the settlement stack to the counterfactual NIV
1:functionRedispatch(S, N, N′,B, H)
2:S ′ ← S
3:ifN >0andN ′ >0then▷short in both cases
4:ifN ′ > Nthen
5:S ′ ←Accept(S ′, N′ −N,B, H)▷accept further offers
6:else
7:(S ′, R)←Remove(S ′, N−N ′)▷remove marginal offers
8:ifN−R > N ′ then
9:S ′ ←Accept(S ′, N′ −(N−R),B, H)▷accept bids
10:end if
11:end if
12:else ifN <0andN ′ <0then▷long in both cases
13:ifN ′ < Nthen
14:S ′ ←Accept(S ′, N′ −N,B, H)▷accept further bids
15:else
16:(S ′, R)←Remove(S ′, N−N ′)▷remove marginal bids
17:ifN−R < N ′ then
18:S ′ ←Accept(S ′, N′ −(N−R),B, H)▷accept offers
19:end if
20:end if
21:else▷NIV changes sign
22:(S ′, R)←Remove(S ′, N)▷remove energy actions in the factual direction
23:S ′ ←Accept(S ′, N′ −(N−R),B, H)▷accept actions in the opposite
direction
24:end if
25:returnS ′ sorted by price
26:end function
Algorithm 2Headroom available on each submitted bid–offer pair
1:functionHeadroom(B,S,PN,MELS,MILS)
2:for allBMUsuinBand pairskofu, taken in orderk= 1,2, . . .(offers) and
k=−1,−2, . . .(bids)do
3:A u,k ← P a∈S:u a=u, ka=k qa ▷volume already accepted on the pair
4:D u,k ←PN u + 1 2 P jbeforek Lu,j ▷energy delivered by earlier pairs
5:ifk >0then
6:H u,k ←max

min(Du,k + 1 2 Lu,k,MELS u)−D u,k −A u,k,0 
7:else
8:H u,k ←min

max(Du,k + 1 2 Lu,k,MILS u)−D u,k −A u,k,0 
9:end if
10:end for
11:returnH
12:end function
32

Algorithm 3Accepting additional balancing actions in merit order. The
direction isσ= sgn(∆), withσ= +1for offers andσ=−1for bids.
1:functionAccept(S,∆,B, H)▷add|∆|MWh of new actions in directionσ
2:M ←pairs inBof directionσin merit order (offers by ascending price; bids by
descending price)
3:a ∗ ←marginal energy action of directionσinS: the most expensive unflagged
offer (σ= +1) or cheapest unflagged bid (σ=−1) with non-zero de minimis-adjusted
volume
4:ifno sucha ∗ then
5:j 0 ←1
6:else if(u a∗ , ka∗ )∈ Mthen
7:j 0 ←position of(u a∗ , ka∗ )inM
8:else
9:j 0 ←position of the pair inMpriced nearest top a∗ that lies strictly beyond
it in merit order
10:end if
11:r← |∆|
12:forj=j 0, . . . ,|M|do▷continue up the merit order from the factual margin
13:(u, k, π)← M j;v←min(|H u,k|, r)
14:ifv >0then
15:S ← S ∪ {(u, k, p=π, q=σv, f=false)};r←r−v
16:end if
17:ifr≤0then
18:break
19:end if
20:end for
21:returnS
22:end function
33

Algorithm 4Removing accepted energy balancing actions from the margin
inward. The direction isσ= sgn(∆), withσ= +1for offers andσ=−1for
bids.
1:functionRemove(S,∆)▷remove up to|∆|MWh of accepted actions in directionσ
2:r← |∆|
3:for alla∈ Swithf a =false andsgn(q a) =σ, from the margin inward (offers by
descending price; bids by ascending price)do
4:v←min(|q a|, r);r←r−v
5:ifv=|q a|then
6:S ← S \ {a}
7:else
8:q a ←q a −σv
9:end if
10:ifr≤0then
11:break
12:end if
13:end for
14:return

S, R=σ(|∆| −r)

▷ R: signed volume removed
15:end function
34

Algorithm 5Counterfactual imbalance price (following BSC Section T,
Annex T-1). †Most expensive in merit order: highest-priced buy actions if
N ′ >0, lowest-priced sell actions ifN′ <0.
1:functionImbalancePrice(S ′, N′,MIP,BPA,SPA,TLM)
2:ifS ′ =∅then
3:returnMIP
4:end if
5: Buy setS + ← {a:q a ≥0}by ascending price; sell setS − ← {a:q a <0}by
descending price
6:De minimis tagging:q a ←0if|q a|<0.1MWh and the total volume of the
same BMU and pair is<0.1MWh
7:Arbitrage tagging:net off each sell action against buy actions with price≤its
price
8:Flagging:actions that are SO or CADL flagged are first-stage flagged. Buy
actions priced above the most expensive first-stage-unflagged buy, and sell actions
priced below the cheapest first-stage-unflagged sell, are second-stage flagged. If no
action is first-stage unflagged, all actions are second-stage flagged.
9:NIV tagging:net off buy and sell volumes, starting from the most expensive buy
(if net short) or the cheapest sell (if net long)
10:R ← S + ifN ′ >0elseS −, keeping only actions with non-zero remaining volume;
PA←BPAifN ′ >0elseSPA
11:if P a∈R qa = 0then
12:returnMIP
13:end if
14:ifany action inRis second-stage flaggedthen
15:RP←volume-weighted price ofthe most expensive † 1 MWh(RPAR) ofsecond-
stage-unflagged actions inR, orMIPif there are none
16: Reprice second-stage-flagged actions atRPand re-rankR
17:end if
18:P AR tagging:keep only the most expensive † 1 MWh (PAR) ofR
19:return
P
a∈R TLMua qapaP
a∈R TLMua qa
+ PA▷TLM u = 1ifuhas no TLM
20:end function
35
