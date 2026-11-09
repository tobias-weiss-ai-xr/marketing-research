---
title: Reinforcement Learning and Rule-Based Peer-to-Peer Pricing in Residential PV-BES Communities
url: https://arxiv.org/abs/2609.01680
category: digital-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Pablo Benalcazar
- Maciej Kalka
- Wilian Guamán
- Jacek Kamiński
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.01680
pages: 22
chars: 42189
fetched_at: '2026-11-08T13:20:56+00:00'
kb_version: 1
---

# Reinforcement Learning and Rule-Based Peer-to-Peer Pricing in Residential PV-BES Communities

Reinforcement Learning and Rule-Based Peer-to-Peer
Pricing in Residential PV-BES Communities
Pablo Benalcazar a,∗, Maciej Kalka a, Wilian Guamán b, Jacek
Kamiński a
aDivision of Energy Economics, Mineral and Energy Economy Research Institute, Polish
Academy of Sciences, Kraków, Poland
bGITEA, Escuela Superior Politécnica de Chimborazo (ESPOCH), Riobamba, Ecuador
Abstract
This paper compares rule-based and learning-based pricing mechanisms for
peer-to-peer (P2P) electricity trading in residential photovoltaic communi-
ties. The rule-based benchmarks comprise bill-sharing as an ex post allo-
cation mechanism, the mid-market rate, and supply–demand-ratio pricing.
The reinforcement-learning (RL) formulation is implemented through a Deep
Q-Network and evaluated under multiplier-based and learnable SDR-shaped
pricing, with a fixed-parameter SDR variant as a non-learning control. Per-
formance is assessed through community savings together with complemen-
tary financial and operational indicators. In the base PV-only configuration,
the rule-based benchmarks outperform the best RL policy. With battery
energy storage, evaluated for the RL policies only, community savings under
the best RL policy increase from€734.23 to€978.52. Across the learning-
based modes and in both configurations, SDR-shaped pricing outperforms
the multiplier-based parameterization considered. The results indicate that
rule-based pricing remains highly competitive wherever the two families are
compareddirectly, andthatstoragesubstantiallyimprovesthelearning-based
outcomes under this accounting, while the distribution of benefits remains
heterogeneous across households.
Keywords:Peer-to-peer electricity trading, Reinforcement learning,
Peer-to-peer pricing mechanisms, Local energy markets, Residential
∗Corresponding author.
Email address:benalcazar@min-pan.krakow.pl(Pablo Benalcazar )
arXiv:2609.01680v1  [cs.LG]  1 Sep 2026

photovoltaic communities, Battery energy storage systems
Nomenclature
Abbreviations
BES Battery energy storage
BS Bill-sharing mechanism
DQN Deep Q-Network
MMR Mid-market rate
P2P Peer-to-peer
PV Photovoltaic
RL Reinforcement learning
RL-M RL-Multiplier: multiplier-based pricing
RL-SDR-F RL-SDR-Fixed: fixed-parameter SDR-shaped pricing, non-learning
control
RL-SDR-L RL-SDR-Learnable: learnable SDR-shaped pricing
SDR Supply–demand ratio
SOC State of charge
SSI Self-sufficiency index
Indices and sets
tSettlement interval (hourly)
iHousehold index; also the minibatch sample index in Algorithm 1
kAction index,k= 1,...,K
ADiscrete action set of the RL agent
KNumber of actions inA
DDataset of days with hourly PV, load, and grid-price profiles
T tr Set of intervals with internal trading
RExperience replay buffer
BMinibatch sampled fromR
Energy quantities(kWh)
Esup t Aggregate local surplus available for internal trading
Esup,pv t PV share of the aggregate local surplus
Edem t Aggregate residual internal demand
Etr t Internally traded volume,Etr annual total
Ebuy t Energy purchased internally by buyers
Esell t Energy sold internally by sellers
Epv t Community PV generation
Eload t Community household consumption
Egrid,in t Grid imports,E grid,in annual total
Egrid,out t Grid exports
bt Community net balance,bt =E pv t −E load t
SDRt Supply–demand ratio,E sup t /Edem t (–)
Prices(€/kWh)
pbuy t Grid import price
2

psell t Grid export price
pMMR t Mid-market rate internal price
pSDR,sell t SDR benchmark internal sell price
pSDR,buy t SDR benchmark average buy price
pp2p,sell t Internal sell price quoted by the RL agent
pp2p,buy t Internal buy price quoted by the RL agent
ptr t Realized internal trading price,¯ptr its average
Costs and economic indicators(€)
C ref Community cost without internal trading,Cref i per household
C pool Community cost after internal trading
C BS i Cost assigned to householdiunder bill-sharing
Bcomm Community benefit,C ref−C pool (distinct from the minibatch sizeB)
ωi Share of the community benefit allocated to householdi,∑ iωi = 1(–)
C usr User cost
Rpro Prosumer revenue
Scomm Community savings
J base t Hourly community cost of the no-P2P reference
J p2p t Hourly community cost after P2P clearing and grid settlement
Pricing-mechanism parameters
µbuy k , µsell k Buy and sell multipliers of actionkunder RL-M (–)
α, βSell- and buy-price sensitivity of the SDR-shaped rule,0≤α≤1,
β≥1(–)
Cctrl Half-width of the grid price corridor (€/kWh)
Cbal Midpoint of the grid price corridor (€/kWh)
δLog-argument stability constant (–)
Reinforcement-learning parameters
st State vector at intervalt
˜bt Discretized community net balance, nine bins (–)
SOCt Mean battery state of charge across households, as a fraction of capacity
(–)
at Action selected at intervalt
rt Reward,J base t −J p2p t (€)
ht Hour of the day
Qθ Action-value network with parametersθ
Qˆθ Target network with parametersˆθ
π∗ Greedy policy obtained after training
γDiscount factor (–)
ηAdam learning rate (–)
BMinibatch size (–)
TTarget-network synchronization period (steps)
ENumber of training episodes (–) (distinct from the energy quantities
E• t)
εExploration rate, fromε 0 toε min (–)
λExploration decay rate per step (–)
3

