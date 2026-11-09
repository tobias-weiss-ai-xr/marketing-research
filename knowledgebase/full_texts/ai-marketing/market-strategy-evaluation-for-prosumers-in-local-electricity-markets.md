---
title: Market Strategy Evaluation for Prosumers in Local Electricity Markets
url: https://arxiv.org/abs/2607.18272
category: ai-marketing
subcategory: empirical
date: 2026-06
venue: ''
authors:
- Lukas Peter Wagner
- Raoul Bisson
- Felix Gehlhoff
source: arxiv
pdf_url: https://arxiv.org/pdf/2607.18272
pages: 8
chars: 44559
fetched_at: '2026-11-08T13:00:44+00:00'
kb_version: 1
---

# Market Strategy Evaluation for Prosumers in Local Electricity Markets

Market Strategy Evaluation for Prosumers in Local
Electricity Markets
Lukas P. Wagner, Raoul Bisson, and Felix Gehlhoff
Institute of Automation Technology,
Helmut Schmidt University, Hamburg, Germany
{lukas.wagner, raoul.bisson, felix.gehlhoff}@hsu.hamburg
Abstract—Prosumers equipped with distributed generation
and flexible loads form autonomous cyber-physical energy sys-
tems that control local resources and participate in local energy
markets with minimal human intervention. This work develops
and evaluates an agent-based simulation platform in which
agents, representing prosumer households with photovoltaic
systems, battery storage systems, electric vehicles, and heat
pumps, participate in a uniform-price double-sided call auction.
The effect of individual bidding strategies on community-level
efficiency and prosumer-level financial outcomes is incompletely
understood, particularly when prosumers with heterogeneous
portfolios interact in one market. Four market strategies of
increasing complexity are compared: a zero-intelligence con-
strained baseline, a boundary-price strategy, an extended storage
cascade, and a market-adaptive pricing strategy. The simulation
is conducted on a community of 33 prosumers at 15-minute
resolution, spanning summer, winter, and spring to characterize
seasonal variation. Results show that rule-based resource con-
trol substantially reduces community energy expenditure: the
extended storage cascade achieves a total cost of 39.06 EUR
compared to 62.38 EUR under the zero-intelligence baseline, a
reduction of 37.4 %. The market-adaptive strategy yields the
highest aggregate community financial gain through local energy
market participation (14.40 EUR vs. 10.28 EUR for the baseline, a
gain of 40.1 %) under summer conditions. Strategy effectiveness
depends on both portfolio composition and seasonal supply
conditions, requiring joint evaluation of resource control and
pricing decisions.
Index Terms—local electricity market, bidding strategies,
agent-based simulation, strategy evaluation
I. INTRODUCTION
The decarbonization of residential energy supply drives
rapid expansion of distributed generation and flexible con-
sumption at the low-voltage level. Rooftop photovoltaic (PV)
systems, battery energy storage systems (BESSs), electric
vehicles (EVs), and heat pumps (HPs) transform a growing
number of households into prosumers that independently con-
trol local energy resources, respond to market signals, and
exchange energy with minimal human intervention. BESSs
and EVs are key enablers of PV self-consumption [1], as they
introduce additional temporal flexibility for shifting locally
generated energy.
This research in the project OptiFlex was funded by dtec.bw (Digitalization
and Technology Research Center of the Bundeswehr). dtec.bw is funded
by the European Union (NextGenerationEU). This work was also supported
by the Federal Ministry for Economic Affairs and Climate Action and the
Projektträger Jülich GmbH within the project InterPhaSe (FKZ 03EI6139A).
In Germany alone, more than 3.7 million residential PV
installations were registered by 2023, with shares of electrified
heating and mobility rising in parallel [2]. Without incentive-
compatible coordination mechanisms, surplus generation is
curtailed or exported at low feed-in tariffs while neighbors
simultaneously import energy at the substantially higher re-
tail tariff [2]. Local electricity markets (LEMs) address this
misalignment by enabling direct energy exchange within a
geographically bounded community, typically a low-voltage
feeder or neighborhood, at negotiated prices between pro-
sumers [3]. Survey work by Mengelkamp et al. [3] identifies
double-sided auctions as the dominant clearing mechanism and
agent-based simulation as the primary methodological tool for
LEM analysis: in double-sided auctions, software agents are
well suited for representing prosumers in this context. Rein-
pold et al. [4] identify autonomy, external resource control,
and sociability as defining agent properties, which correspond
directly to a prosumer’s need to independently control local
resources while interacting with an LEM.
This work is embedded in the InterPhaSe project, which
investigates an integrated platform combining an LEM with
market-based distribution grid congestion management. Prior
contributions addressed decentralized energy dispatch and
scalable agent-based control [5] as well as identity-secured
market access [2]. The present work addresses the prosumer
level: given a specific resource portfolio, which market strat-
egy should a prosumer adopt to maximize its financial benefit
while contributing to community efficiency?
This question involves two intertwined sub-problems. The
resource control problem asks how flexible resources should
be dispatched within each interval to minimize net energy
cost. The bid pricing problem asks at what price the agent
should submit its sell offer or buy request to the auction.
These decisions interact: local storage reduces the quantity
available for market sale, thereby affecting price discovery,
while the achieved clearing price determines the economic
value of stored energy and thus the optimal dispatch rule.
Compounding this interaction is portfolio heterogeneity. A
prosumer combining a PV system with a BESS and an EV can
absorb surplus along two independent storage pathways and
has multiple options for intra-day arbitrage, whereas a PV-only
prosumer is limited to direct market sales, and a pure consumer
acts exclusively as a buyer. This motivates a comparative
evaluation that spans heterogeneous portfolio classes rather
arXiv:2607.18272v1  [cs.GT]  12 Jun 2026

