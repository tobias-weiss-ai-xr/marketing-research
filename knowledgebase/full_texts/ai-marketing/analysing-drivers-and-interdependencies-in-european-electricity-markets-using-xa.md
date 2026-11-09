---
title: Analysing drivers and interdependencies in European electricity markets using XAI
url: https://arxiv.org/abs/2606.19118
category: ai-marketing
subcategory: empirical
date: 2026-06
venue: ''
authors:
- Antoine Pesenti
- Aidan O'Sullivan
source: arxiv
pdf_url: https://arxiv.org/pdf/2606.19118
pages: 12
chars: 58219
fetched_at: '2026-11-08T13:01:59+00:00'
kb_version: 1
---

# Analysing drivers and interdependencies in European electricity markets using XAI

Highlights
Analysing drivers and interdependencies in European electricity markets using XAI
Antoine Pesenti, Aidan O’Sullivan
•39 European electricity markets are analysed with
XAI methods applied to their DNN models
•An EU-wide electricity market is set to explore the
scenario "What if there was a common price in the
European market"
•While solar power contributes the least to overall
electricity generation, it already plays the most im-
portant role in setting electricity prices
•Poland is extreme with 72% of fossil fuel generation
and instead solar, followed by wind, being the most
important sources to explain price movements
•Neighbours are very influential in setting domestic
prices. 6 out of the 11 neighbours of Germany have
the German features as their dominant super-feature
•New SSHAP explainable method is used to address
the SHAP method drawbacks to deal with high-
dimensional models
arXiv:2606.19118v1  [cs.AI]  17 Jun 2026

Analysing drivers and interdependencies in European electricity markets using XAI
Antoine Pesenti∗, Aidan O’Sullivan
UCL Energy Institute, University College London, UK
Abstract
Electricity markets are inherently complex systems characterised by strong nonlinearities, high-dimensional interactions,
and increasing interdependence across regions. While deep neural networks (DNNs) have demonstrated strong predictive
capabilities for electricity prices, their lack of interpretability limits their usefulness for understanding the underlying
drivers of price formation.
This paper addresses this gap by combining DNN models with explainable artificial intelligence (XAI) techniques to
analyse the determinants of electricity prices across 39 European bidding zones. We employ SHAP (SHapley Additive
exPlanations) to quantify feature contributions and apply and extend SSHAP, an aggregation framework to improve
interpretability in high-dimensional settings.
The analysis identifies that renewable energy sources, particularly solar, play a disproportionately important role in
price formation despite their lower share in total power generation. Gas prices remain a dominant and consistent driver
across electricity markets, while interconnections significantly shape price dynamics, highlighting the strong interdepen-
dence of European electricity systems. In addition, a synthetic EU-wide electricity market is constructed to explore the
counterfactual scenario of a fully integrated market with a single price.
Keywords:Electricity price forecasting, EPF, Explainable methods, XAI, SHAP, SSHAP, ENTSO-E
1. Introduction
The European power grid is the largest grid by con-
nected power in the world [1], connecting 36 countries and
managed by 40 TSOs1.ENTSO-E, the European Network
of Transmission System Operators for Electricity, is the as-
sociation of the European transmission system operators
(TSOs). The 40 TSO members are responsible for the se-
cure and coordinated operation of Europe’s electricity sys-
tem. This paper considers 27 of these countries covering
39 bidding zones with total generation of 2.7 PWh in 2025,
or 8.5% of the 32 PWh 2025 world electricity generation
[2].
Electricity price formation in such an interconnected
system is inherently complex. Prices emerge from the
interaction of multiple factors, including demand, power
generation mix, fuel costs, and cross-border exchanges, all
of which evolve dynamically over time and space. The in-
creasing penetration of variable renewable energy sources,
suchaswindandsolar, furtheramplifiesthiscomplexityby
introducing significant variability and uncertainty into the
system. As a result, traditional linear or low-dimensional
modelling approaches often struggle to capture the nonlin-
ear relationships and high-dimensional dependencies that
characterise modern electricity markets.
∗Corresponding author: antoine.pesenti.21@ucl.ac.uk
1Each country has one TSO except Germany with five TSOs
In recent years, machine learning techniques, and in
particular deep neural networks (DNNs), have demon-
strated strong performance in modelling electricity prices
due to their ability to learn complex patterns from large
datasets. However, their black-box nature limits their
usefulness for economic interpretation and policy analy-
sis. While these models can provide accurate predictions,
they offer limited insight into the underlying drivers of
price dynamics, which is a critical requirement for market
participants, regulators, and system operators seeking to
understand and manage increasingly complex electricity
systems.
To address this challenge, this paper adopts an explain-
able artificial intelligence (XAI) approach to analyse elec-
tricity price formation across European electricity mar-
kets. By combining DNN models with SHAP-based ex-
plainability methods and reintroducing the SSHAP frame-
work [3], we aim to uncover the key drivers of price dynam-
icswhilemaintainingthemodellingpowerofdeeplearning.
In addition, we construct a synthetic EU-wide electricity
market as a counterfactual scenario to explore how prices
would behave under a fully integrated system with a single
clearing price. This approach provides new insights into
the degree of interdependence between markets and the
role of interconnections in shaping electricity price forma-
tion.
The main contributions of this paper are as follows:
•We analyse and compare 39 European electricity