1. Introduction
Peer-to-peer (P2P) electricity trading allows prosumers and consumers
to exchange electricity locally instead of relying exclusively on the external
grid [1]. It forms part of the broader development of local energy markets,
where participation rules, governance structures, and settlement mechanisms
continue to evolve [2]. Within that setting, pricing becomes particularly
important because it shapes both the value of internal transactions and the
way economic gains are shared among participants.
Among the pricing mechanisms proposed for P2P electricity trading, the
supply–demand ratio (SDR) and the mid-market rate (MMR) are the most
widely discussed [3]. Their selection is not neutral, as previous studies show
that different pricing rules can materially affect consumer payments and pro-
sumer revenues [4]. In residential settings, those effects also depend on avail-
able technologies, tariff design, and solar generation conditions [5, 6].
Reinforcement learning (RL) is increasingly being used in power-system
operation and planning [7]. In P2P electricity markets, RL has been applied
to price adjustment and trading coordination under changing operating con-
ditions [8]. This is particularly relevant, as learning-based policies may im-
prove aggregate economic outcomes. However, their advantage over simpler
rule-based benchmarks remains unclear [9].
In local communities with photovoltaic (PV) generation, the economic
performance of P2P trading depends on the local surplus available for ex-
change and on the technical configuration of the community, since changes in
PV output affect self-sufficiency, economic savings, and trading revenues [5,
10]. In this context, battery storage plays a key role by influencing both the
internal exchange conditions and the resulting economic outcomes.
Rule-based mechanisms and learning-based schemes have both been ex-
plored in the literature [2, 9], yet comparative evidence focused on their
financial outcomes remains limited [11]. This paper examines rule-based and
learning-based pricing formulations in a P2P electricity market. The rule-
based benchmarks are bill-sharing, MMR, and SDR, while the RL formula-
tion is evaluated through three operating modes. The rule-based mechanisms
are assessed in the base PV-only framework, whereas the RL policies are eval-
uated in both PV-only and PV-BES configurations. The comparison is based
on average trading price, user cost, prosumer revenue, community savings,
and complementary indicators of internal trading and self-sufficiency.
4

2. Market Framework and Pricing Mechanisms
2.1. P2P Market Framework
A local electricity community is considered to comprise prosumers with
PV generation and consumers without on-site generation [1, 2]. At each
interval, the energy exchanged internally is limited by the balance between
aggregate local surplus and aggregate internal demand.
LetE sup t denote the total surplus available for local trading and letEdem t
denote the total residual internal demand at intervalt, both net of self-
consumption. The traded volume is defined as
Etr t = min ( Esup t ,E dem t ) .(1)
Equation (1) gives the internally matchable volume. The rule-based
benchmarks settle this volume in full in every interval, with internal prices
bounded by the grid import and export prices, which ensures that neither
side is worse off than when settling with the grid whenever the export price
lies below the import price. The RL-based mechanisms instead quote prices
ex ante, and internal exchange is settled only in intervals where the quoted
prices remain strictly inside the grid price corridor and the internal buy–sell
spread is non-negative. Otherwise no internal exchange takes place in that
interval and both sides settle directly with the grid. In the intervals where the
export price exceeds the import price, full rule-based settlement reduces the
community benefit, whereas the RL-based mechanisms do not settle those
intervals internally. The realized annual volume therefore depends on the
pricing mechanism, even though (1) itself does not. The residual demand is
covered by grid imports, while surplus not absorbed internally is exported
to the grid. Within each interval, the traded volume is allocated to sellers
in proportion to their surplus and to buyers in proportion to their residual
demand.
2.2. Benchmark Pricing and Settlement Mechanisms
2.2.1. Bill-Sharing Mechanism
Bill-sharing represents collective settlement through the redistribution of
thecommunitybenefit[12]. LetC ref denotethetotalcommunitycostwithout
internal trading, and letCpool denote the total cost after local trading. The
community benefit is
Bcomm =C ref−C pool.(2)
5

The cost assigned to participantiis then
C BS i =C ref i −ωiBcomm, ∑
i
ωi = 1,(3)
whereω i denotes the allocated share of the community benefit, set in pro-
portion to each household’s share of the internally matched energy.
2.2.2. Mid-Market Rate Pricing
The mid-market rate mechanism defines an internal price between the
grid import and export prices [13]. Letpbuy t andp sell t denote the grid import
and export prices at intervalt. The MMR price is
pMMR t = pbuy t +p sell t 2 .(4)
Thisbenchmarkmaintainsadirectrelationtotheexternalgridpricecorridor.
2.2.3. Supply–Demand Ratio Pricing
In the SDR rule, the internal price depends on the local market balance
[4, 14]. The supply–demand ratio at intervaltis
SDRt = Esup t
Edem t .(5)
The corresponding internal sell and buy prices follow the uniform pricing
model of [15], in which both prices decrease monotonically from the grid buy
price when local supply is scarce to the grid sell price when supply meets
demand, giving
pSDR,sell t =



