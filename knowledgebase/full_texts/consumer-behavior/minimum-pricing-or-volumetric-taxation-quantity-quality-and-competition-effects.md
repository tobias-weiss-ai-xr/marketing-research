---
title: Minimum pricing or volumetric taxation? Quantity, quality and competition effects of price regulations
  in alcohol markets
url: https://arxiv.org/abs/2509.14116
category: consumer-behavior
subcategory: empirical
date: 2025-09
venue: ''
authors:
- Celine Bonnet
- Fabrice Etile
- Sebastien Lecocq
source: arxiv
pdf_url: https://arxiv.org/pdf/2509.14116
pages: 91
chars: 206090
fetched_at: '2026-11-08T13:13:33+00:00'
kb_version: 1
---

# Minimum pricing or volumetric taxation? Quantity, quality and competition effects of price regulations in alcohol markets

Minimum pricing or volumetric taxation?
Quantity, quality and competition effects of price
regulations in alcohol markets∗*
Céline Bonnet†, Fabrice Etilé‡, Sébastien Lecocq§
June 2025
Abstract
Reforming alcohol price regulations in wine-producing countries is challenging, as cur-
rent price regulations reflect the alignment of cultural preferences with economic interests
rather than public health concerns. We evaluate and compare the impact of counterfactual
alcohol pricing policies on consumer behaviors, firms, and markets in France. We develop
a micro-founded partial equilibrium model that accounts for consumer preferences over
purchase volumes across alcohol categories and over product quality within categories, and
for firms’ strategic price-setting. After calibration on household scanner data, we compare
the impacts of replacing current taxes by ethanol-based volumetric taxes with a minimum
unit price (MUP) policy of C0.50 per standard drink. The results show that the MUP in
addition to the current tax outperforms a tax reform in reducing ethanol purchases (-15%
vs. -10% for progressive taxation), especially among heavy drinking households (-17%).
The MUP increases the profits of small and medium wine firms (+39%) while decreasing
the profits of large manufacturers and retailers (-39%) and maintaining tax revenues stable.
The results support the MUP as a targeted strategy to reduce harmful consumption while
benefiting small and medium wine producers. This study provides ex-ante evidence that is
crucial for alcohol pricing policies in wine-producing countries.
Keywords: alcohol, corrective taxes, minimum price, demand modelling, market structure.
JEL Classification: D12, D62, H21, H23.
*We thank the Institut National du Cancer (INCa, AAP-SHS-E-SP-2015), the Mission interministérielle de lutte contre les drogues et les
conduites addictives (MILDECA), the Agence nationale de la recherche (ANR-19-CE21-0004 PRIMOFOOD), Toulouse School of Economics
and ANR (ANR-17-EURE-0010), Paris School of Economics and ANR (ANR-17-EURE-0001), and the AXA Research Fund (AXA Awards
2015, Fabrice Etilé) and . This project was part of the “Impact épidémiologique et économique des politiques de prix de l’alcool sur les cancers”
(Epidemiological and economic impact of alcohol pricing policies on cancer) research project, coordinated by Fabrice Etilé. INCa, MILDECA,
ANR, AXA, INRAE, PSE, TSE, and BSE were not involved in the design of the study and are not responsible for its implementation, results
and interpretations. We thank Christine Boizot-Szantai and Valérie Orozco, for collaboration on data acquisition and preparation, and Marine
Friant-Perrot, Amandine Garde, Chantal Julia and Mathilde Touvier for advices on the epidemiological and legal aspects of alcohol markets.
We thank seminar participants at Paris School of Economics, UMR GAEL (Grenoble), UMR SMART (Rennes), UMR BETA (Nancy), 2nd
W AP conference (Bordeaux) for comments.
†Toulouse School of Economics and INRAE,
‡Paris School of Economics and INRAE, Corresponding author: UMR INRAE 1393 Paris-Jourdan Sciences Economiques and Ecole
d’Economie de Paris, 48 Boulevard Jourdan, 75014 Paris. fabrice.etile@inrae.fr
§INRAE, University of Bordeaux, CNRS, INRAE, BSE.
arXiv:2509.14116v1  [econ.GN]  17 Sep 2025

1 Introduction
Alcohol consumption is a major contributor to the global burden of disease, with risks including
cancer, cardiovascular disease, car accidents, injuries, mental health problems, and cognitive de-
cline. It represented 5.3% of all deaths worldwide in 2016 (Shield, Manthey et al. 2020). In France,
it remains a major cause of health and social problems, although consumption has been halved
since the Second World War. Seven per cent of adult deaths (41,000) were attributable to alco-
hol in 2015 (Bonaldi and Hill 2019; Shield, Marant-Micallef et al. 2018; Disease 2018; Praud et
al. 2016). Pricing policies are considered by international public health experts as part of any na-
tional comprehensive strategy to reduce the burden of alcohol-related disease (OMS 2010; INSERM
2021), with calls to target the ethanol content of beverages through minimum unit pricing (MUP)
or volumetric taxes (Cheatley et al. 2021; Cecchini and Devaux 2021). Implementing these recom-
mendations would completely overhaul the regulatory framework for alcohol prices, in France as
in other wine-producing Mediterranean or Central European countries, where alcohol taxation is
historically geared more towards protecting domestic wine producers than towards public health
objectives.1 The specific tax rates on wines are close to zero while they represent approximately
55% of the total volumes of ethanol purchased by households. 2 Therefore, it is not surprising that,
despite the international consensus, attempts to reform alcohol price regulation policies have faced
strong opposition from political representatives. In this paper, we estimate and compare the impacts
of minimum pricing and volumetric taxes on alcohol purchases, equilibrium prices, consumer wel-
fare, and firms’ profits. Our objective is to understand whether there exists a price policy that could
benefit public health while being acceptable by most wine producers.
We develop a model that account both for consumer choices over quantity and quality and for
manufacturers’ and retailers’ price-setting decisions. Modeling the supply-side of the market is
crucial for two reasons. First, strategic price reactions on the supply-side can limit the effective-
ness of behavioral health policies (Bonnet and Réquillart 2013; Allais et al. 2015; Dubois et al.
1France is the world’s 2nd largest wine producer (ahead of Spain, but behind Italy) and 1st largest exporter. The
wine sector represents almost 550,000 jobs, including 250,000 direct jobs (Palle 2013).
2Angus et al. (2019) compares the 2018 tax rates (excise duties) on wine, beer, and spirits in European countries.
The UK, Ireland, Nordic, and Baltic countries have higher rates than other EU countries, with no exemptions for wines.
Wines are not subject to specific duties in the Mediterranean and Central European countries. Unsurprisingly then,
France, Spain, Italy, Portugal and Bulgaria tried to block the Scottish Minimum Unit Price policy after its introduction
in 2012.
1

2018). Two ex-post evaluation studies of the UK alcohol market found that tax increases are under-
transmitted to the prices of basic products and over-transmitted to the prices of premium products,
for all alcohol categories (Wilson et al. 2021; Ally et al. 2014). This under-transmission reduces
the effectiveness of taxation policies if heavy drinkers prefer to buy basic brands. Second, whether
or not a government will be able to reform price regulations will depend on how much different
reforms can affect the profits of the different alcohol producers, from large companies to small wine
farmers, who have a lot of political influence in France. It is therefore important to document the
potential impacts of any reform on firms’ profits. On the demand-side, we consider a multi-level
demand system setting in which households can purchase various volumes of alcohol in six distinct
categories, ciders, beers, aperitifs, spirits, still wines, and sparkling wines. Each category represents
a specific market in which consumers can choose from a variety of products with different ethanol
content. This separability assumption allows us to neatly disentangle the quality and quantity ef-
fects of price policies. As the heterogeneity in the ethanol content between alcohol categories is
large, substitutions in volumes between categories can have large health impacts. Quality effects
within categories, i.e. substitutions between product varieties, may have smaller impacts, but they
drive the strategic price responses of firms. We calibrate the demand functions using longitudinal
homescan data on the alcohol purchases of a representative panel of French households. These data
contain detailed information on prices and product attributes, and the panel dimension allows us
to account for household preferences for ethanol by conditioning all the estimations on purchase
volumes observed during the previous year. On the supply-side, manufacturers face an oligopolistic
price competition and contract with retailers to sell their products to the consumers. Retailers also
sell their own brands (Private Labels). We use the market-specific demand functions to calibrate
the supply-side models, and we are able to recover margins and marginal costs for each product
variety sold in the six markets. It renders possible the simulation of firms’ strategic price reactions
to changes in price regulation policies and consumer behavior. We eventually gain access to evalu-
ations of the impact of pricing policies on firms’ profits, and we can identify the losers and winners
from various counterfactual pricing policies.
We consider several reforms of price regulation policies. In the current tax system, wines are
almost exempt from specific taxes, taxes on beers and ciders are low, and spirits bear most of the
2

burden. We test replacing current taxes by two alternative volumetric tax systems as in Griffith
et al. (2019): a uniform tax rate based on the ethanol content of products; a progressive tax rate that
increases with the ethanol content. The progressive tax maintains a relative disadvantage for spirits,
which consists of a large share of total ethanol purchases observed for high-risk households. These
two taxes are calibrated on one of the two following objectives, assuming that there are no market
reactions. The first objective is neutrality in terms of fiscal revenues, while the second objective is
neutrality of alcohol-specific taxes for public finances. 3 Fiscal neutrality leads to a lower tax rate
(around 7.2 cts/g of ethanol) than neutrality for public finances (14.6 cts/g).
As an alternative to these four tax reform scenarios, we consider introducing a minimum unit
price policy on top of the current tax system. The introduction of a minimum price may make it pos-
sible to better target abusive consumers if they disproportionately buy cheap products with a high
alcohol content. In fact, the results of ex-post evaluations of the minimum pricing policy implemen-
ted in Scotland and Wales show that it led to the substitution of high-alcohol beers and ciders for
lower-alcohol products and that the impact was concentrated in 20% of households with the highest
per capita alcohol consumption, regardless of income category (Llopis et al. 2021; O’Donnell et
al. 2019). Griffith et al. (2022) also use their reduced-form empirical model of the UK market to
show that generalizing the Scottish minimum price throughout the UK would be preferable to a uni-
form tax with the same impact on total consumption, because it affects the heavy drinkers relatively
more. In a theoretical paper, Calcott (2019) shows that the two instruments can be complementary
if quality and quantity of alcohol are substitutes and if the harm is caused by consumers of cheaper
alcohol. We therefore examine a sixth scenario, where the minimum price is combined with the
replacement of the current tax system by a progressive tax.
We find that the addition of a Minimum Unit price set at 0.5e/standard drink to the current tax
system outperforms the four tax reforms. A minimum price policy would reduce average purchases
(in g. of ethanol) by 15.0%, compared to -10.3% for a high progressive ethanol tax. Supply-side
price responses would only slightly increase the effectiveness of the minimum price policy (-13.7%
3The total social cost in 2010 was C120 billion, of which C66 billion was due to mortality and C48 billion to lost
welfare and productivity. The cost to public finances, net of tax revenues and pensions saved due to premature deaths,
was estimated at around C3 billion (Kopp 2015). Tax revenues covered only 42% of public health costs. These figures
justify the implementation of new policies aimed at reducing the population’s alcohol consumption in order to reduce
alcohol-related health and social harm.
3

without response). Low tax rates will have the unintended effect of increasing purchases (in g. of
ethanol), by favoring substitutions from still wines to spirits as mechanic consequences of rising
taxes on the former and falling taxes on the latter.
The superiority of the minimum price policy is essentially due to the quantity effect, as it re-
duces purchases in all alcohol categories. We also find larger effects for heavy-drinking households
(-17.2%). Importantly, a minimum price policy would significantly increase the profits of small and
medium wine manufacturers (+39.3%) to the detriment of large manufacturing firms and retailers
(-38.7%). In fact, it would increase the price competitiveness and market shares of products posi-
tioned in the middle-quality segment, to the detriment of entry-level products currently produced
and marketed by large firms. As the minimum price mechanically increases price-cost margins,
lower quality products make higher unit profits, but their market share drops dramatically, so that
their total profit falls. Finally, tax revenues remain virtually unaffected (-2.3%), because the increase
in V AT revenues offsets the contraction of the market.
Our results complement studies that have provided ex-post evidence that minimum prices and
volumetric taxes are effective in increasing consumer prices, reducing purchases and consumption,
and improving health (Wagenaar et al. 2010; Roodman 2020; Elder et al. 2010; Stockwell et al.
2012; Zhao and Stockwell 2017; Anderson et al. 2021; Robinson et al. 2021; Xhurxhi 2020; Grif-
fith et al. 2022). 4 This ex-post evidence is mainly available for English-speaking countries, which
historically have a drinking culture of binge drinking, beer and spirits, as opposed to wine-producing
countries where wine consumption is integrated into everyday social occasions such as meals (Gor-
don et al. 2012).
Here, we provide ex-ante evidence on the structural impacts of price policy reforms on con-
sumers, firms, and markets for a wine-drinking country. As in Griffith et al. (2022) for the UK,
we compare minimum pricing with progressive volumetric taxation. Beyond the many methodolo-
gical differences, they also find that minimum pricing and ethanol-based progressive taxation with
high tax rates can achieve the same impacts on consumption (with taxation slightly outperforming
minimum pricing in their case). However, our study goes further in the identification of losers and
4Our results are in line with ex-post evaluation studies of the Scottish Minimum Unit Price that have also exploited
Kantar homescan data. In particular, Anderson et al. (2021), using a difference-in-difference ex-post evaluation design
with England as the control group, find that the Scottish MUP resulted in a -7.7% drop in purchase volumes (-8.6% for
the Welsh MUP). Griffith et al. (2022) find an average reduction of 11% in alcohol units purchased per adult per week.
4

winners on the supply-side because we are interested in the acceptability of pricing policies, due to
the strong lobbying of the wine industry (Millot et al. 2022). Here, the industrial organization of
the market is a key difference between Anglo-Saxon countries, and France and other Mediterranean
countries. The deep-rooted cultural preservation of the wine sector in Mediterranean countries and
the resulting current alcohol tax policies explain why minimum pricing is more effective in reducing
ethanol purchases. Our article sheds light on the public debate in France on how to regulate alcohol
more effectively to reduce its consumption and the burden it places on society.
We finally contribute to the literature on empirical IO modeling, with a structural model of de-
mand for quality and quantity that capture patterns of substitution between alcohol products within
each alcohol category, and substitutability or complementarity between alcohol categories. Our ap-
proach is essentially based on the sequential estimation of demand for quality and then demand for
quantity, the latter being conditioned on the former through a structural household-specific qual-
ity index for each alcohol category that measures household preferences for product differentiation
within the category. Most studies to date have used continuous choice demand models that treat
alcohol or alcohol categories as homogeneous (Sharma et al. 2016; Srivastava et al. 2015; ˇCiderová
and Šˇcasný 2022), or discrete choice models that better account for product differentiation but force
substitutability between categories (Griffith et al. 2019; Miravete et al. 2018). Our model goes bey-
ond this division between the quantity and quality dimensions of household choices to account for
richer patterns of behavioral reactions on the demand side.
The remainder of the paper is structured as follows. In the next section, we present our data and
discuss some stylized facts about the French alcohol market. This helps us to motivate our pricing
policy reform scenarios. In Section 3, we detail the structural model, which is calibrated in Section
4. In Section 5, we present the key results, detail the main mechanisms at play, and report additional
heterogeneity analyzes on households and firms. Section 6 concludes with a discussion of the limits
of the study.
2 Data, facts and price regulation scenarios
This section presents the data and stylized facts regarding the structure of alcohol markets in France.
In line with these, we define scenarios of policy reform regarding minimum unit pricing and ethanol-
5

based volumetric taxation.
2.1 Data
2.1.1 Households
This study is based on the 2014 Kantar Worldpanel (KWP) homescan data. The data cover all pur-
chases for consumption at home made by a representative panel of French households (excluding
overseas territories).5 In 2014, 28,375 households were enrolled in KWP, of which 24,177 were con-
sidered actively reporting their purchases of food and beverages for at least one four-week period.
They report their purchases of barcoded products using handheld scanning devices. Approximately
half of them (N = 13,395) also belong to a representative subpanel in which participants must report
their purchases of products without barcodes. 6 Wines, ciders and beers produced by small manu-
facturers do not always have barcodes because they are sold directly in the vineyard or brewery, in
open-air markets, or in cellars or specialty stores. We work with this subpanel and select the 12,170
households that were active in at least three periods of four weeks out of 13 periods that the year
contains.
We further restrict the sample to those households that purchased alcoholic beverages at least
once in 2014 (N=11,463), under the reasonable assumption that a reform of alcohol price regulations
will be justified by a public health objective and will not have the effect of encouraging abstinent
households to become consumers.
In all of our analyses and estimations, we use the four-week sample weights provided by KWP
for each household and each household-purchase act, to make our analysis representative of the
French market. Appendix Section A.1 provides more details on sample selection and sample
weights. Appendix Table A.1 presents some descriptive statistics on household characteristics.
5While the KWP data covers well the population and purchases for consumption at home, as benchmarked against
Family Budget Surveys (Lecocq, Orozco et al. 2023), alcohol consumption away from home is not observed. We come
back to this point in the discussion of the results.
6Information on products with barcodes is directly retrieved from a product database, by using the barcode. For
products without barcodes, KWP asks participants to report a number of standardized attributes, e.g. commercial
segment, brand, packaging, etc.
6

2.1.2 Markets and products
We choose to group products into six categories: ciders, beers, aperitifs, spirits, still wines, and
sparkling wines. This definition of alcohol categories closely follows the SIRENE classification
of manufacturers used by the French National Statistics Office (INSEE). 7 The SIRENE open data
were completed by a careful reading of the professional press on the organization of these six mar-
kets to understand their structure and what the largest manufacturers were in 2014. It appeared that
each of these six alcohol categories constitutes a specific alcohol market with its own supply and
demand characteristics. In supply side modeling, we treat them as six disjoint alcohol markets. We
again used insights from the professional press to divide each alcohol category into subcategories
that map key quality differences in the product space. For example, beers are divided into three
subcategories, depending on their alcohol content: Alcohol-free, Bock/Premium, Special. We dis-
tinguish sweet ciders from raw ciders. Sparkling wines include champagne and other sparkling
wines. For still wines, we use the well-known distinction between table wines (Vins de table),
local wines (Vins de Pays), and wines with a designation of origin (Vins d’Appellation). Spirits
include five subcategories (Rum, Whisky, Aniseed, Liquors, Other spirits), and this is also the case
for Aperitifs (Cocktails/Punches, Liquor wines, Natural Sweet Wines, Amer/Gentiane/Vermouth,
Other aperitifs).
We added information on brand manufacturers using the SIRENE open data and manual search
of information. These information are matched with our purchase data to construct a nomenclature
that makes a distinction between the largest market players, firms with national brands (NB), and
retailers with private label brands (PL), and an aggregate of smaller manufacturers.8 Within manu-
facturing firms, other smaller brands are aggregated.
We eventually consider manufacturers and retailers as additional characteristics because they
7The SIRENE classification downloaded fromhttps://www.data.gouv.fr/fr/datasets/
base-sirene-des-entreprises-et-de-leurs-etablissements-siren-siret/distinguishes spirits (1101Z:
Production of distilled alcohol beverages), sparkling wines (1102A: Production of sparkling wines), still wines (1102B:
Production of still wines), ciders and fruits wines (1103Z: Production of ciders and fruit wines), aperitifs (essentially
the 1104Z class - Production of other non-distilled fermented beverages, and some products in other classes), and beers
(1105Z and 1106Z: Production of beers, malt production)
8The term ’National Brand’ designates the brands that are distributed on the whole French territory, by all retailers
(e.g. Ricard is distributed by all retailers). The term ’Private label’ designates products produced by the retailer itself
(for example, a specific brand produced byIntermarchéand sold only inIntermarché).
7

play a critical role in pricing and marketing (e.g., shelf positioning, price discounts). Vertical rela-
tionships between manufacturers and retailers are likely to modify supply-side adjustments to price
regulations, and therefore it is important to consider brands sold at different retailers as distinct
competing choice alternatives. The retailers were grouped into seven distribution channels, corres-
ponding to the five largest retailers, an aggregate of hard-discounters, and an aggregate of other
shopping places (see Appendix Section A.2 for details).
By interacting categories, subcategories, brands, manufacturers, and retailers, we obtain 1,662
different product varieties. For each variety and four-week period, we calculate the purchase
volumes and the expenditure at national level (adjusting them for sampling weights), and finally
the average unit price in C/litre. Appendix Section A.3 provides details on the computation of key
variables, such as alcohol content, product prices, purchase volumes.
KWP Homescan data offer the advantage of providing detailed information on purchase volumes,
expenditures, and product characteristics: brand, key differentiating attributes, and alcohol content.9
Available information on alcohol content is crucial for the analysis of alcohol taxation, which con-
sists of excise duties (ie, based on the volume purchased, not the value), which can vary depending
on the category of alcohol, the size of the manufacturing firm, and the alcohol content of products.
We constructed the excise and volumetric taxes faced by each variety in 2014 by combining fiscal
information on tax rates applied in 2014 with information on the alcohol categories and subcategor-
ies, the size of manufacturing firms and the alcohol content. Appendix Section A.5 presents the
excise taxes applied in 2014 and 2024, showing that the tax regulations did not change much over
10 years.
2.2 Facts
2.2.1 Markets
Table 1 presents some market statistics for each alcohol category. Still wines represent 45.34% of
purchase acts, followed by beers (21.89%) and spirits (15.38%). 10 Aperitifs, sparkling wines, and
ciders represent less than 10% of purchase acts each. The second line shows that ciders, beers and
9Appendix Section A.4 show that our data match well with the expenditure statistics provided by the 2017 Family
Budget Survey.
10A purchase act is the purchase of a product variety in a given day at a given retailer by a given household.
8

Table 1: Market statistics
Ciders Beers Aperitifs Spirits Still wine Sparkling wines
Share purchase volumes (%) 2.22 31.56 5.13 7.81 48.28 4.99
Average price (e/L) 2.43 (0.67) 2.36 (3.52) 6.07 (2.82) 16.38 (5.72) 3.78 (1.34) 10.41 (8.86)
Number of subcategories 2 3 5 5 3 2
Number of manufacturers 6 25 29 14 12 35
Number of brands 8 52 32 48 26 38
Number of product varieties 75 395 336 404 230 222
CR4 36.07 61.37 35.20 51.11 11.78 21.60
HHI index (∈]0;10,000[) 1473 1388 608 986 342 391
Market shares, in volumes (%)
Main national brands 36.12 73.17 47.26 62.58 13.09 43.89
Private labels 54.50 21.02 33.20 28.99 38.26 32.34
Aggregate of other small brands 9.38 5.81 19.54 8.43 48.65 23.16
Prices (e/L)
Main national brands 2.95 (0.70) 2.93 (1.22) 7.09 (3.57) 18.24 (6.84) 3.81 (1.89) 14.58 (14.46)
Private labels 2.04 (0.24) 1.34 (0.51) 5.08 (2.15) 11.51 (5.18) 2.86 (1.04) 11.74 (7.51)
Aggregate of other small brands 3.23 (0.74) 3.45 (1.10) 6.75 (4.12) 16.93 (8.28) 3.26 (1.37) 12.42 (7.23)
Notes: Market statistics computed over N=1,662 brands observed over 13 periods of 4-weeks, and purchase acts made
by a sample of N=11,463 households. A purchase act is the purchase of a given product variety in a given day at a given
retailer by a given household. Standard deviations in parentheses describe the variability of prices across periods and
product varieties. Market shares are calculated from household purchase volumes (in L) adjusted for household and
purchase period-specific sample weights.
still wines are the cheapest alcohol categories on average, whereas spirits form the most expensive
category.
Table 1 statistics also show that the six markets differ considerably in terms of structure and
competition. The number of varieties is quite heterogeneous in the six markets, from 75 for ciders to
404 for spirits. For ciders, only six manufacturers (including the aggregate of "other manufacturers")
compete by selling eight brands. For spirits, 14 manufacturers compete through 48 brands. To better
measure the level of competition in each market, we compute the concentration ratio (CR4) and the
Herfindahl-Hirschman Index (HHI). 11 Their computation is based on the market shares of firms
apart from private labels and the aggregate of other small brands, meaning that these two measures
11TheCR 4 is defined as the sum of the market shares of the four largest national firms in an industry. The HHI is
defined as the sum of the squares of the market shares of the national firms within the industry. Hence,CR 4 represents
the market power of the largest firms, whereas HHI measures more globally the concentration of all national large firms
within the industry
9

