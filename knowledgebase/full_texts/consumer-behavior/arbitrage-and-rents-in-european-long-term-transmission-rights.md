---
title: Arbitrage and rents in European long-term transmission rights
url: https://arxiv.org/abs/2607.28790
category: consumer-behavior
subcategory: empirical
date: 2026-07
venue: ''
authors:
- Clemens Stiewe
source: arxiv
pdf_url: https://arxiv.org/pdf/2607.28790
pages: 27
chars: 58968
fetched_at: '2026-11-08T13:02:06+00:00'
kb_version: 1
---

# Arbitrage and rents in European long-term transmission rights

Arbitrage and rents in European long-term transmission
rights
Clemens Stiewe∗
Centre for Sustainability, Hertie School, Berlin
July 30, 2026
Abstract
Long-term transmission rights (LTTRs) are designed to support hedging in inter-
connected European electricity markets. LTTR auction prices have historically fallen
short of forward market prices, signaling limited arbitrage. This paper studies the
interaction of transmission rights and forward markets. Option pricing theory predicts
that LTTR holders take short forward positions in importing markets and long for-
ward positions in exporting markets to lock in arbitrage profits. Empirically, I find a
corresponding price effect in the German electricity forward market immediately after
LTTR auctions, using panel regression on EEX futures contracts traded between 2018
and 2025. This shows that LTTR holders can achieve systematic rents, indicating an
inefficient regulatory intervention and a transfer from consumers to LTTR holders.
Keywords:Forward markets, option pricing, electricity, transmission rights
JEL Codes:G13, F15, Q41, C23
∗Corresponding author: clemens.stiewe@gmail.com
arXiv:2607.28790v1  [econ.GN]  30 Jul 2026

1 Introduction
Electricity spot market prices are volatile because electricity cannot yet be stored economi-
cally. Forward markets therefore provide insurance against spot price volatility for generators
(i.e., spot market sellers) and retailers (i.e., spot market buyers). Forward market liquidity
is a concern in many European countries, however. Liquidity concentrates on the German
forward market, which has substantially higher traded volume and lower bid-ask spreads
than neighboring markets (ACER, 2025). Austrian market participants, for example, might
thus prefer to hedge on the German forward market. While this offers lower transaction
costs, it also comes with “basis risk”: German futures are settled against the German spot
price index, so an Austrian generator selling forward in Germany is exposed not only to
Austrian but also to German spot prices. Whenever these spot prices diverge, the hedge
becomes incomplete.
Transmission system operators (TSOs) are therefore required to issue long-term transmis-
sion rights (LTTRs) for market borders with substantial liquidity gaps (European Commis-
sion, 2016). LTTRs are financial transmission rights (FTRs) and resemble European-style
call options on the hourly spot price spread between two neighboring electricity markets dur-
ing the delivery period. LTTRs are issued for most physical market borders and directions
as monthly and annual products. 1
Regulators have acknowledged several design shortcomings that limit the attractiveness
of LTTRs as a hedging instrument for generators and retailers, such as the short maximum
maturity of one year, the lack of a secondary market, and incomplete financial firmness 2
(ACER, 2025). Because of these shortcomings, regulators assume that substantial volumes
of LTTRs are bought by financial traders rather than by physical hedgers (ACER, 2023;
European Commission, 2024). LTTR auction prices fall systematically short of forward
market prices (ACER, 2024), which likely reflects that financial traders, who have a lower
willingness to pay than physical hedgers, tend to be the marginal, price-setting bidders in
LTTR auctions. For inframarginal participants with higher willingness to pay, the under-
pricing of LTTRs relative to forward markets represents an arbitrage opportunity. Using
panel regression on German and Austrian forward contracts traded between 2018 and 2025,
I show that market participants exploit this opportunity by selling the forward spread im-
mediately after buying LTTRs, hence locking in profits. Arbitrage across LTTR and forward
markets is limited because of transaction costs and inelastic LTTR supply, which explains
1Pay-as-clear auctions take place every month and year shortly before the delivery period begins, e.g.,
from 24 November 2024 until 2 December 2024 for an annual 2025 LTTR. Auction results are published
right after the end of the auction window.
2Reduced firmness means that holders face reduced payouts during force majeure events.
1

why mispricing can persist. The rents earned by LTTR holders are financed from congestion
income that would otherwise reduce transmission tariffs (European Parliament and Council
of the European Union, 2019). This study hence provides empirical support for regulators’
concerns about a transfer from consumers to LTTR holders (ACER, 2023). More generally,
it studies the interaction of transmission rights with related derivatives markets.
This paper is organized as follows: Section 2 reviews the literature on forward market
price formation and transmission rights, Section 3 derives the expected effects on forward
markets, and Section 4 discusses the empirical strategy. Section 5 and Section 6 present and
discuss the results, while Section 7 concludes.
2 Research background
This section first reviews the relevant literature on electricity forward markets, focusing on
how price formation is shaped by the hedging pressures of retailers and generators. Con-
trolling for the effects of physical participants’ hedging needs then allows me to empirically
isolate the forward market effect of LTTR arbitrage.
Forward prices for most commodities can be explained by storage costs (Kaldor, 1939).
Since electricity cannot be stored economically for longer periods, however, theories of storage
cannot explain electricity forward prices. The empirical literature on electricity forward
prices therefore mostly builds on theories that involve “hedging pressures” of buyers and
sellers. The concept dates back to Keynes (1930), who postulated that whenever there are
more sellers than buyers on the forward market, speculators take over the price risk from
sellers in exchange for a premium, resulting in “normal backwardation”, i.e., forward prices
that are below expected spot prices. This difference between forward and expected spot
prices for the same delivery period has also been referred to as the forward (or forward risk)
premium.3
The equilibrium model of Bessembinder and Lemmon (2002) has been an influential
extension of the hedging pressure theory to electricity forward markets. They show that
the size and the sign of the forward premium are affected by the skewness and variance of
expected spot prices, which are fundamentally determined by the level of electricity demand.
When expected spot prices are positively skewed and electricity demand is high, retailers face
the risk of spot price spikes, which increases their hedging pressure and induces a positive
3Forward premiums can also emerge when agents are risk-neutral but have market power. Building
on the seminal work by Allaz and Vila (1993), who introduce a model of Cournot competition on forward
markets, Ito and Reguant (2016) show that strategic behavior can induce a premium in sequential electricity
markets, and empirically confirm this for Spain. Borenstein et al. (2008) show that besides risk aversion,
market power drives forward premiums on the Californian electricity market.
2

