---
title: Carbon Regulation and Competition in the European Airline Industry
url: https://arxiv.org/abs/2603.27724
category: consumer-behavior
subcategory: empirical
date: 2026-03
venue: ''
authors:
- Ertian Chen
- Lichao Chen
- Lars Nesheim
source: arxiv
pdf_url: https://arxiv.org/pdf/2603.27724
pages: 48
chars: 89396
fetched_at: '2026-11-08T13:01:11+00:00'
kb_version: 1
---

# Carbon Regulation and Competition in the European Airline Industry

Carbon Regulation and Competition in the
European Airline Industry∗
Ertian Chen† Lichao Chen‡ Lars Nesheim§
October 18, 2026
Abstract
The European Union Emissions Trading System is set to substantially increase the
effective carbon price faced by airlines. We estimate a two-stage model of airline
competition with endogenous product entry, direct departure frequencies, and pricing.
Impacts are highly asymmetric across carrier types and market segments. Consumer
surplus declines by up to 34% overall and up to 95% in medium- and long-haul markets.
Short-haul markets gain welfare as airlines reallocate capacity toward shorter routes.
Airline profits decline by 1–42%, but carbon tax revenue of$1.9–2.9 billion and the
social value of avoided emissions of$2.7–4.0 billion more than offset private-surplus
losses.
Keywords:Carbon Regulation, Airline Competition, Welfare Analysis
JEL Codes:L93, L13, Q52
∗We are grateful to Andreas Sch¨ afer, Lynette Dray, and Khan Doyme from the UCL Air Transportation
Systems Lab for sharing data and insights on the European airline industry. We especially thank Chris-
tian Bontemps and participants at the 2026 Symposium on Aviation Research for valuable comments and
discussion. We gratefully acknowledge the use of the UCL Myriad High Performance Computing Facility
(Myriad@UCL) and associated support services, and the Isambard 3 Tier-2 HPC Facility hosted by the
University of Bristol and operated by the GW4 Alliance, funded by EPSRC [EP/X039137/1]. All errors are
our own.
†School of Economics & Paula and Gregory Chow Institute for Studies in Economics, Xiamen University.
Email: ertianchen@xmu.edu.cn.
‡Cambridge Econometrics. Email: lichaochen331@gmail.com.
§University College London, Bristol, CeMMAP and IFS. Email: l.nesheim@ucl.ac.uk.
1
arXiv:2603.27724v2  [econ.GN]  22 Oct 2026

1 Introduction
The aviation industry’s growing share of EU greenhouse gas emissions presents a significant
environmental challenge. New-generation aircraft and sustainable aviation fuels (SAFs) are
not yet viable at scale, and efficiency gains have historically been outpaced by demand
growth. Meeting this challenge motivates market-based policies such as the EU Emissions
Trading System (EU ETS). This article investigates how carbon regulation reshapes Eu-
ropean airline competition and endogenous route networks. We ask three questions. How
do the distinct business models of full-service carriers (FSCs) and low-cost carriers (LCCs)
shape their responses to rising carbon costs? How does regulation alter market structure
through route entry and exit? And what are the consequences for consumer welfare and its
geographic distribution?
The European market differs from its North American and Asia-Pacific counterparts.
High population densities and short intercity distances favor direct flights over hub-and-spoke
connections and contribute to airport congestion. Europe hosts nearly half of the world’s
slot-coordinated airports (EUROCONTROL and F AA Air Traffic Organization, 2024) and
features high aircraft utilization. Spanning more than 27 countries and deregulated later
than the US market, 1 it remains fragmented despite privatization and consolidation over
the past 35 years. In 2019, the year of our sample, the market included 14 competing
airline groups. Finally, important asymmetries are introduced by the large role of legacy
national carriers. Although state aid to national carriers is prohibited except under specified
conditions, European FSCs are legacy national or flag carriers, with grandfathered slots,
dense hub networks, and legacy costs.
This market structure gives rise to intense competition and a distinction between two
dominant business models. FSCs typically operate from congested primary airports, using
hub advantages and intercontinental networks to serve both point-to-point and international
1The European Council adopted liberalization packages in 1987, 1990, and 1992, creating a substantially
liberalized internal market (Butcher, 2010).
2

connecting traffic. LCCs use decentralized point-to-point networks, often from secondary
airports, with lower costs and unbundled services. Their wider city portfolios provide more
feasible routes for entry. These differences in costs and network organization shape op-
portunities for profitable route adjustment and so shape the potential impacts of carbon
regulation.
Within this competitive asymmetric environment, Europe is implementing stringent avi-
ation carbon policies. Ordinary free allocation of EU ETS allowances to aircraft operators
was phased out in 2026, following reductions in 2024 and 2025, although targeted support for
eligible SAFs remains (European Commission, 2024). The phase-out coincides with higher
jet fuel costs following the 2026 Iran War. Disruptions to Gulf exports and refining capacity
have raised crude prices and jet fuel premiums, with industry and energy market assessments
suggesting supply pressures could persist into 2027 and beyond. Longer-run pressures include
the ReFuelEU mandate to increase SAF usage between 2025 and 2050. SAFs currently cost
several times more than conventional fuel and face production shortfalls (European Union
Aviation Safety Agency, 2024). How these cost shocks interact with airline competition is a
first-order question for the industry’s future.
We estimate a two-stage game in which airlines first choose direct routes, departure
frequencies, and connecting products, then compete on prices. To estimate the game, we
use data containing information on European airline networks, prices, and market shares for
direct and one-stop services. Our counterfactuals then simulate increasingly stringent carbon
taxation through the EU ETS, using an iterative algorithm in which airlines sequentially re-
optimize networks in response to higher distance-related costs.
Our estimates reveal substantial cost differences, with LCCs having lower marginal and
total costs per passenger. 2 Responses to carbon pricing are highly asymmetric. FSC direct
departure frequency declines by 23–62% and regional frequency by 27–35%, whereas LCCs
primarily reallocate departures toward shorter routes. Medium- and long-haul markets (over
2We also report results for a smaller regional carrier category comprising Icelandair and Air Europa.
3

1,500 km) are far more severely affected; short-haul markets gain net welfare as capacity is
redirected toward them. Consumers and airlines share the burden. Consumer surplus falls
substantially, and profit losses grow with the carbon price. Carbon revenue and the social
value of avoided CO2 emissions more than offset these losses, yielding welfare gains of$2.2–
3.3 billion.
We contribute to two literatures. First, we build on the literature on structural models
of airline competition and entry. Most of this literature focuses on the US, where hub-and-
spoke networks and connecting traffic are central (Berry, 1990, 1992; Berry and Jia, 2010;
Ciliberto and Tamer, 2009; Aguirregabiria and Ho, 2012; Ciliberto et al., 2021; Bontemps
et al., 2025a; Yuan and Barwick, 2026). European studies have examined slot allocation
(Marra, 2024; Bauer, 2025) and LCC subsidies (Bontemps et al., 2025b). We build directly
on Yuan and Barwick (2026)’s framework to study how distance-related carbon regulation
changes route profitability, reallocates departure capacity, and redistributes welfare. Airport
capacity constraints, carriers’ feasible redeployment opportunities, and the predominance
of direct services distinguish the European setting. Our analysis quantifies how carbon
regulation reshapes this imperfectly competitive market through endogenous route entry
and exit.
Second, we advance the literature on carbon regulation. Studies of its environmental
efficacy include Metcalf (2019); Bayer and Aklin (2020); Colmer et al. (2025); Timilsina
(2022). We instead examine how carbon pricing reconfigures a large oligopolistic industry.
Our approach is closest to Ryan (2012) and Fowlie et al. (2016) on US cement, and Fowlie
(2009) on emissions leakage under imperfect competition. We adapt their insight that envi-
ronmental policy changes market structure and welfare to aviation. Two features distinguish
our setting. Route-specific exposure generates heterogeneous cost shocks, and firms’ produc-
tion locations (i.e. route networks) are endogenous, creating a restructuring channel largely
absent in manufacturing.
Outline.Section 2 reviews the industry and data. Section 3 presents the model. Sections
4

4 and 5 discuss identification, estimation, and results. Section 6 presents the counterfactuals
and Section 7 concludes.
2 Background and Data
This section provides background on the European airline industry and describes our data
sources and processing steps.
2.1 Background: EU Emissions Trading System
The EU Emissions Trading System (EU ETS), introduced in 2005, establishes a price for
the right to emit CO 2 through a cap-and-trade program. 3 It regulates installations across
thirty-one countries, covering approximately 40% of EU greenhouse gas emissions. Entities
surrender one European Union Allowance (EUA) per tonne emitted, trade allowances at a
uniform European price, and, within limits, bank or borrow across years and phases. The
declining cap creates scarcity and an incentive for abatement (Ellerman et al., 2016).
The EU ETS has evolved through several distinct phases. During Phase I (2005–2007),
prices exceedede30 per tonne before collapsing as the cap proved non-binding. Phase II
(2008–2012) coincided with the Great Recession, with prices betweene8 ande30. Phase III
(2013–2020) centralized allocation and shifted toward auctioning while Phase IV (2021–2030)
tightened the cap’s annual reduction. Manufacturing industry evidence indicates that the
policy reduced emissions 14–16%, primarily through cleaner technologies, without detectable
contractions in economic activity or leakage to unregulated entities (Colmer et al., 2025).
Extension to Aviation.Aviation entered the EU ETS in 2012. 4 Through the end of
2026, the EU ETS and corresponding Swiss and UK systems collectively covered all flights
within the EEA and flights connecting the EEA to Switzerland and the UK, subject to
specified exemptions. Under the framework, operators must monitor emissions, estimated
3Earlier market-based environmental policies include US leaded gasoline permits (1982), Icelandic and
New Zealand fishing quotas (1984 and 1986), and US sulfur dioxide permits (1995).
4EU directive 2008/101/EC included aviation.
5

based on fuel consumption and standard emission factors, and surrender corresponding al-
lowances. Initially, operators were offered free allowances but these were phased out and
then completely removed in 2026 (European Commission, 2024).
The EU ETS impact on aviation has several distinctive features. First, the impact is
operator and route specific because the carbon charge is proportional to fuel consumption,
which depends on aircraft type, passenger load, and distance. Second, the carbon charge
affects both fixed per flight operating costs and per passenger marginal costs, with a larger
effect on fixed costs since each additional passenger adds little to total weight. Third, carbon
prices affect airline entry and exit decisions, and so, unlike manufacturing settings, have first-
order effects on network structure and route-level competition.
Interaction with Sustainable Aviation Fuel Mandates.Mandatory SAF adoption
adds fuel cost pressures. SAF currently costs two to seven times as much as conventional jet
fuel. EASA reports conventional fuel ate734 per tonne and biofuel ate2,085, projecting
a two- to threefold SAF premium through at least 2030 (European Union Aviation Safety
Agency, 2024). Carbon pricing narrows this gap, but the combined mandates raise operating
costs and reinforce the importance of understanding network adjustment.
Heterogeneous Impacts across Carrier Types.Carbon regulation does not affect all
carriers symmetrically. Because carbon costs scale with distance, all carriers with similar
aircraft and loads face similar route-level cost increases. However, network architecture
shapes carriers’ capacity to respond to these cost increases. LCC point-to-point networks
offer flexibility to reallocate departures as relative profitability changes. In contrast, FSC
hub-and-spoke networks are anchored at slot-controlled home-country airports. Our model
is designed to capture these differences so that we can analyze how higher carbon prices
affect entry, exit, network configuration, and pricing.
6

