---
title: 'Saving for sunny days: The impact of climate (change) on consumer prices in the euro area'
url: https://arxiv.org/abs/2401.03740
category: consumer-behavior
subcategory: empirical
date: 2024-01
venue: ''
authors:
- Paulo M. M. Rodrigues
- Mirjam Salish
- Nazarii Salish
source: arxiv
pdf_url: https://arxiv.org/pdf/2401.03740
pages: 57
chars: 82261
fetched_at: '2026-11-08T13:12:01+00:00'
kb_version: 1
---

# Saving for sunny days: The impact of climate (change) on consumer prices in the euro area

Saving for sunny days: The impact of climate
(change) on consumer prices in the euro area
Paulo M. M. Rodrigues ∗, Mirjam Salish †, Nazarii Salish ‡
Preliminary Version: January 2024
Do not cite without permission
Abstract
Climate (change) affects the prices of goods and services in different countries
or regions differently. Simply relying on aggregate measures or summary statis-
tics, such as the impact of average country temperature changes on HICP headline
inflation, conceals a large heterogeneity across (sub-)sectors of the economy. Ad-
ditionally, the impact of a weather anomaly on consumer prices depends not only
on its sign and magnitude, but also on its location and the size of the area affected
by the shock. This is especially true for larger countries or regions with diverse
climate zones, since the geographical distribution of climatic effects plays a role in
shaping economic outcomes. Using time series data of geolocations, we demonstrate
that relying solely on country averages fails to adequately capture and explain the
influence of weather on consumer prices in the euro area. We conclude that the
information content hidden in rich and complex surface data can provide valuable
insights into the role of weather and climate variables for price stability, and more
generally may help to inform economic policy.
Keywords: Inflation, climate change, surface time-series data, heterogeneity, com-
mon factors, functional data analysis
JEL codes: C18, E31, E37, Q54
∗Banco de Portugal and Nova School of Business and Economics, pmrodrigues@bportugal.pt
†Oesterreichische Nationalbank, mirjam.salish@oenb.at
‡Universidad Carlos III de Madrid, nsalish@eco.uc3m.es
Disclaimer: Opinions expressed by the authors do not necessarily reflect the official viewpoint of the
Banco de Portugal, the OeNB or the Eurosystem.
1
arXiv:2401.03740v1  [econ.GN]  8 Jan 2024

1 Introduction
Climate change and the dependence on fossil fuels are one of the greatest challenges of our
time. Anthropogenic greenhouse gas emissions contribute to a rise in global temperatures
and are linked to the increasing incidence of extreme weather events such as droughts,
floods, wildfires, and heat waves. Consequences of global warming include rising sea
levels, melting of glaciers, reduction of biodiversity, as well as heat-related increases in
morbidity and mortality rates, all of which are interrelated. Thus, climate change impacts
economic activity in a variety of ways: From a rise in the volatility of agricultural output,
over productivity losses, supply and demand imbalances, the destruction of infrastructure
and global supply chains, increased uncertainty, to structural and sectoral shifts.
The (observed and expected future) consequences for economic activity are so se-
vere that climate protection is no longer seen as the exclusive responsibility of non-
governmental organizations (NGOs) or environmentalists. The network of greening the
financial system has grown from eight (founding) members in 2017 to more than 100
members as of December 2021. In 2021 the European Central Bank (ECB) vouched to
support the European Union’s (EU) plans for climate protection in its monetary policy
strategy as long as this would not be at odds with its primary mandate of price sta-
bility. Several other central banks also take sustainability considerations into account.
Consequently, one key question from a central bank’s perspective is to understand the
relationship between climate change and price stability. This is becoming ever more
important in light of the recent high inflation period. Not only central banks, but also
national governments need to understand this relation. Price stability is the main priority
of central banks around the globe for a reason: Sustainable and inclusive growth is diffi-
cult to achieve without stable prices and it is not only central banks that have to answer
for high inflation rates. To be able to take evidence-based decisions and design policies
that protect the most vulnerable members of society while adapting to climate change,
it is crucial to understand the implications of climate change on price developments.
Climate can impact consumer prices directly and indirectly through various channels.
Extreme weather events and natural hazards, such as droughts, wildfires or floods destroy
harvests, infrastructure, and livestock. Heat waves, long and cold winters or shifts in
precipitation patterns may raise the costs of agricultural production and increase the
volatility of output, lower labor productivity and exacerbate inequality. At the same time,
2

climate protection policies have direct and indirect effects on prices. The price of carbon,
as measured by the EU’s emissions trading system (EU ETS) allowance prices, increased
markedly throughout 2021, and in many EU countries national policies complementary
to the EU ETS directly raise the prices for fossil energy sources. The direct inflationary
effects of mitigation policies are often easier to measure and quantify than the effects
of climate change itself leading to a possible underestimation of the threat that climate
change poses to price stability.
The existing literature on the impact of climate (change) on inflation (see Section 2)
so far has mainly focused on extreme temperatures (Faccia et al., 2021), natural disasters
(Dafermos et al., 2021 and Parker, 2018) and precipitation (Moessner, 2022 and Kotz
et al., 2023). However, climate change has many dimensions and to fully understand
its impact on prices, studying each of them in isolation or only focusing on a particular
subset may be insufficient and lead to biased estimates (Auffhammer et al., 2013). For
instance, low wind speeds (as experienced in Europe in the summer of 2021), reduce
wind energy and therefore impact electricity consumer prices as well as the prices for
the fossil fuels needed as substitutes. 1 Similarly, insufficient rainfall increases the costs
of agricultural production and reduces water quantities and speed in rivers. This in
turn may dampen hydro-power based electricity generation. Heavy rainfall, on the other
hand, may damage crops, lead to flooding and increase landslide risk. Additionally,
extreme precipitation can degrade water quality by overwhelming wastewater systems
or by carrying pollutants to lakes, streams or bays and thereby harm ecosystems and
increase the risk for waterborne diseases. Changes in solar radiation, often referred to
as “solar brightening” (experienced particularly in North America and Europe over the
last decades) and “solar dimming” (which in recent years concerned particularly China
and India) impacts crop yields, where increased brightening has been shown to have
contributed to surges in crop yield growth (Tollenaar et al., 2017 and Proctor, 2021).
Temperatures affect the demand for energy needed for heating or cooling and thereby
may drive up consumer prices for energy. Energy and food are both essential inputs in
the production of various goods and services, and any upward shifts in their prices can
potentially trigger cascading effects.
1There is no widespread agreement regarding the relation between climate change and wind speeds.
However, IPCC (2021) estimates that climate change will reduce average wind speeds in Europe by up
to 10%.
3

Even if ambitious climate policies manage to keep global warming below 1.5 ◦C until
the end of the century (which seems an overly optimistic assumption at the current
juncture), we need to understand and adapt to the damage already caused. To this end,
it is important to understand the direct short-term as well as potential medium to long-
term effects of the different dimensions of climate change on prices. The contribution of
this paper is twofold. First, we contribute to the empirical discussion on the impact of
weather shocks on consumer price inflation; and second, we show how to use the extensive
information of time-series data for geolocations to study the impact of climate change on
inflation.
For the first part, we set out to answer the following questions: What is the impact of
weather anomalies on consumer prices in the euro area and which sectors of the economy
are affected most? What is the delay and duration of the impact? What kind of weather
events have the strongest impact on inflation and how do different weather events interact
with each other? How important are non-linearities regarding the size, sign, timing, loca-
tion and size of the area of the shock? How heterogeneous is the impact across countries
and are there spillovers from one region to another? In addition to including a larger
variety of climate-related indicators, we also study the effects at a particularly disaggre-
gated level. Faccia et al. (2021) argue that aggregation across time results in a loss of
information. To limit the amount of information loss we use monthly price data for the
20 euro area countries including consumer prices as measured by the harmonised index
of consumer prices (HICP) at the European classification of individual consumption ac-
cording to purpose (ECOICOP) 4 digit level2. Climate data is taken from the Copernicus
database3 and includes detailed data on temperatures, precipitation, solar radiation, and
wind speed.
In a first step, we estimate the impact of different weather variables (using monthly
country averages) on sectoral consumer price inflation via local projections. The impulse
response functions of a change in the deviation of different weather variables from their
historical means on subsector inflation rates, show that there is substantial heterogeneity
across sectors, countries and timing. While temperature has the largest impact, other
climate variables matter as well - particularly at the subsector level. We also confirm the
2https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Glossary:
Classification_of_individual_consumption_by_purpose_(COICOP)
3https://www.copernicus.eu/en/access-data
4

presence of non-linearities by showing that the magnitude and the sign of the weather
shocks matter, and again these effects are highly heterogeneous across subsectors and
countries. Seasons crucially shape the (dis-)inflationary impacts of weather shocks. While
hot summers exert significant upward price pressures in the food sector, a mild autumn
or winter has disinflationary effects on energy prices. Besides this, we find that the results
crucially depend on the choice of the control variables included in the analysis.
In the second step of our study, we expand our analysis by replacing country-level
climate data averages with surface climate data. Conventional tools typically utilised for
climate data processing can be overly restrictive, as they do not adequately capture the
intricate nature of these datasets, leading often to information loss due to aggregation
or other simplifications. By employing novel techniques from functional data analysis
we can treat climate data, collected sequentially over time, as a surface (functional)
time series with a predefined geographical domain. Furthermore, we propose a new
statistical methodology to study potential relationships with such complex data sets and
extract common factors. Our method is based on the adaptation of conventional canonical
correlation analysis (CCA) to high-dimensional and infinitely-dimensional settings.
The remainder of the paper is structured as follows. Section 2 reviews the related
literature. In section 3 the data are described. The results for impact of weather shocks
on sectoral inflation in a low-dimensional setting are summarized in section 4. Section 5
describes how to relate high and infinite-dimensional data sets and estimate the impacts
of weather shocks using surface-time series data. Finally, section 6 concludes. All proofs
are relegated to the appendix.
2 Literature review
Studies on the economic consequences of climate change frequently focus on the impact
of natural disasters on economic growth and are often limited to the “Big Four”: floods,
droughts, windstorms and earthquakes; see e.g. ? and Kousky (2014). Natural disasters
tend to reduce economic activity, particularly in developing economies. They may cause
negative supply-side shocks by destroying harvests and infrastructure (Batten et al., 2020
and Simola, 2020) and consequently raise the costs of production and/or imports. Re-
construction efforts may stimulate demand and thereby raise the prices of reconstruction
5

goods. At the same time, the destruction of wealth may dampen inflation through its
negative impact on consumption and investment. Weather shocks can affect global food
commodity prices (see e.g. Marini, 2020 or Ta¸ skin et al., 2021) and thereby not only
impact economic growth but also increase the risk of conflict (see e.g. De Winne and
Peersman, 2021a,b). It is again the developing countries that are affected most (Ciccarelli
and Marotta, 2021). Similarly, Dell et al. (2012) find that higher temperatures reduce
economic growth particularly in poor countries. Not only growth rates, but also the level
of output can be affected. Additionally, higher temperatures lower agricultural output,
industrial output, and may negatively affect political stability. Beyond the impact of
changes in average temperatures, empirical evidence suggests that weather anomalies ( ?)
or extreme precipitation (Kotz et al., 2022) dampen economic growth, and that most of
these impacts are likely non-linear (IPCC, 2022b). This is in contrast to the findings of
Deschˆ enes and Greenstone (2007), who find variation in temperature and precipitation
will increase agricultural profits.
Empirical evidence on the impact of weather or climate change on consumer prices
is currently an active field of research. Mukherjee and Ouattara (2021) use a panel-
V AR with fixed-effects to show that temperature shocks lead to inflationary pressures.
These effects can persist several years after the shock, particularly in developing coun-
tries. Dafermos et al. (2021) provide empirical evidence that natural disasters lead to
increases in headline and core inflation in the euro zone. Overall, the effects are small
but significant, with food and beverages showing the highest price increases. Moreover,
the authors find substantial heterogeneity across the euro zone. More recently, a few
studies looked at the impact of extreme temperatures on inflation. Faccia et al. (2021)
find that high temperatures tend to increase inflation in the short-run and decrease it
in the medium term. Emerging economies are affected more than advanced economies.
Hot summers show the largest and most persistent impact on inflation, particularly on
the prices for food. Additionally, the effect of climate change on prices is non-linear.
Recently ? analyse the impact of weather shocks on inflation components in the four
largest euro area economies combining high-frequency weather data with monthly in-
flation. The results suggest significant country asymmetries and seasonal responses of
inflation to temperature shocks, mainly via food, energy, and service prices. An increase
in monthly mean temperatures has inflationary effects in summer and autumn, with a
6