forward premium. When expected demand and skewness of prices are low, the hedging
pressure of generators dominates, and a negative premium emerges. A higher variance of
spot prices means that generators face uncertain spot revenues, which increases their hedging
pressure and leads to a negative forward premium.
Electricity forward prices, and the forward premium, are also positively linked to the fuel
prices that electricity generators have to pay. Gas, coal, and carbon price risks therefore
affect not only the spot, but also the forward market price of electricity (Redl and Bunn,
2011; Bunn and Chen, 2013). Higher market shares of wind, solar, and hydro energy, on
the other hand, are associated with lower forward premiums (Huisman et al., 2021; Carnero
et al., 2025).
Because generators tend to hedge price risk at longer horizons than retailers, their net
hedging pressure varies with time to maturity (Benth et al., 2008). This notion is also
crucial for Fleten et al. (2015), who document an overnight risk premium in Nordic and
German/Austrian electricity futures that is positive prior to the front period of a forward
contract, when generators’ hedging pressure dominates, and smaller (or even negative) after
retailers enter the forward market in the front period once they know how much to sell to
end consumers. Pe˜ na and Rodr ´ ıguez (2022) argue that the forward premium in Fleten et al.
(2015) is mostly a liquidity premium that decreases in size as the number of market makers,
who provide liquidity to physical participants, increases towards maturity. I build on the
empirical framework of Fleten et al. as it allows me to control for hedging pressure effects,
isolating the effect of LTTR arbitrage after auctions. An effect of LTTR auctions on forward
prices is suggested by Hirth et al. (2024) in a consultancy report commissioned by German
TSOs, but has not been established empirically in the literature.
The literature on forward market price formation hence provides the foundation for my
identification strategy. A second relevant strand examines the design of FTRs, focusing
on US electricity markets. This literature provides empirical evidence that US markets for
transmission rights involve large transfers from consumers to financial traders but offers
different interpretations.
Opgrand et al. (2022) and Deng et al. (2010) find that FTR auction proceeds systemat-
ically fall short of their expected ex post value. Opgrand et al. show that physical hedgers
are willing to pay a positive risk premium in FTR auctions, while financial traders require a
negative trading premium for holding FTRs. This trading premium may contain transaction
costs, such as collateral requirements, and a risk premium. FTR underpricing is therefore
attributed to a larger share of speculative buyers in the auction. Deng et al. (2010), on the
other hand, attribute FTR underpricing to an inefficient auction mechanism. Longer-term
FTRs, which could be used by physical participants to support project finance, are sug-
3

gested as a remedy (Risanger and Mays, 2024). Petropoulos and Willems (2020) show that
FTRs increase dynamic efficiency by reducing premature investment by incumbent players,
but only if a secondary market for FTRs exists. Leslie (2021) empirically studies firm-level
positions of retailers, generators, and financial traders in transmission congestion contracts
(TCCs), the FTRs of New York’s NYISO market, and finds that retailers participate pri-
marily for hedging, while generators and traders earn profits from their TCC positions. This
suggests a transfer of wealth from network users to firms. However, Leslie cautions that
the net welfare effect of trader participation in TCC auctions on network users can be am-
biguous: trader participation improves price discovery and liquidity, which may ultimately
benefit network users through more efficient retail contracts or generation and transmis-
sion planning. The participation of financial players generally improves market efficiency,
for example through arbitrage (Jha and Wolak, 2013; Mercadal, 2022). Birge et al. (2018)
show, however, that financial participation needs to be accompanied by adequate market
design: when the regulator imposed higher transaction costs on financial participants in the
MISO market, thus limiting their arbitrage profits, financial players started to engage in the
profitable manipulation of FTR value instead.
Inefficiencies of transmission rights on single European borders have been documented
(McInerney and Bunn, 2013; Kristiansen, 2007), but the harmonized European LTTRs in-
troduced in 2016 have received little attention in the literature. Regulators have documented
underpricing of LTTRs, attributing it primarily to short maturities, infrequent auctions and
the lack of a secondary market, as well as incomplete financial firmness (ACER, 2024; Beato,
2021). A survey of market participants indicates that some of them prefer spread futures
over LTTRs for hedging basis risk (European Commission, 2024). ACER (2024) computes
the difference between cleared LTTR auction prices and contemporaneous EEX baseload
spread futures prices for the same delivery period, and finds that on most European borders,
the cross-border spread is priced lower in LTTR auctions than on EEX forward markets. A
systematically higher value for obligations (EEX futures) than for options (LTTRs) on the
same underlying is counterintuitive because spreads are usually volatile and can change sign
from hour to hour, which should make an option more valuable than an obligation (Hull,
2021). Reduced demand from physical hedgers, e.g., because of the non-firmness of LTTRs,
and a lower willingness to pay of financial traders, who purchase these transmission rights
instead, might explain LTTR undervaluation. In the following section, I show that LTTR
underpricing can be profitably exploited through arbitrage and derive the expected effects
of that strategy on forward markets.
This paper contributes to the literature by documenting the interaction of transmission
rights with related derivatives markets. It provides a first empirical assessment of the ef-
4

ficiency of European LTTRs and extends the empirical literature on forward market price
formation with an estimate of the effect of transmission rights auctions.
3 Expected forward market effects
Market participants holding LTTRs can exploit mispricing of spreads across LTTR and
forward markets by selling the baseload forward spread immediately after acquiring LTTRs.
In this section, I derive the expected effect of these forward positions.
The payoff of anA→BLTTR is defined as the monthly or annual sum of positive hourly
B−Aprice spreads (i.e., PH h=1 max  P B h −P A h ,0  for annual (H= 8760) or monthly (H=
730) LTTRs). Net profits Π at deliveryTin Euro/MWh from the combined long LTTR and
short forward position are given by:
ΠT = 1 H
HX
h=1
max

P B h −P A h ,0 
| {z }
LTTR payoff
+

Ft,T − 1 H
HX
h=1

P B h −P A h 
| {z }
forward payoff
−Lt,T −τ t (1)
where 1 H PH h=1  P B h −P A h  ≡S T is the average cross-border spot price spread during the
delivery period,F t,T is the forward spread price on LTTR auction daytfor delivery atT,
Lt,T is the auction price paid at timetfor delivery atT, andτ t are the transaction costs of
arbitrage priced into the auction bid at timetas part of a (negative) trading premium. The
LTTR payoff is expressed per MWh, i.e., divided byH.
Suppose a trader participates in the 2025 LTTR auction and bids today’sB−ACal-
2025 forward spread of 17 Euro/MWh minus a trading premium of 1 Euro/MWh (i.e.,
16 Euro/MWh) for one megawatt (MW) ofA→BLTTR. Assume for simplicity that the
trading premium contains only the transaction costs of arbitrage. On the next day, the
auction clears at 15 Euro/MWh because the marginal bidder has priced in transaction costs
of 2 Euro/MWh. TheB−Aforward spread still trades at 17 Euro/MWh. To capture the gap
between the clearing price and the forward spread price, she sells theB−Aspread forward
(i.e., selling one MW forward inBand buying one MW forward inA) and holds both
positions until delivery. If the realized spread is positive during all hours of 2025, the LTTR
payoff in Equation 1 reduces toS T , and ΠT =S T + (Ft,T −S T )−L t,T −τ t =F t,T −L t,T −τ t =
17−15−1 = 1, leaving the trader with a 1 Euro/MWh profit. If the spread turns negative
in some hours, the LTTR does not pay off in those hours whileS T falls, such that the short
forward payoff increases. The trader’s payoff then equals 1 Euro/MWh plus an uncertain
upside from negative-spread hours.
5