2.2 Background: European Airline Industry
The Rise of European Low-Cost Carriers.Following the deregulation of European
aviation in 1992, the European airline industry experienced successive waves of entry, ex-
pansion, exit and consolidation. Low-cost carriers (LCCs) expanded through both organic
growth and acquisitions. LCCs’ share of flights surged from 1.6% in 1998 to 32.5% by
2022 (EUROCONTROL, 2022) and their passenger share reached 56% by 2016. 5 Numerous
smaller firms entered but then were absorbed or failed. Some smaller regional carriers op-
erated independently or became subsidiaries of larger carriers. Full-service carriers (FSCs)
responded through cost restructuring, changes to service offerings, and the establishment or
acquisition of low-cost subsidiaries. FSC mergers included the formation of Air France–KLM
in 2004 and the combination of British Airways and Iberia under IAG in 2011.
The primary strategic difference between FSCs and LCCs lies in their network architec-
ture. FSCs, such as British Airways at London-Heathrow, Iberia at Madrid-Barajas, or Air
France at Paris-Charles de Gaulle, typically use ahub-and-spokemodel to centralize opera-
tions, exploiting incumbent hub advantages, grandfathered slot holdings, and economies of
scale while funneling passengers from short-haul intra-European flights into lucrative long-
haul services to the rest of the world. In contrast, LCCs use a decentralizedpoint-to-point
(P2P) network focused on high-frequency, short-haul flights between secondary airports.
This provides greater routing flexibility by offering direct flights between a wider variety of
city pairs.
The distinction is visually apparent in Figure 1, which contrasts the hub-centric network
of Air France-KLM with the diffuse, web-like structure of Ryanair. While Ryanair maintains
large operational bases at airports like London Stansted, these do not function as connecting
hubs for transfer passengers. Their strategic role is to serve large origin-destination markets,
not to facilitate transfers.
In addition, FSC and LCC cost structures differ markedly. FSCs incur higher per-
5Authors’ calculations. Time-series data on passenger shares is not available.
7

Figure 1: Route Maps of Air France-KLM (left) and Ryanair (right) in Q2 2019
passenger and per-flight costs, driven by higher legacy labor and fleet costs, lower fleet
utilization, and premium offerings like business class and meal services. The cost per avail-
able seat kilometer for LCCs (excluding fuel) is typically 20%–30% lower than for FSCs
(Doganis, 2010), granting them a substantial pricing advantage.
Finally, service levels and airport use differ. LCCs unbundle baggage and seat selection,
whereas FSCs traditionally offer more inclusive fares. 6 FSCs favor major hubs and LCCs
smaller secondary airports. In London, Heathrow principally serves FSCs, Gatwick accom-
modates both types, and Stansted and Luton are major LCC bases. City and Southend
serve specialized segments.7 Heathrow’s congestion and airport charges make it unattractive
to LCCs despite its connectivity. Section 3 explains how these network, cost, and service
differences enter the model.
Slot Constraints in European Airports.At congested airports, carriers must acquire
slots to gain the right to take off or land at specified times. So, entry or expansion requires
acquisition of available slots. By European Council Regulation (EEC) No 95/93, most slots
are allocated based on historic precedence. Under the regulation, sufficient use in a given
6Annual reports put LCC ancillary revenue shares at 26–45%, compared with 11–24% for FSCs.
7London City mainly serves short-haul business routes; Southend is dominated by charter airlines.
8

season entitles a carrier to retain its existing slots in the next season. This gives incumbent
slot holders, including FSCs with hub operations, an advantage over entrants. 8 Table 1
documents FSCs’ greater presence on routes with slot-controlled endpoints.
Table 1: Passenger share on routes including at least one slot-controlled airport
2016 2017 2018 2019
Low-cost15.42% 14.30% 14.54% 15.08%
Full-service32.91% 33.15% 32.48% 31.96%
To capture the impacts of slot constraints in our estimation and our counterfactuals,
we impose capacity constraints at nine airports, requiring capacity to be released before
expansion when constraints are binding. Airport and airline-hub controls in demand and
marginal costs, and a slot-airport term in fixed costs, also affect route profitability.
Airlines and Hubs.Table 2 lists the 14 airline groups, included carriers, and hub or main
airports in 2019. We label parents by their largest carrier’s name or IATA code. British
Airways (BA), for example, represents IAG, including Iberia, Aer Lingus, and Vueling. Its
hubs include Heathrow, Madrid-Barajas, and Dublin. Carriers within a parent coordinate
through code-sharing and complementary routes. The model distinguishes hubs affecting
demand and costs from airport-capacity constraints affecting entry.
Airline fleet capacity.During 2016–2019, European carriers operated near full capacity
with little scope to increase network frequency without expanding fleets (EUROCONTROL
and F AA Air Traffic Organization, 2024). Moreover, fleet expansion was limited. Since
aircraft orders typically require three to five years, in our model we treat fleet capacity as
fixed and thus require all network and frequency choices to satisfy fleet capacity constraints.
2.3 Data
Our data come from Sabre Market Intelligence (Sabre, 2025), a reservation and pricing
system used by major European airlines for fare optimization. The data cover 2016–2022.
8Historic rights normally require at least 80% use, subject to exceptions. Our static model neither
captures this dynamic incentive nor explicitly allocates airline slot portfolios.
9

Table 2: Airline groups
Code Parent group Included carriers (IA T A codes) Hub/main airports (IA T A
codes)
Full-service groups
BA International Airlines
Group (IAG)
British Airways (BA), BA CityFlyer
(CJ), Iberia (IB), Iberia Express
(I2), Aer Lingus (EI), Vueling (VY)
London Heathrow (LHR), Madrid
Barajas (MAD), Dublin (DUB),
Barcelona El Prat (BCN), Rome
Fiumicino (FCO)
AF Air France–KLM Air France (AF), HOP! (A5), KLM
(KL), KLM Cityhopper (W A),
Transavia (HV/TO), Air Corsica
(XK)
Paris Charles de Gaulle (CDG),
Amsterdam Schiphol (AMS)
LH Lufthansa Group Lufthansa (LH), Lufthansa CityLine
(CL), Austrian Airlines (OS), Swiss
(LX), Brussels Airlines (SN),
Eurowings (EW), Air Dolomiti
(EN), SunExpress (XQ), SunExpress
Deutschland (XG)
Frankfurt (FRA), Munich (MUC),
Zurich (ZRH), Vienna (VIE),
Brussels (BRU)
SK SAS Scandinavian Airlines (SK) Copenhagen (CPH), Stockholm
Arlanda (ARN), Oslo Gardermoen
(OSL)
AY Finnair Finnair (AY) Helsinki (HEL)
A3 Aegean Airlines Aegean Airlines (A3), Olympic Air
(OA)
Athens (ATH)
LO LOT Polish Airlines LOT Polish Airlines (LO) Warsaw Chopin (W A W)
Low-cost groups
DY Norwegian Norwegian (DY) Oslo (OSL)
FR Ryanair Holdings Ryanair (FR) London Stansted (STN), Dublin
(DUB)
LS Jet2 Jet2.com (LS) Leeds Bradford (LBA)
U2 easyJet easyJet (U2), easyJet Europe (EC) London Gatwick (LGW)
W6 Wizz Air Wizz Air (W6) Budapest (BUD)
Regional groups (study classification)
FI Icelandair Icelandair (FI) Keflavik (KEF)
UX Air Europa Air Europa (UX) Madrid Barajas (MAD)
Note:The 14 group codes identify the decision-making units in the model. The table lists the 35 carrier
codes in the retained 2019 sample using our carrier-to-group mapping. Air Corsica is grouped with AF and
SunExpress with LH. HV and TO identify Transavia’s Dutch and French operations. Hub/main airports
include operating bases and differ from the model’s designated connecting airports.
We focus on 2019, the latest pre-COVID year.
Quarterly airline-itinerary observations record endpoint and connecting airports, non-
stop status, average fares, frequency, travel time, and passengers. We retain direct and one-
stop services in the top-100-airport sample, spanning 83 cities. Following Yuan and Barwick
(2026) and Bontemps et al. (2025a), we aggregate opposite directions, which typically have
10

similar prices and frequencies. A product is defined to be an itinerary offered by a parent
group. A market is the set of all products joining a pair of endpoint cities. Distance is
total itinerary distance, including both connecting legs. Direct-flight itineraries carry 99.0%
of retained passengers, but one-stop flights matter for substitution and the profitability
of component legs. Eurostat metropolitan populations determine market size (Eurostat
(European Commission), 2026).
Table 3 presents summary statistics. Our estimation sample contains the 14 parent airline
groups: seven full-service, five low-cost, and two regional groups (Table 2). The six largest
groups are the three primary FSCs (British Airways, Air France, and Lufthansa) and the
three primary LCCs (Ryanair, easyJet, and Wizz Air). These six groups account for 87.2%
of passenger traffic in the sample. We observe 13,509 product-quarters across 2,141 city pairs
and 7,647 city-pair-quarters. Of these, 11,487 product-quarters are direct flights and 2,022
are one-stop flights. The average fare is$91.44, the average direct-flight frequency is 2.88
directional departures per day, and the average itinerary distance is about 1,482 kilometers.
In total, the airlines in our 2019 sample served 348.26 million passengers.
Table 3: Summary statistics
(a) Market dimensions (c) Demand and cost Mean St.Dev
Product-quarters 13,509 Fare (100 USD) 0.91 0.58
City pairs 2,141 Frequency (daily) 2.88 4.03
Passengers (million) 348.26 Distance (1,000 km) 1.48 0.73
Market size (1 million) 2.36 1.66
(b) Market shares
FSCs LCCs Other
British
Airways Air France Lufthansa Ryanair EasyJet Wizz Air
Share 0.15 0.09 0.13 0.25 0.21 0.05 0.13
Table 4 reports city-level connectivity and frequency statistics for the six largest airline
groups, the three largest FSCs and the three largest LCCs. Panels (a) and (b) reveal that
FSCs generally maintain greater connectivity and higher frequencies at their hubs. For
11