pbuy t psell t(
pbuy t −p sell t ) SDRt +p sell t ,0≤SDR t≤1,
psell t ,SDR t >1,
(6)
pSDR,buy t =



pSDR,sell t SDRt +p buy t (1−SDR t),0≤SDR t≤1,
psell t ,SDR t >1, (7)
so that the price responds to local scarcity and surplus conditions within the
grid price bounds. Internal exchange executes at the single pricepSDR,sell t ,
and each buyer covers its residual shortage at the grid import price. The
6

buy price in (7) is therefore the average a buyer pays across its internal
and residual purchases rather than a separately executed price, which makes
the mechanism budget-balanced and leaves no spread retained outside the
community. This is the settlement of [15] and of the original supply–demand-
ratio construction of [14].
2.3. RL-Based Pricing
Unlike the rule-based benchmarks, the RL formulation updates internal
prices sequentially, with a centralized agent that observes the community
state at each settlement interval and selects the pricing parameters. The
study evaluates three parameterizations of this mapping; in two of them the
agent selects among candidate actions, while the third holds the parameters
fixed and serves as a non-learning control within the same pricing family.
2.3.1. Multiplier-Based Pricing
Each action maps to a pair of scaling factors(µbuy k ,µ sell k )applied directly
to the prevailing grid prices, so that
pp2p,buy t =µ buy k ·p buy t ,(8)
pp2p,sell t =µ sell k ·p sell t .(9)
This mode is denoted RL-Multiplier (RL-M), and the candidate values are
listed in Table 2, paired index-wise to giveK= 8actions. The settlement
condition introduced in Sect. 2 requirespsell t <p p2p,sell t ≤p p2p,buy t <p buy t . Be-
cause the two multipliers scale different grid prices, RL-M does not guarantee
the middle inequality. Wheneverµbuy k pbuy t <µ sell k psell t , the internal spread in-
verts, the interval is not settled internally, and both sides trade with the
grid.
2.3.2. SDR-Based Pricing
Building on the supply–demand ratio defined in (5), the P2P prices are
computed as
pp2p,sell t =C ctrl·tanh ( −αln(δ+SDR t−1) ) +C bal,(10)
pp2p,buy t =C ctrl·tanh ( −βln(δ+SDR t−1) ) +C bal,(11)
whereC ctrl = (p buy t −psell t )/2,C bal = (p buy t +psell t )/2, andδ >0is a small
stability constant. Moreover, ifSDRt−1 >1, the price in (11) is set toCbal to
7

preserve a non-negative spread for sellers when local supply exceeds demand.
Prices for intervaltare posted ex ante from the community state observed at
the start of the interval. The supply–demand ratio entering (10) and (11) is
therefore the ratio realized in intervalt−1, and the same convention applies
to the state vector defined below. At the start of each episode, the lagged
supply–demand ratio is initialized to one.
The prices remain bounded betweenp sell t andp buy t , with the bounds
reached under extreme scarcity or surplus, which preserves individual ra-
tionality for both buyers and sellers. The pair(α,β), where0≤α≤1
andβ≥1, determines how sensitive the pricing rule is to changes in the
supply–demand balance. Under RL-SDR-Fixed (RL-SDR-F), the same pair
(α,β)is used throughout the horizon. Its action set contains a single ele-
ment. Consequently, no learning takes place and the state cannot influence
the resulting price. RL-SDR-F therefore acts as a fixed-parameter control
that isolates the contribution of adaptingαto operating conditions. Under
RL-SDR-Learnable (RL-SDR-L), the agent chooses(α,β)from the discrete
setA={(α k,βk)}K k=1, allowing the response to change with operating con-
ditions. In both cases, the supply–demand ratio remains the underlying
signal, but the resulting prices do not coincide with the rule-based SDR
benchmark because the mapping is different. Table 2 reports the value ofδ
and the candidate sensitivity pairs. All three pricing modes share the same
state description, although in RL-SDR-F the state cannot affect the selected
action. The community net balance between the PV generationEpv t and the
household consumptionE load t at intervaltis
bt =E pv t −E load t ,(12)
and its discretized version,˜bt, with nine bins whose edges lie at±0.2,±1,
±2, and±5kWh, is used to keep the state compact. The mean battery
state of charge SOCt is taken over all households as a fraction of capacity,
with households without storage contributing zero, and is discretized into
five equal bins, while the supply–demand ratio enters through a bounded
logarithmic transformation. Together with the cyclic encoding of the hour,
the state is
st =
(
sin(2πht/24),cos(2πh t/24), ˜bt, SOCt,SDR t−1
)
.(13)
For PV-only, SOCt is set to zero, which keeps the same state structure in
both technical configurations. PV generation does not appear as a separate
8