This strategy is only profitable with LTTRs that export from low-price to high-price
zones: assuming that theB→ALTTR clears at a price of zero, selling theA−Bspread
forward at -17 Euro/MWh effectively means paying a large fixed amount (−17−0−1 =−18)
for a small optionality (because theA−Bspread may only turn positive during a few hours).
Buying the forward spread low and selling it high as an LTTR is not possible: without
a secondary market for LTTRs, TSOs are the only sellers of LTTRs. Market participants
can thus only lock in arbitrage profits if they can buy the cross-border spread low (in LTTR
auctions) and sell it higher (on forward markets). Arbitrage with LTTRs from low-price to
high-price markets implies selling forward in the high-price zone and buying forward in the
low-price zone. Assuming that traders hold equal volumes of LTTRs in both directions of
each border, their net forward positions should be short in high-price, importing and long
in low-price, exporting markets.
Transaction costsτ t include funding liquidity costs and market liquidity costs (Brunner-
meier and Pedersen, 2009). Spread volatility raises the risk of large and frequent margin calls,
forcing the trader to post variation margin. Funding liquidity costs are smaller if spreads
are stable and the trader can reliably hold the position to delivery. The directional effect
on forward markets should hence be strongest when cross-border spreads are stable. Market
liquidity costs are determined by bid-ask spreads, which are larger in illiquid markets.
Using the Bachelier option pricing model 4 (Bachelier, 1900), Figure 1 illustrates how
the expected aggregate effect of this strategy depends on the level and the volatility of the
cross-border spot price spread. Panel (a) plots the Bachelier option value for hypothetical
A→BandB→ALTTRs across a range ofB−Aspreads.
Panel (b) shows the net forward positions in marketsAandB. In the unrealistic case of a
perfectly stable spread (σ= 0), the LTTR only has intrinsic value and arbitrage transaction
costs are small. This makes it relatively more attractive for traders to lock in profits via
arbitrage. Volatility (σ >0) increases both option value and transaction costs, making it
relatively more attractive to keep the LTTR option on the books instead. For a given positive
volatility, a larger average positive spread means that negative-spread hours are less likely.
This reduces the uncertain upside from the combined LTTR/forward position and hence the
volatility of the trader’s portfolio.
Aggregate forward positions, which reflect the difference inA→BandB→Aoption deltas
from panel (a), and thus the effect on forward market prices, should therefore be strongest
when spreads are large and stable.
4The undiscounted Bachelier price of a call option on an underlying with forward priceF 0, option strike
priceK, time-to-maturityTand volatility of the underlyingσ N is given asC N (K) = (F 0 −K)N(d N ) +
σN
√
T n(dN ), whered N = F0−K σN √ T ,N(z) is the cumulative distribution function andn(z) is the probability
density function of the standard normal distribution (Choi et al., 2022).
6

0
20
40
60
LTTR value
( /MWh)
(a) Bachelier option value for A B and B A LTTRs
Intrinsic value A B
Intrinsic value B A
Time value A B
Time value B A
T otal value A B
T otal value B A
-60 -50 -40 -30 -20 -10 0 10 20 30 40 50 60
B A spread ( /MWh)
1
0
1
Net forward position
(MW per 1 MW LTTR)
long B long A
short A short B
(b) Net forward positions of LTTR arbitrageurs
Net A position ( =0)
Net B position ( =0)
Net A position ( >0)
Net B position ( >0)
Figure 1: Bachelier option values and net forward positions vs. B–A spread. Panel (a)
shows how LTTR option value changes with the cross-border spread. The corresponding net
forward positions of arbitrageurs are shown in (b). Spread volatility increases option value
but reduces the size of forward market positions. Net positions are short in importing and
long in exporting markets.
4 Empirical strategy
Empirically testing these hypotheses requires a model of forward prices that is granular
enough to capture the instantaneous impact of LTTR arbitrage while controlling for the
effects of physical hedging on forward prices. I build on the model of Fleten et al. (2015)
and use the daily log returns of electricity futures, i.e., the first differences of the natural
logarithm of daily settlement prices for the respective futures contract, as the dependent
variable. In what follows I introduce the independent variables, explain the identification
strategy and the model specification, and describe the data.
4.1 Measuring the effect of LTTR auctions
Section 3 suggests that new forward positions should be opened after the publication of LTTR
auction results. Auctions are usually clustered around the beginning of December for annual
and around the third week of a month for monthly LTTRs. Figure 2 shows daily traded
volumes for annual German-Austrian spread futures, which are equivalent to simultaneous
buy and sell orders for two outright futures, one in Germany and one in Austria. The
publication of German-Austrian LTTR auction results coincides with clear spikes in traded
7

volumes of spread futures with the same delivery period, suggesting that some LTTR holders
engage in arbitrage immediately after acquiring transmission rights. These trades around
auctions, not only for the German-Austrian border but also for others, are visible in total
outright traded volumes too, especially for Austria (see Figure 3).
I construct separate panels of annual and monthly futures contractsitraded at daily
resolutiontto test the effect of LTTR arbitrage on the returns of futures contracts with
the same delivery period. This means, for example, testing whether overnight returns of the
Cal-2025 base future are driven by auction results for an annual LTTR with delivery in 2025.
To capture the instantaneous effect of LTTR auctions, I constructQ i,t, which reflects
awarded LTTR capacity per trading day, normalized by total awarded LTTR capacity for
the respective delivery period.Q i,t therefore represents the normalized daily sum of bilateral
LTTR capacities shown in Figure 3 and is zero on non-auction days.
While the sign of the effect of arbitrage depends on which LTTR direction is in the
money (i.e., on the sign of the cross-border spread), the size of the effect should increase
with auctioned capacities and spread levels and should decrease with spread volatility (see
Figure 1).
Aug '24 Sep '24 Oct '24 Nov '24 Dec '24
0
100
200
300 DE-AT LTTR auction results published
DE-AT spread futures traded volume
Aug '25 Sep '25 Oct '25 Nov '25 Dec '25
0
500
1000
Volume (GWh)
Figure 2: DE-AT spread futures volumes. Daily spread futures volumes traded at EEX
exhibit a spike on the day when LTTR auction results for the DE-AT and AT-DE LTTRs
are published, suggesting that market participants open spread futures positions right after
auctions.
8

Sep '19 Oct '19 Nov '19 Dec '19
0
5000
10000
15000
Cal-20 traded volumes and auctions for 2020 LTTRs
Sep '20 Oct '20 Nov '20 Dec '20
0
5000
10000
15000
Cal-21 traded volumes and auctions for 2021 LTTRs
Sep '21 Oct '21 Nov '21 Dec '21
0
5000
10000
15000Traded volume (GWh)
Cal-22 traded volumes and auctions for 2022 LTTRs
Sep '22 Oct '22 Nov '22 Dec '22
0
5000
10000
15000Traded volume (GWh)
Cal-23 traded volumes and auctions for 2023 LTTRs
Sep '23 Oct '23 Nov '23 Dec '23
0
5000
10000
15000
Cal-24 traded volumes and auctions for 2024 LTTRs
Sep '24 Oct '24 Nov '24 Dec '24
0
5000
10000
15000
Cal-25 traded volumes and auctions for 2025 LTTRs
2
4
0
2
4
2
4
Awarded LTTR capacity (GW)
0
2
4
6
Awarded LTTR capacity (GW)
0
2
4
6
0
2
4
Germany
Registration Exchange DE AT
 DE BE
 DE CH
 DE D1
 DE D2
 DE FR
 DE NL