markets and create an EU electricity market to ex-
plore "What if there was a common price in the Eu-
ropean market"
•We identify the most important factors driving these
electricity markets from two directions, their power
generation mix and their interconnected neighbours
•We use the SSHAP explanation method to deal with
high-dimensional models
The remainder of the paper is organised as follows. Section
2 reviews the relevant literature on electricity price fore-
casting and the explanations of the electricity markets.
Section 3 describes the dataset with some exploratory
analysis. Section 4 presents the models and the method-
ologies used in our research. Section 5 shows the results
and Section 6 discusses them. Finally Section 7 concludes
with key findings and directions for future research.
2. Literature review
Electricity Price Forecasting (EPF) is a critical re-
searchareawithintheenergysector, drivenbytheinherent
complexity, volatility, and deregulated nature of electricity
markets [4, 5]. Traditional econometric models, often re-
ferred to as white-box models, have been extensively used
to predict and explain electricity prices by leveraging fun-
damental market variables such as supply, demand, fuel
prices, and weather conditions [6, 7].
A substantial body of literature documents the price-
suppressing effect of renewable generation across multiple
markets, including Germany [8], Australia [9], the United
States [10], Turkey [11], New Zealand [12] and Canada
[13]. White-box models have the advantage of providing
direct explanations from their models, without interme-
diary methods. However while these models offer direct
interpretability, they often struggle to capture the nonlin-
earities and high-dimensional interactions characteristic of
electricity markets [14, 15, 16].
For example [13] uses Ordinary Least Square regres-
sion models on an Ontario dataset and from the negative
factors for the renewable sources derives that adding more
solar and wind generation brings electricity prices down.
However the R-Squared values are below 20%, highlighting
that linear models do not adequately capture the complex-
ity of electricity systems like electricity. [17] highlights the
importance of natural gas in setting the electricity price
in Europe by using a regression analysis based on the
relationship between marginal electricity generation and
prices, however the R-Squared is low again.
The advent of machine learning has provided new av-
enues to address the limitations of traditional forecasting
approaches. DNNs, in particular, have shown promise in
modelling complex dependencies and interactions in high-
dimensional data, leading to superior predictive accuracy
compared to econometric methods and simpler machine
learning models [18, 19]. However, the black-box nature
of DNNs poses significant challenges in terms of inter-
pretability, raising concerns about trust and transparency
in decision-making processes [20].
To bridge this interpretability gap, XAI techniques
have gained prominence in recent years. XAI aims to pro-
vide understandable and interpretable explanations for AI
model decisions and predictions, thereby enhancing trans-
parency, trustworthiness, and accountability [21, 22, 23].
Methods such as SHAP (SHapley Additive exPlanations)
and LIME (Local Interpretable Model-agnostic Explana-
tions) have been widely adopted to quantify the contri-
bution of individual features to specific outcomes across
various sectors, including energy [24, 25].
Despite the growing interest in XAI, there is a paucity
of research applying these techniques to EPF models. Two
notable studies [26, 27] utilise density and local fit princi-
ples with explanation methods such as Permutation Fea-
ture Importance [28, 29] and SHAP to establish a trust
score for each forecast, thereby improving prediction accu-
racy. However, these studies primarily use SHAP as inter-
mediary variables in stacking models rather than for pro-
viding explanations of electricity market dynamics, which
is the focus of our research.
Anotherrelevantstudy[30]employsagradient-boosted
tree model on the German electricity market using twelve
variables, including five power system features, their
ramps, and fuel prices. The limited number of variables
allows the authors to use SHAP interaction values [31]
to analyse interactions among important variables.Three
studies [32, 33, 3] utilise extensions of the open-source
datasets and models developed in [34] and the SHAP
method to explain the electricity market behaviours.
This paper extends the existing literature by focusing
on providing deeper insights into multiple connected elec-
tricity markets (the European electricity markets), with
explanation features based on the power generation mix
and interconnected neighbours rather than lagged prices
for example.
3. Exploratory data analysis
3.1. ENTSO-E
Almost all the data but gas prices comes from the
ENTSO-E Transparency Platform2. The gas price is the
closing European benchmark TTF gas price, downloaded
from yahoo finance Python API. ENTSO-E plays a cru-
cialroleinthecoordination, reliability, anddevelopmentof
Europe’s electricity transmission infrastructure. Its Trans-
parency Platform is a publicly accessible database that
provides real-time and historical data on electricity gen-
eration, load, prices, and cross-border flows. ENTSO-E
represents 36 European countries, of which we selected 27
2The Dutch solar power generation data from ENTSO-E, being
underreported, was replaced using data from the Dutch National
Energy Dashboard at https://ned.nl/
2

for having enough data for our research, which represent
39 bidding zones. Four countries have multiple bidding
zones : Italy (6), Norway (5), Sweden (4) and Denmark
(2) and two countries, Germany and Luxembourg, joined
to form one bidding zone.
The list of selected countries with the codes of
their bidding zones in brackets are: Austria (AT), Bel-
gium (BE), Bulgaria (BG), Switzerland (CH), Czechia
(CZ), Germany and Luxembourg (DE_LU), Denmark
(DK_1, DK_2), Estonia (EE), Spain (ES), Finland (FI),
France (FR), Greece (GR), Croatia (HR), Hungary (HU),
Italy (IT_CNOR, IT_CSUD, IT_NORD, IT_SARD,
IT_SICI, IT_SUD), Lithuania (LT), Latvia (LV), the
Netherlands(NL),Norway(NO_1, NO_2, NO_3, NO_4,
NO_5), Poland (PL), Portugal (PT), Romania (RO), Ser-
bia (RS), Sweden (SE_1, SE_2, SE_3, SE_4), Slovenia
(SI) and Slovakia (SK).
The list includes all SDAC member countries but Ire-
land [1], and also Switzerland and Serbia. Single Day-
Ahead Coupling (SDAC) is the market integration initia-
tive in Europe that links the day-ahead electricity markets
of multiple countries. It enables cross-border trading of
electricity, ensuring that electricity is allocated efficiently
across Europe based on supply, demand, and transmis-
sion capacity. It uses the common algorithm EUPHEMIA
to calculate electricity prices and cross-border flows, max-
imising economic efficiency and grid stability [35]. See the
European map with bidding zones in Figure 1.
3.2. Dataset
The dataset covers three years, from 1 January 2023
to 31 December 2025. While a longer time-span would
have been preferable, earlier data were excluded due to
the significant irregularities observed during the COVID-
19 period and the subsequent energy-crisis triggered by
the Russian aggression in Ukraine.
Thevariablesarethe actualday-aheadelectricityprice,
load and power generation mix for each of the 39 bidding
zones and gas price. The day-ahead electricity price is
the most traded electricity contract according to the main
European electricity market places EPEX Spot and Nord
Pool. Contracts were set for one hour until September
2025 and then moved to one quarter of an hour; prices are
in€/MWh. Data for load and power generation mix are
covering either one hour or a quarter of an hour period, the
units are MW. We only have the day-close market price
for gas.
In this paper, the 20 power generation categories are
often represented with the following 7 larger categories:
•Solar
•Wind, including onshore and offshore
•Hydro, including run-of-river, water reservoir and
pumped storage
•Nuclear
•Other renewables, including geothermal, biomass,
waste and others
•Fossil gas
•Other fossil fuels, including hard and brown coal,
lignite, oil and others
EU
AT
BE
BG
CH
CZ
DE_LU
DK_1
DK_2
EE
ES
FI
FR
GR
HR
HU
IT_CNOR
IT_CSUD
IT_NORD
IT_SARD
IT_SICI
IT_SUD
LT
LV
NL
NO_1
NO_2
NO_3
NO_4
NO_5
PL
PT
RO
RS
SE_1
SE_2
SE_3
SE_4
SI
SK
0
20
40
60
80
100 Solar
Wind
Hydro
Nuclear
Other Renewables
Fossil Gas
Other Fossil Fuels
Table 1: Power generation mix table showing high diversity between
the bidding zones and solar still generating the least from the main
6 sources
Table 1 and the map in Figure 1 show that there is a
very large diversity of power generation mix across the 39
bidding zones.
SE_4
SI
HU
RS
NO_3
SE_1
NL
DE_LU
IT_CNOR
AT
NO_5
GR
IT_NORD
DK_1
DK_2
HR
FI
IT_SICI
NO_2
BG
IT_SUD
PL
NO_4
ES
IT_CSUD
BE
IT_SARD
NO_1
SK
RO
SE_2
FR
PT
CZ
LT
CH
LV
EE
SE_3
Wind
Hydro
Nuclear
Other Renewables
Fossil Gas
Other Fossil Fuels
Figure1: Dominantgenerationsourcemapshowinglackofgeograph-
ical clusters except fuel gas for Italy and hydro for top northern bid-
ding zones and solar being nowhere the dominant source
Overall the 39 bidding zones and the three year period,
the main power generation source is from fossil fuel with
26% of the total, of which slightly more than half is from
gas, ahead of nuclear at 24%, then wind and hydropower
at both 18%, solar at 10% and other renewables at 4%.
All the data was converted into hourly data by taking
the mean of quarter of an hour data and keeping gas price
constant through the day. The three years of data covers
26,304hours, ofwhichatotalof25,991hoursandinstances
were selected after cleaning the data.
An additional synthetic zone (EU) was constructed
covering the 39 bidding zones with its loads and power
generation mixes being the sums across the 39 bidding
zones. Its prices are set as the weighted average of the 39
bidding zones’ prices with the weights being their mean
loads.
3