feature because its effect is already captured bybt andSDR t−1, both of which
reflect the surplus available for local exchange. Because load, generation, and
the battery trajectory are exogenous, the pricing action does not affect the
state transition, and the DQN thus serves as a discrete-action solver for the
learning problem. In every mode, the reward corresponds to the hourly cost
saving relative to a no-P2P reference, defined as
rt =J base t −J p2p t ,(14)
whereJ base t =E dem t pbuy t −E sup,pv t psell t , withE sup,pv t the PV share of the sur-
plus, andJ p2p t is the actual community cost after P2P clearing and residual
grid settlement. The RL agent is therefore trained to maximize aggregate
community savings. Because the SDR-shaped and multiplier-based rules
quote separate buy and sell prices, an interval withpp2p,buy t > pp2p,sell t gen-
erates a settlement spread that is retained by the market operator and is
not redistributed to participants. This spread entersJ p2p t as a cost. As a
result, maximizing community savings implicitly rewards a narrower internal
spread as well as a larger internal exchange. In the PV-BES configuration,
battery energy offered for internal exchange has no grid-export alternative.
For this reason,Jbase t credits export revenue only for the PV surplus. In in-
tervals without internal settlement, the battery energy offered for exchange
is curtailed, while the PV surplus is exported to the grid. The training base-
line therefore includes battery operation, whereas the reported savings are
expressed relative toCref, which excludes the battery.
The learning stage relies on a Deep Q-Network (DQN) [16] to approx-
imate the action-value functionQθ(s,a)through a feedforward neural net-
work. To stabilize training, the model uses a target networkQ ˆθ and an
experience replay bufferR, from which mini-batches are drawn to minimize
the mean-squared Bellman error. The network uses two hidden layers of 128
and 64 rectified-linear units and a linear output of|A|units, trained with
Adam (η=5×10−4) on minibatches ofB=64from a replay buffer of capacity
50,000. The discount factor isγ=0.95, and the target network is synchro-
nized everyT=200steps. Transitions are bootstrapped uniformly, including
at the episode boundary. Because the transition process is exogenous, the
bootstrapped term does not depend on the selected action and does not
alter the greedy policy. Training runs forE=500episodes, each covering
one day drawn uniformly at random, with replacement, from the 366 days
of the annual dataset. Exploration follows anε-greedy schedule decaying
exponentially from1.0to0.01at rateλ=0.99952per step. Both scenarios
9

Table 2: Pricing parameters for each pricing mode.
Parameter Symbol V alue
SDR stability constant (RL-SDR-F and RL-SDR-L)
Log-argument guardδ10 −6
RL-M action set (K= 8)
Buy multipliersµ buy k 0.2,0.3, ...,0.9
Sell multipliersµ sell k 1.05,1.10, ...,1.40
RL-SDR-F (K= 1)
Fixed sensitivity(α,β) (0.5,2.0)
RL-SDR-L action set (K= 9)
Sensitivity pairs(α k,βk) (0.1,2.0),...,(0.9,2.0)
share these hyperparameters and differ only in their technical configuration.
The full training procedure is outlined in Algorithm 1. Policies are evalu-
ated greedily over the same annual dataset used for training. The reported
results come from a single training run per mode and configuration, with a
fixed random seed. The differences among the RL modes therefore reflect a
single realization of the training process.
2.4. Evaluation Metrics
The comparison between mechanisms is carried out through financial and
operational metrics. Because the RL reward is defined from aggregate com-
munity savings, community savings are considered the main economic out-
come. Average trading price, user cost, prosumer revenue, traded energy,
self-sufficiency, and grid imports are then used to interpret how each mech-
anism produces that outcome [4, 9]. Table 3 lists the metrics used in the
comparative analysis, in whichEbuy t andE sell t denote the energy bought and
sold internally,Egrid,in t andE grid,out t the community grid imports and exports,
andp tr t the internal settlement price. For the rule-based benchmarks this is
a single price that enters both the user cost and the prosumer revenue. The
RL modes apply the internal buy price in the user cost and the internal sell
price in the prosumer revenue, andptr t then denotes their midpoint, which
is used only in the average trading price over the setTtr of intervals with
non-zero internal exchange. The self-sufficiency index uses the total house-
hold consumptionE load t , which includes the share met by on-site generation
and differs from the residual demandEdem t . The community savings coincide
with the community benefitBcomm.
10

Algorithm 1DQN training for RL-based P2P pricing.
Require:DatasetDof days with hourly PV, load, and grid-price profiles; action setA
Require:Discountγ; batch sizeB; target-update periodT; exploration rateε 0; decay
λ; minimumε min
1: InitializeQ θ randomly; setQ ˆθ←Q θ,R←∅,n←0, andε←ε 0
2:forepisodee= 1,...,Edo
3: Sample dayd∼Duniformly with replacement, load its 24 hourly profiles, reset
the community, and observes0
4:fort= 0,...,23do
5:ifUniform(0,1)<εthen
6:a t←random(A)▷explore
7:else
8:a t←arg maxaQθ(st,a)▷exploit
9:end if
10: Compute(p p2p,buy t ,p p2p,sell t )for the active pricing mode
11: Step the environment and observes t+1,J p2p t , andJ base t
12:r t←J base t −J p2p t and store(st,at,rt,st+1)inR
13:if|R|≥Bthen
14: Sample minibatchB={(s i,ai,ri,s′ i)}∼R
15:y i←r i +γmax a′Qˆθ(s′ i,a′)for alli∈B
16:θ←Adam
(
θ,∇θ 1 B ∑ i∈B (yi−Qθ(si,ai))2 ;η )
17:end if
18:n←n+ 1
19:ifnmodT= 0then
20: ˆθ←θ ▷synchronize target network
21:end if
22:ε←max(ε min,ελ)
23:end for
24:end for
Ensure:Greedy policyπ ∗(s) = arg maxaQθ(s,a)
3. Case Study
The case study considers a residential electricity community composed
of 20 heterogeneous households. Local trading is evaluated over an annual
horizon with an hourly settlement interval, and the remaining imbalance
is settled against time-varying grid buy and sell prices, with all monetary
values expressed in euro. Eight households are prosumers with on-site PV
generation, while the remaining 12 households are consumers without local
generation. The household demand profiles were synthetically generated us-
ing the RAMP framework, a bottom-up open-source stochastic model for
load-profile generation [18]. The model was calibrated to represent Polish
11