than assuming a homogeneous prosumer population.
Evaluating such prosumers requires simulation environ-
ments that faithfully reproduce both resource dynamics and the
market interaction layer. Existing simulation studies compare
strategies for homogeneous populations or evaluate market
mechanisms without distinguishing the portfolio dimension.
A joint simulation-based evaluation of resource control and
bid pricing strategies across heterogeneous portfolio classes,
covering both community-level cost and per-portfolio financial
gain, is absent from the literature.
Three research questions (RQs) guide this work:
RQ1. To what extent do resource control and bid pricing rules
each contribute to reducing community energy cost?
RQ2. How does an extended storage cascade, a sequential
dispatch policy prioritizing BESS and then EV storage
(defined in Sec. IV), incorporating the EV battery affect
autarky across portfolio classes?
RQ3. How does market-adaptive pricing redistribute financial
gains, and how sensitive is this effect to community
composition?
The contributions of this work are:
(i) An agent-based LEM simulation platform implemented
with Java Agent Development Framework (JADE) [6],
featuring configurable, portfolio-specific resource models
and bidding strategies.
(ii) A strategy framework that independently varies resource
control and bid pricing, enabling targeted attribution of
each dimension’s contribution to community cost and
financial gain.
(iii) A multi-key performance indicator (KPI) evaluation
across five heterogeneous portfolio classes and three
seasonal scenarios, quantifying community cost, autarky,
market participation, and per-portfolio financial out-
comes.
The remainder of this paper is organized as follows. Sec. II
surveys related work and identifies the research gap. Sec. III
describes the agent architecture, resource models, and mar-
ket mechanism. Sec. IV defines the four strategies. Sec. V
presents the simulation setup and evaluation results. Sec. VI
summarizes findings and outlines future work.
II. RELATEDWORK
This section reviews related work on agent-based LEM sim-
ulation and prosumer bidding strategies, structured around four
requirements (Rs) motivated by the joint resource-control and
bid-pricing problem introduced in Sec. I. These requirements
jointly enable a structured evaluation of market strategies,
including the attribution of system-level effects to resource
control and pricing decisions as well as the analysis of
portfolio-dependent outcomes:
R1. Agent-based prosumer modeling with portfolio-specific
resource configurations, because strategy effectiveness
depends on asset configuration [7].
R2. A uniform-price double-sided call auction as clearing
mechanism, as this is the dominant design in the LEM
literature and determines the incentive structure under
study [3].
R3. Multiple strategies with independently configurable and
analyzable resource control and bid pricing dimensions,
to isolate the contribution of each to observed outcomes
[8].
R4. Quantitative KPI evaluation covering economic effi-
ciency, autarky, and local market participation across
multiple seasonal scenarios, enabling objective and re-
producible strategy comparison [2].
Kilthau et al. [2] present an agent-based platform for peer-
to-peer energy trading combined with congestion management,
evaluating prosumer agents with self-consumption optimiza-
tion and forecast-based pricing across a 16-node distribution
grid (R1). A single strategy variant is implemented without
a central auction mechanism, so neither the clearing design
(R2) nor a comparison of independently configured strategies
(R3) is addressed. Quantitative metrics are reported but not
disaggregated by portfolio class or season (R4 partial).
Kilthau et al. [5] develop a decentralized two-agent archi-
tecture per household for simultaneous energy dispatch and
congestion management on the IEEE 33-bus network (R1).
No central auction or strategy comparison is performed (R2,
R3 absent), and evaluation covers a single scenario without
portfolio-class or seasonal breakdown (R4 partial).
Mengelkamp et al. [7] simulate 100 households in a merit-
order LEM and compare reinforcement learning strategies
with rule-based variants, reporting outcomes separately for
consumer and prosumer types (R2, R4). All households rely
on a shared community storage rather than individual storage
configurations, limiting portfolio heterogeneity (R1 partial).
Furthermore, resource control and bid pricing are not inde-
pendently varied, preventing attribution of observed effects to
either dimension (R3 partial).
El-Baz et al. [9] design resource-type-specific bidding
strategies for a uniform-price double-sided auction covering
PV, HP, EV, and BESS, reporting per-resource-class cost
reductions (R2, R4). Since all households carry the same
full resource set, portfolio-class effects cannot be isolated
(R1 partial), and resource control and bid pricing are not
independently configurable (R3 partial).
Schölzel et al. [8] compare zero-intelligence, reinforcement
learning, and device-oriented strategies in a uniform-price
auction with quantitative evaluation (R2, R4). All households
are identically equipped, precluding portfolio differentiation
(R1 absent), and resource dispatch and bid pricing are not
varied independently (R3 partial).
Bose et al. [10] and Okwuibe et al. [11] apply reinforcement
learning in LEMs and report autarky and cost KPIs (R2).
Agent types are distinguished as prosumer or consumer rather
than by specific resource portfolios (R1 partial), and both ap-
proaches optimize a single combined policy without separating
resource control from bid pricing, limiting interpretability of
strategy effects (R3 partial). Local market participation metrics
are not the primary evaluation target (R4 partial).