stronger response in warmer euro area countries. An increase in temperature variability
has significant upward inflationary impacts. In both ? and Faccia et al. (2021), weather
shocks are defined as deviations from historical averages. Natoli (2023) proposes a dif-
ferent way to construct temperature shocks using county-level data for the US taking
into account temperature shocks that agents anticipate based on past temperature real-
izations. That is, temperature beliefs reflect some learning behavior. In this framework,
temperature surprises dampen aggregate demand by reducing GDP, consumer prices and
interest rates.
Only few papers consider weather variables other than temperatures. One of these is
Moessner (2022) who use dynamic panel data methods for the estimation of food CPI
Phillips curves augmented with climate variables. Precipitation has significant non-linear
effects on food inflation with inflation increasing as precipitation becomes either very low
or very high. Moreover, temperature has no additional explanatory power for food CPI
inflation. Kotz et al. (2023) also consider temperature and precipitation by calculating so
called Standardised Precipitation Evapotranspiration Indices (SPEI) that model dry and
wet conditions. Additionally, they combine their results with projections from physical
climate models to estimate the inflationary impacts caused by future warming. They
identify deviations of monthly mean temperature and daily temperature variability, as
well as excess wet and drought conditions and extreme daily rainfall as the main impact
channels. Taking into account different weather variables is important to obtain unbiased
estimates. For example, temperature and precipitation are historically correlated and this
correlation may be location specific (see Auffhammer et al., 2013).
In the majority of the papers mentioned above weather variables are aggregated across
space (and often time). Weather data, however, is available at a high resolution (and
high frequency) and falls into the category of “big data”. As we propose a method for
leveraging the information from this data, our paper is also related to the field of big
data or high-dimensional data analysis with a particular focus on the use of surface time
series data. To describe and model the relationship between sectoral inflation rates and
weather, we use techniques from canonical correlation analysis (CCA). CCA is a family
of methods that is commonly used to measure the linear relationship between two groups
of multidimensional variables (see e.g. Hotelling (1936) or H¨ ardle and Simar (2007)).
In high-dimensional settings, identifying the canonical variables is impossible, when all
7

dimensions are large (see Bykhovskaya and Gorin (2023)). Therefore, in applications
with high-dimensional data, a regularized modification of CCA is commonly used (see
e.g. Tuzhilina et al. (2020)).
3 Data
Data on consumer prices is taken from Eurostat and includes monthly inflation rates
of the HICP starting from January 2001 until December 2021 for 89 (sub)sectors. The
items in the HICP are classified according to ECOICOP. We focus on the four main
aggregates (energy, food, services and non-energy industrial goods), and their subsectors
at ECOICOP 3 and 4 digit level. As can be seen in Figure 1, inflation rates (measured
as year-on-year changes in percent) in the euro area varied considerably across the 89
sectors.
Figure 1: Range of inflation rates in the euro area: The blue line shows the lowest inflation
rate and the yellow line the highest inflation rate across 89 subsectors in a given month.
Climate data is taken from the Europe-wide E-OBS 4 dataset which consists of daily
interpolations of mean temperature, minimum temperature, maximum temperature, pre-
cipitation, solar radiation, wind speed, humidity and mean sea-level pressure. Addition-
ally, various other indicators and indices, such as e.g., the number of tropical nights
4We acknowledge the E-OBS data set from the EU-FP6 project UERRA ( https://www.uerra.eu)
and the Copernicus Climate Change Service, and the data providers in the ECA&D project ( https:
//www.ecad.eu and https://surfobs.climate.copernicus.eu/dataaccess/access_eobs.php).
8

or heating degree days, are available. For the subsequent analysis we include daytime
temperatures (average, minimum and maximum), precipitation, wind speed and solar
radiation. The E-OBS data set is an ensemble data set, i.e., a climate data set that
consists of a number of equally probable realizations. The mean across the members is
calculated and is provided as the “best-guess” fields, which is the data we use in our
analysis. The data covers the period back to 1950 (except for wind speed which starts in
1980) and is available as gridded fields at a spacing of either 0 .1 × 0.1 or 0 .25 × 0.25 in
regular latitude/ longitude coordinates. We use the 0 .25 × 0.25 spacing which is roughly
equivalent to 25km × 25km. The usual approach in the production of a gridded data set
is to determine the most likely values to interpolate station values to values on a regular
grid. Data is available for entire Europe although station density varies across time and
geographical locations. No homogeneity corrections are applied to the station data. For
more detailed information on the construction of the ensemble data set see Cornes et al.
(2018). We use the period from 1950-1980 as a reference period and calculate the monthly
mean for each month of the year based on the daily mean weather variables of the E-OBS
data set. Then we compare these values to our period of interest 2001-2021. 5
By averaging over space we can neither capture whether different regions are affected
differently by weather shocks, nor can we understand whether these differences matter
for consumer prices - which would be important to quantify climate-related risks for price
stability. As can be seen from Figure 2, both average mean temperatures in the reference
period (1950-80) as well as average deviations in the last two decades varied considerably
across the euro area. The average deviation from the historical mean ranges from 0 .5◦C
to 3◦C, with the highest deviations in the southern and central regions of the euro area.
Particularly in the larger (southern) countries such as Spain and Italy deviations from the
historical mean vary markedly across regions. Moreover, the deviation from the historical
mean is not uniform throughout the year. On average, deviations are highest in spring
and lowest in autumn. Table A.1 in the appendix shows the average yearly deviation
from the historical mean for different euro area countries and weather variables.
5Appendix A provides a description of the steps involved in obtaining the underlying climate data
set for the subsequent analysis.
9

40°N
50°NLatitude
10°W  0° 10°E 20°E 30°E
Longitude
Historical Mean Surface for 50-80s
Esri, HERE, Garmin, USGS
 500 mi
 500 km
 -2
0
2
4
6
8
10
12
14
16
40°N
50°NLatitude
10°W  0° 10°E 20°E 30°E
Longitude
Deviation from the Mean Surface in 2001-2021
Esri, HERE, Garmin, USGS
 500 mi
 500 km
0.5
1
1.5
2
2.5
3
Figure 2: Left Panel: the surface of historical average temperature for the period from
1950 to 1980; Right Panel: average deviation from the historical mean surface for the
period from 2001-2021
4 Weather Impact on Sectoral Inflation: Local Pro-
jections in a Low-Dimensional Context
To set up a benchmark, we estimate the impact of different weather variables on prices
in each sector separately using euro area averages for all variables considered. The effects
are measured by impulse response functions (IRFs) derived from local projections. In
the simplest (linear) form, we estimate the following model for each forecast horizon
h = 0, 1, 2, ...,24,
ys,t+h = αh 0 +
pX
k=1
Ah kys,t−k +
rX
i=0
Bh i xt−i +
lX
j=1
C h j zs,t−j + et+h, (1)
where ys,t is a vector of endogenous variables including year-on-year inflation rates of
consumer and producer prices of sector s, (euro area) commodity prices and industrial
production.6 This means that we implicitly assume that there is no contemporaneous
relationship between the elements of ys,t. We consider up to p lags of the endogenous vari-
ables, where the lag length p is determined using the Akaike information criterion (AIC)
and is therefore sector-specific. xt is the vector of weather shocks that may contempo-
raneously impact prices, and zs,t is a vector of control variables which includes weather
6Appendix A provides a detailed description of the variables used and their respective transformations.
In the subsector analysis the level of disaggregation might differ for the different variables included in
ys,t.
10

variables other than the one(s) included in xt7 and possibly relevant commodity prices
(e.g. oil prices) so that zs,t is also sector-specific. The lag length l is again determined by
the AIC and may therefore depend on the sector being studied. et+h are the innovations.
The impulse response function of the endogenous variable at horizon h to a change in
weather is computed as,
∂ys,t+h
∂xt
= Bh 0 . (2)
For country-specific analysis we slightly modify (1) by replacing the variables in yt,s
and xt,s by their respective country counterparts. Depending on the country of interest,
commodity prices are considered to be exogenous if the country is sufficiently small. Given
the results of ? (see also Ahmadi et al., 2022), we do not consider a panel setting, as
countries even within the euro area seem to be heterogeneous in terms of their exposition
and reaction to climate shocks; see e.g. Kotz et al. (2023) and Faccia et al. (2021) for
the impact of climate shocks in a panel framework.
4.1 The definition of a weather shock
A shock is defined as the deviation from the historical mean, where the latter is computed
as the monthly average of the period from 1950 to 1980 and is depicted in Table 1.
Table 1: Historical mean (1950-1980) for average daytime temperature (in ◦C), precip-
itation (in mm/m2), solar radiation (in W/m2) and wind speed (in m/s) for the euro
area.
Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
Temperature -0.6 0.2 3.2 7.0 11.7 15.9 18.1 17.5 14.0 9.3 4.4 1.0
Precipitation 1.9 1.9 1.7 1.7 1.8 2.0 1.8 1.9 2.0 2.1 2.4 2.2
Solar radiation 49 78 127 180 230 246 246 214 156 99 57 42
Wind speed 0.08 0.08 0.1 0.09 0.09 0.09 0.08 0.08 0.07 0.09 0.1 0.1
As shocks we only consider values that exceed a certain threshold, namely the average
deviation in the period 2001-2021 from the historical mean. Table A.1 in the Appendix
shows these threshold values. For instance, for the euro area, we study the impact
of deviations from historical mean temperatures exceeding 1.3 ◦ Celsius. Furthermore,
7Similarly to Kotz et al. (2023), we use several combinations of different weather shocks and control
for all weather variables.
11

empirical evidence highlights the importance of non-linearities in the impact of climate
shocks. Hence, we consider several extensions to the baseline model. First, we study
seasonal effects by isolating the impact of a weather shock on consumer prices for the four
seasons of the year (spring (March-May), summer (June-August), autumn (September-
November) and winter (December-February)). Second, we analyze whether consumer
prices react differently to positive and to negative shocks. Third, we study extreme
events by considering weather shocks that exceed a certain size in magnitude. Finally,
different combinations of these non-linearities are explored.
4.2 Empirical results: strongest impact on food and energy
We start by calculating the average impact of a weather shock on HICP inflation in
89 subsectors for the euro area. We compare different specifications as far as weather
variables and oil prices are concerned, but always include producer prices (except for the
services sector), industrial production and commodity prices. The impact on inflation
rates varies considerably across subsectors with the effect on aggregate inflation measures,
such as food, energy, services and non-energy industrial goods being muted. Figure 3
shows the impact of a deviation from the historical mean for different weather variables for
the euro are in percentage points up to 24 months after a shock. For all weather variables
except minimum temperature, the impact on headline inflation (CP00) is statistically
significant, but small. Only average temperature shocks have disinflationary impacts,
while higher wind speeds, solar radiation or precipitation tend to raise inflation in the
months after the shock. Energy consumer prices react more strongly than food prices to
weather shocks, while core inflation (services and non-energy industrial goods) is barely
affected by weather anomalies.
12

(a) Temperature
 (b) Precipitation
(c) Minimum Temperature
 (d) Maximum Temperature
(e) Wind Speed
 (f) Solar Radiation
Figure 3: Impact of a deviation from the historical mean on special aggregates and
headline inflation (CP00) in percentage points for the euro area in the 24 months after
the weather shock.
13

While the impact on inflation rates is small if we focus on the four special aggregates,
certain subsectors are considerably affected. The effects are heterogeneous across sectors
and in the aggregate often offset each other or become negligible. Similarly, the time
lag with which shocks impact consumer prices varies markedly across subsectors. Most
effects are observed after 6 to 15 months, but in some subsectors such as non-alcoholic
beverages or fuels, we also find short-term effects. Figure 4 illustrates some of the results
by showing the effects of a precipitation shock on the inflation rates of all sectors related to
food including alcohol and tobacco. The strongest impact is observed in category CP0116
- fruits, but we also find inflationary effects on the inflation rate of wine (CP0212) or
milk products (CP0114).
Figure 4: Average impact of a precipitation shock on euro area HICP inflation rates
in the food sector measured in percentage points (90% confidence interval). The x-axis
shows the horizon in months and the y-axis the different food (sub-)sectors. Controls:
Temperature, wind speed, oil prices.
In Appendix B we present more detailed figures for different combinations of sectors,
weather shocks and control variables. The results show that the effects depend heavily
on the choice of the control variables that are included in the analysis. For the food
sector, for example, we find that the effects on food inflation can be positive as well as
negative depending on the choice of control variables. Another interesting observation
can be made when comparing the effects of temperature deviations. For energy, for
instance, deviations in minimum or maximum temperatures have inflationary effects,
whereas shocks to average temperature deviations have a negative impact on energy
14

inflation.
4.2.1 Negative shocks
So far, we showed the results for positive deviations from the mean such as unusually high
temperatures or precipitation. Figure 5 shows the effects of a negative weather shock for
average daytime temperatures and for precipitation. The impact on headline inflation is
small and negative. A comparison to figure 3 shows that the effects differ considerably
from the ones we observe when the shock is positive. This difference is not simply in
terms of the sign, but also in terms of sectors, timing and magnitude of the effect. This
confirms that weather anomalies impact consumer prices in a non-linear fashion.
(a) Temperature
 (b) Precipitation
Figure 5: Impact of a negative deviation from the historical mean on special aggregates
and headline inflation (CP00) in percentage points for the euro area.
4.2.2 Seasonal effects
Figures 3 and 4 show the average impact throughout the year. However, the timing of
a weather shock strongly influences its impact on prices, as can be seen in Figure 6.
A temperature shock in summer lifts consumer price inflation for food in the months
following the shock, while a shock in winter has a negative impact. In spring and autumn
the impact changes from negative in the short run to positive in the medium run. If
we compare these findings to Figure 3a, we see that the overall impact of a temperature
shock on food prices being insignificant is a result of countervailing impacts across the
different seasons.
15

Figure 6: Seasonal effects of a temperature shock on food inflation.
4.2.3 Geographical heterogeneity
Focusing on euro area aggregates conceals a large heterogeneity across countries. Not
only do countries differ in terms of their exposure to weather shocks and climate change,
also differences in economic structures may amplify or dampen the impacts on consumer
prices. Figure 7 depicts the reaction of energy inflation across various euro area member
states to a temperature shock in summer. In some countries this shock is inflationary,
in others disinflationary. Similarly the timing and the size of the impact vary markedly.
Differences in the energy mix or price setting mechanisms in the energy markets (incl.
taxation or subsidies by national governments) might be responsible for the large hetero-
geneity together with climatic differences.
16

Figure 7: Impact of a temperature shock in summer on energy inflation in different euro
area countries.
The preceding subsections underscored the significant heterogeneity in the impact
of weather on inflation rates across subsectors, seasons, and countries. However, when
aggregating over sectors, time, or regions, valuable information about the economic con-
sequences of extreme weather events is lost. In the next section, we propose a method to
extract the relevant information from the surface data for our analysis.
5 Relating high and infinite-dimensional data: Asso-
ciated factors
Understanding and modelling relationships between changes in price indices and changes
in climate variables presents significant challenges. With price indices consisting of 89
different sectors and climate data treated as time series of surfaces, which implies infi-
nite dimensionality, it can be difficult to identify and quantify patterns or relationships
between these data sets. Complications are further amplified by the fact that not all
indices may be affected, only a subset of them. Furthermore, not all information carried
by climate variables is relevant for price developments. Thus, how can we identify the
“relevant” part? To understand and model the relationships between these two data sets,
we first identify the parts in both data sets that relate to each other. In what follows
we will refer to these as associated factors. Once identified, appropriate methodological
techniques have to be developed to extract and estimate the associated factors from both
17

data sets, and provide a subsequent analysis. For the latter, we propose a generalized
impulse-response analysis that enables us to exploit the geographical aspect of the climate
data.
To offer an intuitive explanation of the methodology, we start our discussion with an
informal description of the problem. We have one finite-dimensional variableY , represent-
ing changes in fixed and finite number of consumer prices, and one infinite-dimensional
variable X, representing changes in a climate variable. We are interested decomposing Y
and X such that
Y = ˜Y + Y ⊥ and X = ˜X + X ⊥, (3)
where ˜Y and ˜X represent the parts referred to as associated factors, encapsulating the
essence of the relationship between X and Y, whereas Y ⊥ and X ⊥ are irrelevant for
describing this relationship. These associated factors can then in a second step be used
for a (linear) structural representation, which may be of interest for a subsequent analysis.
This representation is given by
˜Y = Π

˜X

+ e, (4)
where e is an idiosyncratic error term. In Section 5.2, we show how representation (4)
is used to construct functional impulse-responce analysis (FIRA). The term “functional”
refers here to the nature of climate variables that are treated as surfaces. FIRA allows
us to control for the magnitude of the shock as well as for its geographical location and
size of the area.
5.1 Identification of Associated Factors
In the case when both X and Y are finite dimensional, the solution to the problem
(3)-(4) is well-known and can be derived through canonical correlation analysis (CCA).
CCA is a widely-used method in conventional (finite-dimensional) settings for analyzing
linear associations between two datasets, as initially formulated in a seminal work by
Hotelling (1936). However, extending this methodology to our problem is challenging,
primarily due to the infinitely dimensional nature of the variables representing climate
conditions. To explain the complexities introduced by this characteristic and to provide
insights into our solution, we begin by describing the case where both sets of variables
are finite-dimensional.
18

The finite-dimensional case
Consider two random vectors Y and X in Rp and Rq, respectively. The problem of finding
the associated factors as in (3) can be formulated as finding the pairs of directionsai ∈ Rp
and bi ∈ Rq, for i = 1, ..., K≤ min(p, q), across which Y and X have nonzero covariances.
That is,
Cov (⟨ai, Y⟩⟨bi, X⟩) ̸= 0, (5)
where ⟨., .⟩ denotes the inner product (or the scalar product) on Rp or Rq and can be
interpreted as a projection of Y into ai (or X into bi)8. Furthermore, pairs ( ai, bi) are
selected in a meaningful way, such that, the correlation between ⟨ai, Y⟩ and ⟨bi, X⟩ is
maximized and each pair ( ai, bi) is orthogonal to ( aj, bj) for i ̸= j. Here orthogonal-
ity is defined as Cov (⟨ai, Y⟩)⟨bj, X⟩) = Cov (⟨ai, Y⟩)⟨aj, Y⟩) = Cov (⟨bi, X⟩)⟨bj, X⟩) =
Cov (⟨bi, X⟩)⟨aj, Y⟩) = 0. From this we obtain the structural relationship between Y and
X as,
˜Y = Π ˜X + e, (6)
where ˜Y = [⟨a1, Y⟩, ...,⟨aK, Y⟩]′, ˜X = [⟨b1, X⟩, ...,⟨bK, X⟩]′, Π = diag(ρ1, ..., ρK) and ρk
denotes the correlation corr(⟨ak, Y⟩⟨bk, X⟩). The error term e is a (K ×1) vector of errors
that is uncorrelated with ˜X.
In other words we are searching for solutions {ρk, ak, bk}K k=1 that solve the maximiza-
tion problem,
ρk = max
˜ak∈Rp , ˜bk∈Rq
corr(⟨˜ak, Y⟩⟨˜bk, X⟩), (7)
subject to the orthogonality condition on{ak, bk}K k=1.9 The solution to these maximization
problems is found through the singular-value decomposition (SVD) of the correlation
operator (see, for instance, Johnson and Wichern, 2002)
M = C −1/2 X CXY C −1/2 Y , (8)
where CX = V ar[X], CY = V ar[Y ] and CXY = Cov [X, Y]. The SVD yields a set of
singular value triplets {ρk, fk, gk}K k=1, where , C −1/2 X CXY C −1/2 Y (fk) = ρkgk. Furthermore,
8Here, with the small abuse of notation, we use the same symbol for the inner product on Rp and Rq.
9We first maximize among all choices in Rp and Rq to find a1 and b1. To find a2 and b2 subject to
the orthogonality restriction implies maximization among all choices in Rp and Rq orthogonal to a1 and
b1. This results in ρ2 ≤ ρ1 as ρ2 is the maximum over a smaller subspace. By continuing this process
we can find K ≤ min(p, q) couples.
19

