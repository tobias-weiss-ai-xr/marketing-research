---
title: Accelerating fossil gas independence in Europe
url: https://arxiv.org/abs/2607.21048
category: consumer-behavior
subcategory: empirical
date: 2026-07
venue: ''
authors:
- Lukas Franken
- Iegor Riepin
- Tom Brown
source: arxiv
pdf_url: https://arxiv.org/pdf/2607.21048
pages: 29
chars: 100759
fetched_at: '2026-11-08T12:58:16+00:00'
kb_version: 1
---

# Accelerating fossil gas independence in Europe

Accelerating fossil gas independence in Europe
Lukas Frankena, Iegor Riepina, Tom Browna
aDepartment of Digital Transformation in Energy Systems, Technische Universität Berlin, Germany
Abstract
Recent price shocks have prompted calls to curb Europe’s dependence on fossil gas imports, but the cost of
this goal, and the consumer protection it affords, remain uncertain. Here we address this gap by imposing
constraints on fossil gas supply in a European energy system model that co-optimises abatement across
all gas uses at high spatio-temporal resolution. Cutting import reliance proves economically compelling:
through savings in power generation and low-temperature heat in industry and buildings, Europe can
halve its natural gas consumption for 16bne/a, aligning demand with the continent’s production capacity
of 200 bcm. This extra system cost is comparable to what consumers spend today on a 2e/MWh rise in gas
import prices. However, this sovereignty alone does not shield consumers from global gas price volatility:
we find that, even at a small share of the mix, gas remains dominant in shaping the marginal electricity
price, leaving consumers exposed without additional policy measures.
850
900
950
1000
1050
1100
1150
1200bn
a Autarky (200 bcm) No LNG (275 bcm) Today's Demand
1029
1192
990
1153
957
1129
941
1117
928
1113
917
1111
911
1115
912
1123
912
1133
System cost excl. ETS payments
System cost incl. ETS payments
0 100 200 300 400
T otal fossil gas supply [bcm/a]
-25
0
100
200
300
400Sectoral Gas Allocation [bcm/a]
b
Consumption
<500C industry heat
electricity
building heat
hydrogen
>500C industry heat and feedstock
Supply
biomethane
gas boiler
electric heating
biomass
ambient heat
Industry Heat <100°C
c
Autarky
(200 bcm)
No LNG
(275 bcm)
Today's
Demand
gas boiler
electric heating
biomass
ambient heat
Industry Heat 100-200°C
direct firing gas
biomass
Industry Heat 200-500°C
gas turbineOnshore Wind
Solar PV
Nuclear
Hydro (res+dam)Offshore WindElectricity
Supply Share
gas
biomass CHP
ambient heatelectric heatingDistrict Heating
gas
ambient heat
electric heating
biomass boiler
oil boilerIndividual Heating
steam-methane reformingelectrolysis
Hydrogen
0 100 200 300 400
T otal fossil gas supply [bcm/a]
direct firing gas
hydrogen
Industry Heat >500°C
Email address:lukas.franken@tu-berlin.de(Lukas Franken)
arXiv:2607.21048v1  [econ.GN]  23 Jul 2026

Introduction
Gas is deeply embedded in European economies. Over the last
ten years, annual consumption has hovered between 350 and
450 bcm, making up around a quarter of Europe’s total pri-
mary energy demand [1, 2]. Half of this consumption, around
200 bcm, can be produced domestically; for the remainder, Eu-
rope relies on imports [3].
These gas imports have become an increasingly acute economic
risk for Europe. In 2022, following the near-complete decou-
pling from Russian fossil fuels, the ensuing scarcity and a pivot
to shipped Liquefied Natural Gas (LNG), Europe spent an addi-
tional trillion euros on oil, gas and coal relative to 2021 [4]. In
early 2026, gas imports re-emerged as a vulnerability when the
closure of the Strait of Hormuz tightened global LNG supply by
20% and European gas prices roughly doubled to 45–60e/MWh
[5]. Two shocks within five years have triggered a debate in
Europe about ending gas import reliance altogether [6–8]; ini-
tially considered a safe alternative, the new LNG dependence
reinforces the coupling between volatile global gas markets and
consumer prices across the broad spectrum of gas applications
[9] (Fig 1).
In European policy, the drive to lower gas reliance doubles down
on existing decarbonisation efforts. In 2022, theRePowerEU
package allocated an additional 290 bne to medium- and long-
term gas demand reduction [15], on top of the 2021Fit-for-55
package, which already targeted a 30% reduction in gas use by
2030 [16]. As recently as early 2026, the EU decided to end all
Russian gas imports by the end of the same year [17, 18]. The
same communication also includes a directive for member states
mandating national plans to reduce fossil gas consumption. In
response to the closure of the Strait of Hormuz, in April 2026
the EU introduced theAccelerateEUprogramme, which sets
more ambitious electrification targets, aims to speed up grid
reinforcement, and seeks to protect consumers and industry
from energy-price spikes [ 19]. Meanwhile, the ongoing gas
displacement in Europe is mainly driven by decarbonisation
measures such as carbon pricing [ 20, 21], renewable-power
subsidies [22], and incentives for households to electrify their
heating [23].
So far, the gas phase-out has progressed unevenly across power,
building heat and industry because the cost structure of alter-
natives varies [24, 25]. Wind and solar are directly displacing
bulk power generation [26], and batteries are competing with
gas to balance an increasingly intermittent generation fleet
[27]. In the building sector, Europe currently installs around
2.5 million heat-pump units annually [28], mostly displacing
gas boilers, though heat pumps still provide only a minority of
overall heat [29]. Phase-out in industry is more complex. Most
industrial gas is burned for heat, more than two-thirds for tem-
peratures below 500◦C, where electrification or biomass options
are widely considered commercially available [ 30]. Higher-
temperature demands, such as cement or glass production, are
considered hard-to-abate, with expensive and scarce hydrogen
as the main alternative [31]. Hydrogen production itself, along
with methanol synthesis, hydrocracking and parts of petro-
chemical production, relies on gas as a feedstock [32–34]; there
too gas is hard to replace [35]. A final option is to supplement
supply with biomethane, produced from maize, manure and
agricultural residues: by 2030 the EU targets around 35 bcm of
annual production [15]. However, research suggests that this
target exceeds plausible capacity by roughly a factor of two
[36].
The literature emphasises the role of “low-hanging fruit” in
lowering Europe’s import dependence [37, 38]. These are re-
newable power paired with the electrification of building heat
and low-temperature industry heat, a goal largely aligned with
EU policy [15]. This alignment between decarbonisation and
energy-independence targets has been noted [ 39], but other
work highlights that gas phase-out follows from a decarbonisa-
tion drive only under a carbon-pricing regime [40]; otherwise,
import reduction pulls domestic fossils such as lignite back
into the market, as for instance in Germany in 2022 [41]. For
hard-to-abate sectors, EU policy allocates substantial funds to
electrolysis to scale up production before 2030 [ 15], acceler-
ating the deployment of gas substitutes for high-temperature
industry. However, an alternative pathway proposed byAgora
defers hydrogen uptake to 2035 [37, 38].
Existing studies tend to embed analyses of gas phase-out within
pathways to net-zero emissions by 2050 [ 15, 37, 39]. This is
because the promise of LNG supply in 2022 left climate goals as
the primary motivator for further gas reduction [39]. By 2026
this perspective has shifted. The substantial cost volatility from
exposure to global LNG markets, together with wider geopolit-
ical uncertainty [6], has elevated supply security and resilience
as central objectives. This raises the question of how much gas
demand can be reduced to align either with European produc-
tion capacity alone (around 200 bcm) [3], requiring a halving
of current consumption, or with combined domestic produc-
tion and pipeline imports from North Africa and Azerbaijan
(around 275 bcm) [42, 43], requiring a reduction of roughly one
third. These are non-trivial yet viable near- to medium-term
targets with the potential to meaningfully curb Europe’s import
vulnerability [7]. Existing work fails to isolate the costs, price
changes and interventions needed for Europe to reach these
milestones.
Much of our understanding of opportunities to reduce natural
gas consumption comes from case studies. These assess the
business case for localised alternatives [ 30, 38, 44] or model
sectors in sequence [37]. However, gas supplies around 20% of
European energy [1], and reducing its consumption is a non-
marginal intervention. The partial equilibrium perspective is
only broken once all coupled sectors are cleared within a single
market simulation.
Large-scale sector-coupled energy system models (ESMs) solve
this issue, but lack the fidelity of case studies. This is partly for
historical reasons; modern ESMs emerged from power sector
applications first [45], gradually expanded to other sectors, such
as heat and transport [46], but the industry sector has remained
a holdout, treated exogenously [47]. As a result, even recent
2

FR
UA
BY
LT
CZ
DE
EE
LV
SE
LU
BE
MK
ALES
DK
RO
HU
SK
PL
IE GB
GR
AT
IT
CH
NL
LI
RSHR
SI
BGSMMC
AD ME
PT
MD
GI
MT
JEGG
IM
CY
IL
LB
Atlantic
Ocean
North
Sea
Mediterranean Sea
Baltic
Sea
Black
Sea
Source type
Domestic production
Pipeline import
LNG
Infrastructure
Gas pipeline
Industrial site
Importing pipeline (2024)
Inactive pipeline
LNG terminal
2024 gas supply (bcm)
10
50
UK
Netherlands
Romania
Rest of EU
Norway
Russia
North Africa
Azerbaijan
LNG
Source Country
Consumption
Sectoral
Consumption
Future
Supply
0
100
200
300
400
Gas Supply and Demand [bcm]
Other
Industry
heating
Power
sector
Building
heating
RO
BE
PL
NL
ES
FR
IT
GB
DE
Romania
Netherlands
Rest of EU
UK
Norway
Azerbaijan
North
Africa
Russia
LNG
Romania
Netherlands
Rest of EU
UK
Norway
Azerbaijan
North
Africa
LNG
2024 European Gas Balance
Industry
feedstock
Storage
drawdown
No-LNG
Autarky
Figure 1:aMap of European gas infrastructure and supply pathways.bSupply and consumption split by country and sector. Consumption data from Eurostat
[10, 11]; supply data from [12]; industrial site locations from [13, 14].
ESM studies fix industry gas phase-out exogenously [39], and
fail to capture how gas scarcity drives up its value to the system,
and hence its consumer price. Capturing this scarcity rent is a
key strength of ESMs, but it can only realistically form if the
model internalises the cost of gas alternatives in hard-to-abate
sectors such as high-temperature industry. With exogenous
industry, the model is left to navigate gas phase-out from power
and building sectors, where gas alternatives have a different
cost structure, thereby distorting the optimal sectoral ordering
of gas consumption reduction. Meanwhile, integrated assess-
ment models (IAMs) typically have strong sectoral coverage
but are built on mathematics that complicate the derivation of
scarcity rent [48], and, like some ESM studies [ 15], also lack
the spatio-temporal resolution crucial to simulating commodity
price drivers.
This paper presents the first European energy-system model
to optimise gas allocation across all sectors at high spatio-
temporal resolution for varying gas consumption levels. We
achieve this by iteratively tightening a cap on fossil gas supply
– from 450 bcm, approximating current European consumption,
down to zero in 25 bcm increments. We use the PyPSA-Eur
model, which captures sectoral, geographic and temporal detail
in continent-wide energy-economic trade-offs. The model is
further enhanced such that almost all gas uses are fully en-
dogenously represented, including industrial heat. That means
decisions on fuel switching, infrastructure investment, and heat
provision route selection are not imposed but emerge as part
of the cost-optimisation process, driven by the relative costs
across competing supply and substitution options. As a result,
the model can trace a cost-optimal pathway for gas phase-out–
revealing the sectoral and regional ordering in which it is most
cheaply displaced and the cost penalties incurred when cheap
alternatives dry up and the cost of gas abatement rises.
We anchor the analysis to two near- to mid-term gas-consumption
milestones that could be achieved in the period 2030–35. The
first is theNo-LNGscenario with 275 bcm consumption that
restricts imports to pipeline gas; the second is theAutarkysce-
nario at 200 bcm that only uses domestic European production.
We compare the cost-optimal roll-out needed to reach the mile-
stones with the current pace of European technology deploy-
ment, and quantify the acceleration required for gas-autarkic
supply by 2030 or 2035. We also assess how the commodity gas
price–such as the spike caused by the 2026 supply disruptions–
influences the gas-consumption level that long-term market
equilibrium steers towards. Finally, the analysis highlights and
characterises how gas prices diffuse through the energy system
and shape marginal electricity prices, even after gas has largely
left the bulk electricity mix. This enables us to asssess the con-
ditions and policy levers that help to ensure lower gas imports
turns into an effective means to protect consumers from spikes
in global gas prices.
Cost-Optimal Gas Phase-Out is Concentrated in Low-
Temperature Industry Heat and Bulk Power
We assess total system cost and sectoral implications for differ-
ent levels of gas consumption. The market price for gas is set
at 24.6 e/MWh, representing a uniform commodity price for
both domestically produced and imported gas and reflecting
the typical post-2022 price regime [5]. We frame the analysis as
a perspective on 2030–35 and choose the techno-economic and
roll-out assumptions, along with a carbon price of 100 e/tCO2,
accordingly. If gas consumption stays at today’s levels of 350–
450 bcm/a, its allocation matches how gas is used in the mid-
2020s system–roughly split into thirds between the power sec-
tor, building heat and industry (Fig 2). By inserting the existing
fleet of residential heating, we ensure that the split of heat
3