Table 3: Evaluation metrics considered in this study.
Metric Equation Ref.
Average trading
price¯p tr =|T tr|−1∑ t∈T trptr t [4]
User costC usr =∑ t ( ptr t Ebuy t +p buy t Egrid,in t ) [4]
Prosumer revenueR pro =∑ t ( ptr t Esell t +p sell t Egrid,out t ) [10]
Community
savingsS comm =C ref−C pool [9]
Self-sufficiency
indexSSI = 1−
∑
tEgrid,in t∑
tEload t [10]
Traded energyE tr =∑ t∈T trEtr t [17]
Grid importsE grid,in =∑ tEgrid,in t [5]
households using official energy statistics published by the Central Statisti-
cal Office of Poland [19]. The hourly PV generation profiles are derived from
an hourly irradiance and ambient-temperature series for Poland obtained
from the Renewables.ninja platform [20], converted through a capacity-based
model with temperature derating.
The import price follows a two-zone time-of-use tariff of the kind offered
to Polish households under the G12w tariff group, equal to 0.249€/kWh in
the weekday peak zones from 06:00 to 13:00 and from 15:00 to 22:00, and
to 0.137€/kWh in all other hours, including weekends. The export price
follows the hourly market price applied to prosumer settlement under the
Polish net-billing scheme, ranging from zero to 0.657€/kWh with an annual
mean of 0.100€/kWh. In 384 of the 8,784 hourly intervals the export price
exceeds the import price, in which case the grid price corridor is inverted.
Two technical configurations are considered. The first corresponds to a
PV-only community, while the second retains the same PV portfolio and
adds battery storage to the eight prosumer households. Table 4 summa-
rizes the main characteristics of both configurations. Both cases consider
the same community composition, settlement interval, and PV portfolio.
The PV-BES configuration differs from the base PV-only case by including
battery storage, with an aggregate energy capacity of 68.15 kWh and aggre-
gate charge/discharge power of 32.07 kW. Battery sizing and hourly dispatch
are determined upstream by a genetic algorithm that jointly optimizes each
household’s PV and battery capacity together with a rule-based dispatch
policy, minimizing annualized system cost (capital recovery, operation and
maintenance, grid trading, and battery degradation) over one representative
12

Table 4: Case-study characteristics and technical configurations.
Parameter PV-only PV-BES
Households (prosumers/consumers) 20 (8/12) 20 (8/12)
Households with battery storage 0 8
Community installed PV capacity (kW) 20.14 20.14
Community BESS energy capacity (kWh) 0.00 68.15
Community BESS charge/discharge power (kW) 0.00 32.07
Total annual household consumption (kWh) 37,742.06 37,742.06
Mean annual consumption per household (kWh) 1,887.1 1,887.1
Mean annual consumption of prosumers (kWh/household) 1,960.4 1,960.4
Mean annual consumption of consumers (kWh/household) 1,838.2 1,838.2
Table 5: Financial community-level results.
Method Case
A vg. price
(€/k Wh)
User cost
(€)
Pros. rev.
(€)
Savings
(€)
Savings
(%)
BS PV-only — — — 829.98 17.48
MMR PV-only 0.141 6,043.68 2,125.85 829.98 17.48
SDR PV-only 0.106 5,673.79 1,755.96 829.98 17.48
RL-M PV-only 0.120 6,126.61 1,797.29 418.49 8.81
RL-SDR-F PV-only 0.140 6,095.92 1,964.36 616.26 12.98
RL-SDR-L PV-only 0.147 6,095.92 2,082.34 734.23 15.46
RL-M PV-BES 0.135 6,018.64 1,877.76 606.94 12.78
RL-SDR-F PV-BES 0.150 5,981.40 2,093.68 860.09 18.12
RL-SDR-L PV-BES 0.156 5,981.40 2,212.11 978.52 20.61
year. The resulting hourly state-of-charge trace, sized assuming a round-trip
efficiency of approx. 91.4%, is a fixed input to the P2P evaluation and is
not altered by the settlement mechanism or the RL policy. That dispatch
is degradation-aware and cycles the batteries conservatively, with the result
that the storage contribution reported below is bounded by the upstream
sizing rather than by the settlement mechanism. Battery discharge enters
the hourly community balance, whereas the corresponding charging energy
is committed in the upstream dispatch and is not debited from the simulated
PV surplus or imports. The reported PV-BES results therefore include the
value of this upstream-committed charging energy. Both configurations are
evaluated on the same realization of the household demand profiles, which
keeps the comparison controlled and gives the two cases a common commu-
nity reference costCref of€4,747.81.
13

