---
title: 'Industry Dynamics with Cartels: The Case of the Container Shipping Industry'
url: https://arxiv.org/abs/2407.15147
category: consumer-behavior
subcategory: empirical
date: 2024-07
venue: ''
authors:
- Suguru Otani
source: arxiv
pdf_url: https://arxiv.org/pdf/2407.15147
pages: 63
chars: 152716
fetched_at: '2026-11-08T13:15:44+00:00'
kb_version: 1
---

# Industry Dynamics with Cartels: The Case of the Container Shipping Industry

Industry Dynamics with Cartels: The Case of the Container
Shipping Industry∗
Suguru Otani
First version: October 27, 2023
Current version: July 24, 2026
Abstract
This paper studies how shipping conferences—explicit cartels—shaped container shipping through
prices, entry, and investment from 1973–1990. I estimate a structural model to disentangle static pricing
and internal allocation effects from dynamic entry and investment responses. Estimated price wedges
equal 30–70% of mean observed freight rates, and conference rents encouraged entry and shipbuilding.
Removing the conference regime barely changes consumer plus producer surplus but raises net social
welfare across markets by reducing resource costs. For fixed route quantity, the capacity-proportional
benchmark allocation equalizes members’ marginal costs, but alternative quota tilts produce different
dynamic welfare rankings across markets.
JEL Classification:L41, L91, C73, D25.
Keywords:cartels; industry dynamics; entry and exit; investment; container shipping.
∗suguru.otani@e.u-tokyo.ac.jp, Market Design Center, University of Tokyo
I thank my advisor Jeremy Fox for valuable advice. I also thank my committee members, Yunmi Kong, Maura Coughlin, and
Arun Gopalakrishnan. I am especially grateful to Mitsuru Igami for his detailed comments and guidance. I benefited from
extensive comments from Yinghua He, Koichiro Ito, Jihye Jeon, Myrto Kalouptsidi, Kei Kawai, Takuma Matsuda, Yuri Mat-
sumura, Takeshi Murooka, Jun Nakabayashi, Masato Nishiwaki, Taisei Noda, Shosuke Noguchi, Isabelle Perrigne, Yuta Toyama,
Kosuke Uetake, Naoki Wakamori, and Yasutora Watanabe, as well as from participants at the Summer Workshop on Economic
Theory, the 18th Applied Econometrics Conference, the 18th Annual Economics Graduate Student Conference at Washington
University in St. Louis, the 2024 Asia-Pacific Industrial Organization Conference, the Kanematsu Prize conference, and the
Kanto regional meeting of the Japan Society of Logistics and Shipping Economics. This work won the 2023 Kanematsu Prize
from the Research Institute for Economics and Business Administration (RIEB), Kobe University. This work was supported
by JST ERATO Grant Number JPMJER2301 and JSPS KAKENHI Grant Number 24K22604.
1
arXiv:2407.15147v2  [econ.GN]  23 Jul 2026

1 Introduction
Do cartel profits support the development of a capital-intensive industry, or do they induce socially costly
investment? This question cannot be answered from prices alone. Classic theory shows that market structure
shapes incentives for cost-reducing investment (Spence 1984), while fixed setup costs and business stealing
can make the private return to entry exceed its social value (Mankiw and Whinston 1986). Higher markups
transfer surplus to producers and contract output, but the resulting rents can also induce entry and in-
vestment in long-lived capacity. That capacity may expand future output and lower marginal cost, while
entry, continued operation, exit, and investment consume real resources. Cartels can therefore change both
the current allocation and the path of industry formation. This paper quantifies these forces during the
formation of global container shipping.
Container shipping provides a transparent setting because its institutions make both the cartel and
its investment channel observable. Under the long-standing principle of freedom of shipping, governments
generally did not reserve a country’s foreign-trade cargo for its own flag vessels or assign shippers to particular
carriers. For more than a century, however, many jurisdictions also allowed liner carriers serving the same
routes to form explicit cartels. These route-level cartels, known as shipping conferences, set common freight
rates and allocated cargo among members. 1 The capacity-proportional benchmark studied here allocates
each carrier’s conference cargo in proportion to its route-assigned capacity. In the model, this mapping
links each carrier’s revenue to its installed capacity and thus makes cartel organization directly relevant for
shipbuilding incentives.
The industry also experienced a transition from conference control to competition. During the 1960s
and 1970s, containerization expanded while carriers from developing countries entered the world shipping
market. The 1974 Code broadened access to conference membership and established trade-share principles
(United Nations 1974). Conference control subsequently weakened in two stages. In early 1980, Sea-Land
withdrew from a transpacific market to set its rates independently (Federal Maritime Commission 1980).
The Shipping Act of 1984 then required conferences on U.S.-related routes to allow individual members to set
rates independently, making common tariffs harder to sustain. Although the Act did not govern Asia–Europe
routes, their rates also remained low after 1984. Based on these institutional changes and price patterns,
I distinguish a strong conference regime in 1973–1979, a weakened conference regime in 1980–1983, and a
competitive regime from 1984 onward. Historical accounts refer to the sharp and persistent rate decline
surrounding this breakdown as the “Container Crisis” (Broeze 2002). By focusing on the conference era,
this paper complements Jeon (2022), who shows that uncertainty about the demand process and strategic
1Conference membership was route-specific: a carrier could belong to the conference on one route while operating outside
the conference on another. Unlike conferences, modern alliances are global operational agreements.
2

incentives amplify boom–bust investment in modern container shipping.
This transition brings a long-standing policy debate into focus: did conferences stabilize a young, capital-
intensive industry, or did they protect carriers at shippers’ expense? The welfare calculation reflects a
broader industrial-policy trade-off between static distortions and dynamic gains from investment and industry
development (see Juh´ aszet al.2024). Higher conference prices reduce current shipping demand, whereas the
resulting profits may induce entry and shipbuilding. The additional capacity can lower marginal cost, but
entry, continued fleet operation, exit, and shipbuilding absorb resources. Moreover, capacity-based cargo
allocation changes how conference rents are distributed across capacity levels and hence which firms invest.
Which force dominates is an empirical question.
Despite the long policy debate, the literature has lacked a quantitative welfare analysis of competition
and collusion in this industry. Distinguishing these forces requires jointly recovering demand, marginal cost,
the cartel price wedge, and the costs governing firms’ dynamic choices. I assemble the fragmented historical
records into a unified dataset and estimate a structural model that uses route-year variation in prices,
quantities, and regimes together with firm-market-year variation in entry, exit, and shipbuilding investment.
The data combine route-year and firm-market-year information. The route-year data contain conference
freight rates and shipping quantities for six directional routes: eastbound and westbound services in the
transpacific, transatlantic, and Asia–Europe markets. The firm-market-year data use ship-level records from
theContainerisation International Yearbookto measure each carrier’s capacity, entry, exit, and shipbuilding
investment in the three markets.2 The descriptive data cover 1966–1990. I define the conference segment to
include conference members while collective rate setting was effective and the corresponding former members
after it became ineffective. I treat non-conference quantities as exogenous because their price data are not
available.
I first document the price decline. Descriptive regressions associate the common empirical boundaries
in 1980 and 1984 with a 49% fall in conference freight rates. This fact shows that the regime change is
economically large, but price regressions alone cannot separate cartel price effects from changes in demand,
marginal cost, entry, and shipbuilding investment. A structural model is therefore needed to disentangle
these forces and quantify their welfare effects.
The structural model has a static part and a dynamic part. The static demand and supply system follows
the empirical cartel literature (Porter 1983, Igami 2015) in estimating route-year demand, marginal cost, and
a regime-specific cartel price wedge. The dynamic game builds on empirical models of industry evolution
(Igami 2017) and uses the estimated static profits as payoffs. Each year, firms choose whether to enter, exit,
stay, or build larger ships, and the state is the number of firms by capacity class in each market. Conference
2See Otani and Matsuda (2023, 2025) for more information on data construction.
3

rules affect profits through two channels: the estimated cartel price wedge and the capacity-proportional
benchmark allocation. I estimate entry, exit, operating, and investment costs by matching observed firm
decisions. Firms are assumed to anticipate the weakening of the conference regime in 1980 but not its
breakdown in 1984; therefore, the dynamic model uses decisions during 1973–1983 and treats 1984 as the
terminal period.
The estimates imply large cartel price effects. The demand elasticity is about−1.1, compared with
−3.89 for modern container shipping in Jeon (2022); the lower responsiveness plausibly reflects shippers’
limited access to close transport substitutes during the early container era. Conferences raised prices above
marginal cost by$1,807 per twenty-foot equivalent unit (TEU) during 1973–1979 and by$998 per TEU
during 1980–1983. Across routes, these effects correspond to roughly 30–70% of mean observed freight rates
in the corresponding regimes. The dynamic estimates imply entry costs of about$3–4 billion and large
shipbuilding sunk costs. These costs matter because cartel rents encouraged entry and investment in large
container ships.
The counterfactuals vary the strength of cartel control and allow entry and shipbuilding to respond. In
the modeled conference segment, removing the conference regime over 1973–1983 raises consumer surplus
by about 2–4% and lowers producer surplus by about 17–27%, while changing their sum by less than 1%.
After operating, exit, entry, and shipbuilding costs are included, removal raises net social welfare by 2.7% in
the transpacific market, 4.4% in Asia–Europe, and 64.3% in the transatlantic market; the large transatlantic
percentage reflects its low benchmark net social welfare after operating costs. At the opposite extreme,
hypothetical full collusion lowers net social welfare by 8.4% in the transpacific market, 10.0% in Asia–
Europe, and 35.2% in the transatlantic market, while leaving it positive in all three markets. Evaluated
at observed market states, the estimated conference price effect is 15.8% of the full-collusion effect in the
transpacific market, 14.7% in Asia–Europe, and 31.4% in the transatlantic market, so full collusion remains
an upper bound rather than a close approximation to the estimated conference regime. These calculations
end in 1983 and therefore do not credit possible subsequent returns to the accumulated capacity.
I also study the conferences’ internal quota rule. For a fixed route quantity, the capacity-proportional
benchmark allocation equalizes marginal costs across conference members. I compare this rule with alter-
natives that shift conference cargo toward smaller or larger carriers. In the model, these alternatives create
a participation–upgrading trade-off: favoring small carriers encourages entry but weakens incentives to up-
grade into large-capacity states, whereas favoring large carriers weakens entry but strengthens upgrading
incentives. Favoring large carriers induces a costly transition to the largest ships in the transatlantic market
but reduces smaller-carrier capacity and resource costs in the transpacific and Asia–Europe markets. Thus, a
quota rule that is statically efficient need not be dynamically optimal, and the preferred dynamic allocation
4

is market-specific.
The broader policy implication is that competition authorities should evaluate coordination in capital-
intensive industries dynamically. Current price effects can miss the entry and long-lived investment induced
by cartel rents, while internal quota rules determine which firms receive those rents and expand. Where
coordination is permitted, policy should assess both its pricing effects and its internal allocation rule: within-
period shipping-cost minimization alone is not a sufficient efficiency defense, and the preferred rule may differ
across markets.
Related literatureThis paper contributes to three strands of the literature: empirical cartel analysis,
dynamic models of entry and investment, and shipping and containerization. To the best of my knowledge, it
is the first paper to combine explicit cartels, investment dynamics, and an explicit capacity-proportional allo-
cation benchmark in a welfare analysis of container shipping. The combination matters because conferences
affected both current markups and the future market structure through entry and shipbuilding.
First, the paper contributes to the empirical literature on cartels. Structural work has measured the
welfare consequences of collusion in many industries and auction formats. 3 Much of the empirical industrial
organization literature instead studies tacit collusion or estimates conduct (Porter 1983, Bresnahan 1987,
Byrne and De Roos 2019, Matsumura and Otani 2023). Rather than estimating a conduct parameter, I
study shipping conferences as explicit cartel institutions and use observed conference regimes to estimate
price wedges. Related case studies include sugar (Genesove and Mullin 1998, 2001), cement (R¨ oller and
Steen 2006), bidding rings (Asker 2010b), gasoline (Clark and Houde 2013, 2014), coffee (Igami 2015), beer
(Miller and Weinberg 2017), oil (Askeret al.2019), gynecologists (Al´ e-Chilet and Atal 2020), vitamins (Igami
and Sugaya 2022), and U.S. local newspapers (Tiew 2024). Each of these papers studies a specific cartel
environment. My paper adds a setting in which the cartel is an industry institution, the internal allocation
benchmark is explicit within the model, and dynamic investment responses are central to welfare. This
differs from many cartel applications in which the cartel episode is local to a subset of firms or markets and
the main object is the static price effect.
The closest empirical approach is Igami (2015), who studies an international coffee agreement and com-
pares collusion with Cournot-Nash competition in a homogeneous-good market. Miller and Weinberg (2017)
use merger-induced conduct changes to distinguish Bertrand-Nash competition from collusion in the U.S.
beer industry; Clark and Houde (2013) and Clark and Houde (2014) compare collusive and competitive
gasoline markets in Canada. Like these papers, I exploit a regime change. Unlike a difference-in-differences
setting, however, the empirical regime boundaries are imposed across all six routes, so the analysis uses no
3See the survey by Asker and Nocke (2021).
5

untreated-route comparison and instead relies on a structural model to separate cartel price effects from
changes in demand, costs, entry, and investment. The model also lets me quantify counterfactual welfare,
which cannot be recovered from the descriptive price decline alone.
Shipping conferences themselves have long been recognized as important cartels (Levenstein and Suslow
2006, Asker and Nocke 2021). Historical studies examine particular UK shipping cartels in the nineteenth
century (Morton 1997, Podolny and Morton 1999). Wilson and Casavant (1991) provide evidence on the
Shipping Act of 1984 using quarterly data on freight rates and quantities for five selected commodities on
the transpacific route. Their evidence is valuable but does not use cross-sectional variation across U.S.
and non-U.S. routes or firm-level investment behavior. My contribution is to quantify markups, investment
responses, and welfare for the six main container routes during the expansion of global containerization,
where data limitations have previously made broad quantitative analysis difficult.
Second, the paper contributes to dynamic models of entry, exit, and investment. In container shipping,
ship size is both capacity and technology: larger ships lower marginal shipping costs but require large sunk
investment. New generations of ships, such as Panamax ships, therefore matter for both static costs and
dynamic market structure. In my model, firms decide each year whether to enter, exit, stay, or build larger
ships, conditional on the distribution of firms across capacity classes. This builds on empirical dynamic
models such as Igami (2017) and Igami and Uetake (2020). I complement these papers by adding explicit
cartel price wedges and an explicitly modeled internal allocation mechanism that reallocates cartel output
across firms and changes investment incentives. The setting also tracks the early state of a new global
industry, so the model can study how collusive profits shape market structure during industry formation.
Third, the paper connects to recent work on shipping, shipbuilding, and containerization. 4 The closest
paper is Jeon (2022), who shows that uncertainty about the demand process and strategic incentives amplify
investment cycles in container shipping. She combines route-level price and quantity data from 1997–
2014 with firm-level capacity and investment data from 2006–2014. Both papers estimate constant-elasticity
demand on six major directional routes and map capacity-dependent static profits into shipbuilding decisions.
The questions and periods are complementary: she studies demand learning, investment, and scrapping
among major carriers in the modern industry, whereas I study explicit cartels, entry and exit, and a capacity-
proportional benchmark allocation during the industry’s formative decades. Recent studies of modern liner
4The maritime economics literature includes work on core-theory predictions using two routes around 1983–1985 (Pirrong
1992), market power and conference market share after the Act (Clyde and Reitzes 1998), and conference theories such as
monopolistic cartels, contestable markets, destructive competition, and empty cores (Sjostrom 2013). A separate international
trade literature studies containerization as a technology affecting trade flows and adoption. Rua (2014) provides port-level
evidence on diffusion, Bernhofenet al.(2016) study country-level containerization adoption for 1962–1990, and Co¸ sar and
Demir (2018) study modal choice between containerization and breakbulk shipping using Turkish export data. This paper is
related to that work through the historical spread of containerization, but its object is the industrial organization of carriers
rather than trade quantities, adoption, or modal choice.
6

alliances analyze the trade-off between economies of scale and market power using structural and Automatic
Identification System (AIS)-based evidence (Liet al.2024, Petrose 2025). Related work studies tanker cartel
conduct (Asker 2010a), bulk shipping (Kalouptsidi 2014, Greenwood and Hanson 2015, Brancaccioet al.
2020), and tanker congestion (Bai and Li 2021). Upstream shipbuilding studies analyze industrial policy in
ship production (Kalouptsidi 2017, Barwicket al.2025). These papers are closely related but generally use
modern Clarksons data or post-2000 markets, whereas this paper studies the earlier container era and the
transition from conferences to competition. They also study markets with different competitive structures,
so their estimates do not directly answer how liner conferences affected the container industry in the 1970s
and 1980s.
2 Data and Institutional Background
This section introduces the data and institutional changes and then documents the price decline that moti-
vates the model. Arouteis directional, such as the eastbound transpacific route, whereas amarketcombines
both directions between the same pair of regions. Throughout,iindexes carrier firms,rdirected routes,m
markets, andtyears;R m denotes the two directed routes in marketm. Because ships normally serve both
directions, I define firm entry and exit at the market level.
2.1 Data
I combine route-year data on prices and quantities with ship-level records aggregated to the firm-market-
year level. I treat an independent operator or corporate group as one firm. Each route and market includes
conference and non-conference carriers: conference carriers participated in the route agreement, whereas
non-conference carriers operated outside it. Reliable freight-rate series are unavailable for non-conference
carriers, so the price analysis uses conference rates; capacity data cover both groups. Appendix C provides
additional data-construction details.
Route-level prices and quantitiesThe route-year data contain freight rates and shipping quantities for
both directions of the transpacific, transatlantic, and Asia–Europe markets. Because no single source covers
the early container era, Otani and Matsuda (2023) combine several historical sources to construct these six
series for 1966–2009. Figure 1 shows the full series; freight rates generally fell, particularly in the early 1980s,
while shipping quantities expanded substantially.
The estimation sample covers 1973–1990. It begins with the 1973 oil crisis, a major change in shipping
costs, and ends before the Soviet collapse in 1991. The sample also predates later regulatory changes,
7

including the Ocean Shipping Reform Act of 1998.
(a) Price
 (b) Quantity
