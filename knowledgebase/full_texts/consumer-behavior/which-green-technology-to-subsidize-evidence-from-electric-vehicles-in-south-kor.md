---
title: Which Green Technology to Subsidize? Evidence from Electric Vehicles in South Korea
url: https://arxiv.org/abs/2607.14446
category: consumer-behavior
subcategory: empirical
date: 2026-07
venue: ''
authors:
- Youngjin Hong
- In Kyung Kim
- Frank Verboven
source: arxiv
pdf_url: https://arxiv.org/pdf/2607.14446
pages: 73
chars: 151874
fetched_at: '2026-11-08T13:02:52+00:00'
kb_version: 1
---

# Which Green Technology to Subsidize? Evidence from Electric Vehicles in South Korea

Which Green Technology to Subsidize?
Evidence from Electric Vehicles in South Korea∗
Youngjin Hong† In Kyung Kim‡ Frank Verboven§
September 2026
Abstract
We develop a framework to compare the relative effectiveness of subsidizing alternative
emission-reducing technologies. We show that an intermediate technology may reduce emissions
more effectively than the cleanest technology if it induces sufficiently greater substitution away
from the prevailing high-emission technology. We apply the framework to the South Korean
passenger vehicle market using a demand model that incorporates mileage heterogeneity, an
important determinant of fuel-type choice. First, reallocating existing subsidies from battery
electric vehicles (BEVs), the cleanest technology, to hybrid electric vehicles (HEVs), an inter-
mediate technology, would reduce total greenhouse gas emissions by an additional 47%. Second,
for a BEV-focused subsidy policy to outperform an HEV-focused policy, the carbon intensity of
electricity generation would need to fall by approximately 45%. Our findings suggest that HEV
subsidies remain more effective than BEV subsidies until consumers become sufficiently willing
to switch to BEVs or electricity generation becomes sufficiently decarbonized.
Keywords: electric vehicles; life-cycle greenhouse gas emissions; vehicle purchase subsidies;
demand estimation; consumer mileage heterogeneity
JEL Codes: D12; H23; L62; Q58
∗We thank Soren Anderson, Luming Chen, Charles Murry, and Jingyuan Wang for their valuable comments. We
are also grateful to seminar participants at the University of Michigan IO Lunch, Korea University, Yonsei University,
MSU/UM EEE day, North America Summer Meeting of the Econometric Society, and IIOC. Sukyung Joo, Beomsu
Kim, Yongrok Kim, and Chaeeun Shin provided outstanding research assistance. We gratefully acknowledge the 2024
Data Voucher Program from the Ministry of Science and ICT of South Korea and the BK21 FOUR program, funded
by the Ministry of Education and the National Research Foundation of South Korea. All authors equally contributed
to this paper.
†Department of Economics, University of Michigan, E-mail:yjinhong@umich.edu.
‡Department of Economics, Sogang University, E-mail:inkim@sogang.ac.kr.
§Department of Economics, KU Leuven and CEPR, E-mail:frank.verboven@kuleuven.be.
arXiv:2607.14446v2  [econ.GN]  15 Sep 2026

1 Introduction
The transition from high-emission to low-emission technologies rarely occurs in a single step. The
cleanest technologies typically coexist with both dirty and intermediate technologies. To advance
progress toward net-zero greenhouse gas (GHG) emissions, governments often concentrate policy
support on the technological frontier with the lowest emissions. Although ranking technologies by
their stand-alone emissions provides a simple and salient criterion for allocating policy support, a
technology’s environmental effectiveness also depends on the extent to which it displaces dirtier
technologies. A subsidy for an intermediate technology can therefore generate larger emission
reductions than a subsidy for a frontier technology if it induces substantially greater substitution
away from prevailing dirty technologies.
To evaluate the relative effectiveness of subsidies for alternative emission-reducing technologies,
this paper focuses on the automobile market. This market offers considerable scope for emis-
sion savings because of multiple emission technologies and substantial substitution possibilities
among differentiated products. In particular, battery electric vehicles (BEVs), powered entirely
by rechargeable batteries, are widely viewed as the long-run future of the automotive industry, re-
placing conventional internal combustion engine vehicles (ICEVs). Accordingly, many governments
have promoted BEV adoption through generous purchase subsidies, tax incentives, and investments
in charging infrastructure.1 By contrast, hybrid electric vehicles (HEVs), which combine an internal
combustion engine with an electric motor, have received less policy attention.
Despite substantial government incentives, the expansion of charging networks, and techno-
logical improvements such as faster charging and longer driving ranges, BEV adoption has fallen
short of policy targets. Explanations include high purchase prices even net of subsidies, continued
consumer concerns about charging convenience and battery safety, and regulatory uncertainty.2 At
the same time, despite receiving substantially less policy support than BEVs, HEVs have contin-
ued to gain market share and outsell BEVs across most major economies. For example, in the
United States, BEV market share growth has recently slowed, with the share reaching 7.8% in
2024, whereas the HEV market share has grown more rapidly, reaching 10.6%. The gap between
HEV and BEV market shares is even more pronounced in several European countries, including
Germany, France, Italy, and the United Kingdom, as well as in Asian countries such as Japan,
South Korea, and India. China is a notable exception, where HEVs capture only a small market
share while BEVs account for nearly 30% of new vehicle sales. 3
The growing importance of HEVs raises the question of whether policies promoting HEV adop-
tion may reduce GHG emissions more effectively than policies focused exclusively on BEVs. Relative
1For an overview of policies in EU countries and the US, see European Automobile Manufacturers’ Association
(2025) and Alternative Fuels Data Center (2026), respectively.
2For example, in March 2025, the EU amended its CO 2 regulation to provide automakers with additional com-
pliance flexibility by allowing them to average emission performance over the period 2025-2027 rather than requiring
compliance in 2025 alone. In the United States, qualified BEVs were eligible for a federal tax credit of up to$7 500
for vehicles registered before October 2025, but eligibility expired under theOne Big Beautiful Bill Act.
3Figure G1 in Appendix G shows the evolution of BEV and HEV sales shares across these economies.
1

to BEVs, HEVs are typically less expensive and may better align with current consumer prefer-
ences, making them potentially more effective at inducing substitution away from higher-emission
ICEVs. Moreover, under current production technologies and electricity generation mixes across
different energy sources, the lifecycle GHG emission advantage of BEVs over HEVs may be smaller
than often presumed. While BEVs produce no tailpipe emissions, electricity generation remains
carbon intensive in many countries, and battery production is itself highly carbon intensive. These
considerations suggest that subsidizing HEVs rather than BEVs may, under certain conditions,
lead to larger overall reductions in GHG emissions.
We develop and empirically implement a framework to compare the relative effectiveness of
subsidies for alternative emission-reducing technologies (in our application, HEVs versus BEVs).
We begin with a theoretical model that highlights a possible tradeoff: while one technology may
generate lower stand-alone emissions per vehicle, the alternative technology may yield greater
diverted emissions by inducing more substitution away from the prevailing high-emission technology.
Next, we implement the model to examine the South Korean new passenger vehicle market,
where BEVs have received substantial government subsidies, whereas HEVs have received little
policy support. We estimate a random coefficients (RC) logit demand system (Berry, 1994; Berry
et al., 1995) using product-province-year-level data from 2012 to 2023 on vehicle sales, prices, and
characteristics. We combine these data with individual-level data on annual mileage and second-
choice survey responses by adding micro-moments (e.g., Conlon and Gortmaker, 2025; Grieco et al.,
2024) to account for rich sources of observed and unobserved consumer heterogeneity. The esti-
mates show that consumers perceive vehicles with the same fuel type as closest substitutes. More
interestingly, across fuel types, HEVs are perceived as closer substitutes for ICEVs than BEVs are.
Mileage heterogeneity plays an important role in the estimated substitutability across fuel types:
consumers who drive more place greater value on vehicles with low operating costs such as BEVs
and HEVs.
We subsequently compare the emission effects of subsidizing HEVs instead of BEVs, accounting
for price responses in an equilibrium model of Bertrand price-setting firms. We construct compre-
hensive product-year-level lifecycle GHG emission measures that vary across individuals because
of differences in vehicle usage (mileage). We incorporate two types of emissions: fuel-cycle emis-
sions, relating to (heterogeneous) usage, and vehicle-cycle emissions, relating to production and
recycling. Under South Korea’s current electricity generation mix, lifecycle emissions from BEVs
are on average 38% lower than those from ICEVs and 15% lower than those from HEVs.
Despite the lower per-vehicle emissions of BEVs relative to HEVs, we find that reallocating
the existing subsidy budget from BEVs to a uniform HEV subsidy would reduce total emissions
by an additional 47%. This advantage arises because HEVs induce greater substitution away from
conventional ICEVs than BEVs do. In contrast, BEV subsidies primarily generate within-BEV
substitution, thereby attenuating their overall emission benefits.
We then consider alternative BEV emission levels under electricity generation mixes matching
those observed in other countries. While South Korea’s electricity generation mix is currently
2

comparable to those of the United States and Germany, it relies much less on fossil fuels than the
mixes in China and India. We find that, for BEV subsidies to become more effective than HEV
subsidies, South Korea’s electricity generation mix would need to become at least 45% cleaner
through decarbonization of electricity supply, approximately reaching the level observed in Portugal.
Only a few countries, such as Norway, Brazil, or France, currently have even cleaner electricity
generation mixes. Conversely, our findings imply that BEV subsidies would generate only limited
emission reductions, or could even increase emissions, if electricity generation were as carbon-
intensive as in countries such as India and Kazakhstan.
In sum, our analysis establishes that subsidies should not necessarily target the technology
with the lowest per-vehicle emissions. Subsidies for intermediate emission-reducing technologies
may be more effective if they induce greater substitution away from the prevailing high-emission
technology. Furthermore, this tradeoff may shift in favor of BEVs only when a country’s electricity
generation mix becomes sufficiently less carbon-intensive. The fact that many countries continue
to prioritize BEVs suggests that these policies may reflect industrial policy objectives in addition
to environmental concerns. We return to this in the concluding section.
Related literatureOur paper relates to several strands in the literature. First, a large literature
studies the effects of government incentives to promote the demand for electric vehicles. Early
work examines policies targeting HEVs. 4 More recent work studies policies targeting BEVs. 5 This
literature focuses on the impact of promoting a single technology presumed to be the cleanest
available one, initially HEVs and subsequently BEVs.
Our paper instead highlights the importance of comparing the relative effectiveness of subsidies
for the cleanest technology (BEVs) and an intermediate technology (HEVs). We show theoreti-
cally that this comparison depends not only on the technologies’ stand-alone emission savings, but
also on their capacity to induce substitution away from the prevailing high-emission technology
(conventional ICEVs). We then demonstrate empirically for the South Korean passenger vehicle
market that a subsidy for the intermediate technology (HEVs) reduces emissions more effectively
than a subsidy for the cleanest technology (BEVs), because the intermediate technology diverts
more sales from the prevailing high-emission technology (ICEVs).
Second, a related literature evaluates the environmental effects of policies promoting BEVs,
with particular attention to the measurement of emissions. 6 Emissions measurement has become
4See in particular Chandra et al. (2010); Beresteanu and Li (2011); Gallagher and Muehlegger (2011); Sexton
and Sexton (2014); Heutel and Muehlegger (2015); Gulati et al. (2017). Most recently, Langford and Gillingham
(2023) conduct a comprehensive examination of the economic benefits of HEVs in a flexible demand framework for
California.
5Part of this literature focuses on the impact of these policies on BEV adoption (e.g., DeShazo et al., 2017;
Clinton and Steinberg, 2019; Muehlegger and Rapson, 2022; Barwick et al., 2024), as well as the role of heterogeneity
in adoption (e.g., Davis et al., 2025; Archsmith et al., 2022; Gillingham et al., 2023; Bushnell et al., 2022). Other
studies focus more on the implications of these policies for emissions (e.g., Holland et al., 2016; Xing et al., 2021;
Muehlegger and Rapson, 2023; Fournel, 2024; Allcott et al., 2024). Finally, several studies examine the complementary
role of charging networks (e.g., Li et al., 2017; Zhou and Li, 2018; Li, 2019; Springel, 2021; Fournel, 2024).
6See, among others, Holland et al. (2016); Xing et al. (2021); Muehlegger and Rapson (2023); Guo and Xiao
(2023); Meng et al. (2026); Fournel (2024).
3

increasingly comprehensive, as in the recent work of Allcott et al. (2024) and Heid et al. (2025).
Notably, Holland et al. (2016) account for the carbon intensity of electricity generation. But across
U.S. states it plays only a limited role in explaining differences in local environmental benefits,
compared with differences in local pollution damages. We show that carbon intensity becomes
critical when considering the broader range of electricity generation mixes across countries and
over the course of the energy transition. In particular, BEV subsidies become more effective than
HEV subsidies only when the electricity generation mix is sufficiently clean.
Third, there is a broader literature on technical change and the transition from dirty to clean
energy inputs (e.g., Acemoglu et al., 2012, 2016; Papageorgiou et al., 2017). This work focuses on
dynamic innovation incentives and shows that the gains from environmental policy depend on the
input elasticity of substitution and the productivity gap between clean and dirty technologies. Our
work is complementary to this literature: we highlight the importance of demand-side substitution
in consumer markets characterized by imperfect competition. The automobile market provides
a particularly suitable setting because it has been a major focus of environmental policy, with
well-established empirical methodologies to recover detailed substitution patterns across multiple
technologies.
The remainder of this paper is organized as follows. Section 2 presents the theoretical model
highlighting the mechanisms underlying the comparison of subsidies for two emission-reducing
technologies. Section 3 covers relevant industry background, while Section 4 describes the data
used in the empirical analysis. Section 5 introduces the demand model and discusses the estimation
results, and Section 6 conducts the counterfactual analysis comparing emissions under BEV and
HEV subsidies. Finally, Section 7 concludes.
2 Theoretical framework
This section develops a theoretical framework to compare the relative effectiveness of subsidizing
alternative emission-reducing technologies, in our case HEVs and BEVs. The framework serves as
a guide to identify the key channels that operate in our more elaborate empirical model. We start
from a simple setup with three products, homogeneous vehicle usage, and full subsidy pass-through,
and subsequently generalize it to multiple products, heterogeneous vehicle usage, and equilibrium
pass-through under imperfect competition.
2.1 Basic setup
Consider three substitute products, namely an ICEV, an HEV, and a BEV, indexed byj∈
{I, H, B}, in a market of sizeM. Each product generates a negative externality due to emissions
from production and usage. Lete j denote emissions per unit of productj.
Assume that the ICEV represents the dirtiest technology, so thate j < eI forj∈ {H, B}. The
relative cleanliness of the HEV and the BEV depends on the phase of the energy transition. Since
4

the BEV entails higher emissions during production than the HEV, it is possible thate H < eB
in the early phase of the energy transition, when electricity generation still relies heavily on fossil
fuels. By contrast, in the later phase, when the energy mix relies more heavily on renewables, we
havee B < eH .
To reduce emissions, the government considers a subsidy policyτ= (τ I , τH , τB), whereτ j
denotes the per-unit subsidy for productj. Consequently, the net consumer price of productjis
pj =p G j −τ j wherep G j is the gross price set by firms. Lets j(p) denote the market share of product
jas a function of the consumer price vectorp, with ∂sj ∂pj <0 and ∂sk ∂pj >0 fork̸=j. Total emissions
and total government spending are given, respectively, by
E(τ) =M
X
k∈{I,H,B}
eksk(p(τ)) andG(τ) =M
X
k∈{I,H,B}
τksk(p(τ)),
wherep(τ) denotes the vector of consumer prices underτ. For simplicity, assume that the subsidy
policy does not affect firms’ equilibrium gross pricesp G j , so that there is complete subsidy pass-
through and no price response of non-subsidized products to the subsidy policy (as under perfect
competition with constant marginal costs).
First, consider the stand-alone impact of a subsidyτ j for either the HEV or the BEV,j∈
{H, B}, on total emissions. To highlight the role of substitution, recall the commonly used diversion
ratio fromjtok,D j→k ≡ ∂sk/∂pj −∂sj /∂pj ; this is the fraction of sales diverted fromjtokafter a price
increase of productj. Now, define the diverted emissions of productjas:
eD j ≡ X
k̸=j
Dj→k ek.
This is the weighted average of emissions from alternative productsk̸=j, where the diversion
ratios serve as weights. Intuitively,e D j measures the expected emissions that would be generated
by the marginal consumer of productjabsent the subsidy increase.
Applying these definitions, the impact of a subsidy for productj∈ {H, B}on total emissions
is given by:
∂E
∂τj
=−M
X
k∈{I,H,B}
ek
∂sk
∂pj
=M ∂sj
∂pj

eD j −e j  .(1)
This implies that a subsidy for productj∈ {H, B}reduces total emissions if its net diverted
emissions are positive,e D j −e j >0, i.e., if productj’s own emissions are lower than its diverted
emissions.
We now compare therelativeeffectiveness of subsidies for the HEV and the BEV. To this
end, assume that the ICEV is neither taxed nor subsidized, and consider a budget-neutral subsidy
reallocation from the BEV to the HEV. Formally, letτ= (0, τ H , τB) and letτ B =τ B(τH ) be
5

implicitly defined by the government budget constraintG(0, τ H , τB) = ¯G.
In general, a budget-neutral subsidy reallocation from the BEV to the HEV reduces emissions
if the marginal abatement return of an HEV subsidy, −∂E/∂τ H ∂G/∂τ H , exceeds that of a BEV subsidy; see
Appendix A.1. Under a baseline policy with no subsidies, this comparison amounts to the condition
in the following proposition.
Proposition 1.Consider the baseline policy with no subsidies,τ= (0,0,0). A subsidy for product
j∈ {H, B}, financed by a tax on productk∈ {H, B}withk̸=j, reduces emissions if and only if
− 1 sj ∂sj ∂pj (eD j −e j)>− 1 sk ∂sk ∂pk (eD k −e k).(2)
Proof.See Appendix A.1.
Proposition 1 implies that subsidizing the HEV, while taxing the BEV to maintain a zero-net
budget, may be more effective than the reverse policy. This occurs if the HEV subsidy generates
sufficiently large demand responses, measured by the own-price semi-elasticity (− ∂sj ∂pj 1 sj ), and/or
net diverted emissions (e D H −e H ) relative to the corresponding BEV subsidy.
In the special case of symmetric logit demand, inequality (2) reduces to the simple condition
ej −e k <0. For example, an HEV subsidy is more effective than a BEV subsidy whenever HEV
emissions are lower than BEV emissions (as in the early phase of the energy transition). Under more
flexible substitution patterns, an HEV subsidy may be more effective even when HEV emissions
are higher than BEV emissions, provided that it generates more diversion away from ICEVs.
To further isolate the role of diversion under flexible substitution patterns, suppose that demand
responses are identical across technologies,− ∂sj ∂pj 1 sj =− ∂sk ∂pk 1 sk . In this case, an HEV subsidy is more
effective than a BEV subsidy if and only ife H −e B < eD H −e D B . This inequality holds when the
emissions gape H −e B is sufficiently small or negative and/or when the HEV diverts relatively
more demand from the ICEV than does the BEV. 7 In our empirical analysis, we show that these
conditions are currently satisfied in the South Korean new passenger vehicle market.
2.2 General framework
Proposition 1 imposes simplifying assumptions to highlight the key factors that determine the
relative effectiveness of alternative subsidy policies. Here, we extend the framework along the four
dimensions below.
First, we allow for multiple products within each fuel type, which generates scope for within-
type substitution in response to subsidies. However, such substitution may contribute relatively
little to emissions changes, because products of the same fuel type share similar emissions. Second,
we include additional fuel-type categories, allowing for multiple ICE vehicle types such as gasoline,
7To make this link more explicit, we derive an equivalent condition that is expressed directly in terms of the
diversion ratios from the HEV and the BEV to the ICEV in Appendix A.2.
6

