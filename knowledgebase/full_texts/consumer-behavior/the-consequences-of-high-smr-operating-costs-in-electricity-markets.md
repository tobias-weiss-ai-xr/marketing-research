---
title: The consequences of high SMR operating costs in electricity markets
url: https://arxiv.org/abs/2609.08929
category: consumer-behavior
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Pradyumna Rao
- Daniel T. Kaffine
- Bri-Mathias Hodge
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.08929
pages: 18
chars: 74372
fetched_at: '2026-11-08T13:16:01+00:00'
kb_version: 1
---

# The consequences of high SMR operating costs in electricity markets

Highlights
The consequences of high SMR operating costs in electricity markets
Pradyumna Rao, Daniel T. Kaffine, Bri-Mathias Hodge
•While SMRs are designed for lower investment costs, increased operating costs lead them to be uneconomical
•SMRs at manufacturer advertised costs are unable to pay back in less than their lifetime in wholesale markets.
•Subsidies and prices need to exceed historic highs for SMRs to be economically viable
•Improvements in marginal costs may be more valuable than in investment costs for SMRs in future power grids
arXiv:2609.08929v1  [eess.SY]  8 Sep 2026

The consequences of high SMR operating costs in electricity markets
Pradyumna Raoa,∗∗, Daniel T. Kaffineb and Bri-Mathias Hodgec,∗,1,3
aPaul M. Rady Department of Mechanical Engineering and Renewable and Sustainable Energy Institute, University of Colorado-Boulder, 1111
Engineering Drive, Boulder, 80309, CO, United States
bDepartment of Economics and Renewable and Sustainable Energy Institute, University of Colorado Boulder, Economics Building, 261 UCB
#212, Boulder, 80302, CO, United States
cDepartment of Electrical, Computer, and Energy Engineering and Renewable and Sustainable Energy Institute, University of Colorado Boulder, 4001
Discovery Dr. N321, Boulder, 80309, CO, United States
ARTICLE INFO
Keywords:
Small Modular Reactors
Nuclear Power
Electricity Markets
Tax Credits
ABSTRACT
As US power markets contend with growing demand for firm generation, the nuclear industry has
offeredSmallModularReactors(SMRs).However,howtheseconceptswouldfareinarapidlyevolv-
ing power grid is unclear, given the paucity of operational examples. Current literature, informed by
substantial cost escalations for traditional nuclear plants, focuses on the investment costs SMRs need
toachieveforprivateinvestmentfeasibility.However,thisworkfindsthattheoperatingandmarginal
costsofSMRsaremorecriticaltoeconomicfeasibilityinmarketenvironments.Thisworkdispatches
SMRsusingaflexibleoperationsmodel,consideringrevenuefromtwomainelectricmarkets,capacity
and wholesale energy markets, with and without policy support. Manufacturer advertised costs for
investment and operating costs are used, with fuel costs calculated from manufacturer provided
design parameters. Results indicate that SMRs are uneconomical primarily because investment cost
reductions are offset by increased marginal costs. As such, an environment of prices and subsidies
beyond historic norms are necessary to attract private investment at manufacturer advertised cost
benchmarks.CurrentSMRsareasprofitableasadvancedestimatesoftheAP1000traditionalnuclear
reactor, and if investment costs escalate at the average rate for nuclear projects, they are similar to
Vogtle 3 & 4. In projected future power markets, reductions in marginal cost may be more beneficial
than those in investment costs.
1. Introduction
Momentum for nuclear generation has been building
over the past few years as demand for carbon-free firm gen-
erationgrows.TherestartofThreeMileIslandbyMicrosoft
Corporation Corporation (2024), Power Purchase Agree-
ments by Amazon with Talen and Energy Northwest for
traditionalandSmallModularReactorsAmazon(2024),and
Google’s agreements with Kairos Power Terrell (2024) are
examples of material commitments made towards building
new nuclear power. These efforts follow declarations made
by25countriesatCOP28totriplenuclearcapacityby2050
U.S. Department of Energy (2023) to achieve global net-
zero goals, such as climate benchmarks of limiting average
temperature increase to1.5 ◦C above pre-industrial levels
United Nations (2023).
However, experiences building new nuclear plants in
the United States and France over the past few decades
have incurred substantial cost escalation, classified as “neg-
ative learning by doing" Grubler (2010). Additionally, long
lead times, safety issues, permanent disposal of radioac-
tive waste, and proliferation of potential nuclear weapon
materialAdamantiadesandKessides(2009);Ansolabehere,
Deutch, Driscoll, Gray, Holdren, Joskow, Lester, Moniz,
∗Corresponding author
∗ ∗Principal corresponding author
prady.rao@gmail.com(P. Rao);daniel.kaffine@colorado.edu(D.T.
Kaffine);brimathias.hodge@colorado.edu(B. Hodge)
https://www.colorado.edu/faculty/kaffine/(D.T. Kaffine);
https://www.colorado.edu/faculty/hodge/(B. Hodge)
ORCID(s):0009-0005-8063-2271(P. Rao);0000-0002-9556-7776(D.T.
Kaffine);0000-0001-8684-0534(B. Hodge)
Todreas, Beckjord, Hottle, Jones and Parent (2003) have
increased investor reticence towards new gigawatt scale nu-
clear power plants Locatelli (2018). Existing nuclear power
plants have retired due to difficulty remaining competitive
Haratyk (2017) in electricity markets, attributed to down-
ward pressure on electricity prices from increased penetra-
tion of renewable energy Seel, Mills and Wiser (2018).
Therefore, central to achieving these nuclear buildout
targetsareanewgenerationofnuclearreactorscalledSmall
ModularReactors,commonlyknownasSMRs.Classifiedas
reactors with power outputs<300 MWe, these prototypes
are part of a concerted effort over the last two decades
by the nuclear industry to address techno-economic con-
cernssurroundingtraditionalgigawatt-scalereactors.SMRs
have been touted as simpler, safer, and cheaper due to
their modular designs Vujić, Bergmann, Škoda and Miletić
(2012). Additionally, load-following features of SMRs aim
to improve integration with variable renewable power Lo-
catelli, Boarin, Pellegrino and Ricotti (2015), as well as
enable generation or co-generation with industrial prod-
ucts such as hydrogen Pham, Lovdal, Zhang and Craig
(2022), steam and thermal heat Vanatta, Stewart and Craig
(2024). However, the private investment potential of SMRs
and nuclear power for future power grids is a source of
intensifying debate Kim and Macfarlane (2026); Steiger-
wald,Weibezahn,SlowikandvonHirschhausen(2023);Nø-
land, Hjelmeland, Hartmann, Tjernberg and Korpås (2025);
Schlissel and Wamsted; Froese, Kunz and Ramana (2020).
This work investigates the economic performance of
SMRs under historical and future power scenarios, with
P. Rao et al.:Preprint submitted to ElsevierPage 1 of 17

Consequences of high SMR operating costs
and without additional policy support. Independent System
Operator (ISO) Markets are defined by their two compo-
nents - wholesale energy markets and capacity markets.
Manufacturer-advertised SMR cost estimates should be in-
terpreted with caution, as their veracity remains disputed
Steigerwald et al. (2023); Schlissel. However, given the
limitedavailabilityofSMRcostestimatesvalidatedthrough
operating experience, this work uses these advertised val-
ues as inputs for simulating economic performance. The
primary research question this work seeks to answer is:
are SMR concepts economically viable from a private in-
vestment perspective? With over 70 SMR concepts under
development globally International Atomic Energy Agency
(2024), whether these concepts would be more economical
and attractive as private investment vehicles is key to their
prospects. To explore how SMRs would perform in future
power grids, this paper primarily builds on two main works
from the literature.
The primary work this paper builds on is Steigerwald
et al. (2023), who find after comparing manufacturer and
production-theory based estimates, no SMR concept would
be competitive or profitable. While comparing Levelized
Cost of Electricity (LCOE) and Net Present Value (NPV)
to alternate investment options, such as existing renew-
able technologies, was the focus of the work, a sub-finding
showed low to negative NPVs using SMR manufacturer
advertisedestimates.Exploringcausalfactorsofthefinding
on poor economic outcomes at SMR manufacturer costs is
theprimarymotivationbehindthiswork.Limitingfactorsof
Steigerwaldetal.(2023)weretheiruseofstaticassumptions
on operational characteristics such as capacity factors and
sampled constant lifetime prices. This fails to capture how
evolving features of the grid may affect SMR investments
Driouchi and Bennett (2012), from temporal price volatility
Barcelona (2015) to their corresponding operational de-
cisions, such as ramping in response to low or negative
prices, which will play a significant role for thermal power
feasibility in future low-carbon grids Vithayasrichareon and
Macgill (2014). As such, in calculating feasibility metrics
such as NPV and discounted payback periods, this work
dispatches a flexible operations model based on literature
methodologies Alhadhrami, Soto and Lindley (2023) on
hourlypriceprofilestoendogenizetemporalandoperational
impacts. This work also extends manufacturer advertised
SMR cost parameters Steigerwald et al. (2023) with techni-
cal design constraints and refueling outages to supplement
the operational model.
The second key related work is Haratyk (2017), who
found that existing nuclear power plants remain uncom-
petitive without out-of-market carbon pricing payments to
combat declining wholesale energy prices. Haratyk (2017)
partially attributed premature retirements and the need for
out-of-market support to high nuclear operating costs, de-
fined as the sum of fuel, variable and fixed operating costs,
which motivated this work to explore whether low SMR
NPVsfoundbySteigerwaldetal.(2023)couldbeattributed
tothesamefactors.Twokeyaspectsofthisworkaredistinct
from Haratyk (2017), who robustly modeled existing nu-
clear performance under historical wholesale prices, capac-
ity markets, and policy mechanisms such as carbon pricing.
First, this work models SMRs, which are purported to have
lower investment costs from potential module-based learn-
ing Abou-Jaoude, Lohse, Larsen, Guaita, Trivedi, Joseck,
Hoffman, Stauff, Shirvan and Stein (2024), and different
operational characteristics such as ramping at a rate up to
1% of rated thermal power per hour, as well as refueling
modulessequentiallyAlhadhramietal.(2023).Secondly,as
wholesalepowerpricetrendsaresettochangewithevolving
grid complexity, such as increasing shares of Variable Re-
newableEnergy(VRE)Seeletal.(2018),storageNyamdash
andDenny(2013)andElectricVehicles(EVs)Sauter,Lara,
Turk, Milford and Hodge (2024), this work models future
price scenarios to help capture these price trends in the
analysis.
Building on Haratyk (2017) and Steigerwald et al.
(2023), the primary novel contribution this paper makes
is identifying a new important mechanism not appreciated
in previous literature — that the economic performance
and feasibility of SMR depends more on their marginal
costs, defined as the sum of fuel and variable operating
costs,ratherthanoft-discussedinvestmentcosts.Additional
contributions this works makes are capturing the expanding
set of revenue streams available under current market struc-
turesandpolicyincentives,anddeterminingtheirnecessary
levels to make SMRs economically feasible. Fuel costs
for SMRs are also calculated from manufacturer provided
design parameters to add to the literature around SMR cost
estimates. The final novel contribution is quantifying the
breakeven marginal and investment cost tradeoff for SMRs
under various scenarios. From this, investment cost ceilings
are extracted as benchmarks to contribute to the discussion
around the economics of SMRs.
Overall, the results of this work show that an environ-
ment of prices and subsidies beyond historic highs is neces-
sarytoattractprivateinvestmentatmanufactureradvertised
costbenchmarksforSMRs.Primarily,thepoorperformance
of SMRs can be attributed tothe consequences of high
operating costsin the transition to advanced nuclear. In an
effort to reduce upfront investment cost for SMRs, design
tradeoffs such as using novel High-Assay Low-Enriched
Uranium(HALEU)andTri-structuralIsotropic(TRISO)fu-
els that do not have established supply chains ballooned op-
erational and marginal costs. Intra-hour losses from operat-
ingtheSMRsasaresultovershadowanyupfrontinvestment
cost advantages. While SMRs may potentially experience
issues such as loss of economies of scale Kuznetsov (2008)
and other risks of new technology, this work demonstrates
the greater importance of operating and marginal costs to-
wards private investment feasibility.
High marginal costs at manufacturer advertised cost
estimatesimplythatSMRsrelyingonlyonwholesalemarket
revenues are unable to achieve discounted payback periods
in less than their technical lifetimes. Improving feasibility
P. Rao et al.:Preprint submitted to ElsevierPage 2 of 17