Table I
COVERAGE OF KEY REQUIREMENTS IN RELATED WORK.
Reference R1 R2 R3 R4
Kilthau et al. [2]
Kilthau et al. [5]
Mengelkamp et al. [7]
El-Baz et al. [9]
Schölzel et al. [8]
Bose et al. [10]
Okwuibe et al. [11]
satisfied partial not addressed
As shown in Tab. I, no existing work simultaneously sat-
isfies all four requirements. Existing studies either evaluate
market strategies under homogeneous agent assumptions or
implicitly couple resource control and bid pricing within a
single policy. As a result, the contribution of each dimension
to system-level performance cannot be isolated.
In particular, no study combines a uniform-price call auc-
tion (R2) with independently configurable resource control
and pricing strategies (R3) across a heterogeneous prosumer
population (R1). No study reports KPI results disaggregated
by portfolio class (R4), leaving the portfolio-dependent distri-
bution of gains and the efficiency-benefit trade-off uncharac-
terized.
III. SYSTEMMODEL, MARKETMECHANISM,AND
PERFORMANCEMETRICS
This section describes the simulation platform: the multi-
agent architecture and interaction protocol (Sec. III-A), the
resource models of each prosumer (Sec. III-B), the uniform-
price call auction used for market clearing (Sec. III-C), and
the KPIs used for strategy evaluation (Sec. III-D).
A. Agent Architecture
The simulation is implemented as a multi-agent sys-
tem using JADE [6], a FIPA-compliant platform for asyn-
chronous agent communication language messaging. The plat-
form instantiates two agent types: 33HouseholdAgents,
each representing one prosumer household, and a single
AuctionAgentthat coordinates the market. The per-slot
interaction follows the FIPA Contract Net Interaction Protocol
[12] as a communication and coordination layer, while the
allocation decision is realized through a centralized uniform-
price auction (see Sec. III-C). Fig. 1 shows the message
exchange for one slot.
Each of the𝑇=96slots ofΔ𝑡=15min follows a syn-
chronous round opened by theAuctionAgentbroadcasting
a call for proposals (CFP). EachHouseholdAgentresponds
by computing its net energy balance𝐸 net from local generation
and consumption (Eq. 1), then dispatching BESS and EV
storage according to its assigned strategy. If the residual after
storage dispatch satisfies|𝐸 net| ≥𝜀(𝜀=0.001kWh, the
minimum tradeable quantity), the agent determines a bid price
and submits a proposal (PROPOSE) carrying bid type (sell or
HouseholdAgent(×33) AuctionAgent
loop[𝑡=0,...,95] CFP𝑡
𝐸net←𝐸 PV(𝑡)−𝐸 base(𝑡)−𝐸 HP(𝑡)(see Eq. 1)
dispatchStorage(𝐸 net)
computeBidPrice(𝑡𝑦𝑝𝑒, 𝑡)
PROPOSE/REFUSE
runAuction(𝑏𝑖𝑑𝑠, 𝑡)
ACCEPT-PROPOSAL/REJECT-PROPOSAL
updateStrategy(𝑟𝑒𝑠𝑢𝑙𝑡)
update SOC BESS, SOC EV
INFORM
Figure 1. FIPA Contract Net interaction protocol for one slot𝑡. Activation
boxes indicate local processing steps.
buy), quantity, and price. If storage dispatch absorbs the full
surplus or covers the full deficit within the slot,|𝐸 net|falls
below𝜀and the agent sends a refusal (REFUSE). This is a
per-slot condition and does not imply autarky: the same agent
may still import or export in other slots, or fail to find a match
and fall back to the grid tariff.
After collecting all proposals, theAuctionAgenteval-
uates them jointly via merit-order clearing (see Sec. III-C)
and notifies every agent: matched prosumers receive
ACCEPT-PROPOSALwith clearing price and traded quantity;
unmatched prosumers receiveREJECT-PROPOSALtogether
with the slot clearing price, which can be used for strategy
adaptation in the following slot. EachHouseholdAgent
then adjusts its internal strategy state, updates the state of
charge (SOC) of BESS (SOC BESS) and EV (SOC EV), and
sendsINFORMto theAuctionAgent.
TheAuctionAgentadvances to slot𝑡+1only after
allINFORMmessages have been received. This synchronous-
round structure removes asynchronous timing as a source of
KPI differences. Because all four strategies are evaluated on
the same community and the same input profiles, the remain-
ing differences reflect the strategy rather than the scenario.
B. Resource Models
Each prosumer owns a subset of four resource types. The net
energy balance determining surplus or deficit before storage
dispatch is
𝐸net(𝑡)=𝐸 PV(𝑡)−𝐸 base(𝑡)−𝐸 HP(𝑡),(1)
where𝐸 PV is PV generation,𝐸 base is inflexible base load, and
𝐸HP is HP consumption. BESS and EV dispatch are strategy-
controlled.
Photovoltaics.PV generation per interval follows
𝐸PV(𝑡)=𝑃 peak·𝐺(𝑡)·Δ𝑡,(2)