diesel, and LPG. Third, we allow for nontrivial subsidy pass-through under imperfect competi-
tion between multi-product price-setting firms. Fourth, we allow usage emissions to vary across
consumers through heterogeneous annual mileage.
Accordingly, we extend the basic setup as follows. Products are partitioned intoGgroups
based on their fuel types, indexed byg. LetJ g denote the set of products with fuel typeg, and
letS g = P j∈Jg sj denote the aggregate market share of fuel typeg. Letτ g denote the per-unit
subsidy common to all products with fuel typeg, and let Θ j,g =− ∂pj ∂τg denote the pass-through rate
of subsidyτ g to the price of productj.
To account for individual-specific emissions,eij, stemming from heterogeneous consumer mileage,
we use the following notation. LetD i j→k =− ∂sik/∂pj ∂sij /∂pj denote the individual diversion ratio, and let
eD ij = P k̸=j Di j→k eik denote the individual diverted emissions of productj. Finally, letF(i) denote
the consumer distribution, defined over observed demographics (e.g., income and mileage) as well
as unobserved heterogeneity.
Product-level emissions and product-level diverted emissions are then defined as weighted av-
erages of individual emissions and individual diverted emissions, respectively:
ej =
Z
ωijeij dF(i) ande D j =
Z
ωijeD ij dF(i),(3)
where the weights are given by
ωij = ∂sij/∂pj R ∂sij
∂pj dF(i)
= ∂sij/∂pj
∂sj/∂pj
.(4)
Intuitively, consumers who are more responsive to changes in the price of productj, relative to
the aggregate response, receive greater weight in the construction of these emission metrics; see
Appendix A.3 for the formal derivation. Note that the weights in (4), which define product-level
emissions and diverted emissions, closely resemble those defining product-level diversion ratios in
Conlon and Mortimer (2021). This is because both are derived in the context of a price change for
productj. 8
This setup yields the following generalization of Proposition 1:
Proposition 2.Consider the baseline policy with no subsidies. A subsidy for fuel typeg 1 ∈ {H, B},
financed by a tax on fuel typeg 2 ∈ {H, B}withg2 ̸=g 1, reduces emissions if and only if
− 1 Sg1
GX
g=1
X
j∈Jg
Θj,g1
∂sj
∂pj
(eD j −e j)>− 1 Sg2
GX
g=1
X
j∈Jg
Θj,g2
∂sj
∂pj
(eD j −e j).(5)
8Furthermore, in the special case of homogeneous mileage,e ij =e j for alliandj, it can be verified that
eD j = X
k̸=j
Z
ωijDi j→k dF(i)

ek =
X
k̸=j
Dj→k ek.
This implies that the aggregate diverted emissions of productjare separable in the diversion ratiosD j→k and the
emissionse k (even under consumer heterogeneity in other dimensions than mileage).
7

Proof.See Appendix A.3.
Similar to condition (2), condition (5) compares the marginal abatement returns of subsidies
for two fuel types,g 1 andg 2. The marginal abatement return of a subsidy for fuel typeg, −∂E/∂τ g ∂G/∂τ g ,
still depends on demand responses and net diverted emissions. However, these are now weighted by
the pass-through rates within and across fuel types. One may expect high pass-through rates, Θ j,g,
for productsj∈J g (within-fuel-type pass-through), and lower pass-through rates for products
j /∈Jg (cross-fuel-type pass-through). 9 Furthermore, net diverted emissions (e D j −e j) now ex-
plicitly account for heterogeneity in emissions, demand responses, and substitution patterns across
consumers. If these sources of heterogeneity are systematically correlated, net diverted emissions
may differ between the heterogeneous-mileage model and its homogeneous counterpart. 10
Proposition 2 is based on a baseline policy of no subsidies (τ=0) to simplify algebraic expres-
sions. Extending the analysis to incorporate existing subsidies for HEVs or BEVs is straightforward
and yields a generalization of condition (5) that includes additional terms reflecting existing subsidy
expenditures, as shown in Appendix A.3.
2.3 Empirical implementation
The empirical model implements the general framework discussed above and quantifies its implica-
tions. Two key empirical components are the measurement of emissions and the characterization
of demand substitution patterns across fuel types.
On the emissions side, we draw on the environmental literature to measure lifecycle emissions
as the sum of production and usage emissions. Usage emissions depend not only on vehicle char-
acteristics but also on annual mileage, generating heterogeneity in emissions within fuel types and
amplifying differences across fuel types.
On the demand side, capturing flexible substitution patterns requires accounting for hetero-
geneity in consumer characteristics, in particular annual mileage. High-mileage consumers are
more likely to substitute away from ICEVs toward subsidized alternatives with lower operating
costs (HEVs and BEVs), as they benefit more from lower fuel expenditures.
Finally, to highlight the key mechanisms, our theoretical framework has so far focused on com-
paring themarginaleffects of changing per-unit subsidies across fuel types. In practice, however,
we compare thetotaleffects of alternative budget-neutral subsidy policies. Specifically, we ask
9In the special case where own-fuel-type pass-through rates are all equal to one and cross-fuel-type pass-through
rates are all equal to zero, condition (5) simplifies to
− 1 Sg1 X j∈Jg1 ∂sj ∂pj (eD j −e j)>− 1 Sg2 X j∈Jg2 ∂sj ∂pj (eD j −e j).
In this case, the marginal abatement return of a subsidy for fuel typegdepends only on the demand responses and
net diverted emissions within groupg.
10For example, if high-mileage consumers, who have greater scope for emission reductions (highere D ij −e ij),
are more price-sensitive (higher
∂sij
∂pj ) than low-mileage consumers, aggregate net-diverted emissions exceed those
predicted by the homogeneous model.
8

Table 1: New passenger vehicle sales in 2023
Fuel type
Manufacturer Gasoline Diesel LPG Hybrid + BEV HFCV Total
Hyundai Motor Group 621 548 83 205 45 451 278 525 70 359 4 326 1 103 414
Others 199 162 21 312 7 710 112 368 45 180 - 385 732
Total 820 710 104 517 53 161 390 893 115 756 4 326 1 489 363
+ Hybrid refers to the combined sales of HEVs and PHEVs.
Notes: This table reports sales (i.e., the number of vehicles sold) by each fuel type in 2023. Source: Korea Automobile
& Mobility Association (KAMA).
which of the two fuel-specific policies (BEVs vs. HEVs) is more effective at reducing emissions. To
answer this question, we now turn to our empirical analysis. 11
3 Industry background
3.1 Fuel type segments in the South Korean car market
Automobile ownership in South Korea exceeds one vehicle per household, reaching 1.13 in 2023. In
that same year, nearly 1.5 million new passenger vehicles were sold, ranking South Korea among
the largest automotive markets globally (Statista, 2024).
The South Korean market features three primary categories of conventional ICEVs: gasoline,
diesel, and LPG. Additionally, several categories utilizing new technologies are available: BEVs,
HEVs, plug-in hybrid vehicles (PHEVs), and hydrogen fuel cell vehicles (HFCVs). BEVs are
powered entirely by an onboard rechargeable battery and do not contain an ICE. By contrast,
HEVs combine a conventional ICE with an electric motor and a small battery pack to enhance
fuel efficiency through three key mechanisms: regenerative braking, engine optimization, and a
stop-start system (see Appendix B for details). PHEVs can be viewed as an extension of HEVs:
like HEVs, they combine an ICE with an electric drivetrain, but they also include a larger battery
that can be plugged into an external power source (the grid). Finally, HFCVs generate electricity
through a fuel cell stack that converts hydrogen gas into electrical energy.
Table 1 reports sales volumes by fuel type for 2023. Gasoline-powered vehicles constituted the
majority of newly registered passenger cars, capturing a 55% sales share. Hybrids (including both
HEVs and PHEVs) were the second most popular category, with a share exceeding 25%. This
segment was dominated by HEVs, as fewer than 10 000 PHEVs were sold. While BEVs and diesel
cars each accounted for approximately 7% of total sales, sales of HFCVs totaled only around 4 000
units. Additionally, the sales share of the Hyundai Motor Group, which comprises three brands
(Hyundai, Kia, and Genesis), was approximately 75%, while the remainder was distributed among
other domestic manufacturers and imported brands.
It is instructive to consider the evolution of sales shares by fuel type during our sample period
11Appendix A.4 provides a theoretical comparison of the total effects of two subsidy policies.
9

(2012–2023); for further information, see Figure G3 in Appendix G. Gasoline vehicles experienced
an initial decline followed by a recovery, thereby maintaining their dominance. By contrast, diesel
cars, which were favored until the mid-2010s because of their relatively high fuel economy, have seen
their popularity plummet in recent years due to the Dieselgate scandal and increasing regulatory
pressure from CAFE standards. 12 As manufacturers phased out diesel variants, the HEV sales
share rose more than eightfold, from 2.7% in 2015 to 23.1% in 2023, whereas the BEV sales share
stagnated at only 6.5% in 2023, 0.3 percentage points lower than in the previous year. The growth
in the HEV share and the stagnation of the BEV share occurred despite the removal of HEV
subsidies and substantial subsidies for BEVs (discussed further below).
3.2 Greenhouse gas emissions of vehicles
The GREET model is a standard, comprehensive analytical tool used in the transportation sector
to measure life-cycle GHG emissions, also referred to as cradle-to-grave emissions. 13 As Figure 1
illustrates, a vehicle’s life-cycle GHG emissions consist of two components: vehicle-cycle emissions
and fuel-cycle emissions, the latter also referred to as well-to-wheels emissions.
The first component, vehicle-cycle GHG emissions, is generated during the production, disposal,
and recycling of the vehicle and its battery. This component is independent of the vehicle owner’s
mileage. The second component, fuel-cycle GHG emissions, is associated with producing and
consuming the fuel required to drive 1 km, multiplied by the vehicle owner’s total mileage. The
emissions per km can be further divided into well-to-tank emissions and tank-to-wheels (or tailpipe)
emissions. The former are associated with the extraction, processing, transportation, refining, and
distribution of fuels for ICEVs (including the more efficient HEVs), and with electricity generation
and transmission for BEVs. The latter arise from actual fuel combustion during vehicle operation.
Since BEVs generate no tailpipe emissions, their fuel-cycle emissions per km (in g CO2e/km) consist
solely of well-to-tank emissions, calculated by dividing the emission factor at final consumption (in
g CO2e/kWh) by the vehicle’s fuel economy (in km/kWh). 14
As an illustration, consider a 2020 Toyota Camry HEV whose vehicle-cycle emissions are 6.3
tonnes of CO 2e and fuel-cycle emissions per km are 130.14 g of CO 2e.15 Assuming a 15-year
holding period and an annual mileage of 12 000 km, the cumulative fuel-cycle emissions amount to
23.4 tonnes of CO 2e (15×12 000×130.14×10 −6). The total 15-year GHG emissions are therefore
29.7 tonnes of CO 2e (6.3 + 23.4).
12Since the initial implementation of the Corporate Average Fuel Economy (CAFE) standards in South Korea in
2012 (17 km/L for fuel economy and 140 g/km for GHG emissions), the requirements have been gradually tightened
annually. By 2021, these standards had reached 24.3 km/L for fuel economy and 97 g/km for GHG emissions.
13GREET stands for Greenhouse gases, Regulated Emissions, and Energy use in Technologies. The GREET model
was developed by Argonne National Laboratory (Elgowainy et al., 2016; Kelly et al., 2023).
14The GHG emission factor at final consumption represents the GHG emissions per unit of electricity, accounting
for energy losses incurred during transmission and distribution through the grid.
15Appendix E.1 describes in detail the vehicle-cycle and fuel-cycle emission calculations for each product-year
combination in our sample.
10

Figure 1: The life-cycle GHG emissions of a vehicle
Life-cycle
(Cradle-to-grave)
Vehicle-cycle
Sources of emissions
• Manufacturing (frame + engine + battery)
• Recycling  and disposal
Summary
• High for BEV due to battery production
• Larger vehicle (e.g., SUV) has a higher value
• Does not depend on consumer’s mileage
Fuel-cycle
(Well-to-wheels)
Summary
• Depend on the vehicle's emissions per km and
the consumer's annual mileage
Well-to-tank
Sources of emissions
• Fuel extraction, refinement, and distribution
Summary
• For BEVs, emissions depend on the GHG
emission factor of electricity
• Lower for HEVs compared to other ICEVs due to
their higher fuel efficiency
Tank-to-wheels
(Tailpipe)
Sources of emissions
• Fuel combustion during vehicle operation
Summary
• Zero for BEVs
• Lower for HEVs compared to other ICEVs due to
their higher fuel efficiency
Notes: Based on the GREET model in Kelly et al. (2023), this figure decomposes the life-cycle GHG emissions of a
vehicle into three parts and provides the sources of emissions for each part.
3.3 BEV and HEV subsidy policy
In accordance with the Paris Agreement, the South Korean government established its Nationally
Determined Contribution (NDC) in June 2015. According to the “2050 Carbon Neutrality Scenario”
and the upgraded NDC announced in October 2021, the government aims to reduce GHG emissions
in the transportation sector by approximately 40% by 2030. To achieve this, the government has
been bolstering its support for BEVs.
More specifically, it directly installs electric vehicle chargers and subsidizes private firms to
install them; in 2023, 300 billion KR W (260 million USD) was budgeted for this purpose. 16 It
also determines the national BEV purchase subsidies. The amount of these subsidies was initially
more or less uniform across nameplates, but began to vary in 2018 based on vehicle attributes such
as fuel economy (energy efficiency), maximum range, size, battery efficiency, and price. Subsidies
also depend on whether automakers actively participate in installing charging stations and apply
advanced, up-to-date technologies in their vehicles. For example, the 2023 formula for the national
BEV purchase subsidy is given by:
h
attribute part + infrastructure part + innovation part
i
×price multiplier,
16The average exchange rate between 2012 and 2023, 0.86 USD per 1 000 KR W, is used throughout the paper.
11

Table 2: BEV purchase subsidies and price
Total subsidy Number of Per-vehicle Acquisition Subsidy
value BEVs sold subsidy price share
Year (Billion KR W) (Million KR W) (Million KR W)
2012 0.13 4 32.67 49.01 0.67
2013 3.16 125 25.30 44.72 0.57
2014 11.66 507 23.00 46.45 0.51
2015 45.54 2 042 22.30 45.96 0.50
2016 50.33 2 612 19.27 43.35 0.45
2017 140.53 7 149 19.66 42.38 0.49
2018 374.99 22 183 16.90 46.64 0.38
2019 337.61 23 163 14.58 49.72 0.31
2020 251.83 19 100 13.19 55.07 0.26
2021 346.57 35 684 9.71 58.83 0.18
2022 512.94 62 172 8.25 59.72 0.15
2023 464.70 65 851 7.06 58.06 0.14
Total 2 540.00 240 592 10.56 55.75 0.21
Notes: This table reports the total subsidy value, the number of BEVs registered, the sales-weighted average per-
vehicle purchase subsidy, the sales-weighted average acquisition price, and the sales-weighted average subsidy share
for each year between 2012 and 2023. All monetary values are in 2020 constant KR W (1 000 KR W≈0.86 USD).
Source: official electric vehicle policy websites of the Korean government, official policy documents from the Ministry
of Environment, and news articles for figures from the early 2010s.
where the price multiplier equals 1 for vehicles priced below 57 million KR W (49 thousand USD),
0.5 for those priced between 57 million and 85 million KR W (73 thousand USD), and 0 for vehicles
priced above 85 million KR W. As a result, some BEVs—mostly German models—have not been
eligible for purchase subsidies due to their high prices. In 2023, for example, 25 out of 36 BEV
nameplates (e.g., Kia EV6 and Tesla Model 3) were eligible for subsidies, whereas the remaining
11 nameplates were not; see Table G1 in Appendix G.
Local governments provide additional purchase subsidies, which vary across provinces and years,
generating cross-province variation in the total (national + local) subsidy per vehicle. 17 Table 2
summarizes the evolution of BEV subsidies. The per-vehicle subsidy has declined from almost
33 million KR W in 2012 to around 7 million in 2023; on average, the purchase subsidy covered at
least 50% of the vehicle price up until 2015, but 15% or less since 2022. 18 In contrast, total subsidy
expenditure has increased rapidly due to the rising number of registered BEVs.
The Korean government introduced HEV purchase subsidies of 1 million KR W per vehicle
in 2009 (less than 3% of the purchase price), halved them in 2018, and discontinued them the
following year (with PHEV subsidies ending in 2021). Consequently, subsidies for HEVs have been
significantly lower than those for BEVs; the sales-weighted average per-vehicle subsidy for HEVs
(170 000 KR W or 147 USD) between 2012 and 2023 is negligible compared to that for BEVs (10.56
17Provinces are the first-tier administrative divisions in South Korea. Figure G2 in Appendix G illustrates how
they are geographically defined.
18Section 4 provides details on how we construct the BEV purchase subsidies at the year-province-nameplate level
used in this study.
12

million KR W or 9 100 USD).
In addition to direct purchase subsidies, buyers of BEVs and HEVs have also been eligible for
tax credits since 2012, ranging from 1 million KR W (860 USD) to 4 million KR W (3 440 USD),
with BEVs receiving roughly two to three times the amount provided for HEVs. Tax credits for
HEVs have been gradually reduced since 2020, as the Korean government plans to phase them out
by 2026. In contrast, tax credits for BEVs are expected to remain relatively stable at least until
the end of 2026.
4 Data
4.1 Main dataset
We combine datasets from multiple sources. The primary dataset is provided by ConsumerInsight,
a leading automotive marketing and research firm in South Korea. For each of the 17 provinces
between 2012 and 2023, it contains the annual number of registrations and sales revenues for each
unique combination ofbrand×nameplate×model name×model year×fuel type×various car
attributes (e.g., size, defined by the combination of width, height, and length; fuel economy; engine
displacement; and seating capacity). One advantage of our data is that sales revenues account for
manufacturer promotions at the point of sale as well as the costs of miscellaneous options selected
by consumers. Therefore, the vehicle price, obtained by dividing sales revenue by the number of
registrations and then deflating it using the CPI (2020 = 100), is closer to the actual transaction
price than the manufacturer’s suggested retail price (MSRP) often used in the literature.
We subtract the total subsidy from the price of a BEV or HEV to obtain the vehicle’s net
price. In doing so, we make two assumptions. First, we assume that all consumers of BEVs and
HEVs applied for and received the purchase subsidies, although subsidies are reimbursed only to
purchasers upon request. Second, we assume that the province- and year-specific cap on the total
number of BEVs eligible for subsidies in each province and year is not binding. This assumption
is reasonable, given that local governments typically relax or extend the cap during the year when
the demand for subsidized vehicles exceeds the initially set cap. According to Table 3, the average
net price of BEVs is 45 million KR W (approximately 40 thousand USD), which is 22% and 54%
higher than the average prices of HEVs and gasoline cars, respectively.
The sales data include six domestic brands (Hyundai, Kia, KG Mobility, GM Korea, Renault Ko-
rea, and Genesis) and seven foreign brands (Mercedes-Benz, BMW, Volkswagen, Audi, Toyota,
Lexus, and Tesla). Together, these 13 brands account for 93% of total sales during the sample pe-
riod. The data also report basic vehicle attributes such as fuel type, fuel economy, and body style,
among others. We calculate fuel cost per km (1,000 KR W per km) by dividing the province/year-
level fuel price by fuel economy (km per liter for ICEVs and km per kWh for BEVs). 19 We sup-
19Fuel prices for ICEVs, disaggregated by province and year, are obtained from OPINET (Oil Price Information
Network). The annual charging rates for BEVs (expressed in KR W per kWh) are sourced from official announcements
by the Ministry of Environment (Ministry of Environment (ME), 2024).
13