ρk is the solution to the maximal correlation problem in (7) and the corresponding direc-
tions are given as ak = C −1/2 Y fk and bk = C −1/2 X gk, for k = 1, ..., K. Once all K couples,
{ak, bk}K k=1, are found we can rewrite the original two sets of variables as,
Y =
KX
k=1
⟨ak, Y⟩ak + Y ⊥ and X =
KX
k=1
⟨bk, X⟩bk + X ⊥,
where Y ⊥ is the part of Y that is uncorrelated with X and X ⊥ is the part of X that is
uncorrelated with Y . Hence, PK i=1⟨ai, Y⟩ai and PK i=1⟨bi, X⟩bi are identified, respectively,
as the associated factors, ˜Y and ˜X, described in (3). Furthermore, they can be written
in the structural form (6).
Mix of Finite and Infinite Dimensional Variables
In the context of our application X represents a climate variable (e.g. average daytime
temperature) which we treat as a surface over the geographical domain of the euro area.
From a technical perspective, these surfaces are functions within a well-defined functional
space, implying that, in general, they are infinitely-dimensional objects. The primary
challenge in extending finite-dimensional Canonical Correlation Analysis (CCA) to our
case arises from the fact that the counterpart of the covarianceCX in (8) is not invertible,
constituting what is known as an ill-posed inverse problem. Therefore, the first crucial
point is to verify the existence of associated factors. Second, in empirical applications,
some form of regularization of the problem is required to derive an appropriate estimator.
To prove the existence of associated factors, we adapt the results available in the func-
tional data analysis on CCA. He et al. (2003) considers an extension of CCA to the case
when data samples consist of pairs of square integrable stochastic processes. The authors
derive conditions on the dependence between Y and X (see He et al., 2003, Condition
4.5) to ensure the existence of the correlation operator in (8). An alternative approach
proposed in Eubank and Hsing (2008) transforms the functional CCA problem into find-
ing so-called canonical functions in the reproducing kernel Hilbert space generated by
the corresponding covariance functions. Kupresanin et al. (2010) provides a theoretical
comparison of both approaches. We use tools from both papers to derive a sufficient
condition under which associated factors exist and are well defined.
When X, Y and the associated factors are infinite-dimensional, the ”regularization”
20

of the problem cannot be avoided. This point is also stressed in Leurgans et al. (1993).
However in our case, the regularization can circumvented, since Y is finite dimensional
and therefore the associated factors are finite dimensional by construction. This leads to
the fact that both operators M and CY Xare finite dimensional and SVD of both produces
right and left singular vectors that span the same subspaces (provided that M exists and
is well defined). That is, {αi, βi}K i=1, extracted from SVD of CXY generate subspaces
Ωα = span{α1, ..., αK} and Ω β = span{β1, ..., βK}. These subspaces are identical to the
corresponding subspaces produced by the solutions to the maximum correlation problem,
Ωa = span{a1, ..., aK} and Ωb = span{b1, ..., bK}. This in turn implies that projections of
the original Y and X into Ωα = span{α1, ..., αK} and Ωβ = span{β1, ..., βK} allow us to
extract common factors as ˜Y = PK k=1⟨αk, Y⟩αk and ˜X = PK k=1⟨βk, X⟩Hβk. As a result we
obtain a simple and straightforward approach to identify and estimate associated factors
based on the SVD of CY X rather than the SVD of M which involves inverses of CX and
the consequent estimator regularization. Furthermore, to construct a structural model as
in (4) we can first extract projections ˜YK and ˜XK as described above and then perform
the conventional CCA on these elements as they are finite-dimensional by construction.
This result is formalized below.
To define and derive the associated factors additional notation is required. We work
with two random variables, Y and X, that take values in Rp and in H ≡ L2(∆, ⟨, ⟩H),
respectively. Here H is the space of square-integrable real-valued functions, which is
equipped with the standard inner product ⟨x, y⟩H =
R
∆ x(u)y(u)du, and ∆ ⊂ R2 is the
domain of functions on H that is associated with the geographical restrictions of the
data (i.e., geographical area of euro zone). Since associated factors are determined solely
by the covariance structure, we define the following covariance operators for x ∈ H and
y ∈ Rp,
CX(x) = E [⟨X, x⟩HX] ; CXY (x) = E [⟨X, x⟩HY ] ;
CY X(y) = E [⟨Y, y⟩X] ; CY (y) = E [⟨Y, y⟩Y ] .
Furthermore, CX : H → H, CY : Rp → Rp, CXY : H → Rp and CY X: Rp → H and each
21