850
900
950
1000
1050
1100
1150
1200bn
a Autarky (200 bcm) No LNG (275 bcm) Today's Demand
1029
1192
990
1153
957
1129
941
1117
928
1113
917
1111
911
1115
912
1123
912
1133
System cost excl. ETS payments
System cost incl. ETS payments
0 100 200 300 400
T otal fossil gas supply [bcm/a]
-25
0
100
200
300
400Sectoral Gas Allocation [bcm/a]
b
Consumption
<500C industry heat
electricity
building heat
hydrogen
>500C industry heat and feedstock
Supply
biomethane
gas boiler
electric heating
biomass
ambient heat
Industry Heat <100°C
c
Autarky
(200 bcm)
No LNG
(275 bcm)
Today's
Demand
gas boiler
electric heating
biomass
ambient heat
Industry Heat 100-200°C
direct firing gas
biomass
Industry Heat 200-500°C
gas turbineOnshore Wind
Solar PV
Nuclear
Hydro (res+dam)Offshore WindElectricity
Supply Share
gas
biomass CHP
ambient heatelectric heatingDistrict Heating
gas
ambient heat
electric heating
biomass boiler
oil boilerIndividual Heating
steam-methane reformingelectrolysis
Hydrogen
0 100 200 300 400
T otal fossil gas supply [bcm/a]
direct firing gas
hydrogen
Industry Heat >500°C
Figure 2: European energy system transformation pathways as annual fossil gas supply is constrained to different values (𝑥-axis). A fixed carbon price of 100
e/tCO2 is assumed throughout. The vertical shaded areas indicate consumption levels between 2020 and 2025 (Today’s Demand), vertical lines highlight the
European annual domestic production capacity of 200 bcm (Autarkyscenario) and domestic production plus pipeline imports from Azerbaijan and North Africa
to 275 bcm (No-LNGscenario).aTotal system cost with and without spending in carbon markets.bGas allocation by sector. Industry heat <500°C groups the
three heating bands<100°C, 100–200°C and 200–500°C, building heat includes residential and service sector heat for rural, individual urban and district demands.
Steam-methane reforming with carbon capture is not enabled in the model.cShares of supply mix by sector. Note that the slice of industry heat demand shown
here refers only to the share currently supplied by gas. Further note that the model natively works in TWh. To represent gas-related quantities in billion cubic
meters (bcm), we chose a unit conversion factor of 10 as conventions differ around this value.
supply across electric, gas, oil and biomass sources is broadly
aligned with the real 2020s system (Fig 12).
We find that tightening the cap on fossil gas supply leaves
system cost largely unchanged deep into the phase-out (Fig 2a).
Indeed, the change in system cost is minimal between theNo-
LNG(275 bcm/a) andAutarky(200 bcm/a) scenarios, and rises
by up to∼100 bne for deeper gas phase-out. Not accounting
for carbon spending, costs increase by∼5 bne/a (<1%) for the
No-LNGscenario and∼16 bne/a (<2%) forAutarky.
Cost-optimal curbing of gas use is largely enabled by phas-
ing out gas in industry heat below 500 ◦C and sharply reduc-
ing power-sector gas use (Fig 2). The vast majority of gas
is replaced by renewable power generation, heat pumps and
biomass boilers. Biomass use intensifies in the 200–500°C
band, where electric alternatives are largely unavailable [38].
This pushes biomass consumption from around 1,300 TWh
to roughly 1,700 TWh under deeper gas reductions (Fig 14;
for reference, 1,300 TWh of natural gas corresponds to around
130 bcm). This level is high and, as in the 2020s, includes unsus-
tainable crop-based sources as well as more sustainable wastes
and residues (for reference, 2021 solid biomass use was around
1,300 TWh/a [49]). Its allocation, however, partially aligns with
cost-optimal biomass use in a future carbon-neutral European
energy system, where biomass burning (as it is used here) would
be paired with carbon capture to leverage biogenic carbon for
negative emissions and renewable fuels [49]. The solid-biomass
supply curve used in the present model is shown in Fig 15.
There are potential options to electrify industry heat demands
above 500°C [50], but these are less mature and not included in
the present work.
In the power sector, gas gradually exits bulk electricity genera-
tion at around 250 bcm of total gas use (Fig 2b,c), but continues
to contribute minor volumes well into the phase-out. This is
because gas serves three distinct roles in the power sector, each
with different displacement economics. First, in bulk power gen-
eration its competitors are wind and solar, which are directly
cost-competitive. Second, in day-to-day balancing of renew-
ables, batteries displace gas turbines. Third, backup generation
during extended lulls in renewable generation (Dunkelflaute),
which batteries would be too expensive to bridge. Therefore,
4

even at extremely low fossil gas supply, the model does not
displace gas-based backup, indicated by generation peaks on a
small subset of days (Fig 13).
Residential and service-sector heating (hereafter building heat)
is the third sector to phase out gas, after industry heat below
500°C and power. In contrast to the other sectors, where gas
phase-out exhibits a sharp “switching” behaviour, building heat
phases out more gradually (Fig 2bandc). This is caused by
regional differences in the cost of heat when supplied by heat
pumps. Renewable-power costs and heat-pump coefficients
of performance both depend on local conditions, creating re-
gional hold-outs where alternatives to gas are less competitive.
Some modelling choices also contribute: biomass- and oil-boiler
capacity expansion is prohibited, reflecting both their health
impact [51] and ongoing trends [52]. Further, heat supply is
forced to beload-following(see Methods a), which drives up
the levelised cost of heat to 100–200 e/MWh, a range broadly
in line with the literature [ 53]. As a result, even when gas
consumption falls below 50 bcm/a, around half is used for resi-
dential heating (Fig 2a). As will be discussed, these results are
sound within the logic of the model, but rest on the model’s
cost assumptions, which can differ from those faced by real
consumers. Real supply choices depend on gas and electricity
retail prices, which include grid tariffs, taxes and utility margins
that are only partially represented within the model.
Between theNo-LNGandAutarkyscenarios (200–275 bcm), the
model turns to biogenic methane to compensate for low fossil
gas availability. First, it produces biomethane from straw and
sewage sludge (Fig 14). This implies an extensive biomethane
build-out of more than 30 bcm, aligned with the RePowerEU
target for 2030 (around 35 bcm). Only after exhausting the
biomethane potential does the model replace steam-methane
reforming with electrolysis and scale up hydrogen production
to displace gas in high-temperature industry applications (Fig
2a). As gas consumption falls, carbon emissions decline nearly
linearly, from roughly 2.3 GtCO2 at 450 bcm to 1.8 GtCO 2 at
zero gas use (Fig 24).
Heat Electrification is the Binding Constraint on LNG-
Independence Before 2040
So far, we have characterised the cost-optimal technology mix
at varying fossil gas supply budgets. However, Europe is already
phasing out gas, and incentives to that effect are in place across
all relevant sectors — power, buildings and industry heating.
This raises the question: following current trajectories, when
would Europe become LNG-independent (275 bcm) or fully
autarkic (200 bcm)?
We find that, relative to 2025 installations, the cost-optimal
autarkic scenario requires a doubling of the wind, solar and
heat-pump fleets, as well as the displacement of around 80 bcm
of gas burned for industry heat below 500°C. In the power sector,
current deployment trends indicate that renewable generation
will reach the levels required for gas autarky between 2030 and
2040 (Fig 3a,b). If countries deliver on their National Energy
and Climate Plan targets for 2030, this milestone would be
reached even sooner.
Gas phase-out in buildings and industry lags behind the power
sector. Current building heat-pump trajectories imply autarky-
level displacement only around 2040–2050 (Fig 3c). For industry,
electrification and biomass uptake would need to reach around
75 TWh/a (equivalent to around 7.5 bcm of gas) for a 2035Au-
tarkytarget (Fig 3d). NECP data from 2024 indicate around
150 TWh of gas displacement (around 15 bcm) by 2030, largely
from France and Spain, though EU-level policy does not foresee
substantial industry electrification before 2030 [15, 38].
There is some interchangeability between the sectors that de-
liver these targets. If industry heat fails to phase out gas, the
shortfall would likely be covered by more expensive options,
such as building heat. We find that, without industry electrifica-
tion, reaching 200 bcm of gas consumption (Autarky) becomes
about e10 bn/a more expensive and requires roughly 5–6 mil-
lion additional homes to be equipped with electric heating,
assuming biomass can contribute a further 400 TWh of indus-
try heat (Figure 17).
At a Carbon Price of 100 e/tCO2, Autarky is Cost-Optimal
from a Gas Price of 30e/MWh
It remains unclear where global gas prices will settle in the
long term, but they are unlikely to return to typical pre-2020 or
indeed 20th century levels below 25e/MWh [5]—when the vast
majority of existing gas infrastructure was built [56]. Energy
infrastructure has lifetimes of decades, so the system is too inert
to keep up with changes in commodity prices, a dynamic similar
to “emission lock-in” [57]. As a result, when gas prices spike,
the incumbent capacity build-out commits the energy system
to more gas use than would emerge in a long-term equilibrium.
This effect is likely to be compounded as the second Emissions
Trading Scheme (ETS2) and the Carbon Border Adjustment
Mechanism (CBAM) [58] expands carbon pricing to additional
end-use sectors currently outside the EU ETS, in particular
buildings and road transport [20].
Setting a fossil gas supply constraint, as we do throughout this
paper, lets us explore systems that deviate from the long-term
economically optimal gas consumption (Fig 4), replicating a sys-
tem unable to adjust its long-term infrastructure investment to
short-term price changes. Tracking system costs while varying
gas consumption yields a parabola whose minimum defines the
long-term cost-optimal gas consumption (long-term because in-
vestment is enabled). In other words, for a given gas price, this
is where consumption would settle if it were unconstrained –
where the value of gas to the system equals its price (by duality
in linear programming [59]).
We find that if long-term gas prices settle at 30e/MWh or above,
near-term carbon pricing (100 e/tCO2) drives the system to
autarkic gas-supply levels (Fig 4). Moreover, gas consumption
will only remain above 275 bcm, necessitating LNG imports, if
gas prices return to pre-2020 levels of around 15–25 e/MWh
[56].
5

2020 2025 2030 2035
0
200
400
600
800installed capacity [GW]
Solar PV
73.6 GW/yr
+26%
36.8 GW/yr
-37%
Needed rate of
deployment
Percentage
change
a 2020 2025 2030 2035
0
100
200
300
400
500installed capacity [GW]
Wind
35.2 GW/yr
+156%
17.6 GW/yr
+28%
b
2020 2025 2030 2035
0
10
20
30
40
50
60
70households [million]
Building Electric Heating
6.6 M/yr
+215%
3.3 M/yr
+57%
c 2020 2025 2030 2035
0
200
400
600
800
1000supply volume [TWh/a]
Gas-Displacing
Industry Electrification
and Solid Biomass
NECP Increment for
2030 FR, ES, LU, DK
150.7 TWh/yr 75.4 TWh/yr
d
Cost Optimal Build-Out for...
No LNG (275 bcm)
Autarky (200 bcm)
Autarky by...
2030 2035
current trend
extrapolation
Aggregate 2030 NECPs
Figure 3: Technology roll-out in cost-optimalNo-LNGandAutarkyscenarios relative to early 2020s uptake trends. Wind combines both on- and offshore installation.
Note that solid biomass and electric options already supply heat to industry. The present figure refers only to the additional heat supply needed to displace demand
currently met by gas. In both cases, no consistent trend has been observed over the past years. National Energy and Climate Plan (NECP) targets for 2030 are from
[54, 55]. For 2030 projections of gas-displacing industry electricity and biomass usage, we compare 2020 versus 2030 sector usage in [54]. Both numbers are only
reported for FR, ES, LU, DK and so underrepresent real continent-wide expansion plans.
We find that, accounting for the carbon price, the long-term
elasticity of gas consumption to the external gas price is around
−1.33 (MethodsElasticity, Fig 4). This is a relatively high value
compared with the long-term elasticities reported in the litera-
ture ([60] reports−0.57). However, the frictions captured in em-
pirical work such as [60] (for example capital-stock inertia or im-
perfect information) are omitted in the linear-optimisation mod-
elling used here; a higher value is therefore expected.
Gas Continues to Anchor Electricity Marginal Prices Long
After it Leaves the Bulk Power Mix
A long-standing concern is that, even when gas accounts for
only a small share of the power mix, its price can exert a dispro-
portionate effect on consumer electricity prices. The first mech-
anism driving this is marginal pricing: in Europe’s uniform-
price electricity auctions, the marginal generator sets the clear-
ing price for most dispatched power [61, 62]. The second is the
anchoring of battery dispatch prices to the opportunity cost
of dispatching when gas sets prices [63, 64]. Therefore, phas-
ing out gas power may still fail to shield consumers from that
price. This is directly relevant here: the gas scarcity we simulate
drives the model’s gas shadow price above 100 e/MWh (see
MethodsFossil Gas Supply Constraint and Gas Price).
That battery dispatch prices could be driven by the gas price
might seem counter-intuitive; batteries and demand flexibility
are generally expected to stabilise electricity prices between
near-zero levels — when renewables saturate the market — and
price spikes in the small subset of hours when dispatchable
generators have to recover their investment costs [63]. When
batteries engage in such arbitrage (smoothing intermittent re-
newable supply, and, crucially, preventing backup generation
by thermal plants), the question is at what price they should
discharge. In the logic of capacity-expansion models (such
as PyPSA-Eur), that price is set by the cost of what batteries
displace. When batteries prevent a gas turbine from dispatch-
ing, their effective asking price is the short-run marginal cost
6