Figure 1: Container freight rates and shipping quantities by route
Note: Freight rates are conference rates through 1992 and unified conference and non-conference rates from 1993 onward.
Quantities are route-level container shipments. Vertical dashed lines mark the start of international container service in 1966,
the common empirical regime boundary in 1980, coinciding with Sea-Land’s withdrawals, and the U.S. Shipping Act of 1984.
Firm-level capacity and market compositionThe ship-level data come from successive editions of the
Containerisation International Yearbook. For each ship, I observe its build year, operator, assigned route,
and capacity in TEU. I assign each ship to one of the three markets based on its reported main route and
aggregate the two directions within each market. Firms may operate in multiple markets, but ships rarely
served multiple main markets during the sample period, so each ship is assigned to a single market in the
data. I use these records and conference status to construct firm-market-year capacity, entry, and exit and
to proxy shipment shares with tonnage shares.
Figure 2 shows market capacity by conference status, with Sea-Land reported separately. Non-conference
capacity was largest relative to conference capacity in the transatlantic market, conference capacity dom-
inated Asia–Europe before 1980, and the transpacific market lay between these cases. Sea-Land supplied
substantial capacity in the transpacific and transatlantic markets; its documented 1980 conference with-
drawals occurred in the U.S.–Far East trade.
Investment within conference marketsFigure 3 plots each conference carrier’s capacity path, exclud-
ing Sea-Land. Capacity is persistent, but many expansions occur in discrete steps. These patterns motivate
the discrete capacity state in the dynamic model.
Tables 1 and 2 summarize the route-, market-, and firm-level data. There are more non-conference than
8

(a) Transpacific
 (b) Transatlantic
 (c) Asia–Europe
Figure 2: Fleet capacity by conference status and market
Note: The stacked areas show the total TEU capacity of ships assigned to both directions of each market. Sea-Land is shown
separately from the other conference and non-conference carriers.
(a) Transpacific
 (b) Transatlantic
 (c) Asia–Europe
Figure 3: Firm-market-year capacity paths
Note: Each line represents a firm’s total TEU capacity in the corresponding conference market. Sea-Land is excluded.
conference firms in all three markets, especially in the transatlantic market, but individual non-conference
firms are smaller on average. Conference firms operated 5.57–9.63 ships on average, and across firm-market-
year observations their mean share of whole-market capacity was 4%, compared with 1–2% for non-conference
firms (Table 2).
2.2 Institutional Background and Regime Changes
Shipping conferences were route-level agreements among liner carriers that coordinated both prices and
service. Members jointly published tariffs and coordinated vessel deployment, schedules, and cargo allocation.
A carrier’s cargo allocation was commonly linked to its tonnage, while non-conference carriers remained free
to serve the same route. Conferences supported their common tariffs with loyalty arrangements that made it
costly for shippers to switch to outside carriers. The 1974 United Nations Convention on a Code of Conduct
for Liner Conferences also codified principles governing conference participation and cargo shares (United
Nations 1974).
9

Table 1: Summary statistics: route- and market-year data
(a) Route-year variables
N mean sd min max
Conference quantity (million TEU):Q rt 138 0.61 0.47 0.00 2.05
Non-conference quantity (million TEU):Q non rt 138 0.42 0.33 0.00 1.30
Conference freight rate (1,000 USD per TEU):P rt 138 2.79 1.23 0.89 6.65
Log destination GDP: log(X rt) 138 28.26 0.73 26.33 29.42
(b) Market-year variables
Market Type mean sd min max
Asia-Europe Conference Number of firms 18.45 6.94 2.00 25.00
Total capacity (million TEU) 0.16 0.07 0.00 0.26
Non-conference Number of firms 20.67 12.68 2.00 37.00
Total capacity (million TEU) 0.07 0.07 0.00 0.21
Transatlantic Conference Number of firms 14.08 3.46 6.00 17.00
Total capacity (million TEU) 0.10 0.05 0.01 0.18
Non-conference Number of firms 61.04 36.56 3.00 102.00
Total capacity (million TEU) 0.13 0.09 0.00 0.25
Transpacific Conference Number of firms 12.36 5.54 1.00 19.00
Total capacity (million TEU) 0.14 0.11 0.00 0.31
Non-conference Number of firms 25.52 11.53 4.00 38.00
Total capacity (million TEU) 0.09 0.06 0.01 0.19
Note: Panel (a) covers six directional routes through 1990: transatlantic from 1966, transpacific from 1967, and Asia–Europe
from 1971. Panel (b) aggregates the two directions into three markets. In panel (a),P rt,Q rt,Q non rt , andX rt denote the
conference freight rate, conference quantity, non-conference quantity, and destination-region GDP, respectively.
This system evolved alongside containerization, which reduced cargo-handling costs but raised the capital
required for ships, containers, and terminals. National and state-owned carriers from developing countries
entered the world shipping market during the 1970s, often initially outside the conferences. Entry thus
expanded even as conference members continued to coordinate.
Two institutional features map directly into the model. Collective tariff setting appears as a regime-
specific wedge between conference prices and competitive route marginal costs. In the model, capacity-
proportional cargo allocation maps a carrier’s capacity into its service quantity and profit, linking conference
rules to entry, exit, and shipbuilding incentives.
Conference control weakened in two stages. Sea-Land, a major transpacific and transatlantic carrier,
withdrew from a transpacific market in early 1980 to set rates independently (Federal Maritime Commission
1980). Conference discipline weakened, although conferences continued to publish common tariffs. The Ship-
ping Act of 1984 then required conferences to permit independent rate action, authorized service contracts,
and removed antitrust protection from conference loyalty contracts (United States Congress 1984, Federal
Maritime Commission 1985). These changes made common tariffs harder to enforce on U.S.-related routes.
Historical accounts describe the sharp decline in conference freight rates during the early 1980s as the
10

Table 2: Summary statistics: firm-market-year data
(a) Conference firms
Market mean sd min max
Asia-Europe Number of ships 5.57 4.59 1.00 20.00
Total capacity (1,000 TEU) 8.87 10.04 0.60 40.70
Capacity share (conference): ˜simt/Smt 0.05 0.08 0.00 0.57
Capacity share (whole market): ˜simt/Swhole mt 0.04 0.06 0.00 0.47
Transatlantic Number of ships 7.59 7.46 1.00 36.00
Total capacity (1,000 TEU) 7.35 10.62 0.10 66.55
Capacity share (conference): ˜simt/Smt 0.07 0.09 0.00 0.50
Capacity share (whole market): ˜simt/Swhole mt 0.04 0.05 0.00 0.32
Transpacific Number of ships 9.63 8.28 1.00 28.00
Total capacity (1,000 TEU) 11.12 11.76 0.31 47.22
Capacity share (conference): ˜simt/Smt 0.08 0.11 0.00 1.00
Capacity share (whole market): ˜simt/Swhole mt 0.04 0.05 0.00 0.27
(b) Non-conference firms
Market mean sd min max
Asia-Europe Number of ships 3.99 4.92 1.00 30.00
Total capacity (1,000 TEU) 3.42 5.05 0.11 28.01
Capacity share (non-conference): ˜snon imt /Snon mt 0.05 0.09 0.00 0.88
Capacity share (whole market): ˜snon imt /Swhole mt 0.02 0.07 0.00 0.88
Transatlantic Number of ships 3.17 3.18 1.00 26.00
Total capacity (1,000 TEU) 2.15 3.15 0.10 29.81
Capacity share (non-conference): ˜snon imt /Snon mt 0.02 0.04 0.00 0.54
Capacity share (whole market): ˜snon imt /Swhole mt 0.01 0.01 0.00 0.19
Transpacific Number of ships 4.64 4.51 1.00 24.00
Total capacity (1,000 TEU) 3.56 5.21 0.13 32.37
Capacity share (non-conference): ˜snon imt /Snon mt 0.04 0.06 0.00 0.53
Capacity share (whole market): ˜snon imt /Swhole mt 0.02 0.04 0.00 0.51
Note: The sample covers 1966–1990. Firm shipment shares are proxied by tonnage shares. Here, ˜s imt and ˜snon imt denote
carrieri’s observed conference and non-conference market capacities, whileS mt,S non mt , andS whole mt denote total conference,
non-conference, and whole-market capacity, respectively.
“Container Crisis” and associate it with the breakdown of shipping conferences (Broeze 2002). The break-
down refers to the loss of effective conference control over common tariffs, not necessarily the formal disso-
lution of every conference. Appendix A provides the underlying institutional details.
For the empirical analysis, I classify 1973–1979 as a strong conference regime, 1980–1983 as a weakened
conference regime, and 1984 onward as a competitive regime. The common 1980 boundary is a maintained
pooled classification for all six routes rather than an estimated causal effect of Sea-Land’s withdrawal. The
Act directly governed only U.S.-related routes. I use the same boundary for Asia–Europe because its rates
also remained low after 1984; this classification does not attribute their decline to U.S. legislation.
11

2.3 Descriptive Evidence on the Container Crisis
To document the magnitude of the two breaks, I estimate ordinary least squares (OLS) specifications with
the indicators 1(t≥1980) and 1(t≥1984), controlling for the post-oil-crisis indicator 1(t≥1974) used in
the static model. I also control for destination GDP and the crude oil price:
logP rt =δ11{t≥1974}+δ 21{t≥1980}+δ 31{t≥1984}+δ 4 logX rt +δ 5 logW t +τ r +ξ rt,
whereδ 1, . . . , δ5 are regression coefficients,P rt is the conference freight rate,X rt is destination GDP,W t
is the crude oil price,τ r is a route fixed effect, andξ rt is an error term. Specifications without route fixed
effects omitτ r.
Table 3 reports specifications without route fixed effects in columns 1–3 and with route fixed effects in
columns 4–6.5 The signs of the two break coefficients are stable, and the route fixed effects absorb persistent
differences in rate levels across routes. In column 6, the coefficient on 1(t≥1980) is−0.385, corresponding
to rates 32% lower during 1980–1983 than during 1974–1979, conditional on the controls. The additional
coefficient on 1(t≥1984) is−0.283, implying a further 25% decline; the combined post-1984 difference is
49% (exp(−0.385−0.283)−1 =−0.49).
Table 3: Changes in log conference freight rates
(1) (2) (3) (4) (5) (6)
1(t≥1974) -0.439*** 0.109 -0.192* -0.267** 0.177 -0.099
(0.151) (0.074) (0.103) (0.096) (0.105) (0.099)
1(t≥1980) -0.605*** -0.467*** -0.469*** -0.385***
(0.190) (0.150) (0.086) (0.057)
1(t≥1984) -0.594*** -0.338** -0.422** -0.283**
(0.200) (0.133) (0.149) (0.109)
Log destination GDP: log(X rt) 0.059 -0.081 0.137 -0.132 -0.291* -0.024
(0.194) (0.150) (0.214) (0.121) (0.120) (0.126)
Log crude oil price: log(W t) 0.318*** -0.173 0.088 0.242** -0.131 0.067
(0.059) (0.110) (0.066) (0.063) (0.093) (0.081)
Route fixed effects X X X
Observations 108 108 108 108 108 108
R2 0.460 0.411 0.491 0.812 0.787 0.833
AdjustedR 2 0.439 0.388 0.466 0.795 0.767 0.815
RMSE 0.33 0.35 0.32 0.20 0.21 0.19
Note: The dependent variable is the log conference freight rate in U.S. dollars per TEU. The sample contains six routes over
1973–1990. Standard errors clustered by route are in parentheses. Significance levels are denoted by ∗p <0.1, ∗∗p <0.05, and
∗∗∗p <0.01.
These estimates measure conditional price breaks, not the causal effects of the two events. Changes in
marginal costs, demand, capacity, or conduct could all contribute to the decline. The structural model in the
5Appendix E.1 reports the route-specific year-coefficient paths underlying this summary.
12

next section separates these channels and quantifies the associated changes in market structure and welfare.
3 Model
Cartels in capital-intensive industries affect welfare not only through prices but also by changing entry and
long-lived investment: cartel rents may expand capacity by inducing additional entry and shipbuilding, but
the associated resource costs reduce net social welfare. This dynamic channel is central in liner shipping be-
cause the model’s conference price wedges and capacity-proportional allocation link firms’ profits to installed
capacity. The observed freight-rate decline therefore cannot reveal whether conferences merely redistributed
surplus or also distorted entry and fleet composition, because it combines changes in conduct, demand,
marginal cost, and capacity. I use a structural model to recover the competitive cost curve and cartel price
wedge, estimate firms’ dynamic costs, and simulate market structure and welfare with and without the cartel
effect.
The model has two parts. The static part estimates demand and supply for conference routes. It treats
1984 onward as the competitive regime and 1973–1983 as the conference regime, with separate cartel effects
for 1973–1979 and 1980–1983. This part maps demand and tonnage capacity into current profits. The
dynamic part uses these profits to estimate firms’ entry, exit, and shipbuilding decisions and then simulates
how market structure and welfare change under alternative regimes.
I focus on conference markets. Because non-conference price data are unavailable, I do not model sub-
stitution or strategic interaction between conference and non-conference services. Non-conference quantities
are therefore treated as exogenous and excluded from the demand and supply system below. Accordingly, the
counterfactual welfare calculations are partial-equilibrium measures for the conference segment: they hold
the non-conference segment fixed and do not include substitution toward non-conference services, strategic
responses by non-conference carriers, or welfare changes in the non-conference segment.
I consider a finite-horizon, nonstationary dynamic game. For each market-year, incumbents and potential
entrants observe all firms’ tonnage states and exogenous demand. Current incumbents first earn static profits
determined by these states and the cartel effect. They then sequentially choose whether to exit, stay without
investment, or invest in shipbuilding, and potential entrants choose whether to enter. These choices update
the next year’s market structure.6 The finite horizon and sequential move order permit backward induction.
6The dynamic game follows the equilibrium concept and computational approach of Igami (2017, 2018), while the static model
differs by incorporating cartel effects rather than a static oligopoly game. The constant-elasticity route demand and utilization-
based marginal cost parallel Jeon (2022), whose model also includes demand learning, order books, scrapping, chartering,
and capacity deployment in the modern industry. The present finite-horizon state is tailored to entry, exit, shipbuilding, and
observed conference regime changes.
13

3.1 Demand and supply
DemandLetQ rt denote conference shipping quantity on directed routerin yeart. 7 LetP rt(srt, Drt)
denote the conference freight rate, wheres rt collects firms’ route-assigned TEU capacities andD rt is an
exogenous demand state constructed from observed covariates and estimated coefficients.
Demand for conference shipping services on routerin yearthas constant elasticity:
Qrt(srt, Drt) = exp(Drt) [Prt(srt, Drt)]α1 ,(1)
whereα 1 is the price elasticity of demand.
SupplySupposeN rt firms operate on routerin yeart, and letN rt denote their set. Each firm observes
(srt, Drt), wheres rt = (sirt, s−irt) is the vector of representative TEU capacities,s irt is firmi’s own capacity,
ands −irt collects its rivals’ capacities. The dynamic part and Appendix B describe the mapping from discrete
capacity levels to these representative capacities.
Individual supply equationFirmi’s marginal cost of providing service quantityq irt is
mcirt(qirt, sirt) =c rt +γ 1
qirt
sirt
,(2)
whereγ 1 is the utilization-cost parameter andc rt is an additive route-year cost component common to firms
on routerin yeart. Marginal cost rises with utilization, and greater capacity lowers the cost of serving a
given quantity, as in the interior marginal-cost specification of Jeon (2022). I assume no additional firm-level
marginal-cost heterogeneity. Tonnages irt does not fully measure annual service capacity because service
frequency is unobserved.
I define route marginal costM Crt as the capacity-share-weighted average of the individual marginal costs
in (2):
M Crt ≡
NrtX
i=1
sirt
Srt
mcirt(qirt, sirt) =c rt +γ 1
Qrt
Srt
,
whereS rt = PNrt i=1 sirt. In a competitive market,P rt =M Crt. This specification is similar to Porter (1983).
To derive individual supply in the competitive regime, suppose firmichoosesq irt to maximize variable
7Appendix C describes its data construction.
14

profit
πirt(qirt;s irt, srt, Drt) =P rt(srt, Drt)qirt −
Z qirt
0
mcirt(q, sirt)dq,
given demand stateD rt, tonnage capacitys irt included ins rt, and equilibrium priceP rt(srt, Drt). The
first-order condition isP rt(srt, Drt) =c rt +γ 1qirt/sirt. Solving forq irt gives firmi’s individual supply
equation:
qirt(Prt(srt, Drt), sirt) = Prt(srt, Drt)−c rt γ1 sirt.(3)
Aggregating the individual supply equations givesQ rt = PNrt i=1 qirt = Prt−crt γ1 Srt and therefore the competi-
tive route supply equationP rt =c rt +γ 1Qrt/Srt. In the competitive regime, each firm serves the quantity
at which its marginal cost equals the route price. Through 1983, the capacity-proportional benchmark
allocation instead determines each firm’s quantity; from 1984 onward, (3) determines it.
Route supply equation with and without cartel behaviorThe route price equals competitive route
marginal cost plus the route cartel effect:
Prt =c rt +γ 1
Qrt
Srt
+C t,(4)
Ct = ˜γ11(t≤1979) + ˜γ 21(1980≤t≤1983).
The termC t is the route cartel effect, a regime-specific price wedge over competitive route marginal cost.
Here, ˜γ1 and ˜γ2 are the wedges for 1973–1979 and 1980–1983, respectively. This direct approach is related
to Igami (2015); Appendix D compares it with Porter (1983) and discusses the modeling choice. 8
3.2 Equilibrium price, quantity, and profit in spot markets
In the model, the industry regime changes exogenously from the collusive regime through 1983 to the
competitive regime from 1984 onward.
8The alternative conduct-parameter approach requires specifying a static quantity-setting game (Matsumura and Otani 2023,
Otani and Matsumura 2025). The observed competitive regime identifies the cost curve without that restriction, while fixed
schedules, tonnage quotas, and evolving capacity and entry make a stable conduct index a restrictive summary of conference
behavior.
15