instance, Lufthansa Group operates an average of 7.8 daily departures per direct route
serving Frankfurt, compared with 3.1 for Ryanair routes serving Dublin. This contrast is
also evident in Panels (c) and (d), which measure network concentration. Approximately
46% of Air France-KLM’s direct-flight frequency is to or from Amsterdam, with a similar
share to or from Paris, a clear empirical signature of a hub-and-spoke model. LCCs generally
exhibit lower concentration levels, with their routes more evenly distributed across a wide
range of cities, reflecting their decentralized point-to-point strategy.
Table 4: Connectivity and frequency: six largest airline groups, two most connected cities
Group First City Cities Served Freq. Second City Cities Served Freq.
(a) F ull service:
BA London 67 7.4 Barcelona 60 4.8
AF Amsterdam 71 7.0 Paris 63 6.5
LH Frankfurt 61 7.8 Munich 60 7.4
(b) Low Cost:
FR Dublin 59 3.1 London 56 4.7
U2 London 61 7.2 Berlin 56 3.9
W6 Budapest 40 1.5 Bucharest 27 1.5
Group First City Concentration Second City Concentration
(c) F ull service:
BA London 46.2% Barcelona 21.0%
AF Amsterdam 46.3% Paris 46.5%
LH Frankfurt 28.5% Munich 25.8%
(d) Low Cost:
FR Dublin 12.6% London 18.9%
U2 London 32.1% Berlin 15.5%
W6 Budapest 22.0% Bucharest 17.3%
Note:The table presents statistics for the six largest airline groups and their two most connected cities.
Cities are ranked by the number of directly connected cities. Cities Served counts directly connected cities.
Freq. is the average number of daily departures per direct route serving the listed city. Concentration
measures the proportion of direct flight frequencies to/from the hub city relative to all the airline’s direct
flight frequencies.
Table 5(a) shows that around 47.5% of market-quarters in 2019 are served by more
than one airline group. Average fares are slightly lower in two- and three-firm markets
than in monopoly markets, although the relationship is not monotone. Fares are averaged
within market-quarters, and the standard deviation of these averages is highest in monopoly
markets. Table 5(b) shows that, in 2019, FSCs have about 1.6 times as many slot-airport
12

route-quarter observations per parent airline as LCCs. Table 5(c) reports average quarterly
changes in route observations per parent airline over 2016–2019. Both FSCs and LCCs
expand in Q2, with increases of 26.3 and 44.0 route observations, respectively.
Table 5: Competition and Network Statistics
(a) Price and competition
Number of Firms 1 2 3 4 5 6
Market-quarters4,015 2,567 809 224 30 2
Percentage52.50% 33.57% 10.58% 2.93% 0.39% 0.03%
Average F are ($100)0.901 0.897 0.882 0.995 1.034 0.787
Std. Dev.0.626 0.416 0.298 0.283 0.320 0.009
(b) Slot-Airport Exposure
2016 2017 2018 2019
Low-cost201 214 233 239
F ull-service383 384 392 389
Note:Annual number of route-quarter obser-
vations with at least one slot-controlled airport
per parent airline.
(c) Quarterly dynamics
Q1 Q2 Q3 Q4
All Routes Low-cost−13.9 44.0 10.8−27.9 Full-service−9.9 26.3 8.3−21.7
Slot-Airport Routes Low-cost−1.3 5.4 2.0−4.0 Full-service−5.0 12.0 3.4−9.4
Note:Average quarterly change in route observations per parent airline
over 2016–2019.
Figure 2 shows passenger, revenue, and frequency shares for all 14 parent airline groups.
Their codes are defined in Table 2. While Ryanair (FR) and easyJet (U2) have the largest
passenger shares, IAG (BA) and Lufthansa Group (LH) have the highest revenue shares.
Lufthansa also has the highest frequency share, followed by Ryanair and IAG, reflecting
differences in fares and schedule intensity.
Figure 3 reports statistics on network size, density, and efficiency. Network size is defined
to be the number of airports served. In our model, this determines the scope of feasible entry
alternatives. BA, AF, LH, FR, U2, and W6 have the largest networks. Network density is
13

Figure 2: Passenger, revenue, and frequency shares for all 14 parent airline groups, Q2 2019.
Group codes are defined in Table 2
the number of active direct airport pairs divided by possible pairs. FSCs have lower density,
consistent with hub-and-spoke networks. Network efficiency is a measure of the average
number of active direct routes per airport. Ryanair serves over ten on average compared
with fewer than three for Air France.
3 Model
This section introduces a static two-stage model of airlines’ entry, direct departure frequency,
and pricing decisions. In the first stage, airlines simultaneously choose direct routes and their
departure frequencies, together with the connecting flights to offer. In the second stage,
airlines compete on prices to attract customers. Our model closely follows the framework
of Yuan and Barwick (2026), including the linkage between direct and connecting services
and the use of revealed-preference inequalities to estimate costs. We modify their framework
for the European context by retaining multiple airports per city and multiple options for
connecting airports and by incorporating capacity-constrained redeployment when analyzing
airlines’ responses to distance-related carbon charges.
Letg∈ Gbe an airline group and let a marketm∈ Mbe defined by a non-directional
14

(a) Network size (airports)
 (b) Network density (%)
(c) Actual (green) and possible (pur-
ple) routes
(d) Network efficiency (routes per air-
port)
Figure 3: Network size is the total number of airports served. Network density is the number
of airport pairs served by direct flights divided by the total number of possible pairs. Panel
(c) displays actual pairs linked by direct flights and potential pairs. Network efficiency is
the number of direct routes per airport. Group codes are defined in Table 2
city-pairc, d∈ CwhereCis the set of cities. 9 An itinerary, also referred to as a route, is
defined by its endpoint airports, an indicator for non-stop or one-stop service, and, for one-
9The definition of a market as a city-pair follows Berry (1992); Aguirregabiria and Ho (2012); Yuan and
Barwick (2026).
15

stop service, its connecting airport. We aggregate opposite travel directions, so endpoint
airport pairs are non-directional. A direct or non-stop router∈ Ris an airport pair
a, b∈ A, whereAis the set of airports. A connecting or one-stop route additionally specifies
the connecting airporth. A productjis a route or itinerary offered by a particular airline
group. We use “direct” and “non-stop” interchangeably, and “connecting” (or “indirect”) to
denote a one-stop itinerary comprising two direct legs. An airline group’s direct operating
network consists of its active direct routes and their departure frequencies. Indirect flights
use this network and require both component legs to be active, but offering an indirect
service is a separate decision. In general prose, a flight may refer to a direct or connecting
service. When counting aircraft operations, we use “departures” to distinguish them from
itineraries or products. Furthermore, letj= 0 denote the outside option of not flying. Let
Jgm be the set of products chosen by airlinegin marketmin stage one of the two-stage
game, and let the vectorN g represent airlineg’s product-offering vector, withN gj = 1 if
productjis offered. In the pricing stage, the set of products available in marketmis the
outside optionj= 0 plusJ m = S g Jgm. That is, it is the outside option plus the set of
products chosen by airlines in stage one. Denote the number of products in marketmby
Jm =|J m|. Note that an airline may offer multiple products in a market by using different
airports in the same city or by offering connecting itineraries that use different connecting
airports.
Airlines’ first-stage choices and consideration sets.Each airline’s first-stage choices
include choice of product portfolioN g and direct departure frequenciesF g. For the product
portfolio choice, we impose the following constraints on firms’ consideration sets. We assume
that, in the short run, an airline can only enter routes between cities it already serves, as in
Berry (1992). Costs to expand to unserved cities are assumed to be too high to be profitable
in the short run. The city set is fixed at its observed quarterly support throughout the
simulation. At the nine airports treated as capacity constrained, aggregate direct departure
16

frequency cannot exceed observed capacity.10 Thus entry into an airport with fully occupied
capacity requires departure capacity to be released elsewhere at that airport. Finally, to
capture legacy entry costs of flag carriers, we require that, when considering redeploying
departures from an observed direct route to an alternative route, the number of alternative
route endpoints located in the airline’s home country is weakly greater than the number
on the observed route. These consideration set constraints capture the assumption that
expanding services in directions outside the support of the observed route network entails
greater costs. We assume these greater costs are sufficiently large that such entry is not
feasible in our estimation nor in our counterfactual simulation. We useJ f eas g to denote
the resulting consideration set of feasible products for airlineg, including direct flights and
one-stop flights supported by feasible direct legs. Regarding the choice of direct departure
frequencyF g, total direct frequency across an airline’s network is bounded above by its
observed quarterly total, with released departure capacity available for redeployment.
The model represents the three distinctions between FSCs and LCCs discussed in Sec-
tion 2.2 through several channels. First, differences in network architecture enter through
airlines’ observed city portfolios, designated connecting airports, and the dependence of con-
necting services on their component direct legs. These features shape feasible redeployment
opportunities and the network-wide profit consequences of changing a route. Flag carri-
ers additionally face the home-country restriction described above. Second, differences in
costs are captured by airline-quarter effects and product characteristics in marginal costs,
while fixed operating costs vary with direct departure frequency, distance, market size, and
capacity-constrained airport exposure. The fixed-cost coefficients are common across carri-
ers, so differences in their implied fixed costs arise from their networks and operating choices
rather than separate FSC and LCC cost parameters. Third, differences in service offerings
and airport use enter through airline-quarter, major-airport, and airline-hub effects and other
product controls in demand and marginal costs, together with airport-capacity constraints on
10These airports are Amsterdam, Athens, Paris Charles de Gaulle, Copenhagen, Frankfurt, Helsinki,
London Heathrow, Madrid, and Munich.
17

entry. These controls capture systematic differences across carriers and products, although
we do not separately model baggage charges, individual service amenities, or a secondary
airport cost advantage.
3.1 Second Stage: Demand and Pricing
In the second stage, given product portfolios and direct departure frequencies, airlines com-
pete in prices. They simultaneously set prices for all products in each market to maximize
profits under complete information.
Demand.The demand model is a discrete choice model following Berry and Jia (2010)
and Yuan and Barwick (2026). For a productjin marketm, the utility of consumeriis
given by:
Uijm =



−αpjm +x jmβ+ξ jm +ν im(λ) +λε ijm ifj∈ Jm
εi0m ifj= 0
wherex jm is a vector of product characteristics,p jm is the product price,ξ jm is the unob-
served (to researchers) product characteristic,ν im(λ) is the “nested logit” shock,ε ijm is the
i.i.d. extreme value type I utility shock,αis the price coefficient,βis the vector of utility
parameters, andλ∈(0,1) is the nesting parameter. Letθ d = (α, β, λ) denote the vector of
demand parameters.
The product characteristicsx jm include a constant, the logarithm of product frequency,
total itinerary distance and its square, a non-stop indicator, a high-speed rail competition
indicator, airline-quarter fixed effects, major airport fixed effects, airline-hub fixed effects,
and fixed effects for the top 50 cities ranked by population. Total itinerary distance equals
direct distance for non-stop flights and the sum of the two leg distances for one-stop flights. It
can therefore vary across itineraries in the same market. We also include indicators for routes
with two small-market endpoints or two large-market endpoints, and their interactions with
Aegean, LOT, Air France-KLM, and Finnair. Mixed endpoint categories are the reference
group. Frequency and distance coefficients are common across airlines. Higher frequency
18