represent a lower limit of concentration. These two categories can be thought of as a competitive
fringe offering product varieties that are cheaper or with specific characteristics.
The beer and spirits markets can be perceived as oligopolies, since theirCR4 are equal to 61 and
51%, respectively. In contrast, there are no such large firms in the market of still wines, sinceCR4 is
equal to 12%. Except for ciders, beers, and spirits where the HHI of the main national manufacturers
is at a moderate level of competition, the three other markets do not seem to have a high level of
concentration at the manufacturer, given their HHI below 1000. This is partly explained by a large
private label market share and/or a large market share of small national brands. In fact, those three
markets are largely made up of small producers, and it is particularly important for wines, 23.2%
for sparkling wine and 48.6% for still wines, and to a lesser extent 19.5% for aperitifs. This share
is much lower for the other markets: 5.7% for beers, 9.4% for ciders, 8.4% for spirits, and 5.8% for
beers. This emphasizes a specificity of the French wine market: compared to the US, Australian or
Chilean markets, the French wine sector was and is still characterized by the important role of small
and medium manufacturers as independent winemakers and cooperatives (Cubertafond 2015).
Although all national brands are always more expensive than private label products, the rank-
ing between the main national brands and the other small national brands varies between markets.
Although small national brands for cider and beer are on average more expensive than the main
national brands, the reverse is true for the other four markets. Additional descriptive statistics in
Table A.7 in the Appendix further illustrate the heterogeneity of the product offer between the sub-
categories within the six markets.
2.2.2 Household choices over quantity and quality
Households buy on average 0.83 liters of ethanol per week per household member aged 16 or older.
Taking into account the alcohol content of the varieties, this translates to 79.4g of pure ethanol per
week, or nearly 8 standard drinks, while the French recommendation guidelines set the maximum
at 10 standard drinks per week.
The first panel of Table 2 shows the breakdown of purchases in terms of volume, in liters, and
standard drinks. Still wines top the list, with 48.3% of volume in liters and 49.9% in standard
drinks. The second category with the highest purchase, beer, accounts for 31.6% of volumes but
only 13.2% of standard drinks. The figures for spirits are 7.8% and 25.7%, respectively, showing
10

their important contribution to alcohol intake.
The second panel of Table 2 describes the distribution of the unit values of purchases. The price
ineper liter paid by households is the highest for spirits, ahead of sparkling wines and aperitifs. 12
With the exception of wines, variations in median unit prices between categories are positively
correlated with the median ethanol content of the alcohol category. Unit prices for still wines show
little price differential with beer, contrary to what is often observed in countries with more of a
brewing tradition than a wine-growing one.
2.3 Motivations for price policy reforms
In general, the current price regulation system does not align with public health objectives. The
third panel of Table 2 also shows that the different alcohol categories are subject to very different
tax burden due to the differences in the specific volumetric taxes currently applied. The implicit tax
rate, corresponding to excise duties and other taxes including V AT (Ruiz and Trannoy 2008), ranges
from a rate close to V AT (nearly 21%) for the three least taxed categories, ciders, still and sparkling
wines, to almost 220% for spirits and 50% and 63% for beers and aperitifs, respectively. The fourth
panel of Table 2 reports the average tax levels per standard drinks. Clearly, the current tax design is
much more favorable to ethanol in wines than to the ethanol in spirits.
In addition, the current price regulation system is regressive, as shown by Lecocq, Orozco et
al. (2023) in a descriptive study based on the same data. They find that the household tax ef-
fort rates (the ratio of taxes excluding V AT paid to disposable income) is 0.45% for low-income
households compared to 0. 11% for high-income households. 13 Consistent with the gap in con-
sumption patterns and effort rates between income groups, the implicit tax rate (the ratio of tax
burden to pretax expenditure) is 53.2% for low-income households versus 41.7% for high-income
households. They show that the observed regressivity of the current tax system can be attributed to
higher overall volumes of alcohol per capita purchases and higher share of spirits relative to wines
in low-income households, where income is adjusted for household OECD consumption units (see
12The large dispersion of unit values for sparkling wines is explained by the vertical differentiation between the
subcategory of champagnes and that of other sparking wines.
13The latter is likely to reflect both social differences in circumstantial exposure to addiction risks, and differences in
individual self-control efforts. It is clearly difficult to measure the relative importance of circumstances and efforts in
these inequalities.
11

Table 2: Household purchase volumes, prices and taxes across the six alcohol markets
Ciders Beers Aperitifs Spirits Still wine Sparkling wines
Consumption
Purchase volumes (L/year) 1.69 24.05 3.91 5.95 36.79 3.80
Share purchase volumes (%) 2.22 31.56 5.13 7.81 48.28 4.99
Standard drinks/week 0.09 1.80 0.74 3.51 6.80 0.69
Share standard drinks (%) 0.69 13.17 5.51 25.72 49.87 5.05
Alcohol content
Median alcohol degree 4.4 5.8 15.0 40.0 12.0 12.0
Prices per liter
Unit value - First quartile (e/L) 2.17 1.98 4.22 14.33 2.44 5.68
Median unit value (e/L) 2.74 2.86 6.64 16.93 3.22 8.06
Unit value - Third quartile (e/L) 3.33 3.53 9.15 20.07 4.37 24.38
Taxes
Average unit value (e/L) - all tax included 2.88 2.53 6.40 20.31 4.10 13.28
Average unit value (e/L) - V AT excluded 2.40 2.11 5.37 16.93 3.41 11.07
Average unit value (e/L) - all taxes excluded 2.39 1.76 4.37 8.54 3.38 10.98
Implicit tax rate (%) 20.79 50.40 62.83 219.42 21.56 21.14
Prices per standard drink
Average unit value (e/ standard drink) - all tax included 1.00 0.65 0.64 0.66 0.43 1.41
Average unit value (e/ standard drink) - V AT excluded 0.84 0.54 0.54 0.55 0.35 1.18
Average unit value (e/ standard drink) - all taxes excluded 0.83 0.45 0.44 0.28 0.35 1.17
Policy scenariosExpected % change in average unit price (e/L)
without market reactions
Low uniform tax +10.4 -0.4 -1.7 -33.2 +24.4 +6.9
High uniform tax +21.2 +16.6 +15.5 -16.6 +50.0 +14.7
Low progressive tax +4.9 -7.5 -1.4 -19.4 +21.5 +6.0
High progressive tax +9.7 +0.4 +13.0 +5.8 +40.2 +11.7
Minimum price +1.4 +6.3 +8.3 +3.2 +40.0 +3.2
Minimum price + Low prog. tax +5.9 +1.6 +7.2 -8.0 +46.6 +8.1
Notes: Statistics computed over N=11,463 households. Statistics weighted by household and purchase period-specific
sample weights - see Appendix Section A.3.2 for the exact formula. Implicit tax rate = 100 x tax revenue / (sales - tax
revenue).
12

Appendix Tables A.5 and A.6). From an externality-correction perspective, this raises the question
of horizontal equity, since a euro spent on pure alcohol is not taxed in the same way depending on
household income. This can be an additional legal motivation for a tax reform as discussed in Sassi
et al. (2014).
These statistics finally illustrate the specific economic importance of wine in France. It is the
most consumed and least taxed alcohol category due to its historical role in gastronomic culture and
agricultural production. Given the economic and cultural concerns about the still wine market, it
is important to clarify its market segmentation. In our data, most still wine purchases fall in the
price range that defines the low-end quality level according to market professionals (Cubertafond
2015): more than 80% of wine volumes are purchased at less than 5e/L. Wines purchased at less
than 3e/L account for 35% of purchases and almost 50% of volume, which is explained by the fall
in unit prices for wines in bag-in-box packaging, which is used primarily for low-quality product
varieties. These descriptive statistics highlight a fact that has been overlooked in the public debate
on alcohol regulation in France: a significant proportion of the volume of wine placed on the market
is of poor quality and has a low price. However, the economic importance of the sector implies that
we must pay particular attention to the designs of potential policy reforms, and we must be able to
document their effects on producers and consumers.
2.4 Policy scenarios
We are interested in scenarios of price policy reforms that can promote public health objectives
while still complying with legal constraints. From a legal perspective, any price regulation reform
must be calibrated to match either current fiscal revenues or the monetary externalities on public
finances. Regarding the first objective, Article 40 of the French Constitution prohibits any creation
or aggravation of a public burden and only authorizes the reduction of fiscal revenues if this is
offset by an increase in another revenue. The second objective, internalizing externalities (at least
partially), is a classical rationale for public policies. 14 Beyond fiscal neutrality, a second legal
constraint is that Article 110 of the Fundamental Treaty of the European Union stipulates that direct
14We abstract here from considerations regarding an optimal tax design that would specifically account for the private
externalities (e.g. productivity losses) and the internalities generated by the tax, as in Allcott et al. (2019) for instance.
Their approach requires identifying a priori those consumers who face internalities, and in the specific case of wine in
France, the argument is not well accepted by stakeholders and the general public.
13