Consequences of high SMR operating costs
withsupplementarycapacityrevenuesrequiresaveragelife-
time prices to be greater than PJM’s historic high 2025/26
auction price, which caused the Commonwealth of Penn-
sylvania to threaten to leave PJM Howland (d). Any po-
tential policy support needs to exceed current levels of the
Investment Tax Credits (ITC) and Production Tax Credits
(PTC), and even with capacity revenues, a high PTC rate
is needed, with capacity revenues more impactful than the
PTC.ForsomeSMRs,eveniftheITCsubsidizedthewhole
costofconstruction,itisstillinsufficienttoimprovepayback
periodsbelowtechnicallifetimes.However,ifpolicymakers
were to raise the PTC to $95 𝑀𝑊 ℎ, to better reflect the social cost of carbon Rennert, Errickson, Prest, Rennels, Newell,
Pizer, Kingdon, Anthoff, Cooke, Raftery, Ševčíková, Wat-
son, Hecke, Hardisty, Kobos, Fissel, McJeon, Newell and
Shindell (2022) of avoided emissions (primarily natural gas
at roughly 0.5 tons/MWh), most SMRs would be able to
achievepaybackperiodsbelow20years,withorwithoutca-
pacity revenues. Quantifying the tradeoff between marginal
and investment costs for SMRs, improvements in marginal
costs pay larger dividends than investment cost reductions.
IfSMRmarginalcostsimprovedtobaseloadlevelsat $12 𝑀𝑊 ℎ, investment cost benchmarks can be relaxed by an average
of 30%, with a maximum investment cost of$7,813 𝑘𝑊 𝑒 under high wholesale and capacity prices supplemented by high
PTC rates. Finally, if SMRs experience investment cost
escalations, they have similar profitability to Vogtle 3 & 4,
with SMRs at current estimates as profitable as Nth-of-a-
kind (NOAK) and advanced estimates of the AP1000. This
sharply brings into question the benefits of the transition to
advanced nuclear plants, especially since traditional plants
enjoy economies of scale that SMRs lack.
Following this introduction section, Section 2 describes
the SMR cost and operational dataset, the price profiles
used for energy market analysis and the dispatch algorithm.
Section 3 presents the results in five parts. First, Section
3.1 presents the results of energy markets only under future
and historical price scenarios, Section 3.2 then analyzes
the impact of capacity revenues and Section 3.3 presents
policy support results. Section 3.4 then presents results
from breakeven marginal and investment cost tradeoff, and
Section3.5presentsresultsfrombenchmarkingtotraditional
nuclear power and potential cost overruns.
2. Data and Methodology
2.1. Data Collection
This paper utilizes a cost dataset from Steigerwald et
al. Steigerwald et al. (2023). Investment costs were main-
tained,whileoperationaldatafromtheInternationalAtomic
Energy Agency’s Advanced Reactors Information System
(ARIS) International Atomic Energy Agency were added,
along with manufacturer-provided information for concepts
notincludedintheoriginaldataset.Althoughmanufacturer-
advertised investment costs may reflect optimistic assump-
tions and remain subject to uncertainty, this work does
not assess their validity in detail, as the analysis primarily
Table 1
Selected manufacturer-advertised cost data taken from the
source data of Steigerwald et al. (2023) and expanded using
Lazard (2024). Xe-100 estimates were obtained from X-Energy
Reactor Company, LLC and Ares Acquisition Corporation
(2022) and Aurora estimates from Oklo Inc. (2023).
Project Capacity
[MWel]
Investment
Cost
[$/MWel]
Fuel
Cost
[$/MWh]
Fixed O&M
Cost
[$/MW-yr]
Variable
O&M
Cost
[$/MWh]
BWRX-300 300 2,250,000 8.44 140,160 3.55
UK-SMR 470 5,215,937 10.95 595,680 3.55
SMR-160 160 6,312,500 14.48 103,631 3.55
NuScale 77 3,466,000 17.42 632,998 3.55
Aurora-15 15 3,800,000 13.41 135,868 4.25
Xe-100 80 7,500,000 3.39 21,900 3.55
Table 2
Operational data for SMR concepts from IAEA’s ARIS In-
ternational Atomic Energy Agency. Xe-100 estimates were
obtained from X-Energy Reactor Company, LLC and Ares
Acquisition Corporation (2022) and Aurora estimates from
Oklo Inc. (2023).
Project Lifetime [yr] Modules Const. [mo.] Refuel Min. [mo.] Refuel Max. [mo.]
BWRX-300 60 1 26 12 24
UK-SMR 60 1 24 18 24
SMR-160 80 2 36 20 26
NuScale 60 12 36 15 18
Aurora-15 40 1 12 118 120
Xe-100 60 4 36 6 12
focuses on the role of marginal costs in SMR economic
performance.LazardassumptionsforVariableO&Mdataof
$3.55
𝑀𝑊 ℎ Lazard (2024) were used for SMR concepts without otherwise available estimates of variable O&M costs. For
SMRs with missing fixed cost values, EIA parameters were
usedU.S.EnergyInformationAdministration.Additionally,
assumptions for SMR concepts using online refueling were
takenas6-12months.Priceswerenormalizedto2020USD
for this work to maintain consistency. Figure 1 illustrates
the differences between the dataset used in this work and
Steigerwald et. al.
Front-end fuel costs were calculated using the Argonne
National Laboratory NE-COST / CNPCE calculator Ar-
gonneNationalLaboratory(2024)afterextractingmanufac-
turer advertised design parameters from ARIS International
Atomic Energy Agency. Fabrication cost estimates from
Rothwell Rothwell (2010) were used after cross referenc-
ing publicly available literature on fuel supply sources for
each concept. HALEU and advanced fuel enrichment and
deconversion costs were taken from White and Cothran
White and Cothron and enrichment, fabrication, depleted
uranium deconversion, spent nuclear fuel conditioning, and
geologic disposal costs were taken from the DOE Fuel
CycleEvaluationandScreeningWigeland,Taiwo,Ludewig,
Todosow, Halsey, Gehin, Jubin, Buelt, Stockinger, Jenni
and Oakley (2014). OECD-NEA’s back-end fuel-cycle cost
studies Nuclear Energy Agency were used for sensitivities.
A 92.3% capacity factor was used for fuel cost calculations
Mueller.
P. Rao et al.:Preprint submitted to ElsevierPage 3 of 17

Consequences of high SMR operating costs
Figure 1:Cost estimates used by Steigerwald et al. and calculated in this work. Fixed costs were converted from$∕MWeto
$∕MWhfor ease of comparison.
For the purposes of this work, we focus on six manu-
facturerconcepts-GE-Hitachi’sBWRX-300,Rolls-Royce’s
UK-SMR1,Holtec’sSMR-160,NuScale’sVOYGR,OKLO’s
Aurora15MWePowerhouse,andX-energy’sXe-100.These
are widely considered as some of the leading concepts
Schlegel and Bhowmik (2024) and performed the best in
our analysis. Table 1 outlines the cost data selected for
the bulk of this paper’s analysis, with Table 2 outlining
the respective operational data. While fixed costs were
converted to $/MWh to compare against operating costs
in Figure 1, assuming they were not included in dispatch
decisions, which are only based on marginal costs.
2.2. Price Profiles
Ten hourly real-time price profile scenarios from the
National Renewable Energy Laboratory’s Cambium 2022
and 2023 dataset Gagnon, Sanchez Perez, Obika, Schwarz,
Morris, Gu and Eisenman (2024), spanning 2025-2050,
were used to represent future prices. To benchmark against
historic scenarios, hourly prices between 2011-2023 from
six competitive wholesale markets were extracted from
Lawrence Berkeley National Laboratory’s Renewables and
Wholesale Electricity Prices dataset (ReWEP) Millstein,
O’Shaughnessy and Wiser (2024). Element-wise interpola-
tionwasthenusedtolinkCambiumprofilesfiveyearsapart,
to create a single profile scenario up to the SMR technical
1Although its 470 MWe capacity exceeds the traditional International
AtomicEnergyAgency(IAEA)limitof300MWe,theRolls-Roycedesign
is classified as a Small Modular Reactor (SMR) due to its reliance on stan-
dardized factory prefabrication and modular construction methodologies.
Table 3
Summary statistics of highlighted historical and future price
scenarios used in the study. Three Cambium scenarios and
three average ISO historical price scenarios were selected to
contrast performance expectations. All prices are in$∕MWh.
Price Scenario Type Mean Std. Dev. Max Min
High Natural Gas Prices Future 38.53 101.66 2455.31 -192.27
Mid Case 100 Future 55.24 130.35 3221.74 -733.07
High Renewable Energy Cost Future 36.87 103.58 2338.17 -148.10
PJM Historic 41.51 48.30 4002.80 -284.60
ERCOT Historic 41.77 292.85 9080.56 -144.54
CAISO Historic 44.56 48.91 1600.10 -2491.30
lifetime. While all SMR concepts were run in all scenarios,
thisworkpresentsresultsfromthreefutureandthreehistoric
price scenarios, detailed in Table 3. Additionally, capacity
market revenues were modeled as monthly payments at a
fixed rate and discounted over time. Capacity prices were
varied at and beyond historical limits shown in Figure 2.
2.3. Policy and Research Estimates
Investment and production tax credits were modeled
to calculate policy impacts on nuclear generators. Invest-
ment credits were treated as cost reduction multipliers on
the investment costs, and production as an hourly credit
spanning 10 years, based on a reference of the ITC and
PTC. PTC and ITC rates were taken from NREL’s Annual
TechnologyBaseline(ATB)Abou-Jaoudeetal.(2024),with
ITC cost reduction multipliers calculated from investment
costreductionsintheATB.Additionally,researchestimates
P. Rao et al.:Preprint submitted to ElsevierPage 4 of 17