0 50 100 150 200 250 300 350 400 450
T otal fossil gas supply [bcm/a]
1120
1140
1160
1180
1200
1220
1240
1260System cost [B /a]
24.6
/MWh
30.7
/MWh
36.9
/MWh
43.0
/MWh
49.1
/MWh
long-term market
equilibrium
Autarky
(200 bcm)
No-LNG
(275 bcm)
T oday's
Demand
Figure 4: System cost under different fossil gas supply constraints and global
gas market prices. These prices are exogenous to the system and do not include
a scarcity rent, unlike in Fig 2b. The gas price range of 24.6–49.1 e/MWh
represents where LNG market prices may settle in the long term. Model runs
are in steps of 50 bcm (see small markers), and the long-term market equilibrium
is derived from quadratic interpolations between them. The minimum of each
parabola refers to the level of gas consumption where the value of gas to the
system coincides with its price (i.e. the scarcity rent is zero), interpretable
as the consumption where the model would settle under idealised market
conditions. The total system cost includes investment, and therefore points on
the parabolas to the right of the optimum represent costs for an energy system
that is slow to adapt to changes in the price signal. Throughout, the model
assumes a carbon price of 100e/tCO2.
(SRMC) of the displaced gas turbine. Thus, even as batteries
push fossil generation out of the system, fossil-fuel prices con-
tinue to influence electricity prices via battery opportunity
costs.
We find that thermal-power marginal costs are the dominant
driver of electricity marginal prices. This emerges from the
distribution of these prices across all network regions and snap-
shots (Figure 5). Even when gas contributes less than 8% of
electricity, we find the marginal price anchored by gas around
50% of the time. An upper structure in the distribution follows
the short-run marginal cost of combined-cycle gas turbines
(CCGTs): it increases roughly linearly with the gas price, with
a slope set by the CCGT efficiency ( 𝜂CCGT ≈ 0.58; red line).
At even tighter fossil gas supply constraints, the distribution
broadens as biomass CHPs become the predominant dispatch-
able power source in the model, and the resulting coupling to
heating-sector marginal prices begins to obscure this relation-
ship.
Consumer Exposure to the Global Gas Price under Present
Gas Use Levels
We assess system- and consumer-cost increase that would occur
during a gas-price hike of the kind driven by contractions in
global gas supply, as in 2022 or 2026. Taking the investment-
optimised model with fossil gas supply 400 bcm as baseline,
we run an “operation-only” case in which the model cannot
change installed capacities but re-optimises dispatch decisions,
reflecting the limited responsiveness of a system facing a short-
term gas-price hike.
0 25 50 75 100 125
Wholesale Marginal Electricity Price [ /MWh]
0
10
20
30
40
50
60
70Network-wide Load-Weighted Gas Price [ /MWh]
 CCGT fuel-only
marginal price
slope = _CCGT  0.58
Wholesale Marginal Electricity Prices
Across Buses and Snapshots
100
0.9%
150
4.0%
175
6.1%
200
7.9%
250
11.8%
300
16.2%
400
21.7%
Gas Consumption
[bcm/a]
Gas Share in Electricity Mix [%]
Figure 5: Distribution of electricity marginal prices across networks under
different fossil gas supply constraints. Each violin shows the distribution
of electricity marginal prices at low-voltage (consumer) buses, with every
bus–snapshot pair contributing one sample. Its 𝑦-position is given by the
network-wide load-weighted gas price, which rises with scarcity as consump-
tion decreases; the right-hand labels give the corresponding gas consumption
and gas share of the electricity mix. The red line shows the fuel-only short-run
marginal cost of combined-cycle gas turbines (CCGT), with slope set by their
efficiency (𝜂CCGT ≈ 0.58). Each network has around 146,000 bus–snapshot
pairs.
We find that a year-round gas-price increase of 1e/MWh raises
consumer costs by ∼8.7 bne (Fig 6; see Methods, “Gas Price
Hike”). This is roughly double what the product of gas vol-
ume and price increase would suggest (400 bcm, i.e. 4,000 TWh,
× 1 e/MWh≈ 4 bne), because electricity marginal prices pass
the higher gas cost through to other generation technologies.
Discussion
Geopolitical uncertainty has highlighted the risk inherent in Eu-
rope’s current level of gas imports and motivated policymakers
to seek options for curbing the continent’s import dependence,
for instance by terminating all imports of Russian fossil fuels
[17]. Eliminating LNG imports (i.e. lowering consumption to
275 bcm, at which demand can be met by domestic produc-
tion and pipeline imports) raises annual system cost by ∼5
bne(<1%). Aligning consumption with European production
capacity alone (∼200 bcm, autarky scenario) raises it by ∼16
bne(<2%).
Electrification of low-temperature industry heat appears to be
the most efficient route for displacing around 50 bcm of gas
use. If industry heat fails to deliver its share of gas phase-out
and the shortfall is covered by building heat and increased
industry biomass heating, autarkic system costs are likely to
increase by e4–10 bn (Figure 17). The central role of industry
heat is driven by high utilisation, which is typical of industry
use and eases the burden of heat pumps’ high investment cost.
Indeed, the techno-economics underlying the model already
appear to capture this advantage. For instance, if the (retail)
electricity price is double the gas price, and the carbon price
is 100 e/tCO2, heat pumps deliver heat at a Levelised Cost of
7

by demand
type
by consumer
group
0
1
2
3
4
5
6
7
8
Consumer energy cost increase during gas-price hike
[bn /a per /MWh gas]
4.3
2.0
1.1
0.6
0.7
3.5
3.0
2.0
0.2
industry processes
other
industry heat
building heat
electricity
agriculture
services
households
industry
8.7
Figure 6: Consumer cost markup during a gas-price hike, i.e., an increase in the
exogenous gas price (interpretable as a rise in global gas markets), disaggregated
by sector and consumer group. Results shown for a system at 400 bcm/a gas
consumption. See Methods for details.
Heat (LCOH) roughly 10–20 e/MWhth lower than a gas boiler
(Fig 10), a finding that aligns with previous research that, under
the same power-gas price ratio, locates the break-even between
gas boilers and heat pumps at 40e/tCO2 [38].
The model’s findings reflect this fundamental trade-off from its
social planner’s perspective. However, translating them to real-
world investment decisions hinges on real-world retail price
ratios reflecting those in the model, in particular for electricity
versus gas. This is not guaranteed. On top of the wholesale
price (mostly captured in the model), real retail prices add grid
fees (partially captured) and taxes (not included), which can
muddle the picture. This holds for both electricity and gas.
Nonetheless, related work suggests the model’s findings are
coherent with the picture emerging in 2025 European Union en-
ergy markets [65] (with increasing 2030 carbon levies poised to
tilt the market further toward heat pumps). The partial perspec-
tive of the model yields electricity-to-gas price ratios similar
to those assessed in Salmon et al. [65], which concentrate be-
tween 2 and 3.2, and identifies large cost-saving electrification
opportunities, similar to those we find here.
Findings on residential heat require the same qualification with
regard to retail energy prices, and their inaccuracy is com-
pounded in the household context by inter-country differences
in heat-pump overnight costs; in CAPEX terms, heat pumps
in Germany are twice as expensive as in the UK (Fig 9). The
present-day assessment of Salmon et al.[65], however, comes to
the same outcome as our study: residential heat pumps roughly
break even with gas boilers with some regional differences (Fig
10). This is because the model captures several of the factors
that drive this heterogeneity. For instance, the model’s tempo-
ral resolution captures cold-spell-driven capacity needs both of
the heating technology and of the grid.
Distribution-grid expansion, a necessary condition for electri-
fication, conceptually follows a logic similar to that of heat
pumps themselves. Its high-CAPEX, low-OPEX cost structure
makes it a smaller economic bottleneck for non-seasonal, high-
load-factor industrial demand (Fig 11 and [ 66]), but it is also
subject to uncertainties that are hard to reflect in linear opti-
misation modelling. Uneven network tariffs across European
countries [65, 66] reflect that build cost, geographic context
and policy structure all play a role in creating an extremely
heterogeneous picture [67, 68]. Overall, both this work and the
related literature assess distribution-grid capex to be a smaller
cost factor than the investment cost of the heat pumps them-
selves [65].
Instead of economics, other factors appear to be the roadblocks
to gas phase-out. For instance, on top of distribution-grid eco-
nomics are hard barriers to industry electrification stemming
from grid-access queue times [ 69]. Around half of surveyed
countries report being unable to integrate further industrial de-
mand [70], and there is wide variation both in the process that
manages access and in the priority given to integrating other
assets, such as renewable generators [ 71]. Industry gas use,
where electrification is most economical, is located in the low-
temperature band. Compared with high-temperature demands,
these industries are more likely to fall below the 20 MWth
heat-demand threshold that would include them in the EU’s
Emissions Trading Scheme (ETS) [20, 72]. This threshold would
effectively be removed in 2028 via the introduction of the ETS2
for most of the remaining sectors [73], likely leading to a further
increase in grid-connection requests.
It is often assumed that similar bottlenecks plague heat-pump
uptake in households, in particular that workforce shortages
constrain it [29]. However, other research contends that the
bottleneck lies elsewhere, and indeed leads back to policy fail-
ure. In Germany, for instance, qualified heat-pump installers
currently complete an average of three installations per person
per year [52]. This is well below the rate this workforce could
sustain, given that a heat-pump installation typically requires
only 4–6 person-days. Similar situations have been observed
in other countries such as the United Kingdom and the Nether-
lands [74, 75], highlighting the role of weak demand pull. A
likely driver is inconsistent policy incentives, which forgo the
potential for a meaningful acceleration in roll-out and likely
manifest as a German heat pump costing twice as much as a
British or Portuguese one (Fig 9).
We further highlight that our findings are conditional on carbon
pricing expanding to previously uncovered sectors, especially
8