plement the dataset with additional vehicle specifications, including horsepower, curb weight, and
driving range for BEVs, collected from two comprehensive South Korean automotive databases. 20
We define a product as a unique combination ofbrand×nameplate×fuel type. For in-
stance, Toyota (brand)–Camry (nameplate)–HEV (fuel type) represents a product. We also define
a market as a unique combination of province and year. Accordingly, we aggregate the data to
the product-market level and use average attributes, weighted by the number of registrations, as
the representative product characteristics. According to the National Travel Survey conducted by
the Ministry of Land, Infrastructure, and Transport in 2014, 21 the average replacement cycle for
passenger cars in South Korea is around six years. Therefore, we assume that the market size
associated with provinceris one-sixth of the average annual number of registered passenger cars
in that province during the sample period. The outside option includes buying used vehicles or
continuing to drive currently owned vehicles. 22
From the data, we remove products with cumulative sales below 100 units during the sample
period. We also exclude PHEVs and HFCVs, given their negligible market shares in South Korea.
Finally, we omit observations from Sejong City (a special self-governing city established in July
2012) as reliable income distribution data are unavailable for this region. The final sample consists
of 34 629 observations from 366 products, among which 40 and 34 are BEVs and HEVs, respectively.
Table 3 presents the sales-weighted average product attributes by fuel type. There is a clear
negative correlation between acquisition prices and driving costs. BEVs are the most expensive,
with an average acquisition price of 55.7 million KR W (48 thousand USD), yet they offer the lowest
fuel cost at 50 KR W per km. HEVs are significantly cheaper than BEVs (by 33% in terms of
acquisition price and by 17.8% in terms of net price), and exhibit the highest fuel economy (16.8
km/L) among ICEVs. Consequently, consumers may view HEVs as viable substitutes for BEVs.
The table also shows that BEVs are the heaviest due to their batteries, whereas diesel cars are the
largest since they are mostly SUVs.
4.2 Supplementary datasets
GHG emissionsWe construct data on fuel-cycle emissions per km for each product-year com-
bination in our sample, as well as vehicle-cycle emissions for products sold between 2020 and 2023,
by aggregating information from various sources. Details of these sources and a full description of
the GHG emission calculations are provided in Appendix E.1.
Table 3 shows that sales-weighted average fuel-cycle emissions per km are lowest for BEVs (89 g
CO2e/km), as they generate no tailpipe emissions. HEVs also exhibit significantly lower fuel-cycle
emissions per km (135 g CO 2e/km on average) than conventional ICEVs (200–213 g CO 2e/km)
through their superior fuel economy, as explained in Section 3.2. In contrast, the vehicle-cycle
emissions of BEVs are 37.7%–51.7% higher than those of HEVs and conventional ICEVs. This is
20The two sources are CARISYOU and Danawa.
21Source:https://www.ktdb.go.kr/www/selectBbsNttView.do?key=42&bbsNo=7&nttNo=2688
22Rather than interpreting public transportation as part of the outside option, we let its availability influence
consumer mileage.
14

Table 3: Vehicle attributes by fuel type
Fuel type
Attribute Gasoline Diesel LPG HEV BEV All
Price (Mil. KR W) 29.37 35.87 25.48 37.27 55.71 32.33
Net price (Mil. KR W) 29.37 35.87 25.48 37.10 45.14 32.11
Fuel cost per km (1 000 KR W/km) 0.14 0.11 0.15 0.09 0.05 0.12
Fuel economy (km/L, km/kWh) 12.53 13.27 9.28 16.84 5.16
Size (m3) 12.29 14.96 13.18 13.68 13.21 13.27
Power (hp) 168.14 180.73 152.50 218.47 233.57 176.61
Weight (kg) 1 371.43 1 775.42 1 473.53 1 628.90 1 823.79 1 528.04
Acceleration (hp/kg) 0.12 0.10 0.10 0.13 0.13 0.11
GHG emissions
-Fuel-cycle (g CO2e/km) 199.87 212.88 204.45 134.85 89.21 196.60
-Vehicle-cycle (tonnes CO2e) 6.99 7.70 7.11 7.16 10.61 7.29
Observations 15 551 11 854 2 096 3 147 1 981 34 629
Notes: This table reports sales-weighted average vehicle attributes by fuel type in our sample data (2012–2023, 16
provinces). Fuel economy is expressed in km/kWh for BEVs and km/L for all other fuel types. Fuel-cycle GHG
emissions are measured on a per-kilometer basis, while vehicle-cycle GHG emissions are calculated for products sold
during the 2020–2023 period.
largely because battery production is emissions-intensive and batteries have become heavier over
time to support longer driving ranges.
Consequently, the emissions gap between HEVs and BEVs is relatively small given current
technology. Assuming six years of ownership and an annual mileage of 12 000 km (the average
replacement cycle and annual mileage in South Korea, respectively), the emissions from an HEV
(17 tonnes of CO 2e) are approximately the same as those from a BEV in our sample between
2020 and 2023. Extending the operating period to 15 years, the average passenger vehicle lifespan
in South Korea, results in life-cycle emissions for BEVs of 26.7 tonnes of CO 2e, compared with
31.4 tonnes for HEVs, a difference of only 15%.
BEV purchase subsidiesWe collect BEV purchase subsidies at the year–province–nameplate
level since 2020 from the official electric vehicle policy website of the Korean government. 23 In
some provinces, local subsidies vary across counties within the province, although such variation
is not substantial. In these cases, we proxy the local subsidy using figures from the county where
the majority of the population resides or where most BEVs are registered within the province. For
years prior to 2020, we rely on official policy documents, when available, issued by the Ministry of
Environment, as well as news articles. Figures G4 and G5 in Appendix G show substantial variation
in total (national + local) BEV subsidies across nameplates and across provinces, respectively, for
each year (2016–2023).
23Source: Zero-Emission Vehicle Integrated Portal
15

Second-choicesEach of the two consumer surveys conducted by ConsumerInsight in 2018 and
2023 contains the automobile purchase decisions of respondents who purchased new vehicles within
the two years preceding the survey. Importantly, the survey data record the second choice of
each respondent, that is, the vehicle they would have purchased if the primary choice had not
been available. After excluding respondents whose primary vehicles are not listed in our sales
data or who did not report a second choice, we retain 4,035 and 4,145 consumers for 2018 and
2023, respectively. The two surveys oversample consumers who purchased vehicles with low market
shares such as BEVs, while undersampling gasoline and diesel vehicle buyers. We use the inverse
sampling weights for each survey respondent provided by ConsumerInsight to correct for sampling
imbalances in the estimation process, as detailed in Appendix D.
Mileage informationIn South Korea, all registered passenger vehicles are required to undergo
a regular inspection every two years. The inspection interval is four years for newly purchased
vehicles and one year for vans, trucks, and similar vehicles. The Korea Transportation Safety
Association (KTSA) keeps records of all vehicle inspections. From these publicly available data, we
obtain the following information: (i) inspection year, (ii) annual mileage, (iii) fuel type, and (iv)
province in which the vehicle is registered.
According to Figure 2, HEVs tend to have higher mileage than vehicles with other fuel types,
indicating that consumers who drive longer distances value the high fuel economy of HEVs. In-
terestingly, the average mileage of BEVs increased sharply during the sample period. Potential
explanations include growth in battery capacity and the expansion of the electric charging network.
The exceptionally high average mileage observed across all fuel types in 2021 is likely attributable
to the increase in individual travel demand during the COVID-19 pandemic (2020 to 2021). Finally,
note that people in metropolitan cities tend to drive less than residents of less densely populated
provinces; see Table G2 in Appendix G.
Additional datasetsWe obtain household income data from the Korean Labor and Income
Panel Study (KLIPS) to estimate the corresponding log-normal income distribution for each market
(province–year). We then simulate 1 000 individuals per market from these estimated distributions.
We also obtain a charger dataset from the Korean Environment Corporation. Following Springel
(2021), we define the interaction between the log of the number of chargers in a market and a BEV
dummy as the infrastructure network variable. A full description of these datasets is provided in
Appendix C.
16

Figure 2: Mileage trends
Notes: This figure presents the average annual mileage trend for each fuel type.
5 Demand estimation
5.1 Model for consumer demand
Recall that the marketmrefers to the province and year. The indirect utility of consumeriin
marketmfrom purchasing productjis given by
uijm =x jmβi −α ipjm +ξ jm +ε ijm,(6)
wherep jm denotes the price net of subsidies, andx jm is a vector of product attributes, including
cost per km, acceleration, size, infrastructure network, market entry and exit indicators, and fixed
effects for nameplates, provinces, and fuel type×years. The latter account for time-varying, fuel-
type-specific demand shocks, such as the Dieselgate scandal or non-subsidy benefits for HEVs and
BEVs (e.g., parking fee discounts and designated parking zones). Remaining unobserved factors
are captured by the mean-zero structural error termξ jm, whileε ijm represents an i.i.d. extreme
value distributed idiosyncratic taste shock.
We specify the individual-specific price coefficient and valuation of attributekas:
αi = α yi ,
βik =β k +π k mileagei +σ kvik,
(7)
wherey i and mileage i denote consumeri’s annual income and daily mileage, respectively, and
vik captures remaining unobserved heterogeneity in the valuation of attributek. We allowπ k to
17

be non-zero for the four main fuel-type dummy variables: diesel, gasoline, BEV, and HEV. Our
specification therefore captures how tastes for these four fuel types compared to the outside option
vary with mileage. We also allowσ k to be non-zero for the following variables: the four fuel-type
dummy variables, the SUV indicator, and driving cost per km.
Suppressing the market subscriptmfor brevity, the indirect utility in (6) can then be decom-
posed into three terms:
uij =δ j +µ ij +ε ij,
δj =x jβ+ξ j,
µij =−α pj yi + X k (πk mileagei +σ kvik)x (2) jk , (8)
wherex (2) jk denotes the vector of attributes for which we specify heterogeneity.
We normalize the mean utility of the outside good to zero (δ 0 = 0) and defineDas a vector of
demographic variables (income and mileage). Assuming independence amongD,v, andε, consumer
i’s choice probability for productj(s ij) and the market share of productj(s j) are
sij = exp (δj +µ ij) 1 + P ℓ∈J exp (δℓ +µ iℓ)
sj =
Z
D
Z
v
sij dF(v)dF(D),
(9)
whereJdenotes the set of available inside goods,F(v) represents the (normal) distribution of taste
shocks (v), andF(D) denotes the empirical distribution function of demographic characteristics
(D). Because the empirical distributions of income and mileage come from separate sources, we
further assume independence between these two demographic variables.
5.2 Estimation and identification
Given the vector of nonlinear utility parametersθ= (α,{π k},{σ k}), there is a unique vector of
mean utilities,δ(θ), that equates the observed market shares with the simulated ones (Berry, 1994;
Berry et al., 1995):
sj = 1 N NX i=1 exp (δj +µ ij(θ)) 1 + P ℓ∈J exp (δℓ +µ iℓ(θ)) ,∀j∈J
where we setN= 1 000, i.e., 1 000 draws from the income distribution, 1 000 draws from the mileage
distribution, and 1 000 scrambled Halton draws in each market. By solving the equations using a
fixed point procedure (Berry et al., 1995), we obtain the structural error term as a function of the
utility parameters:ξ j(θ) =δ j(θ)−x j ˆβ(θ), where ˆβ(θ) is recovered from a linear GMM regression
ofδ j(θ) onx j.
Our generalized method of moments (GMM) estimator is derived from two sets of sample
moments. First, we construct a set of aggregate moments. Including the market subscript again,
18

assume that the structural error term is mean independent of a vector of instrumental variables
Zjm for productjin marketmto obtain the following moments:
G1(θ) = 1 Np X j,m ξjm(θ)Zjm,(10)
whereN p is the number of products across markets. In addition to the vector of (non-price) product
attributes, we include two cost shifters as instruments for price: (i) the import tariff rate and (ii)
the raw material price interacted with vehicle weight. Due to the free trade agreement with the
European Union in the early 2010s, import tariffs on German cars progressively declined from
2010 to 2016 with variation by fuel type and engine displacement. Tariffs on Japanese HEVs also
declined slightly in the early 2020s. Based on market reports indicating that the production of a car
requires approximately five times as much iron as aluminum, we calculate the second instrument
as (0.2×aluminum price + iron ore price)×weight. Because the transmission of a cost shock takes
time, we use one-year lagged tariff rates and raw material prices.
Second, for the identification of mileage and fuel-type interaction parameters and the standard
deviations of tastes, ({π k},{σ k}), we construct micro moments,G 2(θ) (e.g., Berry et al., 2004;
Petrin, 2002; Conlon and Gortmaker, 2025; Grieco et al., 2024), using ConsumerInsight’s 2018 and
2023 consumer surveys and KTSA’s vehicle inspection data. More specifically, we compute the
correlation between the product attributes of the first and second choices from the survey data and
match it to the corresponding moment from the model. We also compute the average daily mileage
of each fuel type from the vehicle inspection data and match it to the corresponding model-predicted
moment. Appendix D provides a full description of the construction of the micro moments using
our micro datasets.
We form the objective function by stacking the sample moments. The GMM estimator is
ˆθ= arg min
θ
G(θ)′W G(θ),(11)
where
G(θ) =
"
G1(θ)
G2(θ)
#
, W=
"
W1 0
0W 2
#
,(12)
andW 1 andW 2 are the weighting matrices corresponding to the first and second sets of moment
conditions, respectively. We carry out the estimation usingPyBLP(Conlon and Gortmaker, 2020).
5.3 Results
Table 4 presents the demand parameter estimates. We first consider a simple logit demand model
with homogeneous valuations for product attributes,β i =βandα i =α/ y, where y is the average
income in the market. The first column is based on an OLS regression, while the second column
uses our two cost shifters as instruments for price (i.e., the import tariff rate and the raw material
19

price interacted with vehicle weight). 24 As expected, the IV estimate of the price coefficientαis
larger than the OLS estimate (in absolute value). OLS implies inelastic product-level own-price
elasticities, whereas the IV estimates imply plausible median and average elasticities of, respectively,
-5.5 and -4.3. The coefficients of other attributes are mostly significant and of the expected signs.
To appreciate the role of consumer heterogeneity in the valuation of fuel types, we also estimate
a nested logit demand model, as in Berry (1994). We partition the products in six fuel type groups:
gasoline, diesel, LPG, HEV, BEV, and the outside option. The model includes a nesting parameter
ρ, capturing taste correlation between products of the same group. We estimate the model using the
same cost shifters as price instruments, and the number of products per group as an instrument for
the nesting parameter. We estimate a statistically significant nesting parameter of 0.677, indicating
that consumers perceive vehicles of the same fuel type as much closer substitutes than vehicles of
different fuel types. The median and average own-price elasticities are comparable with those of
the IV logit model. For more details, see Table G3 in Appendix G.
The next columns of Table 4 show the results for two random coefficients logit specifications,
after incorporating micro moments into our GMM estimation. The third and fourth columns assume
that mileage does not affect consumers’ valuation of fuel type and setπ k = 0. The estimates of
the price coefficient and the mean coefficients (α, β) are consistent with the benchmark results
reported in the first two columns. Moreover, the estimates of the standard deviations ({σ k}) are
all statistically significant, indicating that a consumer with a higher taste draw for fuel typek(v ik)
places a higher value on vehicles of that fuel type relative to others. This finding is consistent with
the statistically significant nesting parameter, and suggests that vehicles with the same fuel type
are closer substitutes for one another.
The last three columns present the results from the full model, which adds the interaction be-
tween mileage and each fuel type ({πk}). This addition does not substantially affect the parameter
estimates of the more restrictive specification in the previous two columns (α,β, and{σ k}).25 The
magnitudes and significance of the interaction parameters reveal that consumers’ fuel-type valua-
tions depend on driving distance: the higher the mileage, the higher the value placed on the more
energy-efficient HEVs, diesel vehicles, and especially BEVs. In Section 6, we show that failing
to account for this consumer mileage heterogeneity leads to an underestimation of the emission
reduction effects of a vehicle subsidy policy.
The sales-weighted average own-price elasticities are−5.38 and−5.91 for the specifications
without and with mileage heterogeneity, respectively, which are larger than the earlier reported
average of−4.3 for the restricted logit model. These estimates are broadly comparable to those
reported in previous studies, for example,−5.32 for the Korean market during 1996–2009 (Ohashi
and Toyama, 2017) and−5.06 for the U.S. market during 1980–2018 (Grieco et al., 2024). A
breakdown of the average own-price elasticities by fuel type does not suggest noticeable differences.
Cross-price elasticities for HEVs seem to be stronger with respect to gasoline vehicles than with
24The first-stage regression results, reported in Table G4 in Appendix G, show that the instrumental variables are
jointly significant and have the expected signs.
25Table D1 in Appendix D lists the observed and simulated values of the micro moments.
20