Consequences of high SMR operating costs
0
5
10
15
20
ISO-NE MISO Seasonal MISO Yearly NYISO PJM
Market
Price (USD/kW-month)
Capacity Market Price Comparison
Figure 2:Comparison of historical prices of existing capacity markets in MISO, ISO-NE, NYISO, and PJM. Prices include the
PJM 2025/26 capacity market auction, shown by the outlier at $8.21/kW-month.
Table 4
Future cost estimates of the AP1000 and NREL ATB reactor
scenarios.
Concept Construction
Cost
[$/kWel]
Fuel
Cost
[$/MWh]
Fixed O&M
Cost
[$/MW-yr]
Variable
O&M
Cost
[$/MWh]
Baseline (V3&4
realized)
11,000 9.00 204,000 3.40
Baseline (V3&4 if
built today)
15,000 9.00 204,000 3.40
Next 2 @ Vogtle 8,300 9.00 175,000 2.80
Next 2 @ Greenfield 9,300 9.00 175,000 2.80
NOAK 4,625 9.00 126,000 1.90
ATB_LR_Adv 6,471 9.13 126,000 1.90
ATB_LR_Mod 7,616 10.18 17,000 2.80
ATB_LR_Cons 11,836 11.34 204,000 3.40
from the ATB and the 2024 Total Cost Projection of Next
AP1000 Shirvan (2024) were used to benchmark industry
expectationsoncostdataforSMRsandAP1000’s.Table??
details the collected estimates.
2.4. Flexible Operations Model
Usingcompiledpriceprofilesandgeneratordata,asim-
pleFlexiblePowerOperation(FPO)pricetakerformulation
was used to simulate reactor performance over its lifetime.
The relation of the hourly electricity price to the marginal
costofoperationwasthecentralobjectiveoftheFPO.Ifthe
costwaslowerthanthehourlyprice,theSMRwasexpected
to be operate at maximum power. If the cost was higher,
the SMR was expected to ramp down to a technical Low
Power Output (LPO) defined at 40% of maximum power
Alhadhrami et al. (2023).
Refuelingwasscheduledonemoduleatatime,occurring
whenthepricesignalisinthelowerquartileoftherefueling
range for the generator. Startup costs were obtained from
the ATB at $60 𝑘𝑊 𝑒 Abou-Jaoude et al. (2024). Capacity pay- ments were treated as monthly injections exogenous of the
dispatch, but included in discounting. From this, the price
P. Rao et al.:Preprint submitted to ElsevierPage 5 of 17

Consequences of high SMR operating costs
taker formulation was defined as follows, starting with𝑃(𝑡)
as the net operating cashflow.
𝑃(𝑡) =
⎧
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎨
⎪
⎪
⎪
⎪
⎪
⎪
⎪⎩
𝑝(𝑡)𝑚+𝐼 𝐶 (𝑡)𝑐𝑚− (𝑓+𝑣)𝑚,if𝑝(𝑡)≥𝑓+𝑣, 𝑠(𝑡) = 1, 𝑡∈ [𝑡 𝑠, 𝑡𝑒],
𝑝(𝑡)𝑚′ +𝐼 𝐶 (𝑡)𝑐𝑚′ − (𝑓+𝑣)𝑚 ′ −𝑆𝐶,if𝑝(𝑡)≥𝑓+𝑣, 𝑠(𝑡) = 0, 𝑡∈ [𝑡 𝑠, 𝑡𝑒],
𝑝(𝑡)𝑚− (𝑓+𝑣)𝑚,if𝑝(𝑡)≥𝑓+𝑣, 𝑠(𝑡) = 1, 𝑡∉ [𝑡 𝑠, 𝑡𝑒],
𝑝(𝑡)𝑚′ − (𝑓+𝑣)𝑚 ′ −𝑆𝐶,if𝑝(𝑡)≥𝑓+𝑣, 𝑠(𝑡) = 0, 𝑡∉ [𝑡 𝑠, 𝑡𝑒],
𝑝(𝑡)𝓁+𝐼 𝐶 (𝑡)𝑐𝓁− (𝑓+𝑣)𝓁,if𝑝(𝑡)< 𝑓+𝑣, 𝑠(𝑡) = 1, 𝑡∈ [𝑡 𝑠, 𝑡𝑒],
𝑝(𝑡)𝓁+𝐼 𝐶 (𝑡)𝑐𝓁− (𝑓+𝑣)𝓁−𝑆𝐶,if𝑝(𝑡)< 𝑓+𝑣, 𝑠(𝑡) = 0, 𝑡∈ [𝑡 𝑠, 𝑡𝑒],
𝑝(𝑡)𝓁− (𝑓+𝑣)𝓁,if𝑝(𝑡)< 𝑓+𝑣, 𝑠(𝑡) = 1, 𝑡∉ [𝑡 𝑠, 𝑡𝑒],
𝑝(𝑡)𝓁− (𝑓+𝑣)𝓁−𝑆𝐶,if𝑝(𝑡)< 𝑓+𝑣, 𝑠(𝑡) = 0, 𝑡∉ [𝑡 𝑠, 𝑡𝑒].
Where𝑚total plant capacity,𝑚 ′ is the refueling plant
capacity,𝓁is the LPO,𝑝(𝑡)denotes the hourly electricity
price at time𝑡,𝑓and𝑣correspond to the fuel cost and
variable operating cost, respectively,𝑐represents the hourly
productiontaxcreditandstartupcostisdenotedby𝑆𝐶.The
binary functions𝑠(𝑡) ∈ {0,1}indicate the refueling status
at time𝑡and𝐼 𝐶 (𝑡)denotes the production credit eligibility,
between the operational start time𝑡𝑠 and credit eligibility
expiration𝑡 𝑒.
Key SMR performance metrics of NPV and Discounted
Payback Period were collected. Investment costs were dis-
tributed across the construction duration with a 10% con-
struction interest applied Portugal-Pereira, Ferreira, Cunha,
Szklo, Schaeffer and Araújo (2018). For the purposes of
this work, a 4% discount rate was assumed in all Present
Value calculations. Using these assumptions, the NPV and
Discounted Payback Period was formulated. Let the annual
outlay𝐼 𝑡 be:
𝐼𝑡 = 𝐶const 𝐷 (1 +𝑟 𝑐 ) 𝑡−1, 𝑡= 1,…, 𝐷.
where𝐶 const is the total construction cost,𝐷is the total
construction duration in years, and𝑟𝑐 is the construction
interest rate applied during this period.
The present value of investment𝐼0 is then defined as:
𝐼0 =
𝐷∑
𝑡=1
𝐼𝑡
(1 +𝑟) 𝑡 =
𝐷∑
𝑡=1
𝐶const
𝐷
(1 +𝑟 𝑐 ) 𝑡−1
(1 +𝑟) 𝑡 .
where𝑟isthediscountrateusedforpresent-valuecalcu-
lations.
From this, the net present value is defined as:
NPV = −𝐼 0 +
𝑁∑
𝑡=1
𝑃𝑡 −𝐹 𝑂𝑀
(1 +𝑟) 𝑡 .
where𝑃 𝑡 is the net operating cashflow in year𝑡,𝐹 𝑂𝑀
istheFixedO&Mcostand𝑁isthetechnicallifetimeofthe
plant.
Finally, the discounted payback period𝑇is defined as
the smallest integer such that the cumulative discounted
operating cash flows satisfy∑𝑇 𝑡=1 𝑃𝑡∕(1 +𝑟) 𝑡 ≥𝐼 0, i.e.:
min
{
𝑇∈ {1,…, 𝑁} |||
𝑇∑
𝑡=1
𝑃𝑡
(1 +𝑟) 𝑡 ≥𝐼 0
}
.
3. Results
3.1. Investment Viability in Competitive Energy
Markets
ExploringtheprivateinvestmentviabilityofSmallMod-
ular Reactors, this paper first finds that energy only market
revenue is insufficient under nearly all historical and fu-
ture price scenarios. Almost all concepts have discounted
payback periods greater than their technical lifetimes. The
only reactor to show promise in several of the scenarios,
PBMR-400, was canceled as a demonstration project by
the South African government due to a lack of financing
opportunities, being considered uneconomical and having
accumulatedsignificantlossesHogan(2010).Observingthe
scenarios themselves, SMRs necessitate an environment of
high decarbonization and high prices to achieve feasible
economic outcomes. This is seen by the performance of
SMRs in the Mid Case 100 scenario, a scenario with full
decarbonization, mean prices nearly $15 𝑀𝑊 ℎ higher than the next closest scenario and significantly more price volatility,
as observed in Table 3.
The key finding of this paper is that high marginal
and operating costs drive the poor performance of SMR
concepts. Wholesale energy markets set the system energy
price by the merit order based on short-run marginal cost.
As such, due to ramping and startup constraints forcing
operation, SMRs absorb significant intra-hour losses during
hourswherepricedepressionoccursandtheirmarginalcosts
are higher than the system price. These losses are so large
that even if investment cost reductions are achieved, SMRs
would still be unprofitable. An example is the case of the
RollsRoyce’sUK-SMR.Withreportedfixedoperatingcosts
of $68 𝑀𝑊 ℎ Farmer (2022) and marginal costs of $14.5 𝑀𝑊 ℎ, the concept endures significant intra-hour losses which, over
the course of its operation, results in a discounted pay-
back period greater than its technical lifetime, even if it
were to incur no investment costs. Additionally, during the
hours where the market clearing prices are higher than the
marginal costs, SMRs earn smaller inframarginal rents. As
aresult,evenifSMRsareabletoavoidtechnicalconstraints
and instantaneously ramp from zero to maximum power to
avoid intra-hour losses, compressed margins due to high
marginal costs would still inhibit the profitability of a SMR
plant. This is demonstrated in our results, where the most
substantial reduction to discounted payback periods from
bypassing technical constraints is only 2 years, achieved by
the BWRX-300 under the Mid-Case 100 price scenario.
These dynamics are reflected in operational decisions
made by SMRs. SMRs are, like traditional nuclear power,
expected to provide baseload power to the power grid U.S.
Department of Energy (a). However, as seen in Table??, in
P. Rao et al.:Preprint submitted to ElsevierPage 6 of 17