of them admits the spectral decomposition:
CX(x) =
∞X
i=1
λi⟨x, ϕi⟩Hϕi;
CY (y) =
pX
j=1
γj⟨x, ψj⟩ψj;
CY X(y) =
KX
k=1
rk⟨y, αk⟩βk.
The associated factors ˜Y = PK k=1⟨ak, Y⟩ak and ˜X = PK i=1⟨bi, X⟩bi are defined through,
(ρk, ak, bk)K k=1, the solution to the maximization problem
ρk = sup
a∈Rp , b∈H
Cov(⟨a, Y⟩⟨b, X⟩H), for k = 1, ..., K (9)
subject to V ar(⟨a, Y⟩) = 1 and V ar(⟨b, X⟩H) = 1 and orthogonality condition between
couples (ai, bi) is orthogonal to ( aj, bj) . Finally, we define the covariance operators for
˜Y and ˜X as ˜CX(x) = E
h
⟨ ˜X, x⟩H ˜X
i
, ˜CY (y) = E [⟨Y, y⟩Y ] and ˜CY X(y) = E
h
⟨ ˜Y , y⟩ ˜X
i
=
CY X(y).
Theorem 1. Under the regularity condition
∞X
i=1
λ−1 i E[⟨X, ϕi⟩H⟨Y, ψj⟩] < ∞ for all j, (10)
we have that
(i) the solution{ρk, ak, bk}K k=1 to maximization problem(9) exists and is expressed through
SVD {ρk, fk, gk, }K k=1 of the operatorC −1/2 X CXY C −1/2 Y for k = 1, ..., Kas
{ρk, C−1/2 Y (fk), C−1/2 X (gk)}K k=1,
where C −1/2 X CXY C −1/2 Y (fk) = ρkgk.
(ii) span{a1, ..., aK} = span{α1, ..., αK} and span{b1, ..., bK} = span{β1, ..., βK};
(iii) the solution, (ρk, ak, bk)K k=1, can be equivalently obtained from SVD of the operator
C −1/2 ˜X C ˜X ˜Y C −1/2 ˜Y .
22

Theorem 1 solves several important issues in identifying associated factors and the
structural representation of their relationship. First, the existence of the associated fac-
tors, challenged by the ill-posed inverse problem on CX, is obtained under the regulatory
condition (10). This condition ensures that the range of the operator CY Xis in the range
of the operator C 1/2 X , which in turn implies that the operator C −1/2 X CXY C −1/2 Y is well
defined. Further technical discussion on the role of (10) is given in the remark below.
Second, Theorem 1 shows in item (ii) that the associated factors, if they exist, can be
obtained from projecting into Ω α = span{α1, ..., αK} and span{β1, ..., βK} (instead of
span{a1, ..., aK} and span{b1, ..., bK}). Finally, the synthesis of items (ii) and (iii) of-
fers a rationale for an alternative approach to acquiring the structural representation of
the relationship. This involves projecting the original variables into Ω α and Ωβ, thereby
diminishing the dimensionality of the original variables and eliciting associated factors.
Subsequently, employing CCA on these associated factors yields the desired structural
representation.
5.2 Functional Impulse-Response Analysis
The structural representation in (6) serves as the primary building block in the subsequent
analysis. In this section, we utilize it to construct a functional impulse-response analysis
(FIRA). To this end, we have discussed the identification of associated factors from one
finite and one infinite-dimensional dataset. Now, we incorporate the time series feature of
the data into our analysis. Let Yt ∈ Rp denote a vector of price changes at time t, Xt ∈ H
is an exogenous climate shock at time t. We may be interested in including additional
control variables in our analysis, such as lags ofYt, lags of Xt or other climate variable(s) as
well as economic variables and their lags, which we denote as Zt ∈ HZ ≡ L2(∆Z, ⟨, ⟩H).10
Let Vt denote the collection of all relevant variables i.e.,
Vt = [Xt, Xt−1, ..., Xt−q, Yt−1, ..., Yt−s, Zt−1, Zt−l] .
In what follows we assume that all variables are weakly (covariance) stationary. To
construct functional impulse-responses we extract associated factors between Yt and Vt−h
10An additional climate variable is not necessarily required to be defined over the same geographical
area as Xt. However, it is essential that it belongs to the space of square-integrable functions with the
standard inner product.
23

Figure 8: Functional Impulse-Response Analysis to 1.5 ◦C Temperature Shock in the North-East of
Germany.
with h = 0, ..., hmax. That is, for each horizon h we construct {ρ(h) k , a(h) k , b(h) k }Kh k=1 and
˜Yt = Πh ˜Vt−h + et,
where Πh = diag(ρ(h) 1 , ...ρ(h) Kh). The triplet {Πh, a(h) k , b(h) k }Kh k=1 defines FIRA and can be
seen as a generalization of the classical impulse-response analysis obtained via local pro-
jections. To be more precise, it allows us to operate with a generalized concept of a
weather shock, where we control not only for the magnitude of the shock (e.g., 1 .5C ◦ de-
viation from the historical mean) but also for its geographical attributes such as location
and coverage area. For instance, Figure 8 plots the FIRA of a temperature shock on 80
sectors of the German economy. The temperature shock, plotted on the left panel, has
the following attributes: magnitude - 1 .5C ◦; located Noth-East of Germany and covering
an area with a radius of 150 km which corresponds to approx. 70700 square kilometers.
6 Discussion
The impact of climate change on consumer prices is a complex and multifaceted issue,
as highlighted in this article. Its impact is heterogeneous across regions and sub-sectors,
and is influenced by various weather variables with differing magnitudes, directions, and
timing. Moreover, in the aggregate some of these effects offset each other or become
24

negligible. This does not mean that the heterogeneity and complexity of these effects is
not important for future price developments.
One crucial aspect to consider is the distinction between demand-driven and supply-
driven effects. Certain weather events may lead to changes in consumer behavior and
preferences, creating shifts in demand for specific goods and services. Simultaneously,
other effects may disrupt the production and supply chains, resulting in fluctuations
in the availability and cost of products. These supply-demand imbalances need to be
carefully assessed and monitored as they may potentially create bottlenecks and lead to
more widespread price pressures.
Additionally, the dynamic nature of relative prices in response to climate change
should not be overlooked. As some sectors and regions are more susceptible to climate-
related risks than others, relative prices may fluctuate. This may impact consumers
differently across countries and across various categories of goods and services. Thereby
it may also affect inflation heterogeneity in the euro area. A higher frequency of extreme
weather events may also impact the volatility of inflation rates making it even harder to
predict future inflation developments.
Given the limitations outlined in this study, such as the focus on the euro area and
the relatively short time period considered for price data, it is essential to recognize that
the full extent of climate change’s impact on consumer prices may not be fully captured.
Other research has indicated that the impact in developing countries might be more
pronounced, underscoring the need for a comprehensive global perspective on this issue.
Furthermore, with the limitations of historical data, the analysis might not fully capture
long-term trends or account for the potential amplification of climate-related effects over
time.
In conclusion, it is crucial to harness all available information and consider climate
change in all its dimensions when evaluating its impact on consumer prices. This will
enable us to accurately identify potential areas where intervention may be necessary or
beneficial in a timely manner. As climate change continues to exert its influence on our
world, understanding its intricate relationship with consumer prices remains a critical
aspect of (monetary) policy-making.
25

References
Ahmadi, M., C. Casoli, M. Manera, and D. Valenti (2022, December). Modelling the
effects of climate change on economic growth: a bayesian structural global vector
autoregressive approach. Working Paper 46, FEEM.
Auffhammer, M., S. M. Hsiang, W. Schlenker, and A. Sobel (2013, May). Using Weather
Data and Climate Model Output in Economic Analyses of Climate Change. NBER
Working Papers 19087, National Bureau of Economic Research, Inc.
Batten, S., R. Sowerbutts, and M. Tanaka (2020). Climate change: Macroeconomic
impact and implications for monetary policy. In: Walker, T., Gramlich, D., Bitar, M.
and Fardnia, P. (eds.), Ecological, Societal, and Technological Risks and the Financial
Sector, New York et al.: Springer International Publishing. 17.
Bykhovskaya, A. and V. Gorin (2023). High-dimensional canonical correlation analysis.
arXiv . Submitted on 28 Jun 2023 (v1), last revised 20 Aug 2023 (this version, v2).
Ciccarelli, M. and F. Marotta (2021, October). Demand or supply? An empirical explo-
ration of the effects of climate change on the macroeconomy. Working Paper Series
2608, European Central Bank.
Cornes, R., G. van der Schrier, E. van den Besselaar, and P. Jones (2018). An ensemble
version of the e-obs temperature and precipitation data sets. Journal of Geophysical
Research: Atmospheres 123(17), 9391–9409.
Dafermos, Y., A. Kriwoluzky, M. Vargas, U. Volz, and J. Wittich (2021). The Price of
Hesitation: How the Climate Crisis Threatens Price Stability and What the ECB Must
Do about It; Final Report on Behalf of Greenpeace Germany. Number pbk173 (127) in
DIW Berlin: Politikberatung kompakt. DIW Berlin, German Institute for Economic
Research.
De Winne, J. and G. Peersman (2021a). The adverse consequences of global harvest and
weather disruptions on economic activity. Nature Climate Change 11, 665–672.
De Winne, J. and G. Peersman (2021b). The impact of food prices on conflict revisited.
Journal of Business & Economic Statistics 39(2), 547–560.
26

Dell, M., B. F. Jones, and B. A. Olken (2012). Temperature shocks and economic
growth: Evidence from the last half century †. American Economic Journal: Macroe-
conomics 4(3), 66–95.
Deschˆ enes, O. and M. Greenstone (2007). The economic impacts of climate change:
Evidence from agricultural output and random fluctuations in weather. The American
Economic Review 97(1), 354–385.
Eubank, R. and T. Hsing (2008). Canonical correlation for stochastic processes.Stochastic
Processes and their Applications 118(9), 1634–1661.
Faccia, D., M. Parker, and L. Stracca (2021). Feeling the heat: extreme temperatures
and price stability. Working Paper Series 2626, European Central Bank.
Felbermayr, G. and J. Gr¨ oschl (2014). Naturally negative: The growth effects of natural
disasters. Journal of Development Economics 111(C), 92–106.
Felbermayr, G., J. Gr¨ oschl, M. Sanders, V. Schippers, and T. Steinwachs (2022). The
economic impact of weather anomalies. World Development 151, 105745.
He, G., H.-G. M¨ uller, and J.-L. Wang (2003). Functional canonical analysis for square
integrable stochastic processes. Journal of Multivariate Analysis 85(1), 54–77.
Hotelling, H. (1936). Relations between two sets of variates. Biometrika 28(3/4), 321–
377.
H¨ ardle, W. and L. Simar (2007). Canonical correlation analysis. In Applied Multivariate
Statistical Analysis, pp. 321–330. Springer. CiteSeerX 10.1.1.324.403.
Johnson, R. and D. Wichern (2002). Applied multivariate statistical analysis(5. ed ed.).
Upper Saddle River, NJ: Prentice Hall.
Kotz, M., F. Kuik, E. Lis, and C. Nickel (2023). The impact of global warming on
inflation: averages, seasonality and extremes. Working Paper Series 2821, European
Central Bank.
Kotz, M., A. Levermann, and L. Wenz (2022, January). The effect of rainfall changes on
economic production. Nature 601(7892), 223–227.
27