Table 6: Operational community-level results.
Method Case SSI
T raded energy
(k Wh)
Grid imports
(k Wh)
BS PV-only 0.304 7,266 26,263
MMR PV-only 0.304 7,266 26,263
SDR PV-only 0.304 7,266 26,263
RL-M PV-only 0.219 4,069 29,459
RL-SDR-F PV-only 0.301 7,131 26,398
RL-SDR-L PV-only 0.301 7,131 26,398
RL-M PV-BES 0.245 4,624 28,479
RL-SDR-F PV-BES 0.325 7,644 25,459
RL-SDR-L PV-BES 0.325 7,644 25,459
Figure 1: Hourly household-level P2P participation under RL-SDR-L on June 18 in the
PV-only configuration (a) and the PV-BES configuration (b).
4. Results and Discussion
4.1. Community-Level Comparison
Table 5 reports the financial results, with percentage savings expressed
relative to the community reference costCref. The BS row reports only sav-
ings because bill-sharing settles ex post without an hourly internal price. At
thecommunitylevel, therule-basedbenchmarksperformbestinthebasePV-
only configuration, with BS, MMR, and SDR all attaining€829.98. Within
the RL family, RL-SDR-L yields the best PV-only result, with community
savings of€734.23, followed by RL-SDR-F (€616.26) and RL-M (€418.49).
The SDR-shaped formulations therefore outperform the multiplier-based pa-
14

rameterization considered, but they do not surpass the rule-based bench-
marks in the base PV-only case.
This difference arises from the settlement design rather than from the
quality of learning. All three benchmarks are budget-balanced. Bill-sharing
redistributes the community benefit ex post, while MMR and SDR settle
every internal transaction at a single price, such that every payment made
by a buyer is received by a seller and the entire grid-price spread remains
within the community. Their community savings are therefore determined
by the traded volume and the grid price corridor alone, and the three values
accordingly coincide at€829.98 even though they price and allocate the ex-
change differently. The RL modes instead quote separate buy and sell prices,
and the resulting spread is, for a given traded volume, a net outflow from
the participants. Budget-balanced settlement therefore sets an upper bound
on the community savings that any mechanism retaining an internal spread
can attain on the same physical exchange. The same pattern appears in the
reported costs and revenues, where MMR attains€95.75 higher community
savings than RL-SDR-L, with lower user cost (€6,043.68 vs€6,095.92) and
higher prosumer revenue (€2,125.85 vs€2,082.34). The same ordering holds
operationally in Table 6, where traded energy is the cleared internal volume,
counted once per transaction, and the self-sufficiency index is evaluated at
community level from aggregate grid imports and aggregate household con-
sumption. In PV-only, the rule-based mechanisms clear the full internally
matchable volume (7,266 kWh) and reach the highest self-sufficiency (0.304),
whereas the RL policies clear slightly less (RL-SDR, 7,131 kWh) or substan-
tially less (RL-M, 4,069 kWh). The shortfall arises in the intervals where the
settlement condition fails. Under RL-SDR, the ex-ante buy price reaches the
grid import price in the interval that follows an hour without local surplus,
which prevents internal settlement in that interval, and a small additional
volume is not settled internally in the intervals where the grid price corri-
dor itself is inverted. Under RL-M, the volume not settled internally arises
where the paired multipliers invert the internal spread, and it combines two
distinct effects. At these tariffs, 1,768 kWh of the matchable volume falls in
intervals where no pair in the action set yields a valid spread, and this part of
the shortfall hence follows from the action set rather than from the learned
policy. The remaining 1,429 kWh is not settled internally in intervals where
at least one feasible pair existed and the learned policy nevertheless selected
an inverted one.
When the community moves from PV-only to PV-BES, savings increase
15

from€418.49 to€606.94 for RL-M, from€616.26 to€860.09 for RL-SDR-F,
and from€734.23 to€978.52 for RL-SDR-L. Storage therefore improves the
economic performance of the learning-based policies, especially the SDR-
shaped variants. BecauseC ref excludes the battery, these figures combine
two effects. With batteries operating but no internal trading, the commu-
nity cost falls to€4,642.05. Accordingly,€105.76 of the reported PV-BES
savings comes from storage alone, before accounting for the charging energy
committed upstream, and would accrue under any settlement mechanism.
The internal settlement produces the remaining€872.76 under RL-SDR-L,
€138.53 more than the same policy achieves in the PV-only case.
Fig. 1 provides an operational view of the best-performing RL policy at
household level, with negative values denoting net energy sold to the local
market. On the day shown, selected for its high battery activity, prosumer
households act predominantly as net sellers during the solar production win-
dow, while consumer households absorb that local surplus as net buyers.
Both panels use the same household demand profiles and PV portfolio, and
the two trained policies share the fixed buy-price sensitivityβ, and the dif-
ference between the panels thus reflects battery operation alone. In the
PV-BES panel, trading therefore extends beyond the solar window as the
scheduled battery discharge is exchanged in the evening hours, consistent
with the higher traded energy and self-sufficiency reached by RL-SDR-L in
that configuration.
InbothPV-onlyandPV-BES,RL-SDR-FandRL-SDR-Lattainthesame
traded energy and self-sufficiency index according to Table 6. The advantage
of RL-SDR-L therefore lies in a more effective economic settlement of the
same internal exchange, not in a larger traded volume. That settlement ad-
vantage is measurable, as the annual internal spread falls from€210.46 under
RL-SDR-F to€92.49 under RL-SDR-L in the PV-only case, a reduction of
€117.97 that matches the community-savings difference exactly. The learned
policy is state-dependent rather than constant, selecting a meanαof 0.26 in
surplus intervals and 0.48 in deficit intervals. The same settlement advan-
tage holds in PV-BES, where RL-SDR-L exceeds RL-SDR-F by€118.43 on
the same traded volume. The rule-based benchmarks are not re-evaluated
under storage in this study, and the PV-BES results consequently compare
the learning-based modes only with one another and are not directly compa-
rable with the PV-only rule-based values. Because the battery trajectory is
fixed independently of the settlement mechanism, the budget-balance bound
above indicates that the rule-based benchmarks would retain their advantage
16