where𝐺(𝑡)∈[0,1]is the normalized irradiance for Hamburg
(2019) [13] and𝑃 peak=5kWp per prosumer.
Base load and heat pump.The H0 residential standard load
profile [14] is applied, scaled to 3 000 kWh/a. The HP uses
the WPE standard profile with the VDN TMZ block-heating
method, a standardized German heat-pump load profile [15],
scaled to 4 000 kWh/a. HP operation is treated as non-flexible;
demand-side management of HPs is addressed in [16].
Battery energy storage system.The SOC evolves as
SOC(𝑡)=SOC(𝑡−1)+ 𝜂ch𝑃ch(𝑡)Δ𝑡 𝐶bat − 𝑃dis(𝑡)Δ𝑡 𝜂dis𝐶bat ,(3)
with capacity𝐶 bat =10kWh, maximum power𝑃 max =5kW,
efficiency𝜂 ch=𝜂 dis=0.95, and SOC bounds[0.10,0.90]to
protect cycle life.
Electric vehicle.The same SOC model (Eq. 3) applies with
𝐶bat =60kWh and𝑃 max =11kW. Availability flag𝑎(𝑡) ∈
{0,1}encodes a commuter pattern absent from 07:00 to 17:00.
Daily energy demand is 11.7 kWh (approximately 65 km/day)
[17].
C. Market Clearing Mechanism
Market clearing employs a uniform-price double-sided call
auction once per interval [18]. Sell orders are sorted by ascend-
ing price and buy orders by descending price (merit order). The
lists are matched pairwise from the top, each step trading the
smaller of the two remaining quantities and advancing past any
filled order, until the first pair with𝑝 ask> 𝑝bid. The marginal
pair is the last pair that traded, and the uniform clearing price
is the midpoint of its ask and bid,
𝑝clear(𝑡)= 1 2 𝑝ask,marginal(𝑡)+𝑝 bid,marginal(𝑡) .(4)
All matched volume in interval𝑡settles at𝑝 clear(𝑡). A
price corridor[𝑝 min, 𝑝max]=[0.08,0.36]EUR/kWh bounds
all submitted prices, where𝑝 min equals the statutory feed-
in tariff for small PV installations and𝑝 max the retail tariff
for residential customers [19]. Unmatched sell volume is
exported to the external grid at𝑝 min; unmatched buy volume
is imported at𝑝 max. Every LEM transaction settled within
the corridor produces a bilateral improvement relative to the
grid-tariff alternative, providing the fundamental incentive for
participation. The corridor reflects only the feed-in to retail
spread. Taxes, network charges, levies, and transaction costs
are not modeled. The market mechanism is implemented
as a centralized service within theAuctionAgent(see
Sec. III-A).
D. Performance Metrics
Nine KPIs characterize strategy outcomes:
•Autarky degree (AD): share of consumption covered locally
without grid import [20].
•Self-consumption rate (SCR): fraction of PV generation
consumed locally [20].
•LEM quota: share of total energy volume settled within the
LEM [21].
•𝐶 total: aggregate net grid payments over the simulated day.
•𝑝 clear: uniform settlement price per interval (Eq. 4).
•Financial gain through participation (FGP): cost saving
relative to a no-market counterfactual, in which all surplus
PV is exported at𝑝 min and all deficit is covered by grid
import at𝑝 max, summed over all community members [21].
•Match rate (MR): fraction of submitted bid volume cleared
within the LEM.
•BESS cycles: storage utilization in equivalent full cycles per
day.
•LEM volume: total energy quantity traded per simulated day.
IV. MARKETSTRATEGIES
The four strategies are defined along two dimensions: re-
source control and bid pricing.
ZIC (zero-intelligence constrained).Bid prices are drawn
uniformly at random from the price corridor, following the
ZIC formulation of Gode and Sunder [18]. Device control
applies a basic cascade: PV surplus charges the BESS up to
its upper SOC bound. Remaining surplus is offered to the
market as a sell bid. On a deficit, the BESS discharges first.
If the BESS is exhausted or at its lower SOC bound, the
agent submits a buy bid to the market. If no match is found,
the residual is settled with the grid. ZIC provides a minimal-
intelligence reference that isolates the contribution of market
structure from any strategic intent, and its near-competitive
efficiency in homogeneous populations (established by Gode
and Sunder [18]) makes it a meaningful performance floor
rather than a trivially weak baseline.
EVB (edge-value bidding).Sell bids are fixed at𝑝 min and
buy bids at𝑝 max. Every submitted pair satisfies the matching
condition, and clearing settles at𝑝 clear =0.22EUR/kWh per
Eq. 4. This guarantees full market participation but suppresses
price discovery. Device control is identical to ZIC, so EVB
versus ZIC isolates the bid pricing effect.
ESC (extended storage cascade).The resource control di-
mension is extended by adding a direct charge path from
surplus PV to the EV once the stationary BESS is full. When
surplusΔ𝐸(𝑡)>0remains after BESS saturation and the
vehicle is available, the EV receives
𝑃ev,ch(𝑡)=min

Δ𝐸(𝑡)
Δ𝑡 , 𝑃ev,max𝑎(𝑡), (SOCmax−SOCev)𝐶 ev 𝜂chΔ𝑡

.(5)
AnyΔ𝐸(𝑡)remaining after both storage paths are saturated
is offered to the market. Bid pricing follows the ZIP (zero-
intelligence plus) principle of Cliff [22]: each agent adjusts
its price stepwise byΔ𝑝=0.02EUR/kWh based on the
previous interval’s clearing outcome. Sellers lower their ask
when the previous clearing price fell below their ask; buyers
raise their bid when it exceeded their bid. Ask prices thereby
converge toward𝑝 min during high-supply intervals and rise
toward scarcity levels otherwise. ESC applies this mechanism
uniformly with a sell floor of0.09EUR/kWh for all portfolio
classes. The EVB-to-ESC step therefore combines resource
control and pricing changes; the ESC-to-MA step isolates the
portfolio-specific resource dispatch logic.
MA (market-adaptive strategy).Two portfolio-specific dis-
patch rules extend the resource control of ESC. For prosumers