Kousky, C. (2014). Informing climate adaptation: A review of the economic costs of
natural disasters. Energy Economics 46(C), 576–592.
Kupresanin, A., H. Shin, D. King, and R. Eubank (2010). An rkhs framework for func-
tional data analysis. Journal of Statistical Planning and Inference 140(12), 3627–3637.
Special Issue in Honor of Emanuel Parzen on the Occasion of his 80th Birthday and
Retirement from the Department of Statistics, Texas A&M University.
Leurgans, S. E., R. A. Moyeed, and B. W. Silverman (1993). Canonical correlation
analysis when the data are curves. Journal of the Royal Statistical Society. Series B
(Methodological) 55(3), 725–740.
Moessner, R. (2022). Effects of Precipitation on Food Consumer Price Inflation. CESifo
Working Paper Series 9961, CESifo.
Mukherjee, K. and B. Ouattara (2021). Climate and monetary policy: do temperature
shocks lead to inflationary pressures? Climatic Change 167(32), 1–21.
Natoli, F. (2023). The macroeconomic effects of temperature surprise shocks. Temi di
Discussione (Working Paper) 1407, Bank of Italy.
Parker, M. (2018). The impact of disasters on inflation. Economics of Disasters and
Climate Change 2, 21–48.
Proctor, J. (2021). Atmospheric opacity has a nonlinear effect on global crop yields.
Nature Food 2, 166–173.
Simola, H. (2020). CO2 emissions embodied in EU-China trade and carbon border
tax. BOFIT Policy Briefs 4/2020, Bank of Finland Institute for Emerging Economies
(BOFIT).
Ta¸ skin, D., E. C. Cagli, and P. E. Mandaci (2021). The impact of temperature anoma-
lies on commodity futures. Energy Sources, Part B: Economics, Planning, and Pol-
icy 16(4), 357–370.
Tollenaar, M., J. Fridgen, P. Tyagi, P. W. S. Jr, and S. Kumudini (2017, April). The con-
tribution of solar brightening to the US maize yield trend.Nature Climate Change 7(4),
275–278.
28

Tuzhilina, E., L. Tozzi, and T. Hastie (2020). Canonical correlation analysis in high
dimensions with structured regularization. arXiv . Submitted on 3 Nov 2020 (v1), last
revised 29 Jul 2021 (this version, v3).
29

A Appendix: Data preprocessing
Economic Data
All data are used in year-on-year growth growths unless explicitly stated otherwise. Sub-
sectors which do not have observations dating back to 2001 are removed for the analysis
in Section 5, but are included in sector by sector analysis of Section 4.
Climate Data
Several data preprocessing steps are necessary before the E-OBS data can be used in
our analysis. As the station density varies across time, we exclude all stations from the
dataset which have missing observations.
B Appendix: Figures and Tables
30

/0/1/2/3/4/5 /4/6/7/6/4/8 /9 /10/i255/12/8 /3/7/13/i255/5 /1/8 /14/2/3/6/4/8 /9 /15/i255/16/8 /1/i255/6/17 /2/i255/2/18 /1/8 /i255/7/1/2/7
/19 /20/2/1/7/21 /2/i255/2/16/16/2/3/6/i255/4/9 /i255/5 /2/1/3/2/9 /6/7/21 /2/i255/5 /8 /4/9 /6/15/10/i255/22 /23 /24 /i255/25 /26
/25 /8 /9 /6/1/8 /13/15/10/i255/27 /2/28/5 /2/1/7/6/18 /1/2/29/i255/30/4/9 /31 /29/i255/8 /4/13/i255/5 /1/4/3/2/15/32
/23/33
/33/34/35/36/37/38/39/40/22 /33 /23/33 /33/33 /34/33 /35/33 /36/33 /37/33 /38/33 /39/33 /40
/25 /0/23 /33 /33 /33
/25 /0/23 /33 /33 /34
/25 /0/23 /33 /33 /35
/25 /0/23 /33 /33 /36
/25 /0/23 /33 /33 /37
/25 /0/23 /33 /33 /38
/25 /0/23 /33 /33 /39
/25 /0/23 /33 /33 /40
/25 /0/23 /33 /33 /22
/25 /0/23 /33 /34 /33
/25 /0/23 /33 /34 /34
/25 /0/23 /34 /33 /33
/25 /0/23 /34 /33 /34
/25 /0/23 /34 /33 /35
/25 /0/23 /34 /34
/41/42/42/43
/0/1/2/3/4/5 /4/6/7/6/4/8 /9 /10/i255/12/8 /3/7/13/i255/5 /1/8 /14/2/3/6/4/8 /9 /15/i255/16/8 /1/i255/6/17 /2/i255/2/18 /1/8 /i255/7/1/2/7
/19 /20/2/1/7/21 /2/i255/2/16/16/2/3/6/i255/4/9 /i255/5 /2/1/3/2/9 /6/7/21 /2/i255/5 /8 /4/9 /6/15/10/i255/22 /23 /24 /i255/25 /26
/25 /8 /9 /6/1/8 /13/15/10/i255/27 /8 /9 /2/28
/23/29
/29/30/31/32/33/34/35/36/22 /29 /23/29 /29/29 /30/29 /31/29 /32/29 /33/29 /34/29 /35/29 /36
/25 /0/23 /29 /29 /29
/25 /0/23 /29 /29 /30
/25 /0/23 /29 /29 /31
/25 /0/23 /29 /29 /32
/25 /0/23 /29 /29 /33
/25 /0/23 /29 /29 /34
/25 /0/23 /29 /29 /35
/25 /0/23 /29 /29 /36
/25 /0/23 /29 /29 /22
/25 /0/23 /29 /30 /29
/25 /0/23 /29 /30 /30
/25 /0/23 /30 /29 /29
/25 /0/23 /30 /29 /30
/25 /0/23 /30 /29 /31
/25 /0/23 /30 /30
/37/38/38/39
Figure A.1: Precipitation: Local projections for the Euro Area (Food)
31

/0/1/2/3/4/5 /4/6/7/6/4/8 /9 /10/i255/12/4/9 /2/7/1/i255/13/8 /3/7/13/i255/5 /1/8 /14/2/3/6/4/8 /9 /15/i255/16/8 /1/i255/6/17 /2/i255/2/18 /1/8 /i255/7/1/2/7
/19 /20/2/1/7/21 /2/i255/2/16/16/2/3/6/10/i255/22 /23 /24 /i255/25 /26
/25 /8 /9 /6/1/8 /13/15/10/i255/27 /2/28/5 /2/1/7/6/18 /1/2/29/i255/30/4/9 /31 /29/i255/8 /4/13/i255/5 /1/4/3/2/15/32
/23
/33/34/35/36/37/38/39/40/22 /33 /23/33 /33/33 /34/33 /35/33 /36/33 /37/33 /38/33 /39/33 /40
/25 /0/23 /35 /33 /33
/25 /0/23 /35 /33 /34
/25 /0/23 /35 /33 /35
/25 /0/23 /35 /34
/25 /0/23 /36 /35 /33
/25 /0/23 /36 /36 /33
/25 /0/23 /37 /33 /33
/25 /0/23 /37 /33 /34
/25 /0/23 /37 /34
/25 /0/23 /37 /35
/25 /0/23 /37 /36
/25 /0/23 /37 /37
/25 /0/23 /37 /38 /33
/25 /0/23 /38 /33
/25 /0/23 /38 /33 /33
/25 /0/23 /39 /33
/25 /0/23 /39 /33 /33
/25 /0/23 /39 /34 /33
/25 /0/23 /22 /33 /33
/25 /0/23 /22 /33 /34
/25 /0/23 /22 /33 /35
/25 /0/23 /22 /33 /36
/25 /0/23 /22 /35
/25 /0/23 /22 /35 /33
/25 /0/23 /22 /35 /34
/25 /0/23 /22 /35 /35
/25 /0/23 /22 /37
/25 /0/23 /22 /37 /33
/25 /0/23 /22 /37 /34
/25 /0/33 /34 /33
/25 /0/33 /34 /35 /33
/25 /0/33 /34 /35 /34
/26/41 /42 /43/44 /44 /45 /41
/0/1/2/3/4/5 /4/6/7/6/4/8 /9 /10/i255/12/4/9 /2/7/1/i255/13/8 /3/7/13/i255/5 /1/8 /14/2/3/6/4/8 /9 /15/i255/16/8 /1/i255/6/17 /2/i255/2/18 /1/8 /i255/7/1/2/7
/19 /20/2/1/7/21 /2/i255/2/16/16/2/3/6/10/i255/22 /23 /24 /i255/25 /26
/25 /8 /9 /6/1/8 /13/15/10/i255/27 /8 /9 /2/28
/29/23 /28/30/23 /23 /28/30
/31/32/33/34/30/35/36/37/22 /31 /23/31 /31/31 /32/31 /33/31 /34/31 /30/31 /35/31 /36/31 /37
/25 /0/23 /33 /31 /31
/25 /0/23 /33 /31 /32
/25 /0/23 /33 /31 /33
/25 /0/23 /33 /32
/25 /0/23 /34 /33 /31
/25 /0/23 /34 /34 /31
/25 /0/23 /30 /31 /31
/25 /0/23 /30 /31 /32
/25 /0/23 /30 /32
/25 /0/23 /30 /33
/25 /0/23 /30 /34
/25 /0/23 /30 /30
/25 /0/23 /30 /35 /31
/25 /0/23 /35 /31
/25 /0/23 /35 /31 /31
/25 /0/23 /36 /31
/25 /0/23 /36 /31 /31
/25 /0/23 /36 /32 /31
/25 /0/23 /22 /31 /31
/25 /0/23 /22 /31 /32
/25 /0/23 /22 /31 /33
/25 /0/23 /22 /31 /34
/25 /0/23 /22 /33
/25 /0/23 /22 /33 /31
/25 /0/23 /22 /33 /32
/25 /0/23 /22 /33 /33
/25 /0/23 /22 /30
/25 /0/23 /22 /30 /31
/25 /0/23 /22 /30 /32
/25 /0/31 /32 /31
/25 /0/31 /32 /33 /31
/25 /0/31 /32 /33 /32
/26/38 /39 /40/27 /27 /41 /38
Figure A.2: Precipitation: Local projections for the Euro Area (Non-Energy industrial goods)
32

/0/1/2/3/4/5 /4/6/7/6/4/8 /9 /10/i255/12/8 /3/7/13/i255/5 /1/8 /14/2/3/6/4/8 /9 /15/i255/16/8 /1/i255/6/17 /2/i255/2/18 /1/8 /i255/7/1/2/7
/19 /20/2/1/7/21 /2/i255/2/16/16/2/3/6/i255/4/9 /i255/5 /2/1/3/2/9 /6/7/21 /2/i255/5 /8 /4/9 /6/15/10/i255/22 /23 /24 /i255/25 /26
/25 /8 /9 /6/1/8 /13/15/10/i255/27 /2/28/5 /2/1/7/6/18 /1/2/29/i255/30/4/9 /31 /29/i255/8 /4/13/i255/5 /1/4/3/2/15/32
/23/33
/33/34/35/36/37/38/39/40/22 /33 /23/33 /33/33 /34/33 /35/33 /36/33 /37/33 /38/33 /39/33 /40
/25 /0/23 /36 /37 /33
/25 /0/23 /36 /37 /34
/25 /0/23 /36 /37 /35
/25 /0/23 /36 /37 /36
/25 /0/23 /36 /37 /37
/25 /0/23 /39 /34 /34
/41 /42 /43
/0/1/2/3/4/5 /4/6/7/6/4/8 /9 /10/i255/12/8 /3/7/13/i255/5 /1/8 /14/2/3/6/4/8 /9 /15/i255/16/8 /1/i255/6/17 /2/i255/2/18 /1/8 /i255/7/1/2/7
/19 /20/2/1/7/21 /2/i255/2/16/16/2/3/6/i255/4/9 /i255/5 /2/1/3/2/9 /6/7/21 /2/i255/5 /8 /4/9 /6/15/10/i255/22 /23 /24 /i255/25 /26
/25 /8 /9 /6/1/8 /13/15/10/i255/27 /8 /9 /2/28
/23/29
/29/30/31/32/33/34/35/36/22 /29 /23/29 /29/29 /30/29 /31/29 /32/29 /33/29 /34/29 /35/29 /36
/25 /0/23 /32 /33 /29
/25 /0/23 /32 /33 /30
/25 /0/23 /32 /33 /31
/25 /0/23 /32 /33 /32
/25 /0/23 /32 /33 /33
/25 /0/23 /35 /30 /30
/27 /37 /38
Figure A.3: Precipitation: Local projections for the Euro Area (Energy)
33