Table 4: Estimation results of demand models
OLS logit IV logit RC logit 1 RC logit 2
Variableα, β α, β α, β σ α, β π σ
Price / income -0.406 -6.013 -12.864 -14.569
(0.062) (0.739) (2.299) (2.323)
Cost per km -2.522 -0.668 -3.162 1.557 -3.041 1.453
(0.090) (0.227) (0.388) (0.331) (0.357) (0.341)
Acceleration -0.271 18.033 10.636 11.460
(0.461) (2.659) (1.507) (1.488)
Size 0.324 0.859 1.082 1.147
(0.048) (0.134) (0.115) (0.118)
Network 0.032 0.248 0.362 0.213
(0.069) (0.069) (0.178) (0.171)
Entry year -0.623 -0.457 -0.367 -0.345
(0.032) (0.041) (0.051) (0.052)
Exit year -1.707 -1.720 -1.975 -2.043
(0.034) (0.041) (0.059) (0.061)
BEV 4.992 7.423 5.025
(0.379) (0.450) (0.376)
HEV 1.811 2.681 1.778
(0.114) (0.108) (0.118)
Diesel 1.663 2.495 1.722
(0.125) (0.128) (0.121)
Gasoline 1.830 -3.513 1.568
(0.082) (0.118) (0.087)
SUV 3.514 3.521
(0.105) (0.105)
Own price elasticity
Median -0.371 -5.490 -5.588 -6.125
Weighted average -0.291 -4.302 -5.377 -5.906
Notes: This table presents the estimation results for our demand model. The utility specification includes nameplate,
province, and year-interacted fuel-type fixed effects. The first two columns report the results from the logit model,
where income refers to the average market income (¯ym). The next two columns report random-coefficients estimation
results under the assumption that mileage does not affect consumer valuations of fuel types (RC logit 1). The last
three columns report the results for the full model (RC logit 2), which allows for heterogeneous valuations of fuel
types by mileage. In both random-coefficients specifications, income refers to an individual income draw (y i). Micro-
moments are incorporated into the GMM estimation for the random-coefficients specifications. Robust standard
errors, clustered by market, are reported in parentheses.
respect to BEVs. See Table G5 in Appendix G for further information on own- and cross-price
elasticities by fuel type.
To examine the extent of substitution across different fuel types more systematically, we calcu-
late diversion ratios at the fuel-type level, reported in Table 5 for 2023. These measure the fraction
of a product’s lost sales after a price increase that is diverted to other products with the same or
different fuel type. Not surprisingly, the diversion ratios are larger for products of the same fuel
type. More interestingly, across fuel types, HEVs exhibit higher substitutability with gasoline and
diesel vehicles than with BEVs. For example, following an HEV price increase, gasoline vehicles
21

Table 5: Diversion ratios in 2023
BEV HEV Diesel Gasoline LPG Outside
BEV 0.574 0.101 0.038 0.168 0.009 0.110
HEV 0.029 0.432 0.061 0.288 0.020 0.171
Diesel 0.034 0.194 0.290 0.340 0.026 0.116
Gasoline 0.017 0.098 0.038 0.639 0.015 0.193
LPG 0.023 0.178 0.078 0.442 0.043 0.236
Notes: This table presents the diversion ratios from the row fuel type to the column fuel type in 2023. In a given mar-
ket, the diversion ratio from productjto fuel typeGis defined asD j→G ≡ P k∈JG\{j} Dj→k ≡ P k∈JG\{j} ∂sk/∂pj −∂sj /∂pj ,
whereJ G denotes the set of products with fuel typeG. The sales-weighted average diversion ratio from fuel type
G1 toG 2 is thenD G1→G2 ≡ P j∈JG1 wjDj→G2 , wherew j is productj’s sales share within fuel typeG 1. Finally, we
averageD G1→G2 across the 16 markets in 2023 to obtain ¯DG1→G2 .
capture on average 28.8% of the lost market share of HEVs, while BEVs capture only 2.9%. Sim-
ilarly, when the price of a gasoline vehicle increases, HEVs capture 9.8% of the lost sales, while
diversion to BEVs is limited to only 1.7%. This stronger substitutability between HEVs and ICEVs
than between BEVs and ICEVs is observed throughout the sample period, as shown in Figure G6
in Appendix G.
The full demand model suggests that mileage heterogeneity is an important determinant of con-
sumer choice and substitution across fuel types. To further explore the role of mileage heterogeneity,
we predict each fuel type’s market share in 2023 for consumers in each of five average daily mileage
intervals: 0–20, 20–40, 40–60, 60–80, and 80–100 km. We find that the market shares of vehicles
with lower per-km fuel costs (HEVs, BEVs, and diesel cars) tend to be higher among consumers
with greater mileage. For instance, the BEV market share doubles from 2.22% to 4.44% as daily
mileage increases from the 20–40 km range to the 60–80 km range. In contrast, the market share
of gasoline vehicles, which typically have higher per-km fuel costs, declines sharply in consumer
mileage. See Figure G7 in Appendix G for further information.
6 Comparing BEV and HEV subsidies
In this section, we compare the emission-reducing benefits of the BEV and HEV subsidy policies
over the final four years of the sample period (2020–2023). As detailed in Section 3.3, HEV subsidies
were discontinued in 2019; consequently, only BEVs were subsidized during this period.
6.1 Counterfactual approach
Supply and equilibriumTo evaluate the impact of subsidies on emissions, we integrate our
demand model with a supply-side model of multi-product Bertrand competition. In Section 2, we
defined the net consumer price of productjasp j =p G j −τ j, i.e., the difference between the gross
price and the subsidy. Letpbe the vector of net consumer prices for all products in the market.
22

Then, the variable profit of firmfselling a set of productsJ f is given by
Πf =
X
j∈Jf

pG j −mc j  sj(p)·M,
wheremc j denotes the marginal cost of productj,s j(p) is the product’s market share, specified
earlier by equation (9), andMis the market size. The first-order conditions for profit maximization
are given in vector notation by
pG =mc−  Ω◦ ∇s p(p) −1 s(p),(13)
wherep G =p+τ, Ω is theJ×J(block-diagonal) ownership matrix with elements equal to 1
if product pairs belong to the same firm and zero otherwise, the operator◦denotes element-by-
element multiplication, and∇ s p is theJ×Jmatrix of partial derivatives of market shares with
respect to prices. 26
We first use the system (13) to recover the (constant) marginal costs at the observed price vector.
We subsequently use it to compute equilibrium prices under counterfactual subsidy scenarios. We
obtain the equilibrium price vector using a root solver (or fixed-point algorithm), which is then
used to compute counterfactual market shares, sales, and the implied total emissions.
We consider two counterfactual subsidy scenarios, relative to the current status quo scenario
of BEV subsidies: (i) no subsidy to either BEVs or HEVs and (ii) a reallocation of the total BEV
subsidy budget toward uniform subsidies to HEVs. We focus on a reallocation of the direct BEV
purchase subsidy budget, excluding additional BEV incentives through infrastructure development
and tax credits. Given that existing BEV subsidies already incorporate some degree of optimization,
our estimates may serve as a lower bound on the relative effectiveness of HEV subsidies.
T otal GHG emissionsWe compute total GHG emissions under the status quo and the two
counterfactual policy scenarios. We account for both fuel-cycle emissions (relating to usage) and
vehicle-cycle emissions (relating to production, disposal and recycling). We first calculate consumer
i’s emissions and then aggregate over consumers to obtain total emissions.
Consumeri’s expected emissions under policy scenarioτ,E τ i , are given by the weighted average
of emissions across all products and the outside option, usings τ i , consumeri’s choice-probability
vector under policyτ, as weights:
Eτ i = X
j∈J

T·m i ·e F C j +e V C j| {z }
eij

 sτ ij +e i0sτ i0,(14)
wherem i is consumeri’s annual driving distance (in km) andTis the expected vehicle operating
26Each firm is defined at the parent company level. That is, we have four domestic firms (Hyundai Motor Group,
KG Mobility, GM Korea, and Renault Korea) and five foreign firms (Mercedes-Benz Group, BMW, Volkswagen
Group, Toyota Group, and Tesla).
23

period.
The variablee F C j denotes vehiclej’s fuel-cycle emissions associated with the energy use required
for driving 1 km (in g CO 2e/km). The termT·m i ·e F C j represents vehiclej’s cumulative fuel-cycle
emissions for consumeriover the ownership period. The variablee V C j denotesj’s vehicle-cycle
emissions generated during production, disposal, and recycling (in g CO 2e). The sum of these two
terms constitutes productj’s GHG emissions for consumeri, denoted ase ij.
The variablee i0 represents emissions from the outside option, i.e., secondhand vehicle emissions.
Given the lack of information on each consumer’s specific outside option, we set the fuel-cycle
emissions per km of the outside option, denoted bye F C 0 , equal to the sales-weighted average fuel-
cycle GHG emissions per km in the respective province over the preceding eight years, excluding
the most recent three years (reflecting the assumption that consumers do not replace their vehicles
within the first three years of ownership). Furthermore, we set the vehicle-cycle emissions of the
outside option equal to zero. Assuming a remaining life span ofT O years, emissions from the
outside option are given bye i0 =T O ·m i ·e F C 0 .
We measure fuel-cycle and vehicle-cycle emissions for each product-year combination following
the approach outlined in Section 4.2. In our baseline scenario, we set the expected vehicle operating
period for new and secondhand cars equal to 15 years. This is based on the average vehicle life
span for passenger vehicles in South Korea and in line with standard assumptions in the literature
(e.g., Allcott et al., 2024). We also conduct a sensitivity analysis by considering lower expected
operating periods.
Expected total emissions in marketmunder policyτare obtained by integrating individual
consumers’ emissionsE τ i overDandv:
Eτ m =M m
Z
D
Z
v
Eτ i dF(v)dF(D),(15)
whereM m is the market size. We approximate the expected market-level emissions (15) based
on ourN= 1 000 draws from the income and mileage distribution (D), and Halton draws to
approximate the normal distribution (v).
We then calculate changes in emissions, ∆E τ m, following two distinct policy transitions: (i)
from no subsidies to the current BEV subsidies, and (ii) from no subsidies to HEV subsidies.
We also report the changes in their underlying components: fuel-cycle and vehicle-cycle emissions
associated with the inside goodsj∈J, and outside emissions (i.e., fuel-cycle emissions from the
outside good). See Appendix E.2 for details.
6.2 Budget-neutral subsidy reallocation
Marginal abatement returnsBefore quantifying the emission effects of the policy transitions
in our equilibrium model, it is instructive to evaluate condition (5) in Proposition 2, under which
subsidizing HEVs at the expense of taxing BEVs reduces emissions. Recall that this condition
compares the marginal abatement returns across fuel types under zero government spending, which
24

Table 6: Marginal abatement return by fuel type
BEV HEV Gasoline Diesel LPG
Marginal abatement return 1.402 1.671 -0.355 -1.006 -0.939
Own abatement return 1.395 1.553 -0.338 -1.045 -0.970
Cross abatement return 0.007 0.118 -0.017 0.039 0.031
Notes: For each of the five fuel types, the first row presents the market-size-weighted average of the marginal
abatement return (in tonnes of CO 2e per mil. KR W) across 62 markets during the 2020–2023 period. The bottom
two rows separately report two components of the abatement return: one associated with products eligible for the
subsidy (the own abatement return:− 1 Sg1 P j∈Jg Θj,g1 ∂sj ∂pj (eD j −e j)) and the other associated with products of other
fuel types (the cross abatement return:− 1 Sg1 P g̸=g1 P j∈Jg Θj,g1 ∂sj ∂pj (eD j −e j)).
depend on demand responses and net diverted emissions, weighted by equilibrium subsidy pass-
through rates and incorporating heterogeneous usage emissions.
Table 6 presents the marginal abatement returns for subsidies to each fuel type, evaluated
at counterfactual prices under the no-subsidy scenario. We first derive the subsidy pass-through
matrix under our Bertrand–Nash setup (see Appendix A.5 for details) and compute the marginal
abatement returns separately for each market. The estimates are then averaged across the 62
markets over the 2020–2023 period. 27 The marginal abatement return for HEV subsidies (1.671
tonnes of CO2e per million KR W) is approximately 20% higher than that for BEV subsidies (1.402
tonnes).28 This finding suggests that subsidizing HEVs (financed by taxing BEVs) would reduce
emissions relative to the no-subsidy baseline. Additionally, the marginal abatement returns for
subsidies to the other fuel types are all negative, implying taxes would be appropriate, especially
for diesel and LPG fuel types. The distributions of the marginal abatement returns across markets
are consistent with these conclusions, as shown in Figure G8 in Appendix G.
We also decompose the abatement return into two components: one associated with products
eligible for the subsidy (the own abatement return) and the other associated with products of other
fuel types (the cross abatement return). Table 6 shows that the second term is negligible relative
to the first across all fuel types, reflecting the low cross-fuel-type pass-through rates.
T otal abatement returnsThe previous results suggest that, under zero government spending,
a marginal increase in HEV subsidies at the expense of taxing BEVs would reduce emissions. We
now compare the total effects of BEV and HEV subsidies while accounting for the substantial
existing BEV subsidies in South Korea. Specifically, we compare the current BEV subsidies with a
uniform per-vehicle HEV subsidy calibrated so that total HEV subsidy expenditures approximately
27Of the 64 markets, 2 are excluded (2021 Chungnam and 2022 Gwangju) because the computation of subsidy
pass-through matrices involves ill-conditioned, non-invertible matrices.
28The inverse of the marginal abatement return is the marginal abatement cost, a measure commonly used in the
literature and expressed as the cost per tonne of CO 2 (or CO2e) abated. Under our no-subsidy baseline, the marginal
abatement cost is 0.713 million KR W per tonne of CO2e abated for the BEV subsidy policy and 0.598 million KR W
for the HEV subsidy policy.
25

match the BEV subsidy budget over the four-year period 2020–2023.
Table 7 shows the main findings. According to Panel A, the budget-neutral HEV subsidy
amounts to an average of 1.9 million KR W per vehicle, substantially lower than the actual BEV
subsidy of 8.6 million KR W per vehicle. This reflects the fact that HEV sales are significantly
higher than BEV sales. At the same time, the HEV subsidy induces manufacturers to reduce gross
prices of HEVs across the board (implying pass-through rates above 100% for all models), whereas
the BEV subsidy results in both increases and decreases in BEV prices (implying pass-through
rates that vary across models between 71% and 115%); see Table G6 in Appendix G. In sum, the
budget-neutral HEV subsidy is substantially below the BEV subsidy, but this is accompanied by
slightly higher pass-through. Panels B and C of Table 7 show how the subsidies and implied price
adjustments affect sales and emissions.
According to Panel B, the HEV subsidies would increase HEV sales by almost 178 thousand
units, whereas BEV subsidies would increase BEV sales by only 78 thousand units. Hence, a budget-
neutral HEV subsidy has a much larger sales effect despite the smaller magnitude of the subsidy.
HEV subsidies would encourage more consumers to substitute away from ICEVs (gasoline, diesel,
and LPG) than BEV subsidies do. Most notably, HEV subsidies would reduce gasoline-vehicle
sales by 92 thousand, compared with only 28 thousand under BEV subsidies. Furthermore, HEV
subsidies divert comparatively more sales from the outside good (consisting mainly of older ICEVs
and therefore entailing the highest emissions). In sum, the HEV subsidy policy is more effective at
inducing substitution away from ICEVs than the BEV subsidy policy. Consequently, the former
may yield greater reductions in aggregate emissions than the latter.
Panel C of Table 7 confirms that this is indeed the case. HEV subsidies would lead to a reduction
in total emissions of 2.1 million tonnes of CO2e over the four-year period, approximately 47% larger
than the amount of the emission savings attributable to BEV subsidies. We separately calculate the
various parts of equation (15) to decompose the change in total emissions into three components:
fuel-cycle, vehicle-cycle, and outside emissions. BEV subsidies yield larger reductions in fuel-cycle
emissions than HEV subsidies (942 versus 572 thousand tonnes of CO2e). However, they also imply
larger vehicle-cycle emissions. Furthermore, they imply much lower savings in outside emissions
(871 versus 1 821 thousand tonnes of CO2e), because they are less successful in diverting sales from
the outside good.
Note that HEV subsidies lead to a smaller reduction in fuel-cycle emissions than in outside
emissions (0.6 versus 1.8 million tonnes of CO 2e). This result, however, does not imply that the
HEV subsidy policy reduces emissions primarily by inducing consumers to substitute away from
the outside option rather than from ICEVs. Instead, it arises because the reduction in inside fuel-
cycle emissions is a net figure that accounts for the simultaneous increase in emissions from newly
adopted HEVs. To illustrate this point, Table 7 also decomposes the change in fuel-cycle emissions
by fuel type: ICEVs (combining gasoline, diesel, and LPG), BEVs, and HEVs; see Appendix E.2 for
details of the decomposition. The decomposition reveals that HEV subsidies lead to a substantial
reduction in fuel-cycle emissions from ICEVs (5.2 million tonnes of CO 2e in total), nearly three
26

Table 7: Comparison of BEV and HEV subsidy effects
BEV subsidies HEV subsidies
Panel A: Subsidy spending
Per-unit subsidy (million KR W) 8.646 1.943
Total subsidy expenditure (trillion KR W) 1.563 1.565
Panel B: Sales effects (number of vehicles)
Total sales change
BEV 77 655 -3 206
HEV -15 026 177 697
Gasoline -28 244 -92 213
Diesel -13 793 -31 708
LPG -2 114 -8 666
Outside option -18 478 -41 903
Panel C: Emissions effects (thousand tonnes CO 2e)
Total emissions change -1 433 -2 104
Fuel-cycle -942 -572
- ICEV -1 930 -5 208
- BEV 1 473 -69
- HEV -485 4 705
Vehicle-cycle 381 289
Outside option -871 -1 821
Notes: The top panel compares the observed BEV subsidy levels with the counterfactual HEV subsidy design. The
per-vehicle subsidy is calculated as the sales-weighted average across all nameplates. The bottom two panels report
changes in sales and emissions over the 2020–2023 period following the implementation of BEV and HEV subsidies.
times as large as outside emissions reductions. Furthermore, BEV subsidies lead to a much smaller
reduction in fuel-cycle emissions from ICEVs (only 1.9 million tonnes of CO 2e), reflecting lower
substitution between BEVs and ICEVs.
Sensitivity analysisTo better understand the magnitude of the estimated emission effects, we
compare the baseline emission effects with those obtained under a range of alternative specifications
and assumptions. Table 8 shows the results from this exercise.
First, the baseline emission effects are based on the flexible random coefficients logit model
reported in Table 4, RC logit 2, which incorporates mileage heterogeneity and other sources of un-
observed consumer heterogeneity. To illustrate the role of this flexibility, we quantify the impact of
27