building heat and small industries. As found both here and
in other work, carbon pricing critically aligns decarbonisation
with energy-independence efforts [40], and without it fossil-
import reduction pulls domestic fossil energy sources such as
lignite back into the system [39, 76]. This was also observed in
the 2022 gas crisis, during which EU year-on-year coal genera-
tion rose by 7%.
The risk consumers face during these crises should frame the
discussion of the cost of import independence. We find that
currently, at around 400 bcm gas use, consumer bills rise by
∼8.7 bnefor every e/MWh rise in global gas prices. This scale
matches the markup Europe paid during the 2022 gas crisis:
extrapolated to the∼100 e/MWh rise in the 2022 year-average
gas price relative to 2021, it implies a burden on the order of
∼710 bne, close to the 300–400 bne import markup [24] and
the∼700 bne of consumer support deployed that year. We cau-
tion, however, that the model likely overestimates flexibility to
forgo gas in the power sector and underestimates demand elas-
ticity in industry, which in 2022 was the most price-responsive
gas consumer [77]. We therefore find that the cost of theNo-
LNGscenario is lower than the consumer energy burden of a
sustained 1e/MWh rise in gas prices.
Finally, we highlight the need for policy support that ensures
lower gas consumption translates into lower consumer expo-
sure to global gas prices. We find that gas has a large effect
on marginal electricity prices, even when it supplies only a
low-single-digit share of the power mix. Marginal pricing is
what causes the aforementioned superlinear relationship be-
tween external gas prices and consumer cost. This dynamic
will become more pronounced in a future system, in which
electricity increasingly becomes the backbone of energy sup-
ply. Taken together, these dynamics suggest that decoupling
bulk (renewable) electricity generation from marginal prices
(for instance through two-sided CfDs) will likely be crucial to
protect consumers from global gas shocks, even when gas use
has been greatly curbed.
In conclusion, this work shows that Europe’s path away from
gas imports is not only strategically attractive, but also econom-
ically compelling: The cost of achieving import independence
is substantially lower than the risk premium Europe has paid
on those imports since 2022. Moreover, the policy framework
already in place, combined with gas prices prevailing since 2020,
generates enough market incentive to drive gas consumption
down to levels consistent with domestic production capacity
by 2030–35. The remaining challenge for policy is to disman-
tle the regulatory, infrastructural, and informational barriers
that prevent the market from acting on the cost signal it al-
ready receives, and to ensure that curbing gas imports actually
shields energy consumers from their exposure to swings in gas
prices.
Methods
PyPSA-Eur
This work uses the PyPSA-Eur model [ 47], an open-source,
sector-coupled, linear energy-system model of Europe that co-
optimises investment and operation. We run it at a 3-hourly
temporal resolution with a spatial resolution of 50 nodes, cov-
ering the power, heat, biomass, industry, transport and agri-
culture sectors. The study performs an overnight optimisation
of a brownfield system that includes the capacities existing
in 2024 and uses 2024 weather data. No hard limit is placed
on carbon emissions; instead, a carbon price of 100 e/tCO2 is
applied. The model can expand transmission capacity by up to
an additional 25% of current installations. We use the standard
version of the model, with the additional disaggregation of in-
dustry heat demand into distinct temperature bands described
below. Our assumptions on biomass and biogas availability are
largely based on the JRC ENSPRESO dataset, from which we
use theMedium Potentialscenario [49, 78].
The model is based on the PyPSA modelling framework [79]. Its
fundamental logic is a nodal balance, at each node and timestep,
between the energy supplied and the combined withdrawals.
On top of this logic sit energy demands, along with generation,
conversion, storage and energy transport (such as transmission
lines or pipelines). Each has capital and marginal costs and
technical constraints, such as spatial limits on renewable build-
out. When the optimisation problem is solved, a marginal price
of an energy carrier emerges at each node and timestep, the
price of producing one more unit of that carrier at that node
and timestep. This price is a dual variable: the change in the
optimisation’s objective function if another unit were produced
for free. Therefore, it is a close proxy for real marginal price
formation.
Fossil Gas Supply Constraint and Gas Price
The main results of this paper derive from forcing the model to
use specified volumes of fossil gas: the constraint is an equality,
not an upper bound, so the model uses exactly the prescribed
volume. Gas has a uniform price of 24.6 e/MWh, regardless
of its source (except where different gas prices are explored
explicitly, Fig 4). The PyPSA-Eur model works in MWh, i.e.
TWh for larger quantities. For the exposition we however
chose to show natural gas volumes in billion cubic meters (bcm)
instead of TWh, using a simple conversion factor of 10, given
that conventation vary around this value.
On top of the exogenous price, we observe gas prices that
emerge endogenously during optimisation as shadow prices,
and report these in our findings. Though phenomenologically
similar, price formation in the model is not a simulation of
scarcity pricing in a real market. Instead, it is the dual variable
of the fossil gas supply constraint, quantifying the change in
the objective function were the constraint relaxed by one MWh.
It is the price level required to elicit the corresponding level of
fossil gas supply. Similarly, in a real market the willingness to
pay for gas would be driven by the cost of the next-best supply
option.
9

Industry Heat Demand
As a novel feature, we represent industry heat demand in four
distinct temperature bands, estimating the magnitude of each
per region from local industry presence. This estimation takes
regional sectoral industry outputs and multiplies them by the
share of demand that falls in each temperature band. This is
because the technologies available to meet a heating demand are
determined by the quality of the heat. For instance, above 500◦C
only methane and hydrogen are generally applicable. Up to
almost 200◦C, industrial heat pumps are a viable option.
In detail, we start from the JRC IDEES dataset to obtain country-
level industry production outputs in tonnes, covering the sec-
tors shown in Fig 19. The IDEES dataset also includes input
energy-carrier volumes for industry production, and further
includesbest-in-classprocesses—the production pathways most
likely to provide a carbon-neutral variant. For example, in the
steel sector, most current production uses the coke-based ba-
sic oxygen furnace (BOF) route. The carbon-neutral variant is
hydrogen direct reduction (H2-DRI) paired with an electric arc
furnace (EAF), which is emissions-free when green hydrogen is
used. Past versions of PyPSA-Eur make exogenous assumptions
about the roll-out of these technologies, e.g. assuming that by
2035 half of steel is produced by H2-DRI. These assumptions are
then translated into primary energy demands in the model, in
this case mostly coke for BOF, and hydrogen and electricity for
the H2-DRI route. The model then only optimises the supply
of these input commodities.
For heating demands, which make up a large share of the total,
the input carrier providing the heat is interchangeable, provided
it can deliver heat at the required temperature and does not
also serve as a feedstock (as for instance coke does for steel). As
a result, we treat the large majority of industrial heat currently
supplied by solid biomass, gas and waste heat as generic, except
in steel and some chemical production. Fig 20 shows the share
of heating demand per temperature band for each industry
product considered, which we multiply by the total heat input
per tonne of industry product. The total heat input is estimated
from JRC IDEES [80] as the total MWh value of solid biomass,
gas and waste heat.
Since this work focuses on gas consumption, we endogenise
only the heat demand currently met by gas, and assume the
remainder continues to be met by its original carrier. We cannot
know in which temperature band gas heating is deployed; given
its ability to deliver high-quality heat, we assume that, when
heat demand is sorted by temperature, the hottest X% is met
by gas (Fig 21), since among the carriers currently in use it
is the only one that can generically supply high-temperature
heat.
This results in around 1,300 TWh of heat demand currently met
by gas (equivalent to around 130 bcm), of which roughly half
lies below 500◦C, with the remainder in high-temperature or
feedstock uses (see Fig 22). Fig 18 shows how this sub-500 ◦C
demand is distributed across European countries. For compari-
son, Agora estimates total European industry heat demand at
around 1,860 TWh [38]. Both in aggregate and per sector, our
numbers are broadly consistent with this.
We offer the model a range of technologies to meet heat demand
in each temperature band (Tab 1).
Building Heat Demand
Residential and service-sector heat demand is split in each re-
gion into rural, individual urban, and district urban heating.
The split between residential and service-sector demand fol-
lows shares derived from population-weighted national energy
balances (roughly 70% residential, 30% services across Europe);
within each settlement category the two share a common set
of heating technologies but are tracked separately, letting us
attribute consumer costs to either group (see the gas-price hike
analysis below). Each demand is met by a mix of technologies,
typically gas boilers, biomass boilers, heat pumps and solar ther-
mal (see Zeyen et al. [81] for a detailed discussion). See Table 2
for an overview of costs. For heat pumps (air and ground) the
efficiency represents the coefficient of performance, a quantity
that varies by time and region.
The model is brownfield and therefore includes existing heat-
ing capacities.Country aggregates of these are shown in Fig
25.
However, without additional constraints, the model risks over-
estimating consumers’ supply flexibility. Unlike electricity, for
instance, urban individual and rural heat are not traded in liquid
markets in which consumers can make operational decisions
about their supply. Instead, consumers are committed to the
heating technology they have installed (i.e. to their investment
decision). The model is unaware of this and instead tends to
operate a pooled market, in which low-OPEX technologies
provide baseload heat (typically heat pumps) and low-CAPEX
technologies meet demand peaks (typically boilers).
To address this, we constrain heating technologies in urban
individual and rural heat to beload-following, i.e. their partial
load during time𝑡 is bounded above by the relative load𝑙𝑡/𝑙max,
where 𝑙 is that bus’ time series of heat load and 𝑙max is its
maximum (Fig 7). This constrains all technologies to a partial
load of around 25%, and, as we find, yields LCOH values that
align well with the literature (Fig 16). This method is not applied
to district heating, where heat plants can typically modulate, to
some extent, between heat-production pathways [82].
Gas Price Hike
To quantify how a short-term increase in the global gas price
affects system costs and propagates to consumers, we perform
gas-price hikeruns on top of a pre-solved system (Fig 6). Starting
from an investment-optimised network – here a current-day,
gas-dependent system at 400 bcm/a fossil gas supply – we fix
all asset capacities to their optimised values and re-solve the
operational problem only, raising the marginal cost of every
fossil-gas generator by a uniform markupΔ𝑝 (here+1e /MWh).
Crucially, for these runs we relax the fossil-gas consumption
constraint, so that dispatch is free to curb gas wherever the
10

 1
Jan
 1
Feb
 1
Mar
 1
Apr
 1
May
 1
Jun
 1
Jul
 1
Aug
 1
Sep
 1
Oct
 1
Nov
 1
Dec
15 15 15 15 15 15 15 15 15 15 15 15
1000
750
500
250
0
250
500
750
1000
heat balance [GW]
200 bcm
total gas consumption
GAS
urban individual gas boiler
rural gas boiler
district heat gas boiler
OIL
urban individual oil boiler
rural oil boiler
BIOMASS
urban individual biomass boiler
district heat solid biomass CHP
rural biomass boiler
district heat solid biomass CHP CC
ELECTRIC HEATING
urban individual resistive heater
urban individual air heat pump
rural ground heat pump
district heat air heat pump
rural resistive heater
district heat resistive heater
OTHER
Haber-Bosch
other
CONSUMPTION
urban individual heat
rural heat
district heat
agriculture heat
district heat vent
Figure 7: Aggregate heating supply and demand for a model with 200 bcm gas consumption.
Table 1: Technology options for industrial process heat supply by temperature
band (2030 projections). Investment costs are per unit of input capacity and
include the efficiency scaling applied in the model ( 𝑐inv ×𝜂 ). All monetary
values in EUR2020.
Temp. Technology Input𝜼Inv. VOM Source
e/kWin e/MWh
<100°C
Biomass boiler Biomass 0.89 530 2.84 [83]
Gas boiler CH 4 0.93 43 1.01 [83]
Heat pump (med. T) Elec. 2.70 2 118 3.22 [83]
Electric boiler Elec. 0.99 70 0.88 [83]
100–200°C
Biomass boiler Biomass 0.89 530 2.84 [83]
Gas boiler CH 4 0.93 43 1.01 [83]
Heat pump (high T) Elec. 3.05 2 870 3.22 [83]
Electric boiler Elec. 0.99 70 0.88 [83]
200–500°C
Direct firing (solid) Biomass 1.00 222 9.33 § [83, 84]
Direct firing (gas) CH 4 1.00 15 0.28 [83]
H2 combustion H 2 1.00 151 2.79 own est. ∗
>500°C
Direct firing (gas) CH 4 1.00 15 0.28 [83]
H2 combustion H 2 1.00 151 2.79 own est. ∗
All data compiled via [85]. † Incl. post-combustion capture unit at 2.7 Me/(tCO2/h);
90 % capture rate. ‡𝜂reduced by CCS heat demand.
§ Incl. pelletising cost of 9 e/MWh. ∗ Assumed10× gas direct firing cost (no established
reference).
Table 2: Technology options for building heat supply by heat system (2030
projections). Investment costs are per unit of input capacity and include the
efficiency scaling applied in the model (𝑐inv×𝜂). All monetary values in EUR2020.
System Technology Input𝜼Inv. VOM Source
e/kWin e/MWh
Rural
Air-source
heat pump Elec. 3.60 3 238 – [86]
Ground-source
heat pump Elec. 3.90 5 778 – [86]
Resistive heater Elec. 0.90 95 – [85]
Gas boiler CH 4 0.98 308 – [86]
Oil boiler Oil 0.90 149 – [85]
Biomass boiler Biomass 0.86 591 9.00 † [84, 86]
Solar thermal – – 286 ‡ – [85]
Urban indiv.
Air-source
heat pump Elec. 3.60 3 238 – [86]
Resistive heater Elec. 0.90 95 – [85]
Gas boiler CH 4 0.98 308 – [86]
Oil boiler Oil 0.90 149 – [85]
Biomass boiler Biomass 0.86 591 9.00 † [84, 86]
Solar thermal – – 286 ‡ – [85]
District heat
Air-source
heat pump Elec. 3.20 2 900 2.66 [87]
Resistive heater Elec. 0.99 63 1.06 [87]
Gas boiler CH 4 1.04 55 1.06 [87]
Gas CHP CH 4 0.41 / 0.41§ 243 4.44 [87]
Solid biomass
CHP Biomass 0.27 / 0.82 § 957 4.85 [87]
Solar thermal – – 148 ‡ – [85]
All data compiled via [85]. † Wood-pellet supply-chain cost from [84] applied as marginal cost on the biomass input.
‡ Solar thermal collectors enter the model as generators on the heat bus; investment is given ine/m 2 of collector area, not
per kWin.
§ CHP electric / heat efficiency (per unit fuel input). Investment is per kW of fuel input (i.e.𝑐 inv,el×𝜂el); the heat output is
co-produced via the back-pressure coefficient𝑐𝑏 .
11