/0/1/2/3/4/5 /4/6/7/6/4/8 /9 /10/i255/12/8 /3/7/13/i255/5 /1/8 /14/2/3/6/4/8 /9 /15/i255/16/8 /1/i255/6/17 /2/i255/2/18 /1/8 /i255/7/1/2/7
/19 /20/2/1/7/21 /2/i255/2/16/16/2/3/6/i255/4/9 /i255/5 /2/1/3/2/9 /6/7/21 /2/i255/5 /8 /4/9 /6/15/10/i255/22 /23 /24 /i255/25 /26
/25 /8 /9 /6/1/8 /13/15/10/i255/27 /2/28/5 /2/1/7/6/18 /1/2/29/i255/30/4/9 /31 /29/i255/8 /4/13/i255/5 /1/4/3/2/15/i255/32/7/13/13/i255/4/9 /i255/13/2/20/2/13/15/33/34
/23/35
/35/36/37/38/39/40/41/42/22 /35 /23/35 /35/35 /36/35 /37/35 /38/35 /39/35 /40/35 /41/35 /42
/25 /0/23 /38 /39 /35
/25 /0/23 /38 /39 /36
/25 /0/23 /38 /39 /37
/25 /0/23 /38 /39 /38
/25 /0/23 /38 /39 /39
/25 /0/23 /41 /36 /36
/43 /44 /45
Figure A.4: Precipitation: Local projections for the Euro Area (Energy in levels)
34

/0/1/2/3/4/5 /4/6/7/6/4/8 /9 /10/i255/12/8 /3/7/13/i255/5 /1/8 /14/2/3/6/4/8 /9 /15/i255/16/8 /1/i255/6/17 /2/i255/2/18 /1/8 /i255/7/1/2/7
/19 /20/2/1/7/21 /2/i255/2/16/16/2/3/6/10/i255/22 /23 /24 /i255/25 /26
/25 /8 /9 /6/1/8 /13/15/10/i255/27 /2/28/5 /2/1/7/6/18 /1/2/29/i255/30/4/9 /31 /29/i255/8 /4/13/i255/5 /1/4/3/2/15/32
/33/23 /32/34/33 /23 /32/35 /34/23 /23 /32/35 /34
/36/35/37/38/34/39/40/41/22 /36 /23/36 /36/36 /35/36 /37/36 /38/36 /34/36 /39/36 /40/36 /41
/25 /0/23 /37 /36 /38
/25 /0/23 /38 /36
/25 /0/23 /38 /37 /35
/25 /0/23 /38 /38 /35
/25 /0/23 /38 /38 /37
/25 /0/23 /38 /38 /38
/25 /0/23 /34 /37 /37
/25 /0/23 /34 /39 /35
/25 /0/23 /39 /35
/25 /0/23 /39 /37
/25 /0/23 /40 /35 /37
/25 /0/23 /40 /35 /38
/25 /0/23 /40 /37 /36
/25 /0/23 /40 /37 /35
/25 /0/23 /40 /37 /37
/25 /0/23 /40 /37 /34
/25 /0/23 /40 /37 /39
/25 /0/23 /41 /36
/25 /0/23 /22 /36 /34
/25 /0/23 /22 /38 /36
/25 /0/23 /22 /38 /35
/25 /0/23 /22 /39
/25 /0/36 /36 /36 /36
/25 /0/36 /36 /36 /35
/25 /0/36 /36 /35
/25 /0/36 /35 /36 /36
/25 /0/36 /35 /38
/25 /0/36 /35 /34 /35
/25 /0/36 /35 /34 /37
/25 /0/36 /35 /34 /38
/25 /0/36 /35 /34 /34
/25 /0/36 /35 /40
/42/43/44 /45
/0/1/2/3/4/5 /4/6/7/6/4/8 /9 /10/i255/12/8 /3/7/13/i255/5 /1/8 /14/2/3/6/4/8 /9 /15/i255/16/8 /1/i255/6/17 /2/i255/2/18 /1/8 /i255/7/1/2/7
/19 /20/2/1/7/21 /2/i255/2/16/16/2/3/6/10/i255/22 /23 /24 /i255/25 /26
/25 /8 /9 /6/1/8 /13/15/10/i255/27 /8 /9 /2/28
/29/23 /28/30 /31/23/23 /28/30 /31
/32/30/33/34/31/35/36/37/22 /32 /23/32 /32/32 /30/32 /33/32 /34/32 /31/32 /35/32 /36/32 /37
/25 /0/23 /33 /32 /34
/25 /0/23 /34 /32
/25 /0/23 /34 /33 /30
/25 /0/23 /34 /34 /30
/25 /0/23 /34 /34 /33
/25 /0/23 /34 /34 /34
/25 /0/23 /31 /33 /33
/25 /0/23 /31 /35 /30
/25 /0/23 /35 /30
/25 /0/23 /35 /33
/25 /0/23 /36 /30 /33
/25 /0/23 /36 /30 /34
/25 /0/23 /36 /33 /32
/25 /0/23 /36 /33 /30
/25 /0/23 /36 /33 /33
/25 /0/23 /36 /33 /31
/25 /0/23 /36 /33 /35
/25 /0/23 /37 /32
/25 /0/23 /22 /32 /31
/25 /0/23 /22 /34 /32
/25 /0/23 /22 /34 /30
/25 /0/23 /22 /35
/25 /0/32 /32 /32 /32
/25 /0/32 /32 /32 /30
/25 /0/32 /32 /30
/25 /0/32 /30 /32 /32
/25 /0/32 /30 /34
/25 /0/32 /30 /31 /30
/25 /0/32 /30 /31 /33
/25 /0/32 /30 /31 /34
/25 /0/32 /30 /31 /31
/25 /0/32 /30 /36
/38/39/40 /41
Figure A.5: Precipitation: Local projections for the Euro Area (Services)
35

/0 /1/2 /3 /4/1/i255/6/4/7 /8/4/9/8/2 /10 /11/i255/12/2 /13/4/1/i255/14 /6/2 /15/16/13/9/8/2 /10 /17/i255/18/2 /6/i255/9/19 /16/i255/16/20 /6/2 /i255/4/6/16/4
/21 /22/16/6/4/23 /16/i255/16/18/18/16/13/9/i255/8/10 /i255/14 /16/6/13/16/10 /9/4/23 /16/i255/14 /2 /8/10 /9/17/11/i255/24 /25 /26 /i255/27 /28
/27 /2 /10 /9/6/2 /1/17/11/i255/29 /16/30/14 /16/6/4/9/20 /6/16/31 /i255/14 /6/16/13/8/14 /8/9/4/9/8/2 /10 /31 /i255/32/8/10 /7 /31 /i255/2 /8/1/i255/14 /6/8/13/16/17/33
/34/25 /33/25 /35/25 /25 /33/25 /35
/36/37/38/39/35/40/41/42/24 /36 /25/36 /36/36 /37/36 /38/36 /39/36 /35/36 /40/36 /41/36 /42
/27 /43/25 /36 /36 /36
/27 /43/25 /36 /36 /37
/27 /43/25 /36 /36 /38
/27 /43/25 /36 /36 /39
/27 /43/25 /36 /36 /35
/27 /43/25 /36 /36 /40
/27 /43/25 /36 /36 /41
/27 /43/25 /36 /36 /42
/27 /43/25 /36 /36 /24
/27 /43/25 /36 /37 /36
/27 /43/25 /36 /37 /37
/27 /43/25 /37 /36 /36
/27 /43/25 /37 /36 /37
/27 /43/25 /37 /36 /38
/27 /43/25 /37 /37
/44/45/45/46
/0 /1/2 /3 /4/1/i255/6/4/7 /8/4/9/8/2 /10 /11/i255/12/2 /13/4/1/i255/14 /6/2 /15/16/13/9/8/2 /10 /17/i255/18/2 /6/i255/9/19 /16/i255/16/20 /6/2 /i255/4/6/16/4
/21 /22/16/6/4/23 /16/i255/16/18/18/16/13/9/i255/8/10 /i255/14 /16/6/13/16/10 /9/4/23 /16/i255/14 /2 /8/10 /9/17/11/i255/24 /25 /26 /i255/27 /28
/27 /2 /10 /9/6/2 /1/17/11/i255/29 /2 /10 /16/30
/31 /25 /30/25 /32/31 /25 /30/25 /33 /32/25 /25 /30/25 /33 /32
/34/33/35/36/32/37/38/39/24 /34 /25/34 /34/34 /33/34 /35/34 /36/34 /32/34 /37/34 /38/34 /39
/27 /40/25 /34 /34 /34
/27 /40/25 /34 /34 /33
/27 /40/25 /34 /34 /35
/27 /40/25 /34 /34 /36
/27 /40/25 /34 /34 /32
/27 /40/25 /34 /34 /37
/27 /40/25 /34 /34 /38
/27 /40/25 /34 /34 /39
/27 /40/25 /34 /34 /24
/27 /40/25 /34 /33 /34
/27 /40/25 /34 /33 /33
/27 /40/25 /33 /34 /34
/27 /40/25 /33 /34 /33
/27 /40/25 /33 /34 /35
/27 /40/25 /33 /33
/41/42/42/43
Figure A.6: Global Radiation: Local projections for the Euro Area (Food)
36