Equilibrium prices and quantitiesSubstituting (1) into (4), I obtain the equilibrium priceP ∗ rt(srt, Drt)
as the numerical solution to
Prt =c rt +γ 1
exp(Drt)(Prt)α1
Srt
+C t.
The same equation covers both regimes:C t equals the relevant cartel effect through 1983 and zero from 1984
onward. The fixed point is unique under the standard conditionsα 1 <0 andγ 1 >0. 9 I obtain equilibrium
quantityQ ∗ rt(srt, Drt) by substitutingP ∗ rt(srt, Drt) into (1).
Static profits in marketmand routerFor the dynamic part, I construct market-year variables by
aggregating the corresponding route-year variables. Lets imt denote firmi’s discrete capacity level ands mt
the vector of firm counts by capacity level, as formally defined in Section 3.3. Let ¯s imt denote the market-
specific representative TEU capacity assigned tos imt. For eachr∈ Rm, I sets irt = ¯simt and lets rt collect
these route-level capacities. Firmiin marketmand yearthas static profit
πimt(simt, smt, Dmt) =
X
r∈Rm
πirt(sirt, srt, Drt),(5)
πirt(sirt, srt, Drt) =P ∗ rt(srt, Drt)qirt −
Z qirt
0
mcirt(q, sirt)dq,
s.t.q irt =



Q∗ rt(srt, Drt)ωirt ift≤1983
P ∗ rt(srt,Drt)−crt
γ1 sirt otherwise,
ωirt ∈[0,1],∀i,
NrtX
i=1
ωirt = 1,
whereω irt is the service quota within the cartel andD mt = (Drt)r∈Rm contains the demand states for both
directions in marketmand yeart. Because carrier-level liftings and confidential pool formulas are unavailable,
I approximate each member’s unobserved service share by its share of route-assigned carrying capacity,
ωirt =s irt/ PNrt i=1 sirt. This approximation is equivalent to assuming similar utilization across conference
members within a route-year. Historical evidence indicates that negotiated pool shares were related to
members’ carrying capacity (Bennathanet al.1989:p. 30). 10 I therefore use capacity proportionality as the
preferred, institutionally grounded modeling benchmark. I use the same firm capacities on both directional
routes in a market because each ship serves both directions of a round trip. Section 6 varies the allocation
9Define ∆(Prt) =P rt −c rt −C t −γ 1 exp(Drt)(Prt)α1 /Srt. Underα 1 <0 andγ 1 >0, ∆ ′(Prt)>0, lim Prt →0 ∆(Prt) =−∞,
and limPrt →∞ ∆(Prt) =∞, so the equation has a unique positive solution. The estimates in Section 5 satisfy these conditions. 10Contemporaneous sources support capacity as an observable proxy for service contribution: a Canadian government study
discusses capacity, output, and minimum sailing and cargo obligations in pool bargaining (Canada, Department of Industry,
Trade and Commerce, Transportation Services Branch 1978:pp. 119–124); a Federal Maritime Commission notice records joint
revisions to participation percentages and minimum sailings (Federal Maritime Commission 1973:p. 27322); and UNCTAD
reports describe negotiated, often confidential shares and traditional pools based on actual liftings and freight earnings (United
Nations Conference on Trade and Development 1972:paras. 133–136) and (United Nations Conference on Trade and Development
1986:paras. 160–162). They do not establish a universal tonnage-proportional rule.
16

ruleω irt for the counterfactual simulations.
Firms do not strategically choose utilization in the spot market. Conditional on the state and quota,
quantities and profits are determined without a Cournot quantity-setting game. Appendix D.5 analyzes how
capacity choices affect static profits and reports profit estimates by capacity level.
3.3 Dynamics
Ships are durable and costly to build, so a pricing regime can affect welfare beyond its immediate effect on
freight rates by changing capacity and market structure. I capture this intertemporal margin with a finite-
horizon game in annual periods. The model uses firms’ decisions from 1973 through 1983 and treats 1984 as
the terminal year. This cutoff focuses the estimation on the institutionally coherent pre-breakdown period
and avoids imposing unverifiable assumptions on firms’ beliefs during the uncertain transition after the cartel
breakdown. It covers the three conference markets—transpacific, transatlantic, and Asia–Europe—and treats
them as independent round-trip markets.
Firms, actions, and statesThe players are strategic incumbent carriersi∈ N mt and a fixed pool of
potential entrantsi∈ Npe mt. Potential entrants choose whether to stay out or enter,A pe ={x, e}; incumbents
choose whether to exit, continue without investment, or build enough ships to move to a higher capacity level,
Ainc ={x, k, b}. Each incumbent’s tonnage is represented by a capacity levelsimt ∈ {1,2,3,4}, ordered from
smallest to largest, while potential entrants have state zero. Forl∈ {1,2,3,4}, letN l mt ={i∈ Nmt :s imt =
l}denote the set of level-lincumbents. The endogenous market state iss mt = (N 1 mt, N2 mt, N3 mt, N4 mt), where
N l mt is the number of incumbents in levell. These counts exclude the fixed background carriers used in
the static capacity calculations; Appendix B.2 describes that computational device. Firms also observe the
demand stateD mt from the static model and independently distributed, action-specific type-I extreme-value
payoff shocks, whose component for actionais denoted byε a imt.
T ransitions and payoffsExit removes an incumbent, continued operation leaves its capacity level un-
changed, investment raises it by one level up to level 4, and entry places a firm at level 1 in the next year.
These actions therefore determine the next market state; demand follows its estimated path, and private
shocks are independent across firms and periods. For each feasible actiona, letπ a imt(simt, smt, Dmt, εa imt)
denote the resulting action-specific payoff. Following the timing in Igami (2017), every current incumbent
earns the static profit from Section 3.2 before making its dynamic choice. It then pays the exit costψif
it exits, the operating costϕif it remains active, and the additional investment costI(s imt;ι 1, ι2), defined
below, if it builds. A potential entrant pays the entry costκ e.
17

TimingEach year begins with static market outcomes for the current incumbents. Incumbents then move
by capacity level from level 4 to level 1; each group observes the actions of earlier groups, draws its private
payoff shocks, and moves simultaneously. Potential entrants move last. The state is then updated. In the
terminal periodT, the terminal ex-ante value capitalizes the period profit that firms expect under their main-
tained belief that the 1980–1983 regime continues,V imT (simT , smT , DmT ) =π imT (simT , smT , DmT )/(1−β),
whereβis the annual discount factor. This terminal condition is a boundary (franchise-value) approximation
rather than a continuation of the full dynamic game: it holds terminal static profit fixed and does not model
post-terminal operating costs or exit, entry, and build options. It is applied identically across all coun-
terfactual scenarios. Appendix D.2 reports the capacity thresholds, exact transition and payoff equations,
potential-entrant counts, and full within-year timing.
3.3.1 Dynamic optimization problem
BeliefsFirms have rational expectations about rivals’ strategies. To isolate the conference mechanism, I
condition their dynamic decisions on the estimated paths of demand and marginal costs that determine static
profits; equivalently, firms have perfect foresight over these exogenous profit components. 11 They anticipate
the weakening of the conference regime in 1980 but not its breakdown in 1984. The common 1980 boundary
is a maintained belief restriction, so the dynamic-cost estimates are conditional on this imposed profit path.
Thus, the terminal value is evaluated under the belief that the 1980–1983 regime continues. Appendix E.4
shows that allowing firms to anticipate the 1984 breakdown produces similar estimates.
Choice-specific value functionsThe available actions depend only on the firm’s capacity type:
A(simt) =



{x, e}ifs imt = 0,
{x, k, b}ifs imt ∈ {1,2,3},
{x, k}ifs imt = 4.
Leta imt ∈ A(simt) denote firmi’s action and letε imt = (εa imt)a∈A(simt) denote its private payoff-shock vector.
Let ¯V a imt denote the shock-inclusive choice-specific value, and letVimt denote the ex-ante value before the firm
observes its private payoff-shock vector. Because static market outcomes precede the dynamic choices,π imt
is common to all incumbent choice-specific values. For example, the value of continuing without investment
11Jeon (2022) identifies demand learning using quarterly demand histories, direct shipbuilding and demolition prices, and
firm-level investment and scrapping decisions. The annual historical data here do not contain comparable information with
which to separately identify belief formation from dynamic costs.
18

is
¯V k imt(simt, smt, Dmt, εk imt) =π imt(simt, smt, Dmt)−ϕ+ε k imt
+βE[V imt+1(simt+1, smt+1, Dmt+1)|s imt, smt, aimt =k].(6)
The expectation integrates over rivals’ choices and the resulting market-state transition. The exit, build, and
entry values replace the current payoff and own-state transition according to Section 3.3. After observing
εimt, the ex-post value is
Vimt(simt, smt, Dmt, εimt) = max a∈A(simt) ¯V a imt(simt, smt, Dmt, εa imt).
Ex-ante value and choice probabilitiesThe ex-ante value entering continuation payoffs is
Vimt(simt, smt, Dmt)≡E εimt [Vimt(simt, smt, Dmt, εimt)|s imt, smt, Dmt].
Define the deterministic component of a choice-specific value as eV a imt = ¯V a imt −εa imt. The type-I extreme-value
assumption yields
Vimt(simt, smt, Dmt) =σ

γE + log X
a∈A(simt)
exp
 eV a imt(simt, smt, Dmt)
σ
!
 ,(7)
whereγ E is Euler’s constant andσis the logit scale, normalized to one when profits are measured in billions
of dollars. The corresponding conditional choice probability (CCP) is
Pr(aimt =a|s imt, smt, Dmt) =
exp

eV a imt/σ 
P
a′∈A(simt) exp

eV a′ imt/σ  .(8)
Conditioning on the realized actions of earlier movers is suppressed. Type symmetry implies that firms at
the same capacity level use the same CCP. These CCPs induce the transition distribution of the market
state, and the finite-horizon problem is solved by backward induction from the terminal value. The dynamic
parameter vector isθ π = (κe, ψ, ϕ, ι1, ι2). Appendix D.3 gives the type-specific value functions, expands the
expectation in (6), and derives the market-state transition from the CCPs.
19

3.3.2 Equilibrium concept
I use a finite-horizon perfect Bayesian equilibrium in type-symmetric strategies, following Igami (2017, 2018),
Igami and Uetake (2020). A firm’s type is its capacity level. Conditional on its private payoff shocks, each
firm chooses a pure action; integrating the optimal-choice indicator over the shock distribution yields the
CCP in (8). At each turn, a firm maximizes expected discounted profit given earlier movers’ actions and
correct beliefs about the strategies of firms that move later.
Because private shocks affect rivals only through observed choices and capacity types move sequentially,
each turn reduces to the problem of a representative firm of the relevant capacity type. The finite horizon
then permits backward induction, as in Igami (2017). Economically, the model transmits the conference
regime into entry, exit, and investment through its effect on current and expected future profits. Appendix
D.3 provides the full equilibrium construction.
T echnical specificationsI impose three additional specifications. First, the cost for an incumbent at
capacity levels imt to move up one level is
I(s imt;ι 1, ι2) =



ι1 ifs imt ∈ {1,2},
ι2 ifs imt = 3.
Second, I set the discount factor to the standard annual valueβ= 0.9. Third, I exclude the build action for
level-4 firms, consistent with the observed upper bound of the capacity state.
4 Identification and Estimation
4.1 Demand parameters
Following Kalouptsidi (2014) and Jeon (2022), I specify constant-elasticity route demand and use route-level
fleet characteristics as price instruments. The historical sources consistently report prices, quantities, and
fleet composition at an annual rather than quarterly frequency, so the estimation uses route-year observations.
The instrument set is adapted to the young fleet: the tonnage share of ships over 20 years old provides little
variation before 1986, so the preferred specification uses average ship age and the tonnage share of ships over
15 years old. 12
12Adding the log crude oil price as an additional cost shifter leaves the parameters of interest robust: the demand elasticity
and the cost-side slope and cartel wedges retain their signs and significance. However, the oil-price terms are not significant at
the 5% level, and the first-stageFstatistics fall in both equations, so the preferred demand and cost specifications omit it. With
route fixed effects, a mileage-weighted oil price is numerically equivalent to the aggregate oil price because the mileage weight
is route-constant. The oil price therefore contributes no cross-route variation by construction, and its aggregate time-series
20

Taking logs of the demand equation (1), I estimateα= (α 1, α2, α3, α4, α5, αr) from
log(Qrt) =α 1 logP rt +α 2log(Xrt) +α 31(t≥1974)
+α 41(t≤1979) +α 51(1980≤t≤1983) +α r +ζ rt.(9)
The demand state isD rt =α 2log(Xrt) +α 31(t≥1974) +α 41(t≤1979) +α 51(1980≤t≤1983) +α r. Here,
Xrt denotes destination-region GDP in levels and log(X rt) its logarithm,α r is a route fixed effect, and the
residualζ rt is an econometric demand error that is not part ofD rt or the state used in the dynamic model.
The parameter of primary interest is the demand elasticityα 1. Because route-year priceP rt is correlated
withζ rt, I estimate (9) using instrumental variables (IVs). The price is instrumented with the average age
of ships deployed on each route and the tonnage share of ships over 15 years old. 13 Both instruments are
functions of the current fleet state, which is determined by past entry and shipbuilding decisions and is
therefore predetermined relative to the current independent and identically distributed (i.i.d.) route-year
demand shock. The exclusion restriction is that, conditional on log GDP, route fixed effects, and regime
dummies, the fleet-age measures affect conference quantity only through price; in particular, it rules out
a direct effect through service quality. I add route fixed effects and regime dummies to control for route-
and regime-level unobserved heterogeneity. The regime dummies capture broad shifts over time rather than
demand-side effects of the cartel. I cluster the standard errors at the route level.
The demand parameters are identified from time-series and cross-sectional variation across the six main
routes under the constant-elasticity functional form. Following Jeon (2022), identification also uses the fact
that opposite-direction routes share vessel supply while facing different demand shocks.
4.2 Cost parameters
Based on the supply equation (4), I estimateγ= (γ 0, γ1, γ2,˜γ1,˜γ2, γr) using IVs:
Prt =γ 01(t≥1974) +γ 1
Qrt
Srt
+γ ′ 2Yrt
+ ˜γ11(t≤1979) + ˜γ21(1980≤t≤1983) +γ r +η rt,(10)
whereγ 0 is the coefficient on the post-1973 time control,γ 1 is the supply slope,γ 2 is the vector of coefficients
on the cost shifters, ˜γ1 and ˜γ2 are the regime-specific price wedges,γ r is a route fixed effect, andη rt is an
i.i.d. error term. Like the demand errorζ rt, the supply errorη rt is an econometric residual and is not
variation is largely absorbed by the post-1973 and regime indicators, leaving little identifying variation in either equation.
13Appendix E.3 reports estimates using lagged and alternative fleet-composition instruments.
21

included in the state used in the dynamic model. Route marginal cost is
M Crt =γ 01(t≥1974) +γ 1
Qrt
Srt
+γ ′ 2Yrt +γ r.
The termγ 01(t≥1974) +γ ′ 2Yrt +γ r is the additive route-year cost componentc rt in Section 3. The
cost shiftersY rt are average ship size and the tonnage share of ships over 20 years old; both describe fleet
technology in the route-year cost component. I instrumentQ rt/Srt with log GDP for the destination region.
The exclusion restriction is that, conditional on the cost shifters, the post-1973 time control, route fixed
effects, and regime dummies, destination GDP affects freight rates only through shipping quantity, not
through marginal cost.
The cost parameters are identified by time-series and cross-sectional variation across the six main routes,
given the functional form and the maintained common regime classification described in Section 2. Accord-
ingly, the 1980–1983 wedge is a pooled regime parameter, not the causal effect of Sea-Land’s withdrawal.
4.3 Dynamic parameters
I estimateθ π = (κ e, ψ, ϕ, ι1, ι2) separately for each market by maximum likelihood. For each candidate
parameter vector, the inner loop solves the finite-horizon game by backward induction and computes the
CCPs. The outer loop maximizes the likelihood of the observed entry, exit, continuation, and shipbuilding
choices in 1973–1983; the 1984 terminal year enters only through continuation values. The parameters are
identified by how these choices vary across capacity and market states, given the estimated static profits.
For example, a higher investment cost lowers the build probability relative to continuation. I implement this
nested fixed-point estimator following Rust (1987) and Igami (2017). Appendix B.1 provides the likelihood,
computation, and inference details.
5 Estimation Results
5.1 Demand for container shipping
Table 4 reports the demand estimates. 14 The two fleet-age instruments enter the first stage with opposite
signs: negative for average ship age and positive for the share of ships over 15 years old. The negative
coefficient on average ship age is consistent with lower rates on routes served by older fleets, possibly com-
pensating shippers for lower sailing speed or service frequency. The positive coefficient on the share of ships
over 15 years old is consistent with higher operating costs when older vessels make up a larger share of
14Appendix E.3 and Table 12 compare alternative instrument sets; Table 4 reports the preferred specification.
22

route capacity. The IV estimate of the price elasticity is−1.111: a 1% increase in the freight rate reduces
conference quantity by about 1.11%. 15
Table 4: Demand estimates
1st (log(P rt)) 2nd (log(Q rt))
log(Prt) -1.111***
(0.354)
log GDP: log(X rt) 0.256 0.410*
(0.249) (0.217)
1(t≥1974) 0.104 0.041
(0.084) (0.131)
1(t≤1979) 0.419** 0.552*
(0.162) (0.304)
1(1980≤t≤1983) 0.175 0.168
(0.113) (0.111)
Avg ship age -0.133***
(0.024)
Share (15+ y.o. ships) 1.102
(1.013)
Route FE X X
Num.Obs. 108 108
First-stage F 19.0
R2 Adj. 0.841 0.804
Note: The sample covers six routes in 1973–1990. Column 1 reports the first stage for log(P rt), and Column 2 reports the
IV demand equation. The excluded instruments are average ship age and the tonnage share of ships over 15 years old.
Both columns include log destination GDP, 1(t≥1974), the two regime indicators, and route fixed effects. Standard errors
in parentheses are clustered by route. The first-stage F statistic is a route-clustered joint Wald statistic. Significance
levels are denoted by ∗p <0.1, ∗∗p <0.05, and ∗∗∗p <0.01.
5.2 Cost parameters and cartel effects
Table 5 reports the cost estimates.16 The estimated utilization-cost parameter is ˆγ1 = 596.922, so a one-unit
increase inQ rt/Srt raises route marginal cost by about$597 per TEU, holding the other cost controls fixed.
This positive slope is consistent with the utilization-cost pattern estimated for the modern industry by Jeon
(2022). The negative first-stage coefficient on log GDP indicates that, at annual frequency, destination GDP
shifts utilization net of longer-run capacity adjustment; it should not be read as a pure short-run demand
shift. The estimated cartel wedges are$1,807 per TEU in 1973–1979 and$998 per TEU in 1980–1983,
relative to the competitive regime from 1984 onward. The first wedge equals 33% of the mean 1973–1979
freight rate on the Asia-to-Europe route and 70% on the westbound transatlantic route. Thus, the estimates
imply a large initial cartel wedge that was substantially smaller in 1980–1983.
Figure 4(a) shows that the estimated demand state rises through 1979, declines at the 1980 and 1984
15Jeon (2022) estimates an elasticity of−3.89 using quarterly aggregate route data for 2001:Q2–2014:Q4. The present estimate
pertains to annual conference prices and quantities in 1973–1990.
16Appendix E.3 and Table 13 compare alternative cost specifications; Table 5 reports the preferred specification.
23