offers consumers more travel options and greater flexibility. The airline-hub fixed effect
is important because major European hubs serve both intra-European passengers and a
substantial volume of extra-European transfer passengers. Higher levels of demand due to
these additional extra-European passengers are captured by these airline-hub fixed effects. 11
The model implies that the market share for productjin marketmis:
sjm(pm,x m,ξ m;θ d) = (P k∈Jm exp((−αpkm +x kmβ+ξ km)/λ))λ
1 + (P k∈Jm exp((−αpkm +x kmβ+ξ km)/λ))λ | {z }
Probability of flying
× exp((−αpjm +x jmβ+ξ jm)/λ)P
k∈Jm exp((−αpkm +x kmβ+ξ km)/λ)| {z }
Conditional probability of choosingj
wherep m = (p km :k∈ Jm),x m = (x km :k∈ Jm), andξ m = (ξ km :k∈ Jm). Taking the
logarithm, the demand equation can be expressed as the following linear equation:
ln(sjm)−ln(s 0m) =−αp jm +x jmβ+ (1−λ) ln(s ∗ jm) +ξ jm (1)
wheres 0m is the market share of the outside option, ands ∗ jm is the within-nest market
share of productj. The endogenous variables in this equation are the pricesp jm and the
within-nest market sharess ∗ jm.
Supply.Airlines simultaneously set prices in each market to maximize profits:
X
m∈M
X
j∈Jgm
(pjm −MC jm)·s jm(pm,x m,ξ m;θ d)·MS m ∀g
where MC jm is the marginal cost of productjin marketmand MS m is the market size
defined as the geometric mean of the populations of the two endpoint cities. LetO m be the
ownership matrix for marketmwhere element (j, k) equals 1 if the same firm owns both
11International transfer passengers traveling on single itineraries with short layovers are not included in
our dataset. However, the intra-European legs of international passenger journeys with long layovers are
included.
19

productsjandk. The Bertrand–Nash F.O.C.s for profit maximization yield:
MCm =p m + (Om ⊙ ∂sm
∂pm
)−1sm
where MCm is aJ m ×1 vector of marginal costs for all products in marketm, and⊙denotes
the element-wise product.
We assume marginal cost is a function of observable product characteristics:
MCjm =x jmθs +ω jm (2)
whereω jm is an unobserved cost shock andθ s is a marginal cost parameter vector. The
marginal cost regression uses the same exogenous characteristics and fixed effects as de-
mand, including the non-stop indicator and total itinerary distance. When we compute
our counterfactual simulations, we assume increased fuel costs increase marginal cost per
passenger per kilometer as detailed in Section 6 below.
3.2 First Stage: Entry and Frequency
In the first stage, airlines simultaneously choose product portfolios and direct departure
frequencies. Airlines incur fixed operating costs for each active itinerary. These include
operating costs for direct itineraries and incremental offering costs for connecting itineraries.
For airlineg, offering product portfolioN g and direct departure frequencyF g, we assume
that the total fixed operating cost is:
FCg(Ng,F g,κ g;θ f c) =
X
j∈J f eas g
Ngj ·(z j(fj)θf c+κ j(fj))
wherez j(fj) is a vector of observable product characteristics including a constant, frequency
times distance, the logarithm of market size, the number of capacity-constrained airports on
the route, and an indicator for one-stop itineraries. To be specific, the five-dimensional vector
20

zj equals (1, fjdj,log MS m, Sj,0) for a direct flight and (0,0,0,0,1) for an indirect flight,
whered j is direct distance in thousands of kilometers andS j counts capacity-constrained
endpoint airports. The specification captures the fact that adding an indirect service incurs
only an incremental cost since the direct leg costs are already counted. The variableκ j(fj)
is an unobserved fixed cost shock, andθ f cis a vector of fixed cost parameters. For direct
flights the shock is specific to airline, quarter, route, and frequency. For indirect flights it is
specific to airline, quarter, endpoints, and connector, and does not vary with frequency.κ g
is the vector of these shocks for airlineg. Note that fuel costs, which are impacted by carbon
prices, are a fixed cost of operating a direct route and are proportional to frequency times
distance. The frequency-distance coefficient includes these fuel costs and other distance-
related fixed operating costs. When we compute our counterfactual simulations, increases in
EU ETS prices add to this component without imposing the same aircraft charge a second
time on connecting products. This is detailed in Section 6 below.
We assume that firms choose their product portfolios in stage one before the second-stage
shocksξ jm andω jm are realized.12 Let (N,F,X) be the networks, frequencies, and product
characteristics of all airlines in all markets. Then, for each airlineg, expected second-stage
profits can be written as:
Π2g(N,F,X;θ d, θs) =E ξ,ω

 X
m∈M
X
j∈Jgm
(pjm −MC jm)·s jm(pm,x m,ξ m;θ d)·MS m


In this expression,p m is the equilibrium price vector that arises in stage two in marketm
after the demand and cost shocks (ξm,ω m) are realized. The expectation is taken over all un-
observed demand and cost shocks in all markets. We assume airlines know the distributions
of these shocks when making entry and frequency decisions.
Airlines observe all fixed cost shocks and simultaneously choose (N g,F g) to maximize
expected net profit, Π 2g −FC g.
12Prior work, including Aguirregabiria and Ho (2012), Sweeting (2013), Eizenberg (2014), and Yuan and
Barwick (2026), makes an analogous assumption.
21

3.3 Equilibrium
Airlines choose product portfolios and direct departure frequencies in stage 1 and prices
in stage 2. In this two-stage game, we consider pure strategy subgame perfect equilibria
in product portfolios, direct departure frequencies, and prices:{N ∗,F ∗,P ∗}. The existence
and uniqueness of equilibrium in the second-stage pricing game are established by Nocke and
Schutz (2018) for multi-product nested logit models. However, equilibrium in the first-stage
game is not guaranteed to exist, as noted by Bontemps et al. (2025a) and Yuan and Barwick
(2026). We assume the existence of a first-stage equilibrium, but do not assume uniqueness
and allow for multiple equilibria.
4 Identification and Estimation Strategies
There are two endogenous variables in (1), price and within-nest share. We use three excluded
instruments: the average frequency of other products in the market; the number of distinct
airline parent groups in the market; and an indicator that at least one endpoint airport is a
hub for the airline’s alliance.
We assume that, conditional on the included controls, these instruments are orthogonal
to the second-stage demand shocks. The justification for this assumption is as follows.
Network structure and direct-flight frequency are chosen several months before prices. When
airlines make these choices, they forecast profits based on persistent demand and cost shifters
including city, airport, and hub fixed effects. Their forecast errors are driven by high-
frequency, hard-to-predict demand and cost shocks. We assume that these demand and
cost shocks are orthogonal to the variables in their information sets. This restriction allows
network and frequency choices to respond to predictable demand and cost shifters while
excluding correlation with the unobservable innovations that later affect costs and demand.
Based on this identification strategy, demand is estimated by instrumental variable GMM.
Marginal costs are recovered from the pricing first-order conditions, after which we estimate
equation (2) by least squares using the same exogenous controls as in demand.
22

Identification of the fixed cost parametersθ f crequires more discussion. These parameters
are set identified based on moment inequalities arising from the firms’ entry/exit decisions.
Construction of Moment Inequalities.To ease notation, we suppress dependence on
(X, θs, θd) and on the competitors’ strategies. Let Π 1g(Ng,F g,κ g;θ f c) := Π 2g(Ng,F g)−
FCg(Ng,F g,κ g;θ f c) denote airlineg’s stage 1 profit conditional on its own actions, its com-
petitors’ actions, and all other state variables. Assuming observed choices (N∗ g,F ∗ g) maximize
profits, alternative feasible actions (N a g,F a g) must not increase profits. That is:
Π1g(N∗ g,F ∗ g,κ g;θ f c)−Π 1g(Na g,F a g,κ g;θ f c) = ∆Π1g(N∗ g,F ∗ g,N a g,F a g;θ f c)−∆κ a g ≥0
where ∆Π1g(N∗ g,F ∗ g,N a g,F a g;θ f c) is the deterministic component of the difference in profit and
∆κa g is the sum of fixed cost shocks under the observed network minus the corresponding sum
under the alternative network. Under the linear fixed cost specification, the deterministic
component can be written:
∆Π1g(N∗ g,F ∗ g,N a g,F a g;θ f c) = Π2g(N∗ g,F ∗ g)−Π 2g(Na g,F a g)− X
j∈J f eas g
(z∗ j (f ∗ j )N ∗ gj −z a j (f a j )N a gj )θf c
wherez ∗ j (f ∗ j ) andz a j (f a j ) denote the observable product characteristics under the optimal
and alternative stage-one choices.
Following Yuan and Barwick (2026), we use a vector of non-negative instrumentsYbased
on market size quantile bins. Market size is the geometric mean of the two endpoint cities’
populations. Each instrument equals one when market size falls within the corresponding
bin. These instruments capture variation in observable factors affecting profit changes across
markets. We assume that the fixed cost shock difference has zero conditional mean given
market size and the characteristics defining each moment group. This restriction implies that
its expectation remains zero when multiplied by each bin indicator. We pool observations
across quarters and form moments separately by deviation type and, for the redeployment
23

inequalities, by the change in the number of capacity-constrained endpoint airports. Cells
with fewer than ten observations are excluded. For each retained instrumentY k:
E[Yk ·∆Π 1g(N∗ g,F ∗ g,N a g,F a g;θ f c)]−E[Y k ·∆κ a g]| {z }
=0
≥0
Then we construct sample moment inequalities to estimate the fixed cost coefficientsθ f c
following Pakes et al. (2015):
− 1 N a X N∗g,F∗g,Nag ,Fag Yk ·∆Π 1g(N∗ g,F ∗ g,N a g,F a g;θ f c)≤0∀k= 1, ...K
whereN a is the number of feasible alternative product portfolios for airlineg.
Alternative Product Portfolio and Departure Frequency.Exploring all possible al-
ternative product portfolios and direct departure frequencies is computationally infeasible
because the number of (N a g,F a g) combinations grows exponentially with the number of prod-
ucts in airlineg’s portfolio and the number of feasible departure frequencies for each direct
product. Nonetheless, we can construct an outer region covering the identified set by consid-
ering a subset of alternative product portfolios and direct departure frequencies. Following
Yuan and Barwick (2026) and Bontemps et al. (2025a), we consider local network deviations:
direct-service exit and frequency changes, feasible redeployment to alternative routes, entry
into unserved markets, and connecting-flight entry, exit, or connector replacement.
Moment Inequalities with Connecting Flights.Because a deviation on a single direct
route may affect multiple markets due to impacts on connecting flights, we must account for
these effects. LetM a collect all markets affected by deviationa, and letπ ∗ 2gm andπ a 2gm denote
the airline’s expected variable profits across all its products in marketmbefore and after the
deviation. Define ∆z a g as observed minus alternative fixed cost characteristics, summed over
all affected itineraries, and ∆κ a g analogously for fixed cost shocks. The revealed-preference
24