/0/1 /2 /3 /4/i255/6/7 /8/9/10/i255/11 /12/7 /13/14/8/15/1/7 /2 /16/i255/17/7 /12/i255/15/18 /14/i255/14/19 /12/7 /i255/9/12/14/9
/20 /21/14/12/9/22 /14/i255/14/17/17/14/8/15/4/i255/23 /24 /25 /i255/26 /27
/26 /7 /2 /15/12/7 /10/16/4/i255/28 /14/29/11 /14/12/9/15/19 /12/14/30/i255/31 /12/14/8/1/11 /1/15/9/15/1/7 /2 /30/i255/32/1/2 /3 /30/i255/7 /1/10/i255/11 /12/1/8/14/16/33
/24/24 /33/24 /34 /35/24 /33/24 /35
/36/34/37/38/35/39/40/41/23 /36 /24/36 /36/36 /34/36 /37/36 /38/36 /35/36 /39/36 /40/36 /41
/26 /31 /24 /37 /36 /38
/26 /31 /24 /38 /36
/26 /31 /24 /38 /37 /34
/26 /31 /24 /38 /38 /34
/26 /31 /24 /38 /38 /37
/26 /31 /24 /38 /38 /38
/26 /31 /24 /35 /37 /37
/26 /31 /24 /35 /39 /34
/26 /31 /24 /39 /34
/26 /31 /24 /39 /37
/26 /31 /24 /40 /34 /37
/26 /31 /24 /40 /34 /38
/26 /31 /24 /40 /37 /36
/26 /31 /24 /40 /37 /34
/26 /31 /24 /40 /37 /37
/26 /31 /24 /40 /37 /35
/26 /31 /24 /40 /37 /39
/26 /31 /24 /41 /36
/26 /31 /24 /23 /36 /35
/26 /31 /24 /23 /38 /36
/26 /31 /24 /23 /38 /34
/26 /31 /24 /23 /39
/26 /31 /36 /36 /36 /36
/26 /31 /36 /36 /36 /34
/26 /31 /36 /36 /34
/26 /31 /36 /34 /36 /36
/26 /31 /36 /34 /38
/26 /31 /36 /34 /35 /34
/26 /31 /36 /34 /35 /37
/26 /31 /36 /34 /35 /38
/26 /31 /36 /34 /35 /35
/26 /31 /36 /34 /40
/42/43/44 /45
/0 /1/2 /3 /4/1/i255/6/4/7 /8/4/9/8/2 /10 /11/i255/12/2 /13/4/1/i255/14 /6/2 /15/16/13/9/8/2 /10 /17/i255/18/2 /6/i255/9/19 /16/i255/16/20 /6/2 /i255/4/6/16/4
/21 /22/16/6/4/23 /16/i255/16/18/18/16/13/9/11/i255/24 /25 /26 /i255/27 /28
/27 /2 /10 /9/6/2 /1/17/11/i255/29 /16/30/14 /16/6/4/9/20 /6/16/31 /i255/32/6/16/13/8/14 /8/9/4/9/8/2 /10 /31 /i255/33/8/10 /7 /31 /i255/2 /8/1/i255/14 /6/8/13/16/17/34
/35/25 /36/35 /25 /34/25 /37 /38/25 /25 /34/25 /37 /38/25 /34/25 /38
/39/37/40/41/38/42/43/44/24 /39 /25/39 /39/39 /37/39 /40/39 /41/39 /38/39 /42/39 /43/39 /44
/27 /32/25 /40 /39 /41
/27 /32/25 /41 /39
/27 /32/25 /41 /40 /37
/27 /32/25 /41 /41 /37
/27 /32/25 /41 /41 /40
/27 /32/25 /41 /41 /41
/27 /32/25 /38 /40 /40
/27 /32/25 /38 /42 /37
/27 /32/25 /42 /37
/27 /32/25 /42 /40
/27 /32/25 /43 /37 /40
/27 /32/25 /43 /37 /41
/27 /32/25 /43 /40 /39
/27 /32/25 /43 /40 /37
/27 /32/25 /43 /40 /40
/27 /32/25 /43 /40 /38
/27 /32/25 /43 /40 /42
/27 /32/25 /44 /39
/27 /32/25 /24 /39 /38
/27 /32/25 /24 /41 /39
/27 /32/25 /24 /41 /37
/27 /32/25 /24 /42
/27 /32/39 /39 /39 /39
/27 /32/39 /39 /39 /37
/27 /32/39 /39 /37
/27 /32/39 /37 /39 /39
/27 /32/39 /37 /41
/27 /32/39 /37 /38 /37
/27 /32/39 /37 /38 /40
/27 /32/39 /37 /38 /41
/27 /32/39 /37 /38 /38
/27 /32/39 /37 /43
/45/46/47 /48
Figure A.7: Solar Radiation: Local projections for the Euro Area (Services - max and min)
37

/0 /1/2 /3 /4/1/i255/6/4/7 /8/4/9/8/2 /10 /11/i255/12/2 /13/4/1/i255/14 /6/2 /15/16/13/9/8/2 /10 /17/i255/18/2 /6/i255/9/19 /16/i255/16/20 /6/2 /i255/4/6/16/4
/21 /22/16/6/4/23 /16/i255/16/18/18/16/13/9/11/i255/24 /25 /26 /i255/27 /28
/27 /2 /10 /9/6/2 /1/17/11/i255/29 /2 /10 /16/30
/31 /25 /30/25 /32/31 /25 /30/25 /33 /32/25
/34/33/35/36/32/37/38/39/24 /34 /25/34 /34/34 /33/34 /35/34 /36/34 /32/34 /37/34 /38/34 /39
/27 /40/25 /35 /34 /34
/27 /40/25 /35 /34 /33
/27 /40/25 /35 /34 /35
/27 /40/25 /35 /33
/27 /40/25 /36 /35 /34
/27 /40/25 /36 /36 /34
/27 /40/25 /32 /34 /34
/27 /40/25 /32 /34 /33
/27 /40/25 /32 /33
/27 /40/25 /32 /35
/27 /40/25 /32 /36
/27 /40/25 /32 /32
/27 /40/25 /32 /37 /34
/27 /40/25 /37 /34
/27 /40/25 /37 /34 /34
/27 /40/25 /38 /34
/27 /40/25 /38 /34 /34
/27 /40/25 /38 /33 /34
/27 /40/25 /24 /34 /34
/27 /40/25 /24 /34 /33
/27 /40/25 /24 /34 /35
/27 /40/25 /24 /34 /36
/27 /40/25 /24 /35
/27 /40/25 /24 /35 /34
/27 /40/25 /24 /35 /33
/27 /40/25 /24 /35 /35
/27 /40/25 /24 /32
/27 /40/25 /24 /32 /34
/27 /40/25 /24 /32 /33
/27 /40/34 /33 /34
/27 /40/34 /33 /35 /34
/27 /40/34 /33 /35 /33
/28/0 /41 /42/29 /29 /43 /0
Figure A.8: Global Radiation: Local projections for the Euro Area (Non-Energy industrial goods)
38

/0 /1/2 /3 /4/1/i255/6/4/7 /8/4/9/8/2 /10 /11/i255/12/2 /13/4/1/i255/14 /6/2 /15/16/13/9/8/2 /10 /17/i255/18/2 /6/i255/9/19 /16/i255/16/20 /6/2 /i255/4/6/16/4
/21 /22/16/6/4/23 /16/i255/16/18/18/16/13/9/i255/8/10 /i255/14 /16/6/13/16/10 /9/4/23 /16/i255/14 /2 /8/10 /9/17/11/i255/24 /25 /26 /i255/27 /28
/27 /2 /10 /9/6/2 /1/17/11/i255/29 /16/30/14 /16/6/4/9/20 /6/16/31 /i255/32/6/16/13/8/14 /8/9/4/9/8/2 /10 /31 /i255/33/8/10 /7 /31 /i255/2 /8/1/i255/14 /6/8/13/16/17/34
/25/25 /34/25 /35/25 /34/36
/36/37/38/39/35/40/41/42/24 /36 /25/36 /36/36 /37/36 /38/36 /39/36 /35/36 /40/36 /41/36 /42
/27 /32/25 /39 /35 /36
/27 /32/25 /39 /35 /37
/27 /32/25 /39 /35 /38
/27 /32/25 /39 /35 /39
/27 /32/25 /39 /35 /35
/27 /32/25 /41 /37 /37
/43 /44 /0
/0 /1/2 /3 /4/1/i255/6/4/7 /8/4/9/8/2 /10 /11/i255/12/2 /13/4/1/i255/14 /6/2 /15/16/13/9/8/2 /10 /17/i255/18/2 /6/i255/9/19 /16/i255/16/20 /6/2 /i255/4/6/16/4
/21 /22/16/6/4/23 /16/i255/16/18/18/16/13/9/i255/8/10 /i255/14 /16/6/13/16/10 /9/4/23 /16/i255/14 /2 /8/10 /9/17/11/i255/24 /25 /26 /i255/27 /28
/27 /2 /10 /9/6/2 /1/17/11/i255/29 /2 /10 /16/30
/25/25 /30/25 /31/25 /30/32
/32/33/34/35/31/36/37/38/24 /32 /25/32 /32/32 /33/32 /34/32 /35/32 /31/32 /36/32 /37/32 /38
/27 /39/25 /35 /31 /32
/27 /39/25 /35 /31 /33
/27 /39/25 /35 /31 /34
/27 /39/25 /35 /31 /35
/27 /39/25 /35 /31 /31
/27 /39/25 /37 /33 /33
/29 /40 /0
Figure A.9: Global Radiation: Local projections for the Euro Area (Energy)
39

/0 /1/2 /3 /4/1/i255/6/4/7 /8/4/9/8/2 /10 /11/i255/12/2 /13/4/1/i255/14 /6/2 /15/16/13/9/8/2 /10 /17/i255/18/2 /6/i255/9/19 /16/i255/16/20 /6/2 /i255/4/6/16/4
/21 /22/16/6/4/23 /16/i255/16/18/18/16/13/9/11/i255/24 /25 /26 /i255/27 /28
/27 /2 /10 /9/6/2 /1/17/11/i255/29 /2 /10 /16/30
/31 /25 /30/25 /32 /33/25 /25 /30/25 /32 /33/25 /30/25 /33
/34/32/35/36/33/37/38/39/24 /34 /25/34 /34/34 /32/34 /35/34 /36/34 /33/34 /37/34 /38/34 /39
/27 /40/25 /35 /34 /36
/27 /40/25 /36 /34
/27 /40/25 /36 /35 /32
/27 /40/25 /36 /36 /32
/27 /40/25 /36 /36 /35
/27 /40/25 /36 /36 /36
/27 /40/25 /33 /35 /35
/27 /40/25 /33 /37 /32
/27 /40/25 /37 /32
/27 /40/25 /37 /35
/27 /40/25 /38 /32 /35
/27 /40/25 /38 /32 /36
/27 /40/25 /38 /35 /34
/27 /40/25 /38 /35 /32
/27 /40/25 /38 /35 /35
/27 /40/25 /38 /35 /33
/27 /40/25 /38 /35 /37
/27 /40/25 /39 /34
/27 /40/25 /24 /34 /33
/27 /40/25 /24 /36 /34
/27 /40/25 /24 /36 /32
/27 /40/25 /24 /37
/27 /40/34 /34 /34 /34
/27 /40/34 /34 /34 /32
/27 /40/34 /34 /32
/27 /40/34 /32 /34 /34
/27 /40/34 /32 /36
/27 /40/34 /32 /33 /32
/27 /40/34 /32 /33 /35
/27 /40/34 /32 /33 /36
/27 /40/34 /32 /33 /33
/27 /40/34 /32 /38
/41/42/43 /44
Figure A.10: Global Radiation: Local projections for the Euro Area (Services)
40

/0/1 /2 /3 /4/i255/6/7 /8/9/10/i255/11 /12/7 /13/14/8/15/1/7 /2 /16/i255/17/7 /12/i255/15/18 /14/i255/14/19 /12/7 /i255/9/12/14/9
/20 /21/14/12/9/22 /14/i255/14/17/17/14/8/15/i255/1/2 /i255/11 /14/12/8/14/2 /15/9/22 /14/i255/11 /7 /1/2 /15/16/4/i255/23 /24 /25 /i255/26 /27
/26 /7 /2 /15/12/7 /10/16/4/i255/28 /14/29/11 /14/12/9/15/19 /12/14/30/i255/11 /12/14/8/1/11 /1/15/9/15/1/7 /2 /30/i255/7 /1/10/i255/11 /12/1/8/14/16/31
/24
/32/33/34/35/36/37/38/39/23 /32 /24/32 /32/32 /33/32 /34/32 /35/32 /36/32 /37/32 /38/32 /39
/26 /40/24 /32 /32 /32
/26 /40/24 /32 /32 /33
/26 /40/24 /32 /32 /34
/26 /40/24 /32 /32 /35
/26 /40/24 /32 /32 /36
/26 /40/24 /32 /32 /37
/26 /40/24 /32 /32 /38
/26 /40/24 /32 /32 /39
/26 /40/24 /32 /32 /23
/26 /40/24 /32 /33 /32
/26 /40/24 /32 /33 /33
/26 /40/24 /33 /32 /32
/26 /40/24 /33 /32 /33
/26 /40/24 /33 /32 /34
/26 /40/24 /33 /33
/41/42/42/43
Figure A.11: Wind: Local projections for the Euro Area (Food)
41