Table 8: Emission effects under alternative specifications and assumptions
BEV sub. HEV sub.
Baseline -1 433 -2 104
Panel A: restrictive demand models
IV Logit -1 203 -1 105
RC logit 1 -1 025 -1 624
Panel B: alternative vehicle operating periods
15- & 9-year lifespan -1 084 -1 376
6- & 6-year lifespan -344 -668
Panel C: alternative ownership structures
Brand -1 458 -1 942
Product -1 453 -1 877
Notes: Panel A presents emission changes (in thousand tonnes of CO 2e) under restrictive demand models: IV logit
and RC logit 1. Panel B presents emission changes under alternative vehicle operating periods: the “15- & 9-year
lifespan” row evaluates a truncated 9-year ownership horizon strictly for the outside option. The “6- & 6-year
lifespan” row applies a 6-year holding period to both inside and outside goods. Panel C presents emission changes
under alternative ownership structures: brand-level ownership and product-level ownership.
the HEV and BEV subsidies under our more restrictive specifications in Panel A of Table 8. RC logit
1, which assumes homogeneous mileage but accounts for unobserved heterogeneity, also predicts
considerably larger emission savings under the HEV-focused subsidy, although it underestimates
total emission savings of both policies, compared to the most flexible RC logit 2 specification. 29 In
contrast, IV logit without consumer heterogeneity yieldslargeremission savings under the BEV-
focused subsidy. This is consistent with our theoretical analysis in Section 2, which implies that
under symmetric logit demand a BEV subsidy is more effective whenever BEV emissions are lower
than HEV emissions.
Second, the relative magnitude of the emission effects under HEV and BEV subsidies hinges on
assumptions regarding the vehicles’ expected operating period for new and secondhand vehicles.
Our baseline analysis assumes a 15-year operating period, in line with both the average passenger-
vehicle lifespan in South Korea and the existing literature, and uses this horizon to compute changes
in cumulative emissions. Since the lifespan of the outside option (secondhand vehicles) exceeds 15
years under this baseline specification, we consider two alternatives here. First, we continue to
29Appendix F provides a detailed interpretation of why the assumption of homogeneous mileage underestimates
emission savings under both policies.
28

assume an expected operating period of 15 years for new vehicles, but set the expected operating
period of secondhand vehicles to 9 years, which equals the expected vehicle life span of 15 years
minus the average holding period of new vehicles of 6 years. Second, we conservatively assume an
expected operating horizon of 6 years for all options, matching the average initial holding period in
South Korea, to measure policy-induced environmental effects over the interval before consumers
make their subsequent vehicle choices.
Panel B of Table 8 compares the results from these alternative scenarios with our baseline case.
In both alternative scenarios, HEV subsidies still reduce emissions more than BEV subsidies. In
the first alternative scenario, with a shorter expected operating period of 9 years for secondhand
vehicles, HEV subsidies reduce emissions by 1.4 million tonnes of CO 2e, compared with only 1.1
million tonnes for BEV subsidies. The difference is smaller because emission savings from diverting
sales away from secondhand vehicles (the outside option) are especially reduced under HEV subsi-
dies, owing to the shorter assumed 9-year horizon. In the second scenario, with a shorter expected
operating period of 6 years for both new and secondhand vehicles, estimated emission savings are
naturally smaller, but HEV subsidies remain more effective, even more so in percentage terms.
Third, the relative magnitude of the emission effects may also depend on the degree of subsidy
pass-through, which in turn is influenced by firms’ market power under multi-product Bertrand
competition. As discussed in Section 3.1, the South Korean passenger vehicle market is highly
concentrated, with Hyundai Motor Group accounting for over 70% of total sales. To assess the role
of market power, we compare the predicted emission effects under our baseline parent-company
ownership assumption with those under two alternative ownership structures: brand-level ownership
(treating Hyundai, Kia, and Genesis as separate firms) and product-level ownership.
We find that the emission effects of the subsidies remain very similar across these alternative
ownership structures (see Panel C of Table 8). This suggests that competitive constraints from rival
firms, such as Toyota for HEVs and Tesla for BEVs, limit Hyundai’s incentives to reduce subsidy
pass-through, thereby preserving diversion away from ICEVs.
In sum, across these alternative scenarios, the emission savings are consistently lower under
BEV subsidies than under budget-neutral HEV subsidies. These findings confirm the comparative
strength of HEVs in diverting sales away from conventional ICEVs.
6.3 The role of the carbon intensity of electricity generation
In the previous subsection, our comparison of BEV and HEV subsidies has been based on fuel-cycle
emissions for BEVs evaluated under the current electricity generation mix in South Korea. The
carbon intensity of electricity generation depends on the relative importance of fossil fuels and
renewable energy sources. This mix evolves over time and varies across countries, partly reflecting
past policy choices regarding the promotion of renewable energy. If electricity generation is highly
carbon-intensive, HEV subsidies may be even more effective relative to BEV subsidies. Conversely,
as electricity generation becomes less carbon-intensive, BEV subsidies may become more effective.
To assess how the energy mix affects the relative effectiveness of HEV and BEV subsidies, we
29

Figure 3: Policy comparison with different GHG emission intensity of electricity generation
Notes: This figure illustrates the emission savings under BEV and HEV subsidy policies across varying GHG emission
factors.
compare their emission savings at different phases of the energy transition, using other countries as
benchmarks. Specifically, we adjust the electricity-sector emission factor (g CO2e/kWh of electricity
generation) to the levels in other countries. This adjustment alters the fuel-cycle emissions,e FC j , of
BEVs. As discussed in Section 3.2, these emissions are obtained by dividing the electricity emission
factor by vehiclej’s fuel economy (in km/kWh). Formally,
eFC j = emission factor (g CO 2e/kWh) fuel economyj (km/kWh) .
In 2022, the emission factor in South Korea was 453 g CO 2e/kWh, comparable to that of the
United States and Germany and lower than the world average of 526 g CO2e/kWh. Most European
countries have lower emission factors, whereas Japan, China, and many developing countries have
higher ones. Table C1 in Appendix C provides the emission-factor levels for 148 countries.
We calculate the emission savings under BEV and HEV subsidies using the emission factors
of 18 other countries, assuming that these emission factors affect only the fuel-cycle emissions of
BEVs, while fuel-cycle emissions for other fuel types and vehicle-cycle emissions remain constant.
Figure 3 summarizes the results; the corresponding numerical results are reported in Table G7 of
Appendix G.
Emission savings from the BEV subsidy decrease linearly with the emission factor (represented
by the blue line), amounting to 2.8 million tonnes of CO 2e under Norway’s low-carbon electric-
30

ity generation mix and only 0.2 million tonnes under India’s much more carbon-intensive mix.
Conversely, emission savings from the HEV subsidy increase slightly with the emission factor (rep-
resented by the red line). As the grid becomes more carbon-intensive, the emissions profile of a
BEV worsens relative to that of an HEV, which mechanically increases the emission savings of the
HEV subsidy policy.
At South Korea’s current electricity generation mix, emission savings amount to 1.4 million
tonnes of CO 2e for the BEV subsidy and 2.1 million tonnes for the HEV subsidy. As the emission
factor declines with a cleaner electricity generation mix, the emission savings of a BEV subsidy grow
rapidly. The emission savings from the two policies approximately equalize at Portugal’s emission
factor level (251 g CO 2e/kWh), which is 55% of South Korea’s current level. In other words, BEV
subsidies become as effective as HEV subsidies only if South Korea’s electricity generation mix
becomes 45% cleaner. At even lower emission-factor levels, a BEV subsidy becomes more effective
than an HEV subsidy.
In contrast, BEV subsidies would become less effective at curbing GHG emissions if South
Korea’s emission factor were higher than its current level. For example, at China’s emission factor
level, emission savings from a BEV subsidy would be less than half of the savings from an HEV
subsidy (0.9 million tonnes versus 2.1 million tonnes of CO 2e). If the electricity generation mix
were as carbon-intensive as in India and Kazakhstan, BEV subsidies would hardly reduce emissions
or could even be environmentally harmful.
These results emphasize that the environmental efficacy of a BEV subsidy policy depends crit-
ically on the carbon intensity of electricity generation. The greater the reliance on cleaner energy
sources such as wind, solar, and hydropower, the greater the environmental benefits of BEV adop-
tion. In fact, many countries with large automobile markets, including China, the United States,
Japan, and India, may not yet have transitioned sufficiently toward low-carbon electricity to fully
realize these potential benefits.
7 Conclusion and discussion
We develop a framework for comparing the relative effectiveness of subsidies for alternative emission-
reducing technologies. We show that an intermediate technology may reduce emissions more ef-
fectively than the cleanest technology if it induces sufficiently greater substitution away from the
prevailing high-emission technology to offset its emission disadvantage relative to the cleanest tech-
nology. Our empirical analysis shows that these conditions are satisfied in the South Korean
passenger vehicle market. Specifically, HEVs exhibit a sufficiently small emission gap with BEVs
and induce considerably more substitution away from ICEVs. As a result, reallocating the subsidy
budget from BEVs to HEVs would reduce total emissions by an additional 47%. For BEV subsidies
to outperform HEV subsidies in reducing emissions, the country’s electricity generation mix would
need to become 45% cleaner.
Our findings highlight two main challenges for current BEV-focused policies in fully realizing
31

Table 9: Changes in firm profits and consumer surplus
Term BEV subsidies HEV subsidies
Producer surplus change 292.5 1 024.3
- Hyundai Motor Group 291.7 1 111.4
- Other domestic firms -12.4 -66.0
- German firms -48.4 -66.7
- Toyota Group -5.8 52.7
- Tesla 67.5 -7.1
Consumer surplus change 971.5 1 253.4
- Bottom 20% 0.4 -0.7
- 20-40% 23.6 21.2
- 40-60% 109.4 194.5
- 60-80% 230.0 378.2
- Top 20% 608.1 660.2
Notes: This table reports changes (in billion KR W) in firm profits and consumer surplus (by income quantile) under
vehicle subsidy policies (for either BEVs or HEVs). Other domestic firms include GM Korea, KG Mobility, and
Renault Korea, while German firms include BMW, Mercedes-Benz, and Volkswagen Group.
their environmental benefits. First, technological progress that lowers BEV prices and improves
vehicle attributes is essential for inducing consumers of conventional ICEVs to switch to BEVs in
response to subsidies. Second, a cleaner electricity generation mix is needed to ensure that increased
BEV adoption translates into larger emissions reductions.
If HEV subsidies are currently more effective at reducing emissions than BEV subsidies under
South Korea’s existing electricity generation mix, why has South Korea nevertheless chosen to focus
policy support on BEVs? One possible explanation is that BEV subsidies perform better in terms
of other welfare components. To examine this possibility, we use our model to go beyond emissions
and compare the effects of the two subsidy policies on firm profits and consumer surplus, as shown
in Table 9. First, the industry as a whole benefits much more from HEV than from BEV subsidies.
Moreover, Hyundai Motor Group, the dominant domestic player, benefits disproportionately more
from HEV than from BEV subsidies, with profits increasing by nearly four times as much. These
findings therefore suggest no short-term industrial policy rationale for BEV subsidies.
Second, consumers also benefit more from HEV than BEV subsidies, reflecting the larger de-
mand responses and higher pass-through rates associated with HEV subsidies. Moreover, no income
group benefits more from BEV than from HEV subsidies, apart from negligible differences for the
two lowest income groups. Hence, BEV subsidies also cannot be rationalized as a means of pro-
tecting consumers generally or targeting particular income groups.
The absence of an immediate welfare rationale within our framework suggests that the motiva-
tion for BEV subsidies may lie elsewhere. One possibility is that political economy considerations
32

play a role if governments place disproportionate emphasis on promoting frontier technologies that
are particularly salient to voters. Politicians often invest in public goods based on the visibil-
ity of their outcomes rather than their contribution to voters’ welfare (see, for example, Mani and
Mukand (2007)). In line with this reasoning, BEVs’ widespread reputation as the cleanest available
technology may lead politicians to promote their adoption without closely examining the welfare
consequences relative to other technologies.
Another possible rationale for BEV subsidies is that governments pursue long-term industrial
policy objectives. Indeed, since January 2026, the South Korean government has explicitly identified
“support for the domestic BEV industry” as a policy objective (alongside carbon reduction). Similar
considerations may also apply in other countries that actively promote BEV adoption, such as
China, whose electricity generation mix is more carbon-intensive than South Korea’s. However,
if the objective is to stimulate innovation and learning-by-doing in the domestic BEV industry, it
remains unclear whether purchase subsidies are the most appropriate policy instrument, or whether
alternative instruments targeted more directly at innovation and production would be preferable.
Finally, governments may use BEV subsidies as part of a broader international trade strategy
in response to similar industrial policies adopted abroad. 30 The United States and the European
Union, for example, have recently combined restrictions on Chinese EVs with domestic incentives for
EV and battery production (Office of the United States Trade Representative, 2024a,b; European
Commission, 2024; U.S. Congress, 2022; European Commission, 2021). South Korea has recently
moved in a similar direction by allocating subsidies to firms based on their contribution to the
domestic BEV supply chain (Korea Joongang Daily, 2026), effectively reducing subsidies to Chinese
automakers such as BYD. Exploring the interaction between environmental policy and these broader
policy objectives remains an important topic for future research.
30Barwick et al. (2026) show that a revenue-neutral combination of a moderate tariff on imported EVs and a
subsidy for domestic EV production improves national welfare compared to both outright protectionism and laissez-
faire.
33

References
Acemoglu, D., Aghion, P., Bursztyn, L., and Hemous, D. (2012). The environment and directed
technical change.American economic review, 102(1):131–166.
Acemoglu, D., Akcigit, U., Hanley, D., and Kerr, W. (2016). Transition to clean technology.Journal
of political economy, 124(1):52–104.
Allcott, H., Kane, R., Maydanchik, M. S., Shapiro, J. S., and Tintelnot, F. (2024). The effects
of “buy american”: Electric vehicles and the inflation reduction act. Technical report, National
Bureau of Economic Research.
Alternative Fuels Data Center (2026). Federal Laws and Incentives for Electric Vehicles. Accessed:
May 2026.
Archsmith, J., Muehlegger, E., and Rapson, D. S. (2022). Future paths of electric vehicle adoption
in the united states: predictable determinants, obstacles, and opportunities.Environmental and
Energy Policy and the Economy, 3(1):71–110.
Barwick, P. J., Collison, J., Goldberg, P. K., Li, S., and Wang, Y. (2026). From trade war to
green transition: Optimal electric vehicle tariffs with revenue-funded subsidies. Technical report,
National Bureau of Economic Research.
Barwick, P. J., Kwon, H.-S., and Li, S. (2024). Attribute-based subsidies and market power: an
application to electric vehicles. Technical report, National Bureau of Economic Research.
Beresteanu, A. and Li, S. (2011). Gasoline prices, government support, and the demand for hybrid
vehicles in the united states.International Economic Review, 52(1):161–182.
Berry, S. (1994). Estimating discrete-choice models of product differention.RAND Journal of
Economics, 25(2):242–262.
Berry, S., Levinsohn, J., and Pakes, A. (1995). Automobile prices in market equilibrium.Econo-
metrica, 63(4):841–890.
Berry, S., Levinsohn, J., and Pakes, A. (2004). Differentiated products demand systems from a
combination of micro and macro data: The new car market.Journal of Political Economy,
112(1):68–105.
Bushnell, J. B., Muehlegger, E., and Rapson, D. S. (2022). Energy prices and electric vehicle
adoption. Working Paper 29842, National Bureau of Economic Research.
Chandra, A., Gulati, S., and Kandlikar, M. (2010). Green drivers or free riders? an analysis of tax
rebates for hybrid vehicles.Journal of Environmental Economics and Management, 60(2):78–93.
Choi, W., Yoo, E., Seol, E., et al. (2020). Greenhouse gas emissions of conventional and alternative
vehicles: Predictions based on energy policy analysis in south korea.Applied Energy, 265:114754.
Clinton, B. C. and Steinberg, D. C. (2019). Providing the spark: Impact of financial incentives
on battery electric vehicle adoption.Journal of Environmental Economics and Management,
98:102255.
Conlon, C. and Gortmaker, J. (2020). Best practices for differentiated products demand estimation
with pyblp.The RAND Journal of Economics, 51(4):1108–1161.
34

Conlon, C. and Gortmaker, J. (2025). Incorporating micro data into differentiated products demand
estimation with pyblp.Journal of Econometrics, page 105926.
Conlon, C. and Mortimer, J. H. (2021). Empirical properties of diversion ratios.The RAND
Journal of Economics, 52(4):693–726.
Davis, L. W., Li, J., and Springel, K. (2025). Political ideology and us electric vehicle adoption.
Technical report, National Bureau of Economic Research.
DeShazo, J., Sheldon, T. L., and Carson, R. T. (2017). Designing policy incentives for cleaner
technologies: Lessons from california’s plug-in electric vehicle rebate program.Journal of Envi-
ronmental Economics and Management, 84:18–43.
Elgowainy, A., Han, J., Ward, J., et al. (2016). Cradle-to-grave lifecycle analysis of us light duty
vehicle-fuel pathways: a greenhouse gas emissions and economic assessment of current (2015)
and future (2025-2030) technologies. Technical report, Argonne National Lab.(ANL), Argonne,
IL (United States).
European Automobile Manufacturers’ Association (2025). Electric Cars: Tax Benefits and Incen-
tives (2025). Accessed: May 2026.
European Commission (2021). Important Project of Common European Interest on Batteries.
Accessed: August 2026.
European Commission (2024). EU Commission imposes countervailing duties on imports of battery
electric vehicles (BEVs) from China. Accessed: August 2026.
Fournel, J.-F. (2024). Electric Vehicle Subsidies: Cost-Effectiveness and Emission Reductions.
working paper or preprint.
Gallagher, K. S. and Muehlegger, E. (2011). Giving green to get green? incentives and consumer
adoption of hybrid vehicle technology.Journal of Environmental Economics and Management,
61(1):1–15.
Gillingham, K. T., van Benthem, A. A., Weber, S., Saafi, M. A., and He, X. (2023). Has consumer
acceptance of electric vehicles been increasing? evidence from microdata on every new vehicle
sale in the united states. InAEA Papers and Proceedings, volume 113, pages 329–335. American
Economic Association 2014 Broadway, Suite 305, Nashville, TN 37203.
Grieco, P. L., Murry, C., and Yurukoglu, A. (2024). The evolution of market power in the us
automobile industry.The Quarterly Journal of Economics, 139(2):1201–1253.
Gulati, S., McAusland, C., and Sallee, J. M. (2017). Tax incidence with endogenous quality
and costly bargaining: Theory and evidence from hybrid vehicle subsidies.Journal of Public
Economics, 155:93–107.
Guo, X. and Xiao, J. (2023). Welfare analysis of the subsidies in the chinese electric vehicle industry.
The Journal of Industrial Economics, 71(3):675–727.
Heid, P., Remmy, K., and Reynaert, M. (2025). Equilibrium effects in complementary markets:
Electric vehicle adoption and electricity pricing.
Heutel, G. and Muehlegger, E. (2015). Consumer learning and hybrid vehicle adoption.Environ-
mental and Resource Economics, 62(1):125–161.
35