price increase makes an alternative cheaper. We note, how-
ever, that demand elasticity and fuel-switching options are only
coarsely represented in the model, so this should be read as an
approximate estimate.
Consumer cost is computed as each load’s consumption mul-
tiplied by the nodal marginal (shadow) price of its energy car-
rier, summed over the year, since nodal marginal prices re-
flect the prices seen by consumers. The markup reported in
Fig 6 is the change in this expenditure per unit gas-price in-
crease,(expenditure(Δ𝑝)−expenditure(0))/Δ𝑝 , in bne/a per
e/MWh. We evaluate it directly at Δ𝑝= 1e /MWh, a small
perturbation chosen to keep fossil gas on the price-setting mar-
gin. The response is mildly sub-linear: a large shock would
eventually push gas off the price-setting margin, after which
further increases no longer lift the marginal price; the small
perturbation used here stays in the near-linear regime.
In the main text we disaggregate the markup two ways: once by
energy sector and once by consumer group. For the consumer-
group split, each sector’s expenditure is attributed to house-
holds, services, industry or agriculture, in demand shares de-
rived from population-weighted national energy balances (elec-
tricity split evenly between households and services, building
heat roughly70∶30 between residential and services, while in-
dustrial and agricultural carriers are already separated in the
model).
Elasticity
We use the textbook point definition of the elasticity 𝜖 of a
quantity𝑄with respect to a price𝑃[60]:
𝜖= ln(𝑄∗/𝑄) ln(𝑃∗/𝑃) ,(1)
where(𝑃,𝑄) is the reference operating point and(𝑃∗,𝑄∗) the
perturbed one. The definition can also be expressed in dis-
cretised form as𝜖≈ (Δ𝑄/𝑄)/(Δ𝑃/𝑃) . We evaluate it for gas
consumption responding to the external gas price (Fig 4). We
consider only this demand-side response; the price elasticity
of supply — by which lower consumption would itself depress
the gas price — is not included (see Limitations).
Limitations
The study uses a brownfield model, in which existing capac-
ities in the power sector and building heat are already built.
Since existing assets still have to be paid off during their life-
times, this introduces a slight bias towards using existing assets,
reflecting real-life incentives. However, since existing assets
like gas boilers tend to be CAPEX-light, the model still has
a strong incentive to switch to new technologies with lower
overall costs. A faster boiler phase-out entails more expen-
sive stranding. Capturing this dynamic in an overnight model
would require embedding the cost of asset stranding into the
capital costs of the displacing technology. If gas boilers have a
lifetime of 25 years, the model could split the replacing tech-
nologies into 25 slices, gradually cheapened by the share of
boilers stranded with𝑥 years of lifetime remaining. This is be-
yond the scope of the present study, but could be investigated
in future research.
In industry, real heat-pump prices vary by application size; we
use a single cost value that broadly reflects this range rather
than varying it by size. To examine this, we plot the competi-
tive advantage of heat pumps over gas boilers as a function of
demand-profile shape and the ratio of electricity to gas prices
(Fig 10). As expected, heat demands that are unevenly spread,
i.e. have a low load factor (as arises from seasonality or cold
spells), work against heat-pump economics. This is because
the heating asset is sized by peak rather than average demand,
and heat pumps, which are high-CAPEX and low-OPEX, are
less suited to this configuration. Placing the model’s commod-
ity prices and demand profiles on this map, we see that in
industry heat pumps hold a firm advantage of 10–20 e/MWhth,
while in residential heat they roughly break even with gas
boilers.
The study assesses a broad range of gas consumption levels,
set within a background system that aims to reflect 2030–35.
We chose to include extremes in the range of gas consumption
levels assessed, spanning from zero fossil gas consumption up
to mid-2020s levels of 350–450 bcm/a. These extremes are im-
plausible outcomes for the 2030s, lying far outside the expected
range [15]. They further complicate validation against heat
supply (Fig 12), as it is likely the higher electricity availability
in the 2030s that causes the model to overestimate electric heat
supply, even given the inclusion of the existing heating fleet.
In spite of these drawbacks, we believe the value of isolating
the impact of gas consumption justifies forgoing a framing in
which gas phase-out co-evolves with the wider system, which
would introduce substantial noise into the analysis.
The study relies on a single weather year for 2024 to capture
recent climate conditions. However, this misses inter-annual
weather variation that could change renewable generation, de-
mand and heat-pump capacity factors, and thereby affect the
economics of the building-heat and power sectors. We find
that the COPs and capacity factors, on average, represent a
typical weather year (Fig 26). That said, there was a cold spell
during January 2024. Demand spikes are more burdensome for
heat-pump economics, both because heat pumps are CAPEX-
intensive and because they require expansion of the distribution
grid. This could introduce a bias against gas phase-out in build-
ing heat. On balance, however, we believe this to be a small
effect, as it is mostly localised to northern regions, which host
only a small minority of demand; moreover, geographically
driven hydropower availability is likely to offset the unusually
high demand, as indicated by the low northern electricity prices
(see Fig 23).
Real consumer decisions are based on costs that cannot be fully
represented within the current logic of the PyPSA-Eur model.
This plays a notable role in the case of electrification, where
the cost balance between gas boilers and electric alternatives
could be skewed. For one, the wholesale electricity price—best
represented in the model—makes up only a third of the con-
12

sumer price. Investment in the transmission and distribution
grids is factored into the model’s heat-pump economics, and
could be added here ex-post. However, through its annuitised
formulation, it is constrained to represent grid cost as a markup
of only the network additions needed and delivered within that
year. This does not align with the per-kWh grid tariffs faced by
some consumers. For consumers, grid tariffs remunerate both
the sunk costs of past investment and front-loaded investment
in the future grid. A further share of consumer electricity costs
consists of utility margins and taxes, neither of which is repre-
sented here; overall, however, the macroscopic cost landscape
aligns with the literature (see Discussion).
In industry heating, the endogenisation of heat supply disaggre-
gates demand by temperature alone, abstracting from other pro-
cess characteristics that can bear on the choice of low-carbon
alternative. For instance, many processes below 500°C are sup-
plied via steam, for which an electric boiler or high-temperature
heat pump is a natural substitute. Kilns, by contrast, transfer
heat to the product directly rather than through steam, so their
alternatives must accommodate this mode of heat delivery. For
some products, neglecting these distinctions could misrepresent
the true cost of alternatives. However, the process tempera-
ture remains the dominant determinant of the cost structure
of both incumbent supply and its alternatives [ 25]. Future
work could disaggregate industry heat demand further and,
on a process-by-process basis, offer the model more tailored
alternatives.
CRediT authorship contribution statement
Lukas Franken:Writing – original draft, Writing – review &
editing, Visualization, Validation, Software, Methodology, In-
vestigation, Formal analysis, Conceptualization.Iegor Riepin:
Writing – review & editing, Conceptualization, Methodology,
Project administration.Tom Brown:Writing – review & edit-
ing, Conceptualization, Methodology, Funding acquisition.
Declaration of Competing Interests
The authors declare no competing interests.
Acknowledgements
We thank Bobby Xiong, Anne Neumann, Markus Millinger,
Fabian Neumann, Tobias Fleiter, Khaled Al-Dabbas and Iris
Rieth-Menze for fruitful discussions.
Funding Statements
L.F. and I.R. acknowledge support by the Federal Ministry for
Economic Affairs and Energy of Germany (BMWE) jointly
with the CETPartnership through the Joint Call 2022. As such,
L.F. and I.R. further acknowledge funding from the European
Union’s Horizon Europe research and innovation programme
under grant agreement no. 101069750.
Data availability
The open source code and data to reproduce our experiments,
including the download and installation of data and software
dependencies, are available on GitHub under the MIT license at
https://github.com/LukasFrankenQ/resil
ient-pypsa-eur.
References
[1] Eurostat, Simplified energy balances (nrg_bal_s), Online
data code, European Commission, 2024. URL:https://ec.e
uropa.eu/eurostat/databrowser/view/nrg_bal_s/default/t
able, accessed 2026-05-25.
[2] Department for Business, Energy and Industrial Strategy,
Energy Consumption in the UK (ECUK) 1970 to 2020, Tech-
nical Report, UK Government, BEIS, 2021. URL:https:
//www.gov.uk/government/statistics/energy-consu
mption-in-the-uk-2021.
[3] Norwegian Petroleum Directorate, Exports of Norwegian
oil and gas, norskpetroleum.no, 2024. URL:https://www.
norskpetroleum.no/en/production-and-exports/expor
ts-of-oil-and-gas/, Norway exports ∼30% of EU+UK gas
consumption in 2024.
[4] G. Boccara, D. Hernandez Diaz, B. Heringa, O. Rolser,
N. Sharma, T. Vahlenkamp, C. Xue, A balancing act: Se-
curing European gas and power markets, McKinsey &
Company (2023). URL:https://www.mckinsey.com/industr
ies/oil-and-gas/our-insights/a-balancing-act-securing-e
uropean-gas-and-power-markets, accessed: 2026-03-05.
[5] Trading Economics, EU Natural Gas – TTF Gas Prices, 2026.
URL:https://tradingeconomics.com/commodity/eu-natur
al-gas.
[6] P. Graichen, Wie gefährlich ist Deutschlands Gasab-
hängigkeit wirklich?, 2026. URL:https://steady.page/
de/climate-and-energy-blog/posts/5afee861-6b78-413
f-ab73-b07b5b57f22b, von Mauern und Windmühlen: Ein
Energieblog (Steady).
[7] M. Gillot, Endgame for gas dependence: Electrification and
regional partnerships, 2026. URL:https://strategicperspec
tives.eu/a-credible-gas-endgame-for-europe-electrificati
on-and-regional-partnerships/.
[8] J. Rosenow, War in the Middle East hands Europe another
chance to break its fossil fuel dependency, Nature Energy
(2026). doi:10.1038/s41560-026-02048-z.
[9] S. Zwickl-Bernhard, C. K. Chyong, A. Creti, A. Neumann,
J. Rosenow, Closure of the Strait of Hormuz fuels Europe’s
natural-gas trilemma, One Earth 9 (2026) 101717. doi:10.1
016/j.oneear.2026.101717, commentary.
13