inequality is
X
m∈Ma

π∗ 2gm −π a 2gm  −∆z a g θf c−∆κ a g ≥0.(3)
This expression covers exit, entry, frequency adjustment, and redeployment. Products out-
sideM a cancel, but surviving products in an affected market remain in the profit comparison
because their equilibrium prices and demand can change. Thus neither the direct product’s
own profit alone nor the profit in its endpoint market alone generally measures the gain from
a deviation.
Inference.Following Cox and Shi (2023), we construct the following conditional likelihood
ratio test statistic to conduct inference on the fixed cost parametersθ f c:
CLR(θ f c) =Nmin µ≤0 ( ˆm(θf c)−µ) ′ bΣ(θf c)−1( ˆm(θf c)−µ) (4)
where ˆm(θf c) is the vector of sample moment inequalities, bΣ(θf c) consistently estimates the
covariance matrix of
√
Nˆm(θf c), andµminimizes the quadratic form subject toµ≤0. We
evaluate the quadratic form on the covariance matrix’s non-redundant support. The critical
valueχ 2 ˆr,1−αis the (1−α) quantile of a chi-squared distribution, whereαis the significance
level and ˆris the rank of the active constraints in the covariance-standardized system. The
confidence region isCR 1−α ={θ f c∈R dθf c:CLR(θ f c)≤χ 2 ˆr,1−α}.
5 Estimation Results
This section presents and interprets the estimation results for the demand, marginal cost,
and fixed cost components of our model.
5.1 Demand and Marginal Cost Estimation
As discussed in Section 4, demand parameters are estimated by applying GMM to equation
(1). Marginal costs are recovered from the pricing first-order conditions, and the parameters
in equation (2) are estimated by least squares using the same exogenous characteristics and
25

fixed effects as in demand. Table 6 reports the demand and marginal cost estimation results.
The heteroskedasticity-robust Kleibergen–Paap rk Wald F-statistic (Kleibergen and Paap,
2006) is 12.19. The nesting parameterλis 0.893, indicating modest similarity of products
within a market relative to the outside option.
Table 6: Demand and Marginal Cost Estimation Results
Demand Marginal Cost
Variable Coef. SE Coef. SE
Constant−4.316 (0.534) 0.495 (0.082)
Fare ($100)−3.561 (0.603)
Log Frequency 1.054 (0.035) 0.054 (0.004)
Distance−0.035 (0.068) 0.019 (0.018)
Distance2 0.181 (0.029) 0.038 (0.005)
Nesting Parameter 0.893 (0.037)
Note:Airline-quarter, major airport, airline-hub, and top-50-city
fixed effects, non-stop and high-speed rail indicators, and endpoint-
type controls and their airline interactions are included but not re-
ported. Standard errors in parentheses are heteroskedasticity-robust
for demand and conventional least-squares for marginal cost, condi-
tional on recovered costs. Distance is in 1,000 km; marginal cost is
in$100.
On average, consumers are willing to pay about$29.6 for a one-unit increase in the log of
daily product frequency, reflecting the high value passengers place on schedule convenience.
This is lower than the estimate in Yuan and Barwick (2026) ($106.8). The marginal willing-
ness to pay for distance evaluated at the sample average itinerary distance of 1,482 km is
$14.1 per additional 1,000 km, which is lower than the estimate in Yuan and Barwick (2026)
($144.34) at the average U.S. domestic flight distance of 1,910 km. This difference reflects
many factors including shorter average trip lengths and greater availability of alternative
transport modes (e.g., high-speed rail) in Europe.
The average own-price elasticity derived from our parameter estimates is -3.40, which
is more elastic than the aggregate price elasticity of -3.13 reported in Marra (2024) for the
French market. Compared to estimates from the US market, our estimate is slightly less
elastic than the estimate reported in Bontemps et al. (2025a) (-3.78) and more elastic than
26

the estimate in Berry and Jia (2010) (-2.01). Moderately higher elasticities in Europe are
consistent with higher European availability of close substitutes, both between airlines in
the same market and across alternative modes of transport.
Figure 4 plots a binscatter of the average price elasticities against itinerary distance. We
divide observations into 20 equal-sized bins and plot the average elasticity within each bin.
Elasticities range from approximately -3.1 to -3.5 below 2,000 km and become more negative
for the longest itineraries, reaching approximately -4.3. The relationship is not monotone
over shorter distances. For longer itineraries, the greater price sensitivity indicates that
passengers remain responsive even when surface transport is a less convenient substitute.
Note that the figure does not hold other market characteristics constant and so reflects
variation in elasticities across markets with different prices, shares, and mixes of direct and
connecting products.
Figure 4: Price Elasticity by Distance
Table 7 presents average price, marginal cost, and variable profit by quarter. The average
marginal cost per passenger is$64.3, about 32% lower than the estimate in Yuan and Barwick
(2026) ($95). Part of this difference reflects shorter itineraries and the substantial presence
of low-cost carriers in our sample. Given the average itinerary distance of 1,482 km, the
27

per-mile cost is$0.070. This figure is comparable to Yuan and Barwick (2026)’s estimate of
$0.08 and Berry and Jia (2010)’s$0.06 for U.S. domestic flights. Marginal costs and prices
are higher in the second and third quarters than in the first and fourth, consistent with
seasonal variation in the composition of services and demand.
Table 7: Average Price, Marginal Cost, and Variable Profit by Quarter
Quarter Avg Price Avg MC Avg Variable Profit
Q1 86.56 59.35 0.69
Q2 98.42 71.24 0.75
Q3 92.59 65.43 0.74
Q4 86.88 59.71 0.67
Overall 91.44 64.26 0.71
Note:Price and marginal cost are in USD per passenger. Vari-
able profit is in million USD per product-quarter. Entries are
unweighted product-quarter means.
The average price–marginal-cost spread is$27.2 and the average variable profit per
product-quarter is$0.71 million. Variable profit is revenue less per-passenger marginal costs,
before deducting aircraft operating costs and other fixed network costs. We therefore turn
to fixed cost estimation before assessing the profitability of the observed network.
5.2 Fixed Cost Estimation
To evaluate alternative networks, we must impute frequencies for connecting itineraries ab-
sent from the data. Following Yuan and Barwick (2026), we estimate logfj =a g +γ(logf ah +
logf hb) +uj, wheref j is the connecting-flight frequency,f ah andf hb are its two direct-leg fre-
quencies through connecting airporth,a g is an airline fixed effect, andu j is a regression error.
The least squares regression has anR 2 of 0.596 and a slope coefficientbγ= 0.347. We convert
predictions to frequency levels using the mean exponentiated residual as a correction. For
observed connecting itineraries, we use the estimated elasticity to update frequencies when
either direct leg changes.
We estimate bounds on the fixed cost parameters using the inequalities in (3). To com-
pute expected profits, we randomly drawN= 36 pairs of (ξ, ω) from the empirical joint
28

distribution, with the 2.5th and 97.5th percentiles as the lower and upper bounds of the
respective marginals. Drawing the shocks jointly preserves their empirical dependence. The
same product draws are used when evaluating alternative frequencies and networks to ensure
differences in draws do not drive differences in computed expected profits. As discussed in
Section 4, the instrumentsYare indicator functions whereY k = 1 if a market’s population
falls within thek-th quantile bin. Following Yuan and Barwick (2026), we examine progres-
sively finer population-bin instrument sets and report the last nonempty confidence region
before further refinement yields an empty region. This data-dependent choice balances infor-
mativeness against the feasibility of the estimated restrictions. However, nominal coverage
for a fixed instrument set does not automatically extend to a set selected using the same
data. We therefore describe the reported region as a nominal 95% confidence region for the
selected specification.
Table 8 reports the results for seven bins, retaining all bin indicators and using$5,000
grid increments for each coefficient. The table reports, for each element of the vectorθ f c,
the projection of the estimated 95% confidence region in that dimension.
Table 8: Fixed Cost Estimation
Constant F req.×Dist. Log Market Size Slot Controlled Airport Indirect Flight
Lower Upper Lower Upper Lower Upper Lower Upper Lower Upper
1 9 16 18 30.5 37−41.5−30 4 4.5
Note:For each parameter, the table reports the projection of the estimated 95% confidence region
in that dimension. Instruments are population-bin indicators with seven bins. Quarterly cost is in
$10,000, distance in 1,000 km, population in millions, and frequency in directional departures per
day. The first four coefficients apply to direct products; the slot variable counts endpoint airports.
To compare our results to industry benchmarks, we evaluate parameter vectors in the
confidence region, compute the fixed cost for each direct flight in each market, average across
products and markets, and plot in Figure 5 the resulting distribution of average fixed cost per
flight hour (assuming an average cruising speed of 860 km/h). Our estimated distribution
has a median of$2,945, a 2.5th percentile of$2,823, and a 97.5th percentile of$3,086. These
29

estimates are below the industry reported operating costs per flight hour of$4,829 for A320
family aircraft and$4,337 for B737 NG aircraft (EUROCONTROL, 2024). 13
The frequency–distance coefficient implies distance-related operating costs of$1,778–
2,000 per 1,000 km flown. At an average cruising speed of 860 km/h, this corresponds to
$1,529–1,720 per flight hour. These estimates are below the approximately$2,450–2,960 per
hour implied by fuel and maintenance expenditures in the FY2019 annual reports of easyJet,
Wizz Air, and Ryanair. 14 The coefficient captures fuel, maintenance, and other operating
expenses that increase with flight frequency and distance. The total fixed cost per flight
hour additionally reflects the constant, market size, and airport-slot terms. Its distribution
in Figure 5 incorporates these components jointly.
The airport-slot coefficient ranges from−$415,000 to−$300,000 per endpoint airport
and product-quarter, reflecting a cost advantage conditional on the other characteristics.
The additional fixed operating cost of a connecting flight ranges from$40,000 to$45,000 per
quarter. This is additional to costs incurred on its direct legs, which are already counted as
direct operations rather than charged again to each connecting itinerary.
Table 9 reports the marginal cost recovered from the pricing first-order conditions and
bounds on total cost per passenger computed by adding the deterministic fixed cost. Low-
cost carriers such as Ryanair and easyJet have total cost per passenger that is substantially
lower than that of full-service carriers like BA/IAG and Lufthansa. Ryanair’s total cost is
$44–45 per passenger and easyJet’s is$46–47, compared with$124–125 for BA/IAG and
$146–147 for Lufthansa. The differences in marginal costs account for much of this ordering,
while the fixed cost component also varies with route networks and passenger volumes. These
estimates measure modeled operating costs on intra-European routes.
13Our fixed cost component excludes passenger marginal costs and fixed cost shocks, whereas industry
operating costs cover a broader set of expenses.
14Using easyJet plc (2019), Wizz Air Holdings Plc (2019), and Ryanair Holdings plc (2019), we divide
annual fuel and maintenance expenses, converted to USD at 2019 annual average exchange rates, by sectors
flown times average sector length in kilometers, and multiply by 860. The resulting hourly equivalents are
approximately$2,957,$2,452, and$2,562, respectively.
30