Table 5: Cost estimates and regime-specific price wedges
1st ( Qrt Srt ) 2nd (P rt)
Qrt/Srt 596.922*
(327.028)
Avg ship size (1,000 TEU) 0.789 1817.274
(1.160) (1827.054)
Share (20+ y.o. ships) 4.213 -1491.488
(3.639) (2927.073)
1(t≥1974) -0.047 113.941
(0.427) (320.233)
1(t≤1979) -0.162 1807.343***
(0.216) (411.167)
1(1980≤t≤1983) -0.326* 997.543***
(0.158) (368.733)
log GDP: log(X rt) -0.698**
(0.239)
Route FE X X
Num.Obs. 108 108
First-stage F 8.5
R2 Adj. 0.913 0.714
Note: The sample covers six routes in 1973–1990. Column 1 reports the first stage forQ rt/Srt, and Column 2 reports
the IV cost equation. The excluded instrument is log destination GDP. Both columns include average ship size, the
tonnage share of ships over 20 years old, 1(t≥1974), the two regime indicators, and route fixed effects. Standard errors
in parentheses are clustered by route. The first-stage F statistic is a route-clustered Wald statistic. Significance levels
are denoted by ∗p <0.1, ∗∗p <0.05, and ∗∗∗p <0.01.
regime boundaries, and gradually recovers after 1984. Figure 4(b) plots the estimated route marginal cost
crt + ˆγ1Qrt/Srt. Over the sample period, marginal cost rises on both transpacific routes, declines on the
Europe-to-Asia and westbound transatlantic routes, is nonmonotonic on the Asia-to-Europe route, and
remains broadly flat on the eastbound transatlantic route.
(a) Demand stateD rt
 (b) Route marginal costM Crt
Figure 4: Estimated demand state and route marginal cost
24

Figure 5 compares the static equilibria in 1979 under the strong conference regime, in 1983 under the
weakened conference regime, and in 1984 under competition. Across all six routes, the supply equation shifts
downward as the cartel wedge declines and then disappears. Equilibrium freight rates are highest in 1979,
lower in 1983, and lowest in 1984, while equilibrium quantities generally increase despite modest inward
shifts in demand. Route-specific demand, marginal cost, and capacity account for the remaining differences
across routes. These route-year equilibria determine the static profits used in the dynamic model.
(a) Transpacific westbound
 (b) Transatlantic westbound
 (c) Europe to Asia
(d) Transpacific eastbound
 (e) Transatlantic eastbound
 (f) Asia to Europe
Figure 5: Estimated demand and supply equations
Note: Each panel shows the estimated demand and supply equations in 1979, 1983, and 1984. Their intersections determine
equilibrium freight rates and quantities.
5.3 Dynamic parameters
Table 6 reports the dynamic parameter estimates for each market. 17 Entry costs range from$2.9 billion to
$4.2 billion across markets, and exit costs range from$0.7 billion to$3.4 billion. Annual operating costs range
from$0.04 billion in Asia–Europe to$0.50 billion in the transatlantic market. The investment parameters are
reduced-form sunk costs of crossing a capacity threshold, not construction prices for individual ships. They
can absorb the construction or acquisition of multiple vessels, complementary investments in containers
17With profits expressed in billions of dollars, I imposeσ= 1, which fixes the scale of the i.i.d. payoff shocks at one
billion dollars. The reported parameters are payoff-equivalent reduced-form costs under this maintained scale; their dollar
interpretation and the implied counterfactual responsiveness are conditional on this normalization.
25

Table 6: Dynamic parameters
Parameter Transpacific Transatlantic Asia–Europe
Entry cost:κ e 4.153 2.937 3.867
[3.695,4.666] [2.404,3.587] [3.441,4.346]
Exit cost:ψ0.668 3.369 2.762
[0.055,1.536] [2.758,4.115] [1.516,5.033]
Operation cost:ϕ0.206 0.5 0.044
[0.09,0.313] [0.409,0.61] [0.004,0.154]
Investment cost:ι 1 3.344 3.649 3.833
[2.807,3.984] [2.987,4.457] [3.411,4.307]
Investment cost:ι 2 Not identified 9.766 4.135
[8.691,11.634] [2.772,6.168]
Logit scale:σ(normalized) 1.000 1.000 1.000
Log Likelihood -67.691 -53.687 -67.857
Note: Each market aggregates its eastbound and westbound routes. Cost parameters are measured in billions of U.S. dollars,
and the logit scaleσis normalized to one. The investment parameters are reduced-form sunk costs of moving between capacity
levels, not prices of individual ships. Brackets report conditional likelihood-slice ranges based on a 90% chi-squared cutoff,
holding the other parameters at their maximum likelihood values (Appendix B.1). Reported log-likelihood values are kernels
that omit data-only combinatorial constants. In the transpacific market, no level-3-to-4 investment is observed during the
1973–1983 estimation sample, soι 2 is not finitely identified; I treat the corresponding investment action as unavailable.
and terminal facilities, and one-time fleet-deployment and organizational adjustment costs. They should
therefore be interpreted as firm-market-level capacity-expansion costs. The cost of moving from capacity
level 1 or 2 to the next level,ι 1, ranges from$3.3 billion to$3.8 billion. For level-3 firms, the identified cost
of reaching level 4,ι 2, is$4.1 billion in Asia–Europe and$9.8 billion in the transatlantic market; it is not
finitely identified in the transpacific market.
Figure 6 compares the observed market states with the mean of 1,000 simulated equilibrium paths through
the 1984 terminal year. The model reproduces the broad pre-1984 changes in the number of firms by capacity
level, including the expansion of small firms in the transpacific and Asia–Europe markets and the decline of
small firms in the transatlantic market. The simulated paths smooth some year-to-year movements in the
data but provide the benchmark market-structure paths for the counterfactuals in Section 6.
5.4 Welfare Along the Benchmark Path
Table 7 reports discounted consumer surplus, producer surplus, social welfare, and net social welfare along
the benchmark equilibrium path. Consumer surplus accounts for most of gross surplus in every market and
regime, while operating, exit, entry, and shipbuilding costs create a substantial gap between gross surplus
and net social welfare. The transpacific market is largest in both consumer and producer surplus. The
resource-cost adjustment is proportionally most important in the transatlantic market, where benchmark
net social welfare is less than one-tenth of gross surplus. Because the regime totals combine different years,
26

(a) Transpacific
 (b) Transatlantic
 (c) Asia–Europe
Figure 6: Observed and simulated market structure
Note: Solid lines report the mean of 1,000 simulated paths, and dotted lines report the data. Simulated paths end in 1984; the
data continue through 1990.
market states, and discount factors, they describe the benchmark path rather than the causal effect of the
cartel. Section 6 quantifies the model-implied effect by comparing the benchmark with alternative conference
scenarios.
Table 7: Welfare along the benchmark path
Market Regime CS PS SW Net SW
Transpacific 1973-1979 244.71 22.29 267.00 205.14
1980-1983 69.46 6.25 75.71 62.93
Transatlantic 1973-1979 64.20 7.56 71.76 7.83
1980-1983 18.16 2.23 20.39 1.37
Asia–Europe 1973-1979 205.76 20.18 225.94 164.06
1980-1983 58.18 6.48 64.66 52.20
Note: Entries are discounted to 1973 and measured in billions of U.S. dollars. Each row sums annual flows over the indicated
years. CS denotes consumer surplus, PS producer surplus,SW=CS+P S, and Net SW subtracts operating, exit, entry, and
shipbuilding costs from SW. Appendix D.4 defines these measures.
6 Counterfactuals
Shipping conferences affected the industry through two distinct mechanisms: collective control of route prices
and the internal division of conference cargo. The first determined the rents available to conference carriers;
the second determined how those rents were distributed across carriers of different sizes. Because both
mechanisms changed current profits, they could alter entry, exit, shipbuilding, and hence future shipping
capacity. Their welfare effects therefore cannot be inferred from contemporaneous freight rates alone. The
central welfare question is whether conference rents financed valuable capacity expansion or instead induced
entry and shipbuilding whose resource costs exceeded their service gains.
I use the model to answer two counterfactual questions. What market structure would have emerged
27

without conference price coordination? How would quota rules favoring smaller or larger carriers have
changed investment and welfare? The first exercise removes the estimated price wedges and, as an upper
bound, imposes hypothetical full collusion; the second changes the internal quota rule. For each exercise, I
recompute static profits, solve for equilibrium choice probabilities, and simulate 1,000 market paths through
the 1984 terminal state. I measure welfare over the conference period 1973–1983, with all annual flows
discounted to 1973. The 1984 state affects pre-1984 choices through the terminal value but is not included
in the reported welfare totals.
6.1 With and Without Shipping Cartels
In the first counterfactual, I eliminate the cartel effect from the profit function and assume that individual
service supply is determined by equation (3) throughout the sample. This non-cartel counterfactual parallels
the removal of shipbuilding subsidies in Kalouptsidi (2017). I solve for a new equilibrium under ˜γ1 = ˜γ2 = 0
and use the resulting equilibrium choice probabilities to simulate 1,000 paths in each market.
As a complementary upper bound, the model imposes hypothetical full collusion.18 This replaces the esti-
mated cartel wedge with the joint-profit-maximizing markup while retaining the capacity-proportional bench-
mark allocation. The comparison asks how closely the estimated conference regime approached monopoly
behavior. In each period, the conference price satisfies
Prt

1 + 1 α1

=c rt +γ 1
Qrt
Srt
.
Entry, exit, and shipbuilding then respond to the resulting profits.
Figure 7 presents the state transitions under the benchmark, non-cartel, and full-collusion scenarios.
Removing the cartel shifts the transatlantic market away from the largest capacity class: in 1984, the mean
number of level-4 firms falls from 0.66 to 0.27, while the number of level-3 firms rises from 2.70 to 3.25. It
also lowers the mean number of level-3 firms from 5.76 to 5.07 in the transpacific market and reduces level-3
and level-4 firms in Asia–Europe from 2.97 to 2.55 and from 1.61 to 1.41, respectively. Thus, cartel rents
encouraged capacity expansion in all three markets, but the capacity class that responded differed across
markets.
Under hypothetical full collusion, the higher rents produce a pronounced shift toward larger capacity
classes in the transpacific and Asia–Europe markets but only a modest change in the transatlantic market.
18At ˆα1 =−1.111, the condition below implies a price about ten times marginal cost. Forα 1 ≥ −1, the static problem has
no finite solution; the data do not reject the boundary caseα 1 =−1. This scenario is therefore an upper bound, not a policy
counterfactual. The welfare results below are conditional on the preferred pooled additive-wedge and cost specification and on
the selected admissible demand estimate ( ˆα1 <−1); Appendix E.3 shows that both are sensitive, so the reported surplus levels
should be interpreted conditionally.
28

(a) Transpacific
 (b) Transatlantic
 (c) Asia–Europe
Figure 7: Market structure under benchmark, non-cartel, and full-collusion scenarios
Note: Points show mean simulated firm counts under the benchmark. Dashed lines show the counterfactual without the
conference regime, and dotted lines show the hypothetical full-collusion scenario. Colors and shapes identify capacity levels.
Each path is based on 1,000 simulations.
By 1984, the mean number of level-3 firms rises from 5.76 to 6.45 in the transpacific market. In Asia–Europe,
level-3 and level-4 firms rise from 2.97 to 3.26 and from 1.61 to 1.80, respectively. In the transatlantic market,
the level-4 count rises only from 0.66 to 0.68, while the level-3 count is nearly unchanged.
Table 8 compares welfare under these scenarios with the benchmark. Over 1973–1983, removing the
cartel lowers producer surplus by about 17–27% and raises consumer surplus by about 2–4%. The modest
increase in consumer surplus reflects two opposing effects and the relatively low price elasticity of demand.
Removing the cartel wedge directly lowers prices, but the resulting decline in profits discourages entry and
shipbuilding, reduces total capacity, and raises marginal cost through the supply equation. The estimated
elasticity, close to one in absolute value, further limits the quantity response to lower freight rates.
Measured by the sum of consumer and producer surplus, removing conference price coordination changes
welfare by less than 1% in every market: cartel pricing mainly transfers surplus from consumers to producers.
This measure, however, excludes the resource costs associated with the resulting market structure. Entry
and shipbuilding costs fall by 12–23%, and net social welfare rises by 2.7% in the transpacific market, 4.4%
in Asia–Europe, and 64.3% in the transatlantic market. The large transatlantic percentage reflects low
benchmark net social welfare after the operating costs of maintaining many active firms. The transatlantic
estimate is a conference-segment effect relative to a small benchmark denominator, not an industry-wide
welfare effect. Because the calculation ends with the conference period, it does not credit the accumulated
large-ship capacity for returns after the sample period.
Within the model and the 1973–1983 welfare horizon, these findings weaken an efficiency-based justifi-
cation for centralized price and quantity controls during an industry’s early stage. In this setting, cartel
pricing mainly redistributed surplus toward producers and accelerated large-ship investment; whether that
investment improved welfare depends on the horizon over which its costs and returns are evaluated.
29

Hypothetical full collusion produces larger welfare losses than the estimated conference regime. Over
1973–1983, producer surplus rises by about 4–18%, consumer surplus falls by about 3–7%, and their sum
falls by about 2–5% across markets. Entry and shipbuilding costs rise by about 4–14%. Net social welfare
falls by 8.4% in the transpacific market, 10.0% in Asia–Europe, and 35.2% in the transatlantic market,
but remains positive in all three. Using the 1973–1983 average model-implied price difference from the
no-cartel scenario at observed market states, the estimated conference effect is 15.8%, 14.7%, and 31.4% of
the full-collusion effect in the transpacific, Asia–Europe, and transatlantic markets, respectively. Thus, full
collusion remains substantially stronger than the estimated conference regime in every market, although the
transatlantic market comes closest to that benchmark.
Table 8: Welfare evaluation (non-cartel and full-collusion scenarios)
Present value Change from benchmark
Market Regime CS PS SW Net SW CS PS SW Net SW
Non-cartel
Transpacific 1973-1979 248.93 18.41 267.34 211.70 ( 0.02) (-0.17) ( 0.00) (0.03)
1980-1983 70.07 5.37 75.44 63.63 ( 0.01) (-0.14) ( 0.00) (0.01)
Transatlantic 1973-1979 67.01 5.53 72.54 13.20 ( 0.04) (-0.27) ( 0.01) ( 0.69)
1980-1983 18.49 1.66 20.15 1.91 ( 0.02) (-0.26) (-0.01) ( 0.39)
Asia–Europe 1973-1979 210.96 16.12 227.08 172.43 ( 0.03) (-0.20) ( 0.01) ( 0.05)
1980-1983 58.95 5.44 64.39 53.41 ( 0.01) (-0.16) ( 0.00) ( 0.02)
Full collusion
Transpacific 1973-1979 229.30 26.18 255.48 187.10 (-0.06) (0.17) (-0.04) (-0.09)
1980-1983 65.24 7.60 72.84 58.38 (-0.06) (0.22) (-0.04) (-0.07)
Transatlantic 1973-1979 62.31 7.80 70.11 5.42 (-0.03) (0.03) (-0.02) (-0.31)
1980-1983 17.43 2.35 19.78 0.54 (-0.04) (0.05) (-0.03) (-0.61)
Asia–Europe 1973-1979 191.51 23.29 214.80 147.03 (-0.07) (0.15) (-0.05) (-0.10)
1980-1983 54.45 7.58 62.03 47.58 (-0.06) (0.17) (-0.04) (-0.09)
Note: Each row sums annual flows over the indicated subperiod (1973–1979 or 1980–1983); all entries are discounted to 1973 and
measured in billions of U.S. dollars. The non-cartel block removes the conference wedges and quota constraint; the full-collusion
block imposes static joint-profit maximization under the capacity-proportional benchmark allocation. CS denotes consumer
surplus, PS producer surplus,SW=CS+P S, and Net SW subtracts operating, exit, entry, and shipbuilding costs from
SW. Parentheses report proportional changes from the corresponding benchmark subperiod. Appendix D.4 defines the welfare
measures.
30

6.2 Alternative Internal Allocation Rules
Market-share division is central to cartel organization (Marshall and Marx 2014), but its dynamic effects
are usually difficult to measure because internal allocation rules are rarely observed. Shipping conferences
provide an unusual setting in which route-assigned capacity data allow an explicit capacity-proportional
benchmark to be defined and compared with alternative model allocation rules. Holding a route’s conference
price and quantity fixed, changing this rule reallocates rents across capacity levels and thereby changes
the incentives to enter or build larger ships. Economically, the rule acts as targeted support within the
conference: favoring a capacity class raises its current revenue without changing total conference revenue in
a given state.
Two discrete alternative allocation rulesThe benchmark allocates each route’s conference quantity in
proportion to members’ tonnage. I first consider two discrete alternatives that shift conference cargo toward
smaller or larger carriers. These rules are motivated by policies that favor selected firm types through bid
preferences or subsidies, thereby changing participation and investment incentives (Krasnokutskaya and Seim
2011, Fan and Xiao 2015). Let
ωh irt = wh irtsirt PNrt
j=1 wh jrt sjrt , h∈ {S, L},
wherew S irt = 1.25 for capacity levels 1 and 2 and 0.75 otherwise;w L irt reverses these weights. Thus,ω S shifts
quotas toward small carriers andω L toward large carriers. Conditional on a market state, these rules leave
the route price and total quantity unchanged but redistribute profits across capacity levels. The resulting
profit differences alter entry, exit, and shipbuilding incentives.
Figure 8 shows these responses. In the transatlantic market,ω S raises the mean numbers of level-2 and
level-3 firms in 1984 and lowers the number of level-4 firms from 0.66 to 0.51. By contrast,ωL reduces the two
middle classes and raises the number of level-4 firms to 0.78. In the other markets, capacity similarly shifts
toward the levels favored by each rule. In the model, these equilibrium responses reflect a participation–
upgrading trade-off:ω S raises the value of entry at level 1 but weakens incentives to move into and through
the large-capacity states, leaving more firms at intermediate levels, whereasω L lowers the value of entry but
strengthens incentives to upgrade into levels 3 and 4.
Table 9 shows that neither discrete rule has a uniform welfare ranking across markets. Relative to the
benchmark, changes in net social welfare range from−10.3% to 13.1%. In the transatlantic market,ω S raises
net social welfare by 13.1%, whereasω L lowers it by 10.3%. The large-carrier rule raises net social welfare
by 0.8% in the transpacific market and by 0.1% in Asia–Europe; the small-carrier rule raises it by 0.8% in
31