/0/1 /2 /3 /4/i255/6/7 /8/9/10/i255/11 /12/7 /13/14/8/15/1/7 /2 /16/i255/17/7 /12/i255/15/18 /14/i255/14/19 /12/7 /i255/9/12/14/9
/20 /21/14/12/9/22 /14/i255/14/17/17/14/8/15/4/i255/23 /24 /25 /i255/26 /27
/26 /7 /2 /15/12/7 /10/16/4/i255/28 /14/29/11 /14/12/9/15/19 /12/14/30/i255/31 /12/14/8/1/11 /1/15/9/15/1/7 /2 /30/i255/7 /1/10/i255/11 /12/1/8/14/16/32
/24/24 /32/33
/34/35/36/37/33/38/39/40/23 /34 /24/34 /34/34 /35/34 /36/34 /37/34 /33/34 /38/34 /39/34 /40
/26 /31 /24 /36 /34 /34
/26 /31 /24 /36 /34 /35
/26 /31 /24 /36 /34 /36
/26 /31 /24 /36 /35
/26 /31 /24 /37 /36 /34
/26 /31 /24 /37 /37 /34
/26 /31 /24 /33 /34 /34
/26 /31 /24 /33 /34 /35
/26 /31 /24 /33 /35
/26 /31 /24 /33 /36
/26 /31 /24 /33 /37
/26 /31 /24 /33 /33
/26 /31 /24 /33 /38 /34
/26 /31 /24 /38 /34
/26 /31 /24 /38 /34 /34
/26 /31 /24 /39 /34
/26 /31 /24 /39 /34 /34
/26 /31 /24 /39 /35 /34
/26 /31 /24 /23 /34 /34
/26 /31 /24 /23 /34 /35
/26 /31 /24 /23 /34 /36
/26 /31 /24 /23 /34 /37
/26 /31 /24 /23 /36
/26 /31 /24 /23 /36 /34
/26 /31 /24 /23 /36 /35
/26 /31 /24 /23 /36 /36
/26 /31 /24 /23 /33
/26 /31 /24 /23 /33 /34
/26 /31 /24 /23 /33 /35
/26 /31 /34 /35 /34
/26 /31 /34 /35 /36 /34
/26 /31 /34 /35 /36 /35
/27/41 /42 /43/44 /44 /45 /41
Figure A.12: Wind: Local projections for the Euro Area (Non-Energy industrial goods)
42

/0/1 /2 /3 /4/i255/6/7 /8/9/10/i255/11 /12/7 /13/14/8/15/1/7 /2 /16/i255/17/7 /12/i255/15/18 /14/i255/14/19 /12/7 /i255/9/12/14/9
/20 /21/14/12/9/22 /14/i255/14/17/17/14/8/15/i255/1/2 /i255/11 /14/12/8/14/2 /15/9/22 /14/i255/11 /7 /1/2 /15/16/4/i255/23 /24 /25 /i255/26 /27
/26 /7 /2 /15/12/7 /10/16/4/i255/28 /14/29/11 /14/12/9/15/19 /12/14/30/i255/31 /12/14/8/1/11 /1/15/9/15/1/7 /2 /30/i255/7 /1/10/i255/11 /12/1/8/14/16/32
/24/33
/34/33/35/36/37/38/39/40/23 /34 /24/34 /34/34 /33/34 /35/34 /36/34 /37/34 /38/34 /39/34 /40
/26 /31 /24 /36 /37 /34
/26 /31 /24 /36 /37 /33
/26 /31 /24 /36 /37 /35
/26 /31 /24 /36 /37 /36
/26 /31 /24 /36 /37 /37
/26 /31 /24 /39 /33 /33
/41 /42 /43
Figure A.13: Wind: Local projections for the Euro Area (Energy)
43

/0/1 /2 /3 /4/i255/6/7 /8/9/10/i255/11 /12/7 /13/14/8/15/1/7 /2 /16/i255/17/7 /12/i255/15/18 /14/i255/14/19 /12/7 /i255/9/12/14/9
/20 /21/14/12/9/22 /14/i255/14/17/17/14/8/15/4/i255/23 /24 /25 /i255/26 /27
/26 /7 /2 /15/12/7 /10/16/4/i255/28 /14/29/11 /14/12/9/15/19 /12/14/30/i255/31 /12/14/8/1/11 /1/15/9/15/1/7 /2 /30/i255/7 /1/10/i255/11 /12/1/8/14/16/32
/24/33
/33/34/35/36/37/38/39/40/23 /33 /24/33 /33/33 /34/33 /35/33 /36/33 /37/33 /38/33 /39/33 /40
/26 /31 /24 /35 /33 /36
/26 /31 /24 /36 /33
/26 /31 /24 /36 /35 /34
/26 /31 /24 /36 /36 /34
/26 /31 /24 /36 /36 /35
/26 /31 /24 /36 /36 /36
/26 /31 /24 /37 /35 /35
/26 /31 /24 /37 /38 /34
/26 /31 /24 /38 /34
/26 /31 /24 /38 /35
/26 /31 /24 /39 /34 /35
/26 /31 /24 /39 /34 /36
/26 /31 /24 /39 /35 /33
/26 /31 /24 /39 /35 /34
/26 /31 /24 /39 /35 /35
/26 /31 /24 /39 /35 /37
/26 /31 /24 /39 /35 /38
/26 /31 /24 /40 /33
/26 /31 /24 /23 /33 /37
/26 /31 /24 /23 /36 /33
/26 /31 /24 /23 /36 /34
/26 /31 /24 /23 /38
/26 /31 /33 /33 /33 /33
/26 /31 /33 /33 /33 /34
/26 /31 /33 /33 /34
/26 /31 /33 /34 /33 /33
/26 /31 /33 /34 /36
/26 /31 /33 /34 /37 /34
/26 /31 /33 /34 /37 /35
/26 /31 /33 /34 /37 /36
/26 /31 /33 /34 /37 /37
/26 /31 /33 /34 /39
/41/42/43 /44
/0/1 /2 /3 /4/i255/6/7 /8/9/10/i255/11 /12/7 /13/14/8/15/1/7 /2 /16/i255/17/7 /12/i255/15/18 /14/i255/14/19 /12/7 /i255/9/12/14/9
/20 /21/14/12/9/22 /14/i255/14/17/17/14/8/15/4/i255/23 /24 /25 /i255/26 /27
/26 /7 /2 /15/12/7 /10/16/4/i255/28 /7 /2 /14/29
/30/24 /29/31/30 /24 /29/32 /31/24/24 /29/32 /31
/33/32/34/35/31/36/37/38/23 /33 /24/33 /33/33 /32/33 /34/33 /35/33 /31/33 /36/33 /37/33 /38
/26 /39/24 /34 /33 /35
/26 /39/24 /35 /33
/26 /39/24 /35 /34 /32
/26 /39/24 /35 /35 /32
/26 /39/24 /35 /35 /34
/26 /39/24 /35 /35 /35
/26 /39/24 /31 /34 /34
/26 /39/24 /31 /36 /32
/26 /39/24 /36 /32
/26 /39/24 /36 /34
/26 /39/24 /37 /32 /34
/26 /39/24 /37 /32 /35
/26 /39/24 /37 /34 /33
/26 /39/24 /37 /34 /32
/26 /39/24 /37 /34 /34
/26 /39/24 /37 /34 /31
/26 /39/24 /37 /34 /36
/26 /39/24 /38 /33
/26 /39/24 /23 /33 /31
/26 /39/24 /23 /35 /33
/26 /39/24 /23 /35 /32
/26 /39/24 /23 /36
/26 /39/33 /33 /33 /33
/26 /39/33 /33 /33 /32
/26 /39/33 /33 /32
/26 /39/33 /32 /33 /33
/26 /39/33 /32 /35
/26 /39/33 /32 /31 /32
/26 /39/33 /32 /31 /34
/26 /39/33 /32 /31 /35
/26 /39/33 /32 /31 /31
/26 /39/33 /32 /37
/40/41/42 /43
Figure A.14: Wind: Local projections for the Euro Area (Services)
44

Figure A.15: Temperature: Local projections for the Euro Area (Food)
45

Figure A.16: Temperature: Local projections for the Euro Area (Food)
46

Figure A.17: Temperature: Local projections for the Euro Area (Food)
47

Figure A.18: Temperature: Local projections for the Euro Area (Food - Max and Min)
48

Figure A.19: Temperature: Local projections for the Euro Area (Non-Energy industrial goods)
49

Figure A.20: Temperature: Local projections for the Euro Area (Non-Energy - Max and Min)
50

Figure A.21: Temperature: Local projections for the Euro Area (Energy)
51

Figure A.22: Temperature: Local projections for the Euro Area (Energy - Max and Min)
52

Figure A.23: Temperature: Local projections for the Euro Area (Services)
53

Figure A.24: Temperature: Local projections for the Euro Area (Services). Left panel: Maximum temperature, right panel: Minimum
temperature
54

Table A.1: Average deviation from historical mean of different weather variables for the euro area countries, i.e., threshold values used
above which the observed deviations are considered as shocks.
Country Temperature Precipitation Wind speed Solar radiation Minimum Temperature Maximum Temperature
AT 1.40 0.06 1.11 2.93 1.32 1.42
BE 1.39 0.02 1.99 7.44 1.15 1.82
CY NA NA NA NA NA NA
DE 1.33 -0.02 1.90 4.38 0.91 1.58
EE 1.62 0.23 1.51 4.18 1.64 1.64
EL 0.25 0.04 1.33 NA 0.51 0.06
ES 1.22 -0.10 1.45 NA 0.93 1.55
FI 1.55 0.20 1.59 NA 1.84 1.54
FR 1.37 0.00 1.72 2.18 1.11 1.53
HR 1.26 0.07 1.04 3.91 1.01 1.62
IE 0.74 0.09 2.04 NA 0.85 0.61
IT 1.23 -0.05 1.51 -0.06 1.23 1.64
LT 1.52 0.09 1.68 5.69 1.13 1.28
LU 1.09 -0.02 1.86 4.77 0.59 1.93
L V 1.59 0.13 1.53 4.85 1.40 1.53
MT NA NA NA NA NA NA
NL 1.33 0.21 2.16 8.37 1.02 1.56
PT 1.02 -0.38 1.49 NA 1.07 1.37
SI 1.29 0.10 0.60 5.64 1.16 1.73
SK 1.35 -0.07 1.29 4.18 1.38 1.28
EA 1.30 0.02 2.60 1.96 2.20 1.00
55

Table A.2: Standard deviation of deviation from historical mean for euro area countries.
Country Temperature Precipitation Wind speed Solar radiation Minimum Temperature Maximum Temperature
AT 1.74 1.01 0.19 15.63 1.50 2.09
BE 1.62 1.06 0.52 15.90 1.52 1.94
CY NA NA NA NA NA NA
DE 1.70 0.82 0.41 15.51 1.53 2.05
EE 2.38 0.83 0.37 14.94 2.65 2.28
EL 1.45 0.98 0.17 NA 1.35 1.56
ES 1.23 0.72 0.24 NA 1.23 1.45
FI 2.47 0.58 0.33 NA 2.78 2.29
FR 1.50 0.91 0.36 14.25 1.37 1.79
HR 1.73 1.41 0.18 15.44 1.56 2.02
IE 1.08 1.42 0.46 NA 1.14 1.18
IT 1.20 1.08 0.19 13.29 1.19 1.37
LT 2.27 0.77 0.35 15.37 2.46 2.31
LU 1.67 1.11 0.48 16.91 1.55 2.07
L V 2.31 0.74 0.29 15.16 2.57 2.27
MT NA NA NA NA NA NA
NL 1.59 1.02 0.57 14.73 1.53 1.85
PT 1.18 1.54 0.28 NA 1.27 1.50
SI 1.68 1.95 0.15 16.96 1.57 2.04
SK 1.78 0.94 0.25 15.87 1.75 1.95
EA 1.2 0.45 0.3 10.3
56

Table A.3: Correlation of weather variables
Weather variables Correlation coefficient
Temperature & Solar Radiation 0.86
Temperature & Wind: Deviation 0.34
Temperature & Solar Radiation: Deviation 0.32
Precipitation & Wind: Deviation 0.07
Precipitation & Wind 0.05
Wind & Sun: Deviation 0.01
Temperature & Wind 0.00
Wind & Solar Radiation -0.04
Temperature & Precipitation -0.07
Precipitation & Solar Radiation -0.26
Precipitation & Solar Radiation: Deviation -0.62
57