3.3. Electricity prices
The integration of the European electricity markets is
still ongoing, hence the 39 bidding zones show quite some
diverse patterns in their historic hourly prices as we can
see in Figure 2.
202320242025
0
250
500
750 EU
202320242025
AT
202320242025
BE
202320242025
BG
202320242025
CH
202320242025
CZ
202320242025
DE_LU
202320242025
DK_1
202320242025
0
250
500
750 DK_2
202320242025
EE
202320242025
ES
202320242025
FI
202320242025
FR
202320242025
GR
202320242025
HR
202320242025
HU
202320242025
0
250
500
750 IT_CNOR
202320242025
IT_CSUD
202320242025
IT_NORD
202320242025
IT_SARD
202320242025
IT_SICI
202320242025
IT_SUD
202320242025
LT
202320242025
LV
202320242025
0
250
500
750 NL
202320242025
NO_1
202320242025
NO_2
202320242025
NO_3
202320242025
NO_4
202320242025
NO_5
202320242025
PL
202320242025
PT
202320242025
0
250
500
750 RO
202320242025
RS
202320242025
SE_1
202320242025
SE_2
202320242025
SE_3
202320242025
SE_4
202320242025
SI
202320242025
SK
Figure 2: 2023-2025 historical prices in€/MWh showing high diver-
sity between the 40 bidding zones
Representing the 39 bidding zones with their price
means and standard deviations (SD) scattered as in Figure
3, we can identify a few clusters with different patterns:
•Low mean and low SD for Norway and Sweden
thanks to their very high level of hydropower, which
has a low operational cost. The isolated further
North bidding zones of Norway and Sweden have
very low means and SDs while the ones further
South are higher because of their interconnectors
with other countries (e.g. Germany).
•High mean and high SD for the Baltic and Eastern
European countries
•High mean and low SD for the six Italian bidding
zones
•Low mean and high SD for the outlier Finland
•Medium mean and medium SD for the remaining
bidding zones that are situated around France and
Germany
20 40 60 80 100 120
Mean ( /MWh)
30
40
50
60
70Standard Deviation ( /MWh)
EU
AT
BE
BG
CH
CZ
DE_LUDK_1DK_2
EE
ES
FI
FR
GR
HR
HU
IT_CNOR IT_CSUDIT_NORD
IT_SARD
IT_SICI
IT_SUD
LT LV
NL
NO_1
NO_2
NO_3
NO_4
NO_5
PLPT
RO
RS
SE_1 SE_2
SE_3
SE_4
SISK
Figure3: Meanversusstandarddeviationplotshowinghighdiversity
between the 40 bidding zones
3.4. Correlation analysis
The dendogram in Figure 4 is based on the hierarchi-
cal clustering of the 39 bidding zones when using 1 mi-
nus price correlation as the distance metric between two
bidding zones (i.e. the higher their price correlation, the
closer the bidding zones). The figure highlights the follow-
ing clusters with subclusters:
•Norway and Sweden. Subclusters are the northern
isolated areas and the southern areas with intercon-
nectors to their neighbours across the seas.
•The Baltic countries and Finland. Lithuania and
Latvia have the same prices most of the time. Fin-
land is hardly part of the cluster.
•Spain and Portugal, very close between each other,
and very distant from the others.
•The remaining of Europe with three subclusters:
•The six Italian bidding zones. The two islands
Sicily and Sardinia are the least close.
•Central and Eastern Europe. Bulgaria and Ro-
mania are very close and Poland is the least
close.
•Germany and most of its neighbours. France
and Switzerland are the least close.
ES
PT
IT_SARD
IT_SICI
IT_CNOR
IT_NORD
IT_CSUD
IT_SUD
PL
AT
CZ
SK
HR
SI
GR
RS
HU
BG
RO
DK_1
DK_2
BE
DE_LU
NL
CH
FR
FI
EE
LT
LV
NO_4
NO_3
SE_1
SE_2
SE_3
SE_4
NO_2
NO_1
NO_5
0.0
0.1
0.2
0.3
0.4
0.5
0.6Distance: (1 - Price Correlation)
Figure 4: Hierarchical clustering dendrogram showing three small
small clusters in Europe peripheries and one large main cluster
around the center of Europe
Here we analyse the correlations of electricity prices with
external parameters. As with standard competitive mar-
kets, the higher the demand, the higher the price. Hence
we expect a strong correlation between electricity prices
and loads. The correlation is above +20% for all bidding
zones except Denmark, see in Figure 5, and the average
is +39%. As discussed in [36], it is better to use residual
load in order to show stronger correlations. Residual load
is defined as load minus solar and wind generation, i.e.
load that has to be covered by "non-free" energy, as the
marginal cost for solar and wind generation is almost nil.
The correlation with electricity prices is as high as +84%
in Germany (as in [36]) and the average is +59%.
ES
PT
IT_SARD
IT_SICI
IT_CNOR
IT_NORD
IT_CSUD
IT_SUD
PL
AT
CZ
SK
HR
SI
GR
RS
HU
BG
RO
DK_1
DK_2
BE
DE_LU
NL
CH
FR
FI
EE
LT
LV
NO_4
NO_3
SE_1
SE_2
SE_3
SE_4
NO_2
NO_1
NO_5
0.0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
 Correlation with Gas Price
Correlation with Load
Correlation with Residual Load
Figure 5: Correlations with electricity price plot highlighting very
high values only with residual load
4

Another strong positive correlation is expected with
gas prices. This is because the electricity market uses a
merit order mechanism with uniform price auction, and as
analysed in [37], gas-run power plants set the price 55%
of the time in 2022 while generating 19% of the Euro-
pean electricity (and even in 2030, their projections show
that the price-setting share is still close to 56%, even with
generation decreasing to 11% of electricity). The aver-
age correlation with the 39 bidding zones is only 29% and
confirms that the relationship is more complex than linear
correlation.
4. Methodology
4.1. Models
The models take load, power generation mix and gas
price as input and outputs the market electricity price.
The models have no time dimension, the input and output
refer to the same one hour period and there is no lagged
data. In fact, the day-ahead electricity price is set ahead
of the actual load and power generation mix, so it is clearly
not a forecasting model. The models have been built only
to help to understand the mechanisms of electricity mar-
kets.
The main model is a straightforward multi-layer per-
ceptron (MLP) with two hidden layers with the Adam op-
timiser[38]andtheMAE(MeanAbsoluteError)lossfunc-
tion. The model has 128 neurons in the first hidden layer
and 32 in the second one, its activation function is ReLu,
the learning rate is 0.0001, the dropout rate is 0.175 and
there is a L1 regularisation with lambda equal to 0.0002.
Thebaselinemodelsarethelinearmodel(LR),therandom
forest (RF) and the gradient boosting regressor (GBR) all
from the scikit-learn library3.
The same model architecture has been used to predict
each of the 39 bidding zone electricity prices. For each
bidding zone model, we filter the features meaningful to
the bidding zone, out of the 364 potential features:
•Features specific to the bidding zone: load and power
generation mix
•Gas price
•Features specific to the bidding zone’s neighbours.
A neighbour is a bidding zone with electricity inter-
connectors connected to the bidding zone.
The maximum amount of features is 122 for the Ger-
many/Luxembourg models with 11 neighbours and the
minimum is 20 for the Sicily models with one neighbour.
We define the EU model as the linear combination of
these39biddingzones’modelswherethefactorsorweights
are the 39 bidding zones’mean loads, which is consistent
with the setting of the EU prices in Section 3.2. More
than being an average European price, this model was mo-
tivated by the idea of "What if there was a common price
3https://scikit-learn.org/stable/
in the European market" which is a very relevant idea as
Europe increases the amount of interconnection capacity.
The weighted average MAEs for the 39 DNN models
are€12.89/MWh and€15.81/MWh for the training and
test sets respectively, which compare favourably with the
baseline models LR, RF and GBR with (€14.92/MWh
and€16.29/MWh), (€13.00/MWh and€16.20/MWh)
and (€12.43/MWh and€16.51/MWh) respectively.
4.2. XAI methods
Because these DNN models use smooth tabular data
as input, all the main standard Feature Importance ex-
plainable methods gave very similar results, hence we use
the SHAP method in the paper as it is the most common
and it has additional properties [24]. The DNN models
are trained on normalised data for inputs and outputs as
standard practice. However, when applying the explain-
able methods, we use denormalised outputs to quantify
the absolute importance of the features rather than rela-
tive values. So the SHAP values have the same unit as
the electricity prices, i.e. Euros per MWh, which is use-
ful. We use conditional expectation rather than marginal
expectation when determining the Shapley values [39, 40].
To estimate the conditional Shapley values with the DNN
models, we use the Monte-Carlo sampling method devel-
oped by [41] and implemented in the GitHub SHAP li-
brary4. For the ensemble tree models (LR and GBR), we
use Tree SHAP [31], which is a fast and exact algorithm
to compute SHAP values.
SHAP values are local explanations where each value
indicates the importance of a specific feature for a spe-
cific prediction. In order to get global explanations per
feature, we take the mean across the dataset of the ab-
solute values of the SHAP values. As often with many
machine learning models, the overall number of features is
very large, so we partition the overall set of features in a
small number of subsets to become meaningful categories.
The drawback of summing the mean absolute SHAP val-
ues across the subsets is to potentially overstate the impor-
tance of certain subsets where features offset each others,
which is very likely when there are so many features and
many have dependencies with each others. Hence we will
use Super-SHAP (SSHAP) values for feature partitions or
super-features as introduced in [3] that allow the nettings
to be done within the subsets before considering the global
explanations (with the mean of the absolute values). A no-
tablepropertyofShapleyandSHAPvaluesistheefficiency
property [42] and this is maintained in SSHAP values.
With SSHAPs, we will analyse the electricity markets
through two different angles: the power generation mix
and the interconnected neighbours. In the first case, we
partition the set of 364 features in 9 super-features: the
7 power generation mix categories as in Section 3.2, load
4https://github.com/shap/shap
5