(PV with BESS, PVB), BESS discharge for market sale is
inhibited when the most recent clearing price, observed in the
previous interval, falls below
𝑝dis,min= 𝑝min 𝜂ch·𝜂 dis = 0.08EUR/kWh 0.952 ≈0.089EUR/kWh, (6)
under which selling stored energy yields less revenue than
a direct grid feed-in at𝑝 min, producing a net loss over the
charge-discharge round trip. For PEB prosumers (PV with
both BESS and EV), a dynamic SOC reserve protects the
anticipated remaining base load and HP demand until end-
of-day, shrinking slot by slot as remaining demand decreases
and progressively freeing storage capacity for arbitrage.
Bid pricing uses the same ZIP mechanism as ESC, but
with portfolio-differentiated sell floors:0.089EUR/kWh for
prosumers with a BESS and𝑝 min=0.08EUR/kWh for those
without.
Tab. II summarizes the four strategies along their two
dimensions.
Table II
OVERVIEW OF THE FOUR MARKET STRATEGIES ACROSS THE RESOURCE
CONTROL AND BID PRICING DIMENSIONS.
Strategy Device control Price formation
ZIC Basic cascade (BESS priority) Random in[𝑝 min, 𝑝max]
EVB Basic cascade (BESS priority) Boundary prices
ESC Extended cascade (EV priority
+ BESS→EV discharge)
Adaptive (ZIP-like)
MA Portfolio-specific reserve logic,
price-controlled discharge
Adaptive (ZIP-like)
V. EVALUATION
A. Setup
The community consists of 33 prosumers distributed across
an IEEE 33-bus network topology. Network power flow con-
straints are not enforced. The topology serves as a spatial map-
ping for prosumer assignment, and congestion management is
addressed in prior work, such as Kilthau et al. [2]. Portfolio
assignment follows penetration rates drawn from Kilthau et al.
[5]: 67 % of prosumers own PV, 65 % own an EV, and 80 %
own an HP. The BESS rate of 50 % of PV prosumers is an
assumption of this work, chosen to generate a diverse mix
of classes. All classes include an HP and base load. Tab. III
lists the five resulting portfolio classes. All four strategies are
evaluated independently on the same community composition
using Hamburg irradiance profiles. The simulation code is
publicly available.1
B. Community-Level Strategy Comparison
Fig. 2 summarizes the primary community-level results
(metric definitions in Sec. III-D).
Autarky, self-consumption, and LEM quota (Fig. 2a).ZIC
and EVB yield identical autarky degree (58.5 %) and self-
consumption rate (85.8 %), confirming that bid pricing alone
1https://github.com/lukas-wagner/Market_Strategy_Evaluation
Table III
PROSUMER PORTFOLIO CLASSES WITH RESOURCE COMPOSITION.
Class Count PV BESS EV
PEB 8✓ ✓ ✓
PVB 3✓ ✓−
PVEV 6✓−✓
PV only 5✓− −
Consumer 11− − −
ZIC EVB ESC MA
0
20
40
60
80
100
(%)
AD SCR LQ
(a) Autarky (AD), self-consumption
(SCR) & LEM quota (LQ)
ZIC EVB ESC MA
0
20
40
60
𝐶total / FGP (EUR)
𝐶total FGP
(b) Cost & financial gain (FGP)
Figure 2. Community-level results for the four strategies.
does not affect physical energy coverage. ESC raises both
metrics substantially (autarky to 73.6 %, self-consumption to
94.8 %) by routing surplus PV into EV storage before offering
the remainder to the market. MA follows at 70.8 % and 94.3 %:
the dynamic SOC reserve trades a modest autarky penalty for
price-driven dispatch flexibility. The LEM quota rises from
8.6 % (ZIC) to 12.6 % (MA), with the step from ZIC to EVB
(8.6 to 10.7 %) reflecting guaranteed bid matching, and the
further increase under ESC and MA driven by adaptive pricing
expanding the set of cleared pairs.
Cost and financial gain (Fig. 2b).Regarding RQ1, pricing
strategy has a modest isolated effect: switching from random
to deterministic boundary prices (ZIC to EVB) reduces𝐶 total
by only2.46EUR (3.9 %), confirming that price anchoring
alone yields limited cost reduction. The EVB-to-ESC step
combines the extended storage cascade with adaptive pricing
and achieves the single largest improvement:𝐶 total drops to
39.06EUR, a combined reduction of20.86EUR (34.8 %).
Because this step changes both the storage cascade and the
pricing rule, it quantifies the combined ESC design, not the ex-
tended cascade in isolation. Only the ZIC-to-EVB step isolates
a single dimension, pricing. Switching from the uniform ESC
cascade to the portfolio-specific resource dispatch logic of MA
provides a further0.85EUR (2.2 %) saving. Combined, the
full upgrade from ZIC to MA reduces community expenditure
by24.17EUR (38.8 %) relative to ZIC. Community financial
gain through LEM participation increases in parallel: FGP
rises from10.28EUR (ZIC) to14.40EUR (MA), a total im-