[10] Eurostat, Supply, transformation and consumption of gas
– monthly data (nrg_cb_gasm), Online data code, European
Commission, 2024. URL:https://ec.europa.eu/eurostat/
databrowser/view/nrg_cb_gasm/default/table, inland
consumption (IC_OBS), natural gas (G3000), TJ (GCV). Ac-
cessed 2026-06-02.
[11] Eurostat, Complete energy balances (nrg_bal_c), Online
data code, European Commission, 2024. URL:https://ec.e
uropa.eu/eurostat/databrowser/view/nrg_bal_c/default/t
able, sectoral natural-gas demand split (power, buildings,
industry). Accessed 2026-06-02.
[12] Oxford Institute for Energy Studies, Quarterly Gas Review
– Issue 29, Quarterly Gas Review 29, Oxford Institute for
Energy Studies, 2024. URL:https://www.oxfordenergy.org
/publications/quarterly-gas-review-29/.
[13] Hotmaps project, Industrial sites – industrial database,
Open dataset, GitLab, 2019. URL:https://gitlab.com/hotma
ps/industrial_sites/industrial_sites_Industrial_Database,
locations and emissions of energy-intensive industrial sites
(chemicals, refineries, iron and steel, cement). Accessed
2026-06-02.
[14] OpenStreetMap contributors, OpenStreetMap,https://ww
w.openstreetmap.org, 2024. Data available under the Open
Database License (ODbL).
[15] European Commission, REPowerEU Plan, Communica-
tion COM(2022) 230 final, European Commission, Brussels,
2022. URL:https://eur-lex.europa.eu/legal-content/EN/TX
T/?uri=celex:52022DC0230.
[16] European Commission, ‘Fit for 55’: delivering the EU’s
2030 Climate Target on the way to climate neutrality, Com-
munication from the Commission to the European Par-
liament, the Council, the European Economic and Social
Committee and the Committee of the Regions COM(2021)
550 final, European Commission, Brussels, 2021. URL:https:
//eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:
52021DC0550.
[17] European Commission, EU agrees to permanently stop
Russian gas imports and phase out Russian oil, Press release
IP/25/2860, 2025. URL:https://ec.europa.eu/commission/pr
esscorner/detail/en/ip_25_2860.
[18] A. Corsoni-Husain, A. Lanitis, EU publishes Regulation
phasing out Russian gas and oil imports, Harneys Regula-
tory Blog, 2026. URL:https://www.harneys.com/our-blogs
/regulatory/eu-publishes-regulation-phasing-out-russian
-gas-and-oil-imports/.
[19] European Commission, AccelerateEU – Energy Union: Af-
fordable and Secure Energy through Accelerated Action,
Communication COM(2026) 370 final, European Commis-
sion, Brussels, 2026. URL:https://energy.ec.europa.eu/publ
ications/accelerateeu-energy-union-affordable-and-sec
ure-energy-through-accelerated-action_en.
[20] European Parliament and Council of the European Union,
Directive (EU) 2023/959 of the European Parliament and of
the Council of 10 May 2023 amending Directive 2003/87/EC
establishing a system for greenhouse gas emission al-
lowance trading within the Union and Decision (EU)
2015/1814 concerning the establishment and operation of
a market stability reserve for the Union greenhouse gas
emission trading system,https://eur-lex.europa.eu/eli/dir
/2023/959/oj, 2023. Establishes ETS2 (Chapter IVa) for fuel
combustion in buildings, road transport and additional sec-
tors (small industry outside ETS1); revises the small-emitter
opt-outs; introduces the CBAM free-allocation phase-out
factor.
[21] UK Government, The greenhouse gas emissions trading
scheme order 2020,https://www.legislation.gov.uk/ukdsi/2
020/9780348209761/contents, 2020. SI 2020/1265.
[22] Council of European Energy Regulators, Status Review of
Renewable Support Schemes in Europe for 2022 and 2023,
CEER Report C24-RES-84-05, CEER, Brussels, 2025. URL:
https://www.ceer.eu/wp-content/uploads/2025/07/RES_s
tatus_review_2022_2023_C24-RES-84-05_final.pdf.
[23] European Heat Pump Association, Subsidies for residential
heat pumps in Europe, Technical Report, EHPA, Brussels,
2023. URL:https://www.ehpa.org/wp-content/uploads/202
3/03/EHPA_Subsidies-for-residential-heat-pumps-in-Eur
ope_FINAL_April-2023.pdf.
[24] International Energy Agency, Europe’s energy crisis:
What factors drove the record fall in natural gas demand
in 2022?, Commentary, IEA, Paris, 2023. URL:https://www.
iea.org/commentaries/europes-energy-crisis-what-facto
rs-drove-the-record-fall-in-natural-gas-demand-in-2022,
sectoral decomposition of the 13% drop in EU gas demand
in 2022 across power, buildings and industry.
[25] S. Madeddu, F. Ueckerdt, M. Pehl, J. Peterseim, M. Lord,
K. A. Kumar, C. Krüger, G. Luderer, The CO 2 reduction
potential for the European industry via direct electrification
of heat supply (power-to-heat), Environmental Research
Letters 15 (2020) 124004. doi:10.1088/1748-9326/abbd02.
[26] C. Rosslowe, N. Fulghum, B. Petrovich, et al., European
Electricity Review 2025, Technical Report, Ember, Brussels,
2025. URL:https://ember-energy.org/latest-insights/euro
pean-electricity-review-2025/.
[27] International Energy Agency, Electricity 2026: Analysis
and Forecast to 2027, Technical Report, IEA, Paris, 2026.
URL:https://www.iea.org/reports/electricity-2026.
[28] European Heat Pump Association, European Heat Pump
Market and Statistics Report 2025, Technical Report, Euro-
pean Heat Pump Association (EHPA), Brussels, 2025. URL:
https://www.ehpa.org/wp-content/uploads/2025/07/EHP
A-Market-Report-2025-executive-summary.pdf.
14

[29] International Energy Agency, The Future of Heat Pumps,
Technical Report, International Energy Agency, Paris, 2022.
URL:https://www.iea.org/reports/the-future-of-heat-pum
ps.
[30] M. Rehfeldt, S. Bußmann, T. Fleiter, J. Rissman, Direct
electrification of industrial process heat: An assessment of
technologies, potentials and future prospects for the EU,
Study, Fraunhofer Institute for Systems and Innovation
Research ISI, Karlsruhe, Germany, 2024. URL:https://www.
agora-industry.org, on behalf of Agora Industry.
[31] A. Odenweller, F. Ueckerdt, The green hydrogen ambition
and implementation gap, Nature Energy 10 (2025) 110–123.
[32] International Energy Agency, Global Hydrogen Review
2024, Technical Report, IEA, Paris, 2024. URL:https://www.
iea.org/reports/global-hydrogen-review-2024.
[33] IRENA, Methanol Institute, Innovation Outlook: Renew-
able Methanol, Technical Report, International Renewable
Energy Agency, Abu Dhabi, 2021. URL:https://www.irena.
org/publications/2021/Jan/Innovation-Outlook-Renewab
le-Methanol.
[34] U.S. Energy Information Administration, Hydrogen for
refineries is increasingly provided by industrial suppliers,
Today in Energy, 2015. URL:https://www.eia.gov/todayine
nergy/detail.php?id=24612.
[35] International Energy Agency, The Future of Petrochem-
icals: Towards more sustainable plastics and fertilisers,
Technical Report, IEA, Paris, 2018. URL:https://www.iea.
org/reports/the-future-of-petrochemicals.
[36] H. Fehrenbach, M. Pehnt, Biomethane in Europe, Tech-
nical Report, Institut für Energie- und Umweltforschung
Heidelberg (ifeu), Heidelberg, Germany, 2022. URL:https:
//www.ifeu.de/fileadmin/uploads/ifeu_ECF_biomethane_
EU_final_01.pdf.
[37] Agora Energiewende, Breaking Free from Fossil Gas: A
New Path to a Climate-Neutral Europe, Technical Report,
Agora Energiewende, Berlin, 2023. URL:https://www.agor
a-energiewende.org/publications/breaking-free-from-fos
sil-gas.
[38] Agora Industry, Agora Energiewende, Fraunhofer ISI,
ECCO Think Tank, Reform Institut, The business case
for electrifying industrial heat: Evidence from selected
EU Member States, Technical Report, Agora Industry and
Agora Energiewende, Berlin, Germany, 2026. URL:https:
//www.agora-industry.org/publications/the-business-cas
e-for-electrifying-industrial-heat.
[39] T. T. Pedersen, E. K. Gøtske, A. Dvorak, G. B. Andresen,
M. Victoria, Long-term implications of reduced gas imports
on the decarbonization of the European energy system,
Joule 6 (2022) 1566–1580. doi:10.1016/j.joule.2022.06.023.
[40] J. Jewell, V. Vinichenko, D. McCollum, N. Bauer, K. Riahi,
T. Aboumahboub, O. Fricko, M. Harmsen, T. Kober, V. Krey,
et al., Comparison and interactions between the long-term
pursuit of energy independence and climate policies, Na-
ture Energy 1 (2016) 16073.
[41] Fraunhofer Institute for Solar Energy Systems ISE, Net
electricity generation in Germany in 2022: Significant in-
crease in generation from wind and PV, Press release, Fraun-
hofer ISE, Freiburg, 2023. URL:https://www.ise.fraunhofer
.de/en/press-media/press-releases/2023/net-electricity-g
eneration-in-germany-in-2022-significant-increase-in-g
eneration-from-wind-and-pv.html.
[42] M. Hafner, G. Luciani, Italy and its North African gas
interconnections, Energy Comment, Oxford Institute for
Energy Studies, 2023. URL:https://www.oxfordenergy.o
rg/wpcms/wp-content/uploads/2023/03/Italy-and-its-N
orth-African-gas-interconnections.pdf, TransMed and
Greenstream capacities. Accessed: 2026-05-25.
[43] Trans Adriatic Pipeline AG, How TAP operates, TAP AG
corporate website, 2026. URL:https://www.tap-ag.com/
infrastructure-operation/how-tap-operates, operational
capacity 10 bcm/a, expandable to 20 bcm/a; +1.2 bcm/a
from January 2026. Accessed: 2026-05-25.
[44] L. M. Pastore, G. Lo Basso, L. de Santoli, Towards a dra-
matic reduction in the European natural gas consumption:
Italy as a case study, Journal of Cleaner Production 369
(2022) 133377. doi:10.1016/j.jclepro.2022.133377.
[45] J. Hörsch, F. Hofmann, D. Schlachtberger, T. Brown,
PyPSA-Eur: An open optimisation model of the European
transmission system, Energy Strategy Reviews 22 (2018)
207–215.
[46] T. Brown, D. Schlachtberger, A. Kies, S. Schramm,
M. Greiner, Synergies of sector coupling and transmis-
sion reinforcement in a cost-optimised, highly renewable
European energy system, Energy 160 (2018) 720–739.
[47] F. Neumann, E. Zeyen, M. Victoria, T. Brown, The poten-
tial role of a hydrogen network in Europe, Joule 7 (2023)
1793–1817. doi:10.1016/j.joule.2023.06.016.
[48] A. Nikas, N. Frilingou, C. Heussaff, P. Fragkos, S. Mittal,
J. Sampedro, S. Giarola, J.-P. Sasse, L. Rinaldi, H. Doukas,
et al., Three different directions in which the European
Union could replace Russian natural gas, Energy 290 (2024)
130254.
[49] M. Millinger, F. Hedenus, E. Zeyen, F. Neumann, L. Re-
ichenberg, G. Berndes, Diversity of biomass usage path-
ways to achieve emissions targets in the European energy
system, Nature Energy 10 (2025) 226–242.
[50] P. Glaum, F. Neumann, M. Millinger, T. Brown, A minimal
methanol backstop for high-electrification scenarios, Joule
(2026) 102464. doi:10.1016/j.joule.2026.102464.
15