Table 9: Welfare under alternative internal allocation rules
Present value Change from benchmark
Market Regime CS PS SW Net SW CS PS SW Net SW
Small-carrier rule (ω S)
Transpacific 1973-1979 244.39 21.38 265.77 205.42 (0.00) (-0.04) ( 0.00) ( 0.00)
1980-1983 69.26 5.90 75.16 62.55 (0.00) (-0.06) (-0.01) (-0.01)
Transatlantic 1973-1979 64.02 7.29 71.31 9.02 ( 0.00) (-0.04) (-0.01) ( 0.15)
1980-1983 18.07 2.11 20.18 1.40 ( 0.00) (-0.05) (-0.01) ( 0.02)
Asia–Europe 1973-1979 205.62 19.51 225.13 165.07 (0.00) (-0.03) ( 0.00) ( 0.01)
1980-1983 57.98 6.10 64.08 52.85 (0.00) (-0.06) (-0.01) ( 0.01)
Large-carrier rule (ω L)
Transpacific 1973-1979 244.82 21.59 266.41 206.94 (0.00) (-0.03) (0.00) (0.01)
1980-1983 69.54 6.08 75.62 63.32 (0.00) (-0.03) (0.00) (0.01)
Transatlantic 1973-1979 64.28 7.55 71.83 6.84 (0.00) (0.00) (0.00) (-0.13)
1980-1983 18.22 2.25 20.47 1.41 (0.00) (0.01) (0.00) ( 0.03)
Asia–Europe 1973-1979 205.81 19.69 225.50 164.70 (0.00) (-0.02) (0.00) ( 0.00)
1980-1983 58.27 6.34 64.61 51.82 (0.00) (-0.02) (0.00) (-0.01)
Note: Each row sums annual flows over the indicated subperiod (1973–1979 or 1980–1983); all entries are discounted to 1973
and measured in billions of U.S. dollars. The two blocks report the small-carrier ruleω S and the large-carrier ruleω L. CS
denotes consumer surplus, PS producer surplus,SW=CS+P S, and Net SW subtracts operating, exit, entry, and shipbuilding
costs from SW. Parentheses report proportional changes from the corresponding benchmark subperiod. Appendix D.4 defines
the welfare measures.
Asia–Europe and leaves it nearly unchanged in the transpacific market. No discrete alternative therefore
dominates the capacity-proportional benchmark across markets.
(a) Transpacific
 (b) Transatlantic
 (c) Asia–Europe
Figure 8: Market structure under alternative internal allocation rules
Note: Points show mean simulated firm counts under the benchmark. Dashed and dotted lines showω S andω L, respectively.
Colors and shapes identify capacity levels. Each path is based on 1,000 simulations.
32

A one-parameter family of allocation rulesThe two discrete rules establish the direction of the
investment response but provide only two benchmarks. To examine how the capacity-proportional benchmark
trades off within-period shipping costs against dynamic investment incentives, I embed it in
ωirt(λ) = sλ irtPNrt
j=1 sλ jrt , λ≥0,(11)
whereλ= 1 is the capacity-proportional benchmark andλ= 0 assigns equal quotas. Relative to the
benchmark, 0≤λ <1 favors smaller carriers, whereasλ >1 assigns cargo more than proportionally to
tonnage. In particular, quota per unit of tonnage is proportional tos λ−1 irt , so underλ >1 larger carriers
operate at higher utilization rates than smaller carriers. This allocation is feasible in the model because there
is no hard utilization constraint; large values ofλshould therefore be interpreted as design bounds rather
than literal conference rules. For fixed (P ∗ rt, Q∗ rt) and a fixed market state,λ= 1 equalizes marginal costs
across conference members and minimizes aggregate variable shipping cost among feasible quota allocations.
It need not maximize dynamic welfare because changingλalso changes profit differences across capacity
levels and hence the equilibrium capacity path.
Figure 9 reports the welfare ranking across allocation rules. Among the evaluated grid points, transat-
lantic net social welfare is highest atλ= 0.75, 31.7% above the benchmark. Asλrises above one and quotas
become increasingly concentrated on large carriers, net social welfare falls: it is 51.8% lower atλ= 1.25
and turns negative byλ= 2. Atλ= 3, it is−$2.15 billion, or 123.4% below the benchmark. These large
percentages partly reflect the low level of transatlantic benchmark net social welfare. The latter value ofλis
the upper boundary of the grid and should be read as an extreme illustration of a strong large-carrier tilt, not
as an estimated optimum. At the same endpoint, net social welfare instead rises by 1.7% in the transpacific
market and by 2.8% in Asia–Europe, despite declines in gross surplus of 2.5% and 4.5%, respectively. Thus,
strengthening the same quota tilt can have opposite welfare effects across markets and need not preserve the
ranking based on gross surplus.
Figure 10 explains these rankings. The cross-market divergence is driven primarily by entry and ship-
building costs. A large-carrier tilt raises the relative continuation value of higher capacity; because capacity
choices are discrete, this change can either induce costly upgrades or discourage entry and lower-capacity
operation. The upgrade margin dominates in the transatlantic market: atλ= 1.25, the mean number of
level-4 firms in 1984 rises from 0.66 to 0.94, and entry and shipbuilding costs rise by 26.0%. Atλ= 0.75, by
contrast, the level-4 count falls to 0.19 and these costs fall by 19.1%. The contraction margin dominates in
the other markets. In the transpacific market, where the level-3-to-4 build action is unavailable because its
cost is not identified, no level-4 investment occurs anywhere on the grid; at the endpointλ= 3, a stronger
33

(a) Transpacific
 (b) Transatlantic
 (c) Asia–Europe
Figure 9: Welfare under counterfactual allocation rulesω(λ), relative to the capacity-proportional benchmark
λ= 1
Note: Each panel reports the percentage change from the capacity-proportional benchmark (λ= 1, vertical dashed line) in
gross surplus (CS+P S) and net social welfare (CS+P S−F C−XC−SC), where CS denotes consumer surplus, PS producer
surplus, FC operating costs, XC exit costs, and SC entry and shipbuilding costs. Vertical scales differ across panels to show
within-market variation. Open circles mark the highest net social welfare among the evaluated grid points; a circle at an
endpoint does not identify an interior optimum. Present values are discounted to 1973 over 1973–1983. Appendix D.4 defines
the welfare measures.
large-carrier tilt shifts capacity toward level 3 and reduces operating costs by 9.8% and entry and shipbuild-
ing costs by 20.9%, more than offsetting higher exit costs. In Asia–Europe, the same endpoint reduces the
numbers of smaller carriers and lowers operating costs by 14.5% and entry and shipbuilding costs by 27.5%,
again outweighing higher exit costs. Thus, the welfare sign depends on whether the quota tilt triggers costly
capacity expansion or reduces the number of firms incurring entry and expansion costs.
(a) Transpacific
 (b) Transatlantic
 (c) Asia–Europe
Figure 10: Decomposition of the welfare effect of the allocation ruleω(λ)
Note: Each line reports the change fromλ= 1 in the present value of consumer surplus (CS), producer surplus (PS), operating-
cost savings (−F C), exit-cost savings (−XC), entry and shipbuilding-cost savings (−SC), and net social welfare. Values are
discounted to 1973 over 1973–1983 and measured in billions of U.S. dollars. Appendix D.4 defines the welfare measures.
Within the model’s conference segment and 1973–1983 horizon, the counterfactuals show that conference
design affected welfare through prices and rent allocation. Price coordination transferred surplus to carriers
34

and encouraged costly capacity expansion, so removing it raised net social welfare despite modest consumer
gains. At fixed route price and quantity, alternative quotas changed investment and welfare rankings across
markets; minimizing within-period shipping costs did not ensure dynamic efficiency. Antitrust policy should
therefore account for how cartel rents and quota rules shape entry and investment, not only current prices.
7 Conclusion
This paper asks how cartels affect welfare when they shape not only prices but also entry and long-lived
investment. In capital-intensive industries, cartel rents may support valuable capacity expansion or induce
investment whose resource costs exceed its benefits. I combine historical route and fleet data from early
containerization and estimate demand, marginal cost, regime-specific price wedges, and carriers’ entry, exit,
and shipbuilding decisions. The estimated conference wedge declines by about 45% in 1980–1983 relative to
1973–1979, linking the weakening of conference control to firms’ incentives to enter and expand capacity.
Over 1973–1983 in the modeled conference segment, removing the conference regime raises consumer
surplus by about 2–4% and lowers producer surplus by about 17–27%, while changing their sum by less
than 1%. After operating, exit, entry, and shipbuilding costs are included, removal raises net social welfare
in all three markets, whereas hypothetical full collusion lowers it in all three, most sharply in the transat-
lantic market, but leaves it positive in every market. For a fixed route quantity, the capacity-proportional
benchmark allocation equalizes marginal costs across conference members, but alternative quotas change
investment incentives and yield different dynamic rankings across markets. In capital-intensive industries,
cartel welfare therefore depends not only on prices but also on how rents are allocated and converted into
long-lived capacity.
References
Al´e-Chilet, J.andAtal, J. P.(2020). Trade associations and collusion among many agents: evidence
from physicians.The RAND Journal of Economics,51(4), 1197–1221.
Asker, J.(2010a). Leniency and post-cartel market conduct: Preliminary evidence from parcel tanker
shipping.International Journal of Industrial Organization,28(4), 407–414.
—(2010b). A study of the internal organization of a bidding cartel.American Economic Review,100(3),
724–62.
35

—,Collard-Wexler, A.andDe Loecker, J.(2019). (mis) allocation, market power, and global oil
extraction.American Economic Review,109(4), 1568–1615.
—andNocke, V.(2021). Collusion, mergers, and related antitrust issues. In K. Ho, A. Horta¸ csu and
A. Lizzeri (eds.),Handbook of Industrial Organization, Volume 5,Handbook of Industrial Organization,
vol. 5, Elsevier, pp. 177–279.
Bai, X.andLi, Y.(2021). The congestion effect of oil transportation and its trade implications.Available
at SSRN 3851173.
Barwick, P. J.,Kalouptsidi, M.andZahur, N. B.(2025). Industrial policy implementation: Empirical
evidence from China’s shipbuilding industry.The Review of Economic Studies,92(6), 3611–3648.
Bennathan, E.,Escobar, L.andPanagakos, G.(1989).Deregulation of Shipping: What Is to Be
Learned from Chile. World Bank Discussion Paper 67, World Bank, Washington, DC.
Bernhofen, D. M.,El-Sahli, Z.andKneller, R.(2016). Estimating the effects of the container revo-
lution on world trade.Journal of International Economics,98, 36–50.
Brancaccio, G.,Kalouptsidi, M.andPapageorgiou, T.(2020). Geography, transportation, and en-
dogenous trade costs.Econometrica,88(2), 657–691.
Bresnahan, T. F.(1987). Competition and collusion in the American automobile industry: The 1955 price
war.The Journal of Industrial Economics, pp. 457–482.
Broeze, F.(2002).The Globalisation of the Oceans: Containerisation from the 1950s to the Present. 23,
Oxford University Press.
Byrne, D. P.andDe Roos, N.(2019). Learning to coordinate: A study in retail gasoline.American
Economic Review,109(2), 591–619.
Canada, Department of Industry, Trade and Commerce, Transportation Services Branch
(1978).The Influence of Technological Change on the Competitive Environment of Liner Shipping: The
Development of Containerization. Tech. rep., Department of Industry, Trade and Commerce, Ottawa,
report to the Interdepartmental Committee on Matters Relating to the Shipping Conferences Exemption
Act.
Clark, R.andHoude, J.-F.(2013). Collusion with asymmetric retailers: Evidence from a gasoline price-
fixing case.American Economic Journal: Microeconomics,5(3), 97–123.
36

—and—(2014). The effect of explicit communication on pricing: Evidence from the collapse of a gasoline
cartel.The Journal of Industrial Economics,62(2), 191–228.
Clyde, P. S.andReitzes, J. D.(1998). Market power and collusion in the ocean shipping industry: is a
bigger cartel a better cartel?Economic Inquiry,36(2), 292–304.
Cos ¸ar, A. K.andDemir, B.(2018). Shipping inside the box: Containerization and trade.Journal of
International Economics,114, 331–345.
F an, Y.andXiao, M.(2015). Competition and subsidies in the deregulated us local telephone industry.
the RAND Journal of Economics,46(4), 751–776.
Federal Maritime Commission(1973). United States Gulf/Japan Cotton Pool, agreement no. 8682-10.
38 Fed. Reg. 27322 (October 2, 1973).
Federal Maritime Commission(1980).19th Annual Report for Fiscal Year 1980. Tech. rep., Federal
Maritime Commission, Washington, DC.
Federal Maritime Commission(1985).Annual Report of the Federal Maritime Commission for Fiscal
Year 1985. Tech. rep., Federal Maritime Commission, Washington, DC.
Genesove, D.andMullin, W. P.(1998). Testing static oligopoly models: conduct and cost in the sugar
industry, 1890-1914.The RAND Journal of Economics, pp. 355–377.
—and—(2001). Rules, communication, and collusion: Narrative evidence from the sugar institute case.
American Economic Review,91(3), 379–398.
Greenwood, R.andHanson, S. G.(2015). Waves in ship prices and investment.The Quarterly Journal
of Economics,130(1), 55–109.
Igami, M.(2015). Market power in international commodity trade: The case of coffee.The Journal of
Industrial Economics,63(2), 225–248.
—(2017). Estimating the innovator’s dilemma: Structural analysis of creative destruction in the hard disk
drive industry, 1981–1998.Journal of Political Economy,125(3), 798–847.
—(2018). Industry dynamics of offshoring: The case of hard disk drives.American Economic Journal:
Microeconomics,10(1), 67–101.
—andSugaya, T.(2022). Measuring the incentive to collude: the vitamin cartels, 1990–99.The Review
of Economic Studies,89(3), 1460–1494.
37

—andUetake, K.(2020). Mergers, innovation, and entry-exit dynamics: Consolidation of the hard disk
drive industry, 1996–2016.The Review of Economic Studies,87(6), 2672–2702.
Jeon, J.(2022). Learning and investment under demand uncertainty in container shipping.The RAND
Journal of Economics,53(1), 226–259.
Juh´asz, R.,Lane, N. J.andRodrik, D.(2024). The new economics of industrial policy.Annual Review
of Economics,16(1), 213–242.
Kalouptsidi, M.(2014). Time to build and fluctuations in bulk shipping.American Economic Review,
104(2), 564–608.
—(2017). Detection and impact of industrial subsidies: The case of Chinese shipbuilding.The Review of
Economic Studies,85(2), 1111–1158.
Krasnokutskaya, E.andSeim, K.(2011). Bid preference programs and participation in highway pro-
curement auctions.American Economic Review,101(6), 2653–2686.
Levenstein, M. C.andSuslow, V. Y.(2006). What determines cartel success?Journal of Economic
Literature,44(1), 43–95.
Li, L.,W an, Y.andYang, D.(2024). Do shipping alliances affect freight rates? evidence from global
satellite ship data.Transportation Research Part A: Policy and Practice,181, 104010.
Mankiw, N. G.andWhinston, M. D.(1986). Free entry and social inefficiency.The RAND Journal of
Economics,17(1), 48–58.
Marshall, R. C.andMarx, L. M.(2014).The economics of collusion: Cartels and bidding rings. Mit
Press.
Matsumura, Y.andOtani, S.(2023). Resolving the conflict on conduct parameter estimation in homo-
geneous goods markets between Bresnahan (1982) and Perloff and Shen (2012).Economics Letters,229,
111193.
Miller, N. H.andWeinberg, M. C.(2017). Understanding the price effects of the MillerCoors joint
venture.Econometrica,85(6), 1763–1791.
Morton, F. S.(1997). Entry and predation: British shipping cartels 1879–1929.Journal of Economics &
Management Strategy,6(4), 679–724.
38

Otani, S.andMatsuda, T.(2023). Unified container shipping industry data from 1966: Freight rate,
shipping quantity, newbuilding, secondhand, and scrap price.Transportation Research Part E: Logistics
and Transportation Review,176, 103186.
—and—(2025). Unified merger list in the container shipping industry from 1966 to 2022: A structural
estimation of M&A matching.Transport Policy,165, 58–69.
—andMatsumura, Y.(2025). Conduct parameter estimation in homogeneous goods markets with equilib-
rium existence and uniqueness conditions: The case of log-linear specification.Economics Bulletin,45(4),
1755–1761.
Petrose, L.(2025). Economies of scale and alliances in container shipping, job market paper, MIT De-
partment of Economics.
Pirrong, S. C.(1992). An application of core theory to the analysis of ocean shipping markets.The Journal
of Law and Economics,35(1), 89–131.
Podolny, J. M.andMorton, S. F. M.(1999). Social status, entry and predation: The case of british
shipping cartels 1879–1929.The Journal of Industrial Economics,47(1), 41–67.
Porter, R. H.(1983). A study of cartel stability: The joint executive committee, 1880-1886.The Bell
Journal of Economics, pp. 301–314.
R¨oller, L.-H.andSteen, F.(2006). On the workings of a cartel: Evidence from the norwegian cement
industry.American Economic Review,96(1), 321–338.
Rua, G.(2014).Diffusion of Containerization. Finance and Economics Discussion Series 2014-88, Board of
Governors of the Federal Reserve System.
Rust, J.(1987). Optimal replacement of gmc bus engines: An empirical model of harold zurcher.Econo-
metrica,55(5), 999–1033.
Sjostrom, W.(2013). Competition and cooperation in liner shipping. InThe Handbook of maritime eco-
nomics and business, Informa Law from Routledge, pp. 463–486.
Spence, A. M.(1984). Cost reduction, competition, and industry performance.Econometrica,52(1),
101–121.
Tiew, A.(2024).Flailing Firms and Joint Operating Agreements: An Application to US Local Daily Print
Newspapers from 1932 to 1992. Working paper, University of California, Berkeley.
39