Figure 2: Distribution of household savings by settlement mechanism.
under storage.
4.2. Household-Level Distribution of Benefits
Household-level outcomes show that aggregate community gains are not
distributed uniformly across participants, as illustrated in Fig. 2. Each dis-
tribution collects the savings of the 20 households under one mechanism,
expressed relative to each household’s conventional net bill. The diamond
marks the pooled median, the horizontal bar marks the interquartile range,
and the annotation reports the median saving of the consumer group and of
the prosumer group. For prosumers the conventional bill is reduced by export
revenue, which allows savings to exceed 100%, in which case the annual net
bill turns into a small net income. The rule-based mechanisms appear for the
PV-only configuration, while the RL modes appear for both configurations.
In the PV-only framework, the three benchmarks deliver identical aggregate
17

community savings, yet they distribute those savings differently across house-
holds. SDR distributes the savings most evenly between the two groups, with
consumer and prosumer medians of 19.3% and 28.6%, whereas BS and MMR
give consumer medians near 10% and prosumer medians above 100% on the
same aggregate community savings. The pooled median mainly reflects the
twelve consumer households, while the extended upper tails correspond to
prosumers, whose percentages rest on small net-bill denominators.
A similar pattern appears within the RL family. In PV-only, RL-SDR-L
reaches€734.23, above RL-SDR-F (€616.26) and RL-M (€418.49). After
storage is added, these values rise to€978.52,€860.09, and€606.94, respec-
tively, yet the gain is not distributed evenly across households. In PV-BES,
the RL-SDR variants develop a more extended upper tail, which indicates
stronger gains for only part of the community rather than for all house-
holds in the same proportion. This household-level behavior matches the
community-level results, where rule-based benchmarks remain competitive
in PV-only, SDR-shaped RL pricing outperforms the multiplier-based RL
mode, and RL-SDR-L remains the best-performing learning-based mode un-
der battery storage.
5. Conclusions
This paper compared rule-based and RL-based pricing mechanisms for
P2P electricity trading in residential PV communities. In the base PV-only
configuration, the rule-based benchmarks outperformed the best RL policy.
With battery storage, the best RL policy increased community savings from
€734.23 to€978.52 before accounting for the energy used to charge the bat-
teries. The rule-based benchmarks were evaluated only in the PV-only con-
figuration. The budget-balance bound established in Sect. 4 indicates that
they would retain their advantage under storage, although this comparison
was not carried out in this study.
WithintheRLfamilyandinbothconfigurations, theSDR-shapedpolicies
outperformed the multiplier-based parameterization considered. The advan-
tage of RL-SDR-L over RL-SDR-F is not explained by a larger traded volume
or a higher self-sufficiency index, but by a more effective economic settlement
of the same internal exchange. These findings support adaptive SDR-based
pricing for local electricity markets, particularly when PV communities in-
clude storage. The settlement does not represent network charges, levies, or
taxes. The reported savings are therefore upper bounds in this respect.
18

Future work may extend the analysis to seasonal operating conditions,
evaluate the rule-based benchmarks under storage, and compare rule-based
and learning-based pricing under network-constrained and inter-community
P2P trading.
Acknowledgements
The research was conducted as part of the CoEnerBuild project, funded
by the Polish National Center for Research and Development and the Eu-
ropean Union under the CETPartnership program (project code Cetp-FP-
2023-00014). It was also partially conducted as part of the statutory research
activity of the Mineral and Energy Economy Research Institute of the Polish
Academy of Sciences.
Declaration of competing interest
The authors have no competing interests to declare that are relevant to
the content of this article.
References
[1] T. Sousa, T. Soares, P. Pinson, F. Moret, T. Baroche, E. Sorin, Peer-to-
peer and community-based markets: A comprehensive review, Renew-
able and Sustainable Energy Reviews 104 (2019) 367.doi:10.1016/j.
rser.2019.01.036.
[2] T. Capper, A. Gorbatcheva, M. A. Mustafa, M. Bahloul, J. M. Schwid-
tal, R. Chitchyan, M. Andoni, V. Robu, M. Montakhabi, I. J. Scott,
C. Francis, T. Mbavarira, J. M. Espana, L. Kiesling, Peer-to-peer, com-
munity self-consumption, and transactive energy: A systematic liter-
ature review of local energy market models, Renewable and Sustain-
able Energy Reviews 162 (2022) 112403.doi:10.1016/j.rser.2022.
112403.
[3] H. J. Kim, Y. S. Chung, S. J. Kim, H. T. Kim, Y. G. Jin, Y. T. Yoon,
Pricing mechanisms for peer-to-peer energy trading: Towards an in-
tegrated understanding of energy and network service pricing mecha-
nisms, Renewable and Sustainable Energy Reviews 183 (2023) 113435.
doi:10.1016/j.rser.2023.113435.
19