Holland, S. P., Mansur, E. T., Muller, N. Z., and Yates, A. J. (2016). Are there environmental
benefits from driving electric vehicles? the importance of local factors.American Economic
Review, 106(12):3700–3729.
International Council on Clean Transportation (ICCT) (2024). Real-world CO 2 emission values of
passenger cars in Europe: January 2024 update. White paper, International Council on Clean
Transportation. Accessed: May 2026.
Kelly, J. C., Elgowainy, A., Isaac, R., et al. (2023). Cradle-to-grave lifecycle analysis of us light-duty
vehicle-fuel pathways: a greenhouse gas emissions and economic assessment of current (2020)
and future (2030-2035) technologies. Technical report, Argonne National Laboratory (ANL),
Argonne, IL (United States).
Korea Joongang Daily (2026). Gov’t to implement evaluation system for EV subsidies in July.
Accessed: August 2026.
Langford, R. P. and Gillingham, K. (2023). Quantifying the benefits of the introduction of the
hybrid electric vehicle.International Journal of Industrial Organization, 87:102904.
Li, J. (2019). Compatibility and investment in the us electric vehicle market.Unpublished
manuscript, MIT.
Li, S., Tong, L., Xing, J., and Zhou, Y. (2017). The market for electric vehicles: indirect network
effects and policy design.Journal of the Association of Environmental and Resource Economists,
4(1):89–133.
Mani, A. and Mukand, S. (2007). Democracy, visibility and public good provision.Journal of
Development economics, 83(2):506–529.
Meng, L., Xiao, J., and Liu, M. (2026). Is pollution reduced or redistributed? the impact of electric
vehicle subsidies in china.Journal of Economics & Management Strategy, 35(1):59–98.
Ministry of Environment (ME) (2024). Public Notice on Rapid EV Charging Rates and Infrastruc-
ture. Accessed: May 2026.
Muehlegger, E. and Rapson, D. S. (2022). Subsidizing low-and middle-income adoption of electric
vehicles: Quasi-experimental evidence from california.Journal of Public Economics, 216:104752.
Muehlegger, E. J. and Rapson, D. S. (2023). Correcting estimates of electric vehicle emissions
abatement: Implications for climate policy.Journal of the Association of Environmental and
Resource Economists, 10(1):263–282.
Office of the United States Trade Representative (2024a). Request for Comments on Proposed
Modifications and Machinery Exclusion Process in Four-Year Review of Actions Taken in the
Section 301 Investigation: China’s Acts, Policies, and Practices Related to Technology Transfer,
Intellectual Property, and Innovation. 8Accessed: August 2026.
Office of the United States Trade Representative (2024b). Notice of Modification: China’s Acts,
Policies and Practices Related to Technology Transfer, Intellectual Property and Innovation.
Accessed: August 2026.
Ohashi, H. and Toyama, Y. (2017). The effects of domestic merger on exports: A case study of the
1998 korean automobile industry.Journal of International Economics, 107:147–164.
36

Papageorgiou, C., Saam, M., and Schulte, P. (2017). Substitution between clean and dirty energy
inputs: A macroeconomic perspective.Review of Economics and Statistics, 99(2):281–290.
Petrin, A. (2002). Quantifying the benefits of new products: The case of the minivan.Journal of
Political Economy, 110(4):705–729.
Prussi, M., Yugo, M., De Prada, L., et al. (2020).JEC well-to-tank report V5 – JEC well-to-wheels
analysis – Well-to-wheels analysis of future automotive fuels and powertrains in the European
context. Publications Office.
Sexton, S. E. and Sexton, A. L. (2014). Conspicuous conservation: The prius halo and willingness
to pay for environmental bona fides.Journal of Environmental Economics and Management,
67(3):303–317.
Springel, K. (2021). Network externality and subsidy structure in two-sided markets: Evidence
from electric vehicle incentives.American Economic Journal: Economic Policy, 13(4):393–432.
Statista (2024). New passenger car registrations in selected countries from 2021 to 2023. Accessed:
May 2026.
U.S. Congress (2022). Inflation Reduction Act of 2022. Accessed: August 2026).
Xing, J., Leard, B., and Li, S. (2021). What does an electric vehicle replace?Journal of Environ-
mental Economics and Management, 107:102432.
Zhou, Y. and Li, S. (2018). Technology adoption and critical mass: the case of the us electric
vehicle market.The Journal of Industrial Economics, 66(2):423–480.
37

A Supplement to Section 2
A.1 Proof of Proposition 1
Given our focus on BEV and HEV subsidies,τ= (0, τ H , τB), total emissions and government
expenditure can be expressed as
E(τH , τB) =M
X
j∈{I,H,B}
ejsj(p(τH , τB)),
G(τH , τB) =M
X
j∈{H,B}
τjsj(p(τH , τB)).
Under complete subsidy pass-through and no price response for non-subsidized products, the
effect of a subsidy for productj∈ {H, B}on total emissions is given by Equation (1) in the main
text. The impact on total government expenditure is given by
∂G
∂τj
=M

sj − X
ℓ∈{H,B}
τℓ
∂sℓ
∂pj

 ,(16)
which we assume is positive. This assumption holds provided that (i) the current subsidyτ k (k̸=j)
is sufficiently small, or (ii) the subsidy increase primarily diverts sales away from ICEVs (the highest
emission product) rather than between HEVs and BEVs.
To calculate the impact of a budget-neutral subsidy increase for productj∈ {H, B}, financed by
a subsidy decrease for productk̸=jto maintain a constant government budget ¯G, let the function
τk(τj) be implicitly defined by the government budget constraintG(τ j, τk(τj)) = ¯G. Applying the
implicit function theorem yields
∂G
∂τj
+ ∂G ∂τk dτk dτj = 0,(17)
forj∈ {H, B},k̸=j, so that
dτk
dτj
=− ∂G/∂τ j
∂G/∂τ k
.(18)
The marginal impact of a budget-neutral increase in the per-unit subsidyτ j on total emissions
is then given by
dE(τj, τk(τj))
dτj
= ∂E ∂τj + ∂E ∂τk dτk dτj .(19)
Substituting (18) and rearranging, it follows that dE dτj is negative if and only if
−∂E/∂τ j
∂G/∂τ j
> −∂E/∂τ k
∂G/∂τ k
,(20)
i.e., if and only if the marginal abatement return of a per-unit subsidy is higher for productjthan
for productk.
Substituting equations (1) and (16), we can express the condition (20) under which a budget-
38

neutral subsidy increase for productjdecreases total emissions (i.e.,dE/dτ j <0) as
− ∂sj ∂pj (eD j −e j)
sj −τ j ∂sj ∂pj −τ k ∂sk ∂pj >
− ∂sk ∂pk (eD k −e k)
sk −τ k ∂sk ∂pk −τ j ∂sj ∂pk .(21)
Evaluating condition (21) at zero subsidies (τ H =τ B = 0) yields condition (2) in Proposition 1.
A.2 Comparison of net diverted emissions
If demand responses are identical across technologies,− ∂sj ∂pj 1 sj =− ∂sk ∂pk 1 sk , then the condition for
an HEV subsidy to be more effective than a BEV subsidy reduces toe D H −e H > eD B −e B. This
condition can also be expressed directly in terms of diversion ratios,D H→I andD B→I , instead of
diverted emissions,e D H ande D B :
eD H −e H > eD B −e B if and only if 2−D H→I 2−D B→I < eI −e H eI −e B .(22)
To show this, we use the definition ofe D j and the fact that P k̸=j Dj→k = 1 to obtain
eD H −e H =D H→I eI +D H→B eB −e H
= (1−D H→B )eI +D H→B eB −e H
=D H→B (eB −e I ) +e I −e H .
Similarly,
eD B −e B =D B→H (eH −e I ) +e I −e B.
Substituting these expressions and rearranging yield the equivalent condition above.
Intuitively, condition (22) highlights that whene H =e B, an HEV subsidy is more effective
wheneverD H→I > DB→I , i.e. when HEVs divert more sales from ICEVs than BEVs do.
A.3 Proof of Proposition 2
Here, we allow for multiple products within each fuel type, additional fuel types, and non-trivial
subsidy pass-through under imperfect competition between multi-product price-setting firms. In
this setup, letJandJ g denote the set of all inside products and the set of products with fuel
typeg, respectively. Inside products are partitioned intoGgroups according to their fuel types,
such thatJ=J 1 ∪ · · · ∪Jg ∪ · · · ∪JG. Fix a subsidy policyτ= (τ 1, . . . , τg, . . . , τG), whereτ g
denotes the per-unit subsidy for all products with fuel typeg. Let Θ jg =− ∂pj ∂τg denote the subsidy
pass-through.
We also allow usage emissions to vary across consumers through heterogeneous annual mileage.
Lete ik denote theindividualemissions of productk, that is, the emissions from the product when
used by consumeri. LetD i j→k =− ∂sik/∂pj ∂sij /∂pj denote theindividualdiversion ratio from productjto
39

k. Theindividualdiverted emissions, defined as
eD ij = X
k̸=j
Di j→k eik,
vary across consumers due to heterogeneity in both emissions and demand responses.
Following a similar logic in Section A.1, the condition under which a budget-neutral subsidy
increase for fuel typeg 1, financed by a subsidy decrease for fuel typeg 2 ̸=g 1, decreases total
emissions is given by
−∂E/∂τ g1
∂G/∂τ g1
> −∂E/∂τ g2
∂G/∂τ g2
.(23)
Consumeri’s expected emissions under the subsidy policyτ,E i(τ), are given by the weighted
average of emissions across all products and the outside option, using the consumer’s choice prob-
abilities as weights:
Ei(τ) =
X
k∈J∪{0}
eiksik(p(τ)).
Total market emissions are obtained by integrating these individual emissions:
E(τ) =M
Z
Ei(τ)dF(i) =M
Z X
k∈J∪{0}
eiksik(p(τ))dF(i),
whereMrepresents the market size, andF(i) denotes the consumer distribution, defined over
observed demographics (income and mileage) as well as unobserved heterogeneity.
Differentiating−E(τ) with respect toτ g gives
− ∂E ∂τg =−M· Z X k∈J∪{0} eik ∂sik ∂τg dF(i)
=−M·
Z X
k∈J∪{0}
eik


GX
g=1
X
j∈Jg
∂sik
∂pj
(−Θjg )

 dF(i)
=M·
Z GX
g=1
X
j∈Jg
Θjg

eij ∂sij ∂pj + X k̸=j eik ∂sik ∂pj

 dF(i)
=M
GX
g=1
X
j∈Jg
Θjg ·
Z
− ∂sij
∂pj

X
k̸=j
Di j→k eik −e ij

 dF(i)
=−M
GX
g=1
X
j∈Jg
Θjg
∂sj
∂pj
Z
ωijeD ij dF(i)−
Z
ωijeijdF(i)

=−M
GX
g=1
X
j∈Jg
Θjg
∂sj
∂pj
(eD j −e j),
(24)
40

whereω ij is defined as
ωij = ∂sij/∂pj R ∂sij
∂pj dF(i)
= ∂sij/∂pj
∂sj/∂pj
.
We useω ij as the weights for the individual-level emissions metrics (e ij ande D ij ) to define the
product-level emissionse j and product-level diverted emissionse D j as weighted averages of their
individual counterparts:
ej =
Z
ωijeij dF(i) ande D j =
Z
ωijeD ij dF(i).
The final equality in equation (24) follows from these definitions.
Next, observe that
G(τ) =M
X
j∈J
τjsj(p(τ))
=M

 X
j∈Jg
τgsj(p(τ)) +
X
r̸=g,r̸=0
X
k∈Jr
τrsk(p(τ))


=M

τgSg + X
r̸=g,r̸=0
τrSr

 .
DifferentiatingG(τ) with respect toτ g gives
∂G
∂τg
=M

Sg +τ g ∂Sg ∂τg + X r̸=g,r̸=0 τr ∂Sr ∂τg

 .(25)
Finally, substituting equations (24) and (25), we can express condition (23) as
−
PG
g=1
P
j∈Jg Θj,g1
∂sj
∂pj (eD j −e j)
Sg1 +τ g1
∂Sg1
∂τg1 + P r̸=g1,r̸=0 τr ∂Sr ∂τg1 >−
PG
g=1
P
j∈Jg Θj,g2
∂sj
∂pj (eD j −e j)
Sg2 +τ g2
∂Sg2
∂τg2 + P r̸=g2,r̸=0 τr ∂Sr ∂τg2 .(26)
Evaluating condition (26) at zero subsidies (i.e.,τ g = 0,∀g) yields condition (5) in Proposition 2.
A.4 Total effects of budget-neutral reallocation
Proposition 1 and 2 in the main text and the proofs in Appendix A.1 and A.3 have focused on
themarginaleffects of changing per-unit subsidies across fuel types. We now examine thetotal
effects of a budget-neutral reallocation. Specifically, for a fixed government budget, we provide a
condition under which one fuel-specific policy yields a greatertotalemissions reduction than the
other.
LetG(τ) denote total government expenditure under subsidy vectorτ. For a subsidy policy
targeting fuel typeg, letτ g( ¯G) denote the per-unit subsidy level that yields total government
41

expenditure ¯G >0, with the corresponding subsidy vector
τ g( ¯G) = (0, . . . , τg( ¯G), . . . ,0).
LetE g( ¯G)≡E(τ g( ¯G)) denote the aggregate emissions under this policy. Further, letG g(τ)
represent the total government expenditure required to sustain a per-unit subsidy levelτfor fuel
typeg.
The total emissions reduction under this policy is given by
∆Eg( ¯G) =E(τ g(0))−E(τ g( ¯G))
=
Z τg( ¯G)
0
− ∂E(τ) ∂τg

τ=(0,...,τ,...,0)
dτ
=
Z τg( ¯G)
0
− ∂E(τ)/∂τ g
∂G(τ)/∂τ g

τ=(0,...,τ,...,0)
dGg(τ)
dτ dτ
=
Z ¯G
0
− ∂E(τ)/∂τ g
∂G(τ)/∂τ g

τ=τ g(G)
dG,
(27)
whereτ g(G)≡(0, . . . , τg(G), . . . ,0). The integrand represents the marginal emissions reduction
per unit of government expenditure (marginal abatement return) at expenditure levelG.
Consequently, the subsidy policy targeting fuel typeg 1, given byτ g1( ¯G), reduces emissions
more than the policy targeting fuel typeg 2, given byτ g2( ¯G), if and only if
Z ¯G
0
− ∂E(τ)/∂τ g1
∂G(τ)/∂τ g1

τ=τ g1 (G)
| {z }
M ARg1 (G)
dG >
Z ¯G
0
− ∂E(τ)/∂τ g2
∂G(τ)/∂τ g2

τ=τ g2 (G)
| {z }
M ARg2 (G)
dG.(28)
Figure A1 illustrates condition (28) in a setting where the marginal abatement return declines
with total government expenditure. Observe that comparing the marginal abatement returns at
the zero-subsidy baseline, as in Propositions 1 and 2, is equivalent to comparing they-intercepts of
M ARg1(G) andM ARg2(G). Similarly, comparing the marginal abatement returns at the current
subsidy level would be equivalent to comparing the vertical lines at ¯G. Our empirical analysis of
HEV- vs. BEV-focused subsidy policies yields results consistent with this illustration wheng 1 and
g2 denote the HEV and BEV fuel types, respectively. Specifically, the first part of Section 6.2 shows
that an HEV-focused subsidy policy yields a higher marginal abatement return at the zero-subsidy
baseline than a BEV-focused policy (by the blue intercept). The second part of Section 6.2 shows
that the HEV-focused policy also achieves a greater total emission reduction (by the blue-shaded
area).
42

Figure A1: Comparison of total effects
A.5 Derivation of the subsidy pass-through matrix under Bertrand-Nash setup
Fix a subsidy policyτ= (τ 1,· · ·, τg,· · ·, τG). Recall thatpis aJ×1 net consumer price vector
whose element is given byp j =p G j −τ g, wherep G j is a gross price set by firms andτ g is the per-unit
subsidy given toj∈J g. LetBbe aJ×Gsubsidy assignment matrix whose (j, g) entry is given
byB jg =1{j∈J g}. Then,p=p G −Bτ.
From the Bertrand-Nash first-order condition (13) in the main text, define aJ×1 function
F(p,τ) by
F(p,τ)≡s(p) +∇(p)(p+Bτ−mc) = 0,
where∇(p) = Ω◦ ∇s p(p). Assume thatFis continuously differentiable in a neighborhood of (p,τ)
and that ∂F ∂p′ is invertible. Then, by the Implicit Function Theorem, theJ×Gsubsidy pass-through
matrix Θ is given by
Θ =− ∂p ∂τ =  ∂F ∂p′ −1  ∂F ∂τ  .(29)
First, observe that
∂F
∂τ =∇(p)B.(30)
We next examine ∂F ∂p′ . Thej-th row ofF(p,τ) is given by
Fj(p,τ) =s j(p) +
JX
l=1
∇(p)jl (pl + (Bτ) l −mc l).
43

Then, the (j, k) entry of ∂F ∂p′ is given by
 ∂F
∂p′

jk
= ∂Fj
∂pk
= ∂sj
∂pk
+∇(p) jk +
JX
l=1
∂∇(p)jl
∂pk
(pl + (Bτ) l −mc l)
= ∂sj
∂pk
+∇(p) jk +
JX
l=1
Ωjl
∂2sl
∂pk∂pj
(pl + (Bτ) l −mc l).
(31)
Writing equation (31) in vector notation and substituting it together with (30) in (29) gives
Θ =

  ∇s p(p) ′ | {z }
demand slope
+∇(p) | {z }
demand slope / ownership
+K(p,τ)| {z }
demand curvature


−1 
 ∇(p)| {z }
demand slope / ownership
B

 ,(32)
where
(K(p,τ)) jk =
X
l
(pl + (Bτ) l −mc l)Ωjl
∂2sl
∂pk∂pj
.
44

B HEVs and PHEVs
An HEV, which utilizes both an internal combustion engine and an electric motor, is more fuel-
efficient than conventional ICEVs (gasoline, diesel, and LPG). Its superior fuel economy is achieved
through the following mechanisms:
1.Regenerative braking:When an HEV decelerates, its motor switches to generator mode,
capturing the vehicle’s kinetic energy and converting it into electricity. The HEV stores this
energy, which would have been wasted in conventional ICEVs, to propel the vehicle later.
2.Engine optimization:When the engine operates inefficiently (e.g., at low speeds or in
stop-and-go traffic), an HEV runs exclusively on the electric motor. Conversely, when the
engine generates more power than required while running in its high-efficiency range, the
excess power is used to charge the battery.
3.Stop-start system:An HEV automatically shuts off the engine whenever the vehicle comes
to a stop and restarts it using the electric motor, thereby preventing fuel waste during idling.31
Higher fuel economy results in lower fuel consumption per km, which concurrently reduces
both tank-to-wheel emissions (from combustion) and well-to-tank emissions (associated with fuel
production and distribution). Consequently, HEVs generate lower fuel-cycle GHG emissions than
conventional ICEVs.
Similar to an HEV, a PHEV can charge its battery through the internal mechanisms described
above. However, unlike HEVs, a PHEV can also be plugged into an external power source (the
grid) to charge its battery, as Figure B2 shows.
Figure B2: HEV vs PHEV
31Many standard ICEVs have also been equipped with stop-start systems in recent years.
45