and gas price. For example, the super-feature wind con-
tains all the features onshore and offshore wind for the
39 bidding zones. We will use the same partition for the
SHAP summary table 2. In the second case, we partition
the set of 364 features in 40 super-features, one for each
of the 39 bidding zone, and gas price. For example, the
super-featureFrance(FR)containstheFrenchloadfeature
and all the French power generation mix features.
Finally as the EU model is a linear combination of
39 models and SHAP and SSHAP are linear functions,
SHAP and SSHAP values of the EU model are simply
the weighted average of the 39 model SHAP and SSHAP
values. And the EU model SHAP and SSHAP values give
a valuable summary of the 39 models.
5. Results
5.1. SHAP analysis
Figure 6 shows the SHAP beeswarm plot for the EU
model with the distribution of the 10 most important fea-
tures of the model, in terms of highest mean absolute
SHAP values5. Colour is used to display the original value
of a feature, red being high and blue being low.
60
 40
 20
 0 20 40
SHAP value (impact on price)
Sum of 354 other features
Solar_ES
Hydro Water Reservoir_NO_2
Nuclear_FR
Fossil Gas_BE
Hydro Pumped Storage_DE_LU
Load_DE_LU
Fossil Gas_ES
Solar_DE_LU
Wind Onshore_DE_LU
GasPrice
Low
High
Feature value
Figure 6: EU SHAP beeswarm plot showing that gas price is the
most important feature by far, followed by German wind onshore
and solar generation features with long negative tails
Table 2 is the summary table of the SHAP analysis on
the 40 models with the nine categories described in the
previous section. "Top 80%" in the column names means
that we consider only the features with the highest mean
absolute SHAP values representing 80% of the sum of the
mean absolute SHAP values. This is to ignore the low
importance features which are more likely to be noisy. The
last two columns estimate the importance weight of each
of the nine categories and for this purpose we just consider
the EU model as it contains all the features weighted by
the size of the 39 bidding zones.
5.1.1. Load
We can see in the summary table 2 that load features
are used 183 times in the 39 models, 106 times they are
part of the "top 80%" features of a model (so 77 times
they are not very important) and in 8 models one load fea-
ture is the most important. Summing the mean absolute
SHAPvaluesforthe39loadfeaturesintheEUmodelgives
5https://shap.readthedocs.io/en/latest/example_notebook
s/api_examples/plots/beeswarm.html
Number of
 Features
Appearance
Count
 (39 models)
First
 Position
 Count
T op 80%
 Count
Avg
Correlation %
 (T op 80%)
Sum
 AbsMean /MWh
 (EU model)
Sum
 AbsMean %
 (EU model)
Load 39 183 8 106 20.49 11.15 15.84
Solar 34 158 1 59 -96.04 10.09 14.33
Wind 46 222 5 62 -94.13 10.09 14.33
Hydro 77 363 7 112 19.94 14.93 21.2
Nuclear 13 63 0 24 -47.14 3.73 5.3
Other Renewables 51 256 0 5 -1.39 0.46 0.65
Fossil Gas 33 157 1 50 83.54 9.04 12.84
Other Fossil Fuels 70 355 0 30 88.43 2.81 3.99
Gas Price 1 39 17 34 87.5 8.11 11.52
T otal 364 1796 39 482 70.41 100.0
Table 2: SHAP summary table showing hydro and load as the most
two important feature categories, even if not very directional (i.e.
low absolute average correlation)
€11.15/MWh, which is 15.84% of the total and makes it
the second highest across the nine categories.
5.1.2. Solar and wind
There are 34 different solar features and 46 different
wind features, used 158 and 222 times respectively overall
in the 39 models. Solar is once the most important feature
(i.e. Spanish solar in the Portuguese model) and wind 5
times. Solar is used 59 times as "top 80%" features, and
wind 62 times. Both have very strong average correlations
around -95%, which confirms that these features are very
directional. The sums of the mean absolute SHAP values
forthe34solarfeaturesintheEUmodelrepresents14.33%
of the total and it is the same for wind.
5.1.3. Hydro, nuclear and Other Renewables
There are 77 different hydro features, 13 different nu-
clear features and 51 different Other Renewables features,
used 363, 63 and 256 times respectively overall in the 39
models. Hydrois7timesthemostimportantfeatureandit
is never the case for nuclear and Other Renewables. Hy-
dro is used 112 times as "top 80%" features, nuclear 24
times and Other Renewables 5 times only. The sums of
the mean absolute SHAP values of the category features
in the EU model represents 21.20% of the total for hydro,
the highest of all categories, 5.30% for nuclear and 0.65%
only for Other Renewables. For this reason, we will often
skip the Other Renewables category in the remaining part
of the paper.
5.1.4. Fossil fuels and gas price
There are 33 different fossil gas features, 70 different
other fossil fuels features and 1 gas price feature, used
157, 355 and 39 times respectively overall in the 39 models.
Fossil gas is once the most important feature and gas price
is as many as 17 times the most important feature. Fossil
gasisused50timesas"top80%"features, otherfossilfuels
30 times and gas price 34 times (i.e. only in 5 models gas
price is not important). The sums of the mean absolute
SHAP values of the category features in the EU model
represent 12.84% of the total for fossil gas, 3.99% only for
other fossil fuels and 11.52% for gas price.
5.1.5. EU Model
The EU model has 364 features and gas price is the
most important feature by far: its mean absolute SHAP
value is€8.11/MWh, which is equivalent to the sum of the
second, third and fourth most important features’. Gas
6