United Nations(1974). Convention on a code of conduct for liner conferences. United Nations Treaty
Series, vol. 1334, p. 15, No. 22380.
United Nations Conference on Trade and Development(1972).The Regulation of Liner Confer-
ences: A Code of Conduct for the Liner Conference System. Tech. Rep. TD/104/Rev.1, United Nations,
New York.
United Nations Conference on Trade and Development(1986).Guidelines towards the Application
of the Convention on a Code of Conduct for Liner Conferences. Tech. Rep. UNCTAD/ST/SHIP/1, United
Nations, New York.
United States Congress(1984). Shipping act of 1984. Public Law 98-237, 98 Stat. 67.
Wilson, W. W.andCasavant, K. L.(1991). Some market power implications of the shipping act of 1984:
a case study of the us to pacific rim transportation markets.Western Journal of Agricultural Economics,
pp. 427–434.
40

Appendix (For Online Publication)
This appendix is prepared for online publication and contains supplementary materials. Table 10 lists
the contents.
Table 10: Contents of the Appendix
Appendix Contents Coverage
A Institutional details Conference rules, containerization, and regime changes
B Computation and
estimation details
Dynamic estimation, algorithm, likelihood-slice ranges,
computational time, discretization
C Data details Data construction and merger issues
D Model details Cartel conduct, dynamic setup, welfare measurement, and
the capacity-profit link
E Additional estimation
results
Data fitting, specification and instrument selection, and
robustness to anticipating the breakdown
A Institutional Details
This section provides the institutional details underlying the concise discussion in Section 2.2. It first
describes how conferences coordinated their members and responded to non-conference carriers, then sum-
marizes the spread of containerization and the two events used to define the empirical regimes.
A.1 Conference Agreements and Enforcement
Shipping conferences sought to stabilize liner markets through agreements over rates and service and through
measures that limited competition from carriers outside the conference (Fox 1992, Morton 1997, Clyde and
Reitzes 1998, Podolny and Morton 1999, Fusillo 2003, Marin and Sicotte 2003). Their arrangements covered
three broad areas: limiting rate competition among members, retaining shippers within the conference, and
responding to non-conference entry. Rate agreements set and jointly updated tariffs for individual products.
Vessel allocation agreements coordinated tonnage, voyages, ports of call, operating schedules, and cargo
allocation. These arrangements made conferences explicit price- and quantity-coordinating cartels.
The United Nations Convention on a Code of Conduct for Liner Conferences, adopted in 1974 and
entering into force in 1983 for its contracting states, set out members’ loading and pool-participation rights
and principles for dividing conference trade in trades to which it applied (United Nations 1974). Under
Article 2, national shipping lines of the two trading countries generally received equal participation rights,
while third-country lines could receive a significant share, such as 20%. If one trading country had no
participating national line, its share was distributed among the remaining member lines in proportion to
their existing shares. The Code’s nationality-based participation principles do not supply the carrier-level
service shares required by the empirical model. I therefore approximate each member’s unobserved service
share by its route-assigned carrying-capacity share, as described in Section 3.
Conference tariffs were publicly announced, but non-conference carriers could enter and serve the same
trade routes at lower rates. Conferences used loyalty arrangements to reduce shipper switching. Under a
dual-rate system, a shipper received a lower contract rate in exchange for using only conference carriers
during the contract period. Under a fidelity rebate, a shipper received a rebate after using only conference
carriers for a specified period, commonly four to six months. A deferred rebate added a further waiting period
41

during which the shipper also had to avoid non-conference carriers; the rebate was commonly about 10% of
freight charges. These arrangements are understood as entry-deterrence devices that supported conference
tariffs (Fox 1992, Marin and Sicotte 2003).
Conferences could also deploy “fighting ships” on schedules close to those of a non-conference carrier and
charge lower rates until that carrier left the route. Conference members shared the associated losses. In
the general cartel taxonomy, this practice is a coercive response to non-cartel supply (Marshall and Marx
2014, Harringtonet al.2018). Enforcement differed across markets: Asia–Europe conferences used stricter
membership screening and sometimes pooled freight, whereas transpacific conferences were generally more
open. U.S. law did not categorically prohibit freight or traffic pooling; the Shipping Act of 1916 subjected
such agreements to regulatory filing and approval (United States Congress 1916:secs. 14–15).
A.2 Containerization and Market Structure
International container service began on the transatlantic route in 1966 and on the transpacific route in
1967 with Sea-Land’s service. The first semi-container service on the Asia–Europe route also began in 1967,
and full-container service followed in 1971. Containerization standardized cargo handling and reduced the
labor, time, and specialized knowledge required at ports. At the same time, it made liner shipping more
capital intensive because regular container service required substantial investment in ships, containers, and
terminals. The resulting combination of lower operational barriers and higher capital requirements helps
explain both the entry of new carriers and the importance of shipbuilding investment in the model.
During the 1970s, developing and socialist countries increasingly promoted national and state-owned
shipping lines, many of which initially entered as non-conference carriers. The Convention sought to respond
to demands for access by setting out participation rights for qualifying national lines and the trade-share
principles described above in trades to which it applied. In the 1980s, some Europe-related conferences
also invited non-conference carriers to join as their own shares declined. Containerization additionally
encouraged operational consortia through space chartering, joint terminal use, and schedule coordination.
Unlike conferences, these consortia did not jointly set freight rates; their members retained individual control
over pricing and sales.
A.3 Sea-Land’s U.S.–Far East Conference Withdrawals in 1980
Competition on the transpacific routes intensified in the late 1970s. Sea-Land placed eight 33-knot SL-7
container ships in service in 1972–73 (Federal Maritime Commission 1975:p. 157). Their fuel-intensive design
became increasingly costly after the oil shocks. In early 1980, Sea-Land withdrew from twelve eastbound
conferences in the transpacific trade. The contemporaneous FMC report describes a market with increasing
container capacity, shrinking eastbound cargo, and stronger independent competition (Federal Maritime
Commission 1980). The dual-rate system initially limited its ability to attract conference shippers because
switching could trigger a contractual penalty. Sea-Land therefore focused on import and intermodal cargoes
outside the port-to-port coverage of those contracts and absorbed the cost of returning empty containers from
inland locations. I use 1980 as a common empirical boundary across the three markets because conference
rates weakened broadly around this period, not because Sea-Land withdrew from every conference or route.
42

A.4 The Shipping Act of 1984
The Shipping Act of 1984 was enacted on March 20, 1984, and took effect on June 18, 1984 (United States
Congress 1984, Federal Maritime Commission 1985). It changed conference enforcement through three main
provisions. First, conference agreements had to permit a member to take independent action on a rate or
service item after no more than ten days’ notice. Second, the Act expressly authorized service contracts,
under which a shipper committed a minimum quantity of cargo over a fixed period in exchange for a specified
rate schedule and service level. The minimum quantity was known as the Minimum Quantity Commitment.
The statutory independent-action right did not initially extend to service contracts, so conferences could
still permit, restrict, or prohibit individual members from offering them. Third, the Act removed antitrust
immunity from conference loyalty contracts, effectively ending conference use of the dual-rate system in
U.S. trades. Together, mandatory independent action and the loss of loyalty-contract protection weakened
common tariffs and increased rate competition on U.S.-related routes (Wilson and Casavant 1991, Japan
Maritime Center 2008).
After the traditional conference system weakened, carriers formed stabilization or discussion agreements
under which they exchanged information about demand and capacity and discussed rate-restoration guide-
lines and surcharges without directly binding individual rates. The Transpacific Stabilization Agreement,
formed in 1989 by nine conference and four non-conference carriers, is one example. These arrangements
differed from the earlier conference regime because they lacked the same direct control over tariffs.
The U.S. legislation did not directly govern the Asia–Europe routes. Nevertheless, Figure 13 shows that
Asia–Europe conference rates dropped sharply in 1983 and remained substantially below their 1979 level
after 1984. The paper therefore uses 1984 as a common empirical boundary for the competitive regime in all
six routes, while interpreting the Shipping Act itself as a direct institutional shock only for the U.S.-related
routes.
B Computation and Estimation Details
B.1 Dynamic Parameter Estimation
For each capacity levell∈ {1,2,3,4}, letX l mt,K l mt, andB l mt denote the numbers of incumbents that exit,
continue without investment, and build ships. Thus,N l mt =X l mt +K l mt +B l mt, withB 4 mt = 0. For potential
entrants, letO pe mt andE pe mt denote the numbers that stay out and enter, soN pe mt =O pe mt +E pe mt.
Define the type-specific CCPs as
pa lmt(θπ)≡Pr(a imt =a|s imt =l, smt, Dmt;θ π),
pa 0mt(θπ)≡Pr(a imt =a|s imt = 0, smt, Dmt;θ π).
Type symmetry makes these probabilities common across firms of the same type. Forl∈ {1,2,3}, the
likelihood contribution for incumbents of levellis
Plmt(X l mt, Kl mt, Bl mt |s mt, Dmt;θ π)= N l mt! X l mt!K l mt!Bl mt! [px lmt(θπ)]X l mt  pk lmt(θπ) Kl mt  pb lmt(θπ) Bl mt .
43