Table IV
ADOF THEPEBPORTFOLIO CLASS VS.THE COMMUNITY AVERAGE FOR
ALL FOUR STRATEGIES(SUMMER DAY). DIFFERENCES IN PERCENTAGE
POINTS.
ZIC EVB ESC MA
PEB class AD (%) 50.6 50.6 92.2 84.4
Community average AD (%) 58.5 58.5 73.6 70.8
Difference (pp)−7.9−7.9+18.6+13.6
provement of4.12EUR (40.1 %). Storage utilization, market
volume, clearing price, and match rate are discussed in the
following subsections.
C. Storage Utilization, Market Volume, and Portfolio Effects
Fig. 3 shows battery utilization (Fig. 3a), the primary driver
of the cost reductions in Fig. 2b, and total traded market
volume (Fig. 3b), which reflects the degree to which strategies
activate the LEM as an exchange channel.
ZIC EVB ESC MA
0
0.25
0.5
0.75
1
Eq. cycles / day
(a) BESS utilisation
ZIC EVB ESC MA
0
15
30
45
Energy (kWh) (b) LEM volume
Figure 3. BESS equivalent full cycles per day (left) and total energy volume
settled within the LEM (right).
RQ2 asks how the EV battery integration affects autarky
across portfolio classes. The answer is class-specific: the
largest benefit accrues to prosumers that possess both a BESS
and an EV (PEB class). Tab. IV shows that PEB autarky rises
from 50.6 % under ZIC and EVB to 92.2 % under ESC, a
gain of 41.6 percentage points. The mechanism is the fourfold
increase in BESS equivalent full cycles (Fig. 3a, 0.21 to 0.89
per day): by routing surplus PV into the EV battery once
the BESS is full (Eq. 5), and subsequently discharging the
BESS into the EV when the SOC reserve permits, ESC fills
both the 10 kWh stationary and the 60 kWh mobile storage,
covering evening demand without grid import. Prosumers with
only a PV and an EV (PVEV) see a moderate improvement,
reaching 62–71 % autarky, since the EV battery alone provides
less intra-day flexibility without a stationary buffer. Prosumers
without an EV (PVB) gain no benefit from the cascade
extension, as the EV charge path does not apply. Prosumers
with only PV remain near 45 % regardless of strategy, with no
storage to shift surplus across time.
MA reaches only 84.4 % autarky for PEB, 7.9 percentage
points below ESC: the dynamic reserve logic (Eq. 6) retains
BESS capacity for evening baseload coverage, preventing full
EV charging. The gap between PEB and the community
average grows from−7.9percentage points under ZIC to
+18.6points under ESC, confirming that portfolio class and
strategy are jointly determining factors that cannot be assessed
independently.
Despite the higher storage utilization, market volume is
identical for EVB and ESC at 45.5 kWh (Fig. 3b): the extended
cascade absorbs more energy locally rather than offering it
to the market. MA reaches the highest traded volume of
51.4 kWh, as adaptive pricing attracts additional matching bids
from both sides.
All portfolio classes retain a positive FGP under every
strategy: market participation always improves on the no-
market counterfactual. However, the distribution of gains shifts
under MA. All PV-owning classes receive lower FGP under
MA than under EVB, because the lower clearing price reduces
per-unit sell-side revenue: PV only by0.23EUR, PVEV by
0.12EUR, PEB by0.09EUR, and PVB by0.07EUR per
prosumer. Pure consumers are the sole net beneficiaries of
adaptive pricing, gaining an additional0.41EUR per prosumer
under MA relative to EVB. The portfolio-level FGP spread
widens from0.47EUR under EVB to0.97EUR under MA,
indicating that higher aggregate community gain comes at the
cost of increased distributional inequality. Under adaptive pric-
ing, sellers accept lower ask prices to secure a match, which
compresses their per-unit revenue while buyers clear at a more
favorable price; the pricing rule therefore transfers value from
prosumers with generation assets to pure consumers rather
than distributing gains uniformly.
D. Clearing Price Dynamics and Value Distribution
Fig. 4 summarizes the aggregate pricing outcomes; the
intraday dynamics are shown in Fig. 5.
ZIC EVB ESC MA
0.00
0.08
0.16
0.22
A vg. clearing price (EUR/kWh)
(a) Avg. clearing price
ZIC EVB ESC MA
0
10
20
30
Match rate (%) (b) Match rate
Figure 4. V olume-weighted average clearing price (left) and match rate (right)
for the four strategies.
EVB serves as the deterministic reference: boundary
prices fix the clearing price at0.22EUR/kWh regardless
of supply-demand balance. ZIC already undercuts this level