Sep '19 Oct '19 Nov '19 Dec '19
0
500
1000
Cal-20 traded volumes and auctions for 2020 LTTRs
Sep '20 Oct '20 Nov '20 Dec '20
0
500
1000
Cal-21 traded volumes and auctions for 2021 LTTRs
Sep '21 Oct '21 Nov '21 Dec '21
0
500
1000Traded volume (GWh)
Cal-22 traded volumes and auctions for 2022 LTTRs
Sep '22 Oct '22 Nov '22 Dec '22
0
500
1000Traded volume (GWh)
Cal-23 traded volumes and auctions for 2023 LTTRs
Sep '23 Oct '23 Nov '23 Dec '23
0
500
1000
Cal-24 traded volumes and auctions for 2024 LTTRs
Sep '24 Oct '24 Nov '24 Dec '24
0
500
1000
Cal-25 traded volumes and auctions for 2025 LTTRs
0
2
4
0
2
4
0
2
4
Awarded LTTR capacity (GW)
0
2
4
6
Awarded LTTR capacity (GW)
0
2
4
6
0
2
4
Austria
Registration Exchange AT CH
 AT CZ
 AT DE
 AT HU
 AT IT
 AT SI
Figure 3: Front-year futures traded volumes and annual LTTR auctions for Germany and
Austria. Total traded futures volume comprises exchange-traded volumes and cleared bilat-
eral trades registered at EEX. Total awarded LTTR capacity per border (summed up across
directions) is shown on the secondary axis.
9

To approximate expected spread levels, I calculate the difference between observed auc-
tion prices of importing and exporting LTTRs per auction day. To reflect that LTTR capac-
ities differ by direction for some borders, I weight importing and exporting auction prices
by the capacities awarded in the respective direction. That is, for each futures contraction
marketAwith neighborsj= 1, . . . , J5 and daytI define:
LT T RA i,t =
PJ
j=1 C j→A i,t P j→A i,t
PJ
j=1 C j→A i,t −
PJ
j=1 C A→j i,t P A→j i,t
PJ
j=1 C A→j i,t (2)
whereP A→j i,t andP j→A i,t denote the LTTR auction prices in directionA→jandj→A, and
C A→j i,t , Cj→A i,t are the corresponding awarded capacities.LT T R A i,t is hence denominated in
Euro/MWh. A positive value ofLT T RA i,t reflects that the importing (j→A) LTTR has the
higher expected payoff, such that the expected effect ofLT T R A i,t on overnight returns is
negative: the more positive the LTTR price spread (i.e., the higher the expected spot price
inA, relative to its neighbors), the larger the short forward positions of LTTR arbitrageurs
inA. Increased supply of forward contracts should reduce equilibrium forward prices on
auction days, resulting in negative overnight returns.
To approximate spread volatility, I defineσ A i,t as the standard deviation of daily changes
in theA−jspot price spread over the last two years before the respective LTTR auction.
On days with auctions on multiple borders, I calculate a capacity-weighted average volatility
across all neighbors. Similar toLT T R A i,t,σ A i,t captures the spread volatility per auctioned
border and is zero on non-auction days.
4.2 Identification
A potential threat to identification is that daily futures returns may themselves influence
LTTR auction results. The auction window for annual LTTRs usually spans seven days,
while the window for monthly products is usually between two and four days. Auction
results are published around 20 minutes after the auction window is closed at 2-4pm CET.
The window for settlement price formation at EEX, on the other hand, is 5:05-5:15pm CET
since 2022 (it was 4:20pm-4:30pm CET prior to 2022) (EEX, 2022). Even if LTTR auction
bids are submitted at the very end of the auction window, the LTTR spread is determined
prior to futures prices, which qualifies the LTTR spread as contemporaneously exogenous and
allows for a causal interpretation of Ordinary Least Squares (OLS) estimates (Wooldridge,
2010).
5For Germany,Jincludes Danish bidding zones DK1 and DK2, the Netherlands, Belgium, France,
Switzerland, Austria, as well as the joint Polish-Czech LTTR profile. For Austria,Jincludes Switzerland,
Italy, Slovenia, Hungary, Czechia, and Germany.
10

Past futures returns may affect current futures returns, for example through the bid-ask
spread (Roll, 1984). At the same time, past futures returns may affect the fair value of
LTTRs and thus the current LTTR spread. Conditioning on lagged returns should block
these causal paths.
Spot market conditions determine both forward prices and the fair value of LTTRs.
Hence, it is crucial to control for common fundamentals and systematic risk. Following the
literature, I therefore include fuel and equity market returns, renewable generation, and the
variance and skewness of spot prices. Moreover, specifying the dependent variable as a first
difference reduces persistence and spurious correlation with the LTTR spread, which is a
level variable (Hamilton, 1994).
Another identifying assumption is that LTTR auctions only affect returns on the days
when LTTR auction results are published. This assumption is tested with an event study
around auction days. Even with flat pre- and post-auction trends, however, it cannot be
ruled out that LTTR auction days coincide with unobserved events that affect forward prices.
I therefore use the event study design to conduct a placebo test, which does not use the front-
year futures, as in the baseline model, but the second year-ahead returns as the dependent
variable. This means, for example, testing whether the auction for the 2025 LTTR has an
effect on Cal-2026 futures returns. Both Cal-2025 and Cal-2026 futures are traded on LTTR
auction days, but only the Cal-2025 hedges the 2025 LTTR. Hence, Cal-2026 returns should
be unaffected by the auctions for the 2025 LTTR.
4.3 Model specification
I estimate the following panel model for the log returnsr i,t of annual or monthly contracts
iat daily resolutiont:
ri,t =β 0 +β 1 Qi,t ·LT T Ri,t +β 2 Qi,t ·LT T Ri,t ·σ i,t
+β 3 ri,t−1 +β 4 Qi,t +β 5 LT T Ri,t +β 6σi,t
+β 7 Gast +β 8 Coal t +β 9 Carbon t +β 10 Stockt
+β 11 W indt +β 12 Solar t +β 13 Reservoir t
+β 14 V art +β 15 Skew t
+α i +γ m +γ dow +γ hol +γ f ront+γ 2022 +ϵ i,t
(3)
whereQ i,t ·LT T Ri,t is the variable of interest: it captures how the impact on forward returns
scales with the volume of auctioned capacity and the LTTR spread. A potentially attenuated
effect on forward positions at higher spread volatility is captured byQ i,t ·LT T Ri,t ·σ i,t.
11