Consequences of high SMR operating costs
Figure 3:Discounted payback period (green) of six market-leading and top-performing reactors, with the distribution of electricity
prices (purple) overlaid for selected scenarios.
Table 5
Capacity factors for different SMR designs in selected scenarios from Cambium and ISO historical prices. Values are shown as
percentages.
Capacity factor [%]
Scenario BWRX-300 UK-SMR SMR-160 NuScale Aurora-15 Xe-100
Mid Case 100 62.1 81.8 81.7 80.7 81.2 84.7
High RE Cost 47.4 85.3 84.7 83.6 85.2 89.5
High NG Prices 52.9 80.8 80.1 79.3 80.9 84.9
PJM 68.8 99.6 99.6 99.5 99.5 99.8
ERCOT 51.3 97.2 97.2 96.7 96.9 98.3
CAISO 72.4 96.3 96.3 96.2 96.2 96.9
order to improve economic prospects by minimizing intra-
hourlosses,SMRsaremorelikelytoutilizeflexibleramping
features than operate as baseload power, dropping average
lifetime capacity factors to 47.4% in some price scenarios.
In the price scenario Mid Case 100 where SMRs perform
the best, capacity factors average 78.7% across reactors,
significantly lower than their expected values of 92% U.S.
Department of Energy, Office of Nuclear Energy, and of
currentbaseloadnuclearpowerplantsat93.4%U.S.Depart-
mentofEnergy(b).Additionally,ifSMRswereabletoramp
to zero power, capacity factors would drop further by 7%
in most scenarios. At this level, SMRs would be operating
at similar capacity factors as rapid ramping Natural Gas
plants, which have average capacity factors of 59.9% U.S.
Department of Energy (b).
Evidence suggests that the high SMR marginal costs
discussed so far may be a trade-off by manufacturers in
an effort to reduce upfront investment costs. A majority
of concepts experience higher fuel costs than traditional
reactorsastheyusehigherenrichmentfuelssuchasHALEU,
or need significant investments into new supply chains such
as TRISO fuels Larsen, Kim, Richards, Kim, Davidson,
Asgari, Bae and Abou-Jaoude (2025); Ashton; Valdmanis.
This is observed in this work through average SMR fuel
costsinthecompileddatasetofmanufacturerprovidedcosts
being $23.69 𝑀𝑊 ℎ,significantlyhigherthantraditionalnuclearre- actorsutilizedasbaseloadpowerexperiencingcostsbetween
$9
𝑀𝑊 ℎ and $11 𝑀𝑊 ℎ. Literature also shows that concepts using traditional fuels such as NuScale are expected to have fuel
costs 15% to 70% higher than traditional reactors Pannier
and Skoda (2014), pointing to a possible industry-wide
trend.Additionally,withhigherfixedcostsaveraging $21.81 𝑀𝑊 ℎ, observable in Figure 1, operating and fuel costs of SMRs
total to $45.5 𝑀𝑊 ℎ, significantly higher than the average prices of all historical and non-decarbonization based scenarios
except for Mid Case 100 in Table 3. A possible explanation
P. Rao et al.:Preprint submitted to ElsevierPage 7 of 17

Consequences of high SMR operating costs
Figure 4:Discounted Payback Periods, dark green corresponding to 80 years, of selected SMR prototypes as a function of average
energy and capacity prices.
for high SMR operating costs is that these concepts were
designedforahighpriceenvironment,withNuScale’searly
designs expecting wholesale energy prices of$75 𝑀𝑊 ℎ Inger- soll,Houghton,BrommandDesportes(2014),andOKLO’s
Aurora-15 expecting prices of$105 𝑀𝑊 ℎ Oklo Inc. (2023).
3.2. Investment Viability with Energy and
Capacity Revenues
Evaluatingeconomicperformancesolelyondispatching
to energy markets runs into the “missing money problem"
- where the prices for energy do not reflect the true in-
vestment and operational costs necessary for reliable power
grid operation Hogan (2017). While dispatchable resources
can avail themselves of ancillary services revenue in some
ISOs/RTOs,previousworkhasshownthatco-biddingstrate-
gieswithenergyandancillaryservicemarketsresultina4%
increase in yearly revenues under historical CAISO prices
Alhadhrami et al. (2023). This translates to an average im-
pact of 0.43 years on discounted payback periods. Capacity
markets, on the other hand, are a construct used to mitigate
themissingmoneyproblemTarufelli,EldridgeandSomani,
and provide a rich source of potential additional revenue for
thermalgenerators.RecentrisesincapacitypricesHowland
(b); Walton; Howland (a), such as PJM’s 2025/26 capacity
prices soaring to $269.92 𝑀𝑊−𝑑𝑎𝑦 from $28.92 𝑀𝑊−𝑑𝑎𝑦 Howland (c),
translating to $8.21 𝑘𝑊−𝑚𝑜𝑛𝑡ℎ and $0.88 𝑘𝑊−𝑚𝑜𝑛𝑡ℎ respectively, means that a key factor in the private investment viability of Small
Modular Reactors are the role of capacity revenues.
As such, this work explores how current capacity pay-
mentlevelswouldimpactprivateinvestmentfeasibility,and
what average lifetime price levels would be necessary to
overcome intra-hour energy market losses from high op-
erating costs. To simulate this, average lifetime electricity
prices that do not contain temporal variability and volatility
features of the electricity price profiles used in Section 3.1
were used.
Results show that the dominant sensitivity of SMR pay-
backperiodsistowholesaleenergyprices.Ifcapacityprices
rangearoundhistoricallevels,asillustratedinFigure2,rev-
enues are insufficient to overcome intra-hour energy market
losses,andofferminimalimprovementstopaybackperiods.
As such, this work finds that for capacity payments to offer
noticeable improvements in payback periods, average life-
time prices need to significantly exceed historic highs hit in
PJM’s 2027/28 auction of $10.14 𝑘𝑊−𝑚𝑜𝑛𝑡ℎ . Determining what combination of electricity price and
capacity price is necessary for SMRs to find private in-
vestment feasibility is highly contextual. SMR concepts
vary in cost structures, construction periods, refueling time
and number of modules. As such, capacity and electricity
price benchmarks should be evaluated on the basis of the
SMR concept. Analyzing the performance of current SMR
concepts, most are still unable to achieve payback periods
of 20 years or less within the defined quadrant of economic
feasibility based on historical price data. 12 out of the
22 concepts do not achieve payback periods of less than
20 years even if average lifetime prices were at ERCOT’s
P. Rao et al.:Preprint submitted to ElsevierPage 8 of 17

Consequences of high SMR operating costs
Figure 5:[Left] Discounted Payback Periods as a function of the duration and rate of the PTC. [Right] Discounted Payback
Periods as a function of the PTC and Capacity Price.
2023 price of $65.13 𝑀𝑊 ℎ and NYISO’s 2023 capacity price of
$19.46
𝑘𝑊−𝑚𝑜𝑛𝑡ℎ . Intra-hour energy market losses from high op- erating costs are so high for the CEFR and CAREM SMR
concepts that they are unable to achieve payback periods
below their technical lifetimes even if capacity and energy
prices reached $100 𝑘𝑊−𝑚𝑜𝑛𝑡ℎ and $100 𝑀𝑊 ℎ, respectively. Considering that the average payback period of a solar
PV or onshore wind plant is between 2-20 years Chang and
Starcher (2019), SMRs are less likely to be competitive as
an investment opportunity, even considering both energy
and capacity revenues. This is punctuated further by the
fact that SMRs avail themselves of greater proportions of
capacity revenues due to their higher ELCC’s (Effective
Load Carrying Capacity), essentially the assumed capacity
factor, of around 95% compared to 10-60% for wind and
solar Pham, Cole and Gagnon (2024). It should be noted
that 2-20 year payback periods for wind and solar systems
areincludingtaxcredits,sowhetherSMRswouldbeableto
achievesimilareconomicperformancewiththeinclusionof
tax credits is the focus of the following section. Particularly
of interest is whether a combination of policy support along
with energy and capacity revenues is sufficient to achieve
private investment feasibility.
3.3. Impacts of Policy Support
Tax credits havebeen a centerpiece of financingnuclear
power projects to improve private investment feasibility. In
fact,mostnuclearprojectsonlybecomebankableforprivate
investors after de-risking through government involvement
WeibezahnandSteigerwald(2024).Withtheintroductionof
the Clean Electricity Investment Credit and Zero-Emission
Nuclear Power Production Credit in the 2022 Inflation Re-
ductionActInternalRevenueService(a,c),SMRsinservice
after 2024 can choose to subsidize either a portion of their
investment cost or receive an operational credit for up to 10
years.
Analyzing these policy support mechanisms, this work
finds that maximum available levels of the investment tax
credits, currently the 50% rate, are insufficient to improve
paybackperiodsofmostSMRconceptsbelowtheirtechnical
lifetimesinalmostallscenarios.Additionally,theITCwould
need to cover more than 75% of investment costs for sub-20
yearpaybackperiods,andforsomeSMRs,eveniftaxcredits
covered the whole cost of construction, it is still insufficient
to improve payback periods below technical lifetimes. This
finding punctuates the impact of escalated operating costs
oneconomicfeasibility,whereevenzeroinvestmentcostsof
some SMRs such as Rolls Royce’s UK-SMR and NuScale’s
VOYGR are unable to compensate for intra-hour losses.
Production tax credits (PTC) on the other hand, directly
impact marginal cost competitiveness. Figure 5 illustrates
discountedpaybackperiodsasafunctionofPTCpayout,el-
igibility period and capacity price. Private investment feasi-
bilityisdefinedasachievingsub-20yeardiscountedpayback
periods with PTC rates and capacity revenues at optimistic
benchmarks. This is defined as at or under the maximum
level of the PTC at $33 𝑀𝑊 ℎ for a period of 10 years, and average lifetime capacity prices under the historical high of
the PJM 2027/28 auction price of$10.14 𝑘𝑊−𝑚𝑜𝑛𝑡ℎ . Mid Case 100, theoptimisticpricescenarioinwhichSMRsperformedbest,
was used to analyze PTC and capacity price impacts.
Observing the effects of the PTC only in Figure 5, two
thingsareapparent.First,PTCdurationbeyond10yearshas
nominal effects on payback periods, as most of the value
is captured in the early years. Second, a threshold effect is
observable with the rate of the PTC, where payback periods
only improve after a certain PTC rate is achieved, with the
ratedependingontheSMRcoststructure.Benchmarkingto
the feasibility standard defined earlier, this work finds that
currentlevelsofthePTC,ifSMRswereabletoclaimthem,
are insufficient to make the majority of concepts attractive
to private investment. While concepts such as GE-Hitachi’s
BWRX-300 and OKLO’s Aurora-15 are able to achieve 20-
year payback periods at or under Inflation Reduction Act
(IRA)PTClevels,18outof22consideredSMRswouldnot.
With the ability to capture capacity revenues in addition
to production tax credits, average lifetime capacity prices
havealargerinfluencethanthePTConfeasibility.Duration
P. Rao et al.:Preprint submitted to ElsevierPage 9 of 17