Table 9: Marginal Cost and Total Cost per Passenger by Airline
Full-Service Carriers Low-Cost Carriers
Airline MC/Pax LB UB Airline MC/Pax LB UB
British Airways 100.3 123.9 125.1 Ryanair 21.4 43.6 45.3
Lufthansa 117.9 145.8 147.3 EasyJet 28.4 46.0 46.9
Air France-KLM 100.2 124.2 126.1 Wizz Air 19.2 43.6 46.3
SAS 79.0 103.2 105.0 Jet2 41.0 71.7 74.3
Finnair 93.5 122.1 128.0 Norwegian 64.2 78.1 80.1
Aegean 136.7 174.6 181.5
LOT Polish 172.4 231.2 233.3
Regional Carriers
Icelandair 97.3 130.0 135.2
Air Europa 61.1 81.4 83.4
Note:MC = Marginal Cost, Pax = Passenger, LB/UB = Lower/Upper Bound of
Total Cost per Passenger. All values in USD. Costs are passenger-weighted and exclude
fixed cost shocks. Bounds computed across the confidence region.
6 Counterfactual Simulations
As discussed in Section 2.1, cost pressures from carbon pricing mechanisms and fuel supply
constraints will increase both fixed operating costs and per-passenger marginal costs. To
quantify how these cost pressures will affect airline network and pricing decisions, we simulate
four counterfactual scenarios that increase costs by$1.0–$2.5 per kilometer flown. We label
these scenarios Low, Medium, High, and Very High and use the abbreviations Low, Med,
High, and VH.
To simulate the impact on fixed costs, we increase the fixed-cost coefficient on Frequency
×Distance by 9, 13.5, 18, and 22.5, respectively, in units of$10,000. To simulate the impact
on per-passenger marginal costs we add a per-passenger carbon surcharge to marginal cost,
proportional to total itinerary distance. The surcharge equalsτ×3.16×2.5/1,000 dollars
per passenger per 1,000 km, whereτis the carbon price in dollars per tonne, 3.16 is the
CO2 emission factor, and 2.5 is marginal fuel use in kg per additional passenger per 1,000
km.15 At carbon prices of$100,$150,$200, and$250, the passenger surcharges are$0.79,
$1.185,$1.58, and$1.975, respectively. Aircraft charges apply once per direct leg. Passenger
15The emission factor follows International Civil Aviation Organization (2024) and marginal fuel use
follows Steinegger (2017).
31

charges cover both legs of connecting itineraries.
Then in each scenario we simulate counterfactual outcomes for each quarter in our sample
using a local-deviation algorithm that iteratively updates airline entry, frequency, and pricing
decisions until convergence. Following Yuan and Barwick (2026), the equilibrium concept is
a restricted subgame perfect equilibrium in which airlines are restricted to local deviations.
Details of the algorithm are provided in Appendix A.
6.1 Carbon Regulation Simulation Results
We classify markets as short-haul if market distance is at most 1,500 km and as medium-
and long-haul otherwise. Market distance is the average observed direct-product distance
within the city-pair, using endpoint distance when no direct product is observed.
We simulate counterfactuals separately for four quarters and four carbon price scenarios.
For each scenario we compute impacts on passenger numbers, prices, carbon emissions,
consumer surplus, profits, carbon tax revenue, and increases in social welfare due to reduced
carbon emissions. Carbon emissions reductions are valued at$215 per tonne ofCO 2. Table
10 reports the aggregate welfare effects, and Table 11 decomposes outcomes by airline type.
Baseline Validation.The baseline generates annual net profit of$3.50 billion (s.d. 0.04),
after deducting deterministic fixed costs and realized fixed-cost shocks from expected variable
profit of$9.15 billion. Relative to revenue of$30.67 billion, the profit margin is 11.4%, within
the range of the 7.3%, 10.2%, and 13.2% operating margins calculated from easyJet, IAG, and
Ryanair’s 2019 accounts. 16 Consumer surplus is$9.55 billion and total passenger numbers
are 331.90 million. Expected passenger traffic and variable profit are 4.70% and 4.98% below
their observed counterparts.
Short-haul markets contribute$7.05 billion of consumer surplus,$2.65 billion of profit
(s.d. 0.02), and 244.64 million passengers. Medium- and long-haul markets contribute$2.50
16Authors’ calculations divide operating profit by revenue. Accounts cover entire networks and ancillary
activities. Model net profit deducts modeled operating costs, but is not corporate profit after financing costs
and income taxes.
32

Table 10: Counterfactual Results
Base Low Med High VH
All Markets
Consumer Surplus 9.55 -13.50 (0.49)% -21.97 (0.40)% -27.80 (0.28)% -33.94 (0.30)%
Profit 3.50 (0.04) -1.42 (1.15)% -16.60 (1.16)% -30.01 (1.12)% -41.78 (1.07)%
Carbon Revenue 1.94 (0.02) 2.36 (0.02) 2.70 (0.02) 2.91 (0.02)
Social Value of CO 2 2.66 (0.04) 3.30 (0.02) 3.69 (0.01) 4.02 (0.02)
Welfare Gain 3.26 (0.04) 2.98 (0.05) 2.68 (0.05) 2.22 (0.05)
Passengers 331.90 -14.28 (0.47)% -22.84 (0.39)% -28.73 (0.27)% -34.89 (0.29)%
Short-haul Markets
Consumer Surplus 7.05 11.73 (0.63)% 2.25 (0.53)% -4.64 (0.39)% -12.37 (0.40)%
Profit 2.65 (0.02) 8.90 (1.11)% -8.01 (1.12)% -23.41 (1.07)% -37.06 (1.02)%
Carbon Revenue 1.75 (0.02) 2.18 (0.02) 2.52 (0.01) 2.73 (0.02)
Social Value of CO 2 0.65 (0.04) 1.17 (0.02) 1.50 (0.01) 1.79 (0.01)
Welfare Gain 3.46 (0.03) 3.29 (0.04) 3.07 (0.04) 2.67 (0.04)
Passengers 244.64 10.79 (0.61)% 1.19 (0.52)% -5.79 (0.37)% -13.55 (0.39)%
Medium- and long-haul Markets
Consumer Surplus 2.50 -84.73 (0.42)% -90.34 (0.39)% -93.16 (0.34)% -94.82 (0.27)%
Profit 0.85 (0.03) -33.73 (1.60)% -43.52 (1.65)% -50.69 (1.61)% -56.59 (1.56)%
Carbon Revenue 0.19 (0.01) 0.19 (0.01) 0.18 (0.01) 0.17 (0.01)
Social Value of CO 2 2.01 (0.01) 2.13 (0.01) 2.19 (0.01) 2.23 (0.01)
Welfare Gain -0.20 (0.01) -0.31 (0.02) -0.39 (0.02) -0.45 (0.02)
Passengers 87.26 -84.60 (0.42)% -90.23 (0.40)% -93.06 (0.34)% -94.75 (0.28)%
Note:Entries are means across 50 parameter and shock draws, with standard deviations in parentheses.
Update orders are averaged within each draw. Monetary levels are in USD billions and passenger levels in
millions. Scenario entries for consumer surplus, profit, and passengers are percentage changes from baseline.
Profit deducts fixed costs, including fixed-cost shocks. Short-haul markets are at most 1,500 km. Welfare
Gain = ∆Profit + ∆CS + Carbon Revenue + Social Value of CO 2.
billion,$0.85 billion (s.d. 0.03), and 87.26 million passengers, respectively. The longer-
distance segment thus accounts for about one-quarter of traffic.
Aggregate Welfare Effects.Under Low, consumer surplus falls by 13.5% and profits by
1.4%, so consumers bear a larger proportional loss. However, profit losses grow faster with
the tax. Under VH they reach 41.8%, compared with 33.9% for consumer surplus. The
reduction in passenger volumes rises from 14.3% to 34.9%.
Carbon revenue and avoided emissions more than offset these private losses. Revenue
rises from$1.94 billion under Low to$2.91 billion under VH. The social value of avoided
emissions rises from$2.66 billion to$4.02 billion. Welfare gains decline from$3.26 billion
(s.d. 0.04) to$2.22 billion (s.d. 0.05). Low therefore maximizes welfare among the scenarios.
Additional emissions benefits at higher rates grow more slowly than private-surplus losses.
33