[51] E. D. Vicente, C. A. Alves, An overview of particulate emis-
sions from residential biomass combustion, Atmospheric
Research 199 (2018) 159–185. doi:10.1016/j.atmosres.2017.
08.027.
[52] P. P. Altermatt, J. Clausen, H. Brendel, C. Breyer, C. Ger-
hards, C. Kemfert, U. Weber, M. Wright, Replacing gas
boilers with heat pumps is the fastest way to cut German
gas consumption, Communications Earth & Environment
4 (2023) 56.
[53] International Energy Agency, Levelized cost of heating
(LCOH) for consumers, for selected space and water heat-
ing technologies and countries, 2021. URL:https://www.
iea.org/data-and-statistics/charts/levelized-cost-of-h
eating-lcoh-for-consumers-for-selected-space-and-w
ater-heating-technologies-and-countries, chart only;
methodology not fully documented. Closest publicly avail-
able cross-country consumer LCOH comparison.
[54] Ember, A power sector analysis of the draft national en-
ergy and climate plans (NECPs), Dataset and report, 2024.
URL:https://ember-energy.org/latest-insights/draft-nec
ps-put-eu-shortofrepowereu/, country-level installed ca-
pacity and generation targets for 2025, 2030, 2040 and 2050
extracted from EU Member States’ draft updated NECPs.
[55] Department for Energy Security and Net Zero, Clean
Power 2030 Action Plan: A New Era of Clean Electric-
ity, Technical Report, UK Government, London, 2024. URL:
https://www.gov.uk/government/publications/clean-p
ower-2030-action-plan/clean-power-2030-action-plan-a
-new-era-of-clean-electricity-main-report, 2030 capac-
ity ranges: solar PV 45–47 GW; onshore wind 27–29 GW;
offshore wind 43–50 GW.
[56] ACER, CEER, Annual Report on the Results of Monitor-
ing the Internal Electricity and Natural Gas Markets in
2020 – Gas Wholesale Markets Volume, Technical Report,
European Union Agency for the Cooperation of Energy
Regulators, Ljubljana, 2021. URL:https://www.ceer.eu/wp
-content/uploads/2024/05/ACER-Market-Monitoring-Rep
ort-2020-Gas-Wholesale-Markets-Volume.pdf.
[57] D. Tong, Q. Zhang, Y. Zheng, K. Caldeira, C. Shearer,
C. Hong, Y. Qin, S. J. Davis, Committed emissions from ex-
isting energy infrastructure jeopardize 1.5◦C climate target,
Nature 572 (2019) 373–377.
[58] S. Zwickl-Bernhard, A. Creti, A. Neumann, The EU’s
CBAM trinity in LNG supply: Modeling global trade flows,
supply risks and upstream emissions, Energy Economics
157 (2026) 109252. doi:10.1016/j.eneco.2026.109252.
[59] S. Boyd, L. Vandenberghe, Convex Optimization, Cam-
bridge University Press, Cambridge, UK, 2004. See Ch. 5 on
duality and Ch. 5.6 on perturbation and sensitivity analysis.
[60] X. Labandeira, J. M. Labeaga, X. López-Otero, A meta-
analysis on the price elasticity of energy demand, Energy
Policy 102 (2017) 549–568. doi:10.1016/j.enpol.2017.01.002.
[61] B. Zakeri, I. Staffell, P. E. Dodds, M. Grubb, P. Ekins,
J. Jääskeläinen, S. Cross, K. Helin, G. Castagneto Gissey,
The role of natural gas in setting electricity prices in Eu-
rope, Energy Reports 10 (2023) 2778–2792. doi:10.1016/j.eg
yr.2023.09.069.
[62] T. Schittekatte, C. Batlle, Power Crisis in the EU 3.0: Pro-
posals to Complete Long-Term Markets, CEEPR Working
Paper 2023-04, MIT Center for Energy and Environmen-
tal Policy Research, Cambridge, MA, 2023. URL:https:
//ceepr.mit.edu/wp-content/uploads/2023/02/MIT-CEE
PR-WP-2023-04.pdf.
[63] T. Brown, F. Neumann, I. Riepin, Price formation without
fuel costs: The interaction of demand elasticity with storage
bidding, Energy Economics 147 (2025) 108483.
[64] J. Geis, M. Lindner, T. Brown, Managing the mismatch:
The role of flexibility on the path to a carbon-neutral energy
system, arXiv preprint arXiv:2604.00674 (2026).
[65] N. Salmon, O. Alšauskas, S. Harmsen, S. Bouckaert, The
energy crisis creates even stronger impetus for EU electri-
fication, IEA Commentary, International Energy Agency,
Paris, 2026. URL:https://www.iea.org/commentaries/the-e
nergy-crisis-creates-even-stronger-impetus-for-eu-elect
rification, licence: CC BY 4.0. Accessed 2026-06-14.
[66] D. Arlia, J. Hutchinson, Drivers of electricity prices across
households and energy-intensive industries and their im-
portance for the EU’s decarbonisation objectives, in: ECB
Economic Bulletin, 1, European Central Bank, 2026. URL:
https://www.ecb.europa.eu/press/economic-bulletin/fo
cus/2026/html/ecb.ebbox202601_02~a552b71378.en.html,
published 17 February 2026.
[67] T. Schittekatte, I. Momber, L. Meeus, Future-proof tar-
iff design: Recovering sunk grid costs in a world where
consumers are pushing back, Energy Economics 70 (2018)
484–498. doi:10.1016/j.eneco.2018.01.028.
[68] MIT Energy Initiative, Utility of the Future: An MIT En-
ergy Initiative Response to an Industry in Transition, Tech-
nical Report, MIT Energy Initiative and IIT-Comillas, Cam-
bridge, MA, 2016. URL:https://energy.mit.edu/wp-content
/uploads/2016/12/Utility-of-the-Future-Full-Report.pdf,
principal investigators: I. Pérez-Arriaga and C. Knittel.
[69] European Commission, Commission notice — guidance
on efficient and timely grid connections, Official Journal
of the European Union, CELEX:52025XC06703, 2025. URL:
https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=C
ELEX:52025XC06703, Brussels, 10 December 2025.
[70] E. Cremona, Crossed Wires: Grid Capacity Could Block
EU Energy Security, Technical Report, Ember, 2026. URL:
https://ember-energy.org/latest-insights/crossed-wires-g
rid-capacity-could-block-eu-energy-security/, accessed:
2026-04-15.
16

[71] Eurelectric, From Backlog to Breakthrough: Managing
Connection Queues in Distribution Networks, Technical
Report, Eurelectric, Brussels, 2025. URL:https://www.eure
lectric.org/wp-content/uploads/2025/04/From-Backlog-t
o-Breakthrough-Managing-Connection-Queues-in-Distr
ibution-Networks.cleaned.pdf.
[72] German Emissions Trading Authority (DEHSt), Umwelt-
bundesamt, Relief for small emitters 2026 to 2030, Deutsche
Emissionshandelsstelle (DEHSt), 2024. URL:https://www.
dehst.de/EN/Topics/EU-ETS-1/Stationary/Small-Emitters
-2026-2030/small-emitters-2026-2030_node.html, national
Art. 27 implementation: installations below 15,000 t CO2-
eq in each of 2021–2023 qualify as small emitters; re-entry
into full obligations above 25,000 t/yr; exemption condi-
tional on an equivalent measure (compensation payment
or plant-specific reduction).
[73] European Commission, Directorate-General for Climate
Action, ETS2: buildings, road transport and additional sec-
tors, European Commission, Climate Action, 2026. URL:
https://climate.ec.europa.eu/eu-action/carbon-markets/e
ts2-buildings-road-transport-and-additional-sectors_en,
upstream cap-and-trade: the surrender obligation falls on
fuel suppliers, not end-users; allowances fully auctioned
(no free allocation). Full operation postponed from 2027 to
1 January 2028 (Council/Parliament agreement of Novem-
ber 2025, adopted 2026). Scope = combustion not covered
by ETS1 (CRF 1A1 energy industries, 1A2 manufacturing
and construction, 1A4 buildings, 1A3b road transport).
[74] Nesta, How to Install More Heat Pumps: Insights from
a Survey of Heating Engineers, Technical Report, Nesta,
London, 2024. URL:https://www.nesta.org.uk/report/ho
w-to-install-more-heat-pumps-insights-from-a-surve
y-of-heating-engineers/.
[75] European Heat Pump Association, Dutch heat pump in-
dustry responds to cancellation of 2026 legislation, Press
release, European Heat Pump Association (EHPA), 2024.
URL:https://ehpa.org/news-and-resources/press-releases/
dutch-heat-pump-industry-responds-to-cancellation-o
f-2026-legislation/.
[76] M. Victoria, K. Zhu, T. Brown, G. B. Andresen, M. Greiner,
Early decarbonisation of the European energy system pays
off, Nature Communications 11 (2020) 6223. doi:10.1038/s4
1467-020-20015-4.
[77] O. Ruhnau, C. Stiewe, J. Muessel, L. Hirth, Natural gas
savings in Germany during the 2022 energy crisis, Nature
Energy 8 (2023) 621–628. doi:10.1038/s41560-023-01260-5.
[78] P. Ruiz, W. Nijs, D. Tarvydas, A. Sgobbi, A. Zucker,
R. Pilli, R. Jonsson, A. Camia, C. Thiel, C. Hoyer-Klick,
F. Dalla Longa, T. Kober, J. Badger, P. Volker, B. S. Elbersen,
A. Brosowski, D. Thrän, ENSPRESO – an open, EU-28
wide, transparent and coherent database of wind, solar and
biomass energy potentials, Energy Strategy Reviews 26
(2019) 100379. doi:10.1016/j.esr.2019.100379.
[79] T. Brown, J. Hörsch, D. Schlachtberger, PyPSA: Python
for power system analysis, arXiv preprint arXiv:1707.09913
(2017).
[80] M. Rózsai, M. Jaxa-Rozen, R. Salvucci, P. Sikora, J. Tattini,
F. Neuwahl, JRC-IDEES-2021: the Integrated Database of
the European Energy System — Data update and technical
documentation, JRC Technical Report JRC137809, Publi-
cations Office of the European Union, Luxembourg, 2024.
doi:10.2760/614599.
[81] E. Zeyen, V. Hagenmeyer, T. Brown, Mitigating heat de-
mand peaks in buildings in a highly renewable European
energy system, Energy 231 (2021) 120784.
[82] H. Lund, S. Werner, R. Wiltshire, S. Svendsen, J. E. Thorsen,
F. Hvelplund, B. V. Mathiesen, 4th Generation District
Heating (4GDH): Integrating smart thermal grids into fu-
ture sustainable energy systems, Energy 68 (2014) 1–11.
doi:10.1016/j.energy.2014.02.089.
[83] Danish Energy Agency, Technology Data for Industrial
Process Heat, Technical Report, Danish Energy Agency,
2020. URL:https://ens.dk/en/analyses-and-statistics/tech
nology-data-industrial-process-heat, version 5, accessed
2024.
[84] L. Visser, R. Hoefnagels, M. Junginger, Wood pellet supply
chain costs – a review and cost optimization analysis, Re-
newable and Sustainable Energy Reviews 118 (2020) 109506.
doi:10.1016/j.rser.2019.109506.
[85] M. Victoria, K. Zhu, T. Brown, E. Zeyen, et al., PyPSA
technology-data: Compiled assumptions on energy system
technologies, 2024. URL:https://github.com/PyPSA/techn
ology-data, v0.12.0.
[86] Danish Energy Agency, Technology Data for Heating In-
stallations, Technical Report, Danish Energy Agency, 2018.
URL:https://ens.dk/en/analyses-and-statistics/technology
-catalogues, accessed 2024.
[87] Danish Energy Agency, Technology Data for Generation
of Electricity and District Heating, Technical Report, Dan-
ish Energy Agency, 2024. URL:https://ens.dk/en/analyses
-and-statistics/technology-data-generation-electricity-a
nd-district-heating, accessed 2024.
[88] HeatPumpsWatch, Heat pump installation costs: Germany
vs. Europe, 2026. URL:https://heatpumpswatch.org/hea
t-pump-installation-costs-germany-vs-europe/, cross-
country residential heat-pump installed costs. Accessed
2026-06-08.
[89] UK Department for Energy Security and Net Zero, Boiler
upgrade scheme statistics, 2025. URL:https://www.gov.uk/g
overnment/collections/boiler-upgrade-scheme-statistics,
average installed heat-pump cost, Oct–Dec 2025. Accessed
2026-06-08.
17

[90] A. Marina, S. Spoelstra, H. A. Zondag, A. K. Wemmers, An
estimation of the European industrial heat pump market
potential, Renewable and Sustainable Energy Reviews 139
(2021) 110545. doi:10.1016/j.rser.2020.110545.
[91] H. Pieper, T. Ommen, B. Elmegaard, W. Brix Markussen,
Allocation of investment costs for large-scale heat pumps
supplying district heating, in: Energy Procedia (CONECT
2018), volume 147, 2018, pp. 358–367. URL:https://backen
d.orbit.dtu.dk/ws/portalfiles/portal/150813986/CONECT_
Pieper_Allocation_of_investment_costs_for_large_scale_
heat_pumps.pdf.
[92] International Energy Agency, Levelised cost of production
for heat pumps in selected countries/regions by type, 2023,
2023. URL:https://www.iea.org/data-and-statistics/charts
/levelised-cost-of-production-for-heat-pumps-in-selecte
d-countriesregions-by-type-2023, industrial process-heat
heat pumps. Accessed 2026-06-08.
[93] Eurostat, Energy consumption in households (nrg_d_hhq),
2023. URL:https://ec.europa.eu/eurostat/databrowser/vi
ew/nrg_d_hhq/, share of fuels in residential space heating,
EU-27. Accessed 2026-06-08.
[94] ODYSSEE-MURE (Enerdata/ADEME), Heating energy
consumption by energy sources, 2023. URL:https://ww
w.odyssee-mure.eu/, EU-27 household heating fuel mix.
Accessed 2026-06-08.
[95] Regulatory Assistance Project, The role of district heating
in the European energy system, 2017. URL:https://www.
raponline.org/, EU district-heating fuel mix (via European
Commission). Accessed 2026-06-08.
[96] Office for National Statistics, Census 2021: Type of central
heating in households, England and Wales, 2021. URL:https:
//www.ons.gov.uk/peoplepopulationandcommunity/hous
ing, main heating-fuel shares. Accessed 2026-06-08.
[97] Norwegian Ministry of Energy, Energifakta Norge: Energy
use, 2024. URL:https://energifaktanorge.no/en/, household
heating, electricity-dominated. Accessed 2026-06-08.
[98] T. Fleiter, J. Fragoso, B. Lux, Ş. Alibaş, K. Al-Dabbas,
P. Manz, F. Neuner, B. Weißenburger, M. Rehfeldt, F. Sens-
fuß, Hydrogen infrastructure in the future CO2-neutral
European energy system—how does the demand for hydro-
gen affect the need for infrastructure?, Energy Technology
13 (2025) 2300981. doi:10.1002/ente.202300981.
Appendix
18

0 50 100 150 200 250 300 350 400
T otal fossil gas supply [bcm/a]
0
500
1000
1500
2000
2500Optimal installed capacity [GW]
Carrier
oil
urban central gas CHP
lignite
coal
gas turbines
biomass CHP
battery
nuclear
hydropower
Offshore Wind
Onshore Wind
Solar
Figure 8: Cost-optimal nameplate capacities in the power sector for different levels of gas consumption.
19