Consequences of high SMR operating costs
0 20 40 60 80 100 120 140
Marginal Cost ($/MWh)
0
5000
10000
15000
20000Investment Cost ($/kWe)
(a) 20-Year Payback
0 20 40 60 80 100 120 140
Marginal Cost ($/MWh)
(b) 40-Year Payback
Reactor designs CAISO Mid Case 100 + PTC + PTC + CM
Figure 6:Investment and marginal cost breakeven tradeoff curves for 20- and 40-year payback periods with current manufacturer
costs as data points. Tradeoff curves are calculated for policy support (+PTC) and capacity revenues (+PTC + CM).
Table 6:Investment cost upper bounds to achieve a 20-year payback period under baseload marginal costs ($12/MWh) and SMR
manufacturer-advertised marginal costs ($25/MWh).
Scenario Baseload [$/kWe] SMR [$/kWe]
Mid Case 100 4,699.71 3,936.77
Mid Case 100 + PTC $33/MWh 6,378.18 5,468.75
Mid Case 100 + ITC 30% 5,996.98 4,979.36
Mid Case 100 + Capacity Rate $10.14/kW-month 5,859.42 5,078.13
Mid Case 100 + PTC + Capacity Rate 7,812.50 6,274.43
CAISO 3,222.66 2,050.78
CAISO + PTC $33/MWh 5,151.94 3,906.25
CAISO + ITC 30% 4,049.40 2,610.33
CAISO + Capacity Rate $10.14/kW-month 4,345.70 3,131.68
CAISO + PTC + Capacity Rate 6,250.10 4,739.38
Reference costs:Xe-100 ($7,500/kWe), BWRX-300 ($2,250/kWe), NuScale ($3,466/kWe), Vogtle 3&4 if built today ($15,000/kWe), NOAK AP1000
($4,625/kWe), and Moderate AP1000 ($7,616/kWe).
of the PTC in particular becomes less influential with the
availabilityofcapacityrevenues.HowevermostSMRs,with
the exception of a few reactors such as BWRX-300 and
Aurora-15, necessitate capacity prices and PTC rates in
excessofhistorichighstobefeasibleforprivateinvestment.
What should be noted is that if policy makers were to raise
the PTC to $95 𝑀𝑊 ℎ, to better reflect the social cost of carbon Rennertetal.(2022)ofavoidedemissions(primarilynatural
gas at roughly 0.5 tons/MWh), most SMRs would be able
to achieve payback periods below 20 years, with or without
capacity revenues. For context, wind plants are found to
be competitive at $21 𝑀𝑊 ℎ Lu, Tchou, McElroy and Nielsen
(2011), with current base rates of the PTC starting at$30 𝑀𝑊 ℎ
Internal Revenue Service (b).
Formanyconcepts,SMRfixedcostsareasignificantde-
terminant towards private investment feasibility. For exam-
ple, NuScale’s VOYGR advertises an annual fixed costs of
$185,000,000 for an 8-module plant Ingersoll et al. (2014),
which alone overshadows projected energy market and sup-
plementary capacity market revenues. This is also observed
in the larger influence of capacity revenues as compared to
productiontaxcreditsoneconomicfeasibility.Capacityrev-
enues supplement both investment and operating costs. As
previous findings of this work showed investment subsidies
having low impacts on payback periods, this suggests that
the primary function of capacity revenues for most SMRs
is reducing the burden of fixed costs. However, between
fixedoperatingandmarginalcosts,mostSMRsarestillmore
sensitive to marginal costs due to their influence on bidding
P. Rao et al.:Preprint submitted to ElsevierPage 10 of 17

Consequences of high SMR operating costs
behavior into wholesale energy markets, which remain the
largest revenue stream.
3.4. Breakeven investment and marginal costs
tradeoffs
This work has thus far explored the projected poor per-
formance of SMRs in electricity markets, driven by higher
marginal costs for SMRs. Previously, this work presented
some evidence that SMR manufacturers may have executed
atradeoffforlowerinvestmentcostsbyincreasingoperating
and marginal costs. This section seeks to observe whether
that tradeoff exists, and quantify it under various economic
conditions. Considering that investor reticence for tradi-
tional nuclear has been driven by escalation of investment
costsLocatelli(2018),thissectionalsoquantifiestheimpact
of reducing SMR marginal costs on the ceiling for invest-
ment costs.
A generic 300MWe SMR was simulated under the best
performing price scenarios, the CAISO Historical and Mid
Case 100, and tradeoff curves representing the highest pos-
sible investment cost at each marginal cost level were built
foragivenpaybackperiod,asillustratedinFigure6.Curves
were also calculated with both high policy support and high
capacity revenues. PTC at $33 𝑀𝑊 ℎ Abou-Jaoude et al. (2024)
and lifetime average capacity prices of$10.14 𝑘𝑊−𝑚𝑜𝑛𝑡ℎ were used as benchmarks for high price and policy support. Two pay-
back period standards, 40 and 20 years, were then used to
explore private investment feasibility. Table 6 outlines the
largest investment cost that can be incurred under various
scenarios at baseload and current SMR average marginal
costs extracted from tradeoff curves.
Results show the clear existence of a tradeoff between
marginal and investment costs under all scenarios, as a neg-
ative correlation is observed. This observation is significant
asitemphasizesakeyresultofthiswork:reducedinvestment
costsdonotnecessarilyleadtomoreeconomicoutcomes,if
they come at the expense of higher marginal costs. Observ-
ing Figure 6 for how current concepts perform under this
paradigm, this work finds that under current investment and
marginalcoststructures,themajorityofSMRsexpecttopay
back in 40 years only with an expectation of a high policy
and price environment.
Further strengthening earlier findings of this work on
marginal costs can be found by observing the slopes of
the tradeoff curves in Figure 6. Steeper curves in the 20
year compared to the 40 year payback period plot speak
to the dominance of marginal costs as the target payback
period is reduced. For SMRs to be more feasible for private
investment, improvements in marginal costs pay larger div-
idends than investment cost reductions. On average across
thepricescenarios,ifSMRsweretoimprovemarginalcosts
from current levels of $25 𝑀𝑊 ℎ to baseload costs of $12 𝑀𝑊 ℎ
National Renewable Energy Laboratory (2024), investment
cost ceilings can be relaxed by 30%.
Historically high wholesale and capacity prices, with
high policy subsidies enable a maximum investment cost
of $7,813 𝑘𝑊 𝑒 at baseload marginal costs and $6,259 𝑘𝑊 𝑒 at current
averageSMRmarginalcosts.Whilecurrentinvestmentcosts
ofSMRsareunclear,ifNuScale’searlyNOAKbenchmarks
of $20,139 𝑘𝑊 𝑒 Schlissel are any indication, it is likely that SMRs
would have to achieve steep reductions, at best around 60%
if both marginal cost reductions as well as high policy and
price environment. Most likely, SMRs may have to achieve
investment cost reductions at a rate similar to Utility PV
over the past two decades, greater than 80% Ramasamy,
Zuboy,Feldman,Narayanaswami,WoodhouseandMargolis
(2025), in order to be feasible for private investment.
3.5. Investment cost escalation and comparison
with traditional nuclear
Private investment feasibility of nuclear power has been
traditionally been highly sensitive to their investment costs.
While this work has shown marginal costs as the primary
driverbehindpoorprojectedperformanceforSMRs,nuclear
power historically has experienced investment cost escala-
tions of 117% on 97% of all projects Sovacool, Gilbert and
Nugent (2014).
A similar increase in investment costs for SMRs, as
seen in Figure 7, increases the average lifetime electric-
ity prices required to achieve sub-20 year payback periods
on average by $25 𝑀𝑊 ℎ, resulting in almost all SMRs being unable to achieve the investment feasibility standard. Even
optimistic concepts such as OKLO’s Aurora-15 and GE-
Hitachi’sBWRX-300hoverontheedgeofinvestmentfeasi-
bility under escalated costs.
How SMRs compare to traditional nuclear reactors, es-
pecially to Georgia Power’s Vogtle 3 & 4 units that entered
operation in 2024, is used as a benchmark of whether the
economicperformanceofnuclearpowerhasimprovedinthe
transition to SMRs. Building Vogtle resulted in significant
cost and schedule overruns and the bankruptcy of its man-
ufacturer (Westinghouse) Spangler, Qin, Larsen, Bolisetti,
Abou-Jaoude, Shirvan, Asgari, Stewart, Krellenstein and
Wilkinson (2025). SMRs would need to significantly im-
prove on the experience of Vogtle to achieve private invest-
ment feasibility.
Realized Vogtle costs and projected future AP1000 cost
sets were simulated to compare performance under energy
andcapacitymarketstructures,seeninFigure8.Thiswork’s
final finding is that if SMRs experience investment cost
escalations,atarateoutlinedinFigure7,themajorityofthe
conceptswillhaveaperformanceprofilesimilartomoderate
andconservativeestimatesoftheVogtle3&4,aswellasthe
projected future builds of the AP1000.
Additionally, NOAK and advanced estimates of the
AP1000 perform similarly to most SMRs at manufacturer
estimates. If the SMR manufacturer estimates are NOAK
too, the perceived benefits of the transition to SMRs are
broughtintoquestion.WhileSMRsarelesscapitalintensive,
how private investment feasibility would be impacted if the
concepts had similar economic performance as traditional
reactors is unclear.
P. Rao et al.:Preprint submitted to ElsevierPage 11 of 17