Skew t andV ar t are skewness and variance of spot prices calculated over a 365-day
historical rolling window. I control for the effect of fuel prices by including the logarithmic
returns of TTF gas (Gas t), API2 CIF ARA coal (Coal t), and EU ETS (Carbon t) prices.
W indt andSolar t are the first differences of daily wind and solar generation, whileReservoirt
controls for the deviations of daily hydro reservoir filling ratios from historical averages. I
control for equity market conditions by including the logarithmic returns of national stock
market indices (Stock t).α i,γ m,γ dow,γ f ront, andγ hol capture contract, month, day-of-
the-week, front-period and holiday fixed effects. The 2022 energy crisis was characterized
by high price volatility and substantially reduced forward market liquidity (Kr¨ oger et al.,
2025). To estimate the effect of LTTR arbitrage during non-crisis conditions, I control for the
extraordinary level and slope effects of the 2022 energy crisis throughγ 2022, which contains a
2022 dummy and an interaction of that dummy withQ i,t ·LT T Ri,t. The first lag of returns
ri,t−1 is included to account for autocorrelation in daily returns and the effect of past forward
prices on current LTTR spreads. I compute Driscoll–Kraay standard errors to make inference
robust to heteroskedasticity, autocorrelation, and cross-sectional dependence. This accounts
for persistent common shocks that affect multiple contracts.
4.4 Data
I estimate the model separately for the German and Austrian forward markets. The Ger-
man market is the largest and most liquid forward market in Europe, while the neighboring
Austrian market is much less liquid (see Figure 3). Yet, relative to total electricity consump-
tion, Austria is more interconnected than Germany (Stiewe et al., 2025). Austrian LTTR
capacities are therefore relatively larger than German capacities, suggesting, other things
equal, a stronger effect of LTTR arbitrage in Austria. I use daily trading data from 2018
to 2025 on annual and monthly base and peak futures contracts traded at EEX. The final
sample consists of 26 annual and 186 monthly base and peak contracts each for the German
and Austrian markets. Wind, solar, and hydro reservoir data are obtained from ENTSO-E
(2026), while LTTR auction results are published by Joint Allocation Office (2026). Natural
gas prices are retrieved from Investing.com (2026d), coal prices from Investing.com (2026b),
carbon prices from International Carbon Action Partnership (2026), and stock indices from
Investing.com (2026c) and Investing.com (2026a).
I thus estimate four separate regressions: returns of monthly (annual) futures on monthly
(annual) LTTR spreads for Germany and Austria. In these regressions, both base and
peak futures contracts are included. Reservoir filling ratios are only controlled for in the
Austrian regressions as data are not available for Germany and the share of hydro reservoirs
12

in electricity generation is small. Table 1 shows that annual LTTRs importing into Germany
have on average been priced slightly higher than LTTRs exporting from Germany, while the
opposite holds for annual LTTRs with a leg in Austria. The wide range of LTTR spreads
for both countries and durations reflects that trade patterns change over time. This is also
evident in Figure A2, which plots the daily spreads in monthly and annual LTTR auction
prices for Germany and Austria. The econometric analysis aims to exploit this variation.
Table 1: Descriptive statistics
Variable Mean Median Min Max Std Skew
Germany
LT T Ri,t (annual, EUR/MWh) 0.6 -2.2 -22.2 33.3 10.5 1.0
LT T Ri,t (monthly, EUR/MWh) -3.2 -1.4 -90.2 52.7 13.5 -1.8
Qi,t (annual, GW) 3.4 1.1 0.4 15.5 4.5 1.6
Qi,t (monthly, GW) 3.8 1.8 0.1 21.8 4.3 1.3
σi,t 16.5 13.8 5.9 39.7 9.8 1.1
V art 3381.0 919.8 107.0 20137.1 5581.7 1.9
Skew t 0.1 -0.2 -2.4 3.0 1.2 0.1
Stockt 15390 14494 8442 24611 3687 1
W indt (GW) 11.8 9.4 0.3 44.3 8.7 1.1
Solar t (GW) 6.1 5.7 0.2 20.0 4.2 0.5
Austria
LT T Ri,t (annual, EUR/MWh) -2.1 -3.0 -22.2 17.5 7.2 0.1
LT T Ri,t (monthly, EUR/MWh) -4.0 -3.0 -47.2 47.0 10.4 -0.1
Qi,t (annual, GW) 3.3 1.5 0.1 12.2 4.3 1.2
Qi,t (monthly, GW) 2.7 0.7 0.0 20.3 4.0 1.5
σi,t 14.4 12.8 5.7 30.3 7.6 0.7
V art 3462.2 810.9 59.9 21891.0 5799.0 1.9
Skew t 0.3 0.1 -1.7 3.1 1.0 -0.0
Stockt 3327 3262 1631 5326 593 0
W indt (GW) 0.9 0.7 0.0 3.3 0.7 1.0
Solar t (GW) 0.3 0.1 0.0 1.5 0.3 2.1
Reservoir t (GWh) 74.4 65.5 -277.3 508.8 169.2 0.2
Common controls
Carbon t (EUR/t) 54 62 8 98 26 0
Gast (EUR/MWh) 43 31 4 339 43 3
Coal t (EUR/t) 109 89 35 403 75 2
Notes: This table reports summary statistics of untransformed variables.
13

5 Results
In this section, I summarize the regression results for Germany and Austria, starting with
the models for annual LTTR auctions.
5.1 Annual LTTR auctions
I find a significant effect of LTTR auction results on forward market returns for Germany in
line with the predictions derived in Section 3. More specifically, overnight returns of annual
German futures are more negative when the auction-specific LTTR price spread is more
positive, reflecting that importing LTTRs are priced higher than exporting LTTRs. Arbi-
trage hence reduces prices in importing markets and increases prices in exporting markets.
This reduces forward spreads and therefore the gap between forward spreads and LTTR
prices. The size of this effect increases with auctioned capacity. It shrinks towards zero at
high volatility (β2 is positive and significant), which also corroborates my hypothesis. When
importing and exporting LTTRs are priced similarly, no clear directional effect on forward
markets is expected. Indeed, the main effect ofQ i,t (i.e., the auction effect whenLT T Ri,t is
zero) is insignificant.
To assess if LTTR auction results affect returns before and after auctions, I run an event
study robustness check on annual German futures (see Figure 4). The contemporaneous
coefficient onQ i,t ·LT T Ri,t is significant while leads and lags are not, which shows that ar-
bitrage has an immediate and non-persistent effect on forward markets after auction results
are published. This indicates that the volume spikes in Figure 2 reflect market participants
realizing profits shortly after the auctions. The event-study placebo test yields an insignif-
icant contemporaneous effect of LTTR auctions on second year-ahead futures returns (see
Figure A1), suggesting that the auction-day effects on front-year futures returns are driven
by LTTR arbitrage. Apart from a significant effect of lag 5, pre- and post-trends are as flat
as front-year returns.
The effect of LTTR auctions on Austrian futures returns, on the other hand, is insignif-
icant. This is surprising given that the spikes in traded Austrian futures volume around
LTTR auctions are more pronounced than for Germany (see Figure 3). However, unlike on
the German forward market, most of these traded Austrian volumes are cleared bilateral
trades. These trades are not directly taken into account for settlement price formation by
EEX. They would affect settlement prices indirectly if, for example, the net short positions
of arbitrageurs were offset bilaterally by buyers that would otherwise have traded at the
exchange. However, Austrian exchange-traded volumes are generally very small, which sug-
gests that traded volumes on auction days would have been similarly small without LTTR
14

 -6
 -5 -4 -3 -2 -1 (ref.) 0 1 2 3 4 5  6