[4] Y. Zhou, J. Wu, C. Long, Evaluation of peer-to-peer energy sharing
mechanisms based on a multiagent simulation framework, Applied En-
ergy 222 (2018) 993.doi:10.1016/j.apenergy.2018.02.089.
[5] D. Neves, I. Scott, C. A. Silva, Peer-to-peer energy trading potential:
An assessment for the residential sector under different technology and
tariff availabilities, Energy 205 (2020) 118023.doi:10.1016/j.energy.
2020.118023.
[6] P. Benalcazar, M. Kalka, J. Kamiński, From consumer to prosumer: A
model-based analysis of costs and benefits of grid-connected residential
pv-battery systems, Energy Policy 191 (2024) 114167.doi:10.1016/j.
enpol.2024.114167.
[7] G. Pesántez, W. Guamán, J. Córdova, M. Torres, P. Benalcazar, Re-
inforcement learning for efficient power systems planning: A review
of operational and expansion strategies, Energies 17 (9) (2024) 2167.
doi:10.3390/en17092167.
[8] D. Qiu, Y. Ye, D. Papadaskalopoulos, G. Strbac, Scalable coordi-
nated management of peer-to-peer energy trading: A multi-cluster deep
reinforcement learning approach, Applied Energy 292 (2021) 116940.
doi:10.1016/j.apenergy.2021.116940.
[9] R. May, P. Huang, A multi-agent reinforcement learning approach for
investigating and optimising peer-to-peer prosumer energy markets,
Applied Energy 334 (2023) 120705.doi:10.1016/j.apenergy.2023.
120705.
[10] P. Huang, M. Lovati, J. Shen, J. Chai, X. Zhang, Investigation of the
peer-to-peer energy trading performances in a local community under
the future climate change scenario in sweden, Energy Reports 8 (2022)
989.doi:10.1016/j.egyr.2021.12.032.
[11] S. N. Islam, A review of peer-to-peer energy trading markets: Enabling
models and technologies, Energies 17 (7) (2024) 1702.doi:10.3390/
en17071702.
[12] D. Gonzalez-Asenjo, L. R. Izquierdo, J. Sedano, A Simple and Efficient
Method to Allocate Costs and Benefits in Energy Communities, Journal
20

of Industrial Engineering and Management 16 (2) (2023) 398.doi:
10.3926/jiem.5514.
[13] W. Tushar, T. K. Saha, C. Yuen, P. Liddell, R. Bean, H. V. Poor,
Peer-to-Peer Energy Trading With Sustainable User Participation: A
Game Theoretic Approach, IEEE Access 6 (2018) 62932.doi:10.1109/
ACCESS.2018.2875405.
[14] N. Liu, X. Yu, C. Wang, C. Li, L. Ma, J. Lei, Energy-sharing model with
price-based demand response for microgrids of peer-to-peer prosumers,
IEEE Transactions on Power Systems 32 (5) (2017) 3569–3583.doi:
10.1109/TPWRS.2017.2649558.
[15] R. Zhang, M. Lee, D. Zhao, H. Kang, T. Hong, Peer-to-peer trading
price and strategy optimization considering different electricity market
types, tariff systems, and pricing models, Energy and Buildings 300
(2023) 113645.doi:10.1016/j.enbuild.2023.113645.
[16] V. Mnih, K. Kavukcuoglu, D. Silver, A. A. Rusu, J. Veness, M. G.
Bellemare, A. Graves, M. Riedmiller, A. K. Fidjeland, G. Ostrovski,
S. Petersen, C. Beattie, A. Sadik, I. Antonoglou, H. King, D. Kumaran,
D. Wierstra, S. Legg, D. Hassabis, Human-level control through deep
reinforcement learning, Nature 518 (7540) (2015) 529.doi:10.1038/
nature14236.
[17] M. M. Hoque, M. Khorasany, M. I. Azim, R. Razzaghi, M. Jalili,
A framework for prosumer-centric peer-to-peer energy trading us-
ing network-secure export–import limits, Applied Energy 361 (2024)
122906.doi:10.1016/j.apenergy.2024.122906.
[18] F. Lombardi, S. Balderrama, S. Quoilin, E. Colombo, Generating high-
resolution multi-energy load profiles for remote areas with an open-
source stochastic model, Energy 177 (2019) 433.doi:10.1016/j.
energy.2019.04.097.
[19] Statistics Poland, Energy consumption in households in 2024, publica-
tion released on January 30, 2026 (Jan. 2026).
URLhttps://stat.gov.pl/en/topics/environment-energy/
energy/energy-consumption-in-households-in-2024,2,7.html
21

[20] S. Pfenninger, I. Staffell, Long-term patterns of European PV output
using 30 years of validated hourly reanalysis and satellite data, Energy
114 (2016) 1251.doi:10.1016/j.energy.2016.08.060.
22