C Additional data description
Charging network
We obtain charger data managed by the Korean Environment Corporation. 32 These data contain
charger-level information on the installation year and street address. We use four separate datasets,
each recording chargers available at the end of each year from 2020 to 2023. 33
We calculate the number of chargers in each market (year-by-province level) as follows. First, for
the years 2020 through 2023, we directly obtain the market-level charger counts from the respective
datasets. Second, for the years prior to 2020, we reconstruct the number of available chargers in
each market based on the installation years reported in the 2020 baseline dataset. For example,
the total number of chargers in Seoul in 2015 is constructed by aggregating all chargers located in
Seoul with an installation year less than or equal to 2015.
Figure C1 illustrates the evolution of the charging network over time in South Korea. Each
circle represents the number of chargers at a given street-level address. The number of chargers
began to increase rapidly in 2017, driven by government incentives and growing electric vehicle
demand. Chargers were primarily installed around apartment complexes, public parking lots, public
institutions, and commercial areas.
Country-year-level GHG emissions intensity of electricity generation
The country-year-level GHG emissions intensity of electricity generation (in g CO 2e/kWh) is ob-
tained fromOur World in Data. We utilize the 2022 intensity levels for our counterfactual analysis
in Subsection 6.3. Since these measures are not adjusted for grid losses (i.e., transmission losses are
not accounted for), we merge this dataset with the country-year-level transmission loss rate data
obtained from theWorld Bank. 34
Accounting for transmission losses, the adjusted GHG emission factor is calculated by scaling
the unadjusted intensity data:
GHG emission factor = Unadjusted GHG emission factor·
 100
100−grid loss (%)

Table C1 provides the adjusted GHG emission factors for 148 countries and the world average,
alongside the transmission loss rates (as a percentage) for 2022.
32https://www.keco.or.kr/en/
33Each of these four datasets was retrieved from the Public Data Portal:https://www.data.go.kr/en/index.do
34Our World in Data:https://ourworldindata.org/grapher/carbon-intensity-electricity;World Bank
Data:https://data.worldbank.org/indicator/EG.ELC.LOSS.ZS
46

Figure C1: Charging network: 2013, 2017, 2020, and 2023
(a) 2013
 (b) 2017
(c) 2020
 (d) 2023
Notes: This figure illustrates the evolution of the charging network over time in South Korea. Each circle represents
the number of chargers at a given street-level address.
47

Table C1: GHG emissions intensity of electricity generation and grid loss across countries in 2022
Code Level Loss (%) Code Level Loss (%) Code Level Loss (%)
WORLD 526 6.87 PER 324 11.10 MMR 613 8.02
CRI 26 8.39 ROU 330 9.75 ISR 625 4.67
NPL 28 15.32 NLD 339 4.00 HTI 628 14.92
PRY 28 11.77 R W A 350 17.62 TGO 634 24.63
ALB 28 13.68 KHM 353 13.65 SSD 636 3.90
ISL 28 2.68 NIC 358 19.18 QAT 639 5.71
COD 30 9.04 IRL 359 7.23 DOM 644 9.98
ETH 31 23.06 CMR 360 21.97 MYS 649 6.90
NOR 31 4.54 ZWE 384 22.48 BF A 649 12.46
CHE 40 7.44 CHL 392 5.00 MUS 651 5.51
SWE 43 5.61 ITA 406 6.74 PHL 667 9.59
UGA 71 19.32 PRK 407 15.50 ERI 676 12.53
NAM 75 39.22 LBN 421 9.76 GNQ 676 10.88
FRA 85 7.44 GRC 423 10.88 KWT 700 8.97
TJK 106 18.24 SUR 424 11.61 DZA 701 9.62
URY 121 8.82 TZA 429 18.57 HKG 714 4.48
NZL 122 7.32 USA 430 4.56 EGY 717 19.87
BRA 122 15.35 HND 430 31.85 TTO 719 5.17
SL V 126 10.61 GER 440 4.55 YEM 720 18.91
ZMB 126 11.46 VNM 443 6.20 TUN 723 21.74
FIN 135 3.90 KOR 453 3.20 IDN 725 6.81
KEN 142 22.85 BLR 471 6.81 AZE 726 7.52
BEL 144 3.50 RUS 479 8.56 MDA 726 10.88
L V A 146 7.18 CIV 486 14.96 IRN 728 10.04
AUT 148 4.69 ARG 494 20.51 BGD 734 7.79
SVK 149 4.92 BGR 501 4.97 BIH 740 7.71
LUX 152 6.60 MDG 504 5.28 MKD 747 16.36
MOZ 155 17.28 SGP 506 0.28 JAM 765 26.61
CAN 163 4.01 CZE 509 4.02 SAU 770 9.07
SWZ 173 26.43 PAK 513 14.83 POL 778 5.80
KGZ 177 17.20 GAB 529 18.89 SRB 806 11.77
GEO 181 7.97 GHA 531 11.54 MAR 806 17.79
PAN 182 7.18 BOL 534 9.03 ZAF 811 10.04
AGO 194 11.27 TUR 535 8.85 CUB 820 21.95
DNK 213 5.61 MEX 536 11.87 IND 826 14.91
ECU 213 15.01 JPN 542 4.10 SYR 864 21.00
COL 219 7.71 MLT 544 8.02 TCD 867 28.99
LTU 219 17.67 LKA 557 8.46 KAZ 907 8.27
GTM 220 12.91 MNE 564 14.36 MNG 910 14.08
ESP 238 8.59 EST 565 13.74 BHR 931 3.02
HUN 248 7.77 CYP 571 2.72 BEN 968 38.46
LAO 249 4.68 NGA 579 14.08 BRN 981 8.98
PRT 251 10.24 ARE 584 4.73 LBY 1 040 20.17
ARM 258 6.58 GIB 588 2.86 BW A 1 119 24.22
VEN 262 31.14 SEN 606 13.02 UZB 1 175 4.55
SDN 262 22.08 JOR 606 10.96 COG 1 280 44.58
GBR 274 8.53 THA 606 7.47 NER 1 306 46.68
SVN 275 6.21 OMN 607 9.78 TKM 1 446 9.64
HR V 277 11.67 CHN 607 3.42 IRQ 1 690 59.25
UKR 285 9.99 AUS 608 4.91
Notes: This table provides the adjusted emissions intensity of electricity generation (g CO 2e/kWh) for 148 countries
and the world average, as well as the transmission loss rate (as a percentage) for 2022.
48

D Micro moments
Second choice survey
We utilize second choice responses of consumers to construct micro statistics matched to simulated
model counterparts. As illustrated in Berry et al. (2004) and Conlon and Gortmaker (2025), data on
second choices help identify a random coefficient parameter that governs rich substitution patterns
between products. For example, the correlation between the attributes of the first and second
choice cars of a consumer is informative about the degree to which consumers substitute toward
similar vehicles.
As described in the main text, two surveys oversample consumers who purchased low-market-
share vehicles such as BEVs, HEVs, or some luxury foreign cars, and undersample those who
purchased high-market-share vehicles. Consequently, the micro survey data and the aggregate
car sales data are not perfectly consistent with one another. As noted in Conlon and Gortmaker
(2025), this compatibility between aggregate and micro data is an issue when researchers utilize
moment conditions from both data sources in estimation. For example, if the aggregate and micro
data are incompatible, there may be no set of parameters that simultaneously satisfies the moment
conditions derived from both aggregate and micro data.
To address this concern, we utilize the inverse sampling weights recorded by the data provider
to correct underlying oversampling and undersampling issues in survey data. Based on market
reports and sales information, the data provider calculates and provides an inverse sampling weight
for each individual response. As expected, almost all responses with BEVs as the primary choice,
and most responses with HEVs as the primary choice, have inverse sampling weights less than one.
Observed second choice micro statistics are constructed as follows. Letjdenote the first-choice
product andkthe second-choice product of surveyed consumeri. Letxbe a vehicle attribute, such
as a dummy for BEV, HEV, diesel, gasoline, or SUV, or driving cost measured as fuel cost per
kilometer. Conditional onj, k̸= 0, an observed correlation of an attributexbetween the first and
second choice cars is given by
Pn
i wi(xij − xj)(xik − xk)pPn
i wi(xij − xj)2pPn i wi(xik − xk)2 ,(33)
wherew i is an inverse sampling weight foriand the bar notation indicates a simple average.
The second choice survey conducted in 2023 includes responses from consumers who bought
cars in 2022 and 2023, and the survey conducted in 2018 includes responses from consumers who
bought cars in 2017 and 2018. For each of the vehicle attributes described above, we use equation
(33) to compute the observed micro statistics separately for the 2017–2018 and 2022–2023 market
samples. We then match these observed micro statistics to their model-simulated counterparts.
A model-simulated counterpart to the correlation between the first and the second choice char-
acteristic can be computed as follows using the notation in Conlon and Gortmaker (2025). Let
θbe a vector of all parameters andv p(θ) be a micro partpwhich is an expected value of micro
49

valuev pijkt for individualiwhose first choice isjand second choice iskin markett. LetTbe a
set of markets in which observed micro statistics are computed. In our case,Tis either a set of
markets in year 2017-2018 or a set of markets in year 2022-2023. For givenθand 1 000 individual
demographic and Halton draws in each markett∈Twith equal weights, a micro partv p(θ) can
be computed as
vp(θ) =
P
t∈T
P
i∈It
P
j∈Jt∪{0}
P
k∈Jt∪{0}\{j} wit ·s ijkt (θ)·w dpijkt ·v pijkt P
t∈T
P
i∈It
P
j∈Jt∪{0}
P
k∈Jt∪{0}\{j} wit ·s ijkt (θ)·w dpijkt
,
wheres ijkt (θ) is an individuali’s choice probability of first choicejand second choicekand
wit = 1 1000 . Since our survey is conditioned on the case in which both first and second choice are
inside goods, we letw dpijkt =1{j, k̸= 0}. 35 Each micro valuev pijkt generates a different micro
partv p(θ) denoted by below:
v1(θ)← −v 1ijkt =x jt ·x kt
v2(θ)← −v 2ijkt =x jt
v3(θ)← −v 3ijkt =x kt
v4(θ)← −v 4ijkt =x 2 jt
v5(θ)← −v 5ijkt =x 2 kt
Finally, a model-simulated counterpart to the correlation between the first and the second choice
characteristicsxis given by the standard correlation formula:
f(v(θ)) = v1(θ)−v 2(θ)·v 3(θ)q
v4(θ)−(v 2(θ))2
q
v5(θ)−(v 3(θ))2
An upper panel of Table D1 reports these observed and simulated values of micro statistics
from our main demand estimation result with mileage heterogeneity presented in the right panel
of Table 4.
Mileage data
In addition to the second choice survey, we use KTSA’s vehicle inspection data to help identify the
mileage interaction parameters. Using samples for the entire period (2012-2023), we compute the
average daily mileage (annual mileage divided by 365) for vehicles of each of the five fuel types:
BEV, HEV, diesel, gasoline, and LPG. We then take LPG daily mileage as the reference point and
compute the percentage difference between the daily mileage of each of the four remaining fuel
types and that of LPG.
35This survey weight is different across each combination ofi,j, andksince survey is not conducted in a perfectly
random manner. In an ideal situation where we have an access to each survey weight across all combinations ofi,j,
andk, or to analytical survey weighting formula, we may put different weights across each combination to address
underlying sampling issues in a survey. Since this situation is hardly a case, we instead use inverse sampling weights
when we compute the observed micro statistics as described earlier.
50

To compute model counterparts to observed micro statistics described above, we follow the
notation used earlier. In this case, a micro partv p(θ) is defined by
vp(θ) =
P
t∈T
P
i∈It
P
j∈Jt∪{0} wit ·s ijt(θ)·w dpijt ·v pijt P
t∈T
P
i∈It
P
j∈Jt∪{0} wit ·s ijt(θ)·w dpijt
,
wheres ijt(θ) is an individuali’s choice probability ofjandTis a set of entire markets (2012-2023).
Each combination ofv pijt and a survey weightw dpijt generates a different micro partv p(θ):
v1(θ)← −v 1ijt = dailymileagei andw d1ijt =1{j∈BEV}
v2(θ)← −v 2ijt =1{j∈BEV}andw d2ijt =1{j̸= 0}
v3(θ)← −v 3ijt = dailymileagei andw d3ijt =1{j∈LPG}
v4(θ)← −v 4ijt =1{j∈LPG}andw d4ijt =1{j̸= 0}
Then, the model-simulated percentage difference between the expected daily mileage of BEVs and
LPG is computed as
f(v(θ)) =
 v1(θ)·v 4(θ)
v2(θ)·v 3(θ) −1

·100
The percentage differences between the expected daily mileage of each of the remaining fuel types
and that of LPG are computed analogously.
A lower panel of Table D1 reports these observed and simulated values of micro statistics from
our main demand estimation result with mileage heterogeneity presented in the right panel of
Table 4.
51

Table D1: Observed and simulated values of micro moments
Moment Market Observed Simulated Difference
Second choice
CORR(Cost per km jt,Cost per km kt |j, k̸= 0) 2022-2023 0.551 0.472 0.079
2017-2018 0.519 0.364 0.155
CORR(BEVjt,BEV kt |j, k̸= 0) 2022-2023 0.662 0.650 0.012
2017-2018 0.707 0.638 0.068
CORR(HEVjt,HEV kt |j, k̸= 0) 2022-2023 0.380 0.410 -0.030
2017-2018 0.301 0.247 0.054
CORR(Dieseljt,Diesel kt |j, k̸= 0) 2022-2023 0.382 0.330 0.051
2017-2018 0.568 0.519 0.049
CORR(Gasolinejt,Gasoline kt |j, k̸= 0) 2022-2023 0.453 0.474 -0.021
2017-2018 0.558 0.509 0.049
CORR(SUVjt,SUV kt |j, k̸= 0) 2022-2023 0.540 0.590 -0.050
2017-2018 0.655 0.618 0.037
Mileage:
E(mileagei|j∈BEV)−E(mileagei|j∈LPG)
E(mileagei|j∈LPG) ×100 2012-2023 13.3838 13.3841 -0.0003
E(mileagei|j∈HEV)−E(mileagei|j∈LPG)
E(mileagei|j∈LPG) ×100 2012-2023 9.3668 9.3668 0.0000
E(mileagei|j∈Diesel)−E(mileagei|j∈LPG)
E(mileagei|j∈LPG) ×100 2012-2023 5.9953 5.9953 0.0000
E(mileagei|j∈Gasoline)−E(mileagei|j∈LPG)
E(mileagei|j∈LPG) ×100 2012-2023 -19.6870 -19.6870 0.0000
Notes: This table presents observed and simulated values of micro moments used in the estimation of the random
coefficients model with mileage heterogeneity (RC logit 2). The size of the micro data is as follows: 4 145 for second
choice data for 2022-2023 market, 4 035 for 2017-2018 market, and 69 707 543 for mileage data.
52

E Calculation of vehicle-level and market-level GHG emissions
E.1 Calculation of vehicle-cycle and fuel-cycle GHG emissions
Evaluating the environmental effects of BEV and HEV subsidies requires calculating the vehicle-
cycle and fuel-cycle GHG emissions of each product-year combination.
V ehicle-cycle GHG emissions
Unfortunately, data on vehicle-cycle emissions are not available for South Korea. Instead, we adopt
the estimates of Kelly et al. (2023) for each fuel type of sedans and SUVs sold in the U.S., shown in
Figure E1. In doing so, we assume that vehicle-cycle energy use and the resulting GHG emissions
in Korea are comparable to those in the U.S., which is reasonable given the similarity in fossil fuel
generation shares between the two countries; according to Table E1, the share is 59.6% in the U.S.
in 2020 and 58.2% in Korea in 2023.
For each BEV body type (sedan and SUV), Kelly et al. (2023) reports three emission esti-
mates based on driving ranges of 200, 300, and 400 miles. According to Figure E1, producing a
400-mile-range BEV generates nearly twice the GHG emissions of producing an ICEV, while the
corresponding emission gap for a 200-mile-range BEV varies between 25% and 32%. We utilize
linear interpolation to calculate the vehicle-cycle GHG emissions for each product-year combina-
tion based on the driving range information sourced from CARISYOU, a South Korean automotive
data provider.
Table E1: Electricity generation mix
Power source U.S. Korea
Natural gas 36.8 26.8
Coal 22.8 31.4
Nuclear 20.3 30.7
Renewables 19.4 8.4
Other sources 0.7 2.6
Notes: This table presents the electricity generation mix of the U.S. in 2020 and Korea in 2023. Other sources include
biomass, hydrogen, and residual oil. Sources: Kelly et al. (2023); The 11th Basic Plan for Long-Term Electricity
Supply and Demand (2024–2038), Ministry of Trade, Industry and Energy of Korea, 2025.
F uel-cycle GHG emissions
1. ICEVs and HEVs: We calculate the fuel-cycle GHG emissions per km (in g CO 2e/km) for
each ICEV and HEV as follows. First, for each product, we collect the official trim-year-level
tailpipe (tank-to-wheels) CO 2 emissions (in g CO 2/km) from CARISYOU and calculate the
median for each year. Because official CO 2 emissions tend to understate actual emissions,
we adjust these figures using benchmarks provided by the International Council on Clean
Transportation (ICCT) (2024). Specifically, given that the gap between official and actual
53

CO2 emissions averaged approximately 14% in the European market in 2022, we multiply the
median by 1.14 and adopt this figure as the product-year-level tailpipe CO 2 emissions.
Next, given that CO 2 emissions constitute 95% or more of total GHG emissions from trans-
portation,36 we convert the tailpipe CO 2 emissions (in g CO 2/km) into tailpipe GHG emis-
sions (in g CO 2e/km) by applying a conversion factor of 1.05. For instance, the 2020 Toyota
Camry HEV is available in two trims (LE and XLE) with CO 2 emissions of 92 and 95 g/km,
respectively. We calculate the tank-to-wheels GHG emissions for the 2020 Toyota Camry
HEV as 111.92 g CO 2e/km (93.5×1.14×1.05).
Finally, tank-to-wheels GHG emissions constitute the majority of the fuel-cycle GHG emis-
sions for ICEVs and HEVs (e.g., Elgowainy et al., 2016; Prussi et al., 2020; Choi et al., 2020).
Based on Choi et al. (2020), 37 we assume that tank-to-wheels GHG emissions constitute
86% of fuel-cycle GHG emissions for an ICEV or HEV in South Korea, and therefore divide
the former by 0.86 to obtain the latter. Continuing with the above example, the fuel-cycle
GHG emissions per km for the 2020 Toyota Camry HEV are calculated as 130.14 g CO 2e/km
(111.92 / 0.86).
2. BEVs: The well-to-tank GHG emissions for a BEV are calculated by dividing the GHG
emission factor for South Korea (453 g CO 2e/kWh in 2022) by the vehicle’s fuel economy (in
km/kWh). Since a BEV generates no tailpipe emissions, its well-to-tank GHG emissions are
equivalent to its fuel-cycle GHG emissions.
In this way, we calculate the fuel-cycle GHG emissions per km for the 2 304 product-year
combinations in our dataset. 38
36The other two GHG emissions are CH 4 and N 2O. See “Emissions of Carbon Dioxide in the Transportation
Sector,” Congressional Budget Office, December 2022; and “Greenhouse Gas Emissions from a Typical Passenger
Vehicle,” Environmental Protection Agency, March 2018 for more details on tailpipe GHG emissions.
37They modified the GREET model to reflect the specific conditions and energy policies of South Korea, and
found that the ratio of tank-to-wheels GHG emissions to the fuel-cycle GHG emissions ranges between 85.6% to
86.7% across fuel types.
38There are 61 product-year combinations in the 2012–2019 period for which we cannot retrieve the official trim-
year-level tailpipe CO2 emissions from CARISYOU. We exclude these combinations when calculating GHG emissions
from the outside option.
54