Days relative to LTTR auction
0.100
0.075
0.050
0.025
0.000
0.025
Coefficient
LTTR auction results published
Cal+1 futures effect ± 95% CI
Figure 4: Effect of LTTR spread around annual LTTR auction days on annual German
front-year futures. This event study shows how the effect ofQ i,t ·LT T Ri,t evolves around
the publication of auction results. Returns are flat before and after auctions, suggesting an
immediate and non-persistent price impact of LTTR arbitrage.
arbitrage. Hence, the indirect effect of cleared bilateral trades on Austrian futures settlement
prices is likely negligible, which may explain the insignificant effect.
The control variables enter with signs and magnitudes largely consistent with the litera-
ture on forward price formation, suggesting that observable fundamentals are captured well.
While gas, carbon, and coal returns exhibit strong and positive effects on futures returns,
renewable generation (wind, solar, and reservoir hydro filling ratios) has a negative, yet in-
significant effect on futures returns. I find mixed support for the hypotheses of Bessembinder
and Lemmon (2002) as only annual German overnight returns show a positive effect of spot
price skewness and a negative effect of spot price variance. Full regression results are given
in Table 2.
5.2 Monthly LTTR auctions
The monthly regressions yield insignificant effects of LTTR auctions, suggesting that holders
of monthly LTTRs do not engage in arbitrage after monthly auctions. This might reflect
that uncertainty about realized spreads is lower for monthly products. Holders can better
forecast next month’s spreads than next year’s spreads, which makes holding the LTTR until
delivery less risky. At the same time, the market liquidity costs of arbitrage may be higher
as monthly futures are less liquid than annual futures.
Taken together, this should make it relatively more attractive to hold monthly LTTRs
until delivery. Market participants may therefore equally realize profits with monthly LTTRs,
just without a detectable forward market footprint.
15

Table 2: Regression results
Germany Austria
Annual Monthly Annual Monthly
Intercept -0.0021* -0.0001 -0.0021* 0.0004
(0.0012) (0.0023) (0.0011) (0.0023)
Qi,t ·LT T Ri,t -0.0094*** -0.0017 0.0006 0.0089
(0.0031) (0.0103) (0.0040) (0.0088)
Qi,t ·LT T Ri,t ·σ i,t 0.0005*** 0.0005 -0.0000 -0.0008
(0.0001) (0.0006) (0.0002) (0.0006)
Qi,t ·LT T Ri,t ·γ 2022 -0.0042* -0.0134* 0.0010 0.0102
(0.0023) (0.0076) (0.0016) (0.0072)
LT T Ri,t -0.0000 0.0001 -0.0009* 0.0000
(0.0002) (0.0001) (0.0005) (0.0001)
σi,t -0.0000 0.0000 -0.0008*** 0.0001
(0.0001) (0.0001) (0.0003) (0.0001)
Qi,t -0.0095 0.0677* 0.0178* 0.0288
(0.0100) (0.0363) (0.0094) (0.0294)
Gast 0.1432*** 0.4661*** 0.1371*** 0.4504***
(0.0134) (0.0437) (0.0130) (0.0433)
Coal t 0.0242 0.1271*** 0.0218 0.1260***
(0.0173) (0.0345) (0.0169) (0.0326)
Carbon t 0.2117*** 0.2015*** 0.1968*** 0.1822***
(0.0149) (0.0476) (0.0141) (0.0449)
W indt -0.0004 -0.0003 -0.0001 -0.0001
(0.0003) (0.0007) (0.0003) (0.0005)
Solar t -0.0002 -0.0004 -0.0000 0.0006
(0.0006) (0.0012) (0.0005) (0.0011)
Reservoir t -0.0000 -0.0000***
(0.0000) (0.0000)
Stockt 0.0010 -0.1366** 0.0280 -0.0704
(0.0241) (0.0687) (0.0221) (0.0694)
V art -0.0000** -0.0000** -0.0000** -0.0000**
(0.0000) (0.0000) (0.0000) (0.0000)
Skew t 0.0005** -0.0005 0.0005 -0.0012*
(0.0002) (0.0007) (0.0003) (0.0007)
γ2022 0.0027* -0.0098** 0.0032* -0.0086**
(0.0017) (0.0038) (0.0017) (0.0037)
γf ront -0.0001 -0.0017*** -0.0002 -0.0017***
(0.0005) (0.0004) (0.0005) (0.0004)
Month, day-of-week, holiday FE Yes Yes Yes Yes
Contract FE Yes Yes Yes Yes
N 24168 22701 24072 22620
R2 0.32 0.52 0.32 0.50
F-statistic 350.73 730.06 325.76 664.77
Notes: Driscoll–Kraay standard errors in parentheses. * p<0.10, ** p<0.05, *** p<0.01
16

6 Discussion
These results show a systematic effect of LTTR auctions on forward returns for annual
products on the liquid German forward market. The sign and size of this effect correspond
to the price spread in LTTRs, the auctioned capacity, and the volatility of cross-border
spreads, which suggests that this forward market footprint reflects arbitrage across trans-
mission rights and forward markets. Despite the insignificant effect, arbitrage likely takes
place on the Austrian forward market too: Figure 3 shows a clear correlation of volume
spikes and auctions for annual products. Illiquidity, however, likely mutes the price impact
of arbitrage in Austria.
Arbitrage hence narrows but, as shown by ACER (2024), does not eliminate the gap
between LTTR and spread forward prices. This suggests limits to arbitrage (Shleifer and
Vishny, 1997). Transaction costs represent a first limit to arbitrage (Brunnermeier and
Pedersen, 2009). They are part of the trading premium that financial traders demand for
holding transmission rights (Opgrand et al., 2022). Because of low demand from physical
hedgers for LTTRs, financial participants can set the price in auctions. The negative trading
premiums priced into their marginal bids explain why underpricing emerges. If the marginal
bidder’s trading premium only contains the transaction costs of arbitrage, Equation 1 shows
that she would just break even when engaging in arbitrage. For inframarginal participants
with higher willingness to pay, e.g., because of lower risk aversion or lower transaction
costs, arbitrage is profitable. Because transaction costs are likely non-negligible for most
participants, however, not all of them engage in arbitrage, preventing mispricing from being
fully corrected.
Inelastic supply of transmission rights is another limit to arbitrage. Market participants
cannot buy more than the fixed LTTR capacity, which limits the size and the price impact
of their orders on forward markets. Even if forward volumes are large relative to average
liquidity levels, the example of Austria illustrates that forward market illiquidity can result
in muted price effects.
These findings have clear distributional implications. Who benefits from LTTR auctions
can be inferred from the structure of the demand curve for LTTRs, which is populated by
physical and financial participants. Assuming that all participants are risk-averse, physical
hedgers – if they participate in the auction at all – should be willing to pay a positive risk
premium to hedge basis risk. Financial participants, who demand a premium for holding
LTTRs, should hence be placed below them on the LTTR demand curve. If trading pre-
miums are heterogeneous, the marginal, price-setting bidder is the financial trader with the
largest negative trading premium. Awarded participants with less negative (or even positive)
17