Consequences of high SMR operating costs
Figure 7:Effects of cost escalation on the average lifetime electricity price required to achieve target payback periods of 5, 20, and
40 years. Missing bars indicate that prices must exceed$100∕MWhto achieve the target payback period. With a 117% increase
in investment costs, average electricity prices necessary to achieve sub-20-year payback periods increase significantly.
Figure 8:Payback periods of AP1000 cost scenarios as a function of electricity and capacity prices. SMR economic performance
at escalated investment costs is similar to the AP1000.
P. Rao et al.:Preprint submitted to ElsevierPage 12 of 17

Consequences of high SMR operating costs
4. Conclusion and Policy Implications
Theresultsofthisworkdemonstratethatoperationalcost
escalation of SMRs drive their poor project performance in
ISO electricity markets, with and without policy support.
In an effort to reduce upfront investment cost for SMRs,
design tradeoffs such as using novel fuels that do not have
established supply chains most likely ballooned operational
and marginal costs. As a result, intra-hour losses from op-
erating the SMRs overshadow any upfront investment cost
advantages.
As a consequence, SMRs require an environment of
ISO market prices and public subsidies beyond historic
highs to attract private investment at manufacturer adver-
tised cost benchmarks, with almost all concepts unable to
achievediscountedpaybackperiodslessthantheirtechnical
lifetimes. Average lifetime capacity prices need to exceed
PJM’s historic high 2025/26 auction price, which caused
the Commonwealth of Pennsylvania to threaten to leave
PJM Howland (d). Policy support for investment costs are
generally shown to be ineffective, where for some SMRs,
eveniftheITCsubsidizedtheentirecostofconstructionitis
stillinsufficienttoimprovepaybackperiodsbelowtechnical
lifetimes. However, if policy makers were to raise the PTC
to $95 𝑀𝑊 ℎ, to better reflect the social cost of carbon Rennert et al. (2022) of avoided emissions (primarily natural gas
at roughly 0.5 tons/MWh), most SMRs would be able to
achieve payback periods below 20 years, with or without
capacity revenues.
If cost reductions were to be made, improvements in
marginal costs pay larger dividends than investment cost
reductions. If SMR marginal costs improved to baseload
traditional nuclear levels at $12 𝑀𝑊 ℎ, investment cost bench-
markscanberelaxedbyanaverageof30%,withamaximum
investment cost of$7,813 𝑘𝑊 𝑒 under high wholesale and capacity prices, supplemented with high PTC rates.
Comparing performance to traditional nuclear reactors,
this work finds that SMRs at manufacturer estimates are as
profitableasestimatesofWestinghouse’sAP1000.Ifmanu-
facturerinvestmentcostestimatesweretoincreaseattheav-
erage historical nuclear power plant rate, SMRs would have
similarprofitabilitytoVogtle3&4.Thissharplybringsinto
question the benefits of the transition to advanced nuclear
plants, especially since traditional plants enjoy economies
of scale that SMRs lack.
Future work to explore the operational value of nuclear
power to a power grid would be beneficial, as well as an
examination of performance under global electricity market
structures. Additionally, performance under novel proposed
market structures in the United States should be explored,
especially with a focus on future power grid scenarios.
5. Acknowledgments
The authors would like to thank Dr. Charles F. Kutscher
for his review and helpful feedback throughout the process
of this paper.
CRediT authorship contribution statement
PradyumnaRao:Conceptualizationofthisstudy,Data
curation, Methodology, Software, Writing - Original draft
preparation.Daniel T. Kaffine:Conceptualization of this
study,Writing-Review&Editing,Supervision.Bri-Mathias
Hodge:Conceptualizationofthisstudy,Writing-Review&
Editing, Investigation, Supervision.
P. Rao et al.:Preprint submitted to ElsevierPage 13 of 17

Consequences of high SMR operating costs
A. Additional Reactor Data
Table7:Fulllistofmanufacturer-advertisedcostdatatakenfromSteigerwaldetal.(2023)andexpandedbyaddingadditional
concepts.MissingvariablecostdatauseLazard2024assumptionsLazard(2024).Fixedcostshavebeenconvertedto$/MWh
for comparison purposes.
Project Capacity [MWel] Investment Cost [$/MWel] Fuel Cost [$/MWh] Fixed O&M Cost [$/MWh] Variable O&M Cost [$/MWh]
BWRX-300 300.0 2,250,000 8.44 16.00 3.55
UK-SMR 443.0 5,215,937 10.95 68.00 3.55
SMR-160 160.0 6,312,500 14.48 11.83 3.55
SMART 107.0 10,186,916 4.88 7.44 3.55
NuScale 77.0 3,466,000 17.42 72.26 3.55
RITM 200M 53.0 4,212,000 26.82 19.18 3.55
ACPR 50S 40.0 8,532,000 16.73 11.83 3.55
KLT-40S 35.0 13,531,429 91.18 19.18 3.55
CAREM 30.0 23,187,500 19.24 17.13 3.55
EM2 265.0 4,373,300 11.97 11.91 3.55
HTR-PM 105.0 5,400,000 15.47 18.95 3.55
PBMR-400 165.0 1,550,000 8.63 16.74 3.55
ARC-100 100.0 5,050,000 27.15 19.93 0.31
CEFR 20.0 23,034,536 113.05 19.93 3.55
4S 10.0 2,500,000 48.67 38.99 17.26
IMSR (300) 195.0 4,054,266 8.12 18.69 3.55
SSR-W 37.5 1,950,000 21.63 13.85 3.55
e-Vinci 3.5 5,771,429 2.35 22.75 3.55
Brest-OD-300 300.0 4,160,000 30.62 26.27 3.55
Aurora-15 Oklo Inc. (2023) 15.0 3,800,000 13.41 15.51 4.25
Aurora-50 Oklo Inc. (2023) 50.0 2,320,000 6.64 10.86 3.40
Xe-100 X-Energy Reactor Company, LLC and Ares Acquisition Corporation (2022) 80.0 7,500,000 3.39 2.50 3.55
I
Table 8: Additional operational data for SMR concepts.
Project Lifetime [yr] # Modules Construction Duration [mo.] Refueling Minimum Time [mo.] Refueling Maximum Time [mo.]
BWRX-300 60 1 26 12 24
UK-SMR 60 1 24 18 24
SMR-160 80 2 36 20 26
SMART 60 1 36 27 33
NuScale 60 12 36 15 18
RITM 200M 60 2 48 51 57
ACPR 50S 40 1 30 26 32
KLT-40S 40 2 48 30 36
CAREM 40 1 108 12 16
EM2 60 4 42 15 18
HTR-PM 40 2 48 32 36
PBMR-400 40 1 34 70 74
ARC-100 60 1 54 230 250
CEFR 30 1 120 15 18
4S 60 1 12 360 360
IMSR (300) 60 2 55 80 88
SSR-W 60 8 31 80 88
e-Vinci 40 2 12 36 96
Brest-OD-300 30 4 60 29 48
Aurora-15 Oklo Inc. (2023) 40 1 12 118 120
Aurora-50 Oklo Inc. (2023) 40 1 12 118 120
Xe-100 X-Energy Reactor Company, LLC and Ares Acquisition Corporation (2022) 60 4 36 6 12
References
Abou-Jaoude,A.,Lohse,C.S.,Larsen,L.M.,Guaita,N.,Trivedi,I.,Joseck,
F.C., Hoffman, E., Stauff, N., Shirvan, K., Stein, A., 2024. Meta-
AnalysisofAdvancedNuclearReactorCostEstimations. TechnicalRe-
port. Idaho National Laboratory (INL), Idaho Falls, ID (United States).
URL:https://www.osti.gov/biblio/2371533, doi:10.2172/2371533.
Adamantiades,A.,Kessides,I.,2009. Nuclearpowerforsustainabledevel-
opment: Current status and future prospects. Energy Policy 37, 5149–
5166. URL:https://www.sciencedirect.com/science/article/pii/
S0301421509005436, doi:https://doi.org/10.1016/j.enpol.2009.07.052.
Alhadhrami, S., Soto, G.J., Lindley, B., 2023. Dispatch analysis of flexible
power operation with multi-unit small modular reactors. Energy 280,
128107. URL:https://www.sciencedirect.com/science/article/pii/
S0360544223015013, doi:10.1016/j.energy.2023.128107.
Amazon, 2024. Amazon Signs Agreements for Innovative
Nuclear Energy Projects to Address Growing Energy Demands.
URL:https://www.aboutamazon.com/news/sustainability/
amazon-nuclear-small-modular-reactor-net-carbon-zero.
Ansolabehere, S., Deutch, J., Driscoll, M.J., Gray, P.E., Holdren, J.P.,
Joskow, P.L., Lester, R.K., Moniz, E.J., Todreas, N.E., Beckjord, E.S.,
Hottle, N., Jones, C., Parent, E., 2003. The Future of Nuclear Power:
ATechnicalandEconomicAssessment. URL:https://energy.mit.edu/
wp-content/uploads/2003/07/MITEI-The-Future-of-Nuclear-Power.pdf.
Argonne National Laboratory, 2024. Nuclear Fuel Cycle Cost Calculator.
URL:https://cnpce.ne.anl.gov/cgi-bin/qnecost?select=main_page.
Ashton, L., . Fuelling the Future: Building Fuel
Supply Chains for SMRs and Advanced Reactors
64, 16–17. URL:https://www.iaea.org/bulletin/
fuelling-the-future-building-fuel-supply-chains-for-smrs-and-advanced-reactors.
Barcelona, R.G., 2015. Renewable energy with volatile prices: Why
npv fails to tell the whole story. Journal of Applied Corporate
Finance 27, 101–109. URL:https://onlinelibrary.wiley.com/doi/
abs/10.1111/jacf.12109, doi:https://doi.org/10.1111/jacf.12109,
arXiv:https://onlinelibrary.wiley.com/doi/pdf/10.1111/jacf.12109.
P. Rao et al.:Preprint submitted to ElsevierPage 14 of 17