Figure E1: Vehicle manufacturing cycle GHG emissions
(a) Sedan
(b) SUV
Notes: The top panel (bottom panel) of this figure presents vehicle-cycle GHG emissions for a sedan (an SUV) in
the U.S. Source: Kelly et al. (2023), pp. 137–138.
55

E.2 Estimation of market-level GHG emissions changes
We estimate the market-level GHG emissions (15) as
bEτ m =M m 1 N NX i=1 Eτ i .(34)
Using (14), the change in cumulative GHG emissions in marketmfollowing the policy transition
fromτtoτ ′, ∆E (τ,τ ′) m , is estimated as
d∆E (τ,τ ′) m = d∆E (τ,τ ′) m,FC + d∆E (τ,τ ′) m,VC + d∆E (τ,τ ′) m,outside,(35)
where
d∆E (τ,τ ′) m,FC = Mm N NX i=1 X j∈J T·m i ·e F C j ·∆ˆsij
d∆E (τ,τ ′) m,VC = Mm N NX i=1 X j∈J eV C j ·∆ˆsij
d∆E (τ,τ ′) m,outside = Mm N NX i=1 T O ·m i ·e F C 0 ·∆ˆsi0
where ∆ˆsij = ˆsτ ′ ij −ˆsτ ij denotes the change in the consumer’s choice probability after the policy
transition fromτtoτ ′. Equation (35) decomposes the change in emissions within the market into
three terms: changes in (i) fuel-cycle emissions ( d∆E (τ,τ ′) m,FC), (ii) vehicle-cycle emissions ( d∆E (τ,τ ′) m,VC),
and (iii) outside emissions, which are the emissions from the outside option ( d∆E (τ,τ ′) m,outside).
We can further decompose the changes in fuel-cycle (as well as vehicle-cycle) emissions by fuel
type: ICEVs (combining gasoline, diesel, and LPG), BEVs, and HEVs. Specifically,
d∆E (τ,τ ′) m,FC = Mm N NX i=1 T·m i

 X
j∈JICEV
eF C j ·∆ˆsij + X
j∈JBEV
eF C j ·∆ˆsij + X
j∈JHEV
eF C j ·∆ˆsij

 .
This decomposition allows us to isolate the individual contribution of each fuel type to the overall
change in fuel-cycle emissions.
56

F Mileage heterogeneity and policy effects
In Section 5, we show that a consumer’s driving intensity plays a critical role in their fuel-type
choice. Furthermore, a subsidy policy induces a disproportionately strong response among high-
mileage consumers, causing them to shift away from conventional ICEVs toward subsidized vehicles
(either HEVs or BEVs) at a higher rate than low-mileage consumers.
To illustrate this point, we simulate the 2023 shifts in within-fuel-type market shares under two
distinct counterfactual scenarios: a BEV-focused subsidy and an HEV-focused subsidy. Accord-
ing to Figure F1, the increase in the market share of the subsidized fuel type following subsidy
implementation is larger among consumers with higher driving intensity under both policies. For
instance, the rise in the HEV market share among consumers in the 40–60 km daily mileage range
(2.1 percentage points) is 76% larger than that among consumers in the 0–20 km range (1.2 per-
centage points).
The RC logit 1 specification (which imposes the homogeneous mileage assumption) fails to
capture these shifts in the consumer mileage composition across fuel types following policy imple-
mentation. Consequently, this restricted specification understates the environmental effectiveness
of the subsidies, as shown in Table 8.
Figure F1: Changes in within-group market shares for BEVs and HEVs (2023)
Notes: This figure presents the nationwide averages and two-standard-deviation intervals of the predicted changes in
choice probabilities across five daily mileage groups. The panels compare two counterfactual policy transitions relative
to a baseline of no subsidies: the change in BEV choice probability under BEV subsidies, and the corresponding change
in HEV choice probability under HEV subsidies. For reference, the nationwide averages are equivalent to the changes
in within-group market shares.
57

G Additional figures and tables
Table G1: BEV nameplates and subsidy
# BEV registered # nameplate
year total with subsidy without subsidy with subsidy without subsidy
2012 4 4 0 1 0
2013 125 125 0 3 0
2014 507 507 0 5 0
2015 2 042 2 042 0 5 0
2016 2 612 2 612 0 6 0
2017 7 149 7 149 0 9 0
2018 22 183 22 104 79 10 1
2019 23 163 22 954 209 11 1
2020 19 100 18 591 509 12 2
2021 35 684 34 454 1 230 16 8
2022 62 172 60 979 1 193 22 7
2023 65 851 62 379 3 472 25 11
Notes: This table presents the number of BEVs and nameplates, with and without subsidies, for each year between
2012 and 2023. Source: The official BEV policy website of South Korean government.
58

Table G2: Average daily mileage by province and fuel type
Fuel-type
Province Gasoline Diesel Hybrid BEV LPG Total
Seoul 26.8 35.5 35.8 37.0 32.5 29.7
Busan 28.8 37.7 39.0 39.2 34.8 31.8
Daegu 28.9 38.9 39.8 43.7 35.6 32.4
Incheon 29.0 38.0 39.8 41.2 34.5 32.3
Gwangju 29.4 39.0 39.5 41.3 37.3 33.4
Daejeon 28.5 38.7 39.7 41.0 36.0 32.2
Ulsan 28.7 36.6 38.7 40.1 35.2 31.5
Sejong 32.6 43.5 45.4 48.5 41.4 36.9
Gyeonggi 30.2 39.5 41.1 42.8 36.9 33.7
Gangwon 29.8 40.3 43.0 42.6 37.8 34.0
Chungbuk 30.5 40.3 42.5 43.8 38.4 34.3
Chungnam 31.5 41.0 43.2 43.7 39.8 35.3
Jeonbuk 30.6 41.0 42.4 44.9 38.8 34.9
Jeonnam 31.9 41.5 43.4 43.8 40.0 36.1
Gyeongbuk 30.7 40.4 43.3 44.3 39.0 34.4
Gyeongnam 30.9 40.3 42.6 43.0 38.3 34.3
Jeju 27.6 35.3 37.1 40.5 33.4 30.8
Notes: This table presents the average daily mileage (km) by province and fuel type.
59

Table G3: Estimation results of logit and nested logit demand models
Variable OLS Logit IV Logit Nested Logit
Price / Avg. Income -0.406 -6.013 -2.076
(0.062) (0.739) (0.411)
Cost per km -2.522 -0.668 -0.145
(0.090) (0.227) (0.088)
Acceleration -0.271 18.033 6.229
(0.461) (2.659) (1.290)
Size 0.324 0.859 0.296
(0.048) (0.134) (0.063)
Network 0.032 0.248 0.202
(0.069) (0.069) (0.073)
Entry year -0.623 -0.457 -0.148
(0.032) (0.041) (0.032)
Exit year -1.707 -1.720 -0.565
(0.034) (0.041) (0.107)
lns j|g 0.677
(0.063)
Own elasticity
- Median -0.371 -5.490 -5.755
- Weighted average -0.291 -4.302 -4.370
Notes: This table presents OLS and IV estimates of the linear demand model given by ln(s jm/s0m) =x jmβ−α
pjm
¯ym +
ξjm, as well as estimates of the nested logit demand model given by ln(sjm/s0m) =x jmβ−α
pjm
¯ym +ρlns j|g +ξ jm. The utility specifications also include fixed effects for nameplate, province, and fuel type interacted with year. Two cost
shifters—import tariff rate and raw material price interacted with vehicle weight—are used as excluded instruments
for price in the IV logit estimation, while the within-group product count is used as an additional instrument in the
nested logit estimation. Robust standard errors, clustered by market, are reported in parentheses.
60

Table G4: First-stage regression results
IV Logit Nested Logit
Variablep j/¯ylns j|g
Raw material prices×Weight 0.135 0.130 1.364
(0.127) (0.128) (0.252)
Tariff rates 0.037 0.037 -0.224
(0.005) (0.005) (0.013)
Group product count -0.004 -0.006
(0.001) (0.002)
Cost per km 0.308 0.313 -2.811
(0.026) (0.026) (0.094)
Acceleration 3.365 3.364 -1.763
(0.131) (0.131) (0.394)
Size 0.115 0.114 0.144
(0.011) (0.011) (0.049)
Network 0.019 0.011 -0.109
(0.011) (0.011) (0.046)
Entry year 0.033 0.034 -0.654
(0.004) (0.004) (0.033)
Exit year -0.020 -0.020 -1.602
(0.004) (0.004) (0.031)
R-squared 0.955 0.955 0.781
SW F statistic 26.29 16.40 22.01
Observations 34 629 34 629 34 629
Notes: This table presents the first-stage regression results from the standard logit and nested logit demand models.
The model also includes fixed effects for nameplate, province, and fuel type interacted with year. Robust standard
errors, clustered by market, are reported in parentheses.
61

Table G5: Own- and cross-price elasticities by fuel type
Panel A: Own-price elasticities
Fuel Type Mean Min P10 P50 P90 Max
BEV -6.1823 -16.9671 -9.0477 -6.9034 -4.4898 -0.4315
HEV -5.9411 -10.3288 -7.3308 -5.9954 -4.8752 -3.2270
Diesel -6.3986 -10.1832 -7.7114 -6.2005 -4.9920 -1.9965
Gasoline -5.6100 -16.1493 -7.4639 -6.0916 -4.8829 -2.0436
LPG -5.9390 -9.9424 -7.2039 -5.7529 -4.5009 -3.1466
Panel B: Cross-price elasticities
BEV HEV Diesel Gasoline LPG
BEV 0.0374 0.0030 0.0012 0.0012 0.0018
HEV 0.0012 0.0273 0.0034 0.0026 0.0063
Diesel 0.0008 0.0041 0.0086 0.0019 0.0040
Gasoline 0.0006 0.0030 0.0021 0.0055 0.0040
LPG 0.0010 0.0064 0.0032 0.0032 0.0243
Notes: The top panel reports summary statistics (sales-weighted average, minimum, 10th percentile, median, 90th
percentile, and maximum) for the own-price elasticities for products within each fuel type. The bottom panel reports
the unweighted average cross-price elasticity of demand for products with the fuel type indicated in the row with
respect to the prices of products with the fuel type indicated in the column.
62

Table G6: Equilibrium prices of BEVs and HEVs in 2023
Brand and No BEV Pass- Brand and No HEV Pass-
Nameplate sub. sub. through Nameplate sub. sub. through
Battery Electric Vehicle Hybrid electric vehicle
Audi Q4 e-tron 60.12 60.32 0.94 Hyundai Grandeur 43.46 43.28 1.11
Audi e-tron 82.03 82.35 0.90 Hyundai Santa Fe 38.43 38.26 1.10
BMW i4 65.53 65.34 1.04 Hyundai Sonata 32.42 31.98 1.27
BMW i5+ 81.42 82.27 - Hyundai Elantra 25.99 25.37 1.38
BMW i7+ 159.62 160.02 - Hyundai Kona 30.02 29.83 1.12
BMW iX+ 110.59 111.30 - Hyundai Tucson 31.42 31.18 1.15
BMW iX1 58.31 58.24 1.02 Kia K5 31.40 30.92 1.30
BMW iX3 63.92 63.87 1.01 Kia K8 39.87 39.60 1.17
GM Korea Bolt EUV 40.62 40.55 1.01 Kia Niro 29.61 29.42 1.12
GM Korea Bolt EV 38.57 37.85 1.07 Kia Sportage 34.15 33.94 1.13
Genesis G80 80.04 81.46 0.71 Kia Sorento 39.35 39.17 1.11
Genesis GV60 62.48 63.61 0.76 Kia Carnival 45.62 45.48 1.09
Genesis GV70 69.84 70.99 0.75 Lexus ES 60.46 60.27 1.12
Hyundai Ioniq 5 53.25 52.77 1.04 Lexus LS 137.83 137.72 1.07
Hyundai Ioniq 5 N 69.29 70.21 0.77 Lexus NX 62.65 62.46 1.12
Hyundai Ioniq 6 54.60 55.02 0.96 Lexus RX 88.86 88.74 1.07
Hyundai Kona 44.67 44.25 1.04 Lexus UX 45.81 45.58 1.15
KG Mobility Torres 45.76 45.05 1.07 Renault Korea XM3 31.34 31.11 1.14
Kia EV6 55.09 54.48 1.06 Toyota RA V4 42.39 42.16 1.14
Kia EV9 64.20 65.14 0.80 Toyota Sienna 61.28 61.10 1.11
Kia Niro 45.96 45.36 1.05 Toyota Alphard 88.52 88.41 1.07
Kia Ray 27.08 27.36 0.96 Toyota Camry 38.02 37.77 1.16
Mercedes EQA 57.30 57.22 1.02 Toyota Crown 51.74 51.54 1.12
Mercedes EQB 64.19 64.19 1.00 Toyota Prius 37.92 37.65 1.16
Mercedes EQE+ 84.90 85.53 - Toyota Highlander 62.04 61.86 1.11
Mercedes EQE SUV + 98.97 99.89 -
Mercedes EQS+ 134.77 135.25 -
Mercedes EQS SUV + 137.22 137.62 -
Tesla Model 3 58.89 58.64 1.07
Tesla Model S+ 119.59 120.39 -
Tesla Model X+ 129.10 129.42 -
Tesla Model Y 54.64 54.07 1.15
Volkswagen ID.4 54.31 53.51 1.09
Notes: This table compares the equilibrium prices (in million KR W) of 33 BEVs under the no-subsidy and current
BEV subsidy scenarios, as well as those of 25 HEVs under the no-subsidy and HEV subsidy scenarios, for the year
2023. + denotes models that are not subsidy-eligible.
63

Table G7: Emission savings of BEV and HEV subsidy policies across different emission factors
Country Code GHG factor BEV subsidy HEV subsidy
Norway NOR 31 2 805 2 040
France FRA 85 2 629 2 048
Brazil BRA 122 2 509 2 054
Denmark DNK 213 2 213 2 068
Portugal PRT 251 2 089 2 073
United Kingdom GBR 274 2 015 2 077
Peru PER 324 1 852 2 084
Netherlands NLD 339 1 803 2 087
United States USA 430 1 507 2 101
Germany GER 440 1 475 2 102
South Korea KOR 453 1 433 2 104
World Average WORLD 526 1 195 2 115
Japan JPN 542 1 143 2 118
China CHN 607 932 2 127
Malaysia MYS 649 795 2 134
Philippines PHL 667 737 2 137
Indonesia IDN 725 548 2 145
Poland POL 778 376 2 153
India IND 826 220 2 161
Kazakhstan KAZ 907 -43 2 173
Notes: This table compares the emission savings (in thousand tonnes of CO 2e) under BEV and HEV subsidy policies
across 20 distinct GHG emission factor levels, representing 19 countries and the world average. These nations are
selected to ensure a representative geographic distribution that spans the entire spectrum of global GHG emission
factors.
64

Figure G1: Trends in BEV and HEV sales shares by country
Notes: This figure shows trends in BEV and HEV shares of new light-vehicle sales by country from 2015 to 2024.
PHEV sales are not included in either the BEV or HEV categories.Source: Korean Automobile & Mobility Association
(KAMA).
65

Figure G2: 17 provinces in South Korea
Notes: This figure illustrates how provinces (first-tier administrative divisions) are geographically defined in South
Korea.
66

Figure G3: Sales share trend of each fuel type
Notes: This figure presents sales share of each fuel type during the sample period, 2012–2023.
67

Figure G4: EV subsidy dispersion by year (2016 - 2023)
(a) 2016
 (b) 2017
(c) 2018
 (d) 2019
(e) 2020
 (f) 2021
(g) 2022
 (h) 2023
Notes: This figure presents a histogram of the nameplate/province-level total (national + local) BEV subsidy for
each year (2016-2023).
68

Figure G5: Nameplate-level local subsidies of selected provinces
Notes: This figure presents a scatter plot of the nameplate-level local BEV subsidy for the following selected provinces
(Seoul, Daegu, Gyeonggi, Chungbuk, and Jeju) over the entire sample period (2012-2023). Each point represents a
province-nameplate-level observation.
69

Figure G6: Diversion by fuel types
(a) From BEV
 (b) From HEV
(c) From Diesel
 (d) From Gasoline
(e) From LPG
Notes: This figure presents the annual diversion ratios across fuel types between 2018 and 2023, which are computed as
follows. First, we calculate the diversion ratio from productjwith fuel typeF 1 to fuel typeF 2 (or the outside option)
in a market:D j,F2 ≡ P k∈JF2 Dj,k ≡ P k∈JF2 ∂sk/∂pj −∂sj /∂pj ,whereJ F2 denotes the set of products with fuel typeF2. Then,
we compute the sales-weighted average diversion ratio across fuel types in the market:D F1,F2 ≡ P j∈JF1 wjDj,F2 ,
wherew j is productj’s share within fuel typeF 1. Finally, we average the diversion ratios across the 16 markets in
each year: ¯DF1,F2 .
70

Figure G7: Within-group market shares for each fuel type (2023)
Notes: Each panel in this figure presents nationwide averages (equivalent to within-group market shares) and two-
standard-deviation intervals for the predicted choice probabilities of a specific fuel type, calculated separately for
each of the five daily mileage groups. To compute these statistics, we first sort the 16 000 simulated consumers in
2023 (16 provinces×1 000 individuals) into five groups based on their daily mileage: 0–20, 20–40, 40–60, 60–80, and
80–100 km. Next, for each individuali, we predict the choice probability for fuel typegas ˆs ig = P j∈Jg ˆsij. We
then calculate the nationwide averages and two-standard-deviation intervals of these probabilities for each mileage
group. To ensure that the population share of each regional market is proportionally reflected, we conduct weighted
resampling using market sizes as weights.
71

Figure G8: Market-level distribution of the marginal abatement return by fuel type
Notes: The figure plots the distributions of market-level marginal abatement returns by fuel type with the unrestricted
subsidy pass-through. Each bubble represents the abatement return for a specific fuel-type in a given market, with
bubble sizes scaled by the fuel-type’s total sales in each market.
72