00:00 06:00 12:00 18:00 24:00
0.00
0.08
0.22
0.36
𝑝min
𝑝max
Time of day (h)
Clearing price
(EUR/kWh)
ZIC EVB ESC MA
Figure 5. Intraday clearing price per 15-min slot; only slots with at least one
matched trade are shown (gaps indicate no clearing). ESC (dotted) and MA
(solid) are plotted with overlapping styles to keep both visible where prices
coincide.
(0.14EUR/kWh, Fig. 4a), but not through strategic intent:
random bids occasionally fall well below the competitive level,
matching at prices unfavorable for sellers. This is the alloca-
tively efficient but individually suboptimal outcome identified
by Gode and Sunder [18]. Adaptive pricing (ESC and MA)
achieves lower prices through deliberate convergence: ESC
reaches0.164EUR/kWh and MA0.127EUR/kWh, a reduc-
tion of 42.3 % relative to EVB. ESC’s match rate (24.6 %)
falls marginally below EVB (25.2 %): the extended storage
cascade absorbs more surplus locally, reducing the volume
of sell bids submitted, while the adaptive pricing mechanism
requires several intervals to converge. During this phase, ask
prices may temporarily exceed buy bids and prevent clearing.
MA reverses this effect and raises the match rate to27.9 %
(Fig. 4b): once prices have converged, the lower ask floor
attracts buy bids that could not match at the EVB boundary,
expanding the set of feasible bid pairs.
Fig. 5 reveals the intraday mechanism behind the aggregate
numbers. ZIC produces a scattered price profile across the day:
random sell bids occasionally fall well below what a rational
seller would accept, yielding clearing prices that are irregular
and often low (volume-weighted average0.14EUR/kWh).
EVB is flat at0.22EUR/kWh across all active slots: the
boundary-priced bids always resolve to the midpoint of the
corridor, independent of supply-demand balance. ESC and
MA share an identical morning profile (0.29–0.32EUR/kWh,
07:00–10:00) when PV generation is ramping and seller supply
is thin. As irradiance peaks, both strategies adapt ask prices
downward: ESC stabilizes near0.095EUR/kWh (the round-
trip efficiency sell floor), while MA converges to𝑝 min =
0.08EUR/kWh for non-BESS sellers whose floor is lower. The
critical difference is trading duration. MA remains active until
23:45 (64 slots vs. 51 for ESC), because price-controlled BESS
discharge in PVB prosumers generates sell volume in post-
sunset hours. Sellers in these slots face demand-side scarcity
and can command prices up to𝑝 max; buyers simultaneously
avoid the grid tariff. This evening extension arises from MA’s
portfolio-specific resource dispatch logic for PVB prosumers,
which enables price-controlled BESS discharge that ESC’s
uniform cascade does not provide, and explains the1.66EUR
FGP advantage of MA over ESC (14.40vs.12.74EUR,
Fig. 2b).
The clearing price and the traded volume act through two
separate channels. At a fixed volume the clearing price only
splits the local-trading savings between buyers and sellers,
while the strategies also change the match rate and LEM
volume, and thus how much saving exists to split. When a
kilowatt-hour is traded locally, the buyer pays less than the
grid retail tariff and the seller receives more than the feed-in
tariff; however, a lower clearing price increases the buyer’s
saving at the expense of the seller’s margin, so these effects
offset at community level. Under MA, lower clearing prices
shift0.41EUR per prosumer from sellers to buyers compared
to EVB, consistent with Nicolaisen et al. [23]. Despite this
redistribution, the community’s total FGP under MA rises by
1.67EUR compared to EVB, because more energy is traded
locally rather than settled at regulated grid tariffs.
E. Seasonal Dependency
The summer evaluation in Sec. V-B represents conditions
favorable to LEM activity: high PV generation creates ample
surplus for trading, and the community contains both net
sellers and net buyers in most intervals. A winter evaluation
(Hamburg, January) reveals a qualitatively different regime.
With irradiance at roughly one-sixth of summer peak val-
ues, PV generation is largely consumed immediately at the
generating prosumer, and the self-consumption rate reaches
95.1 % under all strategies. Surplus available for LEM trading
is minimal: LEM quota drops to 1.4 % and community cost
is identical for EVB and MA at367.05EUR, confirming that
the pricing mechanism is irrelevant when there is no surplus to
trade. Under MA, the clearing price rises to0.35EUR/kWh,
approaching𝑝 max, because adaptive buyers compete for the
scarce PV supply rather than sellers competing to sell. The
LEM becomes effectively inactive in winter, not because the
mechanism fails, but because the physical supply-demand
balance produces no meaningful surplus: every kilowatt-hour
of PV generation is already cheaper than a grid alternative and
prosumers consume it locally regardless of market signals.
Spring conditions (Hamburg, April) represent an intermedi-
ate regime. Moderate PV generation combined with residual
space-heating demand creates a supply-demand balance that
is, in some respects, more favorable for intra-community
trading than peak summer: sufficient surplus exists to generate
competitive sell bids, while elevated consumption from heating
loads maintains buy-side demand at a level that absorbs most
of the available surplus. Under EVB, LEM quota reaches
17.4 % in April, notably above the 10.7 % observed in July.
This counter-intuitive result reflects that peak summer PV
surpluses can exceed the LEM’s absorption capacity when
all generators simultaneously produce more than the com-
munity can consume, causing excess export to the grid even
with active market participation. A key reversal occurs for
community FGP: in April, EVB achieves23.59EUR while
MA achieves only22.45EUR (−1.14EUR), the opposite of
the summer relationship. With moderate PV penetration, sell-