For level 4, the contribution is the binomial likelihood
P4mt(X 4 mt, K4 mt |s mt, Dmt;θ π)= N 4 mt! X 4 mt!K 4 mt! [px 4mt(θπ)]X 4 mt  pk 4mt(θπ) K4 mt .
The potential entrants’ contribution is
P0mt(Ope mt, Epe mt |s mt, Dmt;θ π) = N pe mt! Ope mt!Epe mt! [px 0mt(θπ)]Ope mt [pe 0mt(θπ)]Epe mt .
For estimation, I omit the parameter-invariant multinomial and binomial coefficients from these count prob-
abilities. The implemented market-specific log-likelihood is
llm(θπ) =
T−1X
t=1
{Ope mt logp x 0mt +E pe mt logp e 0mt
+
3X
l=1

X l mt logp x lmt +K l mt logp k lmt +B l mt logp b lmt 
+X 4 mt logp x 4mt +K 4 mt logp k 4mt 	 .
The reported log-likelihood values are therefore defined up to data-only additive constants; omitting those
constants does not affect the maximizer or likelihood differences. The likelihood uses decisions observed in
t= 1, . . . , T−1 (1973–1983). The terminal yearT= 12 (1984) supplies continuation values but no choice
observation, consistent with the no-anticipation assumption.
Conditional on the static profit estimates, the entry, exit, continuation, and build frequencies across
capacity and market states identifyθ π = (κ e, ψ, ϕ, ι1, ι2). I estimate the parameters separately by market
to allow the dynamic costs to differ across the transpacific, transatlantic, and Asia–Europe markets. For
each candidateθ π, the inner loop solves the finite-horizon game and its CCP fixed points; the outer loop
maximizesll m(θπ). The following subsection gives the solution algorithm, and the subsequent subsections
describe inference and computational performance.
B.2 Algorithm
I adapt the algorithms of Igami (2017, 2018) to this model. For exposition, fix a candidate parame-
ter vectorθ π and focus on marketm= 1. For computation, I index each feasible market states mt
by an integer in{1, . . . , S}. As in the empirical exercise, I fix the number of potential entrants,N pe mt,
at four, except in Asia–Europe, where it is five. Writeg(s, a) for the deterministic own-state transi-
tion:g(s, x) = 0,g(s, k) =s,g(s, b) =s+ 1, andg(0, e) = 1 for the feasible state-action pairs. Let
Pm(· |simt, smt, aimt) denote the induced market-state transition probability conditional on the focal firm’s
state and action. In equilibrium, a fixed point in CCPs determines the corresponding ex-ante value functions.
Suppressing the deterministic demand-state argument for compactness, the terminal values are initialized as
VimT (simT , smT ) =π imT (simT , smT )/(1−β), whereπ imT is the regime-continuation terminal profit consis-
tent with the no-anticipation assumption in Section 3. The algorithm to compute ex-ante value functions
via backward induction proceeds as follows.
Algorithm 1: V alue F unctions and CCPs
44

1. Fort=T−1, . . . ,1, take the ex-ante value functionV imt+1(simt+1, smt+1) as given and evaluate the
exit, operating, and investment costs underθ π.
(a) For each of theSfeasible values ofs mt, obtain the number of incumbent firmsN mt.
(b) For eachi∈ N mt, initialize Pr(a imt =a|s imt, smt) for alla∈ A(s imt) and the action-specific
continuation expectations fora∈ A(simt)\ {x}.
(c) For eachi∈ N pe mt, initialize Pr(a imt =a|s imt = 0, smt) for alla∈ A(0) and the continuation
expectation for entry.
(d) Find the CCP fixed point as follows.
(i) For levell= 4 and for alla∈ A(l) andi∈ N l mt,
A. Given the previous expectation and CCPs, together withN mt andN pe mt, compute the joint
action-count likelihood defined in Section B.1 for all feasible exit, continuation, build, and
entry counts.
B. ComputeP m(smt+1 |s imt, smt, aimt =a) for each own actionaand allSfeasible next-
period states from the joint likelihood and the incumbent and potential-entrant counts,
removing firmifrom its type’s rival count and adding its own destination level determin-
istically.
C. Given the joint likelihood, transition probabilities, andV imt+1(g(simt, a), smt+1), compute
E[Vimt+1(g(simt, a), smt+1)
|s imt, smt, aimt =a]
=
SX
smt+1=1
Pm(smt+1 |s imt, smt, aimt =a)
× Vimt+1(g(simt, a), smt+1),
for eacha∈ A(simt)\ {x}.
D. Given the updated expectation, compute new CCPs. I use the log-sum-exp form to
prevent numerical overflow.
E. Compute the incumbent CCP gap as the sum of the absolute differences between the new
and old choice probabilities.
F. Replace each old incumbent CCP with the average of its new and old values.
G. Setl=l−1 and repeat these steps untill= 1.
(ii) For potential entrants,
A. Given the previous expectations and CCPs, together withN mt andN pe mt, compute the
joint action-count likelihood for the other players.
B. ComputeP m(smt+1 |s imt = 0, smt, aimt =a) for eacha∈ A(0), removing potential
entrantifrom the rival count and adding its own destination state deterministically.
C. Given the joint likelihood, transition probability, andV imt+1(g(0, a), smt+1), update the
action-specific continuation expectation for entry using the old CCPs; staying out has no
continuation value.
D. Given the updated expectation, compute new CCPs using the log-sum-exp form.
45

E. Compute the potential-entrant CCP gap as the sum of the absolute differences between
the new and old choice probabilities.
F. Replace each old potential-entrant CCP with the average of its new and old values.
(iii) Check whether (incumbent CCP gap) + (potential-entrant CCP gap)<0.01. If so, retain the
new CCPs as the fixed point; otherwise, return to step (i).
(iv) Given the fixed-point CCPs and updated expectations, compute the ex-ante value function
Vimt(simt, smt).
I nest Algorithm 1 as the inner loop and maximize the market-specific log-likelihoodll m(θπ) in the
outer loop. The outer loop uses Nelder–Mead from five economically distinct starting values, followed by a
polishing restart from the best point. Multiple starts address saturated likelihood plateaus, such as regions
in which all incumbents exit with probability close to one. For the fixed point in step 1(d), I use a damped
policy-function iteration similar to Kasahara and Shimotsu (2012), with a one-half damping weight, a 0.01
tolerance for the summed CCP gap, and a maximum of 15 iterations. I compute expectations over rivals’
actions by sequentially convolving the capacity-level multinomial distributions of exit and investment counts
with the binomial distribution of entries, rather than enumerating all joint action profiles. Unit tests confirm
that the two methods agree to machine precision, while factorization reduces each likelihood evaluation to
a few seconds. To limit the state space and computational burden while preserving each market’s observed
minimum presence in each capacity class, I treat the componentwise sample minima as fixed background
carriers. These carriers enter the static capacity and profit calculations but do not make dynamic entry,
exit, or investment choices; the dynamic state records carrier counts above this fixed background.
B.3 Calculation of conditional likelihood-slice ranges
I report conditional one-parameter likelihood-slice ranges rather than profile-likelihood confidence intervals.
Let ˆθπ denote the maximum likelihood estimate and let ˜θπj (u) equal ˆθπ except that parameterjis set
to ˆθπj eu. For each estimated parameter, I evaluate the likelihood on an eleven-point grid withuequally
spaced on [−1,1], holding all other parameters at their maximum likelihood values. The range retains grid
values satisfying 2{ll m(ˆθπ)−ll m(˜θπj (u))} ≤χ2 1,0.90 = 2.706. Because the nuisance parameters are held at
their maximum likelihood values rather than re-optimized, the chi-squared cutoff serves as a descriptive
likelihood threshold and the ranges do not claim nominal 90% coverage. I do not use Wald intervals because
the likelihood has step-like regions, as in Igami (2017, 2018), Igami and Uetake (2020). When the initial
grid yields a degenerate or boundary interval, the grid is recomputed with a narrower (0.35) or wider (2.5)
log half-width and thirteen points. As in Igami (2017), the reported ranges understate overall uncertainty
because they do not incorporate the estimation error of the first-stage static parameters.
B.4 Computational time
The main computational burden comes from Algorithm 1, in particular, finding a CCP fixed point at every
feasible market state and year for each candidate parameter vector. With the factorized computation of
rivals’ action distributions described above, one evaluation of the joint log-likelihood takes a few seconds
per market on a laptop. Using eight Julia threads, the multistart estimation ofθ π takes about two minutes
for the transatlantic market, ten minutes for the transpacific market, and twenty-two minutes for the Asia–
Europe market, whose state space is the largest. Computing the conditional likelihood-slice ranges adds
several minutes per market. Simulating 1,000 equilibrium paths takes less than a minute per market.
46

B.5 Discretization details
To compute static equilibrium outcomes from the discrete capacity states, I let ¯simt denote the market-specific
representative TEU capacity assigned to states imt and specify its logarithm below. The state thresholds
are common across markets, but representative capacities may differ because the capacity distributions are
heterogeneous. I selected the following representative log capacities manually, before dynamic estimation,
to approximate the levels and time paths of equilibrium prices, quantities, and total tonnage; no formal
objective function or sampling weights were used, and the values are held fixed throughout estimation and
the counterfactuals. Figure 11 shows that the approximation is weaker in the transpacific market, especially
for prices. For the Asia–Europe market,
log ¯simt =



10.5 ifs imt = 4
10.0 ifs imt = 3
9.0 ifs imt = 2
8.0 ifs imt = 1.
For the transpacific market,
log ¯simt =



10.5 ifs imt = 4
9.5 ifs imt = 3
8.5 ifs imt = 2
8.0 ifs imt = 1.
For the transatlantic market,
log ¯simt =



12.1 ifs imt = 4
10.1 ifs imt = 3
9.2 ifs imt = 2
7.0 ifs imt = 1.
Figure 11 compares equilibrium outcomes evaluated at the discretized observed states with the data. The
model captures the broad patterns, with some lags and deviations due to discretization.
C Data Details
C.1 Route-Year Prices and Quantities
The route-year price and quantity series follow the construction in Otani and Matsuda (2023). For each
route-year, total quantity is decomposed asQ whole rt =Q rt +Q non rt , whereQ rt andQ non rt are conference and
non-conference quantities. The two directional route quantities sum to market quantityQ whole mt . I recover
conference and non-conference quantities by applying their capacity shares to total quantity, which assumes
that utilization does not differ systematically between the two segments within a market-year. Historical
industry utilization rates were 80–95%, and I found no evidence of systematically lower utilization in either
47

(a) Transpacific: price
 (b) Transatlantic: price
 (c) Asia–Europe: price
(d) Transpacific: quantity
 (e) Transatlantic: quantity
 (f) Asia–Europe: quantity
(g) Transpacific: total tonnage
 (h) Transatlantic: total tonnage
 (i) Asia–Europe: total tonnage
(j) Transpacific: firm profit
 (k) Transatlantic: firm profit
 (l) Asia–Europe: firm profit
Figure 11: Estimated market-year prices, quantities, total tonnage, and firm profits by capacity level
Note: Each outcome is evaluated at the discretized state corresponding to the observed market state. Price and quantity are
sums over the two directed routes in a market, whereas total tonnage counts the market’s capacity once.
48

segment. The model treatsQ non rt as exogenous and does not model customers’ choices between conference
and non-conference services. I found no continuous non-conference freight-rate series in theContainerisation
International YearbookorThe Japan Maritime Daily. Practitioner interviews suggest that non-conference
rates were often 20–30% below conference rates, but they do not provide a consistent time series.
C.2 Ship-Level Records and Firm Histories
The ship-level records assign each vessel a main route. When a vessel is reported on multiple main routes and
its capacity cannot be allocated across them, I classify it as “Multiple routes” and omit it from the market-
level analysis. I construct the entry, exit, and conference-status histories from several archival sources (Pace
1981, Gilpin 1983, Department of Transportation, the United States 1992, Maritime Industry Research
Institute 2004, Van Hamet al.2012) and the Port of Long Beach timeline (https://polb.com/port-info/
timeline/). Firm shipment shares are proxied by capacity shares, which assumes that utilization does not
differ systematically across firms within a market-year.
C.3 Mergers
Industry-level merger patterns between 1966 and 2022 are documented by Otani and Matsuda (2025); Otani
(2021) studies the 1964 consolidation of Japanese shipping firms before global containerization. The sample
contains two mergers in 1986, three in 1988, and two in 1990. Because the dynamic likelihood uses firm
decisions only through 1983, these mergers do not enter the dynamic estimation. In the descriptive post-1984
firm histories, I code an acquired firm as exiting. I code an acquirer as investing if its capacity moves to a
higher level in the following year.
D Model Details
D.1 Cartel-Effect Specification and Alternative Conduct Models
The main model and Porter (1983), who studies the Joint Executive Committee railroad cartel, differ in
how they represent collusive conduct. The main model does not specify a static strategic game: it recovers
competitive marginal cost from the 1984–1990 regime and represents earlier conference pricing with regime-
specific wedges. By contrast, Porter (1983) embeds a conduct parameter in a quantity-setting game. Both
approaches imply that price equals marginal cost under competition, but they interpret collusive prices
differently.
To make the comparison explicit, consider the constant-elasticity demand equation (9). Under Porter’s
marginal-cost specification,mc irt(qirt) =νa irqν−1 irt , wherea ir is a firm-specific cost shifter andν >1. The
firm-level first-order condition can be written as
Prt

1 + θirt
α1

=mc irt(qirt),
where the conduct parameterθ irt equals zero under competition, one under joint-profit maximization, and
49

qirt/Qrt under Cournot competition (Bresnahan 1982). Weighting these conditions by quantity shares gives
Prt

1 + θrt
α1

=
X
i∈Nrt
qirt
Qrt
mcirt(qirt),
θrt =
X
i∈Nrt
qirt
Qrt
θirt.
Conditional on a fixed active set and a conduct factor common across firms—as under competition or
joint-profit maximization—Porter’s cost specification implies output shares that are constant over time
and invariant to changes in conduct; the formula does not generally apply under Cournot conduct, where
θirt =q irt/Qrt varies across firms:
qirt
Qrt
= a1/(1−ν) ir P
j∈Nrt a1/(1−ν) jr .
Under the marginal-cost specification in (2), and using the capacity-proportional allocationq irt/Qrt =
sirt/Srt, the corresponding aggregate condition is
Prt

1 + θrt
α1

=
X
i∈Nrt
sirt
Srt

crt +γ 1
qirt
sirt

=c rt +γ 1
Qrt
Srt
.
Whenθ rt = 0, this condition coincides with the competitive supply equation in the main model. A conduct
interpretation of collusive periods would additionally require conferences to choose total quantity under
a specified static game. The implied markup,θ rtPrt/(−α1), varies with price; the main model instead
represents the observed collusive price as competitive marginal cost plus an additive regime-specific wedge.
I use the wedge specification for four reasons. First, fixed liner schedules limit conferences’ ability to
adjust service quantity to a static joint-profit target. Second, conferences used prices to compete with
non-conference carriers, whose prices are unobserved and whose strategic interaction lies outside the model.
Third, capacity, entry, exit, and investment changed substantially over the sample, making a stable conduct
index and time-invariant member output shares restrictive. The capacity terms irt instead links current
marginal cost directly to the dynamic investment state. Finally, the short route-year panel does not support
a flexible time-varying conduct parameter (Matsumura and Otani 2023a,b, Otani and Matsumura 2025).
Following Igami (2015), I recover marginal cost from a competitive regime and measure collusive markups as
the difference between observed collusive prices and recovered competitive marginal cost, without specifying
the cartel’s static game.
50

D.2 Dynamic State, Payoffs, and Timing
This subsection provides the full setup summarized in Section 3.3. Let ˜s imt ∈R + denote firmi’s actual
tonnage in marketmand yeart. The capacity state used in estimation is
simt =



1 if ˜s imt <exp(8.5),
2 if exp(8.5)≤˜s imt <exp(9.5),
3 if exp(9.5)≤˜s imt <exp(10.5),
4 if exp(10.5)≤˜s imt.
Potential entrants have the null states imt = 0. The market state is
smt =

N 1 mt, N2 mt, N3 mt, N4 mt  , N l mt = X
i∈Nmt
1(simt =l),
andN l mt denotes the set of level-lincumbents. The model has four potential entrants in each market-year,
except in Asia–Europe, where it has five to accommodate the maximum number of entries observed in a
year.
The action-specific private payoff shocks are
εimt =



(εa imt)a∈A(simt) ifi∈ Nmt,
(εa imt)a∈A(0) ifi∈ Npe mt.
The components are private information and are independently distributed type-I extreme-value shocks
across actions, firms, and periods. Thus, each firm observes (t, s imt, smt, Dmt, εimt) at its turn, whereas the
researcher observes all components exceptε imt.
For an incumbent or potential entrant, the individual capacity transition is
simt+1 =



0 ifs imt ∈ {1,2,3,4}, aimt =x,
simt ifs imt ∈ {1,2,3,4}, aimt =k,
simt + 1 ifs imt ∈ {1,2,3}, aimt =b,
1 ifs imt = 0, aimt =e,
0 ifs imt = 0, aimt =x.
The build action is unavailable to level-4 firms. Entry therefore begins at level 1, and the induced market-
51

state transitions are
N 1 mt+1 =N 1 mt + X
i∈N pe mt
1(aimt =e)−
X
i∈N 1 mt
1(aimt =b)−
X
i∈N 1 mt
1(aimt =x),
N 2 mt+1 =N 2 mt + X
i∈N 1 mt
1(aimt =b)−
X
i∈N 2 mt
1(aimt =b)−
X
i∈N 2 mt
1(aimt =x),
N 3 mt+1 =N 3 mt + X
i∈N 2 mt
1(aimt =b)−
X
i∈N 3 mt
1(aimt =b)−
X
i∈N 3 mt
1(aimt =x),
N 4 mt+1 =N 4 mt + X
i∈N 3 mt
1(aimt =b)−
X
i∈N 4 mt
1(aimt =x).
The demand stateD mt follows the path estimated in the static model. The econometric residualsζ rt andη rt
from the static estimation do not enter the dynamic state or payoff function;ε imt contains the only private
shocks in the dynamic game. Because these shocks are i.i.d., the model satisfies conditional independence:
conditional on the current public state and action, next period’s capacity does not depend on the current
private shock (Rust 1987).
For incumbenti∈ Nmt and actiona∈ A(simt), the action-specific per-period payoff is
πa imt(simt, smt, Dmt, εa imt) =π imt(simt, smt, Dmt)−ψ1(a=x)
−ϕ1(a=k)−[ϕ+I(s imt;ι 1, ι2)] 1(a=b) +ε a imt.
Thus, the current static profit is common to all incumbent choices. For potential entranti∈ N pe mt and action
a∈ Ape,
πa imt(simt, smt, Dmt, εa imt) =−κ e1(a=e) +ε a imt.
The within-year game proceeds as follows. Static market outcomes first determine the profits of all current
incumbents. Level-4 incumbents then draw their private payoff shocks and move simultaneously. Level-3,
level-2, and level-1 incumbents move in that order; each group observes the actions of earlier groups, draws
its shocks, and moves simultaneously. Potential entrants move last after observing all incumbent actions.
The capacity and market states are then updated. This deterministic order follows Igami (2017); annual
data do not reveal the shorter-period stochastic order used by Igami and Uetake (2020). At the terminal
date,
VimT (simT , smT , DmT ) = πimT (simT , smT , DmT ) 1−β ,
whereπ imT is evaluated under firms’ belief that the 1980–1983 regime continues.
52

D.3 Dynamic Optimization and Equilibrium Details
This subsection expands the dynamic programming problem in Section 3.3.1. For incumbents at levels
l∈ {1,2,3}, the choice-specific values are
¯V x imt =π imt(l, smt, Dmt)−ψ+ε x imt,
¯V k imt =π imt(l, smt, Dmt)−ϕ+ε k imt +βE[V imt+1(l, smt+1, Dmt+1)|l, s mt, aimt =k],
¯V b imt =π imt(l, smt, Dmt)−ϕ−I(l;ι 1, ι2) +ε b imt +βE[V imt+1(l+ 1, smt+1, Dmt+1)|l, s mt, aimt =b].
Level-4 incumbents have the first two values but no build option. For a potential entrant,
¯V x imt =ε x imt,
¯V e imt =−κ e +ε e imt +βE[V imt+1(1, smt+1, Dmt+1)|0, s mt, aimt =e].
All values condition on the actions of groups that have already moved and integrate over the strategies and
private shocks of later movers. This conditioning is suppressed in the notation.
To expand the expectation in equation (6), leth imt collect the actions observed before firmimoves,
letg(s imt, aimt) denote its deterministic capacity transition, and letP m(· |simt, smt, himt, aimt) denote the
induced transition probability for the market state. Conditional independence gives
E[Vimt+1(simt+1, smt+1, Dmt+1)|s imt, smt, himt, aimt]
=
X
smt+1
Pm(smt+1 |s imt, smt, himt, aimt)Vimt+1(g(simt, aimt), smt+1, Dmt+1).
For example, a level-4 incumbent that continues hasg(4, k) = 4, so the expression reduces to
X
smt+1
Pm(smt+1 |s imt = 4, smt, himt, aimt =k)V imt+1(4, smt+1, Dmt+1).
The generic integrated value in equation (7) specializes to sums over (x, k, b) for levels 1–3, (x, k) for level
4, and (x, e) for potential entrants. Under type symmetry, let eV a lmt denote the common deterministic choice-
specific value for a level-lincumbent and eV a 0mt the corresponding value for a potential entrant. Equation (8)
then implies
pa lmt ≡Pr(a imt =a|s imt =l, smt, Dmt) = exp( eV a lmt/σ)P
a′∈A(l) exp( eV a′ lmt/σ) , a∈ A(l),
pa 0mt ≡Pr(a imt =a|s imt = 0, smt, Dmt) = exp( eV a 0mt/σ)P
a′∈{x,e} exp( eV a′ 0mt/σ) , a∈ {x, e}.
Type symmetry makes these probabilities independent of firm identity within a capacity level.
I next construct the market-state transition from these CCPs. Let (X l mt, Kl mt, Bl mt) be the numbers
of level-lincumbents that exit, continue, and build, respectively, withN l mt =X l mt +K l mt +B l mt and
B4 mt = 0. Let (O pe mt, Epe mt) be the numbers of potential entrants that stay out and enter. WriteX= (X l mt)4 l=1,
K= (K l mt)4 l=1, andB= (B l mt)4 l=1. Each probability below is a sequential conditional probability evaluated
at the realized actions of groups that moved earlier; the corresponding histories are suppressed. Conditional
53

on the public state, type symmetry implies the multinomial probabilities
Plmt(X l mt, Kl mt, Bl mt |s mt) = N l mt! X l mt!K l mt!Bl mt! [px lmt]X l mt [pk lmt]Kl mt [pb lmt]Bl mt ,
P0mt(Ope mt, Epe mt |s mt) = N pe mt! Ope mt!Epe mt! [px 0mt]Ope mt [pe 0mt]Epe mt .
The first expression applies tol∈ {1,2,3}; for level 4 it is the corresponding binomial over (x, k). The
realized action counts map into the next state according to
Ψ(smt, X, K, B, Ope, Epe) =  K 1 mt +E pe mt, K2 mt +B 1 mt, K3 mt +B 2 mt, K4 mt +B 3 mt  .
Therefore,
Pm(smt+1 |s mt) =
X
(X,K,B,O pe,Epe): Ψ(·)=smt+1
P0mt(Ope mt, Epe mt |s mt)
4Y
l=1
Plmt(X l mt, Kl mt, Bl mt |s mt).
At each within-year turn, actions already observed are held fixed and the sum is taken only over firms that
have not yet moved. When computing firmi’s continuation value, its own state and chosen action are also
held fixed, which givesP m(smt+1 |s imt, smt, himt, aimt) above.
Formally, a strategy maps the public state, a firm’s private shocks, and earlier movers’ actions to a
feasible action. A perfect Bayesian equilibrium requires sequential optimality at every information set and
beliefs consistent with these strategies and Bayes’ rule. Type symmetry restricts firms at the same capacity
level to use the same strategy. As in Igami (2017), private shocks affect rivals only through observed choices,
capacity types move sequentially, and the finite horizon permits recursive solution by backward induction.
Continuous private shocks make ties occur with probability zero.
D.4 Welfare Measurement
This subsection defines the welfare measures used in Tables 7–9 and Figures 9–10. Given the estimated
demand elasticitybα1 <−1, consumer surplus, producer surplus, and social welfare in marketmand yeart
are
CS mt =
X
r∈Rm
P ∗ rtQ∗ rt
|1 +bα1| ,(12)
P Smt =
X
i∈Nmt
πimt,(13)
SWmt =CS mt +P Smt.(14)
54

LetN mt = P4 l=1 N l mt andX mt = P4 l=1 X l mt denote the numbers of current and exiting incumbents. Define
operating costs, exit costs, and entry and shipbuilding costs, respectively, as
F Cmt =ϕ(N mt −X mt),(15)
XC mt =ψX mt,(16)
SCmt =κ eEpe mt +
3X
l=1
I(l;ι 1, ι2)Bl mt.(17)
Thus, continuing and building incumbents pay the operating cost, exiting incumbents pay the exit cost,
entrants pay the entry cost, and builders pay the capacity-expansion cost. Net social welfare is
NetSWmt =SW mt −F Cmt −XC mt −SC mt.(18)
This calculation treats the estimated operating, exit, entry, and shipbuilding payoff costs dollar for dollar as
real resource costs. This is a maintained accounting assumption: because these parameters are reduced-form
private costs, any components reflecting transfers, financing premia, or other private wedges would not be
social resource costs. I therefore reportCS+P Sseparately and interpret net social welfare as conditional on
the resource-cost assumption and the logit-scale normalization. For any reported set of yearsT, the present
value of measureZ mt is
P VT (Zm) =
X
t∈T
βt−1973Zmt.(19)
The counterfactual tables and figures useT={1973, . . . ,1983}; Table 7 also reports the two conference
subperiods separately.
D.5 Capacity, Revenue, Total Cost, and Profit
This subsection gives comparative-static intuition for how a change in firm capacity affects static profit. I
hold rivals’ capacities fixed and treat own capacity as continuous, although capacity choices are discrete in
the dynamic model.
In equation (5), firmion routerin yearthas static profit
πirt(sirt, srt, Drt) =P ∗ rt(srt, Drt)qirt| {z }
=Revenue
−
Z qirt
0
mcirt(q, sirt)dq
| {z }
=Total cost
,
s.t.q irt =



Q∗ rt(srt, Drt)ωirt ift≤1983
P ∗ rt(srt,Drt)−crt
γ1 sirt otherwise,
ωirt ∈[0,1],∀i,
NrtX
i=1
ωirt = 1.
For compactness, writeP=P ∗ rt(srt, Drt),Q=Q ∗ rt(srt, Drt),q i =q irt, ands i =s irt. The revenue
derivative is
∂(P qi)
∂si
=q i
∂P
∂si
+P ∂qi
∂si
.
55

The quantity response depends on the regime:
∂qi
∂si
=ω irt
∂Q
∂si
+Q ∂ωirt
∂si
, t≤1983,
∂qi
∂si
= si
γ1
∂P
∂si
+ P−c rt
γ1
, t≥1984.
Total cost isT Ci =c rtqi +γ 1q2 i /(2si). Because equilibrium quantity also changes with capacity, its derivative
is
∂T Ci
∂si
=

crt +γ 1
qi
si
 ∂qi
∂si
−γ 1
q2 i
2s2 i .
Hence,
∂πirt
∂si
=q i
∂P
∂si
+ [P−mc irt(qi, si)] ∂qi ∂si +γ 1 q2 i 2s2 i .
The sign is not determined analytically because price, total quantity, and the quota all respond to capacity.
I therefore evaluate these responses at the numerical equilibrium. Figure 12 reports equilibrium profits
conditional on the observed states; static profit increases with capacity in all three markets.
(a) Transpacificπ imt
 (b) Transatlanticπ imt
 (c) Asia–Europeπ imt
Figure 12: Estimated static profits by capacity level and market
Note: Each series reports estimated static profit at a discrete capacity level, conditional on the observed market states. Level
1 is the smallest capacity state and level 4 is the largest.
E Additional Estimation Results
E.1 Route-Specific Conference Freight-Rate Trends
This subsection documents the timing of the price decline around the 1980 and 1984 empirical regime
boundaries. The exercise is descriptive: it does not by itself separate changes in conference conduct from
changes in costs, demand, or capacity. Figure 13 plots year coefficients from regressions of log conference
freight rates on year and route fixed effects, normalized to 1979. On the U.S.-related routes, rates were
close to their 1979 level throughout the 1970s, fell from 1980 through 1983, and remained lower after 1984.
Asia–Europe rates had already declined before 1980 and then dropped sharply in 1983; they also remained
well below their 1979 level after 1984.
56

Figure 13: Log conference freight rates relative to 1979
Note: Each panel reports year coefficients from a regression of log conference freight rates on year and route fixed effects,
normalized to 1979. The sample covers 1973–1990; dashed lines mark the common empirical regime boundary in 1980 and the
Shipping Act of 1984. In the first two panels, error bars are 95% confidence intervals based on route-clustered standard errors.
Because the eastbound and westbound Asia–Europe rates are obtained in part by applying proportional conversion factors to
the same raw-data series, they provide effectively one independent price series. The third panel therefore shows an illustrative
reference band obtained by applying the year-specific standard errors from the four U.S.-related routes to the Asia–Europe
coefficients; it is not an estimated confidence interval for those routes.
E.2 Fit of the Main Models
Panels (a) and (b) of Figure 14 compare fitted route-year prices and quantities with the data. The fitted
series reproduce the broad regime shifts and trends but are smoother than the data. Table 11 evaluates the
supply-side fit by market and regime. The ratio of the fitted mean price to the observed mean price ranges
from 0.812 to 1.115.
(a)P rt: Estimated (solid) and data (dotted)
 (b)Q rt: Estimated (solid) and data (dotted)
Figure 14: Fitted and observed route-year prices and quantities
57

Table 11: Fit of shipping prices by regime
Regime Market (1) Mean ˆPrt (2) MeanP rt (1)/(2)
1973-1979 Asia and Eur 3975.553 4172.739 0.953
Transatlantic 3111.218 2791.502 1.115
Transpacific 3687.998 3810.528 0.968
1980-1983 Asia and Eur 2710.169 2625.379 1.032
Transatlantic 1926.517 2047.711 0.941
Transpacific 2760.922 2724.519 1.013
1984-1990 Asia and Eur 1821.684 1672.949 1.089
Transatlantic 1081.437 1331.900 0.812
Transpacific 2399.493 2297.765 1.044
Note: Each row pools the two directed-route observations within a market and regime. Fitted route-year prices are calculated
from the estimates in Table 5.
E.3 Specification Sensitivity and Instrument Selection for Demand and Cost
This subsection documents sensitivity to the demand instruments and cost shifters used in Section 5. I
explored a broad grid of demand and cost specifications and then compared economically admissible spec-
ifications by their alignment with the model, first-stage relevance, and overidentification diagnostics where
available. Model admissibility requiresα 1 <−1 for finite consumer surplus under constant-elasticity demand
andγ 1 >0 for upward-sloping supply. Because the reported specification was selected from the same 108
observations using these criteria, the coefficientp-values and confidence sets are conditional on specification
selection and are not selection-adjusted. The comparisons below should therefore be read as sensitivity
analysis rather than independent confirmation of the preferred estimates. Tables 12 and 13 report the main
candidates for the common 1973–1990 sample.
On the demand side, column (1) instruments log(P rt) with average ship age and the contemporaneous
share of tonnage over 20 years old; it yields ˆα 1 =−0.842. The preferred specification in column (2) uses
average ship age and the share of tonnage over 15 years old. It yields ˆα1 =−1.111 and a route-clustered first-
stage F of 19.0. Both instruments are contemporaneous functions of the fleet state, which is determined by
past entry and shipbuilding decisions and is therefore predetermined with respect to the current i.i.d. demand
shock; the lagged variant in column (3) gives a nearly identical ˆα1 =−1.095. Columns (4) and (5) show that
each instrument alone is either too weak or yields an imprecise inelastic estimate. The instruments derive
most of their power from the low-frequency aging of the fleet; the elasticity estimated from the detrended,
within-route variation alone is−0.93, close to the preferred estimate, although the detrended instruments
are weak. No examined specification deliversα 1 significantly below−1: the preferred estimate is statistically
different from zero but not from unit elasticity. In leave-one-route-out estimates, ˆα 1 ranges from−1.211 to
−0.482; omitting the Europe-to-Asia route produces the upper endpoint. Thus, the sign is stable but the
classification as elastic is sensitive to individual routes.
On the cost side, the preferred specification in column (1) includes average ship size and the share of
tonnage over 20 years old as fleet-technology cost shifters and yields ˆγ1 = 597. Its route-clustered first-stage
F is 8.5, below the conventional threshold of ten, although its Anderson–Rubin 95% confidence set is bounded
and positive. Columns (2)–(5) vary the age threshold and, in columns (4) and (5), omit average ship size;
the supply slope is positive in columns (1)–(4) but negative in column (5), and the first-stage F ranges from
2.5 to 8.5. The 1973–1979 wedge is positive across the reported specifications, whereas the 1980–1983 wedge
58

is more sensitive to the treatment of fleet variables. Across leave-one-route-out estimates, ˆγ 1 ranges from
337 to 1,115, the pre-1980 wedge from$1,385 to$1,975, and the 1980–1983 wedge from$596 to$1,220.
Table 12: Demand specifications and instrument choice
(1) (2) (3) (4) (5)
log(Prt):α 1 -0.842*** -1.111*** -1.095*** -0.691 -4.893
(0.274) (0.354) (0.339) (0.476) (23.917)
log GDP 0.419** 0.410* 0.411* 0.425** 0.279
(0.197) (0.217) (0.216) (0.190) (0.634)
1(t≤1979) 0.369** 0.552* 0.541** 0.266 3.129
(0.158) (0.304) (0.268) (0.287) (16.297)
1(1980≤t≤1983) 0.080** 0.168 0.162* 0.030 1.405
(0.039) (0.111) (0.090) (0.153) (7.812)
Num.Obs. 108 108 108 108 108
R2 Adj. 0.850 0.804 0.807 0.869 -1.173
IV: mean ship age X X X X
IV: share of tonnage>20yo X
IV: share of tonnage>15yo X
IV: lag share of tonnage>15yo X X
First-stage F 36.6 19.0 25.0 8.3 0.1
Note: The sample covers six routes in 1973–1990. All columns include the demand shifters of Table 4 and vary only the excluded
instruments; standard errors in parentheses are clustered at the route level. The rows “IV” indicate the excluded instruments
for log(P rt). The first-stage F statistics are route-clustered Wald statistics. Column (2) is the preferred specification used in
Table 4. Significance levels are denoted by ∗p <0.1, ∗∗p <0.05, and ∗∗∗p <0.01.
E.4 Robustness of the Dynamic Estimates to Anticipating the Cartel Break-
down
The benchmark model assumes that firms do not anticipate the 1984 cartel breakdown, so the terminal
ex-ante valueV imT =π imT /(1−β) uses the 1984 profits evaluated under the belief that the 1980–1983 con-
ference regime continues. As a robustness check, I re-estimate the dynamic parameters under the alternative
assumption that firms perfectly foresaw the breakdown: the terminal value uses realized competitive profits
in 1984, so backward induction incorporates the end of the cartel into every pre-1984 decision. Table 14
reports the results. Entry costs fall by 0.9–3.2% across markets. Exit and operating costs remain similar in
magnitude, with the largest proportional movement being a 27% rise in the imprecisely estimated transpa-
cific exit cost. The identified investment costs fall by 2.1–6.0%, and every perfect-foresight cost estimate
lies within its benchmark likelihood-slice range. The stability of the estimates is an empirical robustness
result rather than an exact logit-invariance result: the terminal-value change enters continuation, build, and
entry values but not exit or stay-out values, so it can affect the corresponding odds, and under the capacity-
proportional allocation the change need not be uniform across capacity levels. With the moderate continuing
1980–1983 wedge (˜γ2 = $998 per TEU), the re-estimated costs remain within the benchmark likelihood-slice
ranges. The no-anticipation assumption is therefore maintained because the timing and effectiveness of the
breakdown were uncertain before 1984; the robustness exercise suggests that this terminal-value assumption
is not driving the estimated dynamic costs.
59

Table 13: Cost specifications and instrument choice
(1) (2) (3) (4) (5)
Qrt/Srt:γ 1 596.922* 103.019 901.129* 433.584** -234.438
(327.028) (129.756) (514.259) (195.173) (639.550)
share of tonnage>10yo -1976.313** -1697.562**
(913.555) (778.658)
share of tonnage>20yo -1491.488 1424.614
(2927.073) (3464.868)
share of tonnage>15yo 990.437
(1481.399)
mean ship size (1,000 TEU) 1817.274 2226.129 1209.211
(1827.054) (2016.352) (1465.583)
1(t≥1974) 113.941 3.965 202.355 48.200 -130.107
(320.233) (160.761) (446.873) (296.061) (266.190)
1(t≤1979): ˜γ 1 1807.343*** 1229.007*** 1891.642*** 1743.573*** 1187.760***
(411.167) (309.217) (475.685) (386.512) (333.911)
1(1980≤t≤1983): ˜γ 2 997.543*** 588.864*** 1192.165** 823.640*** 315.925
(368.733) (210.387) (512.491) (244.032) (245.232)
Num.Obs. 108 108 108 108 108
R2 Adj. 0.714 0.800 0.630 0.732 0.769
First-stage F 8.5 7.5 4.3 3.9 2.5
Note: The sample covers six routes in 1973–1990. All columns include the regime dummies and route fixed effects and instrument
Qrt/Srt with log GDP; standard errors in parentheses are clustered at the route level. The columns vary the cost shifters as
indicated by the coefficient rows. Column (1) is the preferred specification used in Table 5. Significance levels are denoted by
∗p <0.1, ∗∗p <0.05, and ∗∗∗p <0.01.
Table 14: Dynamic parameters under perfect foresight of the 1984 breakdown
Parameter Transpacific Transatlantic Asia–Europe
Entry cost:κ e 4.018 2.91 3.804
[3.575,4.515] [2.382,3.554] [3.385,4.275]
Exit cost:ψ0.85 3.419 2.843
[0.07,1.29] [2.799,4.176] [1.56,4.241]
Operation cost:ϕ0.224 0.505 0.052
[0.097,0.339] [0.413,0.617] [0.004,0.181]
Investment cost:ι 1 3.211 3.572 3.709
[2.696,3.825] [2.925,4.363] [3.3,4.168]
Investment cost:ι 2 Not identified 9.185 3.913
[7.71,10.942] [2.623,5.837]
Logit scale:σ(normalized) 1.000 1.000 1.000
Log Likelihood -67.652 -53.796 -67.571
Note: Each market aggregates its eastbound and westbound routes. The terminal value uses realized competitive profits in 1984
instead of the regime-continuation beliefs of the benchmark model. Brackets report conditional likelihood-slice ranges based
on the same 90% chi-squared cutoff as in Table 6. As in Table 6, no level-3-to-4 investment is observed during the 1973–1983
transpacific estimation sample, soι 2 is not finitely identified there. Cost parameters are measured in billions of U.S. dollars,
and the logit scaleσis normalized to one.
60

References for the Appendix
Bresnahan, T. F.(1982). The oligopoly solution concept is identified.Economics Letters,10(1-2), 87–92.
Clyde, P. S.andReitzes, J. D.(1998). Market power and collusion in the ocean shipping industry: is a
bigger cartel a better cartel?Economic Inquiry,36(2), 292–304.
Department of Transportation, the United States(1992).Report to the President and the Congress
of the Advisory Commission on Conferences in Ocean Shipping. DIANE Publishing.
Federal Maritime Commission(1975). Federal maritime commission reports, volume 16. Decisions from
July 1972 through June 1973.
Federal Maritime Commission(1980).19th Annual Report for Fiscal Year 1980. Tech. rep., Federal
Maritime Commission, Washington, DC.
Federal Maritime Commission(1985).Annual Report of the Federal Maritime Commission for Fiscal
Year 1985. Tech. rep., Federal Maritime Commission, Washington, DC.
Fox, N. R.(1992). An empirical analysis of ocean liner shipping.International Journal of Transport Eco-
nomics/Rivista internazionale di economia dei trasporti, pp. 205–225.
Fusillo, M.(2003). Excess capacity and entry deterrence: the case of ocean liner shipping markets.Mar-
itime Economics & Logistics,5(2), 100–115.
Gilpin, K. N.(1983). Hellenic lines in chapter 11.New York Times.
Harrington, J. E.,H ¨uschelrath, K.andLaitenberger, U.(2018). Rent sharing to control noncartel
supply in the German cement market.Journal of Economics & Management Strategy,27(1), 149–166.
Igami, M.(2015). Market power in international commodity trade: The case of coffee.The Journal of
Industrial Economics,63(2), 225–248.
—(2017). Estimating the innovator’s dilemma: Structural analysis of creative destruction in the hard disk
drive industry, 1981–1998.Journal of Political Economy,125(3), 798–847.
—(2018). Industry dynamics of offshoring: The case of hard disk drives.American Economic Journal:
Microeconomics,10(1), 67–101.
—andUetake, K.(2020). Mergers, innovation, and entry-exit dynamics: Consolidation of the hard disk
drive industry, 1996–2016.The Review of Economic Studies,87(6), 2672–2702.
Japan Maritime Center(2008).Report on Inter-Carrier Agreements in Oceangoing Shipping Industry
(Gaikokaiun Ni Okeru Senshakan Kyotei Ni Kakaru Chosa Hokokusho). Japan Maritime Center, accessed:
2022-03-12.
Kasahara, H.andShimotsu, K.(2012). Sequential estimation of structural models with a fixed point
constraint.Econometrica,80(5), 2303–2319.
Marin, P. L.andSicotte, R.(2003). Exclusive contracts and market power: evidence from ocean shipping.
The Journal of Industrial Economics,51(2), 193–214.
61

Maritime Industry Research Institute(2004).Market Structure and Competition Policy in Shipping
(Kaiun ni okeru Sijou Kouzou to Kyousou Seisaku). Maritime Industry Research Institute, accessed:
2021-09-22.
Marshall, R. C.andMarx, L. M.(2014).The economics of collusion: Cartels and bidding rings. Mit
Press.
Matsumura, Y.andOtani, S.(2023a). Challenges in statistically rejecting the perfect competition hy-
pothesis using imperfect competition data.arXiv preprint arXiv:2310.04576.
—and—(2023b). Resolving the conflict on conduct parameter estimation in homogeneous goods markets
between Bresnahan (1982) and Perloff and Shen (2012).Economics Letters,229, 111193.
Morton, F. S.(1997). Entry and predation: British shipping cartels 1879–1929.Journal of Economics &
Management Strategy,6(4), 679–724.
Otani, S.(2021). Estimating endogenous coalitional mergers: Merger costs and assortativeness of size and
specialization.arXiv preprint arXiv:2108.12744.
—andMatsuda, T.(2023). Unified container shipping industry data from 1966: Freight rate, shipping
quantity, newbuilding, secondhand, and scrap price.Transportation Research Part E: Logistics and Trans-
portation Review,176, 103186.
—and—(2025). Unified merger list in the container shipping industry from 1966 to 2022: A structural
estimation of M&A matching.Transport Policy,165, 58–69.
—andMatsumura, Y.(2025). Conduct parameter estimation in homogeneous goods markets with equilib-
rium existence and uniqueness conditions: The case of log-linear specification.Economics Bulletin,45(4),
1755–1761.
Pace, E.(1981). Company news; farrell lines profitable again.New York Times.
Podolny, J. M.andMorton, S. F. M.(1999). Social status, entry and predation: The case of british
shipping cartels 1879–1929.The Journal of Industrial Economics,47(1), 41–67.
Porter, R. H.(1983). A study of cartel stability: The joint executive committee, 1880-1886.The Bell
Journal of Economics, pp. 301–314.
Rust, J.(1987). Optimal replacement of gmc bus engines: An empirical model of harold zurcher.Econo-
metrica,55(5), 999–1033.
United Nations(1974). Convention on a code of conduct for liner conferences. United Nations Treaty
Series, vol. 1334, p. 15, No. 22380.
United States Congress(1916). Shipping act, 1916. Public Law 64-260, 39 Stat. 728.
United States Congress(1984). Shipping act of 1984. Public Law 98-237, 98 Stat. 67.
V an Ham, H.,van Ham, J.andRijsenbrij, J.(2012).Development of containerization: Success through
vision, drive and technology. Ios Press.
62

Wilson, W. W.andCasavant, K. L.(1991). Some market power implications of the shipping act of 1984:
a case study of the us to pacific rim transportation markets.Western Journal of Agricultural Economics,
pp. 427–434.
63