or indirect taxation must be the same for similar goods moving freely within the Union and must not
serve as indirect protection for other goods. 15 This article severely limits the scope for reform, as
has been shown in several cases in the past.16 Only a reform motivated by a legitimate public health
objective and proportionate to that objective (i.e. sufficiently effective compared to less stringent
policies such as information campaigns) can be deemed to comply with Article 110 (Sassi et al.
2014). It will therefore necessarily have to target the ethanol content of products, whatever their
category.
Given these constraints, we will first simulate the replacement of all alcohol-specific taxes by
a single volumetric tax, either uniform or increasing progressively with the ethanol content of the
product. Under the uniform volumetric tax, one gram of ethanol has the same impact, whether it
comes from a glass of cider, wine, or spirit. In contrast, the progressive tax scheme is based on
the premise that each additional gram of ethanol is associated with an increase in marginal risks to
health. Hence, the marginal tax rate on each additional degree is increasing. This progressive volu-
metric tax is similar in spirit to the sugar taxes on soft-drinks that have recently been implemented in
the UK, Chile, or France. In practice, we will consider a multi-tiered tax scheme with six intervals
for the alcohol degree: [0;5[, [5;10[, [10;15[, [15;25[, [25;45[ and [45;100]. 17 We will assume that
marginal taxation is twice higher in the second interval than in the first, three times higher in the
third than in the first, etc.
We calibrate the uniform and progressive tax schemes to achieve one or another of the following
two objectives under the assumption that there are no reactions on the demand and supply sides of
the market: (1) fiscal neutrality (2) neutrality for public finances. Under fiscal neutrality, all alcohol
tax revenues (including V AT revenues) are left unchanged by the reform. Under neutrality for
public finances, the alcohol tax revenues (excluding V AT revenues) must cover the costs of alcohol
15Article 110: "No Member State shall impose, directly or indirectly, on the products of other Member States any
internal taxation of any kind in excess of that imposed directly or indirectly on similar domestic products. Furthermore,
no Member State shall impose on the products of other Member States any internal taxation of such a nature as to afford
indirect protection to other products"
16Article 110 raises the question of the similarity of products within a category and of possible substitutions between
categories. In case 243/84 John Walker (1986), it was ruled that whisky and liqueur wines are not like goods. In case
106/84 Commission vs. Denmark (1986), it was held that grape wines and other wines are similar. In case 170/78,
Commission vs. United Kingdom (1980), the introduction of a tax on wine five times higher than that on beer was
refused on the grounds of substitutions between the two product categories.
17For 100mL of alcohol, one alcohol degree is 1mL of pure ethanol, or 0.8g. In France, a standard drink is 10g of
ethanol.
14

for public finances (health cares and enforcement of the law, minus retirement pensions). Public
finance neutrality always leads to higher calibrated tax rates as we exclude V AT revenues from the
accounting equation. We thus end with four scenarios: Low uniform tax (fiscal neutrality), High
uniform tax (public finance neutrality), Low progressive tax (fiscal neutrality), High progressive tax
(public finance neutrality).
We will also evaluate the implementation of a minimum unit price on top of the current tax sys-
tem. The minimum unit price paid by the consumer (V AT included) will be set to 0.5eper standard
drink (10g of ethanol), which is similar to the MUP initially implemented in Scotland in 2012. This
is our fifth scenario, where existing taxes are left unaltered. Finally, as a final scenario, we will eval-
uate the implementation of the minimum price combined with the replacement of existing excises
and duties by the low progressive tax.
Appendix B provides additional details on the design and calibration of all policy scenarios,
while the lower panel of Table 2 shows their impact on unit prices in the absence of consumer
and market adjustments. Interestingly, given the distortions of current tax schemes, the average
price of still wines would increase by 20% to 50% depending on the scenario, while the average
price of spirits may fall by up to -33% under a flat tax. The flat tax is also unfavorable for ciders
and beers. This is not the case with progressive taxes, which benefit beers, penalize wines less
and are less favorable to spirits. Only a high progressive tax, aimed at cost neutrality for public
finances, would prevent a fall in the price of spirits and aperitifs. To a lesser extent, a minimum price
would also prevent such a drop. However, in all cases, the relative price of wine would increase
sharply, suggesting substitution towards other alcohols that become relatively cheaper. Only by
modeling household substitution behavior can we make predictions about these substitutions and
their consequences for pure alcohol consumption.
3 Model
In this section, we build a tractable quantitative model of alcohol markets that is informed by our
descriptive analysis of markets and household behaviors. Our goal is to capture the behavioral
mechanisms that are the most relevant to explain changes in household purchase patterns and mar-
ket equilibrium: first, substitutions between product varieties of different degrees of alcohol, and
15

substitutionsandcomplementarities between alcohol categories; second, the optimal price-setting
strategies of retailers and manufacturers. Finally, we discuss the assumptions of the model.
3.1 Consumer demand for quality and quantity
We consider alcohol consumption to be separable from the rest of consumption expenditures. The
set of products is partitioned intoAmutually exclusive product categories. In each periodt, the
householdhfirst allocates a predetermined alcohol budgetY h t for at-home consumption. Then, it
will have a number of consumption occasions that will exhaust its budgetY ah t for categorya. Each
consumption occasion consists of the choice of either consuming one productjamong the choice set
Ja t , or not consuming in categoryaand keeping the money for expenditures in other categories (their
outside option). At the beginning of the period, households have perfect anticipations regarding the
availability and price of products during the period. They allocate their budget between categories
according to the expected utility of consuming a product variety in each of these categories.
Defineq a t the quantity vector of productsjin categoryain periodt, with the related price vector
pa t . We assume that preferences over quantity are weakly separable, so that each household solves
at each period the following maximization program:
Maxqat ,∀a=1...AFh

U1h t (q1 t ), ...,UAh t (qA t )  (1)
u.c.
A
∑
a=1
pa t ′qa t =Y h t
whereF h is a regular utility function, andU ah t is the expected utility of consuming quantitiesq a t of
products in categoryaat various occasions of consumption over periodt.
We define a consumption occasionoas the consumption of one unit of a productjin any
alcohol category (whatever the unit: the goods are perfectly divisible). The number of consumption
occasions intfor an alcohol category is therefore equal to the aggregate physical quantityQ ah t =
∑ j∈Jat qah jt . At each consumption occasion, conditional on choosing a productjin categorya, the
household gets some consumption utility that is notedv ah jto. Note that this utility should be the same
for all productsjinaif the household had no taste for variety or if the products were homogeneous.
16

Thus, within-category product differentiation is an extra-source of utility, beyond the consumption
of quantityQ ah t .
When deciding to allocate its budget across alcohol categories and planning consumption occa-
sions, the household shopper has in mind the expected utility that could be obtained from consuming
a product variety in each product category conditional on the purchase of at least one product variety
in this category:
uah to ∼E j∈Jat

vah jto|Qah t >0  (2)
The conditional distribution of utilityv ah jto is identified by the observation of household purchase
behaviors. When shopping, the household decides which variety to purchase according to a standard
trade-off between money and the average utility of consuming the product on any consumption
occasion. Specifically, we assume that, at the point of purchase, the consumption utility enters the
purchase utilityV ah jto, through the following relationships:
V ah jto =−α ahpa jt +v ah jto (3)
whereα ah >0is the household marginal utility of expenditure in category a. The consumption
utility itself,v ah jto, is specified so that purchase decisions can be described by a random utility model,
where the stochastic term captures some taste for variety plus other idiosyncratic factors that affect
the expected value ofjat consumption occasiono. Households also have the choice not to purchase
a product in categoryaand keep their money for purchasing any product in any other category on
the same shopping trip: this is their outside option.
Purchase decisions are finally related to consumption utility through a Random Utility Model,
with the purchase utility associated with optionjbeing equal to:
∀j∈J a t ,∀o,V ah jto =−α ahpa jt +β ahZa jt +ε ah jto| {z }
vah jto
=V ah jt +ε ah jto (4)
17

where theε ah jto have i.i.d. Gumbel distributions, andZ a jt are sets of product attributes. In Appendix
C, we show that this setup implies that the expected utility of a consumption occasion is:
uah to = (1+bah t (pa t ))(5)
whereb ah t (pa t )is the consumer surplus from differentiation between productswithincategorya. We
suppose that the anticipated utility over the periodtof product purchases in categoryais equal to
the linear sum of expected occasion utilities:
Uah t (qa t ) =∑
o
uah to =Q ah t (1+b ah t (pa t ))(6)
We relabel the anticipated utility levelU ah t (qa t )as a quantity indexQ ah t . Then, we derive a corres-
ponding price indexP ah t that satisfies the budget constraint for alcohol categorya:
Pah t Qah t =Y ah t ⇒P ah t = Y ah t Qaht (1+b aht (pat )) (7)
This price index equals the unit value of purchases in categorya—Y ah t /Qah t — adjusted for the
index of the expected welfare surplus from quality differentiation within categorya,b ah t (pa t ). If
the products inawere not differentiated, then all would have the same price, which in turn would
be equal to the price index sinceb ah t (pa t ) =0. Only differentiation between product categories, as
captured by the first-stage budgeting decision, would matter.
Finally, we rewrite the first-stage budgeting decision with the quality-adjusted price and quantity
indices as follows:
MaxQaht ,∀a=1...AFh

Q1h t , ...,QAh t

(8)
u.c.
A
∑
a=1
Pah t Qah t =Y h t (9)
A standard demand system can be estimated to recover the price elasticity of the quantities. The
18

econometric calibration of the demand models is eventually performed in two steps. First, we
estimate a discrete random utility choice model for each product category. Second, we use these
estimates to construct the quality indicesbah t (pa t )and fit the first-stage demand system for quantities.
3.2 Supply-side price-setting decisions
To simulate the impact of price regulations on markets, we need a model of how manufacturers
and retailers set product prices. We do not observe all the determinants of these decisionsdirectly,
especially the production costs and technologies and the nature of vertical contracts. We therefore
need structural assumptions regarding the supply-side of markets to infer this information from the
observed data on purchase behaviors.
Each alcohol category in the demand model corresponds to a market. For each marketa, we
assume that manufacturers and retailers engage in two part-tariff contracts, whereby manufacturers
propose to retailers a wholesale price and a fixed franchise fee. In addition, manufacturers implicitly
use resale price maintenance (RPM), and therefore set the retail prices of national brand products
(NB) while retailers set the prices of their private label products (PL). 18 Profits are shared between
manufacturers and retailers via a set of product-specific fixed fees. This model of vertical relation-
ship helps to take into account the specific role played by PL products in the price-setting strategies
of retailers, especially in low-quality market segments.
Formally, we defineRthe number of retailers, andM a the number of manufacturers in each
separate marketain each time periodt. For notational convenience, we drop the subscriptsaandt.
The profit of retailerris given by:
Πr = ∑
j∈Sr

Q
 p j
1+τ −w j −c j

s j(p)−F j

,∀r=1, ...R(10)
whereS r is the set of products that retailerrsells,Qis the size of the market,τis the V AT rate,p j
is the retail price of productj,w j is the wholesale price of productj,c j is the constant marginal
18The two-part tariffs with RPM has been largely used in the empirical literature on the French retail market. Bonnet
and Dubois (2010) proposed an empirical test of various vertical relationships models on the French market for bottled
water. They demonstrated that the two-part tariff model with RPM provides the best performance in terms of statistical
fit. Following Rey and Vergé (2010), this model may account for situations where manufacturers have all the bargaining
power for a product and make take-it or leave-it offers, as well as for situations where retailers have all the bargaining
power.
19

cost to distribute productj,s j(p)is the market share of productj, andF j if the franchise fee that
the retailer pays to the manufacturer.19 In the specific case of PLs, we assume that the products are
sold to retailers at a wholesale pricew j equal to the marginal cost of the manufacturing firms noted
µ j.20
Each manufacturermmaximizes its profit :
Πm = ∑
j∈Gm

Q(w j −µ j −T 0 j )s j(p) +Fj  ,∀m=1, ...,M a (11)
subject to the participation constraint of each retailerΠ r ≥ eΠr,∀r=1, ...,R.G m is the set of
products that are sold by manufacturerm,w j is the wholesale price of productj,µ j is the marginal
production cost ofj,T 0 j is the excise tax, and eΠr is a fixed reservation utility that we can normalize
to zero without loss of generality.
Following Rey and Vergé (2010), under RPM, the participation constraints are binding and
manufacturers choose to set retail margins to zero. 21 Therefore, the prices of NB products sold by
the manufacturer are given by the following first order conditions for the manufacturermand for all
productsj∈G m:
∑k∈Gm
 pk
1+τ −µ k −c k −T 0 k
 ∂s k(p)
∂p jt
+s j(p) +
R
∑
r=1
∑k∈eSr
 pk
1+τ −µ k −c k −T 0 k
 ∂s k(p)
∂p jt
=0
(12)
where eSr is the set of PL products that retailerrsells. 22 These first-order conditions implies that
the manufacturer’s pricing policy depends on two factors. First, it has to optimize the competi-
tion between products in its portfolio (the two leading terms). Second, it has to account for the
19As a product is a combination of a brand and a retailer, one can define a fixed feeF j for each product and separate
the contracts that manufacturers have with each retailer.F j is then the fixed fee received by a given manufacturer (if
positive) from a given retailer.
20A retailer defines the characteristics of his own PL, organizes competition among manufacturers for delegating the
production of these PL products. This should be interpreted as a price competition with homogeneous products that
leads to a wholesale price equal to the marginal costs.
21The intuition is that RPM produces a situation where prices are set as if the retailer and the manufacturer were
integrated, and this increases total profit. The fixed fees are used to share the profits between manufacturers and
retailers.
22The marginal retail profit from NB products is zero, but they can receive fees, that do not depend on prices, to share
the total profit on NB products. Hence, the manufacturermhas just to care about the profit made by the retailer with its
PL brands, and the competition of the latter with its own brands.
20

competition of retailer brands, the so-called common agency problem (the third term).
On the retailer side, the prices of PLs in eSr are given by the first-order condition:
∑k∈eSr
 pk
1+τ −µ k −c k −T 0 k
 ∂s k(p)
∂p jt
+s j(p) =0,∀j∈ eSr.(13)
LetC j be the total marginal costs for each productj, whereC j =µ j +c j is the sum of the
marginal costs of production and distribution. Knowing the demand functionss j(p), a vector of
marginal costs for all products inJa t , bCt =  bC1t, ..,bCjt, ..,bCJt  , can be calibrated by solving equations
(12) and (13) simultaneously for all manufacturers and retailers (see, for details, Bonnet and Dubois
2010, Appendix).
3.3 Discussion of assumptions
Our modeling strategy relies on three assumptions. First, to identify the expected utility of a con-
sumption occasion within a period, we conflate purchase acts with consumption occasions. How-
ever, each purchase of a product observed in the data could be associated with one or several con-
sumption occasions (depending on the number of units purchased) that are given the same utility.
We thus assume that within each alcohol category, anticipated variations in purchase volumes across
purchase acts are not correlated with consumers’ intrinsic valuations of products on point of pur-
chase. In their first-stage decision, consumers anticipate that purchase volumes will vary randomly
across purchase acts within a period, around an average that only depends on the purchase volume
decided for the period in the first stage of decision, and the number of purchase acts in the category,
which is exogenously determined. This rules out optimal inventory management within the period.
This also excludes the possibility that, conditional on unit price, the number of units purchased is
systematically higher or lower for products associated with a higher consumption utility.23
Second, we assume that each alcohol category is one market (cider, beers, aperitifs, spirits,
still wines, sparkling wines) and that the six markets are disjoint. Hence, we impose that changes
in one market do not affect competition in the other markets, but only the total volume sold in
other markets. As a consequence, neither manufacturers nor retailers are allowed to develop a
23For instance, consumers do not systematically purchase one bottle of a Vin d’Appellation vs. two bottles of a Vin
de Pays when they opt for the former rather than for the latter and the two products have the same unit price.
21

common pricing strategy across several markets. 24 Specifying separate models for each market
allows us to implement a detailed modeling of substitutions between product varieties while keeping
the dimensionality of the household choice set reasonable. In addition, we can apply a supply-side
model that accounts for strategic price-setting decisions by manufacturers and retailers, and for the
vertical relationships between them.
Third, consistent with the assumption of disjoint markets, we separate household choices of
quantity and quality by assuming that households follow a two-stage budgeting procedure, as for
instance in Hausman, Leonard and McFadden (1995). We want to focus on substitutions in qual-
ity between product varieties within alcohol categories and substitutions or complementarities in
quantity between alcohol categories. We thus ignore other possibilities of substitutions. In par-
ticular, we do account neither for substitutions toward on-trade consumption nor for intertemporal
substitutions. We could not model substitutions toward on-trade due to a lack of appropriate data.
We will discuss this limitation in our conclusion. Regarding stockpiling, inventory behaviors may
be of some importance in understanding the seasonality of the wine market. Intertemporal substitu-
tions could be driven by the stockpiling of products during price promotion periods. The KWP data
do not provide precise information on product price promotions, and we do not observe promotions
that the consumer may face on other products.
However, following Griffith et al. (2019), we test for habit formation and stockpiling by examin-
ing the associations between past purchases and steady-state inventory levels and current purchases.
While stockpiling can produce intertemporal substitutions, habit formation would conversely pro-
duce intertemporal complementarities. Our reduced form estimation results in Appendix D show
very small effects of past purchase volumes on current purchases in regressions that control for
household and time fixed effects. We also find positive rather than negative associations between
purchase behaviors and a steady-state inventory level measure constructed under the assumption that
households manage their inventory to smooth consumption (see Hendel and Nevo 2006). Hence,
although we cannot categorically reject the existence of some form of short-term intertemporal de-
pendence in consumer behaviors, these dynamics are not of primary importance once household
preference heterogeneity is taken into account. To this end, we systematically control for the aver-
age purchase volume (in standard drinks per household adult) observed over 2013, when estimating
24National brand manufacturers were mostly different in the six alcohol markets. See the list in Appendix Table A.2
22

the models on the 2014 purchase data.
4 Calibration
4.1 Market models
4.1.1 Specification of demand functions
For each alcohol category, inference on household purchase behaviors is based on a structural de-
mand system that is derived from the Random Utility Model in equation (4). The econometric
counterpart of the household utility function is arandom coefficient logit modelthat allows for
estimating flexible household substitution patterns.
Specifically, we let price disutility vary with the characteristics of households and between al-
cohol categories:α ah =α a +δ aDh +σ aζ ah, whereD h is a vector of household characteristics, and
ζ ah is a random term distributed normally with standard deviationσ a that captures the unobserved
taste of the householdhfor the alcohol categorya. Household characteristics include the household
income category, the age category of the main shopper, and a measure of the household preferences
for alcohol. The latter is constructed from average household purchases observed in 2013, conver-
ted into standard drinks per adult household member per day, categorized into three categories of
alcohol habits: less than one standard drink, between one and two, or two and more.
We control for product-specific household utility (β ahZa jt in equation (4)) through a rich set
of fixed-effects: (1) retailer fixed-effects that account for differences in marketing policies (assort-
ments, promotions) across retailers; (2) brand fixed-effects, that account for differences in marketing
efforts (especially advertising), beyond mere differences in consumer tastes for brands; (3) fixed-
effects specific to product subcategories and sociodemographic groups, that capture sociodemo-
graphic differences in consumer tastes for product subcategories; (4) an alcohol-free times brand
fixed-effects. The set of selected fixed-effects varies from one market to another, based on a de-
scriptive analysis of household heterogeneity in product choices (see Appendix E.1.1).
The choice set does not vary across consumers. At each observed purchase occasion, the house-
hold can choose not to purchase a product in the categoryaand keep its budget for any outside
23

alcohol product. The utility of the outside option is normalized to zero, so thatα ah is the marginal
dis-utility of spending one more euro inarather than keeping it for a purchase in any other alco-
hol category. Without this outside option, a homogeneous increase in the price of all products ina
would not affect the size of the marketaand therefore the reactions of manufacturers and retailers
to changes in overall purchase volumes. The estimates of the first-stage demand system presented
thereafter shows that none of the compensated cross-price elasticities between the six categories is
negative. This preference structure implies that, for each category, the aggregate ’all products in
other alcohol categories’ can effectively be considered a substitute.
4.1.2 Identification of price elasticities
Identification of price effects leverages price variations over time and across brands and retailers
because we define product varieties by interacting brands with retailers. Prices may be endogenous
due to unobserved product characteristics that vary over time and are correlated with both price and
demand. For example, we do not observe neither the advertising efforts made by firms for their
brands nor the display on shelves in stores. These unobserved marketing efforts are likely affecting
the demand and correlated with prices, making them endogenous even if we control for retailer
fixed-effects. We therefore apply a control function approach as in Petrin and Train (2010). In a
first stage, we regress the prices on a set of instrumental variables as well as the exogenous variables
of the baseline utility function. The estimated error term of the first stage is a proxy measure of the
unobserved time-varying product characteristics that are correlated with prices. We include this
residual as a covariate in the estimation of logit models as a control function for the impact of
unobserved product characteristics on prices and demand (see Appendix E.1.2 for details).
The identification of the effect of the control function (the residual) relies on instrumental vari-
ables that are excluded from the demand model. We tested three types of instrument that have
been widely used in the Empirical Industrial Organisation literature. First, taxes represent a large
part of the final price in categories such as aperitifs and spirits. As the alcohol content of these
products varies greatly across subcategories and even within brands, we can leverage tax variations
across alternatives. In the spirits market, the tax level is only 0.08e/L for alcohol-free aniseed spir-
its, and raises up to 13.50e/L for some liquors. In the aperitifs market, the tax level varies from
0.04e/L for some wine-based aperitifs to 12.8e/L for some cocktails. Second, we also exploit
24

Berry-Levinsohn-Pakes (BLP) instruments such as the number ofothercompeting product varieties
within a given subcategory at each period. These competing varieties are likely to impact markups
and therefore prices, but should not have a direct impact on the household’s utility from a specific
alternative (Berry et al. 1995). We sometimes interact these variables with manufacturer fixed-
effects to form instruments that capture the manufacturer-specific market power. Finally, we can
approximate the variation incosts shiftersacross products by considering the mean price of same
brand or retailer product varieties in other periods (Hausman, Leonard and Zona 1994). Here, the
identifying assumption is that the month-variety-specific shocks on prices are uncorrelated across
periods. Hence, the mean retailer and brand prices observed in other periods captures variations in
costs that are orthogonal at period-variety-specific shocks.
We selected for each market (alcohol category) the instruments that are significant in the first
stage regression (F-test statistics to eliminate weak instruments). Appendix Table E.2 displays the
estimation results for the first-stage price equations.
4.1.3 Estimation results
The six demand models are estimated by simulated maximum likelihood (see details in E.1.3) on
the sample of households that have purchased alcohol in 2014 and were also observed in 2013 so
that we can compute an average number of standard drinks per adult household member in 2013
(sample S2, see Appendix Section A.1).
Table 3 presents the detailed results of the estimations of the six logit random coefficient mod-
els, where price endogeneity is controlled by the introduction of the estimated error terms of the
first-stage instrumental variable equations. The coefficient on this control variable is always posit-
ive, which means that unobserved time-varying product characteristics, such as marketing efforts,
simultaneously increase prices and consumer utility.
The price coefficients reflect the willingness-to-pay of households for the various alcohol cat-
egories. For instance, as compared to the other income categories, upper-income households (the
reference category) have a stronger preference for beers, sparkling wines, and still wines, but a
weaker preference for aperitifs and spirits. Older households express a stronger preference for
wines, aperitifs, and ciders than young households, who have a stronger preference for beers and
spirits. Heavy drinking households have a stronger preference for spirits and, to a lesser extent,
25

for still wines and aperitifs. The estimated standard deviation (σ a) of the distribution of the price
coefficient is nearly zero for ciders and still wines (and close to zero for sparkling wines), mean-
ing that age, income, and the overall preference for alcohol capture most of the household taste
heterogeneity in these alcohol categories.
In Appendix E.1.4, Table E.3, we report the average estimated own-price elasticities, by alco-
hol category and subcategory. They reflect the willingness to substitute to any alternative product
(including the outside option). While the average elasticities are the largest for beers (-5.02) and
still wines (-4.43), the standard deviation associated with the distribution of elasticities within these
categories is also greater (+1.6 for beers and +2.15 for still wines). This reflects the greater hetero-
geneity of these alcohol categories, in terms of brand and quality segmentation. For still wines, the
elasticities are larger in the lower-quality segments (‘de Table’ and ‘de Pays’), which implies that
competition is more intense between products within these categories.
Finally, Table 4 shows the average margins (in % of the consumer price) that were calculated
after calibrating the supply-side models. The higher the margin, the higher is the profit per unit.
As expected, margins are generally higher for private labels than for national labels. They are also
higher for lower quality wines than for higher quality ones (‘de Table’ vs. ‘d’Appellation’).
26

Table 3: Random coefficients logit models - Estimation results
Ciders Beers Aperitifs Spirits Still wines Sparkling wines
Price
Mean (αa) -1.700*** -1.991*** -0.643*** -0.408*** -1.572*** -0.381***
xD Income U pper−middle 0.025*** -0.021*** 0.016*** 0.041*** -0.065*** -0.012***
xD Income Lower−middle 0.013*** -0.105*** 0.022*** 0.020*** -0.183*** -0.016***
xD Income Lower -0.054*** -0.092*** 0.031*** 0.006*** -0.275*** -0.034**
xD Age [35;55] 0.454*** -0.165*** 0.028*** -0.006*** 0.052*** 0.083***
xD Age >55 0.539*** -0.374*** 0.056*** -0.037*** 0.133*** 0.054***
xD Habit ]0;1] -0.237*** -0.138*** 0.051*** 0.026*** 0.042*** -0.009***
xD Habit >2 -0.547*** -0.187*** 0.010*** 0.057*** 0.012*** -0.025***
xδ Champagne 0.188***
Standard Deviation (σa) 0.000 0.411*** 0.109*** 0.150*** 0.000 0.005***
Control function 1.153*** 1.562*** 0.369 *** 0.092 *** 1.499*** 0.153***
Fixed Effects
Retailer Yes Yes Yes Yes Yes Yes
Subcategory Yes No Yes Yes Yes Yes
Subcategory xD Income h - - - Yes Yes -
Subcategory xD Age h Yes - - - - Yes
Subcategory xD Habit h - - Yes - - -
Brand Yes Yes Yes Yes No Yes
Brand x Alcohol-free No Yes No No No No
Alcohol-free No No Yes Yes No No
Notes: N=266,460 household-purchase observations. ∗p<0.10, ∗∗ p<0.05, ∗∗∗ p<0.01.D Income . are dummies for
the household income categories (Upper, Upper-middle, Lower-middle, Lower) and Upper is the reference;D Age . are
dummies for the three age of the household head categories (18-35, 35-55, >55 years old) and 18-35 is the reference;
DHabit . are dummies for average household purchases observed in 2013 (≤1,[1;2],>2 standard drinks/adult/day) and
≤1 is the reference;δ Champagne is a dummy distinguishing champaigns from lower quality sparkling wines.
27

Table 4: Estimated own-price elasticities and calibrated margins
Ciders Beers Aperitifs Spirits Still wines Sparkling wines
Own-price elasticity -3.40 (0.84) -5.02 (1.60) -3.04 (1.20) -3.55 (0.20) -4.43 (2.15) -2.71 (1.09)
Margins 32.73 (6.73) 23.67 (18.23) 38.59 (19.54) 33.80 (13.13) 24.42 (7.76) 42.82 (18.34)
Sweet Alcohol-free Cocktails and Punch Rum de Table Champagne
National Brands 25.92 (0.00) 36.82 (6.82) 37.13 (12.18) 31.78 (3.05) 38.70 (5.03) 26.52 (5.10)
Private Labels 37.90 (3.88) 48.28 (5.30) 57.88 (18.64) 32.02 (0.82) 34.21 (1.59) 31.49 (1.83)
Raw Bock/premium Liquor wines Whisky de Pays Other sparkling wines
National Brands 28.30 (7.03) 23.07 (6.84) 22.23 (3.18) 30.18 (6.81) 25.51 (6.46) 76.16 (23.70)
Private Labels 36.09 (3.57) 36.22 (0.75) 24.60 (1.65) 29.76 (0.81) 26.98 (1.65) 68.27 (8.12)
Special Natural sweet wines Aniseed d’Appellation
National Brands 20.36 (3.69) 37.53 (5.66) 32.09 (0.62) 15.57 (2.51)
Private Labels 26.49 (0.00) 40.68 (2.69) 30.24 (0.80) 16.29 (1.59)
Amer, gentiane
and vermouth Liquors
National Brands 36.07 (15.37) 38.07 (7.93)
Private Labels 49.86 (4.13) 41.61 (1.66)
Other aperitifs Other spirits
National Brands 54.16 (10.40) 31.26 (2.17)
Private Labels 48.05 (6.66) 29.92 (0.78)
Notes: N=1,662 product varieties. In parenthesis, the standard deviation of the distribution of calibrated margins in the subcategory or category.
Margins are expressed as a percentage of the consumer price.
28

4.2 Demand for quantity
4.2.1 A pseudo-panel approach
We use a pseudo-panel approach to estimate the quantity demand model, which allows us to avoid
the issue of dealing with zero purchases in certain alcohol categories. The pseudo-panel is con-
structed by grouping households into clusters. We define 120 clusters by combining the following
variables: whether the household consists of single male or single female; couple without children;
or couple with at least one child under 16. , whether the head of the household is under 35, between
35 and 54, or over 54 years old. than 35, between 35 and 54, or more than 54 years old; whether the
household belongs to one of the following four Kantar income categories: rich, mid-rich, mid-poor
or poor; and whether the average number of standard drinks consumed per adult household mem-
ber per day in 2013 was lower than or equal to 1, between 1 and 2, or greater than 2. The latter
characteristic control for heterogeneity in household habits. The Rich and mid-rich, and poor and
mid-poor income categories are grouped when the size of the cluster is too small. Appendix E.2.3
provides details on the construction of the pseudo-panel.
Table 5 reports some descriptive statistics on budget shares, quality indices and quality-adjusted
and unadjusted prices and quantities in the estimation sample (grouping all periods of 2013 and
2014).
As a result of the demand for quality models, the quality indices are larger in categories that are
more differentiated in terms of classifications, such as aperitifs, spirits, and sparkling wines (with
the distinction between mousseux and champagnes), and for which there is a larger heterogeneity
in unobserved consumer taste measured by the standard deviation of the marginal utility of price
in Table 3. Larger quality indices tend to produce lower adjusted prices (third column) and higher
adjusted quantity indices (i.e. larger utility flows for consumers). This is especially true for spirits,
whose small consumption volume in L (0.58 on average vs. 1.14 for wines) is associated with a very
large utility flow (10.74 vs. 3.72 for wines). Adjusting the prices and physical quantities by quality
reveals, to some extent, the preferences of consumers between the various alcohol categories. The
low quality index for still wines specifically confirms that French households do not particularly
value product differentiation on the mass market of wines. This shows the disconnection between
the discourse of lobbyists, experts, and marketers of the French wine sector, which emphasizes its
29

Table 5: Prices, quantities and budget shares
Prices (e/L) Quantities (L/4-weeks) Quality Shares Obs.
Q>0 Unadjusted,PAdjusted,PUnadjusted,QAdjusted,Qb w
Ciders 2.87 (0.70) 0.86 (0.25) 0.21 (0.17) 0.71 (0.60) 2.37 (0.35) 0.03 (0.03) 1,853
Beers 2.57 (0.54) 0.86 (0.18) 2.52 (1.63) 7.57 (4.94) 1.99 (0.15) 0.24 (0.12) 2,330
Aperitifs 6.69 (1.68) 0.73 (0.18) 0.37 (0.24) 3.45 (2.30) 8.22 (0.36) 0.09 (0.05) 2,223
Spirits 19.89 (3.38) 1.18 (0.27) 0.58 (0.53) 10.74 (11.23) 16.16 (2.24) 0.36 (0.12) 2,242
Still wines 5.00 (1.75) 1.55 (0.54) 1.14 (1.19) 3.72 (3.92) 2.23 (0.08) 0.17 (0.09) 2,267
Sparkling wines 11.84 (6.48) 0.82 (0.44) 0.32 (0.30) 4.56 (4.16) 13.48 (1.04) 0.13 (0.10) 2,046
Notes: The first column report the number of cluster-period observations with positive aggregate purchase volumes.
Prices are expressed in Euro/Liter when unadjusted and in Euro/Utility unit when adjusted (cf equation 7), quantities in
Liter/4-weeks when unadjusted and Utility unit/4-weeks when adjusted (cf equation 6) . The quality index is defined in
equation C.3 and its construction is detailed in Appendix Section E.2.2 All observations are weighted by the weight of
the cluster in the total sample. Standard deviations in parenthesis show the variability across clusters and over time.
richness, excellence, and diversity, and the reality of the mass market. French often drink wine
without paying much attention to quality. The last column shows that, despite clustering, there is
still a significant number of zero expenditures for each category. Out of 3,120 observations, we have
only 1,624 observations for which expenditures on all 6 categories are strictly positive. Considering
that this results from finite sampling rather than from variations in cluster-specific taste, we keep all
observations for estimating the model.
4.2.2 Specification and estimation
The quantity demand functions are derived from a Quadratic Almost Ideal Demand System (QUAIDS:
Banks et al. 1997), whereby the budget sharew ac t for alcohol categoryaand clustercin periodt
is modeled as a function of log total expenditure lnY c t =ln  ∑A a=1Y ac t  =ln  ∑A a=1 Pac t Qac t  , the
vector of log prices, lnP c t = (lnP1c t , ...,lnPAc t )′, and cluster-averages of socio-demographic control
variables.25 Appendix E.2.1 provides more details about the specification.
The demand system in the Appendix Equation E.2.1 is estimated using an iterative reweighted
least-squares procedure to deal with non-linearities, imposing homogeneity and symmetry con-
straints (see Lecocq and Robin 2015). In the estimation, each cluster observation is weighted by
25Banks et al. (1997) show that the Engel curves for alcohol are non-linear, as opposed to other food items. This
justifies the use of a QUAIDS instead of the simpler AIDS originally proposed by Deaton and Muellbauer (1980).
30

the proportion of French households represented by the cluster. This therefore limits the influence
of less populated clusters on the estimates. Although we cluster observations and include addi-
tional observed characteristics, some residual cluster-level demand side variable may be correlated
with the total alcohol budgetY c t . We follow the usual practice of instrumenting the latter by log
household income (cluster average).
4.2.3 Identification
The price indices may be endogenous because they are constructed as the ratio of the average price
of product varieties weighted by the probability of purchase (average unit value for the category)
to the quality index. For identification purposes, we first assume that any shocks to consumer
preferences for a category of alcohol do not affect relative preferences for certain products over
others within that category. This assumption is realistic in so far as unobservable shocks to the
specific utility of a variety can be decomposed additively into an average shock specific to the
alcohol category and a deviation from this average shock specific to the product. The average
shocks to the alcohol category therefore have no effect on the relative preferences of consumers for
the different varieties within the category. They do not affect market shares or the quality index.
However, preference shocks specific to the category as a whole may be correlated with the
prices of the varieties. We include the average sociodemographic characteristics of the clusters
in the regressions to control for differences in time-invariant preferences that may simultaneously
affect households’ intra- and inter-category trade-offs. We also include period fixed-effects to take
into account increased demand from all households at certain times, such as the end of the year
holidays or the wine fairs period. The use of aggregate household data mitigates potential issues
with regional/local shocks on demand that could be correlated with prices. Finally, our identification
strategy assumes that the prices of the varieties of a category of alcohol are not affected by transitory
variations in the preferences of certain clusters of consumers for that category of alcohol. This
assumption excludes, for example, a transitory increased demand for sparkling wine from wealthy
households, which would drive up prices.
Nevertheless, as we cannot rule out the possibility that omitted demand-side factors be correlated
with prices, we propose various robustness checks and sensitivity analyses in the next section. We
first estimate the model with period effects interacted with income categories and with alcohol habit
31

categories. We also replace the quality-adjusted price indices by more exogenous Laspeyres price
indices.26
4.2.4 Estimation results
Table 6 reports the estimated elasticities averaged over all cluster-period observations with cluster
weights in the population. The first line shows that all categories except ciders have very significant
income elasticities. These are clearly lower than one for ciders and still and sparkling wines, which
means that an increase 1% in the total alcohol budget increases expenditures in these categories
less than proportionately. Expenditures on beers and spirits are more elastic to alcohol expenditure
(+1.2% and +1.4%). Higher prices are also associated with a higher budget (E PY). The price effect
is not significant for ciders. We also find that an increase in household income increases total alcohol
expenditures, with an elasticity of +0.05% (not reported here).
The compensated cross-price elasticities reported off-diagonal in the middle panel of the Table
measure consumer preferences in terms of willingness to substitute one alcohol category for another.
Consumers show a strong preference for sparkling wines, whose cross-price elasticities are never
significant. They have milder preferences for cider and beers. We find nine cross-price effects
significant at the level of 5%, eight of which are symmetrical: beers and spirits are substitutes —
consumers are willing to substitute beers for spirits when the price of beers increases, and vice versa
– as well as beers and still wines, aperitifs and spirits, spirits and still wines. Households are willing
to substitute ciders for beers if the price of the latter increases, but this is not reciprocal. The absence
of negative compensated cross-price elasticities validates our definition of the outside option as "all
products in other alcohol categories" in our modeling of demand for quality.
The uncompensated own-price elasticities are reported in the diagonal of the lower panel of
Table 6. They are important for understanding the potential impacts of price policies, as they sum-
marize both consumer preferences for substitutions and the income effect of price variations. The
own-price elasticities are lower than one for all categories, larger for spirits and beers (-0.8) and
26These Laspeyres price indices are constructed for each categoryaand each household clustercasP ac L,t = ∑ j∈Jat Sc j p jt, whereS c j is the cluster-average share of productjin purchases. We also tried an instrumental variable strategy by
instrumenting our quality-adjusted price indices with these Laspeyres indices (a form of shift-share instrumentation).
This approach did not pass a weak instrument test, likely because the sources of price variations (e.g. cost shocks) are
correlated across alcohol categories.
32

very low for sparkling wines (-0.2). For spirits and beers, a large part of the large own-price ef-
fect is explained by the large budget elasticity of these categories. As shown in the middle panel,
when compensated for the income loss produced by the price increase, the own-price elasticity for
spirits falls to -0.4%, a compensated own-price elasticity that is similar to what is observed for the
other categories. All 14 significant uncompensated cross-price elasticities are negative. Hence, even
though they are Hicksian substitutes, they are gross complements due to income effects. As expec-
ted, the latter are rather large for sparkling wines, with significant cross-price elasticities (except
with still wines) that are on par with its own-price elasticity. It is noteworthy that an increase in
the prices of still and sparkling wines is likely to generate non-negligible reports on spirits, with
cross-price elasticities close to+0.2. We will see in the next section that these price effects are
going to be an important factor driving our results.
Table G.1 in Appendix Section G.1 compares these results with alternative estimates from a
specification with income-period and alcohol habit-period fixed-effects to control for variations in
prices that may be related to shocks specific to certain consumer segments, depending on their
income and their habitual consumption level. The results are unchanged with own-price uncom-
pensated elasticities that barely vary. We also replace the quality-adjusted price indices by Laspeyres
price indices because residual price endogeneity might still be a concern. We then find significantly
higher own-price elasticities for wines:−0.7 instead of−0.4 for still wines, and−0.7 instead of
−0.2 for sparkling wines. Given this slight discrepancy, we will also test the sensitivity of our
simulation results to the replacement of quality-adjusted prices by Laspeyres indices.
33

Table 6: Average income, budget and price elasticities
Ciders Beers Aperitifs Spirits Still wines Sparkling wines
Income elasticity 0.503 (0.302)* 1.210 (0.112)*** 1.017 (0.154)*** 1.434 (0.083)*** 0.349 (0.126)*** 0.385 (0.187)**
Budget price elasticity 0.007 (0.022) 0.098 (0.031)*** 0.070 (0.021)*** 0.071 (0.027)*** 0.059 (0.020)*** 0.122 (0.011)***
Compensated price elasticities
Ciders -0.491 (0.084)*** 0.217 (0.110)** 0.044 (0.083) 0.183 (0.104)* 0.109 (0.083) -0.063 (0.043)
Beers 0.024 (0.031) -0.542 (0.041)*** 0.039 (0.031) 0.349 (0.039)*** 0.084 (0.031)*** 0.045 (0.017)
Aperitifs 0.012 (0.043) 0.100 (0.055)* -0.438 (0.042)*** 0.242 (0.054)*** 0.077 (0.042)* 0.008 (0.023)
Spirits 0.014 (0.023) 0.237 (0.030)*** 0.063 (0.023)*** -0.381 (0.030)*** 0.066 (0.023)*** 0.000 (0.010)
Still wines 0.017 (0.037) 0.117 (0.049)** 0.041 (0.037) 0.136 (0.047)*** -0.337 (0.037)*** 0.026 (0.019)
Sparkling wines -0.013 (0.058) 0.084 (0.076) 0.005 (0.057) 0.001 (0.071) 0.034 (0.057) -0.112 (0.032)***
Uncompensated price elasticities
Ciders -0.504 (0.085)*** 0.098 (0.133) -0.002 (0.093) 0.008 (0.114) 0.024 (0.106) -0.127 (0.058)**
Beers -0.008 (0.032) -0.828 (0.047)*** -0.072 (0.034)** -0.072 (0.043)* -0.121 (0.040)*** -0.109 (0.022)***
Aperitifs -0.014 (0.043) -0.140 (0.068)** -0.531 (0.045)*** -0.112 (0.058)* -0.096 (0.054)* -0.122 (0.030)***
Spirits -0.024 (0.024) -0.102 (0.038)*** -0.068 (0.025)*** -0.881 (0.030)*** -0.178 (0.030)*** -0.183 (0.015)***
Still wines 0.008 (0.038) 0.035 (0.058) 0.009 (0.040) 0.014 (0.049) -0.396 (0.046)*** -0.019 (0.025)
Sparkling wines -0.023 (0.059) -0.007 (0.089) -0.030 (0.062) -0.133 (0.078)* -0.031 (0.072) -0.161 (0.033)***
Notes: average elasticities where each cluster observation is weighted by the proportion of French households represented by the cluster. Standard errors in parentheses. ***,** and * Significant at the 1%, 5%
and 10% level. The first line display Income elasticities, i.e. the % change in expenditures on a given alcohol category when total alcohol expenditures increase by 1%. The second line displays the % change
in total alcohol expenditures when the price of a given alcohol category (columns) increase by 1%.
34

5 Minimum Unit Pricing vs. Volumetric Taxation: main results
We now present the main results from our counterfactual simulations. The simulation of the im-
pact of a counterfactual price policy on the alcohol markets (household purchases and equilibrium
prices) proceeds in two steps. First, for each market/alcohol category, we use the demand and sup-
ply functions to simulate the market equilibrium that would result from the implementation of the
policy. Second, we use the new equilibrium prices to construct new price indices, and variations
in quantities are predicted using the estimated demand functions for quantities. We provide further
details in Appendix Section F.
We first compare the aggregate impact of the six counterfactual price policy scenarios on house-
hold purchases of pure alcohol. We then detail the market mechanisms explaining these results:
quality, quantity and competition effects.
5.1 Minimum Unit Price has the largest impacts on household purchases
Table 7 presents the simulation results for the impact of the six policies on average household
purchase volumes converted to pure alcohol (upper panel). 27 We report the average impacts, with
95% confidence intervals that have been computed by Monte-Carlo simulations of the model (1000
replications). We obtain four important results.
Firstly, a tax reform calibrated for the objective of fiscal neutrality (low tax rate) unexpectedly
leads to an increase in the purchase and consumption of pure alcohol. This increase is observed
for both a uniform and a progressive tax. It reaches +14.0% (CI95%[11.6%;18.7%]) in the Low
uniform tax scenario when the price reactions of manufacturers and retailers are taken into account.
Secondly, tax reforms calibrated to achieve public finance neutrality result in a significant reduc-
tion in consumption, up to -10.3% in the High progressive tax scenario (CI95%[-12.7%;-7.8%]).
Third, the Minimum Unit Price would yield the greatest benefits for public health, with house-
hold purchase decreasing by -15.0% (CI95%: [-16.4% ;-13.5%]). The aggregate impacts are virtu-
ally the same whether or not a tax reform is implemented at the same time (Minimum Unit Price +
Low progressive tax). It is important to note that the MUP scenario dominates the High progressive
27The estimates are not very different when we adjust for the number of adult household members, or when we
individualize household consumptions.
35

tax scenario, with non-overlapping confidence intervals when we account for supply-side reactions
(Columns 3 and 4).
Fourth, price reactions from producers and retailers have impacts that are substantial in the Low
uniform and Low progressive tax scenarios. Supply-side reactions are predicted to amplify expected
consumption increases (first and third lines). In contrast, supply-side reactions amplify the expected
benefits of minimum price policies, with, for example, an additional drop of -1.3 percentage points
in the MUP scenario (-13.7% without price reaction vs. -15% with price reaction).
In the lower panel of Table 7, we report the impacts on purchase volumes in L, i.e., not ac-
counting for the variability in alcohol content across products. The MUP and high-tax scenarios
negatively impact both purchase volumes and volumes of pure alcohol. Interestingly, the Low uni-
form and Low progressive tax scenarios have almost no impact on purchase volumes expressed in L.
Hence, their positive impacts on purchases of pure alcohol (once we account for the ethanol content
of products) essentially reflect substitutions between products, with households choosing varieties
with higher alcohol content. This result emphasizes the interest in modeling household purchase
behavior along both the quantity and the quality dimension.
As announced in the previous section, to alleviate concerns about the potential endogeneity of
the quality-adjusted price indices, we also produce simulation results with quantity elasticities ob-
tained from the estimation of a QUAIDS where prices are measured by Laspeyres indices. Appendix
Table G.2 shows that this tends to shift downwards all effects without affecting much the ranking
of scenario. The impacts of Low uniform and progressive taxes on household purchases expressed
in pure alcohol are still positive, but closer to zero. The Minimum Unit Price decreases household
purchases by -23.1% vs. -18.8% for the High progressive tax, and -26.1% for a MUP associated
with a Low progressive tax. These simulated impacts are larger than those we obtain with quality-
adjusted prices. This is essentially due to larger price elasticities, as reported in Table G.1. Since
the estimates obtained with quality-adjusted prices are finally more conservative, we focus on these
in the rest of this article.
36

Table 7: Impacts on household purchases of pure alcohol
Without supply-side reactions With supply-side reactions
ScenarioAvg. impact CI95% Avg. impact CI95%
Volumes of pure alcohol (Std. Drinks/hhold)
Low uniform tax +10.1% [+7.2,+13.1] +14.1% [+10.6,+17.7]
High uniform tax -8.2% [-11.8,-4.7] -5.9% [-9.6,-2.2]
Low progressive tax +4.2% [+2.2,+6.2] +6.8% [+4.5,+9.1]
High progressive tax -10.3% [-12.9,-7.8] -10.3% [-12.8,-7.8]
Minimum Unit Price -13.7% [-14.7,-12.6] -15.0% [-16.4,-13.5]
MUP + Low prog. tax -12.4% [-13.7,-11.1] -14.7% [-16.8,-12.5]
Purchase volumes (L/hhold)
Low uniform tax +0.3% [-2.7,+3.3] +1.7% [-2.0,+5.4]
High uniform tax -10.3% [-14.2,-6.5] -9.3% [-13.2,-5.3]
Low progressive tax +0.2% [-1.8,+2.2] +1.3% [-0.9,+3.5]
High progressive tax -7.2% [-9.9,-4.6] -6.8% [-9.4,-4.3]
Minimum Unit Price -12.7% [-13.7,-11.6] -13.5% [-15.0,-11.9]
MUP + Low prog. tax -12.2% [-13.5,-10.8] -13.9% [-16.1,-11.6]
Notes: Mean simulated relative impacts on household purchase volumes, in standard drinks (upper panel) and purchase
volumes (lower panel); 95% Confidence Intervals in brackets.
37

5.2 Understanding the mechanisms: quantity, quality and competition
The estimated average impacts result from the combination of quantity, quality, and competition
effects. In each of the six markets, price variations induce changes in choices of product variety,
generating variations in the average alcohol content of a purchase. Beyond this quality effect within
each market, price variations can produce changes in the total quantities purchased on each market,
as households make substitutions between alcohol categories. The upper panel of Table 8 shows the
effect of the different policies on purchase volumes (in L/household/year), after taking into account
the supply-side reactions. 28 Examination of the results by alcohol category reveals fairly uneven
variations between scenarios, particularly for spirits, where consumption increases sharply in the
first three scenarios. In contrast, the consumption of still wines decreases systematically and very
sharply in the Minimum Unit Price scenario (-23%, CI95%:[-25.2,-20.6]).
The differences between scenarios can be explained by changes in the market size of the overall
alcohol market and by substitutions between alcohol categories, and thus transfers from one market
to another. The current tax system is highly favorable to wines (see Table 2). Any reform based
on the alcohol content of products will therefore tend to reduce the price competitiveness of wines
as compared to the other alcohol categories, especially spirits. The middle panel of Table 8 shows
the variations in the average unit prices of purchases in the different alcohol categories after price
adjustments by manufacturers and retailers. 29 The difference induced by supply-side reactions is
reported in parentheses (in percentage points). We observe sharp increases in the unit price of still
wines in the two Minimum Unit Price scenarios (+48.8% and +62.6%), which is explained by very
low initial prices in view of their alcohol content. The unit value of spirits decreases significantly in
three of the four tax reform scenarios, with price reductions of up to -56.3% in the Low uniform tax
scenario. A progressive tax hardly limits the differential variation in unit prices between still wines
and spirits, even though the marginal tax increases with the alcohol content of the product. The
variations in unit prices for ciders, beers, and aperitifs are smaller than those for wines and spirits.
28For the sake of readability, we report the average simulated impacts without their confidence intervals in the table.
29The average unit prices at baseline and in the counterfactual scenario are computed using the product-level unit
prices weighted by the predicted choice probabilities. This contrasts to the lower panel of Table 2, where we reported
expected variations in observed unit values (total expenditures divided by fixed total quantities) without supply side
reactions.
38

Table 8: Household purchases: quantity effects
Ciders Beers Aperitifs Spirits Still wine Sparkling wines
Initial volumes (L/year) 1.7 23.9 4.0 6.2 37.6 3.8
Simulated % change in average household purchase volumes (L)
Low uniform tax -6.8 -1.6 +4.9 +63.6 -10.7 +0.0
High uniform tax -7.0 -11.0 -4.1 +22.3 -17.7 -7.1
Low progressive tax -4.4 +5.3 +6.4 +30.6 -9.2 -1.5
Low progressive tax -3.1 +0.4 +0.1 -8.0 -14.0 -8.5
Minimum Unit Price +2.7 -9.5 -8.2 -7.3 -23.0 -3.6
MUP + Low prog. tax -0.2 -9.0 -5.8 -0.8 -25.9 -5.0
Simulated % pts change in average unit prices (e/L) of alcohol categories
In parenthesis: % pts change produced by supply-side reactions
Low uniform tax +11.4 (+0.4) +0.1 (+0.4) -6.8 (-0.2) -56.3 (-9.1) +24.8 (-1.1) +13.5 (+0.3)
High uniform tax +21.9 (+0.4) +12.9 (+0.3) +7.5 (-0.2) -28.3 (-6.4) +51 (-2.2) +28.1 (+0.1)
Low progressive tax +5.5 (+0.1) -8.6 (-0.2) -9.2 (-0.6) -33.2 (-6.8) +21.3 (-1.6) +11.6 (+0.1)
High progressive tax +10.4 (+0.2) -1.8 (-0.1) +0.6 (-0.4) +5.1 (+1.0) +40.8 (-2.0) +22.4 (+0.2)
Minimum Unit Price +0.2 (0.0) +11.5 (-1.4) +11.2 (-0.3) +6.9 (-0.6) +48.8 (+11.5) +6.3 (+0.0)
MUP + Low prog. tax +5.5 (+0.1) +9.1 (+1.8) +6.3 (-0.4) -2.8 (-1.8) +62.6 (+18.3) +13.9 (+0.0)
Simulated shares of alcohol categories (%) in total household purchase volumes (L)
Initial shares 2.2 31.0 5.2 8.0 48.6 4.9
Low uniform tax 2.1 31.0 5.5 13.4 44.2 5.0
High uniform tax 2.3 31.3 5.6 11.1 45.5 5.1
Low progressive tax 2.1 33.0 5.6 10.6 44.7 4.9
High progressive tax 2.3 33.9 5.7 8.1 45.7 4.9
Minimum Unit Price 2.6 32.7 5.6 8.7 43.7 5.5
MUP + Low prog. tax 2.6 32.7 5.7 9.2 41.9 5.4
Notes:All estimates are based on model simulations and average across households weighted by their sample weights. Simulated changes in average
household alcohol purchases in each category/market (in L/household/year). Simulated variations in household average unit prices, where the latter is
calculated using the unit prices and the predicted household-level choice probabilities in the observed or counterfactual situations. Simulated shares
of alcohol categories in total household purchase volumes (in % of volumes in L) are average across households (weighted by their sample weights) of
the ratio of predicted purchase volumes in each category on total household alcohol purchases. The % pts change produced by supply-side reactions
are calculated as the difference between the % pts change in average unit prices with and without supply-side reactions.
39

The supply-side reactions amplify in some cases the immediate impact of policies on prices,
as shown by the difference with the price variation without supply-side reactions (reported in par-
entheses). This is especially the case for spirits in the first three scenarios. In the Low uniform
tax scenario, the average unit value is 9.1 percentage points lower than expected in the absence of
supply-side reactions. This is caused by heightened competition in the low-price product range,
resulting in further price decreases and, therefore, lower unit prices than expected. For wines, the
average unit price under the Minimum Unit Price scenario is 11.5 percentage points higher than
without supply-side reactions.
The introduction of a minimum price leads, in fact, to very substantial price increases for low-
quality wines, decreasing their competitiveness. The results by wine quality segment reported in
Appendix Table G.3 reveal that, before price adjustment, the average unit price of still wines initially
sold at lower than 3e/L increases by 107.8%, vs. +19.1% for the wines initially priced between
3e/L and 5e/L, and +0.8% for wines priced at 5e/L s or more. After supply-side price adjustments,
the increases are, respectively, +108. 0%, +20. 3%, and +3. 3%. Hence, strategic price adjustments
at the product segment level are little significant on average, even though, as expected, the higher-
quality products that face the largest demand increase slightly more their prices. Higher-quality
and highly demanded wines adjust only slightly their prices upward (and therefore their margins).
They essentially exploit the benefits of enhanced price competitiveness (the price difference with
low-quality wines still diminishes) to increase their market share.
These price variations, calculated separately for each market, have direct effects on the size of
each market, as well as indirect effects of substitution between markets. The lower panel of Table
8 illustrates these substitutions, comparing the initial market shares in the overall purchase volumes
with the market shares simulated in the different scenarios. In line with the simulated price changes,
the market share of still wines falls, while that of spirits rises (except in the High progressive tax
scenario). For other categories, there are few variations. This is particularly the case for sparkling
wines, for which our estimates show a fairly low direct price elasticity and a rather high budget
elasticity (see Table 6).
Although quantity effects (direct price effects and substitutions between alcohol categories) ex-
plain an essential part of the aggregate results presented in Table 7, substitutions between product
40

varieties within alcohol categories can also attenuate or amplify the effect of public policies. The
upper panel of Table 9 shows that these substitutions are observed for categories that are more
heterogeneous in terms of alcohol content: ciders, beers, aperitifs, and spirits. Substitutions vary
widely from one scenario to another and specifically show the importance of the tax design. For
instance, considering beers, we might think that a progressive tax would reduce more largely the
average alcohol content of purchases than a uniform tax, since it would bear proportionally more on
strong beers. In contrast, the decrease is greater in the High uniform tax scenario (-11.0%) than in
the High progressive tax scenario (-2.2%). This is explained by the tax design. In the High uniform
tax scenario, the prices of all beers increase, whereas in the High progressive tax scenario their
prices slightly decrease with only a small relative advantage for lighter beers.
Finally, the combination of substitution effects and competition effects explains the changes
observed in the contribution of each alcohol category to total household purchase volumes (in g
of ethanol), displayed in the lower panel of Table 9. Unsurprisingly, the share of spirits increases
sharply in the first three scenarios due to cumulative quantity and quality effects. Households would
purchase larger volumes of stronger varieties of spirits. In the last three scenarios, the most inter-
esting from a public health point of view, there are limited substitution effects from still wines to
spirits and, to a lesser extent, to beers, aperitifs and sparkling wines. The large decrease in house-
hold purchases of pure alcohol is then not explained by substantial substitutions between alcohol
categories, but rather by a drop in total purchase volumes (Table 7), and a fall in the average alcohol
content of varieties for spirits, aperitifs, and beers. In the Minimum Unit Price scenario, the average
alcohol content drops by 3.0% for beers, 1.7% for aperitifs, and 3.5% for spirits.
6 Heterogeneity of policy impacts
6.1 Heterogeneity across household category
The effects of policy reforms can differ in terms of distributional incidence and effectiveness in
targeting high-risk households. Table 10 thus presents the simulation results for different household
categories: low vs. high income households on the one hand; households with low vs. high risk on
41

Table 9: Household purchases: quality effects
Ciders Beers Aperitifs Spirits Still wine Sparkling wines
Initial average content (g/L) 3,6 5,2 13,0 37,5 12,0 11,7
Simulated % change in average alcohol content
Low uniform tax -4.5 +0.1 +3.9 +8.9 +0.0 -0.2
High uniform tax -9.0 -11.0 -5.1 +5.7 +0.0 -0.6
Low progressive tax -2.2 +2.8 +1.4 +4.6 +0.0 -0.2
High progressive tax -4.1 -2.2 -7.4 -5.0 +0.0 -0.4
Minimum Unit Price -0.1 -3.0 -1.7 -3.5 +0.2 -0.1
Minimum Unit Price + Low prog. tax -2.2 -0.7 -1.2 -5.5 +0.1 -0.2
Simulated share (in %) of alcohol categories in household purchases (g of ethanol)
Initial shares 0.7 12.8 5.6 26.2 49.8 4.9
Low uniform tax 0.5 11.1 5.3 41.0 38.9 4.3
High uniform tax 0.6 10.8 5.4 36.0 43.5 4.8
Low progressive tax 0.6 13.0 5.6 33.6 42.3 4.5
High progressive tax 0.7 14.0 5.8 25.6 47.7 5.0
Minimum Unit Price 0.8 13.2 5.9 27.6 45.2 5.6
Minimum Unit Price + Low prog 0.8 13.6 6.1 28.8 43.3 5.5
Notes: All estimates are based on model simulations and average across households weighted by their sample weights. Simulated changes in average
alcohol content are averages across households (weighted by their sample weights) of changes in the sum of product alcohol contents weighted by
predicted household-level choice probabilities. Simulated shares of alcohol categories in total household purchase volumes (in % of volumes in L)
are averages across households (weighted by their sample weights) of the ratio of predicted purchase volumes of ethanol in each category on total
household ethanol purchases. All formula for household-level predicted changes are derived in Appendix Section F
42

the other.30 These two dimensions, standard of living and risk level, overlap to some extent, since
lower-income households consume more alcohol on average.
The upper panel of Table 10 shows that the impacts on household purchases (in ethanol volumes)
do not differ between income categories, except for the Low uniform and Low progressive tax scen-
arios (but the 95% confidence intervals overlap).31 Interestingly, the High progressive tax scenario,
the Minimum Unit Price and the combined MUP and low progressive tax scenarios yield larger be-
nefits for high-risk households. For instance, Minimum Unit Price achieves a reduction of -14.3%
(CI95%[-15.7,-12.8]) for the low-risk households as against -17.2% (CI95%[-18.8,-15.6]) for the
high-risk ones. Thus, minimum price policies benefit high-risk households slightly more (+17%
with respect to low-risk households). They would see their consumption fall more sharply in abso-
lute terms, with associated health benefits also greater under the hypothesis of a positive dose-effect
relationship. Therefore, the minimum price policy would be the option that best responds to con-
cerns about reducing health inequalities.
The regressive effects of the different scenarios can be measured by the variations in consumer
welfare generated in the short term by price movements and the resulting variations in purchasing
power. We are not interested here in the variation in household spending on alcohol, but in the
variation in utility resulting both from the implementation of a public policy and from the reaction
of households to price changes. This variation in utility can be measured directly, as our structural
model enables an exact measurement of utility. It can also be converted into money metrics by com-
puting an equivalent variation representing the income variation that would ex-ante be equivalent to
the variation in consumer welfare generated by the counterfactual policy scenario. The equivalent
variation integrates together the expected variation in indirect utility and the negative income effects
caused by higher prices (see Appendix E.3).32
The middle panel of Table 10 reports the impacts on the overall utility households derive from
30Kantar WorldPanel classifies households in four income categories, from high to low, using self-reported household
monthly income adjusted for the number of consumption units (OECD equivalence scale). High-risk households are
defined as those with habitual consumption greater than 2 standard drinks/household adult member/day in 2013. Mod-
erate risk households have habitual consumption levels lower than one standard drink/household member//day in 2013.
This classification masks a very significant gap in risk exposure between these two categories: pure alcohol purchases
are on average 6.7 times higher for high-risk households compared to low-risk households.
31+12.5%, CI95%[9.1,16.1] for the high-income vs. +16.5%, CI95%[13.2,20.0] for the low-income.
32Since we are primarily conducting an ex ante evaluation exercise and we are interested in the ex-ante political
acceptability of the reform, we focus on the equivalent variation rather than on the compensating variation.
43

alcohol consumption, while the lower panel of Table 10 shows the expected welfare losses ine.
Interestingly, the relative utility loss from Minimum Unit Price policies is on average larger for
high-income and low-risk households (around -5.0% for both groups). High-risk households would
need to increase their total expenditures by 76.8e/ year on average to maintain their consumption
level and therefore their utility. This explains why their utility loss is lower than that of low-risk
households (-1.7% vs -5.0%). But this expenditure increase corresponds to an opportunity cost that
is measured (ex-ante) by the equivalent variation. The Minimum Unit Price scenario would indeed
generate a welfare loss equivalent to around 88.9 C/year for high-risk households (CI 95% [-90.2,-
87.0]), as opposed to 115 C/year in the High progressive tax scenario (CI95%[-117.6,-113.3]). In
the three scenarios that are the most attractive from a public health perspective, losses would be
rather limited for most households, except those with high consumption. Yet, these variations in
consumer welfare do not take into account the beneficial effects on physical and mental health of a
reduction in consumption, in the medium or long term.
44

Table 10: Household heterogeneity
Income category Risk category
Low High Low High
Baseline
Purchase volumes (drinks/household/week) 14.9 13.4 6.3 42.5
Average expenditure (e/year) 400.0 354.2 178.3 1081.4
Impact on household purchases of pure alcohol (%)
Low uniform tax +16.5 +12.5 +12.8 +17.8
High uniform tax -5.0 -6.7 -6.5 -4.2
Low progressive tax +8.1 +5.7 +6.8 +6.8
High progressive tax -9.9 -10.6 -9.8 -12.0
Minimum Unit Price -15.1 -14.8 -14.3 -17.2
Minimum Unit Price + Low prog. tax -14.3 -15.0 -13.8 -17.6
Impact on utility derived from alcohol (%)
Low uniform tax +7.0 +5.7 +1.5 +20.5
High uniform tax -4.5 -4.9 -8.0 5.0
Low progressive tax +3.7 +2.8 +1.0 +9.9
High progressive tax -5.9 -6.7 -7.6 -2.3
Minimum Unit Price -3.6 -4.9 -5.0 -1.7
Minimum Unit Price + Low prog. tax -3.8 -6.1 -6.2 -0.6
Equivalent variation in consumer welfare (C/household/year)
Low uniform tax +89.0 +70.9 +37.2 +248.4
High uniform tax -11.7 -19.0 -7.2 -37.3
Low progressive tax +40.4 +30.4 +19.7 +97.7
High progressive tax -35.0 -42.9 -18.7 -115.4
Minimum Unit Price -25.6 -37.3 -15.6 -88.9
Minimum Unit Price + Low prog. tax -22.7 -39.0 -14.5 -90.9
Notes: Low-risk households: average purchases <1 standard drink/household adult member/day in 2013; High-risk
households: average purchases≥2 standard drinks/household adult member/day in 2013.
45

6.2 Industry profits: losers and winners.
The different scenarios have heterogeneous consequences for sectors and firms (producers and re-
tailers), depending on their impact on total market size, substitutions between markets, and within
markets. Our supply-side models enable us to specify the effects on unit profits in the industry.
Although the supply-side model cannot give us insights into profit-sharing between producers and
retailers, we constructed our dataset so as to make a distinction between national brands produced
by small manufacturers on the one hand (small firms), and national brands produced by large man-
ufacturers or private label brands produced by retailers on the other hand (large firms).
Table 11 details the variations in industry profits by market/alcohol category for all scenarios,
and by market and firm size for the three scenarios that yield the largest health benefits. Two results
stand out. Firstly, as shown in the upper panel of the table,with the exception of the Minimum Unit
Price scenario, the profit of the still wine sector falls, with a drop reaching -34.6% in the Minimum
Unit Price scenario with Low progressive tax (CI95%[-37.9,-31.3] (last line of the upper panel).
This drop is due to the implementation of the progressive tax, as the implementation of the Minimum
Unit Price alone leaves profits virtually unchanged (+2.3%, CI95%[-0.8,+5.5]). Secondly, in the
Minimum Unit Price scenario, profits increase slightly in all markets, and for the entire alcohol
sector as a whole (+3.7%, CI95%[+1.9,+5.5]). At the market level, the increase is significant at the
95% confidence level for spirits only (+6.9%, CI95%[+4.2,+9.7]).
Variations in total profit can be further decomposed into a quantity effect that reflects the size
of the market, a quality effect that reflects changes in variety market shares, and a price effect that
reflects changes in product-specific margins. When we conduct this decomposition exercise for the
Minimum Unit Price scenario (Appendix Table G.4), we find significant quantity effects that are
negative for all markets, which is expected since prices increase. The quantity effect is the largest
for still wines, representing -30.4% of initial profits vs -8.5% for spirits. The quality effects are all
negative, except for sparkling wines, and especially large for still wines (-139.7% of initial profits).
This reflects the large substitutions from low-quality wines to higher-quality ones. Finally, the price
effect is positive because unit prices mechanically increase while marginal costs remain constant:
margins are higher, which offsets the profit loss induced by the contraction of the market. The price
component of the change in profit is very large for still wines, representing +172.5% of the initial
46

Table 11: Variations in profits
Ciders Beers Aperitifs Spirits Still Wines Sparkling Wines
Variation in profit by market (%)
Low uniform tax -6.1 -1.3 +5.7 +22.7 -16.5 +2.4
High uniform tax -5.9 -10.6 -2.7 +1.9 -24.9 -1.3
Low progressive tax O1 -4.1 +5.7 +6.8 +6.5 -14.7 +0.4
High progressive tax O2 -2.7 +0.5 +0.9 -3.1 -21.3 -3.7
Minimum Unit Price +3.4 +1.1 +3.4 +6.9 +2.3 +1.8
Minimum Unit Price + Low prog. tax +0.2 +10.7 +8.6 +45.5 -34.6 -1.3
Variation in profits by market and company size (%)
High progressive tax
Small firms -6.3 -4.8 -8.3 +7.9 -20.7 -1.1
Large firms -2.4 +0.6 +3.6 -4.1 -22.0 -5.1
Minimum Unit Price
Small firms +3.4 +7.6 +6.7 +5.8 +39.3 +2.7
Large firms +3.4 +1.0 +2.5 +7.0 -38.7 +1.3
Minimum Unit Price + Low prog
Small firms -1.8 +24.7 -7.8 +50.8 -21.5 +0.3
Large firms +0.4 +10.3 +13.4 +45.1 -49.1 -2.1
Notes: Mean simulated impacts on household purchases by alcohol category (L/year).
profits. Hence, this large price effect offsets the quantity and quality effects, which explain why the
Minimum Unit Price has no impact on the overall profit of the wine sector. The same mechanism
is at play in the other markets, although the magnitude of the transfer from small to large firms is
smaller. The MUP increases the profits of small and medium wine firms (+39%) while decreasing
the profits of large manufacturers and retailers (- 39%). These results support the MUP as a targeted
strategy to curb harmful consumption while benefiting small and medium wine producers.
Finally, Appendix Table G.4 also shows that the MUP maintains stable tax revenues. V AT reven-
ues increase with prices (+7%). This offsets the loss of fiscal revenues produced by the contraction
of the market (-10.3%) and, finally, tax revenues are estimated to drop by 2.3% only.
47

7 Conclusion
Our results clearly outline the superiority of a Minimum Unit Price policy over the alternative tax re-
forms, especially in the French context where the wine sector has always opposed any reform driven
by public health motives. The introduction of a minimum price leads to very substantial price in-
creases for low-quality wines, produced mainly by large manufacturers and retailers. In competition
with higher-quality wines, their market shares would fall. The size of the market shrinks as a con-
sequence of an income effect. These results can be explained by the increase in selling prices at
constant production cost: the implementation of a minimum price increases producers’ unit mar-
gins. This largely compensates for the drop in purchase volumes. In a sense, the minimum unit price
leads to a transfer of surplus from consumers to producers, with the former subsidizing the latter.
The introduction of a minimum price has the advantage of affecting only the largest operators in
this sector, while the profits of other operators would increase sharply despite the drop in quantities
purchased on this market. On the other hand, all operators would again be affected if a progress-
ive tax were added to the minimum price, replacing existing duties: the extra margin mechanically
generated by the introduction of the minimum price would then be taken up by taxation. The MUP
entails only a small loss for public finances. It will be largely offset by the expected decrease in
health care costs, especially since minimum pricing has higher impacts on high-risk households.
These conclusions contrast somewhat with previous empirical evidence that supported the advant-
age of progressive volumetric taxation over minimum pricing (Griffith et al. 2022). Importantly,
these evidence were based on analyses of the UK market and did not really focus on the heterogen-
eity between supply-side operators. That our estimates lead to different conclusions demonstrate
the importance of accounting for country-specific consumption patterns, market organization, and
public regulations when analyzing and designing price regulation policies.
Like all modeling exercises, our study has some limits. In particular, we were not able to model
on-trade consumption in restaurants, bars, night clubs, or consumption away from home (by friends,
etc.). Yet, on-trade consumption is generally more expensive than off-trade consumption, and the
policy reform would apply to all consumption occasions. This limits concerns regarding substitu-
tions from off-trade to on-trade. We also ignore the production capacity constraints. These will
certainly have important consequences for our predictions regarding the wine sector. In the MUP
48

scenario, smaller wine producers will not be able to meet in the short term an increase in demand
volumes. As a consequence, they may increase their prices above the predicted price changes of
our model. This will even more reduce overall purchases. In the long term, the structure of the
market could be affected by shifting to producing higher quality and fewer quantities. Despite these
limits, our modeling framework is well suited to the ex ante evaluation of behavioral price policies
that are likely to affect consumption through three first-order mechanisms: adjustments in consumer
quantity and quality, and strategic price adjustments by firms and retailers.
References
Allais, Olivier, Fabrice Etilé and Sébastien Lecocq (2015). ‘Mandatory labels, taxes and market
forces: An empirical evaluation of fat policies’. In:Journal of Health Economics43, pp. 27–44.
DOI:10.1016/j.jhealeco.2015.06.003.
Ally, Abdallah K. et al. (2014). ‘Alcohol tax pass-through across the product and price range: do
retailers treat cheap alcohol differently?’ In:Addiction109.12, pp. 1994–2002.DOI:10.1111/
add.12590.
Anderson, Peter et al. (2021). ‘Impact of minimum unit pricing on alcohol purchases in Scotland
and Wales: controlled interrupted time series analyses’. In:The Lancet Public Health6.8, e557–
e565.DOI:10.1016/S2468-2667(21)00052-9.
Angus, Colin, John Holmes and Petra S. Meier (2019). ‘Comparing alcohol taxation throughout the
European Union’. In:Addiction114.8, pp. 1489–1494.DOI:10.1111/add.14631.
Banks, James, Richard Blundell and Arthur Lewbel (1997). ‘Quadratic Engel Curves and Consumer
Demand’. In:The Review of Economics and Statistics79.4, pp. 527–539.DOI:10 . 1162 /
003465397557015.
Berry, Steven, James Levinsohn and Ariel Pakes (1995). ‘Automobile Prices in Market Equilib-
rium’. In:Econometrica63.4, pp. 841–890.DOI:10.2307/2171802.
Bonaldi, Christophe and Catherine Hill (2019). ‘La mortalité attribuable à l’alcool en France en
2015’. In:Bulletin Epidemiologique Hebdomadaire, pp. 97–108.
Bonnet, Céline and Pierre Dubois (2010). ‘Inference on vertical contracts between manufactur-
ers and retailers allowing for nonlinear pricing and resale price maintenance’. In:The RAND
Journal of Economics41.1, pp. 139–164.DOI:https : / / doi . org / 10 . 1111 / j . 1756 -
2171.2009.00093.x.
Bonnet, Céline and Vincent Réquillart (2013). ‘Tax incidence with strategic firms in the soft drink
market’. In:Journal of Public Economics106, pp. 77–88.DOI:10.1016/j.jpubeco.2013.
06.010.
Calcott, Paul (2019). ‘Minimum unit prices for alcohol’. In:Journal of Health Economics66,
pp. 18–26.
Cecchini, Michele and Marion Devaux (2021). ‘Addressing harmful alcohol use’. In:Preventing
Harmful Alcohol Use, pp. 21–68.
Cheatley, Jane et al. (2021). ‘Policies and best practices for reducing the harful consumption of
alcohol’. In:Preventing Harmful Alcohol Use, pp. 179–250.
49

ˇCiderová, Tereza and Milan Šˇcasný (2022). ‘Estimation of alcohol demand elasticity: Consumption
of wine, beer, and spirits at home and away from home’. In:Journal of Wine Economics17.4,
pp. 329–337.DOI:10.1017/jwe.2022.42.
Cubertafond, Martin (2015).Entreprendre dans le vin: stratégies 360° pour réussir sur le marché
mondial du vin. Editions Eyrolles.
Deaton, Angus and John Muellbauer (1980). ‘An Almost Ideal Demand System’. In:The American
Economic Review70.3, pp. 312–326.
Disease, Global Burden of (2018). ‘Global, regional, and national incidence, prevalence, and years
lived with disability for 354 diseases and injuries for 195 countries and territories, 1990–2017:
a systematic analysis for the Global Burden of Disease Study 2017’. In:The Lancet392.10159,
pp. 1789–1858.DOI:10.1016/S0140-6736(18)32279-7.
Dubois, Pierre, Rachel Griffith and Martin O’Connell (2018). ‘The Effects of Banning Advertising
in Junk Food Markets’. In:The Review of Economic Studies85.1, pp. 396–436.DOI:10.1093/
restud/rdx025.
Elder, Randy W. et al. (2010). ‘The effectiveness of tax policy interventions for reducing excessive
alcohol consumption and related harms’. In:American Journal of Preventive Medicine38.2,
pp. 217–229.
Gordon, R., D. Heim and S. MacAskill (2012). ‘Rethinking drinking cultures: A review of drinking
cultures and a reconstructed dimensional approach’. In:Public Health126.1, pp. 3–11.DOI:
10.1016/j.puhe.2011.09.014.
Griffith, Rachel, Martin O’Connell and Kate Smith (2019). ‘Tax design in the alcohol market’. In:
Journal of Public Economics172, pp. 20–35.
— (2022). ‘Price Floors and Externality Correction’. In:The Economic Journal132.646, pp. 2273–
2289.DOI:10.1093/ej/ueac011.
Hausman, Jerry, Gregory Leonard and Daniel McFadden (1995). ‘A utility-consistent, combined
discrete choice and count data model Assessing recreational use losses due to natural resource
damage’. In:Journal of Public Economics56.1, pp. 1–30.DOI:10.1016/0047- 2727(93)
01415-7.
Hausman, Jerry, Gregory Leonard and J. Douglas Zona (1994). ‘Competitive analysis with differ-
enciated products’. In:Annales d’Economie et de Statistique, pp. 159–180.
Hendel, Igal and Aviv Nevo (2006). ‘Sales and consumer inventory’. In:The RAND Journal of
Economics37.3, pp. 543–561.DOI:10.1111/j.1756-2171.2006.tb00030.x.
INSERM (2021).Réduction des dommages associés à la consommation d’alcool. INSERM. EDP
Sciences.
Kopp, Pierre (2015).Le coût social des drogues en France. Observatoire Français des Drogues et
des Toxicomanies, p. 75.
Lecocq, Sébastien, Valérie Orozco et al. (2023). ‘Alcohol Price Regulation in France: Choosing
a Reform Scenario to Achieve Public Health and Tax Fairness Objectives’. In:Economie et
Statistique541.1, pp. 17–33.DOI:10.24187/ecostat.2023.541.2105.
Lecocq, Sébastien and Jean-Marc Robin (2015). ‘Estimating Almost-ideal Demand Systems with
Endogenous Regressors’. In:Stata Journal15.2, pp. 554–573.
Llopis, Eva Jané, Amy O’Donnell and Peter Anderson (2021). ‘Impact of price promotion, price,
and minimum unit price on household purchases of low and no alcohol beers and ciders: De-
scriptive analyses and interrupted time series analysis of purchase data from 70, 303 British
50

households, 2015–2018 and first half of 2020’. In:Social Science & Medicine270, p. 113690.
DOI:https://doi.org/10.1016/j.socscimed.2021.113690.
Millot, Ana et al. (2022). ‘An Analysis of How Lobbying by the Alcohol Industry Has Eroded the
French Évin Law Since 1991’. In:Journal of Studies on Alcohol and Drugs83.1, pp. 37–44.
DOI:10.15288/jsad.2022.83.37.
Miravete, Eugenio J., Katja Seim and Jeff Thurk (2018). ‘Market Power and the Laffer Curve’. In:
Econometrica86.5, pp. 1651–1687.DOI:10.3982/ECTA12307.
O’Donnell, Amy et al. (2019). ‘Immediate impact of minimum unit pricing on alcohol purchases in
Scotland: controlled interrupted time series analysis for 2015-18’. In:BMJ366, p. l5274.DOI:
10.1136/bmj.l5274.
OMS (2010).Global Strategy to Reduce the Harmful Use of Alcohol. Tech. rep. Organisation
Mondiale de la Santé.
Palle, C. (2013). ‘Le poids économique de l’alcool’. In:OFDT, Drogues et Addictions-Données
Essentielles. Saint-Denis: OFDT, pp. 154–159.
Petrin, Amil and Kenneth Train (2010). ‘A Control Function Approach to Endogeneity in Consumer
Choice Models’. In:Journal of Marketing Research47.1, pp. 3–13.DOI:10.1509/jmkr.47.
1.3.
Praud, Delphine et al. (2016). ‘Cancer incidence and mortality attributable to alcohol consumption:
Alcohol Attributable Cancers’. In:International Journal of Cancer138.6, pp. 1380–1387.DOI:
10.1002/ijc.29890.
Rey, Patrick and Thibaud Vergé (2010). ‘Resale Price Maintenance and Interlocking Relation-
ships*’. In:The Journal of Industrial Economics58.4, pp. 928–961.DOI:https://doi.org/
10.1111/j.1467-6451.2010.00439.x.
Robinson, Mark et al. (2021). ‘Evaluating the impact of minimum unit pricing (MUP) on off-trade
alcohol sales in Scotland: an interrupted time–series study’. In:Addiction116.10, pp. 2697–
2707.DOI:10.1111/add.15478.
Roodman, David (2020).The impacts of alcohol taxes: A replication review.
Ruiz, Nicolas and Alain Trannoy (2008). ‘Le caractère régressif des taxes indirectes: les enseigne-
ments d’un modèle de microsimulation’. In:Economie et statistique413.1, pp. 21–46.
Sassi, Franco et al. (2014). ‘Taxation and economic incentives’. In:Regulating Lifestyle Risks. The
EU, Alcohol, Tobacco and Unhealthy Diets.pp. 94–119.
Sharma, Anurag, Fabrice Etilé and Kompal Sinha (2016). ‘The effect of introducing a minimum
price on the distribution of alcohol purchase: a counterfactual analysis’. In:Health Economics
25.9, pp. 1182–1200.
Shield, Kevin, Jakob Manthey et al. (2020). ‘National, regional, and global burdens of disease from
2000 to 2016 attributable to alcohol use: a comparative risk assessment study’. In:The Lancet
Public Health5.1, e51–e61.
Shield, Kevin, Claire Marant-Micallef et al. (2018). ‘New cancer cases in France in 2015 attributable
to different levels of alcohol consumption: Alcohol-attributable cancer cases in France’. In:
Addiction113.2, pp. 247–256.DOI:10.1111/add.14009.
Srivastava, Preety et al. (2015). ‘Disaggregated econometric estimation of consumer demand re-
sponse by alcoholic beverage types’. In:Australian Journal of Agricultural and Resource Eco-
nomics59.3, pp. 412–432.DOI:10.1111/1467-8489.12095.
51

Stockwell, Tim et al. (2012). ‘The raising of minimum alcohol prices in Saskatchewan, Canada:
impacts on consumption and implications for public health’. In:American journal of public
health102.12, e103–e110.
Wagenaar, Alexander C., Amy L. Tobler and Kelli A. Komro (2010). ‘Effects of alcohol tax and
price policies on morbidity and mortality: a systematic review’. In:American journal of public
health100.11, pp. 2270–2278.
Wilson, Luke B. et al. (2021). ‘The effect of alcohol tax changes on retail prices: how do on-trade
alcohol retailers pass through tax changes to consumers?’ In:The European Journal of Health
Economics, pp. 1–12.
Xhurxhi, Irena Palamani (2020). ‘The early impact of Scotland’s minimum unit pricing policy on
alcohol prices and sales’. In:Health Economics29.12, pp. 1637–1656.DOI:10.1002/hec.
4156.
Zhao, Jinhui and Tim Stockwell (2017). ‘The impacts of minimum alcohol pricing on alcohol
attributable morbidity in regions of British Colombia, Canada with low, medium and high mean
family income’. In:Addiction112.11, pp. 1942–1951.DOI:10.1111/add.13902.
52

Supplementary Appendix:
Minimum pricing or volumetric taxation?
Quantity, quality and competition effects of price regulations in
alcohol markets.
A Data: details
Our models were developed and calibrated on the 2014 Kantar Worldpanel (KWP) household panel
data. It is important to know the main features of the data in order to understand some of our
modeling choices. This appendix provides additional details on the Kantar WorldPanel household
scanner survey, and on how we prepared the data for the modeling work.
A.1 Data preparation
A.1.1 Sample selection
The panel is representative of the French population. Households may be followed for several years.
In the KWP data, the calendar year is divided into 13 periods of 4 weeks. The reporting activity of
each household is evaluated for each of these periods. Households are awarded points added to an
account, depending on their activity during the four-week period, and can redeem their points for
an award of their choice.33
KWP classifies a household as inactive if it has not reported enough purchases compared to a
minimum expected level (based on its past reporting behavior and its sociodemographic character-
istics). In 2014, 28,375 households were enrolled in the panel, of which 24,177 were considered to
actively report their food and beverage purchases over at least one four-week period.
A period-specific sample weight is calculated for each active household in order to make the
sample of active households representative of the French population for the period. KWP uses
marginal calibration based on the following household characteristics: age of the household head
(4 categories), income class (4 categories), age of the household head (4 categories) interacted with
family structure (5 categories), profession of the household head (7 categories), region of residence
(8) interacted with type of residence area (4 categories). The minimum time step for analyzing
household purchases is therefore a 4-week period, and inactive households must be dropped from
the analysis.
All participating households must report their purchases of barcoded products: they form the
GC panel (GC: Gen-Coded = barcoded, N = 24,177 households). Approximately half of them (N
= 13,395) are also members of a second panel, called PF (PF: Produits Frais = Fresh products).
PF households also have to report their purchases of products without barcodes. Most alcohol
beverages sold in stores have a barcode. However, some wines, ciders, and beers produced by small
local manufacturers are only present in the PF panel. We therefore focus on the PF panel.
33See the awards onhttps://www.boutiquepaneliste.com/decouvrir_cadeaux
53

Figure A.1: Selection of households and samples construction
Kantar WorldPanel data 2013 and 2014
25,649 active households in2013
11,952 households in 2013
active at least 3 periods
panel PF
11,224 alcohol purchasers
in 2013
2,110 no alcohol purchasers
in 2014
24,177 active households in2014
12,170 households
active at least 3 periods
panel PF
S0
11,463 alcohol purchasers
in 2014
S1
9,114 alcohol purchasers
in 2014and2013
S2
13,573 alcohol purchasers
in 2014or2013
S3
11 463+2110
For the computation of market statistics, we decided to keep only households that are active
for at least 3 periods out of 13 in order to avoid introducing too much noise in the estimates (e.g.,
households being active only in Christmas, when purchases are more likely). This is sample S0
(N = 12,170 households). Within this sample, we only keep households that purchased alcoholic
beverages at least once in 2014, because nonpurchasers are unlikely to start purchasing if a health-
oriented price regulation is implemented. This is sample S1 (N = 11,463 households) that is used to
produce the market and household statistics in Section 2.
To control consumption habits in the modeling of demand, we use purchases observed in 2013.
The mixed multinomial logit models of quality demand are thus estimated in the subsample S2 of
households that are in S1, and were also active at least 3 periods out of 13 in PF 2013. The S2
subsample includes 9,114 households.
Finally, in modeling the substitutions in quantities between broad alcohol categories (e.g., wine
for beer), we use a standard Quadratic Almost Ideal Demand System model. To minimize troubles
with zero consumptions in some categories - most households do not purchase in all alcohol categor-
ies -, we aggregate households into clusters that are based, in part, on consumption habits observed
in 2013. To maximize the number of households used in the aggregation, we add to S1 those house-
holds that are observed in 2014 not in S1, but were active at least 3 periods out of 13 in PF 2013
ANDhad at least one alcohol purchase in 2013. This is our sample S3. Figure A.1 summarizes the
sample selection process.
54

A.1.2 Sample weights and sample comparison
KWP provides sample weights for all household-year observations in the permanent PF subpanel,
and all household-period observations in the PF panel. Period-specific weights are non-null only for
those households that were active during the period. We normalized the household sample weights
so that they sum to the same numberH S =12,000 at each period. Letω h,t be the sample weight for
householdh, periodt, we normalized it for sampleSso that:
ωS h,t =H S ωh,t
∑
h∈S
ωh,t
(A.1)
Table A.1 compares the average characteristics of households and adult household members in
the three samples. The three samples are very similar.
A.2 Definition of product nomenclature
In the markets for beers, ciders, and sparkling wines, a productjwas defined as an alcoholic bever-
age from a given quality segment, labeled with a given brand, produced by a given manufacturer,
sold by a given retailer. For aperitifs and spirits, a product was defined according to the same charac-
teristics plus the binary characteristic "alcohol-free" (7 brands for aperitifs, 3 brands for spirits). For
still wines, a productjwas defined using only the subcategory, the manufacturer, and the retailer.
We now detail the construction of these characteristics.
A.2.1 Quality segments
Each alcohol category is divided into quality segments making sub-categories:
• Beers: Alcohol-free, Bock/Premium, Special,
• Ciders: Sweet, Raw,
• Sparkling Wines: Champagne, other sparkling wines,
• Still Wines: Vin de table, Vin de pays, Vin d’appellation (with a designation of origin),
• Spirits: Rum, Whisky, Aniseed, Liquors, Other,
• Aperitifs: Cocktails/Punches, Liquor wines, Natural sweet wines, Amer/Gentiane/Vermouth,
Other.
Vin de Table is France’s lowest level of wine classification. They can result from the blending of
wines from different geographical origins, made with very different grape varieties, produced with
unregulated yields, and often made from imported grapes (often from Spain). They do not require
a vintage date. Vin de Pays is a classification one level above Vin de Table. Grapes come from a
well-defined geographical area and are produced in limited yields. Vin de Pays has recently been
relabeled as IGP wines (IGP: Protected Geographic Indication). Vins d’Appellation is the highest
classification. It corresponds to a name geographical areas, and producers are submitted to strict
55

Table A.1: Households and individuals characteristics
Sample: S1 S2 S3
Nb of households11,463 9,114 13,573
Nb of adults22,728 18,197 26,768
Nb of individuals30,077 23,456 35,707
Households characteristics (%)
Not in the 2013 panel19.2 0.0 16.9
City size. . .
More 20000 57.6 57.8 57.9
Less 20000 42.4 42.2 42.1
Nb of children. . .
0 72.3 74.8 71.2
1 13.0 11.7 13.5
2 10.9 10.1 11.4
[3+[ 3.8 3.4 3.9
Income categories. . .
High 15.7 15.8 15.7
High-middle 29.7 30.0 29.2
Low-middle 40.2 40.8 40.2
Low 14.4 13.4 14.9
Standard drinks/day/household member in 2013. . .
[0,1] 66.5 66.5 68.9
]1,2] 16.5 16.5 15.7
]2,+inf[ 17.0 17.0 15.4
Notes: Percent forStandard drinks/day/household adult membersare calculated on
households that are present in 2013. All statistics are produced using the house-
holds sample-specific weights (average of all period weights over 2013-2014) - see
A.1.2 for their computation. The four income categories are produced by Kantar
WorldPanel from self-reported household monthly income adjusted for the number
of consumption units (OECD equivalence scale).
56

constraints regarding the yields, the use of grape varieties, how the grapes are gown and harvested
and how the wine is made.
A.2.2 Brands, manufacturers and retailers
In 2014, in each market (except wines), some manufacturers had (and still have) large market shares
and offered several brands. For modeling and inference, we decided to define an aggregate of
small manufacturers that sold brands with tiny market shares and, therefore, a very small number of
purchases in our 2014 data: in each market model, a manufacturer "Other" will sell a unique brand
"Other". Larger manufacturers will also have an aggregate brand "Other". Table A.2 lists the main
manufacturers.
We decided to define seven distribution channels: Leclerc/Galec, Intermarché, Auchan, Carre-
four, Casino/EMC Distribution, an aggregate of hard discounters (11.56%), and an aggregate of
other shopping places (16.05%). The first five are the main and largest retailing companies, rep-
resenting 80% of food and drink sales in France. The aggregate of other shopping places is a het-
erogeneous collection of independent shops, cellars, direct-from-producers distribution channels,
stores of minor retail companies.
In our data, about 95% of alcohol purchases were made in 2014 in large retail outlets that were
affiliated with a central purchasing agency. We observe very few purchases at independent cellars
or direct purchases at cooperatives or farms. When we focus on wine drinkers, about 18% of them
shopped at least once in a place that was not a large retail outlet. This proportion increases to
25% when we consider the upper median of wine drinkers (in quantity). For comparison, a 2019
consumer survey (N=1,200 alcohol consumers) found a proportion slightly higher than 30%. 34.
Therefore, the Kantar Worldpanel data slightly cover the upper quality segment of the alcohol mar-
kets (luxury segment). We do not see this as a limit, as the economic and epidemiological burden
of alcohol is likely to be concentrated in the everyday and premium segments.
34Seehttps://www.cavistesprofessionnels.fr/pro/etude-clients-cavistes-images-2019
57

Table A.2: Main Manufacturers
Ciders Beers Aperitifs Spirits Still wine Sparkling wines
ETS MAEY AERT KARLSBERG BRAUEREI KG WEBER VINADEIS RHUMS REUNION VINADEIS LES GRANDS CHAIS DE FRANCE
AGRIAL AB INBEV GROUPE CASTEL DAMOISEAU FRERES LES GRANDS CHAIS DE FRANCE GROUPE CASTEL
LES CELLIERS ASSOCIES BRASSERIE DE SAINT OMER UNICOOPS BACARDI / MARTINI GROUPE CASTEL LVMH
DUJARDIN ABBAYE DE WESTMALLE TERROIRS DISTILLERS BOUGUET PAU BARON PHILIPPE DE ROTHSCHILD COMPAGNIE FRANCAISE DES GRANDS VINS
ABBAYE NOTRE-DAME DE SAINT-REMY CANTINE PELLEGRINO GIFFARD UNION DES VIGNERONS DES COTES DU R CENTRE VINICOLE CHAMPAGNE N FEUILL
DIFCOM LA CA VE DES PERES CROP ENERGIES FAMILLE CAY ARD CHANTOVENT CHARLES DE CAZANOVE
BA V ARIA BREWERY J. GARCIA CARRION LISTEL LANSON-BCC
BRASSERIE CASTELAIN PICARD VINS ET SPIRITUEUX LEJAY LAGOUTE SOCIETE COOPERATIVE AGRICOLE WOLFB CHAMPAGNE ALAIN THIENOT
BRASSEURS DE GAY ANT FELIX SOLIS LIXIR UNION DES CA VES COOPERATIVES DE L’ LES CHAMPS RENIERS
BRASSERIE LINDEMANS BACARDI / MARTINI MARIE BRIZARD MARIE BRIZARD LES PETITS FILS DE LA VEUVE AMBAL
BRASSERIE DE BRABANDERE BOUGUET PAU MHD ACKERMAN
DUCH EXPORT FAMILLE CAY ARD PERNOD RICARD JAILLANCE
GPE CARLSBERG MARIE BRIZARD ROTHSCHILD LAURENT PERRIER
HEINEKEN MHD CHAMPAGNE JACQUART
TSINGTAO PERNOD RICARD EPI - COMPAGNIE CHAMPENOISE PIPER
BRASSERIE LA CHOULETTE ROTHSCHILD BARON PHILIPPE DE ROTHSCHILD
BRASSERIE METEOR VRANKEN LISTEL
BRASSERIE SAINT SYLVESTRE FREIXENET
DUVEL MOORTGAT SOCIETE COOPERATIVE AGRICOLE WOLFB
BRASSERIE DU BOCQ CHAMPAGNE ALFRED GRATIEN
BRASSERIE DUYCK FAMILLE MONMOUSSEAU
CHATEAU MONCONTOUR
ALLIANCE LOIRE
BLMI
UJVR
BARON DE HOEN
CA VE DES PRODUCTEURS DE VINS DE MO
BACARDI / MARTINI
FAMILLE CAY ARD
LEJAY LAGOUTE
PERNOD RICARD
VRANKEN
Notes: This Table reports the names of the main manufacturers by alcohol category.
58

A.3 Computation of key variables
A.3.1 Alcohol contents
KWP provides information on a number of observed product characteristics, such as brand, man-
ufacturer, alcohol category, and alcohol degreed. However, information on alcohol degree was
missing for about 9% of the references, representing 1% of purchase acts. We first imputed the
missing values using information available in previous years of the panel for products with the
same unique KWP-code, or from all other products with similar observed characteristics (using a
weighted average). We also used additional information from producers’ and retailers’ websites.
The alcohol degree information was used to compute quantities of ethanol in grams or standard
drinks, with the following formula:35
e j =0.8×d j ×V j ∗1000 (A.2)
whered j is the degree andV j is the volume (in L) of one market unit of productj.
A.3.2 Formula for prices and consumptions
KWP provides for each purchase the quantity that was purchasedq, with the corresponding ex-
penditurey. KWP also provides correction factors that must be applied to quantities and expendit-
ures to ensure that the purchase sample is representative of markets for each product category in
each four-week period. By construction, the smallest time step is the period: one should not use
these data to analyze purchase variations from one week to another. We use information on pack-
aging (number of units per item and unit volume) to calculate the total volume of a given product in
a given purchase act, taking into account bulk promotions.
These household-purchase-level quantities and expenditures can be appropriately summed to
compute period-specific househol-level quantities, ethanol purchases, and expenditures by alcohol
categorya,Q ah t ,E ah t andY ah t , or by productsj q h jt,e h jt andy h jt. Dividing expenditures by quantities
at the product level yields unit prices.
The price of a productjin alcohol categoryaat periodtwas computed according to the follow-
ing formula:
pa jt = ∑h∈S1 ωS1 h,tyh jt ∑h∈S1 ωS1 h,tqh jt (A.3)
whereω S1 h,t is the sample weight for householdh,y h jt is the household total expenditure in periodt
for productjandq h jt the corresponding purchased quantity. Note that the prices were constructed
using sample S1, in order to use a maximum number of transaction prices.
KWP also provides various formulas for computing averages of household consumption. As
households were not active in all 4-week periods, we had to correct household-level averages by
the number of active periodsN ACT,S h = ∑t 1 n ωS h,t ̸=0 o . The yearly ethanol consumption at the
35For example, a standard wine bottle (0.75L) thus represents 0.8 x 12% x 750 = 72 grams of ethanol, or 7.2 standard
drinks.
59

household level is then given by:
Eh,S = ∑
t
∑
a
Eah t 13 NACT,S h (A.4)
This formula was used, inter alia, to calculate the average number of standard drinks per day per
adult household member in 2013 (after division by 365×10×the number of adult household mem-
bers; see the statistics in Table A.1).
The average yearly quantities of ethanol were calculated at the population level by applying the
following formula:
ES = ∑h∈S

∑t

ωS h,t ∑a Eah t

∗ 13 NACT,S h

HS (A.5)
A.4 Comparison with the French Family Budget Survey 2017
Since the 2000s, economic studies analyzing markets for fast-moving consumer goods and evaluat-
ing policies aimed at regulating the consumption of such goods have mainly relied on scanner data.
The Kantar WorldPanel (KWP) homescan data have three advantages over theBudgets de famille
(Family Budget Surveys, FBS) for the analysis of alcohol price regulations. First, they provide in-
formation on quantity, quality, and expenditure, while information on quantities is only available
for 36% of purchases in the 2017 FBS. Second, the alcohol categories of the FBS nomenclature are
too aggregated to allow a precise study of the potential fiscal impact of reform scenarios targeting
the alcohol content of beverages. Third, these panel scanner data follow purchases by the same
households throughout the year, which limits the observation of zero consumption due to infrequent
purchases (Dubois et al. 2022). Fourth, they allow for very precise measurements of prices (Ruhm
et al. 2012).
Purchase scanner data are also less likely to be affected by bias due to under-reporting of alcohol
quantities than are health data. As the survey does not specifically focus on the risks posed by
alcohol, it does not make salient the stigma associated with excessive drinking. However, reporting
requires more effort from respondents, raising questions about the quality of the data in terms of
their representativeness and coverage of the population.
All of our analyzes use the sociodemographic sample weights provided by the KWP. These
weights are determined using a margin calibration procedure that takes into account the sociopro-
fessional and age categories of the reference person, the number of persons in the household com-
bined with the age category of the reference person, the region of residence, and the standard of
living of the household. The actual representativeness of the household panel and the quality of the
collected scanner data can be questioned, especially compared to the FBS. Lecocq et al. (2023) com-
pare the distribution of the sampling characteristics of households in the Kantar panel with that of
households included in the 2017 FBS. They find that the KWP sample under-represents households
where the reference person is aged between 50 and 64, as well as managers, intermediate occupa-
tions, and white-collar workers, and over-represents blue-collar workers and pensioners. Some of
the differences between the two data sources can be explained by differences in the way the samples
were built-up (Zhen et al. 2009). Young, affluent and dual-income households are less represented
in the scanner data because the survey requires a degree of diligence. Conversely, working-class
60

retired households are over-represented, possibly because they have more free time and because
active participation in the survey is rewarded with points that can be converted into vouchers.
Lecocq et al. (2023) also compare the aggregated expenditure volumes for the categories of
alcoholic beverages in the Classification of Individual Consumption by Purpose (COICOP) used in
the FBS surveys. They show that the structure of expenditure observed in the 2014 KWP data is very
similar to that calculated from the 2017 FBS data, with, for example, a total expenditure volume of
10.38 billion according to the former vs. 11.37 billion in the latter, with the difference attributed
to higher expenditure in unit value among higher income households. Table A.3 reproduces their
results. Finally, we should note a limitation common to both surveys. They do not allow for a
precise identification of alcohol purchases for consumption away from home. This information is
not available in the KWP data we have. It is included in the group "meals outside the home", which
aggregates food and drinks, in the 2017 FBS.
Table A.3: Aggregate expenditure, 2014 Kantar WorldPanel vs. 2017 Family Budget Survey
Expenditure (Cbn) Budget share of alcohol expenditure (%)
Survey KWP 2014 FBS 2017 KWP 2014 FBS 2017
Spirits and liqueurs 3.03 2.93 29.23 25.77
Wines and ciders 4.04 5.08 38.95 44.68
Other wine-based aperitifs, champagne 1.81 1.54 17.46 13.54
and other sparkling wines
Beer and beer-based drinks 1.49 1.82 14.37 16.01
Total alcoholic beverages 10.38 11.37 100.00 100
Notes: Market size statistics by value calculated by applying the household sampling weights provided by each survey;
for comparison, we have used the COICOP nomenclature from FBS 2017.
Sources and coverage:2017 Family Budget Survey , INSEE; 2014 Kantar WorldPanel; full samples.
61

A.5 Current tax system
Table A.4 displays the excise taxes that were applied to alcohol products in 2014 and 2020 in France.
It shows two important points. First, taxes on wines are lower than those on other alcohol, while
spirits are heavily taxed. Second, in addition to wines, there are tax exemptions for products that
are more likely to be produced in France or by French-owned companies, such as ciders, beers from
small breweries, and spirits from overseas territories. In the study, we provide more precise statistics
showing that excise taxes are partially decorrelated from the alcohol content of the products.
Table A.4: Excise taxes on alcohol products in 2024 and 2014
2024 2014
Excise taxes
Droits de circulation
Still wines (e/hl) 4.05 3.72
Sparkling wines (e/hl) 10.02 9.23
Ciders and alike (poirés, hydromel) (e/hl) 1.41 1.31
Droits spécifiques
Beer≤2.8% vol (e/°/hl) 3.98 3.66
Beer >2.8% vol + small brewery (e/°/hl) 3.98 3.66
Beer >2.8% vol + large brewery (e/°/hl) 7.96 7.33
Droits de consommation
Rum from DOM (e/hlap) 933.78 859.79
Other alcohol, e.g., spirits (e/hlap) 1866.52 1718.61
Natural sweet / liquor wines (e/hl) 50.6 46.59
Other intermediary products (e/hl) 202.39 186.36
Social security tax (alcohol >18% vol or 0.5% for beers)
Vin doux naturels / de liqueur (e/hl) 20.26 18.64
Other intermediary products (e/hl) 50.6 46.59
Beers, small brewery (e/hl) 50.6 1.47
Beers, large brewery (e/hl) 50.6 2.93
Other alcohol (e/hlap) 599.31 551.82
Notes: DOM: overseas territories ; hl = hectoliter; hlap = hectoliter of pure alcohol.
62

A.6 Additional descriptive statistics
Table A.5: Purchase volumes (L) by household type and alcohol category
Total Income category Risk category
High Mid-high Mid-low Low≤1]1,2]>2
Yearly purchase volumes (L) 76.19 62.51 72.95 82.66 80.29 29.54 101.63 234.17
Shares (%)
Ciders 2.22 2.54 2.15 2.20 2.13 4.77 2.59 0.84
Beers 31.57 25.58 30.97 32.60 35.05 44.04 33.63 24.64
Aperitifs 5.13 4.64 5.17 4.92 6.15 7.24 5.66 3.89
Spirits 7.81 8.06 7.39 7.79 8.53 6.74 7.46 8.48
Still wines 48.29 53.51 49.28 47.44 44.00 31.38 44.62 57.98
Sparkling wines 4.98 5.67 5.04 5.05 4.14 5.83 6.04 4.17
Notes: N=11,463 households (Sample S1). Statistics computed from purchase data using household and purchase
sample weights. The four income categories are defined by KWP, based on household self-reported income and the
number of OECD consumption units. The three risk categories are defined based on the average number of standard
drinks per week per adult household member purchased by the household in 2013.
Table A.6: Purchase volumes (standard drinks) by household type and alcohol category
Total Income category Risk category
High Mid-high Mid-low Low≤1]1,2]>2
Weekly standard drinks 13.6 11.7 13.0 14.7 14.1 4.5 17.8 45.4
Share (%)
Ciders 0.69 0.82 0.67 0.67 0.65 1.67 0.84 0.26
Beers 13.17 11.17 13.10 13.53 14.15 20.93 14.50 9.71
Aperitifs 5.51 4.75 5.70 5.51 5.85 8.30 6.25 4.17
Spirits 25.72 25.09 24.20 25.93 28.90 24.06 24.99 26.61
Still wines 49.87 52.74 51.17 49.23 46.30 38.18 47.19 55.30
Sparkling wines 5.04 5.43 5.16 5.13 4.15 6.86 6.23 3.95
Notes: N=11,463 households (Sample S1). Statistics computed from purchase data using household and purchase
sample weights. Weekly standard drinks not adjusted for household size. The four income categories are defined by
KWP, based on household self-reported income and the number of OECD consumption units. The three risk categories
are defined based on the average number of standard drinks per week per adult household member purchased by the
household in 2013.
63

Table A.7: Within-category market shares, prices and alcohol degree by sub-category
Beers Ciders Sparkling wines Still wines Aperitifs Spirits
Market Shares (%)
Alcohol-free Sweet Champagnes de Table Cocktails and Punch Rum
6.08 (2.35) 36.51 (2.76) 27.94 (6.13) 18.93 (1.58) 18.00 (2.87) 11.39 (1.06)
Bock and premium Raw Other sparkling wines de Pays Liqueur wines Whisky
44.48 (2.27) 63.49 (2.76) 72.06 (6.13) 23.22 (2.96) 19.42 (2.36) 40.60 (2.16)
Special d’Appellation Natural sweet wines Aniseed
48.68 (4.05) 57.85 (3.78) 14.76 (1.64) 26.72 (2.83)
Amer, Gentiane, Vermouth Liquors
26.18 (4.18) 12.66 (1.53)
Other Other
21.63 (5.45) 8.62 (1.02)
Prices (e/L)
Alcohol-free Sweet Champagnes de Table Cocktails and Punch Rum
1.37 (0.44) 2.66 (0.70) 25.95 (7.82) 2.52 (0.79) 5.90 (3.57) 16.13 (4.03)
Bock and premium Raw Other sparkling wines de Pays Liquor wines Whisky
2.64 (1.36) 2.78 (0.75) 5.99 (2.00) 3.16 (0.72) 9.58 (2.05) 21.80 (7.55)
Special d’Appellation Natural sweet wines Aniseed
3.21 (1.02) 5.49 (2.02) 6.02 (1.88) 12.74 (6.11)
Amer, Gentiane, Vermouth Liquors
7.08 (3.32) 14.89 (6.52)
Other Other
6.03 (4.02) 17.70 (4.06)
Alcohol degree (°)
Alcohol-free Sweet Champagnes de Table Cocktails and Punch Rum
0.71 (0.20) 2.00 (0.00) 12.00 (0.01) 12.00 (0.60) 8.40 (6.81) 44.92 (0.72)
Bock and premium Raw Other sparkling wines de Pays Liquor wines Whisky
4.58 (0.53) 4.47 (0.18) 11.38 (2.60) 12.00 (0.42) 18.34 (1.18) 40.00 (0.10)
Special d’Appellation Natural sweet wines Aniseed
7.04 (1.07) 12.03 (0.15) 15.56 (0.35) 32.44 (19.72)
Amer, Gentiane, Vermouth Liquors
12.79 (6.38) 21.21 (7.77)
Other Other
11.16 (6.33) 36.02 (5.66)
Tax level (e/L) - V AT excluded
Alcohol-free Sweet Champagnes de Table Cocktails and Punch Rum
0.03 (0.01) 0.01 (0.00) 0.10 (0.12) 0.04 (0.00) 1.21 (1.53) 7.61 (1.77)
Bock and premium Raw Other sparkling wines de Pays Liquor wines Whisky
0.32 (0.07) 0.01 (0.00) 0.09 (0.02) 0.04 (0.00) 0.58 (0.07) 9.08 (0.02)
Special d’Appellation Natural sweet wines Aniseed
0.47 (0.11) 0.04 (0.00) 0.47 (0.00) 7.38 (4.44)
Amer, Gentiane, Vermouth Liquors
2.03 (1.07) 4.25 (2.07)
Other Other
1.24 (1.48) 8.11 (1.47)
Notes: Market statistics computed from household purchase data of sample S2, using household and purchase acts sample weights. Standard
deviation which describes the variability of market shares across periods, and the variability of prices, alcohol degrees and taxes across periods
and product varieties.
64

A.7 Differences between the three samples
One may be concerned that we do not calibrate all parts of our model on exactly the same datasets.
The Appendix Table A.1 shows that the different samples do not differ in terms of demographic
characteristics. In Table A.8 we also display statistics of household average consumption in 2014 in
the sample used for the descriptive statistics (S1) and the two samples used for the model calibration
(S2 and S3). The statistics for S2 are slightly higher than those for S1 and S3 because S2 excludes
from S1 households that were not observed purchasing alcohol at least once in 2013. These S1
households were missing in S2 either because they were inactive in 2013, included in 2014 in the
panel, or were truly abstinent in 2013. In the latter case, they are likely to have lower consumption
levels than the average of S1 households.
We have compared these statistics with other sources. Based on data from the national account
statistics, an official report evaluated total ethanol consumption per adult older than 15 years to be
9584 g/year in 2014 (OFDT, 2020). In another official report (France Agrimer, 2019), the yearly
average quantity of alcohol purchase is evaluated at 66L per household in 2017. Given our data
and samples, it is not surprising that our estimates fall in between: first, we decided to focus on
alcohol purchasers, and therefore we average purchases over a smaller population; second the na-
tional account data consider consumption for both at-home and away-from-home consumption (and
nonresidents as well as residents).
Table A.8: Household average alcohol consumption in 2014
Nb HH Week (L) Yearly (L) Standard drinks/week Standard drinks/year
Per Household. . . . .
S1 & S3 11463 1.47 76.19 13.57 709.35
S2 9114 1.51 78.29 14.24 740.58
Per capita (>16 yo). . . . .
S1 & S3 11463 0.84 43.45 7.95 413.15
S2 9114 0.88 45.72 8.36 435.00
Notes: All statistics are produced using the households sample-specific weights (average of all period weights over
2014) - see Appendix Section A.3.2 for their computation.
65

B Policy scenarios: details
In the tax reform scenarios, all current alcohol-specific taxes are replaced by a single volumetric
excise tax. For a productj, the new excise tax per liter of beverage (in euro/L),T 1 j , is defined as a
function ofd j, the alcohol degree of the product.
Under a uniform tax per alcohol degree,T 1 j is proportional tod j:T 1 j =t×d j, where the constant
tcan be varied by the policy-maker.
Under a progressive excise tax,T 1 j is a convex increasing function of the alcohol degree, as
the marginal tax rate increases at some thresholds. We consider a multi-tiered tax scheme with six
intervals for the alcohol degree: [0;5[, [5;10[, [10;15[, [15;25[, [25;45[ and [45;100]. We assume
that marginal taxation is twice higher in the second interval than in the first, three times higher in
the third than in the first, etc. Table B.1 provides the rule for calculating the new excise tax.
Table B.1: New Excise TaxT 1 j
Uni f orm Progressive
t×d j t×d j ifd j ∈[0;5[
t×d j t×(2d j −5)ifd j ∈[5;10[
t×d j t×(3d j −15)ifd j ∈[10;15[
t×d j t×(4d j −30)ifd j ∈[15;25[
t×d j t×(5d j −55)ifd j ∈[25;45[
t×d j t×(6d j −100)ifd j ∈[45;100[
For these two taxes, we calibrate the value oftto achieve one or another of the following two
objectives under the assumption that there are no reactions on the demand and supply sides of the
market.This calibration exercise does not rely on our model: it is a pure accounting calculation
that uses the price and purchase data observed in 2014.
1. Fiscal neutrality: all alcohol tax revenues, about 3.463Be(includingV AT revenues) are left
unaltered by the reform.
2. Neutrality for public finances: alcohol-specific tax revenues (excludingV AT revenues) col-
lected under the new tax scheme must cover the costs of alcohol for public finances (health
cares and enforcement of the law, minus retirement pensions): 3.918Beas evaluated by an
official report Kopp 2015. A factor of 0.58 is applied to social cost to account for the fact that
only 58% of total consumption takes place at home according to the epidemiological data of
the Nutrinet-Santé cohort.
The calibration results in a value oftthat is much lower (7.24 cts/degree/L) to achieve fiscal
neutrality than to achieve neutrality for public finances (14.57 cts/degree/L). This is due to the large
share of V AT in the current fiscal revenues, as ciders, beers and wines face little or no alcohol-
specific taxes and represent a large share of purchase volume. Fiscal neutrality is partly achieved by
maintaining the large contribution of V AT, while just equalizing the tax rates per grams of ethanol
66

across alcohol categories. In contrast, neutrality for public finances is obtained by imposing a direct
relationship between the social costs of alcohol and its specific taxes. The rationale here is that V AT
revenues cannot be easily directed to alcohol-related expenditures (health cares, health education,
information campaigns, etc.), while revenues from alcohol-specific taxes can.
Finally, we will simulate two scenarios for the minimum unit price policy (MUP). In a first
scenario, the current tax system will be maintained, while it will be replaced by the progressive tax
with fiscal neutrality in the second scenario. The minimum unit price will be set a 0.5e/standard
drink, which is similar to the MUP implemented in Scotland.
We end up with the following six scenarios:
1.Low uniform tax: a volumetric tax, uniform per alcohol degree, replacing all other alcohol-
specific taxes witht=0.0724 (7.24 cts/degree/L): Fiscal neutrality,
2.High uniform tax: a volumetric tax, uniform per alcohol degree, replacing all other alcohol-
specific taxes witht=0.1457 (14.57 cts/degree/L): Neutrality for public finances,
3.Low progressive tax: a volumetric tax, progressively increasing with alcohol degree, repla-
cing all other alcohol-specific taxes witht=0.0368 (3.68 cts/degree/L): Fiscal neutrality,
4.High progressive tax: a volumetric tax, progressively increasing with alcohol degree, repla-
cing all other alcohol-specific taxes witht=0.0674 (6.74 cts/degree/L): Neutrality for public
finances,
5.Minimum Unit Price: The addition of a Minimum Unit Price set at 0.5e/standard drink to
the current tax system
6.Minimum Unit Price + Low prog. tax: Minimum Unit Price and a progressive Excise
Tax withx=0.0368 (3.68 cts/degree/L) replacing all other alcohol-specific taxes: Fiscal
neutrality.
Each scenario will be simulated with and without the supply-side responses.
67

C Expected utility of a consumption occasion,u ah to
To identify the expected utility of a consumption occasion within a period, we conflate purchase acts
with consumption occasions. An observed purchase act results from the choice of a product within
a choice set that is made of all productsjavailable in the alcohol category,j=1, ...,J a t , plus an
outside option (j=0). Each purchase of a productjobserved in the data could be associated with
one or more consumption occasions (depending on the number of purchased units) that are given
the same utility. Thus, we assume that, within each alcohol category, variations in purchase volumes
across purchase acts are not correlated with product quality. Purchase volumes vary randomly across
purchase acts within a period, around an average that only depends on the purchase volume decided
for the period in the first stage of decision, and the number of purchase acts in the category, which
is exogenously determined. This rules out behaviors such as consumers systematically purchasing
more or less units of a brand that has a higher consumption utility, as well as within-period optimal
inventory management.
Consider householdhdecision to purchase a productjin alcohol categoryaat periodt. On
point-of-purchase, the anticipation of consumption occasions affects utility through the sum of the
product-household deterministic effect,β ahZah j , and a product-household-occasion specific shock
εah jto. The utility derived from the purchase isV ah jto =−α ahpa jt +β ahZa j +ε ah jto, while the utility anti-
cipated from consumption isv ah jto =β ahZa j +ε ah 0to (see equation 4 in Section 3.1).
A consumption occasion corresponds to the consumption of one quantity unit. Here, and in the
empirical implementation of the model, we assume that the specific shockε ah 0to remains constant
across all units of the same product purchased on the same shopping trip at the same point-of-
purchase. This allows us to treat one purchase act as revealing the consumption utility of one
consumption occasion.
We introduce an outside optionj=0 with utilityV ah 0to =V ah 0t +ε ah 0to representing any other product
in another alcohol category. We letd ah to denote the decision of purchasing productj(notedd ah to =j)
in alcohol categoryafor consumption occasiono.
We noteu ah to the expected utility benefit from any consumption occasion of product in category
a, conditional on the purchase of at least one product in that category. It is equal (up to any strictly
increasing transformation) to:
uah to ∼E
"
∑
j∈Jat
1
h
dah to =j

∃l∈J a t ,V ah lto >V ah 0to i vah jto #
=E
"
∑
k∈Jat
1
h
dah to =j

∃l∈J a t ,V ah lto >U ah 0to i  V ah jto +α ahpa jt #
=E
h
Max j∈Jat

V ah jto

∃l∈J a t ,V ah lto >V ah 0to i +E " ∑
j∈Jat
1
h
dah to =j

∃l∈J a t ,V ah lto >V ah 0to i αahpa jt #
=ln

∑
j∈Jat
exp

V ah jt −V ah 0t
!
+C+α ah ∑
j∈Jat
πah jt pa jt (C.1)
68

whereCis a constant associated to the computation of the first expectation term, andπ ah jt is the
probability of purchasing varietyjconditional on purchasing a product in categorya:
πah jt =E h 1 h dah to =j

∃l∈J a t ,V ah lto >V ah 0to ii (C.2)
This probability does not depend on the consumption occasionoas the latter affects purchase prob-
abilities through the random error-termεah 0to only. The presence of the constantCis related to the fact
that the absolute level of consumption utility cannot be defined. Some normalization is therefore
necessary. Here we use the counterfactual situation where categoryawould only be made of un-
differentiated products, i.e., a single homogeneous product. In comparison with this counterfactual
situation, we letb ah t (pa t )be the conditional consumer surplus from differentiation across products
withincategorya:
bah t (pa t ) = 1 αah
"
ln

∑
k∈Jat
exp(Vah jt −V ah ⋆t )
!
+α ah ∑
k∈Jat
πah jt  pa jt −p a ⋆t 
#
(C.3)
whereV ah ⋆t is the (deterministic) utility of a homogeneous product in categoryawhen there is no
differentiation across productsj, andp a ⋆t is the price of this product. This derivation uses the fact
that if the products were homogeneous in quality, then they would have the same prices and market
shares: ∑ j∈Jat πah ⋆t pa ⋆t =p a ⋆t = ∑ j∈Jat πah jt pa jt
The quality indexb ah t (pa t )is a measure of the consumer welfare gains from having access to
differentiated products in marketa. This surplus is zero when the products are not differentiated.
Using surplus as a measure of utility is a way to ensure that utility flows are normalized across
alcohol categories. The motivation here is that the utility flows are identified by using the purchase
data for each alcohol category and fitting random coefficient logit models for each market separately.
However, these models identify the random utility function up to a scale parameter. Since the
models are estimated separately for each categorya, we must normalize the scale. A natural scale
normalization is to take a money-metric measure of utility, by using the estimated marginal utility of
expenditure on each marketαah. Additionally, our normalization for quality differentiation naturally
implies that the utility of purchasing products inaif they were not differentiated would simply be
equal to one quantity unit of alcohol from categorya, as we would haveb ah t (pa t ) =0.
With these two normalizations, the utility of a consumption occasion isu ah to = (1+bah t (pa t ))
69

D Habit formation and stockpiling effects
Household purchases may show some dependence between periods due to (1) short-term habit form-
ation and (2) stockpiling during sale periods (Hendel and Nevo 2006a). Here we apply the test pro-
cedure implemented in Griffith et al. (2020) to test for these forms of intertemporal dependence. The
results suggest that these forms of dynamics are not of primary importance once household prefer-
ence heterogeneity is taken into account. Our results and conclusions are therefore very similar to
theirs.
We test for the presence of habit formation by running two regressions. In the first regression,
the dependent variable is a dummy variable equal to one if the household purchases alcohol in a
given period; in the second regression, the dependent variable is the number of standard drinks that
the household purchased conditional on purchasing. We consider periods of either one week or four
weeks. We regress these variables on the number of standard drinks purchased by the household in
each of the past eight periods, and period dummies. We estimate each regression with and without
household fixed-effects. As shown in Table D.1, we obtain a moderate relationship between past
and present behaviors in Ordinary Least Squares regressions with household and time fixed-effects.
For example, considering that the period length is a week, purchasing one more standard drink per
adult two weeks ago (t−2) is associated with (i) an increase in the probability of purchasing alcohol
of 0.12 percentage points, for an average of 17.9% and (ii) an increase of 0.04 standard drinks in
conditional purchase volumes for an average of 21.6 standard drinks. The results are of the same
order of magnitude when we take a period of four weeks. Finally, it is interesting to note that, in
the conditional quantity regressions, the coefficients on lagged quantities drop when we control for
fixed-effects. This shows that long-term habit formation is much more important than short-term
habit formation. We account for this heterogeneity by conditioning all of our empirical analyses on
the household average purchase volumes observed in 2013.
We also assess the existence of a state dependence arising from consumer stockpiling during
sale periods; if short-run price reductions lead to an increase in alcohol purchases, which are then
stored rather than immediately consumed, then the own-price elasticities of demand would be over-
estimated (see Hendel and Nevo (2006a)). To test this effect, we follow one of the suggestions in
Hendel and Nevo (2006b). We assume that each household has a constant consumption level equal
to the average number of standard drinks purchased per period. We calculate this level for each
household and combine it with its purchases per period to calculate its inventory at the beginning of
each period. We then regress (i) the probability of buying in a given period and (ii) the number of
standard drinks purchased (conditional on purchasing a positive amount) on this inventory variable,
period effects (which control for price changes, promotions, advertising, etc.), and household fixed-
effects. Hendel and Nevo (2006b) argue that if there is stockpiling, then a high inventory should
be associated with a lower probability of purchase or a smaller quantity purchased (conditional on
purchase). Whether the period is one or four weeks, we find in contrast a very weak positive rela-
tionship between the inventory variable on the one hand and the probability and quantity of alcohol
purchased on the other (see Table D.2).
70

Table D.1: Dependence of current purchase decisions on past purchases
1 week 4 weeks
Purchase? Purchase? Quantity Quantity Purchase? Purchase? Quantity Quantity
Past quantity
t−1 0.0019*** 0.0009*** 0.0736*** -0.0382*** 0.0015*** 0.0008*** 0.2346*** 0.0191
(0.0001) (0.0001) (0.0075) (0.0071) (0.0001) (0.0000) (0.0141) (0.0139)
t−2 0.0023*** 0.0012*** 0.1510*** 0.0363** 0.0010*** 0.0004*** 0.1626*** -0.0100
(0.0001) (0.0001) (0.0164) (0.0176) (0.0001) (0.000) (0.0093) (0.0122)
t−3 0.0018*** 0.0008*** 0.1113*** 0.0088 0.0007*** 0.0003*** 0.1187*** -0.0229*
(0.0001) (0.0000) (0.0084) (0.0069) (0.0000) (0.0000) (0.0074) (0.0108)
t−4 0.0018*** 0.0008*** 0.1120*** 0.0140* 0.0005*** 0.0002*** 0.0849*** -0.0338***
(0.0001) (0.0000) (0.0092) (0.0085) (0.0000) (0.0000) (0.0088) (0.0103)
t−5 0.0016*** 0.0006*** 0.1076*** 0.0143* 0.0004*** 0.0001** 0.0775*** -0.0375***
(0.0001) (0.0000) (0.0078) (0.0075) (0.0000) (0.0000) (0.0076) (0.0092)
t−6 0.0015*** 0.0005*** 0.0959*** 0.0057 0.0003*** 0.0000 0.0758*** -0.0367***
(0.0001) (0.0000) (0.0089) (0.0078) (0.0000) (0.0000) (0.0099) (0.0125)
t−7 0.0015*** 0.0004*** 0.1024*** 0.0073 0.0003*** 0.0000 0.0663*** -0.0462***
(0.0001) (0.0000) (0.0079) (0.0078) (0.0000) (0.0000) (0.0078) (0.0099)
t−8 0.0015*** 0.0005*** 0.0929*** 0.0003 0.0002*** -0.0000 0.0927*** -0.0342***
(0.0001) (0.0000) (0.0070) (0.0072) (0.0001) (0.0000) (0.0086) (0.0104)
Mean of dep. var. 0.1791 0.1791 21.5831 21.5831 0.3929 0.3929 39.3574 39.3574
Period effects? Yes Yes Yes Yes Yes Yes Yes Yes
Household fixed effects? No Yes No Yes No Yes No Yes
Notes: The dependent variable in columns "Purchase?" is a dummy variable equal to one if the household purchased
alcohol in the period. The dependent variable in columns "Quantity" is the number of standard drinks purchased per
adult in that period, conditional on making a non-zero purchase. The table shows the estimated coefficients on the
number of standard drinks purchased per adult in the preceding 8 periods. Standard errors are in parentheses. ***, **
and * indicate a significant effect at the 1%, 5% and 10% levels.
71

Table D.2: Dependence of current purchase decisions on steady-state inventory level
1 week 4 weeks
Purchase? Quantity Purchase? Quantity
Inventory 0.0003*** 0.0393*** 0.0007*** 0.1223***
(0.0000) (0.0039) (0.0000) (0.0094)
Mean of dep. var. 0.1791 21.5831 0.3929 39.3574
Period effects? Yes Yes Yes Yes
Household fixed effects? Yes Yes Yes Yes
Notes: The dependent variable in columns "Purchase?" is a dummy variable equal to one if the household purchased
alcohol in the period. The dependent variable in columns "Quantity" is the number of standard drinks purchased per
adult in that period, conditional on making a non-zero purchase. The table shows the estimated coefficients on a variable
for the household’s alcohol inventory. This is calculated by assuming that the household has a fixed level of consumption
(equal to its mean purchases per period). Standard errors are in parentheses. ***, ** and * indicate a significant effect
at the 1%, 5% and 10% levels.
72

E Calibration: details
E.1 Market models: details
E.1.1 Demand for quality: specification
Consistent with equation 4 in Section 3.1, household’shutility of purchasing productjat timetfor
consumption occasionoin alcohol marketais:
V ah jto =V ah jt +ε ah jto (E.1)
whereV ah jt denotes the deterministic component of the utility function. It is a function of product at-
tributes and households’ characteristics, The error termεah jto is specific to the household, the product,
and the (anticipated) consumption occasions. It captures the effect of unobserved variables such as
occasion-specific effects (e.g., the anticipation of a party), retailer promotions, variations in the
product positioning on shelves etc.
The deterministic component of utility is further specified as:
V ah jt =−α ahpa jt +β ahZa jt (E.2)
withα ah =α a +δ aDh +σ aζ a h , whereα a is the mean marginal disutility for the category andD h
is a vector of discrete demographic characteristics (ζ a is a category-specific vector of coefficients),
σ a represents the unobserved heterogeneity in the disutility of price andζ a h is a random term that
captures the unobserved taste of householdhfor alcohol categorya. We assume thatζ a h follows a
standard normal distribution.
Table A.7 shows that there is a huge difference between the average price of champagnes
(26e/L) and that of other sparkling wines (6e/L), while in the other alcohol categories, the av-
erage prices are more similar between the different subcategories. Hence, for the Sparkling Wine
category, we decided to further distinguish the average disutility of price between the two subcat-
egories by adding a term capturing the specific mean marginal disutility of the price for champaigns.
For sparkling wines, the disutility of the price is specified asα ah +δ Champagne, but we only use the
estimatedα ah in the calculation of the quality index.
We allow the product-specific household utilityβahZa jt to be a set of fixed-effects that capture the
average utility of specific product characteristics (having in mind that a product is a brand-retailer
pair) - see Table E.1: retailer fixed-effectsβ r(j) ; brand fixed-effectsβ b(j) ; alcohol-free fixed-effect
βAlc(j) ; sub-category fixed-effects interacted with demographic fixed-effectsβ c(j) ×D h where the
demographics are the household income category (DIncomeh: 4 classes), the age category of the main
shopper (DAgeh: 3 categories), and alcohol habit as measured by the average purchase volumes per
household member in 2013 (DHabith: 3 categories). The selection was made based on specification
testings by eliminating progressively sets of fixed-effects that were not significant.
73

Table E.1: Vector of fixed effects per alcohol market
Alcohol categoryaProduct-specific household utility:β ahZa jt
Cidersβ r(j) +β c(j) ×D Ageh +β b(j)
Beersβ r(j) +β b(j) ×β Alc(j)
Aperitifβ r(j) +β c(j) ×D Habith +β b(j) +β Alc(j)
Spiritsβ r(j) +β c(j) ×D Incomeh +β Alc(j)
Still winesβ r(j) +β c(j) ×D Incomeh
Sparkling Winesβ r(j) +β c(j) ×D Ageh +β b(j)
Notes:D Incomeh: low-, mid-low, mid-high, high-income household (Kantar
WorldPanel classification based on self-reported household income and in-
come composition);D Ageh: age of main shopper <35 years-old, 35-55 years-
old, 55+ years-old;D Habith: average household purchases in 2013 <1, 1-2,2+
standard drinks/adult/week.
Assuming thatε ah jto is independently and identically distributed like an extreme value type I
distribution, we can write the individual probability that householdhbuys productjof the alcohol
marketaat periodtfor any consumption occasion, conditional on some valueζ a h of the unobserved
household taste shifter:
da jt(ζh,D h) = exp(Vah jt ) 1+ ∑ Jat k=1 exp(Vah kt ) (E.3)
withJ a t denoting the set of alternatives from marketain periodt. Hence, the probability of purchas-
ing productjof the alcohol marketaat periodtis:
sah jt =
Z
ζ
da jt(ζ a h ,D h)dPζ (ζ a h )(E.4)
wheredP ζ is the standard gaussian distribution. The market share of productjof the alcohol market
aat periodtis:
sa jt =
Z
D
Z
ζ
da jt(ζ a h ,D h)dPζ (ζ a h )dPD(Dh)(E.5)
whereP D is the distribution of household demographic characteristics observed from the data.
E.1.2 Price endogeneity
In deriving the expression of householdh’s purchase probability E.3, we have assumed that the
explanatory variables, especially prices, are independent of the error disturbancesε ah jto. Although
we do not let prices vary across household-related characteristics such as their place of residence,
the assumption of price exogeneity may not hold if prices depend on time-varying product-specific
characteristics such as the display on shelves or the advertising efforts by firms.
74

In practice, we can split up the household error term in two components:
εah jto =ξ a jt +e ah jto (E.6)
wheree ah jto is a household-occasion specific taste shock varying across products and occasions and
over time, whileξ a jt captures the influence of time-varying product-specific characteristics. While
eah jto is not observed by the supply-side, the unobserved product characteristics captured inξa jt impact
household purchase decisions and they are likely related to the pricing policies of firms, making
prices endogenous.
To solve this endogeneity issue, we apply a two-stage residual inclusion approach as in Petrin
and Train (2010). We first regress the prices on a set of instrumental variablesW jt as well as the set
of product specific fixed-effects

βr(j) ,β b(j) ,β c(j) ,β Alc(j)

of the baseline utility function:
pa jt =ψ aW a jt +β r(j) +β b(j) +β c(j) +β Alc(j) +η a jt
The estimated error term bηa jt of the first stage is a proxy measure of the impact of unobserved time-
varying product characteristics on prices. We include this residual in the indirect utilityVah jt in order
to control for the impact of these unobserved product characteristics (second stage):
V ah jt =−α ahpa jt +β a jtZa jt +ρ a bηa jt
whereρ a will be the estimated parameter associated with the estimated error term of the first stage.
This approach also shows that we must choose instruments that induce significant variations in
prices, otherwise bηa jt could be collinear with prices andZ a jt. The choice of instruments is discussed
in the main text.
Table E.2 displays the estimation results of the instrumental equation (E.1.2) in which product
prices are instrumented on a set of instrumental variables (IVs) to construct the function controlling
for price endogeneity in the demand models. Various sets of IVs were tested (see the main text)
and we selected the variables that were significant to avoid weak IV issues. The F-test statistics
reported at the bottom of the table are above the recommended threshold of 10 (Stock et al. 2002).
The signs of the coefficients reflect various mechanisms, such as the market power of manufactur-
ers or retailers, or incentives for price differentiation. Typically, a manufacturer may increase its
prices if it offers many products (more market power), but will tend to set lower prices when other
manufacturers also propose many products (more competition).
75

Table E.2: Price Regressions
Ciders Beers Aperitifs Spirits Still wines Sparkling wines
Instrumental Variables (IV)
Taxes 1.226 (0.048)*** 1.744 (0.062)***
Nb of competing products1 0.005 (0.000)*** 0.105 (0.021)*** 0.129 (0.023)***
Nb of competing products -0.010 (0.003)*** -0.113 (0.021)*** -0.079 (0.021)*** -0.022 (0.012) *
offered by the other firms
Mean price of other products
Mean price of other products in
same retailer at other periods -7.9594 (1.332) -7.684 (1.514) *** *** -3.298 (0.777) ***
Mean price of same brand products
in other periods -9.930 (1.475) *** 0.685 (0.019) *** -6.210 (0.379) ***
Fixed Effects
Retailers Yes Yes Yes Yes Yes Yes
Sub-category Yes Yes Yes Yes Yes Yes
Brands Yes Yes Yes Yes No Yes
Brands x Alcohol free No Yes No No No No
Alcohol-free No No Yes Yes No No
F-test IV 53.37*** 28.24*** 216.71*** 275.15*** 660.28*** 106.06***
Adj.R 2 0.98 0.96 0.93 0.97 0.94 0.96
N 774 4,100 3,119 4,417 2,147 1,927
Notes: Standard errors in parentheses.∗p<0.10,∗ ∗p<0.05,∗ ∗ ∗p<0.01. Number of competing products defined as the number of other products within a given classification of alcoholic beverage, offered at the same
period by the manufacturer itself and by the other manufacturers. N: number of price-period observations.
76

E.1.3 Estimation
The model is maximized by applying a maximum simulated log-likelihood procedure, whereby
we sample the standard normal distribution by applying the sparse grid methodology of Heiss and
Winschel (2008). This approach allows approximating the likelihood function without suffering
from the dimensional problem of the large number of draws that are required to minimize the es-
timation error of the simulated likelihood function.
E.1.4 Demand for quality: elasticity formula
At the market level, the own- and cross-price elasticities of product market sharess a jt were derived
using the following formula:
∂s a jt
∂p a kt
pa kt
sa jt =



pa jt
sa jt
Z
D
Z
ζ
αahdah jt (1−d ah jt )dPζ (ζ a h )dPD(Dh)ifj=k
pa kt
sa jt
Z
D
Z
ζ
αahdah jt dah kt dPζ (ζ a h )dPD(Dh)otherwise (E.7)
Household-specific level price elasticities can also be easily calculated, as well as elasticities by
population subgroups or by product subcategories. Table E.3 reports such elasticities.
77

Table E.3: Average estimated own-price elasticities by sub-category
Ciders Beers Aperitifs Spirits Still wines Sparkling wines
By sub-category Sweet Alcohol-free Cocktails and Punch Rum de Table Champagne
-3.59 (0.84) -4.74 (1.73) -2.93 (1.52) -3.45 (0.23) -5.64 (3.61) -2.78 (1.14)
Raw Bock and premium Liquor wines Whisky de Pays Other sparkling wines
-3.48 (0.90) -5.29 (1.68) -4.55 (0.73) -3.68 (0.17) -6.60 (2.43) -2.73 (1.26)
Special Natural sweet wines Aniseed d’Appellation
-5.44 (2.08) -3.05 (0.78) -2.89 (1.05) -4.95 (1.82)
Amer, gentiane and vermouth Liquors
-3.46 (1.33) -3.18 (0.51)
Other aperitifs Other spirits
-2.96 (1.58) -3.56 (0.20)
By category -3.40 (0.84) -5.02 (1.60) -3.04 (1.20) -3.55 (0.20) -4.43 (2.15) -2.71 (1.09)
Notes: in parenthesis, the standard deviation of estimated elasticities across periods and products in the same subcategory or category.
78

E.2 Demand for quantity
E.2.1 Specification
The demand for quantity model is estimated on pseudo-panel data that are constructed by aggreg-
ating data at the level of sociodemographic clusters indexed byc. The demand functions are de-
rived from a Quadratic Almost Ideal Demand System (QUAIDS). The budget sharew ac t on alco-
hol categoryafor clustercat periodtvaries with log total expenditure lnY c t =ln  ∑A a=1Y ac t  =
ln

∑A a=1 Pac t Qac t  and the vector of log price indices, lnP c t = (lnP1c t , ...,lnPAc t )′, according to the
following econometric specification:
wac t = Y ac t Y ct =κ ac +γ a′ lnP c t +χ a(lnY c t −G 1(lnP c t ,θ)) +λa (lnY c t −G 1(lnP c t ,θ)) 2 G2(lnP ct ,θ) +ν ac t (E.8)
with the following non-linear price aggregators
G1(lnP c t ,Θ Q) =κc 0 +κ c′ lnP c t + 1 2 lnP c′ t ΓlnP c t
G2(lnP c t ,Θ Q) =exp(χ′ lnP c t )
whereκ c = (κ1c, ...,κAc)′,χ= (χ 1, ...,χA)′,Γ= (γ 1, ...,γA)′,Θ Q is the set of all parameters, and
νac t is an error term. The parameterκ c 0 in the price aggregator is unidentified and can be set to 0
or to any other fixed value. The heterogeneity of households in clusters enters the demand system
through theκ ac’s, which are modelled as linear combinations of the sociodemographic variablesDc
observed in the data (including a constant):
κac =K a′Dct (E.9)
E.2.2 Construction of the price indices
Consider first a householdhthat purchases a positive quantity in categorya. Following equation
(7), the price index is: for each categorya:
Pah t = Y ah t Qaht (1+b aht (pat )) (E.10)
Total expenditureY ah t will be constructed by deflating observed expenditure by the monthly CPI.
The quantityQ ah t will be the observed alcohol intake ofa.
The quality-adjustment term(1+b ah t (pa t ))is less straightforward to compute, because its for-
mula includes the marginal utility of expenditureα ah (cf. Equation C.3):
bah t (pa t ) =
ln

∑
j∈Jat
exp(Vah jt −V ah ⋆t )
!
+α ah ∑
j∈Jat
πah jt

pa jt −p a ⋆t

αah (E.11)
79

whereπ ah jt is the conditional purchase probability:
πah jt =d a jt(ζ ah,D h)/(1−d a 0t(ζ ah,D h)) = exp(Vah jt ) ∑ Jat k=1 exp(Vah kt ) (E.12)
V ah ⋆t and pricep a ⋆t are ‘reference’ purchase utility and prices that we specify as the weighted average
of purchase utilitiesV ah jt and pricesp a jt with weights equal to the conditional purchase probabilities
πah jt .
V ah ⋆t = ∑
j
πah jt V ah jt (E.13)
pa ⋆t = ∑
j
Eh(πah jt )pa jt (E.14)
In Step 1’s random utility model, the marginal utility of expenditure is specified as a random
variable:α ah =α a +δ aDh +σ aζ a h , whereα a is the average marginal utility of expenditure in
categoryaandζ a h is the household-specific taste shock. As the latter is not observed, we cannot
directly computeb ah t (pa t ). However, we can calculate its expectation conditional on all available
information on household preferencesΩ ah t . This information includes, in particular, its observed
choices in the period. Hence, we apply Bayes rule to compute:
Bah t =E h bah t (pa t )

Ωah t i = Z ζ bah t (pa t )dPζ|Ωaht (ζh)(E.15)
where the conditional distributionP(ζ|Ω)is derived using the Bayes rule. This conditional expect-
ation is calculated by integrating out over the simulated distribution ofζ a h using Halton draws and
the sameζ a h for all purchase acts of the same household.
The price index is finally constructed as:
Pah t = Y ah t Qaht (1+B aht ) (E.16)
E.2.3 Construction of the pseudo-panel
The model estimation uses sample S3 (see definition in Section A.1), as it maximizes the number
of households that we can aggregate to form the clusters. This leaves us with 120 clusters observed
over 26 time periods (13 periods in 2014), 3120 observations (cluster-periods), half of them being
used for estimating the demand in 2014. Table E.4 reports the median, minimum and maximum
numbers of households and purchases aggregated in each cluster, and by year and period for pur-
chases.
For each alcohol categorya, using the QUAIDS specification for budget shares (E.8), we estim-
ate a demand function:
Qac t (P1c t , ...,PAc t ,Y c t ,D c;Θ Q)(E.17)
80

Table E.4: Characteristics of clusters
Median Min Max
Number of households per clusters 212 3 1389
Number of purchases per clusters
Over the year 8,105 28 38,079
Minimum in a period 243 1 1,262
Maximum in a period 431 8 1,753
Notes: All statistics are computed overN=120 clusters.
The first line reports statistics on the median, minimum and
maximum number of households in clusters. The second
line reports the median, minimum and maximum number
of purchases observed in each cluster over a year. The
third and fourth lines reports the same statistics for the min-
imum number of purchases and the maximum number of
purchases that can be observed in a period for each cluster.
whereD c is a vector of average characteristics of households in clusterc,Y c t is the average alcohol
expenditure,Θ Q is the vector of parameters to be estimated, and the price indices represent average
expenditures for one unit of utility expressed in money-metric as in E.16.
We apply the following formula for computing these variables:
Y c t =
A
∑
a=1
Y ac t (E.18)
Y ac t = ∑
h∈c∩S3
ωS3 ht
∑h∈c ωS3 ht Y ah t (E.19)
Dc = ∑
h∈c∩S3
ωS3 ht
∑h∈c ωS3 ht Dh (E.20)
Pac t = Y ac t
∑
h∈c∩S3
ωS3 ht
∑h∈c∩S3 ωS3 ht Qah t (1+B ah t )
(E.21)
Qac t = Y ac t Pact (E.22)
whereω S3 ht is the number of French households represented by householdh(see the weight normal-
ization in Section A.1.2).
In our preferred specification, we include as socio-demographic shiftersD ct the proportion of
81

households in each modality of the variables used in the clustering, period dummies, as well as
the proportion of households living in the 8 administrative regions (ZEAT) defined by INSEE (the
French National Statistics Office) and in town with less than 20,000 inhabitants. These variables will
thus control (adjust) for a variety of effects: position in the life-cycle, income, household structure
and spatial variations in tastes such as rural/urban differences. We also control for seasonality effects
through the inclusion of period fixed-effects.
E.2.4 Demand for quantity: elasticity formula
After having estimated the demand system, we derive the budget and price elasticities. Letaandk
denote two alcohol categories, differentiating (E.8) with respect toY c t andP ac t yields, respectively:
µac =χ a +2λ a (lnY c t −G 1(lnP c t ,Θ Q)) G2(lnP ct ,Θ Q) ,
µack =γ ak −µ a(αak +γ k′ lnP c t )−λ aχa′ (lnY c t −G 1(lnP c t ,Θ Q))2 b(lnP ct ,Θ Q)
Budget elasticities are then given by:
Elas c a =µ a/wac +1 (E.23)
Uncompensated price elasticities for theadjustedquantitiesQare:
Elas uc ak =µ ak/wac −δ ak (E.24)
whereδ ak is the Kronecker delta andw ac is the budget share for clusterc. Compensated price
elasticities are given by:
Elas c ak =Elas uc ak +Elas c awkc (E.25)
.
The elasticities reported in the main text are computed setting all variables to their average
sample value.
E.3 Impacts on consumer welfare
We use equivalent variations to estimate the impact of counterfactual price policies on consumer
welfare. Importantly, we are able to account for consumer adjustments in quality and quantity, as
the quality-adjusted prices take into account changes in market prices and consumers’ substitutions
between products within a market.
Equivalent variation (EV) is the adjustment in income requiredbeforethe change has occurred
to reach the final level of utility (i.e., the level that would occur if the change happened) at the
original prices. It must satisfy the following equalities:
V 1 =V(P 0,Y 0 +EV) =V(P 1,Y 1)
82

whereV 1 is the utility levels of the household after the policy, andP 0 andP 1 are two levels of
quality-adjusted prices.
Then, EV is given by
c(P0,V(P 0,Y 0 +EV)) =c(P 0,V 1)
Y 0 +EV=c(P 0,V 1)
EV=c(P 0,V 1)−c(P 0,V 0)
EV can be decomposed as
EV=

c(P1,V 1)−c(P 0,V 0)  +  c(P0,V 1)−c(P 1,V 1) 
=YV+EV ∗
whereYVis the variation in expenditure, andEV ∗ computed as follows. SinceY 1 =P 1Q1 =
c(P1,V 1)
• useP 1 andY 1 =c(P 1,V 1)to compute the indirect utility in 1,V 1, using the formula
lnV 1 =
(lnY 1 −lna(lnP 1,θ)
b(lnP 1,θ)
−1
+c(lnP 1,θ)
)−1
• and useP 0 andV 1 to compute the costc(P 0,V 1) =eY 0, using the reverse formula
ln eY 0 =lna(lnP 0,θ) +b(lnP0,θ)
 lnV 1
1−c(lnP 0,θ)lnV 1

83

F Simulation: details
The simulations are based on the estimated marginal costs from the supply model as well as on the
other estimated structural demand parameters. We first show how we use the supply-side model to
simulate the impact of new price regulations on market equilibrium outcomes.
F.1 Step 1: Markets simulations
When a reform of price regulations is implemented, the producer faces new constraints taking the
form of either a change in alcohol-specific excise taxes levied at the producer level or a minimum
unit price policy.
For a change in excise tax fromT 0 toT 1, the new vector of equilibrium pricesp 1 t is the solution
of the following system of equations derived from first-order conditions (12) and (13) for each
separate marketa(we omit this superscript):
∑k∈G f
 p1 kt
1+τ − bCkt −T 1 k
 ∂s kt(p1 t )
∂p 1 j +s jt(p1 t )+ ∑k∈eSr
 p1 kt
1+τ − bCkt −T 1 k
 ∂s kt(p1 t )
∂p 1 jt =0,∀j∈G f r,∀f,∀r
∑k∈eSr
 p1 kt
1+τ − bCkt −T 1 k
 ∂s kt(p1 t )
∂p 1 jt +s jt(p1 t ) =0,∀j∈ eSr,∀r.
This system of first-order conditions can be rewritten compactly with matrix notation, and can
be inverted such that the vector of new equilibrium marginsm 1 (with elementsm 1 kt equal to p1 kt 1+τ −
bCkt −T 1 k ) can be expressed as a functionMof the demand parameters and the new equilibrium
pricesp 1:
m1 =M  p1 (F.1)
By construction, this vector of new equilibrium prices must satisfy the following condition:
p1 −m 1 = bC+T 1 (F.2)
This suggests finding the equilibrium prices that minimize the following criterion:
p1 =argmin p
p−M(p)− bC−T 1  (F.3)
where ∥.∥ is the Euclidean norm. In practice, we can implement an iterative algorithm, whereby at
each iterationsand for a vector of pricesp(s), we have:
p(s+1) =M(p(s))− bC−T 1 (F.4)
The algorithm will be initialized withp 0 equal to the actual prices, which means that the focus is on
the fixed-point solutionp(∞)that is consistent with the initial market situation.
84

The pass-through of the tax onto consumer prices will be computed as the ratio of the price
difference on the cost difference:
PTjt =
p1 jt −p 0 jt
C1 jt −C 0 jt (F.5)
Finally, variations in profits will be calculated for each firm, notably allowing us to distinguish
the economic impact by size of manufacturers and by alcohol category.
Simulating a new market equilibrium after a Minimum Unit Price policy
Letp 1 be the vector of minimum prices imposed by a MUP policy, andPthe set of prices that
meet the MUP constraint. For this policy, the new equilibrium prices will be estimated by solving
the following program:
p1 =argmin p∈P
p−M(p)− bC−T 1  (F.6)
We will use a modified version of the iterative algorithm F.4:
∀j,p j(s+1) =max
n
p j;M j (p(s))− bCj −T 1 j
o
(F.7)
F.2 Step 2: Simulating changes in household purchases of pure alcohol
Denoter=0,1 the superscript indicating whether a variableXis constructed using the actual or
new price vector, and∆X= (X 1 −X 0)/X 0 therelativevariation inXgenerated by the change from
actual to new prices.
The relative variation in total alcohol (ethanol) purchasesE h by householdhis a weighted sum
of category-specific variations∆E ah:
∆Eh = ∑
a
∆Eah ∗ Eah0
∑k Ekh0 (F.8)
(F.9)
The impact of the price change on∆E ah, is a combination of a quantity effect and a “quality”
effect, as shown in the following formula:
∆Eah =∆Q ah(1+∆Ψ ah) +∆Ψah (F.10)
where∆Q ah and∆Ψ ah are therelativevariations in, respectively, the aggregatedphysicalquantity
(in Liter) and the average alcohol-content of purchases in categoryaby householdh.
We assume that households who did not purchase any variety in a category throughout 2014
will continue not to purchase in this category regardless of the price level: households who did not
consume before the policy will not consume after the policy, so that for them we have∆E ah =0.
For the other households, the relative variation in quantity is bounded as follows:
∆Qah =Max
Qah1 −Q ah0
Qah0 ;−1

(F.11)
85

Simulation Step 1 provides us withp ar, the vector of new market prices. The aggregate price
index for categoryaand householdhcan be expressed as the average of variety prices,p ar j (∀j∈J a),
weighted by the corresponding conditional purchase probabilities,π ahr j (par)(the probability thath
purchasesjinaconditional on purchasing any product ina). Formally
Pahr = 1 (1+B ahr) ∑ j∈Ja πahr j ∑k∈Ja πahr k pr j (F.12)
where we replace the average unit valueY ah t /Qah t in formula (7) by the weighted average of product
prices atr, and we replaceb ah(par)byB ahr, the expected quality obtained by householdhfrom a
purchase occasion in categoryawith products priced atp ar.B ahr andπ ahr j are calculated by integ-
rating over the simulated distribution of unobserved preferences, as we did previously to evaluate
equation (E.15).
The transmission of the changes in variety price to the aggregated price indices is then measured
by∆P h = (∆P1h, ...,∆PAh), and its impact on the quantity index for categorya, householdh, by
∆Qah =Elas ac(h) P ×∆Ph +Elas ac(h) Y ×(Elas c(h) PY ×∆P h)(F.13)
wherec(h)is the cluster to whichhbelongs,Elas ac(h) P is the vector of uncompensated direct and
cross-price elasticities for alcohol categorya, calculated according to formula (E.24),Elas c(h) PY is the
elasticity vector of total expenditures to price variations on total expenditures, as estimated in the
first-stage instrumental equation of total expenditure for the QUAIDS, andElas ac(h) Y is the budget
elasticity ofa.
Finally, knowingQ ah0 =Q ah0(1+B ah0)and∆Q ah, we will calculateQ ah1 = (1+∆Qah)Qah0.
This will giveQah1 =Q ah1/(1+B ah1), as well as variety quantitiesqah1 j , sinceq ahr j =π ahr j (par)Qahr.
In addition to the relative variation in aggregate quantity ofa, the change in the price of product
varieties may induce substitutions between varieties, which may also alter the average alcohol-
content of the purchases in that category. Letψ a j be the alcohol-content of varietyj(in grams per
liter) in groupa, then the relative variation in the household-specific average alcohol-content of
purchases in categoryjcan be written as:
∆Ψah = ∑
j∈Ja
ψa j ∆πah j (F.14)
Having calculated∆Ψ ah and∆Ψ ah, we will have the outcome of interest,∆Eah, the relative variation
in alcohol purchase from categorya(equation F.10).
86

G Additional results & sensitivity analysis
G.1 Prices in the QUAIDS model: sensitivity analysis
Table G.1 below presents the results of the estimation of the QUAIDS model for two alternative
specifications (2 and 3). These results are commented in the main text. To save space, we do not
report the cross-price elasticities.
Table G.1: Average budget and own-price elasticities: sensitivity analysis
Specification 1 Specification 2 Specification 3
Baseline +income/habit-period FE Laspeyres price indices
Budget
Ciders 0.503 (0.302)* 0.894 (0.308)*** 1.145 (0.044)***
Beers 1.210 (0.112)*** 1.131 (0.108)*** 0.951 (0.016)***
Aperitifs 1.017 (0.154)*** 0.943 (0.152)*** 1.011 (0.023)***
Spirits 1.434 (0.083)*** 1.480 (0.081)*** 0.976 (0.013)***
Still wines 0.349 (0.126)*** 0.352 (0.125)*** 1.134 (0.021)***
Sparkling wines 0.385 (0.187)** 0.387 (0.182)** 0.943 (0.035)***
Uncompensated own-price
Ciders -0.504 (0.085)*** -0.524 (0.085)*** -0.639 (0.024)***
Beers -0.828 (0.047)*** -0.758 (0.045)*** -0.742 (0.012)***
Aperitifs -0.531 (0.045)*** -0.533 (0.04)*** -0.686 (0.015)***
Spirits -0.881 (0.030)*** -0.888 (0.030)*** -0.818 (0.010)***
Still wines -0.396 (0.046)*** -0.389 (0.046)*** -0.747 (0.013)***
Sparkling wines -0.161 (0.033)*** -0.159 (0.032)*** -0.686 (0.014)***
Notes: Kantar Worldpanel 2013-2014; average elasticities where each cluster observation is weighted by the proportion of French households
represented by the cluster; standard errors in parentheses; ***,** and * significant at the 1%. 5% and 10% level; the first six lines display budget
elasticities. i.e. the % change in the quantity for a given alcohol category when total alcohol expenditures increase by 1%; the last six lines display
the % change in the quantity for each alcohol category when their own price increases by 1%; Specification 1 is our preferred specification used for
producing the main results. Specifications 2 adds to specification 1 interactions between time fixed effects and income categories and interactions
between time fixed effects and alcohol habit categories; In specification 3 we replace the quality-adjusted price indices by cluster-specific Laspeyres
indices.
G.2 Key simulation results under QUAIDS estimates obtained with Laspeyres
price indices
87

Table G.2: Key simulation results: sensitivity analysis
Prices in QUAIDS: Quality-adjusted prices Laspeyres price indices
Impacts onPure alcohol Purchase volume Pure alcohol Purchase volume
Low uniform tax +14.0% +1.7% +4.2% -4.5%
High uniform tax -5.9% -9.3% -19.0% -22.2%
Low progressive tax +6.8% +1.3% +2.2% -2.3%
High progressive tax -10.3% -6.8% -18.8% -15.9%
Minimum Unit Price -15.0% -13.5% -23.1% -22.0%
MUP + Low prog. Tax -14.7% -13.9% -26.1% -25.6%
Notes: Policy simulation results when the QUAIDS is estimated with quality-adjusted prices and when it is estimated
with Laspeyres price indices computed using cluster-specific average market shares and product prices.
G.3 Additional results for still wines by quality segment
Table G.3: Impacts of Minimum Price on the market for still wines
Price (e/L) Volume (L/hhold)
Baseline Variation Baseline Variation
e/L (% of baseline) L/hhold (% of baseline)
Supply-side reaction Without With Without With
Segmentation by quality label
Table 2.1 +132.6 +136.0 8.9 -95.5 -96.2
Pays 2.7 +80.4 +82.2 12.3 -87.6 -89.0
Appellation 4.8 +8.3 +10.6 16.3 +69.7 +65.4
Segmentation by initial price
≤3e/L 2.3 +107.8 +108.0 19.3 -94.1 -94.6
∈]3;5]e/L 4.1 +19.1 + 20.3 9.6 -4.5 -11.3
≥5e/L 5.3 +0.8 +3.3 8.6 +124.4 +122.4
Notes: Impacts of minimum price policy on unit prices and volumes purchased by households - sample average.
G.4 MUP: decomposition of variations in tax revenues and firms profits
LetQ a be the size of marketa,s j the market share of productj, and(p j −c j), the unit margin, then
the relative variation in profit can be approximately decomposed as (taking the log):
∆Π j
Π j ≈ ∆Qa Qa |{z}
Quantity
+ ∆s j
s j|{z}
Quality
+ ∆p j
p j −c j| {z }
Price
88

Table G.4: MUP impacts on tax revenues and profits
Ciders Beers Aperitifs Spirits Still wines Sparkling wines Total
Tax revenues
Total +3.2% -6.8% -3.2% -7.6% +15.8% +2.0% -2.3%
Alcohol taxes +3.0% -12.5% -8.2% -9.9% -22.9% -3.8% -10.3%
V AT +3.2% -1.2% +2.5% -0.4% +18.2% +2.3% +7.0%
Profits
Total +3.4% +1.1% +3.4% +6.9% +2.3% +1.8% +3.7%
Quantity +3.0% -10.6% -9.0% -8.5% -30.4% -4.3% -14.1%
Quality -0.0% -15.1% -8.6% -5.8% -139.7% +1.3% -43.6%
Price +0.5% +26.8% +21.1% +21.2% +172.5% +4.8% +61.5%
Small firms
Total +3.4% +7.6% +6.7% +5.8% +39.3% +2.7% +24.5%
Quantity +3.0% -11.3% -9.3% -8.4% -41.4% -4.3% -26.6%
Quality +0.4% +6.0% +5.0% -2.2% -44.4% +5.8% -24.1%
Price -0.0% +12.9% +11.0% +16.4% +125.2% +1.2% +75.3%
Large firms
Total +3.4% +1.0% +2.5% +7.0% -38.7% +1.3% -3.5%
Quantity +3.0% -10.6% -9.0% -8.5% -18.2% -4.3% -9.8%
Quality -0.1% -15.7% -12.6% -6.1% -245.5% -1.2% -50.4%
Price +0.5% +27.2% +24.0% +21.6% +225.0% +6.7% +56.7%
Notes: % pts impacts of minimum price policy on tax revenues and firms profits. The latter are defined as the total marginal profits made by
manufacturers and retailers on a product. Large firms correspond to national brands produced by large manufacturers and to products under private
labels. Small firms correspond to the aggregate of small manufacturers. For each alcohol market, the quantity effects relate to the variation in the size
of the market, the quality effects to the reshuffling of market shares, and the price effect to the change in product specific-margins.
References
Dubois, Pierre, Rachel Griffith and Martin O’Connell (2022). ‘The Use of Scanner Data for Eco-
nomics Research’. In:Annual Review of Economics14.V olume 14, 2022, pp. 723–745.DOI:
10.1146/annurev-economics-051520-024949.
Griffith, Rachel, Martin O’Connell and Kate Smith (2020). ‘Price floors and externality correction’.
In:Insitute for Fiscal Studies Working Paper20/37.
Heiss, Florian and Viktor Winschel (2008). ‘Likelihood approximation by numerical integration on
sparse grids’. In:Journal of Econometrics144.1, pp. 62–80.DOI:10.1016/j.jeconom.2007.
12.004.
Hendel, Igal and Aviv Nevo (2006a). ‘Measuring the Implications of Sales and Consumer Inventory
Behavior’. In:Econometrica74.6, pp. 1637–1673.DOI:10 . 1111 / j . 1468 - 0262 . 2006 .
00721.x.
— (2006b). ‘Sales and consumer inventory’. In:The RAND Journal of Economics37.3, pp. 543–
561.DOI:10.1111/j.1756-2171.2006.tb00030.x.
Kopp, Pierre (2015).Le coût social des drogues en France. Observatoire Français des Drogues et
des Toxicomanies, p. 75.
89

Lecocq, Sébastien et al. (2023). ‘Alcohol Price Regulation in France: Choosing a Reform Scenario
to Achieve Public Health and Tax Fairness Objectives’. In:Economie et Statistique541.1,
pp. 17–33.DOI:10.24187/ecostat.2023.541.2105.
Petrin, Amil and Kenneth Train (2010). ‘A Control Function Approach to Endogeneity in Consumer
Choice Models’. In:Journal of Marketing Research47.1, pp. 3–13.DOI:10.1509/jmkr.47.
1.3.
Ruhm, Christopher J. et al. (2012). ‘What U.S. data should be used to measure the price elasticity
of demand for alcohol?’ In:Journal of Health Economics31.6, pp. 851–862.DOI:https :
//doi.org/10.1016/j.jhealeco.2012.08.002.
Stock, James H, Jonathan H Wright and Motohiro Yogo (2002). ‘A Survey of Weak Instruments and
Weak Identification in Generalized Method of Moments’. In:Journal of Business & Economic
Statistics20.4, pp. 518–529.DOI:10.1198/073500102288618658.
Zhen, Chen et al. (2009). ‘Understanding differences in self-reported expenditures between house-
hold scanner data and diary survey data: a comparison of Homescan and consumer expenditure
survey’. In:Review of Agricultural Economics31.3, pp. 470–492.
90