side competition is weaker, and sellers have no incentive
to adapt their ask prices downward; adaptive pricing thus
fails to expand the cleared volume sufficiently to offset the
lower per-unit revenue. These seasonal patterns imply that
the optimal strategy for a prosumer varies across seasons:
boundary prices are better suited to spring conditions while
adaptive pricing delivers greater advantage in summer when
supply-side competition among sellers is most intense.
VI. CONCLUSION
Prosumers participating in LEMs face two intertwined de-
cisions: how to dispatch flexible resources locally and at what
price to bid into the market. Evaluating these dimensions
jointly and in isolation is essential for understanding their
respective contributions to community cost and financial gain.
This work presented an agent-based LEM simulation with
33 heterogeneous prosumer agents participating in a uniform-
price call auction under four strategies of increasing complex-
ity, evaluated across summer, winter, and spring conditions.
Resource control proved to be the primary lever: the extended
storage cascade reduced community cost by 37.4 % relative to
the zero-intelligence baseline, while market-adaptive pricing
raised community financial gain through LEM participation
by 40.1 %. Autarky improvements were confined to prosumers
combining PV with BESSs and EVs, demonstrating that strat-
egy effectiveness is inseparable from portfolio composition.
Adaptive pricing redistributes value from net sellers to net buy-
ers through lower clearing prices, whereas boundary pricing
offers composition-independent stability at the cost of lower
aggregate gain. Seasonal analysis showed that this advantage is
not universal: in spring, weaker sell-side competition renders
adaptive price adaptation ineffective, and boundary pricing
achieves higher community financial gain. In winter, minimal
PV surplus makes the pricing mechanism largely irrelevant,
and strategy differences vanish. The optimal choice therefore
depends on the season, shown directly, and on community
composition to the extent indicated by the portfolio-class
differences, motivating portfolio- and season-aware strategy
selection, with a composition sensitivity analysis, as a direc-
tion for future work.
Several limitations apply. The simulation assumes perfect
information with no forecast uncertainty, identical PV sizes
across prosumers, deterministic EV availability, and a single
fixed community composition, so the community-composition
dependence is shown only through portfolio-class differences
within that community. All agents use the same strategy
per run, so the results characterize homogeneous strategy
deployment, not the equilibrium under independently chosen
strategies. Mixed-strategy scenarios are not evaluated. ZIC
draws random bids, so its reported results are a single realiza-
tion rather than a mean over repeated draws, and it is the only
stochastic strategy. BESS degradation costs are not modeled:
the fourfold increase in cycling under the extended cascade
(0.21 to 0.89 equivalent full cycles per day, roughly 77 to 325
cycles per year) would narrow its economic advantage once
aging is accounted for. Network constraints are not enforced.
Future work will pursue field deployment to validate the
simulation results under real forecast uncertainty and dynamic
tariff structures. Investigating heterogeneous strategy popu-
lations would reveal competitive dynamics and equilibrium
properties of the market. Additionally, the observed portfolio
and seasonal dependency motivates the development of adap-
tive mechanisms that select or parameterize strategies based
on community composition and prevailing supply conditions.
REFERENCES
[1] R. Luthander, J. Widén, D. Nilsson, and J. Palm, “Photovoltaic self-consumption
in buildings: A review,”Applied Energy, vol. 142, pp. 80–94, 2015.
[2] M. Kilthau, M. Asman, A. Karmann, G. Suriyamoorthyet al., “Integrating peer-
to-peer energy trading and flexibility market with self-sovereign identity for
decentralized energy dispatch and congestion management,”IEEE Access, vol. 11,
pp. 145 395–145 420, 2023.
[3] E. Mengelkamp, J. Diesing, and C. Weinhardt, “Tracing local energy markets: A
literature review,”it – Information Technology, vol. 61, no. 2-3, pp. 101–110, 2019.
[4] L. M. Reinpold, L. P. Wagner, F. Gehlhoff, M. Ramonatet al., “Systematic
comparison of software agents and digital twins: differences, similarities, and
synergies in industrial production,”Journal of Intelligent Manufacturing, vol. 36,
pp. 765–800, 2025.
[5] M. Kilthau, V . Henkel, L. P. Wagner, F. Gehlhoffet al., “A decentralized
optimization approach for scalable agent-based energy dispatch and congestion
management,”Applied Energy, vol. 377, p. 124606, 2025.
[6] F. Bellifemine, G. Caire, and D. Greenwood,Developing Multi-Agent Systems with
JADE. John Wiley & Sons, 2007.
[7] E. Mengelkamp, J. Gärttner, and C. Weinhardt, “Intelligent agent strategies for
residential customers in local electricity markets,” inProceedings of the Ninth
International Conference on Future Energy Systems (e-Energy ’18), 2018, pp. 97–
107.
[8] J. D. Schölzel, S. Henn, M. Tings, R. Streblowet al., “Comparative analysis of
bidding strategies for auction-based local energy markets,”Energy, vol. 291, p.
130211, 2024.
[9] W. El-Baz, P. Tzscheutschler, and U. Wagner, “Integration of energy markets
in microgrids: A double-sided auction with device-oriented bidding strategies,”
Applied Energy, vol. 241, pp. 625–639, 2019.
[10] S. Bose, E. Kremers, E. M. Mengelkamp, J. Eberbachet al., “Reinforcement
learning in local energy markets,”Energy Informatics, vol. 4, no. 1, p. 7, 2021.
[11] G. Okwuibe, J. Bhalodia, A. Shokri Gazafroudi, T. Brenneret al., “Intelligent
bidding strategies for prosumers in local energy markets based on reinforcement
learning,”IEEE Access, vol. 10, pp. 119 168–119 185, 2022.
[12] R. G. Smith, “The contract net protocol: High-level communication and control in
a distributed problem solver,”IEEE Transactions on Computers, vol. C-29, no. 12,
pp. 1104–1113, 1980.
[13] S. Pfenninger and I. Staffell, “Long-term patterns of European PV output using
30 years of validated hourly reanalysis and satellite data,”Energy, vol. 114, pp.
1251–1265, 2016.
[14] BDEW Bundesverband der Energie- und Wasserwirtschaft e.V . (2025)
Standardlastprofile Strom. [Online]. Available: https://www.bdew.de/energie/
standardlastprofile-strom/
[15] Verband der Netzbetreiber, “Lastprofile für unterbrechbare verbrauchseinrichtungen
– step by step,” Verband der Netzbetreiber, Tech. Rep., 2004.
[16] J. Meiers, M. Ortleb, D. Jonas, L. Tadayonet al., “Control strategies for heat
pumps in a residential area under consideration of system operator benefits and
grid stability,”Energy and Buildings, vol. 332, p. 115442, 2025.
[17] C. Nobis and T. Kuhnimhof, “Mobilität in Deutschland – MiD: Ergebnisbericht,”
Bundesministerium für Verkehr und digitale Infrastruktur, Tech. Rep., 2018.
[Online]. Available: https://elib.dlr.de/125879/
[18] D. K. Gode and S. Sunder, “Allocative efficiency of markets with zero-intelligence
traders: Market as a partial substitute for individual rationality,”Journal of Political
Economy, vol. 101, no. 1, pp. 119–137, 1993.
[19] D. S. Kirschen and G. Strbac,Fundamentals of Power System Economics. Chich-
ester: John Wiley & Sons, 2004.
[20] M. Ortleb, J. Meiers, D. Jonas, and G. Frey, “Operation Strategies Using the Smart
Grid Ready Interface in Solar Heat Pump Systems,” inIEEE Industrial Electronics
Society Annual On-Line Conference (ONCON), 2022, pp. 1–6.
[21] M. Kilthau, A. Karmann, C. Derksen, and A. Fay, “Metric for Analysing Coopera-
tive and Competitive Algorithms for Distributed Frequency Control in Microgrids,”
in27th International Conference on Electricity Distribution (CIRED), 2023, pp.
546–550.
[22] D. Cliff, “Minimal-intelligence agents for bargaining behaviors in market-based
environments,” Hewlett-Packard Laboratories, Tech. Rep. HPL-97-91, 1997.
[23] J. Nicolaisen, V . Petrov, and L. Tesfatsion, “Market power and efficiency in a
computational electricity market with discriminatory double-auction pricing,”IEEE
Transactions on Evolutionary Computation, vol. 5, no. 5, pp. 504–523, 2001.