price does play a very important role in setting the prices
in the European electricity markets as discussed in [17]
and Section 3.4, and its top position was expected. Figure
6 shows that it can push up the EU electricity price by as
much as€40/MWh when its price is very high.
Wind onshore and solar powers in Germany are the
second and third most important features of the EU model
with theirmean absoluteSHAP values of€3.25/MWh and
€2.69/MWh respectively. They both have asymmetrical
distribution with a long tail for negative SHAP values that
can push down the EU electricity price by as much as
€20/MWh each when their power generation is very high.
Germany has two other features in the top ten for the EU
model: load and hydro pumped storage.
Fossil gas in Spain and Belgium are 4th and 7th re-
spectively. Nuclear power in France is 8th. Hydro water
reservoir in Norway(2) is 9th, which is notable as its capac-
ity is only 9GW. The direction for hydro pumped storage
and hydro water reservoir is opposite to wind and solar’s
as water is released down when electricity price is high,
and pumped up when electricity price is low.
5.2. SSHAP analysis with power generation mix and load
Figure 7 shows the SSHAP beeswarm plot for the EU
model with the distribution of the 9 super-features (as de-
fined in Section 4.2), in order of the highest mean absolute
SSHAP values first. Table 3 shows for each of the 40 mod-
els the relative importance of each of the 9 super-features
in terms of mean absolute SSHAP values.
40
 20
 0 20 40
SSHAP value (impact on price)
Other Renewables
Other Fossil Fuels
Nuclear
Load
Fossil Gas
Wind
Hydro
Gas Price
Solar
SSHAP beeswarm plot for EU
Low
High
Feature value
Figure 7: EU SSHAP beeswarm plot showing that solar is the most
important super-feature, even if it is the least generating source, and
load is now the 6th super-feature, as many of its SHAP values have
offset each others
EU
AT
BE
BG
CH
CZ
DE_LU
DK_1
DK_2
EE
ES
FI
FR
GR
HR
HU
IT_CNOR
IT_CSUD
IT_NORD
IT_SARD
IT_SICI
IT_SUD
LT
LV
NL
NO_1
NO_2
NO_3
NO_4
NO_5
PL
PT
RO
RS
SE_1
SE_2
SE_3
SE_4
SI
SK
0
20
40
60
80
100 Load
Solar
Wind
Hydro
Nuclear
Other Renewables
Fossil Gas
Other Fossil Fuels
Gas Price
Table 3: SSHAP summary table showing for each bidding zone the
mean absolute SSHAP values for the 9 super-features
Solar is the most important super-feature for the EU
modelanditsmeanabsoluteSSHAPvalueis€9.42/MWh,
ahead of gas price at€8.11/MWh (same as in the previous
section as gas price is only one feature). Solar can push
down the EU electricity price by as much as€60/MWh
when its power generation is very high across Europe. Gas
price can push up the EU electricity price by as much as
€40/MWh when its price is very high.
The mean absolute SSHAP values are between
€5.5MWh and€6.5MWh for hydro, wind, fossil gas and
load, but only€2.11MWh for nuclear and€1.42MWh for
non-gas fossil fuels.
5.3. SSHAP analysis with interconnected neighbours
In this section, we analyse the impact of the neigh-
bours on the domestic electricity prices. So there are 40
super-features made of the 39 bidding zones and gas price,
as described in Section 4.2. Table 4 shows for each of
the model the relative importance of the super-features in
terms of mean absolute SSHAP values. From Table 4, the
sum of the mean absolute SSHAP values for the neigh-
bour bidding zones are represented in the map in Figure
8 highlighting the importance of neighbours in setting the
domestic price.
AT
BE
BG
CH
CZ
DE_LU
DK_1
DK_2
EE
ES
FI
FR
GR
HR
HU
IT_CNOR
IT_CSUD
IT_NORD
IT_SARD
IT_SICI
IT_SUD
LT
LV
NL
NO_1
NO_2
NO_3
NO_4
NO_5
PL
PT
RO
RS
SE_1
SE_2
SE_3
SE_4
SI
SK
0
20
40
60
80
100
AT
BE
BG
CH
CZ
DE_LU
DK_1
DK_2
EE
ES
FI
FR
GR
HR
HU
IT_
IT_C
IT_NORD
IT_SARD
IT_SICI
IT_SUD
LT
LV
NL
NO_1
NO_2
NO_3
NO_4
NO_5
PL
PT
RO
RS
SE_1
SE_2
SE_3
SE_4
SI
SK
DE_LU
DE_LU
GR
DE_LU
DE_LU
AT
DE_LU
DE_LU
LV
PT
SE_3
BE
IT_SUD
HU
AT
IT_NORD
IT_SAR
IT_C
IT_CSUD
IT_SUD
IT_CSUD
PL
LT
DE_LU
SE_3
NO_1
NO_4
NO_3
NO_1
SE_4
ES
HU
HR
NO_4
NO_4
FI
SE_3
AT
CZ
IT_N
NL
RO
AT
AT
NL
NO_2
DK_1
FI
FR
EE
ES
BG
SI
HR
IT_CSUD
IT_SUD
SI
IT_S
LV
EE
NO_2
NO_2
DE_LU
SE_2
SE_2
NO_2
DE_LU
BG
HU
FI
SE_3
SE_4
DE_LU
IT_NOR
HU
CZ
FR
R
IT_NOR
SK
NO_
NL
SE_
SE_1
DE_LU
RS
RO
IT_CN
AT
GR
SE_4
BE
NO_3
DK_1
NO_1
FI
NO_3
SK
RS
RO
SE_2
SE_1
DK_1
DK_
HR
PL
CH
FR
PL
PL
DK
NO_4
IT
SK
FR
D
NO_
NO_5
NO_
SE
CZ
BG
NO_3
SE_
LT
HU
H
BE
SE
C
RS
CH
NL
LT
NO
PL
GP
GP
GP
GP
GP
GP
GP
GP
GP
GP
G
GP
GP
GP
GP
GP
GP
GP
GP
GP
GP
GP
GP
GP
GP
GP
GP
GP
GP
GP
GP
GP
GP
G
G
GP
GP
GP
GP
Domestic bidding zone
1st most important neighbour
2nd most important neighbour
3rd most important neighbour
4th most important neighbour
5th most important neighbour
Least important neighbours
Gas price
Table 4: SSHAP summary table with bidding zone super-features
where yellow shows the importance of the domestic features, black
shows the importance of gas price and all the other colours show the
importance of the different neighbours. The table shows that the
neighbours play a very large role in setting domestic prices in most
bidding zones
30
40
50
60
70
80
Percentage
Figure 8: SSHAP neighbours importance map showing that most
bidding zones have neighbours being more than 50% responsible in
the domestic price formation
The bidding zone most dependent on neighbours is
Sweden(4) with 83% of the total mean absolute SSHAP
values coming from neighbour super-features and the least
dependent ones are the Italian islands and then Spain with
34%. Theaverageacrossthe39biddingzonesisasmuchas
61% for the neighbour super-features. The average for the
7