Consequences of high SMR operating costs
Chang, B., Starcher, K., 2019. Evaluation of wind and solar
energy investments in texas. Renewable Energy 132, 1348–
1359. URL:https://www.sciencedirect.com/science/article/pii/
S0960148118311005, doi:https://doi.org/10.1016/j.renene.2018.09.037.
Corporation, C.E., 2024. Constellation to launch crane clean
energy center, restoring jobs and carbon-free power to the
grid. URL:https://www.constellationenergy.com/newsroom/2024/
Constellation-to-Launch-Crane-Clean-Energy-Center-Restoring-Jobs-and-Carbon-Free-Power-to-The-Grid.
html.
Driouchi, T., Bennett, D.J., 2012. Real options in management and
organizational strategy: A review of decision-making and performance
implications. International Journal of Management Reviews 14, 39–62.
URL:https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1468-2370.
2011.00304.x, doi:https://doi.org/10.1111/j.1468-2370.2011.00304.x,
arXiv:https://onlinelibrary.wiley.com/doi/pdf/10.1111/j.1468-2370.2011.00304.x.
Farmer, M., 2022. Rolls Royce Plans First UK Modular Nuclear
Reactor for 2029. URL:https://www.power-technology.com/news/
uk-first-smr-rolls-royce/.
Froese, S., Kunz, N.C., Ramana, M., 2020. Too small to be vi-
able? the potential market for small modular reactors in min-
ing and remote communities in canada. Energy Policy 144,
111587. URL:https://www.sciencedirect.com/science/article/pii/
S030142152030327X, doi:https://doi.org/10.1016/j.enpol.2020.111587.
Gagnon, P., Sanchez Perez, P., Obika, K., Schwarz, M., Morris, J., Gu,
J., Eisenman, J., 2024. Cambium 2023 scenario descriptions and
documentation. doi:10.2172/2316014.
Grubler, A., 2010. The costs of the french nuclear scale-up: A
case of negative learning by doing. Energy Policy 38, 5174–
5188. URL:https://www.sciencedirect.com/science/article/pii/
S0301421510003526, doi:https://doi.org/10.1016/j.enpol.2010.05.003.
Haratyk, G., 2017. Early nuclear retirements in deregulated u.s. mar-
kets: Causes, implications and policy options. Energy Policy 110,
150–166. URL:https://www.sciencedirect.com/science/article/pii/
S0301421517305177, doi:https://doi.org/10.1016/j.enpol.2017.08.023.
Hogan, B., 2010. Address by the Minister of Public Enterprises,
Barbara Hogan, to the National Assembly, on the Pebble Bed
Modular Reactor. URL:https://www.gov.za/news/speeches/
address-minister-public-enterprises-barbara-hogan-national-assembly-pebble-bed.
Hogan, M., 2017. Follow the missing money: Ensuring reliability
at least cost to consumers in the transition to a low-carbon
power system. The Electricity Journal 30, 55–61. URL:https:
//www.sciencedirect.com/science/article/pii/S1040619016302512,
doi:https://doi.org/10.1016/j.tej.2016.12.006.
Howland,E.,a. MISOSummerCapacityPricesJumpto$666.50/MW-Day
asPowerSuppliesShrink.Utility Dive. URL:https://www.utilitydive.
com/news/miso-capacity-auction/746576/. april 2025.
Howland, E., b. PJM Capacity Prices Set Another Record with
22% Jump.Utility Dive. URL:https://www.utilitydive.com/news/
pjm-interconnection-capacity-auction-prices/753798/. july 2025.
Howland, E., c. Reregulation? How Utilities and States
Are Responding to PJM’s Record Capacity Prices.
Utility Dive. URL:https://www.utilitydive.com/news/
pjm-capacity-auction-results-firstenergy-exelon-aep/725952/.
october 2024.
Howland, E., d. States Threaten to Leave PJM Without Expanded Role
in Grid Operator.Utility Dive. URL:https://www.utilitydive.com/
news/governors-states-pjm-governance-conference-capacity/760842/.
september 2025.
Ingersoll, D., Houghton, Z., Bromm, R., Desportes, C., 2014.
Nuscale small modular reactor for co-generation of electricity
and water. Desalination 340, 84–93. URL:https://www.
sciencedirect.com/science/article/pii/S0011916414000885,
doi:https://doi.org/10.1016/j.desal.2014.02.023.
Internal Revenue Service, a. Clean Electricity Investment
Credit. URL:https://www.irs.gov/credits-deductions/
clean-electricity-investment-credit.
Internal Revenue Service, b. Clean Electricity Production
Credit. URL:https://www.irs.gov/credits-deductions/
clean-electricity-production-credit.
Internal Revenue Service, c. Zero-Emission Nuclear Power Pro-
duction Credit. URL:https://www.irs.gov/credits-deductions/
zero-emission-nuclear-power-production-credit.
International Atomic Energy Agency, . Advanced Reactor Information
System (ARIS). URL:https://aris.iaea.org/.
International Atomic Energy Agency, 2024. Small
Modular Reactors: Advances in SMR Developments
2024. URL:https://www.iaea.org/publications/15790/
small-modular-reactors-advances-in-smr-developments-2024,
doi:10.61092/iaea.3o4h-svum.
Kim, P., Macfarlane, A., 2026. Challenges of small modular
reactors: A comprehensive exploration of economic and waste
uncertainties associated with u.s. small modular reactor designs.
Progress in Nuclear Energy 190, 105989. URL:https:
//www.sciencedirect.com/science/article/pii/S0149197025003877,
doi:https://doi.org/10.1016/j.pnucene.2025.105989.
Kuznetsov, V., 2008. Options for small and medium sized
reactors (smrs) to overcome loss of economies of scale and
incorporate increased proliferation resistance and energy security.
Progress in Nuclear Energy 50, 242–250. URL:https:
//www.sciencedirect.com/science/article/pii/S0149197007001400,
doi:https://doi.org/10.1016/j.pnucene.2007.11.006. innovative
Nuclear Energy Systems for Sustainable Development of the World.
Proceedings of the Second COE-INES International Symposium,
INES-2, November 26-30, 2006, Yokohama, Japan.
Larsen, L.M., Kim, J., Richards, S., Kim, T.K., Davidson, E., Asgari,
M., Bae, J., Abou-Jaoude, A., 2025. Infrastructure and resource
development needs to support a significant expansion of us nuclear
capacity. Energy Strategy Reviews 62, 101876. URL:https:
//www.sciencedirect.com/science/article/pii/S2211467X25002391,
doi:https://doi.org/10.1016/j.esr.2025.101876.
Lazard,2024. Lazard’sLevelizedCostofEnergy+. Report.Lazard. URL:
https://www.lazard.com/media/xemfey0k/lazards-lcoeplus-june-2024-_
vf.pdf.
Locatelli, G., 2018. Why Are Megaprojects, Including Nuclear Power
Plants, Delivered Overbudget and Late? Reasons and Remedies. Tech-
nical Report MIT-ANP-TR-172. Center for Advanced Nuclear Energy
Systems, Massachusetts Institute of Technology. URL:https://arxiv.
org/abs/1802.07312,arXiv:1802.07312.
Locatelli,G.,Boarin,S.,Pellegrino,F.,Ricotti,M.E.,2015. Loadfollowing
with small modular reactors (smr): A real options analysis. Energy
80, 41–54. URL:https://www.sciencedirect.com/science/article/pii/
S036054421401295X, doi:https://doi.org/10.1016/j.energy.2014.11.040.
Lu, X., Tchou, J., McElroy, M.B., Nielsen, C.P., 2011. The impact
of production tax credits on the profitable production of electricity
from wind in the u.s. Energy Policy 39, 4207–4214. URL:https:
//www.sciencedirect.com/science/article/pii/S030142151100317X,
doi:https://doi.org/10.1016/j.enpol.2011.04.034. special Section:
Renewable energy policy and development.
Millstein, D., O’Shaughnessy, E., Wiser, R., 2024. Renewables and
Wholesale Electricity Prices (ReWEP) Tool. URL:https://emp.lbl.
gov/renewables-and-wholesale-electricity-prices-rewep.
Mueller, M., . What Is Generation Capacity? URL:https://www.energy.
gov/ne/articles/what-generation-capacity.
National Renewable Energy Laboratory, 2024. 2024 Annual Technology
Baseline. URL:https://atb.nlr.gov/.
Nuclear Energy Agency, . The Economics of the Back End of the
Nuclear Fuel Cycle. Technical Report NEA No. 7061. OECD Nuclear
Energy Agency. URL:https://www.oecd.org/en/publications/
the-economics-of-the-back-end-of-the-nuclear-fuel-cycle_
9789264208520-en.html.
Nyamdash, B., Denny, E., 2013. The impact of electricity storage on
wholesale electricity prices. Energy Policy 58, 6–16. URL:https:
//www.sciencedirect.com/science/article/pii/S0301421512010154,
doi:https://doi.org/10.1016/j.enpol.2012.11.033.
Nøland, J.K., Hjelmeland, M., Hartmann, C., Tjernberg, L.B., Korpås,
M., 2025. Overview of small modular and advanced nuclear reactors
P. Rao et al.:Preprint submitted to ElsevierPage 15 of 17