Table 11: Counterfactual Results by Airline Type
Metric Base Low Med High VH
All
Profit 3.50 (0.04) -1.42 (1.15)% -16.60 (1.16)% -30.01 (1.12)% -41.78 (1.07)%
Fare 92.42 (0.00) 0.15 (0.28)% -2.79 (0.24)% -4.85 (0.22)% -7.47 (0.25)%
Direct departures 29.79 (0.00) -14.05 (0.78)% -24.22 (0.60)% -30.68 (0.43)% -37.21 (0.41)%
Distance Flown 31,627.42 (0.00) -43.80 (0.64)% -54.50 (0.41)% -61.00 (0.25)% -66.43 (0.26)%
FC/Pax 17.03 (0.11) -9.76 (1.09)% -5.87 (1.09)% 0.11 (1.03)% 5.83 (1.06)%
Cost/Pax 81.87 (0.11) -1.77 (0.48)% -4.19 (0.41)% -5.24 (0.34)% -7.07 (0.37)%
F ull-Service
Profit 1.70 (0.01) -13.51 (1.66)% -27.01 (1.79)% -39.00 (1.61)% -51.66 (1.50)%
Fare 132.82 (0.00) -1.31 (0.14)% -0.49 (0.27)% 0.07 (0.31)% 0.58 (0.32)%
Direct departures 17.43 (0.00) -23.08 (1.34)% -40.43 (1.03)% -51.37 (0.72)% -62.34 (0.69)%
Distance Flown 16,450.43 (0.00) -46.56 (1.07)% -62.41 (0.65)% -71.02 (0.39)% -77.90 (0.41)%
FC/Pax 15.84 (0.10) -1.42 (2.17)% -7.32 (2.59)% -8.39 (2.44)% -9.33 (2.81)%
Cost/Pax 121.12 (0.10) -1.70 (0.34)% -1.38 (0.43)% -0.75 (0.45)% -0.21 (0.47)%
Low-Cost
Profit 1.73 (0.03) 10.11 (1.56)% -6.64 (1.35)% -21.36 (1.24)% -32.18 (1.12)%
Fare 59.52 (0.00) 5.49 (0.16)% 6.07 (0.16)% 6.94 (0.15)% 8.29 (0.17)%
Direct departures 11.76 (0.00) -0.02 (0.00)% -0.03 (0.00)% -0.05 (0.01)% -0.06 (0.01)%
Distance Flown 14,355.58 (0.00) -39.56 (0.26)% -44.76 (0.24)% -49.02 (0.23)% -52.88 (0.22)%
FC/Pax 18.00 (0.15) -15.12 (0.82)% -5.83 (0.82)% 2.58 (0.87)% 9.15 (0.92)%
Cost/Pax 49.88 (0.15) 1.53 (0.36)% 5.46 (0.38)% 9.44 (0.37)% 13.23 (0.40)%
Regional
Profit 0.07 (0.00) 7.66 (3.49)% -9.90 (2.87)% -25.31 (2.97)% -39.05 (2.56)%
Fare 97.25 (0.00) -14.50 (0.57)% -15.00 (0.54)% -14.97 (0.56)% -13.88 (0.69)%
Direct departures 0.60 (0.00) -26.79 (0.26)% -27.36 (0.20)% -30.11 (1.21)% -35.34 (1.78)%
Distance Flown 821.41 (0.00) -62.65 (0.81)% -66.41 (0.59)% -69.90 (0.67)% -73.59 (0.80)%
FC/Pax 16.77 (0.27) -28.29 (2.64)% -16.67 (2.30)% -5.92 (2.82)% 3.21 (2.78)%
Cost/Pax 86.89 (0.27) -21.83 (0.86)% -20.17 (0.83)% -18.22 (0.78)% -15.40 (0.73)%
Note:Means and standard deviations are computed as in Table 10. Base reports levels. Scenario columns
report percentage changes from baseline. Profit is in USD billions. Fare and costs are in USD per passenger.
Direct departures and distance flown are in 100,000 departures and 100,000 km, respectively. FC/Pax
includes fixed-cost shocks. Cost/Pax adds marginal costs, including the carbon surcharge. Per-passenger
values divide annual totals by passengers.
Higher distance-related costs induce exit from longer routes and redeployment toward
shorter city pairs. Marginal-cost increases put upward pressure on prices for a given network,
while exit and frequency reductions diminish product variety and schedule convenience. Pas-
sengers on affected routes substitute toward other itineraries or the outside option. Capacity
redeployment can improve short-haul services, and changes in product composition mean av-
erage fares need not rise. On the supply side, shorter flights lower operating costs, offsetting
much of the variable-profit loss under Low. At higher taxes, fewer profitable redeployment
34

opportunities remain.
Asymmetric Effects by Market Segment.Aircraft and passenger charges both scale
with distance, exposing longer routes more strongly. Under Low, medium- and long-haul
consumer surplus falls by 84.7% (s.d. 0.4), whereas short-haul surplus rises by 11.7% (s.d.
0.6). Under VH, longer-distance surplus falls by 94.8% (s.d. 0.3). Passenger losses rise from
84.6% under Low to 94.7% under VH.
Short-haul consumers benefit from redirected capacity at lower rates. Surplus remains
2.3% above baseline under Med, before falling by 4.6% under High and 12.4% under VH.
Profits similarly rise by 8.9% (s.d. 1.1) under Low, compared with a 33.7% loss (s.d. 1.6)
in longer markets. Under VH, both segments lose profit, but the longer-distance decline is
larger, at 56.6% versus 37.1%.
Environmental benefits are also uneven. Longer markets provide$2.01 billion of the$2.66
billion social value of avoided emissions under Low. Even including emissions benefits and
tax revenue, their welfare changes remain negative, from−$0.20 billion under Low to−$0.45
billion under VH. Short-haul welfare gains range from$3.46 billion to$2.67 billion. Positive
aggregate welfare therefore combines gains in shorter markets with losses on country-pairs
dependent on longer routes.
Heterogeneous Responses by Airline Type.Table 11 distinguishes FSCs, LCCs, and
regional carriers (Icelandair and Air Europa).
Profit impacts.Under Low, FSC profits fall by 13.5% (s.d. 1.7), whereas LCC and regional
profits rise by 10.1% (s.d. 1.6) and 7.7% (s.d. 3.5). Surviving services can have lower operating
costs or more favorable competitive conditions despite falling aggregate traffic. The regional
gain is small in dollars. Baseline profit is$0.07 billion, compared with$1.70 billion for FSCs
and$1.73 billion for LCCs. All three lose at higher rates. Under VH, losses are 51.7% (s.d.
1.5), 32.2% (s.d. 1.1), and 39.1% (s.d. 2.6), respectively.
Pricing responses.LCC fare increases range from 5.5% under Low to 8.3% under VH.
FSC fares fall by 1.3% under Low, remain close to baseline under High, and rise by 0.6% under
35

VH. Regional fares fall by approximately 14–15%. The surcharge is proportionally larger
relative to LCC marginal costs. These passenger-weighted averages also reflect product exit
and changing shares. Removing longer, expensive services can lower average fares despite
higher route-level costs.
Network adjustments.LCCs mainly reallocate departures from longer to shorter routes.
Their total frequency falls by only 0.02% under Low and 0.06% under VH, but distance falls
by 39.6% and 52.9%. FSC frequency falls by 23.1% and 62.3%, alongside distance reductions
of 46.6% and 77.9%. Regional frequency falls by 26.8% and 35.3%, and distance by 62.7%
and 73.6%. All groups shorten the average direct departure, but only LCCs largely preserve
departure totals.
Cost structure.LCC fixed cost per passenger falls by 15.1% under Low as shorter routes
reduce operating costs, then rises by 9.2% under VH. FSC fixed cost per passenger remains
below baseline, by 1.4–9.3%, whereas regional costs initially fall by 28.3% before rising by
3.2% under VH. Both passenger volumes and fixed costs change, so their relative movements
determine these ratios. Total cost per passenger rises by 1.5–13.2% for LCCs but falls by
0.2–1.7% for FSCs and 15.4–21.8% for regional carriers. These averages include fixed cost
shocks and reflect network recomposition, helping explain why traffic reductions need not
translate proportionately into lower profits.
Summary.Carbon revenue and avoided emissions outweigh private-surplus losses under
our tax and valuation assumptions. Adjustment is highly asymmetric across carrier types
and market segments. Shorter markets gain welfare, longer markets lose, and FSCs face the
largest proportional profit loss at the highest tax. Reallocation toward shorter direct routes
is central, with LCCs preserving departures while other carriers also contract frequency.
6.2 Geographic Distribution of Welfare Effects
Figures 6–14 depict the geographic distribution of net welfare, consumer surplus, and profit
across European country-pairs. For each outcome, the figures show both baseline values
36

(Figures 6, 9, and 12) and impacts of the Low and Very High carbon tax scenarios (remaining
figures). We omit figures for the intermediate scenarios. We use the market-distance measure
and short-haul classification defined in Section 6.1.
The figures display results for the top 15 country groups ranked by baseline welfare,
accounting for 82.0% of total welfare. Each figure displays one observation per country-pair
in the lower triangle, with domestic markets on the diagonal. The tax scenario figures report
changes relative to the no-tax baseline. The tax scenario titles display the aggregate impacts.
All monetary values are in billions of dollars.
The baseline figures confirm that airline market welfare, consumer surplus, and profits
are concentrated in a relatively small set of high-traffic country-pairs. Spain–UK contributes
approximately$0.97 billion of baseline welfare, followed by domestic Spain at$0.59 billion
and France–Spain at$0.43 billion. This concentration means that even modest proportional
changes on the busiest corridors can have large effects on aggregate surplus. It also high-
lights the distinction between a country’s total activity and outcomes in particular bilateral
markets.
The tax scenario panels show how this concentration changes as airlines redeploy capac-
ity. Country-pairs dependent on longer itineraries can lose passenger service and consumer
surplus even when the social value of avoided emissions is substantial. Other pairs benefit
from capacity redirected toward shorter routes. Positive aggregate welfare gains therefore
coexist with losses on particular country-pairs.
7 Conclusion
This paper estimates a two-stage model of airline competition with endogenous route en-
try, departure frequency, and pricing to quantify the impact of carbon regulation on the
European airline industry. Our counterfactual simulations reveal that the effects of carbon
pricing under the EU ETS are highly asymmetric. Full-service carriers reduce total direct
departure frequency by 23–62% and regional carriers by 27–35%, while low-cost carriers ad-
37

just primarily by reallocating departures toward shorter direct routes. Consumer surplus
declines by up to 34% overall, with medium- and long-haul markets bearing the brunt, while
short-haul markets experience positive net welfare gains as airlines reallocate capacity toward
shorter routes. Airline profits decline by 1–42%, but carbon tax revenue of$1.9–2.9 billion
together with a social value of avoided CO 2 emissions of$2.7–4.0 billion more than offset
these private-surplus losses. These results demonstrate that carbon regulation can achieve
meaningful environmental gains in European aviation, though at significant and unevenly
distributed cost.
38

References
V. Aguirregabiria and C.-Y. Ho. A dynamic oligopoly game of the us airline industry:
Estimation and policy experiments.Journal of Econometrics, 168(1):156–173, 2012.
S. Bauer. Competition and welfare in airport slot allocation.Available at SSRN 5881882,
2025.
P. Bayer and M. Aklin. The european union emissions trading system reduced co2 emissions
despite low prices.Proceedings of the National Academy of Sciences, 117(16):8804–8812,
2020.
S. Berry and P. Jia. Tracing the woes: An empirical analysis of the airline industry.American
Economic Journal: Microeconomics, 2(3):1–43, 2010.
S. T. Berry. Airport presence as product differentiation.The American Economic Review,
80(2):394–399, 1990.
S. T. Berry. Estimation of a model of entry in the airline industry.Econometrica: Journal
of the Econometric Society, pages 889–917, 1992.
C. Bontemps, C. Gualdani, and K. Remmy. Price competition and endogenous product
choice in networks: Evidence from the us airline industry. Technical report, Working
Paper, 2025a.
C. Bontemps, G. Martini, and F. Porta. The effects of lcc subsidies on the tourism industry.
International Journal of Industrial Organization, page 103242, 2025b.
L. Butcher. Aviation: European liberalisation, 1986-2002.House of Commons Library, 3,
2010.
F. Ciliberto and E. Tamer. Market structure and multiple equilibria in airline markets.
Econometrica, 77(6):1791–1828, 2009.
F. Ciliberto, C. Murry, and E. Tamer. Market structure and competition in airline markets.
Journal of Political Economy, 129(11):2995–3038, 2021.
J. Colmer, R. Martin, M. Muuls, and U. J. Wagner. Does pricing carbon mitigate climate
change? Firm-level evidence from the European Union Emissions Trading System.Review
39