domestic super-feature is only 21% (the remaining 18% is
for the gas price feature). Spain has the highest percentage
by far with 51% coming from its domestic super-feature,
highlighting its isolation.
6. Discussion
6.1. Power generation mix and load
The SSHAP analysis reveals conclusions that differ
substantially from those of the standard SHAP analysis.
First, load proves less important than initially suggested.
As highlighted in Section 5.1.1, the load SHAP values ex-
hibit mixed directional impacts (both positive and nega-
tive correlations with prices), which means that some load
features offset each others. By using SSHAP rather than
SHAP, we get the importance after the nettings which is
more revealing.
Load
Solar
Wind
Hydro
Fossil Gas
Gas Price
Figure 9: Dominant SSHAP super-feature map showing solar being
dominant in as many as 7 medium and large bidding zones
Notably, solar has the largest impact on the EU elec-
tricity prices while it is the source generating the least
(excluding the Other Renewables category), see Table 1.
Its mean absolute SSHAP value is€9.42/MWh, which is
30% of the total impact from power generation sources
or three times its share of EU power generation. Solar is
the dominant SSHAP super-feature in 7 medium and large
bidding zones (see Figure 9).
One reason for this is simply that the most important
trait of a feature is not necessarily its mean; for example
if a feature was constant, then its impact on price would
be nil by definition, even if it had high values. Which is
the reason why nuclear has the least impact on prices, its
generation being quite stable as a base load power. Look-
ing at standard deviation instead, solar has the highest in
terms of weighted average across the 39 bidding zones of
relativestandarddeviationsat25%. Furthermorethetotal
solar power generation across the 39 bidding zones, i.e. the
EU solar power generation, has a standard deviation even
higher relatively at 33%. This is because solar power gen-
erations are more correlated across the 39 bidding zones
thantheothersources; inparticularwindyweatherismore
a localised phenomenon while sunny weather is more re-
gional, or generally more uniform over larger areas.
In contrast, nuclear produces 24% of European elec-
tricity and its EU mean absolute SSHAP value is only
€2.11/MWh (7% of total generation impact). For exam-
ple France’s dominant SSHAP super-feature is gas gener-
ation while it covers only 4% of its electricity production
compared to 69% for nuclear.
Similarly, non-gas fossil fuels covers mainly base load.
It produces 13% of European electricity and its EU mean
absolute SSHAP value is 4% relatively. For example
Poland’s dominant SSHAP super-feature is solar while it
covers only 11% of its electricity production compared to
61% for non-gas fossil fuels. Nuclear and non-gas fossil
fuels are never the dominant SSHAP super-feature for any
bidding zone.
Nordic bidding zones have their dominant SSHAP
super-features, hydro and wind, matching their domi-
nant generation sources for most of them. The excep-
tions are when the dominant generation source is nuclear
(Sweden(3) and Finland) and the corresponding domi-
nant SSHAP super-feature is wind and the third excep-
tion is for Denmark(1) where the dominant SSHAP super-
feature is hydro while the bidding zone has no hydropower!
This is explained by the cross-border influence of German
and Norwegian hydro. Denmark(1) is not unique as the
Netherlands has exactly the same situation and for the
same reasons. This is consistent with Section 5.1.5 that
reveals that hydro pumped storage in Germany and hy-
dro water reservoir in Norway(2) are the 6th and 9th most
important features overall.
There is another cluster of countries with hydro as the
dominant SSHAP super-feature made of Austria, Czechia,
Hungary, Slovakia and Slovenia. Czechia and Hungary
have hardly any hydropower and this time the hydropower
source is mainly from Austria.
Finally Italy is quite unique with its six bidding zones
quite uniform where gas is the dominant generation source
in most of the bidding zones and the dominant SSHAP
super-feature is gas price for all six bidding zones. This is
consistent with Italy having the highest average electricity
prices in Europe with a low standard deviation (see Figure
3) as the renewables are hardly large enough (even at peak
output) to move the prices down significantly.
6.2. Interconnected neighbours
The map in Figure 10 shows the dominant super-
feature for each bidding zone. In only 13 out of the 39
bidding zones, the domestic super-feature is the most im-
portant, including the four largest bidding zones (Ger-
many, France, Spain and Poland) as size does matter. 6
out of the 11 neighbours of Germany have the German
features as their dominant super-feature, confirming the
8

importance of Germany on its neighbours due to its large
solar and wind generation capacities (52GW and 57GW
respectively) and its impactful hydro pumped storage.
SE_3
AT
AT
HR
NO_4
SE_1
DE_LU
DE_LU
GP
AT
NO_1
GR
GP
DE_LU
DE_LU
HR
FI
GP
NO_2
GR
GP
PL
NO_3
ES
GP
DE_LU
GP
SE_3
CZ
RO
NO_4
FR
ES
DE_LU
LT
DE_LU
LT
LV
SE_3
Figure 10: Dominant super-feature map highlighting that German
(DE_LU) features are the most important in 7 bidding zones. Each
colour represents one specific super-feature except the cream colour
representing super-features being dominant just once
Portugal has only one neighbour, Spain, and the Span-
ish features are significantly more important than the Por-
tugese features for the Portugese electricity prices (mean
absolute SSHAP value for Spanish features is€24/MWh
compared to€11/MWh for the Portugese features). The
capacity of interconnectors between Portugal and Spain is
4.1 GW, which is 70% of the mean load in Portugal, and
helps to explain the importance of Spanish features in the
Portugese electricity market. Instead 4.1 GW is 15% only
of the mean load in Spain, and the interconnector capac-
ity with the other neighbour, France, is even lower. So
the total interconnector capacity of Spain is only 29% of
its mean load and this is one reason why Spain has one of
the lowest neighbour dependence percentage as set in Fig-
ure 8. At the other extreme, Sweden(4) has the highest
neighbour dependence percentage and its interconnector
capacity is as high as 313% of its mean load. Across the
39 bidding zones, the correlation between the neighbour
dependence percentages and the interconnector capacities
as a percentage of mean load is +48%, which is significant.
7. Conclusions
This paper provides an analysis of the drivers and in-
terdependencies of European electricity prices across 39
bidding zones, using DNN models combined with XAI
techniques. By leveraging SHAP and the newly intro-
duced SSHAP framework, we move beyond predictive per-
formance to deliver interpretable insights into the mecha-
nisms shaping electricity price formation in highly inter-
connected markets.
Several key results emerge from the analysis. First,
while load is traditionally viewed as a primary driver of
electricity prices, its explanatory power is more limited
than expected once the SSHAP method is used to reduce
the impact of noisy features. In contrast, renewable energy
sources, particularly solar, play a disproportionately large
role in price formation. Despite representing a smaller
share of total power generation, solar energy emerges as
themostinfluentialgenerationsourceintheSSHAPanaly-
sis, reflecting its high variability and strong directional im-
pact on prices. Second, gas price remains a dominant and
highlyconsistentdriveracrosselectricitymarkets, confirm-
ing the continued importance of gas-fired generation in
the merit-order mechanism. However, its influence varies
significantly depending on the power generation mix of
each bidding zone, with reduced impact in systems dom-
inated by non-gas base load sources such as hydropower.
Third, the analysis highlights the critical role of intercon-
nections. Electricity prices are not solely determined by
domestic conditions: neighbouring electricity markets ex-
ert substantial influence, often exceeding that of local vari-
ables. In only a minority of bidding zones is the domestic
system the primary determinant of prices. This finding
underscores the high degree of interdependence within the
European electricity system and the importance of cross-
border flows in price formation.
Future work could refine the representation of intercon-
nections by explicitly modelling transmission constraints
and flows, rather than relying solely on neighbouring fea-
tures. This would help to better capture congestion ef-
fects and the physical limits of market integration. Fu-
ture work could also differentiate explanations for differ-
ent price ranges and for very high prices in particular. As
highlighted with the beeswarm plots, solar and wind distri-
butions have long negative tails to push down prices when
their generations are very high, but they do not push much
the prices up when their generations are very low or nil.
Hence they are not good explanations for extreme high
prices. This is confirmed by their SSHAP values being
significantly lower with tree ensemble baseline models (RF
and GBR) that use RMSE (Root Mean Squared Error) as
loss function rather than MAE.
Finally, from a policy perspective, the insights pro-
vided by this analysis could be used to assess the impact
of different market design choices, such as increased in-
terconnection capacity or alternative pricing mechanisms.
Exploring counterfactual scenarios—such as a fully inte-
grated European electricity market with a single clearing
price—remains a particularly promising direction for fu-
ture research.
Declaration of Competing Interest
The authors declare that they have no known compet-
ing financial interests or personal relationships that could
haveappearedtoinfluencetheworkreportedinthispaper.
9