Consequences of high SMR operating costs
and their role in the energy transition. IEEE Transactions on Energy
Conversion 40, 1933–1945. doi:10.1109/TEC.2025.3529616.
Oklo Inc., 2023. Investor Presentation: Oklo’s Aurora Powerhouse 15
MWe Liquid Metal Fast Fission Power Plant Site and Fuel Secured
for Commercial Plant Deployment at the Idaho National Labora-
tory. URL:https://s203.q4cdn.com/103172959/files/doc_presentation/
Oklo-Investor-Presentation-July-2023_vFinal.pdf.
Pannier, C.P., Skoda, R., 2014. Comparison of small modular reactor and
largenuclearreactorfuelcost. EnergyandPowerEngineering6,82–94.
doi:10.4236/epe.2014.65009.
Pham, A.T., Cole, W., Gagnon, P., 2024. Average and Marginal Capacity
Credit Values of Renewable Energy and Battery Storage in the United
States Power System. Technical Report. National Renewable Energy
Laboratory (NREL), Golden, CO (United States). URL:https://www.
osti.gov/biblio/2478444, doi:10.2172/2478444.
Pham, A.T., Lovdal, L., Zhang, T., Craig, M.T., 2022. A techno-
economic analysis of distributed energy resources versus
wholesale electricity purchases for fueling decarbonized heavy
duty vehicles. Applied Energy 322, 119460. URL:https:
//www.sciencedirect.com/science/article/pii/S0306261922007875,
doi:https://doi.org/10.1016/j.apenergy.2022.119460.
Portugal-Pereira,J.,Ferreira,P.,Cunha,J.,Szklo,A.,Schaeffer,R.,Araújo,
M., 2018. Better late than never, but never late is better: Risk as-
sessment of nuclear power construction projects. Energy Policy 120,
158–166. URL:https://www.sciencedirect.com/science/article/pii/
S0301421518303446, doi:https://doi.org/10.1016/j.enpol.2018.05.041.
Ramasamy, V., Zuboy, J., Feldman, D., Narayanaswami, M., Woodhouse,
M., Margolis, R., 2025. Documenting 15 Years of Reductions in U.S.
Solar Photovoltaic System Costs. URL:https://www.nlr.gov/docs/
fy25osti/92536.pdf.
Rennert, K., Errickson, F., Prest, B.C., Rennels, L., Newell, R.G., Pizer,
W.A., Kingdon, D., Anthoff, D., Cooke, R., Raftery, A.E., Ševčíková,
H., Watson, M., Hecke, G., Hardisty, J., Kobos, D., Fissel, D., McJeon,
J., Newell, P., Shindell, D., 2022. Comprehensive evidence implies a
higher social cost of CO2. Nature 610, 687–692. URL:https://doi.
org/10.1038/s41586-022-05224-9, doi:10.1038/s41586-022-05224-9.
Rothwell, G., 2010. International light water nuclear fuel fabrication
supply: Are fabrication services assured? Energy Economics 32,
538–544. URL:https://www.sciencedirect.com/science/article/pii/
S0140988309001492, doi:https://doi.org/10.1016/j.eneco.2009.08.012.
Sauter, A., Lara, J.D., Turk, J., Milford, J., Hodge, B.M., 2024.
Power system operational impacts of electric vehicle dynamic
wireless charging. Applied Energy 364, 123002. URL:https:
//www.sciencedirect.com/science/article/pii/S0306261924003854,
doi:https://doi.org/10.1016/j.apenergy.2024.123002.
Schlegel, J.P., Bhowmik, P., 2024. Chapter 14 - small modular
reactors, in: Wang, J., Talabi, S., y Leon, S.B. (Eds.), Nuclear
Power Reactor Designs. Academic Press, pp. 283–308. URL:https:
//www.sciencedirect.com/science/article/pii/B978032399880200014X,
doi:https://doi.org/10.1016/B978-0-323-99880-2.00014-X.
Schlissel, D., . Eye-Popping New Cost Estimates Released for
NuScale Small Modular Reactor.Institute for Energy Economics
and Financial Analysis. URL:https://ieefa.org/resources/
eye-popping-new-cost-estimates-released-nuscale-small-modular-reactor.
january 2023.
Schlissel, D., Wamsted, D., . Small Modular Reactors: Still Too
Expensive, Too Slow and Too Risky.Institute for Energy Economics
and Financial Analysis. URL:https://ieefa.org/resources/
small-modular-reactors-still-too-expensive-too-slow-and-too-risky.
may 2024.
Seel, J., Mills, A.D., Wiser, R.H., 2018. Impacts of High Variable
Renewable Energy Futures on Wholesale Electricity Prices, and on
Electric-Sector Decision Making. Report. Lawrence Berkeley Na-
tional Laboratory (LBNL). URL:https://emp.lbl.gov/publications/
impacts-high-variable-renewable. a webinar summarizing key findings
recorded on May 23, 2018, can be viewed online.
Shirvan, K., 2024. 2024 Total Cost Projection of Next AP1000. Tech-
nical report MIT-ANP-TR-201. Center for Advanced Nuclear Energy
Systems,MassachusettsInstituteofTechnology.URL:https://web.mit.
edu/kshirvan/www/research/ANP201%20TR%20CANES.pdf.
Sovacool,B.K.,Gilbert,A.,Nugent,D.,2014. Risk,innovation,electricity
infrastructure and construction cost overruns: Testing six hypotheses.
Energy 74, 906–917. URL:https://www.sciencedirect.com/science/
article/pii/S0360544214008925, doi:https://doi.org/10.1016/j.energy.
2014.07.070.
Spangler,R.,Qin,S.,Larsen,L.M.,Bolisetti,C.,Abou-Jaoude,A.,Shirvan,
K., Asgari, M., Stewart, W.R., Krellenstein, J., Wilkinson, G., 2025.
PotentialCostReductioninNewNuclearDeploymentsBasedonRecent
AP1000 Experience. Technical Report. Idaho National Laboratory
(INL), Idaho Falls, ID (United States). URL:https://www.osti.gov/
biblio/2571083, doi:10.2172/2571083.
Steigerwald, B., Weibezahn, J., Slowik, M., von Hirschhausen, C., 2023.
Uncertainties in estimating production costs of future nuclear technolo-
gies: A model-based analysis of small modular reactors. Energy 281,
128204. URL:https://www.sciencedirect.com/science/article/pii/
S0360544223015980, doi:https://doi.org/10.1016/j.energy.2023.128204.
Tarufelli,B.L.,Eldridge,B.C.,Somani,A.,. CapacityMarketsforTransac-
tiveEnergySystems. TechnicalreportPNNL-33381.PacificNorthwest
National Laboratory. URL:https://www.pnnl.gov/main/publications/
external/technical_reports/PNNL-33381.pdf, doi:10.2172/1995800. pre-
pared for the U.S. Department of Energy under Contract DE-AC05-
76RL01830.
Terrell, M., 2024. New Nuclear Clean Energy Agree-
ment with Kairos Power. URL:https://blog.google/
company-news/outreach-and-initiatives/sustainability/
google-kairos-power-nuclear-energy-agreement/.
United Nations, 2023. 1.5°C: What It Means and Why It Matters.
URL:https://www.un.org/en/climatechange/science/climate-issues/
degrees-matter.
U.S. Department of Energy, a. Advanced Nuclear. URL:https://www.
energy.gov/edf/advanced-nuclear.
U.S. Department of Energy, b. What Is Generation Capacity? URL:
https://www.energy.gov/ne/articles/what-generation-capacity.
U.S. Department of Energy, 2023. At COP28, Countries
Launch Declaration to Triple Nuclear Energy Capacity by
2050, Recognizing the Key Role of Nuclear Energy in
Reaching Net Zero. URL:https://www.energy.gov/articles/
cop28-countries-launch-declaration-triple-nuclear-energy-capacity-2050-recognizing-key.
U.S. Department of Energy, Office of Nuclear Energy, . New DOE
Report Examines How Incentives Used for Renewables Could Benefit
Small Modular Reactors. URL:https://www.energy.gov/ne/articles/
new-doe-report-examines-how-incentives-used-renewables-could-benefit-small-modular.
U.S. Energy Information Administration, . Capital Cost and Per-
formance Characteristics for Utility-Scale Electric Power Generat-
ing Technologies. Report. U.S. Energy Information Administration.
URL:https://www.eia.gov/analysis/studies/powerplants/capitalcost/
pdf/capital_cost_AEO2025.pdf. prepared for the Annual Energy Outlook
2025; includes contractor analysis prepared by Sargent & Lundy.
Valdmanis, R., . SMR Firms Race to Build Nuclear Fuel Supply
Chain.Reuters. URL:https://www.reuters.com/business/energy/
smr-firms-race-build-nuclear-fuel-supply-chain-2025-03-31/. march
2025.
Vanatta, M., Stewart, W.R., Craig, M.T., 2024. The role of policy
and module manufacturing learning in industrial decarbonization by
small modular reactors. Nature Energy URL:https://doi.org/10.1038/
s41560-024-01665-w, doi:10.1038/s41560-024-01665-w.
Vithayasrichareon,P.,Macgill,I.,2014.Impactsofgeneration-cyclingcosts
on future electricity generation portfolio investment. IEEE Power and
EnergySocietyGeneralMeeting2014. doi:10.1109/PESGM.2014.6938915.
Vujić, J., Bergmann, R.M., Škoda, R., Miletić, M., 2012. Small modular
reactors: Simpler, safer, cheaper? Energy 45, 288–295. URL:https:
//www.sciencedirect.com/science/article/pii/S036054421200093X,
doi:https://doi.org/10.1016/j.energy.2012.01.078. the 24th
International Conference on Efficiency, Cost, Optimization, Simulation
and Environmental Impact of Energy, ECOS 2011.
P. Rao et al.:Preprint submitted to ElsevierPage 16 of 17

Consequences of high SMR operating costs
Walton, R., . New England Capacity Prices Rise Almost 40% in Most
RecentAuction.Utility Dive. URL:https://www.utilitydive.com/news/
new-england-iso-ne-capacity-prices-rise/708322/. february 2024.
Weibezahn, J., Steigerwald, B., 2024. Fission for funds: The financing
of nuclear power plants. Energy Policy 195, 114382. URL:https:
//www.sciencedirect.com/science/article/pii/S0301421524004026,
doi:https://doi.org/10.1016/j.enpol.2024.114382.
White, P., Cothron, E., . Characterizing an Emerging Market for High-
Assay, Low-Enriched Uranium Production. Report. Nuclear Innovation
Alliance. URL:https://nuclearinnovationalliance.org/sites/default/
files/2023-12/NIA%20HALEU%20Cost%20Report%20%2812_15_23%29_1.pdf.
Wigeland, R., Taiwo, T., Ludewig, H., Todosow, M., Halsey, W., Gehin,
J., Jubin, R., Buelt, J., Stockinger, S., Jenni, K., Oakley, B., 2014.
NuclearFuelCycleEvaluationandScreening—FinalReport:Appendix
C, Evaluation Criteria and Metrics. Technical Report INL/EXT-14-
31465, FCRD-FCO-2014-000106. Idaho National Laboratory. URL:
https://sai.inl.gov/content/uploads/29/2024/11/es_appendix_c.pdf.
X-Energy Reactor Company, LLC, Ares Acquisition Corporation, 2022.
Clean, Safe, Secure, Affordable. URL:https://www.sec.gov/Archives/
edgar/data/1829432/000119312522298938/d411466dex992.htm.exhibit99.2
to Form 8-K filed by Ares Acquisition Corporation.
P. Rao et al.:Preprint submitted to ElsevierPage 17 of 17