premiums therefore capture inframarginal rents. A different pricing rule might also result in
rents: in pay-as-bid instead of pay-as-clear auctions, bidders might shade their bids down
towards the expected marginal price (Horta¸ csu and McAdams, 2010).
Heterogeneity in trading premiums and the higher willingness to pay of physical partic-
ipants explain rents when all participants are price takers. Market power on the demand
side can increase those rents. Ausubel et al. (2014) show that a bidder whose demand is
large relative to the offered capacity has an incentive to bid below her valuation in order
to lower the clearing price on the units she wins. An assessment of competition levels in
LTTR auctions is beyond the scope of this study but the fact that LTTR auctions are usually
several times oversubscribed suggests that price reductions from withholding demand, and
thus the profits from strategic behavior, are limited. While the results suggest that LTTR
holders are earning rents, a quantification of these rents is not possible in this study because
firm-level data is unavailable for Europe. This is another challenge for future research.
TSOs lose from issuing LTTRs, and they lose more than LTTR holders win: because
arbitrage involves transaction costs, holders can only realize part of the gap between the
LTTR and forward spread price as a profit. TSO losses, on the other hand, amount to the
full gap between the fair option value at the time of the auction and the auction price. This
shortfall is not borne by TSOs but is financed from the congestion income pool that would
otherwise reduce grid fees. If market participants can realize nearly risk-free profits with
LTTRs and TSOs can pass through their losses, this only leaves consumers to bear the cost
through grid fees. This study hence confirms the concerns of regulators (ACER, 2023).
This paper does not attempt a full welfare analysis of LTTRs. Such an analysis should
take into account that consumers benefit from increased forward market liquidity and im-
proved price discovery, which might partly offset the transfer from consumers to LTTR hold-
ers. These benefits are most likely small, however, as the LTTR-induced forward volumes
are essentially one-off events (see Figure 3 for Austria).
7 Conclusion
This study documents the interaction of transmission rights with forward markets and as-
sesses the efficiency of European LTTRs. Because LTTRs are largely unattractive as a
hedging instrument against basis risk, substantial capacity is acquired by financial traders.
Financial traders require a premium for holding LTTRs, which explains their systematic
underpricing relative to forward markets. I show that inframarginal LTTR holders can lock
in profits by taking forward market positions immediately after the auction, effectively en-
gaging in arbitrage across LTTR and forward markets. Building on option pricing theory, I
18

show that their aggregate forward market positions should be short in importing and long in
exporting markets. Using 2018-2025 data, I find empirical support for this hypothesis in the
German market. Arbitrage therefore attenuates but cannot eliminate the mispricing between
transmission rights and forward markets. These results confirm that holders of transmission
rights earn systematic rents. The corresponding losses are ultimately borne by consumers
through higher grid fees, suggesting a transfer from consumers to transmission rights holders.
These findings indicate that LTTRs deliver limited hedging value at substantial cost.
This carries a lesson for transmission rights design. The fundamental problem with LT-
TRs is that TSOs are forced to sell insurance for which there is too little demand. Low
demand for LTTRs as a hedging instrument is not only caused by the design shortcomings
of LTTRs but also reflects that other products for hedging basis risk are traded on private
markets. Any redesign of transmission rights should therefore rest on a thorough investiga-
tion of the incompleteness of these markets, since interventions are potentially costly. This
also involves estimating the future demand for insurance against cross-border spread risk,
given that both the build-out of physical interconnection capacity and the more efficient
utilization of that capacity through flow-based market coupling can increase spot price con-
vergence, reducing basis risk and thus the demand for insuring it through transmission rights
or alternative products.
19

Data availability
The data that support the findings of this study are available from the European Energy
Exchange (EEX), but restrictions apply to the availability of these data, which were used
under license for the current study and so are not publicly available. The code needed to
reproduce the analysis is available under an open license athttps://github.com/cstiewe
/lttr-arbitrage.
Declaration of use of generative AI and AI-assisted technologies
During the preparation of this work, I used Claude to assist with writing the code for the
analysis. I take full responsibility for the content of the published article.
Acknowledgments
I thank Lion Hirth, Jorge S´ anchez Canales, Alice Lixuan Xu, Chiara Fusar Bassini, Vincent
Th´ evenin, and participants at the Young Energy Economists and Engineers Seminar for
valuable feedback and discussions, as well as EEX for providing access to the data used in
this study. This work is supported by the German Federal Ministry of Research, Technology
and Space (BMFTR) via the ARIADNE Project (FKZ 03SFK5K0-2).
20

Appendix
 -6
 -5 -4 -3 -2 -1 (ref.) 0 1 2 3 4 5  6
Days relative to LTTR auction
0.125
0.100
0.075
0.050
0.025
0.000
0.025
0.050
Coefficient
LTTR auction results published
Cal+1 futures effect ± 95% CI
Cal+2 futures effect ± 95% CI
Figure A1: Placebo test of the effect of LTTR auctions on second year-ahead German futures
returns. This tests, for example, whether auctions for the 2025 LTTR affect not only Cal-
2025 futures but also Cal-2026 futures traded on the same day.
21

Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
10
5
0
5
2018
Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
10
5
0
2019
Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
10
5
0
5
2020
Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
40
20
0
20
40
2021
Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
50
0
2022
Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
20
0
20
2023
Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
10
0
10
20
2024
Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
20
0
20
40
2025
LTTR spread (EUR/MWh)
Germany
Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
20
10
0
2018
Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
15
10
5
0
5
2019
Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
10
5
0
2020
Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
20
0
20
2021
Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
50
0
50
2022
Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
20
10
0
10
20
2023
Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
20
0
20
2024
Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
20
0
2025
LTTR spread (EUR/MWh)
Austria
Monthly LTTR Annual LTTR
Figure A2: Monthly and annual LTTR spreads, Euro/MWh. Bars indicate daily spreads in
LTTR auction prices. Positive (negative) values imply that importing (exporting) LTTRs
are valued higher.
22

References
ACER (2023). Further Development of the EU Electricity Forward Market.https://acer
.europa.eu/sites/default/files/documents/Position%20Papers/Electricity_For
ward_Market_PolicyPaper.pdf.
ACER (2024). Progress of EU Electricity Wholesale Market Integration – 2024 Monitoring
Report.https://www.acer.europa.eu/sites/default/files/documents/Publicati
ons/ACER_2024_MMR_Market_Integration.pdf.
ACER (2025). Progress of EU Electricity Wholesale Market Integration – 2025 Monitoring
Report.https://www.acer.europa.eu/sites/default/files/documents/Publicati
ons/ACER-2025-Electricity-market-integration.pdf.
Allaz, B. and Vila, J.-L. (1993). Cournot Competition, Forward Markets and Efficiency.
Journal of Economic Theory, 59(1):1–16.
Ausubel, L. M., Cramton, P., Pycia, M., Rostek, M., and Weretka, M. (2014). Demand reduc-
tion and inefficiency in multi-unit auctions.The Review of Economic Studies, 81(4):1366–
1400.
Bachelier, L. (1900). Th´ eorie de la sp´ eculation.Annales scientifiques de l’ ´Ecole normale
sup´ erieure, 17:21–86.
Beato, P. (2021). Long Term Interconnection, Transmission Rights and Renewable Deploy-
ment.https://dx.doi.org/10.2139/ssrn.3878903.
Benth, F. E., Cartea, ´A., and Kiesel, R. (2008). Pricing forward contracts in power markets
by the certainty equivalence principle: Explaining the sign of the market risk premium.
Journal of Banking & Finance, 32(10):2006–2021.
Bessembinder, H. and Lemmon, M. L. (2002). Equilibrium Pricing and Optimal Hedging in
Electricity Forward Markets.The Journal of Finance, 57(3):1347–1382.
Birge, J. R., Horta¸ csu, A., Mercadal, I., and Pavlin, J. M. (2018). Limits to arbitrage in
electricity markets: A case study of miso.Energy Economics, 75:518–533.
Borenstein, S., Bushnell, J., Knittel, C. R., and Wolfram, C. (2008). Inefficiencies and
Market Power in Financial Arbitrage: A Study of California’s Electricity Markets.The
Journal of Industrial Economics, 56(2):347–378.
23