Data A vailability
The data that support the findings of this study are
available athttps://transparency.entsoe.eu/and can
be accessed with the code fromhttps://github.com/E
nergieID/entsoe-py
Acknowledgments
This work was supported by EDF Energy R&D UK
and EPSRC under Grant EP/V519625/1.
Declaration of generative AI and AI-assisted tech-
nologies in the manuscript preparation process
During the preparation of this work, the author(s) used
Mistral and Claude for correcting some sections of the
Python code and improving the readability of some sec-
tions of the paper. The author(s) reviewed and edited
the output as needed and take full responsibility for the
content of the published article.
References
[1] ENTSO-E, ENTSO-E Market Report 2025 (2025).
URLhttps://eepublicdownloads.blob.core.windows.net/strapi-t
est-assets/strapi-assets/entso-e_Market_report_2025.pdf
[2] IEA, Electricity 2026: Analysis and Forecast to 2030 (2026).
URLhttps://iea.blob.core.windows.net/assets/b73798cb-e452-4
2b9-9d8a-07542de7a041/Electricity_2026.pdf
[3] A. Pesenti, A. O’Sullivan, Explaining deep neural network models
for electricity price forecasting with XAI, Energy and AI 21 (2025)
100532.doi:10.1016/j.egyai.2025.100532.
URLhttps://linkinghub.elsevier.com/retrieve/pii/S2666546825
000643
[4] K. Maciejowska, B. Uniejewski, R. Weron, Forecasting Electricity
Prices, arXiv:2204.11735 [q-fin] (Apr. 2022).doi:10.48550/arXiv.2
204.11735.
URLhttp://arxiv.org/abs/2204.11735
[5] H. A. Gil, C. Gómez-Quiles, A. Gómez-Expósito, J. R. Santos,
Forecasting Prices in Electricity Markets: Needs, Tools and Lim-
itations, in: A. Sorokin, S. Rebennack, P. M. Pardalos, N. A. Il-
iadis, M. V. F. Pereira (Eds.), Handbook of Networks in Power
Systems I, Springer, Berlin, Heidelberg, 2012, pp. 123–150.doi:
10.1007/978-3-642-23193-3_5.
URLhttps://doi.org/10.1007/978-3-642-23193-3_5
[6] J. Contreras, R. Espinola, F. Nogales, A. Conejo, ARIMA models
to predict next-day electricity prices, IEEE Transactions on Power
Systems 18 (3) (2003) 1014–1020, conference Name: IEEE Transac-
tions on Power Systems.doi:10.1109/TPWRS.2002.804943.
URLhttps://ieeexplore.ieee.org/abstract/document/1216141
[7] A. J. Conejo, J. Contreras, R. Espínola, M. A. Plazas, Forecasting
electricity prices for a day-ahead pool-based electric energy market,
International Journal of Forecasting 21 (3) (2005) 435–462.doi:
10.1016/j.ijforecast.2004.12.005.
URLhttps://www.sciencedirect.com/science/article/pii/S01692
07004001311
[8] K. Würzburg, X. Labandeira, P. Linares, Renewable generation and
electricity prices: Taking stock and new evidence for Germany and
Austria, Energy Economics 40 (2013) S159–S171.doi:10.1016/j.en
eco.2013.09.011.
URLhttps://www.sciencedirect.com/science/article/pii/S01409
88313002065
[9] Z. Csereklyei, S. Qu, T. Ancev, The effect of wind and solar power
generationonwholesaleelectricitypricesinAustralia, EnergyPolicy
131 (2019) 358–369.doi:10.1016/j.enpol.2019.04.007.
URLhttps://www.sciencedirect.com/science/article/pii/S03014
21519302435
[10] J. Seel, A. D. Mills, R. H. Wiser, Impacts of High Variable Re-
newable Energy Futures on Wholesale Electricity Prices, and on
Electric-Sector Decision Making (May 2018).
URLhttps://escholarship.org/uc/item/2xq5d6c9
[11] B. Acar, O. Selcuk, S. A. Dastan, The merit order effect of wind and
river type hydroelectricity generation on Turkish electricity prices,
Energy Policy 132 (2019) 1298–1319.doi:10.1016/j.enpol.2019.0
7.006.
URLhttps://www.sciencedirect.com/science/article/pii/S03014
21519304483
[12] L. Wen, K. Suomalainen, B. Sharp, M. Yi, M. S. Sheng, Impact of
wind-hydro dynamics on electricity price: A seasonal spatial econo-
metric analysis, Energy 238 (2022) 122076.doi:10.1016/j.energy.2
021.122076.
URLhttps://www.sciencedirect.com/science/article/pii/S03605
44221023240
[13] T. Stringer, M. Joanis, S. Abdoli, Power generation mix and elec-
tricity price, Renewable Energy 221 (2024) 119761.doi:10.1016/j.
renene.2023.119761.
URLhttps://www.sciencedirect.com/science/article/pii/S09601
48123016762
[14] S. K. Aggarwal, L. M. Saini, A. Kumar, Electricity price forecast-
ing in deregulated markets: A review and evaluation, International
Journal of Electrical Power & Energy Systems 31 (1) (2009) 13–22.
doi:10.1016/j.ijepes.2008.09.003.
URLhttps://linkinghub.elsevier.com/retrieve/pii/S0142061508
000884
[15] R. Weron, Electricity price forecasting: A review of the state-of-the-
art with a look into the future, International Journal of Forecasting
30 (4) (2014) 1030–1081.doi:10.1016/j.ijforecast.2014.08.008.
URLhttps://linkinghub.elsevier.com/retrieve/pii/S0169207014
001083
[16] V.Laitsos, G.Vontzos, P.Paraschoudis, E.Tsampasis, D.Bargiotas,
L. H. Tsoukalas, The State of the Art Electricity Load and Price
Forecasting for the Modern Wholesale Electricity Market, Energies
17 (22) (2024) 5797, number: 22.doi:10.3390/en17225797.
URLhttps://www.mdpi.com/1996-1073/17/22/5797
[17] B. Zakeri, I. Staffell, P. E. Dodds, M. Grubb, P. Ekins, J. Jääskeläi-
nen, S. Cross, K. Helin, G. Castagneto Gissey, The role of natural
gas in setting electricity prices in Europe, Energy Reports 10 (2023)
2778–2792.doi:10.1016/j.egyr.2023.09.069.
URLhttps://www.sciencedirect.com/science/article/pii/S23524
84723013057
[18] A. Khosravi, S. Nahavandi, D. Creighton, Quantifying uncertainties
of neural network-based electricity price forecasts, Applied Energy
112 (2013) 120–129.doi:10.1016/j.apenergy.2013.05.075.
URLhttps://www.sciencedirect.com/science/article/pii/S03062
61913004881
[19] J. Lago, F. De Ridder, B. De Schutter, Forecasting spot elec-
tricity prices: Deep learning approaches and empirical compari-
son of traditional algorithms, Applied Energy 221 (2018) 386–405.
doi:10.1016/j.apenergy.2018.02.069.
URLhttps://linkinghub.elsevier.com/retrieve/pii/S0306261918
30196X
[20] F. Doshi-Velez, B. Kim, Towards A Rigorous Science of Inter-
pretable Machine Learning (Feb. 2017).
URLhttps://arxiv.org/abs/1702.08608v2
[21] F. Bodria, F. Giannotti, R. Guidotti, F. Naretto, D. Pedreschi,
S. Rinzivillo, Benchmarking and Survey of Explanation Methods
for Black Box Models, arXiv:2102.13076 [cs] (Feb. 2021).
URLhttp://arxiv.org/abs/2102.13076
[22] C. Molnar, Interpretable Machine Learning, Molnar, 2022.
URLhttps://christophm.github.io/interpretable-ml-book/
[23] R. Machlev, L. Heistrene, M. Perl, K. Levy, J. Belikov, S. Mannor,
Y. Levron, Explainable Artificial Intelligence (XAI) techniques for
energy and power systems: Review, challenges and opportunities,
Energy and AI 9 (2022) 100169.doi:10.1016/j.egyai.2022.100169.
URLhttps://linkinghub.elsevier.com/retrieve/pii/S2666546822
000246
[24] S. Lundberg, S.-I. Lee, A Unified Approach to Interpreting Model
Predictions, arXiv:1705.07874 [cs, stat] (Nov. 2017).
URLhttp://arxiv.org/abs/1705.07874
[25] M. T. Ribeiro, S. Singh, C. Guestrin, "Why Should I Trust You?":
Explaining the Predictions of Any Classifier, in: Proceedings of the
22nd ACM SIGKDD International Conference on Knowledge Dis-
covery and Data Mining, ACM, San Francisco California USA, 2016,
pp. 1135–1144.doi:10.1145/2939672.2939778.
URLhttps://dl.acm.org/doi/10.1145/2939672.2939778
[26] L. Heistrene, R. Machlev, M. Perl, J. Belikov, D. Baimel, K. Levy,
S. Mannor, Y. Levron, Explainability-based Trust Algorithm for
electricity price forecasting models, Energy and AI 14 (2023)
100259.doi:10.1016/j.egyai.2023.100259.
URLhttps://linkinghub.elsevier.com/retrieve/pii/S2666546823
000319
[27] L. Heistrene, J. Belikov, D. Baimel, L. Katzir, R. Machlev, K. Levy,
S. Mannor, Y. Levron, An Improved and Explainable Electric-
ity Price Forecasting Model via SHAP-based Error Compensation
Approach, IEEE Transactions on Artificial Intelligence (2024) 1–
11Conference Name: IEEE Transactions on Artificial Intelligence.
10