0
500
1000
1500
2000
2500
3000
Overnight Investment Cost
[EUR/kWth output]
314
1482
687
314
899
687
53
906
1160
595
46
784
70
595
46
941
70
595
46
214
46
214
Rural
heat
Urban
individual heat
Urban
central heat
Industry
<100°C
Industry
100 200°C
Industry
200 500°C
Industry
>500°C
DE
GB
FR
NL
AT
PL
DEGB
FR
SE
10 MW
3 MW
1 MW
0.5 MW
50 MW
10 MW
3 MW
1 MW
a
Heat pump literature capex
grid connection (+500 EUR/kWel)
capex incl. grid connection
0
25
50
75
100
125
150
VOM + fuel cost
[EUR/MWhth]
b CO2 price (100 EUR/t)
incl. CO2 price
Gas Boiler
Ground HP
Biomass Boiler
Gas Boiler
Air HP
Biomass Boiler
Gas Boiler
Air HP
Biomass CHP
Biomass Boiler
Gas Boiler
HP (med temp)
Electric Boiler
Biomass Boiler
Gas Boiler
HP (high temp)
Electric Boiler
Biomass Boiler
Gas (direct firing)
H2 (direct firing)
Gas (direct firing)
H2 (direct firing)
0
1
2
3
Weighted-avg
efficiency / COP [-]
c
Figure 9: Comparison between model values and literature values ofaOvernight investment cost,bvariable operational plus fuel cost andcefficiency/COP. As
in the rest of the model, cost assumptions are for 2030, and here are compared with other literature values for 2026. Hydrogen fuel costs assume electrolytic
production. Fuel costs are endogenously estimated from an energy-system model with annual gas consumption of 400 bcm/a. Note the values inbare in thermal
MWh, and therefore already account for efficiency. Multiplication of the shown values with the respective efficiency/COP approximately yields the fuel cost.
Literature cost values are compiled from [88–92].
Figure 10: Comparison of gas boiler and heat pump Levelised Cost of Heat (LCOH) for different heat demands. From the left to right these heat pump technologies
are medium-temperature industry heat pump, high-temperature industry heat pump, (residential) air-source heat pumps and ground-source heat pump. Each cross
refers to the heat pump vs gas boiler trade-off in one region of the network. The model LCOHs are taken from a system with gas consumption of 200 bcm/a.
Demand load factorquantifies the variation within a demand profile by dividing the average by the maximum.Break-evenrefers to LCOH-parity between heat
pumps and gas boilers. The high and low literature values are the same as for Fig 9 [88–92].
20

0
20
40
60
80
100
120
140
160Levelized cost of heat  [EUR/MWhheat]
39
63
38
63
90
63
143
63
35
55
34
55
76
55
131
55
28
46
28
46
73
46
125
46
endogenous
electricity price [EUR/MWhel]
industry heat < 100C
medium-temperature heat pump
industry heat 100-200C
high-temperature heat pump
ground heat pump air heat pump
capex heat pump
capex distribution grid (500 /kW)
opex
electricity cost
Figure 11: Disaggregation of heat pump LCOHs across supply technologies
and model runs.
21

electric
gas oil
biomass ambient
0
10
20
30
40share of heat [%]
a
EU-27 individual heating
(model vs Eurostat & ODYSSEE, final energy)
model
Eurostat 2023
ODYSSEE 2023
 heat pump
 resistive
electric
gas oil
biomass
0
10
20
30
40
50
60
70
80share of heat [%]
b
UK Census 2021
(GB, HP delivered)
model
UK Census 2021
electric
gas oil
biomass
0
10
20
30
40
50
60share of heat [%]
c
Norway (indicative)
(NO, HP delivered)
model
Norway (indicative)
Figure 12: Comparison between system model (400 bcm/a gas consumption) with brownfield existing heat capacities against 2023 heat supply from various sources.
The geographic scope varies between panels: we coveraEU27,bthe United Kingdom andcNorway. Data sources: Eurostat [ 93] and ODYSSEE-MURE [94] for
EU27 individual heating, EU district heating [95], the UK Census 2021 [96] and Energifakta Norge [97].
0 500 1000 1500 2000 2500 3000 3500 4000
T otal Gas Consumption [TWh]
0
1000
2000
3000
4000T otal Daily Energy Output [GWh]
Batteries
Gas power
Figure 13: Distributions of daily power contributions (generation for gas tur-
bines, discharging for batteries). The plot includes both utility-level and home
batteries; gas turbines cover both CCGT and OCGT.
22

0 50 100 150 200 250 300 350 400 450
Gas consumption constraint [bcm]
1500
1000
500
0
500
1000
1500
Energy [TWh]
Solid biomass
forest residues
industry wood
landscape care
solid biomass
unsustainable solid biomass
solid biomass import
Feedstock uses
Industry heat <200°C
Industry heat 200 500°C
Individual heating
Central/district heating
0 50 100 150 200 250 300 350 400 450
Gas consumption constraint [bcm]
300
200
100
0
100
200
300
Energy [TWh]
Biogas
manure and slurry
sewage sludge
straw
unsustainable biogas
Feedstock uses
Figure 14: Solid biomass and biogas balances for different levels of gas consumptions.
0 200 400 600 800 1000 1200
Biomass potential [TWh]
0
2
4
6
8
10
12
14Marginal cost [EUR/MWh]
European solid biomass supply curve
industry wood
landscape care
unsustainable solid biomass
forest residues
Figure 15: Supply curve in the model for solid biomass, taken from the Medium
Potential of the ENSPRESO dataset [78].
23

100
200
300
400LCOH [EUR/MWh]
Electric heating
Urban Individual Heat
Biomass boiler Gas boiler Oil boiler
±2
±1
mean
100
200LCOH [EUR/MWh]
Electric heating
Rural Heat
Biomass boiler Gas boiler Oil boiler
50
100
150LCOH [EUR/MWh]
Biomass CHP
District Heat
Gas boiler
0 1000 2000 3000 4000
System gas consumption [TWh]
Heat pump
10
20
30
40LCOH [EUR/MWh]
Heat pump
Industry <100°C Heat
Biomass Gas
10
20
30
40LCOH [EUR/MWh]
Heat pump
Industry 100-200°C Heat
Biomass
0 1000 2000 3000 4000
System gas consumption [TWh]
Gas
20
40
60LCOH [EUR/MWh]
Biomass
Industry 200-500°C Heat
Gas
0 1000 2000 3000 4000
System gas consumption [TWh]
0
50
100
150LCOH [EUR/MWh]
Gas
Industry >500°C Heat
0 1000 2000 3000 4000
System gas consumption [TWh]
Hydrogen
Figure 16: Levelised costs of heat (LCOH) in different heat demands in the model. The uncertainty bands refer to the spread across the 50 regions in the network.
Data is omitted where a technology supplies less than 10 TWh of heat across the network.
24

50% 25% 2%
Share of optimal industry electrification achieved
0
2
4
6
8
10 bn EUR/a
T otal system cost
50% 25% 2%
Share of optimal industry electrification achieved
0
2
4
6
8
10
12 million households
Heat pumps in buildings
50% 25% 2%
Share of optimal industry electrification achieved
0
50
100
150
200
250
300
350 TWh
Biomass heat in industry
Figure 17: Impact on system cost, building heating and solid biomass use under 200 bcm gas use while constraining the share of industry heat that can be electrified.
The share on the𝑥-axis refers to the share of currently gas-met industry heat demand that can, in the respective model, be met by other means.
AlbaniaAustriaBelgium
Bosnia & Herz.
BulgariaCroatiaCzechiaDenmarkEstoniaFinlandFrance GermanyGreeceHungaryIreland
Italy
KosovoLatvia
Lithuania
LuxembourgMontenegroN. MacedoniaNetherlands
NorwayPolandPortugalRomania SerbiaSlovakiaSlovenia Spain Sweden
Switzerland
United Kingdom
0
20
40
60
80
100Annual heat demand [TWh]
Industry heat demand by country and temperature level
T emperature band
<100°C
100 200°C
200 500°C
Figure 18: Industry heat demand below 500◦C currently met by gas, by European country.
25

0 200 400 600 800 1000
Industry production (Mt/a)
Other industrial sectors
Machinery equipment
Ceramics & other NMM
Transport equipment
Food, beverages and tobacco
Cement
Integrated steelworks
Paper production
T extiles and leather
Electric arc
HVC
Pulp production
Glass production
Wood and wood products
Other chemicals
Ammonia
Other non-ferrous metals
Pharmaceutical products etc.
Printing and media reproduction
Chlorine
Alumina production
Aluminium - secondary production
Aluminium - primary production
Methanol
Figure 19: Annual production volumes for different industry sectors based on
JRC IDEES dataset [80].
0% 20% 40% 60% 80% 100%
Share of process heat demand (%)
Alumina production
Cement
Aluminium - primary production
Ceramics & other NMM
Other non-ferrous metals
Glass production
High value chemicals
Aluminium - secondary production
Food, beverages and tobacco
Paper production
Other industrial sectors
Transport equipment
Machinery equipment
Pharmaceutical products etc.
T extiles and leather
Pulp production
Printing and media reproduction
Wood and wood products
<100 °C 100-200 °C 200-500 °C >500 °C
Figure 20: Share of process heat demand across the four temperature bands for
each industrial sector, derived mostly from Fleiter et al. [98] and supplemented
for uncovered sectors as described in the main text.High value chemicalsrefers
to the basic petrochemicals, i.e. olefins (ethylene, propylene) and aromatics
(benzene, toluene, xylene).
0 200 400 600 800 1000 1200 1400
Endogenised industry process heat, by temperature band (TWh/a)
<100 °C
35%
100-200 °C
62%
200-500 °C
88%
>500 °C
92%
 colder
 hotter
Gas assumed to meet the hottest heat in each process (996 of 1514 TWh)
met by gas today met by other carriers
Figure 21: Visualisation of mapping from industry heat demands to gas demand.
The JRC industry dataset shows that waste-heat, biomass and gas are used to
supply heat. When an industry process utilises multiple of these, and also has
heat demands in different temperature bands, then we assume it is the highest
temperature-end of that heat demand that is met by gas since it is the only
carrier that can provide higher temperature heat generically.
<100 °C 100-200 °C 200-500 °C >500 °C
0
100
200
300
400Heat demand met by gas (TWh/a)
324
406
121
346
T otal: 1198 TWh/a
Figure 22: Gas-attributed industry heat demand per temperature band.
26

Electricity (Low Voltage) Urban Individual Heating Rural Heating District Heating
Solid Biomass Biogas Industry Heat <100 °C Industry Heat >500 °C
45
50
55
60
65
70
75
80
EUR/MWh
20
25
30
35
40
45
EUR/MWh
19.5
19.6
19.7
19.8
19.9
20.0
20.1
20.2
20.3
EUR/MWh
26
28
30
32
34
36
38
EUR/MWh
48
49
50
51
52
EUR/MWh
20
40
60
80
100
Building Heating [EUR/MWh]
Regional Commodity Prices for 200 bcm Gas Consumption
Figure 23: Time-weighted average marginal prices for different commodities under a 200 bcm fossil gas supply constraint. [Higher prices in France in urban
individual heating are somewhat misleading. It appears that price is largely driven by a few days of cold snaps with electric heating creating grid bottlenecks.]
Figure 24: Composition of emissions under varying fossil gas supply constraints.
27

AL
AT
BA
BE
BG
CH
CZ
DE
DK
EE
ES
FI
FR
GB
GR
HR
HU
IE
IT
LT
LU
LV
ME
MK
NL
NO
PL
PT
RO
RS
SE
SI
SK
XK
0
10
20
30
40
50
60
70Installed Capacity [GW]
rural
 374 GW
T echnology
air heat pump
biomass boiler
gas boiler
ground heat pump
oil boiler resistive heater
AL
AT
BA
BE
BG
CH
CZ
DE
DK
EE
ES
FI
FR
GB
GR
HR
HU
IE
IT
LT
LU
LV
ME
MK
NL
NO
PL
PT
RO
RS
SE
SI
SK
XK
country
0
50
100
150
200
250Installed Capacity [GW]
urban individual
 1370 GW
Figure 25: Installed heating capacities for all residential and service-sector heating, except district heating. The dataset used is from 2012 [47], suggesting that
electric options are somewhat more widespread than represented here.
28

Solar
0.10 0.11 0.12 0.13 0.14 0.15 0.16 0.17 0.18
Capacity factor
Onshore Wind
0.1 0.2 0.3 0.4
Capacity factor
Offshore Wind
0.2 0.3 0.4 0.5
Capacity factor
Urban Individual
Air HP
District Heat
Air HP
Rural Air HP
2.4 2.6 2.8 3.0 3.2 3.4 3.6 3.8 4.0
Air heat-pump COP (annual mean)
Figure 26: Capacity factors of renewables and, in the lower row, coefficients of performance for different kinds of heat pumps.
29