Brunnermeier, M. K. and Pedersen, L. H. (2009). Market Liquidity and Funding Liquidity.
The Review of Financial Studies, 22(6):2201–2238.
Bunn, D. W. and Chen, D. (2013). The forward premium in electricity futures.Journal of
Empirical Finance, 23:173–186.
Carnero, M. A., Fleten, S.-E., Størdal, S., and Westgaard, S. (2025). Ex ante and ex post
risk premiums in electricity futures.Quantitative Finance, 25(11):1717–1729.
Choi, J., Kwak, M., Tee, C. W., and Wang, Y. (2022). A Black–Scholes user’s guide to the
Bachelier model.Journal of Futures Markets, 42(5):959–980.
Deng, S.-J., Oren, S., and Meliopoulos, A. P. (2010). The inherent inefficiency of simultane-
ously feasible financial transmission rights auctions.Energy Economics, 32(4):779–785.
EEX (2022). Clearing Circular 42/2022|Adjustment of the settlement window for EEX
Power Derivatives.https://www.ecc.de/fileadmin/Global/News/ECC/ECC_Circulars
/2022/20221103_ECC_Clearing_Circular_No._42_Adjustment_of_the_settlement_w
indow_Power_Derivatives.pdf.
ENTSO-E (2026). ENTSO-E Transparency Platform.https://transparency.entsoe.eu/.
European Commission (2016). Commission Regulation (EU) 2016/1719 of 26 September
2016 establishing a guideline on forward capacity allocation.http://data.europa.eu/e
li/reg/2016/1719/oj.
European Commission (2024). Targeted consultation: Revision of the electricity guideline
on forward capacity allocation.https://energy.ec.europa.eu/consultations/targ
eted-consultation-revision-electricity-guideline-forward-capacity-allocat
ion_en#consultation-outcome.
European Parliament and Council of the European Union (2019). Regulation (EU) 2019/943
of the European Parliament and of the Council of 5 June 2019 on the internal market for
electricity.http://data.europa.eu/eli/reg/2019/943/oj.
Fleten, S.-E., Hagen, L. A., Nyg ˚ ard, M. T., Smith-Sivertsen, R., and Sollie, J. M. (2015). The
overnight risk premium in electricity forward contracts.Energy Economics, 49:293–300.
Hamilton, J. D. (1994).Time Series Analysis. Princeton University Press.
Hirth, L., Schlecht, I., and Eicke, A. (2024). Cross-border Forward Markets.https://neon
.energy/Neon-Forward-Markets.pdf.
24

Horta¸ csu, A. and McAdams, D. (2010). Mechanism choice and strategic bidding in divisible
good auctions: An empirical analysis of the Turkish Treasury auction market.Journal of
Political Economy, 118(5):833–865.
Huisman, R., Koolen, D., and Stet, C. (2021). Pricing forward contracts in power markets
with variable renewable energy sources.Renewable Energy, 180:1260–1265.
Hull, J. (2021).Options, Futures, and Other Derivatives. Pearson International.
International Carbon Action Partnership (2026). ICAP Allowance Price Explorer.https:
//icapcarbonaction.com/en/ets-prices.
Investing.com (2026a). ATX index.https://de.investing.com/indices/atx-historica
l-data.
Investing.com (2026b). Coal (API2) CIF ARA (ARGUS-McCloskey) Futures Historical
Prices.https://www.investing.com/commodities/coal-(api2)-cif-ara-futur
es-historical-data.
Investing.com (2026c). DAX index.https://de.investing.com/indices/germany-30-h
istorical-data.
Investing.com (2026d). Dutch TTF Natural Gas Futures Historical Prices.https://www.
investing.com/commodities/dutch-ttf-gas-c1-futures-historical-data.
Ito, K. and Reguant, M. (2016). Sequential Markets, Market Power, and Arbitrage.American
Economic Review, 106(7):1921–1957.
Jha, A. and Wolak, F. A. (2013). Testing for market efficiency with transactions costs:
An application to convergence bidding in wholesale electricity markets. InIndustrial
Organization Seminar, Yale University.
Joint Allocation Office (2026). Joint Allocation Office.https://www.jao.eu/auctions#/.
Kaldor, N. (1939). Speculation and Economic Stability.The Review of Economic Studies,
7(1):1–27.
Keynes, J. M. (1930). A Treatise on Money: The Pure Theory of Money. InThe History of
Banking II, 1844-1959 Vol 10, pages 86–104. Routledge.
Kristiansen, T. (2007). An assessment of the Danish–German cross-border auctions.Energy
Policy, 35(6):3369–3382.
25

Kr¨ oger, M., Neuhoff, K., and Schwenen, S. (2025). Contracts in Crisis: The War in Ukraine
and Long-Term Contracts in Energy Markets.Discussion Papers of DIW Berlin, (2118).
Leslie, G. W. (2021). Who benefits from ratepayer-funded auctions of transmission conges-
tion contracts? Evidence from New York.Energy Economics, 93:105025.
McInerney, C. and Bunn, D. (2013). Valuation anomalies for interconnector transmission
rights.Energy Policy, 55:565–578.
Mercadal, I. (2022). Dynamic competition and arbitrage in electricity markets: The role of
financial players.American Economic Journal: Microeconomics, 14(3):665–699.
Opgrand, J., Preckel, P. V., Gotham, D. J., and Liu, A. L. (2022). Price Formation in
Auctions for Financial Transmission Rights.The Energy Journal, 43(3):33–57.
Pe˜ na, J. and Rodr ´ ıguez, R. (2022). Market Makers and Liquidity Premium in Electricity
Futures Markets.The Energy Journal, 43(2):91–110.
Petropoulos, G. and Willems, B. (2020). Long-term transmission rights and dynamic effi-
ciency.Energy Economics, 88:104714.
Redl, C. and Bunn, D. W. (2011). Determinants of the Premium in Forward Contracts.
Journal of Regulatory Economics, 43:90–111.
Risanger, S. and Mays, J. (2024). Congestion Risk, Transmission Rights, and Investment
Equilibria in Electricity Markets.The Energy Journal, 45(1):173–200.
Roll, R. (1984). A Simple Implicit Measure of the Effective Bid-Ask Spread in an Efficient
Market.The Journal of Finance, 39(4):1127–1139.
Shleifer, A. and Vishny, R. W. (1997). The Limits of Arbitrage.The Journal of Finance,
52(1):35–55.
Stiewe, C., Xu, A. L., Eicke, A., and Hirth, L. (2025). Cross-border cannibalization: Spillover
effects of wind and solar energy on interconnected European electricity markets.Energy
Economics, 143:108251.
Wooldridge, J. M. (2010).Econometric Analysis of Cross Section and Panel Data. The MIT
Press.
26