doi:10.1109/TAI.2024.3455313.
URLhttps://ieeexplore.ieee.org/document/10669041
[28] L. Breiman, Random Forests, Machine Learning 45 (1) (2001) 5–32.
doi:10.1023/A:1010933404324.
URLhttps://doi.org/10.1023/A:1010933404324
[29] A. Fisher, C. Rudin, F. Dominici, All Models are Wrong, but Many
are Useful: Learning a Variable’s Importance by Studying an En-
tire Class of Prediction Models Simultaneously, Journal of Machine
Learning Research 20 (177) (2019) 1–81.
URLhttp://jmlr.org/papers/v20/18-760.html
[30] J. Trebbien, L. Rydin Gorjão, A. Praktiknjo, B. Schäfer, D. Wit-
thaut, Understanding electricity prices beyond the merit order
principle using explainable AI, Energy and AI 13 (2023) 100250.
doi:10.1016/j.egyai.2023.100250.
URLhttps://linkinghub.elsevier.com/retrieve/pii/S2666546823
000228
[31] S. M. Lundberg, G. G. Erion, S.-I. Lee, Consistent Individualized
Feature Attribution for Tree Ensembles, arXiv:1802.03888 [cs] (Mar.
2019).doi:10.48550/arXiv.1802.03888.
URLhttp://arxiv.org/abs/1802.03888
[32] L. Tschora, E. Pierre, M. Plantevit, C. Robardet, Electricity price
forecasting on the day-ahead market using machine learning, Ap-
plied Energy 313 (2022) 118752.doi:10.1016/j.apenergy.2022.1187
52.
URLhttps://linkinghub.elsevier.com/retrieve/pii/S0306261922
002057
[33] M. M. Mascarenhas, M. Amelin, H. Kazmi, Bridging Accuracy and
Explainability in Electricity Price Forecasting, in: 2024 20th Inter-
national Conference on the European Energy Market (EEM), 2024,
pp. 1–6.doi:10.1109/EEM60825.2024.10608857.
URLhttps://ieeexplore.ieee.org/document/10608857/?arnumber=
10608857
[34] J. Lago, G. Marcjasz, B. De Schutter, R. Weron, Forecasting day-
aheadelectricityprices: Areviewofstate-of-the-artalgorithms, best
practices and an open-access benchmark, Applied Energy 293 (2021)
116983.doi:10.1016/j.apenergy.2021.116983.
URLhttps://linkinghub.elsevier.com/retrieve/pii/S0306261921
004529
[35] NEMOs, EUPHEMIA Public Description - Single Price Coupling
Algorithm (Aug. 2024).
URLhttps://www.nordpoolgroup.com/globalassets/download-cente
r/single-day-ahead-coupling/euphemia-public-description.pdf
[36] A. Aščerić, M. Pantoš, M. Čepin, Correlation of Day-Ahead Elec-
tric Energy Market Price with Renewable Energy Sources Genera-
tion and Load Forecast, in: Advanced Technologies, Systems, and
Applications VI, Springer Nature, Switzerland, 2022, pp. 99–109.
doi:10.1007/978-3-030-90055-7_8.
[37] A. Gasparella, D. Koolen, A. Zucker, The Merit Order and Price-
Setting Dynamics in European Electricity Markets (2023).
URLhttps://publications.jrc.ec.europa.eu/repository/handle/
JRC134300
[38] D. P. Kingma, J. Ba, Adam: A Method for Stochastic Optimization,
arXiv:1412.6980 [cs] (Jan. 2017).doi:10.48550/arXiv.1412.6980.
URLhttp://arxiv.org/abs/1412.6980
[39] H. Chen, J. D. Janizek, S. Lundberg, S.-I. Lee, True to the Model
or True to the Data?, arXiv:2006.16234 [cs, stat] (Jun. 2020).
URLhttp://arxiv.org/abs/2006.16234
[40] H. Chen, I. C. Covert, S. M. Lundberg, S.-I. Lee, Algorithms to
estimate Shapley value feature attributions, Nat Mach Intell 5 (6)
(2023) 590–601.doi:10.1038/s42256-023-00657-x.
URLhttps://www.nature.com/articles/s42256-023-00657-x
[41] E. Štrumbelj, I. Kononenko, Explaining prediction models and indi-
vidual predictions with feature contributions, Knowl Inf Syst 41 (3)
(2014) 647–665.doi:10.1007/s10115-013-0679-x.
URLhttp://link.springer.com/10.1007/s10115-013-0679-x
[42] L. S. Shapley, A value for n-person games (1953), in: A. E. Roth
(Ed.), The Shapley Value: Essays in Honor of Lloyd S. Shapley,
Cambridge University Press, Cambridge, 1988, pp. 31–40.doi:10.1
017/CBO9780511528446.003.
URLhttps://www.cambridge.org/core/books/shapley-value/value
-for-nperson-games/1AA9D343DE7A87A97F69E999D329B57A
11