of Economic Studies, 92(3):1625–1660, 2025.
G. Cox and X. Shi. Simple adaptive size-exact testing for full-vector and subvector inference
in moment inequality models.The Review of Economic Studies, 90(1):201–228, 2023.
R. Doganis.Flying Off Course: Airline Economics and Marketing. Routledge, London, 4th
edition, 2010.
easyJet plc. Annual report and accounts 2019. Technical report, easyJet plc, 2019. URL
https://corporate.easyjet.com/files/rights_issue/2019-annual-report-and-a
ccounts.pdf. Consolidated income statement, p. 128.
A. Eizenberg. Upstream innovation and product variety in the us home pc market.Review
of Economic Studies, 81(3):1003–1045, 2014.
A. D. Ellerman, C. Marcantonini, and A. Zaklan. The European Union Emissions Trading
System: Ten years and counting.Review of Environmental Economics and Policy, 10(1):
89–107, 2016.
EUROCONTROL. Eurocontrol data snapshot low cost carriers: share of total european
flights. Report (PDF), 2022. URLhttps://www.eurocontrol.int/publication/
eurocontrol-data-snapshot-34-rise-low-cost-carriers-europe. Accessed: 27
February 2026.
EUROCONTROL. Aircraft operating costs — standard inputs for economic analyses. Web
page, 2024. URLhttps://ansperformance.eu/economics/cba/standard-inputs/la
test/chapters/aircraft_operating_costs.html. Accessed: 16 January 2026.
EUROCONTROL and F AA Air Traffic Organization. Comparison of air traffic management-
related operational and economic performance: U.s. – europe. Report (PDF), 2024. URL
https://www.eurocontrol.int/sites/default/files/2024-01/eurocontrol-compa
rison-atm-related-performance-us-europe.pdf. Accessed: 16 January 2026.
European Commission. 2024 carbon market report: a stable and well-functioning market,
driving emissions from power and industry installations to a historic reduction of 16.5%.
Web news release, 2024. URLhttps://climate.ec.europa.eu/news-your-voice/new
40

s/2024-carbon-market-report-stable-and-well-functioning-market-driving-e
missions-power-and-industry-2024-11-19_en. Accessed: 16 January 2026.
European Union Aviation Safety Agency. European aviation environmental report 2024,
2024. Accessed: 16 January 2026.
Eurostat (European Commission). Cities database. Web page, 2026. URLhttps://ec.eur
opa.eu/eurostat/web/cities/database. Accessed: 16 January 2026.
M. Fowlie, M. Reguant, and S. P. Ryan. Market-based emissions regulation and industry
dynamics.Journal of Political Economy, 124(1):249–302, 2016.
M. L. Fowlie. Incomplete environmental regulation, imperfect competition, and emissions
leakage.American Economic Journal: Economic Policy, 1(2):72–112, 2009.
International Civil Aviation Organization. ICAO aircraft engine emissions databank. ICAO
Environmental Protection, 2024. URLhttps://www.easa.europa.eu/en/domains/en
vironment/icao-aircraft-engine-emissions-databank. Accessed: 16 January 2026.
F. Kleibergen and R. Paap. Generalized reduced rank tests using the singular value decom-
position.Journal of econometrics, 133(1):97–126, 2006.
M. Marra. A market for airport slots.Available at SSRN 4948006, 2024.
G. E. Metcalf. On the economics of a carbon tax for the united states.Brookings Papers on
Economic Activity, 2019(1):405–484, 2019.
V. Nocke and N. Schutz. Multiproduct-firm oligopoly: An aggregative games approach.
Econometrica, 86(2):523–557, 2018.
A. Pakes, J. Porter, K. Ho, and J. Ishii. Moment inequalities and their application.Econo-
metrica, 83(1):315–334, 2015.
S. P. Ryan. The costs of environmental regulation in a concentrated industry.Econometrica,
80(3):1019–1061, 2012.
Ryanair Holdings plc. Annual report 2019. Technical report, Ryanair Holdings plc, 2019.
URLhttps://investor.ryanair.com/ryanair-report-year/2019/. Consolidated
income statement, p. 147.
41

Sabre. Market intelligence. Web page, 2025. URLhttps://www.sabre.com/airline-mos
aic/. Accessed: 16 January 2026.
R. Steinegger. Fuel economy for aircraft operation as a function of weight and distance.
Technical report, ZHA W Z¨ urcher Hochschule f¨ ur Angewandte Wissenschaften, 2017.
A. Sweeting. Dynamic product positioning in differentiated product markets: The effect of
fees for musical performance rights on the commercial radio industry.Econometrica, 81
(5):1763–1803, 2013.
G. R. Timilsina. Carbon taxes.Journal of Economic Literature, 60(4):1456–1502, 2022.
Wizz Air Holdings Plc. Annual report and accounts 2019. Technical report, Wizz Air
Holdings Plc, 2019. URLhttps://corporate.wizzair.com/investors/business-res
ults-calendar/. Operating expenses and operating statistics, pp. 22 and 26.
T. G. Wollmann. Trucks without bailouts: Equilibrium product characteristics for commer-
cial vehicles.American Economic Review, 108(6):1364–1406, 2018.
Z. Yuan and P. J. Barwick. Network competition in the airline industry: An empirical
framework.The RAND Journal of Economics, 57(1):39–59, 2026.
42

A Counterfactual Simulation Algorithm
The counterfactual simulation algorithm is as follows. First we specify feasible local
route and frequency deviations and draw 50 parameter vectors and fixed-cost shocks. We
hold these draws fixed throughout the analysis. Then for each draw, we simulate restricted
subgame perfect equilibria using the algorithm below.
Feasible Deviations.Route deviations are restricted to local network deviations that
change a single route at a time. Feasible deviations include: exit, frequency reduction
or increase, or redeployment. Deviations must satisfy the consideration set, slot-capacity,
and fleet capacity constraints in Section 3. Frequency increases require released departure
capacity. Connecting services can be added, canceled, or assigned a different connecting
airport if both direct legs remain active. Profit comparisons include all products in affected
markets, so an unprofitable direct product may support profitable connections.
To account for aircraft capacity constraints, we add a smooth capacity penalty to marginal
cost when implied passengers per flight exceed 200. The penalty takes the form penalty j =
2.28 ln(1 + exp(Lj −200)) dollars per passenger, whereL j is the implied load. The penalty
is negligible sufficiently below the threshold and rises approximately linearly above it. It
discourages concentrating passenger traffic on an unrealistically small number of flights, but
it is not a hard capacity limit.
Frequency deviations, measured in directional departures per day, are restricted to
market-specific bins drawn from the set

0, 1 7  ,  1 7 , 2 7  ,  2 7 , 4 7  ,  4 7 ,2  ,(2,4],(4,6],(6,8],(8,10],10+  .
To ensure feasible frequency deviations are empirically relevant, for each market cell defined
by market size and distance, we select frequency bins that account for at least 90% of observed
direct-departure frequency choices. This gives four to six bins per cell. The distance cells
use the market-distance measure defined in Section 6.1, with short-haul markets at or below
43

1,500 km and medium- and long-haul markets above 1,500 km. Frequencies for indirect
flights are determined by the frequencies of their component legs through the relationship in
Section 5.2.
Parameters and shocks.For the counterfactuals, we add two assumptions. First, we
assume the fixed-cost parameters are uniformly distributed over the 1,147 accepted parameter
vectors in the estimated confidence region. Second, we assume that fixed-cost shocks are
drawn from a truncated normal distribution, truncated to ensure that at the baseline, the
observed product portfolio is more profitable than feasible deviations. The truncated normal
shocks, before truncation, have mean zero and airline-specific variances equal to 5% of the
variance of observed direct products’ deterministic fixed costs (Wollmann, 2018).
For routes and frequencies that are in the consideration set but are not feasible in the
baseline (i.e., routes or frequencies that are blocked by slot or frequency constraints), we
draw fixed-cost shocks from the unconditional normal distribution. For each fixed-cost pa-
rameter vector draw, we draw one complete set of fixed-cost shocks for all airlines and all
feasible routes and frequencies. The fixed-cost shock draws are held fixed throughout all
counterfactual simulations.
Simulation Algorithm.We sequentially evaluate local deviations for all airlines in all
markets. We follow Wollmann (2018); Yuan and Barwick (2026); Bontemps et al. (2025a)
and consider multiple orders of evaluation to explore the potential range of network outcomes.
We consider three orders of network evaluation. The first order is based on variable profits.
For each quarter, we rank markets and airlines within a market based on variable profits.
If an airline has multiple direct routes in the same market, we rank those routes based on
their variable profits. Then, we begin with the market with the highest total variable profits.
For each airline in that market, starting from the airline with the highest variable profits,
we evaluate all feasible deviations for each direct product. If an airline finds a profitable
deviation, it deviates accordingly. After all airlines in the market have been evaluated and
potential deviations executed, we proceed to the next market in the variable profit ranking
44

and repeat the process.
After the direct-product sweep, we evaluate feasible connecting-product deviations on
the resulting direct operating network. Each accepted action updates the affected markets,
and we re-solve their price competition before assessing the next relevant profit comparison.
At the end of each iteration, we update the rankings of markets, airlines, and routes based
on the new variable profits.
The second order reverses the ranking, starting with the markets and products with the
lowest total variable profits. The third order randomizes the evaluation order. Although
direct decisions are anchored in currently active products, their redeployment targets need
not be currently served by the airline. We therefore do not assume that every unserved
market must remain unprofitable after the network changes.
For each order, we repeat the process until no airline can find a profitable supported
deviation or the sequence revisits a previous network. In the latter case, we report average
aggregate statistics across the cycle, rather than treating any one state as a stable network.17
To report results, we aggregate outcomes to the annual level, average across completed
network evaluation sequences within each parameter and shock draw, and then average across
the 50 draws. The reported standard deviations describe variation across these draws after
averaging evaluation orders.
17Cycle averages summarize the algorithm’s outcomes. They are not established mixed-strategy equilibria.
Runs reaching the iteration limit without convergence or a completed cycle are excluded.
45

B Supplementary Figures
Figure 5: Distribution of Fixed Cost per Flight Hour
Figure 6: Welfare by country-pair: baseline.
 Figure 7: Welfare change by country-pair: Low sce-
nario.
46

Figure 8: Welfare change by country-pair: Very High
scenario.
Figure 9: Consumer surplus by country-pair: base-
line.
Figure 10: Consumer surplus change by country-pair:
Low scenario.
Figure 11: Consumer surplus change by country-pair:
Very High scenario.
47

Figure 12: Net profit by country-pair: baseline.
 Figure 13: Net profit change by country-pair: Low
scenario.
Figure 14: Net profit change by country-pair: Very
High scenario.
48
